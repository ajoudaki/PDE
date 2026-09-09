"""Resolve relocated source labels and inspect the original historical seal.

Historical inspection never authorizes a new trajectory or refreshes a hash.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


AUDIT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = AUDIT_ROOT.parents[1]
HISTORICAL_ROOT = REPO_ROOT / "data/historical/studies/resnet_proof_audit"
HISTORICAL_SEAL = HISTORICAL_ROOT / "results/seals/FROZEN_INPUTS.json"


def resolve_frozen_source(
    audit_root: Path,
    workspace_root: Path,
    label: str,
    *,
    historical_protocol: bool = False,
) -> Path:
    relative = Path(label)
    if not relative.parts or relative.is_absolute() or any(part in {"", ".", ".."} for part in label.split("/")):
        raise ValueError(f"unsafe frozen source label: {label!r}")
    paths = [audit_root / relative, workspace_root / relative]
    if relative.parts[0] == "activation_linearity_smoking_gun":
        paths.append(workspace_root / "resnet_activation_controls" / Path(*relative.parts[1:]))
    candidates = list(dict.fromkeys(path for path in paths if path.is_file()))
    if not candidates and historical_protocol and audit_root.resolve() == AUDIT_ROOT:
        retained = HISTORICAL_ROOT / relative
        if relative.parts[0] == "protocol" and retained.is_file():
            candidates.append(retained)
    if len(candidates) != 1:
        if not candidates:
            raise FileNotFoundError(f"missing frozen source: {label}")
        raise ValueError(f"ambiguous frozen source label: {label}")
    return candidates[0]


def historical_seal_status() -> dict:
    if not HISTORICAL_SEAL.is_file():
        return {"status": "historical_seal_missing", "path": str(HISTORICAL_SEAL),
                "current_execution_authorized": False}
    raw = HISTORICAL_SEAL.read_bytes()
    seal = json.loads(raw)
    sources = []
    for item in seal["files"]:
        label = item["path"]
        try:
            path = resolve_frozen_source(AUDIT_ROOT, AUDIT_ROOT.parent, label,
                                         historical_protocol=True)
        except (FileNotFoundError, ValueError) as exc:
            sources.append({"label": label, "status": "unresolved", "reason": str(exc)})
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        sources.append({"label": label, "path": str(path),
                        "status": "matches_recorded_bytes" if actual == item["sha256"] else "changed_since_freeze"})
    return {
        "status": "historical_only",
        "current_execution_authorized": False,
        "path": str(HISTORICAL_SEAL),
        "seal_sha256": hashlib.sha256(raw).hexdigest(),
        "recorded_status": seal.get("status"),
        "recorded_environment": seal.get("environment"),
        "source_locations": sources,
        "note": "Original seal retained unchanged; relocated live source is not a refreshed scientific freeze.",
    }
