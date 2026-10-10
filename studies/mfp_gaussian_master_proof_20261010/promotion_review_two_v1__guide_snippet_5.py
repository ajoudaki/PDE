from fractions import Fraction
from pde.mfp_compiler import Program
from pde.mfp_finite import evaluate_finite

p = Program()
x = p.root("x", p.vector_type("neurons"))
O = p.mean(x**2)
assert evaluate_finite(O, 2, {x: [Fraction(1, 2), Fraction(3, 2)]}, {}) == Fraction(5, 4)
