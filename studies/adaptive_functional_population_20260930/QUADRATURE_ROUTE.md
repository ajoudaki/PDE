# Population quadrature and causal history panels

Status: frozen independent theoretical route, 2026-09-30. Scientific input was only the supervisor's architecture and task statement. No other studies, book passages, literature, or another route's conclusions were read. This note proves exact identities and a conditional compact-horizon approximation theorem. It does **not** claim the missing deep width-uniform stability theorem.

## Contract and main finding

Keep the specified finite-width deep network, the entire realized frozen Gaussian initialization, and all trained layers. Approximate the data law by a positive measure with (p) input atoms; approximate learned hidden-matrix history by (q) causal panels in the residual clock. The resulting algorithm has learned state (O(Lnpq+nd)), is autonomous and restartable, and never needs a dense reference trajectory. Its exact error split is

\[
 \text{population-flow error} + \text{history approximation error}.
\]

A one-reference Hilbert-space sampling argument gives a genuinely (p^{-1/2}) source estimate, independent of (m,n,d), despite subsequent adaptive training. Together with a **separate width-uniform stability assumption**, it yields an observable bound of order

\[
 C_T\bigl(p^{-1/2}\delta^{-1/2}+q^{-1}\bigr)
\]

with probability at least (1-\delta). The source bound alone does not prove this statement. For deep networks the required stability does not follow from bounded activations, bounded normalized inputs, bounded initial operator norms, or ordinary loss dissipation. The difficult quantity in the direct parameter-space proof is the neuronwise size of the propagated backward response. This obstruction concerns that proof route, not an impossibility theorem for the desired closure.

For one hidden layer, the needed stability bound *does* follow from the assumptions and the resulting population theorem is unconditional for each fixed initialization. That shallow case does not settle the deep target.

## 1. Canonical system and normalized parameter geometry

Write (z=x/\sqrt d), and assume (\|z\|_2\le R) and \(|f_*(x)|\le Y\) on the support of the probability law (\mu). A finite dataset of arbitrary size is the special case of a finite atomic probability law. No smoothness of the deterministic labels is needed for the sampling source estimate. Smoothness without numerical regularity bounds would not by itself give a deterministic cubature rate.

Let (B_j=\|\phi^{(j)}\|_\infty), (j=0,1,2), and

\[
 a_1=W_1z,\quad h_1=\phi(a_1),\qquad
 a_l=W_lh_{l-1},\quad h_l=\phi(a_l),\qquad
 f_\theta=\langle w,h_L\rangle_n,
\]

where \(\langle u,v\rangle_n=u^Tv/n\), \(|u|_n=\|u\|_2/\sqrt n\), and (w(0)=0). Define

\[
 \delta_L=w\odot\phi'(a_L),\qquad
 \delta_l=\phi'(a_l)\odot W_{l+1}^T\delta_{l+1}.
\]

For (W_l=W_l^0+A_l), the learned parameter space has norm

\[
 \|\theta\|_{\mathcal H_n}^2
 =|w|_n^2+\|A_1\|_F^2/n+\sum_{l=2}^L\|A_l\|_F^2.
\]

The given equations are exactly the negative gradient flow of
(\mathcal R_\nu(\theta)=\int(f_\theta-f_*)^2d\nu)
in this Hilbert space. For one input, the negative gradient is

\[
 G_x(\theta)=\left(
 -2r(x)h_L(x),\;
 -2r(x)\delta_1(x)z^T,\;
 \left[-\frac{2r(x)}n\delta_l(x)h_{l-1}(x)^T\right]_{l=2}^L
 \right),
\]

and (F_\nu(\theta)=\int G_x(\theta)d\nu(x)).

This normalization is essential: an outer product (uv^T/n) has Frobenius norm (|u|_n|v|_n), and an (n\)-by-(d) product (uz^T) has first-layer norm (|u|_n\|z\|_2). These facts remove artificial width factors from the *source* estimate.

## 2. Uniform finite-clock bounds; no dense trajectory is needed

For any positive probability measure \(\nu\), put

\[
 \rho_\nu(t)=\|r_\theta(t,\cdot)\|_{L^2(\nu)},\qquad
 \dot\tau=\rho_\nu,\quad \tau(0)=0.
\]

At \(\rho_\nu=0\), all parameter velocities vanish; physical-time equations below never divide by \(\rho_\nu\).

The same bounds hold for exact gradient flow and for the history-panel algorithm in Section 3. Indeed, that algorithm only replaces each right factor (h_{l-1}) in a hidden-weight update by an earlier vector bounded by (B_0) in (|\cdot|_n).

For a clock bound (s\), define recursively

\[
 M(s)=2B_0s,
\]
\[
 D_l(s)=B_1^{L-l+1}M(s)\prod_{j=l+1}^LK_j(s),\qquad
 K_l(s)=\|W_l^0\|_{\mathrm{op}}+
          2B_0\int_0^sD_l(u)\,du\quad(l=L,L-1,\ldots,2).
\]

The descending recursion is well defined because (D_l) uses only (K_j) with (j>l). Define (D_1) by the same product formula. Directly integrating the equations gives, while \(\tau\le s\),

\[
 |w|_n,\ \|w\|_\infty\le M(s),\qquad
 \|W_l\|_{\mathrm{op}}\le K_l(s),\qquad
 \sup_x|\delta_l(x)|_n\le D_l(s).
\]

For example, 
\(\|\dot A_l\|_F\le2\rho_\nu B_0D_l\) for (l\ge2),
\(\|\dot A_1\|_F/\sqrt n\le2\rho_\nu RD_1\),
and 
\(\|\dot w\|_\infty\le2B_0\rho_\nu\).
No estimate on the norm of (W_1^0) is used. The frozen first-layer matrix is retained exactly.

Since

\[
 \rho_\nu\le Y+B_0|w|_n\le Y+2B_0^2\tau,
\]

a convenient common finite-physical-time bound is

\[
 S_T=YT\exp(2B_0^2T),\qquad \tau(t)\le S_T\quad(0\le t\le T).
\]

This bound also proves that the finite-dimensional flows do not escape in finite time. For the exact gradient flow, loss dissipation gives the sharper \(\tau(t)\le Yt\), but that sharper estimate need not hold for the panel approximation.

There are also width-uniform bounds on forward-feature speed in the residual clock. Define

\[
 H_1(s)=2B_1R^2D_1(s),\qquad
 H_l(s)=B_1\{2B_0^2D_l(s)+K_l(s)H_{l-1}(s)\}.
\]

The chain rule and the preceding velocity estimates give

\[
 |\partial_t h_l(t,x)|_n\le\rho_\nu(t)H_l(S_T).
\]

Consequently, on a clock interval of length \(\Delta\), every feature moves at most (H_l(S_T)\Delta) in normalized Euclidean norm. This controls production of the history error without needing a uniform backward-response maximum.

All constants above are independent of (m,n,d) if (R,Y,L,B_j) and the hidden initialization operator norms are uniformly bounded. The exact Gaussian realization is still present; an operator-norm event is a bound on it, not a replacement of it. No Gaussian variance convention was supplied, so this note does not silently assume a particular probability estimate for that event.

## 3. An explicit autonomous two-order construction

Choose input atoms (X_1,\ldots,X_p) and positive weights \(\alpha_a\) summing to one, and put

\[
 \nu_p=\sum_{a=1}^p\alpha_a\delta_{X_a}.
\]

The simplest provenance is (X_a\stackrel{\mathrm{iid}}\sim\mu), \(\alpha_a=1/p\), sampled before training, independently of the frozen initialization. Evaluate (f_*(X_a)) once. For a finite dataset, sampling means sampling dataset indices with their original probabilities. The exact population path is never used by the algorithm.

For the exact \(\nu_p\)-flow, the hidden learned matrix has the identity

\[
 A_l(t)=-\frac2n\sum_{a=1}^p\alpha_a
  \int_0^t r_a(u)\delta_{l,a}(u)h_{l-1,a}(u)^T\,du.
\]

This is the causal skeleton before truncation. The first layer has fixed right factors (z_a), so it can either be kept as a learned (n\)-by-(d) matrix, or represented exactly by (p) learned left vectors and the fixed (z_a).

For each (l\ge2\), partition the residual-clock interval ([0,S_T]) into (q) panels of size \(\Delta=S_T/q\). At the first hitting time (t_j) of (\tau=j\Delta), store

\[
 V_{l,a,j}=h_{l-1}(t_j,X_a),\qquad U_{l,a,j}(t_j)=0.
\]

While panel (j) is active, evolve

\[
 \dot U_{l,a,j}=-2\alpha_ar_a\delta_{l,a},
\]

and keep all previous (U,V) pairs fixed. Use the represented matrix

\[
 W_l=W_l^0+\frac1n\sum_{a=1}^p\sum_{j\ \mathrm{opened}}U_{l,a,j}V_{l,a,j}^T
\]

in **both** forward propagation and transposed backward propagation. Evolve (w\) and (A_1\) by their exact \(\nu_p\)-gradient formulas evaluated on the represented current network. Compute \(\rho_{\nu_p}\) from the same (p) current residuals.

The panel index, clock, stored factors, (A_1), and (w) determine all future evolution. Thus this is an autonomous hybrid system, restartable from any intermediate state. Its switches depend on its own clock, and its coefficients are determined by the input law access, sampled labels, initialization, horizon, and (q). There are no recorded exact-network trajectories, precomputed future responses, or dense reference drivers.

The learned storage is

\[
 O((L-1)npq+nd+n),
\]

plus (O(Lnp)) transient forward/backward values and (O(1)) clocks and indices. The immutable landmarks take (O(pd)) storage and the exact frozen matrices take their original (O(Ln^2+nd)) storage. The claimed compression concerns **learned state**, not total frozen storage or matrix-multiply work. If the requirement instead counts all data-atom storage inside (O(Lnpq+nd)), an extra condition such as (p\le n\), a succinct input oracle, or a separate (pd\) term is necessary. This accounting must not be hidden.

The (V)'s are feature vectors evaluated on data landmarks at causally selected times. They are not a prescribed frozen-neuron dictionary: each newly opened panel uses the current trained features, all layers continue to evolve, and the full frozen Gaussian operator acts on every forward and backward evaluation.

## 4. The exact history defect

Let \(\theta^{p,q}\) denote the represented network. Away from switching times,

\[
 \dot\theta^{p,q}=F_{\nu_p}(\theta^{p,q})+E_q(t),
\]

where only hidden-weight components (l\ge2) are nonzero, and

\[
 (E_q)_l=-\frac2n\sum_a\alpha_a r_a\delta_{l,a}
       (V_{l,a,j}-h_{l-1,a})^T.
\]

At a switch the represented matrix is continuous, because the new left vectors start at zero. Put

\[
 C_H(S)=\left[\sum_{l=2}^L(D_l(S)H_{l-1}(S))^2\right]^{1/2}.
\]

By the feature-speed estimate and \(\sum\alpha_a|r_a|\le\rho_{\nu_p}\),

\[
 \|E_q(t)\|_{\mathcal H_n}\le2\rho_{\nu_p}(t)C_H(S_T)\Delta,
\]

hence

\[
 \int_0^T\|E_q(t)\|_{\mathcal H_n}\,dt
 \le\frac{2C_H(S_T)S_T^2}{q}.
\]

This is a proved (q^{-1}\) production bound for the concrete causal witness. It is not yet a propagated trajectory estimate. Higher order causal history rules may improve the (q\)-rate, but need additional regularity and their own error proof; they are unnecessary for existence of a finite-history witness on a fixed horizon.

## 5. Population error: concentration on one reference path

Condition on the entire frozen initialization. Let \(\theta^\mu(t)\) be the exact population gradient flow, independent of the landmark draw. Define a Hilbert-valued function of one input by

\[
 Z(X)(t)=G_X(\theta^\mu(t)),\qquad
 Z\in L^2([0,T];\mathcal H_n).
\]

This function is used only in the proof. It is neither computed nor supplied to the approximation. Set

\[
 U_T=Y+B_0M(S_T),\qquad
 C_G^2=B_0^2+R^2D_1(S_T)^2+B_0^2\sum_{l=2}^LD_l(S_T)^2,
\]

and (G_T=2U_TC_G\). Then \(\|G_x(\theta^\mu(t))\|_{\mathcal H_n}\le G_T\).

For iid landmarks, define the reference forcing error

\[
 e_p(t)=F_{\nu_p}(\theta^\mu(t))-F_\mu(\theta^\mu(t)).
\]

Expanding the squared Hilbert norm of a sum of independent centered variables makes every off-diagonal expectation zero. Therefore

\[
 \mathbb E_X\|e_p\|_{L^2_t\mathcal H_n}^2
 =\frac1p\int_0^T\mathbb E_X
  \|G_X(\theta^\mu(t))-\mathbb E G_X(\theta^\mu(t))\|_{\mathcal H_n}^2dt
 \le\frac{TG_T^2}{p}.
\]

Markov's inequality and Cauchy-Schwarz give, with probability at least (1-\delta\),

\[
 \int_0^T\|e_p(t)\|_{\mathcal H_n}\,dt
 \le\frac{TG_T}{\sqrt{p\delta}}.
\]

This proof has no covering number, input basis cutoff, or dependence on the dataset size. It controls the full parameter-gradient source in the correct normalized Hilbert space. The exact flow can depend arbitrarily on the fixed initialization and on \(\mu\); conditioning makes this harmless. The iid samples need only be independent of that exact reference, not of their own subsequently trained approximation.

The adaptivity of training is dealt with by stability in Section 6, **not** by pretending that the trained parameters remain independent of the samples. Replacing \(\theta^\mu\) by the sample-trained path inside the centering step would be invalid.

For a deterministic positive cubature, the same theorem below holds with the measured/established source quantity \(\int\|e_p\|dt\); however, no (p\)-rate follows for arbitrary laws from positivity alone. Selecting or moving atoms during training requires a separate adaptive quadrature theorem. An iid proof cannot be reused unchanged after such selection. Predictable importance sampling could support a martingale version if unbiasedness and bounded weights are proved, but that is a different construction and is not claimed here.

## 6. Conditional compact-horizon theorem and observable norm

Let \(\theta^p\) be the exact \(\nu_p\)-gradient flow with the same frozen initialization. Assume that the empirical vector field obeys the one-sided stability inequality

\[
 \langle\theta-\eta,F_{\nu_p}(\theta)-F_{\nu_p}(\eta)\rangle_{\mathcal H_n}
 \le\Lambda_T\|\theta-\eta\|_{\mathcal H_n}^2
\]

for the pairs needed to compare \(\theta^p\) with \(\theta^\mu\), and \(\theta^{p,q}\) with \(\theta^p\), throughout \([0,T]\). A sufficient condition is

\[
 \nabla^2\mathcal R_{\nu_p}\succeq-\Lambda_T I
\]

on all intervening line segments. The decisive requirement is that \(\Lambda_T\) be independent of (p,m,n,d,q\) under the stated input and initialization bounds. This is an explicit additional assumption for the deep theorem, not a consequence already established above.

For two paths with forcing difference (b(t)\), differentiating squared distance and applying the inequality yields

\[
 \frac d{dt}\|\theta-\eta\|\le\Lambda_T\|\theta-\eta\|+\|b(t)\|.
\]

The zero-distance case follows by replacing the norm with \(\sqrt{\|\theta-\eta\|^2+\varepsilon^2}\) and passing to zero. Integrating and using the previous two sections yields

\[
 \sup_{t\le T}\|\theta^{p,q}(t)-\theta^\mu(t)\|_{\mathcal H_n}
 \le e^{\max(\Lambda_T,0)T}
 \left[\frac{TG_T}{\sqrt{p\delta}}
       +\frac{2C_H(S_T)S_T^2}{q}\right]
\]

with probability at least (1-\delta\). If the stability property itself holds only on an event of probability (1-\eta\), the joint statement has probability at least (1-\delta-\eta\). No independence of these events is required.

To connect this state estimate to the named prediction, define

\[
 V_1=B_1R,\qquad V_l=B_1(B_0+K_l(S_T)V_{l-1}),\qquad
 J_T=B_0+M(S_T)V_L.
\]

Along an interpolating parameter segment, direct forward differentiation gives \(|Dh_l[\xi]|_n\le V_l\|\xi\|_{\mathcal H_n}\), and hence

\[
 \sup_{\|x/\sqrt d\|\le R}|f_\theta(x)-f_\eta(x)|
 \le J_T\|\theta-\eta\|_{\mathcal H_n}.
\]

Thus the theorem controls uniform prediction error on the input ball, not only training loss. It also controls population-risk difference by (2U_TJ_T\|\theta-\eta\|\) when the compared predictions obey the stated uniform residual bound.

The correct quantifiers are: for fixed (T,L,R,Y,B_j\), a common hidden-initialization operator bound, and a **verified common stability bound**, choose (p,q\) from the displayed estimate; then the same randomized construction works for each finite or infinite input law, with constants independent of (m,n,d\). This is not a single landmark set working simultaneously for every possible law.

## 7. Why the deep stability assumption is substantive

Loss dissipation controls the parameter path in \(\mathcal H_n\), and the clock estimates control \(|\delta_l|_n\). Neither estimate controls individual backward coordinates.

Let

\[
 b_L=w,\qquad b_l=W_{l+1}^T\delta_{l+1}\quad(l<L),\qquad
 \delta_l=\phi'(a_l)\odot b_l.
\]

The second derivative of the output contains the exact terms

\[
 \frac1n\sum_i b_{l,i}\phi''(a_{l,i})(Da_{l,i}[\xi])^2.
\]

In the normalized parameter metric a unit perturbation can concentrate an (O(\sqrt n)\) preactivation perturbation on a single neuron. Bounding these terms on a full Hilbert-space tube therefore invokes \(\|b_l\|_\infty\), not just \(|b_l|_n\). The negative part of the squared-loss Hessian includes (2rD^2f\), so its sign cannot be discarded as a positive Gauss-Newton term.

The gap is real at the level of the proposed assumptions: a matrix with first column (\mathbf1/\sqrt n\) and all other columns zero has operator norm one, but maps (\mathbf1\) under its transpose to \(\sqrt n e_1\). Hence bounded hidden operator norm plus bounded top response does not imply a width-uniform backward maximum. This example diagnoses the insufficiency of the norm implication; it is **not** a counterexample drawn from the prescribed Gaussian dynamics. Gaussianity may provide a sharper reachable-direction or probabilistic argument, but such an argument has not been supplied here. Simply conditioning on a Gaussian operator-norm event does not prove the missing implication.

For comparison, when (L=1\), there is no propagated lower response. For a perturbation \(\xi=(U,v)\),

\[
 D^2f[\xi,\xi]
 =2\langle v,\phi'(a_1)Uz\rangle_n
  +\langle w,\phi''(a_1)(Uz)^2\rangle_n,
\]

so

\[
 |D^2f[\xi,\xi]|
 \le\{B_1R+B_2R^2\|w\|_\infty\}\|\xi\|_{\mathcal H_n}^2.
\]

The clock estimate bounds \(\|w\|_\infty\le M(S_T)\) on all intervening segments. Thus one may take

\[
 \Lambda_T=2U_T\{B_1R+B_2R^2M(S_T)\}
\]

for every positive probability measure. This closes the population argument in the shallow case. There are no learned hidden (n\)-by-(n\) matrices there, so the (q\) defect is zero. Treating this special case as a proof for deep networks would change the target.

For deeper networks, a sufficient extra condition is a uniform bound on every \(\|b_l\|_\infty\) along the comparison tubes. The other second-variation terms, (2\langle v,Dh_L\rangle_n\) and (2\langle\delta_l,U_lDh_{l-1}\rangle_n\), are bounded by the already controlled normalized norms and operator norms. The new backward maximum is precisely the additional input that closes this direct Hessian proof. A weaker estimate restricted to the actual error directions may be enough, and is the more promising place to exploit the frozen Gaussian structure without paying a maximum over neurons.

## 8. Compact horizon, all time, and the decisive next obligation

The proved production estimates and conditional theorem are for any fixed finite physical horizon. Both the clock budget and the propagation factor can grow with (T\). Smooth deterministic labels, bounded inputs, and zero output initialization do not imply either finite total residual clock or contraction. In particular, a positive limiting approximation error makes the residual clock diverge even if parameter velocities tend to zero.

An all-time result would need additional ingredients: a uniformly bounded source-to-trajectory propagator, a time-integrable population sampling source in a suitable weighted norm, and a history construction whose error remains summable on the actual infinite trajectory. Finite total residual clock for both compared systems would help the latter two requirements, but is not assumed or proved. The finite-(q\) panel witness cannot silently be run past its prescribed clock budget.

The leading next obligation is therefore:

> Prove a width-uniform compact-horizon stability estimate for the actual deep frozen-Gaussian flow and its quadrature/history perturbations, preferably in a reachable response norm that avoids a worst-neuron backward maximum, while retaining a norm strong enough for the displayed Hilbert sampling source and uniform prediction comparison.

Until that bridge is proved, the full deep population theorem is conditional. What is established here is the exact causal skeleton, a concrete admissible autonomous (O(Lnpq+nd)\) learned-state witness, dimension-independent (p^{-1/2}\) source concentration, dimension-independent (q^{-1}\) history-error production, a complete conditional propagation theorem, and an unconditional shallow population result. No dimension-exponential input basis is used, but no unconditional deep dimension-free closure theorem has been obtained.
