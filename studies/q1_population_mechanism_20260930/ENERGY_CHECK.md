# Bounded internal cross-check of the energy route

Reviewed artifact: `ENERGY_ROUTE.md`, SHA256
`015b9c83cfdcc52c16913f56ef2e2d5f50bd391064a88dba8f0592253c9377b3`.
The hash was verified before reading the complete note. This is an authorized same-study post-freeze cross-check, not an isolated independent promotion review. The reviewer had already developed the predictor route and received the supervisor's moving-span mechanism. No experiment or outside scientific source was used.

**Conclusion:** no substantive mathematical error found. The scalar fitting and finite endpoint results, the comparator and optimized-certificate formulas, and the lag-controlled loss inequalities have the stated normalizations and valid hypotheses. The note appropriately separates reachable results from ambient-state counterexamples and conditional multi-sample fitting.

## 1. Loss identity and lag normalization

The identity `dot E = -D_A-D_w-4||F||_F^2+2<F,Z>_F` follows with the exact stated scaling. In particular, for the temporarily independent forward variable B,

\[
\nabla_BE=\frac{2}{mn}\sum_a r_a d_a h_a^\top=2F,
\qquad \dot B=-2F+Z.
\]

The actual A and w equations equal minus n times their respective loss gradients, so their chain-rule contributions are exactly minus ||dot A||_F^2/n and minus ||dot w||^2/n. There is no missing factor of n or m.

The key averaging formula, storage identity, and lag identity all check. In particular,

\[
\frac{\|\dot H\|_F}{\sqrt{mn}}
\le\frac{\sqrt m\|\dot A\|_F}{\sqrt{mn}}
=\sqrt{D_A}
\]

is precisely the estimate used in (4). The identities apply to the initialized reachable filter and do not assert that its coupling to the values has a sign.

For the quantitative fitting bound, let R=||w||/sqrt(n) and v=||V||_F/sqrt(mn). The needed estimates are

\[
\frac{\|P\|_F}{\sqrt{mn}}\le\rho R,\qquad
v\le2R_*(\tau-1),\qquad
\|Z\|_F\le(2\rho R_*+\alpha v)e\le4\rho R_*e.
\]

The first follows from ||d_a||<=||w||, the second from integrating the value equation, and the third from the Frobenius product inequality and alpha=rho/tau. Completing the square gives

\[
-4\|F\|_F^2+2\langle F,Z\rangle_F
=-4\|F-Z/4\|_F^2+\|Z\|_F^2/4.
\]

The Gram normalization is also correct:

\[
D_w=\frac{4}{m^2n}r^\top G^\top Gr
\ge4\lambda_*\frac{\|r\|^2}{m}=4\lambda_*E
\]

under lambda_min(G^T G/(mn))>=lambda_*. These calculations yield (9) and (10) exactly. Persistent excitation, bounded readout, and sufficiently small lag are hypotheses, not consequences proved for general data. The rank obstruction when m>n is correctly stated.

## 2. Comparator identity and finite-horizon certificate

For each fixed vector u,

\[
\frac d{dt}\frac{\|w-u\|^2}{2n}
=-2\mathbb E_a r_a(f_a-f_{u,a}).
\]

The elementary square identity in the note produces (5). No feature derivative is missing, because the differentiated quantity contains only w and the constant u. Features enter its derivative through dot w, not through differentiation of E_u. This remains valid for endogenously moving features.

For u=0, integrating (5) yields (6). The improved readout bound in (7) is valid because, pointwise in time,

\[
E+\mathbb E_a f_a^2
=\frac12+2\mathbb E_a(f_a-y_a/2)^2\ge\frac12.
\]

Consequently ||w(t)||^2/n<=t. Combining integral E<=t with Cauchy–Schwarz gives tau<=1+t. The V estimate uses

\[
2\int_0^t\rho R
\le2\left(\int_0^tE\right)^{1/2}
\left(\int_0^tR^2\right)^{1/2}
\le\sqrt2\,t^{3/2}.
\]

These estimates bound B and the A derivative on every finite interval. Together with tau>=1 and local Lipschitz continuity of the vector field, they justify the global existence conclusion.

The certificate (12) has the correct linear coefficient b_t and quadratic coefficient C_t. For each fixed terminal time, expanding the integrated comparator loss gives

\[
\int_0^t E_u=t-2u^\top b_t+u^\top C_tu.
\]

The initial comparator storage is ||u||^2/(2n), so the optimized matrix is exactly C_t+I/(2n). It is positive definite. Optimizing over a constant u after fixing the horizon is legitimate: it does not differentiate u_t along the trajectory or inject it into the dynamics.

The pointwise fitting bridge is also valid. A fixed comparator with integrable E_u bounds w and makes E integrable via (5). The bounded readout and bounded features make dot w bounded. Uniform continuity of G therefore implies uniform continuity of E; a nonnegative uniformly continuous integrable function tends to zero by the disjoint-interval argument given in the note. Average fitting alone would not justify this last step, and the note correctly adds the required assumptions.

One minor wording precision: “vanishing average excess loss” in the discussion of (8) means the displayed upper bound, or equivalently limsup of the average excess is at most zero. The average difference can remain negative. The formula itself is unambiguous and correct.

## 3. Scalar fitting and the limiting whole-input function

The sign transformation in the scalar proof checks for both labels and both possible initial signs. Writing W_0=c b, h=sH, k=sK, v=cs q, and w=ycs u gives B=c(b+qK), g=cs Gamma, and f=y u Gamma. Thus r=-y epsilon. Substitution gives exactly the four transformed ODEs in the note, including the squared factor (1-H^2)^2 in dot H.

On epsilon>=0, the cone u,q>=0 and H>=K>0 is invariant. The boundary H=K has nonnegative difference derivative, while u and q cannot become negative. Since the full vector field vanishes at epsilon=0, local uniqueness prevents a trajectory from crossing that boundary. Starting from epsilon=1, finite-time equality would also contradict backward local uniqueness. Therefore epsilon remains positive at finite times.

All of H,K,u,q are nondecreasing in this cone, so Gamma>=Gamma_0>0 and dot Gamma>=0. The inequality

\[
\dot\epsilon=-2\epsilon\Gamma^2-u\dot\Gamma
\le-2\Gamma_0^2\epsilon
\]

proves the stated exponential loss bound. The required W_0h(0) nonzero event has probability one under the stipulated scalar Gaussian initialization: the normalized training preactivation has a nondegenerate Gaussian law, and W_0 also has a continuous nondegenerate Gaussian law.

For the endpoint, u<=1/Gamma_0, q<=1/Gamma_0^3, and the integrated exponential bound give finite total variation of the training preactivation a. Since only the training-input direction of A changes, this also proves convergence of the full row A. All other original parameters converge by the bounds and monotonicity. The limiting margin is one.

The strict permanent lag in (13) is valid. For positive finite time, u>0 and every other factor in dot H is strictly positive: epsilon>0, b+qK>0, and all finite tanh derivatives are positive. Thus H_infinity>H(0). The exact lag integral with finite tau_infinity gives the stated strictly positive lower bound. Successful fitting does not force the key to equal the current feature.

Finally, (14) follows by the exact invariant of A orthogonal to the training input and by solving the limiting interpolation identity w_infinity*g_infinity(x)=y for w_infinity. Its denominator is bounded away from zero by Gamma_0. It characterizes the selected whole-input function in terms of dynamically selected limiting scalars and preserved initial perpendicular components. It does not supply an explicit formula for those scalars or guarantee unseen-label accuracy; the note correctly states both limits.

## 4. Counterexamples and claim levels

The ambient-state increasing-loss example has dot B=-1, dot z=-1/2, and dot E=1 with the displayed scalars. It is not shown reachable and is explicitly labeled accordingly. The equal-label antipodal example is a genuinely reachable arrested trajectory, due to oddness and zero initial supervised readout force. Both conclusions have the claimed strength.

No revision is required for mathematical validity at the reviewed hash. In particular, neither the lag inequality nor the scalar cone proves generic realizable-data fitting, reachable loss monotonicity at arbitrary width, or an endpoint minimum-norm principle. Those remain open as stated.
