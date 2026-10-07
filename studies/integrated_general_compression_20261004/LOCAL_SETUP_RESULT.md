# Near-quadratic local-continuation setup for Harmonic compression

The later [implicit-reference execution](IMPLICIT_SETUP_RESULT.md) preserves
this initializer's joint dense/Harmonic law and improves its sufficient work
to \(O(n\log(en)^{9d/2+3})\) at separately fixed admissible parameters.
It uses the user-authorized fresh implicit Gaussian reference, not a supplied
entrywise realization. This note remains the checked explicit-matrix execution;
its proofs and qualifications are unchanged.

2026-10-06. Completed and internally checked end-to-end construction, continuing
the same integrated study's setup question. Both the component audits and
the final combined-interface audit below are complete. The integrated
accuracy theorem in RESULT.md is unchanged. This note concerns a less costly
initializer for that same final Harmonic model, not a new prediction theorem.

## Clarified target

The user permits a disposable dense reference calculation during setup,
including coverage of the required physical horizon, if its **total** work
is close to quadratic in width and far smaller than ordinary dense Euler
training at the needed step size. The benchmark is therefore

\[
\text{dense Euler work}=O\!\left(m[(L-1)n^2+n(d+1)]T/h\right),
\]

where \(T\) is physical time and \(h\) is a numerical Euler step.
For example \(h=n^{-1/2}\) gives an additional \(n^{1/2}\) factor.
The user supplied that scaling as an illustration; no necessity or accuracy
theorem for that choice of Euler step is assumed. A setup theorem must state
the step-size regime in which its comparison is favorable.

All existing scientific qualifications remain: arbitrary fixed depth, the
same strip-analytic activations including unbounded values, general sphere
inputs, positive feature-Gram gap, the full existing small-label allowance,
and the same eventual-width/confidence event. The final model remains the
autonomous corrected-readout Harmonic model, with the same retained order,
whole-sphere/all-time prediction norm and fitted-limit comparison. No dense
arrays, trajectory samples or jets may be hidden in its retained state.

The original source tolerance \(1/n\) and horizon
\(T=32(m/\gamma)\log(en)\) are the primary target, preserving even
the stronger \(n^{-1+o(1)}\) comparison and
\(O(\log(en)^{3d+2})\) retained-storage specialization. Polynomial
target source accuracies and other supplied orders must be qualified
separately. Fixed-problem width asymptotics do not identify \(m,d,L\)
or \(1/\gamma\), or prove simultaneous growing-parameter rates.

## Sources and execution

Scientific inputs are `RESULT.md`, this study's three previous setup-route
notes and their checks, and `docs/notation.qmd`. Other studies and archived
book material are not inputs. The inherited `RESULT.md` hash is
`c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.
The required canonical-notation skill remains inaccessible; the accessible
rigorous proof/research workflows, maintained notation and explicit user
presentation rules are used without claiming access to the unread skill.

The root owns this synthesis, the research record and README. Separately
scoped agents own:

| Component | Artifact | Obligation |
|---|---|---|
| Restarted Taylor construction | LOCAL_CONTINUATION_SETUP.md | Quantitative complex continuation from computed anchors, truncation and global error |
| Streamed assembly | LOCAL_CONTINUATION_ASSEMBLY.md | All source values, exact pairings, unchanged rank/storage and total work/peak memory |
| Real-node polynomial iteration | LOCAL_CONTINUATION_ALTERNATIVE.md | A certified alternative avoiding high activation derivatives, with bounded work |

The initial routes received the same frozen source inputs but not each other's
developing proofs. After they were frozen, the root read all candidates and
assigned cross-route checks. The Taylor author then supplied a real-value
activation backend and identified the source-jet interface needed for the
factored assembly. The root wrote that interface out in full and assigned a
separate combined check. These are internal reconstructions, not isolated
promotion reviews. No training experiment, Git mutation, book promotion or
paper change is part of this theoretical round.

## Main result

Fix an admissible dataset with sample count \(m\), input dimension \(d\),
depth \(L\ge2\), feature-Gram gap \(\gamma>0\), positive label size
\(Y\), activation envelopes and failure probability \(0<\delta<1\), as
in RESULT.md. These parameters are separately fixed, not identified with one
another. For each sufficiently large individual dense width \(n\), on the
existing event of probability at least \(1-\delta\), the construction below
produces a Harmonic model with

\[
\begin{aligned}
\text{setup work}&=O\!\left(n^2\log(en)^{3d/2+1}\right),\\
\text{peak setup memory}&=O(n^2),\\
\text{all retained model storage}&=O\!\left(\log(en)^{3d+2}\right),\\
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_H(t,x)-f_n(t,x)|&\le n^{-1+o(1)}.
\end{aligned}
\tag{1}
\]

The time supremum includes the fitted limit. The last line means the
unchanged original upper certificate has this asymptotic order; it does not
assert an equality or matching lower bound. The stronger original source
tolerance \(1/n\), not merely root-width prediction accuracy, is retained.
Consequently its previously established comparison with actual dense-copy
variability is preserved when \(m\ge2\).

The constants in (1) can depend on the separately fixed parameters above.
This is **not** a simultaneous growing-\(m,d,L,1/\gamma\) estimate.
In particular the logarithmic exponent retains its dependence on dimension.
All finite operation counts, with the parameters and internal orders exposed,
are in equations (8)--(9) of
[the complete assembly bridge](LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md).
All sufficient local radii, degrees, tolerances and gates are explicit in
the component statements linked below; no new stochastic event is introduced.
The inherited stochastic width onset remains unquantified.

Work in (1) counts exact-real arithmetic, with bounded-cost ordinary scalar
activation and elementary-function evaluation, and Gaussian sampling;
supplied initialization removes the latter. Otherwise their separately
displayed costs must be added.
This is the original scalar-cost convention, not an assertion that an arbitrary
analytic function description has a constant-time evaluator. Real-word memory
does not imply a bit-storage bound. The new algorithm needs no oracle for
high activation derivatives, complex activation values or an observed dense
trajectory.

For the circle \(d=2\), (1) becomes setup work
\(O(n^2\log(en)^4)\), peak setup memory \(O(n^2)\), retained storage
\(O(\log(en)^8)\), and the same \(n^{-1+o(1)}\) prediction error.
This is an eventual-width result, not a claim that its sufficient constants
or exact selector are already attractive at moderate widths.

## Construction and certified internal orders

The algorithm reconstructs the required physical-time interval
\(T=32(m/\gamma)\log(en)\) during setup, but does not use first-order
Euler marching. It restarts short local Taylor expansions from its own
computed anchors. Training derivatives always use the actual training data;
designed sphere nodes are passive source queries. Thus the construction
remains data-dependent.

At source tolerance \(1/n\), sufficient counts have the following orders.
Every big-O here has exactly the fixed-parameter qualification of (1).

| Internal quantity | Sufficient order |
|---|---|
| Local continuation panels | \(O(\log(en)^{3/2})\) |
| Taylor degree per panel | \(O(\log(en))\) |
| Temporary activation-polynomial degree | \(O(\log(en)^{3/2})\) |
| Global temporal Chebyshev degree and time quadrature count | \(O(\log(en)^{5/2})\) each |
| Maximum spherical degree | \(O(\log(en)^{3/2})\) |
| Spatial quadrature count and spherical basis count | \(O(\log(en)^{3(d-1)/2})\) each |
| Retained joint time--sphere modes and sufficient selected width \(q\) | \(O(\log(en)^{3d/2+1})\) each |

For \(d=1\), the spatial rule is simply the two inputs \(\pm1\).
These are sufficient orders, not lower bounds or optimality claims. The
general supplied-order formulas remain available; an arbitrarily enlarged
source horizon or selected budget need not satisfy this table.

The execution has four stages:

1. Build certified scalar polynomial approximations to the original
   activations, using real activation values. They are used only in the
   disposable setup computation. Separately compute the exact initialized
   features with the original activations.
2. On each local time panel, compute the shared training jets once. Keep
   dense matrices only at the panel anchor. Express their higher-order
   actions using the rank-one gradient-flow factors, rather than storing
   a dense parameter tensor for every derivative order.
3. Stream passive sphere-query jets into the original **global**
   Chebyshev--harmonic coefficients. Add panel contributions to those same
   coefficients; do not append a new source basis for every panel. Apply
   initialized matrices to the completed coefficient blocks to preserve
   the required source pairing exactly.
4. Run the original coordinate selection and metric/mixer assembly.
   Discard dense anchors, jets, coefficient arrays and temporary activation
   polynomials. The final model uses the original activations and starts
   at original time zero, not at the last setup anchor.

The unchanged final model therefore has the same training and query costs
as RESULT.md. Neither a polynomial evaluator nor the dense continuation
becomes hidden retained runtime state.

## Why the error and cost claims hold

The proof is a composition of separately specified interfaces, not just an
appeal to analytic regularity.

**Local restart from a computed anchor.** The source theorem supplies a
complex-time strip, but alone does not certify numerical restarts. The
[Taylor proof](LOCAL_CONTINUATION_SETUP.md) builds a moving parameter tube,
proves a genuine pairwise local Lipschitz estimate, and constructs an analytic
local solution from an approximate anchor by contraction. The continuation
radius is of order \(1/\sqrt{\log(en)}\) at fixed parameters. A logarithmic
Taylor degree gives polynomially small local defect.

**Global error without a horizon-length exponential.** The prior
[signed stability proof](POLYNOMIAL_SETUP_ODE_ROUTE.md) retains the negative
prediction-discrepancy square and uses integrability of the true training
residual. Its amplification is exponential in a fixed multiple of
\(\sqrt{\log(en)}\), rather than in a horizon-length worst-case
Lipschitz product. Prefix induction controls every computed anchor and
therefore legitimately reuses the local restart theorem. This is not a
proof by assuming the numerical path already stays in its required tube.

**No high-derivative activation oracle.** The
[activation backend](LOCAL_ACTIVATION_BACKEND.md) constructs its scalar
polynomials by finite real-node cosine sums. Nested complex ellipses control
aliasing and truncation; Cauchy estimates then control the first two
derivatives on the needed network domain. It bounds the setup vector-field
perturbation and its derivative, and measures the resulting numerical defect
against the **original** dense field. Online polynomial composition through
time degree \(K\), with polynomial degree \(D\), costs
\(O(DK^2)\) arithmetic and \(O(DK)\) words per scalar. Both orders
are polylogarithmic in the table above. Original exact initialized features
are not silently replaced by approximate ones.

**Source accuracy, pairing and unchanged rank.** The
[combined bridge](LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md) allocates four source
errors separately: local source-series tail, activation replacement, local
parameter-series tail, and accumulated global parameter error. It includes
the necessary \(\sqrt n\) conversion from coordinate to Euclidean error
before initialized-matrix multiplication. The
[positive quadrature](POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md) then recovers
the original global mode set below its original source tolerance. Numerical
panels need not form a globally analytic path: quadrature is proved on the
exact source and then perturbed using finite nodal error bounds.

**Full setup, not only flow integration.** The
[streamed assembly proof](LOCAL_CONTINUATION_ASSEMBLY.md) charges passive
queries, projections, initialized-matrix images, orthogonalization,
coordinate selection, metric construction and dense-to-small mixer assembly.
It explicitly groups the dense anchor update, so that a spurious extra
Taylor-degree factor is not paid for materializing every dense derivative.
The complete specialization before discarding eventual lower-order terms is

\[
O\!\left(n^2\log(en)^{3d/2+1}
       +n\log(en)^{9d/2+3}+\operatorname{polylog}(n)\right).
\tag{2}
\]

The exponent in the last term is fixed when the structural parameters are
fixed; its unsuppressed contributors are in bridge (8). In particular,
the conservative selector contributes the second displayed term and is not
omitted merely because it is eventually lower order. The streamed working
arrays give bridge (9), which is \(O(n^2)\) eventually at fixed parameters.

An alternative [real-node Picard construction](LOCAL_CONTINUATION_ALTERNATIVE.md)
uses only ordinary activation and first-derivative calls. Its
[fast-transform refinement](LOCAL_PICARD_FAST_TRANSFORM.md) independently
gives near-quadratic setup, with \(O(n^2\log(en))\) peak words. It does
not consume the factored Taylor interface and is not used to justify the
sharper peak-memory result in (1). This separate route provides a checked
fallback, not an unsupported interchange of two integrators.

## Comparison with the clarified dense benchmark

Ordinary dense full-batch Euler, with step \(h\), costs

\[
\Theta\!\left(m[(L-1)n^2+n(d+1)]\,T/h\right),
\qquad T=32(m/\gamma)\log(en),
\tag{3}
\]

under the same scalar-cost convention and when \(T/h\ge1\).
For separately fixed admissible structural parameters, (1)--(3) give

\[
\frac{\text{Harmonic setup work}}{\text{ordinary dense Euler work}}
 =O\!\left(h\log(en)^{3d/2}\right).
\tag{4}
\]

Thus any fixed inverse-polynomial step \(h=n^{-\alpha}\), with
\(\alpha>0\), makes the ratio tend to zero. For the user's example
\(h=n^{-1/2}\), this is \(n^{2+o(1)}\) setup against
\(n^{5/2+o(1)}\) Euler work. More generally the sufficient benchmark
condition is \(h\log(en)^{3d/2}\to0\).

Nothing here proves that Euler needs this small a step, that the illustrative
step attains a particular error, or that Harmonic setup beats every dense
solver. A dense solver using the same high-order continuation can omit the
passive queries and compression assembly. The achieved gain is the
near-quadratic construction target and its explicit comparison with the
specified Euler baseline; it is not a solver-independent lower-bound
separation. The construction covers the full physical source horizon, not
a vanishing physical prefix.

## Checks, limitations and supersession

The following checks reconstruct the indicated frozen arguments. Their
reports bind the precise candidate versions and describe inherited inputs.

| Component | Internal check |
|---|---|
| Approximate-anchor Taylor continuation and global defect | [Taylor check](LOCAL_CONTINUATION_SETUP_CHECK.md) |
| Source projection, paired images, factored jets and total costs | [Assembly check](LOCAL_CONTINUATION_ASSEMBLY_CHECK.md) |
| Real-value scalar polynomial backend | [Backend check](LOCAL_ACTIVATION_BACKEND_CHECK.md) |
| End-to-end Taylor/backend/assembly compatibility | [Combined check](LOCAL_TAYLOR_ASSEMBLY_BRIDGE_CHECK.md) |
| Alternative real-node Picard continuation | [Picard check](LOCAL_CONTINUATION_ALTERNATIVE_CHECK.md) |
| Fast transform preserving the complete Picard polynomial | [Transform check](LOCAL_PICARD_FAST_TRANSFORM_CHECK.md) |

The Taylor candidate was corrected before final checking: the late-time
imaginary preactivation bound is \(3a/8\), not the early-time \(a/4\).
Reducing the parameter perturbation allowance to \(a/16\) leaves
\(7a/16<a/2\), which closes the uniform strip argument. The assembly
bridge also adds the passive source-series tail and explicitly switches its
algebraic recurrence interface to the certified disposable polynomial field.
Those are substantive proof interfaces, not inferred from component verdicts.
The final combined audit found no required correction. It binds bridge
`dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b`
to the precise component hashes recorded there; its report hash is
`464879927f860cc236ee7eb06b372bb175299bd97e61f7b2509c9b2da6584f3f`.
The Taylor author separately checked this synthesis against the final
Taylor/backend/assembly interfaces; its two requested clarifications,
\(0<\delta<1\) and the elementary-function scalar-cost convention,
were incorporated. This check did not cover the separately audited Picard
alternative and is not presented as an independent review of that route.

The scalar script `local_picard_transform_check.py` was run with
`python studies/integrated_general_compression_20261004/local_picard_transform_check.py`.
It passed 512 scalar comparisons, with maximum absolute error
\(1.889\times10^{-15}\), covering transform normalization, synthesis,
integration, and the highest coefficient's endpoint contribution. This is
a deterministic algebra check, not neural-training evidence, a timing
experiment or a floating-point stability theorem for the initializer.
The checked script hash is
`6b6f9bd05b02b1a8b07e3351c13e7f53f113efec004cc898788e785c2f605f6b`.
The final study-scoped tracked diff passed `git diff --check`; separate scans
covered whitespace/control characters in the new notes, and delimiter counts
and local Markdown links in all 15 current-round notes and records. The
inherited RESULT.md hash and the final bridge/audit hashes were reverified.
No full Markdown/TeX render was run.

Unresolved issues include a numerically stable finite-precision implementation,
rank/selector conditioning, bit complexity, effective stochastic width onset,
useful moderate-width constants, and optimality of setup work. The earlier
complex-label continuation conjecture remains open but is no longer needed
for this physical-time construction. The earlier initial-jet-only initializer
is still valid; its expensive continuation order is not a lower bound on
algorithms allowed to use the known dense vector field at computed anchors.

This result supersedes the first round's statement that a permitted complete
near-quadratic initializer was missing, under the user's clarified cost-based
contract. It does not supersede the original prediction theorem, change its
model or activation assumptions, or promote an internal result into the
maintained book. RESULT.md, the paper and all other studies are unchanged.
The new research artifacts remain uncommitted.
