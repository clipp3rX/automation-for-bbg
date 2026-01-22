# DeepEnum & Bug Bounty Directory Generator

A practical, automation-focused toolkit for bug bounty reconnaissance and subdomain enumeration built for real-world offensive security workflows.

This repository contains two complementary tools:

- **Bug Bounty Directory Generator** — creates a standardized, repeatable directory structure for organizing reconnaissance, scans, loot, and reports.
- **DeepEnum** — a deep subdomain enumeration and validation engine that consolidates multiple sources, validates DNS/HTTP results, and serves live results locally for quick review.

This project is intended for professionals and serious hobbyists who perform authorized security testing. It emphasizes structure, repeatability, and clarity of output to fit real reporting workflows.

---

Table of Contents
- [Features](#features)
- [Why this exists](#why-this-exists)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Directory Generator](#1-bug-bounty-directory-generator)
  - [DeepEnum](#2-deepenum--subdomain-enumeration)
- [Output Overview](#output-overview)
- [Recommended Workflow](#recommended-workflow)
- [Security & Ethics](#security--ethics)
- [Roadmap](#roadmap)
- [Credits & Author](#credits--author)
- [License](#license)

---

Features

Bug Bounty Directory Generator
- Creates a clean, consistent recon workspace per target
- Folder layout aligned with bug bounty methodology
- Auto-generated README files per module to keep notes consistent
- Optional safe removal of existing target directories
- Permission handling suitable for pentesting environments (Kali / Linux)

Generated structure includes:
- Subdomain reconnaissance
- Information gathering
- Vulnerability scanning
- Content discovery
- Screenshots
- Loot collection
- Reporting

DeepEnum — Subdomain Enumeration Engine
- Multi-source enumeration (subfinder, assetfinder, findomain, crt.sh, etc.)
- Result merging and de-duplication
- Optional IP resolution and wildcard detection
- HTTP status probing using httpx
- Out-of-scope filtering support
- Concurrent DNS resolution for speed
- Local web server to browse results
- Clean terminal output designed for Kali-style environments

---

Why this exists

Most recon scripts you’ll find are messy, half-automated, and hard to extend. This project enforces:
- Structure
- Repeatability
- Tool chaining
- Output clarity

Good organization and automation matter as much as tooling when working at scale or producing professional reports.

---

Requirements

System
- Linux (Kali recommended)

Python
- Python 3.8+

Python dependencies
Install via pip:
```
pip install termcolor colorama tqdm pyfiglet
```

External tools (must be installed and available on PATH)
- subfinder
- assetfinder
- findomain
- httpx
- jq
- curl

Ensure all required tools are in your $PATH before running DeepEnum.

---

Installation

Clone the repository and make scripts executable:
```
git clone https://github.com/clipp3rX/automation-for-bbg.git
cd automation-for-bbg
chmod +x *.py
```

(Adjust the clone URL to your fork or preferred remote if needed.)

---

Usage

1) Bug Bounty Directory Generator

Creates a structured workspace for a target domain.

Basic:
```
python3 dir_generator.py -t example.com
```

Options:
- `-t <target>`     Target domain (required)
- `-o <path>`       Custom output directory (default: current dir)
- `-r`              Remove existing target directory (use with caution)
- `-v`              Show version

Example:
```
python3 dir_generator.py -t example.com -o ~/bugbounty -r
```

2) DeepEnum — Subdomain Enumeration

Run deep enumeration on a target domain.

Basic:
```
python3 deepenum.py -i example.com
```

Options:
- `-i <target>`         Target domain (required)
- `-ip`                 Resolve IP addresses (optional)
- `-asn`                Reserved for future ASN enrichment
- `-out <file>`         File with out-of-scope domains to filter
- `-o <file>`           Custom output file for subdomain list

Example:
```
python3 deepenum.py -i example.com -ip -out out_of_scope.txt -o all_subdomains.txt
```

---

Output overview

After a typical run you should expect:
- `all_subdomains.txt` — merged, deduplicated subdomains
- `httpx_output.txt` — live HTTP services with status codes and metadata
- Optional IP-mapped results if `-ip` is used
- A local web UI at: `http://localhost:8080/<target>` for browsing results quickly

This output is designed to be fed directly into scanners like Nuclei, Burp Suite, or manual testing workflows.

---

Recommended workflow (practical)

1. Use the Directory Generator to create a workspace:
   - Keep notes, data, and artifacts structured per target.
2. Run DeepEnum inside the `subdomain_recon` directory.
3. Filter and triage live hosts from `httpx_output.txt`.
4. Feed live assets into:
   - Nuclei (automated checks)
   - Burp Suite or manual testing
5. Store validated findings in `loot/` and finalize in `reporting/`.

This mirrors professional recon pipelines and helps produce reproducible reports.

---

Security & Ethics

This tool is intended only for legal and authorized testing:
- Bug bounty programs where you have permission
- Written client permission
- Lab environments

You are responsible for how you use these tools. Do not use them on systems without explicit authorization.

---

Roadmap

Planned improvements:
- ASN enrichment and context
- Screenshot automation integration
- Separate passive + active recon profiles
- JSON output support for easier integrations
- Modular plugin system for extensibility

Contributions and suggestions are welcome—please open an issue or a PR.

---

Credits & Author

- Author: clipp3r
- Inspiration: Real-world bug bounty workflows
- Community tools: ProjectDiscovery ecosystem and other OSINT/subdomain projects

---

License

Specify your license here (e.g., MIT). If you haven’t chosen one yet, consider adding a LICENSE file.

---

Contact / Support

For issues, feature requests, or contributions, please open an issue in this repository.
