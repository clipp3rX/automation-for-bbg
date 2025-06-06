import argparse
import os
import subprocess
import sys
import socket
import platform
from time import sleep
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Emoji constants
SCAN_EMOJI = "🔍"
SAVE_EMOJI = "💾"
FILTER_EMOJI = "🚫"
SERVER_EMOJI = "🌐"
DNS_EMOJI = "📡"
HTTP_EMOJI = "📡"
WILDCARD_EMOJI = "🃏"
ERROR_EMOJI = "❌"
SUCCESS_EMOJI = "✅"

def display_kali_banner():
    """Display the DeepEnum styled banner"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # ASCII Art
    print(Fore.RED + r"""
  ____                   _____                      
 |  _ \  ___  _ __ ___  | ____|_ __ _ __ ___  _ __  
 | | | |/ _ \| '_ ` _ \ |  _| | '__| '__/ _ \| '_ \ 
 | |_| | (_) | | | | | || |___| |  | | | (_) | | | |
 |____/ \___/|_| |_| |_|_____|_|  |_|  \___/|_| |_|
""")

    # System Information
    hostname = socket.gethostname()
    os_info = platform.uname()
    kernel = os_info.release
    architecture = platform.machine()
    
    print(Fore.CYAN + "╭──────────────────────────────────────────────╮")
    print(Fore.CYAN + "│" + Fore.WHITE + "             D E E P E N U M   V 1 . 0 . 0             " + Fore.CYAN + "│")
    print(Fore.CYAN + "╰──────────────────────────────────────────────╯")
    
    print(Fore.GREEN + "\n⚡ Tool Information:")
    print(Fore.YELLOW + f"  • Tool Name  : {Fore.WHITE}DeepEnum v1.0.0")
    print(Fore.YELLOW + f"  • Author     : {Fore.WHITE}clipp3r")
    print(Fore.YELLOW + f"  • Credit     : {Fore.WHITE}lucif3r(666)")
    print(Fore.YELLOW + f"  • Repository : {Fore.WHITE}https://github.com/yourusername/deepenum")
    print(Fore.YELLOW + f"  • Description: {Fore.WHITE}Deep Subdomain Enumeration Tool")

    print(Fore.GREEN + "\n⚡ System Information:")
    print(Fore.YELLOW + f"  • Hostname   : {Fore.WHITE}{hostname}")
    print(Fore.YELLOW + f"  • OS         : {Fore.WHITE}{os_info.system} {os_info.version}")
    print(Fore.YELLOW + f"  • Kernel     : {Fore.WHITE}{kernel}")
    print(Fore.YELLOW + f"  • Architecture: {Fore.WHITE}{architecture}")
    try:
        ip_address = socket.gethostbyname(hostname)
        print(Fore.YELLOW + f"  • IP: {Fore.WHITE}{ip_address}")
    except:
        pass

    print(Fore.MAGENTA + "\n🔓 Stay Ethical - " + Fore.RED + "Hack the Planet!" + Style.RESET_ALL)
    
    print(Fore.CYAN + "\n╭──────────────────────────────────────────────╮")
    print(Fore.CYAN + "│" + Fore.BLUE + "   https://github.com/yourusername/deepenum" + " " * 4 + Fore.CYAN + "│")
    print(Fore.CYAN + "╰──────────────────────────────────────────────╯\n")

def run_command(cmd, description):
    print(f"{SCAN_EMOJI} {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"{SUCCESS_EMOJI} {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{ERROR_EMOJI} Error in {description}: {e.stderr}")
        return False

def resolve_ip(subdomain):
    try:
        return socket.gethostbyname(subdomain.strip())
    except socket.gaierror:
        return None

def main():
    display_kali_banner()
    
    parser = argparse.ArgumentParser(description="Deep Subdomain Enumeration Tool")
    parser.add_argument("-i", "--input", required=True, help="Domain to enumerate")
    parser.add_argument("-o", "--output", default="final_subdomains.txt", help="Output file name")
    parser.add_argument("-ip", action="store_true", help="Include IP resolution")
    parser.add_argument("-asn", action="store_true", help="Include ASN information")
    parser.add_argument("-out", "--out-of-scope", default="out_of_scope.txt", help="Out of scope domains file")
    args = parser.parse_args()

    domain = args.input
    output_file = args.output
    working_dir = domain
    os.makedirs(working_dir, exist_ok=True)
    os.chdir(working_dir)

    # Step 1: Subdomain Enumeration
    tools = [
        (f"subfinder -d {domain} -silent -o subfinder.txt", "Running Subfinder"),
        (f"assetfinder --subs-only {domain} > assetfinder.txt", "Running Assetfinder"),
        (f"findomain --target {domain} --output --quiet && mv {domain}.txt findomain.txt", "Running Findomain"),
        ("curl -s 'https://crt.sh/?q=%25.{}&output=json' | jq -r '.[].name_value' | sed 's/\\*\\.//g' | sort -u > crtsh.txt".format(domain), 
         "Gathering crt.sh data"),
    ]

    for cmd, desc in tqdm(tools, desc=f"{SCAN_EMOJI} Running enumeration tools"):
        run_command(cmd, desc)

    # Merge results
    print(f"{SCAN_EMOJI} Merging results...")
    subdomains = set()
    for file in ['subfinder.txt', 'assetfinder.txt', 'findomain.txt', 'crtsh.txt']:
        if os.path.exists(file):
            with open(file) as f:
                subdomains.update(f.read().splitlines())
    
    # Filter out-of-scope
    if os.path.exists(args.out_of_scope):
        print(f"{FILTER_EMOJI} Filtering out-of-scope domains...")
        with open(args.out_of_scope) as f:
            out_of_scope = set(f.read().splitlines())
        subdomains = subdomains - out_of_scope

    with open('all_subdomains.txt', 'w') as f:
        f.write('\n'.join(subdomains))

    # Wildcard detection
    print(f"{WILDCARD_EMOJI} Checking for wildcard DNS...")
    try:
        wildcard_ip = socket.gethostbyname(f"randomsubdomain123456.{domain}")
    except:
        wildcard_ip = None

    # IP Resolution
    if args.ip:
        print(f"{DNS_EMOJI} Resolving IP addresses...")
        resolved = []
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = list(tqdm(executor.map(resolve_ip, subdomains), total=len(subdomains), desc="Resolving IPs"))
        
        with open(output_file, 'w') as out_f:
            for subdomain, ip in zip(subdomains, results):
                if ip:
                    line = f"{subdomain} - {ip}"
                    if wildcard_ip and ip == wildcard_ip:
                        line += " (Wildcard)"
                    out_f.write(line + '\n')

    # HTTP Status Check
    print(f"{HTTP_EMOJI} Checking HTTP status codes...")
    run_command(f"httpx -l all_subdomains.txt -sc -mc 200,403,301,302 -o httpx_output.txt", 
               "HTTP Status Check")

    # Start HTTP Server
    print(f"{SERVER_EMOJI} Starting HTTP server...")
    os.chdir('..')
    subprocess.Popen(["python3", "-m", "http.server", "8080"], 
                    stdout=subprocess.DEVNULL, 
                    stderr=subprocess.DEVNULL)
    
    print(f"\n{SUCCESS_EMOJI} Enumeration complete!")
    print(f"Access results at: http://localhost:8080/{working_dir}")

if __name__ == "__main__":
    main()
