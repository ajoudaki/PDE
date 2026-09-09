# FINAL ASSEMBLY / INTEGRATION AUDIT

Date: 2026-09-09.

Verdict: **CLEAN for the assembly/integration scope specified below.**

Required corrections found: **none**.

This is a fresh, isolated audit of the incorporated library. It checks the reading guide against exact chapter statements, shared notation, parameter storage, loss clocks, observables, internal dependencies, crossreferences, and the implementation/reproduction contract. It is not a complete independent proof review of every older chapter. CLEAN means that no required correction was found in this audit's inspected material and checks; it does not certify unread proofs.

Sole source root: /tmp/pde-incorporated-library-round2.GAhQOu8u.

Report directory: /tmp/pde-final-assembly-audit.UX7jW5ee, created fresh with permission mode 0700. No source inputs were edited. Whole-file SHA-256 values taken before and after the audit agree for all 25 source files. The source inventory remained unchanged.

## 1. Isolation, execution, and read scope

All project-source reads were confined to the specified source root. No studies, historical research files, prior reviews, other project checkouts, network sources, or other agents were consulted. External bibliography links in the guide were read as part of the guide, but not opened or independently verified.

The only numerical execution was the authorized small “make check”, plus an interpreter/NumPy version query. There were no training experiments, dependency installations, builds, or PDF generation. Source-text inventory, hashing, and crossreference scans were read-only. The supplied structural tests create and remove their own small temporary fixtures outside the source tree; they do not inspect a research tree.

Full-text reading covered 11,989 of the source tree's 26,350 lines. Eighteen files were read completely; seven mathematical chapters were read selectively. The exact inclusive line ranges and whole-file hashes are recorded in Appendix A. Appendix B additionally hashes each selected contiguous passage, preserving its actual bytes and line endings.

The following specifically requested material was read in full:

| Material | Exact full section coverage |
|---|---|
| docs/README.md | Entire guide, lines 1–264 |
| docs/NOTATION.md | Entire notation contract, lines 1–98 |
| code/README.md | Entire implementation/reproduction guide, lines 1–271 |
| Gaussian calculus | Section 7, lines 1817–2433; Section 8, lines 2434–3296 |
| Linear comparisons | Section 2.A, lines 376–557; Sections 8–12, lines 1357–2641 |
| Special-data initialization geometry | Entire Part V, lines 7982–9325 |
| Special-data chapter framing | Front and conventions, lines 1–133; final scope, lines 9326–9362 |
| Earlier special-data compactness contract | Entire Part IV introduction/model/theorem, lines 6384–6664; entire IV.12 scope, lines 7936–7981 |
| Finite-controls additions | Entire Sections 10–11, lines 1240–1735 |

Additional full passages include finite_dynamics.md, Gaussian Section 6, linear Sections 1–2, 5 and 7, special-data III.A, and every Python implementation, test, and structural-check file. Other selections inspect the exact older theorem/model statements and relevant dependency interfaces.

Chapter-wide heading, keyword, link, and equation-label scans are structural inspection, not full-text mathematical reading. Two broad heading listings were truncated; no completeness claim is based on those listings. Required statements and sections were subsequently read through bounded text chunks. The exact substantive-read ledger below excludes unexamined surrounding proof text.

In particular, this audit does not independently certify Gaussian Section 5's unread conditioning/rank/concentration proof, the older arctangent/global-nonlinear construction proofs, special-data Parts I–III's unread dynamics proofs, Part IV's interior compactness proof, the older linear nonclosure proof, or the unread finite-optimization/continuous-depth proofs. Reading their stated contracts establishes what the assembly may claim; it does not independently discharge all their mathematical obligations.

## 2. Guide-to-chapter agreement

The guide's chapter-role table is at docs/README.md:150–159. Its claims match the inspected exact statements at the following scope.

| Guide entry | Statement inspected | Assembly assessment |
|---|---|---|
| Finite dynamics | finite_dynamics.md, entire chapter | Arbitrary fixed depth and finite batch; mean squared loss; exact gradients, mobility-weighted kernels and dissipation; global finite-width GF for C2 activations. Bounded slopes supply the further finite-horizon RMS bounds. No population identification is inferred. |
| Gaussian and flow calculus | Gaussian Sections 4, 5.1–5.3, 5.5, 5.11, 6–8 | Order-one-readout fixed programs, arbitrary finite-state moving jets, and the separately specified frozen-first-block certificate remain distinct. Section 8 is a fixed-depth/fixed-update-count, width-first feature-ascent comparison. |
| Arctangent limits | arctan_limits.md:1–128, 690–904, 1306–1484 | One input/label one and small stored readout. L2 has a global compact-time theorem with eta_n sqrt(n) tending to zero. L3 uses eta_n=n^-2 on its explicit local interval. Fixed-cap global feature-time flows are auxiliary. |
| Global nonlinear learning | global_nonlinear.md:1–180 | One input/label one, fixed activation 1+arctan/10, every separately fixed L>=3, small readout and eta_n=n^-2. The statement includes fitting, compact-time observables, persistent nonaffinity and every-positive-time hidden feature motion. |
| Special data | special_data_limits.md front, I.1, II.1, III.M, III.A, IV.1/IV.12, Part V and final scope | The three full-limit families, partial correlated-data compactness result, and initialization-only comparisons have separate contracts. No arbitrary-dataset theorem is substituted. |
| Linear comparisons | linear_dynamics.md:1–557, 735–815, 908–1017, 1248–2641 | The older L3 GF/GD theorem remains separate from the added one-input GF comparisons. The added general-depth statement does not claim GD, neuron-coordinate laws, or general-data convergence. Fitting is stated for the spectral L2 result and the older L3 result, not silently for every added comparison. |
| Continuous depth | continuous_depth.md:1–154, 329–391, 1474–1490 | Scalar residual particles, no dense trainable hidden matrices or separate readout, half-mean loss, assumptions A1–A2, constant-depth initialization for the quantitative joint comparison. Exact GF width/depth convergence is not a GD or dense-Gaussian theorem. |
| Finite optimization/controls | finite_optimization_and_controls.md selections in Appendix A, including full Sections 10–11 | Canonical finite L3 arctangent optimization/endpoints, a different metric projection, and mixed-activation L2 finite-GF fitting remain distinct. Gate mass has its augmented event and is not stated as hidden motion. |

Specific scope boundaries that survived integration:

- Special Part I covers opposite labels only at rho=0 or rho=-1. Its chapter summary explicitly excludes asymptotic fitting; strict progress is a different claim.
- Part II covers equal binary labels and every fixed -1<=rho<1. Its finite residuals need not occupy the exact population label mode.
- Part III uses three samples, binary labels, a one-sided separation condition G_ij<=1-delta, and a bounded-shape perturbation of a large affine gain. Its chosen activation is independent of depth; convergence is still for each separately fixed depth. The stated nonzero initial acceleration is not upgraded to positive speed at every later time.
- III.A's common-gain classes and depth-uniform absolute nonaffinity margins are not uniform width convergence over an infinite class, nor uniform relative nonlinear strength.
- Part IV's compact containment does not identify a unique population law or a common GF/GD subsequential limit.
- Part V's sequential initialized width/depth comparison does not imply trained dynamics or an L=L(n) theorem.
- The guide's finite-accuracy transfer argument uses a fixed T_epsilon after a fitting theorem for the same model. It does not interchange the width limit with infinite training time or identify optimizer endpoints.
- The guide explicitly leaves generalization, general input populations and dense joint trained depth/width/time convergence open. No inspected chapter summary contradicts that boundary.

## 3. Notation, storage, clocks, and readout normalization

### 3.1 Shared finite model and code

The implemented hidden forward action is W^(ell) h^(ell-1), with no extra width factor. First preactivations use W^(1)x/sqrt(d); predictions use the stored readout pairing divided by n. Residuals are f-y and are excluded from delta. These conventions agree between NOTATION.md, finite_dynamics.md equations (1)–(5), code/README.md and finite_network.py.

The first/readout mobilities are n*kappa; middle mobilities are kappa. Code kernel blocks already include the chosen mobility multipliers and exclude the loss factor 2/m. Its output and energy identities therefore have exactly the guide's factors 2/m and 4/m^2.

The linear chapter deliberately puts its common kappa outside its unit-mobility K. That explicit local convention is consistent with dot(r)=-2*kappa*r*K; its K must be multiplied by kappa when compared with the code's mobility-weighted kernel.

The special-data alternative storage V^(1)=W^(1)/sqrt(d) changes its first-block metric to d||dV^(1)||_F^2/n. Equations (C.1)–(C.4) preserve the canonical first update and rank-one matrix normalization. Part IV and Part V state their use of canonical W^(1) directly. The scoped aliases do not change the optimizer.

### 3.2 Physical-time conversions

For a dense-network loss L_c=c sum_a r_a^2, the stated conversion is

\[
\theta_c(t)=\theta_{\mathrm{mean}}(cm\,t),\qquad
\eta_{\mathrm{mean}}=cm\,\eta_c.
\]

The same initialized raw iterates are being compared. Recomputed observables do not change this factor.

| Result | Loss | Conversion to the code's mean-loss convention |
|---|---|---|
| One-sample arctangent/global/linear models; physical jets | r^2 | No sample-loss conversion |
| Special Parts I, II, IV | Sum of two squared residuals | Mean-loss time and step are twice the theorem's time and step |
| Special Part III | Half sum of three squared residuals | Mean-loss time and step are 3/2 times the theorem's |
| Finite-controls Sections 10–11 | Sum of two squared residuals | Mean-loss GF has half the displayed velocity and needs twice the displayed physical time |
| Continuous-depth benchmark | Half mean squared loss | Half the full-mean-loss velocity at the same mobility; its distinct parameter architecture/mobility must also be retained |
| Gaussian Sections 5 and 8; Section 7.2 certificate | Feature ascent, no residual-loss factor | No fixed loss-clock conversion to raw physical GD |

The arctangent coordinate primitives F(z)=z+z^3/3 and F(z)=10(z+z^3/3) for the shifted activation are continuous-flow changes only. No inspected implementation or integration statement treats raw GD as exact Euler in those transformed coordinates.

Gaussian Section 7.1 retains the moving physical residual. Its third-order clock conversion (J11) includes the additional F'F'' and (F')^3 contributions; multiplying feature derivatives by powers of the initial clock speed would not be its algorithm.

The special Part II feature clock ds/dt=4(1-g) is explicitly a population label-mode construction. The chapter expressly delegates actual finite off-mode residual control to II.C.4 rather than imposing that scalar clock on finite raw GD.

For Part IV, the strong velocity fields are derivatives along the raw interpolant, whereas the residual-weighted GD kernel in (IV.19) uses held node fields. IV.12 explicitly declines to equate that kernel with a kernel recomputed inside an affine cell. This distinction is preserved in the final chapter scope.

### 3.3 Readout regimes and layer types

The finite initializer draws stored readout entries with standard deviation 1/n. That agrees with the nonlinear small-readout convention and Part V's vanishing initial hidden kernel blocks.

Gaussian fixed programs, the quadratic certificate, and all linear comparisons explicitly use order-one stored readout. The code's initializer does not claim to initialize those regimes. General Parameters states and flow_jet accept finite states independently of an initialization law; the exact certificate has its own analytic specification.

Normalized linear endpoint vectors, such as W^(L+1)/sqrt(n), are proof embeddings. They do not change the stored readout distribution. The spectral measure nu in EC11 has mass two, as explicitly stated; it is not silently interpreted as a probability measure.

Finite transposes and population adjoints retain the two directions of the same matrix. Rank-one operators contract within the input layer and have finite representative uv^T/n in the nonlinear population convention. The linear Hilbert representatives use ordinary Hilbert pairings, with their normalization supplied by their endpoint embeddings. No cross-layer neuron pairing or cross-width operator subtraction is introduced by the summaries.

## 4. Gaussian Sections 7–8: integration and dependency closure

### 4.1 Moving physical-flow jets

Section 7.1 is a finite result for L=2, one sample, arbitrary input dimension and finite state, one shared C3 activation, and positive block multipliers. Its input Gram may be zero. The recurrence (J6)–(J8) uses ordinary coefficients v^(k)(0)/k!, moves every raw block, applies the actual moving transpose, and retains all residual coefficients.

The terminal forward coefficient uses activation derivatives through order R<=3; backward coefficients stop at R-1. The text's C3 assumption, local C3 path argument, small-o Taylor conclusion, and finite_jets.py derivative budget agree. No fourth derivative, convergent series, width theorem or positive-time error bound is promised.

The implementation exposes exactly the documented shapes, import location, factorial conversion, ownership rules and numerical limitations. Callback semantics and regularity remain caller obligations. Mantissa/exponent scaling protects the specified scalar combinations; raw contractions and higher composition products retain ordinary float64 limitations.

### 4.2 Forests and the exact certificate

The forest result is expectation factorization at fixed graph size. The quotient-graph count retains only pairings that do not join distinct original components at leading order. It does not supply concentration or a trained empirical-law theorem. The canonical forest key separately implements colored graph isomorphism, preserving component multiplicities.

The certificate specifies quadratic activation, order-one stored readout, feature ascent, and zero first-block mobility. It has its own conditional Gaussian initialization-jet derivation through (7.C1)–(7.C5); it does not invoke the bounded-slope fixed-program theorem for the quadratic activation.

The exact arithmetic implementation generates the derivative polynomial recurrence, inverse series, six moments, shifted determinant and witness. It does not load a retained coefficient table. The negative shifted determinant and negative quadratic witness agree with the displayed fractions and with independent checking routes in the tests.

The conclusion is confined to the proposed nonnegative Stieltjes moment representation for a class including the zero-first-mobility metric. It is not a unit-metric obstruction, a strictly-positive-first-mobility theorem, or nonexistence of a nonlinear population flow. The guide and code guide retain those limitations.

### 4.3 Fixed-program step doubling

Theorem 8.1 matches the Section 5 model: one input, order-one stored readout, simultaneous feature-ascent updates, fixed L and N, with h distinct from physical eta_n and the proof mesh.

The relevant dependency chain was inspected at its interfaces:

1. Section 4 supplies finite Gaussian square roots and moment identities, including singular covariance.
2. Sections 5.1–5.3 specify the width theorem, exact stored-coordinate algorithm and (2N+1)(L-1) action chronology.
3. Section 5.5 supplies the inverse-free scalar program and defines ambient source derivatives with deterministic coefficients held fixed.
4. Section 8.2 reorganizes those assignments into chronological expectation calls; the special L=1 case has its own scalar recursion.
5. Lemma 8.2 provides singular-covariance Price differentiation by regularization, with uniform convergence of the derivative integrals.
6. Section 8.4 separates exact coefficient jets from absolute envelopes. The guarded derivative count allows activation order at most 12 and scalar/covariance derivatives through order five.
7. Section 8.5 supplies the explicit finite recurrence defining E_(L,N), including call count, dimension factors and Gaussian moment cost.
8. Sections 8.6–8.7 give odd parity, the explicit linear coefficient N sum_(a=0)^L mu_(phi')^a, cubic cancellation, and the fifth-order integral remainder.

The Section 8 hypotheses imply the activation assumptions stated in Section 5. The width theorem is used separately at fixed nonzero h and 2h; zero step and constant activations are handled separately. No uniform inverse-Gram gap at h=0 is borrowed from Section 5, and no growing update-count conclusion is imported.

The guide's “exact compiler” refers to the finite mathematical Gaussian-integral construction in Section 8. The implementation guide expressly disclaims a general population compiler. Its small rational primitives and finite jets are not presented as executable implementations or experimental verification of the general Section 8 theorem. This is consistent.

The unread interior proof of Section 5 remains an inherited theorem dependency, not an independently recertified result of this audit.

## 5. Linear Section 2.A and Sections 8–12

Section 2.A provides the operator facts subsequently used: compact singular expansions, trace-norm completeness, ideal bounds, trace continuity/cyclicity, finite-rank Gram reduction and trace-tail control. The later contraction and continuation arguments have an internal operator-space foundation.

The three added comparisons preserve different states and observations:

| Result | Restart state and essential contract |
|---|---|
| EC8, shallow nonlinear GF | Full marked pair (A,U), with consistent residual; every finite moment is an admitted restart domain. Compact-time scalar outputs and separate block energies converge. Under the nested iid coupling this is almost sure. No path-law or fitting theorem is added to its statement. |
| EC10, every separately fixed linear depth | Endpoint Hilbert vectors, each trace-class trained increment, residual consistency, and immutable Gaussian source. Rooted scalar programs, finite-rank Schatten readouts, increment trace norms, individual singular values and tight trace tails are covered. It does not compare matrices in different ambient spaces. |
| EC11, two-hidden-layer linear spectral GF | Current complex Hilbert-field pair and residual, with restart asserted along the initialized solution. The initial source measure and negative atom are retained. Its fitting estimate is |r(t)|<=|y| exp(-3*kappa*t), based on K>=3/2 along that solution. |

EC9 proves the required fixed-word Gaussian laws and bounded source norms for an arbitrary fixed finite number of matrix labels. It does not assert adaptive growing-program convergence or a sharp largest-singular-value limit.

EC10's energy estimate controls trace-norm increments because each matrix velocity is rank one. The Picard and finite-rank approximation arguments operate within each width space before comparing scalar Gram readouts. Equation (EC10.7) includes the full singular-value tail, not only finitely many values.

EC11 uses a single normalized datum; its first-matrix projection has input Gram one and leaves orthogonal first-row directions unchanged. The finite constants C_n and delta_n, matrix-valued spectral source, scalar encoding and three separate block-energy formulas agree. The negative atom -1/2 is present in the source and explicitly handled in the positivity/continuation argument.

Section 12's overlaps at L=1, L=2 and L=3 are comparisons of limits of the same finite readouts under the same initialization and clock. The old root-color construction and EC9's two source sectors have matching rooted Grams. No new raw-GD conclusion is attached to EC8/EC10/EC11. The older nonclosure statement inspected in Section 5 remains restricted to its bounded-contraction, state-universal encoding class; Section 7 explicitly illustrates why arbitrary field encoders lie outside it.

## 6. Special Part V and compatibility with older contracts

### 6.1 Part V's self-contained initialization comparison

All of Part V was read, including its Gaussian/Hermite foundations and endpoint arguments. Its own finite-width proof uses fresh independent initialized matrices at each layer; it does not use a trained-state Gaussian recursion.

The raw feature Gram Q is uncentered. Its unit-diagonal normalization C=Q/q is distinguished from a centered feature Pearson correlation, and the reciprocal spectral condition number is separately bounded. This matters for the offset family.

The three comparisons have correctly separated quantifiers:

- Literal odd mixture: phi_theta=(1-theta)z+theta arctan(z), with 0<theta<=1. The sharp infimum comparison (V.O.3) uses d>=2 and 0<delta<=1/4, with strict two-sided separation. The lower-bound argument has the stated broader realizable separation range. Antipodal exclusion is essential for odd features.
- The variance decrement, summable nonlinear weights, cubic tensor lift and explicit strict planar triple support the stated joint orders. Raw conditioning decays at fixed positive theta as depth grows, while normalized conditioning has a positive floor at fixed separation. Scalar absolute and relative nonaffinity both decay with depth; they are distinct from sample-Gram conditioning.
- Literal convex offset: fixed epsilon in (0,1/2) and a fixed bounded nonconstant C2 shape with bounded first two derivatives. Its contraction constant is strictly below one uniformly in the visited compact variance range. Both scalar nonaffinity notions can have positive depth-uniform floors while the normalized sample Gram tends to rank one.
- Calibrated family: one phi_L is used at every layer of a depth-L network, with gamma_L=sqrt(tau/L). It deliberately changes the activation with L. Orthogonality cancels its linear cross term and keeps every initialized variance one. The correlation interpolation converges after taking width first, with the explicit depth-discretization estimate. That estimate supplies no finite-width error bound when L grows with n.

Part V's comparison with the gain activation is also scoped correctly. Dividing a gain activation by a scalar changes the inner arguments at later layers; it cannot generally be absorbed into a final kernel rescaling. A positive absolute nonaffinity margin need not imply a relative margin. These points agree with Part III/III.A and the guide.

### 6.2 Earlier Part IV contract

The inspected statement covers actual small-readout GF and raw GD with eta_n=n^-2 at fixed -1<=rho<1. It quantifies compact containment over all deterministic initial outcomes satisfying its event bounds, and then supplies explicit probabilities for actual Gaussian initialization.

The topology is W2 on a product containing strong time-L2 velocity coordinates and continuous path coordinates. Along a convergent subsequence it retains derivative compatibility, raw first-row increments, all three kinetic densities, and the entire residual-weighted first-kernel matrix in time-L1. The antiparallel reconstruction uses G/4 instead of G^-1.

The statement and IV.12 agree on exclusions: no unique/full-sequence population law, no equality of GF/GD subsequential limits, no unweighted-kernel reconstruction through vanishing controls, no full-sequence almost-everywhere convergence, and no expected-energy conclusion over bad initialization events. The chapter's final scope does not upgrade these claims.

The interior Part IV proof was not read in full and is not independently certified here.

### 6.3 Finite-controls Sections 10–11

The mixed-activation model is genuinely different from the arctangent compactness model: its first derivative is supported on [-R,R], and its top activation is z+epsilon arctan(z). It covers fixed interior correlations only.

Section 10 derives its own finite flow, kernel, energy identity, saturated-row Gram floor, readout/hidden balance, and actual loss-margin event. It retains the small random readout and states fitting only on the explicit event at sufficiently large width. Outside that event, global finite existence is the conclusion.

Section 11 retains that model and augments the event with Gaussian strips. The all-time subsets can depend on the trajectory but do not modify the optimizer. Its counterexample shows why the extra event cannot be deleted. Permanent gate mass is not identified with a lower bound on residual, reverse query, velocity, or trained nonaffinity.

The older projection's sufficient cap is C(S)sqrt(n), with equality of feature trajectories on [0,S]; choosing S=S_dagger gives all physical times at fixed width. This is not the fixed-cap clipped population flow in the arctangent chapter. The guide and chapter scope keep those auxiliary constructions separate.

## 7. Crossreferences and source/reproduction boundary

The supplied checker traversed 23 Markdown/Python files inside docs/ and code/, checked local file dependencies and import syntax, and passed. It expressly is a structural checker rather than a mathematical proof verifier.

Supplemental read-only scans found:

- no duplicate explicit equation tags within a Markdown file;
- no duplicate explicit HTML anchors;
- every actual fragment link resolves to an explicit anchor, including the finite-controls link to the local L3 arctangent model;
- no unresolved equation-number candidates in the new EC8–EC11 or Part V namespaces;
- Gaussian numbered candidates not matching equation tags were existing section references, including 5.1, 5.3, 5.5, 7.1–7.2 and 8.1–8.7;
- no local dependency on studies/history/reviews, another project path, an external generated artifact, or a missing coefficient file in the inspected dependency paths.

These scans do not establish that every prose reference in every unread proof has the correct mathematical meaning. Meaning and hypothesis matching were checked for the interfaces and passages described above.

The guide's five external primary-source links are labeled contextual rather than proof dependencies. Their existence, contents and bibliographic comparisons were not externally checked because network access was expressly out of scope. That unperformed external check is not a required assembly correction.

The package depends on NumPy and the Python standard library. The standalone rational modules use only standard-library arithmetic, but importing the pde package also imports NumPy; code/README.md correctly discloses this. The mathematical library is therefore self-contained in its source/proof-dependency sense, not a claim of a Python runtime with no installed dependencies.

## 8. Small check and certificate reproduction

Executed from the sole source root:

~~~sh
make check
~~~

Environment observed: Python 3.10.12, GCC 11.4.0, NumPy 1.26.4. The NumPy version matches requirements.txt. No installation was needed.

Result: exit status 0; 23 library files passed the structural checker; all 73 unit tests passed. Unittest reported 0.258 seconds.

| Test file | Tests | What the suite contributes |
|---|---:|---|
| test_exact_calculus.py | 7 | Rational reversion in both directions, independent permutation determinants, forest keys, regenerated certificate and independent witness arithmetic |
| test_finite_jets.py | 14 | Physical-flow coefficients, hand-solvable flows, moving-RHS differences, normalization, degree budget and ownership |
| test_finite_network.py | 15 | Initialization scales/draw order, all parameter gradients, independently differenced output Jacobians, kernels, dissipation, simultaneous GD and validation |
| test_gaussian_moments.py | 11 | Known exact Gaussian moments, singular/zero/negative-correlation cases, rational PSD validation and call isolation |
| test_library_boundary.py | 5 | Missing links/imports, permitted relative modules, math lookalikes and symlink rejection |
| test_numerical_contract.py | 21 | Selected float64 range/scaling, callback ownership, representability, derivative and update checks |

The exact certificate was regenerated by the test suite, including both negative quantities:

\[
-\frac{86245462994269879146938487857152}
{200150589172828762588730609071155193161975},
\qquad
-\frac{673792679642733430835456936384}
{329714727520793070279653295504327135}.
\]

The code guide supplies this complete standalone reproduction command:

~~~sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 python -B -c 'from pde.exact_calculus import quadratic_axis_certificate; c = quadratic_axis_certificate(); print(c["shifted_determinant"]); print(c["witness_value"])'
~~~

That command's import and returned dictionary keys were checked against the implementation. It was not separately rerun: make check already regenerated and checked its outputs. No standalone examples, training panels or additional numerical experiments were executed.

Tests validate their finite numerical and exact-arithmetic contracts. They do not establish the population convergence proofs, implement the general Section 8 compiler, validate every extreme-range floating operation, or certify unread mathematical arguments.

## 9. Required corrections and disposition

No required corrections were identified in the requested assembly/integration audit.

The source tree is unchanged. The release-facing guide, notation contract, inspected theorem/model statements, full requested additions, and implementation/reproduction guide are consistent at the scopes recorded here. The remaining unread proof material is explicitly outside this verdict, rather than implicitly certified by the successful small check.


## Appendix A. Exact substantive-read ledger and source hashes

Line numbers below are one-based and inclusive. FULL means every line of the file was read; SELECTED means only the listed passages were read substantively. The ledger merges adjacent or overlapping read chunks. Whole-file hashing and structural scanning do not count as reading the remaining proofs.

| Source file | Total lines | Read status | Exact lines read |
|---|---:|---|---|
| [Makefile](/tmp/pde-incorporated-library-round2.GAhQOu8u/Makefile:1) | 9 | FULL | 1–9 |
| [code/README.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/README.md:1) | 271 | FULL | 1–271 |
| [code/pde/__init__.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/pde/__init__.py:1) | 26 | FULL | 1–26 |
| [code/pde/exact_calculus.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/pde/exact_calculus.py:1) | 191 | FULL | 1–191 |
| [code/pde/finite_jets.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/pde/finite_jets.py:1) | 176 | FULL | 1–176 |
| [code/pde/finite_network.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/pde/finite_network.py:1) | 363 | FULL | 1–363 |
| [code/pde/gaussian_moments.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/pde/gaussian_moments.py:1) | 114 | FULL | 1–114 |
| [code/tests/test_exact_calculus.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_exact_calculus.py:1) | 122 | FULL | 1–122 |
| [code/tests/test_finite_jets.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_finite_jets.py:1) | 296 | FULL | 1–296 |
| [code/tests/test_finite_network.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_finite_network.py:1) | 297 | FULL | 1–297 |
| [code/tests/test_gaussian_moments.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_gaussian_moments.py:1) | 110 | FULL | 1–110 |
| [code/tests/test_library_boundary.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_library_boundary.py:1) | 58 | FULL | 1–58 |
| [code/tests/test_numerical_contract.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tests/test_numerical_contract.py:1) | 202 | FULL | 1–202 |
| [code/tools/check_library.py](/tmp/pde-incorporated-library-round2.GAhQOu8u/code/tools/check_library.py:1) | 100 | FULL | 1–100 |
| [docs/NOTATION.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/NOTATION.md:1) | 98 | FULL | 1–98 |
| [docs/README.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/README.md:1) | 264 | FULL | 1–264 |
| [docs/arctan_limits.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/arctan_limits.md:1) | 3117 | SELECTED | 1–128; 690–904; 1306–1484 |
| [docs/continuous_depth.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/continuous_depth.md:1) | 1490 | SELECTED | 1–154; 329–391; 1474–1490 |
| [docs/finite_dynamics.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/finite_dynamics.md:1) | 214 | FULL | 1–214 |
| [docs/finite_optimization_and_controls.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/finite_optimization_and_controls.md:1) | 1735 | SELECTED | 1–102; 190–255; 334–378; 642–700; 748–824; 958–995; 1039–1069; 1071–1146; 1209–1735 |
| [docs/gaussian_calculus.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/gaussian_calculus.md:1) | 3296 | SELECTED | 1–12; 196–528; 636–762; 1722–3296 |
| [docs/global_nonlinear.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/global_nonlinear.md:1) | 1796 | SELECTED | 1–180 |
| [docs/linear_dynamics.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/linear_dynamics.md:1) | 2641 | SELECTED | 1–557; 735–815; 908–1017; 1248–2641 |
| [docs/special_data_limits.md](/tmp/pde-incorporated-library-round2.GAhQOu8u/docs/special_data_limits.md:1) | 9362 | SELECTED | 1–368; 2095–2152; 3507–3841; 4072–4168; 6020–6664; 7936–9362 |
| [requirements.txt](/tmp/pde-incorporated-library-round2.GAhQOu8u/requirements.txt:1) | 2 | FULL | 1–2 |

Whole-file SHA-256 manifest, identical at the initial and final source checks:

~~~text
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
b563a8a4fcebbb5fb634057f6cf09d32475462670002c8fbad0502f5c06482e0  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41  code/pde/exact_calculus.py
1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2  code/pde/finite_jets.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439  code/tests/test_exact_calculus.py
991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a  code/tests/test_finite_jets.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
3d045c2a61847d0f78ae08137da7e0d0ad6252eb2734bf0bef75fcf7641fd592  docs/README.md
19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  docs/arctan_limits.md
0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362  docs/continuous_depth.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
cca2df017ad2dffc6c5c6919da720bac34451b8aecca2415b3bb788d18744230  docs/finite_optimization_and_controls.md
9676106aa203f8f3939b794429a945ac1c55a127fa230c94fde0672268eee56d  docs/gaussian_calculus.md
becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95  docs/global_nonlinear.md
c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090  docs/linear_dynamics.md
be4573af77f32d53913b1a50f0eb6e003f54bbf7571db95951d47ebc6c65719a  docs/special_data_limits.md
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
~~~

## Appendix B. Exact selected-passage hashes

Each digest below is SHA-256 of the literal source bytes belonging to the stated inclusive line range, including the original line terminators. No whitespace, encoding, or mathematical-text normalization was applied. For fully read files, the whole-file digest in Appendix A is also the full-passage digest.

### docs/arctan_limits.md

~~~text
1-128  a3cac0d2f9b490800d53d2c2163fc9df0afb74ab1ad1218e38c19bdc00ecdaa7
690-904  deff0a42a1fea762c9c2703f97e3cc7d1bc473dd3654f0e740da7a6e209adbec
1306-1484  84f742a782e3fc631e7f516b9bcc2255e050fd6764642da72ef8ac60628106b3
~~~

### docs/continuous_depth.md

~~~text
1-154  baf34db7e03b85d42ecfe26886755d5240ebd0650f9b418ff6b2f5601e67cb57
329-391  130d1e66d20e70e95584770c03811bd5e1263c945e8085d010b6b85beec651f6
1474-1490  70db6a1ef819cd98932e1f75bf862b6100e5f53bc3aded3ab851b8fc9ed84287
~~~

### docs/finite_optimization_and_controls.md

~~~text
1-102  5fbc718dc14e2236c00826e7d24126e74ab179b71887e524046f7bef579519c1
190-255  45bd240b8ae65ee5063cd816ab120bccb079f98019108ad3e120338b736d6d1f
334-378  a2eef02f5c5368a63f470b363e1bc19343fed2d611fb0e7b6e484500f157fed8
642-700  7aa489d17c0b8fa0b78fae6628c01e8b6c7d0a6b46c1fd0827b2e342c50edf0c
748-824  ac89f4514961180ca2404f067f0b3c7ff5eb45383b63e43842b98421aa1441b8
958-995  9efea7cbcd0b30e750ac42444916c92b290434c47e53cc0dcaec517a2a97d44f
1039-1069  01b72beb471d8680aadbb413af0847bb79ed0c7fe2eafa6e668500544854dffe
1071-1146  6ef1686a90dffd8e402dc18bcbcb58d2595c332a4b93f5a83d15cffcada91214
1209-1735  b4fc2902795bfcd732e7b01635890752838ab24bfcd0be26924ffa22cf168677
~~~

### docs/gaussian_calculus.md

~~~text
1-12  c0fb72b8024544c4cf221f0114e2315fd0232b5804315dc1c721d171dcada330
196-528  80f340a9f8062f8be77fe365a914777455e91582c8dd8e4727204a16bcb8523d
636-762  a29faf6139f48c4c17f7a7d8a4e4a716afce704abfb97dfded6b158dafceda81
1722-3296  c404e8b096f2b70cceb8c50d9f39bcbf4f5934c86ac4b8c8219b29a04563cdf7
~~~

### docs/global_nonlinear.md

~~~text
1-180  8050041d1b3ee400857937422200c17e109b03c89eb5371ea8e74653bb665843
~~~

### docs/linear_dynamics.md

~~~text
1-557  3d876d01d5d4fd752a52953db0da9a0dc2ecebaa6b9d184c5452a147817fe199
735-815  ac8ade9896e33b5a6ac9da9817e549827e41504889fd0b288292529286732410
908-1017  3b12c2dd0d73f93f0b96fcbae373fb1e5e269043d8eead13fd23cb3860b9cb9a
1248-2641  04f8eb23c305b136a7a0f2bc4069181dbe0dd85e11b8eff99d6c6749af35ef53
~~~

### docs/special_data_limits.md

~~~text
1-368  e3e43265d129226b2041e41fdabd22267a0e1a6d0a9cb1381ea4dc3d7cace041
2095-2152  03458b91919e56bdd6ad6c21c6c21cb5217906e1daba0a04163d1ede6d8db873
3507-3841  d74366016de870198755ce1741d6f1596de9aac6297bcf2014a0325c7a70361e
4072-4168  30d22ed5a041d1010d6da5db29473b6efb18e8eaa4bc54219bf8a5625608ae7b
6020-6664  8bfee0fdc0dea36cae16efe35835a1565f97670f97cf450af312cec68bc1a1d9
7936-9362  72e3beaf960816f5089d9aa01d71927d085a082f867290b075015d78239199d2
~~~

## Appendix C. Substantively unread source ranges

The following are the exact complements of the selected-read ledger. Some received keyword, heading, link, or label scans; none is represented as fully read or independently proof-verified. Files marked FULL in Appendix A have no unread range.

| Source file | Substantively unread inclusive ranges |
|---|---|
| docs/arctan_limits.md | 129–689; 905–1305; 1485–3117 |
| docs/continuous_depth.md | 155–328; 392–1473 |
| docs/finite_optimization_and_controls.md | 103–189; 256–333; 379–641; 701–747; 825–957; 996–1038; 1070–1070; 1147–1208 |
| docs/gaussian_calculus.md | 13–195; 529–635; 763–1721 |
| docs/global_nonlinear.md | 181–1796 |
| docs/linear_dynamics.md | 558–734; 816–907; 1018–1247 |
| docs/special_data_limits.md | 369–2094; 2153–3506; 3842–4071; 4169–6019; 6665–7935 |

End of scoped final assembly/integration audit. No required correction was found; no input was changed.
