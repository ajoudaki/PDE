"""Assemble a reviewable standalone edition without editing established paths."""
import argparse
import hashlib
import json
from pathlib import Path
import re

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]


def read(name):
    return (STUDY/name).read_text()


def local_labels(text, prefix):
    text = re.sub(r"\\tag\{(\d+)\}", lambda m: "\\tag{"+prefix+m[1]+"}", text)
    # A bare equation reference has no identifier or TeX brace immediately
    # before it. In particular, preserve W^{(3)} and o_{P}(1).
    text = re.sub(r"(?<![A-Za-z0-9_{}])\((\d{1,2})\)", lambda m: "("+prefix+m[1]+")", text)
    return text


def proposed_section():
    scope = read("H3_v2_scope_proof.md")
    scope = scope[scope.index("## 1. Statement"):scope.index("## 5. Why")]
    start = scope.index("The fixed C-H2 construction")
    stop = scope.index("Here is a fixed finite-input subfamily", start)
    scope = scope[:start]+scope[stop:]
    # The finite law interface is supplied by the maintained library; keep
    # the family definition and its integration proof, without duplicate code.
    start = scope.index("The following exact rational interface")
    stop = scope.index("\n```", scope.index("```python", start)+10)+4
    scope = scope[:start]+scope[stop:]
    scope = local_labels(scope, "H3.S")
    scope = re.sub(r"^## (\d+)\. (.*)$", r"###### A.\1. \2", scope, flags=re.M)
    scope = re.sub(r"[Ss]ections? (\d)", lambda m: "part A."+m[1], scope)

    hierarchy = read("H3_v2_hierarchy_proof.md").split("\n", 2)[2]
    hierarchy = hierarchy.replace("This is a proof candidate for the exact bias-free tanh model of C.4.7.8.\nIts finite numerical realization is treated separately.",
                                  "Use the exact bias-free tanh model of C.4.7.8. Part C proves its finite numerical realization.")
    old = """The initialized observable spaces contain the exact trajectory:
C.4.7.9 proves invariance by finite Euler word approximation followed by its
strong completion. The short-time proposition supplies exactly that strong
completion and tails for the present fixed family, so the same argument
applies on [0,T]. No assumption that the finite Gaussian core alone generates
the full spaces is made."""
    new = """The initialized observable spaces contain the exact trajectory.
The sine/cosine cylinder argument of C.4.7.8 makes the bounded initialized
words dense in their generated L2 spaces. Both A0 and its adjoint take these
spaces into each other; adjointness makes the pair reducing. The initial
Gaussian coordinates belong to them by bounded truncation. Every finite-law
Euler step in part A preserves the generated sigma fields, and its learned
increment is a finite sum of ranks between the two spaces. Closedness in L2
and in the corresponding HS operator block passes this property to the strong
completion in part A. No assumption that the finite Gaussian core alone
generates these full spaces is made."""
    if old not in hierarchy:
        raise ValueError("hierarchy invariance source changed")
    hierarchy = hierarchy.replace(old, new)

    numerical = read("H3_v2_numerical_proof.md")
    numerical = numerical[numerical.index("Fix "):numerical.index("\n---\n\n## Author provenance")]
    numerical = local_labels(numerical, "H3.N")
    numerical = re.sub(r"^## (\d+)\. (.*)$", r"###### C.\1. \2", numerical, flags=re.M)
    numerical = re.sub(r"[Ss]ections? (\d)", lambda m: "part C."+m[1], numerical)
    numerical = numerical.replace("part C.2–4 remove", "Parts C.2–C.4 remove")
    numerical = numerical.replace("The dense-closure\nproposition", "Part B")
    numerical = numerical.replace("the dense-closure proposition", "part B")
    numerical = numerical.replace("the short-time proposition", "part A")
    numerical = numerical.replace("The short-time existence proposition", "Part A")
    numerical = numerical.replace("the short-time existence proposition", "part A")
    numerical = numerical.replace("The short-time proposition", "Part A")
    return """##### C.4.7.10. Finite numerical autonomous observable closure

This section gives a finite numerical implementation of the same nonlinear
population physical gradient flow. Its exact model is C.4.7.8: no biases,
two tanh hidden layers, stored Gaussian variances (1,1/n,1/n²), mobilities
(n,1,n), unhalved squared loss, and both orientations of one reused initialized
Gaussian action. The finite-network interpretation retains its actual random
initial readout.

Fix T=1/200 and one rational two-arc law defined in part A. Part B specifies
a compatible dense closure, with exact prediction f_N at order N. Write
\\(\\mathfrak j=(\\varepsilon,Q,P,m,J,p)\\) for the numerical resolution
of part C: source regularization, initializer and population cubature, input
quadrature, number of time steps and arithmetic precision. Its finite
prediction is \\(\\widehat f_{N,\\mathfrak j}\\). Then

\\[
 \\widehat f_{N,\\mathfrak j}\\longrightarrow f_N,
 \\qquad f_N\\longrightarrow f_\\mu
 \\quad\\hbox{in }C([0,T]\\times S^1),
\\]

with the iterated numerical order in part C.1. The same limits preserve
training-averaged initial/current activation pair laws in W2 and their RMS
displacements in both layers. Neither horizon nor law family shrinks. The
numerical state restarts from its own complete finite marks and coefficients;
at fixed resolution its working storage is independent of elapsed step count.

Part A proves the required explicit short-time population domain; it is not
an assertion that the represented laws belong to the older time-40 neighborhood.
Part B verifies density, both action directions and nonredundant odd-degree
enrichment. Part C proves every numerical limit and accounts for initialization,
evolution, precision and workspace. No rate, per-run error certificate, arbitrary
diagonal refinement or tolerance-to-resolution rule is asserted. Feasible
declared computations are a separate reproducible library validation.

Unqualified equation references within parts A and C carry their displayed
H3.S and H3.N prefixes. Part B uses H3.1–H3.3.

"""+scope+"\n###### B. Dense compatible hierarchy and relevant enrichments\n\n"+hierarchy+"\n"+numerical+"\n"


def canonical_tests(kind):
    text = read("H3_v2_"+kind+"_tests.py")
    if kind == "initialization":
        start = text.index("HERE = Path(")
        stop = text.index("class ExactWordChecks", start)
        text = text[:start]+"from pde import observable_words as words\nfrom pde import observable_arithmetic as arithmetic\nfrom pde import observable_compiler as compiler\nfrom pde import observable_initialization as initialization\n\n\n"+text[stop:]
    if kind == "solver":
        block = "if __name__ == \"__main__\":\n    from H3_v2_candidate_loader import load_candidate\n    load_candidate()\n\n"
        if block not in text:
            raise ValueError("solver test bootstrap source changed")
        text = text.replace(block, "", 1)
    return text


def main(version, output):
    if not re.fullmatch(r"v[0-9]+", version):
        raise ValueError("version must be v followed by digits")
    output.mkdir(parents=True, exist_ok=False)
    section_path = STUDY/("H3_v2_edition_"+version+"_section.md")
    if section_path.exists():
        raise ValueError("preserve earlier editions")
    section = proposed_section()
    section_path.write_text(section)
    mapping, sources = {}, {}
    def add(relative, contents, source=None):
        path = output/relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contents)
        mapping[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        if source is not None:
            sources[str(source.relative_to(ROOT))] = hashlib.sha256(source.read_bytes()).hexdigest()
    for module in ("fixed", "arithmetic", "words", "compiler", "initialization", "solver"):
        source = STUDY/("H3_v2_"+module+".py")
        add("code/pde/observable_"+module+".py", source.read_text(), source)
    for relative in ("code/pde/__init__.py", "code/pde/finite_network.py", "code/pde/gaussian_moments.py", "code/pde/observable_closure.py", "code/tests/test_observable_closure.py"):
        add(relative, (ROOT/relative).read_text(), ROOT/relative)
    for kind in ("compiler", "initialization", "solver"):
        add("code/tests/test_observable_"+kind+".py", canonical_tests(kind), STUDY/("H3_v2_"+kind+"_tests.py"))
    add("code/tests/test_observable_validation.py", read("H3_v2_supervise_tests.py"), STUDY/"H3_v2_supervise_tests.py")
    for kind in ("validate", "analyze"):
        add("code/scripts/"+kind+"_observable_solver.py", read("H3_v2_"+kind+".py"), STUDY/("H3_v2_"+kind+".py"))
    add("code/scripts/run_observable_validation.py", read("H3_v2_supervise.py"), STUDY/"H3_v2_supervise.py")
    plan = json.loads(read("H3_v2_run_plan.json"))
    plan["version"] = "2026-09-13-independent-odd-orders-"+version
    plan["status"] = "predeclared independent reproduction of the corrected canonical candidate"
    plan["purpose"] += " Operational odd degrees 1,3,5 add initialized action information; original author records remain separate."
    for config in plan["configurations"]:
        if config["id"].startswith("tiny"):
            continue
        old = config["order"]
        config["order"] = {1: 1, 2: 3, 3: 5}[old]
        config["id"] = config["id"].replace("_n"+str(old), "_n"+str(config["order"]))
    plan["budget"]["total_cpu_seconds"] = 3600
    add("code/validation/observable_solver_plan.json", json.dumps(plan, indent=2)+"\n")
    flat_plan = STUDY/("H3_v2_reproduction_plan_"+version+".json")
    flat_plan.write_text(json.dumps(plan, indent=2)+"\n")
    book = (ROOT/"docs/global_nonlinear.md").read_text()
    anchor = "#### C.4.8. Sampling fluctuations of the trained prediction"
    if book.count(anchor) != 1:
        raise ValueError("book insertion point changed")
    add("docs/global_nonlinear.md", book.replace(anchor, section+"\n"+anchor), ROOT/"docs/global_nonlinear.md")
    add("docs/special_data_limits.md", (ROOT/"docs/special_data_limits.md").read_text(), ROOT/"docs/special_data_limits.md")
    add("docs/NOTATION.md", (ROOT/"docs/NOTATION.md").read_text(), ROOT/"docs/NOTATION.md")
    guide = (ROOT/"code/README.md").read_text()+"\n\n"+re.sub(r"^(#+) ", r"#\1 ", read("H3_v2_guide.md"), flags=re.M)
    add("code/README.md", guide, ROOT/"code/README.md")
    roadmap = (ROOT/"docs/README.md").read_text()
    marker = "**C-H3: efficient computation with qualitative population convergence.**"
    paragraph = """**C-H3 established scope.** [C.4.7.10](global_nonlinear.md#c4710-finite-numerical-autonomous-observable-closure)
supplies the finite autonomous numerical closure on `[0,1/200]` for a fixed
rational two-arc family, including nonorthogonal atomic and nonatomic laws.
It proves iterated numerical and closure-order convergence to the same
nonlinear GF, whole-circle prediction, paired hidden observations and own-state
restart. The reusable solver has bounded workspace and separate declared
resolution checks; it supplies no true-error certificate or tolerance selector.

"""
    roadmap = roadmap.replace(marker, paragraph+marker, 1)
    roadmap = roadmap.replace("C-H3 and C-H4 remain research\ntargets until fulfilled; changing their scope asserts no new theorem.",
                              "C-H3 has the stated short-time scope; C-H4 remains a research target.\nChanging a roadmap's scope alone asserts no new theorem.")
    roadmap = roadmap.replace("on its stated small nonlinear interval; efficient numerical consistency and\nlater continuation remain C-H3 and C-H4.",
                              "on its stated small nonlinear interval. C-H3 supplies numerical consistency\nand bounded declared computations through time 1/200; time-40 continuation\nand practical operation remain C-H4.")
    roadmap = roadmap.replace("Beyond the C.4.7.9\nclosure, no alternative closure or success of the later numerical-computation\nmilestones is asserted here.",
                              "The compatible C.4.7.10 implementation has the explicit short-time scope\nabove; no time-40 numerical result is asserted here.")
    add("docs/README.md", roadmap, ROOT/"docs/README.md")
    add("review/dependencies.md", read("H3_v2_dependencies.md"), STUDY/"H3_v2_dependencies.md")
    add("review/proposed_section.md", section, section_path)
    add("review/library_guide.md", read("H3_v2_guide.md"), STUDY/"H3_v2_guide.md")
    for name in ("H3_v2_scope_proof.md", "H3_v2_hierarchy_proof.md", "H3_v2_numerical_proof.md", "H3_v2_run_plan.json"):
        sources[str((STUDY/name).relative_to(ROOT))] = hashlib.sha256((STUDY/name).read_bytes()).hexdigest()
    manifest = dict(version=version, output=str(output), author_and_assembler_identities=["/root", "/root/h3v2_route_basis", "/root/h3v2_route_gaussian", "/root/h3v2_scope", "/root/h3v2_scope/arithmetic_audit"],
                    selector="/root/h3v2_relevance", source_hashes=sources, edition_hashes=mapping,
                    assembler_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    role="frozen proposed edition; established workspace files unchanged; review and approval pending")
    (output/"review/manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    (STUDY/("H3_v2_edition_"+version+"_manifest.json")).write_text(json.dumps(manifest, indent=2)+"\n")
    print(json.dumps(dict(output=str(output), files=len(mapping), section_lines=len(section.splitlines())), indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    main(args.version, args.output.resolve())
