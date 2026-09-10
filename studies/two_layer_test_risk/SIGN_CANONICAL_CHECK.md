# Internal check of the signed canonical assembly

Checker: `sign_canonical_check`, 2026-09-10. Base HEAD:
`df1117948764a984e7fd2d28949a3c87bc284f84`.

This is an internal assembly check, not an isolated scientific review, a
promotion verdict, or an integration acceptance. I inherited the coordinator's
assignment and read the current study record. I am therefore not eligible to
fill either fresh scientific reviewer role. I changed only this report and
the assigned generated scratch. No staging, commit, maintained-file edit,
coefficient integration, training, or source repair was performed.

**Outcome:** the assembled proof preserves the complete mathematical content
of its base and four certificate sources, and the checked exact scalar bounds
pass. The candidate needs the notation and process-language corrections below
before the intended fresh review freeze. I found no changed loss factor, lost
response term, reversed risk sign, or erroneous displayed rational comparison.
This does not certify the still-separately-assembled executing code.

## Complete read coverage and limits

Read completely: root `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`, the
study README, `docs/README.md` (265 lines), `docs/NOTATION.md` (98),
`code/README.md` (591), `PROMOTION_C4.md` (642), `PROMOTION_SIGN_C4.md` (1687),
`build_signed_candidate.py` (241), `CERTIFIED_ERROR.md` (339),
`CERTIFICATION_ENGINE.md` (301), `ANGULAR_CERTIFICATE.md` (214),
`DRIVER_CERTIFICATION.md` (270), `PROMOTION_SIGN_DOCS_README.md` (271), and
`PROMOTION_CODE_README_APPENDIX.md` (29). Initial combined-output truncations
were repaired by subsequent explicit reads. The required
`/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely and used.

Additional limited read scope: chapter headings of `docs/global_nonlinear.md`
to confirm the destinations of the unchanged C.1--C.3, Sections 2--3 and
A.1--A.4 references; the beginning through line 120 of
`assemble_signed_promotion.py`, plus its destination mapping extracted by AST,
to check future relative links. The older chapter proof bodies, pending code
candidate, kernel implementation, tests, tool guide, retained coefficient
arrays, and prior reviewer reports were not audited here. No whole-book proof
or new executing-certificate claim follows from this report.

## Required canonical corrections

All locations below refer to the 1687-line candidate with SHA-256
`ae5eff6e5c351410355048f56f8b429383612cbf30558178069e0f8692b2025f`.
These are canonical presentation/interface corrections; none calls for a new
coefficient calculation or a change of model.

1. **Use the shared population and derivative notation throughout the
   certificate.** Lines 737--776 introduce scalar aliases `H,D,E`; lines
   898--924 use `D_a,E_a` for gates; lines 972--1005 introduce `d,dd` and
   unqualified `H`; lines 1207--1216 and 1293--1370 use lower-case population
   `h,e` and upper `H,d,d'`; lines 1523--1594 repeat those symbols.
   `docs/NOTATION.md` explicitly says to write activation derivatives as
   `phi'` rather than introducing another derivative name, and to capitalize
   population hidden fields. The original C.4 already uses `H_i^(1)`,
   `H_i^(2)`, `phi'(Z_i)`, `phi'(Y_i)`, and `phi''(Y_i)`. Continue those exact
   symbols. Use `phi(z),phi'(z),phi''(z)` in the strip and derivative lemmas,
   and `E_1`/`E_2` for the corresponding lower/upper expectations. In
   particular `E_a` in the certificate currently collides with the already
   defined upper hidden-response field in (C4.5), and `B_x` in the angular
   expansion can collide with the lower field `B_b`. Suitable scalar names
   are `mathcal F(x),mathcal B(x)` for the two angular contributions.
   Preserve literal output keys such as `dynamic_dd`, `ESdd_bits`, and
   `T_bits` as implementation identifiers, with their mathematical values
   written in canonical notation. Use `mathcal T_abij`, not an undeclared
   `T_abij`, for the tensor of (C4.27); instances include lines 1004, 1525,
   and 1572. This also avoids confusion with the initialized field `T_x`.

2. **Separate mathematical indices and conditional-root integration from
   the array interface.** Lines 78--80 declare training indices 1,2,3 and
   (C4.27) uses formal slots `{x,1,2,3}`, but line 972 switches to training
   0,1,2 and passive 3; line 1565 calls the passive symbol `x=3`. Keep the
   mathematics at 1,2,3 and x, and state the code map explicitly:
   `(math 1,2,3,x) -> (array 0,1,2,3)`. The three entries of `p` have the
   same mapping and array slot 3 has weight zero. Line 982 uses `E_4` for
   integrating the fourth independent root. This contradicts the declared
   rule that `E_ell` denotes population ell and introduces a nonexistent
   fourth population. Instead define the conditional moments by
   `integral phi^(r)(mu_x+sigma_x u) gamma(u) du`, `r=0,1,2`, conditional
   on the first three roots. The law `Y_x=mu_x+sigma_x xi_4` also keeps
   the conditional mean distinct from the sample count `m`.

3. **Remove the undefined risk-difference alias.** Lines 1622--1623 use
   `Delta(t)` without defining it anywhere in the candidate. Plain `Delta`
   is reserved for a proof mesh by the notation contract. Replace each
   occurrence by `R(g_tau(t))-R(f_t)`, which is already used in (C4.7)--(C4.8).
   In the theorem at line 111 also replace the inherited shorthand
   `L(g_tau(t))=L(f_t)` by `mathcal L(g_tau(t))=mathcal L(f_t)` or
   `L_g(tau(t))=L_f(t)`; those, rather than plain `L`, are the defined loss
   functions.

4. **Remove the surviving study-process statements.** Lines 1004--1006
   retain “No pair/triple-only factorization ... was found,” a report of a
   search rather than mathematical content. Replace it by the concrete fact
   that expanding `S^2 phi'(Y_x)phi'(Y_b)` includes terms involving four
   named upper slots, and conditional integration preserves that joint law.
   Lines 1618--1619 say the final claim “remains conditional on inspection”
   of the sources. Inspection is a review procedure, not a hypothesis of
   the theorem. State instead that the enclosure follows jointly from the
   analytic estimates and the stated arithmetic/runtime contracts, and a
   positive flag alone is insufficient. The final evaluated section already
   makes that distinction correctly. Generic references to the “original
   derivation” can point directly to (C4.27)--(C4.31).

5. **Use one stable label-magnitude bound.** Lines 768 and 1187 define
   `P=sum_a|p_a|=(1+sqrt(5))/6`, whereas line 1434 assigns `P=27/50`.
   The inequalities remain valid, but the same symbol changes exact value
   across proof sections. Keep `P=sum_a|p_a|` and name the rational upper
   bound `P_*:=27/50`, or use `P:=27/50` consistently as a bound. The
   executing dyadic labels and exact labels must both be bounded by the
   chosen common rational constant in the covariance and label-error table.

The builder must make these changes reproducibly, rather than leaving the
rendered candidate inconsistent with `build_signed_candidate.py`.

## Verified preservation, normalization, and scalar bounds

An in-memory execution of the complete builder intercepted both `write_text`
calls and compared their contents with the candidate files. Both were exactly
identical. The printed builder line says “Wrote”, but the check intercepted
the write; the source files were not modified. After reversing only heading
levels and equation-tag prefixes, separate complete source/candidate diffs
were generated and read. They show:

- The 642-line base changes only its title, formerly open-sign statements,
  displayed signed bound, and its corresponding conclusions. All model,
  population capture, unique matching, fourth-moment, actual-flow remainder,
  Gaussian contraction, and finite-clock proof steps are retained.
- All five mathematical sections of `CERTIFIED_ERROR.md` survive. Removed
  material is author/source history, provenance, and dated check discussion.
- The engine's exact conditional reduction, interface, elementary arithmetic
  proof and full uniform-error proof survive. Removed execution history,
  planning costs, environment discovery and ownership notes contain no
  missing proof premise; root-factor covariance treatment is retained in
  the covariance and driver sections.
- The complete angular proof survives, including both matrix responses,
  singular-covariance-safe differentiation, all rational majorants,
  Fourier-error proof, and exact symmetry reduction.
- The complete interval-assembly proof survives; its removed source-run
  and ownership discussion is replaced by maintained destination links.

The base equations retain `p=y/3`, mean square loss, mobilities `(n,1,n)`,
small *stored* readout variance `1/n^2`, correlated rank-two G, both directions
of the reused connector and the full response mean-product term. The loss
derivative at zero is `-4B_0`, the clock coefficient is
`beta=8 mathcal A/(3B_0)`, and the risk sign is
`R(frozen at matched loss)-R(learned)`. With `chi>27/100000` and
`Mt<=27/200000`, the claimed lower risk difference `27 t^3/200000` follows.
The whole-circle teacher has squared mean `1/2`, so the initial-risk display
is consistent. No finite-width order reduction or width rate was introduced.

All 60 local equation tags are unique and all parenthesized local equation
references resolve. The numbered external section names exist in the intended
chapter; their proof bodies remain the responsibility of the full review.

The independent exact-rational check passed every following comparison:

- Both chi endpoints of (C4.32) lie strictly inside
  `(27/100000,273/1000000)`; both beta endpoints of (C4.33) lie strictly
  inside `(35309/1000000,35311/1000000)` and `(0,1/10)`.
- A new implementation of the Stirling/Bell and convolution recurrences in
  (C4.A2)--(C4.A9), written solely from those displayed formulas, gives
  `D_8=41272525446939874982/31640625` and
  `16D_8/(7*256^8)=20636262723469937491/127677049435953561600000000<10^-6`
  exactly. This was a scalar derivative-bound check, not a coefficient run.
- The degree-80 rational partial sums prove all three stated exponential
  lower bounds at 26, 30 and 32. Inserting those bounds into the geometric
  mass factor verifies both target-26 error components and the target-30
  envelope.
- The initial exponential rounding bound is strictly below `46*2^-53`;
  eight squarings give a bound below `2e-12`; and
  `4 gamma_64481201(2^-64)<1.5e-11`.

The displayed exact endpoints were checked arithmetically, not reconstructed
from retained Gaussian primitive outputs. The 86,101,134 node-count claim and
code-to-enclosure correspondence were not independently re-established here.

## Guides, placement, and optional improvements

The complete proposed reading guide correctly adds one fixed-design,
computer-assisted early-time test-risk result and withdraws the old blanket
claim that no proof requires executing a calculation. It retains the
distinctions between optimization, generalization, local capture and growing
limits. The code appendix is compatible with the complete existing guide:
it introduces an opt-in fixed coefficient command, explains the independent
compiler/platform requirement, and makes no training-solver or general
quadrature claim. No required scope correction was found in either guide.

All local links in the two guide candidates and C.4 resolve against the
declared future destinations and current source-to-destination map, including
`certificate.py`, `certificate_kernel.cpp`, `angle_error_bound.py`, and the
tool README. This verifies path planning, not the still-pending tool's API,
dependencies or behavior. No live tool path was assumed already installed.

Optional editorial improvements:

- Extend the proof-roadmap paragraph at lines 151--154 to mention the
  subsequent Gaussian, arithmetic, angular and final interval certificates.
- Distinguish the two finite scalar contributions to J with calligraphic
  function names, and state `J(alpha):=J(x(alpha))`, `a(alpha):=a(x(alpha))`
  once. This makes the parameter-versus-input distinction explicit.
- In the symmetry argument at lines 1373--1377, replace “reflection of both
  initial roots” by the exact transformation
  `(xi_1,xi_2)->(xi_1,-xi_2)` together with training indices 2 and 3 exchanged.
  The separate antipodal transformation already has the correct sign.
- Add a blank line before line 654's certificate heading and rewrap the
  few very long prose lines left by literal replacement. These do not
  affect the mathematical argument or Markdown heading recognition.

## Evidence and reproduction

Working directory for every command: `/home/amir/Codes/PDE`. Python:
`3.10.12`. Generated scratch:
`data/generated/two_layer_test_risk/canonical_check_20260910_01/`.

The deterministic check command was

```sh
python -B data/generated/two_layer_test_risk/canonical_check_20260910_01/check.py > data/generated/two_layer_test_risk/canonical_check_20260910_01/check_stdout.txt
```

Exit status 0. `checks.json` records the boolean results, exact scalar values,
strict margins and individual future links. The five
`*_correspondence.diff` files record complete correspondence checks.
`input_sha256.txt` records the complete read-input hashes. A final
`sha256sum -c data/generated/two_layer_test_risk/canonical_check_20260910_01/input_sha256.txt`
returned OK for every input before this report was written. The maintained
guide and limited-read mapping source had these additional hashes:

```text
00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774  code/README.md
2d3c66b40b0face15120c7993e838608e1ef33c080bc474cc3e070148fb89902  studies/two_layer_test_risk/assemble_signed_promotion.py
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7  /etc/codex/skills/solve-math-rigorously/SKILL.md
```

The essential complete source hashes are retained here as well:

```text
a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517  AGENTS.md
4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442  RESEARCH_WORKFLOW.md
4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453  docs/README.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
5049d0ecb7fcf0bb349adcbcf39ff8b24466b33b78868749c8b02e241ac0652e  studies/two_layer_test_risk/README.md
ae5eff6e5c351410355048f56f8b429383612cbf30558178069e0f8692b2025f  studies/two_layer_test_risk/PROMOTION_SIGN_C4.md
af0b4089124aafcd8006b7b9372fc0a4a338fa4ef2f4b66fe3a08ec4ec0c6dce  studies/two_layer_test_risk/build_signed_candidate.py
b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4  studies/two_layer_test_risk/PROMOTION_C4.md
bcf7fa482d948b73c7ba82b60f514776dbd6d3609a3fb429744aaf507a76c9ad  studies/two_layer_test_risk/CERTIFIED_ERROR.md
52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16  studies/two_layer_test_risk/CERTIFICATION_ENGINE.md
a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2  studies/two_layer_test_risk/ANGULAR_CERTIFICATE.md
871a474c95a36790604c882949ad1cd5870d0965fe11d16c3380fa134793f3de  studies/two_layer_test_risk/DRIVER_CERTIFICATION.md
a41cdf2731891342a3552aae5611206f594efa693e0ffd9a3f01d95e9b560235  studies/two_layer_test_risk/PROMOTION_SIGN_DOCS_README.md
a6e26edb768c601f09d6bf78f61f387c810a2326c29f5ed16c57808c91180e17  studies/two_layer_test_risk/PROMOTION_CODE_README_APPENDIX.md
```

The report applies only to these inputs. After the required canonical fixes,
the coordinator should check the new source correspondence, then freeze the
complete final theory, code, guides and dependencies for the two fresh
scientific reviews and separate integration review required by the workflow.
