# Fixed Gaussian source operators and projected physical dynamics

2026-09-08. The principal activation is always
\(\phi(z)=a(1+z)+e\tanh z\), with \(a=3/4,e=1/4\). This note proves a fixed-operator source decomposition, Gaussian compression estimates, and cap-independent Osgood estimates for projected returns. It does **not** close the full population/finite-algorithm contract: the unprojected backward component identified below remains uncontrolled by the projected estimates.

## 1. Fixed domains and the common-time decomposition

Use the canonical common spaces \(H_1=L^2(\Omega_1)\), \(H_2=L^2(\Omega_2)\) constructed from the countable generated-program language. That language includes a matrix query on each generated input and finite unions of programs. Its generated linear spans are dense in the corresponding Hilbert spaces. The finite-program source identities apply first to admissible smooth finite programs, including every fixed cap and fixed mesh.

For each generated bottom input \(h\), denote its primitive forward source by \(\xi_h\). For each generated top input \(b\), denote its primitive reverse source by \(\zeta_b\). Their covariance rules are

\[
E[\xi_h\xi_{\tilde h}]=\langle h,\tilde h\rangle_{H_1},
\qquad
E[\zeta_b\zeta_{\tilde b}]=\langle b,\tilde b\rangle_{H_2}.
\tag{1}
\]

**Proposition 1.** There are fixed linear isometries

\[
F:H_1\longrightarrow H_2,\qquad R:H_2\longrightarrow H_1,
\quad Fh=\xi_h,\quad Rb=\zeta_b,
\]

whose closed ranges consist of centered Gaussian first-chaos variables. On the full generated spaces the initialized action satisfies

\[
A_0=F+R^*,\qquad A_0^*=F^*+R.
\tag{2}
\]

Here \(F,R\) and their domains do not change with time, cap, or mesh. Their ranges need not exhaust all first Gaussian-chaos directions in the layer spaces; for example the initial first-layer Gaussian root is independent of the reverse source group.

**Proof.** Equation (1) makes each source assignment linear and isometric on the generated span: any linear combination of inputs with zero norm has a source combination with zero variance. Thus the assignment is well-defined on equivalence classes and extends uniquely by continuity from the dense span. Its range is closed because it is an isometry. Every finite source combination is centered Gaussian, and an \(L^2\) limit remains Gaussian by convergence of its variances and characteristic functions. In particular \(F^*F=I\), \(R^*R=I\).

For a finite forward call the exact source rule is

\[
A_0h=Fh+\sum_s\alpha_s b_s,
\qquad \alpha_s=E[\partial_{\zeta_{b_s}}h].
\]

Gaussian integration by parts gives, for every reverse input \(b\) in any finite union program,

\[
\langle h,Rb\rangle
=\sum_s\alpha_s\langle b_s,b\rangle.
\]

This remains true for a reverse input queried later: append its source to the same Gaussian group; the formal expression for \(h\) has zero derivative in unavailable coordinates, and Gaussian integration by parts retains its correlations with those coordinates. Singular source covariances cause no problem, since one can write the finite source vector as a linear image of independent standard Gaussians. Thus the return equals \(R^*h\), by testing against the dense generated top span. Equation (2) holds on the generated bottom span and extends by boundedness to \(H_1\); taking genuine adjoints gives its reverse identity. ∎

Write \(P_R=RR^*\), \(P_F=FF^*\) for the orthogonal projections onto these source ranges. The decomposition yields \(\|A_0\|\le2\). It does not make the two summands in (2) orthogonal or independent. In particular \(Fh\) can be correlated with \(R^*h\), because the latter is a top-layer adapted variable. Also \(F^*1=R^*1=0\), whereas the forward effect of a constant input is the nonzero Gaussian vector \(F1\). Thus the activation offset remains in the forward dynamics.

Once a strong path or fixed-cap path exists on these canonical spaces, (2) applies at every time by continuity. No source-derivative integrability assertion for an unconstructed uncapped path is needed to use this bounded-operator identity.

## 2. Gaussian compressions and an Osgood operator estimate

In this section \(G:H\to L^2(\Omega)\) is any linear isometry whose range is a centered Gaussian first-chaos space. If \((e_j)\) is an orthonormal basis of \(H\), then \(Z_j=Ge_j\) are independent standard Gaussians. Write \(M_m\) for multiplication by \(m\).

**Lemma 2 (compression).** For bounded real \(m\),

\[
G^*M_mG=(Em)I+K_m,
\quad
\|K_m\|_{\rm HS}\le\sqrt2\|m-Em\|_2,
\tag{3}
\]

and

\[
\|K_m-K_{\tilde m}\|_{\rm HS}\le\sqrt2\|m-\tilde m\|_2.
\tag{4}
\]

**Proof.** The matrix entries of the remainder are

\[
(K_m)_{jk}=E[m(Z_jZ_k-\delta_{jk})].
\]

The variables \((Z_j^2-1)/\sqrt2\) and \(Z_jZ_k\), \(j<k\), form an orthonormal family in \(L^2\). This follows directly from independence, centered odd Gaussian moments, \(EZ_j^2=1\), and \(EZ_j^4=3\). Therefore Bessel's inequality gives

\[
\sum_{j,k}|(K_m)_{jk}|^2
=2\left[\sum_j\left|E[m(Z_j^2-1)/\sqrt2]\right|^2
+\sum_{j<k}|E[mZ_jZ_k]|^2\right]
\le2\|m-Em\|_2^2.
\]

Finite basis compressions and monotone convergence prove the Hilbert--Schmidt assertion. Apply the same result to \(m-\tilde m\) for (4). ∎

For \(m_{ij}=\phi'(z_i)\phi'(z_j)\), one has \(a^2\le m_{ij}\le1\). Since a variable in an interval of length \(L\) has variance at most \(L^2/4\), (3) gives

\[
\|K_{m_{ij}}\|_{\rm HS}\le\frac{1-a^2}{\sqrt2}
=\frac7{16\sqrt2}.
\tag{5}
\]

For justification of the variance bound, if \(X\in[l,u]\), then \(E[(X-l)(u-X)]\ge0\), so \(\operatorname{Var}(X)\le(EX-l)(u-EX)\le(u-l)^2/4\).

There is also a stronger continuity estimate for the *uncompressed* projected multiplication operator.

**Lemma 3 (Gaussian multiplier modulus).** Suppose \(\|d\|_\infty\le K\), \(s=\|d\|_2\), and \(0<s\le K\). Then

\[
\|M_dG\|_{H\to L^2}
=\|G^*M_d\|_{L^2\to H}
\le\omega_K(s):=4s\sqrt{\log(eK/s)}.
\tag{6}
\]

Set \(\omega_K(0)=0\). The estimate does not assume independence of \(d\) and the source group. It acts on arbitrary incoming \(L^2\) vectors on the adjoint side.

**Proof.** For any unit \(u\in H\), \(Gu\) is standard Gaussian; write it as \(Z\). For \(L>0\),

\[
\|dZ\|_2\le Ls+K\|Z1_{|Z|>L}\|_2.
\]

The elementary Gaussian Chernoff bound \(P(|Z|>L)\le2e^{-L^2/2}\), obtained by completing the square in \(Ee^{tZ}=e^{t^2/2}\), and Cauchy--Schwarz imply

\[
\|Z1_{|Z|>L}\|_2\le6^{1/4}e^{-L^2/8}.
\]

Choose \(L=\sqrt{8\log(eK/s)}\). The right side is at most \(4s\sqrt{\log(eK/s)}\). Taking the supremum over unit \(u\) proves the first bound; adjoint equality proves the second. ∎

This is an Osgood modulus: \(\int_{0+}ds/\omega_K(s)=\infty\), by the substitution \(x=\log(eK/s)\). Thus a closed comparison using only this modulus could yield uniqueness. The word “closed” is essential; Section 5 identifies the variable which the present bounds do not control.

For unbounded \(m\in L^2\), (3) still defines a bounded *Gaussian compression form*, with matrix \(E[mZ_jZ_k]\) and operator norm at most \(|Em|+\sqrt2\|m\|_2\). This follows by truncating \(m\) in \(L^2\) and using (4). It must not be identified with the composition \(G^*M_mG\) on its usual \(L^2\) domain without checking that multiplication lands in \(L^2\). This distinction matters for formal time derivatives involving \(C\phi''(v)\).

## 3. Exact physical splitting and the noncompact cross-return

Define fixed-space response coefficients and orthogonal components by

\[
\alpha_i=R^*h_i\in H_2,\qquad h_i^\perp=(I-P_R)h_i,
\]

\[
\beta_i=F^*b_i\in H_1,\qquad b_i^\perp=(I-P_F)b_i.
\]

Let \(S_1=RF:H_1\to H_1\), \(S_2=FR:H_2\to H_2\); these are fixed isometries. The actual fields satisfy

\[
v_i=(I+S_2)\alpha_i+Fh_i^\perp+Uh_i,
\tag{7}
\]

\[
q_i=(I+S_1)\beta_i+Rb_i^\perp+U^*b_i.
\tag{8}
\]

All initialized returns and learned feedback remain present. In particular the primitive reverse Gaussian source has covariance determined by the *whole* \(b_i\), not only by \(F\beta_i\).

For an existing strong physical path, \(\alpha_i\) is strongly differentiable because \(h_i\) is. Put \(c_i=y_i-f_i\) and \(m_{ij}=\phi'(z_i)\phi'(z_j)\). Then

\[
\dot\alpha_i=\sum_j\Gamma_{ij}c_j
R^*M_{m_{ij}}(Rb_j+F^*b_j+U^*b_j).
\tag{9}
\]

The primitive term equals \((Em_{ij})b_j+K_{m_{ij}}b_j\). Splitting \(F^*b_j\) into reverse-first-chaos and orthogonal parts gives the complete identity

\[
\begin{aligned}
\dot\alpha_i=\sum_j\Gamma_{ij}c_j\big[&
(Em_{ij})(b_j+S_2^*b_j)
+K_{m_{ij}}(b_j+S_2^*b_j)\\
&+R^*M_{m_{ij}}(I-P_R)F^*b_j
+R^*M_{m_{ij}}U^*b_j\big].
\end{aligned}
\tag{10}
\]

The shift \(S_2^*\) is not compact in infinite dimension: for an orthonormal sequence \(e_n\), it sends the orthonormal sequence \(S_2e_n\) to \(e_n\). The off-chaos term in (10) is also not generally Hilbert--Schmidt. For example let bounded nonconstant \(m\) depend only on an independent bottom root, take \(Em=0\), and set \(v_n=mRe_n/\|m\|_2\). These vectors are orthonormal, lie in \((I-P_R)H_1\), and satisfy \(R^*M_m v_n=\|m\|_2e_n\). Since \(F^*\) maps \(Fv_n\) to \(v_n\), the off-chaos operator preserves a nonzero norm on an orthonormal sequence. It cannot be replaced by a compact perturbation.

Nevertheless Lemma 3 controls its changes, together with every other term in (9), without incoming-field tails. On bounded state balls,

\[
\|R^*(M_m-M_{\tilde m})A^*b\|_2
\le\omega_K(\|m-\tilde m\|_2)\|A\|\|b\|_2.
\tag{11}
\]

Here \(\|m_{ij}-\tilde m_{ij}\|_2\le\tfrac12(\|z_i-\tilde z_i\|_2+\|z_j-\tilde z_j\|_2)\), and one may take \(K=1-a^2\). Changes of \(A\), \(b\), and the physical residual are bounded by their ordinary norm differences. Thus the right side of (9) has a cap-independent Osgood estimate in the variables \((z,U,b,c)\).

The sample block with entries \(\Gamma_{ij}R^*M_{m_{ij}}R\) is positive semidefinite: its quadratic form is the expectation of \(\|\sum_i u_i\phi'(z_i)Rv_i\|^2\). But (9) is driven by \(c_jb_j\), and the remaining terms in (10) persist. Positivity of that one block is not a dissipativity identity for \(\alpha\) alone. The true loss dissipation remains the full raw gradient identity.

## 4. Projected reverse gates and readout coefficients

Lemma 3 also gives an unconditional bounded-ball estimate for the projected reverse gate:

\[
\begin{aligned}
\|F^*[C\phi'(v)]-F^*[\tilde C\phi'(\tilde v)]\|_2
\le{}&\|C-\tilde C\|_2\\
&+\|\tilde C\|_2\,
\omega_{1-a}(\|\phi'(v)-\phi'(\tilde v)\|_2).
\end{aligned}
\tag{12}
\]

The multiplier difference is bounded by \(1-a=1/4\), and its \(L^2\) norm is at most \(\tfrac12\|v-\tilde v\|_2\). This uses the fixed adjoint \(F^*\) on the full product, so it does handle an arbitrary incoming \(L^2\) readout. In particular it is stronger than estimating the unprojected gate first.

To keep the offset and remaining components explicit, put

\[
\gamma=F^*C,\qquad C^\perp=(I-P_F)C,
\qquad s_i=\operatorname{sech}^2(v_i).
\]

Compression gives

\[
\beta_i=(a+eEs_i)\gamma+eK_{s_i}\gamma
+eF^*M_{s_i}C^\perp.
\tag{13}
\]

The physical readout equation and (2) give

\[
\dot\gamma=a\sum_i c_i[h_i+F^*\alpha_i+F^*Uh_i]
+e\sum_i c_iF^*\tanh(v_i),
\tag{14}
\]

\[
\dot C^\perp=a\Big(\sum_i c_i\Big)1
+a\sum_i c_i(I-P_F)(\alpha_i+Uh_i)
+e\sum_i c_i(I-P_F)\tanh(v_i).
\tag{15}
\]

These are exact strong identities. The nonlinear remainder \((I-P_F)\tanh(v_i)\) is a bounded variable minus a centered Gaussian of variance at most one, so its individual subGaussian norm has a universal bound. This observation does not control the other forcing terms in (15).

One must be more careful with a formal derivative of \(\beta_i\). Although \(b_i\) is continuous in \(L^2\), its formal derivative contains \(C\phi''(v_i)\dot v_i\), which need not lie in \(L^2\) or have all the Gaussian test pairings required for a projected derivative. If a regularized path justifies this differentiation and one separates \(\dot v_i=F\dot h_i+\) remaining terms, the compression form for \(m=C\phi''(v_i)\in L^2\) controls the first term. The products with \(R^*\dot h_i\), \(U\dot h_i\), and \(\dot Uh_i\) require additional justification. Equations (12)–(15) avoid asserting this unjustified derivative.

On the energy-preserving cap family, all raw velocities are bounded on compact time intervals by the raw primal bounds, since all gates have magnitude at most one. Consequently \(z,h,v,C\) are uniformly Lipschitz in time in their respective \(L^2\) norms. Equations (4) and (12) then make \(K_{m_{ij}(t)}\) uniformly Lipschitz in time in HS norm and \(\beta_i(t)\) uniformly continuous with a modulus of order \(h\sqrt{\log(1/h)}\). These are time regularity estimates, not strong compactness across caps.

## 5. Exact obstruction to closing only the projected variables

The unprojected backward field remains

\[
b_i=C\phi'(v_i)=F\beta_i+b_i^\perp.
\]

Neither (12) nor the other projection identities control \(\|b_i^\perp-\tilde b_i^\perp\|_2\) from bounded raw norms and \(\|C-\tilde C\|_2+\|v_i-\tilde v_i\|_2\). Here is an exact test of that missing implication.

Choose events \(E_n\) with probabilities \(p_n\downarrow0\), a constant \(v_1\) for which \(\Delta=\phi'(v_1)-\phi'(0)\ne0\), and

\[
C_n=\rho p_n^{-1/2}1_{E_n},\qquad
v_n=v_1 1_{E_n},\qquad \tilde v_n=0.
\]

Then \(\|C_n\|_2=\rho\), \(\|v_n-\tilde v_n\|_2=|v_1|\sqrt{p_n}\to0\), but

\[
\|C_n[\phi'(v_n)-\phi'(\tilde v_n)]\|_2=\rho|\Delta|.
\]

By (12) the projection under \(F^*\) of this difference tends to zero. Orthogonality therefore implies that its \((I-P_F)\) component has norm tending to \(\rho|\Delta|\). The primitive reverse source of that component, \(R(b_n^\perp-\tilde b_n^\perp)\), is a centered Gaussian with the same nonvanishing variance. Thus projection can hide a macroscopic new reverse-source variance even when the projected returns converge.

This test concerns bounded-state estimates, not actual physical reachability. It shows exactly why an Osgood comparison for the projected coefficients alone is insufficient: the next primitive source, the learned-operator update, and (9) all still use the whole \(b\).

The first-layer unprojected equation has the parallel issue

\[
\dot z_i=\sum_j\Gamma_{ij}c_j\phi'(z_j)
(Rb_j+\beta_j+U^*b_j).
\]

Lemma 3 bounds a multiplier difference applied to \(Rb_j\), since this is Gaussian. It does not bound an unprojected multiplier difference applied to arbitrary returned \(\beta_j\) or learned \(U^*b_j\) by the same Osgood modulus. Moving an adjoint onto the entire product is available only after taking a projection or a pairing; doing so in the unprojected equation changes the quantity being estimated.

## 6. What HS compression does and does not give for concentration

For a *fixed* bounded multiplier \(m\) and a bounded weakly-null sequence \(b_n\), compactness of \(K_m\) gives

\[
\|K_m b_n\|_2\longrightarrow0.
\tag{16}
\]

To verify this without invoking a compactness theorem, approximate \(K_m\) in HS, hence operator, norm by a finite-rank basis truncation. The truncation sends a bounded weakly-null sequence to zero in norm because it has finitely many scalar coordinates. The operator-norm tail is uniformly small. Therefore the fixed compression transmits any such concentration only through \((Em)b_n\). The same conclusion is uniform over a compact HS family if the weak convergence is uniform against the finitely many test vectors in an approximating net.

The available energy estimates do not make the family \(K_{m_R(t)}\) compact across approximation levels. In fact uniform time regularity and a common initial value cannot do that. Let \(e_0,e_n\) be orthonormal vectors in \(H_2\), \(Z_0=Re_0,Z_n=Re_n\), and choose

\[
m_n(t)=m_0+\varepsilon f(t)\tanh Z_0\tanh Z_n,
\qquad f(0)=0,\quad |f|\le1,
\]

with fixed Lipschitz \(f\), \(m_0=(1+a^2)/2\), and \(0<\varepsilon<(1-a^2)/2\). These bounded multipliers have a common initial value and uniform \(L^2\)-Lipschitz time bounds. If \(\kappa=E[Z\tanh Z]>0\), independence and parity give exactly

\[
K_{m_n(t)}
=\varepsilon f(t)\kappa^2(e_0\otimes e_n+e_n\otimes e_0).
\tag{17}
\]

The HS family is not precompact whenever \(f(t)\ne0\). The vectors \(e_n\) may be chosen as normalized indicators of disjoint events of vanishing probability, with \(e_0\) on a separate event; then \(K_{m_n(t)}e_0\) has non-uniformly-integrable squared tails. If desired, each multiplier can have the exact pointwise form \(\phi'(z_n(t))^2\): the map \(z\mapsto\phi'(z)^2\) is smoothly invertible from \((0,\infty)\) onto \((a^2,1)\), and the displayed multiplier ranges inside a fixed compact subinterval. The resulting \(z_n(t)\) are bounded and uniformly Lipschitz in \(L^2\).

These paths are not asserted to solve the physical equations or to have the required Gaussian initialization. Their role is narrower: the stated multiplier bounds and time regularity alone do not imply the compactness needed to apply (16) with varying caps. A causal physical argument excluding this change of source directions would be new information. The mixed shift and off-chaos terms in (10) would still need to be retained in that argument.

## 7. Claim registry and remaining implication

| Claim | Status |
|---|---|
| Fixed common-space identity \(A_0=F+R^*\), genuine adjoint, Gaussian isometric ranges | Proved from the canonical finite-program construction |
| Scalar-plus-HS Gaussian compression and HS-Lipschitz dependence on the multiplier | Proved |
| Gaussian-first-chaos restriction and adjoint projection have a cap-independent Osgood multiplier modulus | Proved |
| Osgood stability of the projected reverse gate and of the forward-return velocity in \((z,U,b,c)\) | Proved |
| Projected coefficient equations are a closed passive finite system | Not proved; (10), (13), and \(b^\perp\) show the retained terms |
| Fixed-multiplier HS remainders vanish on bounded weakly-null inputs | Proved |
| Physical cap families have the multiplier compactness and unprojected concentration control needed to use that fact | Open |
| Principal global population and full actual GF/GD contract | Still open |

The next exact missing implication is control of \(b^\perp=(I-P_F)[C\phi'(v)]\), together with the unprojected returned/learned terms in the first-layer equation, along the actual energy-preserving approximation family. Proving a causal concentration-defect inequality for those quantities could finish a new route. The projection and compression estimates above neither establish nor rule out that physical inequality.
