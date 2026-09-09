# Shallow feature-step discretization assembly

This is an author assembly and dependency record, not an independent acceptance
review. The candidate is
[SHALLOW_DISCRETIZATION_ADDITION.md](../SHALLOW_DISCRETIZATION_ADDITION.md).
It is intended as Section 11 of the existing Gaussian-calculus chapter.
Only that candidate and this record were authored by this assembly worker;
no Git operation, shared-record edit, maintained-file edit, training run, or
historical coefficient campaign was performed.

## Added result and exact contract

The primary source has a complete uniform shallow theorem, beyond the
maintained fixed-program remainder and the separately maintained shallow
physical-GF comparison. The candidate imports:

1. Exact expectation identification at every finite width, because feature
   ascent leaves the independent neuron pairs independent.
2. The explicit bound
   \(|F_{k,1}(2h)-F_{2k,1}(h)+k(2k-1)J_\phi h^3/2|
   \le B_\phi^{\rm sh}k^4|h|^5\), for every integer \(k\ge1\) and
   \(|h|\le(16M_\phi k)^{-1}\).
3. The complete finite scalar-envelope recursion defining the constant,
   the Gaussian-integrability proof, exact noncommuting defect telescope,
   transported directions, derivative bookkeeping, and direct cubic
   coefficient calculation.
4. Identity-activation sharpness of the fourth power in the update count.
5. The separately persisted dyadic consequence, specialized with all constants:
   uniform convergence of terminal expected outputs on
   \(|s|\le S\le2c_\phi\), with explicit error proportional to \(2^{-p}\).

The preserved model is one scalar input and one hidden layer, independent
standard Gaussian first weights and **order-one stored readout**, no biases,
both feature-ascent mobilities \(n\), and simultaneous raw Euler updates.
The activation remains \(C^{12}\), normalized by \(E\phi(G)^2=1\), with linear
growth and bounded derivatives through order 12. The proof needs fewer
derivatives, but this assembly does not enlarge its persisted activation class.
The clock is feature ascent with step \(h\), not physical full-loss GD with a
moving residual. Width-first expectation identification precedes differentiation.
There is no joint width/refinement theorem or population physical-loss GD theorem.

## Full source reads and hashes

Every file in the following table was read completely, including its proof
or correction content. The alternate producer and loss-time source were read
for scope reconciliation and contribute no uncontained proof dependency.

| File under repository root | Lines | SHA-256 |
|---|---:|---|
| studies/mfp_depth_time_doubling/UNIFORM_L1.md | 687 | 0be27a8851562cfe063d919581dc57cbdcdc5d6ca3053010b4ed70af545964e1 |
| studies/mfp_depth_time_doubling/AUDIT_UNIFORM_L1.md | 182 | 82d19dcbb90f9965361e174abbf7fe5e8c80472e2a6f607a3dcc4f8d2a06b76e |
| studies/mfp_depth_time_doubling/UNIFORM_BSERIES.md | 567 | cc125b6a393845b0b18f5cdbc5e76cc61ff8afbb2a69dc0c718909c96b7b88a5 |
| studies/mfp_depth_time_doubling/AUDIT_UNIFORM_BSERIES.md | 179 | ce1535ec56904d1ab362befb0864329fbe9b7199a783dc669267f6176f2f817a |
| studies/mfp_depth_time_doubling/AUDIT_DYADIC_CONVERGENCE.md | 226 | 121253a1015edf681436b2c248bf87b5cb0c405a8f441a84595633578fd58e4e |
| studies/mfp_depth_time_doubling/AUDIT_UNIFORM_L23.md | 351 | 6d2f46abc48fcc6cecf3b610fc55839f959acf5b906d4fd74037432205b8b5c4 |
| studies/mfp_depth_time_doubling/AUDIT_UNCONDITIONAL.md | 259 | 205aa0e0cc20abaa05f1ec3d0db0afd33d58e329bc3d2e7312468e28b7492973 |
| studies/mfp_depth_time_doubling/AUDIT_RELEASE_ASSEMBLY.md | 121 | 83a21cee6f5a0fa5bb6ba19c184d8cb2d10722394ef06c25ec57c2211e69e3e9 |
| studies/mfp_depth_time_doubling/RESEARCH_CONTRACT.md | 104 | de6c8cdeecde7a047eb5321d779fcc18de43b95045d9eff56f5bf0380ae9ec08 |
| studies/mfp_depth_time_doubling/RESEARCH_STATE.md | 120 | c0cf73cc4152186de4a8880a332e1acd02abb7dab1e64f53e97a654304d5fda0 |
| studies/mfp_depth_time_doubling/EVIDENCE_LEDGER.md | 16 | 70f7034a74d5b3374a16e89d81c467d0c011723e1883767851cab987ffae246b |
| studies/mfp_general_depth_general_time_stepdoubling_bound/SCALAR_QUANTITATIVE_THEOREM.md | 162 | c1012acb7ba53a810c0b77a845a5624f486817283aaa23e7104025793bf1d403 |
| studies/mfp_loss_time_doubling/LOSS_TIMECHANGE_ANALYSIS.md | 373 | d88c9022a8afb31db27254f78c40238087ceea41d9ea34c8ce6c53ff380db1d7 |
| docs/NOTATION.md | 98 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

The total primary/context source read is 3,347 lines excluding notation.
The complete maintained shallow comparison was read at
docs/linear_dynamics.md lines 1357–1571. The quantitative fixed-program
statement and endpoint scope were read at docs/gaussian_calculus.md
lines 2438–2524 and 3203–3301.
These readings identify the additional scope; their proofs are not invoked
to establish the new theorem. The promotion-completeness report, current
coverage/disposition/ledger, and historical master were consulted as source
locators and for supersession. This is not a new full audit of those reports.

The worker personally read both required skills:
/etc/codex/skills/solve-math-rigorously/SKILL.md and
/etc/codex/skills/investigate-conjectures/SKILL.md, and the latter's
research-contract.md, evidence-ledger.md, and adversarial-audit.md.
No new conjecture search or experiment was opened.

## Corrections, dependencies, and rejected inferences

- The source's update-count variable became \(k\); \(t\) remains physical
  time. The feature step stays \(h\), distinct from \(\eta_n\) and the proof mesh.
- Finite state norms are ordinary Euclidean norms. The source's scalar
  growth expression \(1+|a|+|u|\) is retained as an explicit envelope rather
  than a renamed finite RMS norm. The derivative bounds \(6MR\) and \(5MR\)
  remain valid: every coordinate of a Euclidean unit direction is at most
  one, and summing the at-most-five derivative placements gives those bounds.
- Population fields use \(A_j=W_j^{(2)},U_j=Z_j^{(1)}\) on one explicitly
  defined mark space; finite raw coordinates remain \(a_i,u_i\).
  Auxiliary envelope names do not overwrite network weight notation.
- The local interpolation is a convex combination of two Euler endpoints,
  not an Euler step. The repaired source's explicit \(4k+2k\) path allowance
  and all four derivative domination bounds were retained.
- Sign parity is applied only after averaging over the symmetric readout.
  The exact cubic calculation uses elementary two-coordinate derivatives,
  so no general-depth nine-moment identity, marked compiler, response
  operator construction, or historical verdict enters its proof.
- The alternative scalar-quantitative producer is not silently identified
  with this producer. Its Bell-polynomial proof is not needed or cited.
- Dyadic comparison uses \(h=s/(2k)\), with the exact factors \(1/8,1/32\)
  and radius \(S\le2c_\phi\). It proves a continuous scalar terminal-output
  limit only. It does not assert Lipschitzness, a restartable state,
  arbitrary partitions, an all-feature-time result, or loss-time convergence.
- The reused-matrix depths still require the unresolved horizon-uniform
  mixed response estimates described in their own sources. The abstract
  Banach-space result is not applied to an ambient population \(L^2\) space.
  A source audit's “if and only if” phrasing around a sufficient third
  derivative estimate is not imported.
- Elementary finite-dimensional calculus, Gaussian integrability, and the
  dominated differentiation steps are all supplied. No specialized external
  theorem is imported. There are no maintained references to studies,
  historical verdicts, temporary paths, computational arrays, or chats.

## Author checks and candidate fingerprint

The candidate was reread completely after assembly. A deterministic exact
Fraction/integer check verified for every \(k=1,\ldots,64\) the identity
cubic and fifth coefficients and both separate S/H time-polynomial
coefficients in (SD33)–(SD36). This is a bounded algebra check, not an
experiment and not a substitute for independent proof review.

The final fragment contains 551 lines, 40 uniquely numbered equations,
190 balanced inline-math pairs and 40 balanced display-math pairs.
SHA-256:
4321fc6bf9fdddedccb752072f3326134d514edbdd576c328923432e4345efd9.
Its only mathematical input besides the complete fragment is the canonical
notation contract; the Section 8 mention is an editorial comparison.
Independent reviewers should receive the complete fragment and notation,
without this historical source record or previous review verdicts.
