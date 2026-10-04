# Internal check of the three-error synthesis

Date: 2026-10-01. This is a bounded internal consistency check, not a promotion review. The full finite-tail reconstruction in FINITE_TAIL_CHECK.md is reused. The checker also read the complete current CUTOFF_REMOVAL_ROUTE.md and the complete synthesis and probability-transfer note.

**Verdict: PASS for the three-error reduction, probability statements, and separation of the unresolved width estimate.** The two minor presentation qualifications identified on the first pass have been corrected and their replacement paragraphs checked. No strict or near-root trained dense width theorem is asserted by the checked synthesis.

## Read coverage and frozen hashes

| File | Coverage | SHA-256 |
|---|---|---|
| RESULT.md | Complete, 124 lines; revised setup and one-return paragraphs reread | aaea301f9563980706e967811a44306c6a5156d9a8bb45f9c2e39d5f3debb8c8 |
| THREE_ERROR_REASSEMBLY.md | Complete, 169 lines | b66b678ea0a568fa134341b82c2fd69cdaf2c98e54611a42e87c74a1bcb7ee7f |
| CUTOFF_REMOVAL_ROUTE.md | Complete, 789 lines; reread in complete ranges after initially truncated tool output | 78ab82a56f3adb18f4462b4f59b6328f072d04bcdff85fe6cf48d089f873d300 |
| FINITE_TAIL_ROUTE.md | Complete read and reconstruction in the preceding check | da251f231832e69c74581ba4291e649d1322737eebd46b2a4d9c6ca1a8dd0d65 |
| FINITE_TAIL_CHECK.md | Prior independent internal reconstruction reused | 214ebe24e007563ccac1979b0db01b93f6d9cc2d03ff00b499df3c7cd22b7308 |

Required canonical-notation and rigorous-proof skills were already read completely and remain applied. Their hashes and the allowed manuscript coverage are recorded in FINITE_TAIL_CHECK.md. No other study, numerical experiment, or code test was used. The detailed third-derivative claim attributed to FIRST_FEEDBACK.md was not re-audited in this bounded assignment; it is not used by any cutoff-removal or three-error inference checked here.

## Three distinct errors

The same smooth backward cutoff, unchanged forward map, unchanged readout update, zero initialization of the readout, and canonical mobilities are used in all three comparisons. The cutoff population is constructed on the common initialized operator spaces. Its identification as the fixed-cap finite limit is qualitative and is not used as a numerical width estimate.

For \(M\ge1\), the cutoff route proves the deterministic all-time population estimate

\[
 \mathcal E_\mu(f_{\infty,M},f_\infty)\le C_\mu e^{-cM^2}.
\]

Its assumptions match the manuscript's activation class at every fixed depth and include a positive initial feature-Gram gap and a small fixed label threshold independent of the cap. The comparison uses the true derivative response in one factor of the mixed residual matrix and the clipped update response in the other. The synthesis correctly does not describe the clipped dynamics as a gradient flow.

The finite-tail theorem applies only to two hidden layers, orthonormal training inputs, first activation tanh, and bounded second activation with bounded Lipschitz derivative. On the fitting event, it gives

\[
 \Pr\{\mathcal G_n,\ \max_{a,i}\sup_t|k_{a,i}^{(1)}(t)|>M\}
 \le Cmn e^{-cM^2/S^2},
 \qquad \sup_t\|w(t)\|_\infty\le BS.
\]

For fixed positive \(S\le1\), a constant \(A\) depending on the fixed confidence and model parameters makes \(M_n=A\sqrt{\log(e+n)}\) large enough for finite inactivity. Increasing \(A\) also makes \(cA^2\ge1/2\), which bounds population cutoff removal by \(C_\mu/\sqrt n\). The same deterministic sequence of caps can satisfy both requirements.

Equality of finite parameter trajectories on the inactivity event implies equality of predictors for every input, not just the training set. Hence the synthesis correctly obtains

\[
 \mathcal E_\mu(f_n,f_\infty)
 \le 0+\mathcal E_\mu(f_{n,M_n},f_{\infty,M_n})
          +C_\mu/\sqrt n.
\]

The middle term is explicitly unproved. Fixed-cap qualitative convergence does not control it at the growing sequence \(M_n\), and a hypothetical multiplier \(e^{CM_n}\) would be unbounded. The synthesis explicitly says that even the resulting conditional near-root arithmetic is not an established trained dense rate.

The finite-second-moment input assumption is enough: the population and finite parameter comparison estimates majorize the pointwise time supremum by a constant times \(1+\|x\|/\sqrt d\), and this is squared only when integrating. The order of supremum and input integration is preserved.

## Probability accounting

RESULT.md states finite inactivity with failure probability at most
\(\delta+\Pr(\mathcal G_n^c)\). This is the correct unconditional bound from the event-restricted tail theorem. To formulate total failure at most a prescribed \(\delta_{\rm tot}\), apply the tail theorem with budget \(\delta_{\rm tot}/2\), then take width large enough that
\(\Pr(\mathcal G_n^c)\le\delta_{\rm tot}/2\). No numerical rate for the latter probability is supplied or needed for this asymptotic confidence statement.

THREE_ERROR_REASSEMBLY.md keeps its finite error probability intersected with \(\mathcal G_n\); it does not mistakenly replace that probability by a conditional law given the event.

## Conditional moment transfer

The probability-transfer lemma is correct. Its finite-network exponential-moment premise is explicitly an assumption, not a consequence of population tails. The pointwise estimate

\[
 v^2\mathbf1_{\{|v|>M\}}
 \le\frac{2}{be}e^{-bM^2/2}e^{bv^2}
\]

gives an event-restricted second-moment bound on the summed RMS carrier tails. The deterministic residual envelope then yields

\[
 Z_n(M)^2
 \le\frac Y\kappa\int_0^\infty
       Ye^{-\kappa t}\mathbf1_{\mathcal G_n}H_n(M,t)^2\,dt.
\]

Tonelli proves \(\mathbb EZ_n(M)^2\le Ce^{-cM^2}\), without temporal or neuronal independence. The finite deterministic comparison from CUTOFF_REMOVAL_ROUTE.md, with its two thresholds set equal, gives

\[
 \mathbf1_{\mathcal G_n}\mathcal E_\mu(f_n,f_{n,M})
 \le C_\mu e^{KM}Z_n(M).
\]

The Gaussian quadratic decay absorbs this linear exponential after squaring. Markov then gives the stated event-restricted root-width cutoff-removal probability at a sufficiently large logarithmic cap.

A single fixed \(2p\)-moment instead gives only \(M^{-2p+2}\); the note correctly distinguishes this from a width power at \(M\asymp\sqrt{\log n}\). The proposed telescoping criterion is clearly conditional on full population-centered increment bounds, a base-case bound, and convergence of cutoff limits. It is not presented as a theorem already established for dense training.

## Clarifications verified in the final RESULT.md

The initial pass identified two minor qualifications. Both are now explicitly addressed in the checked final version:

1. The setup states that \(Y=0\) gives stationary initialized flows and zero comparison error. It restricts subsequent division by the activity bound to \(Y>0\).

2. The one-return paragraph now gives the exact \(u_i u_j/n\) factor in the second-moment correction and asserts \(O(1/n)\) for the bounded tanh coordinates used in the application. It also qualifies the root-width coupling by its moment assumptions.

I reread both changed passages. There are no outstanding synthesis issues within this check's scope. General-data finite tails and the growing-cap finite-to-population comparison remain open, and no slower-than-root lower bound is claimed.
