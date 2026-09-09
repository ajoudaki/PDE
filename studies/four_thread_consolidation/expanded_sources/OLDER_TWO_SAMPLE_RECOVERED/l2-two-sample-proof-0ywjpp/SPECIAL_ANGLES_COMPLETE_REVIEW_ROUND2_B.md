# Independent full mathematical review — Round 2 B

## Verdict and scope

**PASS for the theorem stated in Section 1.3: two hidden layers, both activations arctangent, the specified initialization, parameter metric, physical clock, and input correlations exactly \(\rho=0\) or \(\rho=-1\).**

I read and audited the entire supplied document, including all numbered equations (1)–(107), the construction of the common action spaces, the finite-width and time-limit arguments, and all the nontriviality conclusions. I found no mathematical gap requiring correction. In particular, the reused-matrix identification retains the correct response terms and joint source covariances; singular histories are treated by actual perturbed finite programs; the common operator has an actual bounded Hilbert adjoint; and the mesh-uniform response argument does not assume the uniformity it proves.

This verdict is not an all-angle result. It does not cover another depth or activation, a different parameter metric, arbitrary width-dependent probes, a width/time limit with the time horizon tending to infinity, or a restart that discards part of the state. The source expressly excludes these extensions.

Required corrections: **none**. Optional presentation improvements appear at the end and do not qualify the mathematical verdict.

## Isolation and integrity record

- Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`.
- Entire source read directly, with line numbers: **1–1977**, comprising **94,653 bytes**.
- Expected SHA-256: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- Before-review SHA-256: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- After-review SHA-256: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- The initial and final hashes agree with the supplied hash.
- The only other file read was the procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`. It supplied review procedure, not mathematical context.
- No other project files, dependency notes, ledgers, snapshots, previous reviews, or mathematical sources were opened. In particular, the four provenance files named at the end of the source were not opened or used as premises.
- No agents, experiments, numerical calculations, source modifications, or external searches were used. The mathematical checks below are analytic.
- The only file written was this requested report, using `apply_patch`.

Line references below refer to the unchanged source, not this report.

## Coverage and dependency audit

The following table records the full coverage. The explanations following it include the substantive checks, especially at the interfaces between sections.

| Source portion | Obligations checked | Result |
| --- | --- | --- |
| Section 1, lines 10–235, (1)–(14) | Model, gradient metric, normalizations, operator spaces, observable scope, theorem conclusions | Met by the subsequent proof |
| Section 2.1, lines 239–294, (15)–(18) | Special-angle transformation, antiparallel reduction, first-row reconstruction | Correct |
| Section 2.2, lines 296–376, (19)–(22) | Ordinary \(L^2\) estimates, clipping construction, stability, operator/HS comparison | Correct |
| Section 2.3, lines 378–454, (23)–(27) | Global extension, curve chain rule, energy, uniqueness in the original class, restart | Correct |
| Section 2.4, lines 456–553, (28)–(35) | Euler first-exit argument, raw cubic defect, interpolation, velocities, high-probability bounds | Correct |
| Sections 3.1–3.2, lines 557–747, (36)–(45) | Causal scalar program, derivative convention, deterministic readout bound, all-order fixed-program moments | Correct |
| Section 3.3, lines 749–859, (46)–(51) | Adaptive Gaussian conditioning, both orientations, empirical induction, full source identification | Correct |
| Section 3.4, lines 861–958, (52)–(54) | Singular Grams, formal slots, continuity, empirical feedback, Wasserstein convergence | Correct |
| Section 3.5, lines 960–1044, (55)–(56) | Common spaces, bounded actions, actual adjoint, canonicity, common-space Euler comparison | Correct |
| Section 3.6, lines 1046–1149, (57)–(62) | Actual fresh-root perturbations, order of limits, mesh-uniform expected and learned responses | Correct; no circular uniformity argument |
| Section 3.7, lines 1151–1215, (63)–(66) | Bounded Gaussian remainders, cross-program isometries, continuous-time passage and measurability | Correct |
| Section 4.1, lines 1219–1311, (67)–(72) | Product continuity, uniform path moments, auxiliary norm cap, actual initial readout | Correct |
| Sections 4.2–4.3, lines 1313–1396, (73)–(74) | Probes, width/mesh passage, same-neuron path laws, uniform scalar outputs | Correct |
| Section 4.4, lines 1398–1491, (75)–(76) | All original velocities, final gate product, parameter speeds, increments, energies, raw-GD transfer | Correct |
| Sections 5.1–5.3, lines 1495–1708, (77)–(90) | Exchange symmetry, unbounded tails, positive nonaffinity distance, progress and every claimed strict speed | Correct |
| Section 5.4, lines 1710–1806, (91)–(95) | Initial reused-transpose law, full Gaussian covariance, nondegeneracy | Correct |
| Section 5.5, lines 1808–1938, (96)–(107) | Strong initial expansions, both geometries, hidden/readout kernel contributions, physical-time coefficient | Correct |
| Section 5.6, lines 1940–1977 | Scope exclusions and absence of imported mathematical premises | Consistent with the proof |

The dependencies are noncircular. Section 2 proves deterministic existence and stability for a specified bounded operator. Sections 3.1–3.4 prove fixed finite-program laws with constants allowed to depend on the finite program. Section 3.5 then constructs the canonical operator and places the comparison meshes on common spaces. Section 3.6 obtains response constants uniform over meshes from finite-width perturbation estimates, using the already established fixed-program theorem only at one fixed mesh and one fixed nonzero perturbation. Section 3.7 uses those response bounds to obtain the bounded remainders. Independently, Section 4.1 obtains time-uniform moment estimates from deterministic stability and Gaussian concentration. Neither the fixed-program proof nor the fresh-root estimate assumes the bounded remainders or the all-time nontriviality conclusions.

## 1. Model, deterministic dynamics, and raw discretization

### Normalization and the two special geometries

The Euclidean gradients in lines 80–83 are correct. Applying the inverse of the metric (7) gives the three different factors in (6): \(2/d\), \(2/n\), and \(2\). Thus the population rank equation uses \(\delta\otimes h\), whose finite matrix is \(\delta h^T/n\). There is no missing factor of \(n\) in the action of the initial middle matrix or its transpose.

Equipping both finite neuron spaces with the same normalized inner product leaves the middle matrix's adjoint equal to its ordinary transpose, its operator norm equal to the Euclidean operator norm, and its Hilbert–Schmidt norm equal to the ordinary Frobenius norm. The rank-one norm identity (9) is consistent in both the finite and population settings.

The coordinate change is exact at the stated angles. Since

\[
F'(z)=1+z^2=1/\phi'(z),
\]

the diagonal first-layer equation at \(C=I\) becomes \(\dot U_a=c_aQ_a\). For opposite inputs, the odd/even identities (17) hold for arbitrary raw parameter arrays, including arbitrary readout. They give the reduced coefficient \(c_1-c_2=-4r_1\). The factor four is correct for the sum loss. The reconstruction (18) retains the unchanged orthogonal part of the first row and counts only one independent first-field motion in the antiparallel case.

The inverse and composed-feature Lipschitz bounds in Section 2.1 are valid. The initial transformed field has finite second moment, with the displayed value \(\mathbb EF(G)^2=14/3\). At intermediate correlations, the cancellation would leave the unbounded ratio displayed in Section 5.6; the proof does not silently extend its estimates to that case.

### Stability, existence, energy, and restart

All terms of (20) follow by subtracting one factor at a time. In particular, estimating the difference of \(W^*\delta\) needs only an operator norm and the readout's essential bound. Estimating a rank difference uses the product of two ordinary \(L^2\) norms. No bound on the operator's action on arbitrary \(L^p\) inputs, and no \(L^\infty\) bound on the first backward field, is used here.

The clipped-readout construction resolves the fact that an \(L^\infty\) ball is not open in \(L^2\). The clipped vector field is locally Lipschitz on an open state ball. Its readout integral has an essential bound, so choosing the clipping level with slack gives a local interval on which clipping is inactive. The integral-map contraction and the subsequent Gronwall estimate supply local existence and uniqueness in the claimed norms.

The action bounds (23) integrate the readout and rank equations with the correct powers and constants. They yield a limit at any finite endpoint of finite action. The chain rule in lines 400–408 is correctly proved along a \(C^1\), \(L^2\)-valued curve; it does not assume Fréchet differentiability of a nonlinear composition map on an entire \(L^2\) neighborhood.

Using the actual adjoint in the prediction derivative gives precisely the three kernel blocks (12). Each block is a Gram matrix, including the first block with possibly negative off-diagonal input correlation. The loss identity (24) has the correct sign and factor. Its first-matrix term is the sum over the independent first coordinates, not a sum that counts antiparallel motion twice. Consequently residuals remain bounded, the action is at most linear in time, and the a priori bounds extend the solution through every finite horizon.

The uniqueness argument for solutions of the original integral equations is substantive and valid: the readout equation first provides a local essential bound, the first equation then has an almost-everywhere absolutely continuous scalar representative, and the scalar chain rule gives (27) with an \(L^2\) right-hand side. Such a solution therefore lies in the transformed uniqueness class. The same properties hold at every reached state. Restart is justified with the entire operator and all fields retained.

### Euler and raw gradient descent

The transformed Euler estimate is uniform in width on the prescribed state bounds. The first-exit argument is not assuming that discrete loss decreases: it bounds the discrete action up to the candidate exit, then uses closeness to the exact flow to exclude that exit. This is the appropriate way to justify the untruncated iterates.

The polynomial defect (30) is exact. On the bounded-state event,

\[
\|q\|_{\mathrm{emp},2}=O_T(1),\qquad
\|q\|_\infty=O_T(\sqrt n).
\]

Thus the normalized quadratic and cubic defect bounds are respectively \(O_T(\eta^2\sqrt n)\) and \(O_T(\eta^3n)\). Summing \(O(T/\eta)\) steps with \(\eta=n^{-2}\) gives \(O_T(n^{-3/2})\), dominating the usual \(O_T(n^{-2})\) Euler error. The raw-interpolation cubic correction and its differentiated bound have the claimed orders.

Equation (32) then loses one factor \(\sqrt n\), giving \(O_T(n^{-1})\) errors for the original first velocities. In (33), operator bounds control the second preactivation velocity; the final gate difference is controlled using the same finite-coordinate bound. The claimed \(O_T(n^{-1})\) hidden-velocity errors and the smaller rank/readout errors are consistent. Squared norms and kernel blocks transfer by the displayed norm-difference inequality. No exact discrete loss identity is invoked.

The net argument in (34) is sufficient: the two net approximations give the factor two in the operator bound, and the resulting exponent is negative at threshold 8. The readout bounds in (35) are direct Gaussian union bounds. They supply high-probability, width-independent constants without requiring additional bounds on the Gaussian first-row coordinates.

## 2. Full reused-matrix Gaussian identification

### Fixed-program moments

The deterministic readout recursion (41) is valid even when a matrix query is perturbed, because the activations remain bounded. Replacing the readout factor in a coordinate map by a smooth cutoff outside its actual range therefore leaves the program unchanged and makes the needed coordinate map globally Lipschitz.

The induction (42) correctly distinguishes vector and scalar sensitivities to the unscaled Gaussian entries. An initial matrix action has differential

\[
W\,\partial x+n^{-1/2}(\partial E)x,
\]

and a normalized contraction contributes the compensating \(n^{-1/2}\) to its scalar differential. Scalar-times-vector operations consequently preserve the stated scaling. Treating \(F(G)\) as part of an iid stored root tuple avoids an unjustified global Lipschitz assertion for the cubic map.

The Gaussian inequality (43) is proved by rotation and conditional Jensen. The permutation argument (44) is sufficient to control conditional means even though the stored root tuple is not itself jointly Gaussian. Together with the matrix-norm tail bound and the roots' moments, these arguments establish (45) for every fixed graph. These constants may depend on graph size; nothing here claims mesh uniformity prematurely.

### Adaptive conditioning and the source-response formula

Formula (46) has the correct conditional mean and residual covariance. Both constraints are met because \(J^TY=P^TV\), and the residual matrix is projected off the old reverse-input span on the left and the old forward-input span on the right. The adaptive queries are measurable with respect to the preceding transcript and roots. Revealing a new answer therefore adds its linear constraint to the current Gaussian conditional law. There is no independent replacement of the original matrix when its transpose is queried.

For a new forward query, the regression formula involving \(\lambda_n,\nu_n,\sigma_n\) is correctly normalized. The fixed-rank Gaussian projection removed in (47) has empirical \(p\)-moment tending to zero; this follows from the diagonal projection bound and not from coordinate independence of the reused matrix. After this removal, the innovation coordinates are conditionally independent, so (48) applies. Truncation with a higher moment, as in (49), handles general continuous polynomial-growth tests and restores the small projection error.

The derivation of (50) is the central identification step. If \(h_\perp=h-\sum_r\lambda_rh_r\), then the old forward-input components of an old reverse answer have zero inner product with \(h_\perp\). Hence

\[
\mathbb E[(W^Tv_s)h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

Gaussian integration by parts turns the latter vector into \(\Gamma_v\mathbb E\nabla_\zeta h_\perp\). Multiplying by \(\Gamma_v^{-1}\) in the nonsingular case gives exactly the coefficient in lines 844–847. Substitution of the old forward-answer decompositions cancels the derivatives of the least-squares projection, leaving the full derivative of \(h\) in (50). The reverse calculation uses the same matrix with the populations interchanged.

The innovation is added to the projection of the old Gaussian source, so the covariance of the full source is the **uncentered input second moment**, not a centered covariance and not an input variance reduced by a response contribution. This verifies (39), including cross-sample and cross-program covariances. The two source groups and the local independent roots remain independent in the asserted scalar construction; no artificial pairing of neurons from different populations is needed.

The ordering in (37)–(40) is causal. Both forward answers at a node precede the reverse answers, and all updates follow. The current-source derivative of the readout factor is zero at that node, while the current derivative through \(\phi'(Z^{(2)}_{ka})\) gives the diagonal term in (40). Earlier readout derivatives are retained. There is no missing current reverse correction or omitted past readout dependence.

### Singular histories and actual feedback

The singular-history argument uses fresh noise in the **inputs of actual initial-matrix queries**, not an inverse of a singular covariance. A new independent Gaussian input component has squared distance at least \(\epsilon^2\) from the previous limiting same-direction span. At fixed positive \(\epsilon\), nonsingular conditioning is therefore applicable.

The coupled finite-graph estimate (52) gives an \(O(\epsilon)\) normalized \(L^2\) error with a random factor having all finite moments. Interpolation (53) and (45) upgrade this to every finite moment order needed for empirical tests. This comparison does not require any inverse-Gram bound uniform as \(\epsilon\) tends to zero.

On the scalar side, (50) removes inverse covariances from the limiting formula. The finite expressions and their formal source derivatives depend continuously on already selected coefficients. Covariance square roots are continuous at singular matrices, and a common Gaussian coupling plus moment domination proves continuity of the next coefficients and moments. This is a finite causal induction, not an assumption about a limiting infinite history.

Consequently the order “fixed positive noise, width limit, noise tending to zero” proves the unperturbed law even for zero or redundant queries. Retaining formal source slots at a rank drop is necessary and justified. The null-space observation at lines 918–924 also correctly explains why a null-direction ambiguity cannot change a contracted response.

The learned-rank identities (54) are exact. Replacing empirical contractions by their sequentially selected expectations gives a deterministic-coefficient program whose contractions converge by the preceding theorem. The coupled finite induction then recovers the actual feedback program. This comparison is made after the deterministic coefficients have been identified; it does not assume convergence of feedback to prove that same convergence. The finite-dimensional Wasserstein argument by bounded-cell matching and tail control is sufficient for the stated fixed-program law.

## 3. Common action spaces and the bounded adjoint

The countable program construction includes the inputs and outputs needed by both matrix orientations, rational linear combinations, cylinder functions, and the specified probe roots. Every finite part is governed by the same-matrix joint finite-program theorem. Subtracting the selected response also makes the Gaussian sources available as generated nodes.

All three relations in (55) transfer from finite width. For the inequalities, convergence of the finitely many Gram entries to deterministic values and the event \(\|W_n\|\le8\) exclude a strict limiting violation. For the adjoint identity, the finite equality is exact. A zero-norm linear relation among inputs therefore induces a zero-norm relation among answers; this proves that the proposed linear action is well defined on the queried span.

Density is addressed rather than assumed. The finite-cylinder approximation argument generates the relevant sigma field. One-sided smooth approximations of rational threshold events handle atoms, so singular source laws do not invalidate the cylinder-function density step. The two actions extend continuously to the resulting \(L^2\) completions. Passing the bilinear identity to those completions identifies the reverse action as the **actual Hilbert adjoint** of the forward action.

The asserted canonicity is on the generated spaces and their common-law identifications. Additional requested programs can be adjoined without changing earlier marginals, because those marginals already have a unique full-sequence finite-width limit. The proof does not require operator-norm convergence of differently sized matrices, an iid continuum kernel, or an operator bounded on every \(L^p\).

Once these actions exist, every comparison mesh satisfies its Euler equations using this same operator and adjoint. Thus (56) follows from deterministic stability on common spaces. The flow is not assembled from unrelated marginal limits or mesh-specific initial operators.

## 4. Mesh-uniform learned response: explicit circularity check

This part meets the strongest additional scrutiny requested in the review.

First, (57) and the rank updates give state and operator bounds depending only on the horizon, uniformly over the relevant partitions. These are elementary bounds for the actual finite programs. They do not use a previously proved response decomposition. The one-step state comparison has factor \(1+C_Th_k\), including empirical residual feedback. Keeping both first-sample coordinates makes the auxiliary comparison valid when a perturbation leaves the unforced special-angle relations; it is not being asserted to be raw gradient flow off that invariant state.

Forcing a complete reverse answer at node \(s\) first enters the state through an update multiplied by \(h_s\). Therefore (58) has the factor \(h_s\), including after all later steps. Forcing a complete forward answer changes the current activations, deltas, residuals, and reverse answer by \(O(|\epsilon|\|e\|_{\mathrm{emp},2})\), but every state update again carries \(h_s\). This yields (59) for later deltas, while allowing the stated unsuppressed current-node derivative. Both comparisons use the actual transpose and actual empirical feedback.

The next step does not differentiate these finite estimates with respect to a singular Gaussian coordinate. Instead, it fixes the mesh and nonzero \(\epsilon\), takes the joint finite-program width limit of the forced run, unforced run, and fresh root, and uses a genuine independent local Gaussian root in that identified limit. In the local coordinate expression, the root enters only by replacing the designated source slot by that slot plus \(\epsilon e\). The selected coefficients and covariances may depend on \(\epsilon\), but they are deterministic as functions of the local coordinate \(e\). Hence

\[
\partial_e X^\epsilon=\epsilon\partial_{\mathrm{slot}}X^\epsilon,
\qquad
\mathbb E[eX^\epsilon]
=\epsilon\mathbb E[\partial_{\mathrm{slot}}X^\epsilon].
\]

This is differentiation in the independent root, not differentiation of the selected expectations with respect to the perturbation amplitude. The distinction correctly handles feedback.

The unforced field is independent of the unused root. Passing finite Cauchy–Schwarz to the joint limit therefore bounds the last expected derivative by \(C_Th_s\). Only then is \(\epsilon\) sent to zero, using fixed-program continuity of coefficients and formal derivatives. This identifies the derivative with the precise coefficient in (38), even if the unforced slot had zero variance. It establishes (61) without assuming invertibility or control of a derivative transverse to the support of the unforced law.

Finally, the explicit learned terms have a factor \(\gamma_{sb}=O_T(h_s)\), with bounded feature and delta moments. Thus (62) follows, and summing past terms uses \(\sum_sh_s\le T+1\), not the number of queries. Current terms have the separate diagonal bound. This supplies the uniform absolute row sums needed for (63).

The logical order is consequently:

1. Uniform finite-state bounds and actual perturbation estimates.
2. Fixed-mesh, fixed-nonzero-perturbation Gaussian identification.
3. Integration by parts in an independent fresh root.
4. Fixed-mesh continuity as perturbation tends to zero.
5. A response bound whose constant is already uniform over meshes.

There is no exchange of an unproved uniform derivative limit with mesh refinement and no circular response bootstrap.

## 5. Bounded remainders and observable limits

### Gaussian remainders

The absolute response-row bounds and bounded rank factors give (63). The source variances are the full input squared norms from (39). Integrating the first equation then gives (64), with a Gaussian term independent of the initial first row and a bounded remainder. The inverse Lipschitz bound yields the claimed upper-tail and moment controls.

Cross-program covariance identification gives the isometries (65), so convergence of inputs on the common spaces implies convergence of their Gaussian sources. Subtracting these sources from the converging fields identifies limiting remainders. An \(L^2\) limit of variables with a common essential bound retains that bound. The Gaussian integral in (66) is well defined because the source inputs are \(L^2\)-continuous and the coefficients are deterministic; its Gaussian law and independence from the first row persist under the limit. The stated deterministic-time and product-almost-everywhere versions suffice for the later tail arguments and integrals. No stronger sample-path regularity of the source process is assumed.

### Uniform moments and products

Equation (67) correctly addresses the failure of joint \(L^2\)-Lipschitz continuity for a bounded gate multiplied by an arbitrary \(L^2\) field. Subsequent uses either employ a fixed-field continuity argument or establish uniform integrability explicitly.

The initial-operator cap (68) is a 2-Lipschitz map in operator norm. An unscaled-entry perturbation consequently changes it by at most \(2\|\Delta E\|_F/\sqrt n\). Deterministic state stability for the fields in (69) implies, for an individual coordinate,

\[
\left|\sup_{t\le T}|X_i(t)|-\sup_{t\le T}|\widetilde X_i(t)|\right|
\le \sqrt n\sup_{t\le T}\|X(t)-\widetilde X(t)\|_{\mathrm{emp},2}.
\]

The normalization cancels the factor \(\sqrt n\), giving the asserted width-independent scalar Lipschitz constant. Equations (70)–(71) bound the normalized \(L^2\) norm of the coordinatewise path supremum. The conditional Gaussian inequality and permutation estimate therefore apply to these supremum functionals, proving (72).

The capped operator and clipped initial readout are used only for moment estimates and coincide with the actual arrays with probability tending to one. The clipped readout roots have uniformly bounded moments even though their law depends on width. This is sufficient for the moment argument; the fixed-program limit is separately obtained from zero readout and the stability comparison. The bound on \(\delta^{(1)}\) by \(Q^{(1)}\) supplies its path moments without differentiating that product to obtain a stronger moment estimate.

### Probes, paths, and full-sequence convergence

Truncating \(Q^{(1)}\) makes the first velocity-query products globally Lipschitz coordinate instructions. Their untruncated errors vanish in ordinary normalized \(L^2\), uniformly in probability where needed, by (45) or (72). The bounded operator multiplies this error by only a fixed constant, in either orientation. This establishes the velocity probes in (73) without requiring an arbitrary \(L^p\) operator bound.

For fixed observations, the width/mesh triangle has the correct order: choose a fixed sufficiently fine mesh using width-independent deterministic comparisons, then take the width limit of that finite program. The population comparison takes place on the common spaces. The initial readout is restored by an actual same-initialization coupling; its normalized \(L^2\) size tends to zero, and (35) supplies the essential bound needed in the stability constants. No initialization is changed in the asserted finite model.

The general admissible-probe scope is limited to fixed programs and the stated uniform \(L^2\) approximations. Finite programs can be adjoined to the common construction, and learned rank integrals can be approximated by finite sums using their Hilbert–Schmidt continuity. This does not quantify over arbitrary width-dependent directions or amplify the vanishing readout.

The polygonal estimate (74), averaged over neurons, controls path-space transport by an integrated squared derivative. Equations (70)–(71) give the required derivative bounds for the base tuple. Fixed-grid convergence followed by grid refinement therefore gives same-neuron Wasserstein-2 path convergence. Multiplication on continuous-path space and the \(Q^{(1)}\) supremum moments handle \(\delta^{(1)}\). Higher supremum moments upgrade to each finite Wasserstein order and polynomial-growth tests. The operator cap's exceptional event can be removed because the claimed mode of convergence is in probability.

Predictions, loss, and all three kernel blocks are treated with the appropriate continuity estimates. In particular, block 1 uses uniform integrability of the squared backward-field suprema. Finite mesh contractions and the uniform time modulus supply uniform-in-time scalar convergence.

### Velocities, the final gate product, and energies

The transformed velocity comparison first gives the original first preactivation and activation comparisons using (67) and (72). Rank and readout velocities are Lipschitz in the bounded state. The second preactivation velocity then follows from its two-term operator identity in (73), before attempting the final multiplication by \(\phi'(Z^{(2)})\).

The additional uniform-integrability argument at lines 1436–1454 is necessary and sufficient. For clarity, its quantifiers can be read as follows. Fix a target tail tolerance and choose one fixed comparison mesh \(h_0\) making the second-preactivation-velocity \(L^2\) error small in the width limsup. At this fixed mesh there are only finitely many velocity laws, each with Wasserstein-2 convergence, so their squared tails can be made small with one large cutoff \(R\). Equation (75) then gives a time-uniform tail bound for the finite-flow velocity. With that bound established, the mesh used for the final gate comparison may tend to zero independently. On the population side, compactness of a continuous \(L^2\)-valued velocity curve gives the corresponding finite-cover argument.

Thus this step does not assume an \(L^p\) bound for the matrix image of the velocity and does not require selecting a cutoff that is simultaneously controlled by an unproved mesh-uniform moment estimate. Applying (67) is now justified. The integrated mean-square comparisons follow from the stated supremum-in-time \(L^2\) comparisons. Discontinuous comparison velocities are not assigned a continuous-path law.

The first parameter metric follows from (18), the middle squared speed is exactly (76), and the readout speed is its normalized field norm. The converging contractions prove all claimed parameter-speed and hidden-velocity quadratic limits. Cross-time contractions of finite rank sums give the middle-operator increment norm; this concerns the Hilbert–Schmidt increment, not the initial operator. The uniform estimates justify integration over each fixed horizon.

Finally, (31)–(33) transfer these conclusions from finite flow to the specified raw interpolation. For base paths, the normalized \(O_T(n^{-3/2})\) error implies an \(O_T(n^{-1})\) maximal-coordinate error. The first backward product also has a vanishing maximal-coordinate error after the bound in (32). These same-neuron couplings transfer every fixed path Wasserstein order. The argument retains the actual Gaussian readout and the original physical clock.

## 6. Nonlinearity, strict learning, and the full kernel

### Symmetry and tails

The reflection (77) swaps the equal-norm inputs. The parameter transformation (78) preserves initialization law, loss, and metric and commutes with both finite flow and raw updates. Its residual and backward-field signs in (79) are correct because the labels are opposite. Passing to deterministic limiting predictions and squared velocity norms gives (80). At \(\rho=0\), the source correctly uses equality in law and deterministic limiting values; it does not promote this to a finite pathwise sample identity. At \(\rho=-1\), the stronger exact opposition identities do hold.

In (81), the Gaussian integral is independent of the first row and the remainder is bounded. Restricting the Gaussian integral to a bounded event of positive probability and taking a sufficiently large positive or negative initial Gaussian root forces either first-field tail. For \(\rho=0\), independence of \(G_1,G_2\) permits all four limiting feature corners, proving positive definiteness of the uncentered feature Gram (82). The antiparallel case uses only the nonzero one-feature norm.

The second-layer Gaussian source consequently has positive variance. A bounded, possibly dependent remainder cannot remove either unbounded Gaussian tail, so (83) is valid without an independence assumption on the remainder. For each resulting field, \(\operatorname{Var}(Z)>0\) makes the affine span of \(1,Z\) closed. Boundedness of arctangent excludes a nonzero affine slope on an unbounded distribution, and strict monotonicity excludes a constant activation on a nonconstant field. This proves the strictly positive distance in (14), not merely the absence of a particular affine representation.

### Positive progress and all claimed speeds

The exchange law gives \(r=(f_1-1)y\). The prediction equation then yields (85) with the correct factor four. The kernel and residual bounds make its exponent finite on each finite horizon. The initial second-feature covariance is \(mI\) in the orthogonal case and the stated rank-one covariance in the antiparallel case, so \(\kappa(0)>0\). Continuity and monotonicity imply \(0<f_1(t)<1\) at every positive finite time.

This makes the readout field nonzero. Since \(\phi'>0\), every second delta is nonzero. Its Gaussian reverse source has positive variance, and its bounded remainder makes the complete first backward field nonzero. The special-angle first equation then gives every first preactivation and activation speed, and the first-parameter speed, strictly positive.

For the middle parameter, (89) follows by applying the positive definite first-feature Gram to the pointwise vector \((y_a\delta_a^{(2)})_a\) and integrating. The antiparallel velocity is directly a nonzero rank-one operator. This avoids assuming that a sum of nonzero ranks cannot cancel.

Identity (90) correctly handles the possible cancellation between the two contributions to a second preactivation velocity. Its right-hand side is strictly positive. Thus at least one second-layer velocity is nonzero, and the exchange-law equality of norms makes both nonzero. The antiparallel calculation counts the first-field energy once. Positive gates give both second activation speeds. Finally, a zero readout velocity would make the contrast feature zero and contradict \(f_1>0\). Hidden velocities at zero vanish because the limiting readout is zero. Continuity supplies positive energy on every interval of positive length contained in positive time.

### The initial reused-transpose law

Formula (94) is the correctly normalized finite conditional law. Conditional on the initial first features and their forward answers, the bounded row functions \(\widehat\delta\) are fixed. The reverse Gaussian term has covariance \(\Sigma_n\) and projection \(P_{\mathsf H^\perp}\). Removing that fixed-rank projection costs vanishing empirical moments by (47). Conditional averaging identifies the regression coefficient and covariance.

Consequently (92)–(93) have the full covariance

\[
\mathbb E[\eta_a\eta_b]
=\mathbb E[\widehat\delta_a^{(2)}\widehat\delta_b^{(2)}],
\]

without subtracting the covariance of the response term. The response itself remains explicitly correlated with the first features. This is consistent with the general reused-matrix rule (50). The proof's positive-definiteness argument for the orthogonal pair is valid: a vanishing linear combination would force an impossible identity between the nonconstant one-variable functions \(\phi'(u)\) and \(\phi'(v)\) on an open set. The reduced one-column variance is also positive. Equation (95) follows from the independent positive conditional Gaussian variance and the strictly positive gate.

### Initial kernel expansion and the physical-time coefficient

The feature time (96) is used only for a local expansion and satisfies \(s(t)=4t+o(t)\). The orthogonal feature equations have coefficient \(1/2\), while the reduced antiparallel equations have coefficient one. These factors agree with both the parameter metric and the sum loss.

The strong limits (98) follow from the integral readout equation, bounded gate continuity, and operator-norm continuity. Using those limits in the first, rank, and second-preactivation equations gives (99)–(100). At the orthogonal initialization the off-diagonal feature inner product is zero, which explains the isolated \(m\widehat\delta_a\) term in (99). The rank norm and actual adjoint give (101)–(102) with the displayed factors. Equations (103) supply the correct one-field versions at the antiparallel angle.

In both geometries, \(d_*>0\). The hidden part of the label-direction kernel is the squared feature-time hidden-parameter speed, hence

\[
\kappa_{\mathrm{hidden}}(s)=d_*s^2+o(s^2).
\]

Differentiating the readout feature norm along its \(L^2\) curve gives (105). After division by \(s\), the limit is \(2d_*\), using the actual adjoint identity (102), or the two equal antiparallel contributions. Integration gives a further \(d_*s^2\) contribution from the readout kernel. Thus no negative readout term cancels the hidden contribution:

\[
\kappa(s)=\kappa(0)+2d_*s^2+o(s^2),
\qquad
\kappa(t)=\kappa(0)+32d_*t^2+o(t^2).
\]

This verifies the stated strictly positive leading quadratic change of the full raw kernel. The proof uses strong first-order velocity limits and curve chain rules, not an unproved second Fréchet derivative on \(L^2\).

## 7. External-result and hidden-assumption audit

No essential nonclassic theorem is imported without proof. The specialized adaptive Gaussian-program result is established in Sections 3.2–3.4 rather than cited. The global response result is established in Section 3.6 rather than assumed. The document proves the needed Gaussian concentration inequality, Gaussian integration-by-parts identity, finite-rank projection estimate, covariance-square-root continuity, contraction construction, Gronwall estimates, and relevant Wasserstein approximation argument.

The remaining elementary tools—finite-dimensional Gaussian orthogonal projection, scalar integration by parts, Fubini, dominated convergence, basic finite-dimensional spectral facts, and elementary probability-space completion—are used with the relevant integrability or positivity hypotheses supplied. The provenance list in lines 1962–1977 is not used as an imported mathematical premise. No external statement or proof was needed to repair an obligation.

Specific plausible failure mechanisms were checked and excluded:

- Replacing the reused transpose by an independent matrix: excluded by (46), (50), (55), and (94).
- Centering the wrong source covariance or subtracting a response variance: excluded by the projection cancellation calculation and the explicit initial return law.
- Inverting a singular Gram or deleting a zero-variance formal slot: excluded by the actual query-noise comparison and the retained-slot convention.
- Inferring an off-support derivative from a singular marginal law: excluded by the independent fresh-root forcing argument.
- Dropping feedback in the finite perturbation comparison: excluded by the state comparison preceding (58)–(59); only deterministic selected quantities are held fixed in the local scalar derivative.
- Summing a per-query response bound that lacks a step-size factor: excluded by the factors \(h_s\) in (61)–(62).
- Comparing different meshes on unrelated spaces: excluded by the joint finite-program construction and (55)–(56).
- Using bounded \(L^2\) operator norm as an arbitrary \(L^p\) operator bound: excluded by the separate random-field moment and truncation arguments.
- Treating a bounded gate product as jointly Lipschitz on \(L^2\): excluded by (67) and the additional velocity-tail argument (75).
- Assuming discrete loss monotonicity, finite pathwise exchange symmetry at \(\rho=0\), or an unchanged clock under feature-time expansion: none is used.

## 8. Optional clarity improvements

These are presentation suggestions only. They do not identify missing hypotheses or unproved mathematical steps.

1. **Make the two mesh choices in the last velocity argument explicit** (lines 1436–1454). Label the fixed mesh used to establish tail control \(h_0\), and use a separate mesh parameter for the later gate comparison. The existing quantifiers support this reading; separate notation would make the absence of circularity immediate.

2. **State the one-coordinate supremum inequality next to the moment argument** (lines 1259–1265). The displayed inequality in this report makes transparent why a uniform normalized \(L^2\) stability bound yields a width-independent Gaussian Lipschitz constant for an individual coordinate's path supremum.

3. **Emphasize generated-space canonicity when adding probes** (lines 1022–1026 and 1362–1369). One sentence could distinguish re-enumerating a fixed generated family from adjoining new roots or queries and preserving the old marginals. The existing construction already provides the needed consistent extension; this would clarify the intended meaning for readers expecting a prescribed external continuum kernel.

4. **Keep the order of limits beside any later reuse of (61)**. The source states it correctly in Section 3.6. Repeating “fixed mesh, nonzero forcing, width limit, then forcing to zero” when summarizing the response result would help prevent an incorrect interpretation as a uniform derivative-limit interchange.

## Final determination

All mathematical obligations of the complete supplied document are met for the stated \(L=2\), \(\rho\in\{0,-1\}\) theorem. The result includes the canonical joint finite-width limit, the autonomous global-on-finite-horizons population flow and its restart property, the stated probes and path/velocity/energy limits, persistent distributional nonaffinity, all positive-time strict-speed assertions, and the strictly positive initial quadratic change of the full kernel. **PASS within that scope; no all-angle inference.**
