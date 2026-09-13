"""Independent read-only archive checks; no solver imports or trajectory calls."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parent
EDITION = ROOT.parents[2]
ANALYSIS = ROOT.parent / "H4_independent_analysis_v1"


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def exact_values(archive, name):
    row = archive["arrays"][name]
    if archive["digits"] is None:
        values = [Fraction.from_float(float.fromhex(x)) for x in row["values"]]
    elif archive["backend"] == "rational":
        scale = 10 ** archive["digits"]
        values = [Fraction(int(x, 16), scale) for x in row["values"]]
    else:
        values = [Fraction(x) for x in row["values"]]
    return np.asarray(values, dtype=object).reshape(row["shape"])


def rational_record(value):
    return dict(numerator=hex(value.numerator), denominator=hex(value.denominator), float_view=float(value))


def run():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    started, wall = time.process_time(), time.monotonic()
    plan = json.loads((EDITION / "code/validation/observable_horizon_plan.json").read_text())
    result = dict(format="H4-independent-exact-archive-check-v1", command=sys.argv,
                  cwd=str(Path.cwd()), script_sha256=digest(Path(__file__)),
                  scope="Saved values only; exact rational subtraction and polynomial algebra. No new trajectories.",
                  archives=[], rational_polynomial_rounding_gaps=[], rational_precision_comparisons=[])
    precise = {}
    for config in plan["configurations"]:
        folder = ROOT / config["id"]
        record = json.loads((folder / "record.json").read_text())
        assert record["configuration"] == config
        if record["status"] != "operational_pass":
            continue
        dims = record["dimensions"]
        expected = {1: (5, 3), 3: (35, 10), 5: (128, 21)}[config["order"]]
        assert (dims["first_features"], dims["second_features"]) == expected
        assert dims["first_nodes"] == dims["second_nodes"] == config["population_nodes"]
        assert dims["action_matrix"] == [expected[1], expected[0]]
        assert record["restart_exact"] and all(record["restart_comparison"].values())
        assert record["restart_prediction_exact"]
        assert record["frozen_signature_initial"] == record["frozen_signature_final"]
        p, (d1, d2), a = config["population_nodes"], expected, dims["input_nodes"]
        for phase in ("initial", "final"):
            workspace = record["workspace_" + phase]
            assert workspace["state_scalars"] == p * (d1 + 5) + p * (d2 + 2) + 2 * d1 * d2
            assert workspace["data_scalars"] == 4 * a
        midpoint = json.loads((folder / "midpoint_restart.json").read_text())
        final = json.loads((folder / "final_restart.json").read_text())
        for key in ("format", "digits", "backend", "metadata", "data_metadata", "data"):
            assert midpoint[key] == final[key]
        for key in ("b1", "g", "p1", "b2", "p2", "D"):
            assert midpoint["state"][key] == final["state"][key]
        for item in record["observations"]:
            path = folder / item["exact_json"]
            archive = json.loads(path.read_text())
            assert archive["format"] == "observable-horizon-observations-v1"
            assert archive["time"] == item["time"]
            assert archive["digits"] == config["digits"] and archive["backend"] == config["backend"]
            scalars = 0
            with np.load(folder / item["npz"], allow_pickle=False) as npz:
                assert set(archive["arrays"]) == set(npz.files)
                for key, row in archive["arrays"].items():
                    assert tuple(row["shape"]) == npz[key].shape
                    assert len(row["values"]) == npz[key].size
                    scalars += len(row["values"])
                    if archive["digits"] is None:
                        decoded = np.asarray([float.fromhex(x) for x in row["values"]]).reshape(row["shape"])
                    else:
                        decoded = np.asarray(exact_values(archive, key), dtype=float)
                    assert np.isfinite(decoded).all()
                    assert decoded.tobytes() == npz[key].tobytes(), (config["id"], item["time"], key)
            result["archives"].append(dict(id=config["id"], time=item["time"], scalars=scalars,
                                           json_sha256=digest(path), float_view_bitwise_equal=True))
            if archive["backend"] == "rational":
                arrays = {k: exact_values(archive, k) for k in archive["arrays"]}
                precise[(config["id"], item["time"])] = arrays
                weights = arrays["input_weights"]
                expected_loss = sum(w * (y - target) ** 2 for w, y, target in
                                    zip(weights, arrays["training_prediction"], arrays["labels"]))
                gaps = dict(loss=rational_record(arrays["loss"].item() - expected_loss))
                for suffix, prefix in (("1", "first"), ("2", "second")):
                    pairs = arrays[prefix + "_pairs"]
                    expected_motion = sum(weight * weights[j] * (pairs[i, j, 1] - pairs[i, j, 0]) ** 2
                                          for i, weight in enumerate(arrays[prefix + "_weights"])
                                          for j in range(len(weights)))
                    gaps["rms" + suffix + "_squared"] = rational_record(arrays["rms" + suffix].item() ** 2 - expected_motion)
                result["rational_polynomial_rounding_gaps"].append(dict(id=config["id"], time=item["time"], gaps=gaps))
    for instant in plan["common"]["observation_times"]:
        first = precise.get(("tiny_rational24", instant))
        second = precise.get(("tiny_rational36", instant))
        if first is None or second is None:
            continue
        differences = [b - a for a, b in zip(first["prediction"], second["prediction"])]
        result["rational_precision_comparisons"].append(dict(time=instant,
            exact_panel_max_abs=rational_record(max(map(abs, differences))),
            unequal_exact_prediction_entries=sum(x != 0 for x in differences),
            equal_float_view_prediction_entries=sum(float(a) == float(b) for a, b in zip(first["prediction"], second["prediction"])),
            exact_loss_difference=rational_record(second["loss"].item() - first["loss"].item()),
            exact_rms1_difference=rational_record(second["rms1"].item() - first["rms1"].item()),
            exact_rms2_difference=rational_record(second["rms2"].item() - first["rms2"].item())))
    result.update(status="pass", cpu_seconds=time.process_time()-started, wall_seconds=time.monotonic()-wall,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
    output = ANALYSIS / "exact_archive_checks.json"
    with output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({k: result[k] for k in ("status", "cpu_seconds", "wall_seconds", "peak_rss_bytes", "rational_precision_comparisons")}))


if __name__ == "__main__":
    run()
