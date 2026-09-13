"""Persist the complete selected established proof units for H4 review.

Only named book sources are read. All intervals refer to the exact frozen
source hashes checked here; a changed source requires a new selection/check.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/observable_hierarchy"
SOURCES = {
    "docs/global_nonlinear.md": "77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932",
}
UNITS = [
    ("docs/finite_dynamics.md", 1, 227, "Finite model, exact metric, energy and finite existence: sections1–4"),
    ("docs/special_data_limits.md", 3785, 4286, "III.F.1–10: complete finite Gaussian programs, common actions, strong scalar differentiation"),
    ("docs/global_nonlinear.md", 1840, 1898, "A.1–4: value/product extensions, initialized action norm and scalar chain rule"),
    ("docs/global_nonlinear.md", 1903, 2453, "B.1: complete two-hidden-layer transformed reference and actual finite-GF identification"),
    ("docs/global_nonlinear.md", 2924, 3440, "C.2: complete weighted named-source response proof"),
    ("docs/global_nonlinear.md", 3982, 4815, "C.4.1, C.4.2.1–6, C.4.3.1–3: full-row comparison, common carrier, completion and finite proxy"),
    ("docs/global_nonlinear.md", 5270, 6903, "C.4.5 including .1–3: complete substantial-learning statement, reference, tails, exact certificate and actual-GF comparison"),
    ("docs/global_nonlinear.md", 8989, 10554, "C.4.7.1–5: complete time40 strong construction, coefficient bootstrap, completion, finite-GF and observations"),
    ("docs/global_nonlinear.md", 11398, 13981, "C.4.7.7–10: binary learning passage, complete H1/H2/H3 foundations and numerical contract"),
]


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def main():
    output = STUDY / "H4_dependencies.md"
    manifest = STUDY / "H4_dependency_manifest.json"
    if output.exists() or manifest.exists():
        raise FileExistsError("frozen dependency source already exists")
    cache, rows = {}, []
    parts = ["# Complete frozen established proof inputs for H4\n\n"
             "These are exact complete selected source units, with their original local notation and scopes. "
             "They are dependencies, not newly proposed text. The manifest records every source hash and interval. "
             "The complete notation and required guides are supplied separately. No author history or prior verdict is an input.\n"]
    for name, first, last, scope in UNITS:
        if name not in cache:
            payload = (ROOT / name).read_bytes()
            if name in SOURCES and digest(payload) != SOURCES[name]:
                raise ValueError("changed scientific source: " + name)
            cache[name] = (payload, payload.decode().splitlines(keepends=True))
        payload, lines = cache[name]
        excerpt = "".join(lines[first-1:last])
        if not excerpt or last > len(lines):
            raise ValueError("invalid complete-unit interval")
        parts.append("\n\n<!-- BEGIN EXACT DEPENDENCY: " + scope + " -->\n\n" + excerpt +
                     "\n<!-- END EXACT DEPENDENCY -->\n")
        rows.append(dict(source=name, source_sha256=digest(payload), first_line=first, last_line=last,
                         scope=scope, excerpt_sha256=digest(excerpt.encode())))
    content = "".join(parts)
    output.write_text(content)
    guides = {name:digest((ROOT/name).read_bytes()) for name in ("docs/README.md", "docs/NOTATION.md", "code/README.md")}
    manifest.write_text(json.dumps(dict(format="H4-complete-proof-dependencies-v1", units=rows,
                                        output=output.name, sha256=digest(content.encode()), guides=guides), indent=2)+"\n")
    print(json.dumps(dict(units=len(rows), lines=len(content.splitlines()), bytes=len(content.encode()), sha256=digest(content.encode()))))


if __name__ == "__main__":
    main()
