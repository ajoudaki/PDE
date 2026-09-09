# CLEAN

Fresh isolated adversarial proof audit of `finite_optimization_and_controls.md`.

No required mathematical fixes were found in the finite claims at the input
hashes below. The canonical gradient-flow and exact raw-GD coercivity, fitting,
and finite endpoints are proved under their stated hypotheses. The auxiliary
metric projection has the claimed local regularity, global finite flow, energy
identity, integrated normalized-coordinate L1 defect, and eventual exactness
over the whole physical horizon with the stated cap constant. The Gaussian
event supplies every deterministic hypothesis for sufficiently large widths.

This verdict concerns the stated finite results. It does not certify a
population theorem, a width-uniform stability estimate for the projection,
agreement of the GD and gradient-flow endpoints, or an interchange of limits.

## Required fixes

None.

## Optional improvements

No optional change is needed for proof closure. The initial first-vector RMS
bound in Theorem 4.1 is stronger than its proof needs: the bounded activation
and its bounded derivatives make the GD estimates independent of the initial
first-vector size. Retaining this assumption is harmless and is compatible
with the common Gaussian event.

## Read coverage and isolation

All mathematical input paths are relative to
`/tmp/pde-finite-controls-review.0HXzOf`.

| Input | Semantic read coverage | Role |
| --- | --- | --- |
| `finite_optimization_and_controls.md` | All lines 1–1231, including every proof, constant definition, inequality, and scope statement | Primary audited chapter |
| `NOTATION.md` | All lines 1–98 | Network, norm, residual, initialization, mobility, clock, and scope conventions |
| `finite_dynamics.md` | All lines 1–214 | Independent check of finite derivatives, kernel factors, energy, continuation, and finite-horizon norm bounds |
| `arctan_limits.md` | Lines 688–765 only; canonical model and algorithm are lines 698–743, equations (L3.1)–(L3.3) | Exact canonical-model dependency at `#l3-local` |

The arctangent excerpt includes the adjoining explicit local-interval display
(L3.4), lines 745–762, and the next theorem heading. Neither that interval nor
the population conclusions or their proofs are used in this audit. An anchor
search additionally returned link/anchor matches at lines 49 and 688; it was
used only to locate the referred model. Whole-file hashing and line/byte counts
of `arctan_limits.md` do not represent a full semantic read of that file.

No repository, history, other review, web source, agent, or experiment was
consulted. The required `solve-math-rigorously` workflow instructions were read
separately from `/etc/codex/skills/solve-math-rigorously/SKILL.md`; they supplied
review procedure, not mathematical premises. Only `REVIEW.md` was created; the
four inputs were left unchanged. Repeated full-file hashes matched.

## Canonical model and general finite identities

The primary chapter's lines 19–94 agree with both the notation contract and
the exact referred canonical model: three hidden layers, one input and target
equal to one, activation `arctan`, ordinary middle matrix multiplication,
prediction `(W^(4))^T h^(3)/n`, loss `(f-1)^2`, and block mobilities
`n,1,1,n`. Stored readout variance is `n^(-2)`, hence standard deviation `1/n`.
There is no residual in a backward vector.

Differentiating the prediction gives the displayed `1/n` in each raw block
derivative. Applying the mobilities cancels it only in the first and readout
blocks. Thus the physical multiplier is exactly `-2r`, the middle feature
velocities are `delta h^T/n`, and GD evaluates every block at the same old
state. The weighted parameter norm (1.4) and all four squared-speed terms in
(2.3) have the correct normalizations.

The entirety of `finite_dynamics.md` was also checked. Its general first-layer
derivative has the additional `1/sqrt(d)`; its kernel has the input Gram factor
`x_a^T x_b/d`; the middle kernel has two normalized pairings. For the mean
squared loss, the factors in the prediction equation and dissipation are
respectively `2/m` and `4/m^2`. The equality with
`-||D^(-1/2) theta_dot||^2` is correct. Nonnegative loss and the energy identity
give the stated square-root displacement modulus. At fixed width the positive
mobility metric is equivalent to the Euclidean metric, so a proposed finite
maximal endpoint has a finite limit and can be extended. Bounded first
activation derivatives suffice for the subsequent forward and backward RMS
inductions; no uniform second-derivative bound is silently required there.
The Gaussian initial norm argument and its `2·9^(2n) exp(-nM^2/8)` operator
tail bound are consistent with the complete calculation in the audited chapter.

## Canonical feature flow and gradient flow: §§2–3

Every step in lines 96–325 was checked.

- **Global feature existence, (2.4).** Bounded readout velocity first gives
  readout RMS at most `epsilon+cs`. The third matrix increment then has
  Frobenius norm at most `c epsilon s+c^2 s^2/2`. Integrating the resulting
  second-matrix and first-vector velocity bounds in that order gives the
  displayed finite polynomials. Matrix increment bounds apply in Frobenius
  norm, not merely operator norm. These bounds preclude finite escape at each
  fixed dimension and justify the smooth ODE continuation.
- **Exact acceleration and action, (2.1)–(2.3).** The two contributions to
  `(z^(2))'` give `A_2 delta^(2)`; inserting this in the derivative of
  `W^(3) h^(2)` gives `A_3 delta^(3)`. Hence the readout acceleration is
  `P W^(4)`. The congruence structure proves positivity of all three matrices.
  Expanding `W^(4)^T P W^(4)/n` recovers exactly the three non-readout kernel
  blocks. The rank-one Frobenius identity recovers their squared speeds.
- **Readout norm, (2.5).** On its nonzero intervals, `g'=f/g` and the displayed
  expression for `g''` follow by differentiation. Cauchy–Schwarz makes
  `||h^(3)||^2/n-(g')^2` nonnegative; the remaining term is nonnegative by
  positivity of `P`. No coordinate sign assumption is needed.
- **Zero initial readout.** Smoothness gives `g'(0+)=sqrt(mu)`. Convexity
  propagates this slope and excludes any later zero, which validates its own
  domain of use. It gives all four inequalities in (3.1). If the excluded
  initial top feature is zero as well, every raw velocity is zero, as stated.
- **Small initial readout.** On `[0,1]`, the constants `L_3,L_2` bound their
  respective matrix norms and `B` bounds `||P||`. The definitions imply
  `Bc sigma^2 <= b/8` and `epsilon <= b sigma/16 <= c sigma`. Consequently
  (3.6) gives feature change at most `3b/16`. The normalized readout error at
  `sigma`, including its initial value, is at most
  `b/16+b/12=7b/48`. The elementary directional inequality used in the proof
  therefore gives
  `g'(sigma) >= b-14b/48-3b/16=25b/48 > b/2`.
  The nonzero readout and positive slope then persist. This proves the top
  feature and kernel lower bound `mu=b^2/4` on the full feature half-line.
- **Physical clock and endpoint.** The bound
  `|f_0| <= c epsilon <= c^2/16 < 1` verifies the initial clock sign.
  Strict monotonicity `f'>=mu` gives the unique finite crossing `s_*` and
  `s_* <= e_0/mu`. Uniqueness of the scalar ODE prevents finite physical-time
  arrival at its equilibrium. Boundedness and positivity give global clock
  continuation and convergence to `s_*`. The exact equation
  `e_dot=-2K_n e` gives the factors `2mu` for error and `4mu` for loss in
  (3.4). Integrating clock speed proves its other bound; integrating the
  feature kernel proves `s_*-s <= e/mu`.
- **All four parameter blocks.** Feature action between two times equals the
  prediction increment. Joint weighted Cauchy–Schwarz therefore gives (3.5)
  with total squared displacement `e_0^2/mu`, endpoint distance
  `e/sqrt(mu)`, and the same bound on remaining weighted path length.
  Bounded coordinatewise readout speed also gives the stated `ce_0/mu`
  coordinate displacement. Corollary 3.2 correctly propagates the top feature
  lower bound using `|arctan z|<=|z|`; the third-matrix kernel and
  `||q^(2)|| <= Mhat_3 ||delta^(3)||` give precisely
  `Mhat_3^4 e_0/mu` in the backward-energy bound.

## Exact raw GD: every estimate and constant in §4

Lines 327–633 form a closed discrete proof. In particular, the argument does
not use exact transformed-coordinate Euler or assume a comparison with
gradient flow.

**Bounds on positive-step paths.** Summing readout, third-matrix, and
second-matrix increments in that order proves `Q,R_3,R_2` for any positive-step
path of computational length at most `S=32/b^2`. The bounds remain valid
inside frozen raw segments. Each block increment is at most `V alpha` in its
stated vector RMS or matrix Frobenius norm; `V` is not incorrectly asserted
to bound the combined norm of all four blocks.

**Directional identity and remainders.** Equation (4.9) is the derivative at
the segment's initial state. Along the frozen segment, the inequality
`||w odot w||/sqrt(n) <= sqrt(n)(||w||/sqrt(n))^2` gives the required finite
dimension factor. The second derivative of `z^(2)` has terms
`2(W^(2))'(h^(1))' + W^(2)(h^(1))''`. Adding the activation second derivative
gives the three terms defining `u_2`. The next layer gives
`2 sqrt(n) v_3^2 + 2a_3 v_2 + sqrt(n)R_3 u_2 <= 2B sqrt(n)`.
Integration of the Taylor remainder introduces the correct factor one half,
so the feature remainder is bounded by `B sqrt(n) alpha^2` in RMS.

Multiplication by the exactly updated readout leaves exactly the two scalar
remainder terms in lines 508–509. Their bounds are
`alpha^2 c C_P Q` and `Q B sqrt(n) alpha^2`, giving the specified
`B_f=Q(cC_P+B)`. The kernel upper bound is `K_*=c^2+C_P Q^2`.
No maximum-coordinate estimate for the initial readout is used.

**Regularized readout slope.** With positive `lambda`, the interpolated
readout norm is smooth and convex on each segment. At a knot, the term
`alpha W_j^(4)^T P_j W_j^(4)` is nonnegative. The cross term is bounded using
`||W_j^(4)||/(sqrt(n)g_{j+1}) <= 1+alpha c/lambda <= 2`; the Taylor remainder
contributes at most its RMS. The resulting loss of slope is at most
`D sqrt(n) alpha^2`, with exactly `D=2cC_P+B`.

For nodes up to `2tau`, telescoping gives (4.16): the two error terms are at
most `b/64` each. A first node in `[tau,2tau]` exists whenever needed because
the step bound is at most `tau`. At that node the normalized readout-direction
error is `b/16`, the feature error is `b/32`, and the regularizer contribution
is `b/32`. The numerator in (4.18) is at least
`(463/512) h_*^2`; its positive denominator is at most `(35/32)h_*`.
Thus the slope is at least `(463/560)h_* >= 3b/4`. Summing subsequent slope
losses gives at most `DSA sqrt(n) <= b/4`. Convexity on segments then proves
the nodewise feature RMS bound `b/2`. The terminal-node slope is explicitly
defined algebraically, so no extra step is presumed.

**Width threshold.** Every entry of the maximum in (4.7) enforces the
corresponding condition in (4.6). In particular, with `A=4n^(-2)`, the
dimension-dependent conditions reduce exactly to

```
n^(3/2) >= 512 B tau/b,
n^(3/2) >= 16 D S/b,
n^(3/2) >= 32 B_f/b^2,
n^(3/2) >= 4 B_f.
```

The other conditions give the three stated square-root bounds and
`n >= 2 sqrt(K_*+1)`. All quantities in denominators are positive; all
constants depend only on `M,b` because `c=pi/2` is fixed.

**Induction, fitting, and endpoint.** Initial prediction lies in `[-1/2,1/2]`.
The inductive clock bound gives `s_k <= 8e_0/b^2 <= S/2`; the next positive
step has `alpha_k <= A` and stays within computational length `S`.
Consequently the already proved positive-step estimates apply to the extended
prefix without assuming its new prediction. They give

```
(b^2/8) alpha_k <= f_(k+1)-f_k <= (K_*+1) alpha_k <= e_k/2.
```

This proves strict increase, absence of overshoot, and the next clock bound,
closing the induction. Substitution of `alpha_k=2 eta_n e_k` gives the stated
contraction factor `1-eta_n b^2/4`, which is strictly between zero and one.
The error and loss exponential rates in physical node time are respectively
`b^2/4` and `b^2/2`. Summing the lower increment bound gives
`sum_(j>=k) alpha_j <= 8e_k/b^2`. The four block tails are therefore bounded
by `8V e_k/b^2`, proving convergence to a finite raw state whose prediction
is one by continuity. The interpolated raw path has the same endpoint.
These are all-iteration estimates; no finite physical-time truncation enters.

## Metric projection and global auxiliary flow: §§5–6

Every assertion in lines 635–949 was checked, including the order of the
noncollapse and continuation arguments.

The projected vector is the full `delta^(2)`, in the positive definite metric
`M=c_1 I+W^(2)D_1^2(W^(2))^T`. The box is nonempty and compact; strict
convexity gives a unique minimizer. Its variational inequality with competitor
zero gives `delta^T M u >= u^T M u`; Cauchy–Schwarz in this metric gives
`u^T M u <= delta^T M delta`, treating `u=0` separately.

For two projections, adding their variational inequalities and expanding the
matrix difference gives exactly (5.7). On a bounded neighborhood with a
positive common lower eigenvalue, its last factor is bounded by the fixed
box bound plus the bound on the projected vector. Composition with the smooth
network maps proves local Lipschitz continuity at fixed `n,R`. No derivative
of an active set or projection map is assumed. The two changed parameter
blocks contribute `delta^T M u/n` to `f'` and `u^T M u/n` to their joint
squared speed. Thus (5.6), including the nonnegative excess work, is exact.

Bounded coordinatewise readout speed gives `B(S)=1+cS`, which controls both
readout and third backward-vector RMS. The third-matrix increment is bounded
by `cB(S)S` in Frobenius norm as well as operator norm. The prediction bound
and `f_0>=-c` give total squared-speed integral at most
`D(S)=cB(S)+c`. Cauchy–Schwarz gives (6.4), without needing a prior estimate
on the projection size. Product differences and the activation's Lipschitz
constant give each term and coefficient in (6.5).

The definition of `a` makes the two initial feature RMS changes at most one
quarter of their assumed lower bounds. Squaring actually gives the stronger
factor `9/16`; the displayed `1/4` is valid. Compactness with this positive
`c_1` rules out an endpoint at or before `a`. The width condition gives
`2c/n <= beta_3 a/8`, so
`f(a) >= -2c/n+beta_3 a/4 >= f_*>0`.
For later feature times, monotonicity and the two forward matrix bounds imply
`sqrt(c_1) >= f_*/(B(S)A_3(S)A_2(S))`. This proves (6.7) before using it for
global continuation. Its denominators are positive for `S>0`, even in the
formally allowed case `M_0=0`.

The projection inequality then gives (6.8) with the stated square-root
condition factor. The four parameter speed bounds and all three differentiated
field bounds (6.9) have the correct normalizations. In particular,
`((W^(3))')^T delta^(3)` has RMS at most `cB^2`, while differentiating
`delta^(3)` gives RMS at most `c+2B ||(z^(3))'||/sqrt(n)`. This checks the
coefficient `2B` and uses the available coordinatewise readout bound, not an
invalid product-of-RMS inequality. All these finite-feature-horizon constants
are independent of cap and width under the stated uniform initial hypotheses.

Finally, `v'=2f` for `v=||W^(4)||^2/n`, and `f'>=f^2/v` whenever `v>0`.
After `a`, positivity of `f` ensures `v>0` and makes
`(f^2/v)'=(2f/v)(f'-f^2/v)` nonnegative. Its value at `a` is at least
`k=f_*^2/B(1)^2`. Together with the early top-feature bound this proves the
global feature derivative bound `mu_aux=min(beta_3/4,k)`. The first crossing
of one is unique and no later than `S_dagger=a+1/k`, including the case that
it occurs before `a`. The clock, fitting rates, and finite endpoint follow
with the same checked time factors as in the canonical flow. Remaining
weighted squared-speed integral is at most `e(t)`, giving (6.12) with
`e(t)/sqrt(mu_aux)` and total squared displacement at most `S_dagger e_0`.

## Defect topology and whole-horizon exactness: §7

At an upper box face, the allowed negative coordinate variation gives
`e_(R,i)>=0`; at a lower face it gives `e_(R,i)<=0`; in the interior it gives
zero. Symmetry of the metric consequently gives the exact identity

```
(delta^(2)-u_R)^T M u_R/n = u_R^T e_R/n = (R/n) sum_i |e_(R,i)|.
```

Integrating the energy identity proves `D(S)/R` with normalized counting
measure. It proves the bounded measurable test and `C^1` chain-rule versions
as stated. These compare the auxiliary derivative to the canonical equation
evaluated at the same auxiliary state. They do not compare two trajectories.
The support bound `nU(S)^2/R^2` follows from saturation and does not provide
the missing squared-norm control. The chapter correctly refrains from an RMS,
unbounded-test, kernel, or population conclusion.

In physical time the defect is multiplied by the positive clock speed
`2(1-f)`. The substitution `ds=2(1-f)dt` removes exactly this factor from the
integral. Since `s(t)<s_dagger<=S_dagger`, the bound is `D(S_dagger)/R` for
every finite physical horizon and, by monotone convergence of nonnegative
integrals, on the entire physical half-line.

For eventual exactness, the cap-independent auxiliary bounds give
`||delta^(2)||_infinity <= ||delta^(2)||_2 <= sqrt(n) A_3(S)B(S)` at every
state in `[0,S]`. Thus a cap at least `C(S)sqrt(n)` with the stated
`C(S)=A_3(S)B(S)` makes `delta^(2)` itself feasible. Its objective value is
zero and positive definiteness makes it the unique minimizer, including at
equality with the cap. The auxiliary equations become the canonical feature
equations along the entire interval; finite uniqueness identifies their paths.
Taking `S=S_dagger` identifies both clocks and endpoints over all physical
time. No width-independent cap, constant-one cap, stability limit, or
projected-GD argument is needed or asserted.

## Gaussian event and source closure: §§8–9

The initialization calculation uses only the stated independent Gaussian
blocks. Positivity and boundedness of `nu_1,nu_2,nu_3` hold because nondegenerate
normals are nonzero almost surely and `arctan` vanishes only at zero. The first
activation average has variance at most `c^4/n`. Conditional on the previous
activation vector, each next layer consists of independent centered normal
coordinates with variance equal to that vector's squared RMS. Conditional
Chebyshev and continuity of `Psi`, justified by bounded convergence, propagate
the second-moment limits through both middle matrices. Only initialization
independence is used.

The sphere net has at most `9^n` points; its two-vector approximation error
is at most half the operator norm. Each net form has variance `1/n`, so the
Gaussian exponential bound gives exactly (8.5). Its exponent decays at
`M=10`. Integration by parts gives Gaussian second and fourth moments one and
three, so the first-vector and rescaled-readout squared-norm averages have
variance `2/n`. Their stated thresholds hold with probability tending to one.
The coordinatewise readout failure probability is at most
`2n exp(-n^2/2)`. A finite union bound proves the full event (8.3); independence
of the final constituent events is unnecessary.

On that event, the deterministic substitutions are exact:

| Conclusion | Parameters and factors checked |
| --- | --- |
| Canonical GF | `M_2=M_3=10`, `b=sqrt(nu_3)/2`, `mu=b^2/4=nu_3/16` |
| Exact GD | `M=10`, the same `b`, contraction `1-eta_n nu_3/16`, clock tail `32e_k/nu_3` |
| Auxiliary family | `M_0=10`, `beta_1=nu_1/2`, `beta_3=nu_3/2`, plus both readout bounds and first-vector RMS at most two |

The maximum (8.4) enforces `n>=N`, `2/n<=epsilon_GF`,
`2/n<=epsilon_GD`, `n>=16c/(beta_3 a)`, and the strict condition `n>2c`.
Its integer rounding is correct. The event's top-feature lower bound is
stronger than the `b` used in GF and GD. The event's first-vector bound is
stronger than the GD bound. Hence no initialization hypothesis is missing.
At each sufficiently large deterministic width, all indicated times and all
caps are covered by deterministic implications of this one event; there is
no uncountable probabilistic union or assertion of an unstated coupling
across widths.

The dependency list in §9 matches the actual proofs. The canonical model is
the only mathematical import from `arctan_limits.md`; its local population
theorem and proofs are not needed. The new chapter supplies the finite
acceleration, discrete error control, projection regularity and energy,
continuation, physical clocks, endpoints, and Gaussian calculations used by
its conclusions. No unresolved source-dependent finite lemma remains.

## Exact hash manifest

SHA-256 of the complete, unmodified input bytes:

```text
a12a4f2541dd989a01920541f07ce8f80058b88d3e19db65c4b376c1fcf6653e  finite_optimization_and_controls.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  NOTATION.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  finite_dynamics.md
19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  arctan_limits.md
```

| Input | Lines | Bytes |
| --- | ---: | ---: |
| `finite_optimization_and_controls.md` | 1231 | 48237 |
| `NOTATION.md` | 98 | 5110 |
| `finite_dynamics.md` | 214 | 8355 |
| `arctan_limits.md` | 3117 | 143086 |

SHA-256 of the exact arctangent excerpt, lines 688–765 inclusive, retaining
the source newlines and without line-number prefixes:

```text
0e534b03dbf994cc9590e0d83ac5c9c93954ae8add63ac847f87c7bafe0aeddc
```
