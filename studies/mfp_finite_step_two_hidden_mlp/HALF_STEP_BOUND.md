# Width-first non-tautological sharp half-step bound

**Status:** Direct four-stage Price differentiation proves the cubic
coefficient and sharp asymptotic for the Gaussian operator DAG.  The requested
quantitative trained-network bound is open.  The proposed fifth-order
majorant still contains unspecified covariance and integrand-envelope bounds,
no explicit radius $h_\phi$ has been constructed, and the fixed-step
dynamic-cavity argument is an induction outline rather than a complete
value-and-tangent coupling theorem.

## Contract

The architecture is the RMS-normalized two-hidden-layer model with $q=1$. Let $F_1(\eta)$ be the annealed output after one Euler output-ascent step of size $\eta$, and let $F_2(\eta/2)$ be the annealed output after two recomputed Euler steps of size $\eta/2$. Define

$$
\Delta(\eta)=F_2(\eta/2)-F_1(\eta).
$$

The bound constant may use only Gaussian integrals of $\phi$ and its derivatives. It may not use a supremum, derivative, or trajectory property of $F_1$, $F_2$, or $\Delta$.

For the direct cubic operator proof, a safe nonminimal assumption is
$\phi\in C^8$, with $\phi$ and its first eight derivatives of polynomial
growth.  This supplies three singular-covariance Price derivatives at every
node of the limiting Gaussian DAG.  For a proposed trained-network transfer
one may use the stronger class in which $\phi$ has at most linear growth and
its first eight derivatives are bounded.  The current argument does not yet
prove the required pointwise width limit even in that stronger class.

## Exact cancellation

At finite width let

$$
P_n=n\nabla f_n,
\qquad
S_t(\theta)=\theta+tP_n(\theta).
$$

Flip only the readout weights:

$$
R(a,W,w)=(-a,W,w).
$$

Then

$$
f_n(R\theta)=-f_n(\theta),
\qquad
P_n(R\theta)=-R P_n(\theta),
$$

and therefore

$$
S_{-t}(R\theta)=R S_t(\theta).
$$

The initialization law is invariant under $R$. Hence both expected Euler outputs and $\Delta_n$ are odd functions of $\eta$.

The two discretizations also have the same first derivative at zero because

$$
\left.\frac{d}{d\eta}S_\eta\theta\right|_{\eta=0}
=P_n(\theta)
$$

and

$$
\left.\frac{d}{d\eta}S_{\eta/2}^2\theta\right|_{\eta=0}
=P_n(\theta).
$$

Consequently,

$$
\Delta_n(0)=\Delta_n'(0)=\Delta_n''(0)=0.
$$

## Opposite-order comparison only (not used in the proof)

The following finite-width Taylor calculation records the candidate from the
earlier initialization analysis.  It is not an input to the width-first result
below: neither its remainder nor either displayed limit is passed through
$n\to\infty$.  Equality with the width-first coefficient is proved
independently by differentiating the limiting Gaussian operators.

At initialization abbreviate

$$
P=P_n(\theta),
\qquad
J=DP_n(\theta),
\qquad
K=D^2P_n(\theta).
$$

Direct Taylor expansion gives

$$
S_{\eta/2}^2\theta
=S_\eta\theta
+\frac{\eta^2}{4}JP
+\frac{\eta^3}{16}K[P,P]
+O(\eta^4).
$$

Writing

$$
H_n=\nabla^2f_n,
\qquad
T_n=\nabla^3f_n,
$$

and using $P_n=n\nabla f_n$ yields

$$
\Delta_n(\eta)
=\kappa_n\eta^3+o(\eta^3),
$$

where

$$
\kappa_n
=\frac n4\mathbb E\lVert H_nP_n\rVert^2
+\frac1{16}\mathbb E T_n[P_n,P_n,P_n].
$$

The initialization-first MFP calculation gives the candidate limits

$$
H_\phi
=\lim_{n\to\infty}
n\mathbb E\lVert H_nP_n\rVert^2,
$$

and

$$
S_\phi
=\lim_{n\to\infty}
\mathbb E T_n[P_n,P_n,P_n].
$$

Thus that opposite-order calculation suggests

$$
\kappa_\phi
=\frac14H_\phi+\frac1{16}S_\phi.
$$

The next section defines the corresponding activation polynomials without
using those network limits.

## Pure activation formula

Let $G\sim\mathcal N(0,1)$ and write

$$
\phi_r=\phi^{(r)}(G).
$$

RMS normalization is

$$
\mathbb E[\phi_0^2]=1.
$$

Define the nine one-dimensional Gaussian activation moments

$$
\begin{aligned}
d&=\mathbb E[\phi_1^2],
&e&=\mathbb E[\phi_1^4],
&m&=\mathbb E[\phi_0\phi_2\phi_1^2],\\
j&=\mathbb E[\phi_3\phi_1^3],
&s&=\mathbb E[\phi_2^2\phi_1^2],
&\ell&=\mathbb E[\phi_0^2\phi_1^2],\\
b&=\mathbb E[\phi_0\phi_2],
&r&=\mathbb E[\phi_1\phi_3],
&t&=\mathbb E[\phi_2^2].
\end{aligned}
$$

Set

$$
c=1+d,
$$

$$
\tau=\ell+2cm+3c^2s+edt,
$$

and

$$
k=2d+b+c(r+t).
$$

Define the first activation polynomial by

$$
H_\phi
=c^2e+c\tau+2ed^2+3d^2s+k^2\ell+2dkm,
$$

and the second activation polynomial by

$$
\begin{aligned}
S_\phi={}&
3c^2m+3edb+3dm(d+b)
+3c^3j\\
&+3cedr+3cdm(r+t)+3d^2(m+j).
\end{aligned}
$$

Set the resulting activation-only candidate

$$
\kappa_\phi
=\frac{4H_\phi+S_\phi}{16}
$$

is a formula only in one-dimensional Gaussian integrals of $\phi$ and its first three derivatives.

## Direct width-first Gaussian-program bound

The Gaussian operator construction and singular-covariance differentiation
proved in
`../temporary_width_first_operator_peeling/OPERATOR_PEELING.md` establish,
after the width limit has already been taken, the Peano expansion

$$
\Delta(\eta)=\widehat\kappa_\phi\eta^3+o(\eta^3),
$$

where \(\widehat\kappa_\phi\) is returned by the chronological
\(\mathcal L_1\to\mathcal T_1\to\mathcal L_2\to\mathcal T_2\) Gaussian
Price-jet compiler.  It is a finite recursion of Gaussian integrations of
\(\phi\) and its derivatives and contains no output-defined quantity.

Then, for every $\varepsilon>0$, the definition of $o(\eta^3)$ gives an $\eta_0(\phi,\varepsilon)>0$ such that

$$
0<|\eta|<\eta_0
$$

implies

$$
\left|
\frac{\Delta(\eta)}{\eta^3}-\widehat\kappa_\phi
\right|<\varepsilon.
$$

The triangle inequality therefore gives

$$
|F_2(\eta/2)-F_1(\eta)|
\le
(|\widehat\kappa_\phi|+\varepsilon)|\eta|^3.
$$

The constant

$$
C_{\phi,\varepsilon}=|\widehat\kappa_\phi|+\varepsilon
$$

contains no output-defined quantity. Its activation-dependent part is the
finite Gaussian operator-jet formula in the linked note.

If $\widehat\kappa_\phi\ne0$, then

$$
\lim_{\eta\to0}
\frac{|\Delta(\eta)|}{|\eta|^3}
=|\widehat\kappa_\phi|.
$$

Hence $|\widehat\kappa_\phi|$ is the infimum of all asymptotically valid
prefactors. One generally cannot replace
$|\widehat\kappa_\phi|+\varepsilon$ by
$|\widehat\kappa_\phi|$ on a punctured interval because the next odd term may
have the same sign.

The direct node-jet calculation in the linked operator note proves

$$
\widehat\kappa_\phi=\kappa_\phi
=\frac{4H_\phi+S_\phi}{16}
$$

by establishing the explicit third-jet equality

$$
J_3^{(2)}-8J_3^{(1)}=3S_\phi+12H_\phi.
$$

without importing finite-width initialization derivatives.

## Sharpness controls

For $\phi(z)=z$, the nine Gaussian moments give

$$
H_\phi=12,
\qquad
S_\phi=0,
\qquad
\kappa_\phi=\widehat\kappa_\phi=3.
$$

The exact outputs are

$$
F_1(\eta)=3\eta,
$$

and

$$
F_2(\eta/2)
=3\eta+3\eta^3+\frac58\eta^5.
$$

Therefore

$$
\Delta(\eta)
=3\eta^3+\frac58\eta^5.
$$

No $o(|\eta|^3)$ bound, and no $O(|\eta|^p)$ bound with $p>3$, can hold for an activation class containing the identity.

For a literal constant activation, $H_\phi=S_\phi=0$ and $\Delta(\eta)=0$ exactly.

## Claim status and surviving obstruction

The following are exact or proved under the stated activation envelope:

1. the finite-width readout-reflection cancellation;
2. equality of the first derivatives of the two discretizations;
3. the finite-width cubic coefficient;
4. the activation-only Gaussian formula for the initialization MFP
   coefficient;
5. $C^3$ regularity of the width-first four-stage Gaussian operator DAG,
   including at its singular covariance at zero;
6. the direct Peano expansion and sharp cubic asymptotic with the finite
   operator-jet coefficient $\widehat\kappa_\phi$.

The compact identity

$$
\widehat\kappa_\phi=(4H_\phi+S_\phi)/16
$$

is proved directly by the width-first Price-jet table.

The network-level bridge is the pointwise fixed-step statement

$$
\lim_{n\to\infty}\mathbb E[f_{n,k}(h)]=\mathsf F_k(h),
\qquad k\in\{1,2\},
$$

for each fixed sufficiently small $h$.  Exact adaptive Gaussian regression and
the two response cancellations have been derived, but the stopped
concentration/coupling theorem and uniform-integrability passage have only
been outlined.  In particular, convergence of the derivative averages
defining $\rho$ and $\sigma$ requires a coupled tangent-field induction, not
merely convergence of the value fields.  Hence the network-level bridge
remains open.

The old boundary-layer counterexample remains relevant only to the discarded
route that tries to infer a width-first result from finite-width initialization
jets.  It does not obstruct the direct operator argument.
