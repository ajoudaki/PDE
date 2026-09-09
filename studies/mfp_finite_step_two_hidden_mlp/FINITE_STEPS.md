# Finite feature-ascent steps with two hidden layers

## Model and exact finite-width update

Let both hidden layers have width $n$ and set $q=1$:

$$
u_j=\frac{w_j^\top x}{\sqrt d},
\qquad
h_j=\phi(u_j),
$$

$$
z_i=\frac1{\sqrt n}\sum_{j=1}^n W_{ij}h_j,
\qquad
f_n=\frac1n\sum_{i=1}^n a_i\phi(z_i).
$$

All raw parameters are independent standard Gaussians at initialization. The activation is RMS-normalized by

$$
G\sim\mathcal N(0,1),
\qquad
\mathbb E[\phi(G)^2]=1.
$$

Use one simultaneous pure-ascent Euler step

$$
\theta^{s+1}=\theta^s+\eta n\nabla_\theta f_n^s.
$$

Define

$$
h_j^s=\phi(u_j^s),
\qquad
c_i^s=a_i^s\phi'(z_i^s),
\qquad
b_j^s=\frac1{\sqrt n}\sum_iW_{ij}^s c_i^s.
$$

The exact finite-width recursion is

$$
\begin{aligned}
a_i^{s+1}&=a_i^s+\eta\phi(z_i^s),\\
W_{ij}^{s+1}&=W_{ij}^s+\frac{\eta}{\sqrt n}c_i^s h_j^s,\\
u_j^{s+1}&=u_j^s+\eta b_j^s\phi'(u_j^s),
\end{aligned}
$$

followed by

$$
z_i^{s+1}
=\frac1{\sqrt n}\sum_jW_{ij}^{s+1}\phi(u_j^{s+1}).
$$

Both right-hand sides in a parameter update use the old state.

## One step: finite Gaussian DAG

Let

$$
d=\mathbb E[\phi'(G)^2].
$$

Take independent

$$
U\sim\mathcal N(0,1),
\qquad
B\sim\mathcal N(0,d),
$$

and define

$$
u_0=U,
\qquad
u_1=U+\eta B\phi'(U),
\qquad
h_s=\phi(u_s).
$$

Set

$$
Q_{rs}=\mathbb E[h_rh_s],
\qquad r,s\in\{0,1\},
$$

and

$$
\rho_{10}
=\mathbb E\!\left[\frac{\partial h_1}{\partial B}\right]
=\eta\mathbb E[\phi'(u_1)\phi'(u_0)].
$$

Let $(\xi_0,\xi_1)$ be centered Gaussian, independent of $A\sim\mathcal N(0,1)$, with

$$
\mathbb E[\xi_r\xi_s]=Q_{rs}.
$$

Because $Q_{00}=1$, the initial second-layer preactivation is $z_0=\xi_0\sim\mathcal N(0,1)$. Define

$$
L_{10}=\rho_{10}+\eta Q_{01},
$$

$$
c_0=A\phi'(z_0),
\qquad
a_1=A+\eta\phi(z_0),
\qquad
z_1=\xi_1+L_{10}c_0.
$$

The term $\rho_{10}c_0$ is the response caused by reusing $W$ in the forward and backward passes. The term $\eta Q_{01}c_0$ is the explicit update of $W$.

The limiting expected output after one step is

$$
F_1=\mathbb E[a_1\phi(z_1)].
$$

Gaussian integration by parts in $A$ gives the equivalent form

$$
F_1
=\eta\mathbb E[\phi(z_0)\phi(z_1)]
+L_{10}\mathbb E[\phi'(z_0)\phi'(z_1)].
$$

As $\eta\to0$ this implies

$$
F_1
=\eta\left(1+d+d^2\right)+O(\eta^3).
$$

The three terms are respectively the readout, second-layer, and first-layer feature contributions.

## Two steps: recursive Gaussian DAG

Define

$$
c_1=a_1\phi'(z_1),
\qquad
K_{rs}=\mathbb E[c_rc_s],
\qquad r,s\in\{0,1\}.
$$

The backward response coefficients are

$$
\sigma_{1r}
=\mathbb E\!\left[\frac{\partial c_1}{\partial\xi_r}\right],
\qquad r\in\{0,1\}.
$$

Explicitly,

$$
\begin{aligned}
\sigma_{10}
={}&\mathbb E\!\left[
\eta\phi'(z_0)\phi'(z_1)
+L_{10}A a_1\phi''(z_0)\phi''(z_1)
\right],\\
\sigma_{11}
={}&\mathbb E[a_1\phi''(z_1)].
\end{aligned}
$$

Extend the lower fresh field to a centered Gaussian pair $(\chi_0,\chi_1)$ satisfying

$$
\mathbb E[\chi_r\chi_s]=K_{rs}.
$$

Here $\chi_0=B$. The actual backward field used in the second update is

$$
b_1
=\chi_1
+(\sigma_{10}+\eta K_{01})h_0
+\sigma_{11}h_1.
$$

Now set

$$
u_2=u_1+\eta b_1\phi'(u_1),
\qquad
h_2=\phi(u_2),
$$

and extend the lower Gram matrix by

$$
Q_{r2}=\mathbb E[h_rh_2],
\qquad r\in\{0,1,2\}.
$$

Define the second-step forward responses

$$
\rho_{2r}
=\mathbb E\!\left[
\frac{\partial h_2}{\partial\chi_r}
\right],
\qquad r\in\{0,1\},
$$

where the derivatives are obtained by differentiating the displayed lower-layer DAG. Equivalently,

$$
\rho_{21}
=\eta\mathbb E[\phi'(u_2)\phi'(u_1)],
$$

and

$$
\rho_{20}
=\eta\mathbb E\!\left[
\phi'(u_2)\phi'(u_0)
\left(
1+\eta\phi''(u_1)b_1
+\eta\sigma_{11}\phi'(u_1)^2
\right)
\right].
$$

Define

$$
L_{20}=\rho_{20}+\eta Q_{02},
\qquad
L_{21}=\rho_{21}+\eta Q_{12}.
$$

Finally extend $(\xi_0,\xi_1)$ to a centered Gaussian triple satisfying

$$
\mathbb E[\xi_r\xi_s]=Q_{rs},
\qquad r,s\in\{0,1,2\},
$$

and set

$$
z_2=\xi_2+L_{20}c_0+L_{21}c_1,
$$

$$
a_2=A+\eta\bigl(\phi(z_0)+\phi(z_1)\bigr).
$$

The limiting expected output after two steps is

$$
F_2=\mathbb E[a_2\phi(z_2)].
$$

For a Gaussian-integration-by-parts form, define

$$
r_0=\phi'(z_0),
$$

$$
s_1=L_{10}r_0,
\qquad
r_1=\phi'(z_1)+a_1\phi''(z_1)s_1,
$$

$$
s_2=L_{20}r_0+L_{21}r_1.
$$

Here $r_j=\partial_Ac_j$ and $s_j=\partial_Az_j$. Stein's identity yields

$$
F_2
=\eta\mathbb E\!\left[
(\phi(z_0)+\phi(z_1))\phi(z_2)
\right]
+\mathbb E[\phi'(z_2)s_2].
$$

Every expectation above is a finite-dimensional Gaussian integral over the two fresh Gaussian processes $(\xi_0,\xi_1,\xi_2)$ and $(\chi_0,\chi_1)$ together with $A$ and $U$. The evolved variables themselves are not Gaussian.

## Exact controls

For $\phi(z)=z$,

$$
F_1=3\eta,
$$

and

$$
F_2=6\eta+24\eta^3+20\eta^5.
$$

For $\phi(z)=c$,

$$
F_1=\eta c^2,
\qquad
F_2=2\eta c^2.
$$

The finite-width parameter recursion is exact.  The displayed nonlinear
two-step Gaussian recursion is the candidate pointwise fixed-step width limit.
`../temporary_width_first_operator_peeling/FIXED_ETA_CAVITY.md` derives the
exact reused-row and reused-column regression terms, but its adaptive
value-and-tangent LLN is not yet a complete proof.  Identification with the
actual network therefore remains open, including under bounded derivatives
and linear growth.
