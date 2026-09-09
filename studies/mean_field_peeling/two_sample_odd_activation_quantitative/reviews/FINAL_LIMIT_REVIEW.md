# Independent complete-proof audit: quantifiers, source identification, and limits

Date: 2026-09-07.

**Verdict: PASS.** For the four candidate files at the SHA-256 hashes below, I found no missing hypothesis or invalid limit exchange preventing the stated complete two-input theorem with

\[
0<e\le c_{\rm poly}\delta^{800},\qquad 1/2\le a\le1.
\]

This verdict concerns the complete assembled theorem, including the nonlinear response argument and the population/GF/raw-GD bridges. It is not merely approval of polynomial affine bounds. It does not assert optimality of the exponent or sufficiency of an exponent such as two.

I read CONTRACT.md, CANDIDATE_HASHES.json, and all four mathematical candidate files in full. I used the solve-math-rigorously skill. I inspected the mathematical source arguments listed below, particularly the finite Gaussian conditioning and common-action construction, the affine probe identity, the controlled source equations, the cap/physical/GD bridge, and the complete fixed-cap velocity bridge. I did not consult preliminary, sibling, or historical reviews, status records, or conversations. No experiment, delegation, source edit, or commit was performed. The only write is this report.

## 1. Exact candidate hashes

These hashes were computed from the files, rather than copied without verification. All four match CANDIDATE_HASHES.json.

| File | SHA-256 |
|---|---|
| PROOF.md | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |
| AFFINE_POLYNOMIAL_BOUNDS.md | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` |
| POLYNOMIAL_RESPONSE_LEMMA.md | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` |
| OLD_THRESHOLD_AND_NONAFFINITY.md | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` |

## 2. Affine geometry and coefficient arithmetic

The normalization retains the original metric. Since the active input has squared norm divided by dimension equal to v, the change p=P_1/sqrt(v) has unit raw metric; directions orthogonal to that input do not enter the affine objective, even at nonsymmetric nearby states. Thus the factor lambda=a^3 sqrt(v) in the raw Hessian is legitimate. It is not a change of the optimizer.

The three operator balance identities differentiate correctly on the bounded canonical actions. Their use does not take an infinite-dimensional trace. They yield the stated operator bounds and

\[
\dot F\ge2c^4(1+c^2),\qquad
F^2\ge\tfrac23c^6+\tfrac12c^8.
\]

Radial convexity supplies c' at least one in normalized time, and c' at least c^3/sqrt(2). These bounds give the finite first-hit interval and logarithmic integral of curvature. A bounded raw vector field on a finite interval supplies a strong endpoint; local polynomial-field existence gives the required continuation. Hence the argument does not assume existence through its target.

The comparison splits the nonlinear field at the same state and differentiates only the affine field. The cap-independent forcing bound 40 e b^3 therefore combines with the integrated affine Hessian rather than a cap-dependent nonlinear Hessian. The stated powers lambda^-3, lambda^-7/2, and lambda^-11/4 follow from this comparison and the forward product estimates.

The nonaffinity improvement also checks out. Radial growth and the balances imply ||BAp|| at least one and ||Ap||^2 at least 1/101. The original source proof supplies both Gaussianity and inactive-field freezing; bounded operator norms alone would not supply either fact. Consequently the actual sample variances have the stated absolute lower bounds. The Hermite identities, their signs, the explicit eta_* constant, and the 1-Lipschitz property of the square root of the regression residual are valid. No inverse perturbed variance is needed.

The assembled polynomial input exponents are consistent. In particular b_delta^2 G_delta has order delta^-7/8; its row sum costs delta^-1/2; and a learned-moment difference costs b_delta^3 E, hence delta^-15/8 times e before its time weight. The backward sum is explicitly paid as B^2 e in the response lemma. All input exponents are at most two. The displayed C_B has ample coefficient slack for the enumerated factors. Thus B_delta=C_B delta^-2 and the source restriction imply precisely

\[
10^{-70}B_\delta^{-400}
=10^{-70}C_B^{-400}\delta^{800}.
\]

Taking the minimum with c_* and 1/4 preserves the primal, endpoint, nonaffinity, gain, and convex-mixture restrictions. The quantification of the old conservative selection is correctly presented as an upper bound on that selection, not as a necessary restriction on successful activations.

## 3. Enlarged initialization and the actual source inverse

The enlarged-scale argument supplies a genuine input to the source proof. Scaling all hidden initial parameters and retaining the zero population readout gives the homogeneous affine trajectory beta Theta_1(beta^2 t). The continuation interval beyond the original target is longer than the additional interval needed by beta_*^2 T. Its extra integrated curvature is bounded. The identity is used for continuous affine trajectories; the proof does not incorrectly assert exact time-dilation covariance for Euler on a fixed mesh.

For sufficiently fine Euler meshes, the same deterministic raw comparison has a fixed margin. This can be seen by strong Euler approximation and convergence of the integrated Hessian bound: in a radius-one tube each discrete propagation factor is bounded by 1+h_j L_j, and their product is bounded by exp(sum h_j L_j). This argument is uniform over source positions and preserves a single forcing factor h_j. There is no minimum-step assumption. Each dataset uses its own affine endpoint; the uniform upper bound S_delta is not used to prolong a trajectory past that endpoint.

The source-versus-raw identification is supplied by the independent Gaussian probe argument, not by naming a raw tangent a source derivative. At a fixed finite mesh and fixed nonzero probe amplitude, common generated actions retain the original and perturbed programs and their adjoints. The deterministic raw comparison bounds the output difference. The finite-program source rule then identifies the pairing with the independent root; only after that identification is the probe amplitude sent to zero by finite-program continuity. This proves the actual named formal derivative coefficient, including off-support source directions. There is no differentiation through a width limit, covariance square root, or increasing transcript.

At matrix variance beta^2 the conditioning formula multiplies the return by beta^2. Indeed the reverse Gaussian covariance is beta^2 times the input second-moment Gram, whereas the conditional mean uses the unscaled input Gram. Gaussian integration by parts therefore leaves exactly the extra beta^2. The mesh, controls, gain, and K1,K3 do not acquire beta derivatives. Scaling the first root affects learned moments. This verifies the factors in the scaled fixed-point equations.

The positivity argument is applicable to the active sector. In normalized active coordinates the affine Euler updates have positive scalar coefficients and use independent centered Gaussian initial variables. Wick contractions of their moment polynomials have nonnegative coefficients. The chronological affine source recursions likewise use nonnegative active integrations and returns. Thus the active learned-moment derivatives with respect to beta are nonnegative. The bound f'(1) at most f(beta_*)/(beta_*-1) applies entrywise, and also to the nonnegative row sums.

I checked the four affine derivative-only maps against the source equations, and differentiated them to obtain the stated coupled Jacobian. The shift removing arbitrary backward forcing is exact, including its current diagonal. The sandwich estimate retains the rightmost h_j factor without bounding a backward entry by h_j. The identities FL=F+F B3 V and RF=F+V B3 F explain the needed density bounds. In nonactive sample sectors the two feedback products T X3 T and W X2 W vanish. In the active sector the chronological inverse is positive, and the beta derivative forcing dominates any forward forcing of bounded density. Consequently the polynomial inverse bound controls the full coupled coefficient problem; it is not merely a bound on the raw variational propagator.

## 4. Nonlinear response closure

The same-array resolvent step is compatible with the mixed norm. Forward arrays have strict density bounds, while backward arrays are controlled in row norm and may have current diagonals. The products inverted in the source equations are nevertheless strictly causal. The resolvent identities and sandwich estimates provide the needed strict transfers; no inverse of a current backward block is introduced.

The scalar moment argument first uses separately supplied primal bounds to bound each Gaussian source variance. Applying the same-array affine resolvents then leaves an e times X_p term that can be absorbed. This supplies X_p bounded by a fixed polynomial times sqrt(p), independently of cap and mesh. It does not assume that a bounded canonical L2 action preserves Lp tails.

After applying these resolvents to the formal derivative equations, each new feedback term contains e or e Q_r. Terms involving a backward row, such as a B3 DeltaG J, are bounded through that row and a prior derivative maximum; their random unbounded multiplier is not moved to an uncontrolled source-time supremum. Every return to a preactivation goes through a strict transfer. A single reverse-source injection has its own h_j, while complete forward-source rows are measured by their row sum. Both conventions agree with the original source formulas.

The resulting envelope has exponent proportional to e. Jensen in the deterministic time weights and the individual subGaussian bounds control its required fixed moments without a supremum over random source times. Backward output differentiation retains the current (1+e Q_k) factor. The terminal and source multipliers can be kept by fixed-order Hölder; this does not introduce a factor equal to transcript length.

The Taylor remainder and nonlinear derivative defect have sufficient polynomial slack for the stated inequality

\[
D\le2\cdot10^{36}B^{220}e+10^{26}B^{120}D^2.
\]

At the proposed radius d0, the quadratic term is d0/4 and the linear term is strictly smaller than d0/4 under the displayed source threshold. Finite-mesh, fixed-cap amplitude continuity therefore closes the bootstrap. This continuity is a finite causal construction, including at singular covariance, and is not uniform differentiability of a growing transcript. The bound e Lstar S Rstar is also below the stated smallness level. I found no unabsorbed exponential independent of e.

## 5. Complete theorem and order of limits

The original mathematical bridges require bounded primal trajectories, uniform incoming-field tails, and an endpoint above one. The candidate now supplies all three at the polynomial threshold. The original qualitative theorem is a dependency for these bridge arguments; its existence statement alone was not used to validate the polynomial extension.

The asymmetric gate estimate has one linear cap loss on a forward-state discrepancy and uses tails only of the reference. Its error exp(C(1+eR)S-cR^2) tends to zero for each fixed delta,e. It gives strong raw-state and raw-direction convergence, uniqueness against nonsymmetric bounded-primal strong competitors, and restart from reached states. It does not need to impose tail bounds on the competitor.

Population symmetry supplies the scalar clock, while the physical comparison retains both actual residuals. A bounded derivative at the capped first hit is enough for the clock to diverge; capped gradient structure or monotonicity is not assumed. Every fixed physical horizon inherits its cap reference from the same bounded feature interval. Constants in the physical comparison may depend on that horizon, because Gaussian tails defeat exp(C_T R) without another restriction on e.

The finite-limit proof is a triangular argument. Fixed-program convergence is used at fixed cap and auxiliary mesh; exact rank-one unrolling gives a finite operator ball with slack; width-independent deterministic Euler estimates remove the auxiliary mesh. The uncut finite dynamics are compared to the same-width capped reference, and only then is the cap removed. Simultaneous raw GD adds C_{R,T} n^-2 at fixed cap and physical horizon. No theorem for a growing Gaussian transcript is invoked. The finite random readout remains initialized as prescribed; its vanishing population limit does not reset the finite model.

The common-action construction retains both initialized matrix orientations on a countable dense generated family, and passes the finite transpose pairing to true adjoints. Adding the finitely or countably many needed probe programs is permitted by that construction. No assertion of a single simultaneous realization for all real amplitudes, datasets, or horizons is needed for the theorem's quantifiers.

Velocity product queries are first smoothly truncated so that the fixed-program coordinate hypotheses apply. The fixed-cap source proof identifies both appended forward actions and their response terms. For cap removal, the uncut velocity has a continuous L2 time image and hence uniformly vanishing L2 tails on each compact physical interval. The proof sends the cap to infinity at fixed reference-velocity truncation and then removes that truncation; at finite width, width is taken first at fixed cap and truncation. It does not multiply a vanishing cap error by an uncontrolled cap-dependent fourth-moment constant. The recomputed hidden derivatives of the raw GD interpolant, with the prescribed one-sided node convention, are the velocities compared. The path interpolation inequality and integrated squared speeds then give the stated same-layer path-space W2 laws. Products of convergent L2 fields retain all four raw kernels and their off-diagonal entries.

Initial Gram support and the full reused-transpose covariance/return formulas in the original initial-motion lemma apply to every positive e in the new rectangle. They impose no further angle- or horizon-dependent threshold. The convex mixture has a=1-e in the rectangle. The separate Gaussian-unit-energy family also lies in it because 1<D_r<1+r and e_r=r/D_r<r. This does not claim that a nontrivial literal convex mixture itself has unit Gaussian energy.

## 6. Computed hashes of mathematical dependencies inspected

Paths in this table are relative to ../two_sample_odd_activation_theorem/.

| File | SHA-256 |
|---|---|
| PROOF.md | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| AFFINE_CORE.md | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| SOURCE_AND_LIMIT_BRIDGE.md | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| INITIAL_MOTION_AND_NORMALIZATION.md | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |
| sources/TWO_SAMPLE_SOURCE_BASELINE.md | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| sources/L3_LOCAL_COMPLETE_PROOF.md | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| sources/FIXED_CAP_VELOCITY_BRIDGE.md | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |

**Final disposition: PASS for the complete theorem at the recorded candidate hashes. No blocking gap identified.**
