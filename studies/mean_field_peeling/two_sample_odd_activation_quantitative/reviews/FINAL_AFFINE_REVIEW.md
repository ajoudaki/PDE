# Independent final affine and complete-theorem audit

Date: 2026-09-07.

**Verdict: PASS at the exact candidate hashes below.**

This verdict concerns the complete stated two-input theorem with
`0 < e <= c_poly delta^800`, including its numerical input certificate
`B_delta = C_B delta^-2`. It is not a verdict only on the affine comparison
or on an interface lemma. I found no blocking mathematical defect in the
assembled proof. The enormous constants and exponent are sufficient
bounds; no optimality or practical-size claim is established.

The audit was independent. I read the rigorous-math skill, the candidate
contract, the manifest, and all four candidate mathematical files in full.
I inspected the mathematical source proofs listed below directly. I did
not read preliminary, sibling, or historical review/status reports, run
experiments, delegate, change proof files, or commit anything.

## 1. Exact inspected files and source boundary

All four candidate mathematical hashes match `CANDIDATE_HASHES.json`.
They were checked at the beginning and again after the mathematical audit.

| Candidate file | SHA-256 |
|---|---|
| CONTRACT.md | `3dc3192e3ffd98b3489a762a071e45bfaa3d568ad2fc8a3de1d664e781a5bb9b` |
| CANDIDATE_HASHES.json | `ce94f6d9517a00369d363364d5d284b705417d04e1bca5f37e53575da7cdcff8` |
| PROOF.md | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |
| AFFINE_POLYNOMIAL_BOUNDS.md | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` |
| POLYNOMIAL_RESPONSE_LEMMA.md | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` |
| OLD_THRESHOLD_AND_NONAFFINITY.md | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` |

The following paths are relative to `../two_sample_odd_activation_theorem`.
I read all of the named files in full except `L3_LOCAL_COMPLETE_PROOF.md`,
whose generic conditioning, singular-query, feedback, common-action and
adjunction portions, lines 215–731, were inspected. I did not use that
file's specialized arctangent-only local response theorem as a premise.

| Mathematical source | SHA-256 |
|---|---|
| PROOF.md | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| AFFINE_CORE.md | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| SOURCE_AND_LIMIT_BRIDGE.md | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| INITIAL_MOTION_AND_NORMALIZATION.md | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |
| sources/TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| sources/L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| sources/FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |

The new response lemma supersedes the old small-amplitude response
threshold. Its source identities were checked against the displayed
two-sample source equations, and its nonlinear estimates were checked
directly; I did not treat an earlier response-review outcome as evidence.

## 2. Exact raw normalization and affine geometry

The first raw increment norm is `sqrt(d)||dw||_2`. With
`u=(x_1+tau x_2)/2`, `||u||^2/d=v`, and `P_1=w dot u`, an increment parallel
to `u` has squared raw norm `||dP_1||_2^2/v`. Therefore `p=P_1/sqrt(v)` is
an isometric active coordinate. The inactive first-weight directions are
annihilated by the affine objective even away from the symmetric path.
This last fact is needed for the full-radius tube argument, not merely
for the reference ODE.

Substituting `D=sigma C`, `lambda=a^3 sqrt(v)`, and `t=lambda s` in the
original raw equations gives exactly

```
p_dot=A* B* D,  A_dot=B*D tensor p,
B_dot=D tensor Ap,  D_dot=BAp.
```

There is no missing sample factor, gain, or input variance. In particular
`sqrt(delta)/(8 sqrt(2)) <= lambda <= 1`. The independent Gaussian
initialization gives `||p_0||=||A_0p_0||=||B_0A_0p_0||=1`; the population
readout is zero. The finite readout is not reset by using that limit.

The three operator balances are obtained by differentiating bounded
products. Pairing the first and third balances gives
`||B*D||^2 >= c^4` and `||Ap||^2 >= c^2(1+c^2)`, with
`c=||D||` and `||p||^2=1+c^2`. No infinite-dimensional trace is used.
The operator bounds `||B||^2 <=100+c^2` and `||A||^2 <=200+c^2` are valid.

The gradient identity gives `F_dot >=2c^4(1+c^2)` and `(c^2)_dot=2F`.
Differentiating the proposed invariant verifies exactly

```
(F^2 - (2/3)c^6 - (1/2)c^8)_dot
    = 2F [F_dot - 2c^4(1+c^2)] >= 0.
```

Thus `F>=c^4/sqrt(2)`. The radial calculation `D''=JJ*D` gives convexity
of `c`, its initial right slope one, and `c_dot>=1`. These estimates
justify division by `c` after time zero and the change of variable in
the duration and curvature integrals.

At the first hit `F=3/(2lambda)`, the displayed
`M=(3/(sqrt(2)lambda))^(1/4)` bounds `c`. The time before `c=1` is at most
one; afterwards `dt/dc<=sqrt(2)c^-3`. Hence `T<2`, `S<2/lambda`, and
`integral(200+c^2)dt <=401+sqrt(2)log M`. Bounded components and raw
velocities give a strong endpoint, so this argument also proves that
the hit exists rather than presupposing it.

The HS path-length calculation is sound. Before `c=1` the bound 201
is conservative. Afterwards either matrix speed is at most
`c(200+c^2)`, and its integrated contribution is bounded by
`sqrt(2)(200+M)`. Together these are below `500M` for `M>=1`. The raw
first increment and readout obey the stated `3M` and `M` bounds.

## 3. Integrated curvature and the nonlinear radius-one comparison

The Hessian of `lambda <D,BAp>` has six pairs of cross blocks, each
bounded by `lambda R^2`. Its norm in the sum of the four component norms
is at most `3lambda R^2`. Projection from the full first-weight space
to `p` is a contraction, so no inverse-angle cost appears in extending
this to nonsymmetric nearby states.

On a raw radius-one tube, `b=R+1`, and
`b^2 <=(7/6)(200+c^2)` because `R>=sqrt(200)`. Consequently the integrated
coefficient in the comparison is at most `1404+5log M`. The same-state
forcing bound `40 e b^3` applies in the original raw sum norm, including
HS matrix increments, and follows from the three capped gates with
`|D_{a,e,R}(z,q)-aq|<=e|q|`.

Using `b^3<=3600M^3`, `S<=2/lambda`, and
`M^8=9/(2lambda^2)` gives exactly

```
E <=288000 exp(1404) e lambda^-1 M^8
  =1296000 exp(1404) e lambda^-3.
```

Thus the stated `C_0` is correct and the restriction
`e<=lambda^3/(2C_0)` closes the tube with room to spare. This is a
comparison obtained by differentiating only the affine field; it does
not incorrectly assume a cap-independent derivative bound for the
nonlinear Nemytskii map.

The forward expansions have the stated constants `2b` and `3b^2`.
Combining them with `M^2<1.5lambda^-1/2` justifies
`C_z=1500C_0` and exponent `lambda^-7/2`. The scalar comparison retains
the affine coefficient `lambda`, giving
`C_g=14400C_0` and exponent `lambda^-11/4`. The conversion to the
common sufficient restriction `e<=c_*delta^(7/4)` is correct.

## 4. Absolute variance and regression margins

Radial coercivity gives `||BAp||>=1`, and hence
`||Ap||^2 >=max(c^2(1+c^2),(100+c^2)^-1)>=1/101`.
The inactive-field identities used here are genuinely proved in the
source: conditional independence of the initial inactive Gaussian root
and bounded learned Frobenius increments makes its learned action
vanish in the population limit. The source also proves zero
active/inactive covariance and Gaussianity of the affine fields.
Bounded arbitrary operators alone would not suffice for these facts.

Therefore the actual three affine marginal variances are at least
`1`, `1/404`, and `1/16`. The replacement of the old
`delta`-dependent variance floor by an absolute one is valid.

The Hermite formulas and their signs check:

```
h(sigma)=-2 sigma^3 E[G^2/(1+sigma^2 G^2)^2],
h'(sigma)=-2 sigma^2 E[G^4/(1+sigma^2 G^2)^2]<0.
```

Orthogonality to `1,G`, `E H_3^2=6`, and the density lower bound on
`[-1,1]` yield exactly
`eta_*=4*404*exp(-1)/(27*pi*405^4)`.

The regression-transfer improvement is also correct for arbitrary
square-integrable laws, including zero variance. An optimal slope lies
in `[0,1]`; `arctan(z)-beta z` is then 1-Lipschitz. Testing the same
intercept and slope under a coupling and applying Minkowski in both
directions proves the 1-Lipschitz bound for the square root of the
optimal residual. This supplies the nonlinear margin `e^2 eta_*/4`
without an inverse-variance loss.

## 5. Enlarged initialization and the actual affine source certificate

The enlarged-scale argument does not compare the initialized bounded
operators in HS norm. That would be invalid in general. Instead it uses
homogeneity between their respective affine state spaces. The identity
`Theta_beta(t)=beta Theta_1(beta^2 t)` is valid in the primary variables,
while variational perturbations about each reference use HS increments.

With `R_delta^2=200+M_delta^2`, the normalized vector field on component
sizes at most `2R_delta` has sum speed at most `32R_delta^3`. The extension
time `1/(1000R_delta^2)` changes the sum norm by less than `R_delta/2`.
Its added integrated tube Hessian is less than one. Also
`(beta_*^2-1)T<=6(beta_*-1)<1/(1000R_delta^2)` for the displayed beta.
Thus the common enlarged horizon is established. The integrated
propagator bound `exp(1410)M_delta^5`, with the stated extra Euler
factor two, has sufficient slack.

I checked the Gaussian-probe mechanism against Sections 5–7 of the
attached baseline. The probe is inserted after a named matrix answer;
its first effect on a later relevant output passes through an update
with its factor `h_j`. The four answer costs are bounded by `3b`, and
the four output costs by `2b`. The raw deterministic comparison therefore
gives the asserted `6b^2 G h_j` one-entry bound. The independent Gaussian
root identity measures the frozen formal derivative even at singular
source covariance. Taking width first at fixed probe amplitude, then
the amplitude to zero, avoids interchanging a width limit with an
unproved derivative. The common generated-space version used by the
candidate is valid by the same fixed-program identity.

At initialization variance `beta^2`, every initialized-matrix return
is multiplied by `beta^2`. This follows directly by rescaling the
conditional Gaussian matrix law; it is distinct from the learned
rank-one term, which has its original raw-update normalization.
No beta derivative of a covariance square root is needed.

The finite-array premise is also justified independently of trained
operator-norm convergence. At a fixed sufficiently fine mesh, squared
HS update norms are finite sums of empirical contractions. These
converge, and their finite time sums approximate the population
path-length integrals. Exact rank-one unrolling then bounds each
trained operator by its initialized bound plus at most `502M_delta`.
The first projections and readout converge at the finitely many nodes.
The displayed `P_delta=12+600M_delta` has adequate slack. The enlarged
reference extension and its almost-unit scaling fit in this slack as
well. None of these claims requires probability control for a growing
transcript.

## 6. The numerical envelope B_delta and the exponent 800

The interface contains actual response arrays and learned moments,
not merely primal norms. Its powers are as follows:

| Input | Verified power of delta^-1 |
|---|---:|
| duration | 1/2 |
| active variance reciprocal | 1 |
| reciprocal enlargement size | 1/4 |
| primary/forward/backward L2 sizes and source Gaussian standard deviations | at most 3/8 |
| forward strict coefficient density | 7/8 |
| backward coefficient row norm | 11/8 |
| raw discrepancy divided by e | 3/2 |
| preactivation discrepancy divided by e | 7/4 |
| a learned-moment coefficient discrepancy divided by e h_j | 15/8 |

Indeed `b_delta^2 G_delta` has power `1/4+5/8=7/8`, while
`b_delta^4` has power `1/2`. Summing a backward row adds duration
power `1/2`. For moments the largest term is
`b_delta^3 E/e`, of power `3/8+3/2=15/8`; the term `b_delta^4` is
smaller. The source lemma separately pays `S B e<=B^2 e` for the
backward moment row. It does not assume that `15/8` bounds that whole
row, whose direct exponent can exceed two.

For the numerical coefficients, put
`K=1+C_0+C_z+C_g+exp(1410)`. Then `C_B=10^30 K^4` dominates all the
displayed constants. In checking a backward row, the density coefficient
must additionally be multiplied by `S_delta<23delta^-1/2`; an
orthonormal sample-basis change can introduce another universal factor.
For example even twice 23 times

```
100*200^2*3^5 exp(1410) + 100*200^4
```

is far below `10^30K^4`. Similarly the moment-comparison coefficient
`40*200^3*C_0*(8sqrt(2))^3+40*200^4`, with fixed mesh/basis margins,
is below `C_B`. The reciprocal-beta coefficient is at most
`10^5(200+9)`, and even the conservative forward/backward Gaussian
standard-deviation bound `8b_delta^3` is far below `C_B`.
The preactivation factor `(8sqrt(2))^(7/2)` is absorbed as well.

Thus the row-duration and sample-basis factors implicit in the prose
do not invalidate the proposed fully numerical envelope. Every required
individual input is bounded by `C_B delta^-2`. It would be clearer to
display the extra row-duration coefficient beside the probe-density
coefficient, but no change of the final `C_B` is needed.

The source threshold is exactly `10^-70 B^-400`. Substituting the
certified envelope gives `10^-70 C_B^-400 delta^800`; taking the minimum
with `c_*` and `1/4` proves the stated universal coefficient. Since
`delta^800<=delta^(7/4)` on the prescribed range, the comparison and
nonaffinity restrictions are simultaneously met. The coefficient
depends on delta alone.

As an independent scalar-arithmetic check of the practical calibration,
I factored `C_g` from the sum defining `K` and evaluated its logarithm
with high-precision decimal arithmetic. This is evaluation of the fixed
displayed constants, not a trajectory experiment. It gives

```
log10(C_B) = 2510.253928159128260394...
log10(10^-70 C_B^-400) = -1004171.571263651304158...
log10(c_*) = -627.818889722891813...
```

Therefore the source prefactor is indeed the minimum in (17), by an
enormous margin, and
`log10(theta_delta) = -1004171.571263651304158... + 800 log10(delta)`.
The theorem improves the asymptotic form of the sufficient coefficient
as delta decreases; the displayed numerical witness is extraordinarily
small and supplies no practically sizable mixing coefficient.

## 7. Check of the complete source closure

The affine source equations in the candidate agree with the original
two-sample formulas after inserting the constant gate `a`. In particular
the bottom strict transfer is `(I-a^2 H_P B2)^-1 a^2 H_P`, the middle
transfer is `(I-a^2 A2 B3)^-1 a^2 A2`, and the top backward transfer is
`K3(I-A3K3)^-1`. Their four variations give the displayed coupled
Jacobian, including both action orientations.

The backward-forcing shift is an exact substitution. Subtracting
`J3` from `Y3` and `a^2 L J3 R+J2` from `Y2` leaves the two strict
forcings `E2+F J2 F+a^2 F L J3 R F` and `E3+V J3 V`.
The strict/row/strict sandwich estimate retains `h_j` for arbitrary
positive meshes, so diagonal backward forcing does not require a
smallest-step bound.

The sample-sector reduction is valid. Affine forward arrays are
diagonal in the active/inactive basis, while the backward arrays have
only their active-active block. Consequently only that sector has
feedback in the Jacobian. The mixed and inactive systems are acyclic.

The positive-scaling inverse argument is mathematically substantive
and closes the previous response gap. In active normalized finite
coordinates, Euler updates have positive polynomial coefficients in
the independent initialized Gaussian entries. Wick contractions of
their products are nonnegative. This proves nonnegative coefficients
in beta for the learned active moments; the causal source recursions
then prove the same for the response coefficients. It is not a claim
that individual Gaussian weights or realizations are nonnegative.

Differentiating the scaled coefficient equations supplies positive
forcing `2F+M_A2'`, `2V+M_A3'`, `2T+M_B3'`, `2W+M_B2'`.
The strict lower bound `h_j/(8B)` follows from `a>=1/2` and `v>=1/B`.
For a nonnegative-coefficient polynomial,
`f'(1)<=f(beta_*)/(beta_*-1)`, so the actual derivative has mixed norm
at most `B^2`. Positivity of the finite chronological inverse then
dominates arbitrary active strict forcing. Combining the backward
shift and other sectors is consistent with the conservative
`10^6 B^20` bound. This does not identify a raw tangent propagator
with the coupled coefficient inverse without proof.

The same-array neighborhood uses exact resolvent identities. In
particular expanding `R(dA2)L` into identities and strict products is
necessary for its density estimate; a general right multiplication
by a causal row matrix would not suffice. The candidate performs this
expansion, retains current diagonals, and uses a polynomial Neumann
neighborhood. Its `10^20 B^100 D^2` remainder is more conservative
than the displayed first- and second-variation products.

Source moments follow by applying those inverses before estimating
the nonlinear values. The defects are bounded by `e pi/2` and
`e|q|`, so the resulting `Lp` self terms can be absorbed without
an unperturbed Volterra exponential. The stated `Rstar=10^4 B^20`
dominates the explicit finite-depth products.

For formal derivatives, covariance parameters, controls, and
coefficients are correctly frozen. Once the affine inverse is
applied, every unknown derivative feedback has a factor `e` or
`e Q_r` and passes through a strict transfer. The transpose injection
retains `h_j`; a full forward row uses total row norm rather than an
incorrect per-entry step bound. The current backward endpoint factor
`1+eQ_k` is retained. Weighted Jensen followed by Gaussian exponential
moments controls the envelope involving `e sum h_r Q_r`, without a
random supremum over source times. The polynomial smallness controls
the needed fixed moments and both endpoint factors.

The resulting defect `10^30 B^200 e` is consistent with the explicit
products of `Lstar=10^8B^50`, `Rstar`, duration, and coefficient rows.
The homotopy inequality is therefore

```
D <=2*10^36 B^220 e +10^26 B^120 D^2.
```

At `d0=(4*10^26 B^120)^-1`, the quadratic term is `d0/4` and the
linear term under the claimed threshold is smaller than `d0/4`.
The ratio quoted in the candidate, `3.2*10^-7 B^-60`, is correct.
Also `e Lstar S Rstar<=10^-58 B^-329`. Continuity in the finite
amplitude homotopy precludes an exit. This supplies actual cap- and
mesh-uniform incoming-field tails, not only a polynomial component
bound or a conditional source input.

## 8. Complete theorem, limits, and observables

The remaining bridges use the established bounded primal feature
interval, incoming Gaussian L2 tails, and prediction endpoint margin.
They impose no old exponentially small response threshold after those
premises are supplied.

The asymmetric cap estimate has one linear factor in the cap on a
forward discrepancy, while incoming backward errors have bounded
coefficients. Its Gaussian-tail term defeats
`exp(C(1+eR)S)`. This gives strong cap removal including raw directions,
an autonomous uncut C1 path, and uniqueness against bounded-primal
competitors needing no tails of their own. Restart follows by starting
the same estimate at a reached state.

Odd label folding is exact in the finite raw model. Population
sample-exchange symmetry follows from deterministic limiting
contractions before uncut uniqueness is used. The scalar clock is
therefore justified for the constructed population paths. The endpoint
above one supplies a first hit and a divergent physical clock using
only a bounded derivative, including for capped paths. For the uncut
path the gradient/radial identities additionally apply. This preserves
the old global physical conclusions, including its stated loss decay.

The finite comparison retains both actual residuals. Fixed-program
convergence is used only at fixed cap and fixed auxiliary mesh, with
rank-one unrolling supplying finite operator bounds. Deterministic
Euler estimates then remove that mesh, and the asymmetric comparison
removes the cap. For simultaneous raw GD the additional error is
`C_{R,T}n^-2`; no growing-transcript Gaussian theorem or finite scalar
clock is used. The small initialized random readout is retained.

I inspected the full fixed-cap velocity bridge. Its appended product
queries are first smoothly truncated, their response coefficients and
both forward action calls are retained, and truncations are removed
in L2. The deterministic hidden-velocity comparison truncates a
reference preactivation-velocity factor. For cap removal the uncut
velocity has a compact continuous L2 time image, giving uniform tails;
the order is cap to infinity at fixed velocity truncation, then
truncation to infinity. This avoids a claim about cap-dependent fourth
moments growing slowly. The finite limits take width first at each
fixed cap and truncation.

The resulting same-layer joint velocity laws, second moments and
integrated squared speeds give the stated path-space W2 limits via
the observation-grid interpolation estimate. L2 contractions give
all four raw kernels including off-diagonal entries. The canonical
common-action construction retains both matrix orientations and their
actual adjoints on generated probes. No cross-layer neuron pairing or
cross-width operator-norm convergence is silently added.

Finally the old odd-family initial-motion proof uses full covariance
of both reused transpose queries, nonconstant `phi'` for every `e>0`,
and sample symmetry. Its strict Gram and acceleration arguments need
no additional amplitude threshold. The quantitative nonaffinity margin
above passes through strong limits and the physical clock. Both the
convex mixture and the normalized identity-perturbation family lie in
the certified gain/amplitude rectangle.

## 9. Nonblocking clarifications

1. References to all primal quantities being bounded by `R` or `b_delta`
   should be read as the primary projected/operator/readout quantities.
   Forward and backward fields can require powers up to the third;
   the input table and all substantive estimates use those powers.
2. The numerical check for backward rows should display the extra
   duration coefficient as well as the density coefficient. As verified
   above, the proposed `C_B` already absorbs it and the basis factors.
3. The component notes retain descriptions of the source step as a
   remaining limitation. Those statements delimit those component
   results; the assembled proof supplies a separate response argument.
   They should not be interpreted as an additional premise or as proof
   of the full theorem by themselves.

None of these points requires weakening the theorem, changing its
exponent, or changing its stated universal constant. The exact candidate
supports the complete polynomial sufficient coefficient claim.
