"""
Intentionally vulnerable Python code for Semgrep testing.
DO NOT use in production.
"""

import hashlib
import subprocess
import pickle
import yaml

# Vulnerability 1: Hardcoded credentials (p/secrets)
DATABASE_PASSWORD = "super_secret_password_123"
API_KEY = "sk_live_abc123xyz789"

# Vulnerability 2: Weak cryptography (p/trailofbits)
def hash_password_insecure(password):
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 3: Command injection (p/security-audit)
def run_command(user_input):
    result = subprocess.call(f"echo {user_input}", shell=True)
    return result

# Vulnerability 4: SQL Injection pattern
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# Vulnerability 5: Insecure deserialization (p/trailofbits)
def load_user_data(data):
    return pickle.loads(data)

# Vulnerability 6: YAML load without safe_load
def parse_config(yaml_string):
    return yaml.load(yaml_string)

# Vulnerability 7: Hardcoded IP address
INTERNAL_API = "http://192.168.1.100:8080/api"

# Vulnerability 8: Debug mode enabled
DEBUG = True
