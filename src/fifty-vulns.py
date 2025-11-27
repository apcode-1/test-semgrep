"""
50 vulnerabilities for testing inline annotations.
Each function has a unique vulnerability.
"""

import subprocess
import os
import pickle
import yaml
import hashlib
import random
import sqlite3

# 1. Command injection
def vuln_01(user_input):
    subprocess.call(user_input, shell=True)

# 2. Command injection variant
def vuln_02(cmd):
    os.system(cmd)

# 3. Command injection with format string
def vuln_03(filename):
    subprocess.call(f"cat {filename}", shell=True)

# 4. Command injection with popen
def vuln_04(command):
    os.popen(command)

# 5. SQL injection
def vuln_05(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

# 6. SQL injection variant
def vuln_06(name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return query

# 7. SQL injection with format
def vuln_07(email):
    query = "DELETE FROM users WHERE email = '%s'" % email
    return query

# 8. Pickle deserialization
def vuln_08(data):
    return pickle.loads(data)

# 9. Pickle load from file
def vuln_09(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)

# 10. YAML unsafe load
def vuln_10(yaml_str):
    return yaml.load(yaml_str)

# 11. YAML unsafe load from file
def vuln_11(filepath):
    with open(filepath) as f:
        return yaml.load(f)

# 12. MD5 hash
def vuln_12(password):
    return hashlib.md5(password.encode()).hexdigest()

# 13. SHA1 hash (weak)
def vuln_13(data):
    return hashlib.sha1(data.encode()).hexdigest()

# 14. Hardcoded password
PASSWORD = "super_secret_123"

# 15. Hardcoded API key
API_KEY = "sk_live_abcdef123456"

# 16. Hardcoded AWS key
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

# 17. Hardcoded AWS secret
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# 18. Hardcoded database password
DB_PASSWORD = "mysql_root_password_123"

# 19. Hardcoded JWT secret
JWT_SECRET = "my_jwt_secret_key_very_long"

# 20. Hardcoded encryption key
ENCRYPTION_KEY = "aes_256_encryption_key_here"

# 21. Eval usage
def vuln_21(code):
    return eval(code)

# 22. Exec usage
def vuln_22(code):
    exec(code)

# 23. Compile and exec
def vuln_23(code):
    compiled = compile(code, '<string>', 'exec')
    exec(compiled)

# 24. Random for security
def vuln_24():
    return random.randint(100000, 999999)

# 25. Weak random token
def vuln_25():
    return ''.join([str(random.randint(0, 9)) for _ in range(16)])

# 26. Path traversal
def vuln_26(filename):
    return open("/uploads/" + filename).read()

# 27. Path traversal variant
def vuln_27(user_path):
    base = "/var/data/"
    return open(base + user_path).read()

# 28. SSRF potential
def vuln_28(url):
    import urllib.request
    return urllib.request.urlopen(url).read()

# 29. Command injection in subprocess.run
def vuln_29(cmd):
    subprocess.run(cmd, shell=True)

# 30. Command injection in subprocess.Popen
def vuln_30(cmd):
    subprocess.Popen(cmd, shell=True)

# 31. Command injection in subprocess.check_output
def vuln_31(cmd):
    return subprocess.check_output(cmd, shell=True)

# 32. Command injection in subprocess.check_call
def vuln_32(cmd):
    subprocess.check_call(cmd, shell=True)

# 33. SQL injection with sqlite3
def vuln_33(db, user_id):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchall()

# 34. SQL injection with executescript
def vuln_34(db, query):
    db.executescript(query)

# 35. Hardcoded private key
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy
-----END RSA PRIVATE KEY-----"""

# 36. Hardcoded Slack webhook (removed - blocked by GitHub)
SLACK_WEBHOOK = "slack_webhook_placeholder"

# 37. Hardcoded GitHub token
GITHUB_TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 38. Hardcoded Stripe key
STRIPE_KEY = "sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 39. Weak cipher
def vuln_39(data):
    from Crypto.Cipher import DES
    cipher = DES.new(b'8bytekey', DES.MODE_ECB)
    return cipher.encrypt(data)

# 40. Assert used for validation
def vuln_40(user_input):
    assert user_input.isalnum(), "Invalid input"
    return user_input

# 41. Binding to all interfaces
def vuln_41():
    import socket
    s = socket.socket()
    s.bind(('0.0.0.0', 8080))

# 42. Hardcoded Sendgrid key
SENDGRID_KEY = "SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 43. Hardcoded Twilio key
TWILIO_KEY = "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 44. Debug mode enabled
DEBUG = True
FLASK_DEBUG = True

# 45. Hardcoded MongoDB URI
MONGO_URI = "mongodb://admin:password123@localhost:27017/mydb"

# 46. Hardcoded Redis password
REDIS_URL = "redis://:secretpassword@localhost:6379/0"

# 47. SSL verification disabled
def vuln_47(url):
    import requests
    return requests.get(url, verify=False)

# 48. Hardcoded Basic Auth
AUTH_HEADER = "Basic YWRtaW46cGFzc3dvcmQxMjM="

# 49. Hardcoded Bearer token
BEARER_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0"

# 50. Command injection with shell pipe
def vuln_50(filename):
    os.system(f"cat {filename} | grep password")
