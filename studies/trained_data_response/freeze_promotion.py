"""Freeze a canonical promotion candidate with complete neutral review inputs."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main(round_name):
    assert round_name.isalnum() and round_name.startswith("P")
    section = (BASE / "CANONICAL_SECTION.md").read_bytes()
    assert section.endswith(b"\n") and not section.endswith(b"\n\n")
    spec = importlib.util.spec_from_file_location("promotion_builder", BASE / "prepare_promotion.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    originals = {p: (ROOT / p).read_bytes() for p in builder.EXPECTED}
    for p, data in originals.items():
        assert sha(data) == builder.EXPECTED[p], p
    guide = originals["docs/README.md"].decode()
    for edit in builder.EDITS:
        if edit["path"] == "docs/README.md":
            assert guide.count(edit["old"]) == 1
            guide = guide.replace(edit["old"], edit["new"])
    ancillary = "# Complete proposed ancillary changes\n\n"
    ancillary += "## Complete revised docs/README.md\n\n" + guide
    ancillary += "\n## Exact docs/global_nonlinear.md C.4 navigation replacement\n\n"
    edit = builder.EDITS[0]
    ancillary += "Before:\n\n" + edit["old"] + "\n\nAfter:\n\n" + edit["new"] + "\n"
    # Integration readers receive the complete old C.4 unit in combination
    # with the common dependencies. No historical verdict is included.
    oldlines = originals["docs/global_nonlinear.md"].splitlines(keepends=True)
    complement = "# Older integration comparison scope\n\n"
    spans = [(3836, 3971), (4297, 5464), (6586, 6892)]
    for start, end in spans:
        complement += f"\n<!-- docs/global_nonlinear.md:{start}-{end} -->\n\n"
        complement += b"".join(oldlines[start - 1:end]).decode()
    assignment = f"""# Neutral complete canonical scientific review

Assess the exact mathematical validity of the proposed C.4.6 addition and
its guide/navigation statements. You are a fresh isolated scientific reviewer,
distinct from every author/assembler and the selector. Do not infer a preferred
verdict from the existence of this packet.

Your complete allowed inputs in this folder are `{round_name}_MANIFEST.json`,
`{round_name}_SECTION.md`, `{round_name}_ANCILLARY.md`,
`{round_name}_DEPENDENCIES.md`, `{round_name}_CHECK_IDENTITIES.py`,
`{round_name}_REFERENCE_CERTIFICATE.py`, and this assignment, plus the required
skills below. The manifest's other build/integration entries are provenance;
you need not open them for this scientific assignment. Do not read live
author drafts, study README, prior rounds, author history, reports, or other
project files. The report and scratch paths are assigned in the launch prompt.

Read every scientific line, every dependency proof, both complete guides and
both check programs. Repair truncated reads. Verify input hashes before and
after review. Missing required mathematical input is a gap; do not supply a
specialized theorem from memory. Read the complete required skills
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, including applicable
research-contract and adversarial-audit references.

Reconstruct the model/metric, finite right differentiation, cavity conditioning,
Gaussian query process, weighted finite uniform integrability, canonical limit
passage, strongly continuous operator equation, singular endpoint compatibility,
integrable coefficient perturbation, actual finite-tangent identification,
fixed-program versus mesh-removal limit order, and whole-circle observation
argument. Check constants, conditioning dependence, nonatomic laws, both matrix
orientations and actual finite readout. A formal derivative or population
source formula alone is insufficient. Do not claim a nonlinear population
law-to-flow map, finite-contamination remainder, uniform-time width theorem,
law-uniform failure probability, endpoint continuity, risk benefit, or GD
derivative unless the supplied proof actually establishes it.

Run `{round_name}_CHECK_IDENTITIES.py --output <fresh scratch>/identities` and
the complete `{round_name}_REFERENCE_CERTIFICATE.py`, retaining commands and
outputs. Add meaningful independent algebra and boundary checks. No training
experiment or parameter sweep is allowed. Numerical checks supplement proofs.

Persist a full report: distinct process/reviewer identity and isolation;
complete input hashes and line coverage; repaired truncations; actual attacks,
commands and outcomes; component verdicts; precise surviving gaps and required
corrections; optional suggestions separately; and overall ACCEPT or CORRECTION
REQUIRED for the exact proposed scope. Do not abbreviate an unproved step as
routine. Do not edit inputs, use Git, delegate, or contact another task.
"""
    integration = f"""# Neutral independent integration review

Review the proposed canonical addition, its complete dependency/interface
scope and its placement and preservation. This is a fresh integration review,
not authorship, a relevance decision, or a fresh proof audit of the whole book.
No prior scientific verdicts are supplied or may be read.

Read all of `{round_name}_SECTION.md`, `{round_name}_ANCILLARY.md`,
`{round_name}_DEPENDENCIES.md`, `{round_name}_INTEGRATION_BASE.md`,
`{round_name}_MANIFEST.json`, `{round_name}_BUILD.py`,
`{round_name}_VALIDATE.py`, `{round_name}_CHECK_IDENTITIES.py`,
`{round_name}_REFERENCE_CERTIFICATE.py`, and this assignment. The complete
reading guide and notation contract are in those inputs. Use the required
solve-math-rigorously and investigate-conjectures skills under
`/etc/codex/skills/`, with applicable research-contract/adversarial-audit refs.
Do not read study README, author/history files, prior packets, other reports
or verdicts. The frozen dependency packet and integration complement together
contain all old C.4, plus A.1–A.4/B.1 and the complete named external chapter
proof units. Record this older read scope and its unread complement precisely.

Verify every frozen hash. Read every new line and supplied dependency line;
repair truncations. Check notation/normalization, equation cross-references,
the compatibility of source/propagation/capture interfaces, theorem and guide
scope, placement, duplication, preservation of established statements, and
absence of any required study/history/oracle dependency. If you identify a
scientific defect, report it explicitly; do not silently repair the draft.

The build program may read the live base files only to verify their exact
declared hashes and assemble a generated standalone edition; it does not
modify them. Read those already supplied bodies from the frozen packet.
Run `{round_name}_BUILD.py --section <folder>/{round_name}_SECTION.md --output
<fresh scratch>/edition`, then `{round_name}_VALIDATE.py --edition <scratch>/edition
--output <fresh scratch>/validation`. These commands use no study history,
retained arrays or empirical campaign. Inspect their actual outputs. New local
checks are allowed in assigned scratch; no training, Git, input edits,
delegation or contact with another task.

Persist the full independent report with process identity/isolation, hashes,
complete coverage, exact commands/results, interface and preservation findings,
unread complement, required corrections separately from optional suggestions,
and overall ACCEPT or CORRECTION REQUIRED for this integration scope. The
report and exclusive scratch paths are assigned by the launch prompt.
"""
    outputs = {
        f"{round_name}_SECTION.md": section,
        f"{round_name}_ANCILLARY.md": ancillary.encode(),
        f"{round_name}_DEPENDENCIES.md": (BASE / "R1_DEPENDENCIES.md").read_bytes(),
        f"{round_name}_INTEGRATION_BASE.md": complement.encode(),
        f"{round_name}_CHECK_IDENTITIES.py": (BASE / "R1_CHECK_IDENTITIES.py").read_bytes(),
        f"{round_name}_REFERENCE_CERTIFICATE.py": (BASE / "R1_REFERENCE_CERTIFICATE.py").read_bytes(),
        f"{round_name}_BUILD.py": (BASE / "prepare_promotion.py").read_text().replace("R1_CHECK_IDENTITIES.py", f"{round_name}_CHECK_IDENTITIES.py").replace("R1_REFERENCE_CERTIFICATE.py", f"{round_name}_REFERENCE_CERTIFICATE.py").encode(),
        f"{round_name}_VALIDATE.py": (BASE / "validate_edition.py").read_bytes(),
        f"{round_name}_ASSIGNMENT.md": assignment.encode(),
        f"{round_name}_INTEGRATION_ASSIGNMENT.md": integration.encode(),
    }
    manifest = {
        "round": round_name,
        "authors": ["original-task /root (01a090b5-1a52-7072-a829-cd2aad518558)",
                    "/root/propagator", "/root/weighted_source", "/root/capture"],
        "assembler": "/root/capture; original-task /root (ancillary edits and tooling)",
        "selector_instance": "01a090c0-8a58-7da1-8075-8c0b0f23f959",
        "inputs": {p: {"sha256": sha(data), "lines": len(data.splitlines())}
                   for p, data in outputs.items()},
        "base_sha256": builder.EXPECTED,
        "ancillary_edits": builder.EDITS,
        "destinations": ["docs/global_nonlinear.md C.4.6 and C.4 navigation", "docs/README.md chapter row and scope paragraph"],
        "unchanged": "All existing mathematics and other code/book files",
        "required_approval": "Specific user approval before any established-file edit",
    }
    outputs[f"{round_name}_MANIFEST.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    assert all(not (BASE / p).exists() for p in outputs), "round already exists"
    for p, data in originals.items():
        assert (ROOT / p).read_bytes() == data, f"Concurrent source change: {p}"
    assert (BASE / "CANONICAL_SECTION.md").read_bytes() == section
    for p, data in outputs.items():
        (BASE / p).write_bytes(data)
    print(json.dumps({p: sha(data) for p, data in outputs.items()}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--round", required=True)
    main(parser.parse_args().round)
