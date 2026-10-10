# An MLP, its parameter derivatives, and their Gaussian expectations

This example constructs a two-hidden-layer MLP in the typed interface, differentiates its output, and asks for the limiting expectation of a scalar made from that derivative. The runnable source is [mlp_derivative_example.py](mlp_derivative_example.py). It uses the existing compiler without extending its language or changing the master proof.

## Model and requested observable

Both hidden layers have width \(n\). The input is the scalar \(x=1\), and there are no biases. Write \(W^{(1)},W^{(3)}\in\mathbb R^n\) for the first layer's single column and the stored readout, and \(W^{(2)}\in\mathbb R^{n\times n}\). At initialization,

\[
W_i^{(1)},W_i^{(3)}\sim N(0,1),\qquad
W_{ij}^{(2)}\sim N(0,1/n),
\]

with all entries independent. In particular, this example explicitly chooses an order-one stored readout; it is not the book's small-readout initialization. The forward pass is

\[
\begin{aligned}
z^{(1)}&=W^{(1)},& h^{(1)}&=\phi(z^{(1)}),\\
z^{(2)}&=W^{(2)}h^{(1)},& h^{(2)}&=\phi(z^{(2)}),\\
f_n&=\frac1nW^{(3)\top}h^{(2)}.
\end{aligned}
\]

For the generic activation calculation, assume \(\phi\in C^\infty(\mathbb R)\) and that every derivative has polynomial growth, as in the study's theorem. All expectations below are over the stated initialization.

Ask for the first-layer parameter gradient and then its squared magnitude:

\[
b^{(1)}:=n\nabla_{W^{(1)}}f_n,\qquad
O_n:=\frac1n\|b^{(1)}\|^2
     =n\|\nabla_{W^{(1)}}f_n\|^2.
\]

The scaling is part of the interface: `p.gradient` returns \(n\) times a vector-root gradient, while `p.inner` divides a vector inner product by \(n\). Squaring makes this a useful nonzero scalar observable. The expectation of the averaged gradient itself is zero here because the readout is centered and independent.

## Input to the compiler

From this study's directory, the essential program is:

```python
from mfp_compiler import Program

p = Program()
layer1 = p.vector_type("layer1")
layer2 = p.vector_type("layer2")
W1 = p.root("W1", layer1)                  # iid N(0,1)
W2 = p.matrix("W2", layer1, layer2)        # iid N(0,1/n)
W3 = p.root("W3", layer2)                  # iid N(0,1)

z1 = W1                                   # scalar input x=1
h1 = p.phi(z1)
z2 = W2 @ h1
h2 = p.phi(z2)
f = p.inner(W3, h2)                        # W3.T @ h2 / n

grad = p.gradient(f, vectors=[W1])
observable = p.inner(grad[W1], grad[W1])
answer = p.compile(observable, preactivations=[z1, z2])
print(answer.formula())
```

The inputs are symbolic network operations, parameter distributions, the differentiation request, and a scalar observable. There is no numerical width or sampled matrix. `preactivations` requests the restricted activation-moment form and declares the original nonlinear arguments.

## Returned Gaussian calculation

The returned object contains named Gaussian sources, their covariance table, expectation nodes and the applied-rule trace. Its readable formula is

```text
I_1 = E[(phi(r_W1))^2], (r_W1) ~ N(0, [1])
I_2 = E[(phi^(1)(g_W2_F_1))^2], (g_W2_F_1) ~ N(0, [I_1])
I_3 = E[(phi^(1)(r_W1))^2], (r_W1) ~ N(0, [1])
output = (I_2 * I_3)
```

Equivalently, compute in this order:

\[
\begin{aligned}
G&\sim N(0,1),& q_1&=\mathbb E[\phi(G)^2],\\
Z&\sim N(0,q_1),& s_2&=\mathbb E[\phi'(Z)^2],\\
&&s_1&=\mathbb E[\phi'(G)^2].
\end{aligned}
\]

The compiler's result means

\[
\boxed{\lim_{n\to\infty}\mathbb E[O_n]=s_1s_2.}
\]

Thus the second-layer preactivation variance is a previously computed Gaussian expectation. Generic integrals remain explicit integrals; symbolic compilation does not require numerical quadrature.

To see where the result comes from, ordinary finite-network differentiation gives the exact identities

\[
\delta^{(2)}=W^{(3)}\odot\phi'(z^{(2)}),\qquad
b^{(1)}=\phi'(z^{(1)})\odot W^{(2)\top}\delta^{(2)}.
\]

Here \(\odot\) denotes componentwise multiplication. The same \(W^{(2)}\) occurs in the forward and backward computations. Its transpose-call response coefficient is \(\mathbb E[A\phi''(Z)]\), where \(A\sim N(0,1)\) represents the readout and is independent of \(Z\). This coefficient vanishes. The remaining centered backward Gaussian source has variance \(\mathbb E[A^2\phi'(Z)^2]=s_2\) and is independent of the first-layer root \(G\). Multiplying by \(\phi'(G)\) therefore gives the second moment \(s_1s_2\). Matrix reuse is accounted for before its response is found to vanish.

The backpropagation identity holds at each finite width. The boxed formula describes its expectation as width tends to infinity. These are the two operations performed by `gradient` and `compile`, respectively.

## Other requests in the runnable example

The executable also compiles the averaged first-layer derivative, giving zero, and the full parameter gradient norm for the interface's vector mobility \(n\) and matrix mobility \(1\):

\[
K_n=n\|\nabla_{W^{(1)}}f_n\|^2
    +\|\nabla_{W^{(2)}}f_n\|_F^2
    +n\|\nabla_{W^{(3)}}f_n\|^2.
\]

Since
\(\nabla_{W^{(2)}}f_n=\delta^{(2)}h^{(1)\top}/n\)
and \(n\nabla_{W^{(3)}}f_n=h^{(2)}\), its limit is

\[
\lim_{n\to\infty}\mathbb E[K_n]
=s_1s_2+q_1s_2+q_2,
\qquad q_2:=\mathbb E[\phi(Z)^2].
\]

Two polynomial choices give exact numeric Gaussian outputs:

| Activation | First-layer quantity \(\lim\mathbb E[O_n]\) | Full quantity \(\lim\mathbb E[K_n]\) |
| --- | ---: | ---: |
| \(\phi(z)=z\) | 1 | 3 |
| \(\phi(z)=z^3\) | 164025 | 305775 |

For the cubic case, \((q_1,s_1,s_2,q_2)=(15,27,6075,50625)\).

## Run and validation

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/mlp_derivative_example.py
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/mlp_derivative_example.py --activation cubic
PYTHONDONTWRITEBYTECODE=1 python studies/mfp_gaussian_master_proof_20261010/mlp_derivative_example.py --json
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_mfp_mlp_example.py' -v
```

The four focused tests in [test_mfp_mlp_example.py](test_mfp_mlp_example.py) check the finite gradient and both norms against explicit rational-array backpropagation, verify that differentiating the output along its metric gradient gives the full norm, check the returned covariance dependencies, and verify the zero mean and both polynomial Gaussian results. These are deterministic calculations, not a numerical width-convergence experiment. An independent prompt-only derivation is recorded in [mlp_example_check.md](mlp_example_check.md).
