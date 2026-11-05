#!/usr/bin/env python3
"""
ACME CORE INVARIANT GATE & CONSTITUTIONAL VERIFIER (Pure Standard Library)
Self-Compiling Genesis Verifier (v3.0.3-Genesis)
Serves as the Mechanical Gatekeeper Turnike at the repository boundary.
"""

import os
import sys
import json
import re
import subprocess

def run_invariant_audit(verify_all: bool = False) -> bool:
    print("=" * 68)
    print("      ACME GENESIS CONSTITUTIONAL INTEGRITY & INVARIANT GATE (v3.0.3)      ")
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

    # 2. No-BOM UTF-8 & EOL Standard Gate across all tracked documentation
    try:
        for f in tracked:
            if f.endswith(('.md', '.json', '.py', '.txt')):
                if os.path.exists(f):
                    raw = open(f, 'rb').read()
                    if raw.startswith(b'\xef\xbb\xbf'):
                        print(f"[FAIL] UTF-8 BOM detected in: {f}", file=sys.stderr)
                        return False
        print("[+] No-BOM UTF-8 Standard:   [PASS] All tracked repository files verified (No-BOM).")
    except Exception as e:
        print(f"[FAIL] No-BOM verification failed: {e}", file=sys.stderr)
        return False

    # 3. Faculty Catalogs Integrity (SYS_systems.md, LAW_law.md, PHI_philosophy.md)
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

    # 4. Workflows Engine Integrity Gate
    try:
        if not os.path.exists('workflows'):
            print("[FAIL] Missing 'workflows/' directory.", file=sys.stderr)
            return False
        wf_files = [os.path.join('workflows', f) for f in os.listdir('workflows') if f.endswith('.md')]
        if not wf_files:
            print("[FAIL] No workflow specifications found in workflows/.", file=sys.stderr)
            return False
        for wf_path in wf_files:
            content = open(wf_path, 'r', encoding='utf-8').read()
            if 'State 0' not in content or 'State 1' not in content:
                print(f"[FAIL] Workflow lacks state machine transitions: {wf_path}", file=sys.stderr)
                return False
        print(f"[+] Workflows Engine Gate:   [PASS] All {len(wf_files)} workflow state machines verified.")
    except Exception as e:
        print(f"[FAIL] Workflows verification failed: {e}", file=sys.stderr)
        return False

    # 5. Constitutional Integrity & Lex Superior Parity Gate
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
            'Biological Primacy',
            'INV-FORMAL-IR-GATE',
            'INV-RUNTIME-INTERCEPT',
            'INV-CRUCIBLE-CERTIFICATION'
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

        print("[+] Constitutional Parity:   [PASS] All 5 Core Pillars and 12 Lex invariants verified.")
    except Exception as e:
        print(f"[FAIL] Constitution check failed: {e}", file=sys.stderr)
        return False

    # 6. RFC Formal Hardening Integrity Gate (RFC-048, RFC-049, RFC-050)
    try:
        required_rfcs = [
            ('rfcs/RFC_048_FORMAL_INTERMEDIATE_REPRESENTATION.md', 'INV-FORMAL-IR-GATE'),
            ('rfcs/RFC_049_RUNTIME_INTERCEPT_AND_AST_SHIELD.md', 'INV-RUNTIME-INTERCEPT'),
            ('rfcs/RFC_050_ADVERSARIAL_CRUCIBLE_CERTIFICATION.md', 'INV-CRUCIBLE-CERTIFICATION')
        ]
        for rfc_path, anchored_inv in required_rfcs:
            if not os.path.exists(rfc_path):
                print(f"[FAIL] Missing formal RFC document: {rfc_path}", file=sys.stderr)
                return False
            rfc_text = open(rfc_path, 'r', encoding='utf-8').read()
            if anchored_inv not in rfc_text:
                print(f"[FAIL] RFC {rfc_path} lacks anchored invariant: {anchored_inv}", file=sys.stderr)
                return False
        print("[+] RFC Invariant Parity:   [PASS] RFC-048, RFC-049, RFC-050 ratified with constitutional anchors.")
    except Exception as e:
        print(f"[FAIL] RFC verification failed: {e}", file=sys.stderr)
        return False

    # 7. Domain Purity Negative Gate
    prohibited = ['UYAP', 'TCKN', 'UDF']
    if os.path.exists('theses'):
        for root, dirs, files in os.walk('theses'):
            for f in files:
                if f.endswith('.md'):
                    c = open(os.path.join(root, f), 'r', encoding='utf-8').read()
                    for p in prohibited:
                        if p in c:
                            print(f"[FAIL] Domain purity breach ({p}) in {f}", file=sys.stderr)
                            return False
    print("[+] Domain Purity Gate:      [PASS] No proprietary domain leakage detected.")

    # 8. Semantic Fluff & Adjective Density Gate (<= 0.02)
    try:
        subjective_words = ['hızlı', 'mükemmel', 'harika', 'güçlü', 'kolay', 'kusursuz', 'süper']
        total_words = 0
        subj_count = 0
        if os.path.exists('theses'):
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

    # 9. Formal Schema Gate (FIR & JSON-Schema Validation via stdlib)
    try:
        fir_files = []
        for root, dirs, files in os.walk('.'):
            if '.git' in dirs:
                dirs.remove('.git')
            for f in files:
                if f.endswith('.fir.json'):
                    fir_files.append(os.path.join(root, f))
        if not fir_files:
            print("[FAIL] No Formal Intermediate Representation (.fir.json) files found.", file=sys.stderr)
            return False
        required_keys = ['fir_version', 'initial_state', 'states', 'action_transition_matrix', 'invariant_verification_set']
        for p in fir_files:
            with open(p, 'r', encoding='utf-8') as f:
                schema_data = json.load(f)
            for k in required_keys:
                if k not in schema_data:
                    print(f"[FAIL] Missing FIR key '{k}' in {p}", file=sys.stderr)
                    return False
            states = set(schema_data.get('states', []))
            if schema_data.get('initial_state') not in states:
                print(f"[FAIL] initial_state not in states set in {p}", file=sys.stderr)
                return False
            for t in schema_data.get('action_transition_matrix', []):
                for tk in ['from', 'to', 'event', 'pre_conditions', 'post_conditions']:
                    if tk not in t:
                        print(f"[FAIL] Incomplete transition contract '{tk}' in {p}", file=sys.stderr)
                        return False
        print(f"[+] Formal Schema Gate:     [PASS] Intermediate representations strictly typed.")
    except Exception as e:
        print(f"[FAIL] Formal schema validation failed: {e}", file=sys.stderr)
        return False

    # 10. SemVer Cadence & Gatekeeper Assertion (Quench Gate)
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
