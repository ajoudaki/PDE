from pde.mfp_compiler import Program

p = Program()
lower, upper = p.vector_type("lower"), p.vector_type("upper")
x = p.root("x", lower)
W = p.matrix("W", lower, upper)
loss = p.mean((W @ x)**2)
state = p.gradient_descent(loss, vectors=[x], matrices=[W], steps=2, step_size=0.01)
updated_loss = p.at(loss, state)
print(p.compile(updated_loss).formula())
