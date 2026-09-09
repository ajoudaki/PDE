# Three-input geometry and initial feature motion

Mathematical dependency of PROOF.md, 2026-09-07. Review status is recorded separately. The initial-law source proofs INITIAL_FEATURE_LEARNING.md and SYMMETRY_RADIAL_CLOCK.md are attached in sources/. Arguments below explicitly cover three samples rather than importing the two-sample exchange step. Section 5 supplies the explicit perturbation constant used by the assembled theorem.

Write \(u_a=x_a/\sqrt d\), \(\Gamma_{ab}=u_a\cdot u_b\), \(J=\mathbf1\mathbf1^T\), and assume \(\|u_a\|=1\), \(\Gamma_{ab}\le1-\delta\) for \(a\ne b\). When discussing initial feature ascent, use \(p=y/3\), \(m=\sum_a p_a\). Thus \(m\in\{-1,-1/3,1/3,1\}\); its nonvanishing is specific to three binary labels. Physical loss training has the same initial hidden acceleration multiplied by \(9\).

## 1. The augmented Gram has an explicit, order-sharp bound

For every feasible triple,
\[
             \Gamma+J\succeq \frac{\delta^2}{4}I_3.       \tag{1}
\]

Here is a direct proof, including singular ordinary Grams. For any real coefficient vector \(q\),
\[
 q^T(\Gamma+J)q=(\textstyle\sum q_a)^2+
                           \|\textstyle\sum q_a u_a\|^2.
\]
If its nonzero coefficients have one sign, the first term is at least \(\|q\|^2\), which implies (1) because \(\delta\le2\). Otherwise, changing its overall sign and permuting indices makes it \(q=(\alpha_1,\alpha_2,-b)\), where \(\alpha_i\ge0\), \(A=\alpha_1+\alpha_2>0\), and \(b>0\). Put
\[
 s=A-b,\qquad
 D=\frac{\alpha_1(1-u_1\cdot u_3)+\alpha_2(1-u_2\cdot u_3)}A
       \in[\delta,2].
\]
The projection of \(\sum q_a u_a\) onto \(u_3\) equals \(s-DA\). Consequently
\[
 q^T(\Gamma+J)q\ge(A-b)^2+((1-D)A-b)^2.
\]
This quadratic form in \((A,b)\) has matrix
\[
 \begin{pmatrix}1+(1-D)^2&-(2-D)\\-(2-D)&2\end{pmatrix},
\]
with determinant \(D^2\) and trace \(D^2-2D+4\le4\). Its smaller eigenvalue is at least determinant divided by trace, hence at least \(\delta^2/4\). Since \(A^2+b^2\ge\alpha_1^2+\alpha_2^2+b^2\), this proves (1).

The power \(\delta^2\) cannot improve. In two dimensions take
\[
 u_1=(1-\delta,\sqrt{2\delta-\delta^2}),\quad
 u_2=(1-\delta,-\sqrt{2\delta-\delta^2}),\quad u_3=(1,0).
\]
These satisfy the required pairwise bound for \(0<\delta\le3/2\). The coefficient vector \(q=(1,1,-2+\delta)\) gives
\[
 \frac{q^T(\Gamma+J)q}{\|q\|^2}
       =\frac{2\delta^2}{6-4\delta+\delta^2}
       \sim\frac{\delta^2}{3}.
\]
Thus (1) has the optimal separation order, though it does not assert the best possible constant.

Three distinct points of a sphere are affinely independent: a line intersects the sphere in at most two points. Equation (1) strengthens this observation quantitatively. Feasibility itself implies \(\delta\le3/2\), since
\(0\le\|u_1+u_2+u_3\|^2\le9-6\delta\).
For larger \(\delta\), the three-input class is empty. Examples with singular \(\Gamma\) include equilateral triples (null vector \(\mathbf1\)) and an antipodal pair plus an orthogonal third (null vector \((1,0,1)\)); neither makes \(\Gamma+J\) singular.

## 2. Initial forward and backward Grams for every positive nonlinearity

The argument also applies to the gain activation
\[
              \phi(z)=a(1+z)+e\arctan z,\qquad a>0,e>0.
\]
At the first layer, Gaussian projection onto constants and first Gaussian chaos gives
\[
 Q_1:=E[h^1(h^1)^T]\succeq a^2J+b_1^2\Gamma
                    \succeq a^2(J+\Gamma),              \tag{2}
\]
where \(b_1=a+eE[(1+G^2)^{-1}]\ge a\). To check this even for singular \(\Gamma\), write \(Z=\Gamma^{1/2}G_3\), project each scalar activation onto the linear span of the independent standard coordinates \(G_3\), and use Gaussian integration by parts; the orthogonal residual contributes a positive semidefinite Gram. The constant coefficient is \(a\) by oddness.

Every subsequent fresh preactivation vector is therefore nondegenerate Gaussian. Its coordinates have a common positive variance. The same projection, now with the appropriate variance, yields
\[
 Q_2\succeq a^2J+a^2Q_1,\qquad Q_3\succeq a^2J+a^2Q_2.
\]
In particular
\[
 Q_3\succeq a^6\Gamma+(a^2+a^4+a^6)J
          \succeq a^6(\delta^2/4)I_3.                   \tag{3}
\]

Set \(H=\sum p_a h_a^3\) and \(\beta_a^3=H\phi'(Z_a^3)\). Their Gram \(S_3\) is positive definite for every \(e>0\). Indeed, a zero linear combination would give the identity
\[
 [\textstyle\sum p_a\phi(z_a)]
             [\textstyle\sum v_a\phi'(z_a)]=0
                      \quad\hbox{on }\mathbb R^3,
\]
by full Gaussian support and continuity. The first factor has no open zero set, since its derivative in any coordinate is \(p_a\phi'(z_a)\ne0\). The second factor must therefore vanish everywhere. Differentiating in each \(z_a\) gives \(v_a\phi''(z_a)=0\), hence \(v_a=0\) because \(e>0\).

The supplied reused-transpose finite-program rule extends to three queries by the same finite transcript. It gives
\[
 B^*\beta_a^3=G_a^2+\sum_b h_b^2 E[\partial_{z_b}\beta_a^3],
\]
where \(G^2\) has covariance \(S_3\), independently of initial layer-two forward sources. Thus \(\beta_a^2=\phi'(Z_a^2)B^*\beta_a^3\) has a positive definite Gram \(S_2\), with
\(S_2\succeq a^2\lambda_{\min}(S_3)I\).
The second transpose gives an independent named layer-one Gaussian source with covariance \(S_2\). No inverse of \(\Gamma\) enters either return.

Consequently each hidden parameter acceleration is nonzero. For the first block,
\[
 dE\|V^1\|^2\ge a^2\lambda_{\min}(S_2)\sum_b p_b^2>0.
\]
For each of the two matrix blocks, its squared Hilbert--Schmidt norm is the trace pairing of its positive definite feature Gram and the Gram of its backward fields, conjugated by the invertible diagonal matrix \(\operatorname{diag}(p)\), hence is strictly positive.

For each particular first-layer sample,
\[
 U_a^1=\sum_b\Gamma_{ab}p_b\beta_b^1,
\quad
 \operatorname{Var}(U_a^1\mid Z^1)
 \ge a^2\lambda_{\min}(S_2)\sum_b\Gamma_{ab}^2p_b^2
 \ge a^2\lambda_{\min}(S_2)p_a^2>0.                     \tag{4}
\]
All first-layer feature accelerations are nonzero because \(\phi'\ge a\).

## 3. Every upper sample: an affine lower bound, then direct transfer

Aggregate adjunction proves only that at least one upper sample moves. The following argument establishes a strictly positive lower bound separately for every upper sample without sample symmetry.

First set \(e=0\), keeping any gain \(a>0\). Initial actions \(A,B\) are the canonically generated limits of independent square Gaussian matrices with entry variance \(1/n\). Put \(z_p=\sum p_bZ_b^1\), \(c_j=(\Gamma p)_j\), and
\[
 v=a^2m\mathbf1+a^3A(m\mathbf1+z_p),\qquad
 H=am\mathbf1+Bv,\qquad Q=B^*H.
\]
Direct differentiation of the three hidden blocks gives
\[
 U_j^2=a^4[(c_j+m)I+c_jAA^*]Q,                          \tag{5}
\]
\[
 U_j^3=a^5T_jH,\qquad
 T_j=[c_j+(1+a^{-2})m]I+(c_j+m)BB^*
                                      +c_jBAA^*B^*.    \tag{6}
\]
For example the affine first-layer feature Gram is \(a^2(\Gamma+J)\); the second-layer feature Gram is \(a^4\Gamma+(a^2+a^4)J\). Substituting their \(j\)-th row contractions with \(p\), and the gates \(\phi'=a\), gives (5)--(6).

For (5), condition a finite Gaussian array on \(A,z_p\). Direct Gaussian fourth moments give
\[
 E_B Q=v,\qquad
 \operatorname{Cov}_B(Q)
   =(a^2m^2+\|v\|_n^2)I+vv^T/n.
\]
Let \(L=(c_j+m)I+c_jAA^*\). Therefore
\[
 E_B\|LQ\|_n^2
  \ge(a^2m^2+\|v\|_n^2)\,\frac1n\operatorname{tr}L^2.
\]
The fixed Gaussian polynomial transcript has deterministic population moments, so this inequality passes to the population. Wick's formula gives
\(n^{-1}\operatorname{tr}AA^*\to1\) and
\(n^{-1}\operatorname{tr}(AA^*)^2\to2\), while
\(\|v\|_n^2\to a^4m^2+a^6(m^2+p^T\Gamma p)\).
Hence
\[
 \|U_j^2\|^2\ge
 a^8[a^2m^2+a^4m^2+a^6(m^2+p^T\Gamma p)]
                    [(m+2c_j)^2+c_j^2]
 \ge\frac{a^8m^4}{5}(a^2+a^4+a^6)>0.                  \tag{7}
\]
The final inequality uses the exact quadratic minimum
\(\inf_c[(m+2c)^2+c^2]=m^2/5\).

For (6), \(T_j\) is even under \(B\mapsto-B\), whereas \(Bv\) is odd. Thus the deterministic population cross term between \(T_j(am\mathbf1)\) and \(T_jBv\) vanishes. Orthogonal invariance of the Gaussian output rows then gives
\[
 \|U_j^3\|^2\ge a^{12}m^2\tau(T_j^2),                 \tag{8}
\]
where \(\tau\) denotes the limiting normalized trace. Write \(S=BB^*\), \(R=BAA^*B^*\). The needed Gaussian moments are
\[
 \tau(S)=\tau(R)=1,\quad \tau(S^2)=\tau(SR)=2,
                      \quad \tau(R^2)=3.
\]
These require no spectral theorem beyond Gaussian moments. For the last identity, with \(M=B^*B\), Gaussian fourth moments give exactly
\[
 E_A\frac1n\operatorname{tr}(AA^*M AA^*M)
  =(1+1/n)\frac1n\operatorname{tr}M^2
                              +(\operatorname{tr}M/n)^2\to3.
\]
The \(SR\) identity follows by \(E_AAA^*=I\); the remaining identities are the first two square-Gaussian moments. The same Wick calculation shows convergence of the finitely many polynomial contractions to their expectations. Equivalently they follow from the supplied fixed polynomial transcript identification.

Put \(t=a^{-2}\). Expanding (8) gives
\[
 \tau(T_j^2)=[3c_j+(2+t)m]^2+(2c_j+m)^2+c_j^2
         \ge\frac{6+8t+5t^2}{14}\,m^2.
\]
Consequently
\[
 \|U_j^3\|^2\ge
   \frac{a^{12}m^4}{14}(6+8a^{-2}+5a^{-4})>0.           \tag{9}
\]
For \(a=1\), (7) and (9) simplify to \(3m^4/5\) and \(19m^4/14\). Because \(|m|\ge1/3\), these are uniform positive bounds over all feasible three-input Grams and all binary label patterns.

The transfer to sufficiently small positive \(e\) is direct on the same initial actions. The pointwise bounds
\[
 |\phi_e(z)-a(1+z)|\le\pi e/2,\qquad
                         |\phi_e'(z)-a|\le e
\]
give, by the three forward passes, uniform \(O_a(e)\) differences in every initial feature and in \(H\). Backward induction gives \(O_a(e)\) differences in all \(\beta^\ell\), because the gates are bounded by \(a+e\) and the initial actions have norm at most 10. Rank-one difference bounds give the same estimate for all parameter accelerations. Finally use
\[
 U_j^2=V^2h_j^1+A[\phi'(Z_j^1)U_j^1],\quad
 U_j^3=V^3h_j^2+B[\phi'(Z_j^2)U_j^2]
\]
to obtain \(\|U_{j,e}^\ell-U_{j,0}^\ell\|_2\le C(a)e\), \(\ell=2,3\), with one finite \(C(a)\) independent of \(\Gamma,d,y\). Choosing \(e\) below half the square roots of (7),(9), divided by \(C(a)\), preserves every upper sample's nonzero acceleration. This argument does not use continuity of a singular query inverse or an unspecified covariance-dependent threshold.

The nonlinear argument of Section 2 handles all bottom samples, even where the affine bottom motion is zero. For example, an equilateral triple with all labels equal has \(\Gamma p=0\), so its affine bottom acceleration vanishes. This does not obstruct positive nonlinear motion.

The usual adjunction expansion now gives a changing projected kernel: in scalar feature time, \(\kappa(s)=\kappa(0)+2s^2\|V\|_{\rm hidden}^2+o(s^2)\). It also holds directly in physical time without scalar reduction: with \(p=y/3\), \(C(t)=3tH+o(t)\), the hidden displacement is \(9t^2V/2+o(t^2)\), and hence
\(\kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2)\).

## 4. What this does and does not refute

There is no geometry or initial-motion counterexample found to the requested three-input theorem. Pairwise separation supplies exactly the augmented-rank property needed for initial feature Grams, including every singular ordinary Gram.

The two-sample scalar clock does fail in general, already at initialization. For three orthogonal inputs and labels \((1,1,-1)\), the initial top feature Gram has diagonal \(q\) and strictly positive off-diagonal \(c\). (At the first layer independence gives positive off-diagonal \(a^2\); subsequent positive Gaussian correlations and increasing activations preserve positivity.) Therefore
\[
 Q_3y=(q,q,2c-q)^T
\]
is not parallel to \(y\). Since initially \(\dot f=Q_3y\), the population prediction path does not satisfy \(f_a=y_ag\). This defeats use of the two-sample scalar physical clock, but is not a counterexample to global existence, nonaffinity, or the width/GD conclusions.

Global all-time nonaffinity and a complete population/GF/GD bridge still require the parent proof's new global construction. They cannot be inferred from the initial-law statements in this report.

## 5. One fully numerical upper-motion perturbation cutoff

For a gain \(a\ge1\), an explicit sufficient choice for Section 3 alone is
\[
                    0<e\le (10^{10}a)^{-1}.             \tag{10}
\]
It is independent of the geometry and labels. Here are reproducible coarse bounds, with \(e\le1\), initial action norms at most 10, and \(\sum|p|=1\). Bounds without a difference refer to the nonlinear initial field, and \(\Delta\) means nonlinear minus affine:
\[
\begin{array}{c|c|c}
\text{field}&\text{norm upper bound}&\text{difference upper bound}\\\hline
h^1&4a&2e\\
h^2&43a^2&22ae\\
h^3\text{ and }H&433a^3&222a^2e\\
\beta^3&866a^4&655a^3e\\
\beta^2&17320a^5&15210a^4e\\
\beta^1\text{ and }U_j^1&346400a^6&325300a^5e
\end{array}
\]
The table follows successively from \(\|Z_j^1\|_2=1\), \(\pi/2<2\), and the action/gate bounds. For the parameter accelerations it gives
\[
 \|V_e^2\|_{HS}\le69280a^6,\quad
 \|\Delta V^2\|_{HS}\le65060a^5e,
\]
\[
 \|V_e^3\|_{HS}\le37238a^6,\quad
 \|\Delta V^3\|_{HS}\le32807a^5e.
\]
The affine bounds used here are
\(\|\beta_0^3\|\le211a^4\), \(\|\beta_0^2\|\le2110a^5\),
\(\|V_0^2\|_{HS}\le4220a^6\), and \(\|V_0^3\|_{HS}\le4431a^6\).
The two preactivation product rules then yield
\[
 \|U_{j,e}^2\|\le7205120a^7,\quad
 \|\Delta U_j^2\|\le6985680a^6e<7\cdot10^6a^6e,
\]
\[
 \|\Delta U_j^3\|\le143416183a^7e
                          <1.5\cdot10^8a^7e.
\]
The affine lower bounds (7),(9), using \(|m|\ge1/3\), imply
\[
 \|U_{j,0}^2\|\ge a^7/\sqrt{405},\qquad
 \|U_{j,0}^3\|\ge a^6/\sqrt{189}.
\]
Substitution of (10) makes both perturbations smaller than half their respective lower bounds. These constants concern initial upper-sample motion only; they do not select a coefficient sufficient for any separate global continuation argument.

Here is the full scalar induction behind these constants. It also fixes a common comparison constant explicitly. For every sample let \(D_e^\ell=\phi_e'(Z_{j,e}^\ell)\). Then
\[
 \|D_e^\ell\|_\infty\le2a,\qquad
 \|D_e^\ell-a\|_\infty\le e.
\]
All initial actions are identical in the two calculations. The forward bounds are
\[
 \|h_e^1\|\le2a+2\le4a,
 \quad \|h_e^2\|\le a+10a(4a)+2\le43a^2,
 \quad \|h_e^3\|\le a+10a(43a^2)+2\le433a^3,
\]
\[
 \|\Delta h^1\|\le2e,
 \quad\|\Delta h^2\|\le10a(2e)+2e\le22ae,
 \quad\|\Delta h^3\|\le10a(22ae)+2e\le222a^2e.
\]
The affine forward bounds are \(2a,21a^2,211a^3\), respectively. Since \(H=\sum p_jh_j^3\), the same third-layer bounds apply to \(H\) and its difference.

The backward identities and their exact difference decompositions are
\[
 \beta_e^3=D_e^3H_e,\qquad
 \Delta\beta^3=a\Delta H+(D_e^3-a)H_e,
\]
\[
 \beta_e^2=D_e^2B^*\beta_e^3,\qquad
 \Delta\beta^2=aB^*\Delta\beta^3+(D_e^2-a)B^*\beta_e^3,
\]
\[
 \beta_e^1=D_e^1A^*\beta_e^2,\qquad
 \Delta\beta^1=aA^*\Delta\beta^2+(D_e^1-a)A^*\beta_e^2.
\]
Therefore their successive norm bounds are \(2\cdot433=866\),
\(20\cdot866=17320\), and \(20\cdot17320=346400\), with the powers of \(a\) listed in the table. The successive difference coefficients are
\[
 222+433=655,\quad 10\cdot655+10\cdot866=15210,
 \quad10\cdot15210+10\cdot17320=325300.
\]
The powers are \(a^3e,a^4e,a^5e\), respectively. The first sample acceleration is \(U_j^1=\sum_b\Gamma_{jb}p_b\beta_b^1\); \(|\Gamma_{jb}|\le1\) and \(\sum|p_b|=1\) give exactly the same bounds for it.

For the matrix-block accelerations, use the rank-one identity
\(\Delta(\beta\otimes h)=\Delta\beta\otimes h_e+\beta_0\otimes\Delta h\), and sum with absolute coefficients \(|p_b|\). This gives
\[
 \|\Delta V^2\|_{HS}
 \le[(15210)(4)+(2110)(2)]a^5e=65060a^5e,
\]
\[
 \|\Delta V^3\|_{HS}
 \le[(655)(43)+(211)(22)]a^5e=32807a^5e.
\]
The corresponding nonlinear norm coefficients are \((17320)(4)=69280\) and \((866)(43)=37238\). The affine coefficients are \((2110)(2)=4220\) and \((211)(21)=4431\).

Finally expand the preactivation acceleration differences as
\[
 \Delta U_j^2=(\Delta V^2)h_{j,e}^1+V_0^2\Delta h_j^1
        +A[a\Delta U_j^1+(D_e^1-a)U_{j,e}^1],
\]
\[
 \Delta U_j^3=(\Delta V^3)h_{j,e}^2+V_0^3\Delta h_j^2
        +B[a\Delta U_j^2+(D_e^2-a)U_{j,e}^2].
\]
The bound for \(U_{j,e}^2\) has coefficient
\((69280)(4)+(10)(2)(346400)=7205120\), multiplying \(a^7\).
The two difference bounds have coefficients
\[
 (65060)(4)+(4220)(2)+10(325300+346400)
                          =6985680
\]
with factor \(a^6e\), and
\[
 (32807)(43)+(4431)(22)+10(6985680+7205120)
                          =143416183
\]
with factor \(a^7e\). Thus a common explicit constant is
\[
 C(a)=2\cdot10^8a^7,\qquad
       \|\Delta U_j^\ell\|_2\le C(a)e,\quad\ell=2,3.    \tag{11}
\]
For clarity the affine lower bounds in the exact normalization \(p=y/3\) are
\[
 \|U_{j,0}^2\|\ge\frac{a^7}{9\sqrt5},\qquad
 \|U_{j,0}^3\|\ge\frac{a^6}{9}\sqrt{\frac37}.
\]
Under (10), (11) is at most \(a^6/50\). Since \(a\ge1\),
\[
 \frac{a^6}{50}<\frac{a^7}{18\sqrt5},\qquad
 \frac{a^6}{50}<\frac{a^6}{18}\sqrt{\frac37},
\]
so each perturbation is strictly smaller than half its own affine norm lower bound, as claimed.
