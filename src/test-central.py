"""
Test file to verify cross-repo reusable workflows.
Central workflows are in apcode-1/central-repo
"""

import subprocess
import os

# Semgrep should catch these
def cmd_injection(user_input):
    subprocess.call(user_input, shell=True)

def dangerous_eval(code):
    return eval(code)

def system_exec(cmd):
    os.system(cmd)

# No real secrets here - TruffleHog only catches verified ones
