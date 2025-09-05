

[![Python](https://img.shields.io/badge/python-3.12+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20|%20WSL%20|%20Kali%20Linux%20|%20Linux%20|%20macOS-lightgrey.svg)]()


![Example](example.jpg)

# 🔑 MASSGITLEAKS - Run Gitleaks massively

**Stop wasting time scanning repositories one by one!** 

**Massgitleaks** is a bulk [Gitleaks](https://github.com/gitleaks/gitleaks) automation scanner for penetration testers. Massgitleaks automates bulk secret scanning across multiple git repositories with intelligent version compatibility, advanced reporting, and pentester-friendly features.

**`gitleaks` approach:** Run scanner manually on each repository → waste time, miss secrets, fight with inconsistent reports and custom configs.

**`massgitleaks` approach:** Point a directory → scan ALL repositories automatically, grab reports at once, and test your configs across all repositories in the selected directory.

## Features

- **Bulk Scanning**: Pentest all repositories for secrets with a single command
- **Gitleaks Version Agnostic**: Works with both old and new ([v8.19+](https://github.com/gitleaks/gitleaks/releases/tag/v8.19.0)) Gitleaks versions automatically
- **Cross-Platform**: Windows, Linux, macOS, WSL with proper Unicode handling
- **Rich Console Output**: Colorized output with real-time progress tracking
- **Multi-Format Reporting**: Generate CSV, JSON, or multiple formats simultaneously  
- **Complete Audit Trail**: File-based logging with full scan details
- **Smart Redaction**: Percentage-based secret redaction (0-100%)
- **Easier Config Tuning**: Validate custom gitleaks configs against multiple codebases


## Installation 
### ⚙️ Requirements
- Python 3.12+
- [Gitleaks](https://github.com/gitleaks/gitleaks) installed and accessible via PATH (or binary declared via `--gitleaks-path` switch)

### 💽 Universal installer
Automatically detects your platform and handles dependency installation even on restrictive systems like Kali Linux.
```bash
git clone https://github.com/vizzdoom/massgitleaks.git
cd massgitleaks
python install.py
```

### 📦 PyPI Installation
```bash
pip install massgitleaks
```

### 🐉 Kali Linux & Restrictive Environments
```bash
pip install massgitleaks --break-system-packages
# or
pipx install massgitleaks
```

### 🔧 Development install
```bash
git clone https://github.com/vizzdoom/massgitleaks.git
cd massgitleaks
pip install -e .
```

## Example

```
PS D:\Tools\massgitleaks> python .\massgitleaks.py --help

 ███╗  ███╗ ████╗ █████╗█████╗  █████╗ ██╗██████╗██╗  █████╗ ████╗ ██╗ ██╗█████╗
 ████╗████║██╔═██╗██╔══╝██╔══╝ ██╔═══╝ ██║╚═██╔═╝██║  ██╔══╝██╔═██╗██║██╔╝██╔══╝
 ██╔███╔██║██████║█████╗█████╗ ██║ ███╗██║  ██║  ██║  ███╗  ██████║████╔╝ █████╗
 ██║╚█╔╝██║██╔═██║╚══██║╚══██║ ██║  ██║██║  ██║  ██║  ██╔╝  ██╔═██║██╔██╗ ╚══██║
 ██║ ╚╝ ██║██║ ██║█████║█████╗ ╚█████╔╝██║  ██║  ████╗█████╗██║ ██║██║ ██╗█████║
 ╚═╝    ╚═╝╚═╝ ╚═╝╚════╝╚════╝  ╚════╝ ╚═╝  ╚═╝  ╚═══╝╚════╝╚═╝ ╚═╝╚═╝ ╚═╝╚════╝

                       ╔═════════════════════════════════╗
                             RUN GITLEAKS MASSIVELY
                                      v25.1
                       ╚═════════════════════════════════╝

Usage: massgitleaks.py [-h] [--config config_file] [--report-format {csv,json,all,none}]
                       [--output-directory OUTPUT_DIRECTORY] [--redact [PERCENT]] [--gitleaks-path GITLEAKS_PATH]
                       [--debug]
                       [repos_directory]

Scan all git repositories in the specified directory for secrets using gitleaks.

Positional Arguments:
  repos_directory       Directory to scan for git repositories

Options:
  -h, --help            show this help message and exit
  --config config_file  Path to gitleaks configuration file
  --report-format {csv,json,all,none}
                        Report format: csv, json, all, or none (default: csv)
  --output-directory OUTPUT_DIRECTORY
                        Output directory for scan reports (default: same as <repos_directory>)
  --redact [PERCENT]    Redact secrets in the output. Use --redact for 100% or --redact=(0-100)
  --gitleaks-path GITLEAKS_PATH
                        Path to gitleaks executable
  --debug               Print additional debug information for troubleshooting

Basic example: massgitleaks.py /path/to/directory/with/multiple/git/repos


PS D:\Tools\massgitleaks> python .\massgitleaks.py .\test-repos\

 ███╗  ███╗ ████╗ █████╗█████╗  █████╗ ██╗██████╗██╗  █████╗ ████╗ ██╗ ██╗█████╗
 ████╗████║██╔═██╗██╔══╝██╔══╝ ██╔═══╝ ██║╚═██╔═╝██║  ██╔══╝██╔═██╗██║██╔╝██╔══╝
 ██╔███╔██║██████║█████╗█████╗ ██║ ███╗██║  ██║  ██║  ███╗  ██████║████╔╝ █████╗
 ██║╚█╔╝██║██╔═██║╚══██║╚══██║ ██║  ██║██║  ██║  ██║  ██╔╝  ██╔═██║██╔██╗ ╚══██║
 ██║ ╚╝ ██║██║ ██║█████║█████╗ ╚█████╔╝██║  ██║  ████╗█████╗██║ ██║██║ ██╗█████║
 ╚═╝    ╚═╝╚═╝ ╚═╝╚════╝╚════╝  ╚════╝ ╚═╝  ╚═╝  ╚═══╝╚════╝╚═╝ ╚═╝╚═╝ ╚═╝╚════╝

                       ╔═════════════════════════════════╗
                             RUN GITLEAKS MASSIVELY
                                      v25.1
                       ╚═════════════════════════════════╝

[i] Selected directory with repositories to scan:
"test-repos"

[i] Log file:
"test-repos\mass-gitleaks-scan-result-20250905_215819.txt"

[i] Gitleaks binary for scanning:
Binary: gitleaks (from PATH)
Version: gitleaks version 8.28.0

[i] Secrets redaction:
Secrets will not be redacted

Searching for git repositories in test-repos
Found 3 git repositories:
test-repos\leaky-repo1
test-repos\leaky-repo2
test-repos\leaky-repo3

🔬🔬🔬 [1/3] Scanning repository: leaky-repo1
[i] Executing Gitleaks to generate a CSV report
gitleaks git -v --exit-code 50 test-repos\leaky-repo1 --report-format csv --report-path test-repos\leaky-repo1-gitleaks.csv

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     oauth_token: "7f9cc25de23d1a255720b0ae4551f4044d600f46"
Secret:      7f9cc25de23d1a255720b0ae4551f4044d600f46
RuleID:      generic-api-key
Entropy:     3.713461
File:        hub
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:hub:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/hub#L4

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Sensitive.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.tugboat#L4

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Risk.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2020-03-01T02:26:39Z
Fingerprint: 8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a/cloud/.tugboat#L4

Finding:     "HEROKU_API_KEY": "7a2f9a4289e530bef6dbf31f4cbf63d5"
Secret:      7a2f9a4289e530bef6dbf31f4cbf63d5
RuleID:      generic-api-key
Entropy:     3.840018
File:        cloud/heroku.json
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/heroku.json:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/heroku.json#L4

Finding:     export MAILCHIMP_API_KEY="38c47f19e349153fa963bb3b3212fe8e-us11"
Secret:      38c47f19e349153fa963bb3b3212fe8e-us11
RuleID:      mailchimp-api-key
Entropy:     3.800292
File:        .bashrc
Line:        106
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:mailchimp-api-key:106
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L106

Finding:     export JEKYLL_GITHUB_TOKEN="c77e01c1e89682e4d4b94a059a7fd2b37ab326ed"
Secret:      c77e01c1e89682e4d4b94a059a7fd2b37ab326ed
RuleID:      generic-api-key
Entropy:     3.908695
File:        .bashrc
Line:        109
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:generic-api-key:109
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L109

Finding:     -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
Secret:      -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
RuleID:      private-key
Entropy:     6.017279
File:        .ssh/id_rsa
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.ssh/id_rsa:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.ssh/id_rsa#L1

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc # Sensitive
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX # Informative
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L2

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L2

Finding:     -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
Secret:      -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
RuleID:      private-key
Entropy:     6.024437
File:        misc-keys/cert-key.pem
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:misc-keys/cert-key.pem:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/misc-keys/cert-key.pem#L1-L28

Finding:     ...registry.npmjs.org/:_authToken=26dfe8d8-889b-4380-92ff-9c3c6ea5d930
Secret:      26dfe8d8-889b-4380-92ff-9c3c6ea5d930
RuleID:      generic-api-key
Entropy:     3.728972
File:        .npmrc
Line:        6
Commit:      9fd86d0f8888015c6ce7b22bc52597505c0f04d8
Author:      Adam Baldwin
Email:       evilpacket@gmail.com
Date:        2019-11-12T00:29:19Z
Fingerprint: 9fd86d0f8888015c6ce7b22bc52597505c0f04d8:.npmrc:generic-api-key:6
Link:        https://github.com/Plazmaz/leaky-repo/blob/9fd86d0f8888015c6ce7b22bc52597505c0f04d8/.npmrc#L6

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.tugboat#L4

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        5
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:5
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L5

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        9
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:9
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L9

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L4

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        8
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:8
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L8

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L4

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        7
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:7
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L7

Finding:     secret_key_base: e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
Secret:      e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
RuleID:      generic-api-key
Entropy:     3.922094
File:        web/ruby/secrets.yml
Line:        14
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:14
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L14

Finding:     secret_key_base: 96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
Secret:      96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
RuleID:      generic-api-key
Entropy:     3.848557
File:        web/ruby/secrets.yml
Line:        17
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:17
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L17

Finding:     ...ment.
production:
  secret_key_base: 8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
Secret:      8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
RuleID:      generic-api-key
Entropy:     3.944884
File:        web/ruby/secrets.yml
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L22

Finding:     export AWS_SECRET_ACCESS_KEY=nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        .bash_profile
Line:        12
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:12
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L12

Finding:     export HOMEBREW_GITHUB_API_TOKEN='51e61afee2c2667123fc9ed160a0a20b330c8f74'
Secret:      51e61afee2c2667123fc9ed160a0a20b330c8f74
RuleID:      generic-api-key
Entropy:     3.796439
File:        .bash_profile
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L22

Finding:     ...rt SLACK_API_TOKEN='xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
Secret:      xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
RuleID:      slack-user-token
Entropy:     4.046948
File:        .bash_profile
Line:        23
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:slack-user-token:23
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L23

9:58PM INF 21 commits scanned.
9:58PM INF scanned ~96025 bytes (96.03 KB) in 215ms
9:58PM WRN leaks found: 26

❗ Found 26 secret(s) in the repository: leaky-repo1

Report saved: test-repos\leaky-repo1-gitleaks.csv

🔬🔬🔬 [2/3] Scanning repository: leaky-repo2
[i] Executing Gitleaks to generate a CSV report
gitleaks git -v --exit-code 50 test-repos\leaky-repo2 --report-format csv --report-path test-repos\leaky-repo2-gitleaks.csv

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Risk.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2020-03-01T02:26:39Z
Fingerprint: 8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a/cloud/.tugboat#L4

Finding:     oauth_token: "7f9cc25de23d1a255720b0ae4551f4044d600f46"
Secret:      7f9cc25de23d1a255720b0ae4551f4044d600f46
RuleID:      generic-api-key
Entropy:     3.713461
File:        hub
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:hub:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/hub#L4

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc # Sensitive
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX # Informative
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L2

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Sensitive.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.tugboat#L4

Finding:     "HEROKU_API_KEY": "7a2f9a4289e530bef6dbf31f4cbf63d5"
Secret:      7a2f9a4289e530bef6dbf31f4cbf63d5
RuleID:      generic-api-key
Entropy:     3.840018
File:        cloud/heroku.json
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/heroku.json:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/heroku.json#L4

Finding:     ...registry.npmjs.org/:_authToken=26dfe8d8-889b-4380-92ff-9c3c6ea5d930
Secret:      26dfe8d8-889b-4380-92ff-9c3c6ea5d930
RuleID:      generic-api-key
Entropy:     3.728972
File:        .npmrc
Line:        6
Commit:      9fd86d0f8888015c6ce7b22bc52597505c0f04d8
Author:      Adam Baldwin
Email:       evilpacket@gmail.com
Date:        2019-11-12T00:29:19Z
Fingerprint: 9fd86d0f8888015c6ce7b22bc52597505c0f04d8:.npmrc:generic-api-key:6
Link:        https://github.com/Plazmaz/leaky-repo/blob/9fd86d0f8888015c6ce7b22bc52597505c0f04d8/.npmrc#L6

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L2

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        5
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:5
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L5

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        9
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:9
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L9

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L4

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        8
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:8
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L8

Finding:     -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
Secret:      -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
RuleID:      private-key
Entropy:     6.017279
File:        .ssh/id_rsa
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.ssh/id_rsa:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.ssh/id_rsa#L1

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.tugboat#L4

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L4

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        7
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:7
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L7

Finding:     -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
Secret:      -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
RuleID:      private-key
Entropy:     6.024437
File:        misc-keys/cert-key.pem
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:misc-keys/cert-key.pem:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/misc-keys/cert-key.pem#L1-L28

Finding:     export MAILCHIMP_API_KEY="38c47f19e349153fa963bb3b3212fe8e-us11"
Secret:      38c47f19e349153fa963bb3b3212fe8e-us11
RuleID:      mailchimp-api-key
Entropy:     3.800292
File:        .bashrc
Line:        106
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:mailchimp-api-key:106
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L106

Finding:     export JEKYLL_GITHUB_TOKEN="c77e01c1e89682e4d4b94a059a7fd2b37ab326ed"
Secret:      c77e01c1e89682e4d4b94a059a7fd2b37ab326ed
RuleID:      generic-api-key
Entropy:     3.908695
File:        .bashrc
Line:        109
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:generic-api-key:109
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L109

Finding:     export AWS_SECRET_ACCESS_KEY=nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        .bash_profile
Line:        12
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:12
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L12

Finding:     export HOMEBREW_GITHUB_API_TOKEN='51e61afee2c2667123fc9ed160a0a20b330c8f74'
Secret:      51e61afee2c2667123fc9ed160a0a20b330c8f74
RuleID:      generic-api-key
Entropy:     3.796439
File:        .bash_profile
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L22

Finding:     ...rt SLACK_API_TOKEN='xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
Secret:      xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
RuleID:      slack-user-token
Entropy:     4.046948
File:        .bash_profile
Line:        23
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:slack-user-token:23
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L23

Finding:     secret_key_base: e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
Secret:      e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
RuleID:      generic-api-key
Entropy:     3.922094
File:        web/ruby/secrets.yml
Line:        14
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:14
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L14

Finding:     secret_key_base: 96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
Secret:      96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
RuleID:      generic-api-key
Entropy:     3.848557
File:        web/ruby/secrets.yml
Line:        17
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:17
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L17

Finding:     ...ment.
production:
  secret_key_base: 8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
Secret:      8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
RuleID:      generic-api-key
Entropy:     3.944884
File:        web/ruby/secrets.yml
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L22

9:58PM INF 21 commits scanned.
9:58PM INF scanned ~96025 bytes (96.03 KB) in 189ms
9:58PM WRN leaks found: 26

❗ Found 26 secret(s) in the repository: leaky-repo2

Report saved: test-repos\leaky-repo2-gitleaks.csv

🔬🔬🔬 [3/3] Scanning repository: leaky-repo3
[i] Executing Gitleaks to generate a CSV report
gitleaks git -v --exit-code 50 test-repos\leaky-repo3 --report-format csv --report-path test-repos\leaky-repo3-gitleaks.csv

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

Finding:     oauth_token: "7f9cc25de23d1a255720b0ae4551f4044d600f46"
Secret:      7f9cc25de23d1a255720b0ae4551f4044d600f46
RuleID:      generic-api-key
Entropy:     3.713461
File:        hub
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:hub:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/hub#L4

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc # Sensitive
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX # Informative
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.s3cfg#L2

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Sensitive.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      9f1468c79df2cf13c66041692ca7f044a27a874b
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-15T00:28:47Z
Fingerprint: 9f1468c79df2cf13c66041692ca7f044a27a874b:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/9f1468c79df2cf13c66041692ca7f044a27a874b/cloud/.tugboat#L4

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d # Risk.
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2020-03-01T02:26:39Z
Fingerprint: 8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/8c99112abc3f0aa2d8cc54bd8d459525f8c7cc9a/cloud/.tugboat#L4

Finding:     api_key: 3b6311afca5bd8aac647b316704e9c6d
Secret:      3b6311afca5bd8aac647b316704e9c6d
RuleID:      generic-api-key
Entropy:     3.718139
File:        cloud/.tugboat
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.tugboat:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.tugboat#L4

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L4

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/.dockercfg
Line:        8
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/.dockercfg:generic-api-key:8
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/.dockercfg#L8

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        5
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:5
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L5

Finding:     "auth": "X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV..."
Secret:      X3Rva2VuOjEyMzQuMThqZjg0MWZrbDQwYU90dTNrLXdCbDVuaThDM2Q0QVh0QjM2V2VqZzM4MDA2WlR5TDhUOWg5VXgrWWwzdTNV...
RuleID:      generic-api-key
Entropy:     4.987430
File:        .docker/config.json
Line:        9
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.docker/config.json:generic-api-key:9
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.docker/config.json#L9

Finding:     "HEROKU_API_KEY": "7a2f9a4289e530bef6dbf31f4cbf63d5"
Secret:      7a2f9a4289e530bef6dbf31f4cbf63d5
RuleID:      generic-api-key
Entropy:     3.840018
File:        cloud/heroku.json
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/heroku.json:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/heroku.json#L4

Finding:     -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
Secret:      -----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAjosMtDUqbE1/8zxZac1t8fkh2SxGuMXHk9yxniyM2m76donW
Gcb...
RuleID:      private-key
Entropy:     6.017279
File:        .ssh/id_rsa
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.ssh/id_rsa:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.ssh/id_rsa#L1

Finding:     -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
Secret:      -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAbhr5Ivji3OE5
NynIbnH...
RuleID:      private-key
Entropy:     6.024437
File:        misc-keys/cert-key.pem
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:misc-keys/cert-key.pem:private-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/misc-keys/cert-key.pem#L1-L28

Finding:     ...registry.npmjs.org/:_authToken=26dfe8d8-889b-4380-92ff-9c3c6ea5d930
Secret:      26dfe8d8-889b-4380-92ff-9c3c6ea5d930
RuleID:      generic-api-key
Entropy:     3.728972
File:        .npmrc
Line:        6
Commit:      9fd86d0f8888015c6ce7b22bc52597505c0f04d8
Author:      Adam Baldwin
Email:       evilpacket@gmail.com
Date:        2019-11-12T00:29:19Z
Fingerprint: 9fd86d0f8888015c6ce7b22bc52597505c0f04d8:.npmrc:generic-api-key:6
Link:        https://github.com/Plazmaz/leaky-repo/blob/9fd86d0f8888015c6ce7b22bc52597505c0f04d8/.npmrc#L6

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        4
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:4
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L4

Finding:     aws_secret_access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.credentials
Line:        7
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.credentials:generic-api-key:7
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.credentials#L7

Finding:     secret_key = yLryKGwcGc3ez9G8YAnjeYMQOc
Secret:      yLryKGwcGc3ez9G8YAnjeYMQOc
RuleID:      generic-api-key
Entropy:     4.103910
File:        cloud/.s3cfg
Line:        1
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:1
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L1

Finding:     access_key = nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        cloud/.s3cfg
Line:        2
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:cloud/.s3cfg:generic-api-key:2
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/cloud/.s3cfg#L2

Finding:     export MAILCHIMP_API_KEY="38c47f19e349153fa963bb3b3212fe8e-us11"
Secret:      38c47f19e349153fa963bb3b3212fe8e-us11
RuleID:      mailchimp-api-key
Entropy:     3.800292
File:        .bashrc
Line:        106
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:mailchimp-api-key:106
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L106

Finding:     export JEKYLL_GITHUB_TOKEN="c77e01c1e89682e4d4b94a059a7fd2b37ab326ed"
Secret:      c77e01c1e89682e4d4b94a059a7fd2b37ab326ed
RuleID:      generic-api-key
Entropy:     3.908695
File:        .bashrc
Line:        109
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bashrc:generic-api-key:109
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bashrc#L109

Finding:     secret_key_base: e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
Secret:      e0ec946fcefea5ce0d4d924f3c8db11dffeb7d10b320a69133c47a9641ab7d204d22c94f10c1ce1e187c643805fec5b2d2ba...
RuleID:      generic-api-key
Entropy:     3.922094
File:        web/ruby/secrets.yml
Line:        14
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:14
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L14

Finding:     secret_key_base: 96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
Secret:      96dc2e349b1236b9e5915f1526b5e28e19a6557a88026007632c6c11da7cb5952ae55c520eb0d6fa78b972cbe8e855887f53...
RuleID:      generic-api-key
Entropy:     3.848557
File:        web/ruby/secrets.yml
Line:        17
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:17
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L17

Finding:     ...ment.
production:
  secret_key_base: 8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
Secret:      8969518770d7484053e72f09c7bd37995d79c320e618ce3ec7a44b7c43fafff1615622a01513789bff7ac7a5201c6382bb68...
RuleID:      generic-api-key
Entropy:     3.944884
File:        web/ruby/secrets.yml
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:web/ruby/secrets.yml:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/web/ruby/secrets.yml#L22

Finding:     ...rt SLACK_API_TOKEN='xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
Secret:      xoxp-858723095049-581481478633-908968721956-f16b85d1f73ef37c02323bf3fd537ea5
RuleID:      slack-user-token
Entropy:     4.046948
File:        .bash_profile
Line:        23
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:slack-user-token:23
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L23

Finding:     export AWS_SECRET_ACCESS_KEY=nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
Secret:      nAH2VzKrMrRjySLlt8HCdFU3tM2TUuUZgh39NX
RuleID:      generic-api-key
Entropy:     4.807009
File:        .bash_profile
Line:        12
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:12
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L12

Finding:     export HOMEBREW_GITHUB_API_TOKEN='51e61afee2c2667123fc9ed160a0a20b330c8f74'
Secret:      51e61afee2c2667123fc9ed160a0a20b330c8f74
RuleID:      generic-api-key
Entropy:     3.796439
File:        .bash_profile
Line:        22
Commit:      903a9caba59d2514ca1aab7129fece6be3b9b849
Author:      Dylan Katz
Email:       git@dylankatz.com
Date:        2019-11-07T05:56:54Z
Fingerprint: 903a9caba59d2514ca1aab7129fece6be3b9b849:.bash_profile:generic-api-key:22
Link:        https://github.com/Plazmaz/leaky-repo/blob/903a9caba59d2514ca1aab7129fece6be3b9b849/.bash_profile#L22

9:58PM INF 21 commits scanned.
9:58PM INF scanned ~96025 bytes (96.03 KB) in 227ms
9:58PM WRN leaks found: 26

❗ Found 26 secret(s) in the repository: leaky-repo3

Report saved: test-repos\leaky-repo3-gitleaks.csv

                 ╔═════════════════════════╗
                 ║       SCAN SUMMARY      ║
                 ╚═════════════════════════╝

             Scan  started:    2025-09-05 21:58:19
             Scan finished:    2025-09-05 21:58:21
             Scan duration:    1s ⌛

      Repositories scanned:    3 📂📂📂
 Repositories with secrets:    3 ✖️✖️✖️
       Total secrets found:   78 ❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌

      All results saved to:    test-repos
 Complete log available at:    test-repos\mass-gitleaks-scan-result-20250905_215819.txt

```

![Report files](example-run.png)
![Report files - CSV](example-csv.png)

## 🛡️ USE RESPONSIBLY
This tool is designed for authorized security testing and code auditing only.

The developer is not liable for any damages or misuse that may result from using this tool.

You have to accept this term to use or distribute this software.

## 🗯️ GET INVOLVED

Found a bug? Have a feature idea?

→ [Submit an issue](https://github.com/vizzdoom/massgitleaks/issues/new/choose)

---

<div align="center">

**Made with ❤️ for the pentesting and security community**

*Star ⭐ this repo if `massgitleaks` helped you discover secrets faster!*

</div>