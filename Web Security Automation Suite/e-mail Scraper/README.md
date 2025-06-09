# Email Scraper

A Python tool for extracting email addresses from websites and web pages.

## Features

- Extracts email addresses from web pages
- Recursively crawls through linked pages
- Handles various email formats
- Supports multiple URL processing

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - beautifulsoup4==4.12.2
  - requests==2.31.0
  - lxml==4.9.3

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "e-mail Scraper"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python email-scrapper.py
```

When prompted:
1. Enter the target URL to scan
2. The script will automatically:
   - Crawl the website
   - Extract email addresses
   - Display found emails

## Example

```bash
[+] Enter Target URL To Scan: https://example.com
[1] Processing https://example.com
[2] Processing https://example.com/about
...
```

## Notes

- The script will stop after processing 100 URLs to prevent excessive crawling
- Use responsibly and in accordance with website terms of service
- Some websites may block automated scraping attempts

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to scrape websites and comply with their terms of service and robots.txt files.

---

© 2025 Email Scraper - All rights reserved.
