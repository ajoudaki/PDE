"""Prepare the frozen Gram replay menu and literal inputs; never train a model.

The study-owned literal input specification reconstructs the original NPZ. Its
exact JSON bytes remain the input metadata expected by the closure manifest.
Fresh preparation provenance is recorded in gram_campaign.json instead.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

sys.dont_write_bytecode = True
STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison"
HISTORICAL = GENERATED / "WIDE_GPU_20260914_202109Z"
PLAN = STUDY / "GRAM_20260914_PLAN.md"
INPUT_SPECIFICATION = STUDY / "WIDE_GPU_20260914_INPUTS.json"
_spec = importlib.util.spec_from_file_location(
    "gram_prepare_original_closure", STUDY / "WIDE_GPU_20260914_CLOSURE.py")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)


def network_configurations():
    """Exact original sixteen-run order, fixed in source rather than run output."""
    items = []
    for width in (2048, 8192):
        for seed in (11, 29, 47):
            for case in ("axis", "arcs"):
                items.append(dict(name=f"{case}_n{width}_s{seed}", case=case,
                    width=width, seed=seed, step=.01, dtype="float32", kind="primary"))
    for case in ("axis", "arcs"):
        items.append(dict(name=f"{case}_n8192_s11_halfstep", case=case,
            width=8192, seed=11, step=.005, dtype="float32", kind="time_control"))
        items.append(dict(name=f"{case}_n2048_s11_float64", case=case,
            width=2048, seed=11, step=.01, dtype="float64", kind="precision_control"))
    return items


def git_metadata():
    result = {}
    for key, arguments in (("git_head", ("rev-parse", "HEAD")),
            ("git_status", ("status", "--porcelain=v1", "--untracked-files=all"))):
        completed = subprocess.run(("git", *arguments), cwd=ROOT,
                                   capture_output=True, text=True, check=False)
        result[key] = completed.stdout.rstrip("\n") if completed.returncode == 0 else None
        if completed.returncode:
            result[key + "_error"] = completed.stderr.strip()
    return result


def prepare(output):
    output = Path(output)
    if output.is_symlink():
        raise ValueError("output may not be a symbolic link")
    output = output.resolve()
    if output.parent != GENERATED.resolve() or not output.name.startswith("GRAM_"):
        raise ValueError("output must be a direct GRAM_* child of this study's generated namespace")
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise FileExistsError("refusing to prepare a nonempty or non-directory destination")
    # The reader validates literal array hashes, data laws, time grid and panel.
    arrays, specification = base.read_input_specification()
    literal_json = INPUT_SPECIFICATION.read_bytes()
    if literal_json != (HISTORICAL / "inputs.json").read_bytes():
        raise ValueError("study input specification differs from the historical manifest")
    historical_npz_sha256 = base.digest(HISTORICAL / "inputs.npz")
    if historical_npz_sha256 != specification["npz_sha256"]:
        raise ValueError("historical input archive differs from the literal specification checksum")
    if not output.exists():
        output.mkdir(parents=False, exist_ok=False)
    with (output / "inputs.npz").open("xb") as stream:
        base.np.savez_compressed(stream, **arrays)
    inputs_sha256 = base.digest(output / "inputs.npz")
    if inputs_sha256 != historical_npz_sha256:
        raise ValueError("reconstructed NPZ bytes differ from the frozen input; partial preparation retained")
    with (output / "inputs.json").open("xb") as stream:
        stream.write(literal_json)
    base.load_inputs(output)
    sources = base.source_hashes()
    sources.update({str(path.relative_to(ROOT)): base.digest(path) for path in
        (Path(__file__), PLAN, STUDY / "GRAM_20260914_NETWORK.py", STUDY / "GRAM_20260914_CLOSURE.py")})
    campaign = dict(format="gram-20260914-prepared-campaign-v1", status="prepared",
        plan_sha256=base.digest(PLAN), source_run=str(HISTORICAL),
        network_configs=network_configurations(),
        panel_order="training inputs followed by all 128 circle inputs, without deduplication",
        confirmed_quantity="hidden-activation input-index Gram",
        experiment_started_epoch=time.time(), created_utc=datetime.now(timezone.utc).isoformat(),
        command=sys.argv, source_hashes=sources, **git_metadata(),
        inputs_sha256=inputs_sha256, inputs_json_sha256=base.digest(output / "inputs.json"),
        input_specification_sha256=base.digest(INPUT_SPECIFICATION),
        preparation="Decode and validate the study-owned literal specification, regenerate identical NPZ bytes, preserve literal JSON bytes.",
        source_scope="This study's own specification and historical input hashes; no other study is read.",
        expected_network_runs=16, expected_closure_runs=10,
        clock_semantics="The shared 2400-second campaign budget begins at preparation; launch both campaigns immediately.",
        scientific_trajectories_started=0)
    with (output / "gram_campaign.json").open("x") as stream:
        json.dump(campaign, stream, indent=2, allow_nan=False)
        stream.write("\n")
    return campaign


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="fresh empty GRAM_* folder in this study's generated namespace")
    arguments = parser.parse_args()
    campaign = prepare(arguments.output)
    print(json.dumps(dict(status=campaign["status"], output=str(arguments.output.resolve()),
        network_runs=len(campaign["network_configs"]), closure_runs=campaign["expected_closure_runs"],
        inputs_sha256=campaign["inputs_sha256"], scientific_trajectories_started=0), indent=2))


if __name__ == "__main__":
    main()
