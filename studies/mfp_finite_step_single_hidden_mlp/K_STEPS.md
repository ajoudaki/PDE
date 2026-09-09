# Exact finite-step recursion

Status: exact for any fixed number of simultaneous explicit-Euler steps.

Set $q=1$. Let

$$
a_0\sim\mathcal N(0,1),
\qquad
z_0\sim\mathcal N(0,1),
\qquad
a_0\perp z_0.
$$

For $k$ substeps over a fixed total step $\eta$, write

$$
h=\frac{\eta}{k}.
$$

The exact neuron recursion is

$$
\begin{aligned}
a_{s+1}&=a_s+h\phi(z_s),\\
z_{s+1}&=z_s+h a_s\phi'(z_s),
\end{aligned}
\qquad 0\le s<k.
$$

If every training step instead has learning rate $\eta$, replace $h$ by $\eta$.

The expected output at step $k$ is

$$
F_k(\eta)=\mathbb E\!\left[a_k\phi(z_k)\right].
$$

Equivalently, if $a_s(a,z)$ and $z_s(a,z)$ denote the recursive functions seeded by $(a,z)$, then

$$
F_k(\eta)
=\frac{1}{2\pi}
\int_{\mathbb R^2}
a_k(a,z)\phi(z_k(a,z))
e^{-(a^2+z^2)/2}\,da\,dz.
$$

Thus every finite-step output remains a two-dimensional Gaussian integral. Later states are generally not Gaussian; they are deterministic pushforwards of the same two Gaussian seeds.

## Recursive Gaussian integration by parts

Define the sensitivity to the initial output weight by

$$
u_s=\frac{\partial a_s}{\partial a_0},
\qquad
v_s=\frac{\partial z_s}{\partial a_0},
\qquad
(u_0,v_0)=(1,0).
$$

Differentiating the state recursion gives

$$
\begin{aligned}
u_{s+1}&=u_s+h\phi'(z_s)v_s,\\
v_{s+1}&=v_s+h\left(
u_s\phi'(z_s)+a_s\phi''(z_s)v_s
\right).
\end{aligned}
$$

In matrix form,

$$
\begin{pmatrix}u_{s+1}\\v_{s+1}\end{pmatrix}
=
\begin{pmatrix}
1&h\phi'(z_s)\\
h\phi'(z_s)&1+h a_s\phi''(z_s)
\end{pmatrix}
\begin{pmatrix}u_s\\v_s\end{pmatrix}.
$$

Since

$$
a_k=a_0+h\sum_{s=0}^{k-1}\phi(z_s),
$$

Gaussian integration by parts in $a_0$ gives

$$
\mathbb E\!\left[a_0\phi(z_k)\right]
=\mathbb E\!\left[\phi'(z_k)v_k\right].
$$

Consequently,

$$
F_k(\eta)
=h\sum_{s=0}^{k-1}
\mathbb E\!\left[\phi(z_s)\phi(z_k)\right]
+\mathbb E\!\left[\phi'(z_k)v_k\right].
$$

All expectations in this formula are over $(a_0,z_0)$ only.

The raw recursion needs $\phi'$ and integrability of the final output. The integration-by-parts recursion is valid, for example, when $\phi\in C^2$ and $\phi,\phi',\phi''$ have polynomial growth.

## Checks

For $\phi(z)=c$,

$$
a_k=a_0+khc,
\qquad
z_k=z_0,
\qquad
F_k=khc^2.
$$

Thus $h=\eta/k$ gives $F_k(\eta)=\eta c^2$ exactly.

For $\phi(z)=z$,

$$
F_k
=\frac12\left((1+h)^{2k}-(1-h)^{2k}\right).
$$

With $h=\eta/k$,

$$
F_k(\eta)
=\frac12\left[
\left(1+\frac{\eta}{k}\right)^{2k}
-\left(1-\frac{\eta}{k}\right)^{2k}
\right].
$$
