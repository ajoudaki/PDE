# Central theory promotion audit

Read-only planning, 9 September 2026. No repository changes, Git operations, numerical experiments, or historical proof campaign. This private report is the only authored file. The mathematical verification workflow follows `/etc/codex/skills/solve-math-rigorously/SKILL.md`.

## Recommendation

The five requested source manuscripts form a sufficient, minimal **file-level donor closure** for the central bundle: L2 small-readout one-input atan global joint limit; L3 small-readout one-input atan local joint limit; every separately fixed hidden depth L>=3 shifted-atan one-input global joint limit; L3 deep-linear one-input global joint limit; and its restricted scalar/PDE nonclosure boundary. All five were read completely, including their proofs, not accepted from historical PASS labels. No decisive theorem-level gap was found in these precise scopes.

This is readiness for a careful mathematical rewrite, not permission to copy all five verbatim into established theory. The L3 assembly retains references and standalone-note conditional wording that must be resolved internally. The linear manuscript also contains an optional free-probability presentation whose construction is not fully explained, and a historical external-theorem audit that is not a dependency and should be omitted. The required core has an internal route avoiding both.

Use three substantial chapters, with a shared notation/preliminaries section inside `docs/` as the main agent's architecture permits:

1. **Arctangent operator limits:** L2 global and L3 local, with the complete source construction and analytic bridges.
2. **Global nonlinear learning at fixed depth:** the single shifted-atan activation, its depth induction, physical clock, fitting and persistent activity.
3. **Deep-linear dynamics and contraction closure boundaries:** the global joint theorem, fitting, scalar/PDE restrictions and the exact counterexample to an unrestricted PDE prohibition.

Do not turn the six embedded L3 notes into six tiny chapters. Reuse common lemmas only through internal `docs/` statements and proofs; do not replace the stronger source-response lemma by the weaker fixed-law statement during deduplication. Historical provenance can live outside established theory and point into `docs/`; no reverse reference is needed.

## Exact files and reading coverage

Paths below are absolute and identify current donor files. Line counts use `wc -l`. Full read means every line was displayed and read; truncated passages were reread in smaller ranges. Secondary audits were consulted selectively only after the principal proofs; they are not members of the proof closure.

| ID | Source | Lines | Full-proof read | Disposition |
|---|---|---:|---|---|
| A | `/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md` | 543 | 1–543, complete | Ready at its stated global one-input small-readout scope |
| B | `/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md` | 2321 | 1–2321, complete | Ready as an assembled local theorem; resolve internal note references |
| C | `/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/SHIFTED_ATAN_ALL_DEPTHS/GENERAL_DEPTH_SELF_CONTAINED_PROOF.md` | 1727 | 1–1727, complete | Ready for every separately fixed L>=3; one specified activation and input/target |
| D | `/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_joint_audit/JOINT_DEEP_LINEAR_THEOREM.md` | 1065 | 1–1065, complete | Core ready; Q-only Euler clarification and optional free-probability scope need editorial handling |
| E | `/home/amir/Codes/PDE/studies/mean_field_peeling/temporary_deep_linear_pde_no_go/PDE_CLOSURE_BOUNDARY.md` | 654 | 1–654, complete | Ready only with its full encoder/readout/state-domain restrictions |
| | Total | **6310** | **All five full proofs read** | |

Orientation read: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md` (653 lines) and `REVIEW_STATUS.md` in that directory (67 lines). The CLEAN reviews there certify the qualified synthesis, not every source theorem. The source manuscripts above, rather than those reviews, support this recommendation.

## A: L2 pure atan, global joint theorem

Use A as the complete donor, including its 543-line proof. No additional old arctan manuscript, tensor-program theorem, or broad-activation extension is required.

- Lines 3–31: one input and target equal to one; first coordinates N(0,1), middle entries N(0,1/n), stored readout coordinates N(0,n^-2); full square loss; exact raw GD with eta_n sqrt(n) -> 0. Do not reduce its stated mesh scope to n^-2 or enlarge it to all vanishing meshes.
- Lines 129–239: internal fixed-program Gaussian proof, query jitter, singular-direction removal, common generated spaces and true adjoints. Its claim is joint W2/continuous quadratic-growth tests for globally Lipschitz instructions, not the broader all-moment scalar-feedback theorem disputed in the master.
- Lines 241–348: transformed-coordinate existence, width-independent stability, gradient identity and global finite-horizon bounds. The proof uses bounded readout values; ordinary L2 bounds on a variable multiplier alone would not suffice.
- Lines 350–418: deterministic-coefficient oracle, exact discrepancy of its stored matrix action, restoration of empirical feedback, fixed-mesh width passage, then mesh refinement and autonomous measured-law restart.
- Lines 420–486: actual raw-GD cubic defect, same-width flow comparison, uniform square tails, all three kernels, integrated preactivation speeds and W2 whole-path laws.
- Lines 488–542: positive small-time hidden movement, changing kernel and persistent nonaffinity on an initial interval.

Scope guard: A does not supply a general arbitrary-label fitting theorem or every-positive-time activity. Preserve the actual continuous quadratic test class and bounded-factor restrictions. Global existence/identification does not imply a uniform approximation on all time.

## B: L3 local pure atan, and why its complete assembly matters

B alone contains the full six-note proof closure. Its opening theorem is lines 1–206; stopping there is insufficient. The following actual proof bodies are embedded:

| Embedded body | Line interval in B | Role |
|---|---:|---|
| Fixed-mesh source identification | 211–451 | Interleaved matrices, both transposes, response derivatives, singular queries, empirical feedback |
| Common population action spaces and fixed-cap flows | 456–725 | Bounded actions, actual adjoints, complete state class, fixed-cap width/mesh bridge |
| Local response bootstrap | 730–1051 | Mesh- and cap-uniform reference tail bound with explicit local horizon |
| Cutoff removal and actual-GD bridge | 1056–1743 | Uncut construction, uniqueness/restart, finite comparison, random clock, interpolation and observables |
| Gradient structure | 1748–1914 | Raw Hilbert metric, differentiability of the scalar predictor, four kernels |
| Feature learning | 1919–2321 | Initial transpose responses, all-layer motion, changing kernel and local nonaffinity |

The conditional-sounding “Representation premise” at lines 1059–1063 and 1121–1143 is discharged by the earlier bodies in this same file. Likewise the feature-learning note assumes the already constructed flow. These are not new mathematical hypotheses of the assembled local theorem. However, promoting either note alone would leave a conditional result.

Replace the `/tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md` reference at line 462 by the internal source-law lemma. Replace the mention of `TWO_HIDDEN_LAYER_PROOF.md` at line 1393 by B's own query-jitter proof at 379–402; no missing L2 donor is needed for that step. Replace all six note filenames in the opening and later text by internal theorem/section references. Remove historical “main goal” and “this note does not prove” framing while retaining accurate theorem domains.

The source law is stronger than a mere Gaussian averaging statement: it identifies the full expected source derivative with coefficients and covariances held fixed. Its current-step return through the next matrix appears explicitly at 436–445. The bootstrap uses those exact coefficients. Preserve both pieces when sharing preliminaries.

The stated local physical interval is T0 = (1/4) min{S0, 1/(4a^2)}, a=pi/2, with explicit S0 from lines 56–69 and 974–978. The raw mesh is n^-2. Restart means uniqueness along the reached trajectory within this interval; it does not grant another interval of length T0 at its endpoint. The theorem is complete as a local theorem. A global uncut theorem remains outside promotion scope.

## C: fixed-depth shifted atan, global joint theorem

C is already a single mathematical proof with no indispensable research-paper or study-file import. Keep Sections 1–12 together, or resolve shared material internally without dropping a bridge.

Its key closure is:

- Sections 2–5 (lines 145–756): elementary probability tools, finite Gaussian source/response proof, all orientations, singular covariance, actual clipped training feedback, common spaces and fixed-cap flow comparison.
- Section 6 (757–940): causal induction over time, forward through all layers, then backward through all layers. It proves the actual response rows and exponential query bound uniformly through feature time 3/2, independently of cap and mesh.
- Sections 7–8 (941–1076): comparison grows linearly with cap, reference square tails decay quadratically in the exponent, so cap removal, uniqueness and finite uncut identification close. Operator/primal bounds alone are not substituted for this argument.
- Section 9 (1077–1197): true raw gradient, readout kernel >=25/36, first f=1 feature time <=36/25<3/2, divergent physical clock at that first hit, global physical uniqueness and restart.
- Sections 10–11 (1198–1459): actual raw-GD transform defect, stopped positive random feature clock, all endpoint/interpolation checks, every named kernel/action/velocity and whole-path measurements.
- Section 12 (1460–1727): second-order hidden onset, nonconstant kernel, nonaffinity on every compact horizon and nonzero hidden speeds at every finite positive time.

Exact scope: every separately fixed L>=3, one input and target equal to one, phi(z)=1+atan(z)/10 at every layer, small stored readout, full square loss, raw mesh n^-2. The same activation is independent of depth and time. The response estimate has depth-independent constants; the whole theorem does not have depth-uniform constants. Do not transfer this result to unshifted atan, multiple inputs or a joint depth/width limit.

Fitting is an elementary consequence of the internal proof: from dL/dt=-4LK and K>=25/36, L(t)<=exp(-25t/9). No new fitting premise or general optimization theorem is required.

## D and E: global linear dynamics and the restricted nonclosure boundary

D Sections 1–7 (lines 1–803) contain the core global population/finite-GF/exact-GD proof and scalar-contraction negative. It supplies its own colored Fock source, Gaussian fixed-word/rooted Gram lemma, elementary matrix norm bound, trace-norm energy estimate, finite-rank Gram comparison and factorial Picard approximation. E provides the more carefully formulated graph-independence proof and the full PDE restriction/transport boundary.

Necessary details during promotion:

1. **Use the clarified graph argument in E 167–215 once.** Its quotient closure uses auxiliary incidence networks of arbitrary index valence. This makes explicit the auxiliary class only implicit in D 233–258. Both scalar and PDE negatives can reference this proved internal lemma.
2. **Write the GD bridge as Euler for Q alone.** At D 759–802, e_k = y - Tr(C0+Q_k)^4/4 is recomputed from Q_k. It is not an independent Euler variable. Section 6's “same cutoff” wording refers to an augmented (Q,e) flow; for GD explicitly use V(Q)=2 kappa [y-Tr(C0+Q)^4/4](C0*+Q*)^3 and a Q-space cutoff with a strict margin above the energy ball. The existing trace Lipschitz and cubic estimates already prove the required bounds. This is a concrete exposition repair, not an unproved theorem-level extension.
3. **The optional free-Wishart presentation is not a minimal prerequisite.** D 841–918 introduces free MP variables, a reduced free-product GNS space and a spectral square-root lift without fully constructing them. Under a literal self-contained exposition rule, do not copy this passage without definitions and its source identification. The cyclic Fock proof already proves the core theorem without it. Its optional noncommutative moment example at 937–955 also presupposes the free-probability vocabulary. E's finite algebraic counterexamples suffice to explain the restricted boundary without importing that vocabulary.
4. **Delete D Section 10 (1002–1045) from established theory.** It is an audit of a superseded external theorem invocation, explicitly not a dependency of the current proof. No external papers need to be fetched or recursively audited to promote Sections 1–7. Keep historical claims out of the theorem's dependency chain.
5. **Keep the zero-label distinction.** The linear population trajectory is stationary when y=0, but E's state-universal nonclosure theorem still holds for y=0. A stationary initialized orbit does not contradict a statement about all states in the stipulated domain.

The fixed-word Wick count in D 443–478 and 520–525 is concise. Preserve the actual pairing/index-count argument and its variance calculation, not just a sentence invoking a random-matrix limit. An expanded explanation of the elementary pairing induction would improve exposition; this audit did not identify a missing imported research theorem there.

### Retaining linear fitting without the optional free-probability construction

Fitting can be stated entirely in the cyclic factor representation already constructed in D Sections 4–5. This is a direct specialization of D's exact algebra at 810–839 and fitting argument at 903–931; no new source manuscript or conjectural bridge is needed.

Use the original unit-Hilbert-norm factors x,a,B,R of D in this paragraph. Put z=Bx, p=R*a, A=BB*+||x||^2 I and M=R*R+||a||^2 I. The exact product rule gives

    f=<z,p>,    K=<p,Ap>+<z,Mz>.

Both endpoint squared norms start at one, and each physical derivative equals 4 kappa e f. Write their common value as q. Since e(t)=y exp(-2 kappa integral_0^t K), f=y-e has the same sign as y, hence ef>=0 and q>=1. Therefore

    K >= q (||z||^2+||p||^2) >= 2|f|.

For y!=0, K(0)=4 gives f'(0)=8 kappa y. Thus choose t1>0 with |f(t1)|>0. The scalar equation implies |f(t)| is nondecreasing, so K(t)>=2|f(t1)| for t>=t1. Consequently

    |e(t)| <= |e(t1)| exp(-4 kappa |f(t1)|(t-t1)),

and the loss tends to zero. If y=0, Q=0 is the unique stationary solution. This uses only the existing global cyclic flow and avoids defining free MP variables or GNS spaces. It should appear as a short corollary inside the linear chapter if fitting is retained.

### Exact negative scope

E is a complete standalone proof in its bounded-contraction class, not a proof of unrestricted PDE impossibility. Preserve:

- uniformly bounded tensor degree in the current-state encoder, with a finite alphabet of typed complete contractions;
- a fixed finite number of fields, spatial variables and finite differential/readout orders;
- polynomial local differential expressions/readout on a nonempty open state set, or the specified analytic domains on a full neighborhood of the zero network and its realized zero-state jets;
- state-universal identities for all sufficiently large widths, not only the Gaussian orbit;
- the separate physical-flow proof, including y=0;
- the width-uniform local-finiteness premise of the optional jet-complexity corollary in E 604–631.

E Sections 10–12 explain why field count alone cannot be the obstruction: the transport encoder initializes its profile with the whole future output. It is a valid counterexample to an unrestricted encoder theorem, not a predictive population construction. Keep that distinction explicit. Do not add the separate tagged-branch/Hilbert-series negative or older conditional arbitrary-depth notes to this central bundle.

## Canonical notation conversion and risk

Make conversions by mathematical role and layer, not global text replacement. The sources reuse letters with different meanings even inside one assembled file.

| Source notation | Canonical rendering/action | Risk if omitted |
|---|---|---|
| W with subscript/superscript or A,B,C aliases for actual weights | W^(ell); B's fixed-mesh A=W^(2), B=W^(3), C=W^(4) | A later B_2 is a backward field, not W^(3) |
| Z^(ell), H^(ell), Z_ell, H_ell and scalar-program aliases | z^(ell), h^(ell), with finite n and population probability-space types made explicit | Capitalization alone currently distinguishes some finite and population objects |
| d(z), d=phi', D_ell, D_ell,0 | Explicit phi'(z^(ell)); finite multiplication uses diag(phi'(z^(ell))) where an operator is necessary; population use [phi'(z^(ell)) u] | Hidden derivative gates are easy to lose in adjoint or velocity formulas |
| top, mathsf T | T for every finite matrix transpose | Do not change population * to T |
| Population reverse calls | Actual Hilbert-space adjoint * | Reverse Gaussian sources being independent does not make W and W* independent |
| ||v||_n and <u,v>_n in B | ||v||_2/sqrt(n) and u^T v/n | Explicit width factors disappear under naive notation normalization |
| Population ||U||_2, ||U||_ell, |U|_(2,ell) | ||U||_(L2(Omega_ell)) or (E_ell |U|^2)^(1/2) | Source ||.||_2 alternates between ordinary vector and probability-space norms |
| Rank-one population U tensor V | (U tensor V)g=U E[Vg]; finite representative UV^T/n | Using UV^T would change every middle-layer rate |
| Matrix lengths | Ordinary finite Frobenius norm; population HS norm for trained increments only | Initial Gaussian actions are generally bounded, not HS |
| L as both depth, loss and a central positive operator | L=hidden depth; loss mathcal L; rename D Section 8's L to a defined operator symbol | Avoid a false identification of depth with a matrix |
| eta in D; eta_n in A–C; delta_n in D; Delta proof mesh | Separate mobility kappa, physical GD mesh eta_n, and auxiliary proof mesh Delta | D permits every normalized vanishing physical mesh; A has eta_n sqrt(n)->0; B/C state n^-2 |
| r=f-y vs e=y-f | Choose one residual sign and rederive displayed clock signs consistently | The residual is not part of delta^(ell) or the unit-metric kernel |
| F(z) coordinate transform | Keep as a clearly defined proof coordinate, e.g. X^(1)=F(z^(1)) | F(z)=z+z^3/3 for atan but 10(z+z^3/3) for shifted atan; raw GD is not Euler in X |

### Linear rescaling is substantive

In D/E, x is a trained endpoint vector, not the input datum; a is the other endpoint, and all coordinates of x,a,B,R initially have variance 1/n. For the common finite-network convention set

    W^(1)=sqrt(n) x,   W^(2)=B,   W^(3)=R,   W^(4)=sqrt(n) a,
    z^(1)=W^(1),   h^(ell)=z^(ell),   f=(W^(4))^T h^(3)/n.

Then stored W^(4) initially has variance **one**, unlike the three nonlinear donors, whose stored readout variance is n^-2. Equal limiting initial predictions do not equate these initializations.

The canonical endpoint mobilities are n kappa and middle mobilities kappa. Explicitly,

    dot W^(1)=2 kappa e (W^(2))^T (W^(3))^T W^(4),
    dot W^(2)=(2 kappa e/n) ((W^(3))^T W^(4)) (W^(1))^T,
    dot W^(3)=(2 kappa e/n) W^(4) (W^(2)W^(1))^T,
    dot W^(4)=2 kappa e W^(3)W^(2)W^(1).

The same-clock scalar kernel is exactly the source K after these substitutions; the common mobility kappa remains outside it, unless the shared definition deliberately includes mobility in each kernel block. State which convention is used.

To retain the simple cyclic trace proof, explicitly introduce proof embeddings x=W^(1)/sqrt(n), a=W^(4)/sqrt(n) (with unambiguous new names if necessary). Do not simply insert the canonical order-one endpoint vectors into D's cyclic matrix: that would replace f=Tr(C^4)/4 by the wrong normalized trace and spoil the dimension-independent norm bounds. The population Fock vectors represent the normalized endpoint geometry; they are Hilbert vectors, not automatically coordinate random variables on the nonlinear neuron probability spaces.

Under this rescaling, translate E's contraction encoder with explicit powers of n. Its coefficient functions are allowed to depend on n, so this conversion preserves its restriction. State the scalar negative in a correspondingly coefficient-permitting form or retain the explicitly defined normalized proof factors when invoking D's scalar theorem. E already contains the scalar ODE case at differential order zero.

## Promotion blockers and final handoff

There is no identified missing source file or undischarged nonclassical proof premise for the narrowed five-theorem core. There are four concrete rewrite requirements before calling `docs/` self-contained:

1. Embed the entire L3 proof chain and resolve every external-looking note reference to a proved internal result; do not promote the cutoff note as an unconditional theorem by itself.
2. Retain every singular-query, expected-response, mesh-uniform tail, raw-GD and clock bridge needed by the stated theorem. Sharing a common Gaussian lemma must preserve its exact regularity, coefficient and test-class hypotheses.
3. Use the Q-only linear Euler comparison explicitly; preserve the factor normalization and readout initialization. Omit the historical external-theorem audit. For the optional free-Wishart presentation, either supply its construction/identification or leave it out; the core and fitting have the internal cyclic route above.
4. Apply the canonical notation consistently with ordinary finite norms and explicit 1/n factors. Replace all study/tmp/note-path dependencies with mathematical text or internal `docs/` references. The private donor table belongs to planning/provenance, not to the established theory chapters.

No extension-qualified multi-input theorem, broader tensor-program import, global pure-atan L3 assertion, growing-depth claim, historical PASS record, or conditional arbitrary-depth linear note is needed to complete this promotion. This audit does not approve those additions. The separate every-fixed-depth linear physical-GF theorem was outside this requested global-joint L3 audit and was not added or reaudited.

The three suggested chapter groups correspond to 2864, 1727 and 1719 donor lines before deduplication and removal of historical/optional material. They are modest complete units. Main-agent inventory, snapshot, final architecture and repository edits remain outside this read-only handoff.
