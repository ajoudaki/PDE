# Explicit width rate for the all-time response-memory theorem

Started 2026-10-01. This is a new study, separate from the intrinsic q=1 learning investigation. The user asks to replace the paper's qualitative width remainder by an explicit dependence on n, ideally an algebraic rate, retaining the small-label, fixed-depth, all-time canonical Gaussian setting.

## Contract and permitted sources

The primary source is the current paper: paper/main.tex, paper/results.tex, paper/proof_alltime.tex, paper/proof_tracking.tex, and necessary included material. The user explicitly requests extending that theorem. Maintained docs/index.qmd and docs/notation.qmd are the scientific startup sources; relevant maintained book results may be used after full reading. Other studies and historical chat proof claims are not inputs.

Keep the canonical fully Gaussian reused matrices, zero initial readout, fixed finite data and depth, C1 activations with bounded Lipschitz derivative, positive limiting feature-Gram gap, and sufficiently small fixed label RMS. The approximation is the actual autonomous old-clock closure. Error is the paper's all-time normalized parameter distance and all-time whole-input prediction norm. Probability/confidence dependence must be explicit. No clipping, block initialization, frozen-feature replacement or strengthened concentration assumption may be silently inserted.

Authorization: new theoretical proof work and bounded mathematical checks. No paper edits, Git mutations, training experiments or generated numerical evidence. Repository HEAD at startup: 690e3d4f56ca7ecbad37bb6bacb757b8cfff7682. Existing paper/main.pdf and other tasks' artifacts are dirty and will be preserved.

## Exact source decomposition

The paper has D_nq <= C omega(q)+b_n, with omega(q)=q^-2 exp(K sqrt(log(e+q))). It sets b_n=C Phi(a_n), Phi(u)=u exp(K sqrt(log(e+1/u))). The source a_n is the excess of an integrated dense backward-carrier tail above a Gaussian cutoff envelope, uniformly over integer cutoffs. For prediction against the population, b_n,mu=C_mu b_n+d_n,mu, where d_n,mu is the dense-to-population prediction discrepancy. Quantifying the carrier remainder alone does not quantify the full prediction remainder.

## Routes and ownership

Root owns this README and the synthesis and will verify all accepted derivations. Fresh scoped routes examine quantitative finite Gaussian-program transfer, direct finite-width carrier-tail control, and limitations/rate lower bounds under the exact initialization. Each route will receive only the current paper and permitted maintained sources, and will write a separate note. Initial candidates remain separate until frozen.

## Current status

**Internally checked explicit logarithmic rate; general polynomial width rate remains open.** The central statement and proof map are in [RESULT.md](RESULT.md). Under exactly the current paper's small-label all-time hypotheses, a conservative common choice is

\[
r_n=[\log(e^e+n)]^{-1/512}.
\]

For all sufficiently large n, simultaneously for every q, normalized parameter tracking is at most C omega(q)+C r_n on an event of probability at least 1-C n^{-c}. Whole-input all-time prediction error against the dense population is at most C_mu omega(q)+C_mu r_n with probability at least 1-C_mu r_n for every fixed finite-second-moment test law. Fixed bounded input domains also admit a time-and-input supremum bound. Constants are independent of width, order and time; depth remains fixed. This is high-probability control, not an unconditional prediction-moment statement off the original good initialization event.

The result quantifies both the dense-carrier excess entering b_n and the separate dense-to-population prediction remainder. It uses a growing, explicitly conditioned Gaussian query program and a physical proxy whose consistency error is controlled, then residual damping to replace physical-time amplification by total-activity amplification. Clipping and fresh query noise appear only in the proof. The actual network, closure, and old residual-RMS clock are unchanged.

## Proof files and supersession

- `RESULT.md`: final coherent theorem, assumptions, quantitative proof, and scope.
- `PROGRAM_RATE_ROUTE.md`: finite Gaussian-program coupling with exp(C N^5) constants, original-population bias, and an initial conservative transfer.
- `PROGRAM_RATE_ADDENDUM.md`: complete physical-proxy action identities, quantitative initialization event, current-state tails, and the activity-damped refinement in Section 9.
- `DAMPED_TRANSFER.md`: root reconstruction of the improved all-time transfer and whole-input confidence bounds. Its stronger 1/256 logarithmic bookkeeping is also supported, but the central result deliberately uses 1/512.
- `PROGRAM_RATE_CHECK.md`: independent internal reconstruction of all these proof steps, corrected findings, final checked hashes and accepted scope.
- `TRANSFER_DERIVATION.md`: earlier, valid but weaker stretched-logarithm transfer, superseded by the activity-damped result.
- `CARRIER_RATE_ROUTE.md`: independently derived algebraic carrier rate in the linear special case and the remaining nonlinear direct-cavity obstruction. It does not replace the nonlinear proof.
- `WIDTH_OBSTRUCTION_ROUTE.md`: an exact zero-readout example with fitted prediction RMS of order n^-1/2, ruling out a universal n^-1 root-prediction error law in the theorem's whole activation class. It also gives a full linear all-time estimate. This is not a lower bound on the carrier-only b_n.

Frozen route documents retain their original candidate labels as a record of their state before checking; this README and RESULT.md give the final status. No claim of practical width efficiency, a general n^-1/2 upper bound, or an epsilon^-5/2 learned-state budget follows from the logarithmic rate.

## Verification and source identity

The root read and reconstructed the full finite-program and proxy proof, residual-damped comparison, general-test-law passage, and linear obstruction. A separate scoped checker independently reconstructed the difficult Gaussian filtration, inverse-Gram budget, oracle-to-physical consistency, and activity-weighted damping, then reread the complete corrected chain. A second route checked the population bias, covariance regularization, and normalized passive-query argument; its narrower scope is explicitly recorded in its response. Two bookkeeping defects were corrected: backward node errors require a cutoff-tail term, and a large input net must use separate probe programs instead of exceeding the instruction budget. No unresolved substantive defect was found in the extension relative to the current paper's foundational results. This is internal checking, not promotion approval.

Accepted proof hashes are recorded in `PROGRAM_RATE_CHECK.md`. Current paper source hashes, verified unchanged at completion:

| Source | SHA-256 |
|---|---|
| `paper/results.tex` | `6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1` |
| `paper/proof_alltime.tex` | `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d` |
| `paper/proof_tracking.tex` | `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be` |

All work is confined to this study. The paper was not edited; no Git operations, experiments, generated plots, external literature searches, or reads of other studies were performed. The next mathematical target is an algebraic-in-n rate under these same hypotheses, rather than an optimization of the deliberately conservative logarithmic exponent.
