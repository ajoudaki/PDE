# Independent audit of quantitative odd-activation improvements

Audit inputs: `/tmp/sharpen_affine.md` and `/tmp/sharpen_constants.md`, both read in full; the model, affine equations, Gaussian/freezing proof, threshold selection, and source interfaces in `PROOF.md`, `AFFINE_CORE.md`, `SOURCE_AND_LIMIT_BRIDGE.md`, and the relevant finite-array premise in `sources/TWO_SAMPLE_SOURCE_BASELINE.md`. The chronological source algebra was checked at its stated interface and displayed recursions. No sibling reviews or status files were consulted. No experiments, delegation, commits, or proof edits were performed.

## Verdict

**PASS for the stated quantitative component results.** I found no mathematical error in the active normalization, balances, affine time/norm bounds, logarithmic integrated curvature, cap-uniform comparison on a radius-one raw tube, exponent 7/4 sufficient restriction, Gaussian variance improvement, Hermite residual bounds, Wasserstein transfer, or finite-array energy bound.

**FAIL / OPEN for the stronger requested conclusion that the complete population/GF/raw-GD theorem admits a coefficient `theta_delta = c delta^p`.** This is a failure to establish that stronger conclusion, not a false assertion in these notes: both notes expressly retain the unresolved source-response restriction. The cap-uniform raw comparison is not a proof of cap removal, source tails, uniqueness of the uncut flow, or the finite GF/GD limits under a polynomial coefficient restriction.

| Claim | Verdict | Qualification |
| --- | --- | --- |
| Exact active normalization and lambda scaling | PASS | Reference gain is frozen at the nonlinear path's same gain a. |
| Operator and scalar balances | PASS | Products are bounded-operator products; no infinite trace is used. |
| `S <= 2/lambda = O(delta^-1/2)` and readout `O(lambda^-1/4)` | PASS | Matching lower rates hold as lambda tends to zero; not every admissible dataset has time Theta(delta^-1/2). |
| Logarithmic integrated affine raw Hessian | PASS | Retaining the exact factor lambda is essential and justified. |
| Cap-uniform radius-one raw comparison, `E <= C0 e lambda^-3` | PASS | For each fixed cap; uniform constants; no claim of polynomial source bounds. |
| Endpoint and forward errors, exponent `e <= c_* delta^(7/4)` | PASS | Sufficient for capped primal comparison, scalar endpoint, and regression margin. |
| All actual affine variances at least `1/404` | PASS | Uses the previously proved Gaussianity, zero means, and frozen inactive-field orthogonality. |
| Global Hermite nonaffinity and W2-Lipschitz square-root residual | PASS | No upper variance bound or perturbed variance lower bound is required. |
| Old threshold at most `C delta^6 exp(-c delta^-6)` | PASS | An upper bound on that selected threshold, not on the maximal valid coefficient. |
| Improved finite-array premise `P_delta=11+sqrt(2S_delta)` | PASS | Constant feature controls and sufficiently fine fixed meshes; probability limits at each fixed mesh. |
| Complete theorem with improved nonpolynomial selection | PASS relative to supplied source theorem | The recomputed K restriction remains present. |
| Full polynomial complete theorem | FAIL / OPEN | New chronological source-response estimate or another construction is still required. |

## 1. Normalization and exact dynamics

Write `v=(1+tau rho)/2`, `r=sqrt(v)`, `p=P1/r`, `D=sigma C`, and `lambda=a^3 r`. The active first-layer metric is exactly `d ||dw||_2^2=||dP1||_2^2/v=||dp||_2^2` when `dw` is parallel to the input direction u. On the full first-layer space, the linear map `dw -> (dw dot u)/r` has operator norm one from the raw norm `sqrt(d)||dw||_2`. Its metric adjoint is an isometric injection. Therefore passing to active coordinates does not introduce an inverse power of v in any raw Hessian block.

Substitution in AFFINE_CORE equation (4), with normalized time `t=lambda s`, gives all four equations in sharpen_affine (1), including the signs and powers of a. The objective is exactly `g=lambda <D,BAp>`. The lower bound `lambda >= sqrt(delta)/(8sqrt(2))` uses only `a>=1/2` and `v>=delta/2`.

For `a=1-e`, the comparison still uses the affine activation `a z` at that same a. No derivative with respect to a is taken, and no unaccounted term of size `|a-1|` is omitted. Uniformity in `a in [1/2,1]` closes this quantifier correctly.

## 2. Balances, radial growth, and time

Direct differentiation cancels the two rank-one terms in each of `BB*-D tensor D`, `AA*-B*B`, and `A*A-p tensor p`. Also `d||p||^2/dt=d||D||^2/dt=2F`, so `||p||^2=1+c^2` for `c=||D||`.

The operator bounds `||B||^2<=100+c^2` and `||A||^2<=200+c^2` are valid. The stronger `||A||^2<=101+c^2` in sharpen_constants follows independently from the third balance and is also valid. Positivity gives `||B*D||^2>=c^4` and `||Ap||^2>=c^2(1+c^2)`.

The gradient identity gives `F' >= 2c^4(1+c^2)`. The exact derivative of `F^2-(2/3)c^6-(1/2)c^8` is `2F[F'-2c^4(1+c^2)]`; it is nonnegative because F starts at zero and F' is a sum of squares. This verifies (8) without division at the initial zero readout.

The radial relation `D''=JJ*D` implies convexity of c and `c'(0+)=||B0 A0 p0||=1`; thus `c>=t` and `c'>=c^3/sqrt(2)` for positive t. Before the target `F=3/(2lambda)`, one has `c<=M=(3/(sqrt(2)lambda))^(1/4)`. Reaching c=1 costs at most one normalized time unit, and the remaining time is at most `sqrt(2) integral_1^M c^-3 dc < 1`. These estimates also prevent raw-coordinate blowup: the HS derivatives, not merely the operator sizes, are bounded/integrable on the pre-hit branch. The stated `1100 M` raw displacement bound is conservative and valid.

For the matching lower bound, while c<=1 the estimate `||D'||<202` holds. At lambda<=1/200 the target cannot be reached with c<=1, so the time to that level is at least 1/202. For c>=1, `F<202 c^4`, which gives the matching terminal readout lower bound. Hence `S=Theta(lambda^-1)` in the small-lambda regime, and worst-case separated data with `v=delta/2` exhibit `Theta(delta^-1/2)`. A dataset with v bounded below need not have that delta-dependent time.

The stronger radial inequalities (27)--(30) of sharpen_constants also check: dividing `<C,C''> >= 2 lambda^2 u^4(1+u^2)` by u yields its stated lower bound for u'', and integration against `2u'` gives the coefficients 1 and 2/3 in (28).

## 3. Integrated Hessian and cap comparison

The objective is multilinear in four blocks. Its Hessian has zero diagonal blocks and exactly three off-diagonal blocks in each block row/column. Every such block has norm at most `lambda R^2`, where `R=sqrt(200+c^2)`. This is true with HS metrics for the action increments, and with the full raw first-layer metric by the contraction established above. Thus its norm in the sum of component norms is at most `3lambda R^2`.

Using `dt/dc<=sqrt(2)/c^3` after c=1 gives `integral c^2 dt<=1+sqrt(2)log M`; consequently (11) and (13) have the stated constants. The inactive affine directions are exactly annihilated by the objective. Nearby nonlinear states need not have frozen inactive components for this Hessian statement to hold.

On the stopped tube E<=1, the four relevant primal sizes and the normalized active coordinate are bounded by `b=R+1`. The same-state cap comparison from SOURCE_AND_LIMIT_BRIDGE uses `|tau_R(q)|<=|q|`, bounded arctangent, and the gate discrepancy e. The raw component bounds 7,14,11,6 sum to 38, so the constant 40 in (14) is valid in the stronger raw/HS sum norm as well as the older projected/operator norm.

Subtracting the affine fields after this same-state comparison gives `E'<=3lambda b^2 E+40 e b^3`. In particular, no nonlinear Hessian or unbounded gate derivative is being substituted for the affine Hessian.

The numerical checks are valid: `b^2<=(7/6)(200+c^2)`, `b^2<=235M^2`, and independently `b^3<=3600M^3`. The stability integral is at most `1404+5log M`. Gronwall then gives `288000 exp(1404)e lambda^-1 M^8 = 1296000 exp(1404)e lambda^-3`. Restriction (18) closes the tube with E<=1/2. Fixed-cap local Lipschitzness and bounded raw directions justify strong continuation and mesh refinement. These statements do not require cap-uniform source derivative estimates.

## 4. Forward fields, endpoint, and polynomial exponent

The improved forward differences (20) follow by expanding against the affine reference, using `a<=1` and bounding the arctangent terms directly. In particular the third-layer bound is `b[2bE+(pi/2)eb]+R^2 E+(pi/2)eb`, which is at most `3b^2E+pi e b^2`. Combining with (17), `b^2<=235M^2`, and `M^2<1.5lambda^-1/2` gives `C_z=1500C0` safely.

At a common state, the third feature difference is at most `(pi/2)e(b^2+b+1)`, so prediction error is at most `5e b^3`. For the affine state difference, the sum-norm dual estimate uses each gradient block at most `lambda b^3`, hence `|Delta g0|<=lambda b^3 E`, without an extra factor four. These bounds imply `C_g=14400C0` in (22).

The restrictions require powers lambda^3, lambda^(11/4), and lambda^(7/2). Their delta exponents are 3/2, 11/8, and 7/4 respectively. The last is strongest on `(0,1]`, so the displayed absolute c_* does imply all three. This is a valid sufficient polynomial component theorem; optimality of exponent 7/4 is not asserted or proved.

## 5. Gaussian variance and regression

Radial convexity gives `||BAp||=||D'||>=c'>=1`. Thus `||Ap||^2>=1/(100+c^2)` in addition to the balance bound `c^2(1+c^2)`. Splitting at c^2=1 gives the uniform `1/101` bound.

The old affine construction proves zero active/inactive covariance, frozen inactive fields with their original variance, and centered Gaussian marginals. Applying those exact facts gives first-, second-, and third-layer variances at least 1, 1/404, and 1/16. The use of variance rather than uncentered second moment is justified by the already proved zero means. No analogous freezing or Gaussianity is imposed on the nonlinear path.

Both Hermite calculations are correct. In sharpen_affine, Gaussian integration by parts gives `h(sigma)=-2sigma^3 E[G^2/(1+sigma^2G^2)^2]`; differentiating the original Hermite expectation and integrating by parts gives `h'(sigma)=-2sigma^2 E[G^4/(1+sigma^2G^2)^2]<0`. Restriction to `|G|<=1` yields exactly `eta_* = 4*404*exp(-1)/(27*pi*405^4)` after dividing h^2 by `E H3^2=6`.

The integral representation and lower bound in sharpen_constants are also valid; dominated convergence and the arctangent remainder show `eta_delta ~ delta^3/49152` for the old enlarged Gaussian variance interval. This does not conflict with a constant lower bound for the actual narrower family of reference laws.

For every square-integrable law, the optimal arctangent regression slope lies in `[0,1]` by the independent-copy covariance identity. The residual function for any such slope is 1-Lipschitz, so the optimizer-competitor argument proves that the square root of the optimized residual is 1-Lipschitz in W2, including constant variables. The perturbed law requires no variance lower bound. Finally the regression error for `az+e atan z` is exactly e^2 times this residual.

## 6. Old selection and improved finite arrays

The old `p=Theta(delta^-5/2)` and `p^2 S_delta=Theta(delta^-6)` follow from their explicit definitions. Because the old final selection includes one half of the source reciprocal, the stated factor 1280 and upper bound `C delta^6 exp(-c delta^-6)` are correct. They neither lower-bound the chosen minimum nor upper-bound the largest mathematically valid coefficient. The K restriction can be considerably smaller.

For the new finite-array premise, the population gradient energy is exactly 3/2 up to the affine endpoint. Strong affine Euler convergence on sufficiently fine meshes makes the discrete squared-velocity sum at most 7/4. Uniformity of the mesh-size cutoff in admissible gain/data follows from the earlier uniform bounded-ball estimates. At each such fixed mesh, each finite squared raw update norm is a finite combination of converging empirical scalar contractions, including the first-layer Gamma factor; hence the finite sum is at most 2 with probability tending to one.

Cauchy--Schwarz gives a raw displacement bound sqrt(2S_delta) simultaneously for all prefixes. The raw norm controls each ordinary matrix Frobenius norm and each projected first-layer change with the metric factors printed in the note. Initial operator norms at most 10, initial projection norms at most 2, and readout norm at most 1 therefore fit strictly below `P_delta=11+sqrt(2S_delta)`. The original random finite readout is retained and vanishes only in the fixed-program limit. This exactly supplies the source lemma's premise for the meshes under consideration; no assertion over growing random transcripts or arbitrary time-varying controls is needed.

The exponent arithmetic checks: `36P_delta^2 S_delta ~ 2,654,208 delta^-2`, and `9b^2S_delta ~ 7,962,624 delta^-2`. The modified complete selection keeps all required source constraints and replaces only the now unnecessary regression-transfer constraints. Relative to the supplied complete source theorem, it is a valid improved complete selection, still nonpolynomial.

## 7. Remaining proof obligation

The raw affine variational equation bounds perturbations of the four actual parameter blocks. The canonical source derivative system instead uses formally distinct source slots, both action orientations, learned memories, and current transpose returns. These are not automatically the same linear system in the same norm. Absolute row sums can lose cancellations retained by the raw Hilbert metric. Neither note proves a norm-controlled identification or a replacement response estimate.

Accordingly one cannot replace `exp(36P^2S)` or `exp(KS)` in the old source proof by the polynomial raw propagator merely by substitution. Establishing an appropriate chronological source resolvent bound, or bypassing that source perturbation construction, is the concrete outstanding task before claiming a full polynomial theta coefficient.

## 8. Additional audit: combined finite-array premise with exponent delta^-3/4

**PASS** for the subsequent proposed sharpening

`M_delta = 24^(1/4) delta^-1/8`,
`S_delta_new = 16 sqrt(2) delta^-1/2`,
`P_delta_new = 12 + 600 M_delta`.

Indeed the lower bound on lambda gives `M <= M_delta` and `S <= S_delta_new`. The HS path length of either learned action is invariant under the change of time: `integral_0^S ||dA/ds||_HS ds = integral_0^T ||dA/dt||_HS dt`, and similarly for B. Thus the already checked bound `500M` applies in original feature time.

Strong affine Euler convergence in the raw Hilbert space, combined with local Lipschitzness of the affine gradient into that same space, gives uniform convergence of each block velocity and convergence of its norm Riemann sums. After a sufficiently fine mesh restriction, the population sums are at most `501M`. This restriction can be chosen uniformly from the previous delta-dependent bounded-ball constants.

At every fixed mesh, the squared finite Frobenius norm of an action update has the exact form `sum_ij c_i c_j <b_i,b_j>_n <h_i,h_j>_n`. Each contraction converges by the supplied fixed-program theorem. The square root is continuous even when the limiting update is zero, and there are finitely many time nodes, so the entire finite sum of update norms converges in probability to its population Euler sum. No growing-transcript assertion, inverse positive lower bound for a velocity norm, or trained operator-norm convergence is involved. Consequently, with probability tending to one, each such finite sum is at most `502M`.

Exact Euler unrolling and the triangle inequality then give both current finite action operator norms at most `10+502M`. First projected and readout norms converge at the finitely many nodes and fit below `sqrt(200)+M+1` after small Euler/finite-width errors. Every one of these bounds lies strictly below `12+600M_delta`. This proves the finite-array source premise on the meshes needed for the limit construction.

Finally `P_delta_new=Theta(delta^-1/8)` and `S_delta_new=Theta(delta^-1/2)`, so `P_delta_new^2 S_delta_new=Theta(delta^-3/4)`. Therefore the explicit affine factor in the old source lemma is now `exp(O(delta^-3/4))`. The complete sufficient selection `min{c_* delta^(7/4), E_*(P_delta_new,S_delta_new)}` is valid relative to the supplied old source theorem. It retains both the explicit nonpolynomial source reciprocal and the unresolved chronological `K exp(KS)` restriction; it does not establish a full polynomial coefficient.

