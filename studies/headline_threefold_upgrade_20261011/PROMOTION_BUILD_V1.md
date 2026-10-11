# Promotion build validation: v1 (withdrawn frozen candidate)

## Scope and outcome

This is a mechanical validation record for the frozen standalone project
`data/generated/headline_threefold_upgrade_20261011/promotion_v1/docs`.
No candidate `.qmd` or `_quarto.yml` file was modified: the before and after
source manifests are byte-identical (SHA-256
`448a35fb829e4718889e9d72a6192f3813d7a02afaf4e48d1d6ee38f9f6c2c14`), and
the hash-diff file is empty (SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).

The candidate is not render-clean and v1 is withdrawn. HTML completed with
unresolved references/citations; PDF failed in XeLaTeX; the editable-LaTeX
command was started but did not reach an exit-status line before the v1 stop
instruction, so it is incomplete rather than a passing render. No repair or
diagnosis beyond recording compiler output was performed.

## Environment

- Quarto: `/tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto`,
  version `1.8.27`.
- XeLaTeX: `XeTeX 3.141592653-2.6-0.999993 (TeX Live 2022/dev/Debian)`.
- latexmk: `4.76` (20 November 2021).
- Render working directory:
  `data/generated/headline_threefold_upgrade_20261011/promotion_v1/docs`.

## Commands and status

The first invocation of each requested command used the supplied Quarto binary
and failed before rendering with `Read-only file system (os error 30): mkdir
'/home/codex-b/.cache/quarto'`. The preserved logs are
`build-*.initial-readonly-cache-failure.log`. The reruns used a task-owned
cache, preserving the required renderer and target format:

```sh
XDG_CACHE_HOME=../quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to html
XDG_CACHE_HOME=../quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to pdf
XDG_CACHE_HOME=../quarto-cache /tmp/pde-compression-quarto.CoMrum/quarto-1.8.27/bin/quarto render --to latex
```

| Format | Final recorded status | Log |
|---|---:|---|
| HTML | `0` (completed, warnings) | `build-html.stdout-stderr.log` |
| PDF | `1` (XeLaTeX failed) | `build-pdf.stdout-stderr.log` |
| editable LaTeX | incomplete/terminated before completion (no final exit-status line) | `build-latex.stdout-stderr.log` |

The PDF was allowed to finish after the earlier short tool-window invocations;
its final logged exit status is `1`. Per the coordinator instruction, no new
v1 format was started after that and the incomplete editable-LaTeX invocation
was not retried.

## Diagnostics

All reported unresolved targets are in
`08b-trajectory-compression.qmd` (the exact source locations are retained in
`unresolved-target-source-locations.txt`):

- Citeproc unresolved: `@proof-compression-fit` (line 3459),
  `@proof-compression-innovation` (4157), `@proof-compression-panel` (4514),
  `@proof-compression-source-whole-sphere-verification` (3730),
  `@proof-compression-src-finite-working` (4032),
  `@proof-compression-src-gaussian` (3385),
  `@proof-compression-src-local-lemma` (3563 and 3696), and
  `@proof-compression-src-panel-working` (4043).
- Unresolved cross-references: `@sec-compression-every-noncentered-contraction`
  (3905) and `@sec-compression-src-coefficients` (6462).

PDF additionally terminated with `Extra }, or forgotten $.` at generated TeX
line 54930 (`...lambda,\\log2/(4\\mathcal K),1/(32YSD_W)} \\) and at most`).
The matching compiler excerpts are retained in `pdf-failure-log-excerpt.txt`.
The Quarto summary says `compilation failed- missing packages (automatic
installed disabled)`, but the concrete XeLaTeX error recorded immediately
before it is the malformed-math error above; no package repair was attempted.

No duplicate identifiers or additional missing targets were reported by the
saved log scan beyond these warnings and the PDF failure.

## Artifacts and integrity records

All files below are under
`data/generated/headline_threefold_upgrade_20261011/promotion_v1/`:

- `candidate-source-sha256-before.txt`, `candidate-source-sha256-after.txt`,
  and `candidate-source-hash-diff.txt` record the immutable candidate inputs.
- `build-html.stdout-stderr.log`, `build-pdf.stdout-stderr.log`, and
  `build-latex.stdout-stderr.log` are the final render logs; corresponding
  `*.initial-readonly-cache-failure.log` files preserve the initial environment
  failures.
- `build-log-diagnostics.txt` is the warning/error scan.
- `rendered-output-paths.txt` lists all 30 present HTML/PDF/TeX outputs;
  `rendered-output-sha256.txt` gives their SHA-256 hashes.
- `validation-artifact-sha256.txt` records SHA-256 hashes of the manifests and
  build logs. Its output-manifest hash is
  `ed71447ab42271f6d35905ec03fb233d32b05b8f3caa65f10da3de605037d252`.

HTML artifacts were created in `data/generated/DTDL/` within this frozen
project, including `index.html` and the 18 chapter/notation/outlook pages.
The output manifest also records present PDF/TeX artifacts, but PDF cannot be
accepted because its final render failed, and the editable-LaTeX export cannot
be accepted because the final command was intentionally left incomplete.
