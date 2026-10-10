# Independent integration review: frozen promotion_v4

**PASS.** The proposed addition is integrated coherently into Part II, Chapter 7. No required integration correction or unresolved objection remains. This verdict concerns the complete new assembled content and its interfaces; it does not replace the paired scientific reviews or user approval.

Reviewer: `/root/nth_integration_final`, 2026-10-10. Edition root: `data/generated/nth_lower_bound_20261010/promotion_v4/`. Paths below are relative to that root unless stated otherwise.

I read the neutral integration assignment, the required notation skill and its neural-network reference, and the research workflow. I reread the new model-allocation instructions after notification that HEAD changed to `b8367aede266a4136c363f19edbd12128b010088`. That instruction change did not change the frozen scientific inputs.

I read every line of `candidate.qmd` (1–578), including all proof bodies and scope qualifications; the full frozen notation contract (98 lines), index (260 lines), Quarto configuration (68 lines), and bibliography addition. The candidate occurs identically at assembled Chapter 7 lines 447–1024. I checked its complete rendered HTML text as well as the generated formal structure. Older scientific reading was exactly Chapter 7 lines 1–32, 345–446, and 1025–1114, plus Chapter 9 (`08b-trajectory-compression.qmd`) lines 1–225, including the complete added paragraph and its setup. The older Chapter 7 complement, Chapter 9 after line 225, and all other chapter proof bodies were outside this review. Whole-edition hashes, HTML IDs/links, and PDF navigation metadata were checked mechanically without extending the scientific reading scope. The PDF converter also emitted whole-book outline headings; these are navigation metadata, not additional proof inputs.

The manifest and preservation metadata were permitted inputs. I independently recomputed all 104 recorded live baseline hashes and all 104 expected frozen hashes: zero mismatches, including at the final check after both builds. I compared the three changed files against the current maintained files. Chapter 7 contains one exact candidate insertion and one separating blank line; Chapter 9 adds only the specified scope paragraph; the bibliography appends exactly the supplied entry. The other 101 recorded files, including all recorded code, are unchanged. Concurrent content is preserved; no unrelated proof was inspected through a diff. No empirical claims or code changes require reproduction in this addition.

Placement is appropriate and proportionate: one 578-line section within the 4,653-line Chapter 7, after the unrestricted-encoding example and before the existing calculus obstructions. It fixes the representation and supplies a quantitative approximation/storage result, unlike the neighboring unrestricted field-count discussion. No chapter or part was added, and the index/configuration preserve the book's arc. Duplication assessment is limited to the assigned contextual material, not a whole-book novelty audit.

The setup defines the canonical layer shapes, normalized queries, zero readout, identity activations, loss, mobilities, data summaries, source tensors, closure residual, decoder and storage before using them. The transformation to ordinary Euclidean/Frobenius flow correctly accounts for the first-layer and readout factors. The half-MSE/full-MSE correspondence is explicitly correct: the full-MSE trajectory at time t equals the half-MSE trajectory at time 2t. The stated interval therefore becomes [0,T/2]. Ordered tensor slots are not silently symmetrized. Moving arrays, frozen arrays, data storage, coefficient-generation work and precision have distinct accounting.

The main statement and closing paragraph retain the short physical horizon, growing correlated data, fixed positive label scale, exact arithmetic, actual dense-pair comparator, and literal-array restriction. The zero-data-summary case and failure of existence are handled explicitly. The Chapter 9 pointer accurately identifies the different data regime and disclaims a same-family separation. The citation is contextual; the proof does not import a theorem for a different parameterization. No new undefined central object, contradictory summary, or improperly broadened implication was found.

Independent mechanical checks used Python `hashlib`, `difflib`, `html.parser`, and regular-expression checks; evidence is retained in `integration_scratch/`. All 18 HTML pages have unique IDs and all fragment links between those pages resolve. All 38 candidate identifiers and every candidate cross-reference target occur in Chapter 7 HTML. The new output contains one theorem, one corollary, five lemmas and six proof blocks. The Huang–Yau citation resolves to the complete rendered bibliography entry, and the Chapter 9 link resolves to the intended theorem.

I inspected `validation/builds.json` and the HTML/PDF build logs. Full `quarto render --to html` and `quarto render --to pdf` commands both exited 0 (90.03 s and 195.91 s); no warning, error, undefined-reference, missing-target or duplicate diagnostic was present in those logs. The PDF build's retained editable LaTeX is `data/generated/DTDL/docs/DTDL.tex`; it is the actual compiled export, not a separately inferred equivalent. Its candidate region is unchanged from the inspected intermediate and contains all 38 targets with balanced theorem/corollary/lemma/proof environments and no unresolved markers.

`pdfinfo` reports a 1,744-page PDF. I located the new section on pages 668–678 and visually inspected pages 668, 670, 671, 675, 677, 678 and 855 using `pdftoppm` and image inspection. Headings, statement numbering, mathematical displays, proof endings and transitions are legible; ordinary line/page breaks do not clip or obscure content. Page 855's actual PDF link annotations, independently extracted with `pdftohtml`, send both wrapped parts of “its storage theorem” to page 670, where the theorem begins. PDF and HTML use format-specific numbering through native references; the targets remain correct.

Input and artifact SHA-256 hashes:

- `manifest.json`: `152e5f30e7991d061544fa9dd49ab1aca8db4df6bfe1d17d24903ad17c0a0066`
- `candidate.qmd`: `e8c8cbd7474b9e0bbaded9100ce02474708339f9ac95cf606de7b93886616d23`
- `notation.qmd`: `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`
- `references.bib`: `7b7a4a33db9309b9ecb91c3f058236af8c855e7b7470fbd107809140d19b35a9`
- `docs/index.qmd`: `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68`
- `docs/_quarto.yml`: `e8312b9a53ebe0dbff35b93c55f8f8f5f49bd8c3bf633bd44c8bdd2b086f55e7`
- `docs/07-observable-closure.qmd`: `61c07f5813112b18011944618059cf3a1155feab476762aa8602442fd98e36e4`
- `docs/08b-trajectory-compression.qmd`: `405c8e0a4d99d8b5bebcb4c13d5534317050aa0a10d33b0476b9d90c9cc5bdf5`
- `docs/references.bib`: `22e5ef136f3d863bd95f09d66206dca5b09c4e92ee5a0bcc91aac093e94709a1`
- `data/generated/DTDL/07-observable-closure.html`: `47497931d94712c2c95486bb41d18f5afa211484f5db72fcfe119ddbe5a1d5ae`
- `data/generated/DTDL/08b-trajectory-compression.html`: `22f20f76d6a58f6cabaa56713e56cb30dee2444c8447b404a6872d23621364b9`
- `data/generated/DTDL/DTDL.pdf`: `f151aa7bdeda0fd8312cbc7bb7c55dac9611ec8500b4a9ae113adc2c79c25d2f`
- `data/generated/DTDL/docs/DTDL.tex`: `94f7e96140df47854f4966bec344603cb0f91b10799928cf4fa4cb5c54c9003f`

I worked in a fresh isolated review context, received only the neutral assignment and technical coordination, and did not read the study README/history, selector decisions, earlier reviews/verdicts, other studies, or archived book. I spawned no subagents and edited no candidate or edition source. Writes were confined to this report and the assigned integration scratch directory. Required reading and technical inspection are complete; there is no pending build or deferred objection.
