# Supervisory audit of the arbitrary-depth rewrite

Date: 20 August 2026.

## Verdict

The canonical exposition is approved subject to the claim boundary in
`CANONICAL_NOTE.md`.

The audit found no scaling error, counterexample, or inconsistency in the
rooted-path equation.  It did find one material overclaim in the earlier
manuscript: compact-positive-time finite-width convergence was presented as
proved for every fixed hidden depth, although the multi-edge Gaussian-word
and coefficient-lift lemmas were only sketched.

The corrected status is:

| Claim | Verdict |
|---|---|
| Exact normalized finite-width chain and kernel | pass |
| Balancedness invariants | pass |
| Deterministic rooted-path ODE / counting-measure IDE | pass |
| Internal output and loss identities | pass |
| Global well-posedness and exponential residual decay of the path ODE | pass |
| Positive-time finite-width identification for hidden depths 1 and 2 | pass |
| Positive-time finite-width identification for hidden depth at least 3 | conditional; proof incomplete |

## Independent checks

Three independent passes were used:

1. A canonical-notation and pedagogy pass checked that the general-depth
   note follows the structure of the supplied two-hidden-layer note and does
   not confuse rooted-word labels with physical paths or probability points.
2. A hostile mathematical pass rederived the normalized chain, the kernel,
   the energy estimate, the global decay argument, and the low-order Taylor
   coefficients.
3. A proof-completion pass attempted to close the arbitrary-depth width
   theorem.  It confirmed that ODE stability is sufficient once the random
   matrix lemmas are assumed, but that the necessary multi-edge Wick
   enumeration is absent from both the local proof attempt and the published
   arbitrary-layer discussion.

## Precise remaining obligation

For every fixed path cutoff, one must prove the Gram, forward-action, and
transpose-action estimates (6.3)--(6.4) of `CANONICAL_NOTE.md`, followed by
the trained-block lift consistency (6.6).  Those statements imply the
conditional compact-time theorem through the dimension-free energy bound
and Picard estimate in Section 9.

## Regression result

The exact test suite now contains four tests.  It checks finite directional
derivatives, rooted-source initialization, the depth-one closed form, and an
exact rational Taylor recurrence.  The latter reproduces

\[
\begin{array}{c|rrr}
L&f'(0)&f^{(3)}(0)&f^{(5)}(0)\\ \hline
1&2&8&32\\
2&3&48&1464\\
3&4&160&13888.
\end{array}
\]

Result: `4 passed`.

## Supersession

`CANONICAL_NOTE.md` is the authoritative formulation.
`THEOREM_AND_PROOF.md` is retained only as an archived proof attempt and now
contains a prominent correction.  The local and parent evidence ledgers have
also been revised so they no longer classify the hidden-depth-three-and-above
positive-time width limit as proved.
