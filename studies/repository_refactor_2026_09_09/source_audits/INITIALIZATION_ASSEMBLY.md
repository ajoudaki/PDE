# Initialization geometry incorporation report

Prepared 2026-09-09 against sources in /home/amir/Codes/PDE.

Canonical proof artifact:
[ADDITION.md](/tmp/pde-initialization-part-v-20260909.fvUagY/ADDITION.md).

Its SHA-256 is
f5cceadea1341e9f7adc1ba148112932a9360935568b58c638171a10120e5505.

The addition is one contained Part V, headed “Initialization geometry:
fixed mixtures and calibrated depth limits,” with section/equation prefixes
V.M, V.F, V.O, V.C, V.D, and V.S. The requested initialization proof
scope is complete in this draft. No unresolved initialization proof
dependency was found in the arguments incorporated. The main task's
integration review and fresh isolated adversarial proof review remain
pending; no independent approval is represented as completed.

## Output placement and exact correction record

The draft was initially created at
/home/amir/Codes/PDE/private/tmp/initialization_geometry_part_v_20260909/ADDITION.md.
The user clarified that the write scope was a genuine private directory
under /tmp, not a repository-local directory. A directory was then
created using mktemp:
/tmp/pde-initialization-part-v-20260909.fvUagY.
Its observed permissions were drwx------, owned by amir.

The existing ADDITION.md was moved with apply_patch to that directory.
The SHA-256 immediately before and after the move was identical to
the artifact hash above: the complete proof content was preserved
byte for byte. The now-empty authored repository directory
/home/amir/Codes/PDE/private/tmp/initialization_geometry_part_v_20260909
was removed with rmdir. No parent or unrelated directory was removed.
There was no REPORT.md at the original location; this report was
created directly in the genuine /tmp directory with apply_patch.

No current documentation, study source, dataset, seal, or Git state
was edited. No experiments, executable mathematical checks, installs,
Git commands, subagents, external searches, or external writes were
used. Apart from the explicitly requested mktemp creation and removal
of the exact empty authored directory, shell operations were read-only
discovery, searches, file reads, counts, metadata inspection, and the
requested SHA-256 source reads. All authored file content and the
move were handled with apply_patch.

## Exact source identity and read scope

The five source hashes below were obtained after the source reads and
checked again after drafting. Both observations agreed. They identify
the exact versions used; hashing a complete file does not imply that
the complete file was read as mathematical text.

| Source relative to /home/amir/Codes/PDE | Lines | SHA-256 |
|---|---:|---|
| docs/NOTATION.md | 98 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/special_data_limits.md | 6398 | e491ea163cf325ced50a3f1d19ab79cf9f84df85977ad644b68f4c96775e36ea |
| studies/odd_mixture_general_depth/REPORT.md | 643 | cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037 |
| studies/convex_offset_all_depths/REPORT.md | 291 | a6dae64cd54b9ab34520d2b493b78cefbbd4c868b5c222552e169982aff9f668 |
| studies/calibrated_near_identity_reviews/manuscript.md | 171 | f55df0156da98d67a655b27280a005d148df0bb206b783a454dfed379bc99211 |

docs/NOTATION.md was read fully, lines 1–98. All three named donor
documents were read fully: odd-mixture lines 1–643, convex-offset
lines 1–291, and calibrated manuscript lines 1–171. An initially
truncated aggregate output was followed by bounded reads covering
the complete odd-mixture report. Its conditional Part II was read
to determine scope, not incorporated as a theorem or premise.

For docs/special_data_limits.md, the complete heading hierarchy
was inspected, together with searches for scope, initialization,
correlations, and part structure. The exact union of contiguous
text ranges read was:

- 1–128: chapter introduction, family table, conventions, storage,
  kernel/loss normalization, clocks, and the stated generic
  finite-program scope.
- 3500–3777: Part III introduction and all of III.M, including
  the literal large-gain activation, model, theorem statement,
  observables, and fixed-depth quantifiers.
- 4577–4679: III.G introduction and all of III.G.1, including the
  three-input geometric proof, Gaussian constant/linear projection
  proof, variance bounds, and summable gain-normalized Gram estimate.
- 6013–6095: III.A introduction and all of III.A.1, including the
  attained affine-regression formula, two stability estimates,
  and exact absorption of the affine activation term.
- 6230–6398: all of III.A.3–III.A.5 and the chapter's final scope,
  including the compact-support obstruction, Gaussian regression
  positivity and continuity, tail-limit example, infinite-dimensional
  open class, and qualifications on uniformity.

No full read or audit of Parts I–III's trained finite-program,
response, cap-removal, or algorithm-limit machinery is claimed.
III.A.2 was not needed or read in full, and none of its gain-selection
arithmetic is a premise of the addition. At the hashed chapter
snapshot the body ended with Parts I–III and its scope statement;
Part IV was not yet present. Part IV correlated-data compactness
remains assigned to the main task. The addition does not depend
on any prospective Part IV assertion or numbering.

The instruction file
/etc/codex/skills/solve-math-rigorously/SKILL.md
was also read fully and used for proof organization and checks.
It is not a mathematical source or dependency of the addition.
No applicable AGENTS.md was found in the workspace ancestor paths
or the originally proposed output path checked during this task.

## Dependency closure and proof provenance

ADDITION.md has no mathematical citation to a study, temporary
artifact, review certificate, or external theorem. References to
Part III identify its stated activation and normalization; they
do not import a trained theorem. Every specialized initialization
step used in the addition is proved inside V.F–V.D. Elementary
integration, finite-dimensional spectral decomposition, orthogonal
projection, compactness, Chebyshev, Cauchy–Schwarz, Jensen,
dominated/monotone convergence, and Gaussian integration by parts
are applied to the specified concrete objects.

| Addition | Provenance | Included dependency handling |
|---|---|---|
| V.M and V.F.1 | Shared notation; chapter conventions (C.1)–(C.3); odd report's exact-model section and initialization lemma; convex §§1,3; calibrated §1 | Canonical first weights and explicit equivalent storage, unchanged small readout, unit raw metric, conditional Gaussian-row law, finite fourth-moment averaging, singular-covariance continuity, complete Gaussian matrix net bound, all kernel blocks and their initialized limits. Positive-square-root continuity is expanded by a finite-dimensional subsequence proof. |
| V.F.2 | Odd Part I §2 | Hermite generating functions, orthogonality, completeness via Gaussian convolution and Fourier uniqueness, endpoint covariance formula, integration-by-parts coefficient identities, and endpoint derivative sums. The needed uniqueness proof is included. |
| V.F.3 | Odd Part I §4, equation (10); calibrated §3, equation (7) | Complete three-vector tensor separation proof and positive semidefiniteness of every entrywise power, with singular input Grams allowed. |
| V.O.1–V.O.3 | Odd Part I §§1–5, equations (1)–(20), including theorem (A) and normalized order (B) | Entire variance/weight/injection/curvature chain and strict planar matching example. Absolute constants are retained; normalized comparison constants are made explicit from the same proof. |
| V.O.4 | Odd Part I §§6–7, equations (21)–(22), and the cubic estimate in §4 | Fixed-mixture variance and regression equivalents, antipodal necessity, and affine equilateral representational obstruction. Additional uniform two-sided scalar nonaffinity bounds follow directly from the proved cubic coefficient and projection estimate. No stationary trained-trajectory claim is used. |
| V.C contraction | Convex report §§1–3, equations (3)–(10) | Variance interval, strict contraction constant, and explicit arctangent example. The donor's complete density-differentiation proof was read; the addition instead proves the same contraction through its contained Hermite identity (V.F.11), including negative and singular correlations. |
| V.C scalar conclusions | Elementary consequence of that variance interval and the contained regression identity; analogous Gaussian regression foundations fully read in chapter III.A.1 and III.A.4 | A new explicit compact-interval proof gives fixed-shape depth-uniform absolute and relative scalar nonaffinity despite normalized sample collapse. No trained nonaffinity result is used. |
| V.D.1 | Calibrated manuscript §§1–3, equations (1)–(9) | Exact shape, cancellation, sine kernel, positive odd coefficients, fixed unit variance, and tensor-based uniform finite-depth Gram floor, all with contained derivations. |
| V.D.2 | Calibrated §4, equations (10)–(12) | Expanded Picard construction and interval invariance, explicit discrete error recursion, uniform interpolated population correlation limit with an O_tau(1/L) error, matrix and sequential raw-kernel limits, and the equilateral witness. |
| V.D.3 | Calibrated §5, equations (13)–(14) | Near-identity bounds, local scalar variance attraction, and scalar gate moments with their restrictions. The exact absolute/relative scalar gap tau/(L+tau) is an additional direct consequence of the proved orthogonality. |
| V.S | All three donor scope statements; chapter introduction, III.M, III.G.1, III.A, and final scope | Unified distinction between conditioning and nonaffinity, fixed-depth validity and uniform constants, and sequential initialization limits and training. The gain-based relative-nonaffinity upper bound is separately proved by elementary projection. |

No additional donor file is required for this dependency closure.
The earlier odd-mixture studies and the donors' review directories
are not premises. The complete named reports contain the required
initialization proofs, and the addition contains them or the
explicit elementary replacements identified above. The full
adaptive Gaussian-program theorem in the current chapter is
unnecessary for these forward-only initialization laws; the
fresh-matrix proof is supplied instead.

## Conclusions and qualifications for integration

For the odd mixture, (V.O.3) gives

\[
 \frac{e^{-80/3}}{73728}
 \frac{\delta^2\theta^2L}{(1+\theta L)^2}
 \le\Lambda_L^{\rm abs}\le
 11520e^{128/3}\frac{\delta^2\theta^2L}{(1+\theta L)^2},
\]
\[
 \frac{e^{-80/3}}{9216}
 \frac{\delta^2\theta^2L}{1+\theta L}
 \le\Lambda_L^{\rm norm}\le
 2880e^{128/3}\frac{\delta^2\theta^2L}{1+\theta L}.
\]

Their joint range is \(d\ge2\), \(L\ge1\), \(0<\theta\le1\),
\(0<\delta\le1/4\), and strict absolute-correlation separation.
The planar example with \(c=1-2\delta\) matches all parameters
and remains strictly admissible at \(\delta=1/4\). The lower
cubic-lifting argument also works throughout the wider realizable
range \(0<\delta\le1\) with closed absolute separation.
“Sharp” refers to joint orders, not numerical constants.

For convex offsets, the contraction constant depends on fixed
\(\varepsilon,\psi\), independently of depth and input Gram.
Both normalized conditioning measures collapse, the diagonal
stays between positive finite constants, and
\(C_L\to\mathbf1\mathbf1^T\). Positive scalar nonaffinity floors
also depend on the fixed shape and mixture, and are not claimed
uniform over the entire shape class. “Convex” here means the
literal convex mixture; it does not assert a nonnegative second
derivative of the activation.

The calibrated correlation limit is fully included. It uses
the specified depth-dependent activation, exact unit Gaussian
variance at population initialization, and width first/depth
second. It is not a theorem for a fixed activation as depth
changes, a simultaneous width/depth limit, or a normalization
layer. No all-depth monotonicity of the activation is needed
or asserted. Its depth-discretization error bound controls the
deterministic recursion, not the finite-width error.

Relative scalar nonaffinity is explicitly defined as the
affine regression error divided by full feature second moment.
For offsets, the addition distinguishes that quantity and
the uncentered unit-diagonal feature Gram from centered
covariance/Pearson correlation. No centered-conditioning
claim is substituted for the raw-kernel statement.

## Unavailable scope and omitted material

No unresolved gap was found in the initialization proof chains
incorporated here. This is the author's contained proof check,
not the fresh isolated adversarial review assigned to the next
stage. The following stronger conclusions remain unavailable:

- **Literal odd mixture:** no sufficient positive trained-limit
  threshold \(\theta_*(\delta,L)\), and no existence or impossibility
  result for one sufficient \(\theta_*(\delta)>0\) across all
  separately fixed depths. The donor's conditional Part II
  assumes reference existence, cap-independent primal bounds
  (II.3), and the weighted incoming-field exponential bound
  (II.4). Those bounds along canonical trained references are
  unproved there. The whole continuation implication, including
  its tail premise, is omitted from the addition.
- **Literal convex offset:** failure of a depth-uniform
  initialized kernel floor does not rule out a qualitative
  trained theorem with depth-dependent constants. The donor
  gives no admissible trained mixing threshold, all-time
  separation, or trained incoming-tail bound.
- **Calibrated family:** no trained population/GF/raw-GD limit,
  trained nonaffinity or motion, preservation of Gaussian
  cancellations during training, joint width/depth limit,
  or eventual fitting. Local scalar variance attraction and
  scalar gate moments do not settle these questions.
- **All three:** initialization covariance recursion does not
  construct reused trained forward/adjoint actions, response
  histories, cap removal, unique trained continuation,
  trained kernel/path/velocity convergence, or long-time
  optimizer endpoints.

The odd donor's finite-width GF global-existence discussion,
raw-GD step specification, conditional continuation proof,
and state-space tail examples were read but are outside this
initialization-only incorporation. No gain-adjusted or calibrated
surrogate is presented as an answer to a literal activation
question. Current Part III's trained theorem is not extended.

## Review handoff

The most useful independent checks are the strict planar example
and composed-curvature constant chain in V.O.3; the endpoint and
negative-correlation justification in V.F.2/V.C; and the distinction
between finite-depth concentration and the deterministic depth
limit in V.D.2. All mathematical dependencies for these checks
are contained in ADDITION.md.

The main task can incorporate Part V and update the chapter's
introduction and scope around its separately prepared Part IV.
This task has not edited that introduction, inserted a Part IV
placeholder, or represented any current global-limit theorem
as proved for these initialization families.
