# Independent check of the actual-network crossing bridge

Date: 2026-10-11. Review type: isolated mathematical reconstruction of a frozen candidate. No experiments, manuscript changes, Git writes, study-history reads, or other review reports were used.

## Verdict and scope

**PASS for the finite-time crossing theorem stated in equation (3).** I found no missing mathematical estimate in the passage from the readout-only comparator to the two actually trained networks. In particular, the proof obtains a width-uniform bound on the *centered independent-copy remainder*, which is sufficient after choosing one strictly positive label amplitude independent of width. It does not require an unjustified coordinatewise bound on first-layer movement.

For the requested upgrade

\[
\sup_{t\in(0,\infty]}
\frac{\sup_{x\in\mathcal X}|f_{\rm model}(t,x)-f_n(t,x)|}
     {\sup_{x\in\mathcal X}|f_n(t,x)-\widetilde f_n(t,x)|}
\xrightarrow{\mathbb P}0,
\]

the result supplies an obstruction on an admissible singleton test panel **if a zero denominator counts as failure**. This is the zero-denominator convention stated in the supplied compact-paper setup. If the proposed upgrade instead excludes zero-denominator times, the candidate has not proved its failure: it has not analyzed the compression error at, or near, the crossing. The candidate preserves that limitation.

The result does not refute the existing compact-paper ratio of two suprema over complete trajectories. Indeed, on the candidate's crossing event that paper's trajectory denominator is at least \(bY/\sqrt n\), by either of the strict inequalities at times one and two. A singleton crossing also does not establish a zero spatial supremum on the whole sphere or on a larger panel.

The complete scientific inputs read were:

- `ACTUAL_TIME_BRIDGE.md`, SHA256 `31f8a310b563c2acac6a2fd1c18cbe72681c4649359dce5a4283566f5f9447df`.
- `ACTUAL_CROSSING_QUOTIENT.md`, SHA256 `6b3601fa4bb3acafe420bd6ff0d3da69447b9cc17ff4f2753294ff8e8448a432`, added to the authorized scope after the bridge reconstruction; its separate verdict appears below.
- `paper/compact.tex`, SHA256 `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe`.
- The supervisor's neutral specification of the requested same-time ratio and its test-only Taylor domain.

The required rigorous-math and canonical-notation instructions, including the neural-network reference, were applied. No scientific source cited by the candidate was fetched. The arguments needed for the crossing are supplied inside the candidate; its references to earlier route notes are not necessary proof dependencies for this conclusion.

## Model, admissibility, and deterministic estimates

The training inputs are \(x_1=\sqrt2e_1\), \(x_2=\sqrt2e_2\), and the passive input is \(x_*=e_1+e_2\). All have norm \(\sqrt2\); the training inputs span \(\mathbb R^2\), and the passive direction is parallel to neither training direction. The labels are \(y=Y(1,-1)^\top\), so their RMS is precisely \(Y\). The assertion fixes a positive *label amplitude*; it does not use two positive individual labels. Opposite label signs are explicitly permitted by the compact-paper setup.

Writing \(A=W^{(1)}\), \(B=W^{(2)}\), and retaining the paper's readout \(w\), the forward pass is

\[
P_v=\phi(Av),\qquad Z_v=BP_v,\qquad H_v=\psi(Z_v),\qquad
f_v=\frac1n w^\top H_v,
\]

with \(\phi(z)=z+\tanh z\) and \(\psi(z)=\tanh z\). For any neuron vector \(z\in\mathbb R^n\), write \(\|z\|_n=\|z\|_2/\sqrt n\). The activations are nonaffine and holomorphic on a common sufficiently narrow strip. Their first derivatives are bounded on that strip, and the real derivatives needed in the proof are bounded. The lower activation's unbounded values are allowed by the source. Both hidden layers evolve in the candidate; the comparator alone freezes them.

For \(m=2\), the source's factor \(2/m\) is one. Its block mobilities therefore give exactly the three equations in candidate (5), including the \(1/n\) in the \(B\) equation and no such factor in the \(A\) or readout equations. With \(c=y-f\) and loss \(\mathcal L=\|c\|_2^2/2\), positive block mobilities imply \(\dot{\mathcal L}\le0\). Consequently \(\|c\|_2\le\sqrt2Y\), \(\sum_a|c_a|\le2Y\), and bounded upper features give \(\|w(t)\|_\infty\le2Yt\).

The change of coordinates is exact. Since \(1\le\phi'\le2\), the function

\[
\tau(z)=\int_0^z\frac{ds}{\phi'(s)}
\]

is an odd diffeomorphism, with inverse \(\Gamma\) satisfying \(1\le\Gamma'\le2\) and bounded \(\Gamma''\). Thus \(U_{ia}=\tau(A_{ia})\) satisfies

\[
\dot U_{:a}=c_a B^\top[w\odot\psi'(Z_a)].
\]

There is no lower-layer diagonal derivative gate in this vector field. For each of the three fixed queries, the row function
\(F_v(u)=\phi(v_1\Gamma(u_1)+v_2\Gamma(u_2))\)
has bounded first and second derivatives. These facts justify both the transformed dynamics and the later kernel-gradient comparison.

Under the initial operator-norm bounds in (10), the tube estimate is dimension independent. On the proposed tube, direct use of the preceding residual and readout bounds gives

\[
\frac{\|\dot U\|_F}{\sqrt n}\le36Y^2t,
\qquad \|\dot B\|_F\le80Y^2t.
\]

Initially every lower-feature RMS is at most 16. Bounded \(DF_v\) converts the integrated normalized \(U\) movement into an RMS feature increment; \(\|B-B_0\|_{\rm op}\le\|B-B_0\|_F\). A sufficiently small \(Y_0(T)>0\) therefore closes the margins 16 to 20 and 8 to 9 by a first-exit argument. No coordinate maximum of \(U-U_0\) is used.

In normalized coordinates \(\theta=(U/\sqrt n,B)\), \(\zeta=w/\sqrt n\), a unit hidden perturbation changes each \(P_v,Z_v,H_v\) by bounded RMS. Moreover,

\[
\|D_\theta c_a\|=O(Y),\qquad
\|D_\zeta c_a\|\le1,
\]

and, for \(D_a=w\odot\psi'(Z_a)\),

\[
\|D_a\|_n=O(Y),\qquad
\|d_\theta D_a\|_n\le C_TY\|d\theta\|,
\qquad
\|d_\zeta D_a\|_n\le C_T\|d\zeta\|.
\]

The hidden derivative uses the established bound on \(\|w\|_\infty\), not merely its RMS. The product rule now gives all four blocks in (13). The resulting variational equations, with initial values \((J_\theta,J_\zeta)=(I,0)\), give

\[
\|J_\theta\|\le C_T,\qquad
\|J_\zeta\|\le C_TY,\qquad
\|J_\theta-I\|\le C_TY^2.
\]

These estimates and the output derivative bound \(\|D_{\theta_0}f_v\|\le C_TY\) hold with constants uniform in width and in \(0<Y\le Y_0(T)\).

## Gaussian clipping and the kernel derivative

The clipping step is valid and is materially necessary to the stated use of Gaussian Poincare. It does not condition a Gaussian law on an operator-norm event. Euclidean projection onto the closed convex operator-norm ball is nonexpansive and equivariant under left and right orthogonal transformations. Consequently the map from the raw independent standard Gaussian matrices to \(\theta_0^c\) is \(1/\sqrt n\)-Lipschitz and preserves the lower-neuron sign reflections.

The stated net estimate is sufficient: a pair of \(1/4\)-nets gives an operator-norm bound by twice the largest net bilinear form. The failure probabilities are at most \(2\,9^{2n}e^{-8n}\) for \(B\) and \(2\,9^{n+2}e^{-8n}\) for normalized \(A\), both tending to zero. Clipped and canonical trajectories therefore agree exactly on an event whose probability tends to one. No root-width moment bound on the discarded raw trajectories is needed for this coupling argument.

For one lower-neuron reflection, the corresponding row of \(U\) and column of \(B\) change sign while \(Z,H,w,c\) stay unchanged. Thus each \(\Delta U_{ia}\) and each initialized coordinate

\[
C_i^0(a,b)=\left[B_0^\top\{\psi'(Z_a(0))\odot H_b(0)\}\right]_i
\]

has mean zero. The first has raw-Gaussian Lipschitz constant \(C_TY^2\): the \(\sqrt n\) coordinate conversion cancels the clipping map's \(1/\sqrt n\). The second has constant \(C_T\): its gradient in \(\theta_0\) is at most \(C_T\sqrt n\), and the same cancellation applies.

The exact Gaussian Poincare form required here is
\(\operatorname{Var}(X)\le\mathbb E\|\nabla X\|^2\)
for a Gaussian Sobolev function. All these functions are globally Lipschitz. Applying this inequality to a centered \(L\)-Lipschitz function and then to its square gives

\[
\mathbb EX^4\le4L^2\mathbb EX^2+(\mathbb EX^2)^2\le5L^4.
\]

Hence \(\mathbb E|\Delta U_{ia}|^4\le C_TY^8\) and \(\mathbb E|C_i^0|^4\le C_T\). Global Lipschitzness can be justified by composing the Lipschitz projection with the smooth flow on a neighborhood of each clipped initial point and applying the derivative bound along absolutely continuous line images; nondifferentiability of the projection on its exceptional set does not invalidate Poincare.

For the two-time feature kernel \(K_{ab}(s,t)=H_a(s)^\top H_b(t)/n\), the partial gradients in (26) have the correct normalization. The only term that cannot be bounded by a deterministic normalized displacement is

\[
\frac1n\sum_i |C_i^0|^2
\|DF_a(U_i(s))-DF_a(U_i(0))\|^2.
\]

Bounded \(D^2F_a\), Cauchy--Schwarz, and the two fourth-moment estimates bound its expectation by \(C_TY^4\). The two-coordinate row dimension is fixed. Every other gradient-difference term is deterministically \(O(Y^2)\). Composing with \(J_\theta(s)\) and \(J_\theta(t)\) therefore proves precisely

\[
\mathbb E\|D_{\theta_0}(K_{ab}(s,t)-K^0_{ab})\|^2\le C_TY^4.
\]

There is no hidden use of independence between the two coordinate quantities, no maximum-coordinate estimate, and no increasing-width derivative constant at this step.

## The actual-minus-frozen remainder

The Volterra identity is exact: integrate \(\dot w=\sum_b c_bH_b\), then pair with the current feature \(H_a(t)/n\). This gives the candidate's cross-time kernel, rather than a same-time kernel substituted into the integral.

Subtracting the readout-only comparator gives the integral equation (32). The uniform bound \(|K-K^0|\le C_TY^2\), residual bound \(|c_b|\le\sqrt2Y\), and integral Gronwall give errors \(O(Y^3)\) on the fixed horizon. Differentiating that exact equation produces (34), with all four terms present. Its inhomogeneous gradient terms have Gaussian \(L^2\) norm \(O(Y^3)\): respectively,

\[
|e_b|\,\|DK^0_{ba}\|=O(Y^3),\qquad
|\Delta K_{ba}|\,\|Dc_b\|=O(Y^3),\qquad
\|c_bD\Delta K_{ba}\|_{L^2}=O(Y^3).
\]

Minkowski and Gronwall consequently yield
\(\mathbb E\|D_{\theta_0}R(t)\|^2\le C_TY^6\)
for the passive error \(R=f_*-f_{{\rm RF},*}\). Composition with the clipping map followed by Poincare gives

\[
\operatorname{Var}(R_n^c(t))\le\frac{C_TY^6}{n}.
\]

For two independent copies, the means cancel exactly, so the difference has second moment at most \(2C_TY^6/n\). Coupling to the unclipped Gaussian networks and applying Chebyshev gives (39). This is a fixed-label, width-uniform probability bound of order \(Y^4\) after division by the crossing scale \(Y/\sqrt n\). It is not a claim that the normalized remainder converges to zero at fixed \(Y\).

## Frozen covariance, fixed labels, and transfer

The augmented lower population Gram is positive definite. A zero second moment would give an identically zero linear combination of the three lower features, by Gaussian full support. Its mixed derivative in the two independent input coordinates forces the test coefficient to vanish because \(\phi''\) is not identically zero; the two remaining coefficients then vanish separately. Thus the next Gaussian triple is nondegenerate, and applying coordinatewise tanh gives full support on \((-1,1)^3\).

The top population training Gram and test column are \(Q=qI_2\) and \(k=r(1,1)^\top\), with \(0<q<1\) and \(r>0\). Training independence and oddness give the diagonal Gram. Strict positivity of \(r\) follows by Gaussian covariance differentiation along positive cross-covariance: the derivative is the expectation of a product of strictly positive activation derivatives. This applies first to \(\phi\), then to \(\psi\). Thus the source gap is \(\gamma=q\), and its label condition is exactly \(Y\le(q/2)\beta^{-60}\).

The finite-depth central limit argument has the required hypotheses. Lower row-products are iid with finite moments because \(\phi\) has linear growth. Conditional on their empirical Gram, the upper preactivation rows are iid Gaussian. Near the positive-definite population Gram, their mean feature-product map is differentiable by dominated differentiation of the Gaussian density. Their conditional centered feature-products are bounded, so their characteristic-function expansion has a uniform cubic remainder. This proves joint convergence of the new conditional noise and the previous-layer fluctuation to independent Gaussian contributions. It justifies the covariance addition; no potentially negative cross-covariance was omitted.

For \(u=(1,-1)^\top\), the two projected final-row noises are

\[
H_*(H_1-H_2),\qquad r(H_1^2-H_2^2).
\]

Their covariance is positive definite: a constant linear combination must be constant on the open cube; setting \(H_1=H_2\) makes that constant zero, varying \(H_*\) with \(H_1\ne H_2\) removes the first coefficient, and varying \(H_1^2-H_2^2\) removes the second. Earlier-layer covariance is positive semidefinite and cannot cancel this contribution.

With \(h_t(s)=(1-e^{-ts})/s\) continuously extended at zero, the frozen output is exactly \(Yk_n^\top h_t(Q_n)u\). The matrix derivative at the scalar matrix \(qI_2\) is multiplication by \(h_t'(q)\), and the quadratic Taylor remainder is \(O_{\mathbb P}(n^{-1})\). Consequently its normalized limit is \(h_t(q)A+h_t'(q)B\), for the positive-definite Gaussian pair in (41). Independent-copy subtraction doubles that pair's covariance.

The two coefficient vectors at times one and two are linearly independent because

\[
-\frac{h_t'(q)}{h_t(q)}=\frac1q-\frac{t}{e^{qt}-1}
\]

is strictly increasing for \(t>0\). The resulting two-time Gaussian law has an everywhere positive density. Therefore the fixed-margin opposite-sign event in (46) has limiting probability \(p_b>0\), independent of \(Y\).

Choose \(b>0\) first, then one \(Y>0\) below the tube cap, the unchanged source label cap, and the bound making \(4C_2Y^4/b^2<p_b/2\). All three bounds are positive and independent of width. The union bound at the two fixed times then leaves a positive limiting probability of

\[
f_n(1,x_*)-\widetilde f_n(1,x_*)>\frac{bY}{\sqrt n},\qquad
f_n(2,x_*)-\widetilde f_n(2,x_*)<-\frac{bY}{\sqrt n}.
\]

This subtraction of failure probabilities requires no independence between the frozen sign event and the remainder event. Continuity yields an actual crossing in \((1,2)\).

## Limits of this check

The proof establishes a finite-time property of networks training every parameter block. It does not establish a property of their fitted endpoints, nor require one to obtain the obstruction. The optional appeal to the canonical fitting theorem was not independently checked: its proof is in a TeX input outside the assigned scientific scope. No such missing proof input is needed for the displayed crossing theorem.

The result applies to the specified mixed activations and symmetric, opposite-label example. It does not establish the same bridge for an all-tanh network, for arbitrary labels, for arbitrary separated test queries, or for arbitrary full-span training problems. A single admissible example is sufficient to obstruct a universal same-time Taylor claim under the stated failure convention.

No promotion decision follows from this check. Its mathematical verdict concerns the frozen candidate and the qualifications above.

## Separate check of the analytic quotient addendum

**PASS for fixed-time atomlessness, and PASS for the stated conditional quotient theorem.** This addendum does not prove that a particular Taylor construction meets its analytic-path and nonexactness assumptions. Consequently it does not by itself establish an unconditional, convention-independent failure of that construction's ratio.

For clarity, let \(\mathscr F_n\) denote the sigma-field generated jointly by the primary initialization and all randomness used by the compressor. The addendum explicitly requires the second dense initialization to be independent of \(\mathscr F_n\). This is exactly the joint independence needed by its conditioning argument; separate marginal independence would not suffice. The revised addendum was read completely and its new hash verified. The joint-independence wording issue identified during this check is resolved.

The global existence estimate is correct. For arbitrary finite \(A_0,B_0\) and zero readout, set

\[
M_A(t)=\frac{\|A(t)\|_F}{\sqrt n},\qquad M_B(t)=\|B(t)\|_F.
\]

The decreasing loss and bounded top activation still give \(\sum_a|c_a|\le2Y\), \(\|w(t)\|_n\le2Yt\). Using \(|\phi'|\le2\) and \(\|P_a\|_n\le2M_A\), the exact equations imply

\[
D^+M_A\le8Y^2tM_B,\qquad D^+M_B\le8Y^2tM_A.
\]

Their sum is bounded by its initial value times \(e^{4Y^2t^2}\). Together with the readout bound, this prevents finite-time escape at every finite initial point. The vector field is real analytic on the full real parameter space. Local uniqueness and the bounded finite trajectory allow analytic local flow maps to be composed over a finite cover of the time interval. Thus the prediction is real analytic in \((A_0,B_0)\) at every initial point for each fixed \(t>0\), and in time along every positive-time trajectory.

The one-neuron witness proves nonconstancy for every width, not merely asymptotically. Initially set \((A_0)_{11}=a>0\), \((B_0)_{11}=\varepsilon\), with all other coordinates zero. The proposed active subsystem is invariant: every inactive lower neuron has a zero mixer column and zero lower features, and every inactive upper neuron has a zero mixer row and zero readout. At \(\varepsilon=0\), all outputs remain zero. The first variations of the two active lower weights vanish, and the mixer/readout first variations obey

\[
\dot b_1=\frac{Y\phi(a)}n w_1,\qquad
\dot w_1=Y\phi(a)b_1,\qquad (b_1(0),w_1(0))=(1,0).
\]

For \(k=Y\phi(a)/\sqrt n\), their solution is \(b_1=\cosh(kt)\), \(w_1=\sqrt n\sinh(kt)\). The passive prediction therefore has Taylor coefficient

\[
f_n(t,x_*)=
\frac{\varepsilon^2}{\sqrt n}\phi(a/\sqrt2)
\sinh(kt)\cosh(kt)+O(\varepsilon^3).
\]

It is strictly positive at quadratic order for every \(n\ge1\) and \(t>0\). This verifies nonconstancy of the analytic initialization map with the actual hidden-layer dynamics included.

The supplied null-level-set argument is sufficient. A nonconstant real-analytic function on connected Euclidean space cannot have all derivatives vanish at one of its zeros. A nonzero finite-order directional derivative remains nonzero in a small ball. Along each parallel line segment in that ball, repeated Rolle's theorem bounds the number of zeros by the derivative order. Fubini and a countable cover prove that every level set is Lebesgue null. The canonical initialization has a nonsingular Gaussian density at every fixed width. Therefore

\[
\Pr\{f_n(t,x_*)=z\}=0
\quad\text{for all fixed }n\ge1,\ t>0,\ z\in\mathbb R.
\]

Finally, condition on \(\mathscr F_n\). On the event that the analytic error
\(e_n(t)=f_{{\rm comp},n}(t,x_*)-f_n(t,x_*)\)
is not identically zero on \((1,2)\), its zero set there is discrete and countable. Each such time and the primary prediction at that time are now fixed. Joint independence and the preceding atomlessness make the probability of equality with the second prediction zero at every member of this countable set. Their countable union therefore has probability zero. Joint measurability and continuous paths suffice to make this conditioning and the isolated-zero enumeration legitimate, as stated in the addendum.

On the strict sign-change event, the analytic dense difference \(g_n=f_n-\widetilde f_n\) is nonidentically zero and has an isolated interior root \(\tau\). The conditional argument gives \(e_n(\tau)\ne0\) almost surely on the nonexactness event. Continuity then gives

\[
\sup_{\substack{1<t<2\\g_n(t)\ne0}}
\frac{|e_n(t)|}{|g_n(t)|}=+\infty.
\]

If the probability of identically zero error tends to zero, subtracting that probability from the bridge's positive crossing probability proves a positive limiting probability of this divergence. This final inference does not assume that nonexactness and crossing are independent. The required joint independence, analytic compressor paths, and high-probability nonexactness are the precise conditions of the checked strengthening; the latter two remain unverified for the specific Taylor construction.
