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
