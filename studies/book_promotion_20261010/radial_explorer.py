"""Validate and export data for the original offline multi-experiment explorer.

This module evaluates no model and starts no training. Curves have shape (T,Q),
training predictions (T,M), and times (T,). Loss is the weighted squared error
sum_a weights[a]*(prediction[a]-labels[a])**2, with weights summing to one.
The optional loss* arrays support a mean of individual seed losses; plotting a
mean prediction must not silently replace that quantity by its squared error.
"""
from collections.abc import Mapping
import argparse
import json
from pathlib import Path

import numpy as np


def _plain(value, where="data"):
    """Own all input containers and reject values that cannot be safe JSON."""
    if isinstance(value, np.ndarray):
        return _plain(value.tolist(), where)
    if isinstance(value, np.generic):
        return _plain(value.item(), where)
    if isinstance(value, Mapping):
        if any(not isinstance(k, str) for k in value):
            raise ValueError(f"{where} keys must be strings")
        return {k: _plain(v, f"{where}.{k}") for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(v, where) for v in value]
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float) and np.isfinite(value):
        return value
    raise ValueError(f"{where} must contain only finite JSON values")


def _text(value, where):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{where} must be a nonempty string")
    return value


def _array(value, where, shape=None, ndim=None):
    try:
        raw = np.asarray(value)
        if raw.dtype.kind not in "fiu":
            raise ValueError
        result = np.asarray(raw, dtype=float)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{where} must be a finite real array") from error
    if (not np.isfinite(result).all() or (shape is not None and result.shape != shape)
            or (ndim is not None and result.ndim != ndim)):
        raise ValueError(f"{where} has an invalid shape or nonfinite values")
    return result


def _number(value, where, minimum=0.):
    result = _array(value, where, shape=())
    if result < minimum:
        raise ValueError(f"{where} must be at least {minimum}")
    return float(result)


def _integer(value, where, minimum=0):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{where} must be an integer >= {minimum}")
    return value


def _weights(value, count, where):
    result = _array(value, where, shape=(count,))
    if np.any(result < 0) or not np.isclose(result.sum(), 1., rtol=0., atol=1e-8):
        raise ValueError(f"{where} must be nonnegative and sum to one")
    return result


def _ids(value, count, where):
    if not isinstance(value, list) or len(value) != count:
        raise ValueError(f"{where} must contain one source ID per input")
    for item in value:
        _text(item, where)
    if len(set(value)) != count:
        raise ValueError(f"{where} must contain distinct source IDs")


def _loss(predictions, labels, weights):
    with np.errstate(over="ignore", invalid="ignore"):
        result = np.sum(weights * (predictions-labels)**2, axis=-1)
    if not np.isfinite(result).all():
        raise ValueError("Squared training errors overflow; rescale the supplied values")
    return result


def _check_loss(supplied, actual, where):
    supplied = _array(supplied, where, shape=np.shape(actual))
    # Legacy exports round both predictions and reported MSE. These tolerances
    # permit serialization rounding but reject a different loss convention.
    if np.any(supplied < 0) or not np.allclose(supplied, actual, rtol=1e-5, atol=1e-8):
        raise ValueError(f"{where} disagrees with the supplied training predictions")


def _model(model, case, q):
    if not isinstance(model, dict):
        raise ValueError("Each model must be an object")
    ident = _text(model.get("id"), "model.id")
    kind = model.setdefault("kind", "method")
    if kind not in ("method", "network", "network-mean", "closure"):
        raise ValueError(f"{ident}.kind must be method, network, network-mean, or closure")
    model["name"] = _text(model.get("name", model.get("label", ident)), f"{ident}.name")
    for key, minimum in (("width", 1), ("seed", 0), ("order", 1)):
        if key in model:
            _integer(model[key], f"{ident}.{key}", minimum)
    if kind in ("network", "network-mean") and "width" not in model:
        raise ValueError(f"{ident} needs width for network selection")
    if kind == "network" and "seed" not in model:
        raise ValueError(f"{ident} needs seed for network selection")
    if kind == "closure" and "order" not in model:
        raise ValueError(f"{ident} needs order for closure selection")
    times = _array(model.get("times"), f"{ident}.times", ndim=1)
    if not len(times) or times[0] < 0 or np.any(np.diff(times) <= 0):
        raise ValueError(f"{ident}.times must be nonempty, nonnegative and strictly increasing")
    count, m = len(times), len(case["labels"])
    curves = _array(model.get("curves"), f"{ident}.curves", shape=(count, q))
    train = _array(model.get("trainPredictions"), f"{ident}.trainPredictions", shape=(count, m))
    labels, weights = np.asarray(case["labels"]), np.asarray(case["weights"])
    if "lossTrainPredictions" in model:
        train = _array(model["lossTrainPredictions"], f"{ident}.lossTrainPredictions", ndim=2)
        if train.shape[0] != count or not train.shape[1]:
            raise ValueError(f"{ident}.lossTrainPredictions must have shape (T, loss samples)")
        labels = _array(model.get("lossLabels", labels), f"{ident}.lossLabels", shape=(train.shape[1],))
        weights = _weights(model.get("lossWeights", weights), train.shape[1], f"{ident}.lossWeights")
        model["lossLabels"], model["lossWeights"] = labels.tolist(), weights.tolist()
    elif "lossLabels" in model or "lossWeights" in model:
        raise ValueError(f"{ident}: lossLabels/lossWeights require lossTrainPredictions")
    losses = _loss(train, labels, weights)
    if "losses" in model:
        _check_loss(model["losses"], losses, f"{ident}.losses")
    model["losses"] = losses.tolist()
    model["finalTime"] = _number(model.get("finalTime", times[-1]), f"{ident}.finalTime")
    if model["finalTime"] < times[-1]:
        raise ValueError(f"{ident}.finalTime precedes its last recorded time")
    final_curve = _array(model.get("finalCurve", curves[-1]), f"{ident}.finalCurve", shape=(q,))
    same_endpoint = (model["finalTime"] == times[-1]
                     and np.allclose(final_curve, curves[-1], rtol=1e-7, atol=1e-8))
    endpoint_loss = None
    if "finalTrainPredictions" in model:
        final_train = _array(model["finalTrainPredictions"], f"{ident}.finalTrainPredictions", shape=(m,))
        if "lossTrainPredictions" not in model:
            endpoint_loss = _loss(final_train, labels, weights)
    if "finalLossTrainPredictions" in model:
        final_train = _array(model["finalLossTrainPredictions"], f"{ident}.finalLossTrainPredictions", shape=labels.shape)
        endpoint_loss = _loss(final_train, labels, weights)
    if endpoint_loss is None and same_endpoint:
        endpoint_loss = losses[-1]
    if "finalLoss" in model:
        model["finalLoss"] = _number(model["finalLoss"], f"{ident}.finalLoss")
        if endpoint_loss is not None:
            _check_loss(model["finalLoss"], endpoint_loss, f"{ident}.finalLoss")
    elif endpoint_loss is not None:
        model["finalLoss"] = float(endpoint_loss)
    else:
        raise ValueError(f"{ident}: a distinct endpoint needs finalLoss or final training predictions")
    model["finalCurve"] = final_curve.tolist()
    if "settled" in model and not isinstance(model["settled"], bool):
        raise ValueError(f"{ident}.settled must be boolean")
    return model


def normalize_bundle(bundle):
    """Return a validated owned JSON bundle; retain optional legacy metadata.

    Cases contain id, label, anglesDegrees[M], labels[M], weights[M], models,
    and queryAnglesDegrees[Q] sorted strictly within [0,360). Missing query
    angles use the legacy phase-zero uniform grid. Empty bundles are supported.
    Distinct legacy endpoints lacking final training arrays have an externally
    supplied finalLoss: only its finite nonnegative value can be checked.
    """
    bundle = _plain(bundle)
    if not isinstance(bundle, dict) or not isinstance(bundle.get("cases"), list):
        raise ValueError("A bundle must be an object with a cases list")
    seen = set()
    for case in bundle["cases"]:
        if not isinstance(case, dict):
            raise ValueError("Each case must be an object")
        ident = _text(case.get("id"), "case.id")
        if ident in seen:
            raise ValueError(f"Duplicate case ID: {ident}")
        seen.add(ident)
        case["label"] = _text(case.get("label", ident), f"{ident}.label")
        labels = _array(case.get("labels"), f"{ident}.labels", ndim=1)
        if not len(labels):
            raise ValueError(f"{ident} needs at least one training label")
        _array(case.get("anglesDegrees"), f"{ident}.anglesDegrees", shape=labels.shape)
        case["weights"] = _weights(case.get("weights", np.full(len(labels), 1/len(labels))), len(labels), f"{ident}.weights").tolist()
        case["amplitude"] = _number(case.get("amplitude", float(np.max(np.abs(labels))) or 1.), f"{ident}.amplitude")
        if case["amplitude"] == 0:
            raise ValueError(f"{ident}.amplitude must be positive")
        models = case.get("models")
        if not isinstance(models, list) or not models:
            raise ValueError(f"{ident}.models must be a nonempty list")
        if "queryAnglesDegrees" not in case:
            first = models[0] if isinstance(models[0], dict) else {}
            curve = _array(first.get("curves"), f"{ident}.models[0].curves", ndim=2)
            case["queryAnglesDegrees"] = (np.arange(curve.shape[1])*360/curve.shape[1]).tolist() if curve.shape[1] else []
        angles = _array(case["queryAnglesDegrees"], f"{ident}.queryAnglesDegrees", ndim=1)
        if (len(angles) < 3 or angles[0] < 0 or angles[-1] >= 360
                or np.any(np.diff(np.r_[angles, angles[0]+360]) <= 1e-10)):
            raise ValueError(f"{ident}.queryAnglesDegrees needs >=3 distinct increasing angles in [0,360)")
        for key, count in (("trainIds", len(labels)), ("queryIds", len(angles))):
            if key in case:
                _ids(case[key], count, f"{ident}.{key}")
        case["models"] = [_model(model, case, len(angles)) for model in models]
        ids = [model["id"] for model in models]
        if len(set(ids)) != len(ids):
            raise ValueError(f"{ident} contains duplicate model IDs")
        if case.get("ntk") is not None:
            ntk = case["ntk"]
            if not isinstance(ntk, dict):
                raise ValueError(f"{ident}.ntk must be an object")
            eigenvalues = _array(ntk.get("lambda"), f"{ident}.ntk.lambda", ndim=1)
            if not len(eigenvalues) or np.any(eigenvalues < 0):
                raise ValueError(f"{ident}.ntk.lambda must be nonempty and nonnegative")
            basis = _array(ntk.get("basis"), f"{ident}.ntk.basis", shape=(len(angles), len(eigenvalues)))
            _array(ntk.get("trainBasis"), f"{ident}.ntk.trainBasis", shape=(len(labels), len(eigenvalues)))
            endpoint = _array(ntk.get("endpoint"), f"{ident}.ntk.endpoint", shape=(len(angles),))
            if not np.allclose(endpoint, basis @ (eigenvalues > 0), rtol=1e-5, atol=1e-8):
                raise ValueError(f"{ident}.ntk.endpoint disagrees with its positive-eigenvalue limit")
            if ntk.get("initialOutput", 0) != 0:
                raise ValueError("The legacy analytic NTK evaluator supports zero initial output only")
    default = bundle.get("defaultCase", bundle["cases"][0]["id"] if seen else None)
    if (seen and (not isinstance(default, str) or default not in seen)) or (not seen and default is not None):
        raise ValueError("defaultCase must identify a supplied case (or be null for an empty bundle)")
    bundle["defaultCase"] = default
    return bundle


def _circle_inputs(value, where):
    inputs = _array(value, where, ndim=2)
    if (not len(inputs) or inputs.shape[1] != 2
            or not np.allclose(np.linalg.norm(inputs, axis=1), 1., rtol=0., atol=1e-10)):
        raise ValueError(f"{where} must contain finite unit rows of shape (N,2)")
    angles = np.mod(np.degrees(np.arctan2(inputs[:, 1], inputs[:, 0])), 360.)
    angles[np.isclose(angles, 360., rtol=0., atol=1e-12)] = 0.
    return angles


def make_case(case_id, label, query_inputs, training_inputs, labels, models, *,
              weights=None, train_ids=None, query_ids=None, amplitude=None, provenance=None):
    """Adapt assembled-core arrays; sort circle queries and aligned values/IDs.

    Pass data_core.Dataset arrays directly. Each model dictionary supplies its
    own physical times, query curves, and actual training predictions. Curves
    and finalCurve initially follow query_inputs; training arrays keep their
    original ordering. This operation does not interpolate or rescale outputs.
    """
    angles = _circle_inputs(query_inputs, "query_inputs")
    train_angles = _circle_inputs(training_inputs, "training_inputs")
    order = np.argsort(angles, kind="stable")
    models = _plain(models)
    if not isinstance(models, list):
        raise ValueError("models must be a sequence of model dictionaries")
    for model in models:
        if not isinstance(model, dict):
            raise ValueError("Each model must be an object")
        curves = _array(model.get("curves"), "model.curves", ndim=2)
        if curves.shape[1] != len(angles):
            raise ValueError("model.curves must have one column per query input")
        model["curves"] = curves[:, order].tolist()
        if "finalCurve" in model:
            model["finalCurve"] = _array(model["finalCurve"], "model.finalCurve", shape=(len(angles),))[order].tolist()
    case = dict(id=case_id, label=label, anglesDegrees=train_angles,
                queryAnglesDegrees=angles[order], labels=labels, models=models)
    for key, value in (("weights", weights), ("trainIds", train_ids),
                       ("amplitude", amplitude), ("provenance", provenance)):
        if value is not None:
            case[key] = value
    if query_ids is not None:
        source_ids = _plain(query_ids)
        _ids(source_ids, len(angles), "query_ids")
        case["queryIds"] = [source_ids[i] for i in order]
    return normalize_bundle({"cases": [case]})["cases"][0]


def write_explorer(path, bundle, *, template=None):
    """Embed validated data in the local D3 template, without network access."""
    bundle = normalize_bundle(bundle)
    source = Path(template) if template is not None else Path(__file__).with_name("radial_explorer.html")
    html = source.read_text(encoding="utf-8")
    if html.count("__RADIAL_DATA__") != 1:
        raise ValueError("The template must contain exactly one __RADIAL_DATA__ marker")
    encoded = json.dumps(bundle, ensure_ascii=True, separators=(",", ":"), allow_nan=False)
    for char, escaped in (("<", "\\u003c"), (">", "\\u003e"), ("&", "\\u0026")):
        encoded = encoded.replace(char, escaped)
    path = Path(path)
    if path.resolve() == source.resolve():
        raise ValueError("The output must not overwrite the reusable HTML template")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html.replace("__RADIAL_DATA__", encoded), encoding="utf-8")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path, nargs="+", help="JSON case or bundle files to merge")
    parser.add_argument("--out", type=Path, required=True, help="standalone HTML destination")
    args = parser.parse_args(argv)
    cases = []
    default = None
    for source in args.inputs:
        value = json.loads(source.read_text(encoding="utf-8"))
        value = normalize_bundle(value if isinstance(value, dict) and "cases" in value else {"cases": [value]})
        cases.extend(value["cases"])
        if default is None:
            default = value["defaultCase"]
    if args.out.resolve() in {source.resolve() for source in args.inputs}:
        parser.error("--out must not overwrite a source JSON file")
    print(write_explorer(args.out, {"cases": cases, "defaultCase": default}))


if __name__ == "__main__":
    main()
