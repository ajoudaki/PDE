"""Exact finite Taylor algebra through A[t^8], evaluated in float64 on CPU.

Physical probes sqrt(2)*e_a, weights 1/2, zero c(0), ordinary Taylor powers.
Full moving residuals, lower/middle/readout blocks, and both gates are kept.
No population moment substitutions, label interpolation, or finite differences.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


def _time_product(a, b, operation=np.multiply):
    return np.stack([sum(operation(a[j], b[k-j]) for j in range(k+1))
                     for k in range(len(a))])


def _tanh_series(x):
    """y'=x'(1-y^2), solved coefficient by coefficient."""
    y = np.zeros_like(x)
    y[0] = np.tanh(x[0])
    for k in range(1, len(x)):
        for j in range(1, k+1):
            m = k-j
            gate = -sum(y[q]*y[m-q] for q in range(m+1))
            if m == 0:
                gate += 1
            y[k] += j*x[j]*gate/k
    return y


def vector_field(w, a, c, labels):
    """Full normalized-axis vector field on arrays with time as first axis."""
    n = w.shape[1]
    h = _tanh_series(w)
    z = _time_product(a, h, np.matmul)
    upper = _tanh_series(z)
    lower_gate, upper_gate = -_time_product(h, h), -_time_product(upper, upper)
    lower_gate[0] += 1
    upper_gate[0] += 1
    f = _time_product(c[:, :, None], upper).mean(axis=1)
    b = -f.copy()
    b[0] += labels
    cgate = _time_product(c[:, :, None], upper_gate)
    reverse = _time_product(a.transpose(0, 2, 1), cgate, np.matmul)
    weighted_cgate = _time_product(b[:, None, :], cgate)
    dw = _time_product(b[:, None, :], _time_product(lower_gate, reverse))
    da = _time_product(weighted_cgate, h.transpose(0, 2, 1), np.matmul)/n
    dc = _time_product(b[:, None, :], upper).sum(axis=2)
    return dict(w=w, a=a, c=c, h=h, z=z, upper=upper, f=f, b=b,
                lower_gate=lower_gate, upper_gate=upper_gate,
                cgate=cgate, reverse=reverse, lower_velocity=dw,
                middle_velocity=da, readout_velocity=dc)


def _validate(w0, a0, order):
    w0, a0 = np.asarray(w0, dtype=np.float64), np.asarray(a0, dtype=np.float64)
    if w0.ndim != 2 or w0.shape[1] != 2 or w0.shape[0] < 1:
        raise ValueError('w0 must have shape (n,2), n>=1')
    if a0.shape != (len(w0), len(w0)):
        raise ValueError('a0 must have shape (n,n)')
    if not np.isfinite(w0).all() or not np.isfinite(a0).all():
        raise ValueError('initial state must be finite')
    if isinstance(order, bool) or not isinstance(order, int) or not 1 <= order <= 8:
        raise ValueError('order must be an integer from 1 through 8')
    return w0, a0


def full_jet(w0, a0, labels, order=8):
    """Return coefficient arrays J[name][k]=[t^k]name through order<=8.

    `w` is the first weight/lower preactivation, `a` the stored canonical
    middle matrix (outer-product normalization 1/n), `cgate=c*(1-upper^2)`.
    `b=y-f` has the positive-residual convention. Velocities through
    order-1 are completely determined; their last entry is also returned.
    """
    w0, a0 = _validate(w0, a0, order)
    labels = np.asarray(labels, dtype=np.float64)
    if labels.shape != (2,) or not np.isfinite(labels).all():
        raise ValueError('labels must be two finite numbers')
    n = len(w0)
    w, a = np.zeros((order+1, n, 2)), np.zeros((order+1, n, n))
    c = np.zeros((order+1, n))
    w[0], a[0] = w0, a0
    for k in range(order):
        q = vector_field(w[:k+1], a[:k+1], c[:k+1], labels)
        w[k+1] = q['lower_velocity'][k]/(k+1)
        a[k+1] = q['middle_velocity'][k]/(k+1)
        c[k+1] = q['readout_velocity'][k]/(k+1)
    return vector_field(w, a, c, labels)


# Sparse label polynomials use exact exponent bookkeeping, not fitted values.
# p[(i,j)] is the array coefficient of y1^i*y2^j; an empty dict is zero.
def _p_add(*args):
    out = {}
    for p in args:
        for key, value in p.items():
            if key in out:
                out[key] = out[key]+value
            else:
                out[key] = value.copy()
    return {key:value for key,value in out.items() if np.any(value)}


def _p_map(p, fn):
    return {key:fn(value) for key,value in p.items()}


def _p_scale(p, scalar):
    return _p_map(p, lambda a: scalar*a)


def _p_product(p, q, operation=np.multiply):
    out = {}
    for (i,j), left in p.items():
        for (k,l), right in q.items():
            key = (i+k,j+l)
            value = operation(left, right)
            out[key] = out.get(key, 0)+value
    return {key:value for key,value in out.items() if np.any(value)}


def _s_product(a, b, operation=np.multiply):
    return [_p_add(*(_p_product(a[j], b[k-j], operation) for j in range(k+1)))
            for k in range(len(a))]


def _s_map(a, fn):
    return [_p_map(p, fn) for p in a]


def _s_tanh(x):
    if set(x[0]) != {(0,0)}:
        raise ValueError('tanh expansion requires a label-independent base')
    y = [{(0,0):np.tanh(x[0][(0,0)])}]+[{} for _ in x[1:]]
    one = {(0,0):np.ones_like(x[0][(0,0)])}
    for k in range(1, len(x)):
        acc = {}
        for j in range(1, k+1):
            m = k-j
            gate = _p_scale(_p_add(*(_p_product(y[q], y[m-q])
                                    for q in range(m+1))), -1)
            if m == 0:
                gate = _p_add(gate, one)
            acc = _p_add(acc, _p_scale(_p_product(x[j], gate), j/k))
        y[k] = acc
    return y


def _polynomial_vector_field(w, a, c):
    n = len(w[0][(0,0)])
    h = _s_tanh(w)
    z = _s_product(a, h, np.matmul)
    upper = _s_tanh(z)
    lower_gate = _s_map(_s_product(h, h), lambda value:-value)
    upper_gate = _s_map(_s_product(upper, upper), lambda value:-value)
    lower_gate[0] = _p_add(lower_gate[0], {(0,0):np.ones((n,2))})
    upper_gate[0] = _p_add(upper_gate[0], {(0,0):np.ones((n,2))})
    cc = _s_map(c, lambda value:value[:,None])
    f = _s_map(_s_product(cc, upper), lambda value:value.mean(axis=0))
    b = _s_map(f, lambda value:-value)
    b[0] = _p_add(b[0], {(1,0):np.array([1.,0.]), (0,1):np.array([0.,1.])})
    bb = _s_map(b, lambda value:value[None,:])
    cgate = _s_product(cc, upper_gate)
    reverse = _s_product(_s_map(a, np.transpose), cgate, np.matmul)
    dw = _s_product(bb, _s_product(lower_gate, reverse))
    da = _s_map(_s_product(_s_product(bb, cgate), _s_map(h, np.transpose), np.matmul),
                lambda value:value/n)
    dc = _s_map(_s_product(bb, upper), lambda value:value.sum(axis=1))
    return dict(w=w, a=a, c=c, h=h, z=z, upper=upper, f=f, b=b,
                lower_gate=lower_gate, upper_gate=upper_gate,
                cgate=cgate, reverse=reverse, lower_velocity=dw,
                middle_velocity=da, readout_velocity=dc)


def full_polynomial_jet(w0, a0, order=8):
    """Return J[name][k][(i,j)] = [t^k y1^i y2^j]name, without interpolation.

    Every coefficient is an ndarray. Missing monomials are identically zero.
    Initial labels remain symbolic, including all lower homogeneous degrees.
    """
    w0, a0 = _validate(w0, a0, order)
    w, a = [{(0,0):w0.copy()}]+[{} for _ in range(order)], [{(0,0):a0.copy()}]+[{} for _ in range(order)]
    c = [{} for _ in range(order+1)]
    for k in range(order):
        q = _polynomial_vector_field(w[:k+1], a[:k+1], c[:k+1])
        w[k+1] = _p_scale(q['lower_velocity'][k], 1/(k+1))
        a[k+1] = _p_scale(q['middle_velocity'][k], 1/(k+1))
        c[k+1] = _p_scale(q['readout_velocity'][k], 1/(k+1))
    return _polynomial_vector_field(w, a, c)


def _field_shape(jet, name):
    n = len(jet['w'][0][(0,0)])
    if name in ('a', 'middle_velocity'):
        return n,n
    if name in ('c', 'readout_velocity'):
        return (n,)
    if name in ('f', 'b'):
        return (2,)
    return n,2


def label_degree(jet, name, time_power, total_degree):
    """Dense table with final axis j multiplying y1^(degree-j)*y2^j.

    Shape examples: h/cgate -> (n,2,degree+1), a -> (n,n,degree+1).
    This extracts one homogeneous part and retains its zero coefficients.
    """
    if total_degree < 0 or time_power < 0:
        raise ValueError('powers must be nonnegative')
    p = jet[name][time_power]
    shape = _field_shape(jet, name)
    return np.stack([p.get((total_degree-j,j), np.zeros(shape))
                     for j in range(total_degree+1)], axis=-1)


def evaluate_polynomial_jet(jet, labels):
    labels = np.asarray(labels, dtype=np.float64)
    if labels.shape != (2,) or not np.isfinite(labels).all():
        raise ValueError('labels must be two finite numbers')
    result = {}
    for name, series in jet.items():
        shape = _field_shape(jet, name)
        result[name] = np.stack([sum((labels[0]**i*labels[1]**j*value
                                     for (i,j),value in p.items()), np.zeros(shape))
                                 for p in series])
    return result


def _error(left, right):
    if not np.isfinite(left).all() or not np.isfinite(right).all():
        raise AssertionError('nonfinite check quantity')
    return float(np.max(np.abs(left-right))/max(1., float(np.max(np.abs(right)))))


def _derivative(a):
    return np.arange(1, len(a)).reshape((-1,)+(1,)*(a.ndim-1))*a[1:]


def _composition_errors(q):
    """Substitute into independently differentiated derived-field equations."""
    h, H = q['h'][:-1], q['upper'][:-1]
    ell, d = q['lower_gate'][:-1], q['upper_gate'][:-1]
    dw, da, dc = (q[name][:-1] for name in
                  ('lower_velocity','middle_velocity','readout_velocity'))
    hdot = _time_product(q['b'][:-1,None,:],
                        _time_product(_time_product(ell,ell), q['reverse'][:-1]))
    zdot = (_time_product(da,h,np.matmul)
            +_time_product(q['a'][:-1],hdot,np.matmul))
    Hdot = _time_product(d,zdot)
    elldot, ddot = -2*_time_product(h,hdot), -2*_time_product(H,Hdot)
    fdot = (_time_product(dc[:,:,None],H)
            +_time_product(q['c'][:-1,:,None],Hdot)).mean(axis=1)
    udot = (_time_product(dc[:,:,None],d)
            +_time_product(q['c'][:-1,:,None],ddot))
    rhs = dict(w=dw,a=da,c=dc,h=hdot,z=zdot,upper=Hdot,
               lower_gate=elldot,upper_gate=ddot,f=fdot,b=-fdot,cgate=udot)
    return {name:_error(_derivative(q[name]),value) for name,value in rhs.items()}


def _load_file(name):
    path = Path(__file__).with_name(name+'.py')
    spec = importlib.util.spec_from_file_location('p7_check_'+name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _degree_support(polynomial):
    return {name:{str(k):sorted({i+j for i,j in p}) for k,p in enumerate(series)}
            for name,series in polynomial.items()}


def check_case(seed, n, labels, output):
    rng = np.random.default_rng(seed)
    w0, a0 = rng.normal(size=(n,2)), rng.normal(size=(n,n))/np.sqrt(n)
    labels = np.asarray(labels, dtype=float)
    q = full_jet(w0,a0,labels)
    polynomial = full_polynomial_jet(w0,a0)
    errors = {'composition_ODE':_composition_errors(q)}
    legacy, compact = _load_file('jet_check'), _load_file('p45_jet_check')
    oldw, olda, oldc = np.zeros_like(q['w']), np.zeros_like(q['a']), np.zeros_like(q['c'])
    oldw[0], olda[0] = w0,a0
    for k in range(8):
        dw, da, dc = legacy.vector_field(oldw,olda,oldc,np.sqrt(2)*np.eye(2),labels,np.full(2,.5))
        oldw[k+1], olda[k+1], oldc[k+1] = dw[k]/(k+1),da[k]/(k+1),dc[k]/(k+1)
    errors['independent_general_input_oracle'] = {
        name:_error(q[name],value) for name,value in zip(('w','a','c'),(oldw,olda,oldc))}
    old = compact.compact(w0,a0,labels)
    errors['existing_closed_formulas'] = {
        f'{name}_{k}':_error(q[name][k],value)
        for name in ('a','w','c','h','z','upper','f') for k,value in old[name].items()}
    h,H,d,ell = q['h'][0],q['upper'][0],q['upper_gate'][0],q['lower_gate'][0]
    c1 = H@labels
    direct_h2 = labels*ell**2*(a0.T@(c1[:,None]*d))/2
    direct_a2 = (labels*c1[:,None]*d)@h.T/(2*n)
    errors['normalization'] = dict(c1=_error(q['c'][1],c1),
                                 a2=_error(q['a'][2],direct_a2),h2=_error(q['h'][2],direct_h2))
    odd = {'c','f','b','cgate','reverse','readout_velocity'}
    negative = full_jet(w0,a0,-labels)
    errors['label_sign_parity'] = {name:_error(negative[name],(-1 if name in odd else 1)*value)
                                   for name,value in q.items()}
    for sign in (1,-1):
        evaluated = evaluate_polynomial_jet(polynomial,sign*labels)
        numeric = q if sign == 1 else negative
        errors[f'polynomial_evaluation_sign_{sign}'] = {
            name:_error(evaluated[name],numeric[name]) for name in q}
    zero = full_jet(w0,a0,np.zeros(2))
    errors['zero_label_stationarity'] = {name:float(np.max(np.abs(zero[name][1:])))
                                         for name in ('w','a','c','h','z','upper','f','cgate')}
    # All coefficients must have the exact parity forced by y -> -y.
    support = _degree_support(polynomial)
    for name,series in polynomial.items():
        for k,p in enumerate(series):
            for i,j in p:
                assert (i+j)%2 == (1 if name in odd else 0), (name,k,i,j)
    # Position degree cannot exceed its time order; initial values have degree 0.
    for name in ('w','a','c','h','z','upper','f','lower_gate','upper_gate','cgate'):
        for k,p in enumerate(polynomial[name]):
            assert all(i+j <= k for i,j in p), (name,k)
    moving_norms = {f'{name}_{k}':float(np.linalg.norm(q[name][k]))
                    for name,k in (('w',2),('a',2),('c',1),('h',6),('cgate',7),('a',8),('f',3))}
    assert min(moving_norms.values()) > 1e-12, moving_norms
    maximum = max(value for group in errors.values() for value in group.values())
    assert maximum < 3e-12, errors
    # Store ordinary numeric coefficients and symbolic tables for replay.
    numeric_path = output/f'case_{seed}_numeric.npz'
    np.savez_compressed(numeric_path,labels=labels,**q)
    tables = {f'{name}__t{k}__degree{degree}':label_degree(polynomial,name,k,degree)
              for name,series in support.items() for k0,degrees in series.items()
              for k in (int(k0),) for degree in degrees}
    polynomial_path = output/f'case_{seed}_polynomial.npz'
    np.savez_compressed(polynomial_path,**tables)
    degree_norms = {f'{name}_t{k}':{str(degree):float(np.linalg.norm(label_degree(polynomial,name,k,degree)))
                                  for degree in support[name][str(k)]}
                    for name,k in (('a',8),('h',6),('cgate',7))}
    return dict(seed=seed,width=n,labels=labels.tolist(),errors=errors,
                maximum_normalized_absolute_error=maximum,moving_block_norms=moving_norms,
                degree_support=support,requested_coefficient_degree_norms=degree_norms,
                numeric_coefficients=str(numeric_path),polynomial_coefficients=str(polynomial_path),status='PASS')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,required=True)
    args = parser.parse_args()
    output = args.output_dir
    output.mkdir(parents=True,exist_ok=True)
    result_path = output/'results.json'
    if result_path.exists():
        raise FileExistsError('results are frozen; select a fresh output directory')
    for seed in (8101,8107):
        if any((output/f'case_{seed}_{kind}.npz').exists() for kind in ('numeric','polynomial')):
            raise FileExistsError('coefficient archives already exist')
    inputs = ('jet_check.py','p45_jet_check.py','DERIVATION.md','P45_DERIVATION_ROUTE.md',
              'new_dictionary.py','new_dictionary_p45.py')
    payload = dict(status='PASS',purpose='Independent exact finite Taylor algebra; no training or population claim',
                   normalization='physical sqrt(2)e_a, equal weights 1/2, unhalved MSE, zero readout',
                   coefficient_convention='ordinary Taylor powers and exact label-monomial bookkeeping',
                   maximum_position_order=8,tolerance=3e-12,python=sys.version,numpy=np.__version__,
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   input_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                 for name in inputs},
                   cases=[check_case(8101,5,[.7,-1.1],output),check_case(8107,7,[-.6,.9],output)])
    with result_path.open('x') as stream:
        json.dump(payload,stream,indent=2,allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(status='PASS',results=str(result_path),
                          maximum_normalized_absolute_error=max(case['maximum_normalized_absolute_error']
                                                                for case in payload['cases']))))


if __name__ == '__main__':
    main()
