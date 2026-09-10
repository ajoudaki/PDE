# Internal notation correspondence audit

Date: 2026-09-10. Auditor: `/root/signed_notation_assembly/notation_correspondence_audit`.
Assignment: bounded internal assistance to the assembler, not a fresh independent scientific or promotion review.

## Outcome and read coverage

No unresolved mathematical-correspondence correction was found in the final V2 source, SHA256 `dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc`.
This conclusion concerns the notation changes and their stated mathematical meaning. It does not newly certify the original theorem, executing implementation, historical calculation, or promotion status.

Read the original `PROMOTION_SIGN_C4.md` completely, lines 1–1687; read the complete V2 mathematical/prose content in consecutive chunks while its known corrections were being applied; then inspected every subsequent delta through the final 1736-line source. The final-to-preflight_04 comparison has no non-whitespace changes and every displayed equation is byte-identical. This was complete content coverage with explicit change reconciliation, not a claim of one uninterrupted read of a frozen V2.

Read all 657 lines of `preflight_02/original_to_v2.diff`, repairing the initially truncated combined output with a separate read. Also read all of `preflight_03/original_to_v2.diff`; inspected the complete 03→04 delta and complete 04→final delta. Independently reconstructed the 03, 04 and final sources from the original plus their unified diffs; the final 691-line diff reconstructs the live final V2 exactly.

Read all 98 lines of `docs/NOTATION.md` and the 115-line `solve-math-rigorously` skill. Startup reading also covered `RESEARCH_WORKFLOW.md`, the study README, and `docs/README.md`; the guide's initially truncated combined output was reread completely. No executing code or external theorem dependency was inspected, and no coefficient calculation or Git operation was performed. Only this assigned report was written.

## Checks and resolved findings

The original and final sources each contain 80 display blocks. Exactly 12 differ: C4.31, E2, E3, E7, E9, A5, A6, A7, the first A8 bound, the second A8 block, the untagged definition of M preceding D5, and D5. Each was compared term by term. The quadrature displays D2–D3, angular majorant A9, result bounds 8a/32/33, and exact angular constant 34 are literal-identical to the original.

Three defects in preflight_02 were reported immediately and are resolved in the final source:

- The accidental `H_a^(2)lpha^(1)` replacements now read `H_alpha^(1)` with the correct angular derivatives and lower expectation.
- The quadrature spacings accidentally changed from `h_j` to `H_j^(1)` in D2–D3 are restored. These displays now match the original literally.
- The upper derivative-Gram row's remaining bare `E` is now `E_2`.

All four changed mathematical tables were checked: the seven moment-integrand bounds, four Hessian rows, three lower primitive rows, and seven upper primitive-group rows. Activation values and first/second derivatives are consistently substituted without loss of multiplicative factors or constants. The only surviving `H`, `d`, `dd`, `h`, and `e` aliases are explicitly identified code-local arrays; mathematical derivatives use `phi'` or `phi''`. Grid spacings `h_j` remain grid parameters.

The following points received explicit checks:

1. **Population typing.** C4.31's innovation belongs to the lower population, so its covariance is correctly `E_1[Gamma_F1 Gamma_F2]`, while the source moment is `E_2[F1 F2]`. Every changed lower pairing in A5–A7 and D5 uses `E_1`; every changed upper pairing uses `E_2`. The covariance-error notation `delta E_2` explicitly means a difference of two specified Gaussian-coordinate laws, not a change in the fixed population law.
2. **Conditional-root law.** With the training rows' fourth column zero, all training factors are measurable in the first three independent roots. Integrating the fourth root gives exactly the six listed groups, with 3+6+3+1+3+1=17 distinct values. The normalized integral for `E_gamma_4` has no missing variance factor: it integrates a standard root through `m_x+sigma_x z`, including `sigma_x=0`. The distinction between the exact Q law and a dyadic factor's own `E_gamma` law is retained, and covariance discrepancy is still charged. No lower/upper population independence is introduced.
3. **Index correspondence.** The bijection sends mathematical training indices 1,2,3 to array indices 0,1,2 and passive x to 3. Thus the passive mean/scale use row 3, labels p1,p2,p3 map to tokens p0,p1,p2, and row-major tensor offset `64 iota(a)+16 iota(b)+4 iota(i)+iota(j)` is correct. This checks the supplied interface specification, not unseen code.
4. **Tensor and scalar names.** `mathcal T_abij` continues to denote the lower fourth-order tensor of C4.27, separately from the lower field T_x. The scalar functions `mathcal F(alpha)` and `mathcal B(alpha)` reproduce the old scalar F_x and B_x terms with coefficients 4 and 4/3 unchanged; they do not replace the dynamic field F_x(t) or backward field B_b. Both terms of each reverse response remain present. M_bj is deterministic and mu_b is a lower-population field.
5. **Conservative P.** The exact label norm is `(1+sqrt(5))/6<27/50`: equivalently `sqrt(5)<56/25`, whose square follows from `5<3136/625`. Defining P as 27/50 increases only nonnegative upper bounds. The signed p_a in S and the coefficient are unchanged, and both the exact and supplied label norms remain required to lie below P. All affected strip, covariance, label-error and derivative inequalities are monotone in P. A9 already used 27/50 in the original, and its value and the final rational enclosures are unchanged.
6. **Final arithmetic clarification.** Replacing the loose `|phi''|<=2` in the arithmetic-integrand paragraph by `|phi''|<=1` invokes the existing E7 proof, where the maximum is `4/(3 sqrt(3))<1`. It validly exposes the unit bounds on exact factors used by the subsequent existing telescoping estimate. No arithmetic error budget changed.
7. **Scope and hypotheses.** The model, labels, initialization, loss normalization, fixed design, local horizon, fourth-order remainder, matching-clock conditions, positivity division, beta premise, compiler/runtime contracts, singular-covariance treatment and finite-width limitations remain intact. Renaming cubature dimension d to q does not change the network's fixed input dimension. The specified lower-root reflection with exchange of training indices 2 and 3 correctly explains the same parity identities and does not alter the circle rule.

Two prose edits refer to implementation bounds supplied below and checked arithmetic contracts instead of prospective inspection. They reconcile with the original theorem and evaluated-certificate section; they are not merely literal renamings. Their execution/provenance claims were not newly verified in this bounded audit. The independent scientific and integration review requirements remain separate.

## SHA256 input record

| Source | SHA256 |
|---|---|
| `studies/two_layer_test_risk/PROMOTION_SIGN_C4.md` | `ae5eff6e5c351410355048f56f8b429383612cbf30558178069e0f8692b2025f` |
| Initial V2 / preflight_02 | `707979871b1440c87c78e100a7640bd0d4b3b995c1edcdb1583d553c09018dee` |
| V2 / preflight_03 | `9bf6a602bf2f9d9e7c1c197733d3b937afeeab8cb28e3f68ee065863c64d9aa8` |
| V2 / preflight_04 | `1edd07e0248343be52683523e52e7a9c703c6e0c38b591181bf2f1916a4eaddc` |
| Final `PROMOTION_SIGN_C4_V2.md` | `dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc` |
| `preflight_02/original_to_v2.diff` | `0440d7ff812f9c6cad0f5b7f5ebba5a02640f153b2256bb3b0a7511a22ee721b` |
| `preflight_03/original_to_v2.diff` | `15bb1ea82faff905ecfb528d33122341f0b6964aa53c0c9e7306ab84d01bc275` |
| `preflight_04/original_to_v2.diff` | `74ffd3871896411013697c442cdd9116a4022af7c892e023277d44d6d26e53b6` |
| `final_02/original_to_v2.diff` | `5bd1d2cd392fa1226c7083e52a385e5ee9505ba5fe47bb175cc2f5b2452e85f7` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `RESEARCH_WORKFLOW.md` | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| `studies/two_layer_test_risk/README.md` | `5049d0ecb7fcf0bb349adcbcf39ff8b24466b33b78868749c8b02e241ac0652e` |
| `docs/README.md` | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |

Diff paths above are relative to `data/generated/two_layer_test_risk/signed_notation_20260910_01/`. The read-only checks used exact text reconstruction, SHA256, display-block extraction, alias searches and manual mathematical comparison. No promotion verdict is implied.
