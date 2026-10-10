from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
W = p.matrix("W", lower, upper)
z = W @ p.one(lower)
v = W.T @ p.phi(z)
dag = p.compile(p.inner(v, v), preactivations=[z])
print(dag.formula())
