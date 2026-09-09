# Two finite feature-ascent steps

Status: exact for two simultaneous explicit-Euler steps.

Let

$$
f_n(x)=\frac1n\sum_{i=1}^n a_i\phi(z_i),
\qquad
z_i=\frac{w_i^\top x}{\sqrt d},
\qquad
q=\frac{\lVert x\rVert^2}{d}.
$$

At initialization, write

$$
A\sim\mathcal N(0,1),
\qquad
Z\sim\mathcal N(0,q),
\qquad
A\perp Z.
$$

For the ascent update

$$
(a,w)^+=(a,w)+\eta n\nabla f_n(x),
$$

one neuron follows the exact map

$$
a^+=a+\eta\phi(z),
\qquad
z^+=z+\eta q a\phi'(z).
$$

Starting from $a_0=A$ and $z_0=Z$, two recomputed steps are

$$
\begin{aligned}
a_1&=A+\eta\phi(Z),
&
z_1&=Z+\eta qA\phi'(Z),\\
a_2&=a_1+\eta\phi(z_1),
&
z_2&=z_1+\eta q a_1\phi'(z_1).
\end{aligned}
$$

Therefore the exact expected output after two steps is

$$
F_2=\mathbb E\!\left[a_2\phi(z_2)\right].
$$

Equivalently, in initialization variables only,

$$
\begin{aligned}
F_2=\mathbb E\Big[&
\big(A+\eta\phi(Z)+\eta\phi(Z+\eta qA\phi'(Z))\big)\\
&\times\phi\Big(
Z+\eta qA\phi'(Z)
+\eta q\big(A+\eta\phi(Z)\big)
\phi'\big(Z+\eta qA\phi'(Z)\big)
\Big)
\Big].
\end{aligned}
$$

This is a two-dimensional Gaussian expectation for every finite $\eta$. No new Gaussian is sampled at step two: $(a_1,z_1)$ is the dependent pushforward of $(A,Z)$.

The computational DAG is

$$
(A,Z)\longrightarrow(a_1,z_1)
\longrightarrow(a_2,z_2)
\longrightarrow a_2\phi(z_2)
\longrightarrow\mathbb E.
$$

At finite width, the neurons remain independent and identically distributed, so

$$
\mathbb E[f_n^{(2)}(x)]=F_2
$$

for every $n$. Under the usual integrability condition,

$$
f_n^{(2)}(x)\longrightarrow F_2
$$

almost surely and in $L^1$ as $n\to\infty$.

If $\phi$ is twice differentiable and Gaussian integration by parts is valid, an equivalent response form is

$$
\begin{aligned}
F_2={}&\eta\,\mathbb E\!\left[
(\phi(z_0)+\phi(z_1))\phi(z_2)
+q(\phi'(z_0)+\phi'(z_1))\phi'(z_2)
\right]\\
&+\eta^2q^2\,\mathbb E\!\left[
a_1\phi'(z_0)\phi''(z_1)\phi'(z_2)
\right].
\end{aligned}
$$

The last term is the finite-step curvature response created by recomputing the second gradient. The raw Gaussian-DAG formula does not require $\phi''$.

Exact controls are

$$
\phi(z)=z
\quad\Longrightarrow\quad
F_2=4\eta q(1+\eta^2q),
$$

and

$$
\begin{aligned}
\phi(z)=z^2
\quad\Longrightarrow\quad
F_2={}&14\eta q^2+540\eta^3q^4+6792\eta^5q^6\\
&+29040\eta^7q^8+20160\eta^9q^{10}.
\end{aligned}
$$

These are two Euler steps. They are generally different from one frozen step of size $2\eta$ and from continuous feature flow evaluated at time $2\eta$.
