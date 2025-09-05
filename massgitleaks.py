#!/usr/bin/env python3
# -*- coding: utf-8 -*-
VERSION = "25.1"

import argparse
import os
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional
import signal
import re
from colorama import Fore, Style, Back, init as colorama_init
from rich_argparse import RichHelpFormatter

class MassGitleaks:    
    
    param_repos_directory = None
    param_output_directory = None
    param_gitleaks_config = None
    param_gitleaks_path = 'gitleaks'
    param_report_format = 'csv' 
    param_redact = None
    param_debug = False
    log_file = None

    _gitleaks_version = "unknown"
    _gitleaks_uses_fallback = False 
    _log_content = []
    _repositories_found = 0
    _repositories_scanned = 0
    _repositories_with_secrets = 0
    _total_secrets_found = 0
    _scan_start_time = datetime.now()
    
    _exit_interrupted_by_user = 707
    _exit_config_file_not_exist = 10
    _exit_config_path_not_file = 11
    _exit_config_cannot_read = 12
    _exit_dir_validate_file_not_exist = 20
    _exit_dir_validate_path_not_file = 21
    _exit_dir_validate_cannot_read = 22
    _exit_dir_validate_cannot_write = 23
    _exit_no_repos = 30
    _exit_gitleaks_not_found = 40
    _exit_gitleaks_secrets_found = 50
    _exit_noargs = 60
    
    
    def __init__(self):    
        self.setup_unicode_environment()
        self.setup_custom_signal_handler()
        self.show_banner()
        self.parse_arguments()
        self.show_config()
        self._repositories = self.find_git_repositories()
        
        
    def setup_unicode_environment(self):
        try:
            # Initialize colorama for cross-platform console support
            colorama_init(autoreset=True)
            
            # Set Python IO encoding to UTF-8
            os.environ['PYTHONIOENCODING'] = 'utf-8'
            
            # Windows: Reconfigure stdout/stderr for UTF-8 (Python 3.7+ method)
            if sys.platform == "win32":
                sys.stdout.reconfigure(encoding='utf-8', errors='replace') # type: ignore
                sys.stderr.reconfigure(encoding='utf-8', errors='replace') # type: ignore
                
        except Exception:
            # Unicode setup failed, continue anyway - colorama handles most issues
            pass

    def setup_custom_signal_handler(self):
        signal.signal(signal.SIGINT, self.custom_signal_handler)
        signal.signal(signal.SIGTERM, self.custom_signal_handler)
        self._current_process = None  # Track current subprocess


    def custom_signal_handler(self, signum, frame):
        print()
        self._log("[-] Scan interrupted by user", Fore.RED, Style.BRIGHT)
        
        # Kill current subprocess if running
        if self._current_process and self._current_process.poll() is None:
            try:
                self._current_process.terminate()
                self._current_process.wait(timeout=2)
            except (subprocess.TimeoutExpired, AttributeError):
                try:
                    self._current_process.kill()
                except AttributeError:
                    pass
        
        self._print_summary()
        sys.exit(self._exit_interrupted_by_user)


    def show_banner(self):
        """Print ASCII art banner"""
        banner_logo = f"""
 ███╗  ███╗ ████╗ █████╗█████╗  █████╗ ██╗██████╗██╗  █████╗ ████╗ ██╗ ██╗█████╗
 ████╗████║██╔═██╗██╔══╝██╔══╝ ██╔═══╝ ██║╚═██╔═╝██║  ██╔══╝██╔═██╗██║██╔╝██╔══╝
 ██╔███╔██║██████║█████╗█████╗ ██║ ███╗██║  ██║  ██║  ███╗  ██████║████╔╝ █████╗
 ██║╚█╔╝██║██╔═██║╚══██║╚══██║ ██║  ██║██║  ██║  ██║  ██╔╝  ██╔═██║██╔██╗ ╚══██║
 ██║ ╚╝ ██║██║ ██║█████║█████╗ ╚█████╔╝██║  ██║  ████╗█████╗██║ ██║██║ ██╗█████║
 ╚═╝    ╚═╝╚═╝ ╚═╝╚════╝╚════╝  ╚════╝ ╚═╝  ╚═╝  ╚═══╝╚════╝╚═╝ ╚═╝╚═╝ ╚═╝╚════╝"""
        banner_appendix = f"""
                       ╔═════════════════════════════════╗
                             RUN GITLEAKS MASSIVELY      
                                      v{VERSION}          
                       ╚═════════════════════════════════╝
        """
        self._log_info(banner_logo)
        self._log_info(banner_appendix)


    def parse_arguments(self):
        RichHelpFormatter.styles["argparse.metavar"] = "blue"
        RichHelpFormatter.styles["argparse.groups"] = "dark_cyan"
        RichHelpFormatter.styles["argparse.args"] = "bright_cyan"
        parser = argparse.ArgumentParser(
            description="Scan all git repositories in the specified directory for secrets using gitleaks.",
            formatter_class=RichHelpFormatter,
            epilog="""Basic example: %(prog)s /path/to/directory/with/multiple/git/repos""",
        )
        
        parser.add_argument(
            "repos_directory",
            nargs='?',
            help="Directory to scan for git repositories"
        )
        
        parser.add_argument(
            "--config",
            metavar="config_file",
            help="Path to gitleaks configuration file"
        )
        
        parser.add_argument(
            "--report-format",
            choices=['csv', 'json', 'all', 'none'],
            default='csv',
            help="Report format: csv, json, all, or none (default: csv)"
        )

        parser.add_argument(
            "--output-directory",
            help="Output directory for scan reports (default: same as <repos_directory>)"
        )
        
        parser.add_argument(
            "--redact",
            type=int,
            nargs='?',
            const=100, # Assume 100(%) when there is no value 
            metavar='PERCENT',
            help="Redact secrets in the output. Use --redact for 100%% or --redact=(0-100)"
        )
        
        parser.add_argument(
            "--gitleaks-path",
            default='gitleaks',
            help="Path to gitleaks executable"
        )

        parser.add_argument(
            "--debug",
            action="store_true",
            help="Print additional debug information for troubleshooting"
        )
        
        args = parser.parse_args()
        
        # Show help if no directory argument provided
        if args.repos_directory is None:
            parser.print_help()
            sys.exit(self._exit_noargs)
        
        # Simple assignation of arguments to instance variables
        self.param_debug = args.debug
        self._log_debug("MODE ENABLED")
        self.param_report_format = args.report_format
        self.param_redact = args.redact  
        self.param_gitleaks_path = args.gitleaks_path
        if args.config:
            self.param_gitleaks_config = Path(args.config)
            
        # Advanced assignation of arguments to instance attributes
        self.param_repos_directory = Path(args.repos_directory)
        self._validate_directory(self.param_repos_directory, check_read=True, check_write=False)

        if args.output_directory is None:
            self.param_output_directory = self.param_repos_directory
        else:
            self.param_output_directory = self._validate_directory(Path(args.output_directory), check_read=False, check_write=True)
                    
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        redact_suffix = "-REDACTED" if self.param_redact is not None else ""
        self.log_file = self.param_repos_directory / f"mass-gitleaks-scan-result{redact_suffix}-{timestamp}.txt" 

        if args.redact is not None and not (0 <= args.redact <= 100):
            parser.error("--redact value must be between 0 and 100")
            
        self._validate_gitleaks_command()


    def show_config(self):
        self._print_config_item("Selected directory with repositories to scan:", f'"{str(self.param_repos_directory)}"')
        self._print_config_item("Log file:", f'"{str(self.log_file)}"')
        
        gitleaks_info = f"Binary: {"gitleaks (from PATH)" if self.param_gitleaks_config == None else self.param_gitleaks_path}" + f"\nVersion: {self._gitleaks_version}"
        
        # Add fallback warning if needed
        if self._gitleaks_uses_fallback:
            gitleaks_info += f"\n⚠️ Older gitleaks version detected! \n⚠️ Using 'gitleaks detect -s <repo>' fallback mode (instead gitleaks git <repo>).\n⚠️ Consider updating gitleaks binary."
            
        self._print_config_item("Gitleaks binary for scanning:", gitleaks_info)
        # Build redaction info with old gitleaks limitations warning
        if self.param_redact is not None:
            redaction_info = f"{self.param_redact}%"
            if self._gitleaks_uses_fallback:
                redaction_info += f"\n⚠️ Older gitleaks version detected!\n⚠️ Percentage redaction not supported, using 100% redaction fallback mode.\n⚠️ Consider updating gitleaks binary."
        else:
            redaction_info = 'Secrets will not be redacted'
            
        self._print_config_item("Secrets redaction:", redaction_info)


    def find_git_repositories(self) -> List[Path]:
        self._log_info(f"Searching for git repositories in {self.param_repos_directory}")
        
        repositories = []
        for git_dir in self.param_repos_directory.rglob(".git"): # type: ignore
            if git_dir.is_dir():
                repo_path = git_dir.parent
                repositories.append(repo_path) 
        self._repositories_found = len(repositories)
        
        if self._repositories_found == 0:
            self._log_fail(f"No git repositories found in {self.param_repos_directory}", newline_after=True)
            sys.exit(self._exit_no_repos)
        self._log(f"Found {self._repositories_found} git repositories:", Fore.BLUE, Style.DIM)
        self._log('\n'.join(map(str, repositories)), Fore.BLUE, Style.DIM)
        
        return repositories
    
    
    def run(self) -> None:
        for index, repo_path in enumerate(self._repositories, 1):
            self._print_repository_header(repo_path, index)
            self.scan_repository(repo_path)
        self._print_summary()
        
        
    def scan_repository(self, repo_path: Path):
        self._repositories_scanned += 1
        
        # Determine formats to generate
        if self.param_report_format == 'all':
            formats_to_generate = ['csv', 'json']  # CSV first for primary optimization
        else:
            formats_to_generate = [self.param_report_format]

        # Generate reports for each format
        reports_generated = []
        total_secrets = 0
        any_secrets_found = False

        for i, format_name in enumerate(formats_to_generate):
            # First format shows output, subsequent formats are silent
            show_output = (i == 0)
            found, report_path, count = self._generate_report(repo_path, format_name, skip_output=not show_output)
            
            # Track results
            if found:
                any_secrets_found = True
                if total_secrets == 0:  # Use count from first successful scan
                    total_secrets = count
            
            # Collect report paths  
            if report_path:
                reports_generated.append(f" • {report_path}")
                
            # Stop generating additional formats if no secrets found
            elif not found and i == 0:
                break

        # Process and display results once at the end
        self._process_scan_results(repo_path, any_secrets_found, total_secrets, None)

        # Show generated reports
        if reports_generated and any_secrets_found:
            if len(reports_generated) == 1:
                self._log(f"\nReport saved: {reports_generated[0].strip(' • ')}", Fore.CYAN, Style.DIM)
            else:
                self._log("\nReports saved:", Fore.CYAN)
                for report in reports_generated:
                    self._log(report, Fore.CYAN, Style.DIM)


    def _process_scan_results(self, repo_path: Path, secrets_found: bool, secrets_count: int, report_path: Optional[Path]) -> None:
        if secrets_found:
            self._log(f"❗ Found {secrets_count} secret(s) in the repository: {repo_path.name}", Fore.RED, Style.BRIGHT)
            self._repositories_with_secrets += 1
            self._total_secrets_found += secrets_count
        else:
            self._log(f"🛡️ No secrets found in repository {repo_path.name}", Fore.GREEN)
            
        # Handle format-specific messaging
        if self.param_report_format == 'none':
            self._log(f"No reports generated for this repository (selected report format: none)", Fore.YELLOW, Style.DIM)
        elif not secrets_found:
            self._log(f"No reports generated for this repository (no secrets found)", Fore.YELLOW, Style.DIM)


    def _build_base_gitleaks_command(self, repo_path: Path) -> List[str]:
        """Build the base gitleaks command with common options"""
        # Use 'git' subcommand if supported, otherwise fall back to 'detect'
        subcommand = "detect" if self._gitleaks_uses_fallback else "git"
        
        # Base command differs between git and detect
        if self._gitleaks_uses_fallback:
            # gitleaks detect uses -s flag for source path
            base_command = [
                self.param_gitleaks_path, subcommand, "-v", "--exit-code", str(self._exit_gitleaks_secrets_found), "-s", str(repo_path)
            ]
        else:
            # gitleaks git uses positional argument for repo path (added at the end)
            base_command = [
                self.param_gitleaks_path, subcommand, "-v", "--exit-code", str(self._exit_gitleaks_secrets_found)
            ]
        
        # Common options for both commands
        if self.param_gitleaks_config:
            base_command.extend(["--config", str(self.param_gitleaks_config)])
            
        if self.param_redact is not None:
            # Old gitleaks versions don't support percentage redaction
            if self._gitleaks_uses_fallback:
                # Old gitleaks only supports basic --redact flag (always 100%)
                base_command.append("--redact")
            else:
                # New gitleaks supports percentage redaction
                base_command.append(f"--redact={self.param_redact}")

        if self.param_debug:
            base_command.extend(["-l", "debug"])
            
        # For git subcommand, add repo path as positional argument at the end
        if not self._gitleaks_uses_fallback:
            base_command.append(str(repo_path))
            
        return base_command


    def _colorize(self, text: str, color: str = '', style: str = '', background: str = '') -> str:
        colored_text = f"{color}{background}{style}{text}"
        if color or style or background:
            colored_text += Style.RESET_ALL
        return colored_text
    
    
    def _colorize_strip_ansi_codes(self, text: str) -> str:
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)
                

    def _count_secrets_from_file(self, report_path: Path) -> int:
        """Count secrets from report file - optimized for CSV first, fallback to JSON"""
        if not report_path.exists():
            return 0
            
        try:
            if report_path.suffix == '.csv':
                # Count non-empty CSV lines (excluding header)
                with open(report_path, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                    return max(0, len(lines) - 1) if lines else 0
            elif report_path.suffix == '.json':
                # Count JSON array entries
                with open(report_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return len(data) if isinstance(data, list) else 0
            return 0
        except (json.JSONDecodeError, IOError, UnicodeDecodeError):
            return 0


    def _execute_gitleaks(self, command: List[str], description: str, skip_output = False) -> Tuple[int, str]:
        self._log(description, Fore.CYAN, Style.BRIGHT)
        self._log_debug(f"{command=}")
        self._log(" ".join(command), Fore.CYAN, Style.DIM)
        
        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
                encoding='utf-8'
            )
            
            # Track current process for signal handling
            self._current_process = process
            
            output_lines = []
            
            # Use communicate() to avoid hanging on stdout iteration
            try:
                stdout_data, _ = process.communicate()
                self._current_process = None  # Clear tracking
                
                if skip_output:
                    return process.returncode, ""
                else:
                    # Process and display output
                    output_lines = []
                    if stdout_data:
                        for line in stdout_data.splitlines():
                            line = line.rstrip()
                            
                            # Color output based on content
                            if "Finding" in line or "secret" in line.lower():
                                print(self._colorize(line, Fore.YELLOW))
                            elif "error" in line.lower():
                                print(self._colorize(line, Fore.RED))
                            elif "info" in line.lower() or "scanning" in line.lower():
                                print(self._colorize(line, Fore.BLUE, Style.DIM))
                            else:
                                print(line)
                            output_lines.append(line)
                    
                    full_output = "\n".join(output_lines)
                    self._log_write_to_file(output_lines)
                    self._log("")
                    
                    return process.returncode, full_output
            
            except KeyboardInterrupt:
                # Handle Ctrl+C during communicate()
                process.terminate()
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    process.kill()
                self._current_process = None
                raise
            
        except Exception as e:
            error_msg = f"[-] Error running command:\n{command=}\nError: {str(e)}\nDetails: {type(e).__name__}"
            self._log(error_msg, Fore.RED, Style.BRIGHT)
            return -1, str(e)
        
        
    def _generate_report(self, repo_path: Path, report_format: str, skip_output: bool = False) -> Tuple[bool, Optional[Path], int]:
        """
        Generate a single report for the specified format.
        Returns: (secrets_found, report_path, secrets_count)
        """
        repo_name = repo_path.name
        redact_suffix = "-REDACTED" if self.param_redact is not None else ""
        
        # Handle "none" format - scan without generating any output files
        if report_format == 'none':
            # Build command without report format or report path (console output only)
            command = self._build_base_gitleaks_command(repo_path)
            description = f"[i] Executing Gitleaks scan (no output files)"
            exit_code, output = self._execute_gitleaks(command, description, skip_output=skip_output)
            
            # Process results for none format
            if exit_code == self._exit_gitleaks_secrets_found:
                secrets_count = output.count('Secret:') if output else 1
                return True, None, secrets_count
            elif exit_code == 0:
                return False, None, 0
            else:
                secrets_count = output.count('Secret:') if output else 0
                return secrets_count > 0, None, secrets_count
        
        # Handle regular formats with file output
        # Create report file path
        report_path = self.param_output_directory / f"{repo_name}{redact_suffix}-gitleaks.{report_format}"  # type: ignore
        
        # Build command for this specific format
        command = self._build_base_gitleaks_command(repo_path) + [
            "--report-format", report_format,
            "--report-path", str(report_path)
        ]
        
        # Execute gitleaks
        description = f"[i] Executing Gitleaks to generate a {report_format.upper()} report"
        exit_code, output = self._execute_gitleaks(command, description, skip_output=skip_output)
        
        # Process results
        if exit_code == self._exit_gitleaks_secrets_found:
            # Count secrets from output first (more reliable than file parsing)
            secrets_count = output.count('Secret:') if output else 0
            
            # If output counting failed, try counting from file
            if secrets_count == 0:
                secrets_count = self._count_secrets_from_file(report_path)
                
            # Final fallback
            if secrets_count == 0:
                secrets_count = 1
                
            return True, report_path, secrets_count
            
        elif exit_code == 0:
            # No secrets found, remove empty report file
            if report_path.exists():
                report_path.unlink()
            return False, None, 0
            
        else:
            # Scan completed with warnings
            if report_path.exists() and report_path.stat().st_size > 0:
                return True, report_path, 0
            else:
                if report_path.exists():
                    report_path.unlink()
                return False, None, 0
         
         
    def _log(self, message='', color='', style='', background='', newline_before=False, newline_after=False) -> None:
        message = f"{"\n" * newline_before}{message}{"\n" * newline_after}"
        print(self._colorize(message, color, style, background))
        if self.log_file:
            self._log_write_to_file(self._colorize_strip_ansi_codes(message))
 
    
    def _log_dark(self, message: str, newline_before=False, newline_after=False) -> None:
        self._log(message, 
                  Fore.CYAN, 
                  Style.DIM, 
                  newline_before=newline_before, 
                  newline_after=newline_after)
        
        
    def _log_debug(self, message: str) -> None:
        if self.param_debug:
            message_formatted = '\n'.join(f"[DEBUG] {line}" for line in message.splitlines())
            self._log(message_formatted, 
                  Fore.LIGHTBLACK_EX, 
                  Style.DIM,
                  newline_before=True, 
                  newline_after=True)
        
        
    def _log_fail(self, message: str, newline_before=False, newline_after=False) -> None:
        self._log(message, 
                  Fore.RED, 
                  Style.BRIGHT,
                  newline_before=newline_before, 
                  newline_after=newline_after)
 
               
    def _log_hack(self, message: str, newline_before=False, newline_after=False) -> None:
        self._log(message, 
                  '', 
                  Style.BRIGHT,
                  Back.CYAN,
                  newline_before=newline_before, 
                  newline_after=newline_after)
 
 
    def _log_info(self, message: str, newline_before=False, newline_after=False) -> None:
        self._log(message, 
                  Fore.CYAN, 
                  Style.BRIGHT, 
                  newline_before=newline_before, 
                  newline_after=newline_after)       
       
       
    def _log_warn(self, message: str, newline_before=False, newline_after=False) -> None:
        self._log(message, 
                  Fore.YELLOW, 
                  Style.DIM, 
                  newline_before=newline_before, 
                  newline_after=newline_after)
        
    
    def _log_write_to_file(self, lines):
        if not self.log_file:
            return
            
        if isinstance(lines, str):
            lines = [lines]
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            for line in lines:
                f.write(self._colorize_strip_ansi_codes(line) + '\n')
                
                
    def _print_config_item(self, item: str, value: str) -> None:
        self._log_info(f"[i] {str(item)}")
        self._log_dark(str(value), newline_after=True)
        
        
    def _print_repository_header(self, repo_path: Path, index: int):
        self._log_hack(f"🔬🔬🔬 [{index}/{self._repositories_found}] Scanning repository: {repo_path.name}", newline_before=True)
        
        
    def _print_summary(self):
        scan_end_time = datetime.now()
        duration = scan_end_time - self._scan_start_time
        
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            duration_str = f"{hours}h {minutes}m"
        elif minutes > 0:
            duration_str = f"{minutes}m {seconds}s"
        else:
            duration_str = f"{seconds}s"
    
        self._log()
        self._log("                 ╔═════════════════════════╗                 ", Fore.BLACK, Back.CYAN, newline_before=False, newline_after=False)
        self._log("                 ║       SCAN SUMMARY      ║                 ", Fore.BLACK, Back.CYAN, newline_before=False, newline_after=False)
        self._log("                 ╚═════════════════════════╝                 ", Fore.BLACK, Back.CYAN, newline_before=False, newline_after=False)
        
        minutes_emoji = "⌛"
        if total_seconds > 60:
            minutes_emoji = "⌛" * min(total_seconds//60, 20)

        repositories_scanned_emoji = "⚠️"
        if self._repositories_scanned > 0:
            repositories_scanned_emoji = "📂" * min(self._repositories_scanned, 15)

        repositories_with_secrets_emoji = "☑️"
        if self._repositories_with_secrets > 0:
            repositories_with_secrets_emoji = "✖️" * min(self._repositories_with_secrets, 15)
   
        total_secrets_found_emoji = "✅"
        if self._total_secrets_found >0:
            total_secrets_found_emoji = "❌" * min(self._total_secrets_found, 15)

        self._log(f"""
             Scan  started:    {self._scan_start_time.strftime('%Y-%m-%d %H:%M:%S')}                           
             Scan finished:    {scan_end_time.strftime('%Y-%m-%d %H:%M:%S')} 
             Scan duration:    {duration_str} {minutes_emoji}
 
      Repositories scanned: {self._repositories_scanned:>4} {repositories_scanned_emoji}
 Repositories with secrets: {self._repositories_with_secrets:>4} {repositories_with_secrets_emoji}
       Total secrets found: {self._total_secrets_found:>4} {total_secrets_found_emoji}
       
      All results saved to:    {self.param_repos_directory}
 Complete log available at:    {self.log_file}
               """, newline_before=False, newline_after=False)  
    
    
    def _validate_gitleaks_config(self):
        if self.param_gitleaks_config:
            if not self.param_gitleaks_config.exists():
                error_msg = f"[-] Error: Configuration file does not exist: {self.param_gitleaks_config}"
                self._log(error_msg, Fore.RED, Style.BRIGHT)
                sys.exit(self._exit_config_file_not_exist)
                
            if not self.param_gitleaks_config.is_file():
                error_msg = f"[-] Error: Configuration path is not a file: {self.param_gitleaks_config}"
                self._log(error_msg, Fore.RED, Style.BRIGHT)
                sys.exit(self._exit_config_path_not_file)
                
            if not os.access(self.param_gitleaks_config, os.R_OK):
                error_msg = f"[-] Error: Cannot read configuration file: {self.param_gitleaks_config}"
                self._log(error_msg, Fore.RED, Style.BRIGHT)
                sys.exit(self._exit_config_cannot_read)
                
            self.param_gitleaks_config = self.param_gitleaks_config.resolve()
            self._log(f"[i] Configuration file", Fore.BLUE, Style.BRIGHT)
            self._log(f"{self.param_gitleaks_config}", Fore.BLUE, Style.DIM)
            self._log()
            
            
    def _validate_directory(self, directory: Path, check_read: bool = False, check_write: bool = False) -> Path:
        # NOTE: Validation of input and output directories occurs during argument parsing, before log initialization.
        # Using raw print() statements since writing to file is not yet available.
        if not directory.exists():
            self._log_fail(f"[-] Error: Directory does not exist: {directory}")
            self._log_warn(f"Select a valid directory with git repositories to scan", newline_after=True)
            sys.exit(self._exit_dir_validate_file_not_exist) 
            
        if not directory.is_dir():
            self._log_fail(f"[-] Error: Path is not a directory: {directory}")
            self._log_warn(f"Select a path to directory with git repositories inside", newline_after=True)   
            sys.exit(self._exit_dir_validate_path_not_file)
            
        if check_read and not os.access(directory, os.R_OK):
            self._log_fail(f"[-] Error: Cannot read directory: {directory}")
            self._log_warn(f"Read permission to this directory is required to scan git repositories", newline_after=True)
            sys.exit(self._exit_dir_validate_cannot_read)
            
        if check_write and not os.access(directory, os.W_OK):
            self._log_fail(f"[-] Error: Cannot write to directory: {directory}")
            self._log_warn(f"Write permission to this directory is required to write reports", newline_after=True)
            sys.exit(self._exit_dir_validate_cannot_write)
        
        return Path(directory).resolve()
            
            
    def _validate_gitleaks_command(self):
        try:
            gitleaks_version_cmd = subprocess.run(
                [self.param_gitleaks_path, "--version"],
                capture_output=True,
                text=True,
                check=False,
                encoding='utf-8'
            )

            self._log_debug(f"{gitleaks_version_cmd=}")
            
            if gitleaks_version_cmd.returncode == 0:
                output_cmd = gitleaks_version_cmd.stdout.strip()
                version_lines = output_cmd.split('\n')
                detected_version = version_lines[-1] if version_lines else "unknown"
                self._log_debug(f"{detected_version=}")
                if not detected_version.strip():
                    detected_version = version_lines[-2] if len(version_lines) > 1 else "unknown"
            else:
                detected_version = "unknown"
                
            self._gitleaks_version = detected_version
            
            # Test if gitleaks supports 'git' subcommand (preferred over 'detect')
            self._test_gitleaks_git_support()
            
            # Handle redact limitations for old gitleaks versions
            if self._gitleaks_uses_fallback and self.param_redact is not None and self.param_redact != 100:
                self.param_redact = 100
            
        except FileNotFoundError:
            self._log_fail(f"[-] Error: gitleaks not found at: {self.param_gitleaks_path}")
            self._log_warn(f"Try installing gitleaks or use --gitleaks-path to specify location")
            sys.exit(self._exit_gitleaks_not_found)


    def _test_gitleaks_git_support(self):
        """Test if gitleaks supports 'git' subcommand, set fallback flag if not."""
        try:
            # Test 'gitleaks git --help' to see if git subcommand is supported
            git_help_cmd = subprocess.run(
                [self.param_gitleaks_path, "git", "--help"],
                capture_output=True,
                text=True,
                check=False,
                encoding='utf-8',
                timeout=10
            )
            
            self._log_debug(f"gitleaks git --help returncode: {git_help_cmd.returncode}")
            self._log_debug(f"gitleaks git --help stdout: {git_help_cmd.stdout[:200]}")
            self._log_debug(f"gitleaks git --help stderr: {git_help_cmd.stderr[:200]}")
            
            # If git subcommand exists, return code should be 0
            if git_help_cmd.returncode == 0:
                self._gitleaks_uses_fallback = False
                self._log_debug("gitleaks 'git' subcommand is supported")
            else:
                self._gitleaks_uses_fallback = True
                self._log_debug("gitleaks 'git' subcommand not supported, will use 'detect' fallback")
                
        except (subprocess.TimeoutExpired, Exception) as e:
            # If any error occurs, assume git subcommand is not supported
            self._gitleaks_uses_fallback = True
            self._log_debug(f"gitleaks 'git' subcommand test failed: {e}, will use 'detect' fallback")
            

def main():
    try:
        if sys.version_info < (3, 12):
            print(f"WARNING: MassGitleaks requires Python 3.12 or higher, your environment can be unstable (Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})", )
        
        massgitleaks = MassGitleaks()
        massgitleaks.run()
    except Exception as e:
        print(f"""
 │║▌║▌▌█ A fatal error occurred - Please report an issue !! │║▌║▌▌█    
""")
        raise e


if __name__ == "__main__":
    main()
