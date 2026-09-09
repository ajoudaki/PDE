# Current-input refresh addendum to Round 1

Date: 2026-09-09. Private root: /tmp/pde-library-integration.J6HkSP.

**Disposition: CLEAN for the specified repair check. This is not a fresh independent integration round or a new independent whole-library verdict.**

The original-input report is preserved as [ROUND1.md](/tmp/pde-library-integration.J6HkSP/ROUND1.md), with its **NOT CLEAN** verdict, original findings, original input hashes, and original coverage unchanged. During the refresh I initially updated that report in place before the preservation request arrived; I then reversed those edits and moved its original content to ROUND1.md. This separately identified addendum records only the current-input refresh and the previously completed acceptances carried forward on unchanged bytes. It does not replace the independent final integration round that the main task will commission.

Preserved ROUND1.md: 230 lines; SHA-256:

    3ef2825e041f57f8ec0e96c5da09fc76e78dda7d0972087eea5dd81cc080c66d

That hash was taken after restoration; no pre-refresh report hash was recorded for an independent byte-hash comparison. Restoration used the exact inverse of the two report-edit patches. ROUND1.md's source line references and special-data input hash belong to the original snapshot, although the source path now contains the user-refreshed chapter.

## 1. Isolation and exact input delta

Substantive inputs remain ONLY this private root's docs/, code/, Makefile, and requirements.txt. No original repository, studies, data, history, other reviewers' reports, web sources, or agents were consulted. No new external proof premise was introduced. This is a continuation using this audit's own completed work and in-memory hash inventory, not an independent reassessment based on another verdict.

Only docs/special_data_limits.md changed. All other 20 input hashes are identical, including the Gaussian and linear full-proof acceptance hashes frozen below.

Special-data SHA-256:

- Original-input hash: 94ad0b6a9ba39e937e1f90626c74c6b9d1f652fe20523dcdf1cdbf780bdfeda0
- Current-input hash: e491ea163cf325ced50a3f1d19ab79cf9f84df85977ad644b68f4c96775e36ea

Reversing exactly the seven specified edits in a read-only stream of the current chapter reproduced the original-input SHA-256 exactly. The reversal comprised four activation-floor substitutions, one Gram-symbol substitution, the horizon wording with its added line, and one base-query substitution. No earlier source file or review was read to perform that comparison, and no input file was written. The chapter increased from 6,397 to 6,398 lines; all remaining bytes are unchanged.

## 2. Exact repaired regions and acceptance

All locations below refer to the current special-data hash. The added Part I line shifts the subsequent original line numbers by one.

| Region | Original → current lines | Current wording or formula | Result |
| --- | --- | --- | --- |
| Part I horizon bound | 1336 → 1336–1337 | “uniform over each fixed horizon, with a constant depending on that horizon” | Accepted, horizon-local only |
| Part II Gram identity | 2231 → 2232 | \(X^T X=dG\) | R2 Gram-symbol repair accepted |
| Part II first feature covariance | 3204 → 3205 | \(\frac12 E(H_1^{(1)}+H_2^{(1)})^2\ge 2c_-^2\) | First R1 floor repair accepted |
| Part II second-layer source covariance | 3221 → 3222 | \(c_1=\min(2c_-^2,d_1/2)>0\) | Second R1 floor repair accepted |
| Part II second feature covariance | 3233 → 3234 | \(c_2=\min(2c_-^2,d_2/2)>0\) | Third R1 floor repair accepted |
| Part II readout bound | 3282 → 3283 | \(W^{(4)}(s)\ge c_-s\) | Fourth R1 floor repair accepted |
| Part III base forward query | 5692 → 5693 | \(W^{(2)}T_j^1=\xi_{T_j^1}+\sum_i\beta_i^2c^1_{ji}E[D_j^1D_i^1]\) | R2 query-symbol repair accepted |

### Why the repairs are mathematically compatible

**Activation floor, sample count, and feature clock.** Part II keeps \(m=2\) as sample count and \(c_-=5/6\) as the separate activation floor, with upper bound \(a=7/6\). Consequently,

\[
25/18=2c_-^2
\le \tfrac12 E(H_1^{(1)}+H_2^{(1)})^2
\le 2a^2=49/18.
\]

The already established strictly positive separation constants \(d_1,d_2\) make both corrected covariance lower bounds positive. These are compatible with the ensuing rectangle-density lower bounds and forward/reverse covariance arguments in II.D.

For the readout, zero initial readout and the feature-time equation

\[
(W^{(4)})_s=(H_1^{(3)}+H_2^{(3)})/2\ge c_-
\]

give \(W^{(4)}(s)\ge c_-s\) by integration. The following \(b_0\) estimate already uses \(c_-\). This fixes the required motion-proof bounds without changing the physical-time scalar clock, promoting a feature-time estimate to a physical-time estimate, changing stored-readout scale, or altering sum/mean-loss factors.

**Gram type and singular endpoint.** The normalized input Gram is \(G=X^TX/d\), so the corrected identity matches the neighboring \(G^{-1}\) row-metric formulas. Inversion applies for \(-1<\rho<1\). The antiparallel endpoint retains the separate one-field calculation, without an inverse of a singular Gram.

**Same-matrix base query.** The initialized \(W^{(2)}\) maps population 1 to population 2 and is the matrix paired with the reverse query in the surrounding response rule. The corrected expression therefore has the required type and matrix identity. No alias imported from another document is needed, and no assumption about arbitrary growing transcripts is introduced by this replacement.

**Finite horizons.** The Part I wording agrees with the horizon-dependent \(C_T/M_T\) bounds in I.61–I.66. It gives uniformity within each fixed horizon, not a bound uniform as \(T\to\infty\), and does not justify interchanging width and infinite-time limits.

**Required issues remaining in this focused check: none.** R1 and R2 are closed on the current special-data bytes. The horizon clarification is also accepted. This conclusion is deliberately limited to the repair check and the carried-forward coverage below.

## 3. Read coverage and frozen full-proof acceptances

The original audit fully read NOTATION.md, the documentation guide, and the code README; inspected every chapter's theorem/convention/dependency interfaces and relevant actual proof assumptions; and fully proof-audited the following chapters. These are this same audit's completed acceptances, frozen to the exact unchanged hashes—not newly commissioned independent acceptances.

| Chapter | Original full-proof read | Frozen SHA-256 |
| --- | --- | --- |
| docs/gaussian_calculus.md | All lines 1–1812; full mathematical proof audit | cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e |
| docs/linear_dynamics.md | All lines 1–1166; full mathematical proof audit | 36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b |
| docs/finite_dynamics.md | All lines 1–214; full audit of the finite identities | 486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c |

The Gaussian and linear acceptance discussions are preserved in ROUND1.md, Section 3, without expanding their theorem scopes. Rehashing did not constitute a second proof read.

The other five mathematical chapters remain **interface/dependency-assumption audited, not independently fully proof-audited**: arctan_limits.md, global_nonlinear.md, special_data_limits.md, continuous_depth.md, and finite_optimization_and_controls.md. The initial audit inspected their complete text but did not claim independent verification of every proof step. That distinction remains in force.

For this refresh, the mathematical inspection was limited to current special-data lines 1257–1278, 1320–1347, 2128–2145, 2223–2238, 2870–2905, 3195–3243, 3278–3300, 3335–3372, and 5681–5702, plus targeted searches for the replaced notation and a final reread of the seven displayed regions. Those intervals cover the edits and immediate horizon, floor, clock, covariance, metric, and query dependencies. No entire unassigned special-data proof audit was repeated.

Current input counts: eight mathematical chapters total 17,224 lines; all 21 inputs total 18,853 lines. Neither this total nor the prior text inspection is a claim to independently proof-audit the entire library.

The original optional navigation-checker improvement remains optional: same-document fragments are skipped and cross-file fragments stripped by the checker. No current broken anchor was found in the original manual interface inspection. Fragment validation would not certify proof assumptions. It was not implemented.

## 4. Supplied implementation check

After inspecting the refresh, the already-inspected supplied check was rerun inside the private root. No implementation, tests, build file, or requirements changed.

    make check
    Library boundary and local links checked: 19 files.
    Ran 52 tests in 0.152s
    OK
    Exit status: 0

This was the supplied implementation test suite, not a new scientific experiment or an end-to-end proof verifier. No input was edited by the auditor.

## 5. Exact current-input SHA-256 manifest

Paths are relative to the private root. Reports are outputs and excluded. This manifest was checked again after the test run and report assembly against the in-memory refreshed inventory; all 21 current inputs were unchanged.

    199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
    f7d3d22e48aac6ed90d4b041c317b10ecf99a538e02e09cf5183fd46d25af95a  docs/README.md
    19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  docs/arctan_limits.md
    0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362  docs/continuous_depth.md
    486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
    a12a4f2541dd989a01920541f07ce8f80058b88d3e19db65c4b376c1fcf6653e  docs/finite_optimization_and_controls.md
    cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
    becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95  docs/global_nonlinear.md
    36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b  docs/linear_dynamics.md
    e491ea163cf325ced50a3f1d19ab79cf9f84df85977ad644b68f4c96775e36ea  docs/special_data_limits.md
    0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
    65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
    efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
    6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
    7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
    a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
    9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
    375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
    c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
    740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
    c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt

## 6. Handoff disposition

- Original isolated integration round: NOT CLEAN on its original hashes; preserved in ROUND1.md.
- This same audit's current-input addendum: CLEAN for the seven specified edits and their immediate dependencies; R1 and R2 closed, horizon wording accepted.
- Gaussian and linear full-proof acceptances: carried forward only for the frozen unchanged hashes above.
- Fresh independent whole-library final round: not performed or claimed here; to be commissioned by the main task.

No input repair or refactor was performed. Only this addendum and the restoration/renaming of this audit's own original report were written.

