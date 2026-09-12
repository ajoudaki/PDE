"""Deterministic validation of the selected-file proposed edition.

This performs no training and imports no study or historical data into the
mathematical checks. Run with a fresh study-generated output directory.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from io import StringIO
import json
import math
from pathlib import Path
import platform
import re
import sys

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]


def digest(data):
    return sha256(data).hexdigest()


def main():
    manifest = json.loads((STUDY / "scientific_manifest_v2.json").read_text())
    for name, meta in manifest["files"].items():
        assert digest((STUDY / name).read_bytes()) == meta["sha256"], name
    out = Path(sys.argv[1]).resolve()
    assert out.is_relative_to(ROOT / "data/generated/nonlinear_selection_generalization")
    out.mkdir(parents=True, exist_ok=False)
    edition = out / "edition"
    (edition / "docs").mkdir(parents=True)
    old = (ROOT / "docs/global_nonlinear.md").read_bytes()
    assert digest(old) == manifest["source_slices"]["frozen_global_nonlinear_v2.md"]["full_source_sha256"]
    addition = (STUDY / "candidate_addition_v2.md").read_bytes()
    new = old + (b"\n" if old.endswith(b"\n") else b"\n\n") + addition
    (edition / "docs/global_nonlinear.md").write_bytes(new)
    (edition / "docs/README.md").write_bytes((STUDY / "candidate_docs_README_v2.md").read_bytes())
    (edition / "docs/NOTATION.md").write_bytes((STUDY / "frozen_NOTATION_v2.md").read_bytes())
    special = (ROOT / "docs/special_data_limits.md").read_bytes()
    assert digest(special) == manifest["source_slices"]["frozen_special_data_limits_v2.md"]["full_source_sha256"]
    (edition / "docs/special_data_limits.md").write_bytes(special)
    for frozen, name in [("frozen_AGENTS_v2.md", "AGENTS.md"),
                         ("frozen_WORKFLOW_v2.md", "RESEARCH_WORKFLOW.md")]:
        (edition / name).write_bytes((STUDY / frozen).read_bytes())

    # From this point all mathematical inputs are the standalone edition.
    book_path = edition / "docs/global_nonlinear.md"
    book = book_path.read_text()
    start = book.index("###### 5. Reproducible rational Gaussian certificate")
    section = book[start:book.index("##### C.4.5.2.", start)]
    program = section.split("```python\n", 1)[1].split("```", 1)[0]
    printed = StringIO()
    with redirect_stdout(printed):
        exec(compile(program, "standalone:C.4.5.1.5", "exec"), {})

    added = book[book.index("#### C.4.10. Generalization"):]
    assert "studies/" not in added and "data/generated" not in added
    assert added.count(r"\[") == added.count(r"\]")
    assert added.count(r"\(") == added.count(r"\)")
    labels = re.findall(r"\\tag\{([^}]+)\}", added)
    assert len(labels) == len(set(labels)), "Duplicate new equation labels"
    prior = book[:book.index("#### C.4.10. Generalization")]
    prior_labels = set(re.findall(r"\\tag\{([^}]+)\}", prior))
    assert not set(labels) & prior_labels
    expected_heading = "c410-generalization-during-a-finite-added-data-episode"
    assert expected_heading in (edition / "docs/README.md").read_text()
    assert book_path.read_bytes()[:len(old)] == old, "Earlier chapter bytes changed"

    # Exact independent elementary checks of the population/robust algebra.
    # The constant Fourier coefficient of sin^4(t) is binomial(4,2)/16;
    # sin^5(t) has no zero mode. This checks ||h(cos+sin)||_rho^2.
    psi_norm_squared = F(math.comb(4, 2), 16)
    assert psi_norm_squared == F(3, 8)
    assert all(5-2*j != 0 for j in range(6))
    # Completing-square coefficients for ||x+y||² >= ||x||²/2-||y||².
    assert [F(1)-F(1,2), F(2), F(1)+F(1)] == [F(1,2), F(2), F(2)]
    # Ratio of forcing lambda+2L0² to decay lambda/2 is 2+4L0²/lambda.
    for rate, norm_sq in [(F(1, 8), F(3)), (F(7, 3), F(20))]:
        assert (rate+2*norm_sq)/(rate/2) == 2*(1+2*norm_sq/rate)
    inverse_checks = []
    for radius, kt in [(0.5, 0.1), (0.01, 2.0), (1e-6, 5.0)]:
        eta = math.e * math.exp(-(math.sqrt(math.log(math.e/radius))+kt/2)**2)
        recovered = math.e * math.exp(-(math.sqrt(math.log(math.e/eta))-kt/2)**2)
        assert abs(recovered-radius) <= 2e-14*radius
        inverse_checks.append({"radius": radius, "KT": kt,
                               "inverse_roundtrip_relative_error": abs(recovered-radius)/radius})
    report = {
        "result": "PASS: exact reference assertions, algebra, inverse-modulus and assembly checks",
        "kind": "deterministic proof/edition checks; no training or empirical theorem",
        "python": platform.python_version(), "platform": platform.platform(),
        "validation_source_sha256": digest(Path(__file__).read_bytes()),
        "manifest_sha256": digest((STUDY / "scientific_manifest_v2.json").read_bytes()),
        "reference_program_sha256": digest(program.encode()),
        "reference_stdout": printed.getvalue(),
        "new_equation_count": len(labels), "inverse_checks": inverse_checks,
        "edition_files": {str(p.relative_to(edition)): digest(p.read_bytes())
                           for p in sorted(edition.rglob("*")) if p.is_file()},
        "limits": "These checks do not certify the analytic continuation or learning proofs. "
                  "Only new links/fragments and preservation are tested; unread old chapter "
                  "material is included as context, not re-audited. No PDF/exporter change."}
    (out / "validation.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
