# Internal follow-up review: small feature-weighted readout noise

2026-09-19. Theoretical review; no experiments and no promotion.

**Verdict: PASS for the corrected candidate SHA256 `98449a65152741f0880371828d91e16e0edeb61781b1c64158a661b3bcf9ee35`.** The inverse-free proposal, deterministic confinement, history-uniform success lower bound, expected and almost-sure rates, physical perturbation estimate, elapsed-clock bounds, and strong state endpoint are valid. One missing accuracy range in the original submitted version was reported and repaired before completion. No unresolved correctness objection remains for the stated scope.

## 1. Provenance, inputs, and correction

Reviewer: `/root/review_readout_rate`, the reviewer of the original prediction-isotropic candidate, now acting under a separate follow-up assignment. The supervisor had previously sent an informal inverse-free proof sketch after the first review was finished. That exposure is disclosed: this is informed internal checking, not a fresh isolated or promotion review. I recomputed the inequalities and checked the full persisted argument rather than relying on the sketch. No other rate-route candidate, study, or review was consulted.

Permitted scientific inputs were `RATE_SMALL_READOUT_NOISE.md`, corrected `RATE_ADAPTED_READOUT.md`, and the exact model/initialization dependencies already authorized for the earlier review. The new candidate was read completely both before repair, lines 1–248, and after repair, lines 1–249. The corrected main candidate was reread completely, lines 1–356. The previous complete reads of the dependencies and canonical ranges remain applicable: their SHA256 values were verified unchanged. The coverage was `ESCAPE_AND_LIMITS.md` 1–345, `INITIAL_EXCLUSION.md` 1–401, authorized `INITIAL_REVIEW.md` 1–142, `NOISE_GLOBAL_PROGRESS.md` 1–328, `docs/NOTATION.md` 1–98, and `docs/global_nonlinear.md` 13161–13786 and 15146–15528. No scientific source outside these scopes was fetched.

The `solve-math-rigorously` skill and shared process instructions remain applied. `AGENTS.md` was reread and its hash, together with that of `RESEARCH_WORKFLOW.md`, was verified unchanged. No experiments or numerical probability calculations were run. The only Python operation was an in-memory textual reverse substitution and hash comparison to verify the exact amendment; it did not modify a candidate. Only this report and the expressly authorized closure addendum to `RATE_READOUT_REVIEW.md` were written. No Git mutation was performed.

Original submitted small-noise hash: `7e0f2c06f479edf7506fe684516c31fb67858458470edd8797054728491c4fd5`. The hitting-time statement preceding (6) did not specify `0<epsilon<L0`. For `epsilon>L0`, its ceiling can be negative while the actual number of required proposals is zero. I promptly requested either the missing range or a nonnegative truncation of the ceiling. The author added exactly `For 0<epsilon<L0` to that sentence. Complete rereading and reverse-substitution hashing verified that this was the only change and recovered the original hash. The repaired hash is the one in the verdict. The inherited elapsed hitting-time statement uses the same `J_epsilon`, so its range is now fixed as well.

The corrected main dependency explicitly imposes binary labels. Its original loss-one normalization objection is closed in Section 8 of my earlier report. No reliance on an unfixed main-candidate objection remains.

## 2. All-history confinement transfers correctly

The fixed physical Hilbert metric, unhalved loss, exact populations and actual transpose remain those of the supplied closure. For the observation map, `K=AA*` is symmetric and positive, and

\[
\|K\|\le\operatorname{tr}K=\sum_i\mu_i E H_i^2\le1.
\]

Thus `0<kappa<=1/2`, and the proposed `theta=1-kappa^2/(4m)` lies strictly between zero and one. All constants in the main candidate's deterministic schedule are finite and its duration `h` is strictly positive for this choice.

Every proposed readout increment lies in `range(A*)`. For `z=A*v`,

\[
\|Az\|^2=v^TK^2v\ge\kappa v^TKv=\kappa\|z\|_2^2
\]

whenever the current hidden state is in the tube. Accepted fractional reduction gives `|A delta c| <= (1+sqrt(theta))sqrt(ell)` and hence exactly the accepted-jump norm bound required by the main proof. No Gram inverse is needed to evaluate the proposal or to establish this estimate.

The inherited proof can therefore be run up to a hypothetical first exit: kicks leave hidden fields unchanged; stage losses obey `ell_j<=theta^j L0`; the sum of accepted readout norms is at most `(1+sqrt(theta))R_*/sqrt(kappa)`; the readout flow travel is at most `2h sqrt(theta)R_*`; and the full hidden travel is at most

\[
2Bh\overline C(1+\overline M)\sqrt\theta R_*\le\rho/2.
\]

The current readout remains bounded by the same `Cbar`. Hidden travel cannot reach radius `rho`, so the same operator perturbation estimate preserves `K>=kappa I` for every finite accepted history. This does not condition on a favorable random event. Rejected candidates, however large, never enter the state. All original hidden gradients remain active during every GF interval, and the existing whole-Hilbert continuation proof supplies each interval without a pointwise boundedness assumption on `w` or `c`.

If a certified positive lower bound `b<=lambda_min(K0)` replaces `kappa0` everywhere, the tube gives `||K-K0||<=b/2` and consequently `lambda_min(K)>=lambda_min(K0)-b/2>=b/2`. Thus the final paragraph's smaller-certified-bound alternative is valid, provided the same replacement is made consistently in all schedule constants as stated.

## 3. Gaussian event and non-independent success analysis

At a held state, the exact output increment is `A delta c=eta sqrt(ell) K G`. For the unit residual vector `v=e/sqrt(ell)`, the exact loss ratio is

\[
1+2\eta (Kv)\cdot G+\eta^2|KG|^2.
\]

Because `K>=kappa I`, `|Kv|>=kappa`; its direction is therefore defined. Decompose the isotropic Gaussian along this direction and its orthogonal complement. The component in `[-2,-1]` has probability at least `exp(-2)/sqrt(2pi)`. The independent orthogonal squared norm has mean `m-1`, so its event of being at most `2(m-1)` has probability at least one half for `m>1`; it holds surely for `m=1`. The combined event has probability at least `q_*` in every dimension and at every history.

On that event, `(Kv) dot G<=-kappa` and

\[
|KG|^2\le|G|^2\le4+2(m-1)=2m+2\le4m.
\]

Substitution of `eta=kappa/(4m)` gives

\[
1-2\eta\kappa+4m\eta^2
=1-\frac{\kappa^2}{4m}=\theta.
\]

This event proves the lower bound on acceptance. It is not used to sample the proposal, so there is no residual-direction steering. The law `G~N(0,I_m)` remains centered and independent of the past. The actual acceptance probability can depend on `K` and `v`, and the candidate correctly avoids asserting independent or identically distributed success indicators.

Writing `p_k` for the conditional success probability, `p_k>=q_*`. Rejection preserves `L_k`; acceptance and its following flow give loss at most `theta L_k`. Therefore

\[
E[L_{k+1}\mid\mathcal F_k]
\le (1-p_k(1-\theta))L_k
\le(1-q_*(1-\theta))L_k.
\]

Iteration proves (5) without a Bernoulli product formula or an independence assumption. While one stage is held, its independent trials have fixed probability `p(S)>=q_*`, so its conditional mean waiting time is at most `1/q_*`. Each of the first `J_epsilon` stages has this conditional bound. Summing and using `-log(1-kappa^2/(4m))>=kappa^2/(4m)` proves both bounds in (6) for the now-declared range `0<epsilon<L0`. Earlier success due to extra GF decrease only shortens the actual hitting time.

Markov's inequality gives the stated high-probability loss bound. At threshold `L0 exp(-a k)`, its right side is `exp(-(q_*kappa^2/(4m)-a)k)`, a summable sequence for the declared `a`. The elementary first Borel–Cantelli implication therefore proves the eventual almost-sure rate. No independence of those exceptional events is needed.

## 4. Physical size and admissible information

In the unchanged physical `L2` readout metric, the conditional covariance is exactly

\[
\ell\eta^2 A^*A,
\]

and the finite-rank trace identity gives

\[
E[\|\delta c\|_2^2\mid S]
=\ell\eta^2\operatorname{tr}(AA^*)
\le\frac{\ell\kappa^2}{16m^2}.
\]

Thus the declared smallness is an actual conditional second-moment bound on proposed physical increments, not an output-space bound mislabeled as a parameter bound. In particular, its conditional RMS is at most `sqrt(ell) kappa/(4m)`. The statement correctly distinguishes this from a deterministic support bound: Gaussian proposals remain unbounded.

The covariance is for trials, rather than the law conditioned on acceptance. This distinction is stated accurately. As an additional check, the latter also obeys

\[
E[\|\delta c\|_2^2\mid S,\mathrm{accept}]
\le\frac{\ell\kappa^2}{16m^2q_*},
\]

because its acceptance probability is at least `q_*`. This is not needed for confinement, which already uses the deterministic accepted-step bound.

The proposal evaluates only a weighted random linear combination of current features; it has no inverse-Gram or fitted-readout step. Its scalar choices require a starting Gram eigenvalue or certified positive lower bound, and exact current loss/features are still required. The theorem does not furnish a geometry-independent lower bound for that eigenvalue or a numerical cost guarantee for obtaining it. Those are retained scope limits, not unstated assumptions about a fitted endpoint. The field metric does not change or degenerate with time.

## 5. Endpoint and elapsed time

At every held stage, the probability of more than `n` failed proposals is at most `(1-q_*)^n`. Each stage therefore finishes almost surely, and a countable intersection proves completion of all stages unless exact fitting terminated the process. Invertibility of `K` makes exact fitting by a positive-loss Gaussian proposal a measure-zero event; local uniqueness prevents the GF interval from first hitting an equilibrium at finite time. The terminal convention is nevertheless harmless.

Summable accepted readout jumps and summable full-GF travel make the entire actual-state path Cauchy in the complete physical Hilbert state space. Since infinitely many completed stages force their losses to zero and loss is continuous in that topology, the strong limiting state is finite and fitted. Waiting on rejected trials leaves the state constant, so it causes no additional endpoint issue. This argument controls neutral coordinates by total travel; it does not replace strong compactness with mere boundedness.

Each trial and optional following GF segment takes at most `Delta+h` under the declared hybrid clock. By time `t`, at least `floor(t/(Delta+h))` such units have completed, unless fitting already terminated the process. Loss monotonicity and (5) imply (14). The expected time to complete `J_epsilon` successes is at most `J_epsilon(Delta/q_*+h)`, proving the expected elapsed hitting bound. The associated tail bound, although not separately displayed in this candidate, also follows directly as

\[
P\{\tau_\epsilon>t\}
\le\min\!\left\{1,\frac{L_0}{\epsilon}
\exp\!\left[-\frac{q_*\kappa^2}{4m}
\left\lfloor\frac{t}{\Delta+h}\right\rfloor\right]\right\}.
\]

Rejection costs and full original GF durations are counted. `Delta` is explicitly an assigned exact-oracle cost, not measured computational time for population integration. Infinitely many successes with the fixed positive `h` imply infinite accumulated GF physical time almost surely even though the path length is finite.

Canonical order-one and order-two initial Gram positivity uses exactly the already-checked full-correlation, positive-ridge feature-independence proof. The candidate does not claim unconditional canonical order-three positivity; it invokes the explicitly optional data-only hidden reset. That reset remains a change of starting hidden state. Both variants limit accumulated hidden travel deliberately. No conclusion is asserted for unmodified GF, minibatch SGD, unrestricted hidden trajectories, or unbounded-time neural-width approximation.

## 6. Input versions and completion

| Input | SHA256 |
|---|---|
| Small-noise candidate before repair | `7e0f2c06f479edf7506fe684516c31fb67858458470edd8797054728491c4fd5` |
| Small-noise candidate, final reviewed version | `98449a65152741f0880371828d91e16e0edeb61781b1c64158a661b3bcf9ee35` |
| Corrected `RATE_ADAPTED_READOUT.md` | `1e1ad47811a41d9f09d625746c7b4bc6f95857a1a08521a80b4c80bf9dfb610b` |
| `ESCAPE_AND_LIMITS.md` | `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2` |
| `INITIAL_EXCLUSION.md` | `34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c` |
| `INITIAL_REVIEW.md` | `6fd58a9faa1b07a0eaa53fe9595b63180b225e72df35a7f50fe9f6e629d64baf` |
| `NOISE_GLOBAL_PROGRESS.md` | `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `AGENTS.md` | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |

The model/dependency hashes matched the original complete-read review throughout this follow-up. Shared checkout HEAD at the metadata check was `976690bcd0f173171e8b73f4ad28dfcfb81cac56`; the index contained no staged paths. The sole objection to the original new candidate was the missing accuracy range, now closed. All assigned theoretical checks are complete for the corrected version. This report supplies internal checking only and is not an independent promotion gate.
