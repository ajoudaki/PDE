# Independent internal check of historical repair

Reviewer: `/root/history_review`, 2026-10-01. This is the assigned bounded
internal check, not a promotion review. The observer algebra, repair signs,
specified dense dynamics, and reproduced seed201 result pass the checks below.
The original strong practical effect is **not uniformly confirmed**: seed202
misses the preregistered 10% improvement threshold at both time steps. The
supported statement is a finite-benchmark, fixed-cleanup intervention benefit,
with substantial variation between initializations.

## Assignment, isolation, and complete read coverage

The neutral assignment was to audit the dense update observer, activity scaling,
Legendre integrals, online power moments, repair signs, current-gradient control,
information leakage, and refinement; independently reproduce corrupted seed201,
width256, dt1/64, T32, with six cleanup continuations; and report exact hashes,
coverage, commands, differences, and limitations. The bound was one full
trajectory plus six cleanups, at most120 CPU seconds or3 GPU minutes, with tiny
independent oracles permitted. Only the seven named scientific sources and the
five named generated directories below were allowed. Output ownership was this
report, `history_review*.py`, and `history_independent_review01/`.

I read all lines of `baseline_compact_flow.py` (1–2056), `history_probe.py`
(1–292), `history_probe_initial.py` (1–261), `history_controls.py` (1–54),
`HISTORY_PROTOCOL.md` (1–92), `HISTORY_CONTROL_PROTOCOL.md` (1–22), and
`MODEL_RECONCILIATION.md` (initially 1–94, then the final revision 1–115).
Truncated combined reads were repaired with
separate source ranges. The mathematical audit concerns the tanh dense Flow
execution path; reading the other classes does not constitute a correctness
review of their unrelated methods. The comparison with the paper is limited to
the supplied reconciliation document; I did not independently inspect the paper.

I read the manifests, completion records, and scientific result fields for
`history_pilot01`, `history_pilot02`, `history_confirm01`, `history_refine01`,
and `history_controls01`. The check script reads/hashes every file in those
directories, verifies every producer-recorded NPZ digest, checks that individual
result JSONs equal the corresponding aggregate rows, and checks every control
candidate's selection and base-edit norm. Every array of the reproduced seed201
archive is compared elementwise. Other trajectory arrays are hash-verified, not
independently reproduced or exhaustively reinterpreted numerically.

Required process inputs were the shared instructions, Part1 of
`RESEARCH_WORKFLOW.md`, `explain-with-canonical-notation` and its neural response
reference, and `investigate-conjectures` with the bounded-experiment and
adversarial-audit references. No study history, other study research, route
reports, author verdict, manuscript, or archived book was read. Git checks were
metadata only. `baseline_compact_flow.py` imports the established
`pde.observable_initialization.build_dictionary`; the supervisor explicitly
allowed execution of that unchanged import without widening source scope.
That helper is not called by the audited dense path and its source was not read.

## Algebra and implementation

For sample a, let u_a in R^2 be the normalized input row used by Flow,
W^(1) in R^(n x 2) and W^(2) in R^(n x n) the two hidden matrices, and w in R^n
the readout. The audited network is

\[
h_a^{(1)}=\tanh(W^{(1)}u_a),\quad
h_a^{(2)}=\tanh(W^{(2)}h_a^{(1)}),\quad
f_a=w^\top h_a^{(2)}/n,\quad r_a=f_a-y_a,
\quad\mathcal L=m^{-1}\sum_a r_a^2.
\]

There are no biases or normalization layers. Both hidden layers evolve, the
readout starts at exactly zero, W^(1) has independent standard-normal entries,
and W^(2) has independent normal entries of variance1/n. Flow applies
simultaneous explicit Euler to the negative loss gradients with mobilities
(n,1,n). Its upper backward response is
\(\delta_a^{(2)}=w\odot(1-h_a^{(2)}\odot h_a^{(2)})\), so the hidden-matrix sample velocity is

\[
\dot W_a^{(2)}=-\frac{2}{mn}r_a\delta_a^{(2)}h_a^{(1)\top}.
\]

`train_record` samples h, delta and r before each call to `step`, just as the
Euler RHS does. Its per-sample accumulator sums dt times this velocity with
the correct sign and no missing width or sample factor. The accumulated sum
matches the actual hidden-matrix displacement; this checks the producer, not
just a second reconstruction formula. A separate autograd oracle also checks
each layer's mobility and each sample's hidden write.

For a step with residual RMS \(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\), the observer's
activity interval has length dS=rho dt and carries constant forward history
h_a^(1) and backward history b_a=r_a delta_a^(2)/rho. At rho=0 the sample write
is zero and the interval has zero length. Thus, for final positive activity
length S, the exact recorded displacement is

\[
\Delta W^{(2)}=-\frac{2}{mn}\sum_a\int_0^S
b_a(\xi)h_a^{(1)}(\xi)^\top\,d\xi.
\]

The observer deliberately excludes the manuscript's artificial prefix. With
\(\psi_j(\xi)=\sqrt{(2j+1)/S}\,P_j(2\xi/S-1)\), its coefficients are
\(\bar h^{\rm obs}_{a,j}=\int_0^S h_a^{(1)}\psi_j\,d\xi\) and
\(\bar\delta^{\rm obs}_{a,j}=\int_0^S b_a\psi_j\,d\xi\). These are orthonormal
projection coefficients, not the manuscript's raw moments. `interaction`
implements the order-q approximation

\[
\Delta W_q^{(2)}=-\frac{2}{mn}\sum_a\sum_{j=0}^{q-1}
\bar\delta^{\rm obs}_{a,j}\bar h^{\rm obs\top}_{a,j}.
\]

For j>=1, integrating the Legendre primitive
(P_(j+1)-P_(j-1))/(2j+1), including the change-of-variable factor S/2,
gives precisely `interval_coefficients`. The zeroth integral is the interval
mass. An independent 40-node Gauss rule on each unequal interval, including
zero-mass intervals, agrees through q32 to1.41e-14 absolute.

The online coordinates are genuinely causal. For either history g, define
\(J_k(S)=\int_0^S g(\xi)(\xi/S)^k\,d\xi\). On appending a constant interval
g_new of length dS, put S_new=S+dS and alpha=S/S_new. Then

\[
J_k(S_{\rm new})=\alpha^kJ_k(S)+
g_{\rm new}S_{\rm new}\frac{1-\alpha^{k+1}}{k+1}.
\]

This derives the implemented recurrence directly by splitting the integral.
Converting the powers to shifted Legendre polynomials and applying the
normalization above is correct. Each current update needs only the previous
eight moments, accumulated activity, and current fields. Raw histories and
full per-sample matrices are nevertheless retained in this diagnostic program
for validation. They are not read to construct the online repair edits.
The observed q8 power-basis agreement supports this bounded implementation;
it supplies no high-order or arbitrarily long-time conditioning guarantee.

Let B={1,7} be the declared corrupted pair, and let Delta W_B be the sum of its
recorded hidden updates. Adding -Delta W_B undoes those accumulated physical
writes while leaving the other weights unchanged at surgery. The sign in both
the exact and moment repairs is correct. This is not retraining without B:
all histories were generated along a coupled trajectory influenced by B.
`edit_score` deep-copies the state, applies the edit, changes training labels to
their corrected values, and applies the same T_clean=2 Euler budget to all six
original arms. The underlying parameter aliases survive the deep copy.

The original current-gradient edit is the current **negative** corrected-loss
hidden gradient, scaled to the exact-history edit's Frobenius norm. It uses all
corrected training labels. Thus the update has the correct descent sign; its
finite size can still overshoot. It matches the exact arm's norm, not every
approximate arm's norm individually. The later control instead matches the q4
norm exactly and gives both directions the same six multipliers. Selection is
the minimum immediate corrected **training** MSE. Held-out values and losses
after cleanup are computed and stored but are not selection keys. This is a
valid declared exploratory control, not independent confirmation.

The teacher on held-out angles enters scoring only. Initial draws and online
coefficient production do not use evaluation truth. Corrected labels and the
identity of the corrupted examples are assumed available to the intervention;
neither corruption detection nor repair without corrected labels was tested.

## Executed checks and reproduction

From `/home/amir/Codes/PDE`, I ran exactly:

```bash
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 110s /home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/history_probe.py --seeds 201 --width 256 --horizon 32 --dt 0.015625 --device cpu --panel repair --out data/generated/response_memory_use_cases_20261001/history_independent_review01
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 20s /home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/history_review_checks.py
```

Both commands exited0. Environment: Python `/home/amir/miniconda3/bin/python`,
PyTorch2.9.0+cu130, NumPy1.26.4, Linux5.15.0-151-generic, CPU float64, one thread,
TF32 disabled. HEAD was `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`; the shared
index was empty and unrelated working changes were left untouched. No Git
writes occurred. The full producer plus six cleanups took7.262192 seconds;
small checks took0.414830 seconds, excluding interpreter startup. No GPU was
used and the120-second CPU allowance was not approached. The small oracles
used width7 with one-step and16-step histories, not additional research runs.

Every seed201 scientific JSON value is exactly equal to the saved confirmation
after excluding elapsed training time. All20 NPZ arrays match elementwise
with maximum absolute difference0; the entire archive SHA256 also matches.
The producer's q32 relative errors are1.13687e-7 for the total write and
5.38887e-8 for the bad-pair write, well below the2% gates. Update parity is
3.03790e-14 against the1e-10 threshold. Online/offline moment discrepancy is
2.54204e-11 against the1e-6 threshold.

| Seed201 arm | Evaluation MSE after cleanup |
|---|---:|
| No edit | 0.05784276315199181 |
| Exact history | 0.04218372205553535 |
| q1 online | 0.039993982780931116 |
| q4 online | 0.042154923103645145 |
| q8 online | 0.04218311800263391 |
| Current gradient | 0.057423080639710196 |

Independent oracle errors: at most2.22e-16 absolute for the three negative
gradient velocities,3.39e-21 absolute for per-sample writes, and2.02e-12 relative
for the online q8 moments against direct interval quadrature. Edit addition,
state isolation, recorded archive hashes, aggregate/individual JSON consistency,
and all saved training-only control selections passed.

## Findings and claim limits

The q4 evaluation-MSE improvements over equal-budget no edit are27.12%,1.03%,
26.14%,24.64%,10.22% for seeds201–205. The first-screen pilots all pass their
10% gate, but the five fresh confirmations do not pass it uniformly. q4
closely reproduces the exact-history benefit, including the weak seed202
effect. At dt1/128 the q4 improvements for seeds201/202 are27.04%/0.99%.
Using the conservative larger of the no-edit and q4 MSE changes as the
refinement discrepancy, the coarse benefit is169.2 and14.9 times twice that
discrepancy, respectively. Thus the tested benefits clear the step-refinement
gate, while refinement does not rescue the strong practical threshold.

All five selected history directions beat the selected current-gradient
directions after equal cleanup in the supplied exploratory control. However,
T_clean=2.5 with no edit beats the selected history edit on seeds202 and205.
It nearly matches the history result on204. An advantage over a modest amount
of ordinary optimization is therefore not uniform. No runtime or energy
advantage follows: the diagnostic records full trajectories, stores dense
per-sample accumulators, and the control producer performs cleanup for every
candidate multiplier before selecting one.

q1 has lower final evaluation MSE than q4, q8, and exact-history repair on all
five confirmations. Therefore these data do not establish that centered
temporal pairing or higher moments are necessary for the repair benefit.
They do establish that low-order online histories approximate this chosen
physical edit accurately. Mean-only historical writes remain a strong simpler
explanation of the useful intervention.

The coordination pilots are negative under the stated20% evaluation-RMS gate:
removing the centered part changes RMS by2.68%,3.03%,6.48%; the worst of the
five rotations changes it by3.28%,5.04%,11.10%. Simultaneous rotations and the
reported second-moment invariants are numerically preserved. The current
implementation matches random perturbations for the five rotations, but not
for the removal/half-removal arms, although the protocol says each intervention
is matched. It also does not save the promised prediction difference from the
dense baseline. Those omissions prevent claiming complete execution of every
coordination diagnostic, but do not manufacture a positive result or affect
the repaired-label experiment reviewed here. No new coordination run was made.

Two bounded robustness limitations were found. First, `train_record` divides
its final coefficient normalization by zero if the entire trajectory has
zero activity; a tiny stationary example returns nonfinite moments although
the network correctly remains stationary. `interval_coefficients` separately
rejects zero activity. The positive-activity benchmark is unaffected; the helper
should not be advertised as handling arbitrary stationary data. Second, if
q32 failed and q64 also failed the2% gate, `run_case` would still return scores
without enforcing an inconclusive status. Every supplied run passes already at
q32, so this is an unexercised gate-enforcement limitation, not an observed
failure of these results. Neither candidate source was changed in this review.

These tests concern one teacher,12 correlated circle inputs, a known antipodal
corruption pair, finite widths128/256, fixed horizon32, and finite cleanup
budgets. Corrupted training RMS remains above0.1. The study does not establish
unlearning, autonomous closure accuracy, convergence of the moment hierarchy,
population generalization guarantees, or a theorem about all initializations.

## Exact provenance

| Complete scientific input | SHA256 |
|---|---|
| baseline_compact_flow.py | f908c03cb63be0286d8505c2ce7959ea2377ccbcb8f740a10fac9dac8c49a67d |
| history_probe.py | a92d360ea6609943ecadc8cde99b2295871e3df0c9907e2a910a7fd7fd7bb2d3 |
| history_probe_initial.py | fed94a96d5d34741e23b3edfdcd8ffeb27e0eb6428d3e1a1e4e399d3488aac43 |
| history_controls.py | 17d5130b6d0d8e1966d1bcd0ef34a161067ebaabb703965718ad1f49eede2a63 |
| HISTORY_PROTOCOL.md | aa660ce13ff9dc85f537c5f615f5f61b0f60a6b253eff536365864e769fa2498 |
| HISTORY_CONTROL_PROTOCOL.md | 0d56a61705ea2857b65c69f721c602cf6e42d55f795683b5251f9ab92400bcb6 |
| MODEL_RECONCILIATION.md | 473ede0a69a474626aa94f1880e484c8c67358065ccb64c5670785c2be03db4f |

The final freeze check detected a concurrent revision of
`MODEL_RECONCILIATION.md`. I read all 115 lines of that revision; its SHA256 is
`864c0b875cd1ea25c3228fd8dba9c6f6af71c045695bb55ec3657c3a9cc75a20`.
It adds qualifications about the hypergradient Gram hypothesis and an
input-field normalization correction. The common dense equations, history
intervention paragraph, and audited history code are unchanged. Those route
qualifications were not used as evidence for this review. The table above and
`review_checks.json` preserve the exact inputs at execution; the final input
check records the changed prose digest separately. All other six inputs remain
unchanged, so no numerical rerun is needed for this unrelated prose revision.

The initial-script hash equals the script hash in both pilot manifests. The
current script hash equals the confirmation/refinement manifest hash. Their
protocol hashes differ because the current protocol contains the later online
strengthening; the original pilot protocol bytes were not separately supplied,
so its exact earlier contents cannot be independently reconstructed from its
digest alone. Current pilot/confirmation source correspondence is verifiable.

All prior evidence-file digests are retained under `evidence_file_hashes` in
`data/generated/response_memory_use_cases_20261001/history_independent_review01/review_checks.json`.
That check record has SHA256
`550cdd2830b1a9f66c07bd17e77c09f1486826a8462fd3c04c35ef77f2551a15`.
The independent check source has SHA256
`a38f50fce453b46a775a52fc54707aa7f0bc51496ac732d2de8fcd6d8b2a1bbe`.
The reproduced NPZ has SHA256
`5342ae04b16629c3abb9223a3b72ea38e74df869ee079296c81591e1daddabe9`;
the new manifest has SHA256
`d92c404b13bec63f56d64684894bf7bee5543c983d1198ed504b9c87d4ae14ce`;
the completion record has SHA256
`328fa5f3d447fcae7b19c7da1a14e3f4cfa9c30f91339e1cfe9e68c0de6a1ca0`.

No empirical design was expanded, no further trajectories are recommended by
this check, and no established material was edited. Internal implementation
and seed201 reproduction checks are complete for the precise scope above;
the failed uniform10% claim and the stated limitations remain part of the result.
