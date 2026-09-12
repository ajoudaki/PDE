"""Assemble the authorized C.5 promotion from retained source and current guides.

Writes only a fresh study-owned review edition. This is not an integration tool.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
TITLE = "### C.5. Early test-risk advantage over frozen features at matched training loss"
OLD_TITLE = "### C.4. Early test-risk improvement at equal training loss for a fixed tanh model"
LINK = "global_nonlinear.md#c5-early-test-risk-advantage-over-frozen-features-at-matched-training-loss"
SUMMARY = ("[Section C.5](" + LINK + ") separately proves a small early-time test-risk advantage "
           "over frozen initial hidden features at matched training loss for one prescribed "
           "three-point tanh design and the uniform-circle target `cos(3 alpha)`. Its "
           "computer-assisted positive cubic coefficient has a controlled actual-flow "
           "remainder; neither the time interval nor the remainder constant is numerically "
           "evaluated. The frozen population kernel equals the full initial tangent kernel "
           "under this initialization; the finite comparator freezes hidden layers and "
           "trains only the readout. This is no class-level or later-time superiority theorem.")


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f"Expected one occurrence: {old[:100]!r}")
    return text.replace(old, new, 1)


def relabel(text):
    return re.sub(r"\bC4\b", "C5", re.sub(r"\bC\.4\b", "C.5", text))


def scientific_ast(text):
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if (node.body and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)):
                node.body.pop(0)
    return ast.dump(tree)


def guide_after(text):
    text = replace_once(text,
        "for studying the internal dynamics rather than only the training loss.",
        "for studying the internal dynamics rather than only the training loss. "
        "The scoped generalization and comparison results below address parts of "
        "that second question; broader task-class and architectural conclusions remain open.")
    lines = text.splitlines(keepends=True)
    index = next(i for i, line in enumerate(lines)
                 if line.startswith("| [Global nonlinear learning]"))
    lines[index] = lines[index].rstrip().removesuffix(" |") + " " + SUMMARY + " |\n"
    text = "".join(lines)
    text = replace_once(text,
        "arithmetic. Code execution is not needed\nto check the proofs; the displayed certificate has a complete reproduction\ncommand and independent checking routes.",
        "arithmetic. Section C.5 additionally includes a computer-assisted sign proof: "
        "its analytic error bounds and executed finite arithmetic jointly establish "
        "the coefficient enclosure. The optional certificate tool regenerates its "
        "inputs and exact intervals from source, with independent checking routes "
        "and no archived-array dependency.")
    text = replace_once(text,
        "A global input-population theorem and a dense Gaussian joint depth/width/time\n",
        SUMMARY + "\nA global input-population theorem and a dense Gaussian joint depth/width/time\n")
    return replace_once(text,
        "No currently included theorem relies on a numerical figure or a\ngenerated coefficient table.",
        "No theorem relies on an empirical figure or an unreproducible coefficient "
        "table. C.5 explicitly includes its computer-assisted certificate, complete "
        "analytic error bounds, and maintained reproduction source.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    if not out.is_relative_to(ROOT / "data/generated/two_layer_test_risk"):
        raise ValueError("Output must use the study generated namespace")
    old = STUDY / "PROMOTION_SIGN_C4_V2.md"
    if digest(old) != "dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc":
        raise ValueError("Changed original candidate")
    original = old.read_text()
    candidate = replace_once(relabel(original), relabel(OLD_TITLE), TITLE)
    inverse = replace_once(candidate, TITLE, relabel(OLD_TITLE))
    inverse = re.sub(r"\bC5\b", "C4", re.sub(r"\bC\.5\b", "C.4", inverse))
    assert inverse == original
    baseline = (ROOT / "docs/global_nonlinear.md").read_text()
    if re.search(r"^### C\.5\.", baseline, re.M):
        raise ValueError("C.5 is already occupied")
    destinations = {
        "docs/global_nonlinear.md": baseline + "\n" + candidate.rstrip() + "\n",
        "docs/README.md": guide_after((ROOT / "docs/README.md").read_text()),
        "code/README.md": (ROOT / "code/README.md").read_text() + "\n"
            + relabel((STUDY / "PROMOTION_CODE_README_APPENDIX.md").read_text()),
    }
    mapping = {
        "PROMOTION_certificate.py": "certificate.py",
        "certificate_kernel.cpp": "certificate_kernel.cpp",
        "angle_error_bound.py": "angle_error_bound.py",
        "PROMOTION_check_driver.py": "check_driver.py",
        "PROMOTION_check_kernel.py": "check_kernel.py",
        "PROMOTION_TOOL_GUIDE.md": "README.md",
    }
    for source, name in mapping.items():
        before = (STUDY / source).read_text()
        after = relabel(before)
        # Retain executable code exactly; repair two obsolete explanatory names.
        if name == "certificate_kernel.cpp":
            after = after.replace("See CERTIFICATION_ENGINE.md", "See the arithmetic proof in global_nonlinear.md, C.5")
        if name == "check_driver.py":
            after = after.replace("for certificate_driver.", "for certificate.")
        if name.endswith(".py"):
            assert scientific_ast(before) == scientific_ast(after)
        destinations["code/tools/two_layer_risk/" + name] = after
    out.mkdir(parents=True, exist_ok=False)
    edition, packet = out / "edition", out / "packet"
    edition.mkdir()
    packet.mkdir()
    # A selected documentation/source review edition, never a checkout or Git copy.
    copied = list((ROOT / "docs").glob("*.md")) + [ROOT / "code/README.md", ROOT / "code/tools/check_library.py"]
    for source in copied:
        target = edition / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    for path, text in destinations.items():
        target = edition / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
    (STUDY / "C5_SECTION.md").write_text(candidate)
    (packet / "candidate.md").write_text(candidate)
    for name in ("docs/README.md", "code/README.md", "docs/global_nonlinear.md"):
        target = packet / (name.replace("/", "_") + ".before")
        shutil.copyfile(ROOT / name, target)
    frozen = ROOT / "data/generated/two_layer_test_risk/signed_promotion_v1/packet"
    shutil.copyfile(frozen / "dependencies.md", packet / "dependencies.md")
    shutil.copyfile(frozen / "original_numerical_source.py", packet / "original_numerical_source.py")
    shutil.copyfile(ROOT / "docs/NOTATION.md", packet / "NOTATION.md")
    (packet / "original_candidate.md").write_text(original)
    evidence = out / "evidence"
    shutil.copytree(frozen.parent / "evidence", evidence)
    manifest = {
        "authors_assemblers": ["root", "cubic_derivation", "matching_remainder", "quadrature_check",
            "sign_structure", "certified_error", "certification_engine", "sign_code_assembly", "signed_notation_assembly"],
        "selector": "risk_promotion_placement",
        "scope": "Exact original signed theorem, C.5 relabeling and current guide integration; no scientific expansion",
        "original_candidate_sha256": digest(old),
        "candidate_inverse_relabel_matches_original": inverse == original,
        "source_sha256": {source: digest(STUDY / source) for source in mapping},
        "baseline_sha256": {str(p.relative_to(ROOT)): digest(p) for p in copied},
        "destinations": {p: digest(edition / p) for p in destinations},
        "packet_sha256": {str(p.relative_to(packet)): digest(p) for p in packet.iterdir()},
        "edition_sha256": {str(p.relative_to(edition)): digest(p) for p in edition.rglob("*") if p.is_file()},
        "evidence_sha256": {str(p.relative_to(evidence)): digest(p) for p in evidence.rglob("*") if p.is_file()},
        "assembler_sha256": digest(Path(__file__)),
        "approval": "User: 'ok, can you promote it yourself to C.5, using the promotion gates?' (2026-09-12)",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"output": str(out), "destinations": len(destinations),
                      "manifest_sha256": digest(out / "manifest.json")}, indent=2))


if __name__ == "__main__":
    main()
