"""Deterministic analytic fixtures for activation analysis; no network or GPU.

All generated records are synthetic reporting fixtures, not scientific runs.
Fixture predictions are Fourier modes with analytically known discrete RMS.
Scratch is retained below activation_circle_analysis_fixture01.
"""

from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

import analyze_activation_circle as analysis


core = analysis.core
CASES = core.read_json(analysis.STUDY / "activation_circle_cases.json")
ANGLE = 2 * np.pi * np.arange(8192) / 8192
PANEL = np.column_stack((np.cos(ANGLE), np.sin(ANGLE)))
FIXTURE_ROOT = analysis.STUDY.parents[1] / "data/generated/neural_response_memory_20260922/activation_circle_analysis_fixture01"
INITIAL_HASH = "6043d3c0097c6cdb4c22b6db84fc4d5975b61dbeac895b6f6a2a2a8402e79ca0"


def diagnostics():
    return dict(feature_motion_h1_rms=.1, feature_motion_h2_rms=.2, feature_motion_h3_rms=.3,
                w_motion_rms=.4, c_motion_rms=.5,
                activation_diagnostics={f"layer{k}": {"activation_rms": .5, "derivative_rms": .2}
                                        for k in (1, 2, 3)})


def prediction(model, coarse=False, sensitivity=.00005):
    order = 0 if model == "dense" else int(model[1:])
    error = (0., .12, .03, .05)[order]
    return (np.sin(ANGLE) + np.sqrt(2) * error * np.sin(2 * ANGLE)
            + (np.sqrt(2) * sensitivity * np.cos((3 if model == "dense" else 5) * ANGLE) if coarse else 0))


def memory_run(case, model, coarse=False, losses=analysis.MILESTONES, sensitivity=.00005):
    tol = analysis.PRIMARY_RTOLS[0 if coarse else 1]
    observations = {core.milestone_label(loss): dict(time=20. * (i + 1), physical_mse=loss,
                        prediction=prediction(model, coarse, sensitivity), requested_loss=loss,
                        requested_time=None, kind="loss", **diagnostics()) for i, loss in enumerate(losses)}
    for t in analysis.TIMES:
        observations[analysis.time_label(t)] = dict(time=t, physical_mse=.37,
            prediction=prediction(model, coarse, sensitivity), requested_time=t, requested_loss=None,
            kind="time", **diagnostics())
    config = dict(activation=CASES[case]["activation"], task=CASES[case]["task"], case=case,
                  model="dense" if model == "dense" else "moment", order=1 if model == "dense" else int(model[1:]),
                  rtol=tol, atol=tol / 100)
    summary = dict(status="target_loss" if .001 in losses else "wall_limit", training_mse=min(losses), time=1500.)
    return core.Run(Path("/synthetic_fixture") / case / f"{model}_{tol}", config, summary, case, model,
                    observations, ANGLE, np.array([0., 1500.]), np.array([1., min(losses)]), {})


def selection(case, cap_p3=False):
    return {(case, model): (memory_run(case, model, losses=(.9, .5) if cap_p3 and model == "P3" else analysis.MILESTONES),
                           memory_run(case, model, True, losses=(.9, .5) if cap_p3 and model == "P3" else analysis.MILESTONES))
            for model in analysis.MODELS}


def write_fixture(root, case, model, coarse, *, capped=False, failed=False, sensitivity=.00005):
    """Write runner-shaped synthetic archives; checkpoints contain only audited scalars."""
    literal, tol = CASES[case], analysis.PRIMARY_RTOLS[0 if coarse else 1]
    path = root / case / (model + ("_coarse" if coarse else "_fine"))
    path.mkdir(parents=True)
    theta = np.deg2rad(literal["angles_degrees"])
    inputs, labels = np.column_stack((np.cos(theta), np.sin(theta))), np.asarray(literal["labels"], dtype=float)
    config = dict(case=case, activation=literal["activation"], task=literal["task"], phase="primary",
                  model="dense" if model == "dense" else "moment", order=1 if model == "dense" else int(model[1:]),
                  width=4096, seed=20260920, rtol=tol, atol=tol / 100, query_count=8192,
                  milestones=list(analysis.MILESTONES), observation_times=list(analysis.TIMES), target_loss=.001,
                  inputs=inputs.tolist(), labels=labels.tolist(), synthetic_fixture=True)
    config.update(analysis.CONTROLS)
    core.write_json(path / "config.json", config)
    if failed:
        core.write_json(path / "failure.json", dict(status="failed", message="Deliberate synthetic failed attempt"))
        return path
    losses = (.9, .5) if capped else analysis.MILESTONES
    end = 200. if capped else 1500.
    events = [(0., "initial", None, None, 1.)]
    events.extend((20. * (i + 1), core.milestone_label(loss), None, loss, loss) for i, loss in enumerate(losses))
    events.extend((t, analysis.time_label(t), t, None, .37) for t in analysis.TIMES if t < end)
    events.append((end, "final", None, None, min(losses)))
    events.sort(key=lambda event: (event[0], event[1]))
    records, checkpoints, checkpoint_hashes = [], [], {}
    for t, label, requested_time, requested_loss, loss in events:
        record = dict(label=label, time=t, training_mse=loss, requested_time=requested_time,
                      requested_loss=requested_loss, kind="loss" if requested_loss else "time" if requested_time else label,
                      **diagnostics())
        records.append(record)
        if label.startswith(("time_", "loss_")):
            checkpoint = "checkpoint_" + label.replace(".", "p") + ".npz"
            np.savez(path / checkpoint, physical_time=np.asarray(t), training_mse=np.asarray(loss))
            checkpoints.append(checkpoint)
            checkpoint_hashes[checkpoint] = core.sha256(path / checkpoint)
    times = np.arange(0., end + 2., 2.)
    trace_losses = np.linspace(1., min(losses), len(times))
    np.savez(path / "arrays.npz", circle_angles=ANGLE, circle_inputs=PANEL,
             circle_predictions=np.stack([prediction(model, coarse, sensitivity)] * len(records)),
             train_inputs=inputs, train_labels=labels,
             train_predictions=np.stack([labels + np.sqrt(record["training_mse"]) for record in records]),
             observation_times=np.array([record["time"] for record in records]),
             observation_training_mse=np.array([record["training_mse"] for record in records]),
             observation_labels=np.array([record["label"] for record in records]), times=times, losses=trace_losses,
             accepted_steps=np.diff(times), local_error_ratios=np.full(len(times) - 1, .1))
    manifest = dict(case=case, activation=literal["activation"], task=literal["task"], phase="primary",
                    effective_config_sha256=core.sha256(path / "config.json"), initialization_hash=INITIAL_HASH,
                    source_sha256={name: core.sha256(analysis.STUDY / name) for name in analysis.PRODUCER_SOURCES},
                    data_sha256=core.array_hash(inputs, labels), query_sha256=core.array_hash(PANEL), synthetic_fixture=True)
    summary = dict(manifest, model=config["model"], P=config["order"] if model != "dense" else None,
                   hidden_layers=3, d=2, width=4096, seed=20260920, rtol=tol, atol=tol / 100,
                   query_count=8192, sample_count=8, dtype="float64", time=end, training_mse=min(losses),
                   status="wall_limit" if capped else "target_loss", crossed_losses=list(losses),
                   observed_physical_times=[t for t in analysis.TIMES if t < end], observations=records,
                   checkpoints=checkpoints, checkpoint_sha256=checkpoint_hashes,
                   arrays_sha256=core.sha256(path / "arrays.npz"), accepted=len(times) - 1, rejected=0,
                   integration_with_observations_seconds=1., integration_seconds_excluding_observations=.8)
    core.write_json(path / "manifest.json", manifest)
    core.write_json(path / "summary.json", summary)
    return path


class ActivationAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        FIXTURE_ROOT.mkdir(parents=True, exist_ok=True)
        cls.scratch = Path(tempfile.mkdtemp(prefix="checks_", dir=FIXTURE_ROOT))

    def test_fourier_scores_and_common_dense_reference(self):
        case = next(iter(CASES))
        selected = selection(case)
        rows, primary, _, times, _, _ = analysis.comparison_tables({case: CASES[case]}, selected)
        self.assertEqual(len(rows), 21)
        self.assertEqual(len(times), 9)
        for row, expected in zip(primary, (.12, .03, .05)):
            self.assertAlmostEqual(row["rms_8192"], expected, places=14)
            self.assertAlmostEqual(row["rms_4096"], expected, places=14)
            self.assertAlmostEqual(row["closure_refinement_rms"], .00005, places=14)
            self.assertTrue(row["numerical_pass"])
            self.assertEqual(row["dense_run"], str(selected[(case, "dense")][0].path))
        order = core.order_comparisons(rows)
        self.assertTrue(all(row["resolved"] for row in order))
        self.assertEqual(next(row["verdict"] for row in order if row["lower_P"] == 2 and row["higher_P"] == 3),
                         "higher_order_worsens")

    def test_cap_does_not_hide_other_fitted_pairs(self):
        case = next(iter(CASES))
        _, primary, fallback, _, _, endpoints = analysis.comparison_tables({case: CASES[case]}, selection(case, True))
        self.assertEqual([row["available"] for row in primary], [True, True, False])
        self.assertEqual(endpoints[case]["plot_milestone"], .001)
        self.assertEqual(endpoints[case]["fallback_common_milestone"], .5)
        self.assertEqual([row["milestone"] for row in fallback], [.5, .5, .5])

    def test_time_pairing_uses_requested_time_not_loss(self):
        case, requested = next(iter(CASES)), 100.
        selected = selection(case)
        row = analysis.matched_time_comparison(case, 1, requested, selected)
        self.assertTrue(row["numerical_pass"])
        self.assertNotIn("physical_loss", row["numerical_gates"])
        self.assertEqual(row["requested_time"], requested)
        selected[(case, "P1")][0].observations[analysis.time_label(requested)]["requested_time"] = 10.
        row = analysis.matched_time_comparison(case, 1, requested, selected)
        self.assertFalse(row["numerical_gates"]["physical_time"])
        selected[(case, "P1")][0].observations.pop(analysis.time_label(requested))
        self.assertIsNone(analysis.matched_time_comparison(case, 1, requested, selected))

    def test_refinement_requires_finished_schedule_and_shared_evidence(self):
        case = next(iter(CASES))
        selected = selection(case)
        selected[(case, "P2")] = (selected[(case, "P2")][0], memory_run(case, "P2", True, sensitivity=.02))
        rows = analysis.comparison_tables({case: CASES[case]}, selected)[0]
        self.assertEqual(analysis.refinement_decisions(rows, selected, False), [])
        requests = analysis.refinement_decisions(rows, selected, True)
        self.assertEqual([row["model"] for row in requests], ["dense", "P2"])
        self.assertIn("paired_dense_required_by_protocol", requests[0]["reasons"][0]["gates"])
        selected[(case, "dense")] = (selected[(case, "dense")][0], None)
        rows = analysis.comparison_tables({case: CASES[case]}, selected)[0]
        self.assertEqual(analysis.refinement_decisions(rows, selected, True), [])

    def test_grid_and_time_only_failures_do_not_trigger(self):
        case = next(iter(CASES))
        selected = selection(case)
        for run in selected[(case, "P1")]:
            for loss in analysis.MILESTONES:
                run.observations[core.milestone_label(loss)]["prediction"] = np.sin(ANGLE) + .04 * (1 + np.cos(4096 * ANGLE))
        for requested in analysis.TIMES:
            selected[(case, "P2")][1].observations[analysis.time_label(requested)]["prediction"] += .1
        rows, _, _, times, _, _ = analysis.comparison_tables({case: CASES[case]}, selected)
        self.assertTrue(any(row["failed_gates"] == ["grid"] for row in rows))
        self.assertTrue(any(not row["numerical_pass"] for row in times))
        self.assertEqual(analysis.refinement_decisions(rows, selected, True), [])

    def test_physical_loss_gate_triggers_only_affected_model(self):
        case = next(iter(CASES))
        selected = selection(case)
        selected[(case, "P3")][0].observations[core.milestone_label(.001)]["physical_mse"] = .0012
        rows = analysis.comparison_tables({case: CASES[case]}, selected)[0]
        requests = analysis.refinement_decisions(rows, selected, True)
        self.assertEqual([r["model"] for r in requests], ["dense", "P3"])
        self.assertIn("physical_loss", requests[1]["reasons"][0]["gates"])

    def test_failed_refinement_is_unresolved_and_cannot_be_retried(self):
        case = next(iter(CASES))
        selected = selection(case)
        failed = dict(case=case, model="P2", rtol=core.EXTRA_RTOL, finished=True,
                      valid_scientific_run=False, path="/synthetic_failed_extra", status="failed")
        rows, primary, _, _, _, _ = analysis.comparison_tables({case: CASES[case]}, selected, {(case, "P2"): failed})
        self.assertFalse(primary[1]["numerical_pass"])
        self.assertIn("closure_additional_resolution_unavailable", primary[1]["failed_gates"])
        requests = analysis.refinement_decisions(rows, selected, True, [failed])
        self.assertEqual([row["model"] for row in requests], ["P2"])
        request = next(row for row in requests if row["model"] == "P2")
        self.assertFalse(request["conditional_run_available"])
        self.assertEqual(request["action"], "unresolved_after_failed_refinement")

    def test_activation_metadata_and_event_integrity(self):
        case = next(iter(CASES))
        path = write_fixture(self.scratch / "metadata", case, "dense", False)
        run = analysis.load_run(path, [self.scratch], CASES, {(4096, 20260920): INITIAL_HASH}, {})
        wrong = dict(run.summary, activation="sigmoid")
        with self.assertRaisesRegex(ValueError, "activation mismatch"):
            analysis.case_metadata(run.config, CASES, wrong)
        wrong = dict(run.summary, task="quadrant_alternating")
        with self.assertRaisesRegex(ValueError, "task mismatch"):
            analysis.case_metadata(run.config, CASES, wrong)
        with self.assertRaisesRegex(ValueError, "control mismatch"):
            analysis.validate_config(dict(run.config, max_step=20.))
        with self.assertRaisesRegex(ValueError, "phase/tolerance"):
            analysis.validate_config(dict(run.config, phase="exploratory"))
        analysis.validate_config(dict(run.config, phase="refine", rtol=core.EXTRA_RTOL))
        with self.assertRaisesRegex(ValueError, "phase/tolerance"):
            analysis.validate_config(dict(run.config, phase="refined", rtol=core.EXTRA_RTOL))
        run.summary["observations"][1], run.summary["observations"][2] = run.summary["observations"][2], run.summary["observations"][1]
        with self.assertRaisesRegex(ValueError, "chronological"):
            analysis.validate_observations(run)
        run.summary["observations"][1], run.summary["observations"][2] = run.summary["observations"][2], run.summary["observations"][1]
        np.savez(path / "checkpoint_time_10.npz", physical_time=np.asarray(11.), training_mse=np.asarray(.37))
        with self.assertRaisesRegex(ValueError, "checkpoint scalar"):
            analysis.validate_observations(run)

    def test_optional_campaign_manifest_checks_frozen_phase_and_sources(self):
        case = next(iter(CASES))
        root = self.scratch / "campaign_manifest"
        path = write_fixture(root, case, "dense", False)
        initial = {(4096, 20260920): INITIAL_HASH}
        standalone = analysis.load_run(path, [root], CASES, initial, {})
        self.assertEqual(standalone.provenance["campaign_manifests"], [])
        manifest = dict(phase="primary", source_sha256={name: core.sha256(analysis.STUDY / name)
                                                     for name in analysis.CAMPAIGN_SOURCES})
        core.write_json(root / "manifest.json", manifest)
        checked = analysis.load_run(path, [root], CASES, initial, {})
        self.assertEqual(checked.provenance["campaign_manifest_status"], "validated")
        core.write_json(root / "manifest.json", dict(manifest, phase="refine"))
        with self.assertRaisesRegex(ValueError, "Campaign phase mismatch"):
            analysis.load_run(path, [root], CASES, initial, {})
        manifest["source_sha256"]["ACTIVATION_CIRCLE_PROTOCOL.md"] = "0" * 64
        core.write_json(root / "manifest.json", manifest)
        with self.assertRaisesRegex(ValueError, "Campaign frozen source digest"):
            analysis.load_run(path, [root], CASES, initial, {})

    def test_full_schedule_failed_attempt_and_eight_panel_artifacts(self):
        root = self.scratch / "full_schedule"
        capped_case, failed_case = "sigmoid__quadrant_alternating", "gelu__two_outliers_alternating"
        for case in CASES:
            for model in analysis.MODELS:
                for coarse in (True, False):
                    write_fixture(root, case, model, coarse,
                        capped=case == capped_case and model == "P3",
                        failed=case == failed_case and model == "P1" and coarse,
                        sensitivity=.02 if case == next(iter(CASES)) and model == "P2" else .00005)
        out = self.scratch / "analysis"
        result = analysis.analyze([root], out)
        self.assertTrue(result["primary_schedule_complete"])
        self.assertFalse(result["primary_inventory_complete"])
        self.assertEqual(result["finished_primary_attempts"], 64)
        self.assertEqual(result["valid_primary_trajectories"], 63)
        self.assertEqual(result["resources"]["scientific_trajectories"], 63)
        self.assertEqual(len(result["run_inventory"]), 64)
        self.assertEqual(len(result["primary_comparisons"]), 24)
        self.assertEqual(len(result["endpoint_comparisons"]), 23)
        self.assertEqual(result["endpoints"][capped_case]["primary_available_orders"], [1, 2])
        self.assertEqual([row["model"] for row in result["required_refinements"]], ["dense", "P2"])
        self.assertEqual(set(result["figure_panel_counts"].values()), {8})
        self.assertEqual(len(result["figures"]), 8)
        self.assertTrue(all((out / name).stat().st_size > 1000 for name in result["figures"]))
        self.assertEqual(set(result["source_sha256"]), set(analysis.SOURCES))
        with self.assertRaisesRegex(ValueError, "fresh directory"):
            analysis.analyze([root], out)
        (self.scratch / "fixture_receipt.json").write_text(json.dumps(dict(
            synthetic_fixture=True, checks="analytical Fourier reporting fixtures; no training", output=str(out)), indent=2) + "\n")


if __name__ == "__main__":
    unittest.main()
