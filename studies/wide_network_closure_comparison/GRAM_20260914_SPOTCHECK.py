"""Independent raw-array spot check of the declared arcs/8192 Gram metrics.

This script never imports the analyzer or a scientific producer and never trains.
It writes only gram_spotcheck.json in the assigned completed GRAM run directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[name] = "1"
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison/GRAM_20260914_v1"


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024**2), b""):
            result.update(block)
    return result.hexdigest()


def one(rows, **criteria):
    matches = [row for row in rows if all(row.get(key) == value for key, value in criteria.items())]
    if len(matches) != 1:
        raise AssertionError(("Expected one reported row", criteria, len(matches)))
    return matches[0]


def norm(matrix, q):
    """Explicit probability-weighted entry sum, independent of analyzer einsum."""
    squares = (matrix * matrix) * np.outer(q, q)
    return math.sqrt(math.fsum(float(value) for value in squares.ravel()))


def metrics(left, right, q, times, increment):
    rms, entries, reference = [], [], []
    for instant in range(len(times)):
        a, b = left[instant], right[instant]
        if increment:
            a, b = a - left[0], b - right[0]
        difference = a - b
        rms.append(norm(difference, q))
        entries.append(float(np.max(np.abs(difference))))
        reference.append(norm(b, q))
    integral = math.fsum(float(times[j+1] - times[j]) * (rms[j+1] + rms[j]) / 2
                         for j in range(len(times)-1))
    return dict(primary_rms_max=max(rms), rms_initial=rms[0], rms_terminal=rms[-1],
                rms_time_integral=integral, rms_time_average=integral / float(times[-1]-times[0]),
                maximum_entry_error=max(entries), reference_rms_max=max(reference),
                reference_rms_initial=reference[0], reference_rms_terminal=reference[-1],
                rms_curve=rms, entry_max_curve=entries, reference_rms_curve=reference)


def main(output):
    started = time.perf_counter()
    output = output.resolve()
    if output != GENERATED.resolve():
        raise ValueError("Spot check restricted to the assigned generated run")
    destination = output / "gram_spotcheck.json"
    if destination.exists():
        raise FileExistsError("Refusing to overwrite an earlier spot-check result")
    source_paths = (STUDY / "GRAM_20260914_PLAN.md", STUDY / "GRAM_20260914_ANALYSIS.py",
                    output / "gram_comparison.json", output / "inputs.npz")
    hashes = {str(path): digest(path) for path in source_paths}
    report = json.loads((output / "gram_comparison.json").read_text())
    with np.load(output / "inputs.npz", allow_pickle=False) as archive:
        inputs = {key: archive[key].copy() for key in archive.files}
    times = inputs["times"]
    assert times.shape == (206,) and times[0] == 0 and times[-1] == 40
    cache, run_inputs = {}, []

    def load(family, name):
        key = family, name
        if key not in cache:
            directory = output / family / name
            record = json.loads((directory / "record.json").read_text())
            assert record["status"] == "complete" and record["gram_completed_observations"] == 206
            actual = digest(directory / "gram.npy")
            assert actual == record["gram_sha256"]
            gram = np.load(directory / "gram.npy", mmap_mode="r", allow_pickle=False)
            assert gram.shape == (206, 2, 144, 144) and gram.dtype == np.float64
            run_inputs.append(dict(family=family, name=name, gram_sha256=actual,
                                   record_sha256=digest(directory / "record.json")))
            cache[key] = gram
        return cache[key]

    # Deliberately use sum-then-divide, rather than the analyzer's divide-then-sum.
    network_mean = sum(np.asarray(load("network", f"arcs_n8192_s{seed}"))
                       for seed in (11, 29, 47)) / 3
    comparisons, control_checks, baseline_checks, classifications = [], [], [], []
    differences = []

    def compare(got, reported, identity):
        errors = {}
        for field, calculated in got.items():
            supplied = np.asarray(reported[field], dtype=float)
            error = float(np.max(np.abs(np.asarray(calculated) - supplied)))
            errors[field] = error
            if not np.allclose(calculated, supplied, atol=1e-12, rtol=1e-11):
                raise AssertionError((identity, field, error))
            differences.append(error)
        return dict(identity, recomputed={key: value for key, value in got.items() if not key.endswith("curve")},
                    maximum_report_difference=max(errors.values()), per_field_report_differences=errors)

    panels = (("data", slice(0, 16), inputs["arcs_probabilities"]),
              ("circle", slice(16, 144), np.full(128, 1/128)))
    for panel, selection, q in panels:
        for layer in (1, 2):
            reference = network_mean[:, layer-1, selection, selection]
            baseline = metrics(np.broadcast_to(reference[0], reference.shape), reference, q, times, False)
            reported = one(report["frozen_initial_baselines"], case="arcs", width=8192,
                           family="network_seed_mean", panel=panel, layer=layer)
            baseline_checks.append(compare(baseline, reported, dict(panel=panel, layer=layer)))
            for order in (1, 3, 5):
                closure = load("closure", f"arcs_N{order}")[:, layer-1, selection, selection]
                for observable in ("G", "DeltaG"):
                    got = metrics(closure, reference, q, times, observable == "DeltaG")
                    identity = dict(case="arcs", width=8192, closure=f"arcs_N{order}",
                                    panel=panel, layer=layer, observable=observable)
                    reported = one(report["seed_mean_comparisons"], **identity)
                    comparisons.append(compare(got, reported, identity))
                    classification = ("close" if got["primary_rms_max"] <= .02 else
                                      "material_disagreement" if got["primary_rms_max"] > .05 else "inconclusive")
                    assert classification == reported["descriptive_closeness"]
                    classifications.append(dict(identity, descriptive_closeness=classification))
    controls = (("network_time_control", "network", "arcs_n8192_s11_halfstep", "arcs_n8192_s11"),
                ("network_precision_control", "network", "arcs_n2048_s11_float64", "arcs_n2048_s11"),
                ("closure_quadrature_control", "closure", "arcs_N3_refined", "arcs_N3"),
                ("closure_time_control", "closure", "arcs_N3_halfstep", "arcs_N3"))
    for kind, family, left_name, right_name in controls:
        left, right = load(family, left_name), load(family, right_name)
        for panel, selection, q in panels:
            for layer in (1, 2):
                for observable in ("G", "DeltaG"):
                    got = metrics(left[:, layer-1, selection, selection], right[:, layer-1, selection, selection],
                                  q, times, observable == "DeltaG")
                    identity = dict(case="arcs", control_kind=kind, panel=panel, layer=layer, observable=observable)
                    reported = one(report["numerical_controls"], **identity)
                    checked = compare(got, reported, identity)
                    checked["below_declared_0_002"] = got["primary_rms_max"] <= .002
                    assert checked["below_declared_0_002"] == reported["below_declared_0_002"]
                    control_checks.append(checked)
    trends = []
    for panel, _, _ in panels:
        for layer in (1, 2):
            for observable in ("G", "DeltaG"):
                identity = dict(case="arcs", width=8192, panel=panel, layer=layer, observable=observable)
                values = [one(comparisons, **identity, closure=f"arcs_N{order}")["recomputed"]["primary_rms_max"]
                          for order in (1, 3, 5)]
                matched = [row for row in control_checks if row["panel"] == panel and row["layer"] == layer
                           and row["observable"] == observable]
                assert len(matched) == 4
                worst = max(row["recomputed"]["primary_rms_max"] for row in matched)
                monotone = values[0] >= values[1] >= values[2]
                attributable = worst <= .002 and all(values[j] - values[j+1] > worst for j in (0, 1))
                reported = one(report["monotonicity"], **identity, metric="primary_rms_max")
                assert reported["monotone_nondecreasing_accuracy"] == monotone
                assert reported["order_attribution_supported_by_declared_diagnostics"] == attributable
                for order in (1, 3, 5):
                    row = one(report["seed_mean_comparisons"], **identity, closure=f"arcs_N{order}")
                    assert row["numerical_controls_pass"] == (worst <= .002)
                trends.append(dict(identity, N1=values[0], N3=values[1], N5=values[2], maximum_control=worst,
                                   monotone=monotone, numerically_resolved=worst <= .002,
                                   order_attribution_supported=attributable))
    labels = []
    for case in ("axis", "arcs"):
        u, y = inputs[case + "_inputs"], inputs[case + "_labels"]
        margins = y * (u[:, 0] - u[:, 1]) / math.sqrt(2)
        assert np.min(margins) > 0
        labels.append(dict(case=case, count=len(y), labels=y.tolist(), separator="u_x-u_y",
                           minimum_normalized_signed_margin=float(np.min(margins))))
    for path in source_paths:
        assert digest(path) == hashes[str(path)], "Input changed during spot check"
    result = dict(status="passed", claim_type="internal empirical postprocessing check",
                  source_sha256=digest(__file__), command=sys.argv, numpy_version=np.__version__,
                  wall_seconds=time.perf_counter()-started, input_hashes=hashes, raw_runs=run_inputs,
                  primary_comparisons=comparisons, numerical_control_checks=control_checks,
                  frozen_initial_baselines=baseline_checks, label_separation=labels,
                  primary_classifications=classifications, primary_trend_checks=trends,
                  maximum_metric_report_discrepancy=max(differences),
                  input_scope="Only this study's frozen Gram plan, analysis source, and completed GRAM_20260914_v1 arrays/records/report. No analyzer invocation, producer import, training, or other study.",
                  limitations=["Spot-check numerical comparisons cover arcs and width8192 seed means; axis metrics and width2048 primary comparisons were not independently recomputed.",
                               "N3 time/quadrature controls do not bound N5 error, and network precision was controlled at width2048.",
                               "Finite-panel, saved-time Gram checks do not certify continuous-time or infinite-width convergence.",
                               "This is a scoped internal author-method check with prior implementation involvement, not an isolated promotion review."])
    with destination.open("x") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps(dict(status=result["status"], comparisons=len(comparisons), controls=len(control_checks),
                          baselines=len(baseline_checks), maximum_metric_report_discrepancy=max(differences),
                          wall_seconds=result["wall_seconds"], output=str(destination)), indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=GENERATED)
    main(parser.parse_args().output)
