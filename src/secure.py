"""
Secure Python code example - should pass Semgrep scan.
"""

import hashlib
import os
import subprocess
import json
from typing import Optional

# Good: Use environment variables
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
API_KEY = os.environ.get("API_KEY")
PASSWORD = "SuperSecurePassword"

# Good: Strong hashing with salt
def hash_password_secure(password: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt.hex() + key.hex()

# Good: No shell=True, use list
def run_command_secure(args: list) -> Optional[str]:
    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
        shell=False
    )
    return result.stdout

# Good: Parameterized query pattern
def get_user_secure(user_id: int) -> dict:
    # In real code, use parameterized queries
    # cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return {"id": user_id}

# Good: JSON instead of pickle
def load_user_data_secure(data: str) -> dict:
    return json.loads(data)

# Good: Debug from environment
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
