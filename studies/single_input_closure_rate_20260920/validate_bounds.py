"""Deterministic reproduction of the maintained fitting-constant certificate.

Run from the repository root with python -B. No neural training or quadrature
trajectory is performed. The only executed dependency is the complete exact
rational Python certificate printed in the maintained chapter.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json


def main():
    chapter = Path("docs/global_nonlinear.md")
    text = chapter.read_text()
    marker = "The following complete Python program uses exact rational arithmetic,"
    start = text.index("```python\n", text.index(marker)) + len("```python\n")
    end = text.index("\n```", start)
    source = text[start:end]
    namespace = {"__name__": "__certificate__"}
    exec(compile(source, str(chapter) + "::C.4.5.1-certificate", "exec"), namespace)
    assert namespace["vlo"] > Fraction(1, 5)
    s = Fraction(6)
    b = 2 + s * s / 2
    cd = 2 * b + 1 + 2 * s * (b * b + b + 1)
    cr = 2 * s * (b + 1) + 3
    vsq = 1 + s * s * (b * b + 1)
    assert (b, cd, cr, vsq, 1 + 5 * vsq) == (20, 5093, 255, 14437, 72186)
    print(json.dumps({
        "certificate_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "chapter_sha256": hashlib.sha256(chapter.read_bytes()).hexdigest(),
        "certified_m_lower": str(namespace["vlo"]),
        "feature_horizon": 6,
        "state_lipschitz_constant": int(cd),
        "source_constant": int(cr),
        "physical_clock_factor": int(1 + 5 * vsq),
        "status": "PASS: exact rational certificate and comparison constants",
    }, indent=2))


if __name__ == "__main__":
    main()
