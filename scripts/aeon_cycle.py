#!/usr/bin/env python3
"""AEON-LORN-15X registered cycle entrypoint. Default is dry-run."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"(api[_-]?key|token|secret|password)\s*=\s*['\"][^'\"]+['\"]", re.I),
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    re.compile(r"LORNT_GH_TOKEN|GH_TOKEN|GITHUB_TOKEN|AWS_SECRET"),
]

DEFAULT_TOPIC = {
    "topic": "Orbital-Hydroponic-AI-Telemetry",
    "description": "Closed-loop nutrient and lighting telemetry sketch for habitat hydroponics.",
    "stack": "Python / FastAPI / Docker",
}


def secret_hits(text: str) -> list[str]:
    hits = []
    for pat in SECRET_PATTERNS:
        for m in pat.finditer(text):
            hits.append(m.group(0)[:48])
    return hits


def scaffold(topic: str, description: str, stack: str) -> dict[str, str]:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return {
        "README.md": f"# {topic}\n\n{description}\n",
        "main.py": (
            "#!/usr/bin/env python3\n"
            f'"""{topic} local stub. Not a flight system."""\n'
            "def health() -> dict:\n"
            "    return {\"ok\": True, \"mode\": \"stub\"}\n\n"
            "if __name__ == \"__main__\":\n"
            "    print(health())\n"
        ),
        "Dockerfile": (
            "FROM python:3.12-slim\nWORKDIR /app\nCOPY main.py .\n"
            'CMD ["python", "main.py"]\n'
        ),
        "pyproject.toml": f'[project]\nname = "aeon-{slug}"\nversion = "0.0.1"\n',
    }


def main() -> int:
    p = argparse.ArgumentParser(description="AEON-LORN-15X one-cycle runner")
    p.add_argument("--topic", default=DEFAULT_TOPIC["topic"])
    p.add_argument("--description", default=DEFAULT_TOPIC["description"])
    p.add_argument("--stack", default=DEFAULT_TOPIC["stack"])
    p.add_argument("--apply", action="store_true")
    p.add_argument("--out", default="/home/workdir/artifacts/AEON-LORN-15X")
    args = p.parse_args()
    allow = os.environ.get("AEON_ALLOW_APPLY") == "1"
    mode = "apply" if args.apply and allow else "dry-run"
    wake_id = datetime.now(timezone.utc).strftime("wake-%Y%m%dT%H%M%SZ")
    cycle_dir = Path(args.out) / "cycles" / wake_id
    cycle_dir.mkdir(parents=True, exist_ok=True)
    files = scaffold(args.topic, args.description, args.stack)
    hits = []
    for name, content in files.items():
        hits.extend(secret_hits(content))
        (cycle_dir / name).write_text(content, encoding="utf-8")
    class13 = "REFUSE" if hits else "PASS"
    git_plan = "DISCARDED" if hits else ("WOULD-PUSH" if mode == "dry-run" else "APPLY-PLAN")
    slug = re.sub(r"[^a-z0-9]+", "-", args.topic.lower()).strip("-")
    receipt = {
        "daemon": "AEON-LORN-15X",
        "wake_id": wake_id,
        "mode": mode,
        "topic": args.topic,
        "class13": class13,
        "secret_scan": "REFUSE" if hits else "PASS",
        "artifact": str(cycle_dir),
        "git_plan": git_plan,
        "target": f"Lornt1666/aeon-{slug}",
        "live_github_called": False,
    }
    (cycle_dir / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(f"[CLASS 01] mode={mode} wake_id={wake_id}")
    print(f"[CLASS 13] {class13}")
    print(f"[CLASS 15] {git_plan} target=Lornt1666/aeon-{slug}")
    print(f"[RECEIPT] {cycle_dir / 'receipt.json'}")
    if mode == "dry-run":
        print("[dry-run] no repository created, no git push")
    return 2 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
