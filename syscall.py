#!/usr/bin/env python3

import os
import subprocess


# all_files = subprocess.call('ls')

file_names = []
for i in os.walk('.'):
    prefix, subdir, files = i
    files_wpref = [prefix + '/' + x for x in files]
    file_names.extend(files_wpref)
    
file_names = [file_name for file_name in file_names if file_name.endswith('.py')]

code = []
for fn in file_names:
    p = subprocess.Popen(["cat", fn], stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    code.append(stdout.decode("utf-8"))
    
with open('total.py', 'w') as ofile:
     ofile.write('\n'.join(code))
