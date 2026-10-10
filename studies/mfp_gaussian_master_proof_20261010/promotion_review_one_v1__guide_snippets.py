from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
W = p.matrix("W", lower, upper)
z = W @ p.one(lower)
v = W.T @ p.phi(z)
dag = p.compile(p.inner(v, v), preactivations=[z])
print(dag.formula())


from pde.mfp_compiler import Program

p = Program()
kind = p.vector_type("neurons")
x = p.root("x", kind)
O, V = p.mean(x**2), -(x**3)
frozen = p.derivatives(O, {x: V}, order=2)
moving = p.derivatives(O, {x: V}, order=2, moving=True)
assert str(p.compile(frozen[2]).output) == "30"
assert str(p.compile(moving[2]).output) == "120"
assert str(p.compile(p.jets(O, {x: V}, 2, moving=True)[2]).output) == "60"


from pde.mfp_compiler import Program

p = Program()
x = p.root("x", p.vector_type("neurons"))
jet = p.curve_jets(p.mean(x**2), {x: (x**2, -x)}, order=2)
assert str(p.compile(jet[2]).output) == "1"  # E[x**4-2*x**2]


from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
x = p.root("x", lower)
W = p.matrix("W", lower, upper)
loss = p.mean((W @ x)**2)
state = p.gradient_descent(loss, vectors=[x], matrices=[W], steps=2, step_size=0.01)
updated_loss = p.at(loss, state)
print(p.compile(updated_loss).formula())


from fractions import Fraction
from pde.mfp_compiler import Program
from pde.mfp_finite import evaluate_finite

p = Program()
x = p.root("x", p.vector_type("neurons"))
O = p.mean(x**2)
assert evaluate_finite(O, 2, {x: [Fraction(1, 2), Fraction(3, 2)]}, {}) == Fraction(5, 4)
