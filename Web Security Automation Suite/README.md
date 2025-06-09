# Web Security Automation Suite

A collection of web security and penetration testing tools for educational purposes.

## Contents

### Email Scraper
- Extracts email addresses from websites
- Recursively crawls through linked pages
- Handles various email formats
- Supports multiple URL processing

### Directory Discovery
- Scans web servers for common directories
- Uses wordlists for directory enumeration
- Simple and efficient directory discovery
- Supports custom wordlists

### Brute Force Tool
- Tests multiple passwords against web login forms
- Supports custom login failure detection
- Optional cookie-based authentication
- Colored terminal output

## Requirements

- Python 3.x
- Required packages:
  - beautifulsoup4==4.12.2
  - requests==2.31.0
  - lxml==4.9.3
  - termcolor==2.3.0

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Web Security Automation Suite"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Email Scraper
```bash
python email-scrapper.py
```
When prompted, enter the target URL to scan.

### Directory Discovery
```bash
python directories.py
```
When prompted, provide:
- Target URL (without http://)
- Name of your wordlist file

### Brute Force Tool
```bash
python bruteforce.py
```
When prompted, provide:
- Target page URL
- Username to test
- Password file path
- Login failure string
- Optional cookie value

## Notes

- These tools are for educational purposes only
- Always obtain proper authorization before using
- Some websites may block automated attempts
- Use responsibly and ethically

## Disclaimer

This suite is for educational purposes only. Always ensure you have permission to test the target website and comply with all applicable laws and regulations. 