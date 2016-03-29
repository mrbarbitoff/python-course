#!/usr/bin/env python3

import argparse
import os
import re
import shutil   # Here useless - seems to fail to create missing paths in dst - using os.system and shell cp without a doubt
import subprocess
import sys

# Constructing parser
parser = argparse.ArgumentParser(description='Store and compare file versions')
parser.add_argument("mode",
                    type=str,
                    choices=['store', 'diff'],
                    help='Running mode. store (to store) or diff (to compare).')
parser.add_argument("path",
                    type=str,
                    help='Path to file or directory')
    
# Processing inputs and checking folder/not folder
args = parser.parse_args()

# Checking whether ~/sad exists
if 'sad' not in subprocess.check_output('ls ~', shell=True).decode('utf-8').split('\n'):
    status_code = subprocess.call('mkdir ~/sad', shell=True)

# Storing
def store(path):
    if os.path.isdir(os.path.abspath(path)):
        status_code = subprocess.call('cp -r --parents ' + os.path.abspath(path) + ' ~/sad/', shell=True)
    else:
        status_code = subprocess.call('cp --parents ' + os.path.abspath(path) + ' ~/sad/', shell=True)

# Diffing
def diff(path):
    status_code = subprocess.call('diff ' + path + ' ~/sad/' + os.path.abspath(path), shell=True)

if args.mode == 'store':
    store(args.path)
elif args.mode == 'diff':
    diff(args.path)

