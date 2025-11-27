"""
New vulnerable code to test PR blocking.
"""

import subprocess
import os

# High severity: Command injection
def execute_user_command(user_input):
    subprocess.call(user_input, shell=True)

# High severity: Hardcoded AWS credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# High severity: SQL injection
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return query

# Medium severity: Weak random
import random
def generate_token():
    return random.randint(1000, 9999)
