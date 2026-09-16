"""Explicit-array prediction/Gram diagnostics and training-loss checkpoint matching.

No calibration, data acquisition, checkpoint selection by output agreement,
interpolation, extrapolation, scientific seeding or population claim occurs.
Undefined relative errors/correlations are returned as None (JSON null).
"""
import math
import numpy as np


def _real(value, name, ndim):
    raw = np.asarray(value)
    if raw.dtype.kind not in "iuf" or raw.ndim != ndim or not raw.size:
        raise ValueError(f"{name} needs a nonempty real {ndim}-dimensional array")
    with np.errstate(over="ignore", under="ignore", invalid="ignore"):
        out = np.array(raw,dtype=np.float64,copy=True)
    if np.any((raw != 0) & (out == 0)):
        raise ValueError(f"{name} has nonzero entries below float64 range")
    if not np.isfinite(out).all():
        raise ValueError(f"nonfinite {name}")
    return out


def _same_ids(ids, reference_ids, count):
    a,b = np.asarray(ids),np.asarray(reference_ids)
    if a.shape != (count,) or b.shape != (count,):
        raise ValueError("IDs must match the sample axis")
    if a.dtype.kind not in "iuUS" or b.dtype.kind not in "iuUS":
        raise ValueError("IDs must be integers or strings")
    if len(np.unique(a)) != count or len(np.unique(b)) != count or not np.array_equal(a,b):
        raise ValueError("prediction/Gram IDs must be unique and identical in order")


def _difference(candidate, reference):
    with np.errstate(over="ignore", invalid="ignore"):
        error = candidate-reference
    if not np.isfinite(error).all():
        raise ValueError("pointwise error is outside finite float64 range")
    return error


def _norm_parts(values, *, rms=False):
    """Norm as a positive scale and order-one factor, or exact (0,0).

    Scaling precedes squaring. A largest scaled entry is exactly one, so
    the sum cannot vanish even if insignificant squared terms underflow.
    """
    scale = float(np.max(np.abs(values)))
    if scale == 0:
        return 0.0, 0.0
    scaled = values/scale
    factor = math.sqrt(float(np.sum(scaled*scaled)))
    if rms:
        factor /= math.sqrt(values.size)
    return scale, factor


def _positive_value(numerators, denominators=(), *, exponent_adjustment=0):
    """Combine a few positive factors without premature exponent loss."""
    mantissa, exponent = 1.0, exponent_adjustment
    for factors, inverse in ((numerators, False), (denominators, True)):
        for value in factors:
            part, shift = math.frexp(value)
            mantissa = mantissa/part if inverse else mantissa*part
            exponent += -shift if inverse else shift
    try:
        result = math.ldexp(mantissa, exponent)
    except OverflowError as exc:
        raise ValueError("diagnostic exceeds finite float64 range") from exc
    if not math.isfinite(result) or result == 0:
        raise ValueError("nonzero diagnostic is outside nonzero finite float64 range")
    return result


def _norm_value(parts):
    return 0.0 if parts[0] == 0 else _positive_value(parts)


def _relative(error_parts, reference_parts):
    # Zero scale here means all ORIGINAL stored entries are zero, not a
    # computed zero norm. Subtraction of unequal finite float64 entries cannot
    # round to zero; unrepresentable differences have already been rejected.
    if reference_parts[0] == 0:
        return 0.0 if error_parts[0] == 0 else None
    if error_parts[0] == 0:
        return 0.0
    return _positive_value(error_parts, reference_parts)


def _centered_unit(values):
    # Power-of-two rescaling preserves nearby large/tiny entries. Subtract
    # an anchor before averaging to avoid losing their small centered spread.
    _, exponent = math.frexp(float(np.max(np.abs(values))))
    scaled = np.ldexp(values, -exponent)
    shifted = scaled-scaled[0]
    centered = shifted-math.fsum(shifted)/len(shifted)
    scale, factor = _norm_parts(centered)
    if scale == 0:
        raise ValueError("nonconstant correlation variance is unresolved")
    return (centered/scale)/factor


def _correlation(candidate, reference):
    # Rounded centering must not turn stored constants (such as 0.1) into
    # nonconstant vectors. This check deliberately uses the original arrays.
    if np.all(candidate == candidate[0]) or np.all(reference == reference[0]):
        return None
    x, y = _centered_unit(candidate), _centered_unit(reference)
    products = x*y
    result = math.fsum(products)
    if result == 0 and np.any((x != 0) & (y != 0) & (products == 0)):
        raise ValueError("correlation is unresolved after product underflow")
    # Dot products of computed unit vectors can leave [-1,1] by roundoff.
    return float(np.clip(result, -1.0, 1.0))


def _seed_mean(values):
    """Column means without overflowing the sum or erasing tiny constants."""
    result = np.empty(values.shape[1])
    for j, column in enumerate(values.T):
        if np.all(column == column[0]):
            result[j] = column[0]
            continue
        _, exponent = math.frexp(float(np.max(np.abs(column))))
        scaled = np.ldexp(column, -exponent)
        if np.any((column != 0) & (scaled == 0)):
            raise ValueError("reference mean has unsupported exponent spread")
        total = math.fsum(scaled)
        result[j] = (0.0 if total == 0 else math.copysign(
            _positive_value((abs(total),), (float(len(column)),),
                            exponent_adjustment=exponent), total))
    return result


def _metrics(candidate, reference):
    if not len(candidate):
        return dict(count=0,rms=None,relative_rms=None,max_absolute=None,correlation=None,sign_disagreements=0)
    error = _difference(candidate,reference)
    error_parts = _norm_parts(error,rms=True)
    reference_parts = _norm_parts(reference,rms=True)
    return dict(count=len(candidate),rms=_norm_value(error_parts),
                relative_rms=_relative(error_parts,reference_parts),
                max_absolute=float(np.max(np.abs(error))),
                correlation=_correlation(candidate,reference),
                sign_disagreements=int(np.count_nonzero(np.sign(candidate)!=np.sign(reference))))


def prediction_metrics(candidate, reference, *, ids, reference_ids, labels=None, classes=None):
    """Unweighted per-image errors; sign(0)=0; constant correlations are null.

    labels may define within-class metrics. Explicit classes can include an
    absent class, represented by count zero and null-valued real diagnostics.
    """
    a,b = _real(candidate,"candidate",1),_real(reference,"reference",1)
    if a.shape != b.shape:
        raise ValueError("prediction shapes differ")
    _same_ids(ids,reference_ids,len(a))
    result = {"overall":_metrics(a,b)}
    if classes is not None and labels is None:
        raise ValueError("classes require labels")
    if labels is not None:
        labels = _real(labels,"labels",1)
        if labels.shape != a.shape:
            raise ValueError("labels must match samples")
        chosen = np.unique(labels) if classes is None else _real(classes,"classes",1)
        if len(np.unique(chosen)) != len(chosen):
            raise ValueError("duplicate classes")
        result["within_class"] = [{"label":float(k),**_metrics(a[labels==k],b[labels==k])} for k in chosen]
    return result


def all_seed_pairs(candidates, references, *, ids, reference_ids, labels=None):
    """Return every individual pair and each candidate versus reference mean.

    Seed axis is first, sample axis second; ranges are descriptive and are not
    confidence intervals. Equal seed indices do not imply coupled initializations.
    """
    a,b = _real(candidates,"candidates",2),_real(references,"references",2)
    if a.shape[1] != b.shape[1]:
        raise ValueError("sample counts differ")
    kw = dict(ids=ids,reference_ids=reference_ids,labels=labels)
    mean = _seed_mean(b)
    return dict(individual_pairs=[dict(candidate=i,reference=j,metrics=prediction_metrics(x,y,**kw))
                                  for i,x in enumerate(a) for j,y in enumerate(b)],
                reference_mean=[dict(candidate=i,metrics=prediction_metrics(x,mean,**kw))
                                for i,x in enumerate(a)])


def gram_metrics(candidate,reference,*,ids,reference_ids):
    """Compare uncentered activation Grams, or explicitly supplied cross Grams."""
    a,b = _real(candidate,"candidate Gram",2),_real(reference,"reference Gram",2)
    if a.shape != b.shape or a.shape[0] != a.shape[1]:
        raise ValueError("Grams must have equal square shape")
    _same_ids(ids,reference_ids,len(a))
    error = _difference(a,b)
    error_parts,reference_parts = _norm_parts(error),_norm_parts(b)
    return dict(frobenius=_norm_value(error_parts),
                relative_frobenius=_relative(error_parts,reference_parts),
                rms_entry=_norm_value(_norm_parts(error,rms=True)),
                max_absolute=float(np.max(np.abs(error))))


def match_training_loss(times, losses, target):
    """Nearest saved training loss, earliest-time tie; no interpolation.

    target must lie in the attained saved loss range (monotonicity is not
    assumed). Lower/upper loss brackets expose checkpoint sensitivity. Compare
    their predictions separately; this routine never sees passive predictions.
    """
    times,losses = _real(times,"times",1),_real(losses,"losses",1)
    if times.shape != losses.shape or np.any(np.diff(times)<=0) or times[0]<0 or np.any(losses<0):
        raise ValueError("times must increase from nonnegative values; losses must be nonnegative and match")
    if isinstance(target,(bool,np.bool_)) or not np.isscalar(target):
        raise ValueError("target must be a finite scalar")
    target = float(target)
    if not np.isfinite(target) or not losses.min() <= target <= losses.max():
        raise ValueError("target outside attained saved loss range; no extrapolation")
    index = int(np.argmin(np.abs(losses-target)))
    low_value = losses[losses<=target].max()
    high_value = losses[losses>=target].min()
    low,high = int(np.flatnonzero(losses==low_value)[0]),int(np.flatnonzero(losses==high_value)[0])
    mismatch = float(losses[index]-target)
    return dict(index=index,time=float(times[index]),loss=float(losses[index]),target=target,
                signed_mismatch=mismatch,absolute_mismatch=abs(mismatch),
                relative_mismatch=abs(mismatch)/target if target else (0.0 if mismatch==0 else None),
                lower_index=low,upper_index=high,lower_loss=float(low_value),upper_loss=float(high_value))
