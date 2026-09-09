# One-bottom-row cavity: exact return formula and the unresolved response

2026-09-08. This bounded subtask uses `CONTRACT.md` and the two plateau notes. It does not re-prove row confinement. The activation is the fixed bounded smooth plateau activation from `PLATEAU_GEOMETRY.md`, not the contract's principal affine–tanh activation.

**Finding.** Deleting one bottom feature produces a conditionally Gaussian cavity return with width-independent compact-time tails. The direct return and the trained-matrix return are also controlled. Transferring these bounds to the actual return still requires a response estimate for the other bottom rows. Their difference equation has a diagonal curvature term containing the actual or cavity return field. Bounded row amplitudes and a bound on its normalized second moment do not control that term. A concrete bounded-row saddle below proves that confinement alone cannot yield the needed deterministic sensitivity bound. This is not a counterexample to the physical GF or its proposed limit.

## 1. Notation and elementary compact-time bounds

Use \(\|z\|_n^2=n^{-1}\sum_a z_a^2\), the usual matrix operator norm, and the unnormalized Frobenius norm for \(A\). The normalized bottom variable is \(w_a=\sqrt d\,W_{a,:}\), with norm \(n^{-1}\sum_a\|w_a\|^2\). Let

\[
 B=\|\phi\|_\infty=3/2,\qquad
 M_1=\|\phi'\|_\infty,\qquad M_2=\|\phi''\|_\infty.
\]

All constants in this note may depend on the fixed inputs, these three activation constants, a fixed time \(T\), and deterministic bounds on \(\|A_0\|_{\rm op}\), \(\|C_0\|_\infty\), and initial losses. They do not depend on width. Statements made under these initial bounds are deterministic statements, not an invocation of an unproved random-matrix limit.

For any existing actual or cavity GF, write \(E_*\) for an upper bound on its initial loss, \(c_0\) for the initial readout sup norm, and \(K_0\) for its initial matrix operator norm. The exact GF energy identity gives

\[
 \sum_i|r_i(t)|\leq S:=\sqrt{6E_*}.
\]

Define successively

\[
 C_T=c_0+BST,\quad B_T=M_1C_T,\quad
 A_T=K_0+BB_TST,\quad Q_T=A_TB_T.
\]

Directly from the raw equations,

\[
 \|C(t)\|_\infty\leq C_T,\quad
 \|b_i(t)\|_\infty\leq B_T,\quad
 \|A(t)\|_{\rm op}\leq A_T,\quad
 \|q_i(t)\|_n\leq Q_T.
 \tag{1.1}
\]

For the matrix bound, integrate
\(\|\dot A\|_F\leq\sum_i|r_i|\|b_i\|_n\|h_i\|_n\leq S B_TB\), using the exact factor \(1/n\) in the matrix update. Also,

\[
 \|\dot w\|_n\leq M_1SQ_T,\quad
 \|\dot h_i\|_n\leq M_1^2SQ_T,\quad
 \|\dot C\|_n\leq SB.
\]

Consequently

\[
 \|\dot v_i\|_n\leq SB^2B_T+A_TM_1^2SQ_T=:V_T,
 \qquad
 \|\dot b_i\|_n\leq M_1SB+M_2C_TV_T=:L_T.
 \tag{1.2}
\]

These estimates control the mean-square return and the upper fields. They do not imply uniform integrability of \(q_i^2\) across widths. The row confinement theorem additionally bounds individual bottom primal amplitudes, but does not change that distinction.

## 2. Freezing is not deletion

Fix a bottom index \(k\), and write \(a_k=A_{0,:,k}\) for the original Gaussian column. It has independent entries \(N(0,1/n)\).

If only \(w_k\) is frozen at its initial value, its nonzero feature \(h_{i,k}(0)\) still enters the upper preactivation through \(a_kh_{i,k}(0)\). The outside trajectory therefore still depends on \(a_k\). One cannot condition on that trajectory and declare \(a_k^Tb_i\) a Gaussian linear functional of an independent column.

For genuine conditional independence, use an auxiliary **deleted-feature cavity**. Mask coordinate \(k\) to zero in all three first-layer feature vectors, keep \(w_k\) frozen, and evolve the remaining variables with the exact constrained raw GF. In particular, the masked \(k\)-th matrix column is not trained. Keep the denominator \(n\) in all formulas. This is an auxiliary comparison system, not a replacement architecture in the claimed limit theorem.

Denote this cavity by bars. It starts with the same \(A_0,C_0,w_a(0)\) for \(a\ne k\), but \(\bar h_{i,k}\equiv0\). Its used fields and outside trajectories are measurable with respect to

\[
 \mathcal F_{-k}=\sigma\big(A_{0,:,a}:a\ne k;\ C_0;\ w_a(0):a\ne k\big),
\]

and hence are independent of \(a_k\). This follows directly from the cavity equations: the unused column never appears in any forward field or outside update. Conditional claims below assume a uniquely specified cavity solution on the interval; at finite width the smooth vector field has local uniqueness, and the estimates concern its existing interval.

The direct missing upper preactivation is \(a_kh_{i,k}\), whose normalized norm is bounded by

\[
 \|a_kh_{i,k}\|_n\leq B\|a_k\|_2/\sqrt n.
 \tag{2.1}
\]

This is the correct direct \(n^{-1/2}\) forcing scale.

## 3. The independent cavity source has compact-time Gaussian tails

Set

\[
 G_{i,k}(t)=a_k^T\bar b_i(t).
\]

Conditional on \(\mathcal F_{-k}\), this is a centered Gaussian process, because each finite collection of its values is a linear function of the independent Gaussian column. Its covariance is exactly

\[
 \mathbb E[G_{i,k}(s)G_{j,k}(t)\mid\mathcal F_{-k}]
 =\langle\bar b_i(s),\bar b_j(t)\rangle_n.
 \tag{3.1}
\]

For this conditional estimate, repeat the derivation of the bounds on \(b\) and \(\dot b\) using the masked operator \(\bar A D_k\), where \(D_k\) is the diagonal matrix that zeros coordinate \(k\), and restrict lower velocities and returns to the other rows. This uses only \(K_0=\|A_0D_k\|_{\rm op}\), the cavity initial loss, and the initial readout bound, all of which are \(\mathcal F_{-k}\)-measurable. The unused tagged return is not included in that deterministic return bound. Thus the resulting bounds on \(\bar b_i\) and \(\dot{\bar b}_i\) have the same forms as (1.1)–(1.2) and are measurable with respect to the outside data. In particular, let \(B_0\) bound \(\|\bar b_i(0)\|_n\) and let \(L_T\) bound \(\|\dot{\bar b}_i(t)\|_n\). Then

\[
 \mathbb E[G_{i,k}(0)^2\mid\mathcal F_{-k}]\leq B_0^2,
 \qquad
 \mathbb E[\dot G_{i,k}(t)^2\mid\mathcal F_{-k}]\leq L_T^2.
\]

The fundamental theorem of calculus and the integral inequality
\((\int_0^T|g'|)^2\leq T\int_0^T|g'|^2\) give

\[
 \sup_{t\leq T}|G_{i,k}(t)|^2
 \leq2|G_{i,k}(0)|^2+2T\int_0^T|\dot G_{i,k}(t)|^2\,dt.
\]

Put \(\Sigma_T^2=2B_0^2+2T^2L_T^2\). Divide the preceding right-hand side by \(\Sigma_T^2\); it is a convex combination of \((G(0)/B_0)^2\) and the time average of \((\dot G(t)/L_T)^2\), with zero-weight terms omitted. Convexity of the exponential, followed by Gaussian integration, yields for \(0<\eta<1/2\)

\[
 \mathbb E\left[\exp\left\{\eta\frac{\sup_{t\leq T}|G_{i,k}(t)|^2}{\Sigma_T^2}\right\}
       \middle|\mathcal F_{-k}\right]
 \leq(1-2\eta)^{-1/2}.
\]

Here a centered Gaussian with variance at most one has exponential square moment at most \((1-2\eta)^{-1/2}\), obtained by integrating its Gaussian density. No independence between different times is required. In particular,

\[
 \mathbb P\left(\sup_{t\leq T}|G_{i,k}(t)|>u\mid\mathcal F_{-k}\right)
 \leq\sqrt2\exp\left(-\frac{u^2}{4\Sigma_T^2}\right).
 \tag{3.2}
\]

If \(\Sigma_T=0\), the process is identically zero. This proves the desired strong tail statement for the independent cavity source itself.

## 4. Exact tagged return identity

Integrating the actual matrix equation gives

\[
 A(t)=A_0-\frac1n\sum_{\ell=1}^3
       \int_0^t r_\ell(s)b_\ell(s)h_\ell(s)^T\,ds.
\]

Therefore the actual return to the tagged bottom row has the exact three-component Volterra identity

\[
 \boxed{\quad
 q_{i,k}(t)=G_{i,k}(t)
     +a_k^T\big(b_i(t)-\bar b_i(t)\big)
     -\sum_{\ell=1}^3\int_0^t
       r_\ell(s)h_{\ell,k}(s)
       \langle b_\ell(s),b_i(t)\rangle_n\,ds.
 \quad}
 \tag{4.1}
\]

The two-time inner product in the memory term retains the actual current return field \(b_i(t)\), the original repeated matrix, and the physical residual. No independence has been assigned to actual feedback fields.

The memory term has absolute value at most

\[
 BSB_T^2T.
 \tag{4.2}
\]

Thus only the propagated response
\(a_k^T(b_i-\bar b_i)\) remains unbounded by the preceding arguments.

## 5. What a successful response estimate would need

Let

\[
 X(t)=\|w_{-k}(t)-\bar w_{-k}(t)\|_n^2
       +\|A(t)-\bar A(t)\|_F^2
       +\|C(t)-\bar C(t)\|_n^2.
\]

The bottom norm omits the tagged row and keeps the factor \(1/n\). All compared state coordinates agree initially, so \(X(0)=0\). The tagged feature difference is bounded by \(B\), since the cavity masks it to zero. The Lipschitz bounds on \(\phi\) and \(\phi'\), together with (1.1), give successively

\[
 \|h_i-\bar h_i\|_n\leq M_1\sqrt X+B/\sqrt n,
\]

\[
 \|v_i-\bar v_i\|_n+|r_i-\bar r_i|
 +\|b_i-\bar b_i\|_n+\|q_i-\bar q_i\|_n
 \leq K_T(\sqrt X+n^{-1/2}).
 \tag{5.1}
\]

For example, \(v_i-\bar v_i=A(h_i-\bar h_i)+(A-\bar A)\bar h_i\); use \(\|A-\bar A\|_{\rm op}\leq\|A-\bar A\|_F\). Also \(q_i-\bar q_i=A^T(b_i-\bar b_i)+(A-\bar A)^T\bar b_i\), so the normalized return norm obeys the same estimate. These are actual differences, not Gaussian replacements.

If one could establish

\[
 \sup_{t\leq T}X(t)\leq K_T/n,
 \tag{5.2}
\]

then Cauchy–Schwarz and (5.1) would give

\[
 |a_k^T(b_i-\bar b_i)|
 \leq\|a_k\|_2\sqrt n\,\|b_i-\bar b_i\|_n
 \leq K_T\|a_k\|_2.
\]

Together with (3.2) and (4.2), this would control the actual tagged return. The independent Gaussian column norm has width-independent moments: for every positive integer \(p\), convexity gives

\[
 \mathbb E\|a_k\|_2^{2p}
 =\mathbb E\left(\frac1n\sum_j\xi_j^2\right)^p
 \leq\frac1n\sum_j\mathbb E|\xi_j|^{2p}
 =\mathbb E|N(0,1)|^{2p}<\infty.
\]

The missing statement is (5.2), or another estimate directly controlling the projection in (4.1).

## 6. The exact lower-row response term

For \(a\ne k\), put \(\Delta w_a=w_a-\bar w_a\), \(z_{i,a}=u_i\cdot w_a\), and define the bounded secant curvature

\[
 s_{i,a}=
 \begin{cases}
 [\phi'(z_{i,a})-\phi'(\bar z_{i,a})]/(z_{i,a}-\bar z_{i,a}),&z_{i,a}\ne\bar z_{i,a},\\
 \phi''(z_{i,a}),&z_{i,a}=\bar z_{i,a}.
 \end{cases}
\]

Then \(|s_{i,a}|\leq M_2\), by integrating \(\phi''\) along the segment. Exact subtraction of the two raw row equations gives

\[
 \Delta\dot w_a=H_a(t)\Delta w_a+F_a(t),
 \qquad
 H_a(t)=-\sum_i\bar r_i(t)\bar q_{i,a}(t)s_{i,a}(t)u_i u_i^T,
 \tag{6.1}
\]

where

\[
 F_a=-\sum_i\left[(r_i-\bar r_i)q_{i,a}
                  +\bar r_i(q_{i,a}-\bar q_{i,a})\right]
                 \phi'(z_{i,a})u_i.
\]

The normalized norm of \(F\) is bounded by \(K_T(\sqrt X+n^{-1/2})\), using (1.1) and (5.1). This isolates the coefficient that a direct stability proof must handle. Its row propagation matrix \(\Phi_a\), defined by \(\partial_t\Phi_a(t,s)=H_a(t)\Phi_a(t,s)\) and \(\Phi_a(s,s)=I\), obeys

\[
 \Delta w_a(t)=\int_0^t\Phi_a(t,s)F_a(s)\,ds,
 \qquad
 \|\Phi_a(t,s)\|\leq
 \exp\left(M_2\int_s^t\sum_i|\bar r_i(v)\bar q_{i,a}(v)|\,dv\right).
 \tag{6.2}
\]

These formulas follow by differentiating the product with the inverse fundamental matrix. The bound follows from the same integrating-factor integral inequality used in the confinement proof. Finite-dimensional linear equations with integrable coefficients can be constructed directly by the convergent iterated-integral series, bounded by the exponential series of the coefficient integral, so no additional existence result is needed here.

Taking squared norms in (6.1), and estimating the upper-variable difference equations by their multilinear forms, yields

\[
 \frac{d}{dt}X(t)
 \leq K_T X(t)+\frac{K_T}{n}
 +2M_2\sum_i|\bar r_i(t)|\,
       \frac1n\sum_{a\ne k}|\bar q_{i,a}(t)|\,\|\Delta w_a(t)\|^2.
 \tag{6.3}
\]

The last term is the obstacle. Replacing it by a maximum return gives a width-dependent exponential stability constant. Replacing it by the mean-square return gives only

\[
 \frac1n\sum_a|\bar q_{i,a}|\,\|\Delta w_a\|^2
 \leq\|\bar q_i\|_n
      \left(\frac1n\sum_a\|\Delta w_a\|^4\right)^{1/2}.
\]

Even if all row differences had a common deterministic amplitude bound \(D\), this is at most \(Q_TD\sqrt X\), rather than a constant times \(X\). Such a differential inequality with \(X(0)=0\) does not imply (5.2). The actual confinement envelope has Gaussian initial-row dependence and supplies no stronger cancellation in (6.3).

One can alternatively place the unbarred return in \(H_a\) by a different exact subtraction. This merely changes which dependent return field must be controlled.

## 7. The bounded self-return versus propagated cross-return

It is useful to separate the intuitive direct self-return from the term still missing. Write \(A=A_0+U\), \(\bar A=A_0+\bar U\), and \(\Delta h=h-\bar h\). Then

\[
 \Delta v_i=A_0\Delta h_i+(U-\bar U)h_i+\bar U\Delta h_i.
\]

Componentwise, with a secant \(m_i\) satisfying \(|m_{i,j}|\leq M_2\),

\[
 \Delta b_i=\phi'(v_i)\Delta C+\bar C\,m_i\,\Delta v_i.
\]

The part of \(a_k^T\Delta b_i\) coming from its own column in \(A_0\Delta h_i\) is

\[
 \Delta h_{i,k}\,a_k^T\operatorname{diag}(\bar C\,m_i)a_k,
\]

whose absolute value is at most \(BC_TM_2\|a_k\|_2^2\). Thus the proposed bounded direct self-return is valid even though the secant depends on the actual trajectory.

The other initial columns produce

\[
 \sum_{a\ne k}\Delta h_{i,a}\,
      a_k^T\operatorname{diag}(\bar C\,m_i)A_{0,:,a}.
\]

The coefficients \(\Delta h_{i,a}\) and \(m_i\) depend on the same original matrix and the actual feedback. Deterministic estimation gives a factor proportional to \(\sqrt n\|\Delta h_{i,-k}\|_n\); declaring independent Gaussian cancellation here would discard the very propagated response under investigation.

## 8. An explicit confined row with arbitrarily large sensitivity

This example refutes a control-independent Lipschitz response estimate based solely on the row amplitude envelope. It is not asserted to be a physical neural-network trajectory.

Take the admissible rank-two inputs

\[
 u_1=(1,0),\quad u_2=(-1/2,\sqrt3/2),\quad
 u_3=(-1/2,-\sqrt3/2).
\]

Their pairwise inner products are \(-1/2\), satisfying the contract for, for example, \(\delta=1/4\). Let \(g=\phi'\), \(w_*=(1/2,0)\), and prescribe constant controls

\[
 a_i=\frac{M}{g(u_i\cdot w_*)},\qquad M>0.
\]

These are finite and integrable on every compact interval. Since \(u_1+u_2+u_3=0\), the vector field
\(F(w)=\sum_i a_i g(u_i\cdot w)u_i\) satisfies \(F(w_*)=0\). Thus the row stays at the same bounded point for every \(M\).

For our activation, inside the transition

\[
 \frac{g'(z)}{g(z)}=-\frac{2z}{(1-z^2)^2}.
\]

At the three preactivations \((1/2,-1/4,-1/4)\), this equals respectively \(-16/9,128/225,128/225\). Directly summing the three outer products yields

\[
 DF(w_*)=M\begin{pmatrix}-112/75&0\\0&64/75\end{pmatrix}.
\]

Consequently the derivative of the time-\(T\) row map at \(w_*\), applied in direction \(e_2\), is

\[
 e^{64MT/75}e_2.
 \tag{8.1}
\]

To justify this last assertion directly, start at \(w_*+\epsilon e_2\), subtract the equilibrium integral equation, and divide by \(\epsilon\). The resulting coefficient is the integral of \(DF\) along the segment between the perturbed row and \(w_*\). For each fixed \(M,T\), the bounded derivative of \(F\) and the integral inequality give uniform convergence of the perturbed row to \(w_*\). The coefficient matrices therefore converge uniformly to \(DF(w_*)\). Subtracting the corresponding linear integral equations and applying the same integral inequality gives convergence of the difference quotients to the solution of \(J'=DF(w_*)J\), \(J(0)=e_2\), which is exactly (8.1).

All these trajectories still satisfy the confinement theorem. Thus bounded location does not bound the differential response. Nor does a normalized second-moment bound on the controls restore a general width-independent Lipschitz bound: among \(n\) independent row equations put \(M=\sqrt n\) in one row and zero in the others. The normalized sum of squared controls stays bounded, whereas the response operator in the normalized row metric has norm at least \(e^{64T\sqrt n/75}\). This last construction concerns arbitrary row perturbations; it does not establish that the specific Gaussian cavity forcing realizes the expanding direction with a problematic probability.

## 9. Exact remaining obligation

The one-row cavity provides an independent Gaussian source, a bounded direct self-return, and a bounded physical trained-matrix memory. A valid closure still needs one of the following, proved for the physical coupled GF with its original Gaussian matrix:

* a response bound strong enough to control \(a_k^T(b_i-\bar b_i)\), such as (5.2), with adequate moment control on its constant;
* a direct estimate of that scalar response that uses its actual Gaussian-column structure without assuming independence of propagated coefficients;
* a physical cancellation or integrability estimate for the return-weighted curvature term in (6.3), stronger than the available mean-square return bound.

The confinement theorem supplies a primal envelope for these arguments. It does not supply the missing response estimate, and the arbitrary-control saddle shows why that implication cannot be made on amplitudes alone. The global canonical population and raw-GD bridge remain outside the results proved here.
