# Live book integration check

Date: 2026-10-11.  This is the post-approval mechanical integration check for
`docs/08b-trajectory-compression.qmd`.  No `docs/`, `code/`, or `paper/` source
was edited by this check, and no Git operation was performed.

## Source correspondence

The initial live chapter was exactly the approved v6 chapter:

```
3b6ca32de3f4feef6771c15c7826edc4c38d70836e7d261fa06468582f4646f1
```

The initial exact-live snapshot renders are retained in
`data/generated/headline_threefold_upgrade_20261011/book_live_integration/`.
They are superseded because the coordinator then made exactly two authorized
locality-prose clarifications (the diff is at lines 619--625 and 2240--2249 of
the live chapter).  They state that the quantitative-width and initialization
proofs explicitly recall the coefficient recurrences they use.  No label,
formula, hypothesis, mathematical claim, or proof calculation changed.

The final live chapter is byte-identical to both frozen copies
`paper_integration_v2/docs/08b-trajectory-compression.qmd` and
`paper_integration_v3/docs/08b-trajectory-compression.qmd`:

```
4b18d60c47f760e91d0077182b56c97484697753937c814d64264d52df2d03aa
```

Final live/source-snapshot hashes were identical before the final renders and
after them:

| Path | SHA-256 |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `4b18d60c47f760e91d0077182b56c97484697753937c814d64264d52df2d03aa` |
| `docs/_quarto.yml` | `3a64f59b5923060d7196ffaf7ad8494ec3a6f906c90d2801e86ecdb3027d5a2e` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `docs/references.bib` | `5fa1272b98a6748cd624ab1aeb0badb3654437e90dfd0ff136bf67103331ebc7` |
| `docs/package_code_links.py` | `9b6013ee40957732da7ce4b8e7f2cae019eeae77b3adb15799de7833a1e8fdd2` |
| `docs/pdf_breakable_tables.lua` | `dd08fd0aa5efc43bf7894d5688d0c2ecfdfbe1367259b09df5aa136b00f4dd48` |
| `docs/print_code_links.lua` | `5540e06477f1030e25013e86e0028a3ac853889d26bb4fa1f5b1921903774745` |

The final snapshot is
`data/generated/headline_threefold_upgrade_20261011/book_live_integration_v2/live_source_snapshot/`.
It was copied from the current live `docs/` and `code/` with the established
`assemble_promotion.py` exclusions: hidden paths (including `.quarto`),
`__pycache__`, and `*.pyc`.  The snapshot has the same live chapter and all
listed Quarto dependencies.  The only non-cache difference in the earlier
frozen-v6/live documentation comparison was `.gitignore`: live adds
`/DTDL.tex`, which has no rendering semantics.

## Render results

Renderer: `/tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto`
(Quarto 1.8.27).  Each final command ran from the snapshot `docs/` directory,
with `XDG_CACHE_HOME` set to the fresh final integration directory's `cache/`.
They ran sequentially:

```
quarto render --to html   # exit 0
quarto render --to pdf    # exit 0
quarto render --to latex  # exit 0
```

Their complete logs are `render-html.log`, `render-pdf.log`, and
`render-latex.log` in
`data/generated/headline_threefold_upgrade_20261011/book_live_integration_v2/`.
`rendered-output-sha256.txt` there records SHA-256 hashes for all 23 rendered
HTML/PDF/TeX files.  Key final outputs are:

| Output | Size | Location |
|---|---:|---|
| HTML book | 18 chapter/navigation pages | `.../book_live_integration_v2/live_source_snapshot/data/generated/DTDL/` |
| PDF | 6,774,224 bytes | `.../book_live_integration_v2/live_source_snapshot/data/generated/DTDL/DTDL.pdf` |
| Editable LaTeX | 4,700,795 bytes | `.../book_live_integration_v2/live_source_snapshot/data/generated/DTDL/book-latex/DTDL.tex` |

The source structural checker found zero duplicate identifiers, zero missing
cross-references, and zero non-heading section cross-references; its result is
`structural_check.json`.  The final render logs contain no diagnostics matching
error, warning, unresolved, undefined, duplicate, missing, or malformed.
`navigation-targets.txt` confirms all 18 configured HTML targets.  Successful
Quarto rendering in all three formats additionally checks citation resolution
and formal-environment syntax.

## Direct-live cache limitation and preserved first pass

The first direct-live HTML command, from `docs/` with a fresh XDG cache, exited
1 before rendering because the inherited `docs/.quarto/project-cache/` Deno KV
database is read-only (`TypeError: Can not write to a read-only database`).  Its
log is `book_live_integration/render-html.log`.  The inherited cache was not
removed, chmodded, or otherwise modified.  The exact-live snapshot fallback is
therefore the render evidence; it deliberately did not overwrite the existing
live `data/generated/DTDL` outputs.

The earlier exact-v6 snapshot HTML/PDF/LaTeX logs in
`book_live_integration/` all have exit 0 and are retained as the superseded
first pass.  Its original direct-cache failure log is retained separately.

`docs/DTDL.tex` already existed before this task and remained unchanged:
`a5efebb3d7d30f5013291bfaf0d415c13d32d683d6f82230591429b2e378e653`
(4,601,709 bytes, timestamp `2026-10-11 08:55:09 +0200`).  The snapshot render
generated packaged TeX copies under its own output tree only; it did not create
or change the live `docs/DTDL.tex`.

No new visual inspection was repeated: accepted v6 visual checks cover the
unchanged material, and the final change is the two stated prose-only locality
clarifications.  Browser screenshot testing remains unavailable.
