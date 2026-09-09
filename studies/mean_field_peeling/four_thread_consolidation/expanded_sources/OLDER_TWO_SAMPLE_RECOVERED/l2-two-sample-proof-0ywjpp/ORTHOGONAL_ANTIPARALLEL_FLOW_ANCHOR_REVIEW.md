# Isolated adversarial audit of the deterministic two-sample flow anchor

Date: 2026-09-06.

## Verdict and scope

**PASS — scoped conditional deterministic result only. No required mathematical correction found.**

The supplied note establishes the stated orthogonal and antiparallel deterministic physical flows, including existence at all finite times, uniqueness against original ordinary-L2 integral-equation competitors, restart, common-control stability, both operator-norm and Hilbert--Schmidt-increment estimates, transformed Euler convergence, and the same-initialization finite raw-GD/GF comparison and its stated corollaries. The finite Gaussian initialization event also has the stated probability bound. The proof's constants and rates are consistent with its normalization and loss SUM.

This verdict is conditional on a supplied actual bounded population operator. It does not certify a canonical mean-field realization, initialization/reuse laws, convergence across widths, nontrivial learning, distributional nonaffinity, other angles, or another depth. Those are explicitly excluded in the input; their absence is not a defect in this theorem. An arbitrary bounded initial readout is allowed, and actual finite random readouts are retained.

## Isolation and source integrity

The sole mathematical input was:

`/tmp/l2-two-sample-proof-0ywjpp/ORTHOGONAL_ANTIPARALLEL_FLOW_ANCHOR.md`

All 1,015 lines were read. The initial whole-file SHA-256 matched the user-supplied value:

`c3f147633689050f8d9a4749e23861b02640dd7ba0e201b0f05a609b9c76cf39`

The proof-content convention at lines 1006–1015 was independently checked by hashing the first 1,005 lines, including their final newline. It produced the recorded digest:

`3e1da9dc804fc922ece75a1cf66f4cb3290971d99478547de59fa915a9a84af9`

The only procedural skill file read was:

`/etc/codex/skills/solve-math-rigorously/SKILL.md`

That skill supplied the completeness and hypothesis-checking procedure, not mathematical input. No contract, other project file, previous review, history, or external mathematical source was read. References to the contract inside the supplied note were treated as provenance statements, not as additional evidence. No experiments, agents, or candidate edits were performed. Only this review was written, using `apply_patch`. Source readback and hashing are integrity checks, not experiments. A final whole-file hash check is recorded at the end of this review.

## 1. Statement, scalar calculus, spaces, and finite normalization

Source: lines 1–166, equations (1.1), (2.1)–(2.3).

The precise analytic initial conditions are cubic coordinates in H1, a bounded A0:H1→H2, and b0 in L-infinity. These include the stated Gaussian population fields with zero readout, all finite initializations, and every reached restart. No initial first-field maximum is required.

For F(z)=z+z^3/3, F'(z)=1+z^2≥1 and F tends to the corresponding infinities at both ends of the real line. Thus F is an increasing bijection. Its inverse satisfies

\[
g'(u)=\frac{1}{1+g(u)^2}=D(g(u)),\qquad 0<g'(u)\leq1.
\]

Both g and arctan composed with g are 1-Lipschitz; the latter derivative is D(g(u))^2. The bounds |arctan z|≤B=π/2, 0<D≤1, and |D'|≤1 are valid. The Gaussian calculation is also exact:

\[
\mathbb E F(G)^2
=\mathbb E G^2+\tfrac23\mathbb E G^4+\tfrac19\mathbb E G^6
=1+2+15/9=14/3.
\]

On the two probability spaces, bounded activations belong to ordinary L2 with norm at most B. For v⊗w, the operator norm is ||v||2||w||2 by Cauchy--Schwarz and equality in the w direction, and its HS norm is the same by the rank-one formula. These facts require no kernel representation of A.

In normalized finite spaces, v⊗w=vw^T/n. An orthonormal coordinate basis consists of the vectors sqrt(n)e_i, so the matrix of A in these bases is the raw matrix A itself. Consequently the induced operator norm is the usual matrix spectral norm, the adjoint is the actual transpose, and the HS norm is the raw Frobenius norm. No additional n factor is missing in (2.2).

The HS state space is correctly interpreted as the affine class A0+HS, with A−A0 as the Banach coordinate. It does not require A0 to be HS. The operator-norm state space allows arbitrary bounded increments. Comparisons in the HS metric require the compared operator difference to be HS; the note does not assert finite HS distances between arbitrary bounded operators on unrelated spaces.

The input geometries mean ||x_a||^2=d, with normalized inner product zero or minus one. With the displayed independent N(0,1/d) first-matrix entries, the resulting rowwise first-field covariance is precisely C_ab=x_a^Tx_b/d. Thus the stated finite Gaussian pairs are consistent with the geometry. Every finite readout has a finite coordinate maximum, even though no fixed bound applies to every random realization at once; the deterministic constants depend on that realization's initial bounds.

## 2. Orthogonal flow and the physical metric

Source: lines 168–232, equations (3.1)–(3.4).

All fields in (3.1) are well-defined in the asserted spaces. In particular delta2=bD(z2) is in H2, q=A*delta2 is in H1, and delta1=D(z1)q is in H1. Residuals are scalar and are excluded from both deltas.

With C=I, the original first equation is zdot_a=c_aD(z_a)q_a. Multiplication by the scalar derivative F'(z_a) removes D exactly, giving udot_a=c_aq_a. The A and b equations use the same controls. Setting c_a=−2r_a therefore gives the stated physical clock, without rescaling.

The finite normalization can also be verified directly from the prediction f_a=b^Th2_a/n. For L=sum_a r_a^2, its Euclidean gradients are

\[
\nabla_{W^{(1)}}L=\frac2n\sum_a r_a\delta^{(1)}_a x_a^T,
\quad
\nabla_A L=\frac2n\sum_a r_a\delta^{(2)}_a(h^{(1)}_a)^T,
\quad
\nabla_b L=\frac2n\sum_a r_a h^{(2)}_a.
\]

Using the squared tangent metric

\[
\frac dn\|\dot W^{(1)}\|_F^2+\|\dot A\|_F^2+\frac1n\|\dot b\|_{\ell^2}^2
\]

therefore produces W1dot=−(2/d)sum_a r_a delta1_a x_a^T, Adot=−2sum_a r_a delta2_a⊗h1_a, and bdot=−2sum_a r_a h2_a. These agree with the equations written in the input. This checks their internal raw-metric consistency without reading the referenced contract.

For the first-matrix reconstruction, multiplying (3.3) by x_b gives precisely z_b because x_a^Tx_b/d=delta_ab. Its update lies in the input span and leaves the complementary component fixed. Orthogonality also gives

\[
\left\|\sum_a\Delta z_a x_a^T/d\right\|_F^2
=\frac1d\sum_a\|\Delta z_a\|_{\ell^2}^2,
\]

which proves (3.4) for increments and velocities. The first-field metric is a sum over the two independent fields.

## 3. Antiparallel reduction, factor four, and readout

Source: lines 234–330, equations (4.1)–(4.8).

Equality in the input Cauchy--Schwarz relation gives x2=−x1. The first fields are opposite at every raw parameter state. Oddness of both arctans, together with linearity of A and of the readout pairing, propagates opposition through both layers and the prediction. This argument works for every b, including the actual nonzero finite random b0.

Since D is even, delta2_2=delta2_1, q2=q1, and delta1_2=delta1_1. With labels (1,−1), the residuals are exactly (r,−r) and loss SUM is L=2r^2. Thus the effective control is c1−c2. Physical feedback gives c1=−2r and c2=2r, hence c=−4r in all three reduced equations.

There is no missing or extra factor two in the first-matrix metric. Only one independent field is reconstructed: W1−W1(0)=(z1−G1)x1^T/d. Its metric is ||zdot1||_n^2, not twice that quantity.

The three kernel blocks have the displayed sign matrix because C has antiparallel signs, delta fields coincide, and h fields are opposite. Their scalar coefficients are exactly

\[
\kappa_1=\|D(z_1)q\|_2^2,\qquad
\kappa_2=\|\delta\|_2^2\|h\|_2^2,\qquad
\kappa_3=\|k\|_2^2.
\]

Consequently rdot=−4κr and Ldot=4r rdot=−16κr^2. The exponential formula (4.8) has the correct exponent. Finite-horizon bounds proved later ensure the integral of κ is finite, so this formula is valid even when no positive lower bound on κ exists.

At population b0=0, r0=−1; therefore r(t)<0 at every finite time and sdot=−4r>0. This supplies the stated scalar action reparameterization. For arbitrary finite b0, the formula preserves either nonzero initial sign, while r0=0 gives the stationary physical solution. The signed-control formulation covers all cases. Neither monotonic action for arbitrary b0 nor nontrivial learning is claimed.

## 4. Every L2 Lipschitz estimate and local construction

Source: lines 332–453, equations (5.1)–(5.5).

Write x=||u_a−utilde_a||2, e=||A−Atilde||p, and v=||b−btilde||2. Assume both operator norms are at most a and both readout maxima at most M. In either p metric, the operator difference is bounded by e in operator norm.

The estimates in (5.1) follow as follows:

1. The first preactivation and activation differences are at most x by (1.1).
2. Ah−Atilde htilde=A(h−htilde)+(A−Atilde)htilde gives ||z2−z2tilde||2≤ax+Be. The second activation difference satisfies the same bound.
3. Splitting bD(z2)−btilde D(z2tilde) with the unmodified first multiplier on b−btilde gives ||delta−deltatilde||2≤v+M(ax+Be). This uses only a bound on the readouts themselves, not an L-infinity norm of their difference.
4. Splitting A*delta−Atilde*deltatilde gives

   \[
   \|q-\widetilde q\|_2
   \leq a[v+M(ax+Be)]+Me
   =av+Ma^2x+M(aB+1)e.
   \]

5. The rank-one split gives

   \[
   \|\delta\otimes h-\widetilde\delta\otimes\widetilde h\|_p
   \leq B[v+M(ax+Be)]+Mx
   =Bv+M(Ba+1)x+MB^2e.
   \]

   This is equally valid in operator and HS norm.
6. Splitting the final scalar pairing gives |f−ftilde|≤Bv+M(ax+Be).

In the norm of the whole V_a difference, the coefficients of v, x, and e are respectively

\[
a+B,\qquad Ma^2+M(Ba+1)+a,\qquad M(aB+1)+MB^2+B.
\]

Their sum is the displayed L0 and is an admissible common Lipschitz constant. The size bound follows from ||q||2≤aM, ||delta⊗h||p≤MB, and ||h2||2≤B, giving V0=(a+B)M+B. The stated Lf is likewise a valid bound for the prediction estimate. These are conservative constants but correct; none depends on u, n, d, or an initial field maximum.

For physical feedback, splitting rV−rtilde Vtilde gives ((BM+1)L0+V0Lf) times the state distance for each term. Summing the two orthogonal terms with coefficient 2, or using the one antiparallel term with coefficient 4, gives exactly the admissible common constant in (5.3).

### The L-infinity-ball issue is resolved

The original bounded-readout set has empty L2 interior in typical population spaces, so a Banach local-existence theorem cannot simply be applied to it as an open set. Lines 396–428 avoid that error.

Pointwise clipping P_M is 1-Lipschitz on L2 and takes values in the interval [−M,M]. Replacing b by P_Mb in both prediction and delta therefore makes the field locally Lipschitz on the entire Banach state space, with bounds on any ball controlling the operator norm. The readout state coordinate remains b. This works for either operator coordinate, including the affine HS one.

On a small closed ball, the time-integral map has a finite drift bound and a finite Lipschitz bound. Choosing the interval so that drift times length fits inside the ball and Lipschitz constant times length is less than one makes that map a contraction on the complete continuous-path space. For prescribed L1 controls, the same argument uses the integral of the sum of absolute controls. That integral becomes arbitrarily small on sufficiently short intervals. This supplies the stated controlled absolutely continuous solution and autonomous C1 solution.

The readout equation has a bounded integrand in its population coordinate: each h2 is pointwise bounded by B. Its integral therefore has a representative satisfying (5.4), even though the construction was carried out in L2. Equivalently, jointly measurable representatives of the L2 integrand and Fubini give the pointwise bound, which represents the same Bochner integral. This does not require Bochner continuity in the L-infinity norm.

For the clipped physical field, |r_a|≤BM+1 first provides a finite short-time control bound. Taking M>||b0||infinity and then a sufficiently short interval keeps the actual b strictly inside the clipping threshold. The clipped and original fields coincide there. Any other original integral solution beginning with bounded readout obeys its own version of (5.4), so it also belongs locally to a suitable common bounded-readout set. Uniqueness has not been obtained by excluding admissible L2 solutions through an extra topology.

For different prescribed controls, subtracting the equations gives a coefficient L0 times the first control's total variation multiplying the state error, plus V0 times the L1 control difference. Applying the scalar integral majorant yields (5.5). In the reduced geometry this uses |c| and |c−ctilde|. The physical stability estimate follows from (5.3). These comparisons are on identified spaces, as stated; no cross-width coupling is inferred.

## 5. Action bounds, global extension, and dissipation

Source: lines 455–578, equations (6.1)–(6.6).

Put S(t)=integral sum_a |c_a|, or integral |c| after antiparallel reduction. Since ||delta||2≤||b||2, integration gives ||b||infinity≤b_infinity+BS and ||b||2≤b2+BS. The operator derivative has either norm at most B||b||2 times the action density. Thus

\[
\|A-A_0\|_p\leq\int_0^S B(b_2+Bv)\,dv
=Bb_2S+\tfrac12B^2S^2.
\]

Adding ||A0||op gives the operator bound in (6.1). In particular, A0 can remain non-HS: the time integral of the rank-one derivative is an HS increment. The rank-one map is continuous in HS norm along the constructed fields, so this integral exists there and agrees with its operator-norm integral. This also justifies the note's conclusion that the operator-norm construction has HS increments.

For u increments, the integrand is bounded by ||A||op||b||2 times the action density. Expanding the product used in the note gives

\[
(a_0+Bb_2v+B^2v^2/2)(b_2+Bv)
=a_0b_2+(a_0B+Bb_2^2)v
+\tfrac32B^2b_2v^2+\tfrac12B^3v^3.
\]

Its integral is exactly P(S) in (6.2), including the coefficients 1/2 on S^3 and 1/8 on S^4. The z1-increment bound follows from g's Lipschitz constant, and ||z2||2≤B||A||op.

If prescribed controls have finite action on a compact interval, these bounds control all state increments and the local Lipschitz constants. The derivative is bounded by a fixed constant times the L1 action density, making the state Cauchy at any finite putative endpoint. The interval version of (5.4) also makes b Cauchy in L-infinity, so its endpoint remains bounded. Local construction at that endpoint extends the solution. This is a valid Banach-space continuation argument; it does not require compactness of bounded sets.

### Chain rule along L2 paths and exact loss SUM

The note correctly avoids claiming Fréchet differentiability of the nonlinear L2-to-L2 maps. For a C1 L2 path v, replace v(t+h) by v(t)+h vdot(t). The Lipschitz constant of psi bounds the resulting difference-quotient error by a quantity tending to zero. In the fixed direction vdot(t), the scalar quotient converges pointwise and is bounded by ||psi'||infinity |vdot(t)|. Dominated convergence of its square proves (6.3) in L2. Its hypotheses apply to g and both arctans.

Operator multiplication is continuous bilinear in the relevant norms, and the final scalar pairing is continuous bilinear on L2×L2. Differentiation through the layers therefore gives the three contributions displayed after (6.4). Moving A through its actual adjoint is legitimate. The first contribution contains D(z1) twice after substituting zdot, producing the delta1 inner products rather than an undamped q inner product.

Each K block is positive semidefinite: the first is the Gram matrix incorporating the input Gram factor, the second the Gram matrix of the rank-one parameter gradients in HS, and the third a field Gram matrix. Hence

\[
\dot L=2r^T\dot f=-4r^T(K^{(1)}+K^{(2)}+K^{(3)})r.
\]

The three squared raw parameter speeds equal the respective terms 4r^TK^(ell)r. In the orthogonal case the first term is the sum of the two independent squared first-field speeds. In the antiparallel case it is one squared speed: all three terms together give 16r^2κ. This proves (6.5) with precisely the displayed normalized finite metric. The HS norm of Adot is meaningful even when A0 is not HS.

Loss decrease gives ||r||≤R0. Orthogonal action is 2 integral (|r1|+|r2|)≤2sqrt(2)R0t. Antiparallel action is 4 integral |r|, and R0 bounds sqrt(2)|r|, giving the same constant. Integrating the loss identity proves the energy equality and bound in (6.6).

These action bounds make the continuation argument apply to physical feedback on every finite horizon. Also

\[
\kappa\leq\|A\|_{\rm op}^2\|b\|_2^2+B^2\|b\|_2^2+B^2,
\]

which verifies the finite integral needed in (4.8). At each reached time, u remains in H1, A bounded, and b bounded. Reapplying the same construction and uniqueness at that full state proves restart without resetting any field, operator, or readout.

## 6. Uniqueness against arbitrary original-L2 competitors

Source: lines 580–618, equation (6.7).

The stated competitor class consists of original physical integral-equation solutions with the prescribed initial state, continuous L2 fields, and operator-norm-continuous A. No prior assumption F(z(t)) in L2 is made. This is the appropriate integral-solution class; solutions of these Bochner integral equations have the required continuity.

Here is the full reduction, including the potentially dangerous unbounded F':

1. A, z1, and b are locally bounded in their continuous state norms. Bounded Lipschitz activations make h1, z2=Ah1, and h2 continuous in L2. Predictions and residuals are consequently continuous scalars.
2. The readout integral equation implies b has a uniformly bounded L-infinity representative on each compact interval, because the controls are continuous and h2 is bounded pointwise. Thus ||q||2≤||A||op||b||2 is locally bounded and integral |c| ||q||2 is finite.
3. In each independent first coordinate, the raw equation is the L2 Bochner identity z(t)=z(0)+integral cD(z)q. On a probability space, the integral of the L1 spatial norm of this integrand is bounded by the integral of its L2 norm. Fubini therefore provides a representative with absolutely continuous scalar time paths for almost every neuron.
4. The same argument applies to cq. Outside a single null set, both required scalar time integrals are finite. Each scalar z path has a bounded range on a compact time interval. The usual scalar chain rule for the C1 polynomial F along that absolutely continuous path therefore applies. The cancellation F'(z)D(z)=1 gives exactly (6.7), pointwise on those paths.
5. The right side of (6.7) is an L2-valued function, since F(z(0)) is in L2 and integral |c| ||q||2 is finite. Therefore F(z(t)) is automatically in L2 and satisfies the transformed integral equation for every time, with its continuous L2 representative. Transformed uniqueness then identifies the competitor with the constructed flow.

No claim that multiplication by 1+z^2 is bounded on L2 occurs in this argument. It also does not require applying F as a continuous map from all of L2 into L2, or an unproved L6 bound for the competitor.

If both antiparallel sample fields are retained in an abstract population formulation, the two rows of C are negatives. Their first-field derivatives therefore sum to zero before any opposition of the fields is invoked. Initial opposition persists; odd/even activation identities then give the reduction already checked. This avoids a circular symmetry assumption in the uniqueness proof.

Finally, the bounded-multiplier continuity argument at lines 610–618 is sound. For bounded multipliers converging in measure, split a fixed L2 field into a bounded part and an L2-small tail. The product on the bounded part converges in L2, and the tail is uniformly small. Splitting off a varying L2 field proves the corresponding product continuity. This gives continuity of the original hidden-field derivatives and kernel blocks along the physical flow, without requiring the original vector field to be locally Lipschitz on unrestricted L2.

## 7. Transformed Euler consistency and the closed residual bootstrap

Source: lines 620–701, equations (7.1)–(7.3).

On the exact solution's finite-horizon bounds, the physical field has a width-independent size bound V_T and Lipschitz constant L_T. Hence ||Y(t)−Y(s)||≤V_T|t−s|, and integrating ||G(Y(t+v))−G(Y(t))||≤L_TV_Tv gives the coefficient 1/2 in (7.1). This needs no coordinate maximum of q or a hidden field.

For the numerical argument, choose eta≤1 and stop at the first residual index exceeding R=R0+1. Every preceding update has action increment alpha_k=eta sum |c_a,k|, or eta |c_k| after reduction, bounded by 2sqrt(2)R eta. Up to an index at time at most T+eta, the accumulated action is therefore at most S*=2sqrt(2)R(T+1).

The b update gives ||b_k||infinity≤b_infinity+BS* and ||b_k||2≤b2+BS_k. Summing the A updates gives

\[
\|A_N-A_0\|_p
\leq Bb_2 S_N+B^2\sum_{k<N}\alpha_kS_k
\leq Bb_2S_*+\tfrac12B^2S_*^2,
\]

because S_N^2=sum alpha_k^2+2sum alpha_k S_k. The discrete half coefficient is correct in both norms.

Crucially, these bounds include the first candidate exit state: its update is evaluated using the previous, still-admissible residual. The Lipschitz bounds do not depend on the size of u, so a separate bound on a numerical cubic coordinate is not needed. Take a,M large enough for both these numerical bounds and the exact flow through T+1, and use their associated constants in the comparison.

Subtracting the exact endpoint consistency identity from the numerical recurrence gives

\[
e_{k+1}\leq(1+\eta L_T)e_k+C_T\eta^2+\|d_k\|.
\]

Iteration through the stopped candidate index, with e0=0, gives (7.3); at most T+1 units of time and the inequality (1+eta L_T)^N≤exp(L_T(T+1)) suffice. No division by L_T is needed, so the zero-constant case causes no issue.

In both geometries the two-residual error is at most sqrt(2)Lf e_k. For unperturbed Euler, the right side of (7.3) tends to zero as eta does, uniformly in width with the specified initial bounds. Choosing it below 1/(2sqrt(2)Lf) when Lf>0 makes a residual exit above R0+1 impossible. If Lf=0, residual differences vanish directly. This closes the bootstrap rather than assuming numerical stability as input.

Convex interpolation preserves the bounded A and b sets. Endpoint error plus the bounded exact and numerical speeds gives O_T(eta) transformed interpolation error. Piecewise constant Euler velocities are G(Y_k), so comparison with G(Y(t)) and the O(eta) exact motion inside a cell gives the same velocity rate. The proof thus establishes actual untruncated Euler convergence.

## 8. Exact raw-GD defect, all powers of n, and initialization event

Source: lines 703–853, equations (8.1)–(8.8).

The raw first update is Delta z=eta cD(z)q, with c=−2r_a or c=−4r according to geometry. Direct expansion of the cubic gives

\[
F(z+\Delta z)-F(z)
=(1+z^2)\Delta z+z(\Delta z)^2+(\Delta z)^3/3.
\]

The first term is exactly eta cq, not an approximation. Substitution gives precisely (8.2), including the powers of c and D and the cubic coefficient 1/3. The A and b updates already equal their transformed Euler updates evaluated at the same raw mesh state, so their local defects are zero.

Under (8.3), ||q||_n≤A_TM_T=Q. The normalized finite norm gives max_i |q_i|≤sqrt(n)Q. Therefore

\[
\|q^2\|_n\leq\|q\|_\infty\|q\|_n\leq\sqrt n Q^2,
\qquad
\|q^3\|_n\leq\|q\|_\infty^2\|q\|_n\leq nQ^3.
\]

Since |z|D(z)^2≤1 and D≤1, (8.5) follows with its stated constants. No bound on max |z_i| is hidden in this calculation. In both geometries |c|≤4R_T is sufficient; summing at most two independent-coordinate defects only changes a constant.

All three rows of (8.6) check:

| Quantity | Bound before eta substitution | At eta=n^−2 |
| --- | --- | --- |
| One-step defect | O_T(eta^2 sqrt(n)+eta^3 n) | O_T(n^−7/2+n^−5) |
| Sum over O_T(eta^−1) steps | O_T(eta sqrt(n)+eta^2 n) | O_T(n^−3/2+n^−3) |
| One-step defect divided by eta | O_T(eta sqrt(n)+eta^2 n) | O_T(n^−3/2+n^−3) |

Adding the transformed Euler consistency contribution O_T(eta) in (7.3) gives exactly the right side of (8.7). The GF in this comparison starts from the same finite W1, A, and actual b0. Both p metrics are valid because the only defect coordinates are the u coordinates and all operator estimates above apply in both norms.

### Raw-GD residual bootstrap

Assume only ||A0||op≤a* and ||b0||infinity≤b*. Then R0≤sqrt(2)(Bb*+1). Stop the raw iterates at the same residual exit used in Section 7. Their A and b updates are the same ones used to prove the discrete action bounds, so these bounds again hold through the candidate exit. They bound q at every preceding defect-producing state. Equation (8.5), summed only over those steps, supplies the O_T(n^−3/2+n^−3) perturbation term in the stopped version of (7.3).

All constants now depend only on T,a*,b*. For sufficiently large n, the residual error is less than 1/2, contradicting an exit above R0+1. Thus the raw primal bounds and the comparison follow simultaneously. No post-training Gaussian law, a priori residual theorem, numerical loss decrease, or first-field tail event is used. The required T+eta endpoint is covered by the T+1 padding already used in the bootstrap.

### Probability in (8.8)

A maximal 1/4-separated subset of the Euclidean unit sphere is a 1/4-net. Its disjoint radius-1/8 balls fit in a radius-9/8 ball, so it has at most 9^n points. For unit u,v and respective approximants u0,v0,

\[
|u^TAv-u_0^TAv_0|
\leq\|u-u_0\|\|A\|_{\rm op}\|v\|
+\|u_0\|\|A\|_{\rm op}\|v-v_0\|
\leq\tfrac12\|A\|_{\rm op}.
\]

Taking the supremum gives ||A||op≤2max_net |u0^TAv0|. For fixed unit vectors and the stated independent Gaussian entries, that scalar has variance 1/n. The two-sided Gaussian bound follows from the stated moment generating function and Markov's inequality, choosing the optimizing parameter for each sign. A union bound at scalar threshold 4 therefore gives

\[
\mathbb P(\|A_0\|_{\rm op}>8)
\leq 2\,9^{2n}e^{-8n}
=2e^{-(8-2\log9)n}.
\]

The readout has scalar standard deviation 1/n, hence P(||b0||infinity>1)≤2n exp(−n^2/2). Their union bound is exactly (8.8). The exponent 8−2log9 is positive, so this is a probability tending to one. Independence between the two events is unnecessary. Similarly, threshold sqrt(6log n)/n gives the additional bound 2n^−2. These probability estimates concern the finite initialization only and do not establish any population-law identification.

## 9. Actual raw interpolation, original velocities, energies, and paths

Source: lines 855–936, equations (9.1)–(9.3).

### Recomputed cubic interpolation and transformed velocities

On a raw mesh interval let d=Delta z_k and t=k eta+theta eta. The raw first field is z_k+theta d. Subtracting the affine interpolation of its cubic endpoint values gives

\[
F(z_k+\theta d)-[(1-\theta)F(z_k)+\theta F(z_k+d)]
=(\theta^2-\theta)z_kd^2+(\theta^3-\theta)d^3/3.
\]

Thus (9.1) is exact. The absolute values of both theta coefficients are at most one on [0,1], so the same bound as (8.5) applies. The recomputed cubic path is within O_T(eta^2 sqrt(n)+eta^3 n) of the straight endpoint path. Combined with endpoint comparison and O_T(eta) exact motion, this proves the stated continuous-time O_T(n^−3/2) comparison in both p metrics. A and b interpolate linearly and remain in the bounded sets.

Differentiating on an open interval gives

\[
\frac{d}{dt}F(z_k+\theta d)
=cq+2\theta z_kd^2/\eta+\theta^2d^3/\eta.
\]

Both coefficients and powers in (9.2) are correct. The excess over cq is O_T(eta sqrt(n)+eta^2n). A and b velocities are their physical vector fields frozen at the left endpoint. Applying (5.3) between that endpoint and the contemporaneous GF state yields O_T(n^−3/2) for the full transformed velocity error. The right/left mesh-node convention is explicitly stated and sufficient; equality of the one-sided raw-GD derivatives is not needed.

### Positions, predictions, and probes

The maps to z1, h1, z2, h2, and predictions have the Lipschitz bounds in (5.1). On the bounded residual set, loss is also Lipschitz because |r_a^2−rtilde_a^2|≤(|r_a|+|rtilde_a|)|r_a−rtilde_a|. They inherit O_T(n^−3/2) position or scalar-value errors. For any common bounded-norm probe, the forward error is bounded by the operator difference times the probe norm, and the adjoint operator difference has the same operator norm. This verifies both directions of the fixed-width probe assertion without treating the transpose as an independent object.

### Original first velocities

The map D(z)q is not asserted to be dimension-free L2-Lipschitz in both fields. The actual finite estimate is

\[
\|D(z)q-D(\widetilde z)\widetilde q\|_n
\leq\|q-\widetilde q\|_n
+\|\widetilde q\|_\infty\|z-\widetilde z\|_n,
\]

obtained by splitting the q difference and using |D|≤1, Lip(D)≤1. This verifies (9.3).

For the frozen raw first velocity, compare c_kD(z_k)q_k with c(t)D(z_GF(t))q_GF(t). The scalar-control difference times ||q_k|| is O_T(n^−3/2+eta). Equation (5.1) bounds the q difference at the same rate. The remaining multiplier term is at most sqrt(n)Q times the z difference. The latter is O_T(n^−3/2+eta), including exact motion from the preceding mesh time. At eta=n^−2 the resulting total is O_T(n^−1), as asserted. Multiplication by c only changes a horizon constant.

The readout and A velocities retain O_T(n^−3/2) errors in normalized L2 and HS, respectively, because their vector fields are already covered by (5.1). The metric reconstruction (3.4), or its one-field antiparallel version, transfers the first-field velocity error to the appropriately weighted raw first-matrix velocity error.

### Every hidden-field velocity

The instantaneous velocities of both GF and raw interpolation have width-independent L2 bounds. For example, ||zdot1||2≤|c|||q||2, ||hdot1||2≤||zdot1||2, and

\[
\dot z_2=\dot A h_1+A\dot h_1,\qquad
\dot h_2=D(z_2)\dot z_2.
\]

Here ||Adot||op≤||Adot||HS is bounded by the rank-one derivative estimates; ||h1||2≤B and ||A||op is bounded. These identities hold for recomputed raw hidden fields almost everywhere, as well as for GF.

For h1dot=D(z1)z1dot, split the difference into a velocity difference and a multiplier difference times the GF velocity. The first is O_T(n^−1). The second is bounded by sqrt(n) times a bounded GF velocity L2 norm, multiplied by the O_T(n^−3/2) position error. It is also O_T(n^−1).

For z2dot, the four terms in the difference of Adot h1+A h1dot are controlled by: the O_T(n^−3/2) Adot operator error times bounded h1; bounded GF Adot times the h1 position error; the A operator error times bounded h1dot; and bounded GF A times the O_T(n^−1) h1dot error. Thus z2dot has error O_T(n^−1). Applying the same scalar multiplier split to h2dot=D(z2)z2dot gives O_T(n^−1), using the bounded L2 norm of GF z2dot and its elementary finite maximum bound. This checks all original preactivation and activation velocities for both samples. There is no additional repeated sqrt(n) loss and no need for A to act boundedly on another Lp space.

### Integrated energies and kernel blocks

In the weighted raw parameter metric from (6.5), all compared speeds are uniformly bounded and the largest velocity error is O_T(n^−1). The inequality for the difference of squared norms therefore gives O_T(n^−1) for the integrated parameter energies over [0,T]. It also gives that rate for each individual hidden-field velocity energy. The claim concerns this specified raw physical metric, not unweighted first-matrix or readout Frobenius energies. No exact discrete loss-dissipation identity is used or inferred.

The first kernel uses D(z1)q, whose difference is O_T(n^−1) by (9.3), while these fields have bounded L2 norms. Its inner-product differences are therefore O_T(n^−1). The second kernel uses delta2 and h1, whose differences are O_T(n^−3/2), with all factors bounded; the third uses h2 with the same rate. This verifies the three stated kernel rates, for both geometries.

### Hidden-path empirical Wasserstein distance

For each population, couple a neuron's GD path with its GF path from the identical finite initialization. Each scalar hidden-path difference e_i starts at zero and is absolutely continuous, so

\[
\sup_{0\leq t\leq T}|e_i(t)|^2
\leq\left(\int_0^T|\dot e_i(t)|\,dt\right)^2
\leq T\int_0^T|\dot e_i(t)|^2\,dt.
\]

Averaging over neurons and summing over the two samples, and over any stated finite tuple of hidden fields, gives an admissible coupling cost bounded by T times the integral of the squared normalized L2 velocity errors. Their uniform O_T(n^−1) bound makes the squared cost O_T(n^−2). Taking its square root proves the asserted W2 path rate O_T(n^−1). The derivative estimate is what controls the supremum inside the neuron average; a mere supremum-in-time L2 position estimate would not by itself suffice. The comparison remains between GD and GF at the same n, separately on each population or for its specified finite tuple of sample fields.

## 10. Other angles, exclusions, and complete coverage

Source: lines 938–1015, equation (10.1) and the remaining-bridges list.

For a nonzero intermediate correlation, multiplying the raw cross term by F'(z_a) gives exactly D(z_b)/D(z_a)=(1+z_a^2)/(1+z_b^2). The sign, residual index, and factor −2rho in (10.1) are correct. Orthogonality removes the term; actual antiparallel opposition makes the ratio one and gives the checked factor four.

For a nondegenerate Gaussian pair, sets with the numerator coordinate arbitrarily large and the denominator coordinate bounded have positive probability. The ratio is therefore essentially unbounded. On a probability space, a positive-measure set where its magnitude is at least N gives a unit L2 indicator whose multiplied norm is at least N or infinite. This proves failure of a bounded multiplication operator on unrestricted L2. It does not prove failure on the actual canonical q fields, and the note explicitly makes that distinction, including the fact q=0 at zero-readout initialization.

The stationary example A0=0, b0=0 is consistent: h2=0, delta2=0, q=0, and every parameter derivative vanishes. Thus the disclaimer about nontriviality is substantive and correct. No intermediate-angle or canonical-population theorem is silently used in the proof.

Every substantive section and every numbered estimate was audited: (1.1); (2.1)–(2.3); (3.1)–(3.4); (4.1)–(4.8); (5.1)–(5.5); (6.1)–(6.7); (7.1)–(7.3); (8.1)–(8.8); (9.1)–(9.3); and (10.1). This includes the unnumbered constants, continuation and symmetry arguments, initialization tail estimate, interpolation and velocity claims, energy comparisons, path assertion, stated exclusions, and proof-content digest. The introductory contract-history statements were read but not independently authenticated, in accordance with the isolation instruction; they are unnecessary for the internal theorem verified here.

## Required versus optional findings

Required mathematical errors or missing hypotheses within the stated deterministic scope: **none found**.

Two optional presentation clarifications could make the already-valid arguments easier to parse:

1. Near (7.3), label the intermediate maximum explicitly as stopped at the first candidate residual exit and distinguish the enlarged a,M constants from constants initially chosen only for the exact flow. Lines 668–670 and 694–698 already supply these facts, so no proof correction is required.
2. At the path-measure corollary, write the precise path tuple for each population, for example C([0,T];R^2) for the two sample fields, or the corresponding finite-dimensional tuple when both preactivations and activations are included. The given same-neuron coupling proof establishes these versions directly. This is a notation clarification, not a change in rate or scope.

No candidate edits were made or are needed for this verdict. In particular, constructing a canonical operator, proving a population law or nontriviality, or addressing other angles would expand the theorem rather than repair it.

## Final integrity check

After the complete review was written, the supplied source's line count and whole-file SHA-256 were checked again. The final recorded values are 1,015 lines and:

`c3f147633689050f8d9a4749e23861b02640dd7ba0e201b0f05a609b9c76cf39`

The whole-file hash is unchanged. The verdict remains **PASS for the scoped conditional deterministic theorem and its stated same-width finite-GD/GF corollaries only**.
