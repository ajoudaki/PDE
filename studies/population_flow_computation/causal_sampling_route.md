# Causal sampling route: a lazy, reused Gaussian operator

Frozen first-round report, 2026-09-12. Scientific input was the supervisor's self-contained assignment only. Required rigorous-math and conjecture-process instructions were read; no book, code, other study, other route, or scientific simulation was read or run. This is an internal research artifact, not established material.

**Outcome.** There is an explicit causal simulator with exact finite-representative Gaussian reuse, positive semidefinite covariance even at singular histories, and no stored dense trainable matrix. It uses correlations of its own fields to compute every response coefficient; no differentiation of feedback is needed. Its finite construction is proved below. A useful population error guarantee through time 40 is **open**. History cost and the missing quantitative sampling theorem prevent claiming milestone C from this construction alone.

## 1. Frozen contract and approximation axes

The target is the supplied bias-free, two-hidden-layer tanh population physical gradient flow, with input `x = sqrt(2) u`, `u in S^1`, bounded labels, initial first-layer Gaussian coordinates, initialized reused Gaussian action `A0`, and zero initial `K,c`. Predictions are `f_t(u)`. The primary desired comparison is

\[
\sup_{0\le t\le40}\|\widehat f_t-f_t\|_{L^2(\mu_u)}\le\varepsilon,
\qquad \varepsilon\in[0.02,0.1],
\]

in probability, with costs independent of the original network width. Finite support laws are handled exactly in the data variable. A broader law needs an executable sampler or a computable integration interface; the words “finite description” alone do not supply one. An atom approximation is a separate law-approximation axis, not free quadrature. No uncounted Gaussian quadrature is used.

Parameters are a representative count `P`, a data atom count `m`, and time steps `h_k` with `J` updates. The fixed approximation state contains real arrays with ordinary finite precision, query histories, and a reproducible random-generator state. It is restartable by retaining all these arrays. No history compression is claimed in this round.

The construction below is exactly a lazy simulation of a `P`-representative Gaussian operator and a factored learned correction. Thus `P` is a statistical approximation parameter, not the ambient network width. However, proving that a modest `P` approximates the population is substantive work. Relabeling a very large network as representatives is not by itself success.

## 2. Exact Gaussian conditioning, including singular histories

This section is a finite-dimensional identity, not a limiting theorem. Equip each copy of `R^P` with

\[
\langle a,b\rangle_P=P^{-1}a^Tb.
\]

Let `G` have independent `N(0,1/P)` entries. Its adjoint for these equal normalized inner products is `G^T`. Suppose previous queries have revealed

\[
GH=Y,\qquad G^TD=X,
\]

where `H,Y` have `l` columns and `D,X` have `r` columns. A query may depend measurably on all preceding revealed fields and on independent auxiliary randomness. This adaptivity is permitted: conditioning on the transcript fixes the queries already made, and each new observation adds a linear constraint on the still-Gaussian matrix.

Write

\[
C_H=H^TH/P,\quad C_D=D^TD/P,\quad
\Pi_H=HC_H^+H^T/P,\quad \Pi_D=DC_D^+D^T/P.
\]

The superscript `+` means the Moore–Penrose inverse on the nonzero eigenspace. These are orthogonal projectors, also when the history is rank deficient. Empty histories give zero projectors. Compatible observed constraints satisfy `D^T Y = X^T H` and annihilate every null linear combination of their query columns.

One conditional mean is

\[
M=YH^+ +D(D^TD)^+X^T(I-\Pi_H).
\]

Indeed `MH=Y`. Also

\[
M^TD=(H^+)^TY^TD+(I-\Pi_H)X=\Pi_HX+(I-\Pi_H)X=X,
\]

where compatibility and the null-space conditions give the first equality to `Pi_H X`. The unconstrained matrix subspace consists exactly of `(I-Pi_D) B (I-Pi_H)`. Orthogonal projection of a centered isotropic Gaussian onto this subspace is independent of its complementary projection. Therefore the conditional law is

\[
G\mid\text{history}\ \overset d=\ M+(I-\Pi_D)\widetilde G(I-\Pi_H),
\tag{2.1}
\]

with fresh independent Gaussian `Gtilde` of the same variance. Formula (2.1) is only a derivation; the simulator never creates this matrix.

For a new forward query `h`, calculate

\[
\begin{split}
\alpha&=C_H^+\langle H,h\rangle_P, & h_\perp&=h-H\alpha,\\
\beta&=C_D^+\langle X,h_\perp\rangle_P, & \sigma^2&=\|h_\perp\|_P^2.
\end{split}
\]

Then reveal

\[
 y=Y\alpha+D\beta+\sigma(I-\Pi_D)\xi,
 \qquad \xi\sim N(0,I_P),
\tag{2.2}
\]

and append `(h,y)` to `(H,Y)`. This uses `P` Gaussian numbers. Its conditional covariance is `sigma^2 (I-Pi_D)`, which is positive semidefinite by construction. No covariance clipping is needed mathematically.

For a new backward query `d`, using the history after any current forward queries, calculate

\[
\begin{split}
\gamma&=C_D^+\langle D,d\rangle_P, & d_\perp&=d-D\gamma,\\
\delta&=C_H^+\langle Y,d_\perp\rangle_P, & \tau^2&=\|d_\perp\|_P^2.
\end{split}
\]

Reveal

\[
 x=X\gamma+H\delta+\tau(I-\Pi_H)\zeta,
 \qquad \zeta\sim N(0,I_P),
\tag{2.3}
\]

and append `(d,x)` to `(D,X)`. New normals are independent of the transcript. Here `beta` and `delta` are the actual reuse responses; they are computed from fields, not fitted, supplied by a target, or obtained by differentiating the nonlinear feedback program.

If a new query belongs to the previous query span, its perpendicular component is exactly zero; the answer is the corresponding linear combination of previous answers, with no new randomness. At initialization all backward queries are zero, so they are skipped. A rank-deficient initial feature family is also valid. The formula does not require a nonsingular data Gram matrix.

**Implementation rule.** Maintain orthonormal bases by rank-revealing QR or SVD and apply the projectors through their bases. Do not form `P x P` projectors. Moore–Penrose formulas specify the algebra; forming and inverting ill-conditioned normal equations is not the recommended implementation. Any numerical rank threshold is an additional approximation whose discarded residuals must be recorded. Exact zero dependence and a small positive singular value are different cases.

## 3. Full initialization, time update, prediction, and restart

For data atoms `(u_a,y_a,p_a)`, `a=1,...,m`, with nonnegative weights summing to one:

1. Draw `w_i^0 = g_i` independently from `N(0,I_2)`, `i=1,...,P`.
2. Set `c^0=0`, learned-factor lists empty, and both query histories empty. For an exact comparison with the original finite network's stated initialization one may instead draw `c_i^0=P^{-1} eta_i`; this change is a separate vanishing initialization error relative to the population initial condition.
3. Store the random-generator state, atom law, time grid rule, and all subsequently generated arrays.

At step `k`, compute first-layer feature vectors

\[
h_a^k(i)=\tanh(w_i^k\cdot u_a).
\]

Reveal all `y_a^k=G h_a^k` sequentially by (2.2). The order is fixed and does not change the joint conditional distribution. Let the learned operator be represented by previously stored triples

\[
K^k=\sum_{\ell<k}\sum_b \omega_{\ell b}\,
d_b^\ell\otimes h_b^\ell,
\qquad \omega_{\ell b}=-2h_\ell p_b r_b^\ell,
\tag{3.1}
\]

where `(d tensor h) v = d <h,v>_P`. Calculate

\[
\begin{split}
z_a^k &= y_a^k+\sum_{\ell<k,b}\omega_{\ell b}
d_b^\ell\langle h_b^\ell,h_a^k\rangle_P,\\
v_a^k&=\tanh z_a^k,\qquad
f_a^k=\langle c^k,v_a^k\rangle_P,\qquad
r_a^k=f_a^k-y_a,\\
d_a^k&=c^k\operatorname{sech}^2 z_a^k.
\end{split}
\]

Products here are coordinatewise. Reveal `x_a^k=G^T d_a^k` by (2.3), then calculate

\[
q_a^k=x_a^k+\sum_{\ell<k,b}\omega_{\ell b}
h_b^\ell\langle d_b^\ell,d_a^k\rangle_P.
\]

The explicit Euler update is

\[
\begin{split}
c^{k+1}&=c^k-2h_k\sum_a p_a r_a^k v_a^k,\\
w_i^{k+1}&=w_i^k-2h_k\sum_a p_a r_a^k
\operatorname{sech}^2(w_i^k\cdot u_a)q_a^k(i)u_a.
\end{split}
\tag{3.2}
\]

Append the `m` learned triples in (3.1), with their current coefficients. This completes one step. Higher-order integrators add their stage queries and factors to the same history and must pay for those queries; they are not free improvements in this representation.

For prediction at a new `u`, form `h_u=tanh(w dot u)`, reveal its Gaussian action by (2.2), add the factored `K h_u`, and average `c tanh(z_u)`. The prediction query and Gaussian realization are added to the history if the simulation is to continue. Thus arbitrary new prediction requests carry a counted cost and can enlarge the state. A fixed evaluation bank can be included from the start. Uniform prediction on all of `S^1` additionally requires an angular interpolation error bound; finite-bank error does not establish it.

A restart checkpoint contains `w,c`, the atom law, current time, the coefficient list `omega`, all four query histories or equivalent basis/factor representations, the linear-algebra rank decisions, and the random-generator state. Merely storing `w,c,f` does not permit a valid restart. Continuing from the full checkpoint reproduces the same conditional distribution, and with the same generator state the same future random choices.

**Exact finite statement.** Induction on queries using (2.1) shows that all simulator fields have precisely the joint law of Euler integration of the `P`-representative physical equations using a single independent Gaussian matrix `G`. Formula (3.1) is exactly Euler's accumulated learned matrix update. Consequently no independent-adjoint substitution is present. This statement alone supplies neither a population approximation rate nor useful complexity.

## 4. Population causal version and its nontrivial bridge

For a fixed finite query program, the formal population counterpart replaces empirical inner products by expectations on the two coordinate probability spaces. It retains the conditional means in (2.2)–(2.3), but replaces projected finite-coordinate normals by independent scalar innovations for each representative:

\[
Y_{\rm new}=Y\alpha+D\beta+\sigma\xi_2,
\qquad
X_{\rm new}=X\gamma+H\delta+\tau\xi_1.
\tag{4.1}
\]

Every coefficient is still given by the explicit Gram and cross-correlation expressions above. A population-to-sampling implementation replaces each expectation by its own coordinate average, so there is no high-dimensional quadrature or unevaluated expectation in the executable construction.

There are two different numerical schemes: the projected exact finite simulator (2.2)–(2.3), and the independent-innovation empirical population simulator (4.1). They should not be silently identified. For example, if `r_D` is the rank of the preceding backward history, replacing `(I-Pi_D) xi` by `xi` removes the projection correction with exact conditional mean squared normalized norm

\[
\mathbb E\|\sigma\Pi_D\xi\|_P^2=\sigma^2 r_D/P.
\tag{4.2}
\]

It also produces an empirical adjoint-compatibility error

\[
D^T y/P-X^T h/P=\sigma D^T\xi/P,
\qquad
\operatorname{Cov}(\text{error}\mid\text{history})=
\sigma^2 C_D/P.
\tag{4.3}
\]

At fixed history length (4.2) is small as `P` grows. It need not be small when the history grows with accuracy or horizon. Later coefficients use the same corrupted correlations, so a single-query variance bound is not a global error guarantee. This is a precise error-production term, separate from its subsequent propagation.

The projected construction is preferable for the first certified candidate: it preserves the adjoint identity exactly and avoids adding (4.2)–(4.3). Its remaining statistical problem is quantitative approximation of the intended population by a finite number of representatives. The supplied network-identification assumption establishes a limit near the reference law, but the assignment explicitly supplies no rate. A fixed-program limiting argument for (4.1) also does not give a useful bound when `mJ` grows.

## 5. First backward response: an explicit check

At time zero let `H_a=tanh(g dot u_a)` and let `Y=(A0 H_a)_a` be centered Gaussian with covariance `C_ab=E[H_a H_b]`. The initial readout derivative and the first nonzero backward input are

\[
\dot c_0=2\sum_b p_b y_b\tanh Y_b,
\qquad
D_a(t)=t d_a+O(t^2),\quad
d_a=2\sum_b p_b y_b\tanh Y_b\operatorname{sech}^2Y_a.
\]

The initial forward history therefore generates the response coefficient

\[
\delta_a=C^+\mathbb E[Yd_a].
\tag{5.1}
\]

If `C` is invertible, direct Gaussian integration by parts gives `delta_ab=E[partial_b d_a]`. To verify that identity, differentiate the Gaussian density: `partial_b rho=-(C^{-1}Y)_b rho`; integrate the bounded smooth function `d_a` against it. Its derivative is

\[
\partial_b d_a=
2p_b y_b\operatorname{sech}^2Y_b\operatorname{sech}^2Y_a
-4\mathbf1_{a=b}\sum_\ell p_\ell y_\ell
\tanh Y_\ell\operatorname{sech}^2Y_a\tanh Y_a.
\tag{5.2}
\]

Thus the first backward field has mean `sum_b H_b delta_ab`, in addition to its Gaussian innovation. Formula (5.1), rather than differentiating the feedback map, is what the executable method evaluates. At singular `C`, (5.1) gives the projection onto the actual feature span; the density argument above is replaced by the same integration by parts on that span.

For the exact two-atom reference law define `kappa=E[tanh^2 G]`, `G~N(0,1)`. Then `Y_1,Y_2` are independent `N(0,kappa)`. Write

\[
a=3\mathbb E[\operatorname{sech}^4Y_1]
-2\mathbb E[\operatorname{sech}^2Y_1],\qquad
b=(\mathbb E[\operatorname{sech}^2Y_1])^2.
\]

The two response rows are `(a,-b)` and `(b,-a)`. In particular `b>0`, so the cross-feature response cannot vanish. This is a symbolic sanity check, not a quadrature calculation or experiment.

A still simpler check is a backward query `d=Y=GH` for one scalar feature column, independent of `G` before the forward query. The first backward conditional mean is `H E[Y^2]/E[H^2]=H` in the population calculation. The complete limiting field is `H+sqrt(E[H^2]) zeta`. Fresh independent adjoint noise would omit `H` and give the wrong second moment. This detects the reuse mechanism before any training occurs.

## 6. State, random, arithmetic, and data costs

Let `L` and `R` be total forward and backward query counts, including numerical stages and requested predictions. Plain Euler on `m` atoms has `L<=m(J+1)` and `R<=mJ`; zero or exactly redundant queries reduce ranks, not necessarily the number of coefficients needed for bookkeeping.

| Item | Worst-case count |
|---|---:|
| First-layer coordinates and readout | `3P` reals, plus initial/restart data |
| All four coordinate histories | `2P(L+R)` reals |
| Gram, cross-correlation, QR/SVD triangular factors | `O((L+R)^2)` reals |
| Learned coefficients, residuals, weights | `O(mJ)` reals |
| New independent Gaussian numbers | `O(P(L+R))` |
| Feature evaluations | `O(PmJ)` |
| All correlations, projections, and learned-factor actions | `O(P(L+R)^2)` arithmetic |
| Rank-revealing linear algebra with incremental updates | `O((L+R)^3)` arithmetic |

Recomputing every full pseudoinverse at every query would instead produce quartic history cost. An implementation must actually use incremental factorizations or pay that cost. No `P x P` matrix is formed; projection and learned actions use history vectors. Nevertheless, once the history rank approaches `P`, memory and arithmetic approach ordinary dense-operator costs. Avoiding a stored neural matrix does not remove that crossover.

For a cost illustration only, take the reference two-atom law, `J=400` and hence `h=0.1`. Then `L+R` is approximately 1600. At `P=4096`, coordinate histories alone take about 105 MB in 64-bit arithmetic, and the conservative `P(L+R)^2` arithmetic count is about `1.05e10`. At `P=100000`, histories take about 2.56 GB and this count is `2.56e11`. Constants and symmetry can improve arithmetic, but these are substantial costs. `h=0.1` is not certified accurate by this illustration. Extra stages or a larger data atom count increase history costs quadratically and cubically.

For a non-atomic law, drawing `m` fixed examples costs `m` calls to its sampler plus storage. Their law discrepancy persists throughout the trajectory and needs its own bound. Large data quadrature is especially expensive here because each atom at each time becomes an operator query. Replacing full-law integration by fresh minibatches would be a different stochastic approximation and needs a new analysis; it is not hidden inside the present cost claim.

## 7. Exact error production versus propagation

There are separate axes:

1. **Initialization:** finite-network readout noise versus population zero. It vanishes at initialization but still needs a propagated bound if included.
2. **Data law:** the force defect is exactly `(integral dmu_m - integral dmu)` applied to each displayed force integrand. Bounded labels alone do not bound this defect uniformly over the evolved nonlinear random integrands without additional control.
3. **Time:** along an exact trajectory `S(t)`, the one-step Euler defect is exactly
   \[
   \int_{t_k}^{t_{k+1}}[F_\mu(S(s))-F_\mu(S(t_k))]\,ds.
   \]
   A proven modulus of continuity of the force turns this into a numerical source bound. Temporal regularity without quantitative constants does not select `J` for a requested error.
4. **Representatives:** for the projected simulator this is the finite-representative-to-population discrepancy. It is not an extra Gaussian quadrature, but no usable finite-`P` bound is yet proved. For (4.1), sampling errors in all Grams and correlations, innovation empirical laws, and the compatibility defect (4.3) are additional explicit sources.
5. **Numerical conditioning:** a nonzero query residual discarded by numerical rank truncation has an omitted Gaussian component with conditional RMS norm `sigma sqrt(1-r_D/P)` on a forward query, as well as its omitted conditional mean. Recording a small eigenvalue alone does not bound both terms.
6. **History compression:** none is performed here. Any later deletion or truncation creates another source, which cannot be excused by a stability estimate.

For a positive definite correlation matrix with smallest eigenvalue `lambda`, a perturbed coefficient `bhat=(C+E)^{-1}(v+e)` obeys, when `||E||<=lambda/2`,

\[
\|\widehat b-b\|\le
2\lambda^{-1}\|e\|+2\lambda^{-2}\|E\|\,\|v\|.
\tag{7.1}
\]

This follows by the inverse identity and `||(C+E)^{-1}||<=2/lambda`. It diagnoses why a naive Gram-based population sampler lacks a uniform error theorem: temporally neighboring queries are almost dependent, and early backward fields are small. It does not prove that the physical process is unstable. Scaling and exact linear consistency can cancel large coefficient condition numbers. The projected finite simulator preserves that consistency; a proof comparing it to population still must quantify such cancellations or use an invariant basis-level estimate.

For continuous exact physical flow, gradient dissipation gives

\[
\frac{d}{dt}\mathcal L
=-\|\dot w\|_{L^2_1}^2-\|\dot K\|_{\rm HS}^2
-\|\dot c\|_{L^2_2}^2.
\tag{7.2}
\]

Indeed each supplied velocity is minus the corresponding gradient in the stated Hilbert metrics; pairing the gradient with its negative gives (7.2). Since initial prediction is zero, `L(0)<=Y^2`. Cauchy–Schwarz in time yields

\[
\|c(t)\|_2\le Y\sqrt t,\quad
\|K(t)\|_{\rm HS}\le Y\sqrt t,\quad
\|w(t)-g\|_2\le Y\sqrt t.
\tag{7.3}
\]

These exact energy bounds do not automatically hold for unmodified Euler at arbitrary step size.

At the observable level, along an exact physical trajectory the residual obeys a positive-kernel evolution `dot r=-2 Theta_t r`, where `Theta_t=J_t J_t^*` is the Gram operator of the derivative of prediction with respect to the three parameter fields. Thus its propagator is an `L^2(mu)` contraction: differentiating the squared norm of a homogeneous solution gives `-4 <e,Theta_t e><=0`. A perturbed kernel produces a source `-2(Thetahat-Theta) rhat`, so the observable difference can be bounded by the time integral of that source. This is useful propagation structure, but it is not a bound on the kernel error produced by representative sampling. State dependence of the kernel is the missing link.

## 8. Practical error check through 40

Even an optimistic benchmark is demanding. Suppose exact independent samples of the *true* population coordinates were available at one time, so coefficient feedback caused no error. Since `|V|<=1`, the variance of the Monte Carlo prediction would be at most `||c(t)||_2^2/P <= tY^2/P`. The resulting RMS upper bound at `T=40`, `Y=1`, reaches `0.1` only at `P>=4000`, and `0.02` at `P>=100000`. These are not lower bounds on the necessary sample count, and they are not guarantees for the interacting simulator. They are the sample counts required by this particular energy-only, pointwise, idealized variance bound. Actual readout norms may be much smaller; no such bound was supplied.

Uniform-in-time confidence, law error, time error, and adaptive correlation errors require more budget. In particular, these pointwise counts cannot be used in a final certificate. Conversely they do not prove the construction impractical: residual decay could sharply reduce the readout norm, accumulated forcing, number of effective time steps, and effective history rank. Establishing those quantitative reductions is a real missing result.

The assignment's tail and temporal-regularity assumptions are qualitative here. They permit neither assigning a small numerical constant to a sampling bound nor assuming a conditioned Gram spectrum. Generic Gronwall estimates with a constant integrated over 40 could make sample and step requirements astronomically large. The positive-kernel contraction above is a possible mechanism for avoiding that loss, but it must be coupled to an actual source estimate.

Therefore this round establishes a computable mechanism and exposes its costs, but does **not** establish useful `0.02–0.1` accuracy through time 40. It would be incorrect to call the hierarchy successful on the strength of a fixed finite-program Gaussian limit.

## 9. Claim ledger, hostile audit, and smallest next obligation

| Claim | Status | Main dependency / resolver |
|---|---|---|
| Conditional two-sided Gaussian query formulas, including singular histories | Proved finite identity | Gaussian orthogonal projection derivation in section 2 |
| All response coefficients computed from current and past fields | Exact | Equations (2.2), (2.3); no derivative oracle |
| Causal initialized, updated, predicted, restartable finite algorithm | Exact construction | Full state in section 3 retained |
| Same joint law as finite representative Euler flow with one reused matrix | Proved by sequential conditioning | Valid finite precision implementation still required |
| Independent-population-innovation replacement has no finite-sample defect | False | Explicit compatibility defect (4.3) |
| Population identification near the supplied reference law | Assumed input for original physical flow; no new proof | Does not supply this route's numerical rates |
| Quantitative population error for this simulator on a fixed horizon | Open | Uniform adaptive representative source estimate |
| Useful error and cost through 40 | Open | Constants for source, propagation, and time regularity |
| Natural dynamics for broader executable same-model laws | Exact finite algorithm | Population existence/identification beyond the supplied neighborhood remains open |

The strongest structural objection is that the history can become as expensive as a dense operator before a useful statistical error is reached. The strongest proof obstruction is correlated representative error entering ill-conditioned reuse coefficients; coordinatewise Gaussian laws do not resolve it. The strongest mundane explanation for apparently good future tests would be small movement of the first layer or observable insensitivity despite inaccurate backward response. No test was run, and no such explanation has been ruled out.

**Smallest decisive mathematical obligation.** Prove a quantitative bound for the prediction-relevant error produced by the projected representative simulator, uniform over a discretization with `L+R` queries, expressed in invariant query-residual energies and accumulated forcing rather than the smallest eigenvalue of the entire raw Gram matrix. It must include bias from adaptive coefficient reuse, not only fluctuations of an iid final readout. Then combine it with observable contraction and a costed time-defect estimate. A result with unusably exponential constants would establish convergence but would not settle the practical target.

An especially useful first sublemma would compare two representative resolutions using matched Gaussian innovations and bound the accumulated error by a summable residual-energy quantity, without multiplying a `lambda_min^{-1}` factor at every query. This is presently a conjectured mechanism, not a theorem.

**Status:** viable exact numerical skeleton; quantitative convergence and useful-cost certificate unresolved. **Reopen condition:** an invariant quantitative adaptive-sampling lemma, or an authorized bounded experiment with preregistered acceptance gates that shows whether low effective history rank and accumulated forcing are actually present. Any experiment would require coordinator preregistration before implementation or execution. No claim about impossibility of all admissible simulators follows from this route's gaps.
