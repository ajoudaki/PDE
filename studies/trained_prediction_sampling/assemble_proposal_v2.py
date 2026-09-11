"""Preserve v1 and assemble the corrected notation/integration package."""
import hashlib
import json
from pathlib import Path

STUDY = Path(__file__).resolve().parent
ORIGINAL = "53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456"
CHANGES = [
    ("### C.4.8. Sampling fluctuations of the trained prediction",
     "#### C.4.8. Sampling fluctuations of the trained prediction"),
    (r"\ler_{\rm loc}/2", r"\le r_{\rm loc}/2"),
    ("###### 3. Actual atom response, centering, and general directions",
     "###### Actual atom response, centering, and general directions"),
    ("###### 4. A usable characterization of the signed field",
     "###### A usable characterization of the signed field"),
    ("ball of Section 2. Finite-support Taylor's formula",
     "ball described at the start of C.4.8.2. Finite-support Taylor's formula"),
    ("###### 6. Actual finite gradient flow, including exceptional laws",
     "###### Actual finite gradient flow, including exceptional laws"),
]

FINITE_PARAGRAPH = r"""For every finite labeled law and every finite initialized array, the smooth
finite-dimensional physical GF exists through \(T\). The following bounds
also cover laws outside \(U_Y\). Write \(c_{n,0}\) for the actual initialized
readout and \(A_n=A_{n,0}+K_n\). Use ordinary Euclidean vector norms,
Frobenius matrix norms and spectral action norms throughout this finite
paragraph, with all normalization factors displayed. In particular
\(w_n\in\mathbb R^{n\times2}\) contains the full first rows. The exact
middle update and its rank identity give
\[
 \dot K_n=-\frac2n\int r\Delta h^T\,d\mu_m,\qquad
 \left\|\frac{\Delta h^T}{n}\right\|_F
       =\frac{\|\Delta\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n},
\]
and consequently
\[
 \|\dot K_n\|_F\le2\int |r|
       \frac{\|\Delta\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}\,d\mu_m.
\]
The bounded gates imply \(\|h\|_2/\sqrt n\le1\),
\(\|\Delta\|_2/\sqrt n\le\|c_n\|_2/\sqrt n\), and
\(|r|\le\|c_n\|_2/\sqrt n+Y\). Applying the same bounds to the two
end-block equations yields
\[
 \frac{\|\dot c_n\|_2}{\sqrt n}
     \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right),\qquad
 \|\dot K_n\|_F
     \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
                \frac{\|c_n\|_2}{\sqrt n},
\]
\[
 \frac{\|\dot w_n\|_F}{\sqrt n}
 \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
       (\|A_{n,0}\|_{\rm op}+\|K_n\|_F)
                      \frac{\|c_n\|_2}{\sqrt n}.             \tag{C.4.8.P18}
\]
The first inequality gives
\[
 \frac{\|c_n(t)\|_2}{\sqrt n}
 \le\left(\frac{\|c_{n,0}\|_2}{\sqrt n}+Y\right)e^{2t}-Y.
\]
Integration then bounds \(K_n\) and \(w_n\) on each finite time interval.
These constants may depend on the initialized array and \(n\); no uniform
bound is needed here. A solution of a locally Lipschitz finite-dimensional
equation that remains bounded on each such interval extends through its
endpoint: on a containing compact ball the vector field is bounded and locally
Lipschitz, giving a Cauchy endpoint and a local continuation. This proves global
finite-time existence. Smooth dependence on the finite data and initialization
gives measurability of the \(H\)-valued prediction statistic; the bounds ensure
the local dependence can be continued through \(T\).

"""


def run():
    original = (STUDY / "proposal_C4_8.md").read_bytes()
    assert hashlib.sha256(original).hexdigest() == ORIGINAL
    text = original.decode()
    first = text.index("For every finite labeled law and every finite initialized array,")
    last = text.index("Fix \\(m\\), and condition", first)
    changes = CHANGES + [(text[first:last], FINITE_PARAGRAPH)]
    for old, new in changes:
        assert text.count(old) == 1, old
        text = text.replace(old, new, 1)
    restored = text
    for old, new in reversed(changes):
        assert restored.count(new) == 1, new
        restored = restored.replace(new, old, 1)
    assert restored.encode() == original
    destination = STUDY / "proposal_C4_8_v2.md"
    destination.write_text(text)
    edits = json.loads((STUDY / "promotion_edits.json").read_text())
    edits["append"]["source"] = destination.name
    edits_path = STUDY / "promotion_edits_v2.json"
    edits_path.write_text(json.dumps(edits, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "candidate_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "edits_sha256": hashlib.sha256(edits_path.read_bytes()).hexdigest(),
        "lines": len(text.splitlines()), "changes": CHANGES,
        "finite_paragraph_replaced_with_explicit_factors": True,
        "inverse_preservation": True,
    }, indent=2))


if __name__ == "__main__":
    run()
