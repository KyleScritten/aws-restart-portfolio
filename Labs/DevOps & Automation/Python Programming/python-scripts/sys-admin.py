# Python3.11  
# Coding: utf-8 

# Exercise 1: Using os.system

import os
import subprocess

os.system("ls")

# Exercise 2: Using subprocess.run

subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments

subprocess.run(["ls","-l"])

# Exercise 4: Using subprocess.run with three arguments

subprocess.run(["ls","-l","ainsulin-seq-clean.txt"])

# Exercise 5: Retrieving system information

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Exercise 6: Retrieving information about disk space

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])