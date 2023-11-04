import socket
from colorama import Fore, Style

# List to store URLs from site.txt
urls = []

# Reading URLs from site.txt
with open('site.txt', 'r') as file:
    urls = file.read().splitlines()

# Reading ports from wordlist.txt
with open('wordlist.txt', 'r') as ports_file:
    ports = [int(port) for port in ports_file.read().splitlines()]

def check_site_reachability(url):
    try:
        socket.gethostbyname(url)
        return True
    except socket.error:
        return False

def check_port(url, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust timeout as needed
        result = sock.connect_ex((url, port))
        if result == 0:
            print(f"{Fore.GREEN}Port {port} is open on {url}{Style.RESET_ALL}")
        sock.close()
    except socket.error:
        pass

# Loop through URLs and ports
for url in urls:
    if check_site_reachability(url):
        print(f"Scanning ports for {url}")
        for port in ports:
            check_port(url, port)
    else:
        print(f"{Fore.RED}Site {url} is unreachable{Style.RESET_ALL}")

