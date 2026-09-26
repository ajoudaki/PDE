# Two-probe gradient-flow coefficients through middle-layer order six

This is an independent scoped algebra check using only the assigned finite vector field and the complete `jet_check.py`. The accompanying `p45_jet_check.py` compares a direct recurrence with that file's full-vector-field series oracle. It performs no training and makes no width-limit claim.

**Conclusion.** Under the ideal initial upper Gram identity, the middle-layer coefficient at position power \(t^5\) introduces no new factor functions beyond those through \(t^4\), after collecting label polynomials. Its scalar label coefficients are new. At position power \(t^6\), new factors can occur; an exact-Gram example below proves this. These statements use ordinary Taylor coefficients: position powers \(t^5,t^6\) correspond to velocity powers \(t^4,t^5\).

## 1. Normalization and notation

The physical inputs are \(\sqrt2 e_1,\sqrt2 e_2\), so the effective input coordinates are the two normalized axes. Both loss weights are \(1/2\). Let \(y\in\mathbb R^2\), \(w\in\mathbb R^{n\times2}\), \(A\in\mathbb R^{n\times n}\), and \(c\in\mathbb R^n\). With elementwise products understood,

\[
h=\tanh w,\quad Z=Ah,\quad H=\tanh Z,\quad f=H^Tc/n,\quad r=y-f,
\]
\[
\dot w=(1-h^2)\odot[A^T(c[:,None]\odot(1-H^2))]\odot r,
\]
\[
\dot A=((c[:,None]\odot(1-H^2))\odot r)h^T/n,
\qquad \dot c=Hr.
\tag{1}
\]

An input-index vector multiplying an \(n\times2\) array acts columnwise. All coefficients below are ordinary powers, with no factorial absorbed:
\(A(t)=A_0+A_2t^2+A_3t^3+\cdots\), and likewise for \(w,h,Z,H\). The readout satisfies \(c(0)=0\), \(c(t)=\sum_{j\ge1}c_jt^j\). Every hidden coefficient with index one is zero. Bare \(h,H,A\) below denote their initial values. Set

\[
P=1-h^2,\quad D=1-H^2,\quad
P'=-2hP,\quad D'=-2HD,\quad D''=2D(3H^2-1).
\tag{2}
\]

Here \(P'\) is the second derivative of \(\tanh\) at \(w_0\), while \(D',D''\) are the second and third derivatives at \(Z_0\). These primes refer to the activation argument, not time.

The recurrence in Section 2 retains the exact empirical Grams. Sections 3–5 impose

\[
h^Th/n=vI_2,\qquad H^TH/n=\tau I_2,
\quad v,\tau>0.
\tag{3}
\]

For population notation, normalized dot products are replaced by the designated expectations. The algebraic simplifications require (3); a generic finite random sample does not satisfy it exactly.

## 2. Compact recurrence through \(A_6\), with arbitrary empirical Grams

The following equations constitute a causal evaluation order. They require hidden coefficients only through order four and readout coefficients only through order five.

First compute

\[
c_1=Hy,\quad f_1=H^Tc_1/n,\quad
c_2=-Hf_1/2,\quad f_2=H^Tc_2/n.
\tag{4}
\]

Let \(U_j\) be the coefficient of \(t^j\) in \(c[:,None](1-H(t)^2)\), and \(R_j\) the corresponding coefficient after multiplication by \(r\). Initially,

\[
U_1=c_1[:,None]D,\quad U_2=c_2[:,None]D,\quad
R_1=U_1y,\quad R_2=U_2y-U_1f_1.
\tag{5}
\]

Then

\[
\begin{aligned}
2A_2&=R_1h^T/n,&3A_3&=R_2h^T/n,\\
2w_2&=P\odot(A^TU_1)\odot y,&
3w_3&=P\odot[(A^TU_2)\odot y-(A^TU_1)\odot f_1],\\
h_2&=P\odot w_2,&h_3&=P\odot w_3,\\
Z_2&=Ah_2+A_2h,&Z_3&=Ah_3+A_3h,\\
H_2&=D\odot Z_2,&H_3&=D\odot Z_3,\\
D_2&=D'\odot Z_2,&D_3&=D'\odot Z_3.
\end{aligned}
\tag{6}
\]

The symbols \(Z_2,Z_3\) in this note mean the middle preactivation coefficients \(Z_{2,2},Z_{2,3}\) in layer-index notation. The time-dependent upper gate is \(D+D_2t^2+D_3t^3+\cdots\).

Next compute

\[
\begin{aligned}
c_3&=(H_2y-Hf_2)/3,&
f_3&=(H^Tc_3+H_2^Tc_1)/n,\\
c_4&=(H_3y-H_2f_1-Hf_3)/4,&
f_4&=(H^Tc_4+H_2^Tc_2+H_3^Tc_1)/n,\\
U_3&=c_3[:,None]D+c_1[:,None]D_2,\\
U_4&=c_4[:,None]D+c_2[:,None]D_2+c_1[:,None]D_3,\\
R_3&=U_3y-U_2f_1-U_1f_2,\\
R_4&=U_4y-U_3f_1-U_2f_2-U_1f_3,\\
4A_4&=(R_3h^T+R_1h_2^T)/n.
\end{aligned}
\tag{7}
\]

Put \(V_1=A^TU_1\), \(V_2=A^TU_2\), and \(V_3=A^TU_3+A_2^TU_1\). The only further first-layer calculation needed is

\[
\begin{aligned}
4w_4&=P\odot(V_3y-V_2f_1-V_1f_2)
       +P'\odot w_2\odot V_1\odot y,\\
h_4&=P\odot w_4+\tfrac12P'\odot w_2^2,\\
Z_4&=Ah_4+A_2h_2+A_4h,\\
H_4&=D\odot Z_4+\tfrac12D'\odot Z_2^2,\\
D_4&=D'\odot Z_4+\tfrac12D''\odot Z_2^2.
\end{aligned}
\tag{8}
\]

Finally,

\[
\begin{aligned}
c_5&=(H_4y-H_3f_1-H_2f_2-Hf_4)/5,\\
U_5&=c_5[:,None]D+c_3[:,None]D_2
                 +c_2[:,None]D_3+c_1[:,None]D_4,\\
R_5&=U_5y-U_4f_1-U_3f_2-U_2f_3-U_1f_4,\\
5A_5&=(R_4h^T+R_2h_2^T+R_1h_3^T)/n,\\
6A_6&=(R_5h^T+R_3h_2^T+R_2h_3^T+R_1h_4^T)/n.
\end{aligned}
\tag{9}
\]

Equations (4)–(9) follow by multiplying the Taylor series in (1), equating coefficients, and applying the second-order Taylor formula for each activation in (8). Each coefficient of velocity at power \(j\) is divided by \(j+1\) to obtain the next position coefficient. There are no omitted contributions from order-one hidden coefficients because those coefficients vanish.

## 3. The normalized-axis structural relations

For a general empirical upper Gram \(C=H^TH/n\),

\[
f_1=Cy,\qquad c_2=-HCy/2.
\]

Under (3), these become

\[
f_1=\tau y,\quad c_2=-\tau c_1/2,\quad
f_2=-\tau^2y/2,\quad U_2=-\tau U_1/2,
\quad R_2=-3\tau R_1/2.
\]

Substitution in (6) gives the exact identities

\[
A_3=-\tau A_2,\quad w_3=-\tau w_2,\quad
h_3=-\tau h_2,\quad Z_3=-\tau Z_2,\quad
H_3=-\tau H_2,\quad D_3=-\tau D_2.
\tag{10}
\]

Thus all three requested relations hold, including the readout factor \(1/2\). The upper Gram identity and the normalized axes suffice for (10); the lower Gram identity is not needed for this step.

## 4. Collecting label polynomials at powers five and six

For vectors \(c\in\mathbb R^n\) and \(r\in\mathbb R^2\), define the bilinear operators

\[
\begin{aligned}
L_0(c,r)&=\big((c[:,None]D)\odot r\big)h^T/n,\\
L_2(c,r)&=\left[\big((c[:,None]D_2)\odot r\big)h^T
                 +\big((c[:,None]D)\odot r\big)h_2^T\right]/n,\\
L_4(c,r)&=\left[\big((c[:,None]D_4)\odot r\big)h^T
                 +\big((c[:,None]D_2)\odot r\big)h_2^T
                 +\big((c[:,None]D)\odot r\big)h_4^T\right]/n.
\end{aligned}
\tag{11}
\]

Their hidden arguments depend polynomially on \(y\); their displayed arguments \(c,r\) are external slots. Equation (10) gives \(L_3=-\tau L_2\). Define the homogeneous cubic input vector

\[
b=\frac1n\left(\frac13H^TH_2y+H_2^THy\right),
\quad U=L_0(Hb,y),\quad V=L_0(Hy,b).
\tag{12}
\]

The relevant readout and output coefficients collect to

\[
\begin{aligned}
c_3&=\tau^2c_1/6+H_2y/3,\\
c_4&=-\tau^3c_1/24-Hb/4-\tau H_2y/2,\\
c_5&=\tau^4c_1/120+(7\tau/20)Hb
                       +(3\tau^2/10)H_2y+H_4y/5,\\
f_3&=\tau^3y/6+b,\qquad
f_4=-\tau^4y/24-7\tau b/4.
\end{aligned}
\tag{13}
\]

For example, the formula for \(f_4\) follows by inserting \(c_4,c_2,H_3\) into (7): the cubic terms are
\(-\tau H^TH_2y/(2n)-3\tau H_2^THy/(2n)-\tau b/4=-7\tau b/4\).

Collecting (7) and (9) now gives

\[
A_4=\frac{7\tau^2}{12}A_2
     +\frac1{12}L_0(H_2y,y)+\frac14L_2(c_1,y),
\]
\[
A_5=-2\tau A_4+\frac{11\tau^3}{12}A_2
                       -\frac1{20}U-\frac15V.
\tag{14}
\]

Both \(U,V\) consist of scalar label-polynomial weights on the initial channels

\[
(H_{:,s}\odot D_{:,a})h_{:,a}^T,
\qquad s,a\in\{1,2\}.
\tag{15}
\]

These channels require no new left or right factor functions. More precisely, the two diagonal quadratic coefficients of \(A_2\) expose each right factor \(h_{:,a}\). Their left factors are nonzero because \(\tau>0\) and \(D>0\). The mixed coefficient is a sum of the two cross channels. Since \(h_{:,1},h_{:,2}\) are independent by \(v>0\), multiplying that coefficient by their dual vectors isolates both cross-channel left factors. Thus all left and right factor spaces used by (15) are already present after collecting the three quadratic coefficients of \(A_2\). Equation (14) proves the stated absence of new factor functions at position power five.

For order six put

\[
\kappa=7\tau^2/12,\quad Q=A_4-\kappa A_2,
\quad J=H_4-\kappa H_2,\quad M=L_4-\kappa L_2.
\tag{16}
\]

The coefficient recurrence shows that the quadratic parts of \(w_4,h_4,Z_4,H_4,D_4\) are \(\kappa\) times their order-two counterparts. Consequently \(Q,J\), and the hidden coefficient operator \(M\), have label degree four. The exact collection by total label degree is

\[
\begin{aligned}
A_6^{[2]}&=\frac{31\tau^4}{360}A_2,\\
A_6^{[4]}&=\frac{13\tau^2}{6}Q+\frac\tau{10}U+\frac{3\tau}{8}V,\\
A_6^{[6]}&=\frac1{30}L_0(Jy,y)
            +\frac1{18}L_2(H_2y,y)+\frac16M(c_1,y).
\end{aligned}
\tag{17}
\]

One scalar-coefficient check before this final collection is

\[
\begin{aligned}
6A_6={}&\frac{31\tau^4}{120}L_0(c_1,y)
 +\frac{3\tau}{5}U+\frac{9\tau}{4}V
 +\frac{29\tau^2}{30}L_0(H_2y,y)+\frac15L_0(H_4y,y)\\
&+\frac{8\tau^2}{3}L_2(c_1,y)
 +\frac13L_2(H_2y,y)+L_4(c_1,y).
\end{aligned}
\]

Substitution of (16) and \(2A_2=L_0(c_1,y)\) produces (17). In particular, \(A_2,A_3\) have only label degree two; \(A_4,A_5\) have degrees two and four; and \(A_6\) has degrees two, four, and six. The \(D_4,h_4\) terms in \(M\) show where further factors can enter.

## 5. Actual sixth-order factor novelty under the same Gram assumptions

The following finite algebraic example establishes that Gram identities alone do not extend the fifth-order factor closure to sixth order. It is not a claim about a particular iid initialization law.

Take \(n=8\), \(x=(1/5,2/5,3/5,4/5)^T\),

\[
h_{:,1}=(x,0)^T,\quad h_{:,2}=(0,x)^T,
\quad w_0=\operatorname{arctanh}(h),\quad A_0=\lambda I_8.
\]

For any nonzero real \(\lambda\), both Grams in (3) are scalar identities, with
\(v=3/20\) and \(\tau=\sum_i\tanh(\lambda x_i)^2/8>0\).
On one four-node block write

\[
P=1-x^2,\quad H=\tanh(\lambda x),\quad D=1-H^2,
\quad B=HD,\quad \beta=\sum_i B_i^2/8,
\]
\[
u=\frac\lambda2BP^2,\qquad
E=\frac12HD^2(\lambda^2P^2+v),
\]
\[
k=\frac\lambda{12}P^2E(1-7H^2)
     +\frac\beta8xP^2-\frac{\lambda^2}{2}xB^2P^3.
\tag{18}
\]

For labels \((s,0)\), these are the coefficients
\(h_2=s^2u\), \(H_2=s^2E\), and \(h_4^{[4]}=s^4k\) on the active block. They follow directly from (6)–(8). With both labels allowed, the cross-probe order-two lower feature on this block is \((\lambda H/2)y_1y_2\). Therefore every right factor of the full two-label coefficient collection through \(A_4\), and through \(A_5\) by (14), belongs blockwise to

\[
\operatorname{span}\{x,H,u\}.
\tag{19}
\]

Nevertheless,

\[
\det[x,H,u,k]=\frac{1008}{244140625}\lambda^9+O(\lambda^{11}).
\tag{20}
\]

Here is an explicit rational check of its leading coefficient. Write \(m_4=\sum_i x_i^4/8\). The expansions needed are

\[
H=\lambda x-\lambda^3x^3/3+O(\lambda^5),\qquad
u=\lambda^2xP^2/2-2\lambda^4x^3P^2/3+O(\lambda^6),
\]
\[
k-(v/3)u
=\lambda^4\left(xP^4/24-vx^3P^2/6-m_4xP^2/3-x^3P^3/2\right)
 +O(\lambda^6).
\]

Subtract \(\lambda x\) from the second determinant column and \((v/3)u\) from the fourth. The coefficient of \(\lambda^9\) is precisely the determinant of the four displayed leading rational vectors, which evaluates to the positive rational in (20). The checker verifies this evaluation using exact fractions. Analyticity near \(\lambda=0\) and the nonzero leading coefficient prove that \(k\) lies outside (19) for sufficiently small nonzero \(\lambda\).

The \(y_1^6\) coefficient of \(A_6\) contains \(Bk^T/(6n)\). Every other right factor in that coefficient lies in \(\operatorname{span}\{x,u\}\): they arise from the first two terms of \(A_6^{[6]}\) in (17), or from the \(D_4h^T,D_2h_2^T\) parts of \(M\). Since \(B\ne0\), projection onto the orthogonal complement of (19) leaves a nonzero matrix. Thus the full two-label factor collection can require a new right factor at sixth order.

## 6. Verification record and limits

`p45_jet_check.py` uses the complete supplied `jet_check.py` as the independent series oracle, with physical inputs \(\sqrt2I_2\) and weights \((1/2,1/2)\). The compact recurrence is implemented separately, retaining the exact empirical upper Gram and all finite matrix products. Its checks cover:

- Four arbitrary finite fixtures, including a zero-label fixture, through \(A_6\) and middle velocity power five.
- Six label choices on a finite fixture satisfying both ideal Grams, verifying (10), (14), and (17) separately from the arbitrary-Gram checks.
- Held-out bivariate label-polynomial interpolation checks for the asserted degrees through \(A_6\).
- The exact rational coefficient in (20), the explicit hidden coefficient (18), and finite matrix projection checks of sixth-order factor novelty.

The final record is `data/generated/gradient_flow_probe_dictionary_20260921/p45_jet_check01/result_final.json`. It reports PASS. The largest compact-recurrence versus full-oracle error is \(1.11\times10^{-16}\); the largest ideal-Gram identity error is \(1.39\times10^{-16}\), against tolerance \(3\times10^{-12}\). The sixth-order matrix component outside the older right-factor space has norm approximately \(7.07\times10^{-5}\) in the \(\lambda=1\) algebra fixture. The symbolic determinant, rather than that numerical residual, establishes existence of novelty.

These computations verify finite algebra and the stated conditional Gram identities. They do not establish convergence of finite random coefficients to population coefficients, interchange differentiation with a width limit, or prove that a particular population initialization has no additional identities.
