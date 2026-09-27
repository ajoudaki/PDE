# Bounded independent audit: full rank, closure, and polynomial complexity

This is a prompt-scoped theoretical audit, not a review of the study's other artifacts. No other study or source files were read and no training was run. The research-contract and adversarial-audit instructions of `investigate-conjectures`, and `solve-math-rigorously`, were applied. Results below are elementary derivations; no external theorem is invoked.

## Assessment

There is no valid general impossibility argument from full rank, nonlinear training, or infinite response memory alone. A small ordinary Gaussian network is already a finite autonomous scalar ODE and, conditional on a quantitative population-limit theorem, provides a polynomial-size approximation at fixed horizon. A structured full-rank initialization at arbitrarily large widths is a stronger requirement. Rank and fast matrix multiplication do not establish its fidelity or its finite closure. Broad polynomial tractability remains an actual theorem obligation, not a consequence of finite approximation existence.

I regard a randomized polynomial approximation on fixed bounded horizons and fixed bounded training tasks as plausible, conditional on a stable quantitative population limit. I do not regard polynomial complexity uniformly over unrestricted tasks, horizons, all Gaussian realizations, or the original finite-response-order implementation as established.

## Canonical equations supplied for this audit

For width n, m training samples, and tanh activation,

\[
h_1=\tanh(wx/\sqrt d),\quad h_2=\tanh(Wh_1),\quad f=n^{-1}c^T h_2,
\]

\[
\delta_2=c\odot(1-h_2^2),\qquad
\delta_1=(1-h_1^2)\odot(W^T\delta_2),
\]

\[
\dot w=-\frac2m\sum_\alpha r_\alpha\delta_{1,\alpha}(x_\alpha/\sqrt d)^T,
\quad \dot c=-\frac2m\sum_\alpha r_\alpha h_{2,\alpha},
\quad \dot W=-\frac2{mn}\sum_\alpha r_\alpha\delta_{2,\alpha}h_{1,\alpha}^T.
\]

Initialization is iid Gaussian with variances 1, 1/n, and 1/n² respectively for w, W, and c. In the population limit the initial output/readout vanish, while subsequent training need not be lazy.

## 1. An exact full-rank quotient exposes the rank loophole

Let n=qk and R=1_q tensor I_k, so R^T R=qI_k. Choose an invertible k by k matrix G, and initialize

\[
w(0)=Ru(0),\qquad c(0)=Ra(0),\qquad W(0)=I_q\otimes G.
\]

The unrestricted canonical gradient flow preserves the form

\[
w=Ru,\quad c=Ra,\quad
W=I_q\otimes G+\frac1qR(B-G)R^T,
\qquad B(0)=G.
\]

Indeed WR=RB and W^T R=RB^T. Elementwise tanh commutes with replication, so hidden features and both deltas are replicated. The output equals k^{-1}a^T tanh(B tanh(ux/sqrt d)). Finally,

\[
\dot W=\frac1qR\left[-\frac2{mk}
\sum_\alpha r_\alpha\bar\delta_{2,\alpha}\bar h_{1,\alpha}^T\right]R^T.
\]

Thus (u,a,B) obey exactly the canonical width-k equations, including the specified learning-rate normalization. All learned dense off-block entries are permitted; this is an invariant family of the unrestricted training flow. State dimension is k²+kd+k, independent of q. Taking G Gaussian with variance 1/k makes W(0) full rank n almost surely. Its nonzero singular values are those of G repeated q times.

This is not a nondegenerate solution to every intended interpretation. It changes the joint initialization of w and c by cloning them. If only W may be changed while w and c must remain iid Gaussian, the construction is inadmissible. It also leaves an invariant unobserved complement: features lie in range(R), and learning does not activate its orthogonal complement. It therefore shows precisely why full rank alone cannot certify that all n modes participate. For k to infinity, its observable identification and rate reduce to the ordinary Gaussian finite-width problem. Correct finite-n readout variance is not preserved by cloning width-k Gaussian readouts, although both initial readouts vanish in their respective large-width limits.

## 2. Full rank and second moments already fail to identify the initial velocity

Consider one sample, d=1, input x=s, target y=1, and the limiting initial c=0. At t=0, only the readout contribution affects the output velocity:

\[
\dot f(0)=2\mathbb E[h_2(0)^2].
\]

For Gaussian W, write Q_s=E[tanh²(sZ)] with Z standard Gaussian. The canonical initial velocity is

\[
2\mathbb E[\tanh^2(\sqrt{Q_s}Z)].
\]

For the full-rank and computationally trivial initialization W=I, it is

\[
2\mathbb E[\tanh^2(\tanh(sZ))].
\]

As s tends to infinity these approach 2E[tanh² Z] and 2tanh²(1), respectively, with a strict gap. For completeness, g(v)=tanh²(sqrt v) is strictly concave on v≥0. Put u=sqrt v and t=tanh u. Its derivative is t(1-t²)/u. The sign of its derivative with respect to u is the sign of u(1-3t²)-t, which is negative because

\[
\frac{d}{dt}\{t-(1-3t^2)\operatorname{atanh}t\}
=\frac{2t^2}{1-t^2}+6t\operatorname{atanh}t>0
\]

and the bracket vanishes at zero. Strict Jensen therefore gives E[g(Z²)]<g(E[Z²])=tanh²(1). Dominated convergence transfers the nonzero gap to some sufficiently large finite s. Both preactivations have second moment Q_s, but their nonlinear readout kernels differ.

This defeats the diagonal witness and any claim that matching rank and covariance suffices. It does not defeat a growing Gaussian-block hierarchy.

## 3. A conditional polynomial-size baseline, and its exact missing assumption

Let F_k be the training/query output path of the ordinary width-k Gaussian network. Suppose the canonical limit F_infinity is deterministic and, uniformly on an explicitly bounded task class, a proved estimate has the form

\[
\Pr\left\{\sup_{0\le t\le T}\|F_k(t)-F_\infty(t)\|
>C_T k^{-a}\log^b(1/\delta)\right\}\le\delta,
\qquad a>0.
\]

Then choosing k at least (C_T log^b(1/delta)/epsilon)^{1/a} gives an autonomous scalar ODE of dimension k²+kd+k, polynomial in epsilon^{-1} for fixed T and fixed structural parameters. Gaussian G is full rank almost surely and the entire k by k learned matrix is trained. This is an honest conditional existence proof, but it merely replaces the original width by an accuracy-controlled width. It is not a proof of the displayed rate or of a particular response-memory closure.

If the canonical limit is random, independent resampling does not imply pathwise approximation to the same realization. A coupling to its limiting randomness, or a distributional rather than pathwise metric, must be specified.

Dimension and RHS evaluation count also do not alone establish polynomial computational cost. Coefficient generation, bit precision, numerical integration/conditioning, output-query cost, and any preprocessing must be bounded. A stability estimate of the form e^{LT} times a source error is polynomial in epsilon^{-1} at fixed T when L is controlled; it is not polynomial in T. Polynomial dependence jointly on T is a separate claim.

## 4. Independent blocks and representative particles need two identification bridges

A block diagonal matrix with independent k by k Gaussian blocks is full rank almost surely. Keeping all dense weights trainable is essential: the outer-product gradient instantly creates cross-block entries. Freezing off-block entries changes the model. Likewise, repeatedly resampling Gaussian actions during training changes quenched initialization into annealed noise unless its equivalence is proved.

With iid outer-layer initialization retained, letting the number of independent blocks tend to infinity at fixed k generally gives a population of block states, not automatically a finite scalar ODE. Finite representatives must approximate that population. The required bridges are:

1. A representative approximation with an explicit error rate and stability constants controlled as k grows, including the learned dense interactions and initialization reuse.
2. Identification of the large-k block-population flow with the canonical dense-Gaussian flow, in the required path metric.

A finite collection of independent trained networks is not automatically the first bridge: those networks have separate residuals, whereas the original dense model has a shared residual and cross-block learned interactions. Neither Gaussian marginal matching nor a central-limit argument at t=0 closes the second bridge during training.

## 5. The joint complexity bound is the decisive efficiency obligation

Keep initialization rank/structure parameter k, response order P, representative count, coefficient precision, and numerical accuracy separate. A bound must ultimately select all of them as functions of the same epsilon, task bounds, and T, and then bound total cost.

For example, even granting initialization error O(k^{-a}) and memory error O(rho^P), 0<rho<1, a state count k^P yields

\[
k\asymp\epsilon^{-1/a},\quad P\asymp\log(1/\epsilon)
\quad\Longrightarrow\quad
k^P=\exp\{\Theta((\log(1/\epsilon))^2)\},
\]

which is not polynomial in epsilon^{-1}. Similarly, m^P is not jointly polynomial in m and epsilon^{-1}. Polynomial cost at every fixed response order plus convergent response order is insufficient.

An honest theorem should bound the initialization-identification source error and the response-truncation source error before applying a stability estimate. A stability theorem alone supplies no small omitted term. A polynomial hierarchy needs one total cost bound after these errors are balanced, with no trajectory-derived coefficients, hidden time histories, or arbitrarily precise real-number encoding.

## 6. Quantifier and final-fit limitations

A deterministic surrogate that receives only the Gaussian law cannot approximate every finite-width Gaussian realization uniformly: Gaussian support includes open sets with separated initial outputs. The relevant positive claim should concern the population object or a high-probability approximation under a stated coupling. This elementary obstruction does not rule out population approximation.

Uniform finite-time output accuracy also does not by itself transfer fitting times. Even losses differing uniformly by epsilon can sit on opposite sides of the target threshold forever. If loss error is eta and the canonical loss crosses the threshold with derivative bounded above by a negative constant -gamma throughout a crossing neighborhood, then monotonicity and the mean-value estimate give hitting-time error at most eta/gamma, provided the horizon covers that neighborhood. Some comparable crossing/stability assumption is necessary for final-fit claims.

## Highest-leverage theorem target

For a precisely specified structured initialization family that leaves the allowed outer-layer initialization intact, prove a joint, finite-time error bound for representative count, block size k, and response order P, with constants uniform in the discarded width n. Then substitute actual parameter choices into the actual scalar-state/RHS/precision cost. A successful bound would answer the efficiency question. A failure of a particular closure, or a rank argument alone, would not answer the broader existence question.

## Addendum: an actual O(1/k) Gaussian-block initialization bound

This addendum verifies a positive statement for the same one-sample canonical normalization, with target y and limiting initial c=0. It concerns only the initial output velocity. Take independent k by k Gaussian diagonal blocks, each with entry variance 1/k, and retain iid Gaussian first-layer weights. Each finite block matrix, and therefore the full block diagonal matrix, is full rank almost surely. Write

\[
h_j=\tanh(sZ_j),\quad Q_k=\frac1k\sum_{j=1}^k h_j^2,
\quad Q=\mathbb E h_1^2,\quad
\psi(q)=\mathbb E F(\sqrt q Z),\quad F(z)=\tanh^2 z,
\]

where the Z_j and the additional Z are independent standard Gaussians. Conditional on the block's first-layer features, each second-layer preactivation has law N(0,Q_k). At c=0 one has f=0, wdot=Wdot=0, and cdot=2y h_2. Thus the infinite independent-block population and the dense Gaussian population have respective initial output velocities

\[
v_k=2y\mathbb E\psi(Q_k),\qquad v_\infty=2y\psi(Q).
\]

All derivatives of F are bounded. For q>0, differentiation under the Gaussian integral followed by integration by parts gives

\[
\psi'(q)=\tfrac12\mathbb E F''(\sqrt q Z),\qquad
\psi''(q)=\tfrac14\mathbb E F''''(\sqrt q Z).
\]

These formulas extend continuously to q=0: integrate the first identity from a positive lower endpoint and take that endpoint to zero by bounded convergence, then do the same for the derivative. Hence psi is C² on [0,1], including the endpoint, and sup|psi''|≤M/4 where M=sup over real z of |F''''(z)|.

Centered Taylor expansion about Q, together with E(Q_k-Q)=0 and Var(Q_k)=Var(h_1²)/k, yields

\[
\left|\mathbb E\psi(Q_k)-\psi(Q)\right|
\le\frac{M}{8k}\operatorname{Var}(h_1^2),
\]

and therefore

\[
|v_k-v_\infty|
\le\frac{|y|M}{4k}\operatorname{Var}(h_1^2)
\le\frac{|y|M}{16k}.
\]

The last step uses 0≤h_1²≤1, which implies Var(h_1²)≤1/4. The constants in the proposed bound are therefore correct. In fact M=16: with u=tanh²z in [0,1],

\[
F''''(z)=-8(1-u)(2-15u+15u^2).
\]

The quadratic lies in [-7/4,2], so |F''''|≤16, with equality at z=0. Consequently

\[
|v_k-v_\infty|
\le\frac{4|y|}{k}\operatorname{Var}(h_1^2)
\le\frac{|y|}{k},
\]

uniformly in the input scale s. This is a genuine nontrivial initialization agreement rate for full-rank Gaussian blocks with independent first-layer weights. It supplies no bound for trained trajectories at t>0, finite representative error, response-memory truncation, or joint computational complexity.
