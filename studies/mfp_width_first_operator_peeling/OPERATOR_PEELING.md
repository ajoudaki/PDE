# Width-first operator peeling for two feature-ascent steps

## Status

The small-learning-rate comparison can be proved directly for the finite
Gaussian mean-field program after taking the width limit, with its cubic
constant defined by a finite Gaussian operator-jet compiler.  No interchange
of the width and learning-rate limits, and no width-uniform Taylor remainder,
is used.

Direct Price differentiation through all four operator stages reduces that
coefficient to the displayed nine Gaussian activation moments.  The complete
node-jet table and an exact terminal polynomial audit are included below.

The exact fixed-step row/column regression algebra is derived in
`FIXED_ETA_CAVITY.md`.  Its probability part is presently a proof program,
not a complete theorem: the stopped adaptive coupling, the joint innovation
block, the tangent-field LLN for the response coefficients, and bad-event
removal have not all been proved in full.  Consequently identification with
the actual finite-width network remains open even under bounded derivatives
and linear growth.  The polynomial-growth extension is also open.

## Contract

Let \(\mathsf F_1(h)\) denote the annealed mean-field output after one ascent
step of size \(h\), and let \(\mathsf F_2(h)\) denote the corresponding output
after two recomputed steps, each of size \(h\).  The object of interest is

$$
\Delta(\eta)=\mathsf F_2(\eta/2)-\mathsf F_1(\eta).
$$

The limit order is

$$
n\longrightarrow\infty
\quad\text{at fixed }h,
\qquad\text{followed by}\qquad
h\longrightarrow0.
$$

Assume throughout that

$$
G\sim\mathcal N(0,1),
\qquad
\mathbb E[\phi(G)^2]=1.
$$

A safe, nonminimal regularity hypothesis for the cubic result is

$$
\phi\in C^8(\mathbb R),
$$

with \(\phi,\ldots,\phi^{(8)}\) of polynomial growth.  This contains the
identity activation.  The derivative order can probably be lowered after a
cancellation-aware audit.

## Gaussian expectation operators

For any positive-semidefinite covariance matrix \(C\), including singular
ones, define

$$
\Gamma_C[\psi]
=\mathbb E[\psi(X_C)],
\qquad
X_C\sim\mathcal N(0,C).
$$

Let \(C\in C^k(I;\mathbb S_+^m)\).  Assume that all mixed derivatives

$$
\partial_h^qD_x^\alpha\psi_h,
\qquad
q+\left\lceil\frac{|\alpha|}{2}\right\rceil\le k,
$$

exist and have locally uniform polynomial-growth envelopes.  For \(k\ge1\),

$$
\boxed{
\frac{d}{dh}\Gamma_{C(h)}[\psi_h]
=
\Gamma_{C(h)}\left[
\left(
\partial_h+\frac12 C'(h):D^2
\right)\psi_h
\right].
}
$$

This identity remains valid when \(C(h)\) changes rank.  Thus one never has
to differentiate a Cholesky factor or a covariance square root.

More generally, set

$$
L_r(h)=\frac12 C^{(r)}(h):D^2.
$$

For an \(h\)-independent integrand,

$$
\begin{aligned}
\frac{d}{dh}\Gamma_C[\psi]
&=\Gamma_C[L_1\psi],\\
\frac{d^2}{dh^2}\Gamma_C[\psi]
&=\Gamma_C[(L_1^2+L_2)\psi],\\
\frac{d^3}{dh^3}\Gamma_C[\psi]
&=\Gamma_C[(L_1^3+3L_1L_2+L_3)\psi].
\end{aligned}
$$

For a varying integrand one recursively applies

$$
\mathscr D_h
=
\partial_h+\frac12C'(h):D^2.
$$

### Proof at a singular covariance

For a Schwartz function, Fourier inversion gives

$$
\Gamma_C[\psi]
=
\frac1{(2\pi)^m}
\int_{\mathbb R^m}
\widehat\psi(\xi)
e^{-\xi^\top C\xi/2}
\,d\xi.
$$

Differentiating the exponential produces

$$
-\frac12\xi^\top C'(h)\xi,
$$

which is the Fourier multiplier of
\(\frac12C'(h):D^2\).  This proof never uses \(C^{-1}\), so singularity is
harmless.  Integrands satisfying the displayed mixed smoothness and polynomial
envelopes follow by cutoff and mollification.  On a compact \(h\)-interval,
\(\operatorname{tr}C(h)\) is bounded, hence every Gaussian moment is bounded
uniformly.  The cutoff approximants and all differentiated formulas converge
uniformly on that interval, which passes differentiability to the limit.

Polynomial growth without the mixed smoothness is insufficient.  For example,

$$
C(h)=[h^2],
\qquad
\psi(x)=|x|
$$

gives

$$
\Gamma_{C(h)}[\psi]
=\sqrt{\frac2\pi}|h|,
$$

which is not differentiable at zero.

## The user's scalar smoothing operator

For \(A\sim\mathcal N(0,1)\), let

$$
(H_tg)(z)=\mathbb E[g(z+\sqrt t A)].
$$

Then the proposed operator is exactly

$$
\boxed{
\mathcal P_f(z)
=
\mathbb E_A[f(z+Af(z))]
=
(H_{f(z)^2}f)(z).
}
$$

The top readout peel repeatedly uses the more general identity

$$
\boxed{
\mathbb E_A[(A+r)g(x+\lambda A)]
=
rH_{\lambda^2}g(x)
+\lambda H_{\lambda^2}g'(x).
}
$$

For nonlinear reuse of the same Gaussian carrier, the closed operator is

$$
\mathcal T_{g,\Psi}(z)
=
\mathbb E_A[\Psi(z+Ag(z),A)].
$$

This vector-valued conditional Gaussian operator, rather than
\(\mathcal P_f\) alone, is needed when one Gaussian readout appears in several
updated fields.

Gaussian averaging preserves \(C^k\) polynomial-growth functions.  It is not,
however, uniformly smoothing everywhere: when \(f(z)=0\), the heat time in
\(H_{f(z)^2}\) is zero.  Consequently the activation must still supply the
regularity required at initialization.

## Exact chronological operator DAG

Write

$$
d=\mathbb E[\phi'(G)^2].
$$

All variables in each stage below are recomputed inside that stage.  This is
essential: no time-indexed Gaussian is replaced by an independent copy.

### 1. First lower-layer operator

Let

$$
\mathcal L_1^h[\psi]
=
\Gamma_{\operatorname{diag}(1,d)}[\psi(U,\chi_0)].
$$

Set

$$
u_0=U,
\qquad
u_1=U+h\chi_0\phi'(U),
\qquad
h_r=\phi(u_r).
$$

This operator produces

$$
Q_{rs}=\mathcal L_1^h[h_rh_s],
\qquad r,s\in\{0,1\},
$$

$$
\rho_{10}
=
\mathcal L_1^h[\partial_{\chi_0}h_1],
\qquad
L_{10}=\rho_{10}+hQ_{01}.
$$

### 2. First top-layer operator

Let

$$
\mathcal T_1^h[\psi]
=
\Gamma_{\operatorname{diag}(1,Q(h))}
[\psi(A,\xi_0,\xi_1)].
$$

Inside this operator define

$$
z_0=\xi_0,
\qquad
c_0=A\phi'(z_0),
$$

$$
a_1=A+h\phi(z_0),
\qquad
z_1=\xi_1+L_{10}c_0,
\qquad
c_1=a_1\phi'(z_1).
$$

It produces

$$
\mathsf F_1(h)
=
\mathcal T_1^h[a_1\phi(z_1)],
$$

$$
K_{rs}=\mathcal T_1^h[c_rc_s],
\qquad
\sigma_{1r}
=
\mathcal T_1^h[\partial_{\xi_r}c_1].
$$

This is the top peel: all effects of the readout Gaussian \(A\) are now
contained in the functions returned by \(\mathcal T_1^h\).

### 3. Second lower-layer operator

Return to the lower layer with

$$
\mathcal L_2^h[\psi]
=
\Gamma_{\operatorname{diag}(1,K(h))}
[\psi(U,\chi_0,\chi_1)].
$$

The first updated feature is recomputed using this same \(\chi_0\).  Define

$$
b_1
=
\chi_1
+(\sigma_{10}+hK_{01})h_0
+\sigma_{11}h_1,
$$

$$
u_2=u_1+hb_1\phi'(u_1),
\qquad
h_2=\phi(u_2).
$$

Then

$$
Q_{r2}=\mathcal L_2^h[h_rh_2],
\qquad
\rho_{2r}
=
\mathcal L_2^h[\partial_{\chi_r}h_2],
$$

and

$$
L_{2r}=\rho_{2r}+hQ_{r2},
\qquad r\in\{0,1\}.
$$

### 4. Final top-layer operator

Let \(Q^{(2)}\) be the full \(3\times3\) Gram matrix and set

$$
\mathcal T_2^h[\psi]
=
\Gamma_{\operatorname{diag}(1,Q^{(2)}(h))}
[\psi(A,\xi_0,\xi_1,\xi_2)].
$$

Recompute \(z_0,z_1,c_0,c_1\) from the same
\((A,\xi_0,\xi_1)\), and define

$$
z_2
=
\xi_2+L_{20}c_0+L_{21}c_1,
$$

$$
a_2
=
A+h\bigl(\phi(z_0)+\phi(z_1)\bigr).
$$

The two-step output is

$$
\boxed{
\mathsf F_2(h)
=
\mathcal T_2^h[a_2\phi(z_2)].
}
$$

This is the recursive operator form proposed in the question.  It peels the
top, returns to the lower layer with the resulting operator coefficients, and
then peels the top again.

## Direct regularity after the width limit

Every covariance above is a Gram matrix and therefore positive semidefinite.
At \(h=0\), all time copies coalesce, so the Gram matrices are singular.  The
singular-covariance differentiation identity nevertheless applies.

Proceeding through

$$
\mathcal L_1^h
\longrightarrow
\mathcal T_1^h
\longrightarrow
\mathcal L_2^h
\longrightarrow
\mathcal T_2^h
$$

shows inductively that every \(Q,K,\rho,\sigma,L\), and therefore
\(\mathsf F_1,\mathsf F_2\), is \(C^3\) near zero.  Polynomial-growth
domination is preserved because only finitely many Gaussian expectations,
products, derivatives, and compositions occur.

This argument differentiates the width-limit objects themselves.  It does not
differentiate a finite-width network and does not exchange limits.

## Parity and the first jet

The operator DAG is invariant in law under

$$
h\mapsto-h,
\qquad
A\mapsto-A,
\qquad
(\chi_0,\chi_1)\mapsto(-\chi_0,-\chi_1),
$$

with \(U\) and the \(\xi\)-process unchanged.  Inductively,

$$
Q(-h)=Q(h),
\qquad
K(-h)=K(h),
$$

$$
\rho(-h)=-\rho(h),
\qquad
\sigma(-h)=-\sigma(h),
\qquad
L(-h)=-L(h).
$$

Consequently,

$$
\mathsf F_1(-h)=-\mathsf F_1(h),
\qquad
\mathsf F_2(-h)=-\mathsf F_2(h).
$$

At zero,

$$
Q_{rs}(0)=1,
\qquad
K_{rs}(0)=d,
$$

and

$$
L_{10}'(0)=L_{20}'(0)=L_{21}'(0)=1+d.
$$

Direct differentiation of the operator Stein forms gives

$$
\mathsf F_1'(0)=1+d+d^2,
$$

$$
\mathsf F_2'(0)=2(1+d+d^2).
$$

Therefore

$$
\Delta(0)=\Delta'(0)=\Delta''(0)=0.
$$

## Cubic coefficient from the operator compiler

Apply

$$
\mathscr D_h
=
\partial_h+\frac12C'(h):D^2
$$

three times at each of the four chronological Gaussian operators.  This gives
an entirely activation-defined finite compiler.  For a Gaussian node

$$
N(h)=\Gamma_{C(h)}[\psi_h],
$$

define

$$
\Psi_0=\psi_h,
\qquad
\Psi_{r+1}
=
\left(
\partial_h+\frac12C'(h):D^2
\right)\Psi_r,
$$

$$
J_rN
=
\Gamma_{C(0)}[\Psi_r(0)],
\qquad 0\le r\le3.
$$

Use the usual Leibniz and Faà di Bruno jet rules for sums, products,
compositions, covariance entries, and response entries, and run the compiler
in the fixed order

$$
\mathcal L_1
\longrightarrow
\mathcal T_1
\longrightarrow
\mathcal L_2
\longrightarrow
\mathcal T_2.
$$

Let \(J_3^{(1)}(\phi)\) and \(J_3^{(2)}(\phi)\) be its terminal one- and
two-step third jets.  Define

$$
\boxed{
\widehat\kappa_\phi
=
\frac{J_3^{(2)}(\phi)}{48}
-\frac{J_3^{(1)}(\phi)}6.
}
$$

This is a finite recursive formula containing only Gaussian integrations of
\(\phi\) and its derivatives.  It contains no supremum, derivative, or
trajectory property of the output.

The compact simplification can be obtained directly from the width-first
operators.  No finite-width jet or B-series identity is imported.  Write

$$
c=1+d,
\qquad
\beta=b+cr,
\qquad
\delta=d+ct,
$$

so that

$$
k=d+\beta+\delta=2d+b+c(r+t).
$$

Because every covariance is even, if
\(N(h)=\Gamma_{C(h)}[\psi_h]\), then at zero

$$
N'''(0)
=
\mathbb E\left[
\partial_h^3\psi_0
+\frac32C''(0):D^2\partial_h\psi_0
\right].
$$

With the moment notation of `HALF_STEP_BOUND.md`, the first lower operator
gives

$$
\begin{aligned}
Q_{01}''(0)&=dm,
&Q_{11}''(0)&=2d(e+m),\\
\rho_{10}'(0)&=d,
&\rho_{10}'''(0)&=3dj,\\
L_{10}'(0)&=1+d,
&L_{10}'''(0)&=3d(m+j),
\end{aligned}
$$

and at the first top node,

$$
\sigma_{10}'(0)=d+(1+d)t,
$$

$$
\sigma_{11}'(0)=b+(1+d)r.
$$

The first top covariance jets are

$$
K_{01}''(0)
=
2cm+3c^2j+dmt+d(e+m)r,
$$

$$
K_{11}''(0)
=
2\ell+8cm+6c^2(s+j)+2d(e+m)(t+r).
$$

Since \(K_{01}(0)=d\), the first variation of the second backward field has
coefficient

$$
2d+b+(1+d)(r+t)=k,
$$

and direct Price differentiation of the one-step terminal operator yields

$$
\begin{aligned}
J_3^{(1)}={}&
3c^2m+3c^3j+3d^2(m+j)\\
&+3dm\delta+3d(e+m)\beta
=S_\phi.
\end{aligned}
$$

At the second lower operator,

$$
\begin{aligned}
Q_{02}''(0)&=2k\ell+6dm,\\
Q_{12}''(0)&=2k\ell+7dm+4de,\\
Q_{22}''(0)&=4k\ell+12dm+8de,
\end{aligned}
$$

and

$$
\begin{aligned}
\rho_{20}'''(0)
&=18d(s+j)+12km+6\beta e,\\
\rho_{21}'''(0)
&=18ds+15dj+6km.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
L_{20}'''(0)
&=18ds+18dj+18dm+12km+6k\ell+6\beta e,\\
L_{21}'''(0)
&=18ds+15dj+21dm+6km+6k\ell+12de.
\end{aligned}
$$

The \(K''\) Price terms vanish at this stage because the zeroth lower
integrands and the relevant first response integrands are independent of
\((\chi_0,\chi_1)\).

For the final top operator, direct differentiation of its integrand gives

$$
\begin{aligned}
E_3={}&
12c^2e+12c\ell+57c^2m+33c^3j+36c^3s\\
&+d\bigl(L_{20}'''(0)+L_{21}'''(0)\bigr).
\end{aligned}
$$

The only nonzero expected Hessian entries of its first integrand jet are

$$
\mathbb E[\partial_{11}\psi_1]=\beta,
\qquad
\mathbb E[\partial_{22}\psi_1]=2\beta,
$$

$$
\mathbb E[\partial_{02}\psi_1]
=
\mathbb E[\partial_{12}\psi_1]
=\delta.
$$

Hence

$$
\begin{aligned}
J_3^{(2)}={}&E_3\\
&+3\left(
\frac{Q_{11}''(0)}2+Q_{22}''(0)
\right)\beta\\
&+3\bigl(Q_{02}''(0)+Q_{12}''(0)\bigr)\delta.
\end{aligned}
$$

Substitution gives

$$
\begin{aligned}
J_3^{(2)}={}&
12c^2e+12c\ell+57c^2m+33c^3j+36c^3s\\
&+36d^2s+33d^2j+57dkm+33de\beta\\
&+12cedt+24ed^2+12k^2\ell.
\end{aligned}
$$

Finally, the two activation polynomials can be written as

$$
S_\phi
=
3c^2m+3c^3j+3de\beta+3dkm+3d^2j,
$$

$$
\begin{aligned}
H_\phi={}&
c^2e+c\ell+2c^2m+3c^3s+cedt\\
&+2ed^2+3d^2s+k^2\ell+2dkm.
\end{aligned}
$$

Termwise comparison proves

$$
J_3^{(2)}=11S_\phi+12H_\phi.
$$

Since \(J_3^{(1)}=S_\phi\),

$$
\boxed{
\widehat\kappa_\phi
=
\frac{J_3^{(2)}-8J_3^{(1)}}{48}
=
\frac{4H_\phi+S_\phi}{16}.
}
$$

The final polynomial collection is independently checked by
`operator_third_jet_audit.py` using exact rational polynomial arithmetic.

## Width-first sharp bound

The direct operator calculation proves

$$
\Delta(\eta)
=
\widehat\kappa_\phi\eta^3+o(\eta^3).
$$

Indeed, since \(\Delta'''\) is continuous and
\(\Delta'''(0)=6\widehat\kappa_\phi\),

$$
\Delta(\eta)-\widehat\kappa_\phi\eta^3
=
\frac12
\int_0^\eta
(\eta-t)^2
\bigl(\Delta'''(t)-6\widehat\kappa_\phi\bigr)
\,dt.
$$

For every \(\varepsilon>0\), choose
\(\eta_0=\eta_0(\phi,\varepsilon)>0\) so that

$$
|\Delta'''(t)-6\widehat\kappa_\phi|<6\varepsilon
\qquad
\text{for }|t|<\eta_0.
$$

Then

$$
\boxed{
|\mathsf F_2(\eta/2)-\mathsf F_1(\eta)|
\le
(|\widehat\kappa_\phi|+\varepsilon)|\eta|^3,
\qquad
0<|\eta|<\eta_0.
}
$$

The prefactor contains only the activation-defined Gaussian coefficient
\(\widehat\kappa_\phi\) and the arbitrarily small universal slack
\(\varepsilon\).  No output supremum appears.

If \(\widehat\kappa_\phi\ne0\), then

$$
\lim_{\eta\to0}
\frac{|\Delta(\eta)|}{|\eta|^3}
=|\widehat\kappa_\phi|,
$$

so the exponent and asymptotic prefactor are sharp.

Under the stronger safe condition \(\phi\in C^{12}\), with derivatives of
polynomial growth, the same operator argument gives \(C^5\) regularity and
hence existence of a fifth-order remainder.  That existence statement alone
does not meet the quantitative contract, because its constant could be an
unknown output modulus.  An admissible activation-only estimate would have to
prove numbers \(B_\phi<\infty\) and \(h_\phi>0\) such that

$$
|\Delta(\eta)-\widehat\kappa_\phi\eta^3|
\le B_\phi|\eta|^5
$$

on \(|\eta|\le h_\phi\).  The following records the intended recursive
majorant scheme, but it is not yet a completed construction.

Choose \(p\in\mathbb N\) and \(M\ge1\) such that

$$
|\phi^{(r)}(x)|
\le M(1+|x|)^p,
\qquad 0\le r\le12.
$$

For a Gaussian node

$$
N(h)=\Gamma_{C(h)}[\psi_h]
$$

on \(|h|\le1\), the provisional scheme writes

$$
c_j=\sup_{|h|\le1}\|C^{(j)}(h)\|_1,
\qquad 0\le j\le5,
$$

and asks for weighted polynomial-envelope bounds \(a_{j,s}\) for
\(\partial_h^jD_x^s\psi_h\).  Initialize

$$
R^{(0)}_{j,s}=a_{j,s}
$$

and recurse by

$$
R^{(r+1)}_{j,s}
=
R^{(r)}_{j+1,s}
+\frac12
\sum_{\ell=0}^j
\binom j\ell
c_{\ell+1}R^{(r)}_{j-\ell,s+2}.
$$

If \(P\) is the resulting polynomial-envelope degree and the node dimension
is \(m\), then

$$
\mathcal J_r(N)
=
\mathbb E
\left[
(1+\sqrt{c_0}\|G_m\|)^P
\right]
R^{(r)}_{0,0}
$$

bounds the \(r\)-th node derivative.  Generate the \(a_{j,s}\) by Leibniz and
Bell-polynomial envelope rules and apply this recursion chronologically to
\(\mathcal L_1,\mathcal T_1,\mathcal L_2,\mathcal T_2\).  All covariance-jet
bounds at one stage are outputs of the preceding stage, so this construction
contains no output supremum and no circular definition.

If every \(c_j\) were replaced by an explicit preceding-stage numerical
majorant and every \(a_{j,s}\) were generated by a fully specified
Bell--Leibniz table, let \(\mathcal J_{1,5}\) and \(\mathcal J_{2,5}\) denote
the resulting terminal fifth-jet majorants.  The candidate

$$
\boxed{
B_\phi
=
\frac1{120}
\left(
\mathcal J_{1,5}+\frac{\mathcal J_{2,5}}{32}
\right)
}
$$

would then be valid.  As written, however, the \(c_j\) are suprema of unknown
covariance trajectories and the \(a_{j,s}\) and their polynomial degrees are
not explicitly constructed.  Therefore this formula is a proof strategy, not
the requested activation-only bound.  No explicit \(h_\phi\) has yet been
proved either.

The nine cubic moments alone cannot control this fifth-order constant.  They
do not control, for example, fourth powers of higher derivatives generated by
the Bell/Price compiler.  A narrow smooth perturbation

$$
\psi_\delta(x)
=
\delta^{13/8}
b\left(\frac{x-x_0}{\delta}\right),
\qquad
b\in C_c^\infty,
$$

has

$$
\mathbb E[(\psi_\delta''(G))^2]
=O(\delta^{1/4}),
$$

while

$$
\mathbb E[(\psi_\delta''(G))^4]
\asymp\delta^{-1/2}.
$$

Thus cubic atoms can remain asymptotically unchanged while fifth-order
majorants diverge.  A quantitative \(B_\phi\) genuinely needs higher
activation atoms or a weighted global derivative envelope.

## Identification with the actual network

To transfer the proved operator inequality to the original width-\(n\)
network, it is enough to establish, for every fixed sufficiently small \(h\),

$$
\lim_{n\to\infty}\mathbb E[f_{n,1}(h)]
=\mathsf F_1(h),
$$

$$
\lim_{n\to\infty}\mathbb E[f_{n,2}(h)]
=\mathsf F_2(h).
$$

The appropriate proof is chronological dynamic peeling:

1. condition a Gaussian weight matrix on the row and column fields revealed
   at the previous stages;
2. decompose its next multiplication into a fresh Gaussian innovation and
   the exact regression on the revealed fields;
3. identify the regression coefficients by Gaussian integration by parts as
   \(\rho\) and \(\sigma\);
4. prove concentration of the empirical Grams \(Q\) and \(K\);
5. remove bounded truncations using the polynomial moment envelope.

The precise alternating-cavity lemma needed here has the following form.  For
a fixed causal program alternating

$$
g^s=\frac1{\sqrt n}Wx^s,
\qquad
y^r=\frac1{\sqrt n}W^\top b^r,
$$

one must prove, for every fixed set of tagged coordinates,

$$
g_i^s
=
\xi_i^s
+\sum_{r<s}
\left(
\frac1n\sum_j
\frac{\partial x_j^s}{\partial\chi_j^r}
\right)b_i^r
+o_{L^2}(1),
$$

$$
y_j^r
=
\chi_j^r
+\sum_{s\le r}
\left(
\frac1n\sum_i
\frac{\partial b_i^r}{\partial\xi_i^s}
\right)x_j^s
+o_{L^2}(1).
$$

The fresh processes have empirical Gram covariances

$$
\operatorname{Cov}(\xi^s,\xi^t)
=\frac1n\sum_jx_j^sx_j^t,
$$

$$
\operatorname{Cov}(\chi^r,\chi^\ell)
=\frac1n\sum_ib_i^rb_i^\ell,
$$

and their cross-covariance must vanish asymptotically.  The empirical
derivative averages must converge jointly with the Grams.

For the present two-step recursion, row and column cavity expansions then give

$$
\frac1{\sqrt n}(Wh^1)_i
=
\xi_i^1+\rho_{10}^{(n)}c_i^0+o_{L^2}(1),
$$

$$
\frac1{\sqrt n}(W^\top c^1)_j
=
\chi_j^1
+\sigma_{10}^{(n)}h_j^0
+\sigma_{11}^{(n)}h_j^1
+o_{L^2}(1),
$$

and

$$
\frac1{\sqrt n}(Wh^2)_i
=
\xi_i^2
+\rho_{20}^{(n)}c_i^0
+\rho_{21}^{(n)}c_i^1
+o_{L^2}(1).
$$

The learned rank-one matrix terms add, exactly,

$$
hQ_{01}^{(n)}c_i^0,
$$

$$
hK_{01}^{(n)}h_j^0,
$$

and

$$
hQ_{02}^{(n)}c_i^0+hQ_{12}^{(n)}c_i^1,
$$

respectively.  There is no \(hK_{11}h^1\) term in the second transpose use,
because at that time the matrix contains only its first rank-one update.

The first transpose multiplication also has a potential response

$$
\sigma_{00}h^0,
\qquad
\sigma_{00}
=\mathbb E[A\phi''(Z)]
=0,
$$

which vanishes by centered-readout parity.  It should be removed by this
calculation, not by assuming independence.

The delicate step is the reused-column expansion for \(W^\top c^1\): the
tagged feature \(h_j^1\) already depends on the same tagged column through
\(\chi_j^0\).  A valid proof must condition on the whole earlier transpose
trajectory, or prove the alternating-cavity lemma while retaining
\((\chi_0,\chi_1)\) as one jointly Gaussian block.  A naive independent-column
replacement is invalid.

For two fixed steps this is a finite row/column conditioning problem.  The two
required response cancellations are proved in `FIXED_ETA_CAVITY.md`, and a
localized high-moment induction is outlined there under bounded derivatives
and linear growth.  A complete proof must additionally construct the stopped
stage-indexed coupling, preserve the joint innovation covariances, augment it
by the tangent fields defining \(\rho,\sigma\), and remove the bad event with
proved raw moment estimates.  Until those steps are written, the transfer to
the network is open.

## Controls

For \(\phi(z)=z\),

$$
\Delta(\eta)
=3\eta^3+\frac58\eta^5,
$$

so \(\widehat\kappa_\phi=3\).

For a literal constant activation,

$$
\Delta(\eta)=0.
$$
