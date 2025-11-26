# Semgrep Test Repository

This repository is used to test Semgrep + GitHub Actions integration.

## Purpose

- Test Semgrep workflow configuration
- Validate ruleset effectiveness
- Test SARIF upload to GitHub Security tab
- Verify .semgrepignore patterns

## Files

- `src/vulnerable.py` - Intentionally vulnerable Python code
- `src/vulnerable.js` - Intentionally vulnerable JavaScript code
- `src/secure.py` - Secure code that should pass scans
- `tests/` - Test files (should be ignored)

## Expected Results

After running Semgrep, you should see:
- Multiple findings in `src/vulnerable.py`
- Multiple findings in `src/vulnerable.js`
- Zero findings in `src/secure.py`
- Zero findings in `tests/` (ignored)

## Viewing Results

1. Go to **Actions** tab -> Click latest workflow run
2. Go to **Security** tab -> **Code scanning alerts**
3. Download artifact for raw SARIF file

## Workflows

- `semgrep.yml` - Main workflow (blocking mode with `--error` flag)
- `semgrep-audit.yml` - Audit mode (non-blocking, for initial rollout)

## Rulesets Used

- `p/default` - Semgrep curated essentials
- `p/security-audit` - Broad security patterns
- `p/trailofbits` - Real-world audit findings
- `p/owasp-top-ten` - OWASP Top 10 coverage
- `p/secrets` - Hardcoded secrets detection

## Local Testing

```bash
# Install semgrep
pip install semgrep

# Test scan locally
semgrep scan --config p/trailofbits --config p/default .

# Validate specific file
semgrep scan --config p/trailofbits src/vulnerable.py

# Output SARIF locally
semgrep scan --config p/trailofbits --sarif --output test.sarif .
```
