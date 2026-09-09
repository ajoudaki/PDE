"""Build and verify the self-contained H=3,4 Route S report."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEPTH_ROOT = HERE.parent
REPORT = HERE / "H3_H4_ORDER5_SELF_CONTAINED.md"
MANIFEST = HERE / "H3_H4_REPORT_MANIFEST.json"
MANIFEST_SHA = HERE / "H3_H4_REPORT_MANIFEST_SHA256.txt"

EMBEDS = (
    ("ARBITRARY_DEPTH_RECURSION.md", "markdown"),
    ("H3_LAYER_TAGGED_ABC.cse.txt", "text"),
    ("H3_UNIT_ABC.cse.txt", "text"),
    ("H4_LAYER_TAGGED_ABC.cse.txt", "text"),
    ("H4_UNIT_ABC.cse.txt", "text"),
)

AUDIT_PATHS = (
    HERE / "PRIMARY_FREEZE_MANIFEST.json",
    DEPTH_ROOT / "independent/FROZEN_MANIFEST.json",
    DEPTH_ROOT / "audit/FROZEN_MAP_COMPARISON.json",
    DEPTH_ROOT / "audit/SYMBOLIC_Q0_AUDIT.json",
    DEPTH_ROOT / "audit/STRUCTURAL_AUDIT.md",
    DEPTH_ROOT / "audit/PROBABILITY_AUDIT.md",
    DEPTH_ROOT / "audit/TWO_ORACLE_GATE.json",
    DEPTH_ROOT / "audit/NORMALIZED_SINE_EXPERIMENT.json",
    DEPTH_ROOT / "independent/CONTROL_AUDIT.json",
    HERE / "NORMALIZED_SINE_CONTROL.json",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def build_bytes() -> tuple[bytes, dict[str, dict[str, object]]]:
    preamble = (HERE / "REPORT_PREAMBLE.md").read_text(encoding="utf-8")
    if "{{" in preamble:
        raise RuntimeError("unresolved report placeholder")
    pieces = [preamble.rstrip() + "\n"]
    records: dict[str, dict[str, object]] = {}
    headings = {
        "ARBITRARY_DEPTH_RECURSION.md": "Part II. Arbitrary-fixed-depth derivation",
        "H3_LAYER_TAGGED_ABC.cse.txt": "Part III. H=3 arbitrary-variance terminal formula",
        "H3_UNIT_ABC.cse.txt": "Part IV. H=3 unit-Gram terminal formula",
        "H4_LAYER_TAGGED_ABC.cse.txt": "Part V. H=4 arbitrary-variance terminal formula",
        "H4_UNIT_ABC.cse.txt": "Part VI. H=4 unit-Gram terminal formula",
    }
    for name, mode in EMBEDS:
        path = HERE / name
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        if not text.endswith("\n"):
            raise RuntimeError(f"embedded source lacks terminal LF: {name}")
        digest = sha256_bytes(raw)
        pieces.append(f"\n# {headings[name]}\n\n")
        pieces.append(
            f"<!-- ROUTE_S_EMBED_BEGIN file={name} sha256={digest} mode={mode} -->\n"
        )
        if mode == "text":
            pieces.append("```text\n")
            pieces.append(text)
            pieces.append("```\n")
        else:
            pieces.append(text)
        pieces.append(f"<!-- ROUTE_S_EMBED_END file={name} -->\n")
        records[name] = {
            "sha256": digest,
            "bytes": len(raw),
            "mode": mode,
        }
    return "".join(pieces).encode("utf-8"), records


def build() -> None:
    report_bytes, embedded = build_bytes()
    missing = [str(path) for path in AUDIT_PATHS if not path.exists()]
    if missing:
        raise RuntimeError(f"required audit artifacts missing: {missing}")
    REPORT.write_bytes(report_bytes)
    manifest = {
        "schema": "route-s-self-contained-report-v1",
        "report": {
            "file": REPORT.name,
            "bytes": len(report_bytes),
            "sha256": sha256_bytes(report_bytes),
        },
        "preamble": {
            "file": "REPORT_PREAMBLE.md",
            "sha256": sha256(HERE / "REPORT_PREAMBLE.md"),
        },
        "embedded_sources": embedded,
        "audit_sources": {
            str(path.relative_to(DEPTH_ROOT)): sha256(path) for path in AUDIT_PATHS
        },
        "consistency_rule": (
            "build_bytes() concatenates the preamble and each embedded source "
            "without transforming embedded payload bytes; --check reconstructs "
            "and requires byte equality with the report"
        ),
    }
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    MANIFEST_SHA.write_text(
        f"{sha256(MANIFEST)}  {MANIFEST.name}\n", encoding="utf-8"
    )
    print("report_sha256", manifest["report"]["sha256"])
    print("manifest_sha256", sha256(MANIFEST))


def check() -> None:
    expected, embedded = build_bytes()
    if REPORT.read_bytes() != expected:
        raise AssertionError("self-contained report differs from deterministic rebuild")
    manifest = json.loads(MANIFEST.read_text())
    if manifest["report"]["sha256"] != sha256(REPORT):
        raise AssertionError("report hash mismatch")
    for name, record in embedded.items():
        if manifest["embedded_sources"][name] != record:
            raise AssertionError(f"embedded manifest mismatch: {name}")
    for relative, digest in manifest["audit_sources"].items():
        if sha256(DEPTH_ROOT / relative) != digest:
            raise AssertionError(f"audit source drift: {relative}")
    recorded_manifest_hash = MANIFEST_SHA.read_text().split()[0]
    if recorded_manifest_hash != sha256(MANIFEST):
        raise AssertionError("manifest exact-file hash mismatch")
    print("PASS deterministic report byte reconstruction")
    print("PASS all embedded source and audit hashes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check() if args.check else build()


if __name__ == "__main__":
    main()
