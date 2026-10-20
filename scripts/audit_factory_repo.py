#!/usr/bin/env python3
"""
Static compliance auditor for SaaS Factory repositories and product workspaces.
Checks Cloudflare Python Worker limits, security settings, UI rules, and growth guardrails.
"""

import os
import re
import sys
from pathlib import Path

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002702-\U000027B0"
    "\U0001F900-\U0001F9FF"
    "]+",
    flags=re.UNICODE,
)

HARDCODED_PLAN_PATTERN = re.compile(
    r"""(?:\.plan\s*[!=]=\s*['"](?:free|scout|pro|autopilot|agency|enterprise)['"])""",
    re.IGNORECASE,
)


def audit_wrangler_configs(root: Path, findings: list[str]) -> None:
    wrangler_files = list(root.rglob("wrangler.toml")) + list(root.rglob("wrangler.json*"))
    if not wrangler_files:
        findings.append("[WARN] Edge: No wrangler.toml or wrangler.jsonc found in target path.")
        return

    for wf in wrangler_files:
        content = wf.read_text(encoding="utf-8", errors="ignore")
        rel = wf.relative_to(root)
        if "workers_dev = true" in content or '"workers_dev": true' in content:
            findings.append(f"[FAIL] Edge ({rel}): workers_dev must be disabled in production (Custom Apex Domains Only).")
        if "cpu_ms" not in content:
            findings.append(f"[WARN] Edge ({rel}): Missing explicit cpu_ms = 1000 cap on HTTP requests.")
        if "dlq" not in content.lower() and "queues" in content.lower():
            findings.append(f"[FAIL] Queues ({rel}): Queue definition detected without a paired *-dlq Dead-Letter Queue.")


def audit_python_files(root: Path, findings: list[str]) -> None:
    for py_file in root.rglob("*.py"):
        if any(part in py_file.parts for part in (".venv", "venv", "node_modules", "__pycache__", "migrations")):
            continue
        content = py_file.read_text(encoding="utf-8", errors="ignore")
        rel = py_file.relative_to(root)

        # Check hardcoded plan strings vs entitlements.can()
        if HARDCODED_PLAN_PATTERN.search(content):
            findings.append(
                f"[FAIL] Entitlements ({rel}): Hardcoded plan string check found. Use entitlements.can(subject, 'feature')."
            )

        # Check Django settings security rules
        if py_file.name in ("settings.py", "base.py", "production.py"):
            if "SESSION_COOKIE_SECURE" in content and "SESSION_COOKIE_SECURE = True" not in content:
                findings.append(f"[FAIL] Security ({rel}): SESSION_COOKIE_SECURE must be True.")
            if "__Host-" not in content and "SESSION_COOKIE_NAME" in content:
                findings.append(f"[FAIL] Security ({rel}): Session cookie must use strict __Host- prefix.")
            if re.search(r"SESSION_COOKIE_DOMAIN\s*=\s*['\"]\.[a-zA-Z0-9.-]+['\"]", content):
                findings.append(f"[FAIL] Security ({rel}): Wildcard SESSION_COOKIE_DOMAIN is prohibited.")


def audit_templates_and_styles(root: Path, findings: list[str]) -> None:
    template_files = list(root.rglob("*.html")) + list(root.rglob("*.css"))
    found_1440_grid = False

    for tf in template_files:
        if any(part in tf.parts for part in (".venv", "venv", "node_modules")):
            continue
        content = tf.read_text(encoding="utf-8", errors="ignore")
        rel = tf.relative_to(root)

        if "1440px" in content:
            found_1440_grid = True

        if tf.suffix == ".html" and EMOJI_PATTERN.search(content):
            findings.append(
                f"[FAIL] UI Standard ({rel}): Unicode emoji detected in HTML template. Use 100% vector SVG icons via IconKit."
            )

    if template_files and not found_1440_grid:
        findings.append("[WARN] UI Standard: Canonical 1440px grid (max-width: 1440px) not detected in HTML/CSS files.")


def main() -> int:
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    if not target.exists():
        print(f"Error: Target path {target} does not exist.")
        return 1

    findings: list[str] = []
    audit_wrangler_configs(target, findings)
    audit_python_files(target, findings)
    audit_templates_and_styles(target, findings)

    print(f"=== SaaS Factory Compliance Audit: {target.name} ===")
    if not findings:
        print("PASS: All static checks passed (Edge limits, __Host- cookies, Entitlements, IconKit SVGs, 1440px grid).")
        return 0

    for item in findings:
        print(f" - {item}")
    return 1 if any(f.startswith("[FAIL]") for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
