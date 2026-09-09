# Isolated adversarial audit: actual-query time regularity

Date: 2026-09-06.

Audited file: /tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_ACTUAL_QUERY_TIME_REGULARITY.md

Verified SHA-256:
e3fd00736b3094a16395b524d4e6ed7a0376b5c4e0c4d2e2b5bdccc5e8d71112

Line references below refer to that exact version.

## Verdict and scope

**CONDITIONAL PASS. No required mathematical correction was found in the new claims, with the bounded-state obstruction interpreted as the document explicitly limits it in Section 5.**

The query equations, uniform constants, constant-one selected-mode spatial L1 action estimate, cutoff increment inequalities, and both divergent query derivatives check out. In particular, recalculation of the complete lower motion gives the stated coefficient
\[
K_*=\frac{e^2}{256}(-T+35v^2)<0.
\]
The lower matrix and first-layer motion add a strictly positive quantity to \(T\), strengthening the negative leading contribution. The other terms in the first-query equation cannot cancel it.

This is a sidecar audit, not whole-goal certification. Its mathematical project input was **only** the audited file. Neither of its two cited inputs, any other mathematical project file, nor any old review or history was read. The procedural skill /etc/codex/skills/solve-math-rigorously/SKILL.md was read as guidance. No experimental checks, numerical experiments, subagents, or candidate edits were used.

As requested, the global bounded-reference/common-space, primal and operator bounds, action identity, symmetry, first raw metric, and prescribed initialization premises are accepted conditionally. Their construction, consistency with their original sources, and validity for a canonical limit are not certified. Identification of the displayed modal quantities with every named action density in the unread inputs also remains conditional; the actual fields and weighted quantities used here are checked explicitly below.

The witness establishes failure of a uniform instantaneous L2 derivative bound on the stated class of symmetric bounded states with the exact gradient vector field. It does **not** establish reachability from the prescribed zero-readout initialization, failure of uniform time regularity of the prescribed reference sequence, or failure of a history-dependent time-integrated estimate.

## 1. Evolution formulas and memories: pass

All calculations here use real Hilbert spaces on the separate populations. For a rank-one map,
\[
(u\otimes v)^*=v\otimes u,\qquad
(u\otimes v)h=u\langle v,h\rangle.
\]
Thus the exact updates in (1) give
\[
A'^*\delta^3_a
=\sum_b\lambda_b H^2_b\langle\delta^3_b,\delta^3_a\rangle
=R^2_a,
\]
and likewise \(B'^*\delta^2_a=R^1_a\). Both sample weights are retained.

Differentiating \(Z^2_a=BH^1_a\), \(Z^3_a=AH^2_a\), and \(H^\ell_a=\phi(Z^\ell_a)\) gives
\[
v^2_a=B'H^1_a+B(p^1_av^1_a),\qquad
v^3_a=A'H^2_a+A(p^2_av^2_a),
\]
which are exactly (2). Differentiating the backward definitions gives
\[
\begin{aligned}
(\delta^3_a)'&=p^3_aF+c^3_aw v^3_a,\\
(q^2_a)'&=A'^*\delta^3_a+A^*(\delta^3_a)',\\
(\delta^2_a)'&=p^2_a(q^2_a)'+c^2_aq^2_av^2_a,\\
(q^1_a)'&=B'^*\delta^2_a+B^*(\delta^2_a)'.
\end{aligned}
\]
This verifies (3)–(5), including every adjoint, gate, sign, and curvature term. Substitution in the last equation produces
\[
(q^1_a)'=F^1_a+B^*\bigl(p^2_a A^*P^3_a+P^2_a\bigr).
\]
There is no extra matrix derivative missing from this expression: those derivatives are already \(R^1_a,R^2_a\). Nor can either be omitted.

The integrated matrix identities (6) are exact. Applying them to a field at the current endpoint \(s\) gives (7); the second factor in each covariance also depends on \(s\). For example, differentiating the reverse memory produces
\[
R^{\ell-1}_a(s)
+W^\ell(0)^*(\delta^\ell_a)'(s)
+\int_0^s\sum_b\lambda_b H^{\ell-1}_b(u)
 \langle\delta^\ell_b(u),(\delta^\ell_a)'(s)\rangle\,du.
\]
The last two terms equal \(W^\ell(s)^*(\delta^\ell_a)'(s)\). Hence the memory representation preserves the curvature terms rather than eliminating them. These differentiations are justified at each bounded classical reference under the accepted premise; no uniform L2 Fréchet chain rule is used.

The equations are closed with the full reference state, as the document says at lines 123–126. They are not autonomous in the two queries alone.

## 2. Uniform constants and spatial L1 bounds: pass

For softplus,
\[
p(z)=\frac{e\exp(z)}{1+\exp(z)},\qquad
c(z)=\frac{e\exp(z)}{(1+\exp(z))^2}
=p(z)-\frac{p(z)^2}{e},
\]
so \(0<p<e\), \(0<c\le e/4\), and \(c\le p\). The constants used in the note are correct.

The first-coordinate evaluation has norm \(\sqrt{C_{aa}}=1\) in the stated raw metric. With the stipulated one-field interpretation at the degenerate endpoint, this gives
\[
\|v^1_a\|_2\le a.
\]
Using the Hilbert–Schmidt tangent norm to control the operator norm,
\[
\begin{aligned}
\|v^2_a\|_2
&\le \|B'\|_{\rm HS}\|H^1_a\|_2
 +\|B\|_{\rm op}e\|v^1_a\|_2
\le M(1+e)a,\\
\|v^3_a\|_2
&\le \|A'\|_{\rm HS}\|H^2_a\|_2
 +\|A\|_{\rm op}e\|v^2_a\|_2
\le (M+MeL_2)a.
\end{aligned}
\]
Thus (8) has the stated \(L_2,L_3\), without any hidden kernel supremum.

Since \(\sum_b|\lambda_b|=1\), the matrix gradients have norms at most \(M^2\), and the readout gradient has norm at most \(M\). For the first block, \(d_b=\lambda_b\delta^1_b\) and \(\|C\|_{\rm op}\le2\) give
\[
\|Z^{1\,\prime}\|_{\rm raw}^2
=\mathbb E[d^\top C d]
\le2\sum_b\lambda_b^2\|\delta^1_b\|_2^2
\le M^2.
\]
At \(\rho=-1\), the one-field gradient is a signed sum of the two weighted backward fields and also has norm at most \(M\). Consequently
\[
a^2\le 2M^4+2M^2\le4M^4,
\]
so \(K=2M^2\) is valid. The argument does not require a bound on \(C^{-1}\) as \(\rho\) approaches the stipulated endpoint.

For \(I=[s,t]\),
\[
\int_I a\le\sqrt{(t-s)\int_Ia^2}=D_I,\qquad
D_I\le K(t-s).
\]
Integration of the raw velocity and of (8) proves the stated increment bounds. Under the action premise one also has \(E_I=g(t)-g(s)\le1\); the note does not confuse this global action control with uniform smallness of arbitrary spatial tails.

The noncurvature constants in (9) follow from
\[
\|R^2_a\|_2,\|R^1_a\|_2\le Ma,\qquad
\|F\|_2\le a.
\]
Explicitly,
\[
\|F^2_a\|_2\le M(1+e)a,\qquad
\|F^1_a\|_2\le\bigl[M+M^2e(1+e)\bigr]a.
\]

Spatial Cauchy–Schwarz gives
\[
\begin{aligned}
\|P^3_a\|_1&\le(e/4)\|w\|_2\|v^3_a\|_2
\le(eM/4)L_3a,\\
\|P^2_a\|_1&\le(e/4)\|q^2_a\|_2\|v^2_a\|_2
\le(eM/4)L_2a.
\end{aligned}
\]
Time integration proves (10). The probability-space normalization also gives \(\|F\|_1\le\|F\|_2\), and therefore
\[
\|\delta^3_a(t)-\delta^3_a(s)\|_1
\le[e+(eM/4)L_3]D_I.
\]
Together with \(D_I\le K(t-s)\), this proves the claimed uniform spatial L1 Lipschitz bound. It does not bound \(A^*P^3_a\) in L2, since no uniform \(L^1\to L^2\) adjoint bound has been assumed.

## 3. Constant-one selected-mode action estimate: pass

This estimate does not require independence of any fields.

At a fixed third-layer point, the readout \(w\) is common to the two samples. The identity
\[
c_1-c_2
=\left(1-\frac{p_1+p_2}{e}\right)(p_1-p_2)
\]
has a multiplier of absolute value at most one. Hence
\[
|m_-|\le|\delta_-|.
\]
Also \(c_1+c_2\le p_1+p_2\), and the common factor \(w\) has the same sign in both summands, so
\[
|m_+|\le|\delta_+|.
\]
This verifies both inequalities in (12), including for a signed readout.

Symmetry implies equal feature norms and thus
\[
\langle U,V\rangle
=\frac{\|H^2_1\|_2^2-\|H^2_2\|_2^2}{4}=0.
\]
For opposite labels, direct expansion of the two-sample update yields
\[
A'=\delta_-\otimes U+\delta_+\otimes V,\qquad
A'H^2_a=u^2\delta_-+\epsilon_a\kappa\delta_+.
\]
Taking the difference mode after multiplying by \(m_a\) gives
\[
P^{3,\mathrm{mat}}_-
=u^2m_-\delta_-+\kappa m_+\delta_+.
\]
Therefore
\[
\|P^{3,\mathrm{mat}}_-\|_1
\le u^2\|\delta_-\|_2^2+\kappa\|\delta_+\|_2^2
=\|A'\|_{\rm HS}^2.
\]
The last equality follows because the cross term in the squared Hilbert–Schmidt norm is
\[
2\langle\delta_-,\delta_+\rangle\langle U,V\rangle=0.
\]
It does not require the two output modes to be orthogonal.

For equal labels the full update is
\[
A'=\delta_+\otimes U+\delta_-\otimes V,
\]
and the same expansion gives
\[
P^{3,\mathrm{mat}}_+
=u^2m_+\delta_++\kappa m_-\delta_-,
\]
with the same constant-one estimate. There is no missing factor of two from the modal convention, no division by \(\kappa\), and no need to exclude \(\kappa=0\).

Since \(\|A'\|_{\rm HS}^2\) is one summand of the raw action density,
\[
\int_I\|P^{3,\mathrm{mat}}_{\mathrm{selected}}\|_1
\le\int_I\|A'\|_{\rm HS}^2\le E_I.
\]
This establishes exactly (13)–(15). It does not assert optimality of the numerical constant one, nor an estimate for the full source or full derivative.

The unselected mode remains in the update. For the lower-motion part, taking the difference mode of \(m_aA(H^{2\,\prime}_a)\) gives exactly
\[
m_-A(H^{2\,\prime}_+)+m_+A(H^{2\,\prime}_-),
\]
as in (16). Neither the action bound nor the mode algebra supplies the missing L2 multiplication estimate for this expression.

## 4. Increment and tail quantifiers: pass

The precise valid quantifiers are: one common choice of \(M,K,L_2,L_3\), every sufficiently large reference index \(N\), every sample, every \(0\le s\le t\le s_N\), and every finite \(R_2,R_3\ge0\).

For the top backward field, the exact increment decomposition is
\[
\delta^3_a(t)-\delta^3_a(s)
=p^3_a(t)(w(t)-w(s))
 +(p^3_a(t)-p^3_a(s))w(s).
\]
On \(\{|w(s)|\le R_3\}\), use the Lipschitz constant \(e/4\) of \(p\); on its complement use the amplitude bound \(|p(z)-p(z')|\le e\). Thus
\[
\|\Delta\delta^3_a\|_2
\le[e+(e/4)R_3L_3]D_I+eT_w(s,R_3).
\]
In particular, the tail coefficient is \(e\), not \(e/4\).

Using
\[
\Delta q^2_a=(A(t)-A(s))^*\delta^3_a(t)
 +A(s)^*\Delta\delta^3_a
\]
proves (17), including the additional \(MD_I\) from the matrix increment:
\[
\|\Delta q^2_a\|_2
\le M[1+e+(e/4)R_3L_3]D_I+MeT_w(s,R_3).
\]
Similarly,
\[
\Delta\delta^2_a=p^2_a(t)\Delta q^2_a
 +(p^2_a(t)-p^2_a(s))q^2_a(s),
\]
and the increment of \(B\) gives exactly
\[
\|\Delta q^1_a\|_2
\le MD_I+Me\|\Delta q^2_a\|_2
 +(Me/4)R_2L_2D_I+MeT_{q^2_a}(s,R_2).
\]
Thus (18) cuts off the correct actual field at the correct endpoint. These are analytic splits of a fixed increment, not modified equations of motion. Swapping endpoints is legitimate using \(|t-s|\) and tails based at the other endpoint. Zero cutoffs and zero-length intervals cause no problem.

At a fixed reference, boundedness over its compact feature interval supplies finite, reference-dependent cutoffs that remove both tails. This gives classical L2 Lipschitz regularity for that reference.

Uniform equicontinuity would follow, for example, from the additional conditions
\[
\lim_{R\to\infty}\sup_{N,s\le s_N}T_w(s,R)=0,\qquad
\lim_{R\to\infty}\sup_{N,s\le s_N,a}T_{q^2_a}(s,R)=0.
\]
Then one first chooses cutoffs to control the tails and only afterward chooses the interval length to control the \(D_I\) terms. The document does not assert these conditions or exchange these choices illegitimately. Uniform L2 boundedness alone supplies neither condition. These are sufficient conditions for this argument, not a claim of necessity for equicontinuity.

For the initial endpoint, \(w(0)=0\) and the action premise give
\[
\|w(s)\|_2\le\int_0^s a
\le\min\{Ks,\sqrt{s\,g(s)}\}.
\]
Consequently
\[
\|q^2_a(s)\|_2\le eM\min\{Ks,\sqrt{s\,g(s)}\},\qquad
\|q^1_a(s)\|_2\le e^2M^2\min\{Ks,\sqrt{s\,g(s)}\}.
\]
The constants in (19) are correct. This controls increments from the initial endpoint only.

Given the stated physical clock \(ds/dt=4(1-g)\), the chain-rule conversion and pullback of variation bounds at lines 573–580 are correct; in particular \(\Delta s\le4\Delta t\). The clock law's derivation from the original physical loss is outside this isolated audit. Multiplication by this clock factor supplies no spatial product estimate.

## 5. Witness: spaces, symmetry, forward state, and margin

The probability-space construction can be realized on fixed spaces throughout the limit. Take the first two populations to be separate copies of the four equiprobable sign pairs \((x,h)\). For the third, one may take \([0,1]\times\{-1,1\}\) with product measure, involution flipping the second coordinate, and
\[
E_\pm=[0,m]\times\{\pm1\}.
\]
This confirms that varying \(m\) need not change the underlying Hilbert spaces.

The functions \(b,o\) have norm one, are orthogonal, and satisfy \(Jb=b,Jo=-o\). The first two populations have orthonormal basis \(1,x,h,xh\). The operator \(B\) maps \(x_1\) to \(x_2\), \(h_1\) to \(h_2\), and annihilates the other two directions, so \(\|B\|_{\rm op}=1\).

The identities
\[
\phi(z)-\phi(-z)=ez,\qquad p(z)+p(-z)=e
\]
verify every formula in (21), including
\[
V_1=t_2=p_0=e/2,\qquad v=e^2/4.
\]

For \(r=\sqrt m\), the third operator acts by
\[
Ah=b,\qquad A1=ra_0b,\qquad Ax=-ra_1o,\qquad A(xh)=0.
\]
Its even and odd blocks have orthogonal images, giving exactly
\[
\|A\|_{\rm op}=\max\{\sqrt{1+ma_0^2},ra_1\}.
\]
This is at most two for sufficiently small \(m\). Also
\[
\|A\|_{\rm HS}^2=1+m(a_0^2+a_1^2),\qquad
\|B\|_{\rm HS}^2=2,
\]
so the obstruction does not rely on a diverging current Hilbert–Schmidt state norm either.

Application to \(H^2_a=u+\epsilon_avx\) gives
\[
Z^3_a=(L/2)1_E-\epsilon_a(L/2)\operatorname{sign}_E1_E,
\]
which verifies (23). Both operators intertwine the involutions, the forward samples exchange under the involutions, and \(w=-o\) is odd. Thus the required sample symmetry is exact.

Write
\[
f=\frac{\phi(L)-\phi(0)}2=\frac{e\log2}{2}>0.
\]
Then
\[
F=H^3_-=-fr\,o,\qquad g=\langle-o,-fr\,o\rangle=fr.
\]
This verifies the sign and factor in (24). For small \(m\), \(0<g<1\). The first raw norm is \(\sqrt2\), all forward fields are bounded pointwise independently of \(m\), and the readout has norm one.

The top gate constants recalculate to
\[
p(0)=e/2,\quad p(L)=3e/4,\quad
c(0)=e/4,\quad c(L)=3e/16.
\]
Therefore
\[
d=-e/8,\quad \bar p=5e/8,\quad
c_-=e/32,\quad c_+=7e/32,
\]
with the signs used in the note.

## 6. Exact lower-motion calculation

Here and below \(x,h\) denote the basis on the layer where the expression lives. The tensor formulas specify the population mapping. No identification of random variables on different populations is used.

The following extra scalar notation makes every remainder in the witness explicit:
\[
\begin{aligned}
\alpha&=a_1\bar p,&\beta&=a_0d,\\
k&=p_0\alpha-d_2\beta,&
\ell&=d_2\alpha-p_0\beta,\\
D&=V_1^2+(p_0^2+d_1^2)/2,&
\gamma_0&=U_1^2\ell,\qquad \gamma_1=kD,\\
\eta_0&=p_0\gamma_0+d_2\gamma_1,&
\eta_1&=p_0\gamma_1+d_2\gamma_0.
\end{aligned}
\]
All are finite constants independent of \(m\). Since \(\alpha>0,\beta<0\) and \(d_1,d_2>0\), \(k,\ell,\gamma_0,\gamma_1,\eta_0,\eta_1\) are positive.

The top backward fields are exactly
\[
\delta^3_a=-\bar p\,o-\epsilon_a d\,b.
\]
Applying \(A^*\), multiplying by the middle gate, and applying \(B^*\) gives
\[
\begin{aligned}
q^2_a&=-\epsilon_a d\,h+r(\alpha x-\epsilon_a\beta),\\
\delta^2_a&=-\epsilon_a dp_0h-dd_2xh
 +r(kx+\epsilon_a\ell),\\
q^1_a&=-\epsilon_a dp_0h+rkx.
\end{aligned}
\]
Thus the unspecified scalar \(b_a\) in (26) can in fact be chosen as the same constant \(k\) for both samples.

Because \(C=I\) and the labels are opposite,
\[
v^1_a=\frac{\epsilon_a}{2}p^1_aq^1_a
=-\frac{dp_0^2}{2}h
-\frac{\epsilon_a dp_0d_1}{2}xh
+\frac{rk}{2}(\epsilon_ap_0x+d_1).
\]
Multiplication by \(p^1_a\) and projection through \(B\) give the full contribution
\[
B(p^1_av^1_a)
=-\frac{dp_0}{2}(p_0^2+d_1^2)h
+\frac{r\epsilon_ak}{2}(p_0^2+d_1^2)x.
\]
In particular, its h coefficient is exactly the one at line 431.

The complete lower matrix update is
\[
B'
=U_1(-dp_0h+r\ell)\otimes1
+V_1(-dd_2xh+rkx)\otimes x.
\]
It follows that
\[
B'H^1_a
=-d[p_0U_1^2+\epsilon_ad_2V_1^2x]h
+r[U_1^2\ell+\epsilon_akV_1^2x].
\]
Adding both contributions gives the exact formula
\[
v^2_a=-d(A_0+\epsilon_aA_1x)h
+r(\gamma_0+\epsilon_a\gamma_1x),
\]
where \(A_0,A_1\) are precisely those in the document:
\[
A_0=p_0[U_1^2+(p_0^2+d_1^2)/2],\qquad
A_1=d_2V_1^2.
\]

Put \(B_1=p_0A_1+d_2A_0\), with \(B_0=p_0A_0+d_2A_1\) as in the note. Then
\[
p^2_av^2_a
=-d(B_0+\epsilon_aB_1x)h
+r(\eta_0+\epsilon_a\eta_1x).
\]
Using all four basis actions of \(A\) gives
\[
A(p^2_av^2_a)
=-dB_0b+m(a_0\eta_0b-\epsilon_aa_1\eta_1o).
\]
This proves (27) with explicit coefficients for both \(O(m)\) terms. The \(xh\) input is annihilated by \(A\), and the remaining \(1,x\) input acquires its second factor of \(r\); there is no missing order-one component.

The exact upper update is
\[
A'=-du\,b\otimes1-\bar p v\,o\otimes x,
\]
so
\[
A'H^2_a=-du^2b-\epsilon_a\bar p v^2o.
\]
Consequently, defining
\[
T=u^2+B_0,\qquad
X(m)=-dT+ma_0\eta_0,\qquad
Y(m)=\bar p v^2+ma_1\eta_1,
\]
the full top velocity is exactly
\[
v^3_a=X(m)b-\epsilon_aY(m)o.
\]
This proves (28), including both matrix updates and every first- and second-layer motion term.

Moreover,
\[
B_0=p_0^2[U_1^2+(p_0^2+d_1^2)/2]+d_2^2V_1^2>0.
\]
Both updates are nonzero: \(B'\) has the nonzero constant-to-h rank term displayed above, and \(A'\) has the nonzero constant-to-b term. The additional terms cannot cancel them because their input or output basis directions are orthogonal.

## 7. Exact source and both query derivatives

On \(E\),
\[
b^2=o^2=b/r,\qquad bo=o/r,\qquad
c^3_a=c_++\epsilon_ac_-\operatorname{sign}_E.
\]
Since \(w=-o\), direct multiplication gives
\[
P^3_a=\frac{\epsilon_aK(m)b+N(m)o}{r},
\]
where
\[
\begin{aligned}
K(m)&=c_+Y(m)-c_-X(m)
=K_*+m(c_+a_1\eta_1-c_-a_0\eta_0),\\
N(m)&=c_-Y(m)-c_+X(m),\\
K_*&=c_-dT+c_+\bar p v^2
=\frac{e^2}{256}(-T+35v^2).
\end{aligned}
\]
Thus
\[
\langle b,P^3_a\rangle
=\frac{\epsilon_aK_*}{r}+O(r),
\]
exactly as in (29).

For \(e=1/10\), \(v=1/400\) and
\[
35v^2=\frac7{32000}<1,\qquad T\ge u^2>1.
\]
In particular,
\[
K_*\le-\frac{1-7/32000}{25600}
=-\frac{31993}{819200000}<0.
\]
The contribution of the full lower motion to \(K_*\) is \(c_-dB_0<0\). This confirms its sign and rules out the proposed leading-order cancellation.

For additional verification of every other top-query term, define scalars
\[
H_m=\frac{K(m)}r-frd,\qquad
O_m=\frac{N(m)}r-fr\bar p.
\]
The readout term is exactly
\[
p^3_aF=-fr(\bar p\,o+\epsilon_ad\,b),
\]
so
\[
(\delta^3_a)'=\epsilon_aH_m b+O_m o.
\]
The readout term's contribution to the b pairing is order \(r\), as claimed.

The other top-query contribution is
\[
R^2_a=\epsilon_a d^2u+\bar p^2v x.
\]
Set
\[
E_m=d^2u+ra_0H_m,\qquad
X_m=\bar p^2v-ra_1O_m.
\]
Application of \(A^*\) now gives the **complete** second-query derivative
\[
(q^2_a)'=\epsilon_aH_m h+\epsilon_aE_m+X_mx.
\]
Both \(E_m\) and \(X_m\) are uniformly bounded: the possible \(1/r\) coefficients have acquired a factor \(r\). Meanwhile
\[
H_m=K_*/r+O(r).
\]
Hence (30) is exact at the claimed order.

For the first-query equation, the full matrix term is
\[
R^1_a
=\epsilon_aU_1(d^2p_0^2+m\ell^2)
+V_1(d^2d_2^2+mk^2)x.
\]
It has zero h pairing. Since \(p^2_a\) depends only on \(x\),
\[
\langle h,p^2_a(q^2_a)'\rangle=\epsilon_ap_0H_m.
\]
Here no correlation term has been discarded: the other terms are functions of \(x\), and the \(xh\) part has zero h projection.

Write \(c_2=c(t_2)\); it is constant on both samples because \(c\) is even. Multiplying the exact formulas for \(q^2_a\) and \(v^2_a\) gives
\[
\begin{aligned}
\langle h,P^2_a\rangle
&=-\epsilon_a r c_2d(\gamma_0+\alpha A_1-\beta A_0),\\
\langle x,P^2_a\rangle
&=c_2[d^2A_1+m(\alpha\gamma_0-\beta\gamma_1)].
\end{aligned}
\]
The leading product of the two h-dependent factors has \(h^2=1\) and therefore zero h projection; the two cross products are exactly order \(r\).

For completeness, \(B^*\) projects onto \(x,h\), so the **complete** first-query derivative is
\[
\begin{aligned}
(q^1_a)'={}&
\epsilon_aU_1(d^2p_0^2+m\ell^2)\\
&+\bigl[
V_1(d^2d_2^2+mk^2)+p_0X_m+d_2E_m
+c_2\{d^2A_1+m(\alpha\gamma_0-\beta\gamma_1)\}
\bigr]x\\
&+\epsilon_a\bigl[
p_0H_m-r c_2d(\gamma_0+\alpha A_1-\beta A_0)
\bigr]h.
\end{aligned}
\]
All coefficients except the h coefficient are bounded. Therefore
\[
\langle h,(q^1_a)'\rangle
=\frac{\epsilon_ap_0K_*}{r}+O(r),
\]
which verifies (31) without leaving any lower motion or matrix term implicit.

Since the test directions have norm one, both query derivative norms diverge at least as a positive constant times \(m^{-1/2}\). The sample coefficients are opposite in the h direction, so taking the difference mode preserves this divergence. The factor \(1/2\) in the mode definition does not remove it.

## 8. Bounded quantities versus divergent derivatives

The exact formulas also independently verify the current bounds used to support the obstruction:
\[
\begin{aligned}
\|q^2_a\|_2^2&=d^2+m(\alpha^2+\beta^2),\\
\|q^1_a\|_2^2&=d^2p_0^2+mk^2,\\
\|\delta^2_a\|_2^2&=d^2(p_0^2+d_2^2)+m(k^2+\ell^2),\\
\|\delta^1_a\|_2^2&=(p_0^2+d_1^2)(d^2p_0^2+mk^2),\\
\|\delta^3_a\|_2^2&=d^2+\bar p^2.
\end{aligned}
\]
The current raw speed has the exact expression
\[
\begin{aligned}
a^2={}&
\tfrac12(p_0^2+d_1^2)(d^2p_0^2+mk^2)\\
&+U_1^2(d^2p_0^2+m\ell^2)
+V_1^2(d^2d_2^2+mk^2)\\
&+d^2u^2+\bar p^2v^2+f^2m.
\end{aligned}
\]
The first line is the first raw block for \(C=I\), the second is \(\|B'\|_{\rm HS}^2\), and the third contains \(\|A'\|_{\rm HS}^2+\|F\|_2^2\). It is bounded and has a strictly positive limit.

The top curvature modes are
\[
m^3_-=-c_-b,\qquad m^3_+=-c_+o,
\]
so their norms and the weighted quantities
\[
u^2\|m^3_-\|_2^2+v^2\|m^3_+\|_2^2
=u^2c_-^2+v^2c_+^2
\]
are bounded. The corresponding exact matrix action density is
\[
\|A'\|_{\rm HS}^2=d^2u^2+\bar p^2v^2.
\]
On the middle layer, \(m^2_a=c_2q^2_a\) is uniformly bounded even in L-infinity, and its modes are
\[
m^2_-=-c_2dh-rc_2\beta,\qquad
m^2_+=rc_2\alpha x.
\]
The first- and second-layer feature-Gram weights \(U_1,V_1,u,v\) are fixed and finite. Thus the weighted L2 modal quantities described in the note remain bounded. Any further identification with an undisplayed imported density is within the stipulated conditional premise, not independent certification of that input.

The new selected-mode estimate is also explicitly compatible with the example:
\[
P^{3,\mathrm{mat}}_-
=\frac{c_-du^2+c_+\bar p v^2}{m}1_E,
\]
and therefore
\[
\|P^{3,\mathrm{mat}}_-\|_1
=|c_-du^2+c_+\bar p v^2|
\le d^2u^2+\bar p^2v^2.
\]
The full source satisfies
\[
\|P^3_a\|_1
=\tfrac12\bigl(|\epsilon_aK(m)+N(m)|
+|\epsilon_aK(m)-N(m)|\bigr)
=\max\{|K(m)|,|N(m)|\},
\]
which stays bounded, while
\[
\|P^3_a\|_2^2=\frac{K(m)^2+N(m)^2}{m}.
\]
This displays the L1/L2 distinction exactly, without a probabilistic factorization or experimental scaling argument.

## 9. Logical reach of the obstruction

The defensible quantifier is the one supplied by lines 543–550: there is a fixed finite tuple of upper bounds for the named current quantities, and a family of states satisfying those same bounds, for which
\[
\sum_a\bigl(\|(q^2_a)'\|_2+\|(q^1_a)'\|_2\bigr)\longrightarrow\infty.
\]
Thus no universal finite bound depending only on that tuple of upper bounds exists. An estimate allowed to depend on additional concentration or tail information, inverse vanishing quantities, kernel suprema, or prescribed history is not ruled out.

For every fixed \(m>0\), the kernels and fields in the construction are bounded. They can be represented on the finite partitions used above, where the softplus vector field is smooth and has a classical local trajectory. The instantaneous raw energy identity also follows directly by differentiating
\[
g=\sum_a\lambda_a\langle w,H^3_a\rangle:
\]
successive substitution of the forward derivatives, with
\(\mathfrak d_b=\lambda_b\delta^1_b\), gives
\[
g'=\|F\|_2^2+\|A'\|_{\rm HS}^2+\|B'\|_{\rm HS}^2
+\mathbb E[\mathfrak d^\top C\mathfrak d]=a^2.
\]
This is a local identity at the witness; it does not give it the stipulated global history.

In particular, the witness has \(w=-o\ne0\). It does not meet the prescribed zero-readout initial condition, and no argument in the note or this audit constructs it as a later state from that initialization. Its local action identity is not evidence that it belongs to a reference path satisfying the full initial-to-fitting action premise. Large derivatives at isolated arbitrary states also do not by themselves disprove an integrated derivative bound or uniform equicontinuity.

The document makes these distinctions explicitly at lines 552–562. Its final comments about retaining history and needing further tail or compactness information are appropriately limited: the note does not establish compactness of the moving source family, and this audit certifies no canonical convergence, uniqueness, or finite-width identification.

## 10. Required and optional fixes

### Required fixes

None for the new equations, inequalities, asymptotic coefficients, or the explicitly restricted bounded-state obstruction.

No additional conclusion about the prescribed reference sequence should be attached to this verdict. Such a conclusion would require a new argument using reachability/history or appropriate uniform tail control, as the document already acknowledges.

### Optional clarifications

1. **Make the uniform-bound quantifier in (20) explicit there.** Section 5 already supplies the correct interpretation. Stating directly at (20) that the right side is evaluated at a common tuple of upper bounds would avoid a literal reading involving an arbitrary, non-locally-bounded function of the exact state values.

2. **List the imported action-density expressions if standalone verifiability is desired.** Lines 396–400 refer to densities defined in unread inputs. The actual curvature fields, modal norms, feature weights, and matrix densities relevant to this calculation are bounded as shown above. Reproducing the precise imported list would make that identification independently checkable from this file alone. This is a scope clarification under the present conditional audit, not a request to recertify those dependencies.

3. **Optionally expose the two \(O(m)\) coefficients in (27).** They are \(a_0\eta_0\) and \(-\epsilon_aa_1\eta_1\) in the notation of this report. The existing remainder argument is valid, but these coefficients make the inclusion of all lower motions particularly easy to verify.

**Final verdict:** the new sidecar mathematics passes this isolated analytical audit under the stated premises. The constant-one L1 action estimate and the complete two-query algebraic obstruction both survive recalculation. This is not an actual-path counterexample and not final whole-goal certification.
