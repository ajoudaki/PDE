"""Re-run the complete established rational certificate; no training occurs."""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import platform
import sys

root = Path(__file__).resolve().parents[2]
book_path = root / "docs/global_nonlinear.md"
book = book_path.read_text()
start = book.index("###### 5. Reproducible rational Gaussian certificate")
section = book[start:book.index("##### C.4.5.2.", start)]
program = section.split("```python\n", 1)[1].split("```", 1)[0]
output = StringIO()
with redirect_stdout(output):
    exec(compile(program, str(book_path) + ":C.4.5.1.5", "exec"), {})

report = {
    "claim": "Established C.4.5 rational initialization/fitting certificate",
    "kind": "deterministic exact rational arithmetic, no training",
    "book_sha256": sha256(book_path.read_bytes()).hexdigest(),
    "extracted_program_sha256": sha256(program.encode()).hexdigest(),
    "check_script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "python": platform.python_version(),
    "platform": platform.platform(),
    "command": "python3 studies/nonlinear_selection_generalization/check_reference_certificate.py <new-output-directory>",
    "result": "PASS: all assertions completed",
    "stdout": output.getvalue(),
}
out = Path(sys.argv[1]).resolve()
allowed = (root / "data/generated/nonlinear_selection_generalization").resolve()
if not out.is_relative_to(allowed):
    raise ValueError("Output must be study-owned generated data")
out.mkdir(parents=True, exist_ok=False)
(out / "reference_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
