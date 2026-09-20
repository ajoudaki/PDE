# Filter geometry and a posteriori endpoint certificates

Lead derivation, 2026-09-20. Scientific inputs: docs/NOTATION.md and
docs/global_nonlinear.md C.4.7.9, C.4.7.10.B/C.1/D.3. This is an
internally checkable candidate, not established material. The order p below
is exactly the enriched polynomial-plus-word hierarchy of C.4.7.10.B,
with eta_p=1/[1024(p+1)^2], exact population expectations and the physical
unhalved-loss gradient metric. No previous study is an input.

## 1. An order-monotone quadratic approximation error

On either canonical initialized observable Hilbert space let S_p map raw
coefficients to their raw feature combination, G_p=S_p* S_p, and

\[
 Q_p=S_p(G_p+\eta_p I)^{-1}S_p^*.
\]

The raw lists are nested up to coordinate insertion/reordering, which is an
isometric zero-padding on coefficients. Whitening coordinates themselves
need not be nested. Define for every fixed field v

\[
 E_p(v)=\inf_a\{\|v-S_pa\|_2^2+\eta_p|a|^2\}.
\]

Completing the finite-dimensional square, the unique minimizer is
a=(G_p+eta_p I)^(-1)S_p* v, and

\[
 E_p(v)=\|v\|_2^2-\langle S_p^*v,(G_p+\eta_pI)^{-1}S_p^*v\rangle
       =\langle v,(I-Q_p)v\rangle.                 \tag{1}
\]

Padding any trial coefficient vector and using eta_(p+1)<=eta_p gives
E_(p+1)(v)<=E_p(v). Consequently, as quadratic forms,

\[
 0\le Q_p\le Q_{p+1}\le I.                       \tag{2}
\]

This order is valid even when the raw Gram is singular. Since every positive
contraction R satisfies R^2<=R (diagonalize on its finite-dimensional range,
and use the identity on its orthogonal complement where appropriate),

\[
 \|(I-Q_p)v\|_2^2\le E_p(v),\qquad
 \|(Q_{p+1}-Q_p)v\|_2^2\le E_p(v)-E_{p+1}(v).
\]

Thus

\[
 \sum_{p\ge1}\|(Q_{p+1}-Q_p)v\|_2^2\le E_1(v)\le\|v\|_2^2. \tag{3}
\]

The sum bound does not assert absolute summability or monotonic trained
prediction error. The field v is fixed in this statement; substituting a
different trained field at every order does not preserve the telescoping sum.
Density of the raw spans and eta_p down to zero give E_p(v) down to zero:
for fixed a from an earlier raw span, E_p(v)<=||v-Sa||^2+eta_p|a|^2;
first let p increase, then approximate v by that dense span.

The useful sharper norm estimate, obtained by adding and subtracting S_pa,
is

\[
 \|(I-Q_p)v\|_2\le
 \inf_a\left\{\|v-S_pa\|_2+\frac{|a|}{64(p+1)}\right\}.    \tag{4}
\]

Indeed ||I-Q_p||<=1 and
||(I-Q_p)S_pa||<=sqrt(eta_p)|a|/2. The coefficient norm in (4) is not
automatically bounded as a better approximation is requested.

For B_p=Q_(2,p) A_0 Q_(1,p), ||A_0||<=2 implies

\[
 \|(B_p-A_0)v\|_2\le
 2\sqrt{E_{1,p}(v)}+\sqrt{E_{2,p}(A_0v)}.          \tag{5}
\]

The adjoint estimate exchanges the layers. These are bounds in the actual
common carrier, preserving the actual adjoint. They do not assume operator
norm convergence of B_p, which finite-rank approximation need not have.

For initialized fields v=phi(g dot x/sqrt2), (1) and (5) use only finite
Gaussian contractions and a positive finite matrix inverse at each query x.
Thus they are legitimate initialization diagnostics, not future-oracle inputs.
For a trained reference field, the same expression is an analytical defect
unless that reference field has independently been computed or bounded.

## 2. A checkable small-loss certificate at any fixed order

Let t0 be any reached state of a fixed-p canonical closure. Write A=U_2 M U_1*
for its lifted middle action. On a finite training set with positive weights
define the weighted upper-feature Gram

\[
 K_{ij}=\sqrt{\mu_i\mu_j}\,E_2[H(x_i)H(x_j)].
\]

Assume at t0 that kappa=lambda_min(K)>0; put A_*=||A(t0)||op and
C_*=||c(t0)||2. All these quantities are current-state data. Define

\[
 r=\min\{1,\kappa/[4(A_*+2)]\},\qquad
 B=\sqrt{1+(C_*+1)^2[1+(A_*+1)^2]}.
\]

If

\[
 \sqrt{2L(t0)/\kappa}<r,                         \tag{6}
\]

then the original, unchanged closure gradient flow has a finite physical
state endpoint, fits every training label, and for s>=0 satisfies

\[
 \begin{split}
 K(t0+s)&\ge(\kappa/2)I,\\
 L(t0+s)&\le L(t0)e^{-2\kappa s},\\
 \int_{t0+s}^{\infty}\|\dot S(t)\|_{\rm physical}\,dt
       &\le\sqrt{2L(t0+s)/\kappa},\\
 \sup_{x\in\sqrt2 S^1}|f(t0+s,x)-f^\infty(x)|
       &\le B\sqrt{2L(t0+s)/\kappa}.             \tag{7}
 \end{split}
\]

Here physical state differences mean row-L2, readout-L2 and coefficient
Frobenius differences at this same order, on its fixed canonical mark carrier.
No comparison of differently sized coefficient matrices is used.

Proof. In the physical ball of radius r<=1 about S(t0), contraction of U_l
gives ||A||<=A_*+1 and ||c||<=C_*+1. Subtracting the two hidden forwards gives

\[
 \sup_x\|H_S(x)-H_{S(t0)}(x)\|_2
 \le (A_*+1)\|w-w(t0)\|_2+\|M-M(t0)\|_F
 \le (A_*+2)\|S-S(t0)\|_{\rm physical}.
\]

The weighted feature operator has norm at most one. Its change is bounded
by this last feature difference, so its Gram changes by at most twice that
amount. The chosen radius therefore ensures K>=kappa I/2. Readout dissipation
alone gives ||grad L||^2>=||grad_c L||^2>=2 kappa L. Exact energy gives
||dot S||^2=-dot L. At positive loss,

\[
 \|\dot S\|=\frac{-\dot L}{\|\nabla L\|}
 \le \frac{-\dot L}{\sqrt{2\kappa L}}
 =-\sqrt{2/\kappa}\,\frac d{dt}\sqrt L.          \tag{8}
\]

Integrating (8), (6) precludes a first exit from the radius-r ball. Global
fixed-order existence is already established. At L=0 the gradient vanishes
and continuation is constant. The same integration starting at any later
time yields finite remaining travel, hence a strong endpoint. The Gram bound
gives exponential loss decay. For any passive input the three prediction
gradient blocks have norms <=(A_*+1)(C_*+1), C_*+1 and 1; their product-metric
norm is at most B. Integrating along the remaining path proves (7), uniformly
on the entire circle. The constants involve no dictionary supremum norms.

## 3. Consequences for adjacent orders

If orders p and q both pass (6) at a common time T, let kappa_j and B_j be
their own certificate constants. The triangle inequality gives the entirely
current-state bound

\[
 \|f_p^\infty-f_q^\infty\|_\infty
 \le \|f_p(T)-f_q(T)\|_\infty
 +B_p\sqrt{2L_p(T)/\kappa_p}
 +B_q\sqrt{2L_q(T)/\kappa_q}.                    \tag{9}
\]

This applies in particular to q=p+1 and to any finite compatible dataset
whose reached states pass the certificate. It is an a posteriori theorem,
not an unconditional assertion that every canonical trajectory passes (6).
No unknown endpoint appears on the right side.

Suppose a family of closure trajectories has constants A,C,kappa,r and one
common T0 satisfying the hypotheses uniformly for all sufficiently large p.
If their predictions converge on every finite time interval to a reference
f(t), then (7) gives a uniform exponential output tail. Hence the endpoints
converge uniformly on the circle, the reference also has a uniform endpoint,
and the limits p->infinity and t->infinity commute for predictions. Explicitly,
for T>=T0, if d_p(T)=||f_p(T)-f(T)||infty and the common output-tail bound
is C_tail exp[-kappa(T-T0)], then

\[
 \|f_p^\infty-f^\infty\|_\infty
 \le d_p(T)+2C_{\rm tail}e^{-\kappa(T-T0)}.        \tag{10}
\]

The reference endpoint exists because the same triangle argument bounds
||f(t)-f(s)|| by passing to the p limit first. Thus it is not being assumed.
Uniform convergence in time on [0,infinity) follows by splitting at T.

If additionally d_p(T)<=A delta_p exp[b(T-T0)] with 0<delta_p<=1 and b>=0,
choose T-T0=log(1/delta_p)/(b+kappa) to obtain an endpoint error at most
(A+2C_tail) delta_p^{kappa/(b+kappa)}. This is a conditional rate-transfer
statement; no such p-dependent source rate is supplied by span density alone.

## 4. Why density alone supplies no rapid rate

Let V_p be any nested finite-dimensional subspaces with dense union in an
infinite-dimensional Hilbert space, and let Q_p have range in V_p. Given any
positive decreasing sequence r_p->0, choose increasing p_j with r_(p_j)<=2^(-2j).
Inductively choose unit e_j orthogonal to V_(p_j) and to e_1,...,e_(j-1);
finite-dimensionality permits this. Let v=sum_j 2^-j e_j. For k>=j,
e_k is orthogonal to V_(p_j), so

\[
 \|(I-Q_{p_j})v\|\ge |\langle e_j,(I-Q_{p_j})v\rangle|
=2^{-j}\ge 2^j r_{p_j}.
\]

The error/r_(p_j) ratio is unbounded, excluding an O(r_p) bound for this v.
This only proves absence of a rate for arbitrary fields from nested density
alone. It does NOT construct a canonical trained trajectory with arbitrarily
slow order convergence, and does not disprove fast convergence on the actual
reachable family. That requires a regularity/approximation theorem for those
particular fields and their forward and reverse actions.
