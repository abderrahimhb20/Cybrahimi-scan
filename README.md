#  Cybrahimi-scan

<div align="center">


**Advanced Port Scanner Tool**

<img width="836" height="673" alt="2025-11-06 17_58_17-kali-linux-2025 3-vmware-amd64 - VMware Workstation" src="https://github.com/user-attachments/assets/7dbe6b1f-5dbe-4526-afea-b06e1b85bf2e" />

<img width="684" height="515" alt="2025-11-06 17_58_45-kali-linux-2025 3-vmware-amd64 - VMware Workstation" src="https://github.com/user-attachments/assets/01c17642-f8f8-4bf5-9822-fe87e05e5152" />



A powerful, colorful, and user-friendly port scanning tool for network security analysis.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Legal](#-legal-disclaimer) • [Contributing](#-contributing)

</div>

---

## ✨ Features

- 🎨 **Colorful Interface** - Beautiful ASCII art logo and color-coded output
- 🚀 **Fast Scanning** - Efficient port scanning with progress tracking
- 🎯 **Customizable Range** - Scan specific port ranges or all 65,535 ports
- 🔍 **Service Detection** - Automatically identifies common services on open ports
- 📊 **Real-time Progress** - Live progress indicator during scanning
- ⌨️ **Interactive Input** - User-friendly prompts for IP address and port ranges
- 🛡️ **Error Handling** - Robust error handling and input validation
- 🎪 **Cross-Platform** - Works on Linux, Windows, and macOS

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/abderrahimhb20/Cybrahimi-scan.git
cd Cybrahimi-scan
```

### Make it Executable (Linux/macOS)

```bash
chmod +x Cybrahimi-scan.py
```

## 🚀 Usage

### Basic Usage

```bash
python3 Cybrahimi-scan.py
```

or (on Linux/macOS):

```bash
./Cybrahimi-scan.py
```

### Interactive Mode

The tool will prompt you for:
1. **Target IP Address** - Enter the IP you want to scan
2. **Port Range** (optional) - Choose custom range or scan all ports (1-65535)

### Example Session

```
[?] Enter target IP address to scan: 192.168.1.1

[?] Use custom port range? (y/n, default: n): y
[?] Start port (default: 1): 1
[?] End port (default: 65535): 1000

[*] Starting scan on: 192.168.1.1
[*] Scanning ports 1 to 1000
[*] Scan started at: 2024-11-06 14:30:15
------------------------------------------------------------
[*] Progress: 1000/1000 ports (100.0%)
[+] Port    22 is OPEN - Service: SSH
[+] Port    80 is OPEN - Service: HTTP
[+] Port   443 is OPEN - Service: HTTPS
------------------------------------------------------------
[*] Scan completed at: 2024-11-06 14:32:45

============================================================
                    SCAN RESULTS
============================================================

[+] Found 3 open port(s):

    Port    22 - SSH
    Port    80 - HTTP
    Port   443 - HTTPS

============================================================

[*] Scan complete. Thank you for using Cybrahimi-scan!
```

## 🎯 Detected Services

The scanner automatically identifies common services including:

| Port | Service | Port | Service |
|------|---------|------|---------|
| 21 | FTP | 22 | SSH |
| 23 | Telnet | 25 | SMTP |
| 53 | DNS | 80 | HTTP |
| 110 | POP3 | 143 | IMAP |
| 443 | HTTPS | 445 | SMB |
| 3306 | MySQL | 3389 | RDP |
| 5432 | PostgreSQL | 5900 | VNC |
| 8080 | HTTP-Proxy | 8443 | HTTPS-Alt |
| 27017 | MongoDB | | |

## ⚙️ Advanced Options

### Scan Specific Port Range

```
[?] Use custom port range? (y/n, default: n): y
[?] Start port (default: 1): 80
[?] End port (default: 65535): 443
```

### Interrupt Scan

Press `Ctrl+C` to stop the scan at any time. The tool will display results for ports scanned before interruption.


## ⚠️ Legal Disclaimer

**IMPORTANT**: This tool is for educational and authorized security testing purposes only.

### Legal Usage

✅ **Authorized Use:**
- Scanning your own networks and devices
- Penetration testing with written permission
- Security audits on systems you own
- Educational purposes in controlled lab environments

❌ **Unauthorized Use:**
- Scanning networks without permission
- Attempting to access systems you don't own
- Using for malicious purposes

### Responsibility

- Users are solely responsible for their actions
- Unauthorized port scanning may be **illegal** in your jurisdiction
- Always obtain proper authorization before scanning any network
- Violation of laws may result in criminal prosecution

**By using this tool, you agree to use it legally and ethically.**



## 🙏 Acknowledgments

- Inspired by classic network scanning tools
- Built with Python's standard socket library
- ASCII art created for cybersecurity aesthetics

---

<div align="center">

**⭐ Star this repository if you find it useful!**

Made with ❤️ for the cybersecurity community

</div>
