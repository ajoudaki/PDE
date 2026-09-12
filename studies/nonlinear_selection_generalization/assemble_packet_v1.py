"""Freeze the proposed theory addition and exact established dependencies.

No established file is written. Existing outputs are never overwritten.
The assembled edition is a selected-file proof workspace, not a checkout copy.
"""
from hashlib import sha256
import json
from pathlib import Path

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]


def digest(data):
    return sha256(data).hexdigest()


def write_new(name, data):
    if isinstance(data, str):
        data = data.encode()
    with (STUDY / name).open("xb") as stream:
        stream.write(data)
    return {"sha256": digest(data), "bytes": len(data),
            "lines": len(data.splitlines())}


def main():
    manifest = {"kind": "frozen complete scientific packet v1",
                "authors_assemblers": ["/root", "/root/population_route",
                    "/root/continuation_route", "/root/alternative_route"],
                "selector_excluded_from_reviews": "/root/relevance_selector",
                "files": {}, "source_slices": {}}
    units = ["canonical_model_v1.md", "canonical_continuation_v1.md",
             "canonical_separation_v1.md", "canonical_learning_v1.md"]
    texts = []
    for unit in units:
        data = (STUDY / unit).read_bytes()
        manifest.setdefault("assembly_unit_hashes", {})[unit] = digest(data)
        texts.append(data.decode().rstrip())
    addition = "\n\n".join(texts) + "\n"
    manifest["files"]["candidate_addition_v1.md"] = write_new(
        "candidate_addition_v1.md", addition)

    slices = {
        "docs/global_nonlinear.md": [
            (1840, 1898, "A.1-A.4, complete"),
            (1903, 2274, "B.1 complete GF construction; GD bridge excluded"),
            (3982, 4207, "C.4.1 complete full-row transport"),
            (5475, 5782, "C.4.5.1 sections 1-3, complete reference endpoint"),
            (5999, 6595, "C.4.5.1 section 5 and complete C.4.5.2"),
            (7652, 8258, "C.4.6.3 sections 1-6, complete source/moment proofs"),
            (12994, 15322, "C.4.9 complete theorem and all proof units")],
        "docs/special_data_limits.md": [
            (3785, 4326, "III.F.1-III.F.11, complete Gaussian/strong calculus")]
    }
    for source, ranges in slices.items():
        data = (ROOT / source).read_bytes()
        lines = data.decode().splitlines(keepends=True)
        name = "frozen_" + Path(source).stem + "_v1.md"
        chunks = [f"# Frozen established dependencies from {source}\n\n"
                  f"Source SHA-256: `{digest(data)}`.\n"
                  "Only the exact complete sections listed below are included.\n"]
        for first, last, scope in ranges:
            chunks.append(f"\n<!-- SOURCE {source}:{first}-{last}; {scope} -->\n\n")
            chunks.append("".join(lines[first-1:last]))
        manifest["files"][name] = write_new(name, "".join(chunks))
        manifest["source_slices"][name] = {
            "source": source, "full_source_sha256": digest(data),
            "ranges": ranges}

    guides = {"AGENTS.md": "frozen_AGENTS_v1.md",
              "RESEARCH_WORKFLOW.md": "frozen_WORKFLOW_v1.md",
              "docs/NOTATION.md": "frozen_NOTATION_v1.md",
              "docs/README.md": "frozen_docs_README_v1.md"}
    for source, name in guides.items():
        manifest["files"][name] = write_new(name, (ROOT / source).read_bytes())

    old = (ROOT / "docs/README.md").read_text()
    summary = ("[Section C.4.10](global_nonlinear.md#c410-generalization-during-a-finite-added-data-episode) "
        "gives finite-episode generalization for an independently specified odd Fourier "
        "regression family with full-circle input densities and bounded centered noise. "
        "It combines finite-mode nonlinear approximation, separate input/noise sampling "
        "bounds and a class-determined positive stop, with robust unseen-risk improvement, "
        "paired circle-plus-anchor second-hidden motion, and ordered width/contamination/sample "
        "limits for actual GF; conditioning constants remain unevaluated.")
    marker = ("It does not assert a final changed-law endpoint or an out-of-sample risk guarantee.")
    assert old.count(marker) == 2
    new = old.replace(marker, marker + " " + summary)
    roadmap_marker = ("superiority theorem.\n\n### C. Independent computation")
    assert new.count(roadmap_marker) == 1
    new = new.replace(roadmap_marker,
        "superiority theorem.\n\n"
        "Section C.4.10 supplies B at a finite-episode scope for a declared full-circle "
        "regression family. Its approximation floor and unevaluated conditioning constants "
        "leave arbitrary-accuracy learning and practical computation as further questions.\n\n"
        "### C. Independent computation")
    manifest["files"]["candidate_docs_README_v1.md"] = write_new(
        "candidate_docs_README_v1.md", new)
    for name in [Path(__file__).name, "validate_edition_v1.py", "scientific_assignment_v1.md"]:
        data = (STUDY / name).read_bytes()
        manifest["files"][name] = {"sha256": digest(data), "bytes": len(data),
                                   "lines": len(data.splitlines())}
    write_new("scientific_manifest_v1.json", json.dumps(manifest, indent=2)+"\n")
    print(json.dumps({"candidate_sha256": digest(addition.encode()),
                      "files": len(manifest["files"]),
                      "lines": sum(x["lines"] for x in manifest["files"].values())}))


if __name__ == "__main__":
    main()
