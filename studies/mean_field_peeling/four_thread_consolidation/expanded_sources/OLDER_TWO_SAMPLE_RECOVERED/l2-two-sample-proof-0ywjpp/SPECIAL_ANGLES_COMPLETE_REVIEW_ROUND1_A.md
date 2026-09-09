# Independent adversarial full-document review — Round 1 A

## Verdict

**PASS, for precisely the special-angle theorem stated in Section 1.3.**

I found no mathematical gap requiring correction in the complete document. In particular, the Gaussian conditioning argument uses the same matrix in both orientations; the singular-Gram passage preserves the prescribed formal expressions; the operator construction supplies one bounded operator and its actual adjoint; and the fresh-root argument establishes the expected-response bounds needed for the bounded Gaussian remainders. The subsequent convergence and nontriviality arguments do not assume those conclusions in order to prove their premises.

This verdict covers both and only `rho = 0` and `rho = -1`, both hidden widths equal to `n`, the displayed arctangent model, the loss-SUM parameter metric, the prescribed physical step `eta_n = n^{-2}`, and each fixed finite time horizon. It does not certify other correlations, arbitrary matrix directions, an operator-norm limit of matrices of growing dimension, a Hilbert–Schmidt initial operator, a limit uniform over unbounded time, or a newly sampled operator at restart. Those stronger statements are not asserted by the document.

**Required mathematical corrections: none.** Optional clarifications are listed separately below; they do not supply missing hypotheses or rescue invalid arguments.

## Isolation, source integrity, and method

- Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`.
- Source length: 1,935 lines, 91,679 bytes. I read all lines 1–1935 before forming a verdict, including the statement, all proofs, the limitations, and the provenance paragraph.
- Requested and observed SHA-256 before reading: `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`.
- Observed SHA-256 after the complete audit and review-file write: `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`, identical to the requested and initial hashes.
- The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely. It guided hypothesis checking, normalization checks, limit-order checks, and the distinction between an actual gap and an optional expansion of an already justified step.
- No other mathematical documents, project directories, proof snapshots, prior reviews, history, agents, or mathematical references were accessed. The filenames at source lines 1920–1935 were treated only as text in the permitted source; their targets were not opened.
- No experiments, simulations, numerical tests, or agents were used. The audit below consists of symbolic re-derivations and checks of the logical dependencies.
- No heavy external theorem is used as an unproved premise in the source. There was therefore no external theorem or dependency to retrieve, and no external-source access blocker.

All line and equation references below refer to the reviewed source, not to this review.

## Scope and obligation ledger

| Stated obligation | Location | Audit result and supporting argument |
| --- | --- | --- |
| Correct finite initialization, gradients, metric, and clock | Lines 12–86; (1)–(7) | Verified. The inverse metric produces exactly the three updates in (6). The finite Gaussian readout is not silently replaced in the asserted algorithm. |
| Separate neuron spaces and correct rank/operator normalizations | Lines 88–144; (8)–(11) | Verified. The rank is `v h^T/n`, its Hilbert–Schmidt norm is the ordinary Frobenius norm, and the adjoint of the ordinary matrix action is its transpose. |
| One canonical operator, bounded by 8, with genuine adjoint | Lines 146–152, 949–1018; (55) | Verified through simultaneous limits of forward and reverse queries, norm inequalities, zero-relation preservation, density, and the limiting pairing identity. |
| Global autonomous flow and uniqueness from reached states | Lines 146–152, 233–448; (15)–(27) | Verified in the transformed coordinates and then for the original integral-equation class. Restart retains the complete state and its unchanged initial operator. |
| Deterministic full-sequence finite-width law for GF and raw GD | Lines 149–162, 637–947, 1298–1451 | Verified. Fixed-program identification is a full-sequence result; fixed-mesh comparisons then avoid any width-subsequence selection. Raw GD is separately compared with GF with the same actual initialization. |
| Joint same-neuron path laws in every finite Wasserstein order | Lines 154–166, 1356–1372, 1439–1447; (72), (74) | Verified. Finite-grid convergence plus derivative-energy control gives path order 2; supremum moment bounds give every fixed higher order. No pairing between different populations is needed. |
| Uniform predictions, loss, and all three kernel blocks | Lines 168–179, 1374–1381; (12) | Verified. Block 1 uses a bounded-gate/product truncation argument with uniform integrability; blocks 2 and 3 use the simpler Lipschitz estimates. |
| Both orientations for every fixed admissible finite probe and its stipulated L2 limits | Lines 179–192, 1298–1354, 1447–1449 | Verified for the stated finite-program scope. Subsequent unbounded queries are justified by truncation and the operator bound, not by an unproved Lp operator bound. |
| Original hidden velocities and readout velocity | Lines 194–198, 1383–1418; (67), (73), (75) | Verified. The last multiplication in the second activation velocity receives its own noncircular uniform-integrability argument. |
| Parameter speeds, hidden-velocity energies, and increment sizes | Lines 198–209, 1420–1437; (13), (18), (24)–(25), (76) | Verified. The antiparallel first-matrix motion is counted once. The middle increment is a rank integral with a Hilbert–Schmidt norm; no initial Hilbert–Schmidt norm is claimed. |
| Strict distributional nonaffinity at every finite time | Lines 211–215, 1513–1568; (14), (81)–(83) | Verified. Both tails remain unbounded; the affine subspace is closed; a bounded strictly increasing activation cannot equal an affine function of such a variable. |
| Strict positivity of every asserted positive-time speed | Lines 217–219, 1570–1666; (84)–(90) | Verified. Progress makes the readout and deltas nonzero; reverse Gaussian tails make the first motions nonzero; the adjoint identity and exchange law rule out cancellation of second-layer motions. |
| Vanishing population hidden speeds at initialization | Lines 219, 1590, 1665–1666 | Verified. The limiting readout is zero. This is a population statement, not an assertion that the finite Gaussian readout vanishes. |
| Positive leading change of the full kernel in physical time | Lines 220–222, 1668–1896; (91)–(107) | Verified. Both the hidden and readout blocks contribute positively at second order. The coefficient for the defined scalar label-direction kernel is exactly `32 d_*`. |
| No all-angle or long-time overclaim | Lines 1898–1935 | Verified. The off-diagonal transformed multiplier is correctly identified as the obstruction outside the two special geometries. The provenance records are not mathematical premises. |

## Complete equation and proof-step coverage ledger

### Section 1: model, spaces, and statement

| Lines / equations | Check |
| --- | --- |
| 12–35; (1)–(3) | The input normalization implies unit-variance first preactivations and covariance `C`. Orthogonality requires `d >= 2`; correlation `-1` with the prescribed equal norms forces opposite inputs. The activation derivatives are correct. |
| 36–70; (4)–(6) | Prediction carries the displayed `1/n`, while each backward field deliberately omits the residual. The three updates, dimensions, and interpolation convention are mutually consistent. |
| 72–86; (7) | Euclidean gradients each carry `2/n`. The inverse metric multiplies their blocks by `n/d`, `1`, and `n`, giving precisely `2/d`, `2/n`, and `2` in the physical vector field. |
| 88–114; (8)–(9) | For equal normalized domain and range inner products, the matrix adjoint is the transpose. A normalized orthonormal basis is `sqrt(n) e_j`, so the Hilbert–Schmidt norm of a matrix is its ordinary Frobenius norm. Both rank-one norm equalities follow. |
| 116–144; (10)–(11) | The field types and pointwise products agree with the two spaces. Multiplication of the first-row equation by `x_a` gives the displayed `C_ab` factor. The rank update contains its required finite normalization through (9). |
| 146–229; (12)–(14) | Every advertised conclusion was included in the obligation ledger. The three kernels are the parameter-gradient Grams in the stated metric. Their first block uses the input Gram as well as the backward-field Gram. |

### Section 2: deterministic flow and discretization

| Lines / equations | Check |
| --- | --- |
| 233–251; (15) | `F' = 1 + z^2`; `(F^{-1})' = phi' composed with F^{-1}`; `(phi composed with F^{-1})' = (phi')^2`. All Lipschitz and bounded-derivative assertions used here follow. `E F(G)^2 = 1 + 2 + 15/9 = 14/3`. |
| 253–260; (16) | For `C = I`, multiplication by `F'` cancels the first-layer gate exactly, leaving `dot U_a = c_a Q_a`. The other equations are unchanged. |
| 262–275; (17) | Opposite inputs, odd activations, and even derivatives give the full pathwise identities for any readout. The effective single control is `c_1-c_2 = -4r_1`, not `-2r_1`. |
| 277–288; (18) | Orthogonal input directions reconstruct the entire changing first row, with its orthogonal component unchanged. The antiparallel reduction has one independent direction and one copy of its squared speed. |
| 290–326; (19)–(20) | Each subtraction estimate follows by splitting one factor at a time, using bounded readout and bounded scalar derivatives. No step requires `Q` bounded in L-infinity or bounded matrix action on Lp for `p != 2`. |
| 328–370; (21)–(22) | Clipping supplies a locally Lipschitz vector field on an actual L2-open domain. The integral contraction proves local existence and uniqueness. The readout increment bound makes clipping inactive locally. The stability estimate follows from the scalar integral inequality. The mixed initial-operator/HS-increment comparison is legitimate. |
| 372–392; (23) | The operator increment follows by integrating `B(b_2+Bv)` in accumulated action. The U bound follows by integrating the operator bound times the readout bound. An integrable drift gives an endpoint limit, and the readout is also Cauchy in L-infinity. |
| 394–402 | The chain rule along a C1 L2 curve is proved with the fixed-direction difference quotient and square domination. This avoids an unjustified assertion of Frechet differentiability of the whole composition operator. |
| 404–431; (24)–(26) | The three parameter contributions yield `dot f = -2Kr` and the exact gradient-flow loss balance. Positive semidefiniteness is witnessed by three explicit Gram representations. Residual control gives finite action and hence global extension. For population initialization, `R_0=sqrt(2)` gives `S(t)<=4t`, and the stated operator bound is correct. |
| 433–448; (27) | Original-class uniqueness is not left conditional on assuming `F(Z)` lies in L2. The scalar chain rule after Fubini proves precisely that membership from the original integral equation and the initial Gaussian moment. The antiparallel relation is preserved. |
| 450–475; (28)–(29) | Bounded Lipschitz drift gives a local defect of order `h^2`; iteration gives the stated global estimate. The first-exit argument supplies bounds through the candidate exit update before using the comparison to rule out exit. The discrete rank bound uses the correct half coefficient. |
| 477–504; (30)–(31) | The exact cubic expansion has all coefficients correct. With `||q||_n` bounded and `||q||_infinity <= sqrt(n)||q||_n`, the defect is `O(eta^2 sqrt(n)+eta^3 n)`. Accumulation at `eta=n^{-2}` gives `O(n^{-3/2})`. The interpolation remainder and its derivative have the claimed orders. |
| 506–525; (32)–(33) | The potentially unbounded backward factor costs at most `sqrt(n)` in the finite product estimate, yielding original velocity errors `O(n^{-1})`. The second-layer product rule uses the actual evolving operator. The norm-square comparison correctly transfers these errors to energies and kernels. No discrete exact loss identity is assumed. |
| 527–547; (34)–(35) | The net has size at most `9^n`; approximating both arguments gives the factor 2 in the norm estimate. The Gaussian variance is `1/n`, giving exponent `-nt^2/8`. At `t=8` the failure probability tends to zero. Both readout union bounds have the correct variance and exponents. |

### Section 3: finite Gaussian programs, canonical operator, and response bounds

| Lines / equations | Check |
| --- | --- |
| 551–569; (36) | This is exactly the transformed Euler scheme in the two permitted geometries. Its off-invariant uses are explicitly auxiliary finite programs, so they do not assert the unavailable general-angle raw-flow identity. |
| 571–615; (37)–(39) | The causal order is correct: first features depend only on past reverse calls, current forward calls precede reverse calls, and updates come last. Learned forward/reverse rank terms have the correct inner products. Source covariances are uncentered input Grams with all times, samples, and jointly run programs retained. |
| 616–635; (40) | Formal differentiation holds selected scalar quantities fixed but differentiates the whole coordinate expression. Both terms in the derivative of the second delta are present. The current beta is diagonal in the formal sample slot; singularly correlated slots are not identified or deleted. |
| 642–660; (41) | Bounded activations give the stated readout recurrence, even for the auxiliary noisy programs. The readout-gate node can be smoothly clipped without changing program values. Storing the cubic Gaussian expression as part of the iid root tuple avoids a false globally Lipschitz root-map assumption. |
| 662–694; (42) | The Gaussian matrix parameter is unscaled `E`. A differentiated matrix action contributes `v x/sqrt(n)`, with Euclidean norm bounded by `||v||_F ||x||_n`. The contraction derivative has the necessary `n^{-1/2}`; this cancels the `sqrt(n)` in scalar-times-vector nodes. Finite graph induction therefore has dimension-free polynomial bounds. |
| 696–713; (43) | The independent Gaussian rotation has independent standard Gaussian velocity. Integral Holder and conditional Gaussian integration give the displayed constant, and Jensen centers at the mean. Integrated (34) supplies all matrix-norm moments. |
| 715–740; (44)–(45) | Permutation equivariance controls conditional coordinate means using the local root entries, not a spurious coordinate bound from normalized RMS alone. Together with (43), polynomial root-norm moments, and Holder, it proves all fixed-program coordinate moments. |
| 742–759; (46) | Verified by Gaussian orthogonal projection onto the accumulated linear matrix constraints. The mean satisfies both observations using `J^T Y=P^T V`. The residual is the common orthogonal null component. Adaptivity is handled sequentially after queries become measurable from earlier answers. |
| 761–782; (47) | Applying (46) to the new orthogonal input gives the stated regression coefficients and innovation variance. The removed finite-rank projection has empirical p-moment at most a constant times rank divided by `n`, since each projection diagonal lies in `[0,1]`. |
| 784–804; (48)–(49) | Conditional concentration uses independent innovation coordinates only after projection removal. Gaussian-integrated continuous tests remain continuous with controlled growth on bounded parameter events. Higher moments justify both truncation and replacing the negligible projection. |
| 806–848; (50)–(51) | Re-derived below. Integration by parts cancels the old forward regression contributions and produces the expected formal derivatives. The innovation and old source projection have combined variance `E h^2`. The reverse argument uses the same matrix, not a fresh matrix. |
| 850–880; (52)–(53) | Every new query-input perturbation has its own fresh root, yielding limiting Schur complement at least `epsilon^2`. Coupled graph subtraction gives an L2 error of order epsilon times a polynomial with uniform moments. Interpolation with a higher moment extends this to every fixed finite order. |
| 882–913 | The inverse-free response formula has continuous coefficients and bounded continuous formal first derivatives on compact coefficient sets. Covariance square roots remain continuous at rank loss. Dominated convergence and the finite-width coupling establish the singular theorem without a pseudoinverse continuity assumption. Null response directions contract to zero, while formal slots are retained. |
| 915–937; (54) | The learned rank identities are exact in both orientations. Causal expectation selection gives a deterministic-coefficient program; empirical-feedback errors then vanish by finite graph subtraction. The resulting coefficients are exactly (38). |
| 939–947 | The finite-dimensional Wasserstein upgrade is justified by matching empirical and limiting mass in small cells, with higher moments controlling the unmatched tails. |
| 949–992; (55) | Countable jointly run programs cover the required dense query family. Limits of finite norm inequalities and the exact transpose pairing define bounded linear maps. Zero-norm input relations imply zero-norm output relations, so this is a well-defined operator construction, not just a list of field laws. |
| 994–1018 | Cylinder approximation supplies density in the generated L2 spaces, including in the presence of atoms. Both maps extend continuously; the pairing identity makes the reverse extension the genuine adjoint. Finite-program marginal consistency gives canonicity on the generated spaces, modulo null sets. |
| 1020–1033; (56) | Section 2 is applied only after the common operator and spaces exist. All included mesh programs solve their Euler equations for that same operator. Deterministic stability thus gives a common-space strong L2/HS comparison. |
| 1035–1057; (57) | The exponential readout bound and summed-control bound depend only on the finite horizon. The rank bound then controls the operator in the forced programs. The two-coordinate auxiliary update is stable even when a forced query breaks a sample identity. |
| 1059–1084; (58)–(59) | Reverse forcing affects the next state only through an `h_s`-weighted first-coordinate update. Forward forcing changes current outputs and residuals, but all state changes still carry `h_s`. Current-node delta changes are correctly treated separately. Later Lipschitz factors multiply to a horizon-dependent constant. |
| 1086–1128; (60)–(61) | At fixed nonzero forcing, the joint finite-program limit makes the fresh local root enter through the designated shifted source slot. Local Gaussian integration by parts therefore extracts the expected frozen derivative. Finite feedback is included before taking the width limit. Only afterward is forcing sent to zero using fixed-program continuity. This also covers zero-variance initial slots. |
| 1130–1138; (62) | The learned rank coefficients add only `O(h_s)` past terms because features and deltas are bounded. Current terms have the separate displayed bound. Absolute response row sums are uniformly bounded as the mesh is refined. |
| 1140–1161; (63)–(64) | Response row bounds times bounded features/deltas give actual essentially bounded remainders. The U correction is a deterministic linear combination of reverse Gaussian sources plus a bounded remainder. Gaussian variances are uniformly bounded, and the Gaussian correction is independent of the first-row roots. |
| 1163–1200; (65)–(66) | Cross-program covariances make both source assignments Gaussian isometries. Strong convergence of query inputs therefore gives strong convergence of sources on the common spaces. Subtracting sources passes the bounded remainders to the flow. Riemann sums converge in L2; Gaussianity and root independence persist. Joint measurability/Fubini suffice for the integrals. |

### Section 4: observable convergence, paths, velocities, and energies

| Lines / equations | Check |
| --- | --- |
| 1204–1220; (67) | The bounded-gate product inequality is correct. It invokes uniform integrability for the unbounded factor rather than incorrectly asserting a globally Lipschitz multiplication map on L2. Its fixed-field version proves continuity along the population paths. |
| 1222–1237; (68) | Radial truncation to operator norm 8 is 2-Lipschitz in operator norm. Its dependence on unscaled Gaussian entries is therefore at most `2/sqrt(n)` in Frobenius norm. It is used for moment estimates and is absent with probability tending to one. |
| 1239–1250; (69) | Deterministic transformed-state stability controls all listed base fields uniformly in time. Converting one coordinate from normalized RMS cancels the `1/sqrt(n)` parameter scale, giving dimension-free Lipschitz constants for coordinate path suprema. |
| 1252–1271; (70)–(71) | The pointwise integral inequality and Minkowski give the RMS bound on coordinate suprema. Differentiating delta2 and Q introduces only bounded multipliers and L2 operator actions. No derivative of delta1 with an uncontrolled Q-product is needed here. |
| 1273–1296; (72) | Gaussian concentration conditional on stored roots, followed by the permutation conditional-mean bound, gives every finite path-supremum moment for the truncated-matrix model. The same estimates hold for Euler and clipped initial readout. High-probability equality with the original model supplies the required uniform integrability in probability. |
| 1298–1320; (73) | Delta1 is first a polynomial-growth observable. Before using its single- or double-gated version as a new query, Q is smoothly truncated. The input error vanishes in ordinary L2, and the operator bound transfers it. All four displayed velocity identities and antiparallel signs are correct. |
| 1322–1345 | The finite-flow/fixed-mesh/population-flow triangle proves full-sequence convergence at finite observation lists. Restoring the actual Gaussian readout uses stability with its initial L2 norm tending to zero and a high-probability essential bound. |
| 1347–1354 | General admissible probes are appended to the same finite graph. The stipulated L2 approximation property, not an arbitrary-direction claim, extends the result to the admitted limits of probes. |
| 1356–1372; (74) | Cauchy–Schwarz on observation-grid intervals bounds the path interpolation error by derivative energy times the grid spacing. Averaging gives the transport bound. The delta1 path product is continuous and dominated by the Q path norm. Higher supremum moments upgrade the order. |
| 1374–1381 | Uniform scalar convergence follows from the state/product estimates, finitely many fixed-mesh contractions, and their time modulus. Both parts of the time/width comparison are controlled. |
| 1383–1394 | First velocities use Q-square uniform integrability. The second preactivation comparison is completed before the final activation gate is applied; its L2 estimate uses only the bounded operator and the already controlled first activation velocity. |
| 1396–1418; (75) | Re-derived below. Fixed-mesh W2 convergence yields tail control for finitely many second-preactivation velocity evaluations. The displayed inequality and the uniform approximation transfer this to finite GF, then (67) justifies the final gate. This is not circular. |
| 1420–1437; (76) | The middle squared parameter speed has coefficient 4 and two uncentered Gram factors. Time integrals follow from uniform quadratic convergence. Operator increment norms use cross-time Gram contractions of finite rank sums, with an HS Riemann approximation. |
| 1439–1451 | Raw-GD transfer is justified for paths as well as fixed times: the `O(n^{-3/2})` normalized base-field error gives `O(n^{-1})` maximal coordinate error. Delta1 incurs the finite product loss but still has vanishing maximal coordinate error. The verified probe approximations transfer too. |

### Section 5: symmetry, nonlinearity, positive motion, and kernel change

| Lines / equations | Check |
| --- | --- |
| 1455–1494; (77)–(79) | Equal input norms give the displayed reflection. The transformation swaps forward sample fields and flips the readout, residuals, and backward fields with the stated signs. It preserves the metric and commutes with GF and raw GD. Both actual Gaussian and auxiliary zero-readout initialization laws are invariant. |
| 1496–1511; (80) | Deterministic population limits transfer finite distributional symmetry into equalities of predictions and velocity norms. The orthogonal case is correctly treated as a law symmetry; only the antiparallel case has the stronger pathwise identities. |
| 1513–1544; (81)–(82) | Root-independent Gaussian integrals plus bounded remainders leave both first-layer tails unbounded. In the orthogonal case, independent first roots allow all four large-sign patterns, forcing the feature Gram to be positive definite. In the antiparallel case the full Gram remains rank one and is not inverted. |
| 1546–1568; (83), (14) | Positive first-feature variance makes each second Gaussian source nondegenerate. Its bounded remainder cannot remove either tail, even if dependent on the source. The explicit closed-affine-span argument proves a strictly positive approximation error, not merely the absence of a displayed affine identity. |
| 1570–1602; (84)–(87) | With `r=(f_1-1)y`, the prediction equation gives the scalar coefficient 4 and the stated exponential formula. Initial second-layer covariances are `mI` or the reduced variance `m`; the initial contrast variance is positive. Monotonicity then gives `0<f_1(t)<1` for every positive finite time. |
| 1604–1615; (88) | Nonzero readout and strictly positive gates make every delta2 nonzero. The reverse Gaussian source consequently has positive variance, and bounded remainder gives nonzero Q. Both permitted first-coordinate controls are nonzero, so every first preactivation and activation speed is positive. |
| 1617–1630; (89) | Positive definiteness of the orthogonal first-feature Gram applies pointwise to the signed delta vector and gives the lower bound. The antiparallel rank-one velocity is also nonzero. |
| 1632–1666; (90) | Expanding the second preactivation derivative and using the actual adjoint gives the sum of middle-parameter and independent first-coordinate squared speeds. This rules out simultaneous vanishing; exchange symmetry makes both second preactivation speeds positive. Positive gates handle activations. A vanishing readout velocity would contradict `f_1>0`. |
| 1668–1697; (91)–(93) | The initial readout coefficient is the half contrast. The reused-transpose return contains its nonzero response to first features plus a centered Gaussian with the full delta second moment. The antiparallel calculation uses one independent column. |
| 1699–1744; (94) | Conditional row projection and transposition produce exactly the `Gamma_n^{-1}` coefficient and the residual covariance `Sigma_n`. Finite-rank projection removal is justified in every finite moment. The reduced limiting Gram is strictly positive, so this local inverse has valid hypotheses. |
| 1746–1764; (95) | Each delta variance is positive. In the orthogonal case, varying the two initial Gaussian coordinates proves positive definiteness of their covariance. Conditional Gaussian variance given the first row, followed by multiplication by a strictly positive gate, proves the displayed positive norm. |
| 1766–1783; (96)–(97) | Feature time has derivative `4(1-f_1)` and satisfies `s=4t+o(t)`. The orthogonal feature equations have coefficient one-half; the antiparallel reduction has coefficient one. This time change is only used to analyze the local expansion. |
| 1785–1796; (98) | The integral readout equation gives its strong first-order limit. Bounded gates and operator-norm continuity transfer it to delta and Q. The proof uses strong convergence along curves, not an unproved second Frechet derivative on L2. |
| 1798–1838; (99)–(102) | All three leading velocity coefficients follow from the initial feature Gram `mI` and the product rule. Rank-one norms give the displayed expression for `d_*`. Moving the initial operator through its genuine adjoint gives (102) with coefficient one-half. |
| 1841–1855; (103) | The single-coordinate antiparallel coefficients are the correct reductions; no hidden double counting remains. The inner-product identity equals `d_*`. |
| 1857–1885; (104)–(106) | The hidden label-direction kernel equals the squared feature-time hidden speed, hence contributes `d_* s^2`. The derivative of the readout contrast norm divided by `s` tends to `2d_*`, hence the readout contributes another `d_* s^2`. |
| 1887–1896; (107) | Since `s^2=16t^2+o(t^2)`, the full scalar label-direction change is `32d_* t^2+o(t^2)`. Its coefficient is strictly positive. |
| 1898–1935 | The proof record is consistent with the dependency checks. The general-angle off-diagonal ratio is the correct transformed factor and is not generally a bounded L2 multiplier. No result from the provenance filenames is imported. |

## Detailed adversarial checks of the highest-risk arguments

### 1. Reuse conditioning and the response formula

For fixed old constraints `WV=Y` and `W^T J=P`, let `P_V` and `P_J` denote the two Euclidean orthogonal projections. The proposed mean is

\[
M=Y(V^TV)^{-1}V^T+J(J^TJ)^{-1}P^TP_{V^\perp}.
\]

It satisfies `MV=Y`. Also

\[
M^TJ=P_VP+P_{V^\perp}P=P,
\]

where the first equality uses `Y^TJ=V^TP`. The remaining Gaussian component has precisely the form `P_{J^perp} tilde W P_{V^perp}`. Thus (46) is the conditional law for the same original matrix subject to both orientations of observations. There is no missing constraint and no replacement by an independent transpose.

For a new input, write `h=V lambda+h_perp`. The non-forward part of the conditional mean is

\[
J(J^TJ/n)^{-1}(P^Th_\perp/n).
\]

At the limiting scalar level, old reverse answers are Gaussian reverse sources plus responses in the old forward-input span. The latter disappear upon pairing with `h_perp`. Consequently

\[
\nu=\Gamma_v^{-1}\mathbb E[\zeta h_\perp]
=\mathbb E\nabla_\zeta h-
\sum_r\lambda_r\mathbb E\nabla_\zeta h_r.
\]

Substituting the old forward-answer decompositions cancels the second term. This gives exactly (50). No extra variance subtraction is appropriate: the new source consists of the old forward-source projection and an orthogonal Gaussian innovation, with total variance

\[
\|V\lambda\|_{L^2}^2+\|h_\perp\|_{L^2}^2=\|h\|_{L^2}^2.
\]

The source-source cross-covariances are similarly the full input inner products. This is the reason the reused-transpose covariance in (92)–(94) is the full delta second moment.

The finite-rank residual projection is not simply declared irrelevant. Equation (47) controls its empirical p-moment by `rank/n`, and the moment/truncation argument handles continuous tests after its removal. This resolves the dependence among the original finite coordinates without falsely asserting their independence.

### 2. Singular Grams, frozen formal derivatives, and initialization

The unperturbed initial reverse query is identically zero, and at the antiparallel geometry there are redundant sample queries. Inverting those unperturbed Grams would invalidate the proof. The source does not do so.

The perturbation in lines 850–858 is to each initial-matrix query input and uses a fresh root for that particular call. Conditional on the old inputs, the new independent coordinate contribution has variance `epsilon^2`; its component cannot be represented by the previous same-direction input span. Fixed positive epsilon therefore permits the nonsingular induction. Finite-width perturbation errors are then controlled directly with the same actual matrix, independently of any conditioning inverse.

On the scalar side, (50) is an inverse-free formula. At fixed program length, the coordinate expressions and their frozen first derivatives are continuous in their deterministic coefficients and Gaussian covariance parameters. The positive semidefinite covariance square-root argument works at rank loss. The passage to zero perturbation therefore identifies the prescribed formal-expression law, including the zero-variance slots.

The null-space observation at lines 907–913 is correctly limited: a derivative ambiguity in a null covariance direction disappears only after contraction with the corresponding reverse-input family. It is not used to claim that arbitrary transverse derivatives are determined by a singular distribution. The actual formal convention is supplied earlier, and continuity of perturbed finite programs justifies its use.

At a node, the derivative of `delta2 = W3 phi'(Z2)` has the two terms in (40). Omitting the past readout derivative would change the response. Conversely, differentiating selected expectations or feedback coefficients as functions of a single local Gaussian coordinate would introduce spurious terms. The document makes neither mistake. The diagonal current beta follows because the current own source enters `Z2_ka` additively, current other sample slots remain formally separate, and the readout depends only on earlier activations.

### 3. One operator and its genuine adjoint

An abstract field recursion would not alone justify energy identities, unbounded-query limits, or restart. Lines 949–1018 supply the additional construction.

For every finite rational combination of inputs, finite-width linearity and the high-probability norm bound pass to deterministic limiting second moments. In particular,

\[
\left\|\sum_i t_i h_i\right\|_2=0
\quad\Longrightarrow\quad
\left\|\sum_i t_i a(h_i)\right\|_2=0.
\]

Thus the proposed action is well defined on L2 equivalence classes, not dependent on the presentation of a query. The same argument works in reverse. The finite exact pairing identity passes to the joint limit. Density of the smooth cylinder-query span then extends both actions to the full generated L2 spaces, and the pairing identifies the reverse extension with the Hilbert adjoint.

The countable closure is important: applying the orientations to generated fields and including a dense collection of cylinder inputs prevents the argument from stopping at an inadequate finite span. Threshold approximation does not require atomless coordinate laws; one-sided smooth approximations handle atoms. Different enumerations preserve all common finite-program laws, so the canonical state is determined on the generated spaces up to the indicated measure-space/L2 identifications.

The resulting norm bound is 8. No convergence of finite matrix operator norms to this particular operator is claimed. Its learned increments, rather than its initialization, are Hilbert–Schmidt. All later uses of an adjoint, including (24), (90), and (102), therefore refer to a genuine bounded-operator adjoint.

### 4. Expected responses from fresh-root forcing

This is the principal nontrivial bridge from deterministic stability to the Gaussian-remainder theorem. I checked it separately from the singular-query regularization.

If one complete reverse answer receives `epsilon e` at node `s`, the immediate state discrepancy is confined to an `h_s`-weighted U update. If one complete forward answer receives that forcing, the current activation, delta, prediction, and residual may all change by order `|epsilon| ||e||_n`, but every resulting state update still carries `h_s`. The actual current transpose has bounded L2 operator norm and controls the backward discrepancy. Future state discrepancies grow by at most the product of `1+C_T h_k`. Thus the estimates (58)–(59) genuinely concern the finite empirical-feedback program, with constants uniform over partitions of the fixed horizon.

For a fixed mesh and nonzero epsilon, apply the already proved finite-program theorem to the forced run, the unforced run, and the additional root. In the local population of the forcing, the Gaussian sources are independent of this root. With epsilon fixed, selected scalar coefficients are deterministic. The local expression therefore has

\[
\partial_eX^\epsilon=
\epsilon\,\partial_{\rm slot}X^\epsilon,
\qquad
\mathbb E[eX^\epsilon]=
\epsilon\mathbb E[\partial_{\rm slot}X^\epsilon].
\]

The unforced expression has zero pairing with `e`. Passing the finite Cauchy–Schwarz inequality to the joint limit yields

\[
\left|\mathbb E[\partial_{\rm slot}X^\epsilon]\right|
\le C_T h_s.
\]

Only now does fixed-program derivative continuity permit `epsilon -> 0`. The limit is the expected derivative in (38). At the current node, the explicit derivative of the delta yields the separate `M_T` bound. Hence (61) is an expected-response bound, not a claimed samplewise bound on all derivative trajectories.

The argument includes feedback in the finite comparison and freezes it only for the local scalar differentiation after law selection. It does not differentiate the population-law selection map. It also does not infer an off-support derivative from a bound on an unforced singular distribution. Even when an initial reverse source is zero, forcing inserts an actual independent local variable into the complete answer before descendants are formed. The auxiliary two-sample program is available when forcing breaks a special sample relation.

The limiting order is therefore valid: fixed mesh and nonzero forcing; width limit; Gaussian integration by parts in the fresh root; forcing tending to zero; mesh refinement later. No derivative/width interchange or uniform-in-mesh inverse-Gram estimate is hidden here.

### 5. Global bounded Gaussian remainders

Adding learned rank terms preserves an `O(h_s)` bound on past response coefficients. Summing their absolute values over past nodes gives a horizon-dependent bound. Multiplying by bounded deltas or bounded first features gives `|S_ka|+|R_ka| <= C_T` in (63). This deduction uses neither positive definiteness of the current feature Gram nor nonzero deltas; those are proved later.

The cross-program covariance identity supplies a linear Gaussian isometry for the source assignments: an input L2 difference has precisely the same L2 size as its source difference. It follows that the already constructed strong mesh-to-flow convergence also converges the Gaussian sources. Subtracting them from the limiting fields passes the bounded remainders on the same spaces. An almost-everywhere convergent subsequence of an L2-convergent bounded sequence suffices to preserve the essential bound.

The first U expression then has a bounded remainder and a deterministic-coefficient Gaussian integral independent of the full first row. Its finite variance follows from the control bound and the source covariance. Gaussianity and independence persist under the L2 limit of the Riemann sums. Neither second-layer tail argument assumes independence between a Gaussian source and its bounded remainder.

The time assertions are also properly limited: L2-continuous sources give well-defined integrals; jointly measurable representatives and Fubini suffice. It is not necessary to assert independent innovations at different times or to prove that every Gaussian source path is pointwise differentiable.

### 6. Uniform integrability, velocities, and passage to continuous time

I specifically checked that ordinary L2 stability is not silently promoted to convergence of every nonlinear product. The document handles three distinct needs.

1. For each fixed program, all coordinate moments follow from differentiated graph bounds, Gaussian rotation, and the permutation argument for conditional means. This precedes singular regularization and feedback comparison, so those steps can use it without circularity.
2. For continuous-time base fields, the matrix is radially bounded only in an auxiliary moment argument. Deterministic flow stability gives dimension-free Lipschitz control of each coordinate path supremum as a function of the unscaled Gaussian matrix. The conditional-mean permutation argument again controls non-Gaussian stored roots. This proves (72). High-probability equality transfers the required uniform integrability in probability to the actual model; unconditional all-order moments of the untruncated continuous-time system are not needed.
3. For the second preactivation velocity, no bounded Lp operator theorem is available or claimed. Its L2 approximation is proved first from the operator bound and the first activation velocity approximation. At any fixed mesh, the velocity query is identified by Q truncation followed by an L2 query limit. Its W2 convergence controls the squares' tails. Equation (75) transfers that control to the continuous-time finite velocity.

For the last point, a piecewise constant choice of fixed-mesh velocity evaluations makes the quantifiers transparent. Write that comparison as `v_n^h`, and let `v_n` be the finite GF second-preactivation velocity. The preceding estimates give a uniform-in-time L2 error tending to zero as `h -> 0` in the width limsup. Equation (75) gives

\[
\sup_{t\le T}\frac1n\sum_i |v_{n,i}(t)|^2
\mathbf1_{\{|v_{n,i}(t)|>R\}}
\le
4\sup_{t\le T}\|v_n(t)-v_n^h(t)\|_n^2
+2\max_k\frac1n\sum_i |v^h_{n,k,i}|^2
\mathbf1_{\{|v^h_{n,k,i}|>R/2\}}.
\]

Choose a sufficiently fine fixed `h` for the first term. At that `h`, the second term involves finitely many W2-convergent empirical laws and its tails vanish as `R -> infinity`. Then decrease `h` as needed. This proves the uniform tail control used in (67) for the final activation gate. The population version follows from compactness of a continuous L2 velocity curve and the same inequality. This does not require a path-supremum moment bound for `dot Z2` to be assumed in advance.

For the base path laws, the interpolation estimate (74) bounds the average of squared coordinate path errors using the integral of normalized derivative energy. Thus the proof does not confuse the supremum of an RMS error with the RMS of coordinate suprema. The later raw-GD transfer has a stronger maximal-coordinate estimate, obtained explicitly by the finite `sqrt(n)` inequality, so all finite Wasserstein orders transfer there too.

### 7. Strict motion, nonaffinity, and kernel coefficients

The independence needed for first-layer tails is precisely the independence of the reverse Gaussian source family from the first-row roots. Boundedness of the remaining correction permits arbitrary large first Gaussian roots to dominate it. Orthogonal first roots allow two independent signs simultaneously, so the feature Gram is positive definite. At correlation `-1`, the argument uses one nonzero feature and does not manufacture an invertible two-sample Gram.

Positive initial readout-kernel contrast and the exact scalar residual equation give `0<f_1(t)<1`. The readout is therefore nonzero, every second delta is nonzero, and every reverse source variance is positive. Bounded remainders then rule out a zero Q field. This proves all first motions without assuming a sign for an unbounded Q field.

For second motions, the exact identity is

\[
\sum_a c_a\langle\delta^{(2)}_a,\dot Z^{(2)}_a\rangle_2
=\|\dot W^{(2)}\|_{\rm HS}^2+
\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2.
\]

The right side is positive. Exchange-law equality of the two second-layer speed norms then rules out either being zero. In the antiparallel reduction the first-layer term is a single square, not twice that square. The separate contrast/readout identity rules out zero readout speed.

For the local expansion, the reused-transpose return in (94) has conditional residual covariance `Sigma_n`, with no factor `1/n` left after summing over the second population. Removing the finite-rank projection leaves the variance displayed in (92)–(93). This validates the initial reverse coefficients on the canonical operator space.

In feature time, the hidden label-direction kernel is exactly the squared hidden parameter speed. The leading coefficients therefore give

\[
\kappa_{\rm hidden}(s)=d_*s^2+o(s^2).
\]

The derivative of the readout contrast norm, divided by `s`, tends to `2d_*` by the initial adjoint identity. Consequently

\[
\kappa_{\rm readout}(s)=\kappa(0)+d_*s^2+o(s^2),
\qquad
\kappa(s)=\kappa(0)+2d_*s^2+o(s^2).
\]

Finally `s(t)=4t+o(t)`, so `2d_*s(t)^2=32d_*t^2+o(t^2)`. Both hidden and readout contributions are positive; the proof does not infer a full-kernel change from a hidden block while leaving possible readout cancellation unchecked. The expansion uses only first-order strong limits along the actual curve.

## Dependency and theorem-import audit

The proof's dependencies are in a valid order:

1. Section 2 constructs and controls the deterministic flow conditional on a specified bounded operator. It does not pretend that this arbitrary operator has the required Gaussian law.
2. Sections 3.2–3.4 prove the fixed finite-program law, including moments, reuse, singular Grams, and feedback, directly from finite Gaussian conditioning.
3. Section 3.5 uses those laws and the finite operator norm bound to construct the canonical operator and its adjoint, then invokes Section 2 on those spaces.
4. Section 3.6 uses finite-program identification and deterministic stability to prove the expected-response estimates. It does not assume the later nondegeneracy, Gaussian tail conclusions, or strict motion.
5. Section 3.7 combines the response estimates with common-space mesh convergence to obtain bounded Gaussian remainders.
6. Section 4 proves the full observable limits, including the moment and velocity assertions needed to pass symmetry. It does not assume the positive-time speed conclusions of Section 5.
7. Section 5 then uses symmetry, the remainder representations, and initial strong expansions to establish the strict conclusions.

The Gaussian projection, integration-by-parts, rotation inequality, covariance-square-root continuity, contraction construction, scalar integral inequality, finite-net norm bound, and finite-dimensional Wasserstein approximation are all supplied or reduced to elementary calculations within the source. Routine scalar calculus, finite-dimensional linear algebra, completeness, Fubini, dominated convergence, and elementary probability inequalities are used with valid hypotheses. There is no tensor-program theorem, infinite-width theorem, all-angle flow theorem, or external response theorem imported without proof.

## Required versus optional corrections

### Required corrections

**None.** I found no false displayed identity, missing essential hypothesis, unproved heavy theorem import, invalid use of a singular inverse, circular uniform-integrability argument, or unjustified width/time/forcing exchange that prevents the stated theorem from following.

### Optional clarifications

These changes would make the proof easier to audit. They are not conditions of the PASS verdict.

| Item | Source reference | Concrete optional edit and reason |
| --- | --- | --- |
| O1: Specify all parameters bounded in conditional test estimates | Lines 784–801; (48) | Say “on an event bounding the regression coefficients and innovation standard deviation.” For general additional unbounded probes, one can explicitly intersect with `sigma_n <= A`; (45) and `sigma_n <= ||h||_n` justify removing this event. This makes the dependence of the constant in (48) transparent. For the base bounded feature/delta inputs the innovation bound is already deterministic at fixed program length. |
| O2: Name the time extension of the finite velocity comparison | Lines 1383–1413; (73), (75) | State that the comparison velocity may be taken piecewise constant at the left mesh nodes and write the finite-maximum tail estimate displayed in this review. The existing estimates already justify this choice; naming it makes the passage from finitely many evaluations to uniform-in-time tail control immediate. |
| O3: Make the fixed-program quantifier explicit | Lines 179–190, 1347–1354 | Add that a requested finite probe program has fixed instructions, scalar coefficients, and root laws as width varies, apart from the normalization explicitly built into the model. This restates the finite-program scope and prevents interpreting it as permission to recover an order-one root by an arbitrary width-dependent amplification of the vanishing initial readout. |
| O4: Qualify the zero-time hidden-speed sentence locally | Lines 217–219 and 1665–1666 | Write “The limiting population hidden speeds at zero are zero.” The theorem's context already gives this interpretation, and the finite-readout restoration is correct; the added word prevents that sentence from being read as a finite-width pathwise assertion. |

No source modification was made. The general-angle task mentioned in the review request was not inspected or worked on.

## Final integrity record

The source was hashed again after the complete audit and the review-file write. Its SHA-256 remained `5cd54a6125dfbf4b7d1bc86149760b842d7d2c1f9a44fe73fcf57f5d3d15f12e`; its length remained 1,935 lines and 91,679 bytes. The separate review file was checked for its verdict, coverage sections, required/optional correction sections, and completion of the integrity record. The source was not modified.
