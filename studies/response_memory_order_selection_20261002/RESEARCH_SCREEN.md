# Can data order determine which features survive fitting?

The consequential target is **a prospective prediction of shortcut retention after identical training examples have been fitted**. Consider ordinary minibatch SGD on the paper's deep nonlinear network: can changing the correlation time or order of two training environments select a different invariant feature, with a persistent difference in shifted-distribution risk? The hoped-for contribution is a quantitative selection boundary or an effective ordering intervention predicted from a small response-memory state. Merely showing order effects, beneficial noise, or a nonzero commutator would have little novelty.

This is a credible but high-risk application. The exact sampled-history representation below is available now; a useful selection prediction and compact stochastic closure remain open. I would pursue one discriminator before any stochastic all-time theorem.

## Existing explanations set a high bar

[Sclocchi, Geiger and Wyart](https://proceedings.mlr.press/v202/sclocchi23a.html) already connect SGD noise, feature-learning regimes, late fitting and performance. [Beneventano](https://arxiv.org/abs/2312.16143) studies without-replacement trajectories through a covariance-related regularizer. [Kühn and Rosenow](https://arxiv.org/abs/2306.05300) calculate epoch noise anticorrelations and their effects on stationary weight fluctuations. These make white-noise versus correlated-order comparisons insufficient by themselves.

Recent work makes the feature claim crowded too. [LaBonte and Muthukumar](https://arxiv.org/abs/2606.30444) prove shortcut priority and suppression of a nonlinear signal for two-layer ReLU networks with logistic loss. [Cornacchia, Mikulincer and Mossel](https://arxiv.org/abs/2605.10237) show benefits of temporal correlations for sparse learning, but their positive result uses stylized SGD with a temporal-difference loss; that is a material distinction from the present ordinary pointwise squared loss. [The Order Is The Message](https://arxiv.org/abs/2603.25047) reports ordering-selected Fourier representations. Its abstract's stronger sample-complexity claims have not been audited here and should not be accepted as established. None of these references licenses claiming that order-to-representation effects themselves are new.

## Exact skeleton, retaining raw SGD

Use the paper's forward pass
\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\quad f_a=w^\top h_a^{(L)}/n,
\]
with residuals \(r_a=f_a-y_a\), loss \(m^{-1}\sum_a r_a^2\), and residual-free responses \(\delta_a^{(L)}=w\odot\phi'(z_a^{(L)})\), \(\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot W^{(\ell+1)\top}\delta_a^{(\ell+1)}\). Preserve Gaussian initialization, zero readout and mobilities \((n,1,\ldots,1,n)\).

At step \(k\), let \(c_{a,k}\) count sample \(a\)'s occurrences in a batch of size \(B\), and set \(u_{a,k}=mc_{a,k}/B\). With actual SGD step \(\eta\), every hidden link satisfies exactly
\[
W_K^{(\ell)}-W_0^{(\ell)}
=-\frac{2\eta}{nm}\sum_{k<K,a}u_{a,k}r_{a,k}
\delta_{a,k}^{(\ell)}h_{a,k}^{(\ell-1)\top}.
\tag{1}
\]
The first-layer and readout increments are respectively
\(-2\eta m^{-1}\sum_a u_ar_a\delta_a^{(1)}x_a^\top/\sqrt d\) and
\(-2\eta m^{-1}\sum_a u_ar_ah_a^{(L)}\).

Define the **global full-data residual clock** by
\(\rho_k^2=m^{-1}\sum_a r_{a,k}^2\), \(\tau_0=1\),
\(\tau_{k+1}=\tau_k+\eta\rho_k\).
On each interval \([\tau_k,\tau_{k+1})\), insert constant histories
\[
h_a(\xi)=h_{a,k},\qquad
b_a(\xi)=u_{a,k}r_{a,k}\delta_{a,k}/\rho_k.
\]
Layer superscripts are suppressed only here. The unit prefix has initial forward features and zero backward history. A zero full residual makes every SGD update zero; define no new interval and perform no division. Then (1) is exactly \(-2(nm)^{-1}\sum_a\int b_ah_a^\top d\xi\). This is a representation of discrete SGD, not its continuous-flow approximation.

Let \(p_j\) be the shifted Legendre polynomials with \(\int_0^1p_ip_j=\mathbf1_{i=j}/(2j+1)\). Store
\(\bar h_{a,j}=\int_0^{\tau_K}h_ap_j(\xi/\tau_K)d\xi\) and
\(\bar\delta_{a,j}=\int_0^{\tau_K}b_ap_j(\xi/\tau_K)d\xi\), for \(j<q\).
These moments update exactly from their previous values: re-expand
\(p_j((\tau_k/\tau_{k+1})x)\) in modes \(p_0,\ldots,p_j\), then add the integral of the constant new history over the appended interval. Thus no past samples need be replayed.

Reconstruction is the paper's paired sum
\[
\widehat W^{(\ell)}_K=W_0^{(\ell)}-
\frac{2}{nm\tau_K}\sum_{a,j<q}(2j+1)
\bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\]
For the **same inserted histories**, its difference from their exact accumulated update is
\[
\widehat W_K-W_{\rm acc,K}
=\frac2{nm}\sum_a\int
[(I-\Pi_q)b_a][(I-\Pi_q)h_a]^\top d\xi.
\tag{2}
\]
Mixed terms vanish by orthogonality. Evaluating future histories in the reconstructed network creates the actual compressed algorithm; (2) alone does not control its feedback error relative to dense SGD.

The prospective causal quantity is the sensitivity of shifted test risk \(R(\theta_K)\) to an exposure-preserving perturbation of batch weights. Define \(F_a=-\mathcal D\nabla_\theta r_a^2/m\), with the stated mobility matrix \(\mathcal D\). For a differentiable schedule \(u(\varepsilon)\), its parameter sensitivity \(v_k=\partial_\varepsilon\theta_k\) obeys exactly
\[
v_{k+1}=\left[I+\eta\sum_a u_{a,k}DF_a(\theta_k)\right]v_k
+\eta\sum_a(\partial_\varepsilon u_{a,k})F_a(\theta_k),\qquad v_0=0,
\]
and \(\partial_\varepsilon R=DR(\theta_K)v_K\). This is ordinary tangent dynamics, not a new theorem. The research opportunity is predicting its nonlinear, finite-intervention continuation using bounded paired histories, including evolving forward features and backward credit. A local bracket or initial gradient alignment cannot supply that continuation by itself.

## Stochastic closure audit

Every sample's forward history must be inserted at every global step, including samples absent from the batch. Their current features change through other samples' updates. Updating only sampled forward memories silently changes the construction. Full-data \(\rho\) and these forward evaluations also remove the usual minibatch arithmetic advantage; efficiency is not the proposed benefit.

Sampling belongs in \(u_ar_a\delta_a\), with the original physical step retained. Replacing it by mean residual weighting erases the effect under investigation. A sampler's phase, remaining permutation, or Markov state must accompany the memory if restartability of the stochastic process is claimed.

Finite-step histories are discontinuous. Their projection identity survives, but the paper's smooth-history rates and all-time fitting bounds do not automatically survive. In a Brownian diffusion approximation, forward paths generally have infinite variation and white-noise forcing is not an ordinary \(L^2\) backward history. The joint derivative clock is then undefined as written; stochastic integrals, Itô corrections, and a new error argument would be necessary. Start with raw SGD.

## One bounded discriminator

Use two tanh hidden layers, width 256, 2,560 fixed examples, batch size 32, step \(\eta=0.01\), and 16 input coordinates. Generate three standard Gaussian signal coordinates \(z\) with pairwise correlation 0.2, label \(y=\tanh(z_1z_2z_3)\), and an easy shortcut coordinate \(s=ey+0.1\epsilon\), with independent standard Gaussian \(\epsilon\). Environment \(e=+1\) supplies 90% of examples and \(e=-1\) 10%; remaining coordinates are nuisance Gaussians. The odd target respects the bias-free tanh architecture. On the test distribution, redraw \(s\) independently of \(y\). This supplies nonlinear signal/linear shortcut competition without changing the paper's optimizer or architecture.

Run one common SGD prefix, capped at 100 epochs. Define \(V_y=\mathbb E y^2\), shifted risk \(R=\mathbb E(f-y)^2\), and shortcut dependence \(S=\mathbb E[f(z,s)-f(z,s')]^2\), with independent shortcut redraw \(s'\) and unchanged nuisance coordinates. Branch at the first epoch with \(S/V_y\ge0.1\) and \(0.25<R/V_y<0.9\). If this competition gate never opens, stop as inconclusive; do not search a parameter grid.

From that common state, precompute predictions for exactly two one-epoch schedules: all majority minibatches then all minority minibatches, and their reverse. Counts, minibatches and step size are identical. Follow both by the same 50-epoch mixed continuation. Record predictions **before** running the two dense branches. Compare orders \(q=4,8\), a kernel frozen at the switching state, the full first-order discrete dynamics about a common reference continuation, and a Gaussian-noise surrogate matching the reference batch mean and lag covariance, including epoch anticorrelations. No coefficients may use either prospective dense branch. For this screening, initialize memory at the common switching network with a fresh unit prefix and retain that network as its fixed source. This legitimate restart sacrifices from-initialization compression and must be reported. At this sample count the memory can exceed dense moving storage; the test addresses explanation.

Primary outcome: signed difference in shifted test risk after common continuation, with a secondary comparison at each branch's first training-MSE \(10^{-3}\) crossing within that continuation cap. Precommit success as an effect at least \(0.05V_y\), correct sign in four of five paired seeds, risk-difference error below 25%, agreement between orders within 10% of the observed effect, and at least twice the predictive accuracy of the strongest control. Replicate only this fixed contrast. If the fitting threshold is not reached, the fitted-selection claim remains untested. If controls already predict the contrast, memory has provided trajectory reproduction but no new selection explanation. If the effect disappears after common continuation, it is chiefly an optimization transient. No contrast can establish a phase boundary; that would be subsequent work.

Ceiling: potentially a strong mechanistic result if compressed histories predict a useful, persistent representation-selection intervention beyond colored-noise and tangent models. Present status: exact representation plus a falsifiable design, with no demonstrated new mechanism and substantial risk that ordinary competitors explain the effect.
