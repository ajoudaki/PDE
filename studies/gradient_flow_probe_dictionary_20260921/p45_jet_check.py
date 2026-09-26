"""Finite Taylor-algebra checks through A(t)'s t**6 term; no training."""

import argparse
from fractions import Fraction
import hashlib
import importlib.util
from itertools import permutations
import json
from pathlib import Path
import sys

import numpy as np


SOURCE = Path(__file__).with_name("jet_check.py")
spec = importlib.util.spec_from_file_location("p45_original_jet", SOURCE)
oracle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oracle)


def compact(w, a, labels):
    """Direct coefficient formulas, using the full empirical initial Gram."""
    n = len(w)
    h = np.tanh(w)
    z = a @ h
    upper = np.tanh(z)
    p, d = 1-h*h, 1-upper*upper
    lower2, upper2 = -2*h*p, -2*upper*d
    upper3 = 2*d*(3*upper*upper-1)
    c1 = upper @ labels
    f1 = upper.T @ c1/n
    c2 = -upper @ f1/2
    f2 = upper.T @ c2/n
    u1, u2 = c1[:, None]*d, c2[:, None]*d
    r1 = u1*labels
    r2 = u2*labels-u1*f1
    a2, a3 = r1 @ h.T/(2*n), r2 @ h.T/(3*n)
    v1, v2 = a.T @ u1, a.T @ u2
    w2 = p*v1*labels/2
    w3 = p*(v2*labels-v1*f1)/3
    h2, h3 = p*w2, p*w3
    z2, z3 = a @ h2+a2 @ h, a @ h3+a3 @ h
    upper_h2, upper_h3 = d*z2, d*z3
    d2, d3 = upper2*z2, upper2*z3
    c3 = (upper_h2 @ labels-upper @ f2)/3
    f3 = (upper.T @ c3+upper_h2.T @ c1)/n
    c4 = (upper_h3 @ labels-upper_h2 @ f1-upper @ f3)/4
    f4 = (upper.T @ c4+upper_h2.T @ c2+upper_h3.T @ c1)/n
    u3 = c3[:, None]*d+c1[:, None]*d2
    u4 = c4[:, None]*d+c2[:, None]*d2+c1[:, None]*d3
    r3 = u3*labels-u2*f1-u1*f2
    r4 = u4*labels-u3*f1-u2*f2-u1*f3
    a4 = (r3 @ h.T+r1 @ h2.T)/(4*n)
    v3 = a.T @ u3+a2.T @ u1
    w4 = (p*(v3*labels-v2*f1-v1*f2)
          +lower2*w2*v1*labels)/4
    h4 = p*w4+lower2*w2*w2/2
    z4 = a @ h4+a2 @ h2+a4 @ h
    upper_h4 = d*z4+upper2*z2*z2/2
    d4 = upper2*z4+upper3*z2*z2/2
    c5 = (upper_h4 @ labels-upper_h3 @ f1
          -upper_h2 @ f2-upper @ f4)/5
    u5 = (c5[:, None]*d+c3[:, None]*d2
          +c2[:, None]*d3+c1[:, None]*d4)
    r5 = u5*labels-u4*f1-u3*f2-u2*f3-u1*f4
    a5 = (r4 @ h.T+r2 @ h2.T+r1 @ h3.T)/(5*n)
    a6 = (r5 @ h.T+r3 @ h2.T+r2 @ h3.T+r1 @ h4.T)/(6*n)
    return dict(a={2:a2, 3:a3, 4:a4, 5:a5, 6:a6},
                w={2:w2, 3:w3, 4:w4},
                c={1:c1, 2:c2, 3:c3, 4:c4, 5:c5},
                h={0:h, 2:h2, 3:h3, 4:h4},
                z={0:z, 2:z2, 3:z3, 4:z4},
                upper={0:upper, 2:upper_h2, 3:upper_h3, 4:upper_h4},
                f={1:f1, 2:f2, 3:f3, 4:f4}, d=d)


def full_jet(w0, a0, labels):
    """Independent full-vector-field series implementation from jet_check.py."""
    order, n = 6, len(w0)
    w = np.zeros((order+1, n, 2))
    a = np.zeros((order+1, n, n))
    c = np.zeros((order+1, n))
    w[0], a[0] = w0, a0
    x, weights = np.sqrt(2)*np.eye(2), np.full(2, 0.5)
    for k in range(order):
        dw, da, dc = oracle.vector_field(w, a, c, x, labels, weights)
        w[k+1], a[k+1], c[k+1] = dw[k]/(k+1), da[k]/(k+1), dc[k]/(k+1)
    h = oracle.tanh_series(w)
    z = oracle.mm(a, h)
    upper = oracle.tanh_series(z)
    f = oracle.mul(c[:, :, None], upper).mean(axis=1)
    velocity = oracle.vector_field(w, a, c, x, labels, weights)[1]
    return dict(w=w, a=a, c=c, h=h, z=z, upper=upper, f=f,
                middle_velocity=velocity)


def maximum_error(x, y):
    return float(np.max(np.abs(x-y)))


def compare(w, a, labels):
    expected, actual = compact(w, a, labels), full_jet(w, a, labels)
    errors = {}
    for name in ("a", "w", "c", "h", "z", "upper", "f"):
        errors[name] = {str(k):maximum_error(value, actual[name][k])
                        for k, value in expected[name].items()}
    errors["middle_velocity"] = {
        str(k-1):maximum_error(k*value, actual["middle_velocity"][k-1])
        for k, value in expected["a"].items()}
    maximum = max(value for group in errors.values() for value in group.values())
    assert maximum < 3e-12, errors
    gram = expected["upper"][0].T @ expected["upper"][0]/len(w)
    return dict(labels=labels.tolist(), width=len(w), upper_gram=gram.tolist(),
                errors=errors, maximum_error=maximum, status="PASS")


def ideal_initial(seed):
    """Finite fixtures satisfying both initial Gram identities exactly."""
    rng = np.random.default_rng(seed)
    signs = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
    h = np.vstack([0.3*signs, 0.6*signs])
    upper = np.vstack([0.4*signs[:, ::-1], -0.55*signs[:, ::-1]])
    n = len(h)
    v, tau = np.mean(h[:, 0]**2), np.mean(upper[:, 0]**2)
    z = np.arctanh(upper)
    projector = np.eye(n)-h @ h.T/(n*v)
    a = z @ h.T/(n*v)+(rng.normal(size=(n,n))/np.sqrt(n)) @ projector
    return np.arctanh(h), a, float(v), float(tau)


def ideal_checks(seed):
    w, a, v, tau = ideal_initial(seed)
    n = len(w)
    label_cases = [np.array(x, dtype=float) for x in
                   [(0.7,-1.1), (1.,0.), (0.,1.), (1.,1.), (1.,-1.), (0.,0.)]]
    checks = []
    for labels in label_cases:
        q = compact(w, a, labels)
        h, upper, d = q["h"][0], q["upper"][0], q["d"]
        cubic = (upper.T @ q["upper"][2] @ labels/3
                 +q["upper"][2].T @ upper @ labels)/n
        def l0(c, r):
            return ((c[:, None]*d)*r) @ h.T/n
        d2 = -2*upper*q["upper"][2]
        d4 = -2*upper*q["upper"][4]-q["upper"][2]**2
        def l2(c, r):
            return (((c[:, None]*d2)*r) @ h.T
                    +((c[:, None]*d)*r) @ q["h"][2].T)/n
        def l4(c, r):
            return (((c[:, None]*d4)*r) @ h.T
                    +((c[:, None]*d2)*r) @ q["h"][2].T
                    +((c[:, None]*d)*r) @ q["h"][4].T)/n
        predicted_a5 = (-2*tau*q["a"][4]+11*tau**3*q["a"][2]/12
                        -l0(upper @ cubic, labels)/20
                        -l0(upper @ labels, cubic)/5)
        kappa = 7*tau*tau/12
        quartic_a4 = q["a"][4]-kappa*q["a"][2]
        quartic_upper4 = q["upper"][4]-kappa*q["upper"][2]
        predicted_a6 = (31*tau**4*q["a"][2]/360
                        +13*tau*tau*quartic_a4/6
                        +tau*l0(upper @ cubic, labels)/10
                        +3*tau*l0(upper @ labels, cubic)/8
                        +l0(quartic_upper4 @ labels, labels)/30
                        +l2(q["upper"][2] @ labels, labels)/18
                        +(l4(upper @ labels,labels)
                          -kappa*l2(upper @ labels,labels))/6)
        errors = dict(
            lower_gram=maximum_error(h.T @ h/n, v*np.eye(2)),
            upper_gram=maximum_error(upper.T @ upper/n, tau*np.eye(2)),
            c2=maximum_error(q["c"][2], -tau*q["c"][1]/2),
            a3=maximum_error(q["a"][3], -tau*q["a"][2]),
            w3=maximum_error(q["w"][3], -tau*q["w"][2]),
            h3=maximum_error(q["h"][3], -tau*q["h"][2]),
            z3=maximum_error(q["z"][3], -tau*q["z"][2]),
            upper3=maximum_error(q["upper"][3], -tau*q["upper"][2]),
            a5_factor_closure=maximum_error(q["a"][5], predicted_a5),
            a6_collected_formula=maximum_error(q["a"][6], predicted_a6))
        assert max(errors.values()) < 3e-12, errors
        checks.append(dict(labels=labels.tolist(), errors=errors,
                           oracle_check=compare(w, a, labels), status="PASS"))
    # The recurrence proves the degree restriction; interpolation tests it
    # independently for this fixture without imposing it in compact().
    rng = np.random.default_rng(seed+10000)
    fit_labels = rng.uniform(-1,1,size=(40,2))
    test_labels = rng.uniform(-1,1,size=(12,2))
    degrees = {}
    fit_values = [compact(w,a,y) for y in fit_labels]
    test_values = [compact(w,a,y) for y in test_labels]
    for order, totals in ((2,(2,)), (3,(2,)), (4,(2,4)), (5,(2,4)), (6,(2,4,6))):
        monomials = [(j,total-j) for total in totals for j in range(total+1)]
        def vandermonde(labels):
            return np.array([[y[0]**p*y[1]**q for p,q in monomials] for y in labels])
        fit = np.stack([q["a"][order].reshape(-1) for q in fit_values])
        coeff, *_ = np.linalg.lstsq(vandermonde(fit_labels), fit, rcond=None)
        predicted = vandermonde(test_labels) @ coeff
        observed = np.stack([q["a"][order].reshape(-1) for q in test_values])
        error = maximum_error(predicted, observed)
        assert error < 3e-12, error
        degrees[str(order)] = dict(allowed_total_degrees=list(totals),
                                  held_out_maximum_error=error,
                                  coefficient_norm=float(np.linalg.norm(coeff)),
                                  status="PASS")
    return dict(seed=seed, v=v, tau=tau, cases=checks,
                label_polynomial_checks=degrees, status="PASS")


def sixth_order_novelty():
    """Exact rational leading determinant, plus a finite formula check."""
    xq = [Fraction(j,5) for j in range(1,5)]
    pq = [1-x*x for x in xq]
    vq = sum(x*x for x in xq)/8
    fourth_moment = sum(x**4 for x in xq)/8
    h_lambda3 = [-x**3/3 for x in xq]
    u_lambda2 = [x*p*p/2 for x,p in zip(xq,pq)]
    adjusted_k_lambda4 = [
        x*p**4/24-vq*x**3*p*p/6-fourth_moment*x*p*p/3-x**3*p**3/2
        for x,p in zip(xq,pq)]
    columns = [xq,h_lambda3,u_lambda2,adjusted_k_lambda4]
    determinant = Fraction(0)
    for perm in permutations(range(4)):
        inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = Fraction((-1)**inversions)
        for i,j in enumerate(perm):
            term *= columns[j][i]
        determinant += term
    assert determinant == Fraction(1008,244140625), determinant
    x = np.array([float(q) for q in xq])
    h = np.zeros((8,2))
    h[:4,0], h[4:,1] = x,x
    w, a = np.arctanh(h), np.eye(8)
    q = compact(w,a,np.array([1.,0.]))
    upper, p = np.tanh(x), 1-x*x
    d = 1-upper*upper
    b = upper*d
    u = b*p*p/2
    v, tau = float(vq), float(np.sum(upper*upper)/8)
    e = upper*d*d*(p*p+v)/2
    beta = np.sum(b*b)/8
    k = p*p*e*(1-7*upper*upper)/12+beta*x*p*p/8-x*b*b*p**3/2
    actual_k = q["h"][4][:4,0]-7*tau*tau*q["h"][2][:4,0]/12
    k_error = maximum_error(k,actual_k)
    assert k_error < 3e-12, k_error
    old_block = np.column_stack((x,upper,u))
    old = np.zeros((8,6))
    old[:4,:3], old[4:,3:] = old_block,old_block
    orthonormal, _ = np.linalg.qr(old)
    complement = np.eye(8)-orthonormal @ orthonormal.T
    a6_residual = float(np.linalg.norm(q["a"][6] @ complement))
    assert a6_residual > 1e-9, a6_residual
    prior_errors = {}
    for labels in (np.array([1.,0.]),np.array([0.,1.]),np.array([1.,1.]),np.array([1.,-1.])):
        local = compact(w,a,labels)
        for order in range(2,6):
            key = f"order_{order}_labels_{labels.tolist()}"
            prior_errors[key] = float(np.linalg.norm(local["a"][order] @ complement))
    assert max(prior_errors.values()) < 3e-12, prior_errors
    return dict(status="PASS", v=str(vq),
                exact_determinant_leading_power=9,
                exact_determinant_leading_coefficient=str(determinant),
                determinant_column_order=["x","H","u","k"],
                finite_lambda=1, hidden_fourth_order_formula_error=k_error,
                middle_sixth_order_outside_old_right_space_norm=a6_residual,
                prior_right_space_residuals=prior_errors,
                scope="Algebraic exact-Gram counterexample, not an iid-population limit")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    finite = []
    for seed,n,labels in [(7101,7,[.7,-1.1]), (7103,9,[-.5,.8]),
                          (7109,11,[1.,0.]), (7111,7,[0.,0.])]:
        rng = np.random.default_rng(seed)
        w = rng.normal(size=(n,2))
        a = rng.normal(size=(n,n))/np.sqrt(n)
        result = compare(w,a,np.array(labels))
        result["seed"] = seed
        finite.append(result)
    payload = dict(purpose="Deterministic Taylor-algebra verification; no training or width-limit claim",
                   normalization="physical inputs sqrt(2)*e_a; equal probe weights 1/2",
                   coefficient_convention="ordinary Taylor powers, no factorials",
                   middle_position_orders=list(range(2,7)),
                   middle_velocity_orders=list(range(1,6)),
                   python=sys.version, numpy=np.__version__,
                   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   oracle_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                   tolerance=3e-12, finite_empirical_gram_cases=finite,
                   ideal_gram_checks=ideal_checks(7201),
                   sixth_order_factor_novelty=sixth_order_novelty(), status="PASS")
    output = Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open("x") as stream:
        json.dump(payload,stream,indent=2)
        stream.write("\n")
    print(json.dumps(dict(status=payload["status"], output=str(output),
                          finite_cases=len(finite), ideal_cases=len(payload["ideal_gram_checks"]["cases"]))))


if __name__ == "__main__":
    main()
