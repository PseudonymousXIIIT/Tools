# Port Scanner

A Python tool for scanning open ports on target systems.

## Features

- Scans multiple targets simultaneously
- Configurable port range
- Colored terminal output
- Simple and efficient port detection

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - termcolor==2.3.0

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Port Scanner"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python Simple_Port_scanner.py
```

When prompted, provide:
- Target IP address(es) (comma-separated for multiple targets)
- Number of ports to scan

## Example

```bash
[*] Enter Targets To Scan(split them by ,): 192.168.1.1,192.168.1.2
[*] Enter How Many Ports You Want To Scan: 1000
[*] Scanning Multiple Targets
Starting Scan For 192.168.1.1
[+] Port Opened 80
[+] Port Opened 443
Starting Scan For 192.168.1.2
[+] Port Opened 22
[+] Port Opened 80
```

## Notes

- The tool scans ports sequentially
- Multiple targets can be scanned by separating IPs with commas
- Use responsibly and only on networks you own or have permission to scan
- Some networks may block port scanning attempts

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to scan the target system and comply with all applicable laws and regulations.