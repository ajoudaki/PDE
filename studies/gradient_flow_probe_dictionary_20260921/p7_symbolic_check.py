"""Exact formal K3/M/P collection audit; no training or empirical fitting.

Run with an environment providing SymPy, e.g. the local conda base Python.
The formal rank is not a proof of Gaussian-population minimality.
"""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def fields(beta_mode):
    y = sp.symbols("y1 y2")
    h = sp.symbols("H1 H2")
    ff = sp.symbols("F11 F12 F21 F22")
    d = [1 - z*z for z in h]
    e = [-2*h[a]*d[a] for a in range(2)]
    ss = sum(y[a]*h[a] for a in range(2))
    r = [y[a]*sum(y[b]*ff[2*a+b] for b in range(2))/2 for a in range(2)]
    j = sum(y[a]*d[a]*r[a] for a in range(2))
    k3 = [d[a]*j/3 + ss*e[a]*r[a] for a in range(2)]
    beta = ([y[a]**3 for a in range(2)] if beta_mode == "anisotropic"
            else [y[a]*(y[0]**2+y[1]**2) for a in range(2)])
    bb = sum(beta[a]*h[a] for a in range(2))
    zz = [-y[a]*sum(beta[b]*ff[2*a+b] for b in range(2))/20
          -beta[a]*sum(y[b]*ff[2*a+b] for b in range(2))/5 for a in range(2)]
    zp = [y[a]*sum(beta[b]*ff[2*a+b] for b in range(2))/10
          +sp.Rational(3, 8)*beta[a]*sum(y[b]*ff[2*a+b] for b in range(2))
          for a in range(2)]
    mm = [d[a]*sum(y[b]*d[b]*zz[b]-beta[b]*d[b]*r[b] for b in range(2))/6
          -bb*e[a]*r[a]/4+ss*e[a]*zz[a] for a in range(2)]
    pp = [d[a]*sum(y[b]*d[b]*(zp[b]-zz[b])
                    +sp.Rational(11, 4)*beta[b]*d[b]*r[b] for b in range(2))/7
          +sp.Rational(3, 5)*bb*e[a]*r[a]
          +ss*e[a]*(zp[a]-zz[a]/2) for a in range(2)]
    def coefficients(values, degree):
        return [sp.Poly(f, *y).coeff_monomial(y[0]**(degree-j)*y[1]**j)
                for f in values for j in range(degree+1)]
    return dict(k3=coefficients(k3, 3), m=coefficients(mm, 5),
                p=coefficients(pp, 5), variables=(*h, *ff))


def coefficient_matrix(polynomials, variables):
    polys = [sp.Poly(f, *variables) for f in polynomials]
    monomials = sorted(set(m for f in polys for m in f.monoms()))
    return sp.Matrix([[f.coeff_monomial(m) for f in polys] for m in monomials])


def check():
    anis = fields("anisotropic")
    radial = fields("radial")
    full = anis["k3"]+anis["m"]+anis["p"]
    matrix = coefficient_matrix(full, anis["variables"])
    _, pivots = matrix.rref()
    assert pivots == (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 16, 21, 28), pivots
    ranks = [matrix[:, :n].rank() for n in (8, 20, 32)]
    assert ranks == [8, 12, 14], ranks
    basis = matrix[:, list(pivots)]
    solution, parameters = basis.gauss_jordan_solve(matrix)
    assert parameters.rows == 0
    assert basis*solution == matrix
    radial_matrix = coefficient_matrix(radial["k3"]+radial["m"]+radial["p"],
                                       radial["variables"])
    assert radial_matrix.rank() == 8
    return dict(status="PASS", arithmetic="exact rational SymPy coefficients",
                ranks=dict(K3=8, K3_and_M=12, K3_M_P=14, radial_beta=8),
                pivot_indices_zero_based=list(pivots),
                M_pivots_axis_one_based_j_zero_based=[[1, 1], [1, 2], [2, 3], [2, 4]],
                P_pivots_axis_one_based_j_zero_based=[[1, 1], [2, 4]],
                basis_reconstruction_exact=True,
                coordinate_matrix=[[str(solution[i, j]) for j in range(solution.cols)]
                                   for i in range(solution.rows)],
                limits="Formal independent F_ab symbols; no Gaussian minimality or training claim")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = check()
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["sympy_version"] = sp.__version__
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "output": str(output),
                      "ranks": result["ranks"]}))


if __name__ == "__main__":
    main()
