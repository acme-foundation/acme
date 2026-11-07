#!/usr/bin/env python3
"""
ACME CORE INVARIANT GATE & CONSTITUTIONAL VERIFIER (Pure Standard Library)
Self-Compiling Genesis Verifier (v3.2.0 - Systems Architecture 13-Gate Turnstile)
Serves as the Mechanical Gatekeeper Turnstile at the repository boundary.
Codifies Canonical Interlingua Invariant (INV-CANONICAL-INTERLINGUA / DoF = 0).
Codifies Mandatory Execution Registry (INV-MANDATORY-CASE-BINDING / DoF = 0).
Codifies Canonical Identifier Standard (INV-CANONICAL-IDENTIFIER / DoF = 0).
Codifies Pipeline Topology & Migration Invariant (INV-PIPELINE-MIGRATION / DoF = 0).
Codifies Flat Case Registry & Precedent Lineage (INV-FLAT-REGISTRY / INV-PRECEDENT-PROMOTION / DoF = 0).
Codifies Pipeline Expansion & Keystone Precedence (INV-PIPELINE-EXPANSION / INV-KEYSTONE-PRECEDENCE / DoF = 0).
"""

import os
import sys
import re
import subprocess
from pathlib import Path

def ensure_git_hooks() -> None:
    hooks_dir = Path(".git/hooks")
    if not hooks_dir.is_dir():
        return

    pre_commit_path = hooks_dir / "pre-commit"
    commit_msg_path = hooks_dir / "commit-msg"

    py_exec = sys.executable.replace("\\", "/")

    pre_commit_script = (
        "#!/bin/sh\n"
        "# ACME Mandatory Pre-Commit Hook (Gatekeeper Turnstile)\n"
        f'if [ -f "{py_exec}" ]; then\n'
        f'    "{py_exec}" verify.py --verify-all\n'
        "elif command -v py >/dev/null 2>&1; then\n"
        "    py -3 verify.py --verify-all\n"
        "else\n"
        "    python verify.py --verify-all\n"
        "fi\n"
    )

    commit_msg_script = (
        "#!/bin/sh\n"
        "# ACME Mandatory Commit Message Hook (INV-COMMIT-LINKAGE-02)\n"
        f'if [ -f "{py_exec}" ]; then\n'
        f'    "{py_exec}" verify.py --check-commit-msg "$1"\n'
        "elif command -v py >/dev/null 2>&1; then\n"
        "    py -3 verify.py --check-commit-msg \"$1\"\n"
        "else\n"
        "    python verify.py --check-commit-msg \"$1\"\n"
        "fi\n"
    )

    try:
        if not pre_commit_path.is_file() or pre_commit_path.read_text(encoding="utf-8") != pre_commit_script:
            pre_commit_path.write_text(pre_commit_script, encoding="utf-8")
        if not commit_msg_path.is_file() or commit_msg_path.read_text(encoding="utf-8") != commit_msg_script:
            commit_msg_path.write_text(commit_msg_script, encoding="utf-8")
    except Exception:
        pass

def verify_commit_message_file(msg_path: Path) -> bool:
    if not msg_path.is_file():
        print(f"[FAIL] Commit message file not found: {msg_path}", file=sys.stderr)
        return False
    lines = [
        line.strip()
        for line in msg_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if not lines:
        print("[FAIL] Commit message is empty.", file=sys.stderr)
        return False
    first_line = lines[0]
    case_pattern = re.compile(r'^\[(?:CAS|CASE)-[0-9A-Fa-f]{3,4}\]', re.IGNORECASE)
    if not case_pattern.match(first_line):
        print(
            f"[FAIL] (INV-COMMIT-LINKAGE-02) Commit message must start with '[CAS-XXX]' tag: '{first_line}'",
            file=sys.stderr
        )
        return False
    print(f"[PASS] Commit message case citation verified: {first_line}")
    return True

def run_invariant_audit(verify_all: bool = False) -> bool:
    print("=" * 68)
    print("      ACME GENESIS CONSTITUTIONAL INTEGRITY & INVARIANT GATE (v3.2.0)      ")
    print("=" * 68)

    root = Path(".")

    # Ensure pre-commit and commit-msg hooks are configured
    ensure_git_hooks()

    # Gate 1: Zero-Code Invariant: No code artifacts tracked in core (except verify.py and migrations/*.py)
    forbidden_exts = ['.py', '.sh', '.exe', '.dll', '.bin']
    try:
        tracked = subprocess.check_output(['git', 'ls-files'], text=True).splitlines()
        for f in tracked:
            norm_f = Path(f).as_posix()
            if norm_f == 'verify.py':
                continue
            if norm_f.startswith('migrations/') and norm_f.endswith('.py'):
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
            if posix_path.startswith("migrations/") and posix_path.endswith(".py"):
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

    # Gate 3: Constitutional Parity: Articles 0 to 15 in CONSTITUTION.md
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
            "ARTICLE 7: PRECEDENT CACHE",
            "ARTICLE 8: CANONICAL LANGUAGE & INTERLINGUA PROTOCOL",
            "ARTICLE 9: MANDATORY TEMPORAL ALIGNMENT & PROCEDURAL PRECEDENCE",
            "ARTICLE 10: ZERO-RHETORIC & OPERATIONAL SPECIFICATION",
            "ARTICLE 11: MANDATORY EXECUTION REGISTRY",
            "ARTICLE 12: CANONICAL NAMING & LEXICAL TRACEABILITY",
            "ARTICLE 13: PIPELINE TOPOLOGY & AUTOMATED MIGRATION",
            "ARTICLE 14: CASE TOPOLOGY, LOCAL SCOPING & PRECEDENT PROMOTION",
            "ARTICLE 15: DYNAMIC PIPELINE EXPANSION & KEYSTONE PRECEDENCE",
            "ARTICLE 16: INCEPTION RIGOR & EXPLORATORY SPIKES"
        ]
        for art in required_articles:
            if art not in const_text:
                print(f"[FAIL] Missing constitutional article: {art}", file=sys.stderr)
                return False
        print("[+] Gate 3: Constitutional Parity:       [PASS] Articles 0 to 16 ratified in CONSTITUTION.md.")
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
            Path("templates/CAS_TEMPLATE.md"),
            Path("templates/PRE_TEMPLATE.md"),
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
            Path("precedents/PRE_001_stream_quarantine.md")
        ]
        for prec in required_precedents:
            if not prec.is_file():
                print(f"[FAIL] Missing precedent ruling: {prec}", file=sys.stderr)
                return False
            if len(prec.read_bytes()) < 100:
                print(f"[FAIL] Precedent ruling too small: {prec}", file=sys.stderr)
                return False
        print("[+] Gate 5: Templates & Precedents:      [PASS] 3 canonical templates and precedent registry verified.")
    except Exception as e:
        print(f"[FAIL] Gate 5 check failed: {e}", file=sys.stderr)
        return False

    # Gate 6: Adjective Density Gate (<= 0.02)
    try:
        subjective_words = ['fast', 'perfect', 'wonderful', 'powerful', 'easy', 'flawless', 'super', 'legendary', 'urgent', 'modern', 'lightweight']
        total_words = 0
        subj_count = 0
        audit_paths = [
            Path("CONSTITUTION.md"),
            Path("README.md"),
            Path("migrations/README.md"),
            Path("pipelines/README.md")
        ] + list(Path("norms").rglob("*.md")) + list(Path("precedents").rglob("*.md"))

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

    # Gate 8: Mandatory Case Registry & Zero Unregistered Execution (INV-MANDATORY-CASE-BINDING)
    try:
        cases_dir = Path("cases")
        case_commit_pattern = re.compile(r'^\[(?:CAS|CASE)-([0-9A-Fa-f]{3,4})\]', re.IGNORECASE)

        # Inspect working tree status for any uncommitted changes
        status_output = subprocess.check_output(
            ['git', 'status', '--porcelain', '-uall'],
            text=True
        ).splitlines()

        modified_files = []
        for line in status_output:
            if not line.strip():
                continue
            raw_path = line[3:].strip()
            if " -> " in raw_path:
                raw_path = raw_path.split(" -> ")[1].strip()
            if raw_path.startswith('"') and raw_path.endswith('"'):
                raw_path = raw_path[1:-1]
            posix_f = Path(raw_path).as_posix()
            parts = posix_f.split("/")
            if ".git" in parts or ".tmp" in parts:
                continue
            if Path(posix_f).is_dir():
                for sub_p in Path(posix_f).rglob("*"):
                    if sub_p.is_file():
                        sub_posix = sub_p.as_posix()
                        if not any(x in sub_posix.split("/") for x in [".git", ".tmp"]):
                            modified_files.append(sub_posix)
            else:
                modified_files.append(posix_f)

        if modified_files:
            if not cases_dir.is_dir():
                print("[FAIL] Gate 8: Working tree modifications detected, but 'cases/' directory does not exist.", file=sys.stderr)
                return False
            case_files = list(cases_dir.glob("CAS_*.md")) + list(cases_dir.glob("CASE_*.md"))
            if not case_files:
                print("[FAIL] Gate 8: Working tree modifications detected, but no case ledger found under 'cases/'.", file=sys.stderr)
                return False

            active_cases = []
            for cf in case_files:
                content = cf.read_text(encoding="utf-8")
                state_match = re.search(r'(?:Execution State|STATUS)[^\n:]*:\s*\*?\*?\s*(ACTIVE)', content, re.IGNORECASE)
                if state_match:
                    whitelisted = set()
                    in_scope = False
                    for c_line in content.splitlines():
                        stripped = c_line.strip()
                        if re.search(r'Target Scope.*:', stripped, re.IGNORECASE):
                            in_scope = True
                            continue
                        if in_scope:
                            if stripped.startswith("- **") or stripped.startswith("##") or (stripped and not stripped.startswith("-") and not stripped.startswith("*")):
                                in_scope = False
                            else:
                                bullet_match = re.match(r'^\s*[-*]\s+(.*)$', c_line)
                                if bullet_match:
                                    w_path = bullet_match.group(1).strip().strip('`').strip()
                                    if w_path and not w_path.startswith("["):
                                        whitelisted.add(Path(w_path).as_posix())
                    active_cases.append((cf, whitelisted))

            if not active_cases:
                print("[FAIL] Gate 8: Working tree modifications detected, but no case in 'cases/' is marked 'ACTIVE'.", file=sys.stderr)
                return False

            for mf in modified_files:
                covered = False
                for cf, whitelisted in active_cases:
                    if mf == cf.as_posix() or mf.startswith("cases/CAS_") or mf.startswith("cases/CASE_"):
                        covered = True
                        break
                    if mf in whitelisted:
                        covered = True
                        break
                if not covered:
                    print(f"[FAIL] Gate 8 (INV-DIFF-CONTAINMENT-03): File mutation '{mf}' outside whitelisted scope of active cases.", file=sys.stderr)
                    return False

            print(f"[+] Gate 8: Mandatory Case Registry:     [PASS] Active case ledger validated for {len(modified_files)} working tree mutation(s).")
        else:
            try:
                head_commit_msg = subprocess.check_output(
                    ['git', 'log', '-1', '--pretty=%B'],
                    text=True
                ).strip()
                first_line = head_commit_msg.splitlines()[0] if head_commit_msg else ""
                legacy_anchor_hashes = {'c50a958', 'd0809ae', '419deb4', '3e56c2d', '0a96847'}
                head_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()

                commit_match = case_commit_pattern.match(first_line)
                if commit_match:
                    case_tag = commit_match.group(1).upper()
                    matching_cases = list(cases_dir.glob(f"CAS_{case_tag}*.md")) + list(cases_dir.glob(f"CASE_{case_tag}*.md"))
                    if not matching_cases:
                        print(f"[FAIL] Gate 8: Commit tag '[CAS-{case_tag}]' has no matching ledger under 'cases/'.", file=sys.stderr)
                        return False
                    print(f"[+] Gate 8: Mandatory Case Registry:     [PASS] HEAD commit citation '[CAS-{case_tag}]' verified against case registry.")
                elif head_hash in legacy_anchor_hashes:
                    print(f"[+] Gate 8: Mandatory Case Registry:     [PASS] Clean tree. Anchor commit {head_hash} verified (pre-Gate 8 baseline).")
                else:
                    print(f"[FAIL] Gate 8: Commit message lacking canonical '[CAS-XXX]' tag: '{first_line}'", file=sys.stderr)
                    return False
            except Exception as e:
                print(f"[FAIL] Gate 8 git log check failed: {e}", file=sys.stderr)
                return False
    except Exception as e:
        print(f"[FAIL] Gate 8 check failed: {e}", file=sys.stderr)
        return False

    # Gate 9: Lexical Parity & Naming Syntax (INV-CANONICAL-IDENTIFIER)
    try:
        registered_tags = {'CAS', 'INV', 'PRE', 'COR', 'ING', 'PRO', 'MIG'}
        canonical_pattern = re.compile(r'^[A-Z]{3}_[0-9A-Fa-f]{3}_[a-zA-Z0-9_]+$')
        syntax_prefix_pattern = re.compile(r'^[A-Z]{3}_[0-9A-Fa-f]{3}_')

        audit_dirs = [Path("cases"), Path("norms"), Path("precedents")]
        violations = []
        total_audited = 0

        for ad in audit_dirs:
            if not ad.is_dir():
                continue
            for doc in ad.rglob("*.md"):
                total_audited += 1
                stem = doc.stem
                if not syntax_prefix_pattern.match(doc.name) or not canonical_pattern.match(stem):
                    violations.append(f"Invalid file name syntax: {doc}")
                tag = stem[:3]
                if tag not in registered_tags:
                    violations.append(f"Unregistered namespace token '{tag}' in file: {doc}")

                content = doc.read_text(encoding="utf-8")
                lines = [l.strip() for l in content.splitlines() if l.strip()]
                if not lines:
                    violations.append(f"Empty document: {doc}")
                    continue
                header_line = lines[0]
                if not header_line.startswith("#"):
                    violations.append(f"Missing H1 heading in {doc}: '{header_line}'")
                    continue
                header_id = re.sub(r'^#+\s*(?:CASE|NORM|PRECEDENT)?\s*:?\s*', '', header_line).strip()
                if not syntax_prefix_pattern.match(header_id):
                    violations.append(f"Invalid ledger title in {doc}: '{header_line}' (resolved id: '{header_id}')")

        if violations:
            for v in violations:
                print(f"[FAIL] Gate 9 (INV-CANONICAL-IDENTIFIER): {v}", file=sys.stderr)
            return False

        print(f"[+] Gate 9: Lexical Parity & Naming:     [PASS] All {total_audited} artifacts and ledger titles verified under ^[A-Z]{{3}}_[0-9A-F]{{3}}_.")
    except Exception as e:
        print(f"[FAIL] Gate 9 check failed: {e}", file=sys.stderr)
        return False

    # Gate 10: Pipeline Topology & Path Whitelist (INV-PIPELINE-TOPOLOGY-01)
    try:
        whitelisted_root_dirs = {'.git', '.tmp', 'cases', 'norms', 'precedents', 'templates', 'migrations', 'pipelines'}
        whitelisted_root_files = {'.gitignore', 'README.md', 'CONSTITUTION.md', 'verify.py'}
        required_topology_dirs = {'cases', 'norms', 'precedents', 'templates', 'migrations', 'pipelines'}

        for entry in root.iterdir():
            if entry.is_dir():
                if entry.name not in whitelisted_root_dirs:
                    print(f"[FAIL] Gate 10 (INV-PIPELINE-TOPOLOGY-01): Unauthorized root directory detected: '{entry.name}'.", file=sys.stderr)
                    return False
            elif entry.is_file():
                if entry.name not in whitelisted_root_files:
                    print(f"[FAIL] Gate 10 (INV-PIPELINE-TOPOLOGY-01): Unauthorized root file detected: '{entry.name}'.", file=sys.stderr)
                    return False

        for req_dir in required_topology_dirs:
            p = root / req_dir
            if not p.is_dir():
                print(f"[FAIL] Gate 10 (INV-PIPELINE-TOPOLOGY-01): Missing mandatory pipeline topology directory: '{req_dir}'.", file=sys.stderr)
                return False

        migrations_readme = Path("migrations/README.md")
        if not migrations_readme.is_file() or len(migrations_readme.read_bytes()) < 50:
            print("[FAIL] Gate 10 (INV-PIPELINE-TOPOLOGY-01): Missing or corrupted 'migrations/README.md'.", file=sys.stderr)
            return False

        pipelines_readme = Path("pipelines/README.md")
        if not pipelines_readme.is_file() or len(pipelines_readme.read_bytes()) < 50:
            print("[FAIL] Gate 10 (INV-PIPELINE-TOPOLOGY-01): Missing or corrupted 'pipelines/README.md'.", file=sys.stderr)
            return False

        print("[+] Gate 10: Pipeline Topology:          [PASS] Filesystem topology validated against canonical whitelist.")
    except Exception as e:
        print(f"[FAIL] Gate 10 check failed: {e}", file=sys.stderr)
        return False

    # Gate 11: Flat Case Registry (INV-FLAT-REGISTRY-01)
    try:
        cases_dir = Path("cases")
        if not cases_dir.is_dir():
            print("[FAIL] Missing 'cases/' directory.", file=sys.stderr)
            return False
        subdirs = [p for p in cases_dir.iterdir() if p.is_dir()]
        if subdirs:
            print(f"[FAIL] Gate 11 (INV-FLAT-REGISTRY-01): Nested case directory detected: {subdirs[0].as_posix()}", file=sys.stderr)
            return False
        case_files = list(cases_dir.glob("*.md"))
        print(f"[+] Gate 11: Flat Case Registry:         [PASS] Flat topology verified under cases/ ({len(case_files)} case(s), zero subdirectories).")
    except Exception as e:
        print(f"[FAIL] Gate 11 check failed: {e}", file=sys.stderr)
        return False

    # Gate 12: Precedent Format Integrity (INV-PRECEDENT-PROMOTION-03)
    try:
        precedents_dir = Path("precedents")
        if not precedents_dir.is_dir():
            print("[FAIL] Missing 'precedents/' directory.", file=sys.stderr)
            return False

        pre_filename_pattern = re.compile(r'^PRE_[0-9A-Fa-f]{3}_[a-z0-9_]+\.md$')
        pre_files = list(precedents_dir.rglob("*.md"))
        if not pre_files:
            print("[FAIL] No precedent files found under 'precedents/'.", file=sys.stderr)
            return False

        required_schema_markers = [
            "Ratified Invariant:",
            "Originating Workspace:",
            "Source Case Ref:",
            "Merkle Anchor:",
            "Status: RATIFIED_CANONICAL",
            "## 1. ANOMALY & CONTEXT",
            "## 2. RATIFIED RULE (THE RULING)",
            "## 3. VERIFICATION ASSERTION"
        ]

        for pf in pre_files:
            if not pre_filename_pattern.match(pf.name):
                print(f"[FAIL] Gate 12: Precedent file violates naming pattern ^PRE_[0-9A-F]{{3}}_[a-z0-9_]+\\.md$: {pf.name}", file=sys.stderr)
                return False

            content = pf.read_text(encoding="utf-8")
            lines = [l.strip() for l in content.splitlines() if l.strip()]
            if not lines:
                print(f"[FAIL] Gate 12: Empty precedent file: {pf}", file=sys.stderr)
                return False

            first_line = lines[0]
            if not re.match(r'^#\s*PRECEDENT:\s*PRE_[0-9A-Fa-f]{3}_', first_line):
                print(f"[FAIL] Gate 12: Invalid precedent title in {pf}: '{first_line}'", file=sys.stderr)
                return False

            for marker in required_schema_markers:
                if marker not in content:
                    print(f"[FAIL] Gate 12: Precedent file {pf} missing required schema marker: '{marker}'", file=sys.stderr)
                    return False

        print(f"[+] Gate 12: Precedent Format:           [PASS] All {len(pre_files)} precedent file(s) conform to PRE_TEMPLATE.md schema.")
    except Exception as e:
        print(f"[FAIL] Gate 12 check failed: {e}", file=sys.stderr)
        return False

    # Gate 13: Unregistered Domain & Asset Protection (INV-PIPELINE-EXPANSION-01 / INV-KEYSTONE-PRECEDENCE-02)
    try:
        pipelines_dir = Path("pipelines")
        asset_exts = {'.wav', '.mp3', '.ogg', '.flac', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.bin', '.ttf', '.otf'}

        # Gather whitelisted ingress/egress directories from registered pipeline definitions
        registered_asset_dirs = set()
        if pipelines_dir.is_dir():
            for p_file in pipelines_dir.glob("*.yaml"):
                content = p_file.read_text(encoding="utf-8")
                dir_matches = re.findall(r'directory:\s*["\']?([^"\']+)["\']?', content)
                for d in dir_matches:
                    registered_asset_dirs.add(Path(d.strip()).as_posix())

        # Scan repository for unmanaged modal assets
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            posix_path = p.as_posix()
            parts = posix_path.split("/")
            if ".git" in parts or ".tmp" in parts:
                continue
            if p.suffix.lower() in asset_exts:
                is_covered = any(posix_path.startswith(rad) for rad in registered_asset_dirs)
                if not is_covered:
                    print(f"[FAIL] Gate 13 (INV-PIPELINE-EXPANSION-01): Unregistered asset ingress detected: {p}", file=sys.stderr)
                    return False

        # Verify keystone precedence in case ledgers
        cases_dir = Path("cases")
        if cases_dir.is_dir():
            for c_file in cases_dir.glob("CAS_*.md"):
                c_content = c_file.read_text(encoding="utf-8")
                is_secondary_asset_case = bool(
                    re.search(r'Type:\s*ASSET', c_content, re.IGNORECASE) or
                    re.search(r'Domain:\s*asset', c_content, re.IGNORECASE)
                )
                if is_secondary_asset_case:
                    dep_match = re.search(r'Depends On:\s*\[?(CAS-[0-9A-Fa-f]{3,4})\]?', c_content, re.IGNORECASE)
                    if not dep_match:
                        print(f"[FAIL] Gate 13 (INV-KEYSTONE-PRECEDENCE-02): Asset case {c_file.name} lacks required keystone 'Depends On: [CAS-XXX]'.", file=sys.stderr)
                        return False
                    dep_case_tag = dep_match.group(1).upper().replace("CAS-", "")
                    matching_dep = list(cases_dir.glob(f"CAS_{dep_case_tag}*.md"))
                    if not matching_dep:
                        print(f"[FAIL] Gate 13 (INV-KEYSTONE-PRECEDENCE-02): Keystone dependency 'CAS-{dep_case_tag}' in {c_file.name} not found.", file=sys.stderr)
                        return False
                    dep_content = matching_dep[0].read_text(encoding="utf-8")
                    is_closed = bool(re.search(r'(?:Execution State|Status)\s*:\s*(?:RESOLVED|CLOSED)', dep_content, re.IGNORECASE))
                    if not is_closed:
                        print(f"[FAIL] Gate 13 (INV-KEYSTONE-PRECEDENCE-02): Keystone dependency 'CAS-{dep_case_tag}' is not CLOSED/RESOLVED.", file=sys.stderr)
                        return False

        print("[+] Gate 13: Asset Protection & Keystone: [PASS] Domain expansion circuit breaker and keystone precedence verified.")
    except Exception as e:
        print(f"[FAIL] Gate 13 check failed: {e}", file=sys.stderr)
        return False

    # Gate 14: Inception File Compliance (INV-INCEPTION-RIGOR / INV-INCEPTION-CODE-BAN-01 / INV-ANTI-TUTORIAL-02)
    try:
        cases_dir = Path("cases")
        if cases_dir.is_dir():
            for c_file in cases_dir.glob("CAS_*.md"):
                c_content = c_file.read_text(encoding="utf-8")
                is_spike = bool(re.search(r'Type:\s*SPIKE\b', c_content, re.IGNORECASE))
                first_line = c_content.splitlines()[0] if c_content.splitlines() else ""
                has_inception = bool(
                    "INCEPTION" in c_file.name.upper() or
                    re.search(r'#.*INCEPTION\b', first_line, re.IGNORECASE) or
                    re.search(r'Station\s*/\s*Node:\s*Inception\b', c_content, re.IGNORECASE)
                )

                if is_spike or has_inception:
                    # Check for implementation code block
                    code_block_match = re.search(
                        r'```\s*(?:python|py|javascript|js|typescript|ts|rust|rs|c|cpp|c\+\+|csharp|cs|go|golang|java|bash|sh|shell|zsh|powershell|ps1|ruby|rb|php|swift|kotlin|kt|scala|lua|perl|dart|zig|sql|html|css)\b',
                        c_content,
                        re.IGNORECASE
                    )
                    if code_block_match:
                        print(f"[FAIL] Gate 14 (INV-INCEPTION-CODE-BAN-01): FAIL: Code block detected inside Inception case: {c_file.name}", file=sys.stderr)
                        return False

                    # Check for mandatory headings
                    has_decision_matrix = bool(re.search(r'^##\s*1\.\s*BLOCKING\s+DECISION\s+MATRIX', c_content, re.MULTILINE | re.IGNORECASE))
                    has_structural_skeleton = bool(re.search(r'^##\s*2\.\s*STRUCTURAL\s+SKELETON', c_content, re.MULTILINE | re.IGNORECASE))

                    if not has_decision_matrix:
                        print(f"[FAIL] Gate 14 (INV-ANTI-TUTORIAL-02): Inception case {c_file.name} missing required heading '## 1. BLOCKING DECISION MATRIX'.", file=sys.stderr)
                        return False

                    if not has_structural_skeleton:
                        print(f"[FAIL] Gate 14 (INV-ANTI-TUTORIAL-02): Inception case {c_file.name} missing required heading '## 2. STRUCTURAL SKELETON'.", file=sys.stderr)
                        return False

        print("[+] Gate 14: Inception File Compliance:  [PASS] Zero code emission and structural headings verified for spike cases.")
    except Exception as e:
        print(f"[FAIL] Gate 14 check failed: {e}", file=sys.stderr)
        return False

    print("-" * 68)
    print("[PASS] All 14 ACME v3.2.0 Systems Architecture & Invariant Gates PASS.")
    print("=" * 68)
    return True

if __name__ == "__main__":
    if "--check-commit-msg" in sys.argv:
        idx = sys.argv.index("--check-commit-msg")
        if idx + 1 < len(sys.argv):
            msg_file = Path(sys.argv[idx + 1])
            is_valid = verify_commit_message_file(msg_file)
            sys.exit(0 if is_valid else 1)
        else:
            print("[FAIL] Missing commit message file path.", file=sys.stderr)
            sys.exit(1)

    verify_all_flag = "--verify-all" in sys.argv or "-a" in sys.argv
    success = run_invariant_audit(verify_all=verify_all_flag)
    sys.exit(0 if success else 1)
