# Canonical training onset for circle population closures

Date: 2026-09-21. New theory-only study: derive what the fully trained finite
population closures select at the onset of canonical gradient flow, and how
orders p=1,2,3 differ. This is a different question from freely prescribing
static populations and middle matrices. No training or numerical experiment
is authorized or run here.

The model is the bias-free two-hidden-layer tanh closure, normalized inputs
on S^1, probability-weighted unhalved squared loss, population L2 read-in/
readout metric and ordinary Frobenius middle metric. Initialization is exactly
w=G,c=0,M=D_p, with the book's source/response contractions and ridge schedule.
The target is a local physical-time expansion, uniformly over the input circle
at each fixed finite p, for any bounded-label training law. Finite empirical
data are included. No large-p, long-time, or finite-neural-width claim is made.

Scientific inputs are exclusively established docs/observable_p1.md,
docs/NOTATION.md, and the complete relevant source/response, H3 dictionary,
canonical closure, parity and tangent-kernel sections of docs/global_nonlinear.md.
No other study's scientific result is a dependency. The user's question about
an earlier hand-selected matrix is answered separately as an explanation of
that choice; it does not supply a premise of the onset analysis.

[ONSET.md](ONSET.md) derives canonical initialization, the initial kernel,
hidden/middle accelerations and the cubic feature-learning correction. It also
proves initial middle ranks 2,2,4 for p=1,2,3 and gives an explicit case where
a cubic initialized readout component is produced immediately even at p=1.
The common-ridge p=1/p=2 equivalence is distinguished from the maintained
order-dependent ridge. Higher-order superiority is not assumed.

Root owns README.md and ONSET.md. Fresh scoped agents onset_flow_derivation
(prompt-only equations) and onset_order_structure (specified established book
sections) independently derived the temporal and order-structure components.
Their final-source checks are recorded in [FLOW_CHECK.md](FLOW_CHECK.md) and
[STRUCTURE_CHECK.md](STRUCTURE_CHECK.md). Both pass their assigned scopes at
ONSET.md SHA256
`ff2e3d72e8ba601482fb6fe61f1ef6dc38d38b78e464a513b4b2534f74ee462a`.
The structural check required narrowing the H3.1 shortcut to polynomial-core
actions (including p<=3); general retained new actions require the full
finite-source rule. That correction is included and checked.

Status: derivation and internal contributor checks complete. These checks are
not independent promotion reviews, and nothing is promoted. No numerical
experiment is queued. The result is a local training-onset prediction, not
a trained endpoint or a cross-order performance guarantee.

## Continuation: explicit Gaussian peeling of the p=1 kernel

The user requests an actual reduction of the initialized population kernel,
with n tending to infinity at fixed p=1, to recursive expectations of products
of activations and their derivatives at primitive Gaussian arguments. Nested
activation integrals alone do not meet this target. Non-Gaussianity of a
derived variable is not a valid obstruction to Stein elimination.

This continues the kernel calculation in ONSET.md; its frozen results and
checks remain unchanged. Root owns PEELING.md and deterministic validation
source. Fresh scoped contributors own PEEL_DIRECT.md (specified established
sources, direct elimination attempt) and PEEL_ATOMS.md (prompt-only independent
moment reduction). Finite terminating identities and convergent infinite
reductions will be distinguished explicitly. No training is authorized here.

Deterministic verification, if needed, compares the derived moment reduction
against the original Gaussian-integral kernel, with separate quadrature and
series refinements on a fixed small circle panel. It is an algebra check,
not a learning experiment. Use float64, one process, at most two minutes per
verification execution and no more than three executions before reviewing
errors. Record source, parameters and outputs under this study's namespace.

Completed result: [PEELING.md](PEELING.md) gives an exact uniformly convergent
reduction of the p=1 initialized kernel to elementary Gaussian activation and
derivative moments. The independent derivations are
[PEEL_DIRECT.md](PEEL_DIRECT.md) and [PEEL_ATOMS.md](PEEL_ATOMS.md). Every finite
stage is an explicit Gaussian-moment expression; the full tanh kernel uses an
infinite-degree limit, with geometric analytic remainder bounds. A finite
terminating Stein-only identity remains unproved; no impossibility is claimed.
The matrix/source contractions use the established book, and the full
nonlinear resummation additionally uses the proved analytic/polynomial
expansions. Thus the result is not represented as finite Stein elimination
alone.

Fresh internal checks completed: [PEEL_REVIEW.md](PEEL_REVIEW.md) passes the
mathematical statement at the frozen source hashes; its independent input
scope and an incidental unused established-source read are disclosed.
[PEEL_CODE_REVIEW.md](PEEL_CODE_REVIEW.md) found no blocking implementation
defect and independently executed the frozen [peel_check.py](peel_check.py).
Neither check is a promotion review. The source hash of the driver is
`e696b7a5a6ae4231367ac75a0711fd0c72ad16160b928b1510d65fd07ed58584`;
PEELING.md is
`5eb8af10ae0d41f3af01de62deae06315519bf41b27142b71de9fa870ffac7d2`.

Three deterministic executions are retained at
`data/generated/closure_training_onset_20260921/peel_check_01`,
`peel_check_02`, and `peel_check_independent_03`. The last run used 192/256
Gaussian nodes and compared all 81 entries of a fixed nine-angle kernel.
At degree (64,64), the two evaluation routes differ by 5.00e-16 at 256 nodes;
the original-kernel quadrature refinement changes it by 2.78e-16. These are
floating-point diagnostics, not rigorous quadrature or roundoff certificates.
The full analytic error bound assumes exact moments and is distinct from the
measured discrepancies. Full commands, source snapshots, environments,
coefficients and output tables are retained with each execution and linked
from the reports. No training or neural-width experiment was run.

Status of the expansion route: internally checked convergent moment reduction
completed. The stronger finite-only reduction is open. No established docs/code
were changed.

## Continuation: exact calculation without activation polynomials

The user explicitly requests another constructive attempt to obtain the same
canonical p=1 initial kernel by exact Gaussian peeling, without polynomial
approximations of the activation. The target remains products of original tanh
or its derivatives at explicitly specified Gaussian arguments. A generic
Gaussian expectation containing composed nonlinearities does not fulfill that
stronger target. Exact continuum integral formulas are recorded separately from
a finite elementary-Gaussian normal form; no failure of one route is a general
impossibility claim. This is a continuation of the same kernel investigation.

Root coordinates and owns the synthesis and README. Fresh independent attempts:
`exact_peel_canonical` reads only the specified established initialization and
Gaussian-calculus sources and owns EXACT_PEEL_CANONICAL.md;
`exact_peel_analytic` receives the complete kernel definitions in its prompt,
uses no scientific retrieval, and owns EXACT_PEEL_ANALYTIC.md. Attempts freeze
before comparison. The bounded first round is these two routes plus root's
direct source audit, followed by verification of any concrete new identity.
No training is authorized or queued. Current HEAD at restart is
`ab6dd76987007b925b4d9559a936234e224ef6e9`; the shared index is untouched.

This round is complete. Both independent attempts reproduced the actual
canonical matrix peeling, including the reverse response. They did not obtain
the strict original-activation-only terminal form. Their frozen derivations are
[EXACT_PEEL_CANONICAL.md](EXACT_PEEL_CANONICAL.md) and
[EXACT_PEEL_ANALYTIC.md](EXACT_PEEL_ANALYTIC.md). They retain, respectively, an
exact Gaussian density-translation identity and explicit continuum-integral
identities; these are scoped partial results, not completion of the strict target.

Root's [EXACT_PEEL_WEIGHTED.md](EXACT_PEEL_WEIGHTED.md) gives a complete exact
Gaussian-integral formula for the coefficients and kernel with explicit
density weights, without any activation polynomial or series. Its upper
formula integrates products of tanh at Gaussian linear arguments against
known density ratios; its shorter lower formula translates a Gaussian mean
using an explicit exponential likelihood ratio. These weights preserve the
actual initialized law and cannot be silently omitted or classified as
original activation-derivative atoms. No polynomial cutoff or radius is used.

The exact weighted identities are internally checked at SHA256
`b5e328d19bf00de0f84e4fc0bc93a4406cab442c615d5eb05407f29701571ecc`.
A fresh isolated reviewer read the complete frozen candidate, canonical p=1
source and notation contract, reconstructed the normalization, and checked
all densities, Gaussian covariances, Stein steps, endpoints and integrability.
[EXACT_PEEL_WEIGHTED_REVIEW.md](EXACT_PEEL_WEIGHTED_REVIEW.md) passes only the
explicitly enlarged weighted-Gaussian claim and confirms the stricter target
is not met. Root read the full original report. No numerical/training run or
promotion was performed, and no established files or Git index were changed.

Current result: an exact series-free weighted Gaussian representation is
available; an exact finite normal form using only original tanh/derivative
products remains unresolved. No claim of impossibility is made. No further
compute or training is queued.
