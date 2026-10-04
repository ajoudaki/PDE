# Finite-neuron replacement: exact scalar expansion and the unresolved terms

2026-10-04. Bounded, scoped continuation authorized to use this study and
`dense_cutoff_population_rate_20261001`. This report is a new proof attempt,
not an independent promotion review. No experiment, maintained-source edit,
Git mutation, or write outside this report was performed.

**Outcome.** Replacing independent incoming Gaussian rows reduces the
Efron–Stein sum to (Ln) terms. Full-neuron deletion supplies the correct
independent reference for each term. However, the existing deletion theorem
does not establish a scalar replacement influence of order (1/n). Its
linear scalar term contains a prediction-directed response norm that is not
bounded by the existing trace estimates. Its nonlinear retained-state
remainder also loses the required scale. The formulas below exhibit both
terms, with the actual adaptive residual and learned edges retained. The
strict all-time, whole-sphere dense-versus-independent-dense theorem remains
open; this is not a counterexample to that theorem.

The four assigned primary sources were read completely:
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`,
`UNBOUNDED_INSERTION_CHECK.md`, and `GENERAL_SELF_AVERAGING.md` in the
authorized prior study. This study's `INTEGRATED_DENSE_VARIABILITY_ROUTE.md`
was also read completely. The canonical-notation/neural, rigorous-proof,
and conjecture-investigation instructions and the maintained notation
contract were applied. The conclusions below use the explicit deletion
calculations rather than their recorded PASS labels.

## 1. Model, target, and independent blocks

Fix the hidden depth (L\ge2), input dimension (d), a finite dataset
((v_a,y_a)_{a=1}^m), and positive weights (p_a) summing to one. Here
(v_a=x_a/\sqrt d). The dense network is
\[
 z^{(1)}(v)=W^{(1)}v,\qquad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\qquad
 h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\qquad
 f_n(t,v)=\frac1n w(t)^\top h^{(L)}(t,v).
 \tag{1}
\]
The loss is (\sum_a p_a r_a^2), where (r_a=f_n(t,v_a)-y_a),
with mobilities ((n,1,\ldots,1,n)). First weights have independent
(N(0,1)) entries, hidden weights independent (N(0,1/n)) entries,
all initialized blocks are independent, and (w(0)=0). This explicitly
uses the zero-readout convention of the assigned sources. Each activation
is (C^3) with bounded first three derivatives; values may grow linearly.
The limiting initialized feature Gram has a positive gap on the compatible
weighted data quotient, and the fixed label RMS
(Y=(\sum_a p_a y_a^2)^{1/2}) is sufficiently small as in those sources.

Write the independent standard Gaussian incoming row blocks as
\[
 G_{1i}=W^{(1)}_{0,i,:}\in\mathbb R^d,\qquad
 G_{ji}=\sqrt n W^{(j)}_{0,i,:}\in\mathbb R^n
 \quad(2\le j\le L),\qquad 1\le i\le n.
 \tag{2}
\]
There are (Ln) independent blocks, despite the (O(n^2)) scalar
coordinates. Let (G^{[ji]}) replace just (G_{ji}) by an independent
copy, leaving all other initialization unchanged. Both networks train with
their own residuals and are compared at the same physical time.

For a scalar square-integrable function (F(G)), the Efron–Stein
inequality is
\[
 \operatorname{Var}F\le\frac12\sum_{j,i}
   \mathbb E|F(G)-F(G^{[ji]})|^2.
 \tag{3}
\]
To recall why the factor is correct, conditional on all blocks except one,
half the squared independent-replacement difference equals the conditional
variance in that block. Iterating the variance decomposition over independent
blocks, with conditional Jensen for the functions averaged over later blocks,
bounds the total variance by the sum of these conditional variances. Thus
(\|F-F^{[ji]}\|_{L^2}\le C/n) for every block would give variance
(O(1/n)). This implication requires global square integrability and the
stated replacement bounds, not just bounds on a likely event.

The requested conclusion is stronger than this fixed-scalar implication:
\[
 \Pr\left\{\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_n(t,v)-f_n'(t,v)|\le C_\delta n^{-1/2}\right\}\ge1-\delta.
 \tag{4}
\]
It includes all physical times and the fitted endpoint. A moment estimate
for time/query increments and legitimate localization are still needed
after fixed-scalar replacement. No time change is made in the optimizer.

## 2. Why full-neuron cavities match row replacement

For (1<j<L), delete neuron (i) at layer (j), its incoming row,
and its outgoing column. Keep normalization (n) and train the retained
rectangular network autonomously. Its omitted initialized directions are
\[
 \xi=W^{(j+1)}_{0,:,i},\qquad
 \eta=W^{(j)\top}_{0,i,:},\qquad
 \xi,\eta\sim N(0,I_n/n).
 \tag{5}
\]
Conditional on the retained initialization, these vectors are independent.
The original network and its incoming-row replacement share the same cavity
and the same outgoing vector \(\xi\); their incoming vectors are
\(\eta\) and an independent \(\eta'\). The cavity is independent
of all three. Consequently a scalar full-to-cavity (L^p) bound (C_p/n)
would imply the row-replacement bound (2C_p/n) by the triangle inequality.
The overlapping sets of weights removed by cavities at different neurons
do not affect the independence of the original row blocks in (2).

At (j=1), the omitted first row has dimension (d), and there is no
reverse force on retained lower parameters. At (j=L), remove the incoming
row and its readout coordinate. That readout coordinate starts at zero and
is not an additional random block. The top-layer prediction offset must
still enter the retained residual, as described below. Deletion removes
the activation itself; it does not set a preactivation to zero when
\(\phi_j(0)\ne0\).

## 3. Exact retained dynamics and first scalar variation

Use the retained mobility-Euclidean parameter vector
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w).
\]
An external vector (e_a\in\mathbb R^n) enters the retained
preactivation at layer (j+1). Let
\(\mathcal F_a(\Theta,e_a)=nf_a(\Theta,e_a)\).
Let (q_a\in\mathbb R^n) be the reverse source at layer (j-1).
The exact retained equation for an interior deletion is
\[
 \dot\Theta=-2\sum_a p_a r_a
 \left[\nabla_\Theta\mathcal F_a(\Theta,e_a)
       +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right],
 \qquad r_a=\mathcal F_a(\Theta,e_a)/n-y_a.
 \tag{6}
\]
For the actual full path, put
\[
 a_a=h_{a,i}^{(j)},\qquad b_a=\delta_{a,i}^{(j)},\qquad
 e_a=\xi a_a+\zeta_a,\qquad q_a=\eta b_a+\chi_a,
 \tag{7}
\]
where the exact learned-edge corrections are
\[
 \zeta_a=(W^{(j+1)}_{:,i}-\xi)a_a,\qquad
 \chi_a=(W^{(j)\top}_{i,:}-\eta)b_a.
 \tag{8}
\]
Here (k_a^{(L)}=w),
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\), and
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\).
Thus no residual factor is hidden in (b_a).

Let a superscript (0) indicate the autonomous zero-source cavity.
Along it define
\[
 \begin{gathered}
 g_a=\nabla_\Theta\mathcal F_a^0,\qquad
 H_a=D_\Theta^2\mathcal F_a^0,\qquad
 d_a=\delta_a^{(j+1),0},\\
 B_a=D_\Theta\delta_a^{(j+1),0},\qquad
 C_a=D_\Theta h_a^{(j-1),0}.
 \end{gathered}
\]
Let (J(t,s)) be its variational propagator. Differentiation of the
actual residual in (6) gives
\[
 \partial_tJ(t,s)=
 \left[-\frac2n\sum_a p_ag_ag_a^\top
       -2\sum_a p_ar_a^0H_a\right]J(t,s),\qquad J(s,s)=I.
 \tag{9}
\]
The external derivatives of (6) at zero sources are
\[
 P_a=-\frac{2p_a}{n}g_ad_a^\top,\qquad
 Q_a=-2p_ar_a^0B_a^\top,\qquad
 T_a=-2p_ar_a^0C_a^\top.
 \tag{10}
\]
In particular (P_a) is an adaptive-residual term and has no multiplier
\(r_a^0\). Discarding it, or integrating it using residual activity,
would change the problem. The reverse term (T_a) is absent at (j=1).

Temporarily freeze deterministic scalar control paths (a_a,b_a), as
the local deletion proof does before its control-net argument. Its first
retained variation is
\[
 V(t)=\sum_a\int_0^tJ(t,s)
 \left[(P_a+Q_a)\xi a_a(s)+T_a\eta b_a(s)\right]ds.
 \tag{11}
\]
For a terminal query (v), put
\(g_v(t)=\nabla_\Theta\mathcal F_v^0(t)\),
\(d_v(t)=\delta_v^{(j+1),0}(t)\), and freeze also its terminal
activation control (a_v(t)). The first variation of the normalized
prediction is exactly
\[
 L_v(t)=\frac1n\left[g_v(t)^\top V(t)
                         +d_v(t)^\top\xi a_v(t)\right]
       =\frac1n\left[\xi^\top A_\xi(t,v)
                          +\eta^\top A_\eta(t,v)\right],
 \tag{12}
\]
where the conditional deterministic coefficients are
\[
 \begin{aligned}
 A_\xi(t,v)&=a_v(t)d_v(t)
   +\sum_a\int_0^t a_a(s)(P_a+Q_a)^\top
                          J(t,s)^\top g_v(t)\,ds,\\
 A_\eta(t,v)&=\sum_a\int_0^t b_a(s)T_a^\top
                          J(t,s)^\top g_v(t)\,ds.
 \end{aligned}
 \tag{13}
\]
Conditional Gaussian integration now gives an exact scalar identity:
\[
 \mathbb E[L_v(t)^2\mid\text{cavity, fixed controls}]
       =\frac{\|A_\xi(t,v)\|_2^2+
                         \|A_\eta(t,v)\|_2^2}{n^3}.
 \tag{14}
\]
This is the concrete gain the route seeks: coefficients of size
\(O(\sqrt n)\) give scalar size \(O(1/n)\), even when the
retained Euclidean variation is only \(O(1)\). It also exposes the
first missing term without a nonlinear approximation.

The common outgoing vector in the two row-replacement systems does not
resolve this issue. In the auxiliary calculation with the same frozen
controls in both copies, its contribution cancels and
\[
 L_v(t;\eta)-L_v(t;\eta')
      =\frac{(\eta-\eta')^\top A_\eta(t,v)}n,\qquad
 \mathbb E|L_v(t;\eta)-L_v(t;\eta')|^2
      =\frac{2\|A_\eta(t,v)\|_2^2}{n^3}.
\]
Thus the reverse prediction-directed coefficient remains even after this
useful cancellation. In the actual copies the controls also change, so
the cancellation cannot remove their additional forward contribution.

For example the reverse coefficient contains
\[
 -2\sum_a p_a\int_0^t r_a^0(s)b_a(s)
       C_a(s)J(t,s)^\top g_v(t)\,ds,
 \tag{15}
\]
and the forward coefficient contains the analogous
\(B_a(s)J(t,s)^\top g_v(t)\), together with
\(d_a(s)g_a(s)^\top J(t,s)^\top g_v(t)/n\) from (P_a).
The local proof controls normalized traces with two response-matrix
endpoints, for example
\(n^{-1}\operatorname{tr}(B_vJ B_a^\top)\). It does not control
the prediction-vector endpoints in (15).

Even a bound
\(\|J-U_0\|_{\mathrm{HS}}\le C\sqrt n\), with (U_0)
contractive and \(\|g_v\|_2\le C\sqrt n\), gives only
\(\|(J-U_0)^\top g_v\|_2\le Cn\) by these norms. The
available weak operator bound supplies the better but still growing
\(Cn^{1/1000}\sqrt n\) on the stopped interval. Neither is
the width-independent bound needed in (14). Rank-one adaptive terms
have small normalized trace, but rank alone does not make their action
on (g_v) small. This calculation identifies a limitation of the
available estimates, not a neural counterexample.

## 4. Adaptive controls and the complete nonlinear remainder

Equation (14) is conditional on deterministic controls. In the actual
network, (a_a,b_a) depend on the omitted Gaussian vectors. The source
proof correctly establishes uniformity over a control class before
substituting them. Its control net has
\[
 \log N_n\le Cn^{5/8}(\log n)^C,
 \tag{16}
\]
and its uniform Gaussian conclusions use thresholds (n^{-1/10}).
Those choices are appropriate for a vanishing retained-coordinate error.
They cannot be reused to claim a scalar (C/n) bound: even if every
fixed-control scalar had standard deviation (C/n), its Gaussian tail
at a fixed multiple of (1/n) has only a constant exponent, which does
not dominate (16). A direct union bound would spend the factor
\(\sqrt{\log N_n}\). The actual control class may admit a better
stochastic estimate, but that estimate has not been proved in the sources.

There is a separate nonlinear accuracy problem. Write the exact retained
difference as
\[
 \Theta(t)-\Theta^0(t)=V(t)+U(t).
\]
For a fixed terminal query, augment the argument of \(\mathcal F_v\)
by its external preactivation. Define the exact scalar Taylor remainder
\[
 \begin{aligned}
 R_v^{\rm out}(t)=\int_0^1(1-\theta)\,
 D^2\mathcal F_v\bigl((\Theta^0,0)
       +\theta(V+U,e_v)\bigr)
       [(V+U,e_v),(V+U,e_v)]\,d\theta.
 \end{aligned}
 \tag{17}
\]
Since (e_v=\xi a_v+\zeta_v), the full scalar deletion difference is
\[
 f_n(t,v)-f_n^0(t,v)
 =L_v(t)+\frac1n g_v(t)^\top U(t)
          +\frac1n d_v(t)^\top\zeta_v(t)
          +\frac1n R_v^{\rm out}(t).
 \tag{18}
\]
This is an identity, not a neglect of higher-order flow effects. In
particular (U) contains the learned-edge forces (8), the nonlinear
dependence of all forward and backward quantities, and residual adaptation.

One can also display its exact forcing. Let \(\mathcal V(\Theta,e,q)\)
be the right side of (6), let
\(A_0=D_\Theta\mathcal V(\Theta^0,0,0)\), and set
\[
 \begin{aligned}
 R^{\rm flow}(s)={}&\mathcal V(\Theta^0+V+U,e,q)
       -\mathcal V(\Theta^0,0,0)-A_0(V+U)\\
       &-\sum_a[(P_a+Q_a)\xi a_a+T_a\eta b_a].
 \end{aligned}
\]
Then
\[
 U(t)=\int_0^tJ(t,s)R^{\rm flow}(s)\,ds,\qquad
 \frac{g_v(t)^\top U(t)}n
   =\frac1n\int_0^t
       [J(t,s)^\top g_v(t)]^\top R^{\rm flow}(s)\,ds.
 \tag{19}
\]
Thus the unproved nonlinear cancellation is a definite scalar pairing
between the terminal prediction adjoint and the full insertion remainder.
It is not merely a requirement that the original state distance improve.

The proved local estimates, on their common stopped prefix, are
\[
 \|V(t)\|_2\le n^{1/100},\qquad
 \|U(t)\|_2\le n^{-1/25}.
 \tag{20}
\]
For a training query the physical tube gives \(\|g_a\|_2\le C\sqrt n\).
Consequently these estimates supply only
\[
 \frac{|g_a^\top U|}{n}\le Cn^{-27/50}.
 \tag{21}
\]
This is approximately (n^{-0.54}), not (n^{-1}). Squaring it and
summing (Ln) terms gives (O(n^{-2/25})), rather than the desired
(O(n^{-1})). This diagnoses the insufficiency of the existing bound;
it does not claim that the actual remainder has this larger size.

Even the favorable direct scalar Taylor bound for a training query is
only
\[
 \frac{|R_a^{\rm out}|}{n}
 \le C(\log n)^C n^{-49/50}
 \tag{22}
\]
when the source proof's augmented Hessian bound and linear radius in (20)
are used. The learned-edge corrections have Euclidean size
\(n^{-1/2}(\log n)^C\), so their direct scalar contribution has the
right power \(n^{-1}\), but still logarithmic envelopes. Removing
those envelopes requires actual control moments. Extending these estimates
to off-training queries and their sphere increments is an additional
obligation, not supplied by the training-coordinate insertion event.

At the top layer the exact equation is instead
\[
 \dot\Theta=-2\sum_a p_a(r_a^0+d_a^{\rm out})
 \left[\nabla_\Theta\mathcal F_a^{\rm ret}
       +D_\Theta h_a^{(L-1)\top}q_a\right],\qquad
 d_a^{\rm out}=\frac{w_i h_{a,i}^{(L)}}n.
 \tag{23}
\]
The omitted output \(d_a^{\rm out}\) multiplies both the retained
gradient and reverse force. Both products must be included in
\(R^{\rm flow}\), exactly as in the assigned unbounded insertion
correction. Their smallness for the existing local theorem does not by
itself establish scalar (1/n) accuracy. The first layer drops the
reverse source but retains the forward, adaptive-residual, and nonlinear
terms. Therefore the boundary layers do not remove all of the identified
obligations.

## 5. Why the existing likely event does not localize Efron–Stein

Let \(\Omega_n\) be the inherited all-time fitting/carrier event,
with \(\Pr(\Omega_n^c)=\varepsilon_n\to0\), and let (A) be
the fixed prediction amplitude bound on that event. Suppose, optimistically,
that the required scalar replacement estimate has been proved whenever both
initializations belong to \(\Omega_n\). The globally bounded auxiliary
observable \(\widehat F=\mathbf1_{\Omega_n}F\) then satisfies
\[
 \mathbb E|\widehat F(G)-\widehat F(G^{[ji]})|^2
 \le \mathbb E[\mathbf1_{\Omega_n\cap\Omega_n^{[ji]}}
                   |F(G)-F(G^{[ji]})|^2]
       +2A^2\varepsilon_n.
 \tag{24}
\]
Thus direct use of (3) adds (O(n\varepsilon_n)), and the known
\(\varepsilon_n=o(1)\) gives no root-width variance bound. The
sufficient bound for this particular truncation would be
\(\varepsilon_n=O(n^{-2})\); no such bound is established by the
fixed-degree-then-width stopping argument. The true probability of a
replacement crossing the event boundary could be smaller, but that too
would need a proof. For (L^p) influences of size (1/n), this crude
truncation would require corresponding (O(n^{-p})) tail control.

The finite-neuron reference can be stopped on its own cavity-measurable
event and set to zero if that event fails. This correctly preserves its
independence from the omitted Gaussian vectors. It does not construct a
single global observable \(\widehat F\), agreeing with the full
prediction on \(\Omega_n\), whose influences satisfy (3) at the
desired scale for all row replacements.

The global Gaussian Lipschitz extension in
`GENERAL_SELF_AVERAGING.md` solves this localization issue for the
near-root bound. Its Lipschitz constant retains
\(e^{C\sqrt{\log n}}/\sqrt n\). It supplies neither the proposed
strict scalar row influence nor a strict-rate replacement extension.

## 6. The all-time, whole-sphere bridge, conditional on genuinely new inputs

For clarity, a sufficient replacement program can be specified without
claiming it has been completed. Compactify time only for the proof by
\(u=1-e^{-\kappa t}\in[0,1]\). Suppose a continuous global
auxiliary family \(\widehat f_n(G;u,v)\), equal to the actual
flow on \(\Omega_n\), has deterministic initial value zero and,
for one fixed (p>2(d+1)), every independent row replacement obeys
\[
 \bigl\|[\widehat f_n(u,v)-\widehat f_n(u',v')]
       -[\widehat f_n^{[ji]}(u,v)-\widehat f_n^{[ji]}(u',v')]
       \bigr\|_{L^p}
 \le\frac{C_p}{n}
       (|u-u'|+\|v-v'\|_2)^{1/2}.
 \tag{25}
\]
This is a precise new input, not an assertion about the known flow.
Here is the implication to (4). Reveal the (Ln) independent row
blocks sequentially. Each Doob martingale difference of a scalar
observable has (L^p) norm at most its corresponding independent
replacement difference, by conditional Jensen. For (p\ge2),
the elementary (L^p) martingale estimate is
\[
 \left\|\sum_k D_k\right\|_{L^p}^2
       \le(p-1)\sum_k\|D_k\|_{L^p}^2.
 \tag{26}
\]
One proof uses the second derivative bound
\(D^2\|X\|_p^2[Z,Z]\le2(p-1)\|Z\|_p^2\), obtained by
twice differentiating \((\mathbb E|X|^p)^{2/p}\) and applying
Hölder. The first derivative term has zero expectation for a martingale
increment because its coefficient is measurable with respect to the past.
Taylor's integral formula, smoothing at zero if needed, and induction give
(26). Hence (25) gives centered increments of order
\(n^{-1/2}(|u-u'|+\|v-v'\|)^{1/2}\).

Dyadic nets of \([0,1]\times S^{d-1}\) can be chosen with at most
\(C_d2^{k(d+1)}\) parent-child edges at level (k). The
\(L^p\) norm of the largest centered increment at that level is at
most
\[
 C_p n^{-1/2}2^{-k/2+k(d+1)/p}.
\]
The sum converges. Telescoping from (u=0), continuity, and the
triangle inequality in \(L^p\) give the strict-root centered full
supremum. Apply Markov to both copies, use the same deterministic center,
and discard only the two final events \(\Omega_n^c\), whose
probabilities tend to zero. This proves (4) from (25) and the existence
of the stated global family. A fixed-query variance estimate alone does
not provide that family or its increment bounds.

## 7. Decision from this bounded pass

The route is concrete but unclosed. The smallest new scalar object to
estimate is (13), especially its reverse term (15), followed by the
adjoint pairing of the exact nonlinear remainder in (19). Gaussian
reinsertion does reveal the (1/n) normalization. It does not eliminate
the prediction-adjoint dependence: conditional variance converts that
dependence into a squared response norm.

The existing two-endpoint trace theorem, the vanishing retained-coordinate
remainder, and the (1-o(1)) stopping probability solve different parts
of the carrier proof. None can be substituted for the missing scalar
norm, scalar remainder, adaptive-control, or global-localization estimate.
The proved whole-sphere near-root result is unchanged. No new hypothesis
is appended to a purported strict theorem, and no negative statement about
the actual neural model is inferred from these proof losses.
