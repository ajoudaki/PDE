from pde.mfp_compiler import Program

p = Program()
x = p.root("x", p.vector_type("neurons"))
jet = p.curve_jets(p.mean(x**2), {x: (x**2, -x)}, order=2)
assert str(p.compile(jet[2]).output) == "1"  # E[x**4-2*x**2]
