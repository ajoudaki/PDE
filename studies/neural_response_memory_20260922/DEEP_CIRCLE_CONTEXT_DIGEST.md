# Context and correction audit for the three-hidden-layer circle extension

Date: 2026-09-24. Author: scoped theory agent `/root/deep_derivation`.
This is a read-and-derive internal context audit, not an independent review,
a fresh implementation audit, a numerical reproduction, or promotion.

The complete assigned progression and correction reports support the equations
in `DEEP_CIRCLE_DERIVATION.md`. No change to its dense dynamics, two moment
operators, response lift, initialization, or two defect formulas is needed.
The main consequences concern the description of the implementation, what
must be tested, and the strength of the conclusion. In particular, direct
tanh evaluation implements a closure with an exact rational lift; it is not
itself an evaluation of a rational right-hand side. Small-order agreement
and an implementation PASS do not establish numerical resolution or a
monotone approximation hierarchy.

## 1. What changed across the mathematical progression

`RESPONSE_STATE_SYNTHESIS.md` separates evolving memory from a Taylor
polynomial. A finite autonomous state can saturate or retain a plateau, and
zero radius of a population time-Taylor series does not rule out simple
per-neuron dynamics. Neither observation proves an efficient neural closure.
Its exact moving-response ladder exposes the missing actions on changing
forward and backward probes. This motivates retaining history information,
while leaving its finite closure open. Its earlier requirement to avoid the
original dense operator is subsequently narrowed by the user's express
permission to retain initialized mixing.

`COUPLED_CURRENT_STATE_SYNTHESIS.md` records that correction: the complete
collective configuration is the state, and actual W0/W0-transpose actions are
permitted. Individual neurons need not evolve autonomously. It distinguishes
receiver-dependent initialized fields, learned operator actions, and shared
scalar averages. Reusing the same initialized matrix induces correlations
that cannot be replaced by fresh Gaussian actions or by their zero means.
The universal reconstruction derivative must include every aggregate and
receiving-field dependency. A path-conditioned kernel can already contain
the environment derivative inside its time derivative; adding that term
again would double count it.

For the deep extension, the two actual initialized matrices and both actual
transposes are retained. The chain rule differentiates each current moment
pair and its shared denominator L, so the environmental dependence is not
dropped. A2 and B3 occupy the same neuron layer but encode different responses
and remain separate. The construction imposes a rank bound through its
explicit history projection; it does not infer low rank from collective
autonomy alone.

`SELF_CONSISTENCY_CRITERIA.md` makes exact closure a condition on all reachable
retained states: equal retained configurations must have equal induced
velocities. Instantaneous common-operator identities and scalar moment
balances are weaker tests. Source linear relations and mixed forward/reverse
pairings must be respected, including nearly null source directions in
limiting formulations. Matching Gaussian mean-square initial defects is a
local certificate; matching means alone permits cancellation. All initial
jets still do not determine a merely smooth nonanalytic trajectory.

The two factor reconstructions in the deep extension provide common matrices
for all their forward and transpose queries, hence their instantaneous source
relations and pairings hold automatically. This is a structural consistency
property of the candidate. Its generally nonzero positive-time E2 and E3
remain the failure of exact canonical motion, so those structural identities
must not be presented as a proof of exact reduced dynamics.

`AUTONOMOUS_CLOSURE_CERTIFICATES.md` isolates one reconstruction defect and
separates its production from propagation. Its exactness criterion is the
chain rule D R[F]=V(R), with regularity, existence, uniqueness, consistent
readouts, and the stated reachable-state scope. Its all-time theorem requires
substantive gradient lower bounds, Hessian/stability bounds, relative defect
control, and global existence. Nonincreasing loss alone supplies none of
these. The unit-readout Gaussian illustration in that note is a separately
declared initialization and must not replace the canonical small stored
readout used in the present experiment.

The deep version has one physical approximation mechanism at two parameter
blocks: projected history cross moments. Its full defect is (0,E2,E3,0).
Both blocks contribute to loss perturbation and error propagation. There is
no new proof that compatible circle geometry supplies the global hypotheses.
Initial E2=E3=0 is exact realization by realization with the canonical
small-readout scaling, independently of that note's different illustration.

## 2. Why the orthogonal construction resolves the specified closure step

`RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md` replaces the older fixed rational
activity-bin gates by shifted Legendre moments on the entire growing activity
interval. These are distinct approximation families. The chronological
construction uses prefix length eta=1 independent of P, rather than the
bin route's eta=10^-3 P^-6. Its coefficients come from exact interval
transport. They are not optimized factors, chosen damping rates, a frozen
response dictionary, or externally supplied coefficients.

The retained raw moments are exact history coefficients of the surrogate's
own response paths. The sole approximation replaces their full history
cross integral by the cross integral of the first P orthogonal projections.
The constant forward prefix and zero backward prefix have zero unprojected
cross integral. In derivative-memory coordinates, the normalized backward
history's jump contributes the known initial-source correction. Omitting
this term changes the initial learned weight.

For each internal link ell=2,3, the deep derivation preserves all of this:

\[
 \Delta W_\ell=-\frac{2}{MnL}\sum_{a,k<P}(2k+1)
                  A_{\ell,k,a}B_{\ell,k,a}^T,
\]
\[
 E_\ell=\frac{2}{Mn}\sum_a
 (r_a\delta_{\ell,a}-\rho u_{\ell,P,a})
 (h_{\ell-1,a}-h_{\ell-1,P,a})^T.
\]

The positive sign, output normalization, sample normalization, and use of
the actual transpose are unchanged. The initial-source correction is
explicit in its derivative-memory formulas. The two links share activity
rho,L but have different forward histories and backward histories.

`MOMENT_INDEPENDENT_CHECK.md` independently verified the original
single-link formulas, including the transport matrix identity
T^T D+DT+D=ww^T, derivative-coordinate transformation, both rational-lift
invariants, and the exact initial tangency. Its corrected numerical account
does not invalidate the algebra. It also stresses that the rational lift
represents the same truncated closure, not the exact dense flow.

The prior conditional hierarchy estimate uses finite total activity,
activity-Lipschitz forward history, and bounded total variation of normalized
backward history, including its prefix jump. Bounded amplitude does not imply
bounded variation. For the deep extension, analogous estimates would require
these controls for h1 and h2 and both normalized backward sources. The
h2 regularity and lower-layer backward-source variation cannot be inherited
merely from the corresponding first-layer/two-hidden-layer statement.
Coupled stability and region containment would still be additional tasks.
The deep derivation correctly does not claim that these conditions are now
proved or that P=1,2,3 estimates establish a rate.

## 3. Rational equations versus the direct numerical realization

The exact lift stores h1,h2,h3,rho and evolves their chain rules, using
1-h^2 for the original tanh derivative. Its RHS is rational on rho>0,L>0.
The zero-residual boundary is a separately defined stationary case.
The explicit stage order in the deep derivation is valid: current backward
responses, all moment/outer velocities, both operator derivatives, then
forward response derivatives and rhodot. Neither A2dot nor B3dot needs
an unknown response derivative, so adding the upper link creates no
simultaneous implicit solve.

Both MNIST result/check pairs explicitly use direct tanh recomputation and
an algebraic residual RMS. They realize the same continuous closure while
avoiding numerical drift of redundant lifted coordinates. A new deep run
using that choice must be described the same way. It establishes evidence
about the rational-liftable closure, but it does not test numerical accuracy
of the fully rational lifted integrator. It also still needs solver and
endpoint refinement checks.

This distinction changes storage accounting. The deep minimal lifted state
contains nd+n+4PnM+3nM+2 scalars. A direct implementation storing only
W1,c,A2,B2,A3,B3,s has nd+n+4PnM+1 moving scalars. Any actual redundant C
coordinates, initialization copies, solver stages, data, and workspace must
be counted separately. Both realizations retain two initialized n-by-n
matrices. At n=4096 those two float64 matrices alone occupy 256 MiB.
Compressing the learned increments does not eliminate this fixed storage
or its dense multiplication cost.

## 4. Numerical corrections that must carry into the new interpretation

The earlier circle audit found that all six initial primary cells failed
the sampled maximum h1 lift-drift gate, even when an endpoint-only drift
looked acceptable. Refinement repaired the selected cells under the stated
empirical gates. Sampled maxima were not certified continuous-time maxima.
The fit flag referred to lifted loss, so independently recomputed physical
loss was essential. A direct-response implementation removes this redundant
activation-drift issue, but it does not inherit a flow-accuracy certificate.

That audit also separates reconstruction correctness from reference accuracy.
Rebuilding saved predictions to roundoff verifies saved states and formulas;
it does not verify the numerical integration that produced those states.
Dense-reference refinement mattered when closure discrepancies approached
the observed reference sensitivity. Once the reference changes, every order
or baseline must be recomputed against that same target. Coarse/fine
prediction changes are sensitivity diagnostics, not error bounds, lower
bounds, or confidence intervals. Nested circle quadrature grids likewise
test grid sensitivity, not a uniform-in-angle guarantee.

The exact oddness of a bias-free tanh network preserves antipodal reduction
at three hidden layers as well. If x and -x have opposite labels, hidden
responses, residuals, normalized source u, and both A/B moment pairs change
sign; each delta stays unchanged because tanh' is even. Both outer products
therefore remain unchanged, and averaging both members is equivalent to
averaging one representative when all pairs have the matching weights.
This conditional identity does not authorize changing arbitrary data.
Actual executed M, after any valid declared reduction, controls each MP
rank bound and the deep history count 4nMP. Labels or stored task names
cannot substitute for that actual count.

All prior main endpoint comparisons stop each model at its own first chosen
training-loss crossing. They are matched-training-loss comparisons, not
common-time trajectory tests or infinite-time endpoint theorems. A deep
experiment following that convention must retain the same qualification;
matched-time tracking requires separately saved aligned times.

## 5. What the MNIST evidence actually says

These are reports of the assigned study documents, not fresh reproductions
performed by this digest author. They concern two hidden layers, so they do
not establish accuracy of the new third-layer experiment.

| Campaign | Primary closure/dense RMS, P1 / P2 / P3 | Numerical conclusion |
|---|---|---|
| 1000 training images, n=1024 | 0.018771946 / 0.001918187 / 0.001232135 | P1 passes; P2/P3 fail the frozen relative-resolution gate |
| 100 training images, n=4096 | 0.0032475604 / 0.0010844347 / 0.0011992242 | All declared gates pass; P3 is slightly worse than P2 under the frozen margin rule |

In the 1000-image campaign, the dense predictor's latest refinement change
0.000220387 exceeds ten percent of the measured P2 and P3 discrepancies;
P3's own change also exceeds its threshold. The P2-to-P3 improvement is
0.000686052 against summed empirical sensitivities 0.000688191. Thus the
implementation and saved-output audit PASS coexists with an inconclusive
strict numerical ranking. It is not a contradiction or a reason to erase
the failed gate.

In the 100-image campaign, the P3 worsening relative to P2 is
0.00011478946, narrowly above the specified combined observed margin
0.00009998602. This is a resolved nonmonotonicity under that empirical rule,
not a rigorous sign theorem for exact-flow error. Dense/P3 repeated on the
opposite GPUs reproduce the saved arrays and checkpoints bitwise. This
checks repeatability at the same resolution; it does not add an independent
initialization, subset, or discretization-convergence theorem.

The two campaigns change both sample count and width. Their difference
cannot isolate a width effect or a sample-count effect. The first campaign
does not demonstrate a storage saving because its 2nMP history coordinates
already exceed n^2. The second shows smaller learned-history storage and
lower measured peak allocations in the particular implementation, while
moving-plus-fixed minimal totals exceed dense and integration is slower.
None of these facts transfers a universal memory or runtime advantage to
the deep experiment. State count, rank bound, fixed storage, retained
initialization, measured peak memory, and measured runtime are separate
quantities.

## 6. Audit conclusion and exact read coverage

No mathematical equation in `DEEP_CIRCLE_DERIVATION.md` was changed by this
context audit. Its initial-source correction, coupling, factor of n,
transpose semantics, rational-lift evaluation order, zero-residual case,
defect scope, and declared absence of a convergence theorem agree with the
subsequent correction record. Its introductory provenance now links this
audit so the expanded input scope is explicit.

The deepest unresolved issue remains control of both error production and
coupled error propagation over the intended trajectory family. The bounded
P=1,2,3 experiment can provide numerical evidence at its specified width,
data, initialization, stopping convention, and tolerance; it cannot resolve
the all-time, width-uniform, or hierarchy-existence obligations by itself.

Each file below was read completely, from first line to last, including
proofs, corrections, adverse outcomes, and limitations. The initially read
five inputs and their hashes remain recorded in the derivation file.
Links within these documents were not followed. No other study was opened,
no generated array or new engine source was read, and no experiment or
deterministic numerical test was run for this digest.

| Additional complete input | Lines | SHA256 |
|---|---:|---|
| RESPONSE_STATE_SYNTHESIS.md | 242 | b64e84242abc48d1ffaf0188e898c2e4240a2bfe8bb7b03ecc0d37b518227b49 |
| COUPLED_CURRENT_STATE_SYNTHESIS.md | 246 | 1ee7ccd1dbb59d257bf71ec3b18eb332d399c09cbca0c930449f5fac8fc2ae7c |
| SELF_CONSISTENCY_CRITERIA.md | 271 | 479f3f99b86bce19a1d70e29cf33e288c0ab74bba45a4f19bec2ad77acfedb8d |
| AUTONOMOUS_CLOSURE_CERTIFICATES.md | 395 | 6308ca4479eeea7f2b6e41ba7294d607e6f30648359dc81f466eb5e57956be93 |
| RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md | 268 | 677b4d4f7abd5239e1894411c127cf87230ddbde27ec447c2ae56836b7629f23 |
| MOMENT_INDEPENDENT_CHECK.md | 530 | 960fc9cbb46dad08d0d7e0a17cf186565891d7064ccd6219efecf7c03257ab6f |
| MNIST_CHECK.md | 173 | e3a0600a0fb7ec726be2b22a799db9bd10e889c291f92cd268d6b8be9db8365c |
| MNIST100_CHECK.md | 159 | edc904cf492883ddcf72896158216054b26d72cef7785bf6d930934873aada4b |
| MNIST_RESULTS.md | 131 | da2a3e32c648a2ff70dcf817c959f80e56c7af002c7268052845436e7b12e376 |
| MNIST100_RESULTS.md | 165 | 31146d381a143ed01f8be0c2badabac1396cdf9f34a695ec842544fe9e215f49 |

Total additional coverage: 2,580 lines. All writes are confined to this
digest and its companion derivation. The shared Git index is untouched.
