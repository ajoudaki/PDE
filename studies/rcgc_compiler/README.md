# RCGC syntax compiler

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

This directory contains the executable G0 compiler for the canonical
single-sample MLP. It is intentionally smaller than the analytic calculus:
it derives exact forward/backward equations, block velocities, raw kernel
terms, and the same-time curvature words that a sound dynamic Gaussian
backend must classify.

The compiler does **not** decide convergence. In particular, an emitted
multi-colour word is a promotion obligation, not a negative theorem, and an
empty curvature list for identity activation is not by itself a
continuous-time proof.

From the repository root, run:

    python -m unittest studies.rcgc_compiler.test_rcgc_compiler
