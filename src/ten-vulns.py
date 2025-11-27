"""
10 vulnerabilities for testing inline annotations on Conversation tab.
"""

import subprocess
import os
import pickle

# 1. Command injection
def vuln_01(user_input):
    subprocess.call(user_input, shell=True)

# 2. Command injection variant
def vuln_02(cmd):
    os.system(cmd)

# 3. Command injection with format string
def vuln_03(filename):
    subprocess.call(f"cat {filename}", shell=True)

# 4. Pickle deserialization
def vuln_04(data):
    return pickle.loads(data)

# 5. Eval usage
def vuln_05(code):
    return eval(code)

# 6. Exec usage
def vuln_06(code):
    exec(code)

# 7. Command injection subprocess.run
def vuln_07(cmd):
    subprocess.run(cmd, shell=True)

# 8. Command injection subprocess.Popen
def vuln_08(cmd):
    subprocess.Popen(cmd, shell=True)

# 9. Command injection subprocess.check_output
def vuln_09(cmd):
    return subprocess.check_output(cmd, shell=True)

# 10. Command injection with pipe
def vuln_10(filename):
    os.system(f"cat {filename} | grep secret")
