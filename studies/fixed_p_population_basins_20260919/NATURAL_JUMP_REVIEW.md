# Internal isolated review of the two natural jump routes

2026-09-19. **PASS for the explicitly specified hybrid processes.** No
blocking mathematical error was found. One minor regularity wording change
was requested below and has been closed in Section 7. This is an internal mathematical check, not promotion,
and it does not establish a result for original gradient flow, ordinary
Brownian noise, or ordinary small accepted Poisson kicks.

The rare-refresh route proves its physical-time rates at p=1,2,3; its
auxiliary-search variant also proves finite expected total parameter
variation and a strong zero-loss endpoint. The readout-only deadline route
proves its unconditional canonical conclusions at p=1,2, with almost-sure
finite total variation, continuous hidden paths, and rare-activation
compact-time convergence to original GF. Its singular proposal clock and
Gram inverse are essential parts of this verdict.

## 1. Frozen scope and independence

The complete reviewed candidates, whose hashes matched before and after
the scientific audit, are:

| File | SHA-256 |
|---|---|
| NATURAL_RARE_ROUTE.md | `594a4da44b0ad96ea6fe5e94a1ba36bec47c0a4c8d28c087eeaec461af6e57ef` |
| NATURAL_CONTINUOUS_ROUTE.md | `c7871163b65ead30324427350b1ef87cdba0d94bdec9d45e3064f0ef8a1c8be5` |

The following permitted scientific dependencies were read completely:

| File | SHA-256 |
|---|---|
| RATE_RESTART_ROUTE.md | `6a2c8b8d4e962962685e98175a7332d292c7e7676ffc19b622093a0f3c15b923` |
| NOISE_GLOBAL_PROGRESS.md | `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288` |
| ESCAPE_AND_LIMITS.md | `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2` |
| RATE_ADAPTED_READOUT.md | `1e1ad47811a41d9f09d625746c7b4bc6f95857a1a08521a80b4c80bf9dfb610b` |
| RATE_SMALL_READOUT_NOISE.md | `98449a65152741f0880371828d91e16e0edeb61781b1c64158a661b3bcf9ee35` |
| INITIAL_EXCLUSION.md | `34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c` |
| INITIAL_REVIEW.md | `6fd58a9faa1b07a0eaa53fe9595b63180b225e72df35a7f50fe9f6e629d64baf` |
| RATE_EXISTING_RULE.md | `1632f66b461f492468aa91d07b564694e1f146ca35187e37bd6862ef3e0c1c50` |

Established inputs were exactly the complete assigned spans 13161–13786
and 15146–15528 of `docs/global_nonlinear.md`, plus `docs/NOTATION.md`.
Required process reading comprised the rigorous-math skill and the
conjecture-investigation skill with its adversarial-audit reference. The
supervisor's isolated-review scope replaced author startup reading. No
study README, other study, other current route, other current review,
chat, Git history, or agent-list output was read. No experiments or
numerical calculations were run, and the candidate files were not edited.

The assigned `INITIAL_REVIEW.md` necessarily exposes a previous verdict:
its Section 6 supplies the order-one extension. That exposure is disclosed;
this review is independent of the current candidates' authors and current
reviews, but is not wholly blind to earlier dependency verdicts. The
initialization algebra was checked directly against the assigned book
spans rather than accepted because of that verdict.

## 2. Common model and initialization checks

Both routes use the correct residual, unhalved probability-weighted loss,
actual transpose, fixed joint mark laws, and population/Frobenius metric.
Their factor two in F and identity L'=-||F||² are consistent with
(H3.N2), (H3.CS3), and (H40.C6)–(H40.C9). Merging compatible duplicate
and antipodal observations preserves the whole loss, hence its gradient.

The extension in ESCAPE_AND_LIMITS.md to all finite Hilbert states is
valid. Bounded dictionaries make a_i locally Lipschitz in w and z_i
locally Lipschitz into L-infinity. The readout pairings are locally
Lipschitz in L2; the lower tanh derivative is Lipschitz in L2 and is
multiplied only by a bounded backward coefficient. These estimates give
a vector field bounded and Lipschitz on Hilbert balls. The displayed
successive bounds on c, M, and w prevent finite-time escape. This does
not require a false C2 assertion for the loss on the entire L2 space.

At p=1,2, the initialized feature-independence dependency is sound. The
active odd lists agree, while each order retains its own positive ridge.
The raw contraction includes the reverse-response term tau beta. In the
notation of INITIAL_EXCLUSION.md, its estimate
Delta(ell+alpha r b(h)) >= alpha v tau beta(2b_*-b^*) > 0
holds for every positive ridge. Consequently F is strictly increasing,
the vectors (F(u_1),F(u_2)) identify only equal or antipodal inputs, and
the analytic ridge-function argument proves finite-set independence.
Positive masses therefore make the weighted readout Gram positive
definite. Nothing in this argument proves the analogous p=3 assertion.

## 3. Rare-refresh route

The sign-direction construction is valid even for nearly coincident
distinct input lines: the requisite equal-sign and opposite-sign arcs
are nonempty. Powers-of-three masses make every signed sum nonzero and
make distinct sign rows different modulo sign. The finite tanh margin
keeps those properties at T_*. The one-variable analytic independence
argument then proves K>0. Constants and the proposal family use geometry
and mark laws only; the fitted readout is used only in the proof.

The Gaussian ball probabilities (10), (13) are correct. In particular,
the all-block estimate is genuinely global relative to S_*: expanding
(M-M_*)a_i+M_*(a_i-a_i^*) leaves the fixed c_* in the feature-error
pairing. It therefore gives the stated A_* without requiring a bound on
the proposed readout or incumbent norms. Poisson thinning/conditioning
gives (11)–(12), including the gamma-function factor in expected loss.
Rejected events and all intervening physical GF time are counted.

For the auxiliary chain, on the stated Gaussian event,

\[
2\sigma g\cdot G+\sigma^2G^TQG
\le-2\sigma\sqrt{\kappa\ell}+4n\Lambda\sigma^2
=-\frac{\kappa\ell}{4n\Lambda}.
\]

The event has probability at least q_0, including n=1. Thus
E V_k <= (1-gamma)^k. The incumbent dominance L(S(t))<=V_(N_t)
holds after every offer and throughout every full-flow segment. Crucially,
the auxiliary chain does not depend on the Poisson event times. Its
Poisson generating function therefore yields exactly
E L(S(t))<=exp(-epsilon gamma t), and integration of the clipped
survival bound gives the hitting-time formulas (19).

Finite-time construction requires no compactness: each bounded interval
has finitely many Poisson events and every candidate has finite Hilbert
norm. The energy identity with jump loss drops is exact. For
a_0=epsilon gamma and 0<beta<a_0 it gives

\[
E\int_0^\infty e^{\beta t}\|F(S(t))\|^2dt
\le\frac{a_0}{a_0-\beta},\qquad
E\int_0^\infty\|F(S(t))\|dt
\le\sqrt{\frac{a_0}{\beta(a_0-\beta)}}.
\]

At beta=a_0/2 this is (21). Candidate distances to the single S_*
are summable in expectation by (9), Jensen, and the geometric auxiliary
loss bound. For accepted incumbent jumps the previous accepted offer,
intervening continuous travel, and S_* give the triangle estimate (23).
This proves (24), including histories with finitely many or no accepted
incumbent offers. Finite total variation yields a strong Hilbert endpoint;
continuity of loss makes it an exact fit. Infinite accepted offers force
that endpoint to be S_*, while finitely many need not.

The compact-time claims also check. Before the first event the trajectories
are identical. The probability, total-variation-of-path-law, and coupled
almost-sure statements follow directly. Path laws may be taken on the
usual cadlag/evaluation sigma-field; the displayed uniform distance is
measurable by taking the supremum over rational times and the endpoint.
For the auxiliary construction all offers lie in a deterministic norm
ball, and total continuous travel through T is at most sqrt(T) by energy.
This verifies its stronger bounded-horizon raw-moment estimate (27).
No corresponding unbounded-norm moment claim is needed for arbitrary
independent global refreshes.

## 4. Readout-only deadline route

### Analyticity and regular activation

The shifted characteristic space (w-g,c,M) in L-infinity is the correct
space for this argument. The canonical trajectory stays in it on every
finite interval: |c'|<=2sqrt(L), and bounded dictionary coefficients give
a finite supremum-norm bound for w' once c and M are bounded. The frozen
unbounded Gaussian g stays real. Small complex perturbations in this
shifted space keep lower preactivations in a common pole-free strip.
Bounded dictionaries and local matrix bounds do the same for upper
preactivations. Uniform strip Cauchy bounds justify the claimed
holomorphic Nemytskii maps, expectations, and products.

The local complex-time Picard construction is valid, and uniqueness
identifies its real restriction with GF. Extending the Gram entries
bilinearly, without complex conjugation, is essential and is done
correctly. Hence det K(t) is real analytic, with det K(0)>0. Its zeros
are isolated and have no accumulation on a compact interval, since the
trajectory has a local analytic extension at each finite endpoint.
An independent absolutely continuous activation time avoids this
countable set almost surely. This proves regular activation, not a
uniform positive lower bound along all of original GF.

### Tube, deadline clock, and nonexplosion

The hidden Gram perturbation estimate and the selected radius imply
K>=kappa I before a hypothetical first exit. The proposal produces
exactly e_trial=e+sqrt(ell)Z. Rotational invariance makes its conditional
acceptance probability the same positive q at every proposal, even
though GF continues between rejections. Accepted jumps have norm at
most (1+sqrt(theta))sqrt(ell)/sqrt(kappa).

The finite-history argument avoids circularity. Stage-start losses are
bounded by theta^j ell_*, so their square roots have sum at most R.
Before any first exit, durations of completed stages are less than h
and the current partial stage has duration at most h. This first bounds
c by Cbar and then bounds all hidden travel by
2Bh Cbar(1+Mbar)R<=rho/2. Thus neither a Gram singularity nor a tube exit
can precede the deadline, including on a history with no success yet.

On a stage the cumulative proposal intensity is
nu log[h/(h-s)]. Conditional rejection probabilities remain 1-q;
conditioning on the scheduled times or successively on the history
therefore gives

\[
P(W>s\mid\text{past, activation constants})=(1-s/h)^{\nu q}.
\]

This is a proper law on (0,h), so success precedes h almost surely and
only finitely many proposals precede it. Until termination, successive
stage durations have this same conditional law and are conditionally iid.
There is no hidden finite-time zero-loss exception: original GF cannot
first reach an equilibrium at finite time by local uniqueness, and an
exact-fit Gaussian proposal has probability zero. Alternatively one can
append fictitious stages after absorption. The probability of W>=h/2 is
the fixed positive number 2^(-nu q); infinitely many such stages force
their sum to diverge. Together with finite proposals per stage this proves
nonexplosion of the actual accepted-and-rejected event process. The
underlying unstopped proposal clock would have infinitely many events at
its deadline, but almost surely no actual stage reaches that deadline.

Summing the accepted-jump bound and the three integrated original
velocity bounds proves finite total variation after activation. The
preactivation interval is finite almost surely and has finite GF travel.
The strong full-state zero-loss endpoint follows. No compactness from a
Hilbert norm bound, or moment bound on the random inverse Gram, is used.

### Rates and cost semantics

At least floor((t-T_epsilon)/h) stages finish by time t. Since h<=1,
the envelope (12) is correct. Integrating it against the independent
exponential activation density gives (13) for its stated range
0<epsilon<a=log(1/theta); its hitting-time estimate (14) is also correct.
The conclusion is unconditional despite random activation constants,
because the final envelope uses h<=1 and ell_*<=1. The theorem does not
need finite moments of those constants.

Each stage uses a geometric(q) number of exact proposals, of mean 1/q.
The rate is measured in continuously running GF time with zero-duration
evaluations. A uniform finite bound on evaluation speed would invalidate
the deterministic stage deadline, and hence this proof. Poor geometry
still enters through the inverse Gram and through the possibly very small
h. The absence of that geometry in the coarse physical-time exponential
envelope must not be reported as affordable computation.

Rare activation gives exact equality with GF before T_epsilon, proving
the stated uniform compact-time probability bound and the coupling
T_epsilon=E/epsilon. No state-moment convergence or all-time closeness
is claimed. Both candidates correctly retain the noncommuting order of
the long-time and epsilon limits.

## 5. Simpler noises and the surviving obstruction

The continuous route's stopped Itô identity (18) is correct: the hidden
variables have finite variation, and predictions are linear in c, so
their only quadratic variation comes from the displayed readout noise.
The full tangent Gram dominates K, and tr(K²)<=1. A uniform positive
Gram bound and the stated continuation/integrability hypotheses would
give the conditional drift estimate; initial positivity alone does not.
The ambient absorbing states (w,0,0), and the larger w=M=0 readout-noise
obstruction, are valid but do not refute the canonical-initialization
claim. The additive-noise observation is local and is correctly not
presented as an invariant-measure theorem.

For ordinary homogeneous Poisson small accepted kicks, finite-time
well-posedness and compact-time small-amplitude convergence hold by the
finite number of proposals and continuous dependence of GF. The Gaussian
event in (20) gives the stated fractional decrease under K>=kappa I.
If that deterministic bound held along the whole path, the resulting
exponential mean loss bound would make both continuous readout travel
and expected jump variation integrable; successive c, M, w bounds would
give the strong endpoint as claimed. The missing all-time Gram lemma
remains missing. Unbounded homogeneous waiting times invalidate reuse
of the deterministic h-per-success tube argument.

## 6. Hostile checks and one minor correction

| Target | Strongest obstruction and discriminator | Result and consequence |
|---|---|---|
| Rare physical-time exponential rate | Auxiliary chain might depend on the event clock or fail to dominate incumbent loss | It is clock-independent and dominance holds on every segment; rate verified |
| Strong parameter endpoint | Loss decay alone may allow infinite travel or jumps | Weighted energy plus summable candidate distances bounds total variation; endpoint verified |
| Regular late activation | Gram could vanish on a positive-measure set | Analytic determinant with positive initial value rules this out; no uniform coercivity follows |
| Deadline confinement | Success might be assumed before proving invertibility | Finite-history tube applies through every partial stage up to h; circularity excluded |
| Nonexplosion | Singular intensity might accumulate actual proposals in finite time | Proper accepted-stage law and infinitely many long stages exclude this almost surely |
| Small-noise interpretation | Compact-time closeness might be mistaken for small amplitudes or original-GF fitting | Both limits here are rare interventions; simpler all-time noise claims remain open |
| Practical timing | Zero-duration evaluations might conceal cost | They are explicitly disclosed; no finite-computation guarantee is established |

**Minor wording correction:** NATURAL_CONTINUOUS_ROUTE.md lines 11–12
and 365–366 say that the hidden blocks obey the original equations “at
every physical time.” Accepted readout jumps can change F_w and F_M
instantaneously. The hidden paths are continuous and locally absolutely
continuous, and satisfy the original equations almost everywhere, or
equivalently their integral equations at every time. They need not be
classically differentiable at an accepted jump. State this usual hybrid
ODE interpretation explicitly. This does not change any estimate or
endpoint conclusion.

The strongest surviving ordinary explanation is exactly the one the
candidates disclose: an external readout search with proved progress
supplies the global guarantee, while full GF supplies descent. The
rare route can replace all incumbent blocks; the deadline route keeps
hidden paths continuous but controls their total travel by the singular
clock. Neither identifies an intrinsic global-convergence mechanism of
unmodified GF. Subject to that scope, both candidates pass this internal
check; the minor regularity wording is now repaired as recorded below.

## 7. Closure of the hidden-regularity wording repair

The corrected `NATURAL_CONTINUOUS_ROUTE.md` has SHA-256
`64cd681fbe3eda3ead3486e8c6437852e434f12e4259fc6f45121fd75d87d216`.
Its opening bullet now specifies continuous hidden paths, original
equations almost everywhere, and integral equations across readout jumps.
Section 6 explicitly declines a classical hidden derivative at a jump.
These formulations exactly resolve the minor item in Section 6 above.

For an integrity check, reversing only these two disclosed text changes
reconstructed the originally reviewed SHA-256
`c7871163b65ead30324427350b1ef87cdba0d94bdec9d45e3064f0ef8a1c8be5`.
Thus the candidate's scientific definitions, proof, and conclusions are
otherwise unchanged. The PASS applies to this corrected version, with
no outstanding correction required by this review. No new independent
or promotion-level review is claimed by this narrow repair check.
