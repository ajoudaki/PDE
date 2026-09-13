# Approved H3 integration and bounded live checks

The user approved the exact seventeen-file proposal with “yes I approve” on
2026-09-13 in task `01a09b51-6f6c-7371-9726-159b9402da2b`. The frozen proposal,
mapping, patch and review reports remain unchanged; the promotion record binds
their hashes and retains the approval. Root is the sole Git writer.

Before application, the existing preapproval checker is rerun into fresh
`data/generated/observable_hierarchy/H3_v2_approved_preflight/`. Its 361 hash
comparisons and dry application check must pass. Apply only the approved patch
after rechecking all seventeen base hashes; retain exact reviewed-to-live hashes.
Use the common nonblocking Git writer lock for each stage/verify/commit transaction.
Do not hold it while running numerical checks or touch concurrent unrelated work.

Before executing live checks, the following bounded validation is declared:

- Exact live correspondence for all 24 established files in the 27-file frozen
  edition, including the seventeen promoted destinations and unchanged dependencies.
- The five complete observable test suites: 54 tests in the frozen edition.
- The unchanged published guide example at order 3, Q=2048, P=1024,
  8 midpoint nodes per arc, 32 Heun steps through T=1/200, float64, and a
  128-direction panel. Its midpoint JSON restart is compared with uninterrupted
  and in-memory continuation on every state/data array. This repeats an existing
  supported configuration; it is not a new trajectory experiment.
- Actual imports must resolve to the maintained live package. Check the new
  chapter heading/roadmap fragment, exact section insertion, and guide append.

Total allowance: 600 CPU seconds and 600 wall seconds for tests and example;
4 GiB address space per child, one numerical thread. Each of two sequential
children has 240 CPU seconds and 280 wall seconds; ordinary static checks are
bounded separately to 60 CPU seconds/1 GiB. Stop on any failure or exhausted
budget, retain all output and investigate its cause. No automatic rerun,
additional resolution, broad sweep, finite-network training or time-40 extension.

Success requires all frozen byte comparisons and all tests/example checks to
pass. Numerical agreement here establishes installation/operation, not an error
certificate. Original independent twelve-configuration reproduction remains the
performance evidence of the unchanged code. Live results go into a fresh
`data/generated/observable_hierarchy/H3_v2_live_promotion_v4/` directory.
The retained `H3_v2_check_promoted_v4.py` implements the check and can be rerun
with a fresh output path; the preapproval checker deliberately expects old bases.
