# Round 1: isolated document-only mathematical review

**Verdict: NEEDS_CORRECTIONS.**

Source: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`

Source SHA256: `dee7a2fb5c4350d1883d2939f06bca67581274d9b94b44dce9b23225d7a8e62a`

Full-read confirmation: I read the complete document, lines 1–541, including the complete contribution map and final audit obligations. The source has 541 lines and 79,991 bytes. All line references below refer to this hash.

Isolation: the master was my only research evidence. I did not read its linked sources, other project files, histories, source-audit reports, or other reviewers' outputs; did not browse; and did not run experiments or start a proof campaign. I read only the operational review skill and its severity rubric in addition to the master. This file is the sole review artifact.

The required corrections below are localized defects in the master's stated hypotheses and clock conventions. They do not establish that an underlying source theorem is false. In particular, the document correctly treats the canonical quadratic initial-layer result, the bounded-slope counterexample argument, and the fixed-program import as having unresolved audit obligations. Those declarations are not grounds for rejecting an otherwise accurately qualified consolidation.

## Required corrections

### L1. Restore the baseline-slope and positivity restrictions in the perturbation theorem rows

**Location:** lines 251–253, especially the “Two-sample shape class” row at [line 253](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:253).

The odd perturbation row explicitly restricts `1/2 <= a <= 1` and `0 < e`. The shape-class row states an activation `a z + e psi(z)` and an upper bound on `e`, but gives no restriction on `a`. Its stated restrictions on `psi` allow `psi = 0`. Taken literally, `a = 0`, `psi = 0`, and any sufficiently small positive `e` satisfy that row's displayed conditions and give the identically zero activation. Such a network cannot fit nonzero binary labels. The later proviso about nonaffine shapes restricts persistent nonaffinity, not the preceding fitting assertion, and therefore does not repair this counterexample.

The all-depth row at line 252 also drops the explicit ranges of `a` and `e`. “Same geometry/labels” does not expressly carry those parameter restrictions forward.

**Required repair:** state the full parameter range in each affected row. If the intended inheritance is the range in line 251, use:

> `1/2 <= a <= 1` and `0 < e <= c_L delta^{p_L}`

for the all-depth row, and

> `1/2 <= a <= 1`, `0 < e <= c_dyn delta^{31/8}`, and `|psi(0)|, ||psi'||_infinity, ||psi''||_infinity <= 1`

for the shape row. If the source uses a different positive baseline-slope range, state that range instead; this document-only review cannot recover it. A uniform fitting assertion over unrestricted `a` must not remain.

**Impact/severity:** localized scope correction. The small-perturbation theorem and the report's scientific assessment can survive intact. This is not a demonstrated flaw in the source's intended restricted theorem.

### L2. Define the geometric class in the sharp three-sample infima

**Location:** [lines 296–306](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:296), especially the displays at lines 298–304.

Neither displayed infimum has an indexing set. The following sentence calls the class “stated,” but lists only `L`, `d`, `theta`, and `delta`; it does not state the actual separation condition on the input triple. This is material for an odd network. With normalized inputs `x_2 = -x_1`, the feature vectors satisfy `H_2 = -H_1` at every layer, so their Gram matrix has a zero eigenvalue. Duplicate inputs give another zero eigenvalue. Thus the positive lower bound cannot hold over arbitrary normalized triples, and one-sided exclusion of duplicates alone does not suffice.

**Required repair:** define the admissible set before the display, including normalization and two-sided pairwise separation. For example, if this is the intended source class, write

\[
\mathcal A_{d,\delta}
=\left\{(x_1,x_2,x_3):
\|x_a\|^2/d=1,\quad
|x_a^Tx_b|/d\le 1-\delta\quad(a\ne b)\right\},
\]

and put `inf_{(x_1,x_2,x_3) in A_{d,delta}}` on both eigenvalue expressions. State any strict-versus-nonstrict convention needed by the source. Also identify `Q_L(0)` as the initialized feature Gram and `q_L` as its common diagonal entry. Do not silently impose positive definiteness of the raw input Gram: singular planar triples are explicitly part of the stated sharpness discussion.

The report does not give enough information to certify that the example class above is exactly the source's class. If its exact geometry cannot yet be supplied, label the displayed sharp result as a source summary with its admissible class awaiting specification, rather than asserting universality over the currently listed scalar parameters alone.

**Impact/severity:** localized but substantive theorem-scope omission. The depth and nonlinearity scalings are not refuted once the intended admissible class is restored.

### L3. State the nonzero residual/label conditions in two deductions

**Locations:** [line 145](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:145), with the canonical contract at lines 120–127; and [line 437](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:437).

**Loss jets.** The statement that physical-loss coefficients inherit divergence through the residual clock needs a nonzero initial residual. The canonical description here does not specify the label. For a formal feature series with `F(0)=0`, square-loss physical time satisfies

\[
\frac{ds}{dt}=c\,[y-F(s)],\qquad s(0)=0,
\]

where `c>0` is fixed by the loss normalization. If `y=0`, the formal solution is `s(t)=0`; the corresponding formal prediction and loss are stationary, irrespective of the divergent higher feature coefficients. The clock is not formally invertible at initialization. This counterexample concerns the formal deduction, not an assertion about actual finite-network paths.

**Required repair:** specify the nonzero target used by this no-go family, for example:

> For the normalized nonzero-target problem (`y=1`, `F(0)=0`), the residual clock has nonzero initial derivative. The formal physical-loss series consequently inherits the feature-series divergence. The zero-initial-residual case is excluded from this deduction and from the asserted subtarget hitting-time statement.

More generally replace `y=1` by the intended assumption `y-F(0) != 0`, with the clock and loss normalization stated. This leaves the formal-versus-actual distinction in lines 145 and 159 intact.

**Symmetry obstruction.** Line 437 says equal-label antipodes cannot both fit in a bias-free odd network. That is false for equal labels zero: `f=0` fits both. The report elsewhere permits real labels, so the nonzero condition should be explicit here.

**Required repair:** use “antipodes with the same **nonzero** label cannot both fit.” For the even-first-activation case, state the actual constraint `f(-x)=f(x)` and its obstruction for unequal labels.

**Impact/severity:** localized hypothesis corrections. No claimed nonzero-target obstruction is overturned.

### L4. Identify the clock in the exact activation-stability witness

**Location:** [lines 105–112](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:105), in conjunction with the normalization warning at line 51.

The exact updates `4h 1` and `3h 1` are feature-gradient updates. They are not, as written, the two updates under a common physical square-loss GD step: the activation perturbation changes the initial prediction and hence the residual multiplier. The paragraph does not specify which update it is using.

This can be checked directly from its arrays, without the linked source. Put `psi_n = psi + n^{-1/2}` and interpret the readout as `a_0 = sqrt(n) e_1`. Under the displayed network normalization,

\[
f_{\rm ref}(0)=0,
\qquad f_{\rm pert}(0)
=\frac{1+\pi/4}{\sqrt n}+\frac1n,
\]

while

\[
n\nabla_{z^{(1)}} f_{\rm ref}=4\mathbf1,
\qquad
n\nabla_{z^{(1)}} f_{\rm pert}=3\mathbf1.
\]

Thus a common feature-ascent Euler step `h` gives precisely the reported updates. For half-square loss with target one and a common physical step `h`, the updates are instead

\[
4h\mathbf1,
\qquad
3h\bigl(1-f_{\rm pert}(0)\bigr)\mathbf1.
\]

Full square loss introduces an additional common factor two. In either normalization the order-`h` discrepancy persists, so the deterministic stability refutation is preserved.

**Required repair:** explicitly say “For a common feature-time Euler step of `dot z^{(1)} = n grad_{z^{(1)}} f`, the updates are …,” or give the actual residual-weighted updates for the intended physical loss. In line 108 also write `W_0^{(3)} = sqrt(n) e_1`; the current comma obscures the vector multiplication.

**Impact/severity:** localized normalization correction, not a repair of the pending annealed counterexample theorem. The report is right that a deterministic bad state does not by itself settle a Gaussian-typical statement.

## Checks that survived the adversarial audit

### Finite-width GF and the deterministic diagonal

Lines 223–238 give a valid bridge, with the population theorem's qualifications preserved. At a fixed width, for a constant nonnegative diagonal mobility `D_n` and nonnegative square loss,

\[
\|D_n\nabla\mathcal E_n\|^2
\le \|D_n\|\,
\nabla\mathcal E_n^T D_n\nabla\mathcal E_n
=-\|D_n\|\,\dot{\mathcal E}_n.
\]

Integration proves the displayed bound. On a hypothetical finite maximal interval, Cauchy–Schwarz makes the remaining path length tend to zero, giving a finite parameter endpoint. Local Lipschitzness then extends the solution. This argument neither needs invertible mobility nor a width-uniform Euclidean bound.

Fixed-width Euler convergence and continuity of the finite network give the listed path, kernel, and fixed-probe comparisons. The derivative comparison uses continuous hidden Jacobians and the convergence of the parameter velocities; it does not require second derivatives of the activations. Pairing neuron indices is legitimate for this fixed-width GD/GF comparison.

For each width, convergence in probability as the step decreases permits a deterministic step satisfying line 235. The theorem's **every deterministic vanishing sequence** quantifier then gives the triangle-inequality conclusion for any chosen finite family of admitted observables. It gives no uniform Euler rate and does not upgrade arbitrary probe classes or population time horizons. The square-loss global finite-GF proof is appropriately distinguished from the stopped separable-loss extension.

### Formal jets, actual paths, and no-go scopes

The smooth nonanalytic Gaussian example at lines 147–159 is correct. Its derivatives are dominated by finite Gaussian moments, its Taylor coefficients have zero radius, and the two-dimensional autonomous clock ODE has the stated unique solution. It therefore refutes the proposed inference from zero radius to nonexistence of any smooth ODE. It does not identify any neural trajectory.

The report appropriately distinguishes finite-order Hankel tests from all-order Stieltjes positivity, formal inverse-series constructions from actual inverses of identified trajectories, and metric/activation-specific negatives from the canonical unit-metric quadratic question. The high-order coefficients and rational certificates are reported evidence whose upstream generation is expressly not certified here.

The covariant-Schur and tagged-DMFT statements remain qualified in the operative conclusions. A fixed positive output jump at times tending to zero would indeed obstruct uniform convergence to a continuous output, provided the jump occurs with probability bounded away from zero. No conclusion about a settled canonical initial layer is extracted here.

The representation no-gos are restricted to the stated encoders and full state domains. They do not contradict infinite-dimensional operator dynamics, orbit-specific encodings, or approximation schemes. The master does not provide their complete contraction-independence proofs, so this is a check of scope and internal compatibility, not independent certification of those external proofs.

### Clipping and response concentration

The three rows of section 8 are not interchangeable, and the report correctly declines to concatenate them. The displayed growing-cap estimate tends to zero for `R_n=o(log n)`: its logarithm is `-(1/24) log n + o(log n)`. Agreement of two varying constructions does not supply convergence of either.

For the metric projection, let `e_R=M(delta-u_R)`. The box optimality conditions imply `e_i=0` in the interior, `e_i>=0` at `u_i=R`, and `e_i<=0` at `u_i=-R`. Therefore `e_R^T u_R=R ||e_R||_1`, exactly as displayed. The integral estimate needs the stated work bound; the optimality identity alone would not prove it. The document presents it as a source result, rather than deriving that work bound from the identity alone.

The normalized `L^1` defect bound controls bounded adaptive tests but not RMS defects or squared work. For example, a defect vector `sqrt(n) e_1` has normalized `L^1` norm tending to zero and normalized RMS norm one. Inactivity above `C_S sqrt(n)` is compatible with an RMS bound; it does not imply inactivity at coefficient-one `sqrt(n)` or provide a fixed-cap population theorem.

The rare-coordinate product obstruction is valid. The generated-action construction is explicitly separated from actual training queries, and the actual-state non-Lipschitz statement is not incorrectly turned into nonexistence or nonuniqueness of the constructed flow. The proposed Osgood tail criterion is consistent with a comparison cost linear in the cutoff: balancing the stated tail gives a modulus of order `u log(1/u) log log(1/u)`, whose reciprocal has divergent integral at zero. This checks the proposed sufficient mechanism, not its unproved trajectory premise.

## Complete displayed-formula coverage

“Reported” in this table means the formula depends on source machinery not supplied in the master. It is not a new adverse verdict or an independent proof certification.

| Master lines | Formula/deduction | Document-only assessment |
|---|---|---|
| 43–47; 49–51 | Forward normalization and mobilities | Internally consistent. Changing `W^{(1)}/sqrt(d)` to `V^{(1)}` changes the first mobility by `1/d`. Small stored readout is properly distinguished from order-one readout with vanishing averaged prediction. |
| 80–83 | `D^3 f` | Correct for the fixed flat learning metric: differentiate `Df=||grad f||^2` twice. A state-dependent metric would require extra terms, but is not the stated setting. |
| 93–99 | Coarse/fine cubic coefficient and remainder | The finite-step quantifiers are kept separate from mesh-uniform control. The coefficient compiler and depth-dependent remainder are reported; the master does not supply their full derivation. |
| 107–112 | Deterministic witness | Directly checkable; requires the feature-clock repair L4. |
| 123–127 | Formal Stieltjes moments | Properly identified as formal. The moment counts and coefficient values are source-dependent. |
| 149–159 | Zero-radius smooth function and autonomous ODE | Correct; the neural physical-loss claim separately needs L3. |
| 179–191 | Deep-linear output, cyclic flow, kernel, action bound | Compatible with the usual ordinary block trace and gradient identities. In particular the flow gives `dot f=2 eta (y-f) K`. The trace-norm action bound additionally uses the reported cyclic finite-rank structure; that structure is not constructed in the master. |
| 216–221 | Reference-tail comparison | No internal contradiction; a reported estimate with clearly stated reference-only and cutoff/mesh quantifiers. |
| 225–238 | Finite-GF energy and deterministic diagonal | Valid, as checked above. |
| 259 | Feature clock, kernel floor, loss rate | Constants are consistent in the stated normalized one-sample square-loss convention: `4(25/36)=25/9`. Clock divergence at the first hit uses local upper control of `df/ds` as well as the lower kernel bound; the paragraph supplies a controlled feature interval containing that hit. |
| 263–266 | Sufficient gain | Source-dependent; `c_psi` is not defined in the master. See optional suggestion O1. No independent numerical certification. |
| 272–278 | Relative affine-fit error | Correct for the positive perturbation strength used here: take slope `a` and intercept `e E psi(Z)`, use the independent-copy variance identity, and obtain the lower denominator `(a-e)^2 Var(Z)`. The offset version is covered because the best affine fit absorbs the offset. The odd equal-coefficient case is correctly excluded from this bound. |
| 298–308 | Sharp initialized Gram and nonaffinity asymptotics | The infima require L2. The stated fixed-`theta` variance and nonaffinity powers are mutually consistent; their full depth-uniform proof is reported, not reproduced. |
| 326–331 | Coordinate-query clipping | Auxiliary dynamics is explicitly distinguished from original GF. Global fixed-feature-time identification and its Lipschitz estimate are reported. |
| 335–340 | Growing-cap error | The displayed convergence follows at the stated cap scale. It gives comparison, not an uncut limit. |
| 344–357 | Metric, optimality identity, weak defect | `M` is positive semidefinite; the box identity and defect interpretation are correct. The integrated work bound and inactivity constants remain reported estimates. |
| 365–370 | Gate difference times reverse field | The asserted failure of an ambient `L^2` product estimate is correct. Bounded gates do not repair concentration of squared reverse-field energy. |
| 376–380 | Generated Gaussian response law and `L^p` growth | Internally consistent as a population/width-limit coordinate law. An even bump removes the first transpose mean response; the return response has coefficient `E sech^2(G)`. Conditional Jensen gives the stated lower growth from the bump term. Finite-width exactness should not be inferred; see O2. |
| 387 | RMS-normalized kernel and balance qualification | The kernel's numerical value needs the omitted normalization calculation. The report does not infer global identification or positive-time activity from it. |
| 393–397 | Scalar-particle residual scaling | `nL` mobility is compatible with a `1/(nL)` particle contribution. The architecture is expressly distinct from dense Gaussian connectors. |
| 401–404 | Bounded residual example | The nested tanh example meets the stated boundedness and derivative requirements on bounded state strips. |
| 408–413 | Averaged initial `W_1` error and joint limit | Given the displayed stability theorem, the deduction is correct: identical layer initialization laws make the expectation of the averaged error equal to the single-layer expectation, independent of `L`. Independence across layers is not needed for that expectation calculation. |
| 441–448 | Opposite-label contrast and readout lower bound | Correct for probability-normalized neuron `L^2` norms and prediction error at most `epsilon` for labels `+1,-1`. It is a necessary scale cost, not impossibility at fixed positive variation. |
| 456–461 | Mean-square loss and metric kernel | Correct with `L=||r||^2/m` and `K=J D J^T`. A uniform positive residual-direction lower bound gives rate `4 kappa/m`; the text correctly requires that bound along training. |
| 465–471 | Prescribed-accuracy probability bridge | Correct. Later accuracy preservation requires monotonicity of the actual finite loss, as expressly stated; it is not an all-time trajectory or endpoint limit. |

I also checked the inline scopes and deductions in the remaining prose and task map. In particular, fixed update count is not promoted to a growing program, fixed depth is not promoted to a trained continuous-depth limit, nonzero initial activity is not generally promoted to persistent activity, and fitting is not promoted to generalization. External theorem descriptions, empirical numbers, coefficient-generation assertions, and reported read/hash provenance cannot be independently verified under the imposed isolation.

## Optional suggestions, not conditions for the verdict

**O1 — Define the gain constant (lines 261–266).** Introduce `c_psi>0` as the exact shape-dependent constant from the source, or expressly say its definition is not reproduced. The displayed gain is currently unusable as a numerical prescription. Do not invent an infimum defining `c_psi` without its source contract.

**O2 — Type the Gaussian law explicitly (lines 375–380).** Add “in the width-limit coordinate law, with `G` standard normal independent of `Y`,” or explicitly identify the symbols as population operators. The adjoint notation and generated-space discussion support that interpretation already, but the distributional equality should not be mistaken for an exact identity at finite `n`. It is also helpful to state that width is taken first at fixed bump scale.

**O3 — Make the pending initial-layer probability quantifier visible (line 165).** If restating the implication, use fixed `c,p>0` and deterministic `t_n -> 0` with `liminf P(sup_{t<=t_n}|f_n(t)-f_n(0)|>=c) >= p`. That suffices to obstruct uniform convergence in probability to a continuous limit. A rare event whose probability vanishes would not suffice. This suggestion does not reopen or resolve the declared source follow-up.

**O4 — Repair damaged inline math delimiters.** Examples include the reused-matrix response coefficient at line 72, `r(u)=(1+u^2)^{-1}` at line 153, the parenthesized ReLU time constant at line 169, `(1-theta)z+theta arctan(z)` at line 296, and the readout lower bound `(1-epsilon)/a` at line 448. These are mostly presentation defects; L4 separately addresses an exact update whose clock matters mathematically.

No request for an experiment, new proof campaign, complete resolution of the central research objective, or blanket re-audit of unavailable sources is made by this review. Correcting L1–L4 would remove the substantive internal defects identified here while retaining the master's honestly declared source qualifications.
