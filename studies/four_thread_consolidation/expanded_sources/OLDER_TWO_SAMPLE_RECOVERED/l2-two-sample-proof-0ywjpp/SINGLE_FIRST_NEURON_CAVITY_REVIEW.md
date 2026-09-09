# Isolated adversarial referee report

## Provenance and scope

Mathematical source read in full: `/tmp/l2-two-sample-proof-0ywjpp/SINGLE_FIRST_NEURON_CAVITY_TEST.md`, lines 1–946, dated 2026-09-06.

Requested SHA-256:

`a94813d504e4e9bc9a7c7e2c66472f41b76d66dfc20e9c120ddabca1add558bc`

SHA-256 computed from the source before review:

`a94813d504e4e9bc9a7c7e2c66472f41b76d66dfc20e9c120ddabca1add558bc`

The hashes match. No named dependency, other mathematical file, prior review, or history was read. No agents, experiments, or external mathematical sources were used. The only procedural skill consulted was `/etc/codex/skills/solve-math-rigorously/SKILL.md`. The source was not edited. Equation and line references below refer to this exact source version.

This is an audit of a finite-network deletion/restoration construction and its stated component estimates. It is not a review of a submitted global mean-field theorem, and no population-limit, propagation-of-chaos, or population-adjoint identification is demanded.

## Scoped verdict

The principal positive results survive the audit: the cavity is independent of the removed Gaussian column; the GF and simultaneous raw-GD restoration identities are exact; the initial root, readout, residual, and learned-column terms are retained; the bulk metric and secant normalizations are correct; and the normalized logarithmic singular-value estimate is proved with adequate treatment of repeated eigenvalues and noncommuting GD factors. The probability bookkeeping in (47) is also correct as a reduction.

Two revisions are required for the note to be fully precise and self-contained as written:

1. The literal fixed-neuron, uniform-in-probability target needs to be distinguished from the stronger conditional or directional targets. The supplied time-derivative estimates, together with the actual network's permutation symmetry, already imply a weak uniform-in-probability bound for the complete fixed-neuron path. I give that proof below. Thus an unqualified assertion that even this weak tail, or tightness of the scalar remainder, is still unproved is misleading. The exposure, participation, and conditional-directional estimates remain unproved.
2. The compact-gate positive-active-fraction statement needs an explicit nontriviality assumption on the gate. Smooth compact support and (4) alone do not imply it. This affects only that auxiliary statement, not the restoration or propagator estimates.

Neither issue invalidates the principal identities or the positive matrix estimate. The first is a substantive target/scope correction, not a counterexample to the canonical dynamics. The second is a local hypothesis omission. The note correctly refrains from proving a mean-field theorem or claiming an impossibility result.

## Required findings

### R1. Separate the weak fixed-neuron path tail from the genuinely unestimated directional quantities

Locations: lines 76–79, (6), lines 736–742, (47), and lines 930–945.

The note asks for a width-uniform tail or self-response bound for a deterministic first-neuron index. Later it explicitly discusses uniform-in-probability bounds. Under that interpretation, a further consequence of (6) is available. This consequence is stronger than merely recording an empirical second moment at one time.

For GF define

\[
 Q_i=\max_{a=1,2}\sup_{0\le t\le T}|q^{(1)}_{a,i}(t)|.
\]

Absolute continuity and scalar Cauchy–Schwarz give, for each sample and neuron,

\[
 \sup_{t\le T}|q^{(1)}_{a,i}(t)|^2
 \le 2|q^{(1)}_{a,i}(0)|^2
       +2T\int_0^T|\dot q^{(1)}_{a,i}(s)|^2\,ds.
\]

After summing over samples and neurons, (6) proves the deterministic path-supremum estimate

\[
 \frac1n\sum_{i=1}^n Q_i^2
 \le \frac2n\sum_a\|q^{(1)}_a(0)\|^2
       +\frac{2T}{n}\int_0^T\sum_a\|\dot q^{(1)}_a(s)\|^2\,ds
 \le C_T
 \qquad\text{on }\mathcal E_n. \tag{R1.1}
\]

The conversion to the specified fixed index is legitimate and needs to be written out. If a permutation matrix is denoted by \(P_\pi\), transform the actual initialization and parameters by

\[
 W^{(1)}\mapsto P_\pi W^{(1)},\qquad
 A\mapsto A P_\pi^T,\qquad w\mapsto w.
\]

The initialization law is invariant, the raw vector field is equivariant, and the query vector transforms by \(q^{(1)}_a\mapsto P_\pi q^{(1)}_a\). Uniqueness gives this equivariance for the whole GF path. The event \(\mathcal E_n\) is invariant because the operator norm is invariant under a column permutation. Consequently all the truncated expectations below are equal, and for every deterministic valid index \(j\),

\[
 \mathbb E[\mathbf1_{\mathcal E_n}Q_j^2]
 =\frac1n\mathbb E\!\left[\mathbf1_{\mathcal E_n}\sum_iQ_i^2\right]
 \le C_T.
\]

In particular,

\[
 \Pr(Q_j>v)
 \le \Pr(\mathcal E_n^c)+\frac{C_T}{v^2},\qquad v>0. \tag{R1.2}
\]

This does not assume neuron independence at positive time. It uses permutation symmetry of the actual trajectory, not symmetry of the cavity with its distinguished neuron. It also does not apply to an index selected after inspecting the initialized or trained network, nor to the maximum over all neurons.

The same conclusion holds for raw GD. One can use the node increments from (6): set

\[
 V_{a,i}=|q^{(1)}_{a,i,0}|+
       \sum_{k<N}|q^{(1)}_{a,i,k+1}-q^{(1)}_{a,i,k}|,
 \qquad N=\lceil T/\eta\rceil.
\]

The Euclidean triangle inequality gives \(\|V_a\|/\sqrt n\le C_T\), since each increment has RMS norm at most \(C_T\eta\). Thus the normalized sum of squared node suprema is bounded. For the prescribed raw interpolation, the product-rule argument used in Section 10 also gives

\[
 \dot q^{(1)}_a=\dot A^T\delta^{(2)}_a+A^T\dot\delta^{(2)}_a,
 \qquad \|\dot q^{(1)}_a\|/\sqrt n\le C_T
\]

on every cell: \(\dot A\) is the bounded old-node raw direction, and the recomputed \(\dot\delta^{(2)}\) has the RMS bound established there. Therefore (R1.1) holds on the full interpolation as well. Simultaneous updates and raw interpolation preserve the same permutation symmetry. Formula (R1.2) follows for sufficiently large widths, exactly the regime of the source's GD estimates.

Since (23) tends to zero, (R1.2) proves asymptotic tightness uniformly in width. It also gives tightness over all admissible widths: first choose a width cutoff making (23) small, and then handle the finitely many smaller widths using finiteness of each path on the fixed horizon. GF has global existence as established in Section 2; GD has finitely many finite updates and continuous cell interpolations at each fixed width. No explicit polynomial rate for these finitely many exceptional widths is needed for that tightness conclusion.

There is a corresponding weak consequence for the scalar remainder. Write the final exact decomposition as

\[
 q^{(1)}_{a,j}=G_{j,a}+B_{j,a}+\Gamma_{j,a},
 \qquad B_{j,a}=M_{j,a}+S_{j,a}+g^TL_aY_0,
\]

where \(\max_a\sup_t|B_{j,a}|\le C_T\) on \(\mathcal E_n\). Integrating the conditional tail (22), on its proper event \(\widehat{\mathcal E}_n\), gives

\[
 \mathbb E\!\left[
   \mathbf1_{\widehat{\mathcal E}_n}
   \big(\max_a\sup_t|G_{j,a}(t)|\big)^2\right]\le C_T.
\]

Because \(\mathcal E_n\subseteq\widehat{\mathcal E}_n\), (R1.1) and the decomposition imply

\[
 \mathbb E[\mathbf1_{\mathcal E_n}\Gamma_j(T)^2]\le C_T,
 \qquad
 \Pr(\mathcal E_n\cap\{\Gamma_j(T)>v\})\le C_T/v^2. \tag{R1.3}
\]

For GD this argument applies to the node remainder defined in (45). The direct argument above already supplies the weak query bound on the full raw interpolation.

These are referee-derived consequences of actual bounds in the source. Merely naming \(\Gamma\), rewriting the query, or stating an equivalent response criterion would not prove (R1.3); the independent ingredient here is (R1.1) plus the verified permutation symmetry.

What this argument does **not** prove is a Gaussian tail for the actual query, a bound conditional on \(\mathcal F_{-j}\), a deterministic uniform bound for the complete response on \(\mathcal E_n\), a useful estimate on \(\int\kappa_j\), a bound on \(\int\Pi_j\), or the overlap estimate in (39). It does not control \(\|Y\|\). Those are substantive stronger targets. The required revision is to distinguish them explicitly from the literal weak fixed-neuron probability target, and to qualify the assertion that the scalar remainder is wholly unestimated. If the intended requested upgrade excludes a symmetry-based polynomial tail, its additional requirement must be stated mathematically.

### R2. State the compact gate's nontriviality within this file

Locations: lines 65–70 and 899–910.

The source refers to a particular compact gate defined elsewhere, but only states smooth compact support and the bounds (4) within this file. To verify the claim that the initially non-doubly-saturated fraction has probability strictly between zero and one, the reader also needs \(p\not\equiv0\). The stated properties alone allow \(p\equiv0\), in which case every first row is frozen and the asserted positive fraction is false.

For a self-contained statement, it suffices to assume explicitly

\[
 p\in C_c^\infty(\mathbb R),\qquad p\not\equiv0,
 \qquad \phi_1(s)=\int_0^s p(u)\,du,
\]

and define a doubly saturated pair as one at which both first gates vanish. No particular formula, sign condition, or shape of \(p\) is needed for the arguments here. Nontriviality and continuity give a nonempty open interval where the gate is nonzero; compact support gives an open region where both gates vanish. The nonsingular Gaussian density assigns positive probability to both regions. The independent-row variance calculation then proves the claimed limiting fraction.

The freezing statement itself remains correct even for the zero gate. This finding is confined to the positive-fraction assertion and its self-contained hypotheses. It does not affect the arctan branch, the exact restoration identities, or (35).

## Detailed mathematical audit

### 1. Raw metric, GF estimates, existence, and raw-GD descent

Equations (1)–(3) have consistent normalization. The Euclidean first-layer derivative of the loss carries \(1/n\); inversion of the first-layer raw metric multiplies by \(n/d\), giving the stated \(1/d\). The second-layer metric is unscaled, giving \(1/n\) in its direction. Inversion of the readout metric multiplies by \(n\), giving the unscaled readout direction. With \(c_a=-2r_a\), the directions are exactly the negative raw gradient. Consequently (7) is the correct dissipation identity, with no missing factor of two.

On \(\mathcal E_n\), bounded features give \(|f_a(0)|\le B_2\) and hence \(\|r(0)\|\le\sqrt2(B_2+1)\). Loss dissipation bounds \(c\); integrating the readout equation bounds \(w\) coordinatewise; and the rank-one second-layer estimate bounds \(A\) spectrally. The RMS bounds on \(\delta^{(2)}\) and \(q^{(1)}\) then follow. Furthermore,

\[
 \|\dot z^{(1)}_a\|/\sqrt n\le C_T,
 \quad \|\dot h^{(1)}_a\|/\sqrt n\le C_T,
 \quad \|\dot z^{(2)}_a\|/\sqrt n\le C_T.
\]

The product rules displayed in Section 2 now prove all time-derivative bounds in (6). Prediction differentiation in the raw metric supplies the bound on \(\dot c\). This reasoning uses only two sample directions and cancels the dependence on \(d\); the constants may depend on the fixed \(\rho\), as allowed.

For each finite-dimensional system, the dissipation estimate bounds finite-time raw displacement by Cauchy–Schwarz. A finite maximal existence time would therefore leave the parameters in a bounded set with a limiting point, at which the locally Lipschitz vector field can be continued. This validates global GF existence on any fixed horizon. The same reasoning works for the constrained cavity, using its restricted raw metric and unchanged denominator \(n\).

The GD bootstrap is legitimate. Before a possible residual exit, old-node residuals bound the updates, which in turn bound \(A,w\) at the candidate next node and on its raw connecting segment. These parameter bounds already bound the segment prediction derivative; the segment residual is therefore controlled without assuming descent at the candidate node. For raw unit directions,

\[
 \|U^{(1)}x_a\|\le\sqrt n,
 \quad \|U^{(2)}\|_F\le1,
 \quad \|U^{(3)}\|\le\sqrt n.
\]

Every term of \(D^2f_a\) except the displayed first-layer curvature term is bounded by \(C_T\). That term is bounded by \(C_T\sqrt n\), using the RMS bound on \(q\) and then its coordinate maximum. Thus the loss Hessian on the segment is \(O_T(1+\sqrt n)\). With \(\eta=n^{-2}\), the Taylor remainder is at most half the descent term for large \(n\), so the proposed exit cannot occur. No GF-to-GD approximation is used. The statements include the final node beyond \(T\) by the stated enlarged horizon.

### 2. Action and path estimates

The total-variation definition of \(U_i\), (6), and the Euclidean triangle inequality imply \(n^{-1}\sum_iU_i^2\le C_T\). The row-work identity is exact:

\[
 d\|\dot W_i^{(1)}\|^2
 =\sum_a c_aq^{(1)}_{a,i}\dot h^{(1)}_{a,i}
 =d_i^TCd_i.
\]

Integration by parts bounds its time integral by \(2B_1U_i\), including both endpoint terms. Since \(\|C\|_{\rm op}<2\), this gives the displayed quadratic-action bound, while \(\sup|\dot z_i^{(1)}|\le2P_1U_i\). Their product proves the cubic action bound in (8). The quartic path bound follows with the displayed coefficient on the initial moment and a larger constant on \(U_i^2\).

The terse GD absorption statement is also correct. To expose the omitted algebra, put \(a_{k,a}=c_{k,a}q^{(1)}_{k,a,i}\), \(v_k=(z^{(1)}_{i,k+1}-z^{(1)}_{i,k})/\eta\), and \(E_{i,k}=d\|(W^{(1)}_{i,k+1}-W^{(1)}_{i,k})/\eta\|^2\). Then \(|v_k|^2\le2E_{i,k}\), and scalar Taylor expansion gives

\[
 \sum_a a_{k,a}(h^{(1)}_{a,i,k+1}-h^{(1)}_{a,i,k})
 =\eta E_{i,k}+\mathcal R_{i,k},
 \qquad |\mathcal R_{i,k}|\le L_1\eta^2U_iE_{i,k}.
\]

Summation by parts bounds the sum of the left side by \(2B_1U_i\). Since \(\eta\max_iU_i\le C_Tn^{-3/2}\), the remainder is absorbable. The raw first-root interpolation is linear, so the same quadratic/cubic and path arguments apply there. No interpolation of nonlinear features is substituted for recomputation.

The moment calculations used in Section 12 are valid. The Gaussian law gives \(\mathbb E|\xi|^4=8+4\rho^2\). Also \((x^2+y^2)^4\le8(x^8+y^8)\) and the marginal eighth moment is 105, giving the stated upper bound 1680. Independent initial rows and Chebyshev yield the failure bound \(1680/n\) for the empirical fourth moment exceeding 13. Applying (8) to actual and cavity paths does not require independence of those paths. Formula (49) follows, with the fixed \(C^{-1/2}\) norm absorbed in the constant.

These action bounds do not prove the participation or overlap estimates proposed in Section 9. Finding R1 uses the different derivative estimate for the query itself and permutation symmetry; it does not repair those directional estimates.

### 3. Deletion, measurability, and exact restoration

The deletion in (9) removes the whole trained column: it imposes a zero column permanently and eliminates its feature from the bulk updates. A zero initialization followed by ordinary training would indeed be a different system. Freezing the corresponding first row is consistent, because its cavity reverse field is zero. The normalization remains \(n\), which is essential for the subsequent exact comparisons.

The deleted trajectory is a deterministic measurable function of the initialization excluding \(g\). Its initialization and equations use no \(g\), and uniqueness fixes the trajectory. The included initial root \(\xi\) is independent of \(g\); retaining it in \(\mathcal F_{-j}\) is harmless, and the upper cavity fields do not use its feature.

The column equation (10), omitted input (11), and bounds (12) are correct. The learned column has norm \(O_T(n^{-1/2})\); its inner product with an RMS-bounded reverse field can still be \(O_T(1)\). The source makes that distinction correctly.

All product subtractions in (13) check out. In particular the three terms in the bulk weight update respectively retain the residual, upper reverse-field, and first-feature differences. The first-root difference keeps the actual query in the gate-difference term and the cavity gate in the query-difference term, which is a valid exact telescoping. Equation (14) retains both the initial and learned column in the distinguished root's own evolution. The equations form a closed restoration system, with no prescribed future trajectory supplied as an external control.

### 4. Initial root, initial readout, and residual terms

The zero initial bulk-parameter difference does not imply zero initial upper-field difference. Equation (15) retains exactly the omitted input \(g\phi_1(\xi_a)\), the initial readout multiplying the gate difference, and the initial prediction difference. In particular \(\Delta c_a(0)=-2\Delta f_a(0)\) generally does not vanish. The common initialization of \(w\) only makes \(\Delta w(0)=0\); it does not remove the \(w(0)\)-weighted nonlinear difference.

At time zero the bulk-with-zero-input field equals the cavity field, and the learned column is zero. Therefore \(R(0)=M(0)=0\), and the remaining direct difference is bounded exactly as in (20). The actual initial query is not asserted to be an independent Gaussian projection. Its dependence on the initial first root and the Gaussian column is visible in (15) and (20).

### 5. Self-response split and Gaussian path tail

The fundamental-theorem secant in \(D_a\) is correctly evaluated at the actual bulk parameters and along the entire omitted-input segment. It gives

\[
 g^T\delta^{(2)}_a
 =g^T\widehat\delta^{(2)}_a
  +g^T(\delta^{(2),0}_a-\widehat\delta^{(2)}_a)
  +g^TD_ab\,h^{(1)}_{a,j}.
\]

Adding \(\ell^T\delta^{(2)}_a\) proves (18), without losing or double-counting the learned-column contribution. The estimates (17), (19), and (20) follow from the stated norms. None needs independence of the trained root, secant matrix, learned column, or residuals.

Conditional on \(\mathcal F_{-j}\), (16) is precisely the covariance of Gaussian projections with column covariance \(I_n/n\). The cavity Lipschitz estimate (21) follows from (6), with deterministic constants on the measurable event \(\widehat{\mathcal E}_n\).

The dyadic proof of (22) has sufficient constants. At level \(m\), the scalar Gaussian tail and union bound contribute at most

\[
 2e^{-u^2/2}\,2^m e^{-2(m+1)}
\]

per sample. The increment thresholds are summable, the initial value and the endpoint increment are controlled separately, and continuity extends the bound from the dyadic grids. The displayed factors 6 and 12 safely dominate these sums. Independence across times or between the two sample processes is not used. Zero-variance Gaussian variables cause no difficulty.

The distinction between the two initialization events is correct and essential. The full event depends on \(g\), so it cannot be inserted into the Gaussian conditioning without altering the conditional law. The inclusion \(\mathcal E_n\subseteq\widehat{\mathcal E}_n\) permits intersection with \(\mathcal E_n\) after applying the valid conditional bound. The two-net argument at threshold 4 gives the matrix term in (23), with exponent \(8-2\log9\); the variance \(n^{-2}\) of each readout entry gives its term \(2n e^{-n^2/2}\). The analogous estimate for the projected initial matrix also holds.

### 6. Bulk coordinates, secants, and scalar-readout normalization

Let the matrix with columns \(x_1,x_2\) be denoted by \(\mathsf X\), so \(\mathsf X^T\mathsf X=dC\). For a change in the input span, \(\Delta W_i^{(1)}=\mathsf X(dC)^{-1}\Delta z_i^{(1)}\), with the row/column convention adjusted by transpose. Thus

\[
 d\|\Delta W_i^{(1)}\|^2
 =(\Delta z_i^{(1)})^TC^{-1}\Delta z_i^{(1)}.
\]

The first blocks in (24) therefore represent exactly the restricted raw metric. The other blocks have the right factors as well. The dimension is

\[
 2(n-1)+n(n-1)+n=n^2+2n-2.
\]

The constant input-orthogonal first-row components do not enter the dynamics or this metric comparison.

Holding \(E\) fixed in the gradient in (25) is correct: the distinguished root and column are outside the bulk coordinates. Their omitted input depends on the full evolving trajectory, but it is independent of a bulk partial variation at fixed distinguished parameters. No chain-rule derivative of that trajectory dependence belongs in the bulk gradient.

The secant split is exactly

\[
 F(X,E)-F(\widehat X,0)
 =[F(X,E)-F(X,0)]+[F(X,0)-F(\widehat X,0)]
 =\mathcal B E+J\Delta X.
\]

Both secants retain derivatives of the residuals. The output secant satisfies

\[
 \delta^{(2),0}_a-\widehat\delta^{(2)}_a
 =\sqrt n\,L_a\Delta X=L_aY,
\]

which verifies the normalization of (27) and (29). The source \(v=\mathcal B e\) is \(O_T(1)\) on the good event even though the unscaled bulk forcing is \(O_T(n^{-1/2})\).

The tangent bounds following (28) are correct. In the mixed \(X,E\) derivative of \(f\), the explicit \(1/\sqrt n\) cancels the \(\sqrt n\) size of each bulk-induced readout or upper-input tangent. This bounds \(\mathcal B\). Similarly \(D_X\delta^{(2)}/\sqrt n\) is bounded, giving \(L_a\). Secant residuals are bounded by bounded readouts and activations, without treating the secant points as gradient trajectories.

The maximum estimate (30) is valid with the actual bulk query maximum. The only coefficient requiring that maximum is the gate-difference term multiplied by the actual query. All other terms use RMS bounds. The scalar output in (31) really restores a factor \(\sqrt n\); it would be an error to transfer the bulk \(n^{-1/2}\) factor directly to the scalar query. The conclusions about the displayed exponential bounds in Section 7 are valid limitations of those particular deterministic estimates. They do not rule out the different probability argument in R1.

### 7. Symmetric Hessian split and normalized Frobenius estimate

Since \(F(X,0)\) is a negative Euclidean gradient in the coordinates (24), every \(D_XF\), and hence its secant average \(J\), is symmetric. Differentiating the loss gives

\[
 D_XF=-2\sum_a Df_a\otimes Df_a+\sum_a c_aD^2f_a.
\]

The first term and all readout, upper-curvature, and first/second-layer mixed terms have uniformly bounded bilinear forms in the raw coordinates. The only unbounded coefficient is the first-layer curvature term

\[
 \frac1n\sum_{i,a}c_aq^{(1),0}_{a,i}\phi_1''(z^{(1)}_{a,i})
                  D_Uz^{(1)}_{a,i}D_Vz^{(1)}_{a,i}.
\]

Substitution of \(D_Uz_i^{(1)}=\sqrt n C^{1/2}U_i\) cancels the \(1/n\) and gives exactly (33), including its sign and both \(C^{1/2}\) factors. Thus \(J_0\) is symmetric and uniformly bounded in operator norm, while \(H\) consists of the displayed first-neuron blocks.

At every secant point the spectral bound for the bulk matrix and the coordinate bound for the readout persist by convexity. Bounded activations then give uniformly bounded secant residuals and RMS reverse fields. Jensen/Cauchy–Schwarz in the secant parameter and the Frobenius multiplication inequality give (34). The normalization is by \(n\), not by the full parameter dimension. No coordinate maximum or higher operator-space estimate is used in this step.

### 8. Logarithmic singular values, including eigenvalue collisions

The finite-matrix proof in Section 8 is valid for the continuous coefficients used by GF. It also applies piecewise to the finite number of continuous pieces used in the GD embedding below.

Writing \(A_*=K+H\) and \(M=VV^T\), invertibility follows from the companion inverse equation. Hence \(M\) is positive definite throughout a compact time interval, with a positive lower eigenvalue bound. Its derivative is

\[
 \dot M=A_*M+MA_*.
\]

For a simple normalized eigenvector, this gives

\[
 \dot\lambda=2\lambda\,v^TA_*v,
 \qquad \frac d{dt}\log\sqrt\lambda=v^TA_*v.
\]

The repeated-eigenvalue argument is adequate. Min-max gives local Lipschitz continuity of the ordered eigenvalues. At an eigenvalue cluster, the complementary block has a spectral gap from the cluster value, so a nearby normalized eigenvector's complementary component is \(O(h)\). The projected equation then determines the first-order slopes from the restricted derivative. In this case that restriction is \(2\lambda\) times the compression of \(A_*\). Choosing an orthonormal eigenbasis of this compression gives the required diagonal formula wherever the ordered eigenvalues are differentiable. Crossings at which an ordered eigenvalue is not differentiable are omitted only on a null set. No globally differentiable choice of singular vectors is required.

Because the eigenvalues are bounded away from zero, their logarithms are locally Lipschitz and absolutely continuous. The function \(x\mapsto(x_+)^2\) is continuously differentiable, so the chain rule yields the stated inequality for the sum of squared positive shifted logarithms. In any orthonormal basis, the squared diagonal sum of \(H\) is at most \(\|H\|_F^2\). The \(\sqrt{F+\epsilon}\) regularization justifies integration even when \(F=0\), and proves

\[
 \left\|\big(\log s(V)-c(t-s)\big)_+\right\|_{\ell^2}
 \le\int_s^t\|H(u)\|_F\,du.
\]

Together with (34), this proves (35), including the case \(s=t\). Counting terms exceeding \(u\) gives the claimed singular-value counting bound. No dimension factor from the bounded \(J_0\) part is introduced because its contribution is removed by the scalar exponential shift. The estimate neither asserts an operator-norm bound uniform in width nor supplies conditional isotropy of the singular directions.

### 9. Curvature remainder and sufficient exposure criteria

Variation of constants around \(J_0\) proves (36)–(38). The deterministic source bound and the core propagator estimate give \(\|Y_0\|\le C_T\) on \(\mathcal E_n\), so the core readback is uniformly bounded there. The block expression in (38) is an exact scalar insertion of \(H\); its vectors and the matrix all depend on the same actual/cavity realization.

The overlap inequality (39) follows by applying Frobenius Cauchy–Schwarz across blocks, and its \(\sqrt n\) factor is necessary for that calculation. The two inequalities in (41) are also valid: the first uses (34), and the second follows from

\[
 \frac d{dt}(1+\|Y\|^2)
 \le(C_T+2\kappa_j)(1+\|Y\|^2).
\]

The positive part in \(\kappa_j\) handles the signed quadratic curvature contribution without replacing it by an absolute operator norm. These are sufficient criteria for controlling the entire response norm. Neither criterion is proved by defining it. The scalar decomposition alone also does not estimate its own remainder. Finding R1 derives a weak scalar probability estimate through a separate argument; it does not establish either exposure criterion or any delocalization property of \(Y\).

### 10. Exact raw GD, order of factors, and interpolation

All parameter-update differences in (13) and the distinguished root equation remain exact forward-difference identities when their right sides are evaluated at the old node. The learned-column history (42) correctly uses \(l<k\). Its final reverse field is evaluated at node \(k\); there is no missing or extra current-node contribution.

The coordinates (24) depend linearly on raw parameters, so simultaneous raw GD gives (43) exactly. Iterating this recurrence places a source from step \(l\) into \(Y_{l+1}\), and propagation to step \(k\) is by \(\mathcal U_{k,l+1}\). This verifies both the factor ordering and the source index in (44). The discrete core variation of constants similarly proves (45).

Expanding \(\|Y_k+\eta(J_kY_k+v_k)\|^2\) gives the energy recurrence in Section 10. The squared increment is bounded by \(C_T\eta^2n(1+\|Y_k\|^2)\). Summing over at most \((T+\eta)/\eta\) steps gives \(O_T(\eta n)=O_T(1/n)\), exactly the correction recorded in (46). The bound is not an unaccumulated one-step estimate.

For the discrete logarithmic singular-value bound, symmetry and \(\eta\|J_k\|\le1/2\) ensure that every factor \(I+\eta J_k\) is positive definite. Spectral functional calculus and the scalar remainder inequality give

\[
 G_k=\eta^{-1}\log(I+\eta J_k),\qquad
 \|G_k-J_k\|_{\rm op}\le\eta\|J_k\|_{\rm op}^2\le C_T/n.
\]

On cell \(k\), the generator \(G_k\) has exact evolution \(\exp(\eta G_k)=I+\eta J_k\). Consecutive cells therefore give the ordered product, with the latest factor on the left. This construction never takes the logarithm of the whole product or equates it to a sum of logarithms. The decomposition

\[
 G_k=(J_{0,k}+G_k-J_k)+H_k
\]

puts the small symmetric correction into the uniformly bounded part and keeps the normalized Frobenius estimate for \(H_k\). The continuous inequality applies on the cells and across their finitely many boundaries. Thus (35) holds at GD nodes with enlarged constants. Noncommutativity is fully respected.

The interpolation discussion is correctly scoped. The logarithmic product estimate is a node statement. Raw bulk differences and the learned column interpolate linearly, so their norm bounds pass to cell interiors. Upper fields must be recomputed, and the source does so. The recomputed cavity backward field remains independent of \(g\) and has a uniform RMS derivative on each cell, yielding the actual interpolated Gaussian-path bound. A bound on \(Y_k\) therefore extends to the whole raw-interpolation response. The source does not falsely identify this interpolation with GF, nor does it automatically promote a scalar node-remainder criterion to a bound on \(Y\).

### 11. Final probability accounting and remaining scope

On \(\mathcal E_n\), the decomposition and deterministic component bounds imply

\[
 \{Q_j>C_T(1+u)+v\}
 \subseteq\{G_j^*>C'_T(1+u)\}\cup\{\Gamma_j(T)>v\},
\]

after intersection with \(\mathcal E_n\) and adjustment of constants. The Gaussian exceptional event is bounded by conditioning on \(\mathcal F_{-j}\) over \(\widehat{\mathcal E}_n\); the complement of \(\mathcal E_n\) is added afterward. This proves (47) without requiring independence of \(G\) and \(\Gamma\). The analogous node statement is valid for GD.

As written, (47) is a reduction, not by itself a closed tail theorem. The note's warning against promoting (35) to an estimate in the selected random direction is correct. The note also correctly leaves the signed exposure, fourth-order participation, and directional overlap routes without a claimed proof. The qualification needed is R1: the already established derivative bounds and symmetry provide a weaker unconditional fixed-neuron path tail and, through the exact decomposition, a weak scalar-remainder tail. They do not provide the stronger directional analysis proposed by the cavity method.

## Optional improvements

1. **Clarify event language.** Lines 854–858 say the positive results are “unconditional on the good initialization event.” The formulas themselves are precise, but this wording can be read as conditioning (22) on the full good event. Prefer: the deterministic estimates hold on \(\mathcal E_n\), and the Gaussian conditional estimate holds on the \(\mathcal F_{-j}\)-measurable event \(\widehat{\mathcal E}_n\), without an additional response assumption.
2. **State the matrix lemma's regularity class.** Its applications have continuous or piecewise continuous coefficients on a compact interval. Say so in the standalone formulation rather than “any real matrix equation”; those hypotheses justify the local Lipschitz steps used in its proof.
3. **Expand the discrete action absorption by one displayed inequality.** The formula for \(\mathcal R_{i,k}\) in the audit above would make lines 191–195 independently checkable without reconstructing the work convention. The calculation is valid; this is an exposition improvement.
4. **Call the fourth-order scale a pointwise sufficient scale.** When \(\|Y\|=O(1)\), a pointwise bound on \(\Pi_j\) corresponds to \(\sum_i|Y_i|^4=O(n^{-1})\). Boundedness of the time integral of \(\Pi_j\) does not literally require that pointwise bound at every time. The current discussion of the scale can be qualified accordingly.

## Final assessment

Accept the exact finite-network restoration calculations, Gaussian cavity tail, deterministic learned/direct/core response bounds, and normalized logarithmic singular-value bounds within their stated GF and sufficiently-large-width raw-GD regimes. Require the two local revisions R1–R2 before accepting the note's full account of what remains open and its compact-gate auxiliary claim.

The stronger conditional/directional response analysis remains unfinished. The source does not prove the exposure or participation estimates, and an equivalent response criterion is not a substitute for such a proof. At the same time, the weaker fixed-neuron uniform-in-probability path bound follows from the source's own time-regularity estimates and permutation symmetry, as derived explicitly in this report. No global mean-field conclusion or negative conclusion about the canonical dynamics follows from this audit.
