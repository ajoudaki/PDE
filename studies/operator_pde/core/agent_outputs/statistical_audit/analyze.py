#!/usr/bin/env python3
"""Independent statistical audit of the operator-PDE numerical evidence.

The script reads, but never modifies, the solver/reference archives under
``dense_mup_pde_repro/results/raw`` and ``agent_outputs/numerics``.  It does
not fit, calibrate, or otherwise alter any PDE coefficient.  Its outputs are
plain CSV/JSON files intended to make every numerical comparison auditable.

One exact-network archive was interrupted before its ZIP central directory
was written.  When the system ``zip``/``unzip`` utilities are available, the
script salvages only CRC-valid complete ``.npy`` members into a temporary
directory.  The original archive is never changed.  The salvage status is
recorded in ``inventory.csv`` and the report.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dense_mup_pde_repro" / "results" / "raw"
NUM = ROOT / "agent_outputs" / "numerics"
OUT = Path(__file__).resolve().parent
Y3 = np.asarray([0.8, -0.55, 0.35], dtype=float)
Y2 = np.asarray([0.8, -0.55], dtype=float)
RNG_SEED = 24681357


@dataclass
class Archive:
    path: Path
    arrays: dict[str, np.ndarray]
    status: str
    note: str = ""
    metadata: dict[str, Any] | None = None

    @property
    def name(self) -> str:
        return self.path.name


def _scalar_text(array: np.ndarray) -> str:
    if array.shape == ():
        return str(array.item())
    return str(array)


def _load_valid_npz(path: Path) -> Archive:
    with np.load(path, allow_pickle=False) as data:
        arrays = {key: data[key].copy() for key in data.files}
    metadata: dict[str, Any] | None = None
    if "metadata_json" in arrays:
        metadata = json.loads(_scalar_text(arrays["metadata_json"]))
    return Archive(path=path, arrays=arrays, status="valid", metadata=metadata)


def _salvage_npz(path: Path) -> Archive:
    """Read only complete members from a truncated NPZ, without mutation."""

    with tempfile.TemporaryDirectory(prefix="pde_stat_audit_") as tmp:
        tmp_path = Path(tmp)
        repaired = tmp_path / "repaired.npz"
        proc = subprocess.run(
            ["zip", "-FF", str(path), "--out", str(repaired)],
            input="y\n",
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if proc.returncode != 0 or not repaired.exists():
            raise OSError(f"zip salvage failed: {proc.stdout[-500:]}")
        extract = tmp_path / "members"
        extract.mkdir()
        proc2 = subprocess.run(
            ["unzip", "-q", str(repaired), "-d", str(extract)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if proc2.returncode != 0:
            raise OSError(f"unzip salvage failed: {proc2.stdout[-500:]}")
        arrays = {
            member.stem: np.load(member, allow_pickle=False).copy()
            for member in sorted(extract.glob("*.npy"))
        }
    if not arrays:
        raise OSError("no complete NPY members recovered")
    return Archive(
        path=path,
        arrays=arrays,
        status="salvaged_complete_members",
        note=(
            "Original NPZ lacks a central directory; complete CRC-valid NPY "
            f"members recovered read-only: {','.join(sorted(arrays))}"
        ),
        metadata=None,
    )


def load_archive(path: Path) -> Archive:
    try:
        return _load_valid_npz(path)
    except Exception as first_error:  # noqa: BLE001 - audit must record damage
        try:
            archive = _salvage_npz(path)
            archive.note += f"; direct load error: {type(first_error).__name__}"
            return archive
        except Exception as second_error:  # noqa: BLE001
            return Archive(
                path=path,
                arrays={},
                status="unreadable",
                note=(
                    f"direct={type(first_error).__name__}: {first_error}; "
                    f"salvage={type(second_error).__name__}: {second_error}"
                ),
            )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(2**20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def finite_float(value: Any) -> float | str:
    if value is None:
        return ""
    result = float(value)
    if not np.isfinite(result):
        return ""
    return result


def get_time(archive: Archive) -> np.ndarray:
    arrays = archive.arrays
    if "times" in arrays:
        return np.asarray(arrays["times"], dtype=float)
    return np.asarray(arrays["time"], dtype=float)


def get_curve(archive: Archive, key: str) -> np.ndarray | None:
    arrays = archive.arrays
    if key in arrays:
        return np.asarray(arrays[key], dtype=float)
    aliases = {"grams": "g", "f": "f"}
    alias = aliases.get(key)
    if alias and alias in arrays:
        return np.asarray(arrays[alias], dtype=float)
    return None


def metadata_from_name(archive: Archive) -> dict[str, Any]:
    """Fill only filename-declared fields; never infer scientific values."""

    meta = dict(archive.metadata or {})
    name = archive.name
    patterns = {
        "basis_size_P": r"(?:^|_)P(\d+)",
        "depth_nodes_N": r"(?:^|_)N(\d+)",
        "base_quadrature_M": r"(?:^|_)M(\d+)",
        "fast_quadrature_R": r"(?:^|_)R(\d+)",
        "quadrature_seed": r"(?:^|_)s(\d+)",
        "n": r"(?:^|_)n(\d+)",
        "depth": r"(?:^|_)L(\d+)",
        "seeds": r"(?:^|_)S(\d+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, name)
        if match and key not in meta:
            meta[key] = int(match.group(1))
    dt_match = re.search(r"_dt([0-9mp]+)", name)
    if dt_match and "dt" not in meta:
        meta["dt"] = float(dt_match.group(1).replace("m", "-").replace("p", "."))
    return meta


def inventory_row(archive: Archive) -> dict[str, Any]:
    meta = metadata_from_name(archive)
    arrays = archive.arrays
    time = None
    if arrays and ("times" in arrays or "time" in arrays):
        time = get_time(archive)
    return {
        "path": str(archive.path.relative_to(ROOT)),
        "filename": archive.name,
        "bytes": archive.path.stat().st_size,
        "sha256": sha256(archive.path),
        "load_status": archive.status,
        "note": archive.note,
        "keys": ";".join(sorted(arrays)),
        "time_points": "" if time is None else int(time.size),
        "time_start": "" if time is None else finite_float(time[0]),
        "time_end": "" if time is None else finite_float(time[-1]),
        "f_shape": "" if "f" not in arrays else "x".join(map(str, arrays["f"].shape)),
        "grams_shape": (
            "" if "grams" not in arrays else "x".join(map(str, arrays["grams"].shape))
        ),
        "theta_shape": (
            "" if "theta" not in arrays else "x".join(map(str, arrays["theta"].shape))
        ),
        "P": meta.get("basis_size_P", ""),
        "N_or_L": meta.get("depth_nodes_N", meta.get("depth", "")),
        "M": meta.get("base_quadrature_M", ""),
        "R": meta.get("fast_quadrature_R", ""),
        "quadrature_seed": meta.get("quadrature_seed", ""),
        "network_width_n": meta.get("n", ""),
        "ensemble_seeds_S": meta.get("seeds", ""),
        "dt": meta.get("dt", ""),
        "sample_dt": meta.get("sample_dt", ""),
        "quadrature": meta.get("quadrature", ""),
        "raw_basis_gram_error": meta.get("raw_basis_gram_error", ""),
        "whitened_basis_gram_error": meta.get(
            "whitened_basis_gram_error", ""
        ),
        "fast_mean_error": meta.get("fast_mean_error", ""),
        "fast_cov_error": meta.get("fast_cov_error", ""),
        "actual_width_independent_pde_run": meta.get(
            "actual_width_independent_pde_run", ""
        ),
        "contains_dense_network_weight_matrix": meta.get(
            "contains_dense_network_weight_matrix", ""
        ),
    }


def integrity_row(archive: Archive) -> dict[str, Any]:
    arrays = archive.arrays
    row: dict[str, Any] = {
        "filename": archive.name,
        "load_status": archive.status,
        "all_numeric_values_finite": True,
    }
    for key, value in arrays.items():
        if np.issubdtype(value.dtype, np.number):
            if not np.all(np.isfinite(value)):
                row["all_numeric_values_finite"] = False
                row.setdefault("nonfinite_arrays", "")
                row["nonfinite_arrays"] += f"{key};"
    for raw_key, stored_key in (
        ("f", "f_mean"),
        ("grams", "grams_mean"),
        ("theta", "theta_mean"),
    ):
        if raw_key in arrays and stored_key in arrays and arrays[raw_key].ndim == arrays[stored_key].ndim + 1:
            row[f"{stored_key}_recompute_max_abs"] = float(
                np.max(np.abs(np.mean(arrays[raw_key], axis=0) - arrays[stored_key]))
            )
    for raw_key, stored_key in (
        ("f", "f_sem"),
        ("grams", "grams_sem"),
        ("theta", "theta_sem"),
    ):
        if raw_key in arrays and stored_key in arrays and arrays[raw_key].ndim == arrays[stored_key].ndim + 1:
            recomputed = np.std(arrays[raw_key], axis=0, ddof=1) / np.sqrt(
                arrays[raw_key].shape[0]
            )
            row[f"{stored_key}_recompute_max_abs"] = float(
                np.max(np.abs(recomputed - arrays[stored_key]))
            )
    if "grams" in arrays:
        grams = np.asarray(arrays["grams"], dtype=float)
        row["gram_symmetry_max_abs"] = float(
            np.max(np.abs(grams - np.swapaxes(grams, -1, -2)))
        )
        row["gram_min_eigenvalue"] = float(
            np.min(np.linalg.eigvalsh(0.5 * (grams + np.swapaxes(grams, -1, -2))))
        )
    if "theta" in arrays:
        theta = np.asarray(arrays["theta"], dtype=float)
        symmetric = 0.5 * (theta + np.swapaxes(theta, -1, -2))
        row["theta_symmetry_max_abs"] = float(
            np.max(np.abs(theta - np.swapaxes(theta, -1, -2)))
        )
        eigenvalues = np.linalg.eigvalsh(symmetric)
        row["theta_min_eigenvalue_recomputed"] = float(np.min(eigenvalues))
        if "theta_min" in arrays:
            row["theta_min_stored_recompute_max_abs"] = float(
                np.max(np.abs(arrays["theta_min"] - eigenvalues[..., 0]))
            )
    if "f" in arrays and "loss" in arrays:
        f = np.asarray(arrays["f"], dtype=float)
        if f.ndim == 2:
            y = Y3 if f.shape[-1] == 3 else Y2
            expected_loss = 0.5 * np.sum((f - y[None, :]) ** 2, axis=-1)
            row["loss_identity_max_abs"] = float(
                np.max(np.abs(expected_loss - arrays["loss"]))
            )
            if "theta" in arrays and "loss_dot" in arrays:
                e = f - y[None, :]
                expected_dot = -np.einsum(
                    "ti,tij,tj->t", e, arrays["theta"], e, optimize=True
                )
                row["loss_dot_identity_max_abs"] = float(
                    np.max(np.abs(expected_dot - arrays["loss_dot"]))
                )
    if "projected_energy" in arrays:
        energy = np.asarray(arrays["projected_energy"], dtype=float)
        row["projected_energy_min"] = float(np.min(energy))
        row["projected_energy_max"] = float(np.max(energy))
        row["projected_energy_max_abs_from_one"] = float(
            np.max(np.abs(energy - 1.0))
        )
    return row


def interp_axis0(values: np.ndarray, old: np.ndarray, new: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    flat = values.reshape(values.shape[0], -1)
    out = np.empty((new.size, flat.shape[1]), dtype=float)
    for j in range(flat.shape[1]):
        out[:, j] = np.interp(new, old, flat[:, j])
    return out.reshape((new.size,) + values.shape[1:])


def align_time(
    left: Archive | Mapping[str, np.ndarray],
    right: Archive | Mapping[str, np.ndarray],
    key: str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray] | None:
    def time_of(item: Archive | Mapping[str, np.ndarray]) -> np.ndarray:
        if isinstance(item, Archive):
            return get_time(item)
        return np.asarray(item["times"], dtype=float)

    def curve_of(item: Archive | Mapping[str, np.ndarray]) -> np.ndarray | None:
        if isinstance(item, Archive):
            return get_curve(item, key)
        value = item.get(key)
        return None if value is None else np.asarray(value, dtype=float)

    tl, tr = time_of(left), time_of(right)
    vl, vr = curve_of(left), curve_of(right)
    if vl is None or vr is None:
        return None
    start, end = max(tl[0], tr[0]), min(tl[-1], tr[-1])
    if end < start:
        return None
    dl = np.median(np.diff(tl)) if tl.size > 1 else math.inf
    dr = np.median(np.diff(tr)) if tr.size > 1 else math.inf
    step = min(dl, dr)
    if not np.isfinite(step) or step <= 0:
        grid = np.asarray([start])
    else:
        count = int(round((end - start) / step))
        grid = np.linspace(start, end, count + 1)
    return grid, interp_axis0(vl, tl, grid), interp_axis0(vr, tr, grid)


def interp_depth(grams: np.ndarray, points: int) -> np.ndarray:
    grams = np.asarray(grams, dtype=float)
    old = np.linspace(0.0, 1.0, grams.shape[1])
    new = np.linspace(0.0, 1.0, points)
    swapped = np.swapaxes(grams, 0, 1)
    flat = swapped.reshape(swapped.shape[0], -1)
    out = np.empty((points, flat.shape[1]), dtype=float)
    for j in range(flat.shape[1]):
        out[:, j] = np.interp(new, old, flat[:, j])
    return np.swapaxes(
        out.reshape((points,) + swapped.shape[1:]), 0, 1
    )


def curve_metrics(
    left: Archive | Mapping[str, np.ndarray],
    right: Archive | Mapping[str, np.ndarray],
    depth_points: int = 257,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    f_pair = align_time(left, right, "f")
    if f_pair is not None:
        grid, lf, rf = f_pair
        delta = lf - rf
        norms = np.linalg.norm(delta, axis=-1)
        centered = (lf - lf[0]) - (rf - rf[0])
        centered_norms = np.linalg.norm(centered, axis=-1)
        max_index = int(np.argmax(norms))
        result.update(
            {
                "overlap_start": float(grid[0]),
                "overlap_end": float(grid[-1]),
                "time_points_compared": int(grid.size),
                "output_max_l2": float(np.max(norms)),
                "output_rms_l2": float(np.sqrt(np.mean(norms**2))),
                "output_terminal_l2": float(norms[-1]),
                "output_max_abs_component": float(np.max(np.abs(delta))),
                "output_initial_l2": float(norms[0]),
                "output_time_of_max_l2": float(grid[max_index]),
                "output_initial_centered_max_l2": float(
                    np.max(centered_norms)
                ),
                "output_initial_centered_rms_l2": float(
                    np.sqrt(np.mean(centered_norms**2))
                ),
                "output_initial_centered_terminal_l2": float(
                    centered_norms[-1]
                ),
            }
        )
    loss_pair = align_time(left, right, "loss")
    if loss_pair is not None:
        _, ll, rl = loss_pair
        diff = np.abs(ll - rl)
        result["loss_max_abs"] = float(np.max(diff))
        result["loss_terminal_abs"] = float(diff[-1])
    grams_pair = align_time(left, right, "grams")
    if grams_pair is not None:
        ggrid, lg, rg = grams_pair
        if lg.shape[1] != rg.shape[1]:
            lg = interp_depth(lg, depth_points)
            rg = interp_depth(rg, depth_points)
            result["depth_interpolated"] = True
            result["depth_points_compared"] = depth_points
        else:
            result["depth_interpolated"] = False
            result["depth_points_compared"] = int(lg.shape[1])
        delta = lg - rg
        norms = np.linalg.norm(delta, axis=(-2, -1))
        centered = (lg - lg[0]) - (rg - rg[0])
        centered_norms = np.linalg.norm(centered, axis=(-2, -1))
        max_flat = int(np.argmax(norms))
        max_time_index, max_depth_index = np.unravel_index(
            max_flat, norms.shape
        )
        result.update(
            {
                "gram_max_fro": float(np.max(norms)),
                "gram_rms_fro": float(np.sqrt(np.mean(norms**2))),
                "gram_terminal_max_fro": float(np.max(norms[-1])),
                "gram_max_abs_entry": float(np.max(np.abs(delta))),
                "gram_initial_max_fro": float(np.max(norms[0])),
                "gram_time_of_max_fro": float(
                    ggrid[max_time_index]
                ),
                "gram_depth_fraction_of_max_fro": float(
                    max_depth_index / (norms.shape[1] - 1)
                    if norms.shape[1] > 1
                    else 0.0
                ),
                "gram_initial_centered_max_fro": float(
                    np.max(centered_norms)
                ),
                "gram_initial_centered_rms_fro": float(
                    np.sqrt(np.mean(centered_norms**2))
                ),
                "gram_initial_centered_terminal_max_fro": float(
                    np.max(centered_norms[-1])
                ),
            }
        )
    theta_pair = align_time(left, right, "theta")
    if theta_pair is not None:
        _, lt, rt = theta_pair
        delta = lt - rt
        norms = np.linalg.norm(delta, axis=(-2, -1))
        centered = (lt - lt[0]) - (rt - rt[0])
        centered_norms = np.linalg.norm(centered, axis=(-2, -1))
        result.update(
            {
                "theta_max_fro": float(np.max(norms)),
                "theta_rms_fro": float(np.sqrt(np.mean(norms**2))),
                "theta_terminal_fro": float(norms[-1]),
                "theta_max_abs_entry": float(np.max(np.abs(delta))),
                "theta_initial_fro": float(norms[0]),
                "theta_initial_centered_max_fro": float(
                    np.max(centered_norms)
                ),
                "theta_initial_centered_terminal_fro": float(
                    centered_norms[-1]
                ),
            }
        )
    return result


def mean_sem_archive(
    name: str,
    times: np.ndarray,
    f: np.ndarray,
    grams: np.ndarray,
    theta: np.ndarray | None = None,
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
    mean: dict[str, np.ndarray] = {
        "times": np.asarray(times, dtype=float),
        "f": np.mean(f, axis=0),
        "grams": np.mean(grams, axis=0),
    }
    sem: dict[str, np.ndarray] = {
        "times": np.asarray(times, dtype=float),
        "f": np.std(f, axis=0, ddof=1) / np.sqrt(f.shape[0]),
        "grams": np.std(grams, axis=0, ddof=1) / np.sqrt(grams.shape[0]),
    }
    if theta is not None:
        mean["theta"] = np.mean(theta, axis=0)
        sem["theta"] = np.std(theta, axis=0, ddof=1) / np.sqrt(theta.shape[0])
    mean["name"] = np.asarray(name)
    sem["name"] = np.asarray(name)
    return mean, sem


def reference_from_m3(archive: Archive) -> dict[str, Any]:
    arrays = archive.arrays
    meta = metadata_from_name(archive)
    f = np.asarray(arrays["f"], dtype=float)
    grams = np.asarray(arrays["grams"], dtype=float)
    theta = np.asarray(arrays["theta"], dtype=float)
    mean, sem = mean_sem_archive(
        archive.name, get_time(archive), f, grams, theta
    )
    mean["loss"] = 0.5 * np.sum((mean["f"] - Y3[None, :]) ** 2, axis=-1)
    # Stored means/SEMs are cross-checked rather than trusted silently.
    stored_defects: dict[str, float] = {}
    for key, calculated in (
        ("f_mean", mean["f"]),
        ("f_sem", sem["f"]),
        ("grams_mean", mean["grams"]),
        ("grams_sem", sem["grams"]),
        ("theta_mean", mean["theta"]),
        ("theta_sem", sem["theta"]),
    ):
        if key in arrays:
            stored_defects[key] = float(
                np.max(np.abs(np.asarray(arrays[key]) - calculated))
            )
    return {
        "name": archive.name,
        "archive": archive,
        "n": int(meta["n"]),
        "depth": int(meta["depth"]),
        "S": int(meta["seeds"]),
        "mean": mean,
        "sem": sem,
        "raw_f": f,
        "raw_grams": grams,
        "raw_theta": theta,
        "stored_defects": stored_defects,
        "status": archive.status,
    }


def reference_from_m2(
    archive: Archive, width: int, sample_count: int | None
) -> dict[str, Any]:
    arrays = archive.arrays
    mean = {
        "times": np.asarray(arrays["time"], dtype=float),
        "f": np.asarray(arrays[f"f_mean_n{width}"], dtype=float),
        "grams": np.asarray(arrays[f"g_mean_n{width}"], dtype=float),
        "name": np.asarray(f"{archive.name}:n{width}"),
    }
    mean["loss"] = 0.5 * np.sum((mean["f"] - Y2[None, :]) ** 2, axis=-1)
    sem = {
        "times": mean["times"],
        "f": np.asarray(arrays[f"f_se_n{width}"], dtype=float),
        "grams": np.asarray(arrays[f"g_se_n{width}"], dtype=float),
        "name": np.asarray(f"{archive.name}:n{width}"),
    }
    return {
        "name": f"{archive.name}:n{width}",
        "archive": archive,
        "n": width,
        "depth": 16,
        "S": sample_count,
        "mean": mean,
        "sem": sem,
        "status": archive.status,
    }


def pool_m3_references(
    name: str, references: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    """Pool independent exact-network ensembles with identical (n,L)."""

    if not references:
        raise ValueError("cannot pool an empty reference list")
    first = references[0]
    for ref in references[1:]:
        if (ref["n"], ref["depth"]) != (first["n"], first["depth"]):
            raise ValueError("pooled references must have identical n and L")
        if not np.array_equal(
            ref["mean"]["times"], first["mean"]["times"]
        ):
            raise ValueError("pooled references must share a time grid")
    raw_f = np.concatenate([ref["raw_f"] for ref in references], axis=0)
    raw_grams = np.concatenate(
        [ref["raw_grams"] for ref in references], axis=0
    )
    raw_theta = np.concatenate(
        [ref["raw_theta"] for ref in references], axis=0
    )
    mean, sem = mean_sem_archive(
        name,
        np.asarray(first["mean"]["times"]),
        raw_f,
        raw_grams,
        raw_theta,
    )
    mean["loss"] = 0.5 * np.sum((mean["f"] - Y3[None, :]) ** 2, axis=-1)
    return {
        "name": name,
        "archive": None,
        "n": int(first["n"]),
        "depth": int(first["depth"]),
        "S": int(raw_f.shape[0]),
        "mean": mean,
        "sem": sem,
        "raw_f": raw_f,
        "raw_grams": raw_grams,
        "raw_theta": raw_theta,
        "stored_defects": {},
        "status": "pooled_independent_archives",
        "members": ";".join(ref["name"] for ref in references),
    }


def sem_summary(ref: Mapping[str, Any]) -> dict[str, Any]:
    sem = ref["sem"]
    row: dict[str, Any] = {
        "reference": ref["name"],
        "m": int(sem["f"].shape[-1]),
        "network_width_n": ref["n"],
        "depth_L": ref["depth"],
        "ensemble_size_S": "" if ref["S"] is None else ref["S"],
        "archive_status": ref["status"],
        "members": ref.get("members", ""),
    }
    f_sem_norm = np.linalg.norm(sem["f"], axis=-1)
    g_sem_fro = np.linalg.norm(sem["grams"], axis=(-2, -1))
    row.update(
        {
            "output_sem_norm_max": float(np.max(f_sem_norm)),
            "output_sem_norm_rms": float(np.sqrt(np.mean(f_sem_norm**2))),
            "output_sem_norm_terminal": float(f_sem_norm[-1]),
            "gram_sem_fro_max": float(np.max(g_sem_fro)),
            "gram_sem_fro_rms": float(np.sqrt(np.mean(g_sem_fro**2))),
            "gram_sem_fro_terminal_max": float(np.max(g_sem_fro[-1])),
        }
    )
    if "theta" in sem:
        t_sem_fro = np.linalg.norm(sem["theta"], axis=(-2, -1))
        row.update(
            {
                "theta_sem_fro_max": float(np.max(t_sem_fro)),
                "theta_sem_fro_rms": float(np.sqrt(np.mean(t_sem_fro**2))),
                "theta_sem_fro_terminal": float(t_sem_fro[-1]),
            }
        )
    return row


def _multinomial_bootstrap_sup(
    raw: np.ndarray,
    norm_axes: tuple[int, ...],
    replicates: int = 500,
) -> np.ndarray:
    """Bootstrap sup-norm uncertainty of an ensemble mean curve."""

    rng = np.random.default_rng(RNG_SEED + raw.shape[0] + raw.ndim)
    samples = raw.shape[0]
    full = np.mean(raw, axis=0)
    flat = raw.reshape(samples, -1)
    result = np.empty(replicates, dtype=float)
    batch = 25
    for start in range(0, replicates, batch):
        stop = min(replicates, start + batch)
        counts = rng.multinomial(
            samples, np.full(samples, 1.0 / samples), size=stop - start
        )
        boot = (counts @ flat / samples).reshape(
            (stop - start,) + full.shape
        )
        delta = boot - full
        norms = np.linalg.norm(delta, axis=norm_axes)
        result[start:stop] = np.max(norms.reshape(stop - start, -1), axis=1)
    return result


def _bootstrap_loss_of_mean_sup(
    raw_f: np.ndarray,
    y: np.ndarray,
    replicates: int = 500,
) -> np.ndarray:
    rng = np.random.default_rng(RNG_SEED + 7919 + raw_f.shape[0])
    samples = raw_f.shape[0]
    full_mean = np.mean(raw_f, axis=0)
    full_loss = 0.5 * np.sum((full_mean - y[None, :]) ** 2, axis=-1)
    flat = raw_f.reshape(samples, -1)
    result = np.empty(replicates, dtype=float)
    for index in range(replicates):
        counts = rng.multinomial(
            samples, np.full(samples, 1.0 / samples)
        )
        boot_mean = (counts @ flat / samples).reshape(full_mean.shape)
        boot_loss = 0.5 * np.sum(
            (boot_mean - y[None, :]) ** 2, axis=-1
        )
        result[index] = float(np.max(np.abs(boot_loss - full_loss)))
    return result


def bootstrap_thresholds(ref: Mapping[str, Any]) -> dict[str, float]:
    if "raw_f" not in ref:
        return {}
    f_sup = _multinomial_bootstrap_sup(
        np.asarray(ref["raw_f"]), norm_axes=(-1,)
    )
    g_sup = _multinomial_bootstrap_sup(
        np.asarray(ref["raw_grams"]), norm_axes=(-2, -1)
    )
    g_increment_sup = _multinomial_bootstrap_sup(
        np.asarray(ref["raw_grams"])
        - np.asarray(ref["raw_grams"])[:, 0:1],
        norm_axes=(-2, -1),
    )
    t_sup = _multinomial_bootstrap_sup(
        np.asarray(ref["raw_theta"]), norm_axes=(-2, -1)
    )
    loss_sup = _bootstrap_loss_of_mean_sup(
        np.asarray(ref["raw_f"]), Y3, replicates=f_sup.size
    )
    return {
        "bootstrap_replicates": int(f_sup.size),
        "output_mean_sup_bootstrap_p95": float(np.quantile(f_sup, 0.95)),
        "gram_mean_sup_bootstrap_p95": float(np.quantile(g_sup, 0.95)),
        "gram_increment_mean_sup_bootstrap_p95": float(
            np.quantile(g_increment_sup, 0.95)
        ),
        "theta_mean_sup_bootstrap_p95": float(np.quantile(t_sup, 0.95)),
        "loss_of_mean_sup_bootstrap_p95": float(
            np.quantile(loss_sup, 0.95)
        ),
    }


def standardized_comparison(
    left_mean: Mapping[str, np.ndarray],
    right_mean: Mapping[str, np.ndarray],
    combined_sem: Mapping[str, np.ndarray],
    y: np.ndarray,
) -> dict[str, Any]:
    """Componentwise SEM scaling; intentionally not called a global p-value."""

    result: dict[str, Any] = {}
    f_pair = align_time(left_mean, right_mean, "f")
    fs_pair = align_time(combined_sem, combined_sem, "f")
    if f_pair is not None and fs_pair is not None:
        _, left, right = f_pair
        _, se, _ = fs_pair
        active = np.linalg.norm(right - y[None, :], axis=-1) > 1e-4
        valid = (se > 1e-12) & active[:, None]
        z = np.divide(
            np.abs(left - right),
            se,
            out=np.full_like(left, np.nan),
            where=valid,
        )
        result.update(
            {
                "output_active_points": int(np.sum(valid)),
                "output_active_max_abs_z": (
                    float(np.nanmax(z)) if np.any(valid) else ""
                ),
                "output_active_rms_z": (
                    float(np.sqrt(np.nanmean(z**2))) if np.any(valid) else ""
                ),
                "output_active_fraction_within_1p96_sem": (
                    float(np.mean(z[valid] <= 1.96)) if np.any(valid) else ""
                ),
            }
        )
    g_pair = align_time(left_mean, right_mean, "grams")
    gs_pair = align_time(combined_sem, combined_sem, "grams")
    if g_pair is not None and gs_pair is not None:
        _, left, right = g_pair
        _, se, _ = gs_pair
        if left.shape[1] != right.shape[1]:
            points = 257
            left, right = interp_depth(left, points), interp_depth(right, points)
            se = interp_depth(se, points)
        m = left.shape[-1]
        tri = np.triu_indices(m)
        delta = np.abs(
            (left - right)[..., tri[0], tri[1]]
        )
        gse = se[..., tri[0], tri[1]]
        valid = gse > 1e-12
        z = np.divide(
            delta,
            gse,
            out=np.full_like(delta, np.nan),
            where=valid,
        )
        result.update(
            {
                "gram_unique_points": int(np.sum(valid)),
                "gram_max_abs_z": float(np.nanmax(z)),
                "gram_rms_z": float(np.sqrt(np.nanmean(z**2))),
                "gram_fraction_within_1p96_sem": float(
                    np.mean(z[valid] <= 1.96)
                ),
            }
        )
    return result


def combine_sem(
    left: Mapping[str, np.ndarray], right: Mapping[str, np.ndarray]
) -> dict[str, np.ndarray]:
    result: dict[str, np.ndarray] = {
        "times": np.asarray(left["times"], dtype=float)
    }
    for key in ("f", "grams", "theta"):
        if key not in left or key not in right:
            continue
        if not np.array_equal(left["times"], right["times"]):
            pair = align_time(left, right, key)
            if pair is None:
                continue
            grid, lv, rv = pair
            result["times"] = grid
            if key == "grams" and lv.shape[1] != rv.shape[1]:
                lv, rv = interp_depth(lv, 257), interp_depth(rv, 257)
            result[key] = np.sqrt(lv**2 + rv**2)
        else:
            lv, rv = left[key], right[key]
            if key == "grams" and lv.shape[1] != rv.shape[1]:
                lv, rv = interp_depth(lv, 257), interp_depth(rv, 257)
            result[key] = np.sqrt(lv**2 + rv**2)
    return result


def zero_sem_like(mean: Mapping[str, np.ndarray]) -> dict[str, np.ndarray]:
    result = {"times": np.asarray(mean["times"], dtype=float)}
    for key in ("f", "grams", "theta"):
        if key in mean:
            result[key] = np.zeros_like(mean[key])
    return result


def exact_difference_row(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
    comparison_type: str,
) -> dict[str, Any]:
    row = {
        "comparison_type": comparison_type,
        "left": left["name"],
        "right": right["name"],
        "left_n": left["n"],
        "right_n": right["n"],
        "left_L": left["depth"],
        "right_L": right["depth"],
        "left_S": "" if left["S"] is None else left["S"],
        "right_S": "" if right["S"] is None else right["S"],
    }
    row.update(curve_metrics(left["mean"], right["mean"]))
    combined = combine_sem(left["sem"], right["sem"])
    row.update(
        standardized_comparison(left["mean"], right["mean"], combined, Y3 if left["mean"]["f"].shape[-1] == 3 else Y2)
    )
    return row


def qmc_group(
    group_name: str, archives: Sequence[Archive]
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], dict[str, Any]]:
    times = get_time(archives[0])
    end = min(get_time(a)[-1] for a in archives)
    mask = times <= end + 1e-12
    times = times[mask]
    stack: dict[str, list[np.ndarray]] = {key: [] for key in ("f", "loss", "grams", "theta")}
    for archive in archives:
        for key in stack:
            pair = align_time(
                {"times": times, key: np.zeros((times.size,) + get_curve(archive, key).shape[1:])},
                archive,
                key,
            )
            if pair is None:
                continue
            _, _, values = pair
            stack[key].append(values)
    mean: dict[str, np.ndarray] = {"times": times, "name": np.asarray(group_name)}
    sem: dict[str, np.ndarray] = {"times": times, "name": np.asarray(group_name)}
    summary: dict[str, Any] = {
        "group": group_name,
        "replicates": len(archives),
        "members": ";".join(a.name for a in archives),
    }
    for key, members in stack.items():
        if not members:
            continue
        values = np.stack(members)
        mean[key] = np.mean(values, axis=0)
        sem[key] = np.std(values, axis=0, ddof=1) / np.sqrt(values.shape[0])
        if key == "f":
            sem_norm = np.linalg.norm(sem[key], axis=-1)
            summary["output_qmc_sem_norm_max"] = float(np.max(sem_norm))
            summary["output_qmc_sem_norm_rms"] = float(
                np.sqrt(np.mean(sem_norm**2))
            )
        elif key == "grams":
            sem_norm = np.linalg.norm(sem[key], axis=(-2, -1))
            summary["gram_qmc_sem_fro_max"] = float(np.max(sem_norm))
            summary["gram_qmc_sem_fro_rms"] = float(
                np.sqrt(np.mean(sem_norm**2))
            )
        elif key == "theta":
            sem_norm = np.linalg.norm(sem[key], axis=(-2, -1))
            summary["theta_qmc_sem_fro_max"] = float(np.max(sem_norm))
            summary["theta_qmc_sem_fro_rms"] = float(
                np.sqrt(np.mean(sem_norm**2))
            )
    pair_metrics = [
        curve_metrics(archives[i], archives[j])
        for i in range(len(archives))
        for j in range(i + 1, len(archives))
    ]
    for metric in (
        "output_max_l2",
        "gram_max_fro",
        "theta_max_fro",
        "output_terminal_l2",
        "gram_terminal_max_fro",
    ):
        values = [float(row[metric]) for row in pair_metrics if metric in row]
        if values:
            summary[f"pairwise_{metric}_max"] = max(values)
            summary[f"pairwise_{metric}_median"] = float(np.median(values))
    return mean, sem, summary


def plateau_metrics(
    name: str,
    curve: Mapping[str, np.ndarray],
    y: np.ndarray,
    tail_start: float,
    member_arrays: Mapping[str, np.ndarray] | None = None,
) -> dict[str, Any]:
    times = np.asarray(curve["times"], dtype=float)
    if tail_start < times[0] or tail_start >= times[-1]:
        raise ValueError(f"tail start {tail_start} outside {name}")
    start_index = int(np.searchsorted(times, tail_start, side="left"))
    row: dict[str, Any] = {
        "curve": name,
        "time_start": float(times[0]),
        "tail_start": float(times[start_index]),
        "time_end": float(times[-1]),
    }
    f = np.asarray(curve["f"], dtype=float)
    f_tail = f[start_index:] - f[start_index]
    f_norm = np.linalg.norm(f_tail, axis=-1)
    increments = np.linalg.norm(np.diff(f[start_index:], axis=0), axis=-1)
    total_f_motion = float(np.max(np.linalg.norm(f - f[0], axis=-1)))
    row.update(
        {
            "tail_output_max_drift_l2": float(np.max(f_norm)),
            "tail_output_terminal_drift_l2": float(f_norm[-1]),
            "tail_output_path_length_l2": float(np.sum(increments)),
            "tail_start_residual_l2": float(np.linalg.norm(f[start_index] - y)),
            "tail_end_residual_l2": float(np.linalg.norm(f[-1] - y)),
            "total_output_motion_max_l2": total_f_motion,
            "tail_output_drift_fraction_total": (
                float(np.max(f_norm) / total_f_motion)
                if total_f_motion > 0
                else 0.0
            ),
        }
    )
    if "loss" in curve:
        loss = np.asarray(curve["loss"], dtype=float)
    else:
        loss = 0.5 * np.sum((f - y[None, :]) ** 2, axis=-1)
    row.update(
        {
            "tail_start_loss": float(loss[start_index]),
            "tail_end_loss": float(loss[-1]),
            "tail_loss_max_abs_change": float(
                np.max(np.abs(loss[start_index:] - loss[start_index]))
            ),
        }
    )
    if "grams" in curve:
        grams = np.asarray(curve["grams"], dtype=float)
        g_delta = grams[start_index:] - grams[start_index]
        g_norm = np.linalg.norm(g_delta, axis=(-2, -1))
        g_inc = np.linalg.norm(
            np.diff(grams[start_index:], axis=0), axis=(-2, -1)
        )
        total_g = np.linalg.norm(grams - grams[0], axis=(-2, -1))
        total_g_motion = float(np.max(total_g))
        tail_max = float(np.max(g_norm))
        row.update(
            {
                "tail_gram_max_drift_fro": tail_max,
                "tail_gram_terminal_max_drift_fro": float(
                    np.max(g_norm[-1])
                ),
                "tail_gram_path_length_sum_maxdepth": float(
                    np.sum(np.max(g_inc, axis=1))
                ),
                "total_gram_motion_max_fro": total_g_motion,
                "tail_gram_drift_fraction_total": (
                    tail_max / total_g_motion if total_g_motion > 0 else 0.0
                ),
            }
        )
    if member_arrays is not None and "f" in member_arrays:
        member_f = np.asarray(member_arrays["f"], dtype=float)
        drift = np.linalg.norm(
            member_f[:, -1] - member_f[:, start_index], axis=-1
        )
        row["member_terminal_output_drift_mean"] = float(np.mean(drift))
        row["member_terminal_output_drift_sem"] = float(
            np.std(drift, ddof=1) / np.sqrt(drift.size)
        )
        row["member_terminal_output_drift_max"] = float(np.max(drift))
    if member_arrays is not None and "grams" in member_arrays:
        member_g = np.asarray(member_arrays["grams"], dtype=float)
        drift = np.max(
            np.linalg.norm(
                member_g[:, -1] - member_g[:, start_index],
                axis=(-2, -1),
            ),
            axis=-1,
        )
        row["member_terminal_gram_drift_mean"] = float(np.mean(drift))
        row["member_terminal_gram_drift_sem"] = float(
            np.std(drift, ddof=1) / np.sqrt(drift.size)
        )
        row["member_terminal_gram_drift_max"] = float(np.max(drift))
    return row


def concatenate_curves(first: Archive, second: Archive, name: str) -> dict[str, np.ndarray]:
    result: dict[str, np.ndarray] = {"name": np.asarray(name)}
    t1, t2 = get_time(first), get_time(second)
    start = 1 if np.isclose(t1[-1], t2[0]) else 0
    result["times"] = np.concatenate([t1, t2[start:]])
    for key in ("f", "loss", "grams", "theta"):
        a, b = get_curve(first, key), get_curve(second, key)
        if a is not None and b is not None:
            result[key] = np.concatenate([a, b[start:]], axis=0)
    return result


def archive_curve(archive: Archive) -> dict[str, np.ndarray]:
    result: dict[str, np.ndarray] = {
        "times": get_time(archive),
        "name": np.asarray(archive.name),
    }
    for key in ("f", "loss", "grams", "theta"):
        value = get_curve(archive, key)
        if value is not None:
            result[key] = value
    return result


def add_pair(
    rows: list[dict[str, Any]],
    category: str,
    isolated_axis: str,
    left: Archive,
    right: Archive,
    note: str = "",
) -> None:
    row: dict[str, Any] = {
        "category": category,
        "isolated_axis": isolated_axis,
        "left": left.name,
        "right": right.name,
        "note": note,
    }
    row.update(curve_metrics(left, right))
    rows.append(row)


def reference_discrepancy_row(
    pde_name: str,
    pde_mean: Mapping[str, np.ndarray],
    pde_sem: Mapping[str, np.ndarray],
    pde_replicates: int,
    ref: Mapping[str, Any],
    bootstrap: Mapping[str, float],
    note: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "pde": pde_name,
        "reference": ref["name"],
        "pde_replicates": pde_replicates,
        "reference_n": ref["n"],
        "reference_L": ref["depth"],
        "reference_S": "" if ref["S"] is None else ref["S"],
        "note": note,
    }
    metrics = curve_metrics(pde_mean, ref["mean"])
    row.update(metrics)
    grams_pair = align_time(pde_mean, ref["mean"], "grams")
    if grams_pair is not None:
        _, pde_grams, ref_grams = grams_pair
        if pde_grams.shape[1] != ref_grams.shape[1]:
            pde_grams = interp_depth(pde_grams, 257)
            ref_grams = interp_depth(ref_grams, 257)
        pde_increment = pde_grams - pde_grams[0:1]
        ref_increment = ref_grams - ref_grams[0:1]
        pde_motion = float(
            np.max(np.linalg.norm(pde_increment[-1], axis=(-2, -1)))
        )
        ref_motion = float(
            np.max(np.linalg.norm(ref_increment[-1], axis=(-2, -1)))
        )
        row["pde_terminal_feature_motion_max_fro"] = pde_motion
        row["reference_terminal_feature_motion_max_fro"] = ref_motion
        if pde_motion > 0 and "gram_initial_centered_max_fro" in metrics:
            row["gram_increment_gap_fraction_pde_feature_motion"] = float(
                metrics["gram_initial_centered_max_fro"] / pde_motion
            )
    # Align SEMs to the comparison grid.  All central comparisons currently
    # share the same sample grid, but the generic path avoids hidden reliance.
    combined = combine_sem(pde_sem, ref["sem"])
    row.update(
        standardized_comparison(
            pde_mean,
            ref["mean"],
            combined,
            Y3 if pde_mean["f"].shape[-1] == 3 else Y2,
        )
    )
    for key, value in bootstrap.items():
        row[key] = value
    if (
        "output_max_l2" in metrics
        and "output_mean_sup_bootstrap_p95" in bootstrap
    ):
        row["output_discrepancy_over_ref_bootstrap_p95"] = float(
            metrics["output_max_l2"]
            / bootstrap["output_mean_sup_bootstrap_p95"]
        )
    if "gram_max_fro" in metrics and "gram_mean_sup_bootstrap_p95" in bootstrap:
        row["gram_discrepancy_over_ref_bootstrap_p95"] = float(
            metrics["gram_max_fro"] / bootstrap["gram_mean_sup_bootstrap_p95"]
        )
    if (
        "gram_initial_centered_max_fro" in metrics
        and "gram_increment_mean_sup_bootstrap_p95" in bootstrap
    ):
        row["gram_increment_gap_over_ref_bootstrap_p95"] = float(
            metrics["gram_initial_centered_max_fro"]
            / bootstrap["gram_increment_mean_sup_bootstrap_p95"]
        )
    if (
        "loss_max_abs" in metrics
        and "loss_of_mean_sup_bootstrap_p95" in bootstrap
    ):
        row["loss_gap_over_ref_bootstrap_p95"] = float(
            metrics["loss_max_abs"]
            / bootstrap["loss_of_mean_sup_bootstrap_p95"]
        )
    return row


def fit_loglog_slope(
    x: np.ndarray, y: np.ndarray
) -> tuple[float, float, float]:
    lx, ly = np.log(x), np.log(y)
    design = np.column_stack([np.ones_like(lx), lx])
    coef, *_ = np.linalg.lstsq(design, ly, rcond=None)
    residual = ly - design @ coef
    dof = x.size - 2
    sigma2 = float(residual @ residual / dof)
    covariance = sigma2 * np.linalg.inv(design.T @ design)
    se = float(np.sqrt(covariance[1, 1]))
    # Four points only; use exact t_{.975,2}=4.3026527.
    critical = 4.302652729911275
    return float(coef[1]), se, critical * se


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_paths = sorted(RAW.glob("*.npz")) + sorted(NUM.glob("*.npz"))
    archives = {path.name: load_archive(path) for path in all_paths}
    inventory = [inventory_row(archive) for archive in archives.values()]
    write_csv(OUT / "inventory.csv", inventory)
    integrity_rows = [
        integrity_row(archive)
        for archive in archives.values()
        if archive.arrays
    ]
    write_csv(OUT / "data_integrity_checks.csv", integrity_rows)

    # ---------- PDE numerical convergence and independent solver checks ----------
    solver_rows: list[dict[str, Any]] = []
    p = archives
    explicit_pairs = [
        (
            "time_step",
            "dt",
            "pde_QMC_P5_N16_M64_R32_s20260723_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M64_R32_s20260723_dt0p01_T4.npz",
            "Same PDE/quadrature; RK4 dt 0.02 versus 0.01.",
        ),
        (
            "depth_grid",
            "N",
            "pde_QMC_P5_N8_M128_R64_s20260724_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M128_R64_s20260724_dt0p02_T4.npz",
            "Same P,M,R,QMC scramble; normalized-depth interpolation for Grams.",
        ),
        (
            "depth_grid",
            "N",
            "pde_QMC_P5_N16_M128_R64_s20260724_dt0p02_T4.npz",
            "pde_QMC_P5_N32_M128_R64_s20260724_dt0p02_T4.npz",
            "Same P,M,R,QMC scramble; normalized-depth interpolation for Grams.",
        ),
        (
            "operator_basis",
            "P",
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "pde_QMC_P15_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "Same N,M,R,QMC scramble; P=5 versus P=15.",
        ),
        (
            "operator_basis",
            "P",
            "pde_P5_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "pde_P15_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "Same N,M,R,QMC scramble under the earlier filename schema.",
        ),
        (
            "operator_basis_clean_hybrid",
            "P",
            "pde_HYBRID_P5_N16_M81_R128_s20260723_dt0p02_T8.npz",
            "pde_HYBRID_P15_N16_M81_R128_s20260723_dt0p02_T8.npz",
            "Clean nested hybrid basis step at fixed N,M,R and seed.",
        ),
        (
            "fast_quadrature_clean_hybrid",
            "R",
            "pde_HYBRID_P15_N16_M81_R128_s20260723_dt0p02_T8.npz",
            "pde_HYBRID_P15_N16_M81_R256_s20260723_dt0p02_T8.npz",
            "Clean hybrid P15 fast-cubature refinement at fixed N,M,P and seed.",
        ),
        (
            "operator_basis_and_base_quadrature",
            "P_and_M",
            "pde_HYBRID_P15_N16_M81_R128_s20260723_dt0p02_T8.npz",
            "pde_HYBRID_P35_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "P15 to complete-cubic P35 stress test; base cubature changes, so not a one-axis P refinement.",
        ),
        (
            "base_quadrature",
            "M",
            "pde_QMC_P5_N16_M64_R32_s20260723_dt0p02_T4.npz",
            "pde_P5_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "Same P,N,R,QMC scramble; M=64 versus M=128.",
        ),
        (
            "base_quadrature",
            "M",
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M512_R128_s20260723_dt0p02_T4.npz",
            "Same P,N,R,QMC scramble; isolated M=256 versus M=512.",
        ),
        (
            "fast_quadrature",
            "R",
            "pde_P5_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "Same P,N,M,QMC scramble; R=32 versus R=64.",
        ),
        (
            "fast_quadrature",
            "R",
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M256_R256_s20260723_dt0p02_T4.npz",
            "Same P,N,M,QMC scramble; isolated R=128 versus R=256.",
        ),
        (
            "fast_quadrature",
            "R",
            "pde_P15_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "pde_QMC_P15_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "Same P,N,M,QMC scramble; R=32 versus R=64.",
        ),
        (
            "coupled_quadrature",
            "M_and_R",
            "pde_QMC_P5_N16_M64_R32_s20260723_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "QMC M/R doubled together.",
        ),
        (
            "coupled_quadrature",
            "M_and_R",
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "QMC M/R doubled together.",
        ),
        (
            "quadrature_method",
            "method_M_R",
            "pde_GH_P5_N16_M81_R243_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "Independent tensor Gauss-Hermite versus scrambled-QMC cubature; resolutions differ.",
        ),
        (
            "implementation_crosscheck",
            "implementation_and_cubature",
            "operator_pde_m3_P5_N16_GH3_T1.npz",
            "pde_GH_P5_N16_M81_R243_s20260723_dt0p02_T8.npz",
            "Independent prototype/new implementation; same nominal P,N and GH3 fast rule, but old archive has no metadata.",
        ),
        (
            "m2_qmc_moment_matching",
            "whitening",
            "operator_pde_m2_deg1_L16_qmc256.npz",
            "operator_pde_m2_deg1_L16_qmc256_white.npz",
            "Same degree-one/QMC-256 pilot; moment matching toggled.",
        ),
        (
            "m2_qmc_moment_matching",
            "whitening",
            "operator_pde_m2_deg2_L16_qmc256.npz",
            "operator_pde_m2_deg2_L16_qmc256_white.npz",
            "Same degree-two/QMC-256 pilot; moment matching toggled.",
        ),
        (
            "m2_fast_quadrature",
            "R",
            "operator_pde_m2_deg1_L16_qmc256_white.npz",
            "operator_pde_m2_deg1_L16_qmc512_white.npz",
            "Moment-matched QMC-256 versus QMC-512.",
        ),
        (
            "m2_fast_quadrature",
            "R",
            "operator_pde_m2_deg2_L16_qmc256_white.npz",
            "operator_pde_m2_deg2_L16_qmc512_white.npz",
            "Moment-matched QMC-256 versus QMC-512.",
        ),
        (
            "m2_operator_basis",
            "P",
            "operator_pde_m2_deg1_L16_qmc512_white.npz",
            "operator_pde_m2_deg2_L16_qmc512_white.npz",
            "Same QMC-512 label; degree one (P=4) versus degree two (P=10).",
        ),
        (
            "m2_tensor_cubature",
            "base_order_inferred",
            "operator_pde_m2_P4_L16.npz",
            "operator_pde_m2_P4_L16_GH3_base4.npz",
            "Archive lacks metadata; current code/filename suggest base GH5 versus GH4 with fast GH3.",
        ),
        (
            "m2_tensor_cubature",
            "fast_GH_order",
            "operator_pde_m2_P4_L16_GH3_base4.npz",
            "operator_pde_m2_P4_L16_GH4.npz",
            "Filename-only method comparison; exact base order not serialized.",
        ),
        (
            "m2_tensor_cubature",
            "fast_GH_order",
            "operator_pde_m2_P4_L16_GH4.npz",
            "operator_pde_m2_P4_L16_GH5.npz",
            "Filename-only method comparison; exact base order not serialized.",
        ),
    ]
    for category, axis, left_name, right_name, note in explicit_pairs:
        if (
            left_name in p
            and right_name in p
            and p[left_name].arrays
            and p[right_name].arrays
        ):
            add_pair(
                solver_rows,
                category,
                axis,
                p[left_name],
                p[right_name],
                note,
            )
    write_csv(OUT / "pde_solver_convergence.csv", solver_rows)

    # ---------- Restart/semigroup checks ----------
    semigroup_rows: list[dict[str, Any]] = []
    direct = p.get("pde_QMC_P5_N8_M64_R16_s20260723_dt0p02_T2.npz")
    first = p.get("pde_P5_N8_M64_R16_s20260723_dt0p02_T1.npz")
    restart = p.get(
        "pde_QMC_P5_N8_M64_R16_s20260723_dt0p02_T1_from1_to2.npz"
    )
    if direct and first and restart:
        stitched = concatenate_curves(first, restart, "stitched_N8_T2")
        row = {
            "comparison": "direct_T2_vs_serialized_T1_plus_restart_T1",
            "direct": direct.name,
            "first": first.name,
            "restart": restart.name,
        }
        row.update(curve_metrics(archive_curve(direct), stitched))
        for key in ("final_B", "final_a", "final_c"):
            if key in direct.arrays and key in restart.arrays:
                row[f"{key}_max_abs"] = float(
                    np.max(np.abs(direct.arrays[key] - restart.arrays[key]))
                )
        semigroup_rows.append(row)
    small_first = p.get("pde_QMC_P5_N4_M32_R16_s4321_dt0p02_T0p2.npz")
    small_restart = p.get(
        "pde_QMC_P5_N4_M32_R16_s4321_dt0p02_T0p2_from0p2_to0p4.npz"
    )
    if small_first and small_restart:
        semigroup_rows.append(
            {
                "comparison": "serialized_restart_only_no_direct_T0p4_control",
                "direct": "",
                "first": small_first.name,
                "restart": small_restart.name,
                "note": "No direct 0-to-0.4 archive was present; this pair cannot quantify a semigroup defect.",
            }
        )
    write_csv(OUT / "semigroup_checks.csv", semigroup_rows)

    # ---------- Exact-network references ----------
    m3_refs: dict[str, dict[str, Any]] = {}
    exact_pattern = re.compile(
        r"^exact_ensemble_n\d+_L\d+_S\d+_seed\d+_dt"
    )
    for name, archive in sorted(p.items()):
        if (
            exact_pattern.match(name)
            and all(key in archive.arrays for key in ("f", "grams", "theta"))
        ):
            m3_refs[name] = reference_from_m3(archive)
    grouped_m3: dict[tuple[int, int], list[dict[str, Any]]] = {}
    for ref in m3_refs.values():
        grouped_m3.setdefault((ref["n"], ref["depth"]), []).append(ref)
    pooled_m3: dict[str, dict[str, Any]] = {}
    best_m3: dict[tuple[int, int], dict[str, Any]] = {}
    for (width, depth), refs in grouped_m3.items():
        if len(refs) > 1:
            pool_name = (
                f"pooled_exact_m3_n{width}_L{depth}_S"
                f"{sum(int(ref['S']) for ref in refs)}"
            )
            pooled = pool_m3_references(pool_name, refs)
            pooled_m3[pool_name] = pooled
            best_m3[(width, depth)] = pooled
        else:
            best_m3[(width, depth)] = refs[0]
    m2_large = p.get("exact_m2_L16_width_ensemble_large.npz")
    m2_refs: dict[int, dict[str, Any]] = {}
    if m2_large and m2_large.arrays:
        # Counts are explicit defaults in the adjacent generator source.
        for width, count in ((64, 128), (128, 96), (256, 48)):
            m2_refs[width] = reference_from_m2(m2_large, width, count)

    all_m3_refs = {**m3_refs, **pooled_m3}
    bootstrap: dict[str, dict[str, float]] = {
        name: bootstrap_thresholds(ref) for name, ref in all_m3_refs.items()
    }
    uncertainty_rows = [
        {**sem_summary(ref), **bootstrap.get(name, {})}
        for name, ref in all_m3_refs.items()
    ] + [sem_summary(ref) for ref in m2_refs.values()]
    write_csv(OUT / "exact_ensemble_uncertainty.csv", uncertainty_rows)

    exact_difference_rows: list[dict[str, Any]] = []
    # Independent ensemble replication at identical architecture.
    for refs in grouped_m3.values():
        if len(refs) > 1:
            for i in range(len(refs)):
                for j in range(i + 1, len(refs)):
                    exact_difference_rows.append(
                        exact_difference_row(
                            refs[i],
                            refs[j],
                            "independent_ensemble_replication",
                        )
                    )
    # Width checks at fixed depth, using pooled references where available.
    depths = sorted({depth for _, depth in best_m3})
    for depth in depths:
        widths = sorted(
            width for width, candidate_depth in best_m3
            if candidate_depth == depth
        )
        for left_width, right_width in zip(widths[:-1], widths[1:]):
            exact_difference_rows.append(
                exact_difference_row(
                    best_m3[(left_width, depth)],
                    best_m3[(right_width, depth)],
                    f"width_at_fixed_L{depth}",
                )
            )
        if len(widths) >= 3:
            exact_difference_rows.append(
                exact_difference_row(
                    best_m3[(widths[0], depth)],
                    best_m3[(widths[-1], depth)],
                    f"width_endpoint_at_fixed_L{depth}",
                )
            )
    # Depth checks at fixed width.
    widths = sorted({width for width, _ in best_m3})
    for width in widths:
        candidate_depths = sorted(
            depth for candidate_width, depth in best_m3
            if candidate_width == width
        )
        for left_depth, right_depth in zip(
            candidate_depths[:-1], candidate_depths[1:]
        ):
            exact_difference_rows.append(
                exact_difference_row(
                    best_m3[(width, left_depth)],
                    best_m3[(width, right_depth)],
                    f"depth_at_fixed_n{width}",
                )
            )
    # Preserve each individual n=256,L=32 versus L=64 increment check,
    # even when a pooled L=32 mean is also available.
    if (256, 32) in grouped_m3 and (256, 64) in grouped_m3:
        for left_ref in grouped_m3[(256, 32)]:
            for right_ref in grouped_m3[(256, 64)]:
                exact_difference_rows.append(
                    exact_difference_row(
                        left_ref,
                        right_ref,
                        "depth_at_fixed_n256_individual_archives",
                    )
                )
    for left_width, right_width in ((64, 128), (128, 256), (64, 256)):
        if left_width in m2_refs and right_width in m2_refs:
            exact_difference_rows.append(
                exact_difference_row(
                    m2_refs[left_width],
                    m2_refs[right_width],
                    "width_at_fixed_L16",
                )
            )
    write_csv(OUT / "exact_limit_differences.csv", exact_difference_rows)

    # ---------- Randomized QMC replicate uncertainty ----------
    qmc_rows: list[dict[str, Any]] = []
    qmc_groups: dict[str, tuple[dict[str, np.ndarray], dict[str, np.ndarray], int]] = {}
    group_specs = {
        "m3_P5_N16_M128_R64_QMC": [
            "pde_QMC_P5_N16_M128_R64_s20260723_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M128_R64_s20260724_dt0p02_T4.npz",
        ],
        "m3_P5_N16_M256_R128_QMC": [
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M256_R128_s20260725_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M256_R128_s20260726_dt0p02_T4.npz",
        ],
    }
    for group_name, names in group_specs.items():
        members = [p[name] for name in names if name in p and p[name].arrays]
        if len(members) >= 2:
            mean, sem, row = qmc_group(group_name, members)
            qmc_groups[group_name] = (mean, sem, len(members))
            qmc_rows.append(row)
    write_csv(OUT / "qmc_replicate_summary.csv", qmc_rows)

    # ---------- PDE versus exact-network curve comparisons ----------
    discrepancy_rows: list[dict[str, Any]] = []
    if all_m3_refs:
        ref16 = best_m3.get((64, 16))
        ref32s = [
            best_m3[key]
            for key in sorted(best_m3)
            if key[1] == 32
        ]
        # Main high-resolution replicate mean at matching N=L=16.
        if ref16 and "m3_P5_N16_M256_R128_QMC" in qmc_groups:
            mean, sem, count = qmc_groups["m3_P5_N16_M256_R128_QMC"]
            discrepancy_rows.append(
                reference_discrepancy_row(
                    "m3_P5_N16_M256_R128_QMC_replicate_mean",
                    mean,
                    sem,
                    count,
                    ref16,
                    bootstrap[ref16["name"]],
                    (
                        "Matching depth N=L=16. Exact reference is finite "
                        "n=64; SEM excludes finite-width and depth-limit bias."
                    ),
                )
            )
        # Single-run central P/N/cubature variants at matching depth.
        matching16 = [
            "pde_GH_P5_N16_M81_R243_s20260723_dt0p02_T8.npz",
            "pde_P5_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "pde_P15_N16_M128_R32_s20260723_dt0p02_T8.npz",
            "pde_P35_N16_M64_R64_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
            "pde_QMC_P5_N16_M512_R128_s20260723_dt0p02_T4.npz",
            "pde_QMC_P5_N16_M256_R256_s20260723_dt0p02_T4.npz",
            "pde_QMC_P15_N16_M128_R64_s20260723_dt0p02_T4.npz",
        ]
        if ref16:
            for name in matching16:
                if name not in p or not p[name].arrays:
                    continue
                curve = archive_curve(p[name])
                discrepancy_rows.append(
                    reference_discrepancy_row(
                        name,
                        curve,
                        zero_sem_like(curve),
                        1,
                        ref16,
                        bootstrap[ref16["name"]],
                        (
                            "Matching depth N=L=16; deterministic cubature "
                            "run. Exact SEM excludes finite-width bias."
                        ),
                    )
                )
        pde32 = p.get(
            "pde_QMC_P5_N32_M128_R64_s20260724_dt0p02_T4.npz"
        )
        if pde32 and pde32.arrays:
            curve = archive_curve(pde32)
            for ref in ref32s:
                discrepancy_rows.append(
                    reference_discrepancy_row(
                        pde32.name,
                        curve,
                        zero_sem_like(curve),
                        1,
                        ref,
                        bootstrap[ref["name"]],
                        (
                            "Matching depth N=L=32. Single QMC scramble; "
                            "exact reference is finite-width."
                        ),
                    )
                )
        # The primary high-cubature PDE is already intended as a
        # continuous-depth approximation; compare it to all stored L=32/64
        # references as well as to the matching finite N=L=16 check.
        primary = p.get(
            "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz"
        )
        if primary and primary.arrays:
            curve = archive_curve(primary)
            for ref in all_m3_refs.values():
                if int(ref["depth"]) < 32:
                    continue
                discrepancy_rows.append(
                    reference_discrepancy_row(
                        f"{primary.name}:continuous_depth_comparison",
                        curve,
                        zero_sem_like(curve),
                        1,
                        ref,
                        bootstrap[ref["name"]],
                        (
                            "Primary high-cubature PDE versus finite-depth "
                            "exact ensemble; Grams are compared on normalized "
                            "depth and include an initialization-cancelled "
                            "increment diagnostic."
                        ),
                    )
                )

    # Every m=2 PDE pilot against all three fixed-L width means.
    if m2_refs:
        m2_pde_names = sorted(
            name
            for name in p
            if name.startswith("operator_pde_m2_") and p[name].arrays
        )
        for name in m2_pde_names:
            curve = archive_curve(p[name])
            for ref in m2_refs.values():
                discrepancy_rows.append(
                    reference_discrepancy_row(
                        name,
                        curve,
                        zero_sem_like(curve),
                        1,
                        ref,
                        {},
                        (
                            "Pilot archive lacks full run metadata; fixed "
                            "L=16 finite-width mean, not an ordered limit."
                        ),
                    )
                )
    write_csv(OUT / "pde_reference_discrepancy.csv", discrepancy_rows)

    # ---------- Plateau / tail drift ----------
    plateau_rows: list[dict[str, Any]] = []
    main0 = p.get("pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz")
    main_ext = p.get(
        "pde_QMC_P5_N16_M256_R128_s20260723_dt0p1_T24_from8_to32.npz"
    )
    if main0 and main_ext:
        concatenated = concatenate_curves(main0, main_ext, "PDE_P5_N16_M256_R128_T32")
        plateau_rows.append(
            plateau_metrics(
                "PDE_P5_N16_M256_R128_T32",
                concatenated,
                Y3,
                tail_start=8.0,
            )
        )
    for ref in all_m3_refs.values():
        plateau_rows.append(
            plateau_metrics(
                ref["name"],
                ref["mean"],
                Y3,
                tail_start=4.0,
                member_arrays={
                    "f": ref["raw_f"],
                    "grams": ref["raw_grams"],
                },
            )
        )
    for ref in m2_refs.values():
        plateau_rows.append(
            plateau_metrics(
                ref["name"],
                ref["mean"],
                Y2,
                tail_start=2.0,
            )
        )
    # One representative from every distinct m=3 PDE resolution with T>=4.
    for archive in p.values():
        if not archive.arrays or not archive.name.startswith("pde_"):
            continue
        times = get_time(archive)
        if times[0] != 0 or times[-1] < 4:
            continue
        curve = archive_curve(archive)
        if curve["f"].shape[-1] != 3:
            continue
        tail_start = 4.0 if times[-1] >= 8 else 2.0
        plateau_rows.append(
            plateau_metrics(archive.name, curve, Y3, tail_start=tail_start)
        )
    write_csv(OUT / "plateau_tail_drift.csv", plateau_rows)

    # ---------- Conditional fast-layer variance versus depth ----------
    variance_rows: list[dict[str, Any]] = []
    variance_summary: list[dict[str, Any]] = []
    hp_path = NUM / "paired_W_conditional_variance_hp.csv"
    if hp_path.exists():
        with hp_path.open(newline="", encoding="utf-8") as handle:
            source_rows = list(csv.DictReader(handle))
        for source in source_rows:
            row = {key: float(value) for key, value in source.items()}
            row.update(
                {
                    "L_times_h_var_t0": row["L"] * row["h_var_t0"],
                    "L_times_h_var_t0p5": row["L"] * row["h_var_t0p5"],
                    "L_times_p_var_t0": row["L"] * row["p_var_t0"],
                    "L_times_p_var_t0p5": row["L"] * row["p_var_t0p5"],
                }
            )
            variance_rows.append(row)
        array = {
            key: np.asarray([row[key] for row in variance_rows], dtype=float)
            for key in variance_rows[0]
        }
        for field in (
            "h_var_t0",
            "h_var_t0p5",
            "p_var_t0",
            "p_var_t0p5",
        ):
            slope, slope_se, half_width = fit_loglog_slope(
                array["L"], array[field]
            )
            variance_summary.append(
                {
                    "field": field,
                    "depths": ";".join(str(int(v)) for v in array["L"]),
                    "loglog_slope": slope,
                    "slope_standard_error": slope_se,
                    "slope_95ci_lower": slope - half_width,
                    "slope_95ci_upper": slope + half_width,
                    "one_over_L_target": -1.0,
                    "max_L_times_variance": float(
                        np.max(array["L"] * array[field])
                    ),
                    "min_L_times_variance": float(
                        np.min(array["L"] * array[field])
                    ),
                }
            )
    write_csv(OUT / "conditional_variance_by_depth.csv", variance_rows)
    write_csv(OUT / "conditional_variance_slopes.csv", variance_summary)

    # ---------- Selected scale comparison (no new calculation or fitting) ----------
    headline_rows: list[dict[str, Any]] = []

    def headline_from(
        label: str,
        source_table: str,
        row: Mapping[str, Any],
        interpretation: str,
    ) -> None:
        headline_rows.append(
            {
                "label": label,
                "source_table": source_table,
                "output_curve_scale": row.get(
                    "output_max_l2",
                    row.get("pairwise_output_max_l2_max", ""),
                ),
                "gram_curve_scale": row.get(
                    "gram_max_fro",
                    row.get("pairwise_gram_max_fro_max", ""),
                ),
                "theta_curve_scale": row.get(
                    "theta_max_fro",
                    row.get("pairwise_theta_max_fro_max", ""),
                ),
                "gram_increment_curve_scale": row.get(
                    "gram_initial_centered_max_fro", ""
                ),
                "loss_of_mean_curve_scale": row.get("loss_max_abs", ""),
                "pde_feature_motion_scale": row.get(
                    "pde_terminal_feature_motion_max_fro", ""
                ),
                "gram_increment_fraction_pde_motion": row.get(
                    "gram_increment_gap_fraction_pde_feature_motion", ""
                ),
                "interpretation": interpretation,
            }
        )

    for row in solver_rows:
        if row["category"] == "time_step":
            headline_from(
                "RK4 dt 0.02 vs 0.01",
                "pde_solver_convergence.csv",
                row,
                "Pure time-discretization Cauchy difference.",
            )
        if (
            row["category"] == "depth_grid"
            and "N16_" in row["left"]
            and "N32_" in row["right"]
        ):
            headline_from(
                "PDE depth N16 vs N32",
                "pde_solver_convergence.csv",
                row,
                "Depth-discretization Cauchy difference.",
            )
        if (
            row["category"] == "operator_basis"
            and "QMC_P5_" in row["left"]
            and "QMC_P15_" in row["right"]
        ):
            headline_from(
                "PDE operator basis P5 vs P15",
                "pde_solver_convergence.csv",
                row,
                "Finite-P model-resolution difference.",
            )
        if row["category"] == "operator_basis_clean_hybrid":
            headline_from(
                "Clean hybrid PDE basis P5 vs P15",
                "pde_solver_convergence.csv",
                row,
                "Nested finite-P step at fixed N,M,R and cubature seed.",
            )
        if row["category"] == "fast_quadrature_clean_hybrid":
            headline_from(
                "Clean hybrid P15 fast cubature R128 vs R256",
                "pde_solver_convergence.csv",
                row,
                "Isolated fast-cubature refinement for the nested P15 PDE.",
            )
        if (
            row["category"] == "base_quadrature"
            and "M256_" in row["left"]
            and "M512_" in row["right"]
        ):
            headline_from(
                "PDE base cubature M256 vs M512",
                "pde_solver_convergence.csv",
                row,
                "Isolated high-resolution base-cubature difference.",
            )
        if (
            row["category"] == "fast_quadrature"
            and "R128_" in row["left"]
            and "R256_" in row["right"]
        ):
            headline_from(
                "PDE fast cubature R128 vs R256",
                "pde_solver_convergence.csv",
                row,
                "Isolated high-resolution fast-cubature difference.",
            )
        if row["category"] == "quadrature_method":
            headline_from(
                "Tensor GH vs high-resolution QMC",
                "pde_solver_convergence.csv",
                row,
                "Independent cubature-method disagreement; M/R differ.",
            )
    for row in qmc_rows:
        if row["group"] == "m3_P5_N16_M256_R128_QMC":
            headline_from(
                "QMC scramble spread at M256/R128",
                "qmc_replicate_summary.csv",
                row,
                "Maximum pairwise difference over three independent scrambles.",
            )
    for row in discrepancy_rows:
        if (
            row["pde"].startswith("pde_QMC_P5_N32_")
            and row["reference"].startswith("exact_ensemble_n256_L32")
        ):
            headline_from(
                "PDE N32 vs exact n256/L32 ensemble mean",
                "pde_reference_discrepancy.csv",
                row,
                "Best architecture-matched raw curve discrepancy currently stored.",
            )
        if (
            ":continuous_depth_comparison" in row["pde"]
            and row["reference"] == "pooled_exact_m3_n256_L32_S128"
        ):
            headline_from(
                "Primary PDE vs pooled exact n256/L32 S128",
                "pde_reference_discrepancy.csv",
                row,
                (
                    "Preregistered primary comparison; increment Gram "
                    "cancels independent finite-sample initialization noise."
                ),
            )
    for row in exact_difference_rows:
        if (
            row["comparison_type"] == "width_at_fixed_L32"
            and int(row["left_n"]) == 128
            and int(row["right_n"]) == 256
        ):
            headline_from(
                "Exact width n128 vs n256 at L32",
                "exact_limit_differences.csv",
                row,
                "Finite-width reference Cauchy difference.",
            )
        if (
            row["comparison_type"] == "depth_at_fixed_n256"
            and int(row["left_L"]) == 32
            and int(row["right_L"]) == 64
        ):
            headline_from(
                "Exact depth L32 vs L64 at n256",
                "exact_limit_differences.csv",
                row,
                "Finite-depth reference Cauchy difference.",
            )
        if (
            row["comparison_type"]
            == "depth_at_fixed_n256_individual_archives"
            and "seed6000" in row["left"]
        ):
            headline_from(
                "Exact n256 Gram increment L32 vs L64",
                "exact_limit_differences.csv",
                row,
                (
                    "Variance-reduced dense depth check; absolute Gram "
                    "difference is dominated by independent initialization."
                ),
            )
    write_csv(OUT / "headline_error_budget.csv", headline_rows)

    # ---------- Machine-readable synthesis ----------
    def find_pair(category: str, axis: str) -> list[dict[str, Any]]:
        return [
            row
            for row in solver_rows
            if row["category"] == category and row["isolated_axis"] == axis
        ]

    summary = {
        "generated_by": str(Path(__file__).relative_to(ROOT)),
        "coefficient_fitting_performed": False,
        "archives_total": len(archives),
        "archives_valid": sum(a.status == "valid" for a in archives.values()),
        "archives_salvaged": sum(
            a.status == "salvaged_complete_members" for a in archives.values()
        ),
        "archives_unreadable": sum(
            a.status == "unreadable" for a in archives.values()
        ),
        "solver_pair_rows": len(solver_rows),
        "reference_discrepancy_rows": len(discrepancy_rows),
        "qmc_groups": qmc_rows,
        "headline_error_budget": headline_rows,
        "time_step_rows": find_pair("time_step", "dt"),
        "semigroup_rows": semigroup_rows,
        "conditional_variance_slopes": variance_summary,
        "warnings": [
            (
                "The n=96,L=32 exact archive is truncated. Only complete "
                "CRC-valid raw members were used; its missing metadata and "
                "stored SEM arrays were reconstructed from filename/raw arrays."
            )
            if any(a.status == "salvaged_complete_members" for a in archives.values())
            else ""
        ],
    }
    (OUT / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(
        json.dumps(
            {
                "output_dir": str(OUT),
                "archives": len(archives),
                "solver_rows": len(solver_rows),
                "discrepancy_rows": len(discrepancy_rows),
                "plateau_rows": len(plateau_rows),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
