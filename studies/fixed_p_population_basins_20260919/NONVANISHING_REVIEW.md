# Informed check of the nonvanishing-rate continuation

2026-09-19. Reviewer: `/root/rate_limit_transfer`.

**Verdict: PASS for the new limiting, activation, decay, endpoint, scalar,
and clock-potential arguments, under the stated source assumptions below.**
No correction is required to those arguments. This is an informed scoped
internal check, not an isolated promotion review or an independent audit of
the canonical initialization and established-book identification.

## 1. Input scope, freeze, and coverage

The reviewer first completed and froze its prompt-only independent route,
`NONVANISHING_LIMIT_ROUTE.md`, at SHA-256
`96ddd60c46bf7806fcf2841a52c34b2bb3014106f8fb788bd5d7c7c02267f106`.
Only after that freeze did the supervisor authorize the present informed
check. That independent route remains unchanged.

The following were read completely and checked at these hashes:

| Input | SHA-256 |
|---|---|
| `NONVANISHING_RATE_RESULTS.md` | `9683068ab81102bf09c8bd3b23d357bc8e0011da80c0ddc6c2eb253231882008` |
| `NATURAL_CONDITIONING_FLOW.md` | `0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0` |
| `NATURAL_TANGENT_NOISE.md` | `12272146e901e97014a035ab2a9079d8161c55d0d838fe14c234396ae3ddd0b0` |
| `NONVANISHING_SMALL_FORCE_EXAMPLE.md` | `18ab00ca5d75c1157dd03148c6055751834ab1b40420d18ce3678dd591407357` |
| `NONVANISHING_CLOCK_POTENTIAL.md` | `4a0b013c393938037fba8ee12af07378dee2ae9b39223a685117888435b40fe3` |

Also read and checked the complete Section 3, analytic-Gram lemma, of
`NATURAL_CONTINUOUS_ROUTE.md`, whose full-file hash is
`64cd681fbe3eda3ead3486e8c6437852e434f12e4259fc6f45121fd75d87d216`.
The explicitly supplied read range, lines 72--135, additionally included
the trailing paragraph of Section 2. The rest of that source was not read.
The initially truncated conditioning-source display was repaired by a full
separate read. No scientific source outside the authorized packet was read.
Required math/conjecture skills and process instructions were followed.
No experiments, numerical tests, or candidate edits were made.

## 2. Source assumptions and dependency boundary

The review uses these declared inputs from the supplied sources:

1. The finite-data physical Hilbert closure is exactly the one displayed in
   `NATURAL_CONDITIONING_FLOW.md` Section 1, with bounded marks, `tanh`, actual
   transpose, positive probability weights, compatible merging, unhalved
   loss `L=|e|^2`, and the original population L2/Frobenius metric.
2. The canonical p=1,2 initialization has finite physical norm, `L_0=1`,
   and strictly positive initial feature Gram. The cited initialization
   proofs are outside this packet and were not independently re-read.
3. Original canonical GF exists on every finite physical interval and has
   bounded characteristic coordinates `(w-g,c,M)` in the Banach space used
   by the supplied analytic-Gram lemma. The original model identification,
   canonical bounded initial characteristic coordinates, and cited
   energy/velocity bounds are source inputs, not newly audited book claims.
4. The prescribed finite refresh interval has only finitely many refreshes
   on compact intervals; the readout forcing fields have norm at most one.
   The scalar activation variable has the stated absolutely continuous
   bounded-window law and is independent of the deterministic reference GF.

The supplied proofs of local conditioning-flow regularity, dissipation,
finite travel, singular fitted absorption, noise orthogonality, and the
analytic extension/zero-set argument were all checked, rather than merely
assuming their concluding theorems. The scope restriction leaves the
canonical initialization and external model identification as the explicit
dependencies above. It does not reveal a gap in their previously asserted
validity; it prevents this report from being represented as their fresh audit.

## 3. Transfer, prefactor, and dissipation checks

**Transfer without uniform integrability: PASS.** For any fixed time and
`0<a<L(S^0(t))`, convergence in probability plus continuity makes
`P(L(S_epsilon(t))>=a)` tend to one. The lower expectation bound by `a`
times this probability proves the stated lower semicontinuity. Taking
`a` up to the reference loss is valid; no upper-tail assumption or exchange
of infinite time with vanishing perturbation is used. The deterministic
limit allows the result at every time without an uncountable probabilistic
intersection. The lead's conservative prefactor constant `ell/4` is valid;
the independent route proves the sharper lower bound

\[
\liminf_{\varepsilon\to0}C_\varepsilon
\ge\sup_{t\ge0}e^{\lambda t}L(S^0(t))/L_0.
\]

The deviation bound follows by restricting the expectation to the open
state ball in which loss exceeds `ell/2`; its complementary event has
distance at least the chosen radius, as written. A negative right-hand
side remains a valid, vacuous lower bound. The first-hitting-time statement
uses its expressly assumed continuous nonincreasing loss paths, so a hit
by `T` is equivalent to endpoint loss at most the threshold. A strict
reference loss gap is needed and is stated.

**Sharper conditioning decay and full tangent criterion: PASS.** With
`P=I`, tangent noise has zero pairing with the readout loss gradient.
Writing `h=1+epsilon R`, the safeguard adds `epsilon L[-q]_+` to
loss dissipation, giving exactly

\[
-\dot L=h\|\nabla L\|^2+\varepsilon L[q]_+.
\]

Because `||grad_c L||^2=4e^TKe>=4kL` and `kR>=1`, one has
`kh>=k+epsilon`; integration gives the proposed improved exponent
and integrated-Gram term. No unproved lower bound on the integral is
inserted. With `J=De`, the physical gradient is `2J*e`, so original
GF has `-dot L=4e^TJJ*e`. Its readout block is precisely `A`, and
`JJ*=K` plus positive semidefinite contributions from the other blocks.
The factor four, metric, and weighted residual conventions match.
The accumulated residual-direction criterion is equivalent to the loss
bound on positive-loss portions, with zero-loss absorption treated separately.

## 4. Complete continuation and random activation checks

**Conditioning and tangent-noise dependencies: PASS under the model inputs.**
The finite-dimensional feature expectations have locally Lipschitz first
derivatives in the physical Hilbert variables: bounded `tanh''` controls
the L2 Taylor remainder and the difference of derivative representers.
Finite matrix inversion is locally smooth where `K>0`. The source does
not require an invalid twice-Frechet-differentiable L2 Nemytskii map.
At a regular zero-loss state, the safeguard is a degree-one residual
function with uniformly controlled angular denominator; its zero extension
is locally Lipschitz. Its product with the readout gradient is therefore
also locally Lipschitz. These checks support the local solution/continuation
argument at every regular restart state, not only at the original state.

The tangent operator annihilates the current readout gradient and has norm
at most one. Since `R` has no readout dependence, it annihilates the readout
potential derivative as well. The noise is a bounded colored ODE forcing;
no stochastic second-order term belongs in the chain rule.

For correction strength `alpha>0` and noise amplitude `nu`, let
`Phi=L(1+alpha R)` and `D=-dot Phi`. The checked estimates give

\[
\|\hbox{deterministic drift}\|\le D/\sqrt{\alpha\Phi},
\qquad
\|\hbox{noise drift}\|\le\nu\sqrt L,
\]

and therefore, from any finite regular restart state `S_A`,

\[
\operatorname{Var}_{[A,\infty)}S
\le2\sqrt{\Phi(S_A)/\alpha}
 +\frac{\nu\sqrt{L(S_A)}}{2\alpha}.
\tag{R1}
\]

The subinterval form of the first bound and the integrable noise tail make
the state Cauchy at a finite maximal endpoint and at infinity. At a finite
singular-Gram endpoint, bounded `Phi` forces continuous limiting loss zero;
the specified absorbing extension is therefore fitted. The possible
downward jump of the auxiliary potential does not create a state jump or
conceal positive loss. Regular endpoints continue by local existence.
These facts establish a finite strong fitted endpoint, not an expectation
bound on the norm of that endpoint.

**Analytic-Gram lemma: PASS under source assumption 3.** A bounded complex
neighborhood of the real characteristic coordinates keeps both activation
arguments in a common pole-free `tanh` strip. The frozen unbounded Gaussian
coordinate is real, so it does not invalidate the strip estimate. Uniform
Taylor bounds yield analytic expectation/Nemytskii operations. Picard
iteration on a sufficiently small complex time disk then gives local
analyticity of the actual GF trajectory by uniqueness. The complex Gram
extension correctly uses bilinear products without conjugation; it agrees
with the real Gram on real time. Analyticity of the determinant and its
nonzero initial value exclude accumulating zeros, including finite endpoints
via the local time extension. Positive semidefiniteness of the real Gram
makes nonzero determinant equivalent to positive definiteness.

**Bounded-window activation: PASS.** For each fixed `epsilon`, its
absolutely continuous activation law assigns zero probability to the
countable exceptional GF times. It is not necessary to claim Gram
positivity at every deterministic time, or on the entire preactivation
interval. The null-event convention continuing GF is compatible with
all stated almost-sure conclusions. The preactivation state is retained
exactly, and the restart includes the alarm and refresh information.

At regular activation, choose `alpha=lambda/4` and `nu=epsilon` in (R1).
The random value `Phi(S_A)` is finite almost surely because `K(S_A)>0`;
its expectation need not be finite. Nevertheless the actual-loss decay
has prefactor `L(S_A)<=L_0`, so conditioning on the activation state is not
needed to obtain a deterministic bound on loss. This is precisely why
no moment of the random inverse Gram is hidden in the expectation estimate.

Before activation the original loss decreases. Afterwards it is at most
`L_0 exp[-lambda(t-A)]`. The deterministic upper bound
`A<=T_epsilon+1/lambda` gives the stated all-time bound
`L_0 min{1,(e/epsilon)exp(-lambda t)}`. Integrating `exp(V)` gives
`e-1` and proves the lead's sharper late expectation estimate. The
fixed-accuracy time estimate follows by solving this upper envelope for
the threshold. It is correctly described as a diverging guarantee, not
a claim that actual training must wait that long.

Finally, `A>=T_epsilon` and `T_epsilon` tends to infinity. Thus for every
fixed physical horizon, all sufficiently small perturbations run exactly
the original GF throughout that horizon, for every activation realization.
This argument requires no regular-Gram comparison on that horizon and
remains valid if it contains isolated Gram zeros. It does not show that
the postactivation force is uniformly small; the fixed correction strength
is explicitly disclosed.

## 5. Scalar and clock-potential checks

**The lead's quartic example: PASS.** For `L=x^4`, original GF is
`x'=-4x^3`. Differentiating `x^{-2}` gives eight; adding `-epsilon x`
gives `z'=8+2epsilon z`. Solving this scalar linear equation reproduces
both displayed loss formulas and the asymptotic exponent `4epsilon`.
The compact-horizon small-parameter limit follows from the elementary
uniform exponential remainder on bounded time intervals. The example is
properly separated from any canonical population claim.

**Uniformly small saturating force: PASS.** In the auxiliary note,
`|epsilon tanh(x/epsilon)|<=epsilon` globally. On `(0,1]`,
`x'>=-(4+1)x`, because `tanh u<=u` for positive `u`; thus the trajectory
cannot reach zero at finite time. It decreases towards zero, since a
positive limiting value would keep the velocity bounded away from zero.
The integrating-factor identity for `q=x^0-x_epsilon` gives `q>=0`, and
then `q'<=epsilon` gives the compact-horizon bound. The logarithmic loss
derivative tends to four, and averaging that derivative proves the stated
late exponent without claiming a common from-start prefactor.

For `0<epsilon<=1`, the ordinary-flow comparison reaches
`x<=epsilon^(1/3)` by `(epsilon^(-2/3)-1)/8`. Between that scale and
`epsilon`, speed is at least `epsilon tanh(1)`, yielding the stated
additional time bound. Below `epsilon`, the proved inequality
`tanh u>=u tanh(1)` gives decay rate `4 tanh(1)` for the quartic loss.
All threshold orders, signs, and prefactors are correct, including
`epsilon=1`. The divergence obstruction follows from the transfer theorem
and the polynomial reference loss. No closure accessibility claim is made.

**Clock potential: PASS.** The declared countdown satisfies `a'=-1`
before activation and `a'=0` afterwards. Consequently
`Psi=e^(lambda a)L` obeys `dot Psi<=-lambda Psi` on both pieces, is
continuous at activation, and stays zero at a fitted absorbing endpoint.
The estimates hold on the probability-one regular activation event.
Its initial value is exactly `(e^V/epsilon)L_0`; hence

\[
\mathbb E L(t)\le
L_0\min\{1,((e-1)/\varepsilon)e^{-\lambda t}\}
\]

for every time. The minimum is justified by taking the two separate upper
bounds, not by interchanging a minimum with expectation. This extends the
lead's late bound without changing the frozen lead statement. The clock
is explicitly part of the restart state and uses only a sampled planned
intervention, so it is not future-trajectory playback. The note correctly
declines to interpret this as a geometry potential of ordinary GF on `S`
alone: the initial countdown factor diverges and records the delayed change
of optimizer.

## 6. Residual limitations

There is no detected defect in the new mathematical continuation. The
remaining substantive issue is exactly the stated open one: a bounded
prefactor and positive uniform exponent would imply the corresponding
ordinary-GF fitting estimate. Neither the delayed construction, the clock
potential, nor either scalar example supplies that missing canonical
dynamical estimate. The review does not extend the conclusions to p=3,
finite width, a diffusion, minibatch noise, computational complexity,
uniform endpoint moments, or a globally small postactivation correction.

The comment that many small rapid random increments *can* accumulate an
order-one effect is a possibility statement, not an averaging theorem;
the transfer argument is correctly conditioned on actual convergence to
the original GF. No noisy effective-limit identification is used by the
proved construction.

This report and the independent route are the only files assigned to and
written by this reviewer. No shared index or candidate file was changed.
