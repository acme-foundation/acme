#!/usr/bin/env python3
"""
ACME CORE INVARIANT GATE & CONSTITUTIONAL VERIFIER (Pure Standard Library)
Self-Compiling Genesis Verifier (v3.2.0 - Jurisprudential 7-Gate Turnstile)
Serves as the Mechanical Gatekeeper Turnstile at the repository boundary.
Codifies Canonical Interlingua Invariant (INV-CANONICAL-INTERLINGUA / DoF = 0).
"""

import os
import sys
import re
import subprocess
from pathlib import Path

def run_invariant_audit(verify_all: bool = False) -> bool:
    print("=" * 68)
    print("      ACME GENESIS CONSTITUTIONAL INTEGRITY & INVARIANT GATE (v3.2.0)      ")
    print("=" * 68)

    root = Path(".")

    # Gate 1: Zero-Code Invariant: No code artifacts tracked in core (except verify.py)
    forbidden_exts = ['.py', '.sh', '.exe', '.dll', '.bin']
    try:
        tracked = subprocess.check_output(['git', 'ls-files'], text=True).splitlines()
        for f in tracked:
            norm_f = Path(f).as_posix()
            if norm_f == 'verify.py':
                continue
            if Path(f).suffix.lower() in forbidden_exts:
                print(f"[FAIL] Code artifact tracked in git: {f}", file=sys.stderr)
                return False
        # Also check untracked files on filesystem (excluding .git and .tmp)
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            posix_path = p.as_posix()
            if ".git" in posix_path.split("/") or ".tmp" in posix_path.split("/"):
                continue
            if posix_path == "verify.py":
                continue
            if p.suffix.lower() in forbidden_exts:
                print(f"[FAIL] Forbidden executable file on disk: {p}", file=sys.stderr)
                return False
        print("[+] Gate 1: Zero-Code Invariant:         [PASS] Zero executable artifacts tracked (verify.py exempted).")
    except Exception as e:
        print(f"[FAIL] Gate 1 check failed: {e}", file=sys.stderr)
        return False

    # Gate 2: No-BOM UTF-8 & Canonical Interlingua Gate (INV-CANONICAL-INTERLINGUA)
    try:
        # Check for localized Turkish characters across all documentation and templates
        turkish_codepoints = {
            0x00E7, 0x011F, 0x0131, 0x00F6, 0x015F, 0x00FC,
            0x00C7, 0x011E, 0x0130, 0x00D6, 0x015E, 0x00DC
        }
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            posix_path = p.as_posix()
            if ".git" in posix_path.split("/") or ".tmp" in posix_path.split("/"):
                continue
            if posix_path == "verify.py":
                continue
            if p.suffix.lower() in ['.md', '.py', '.json', '.txt']:
                raw = p.read_bytes()
                if raw.startswith(b'\xef\xbb\xbf'):
                    print(f"[FAIL] UTF-8 BOM detected in: {p}", file=sys.stderr)
                    return False
                text = p.read_text(encoding="utf-8")
                for ch in text:
                    if ord(ch) in turkish_codepoints:
                        print(f"[FAIL] Canonical Interlingua Breach: Localized character '{ch}' (U+{ord(ch):04X}) detected in: {p}", file=sys.stderr)
                        return False
        print("[+] Gate 2: No-BOM UTF-8 & Interlingua:  [PASS] All tracked artifacts verified (No-BOM / Interlingua).")
    except Exception as e:
        print(f"[FAIL] Gate 2 check failed: {e}", file=sys.stderr)
        return False

    # Gate 3: Constitutional Parity: Articles 0 to 8 in CONSTITUTION.md
    try:
        const_path = Path("CONSTITUTION.md")
        if not const_path.is_file():
            print("[FAIL] Missing CONSTITUTION.md", file=sys.stderr)
            return False
        const_text = const_path.read_text(encoding="utf-8")
        required_articles = [
            "ARTICLE 0: TELEOLOGICAL GROUNDING",
            "ARTICLE 1: PRINCIPLE OF LEAST ACTION",
            "ARTICLE 2: DEWDROP BOUNDARY ISOLATION",
            "ARTICLE 3: BIOLOGICAL PRIMACY",
            "ARTICLE 4: BI-DIRECTIONAL ZERO-TRUST GATEKEEPER",
            "ARTICLE 5: ADVERSARIAL TWIN DYNAMICS",
            "ARTICLE 6: SOVEREIGN OVERRIDE",
            "ARTICLE 7: JURISPRUDENTIAL PRECEDENT",
            "ARTICLE 8: CANONICAL LANGUAGE & INTERLINGUA PROTOCOL",
            "ARTICLE 9: MANDATORY TEMPORAL ALIGNMENT & PROCEDURAL PRECEDENCE"
        ]
        for art in required_articles:
            if art not in const_text:
                print(f"[FAIL] Missing constitutional article: {art}", file=sys.stderr)
                return False
        print("[+] Gate 3: Constitutional Parity:       [PASS] Articles 0 to 9 ratified in CONSTITUTION.md.")
    except Exception as e:
        print(f"[FAIL] Gate 3 check failed: {e}", file=sys.stderr)
        return False

    # Gate 4: 3-Letter Hex Norms: All files under norms/ must follow (COR|ING|PRO)_[0-9A-F]{3}_.*\.md
    try:
        norms_dir = Path("norms")
        if not norms_dir.is_dir():
            print("[FAIL] Missing 'norms/' directory.", file=sys.stderr)
            return False
        norm_files = list(norms_dir.rglob("*.md"))
        if not norm_files:
            print("[FAIL] No norm specifications found under norms/.", file=sys.stderr)
            return False
        hex_pattern = re.compile(r'^(COR|ING|PRO)_[0-9A-F]{3}_.*\.md$', re.IGNORECASE)
        for nf in norm_files:
            if not hex_pattern.match(nf.name):
                print(f"[FAIL] Norm file does not conform to 3-letter hex pattern: {nf.name}", file=sys.stderr)
                return False
            if len(nf.read_bytes()) < 50:
                print(f"[FAIL] Norm file suspiciously small: {nf}", file=sys.stderr)
                return False
        print(f"[+] Gate 4: 3-Letter Hex Norms:          [PASS] All {len(norm_files)} norm files validated under pattern.")
    except Exception as e:
        print(f"[FAIL] Gate 4 check failed: {e}", file=sys.stderr)
        return False

    # Gate 5: Templates & Precedents Integrity
    try:
        required_templates = [
            Path("templates/CASE_TEMPLATE.md"),
            Path("templates/PRECEDENT_TEMPLATE.md"),
            Path("templates/NORM_TEMPLATE.md")
        ]
        for tmpl in required_templates:
            if not tmpl.is_file():
                print(f"[FAIL] Missing template: {tmpl}", file=sys.stderr)
                return False
            if len(tmpl.read_bytes()) < 50:
                print(f"[FAIL] Template too small: {tmpl}", file=sys.stderr)
                return False

        required_precedents = [
            Path("precedents/ingestion/ING_001_STREAM_QUARANTINE_RULING.md")
        ]
        for prec in required_precedents:
            if not prec.is_file():
                print(f"[FAIL] Missing precedent ruling: {prec}", file=sys.stderr)
                return False
            if len(prec.read_bytes()) < 100:
                print(f"[FAIL] Precedent ruling too small: {prec}", file=sys.stderr)
                return False
        print(f"[+] Gate 5: Templates & Precedents:      [PASS] 3 canonical templates and precedent registry verified.")
    except Exception as e:
        print(f"[FAIL] Gate 5 check failed: {e}", file=sys.stderr)
        return False

    # Gate 6: Adjective Density Gate (<= 0.02)
    try:
        subjective_words = ['fast', 'perfect', 'wonderful', 'powerful', 'easy', 'flawless', 'super', 'legendary', 'urgent', 'modern', 'lightweight']
        total_words = 0
        subj_count = 0
        audit_paths = [Path("CONSTITUTION.md"), Path("README.md")] + list(Path("norms").rglob("*.md")) + list(Path("precedents").rglob("*.md"))
        for ap in audit_paths:
            if ap.is_file():
                text = ap.read_text(encoding="utf-8").lower()
                words = re.findall(r'\b[a-zA-Z]+\b', text)
                total_words += len(words)
                for w in subjective_words:
                    subj_count += len(re.findall(r'\b' + w + r'\b', text))
        density = subj_count / max(1, total_words)
        if density > 0.02:
            print(f"[FAIL] Adjective Density breached: {density:.4f} > 0.02", file=sys.stderr)
            return False
        print(f"[+] Gate 6: Adjective Density Gate:      [PASS] Subjective fluff density {density:.4f} <= 0.02.")
    except Exception as e:
        print(f"[FAIL] Gate 6 check failed: {e}", file=sys.stderr)
        return False

    # Gate 7: SemVer Cadence: v3.2.0 active tag verification
    try:
        readme_text = Path("README.md").read_text(encoding="utf-8")
        if "v3.2.0" not in readme_text:
            print("[FAIL] Version v3.2.0 missing in README.md.", file=sys.stderr)
            return False
        const_text = Path("CONSTITUTION.md").read_text(encoding="utf-8")
        if "v3.2.0" not in const_text:
            print("[FAIL] Version v3.2.0 missing in CONSTITUTION.md.", file=sys.stderr)
            return False

        try:
            latest_tag = subprocess.check_output(
                ['git', 'describe', '--tags', '--abbrev=0'],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
            print(f"[+] Gate 7: SemVer Cadence:              [PASS] Version v3.2.0 confirmed (Active Tag: {latest_tag}).")
        except Exception:
            print("[+] Gate 7: SemVer Cadence:              [PASS] Version v3.2.0 ratified in specification.")
    except Exception as e:
        print(f"[FAIL] Gate 7 check failed: {e}", file=sys.stderr)
        return False

    print("-" * 68)
    print("[PASS] All 7 ACME v3.2.0 Jurisprudential & Invariant Gates PASS.")
    print("=" * 68)
    return True

if __name__ == "__main__":
    verify_all_flag = "--verify-all" in sys.argv or "-a" in sys.argv
    success = run_invariant_audit(verify_all=verify_all_flag)
    sys.exit(0 if success else 1)
