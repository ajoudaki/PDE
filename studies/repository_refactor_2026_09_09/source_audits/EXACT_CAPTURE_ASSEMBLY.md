# Priority 3 — exact-capture comparison incorporation for PDE

Date: 2026-09-09. Source workspace: `/home/amir/Codes/PDE`.

Deliverables are private drafts in
`/tmp/pde-priority3-exact-capture-SGvsqOl1` (directory mode `0700`):

- `ADDITION.md`: complete proposed Sections 8–12 for the existing
  `docs/linear_dynamics.md`, with independent `EC` equation labels.
- `REPORT.md`: this source, scope, dependency, and handoff record.

The draft addition has 1,293 lines and SHA-256
`b92d47b240d848a2f91ac4d24ad195ddf86d29a2e7be81a3307f87b51a5d13dd`.

## Result and review status

All three requested GF families have proof-complete candidate additions:
the shallow characteristic population (Theorem EC8), every separately fixed
linear depth (Theorem EC10), and the two-hidden-layer spectral population
(Theorem EC11). Section 9 supplies the shared Gaussian norm and fixed-word
Wick proofs. Section 12 proves agreement on overlaps at matching scopes.

There is no open lemma being assumed for these stated GF conclusions.
This is an assembly-stage mathematical conclusion, not an independent-review
acceptance or an established-library promotion. The main task supplies the
fresh isolated review. No agent or separate reviewer was invoked here.

The source studies' review labels were not used as proof premises. Compressed
random-matrix and transfer steps have been replaced by actual contained
arguments. The shallow theorem remains visibly a nonlinear comparison at
one hidden layer; it is not folded into a deep nonlinear theorem.

No repository file was edited. The only authored files are the two deliverables,
created and revised with `apply_patch` inside the new private temporary
directory. No experiments, code generators, builds, installs, Git operations,
subagents, network retrieval, or external messages were used. Read-only
operations were file discovery, complete or explicitly ranged reading,
search, line counts, hashes, and the directory permission check.

## Captured theorem scopes

| Family | Initialization and data | Physical GF and state | Captured readouts |
|---|---|---|---|
| Shallow characteristic | `L=1`, one scalar datum `m=d=1`, `x=1`, arbitrary fixed real label; independent `N(0,1)` first weights and stored readout; `C^2` activation, bounded first and second derivatives, linear growth | Full MSE; common multiplier `kappa>=0`; endpoint mobilities `n kappa`; two marked fields on the fixed two-Gaussian probability space plus residual | Uniform compact-time prediction, kernel, residual, loss, and separate endpoint energies; convergence in probability, also almost sure under the nested iid coupling |
| Two-hidden-layer spectral | `L=2`, identity activation; one fixed input in a fixed dimension with `x^T x/d=1`; projected first weights and stored readout order one, hidden stored matrix variance `1/n`; independent Gaussian initialization | Full MSE; `kappa>0`; mobilities `n kappa,kappa,n kappa`; one fixed finite spectral measure, one complex field/velocity pair and residual | Uniform compact-time prediction, kernel, residual, loss, norm `q`, and all three block energies; probability mode; global initialized population and limiting fitting |
| Every fixed linear depth | Each separately fixed integer `L>=1`, identity activation; `m=d=1,x=1`, fixed real label; independent order-one Gaussian endpoints and hidden entries `N(0,1/n)` | Full MSE; `kappa>0`; endpoint mobilities `n kappa`, hidden mobilities `kappa`; typed real word-space sources, endpoints, current trace-class increments and residual | Uniform compact-time prediction, kernel, residual, loss, block energies, fixed current rooted-program scalar readouts, finite Gram geometry and finite-rank norms, increment trace norms/fixed singular values, uniformly tight nuclear tails |

All residuals in the insertion are `r=f-y`. The studies' `e=y_star-f` is
translated as `e=-r`, and their continuous mobility multiplier `eta` becomes
`kappa`. The spectral study's `r=||x||^2` is renamed `q`; it is never confused
with the residual. Finite endpoints are explicitly divided by `sqrt(n)` when
ordinary Euclidean norms are used. Hilbert auxiliary aliases are typed and
related to the layer-indexed population weights.

No theorem silently imports `E phi(G)^2=1` from the fixed-program calculus.
The shallow class has no such normalization. All three families use stored
readout variance one, which differs from the library's nonlinear
small-readout convention.

The spectral source has total mass two, not one. Its two diagonal channels
each have mass one, and the negative atom is exactly mass `3/4` at `-1/2`.
The three initial kernels are checked as `2` for shallow identity, `3` for
the spectral case, and `L+1` for fixed linear depth.

The spectral source study's displayed width-limit theorem names prediction
and loss. Its exact reduction also gives kernel and block-energy formulas.
The insertion proves their uniform convergence explicitly in
(EC11.30)–(EC11.32); it does not infer it from convergence of prediction
or from convergence of time derivatives. Likewise, increment trace norms
and fixed singular values in EC10 are proved through finite-rank Picard
approximants, not inferred from weak rooted pairings alone.

## Source hashes and exact read coverage

Paths below are relative to `/home/amir/Codes/PDE`. Hashes are SHA-256 over
the entire file bytes, including for the selectively read calculus chapter.
The same eleven repository hashes were obtained after source reading and
again during the final draft audit; none differed between those checks.

| ID | Source | Read coverage |
|---|---|---|
| N | `docs/NOTATION.md` | FULL, lines 1–98 |
| LD | `docs/linear_dynamics.md` | FULL, lines 1–1166; read in nontruncated chunks |
| GC | `docs/gaussian_calculus.md` | Lines 1–480 and 1739–1812; Sections 1–4 read fully, including the complete gradient and Gaussian moment proofs; Section 5.1 and 5.2 read fully for statement/scaling separation, first part of 5.3 read; Section 6 read fully |
| SH | `studies/rcgc_shallow/GENERIC_L1_THEOREM.md` | FULL, lines 1–266 |
| SP | `studies/mfp_identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md` | FULL, lines 1–570; reread as 1–389 and 390–570 after the first combined output was truncated |
| FD | `studies/rcgc_linear_depth/LINEAR_FIXED_DEPTH_THEOREM.md` | FULL, lines 1–470 |
| CT | `studies/rcgc_program_history/RESEARCH_CONTRACT.md` | FULL, lines 1–172 |
| CS | `studies/rcgc_program_history/CALCULUS_SPECIFICATION.md` | FULL, lines 1–362 |
| AU | `studies/rcgc_program_history/audits/LINEAR_PHYSICAL_FINAL_AUDIT_03.md` | FULL, lines 1–47; provenance only, not a proof premise |
| FR | `studies/rcgc_linear_depth/README.md` | FULL, lines 1–21; source routing and scope |
| SR | `studies/rcgc_shallow/README.md` | FULL, lines 1–15; source routing and scope |

The remainder of GC, lines 481–1738, was not read as proof text. A heading
search also saw its section labels. None of its adaptive-conditioning,
strict-rank, finite-moment-tower, or fixed-program convergence theorems is a
dependency of this insertion. Its relevant exact finite Gaussian moment
proof in Section 4 was read fully and its needed identity is rederived in
EC9. No unread transitive proof is being imported.

The historical FD link `../audits/LINEAR_PHYSICAL_FINAL_AUDIT_03.md` was
resolved to AU in the reorganized `rcgc_program_history/audits` directory.
Likewise its parent model contract is CT and its named compilation rules
are specified in CS. These exact files were found by repository path search;
no broad research campaign or unrelated nonlinear gate was followed.

```text
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b  docs/linear_dynamics.md
cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
b098feb5c96d8217293f4a0421be8901b1d0f49f968906d80c6e427058fbefe2  studies/rcgc_shallow/GENERIC_L1_THEOREM.md
0a18f1badd4a9412886f08118e0d0ea8a6cfac06fda118edba848e2ca15c1430  studies/mfp_identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md
a4be9b8f5193685533a622af2aca4d7eca135712b0b858db684f40a89e89c9b1  studies/rcgc_linear_depth/LINEAR_FIXED_DEPTH_THEOREM.md
ecee4e7c21ac9d132400ac3d3cdc9e14de36f4850ddb62486681652f03c5d3d3  studies/rcgc_program_history/RESEARCH_CONTRACT.md
6a1489764720e53c7b756c52a2224be6d971c68d2d92836299c5357145034240  studies/rcgc_program_history/CALCULUS_SPECIFICATION.md
726512a8b94e21608dca3b00a60b31aa450632c9f718eafcddb028925cb069db  studies/rcgc_program_history/audits/LINEAR_PHYSICAL_FINAL_AUDIT_03.md
1b3e3e4efaafca8d807e5b6e752539336a947a0811a2f4ca24a486dfa6ae0df2  studies/rcgc_linear_depth/README.md
5e45bc316ea801be85a04b4934b52e692d1df19fa026c160cc62ac94a72bff27  studies/rcgc_shallow/README.md
```

Procedural instruction source: `/etc/codex/skills/solve-math-rigorously/SKILL.md`,
read FULL, lines 1–115, SHA-256
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
Its use emphasized explicit hypotheses, complete transitions, and a manual
proof audit. It supplied no mathematical theorem premise and required no
permission pause. No `AGENTS.md` was found at the workspace or its checked
ancestors; no repository-local instruction file was edited.

## Dependency map and checked matches

| Addition | Existing mathematical input and match | Contained completion |
|---|---|---|
| EC8 exact finite equations | SH Sections 1–2; CT Section 1; GC Section 3's constant-metric chain rule; one sample and two normalized endpoint metrics | Direct finite equations in stored coordinates, residual sign translation, characteristic construction, global two-sided characteristic envelope |
| EC8 physical existence and width law | SH Sections 2–4, same activation bounds and independent Gaussian marks | Scalar residual clock bound; cubic derivative envelope for kernel; fourth-moment summable empirical bound and finite nets; true random initial residual; physical-clock comparison |
| EC9 Gaussian norm event | LD Lemma 2, especially its sphere-net proof (2.11); same square real Gaussian entries of variance `1/n` | Repeated in full, with Gaussian tail and packing count; constant 12 suffices; finite union over any fixed number of labels |
| EC9 fixed-word law | LD Lemma 2's trace/Gram proof; GC Section 4 finite Wick identity; real independent matrices and independent normalized Gaussian endpoints | Full tree/free-index count, noncrossing/opposite-transpose characterization, two-trace variance, actual-adjoint Fock realization and conditional root quadratic-form variances |
| EC10 equations and energy | FD Sections 2 and 4, CT metric, LD Section 3's local trace-space method; all fixed-depth block velocities are rank one | Separate endpoint normalization, exact raw kernel, product Lipschitz estimates, trace-norm path lengths, Banach continuation and restart |
| EC10 width transfer and tails | FD Section 5; LD Section 4's cutoff/Picard/finite-Gram mechanism | Cutoff on the actual endpoint/trace/residual state ball; global bounded Lipschitz field; finite-word coefficient induction, singular Gram continuity, factorial Picard remainder, scalar comparison, Lipschitz Riemann trace tails |
| EC11 finite spectral reduction | SP Section 3; same projected normalized datum and raw-to-stored matrix change | Direct physical-time invariants, two-channel functional calculus, exact kernel and random initial residual; no division by residual |
| EC11 source measure | SP Section 4 specifies the target; EC9 supplies the proved probability inputs | Alternating-word Catalan count, density moments by integration, Bernstein approximation, elementary resolvent evaluation, explicit rank-one inverse, direct verification of atom and continuous density, transform-to-moment identification, second-channel and cross-channel concentration |
| EC11 global physical system | SP Sections 1, 5 and 6 specify the desired system/conclusions | Direct physical invariant `F=y+r`, bootstrap `q>=1`, norm bound `q<=1+kappa y^2 t`, bounded velocity field on each horizon, global continuation and limiting loss decay |
| EC11 compact-time width limit | SP Sections 3–5 finite oscillator architecture, plus contained source proof | Common spectral interval from the coarse norm bound; finite nets for mode-product tests; stopped same-domain integral comparison and Grönwall; separate block readouts |
| EC12 overlap identification | Matching finite equations of EC8/EC10/EC11 and LD's already proved `L=3` limit | Direct shallow linear characteristic calculation; uniqueness of deterministic limits in probability for common finite observables |

The logical order is acyclic:

```text
N + SH + exact finite differentiation -> EC8
LD Lemma 2 method + GC finite Wick identity -> contained EC9
EC9 + contained rank-one energy/cutoff/Picard proof -> EC10
EC9 -> EC11.2 source measure
EC11.1 exact finite identities + EC11.3 direct physical existence
        + EC11.2 source measure -> EC11.4 uniform width identification
EC10 energy at the exactly matching L=2 normalization -> finite existence only
EC8 + EC10 + EC11 + matching LD L=3 observables -> EC12
```

The extension from two matrix labels in LD to `L-1` labels is not an invocation
of the original two-label lemma outside its scope: EC9 repeats its complete
counting and norm proof for any separately fixed number of labels. The
all-depth proof uses per-block rank-one bounds; it does not apply LD's special
rank-four cyclic estimate at other depths. No sharp Bai–Yin edge theorem,
asymptotic-freeness theorem, Marchenko–Pastur theorem, or external spectral
inversion theorem is being cited in place of a proof.

## Repairs, non-promoted claims, and remaining boundaries

The source manuscripts have several steps requiring completion for a
self-contained library addition. These are closed in the candidate text:

1. FD Lemma 3.1 compresses its Wick count and cites Bai–Yin for the source
   edge. EC9 gives the entire count and an elementary norm bound. It does
   not retain the unnecessary auxiliary assertion `max ||G||<=3` or the
   sharp edge limit.
2. SP Section 4 cites Marchenko–Pastur and the extreme-eigenvalue theorem,
   then invokes inversion for the perturbed measure. EC11.2 derives the
   moments and density and verifies the full perturbed measure directly.
   The negative atom is included; there is no unidentified singular part.
3. The fixed-depth varying-space transfer needs uniformly controlled
   approximations, not merely finite-word membership. EC10 supplies the
   cutoff, coefficient continuity including singular Grams, and explicit
   uniform Picard errors before taking width to infinity.
4. Physical continuation of the spectral system must not presume global
   feature time. EC11.3 gives a direct physical proof, for both signs of
   the label and for zero label. The bound `K>=3/2` also yields the stated
   sufficient exponential fitting bound.
5. Nuclear tails require equicontinuity of the rank-one integrand.
   EC10 derives it from the state/vector-field bounds and supplies the
   rank and trace-error estimate explicitly.

No unclosed requested family is being deferred. The following are outside
the inserted conclusions, not assumed lemmas or hidden extensions:

- Arbitrary datasets or Gram matrices, multiple samples, a non-normalized
  input in the spectral projection, non-Gaussian initialization, small
  readout, or unequal block mobility multipliers.
- Raw GD, including attaching LD's existing `L=3` GD bridge to the shallow,
  spectral, or all-depth statements. Picard iteration and Riemann sums in
  the proof are auxiliary approximations, not optimizer statements.
- Growing depth, growing physical horizons, interchange of width and
  long-time limits, or a general fixed-depth fitting theorem.
- Global unit feature time for linear depth at least two; the historical
  blow-up statement is not reproduced or used.
- The spectral study's feature-domain bijection, its exact asymptotic
  logarithmic fitting rate, Stieltjes/Taylor claims, or reconstruction of
  every rooted operator signature from the spectral fields.
- An unrestricted scalar/PDE nonclosure theorem, a new nonlinear deep
  result, or reopening the unresolved global nonlinear program in CS.

For the main task's fresh review, the concrete proof leaves are EC8.9–EC8.14
(characteristic empirical and clock bounds), EC9.5–EC9.8 (norm/Wick/root
law), EC10.11–EC10.15 (cutoff, varying spaces and tails), and EC11.15–EC11.32
(source identification, physical continuation, and uniform mode comparison).
All source fingerprints and read boundaries needed to reproduce that review
are recorded above. Incorporation itself remains for the main task after
its review; no existing chapter text or library status was changed here.
