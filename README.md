DeepEnum & Bug Bounty Directory Generator

A practical, automation-focused toolkit for bug bounty reconnaissance and subdomain enumeration, designed for real-world offensive security workflows.

This repository contains two complementary tools:

Bug Bounty Directory Generator – A standardized, repeatable directory structure for organizing reconnaissance, scans, loot, and reports.

DeepEnum – A deep subdomain enumeration and validation engine combining multiple sources, DNS checks, HTTP probing, and live result hosting.

This is not a toy project. It is built for people who actually hunt.

Features
Bug Bounty Directory Generator

Creates a clean, structured recon workspace per target

Consistent folder layout aligned with real bug bounty methodology

Auto-generated README files per module

Optional safe removal of existing target directories

Permission handling for pentesting environments (Kali / Linux)

Generated structure includes:

Subdomain reconnaissance

Information gathering

Vulnerability scanning

Content discovery

Screenshots

Loot collection

Reporting

DeepEnum – Subdomain Enumeration Engine

Multi-source subdomain enumeration:

subfinder

assetfinder

findomain

crt.sh

Automatic result merging and de-duplication

Optional IP resolution with wildcard detection

HTTP status probing using httpx

Out-of-scope filtering

Concurrent DNS resolution

Local HTTP server to browse results

Clean, Kali-style terminal output with system info

Why This Exists (Honest Version)

Most recon scripts online are:

Messy

Half-automated

Hard to extend

Not aligned with real reporting workflows

This project fixes that by enforcing:

Structure

Repeatability

Tool chaining

Output clarity

If you are serious about bug bounty, organization and automation matter as much as payloads.

Requirements
System

Linux (Kali Linux recommended)

Python 3.8+

Python Dependencies
pip install termcolor colorama tqdm pyfiglet

External Tools (Must Be Installed)
subfinder
assetfinder
findomain
httpx
jq
curl


Make sure all tools are in your $PATH.

Installation
git clone https://github.com/yourusername/deepenum.git
cd deepenum
chmod +x *.py

Usage
1. Bug Bounty Directory Generator

Creates a structured workspace for a target.

python3 dir_generator.py -t example.com


Optional flags:

-o /path/to/output      # Custom output directory
-r                      # Remove existing target directory
-v                      # Show version


Example:

python3 dir_generator.py -t example.com -o ~/bugbounty -r

2. DeepEnum – Subdomain Enumeration

Run deep enumeration on a target domain.

python3 deepenum.py -i example.com


Optional flags:

-ip                     # Resolve IP addresses
-asn                    # (Reserved for future ASN expansion)
-out out_of_scope.txt   # Filter out-of-scope domains
-o output.txt           # Custom output file


Example:

python3 deepenum.py -i example.com -ip -out out_of_scope.txt

Output Overview

After execution, you get:

all_subdomains.txt – merged unique subdomains

httpx_output.txt – live HTTP services with status codes

Optional IP-mapped results

A local web server at:

http://localhost:8080/<target>


This makes reviewing recon results fast and visual.

Workflow Recommendation (Realistic)

Generate directory structure

Run DeepEnum inside subdomain_recon

Filter live hosts

Feed live assets into:

Nuclei

Manual testing

Burp Suite

Store findings directly under loot

Write final report in reporting

This mirrors actual professional recon pipelines.

Security & Ethics

This tool is intended only for legal and authorized testing:

Bug bounty programs

Written client permission

Lab environments

You are responsible for how you use it.
No excuses.

Roadmap

Planned improvements:

ASN enrichment

Screenshot automation integration

Passive + active recon profiles

JSON output support

Modular plugin system

Credits

Author: clipp3r

Inspiration: Real-world bug bounty workflows

Community tools: ProjectDiscovery ecosystem
