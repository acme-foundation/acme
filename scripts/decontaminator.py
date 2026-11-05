#!/usr/bin/env python3
"""
ACME Pre-Commit Decontamination & PII Shield (Pure Standard Library)
Enforces INV-DECONTAMINATION: Zero absolute local paths, secret tokens, or private credentials.
"""

import os
import sys
import re
import subprocess
from pathlib import Path

# Prohibited absolute local path patterns (Windows and Unix host paths)
PATH_PATTERNS = [
    re.compile(r'[A-Za-z]:\\[Uu]sers\\[a-zA-Z0-9._-]+', re.IGNORECASE),
    re.compile(r'[A-Za-z]:/[Uu]sers/[a-zA-Z0-9._-]+', re.IGNORECASE),
    re.compile(r'[A-Za-z]:\\[Dd]rive[^\\]*', re.IGNORECASE),
    re.compile(r'[A-Za-z]:/[Dd]rive[^/]*', re.IGNORECASE),
    re.compile(r'/(?:home|Users)/[a-zA-Z0-9._-]+/(?:workspaces|projects|desktop)', re.IGNORECASE),
]

# Sensitive credentials and secret key patterns
SECRET_PATTERNS = [
    re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    re.compile(r'\bsk-[a-zA-Z0-9]{20,}\b'),
    re.compile(r'\bAIza[0-9A-Za-z-_]{35}\b'),
    re.compile(r'-----BEGIN (?:RSA )?PRIVATE KEY-----'),
    re.compile(r'(?i)(?:api_key|secret_key|auth_token)\s*[:=]\s*["\'][a-zA-Z0-9_\-]{24,}["\']'),
]

# Excluded binary extensions and directories
EXCLUDED_EXTS = {'.bundle', '.png', '.jpg', '.jpeg', '.gif', '.ico', '.bin', '.exe', '.dll'}
EXCLUDED_PATHS = {'.git', '.tmp', 'scratch'}

def get_tracked_files():
    try:
        output = subprocess.check_output(['git', 'ls-files'], text=True, stderr=subprocess.DEVNULL)
        return [f.strip() for f in output.splitlines() if f.strip()]
    except Exception:
        # Fallback to walking filesystem if git is unavailable
        files = []
        for root, dirs, filenames in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_PATHS]
            for f in filenames:
                files.append(os.path.relpath(os.path.join(root, f), '.'))
        return files

def scan_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in EXCLUDED_EXTS:
        return []

    if not os.path.exists(file_path) or os.path.isdir(file_path):
        return []

    violations = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_no, line in enumerate(f, 1):
                # Check path leaks
                for pat in PATH_PATTERNS:
                    m = pat.search(line)
                    if m:
                        violations.append((file_path, line_no, "Absolute Local Path Leak", m.group(0)))

                # Check secret leaks
                for pat in SECRET_PATTERNS:
                    m = pat.search(line)
                    if m:
                        violations.append((file_path, line_no, "Credential / Key Leak", "***REDACTED***"))
    except Exception as e:
        violations.append((file_path, 0, "Read Error", str(e)))

    return violations

def run_decontamination_audit(fix: bool = False):
    tracked = get_tracked_files()
    total_violations = []

    for file_path in tracked:
        # Skip self to avoid regex pattern false-positives
        if os.path.normpath(file_path) == os.path.normpath(os.path.join('scripts', 'decontaminator.py')):
            continue

        violations = scan_file(file_path)
        if violations:
            total_violations.extend(violations)

    if total_violations:
        print("[FAIL] Decontamination Shield Breached! Absolute paths or credentials detected:", file=sys.stderr)
        for fpath, lno, vtype, snippet in total_violations:
            print(f"  - {fpath}:{lno} [{vtype}]: {snippet}", file=sys.stderr)
        return False

    print("[PASS] Decontamination Shield Clean: Zero absolute local paths or secret credentials detected.")
    return True

if __name__ == "__main__":
    fix_mode = "--fix" in sys.argv
    success = run_decontamination_audit(fix=fix_mode)
    sys.exit(0 if success else 1)
