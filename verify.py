#!/usr/bin/env python3
"""
ACME CORE INVARIANT GATE & CONSTITUTIONAL VERIFIER (Pure Standard Library)
Self-Compiling Genesis Verifier (v3.2.0)
Serves as the Mechanical Gatekeeper Turnstile at the repository boundary.
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

    # Gate 1: Zero-Code Invariant: No code artifacts tracked in core (except verify.py)
    forbidden_exts = ['.py', '.sh', '.exe', '.dll', '.bin']
    root = Path(".")
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
        print("[+] Gate 1: Zero-Code Invariant:     [PASS] Zero executable artifacts tracked (verify.py exempted).")
    except Exception as e:
        print(f"[FAIL] Gate 1 check failed: {e}", file=sys.stderr)
        return False

    # Gate 2: No-BOM UTF-8 standard on all text and markdown files
    try:
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            posix_path = p.as_posix()
            if ".git" in posix_path.split("/") or ".tmp" in posix_path.split("/"):
                continue
            if p.suffix.lower() in ['.md', '.py', '.json', '.txt']:
                raw = p.read_bytes()
                if raw.startswith(b'\xef\xbb\xbf'):
                    print(f"[FAIL] UTF-8 BOM detected in: {p}", file=sys.stderr)
                    return False
        print("[+] Gate 2: No-BOM UTF-8:            [PASS] All markdown and text files verified (No-BOM).")
    except Exception as e:
        print(f"[FAIL] Gate 2 check failed: {e}", file=sys.stderr)
        return False

    # Gate 3: Constitutional Parity (Madde 0 to Madde 7 in CONSTITUTION.md)
    try:
        const_path = Path("CONSTITUTION.md")
        if not const_path.is_file():
            print("[FAIL] Missing CONSTITUTION.md", file=sys.stderr)
            return False
        const_text = const_path.read_text(encoding="utf-8")
        required_articles = [
            "MADDE 0: TELEOLOJİK ZEMİNLEME",
            "MADDE 1: EN AZ EYLEM VE SIFIR SERBESTLİK DERECESİ",
            "MADDE 2: ÇİĞ DAMLASI İZOLASYONU",
            "MADDE 3: BİYOLOJİK ASALET VE TERMAL DENGE",
            "MADDE 4: ÇİFT TARAFLI GATE-KEEPER VE SIFIR GÜVEN",
            "MADDE 5: HASMANE İKİZ DİNAMİĞİ",
            "MADDE 6: EGEMEN İRADE VE TERMİNAL FATURA",
            "MADDE 7: EMSAL İÇTİHAT VE NORM TERFİ PROTOKOLÜ"
        ]
        for art in required_articles:
            if art not in const_text:
                print(f"[FAIL] Missing constitutional article: {art}", file=sys.stderr)
                return False
        print("[+] Gate 3: Constitutional Parity:   [PASS] Articles 0 to 7 verified in CONSTITUTION.md.")
    except Exception as e:
        print(f"[FAIL] Gate 3 check failed: {e}", file=sys.stderr)
        return False

    # Gate 4: Norms Hierarchy verification
    try:
        required_norms = [
            Path("norms/core/NORM_001_MASS_BALANCE.md"),
            Path("norms/core/NORM_002_CONSTANT_MEMORY.md"),
            Path("norms/core/NORM_003_STATIC_SHIELD.md"),
            Path("norms/domain/ingestion/NORM_STREAM_QUARANTINE.md"),
            Path("norms/procedural/NORM_PRE_EXEC_DIALECTIC.md")
        ]
        for norm_p in required_norms:
            if not norm_p.is_file():
                print(f"[FAIL] Missing canonical norm file: {norm_p}", file=sys.stderr)
                return False
            if len(norm_p.read_bytes()) < 50:
                print(f"[FAIL] Norm file suspiciously small: {norm_p}", file=sys.stderr)
                return False
        print(f"[+] Gate 4: Norms Hierarchy:         [PASS] All {len(required_norms)} canonical norm specifications verified.")
    except Exception as e:
        print(f"[FAIL] Gate 4 check failed: {e}", file=sys.stderr)
        return False

    # Gate 5: Adjective Density Gate (<= 0.02)
    try:
        subjective_words = ['hızlı', 'mükemmel', 'harika', 'güçlü', 'kolay', 'kusursuz', 'süper', 'legendary', 'urgent', 'modern', 'hafif']
        total_words = 0
        subj_count = 0
        audit_paths = [Path("CONSTITUTION.md"), Path("README.md")] + list(Path("norms").rglob("*.md"))
        for ap in audit_paths:
            if ap.is_file():
                text = ap.read_text(encoding="utf-8").lower()
                words = re.findall(r'\w+', text)
                total_words += len(words)
                for w in subjective_words:
                    subj_count += len(re.findall(r'\b' + w + r'\b', text))
        density = subj_count / max(1, total_words)
        if density > 0.02:
            print(f"[FAIL] Adjective Density breached: {density:.4f} > 0.02", file=sys.stderr)
            return False
        print(f"[+] Gate 5: Adjective Density Gate:  [PASS] Subjective fluff density {density:.4f} <= 0.02.")
    except Exception as e:
        print(f"[FAIL] Gate 5 check failed: {e}", file=sys.stderr)
        return False

    # Gate 6: SemVer Cadence verification
    try:
        readme_text = Path("README.md").read_text(encoding="utf-8")
        if "v3.2.0" not in readme_text:
            print("[FAIL] Sürüm v3.2.0 README.md dosyasında bulunamadı.", file=sys.stderr)
            return False
        const_text = Path("CONSTITUTION.md").read_text(encoding="utf-8")
        if "v3.2.0" not in const_text:
            print("[FAIL] Sürüm v3.2.0 CONSTITUTION.md dosyasında bulunamadı.", file=sys.stderr)
            return False

        try:
            latest_tag = subprocess.check_output(
                ['git', 'describe', '--tags', '--abbrev=0'],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
            print(f"[+] Gate 6: SemVer Cadence:          [PASS] Version v3.2.0 confirmed (Active Tag: {latest_tag}).")
        except Exception:
            print("[+] Gate 6: SemVer Cadence:          [PASS] Version v3.2.0 ratified in specification.")
    except Exception as e:
        print(f"[FAIL] Gate 6 check failed: {e}", file=sys.stderr)
        return False

    print("-" * 68)
    print("[PASS] All ACME v3.2.0 Constitutional & Modular Norm Invariants PASS.")
    print("=" * 68)
    return True

if __name__ == "__main__":
    verify_all_flag = "--verify-all" in sys.argv or "-a" in sys.argv
    success = run_invariant_audit(verify_all=verify_all_flag)
    sys.exit(0 if success else 1)
