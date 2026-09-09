# Primary-paper reading record

Author/auditor preparation date: 2026-09-07.

Primary source: Greg Yang, *Tensor Programs III: Neural Matrix Laws*, [arXiv:2009.10685v3](https://arxiv.org/abs/2009.10685v3), revised 8 May 2021. [Primary PDF](https://arxiv.org/pdf/2009.10685v3).

Local downloaded files:

- `literature/yang_tensor_programs_iii.pdf`, 87 pages; SHA-256 `6b0d6504c12373e6837de0aff5ab77bb18675a225fcda10d59b56540ec74b5da`.
- `literature/yang_tensor_programs_iii.txt`, layout-preserving full extraction, 6,338 lines; SHA-256 `7da471803779bc2f584cf34b262b47d353ec98181c4ffaa88f4d18b2571648d7`.
- `literature/yang_p86.png`, visual check of the original PDF page containing Appendix N.3's normalization display.

## Actual reading coverage

The full paper was read, including its main text, references, and every proof appendix A–N. The complete extraction was displayed and read in the following untruncated intervals:

| Extracted lines | Coverage |
|---|---|
| 1–429 | Opening material and program setup |
| 430–650 | Source definitions and main theorem |
| 651–1071 | Main applications |
| 1072–1574 | Main proof discussion, remaining main text, references |
| 1575–2054 | Appendices A–E.2 |
| 2055–2147 | Remaining E.2, E.3, beginning F |
| 2148–2600 | F–H.2 |
| 2601–3027 | Remaining H, I–J |
| 3028–3511 | K.1–K.3 |
| 3512–3900 | K.4 and beginning K.5 |
| 3901–4304 | Remaining K.5 and opening L |
| 4305–4752 | L.1–L.4.2 |
| 4753–5236 | Remaining L.4, L.5–L.6 |
| 5237–5725 | L.7 through early L.7.3 |
| 5726–6181 | Remaining L.7 and M |
| 6182–6338 | N, through the paper's final line |

An earlier batch was truncated by tool-output limits; its missing portions were subsequently displayed and read in the intervals listed above. The statement of full coverage relies on those complete reads, not on a search hit, theorem excerpt, or file download alone.

## Substantive cross-check and dependency decision

Box 1 and Remark 2.11 support the formal expression derivative convention. Lemmas K.8–K.9 supply the same conditional Gaussian projection geometry; L.8–L.10 exhibit the response cancellation. Theorem E.15 and Appendix N address rank loss for broader pseudo-Lipschitz programs. The present chapter instead proves its smooth fixed-program W2 result by independent input noise and an operator bound, so it needs neither CoreSet nor the high-moment weakly correlated Gaussian theorem.

The displayed normalization in Appendix N.3, PDF page 86, uses h^0 divided by a normalized squared residual norm; as printed, it does not yield the stated orthogonal unit-norm input. This was checked visually in the PDF. No conclusion about the broad theorem is inferred from that isolated typographical issue. It reinforces that the manuscript must contain its own complete specialization. At singular covariance, agreement of correction vectors is the pertinent invariant, not agreement of every off-support derivative entry.

No external result is load-bearing in `FOUNDATIONS_CHAPTER.md`. Accordingly none of the paper's references is recursively invoked by that chapter; its used mathematical steps are proved directly there.
