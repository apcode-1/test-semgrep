"""
Test vulnerabilities for security scan.
"""

import subprocess
import os

def command_injection(user_input):
    # Semgrep will catch: subprocess with shell=True
    subprocess.call(user_input, shell=True)

def dangerous_eval(code):
    # Semgrep will catch: eval usage
    return eval(code)

def system_call(cmd):
    # Semgrep will catch: os.system
    os.system(cmd)
