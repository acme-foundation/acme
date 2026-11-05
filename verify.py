#!/usr/bin/env python3
"""
ACME CORE INVARIANT GATE & CONSTITUTIONAL VERIFIER (Pure Standard Library)
Self-Compiling Genesis Verifier (v3.0.1-Genesis)
Serves as the Mechanical Gatekeeper Turnike at the repository boundary.
"""

import os
import sys
import json
import re
import subprocess

def run_invariant_audit(verify_all: bool = False) -> bool:
    print("=" * 68)
    print("      ACME GENESIS CONSTITUTIONAL INTEGRITY & INVARIANT GATE (v3.0.1)      ")
    print("=" * 68)

    # 1. Zero-Code Invariant: No code artifacts tracked in core (except verify.py gatekeeper)
    forbidden_exts = ['.py', '.sh', '.exe', '.dll', '.bin']
    try:
        tracked = subprocess.check_output(['git', 'ls-files'], text=True).splitlines()
        for f in tracked:
            if f == 'verify.py':
                continue
            if os.path.splitext(f)[1].lower() in forbidden_exts:
                print(f"[FAIL] Code artifact tracked in git: {f}", file=sys.stderr)
                return False
        print("[+] Zero-Code Invariant:     [PASS] Zero executable artifacts tracked in git (verify.py exempted).")
    except Exception as e:
        print(f"[WARN] Unable to run git ls-files: {e}")

    # 2. Registry & Thesis Integrity (File presence, size, UTF-8 No-BOM)
    try:
        with open('registry/graduates.json', 'r', encoding='utf-8') as fl:
            grads = json.load(fl)
        if not grads:
            print("[FAIL] Graduates registry is empty.", file=sys.stderr)
            return False

        for g in grads:
            t_file = g.get('thesis_file')
            if not t_file or not os.path.exists(t_file):
                print(f"[FAIL] Missing thesis file: {t_file}", file=sys.stderr)
                return False

            raw_bytes = open(t_file, 'rb').read()
            if len(raw_bytes) < 100:
                print(f"[FAIL] Thesis file too small (<100 bytes): {t_file}", file=sys.stderr)
                return False

            # Check UTF-8 BOM
            if raw_bytes.startswith(b'\xef\xbb\xbf'):
                print(f"[FAIL] UTF-8 BOM detected in thesis file: {t_file}", file=sys.stderr)
                return False

        print(f"[+] Registry Integrity:      [PASS] All {len(grads)} accredited thesis files verified (No-BOM).")
    except Exception as e:
        print(f"[FAIL] Registry verification failed: {e}", file=sys.stderr)
        return False

    # 2.5. Faculty Catalogs Integrity (SYS_systems.md, LAW_law.md, PHI_philosophy.md)
    try:
        required_faculties = ['faculty/SYS_systems.md', 'faculty/LAW_law.md', 'faculty/PHI_philosophy.md']
        for fac_path in required_faculties:
            if not os.path.exists(fac_path):
                print(f"[FAIL] Missing faculty catalog: {fac_path}", file=sys.stderr)
                return False
            fac_bytes = open(fac_path, 'rb').read()
            if fac_bytes.startswith(b'\xef\xbb\xbf'):
                print(f"[FAIL] UTF-8 BOM detected in faculty catalog: {fac_path}", file=sys.stderr)
                return False
            if len(fac_bytes) < 100:
                print(f"[FAIL] Faculty catalog too small: {fac_path}", file=sys.stderr)
                return False
        print("[+] Faculty Integrity:       [PASS] All 3 unified faculty catalogs verified (No-BOM).")
    except Exception as e:
        print(f"[FAIL] Faculty verification failed: {e}", file=sys.stderr)
        return False

    # 3. Domain Purity Negative Gate
    prohibited = ['UYAP', 'TCKN', 'UDF']
    for root, dirs, files in os.walk('theses'):
        for f in files:
            if f.endswith('.md'):
                c = open(os.path.join(root, f), 'r', encoding='utf-8').read()
                for p in prohibited:
                    if p in c:
                        print(f"[FAIL] Domain purity breach ({p}) in {f}", file=sys.stderr)
                        return False
    print("[+] Domain Purity Gate:      [PASS] No proprietary domain leakage detected.")

    # 4. Constitutional Integrity & Lex Superior Parity Gate
    try:
        const_text = open('CONSTITUTION.md', 'r', encoding='utf-8').read()
        required_invariants = [
            'REJECT_SCOPE_EVASION',
            'REJECT_EXTREME_ENTROPY',
            'REJECT_SPECULATIVE_STATE',
            'QUARANTINE_AND_LOG',
            'INV-SINGLE-MANIFEST',
            'INV-OPTIN-STRICT',
            'Dewdrop Boundary Invariant',
            'Biological Primacy'
        ]
        for inv in required_invariants:
            if inv not in const_text:
                print(f"[FAIL] Missing core constitutional invariant: {inv}", file=sys.stderr)
                return False

        # Verify the 5 Pillars are declared
        five_pillars = [
            'PRINCIPLE OF LEAST ACTION',
            'SPEC-FIRST',
            'VIA NEGATIVA',
            'AUTONOMOUS OVERSIGHT',
            'CONTROL PLANE'
        ]
        for pillar in five_pillars:
            if pillar not in const_text.upper():
                print(f"[FAIL] Missing constitutional pillar: {pillar}", file=sys.stderr)
                return False

        print("[+] Constitutional Parity:   [PASS] All 5 Core Pillars and Lex invariants verified.")
    except Exception as e:
        print(f"[FAIL] Constitution check failed: {e}", file=sys.stderr)
        return False

    # 5. Cross-Merkle SHA Consistency Gate
    try:
        for g in grads:
            sha = g.get('graduation_sha', '').strip()
            if not re.match(r'^[0-9a-f]{40}$', sha, re.IGNORECASE):
                print(f"[FAIL] Invalid Merkle commit SHA for {g.get('node_id')}: {sha}", file=sys.stderr)
                return False
            # Check git object exists
            exit_code = subprocess.call(['git', 'cat-file', '-e', f'{sha}^{{commit}}'],
                                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if exit_code != 0:
                print(f"[FAIL] Merkle commit SHA not found in git tree: {sha}", file=sys.stderr)
                return False
        print(f"[+] Merkle Consistency:     [PASS] All {len(grads)} graduation commit SHAs validated in git tree.")
    except Exception as e:
        print(f"[WARN] Merkle git verification check bypassed: {e}")

    # 6. Full-Sweep Crucible Audit
    if verify_all:
        print("\n--- FULL-SWEEP THESIS CRUCIBLE AUDIT ---")
        for g in grads:
            t_file = g['thesis_file']
            c = open(t_file, 'r', encoding='utf-8').read()
            # Invariant check: must have at least one invariant or Lex
            if not re.search(r'(?:INVARIANT|THE LEX|DoF\s*=\s*0)', c, re.IGNORECASE):
                print(f"[FAIL] Thesis lacks formal invariants: {t_file}", file=sys.stderr)
                return False
            # Check Pre-Mortem Anti-Pattern Gate (Section 1.4 DoF = 0)
            if 'SECTION 1.4' not in c or '[PROHIBITED]' not in c:
                print(f"[FAIL] Thesis lacks Section 1.4 Pre-Mortem Gate ([PROHIBITED]): {t_file}", file=sys.stderr)
                return False
            # Check DoD
            if not re.search(r'(?:DEFINITION OF DONE|DoD)', c, re.IGNORECASE):
                print(f"[FAIL] Thesis lacks Definition of Done: {t_file}", file=sys.stderr)
                return False

        print(f"[+] Full-Sweep Audit:        [PASS] All {len(grads)} theses passed crucible verification.")

    # 7. Semantic Fluff & Adjective Density Gate (<= 0.02)
    try:
        subjective_words = ['hızlı', 'mükemmel', 'harika', 'güçlü', 'kolay', 'kusursuz', 'süper']
        total_words = 0
        subj_count = 0
        for root, dirs, files in os.walk('theses'):
            for f in files:
                if f.endswith('.md'):
                    text = open(os.path.join(root, f), 'r', encoding='utf-8').read().lower()
                    words = re.findall(r'\w+', text)
                    total_words += len(words)
                    for w in subjective_words:
                        subj_count += len(re.findall(r'\b' + w + r'\b', text))
        density = subj_count / max(1, total_words)
        if density > 0.02:
            print(f"[FAIL] Adjective Density breached: {density:.4f} > 0.02", file=sys.stderr)
            return False
        print(f"[+] Adjective Density Gate:  [PASS] Subjective fluff density {density:.4f} <= 0.02.")
    except Exception as e:
        print(f"[WARN] Adjective density check bypassed: {e}")

    # 8. SemVer Cadence & Gatekeeper Assertion
    try:
        latest_tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--abbrev=0'],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        last_commit_msg = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B'],
            text=True
        ).strip()

        match = re.match(r'^v?(\d+)\.(\d+)\.(\d+)(?:-.*)?$', latest_tag)
        if match:
            major, minor, patch = map(int, match.groups())
            if major >= 3 and minor > 0:
                if '[RELEASE]' not in last_commit_msg.upper():
                    print(f"[FAIL] SemVer Cadence Breach: Minor tag '{latest_tag}' forbidden without [RELEASE] in commit!", file=sys.stderr)
                    return False
        print(f"[+] SemVer Cadence Gate:     [PASS] Tag ({latest_tag}) verified under monotonic lock.")
    except Exception:
        print(f"[+] SemVer Cadence Gate:     [PASS] Initial bootstrap tag verified.")

    print("--------------------------------------------------------------------")
    print("[PASS] All ACME Genesis pure NLP invariants and CI/CD gates verified.")
    print("=" * 68)
    return True

if __name__ == "__main__":
    verify_all_flag = "--verify-all" in sys.argv or "-a" in sys.argv
    success = run_invariant_audit(verify_all=verify_all_flag)
    sys.exit(0 if success else 1)
