# Symbolic geometry and labels in final-layer kernel jets

The executable [symbolic_kernel_jets.py](symbolic_kernel_jets.py) constructs two hidden layers plus a readout, accepts symbolic input coordinates and labels, and computes the initialization jets of the last hidden layer's feature kernel along the full gradient flow. The existing compiler is used without modification. The code preserves the shared first-layer parameters instead of treating each sample's preactivation as an unrelated trainable vector.

## Geometry, model and training time

There are two samples and two input coordinates, \(m=d=2\). Choose fixed real symbolic numbers \(\alpha,\beta,\gamma,y_1,y_2\), and define the normalized input coordinates by

\[
\frac{x_1}{\sqrt2}=(\alpha,0)^\top,\qquad
\frac{x_2}{\sqrt2}=(\beta,\gamma)^\top.
\]

Their input Gram is

\[
Q_{ab}:=\frac{x_a^\top x_b}{2},\qquad
Q=\begin{pmatrix}\alpha^2&\alpha\beta\\
\alpha\beta&\beta^2+\gamma^2\end{pmatrix}.
\]

This is a symbolic positive-semidefinite family, including singular cases. Every positive-semidefinite two-by-two matrix has such a factorization, although converting arbitrary symbolic covariance entries into factors is not an operation of the current interface. Here the factors themselves are the supplied symbolic geometry.

Write \(U,V\in\mathbb R^n\) for the two columns of \(W^{(1)}\), \(W^{(2)}\in\mathbb R^{n\times n}\) for the hidden matrix, and \(W^{(3)}\in\mathbb R^n\) for the readout. All initialization entries are independent, with

\[
U_i,V_i,W_i^{(3)}\sim N(0,1),\qquad W_{ij}^{(2)}\sim N(0,1/n).
\]

The readout is explicitly order one, rather than the book's small-readout initialization. There are no biases. The forward pass is

\[
\begin{aligned}
z_1^{(1)}&=\alpha U,&z_2^{(1)}&=\beta U+\gamma V,\\
h_a^{(1)}&=\phi(z_a^{(1)}),&
z_a^{(2)}&=W^{(2)}h_a^{(1)},\\
h_a^{(2)}&=\phi(z_a^{(2)}),&
f_{n,a}&=\frac1nW^{(3)\top}h_a^{(2)}.
\end{aligned}
\]

For generic activation output, \(\phi\) is smooth and every derivative has polynomial growth, as required by the study's theorem. Labels are fixed symbolic parameters. The loss and physical flow are

\[
\mathcal L_n=\frac1{2m}\sum_{a=1}^m(f_{n,a}-y_a)^2,\quad
\dot U=-n\nabla_U\mathcal L_n,\quad
\dot V=-n\nabla_V\mathcal L_n,\quad
\dot W^{(2)}=-\nabla_{W^{(2)}}\mathcal L_n,\quad
\dot W^{(3)}=-n\nabla_{W^{(3)}}\mathcal L_n.
\]

The factor \(1/(2m)\) is part of the clock convention. Geometry and labels stay fixed. Both hidden layers and the readout train.

The final-layer kernel means

\[
K_{n,ab}(t):=\frac1n h_a^{(2)}(t)^\top h_b^{(2)}(t)
=n\,\nabla_{W^{(3)}}f_{n,a}(t)^\top\nabla_{W^{(3)}}f_{n,b}(t).
\]

It is the readout block's contribution to the tangent kernel, not the sum over parameter blocks. We ask for the off-diagonal entry and its first three jet coefficients:

\[
J_r:=\lim_{n\to\infty}\mathbb E\left[
\frac1{r!}\left.\frac{d^r}{dt^r}K_{n,12}(t)\right|_{t=0}\right],
\qquad r=0,1,2.
\]

Expectation is over initialization. The training derivatives are taken first at finite width.

## Executable input

From the study directory, this uses the example's construction and asks for the jets:

```python
from symbolic_kernel_jets import build_example

p, parameters, network, flow = build_example("symbolic")
jets = p.jets(network["kernel12"], flow, order=2, moving=True)
answers = [p.compile(jet, preactivations=[*network["z1"], *network["z2"]])
           for jet in jets]
for answer in answers:
    print(answer.formula())
```

The construction performed inside `build_example` is ordinary typed code:

```python
from mfp_compiler import Program

p = Program()
layer1, layer2 = p.vector_type("layer1"), p.vector_type("layer2")
alpha, beta, gamma, y1, y2 = [p.parameter(name)
    for name in ("alpha", "beta", "gamma", "y1", "y2")]
U, V = p.root("W1_col1", layer1), p.root("W1_col2", layer1)
W2, W3 = p.matrix("W2", layer1, layer2), p.root("W3", layer2)

z1 = [alpha*U, beta*U + gamma*V]
z2 = [W2 @ p.phi(z) for z in z1]
h2 = [p.phi(z) for z in z2]
f = [p.inner(W3, h) for h in h2]
loss = ((f[0]-y1)**2 + (f[1]-y2)**2)/4
grad = p.gradient(loss, vectors=[U, V, W3], matrices=[W2])
flow = {weight: -value for weight, value in grad.items()}
K12 = p.inner(h2[0], h2[1])
jets = p.jets(K12, flow, order=2, moving=True)
answers = [p.compile(jet, preactivations=[*z1, *z2]) for jet in jets]
```

`moving=True` differentiates the parameter-dependent flow again. Thus the second entry beyond the first derivative includes both the second differential of the kernel and the acceleration of the parameters. Residuals are differentiated as part of the loss; they have not been frozen. `jets` includes the factor \(1/r!\); `derivatives` would return the derivatives without that factor.

## What the compiler returns

For generic \(\phi\), first compute

\[
(G_1,G_2)\sim N(0,Q),\qquad
S_{ab}=\mathbb E[\phi(G_a)\phi(G_b)],\qquad
(Z_1,Z_2)\sim N(0,S).
\]

The zeroth result is \(J_0=\mathbb E[\phi(Z_1)\phi(Z_2)]\), and the first is \(J_1=0\). The second is a homogeneous quadratic polynomial in the labels,

\[
J_2=C_{11}(Q)\,y_1^2+C_{12}(Q)\,y_1y_2+C_{22}(Q)\,y_2^2,
\]

whose coefficients are sums and products of explicit Gaussian expectations of activation derivatives. The current output contains 4, 14 and 132 expectation nodes for orders 0, 1 and 2, respectively. These counts include intermediate nodes that can become unused after the final simplification; for example the first output simplifies to zero. They are not minimal-complexity claims. The complete [generic formula](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/symbolic.txt), [label coefficients](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/symbolic_label_coefficients.txt), and [JSON graph](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/symbolic.json) are retained.

The zero first coefficient concerns the limiting expected derivative. At finite width, the output-dependent part of the residual can contribute a nonzero expected derivative even though the readout is centered. The [independent derivation](kernel_jet_check.md) explains this distinction and gives an exact finite-width check in the linear case.

## A fully symbolic nonlinear result

Set \(\phi(z)=z^2\), using `build_example("quadratic")` or the CLI flag below. All Gaussian integrals then evaluate exactly. To write the returned polynomial compactly, define

\[
s:=Q_{11}Q_{22},\qquad c:=Q_{12},
\]

and the two explicit polynomials

\[
\begin{aligned}
A(s,c)&=5815s^2+11746sc^2+16702c^4,\\
B(s,c)&=4542s^4+14636s^3c^2+30788s^2c^4
       +13856sc^6+4704c^8.
\end{aligned}
\]

The compiler returns

\[
\begin{aligned}
J_0&=9s^2+2(s+2c^2)^2,\\
J_1&=0,\\
J_2&=A(s,c)\bigl(Q_{11}^4y_1^2+Q_{22}^4y_2^2\bigr)
     +B(s,c)y_1y_2.
\end{aligned}
\]

No geometry or label has been assigned a numerical value. For example, \(Q_{12}=\alpha\beta\) throughout. The same expression is obtained by first compiling with generic \(\phi\), then substituting \(\phi(z)=z^2\) into every Gaussian expectation node and evaluating those moments. The [direct polynomial output](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/quadratic.txt) and the coefficient extraction are preserved.

For a smaller independent validation case, identity activation gives

\[
J_0=Q_{12},\qquad J_1=0,\qquad
J_2=\frac94(Q_{11}y_1+Q_{12}y_2)(Q_{12}y_1+Q_{22}y_2).
\]

The coefficient \(9/4\) was independently derived by differentiating the full finite flow and evaluating its Gaussian matrix moments. The nonlinear example, not this validation case, is the primary demonstration.

## Run and check scope

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets.py
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets.py --activation quadratic
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets.py --json
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_symbolic_kernel_jets.py' -v
```

For all three variants, text/JSON outputs, symbolic comparisons and a source/environment manifest, run [run_symbolic_kernel_jets.py](run_symbolic_kernel_jets.py) with `--out` pointing to a new run folder under this study's generated-data namespace. The retained [v2 manifest](../../data/generated/mfp_gaussian_master_proof_20261010/symbolic_kernel_jets_v2/manifest.json) records successful serialization, label-degree checks, the independent linear target, the quadratic initial kernel, the compact nonlinear formula, and agreement between generic-activation and direct-polynomial compilation paths.

The [finite verification report](kernel_jet_finite_check.md) records three passing tests from [test_symbolic_kernel_jets.py](test_symbolic_kernel_jets.py). Its independent rational-array backpropagation and degree-two ODE series check all four trainable parameter blocks, both nonlinear input representations, and moving versus frozen directions at widths 2 and 3. The [mathematical report](kernel_jet_check.md) independently derives the identity-activation Gaussian targets and explains the nonlinear first-jet cancellation under its stated bounded-derivative assumptions. It does not independently derive the long nonlinear second-jet formula.

This is a finite-order calculation at initialization under the study theorem's assumptions. It does not assert convergence of an infinite Taylor series or reconstruct the positive-time kernel from three coefficients. No core compiler or master-proof changes were needed.
