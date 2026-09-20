"""Audit reported ratios and tested-budget targets from independent raw metrics.

This does not import analyzer logic. All numerical scalar arithmetic, including
target comparisons, runs on CUDA float64; structural row matching uses the CPU.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import sys
import time

import torch


DATA = Path(__file__).resolve().parents[2] / "data/generated/random_dictionary_learned_circle_20260920"
METHODS = ("ours", "gaussian", "orthogonal")
METRICS = {"l1": "l1", "l2": "rms", "max_abs": "max_abs"}
TARGETS = (1.0, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01)
ROW_KEYS = {
    "random_over_ours": ("case", "order"),
    "target_accuracy": ("case", "method", "metric", "target"),
    "tested_budget_ratios": ("case", "metric", "target", "control"),
}
CSV_NAMES = {"random_over_ours": "ratios.csv", "target_accuracy": "target_accuracy.csv",
             "tested_budget_ratios": "tested_budget_ratios.csv"}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decode_csv(value):
    if value == "":
        return None
    if value in ("True", "False"):
        return value == "True"
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def parse_cell(name):
    if name.endswith("_full"):
        return name[:-5], "full", 0
    for method in METHODS:
        tag = "_" + method + "_p"
        if tag in name:
            case, order = name.rsplit(tag, 1)
            return case, method, int(order)
    raise ValueError("Unrecognized cell key: " + name)


class SummaryAudit:
    def __init__(self, args):
        self.args = args
        self.device = torch.device(args.device)
        self.checks = []
        self.hashes = {}

    def read(self, path):
        self.hashes[str(path.resolve())] = sha256(path)
        return json.loads(path.read_text())

    def scalar(self, number):
        return torch.tensor(number, device=self.device, dtype=torch.float64)

    def check(self, name, passed, **details):
        self.checks.append(dict(name=name, passed=bool(passed), **details))

    def divide(self, numerator, denominator):
        n, d = self.scalar(numerator), self.scalar(denominator)
        return None if bool(d == 0) else float((n / d).item())

    def budget(self, dimensions):
        a, b = map(self.scalar, dimensions)
        return dict(dictionary_columns=int((a + b).item()), middle_coefficients=int((a * b).item()))

    def compare_value(self, label, expected, actual):
        if isinstance(expected, float) and isinstance(actual, (int, float)) and not isinstance(actual, bool):
            error = (self.scalar(expected) - self.scalar(actual)).abs()
            self.check(label, bool(error <= self.scalar(1e-11)), error=float(error.item()))
        else:
            self.check(label, expected == actual, expected=expected, actual=actual)

    def compare_rows(self, label, expected, actual, key_fields):
        def key(row):
            return tuple(row.get(field) for field in key_fields)
        wanted, found = Counter(map(key, expected)), Counter(map(key, actual))
        self.check(label + ":row_multiset", wanted == found,
                   missing=[list(v) for v in (wanted - found).elements()],
                   extra=[list(v) for v in (found - wanted).elements()])
        actual_index = {key(row): row for row in actual}
        for row in expected:
            token = key(row)
            if token not in actual_index:
                continue
            claimed = actual_index[token]
            self.check(label + ":fields:" + str(token), set(row) == set(claimed),
                       missing=sorted(set(row) - set(claimed)), extra=sorted(set(claimed) - set(row)))
            for field, expected_value in row.items():
                self.compare_value(label + ":" + str(token) + ":" + field,
                                   expected_value, claimed.get(field))

    def run(self):
        started = time.monotonic()
        if self.device.type != "cuda" or not torch.cuda.is_available():
            raise ValueError("CUDA float64 is mandatory; coordinate GPU allocation first")
        torch.set_default_dtype(torch.float64)
        independent = self.read(self.args.independent / "checks.json")
        summary = self.read(self.args.analysis / "summary.json")
        self.check("upstream_technical_audit", independent["technical_checks_passed"])
        upstream_metric_path = (self.args.analysis / "metrics.json").resolve()
        expected_metric_hash = independent["input_hashes"].get(str(upstream_metric_path))
        self.check("same_audited_metric_file", expected_metric_hash == sha256(upstream_metric_path),
                   expected=expected_metric_hash, actual=sha256(upstream_metric_path))
        metrics = {(r["case"], r["method"], r["order"], r["level"]): r for r in independent["metrics"]}
        self.check("independent_metric_unique_keys", len(metrics) == len(independent["metrics"]))
        selected = independent["selected"]
        cells = {parse_cell(name): name for name in selected if not name.endswith("_full")}
        cases = sorted({case for case, _, _ in cells})
        orders = sorted({order for _, _, order in cells})
        self.check("summary_cases", sorted(summary["cases"]) == cases)
        self.check("summary_orders", sorted(summary["orders"]) == orders)
        expected_cells = {(case, method, order) for case in cases for method in METHODS for order in orders}
        self.check("complete_cell_set", set(cells) == expected_cells,
                   missing=sorted(expected_cells - set(cells)), extra=sorted(set(cells) - expected_cells))
        validity = {}
        budgets = {}
        for cell, name in cells.items():
            case, method, order = cell
            validity[cell] = bool(independent["refinements"].get(name, {}).get("numerically_valid", False) and
                                  independent["refinements"].get(case + "_full", {}).get("numerically_valid", False))
            if validity[cell]:
                self.check("both_metric_levels:" + name, all((*cell, level) in metrics for level in (0, 1)))
            dimensions = []
            for path, dictionary in independent["dictionaries"].items():
                if Path(path).name == name:
                    dimensions.append(tuple(p["count"] for p in dictionary["populations"]))
            self.check("dictionary_dimensions_present:" + name, bool(dimensions))
            self.check("dictionary_dimensions_consistent:" + name, bool(dimensions) and len(set(dimensions)) == 1)
            if dimensions:
                budgets[cell] = self.budget(dimensions[0])
        self.check("summary_valid_count", summary["valid_comparisons"] == sum(validity.values()))
        self.check("summary_declared_count", summary["declared_comparisons"] == len(expected_cells))
        self.check("summary_all_valid", summary["all_comparisons_valid"] == all(validity.values()))
        ratios = []
        for case in cases:
            for order in orders:
                valid = all(validity.get((case, method, order), False) for method in METHODS)
                row = dict(case=case, order=order, valid=valid, **budgets[(case, "ours", order)])
                for method in METHODS:
                    self.check("matched_dictionary_budget:" + str((case, method, order)),
                               budgets[(case, method, order)] == budgets[(case, "ours", order)])
                for level, prefix in ((0, ""), (1, "refined_")):
                    for field, metric in METRICS.items():
                        if valid:
                            ours = self.scalar(metrics[(case, "ours", order, level)][metric])
                            randoms = {method: self.scalar(metrics[(case, method, order, level)][metric])
                                       for method in METHODS[1:]}
                            values = {method: None if bool(ours == 0) else float((value / ours).item())
                                      for method, value in randoms.items()}
                            best = None if bool(ours == 0) else float((torch.minimum(*randoms.values()) / ours).item())
                        else:
                            values = {method: None for method in METHODS[1:]}
                            best = None
                        for method, value in values.items():
                            row[prefix + method + "_over_ours_" + field] = value
                        row[prefix + "better_random_over_ours_" + field] = best
                ratios.append(row)
        targets = []
        boundary = []
        for case in cases:
            for method in METHODS:
                valid_orders = [p for p in orders if validity.get((case, method, p), False)]
                unresolved = [p for p in orders if p not in valid_orders]
                for field, metric in METRICS.items():
                    for target in TARGETS:
                        # Exact <= comparisons at BOTH levels; no tolerance around target.
                        hits = [p for p in valid_orders if all(bool(self.scalar(metrics[(case, method, p, level)][metric]) <=
                                                                      self.scalar(target)) for level in (0, 1))]
                        smallest = min(hits, key=lambda p: (budgets[(case, method, p)]["dictionary_columns"],
                                                           budgets[(case, method, p)]["middle_coefficients"], p)) if hits else None
                        row = dict(case=case, method=method, metric=field, target=target,
                            status="achieved_at_tested_budget" if hits else "not_demonstrated_at_tested_budgets",
                            smallest_tested_achieving_order=smallest,
                            **(budgets[(case, method, smallest)] if hits else dict(dictionary_columns=None, middle_coefficients=None)),
                            tested_orders=orders, valid_tested_orders=valid_orders,
                            achieving_tested_orders=hits, unresolved_tested_orders=unresolved)
                        targets.append(row)
                        if method == "ours" and field == "l2" and target == 0.05 and 7 in valid_orders:
                            boundary.append(dict(case=case, order=7, target=target,
                                lower=metrics[(case, method, 7, 0)][metric], higher=metrics[(case, method, 7, 1)][metric],
                                both_qualify=7 in hits, smallest_tested_achieving_order=smallest))
        target_index = {(r["case"], r["method"], r["metric"], r["target"]): r for r in targets}
        budget_ratios = []
        for case in cases:
            for field in METRICS:
                for target in TARGETS:
                    ours = target_index[case, "ours", field, target]
                    for control in METHODS[1:]:
                        other = target_index[case, control, field, target]
                        both = ours["dictionary_columns"] is not None and other["dictionary_columns"] is not None
                        budget_ratios.append(dict(case=case, metric=field, target=target, control=control,
                            ours_status=ours["status"], control_status=other["status"],
                            dictionary_columns_ratio=self.divide(other["dictionary_columns"], ours["dictionary_columns"]) if both else None,
                            middle_coefficients_ratio=self.divide(other["middle_coefficients"], ours["middle_coefficients"]) if both else None))
        expected_tables = dict(random_over_ours=ratios, target_accuracy=targets, tested_budget_ratios=budget_ratios)
        for name, rows in expected_tables.items():
            self.compare_rows("summary:" + name, rows, summary[name], ROW_KEYS[name])
            path = self.args.analysis / CSV_NAMES[name]
            self.hashes[str(path.resolve())] = sha256(path)
            with path.open() as stream:
                csv_rows = [{key: decode_csv(value) for key, value in row.items()} for row in csv.DictReader(stream)]
            self.compare_rows("csv:" + name, rows, csv_rows, ROW_KEYS[name])
        torch.cuda.synchronize(self.device)
        output = dict(scope="Independent summary arithmetic audit from prior independently replayed raw metrics.",
            command=sys.argv, cwd=str(Path.cwd()), source_sha256=sha256(__file__), input_hashes=self.hashes,
            device=str(self.device), gpu=torch.cuda.get_device_name(self.device), dtype="float64", torch=torch.__version__,
            wall_seconds=time.monotonic() - started, checks=self.checks, boundary_p7_rms_005=boundary,
            tables=expected_tables, passed=all(c["passed"] for c in self.checks),
            limitations=["Depends on the recorded independent raw-output audit; no new training or replay.",
                         "Budgets are tested nominal feature counts and middle coefficients, not untested or whole-model guarantees."])
        self.args.out.mkdir(exist_ok=False, parents=True)
        (self.args.out / "summary_checks.json").write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
        print(json.dumps(dict(passed=output["passed"], checks=len(self.checks), wall_seconds=output["wall_seconds"],
                             boundary_p7_rms_005=boundary), indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--independent", type=Path, required=True)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:1")
    args = parser.parse_args()
    for name in ("independent", "analysis", "out"):
        path = getattr(args, name).resolve()
        if path.parent != DATA:
            raise ValueError("Path outside permitted study data namespace")
        setattr(args, name, path)
    if not args.out.name.startswith("scaling_independent_check"):
        raise ValueError("Output outside assigned independent-check namespace")
    with torch.inference_mode():
        SummaryAudit(args).run()


if __name__ == "__main__":
    main()
