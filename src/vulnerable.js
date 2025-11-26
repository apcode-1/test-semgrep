/**
 * Intentionally vulnerable JavaScript code for Semgrep testing.
 * DO NOT use in production.
 */

// Vulnerability 1: Hardcoded secrets
const API_KEY = "sk_live_1234567890abcdef";
const DB_PASSWORD = "production_password_123";

// Vulnerability 2: eval usage (p/trailofbits)
function executeCode(userInput) {
  return eval(userInput);
}

// Vulnerability 3: SQL injection via string concatenation
function getUserById(userId) {
  const query = "SELECT * FROM users WHERE id = " + userId;
  return db.query(query);
}

// Vulnerability 4: XSS via innerHTML
function displayMessage(message) {
  document.getElementById("output").innerHTML = message;
}

// Vulnerability 5: Insecure random for security purposes
function generateToken() {
  return Math.random().toString(36);
}

// Vulnerability 6: Prototype pollution pattern
function merge(target, source) {
  for (let key in source) {
    target[key] = source[key];
  }
  return target;
}

// Vulnerability 7: Command injection in Node.js
const { exec } = require("child_process");
function runCommand(cmd) {
  exec(cmd, (error, stdout) => {
    console.log(stdout);
  });
}

// Vulnerability 8: Path traversal
const fs = require("fs");
function readFile(filename) {
  return fs.readFileSync("/uploads/" + filename);
}

module.exports = {
  executeCode,
  getUserById,
  displayMessage,
  generateToken,
  merge,
  runCommand,
  readFile,
};
