
# Simple Port Scanner

A simple Python script to scan open ports on one or multiple target systems. This tool is ideal for basic network troubleshooting or educational purposes.

---

## Features

- Scan a single target or multiple targets simultaneously.
- Define the range of ports to scan (e.g., ports 1-100).
- Outputs open ports in real-time for each scanned target.

---

## Prerequisites

Before using this script, ensure you have the following installed:

- **Python 3.x**  
- **termcolor** module for colored terminal output:  
  Install it using:  
  ```bash
  pip install termcolor
  ```

---

## Usage

### Run the Script

1. Clone this repository and navigate to the script location.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Execute the script in your terminal:
   ```bash
   python port_scanner.py
   ```

3. Provide input when prompted:
   - **Targets**: Enter IP addresses or hostnames to scan, separated by commas for multiple targets.
   - **Port Range**: Enter the number of ports to scan (e.g., `100` scans ports 1 through 100).

### Example Output

#### **Single Target**
```plaintext
[*] Enter Targets To Scan(split them by ,): 192.168.1.1
[*] Enter How Many Ports You Want To Scan: 50

Starting Scan For 192.168.1.1
[+] Port Opened 22
[+] Port Opened 80
```

#### **Multiple Targets**
```plaintext
[*] Enter Targets To Scan(split them by ,): 192.168.1.1, 192.168.1.2
[*] Enter How Many Ports You Want To Scan: 20

[*] Scanning Multiple Targets

Starting Scan For 192.168.1.1
[+] Port Opened 22

Starting Scan For 192.168.1.2
[+] Port Opened 80
```

---

## Important Notes

1. **Responsible Use**  
   Ensure you have permission before scanning any target. Unauthorized scanning may violate laws and ethical guidelines.

2. **Limitations**  
   - This script uses TCP connection attempts to detect open ports, which might be slower and less stealthy compared to advanced tools.
   - Does not perform advanced scans (e.g., UDP, banner grabbing).

3. **Error Handling**  
   The script ignores errors when a port is closed or inaccessible to ensure clean output.

4. **Customization**  
   Feel free to extend the script with features like threading for faster scans or scanning specific port ranges.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this script.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse of this tool.
