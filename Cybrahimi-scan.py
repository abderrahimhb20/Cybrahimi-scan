#!/usr/bin/python3
import sys
import socket
from datetime import datetime

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_logo():
    """Display the Cybrahimi-scan ASCII logo with colors"""
    logo = f"""{Colors.CYAN}{Colors.BOLD}
    ╔═════════════════════════════════════════════════════════════════════╗
    ║                                                                     ║
    ║   ██████╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗  ██╗██╗███╗   ███╗██╗ ║
    ║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║  ██║██║████╗ ████║██║ ║
    ║  ██║      ╚████╔╝ ██████╔╝██████╔╝███████║███████║██║██╔████╔██║██║ ║
    ║  ██║       ╚██╔╝  ██╔══██╗██╔══██╗██╔══██║██╔══██║██║██║╚██╔╝██║██║ ║
    ║  ╚██████╗   ██║   ██████╔╝██║  ██║██║  ██║██║  ██║██║██║ ╚═╝ ██║██║ ║
    ║   ╚═════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝ ║
    ║                                                                     ║{Colors.END}
    {Colors.MAGENTA}{Colors.BOLD}║              ███████╗ ██████╗ █████╗ ███╗   ██╗                     ║
    ║              ██╔════╝██╔════╝██╔══██╗████╗  ██║                     ║
    ║              ███████╗██║     ███████║██╔██╗ ██║                     ║
    ║              ╚════██║██║     ██╔══██║██║╚██╗██║                     ║
    ║              ███████║╚██████╗██║  ██║██║ ╚████║                     ║
    ║              ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                     ║{Colors.END}
    {Colors.CYAN}║                                                                     ║
    ║{Colors.YELLOW}                 Advanced Port Scanner Tool v1.0{Colors.CYAN}                     ║
    ║{Colors.WHITE}             Use only on networks you own or have{Colors.CYAN}                    ║
    ║{Colors.WHITE}                 permission to scan legally!{Colors.CYAN}                         ║
    ╚═════════════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(logo)

def probe_port(ip, port, timeout=0.5):
    """
    Probe a port on the target IP.
    Returns 0 if port is open, 1 otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result
    except Exception:
        return 1

def get_service_name(port):
    """Get common service name for well-known ports"""
    services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
        443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
        5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP-Proxy",
        8443: "HTTPS-Alt", 27017: "MongoDB"
    }
    return services.get(port, "Unknown")

def scan_ports(ip, start_port=1, end_port=65535):
    """Scan ports on target IP"""
    open_ports = []
    
    print(f"\n{Colors.BLUE}[*]{Colors.END} Starting scan on: {Colors.BOLD}{Colors.CYAN}{ip}{Colors.END}")
    print(f"{Colors.BLUE}[*]{Colors.END} Scanning ports {Colors.YELLOW}{start_port}{Colors.END} to {Colors.YELLOW}{end_port}{Colors.END}")
    print(f"{Colors.BLUE}[*]{Colors.END} Scan started at: {Colors.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
    print(f"{Colors.CYAN}" + "-" * 60 + f"{Colors.END}")
    
    total_ports = end_port - start_port + 1
    
    try:
        for i, port in enumerate(range(start_port, end_port + 1), 1):
            # Progress indicator
            if i % 1000 == 0 or i == total_ports:
                percent = (i / total_ports) * 100
                print(f"\r{Colors.YELLOW}[*]{Colors.END} Progress: {Colors.CYAN}{i}/{total_ports}{Colors.END} ports ({Colors.YELLOW}{percent:.1f}%{Colors.END})", end='')
                sys.stdout.flush()
            
            response = probe_port(ip, port)
            if response == 0:
                open_ports.append(port)
                service = get_service_name(port)
                print(f"\n{Colors.GREEN}{Colors.BOLD}[+]{Colors.END} Port {Colors.BOLD}{Colors.GREEN}{port}{Colors.END} is {Colors.GREEN}OPEN{Colors.END} - Service: {Colors.CYAN}{service}{Colors.END}")
        
        print("\n" + f"{Colors.CYAN}" + "-" * 60 + f"{Colors.END}")
        print(f"{Colors.BLUE}[*]{Colors.END} Scan completed at: {Colors.WHITE}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}{Colors.BOLD}[!]{Colors.END} Scan interrupted by user!")
        print(f"{Colors.YELLOW}[*]{Colors.END} Scanned {Colors.CYAN}{i}{Colors.END} ports before interruption")
    
    return open_ports

def main():
    """Main function"""
    print_logo()
    
    # Get target IP from user
    while True:
        ip = input(f"\n{Colors.MAGENTA}[?]{Colors.END} Enter target IP address to scan: ").strip()
        
        # Validate IP format
        try:
            socket.inet_aton(ip)
            break
        except socket.error:
            print(f"{Colors.RED}[!]{Colors.END} Invalid IP address format. Please try again.")
    
    # Optional: Custom port range
    custom_range = input(f"\n{Colors.MAGENTA}[?]{Colors.END} Use custom port range? (y/n, default: n): ").strip().lower()
    
    if custom_range == 'y':
        try:
            start = int(input(f"{Colors.MAGENTA}[?]{Colors.END} Start port (default: 1): ").strip() or "1")
            end = int(input(f"{Colors.MAGENTA}[?]{Colors.END} End port (default: 65535): ").strip() or "65535")
            
            if start < 1 or end > 65535 or start > end:
                print(f"{Colors.RED}[!]{Colors.END} Invalid range. Using default: 1-65535")
                start, end = 1, 65535
        except ValueError:
            print(f"{Colors.RED}[!]{Colors.END} Invalid input. Using default: 1-65535")
            start, end = 1, 65535
    else:
        start, end = 1, 65535
    
    # Perform the scan
    open_ports = scan_ports(ip, start, end)
    
    # Display results
    print(f"\n{Colors.CYAN}{Colors.BOLD}" + "=" * 60 + f"{Colors.END}")
    print(f"{Colors.BOLD}{Colors.WHITE}                    SCAN RESULTS{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}" + "=" * 60 + f"{Colors.END}")
    
    if open_ports:
        print(f"\n{Colors.GREEN}{Colors.BOLD}[+]{Colors.END} Found {Colors.BOLD}{Colors.GREEN}{len(open_ports)}{Colors.END} open port(s):\n")
        for port in sorted(open_ports):
            service = get_service_name(port)
            print(f"    {Colors.CYAN}Port {port:5d}{Colors.END} - {Colors.YELLOW}{service}{Colors.END}")
    else:
        print(f"\n{Colors.RED}[-]{Colors.END} No open ports found on target.")
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}" + "=" * 60 + f"{Colors.END}")
    print(f"\n{Colors.GREEN}[*]{Colors.END} Scan complete. Thank you for using {Colors.BOLD}{Colors.CYAN}Cybrahimi-scan{Colors.END}!")

if __name__ == "__main__":
    main()
