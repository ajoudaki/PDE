# Equal-exposure support shifts: current conclusion

The stronger support-shift test also rejects its registered positive claim.
Timing and support order matter, but favorable chronology beyond phase means
and ordinary gradient controls is not established. Fashion shows a reproducible
signed distinction: reversing credit within a phase can hurt substantially,
while exchanging whole phases can improve prediction. Its phasewise mean-only
swap improves more than the full historical swap. This is a useful diagnostic
of competing temporal contributions, not a successful high-order training method.

All54 allocated solves completed:48 fresh fits (four seeds, three domains,
four exposure-matched schedules), plus6 half-step checks. Their definitions,
thresholds, branches and input-only support groups were frozen in
STAGE2_COORD_CURRICULUM_PROTOCOL.md before scientific execution. The earlier
fixed-support failure remains unchanged in STAGE2_COORD_FIXED_RESULTS.md.

## What was controlled

The same512 labeled examples train a dense two-hidden-layer tanh model with
width256, canonical Gaussian initialization, zero readout, unhalved weighted MSE,
block mobilities(n,1,n), physical horizon64 and Euler step1/16. The target of
an example never changes. A/B groups use standardized image appearance for
Fashion, longitude for Housing, and training-subject IDs for HAR. Joint training,
A then B, B then A, and eight alternating A/B blocks give every example exactly
the same integrated loss weight. This is checked algebraically and numerically.
The supplied root data retain their original deterministic splits and provenance.

A physical-time observer records h and b=m lambda_a r_a delta_a. An endpoint
half-swap of b preserves each complete unpaired empirical history while changing
which features receive which historical credit. Reversal within each half is
a second fixed intervention preserving phase membership. Both are compared to
five controls preserving the edit's exact left and right Gram matrices, plus
isotropic same-spectrum controls and balanced-joint/last-phase gradient controls.
Training, validation and test curves are saved at0,8,...,64; both input-support
subgroups are scored wherever present. HAR's A-validation subgroup is absent
under its prescribed subject-disjoint validation split and is explicitly null;
both groups exist in training and test. This preflight metadata clarification
occurred before any fit and did not change the grouping.

The observer evaluates forward features on all512 training inputs at every
step, including inputs whose current phase weight is zero. All data remain
available throughout this experiment. Thus this is a controlled curriculum
on a known union support, not a demonstration of replay-free continual learning
or an online setting where future-task inputs are unavailable. Inactive labels
have zero update weight; full-support losses are logged for evaluation only.

The posthoc edited endpoint is not the endpoint of ordinary GD with shuffled
times. Neither matched exposure nor marginal-preserving surgery supplies that
causal bridge. The separate fixed-support causal block test had already failed
to establish an optimizer advantage; this extension does not relabel surgery as
an actual alternative learning trajectory.

## Every registered gate

The registered statistic first compares swap versus within-phase reversal,
subtracts the same contrast for their exact-Gram sign controls, averages AB/BA,
and subtracts the joint-schedule contrast. Positive chronology required that
statistic F be positive in all four seeds, median F>=0.05, centered-residual
damage>=0.02, and phasewise q1 account for less than half the full-swap absolute
loss change, in at least two domains.

| Domain | Four F values | Median F | Median centered damage | Median phase-q1 loss ratio |
|---|---|---:|---:|---:|
| Fashion | -.3231,-.3173,-.1209,-.1186 | -.2191 | .0806 | 1.784 |
| Housing | -.0287,-.0225,-.0256,-.0375 | -.0271 | .0219 | 1.085 |
| HAR | .0915,.1287,-.0041,-.0088 | .0437 | -.0447 | 2.332 |

No domain passes. Fashion/Housing have the wrong sign in every seed; HAR is
mixed. All domains fail the phasewise-q1 gate. The centered-residual column
uses a separate weight edit E_swap-E_swap,q1; that residual is not itself
claimed to preserve the complete history marginals. A large residual effect
therefore does not rescue the registered permutation-based interpretation.

## Signed effects worth retaining

Entries are median percentage changes in global held-out MSE relative to each
schedule's own untouched endpoint; negative means improvement.

| Domain/schedule | Full phase swap | Within-phase reversal | Phasewise q1 swap |
|---|---:|---:|---:|
| Fashion joint | +7.85% | +0.23% | +6.66% |
| Fashion AB | -3.31% | +6.78% | -8.45% |
| Fashion BA | -7.65% | +21.22% | -7.94% |
| Fashion alternating | +4.89% | -2.68% | +3.34% |
| Housing joint | +1.34% | +0.74% | +0.28% |
| Housing AB | -2.69% | +1.69% | -3.98% |
| Housing BA | +3.45% | +2.79% | +2.05% |
| Housing alternating | +1.47% | -0.47% | -0.34% |
| HAR joint | -1.33% | -3.39% | -6.37% |
| HAR AB | -1.41% | -3.36% | -5.80% |
| HAR BA | +1.11% | +2.70% | -2.35% |
| HAR alternating | -1.67% | -3.40% | -6.11% |

This separates operations that a blanket statement that “destroying history
hurts” would conflate. It also shows why selecting the largest damaging window
would have been misleading: the windows and operation meanings were fixed,
and whole-phase swaps can have the opposite sign. The relation is signed,
schedule-specific, and does not imply uniformly beneficial temporal coordination.

Subgroup curves expose the strongest simple alternative. Housing AB ends with
median test MSE .2003, against .1091 for joint and .1224 for BA. Its A/B subgroup
MSEs are .3137/.1014, whereas BA has .1087/.1352. Much of the order effect is
ordinary recency bias toward the last support. A balanced-joint gradient edit
improves AB by20.26%, versus2.69% for the full historical swap; it improves BA
by8.96%, while the swap damages it by3.45%. Temporal memory does not beat that
simple corrective signal. Fashion's curves also show late overfitting: a final
surgery improvement is not evidence that it beats standard stopping/model
selection. No test-selected stopping rule was fitted here.

HAR is almost perfectly classified; its small absolute MSE changes should not
be read as a large classification gain. Median base MSE is .00656 joint,
.00670 AB, .00610 BA and .00668 alternating. The balanced gradient improves
joint/AB/alternating more than the historical swap; BA is sensitive to the
choice of current support gradient. Ordinary directions remain viable accounts.

## A concrete compressed intervention, with honest scope

For two equal temporal halves, define phase-difference histories on local time
s in[0,T/2] by b_A-b_B and h_A-h_B. Their orthonormal Legendre coefficients
D_aj,H_aj give the swap edit

    E_swap,q = 2/(mn) sum_a sum_(j<q) D_aj H_aj^T.

The exact error is the interaction of the two discarded tails and is bounded
by their product, as proved completely in STAGE2_COORD_THEORY.md. The test
checks that bound for every order and endpoint. q1 is already a difference of
phase means; it can represent coarse phase coordination even though q1 cannot
represent single-interval reflection. These are distinct operators and moments.

Across all48 main fits, the largest q8 relative swap-edit error is .04595 and
largest q16 error is .009925. The largest q16 error occurs in alternating
Fashion, whose support switches create several discontinuities. Across sequential
AB/BA fits alone, maximum q16 error is .001005. The measured reconstruction
usually improves sharply with order, but monotone functional utility is absent:
the phasewise q1 edit often gives better test loss than the more faithful edit.
This cleanly separates faithful historical intervention from an effective learner.

Moment coefficients can be accumulated online at a known fixed block horizon
by adding each exact interval integral times the current signal. The audit code
retains full histories as the independent oracle; it does not benchmark a
storage-minimized implementation. With m=512 the coefficient state can exceed
one dense matrix. The supported tool is temporal-history compression and
structured surgery, not a total training-memory or runtime advantage.

## Checks and numerical scope

Independent weighted autograd agrees with every block velocity to2.7e-16;
uniform weights reproduce the source dense flow. All four schedules' exposure
sums match exactly. The half-swap algebra oracle errs by1.84e-16; its independent
product-bound test passes. Across main runs all observer, exposure, permutation
and Gram invariants are below5.19e-13. Relative feature motion is .439–.648
and nonlinearity gates pass, so the negative result is not a frozen-feature test.

Six half-step repeats use seed3401, joint and AB on every domain. Their largest
baseline held-out prediction RMS discrepancy is .000718. Their AB-minus-joint
control contrasts are more than twice their refinement changes in every domain.
BA was not refined; the full four-schedule difference-in-differences is therefore
not advertised as uniformly certified in step size. No positive claim depends
on extending the available numerical check. All registered positive claims
already fail by resolved signs, seed inconsistency or mean-only controls.

These are four initialization replications on one fixed split per domain, not
independent population/data replications. They establish no universality,
statistical-mechanical limit, or priority relative to existing continual-learning
methods. The exact finite identities are stronger mathematically but narrower
in scientific implication than those unproved claims.

## Artifacts, budget and closure

Sources: stage2_coord_curriculum.py, stage2_coord_curriculum_checks.py and
stage2_coord_curriculum_analyze.py; fixed contract and full theory are adjacent.
Generated stage2_coord_curriculum01 and stage2_coord_curriculum_refine01 contain
frozen source snapshots, commands/configuration, dataset hashes, every endpoint,
all curves, compressed coefficient arrays, matrices and completion hashes.
The tiny check report is stage2_coord_curriculum_checks01/results.json.
The fully keyed summary is stage2_coord_curriculum_analysis01/summary.json;
its static figures curriculum.png and curriculum.pdf show the curves and fixed
endpoint comparisons. Analysis consumes recorded data only; no fit is selected.

All54 extension solves completed in315.622 GPU-process wall seconds, including
archive output. Combined with the fixed campaign there are150 conservatively
counted solves:96 original-route solves and54 explicitly allocated root-reserve
solves. The two campaigns total484.186 producer seconds; fixed reflection analysis
adds9.95seconds, and small CPU oracles are subsecond excluding startup. No budget
was expanded autonomously. No new training branch remains under this allocation.
The findings are author-checked and await the root's separate independent audit.
No shared README, established book/code, manuscript, Git index or commit was edited.
