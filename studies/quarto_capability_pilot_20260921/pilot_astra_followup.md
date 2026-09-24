# Bounded correction verification: linear-opening pilot

**Verdict: PASS for preservation of the corrected frozen excerpt.** The previously reported theorem-boundary error is fixed. The only other candidate changes are the authorized display-whitespace corrections. No further preservation correction is required by this check.

Date: 2026-09-21. This is a bounded verification following my complete initial read and independent audit, not a new isolated scientific review. The original report and original scratch scripts/results remain unchanged. I read no root verdict, worker report, study history, or other study, and edited no candidate or input. Rendering remains outside this verification.

**Coverage and frozen identities**

The corrected packet is `data/generated/quarto_capability_pilot_20260921/pilot03/audit_inputs/`. I manually read the entire exact old/new candidate diff, the complete nine-line `hashes.json`, the complete 99-line `future_instructions_v2.md`, and its complete diff against v1. I also reread corrected candidate lines 130–157 around the repaired theorem boundary.

The source, manifest, v1 instructions, configuration, and index were already read completely in the initial audit. Byte-for-byte comparisons confirm that those five inputs are unchanged. The complete 916-line corrected candidate was processed by the independent full-text, math, reference, and environment checks against all 907 source lines. I did not manually reread every unchanged candidate line in this bounded follow-up; the initial full read, exact complete diff, byte identity of the other inputs, and full mechanical checks provide the coverage stated here.

All seven file digests in the new `hashes.json` match their actual bytes. All six source-block digests also match the manifest.

| Input | SHA-256 |
| --- | --- |
| `pilot_source.md` | `3217f65ee957581085b6152c5ab6d59b1a62b3c9470bc48003908cbae55b1db7` |
| `pilot_linear.qmd` | `86bc7accfde529da616fba82407e79e5b98b5c72a045468ba99caa7aaae3ce73` |
| `pilot_manifest.json` | `efbce69c35a87c4c28434eb1b4e82e99fbc1edb5a915d4834df16ab43959e5e4` |
| `pilot_instructions.md` | `794cecd4f165596394dd255c5353d0a1ab163d67d24250fd5ee3c12977f77564` |
| `pilot_quarto.yml` | `993b22465798a0c6699db06d67ea34fb221f0724e989d5d073b44d96d77592fd` |
| `pilot_index.qmd` | `5ac86fb0ce6cd4381a1567f75833cca56aa35c8d11f3371298e414de2ba4de8e` |
| `future_instructions_v2.md` | `ce09df6b9aa357fc1477fa8ab78e1af67926ae2fa5ae65bf8d1a7875424ddefe` |
| `hashes.json` | `0862e6c7b5c9be712da01065a2e8057c0198ccf897cead7a18d2b6ed2e5b72e2` |

The last digest records `hashes.json` itself; no independent expected digest for that file is supplied. The old candidate identity remains `d6f78030984d9932be8e01d690dfb9e33f2cfa42443612829d88764b52fe361b` in the original report.

**Exact correction checks**

I independently reconstructed the corrected candidate from the old candidate using only these operations and asserted exact equality, including line endings, to the actual new file:

1. Move the theorem's closing fence and adjacent blank line from old candidate 149–150 to before the roadmap. The corrected fence is at line 143, following the final theorem sentence at 141. The roadmap remains verbatim at corrected lines 145–149 and lies outside every statement/proof environment.
2. Add 18 blank lines outside nine displays in the trace-class section so each opening and closing delimiter is separated from surrounding prose.
3. Remove the single whitespace-only line formerly at old candidate 386, left after deleting the indented tag-only source line 390. No substantive equation character is removed.

No other candidate changes occurred. All 49 corrected displays now have blank lines before and after them, and none has an internal blank line. This asserts the requested source syntax; it does not assert a rendered result.

**Complete independent check results**

| Check | Result |
| --- | --- |
| Complete prose/qualifier/emphasis/order comparison under allowed transformations | PASS; empty lexical difference |
| Inline mathematical expressions | PASS; all 316 match exactly |
| Display mathematical expressions | PASS; all 49 match individually and in order after only authorized tag-line removal |
| Equation identities | PASS; 45 correctly matched labels and four unnumbered displays |
| Reference destinations | PASS; all 63 occurrences resolve to the preserved intended objects, with no old in-scope reference syntax remaining |
| Native IDs and mapping | PASS; 55 unique IDs, six correctly ordered block markers, unchanged heading hierarchy |
| Statement and proof membership | PASS; all seven environments have their exact required original spans |
| Pending references, resource link, and partial-edition wording | PASS; unchanged from the reviewed packet |

The corrected environment membership is:

| Environment | Corrected candidate fences | Original content span |
| --- | --- | --- |
| Population theorem | 89–143 | 91–143 |
| Gaussian-word lemma | 231–253 | 237–256 |
| Gaussian-word proof | 255–337 | 258–341 |
| Trace-class lemma | 381–412 | 386–409 |
| Named singular-expansion proof | 414–574 | 411–556 |
| Fitting corollary | 704–710 | 691–692 |
| Fitting proof | 712–749 | 694–733 |

The reused independent checker was copied to a new scratch directory. Its only analytical adjustment permits indentation on a tag-only source line when removing that entire line, exactly matching the separately authorized correction. It does not generally normalize mathematical whitespace or suppress mathematical differences. The separate exact old/new reconstruction check prevents this adjustment from masking any additional candidate change.

Actual commands included complete `diff -u` comparisons, `wc -l`, `cat`, the numbered boundary read, and:

```text
python data/generated/quarto_capability_pilot_20260921/pilot-audit-followup/independent_check.py
python data/generated/quarto_capability_pilot_20260921/pilot-audit-followup/correction_check.py
```

Both completed successfully. New evidence is retained in `pilot-audit-followup/`: both scripts, `independent_check.json` (including the complete reference/display ledgers), `correction_check.json`, and `candidate_exact.diff`. No old scratch file was overwritten.

**Future instruction amendment**

`future_instructions_v2.md` adequately states both requested rules for this packet. Rule 3 explicitly requires blank lines before opening and after closing display delimiters, including labeled closings, and deletion of an entire tag-only line with its indentation. It continues to protect mathematical characters and same-line tagged equation bodies. Rule 5 explicitly closes statements at their original endpoints, identifies the roadmap as outside Theorem 1, and requires separate statement-body comparisons. The final checklist adds exact comparisons for all four statement and three proof spans and accurate ID/display counts. These amendments address the observed failure modes without authorizing a content rewrite.

**Final verdict: PASS for preservation of this corrected frozen excerpt.** This does not certify rendered HTML/PDF, external resource delivery, the truth of all original mathematical proofs, scientific promotion, or readiness/authorization for full-book migration.
