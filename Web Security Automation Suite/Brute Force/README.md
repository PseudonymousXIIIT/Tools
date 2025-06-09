# 🔓 Web Login Brute-Force Script

This Python script performs a **brute-force attack** on a web application's login form. It tries a list of passwords against a specified username and checks for login success based on a known failure message.

> ⚠️ **Disclaimer:** This tool is for **authorized testing and educational** purposes only. Unauthorized use is illegal and unethical.

---

## 🧠 How It Works

- Accepts:
  - Target URL
  - Username
  - Password list (wordlist)
  - Login failure string (used to detect failed login)
  - Optional session cookie
- Tries each password in the wordlist.
- If login fails (failure string is present), it tries the next password.
- If login succeeds (failure string not found), it reports the valid credentials.

---

## ⚙️ Requirements

- Python 3.x  
- `requests` library  
- `termcolor` for colored console output

Install dependencies:
```bash
pip install requests termcolor
```

---

## 🚀 Usage

```bash
python3 bruteforce.py
```

You will be prompted to input:
- Target login **URL**
- Target **username**
- Path to your **password list** (e.g., `rockyou.txt`)
- The **login failure string** (e.g., `"Invalid credentials"`)
- Optional cookie value for session-authenticated attempts

---

## 📄 Code Overview

- Uses `POST` (or `GET` if cookie is set) to try credentials.
- Checks response for a failure string.
- Terminates if a match is found.

---

## 🧪 Example

```
[+] Enter Page URL: https://example.com/login
[+] Enter Username For The Account To Bruteforce: admin
[+] Enter Password File To Use: passwords.txt
[+] Enter String That Occurs When Login Fails: Invalid
Enter Cookie Value(Optional):
```

Output:
```
Trying: 123456
Trying: password1
[+] Found Username: ==> admin
[+] Found Password: ==> secret123
```

---

## 📜 License

MIT License – use responsibly and legally.

---

## 🙏 Acknowledgments

Inspired by standard penetration testing techniques for training purposes.

# Brute Force Tool

A Python tool for testing web application authentication through password brute forcing.

## Features

- Tests multiple passwords against a web login form
- Supports custom login failure detection
- Optional cookie-based authentication
- Colored terminal output for better visibility

## Requirements

- Python 3.x
- Required packages (see requirements.txt):
  - requests==2.31.0
  - termcolor==2.3.0

## Installation

1. Clone the repository or download the files
2. Navigate to the tool directory:
```bash
cd "Brute Force"
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a password wordlist file
2. Run the script:
```bash
python bruteforce.py
```

3. When prompted, provide:
   - Target page URL
   - Username to test
   - Password file path
   - Login failure string
   - Optional cookie value

## Example

```bash
[+] Enter Page URL: http://example.com/login
[+] Enter Username For The Account To Bruteforce: admin
[+] Enter Password File To Use: passwords.txt
[+] Enter String That Occurs When Login Fails: "Invalid password"
Enter Cookie Value(Optional): session=abc123
```

## Notes

- The tool requires a wordlist file containing passwords to test
- The login failure string should be unique to failed login attempts
- Use responsibly and only on systems you have permission to test

## Disclaimer

This tool is for educational purposes only. Always ensure you have permission to test the target system and comply with their terms of service.
