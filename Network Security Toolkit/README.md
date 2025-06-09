# Network Security Toolkit

A collection of network security and penetration testing tools for educational purposes.

## Contents

### ARP Poisoning Tool
- Simulates man-in-the-middle attacks
- Uses Scapy for packet manipulation
- Requires root/administrator privileges
- Supports continuous spoofing

### Port Scanner
- Scans multiple targets simultaneously
- Configurable port range
- Colored terminal output
- Simple and efficient port detection

## Requirements

- Python 3.x
- Required packages:
  - scapy==2.5.0
  - termcolor==2.3.0

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Network Security Toolkit"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### ARP Poisoning Tool
```bash
sudo python arp_poision.py
```
When prompted, provide:
- Target IP address
- Gateway IP address

### Port Scanner
```bash
python Simple_Port_scanner.py
```
When prompted, provide:
- Target IP address(es) (comma-separated for multiple targets)
- Number of ports to scan

## Notes

- These tools are for educational purposes only
- Always obtain proper authorization before using
- Some networks may have protection mechanisms
- Use responsibly and ethically

## Disclaimer

This toolkit is for educational purposes only. Always ensure you have permission to test the target network and comply with all applicable laws and regulations. 