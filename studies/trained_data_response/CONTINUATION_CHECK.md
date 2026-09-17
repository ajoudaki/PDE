# Continuation reconstruction of the primary response candidate

Checker: `/root` in task `01a090bb-ded9-7f73-b893-0fce3cf9e257`,
2026-09-11. This is an author-side check with project context, not a fresh
isolated scientific review. It does not satisfy either promotion review slot.

## Checked claim and present finding

The four component sources frozen in R1 give a complete candidate for the
requested primary milestone: the actual finite right data derivative has a
deterministic whole-circle limit on each fixed physical interval; its forcing
is a bounded linear map of finite signed measures in total variation into the
reference clock/HS/readout space; and its homogeneous population propagator
is uniformly bounded for all starting and ending times. The resulting forced
norm bound is linear in the physical horizon and in total variation mass.

No substantive mathematical gap was found in this reconstruction. This
finding supersedes this task's startup diagnosis of a missing source file:
the original task was still working and subsequently supplied that file.
Independent isolated reviews of the frozen packet are being coordinated by
the original task. Acceptance and promotion remain distinct from this check.

## Finite source reconstruction

The delicate finite estimate uses an actual auxiliary GF with initialized
column i zeroed, while every learned parameter remains trainable. It is
independent of the removed Gaussian column conditional on the remaining
arrays. Its good event contains the full-network good event and is measurable
without the removed column; conditioning on the full-network event would
instead be invalid. The proof uses the correct event.

The forward contribution of the removed column on a bounded hidden feature
has RMS at most its Euclidean column norm divided by sqrt(n). Its reverse
contribution to a cavity backward field is supported on the single coordinate
i, with RMS equal to the absolute Gaussian probe divided by sqrt(n).
Comparing complete clocks, learned matrix increments and readout consequently
gives an O(n^(-1/2)) difference multiplied by the supremum of that probe and
a deterministic compact-time constant. The learned matrix difference is
measured in Frobenius norm; no small operator norm of the removed initialized
column is asserted. Residual differences are included in this comparison.

The cavity backward fields are uniformly Lipschitz in time and input in RMS.
Conditional on the cavity, the probe therefore has a Gaussian canonical
metric controlled by the ordinary two-dimensional time/input parameter
metric. The contained dyadic-grid calculation bounds all fixed moments of
its supremum independently of n. Combining this with the preceding comparison
gives actual finite query moments. This is an independent probabilistic
estimate, not an inference from population second-moment convergence.

The exact identity

\[
 \partial_X\cosh^2 J(X,g)=2\tanh J(X,g),\qquad
 \cosh^2 J(X,g)\le\cosh^2g+2|X|
\]

then converts query moments to inverse-gate-weighted moments. Clock growth
is bounded coordinatewise by the integrated active query. Gaussian root
moments and Holder control all products needed for the source and the input
modulus. No independence between the trained query and its root is used.

For all-time population forcing, the same cavity argument is applied to a
separate finite feature equation on the fixed interval [0,10]. Zero readout
is used only for that auxiliary equation. Fixed-program identification and
the transformed same-array comparison transfer bounded tests to the canonical
feature flow. Monotone convergence supplies moments over a countable dense
parameter set; L2 continuity supplies the bound for each remaining fixed
input/time equivalence class. Fubini justifies integration against each fixed
deterministic law. The actual finite physical reference retains its Gaussian
readout everywhere in the derivative theorem.

## Derivative and propagation reconstruction

At fixed n, bounded input/label support permits differentiation of the exactly
integrated loss on every compact parameter set. Energy prevents finite-time
escape. Subtraction of the finite ODEs, the mean-value identity and an integral
inequality give the right parameter derivative along the probability segment.
The initial derivative is zero because all initial arrays are shared.

Transforming first coordinates before deriving its linear equation cancels
the own-gate derivative exactly at the two active axis inputs. The new-input
term keeps the inverse own gate. The equation retains the full row, both
orientations of the initialized middle action, its varied action and adjoint,
and the readout variation. Its bounded generator does not require an ambient
Frechet derivative of an L2-valued nonlinear field.

The capture proof fixes source clipping, data quadrature and a time mesh
before taking width to infinity. Every tangent mesh instruction has at most
linear growth after the inactive readout clip, and middle updates expand into
finite ranks. Multiplier consistency uses truncation of the tested tangent
fields. Compactness of the converging population tangent paths supplies
uniform L2 tails for these test fields as the mesh is refined. The proof
takes the finite-program width limit at each fixed mesh, then removes the
mesh; it never invokes a fixed-program theorem on a growing actual transcript.
The weighted-source bounds remove clipping and quadrature. The first-row
and passive-query moment bounds give the whole-circle modulus independently
of the pointwise derivative-convergence argument.

The propagator reconstruction is detailed in PROPAGATOR_CHECK.md. Its key
identity is E=S*D with D=R*R injective, where R converts clock variations to
raw variations. It gives ker(ES)=ker S=ker E*, even for a singular endpoint
training Gram. Hence the endpoint finite-rank semigroup is uniformly bounded
with a constant depending on the pseudoinverse of the fixed two-by-two Gram.
The reference's exponentially small residual, exponential raw endpoint
approach, and the fixed endpoint active-query L4 bound make the difference
between the actual generator and this endpoint generator integrable in
operator norm. Variation of constants yields the uniform all-time bound.

Constants depend on the fixed reference and its endpoint conditioning, with
additional label dependence through Y; compact-time finite comparisons also
depend on T. They do not depend on support size, atom weights or input Gram
invertibility of the perturbing law. Probability convergence remains for
each fixed law. Neither an all-time finite-width result nor a nonlinear
finite-contamination theorem follows from these assertions.

## Inputs, execution and limitations

Complete author sources read: THEOREM.md (245 lines), PROPAGATOR.md (540),
FINITE_CAPTURE.md (626), WEIGHTED_SOURCE.md (894), check_identities.py (197).
Complete scientific source spans read: global_nonlinear.md A.1–A.4 and B.1
(1840–2453), all C.4 (3836–6892); special_data_limits.md III.F.1–III.F.11
(3785–4326); finite_dynamics.md §§1–4 (1–227). Also read the full shared
notation, reading guide, root AGENTS, workflow Parts 1–2 and required math
skills/references. Truncated source reads were repaired in smaller spans.
The unrelated complements of the maintained scientific chapters were not
audited. This is not a whole-book audit or formal verification.

Author hashes agree with R1_MANIFEST.json:

| Source | SHA-256 |
|---|---|
| THEOREM.md | 123e5ee20adad45b5ee7262c7fc66b3d22ccf0dddc0cbf2ea93df333750c7191 |
| PROPAGATOR.md | 0f803ef07553d6ad3c618b5d83c06af4de74393c939493f5e003509330da363c |
| FINITE_CAPTURE.md | d8fe981bf38cf3e1610b2d025174d64c78a3330a25d681c92a6d7597d3e4a4b8 |
| WEIGHTED_SOURCE.md | 580c7556976c52727733263b2cfc199c16ff699d8ea64130111b7bba8fe45831 |

The R1 manifest SHA-256 at verification was
`17cfcd0231bd39079f8f5d4b33e1911201ed3c20d62cce8fe8b5a281cd3cd362`.
Every listed frozen input and author source matched its manifest digest.

Executed `python studies/trained_data_response/check_identities.py --output
data/generated/trained_data_response/algebra_recovery_20260911`: exit zero,
PASS; final finite tangent central-difference error 1.61e-8, raw loss/metric
error 7.90e-12, maximum singular-semigroup identity error 1.53e-14.
Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0.

Executed the complete exact-rational scalar check embedded in
WEIGHTED_SOURCE.md: exit zero, PASS for the primitive, clock-envelope
derivative, interpolation exponents and loss weights. Its log and verified
hashes are retained in
`data/generated/trained_data_response/continuation_source_check_20260911/`.
These calculations are algebra checks, with no optimizer trajectory or
parameter sweep. The separate rational reference certificate was read in
full; this coordinator did not claim a new execution of that certificate.

Optional presentation corrections are those in PROPAGATOR_CHECK.md:
disambiguate K and clarify which of the two complementary projections is
being described after equation (31). Frozen inputs were left unchanged.
