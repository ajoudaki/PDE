"""Launch one fresh isolated review and retain complete local provenance.

The assignment controls read/write scope. This utility does not pass task history,
choose a model, use Git, or create a user-owned desktop task.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assignment", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--run", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    run = args.run.resolve()
    assert run.is_relative_to(root / "data/generated/trained_data_response")
    assert not run.exists(), "fresh run required"
    assert not args.report.exists(), "report must not already exist"
    run.mkdir(parents=True)
    prompt = (
        "You are a fresh isolated reviewer. Read and follow only the neutral assignment at "
        + str(args.assignment.resolve()) + ". Your exclusive report is "
        + str(args.report.resolve()) + "; exclusive scratch is " + str(run) + ". "
        "The assignment names the complete allowed inputs. Do not read author history, "
        "study README, other reviewer reports, prior rounds, or unlisted sources. "
        "Do not perform author startup, use Git, edit an input, delegate, or contact another task. "
        "Read every required scientific line and repair truncated reads. Retain your full "
        "independent report and all checks. Your report must distinguish your fresh process "
        "identity from reusable /root role labels. Complete the assignment autonomously.\n"
    )
    command = ["codex", "exec", "--ephemeral", "--json", "--approve-for-me", "-C", str(root),
               "-o", str(run / "last_message.txt"), "-"]
    (run / "prompt.txt").write_text(prompt)
    (run / "command.json").write_text(json.dumps(command, indent=2) + "\n")
    with (run / "events.jsonl").open("w") as stdout, (run / "stderr.log").open("w") as stderr:
        result = subprocess.run(command, input=prompt, text=True, stdout=stdout, stderr=stderr)
    (run / "exit_code.txt").write_text(str(result.returncode) + "\n")
    print(f"isolated review exited {result.returncode}; report {args.report}")
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
