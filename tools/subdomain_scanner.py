#!/usr/bin/python3

"""
Subdomain scanner

provide a file with the list of subdomains

Usage:
    ex1: ./subdomain_scanner.py example.com
"""

import sys
import requests

wordlist = None 

#read file content
with open("wordlist.txt","r") as file:
    wordlist = file.read()
    wordlist = wordlist.splitlines()

#make request to each word in the list
for subdomain in wordlist:
    URL = f"http://{subdomain}.{sys.argv[1]}"
    response = None
    
    try:
        print(f"Fetching {URL}")
        response = requests.get(URL)

    except Exception as err:
        print(f"Error: {err}")

    else:
        print(f"Status {response.status_code} SUCCESS")
