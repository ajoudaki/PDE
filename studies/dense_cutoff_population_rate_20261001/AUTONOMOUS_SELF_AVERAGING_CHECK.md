# Reconstruction of autonomous finite-width concentration

This is a complete scoped reconstruction of AUTONOMOUS_SELF_AVERAGING.md,
performed on 2026-10-01. It uses that candidate and the already authorized
and checked same-study controlled-feedback and passive-query results.
No other source, experiment, manuscript edit, or Git write was used.

**Outcome: the theorem reconstructs without the local response hypothesis H.**
The deterministic finite-width reference exists uniquely, fits exponentially,
and has uniformly bounded activity. The actual autonomous predictions
concentrate at strict root width around it in the stated fixed-confidence
whole-time norm. Two actual runs consequently differ at root width.
The result does not control the reference's population bias at a rate or
identify it with the autonomous expectation.

The setting remains two tanh hidden layers, fixed orthonormal training
inputs, zero readout, Gaussian initialization, a positive limiting initial
feature-Gram gap, sufficiently small fixed labels, and a bounded test-input
law. The result is unconditional with respect to H; it still has these
explicit model assumptions.

## 1. The reference equation has a closed Picard domain

Fix \(S\le1\) and the operator radius \(K\). For a deterministic control
\(b\) with total variation at most \(S\), let
\[
M_n[b](t,x)=\mathbb E f_{n,\Pi}^{b}(t,x).
\]
The expectation is over canonical first-layer initialization and the
projected hidden initialization. Each member has
\(\|W_0^\Pi\|_{\mathrm{op}}\le K\).
The checked controlled estimates give, uniformly over that initialization,
\[
|f_{n,\Pi}^b(t,x)|\le S,\qquad
\max_a\sup_{t\le T}
|M_n[b](t,x_a)-M_n[c](t,x_a)|
\le C\max_a\sup_{t\le T}|b_a(t)-c_a(t)|.
\tag{1}
\]
The constant depends on the fixed training data and \(K,S\), not on width,
physical duration, or first-root values. Taking expectation preserves the
pathwise Lipschitz bound. The first-layer roots may be unbounded; no root
cutoff is used.

Write \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\) and \(L_0=2(Y+S)\).
On \([0,\tau]\), consider controls starting at zero whose Lipschitz
constant in the vector \(\ell^1\) norm is at most \(L_0\).
This is a closed subset of the continuous path space with the uniform
metric, hence complete. If \(L_0\tau\le S\), every such path has total
variation at most \(S\).

Define the Volterra map
\[
(\mathcal T b)_a(t)
=-\frac2m\int_0^t[M_n[b](s,x_a)-y_a]\,ds.
\tag{2}
\]
The map is causal because the finite controlled ODE is causal. Its derivative
satisfies
\[
\sum_a|(\mathcal T b)'_a(t)|
\le\frac2m\sum_a(|M_n[b](t,x_a)|+|y_a|)
\le2(S+Y)=L_0,
\tag{3}
\]
where \(m^{-1}\sum_a|y_a|\le Y\).
Thus it preserves the closed Lipschitz domain.
Equation (1) gives
\[
\|\mathcal T b-\mathcal T c\|_\infty
\le C_0\tau\|b-c\|_\infty,
\tag{4}
\]
with only fixed-dimensional norm conversions. Choose \(\tau\) so
\(C_0\tau<1\). Successive iteration is then Cauchy by (4), its uniform
limit lies in the closed domain, and continuity of \(\mathcal T\) makes it
the unique fixed point. This supplies local existence and uniqueness of
the deterministic driver and therefore of
\(\bar f_n=M_n[\bar b_n]\).

This construction averages networks sharing the same deterministic control.
It neither averages their autonomous residuals nor invokes any population
quantity. In particular, the reference is deterministic even though its
definition contains an expectation over initialized finite networks.

For restart at \(t_0\), fix the already constructed history and apply the
same map only to its continuation, with value \(b(t_0)\) at the left endpoint.
If the history has variation at most \(S/2\), a continuation of length
\(\tau\) with \(L_0\tau\le S/2\) remains inside the same total-variation
tube. Its domain is again closed, and (1)--(4) apply to the full paths:
they agree on the past, so their uniform difference is just the continuation
difference. The same \(\tau\), independent of \(t_0\) and width, suffices.
Section 3 below provides exactly this strict activity margin.

## 2. Expected initial Gram and positive tangent matrix

The initial unprojected feature Gram converges qualitatively to the assumed
positive limiting Gram. Every entry is bounded by one, so its expectation
converges. Projection changes nothing on
\(E_n=\{\|W_0\|_{\mathrm{op}}\le K\}\), and
\(\Pr(E_n^c)\le Ce^{-cn}\). The change of any initial Gram-entry expectation
is at most \(2\Pr(E_n^c)\). Thus, for sufficiently large \(n\),
\[
\bar Q_{0,n}/m\succeq2\lambda I_m
\tag{5}
\]
for a fixed \(\lambda>0\) chosen below half the limiting gap.
No quantitative trained-population comparison is used here.

For each initialized controlled member, the exact training tangent matrix is
\[
\Lambda^b_{ab}
=\frac{g_a^\top g_b}{n}
 +\frac{\delta_a^\top\delta_b}{n}\frac{h_a^\top h_b}{n}
 +(v_a^\top v_b)\frac{(s_a\odot k_a)^\top(s_b\odot k_b)}n.
\tag{6}
\]
Each term is positive semidefinite. The first is an ordinary feature Gram;
the second is the Gram of \(\delta_a\otimes h_a/n\);
the third is the Gram of \(v_a\otimes(s_a\odot k_a)/\sqrt n\).
Thus \(\Lambda^b\succeq g(X)^\top g(X)/n\) for each member, independent
of whether that member fits its own labels.

The projected operator bound makes all deterministic controlled estimates
uniform across the ensemble:
\[
\|w\|_\infty\le S,\quad
\|W-W_0^\Pi\|_F\le S^2,\quad
\frac{\|p_a-p_a(0)\|_2}{\sqrt n}\le CS^2.
\]
Forward subtraction consequently gives
\(\|g_a-g_a(0)\|_2/\sqrt n\le CS^2\).
Each feature Gram entry changes by at most \(CS^2\).
For an \(m\times m\) matrix, its operator norm is at most \(m\) times
its maximum absolute entry, so
\[
\left\|\frac{g(X)^\top g(X)-g_0(X)^\top g_0(X)}{mn}\right\|_{\mathrm{op}}
\le CS^2.
\tag{7}
\]
Taking expectation and combining (5)--(7) proves
\[
\mathbb E\Lambda^b/m\succeq(2\lambda-CS^2)I_m.
\tag{8}
\]
Choose the fixed activity radius so that \(CS^2\le\lambda\).
It is the expected Gram that needs a uniform gap for this reference;
individual ensemble members do not need an initial gap.

The entries of \(\Lambda^b\) are also uniformly bounded above on this
tube. The feature factors are bounded, \(\|\delta_a\|_2/\sqrt n\le S\),
and \(\|k_a\|_2/\sqrt n\le(K+1)S\). These estimates justify integration
and expectation interchange in the next step even though the first roots
have no deterministic bound.

## 3. Expectation differentiation, fitting, and global continuation

For any deterministic absolutely continuous driver,
\[
f_{n,\Pi}^b(t,x_a)
=\sum_b\int_0^t\Lambda_{ab}^b(s)b_b'(s)\,ds.
\]
The bounded tangent matrix and integrable driver derivative allow Fubini.
For the fixed point \(\bar b_n\), the residual
\(\bar r=\bar f_n(X)-y\) therefore satisfies, almost everywhere,
\[
\dot{\bar r}
=\mathbb E\Lambda^{\bar b_n}\dot{\bar b}_n
=-\frac2m\mathbb E\Lambda^{\bar b_n}\bar r.
\tag{9}
\]
Pulling \(\bar r\) outside the expectation is valid because it is deterministic.
It would not be valid for the individual autonomous residuals, which do not
appear in this construction.

With \(\bar\rho=\|\bar r\|_2/\sqrt m\), (8) yields
\[
\bar\rho(t)\le Y e^{-2\lambda t}
\tag{10}
\]
as long as the control remains in the activity tube. This follows directly
by differentiating \(\|\bar r\|_2^2/m\); at zero residual it follows by
continuity and uniqueness. Hence
\[
\sum_a\int_0^t|d\bar b_{n,a}|
\le 2\int_0^t\bar\rho(s)\,ds
\le Y/\lambda.
\tag{11}
\]
Choose the fixed label threshold so \(Y/\lambda<S/2\).
On any existing local solution, (11) rules out its first exit from the
activity tube. At every endpoint of a constructed local interval the
variation is already below \(S/2\), so the uniform restart construction
in Section 1 applies. Iteration gives a unique global reference and preserves
the exponential estimate.

For \(Y=0\), the fixed point is the zero driver and stationary zero
predictor; the same conclusion holds without dividing by activity.
For positive labels, the readout, hidden matrix, and transformed coordinates
all have finite total variation on each member. Their increments after
time \(T\) are bounded by a constant times the remaining driver variation,
which is \(O(e^{-2\lambda T})\). They therefore converge as \(t\to\infty\).
Forward reconstruction gives convergence of every bounded-domain query
prediction, uniformly over the query ball for its differences.
Prediction boundedness permits expectation to pass to the endpoint.

The same fixed \(S\) can be chosen to satisfy the feedback theorem's
absorption requirement. The label threshold is decreased once more, if
needed, so the manuscript's actual-network activity bound is also at most
\(S\) on its fitting event. All these restrictions are width independent.

## 4. Original initialization, fluctuations, and adaptive training

The reference driver \(\bar b_n\) may depend on width, but it is deterministic.
The checked controlled fluctuation theorem is uniform over deterministic
drivers of variation at most \(S\). Thus it applies to this sequence of
drivers without an empirical-process supremum or random-driver substitution.
Reparametrization by the total variation of \(\bar b_n\) is deterministic
at every width and includes its full physical-time trajectory.

Couple the original and projected controlled networks by their first roots
and original hidden Gaussian matrix. On \(E_n\), their initializations and
entire trajectories agree. For every initialization and query, both
predictions have absolute value at most \(S\), because \(\|w\|_\infty\le S\)
and tanh features are bounded. Thus
\[
\begin{aligned}
\sup_t\left|\mathbb Ef_n^{\bar b_n}(t,x)
           -\mathbb Ef_{n,\Pi}^{\bar b_n}(t,x)\right|
&\le\mathbb E\sup_t
 |f_n^{\bar b_n}(t,x)-f_{n,\Pi}^{\bar b_n}(t,x)|\\
&\le2S\Pr(E_n^c)\le CSe^{-cn}.
\end{aligned}
\tag{12}
\]
The bound is uniform in the query. No conditioning on \(E_n\) is inserted
inside either expectation; the reference mean retains its intended law.
The original controlled flow exists even off \(E_n\): the readout is bounded,
the hidden matrix increment is bounded by \(S^2\), and the finite initial
matrix has finite norm almost surely.

Apply the original controlled fluctuation theorem and add (12).
For \(\eta_n=f_n^{\bar b_n}-\bar f_n\), this gives
\[
\mathbb E\int\sup_t|\eta_n(t,x)|^2\,d\mu(x)
+\sum_a\mathbb E\sup_t|\eta_n(t,x_a)|^2\le C/n.
\tag{13}
\]
The squared deterministic correction from (12) is exponentially smaller.
There is no population predictor in this step: the reference is the
projected finite expectation by definition.

On the actual fitting/operator/initial-Gram event \(G_n\), use the checked
pathwise feedback theorem with \(f_*=\bar f_n\).
The defining residual equation verifies its reference-control hypothesis;
(11) verifies the reference activity bound; the actual activity and initial
Gram bounds hold on \(G_n\). The result is
\[
\mathcal E_\mu(f_n,\bar f_n)
\le C_B\max_a\sup_t|\eta_n(t,x_a)|
  +\left(\int\sup_t|\eta_n(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]
Squaring and applying (13), without any independence assumption involving
\(G_n\), gives
\[
\mathbb E[\mathbf1_{G_n}\mathcal E_\mu(f_n,\bar f_n)^2]\le C/n.
\tag{14}
\]
For each fixed \(0<\delta<1\), take \(n\) large enough that
\(\Pr(G_n^c)\le\delta/2\), and apply Markov at squared threshold
\(2C/(\delta n)\). This proves the asserted fixed-confidence root-width
bound. The width threshold may depend on \(\delta\), as now explicitly
stated in the candidate.

This is not a claim of unconditional expected squared error \(C/n\) for
actual training: (14) includes the fitting event. Nor does it identify
\(\bar f_n\) with the expectation of the autonomous predictor. No moment
bound on the autonomous prediction outside the fitting event is needed.

For two actual runs, apply the one-run estimate at failure probability
\(\delta/2\) to each, use a union bound, and then the triangle inequality
through the same deterministic center. The resulting constant can be
absorbed into \(C_\delta\). Independence is unnecessary for the union bound;
the stated independent-run case is valid.

The metric keeps the time supremum inside the input integral throughout.
Both the reference and actual fitting trajectories have limits, so their
endpoint comparison is included without a limit/derivative interchange.

## 5. Qualitative identification is separate from a bias rate

The concentration result implies
\(\mathcal E_\mu(f_n,\bar f_n)\to0\) in probability. One may see this
directly from (14) and \(\Pr(G_n^c)\to0\):
\[
\Pr\{\mathcal E_\mu(f_n,\bar f_n)>\epsilon\}
\le\Pr(G_n^c)+C/(n\epsilon^2)\longrightarrow0.
\]
Combine this with the authorized manuscript's qualitative actual-population
convergence. The deterministic number
\[
D_n=\mathcal E_\mu(\bar f_n,f_\infty)
\]
is at most the sum of those two random distances, by the triangle inequality.
If \(D_n\) were bounded below by some \(\epsilon>0\) along a subsequence,
the sum would exceed \(\epsilon\) with probability one there, contradicting
its convergence to zero in probability. Hence \(D_n\to0\).

This supplies no numerical bound on \(D_n\). A deterministic displacement
of order \(n^{-1/4}\), for example, is compatible with the proved concentration
and qualitative convergence. The local profile response hypothesis H is
absent from the reference construction, its fitting proof, the controlled
fluctuation estimate, and the adaptive comparison. Its separate role is
to bound systematic displacement from the population at a rate.

Consequently the claimed distinction is valid in the fixed-confidence
topology of the theorem: a slower population approximation cannot be
explained solely by widening initialization-to-initialization trajectory
spread in this structured regime. A common finite-width bias remains open.

## Frozen inputs and audit status

The complete candidate was read, including the final clarity edits to the
confidence quantifier and definitions of \(Y\) and \(g(X)\).
Canonical-notation and rigorous-math requirements were applied.
The already checked same-study dependency files were used within the
assigned scope. No new scientific input was obtained from other studies.

SHA-256:

    a15921824dad13a27e396f37fdb31bdd7817d0700b0dff260dbe197c70ffe271  AUTONOMOUS_SELF_AVERAGING.md
    6a5b99cbaf1b7a905eb5666e77211e6e8ce705246d3146968c4b281a46568abb  CONTROLLED_FEEDBACK_STABILITY.md
    1ddda713770011e7be4eb589917aae2b4ee53fb1032d1c1bc7901903cd230e9c  PASSIVE_QUERY_FLUCTUATIONS.md

No substantive repair was needed. The Picard domain, restart argument,
expectation differentiation, positive-Gram bootstrap, and rare-event
accounting are expanded above to make the candidate's compact steps
explicit. This is collaborative internal checking, not a promotion review.
