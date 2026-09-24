# Historical migration workflow — superseded

**Do not use this file operationally.** The active contract is
[`LIGHTWEIGHT_MIGRATION.md`](LIGHTWEIGHT_MIGRATION.md). The material below is
retained only to explain historical packets and must not be supplied to future
workers or auditors.

# Former migration workflow — packet010 onward

This is the controlling operational policy. It supersedes historical worker,
reviewer, rendering and retry instructions. Keep the original book intact and
keep the migrated prefix in source order. No scientific change or reorganization.
Luna5.6 is the conversion worker; Sol5.6 is the sole preservation reviewer.
Use Luna/high for packets requiring ASCII-to-TeX mathematical transcription.
Medium-effort wrapper conversion failed repeatedly in009/010; do not repeat that
configuration expecting instructions alone to fix this demonstrated limitation.
Mechanical TeX delimiter/tag edits still use deterministic code.
Root owns instructions, acceptance and provenance checks, not a duplicate audit.
Read this policy and the three syntax contracts once per isolated worker packet.

## One completed handoff, one consolidated review

1. Worker owns the whole assigned packet: conversion, reference discovery and
   mechanical validation. Reuse the registry, checker and accepted syntax.
   Generate the candidate from source offsets; never retype unchanged prose.
   Prefer deterministic conversion for already-TeX delimiters/tags/headings.
   First inventory source tag/environment shapes against supported syntax; report
   a genuine unsupported shape before bulk conversion, while completing work
   that does not depend on its remedy. Do not confuse unfinished ordinary edits
   with that blocker or submit them as a completed handoff.
2. Before submitting, finish ONE integrated omission pass covering all source
   math and references. Include bare symbols/variable lists, ASCII/Unicode math,
   full multiline code-form expressions, named destinations, lowercase section
   references, and BOTH endpoints of abbreviated ranges. Actual code stays code.
   Use whole-symbol matches, never first-letter matches inside prose words.
   Dollar delimiters alone do not transcribe ASCII mathematics. Never submit
   unchanged pseudo tokens as converted TeX; the retained-ASCII guard is mandatory
   alongside a semantic expression check. It detects known patterns, not all
   mathematical errors.
   Preserve multiplication, indices, grouping, norm type, expectation operators,
   and Euclidean-space notation. Derivative primes must be attached superscripts
   (`f'` or `f^{\prime}`), never detached `f\prime`.
3. Run the actual strict checker on the complete assembled packet. Resolve ALL
   reported errors together and rerun locally; do not submit partial artifacts,
   individual fixes, or a self-written substitute for the checker. Do not edit
   checker rules to force PASS. A genuine unsupported syntax is reported once
   with its exact source context; root chooses a minimal general remedy.
4. Only after the whole packet passes, freeze it and send it to Sol. Sol checks
   all NEW source correspondence, math and references once, including omissions.
   Finish that review and residual scan BEFORE issuing one complete correction
   list. Do not drip-feed findings or start repair workers while still scanning.
5. Apply reference corrections before math corrections: a numbered locator is
   a reference, not a mathematical variable. Where a correction ledger mentions
   a span in both categories, use its explicit reference disposition and remove
   the superseded math edit. If corrections are delegated by category, hand over
   the reference intervals before merging; exact overlaps must be resolved.
   Validate decoded TeX strings, not just their JSON spelling: serialization
   must not introduce an extra backslash layer.
   The same worker applies the complete list, checks the affected failure class
   across its own packet, and reruns the strict checker before returning. Send
   only the frozen delta and affected dependencies back to the SAME Sol auditor
   until PASS. Keep earlier review evidence; never repeat unchanged full audits,
   recruit a fresh reviewer, or discard the initial work after fixes. If a new
   defect is found, finish the bounded changed-scope check before reporting it.
6. Root reads the concise verdict and verifies reviewed identities, unchanged
   sources, prefix and registry. Then record one receipt and README checkpoint.
   Registry reservations remain binding future obligations. No acceptance while
   actual defects remain. Repeated failures trigger a concrete process/model
   diagnosis, not blind retries or an automatic full restart.

## Permanent cost and quality controls

- No rendering, browsers, PDF/LaTeX builds, cosmetic work or capability campaigns
  during migration. Presentation validation is deferred to later integration.
- Run relevant tests once when utility code changes; otherwise use the existing
  packet checker. No repeated full utility reviews, tests or source rereads.
- Findings must become general instructions or narrow mechanical guards where
  mechanically decidable. Check the affected class, not arbitrary extra scope.
  Do not claim mechanics proves mathematical equivalence.
- Return brief completion/failure messages. Avoid verbose worker reports,
  repeated status requests, redundant planning and token-heavy output dumps.
  Root progress updates state actual developments, not repeated plans.
- Preserve consumed snapshots and exact changes with compact hash manifests.
  One worker report (at most150words), one final audit report (at most200words),
  and the existing README suffice. Do not build another tracking system.
- Do not promise unmeasured token/time improvements or trade correctness for
  a speed target. Optimize away coordination and rework, keeping the same gate.

Earlier packets001–008 retain their receipts but require targeted removal of
remaining plain/code-form math before the whole edition is called migrated.
That obligation does not automatically authorize another cleanup campaign.
