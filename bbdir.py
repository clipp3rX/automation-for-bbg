import argparse
import os
import sys
import random
from termcolor import colored

# New ASCII banner
BANNER = """
██████╗ ██╗   ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗████████╗██╗   ██╗
██╔══██╗██║   ██║██╔════╝    ██╔════╝ ██╔══██╗████╗  ██║╚══██╔══╝╚██╗ ██╔╝
██████╔╝██║   ██║██║  ███╗   ██║  ███╗███████║██╔██╗ ██║   ██║    ╚████╔╝ 
██╔═══╝ ██║   ██║██║   ██║   ██║   ██║██╔══██║██║╚██╗██║   ██║     ╚██╔╝  
██║     ╚██████╔╝╚██████╔╝   ╚██████╔╝██║  ██║██║ ╚████║   ██║      ██║   
╚═╝      ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═╝   
Bug Bounty Directory Generator
"""

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# Version
VERSION = "2.0"

def print_banner():
    """Print the banner in a random color."""
    color = random.choice(COLORS)
    print(colored(BANNER, color))

def create_directory(path):
    """Create directory with full permissions if it doesn't exist."""
    try:
        os.makedirs(path, mode=0o777, exist_ok=True)
        print(f"[+] Created directory: {path}")
    except Exception as e:
        print(f"[-] Error creating {path}: {e}")
        sys.exit(1)

def create_file(file_path, content):
    """Create a file with specified content and full permissions."""
    try:
        with open(file_path, "w") as f:
            f.write(content)
        os.chmod(file_path, 0o777)
        print(f"[+] Created file: {file_path}")
    except Exception as e:
        print(f"[-] Error creating file {file_path}: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Bug Bounty Target Reconnaissance Structure Generator",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
        epilog="""
Examples:
  %(prog)s -t example.com
  %(prog)s -t example.com -o /path/to/output -r
        """
    )
    
    parser.add_argument("-t", "--target", required=True, help="Target name (e.g., domain.com)")
    parser.add_argument("-o", "--output", default=os.getcwd(), help="Output directory (default: current directory)")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}", help="Show program version")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove existing directory if it exists")
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    
    args = parser.parse_args()

    print_banner()  # Print banner with random color

    # Main directory structure
    base_dir = os.path.join(args.output, args.target)
    directories = [
        "subdomain_recon",
        "info_gathering",
        "vulnerability_scanning",
        "content_discovery",
        "screenshots",
        "loot",
        "reporting"
    ]

    if args.remove:
        if os.path.exists(base_dir):
            os.system(f"rm -rf {base_dir}")
            print(f"[+] Removed existing directory: {base_dir}")

    # Create base directory
    create_directory(base_dir)

    # Create category directories and files
    for category in directories:
        category_path = os.path.join(base_dir, category)
        create_directory(category_path)
        
        if category == "subdomain_recon":
            create_file(os.path.join(category_path, "live_subs.txt"), "# Live Subdomains List\n\n")
            create_file(os.path.join(category_path, "200_subs.txt"), "# Subdomains with 200 Status Code\n\n")

        readme_content = f"""# {category.replace('_', ' ').title()}

## Directory Purpose
This directory contains resources related to {category.replace('_', ' ')} for target {args.target}

## Recommended Tools:
{{
- subdomain_recon: amass, sublist3r, assetfinder, dnsgen
- info_gathering: nmap, whois, waybackurls, shodan
- vulnerability_scanning: nuclei, sqlmap, xsstrike
- content_discovery: ffuf, dirsearch, gospider
- screenshots: gowitness, aquatone
}}"""
        create_file(os.path.join(category_path, "README.md"), readme_content)

    main_readme = f"""# {args.target} Bug Bounty Report

## Target Overview
**Domain:** {args.target}
**Start Date:** {os.popen('date').read().strip()}

## Structure Guide
This report follows the directory structure for bug bounty reconnaissance and reporting."""
    create_file(os.path.join(base_dir, "README.md"), main_readme)

if __name__ == "__main__":
    main()
