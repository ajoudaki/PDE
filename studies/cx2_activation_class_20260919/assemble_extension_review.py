"""Freeze this study's extension and complete explicit review dependencies.

No other study or Git history is an input. Generated packets are immutable:
use a new round name after any correction. No tests or training run here.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[2]
STUDY = Path("studies/cx2_activation_class_20260919")
GENERATED = Path("data/generated/cx2_activation_class_20260919")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("round")
    args = parser.parse_args()
    if not args.round.replace("_", "").isalnum():
        raise ValueError("round name must use letters, digits and underscores")
    target = ROOT / GENERATED / (args.round + "_inputs")
    if target.exists():
        raise ValueError("refusing to overwrite a frozen packet")
    sources = {}

    def add(path):
        path = Path(path)
        data = (ROOT / path).read_bytes()
        sources[str(path)] = (data, dict(source=str(path), source_sha256=digest(data)))

    for name in ("REVISED_RESULT.md", "ONSET_EXTENSION.md", "BOUNDED_EXTENSION.md",
                 "COMMUTATOR_RESPONSE.md", "REFERENCE_PROOF.md", "CLOSURE_PROOF.md",
                 "SOURCE_PROOF.md",
                 "PARTIAL_RESULT.md", "NUMERICAL_EXTENSION.md",
                 "NUMERICAL_VALIDATION_PLAN.md", "activation_closure.py",
                 "test_activation_closure.py"):
        add(STUDY / name)
    add("docs/NOTATION.md")

    def excerpt(path, first, stop, name):
        raw = (ROOT / path).read_bytes()
        text = raw.decode()
        left = text.index(first)
        right = text.index(stop, left + len(first))
        data = text[left:right].encode()
        sources["dependencies/" + name] = (data, dict(
            source=path, source_sha256=digest(raw), start_heading=first,
            stop_before_heading=stop, first_line=text[:left].count("\n")+1,
            last_line=text[:right].count("\n")))

    book = "docs/global_nonlinear.md"
    excerpt(book, "## A. Contained probability", "### C.4. Training-law",
            "activation_foundation.md")
    excerpt(book, "#### C.4.1. Full-row", "#### C.4.5. Robust",
            "law_construction.md")
    excerpt(book, "##### C.4.7.2. Raw bounds", "##### C.4.7.6. Nonlinear variation",
            "source_and_completion.md")
    excerpt(book, "###### A.1. Statement and the executable family",
            "###### B. Dense compatible hierarchy", "onset_law_proof.md")
    excerpt(book, "###### C.1. Finite equations and assertion",
            "###### D.1. Computation through physical time 40", "numerical_proof.md")
    excerpt(book, "###### D.1. Computation through physical time 40",
            "###### D.4. Finite numerical limits", "supported_law_proof.md")
    excerpt("docs/special_data_limits.md",
            "### III.F. Fixed finite Gaussian programs",
            "### III.S. Direct controlled source", "gaussian_foundation.md")
    # Follow the complete repository Python import closure, including eager
    # package imports and imports located inside functions.
    pending = [STUDY / "activation_closure.py", STUDY / "test_activation_closure.py",
               Path("code/pde/__init__.py")]
    visited = set()
    while pending:
        path = pending.pop()
        if path in visited:
            continue
        visited.add(path)
        add(path)
        tree = ast.parse((ROOT / path).read_text(), filename=str(path))
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [item.name for item in node.names]
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if node.level and str(path).startswith("code/pde/"):
                    module = "pde." + module
                names = [module]
                if module in ("pde", "pde."):
                    names += ["pde." + item.name for item in node.names]
            for name in names:
                if name == "activation_closure":
                    pending.append(STUDY / "activation_closure.py")
                elif name == "pde":
                    pending.append(Path("code/pde/__init__.py"))
                elif name.startswith("pde."):
                    candidate = Path("code") / (name.replace(".", "/") + ".py")
                    if (ROOT / candidate).is_file():
                        pending.append(candidate)

    for _, origin in sources.values():
        assert digest((ROOT / origin["source"]).read_bytes()) == origin["source_sha256"], \
            "source changed during assembly"
    target.mkdir(parents=True)
    files = []
    for path, (data, origin) in sorted(sources.items()):
        output = target / path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
        files.append(dict(file=path, sha256=digest(data), lines=data.count(b"\n"), **origin))
    record = dict(created_utc=datetime.now(timezone.utc).isoformat(), round=args.round,
                  scope="Complete internal scientific and implementation review; no promotion",
                  files=files, repository_python_import_closure=sorted(map(str, visited)))
    manifest = json.dumps(record, indent=2) + "\n"
    (target / "INPUTS.json").write_text(manifest)
    (ROOT / STUDY / (args.round.upper() + "_INPUTS.json")).write_text(manifest)
    print(json.dumps(dict(packet=str(target), files=len(files),
                          lines=sum(f["lines"] for f in files),
                          manifest_sha256=digest(manifest.encode())), indent=2))


if __name__ == "__main__":
    main()
