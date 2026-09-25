# Rational residual-activity response-memory closure

Status: first-principles candidate and conditional approximation argument; no experiment or external source used. The scientific input was the supervisor's explicit assignment and subsequent implementation clarifications only. This report does not assert that input compatibility proves its stability assumptions.

## Contract and conclusion

Keep the actual initialized matrix `W0`, its forward action, and its transpose action. Replace only the learned dense increment by an autonomous population-state reconstruction. Retain the original finite-sample nonlinear tanh forward and backward computations at the reconstructed weights. The construction below has `O(n M P)` additional scalar state, rank at most `M P`, rational coefficients after an exact tanh lift, and no trajectory oracle or fitted dictionary.

It is a genuine approximation hierarchy under explicit boundedness and stability conditions. Its approximation defect is derived and bounded, rather than postulated. Compatibility of the inputs, including exclusion of parallel/antiparallel pairs, does not by itself establish these conditions or width-independent efficiency.

## 1. Exact source and intrinsic activity coordinate

Write `h_a=h1_a`, `delta_a=delta2_a`, `r_a=f_a-y_a`, and

\[
 \rho=\left(M^{-1}\sum_a r_a^2\right)^{1/2},\qquad
 \dot s=\rho,\quad s(0)=0,\qquad v=\frac{s}{1+s}.
\]

The activity coordinate is a state, not explicit physical time. Define, for the proof only,

\[
 u_a=\frac{r_a\delta_a}{\rho}.
\]

The exact learned increment satisfies

\[
 W_2=W_0+K_*/n,\qquad
 \dot K_*=-\frac2M\sum_a r_a\delta_a h_a^T
          =-\frac{2\rho}{M}\sum_a u_a h_a^T.
\]

Thus it is an activity-history cross moment of a second-layer response and a first-layer response. All responses in the surrogate below are computed using its current reconstructed matrix; they are not supplied from the dense trajectory.

## 2. Rational gates and stored moments

For an integer `P>=1`, set `h=1/P`, `c_j=(j+1/2)/P`, `j=0,...,P-1`, and

\[
 k_j(v)=\left(1+((v-c_j)/h)^2\right)^{-2},\qquad
 w_j(s)=\frac{k_j(s/(1+s))}{\sum_\ell k_\ell(s/(1+s))}.
\]

These positive rational gates sum to one. Their centers and widths depend only on `P`, not on a realized dense trajectory or an unknown final activity. Fix a positive pseudomass `eta`; the proposed hierarchy uses `eta=10^{-3}P^{-6}`.

For every training input `a` and gate `j`, store two neuron vectors `A_aj,B_aj`; share scalar `C_j` across inputs:

\[
\begin{aligned}
 \dot A_{aj}&=w_j r_a\delta_a,& A_{aj}(0)&=0,\\
 \dot B_{aj}&=w_j\rho h_a,& B_{aj}(0)&=\eta h_a(0),\\
 \dot C_j&=w_j\rho,& C_j(0)&=\eta.
\end{aligned}
\]

Reconstruct

\[
 \boxed{K=-\frac2M\sum_{a,j} A_{aj}\left(B_{aj}/C_j\right)^T,
 \qquad \widehat W_2=W_0+K/n.}
\]

The `A` and `B` vectors are integrated neuron responses. They are neither fixed response features nor freely optimized basis vectors. Scalar activity gates provide the quadrature organization; no neuron dictionary is prescribed.

Initialization gives `K(0)=0`. More strongly,

\[
 \dot K(0)=-\frac2M\sum_a r_a(0)\delta_a(0)h_a(0)^T,
\]

because `B_aj(0)/C_j(0)=h_a(0)` and the gates sum to one. The pseudomass avoids an initial `0/0` without suppressing the true initial source.

## 3. Exact derivative-memory coordinates

This same closure can be written as weighted moments of response derivatives. Define

\[
 D^1_{aj}=C_jh_a-B_{aj},\qquad
 D^2_{aj}=C_ju_a-A_{aj}-\eta u_a(0).
\]

Both memories start at zero and obey the exact identities

\[
 \boxed{\dot D^1_{aj}=C_j\dot h_a,\qquad
        \dot D^2_{aj}=C_j\dot u_a.}
\]

Consequently

\[
 B_{aj}/C_j=h_a-D^1_{aj}/C_j,\qquad
 A_{aj}=C_ju_a-D^2_{aj}-\eta u_a(0).
\]

These are cumulative weighted derivative moments, not Taylor coefficients or a finite jet approximation. Repeated derivatives are unnecessary. The transformation is exact for positive `rho`. At a stationary zero-residual state the original `A,B,C` coordinates remain well defined and stationary.

For implementation, evolving `A,B,C` is preferable: derivative coordinates subtract quantities that can nearly cancel, and `u` derivatives contain divisions by `rho`. Reporting `D1,D2` reconstructed from these stable coordinates still reports the states of the equivalent derivative-memory system. An implementation claiming to evolve derivative coordinates directly should disclose its conditioning near zero residual.

## 4. Complete autonomous rational lift

Retain `W1,W3`, training responses `h1_a,h2_a`, the moment states, and `s,rho`. Initialize the responses by the actual tanh forward pass. The original first- and third-layer equations remain

\[
 \dot W_1=-\frac2M\sum_a r_a\delta^1_a x_a^T/\sqrt d,
 \qquad
 \dot W_3=-\frac2M\sum_a r_a h^2_a,
\]

with backward signals evaluated at `W0+K/n`. If `z1_a=W1 x_a/sqrt(d)` and `z2_a=What2 h1_a`, use the exact response lift

\[
 \dot h^1_a=(1-(h^1_a)^2)\odot(\dot W_1x_a/\sqrt d),
\]

\[
 \dot h^2_a=(1-(h^2_a)^2)\odot
       (\dot K h^1_a/n+\widehat W_2\dot h^1_a).
\]

All squares and products in these displays are componentwise. In scientific prose these factors are the original activation derivatives; their polynomial identities establish rationality of the implementation, rather than change the activation.

Compute `Kdot` explicitly by differentiating the displayed `A B^T/C` reconstruction using the already known `Adot,Bdot,Cdot`. Then compute `h2dot`, `fdot`, and

\[
 \dot\rho=\frac{M^{-1}\sum_a r_a\dot f_a}{\rho}.
\]

This order has no implicit equation. For derivative-memory coordinates, compute `udot` only after those steps:

\[
 \dot u_a=(\dot f_a\delta_a+r_a\dot\delta_a)/\rho
              -u_a\dot\rho/\rho.
\]

For scalar linear readout, `delta2_a=W3 odot (1-h2_a^2)` and its derivative is polynomial in `W3,W3dot,h2,h2dot`. Other normalization constants in the specified forward pass simply multiply these formulas.

The invariant `rho^2=mean(r^2)` and the tanh consistency manifolds hold exactly when initialized consistently. For nonzero residual the lift is rational on `rho>0,C_j>0`. Zero initial loss is the stationary special case. Numerical integration must check the invariants; exact invariance is not a numerical guarantee. The lifted equation for `rho` can be poorly conditioned when residuals are tiny.

Partitioning the population state as requested, `m1` holds the first-layer weights, responses, and `B` or `D1` histories; `m2` holds readout weights, second-layer responses, and `A` or `D2` histories. The finite shared clocks and masses complete the state. The statistics `Q` are current response contractions and the required `W0,W0^T` actions. No inaccessible encoder is imported.

## 5. One exact defect

Let `bar h_aj=B_aj/C_j`, `bar u_aj=A_aj/C_j`. Relative to the original middle-layer gradient evaluated at the surrogate's own current state, the exact vector-field defect is

\[
\boxed{
 E_2:=\dot{\widehat W}_2+
       \frac{2}{nM}\sum_a r_a\delta_a h_a^T
   =-\frac{2\rho}{nM}\sum_{a,j}w_j
          (u_a-\bar u_{aj})(\bar h_{aj}-h_a)^T.}
\]

This is the only modification of the original weight dynamics. It includes both forward and transpose effects because both use the same reconstructed matrix. It vanishes initially. It is a covariance mismatch produced by averaging response history within finite activity bins, not an arbitrary damping term.

## 6. Derived localization estimate

Use neuron norm `||z||_n=||z||_2/sqrt(n)`. Suppose along a surrogate trajectory

\[
 s_\infty\le S<\infty,\qquad
 \|u_a(s)\|_n\le U,\qquad
 \|h_a(s)-h_a(t)\|_n\le H|s-t|.
\]

These are explicit hypotheses. For example, bounded `||delta2_a||_n<=D2` implies `U<=sqrt(M)D2`. The given `W1` equation implies `H<=2 D1 X^2` if `||delta1_a||_n<=D1` and `|x_a^T x_b|/d<=X^2`, since the tanh derivative has magnitude at most one.

The following elementary gate facts yield the estimate. The gate denominator has upper and lower positive constants independent of `P`, and

\[
 \sum_j w_j(v)|v-c_j|\le C h.
\]

For a gate truncated to its past history, its conditional mean age in the `v` coordinate is at most `C(h+|v-c_j|)`. To see this, centers behind `v` contribute their distance plus the finite first moment of the kernel `(1+z^2)^{-2}`; for centers ahead of `v`, integrate the decreasing algebraic tail to obtain the same bound. On `0<=s<=S`, `ds/dv<=(1+S)^2`; the change-of-measure density is bounded above and below. Hence

\[
 \sum_jw_j(s)
 \frac{\int_0^s w_j(t)(s-t)\,dt}
      {\int_0^s w_j(t)\,dt}
 \le C_S h.
\]

The pseudomass adds at most `H S eta/w_min`, where `w_min` is the minimum gate value over all gates and `v in [0,1]`. Since `w_min>=c h^4`, the choice `eta=10^{-3}h^6` gives

\[
 \sum_jw_j\|\bar h_{aj}-h_a\|_n
 \le H(C_S h+C S\eta h^{-4})=O_S(Hh).
\]

Here a zero history length is handled by its continuous limit. Also `||bar u_aj||_n<=U`, because its denominator includes positive pseudomass and its numerator is an integral of `w_j u_a ds`. Therefore the exact defect satisfies

\[
 \boxed{\|E_2(t)\|_F
   \le 4 U H\rho(t)(C_S h+C S\eta h^{-4})
   =:c_P\rho(t),\qquad c_P\longrightarrow0.}
\]

The inequality uses `||xy^T/n||_F=||x||_n||y||_n`. Constants can grow with total activity `S`; compactification does not make an infinite-activity path compact in the required response-variation metric.

In particular, `integral ||E2||_F dt <= c_P S`. This estimates error production from actual dynamics. It does not alone prove stability of all observables over infinite physical time.

## 7. Conditional all-time approximation argument

For each fixed width, bounded smooth dynamics and the defect bound give convergence on compact physical-time intervals by the ordinary perturbed-ODE estimate. For a uniform-in-time conclusion, one sufficient additional package is a common forward region for the true and approximate trajectories in which:

1. the original gradient system has a uniform loss decay inequality `Ldot<=-2 gamma L`, where `L=rho^2`;
2. the perturbation's contribution to loss is bounded by `C_L rho ||E2||_F`;
3. total weight velocity in the selected comparison norm is at most `C_V rho` for the original field, and the embedding of `E2` into that norm is bounded;
4. the source bounds used above hold uniformly, and the region's forward containment is independently justified (for example by a path-length bootstrap with margin).

These conditions are stated on the actual model; in gradient notation the first is a Polyak--Lojasiewicz type bound with the model's fixed parameter mobilities. Normalizations and norm conversion factors must be retained.

For sufficiently large `P`,

\[
 \dot L_{\rm closure}
 \le-2\gamma\rho^2+C_Lc_P\rho^2
 \le-\gamma\rho^2.
\]

Thus both flows have uniform exponential residual tails, the closure has `s_infinity<=2 rho(0)/gamma`, and its remaining parameter path after time `T` is exponentially small uniformly in `P`. This closes the finite-activity hypothesis using any larger `S` in the preceding estimate. Convergence on `[0,T]`, followed by the uniform tail bound and then `T->infinity`, gives all-time convergence. There is no interchange of limits without this tail control.

This is a sufficient conditional hierarchy result, not a proof that these hypotheses hold for every compatible finite input set. Width-independent complexity requires all source, stability, initial-loss, and comparison-norm constants to be uniform in width. Finite state dimension by itself proves neither that fact nor low-rank compressibility.

## 8. Size, implementation costs, and falsifiers

The moment storage is `2 n M P + P` scalars. Including training responses, full first-layer weights, readout, and clocks gives `2 n M P + 2 n M + nd+n+P+2` scalars, up to whether residual/output scalars are cached. Actual initialized `W0` remains a separate `n by n` operator. Matrix and transpose actions of the increment cost `O(n M P)` per vector and require no dense learned matrix. The retained `W0` matvecs are still dense; this is learned-state compression, not removal of the initialized operator cost.

Evolve raw `A,B,C`, not their ratios. Small pseudomass can create fast transient variation in ratios; `eta=P^-6*10^-3` is a theoretical localization choice and may require careful step control or quadrature. Higher `P` without solver refinement can therefore be numerically inconclusive. The conditioning issue is exposed rather than removed by the rational formulation.

Concrete falsifiers are persistent growth of total activity, loss of a uniform response-variation bound, failure of a gradient/stability bound in the visited region, or approximation errors that persist after numerical convergence as `P` increases. Failure at small `P` rejects that tested compression level; it does not disprove the hierarchy. A width trend in the required `P` would challenge the width-independent version even if every fixed-width system converges.

No experiments, empirical accuracy claims, or promotion claims are made in this report.
