#!/usr/bin/python3
#
# Author: Flavio Moreira
# Port Scanner
#

"""
Port Scanner
    Scan ports on a target machine to find which ports are open
"""

import socket as Socket, sys, pyfiglet, argparse

# arguments
parser = argparse.ArgumentParser(prog="Port Scanner", description="Simple script to scan open ports on a target machine.", epilog="\nPartaS by Flavio Moreira")
parser.add_argument("--targets", "--url", "-u", "-t", nargs="*", required=True, help="Target machine IP or url")
parser.add_argument("--ports", "-p", nargs="*", type=int, help="Ports to be scanned. Default 1-65535")

# represent target machine
class Target:
    pass

target = Target()

parser.parse_args(namespace=target)

#banner = pyfiglet.figlet_format("Port Scanner")
targets = target.targets
ports = target.ports if target.ports else range(1, 65535)

#socket = Socket.socket(family=Socket.AF_INET, type=Socket.SOCK_STREAM)

print(targets)