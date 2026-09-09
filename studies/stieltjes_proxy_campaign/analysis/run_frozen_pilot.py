#!/usr/bin/env python3
"""Command-line entry point for the frozen successor-02 offline analysis."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from analysis.pilot_runner import (  # noqa: E402
    PilotAnalysisInvalid,
    analyze_pilot,
    write_json_atomic,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--analysis-config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = analyze_pilot(args.summary, args.config, args.analysis_config)
        write_json_atomic(args.output, result)
        return 0
    except Exception as exc:
        # A failure certificate contains no trajectory values.  It prevents a
        # caller from confusing an implementation/provenance failure with a
        # contrary scientific result.
        failure = {
            "schema_version": 1,
            "status": "inconclusive_analysis_failure",
            "protocol_result": "inconclusive",
            "failure_type": type(exc).__name__,
            "reason": str(exc),
        }
        try:
            write_json_atomic(args.output, failure)
        except FileExistsError:
            pass
        print(json.dumps(failure, sort_keys=True), file=sys.stderr)
        return 2 if isinstance(exc, PilotAnalysisInvalid) else 1


if __name__ == "__main__":
    raise SystemExit(main())

