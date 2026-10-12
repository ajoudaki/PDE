"""Independent exact ODE check of general moving-flow and scalar-feedback AD.

Run from the checkout root with Python -B.  For O=mean(x^2), loss=O^2/4
and vector mobility n, x_dot=-O*x, hence O_dot=-2*O^2.  Consequently
O(t)=O(0)/(1+2*O(0)*t) and its factorial-normalized coefficient is
(-2)^r O(0)^(r+1).  Standard Gaussian roots have limiting O(0)=1.
"""
from fractions import Fraction as F
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "paper_MFP/code"))
from pde.mfp_compiler import Program
from pde.mfp_finite import evaluate_finite
from pde import mfp_expr as ex

p = Program()
x = p.root("x", p.vector_type("neurons"))
observable = p.mean(x*x)
loss = observable*observable/4
velocity = -p.gradient(loss, vectors=[x])[x]
jets = p.jets(observable, {x: velocity}, order=6, moving=True)
initial = [F(1, 2), F(-2, 3), F(4, 5)]
initial_observable = sum(v*v for v in initial)/3
for order, jet in enumerate(jets):
    value = evaluate_finite(jet, 3, {x: initial}, {})
    expected = (-2)**order * initial_observable**(order+1)
    limit = p.compile(jet).output
    assert value == expected, (order, value, expected)
    assert str(limit) == str((-2)**order), (order, limit)
    print(order, "finite exact ODE identity passed; Gaussian limit", limit)

# One original preactivation depending on five shared input-column roots.
# Two applications of Stein give E[U0^2 F(Z)] = E[F(Z)] + a0^2 E[F''(Z)].
# For F=(phi'')^3, F''=6 phi''(phi''')^2+3(phi'')^2 phi''''.
p = Program()
kind = p.vector_type("layer1")
columns = [p.root("U"+str(j), kind) for j in range(5)]
coefficients = [p.parameter("a"+str(j)) for j in range(5)]
z = sum((a*u for a, u in zip(coefficients, columns)), p.zero(kind))
dag = p.compile(p.mean(columns[0]**2*p.phi(z, 2)**3), preactivations=[z])
assert len(dag.sources) == 5
assert len(dag.expectations) == 3
assert all(len(atom.coordinates) == 1 for atom in dag.expectations)
coordinate = dag.expectations[0].coordinates[0]
variance = sum((ex.symbol("s_a"+str(j))**2 for j in range(5)), ex.const(0))
assert all(atom.coordinates == (coordinate,) and atom.covariance == ((variance,),)
           for atom in dag.expectations)
by_integrand = {atom.integrand: atom.symbol for atom in dag.expectations}
zeroth = by_integrand[ex.phi(coordinate, 2)**3]
third = by_integrand[ex.phi(coordinate, 2)*ex.phi(coordinate, 3)**2]
fourth = by_integrand[ex.phi(coordinate, 2)**2*ex.phi(coordinate, 4)]
expected = zeroth+ex.symbol("s_a0")**2*(6*third+3*fourth)
assert ex.expand(dag.output-expected) == ex.const(0)
print("Rebasing: 5 retained root sources; 3 activation atoms of dimension 1; exact Stein identity passed.")
