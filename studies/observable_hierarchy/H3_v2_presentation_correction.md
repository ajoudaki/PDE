# Edition v3: integration presentation correction

The complete integration review `H3_v2_integration_v3.md` requires R1:
the bare ASCII comparison bound is parsed as a Markdown link, hiding its
multiplicative factor. Its raw mathematical argument was accepted; this is
a presentation correction only. The old edition and original report remain
unchanged. Edition v3 displays exactly the same inequality in LaTeX.

No equation, hypothesis, proof inference, API, implementation, test, guide,
configuration or execution result changes. In particular the executed v2
validation plan is reused byte for byte. The two complete scientific reviews
of edition v2 remain attached to their exact original inputs. Part 2 step 4
requires a fresh complete integration review of this corrected edition;
its rule that scientific changes reopen the paired gate does not apply to
this purely presentational change. The new reviewer receives no old verdict.

Before executing correspondence/render checks: static budget 60 CPU seconds,
1 GiB; verify all edition hashes, exactly one formula substitution in each
of the section and full chapter, identity of the other 25 files, and absence
of the accidental factor link. No new numerical computation is needed.

Reassemble with:

```sh
python studies/observable_hierarchy/H3_v2_assemble.py --version v3 \
  --output data/generated/observable_hierarchy/H3_v2_edition_v3 \
  --plan-source studies/observable_hierarchy/H3_v2_reproduction_plan_v2.json
```

Then run `H3_v2_prepare_integration_v4.py` from the repository root. It saves
the exact substitution and byte correspondence, and freezes the complete
neutral integration packet. The original v2 manifest remains a complete
input so all execution provenance continues to resolve to its actual source.
