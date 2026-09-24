# Second Terra submission: coordinator rejection and reassessment

The v2 Terra submission is frozen in `linear001-submission02/` under the study's
generated namespace. Its original self-report is `linear_001_report_v2.md`.
It added the notation and italicized chapter links, but classified the explicit
plain-text continuous-depth chapter reference as generic prose. It also encoded
the eight labels as whole-heading replacements, contrary to the surgical edit
grammar. The candidate's heading text itself was preserved. Mechanical evidence:
`linear001-checked01/` contains the rejected metadata check and complete raw diff.

After the one fresh Terra corrective pass, the coordinator reassessed rather
than beginning another Terra retry. A fresh Sol/medium worker performed one
bounded repair using the complete packet and the stricter v3 instructions:
plain-text/hyphenated chapter names count as named references, and label records
must be actual zero-length insertions. Sol also added supported links from the
two explicitly identified benchmark names to their chapters, reusing the
continuous-depth reservation. The checker was not weakened to admit whole-line
replacements. Exact replay continued to enforce the final blank source line;
Sol's local failing checks and final passing check remain in
`linear001-sol-repair/`. Its final candidate is the one submitted for full audit.

These outcomes do not establish clean Terra calibration or low migration cost.
Full independent audit remains required. Future workers must be allowed and
instructed to run the existing checker before handing off, rather than relying
on a self-written self-check; this was unavailable to the initial parallel
worker and excluded from the second Terra worker's restricted input scope.
Allowing the checker prevents known mechanical defects reaching the auditor;
semantic reference omissions still require complete reading.

The accepted linear prefix was still empty, so there was no accepted content to
repair. The earlier out-of-order linear pilot retains two declared section-range
references and its bundled notation link as legacy integration obligations;
its source/evidence are not silently rewritten or counted in this prefix.
