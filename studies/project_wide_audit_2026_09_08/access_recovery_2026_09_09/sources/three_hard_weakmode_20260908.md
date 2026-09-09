# Three-input L3: one weak mode, exact Schur dynamics, and a trained-reference coupling calculation

2026-09-08. Independent theory-only route. All calculations use three hidden layers, all four trained raw blocks, the original raw metric, population readout C(0)=0, unit projected inputs, and the odd convex mixture phi_e(z)=(1-e)z+e atan z. No previous proof file was edited and no numerical trajectory experiment was performed.

**Result.** The input geometry does give at most one weak mode and a quantitative nonzero label component in a nearly null mode. This is a useful improvement over treating three directions as simultaneously weak. I derived the exact residual/Schur equations and found a concrete, architecture-specific failure of one tempting simplification: the initialized O(e^2) strong/weak kernel coupling becomes O(e) along the true, all-block, evolving affine reference, even for a triple whose two positive input-Gram eigenvalues are 2 and 1. The first nonzero coefficient is calculated explicitly below. A correctly formulated fast/slow construction remains possible, but it must retain this coupling, the motion of the fast constraint, and a state radius growing with 1/e. No full horizon-independent nonlinear population theorem or sufficient activation amplitude is proved here.

## 1. Geometry: exactly two well-conditioned input directions

Let Gamma be a realizable 3 by 3 unit-input Gram with |Gamma_ij|<=1-delta, where 0<delta<=1. Write its eigenvalues in decreasing order. Every 2 by 2 principal submatrix has smaller eigenvalue 1-|Gamma_ij|>=delta. Cauchy interlacing therefore gives

\[
                    \lambda_2(\Gamma)\ge\delta.                 \tag{1}
\]

In particular a singular admissible Gram has rank exactly two. This statement concerns the input Gram, not the complete trained tangent kernel.

Oddness permits replacing (x_i,y_i) by (y_i x_i,1) without changing raw parameter dynamics or absolute separation. In these folded coordinates the elementary augmented-Gram lemma, Appendix C, Part G.1 of `odd_mixture_separation_quantitative/REPORT.md`, gives

\[
          \Gamma+\mathbf1\mathbf1^T\succeq\delta^2 I/4.          \tag{2}
\]

For completeness, its proof needs only the three-input geometry. For a mixed-sign coefficient vector write q=(alpha_1,alpha_2,-b), alpha_i>=0, A=alpha_1+alpha_2. If D=[alpha_1(1-u_1.u_3)+alpha_2(1-u_2.u_3)]/A, then D is in [delta,2] and

\[
 q^T(\Gamma+11^T)q\ge(A-b)^2+((1-D)A-b)^2.
\]

The displayed quadratic form in (A,b) has determinant D^2 and trace D^2-2D+4<=4, hence is at least (delta^2/4)(A^2+b^2)>=(delta^2/4)||q||^2. One-sign vectors are controlled by (sum q_i)^2. Zero coefficients follow by continuity.

For a unit weak eigenvector v, with eigenvalue lambda_3, (2) implies

\[
       |v^T\mathbf1|^2\ge\delta^2/4-\lambda_3.                 \tag{3}
\]

Thus a unit null vector has |v^T 1|>=delta/2; if lambda_3<=delta^2/8, then |v^T 1|>=delta/(2 sqrt(2)). In original coordinates replace 1 by y and conjugate Gamma and v by the label-sign matrix. Consequently the very weak direction cannot simply have a negligible target uniformly over this class.

## 2. Exact projected equations and the missing moving-constraint term

On any already-existing strong trajectory with the scalar raw chain rule, let r=f-y and let K be the **complete** gradient Gram, summing first-layer, A, B and C blocks. Then r'=-Kr.

Fix a unit weak eigenvector v of the input Gram, and an orthonormal column matrix E spanning v-perp. These are fixed sample-space coordinates. Set

\[
 s=E^Tr,\quad w=v^Tr,\quad
 \mathsf A=E^TKE,\quad b=E^TKv,\quad c=v^TKv.
\]

The exact equations are

\[
                s'=-\mathsf A s-bw,
 \qquad         w'=-b^Ts-cw.                                  \tag{4}
\]

On an interval where mathsf A is positive definite define

\[
 p=\mathsf A^{-1}b,\qquad
 \sigma=c-b^T\mathsf A^{-1}b\ge0,\qquad z=s+pw.
\]

If p is absolutely continuous, differentiation gives, almost everywhere,

\[
 \boxed{\quad w'=-\sigma w-b^Tz,\qquad
 z'=-(\mathsf A+pb^T)z+(p'-p\sigma)w.\quad}                    \tag{5}
\]

This follows by substituting s=z-pw in (4): s'=-mathsf A z, w'=-b^Tz-sigma w, and then z'=s'+p'w+pw'. In particular setting z=0 is not invariant unless p'=p sigma along the actual trajectory. The p' term is present even if the kernel is smooth and its fast block has a fixed spectral gap.

Orders b=O(e), c=O(e^2) are consistent with an e^-2 slow time. Positivity only gives sigma>=0. For example the positive semidefinite block matrix with mathsf A=I, b=e beta and c=e^2||beta||^2 has sigma=0. This algebraic example is not a claim about the neural trajectory; it identifies why kernel positivity and the correct entrywise scales do not themselves prove slow coercivity.

A singular-perturbation proof would have to control the trained fast block, the positive Schur coefficient, and the forcing p'-p sigma on its admitted state region. Interlacing (1) supplies none of those trained estimates by itself.

## 3. Actual affine training destroys the initialized extra cancellation

The following is a concrete calculation in the original architecture. It does not freeze the first layer or either initialized action.

### 3.1 Setup and local regularity

At e=0 the activation is the identity. Let Theta^0(t) be the actual affine raw gradient flow, with loss (1/2)sum_i(f_i-y_i)^2. Its vector field is polynomial on the raw Hilbert state space of first-layer changes, Hilbert-Schmidt action changes, and readout. Initialized actions are bounded. Thus the ordinary local Banach-space ODE theorem applies and the affine solution is smooth, indeed locally analytic. A different fixed normalization of the empirical loss only rescales time in the calculation below.

Write A=A(0), B=B(0), z_i=z_i^1(0), and

\[
 Z=\sum_i y_i z_i,\qquad k=\Gamma y,\qquad
 M=A^*B^*BA.                                                   \tag{6}
\]

The first-layer metric gives, exactly in the affine model,

\[
 (z_i^1)'=\sum_j (y_j-f_j)\Gamma_{ij}A(t)^*B(t)^*C(t),
\]

\[
 A'=\sum_j(y_j-f_j)(B(t)^*C(t))\otimes z_j^1(t),
\quad B'=\sum_j(y_j-f_j)C(t)\otimes z_j^2(t),
\quad C'=\sum_j(y_j-f_j)z_j^3(t).                              \tag{7}
\]

Here z_j^2=A(t)z_j^1 and z_j^3=B(t)z_j^2. These are the original updates of all four blocks.

The canonical affine program has jointly centered Gaussian scalar fields within each layer. Finite affine source programs consist of linear Gaussian coordinates and deterministic population contractions; strong affine Euler limits preserve those joint Gaussian laws. This is the same affine-law justification used in `two_sample_odd_activation_theorem/PROOF.md`, Section 3, and does not use its two-input permutation symmetry. The label/control coefficients may be arbitrary deterministic functions of time. Actual adjoints, including all reused-transpose corrections, are retained.

### 3.2 The second-order trained marginal variances

Equations (7) and C(0)=0 give

\[
 C(t)=tBAZ+O(t^2),
\]

\[
 z_i^1(t)=z_i+\tfrac12t^2 k_i MZ+O(t^3),
\]

\[
 A(t)=A+\tfrac12t^2(B^*BAZ)\otimes Z+O(t^3),
\qquad
 B(t)=B+\tfrac12t^2(BAZ)\otimes(AZ)+O(t^3).                     \tag{8}
\]

The remainders are in L2 for fields and in Hilbert-Schmidt norm for action changes. Initialized contractions satisfy <Z,z_i>=<AZ,Az_i>=k_i. Composing (8), without discarding trained action terms, yields

\[
 z_i^2(t)=Az_i+\tfrac12t^2 k_i
       (AA^*B^*BA+B^*BA)Z+O(t^3),
\]

\[
 z_i^3(t)=BAz_i+\tfrac12t^2 k_i
       (BAA^*B^*BA+BB^*BA+BA)Z+O(t^3).                         \tag{9}
\]

Let q_{ell i}(t)=||z_i^ell(t)||_2^2. Then

\[
 q_{\ell i}(t)=1+d_\ell k_i^2t^2+O(t^3),
 \qquad (d_1,d_2,d_3)=(1,3,6).                               \tag{10}
\]

Here is a check of every nontrivial coefficient in (10). For a fixed initialized polynomial P independent of first-layer roots, the canonical contraction is <z_i,PZ>=k_i tau(P), where tau denotes the limiting normalized finite-matrix trace, not a trace of the infinite-dimensional action. The needed traces are

\[
 \tau(M)=1,\quad
 \tau(A^*AA^*B^*BA)=2,\quad
 \tau(M^2)=3,\quad
 \tau(A^*B^*BB^*BA)=2.                                       \tag{11}
\]

They follow directly from Gaussian fourth moments. For independent normalized square Gaussian A_n,B_n, set Q=B_n^*B_n. Then E tau(Q)=1, E tau(Q^2)=2+1/n, and

\[
 E_{A_n}\tau((A_n^*QA_n)^2)
 =(\tau Q)^2+(1+1/n)\tau(Q^2)\longrightarrow3.
\]

Conditioning on B for the last trace in (11) gives tau(Q^2), with limit 2. Conditioning on B in the second trace gives tau((A_n A_n^*)^2), also with limit 2. The fixed-program trace-probe and moment argument in `odd_mixture_separation_quantitative/REPORT.md`, Parts F and N.4, gives deterministic convergence and uniform integrability, so these expectation calculations identify population contractions. Thus the three coefficients in (10) are respectively 1, 2+1, and 3+2+1.

### 3.3 First-order nonlinear null signal at the trained affine state

Assume Gamma has rank two and v belongs to its null space. For every raw state and every e, the exact null decomposition is

\[
 v^Tf_e=eN_{v,e},\quad
 N_{v,e}=\langle C,a^2BA T_1+aBT_2+T_3\rangle,
 \quad T_\ell=\sum_i v_i\arctan z_i^\ell,\quad a=1-e.           \tag{12}
\]

Evaluate its e=0 coefficient at Theta^0(t):

\[
 N_v(t)=\langle C(t),B(t)A(t)\sum_i v_i\arctan z_i^1(t)
       +B(t)\sum_i v_i\arctan z_i^2(t)
       +\sum_i v_i\arctan z_i^3(t)\rangle.                    \tag{13}
\]

Thus N_v(t)=partial_e[v^Tf_e(Theta^0(t))] at e=0. Derivatives of a contribute only linear terms, annihilated by v.

Put m(q)=E(1+qG^2)^(-1), where G is standard Gaussian. Then

\[
                   m'(1)=-E\frac{G^2}{(1+G^2)^2}<0.            \tag{14}
\]

For the three terms of (13) set respectively

\[
 U_1=A(t)^*B(t)^*C(t),\qquad U_2=B(t)^*C(t),\qquad U_3=C(t).
\]

Joint Gaussian integration by parts, including singular joint covariances, gives

\[
 E[U_\ell\arctan z_i^\ell]
       =m(q_{\ell i})E[U_\ell z_i^\ell].                     \tag{15}
\]

At every affine state, sum_i v_i z_i^ell=0 exactly. Therefore sum_i v_i E[U_ell z_i^ell]=0 exactly; this cancellation includes every higher-order term of these covariances. Also (8)-(11) give E[U_ell z_i^ell]=t k_i+O(t^2) for all three layers. Subtract m(1) times the exact zero sum in (15), then apply (10):

\[
 \boxed{\quad
 N_v(t)=10m'(1)\left(\sum_i v_i(\Gamma y)_i^3\right)t^3
                  +O(t^4).\quad}                            \tag{16}
\]

The Taylor expansion may be differentiated: affine state covariances are smooth and m is smooth near q=1, while (15) is an exact formula there. Thus N_v'(t)=30m'(1)(sum_i v_i k_i^3)t^2+O(t^3).

This is generated by the unequal trained marginal variances in (10). It disappears if one incorrectly freezes the first layer and action maps or assumes all sample variances stay equal.

### 3.4 A separated triple with fast gap one and a nonzero coefficient

Take

\[
 u_1=(1,0),\quad u_2=(0,1),\quad
 u_3=(2^{-1/2},2^{-1/2}),\qquad y=(1,1,1).
\]

Its nonzero Gram eigenvalues are 2 and 1, and it is admissible for every delta<=1-1/sqrt(2). Let q=1/sqrt(2) and use the unnormalized null vector v=(-q,-q,1). Then

\[
 k=(1+q,1+q,1+2q),\qquad
 \sum_i v_i k_i^3=(1+2q)^3-2q(1+q)^3
                =\tfrac72+5q>0.                            \tag{17}
\]

Normalization divides v and every expression linear in v by sqrt(2). Hence (16) is nonzero for this fully realizable geometry. No vanishing fast input eigenvalue is involved.

### 3.5 The complete-kernel mixed term is first order in e

At initialization C=0, all hidden gradient blocks vanish. Therefore K_e(0)=Q_3(e). The Gaussian covariance recursion for phi_e=z+e(atan z-z) gives

\[
 Q_3(e)=\Gamma+6e(m(1)-1)\Gamma+O(e^2).
\]

Consequently the initialized strong/weak block is O(e^2).

Now evaluate the complete K_e at the actual trained affine state Theta^0(t), and write K^{(1)}(t)=partial_e K_e(Theta^0(t)) at e=0. Since the affine scalar predictor v^Tf_0 is identically zero on the **entire raw state space**, its raw gradient is identically zero. Differentiating (12) and the gradient-Gram identity therefore gives, for every sample vector u,

\[
 v^TK^{(1)}(t)u
 =\langle\nabla N_v(\Theta^0(t)),\nabla(u^Tf_0)(\Theta^0(t))
                                                    \rangle_{raw}.
                                                               \tag{18}
\]

The e derivative here is legitimate at a fixed affine state: arctangent and its first derivatives are bounded; finite-e forward fields converge in L2; the multiplier convergence against the fixed affine Gaussian backward fields follows by truncating their tails and then using dominated convergence. This uses the scalar weighted chain rule, not an unsupported Frechet derivative of an L2 Nemytskii map. It establishes the one-sided first-order expansion; no second-order state differentiability is required.

Along the true affine GF, (18) and the scalar chain rule imply

\[
 v^TK^{(1)}(t)(y-f_0(t))=N_v'(t)
   =30m'(1)\left(\sum_i v_i k_i^3\right)t^2+O(t^3).             \tag{19}
\]

The weak component of y-f_0 does not contribute, because v^TK^{(1)}v=0, again from the identically zero affine null gradient. Thus (17)-(19) prove that the **strong/weak** coefficient E^T K^{(1)}(t)v is nonzero at all sufficiently small positive t for the displayed triple. At any such fixed t,

\[
 E^TK_e(\Theta^0(t))v=e\,b_1(t)+o(e),\qquad b_1(t)\ne0.        \tag{20}
\]

Equation (20) is a calculation on the actual all-block evolving affine reference, not an assertion that the unknown global nonlinear trajectory equals that reference. It already rules out propagating the initialized O(e^2) coupling as a reference identity. Any differentiable local family of nonlinear flows would have the same first-order coefficient: the derivative through the state is zero for the null row at e=0 because that row is identically zero as a function of state. No such family theorem is assumed for the present conclusion.

Importantly, (20) is consistent with a correctly scaled Schur method. It does not refute one. The difficulty is retaining its order-e mixing and moving-constraint terms with sufficient uniform estimates, rather than claiming that small nonlinear curvature preserves initial orthogonality.

## 4. Why the known scalar readout-ascent lemma is not the constrained weak equation

There is an exact concrete correction, beyond a statement about missing symmetry. Let hidden parameters be h and let H(h):R^3->H_3 be the last-feature column operator. Put H_s=H E and H_w=H v. If the strong predictions are constrained to their target y_s=E^T y, and Q_ss=H_s^*H_s is invertible, the readout decomposes uniquely as

\[
 C=H_s Q_{ss}^{-1}y_s+C_\perp,\qquad H_s^*C_\perp=0.
\]

The remaining prediction is exactly

\[
 v^Tf=y_s^T Q_{ss}^{-1}H_s^*H_w+\langle C_\perp,H_w\rangle.
                                                               \tag{21}
\]

Both the offset in (21) and the orthogonality subspace of C_perp depend on the evolving hidden state. Projection of the full raw gradient onto this constraint also changes the hidden/readout metric. Thus one does not obtain the zero-readout unconstrained scalar system C'=H, h'=D H^* C to which the established convexity-of-readout-norm ascent lemma applies. One would need a new constrained ascent argument controlling the offset, projection metric, and moving constraint. Equations (5), (19), and (21) are three compatible manifestations of this issue.

## 5. A uniformly bounded affine neighborhood cannot complete the slow fit

This final obstruction is quantitative and concerns actual states of the target network. From (12), |atan|<=pi/2, and the raw-radius estimates ||A||,||B||,||C||<=U=11+R,

\[
 |v^Tf_e|\le\frac{3\pi}{2}e\|v\|_1U^3.                       \tag{22}
\]

For a unit null vector, after folding, |v^Ty|>=delta/2 by (3). If a state has ||f-y||_2<=delta/4, then |v^Tf|>=delta/4. Therefore

\[
 R\ge\left(\frac{\delta}{6\pi\sqrt3\,e}\right)^{1/3}-11.       \tag{23}
\]

For the fixed triple in (17), |v^Ty|=(sqrt(2)-1)/sqrt(2)>0 with unit v, so the same argument gives R>=c e^(-1/3)-11 for a fixed positive fitting accuracy. Its fast eigenvalues remain 2 and 1 at initialization. This precludes completing the fitting device inside any e-independent bounded affine neighborhood as e tends to zero. It does not preclude a nonlinear reference on a growing radius, nor a constant-amplitude witness theorem.

## 6. What this route has and has not established

The new established facts are (1)-(3), the exact Schur system (5), and the explicit all-block trained-reference expansion (16)-(20). They make a one-weak-mode proof substantially more precise: there really are only two strong input directions, but even an extremely well-conditioned pair of those directions generates first-order mixed coupling during actual hidden training. The initialized O(e^2) cancellation is not preserved.

A complete fast/slow proof still needs an invariant trained region with a positive fast kernel gap, a positive Schur slow coefficient, and control of the p' forcing and the moving readout constraint on the growing radius forced by (23). It would then need source-tail continuation and the original strong/action/GF/GD/observable bridge. No such region or source-compatible global continuation is established here. The note therefore supplies neither a new sufficient power of delta nor an unconditional global theorem.
