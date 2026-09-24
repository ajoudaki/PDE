# Packet 010 Sol preservation audit: consolidated corrections

Verdict: **FAIL; correction required.** I reviewed all 1,568 source lines, 953 edits, 108 target proposals, all reference destinations, and a separate residual scan. Exact replay/native-TeX preservation and the 35 focused tests pass; no rendering was performed.

The complete machine-readable correction list is `data/generated/quarto_capability_pilot_20260921/packet010-audit/sol_correction_ledger.json` (SHA-256 `ad44bad33915a8e45e468ec3fa30b3b5e61ba1749422136704662b2ba6f50f92`). It records 258 specific inline edits requiring semantic TeX, 76 residual-math source lines, 11 reference corrections, and five exact new targets. The other 119 inline transcriptions and all unlisted edits/targets are accepted.

For every listed transcription, replace pseudo tokens with mathematical TeX while preserving the source expression: Greek symbols, `\sqrt`, `\exp`, `\sum`, `\prod`, `\log`, `\tanh`, `\cosh`, norms, expectations/probabilities, adjoints, spaces, multi-character indices, `\mathcal`/`\mathbb`, and `\infty`. For example, source 6343 must be `$\|\Delta\delta\|_2+C\|\Delta H^1\|_2$`; `A*` means `A^*`; `C1` means `C^1`; and `o_P(1)` means `o_{\mathbb P}(1)`.

Apply every reference correction exactly as recorded. In particular, source 6428 targets local subsection 6190; restore the four C.4.6.T/P/S/F label families as prose; and convert both endpoints of every listed range. Typeset every omission span in place, using the surrounding source to retain its exact role.

## Surgical review of the first corrected bundle

All unlisted corrections and the five added targets are accepted. Apply this complete bounded follow-up:

- 6466–6467: attach primes inside the source subscripts: `\xi_H-\xi_{H'}` and `\zeta_\delta-\zeta_{\delta'}`.
- 6554: use `\operatorname{clip}_R(q)`; include `clip` in the retained-ASCII operator guard and focused test.
- 6623 and 7013: `E_1` is expectation, `\mathbb E_1`.
- 6666: restore the second argument exactly as `\phi'(\bar z)`, not `\phi'(z-\bar z)`.
- 6770: both changed `Z1` occurrences are `Z^1`, not `Z_1`.
- 6828: use `c_{j+1}` and `e^{2(T+1)}`.
- 6938 and 6940: the fixed reference is `\nu_*`, not `\nu^*`.
- 6987, 7061–7062, and 7570: the norm subscript is `\mathcal V`.
- 7069: convert the trailing endpoint `2` in C.4.5.1–2 to `@sec-docs-global-nonlinear-l6104`.
- 7328: use `(H^1)^2-(H^2)^2`; the current `H^1^2-H^2^2` has double superscripts.
- 7373: replace `\mathbb \mathbb R^2` by `\mathbb R^2`.
- 7392: use `\Gamma^{j-1}`.
- 7432: use `d_{\mathrm{ref}}`.
- 7483 and 7541: the operator is `\mathcal B`, so use `\|\mathcal B(t)v\|` and `(\int\|\mathcal B\|)^j/j!`.
- 7576 and 7590: `w dot u` is the dot product `w\cdot u`, not `w\dot u`.
