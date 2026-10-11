# Independent check of the endpoint transverse route

2026-10-11. Fresh isolated mathematical review of
`ENDPOINT_TRANSVERSE_ROUTE.md`. The complete candidate and the four authorized
dependencies listed below were read. The rigorous proof and canonical notation
skills, including the neural-network reference, were applied. No history,
study README, prior review, other route or study, experiment, or Git operation
was used. Only this report was written.

**Verdict: PASS for the stated partial results, with the scope qualifications
below.** I found no blocking mathematical error in the exact endpoint identities,
the original-cap cubic transverse-readout estimate, the local finite-width
holomorphic endpoint construction, or the cubic coefficient. The activation
example correctly obstructs a uniform relative estimate for arbitrary
first-layer displacements. It does not prove an obstruction for a final-layer
estimate alone, does not describe an actual training displacement, and does not
give a counterexample to endpoint variability. The requested endpoint lower
bound remains open.

## 1. Exact endpoint decomposition and constants

Use the candidate's normalized readout and final features
\(a=w/\sqrt n\), \(B=[h^{(L)}(x_1),\ldots,h^{(L)}(x_m)]/\sqrt n\),
and \(b_q=h^{(L)}(x_q)/\sqrt n\). The canonical physical flow gives
\(\dot a=-(2/m)Br\), where \(r=B^\top a-y\). On the supplied fitting
event, parameters converge, \(B_\infty^\top a_\infty=y\), and the residual
is integrable.

For \(B_0=B(0)\), the candidate defines
\[
G_0=B_0^\top B_0,\qquad
c_q=G_0^{-1}B_0^\top b_q(0),\qquad
R_q(t)=b_q(t)-B(t)c_q,\qquad
P_0=B_0G_0^{-1}B_0^\top.
\]
Thus \(P_0\) is an orthogonal projection,
\(B_0^\top R_q(0)=0\), and
\[
f_n(\infty,x_q)-c_q^\top y
=a_\infty^\top R_q(\infty),\qquad
a_\infty^\top R_q(0)
=-\frac2m\int_0^\infty R_q(0)^\top(B(t)-B_0)r(t)\,dt.
\]
Adding and subtracting \(a_\infty^\top R_q(0)\) proves candidate (3).
Applying \(I-P_0\) directly to the integrated readout equation proves (4).
All these integrals converge absolutely by bounded features and residual
decay. At a training query \(c_q\) is the corresponding coordinate vector
and \(R_q(t)=0\) at every time, so both endpoint-error terms vanish.

The fitting source gives exactly the constants quoted in candidate (5), with
\(\lambda=\gamma/m\), \(Y=\|y\|/\sqrt m\), and
\(D=8FY^2/\lambda^{3/2}\), where \(F\) is the source's forward-displacement
coefficient. In particular,
\[
\frac2m\sup_t\|B(t)-B_0\|_{\rm op}
\int_0^\infty\|r(t)\|\,dt
\le \frac2m(\sqrt mD)\frac{2\sqrt mY}{\lambda}
=\frac{32FY^3}{\lambda^{5/2}}.
\]
This verifies (6), including every factor of \(m\). Cauchy--Schwarz in (3)
then proves (7). The coefficient estimate used in (8) follows from
\[
\sqrt{\gamma/2}\,\|c_q\|
\le\|B_0c_q\|\le\|b_q(0)\|\le3H/2,
\qquad
\sqrt m\|c_q\|\le\frac{3H}{\sqrt{2\lambda}}.
\]
Together with \(\|R_q(0)\|\le3H/2\), this gives the two constants
\(16F/\lambda^2\) and \(48HF/\lambda^{5/2}\) in (8).

These are width-independent bounds on the supplied fitting event, with the
original label cap. They require no nonparallel geometry. Their size remains
fixed as \(n\) grows, so they do not transfer an \(n^{-1/2}\)
anti-concentration bound from the frozen interpolant to the true endpoint.

## 2. Local holomorphic endpoint and cubic coefficient

Candidate (9) has the correct mobility normalization. In
\(u=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)})\), both \(u\) and
\(a=w/\sqrt n\) are Euclidean gradient coordinates. The label-amplitude
parameter \(s\) replaces \(y\) by \(sy\), giving
\[
\dot a=-\frac2mB(u)r,\qquad
\dot u=-\frac2m\sum_j r_jDb_j(u)^\top a,
\qquad r=B(u)^\top a-sy.
\]

The complex-neighborhood argument in lines 200--220 is valid. Here are the
details that make its infinite-time conclusion precise. The coordinate
\(e=(I-P_0)a\) ranges in the fixed complex vector space
\(\ker B_0^\top\), rather than independently in all of \(\mathbb C^n\).
Since \(B(u_0)^\top B_0=G_0\) is invertible, the candidate's formula for
\(a\) gives a holomorphic chart in \((u,e,r,s)\) near the zero-label
stationary state. At fixed finite width the network itself is holomorphic
on a sufficiently small complex neighborhood: all finitely many training
and test preactivations remain inside the activation strips there.

Let \(J\) denote the training Jacobian with respect to \((u,a)\), and put
\(A=(2/m)JJ^\top\). The transpose is retained in the analytic extension;
it is not replaced by a conjugate transpose. At the base point
\(A_0=(2/m)G_0\). If \(g=\lambda_{\min}(G_0)>0\), shrink the
neighborhood until \(\|A-A_0\|_{\rm op}\le g/m\). Its Hermitian part
then satisfies
\[
\operatorname{Re}(z^*Az)\ge\frac gm\|z\|^2
\quad\text{for every }z\in\mathbb C^m.
\]
Along real time, the complexified residual therefore obeys
\[
\|r(t;s)\|\le |s|\|y\|e^{-gt/m},
\qquad r(0;s)=-sy.
\]
On a smaller closed neighborhood, the analytic matrices multiplying \(r\)
in the \((u,e)\) equations have a finite norm bound \(M\). Consequently
their total displacement is at most \(Mm|s|\|y\|/g\). For sufficiently
small \(|s|\), this bound, the residual bound, and the constant coordinate
\(s\) prevent exit. Their endpoint tails tend to zero uniformly on a
common smaller \(s\)-disk. Hence the holomorphic finite-time solutions
converge locally uniformly to a holomorphic endpoint. No global complex
positivity assertion is needed.

This also justifies the coefficient manipulations under the infinite-time
integral. Cauchy estimates on a smaller disk preserve the exponential
residual bound for its Taylor coefficients. The remaining factors are
uniformly bounded there. The parity symmetry gives \(a,r\) odd in \(s\)
and \(u\) even in \(s\), with \(u(t;0)=u_0\).

Writing the coefficients without factorials as in the candidate, direct
substitution yields
\[
r_1=-e^{-2G_0t/m}y,\qquad
a_1=B_0G_0^{-1}(I-e^{-2G_0t/m})y,
\qquad
\dot u_2=-\frac2m\sum_jr_{1,j}Db_j(u_0)^\top a_1.
\]
Thus (10) is correct, \(u_2\) has an integrable derivative, and
\(a_1(\infty)=B_0G_0^{-1}y\). Expanding exact identity (3) gives precisely
\[
p_3=a_1(\infty)^\top DR_q(u_0)[u_2(\infty)]
-\frac2m\int_0^\infty
R_q(u_0)^\top DB(u_0)[u_2(t)]r_1(t)\,dt.
\]
There is no missing readout-cubic term: (3) has already eliminated the
fitting-determined component, and its first product starts at order
\(s\cdot s^2\). Differentiating \((B^\top B)^{-1}\) also verifies
candidate (12), including the sign and coefficient of its residual term.

The resulting expansion is local at each fixed width and initialization.
It does not establish that its analytic disk reaches the original fixed
labels, or that the cubic term has a definite sign or a nonzero variance.

## 3. High-frequency activation obstruction

For \(\phi_k(z)=z+\varepsilon_k\sin(kz)\),
\(\varepsilon_k=e^{-2k}/k\), the claimed strip bounds are correct:
\[
\sup_{|\operatorname{Im}z|<1}|\phi_k'(z)|\le1+e^{-k},
\qquad
\sup_{|\operatorname{Im}z|\le1/2}|\phi_k''(z)|
\le k e^{-3k/2}<1.
\]
Also \(\phi_k(0)=0\), so the source envelope is exactly \(\beta=16\)
when the strip width is chosen to be one. Every activation is nonaffine.

With \(Z_1,Z_2\) independent standard Gaussians,
\(U=(Z_1+Z_2)/\sqrt2\), and \(\rho=1/\sqrt2\), the linear parts of
the residual in (14) cancel. For jointly standard Gaussian \(X,Y\)
with correlation \(\rho\),
\[
\mathbb E[\sin(kX)\sin(kY)]
=\tfrac12\bigl(e^{-k^2(1-\rho)}-e^{-k^2(1+\rho)}\bigr).
\]
This proves the exact variance formula (15). The dilation derivative in
(16) is also exact. Its three diagonal contributions have total limiting
variance one after division by \(\varepsilon_k^2k^2\). The independent
cross term vanishes by oddness. For the remaining cross terms, an explicit
check is
\[
\begin{split}
\mathbb E[XY\cos(kX)\cos(kY)]
=\tfrac12\bigl[&\bigl(\rho-k^2(1+\rho)^2\bigr)e^{-k^2(1+\rho)}\\
&+\bigl(\rho+k^2(1-\rho)^2\bigr)e^{-k^2(1-\rho)}\bigr]\to0.
\end{split}
\]
Thus (17) has the correct asymptotic constant. The dilation direction's
Gaussian parameter norm is \(\sqrt2\), so the derivative-to-residual ratio
divided by the direction norm still diverges.

The population projection correction is also controlled. If \(c_k\) is
either projection coefficient and \(s_k,t_k,g_k\) are as defined in the
candidate, its displayed formula gives the exact difference
\[
c_k-\rho=\frac{\varepsilon_k^2(t_k-\rho s_k)}{g_k}.
\]
It is \(O(\varepsilon_k^2)\). Holding this initial coefficient fixed,
as required by definition (2), changes both the residual and its dilation
derivative by \(O(\varepsilon_k^2)\) in \(L^2\). This is negligible
relative to \(\varepsilon_k\) and \(\varepsilon_k k\), respectively.

For \(\eta_k\to0\) with \(k\eta_k\to\infty\), the mixed-frequency
covariance for equal directions is bounded by
\(\tfrac12e^{-(k\eta_k)^2/2}\); for distinct directions it decays
exponentially in \(k^2\). Both bracket variances tend to one. Therefore
the relative finite displacement tends to \(\sqrt2\), as in (18).
The same limit survives the initial population projection correction.

The first-layer construction is compatible with bounded training
conditioning at any fixed depth. Oddness and independent training
coordinates keep the population training Gram diagonal. If its diagonal
at layer \(\ell\) is \(q_{\ell,k}\), then the real-line estimate
\(|\phi_k(x)-x|\le\varepsilon_k\) and the triangle inequality give
\[
\bigl|\sqrt{q_{\ell,k}}-\sqrt{q_{\ell-1,k}}\bigr|
\le\varepsilon_k,
\qquad
\bigl|\sqrt{q_{\ell,k}}-1\bigr|\le\ell\varepsilon_k.
\]
Thus the gap stays bounded below and tends to one at fixed depth. For
empirical versions, the justified order is first \(n\to\infty\) at fixed
\(k\), then \(k\to\infty\), or a sufficiently large diagonal choice of
widths. No uniform empirical accuracy at arbitrarily growing frequency is
implied. Empirical initial projection coefficients converge to the
population coefficients by convergence of their Gram and cross moments.
The all-row dilation has first-layer mobility norm tending to \(\sqrt2\),
so this transfer preserves the parameter normalization.

## 4. Qualifications and remaining gap

There are no required scientific inputs missing for the audited claims.
The following are precision points rather than failed proofs:

1. The summary-table wording at line 404 should be read as a statement
   about first-layer residuals and arbitrary small hidden displacements,
   uniformly over activations with the stated common envelope and a
   training gap bounded below. Section 4 explicitly supplies this narrower
   scope. The opening summary and table would be clearer if they repeated
   “first-layer.” A final-layer-only estimate is not refuted here.
2. The phrase “actual population projection residual” at line 349 means
   that the coefficients are the true initial population projection
   coefficients and are subsequently held fixed. This is consistent with
   (2). Recomputing the projection during a displacement is a different
   definition and should not be silently substituted.
3. The local holomorphic proof uses the fixed subspace for \(e\), ordinary
   transpose for analytic continuation, and the Hermitian-part estimate
   detailed above. Making these points explicit would prevent a mistaken
   objection that a complex symmetric Gram must itself remain Hermitian.

The example rules out a constant uniform over this activation family, or
a uniform modulus of relative continuity tending to zero with arbitrary
hidden displacement, based only on the displayed envelope, geometry and
gap bounds. It does not rule out activation-dependent constants. For each
fixed activation, the example does not claim a sequence of displacements
with a discontinuous residual map.

Most importantly, the constructed dilation is not shown to be produced by
canonical training. The cubic coefficient contains only the reachable
direction \(u_2(t)\), while the obstruction tests an unrestricted direction.
No cancellation or noncancellation of the two terms in (3) along the actual
flow has been proved. No nonzero fixed-label canonical endpoint
identification, endpoint fluctuation lower bound, or contradiction to that
lower bound follows from this note. The Gaussian small-ball criterion in
the authorized structural dependency also still requires width-uniform
control of the normalized pulled-back endpoint direction and its Gaussian
derivative. The candidate correctly leaves that bridge open.

## Reviewed input hashes

All four dependency hashes match the candidate's frozen-input table.

| Input | SHA-256 |
| --- | --- |
| `ENDPOINT_TRANSVERSE_ROUTE.md` | `62e11f088b884aaf6a3734e18a9ea19c3dbad1d9cd665e2fefa139c647e3030a` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `NONPARALLEL_INITIAL_VARIABILITY.md` | `017c2dcbd3e3b938099ab7dd748a211f859126bd636767b667ef3432386e33bc` |
| `ENDPOINT_SEPARATION_STRUCTURE.md` | `158d5bbfa8aa9a29cf6aeb26c36aeba6da9f2580aad536972b9b264a631b3a1c` |

This is an internal isolated check of the stated partial results, not a
promotion decision or a certification of the unresolved endpoint theorem.
