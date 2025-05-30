#!/usr/bin/env python3

import sys
import requests
from colorama import Fore, Style

def green(t):
    return Fore.GREEN + t + Style.RESET_ALL

def red(t):
    return Fore.RED + t + Style.RESET_ALL

def search(kw):
    fkw = kw.replace(" ","+")
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={fkw}'

    req = requests.get(url)

    if req.status_code != 200:
        print("Error. Try again.")
        return

    data = req.json()
    vulns = data.get("vulnerabilities", [])
    for vuln in vulns:
        cve = vuln.get("cve", {})
        cve_id = cve.get("id", "N/A")
        descriptions = cve.get("descriptions", [])
        description = descriptions[0]["value"] if descriptions else "No descriptions."
        print(green(cve_id) + ": " + red(description) + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./cvsearch.py <keyword>")
        sys.exit(1)

    keywords = " ".join(sys.argv[1:])
    search(keywords)
