"""
Test file - should be ignored by Semgrep.
"""

# This hardcoded password should NOT trigger alerts (tests are ignored)
TEST_PASSWORD = "test_password_123"
TEST_API_KEY = "sk_test_fake_key_for_testing"

def test_something():
    assert True

def test_with_fake_credentials():
    # Using fake credentials in tests is acceptable
    api_key = "fake_api_key"
    assert len(api_key) > 0
