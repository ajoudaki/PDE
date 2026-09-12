"""Contained proof checks only; no neural training or numerical trajectory solver."""

import argparse
import contextlib
import hashlib
import io
import json
import platform
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = args.output.resolve()
    allowed = root / "data/generated/nonlinear_adaptation_advantage"
    if not output.is_relative_to(allowed):
        raise ValueError("Output must remain in this study's generated namespace")
    output.mkdir(parents=True, exist_ok=False)
    source = root / "docs/global_nonlinear.md"
    expected = "5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483"
    if digest(source) != expected:
        raise ValueError("Established source changed; reread before running its proof")
    section = source.read_text().split(
        "###### 5. Reproducible rational Gaussian certificate", 1
    )[1].split("##### C.4.5.2.", 1)[0]
    program = section.split("```python\n", 1)[1].split("```", 1)[0]
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(program, str(source) + ":C.4.5.1-certificate", "exec"), {})
    result = {
        "scope": "Exact rational Gaussian gate bounds in established C.4.5.1; no training",
        "source_sha256": digest(source),
        "runner_sha256": digest(Path(__file__)),
        "extracted_program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "stdout": capture.getvalue(),
        "result": "all exact rational assertions passed",
    }
    (output / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
