#!/usr/bin/python3

"""
Downloader

Download a any file from the internet
"""

import pyfiglet, argparse, requests

# setup argument list
parser = argparse.ArgumentParser(prog="Downloader", description="Download any file from the internet", epilog="By Flavio Moreira")
parser.add_argument("--url", "-u", type=str, required=True, help="URL to the file to download")
parser.add_argument("--output", "-o", type=str, help="Name of the file to save")

class Downloader:
    pass

downloader = Downloader()
parser.parse_args(namespace=downloader)

#print(f"{downloader.url} {downloader.output}")
