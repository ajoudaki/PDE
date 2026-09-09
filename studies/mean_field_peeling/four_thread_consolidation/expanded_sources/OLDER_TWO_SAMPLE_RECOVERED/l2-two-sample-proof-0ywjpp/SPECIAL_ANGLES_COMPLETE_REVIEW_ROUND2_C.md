# Independent adversarial mathematical review — Round 2 C

## Verdict and exact scope

**PASS for the stated two-input, two-hidden-layer theorem with arctangent activations and input correlation \(\rho\in\{0,-1\}\).** I found no required mathematical correction after auditing the entire document, including the construction and convergence arguments on which its nontriviality conclusions depend.

This verdict includes the specified parameter metric and physical clock, the canonical generated-space operator and its actual adjoint, existence and restart uniqueness on every finite horizon, the complete stated observable contract, distributional nonaffinity at every finite time, strictly positive hidden and readout speeds at every positive time, and the calculation of the full label-direction kernel. It is not a verdict for intermediate correlations, other depths, a different descent metric, arbitrary width-dependent probes, arbitrary bounded initial operators, or an interchange of the infinite-width and infinite-time limits.

The proof does not merely show that the hidden kernel increases: its calculation also includes the readout block. With the document's normalization \(\kappa=\tfrac14 y^TKy\), the verified physical-time expansion is

\[
\kappa(t)=\kappa(0)+32d_*t^2+o(t^2),\qquad d_*>0.
\]

No essential specialized external theorem is imported without proof. The optional wording improvements at the end of this report do not qualify the mathematical verdict.

## Audit provenance, isolation, and source integrity

- Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md`.
- Source length: 1,977 lines; 94,653 bytes. I personally read all lines, including the observable statement, every proof section, and the final scope/provenance record. The portion affected by tool-output truncation was reread explicitly.
- Expected SHA-256: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- SHA-256 before reading/auditing: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- SHA-256 after the complete source audit, immediately before report creation: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.
- SHA-256 after report creation and completion of the mathematical audit: `830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`. The before/after hashes match the requested hash exactly; the source is unchanged.
- The only additional instruction file read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`, used solely for the procedural mathematical-audit requirements. It supplied no mathematical context for this theorem.
- No other project files, mathematical sources, ledgers, reviews, snapshots, dependency notes, or other tasks/conversations were consulted. In particular, none of the four provenance snapshots named at the end of the source was opened.
- No agents, experiments, numerical simulations, external searches, or source edits were used. The mathematical checks below are analytic derivations from the sole source. Tools were used to read that source and the permitted procedural instruction, inspect file metadata and hashes, and create this report using `apply_patch`.
- The requested report path was absent before creation. This report is the only file written.

Line references below refer to the audited source; equation numbers are its equation numbers.

## 1. Model, normalization, and precise theorem contract

**Coverage:** Section 1, lines 12–235, equations (1)–(14).

### 1.1 Parameterization and descent metric

The shapes, initial variances, and prediction normalization are consistent. In particular, the prediction is

\[
f_{n,a}=n^{-1}(W_n^{(3)})^T H^{(2)}_{n,a},
\]

with the readout already expressed in the displayed rescaled coordinates. Differentiating the loss sum gives Euclidean gradients \((2/n)\sum_a r_a\delta^{(1)}_a x_a^T\), \((2/n)\sum_a r_a\delta^{(2)}_a(H^{(1)}_a)^T\), and \((2/n)\sum_a r_aH^{(2)}_a\). The inverse weights of (7) are respectively \(n/d\), \(1\), and \(n\). Their application gives exactly (6), including all factors of two, \(d\), and \(n\).

Thus the stated dynamics really are gradient descent in the stated metric. They would not be ordinary Euclidean descent in the three displayed arrays, and the source explicitly prevents that interpretation. The clock \(t=k n^{-2}\) is used in the discretization estimates and restored after the later local feature-time calculation.

The geometric hypotheses are sufficient: \(d\ge2\) is required and stated for orthogonal inputs; equality in the negative Cauchy–Schwarz bound forces \(x_2=-x_1\) in the antiparallel case. There are no biases that would invalidate oddness-based sample identities.

### 1.2 Two neuron spaces and operator normalization

Both finite neuron spaces use the same normalized inner product \(n^{-1}v^Tw\). Consequently the actual adjoint of a finite matrix between them is its transpose, and its operator norm is its ordinary Euclidean operator norm. An orthonormal basis in a normalized finite space is \(\{\sqrt n e_i\}\); summing the squared output norms on this basis gives the ordinary Frobenius norm squared. Hence (9), including its finite realization \(vh^T/n\), is correct.

This check matters for all subsequent rank updates, transpose regressions, kernel blocks, and Hilbert–Schmidt energies. There is no missing empirical factor in those passages. The theorem properly distinguishes the bounded initial operator from its Hilbert–Schmidt increments; it never assigns a finite Hilbert–Schmidt norm to the limiting initial random-matrix action.

### 1.3 Observable quantifiers

I audited the full statement, rather than interpreting it as convergence of predictions alone. Its obligations are:

| Stated obligation | Proof mechanism checked | Result |
|---|---|---|
| Same-neuron joint laws of both samples and all listed forward/backward fields, separately in each population | Fixed-program law, mesh comparisons, path interpolation, supremum moments | Met |
| Path-space Wasserstein convergence for every fixed finite order | Equations (70)–(74), truncation, and the raw-GD coordinate comparison | Met |
| Joint finite-time continuous polynomial-growth tests | All-order moments and the finite-dimensional empirical law | Met |
| Predictions, loss, and every kernel block uniformly on a fixed horizon | State continuity plus the special product estimate for block 1 | Met |
| Both orientations of every fixed finite admissible probe program, and the stated ordinary-\(L^2\) closures | Canonical adjoint, finite-program identification, truncation, bounded operator action | Met |
| All preactivation/activation velocity laws at fixed times, integrated mean-square comparisons, and uniform quadratic norms | Section 4.4, including the extra integrability step for the second activation velocity | Met |
| Readout and both hidden parameter speeds, their integrals, and parameter-increment quadratic metrics | Metric identities, rank Gram formulas, cross-time contractions | Met |
| Actual Gaussian initial readout and the specified raw interpolation | Stability from zero-readout comparison, followed by (31)–(33) | Met |

The probe statement is intentionally finite-program/approximation based. It excludes unrestricted width-dependent amplification and does not imply convergence on every vector in \(\mathbb R^n\) or operator-norm convergence across dimensions. These restrictions are mathematically material and explicit. There is likewise no asserted artificial neuron matching across the two populations and no continuous-path law claimed for discontinuous mesh velocities.

## 2. Deterministic flow, original-variable uniqueness, and raw GD

**Coverage:** Section 2, lines 237–553, equations (15)–(35).

### 2.1 Special-angle transformation and row reconstruction

Since \(F'(z)=1+z^2=1/\phi'(z)\), \(F\) is a bijection of \(\mathbb R\), and

\[
(F^{-1})'(u)=\phi'(F^{-1}(u)),\qquad
(\phi\circ F^{-1})'(u)=\phi'(F^{-1}(u))^2.
\]

Both maps are 1-Lipschitz. The stated bounds on \(\phi,\phi',\phi''\) hold. The initial transformed root is square integrable: expanding \((G+G^3/3)^2\) gives \(1+2+15/9=14/3\).

For \(C=I\), the first equation becomes \(\dot U_a=c_aQ_a\), with \(c_a=-2r_a\). For \(\rho=-1\), oddness of \(\phi\), evenness of \(\phi'\), and opposite inputs give all of (17) at every raw parameter state, including for a nonzero readout. The reduced control is \(c_1-c_2=-4r_1\). No factor of two is lost by retaining only one independent first coordinate.

Equation (18) reconstructs exactly the changing component of the first row, while retaining its initial component orthogonal to the input span. Orthogonality of the independent input directions gives the stated first-parameter metric. In particular, the antiparallel sample pair must not be counted twice in that metric, and the proof does not do so.

### 2.2 Stability and local construction

I checked each subtraction in (20). For example,

\[
\|\delta_a^{(2)}-\widetilde\delta_a^{(2)}\|_2
\le e_3+M(a_0'e_a+Be_W),
\]

and applying the adjoint and splitting its difference gives

\[
\|Q_a-\widetilde Q_a\|_2
\le a_0'e_3+M(a_0')^2e_a+M(a_0'B+1)e_W.
\]

The rank difference is a sum of two rank-one operators, yielding exactly the coefficients in (20). These estimates do not require an \(L^\infty\) bound on \(Q\), and do not assert that the initial operator acts boundedly on \(L^p\) for \(p\ne2\).

The clipped-readout construction resolves the fact that an \(L^\infty\) ball is not open in \(L^2\). Clipping is Lipschitz, the resulting field is bounded and Lipschitz on a small Banach-space ball, and its integral map is a contraction for short enough time. The direct readout increment bound (21) then makes clipping inactive. The accumulated-action argument applies to integrable controls as stated. Subtraction and the scalar integral inequality give (22), including the comparison with different initial operators and Hilbert–Schmidt differences of their increments.

### 2.3 Global bounds and loss identity

Integrating \(\|\dot W^{(3)}\|_2\le B\sum|c_a|\) gives the first bound in (23). Integrating the rank norm bound \(B\|W^{(3)}\|_2\sum|c_a|\) gives

\[
\|W^{(2)}(t)-W^{(2)}(0)\|_p
\le Bb_2S+\tfrac12B^2S^2.
\]

The transformed first-field bound follows from \(\|Q\|_2\le\|W^{(2)}\|_{\rm op}\|W^{(3)}\|_2\). These estimates ensure a limit in the chosen Banach norm at a finite endpoint of finite action, so the extension argument is valid.

The source supplies the along-curve \(L^2\) chain rule needed to differentiate the prediction; it does not invoke unjustified Fréchet differentiability of nonlinear superposition on all of \(L^2\). Direct differentiation gives all three blocks of (12), and

\[
\dot f=-2Kr,\qquad
-\dot L=4r^TKr
=d\mathbb E_1|\dot W^{(1)}|^2+
\|\dot W^{(2)}\|_{\rm HS}^2+\|\dot W^{(3)}\|_2^2.
\]

Each block is the displayed Gram matrix, hence positive semidefinite. Loss decrease bounds the residual and action, completing global existence on every finite horizon. The zero-readout bounds (26) follow with \(S\le4t\).

Original-variable uniqueness is also discharged. For an original integral solution, Fubini gives scalar absolutely continuous representatives. Applying the scalar chain rule to \(F(Z)\) yields (27) with an \(L^2\) right-hand side. Such a solution therefore belongs to the transformed class, where uniqueness was proved. The same argument applies at every reached state; restart retains the operator, readout, first row, and their joint structure. Opposition is preserved in the antiparallel abstract equations because the two raw first derivatives sum to zero.

### 2.4 Euler comparison, raw discretization, and velocity transfer

The drift and Lipschitz bounds give the local \(O(h^2)\) defect (28), and iteration of the error recurrence gives (29). The first-exit argument is legitimate: through the candidate exit node, the explicit updates give uniform action, readout, and operator bounds, so the comparison estimate is already available there. Its residual cannot be a unit beyond the exact bound when its prediction error is less than \(1/2\).

The exact cubic expansion (30) is correct. In normalized \(L^2\), the quadratic defect is bounded by \(C_T\eta^2\sqrt n\), using \(\|q\|_\infty\le\sqrt n C_T\); the cubic defect is bounded by \(C_T\eta^3n\). Summing over \(O(T/\eta)\) steps with \(\eta=n^{-2}\) gives \(O_T(n^{-3/2})\). The interpolation defect and its derivative have the stated orders. This justifies (31) for the raw parameter interpolation, not just at mesh nodes.

The factor \(\sqrt n\) in (32) is accounted for: multiplying the \(O(n^{-3/2})\) field error by the available \(O(\sqrt n)\) coordinate bound leaves an \(O(n^{-1})\) original first-velocity error. Applying the same product splitting and then (33) gives the stated second-layer velocity errors. The final second gate again multiplies a base-field discrepancy of order \(n^{-3/2}\) by a velocity coordinate bound of order \(\sqrt n\); it does not create an additional uncompensated loss of \(\sqrt n\). Quadratic energies and kernel comparisons consequently transfer.

Finally, the net argument in (34) is correctly normalized: the two \(1/4\)-net approximations cost a factor two in the bilinear supremum, producing the exponent \(-nt^2/8\). At \(t=8\) the exceptional probability decays exponentially. The readout tail estimates (35) follow from variance \(n^{-2}\) and a union bound. All deterministic comparison constants can therefore be chosen on events of probability tending to one under the actual initialization.

## 3. Finite Gaussian programs and the canonical operator

**Coverage:** Sections 3.1–3.5, lines 555–1044, equations (36)–(56).

### 3.1 Causality and formal source conventions

The finite transformed mesh program is exact for the specified Euler dynamics. Its antiparallel off-invariant version is explicitly only an auxiliary program; it is not used as an identity for the raw flow off that invariant set.

In (37)–(39), both forward calls precede the reverse calls at a node. The current first features depend only on earlier reverse answers. The readout at that node also depends only on earlier forward answers. Thus the recursion is causal even though the reverse answer contains current first features.

The formal derivatives are of the complete selected coordinate expression, with deterministic expectations, scalar feedback coefficients, and covariance parameters held fixed. In particular, the past derivative of the readout is present, and the current reverse response is

\[
\beta_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[W_k^{(3)}\phi''(Z^{(2)}_{ka})].
\]

Correlated or identical Gaussian source slots do not acquire artificial cross derivatives merely because of their covariance. This convention is then justified through actual regularized finite programs; it is not simply imposed at singular covariance.

### 3.2 All-order moments for fixed programs

The readout bound (41) is independent of coordinate values and remains valid for the auxiliary perturbed graphs. It permits a smooth clipping extension of the readout factor in \(w\phi'(z)\), making the relevant coordinate operation globally Lipschitz without changing the actual graph. Storing \(F(G)\) as part of the root tuple avoids any false global Lipschitz claim for the cubic root map itself.

The inductive derivative estimates (42) have the correct scaling. A matrix differential contributes \(n^{-1/2}vx\), with Euclidean norm at most \(\|v\|_F\|x\|_2/\sqrt n\); a normalized contraction contributes a factor \(n^{-1/2}\). A scalar-times-vector operation cancels that factor against the vector's \(\sqrt n\) size. This supports the claimed polynomial bounds for the finite graph.

The Gaussian inequality (43) is proved within the source by rotation between two independent Gaussian matrices, integral Hölder, and conditional Jensen. The orthogonal rotation velocity is independent standard Gaussian, which supplies the stated constant. Polynomial domination and the integrated operator tail justify its use here.

The conditional mean argument is essential and correct. Gaussian concentration alone would not control a possibly large root-dependent mean. Permuting two output neurons and the corresponding root/matrix indices gives the difference bound preceding (44). Averaging over the second index and using the normalized norm bound yields (44). Root moments and Hölder then establish (45), including for empirical-feedback graphs. No arbitrary-input \(L^p\) operator estimate is smuggled into this argument.

### 3.3 Conditional matrix law and empirical induction

The conditional mean in (46) satisfies both constraints:

\[
MV=Y,
\qquad
J^TM=P^TP_V+P^TP_{V^\perp}=P^T,
\]

where compatibility is \(J^TY=P^TV\). Its independent Gaussian remainder is the common orthogonal null component. The adaptive-query justification is sufficient: after conditioning on previous answers, each new query is measurable and its observation imposes precisely its new linear constraint.

The regression coefficients, innovation variance, and factor \(1/n\) in the new-answer formula are consistent. The finite-rank projection error (47) tends to zero in every fixed empirical \(L^p\): for \(p\ge2\), the diagonal projection entries satisfy \(\sum_i(P_0)_{ii}^{p/2}\le\operatorname{rank}P_0\); smaller orders follow from the probability-space norm inequality.

After projection removal, conditional coordinate independence gives (48). On bounded coefficient sets, Gaussian integration preserves continuity and polynomial growth of the test. Equation (49) handles its tails and removal of the coefficient truncation. Along with the iid root step, this proves the nonsingular empirical induction, rather than assuming a tensor-program theorem.

For the source form (50), projecting a new input off previous same-direction inputs leaves a cross inner product with the old reverse answers equal to \(\mathbb E[\zeta h_\perp]\). Gaussian integration by parts (51) yields the derivative coefficient. Substitution of the previous forward-answer decompositions cancels the regression correction exactly. The new full Gaussian source is the old-source projection plus the new innovation, so its variance is the full input second moment. It is not a residual variance with a response term subtracted. The same reasoning with the populations interchanged proves the actual transpose rule.

### 3.4 Singular Grams and empirical feedback

Adding an independent \(\epsilon\)-Gaussian root to each queried input gives a Schur complement at least \(\epsilon^2\): its fresh component is independent of both the previous same-direction inputs and the unperturbed current input. This supplies the missing invertibility only in the auxiliary positive-noise program.

The finite coupling bound from (42) and (52) is uniform in width for a fixed graph. Interpolation (53) and higher moments upgrade its normalized \(L^2\) error to every needed empirical order. On the scalar side, the source recursion has no inverse covariance; coefficient and expected-derivative continuity follow through its finite causal construction. Continuity of positive semidefinite square roots is also proved, including at rank drops. These facts justify the order of limits: width first at positive noise, then noise to zero.

The source explicitly retains zero and redundant formal slots. If a derivative ambiguity lies in a covariance null direction, its contraction with the corresponding reverse-input combination is zero almost surely. Thus there is no hidden positive-definiteness assumption in the zero-noise law.

The learned-rank identities (54) are exact. Selecting contractions causally gives the deterministic comparison program, and finite graph subtraction transfers its law to the actual empirical-feedback program. The upgrade to continuous polynomial-growth tests uses already proved moments. The finite-cell coupling argument at lines 950–958 supplies the claimed Wasserstein convergence without importing a separate specialized convergence theorem.

### 3.5 Common spaces, density, adjoint, and canonicity

The countable program construction includes sufficient cylinder functions and both matrix orientations. Inequalities (55) pass from finite Gram convergence and the high-probability norm bound. They imply that a zero-norm relation among inputs has a zero-norm relation among outputs, so the proposed linear maps are well defined before completion.

The density argument is explicit: finite-cylinder events approximate the generated sigma field in measure, threshold rectangles generate finite-dimensional Borel sets, and one-sided smooth approximations handle atoms. Truncation and simple functions then give \(L^2\) density. Extending the two actions by the norm inequalities and passing the bilinear identity to their completions establishes an actual bounded operator and its actual Hilbert adjoint.

Canonicity is appropriately stated for the generated laws/function spaces. Adding unused programs cannot change an earlier finite marginal because that marginal already has a full-sequence finite-width limit. A requested finite or countable probe family can be adjoined compatibly. This is not an assertion of a canonical pairing of finite neurons or a continuum iid matrix kernel.

The deterministic flow can now be constructed on these spaces. Every included mesh satisfies its Euler equations with this same operator, and (56) follows from the earlier deterministic comparison. No width subsequence or independent operator refresh is used to obtain the flow.

## 4. Global response bounds and bounded Gaussian remainders

**Coverage:** Sections 3.6–3.7, lines 1046–1215, equations (57)–(66).

This is a central obligation: without it, the later Gaussian-tail argument would not follow merely from bounded operator norms or \(L^2\) stability. I checked the forcing argument separately from the primal flow construction.

Equation (57), the bound on the total absolute mesh controls, and the rank equation give state bounds depending only on the fixed horizon, not on the number of mesh calls. For the auxiliary antiparallel program, retaining both transformed sample coordinates and using \(\|C\|\le2\) gives the needed Lipschitz estimate even when forcing leaves the invariant set. The source explicitly avoids identifying that off-invariant auxiliary program with raw dynamics.

Inserting \(\epsilon e\) into one complete reverse answer affects the first state update with a factor \(h_s\). Multiplying subsequent factors \(1+C_Th_k\) gives (58). Inserting it into one complete forward answer changes current features, deltas, predictions, and reverse answers by \(O(|\epsilon|\|e\|_2)\), but changes the future state only through a step multiplied by \(h_s\); this gives (59). The direct current delta response has size at most \(M_T\), and the other current sample has no direct delta change. Feedback and learned-rank changes are included in these estimates.

For a fixed mesh and nonzero forcing, the already established finite-program law applies jointly to forced and unforced runs. In the relevant population, the new independent root enters the selected scalar expression only through the forced source slot. The selected coefficients may depend on \(\epsilon\), but are constants with respect to that neuron's fresh root. Therefore

\[
\mathbb E[eX^\epsilon]
=\epsilon\mathbb E[\partial_{\rm slot}X^\epsilon],
\qquad
\mathbb E[eX^0]=0.
\]

The finite Cauchy–Schwarz inequality and (58)–(59) bound the left side by \(C_Th_s|\epsilon|\) for past slots. Only after taking the width limit does the proof send \(\epsilon\) to zero, using the finite scalar recursion's derivative continuity. This identifies exactly the coefficients in (38), including slots with zero unforced variance. The method consequently does not infer a transverse derivative from a singular unforced distribution alone.

Adding the learned terms gives (62). Their absolute row sums are bounded because past coefficients are \(O(h_s)\), the total mesh length is bounded, and current coefficients have their separate diagonal bound. Multiplying these rows by bounded first features or bounded second deltas gives (63); integrating the transformed first equation gives (64).

The passage to the flow is on the already constructed common space. The cross-program covariance rule gives the Gaussian isometries (65), so mesh convergence of the input fields yields convergence of the Gaussian sources. Subtracting from the convergent fields preserves an essential bound on the remainders. The integral in the first-layer representation is the \(L^2\) limit of Gaussian sums and remains Gaussian and independent of the first-row roots. Thus all of (66), including its exact covariance formulas and first-root independence, are proved.

The exceptional-set formulation is sufficient. The later arguments need the decomposition almost surely at each deterministic time and product-almost-everywhere for integration; they do not need an unproved common pointwise realization at every time. Uniform bounds here are bounds over a fixed finite horizon and may depend on that horizon.

## 5. Complete observable-limit audit

**Coverage:** Section 4, lines 1217–1491, equations (67)–(76).

### 5.1 Products and path supremum moments

Equation (67) is the correct replacement for a false general \(L^2\)-Lipschitz product estimate. Splitting at \(|b|=R\) bounds the small-field part by \(R^2\|a-a'\|_2^2\) and the tail by \(4M^2\mathbb E[|b|^2\mathbf1_{|b|>R}]\). The fixed-field consequence for bounded multipliers converging in measure is also valid. This covers population product continuity without assuming \(Q\in L^\infty\).

The radial matrix clipping in (68) is used only to prove moment bounds and equals the original matrix with probability tending to one. Its 2-Lipschitz operator-norm estimate implies a \(2/\sqrt n\) bound with respect to unscaled Gaussian matrix entries. Flow stability therefore makes each coordinate path-supremum functional Lipschitz with a constant independent of width: the coordinate extraction factor \(\sqrt n\) cancels the normalized input factor.

This coordinate Lipschitz estimate alone would not control its mean. The source additionally proves (70) using absolutely continuous representatives, the integral triangle inequality, and bounded \(L^2\) derivatives. The derivative formulas (71) use only bounded readout/gate multipliers and bounded \(L^2\) operator action. Applying the same conditional concentration and permutation-mean argument as before gives (72).

The argument extends to Euler paths with constants uniform over small meshes. Clipping the actual initial readout to \([-1,1]\) for this estimate supplies a bounded extra root, with clipping absent with high probability. First-layer deltas inherit the supremum bound from \(|\delta^{(1)}|\le|Q|\), and the first row follows from (18). No clipping becomes part of the claimed model.

### 5.2 Fixed-time laws and both probe orientations

At a fixed mesh, \(\delta^{(1)}\) is already a continuous polynomial-growth test of identified nodes. To use gated \(Q\) as an input to another matrix action, the source smoothly truncates \(Q\), applies the finite-program theorem to that globally Lipschitz instruction, and removes truncation in normalized \(L^2\) using (45) or (72). The operator norm controls the output error. This establishes the needed unbounded velocity probes without an arbitrary-input \(L^p\) estimate.

The width/time passage uses a legitimate three-part comparison: finite GF to a fixed mesh, the fixed-mesh empirical limit, and the population mesh to the common-space flow. The mesh is chosen before the width, giving full-sequence convergence in probability. Products and polynomial-growth tests are then handled by the established integrability estimates.

Restoring the actual initial readout uses the same two Gaussian matrices and first-row roots. Its normalized initial size tends to zero, and (22), (35), and the product estimates transfer the fields. Thus the zero limiting readout is justified as a limit of the specified nonzero finite initialization.

A general fixed admissible probe family can be inserted into a joint finite graph after the comparison mesh; an admitted limit of such probes is covered by its explicit uniform normalized-\(L^2\) approximation property. Both orientations are supported by the actual adjoint construction. There is no extension here to arbitrary width-dependent directions.

### 5.3 Path laws and uniform scalar outputs

The source does not confuse \(\sup_t\|X_n(t)-X(t)\|_2\) with an \(L^2\) norm of the coordinatewise path supremum. Instead, (74) directly bounds a scalar path's interpolation error by its integrated squared derivative. Averaging supplies a path-space transport bound. Fixed-grid convergence and refinement then give the joint same-neuron Wasserstein-2 path law for (69).

Multiplication is continuous on the finite-dimensional continuous-path space. Together with the supremum bound on \(Q\), this extends the joint path law to \(\delta^{(1)}\). Larger moments in (72) supply the tail control for every fixed finite Wasserstein order, including unbounded first-row coordinates reconstructed by (18).

Predictions and kernel blocks 2 and 3 have direct uniform \(L^2\) continuity on the state bounds. Block 1 additionally uses (67) and the uniformly integrable squared supremum of \(Q\). Finite endpoint contractions and the state time modulus control fixed-mesh interpolation. This establishes uniform convergence of predictions, loss, and all three blocks.

### 5.4 Velocities, integrability after a matrix action, and energies

The transformed vector field converges uniformly in normalized \(L^2\) under mesh comparison. The first two velocity formulas in (73) follow through the gated-product estimate and \(Q\) supremum integrability. The rank and readout velocities use the Lipschitz state estimates. Subtracting the operator and input in

\[
\dot Z^{(2)}=\dot W^{(2)}H^{(1)}+W^{(2)}\dot H^{(1)}
\]

then controls the second preactivation velocity in \(L^2\). Its law is identified by the preceding truncated-query construction.

For the second activation velocity, boundedness of the operator alone would not give the needed uniform integrability of \(\dot Z^{(2)}\) coordinates. The extra argument at lines 1436–1454 fills precisely that obligation. At a fixed comparison mesh, there are finitely many velocity laws with Wasserstein-2 convergence. Inequality (75) transfers their square-tail control to the uniformly \(L^2\)-close exact velocities. A finite cover of the continuous population \(L^2\) curve gives the population counterpart. Only then does (67) justify the last gate multiplication in (73).

The order of limits in lines 1419–1434 and 1448–1454 is sufficient for a supremum-in-time normalized error in probability. Integrated mean-square comparison follows by multiplying its square by the fixed horizon. This does not assert a coupling of finite neuron labels with population labels.

The first parameter speed follows from the independent-coordinate identity (18); the middle squared speed is exactly the rank Gram expression (76); the readout speed is its normalized field norm. Uniform norm convergence gives the requested energies. For increments, the first and third parameters are covered by their field/path laws, and the middle increment is a Hilbert–Schmidt integral with a uniform modulus of continuity. Finite rank-sum approximations reduce its squared norm to cross-time contractions, which have already been identified.

Finally, the raw-GD comparisons transfer the whole contract, not merely fixed-time predictions. The base-field error \(O_T(n^{-3/2})\) in normalized norm bounds every coordinate path error by \(O_T(n^{-1})\). For \(\delta^{(1)}\), the product estimate gives a maximal coordinate error tending to zero as well. These same-index couplings preserve every fixed path Wasserstein order. The separately established velocity and quadratic-norm comparisons cover the chosen node conventions and time integrals.

## 6. Nonaffinity at every finite time

**Coverage:** Sections 5.1–5.2, lines 1493–1608, equations (77)–(83), and obligation (14).

The reflection (77) swaps equal-norm inputs. The parameter map (78) swaps forward sample fields and negates the readout and swapped backward fields. The residual transformation uses the opposite labels. Direct substitution in the updates verifies equivariance, and the Gaussian initialization law is invariant. Passing the finite symmetry through the deterministic full-sequence limit gives (80).

For orthogonal inputs this is a law symmetry, not a false assertion of finite pathwise antisymmetry. The equal velocity norms used later are justified by convergence of the corresponding finite squared norms. For antiparallel inputs, the stronger pathwise identities really do hold.

The first-layer tail argument uses more than a mere \(L^2\) perturbation bound. In (81), the added Gaussian integral is independent of the entire initial first row, and the remainder is essentially bounded. At a fixed time, bounding the finitely many Gaussian integrals on a positive-probability event and independently taking sufficiently large positive or negative initial Gaussian coordinates forces either tail of \(Z^{(1)}\). Dependence of the remainder on those variables cannot defeat the deterministic remainder bound.

At \(\rho=0\), independent \(G_1,G_2\) allow all four sign patterns simultaneously. The first features therefore approach all four saturation corners. If a linear combination vanished almost surely, it would vanish at both \((B,B)\) and \((B,-B)\), forcing both coefficients to be zero. Thus \(\Gamma_1(t)\) is positive definite at every finite time. At \(\rho=-1\), the source correctly uses a rank-one Gram and only needs the nonzero norm of the independent feature.

The exact source variance in (66) is consequently positive for each second-layer sample. Since \(Z^{(2)}=\xi+S\) with bounded \(S\), the event inclusions in (83) give both unbounded tails. No independence between \(\xi\) and \(S\) is needed.

Finally, unbounded tails imply positive variance and hence a nonsingular Gram for \(1,Z\). Their affine span is closed in \(L^2\). If the infimum in (14) were zero, an affine fit would attain zero error. Boundedness of \(\arctan\) on an unbounded tail forces its slope to be zero; strict monotonicity would then force \(Z\) to be constant. This contradiction proves a strictly positive infimum, not just failure of one proposed affine identity.

This argument works at every deterministic finite time, including zero, for both layers and both samples. It does not claim a positive lower bound uniform as \(t\to\infty\), and none is needed by the theorem.

## 7. Persistent nonlazy behavior and every individual speed

**Coverage:** Section 5.3, lines 1610–1708, equations (84)–(90).

From the exchange law, \(r=(f_1-1)y\). Multiplying \(\dot f=-2Kr\) by \(y^T/2\) gives

\[
\dot f_1=(1-f_1)y^TKy=4(1-f_1)\kappa.
\]

The finite-horizon bounds make \(\kappa\) integrable. Thus (85) gives \(1-f_1(t)>0\) at every finite time. At zero, the initial second-layer covariance is \(mI\) in the orthogonal case and the appropriate opposite Gaussian pair in the antiparallel case. Hence the initial contrast feature is nonzero and \(\kappa(0)>0\). Continuity first makes \(f_1>0\) near zero; nonnegativity of \(\kappa\) then preserves \(0<f_1<1\) for all positive finite times. This does not assume a positive kernel lower bound for all time.

The positive prediction forces \(W^{(3)}\ne0\). Because \(\phi'\) is strictly positive at every finite argument, each \(\delta^{(2)}_a\) is nonzero. Its nonzero norm is the exact variance of \(\zeta_a\), and the bounded-remainder representation then prevents \(Q_a\) from vanishing. Multiplication by the positive first-layer gate and the nonzero residual coefficient proves each first preactivation speed is positive. A second positive gate proves each first activation speed is positive, and (18) proves the first parameter speed is positive.

For the middle parameter, (89) integrates the positive-definite first-feature Gram against the pointwise vector \((y_a\delta^{(2)}_a)_a\). The lower bound is strictly positive. In the antiparallel reduction, the velocity is a nonzero rank-one operator. Thus cancellation of the two sample ranks is excluded in both geometries.

Strictness of an individual second preactivation velocity does not follow just from the positivity of a parameter speed. The source instead proves the exact identity (90). Its first contribution is the Hilbert–Schmidt inner product of \(\dot W^{(2)}\) with itself. Moving the remaining contribution through the actual adjoint gives

\[
\sum_a c_a\mathbb E_1[\delta^{(1)}_a\dot Z^{(1)}_a].
\]

For \(C=I\), this is the sum of the independent first-field squared speeds. For opposite inputs, it is exactly one squared speed because the coefficient is \(c_1-c_2\); there is no extra factor two. The positive right side of (90) forces at least one second preactivation speed to be nonzero. The previously justified equal-norm exchange law then forces both to be nonzero. Strict positivity of the second gate gives both activation speeds.

The readout velocity is \(2(1-f_1)(H^{(2)}_1-H^{(2)}_2)\). If it vanished, the contrast feature would vanish, contradicting the positive contrast prediction. All speeds are continuous in their stated norms, so their energies are positive on each positive-time interval of positive length. Their limiting hidden values at zero are zero because the readout and backward fields are zero there. All stated persistent-motion obligations are therefore met, without conflating parameter motion with individual feature motion.

## 8. Reused-transpose law and full-kernel expansion

**Coverage:** Sections 5.4–5.5, lines 1710–1938, equations (91)–(107).

### 8.1 Initial return law

The readout coefficient \(\widehat W^{(3)}\) in (91) is bounded and nontrivial. For the return law, conditioning on the initial first features and their forward answers gives a mean

\[
\mathsf H\Gamma_n^{-1}
\bigl(\mathsf Z^T\widehat{\boldsymbol\delta}/n\bigr)
\]

and an independent projected Gaussian remainder with row covariance \(\Sigma_n\), as in (94). This has the correct factor \(1/n\) in both contractions. The reduced initial feature Gram tends to \(mI\) or \(m\), so its inverse is bounded with high probability.

The deltas are bounded, but \(\mathsf Z\) is not. The proof correctly uses Gaussian moments for the latter contraction. The finite-rank projection can be removed in empirical \(L^p\) by (47). The resulting covariance of the fresh return Gaussian is the full second moment of the delta; subtracting a regression variance here would be erroneous. Equations (92)–(93) are therefore correct for the actual reused transpose.

For orthogonal inputs, \(\widehat W^{(3)}\) is nonzero away from a null diagonal of a full-support Gaussian pair. A vanishing linear combination of the deltas would imply \(\lambda_1\phi'(u)+\lambda_2\phi'(v)=0\) on the off-diagonal support; varying one coordinate forces both coefficients to vanish. The return covariance is positive definite, in particular with positive diagonals. The antiparallel one-variable delta is nonzero except on a Gaussian null set. Conditioning on the first row and using the independent Gaussian return component proves (95).

### 8.2 Feature time and leading velocity coefficients

The auxiliary time \(s\) satisfies \(ds/dt=4(1-f_1)>0\) and \(s(t)=4t+o(t)\). Dividing the physical controls by this derivative gives the factors \(y_a/2\) in the orthogonal system (97), and coefficient one in the antiparallel reduction. These are the gradient equations of the prediction contrast in the same parameter metric.

The integral readout equation and bounded-gate product convergence give (98) strongly in \(L^2\). Operator-norm continuity and rank convergence then give (100). In particular, at orthogonal inputs the rank contribution to the second preactivation coefficient is

\[
\frac12\sum_b y_b\widehat\delta_b^{(2)}
\mathbb E[\phi(G_b)\phi(G_a)]
=\frac12y_a m\widehat\delta_a^{(2)},
\]

which agrees with (99). The other contribution is the initial operator applied to the gated first-layer coefficient. These limits require only along-curve and bounded-multiplier arguments already supplied, not a second Fréchet derivative on the whole \(L^2\) state space.

Writing

\[
A_a=\|\phi'(G_a)\widehat Q_a^{(1)}\|_2^2,
\qquad D_a=\|\widehat\delta_a^{(2)}\|_2^2,
\]

the orthogonal constant is \(d_*=\tfrac14\sum_a(A_a+mD_a)>0\). The actual adjoint gives

\[
y_a\langle\widehat\delta_a^{(2)},\widehat v_a^{(2)}\rangle
=\tfrac12(mD_a+A_a),
\]

which is (102). For the antiparallel reduction, \(d_*=A_1+mD_1>0\) and \(\langle\widehat\delta_1^{(2)},\widehat v_1^{(2)}\rangle=d_*\). The independent-coordinate metric explains the different prefactors in (101) and (103).

### 8.3 Both hidden and readout contributions

The label-direction hidden kernel is exactly the squared feature-time hidden parameter speed:

\[
\kappa_{\rm hidden}
=\sum_{a=1}^{m_\rho}\|(Z_a^{(1)})'\|_2^2
+\|(W^{(2)})'\|_{\rm HS}^2.
\]

The leading velocity limits therefore give \(\kappa_{\rm hidden}=d_*s^2+o(s^2)\).

For the readout block, let \(A(s)=(H_1^{(2)}-H_2^{(2)})/2\). Differentiating \(\|A(s)\|_2^2\) gives exactly (105), with no missing factor two. Dividing by \(s\) and using the strong limits gives

\[
\lim_{s\downarrow0}\frac{\kappa_{\rm readout}'(s)}s
=\sum_a y_a\langle\widehat\delta_a^{(2)},\widehat v_a^{(2)}\rangle
=2d_*.
\]

For antiparallel inputs the two sample contributions are equal and their sum is also \(2d_*\). Integrating yields

\[
\kappa_{\rm readout}(s)=\kappa(0)+d_*s^2+o(s^2),
\qquad
\kappa(s)=\kappa(0)+2d_*s^2+o(s^2).
\]

Thus the hidden and readout changes have the same positive coefficient; the readout block cannot cancel the hidden increase. Substituting \(s(t)^2=16t^2+o(t^2)\) gives the physical coefficient \(32d_*\) in (107). For the unnormalized quadratic form \(y^TKy=4\kappa\), the corresponding coefficient would be \(128d_*\); there is no discrepancy because the source explicitly defines its \(\kappa\).

The positive quadratic expansion proves nonconstancy on every sufficiently short interval beginning at zero. It does not establish or assert monotonicity of the full kernel for all positive times.

## 9. Hypotheses, external results, and adversarial failure modes

**Coverage:** Also includes Section 5.6, lines 1940–1977, and its scope limitation.

The hypotheses needed at the main transitions are supplied within the document:

| Potential missing hypothesis or failure mode | What prevents it here |
|---|---|
| Singular antiparallel input or query Grams | One independent physical coordinate; noisy-query proof; retained zero/redundant source slots |
| Wrong descent metric or lost empirical normalization | Explicit metric (7), normalized rank operators, and checked gradient/adjoint formulas |
| Open-set failure for bounded readout states in \(L^2\) | Clipped locally Lipschitz field followed by the direct readout bound |
| Uniqueness only for transformed solutions | Scalar representatives and (27) place original solutions in that class |
| Finite-time blowup or unbounded residual action | Exact loss balance, bounded activations, and (23)–(26) |
| Treating a reused transpose as independent | Conditional projection proofs (46), (50), and (94) |
| Formal derivatives unjustified off singular Gaussian support | Actual fresh-root forcing, with width and forcing limits taken in the stated order |
| Extending a short-time response bound to arbitrary finite times without control | Uniform-in-mesh state bounds and \(O(h_s)\) response estimates on each fixed horizon |
| Gaussian-plus-remainder tails destroyed by cancellation | Essentially bounded remainders, not merely \(L^2\) remainders |
| Hidden first-feature rank loss at positive times | Four-corner support argument at \(\rho=0\), nonzero reduced feature at \(\rho=-1\) |
| Zero residual at a finite time | Exponential identity (85) and bounded finite-horizon kernel |
| Parameter motion without individual feature motion | Nondegenerate reverse sources, (89), the adjoint identity (90), and exchange of velocity norms |
| Infimum of affine-fit errors zero without exact affinity | Closedness of \(\operatorname{span}\{1,Z\}\) in \(L^2\) |
| Operator \(L^2\) bounds incorrectly promoted to arbitrary \(L^p\) bounds | Gaussian-program moments, truncation, and the extra square-tail transfer (75) |
| Fixed-time convergence incorrectly promoted to path convergence | Integrated derivative interpolation estimate (74) and path supremum moments |
| Gaussian initial readout silently replaced by zero | Explicit same-initial-matrix comparison and restoration of the actual readout |
| Raw parameter interpolation replaced by recomputed Euler coordinates | Cubic interpolation defect and derivative estimates in Section 2.4 |
| Positive hidden-kernel change canceled by the readout block | Direct calculation (105)–(107) of both contributions |
| An all-angle conclusion from special-angle cancellation | The source explicitly displays the uncontrolled intermediate-angle multiplier and declines that conclusion |

The argument relies on classical finite-dimensional Gaussian projection, scalar Gaussian integration by parts and tail bounds, basic Hilbert/Banach-space completeness, elementary integral inequalities, Fubini, dominated convergence, elementary finite-dimensional spectral facts, and standard measure approximation. The source provides the specialized statements and calculations needed here: the local contraction construction, chain rule along \(L^2\) curves, concentration inequality, adaptive matrix conditioning, source regression, singular-query removal, density/extension, and finite-cell Wasserstein coupling. I found no essential nonclassic theorem for which an external statement or proof had to be supplied. Consequently no external mathematical source was consulted.

The final provenance list is not used as a premise. All substantive steps assigned to that provenance are reproved in the audited document. The intermediate-angle expression after line 1950 is also correct: the off-diagonal transformed drift contains \((1+(Z_a^{(1)})^2)/(1+(Z_b^{(1)})^2)\), which is not generally a bounded multiplier. The two special-angle arguments do not control it.

## 10. Required corrections and optional clarity

**Required mathematical corrections: none identified.** No missing hypothesis or unproved essential obligation was found for the stated \(\rho=0,-1\), \(L=2\) theorem.

The following are optional wording improvements only:

1. At lines 1211–1213, replace “Essential remainder bounds are uniform in the horizon” with “Essential remainder bounds are uniform over time in each fixed finite horizon.” The surrounding formulas consistently use \(C_T\), so the intended dependence is already clear; this would prevent a reader from mistaking it for a bound independent of \(T\).
2. At lines 1705–1707, “an interval of positive length contained in \((0,\infty)\)” would be more literal than “any nonempty positive-time interval” when discussing positive integrated energy. The proof establishes positivity for nondegenerate intervals; a singleton has zero time integral. This is a prose clarification and does not affect the theorem's speed assertions or its stated energy-convergence contract.
3. Near the probe statement, an explicit reminder that any requested finite/countable probe family is incorporated by the compatible enlargement in Section 3.5 could help distinguish this construction from an assertion about arbitrary unqueried width-dependent directions. The present definition and proof already make that distinction.

## 11. Complete coverage record

All equation groups were audited, not just the emphasized conclusions:

| Equations | Obligations covered |
|---|---|
| (1)–(14) | Inputs, initialization, prediction and backward fields, raw updates, metric, operator norms, population equations, complete theorem contract |
| (15)–(22) | Special-angle transformation, antiparallel reduction, reconstruction, local \(L^2\) stability and existence |
| (23)–(27) | Global extension, chain rule, kernel/energy identity, original-variable uniqueness and restart |
| (28)–(35) | Euler error, first-exit closure, raw-GD defect and interpolation, velocity comparisons, high-probability initial bounds |
| (36)–(45) | Fixed meshes, causal scalar source law, derivative convention, all-order moments and Gaussian concentration proof |
| (46)–(53) | Adaptive conditioning, projected innovations, empirical tests, response derivation, singular-query removal |
| (54)–(56) | Learned-rank terms, empirical feedback, Wasserstein law, common spaces, bounded operator/adjoint, canonical flow |
| (57)–(62) | Horizon bounds, actual fresh-root forcing, coefficient extraction, summable global response rows |
| (63)–(66) | Bounded remainders, exact Gaussian covariances, common-space completion and Gaussian first-layer integrals |
| (67)–(72) | Product continuity, harmless moment-estimate clipping, uniform path moments and actual-readout integrability |
| (73)–(76) | Both-orientation velocity probes, path interpolation, extra square-tail control, speeds, energies and increments |
| (77)–(83) | Finite-law exchange, deterministic symmetry, all-time tails, first-feature Gram, nonaffinity |
| (84)–(90) | Residual positivity, nonzero readout/deltas/reverse fields, every hidden/readout speed, cancellation identity |
| (91)–(95) | Initial reused-transpose law, normalization, return covariance nondegeneracy |
| (96)–(103) | Feature-time normalization, strong leading velocity limits, both special-angle positive constants |
| (104)–(107) | Separate hidden and readout expansions, full-kernel coefficient, return to physical time |
| Final scope/provenance paragraphs | Explicit exclusion of all-angle, other-depth, infinite-time-interchange, and refreshed-restart conclusions; no imported snapshot premise |

**Final mathematical verdict: PASS, restricted to the precise \(\rho\in\{0,-1\}\), two-hidden-layer theorem and observable scope stated in this source.**
