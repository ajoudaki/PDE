"""Deterministic schema, source alignment, loss, and HTML export checks."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

from data_core import toy_data
from radial_explorer import make_case, normalize_bundle, write_explorer


SCRATCH = Path(__file__).resolve().parents[2] / "data/generated/book_promotion_20261010/radial_support"


def fixture():
    return {"cases": [{
        "id": "circle-a", "label": "Small circle", "anglesDegrees": [10., 190.],
        "queryAnglesDegrees": [0., 60., 200., 300.],
        "labels": [1., -2.], "weights": [.25, .75],
        "models": [{"id": "supplied", "times": [0., .3, 1.],
                    "curves": [[0., 0., 0., 0.], [1., 2., 3., 4.], [2., 3., 4., 5.]],
                    "trainPredictions": [[0., 0.], [.5, -1.], [1., -2.]]}]
    }]}


class RadialDataTests(unittest.TestCase):
    def assert_bad(self, update):
        bundle = fixture()
        update(bundle, bundle["cases"][0], bundle["cases"][0]["models"][0])
        with self.assertRaises(ValueError):
            normalize_bundle(bundle)

    def test_defaults_are_owned_and_loss_is_weighted_mse(self):
        original = fixture()
        normalized = normalize_bundle(original)
        case = normalized["cases"][0]
        model = case["models"][0]
        self.assertEqual(normalized["defaultCase"], "circle-a")
        self.assertEqual((model["kind"], model["name"]), ("method", "supplied"))
        # Independent arithmetic oracle, deliberately unequal sample weights.
        self.assertEqual(model["losses"], [3.25, .8125, 0.])
        self.assertEqual(model["finalCurve"], [2., 3., 4., 5.])
        self.assertEqual((model["finalTime"], model["finalLoss"]), (1., 0.))
        self.assertNotIn("losses", original["cases"][0]["models"][0])
        model["curves"][0][0] = 123.
        self.assertEqual(original["cases"][0]["models"][0]["curves"][0][0], 0.)

    def test_seed_mean_keeps_mean_of_losses(self):
        bundle = fixture()
        model = bundle["cases"][0]["models"][0]
        model.update(kind="network-mean", width=32,
                     trainPredictions=[[0., 0.]]*3,
                     lossTrainPredictions=[[0., 0., 2., -4.]]*3,
                     lossLabels=[1., -2., 1., -2.],
                     lossWeights=[.125, .375, .125, .375])
        # Last two seeds average to labels, but their average MSE is nonzero.
        model["trainPredictions"][-1] = [1., -2.]
        result = normalize_bundle(bundle)["cases"][0]["models"][0]
        self.assertEqual(result["losses"], [3.25]*3)
        self.assertEqual(result["finalLoss"], 3.25)
        bad = copy.deepcopy(bundle)
        bad["cases"][0]["models"][0]["losses"] = [3.25, 3.25, 0.]
        with self.assertRaisesRegex(ValueError, "disagrees"):
            normalize_bundle(bad)

    def test_explicit_endpoint_uses_actual_training_values(self):
        bundle = fixture()
        model = bundle["cases"][0]["models"][0]
        model.update(finalTime=2., finalCurve=[9., 8., 7., 6.],
                     finalTrainPredictions=[.5, -1.])
        result = normalize_bundle(bundle)["cases"][0]["models"][0]
        self.assertEqual(result["finalLoss"], .8125)
        model["finalLoss"] = 99.
        with self.assertRaisesRegex(ValueError, "disagrees"):
            normalize_bundle(bundle)
        del model["finalTrainPredictions"]
        # Explicit legacy endpoint MSE can be retained, not re-derived without
        # endpoint training arrays. This is the documented provenance boundary.
        self.assertEqual(normalize_bundle(bundle)["cases"][0]["models"][0]["finalLoss"], 99.)
        del model["finalLoss"]
        with self.assertRaisesRegex(ValueError, "distinct endpoint"):
            normalize_bundle(bundle)

    def test_array_adapter_sorts_shifted_queries_and_source_ids(self):
        data = toy_data(train_samples=3, query_samples=5, seed=2)
        permutation = np.array([3, 1, 4, 0, 2])
        queries = data.query_inputs[permutation]
        values = np.array([permutation, permutation+10.])
        model = dict(id="Taylor", name="Taylor dictionary", times=np.array([0., .2]),
                     curves=values, finalCurve=values[-1],
                     trainPredictions=np.zeros((2, 3)))
        case = make_case("toy", "Shifted queries", queries, data.train_inputs,
                         data.train_labels, [model], train_ids=data.train_ids,
                         query_ids=data.query_ids[permutation], provenance=data.provenance)
        np.testing.assert_allclose(case["models"][0]["curves"], [np.arange(5), np.arange(5)+10])
        self.assertEqual(case["models"][0]["finalCurve"], list(np.arange(5)+10))
        self.assertEqual(case["queryIds"], data.query_ids.tolist())
        self.assertEqual(case["trainIds"], data.train_ids.tolist())
        self.assertEqual(case["labels"], data.train_labels.tolist())
        self.assertEqual(case["provenance"], data.provenance)
        np.testing.assert_allclose(case["queryAnglesDegrees"][0], np.degrees(.137))
        np.testing.assert_array_equal(model["curves"], values)

    def test_reject_bad_shapes_times_grids_ids_and_missing_training_arrays(self):
        updates = [
            lambda b,c,m: b.update(defaultCase="absent"),
            lambda b,c,m: b["cases"].append(copy.deepcopy(c)),
            lambda b,c,m: c["models"].append(copy.deepcopy(m)),
            lambda b,c,m: c.update(labels=[]),
            lambda b,c,m: c.update(weights=[1., 1.]),
            lambda b,c,m: c.update(weights=[-.1, 1.1]),
            lambda b,c,m: c.update(amplitude=0),
            lambda b,c,m: c.update(anglesDegrees=[0.]),
            lambda b,c,m: c.update(queryAnglesDegrees=[0., 200., 60., 300.]),
            lambda b,c,m: c.update(queryAnglesDegrees=[0., 60., 60., 300.]),
            lambda b,c,m: c.update(queryAnglesDegrees=[0., 60., 200., 360.]),
            lambda b,c,m: c.update(queryAnglesDegrees=[0., 60., 200.]),
            lambda b,c,m: c.update(trainIds=["same", "same"]),
            lambda b,c,m: c.update(queryIds=["q"]),
            lambda b,c,m: c.update(queryIds=[1, 2, 3, 4]),
            lambda b,c,m: m.update(times=[0., .3, .3]),
            lambda b,c,m: m.update(times=[-.1, .3, 1.]),
            lambda b,c,m: m.update(times=[0., float("inf"), 1.]),
            lambda b,c,m: m.update(times=[0., .3]),
            lambda b,c,m: m.update(curves=[[0., 0., 0.]]*3),
            lambda b,c,m: m.pop("trainPredictions"),
            lambda b,c,m: m.update(trainPredictions=[[0., 0., 0., 0.]]*3),
            lambda b,c,m: m.update(trainPredictions=[[0., float("nan")]]*3),
            lambda b,c,m: m.update(losses=[0., 0., 0.]),
            lambda b,c,m: m.update(lossWeights=[.5, .5]),
            lambda b,c,m: m.update(finalLoss=-1.),
            lambda b,c,m: m.update(finalTime=.1),
            lambda b,c,m: m.update(settled="yes"),
            lambda b,c,m: m.update(kind="network", width=32),
            lambda b,c,m: m.update(kind="closure", order=True),
            lambda b,c,m: m.update(provenance={"value": float("inf")}),
        ]
        for update in updates:
            with self.subTest(update=updates.index(update)):
                self.assert_bad(update)

    def test_bad_circle_geometry_and_duplicate_queries(self):
        directions = np.array([[1., 0.], [0., 1.], [-1., 0.], [0., -1.]])
        model = dict(id="a", times=[0.], curves=[[0.]*4], trainPredictions=[[0.]])
        for queries in (directions*2, np.ones((4,3)), directions[[0,1,2,0]]):
            with self.subTest(queries=queries), self.assertRaises(ValueError):
                make_case("x", "X", queries, directions[:1], [1.], [model])

    def test_single_frame_and_legacy_uniform_grid(self):
        bundle = fixture()
        case = bundle["cases"][0]
        del case["queryAnglesDegrees"]
        model = case["models"][0]
        model.update(times=[2.], curves=[[1., 2., 3., 4.]], trainPredictions=[[1., -2.]])
        result = normalize_bundle(bundle)["cases"][0]
        self.assertEqual(result["queryAnglesDegrees"], [0., 90., 180., 270.])
        self.assertEqual(result["models"][0]["finalTime"], 2.)
        self.assertEqual(result["models"][0]["finalLoss"], 0.)

    def test_ntk_zero_eigenvalue_and_shapes(self):
        bundle = fixture()
        ntk = dict(lambda_=[0., 2.], basis=[[100., 1.]]*4,
                   trainBasis=[[10., 2.], [20., 3.]], endpoint=[1.]*4)
        ntk["lambda"] = ntk.pop("lambda_")
        bundle["cases"][0]["ntk"] = ntk
        self.assertEqual(normalize_bundle(bundle)["cases"][0]["ntk"]["endpoint"], [1.]*4)
        for key, value in (("endpoint", [101.]*4), ("lambda", [-1., 2.]),
                           ("trainBasis", [[1., 2.]]), ("initialOutput", 1.)):
            bad = copy.deepcopy(bundle)
            bad["cases"][0]["ntk"][key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                normalize_bundle(bad)

    def test_empty_bundle_and_export_escaping(self):
        self.assertEqual(normalize_bundle({"cases": []}), {"cases": [], "defaultCase": None})
        hostile = '</script><img src=x onerror="alert(1)">&\u2028\u2029'
        bundle = fixture()
        bundle["cases"][0]["label"] = hostile
        bundle["cases"][0]["models"][0]["name"] = hostile
        SCRATCH.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="data_test_", dir=SCRATCH) as directory:
            template = Path(directory)/"template.html"
            template.write_text('<script type="application/json">__RADIAL_DATA__</script>')
            output = write_explorer(Path(directory)/"nested/view.html", bundle, template=template)
            html = output.read_text()
            self.assertNotIn(hostile, html)
            self.assertEqual(html.count("</script>"), 1)
            self.assertNotIn("__RADIAL_DATA__", html)
            encoded = html.split(">", 1)[1].rsplit("<", 1)[0]
            self.assertEqual(json.loads(encoded)["cases"][0]["label"], hostile)
            with self.assertRaises(ValueError):
                write_explorer(template, bundle, template=template)
            for text in ("no marker", "__RADIAL_DATA____RADIAL_DATA__"):
                template.write_text(text)
                with self.assertRaises(ValueError):
                    write_explorer(output, bundle, template=template)


if __name__ == "__main__":
    unittest.main()
