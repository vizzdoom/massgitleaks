#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Massgitleaks Universal Installer
Cross-platform installer for massgitleaks with automatic dependency management
"""

import os
import sys
import platform
import subprocess
import urllib.request
import shutil
from pathlib import Path

class MassGitleaksInstaller:
    def __init__(self):
        self.os_type = platform.system().lower()
        self.is_kali = self.detect_kali_linux()
        self.python_cmd = self.find_python_command()
        
    def detect_kali_linux(self):
        """Detect if running on Kali Linux"""
        try:
            # Check /etc/os-release for Kali
            if os.path.exists('/etc/os-release'):
                with open('/etc/os-release', 'r') as f:
                    content = f.read().lower()
                    if 'kali' in content:
                        return True
            
            # Check /etc/debian_version and hostname
            if os.path.exists('/etc/debian_version'):
                hostname = platform.node().lower()
                if 'kali' in hostname:
                    return True
                    
        except Exception:
            pass
        return False
    
    def find_python_command(self):
        """Find the best Python command to use"""
        for cmd in ['python3', 'python', 'py']:
            if shutil.which(cmd):
                return cmd
        return 'python'  # fallback
    
    def run_command(self, cmd, check=True, capture_output=False):
        """Run a command and return the result"""
        try:
            print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
            result = subprocess.run(cmd, shell=isinstance(cmd, str), 
                                  check=check, capture_output=capture_output, 
                                  text=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e}")
            return None
    
    def check_pip_available(self):
        """Check if pip is available"""
        for pip_cmd in ['pip3', 'pip']:
            if shutil.which(pip_cmd):
                return pip_cmd
        return None
    
    def check_pipx_available(self):
        """Check if pipx is available"""
        return shutil.which('pipx') is not None
    
    def try_pypi_install(self):
        """Try to install from PyPI using different methods"""
        pip_cmd = self.check_pip_available()
        if not pip_cmd:
            print("❌ pip not found")
            return False
            
        # Method 1: Standard pip install
        print("\n🔧 Trying standard pip install...")
        result = self.run_command([pip_cmd, 'install', 'massgitleaks'], check=False)
        if result and result.returncode == 0:
            print("✅ Successfully installed massgitleaks via pip!")
            return True
        
        # Method 2: For Kali Linux - try with --break-system-packages
        if self.is_kali:
            print("\n🐉 Kali Linux detected, trying with --break-system-packages...")
            result = self.run_command([pip_cmd, 'install', 'massgitleaks', '--break-system-packages'], check=False)
            if result and result.returncode == 0:
                print("✅ Successfully installed massgitleaks on Kali Linux!")
                return True
        
        # Method 3: Try with --user flag
        print("\n👤 Trying with --user flag...")
        user_flag = '--break-system-packages --user' if self.is_kali else '--user'
        cmd = [pip_cmd, 'install', 'massgitleaks'] + user_flag.split()
        result = self.run_command(cmd, check=False)
        if result and result.returncode == 0:
            print("✅ Successfully installed massgitleaks with --user flag!")
            return True
            
        return False
    
    def try_pipx_install(self):
        """Try to install using pipx"""
        if not self.check_pipx_available():
            print("❌ pipx not available")
            return False
            
        print("\n📦 Trying pipx install...")
        result = self.run_command(['pipx', 'install', 'massgitleaks'], check=False)
        if result and result.returncode == 0:
            print("✅ Successfully installed massgitleaks via pipx!")
            return True
        return False
    
    def install_dependencies_locally(self):
        """Install dependencies locally as fallback"""
        pip_cmd = self.check_pip_available()
        if not pip_cmd:
            print("❌ Cannot install dependencies - pip not found")
            return False
            
        dependencies = ['colorama>=0.4.6', 'rich-argparse>=1.7.1']
        
        for dep in dependencies:
            print(f"📥 Installing dependency: {dep}")
            
            # Try different methods based on platform
            install_methods = []
            if self.is_kali:
                install_methods = [
                    [pip_cmd, 'install', dep, '--break-system-packages'],
                    [pip_cmd, 'install', dep, '--break-system-packages', '--user'],
                    [pip_cmd, 'install', dep, '--user']
                ]
            else:
                install_methods = [
                    [pip_cmd, 'install', dep],
                    [pip_cmd, 'install', dep, '--user']
                ]
            
            success = False
            for method in install_methods:
                result = self.run_command(method, check=False)
                if result and result.returncode == 0:
                    success = True
                    break
                    
            if not success:
                print(f"❌ Failed to install {dep}")
                return False
                
        print("✅ Dependencies installed successfully!")
        return True
    
    def download_massgitleaks_script(self):
        """Download massgitleaks.py directly"""
        url = "https://raw.githubusercontent.com/vizzdoom/massgitleaks/main/massgitleaks.py"
        
        try:
            print("📥 Downloading massgitleaks.py...")
            
            # Determine download location
            if self.os_type == 'windows':
                install_dir = Path.home() / 'massgitleaks'
            else:
                install_dir = Path.home() / '.local' / 'bin'
            
            install_dir.mkdir(parents=True, exist_ok=True)
            script_path = install_dir / 'massgitleaks.py'
            
            # Download the file
            urllib.request.urlretrieve(url, script_path)
            
            # Make executable on Unix systems
            if self.os_type != 'windows':
                os.chmod(script_path, 0o755)
                
            print(f"✅ Downloaded to: {script_path}")
            return script_path
            
        except Exception as e:
            print(f"❌ Failed to download massgitleaks.py: {e}")
            return None
    
    def create_wrapper_script(self, script_path):
        """Create a wrapper script for easy execution"""
        if self.os_type == 'windows':
            # Create .bat file for Windows
            wrapper_path = script_path.parent / 'massgitleaks.bat'
            with open(wrapper_path, 'w') as f:
                f.write(f'@echo off\n{self.python_cmd} "{script_path}" %*\n')
            print(f"✅ Created wrapper: {wrapper_path}")
        else:
            # Create shell script for Unix systems
            bin_dir = Path.home() / '.local' / 'bin'
            bin_dir.mkdir(parents=True, exist_ok=True)
            wrapper_path = bin_dir / 'massgitleaks'
            
            with open(wrapper_path, 'w') as f:
                f.write(f'#!/bin/bash\n{self.python_cmd} "{script_path}" "$@"\n')
            os.chmod(wrapper_path, 0o755)
            print(f"✅ Created wrapper: {wrapper_path}")
            
        return wrapper_path
    
    def show_usage_instructions(self, script_path, wrapper_path=None):
        """Show usage instructions"""
        print("\n" + "="*60)
        print("🎉 INSTALLATION COMPLETED!")
        print("="*60)
        
        if wrapper_path:
            print(f"You can now run massgitleaks using:")
            if self.os_type == 'windows':
                print(f"  {wrapper_path}")
                print(f"  Or add {wrapper_path.parent} to your PATH")
            else:
                print(f"  massgitleaks")
                print(f"  (Make sure ~/.local/bin is in your PATH)")
        
        print(f"\nDirect script usage:")
        print(f"  {self.python_cmd} {script_path} --help")
        
        print(f"\nExample:")
        if wrapper_path and self.os_type != 'windows':
            print(f"  massgitleaks /path/to/repositories")
        else:
            print(f"  {self.python_cmd} {script_path} /path/to/repositories")
    
    def install(self):
        """Main installation method"""
        print("🚀 Massgitleaks Universal Installer")
        print("="*50)
        print(f"OS: {self.os_type}")
        print(f"Kali Linux: {'Yes' if self.is_kali else 'No'}")
        print(f"Python: {self.python_cmd}")
        
        # Method 1: Try PyPI installation
        if self.try_pypi_install():
            print("\n🎉 Installation completed via PyPI!")
            print("You can now run: massgitleaks --help")
            return
        
        # Method 2: Try pipx installation
        if self.try_pipx_install():
            print("\n🎉 Installation completed via pipx!")
            print("You can now run: massgitleaks --help")
            return
        
        # Method 3: Fallback - manual installation
        print("\n🔧 PyPI installation failed, falling back to manual installation...")
        
        if not self.install_dependencies_locally():
            print("❌ Failed to install dependencies")
            sys.exit(1)
            
        script_path = self.download_massgitleaks_script()
        if not script_path:
            print("❌ Failed to download massgitleaks.py")
            sys.exit(1)
            
        wrapper_path = self.create_wrapper_script(script_path)
        self.show_usage_instructions(script_path, wrapper_path)

def main():
    installer = MassGitleaksInstaller()
    installer.install()

if __name__ == "__main__":
    main()
