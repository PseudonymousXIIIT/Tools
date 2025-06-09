# ARP Poisoning Tool

A Python tool for performing ARP spoofing attacks on local networks.

## Features

- Performs ARP poisoning between target and gateway
- Supports continuous spoofing
- Uses Scapy for packet manipulation
- Real-time network traffic redirection

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - scapy==2.5.0
- Root/Administrator privileges
- Network interface in promiscuous mode

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Arp Poision"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with root/administrator privileges:
```bash
sudo python arp_poision.py
```

When prompted, provide:
- Target IP address
- Gateway IP address

## Example

```bash
Enter the target IP address: 192.168.1.100
Enter the gateway IP address: 192.168.1.1
Poisoning 192.168.1.100 to think you are the gateway 192.168.1.1...
Poisoning 192.168.1.1 to think you are the target 192.168.1.100...
```

## Notes

- Requires root/administrator privileges to run
- Only use on networks you own or have permission to test
- May cause network disruption if used improperly
- Some networks may have ARP protection mechanisms

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to test the target network and comply with all applicable laws and regulations.
