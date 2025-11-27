"""
5 vulnerabilities to test inline annotations without PR comment.
"""

import subprocess
import os
import pickle

# 1. Command injection
def vuln_1(user_input):
    subprocess.call(user_input, shell=True)

# 2. Command injection variant
def vuln_2(cmd):
    os.system(cmd)

# 3. Pickle deserialization
def vuln_3(data):
    return pickle.loads(data)

# 4. Eval usage
def vuln_4(code):
    return eval(code)

# 5. Exec usage
def vuln_5(code):
    exec(code)
