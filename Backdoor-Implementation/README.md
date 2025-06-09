# Backdoor Implementation

A Python-based backdoor tool for educational purposes.

## Features

- Remote command execution
- File upload and download capabilities
- Directory navigation
- Persistent connection
- JSON-based communication

## Requirements

- Python 3.x
- No external dependencies required (uses standard library)
- Network access between client and server

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Backdoor Implementation"
```

3. No additional package installation required

## Usage

The tool consists of two components:

### Server (Control Center)
```bash
python server.py
```

### Client (Target Machine)
```bash
python backdoor.py
```

## Configuration

Before running the client, modify the following in `backdoor.py`:
- Replace 'LHOST' with the server's IP address
- Replace 'LPORT' with the desired port number

## Available Commands

- `exit`: Close the connection
- `clear`: Clear the terminal
- `cd <directory>`: Change directory
- `download <filename>`: Download a file from target
- `upload <filename>`: Upload a file to target
- Any other command will be executed on the target system

## Notes

- The client will attempt to reconnect every 20 seconds if connection is lost
- All communication is done using JSON format
- File transfers use binary mode
- Use responsibly and only on systems you own or have permission to test

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to access the target system and comply with all applicable laws and regulations.
