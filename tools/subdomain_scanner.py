#!/usr/bin/python3

"""
Subdomain Scanner

Params:
    -w/--wordlist   : File containing words to use as subdomain
    -d/--domain/ip  : Domain or IP address ex: example.com, 125.165.2.44 
    --protocol      : Protocol to use with the domain/IP. HTTP, HTTPS, DNS
    -p/--port       : Target port default 80 for http and 443 for https
    -l/--log        : File to save the results to a log file 

Usage:
    ex1: ./subdomain_scanner.py example.com
"""

import sys
import requests
from datetime import datetime as date

# Construct a dict with the cli args
cli_args = dict({
    ("--wordlist", "wordlist.txt"),
    ("-w", "wordlist.txt"),
    ("--protocol", "http"),
    ("--port", 80),
    ("-p", 80),
    ("--log", None),
    ("-l", None),
    ("--domain", None),
    ("-d", None),
    ("--ip", None)
})

# terminate the program if no domain was passed
if len(sys.argv) < 3 or (not (cli_args["--domain"] and cli_args["-d"])):
    sys.exit()

wordlist = None 

input_file = cli_args["--wordlist"]
protocol = cli_args["--protocol"]
port     = cli_args["--port"] if cli_args["--port"] else cli_args["-p"] if cli_args["-p"] else 80 
log      = cli_args["--log"] if cli_args["--log"] else cli_args["-p"] if cli_args["-p"] else None
domain   = cli_args["--domain"] if cli_args["domain"] else cli_args["-d"] if cli_args["-d"] else None

#File Mode
READ    = "r"
WRITE   = "w"
APPEND  = "a"

# Read file content
with open(input_file, READ) as file:
    wordlist = file.read()
    wordlist = wordlist.splitlines()

# Make request to each word in the list
for subdomain in wordlist:
    URL = f"{protocol}://{subdomain}.{domain}:{port}"
    response = None
    
    try:
        print(f"Fetching {URL}")
        response = requests.get(URL)

    except Exception as err:

        # write log to log_file
        if arg_is_set(("--log","-l")):
            with open(log,APPEND) as log_file:
               log_file.write(f"{date.now()} {err}\n") 

        print(f"Error: {err}")

    else:
        print(f"Status {response.status_code} SUCCESS")
