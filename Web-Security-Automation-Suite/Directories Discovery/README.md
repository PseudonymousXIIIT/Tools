# Directories Discovery Tool

A Python tool for discovering directories and files on web servers.

## Features

- Scans web servers for common directories
- Uses a wordlist for directory enumeration
- Simple and efficient directory discovery
- Supports custom wordlists

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - requests==2.31.0

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Directories Discovery"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a wordlist file containing directory names to check
2. Run the script:
```bash
python directories.py
```

3. When prompted:
   - Enter the target URL (without http://)
   - Enter the name of your wordlist file

## Example

```bash
[*] Enter Target URL: example.com
[*] Enter Name Of The File Containing Directories: wordlist.txt
[*] Discovered Directory At This Path: example.com/admin
[*] Discovered Directory At This Path: example.com/images
```

## Notes

- The tool requires a wordlist file containing directory names to check
- Common wordlists include:
  - directory-list.txt
  - common.txt
  - dirb.txt

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to scan the target website and comply with their terms of service.
