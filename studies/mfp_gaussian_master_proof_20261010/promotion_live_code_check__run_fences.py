#!/usr/bin/env python3
"""Run every Python fenced block in an MFP guide in independent namespaces."""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import traceback
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("guide", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=False)
    text = args.guide.read_text(encoding="utf-8")
    blocks = re.findall(r"```(?:python|py)\n(.*?)```", text, flags=re.DOTALL)
    assert len(blocks) == 5, f"expected 5 Python fences, found {len(blocks)}"
    results = []
    for number, block in enumerate(blocks, start=1):
        stdout, stderr = io.StringIO(), io.StringIO()
        result = {"block": number, "source": block}
        try:
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                exec(compile(block, f"{args.guide}:python-fence-{number}", "exec"), {"__name__": "__main__"})
            result["exit_code"] = 0
        except Exception:
            result["exit_code"] = 1
            result["traceback"] = traceback.format_exc()
        result["stdout"] = stdout.getvalue()
        result["stderr"] = stderr.getvalue()
        (args.output_dir / f"fence_{number}.log").write_text(
            result["stdout"] + result["stderr"] + result.get("traceback", ""), encoding="utf-8"
        )
        results.append(result)
    (args.output_dir / "results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    return 0 if all(item["exit_code"] == 0 for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
