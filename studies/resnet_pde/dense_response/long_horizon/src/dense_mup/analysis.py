"""Plateau, uniform-error, table, and plot generation."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .experiment import load_trace


def _norm_last(x: np.ndarray) -> np.ndarray:
    return np.linalg.norm(x, axis=(-2, -1))


def _quantiles(values: Iterable[float]) -> dict[str, float]:
    x = np.asarray(list(values), dtype=float)
    return {
        "min": float(np.min(x)),
        "median": float(np.median(x)),
        "p90": float(np.quantile(x, 0.9)),
        "max": float(np.max(x)),
    }


def plateau_at_horizon(
    metadata: dict[str, Any],
    arrays: dict[str, np.ndarray],
    method_index: int,
    horizon: float,
    protocol: dict[str, Any],
) -> dict[str, Any] | None:
    """Evaluate the audit-fixed half-horizon tail test."""

    elapsed = arrays["times"] - arrays["times"][0]
    if horizon > elapsed[-1] + 1e-12:
        return None
    end = int(np.argmin(np.abs(elapsed - horizon)))
    tail_start = horizon * float(protocol["tail_fraction"])
    start = int(np.searchsorted(elapsed, tail_start - 1e-12))
    if end <= start:
        raise ValueError("plateau tail has fewer than two samples")

    y = np.asarray(metadata["y"], dtype=float)
    f = arrays["f"][method_index, : end + 1]
    grams = arrays["grams"][method_index, : end + 1]
    residual = arrays["residual_norm"][method_index, : end + 1]
    output_speed = arrays["output_speed"][method_index, : end + 1]
    gram_speed = arrays["gram_speed"][method_index, : end + 1]
    times = elapsed[: end + 1]

    S_f = max(1.0, float(np.linalg.norm(y)), float(np.linalg.norm(f[0])))
    S_g = max(1.0, float(np.max(_norm_last(grams[0]))))
    M_f = float(np.max(np.linalg.norm(f - f[0], axis=-1)))
    M_g = float(np.max(_norm_last(grams - grams[0])))
    delta_f = (
        float(protocol["absolute_scale"]) * S_f
        + float(protocol["motion_scale"]) * M_f
    )
    delta_g = (
        float(protocol["absolute_scale"]) * S_g
        + float(protocol["motion_scale"]) * M_g
    )

    tail = slice(start, end + 1)
    output_terminal_drift = float(
        np.max(np.linalg.norm(f[tail] - f[end], axis=-1))
    )
    gram_terminal_drift = float(
        np.max(_norm_last(grams[tail] - grams[end]))
    )
    max_residual = float(np.max(residual[tail]))
    max_output_speed = float(np.max(output_speed[tail]))
    max_gram_speed = float(np.max(gram_speed[tail]))
    output_arclength = float(
        np.trapezoid(output_speed[tail], x=times[tail])
    )
    gram_arclength = float(
        np.trapezoid(gram_speed[tail], x=times[tail])
    )
    checks = {
        "residual": max_residual
        <= float(protocol["residual_scale"]) * S_f,
        "output_terminal_drift": output_terminal_drift <= delta_f,
        "gram_terminal_drift": gram_terminal_drift <= delta_g,
        "output_speed": max_output_speed <= delta_f,
        "gram_speed": max_gram_speed <= delta_g,
        "output_arclength": output_arclength
        <= float(protocol["arclength_multiplier"]) * delta_f,
        "gram_arclength": gram_arclength
        <= float(protocol["arclength_multiplier"]) * delta_g,
    }
    return {
        "horizon": horizon,
        "tail_start": tail_start,
        "passes": bool(all(checks.values())),
        "checks": checks,
        "S_f": S_f,
        "S_g": S_g,
        "M_f": M_f,
        "M_g": M_g,
        "delta_f": delta_f,
        "delta_g": delta_g,
        "max_residual": max_residual,
        "output_terminal_drift": output_terminal_drift,
        "gram_terminal_drift": gram_terminal_drift,
        "max_output_speed": max_output_speed,
        "max_gram_speed": max_gram_speed,
        "output_arclength": output_arclength,
        "gram_arclength": gram_arclength,
    }


def plateau_ladder(
    metadata: dict[str, Any],
    arrays: dict[str, np.ndarray],
    method_index: int,
    protocol: dict[str, Any],
) -> dict[str, Any]:
    tests: list[dict[str, Any]] = []
    for horizon in protocol["horizons"]:
        test = plateau_at_horizon(
            metadata, arrays, method_index, float(horizon), protocol
        )
        if test is not None:
            tests.append(test)
    first_passing = next(
        (float(x["horizon"]) for x in tests if x["passes"]), None
    )
    candidate = None
    validated = None
    validation_drifts: list[dict[str, float]] = []
    elapsed = arrays["times"] - arrays["times"][0]
    f = arrays["f"][method_index]
    grams = arrays["grams"][method_index]
    # A stable candidate must have at least one later doubling. Every
    # available later audit-fixed doubling must pass, and every successive
    # H -> 2H drift must stay within the earlier horizon's tolerance.
    for start_index, start_test in enumerate(tests):
        suffix = tests[start_index:]
        if not start_test["passes"] or len(suffix) < 2:
            continue
        if not all(x["passes"] for x in suffix):
            continue
        local_drifts: list[dict[str, float]] = []
        chain_ok = True
        for previous, current in zip(suffix, suffix[1:]):
            if not np.isclose(
                float(current["horizon"]), 2.0 * float(previous["horizon"])
            ):
                chain_ok = False
                break
            i = int(
                np.argmin(np.abs(elapsed - float(previous["horizon"])))
            )
            j = int(
                np.argmin(np.abs(elapsed - float(current["horizon"])))
            )
            f_drift = float(np.linalg.norm(f[j] - f[i]))
            g_drift = float(np.max(_norm_last(grams[j] - grams[i])))
            record = {
                "from_horizon": float(previous["horizon"]),
                "to_horizon": float(current["horizon"]),
                "output": f_drift,
                "gram": g_drift,
                "output_threshold": float(previous["delta_f"]),
                "gram_threshold": float(previous["delta_g"]),
            }
            local_drifts.append(record)
            if (
                f_drift > float(previous["delta_f"])
                or g_drift > float(previous["delta_g"])
            ):
                chain_ok = False
                break
        if chain_ok:
            candidate = float(start_test["horizon"])
            validated = float(suffix[-1]["horizon"])
            validation_drifts = local_drifts
            break
    return {
        "tests": tests,
        "first_passing_horizon": first_passing,
        "candidate_horizon": candidate,
        "validated_through": validated,
        "validation_drifts": validation_drifts,
    }


def prediction_metrics(
    metadata: dict[str, Any],
    arrays: dict[str, np.ndarray],
    method_index: int,
    horizon: float | None = None,
) -> dict[str, float]:
    elapsed = arrays["times"] - arrays["times"][0]
    if horizon is None:
        end = len(elapsed) - 1
    else:
        end = int(np.argmin(np.abs(elapsed - horizon)))
    sl = slice(0, end + 1)
    f0 = arrays["f"][0, sl]
    fk = arrays["f"][method_index, sl]
    loss0 = arrays["loss"][0, sl]
    lossk = arrays["loss"][method_index, sl]
    g0 = arrays["grams"][0, sl]
    gk = arrays["grams"][method_index, sl]
    theta0 = arrays["theta"][0, sl]
    thetak = arrays["theta"][method_index, sl]

    output_error = np.linalg.norm(fk - f0, axis=-1)
    loss_error = np.abs(lossk - loss0)
    gram_error_td = _norm_last(gk - g0)
    theta_error = _norm_last(thetak - theta0)
    diagonal = np.diagonal(gk - g0, axis1=-2, axis2=-1)
    offdiag_mask = ~np.eye(g0.shape[-1], dtype=bool)
    offdiag = (gk - g0)[..., offdiag_mask]
    exact_motion = float(np.max(_norm_last(g0 - g0[0])))
    output_motion = float(
        np.max(np.linalg.norm(f0 - f0[0], axis=-1))
    )
    mid = g0.shape[1] // 2

    output_argmax = int(np.argmax(output_error))
    gram_flat_argmax = int(np.argmax(gram_error_td))
    gram_argmax = np.unravel_index(
        gram_flat_argmax, gram_error_td.shape
    )
    tail_start = int(np.searchsorted(elapsed[: end + 1], elapsed[end] / 2))
    tail = slice(tail_start, end + 1)
    return {
        "horizon": float(elapsed[end]),
        "sup_output_error": float(np.max(output_error)),
        "sup_loss_error": float(np.max(loss_error)),
        "sup_all_depth_gram_error": float(np.max(gram_error_td)),
        "sup_mid_gram_error": float(np.max(gram_error_td[:, mid])),
        "sup_terminal_gram_error": float(np.max(gram_error_td[:, -1])),
        "sup_diagonal_gram_error": float(
            np.max(np.linalg.norm(diagonal, axis=-1))
        ),
        "sup_offdiagonal_gram_error": float(
            np.max(np.linalg.norm(offdiag, axis=-1))
        ),
        "sup_theta_error": float(np.max(theta_error)),
        "tail_sup_output_error": float(np.max(output_error[tail])),
        "tail_sup_all_depth_gram_error": float(
            np.max(gram_error_td[tail])
        ),
        "terminal_output_error": float(output_error[-1]),
        "terminal_all_depth_gram_error": float(
            np.max(gram_error_td[-1])
        ),
        "output_error_time": float(elapsed[output_argmax]),
        "gram_error_time": float(elapsed[gram_argmax[0]]),
        "gram_error_depth_index": int(gram_argmax[1]),
        "l1_output_error": float(
            np.trapezoid(output_error, x=elapsed[sl])
        ),
        "l1_all_depth_gram_error": float(
            np.trapezoid(np.max(gram_error_td, axis=1), x=elapsed[sl])
        ),
        "normalized_output_error": float(
            np.max(output_error) / max(1.0, output_motion)
        ),
        "motion_normalized_gram_error": float(
            np.max(gram_error_td) / max(exact_motion, 1e-15)
        ),
        "sup_kernel_identity_defect": float(
            np.max(arrays["kernel_identity_defect"][method_index, sl])
        ),
        "sup_forward_defect": float(
            np.max(arrays["forward_defect"][method_index, sl])
        ),
        "sup_adjoint_defect": float(
            np.max(arrays["adjoint_defect"][method_index, sl])
        ),
        "sup_terminal_constraint_defect": float(
            np.max(arrays["terminal_defect"][method_index, sl])
        ),
        "max_loss_increase_per_sample": float(
            max(0.0, np.max(np.diff(lossk))) if lossk.size > 1 else 0.0
        ),
    }


def summarize_trace(
    path: Path, protocol: dict[str, Any]
) -> dict[str, Any]:
    metadata, arrays = load_trace(path)
    labels = [str(x) for x in arrays["method_labels"]]
    elapsed = arrays["times"] - arrays["times"][0]
    exact_grams = arrays["grams"][0]
    exact = {
        "initial_loss": float(arrays["loss"][0, 0]),
        "final_loss": float(arrays["loss"][0, -1]),
        "final_residual_norm": float(arrays["residual_norm"][0, -1]),
        "total_all_depth_gram_motion": float(
            np.max(_norm_last(exact_grams - exact_grams[0]))
        ),
        "terminal_mid_gram_motion": float(
            np.linalg.norm(
                exact_grams[-1, exact_grams.shape[1] // 2]
                - exact_grams[0, exact_grams.shape[1] // 2]
            )
        ),
        "terminal_out_gram_motion": float(
            np.linalg.norm(exact_grams[-1, -1] - exact_grams[0, -1])
        ),
        "min_sampled_theta_eigenvalue": float(
            np.min(arrays["theta_min"][0])
        ),
        "max_sampled_gram_speed": float(
            np.max(arrays["gram_speed"][0])
        ),
        "final_sampled_gram_speed": float(
            arrays["gram_speed"][0, -1]
        ),
        "duration": float(elapsed[-1]),
        "plateau": plateau_ladder(metadata, arrays, 0, protocol),
    }
    methods: dict[str, Any] = {}
    order_to_index = {
        int(order): idx for idx, order in enumerate(arrays["orders"])
    }
    for idx, label in enumerate(labels[1:], start=1):
        order = int(label[1:])
        active = arrays["residual_norm"][0] >= 1e-8
        derivative_idx = order_to_index[order]
        by_horizon = {}
        for horizon in protocol["horizons"]:
            if float(horizon) <= float(elapsed[-1]) + 1e-12:
                by_horizon[str(float(horizon))] = prediction_metrics(
                    metadata, arrays, idx, float(horizon)
                )
        methods[label] = {
            "prediction": prediction_metrics(metadata, arrays, idx),
            "by_horizon": by_horizon,
            "plateau": plateau_ladder(metadata, arrays, idx, protocol),
            "instantaneous_response": {
                "sup_h_relative_active": float(
                    np.max(arrays["inst_h_rel"][derivative_idx, active])
                ),
                "sup_p_relative_active": float(
                    np.max(arrays["inst_p_rel"][derivative_idx, active])
                ),
                "sup_h_rms": float(
                    np.max(arrays["inst_h_rms"][derivative_idx])
                ),
                "sup_p_rms": float(
                    np.max(arrays["inst_p_rms"][derivative_idx])
                ),
            },
        }
    return {
        "run_id": metadata["id"],
        "group": metadata["group"],
        "path": str(path),
        "metadata": metadata,
        "exact": exact,
        "methods": methods,
    }


def _flatten_rows(summaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for run in summaries:
        meta = run["metadata"]
        exact = run["exact"]
        for label, method in run["methods"].items():
            p = method["prediction"]
            rows.append(
                {
                    "run_id": run["run_id"],
                    "group": run["group"],
                    "method": label,
                    "order": int(label[1:]),
                    "n": meta["n"],
                    "depth": meta["depth"],
                    "seed": meta["seed"],
                    "sigma_w": meta["sigma_w"],
                    "A": meta["A"],
                    "gamma": meta["gamma"],
                    "restart_time": meta["restart_time"],
                    "dt": meta["dt"],
                    "duration": meta["duration"],
                    "code_sha256": meta["code_sha256"],
                    "config_sha256": meta["config_sha256"],
                    "model": meta["model"],
                    "training": meta["training"],
                    "surrogate": meta["surrogate"],
                    "actual_compiled_liouville_pde_run": meta[
                        "actual_compiled_liouville_pde_run"
                    ],
                    "integrator": meta["integrator"],
                    "exact_initial_loss": exact["initial_loss"],
                    "exact_final_loss": exact["final_loss"],
                    "exact_gram_motion": exact[
                        "total_all_depth_gram_motion"
                    ],
                    "exact_min_theta": exact[
                        "min_sampled_theta_eigenvalue"
                    ],
                    "exact_plateau_candidate": exact["plateau"][
                        "candidate_horizon"
                    ],
                    "exact_plateau_validated": exact["plateau"][
                        "validated_through"
                    ],
                    "surrogate_plateau_candidate": method["plateau"][
                        "candidate_horizon"
                    ],
                    "surrogate_plateau_validated": method["plateau"][
                        "validated_through"
                    ],
                    **p,
                }
            )
    return rows


def _horizon_rows(summaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for run in summaries:
        meta = run["metadata"]
        for label, method in run["methods"].items():
            previous: dict[str, float] | None = None
            for horizon_text, metrics in sorted(
                method["by_horizon"].items(), key=lambda item: float(item[0])
            ):
                row = {
                    "run_id": run["run_id"],
                    "group": run["group"],
                    "method": label,
                    "order": int(label[1:]),
                    "horizon": float(horizon_text),
                    "n": meta["n"],
                    "depth": meta["depth"],
                    "seed": meta["seed"],
                    "dt": meta["dt"],
                    "code_sha256": meta["code_sha256"],
                    "config_sha256": meta["config_sha256"],
                    **metrics,
                }
                if previous is None:
                    row["output_prefix_increment"] = None
                    row["gram_prefix_increment"] = None
                else:
                    row["output_prefix_increment"] = (
                        metrics["sup_output_error"]
                        - previous["sup_output_error"]
                    )
                    row["gram_prefix_increment"] = (
                        metrics["sup_all_depth_gram_error"]
                        - previous["sup_all_depth_gram_error"]
                    )
                rows.append(row)
                previous = metrics
    return rows


def _required_order_rows(
    summaries: list[dict[str, Any]], accuracy_levels: list[float]
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for run in summaries:
        methods = {
            int(label[1:]): method
            for label, method in run["methods"].items()
            if int(label[1:]) <= 3
        }
        horizons = sorted(
            {
                float(h)
                for method in methods.values()
                for h in method["by_horizon"]
            }
        )
        for horizon in horizons:
            key = str(float(horizon))
            for epsilon in accuracy_levels:
                qualifying = []
                for order, method in methods.items():
                    metrics = method["by_horizon"].get(key)
                    if metrics is None:
                        continue
                    if max(
                        metrics["sup_output_error"],
                        metrics["sup_all_depth_gram_error"],
                    ) <= epsilon:
                        qualifying.append(order)
                rows.append(
                    {
                        "run_id": run["run_id"],
                        "group": run["group"],
                        "horizon": horizon,
                        "epsilon": float(epsilon),
                        "minimum_order": min(qualifying)
                        if qualifying
                        else None,
                    }
                )
    return rows


def _refinement_comparison(
    summaries: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    refinement = [
        x for x in summaries if x["group"] == "refinement"
    ]
    if len(refinement) < 2:
        return []
    fine = min(refinement, key=lambda x: float(x["metadata"]["dt"]))
    medium = max(refinement, key=lambda x: float(x["metadata"]["dt"]))
    target_meta = fine["metadata"]
    coarse_candidates = [
        x
        for x in summaries
        if x["group"] == "central"
        and x["metadata"]["seed"] == target_meta["seed"]
        and x["metadata"]["n"] == target_meta["n"]
        and x["metadata"]["depth"] == target_meta["depth"]
        and np.isclose(x["metadata"]["sigma_w"], target_meta["sigma_w"])
        and np.isclose(x["metadata"]["A"], target_meta["A"])
        and np.isclose(x["metadata"]["gamma"], target_meta["gamma"])
    ]
    if not coarse_candidates:
        return []
    coarse = min(
        coarse_candidates, key=lambda x: float(x["metadata"]["dt"])
    )
    loaded = {}
    for name, summary in (
        ("coarse", coarse),
        ("medium", medium),
        ("fine", fine),
    ):
        _, loaded[name] = load_trace(Path(summary["path"]))
    fine_t = loaded["fine"]["times"] - loaded["fine"]["times"][0]
    horizon = float(fine_t[-1])
    rows: list[dict[str, Any]] = []

    def crop_and_index(
        arrays: dict[str, np.ndarray], label: str
    ) -> tuple[np.ndarray, int]:
        times = arrays["times"] - arrays["times"][0]
        end = int(np.argmin(np.abs(times - horizon)))
        if not np.allclose(times[: end + 1], fine_t, atol=1e-12, rtol=0.0):
            raise ValueError("refinement traces do not share the sample grid")
        labels = [str(x) for x in arrays["method_labels"]]
        return np.arange(end + 1), labels.index(label)

    common_labels = sorted(
        set(str(x) for x in loaded["coarse"]["method_labels"])
        & set(str(x) for x in loaded["medium"]["method_labels"])
        & set(str(x) for x in loaded["fine"]["method_labels"]),
        key=lambda x: (-1 if x == "exact" else int(x[1:])),
    )
    fine_labels = [str(x) for x in loaded["fine"]["method_labels"]]
    exact_fine_index = fine_labels.index("exact")
    for label in common_labels:
        indices = {
            name: crop_and_index(arrays, label)
            for name, arrays in loaded.items()
        }
        fine_time_index = indices["fine"][0]
        fine_idx = indices["fine"][1]
        exact_model_output = None
        exact_model_gram = None
        if label != "exact":
            exact_model_output = float(
                np.max(
                    np.linalg.norm(
                        loaded["fine"]["f"][fine_idx, fine_time_index]
                        - loaded["fine"]["f"][
                            exact_fine_index, fine_time_index
                        ],
                        axis=-1,
                    )
                )
            )
            exact_model_gram = float(
                np.max(
                    _norm_last(
                        loaded["fine"]["grams"][fine_idx, fine_time_index]
                        - loaded["fine"]["grams"][
                            exact_fine_index, fine_time_index
                        ]
                    )
                )
            )
        for comparison, left_name in (
            ("dt_0.02_vs_0.005", "coarse"),
            ("dt_0.01_vs_0.005", "medium"),
        ):
            left = loaded[left_name]
            left_time_index = indices[left_name][0]
            left_idx = indices[left_name][1]
            output = float(
                np.max(
                    np.linalg.norm(
                        left["f"][left_idx, left_time_index]
                        - loaded["fine"]["f"][fine_idx, fine_time_index],
                        axis=-1,
                    )
                )
            )
            gram = float(
                np.max(
                    _norm_last(
                        left["grams"][left_idx, left_time_index]
                        - loaded["fine"]["grams"][
                            fine_idx, fine_time_index
                        ]
                    )
                )
            )
            row = {
                "method": label,
                "comparison": comparison,
                "horizon": horizon,
                "output_difference": output,
                "all_depth_gram_difference": gram,
                "fine_model_output_error": exact_model_output,
                "fine_model_gram_error": exact_model_gram,
                "output_ratio_to_model_error": (
                    output / exact_model_output
                    if exact_model_output not in (None, 0.0)
                    else None
                ),
                "gram_ratio_to_model_error": (
                    gram / exact_model_gram
                    if exact_model_gram not in (None, 0.0)
                    else None
                ),
            }
            if label != "exact" and comparison == "dt_0.01_vs_0.005":
                row["resolved_at_dt_0.01"] = bool(
                    output <= max(1e-8, 0.1 * exact_model_output)
                    and gram <= max(1e-8, 0.1 * exact_model_gram)
                )
            else:
                row["resolved_at_dt_0.01"] = None
            rows.append(row)
    return rows


def _aggregate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in rows:
        if row["order"] > 3:
            continue
        groups.setdefault((row["group"], row["order"]), []).append(row)
    output: list[dict[str, Any]] = []
    for (group, order), values in sorted(groups.items()):
        record: dict[str, Any] = {
            "group": group,
            "order": order,
            "runs": len(values),
            "exact_plateau_validated_count": sum(
                x["exact_plateau_validated"] is not None for x in values
            ),
            "surrogate_plateau_validated_count": sum(
                x["surrogate_plateau_validated"] is not None for x in values
            ),
        }
        for key in (
            "sup_output_error",
            "sup_all_depth_gram_error",
            "sup_theta_error",
            "tail_sup_output_error",
            "tail_sup_all_depth_gram_error",
            "terminal_all_depth_gram_error",
            "motion_normalized_gram_error",
            "sup_forward_defect",
            "sup_adjoint_defect",
        ):
            record[key] = _quantiles(x[key] for x in values)
        output.append(record)
    return output


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _plot_representative(
    summary: dict[str, Any], figures: Path
) -> None:
    metadata, a = load_trace(Path(summary["path"]))
    labels = [str(x) for x in a["method_labels"]]
    t = a["times"] - a["times"][0]
    colors = {
        "exact": "black",
        "K0": "#9c755f",
        "K1": "#e15759",
        "K2": "#4e79a7",
        "K3": "#59a14f",
    }
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), constrained_layout=True)
    for i, label in enumerate(labels):
        if label not in colors:
            continue
        axes[0, 0].semilogy(
            t, np.maximum(a["loss"][i], 1e-30), label=label, color=colors[label]
        )
        mid = a["grams"].shape[2] // 2
        gmid_motion = _norm_last(
            a["grams"][i, :, mid] - a["grams"][i, 0, mid]
        )
        gout_motion = _norm_last(
            a["grams"][i, :, -1] - a["grams"][i, 0, -1]
        )
        axes[0, 1].plot(t, gmid_motion, color=colors[label], label=label)
        axes[0, 2].plot(t, gout_motion, color=colors[label], label=label)
        if i > 0:
            ferr = np.linalg.norm(a["f"][i] - a["f"][0], axis=-1)
            gerr = np.max(
                _norm_last(a["grams"][i] - a["grams"][0]), axis=1
            )
            axes[1, 0].semilogy(
                t, np.maximum.accumulate(np.maximum(ferr, 1e-18)),
                color=colors[label], label=label
            )
            axes[1, 1].semilogy(
                t, np.maximum.accumulate(np.maximum(gerr, 1e-18)),
                color=colors[label], label=label
            )
    axes[1, 2].semilogy(
        t, np.maximum(a["gram_speed"][0], 1e-30), color="black",
        label="exact"
    )
    for i, label in enumerate(labels[1:], start=1):
        if label in colors:
            axes[1, 2].semilogy(
                t, np.maximum(a["gram_speed"][i], 1e-30),
                color=colors[label], label=label
            )
    titles = [
        "Loss over simulated horizon",
        "Mid-depth Gram motion",
        "Terminal Gram motion",
        "Prefix recorded-grid max output error",
        "Prefix recorded-grid max all-depth Gram error",
        "Max all-depth Gram speed",
    ]
    for ax, title in zip(axes.flat, titles):
        ax.set_title(title)
        ax.set_xlabel("training time")
        ax.grid(alpha=0.25)
    axes[0, 0].set_ylabel("loss")
    axes[0, 1].set_ylabel("Frobenius motion")
    axes[0, 2].set_ylabel("Frobenius motion")
    axes[1, 0].set_ylabel("absolute error")
    axes[1, 1].set_ylabel("Frobenius error")
    axes[1, 2].set_ylabel("speed")
    axes[0, 0].legend(ncol=3, fontsize=8)
    fig.suptitle(
        f"Corrected q/r response projection: {metadata['id']}",
        fontsize=13,
    )
    fig.savefig(figures / "representative_curves.png", dpi=180)
    plt.close(fig)

    # Time-depth error heat maps for K=1 and K=2.
    selected = [x for x in ("K1", "K2") if x in labels]
    fig, axes = plt.subplots(
        1, len(selected), figsize=(6 * len(selected), 4), constrained_layout=True
    )
    if len(selected) == 1:
        axes = [axes]
    for ax, label in zip(axes, selected):
        i = labels.index(label)
        err = _norm_last(a["grams"][i] - a["grams"][0]).T
        image = ax.imshow(
            np.log10(np.maximum(err, 1e-16)),
            aspect="auto",
            origin="lower",
            extent=(t[0], t[-1], 0.0, 1.0),
            cmap="magma",
        )
        ax.set_title(f"{label}: log10 Gram error")
        ax.set_xlabel("training time")
        ax.set_ylabel("normalized depth")
        fig.colorbar(image, ax=ax)
    fig.savefig(figures / "time_depth_gram_error.png", dpi=180)
    plt.close(fig)

    # All six unique entries at the middle and terminal depths.
    for depth_index, name in ((a["grams"].shape[2] // 2, "mid"), (-1, "out")):
        fig, axes = plt.subplots(2, 3, figsize=(13, 7), constrained_layout=True)
        pairs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        for ax, (r, q) in zip(axes.flat, pairs):
            for i, label in enumerate(labels):
                if label in ("exact", "K1", "K2"):
                    ax.plot(
                        t,
                        a["grams"][i, :, depth_index, r, q],
                        color=colors[label],
                        label=label,
                    )
            ax.set_title(f"G[{r + 1},{q + 1}]")
            ax.grid(alpha=0.25)
            ax.set_xlabel("training time")
        axes[0, 0].legend()
        fig.suptitle(f"{name}-depth Gram entries")
        fig.savefig(figures / f"gram_entries_{name}.png", dpi=180)
        plt.close(fig)


def _plot_aggregate(
    rows: list[dict[str, Any]], figures: Path
) -> None:
    primary = [
        x
        for x in rows
        if x["order"] <= 3 and x["group"] not in ("control", "refinement")
    ]
    if not primary:
        fig, ax = plt.subplots(figsize=(7, 3), constrained_layout=True)
        ax.text(
            0.5,
            0.5,
            "No primary runs selected",
            ha="center",
            va="center",
            transform=ax.transAxes,
        )
        ax.set_axis_off()
        fig.savefig(figures / "order_convergence.png", dpi=180)
        plt.close(fig)
        return
    orders = sorted({x["order"] for x in primary})
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), constrained_layout=True)
    for ax, key, title in (
        (
            axes[0],
            "sup_output_error",
            "Prefix recorded-grid max output error",
        ),
        (
            axes[1],
            "sup_all_depth_gram_error",
            "Prefix recorded-grid max all-depth Gram error",
        ),
    ):
        data = [[x[key] for x in primary if x["order"] == order] for order in orders]
        ax.boxplot(data, tick_labels=[f"K={x}" for x in orders], showfliers=True)
        ax.set_yscale("log")
        ax.set_title(title)
        ax.set_ylabel("absolute error")
        ax.grid(alpha=0.25, axis="y")
    fig.savefig(figures / "order_convergence.png", dpi=180)
    plt.close(fig)


def _build_report(
    summaries: list[dict[str, Any]],
    rows: list[dict[str, Any]],
    aggregates: list[dict[str, Any]],
    horizon_rows: list[dict[str, Any]],
    required_order_rows: list[dict[str, Any]],
    refinement_rows: list[dict[str, Any]],
    representative_id: str,
) -> str:
    del aggregates  # The machine-readable aggregate remains a separate file.
    primary_rows = [
        x
        for x in rows
        if x["order"] <= 3 and x["group"] not in ("control", "refinement")
    ]
    by_order = {
        order: [x for x in primary_rows if x["order"] == order]
        for order in sorted({x["order"] for x in primary_rows})
    }
    primary_runs = [
        x for x in summaries if x["group"] not in ("control", "refinement")
    ]
    n_primary = len(primary_runs)
    exact_validated = sum(
        x["exact"]["plateau"]["validated_through"] is not None
        for x in primary_runs
    )
    method_validated = {
        order: sum(
            run["methods"].get(f"K{order}", {})
            .get("plateau", {})
            .get("validated_through")
            is not None
            for run in primary_runs
        )
        for order in by_order
    }
    if n_primary:
        motion = _quantiles(
            run["exact"]["total_all_depth_gram_motion"]
            for run in primary_runs
        )
        counts = ", ".join(
            f"K={order}: {method_validated[order]}/{n_primary}"
            for order in sorted(method_validated)
        )
        bottom_line = (
            f"The audit-fixed horizon-doubling plateau test passed for "
            f"{exact_validated}/{n_primary} exact trajectories and for "
            f"{counts} projected trajectories. Quantitative recorded-grid "
            f"prediction errors are reported below."
        )
    else:
        motion = None
        bottom_line = (
            "No completed primary runs were included, so this report makes "
            "no numerical accuracy or plateau claim."
        )

    lines = [
        "# Long-horizon dense Euclidean μP response audit",
        "",
        "## Bottom line",
        "",
        bottom_line,
        "",
        "**This is not a numerical run of the conjectured width-independent "
        "Liouville PDE.** Every projected simulation still retains all dense "
        "W matrices. Any positive numerical result here concerns the response-"
        "compression mechanism behind the PDE conjecture, not the homogenized "
        "finite-PDE limit itself.",
        "",
        "## Provenance",
        "",
        f"- Completed primary finite-network runs: {n_primary}",
        f"- Exact trajectories passing the audit-fixed doubling test: "
        f"{exact_validated}/{n_primary}",
        *[
            f"- K={order} projected trajectories passing the same test: "
            f"{method_validated[order]}/{n_primary}"
            for order in sorted(method_validated)
        ],
        "- Integrator: fixed-step classical RK4",
        "- Observable error: maximum over recorded times and every discrete "
        "depth node",
        "- Plateau test: residual, terminal drift, sampled vector-field speed, "
        "and trapezoidal tail-arclength estimate on the half-horizon tail",
        f"- Representative trace: `{representative_id}`",
        "- Actual compiled Liouville PDE runs: **0**",
        "",
        "## Recorded-grid errors over the full simulated horizon",
        "",
        "| Order | Runs | Output median (max) | All-depth Gram median (max) | "
        "Gram error / feature motion, median (max) |",
        "|---:|---:|---:|---:|---:|",
    ]
    for order, values in by_order.items():
        out = _quantiles(x["sup_output_error"] for x in values)
        gram = _quantiles(x["sup_all_depth_gram_error"] for x in values)
        normalized = _quantiles(
            x["motion_normalized_gram_error"] for x in values
        )
        lines.append(
            f"| {order} | {len(values)} | {out['median']:.3e} "
            f"({out['max']:.3e}) | {gram['median']:.3e} "
            f"({gram['max']:.3e}) | {normalized['median']:.3e} "
            f"({normalized['max']:.3e}) |"
        )
    lines.extend(
        [
            "",
            "These are curvewise prefix maxima on the stored time grid, not "
            "terminal-only errors. "
            "Near zero loss, loss error is deliberately not used as the main "
            "accuracy statistic because both systems fit the labels.",
            "",
            (
                "The exact all-depth feature motion had median "
                f"{motion['median']:.3e} and range "
                f"[{motion['min']:.3e},{motion['max']:.3e}]."
                if motion is not None
                else "No feature-motion statistic is available."
            ),
            "",
            "## Plateau interpretation",
            "",
            "For a candidate horizon H, the test uses every stored sample in "
            "[H/2,H]. It requires small residual, small distance to the "
            "terminal output and every terminal depth-Gram, small sampled "
            "vector-field output/Gram speeds, and small trapezoidal tail "
            "arclength. A candidate is accepted only when every later "
            "audit-fixed doubling through the final horizon passes and each "
            "successive drift stays below the earlier tolerance.",
            "",
            "This rules out two misleading shortcuts: a nearly constant "
            "Gram-motion radius while the matrix moves tangentially, and a "
            "prefix-maximum error that looks flat merely because its maximum "
            "occurred early.",
            "",
            "## Error growth across horizon doublings",
            "",
            "| H | K | max output error | max all-depth Gram error | "
            "max new output-prefix increment | max new Gram-prefix increment |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    primary_horizon = [
        x
        for x in horizon_rows
        if x["group"] not in ("control", "refinement") and x["order"] <= 3
    ]
    for horizon in sorted({x["horizon"] for x in primary_horizon}):
        for order in sorted({x["order"] for x in primary_horizon}):
            values = [
                x
                for x in primary_horizon
                if np.isclose(x["horizon"], horizon)
                and x["order"] == order
            ]
            if not values:
                continue
            output_increment = [
                float(x["output_prefix_increment"] or 0.0) for x in values
            ]
            gram_increment = [
                float(x["gram_prefix_increment"] or 0.0) for x in values
            ]
            lines.append(
                f"| {horizon:g} | {order} | "
                f"{max(x['sup_output_error'] for x in values):.3e} | "
                f"{max(x['sup_all_depth_gram_error'] for x in values):.3e} | "
                f"{max(output_increment):.3e} | "
                f"{max(gram_increment):.3e} |"
            )

    lines.extend(
        [
            "",
            "A zero late increment means the largest recorded-grid error "
            "occurred in an earlier prefix; it is not an infinite-time tail "
            "bound.",
            "",
            "## Required response order",
            "",
            "For each absolute tolerance ε, the table counts primary runs at "
            "the final common horizon whose recorded-grid output and all-depth "
            "Gram maxima are both at most ε.",
            "",
            "| ε | final H | K=0 | K=1 | K=2 | K=3 | unresolved |",
            "|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    primary_required = [
        x
        for x in required_order_rows
        if x["group"] not in ("control", "refinement")
    ]
    if primary_required:
        final_horizon = max(x["horizon"] for x in primary_required)
        for epsilon in sorted(
            {x["epsilon"] for x in primary_required}, reverse=True
        ):
            values = [
                x
                for x in primary_required
                if np.isclose(x["horizon"], final_horizon)
                and np.isclose(x["epsilon"], epsilon)
            ]
            counts = {
                order: sum(x["minimum_order"] == order for x in values)
                for order in range(4)
            }
            unresolved = sum(x["minimum_order"] is None for x in values)
            lines.append(
                f"| {epsilon:.0e} | {final_horizon:g} | "
                f"{counts[0]} | {counts[1]} | {counts[2]} | "
                f"{counts[3]} | {unresolved} |"
            )
    else:
        lines.append("| — | — | — | — | — | — | — |")

    lines.extend(
        [
            "",
            "## RK4 refinement on the representative trace",
            "",
            "| Method | Comparison | output difference | all-depth Gram "
            "difference | ratio to fine-grid model Gram error |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for record in refinement_rows:
        ratio = record["gram_ratio_to_model_error"]
        ratio_text = "—" if ratio is None else f"{ratio:.3e}"
        lines.append(
            f"| {record['method']} | {record['comparison']} | "
            f"{record['output_difference']:.3e} | "
            f"{record['all_depth_gram_difference']:.3e} | {ratio_text} |"
        )
    if not refinement_rows:
        lines.append("| — | no matched refinement traces | — | — | — |")

    lines.extend(
        [
            "",
            "The reconstructed tangent kernel for a projected state is a PSD "
            "proxy, not automatically the kernel driving its output rate. The "
            "raw traces therefore store the independent defect "
            "`||f_dot + theta_hat e||`; no surrogate coercivity claim is "
            "deduced merely from the proxy's eigenvalues.",
            "",
            "## Scientific status",
            "",
            f"- Observed exact plateau-test count: {exact_validated}/{n_primary}.",
            *[
                f"- Observed K={order} plateau-test count: "
                f"{method_validated[order]}/{n_primary}."
                for order in sorted(method_validated)
            ],
            "- The response order is fixed for each complete trajectory; no "
            "training-time Taylor restart or outcome-dependent order change "
            "is used.",
            "- Not tested: the J nonlinear grammar cutoff, N depth-Galerkin "
            "limit, Gaussian conditioning/Onsager compiler, width limit, or "
            "full outgoing residual of the finite Liouville PDE.",
            "- Not proved: literal uniformity on t in [0,∞), interchange of "
            "width/depth/response/time limits, or the PDE conjecture.",
            "",
            "## Files to inspect",
            "",
            "- `results/processed/per_run.csv`: one row per run and order.",
            "- `results/processed/errors_by_horizon.csv`: prefix maxima and "
            "new increments at every horizon doubling.",
            "- `results/processed/required_order.csv`: minimum K for each "
            "declared absolute tolerance.",
            "- `results/processed/refinement.csv`: common-grid RK4 refinement.",
            "- `results/processed/aggregate.json`: group/order quantiles.",
            "- `results/raw/*.npz`: loss, output, every depth-Gram, analytic "
            "speeds, kernels, constraint defects, and instantaneous q/r errors.",
            "- `figures/representative_curves.png`: complete simulated "
            "transient and operational plateau test.",
            "- `figures/time_depth_gram_error.png`: error over time and depth.",
            "- `tests/test_core.py`: algebraic and plateau-detector controls.",
            "- `theory/dense_euclidean_continuous_depth_pde_conjecture.md`: "
            "the finite-PDE specification whose homogenized convergence remains "
            "conjectural.",
            "",
        ]
    )
    return "\n".join(lines)


def analyze_directory(
    raw_dir: Path,
    processed_dir: Path,
    figures_dir: Path,
    protocol: dict[str, Any],
    representative_id: str,
    expected_manifest: list[dict[str, Any]],
) -> dict[str, Any]:
    expected = {item["id"]: item for item in expected_manifest}
    paths = [raw_dir / f"{run_id}.npz" for run_id in sorted(expected)]
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise ValueError(f"missing expected traces: {missing}")
    if not paths:
        raise ValueError("the current run manifest contains no traces")
    included = []
    for path in paths:
        metadata, _ = load_trace(path)
        wanted = expected[metadata["id"]]
        if metadata["config_sha256"] != wanted["config_sha256"]:
            raise ValueError(f"stale config hash in {path}")
        if metadata["code_sha256"] != wanted["code_sha256"]:
            raise ValueError(f"stale code hash in {path}")
        included.append(
            {
                "run_id": metadata["id"],
                "path": str(path),
                "config_sha256": metadata["config_sha256"],
                "code_sha256": metadata["code_sha256"],
                "file_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    summaries = [summarize_trace(path, protocol) for path in paths]
    rows = _flatten_rows(summaries)
    horizon_rows = _horizon_rows(summaries)
    required_order_rows = _required_order_rows(
        summaries, [float(x) for x in protocol["accuracy_levels"]]
    )
    refinement_rows = _refinement_comparison(summaries)
    aggregates = _aggregate(rows)
    processed_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)
    _write_csv(processed_dir / "per_run.csv", rows)
    _write_csv(processed_dir / "errors_by_horizon.csv", horizon_rows)
    _write_csv(processed_dir / "required_order.csv", required_order_rows)
    _write_csv(processed_dir / "refinement.csv", refinement_rows)
    (processed_dir / "per_run.json").write_text(
        json.dumps(summaries, indent=2), encoding="utf-8"
    )
    (processed_dir / "aggregate.json").write_text(
        json.dumps(aggregates, indent=2), encoding="utf-8"
    )
    representative = next(
        (x for x in summaries if x["run_id"] == representative_id),
        summaries[0],
    )
    _plot_representative(representative, figures_dir)
    _plot_aggregate(rows, figures_dir)
    report = _build_report(
        summaries,
        rows,
        aggregates,
        horizon_rows,
        required_order_rows,
        refinement_rows,
        representative["run_id"],
    )
    report_path = processed_dir.parent.parent / "REPORT.md"
    report_path.write_text(report, encoding="utf-8")
    result = {
        "traces": len(paths),
        "per_run_rows": len(rows),
        "horizon_rows": len(horizon_rows),
        "required_order_rows": len(required_order_rows),
        "refinement_rows": len(refinement_rows),
        "representative_id": representative["run_id"],
        "report": str(report_path),
        "actual_compiled_liouville_pde_runs": 0,
        "protocol_sha256": hashlib.sha256(
            json.dumps(
                protocol, sort_keys=True, separators=(",", ":")
            ).encode("utf-8")
        ).hexdigest(),
        "included_traces": included,
    }
    (processed_dir / "analysis_manifest.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    return result
