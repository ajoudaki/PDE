# Endpoint separation: reachable tangent directions and a Gaussian reduction

2026-10-11. Independent bounded structural route. The scientific inputs were
only `paper/compact.tex`, `paper/compact_fitting.tex`, and
`NONPARALLEL_INITIAL_VARIABILITY.md`. Required research/proof/notation
instructions were also read. No other new route, other study, experiment,
manuscript modification, or Git operation was used.

**Conclusion.** This route does not prove or disprove the requested canonical
endpoint lower bound. No exact canonical endpoint identification was found
under the stated exclusions. It does prove a local endpoint-derivative
description, identifies why augmented feature rank and a near-identity hidden
endpoint map do not alone finish the argument, and gives a precise Gaussian
integration-by-parts condition that would imply the requested scale without
an endpoint central limit theorem. The missing estimates are specified below.

The target remains the fully trained canonical network, nonzero fixed labels
under the original cap, and a fixed test direction separated from both signs
of every training direction. The test may lie in the training input span.
All constants below may depend on the fixed problem and confidence, but the
desired probabilistic constants must not depend on width.

## 1. Canonical coordinates and the endpoint derivative

Use the source's forward pass, loss, and physical flow:

\[
z^{(1)}(x)=W^{(1)}v,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
f_n(x)=w^\top h^{(L)}(x)/n,
\]

where \(v=x/\sqrt d\), and
\(\mathcal L=m^{-1}\sum_{a=1}^m(f_n(x_a)-y_a)^2\).
The hidden activations satisfy the stated strip assumptions. Write the
Euclidean mobility coordinates as

\[
\vartheta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
\in\mathbb R^P,
\qquad P=nd+(L-1)n^2+n.
\]

Let \(F(\vartheta)=(f_n(x_a))_{a=1}^m\), let
\(J(\vartheta)=DF(\vartheta)\in\mathbb R^{m\times P}\), and
let \(r=F-y\). The exact canonical flow in these coordinates is

\[
\dot\vartheta=-\frac2mJ(\vartheta)^\top r,
\qquad
\dot r=-\frac2mJ(\vartheta)J(\vartheta)^\top r.
\tag{1}
\]

Fix a finite width and an initialization on the source fitting event.
The source gives convergence to a fitted parameter \(\vartheta_\infty\)
and a positive final training-feature gap. Hence
\(J(\vartheta_\infty)\) has row rank \(m\): its readout-coordinate
block is \(H_\infty^\top/\sqrt n\), where
\(H_\infty=[h^{(L)}_\infty(x_1),\ldots,h^{(L)}_\infty(x_m)]\).

**Lemma 1: local endpoint map.** There is a neighborhood of this
initialization on which the fixed-label endpoint map

\[
E_y:\vartheta_0\longmapsto\vartheta_\infty
\]

is continuously differentiable. Its derivative has rank \(P-m\).
For an initial perturbation \(\xi_0\in\mathbb R^P\), its derivative
\(DE_y(\vartheta_0)\xi_0\) is the limit of the exact variational equation

\[
\dot\xi=-\frac2mJ^\top J\xi
          -\frac2m\sum_{a=1}^m r_aD^2F_a\xi,
\qquad \xi(0)=\xi_0.
\tag{2}
\]

The limit lies in \(\ker J(\vartheta_\infty)\).
This is a finite-width local statement; it claims no width-uniform bound
for the derivative or higher derivatives.

*Proof.* First work near a fitted parameter \(\vartheta_*\) with full
row-rank \(J_*\). On a small closed ball, arrange
\(JJ^\top\succeq aI_m\), \(\|J\|\le M\), and bounded second
derivatives, with \(a>0\). A trajectory remaining in this ball satisfies

\[
\|r(t)\|\le e^{-2at/m}\|r(0)\|,
\qquad
\int_0^\infty\|\dot\vartheta(t)\|\,dt
\le (M/a)\|r(0)\|.
\]

For a sufficiently small neighborhood of \(\vartheta_*\), the last
bound prevents exit from the ball. It proves a locally uniform endpoint
limit. In (2), the first matrix is negative semidefinite, and the norm of
the second matrix has an integrable, exponentially decaying bound.
Consequently \(\xi(t)\) is uniformly bounded by a fixed multiple of
\(\|\xi_0\|\).

Put \(\eta(t)=J(\vartheta(t))\xi(t)\). Hessian symmetry and (1)--(2)
give the exact identity

\[
\dot\eta=-\frac2mJJ^\top\eta
 -\frac2mD(JJ^\top)[\xi]r.
\tag{3}
\]

The forcing is exponentially decaying. The energy estimate for the first
term, followed by variation of constants, bounds \(\eta(t)\) by
\(C(1+t)e^{-2at/m}\|\xi_0\|\). Equation (2) now shows that
\(\dot\xi\) is integrable. These estimates are uniform in the small
initialization neighborhood, so the finite-time derivatives converge
uniformly. The endpoint map is \(C^1\), and
\(J(\vartheta_\infty)\xi(\infty)=0\).

At the fitted parameter itself the trajectory is constant and (2) gives

\[
DE_y(\vartheta_*)
=\lim_{t\to\infty}e^{-2tJ_*^\top J_*/m}
=P_{\ker J_*}.
\tag{4}
\]

This has rank \(P-m\). Since \(F\circ E_y=y\), the rank is at most
\(P-m\) throughout a sufficiently small neighborhood. Continuity of
a nonzero \((P-m)\)-minor at \(\vartheta_*\) gives the reverse
inequality there. Finally, the original fitted trajectory enters such a
neighborhood after finite time. Its finite-time flow is a local
diffeomorphism, and \(E_y=E_y\circ\Phi_T\), where \(\Phi_T\)
is that finite-time flow. The chain rule transfers the rank and derivative
description to the original initialization. This proves the lemma.

## 2. The zero-readout slice is the missing geometric condition

Let \(S=\mathbb R^{P-n}\times\{0\}\) be the tangent space of
admissible hidden-only initialization perturbations, and define

\[
A_n=DE_y(\vartheta_0)|_S:
\mathbb R^{P-n}\longrightarrow\ker J(\vartheta_\infty).
\tag{5}
\]

For the fixed test input \(x_q\), let
\(g_q=\nabla_\vartheta f_n(\vartheta_\infty,x_q)\).
The endpoint prediction's exact hidden-initialization derivative is

\[
D_{\vartheta_{0,\rm hid}}f_n(\infty,x_q)=A_n^\top g_q.
\tag{6}
\]

**Lemma 2: what feature rank does and does not say.** Suppose, additionally,
that the final augmented feature matrix \([H_\infty,h_{\infty,q}]\)
has full column rank. Then \(g_q\) is nonzero on the full fitting tangent
space \(\ker J(\vartheta_\infty)\). Nevertheless, the facts proved
so far do not show that \(A_n^\top g_q\ne0\).

Indeed, for any \(b\in\mathbb R^m\), the readout block gives

\[
\|g_q-J^\top b\|^2
\ge \frac1n\|h_{\infty,q}-H_\infty b\|^2.
\]

Thus the squared norm of the restriction of \(g_q\) to \(\ker J\)
is at least the positive final-feature Schur complement

\[
\frac1n\|(I-P_{H_\infty})h_{\infty,q}\|^2>0.
\tag{7}
\]

But \(\dim\operatorname{range}A_n\le P-n\), while the fitting tangent
space has dimension \(P-m\). For \(n>m\), the reachable image misses
at least \(n-m\) fitting tangent directions. A covector nonzero on
\(\ker J\) can vanish on this smaller image. Equation (6), rather than
(7), is the required quantity.

This is a proof-route obstruction, **not** a canonical counterexample.
It does not assert that the annihilation in (6) actually occurs. It shows
why full fitting-manifold rank, even augmented by a hidden map close to
the identity, is not by itself the claimed bridge. One must prove that a
query-changing fitted tangent perturbation has an admissible preimage
with \(\delta w(0)=0\), with quantitative control, or estimate (6)
directly.

There is a second distinction: the supplied nonparallel result proves
augmented feature rank at initialization, whereas (7) concerns the endpoint.
The fitting lemma protects the training gap only. Its deterministic bound
on feature displacement is of order \(Y^2\), independent of width.
The initial augmented Schur complement may depend on the fixed test
geometry. A direct perturbation argument requiring displacement smaller
than that Schur complement can impose a stronger, test-dependent label
restriction. The assignment forbids that change. This route has not shown
that endpoint augmented rank fails; it has identified the missing estimate.

## 3. A precise sufficient condition for the desired scale

The Gaussian initialization is particularly simple in mobility coordinates.
There is a standard Gaussian vector \(G\in\mathbb R^{P-n}\) such that
every hidden mobility coordinate at time zero is \(G_i/\sqrt n\).
For the first layer this uses \(W^{(1)}/\sqrt n\); for later layers it
uses their original variance \(1/n\).

Let

\[
p_n(G)=f_n(\infty,x_q),\qquad
a_n(G)=A_n^\top g_q.
\]

On an open fitting neighborhood where these derivatives exist,

\[
\nabla_Gp_n=\frac{a_n}{\sqrt n}.
\tag{8}
\]

**Lemma 3: localized Gaussian small-ball criterion.** Suppose, for a given
confidence budget \(\eta>0\), there are smooth cutoffs
\(0\le\chi_n\le1\), supported in open regions where \(p_n\) is
twice continuously differentiable and \(a_n\ne0\), such that

\[
\Pr\{\chi_n\ne1\}\le\eta,
\qquad
U_n=\frac{\chi_na_n}{\|a_n\|^2},
\qquad
\mathbb E\bigl(\|U_n\|^2+\|D_GU_n\|_{\rm HS}^2\bigr)
\le C_\eta^2,
\tag{9}
\]

with \(C_\eta<\infty\) independent of width. Assume the cutoffs allow
the integrations by parts below; compact support suffices, as does smooth
approximation with convergence in the two norms in (9). Then

\[
\sup_{b\in\mathbb R}
\Pr\{|p_n-b|\le h/\sqrt n\}
\le\eta+2hC_\eta
\qquad(h>0).
\tag{10}
\]

Consequently (9), together with a fitting failure probability tending to
zero, implies the requested two-run endpoint lower bound at every fixed
confidence for all sufficiently large individual widths. It uses the
original labels and allows constants depending on the fixed test geometry.

*Proof.* For a smooth compactly supported vector field \(U\), define its
Gaussian divergence by

\[
\operatorname{div}_{\!G}^{*}U=G^\top U-\operatorname{div}U.
\]

Ordinary integration by parts against the Gaussian density gives

\[
\mathbb E\langle\nabla\psi,U\rangle
=\mathbb E[\psi\operatorname{div}_{\!G}^{*}U].
\tag{11}
\]

A second application gives

\[
\mathbb E|\operatorname{div}_{\!G}^{*}U|^2
=\mathbb E\|U\|^2
 +\mathbb E\sum_{i,j}(\partial_iU_j)(\partial_jU_i)
\le\mathbb E(\|U\|^2+\|DU\|_{\rm HS}^2).
\tag{12}
\]

For completeness, differentiate the divergence to obtain
\(\partial_i\operatorname{div}_{\!G}^{*}U
=U_i+\operatorname{div}_{\!G}^{*}(\partial_iU)\).
Apply (11) first to the divergence itself and then to each \(U_i\);
this yields the equality in (12). The inequality uses
\(2ab\le a^2+b^2\) for the transposed derivative entries.

For any smooth scalar \(\varphi\), (8) and (11) give

\[
\mathbb E[\chi_n\varphi'(p_n)]
=\sqrt n\,\mathbb E[
\varphi(p_n)\operatorname{div}_{\!G}^{*}U_n].
\tag{13}
\]

If \(I\) is an interval, approximate its indicator by smooth functions
and choose \(\varphi\) to be their cumulative integral. One can use
\(0\le\varphi\le |I|+o(1)\). Equations (9), (12), (13), and
Cauchy--Schwarz yield

\[
\Pr\{p_n\in I\}
\le\Pr\{\chi_n\ne1\}
 +|I|\sqrt n\,C_\eta.
\]

Taking \(|I|=2h/\sqrt n\) proves (10). Endpoint values outside the
fitting region may be assigned arbitrarily when making this calculation;
their probability is already charged to the cutoff failure.

For an independent second run, condition on its endpoint value and apply
the shift-uniform estimate (10) to the first run. Separately charge a missing
second fitted endpoint as failure. For example, choose
\(\eta=\delta/3\), make the second fitting failure at most
\(\delta/3\), and take
\(h=\delta/(6\max\{C_\eta,1\})\). The total failure probability is
at most \(\delta\). This is exactly a
\(c_\delta/\sqrt n\) lower bound, with no simultaneous-in-width claim.

The criterion requires both inverse control of the pulled-back gradient
and regularity of its normalized direction. A lower bound on a gradient
norm alone is not substituted for anti-concentration. Likewise, Gaussian
Poincare gives an upper variance estimate and cannot fill this step.

## 4. What the small-label tangent calculation actually proves

There is a valid local check at zero label amplitude, but it does not close
the problem at the original fixed positive amplitude.

Fix a finite-width initialization with full-rank initialized training feature
matrix \(H_0\), and replace the target by \(s y\). Let
\(p_n(s)=f_n(\infty,x_q;s y)\), where only labels vary. Local endpoint
differentiability with respect to \(s\) follows by the same stable
argument as Lemma 1, treating the label as an additional stationary
coordinate. At \(s=0\), the trajectory has \(w=0\) and stationary
hidden parameters. Its first label derivative has zero hidden component.
Writing \(b(t)=\partial_s w(t)|_{s=0}\), direct differentiation gives

\[
\dot b=\frac2mH_0\left(y-\frac1nH_0^\top b\right),
\qquad b(0)=0.
\]

With \(G_0=H_0^\top H_0/n\), this yields

\[
b(\infty)=H_0G_0^{-1}y,
\qquad
p_n'(0)=\frac1nh_{0,q}^\top H_0G_0^{-1}y.
\tag{14}
\]

The exact symmetry \((y,w)\mapsto(-y,-w)\), with all hidden parameters
unchanged, also gives \(p_n(-s)=-p_n(s)\) wherever the endpoints exist.

Equation (14) identifies the frozen-feature interpolant as the first
label-amplitude derivative of the true endpoint. It is not an identity
between the fully trained endpoint and that interpolant. In particular:

1. A bound for a positive fixed-amplitude nonlinear remainder that does not
   decrease with width cannot transfer an \(n^{-1/2}\) lower bound.
2. Positivity of a leading small-amplitude coefficient does not exclude a
   zero at another allowed amplitude. Even an odd real-analytic scalar
   coefficient \(s(1-s^2/s_0^2)\) has this behavior. This scalar example
   is only a counterexample to the analytic-continuation inference, not
   a canonical-network counterexample.
3. Analyticity of the finite-time flow does not by itself establish
   analyticity of its infinite-time limit. A uniform complex-neighborhood
   argument, or another proof of endpoint analyticity, is required before
   such a continuation argument can even be invoked.

The source's original cap controls real fitting and small parameter motion.
This route has not converted that cap into a nonvanishing bound for (6),
or into (9), for every permitted fixed label vector and test geometry.

## 5. Frozen route status and exact reopening condition

| Claim | Status in this route |
| --- | --- |
| Local finite-width fitted endpoint is \(C^1\), with derivative (2) and rank \(P-m\) | Proved above on the supplied fitting event |
| Admissible endpoint randomness is controlled by \(A_n^\top g_q\), not only by the full fitting tangent space | Exact identity (6) |
| Final augmented feature rank would make the test gradient nonzero on the full fitting tangent space | Proved conditionally in (7) |
| Initial augmented feature rank implies the needed endpoint pullback bound under the original cap | Open |
| Bounds (9) imply the required endpoint \(n^{-1/2}\) small-ball estimate | Proved conditional lemma |
| The canonical fully trained flow satisfies (9) with width-independent constants | Open; decisive gap |
| A canonical nonzero-label separated-test endpoint cancellation exists | Not established |
| Small-label analyticity by itself rules out such cancellation | Invalid inference; it also requires an endpoint analyticity proof |

The structural route should be retained as a reduction, not counted as a
completed endpoint proof or a counterexample. Reopen it when a new argument
controls the zero-readout pullback \(A_n^\top g_q\) and the Gaussian
derivative in (9) under the existing label cap. A bound requiring a smaller
test-dependent label amplitude would resolve a different statement.

No external scientific theorem was imported. The differential and Gaussian
identities used in the new reductions are derived above. This artifact is
an author derivation awaiting independent checking, not a promoted result.

## Frozen input hashes

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `NONPARALLEL_INITIAL_VARIABILITY.md` | `017c2dcbd3e3b938099ab7dd748a211f859126bd636767b667ef3432386e33bc` |
