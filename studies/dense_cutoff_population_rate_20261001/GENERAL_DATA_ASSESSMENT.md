# Removing input orthogonality: current result and remaining gap

2026-10-03. Continuation of the same-width comparison requested in this
study. The original dense-to-population question remains separate. This is
internal research, not a manuscript theorem or promotion review.

**Outcome.** The useful general-data theorem is not proved: the canonical
unclipped closure has not been shown to track dense training with strict
root-width error using a sublinear memory order, under only the existing
small-label fitting assumptions. Three additional routes were developed,
with exact finite-network estimates rather than population surrogates. The
remaining issue is probabilistic stability under repeated feedback. No
counterexample to that theorem was found.

There is an unconditional but computationally poor fallback: an order
exponential in the square root of width gives strict root-width, all-time
tracking for arbitrary input geometry satisfying the manuscript's initial
feature-Gram condition. Section 5 proves this directly from the manuscript,
at arbitrary fixed depth. It loses the compression advantage and does not
settle the intended sublinear-order result.

## 1. The precise target

The dense predictor is $f_{n,D}(t,x)$; the autonomous Legendre
response-memory predictor is $\widehat f_{n,q}(t,x)$. Both use width
$n$, the same canonical Gaussian initialization, zero initial readout,
the original residual-RMS clock, and the original unclipped updates. The
order $q$ is allowed to grow with $n$. For a fixed query law $\mu$
with finite second moment, the error is

\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
=\left(\int\sup_{t\ge0}
 |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

The desired statement is $\mathcal E_\mu\le C_{\delta,\mu}/\sqrt n$
with probability at least $1-\delta$, with constants independent of
width and physical time and with a useful sublinear order $q(n)=o(n)$.
The fitted endpoint is included. This means a confidence statement for
each sufficiently large width; it does not assert a single event for
infinitely many independently sampled networks. The fixed mixer remains
stored exactly and has quadratic size.

For the two-layer calculations write the parameters as $\theta=(A,W,w)$,
where $A$ is the read-in, $W$ the dense hidden matrix or its closure
reconstruction, and $w$ the readout. Define

\[
\|\Delta\theta\|_{\rm mob}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n,
\qquad Y=(m^{-1}\sum_a y_a^2)^{1/2}.
\]

The paper's distance $d_n$ is the sum of the three normalized block norms
whose squares appear here; hence
$\|\Delta\theta\|_{\rm mob}\le d_n\le\sqrt3\|\Delta\theta\|_{\rm mob}$.
The dense vector field is denoted by $F$ below.

The manuscript's common initialization event gives exponential fitting,
bounded operators, and total residual activity $O(Y)$, uniformly in
order. Its label threshold and constants may depend on the fixed dataset.
They are not uniform over geometries whose feature-Gram gap tends to zero.

## 2. Direct discrepancy energy: a more specific sufficient condition

The checked [general-data defect estimate](NONORTHOGONAL_DIRECT_ROUTE.md)
is

\[
\dot{\widehat\theta}=F(\widehat\theta)+(0,E_2,0),\qquad
\epsilon_q:=\int_0^\infty\|E_2(t)\|_Fdt
\le CY^{5/2}q^{-2}\sqrt{\log(e+q)}.
\tag{1}
\]

This holds for two tanh hidden layers without input orthogonality, on the
fitting event. It is an error in the differential equation evaluated along
the closure trajectory, not already an error between trajectories.

The new [direct energy calculation](GENERAL_DATA_STABILITY_ROUTE.md)
keeps the negative squared prediction discrepancy from gradient flow.
With $\Delta\theta=\widehat\theta-\theta_D$, define

\[
e^2=\|\Delta\theta\|_{\rm mob}^2,\qquad
A_4^2=\left(n^{-1}\sum_i\|\Delta A_{i,:}\|_2^4\right)^{1/2}.
\]

If $\rho_D$ and $\widehat\rho$ are the residual RMS values, then

\[
\frac12(e^2)'
\le-2\|\widehat f-f_D\|_m^2
 +C(\rho_D+\widehat\rho)(e^2+YA_4^2)+e\|E_2\|_F.
\tag{2}
\]

Here the norm in the negative term is over training samples. The residuals
in (2) belong to the two actual trajectories; substituting residuals on an
interpolating parameter segment would lose the all-time integrability.

Define the actual, residual-weighted discrepancy functional

\[
K_{n,q}=\int_0^\infty
Y(\rho_D+\widehat\rho)\frac{A_4^2}{e^2}\,dt,
\tag{3}
\]

with ratio zero when $e=0$. Then the manuscript's parameter distance
$d_n$ obeys

\[
\sup_{t\ge0}d_n(\widehat\theta,\theta_D)
\le C e^{CY+CK_{n,q}}\epsilon_q.
\tag{4}
\]

Consequently tightness in probability of $K_{n,q_n}$, for

\[
q_n=\left\lceil n^{1/4}[\log(e+n)]^{1/4}\right\rceil,
\tag{5}
\]

would prove the desired strict root-width bound. Tightness here means that
for each fixed confidence the functional has a bound independent of width.
A uniform expectation bound on the fitting event would suffice.

**Unproved step:** (3) is not known to be tight for the actual Gaussian
network. Deterministically its bound is only $CY^2\sqrt n$. A small
RMS discrepancy can be concentrated in a few neurons, and neither
exchangeability nor the rank of the memory defect excludes that. The
original signed Hessian form may be more favorable than the fourth-moment
relaxation; its control is also open. The full reconstruction is in
[GENERAL_DATA_STABILITY_CHECK.md](GENERAL_DATA_STABILITY_CHECK.md).

## 3. Weighted mixed moments were attempted, including actual sensitivities

The [mixed-moment route](FINITE_MIXED_MOMENT_ROUTE.md) analyzes the actual
finite dense network with arbitrary fixed input Gram matrix. Put
$h_a=\tanh(Ax_a/\sqrt d)$ and let

\[
\delta_a=w\odot\operatorname{sech}^2(Wh_a),\qquad
k_a=W^\top\delta_a,\qquad K_i(t)=\max_a|k_{a,i}(t)|,
\qquad S=2Y/\kappa,
\]

where $\rho_D(t)\le Ye^{-\kappa t}$. A sufficient finite empirical
budget is

\[
\mathcal M_\eta=\kappa\int_0^\infty e^{-\kappa t}
 \frac1n\sum_i e^{\eta K_i(t)/S}\,dt,
\qquad
\mathbb E[\mathbf1_{\mathcal G_n}\mathcal M_\eta]\le C,
\tag{6}
\]

for fixed positive $\eta,C$. The inequality in (6) remains unproved.
Its implication for exponentially small *weighted carrier tails* is proved;
it does not demand that every neuron remain below a cutoff.

The route goes beyond marginal moments. In coordinates
$\Theta=(A,\sqrt nW,w)$, the derivative $J$ of the finite training map
obeys exactly

\[
\dot J=(-LL^\top+\rho_D\mathcal A)J.
\]

Here, with $\mathcal F_a(\Theta)=nf_a(\Theta)$ and Euclidean derivatives
in $\Theta$,
\[
L=\sqrt{2/(mn)}[\nabla\mathcal F_a]_{a=1}^m,\qquad
\rho_D\mathcal A=-\frac2m\sum_a r_a\nabla^2\mathcal F_a.
\]

The negative Gram term comes from differentiating the adaptive residual.
The residual-Hessian part has rank $O(n)$ at every time; its only
unbounded blocks contain the first-layer carriers. Normalized Schatten
estimates and a Duhamel expansion give, **conditional on the budget**,
and for $CS^2\le\eta/2$,

\[
\sup_{t\ge0}\frac{\|J(t)-U_0(t,0)\|_{\rm HS}}{\sqrt n}
\le CS+C(S^2/\eta)\sqrt{\mathcal M_\eta},
\tag{7}
\]

where $U_0$ is the contraction generated by $-LL^\top$. There is a
corresponding averaged estimate for the backward response to initial
matrix perturbations. These retain the finite network and its residual
adaptation throughout.

The exact obstruction in the reverse direction is visible in Gaussian
integration by parts. Write $g_i=\sqrt nW_{0,:,i}$, a standard Gaussian
column, and $C_i=D_{g_i}\delta_a$. For the scalar carrier
$X_i=g_i^\top\delta_a/(S\sqrt n)$ and a smooth scalar test function
$\varphi$, the identity contains both

\[
\mathbb E[\varphi(X_i)\operatorname{tr}C_i]\quad\hbox{and}\quad
\mathbb E[\varphi'(X_i)g_i^\top C_i\delta_a],
\tag{8}
\]

with explicit normalization factors given in the route. Localization adds
a third term involving the derivative of its cutoff. For exponential
$\varphi$, unweighted averaged sensitivity estimates do not bound these
exponentially weighted products. A direct Schwarz estimate asks for a
larger exponential parameter and does not close (6). A proved Gaussian
transport lemma offers another route, but its required derivative bounds
on neighborhoods of the good set are not established for this network.

Thus mixed moments were genuinely attempted. Equations (7)--(8) identify
the feedback issue rather than inferring failure from a maximum-signal
bound. They do not establish failure of the weighted route either.

## 4. Which data assumptions are actually necessary?

The [exact data quotient](DATA_QUOTIENT_CLOCK.md), checked in
[DATA_QUOTIENT_CHECK.md](DATA_QUOTIENT_CHECK.md), removes redundant
duplicate/antipodal inputs using the oddness of the no-bias tanh network.
For any fixed normalized representatives that are pairwise nonproportional,
the population initialized feature Gram is positive definite at every
fixed depth. Thus its positive gap is automatic for each such dataset;
it need not be imposed independently. Its numerical size still depends on
the geometry.

If duplicated or antipodal labels are compatible with oddness, the quotient
has the original residual clock, positive sample weights, and the same
fitting argument. Input orthogonality is unnecessary for this reduction.

If labels conflict with these exact symmetries, the residual decomposes as

\[
\rho^2=u^2+\sigma^2,
\]

where $u$ is the residual on the effective class averages and $\sigma$
is the irreducible label inconsistency. Then the actual clock runs at
$\sqrt{u^2+\sigma^2}$, even after the effective problem fits. Replacing
it by $u$ would change the algorithm.

For two tanh layers, every fixed order admits a small-effective-label
fitting and physical convergence result even in this case. Its present
label threshold depends on order, so it does not justify a growing-order
theorem for fixed labels. A further exact identity shows that the endpoint
Legendre residual is an isometry on square-integrable histories over an
unbounded clock. This exposes an order/time issue but proves no tracking
lower bound.

A separate [endpoint diagnostic](PERSISTENT_CLOCK_ENDPOINT_DIAGNOSTIC.md)
computes how a static replacement of historical feature pairing changes
an unseen prediction after restoring the training prediction. It has not
been identified with an actual autonomous endpoint. Even its displayed
limiting coefficient has no proved nonzero sign. It supplies no negative
example. Its complete internal check found these limitations correctly
stated.

## 5. An unconditional, expensive order schedule

This corollary uses only the deterministic comparison inequalities already
proved in `paper/proof_tracking.tex`. It applies at arbitrary fixed depth
and with the paper's activation assumptions, on its common all-order
fitting event. It therefore retains the initial feature-Gram and small-label
assumptions, but imposes no orthogonality or additional carrier-tail
hypothesis.

The physical RMS bound on every dense carrier is

\[
\sup_{t,\ell,a}\|k_{D,a}^{(\ell)}(t)\|_2/\sqrt n\le C_{\rm car}.
\]

Choose the integer $M_n=\lceil C_{\rm car}\sqrt n\rceil+1$.
Every coordinate is then below $M_n$, so the manuscript's integrated
carrier tail $Z_n(M_n)$ is exactly zero. This is a deterministic
RMS-to-maximum bound, not a claimed Gaussian maximum estimate.

Put $A_n=Ce^{KM_n}\ge1$, the manuscript's damping factor, and set

\[
q_n=\left\lceil C_0(1+M_n)A_n n^{1/4}\right\rceil,
\qquad T_n=\kappa^{-1}\log(e+n).
\tag{9}
\]

Take the fixed $C_0$ large enough that the manuscript's linear feedback
absorption holds. Its cutoff conclusion, with $Z_n=0$, gives

\[
\begin{aligned}
D_n&:=\sup_{t\ge0}d_n(\widehat\theta_{n,q_n}(t),\theta_{n,D}(t))\\
&\le CA_n\left[\frac{1+M_n+\sqrt{T_n}}{q_n^2}
 +\frac{(e+n)^{-1/2}}{q_n}\right]
 +\frac{C(1+M_n)A_n^2}{q_n^2}
\le \frac C{\sqrt n}.
\end{aligned}
\tag{10}
\]

For the last step, $\sqrt{T_n}\le C(1+M_n)$. Substituting (9)
bounds the three terms by, respectively,

\[
\frac{C}{(1+M_n)A_n\sqrt n},\qquad
\frac{C}{(1+M_n)n^{3/4}},\qquad
\frac{C}{(1+M_n)\sqrt n}.
\]

The paper's whole-input comparison transfers (10) to $\mathcal E_\mu$.
Its common initialization event has probability tending to one. Hence for
each fixed confidence the conclusion holds at every sufficiently large
width with a constant independent of width and time. Algorithmic clipping
has not been introduced: the cutoff is used only in this proof.

However, (9) has size $n^{3/4}\exp(O(\sqrt n))$. Its evolving memory
is much larger than a dense learned matrix. It is a valid general-geometry
comparison, **not** a compression theorem. In the two-tanh scope, (1)--(4)
also give the slightly sharper fallback

\[
q_n=\left\lceil n^{3/8}e^{BY^2\sqrt n}\right\rceil
\]

for a sufficiently large data-dependent $B$; it is still exponential
for every fixed nonzero $Y$. Neither schedule resolves the requested
useful rate/order combination.

## 6. Evidence and next precise obligation

The three routes were initially developed by separate scoped collaborators,
then exchanged specific findings. The direct-energy and data-quotient notes
have complete internal reconstruction reports. The coordinator derived the
static diagnostic and the elementary fallback schedules; scoped
collaborators checked both. All are internal checks, not independent
promotion reviews. No numerical training, CPU fallback, paper edit, commit,
or push was performed.

The complete [mixed-moment check](FINITE_MIXED_MOMENT_CHECK.md) applies to
source SHA-256
`882fc64d4a0f3e98e630fdf9609ce911b1df21eee31fc9ac058be6058afdd571`,
after adding the explicit nonnegative parameter to the transport lemmas.
The complete scoped diagnostic check applies to SHA-256
`da87a5431ac588f839d64034dfcc9af562ec555cfea3c7c61ddb95dfcb073a4b`;
it verifies the asymmetric query coefficient and explicitly does not give
its sign or an actual autonomous endpoint identification. The two fallback
schedules were separately reconstructed from their displayed inequalities.

The next theorem-strength obligation is either a finite probabilistic bound
on (3), a closed mixed-moment estimate proving (6), or a sharper signed
prediction-Hessian estimate along the actual defect response. A complete
counterexample would instead need a nonvanishing or slower-than-root
*prediction* discrepancy along an actual initialized trajectory; an
arbitrary-state instability or a static matrix replacement does not suffice.

The useful same-width theorem without orthogonality therefore remains open.
The dense-to-population bias problem remains a separate open question.
