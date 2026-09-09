# Fixed L=2 research: persistent final record

**Status: stopped at the user's request on 2026-09-08.**

The requested practical global theorem was **not proved or disproved**.
There is no complete candidate manuscript for that theorem and no
counterexample to the actual prescribed Gaussian-initialized gradient flow.
The user explicitly superseded the earlier instruction to continue until
resolution with: “please stop and make sure all results are stored in a
persistent doc”. Research agents were stopped. Do not resume this program
without a new user instruction.

This document is the entry point to all saved results from the fixed-depth
program. Full derivations and reviews remain in the linked local files;
this consolidation does not replace or upgrade their proof status.
[FILE_MANIFEST.json](FILE_MANIFEST.json) inventories and hashes the saved files.
No numerical experiments, publication, or external messages were performed.

## 1. Exact intended theorem

The historical [CONTRACT.md](CONTRACT.md) contains the full quantifiers and
normalization. The main activation was fixed once and for all:

\[
\phi(z)=\tfrac34(1+z)+\tfrac14\tanh z.
\]

It was independent of input separation, dataset, width and time horizon.
There are exactly two hidden layers and three inputs with
`||x_i||^2=d` and pairwise cosine in `(-1+delta,1-delta)`. Singular input
Gram matrices are admitted. Labels are `+1` or `-1`.

The finite initialization remains independent Gaussian with entry variances
`1/d` for `W`, `1/n` for `A`, and `1/n^2` for the readout `C`. The small
finite random readout was never licensed to be silently set to zero.
The model, using normalized inner products, is

    z_i = W x_i, h_i = phi(z_i), v_i = A h_i,
    k_i = phi(v_i), f_i = <C,k_i>_n, r_i = f_i-y_i,
    b_i = C phi'(v_i), q_i = A^T b_i, d_i = phi'(z_i)q_i.

All three blocks train in the original raw metric
`(d/n)||Delta W||_F^2+||Delta A||_F^2+||Delta C||_n^2`:

    Wdot = -(1/d) sum_i r_i d_i x_i^T,
    Adot = -(1/n) sum_i r_i b_i h_i^T,
    Cdot = -sum_i r_i k_i.

The population action is the canonical limit of the actual repeated Gaussian
matrix programs, with its genuine adjoint. It is not an arbitrary substitute
bounded operator, nor an assumed Hilbert–Schmidt initialized operator.

The intended conclusion includes global autonomous strong population GF,
bounded-primal uniqueness and restart from every reached state; and, for every
finite `T`, full-sequence finite-width convergence in probability uniformly
on `[0,T]`, jointly for predictions, loss, all three true kernel blocks and
same-layer field path laws in `W2`. The actual simultaneous raw-GD bridge,
with step `n^-2`, and true velocity/second-moment/integrated-speed observations
also remain required where specified by the contract. Fitting and a positive
all-time kernel floor are stronger optional claims, not substitutes for this
target.

Distinct fixed bounded activations were investigated openly as alternative
candidates. Results for them must not be attributed to the principal
affine–tanh activation.

## 2. Results that passed fresh isolated review

Only the following two partial manuscripts acquired the stated fresh
whole-manuscript review status in this fixed-depth program. Neither is the
desired unconditional theorem. [REVIEW_SUMMARY.md](reviews/REVIEW_SUMMARY.md)
records the corrections and exact review scope.

### A. Dissipative approximants and conditional continuation

[CAPS_MANUSCRIPT.md](CAPS_MANUSCRIPT.md) constructs global approximants on
the given population spaces. It caps the whole first-row gradient with one
common nonnegative scalar, caps the readout velocity, and preserves the true
learned-matrix update. It proves

\[
E_R(t)+\int_0^t\|\dot\Theta_R(s)\|_{\rm raw}^2\,ds\le E(0),
\qquad
\|\Theta_R(t)-\Theta(0)\|_{\rm raw}\le\sqrt{tE(0)}.
\]

For `P_R=(sum_i r_{R,i}^2 q_{R,i}^2)^(1/2)` and
`g_{C,R}=sum_i r_{R,i} phi(v_{R,i})`, its conditional theorem assumes, for
every finite `T`, constants independent of the cap such that

\[
\sup_{R,t\le T}\left(
\|P_R\mathbf1_{P_R>a}\|_2+
\|g_{C,R}\mathbf1_{|g_{C,R}|>a}\|_2\right)
\le K_T e^{-c_Ta},\qquad a\ge1.
\]

It derives strong compact-time cap convergence, the true population flow,
uniqueness against bounded-primal strong competitors, restart and true-field
convergence through an explicit Osgood estimate. **The displayed tail premise
is unproved.** The actual finite GF/GD and observation bridges remain further
obligations.

Accepted SHA-256:
`c83bdce94e4655befbc35c88cafb19012c39a9fb2a3a08ced3ef216433acbaed`.
Fresh reviews: [CAPS_FINAL_ONE.md](reviews/CAPS_FINAL_ONE.md) and
[CAPS_FINAL_TWO.md](reviews/CAPS_FINAL_TWO.md), both PASS/no objections.

### B. First-row confinement for a distinct plateau activation

[PLATEAU_CONFINEMENT.md](development/PLATEAU_CONFINEMENT.md) proves a
deterministic control-independent amplitude bound for existing absolutely
continuous row paths

\[
\dot w=\sum_{i=1}^3 a_i(t)g(u_i\cdot w)u_i,
\quad g=0\text{ outside }[-1,1],\quad a_i\in L^1_{\rm loc}.
\]

Put `D_delta=sqrt(2/delta)+2`. In rank two it gives
`|w(t)| <= |w(0)|+D_delta`. In rank three, with
`kappa=lambda_min(Gamma)>0`, the additive constant is
`D_delta+(1+D_delta)/sqrt(kappa)`. Thus a Gaussian initial row supplies a
common Gaussian amplitude envelope. The rank-three constant is not asserted
uniform as the positive eigenvalue approaches zero; rank two is handled
separately.

This is confinement of existing paths. It does not prove coupled population
existence, source tails, global uniqueness, or the finite GF/GD theorem.

Accepted SHA-256:
`e66b09fd0b115113da658cff6a0e7f3da3ddbc5401360b275546cdacb027b5d3`.
Fresh reviews: [PLATEAU_CONFINEMENT_FINAL_TWO.md](reviews/PLATEAU_CONFINEMENT_FINAL_TWO.md)
and [PLATEAU_CONFINEMENT_FINAL_THREE.md](reviews/PLATEAU_CONFINEMENT_FINAL_THREE.md),
both PASS/no objections.

## 3. Final completed round: useful partial results, not isolated-reviewed

These three complete reports were saved before the stop. They are development
proofs and have not passed the requested final isolated review process.

**Canonical response measures.**
[BOUNDED_RESPONSE_MEASURE.md](development/BOUNDED_RESPONSE_MEASURE.md) treats
`phi=1+.5 sin`. The chronological Gaussian program gives

\[
v=\xi+Pb,\qquad q=\zeta+Rh,
\quad X=F_q+F_qRX,\quad P=\mathbb EX+L_h,
\quad Y=Q+QPY,\quad R=\mathbb EY+L_b.
\]

The report retains current response atoms, both learned returns and both
matrix orientations, without temporal Gram inverses. It controls Gaussian
primitive path suprema and derives a cap-uniform *local* response bound. If
`r_resp(t)` is the maximum row total variation of `R`, the strongest general
majorant is

\[
r_{\rm resp}(t)\le L_Rt+
Q_T\exp\!\left(K_Tt+b\int_0^t r_{\rm resp}(s)\,ds\right).
\]

Its comparison equation can blow up at a finite time. This does not establish
physical blowup. A signed averaged-chain hypothesis would instead yield a
global convolution bound with an explicit Catalan/factorial majorant; that
hypothesis remains unproved for general admitted input Grams.

**Bounded legal-query audit.**
[LEGAL_QUERY_AUDIT.md](development/LEGAL_QUERY_AUDIT.md) proves width-uniform
sub-Gaussian source-path tails for a narrower class of continuous systems:
bounded Lipschitz queries, globally Lipschitz drifts, and *constant*
coefficients multiplying Gaussian incoming fields. The proof uses the same
matrix and transpose throughout, Gaussian-entry sensitivity, exchangeability,
and an explicit matrix-norm tail argument. The network's first-row multiplier
depends on the state, so the theorem does not apply. A legal auxiliary
gradient example shows unbounded maximum variational response without source
concentration. No valid concentration counterexample satisfying the complete
physical contract was found.

**Sine-preserving steps and capped source production.**
[SINE_RESUMMED_ITERATION.md](development/SINE_RESUMMED_ITERATION.md) retains
the actual finite random readout, uses a common radial return cap, and solves
the local sine row equation exactly. Its raw consistency defect is `O(mesh)`
with a constant independent of cap and width. Stability still costs
`exp(C_T(1+M)T)`. A legal deleted-column comparison produces Gaussian tails
for the actual capped backward source, but with scale of that same exponential
order in cap `M`. Since this exceeds the clipping threshold as `M` grows,
the estimate does not remove the cap. A separate conditional theorem shows
that a cap-independent exponential path-source bound would give uniform
finite-width cap removal. The short-time refinement still contains the
correlated product
`M_exp(Lambda) A^T(b-b_cavity)`; the cavity Gaussian primitive does not control
that product.

## 4. Complete development index

Except for the specifically reviewed confinement report, these files are
development analyses. “Counterexample” below means a counterexample to a
stated auxiliary implication, not to the actual physical theorem.

| Saved report | Content and scope |
|---|---|
| [ENERGY_ROUTE.md](development/ENERGY_ROUTE.md) | Energy-preserving cap construction, one-cap comparison, residual-weighted tail target, curvature-decay refinement; precursor to the accepted cap manuscript. |
| [SOURCE_ROUTE.md](development/SOURCE_ROUTE.md) | Exact Gaussian source/return chronology, primitive bounds, generic tail-transfer obstruction, endpoint attainment without a restart theorem. |
| [CAVITY_ROUTE.md](development/CAVITY_ROUTE.md) | Tagged-neuron comparison, surviving order-one self-return, adapted-state stability counterexamples, restricted fresh-kick estimates. |
| [DISORDER_LITERATURE.md](development/DISORDER_LITERATURE.md) | Full-text/proof applicability checks of the recorded disorder-dynamics sources; none supplies the requested theorem. Elementary conditional convolution estimate. |
| [INTEGRATED_CURVATURE.md](development/INTEGRATED_CURVATURE.md) | Signed velocity-curvature identity, orthogonal cancellation, and nonorthogonal metric/commutator obstruction. |
| [VARIATIONAL_ROUTE.md](development/VARIATIONAL_ROUTE.md) | Ambient convexity and weak-compactness shortcuts fail on non-reached states; not a physical negative theorem. |
| [STRUCTURAL_ACTIVATION_ROUTE.md](development/STRUCTURAL_ACTIVATION_ROUTE.md) | Distinct bounded activations with a global population argument for orthogonal inputs; general geometry and full finite bridge remain open. |
| [GAUSSIAN_OPERATOR_ROUTE.md](development/GAUSSIAN_OPERATOR_ROUTE.md) | Common-source action decomposition, Gaussian compression, projected Osgood estimates; unprojected closure remains missing. |
| [CONCENTRATION_DEFECT_ROUTE.md](development/CONCENTRATION_DEFECT_ROUTE.md) | Learned-return defect estimates and nonphysical concentration paths, including energy-compatible paths; physical reachability is not established. |
| [PLATEAU_GEOMETRY.md](development/PLATEAU_GEOMETRY.md) | A fixed smooth activation with plateaus `.5,1.5`; invariant frozen first-feature Gram at least `exp(-22/delta) I/240`, including singular Grams; initial nonaffinity. |
| [PLATEAU_CONFINEMENT.md](development/PLATEAU_CONFINEMENT.md) | Reviewed deterministic row confinement theorem; exact limits stated in Section 2 above. |
| [PLATEAU_DYNAMICS.md](development/PLATEAU_DYNAMICS.md) | Dormant top rows and compact-time kernel floor for already source-identified paths; sharper chaining; explicit finite-clock certificate insufficient for the moderate candidate. |
| [PLATEAU_HOSTILE.md](development/PLATEAU_HOSTILE.md) | Force coercivity and bounded learned returns; a rare finite initialization event refutes a deterministic fitting implication, not the limit theorem. |
| [FEATURE_MOBILITY_HOSTILE.md](development/FEATURE_MOBILITY_HOSTILE.md) | A feature-only reduction loses raw plateau depths; entropy/mobility comparison shortcuts fail. |
| [PLATEAU_PATH_COMPACTNESS.md](development/PLATEAU_PATH_COMPACTNESS.md) | `W2` path-law total boundedness for selected bounded observables across existing approximants; no canonical strong identification or raw-backward-field conclusion. |
| [PLATEAU_BOTTOM_CAVITY.md](development/PLATEAU_BOTTOM_CAVITY.md) | Deleted-row primitive Gaussian tails and exact correlated return identity; missing propagated response. Confined supplied-control saddle does not reproduce physical GF. |
| [BOUNDED_SOURCE_EVOLUTION.md](development/BOUNDED_SOURCE_EVOLUTION.md) | Exact bounded `L2` generator for backward fields of a separate tanh candidate; initial Gaussian-plus-bounded seed; projected compensation; missing unprojected source moments. |
| [BOUNDED_CURVATURE_COMPENSATION.md](development/BOUNDED_CURVATURE_COMPENSATION.md) | Backward-field and compensated metrics leave specified uncontrolled products; no impossibility theorem for all metrics. |
| [BOUNDED_SINE_PICARD.md](development/BOUNDED_SINE_PICARD.md) | Initial nondegenerate canonical return for sine, including singular Grams; absolute differential majorant loses cancellations; bounded legal queries remain relevant. |
| [BOUNDED_RESPONSE_MEASURE.md](development/BOUNDED_RESPONSE_MEASURE.md) | Completed final response-measure branch summarized in Section 3. |
| [LEGAL_QUERY_AUDIT.md](development/LEGAL_QUERY_AUDIT.md) | Completed final semilinear bounded-query theorem and scope audit summarized in Section 3. |
| [SINE_RESUMMED_ITERATION.md](development/SINE_RESUMMED_ITERATION.md) | Completed final exact-local-step/capped-cavity branch summarized in Section 3. |
| [INTERRUPTED_AVERAGING_NOTES.md](development/INTERRUPTED_AVERAGING_NOTES.md) | Unverified interim claims from the immediately interrupted last worker, including the erf weighted-volume idea and an unproved supplied-control loop. Not an established result. |

The last interrupted worker had not created its intended full report. Its
interim messages are preserved in the last row above so they are neither lost
nor mistaken for a proof. In particular, its proposed control-loop example
had not addressed the actual uniform unweighted backward-field `L2` bound.

## 5. Remaining gaps and conclusions that must not be claimed

The repeated-matrix backward return is the unresolved part of this program.
Bounded activations give bounded legal queries `h,b`, bounded learned kernels,
and controlled primitive Gaussian paths. These facts did not yield a uniform
tail or comparison estimate for the entire adapted backward field. Exact
comparison still includes products such as

\[
(\phi'(z)-\phi'(\widetilde z))\,q,
\]

which are not controlled in raw `L2` by the established state bounds alone.
The reports isolate several sufficient stronger estimates, but none has
been proved on every compact physical-time interval in the required general
geometry.

In particular, do not infer any of the following from the saved work:

- unconditional global canonical strong existence and uniqueness for the
  principal practical activation;
- the required full actual finite GF/GD joint limit;
- cap removal from a source estimate whose constants diverge with the cap;
- a physical counterexample from an arbitrary adapted state, prescribed
  control path, or rare finite-width event;
- a global result from a local response bound without quantitative restart;
- coverage of correlated inputs from an orthogonal-input coordinate change;
- validation of the whole research objective from the two partial PASS
  review rounds.

No new external theorem was adopted in the final bounded-query/response round.
The final web screening returned related spin-glass and DMFT papers, but no
new full-proof applicability conclusion was obtained from that screening.
The explicit external-dependency audits that were completed are preserved in
[DISORDER_LITERATURE.md](development/DISORDER_LITERATURE.md). A future reader
must not treat a search result or a source's abstract as an audited invocation.

## 6. Earlier context retained outside this directory

These existing documents were left unchanged. They are background, not newly
proved fixed-depth results:

- [Practical-route assessment](../practical_global_limit_assessment/ASSESSMENT.md)
  and its [review record](../practical_global_limit_assessment/REVIEW_SUMMARY.md).
- [All-depth activation-class manuscript](../activation_class_all_depths/MANUSCRIPT.md)
  and [review record](../activation_class_all_depths/REVIEW_SUMMARY.md). Its
  large affine gain is the practical limitation that motivated this program.
- [Convex-offset depth report](../convex_offset_all_depths/REPORT.md) and
  [review record](../convex_offset_all_depths/REVIEW_SUMMARY.md), with its
  initialized-conditioning scope.
- [Calibrated near-identity initialization manuscript](../calibrated_near_identity_reviews/manuscript.md)
  and [review record](../calibrated_near_identity_reviews/REVIEW_SUMMARY.md).
  This establishes initialized covariance behavior, not trained global GF.

The detailed historical ledger is [PROJECT_STATE.md](PROJECT_STATE.md), and
the shorter results narrative is [RESULT.md](RESULT.md). All are now marked
stopped. The underlying mathematical objective remains unresolved; stopping
was the user's decision, not a claim of scientific completion or impossibility.
