# Independent preservation audit: linear-opening pilot

**Verdict: NEEDS CORRECTION.** The frozen candidate preserves the complete text and mathematics under the permitted lexical transformations, but incorrectly includes the explanatory proof roadmap inside the population theorem. This is a required environment-boundary correction, not optional typography.

Audit date: 2026-09-21. This fresh review used only the neutral assignment and its seven named frozen inputs, together with the shared instructions supplied to this context. It did not read the study README/history, worker report, other reviews, other studies, or the remaining book. No candidate, input, configuration, or Git state was changed.

**Read coverage and identity**

All lines were read, including blank lines, in every named input. The source and candidate were read in consecutive numbered ranges 1–310, 311–620, and 621–EOF; the other inputs were read completely. No required packet material remains unread.

| Frozen input | Complete line coverage | SHA-256 |
| --- | --- | --- |
| `pilot_source.md` | 1–907 | `3217f65ee957581085b6152c5ab6d59b1a62b3c9470bc48003908cbae55b1db7` |
| `pilot_linear.qmd` | 1–899 | `d6f78030984d9932be8e01d690dfb9e33f2cfa42443612829d88764b52fe361b` |
| `pilot_manifest.json` | 1–340 | `efbce69c35a87c4c28434eb1b4e82e99fbc1edb5a915d4834df16ab43959e5e4` |
| `pilot_instructions.md` | 1–86 | `794cecd4f165596394dd255c5353d0a1ab163d67d24250fd5ee3c12977f77564` |
| `pilot_quarto.yml` | 1–18 | `993b22465798a0c6699db06d67ea34fb221f0724e989d5d073b44d96d77592fd` |
| `pilot_index.qmd` | 1–14 | `5ac86fb0ce6cd4381a1567f75833cca56aa35c8d11f3371298e414de2ba4de8e` |
| `hashes.json` | 1–8 | `cf4ddef6217530a3bf9af07765ebefec0800adadb6682e9cb630e6cff8102bc5` |

The six file digests recorded in `hashes.json` all match the actual input bytes. Its own digest above is recorded for identity; the packet does not supply an independently anchored expected digest for that file. The source excerpt also matches the manifest's excerpt digest, and independently hashing each of the six exact source-line spans reproduces every manifest block digest. The manifest's full-book and notation-resource digests cannot be verified from this packet: those files are outside the permitted inputs and were not retrieved.

**Methods and executed checks**

The actual reads/checks used `cat` for the neutral assignment and complete supporting inputs; `wc -l` and `sha256sum` on the seven packet files; and `nl -ba … | sed -n 'START,ENDp'` for the six complete source/candidate reading ranges above. I wrote and ran:

```text
python data/generated/quarto_capability_pilot_20260921/pilot-audit/independent_check.py
```

The independent script and full diagnostic output are retained in the assigned scratch directory as `independent_check.py` and `independent_check.json`. A separate Python read printed every display mapping and every reference occurrence with source line, candidate line, and destination line; I inspected that complete output.

The checks independently extract math expressions in occurrence order, compare their interior strings exactly after removing only the authorized tags/proof squares, derive expected equation IDs directly from original tags, and compare all nonblank source/candidate lines after the permitted lexical changes. The text comparison disregards blank lines and right-edge whitespace but does not remove or alter internal prose or mathematical characters. Crucially, a separate fence-stack check maps the content of each actual candidate environment back to original source lines; stripping structural markup for the lexical check does not excuse an incorrect scope. Manual reading separately evaluated whether the manifest's boundaries make sense against the original text.

No renderer was run and no rendered output was included in the assigned packet. Accordingly this report verifies the frozen source-format migration, including reference destinations in that candidate, rather than certifying HTML/PDF rendering or deployed resource availability.

**Component results**

| Component | Result | Evidence |
| --- | --- | --- |
| Prose, qualifiers, emphasis, and order | PASS | Complete allowed-transform line comparison has an empty difference. The roadmap is present and in its original order, but has the scope error below. |
| Inline mathematics | PASS | All 316 substantive inline expressions match exactly, including multiline expressions. The two additional original inline expressions are precisely the authorized terminal `\square` markers at source 341 and 733. |
| Display mathematics | PASS | All 49 displays match individually and in order, with no splitting/combining. The 45 tagged displays have the correct corresponding labels; the four originally untagged displays remain unnumbered. Same-line tags in Section 2.A retain their complete equation bodies. |
| Reference targets | PASS | All 63 native reference occurrences match the original intended identities and resolve to unique candidate IDs. These comprise 58 equation references and five theorem/lemma references. No old equation-reference syntax or named in-scope theorem/lemma/corollary reference remains. |
| Section structure and mapping | PASS | Six section headings retain title text and levels 1, 2, 2, 3, 2, 2. Six mapping comments occur once each in the required order. Statement title headings are within their corresponding divs. |
| Statement type/title/body boundary | NEEDS CORRECTION | All four types and original titles are correct, including the untitled trace-class lemma. Three statement spans are exact; the population theorem absorbs the following explanatory paragraph. |
| Proof structure and endings | PASS | All three proof spans match the original, including the named proof and its internal bold headings. The two explicit terminal squares are replaced only by proof-environment endings. No proof ID or extraneous proof wrapper occurs. |
| Partial-edition scope and pending references | PASS within packet | The introductory ranges remain literal at candidate 4 and 11; the index explicitly calls them pending and limits this edition to original Section 4. The notation link remains unchanged and the configuration declares the resource. Actual resource bytes/shipping are not included in this audit. |
| Invented/lost mathematical content or citations | PASS | None found. No bibliography entries or fabricated citations were added. |

The exact environment membership check produced:

| Environment | Candidate fence lines | Actual original content span | Required original content span |
| --- | --- | --- | --- |
| Population theorem | 89–149 | 91–149 | 91–143 |
| Gaussian-word lemma | 231–253 | 237–256 | 237–256 |
| Gaussian-word proof | 255–337 | 258–341 | 258–341 |
| Trace-class lemma | 381–407 | 386–409 | 386–409 |
| Named singular-expansion proof | 409–557 | 411–556 | 411–556 |
| Fitting corollary | 687–693 | 691–692 | 691–692 |
| Fitting proof | 695–732 | 694–733 | 694–733 |

These boundaries were not accepted merely because the manifest listed them. In the original, the population theorem's final compact-time restriction ends at source 143; source 145–149 changes to a prose description of how the proof proceeds. The other statement endings retain their final qualifications. The Gaussian proof ends after the fixed-degree qualification and explicit square at source 341; the fitting proof ends after the zero-label uniqueness case and square at 733. The named proof's original internal headings and subsequent derived consequences continue through its concluding paragraph at 554–556, before the next section; the candidate retains that full sequence.

Every reference was checked against the corresponding preserved destination content, not merely for existence of an ID. In particular, introductory `Lemma 2.A` at source 15 becomes candidate 16's `@lem-linear-trace-class`, pointing to the compact-operator/trace-class lemma at candidate 381, while source 740 and 822's `Lemma 2` point to the Gaussian-word lemma at candidate 231. References to the main theorem at candidate 690 and 847 correctly target candidate 89. The full 63-occurrence ledger and 49-display correspondence are in the independent diagnostic JSON.

**Required finding P1: close the population theorem before its proof roadmap**

Source: `pilot_source.md` 139–149, especially the completed scope restriction at 143 and explanatory paragraph at 145–149. Candidate: `pilot_linear.qmd` 137–149, especially the final theorem sentence at 141, roadmap at 143–147, and delayed closing fence at 149. Contract: the manifest declares statement 91–143; conversion rule 5 explicitly forbids absorbing explanatory paragraphs.

The opening fence at candidate 89 remains active through the roadmap. Consequently the paragraph beginning “The proof first packages the finite factors in one cyclic operator” becomes part of the formal theorem environment. Its words are unchanged, but its formal placement is not preserved. This is why an empty normalized text difference is insufficient to pass this packet.

The smallest reliable correction is to move the existing closing `:::` at candidate 149 to immediately after candidate 141, keeping a blank line before the roadmap. Do not delete, rewrite, or reorder the roadmap. Then freeze the revised candidate and hash and rerun the independent lexical/math/reference checks plus the explicit environment-membership check; the theorem must map to original 91–143 and the roadmap must map outside every statement/proof div.

This is an isolated observed error in this packet. The review supplies no evidence about earlier packets, which were not read. The failure mode can recur in future packets whenever a check strips div markers or only checks that a closing fence exists. Require both exact source-line membership and manual assessment of the proposed boundary for each formal environment.

No other required preservation correction was found. Whitespace left where same-line tags were removed is optional typography and does not change the mathematics.

**Final verdict: NEEDS CORRECTION for this frozen excerpt.** This is a preservation audit; it does not audit all original mathematical proofs, establish their truth, authorize scientific promotion, or authorize full-book migration.
