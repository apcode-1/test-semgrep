"""
Test file for both Semgrep and TruffleHog scanning.
"""

import subprocess
import os

# Semgrep will catch this - command injection
def run_command(user_input):
    subprocess.call(user_input, shell=True)

# Semgrep will catch this - eval
def execute_code(code):
    return eval(code)

# Semgrep will catch this - os.system
def system_call(cmd):
    os.system(cmd)
