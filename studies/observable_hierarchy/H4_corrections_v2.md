# H4 corrected edition v2 — author disposition

The original frozen v1 packet, two complete scientific reports and all original
evidence remain unchanged. Both scientific reviewers found a required literal
inequality correction. Reviewer B also reproduced a failure of the printed
test recipe. The separate original integration review is complete and independently
identified the placement, recipe, Markdown and constant-display defects. This record is author
history and is excluded from all fresh reviewer input packets.

1. In (H40.D7), replace `C,R<e^80` by `C<e^80, R=e^80`, agreeing with the
   definitions in (H40.E2). The later strict bounds retain their original
   slack: for example `M=10+80RC<10+80e^160<e^200`. No constant, family,
   algorithm, target threshold or numerical configuration changes.
2. Both full observable-test recipes now create fresh scratch under the
   edition's `data/established/` and supply `H4_LAW_TEST_SCRATCH`,
   `H4_VALIDATION_TEST_SCRATCH` and `TMPDIR`. This includes the earlier H3
   discovery command, since its wildcard also discovers the new tests.
   The two setups are byte-identical. The installed test docstrings now name
   canonical test paths and fresh data/established scratch, and their failure
   messages refer to the reusable guide. Test logic is unchanged. Running the
   exact setup with the variables initially absent passes all 67 tests.
3. The assembler inserts D directly at the end of C.4.7.10, before C.4.8,
   preserving every byte of the previous chapter. The first new header is
   `###### D.1. Computation through physical time 40: fixed family and target`;
   D.2–D.5 have the same six-hash level as the existing A/B/C subsections.
   The prior five-hash parent/sibling heading and duplicate D.1 heading are
   removed. The frozen v1 assembler's end-of-chapter placement is not reused.
4. Close the three unmatched bold local subsection labels in the new support
   proof. This changes only Markdown delimiters.

`H4_proposed_section_v2.md` is the complete corrected new theory source;
`H4_code_guide_v2.md` is the complete new guide addition and
`H4_code_readme_v2.md` is the complete intended code guide, including the
earlier discovery-command repair. `H4_assemble_v2b.py` supplies the corrected
placement and canonical test documentation. The earlier draft `H4_candidate_v2`
and its executed check remain preserved; the final corrected packet uses
`H4_candidate_v2b`. The doc roadmap, every numerical runtime/plan file, test logic and all older
scientific proofs are unchanged; only the two test docstrings/error wording
change in code files. All 79 new equation tags remain unique.

`H4_check_revision_v2.py` predeclared a 600-CPU-second/660-wall-second check
with one numerical thread, 4 GiB and no research trajectories. It verified
exact chapter insertion/preservation, all executable byte identities, headings,
tags and the two complete test setups. The exact recipe passed in 4.690 child
CPU seconds, 5.026 wall seconds, peak RSS 50,487,296 bytes. Evidence is in
`data/generated/observable_hierarchy/H4_revision_checks_v2/`. Neither a
successful check nor this author disposition substitutes for new reviews.

The final v2b recipe check also passed all 67 tests (4.684 CPU seconds,
5.078 wall seconds, 50,827,264 bytes peak RSS) and verified identical runtime
and plan bytes plus unchanged test logic. Its source/evidence are
`H4_check_revision_v2b.py` and generated `H4_revision_checks_v2b/`.

The complete corrected [packet](H4_review_manifest_v2.json) is frozen with
271 inputs. Two new complete isolated scientific reviewers C/D and a fresh
complete integration reviewer are running from that packet without access to
prior findings. No established source is changed
and no promotion approval is requested until those gates are complete.
