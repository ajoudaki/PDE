# Notation normalization log

Date: 2026-09-06.

This was a notation-only editorial normalization of
`ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md`.
The complete original was read before editing. No other mathematical source
files, external sources, or other agents were used. All file writes used
`apply_patch` and were limited to the complete proof, its author snapshot,
and this log.

## SHA-256 hashes

All three files are in `/tmp/l2-two-sample-proof-0ywjpp/`.

| File | Before | After |
|---|---|---|
| `ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md` | `a3aa59799be06b90322b3825f56ed19c3f0b21d69f8a52de51518f0cfaa97586` | `910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9` |
| `ALL_ANGLE_FIRST_LAYER_COMPACTNESS_AUTHOR_SNAPSHOT.md` | Did not exist | `a3aa59799be06b90322b3825f56ed19c3f0b21d69f8a52de51518f0cfaa97586` |

The snapshot was created before changing the complete proof. A byte comparison
confirmed that it was identical to the original, and its hash was checked again
after the normalization.

## Exact classes of edits

1. **Finite raw parameter notation.** Replaced finite layer weights
   \(w^{(1)},w^{(2)},w^{(3)}\) by \(W^{(1)},W^{(2)},W^{(3)}\), including
   initial values, entries, rows, node indices, width indices, derivatives,
   increments, gradients, transpose products, reconstruction formulas, and
   parameter bounds. Replaced the full parameter tuple \(w\) by \(W\) in
   the loss, flow construction, raw metric expressions, and GD formulas.
   Wrote the width-indexed first matrix as \(W^{(1)}_n\).
   Updated the introductory convention and explicitly named
   \(W=(W^{(1)},W^{(2)},W^{(3)})\). Finite neuron fields remain lowercase;
   population coordinate fields remain capitalized.

2. **Gate notation.** Removed \(p(s)=\phi'(s)\) from (3), leaving the
   explicit formula for \(\phi'\). Replaced every gate application and
   standalone gate reference \(p\) by \(\phi'\), and every gate derivative
   \(p'\) by \(\phi''\), including the range, evenness, logarithmic
   derivative, chain rules, finite differences, population compatibility,
   and relative-gate argument. Preserved the dummy exponent \(p\) in
   \(|a_i(t)|^p\) and the outer power \(1/p\) in (2).

3. **Explicit empirical averages and array moments.** Removed the aliases
   \(\langle a_i\rangle_n\), \(\|a\|_{n,2}\), and \(\|a\|_{p;n,I}\)
   from (2). The replacement displays the empirical average directly,
   the ordinary full-array Frobenius norm divided by \(\sqrt n\), its
   empirical sum expression, and the empirical time moment directly.
   The accompanying text distinguishes the ordinary norm \(|a_i|\) of
   one two-vector from the ordinary Frobenius norm of the full array.

   Expanded every occurrence of the removed array norms in (71)–(80)
   and their intervening estimates into explicit \(1/n\) sums over
   \(i=1,\ldots,n\), with ordinary pointwise absolute values or
   two-vector norms and explicit time integrals. Preserved the domains
   \([0,T]\) and \(I_\tau\), the shifts, and the gate/node distinctions.
   Preserved outer square and cube roots for unsquared norms and removed
   those roots for squared norms. Expanded the sixth and second powers
   of the gate-ratio norms into their corresponding sixth and second
   moment integrals. In (80), the two squared translation integrals
   share one empirical sum and time integral, with their integrands added.

4. **Implicit scaling in notation-related prose.** Replaced the RMS
   descriptions surrounding (45) with ordinary Euclidean norms divided
   by \(\sqrt n\). Wrote the three scaled Euclidean increment quantities
   following (52) explicitly, and expanded the empirical RMS statement
   following (72) into a sum over pair index \(i\). Replaced the phrase
   “sixth norm” before (77) by the explicit sixth empirical time moment
   of the maximum gate difference over the two sample coordinates.
   This display restates the existing bound with the same constant.

5. **Equation layout.** Added line breaks and alignment only where the
   expanded expressions require them, including (71), (75), (77), and
   (80). All existing equation numbers (1)–(106) are unchanged.

## Verification and preserved notation

- Compared the written proof with the intended edit exactly and inspected
  the complete edit diff against the original.
- Confirmed that no finite lowercase layer weights or full-parameter
  lowercase \(w\) remain, including the matrix adjacent to \(u^T\).
  The remaining lowercase \(w\) denotes a generic comparison vector/path
  in Section 11; \(D_w\) remains the original scalar constant name.
- Confirmed that no gate \(p\) or \(p'\) aliases remain. The remaining
  mathematical \(p\) is solely the original dummy exponent in (2).
- Confirmed that no normalized empirical-average or array-norm aliases
  from (2), or implicit RMS/sixth-norm descriptions, remain.
- Preserved the ordinary, unnormalized individual path norms, population
  path norms, and \(L^1(F)\) matrix-path norm. The separately defined raw
  parameter metric and its inner product remain as in (22); they are
  not the removed neuron-array notation.
- Confirmed the identical ordered list of all 106 equation tags and
  balanced TeX braces, environments, and inline/display delimiters.
- Confirmed that (22), the constant-definition displays
  (26), (29), (33), (35), (43), (46), (47), (54), (55), (60), (69), and
  (70), all of Section 12, and the provenance appendix are unchanged.
- The edits preserve the original constants, assumptions, theorem scope,
  and proof claims. No additional result was introduced.
