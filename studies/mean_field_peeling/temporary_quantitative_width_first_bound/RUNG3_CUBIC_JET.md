# Third-rung cubic jet

**Superseding calculation.**  The formerly compressed arbitrary-time
third-derivative steps in Sections 4--5 below are expanded completely in
`../temporary_general_time_doubling/CUBIC_JET_COMPLETE_LEDGER.md`.  In
particular, its equations (3.3)--(3.14) prove \(R_N'''(0)\) one
product-rule atom at a time, equations (5.1)--(6.4) do the same for the
terminal contribution \(E_{3,N}\), and equations (8.1)--(8.11) prove the
final \(S_\phi,H_\phi\) grouping.  The supplement is the authoritative
no-omission proof of the formulas summarized here.

This note derives the cubic jet of the finite-time Gaussian operator DAG.  It
does not use a finite-width Taylor expansion.  The final section distinguishes
this operator theorem from the additional fixed-step identification needed for
an actual-network theorem at three or four steps.

## 1. The finite-time operator DAG

For a fixed integer \(N\), recursively define the following Gaussian program.
At time \(s\), let

$$
Q_{rs}=\mathbb E[H_rH_s],
\qquad
K_{rs}=\mathbb E[C_rC_s].
$$

The lower variables are

$$
u_{s+1}=u_s+h b_s\phi'(u_s),
\qquad H_s=\phi(u_s),
$$

$$
b_s
=\chi_s+
\sum_{r=0}^s\sigma_{sr}H_r
+h\sum_{r<s}K_{rs}H_r,
$$

where \((\chi_0,\ldots,\chi_s)\) is centered Gaussian with covariance
\((K_{rt})\), independently of \(U=u_0\), and

$$
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s].
$$

The top variables are

$$
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad
C_s=a_s\phi'(z_s),
$$

$$
z_s=\xi_s+\sum_{r<s}L_{sr}C_r,
\qquad
L_{sr}=\rho_{sr}+hQ_{rs},
$$

where \((\xi_0,\ldots,\xi_s)\) is centered Gaussian with covariance
\((Q_{rt})\), independently of \(A\), and

$$
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s].
$$

The output node is

$$
F_N(h)=\mathbb E[a_N\phi(z_N)].
$$

For \(N=1,2\), this is exactly Section 3 of `PROOF.md`.

The response form above is also the exact form forced by adaptive Gaussian
conditioning at every finite time, provided the population query Grams used
before the relevant action are invertible.  Indeed, with all previous fields
placed in vectors, write

$$
y=\xi+A_f^\top c,
\qquad
d_{\rm raw}=\chi+\Sigma^\top H.
$$

Then

$$
R:=\mathbb E[cy^\top]=\Sigma^\top Q+KA_f.
$$

For a new lower feature \(H_s\), Gaussian integration by parts gives

$$
\mathbb E[d_{\rm raw}H_s]=K\rho+\Sigma^\top q,
\qquad q=\mathbb E[HH_s].
$$

The row-conditioning coefficient of \(c\) is therefore

$$
K^{-1}\{K\rho+\Sigma^\top q-RQ^{-1}q\}
=\rho-A_fQ^{-1}q.
$$

The separate row projection \(y^\top Q^{-1}q\) contributes
\(c^\top A_fQ^{-1}q\), leaving exactly \(c^\top\rho\).

Similarly, for a new top cotangent \(C_s\), put

$$
k=\mathbb E[cC_s],
\qquad
r=\mathbb E[yC_s]=Q\sigma+A_f^\top k.
$$

The total coefficient of \(H\) in the column-conditioning formula is

$$
\Sigma K^{-1}k
+Q^{-1}\{r-R^\top K^{-1}k\}
=\sigma.
$$

Thus no unlisted response is introduced at later steps.

## 2. Activation moments

Use the notation of Section 8 of `PROOF.md`:

$$
\begin{aligned}
d&=\mathbb E[\phi_1^2],
&e&=\mathbb E[\phi_1^4],
&m&=\mathbb E[\phi_0\phi_2\phi_1^2],\\
j&=\mathbb E[\phi_3\phi_1^3],
&s_0&=\mathbb E[\phi_2^2\phi_1^2],
&\ell&=\mathbb E[\phi_0^2\phi_1^2],\\
b&=\mathbb E[\phi_0\phi_2],
&r&=\mathbb E[\phi_1\phi_3],
&t&=\mathbb E[\phi_2^2],
\end{aligned}
$$

where all activation factors are evaluated at one standard Gaussian.  Put

$$
c=1+d,
\qquad
\beta=b+cr,
\qquad
\delta=d+ct,
\qquad
k=d+\beta+\delta.
$$

Finally, let

$$
S
=3c^2m+3c^3j+3de\beta+3dkm+3d^2j
$$

and

$$
H
=c^2e+c\ell+2c^2m+3c^3s_0+cedt
+2ed^2+3d^2s_0+k^2\ell+2dkm.
$$

These are exactly \(S_\phi,H_\phi\) in `PROOF.md`.

## 3. General lower second jets

At \(h=0\), all \(\chi_r\) collapse to one
\(X\sim\mathcal N(0,d)\), all lower preactivations collapse to
\(G\), and all \(H_r\) collapse to \(g=\phi(G)\).  Write
\(p=\phi'(G)\), \(q=\phi''(G)\).

Direct differentiation of the operator recursion gives

$$
u_s'(0)=sXp,
$$

$$
u_s''(0)
=s(s-1)\{kgp+X^2pq\}.
$$

Indeed, the first derivative of the deterministic part of \(b_s\) is

$$
b_s'(0)=s(d+\delta+\beta)g=skg.
$$

Here the response derivatives themselves follow from the top operator, not
from an imported initialization jet:

$$
\sigma_{sr}'(0)=\delta \quad (r<s),
\qquad
\sigma_{ss}'(0)=s\beta.
$$

To see this, hold the Gaussian coordinates fixed.  At first order,

$$
C_s'
=\left(\sum_{r<s}\phi(x_r)\right)\phi'(x_s)
+cA^2\left(\sum_{r<s}\phi'(x_r)\right)\phi''(x_s).
$$

Differentiating this expression in a historical coordinate gives
\(d+ct=\delta\) after expectation; differentiating in \(x_s\) gives
\(s(b+cr)=s\beta\).  The Gaussian covariance \(Q(h)\) is even, so
\(Q'(0)=0\), and therefore Price differentiation introduces no covariance
term into these first response derivatives.

It follows that the three contributions to \(b_s'(0)\) are: \(s\)
learned-matrix terms of size \(dg\), \(s\) historical responses of size
\(\delta g\), and one terminal response of size \(s\beta g\).  Substitution into

$$
u_{s+1}=u_s+h b_s\phi'(u_s)
$$

proves the two displayed formulas by induction.

Consequently

$$
H_s'(0)=sXp^2,
$$

$$
H_s''(0)
=s(2s-1)X^2p^2q+s(s-1)kgp^2.
$$

The lower Gaussian covariance \(K(h)\) is even.  Thus \(K'(0)=0\), and the
only possible covariance term in this second derivative is

$$
\frac12K''(0):D_\chi^2\{H_rH_s\}\big|_{h=0}.
$$

The zeroth integrand is \(g^2\), independent of every
\(\chi\)-coordinate, so this term vanishes.  Hence, for all \(r,s\),

$$
\boxed{
Q_{rs}''(0)
=dm\{r(2r-1)+s(2s-1)\}
+k\ell\{r(r-1)+s(s-1)\}
+2rsde.
}
$$

This specializes to every \(Q''\) displayed in Sections 8.1 and 8.4 of
`PROOF.md`.

## 4. Sum of the lower response jets

Only the sum

$$
R_N=\sum_{r<N}\rho_{Nr}
$$

enters the direct terminal third derivative.  Let

$$
T_2=\frac{N(N-1)(2N-1)}6,
\qquad
C_2=\frac{N(N-1)}2,
\qquad
C_3=\frac{N(N-1)(N-2)}6.
$$

Before coalescing the \(\chi\)'s, set
\(S_s=\sum_{r<s}\chi_r\).  Then

$$
u_s'=pS_s,
$$

$$
u_s''
=s(s-1)kgp+2pq\sum_{r<s}\chi_rS_r.
$$

If \(D=\sum_{r<N}\partial_{\chi_r}\), direct differentiation of the
lower recursion gives

$$
\begin{aligned}
D u_N'''={}&
6p^3\{(\delta+d)C_3+\beta T_2\}\\
&+3kgpq(3T_2-C_2)
+9X^2p^2\phi_3T_2
+18X^2pq^2C_3.
\end{aligned}
$$

Using

$$
D H_N'''
=3\phi_3(u_N')^2Du_N'
+3q\{Du_N'\,u_N''+u_N'Du_N''\}
+pDu_N'''
$$

and taking expectation yields

$$
\boxed{
\begin{aligned}
R_N'''(0)={}&
\frac32N(4N^2-3N+1)dj\\
&+6N(N-1)(2N-1)ds_0\\
&+3N(N-1)(2N-1)km\\
&+N(N-1)e\{(\delta+d)(N-2)+\beta(2N-1)\}.
\end{aligned}
}
$$

The singular-covariance third Price formula contains exactly one possible
source-covariance term,

$$
\frac32K''(0):D_\chi^2\partial_h(DH_N)\big|_{h=0}.
$$

But \(\partial_h(DH_N)|_{h=0}=Np^2\), which is independent of all
\(\chi\)-coordinates.  Therefore this term vanishes.  This accounts for
all derivatives of the lower Gaussian source law; none is hidden in the
fixed-coordinate calculation above.

Since \(L_{Nr}=\rho_{Nr}+hQ_{rN}\),

$$
\sum_{r<N}L_{Nr}'''(0)
=R_N'''(0)+3\sum_{r<N}Q_{rN}''(0),
$$

where summing the formula in Section 3 gives

$$
\boxed{
\begin{aligned}
\sum_{r<N}Q_{rN}''(0)={}&
\frac{N(16N^2-15N+5)}6dm\\
&+\frac{2N(N-1)(2N-1)}3k\ell
+N^2(N-1)de.
\end{aligned}
}
$$

## 5. Terminal direct and Price terms

At coalescence of the top Gaussian variables,

$$
a_N'=Ng,
\qquad
a_N''=N(N-1)cAp^2,
$$

$$
a_N'''
=cN(N-1)(N-2)gp^2
+\frac12c^2N(N-1)(4N-5)A^2p^2q,
$$

and

$$
z_N'=NcAp,
$$

$$
z_N''=cN(N-1)\{gp+cA^2pq\}.
$$

Writing \(L_N^{(3)}=\sum_{r<N}L_{Nr}'''(0)\), the direct third derivative
of \(z_N\) is

$$
\begin{aligned}
z_N'''={}&ApL_N^{(3)}
+c^2N(N-1)(N-2)Ap^3\\
&+3c^2N(N-1)^2Agpq\\
&+\frac12c^3N(N-1)(2N-1)A^3p^2\phi_3\\
&+c^3N(N-1)(N-2)A^3pq^2.
\end{aligned}
$$

Substitution into the six product/chain-rule terms for
\((a_N\phi(z_N))'''\) gives the complete fixed-coordinate contribution

$$
\boxed{
\begin{aligned}
E_{3,N}={}&
2cN(N-1)(2N-1)\ell\\
&+2c^2N(N-1)(2N-1)e\\
&+\frac12c^2N(28N^2-33N+11)m\\
&+\frac32c^3N(4N^2-3N+1)j\\
&+6c^3N(N-1)(2N-1)s_0+dL_N^{(3)}.
\end{aligned}
}
$$

The first terminal integrand derivative, before coalescence, is

$$
\psi_1
=\left(\sum_{r<N}\phi(x_r)\right)\phi(x_N)
+cA^2\left(\sum_{r<N}\phi'(x_r)\right)\phi'(x_N).
$$

Its historical diagonal Hessians have expectation \(\beta\), its terminal
diagonal Hessian has expectation \(N\beta\), its historical-terminal
Hessians have expectation \(\delta\), and all distinct historical Hessians
vanish.  Therefore the singular-covariance Price correction is exactly

$$
\boxed{
P_N
=\frac32\beta
\left\{\sum_{r<N}Q_{rr}''(0)+NQ_{NN}''(0)\right\}
+3\delta\sum_{r<N}Q_{rN}''(0).
}
$$

This is the entire contribution from differentiation of the top Gaussian
source law.  Indeed, \(Q(h)\) is even, so the first and third covariance
derivatives vanish, and the singular-covariance third Price identity is

$$
F_N'''(0)
=\mathbb E[\partial_h^3\psi_0]
+\frac32Q''(0):\mathbb E[D_x^2\partial_h\psi_0].
$$

The first term is \(E_{3,N}\), while the second is precisely \(P_N\).

The remaining diagonal sum is

$$
\begin{aligned}
\sum_{r<N}Q_{rr}''+NQ_{NN}''={}&
\frac{N(16N^2-15N+5)}3dm\\
&+\frac{4N(N-1)(2N-1)}3k\ell\\
&+\frac{N(8N^2-3N+1)}3de.
\end{aligned}
$$

Combining \(E_{3,N}\), \(P_N\), the two response sums, and
\(k=d+\beta+\delta\), and grouping the displayed activation moments gives

$$
\boxed{
F_N'''(0)
=\frac{N(4N^2-3N+1)}2S
+2N(N-1)(2N-1)H.
}
$$

This is a nodewise differentiation of the limiting Gaussian program.  It
does not input finite-width jets and does not exchange the width and
learning-rate limits.  For \(N=1\) it gives \(S\); for \(N=2\) it gives
\(11S+12H\), agreeing with the independent calculations in `PROOF.md`.

## 6. The third- and fourth-rung cubic coefficients

Parity of the operator DAG gives odd \(F_N\), and the first derivative is

$$
F_N'(0)=N(1+d+d^2).
$$

For

$$
\Delta_{31}(\eta)=F_3(\eta)-F_1(3\eta),
$$

the linear terms cancel and

$$
F_3'''(0)=42S+60H.
$$

Thus

$$
\boxed{
\kappa_{31}
=\frac{F_3'''(0)-27F_1'''(0)}6
=\frac52S+10H
=\frac52(S+4H).
}
$$

For

$$
\Delta_{42}(\eta)=F_4(\eta)-F_2(2\eta),
$$

one has

$$
F_4'''(0)=106S+168H,
$$

and hence

$$
\boxed{
\kappa_{42}
=\frac{F_4'''(0)-8F_2'''(0)}6
=3S+12H
=3(S+4H).
}
$$

The constant-activation edge case has \(S=H=0\) and
\(F_N(h)=Nh\), so both discrepancies vanish identically.  For an affine
RMS-normalized activation, \(S=0\) and

$$
H=d+2d^2+6d^3+3d^4.
$$

Thus \(\kappa_{31}=10H\) and \(\kappa_{42}=12H\).  In particular, for
\(\phi(x)=x\), these coefficients are \(120\) and \(144\), respectively.

## 7. Quantitative remainder and fixed-step rank bridge

Once actual-network fixed-step identification and the activation-envelope
compiler have been extended to \(F_3\), define the compiler output

$$
\overline{\mathcal J}_{3,5}
\ge |F_3^{(5)}(h)|
$$

on its explicitly certified interval.  Taylor's integral remainder then
gives the activation-defined candidate

$$
B_{31}
=\frac1{120}
\left(\overline{\mathcal J}_{3,5}
+3^5\overline{\mathcal J}_{1,5}\right).
$$

Similarly,

$$
B_{42}
=\frac1{120}
\left(\overline{\mathcal J}_{4,5}
+2^5\overline{\mathcal J}_{2,5}\right).
$$

The chronological envelope recursion of Section 6 terminates after adding
the corresponding finite lower/top stages; it remains activation-defined
and has no output-derived constants.

The original `PROOF.md` does not prove the fixed-nonzero-step identification
of the actual network for three or four steps.  At three steps, adaptive
conditioning must invert the three-time population feature and cotangent
Grams

$$
Q^{(2)}=(Q_{rs})_{0\le r,s\le2},
\qquad
K^{(2)}=(K_{rs})_{0\le r,s\le2}.
$$

The following forward-difference argument supplies the missing rank lemma
without differentiating a determinant eight times.  For a three-time Gram
\(G=(G_{rs})_{0\le r,s\le2}\), put

$$
N_{ab}(h)
=\sum_{r\le a}\sum_{s\le b}
(-1)^{a-r+b-s}\binom ar\binom bsG_{rs}(h),
$$

and, for \(h\ne0\),

$$
\widehat G_{ab}(h)=\frac{N_{ab}(h)}{h^{a+b}}.
$$

This is the Gram of the zeroth, first, and second forward-difference fields.
The operator jets give \(N_{ab}^{(j)}(0)=0\) for \(j<a+b\), so
\(\widehat G\) extends continuously to zero.

For the feature Gram, take independent
\(U\sim\mathcal N(0,1)\), \(B\sim\mathcal N(0,d)\), and
\(T\sim\mathcal N(0,\tau)\), where

$$
\tau=\ell+2cm+3c^2s_0+edt.
$$

Its forward jet fields are

$$
P_0=\phi(U),
\qquad
P_1=B\phi'(U)^2,
$$

$$
P_2
=T\phi'(U)^2+k\phi(U)\phi'(U)^2
+2B^2\phi'(U)^2\phi''(U).
$$

They satisfy

$$
\langle P_0,P_1\rangle
=\langle P_1,P_2\rangle=0,
\qquad
\|P_1\|_2^2=de,
$$

$$
a_Q:=\langle P_0,P_2\rangle=k\ell+2dm,
$$

and

$$
\lambda_Q
:=\|P_2-a_QP_0\|_2^2
\ge\tau e>0.
$$

Consequently

$$
\det\widehat Q(0)=de\lambda_Q>0.
$$

For the cotangent Gram, let \(X,Z_1,Z_2,A\) be independent standard
Gaussians, and set

$$
S_1=\sqrt{de}\,Z_1,
\qquad
R=a_QX+\sqrt{\lambda_Q}\,Z_2,
$$

$$
g=\phi(X),\quad p=\phi'(X),\quad q=\phi''(X),\quad r_3=\phi'''(X),
$$

$$
R_1=S_1+cAp,
\qquad T_0=Ap,
$$

$$
T_1=gp+AqR_1,
\qquad R_2=R+cT_1,
$$

$$
T_2
=p^2R_1+AqR_2+2gqR_1+Ar_3R_1^2.
$$

These are the zeroth, first, and second cotangent forward jets.  One has

$$
\langle T_0,T_1\rangle=0,
\qquad
\|T_0\|_2^2=d,
\qquad
\|T_1\|_2^2=\tau.
$$

Writing

$$
\lambda_K
=\left\|T_2-operatorname{Proj}_{\operatorname{span}(T_0,T_1)}T_2
\right\|_2^2,
$$

if \(t=\mathbb E[q^2]>0\), the independent \(Z_2\)-component gives

$$
\lambda_K\ge t\lambda_Q>0.
$$

If \(t=0\), continuity forces \(\phi\) to be affine; then the independent
\(Z_1\)-component has squared norm \(d^5>0\).  Thus in every nonconstant
case

$$
\det\widehat K(0)=d\tau\lambda_K>0.
$$

This is also quantitative using only the fifth-derivative compiler.  If
\(\bar G_{rs,j}\) are its activation-defined derivative majorants, define

$$
e_{ab}(G)
=\frac1{(a+b+1)!}
\sum_{r\le a,s\le b}
\binom ar\binom bs\bar G_{rs,a+b+1},
$$

$$
E_G=\left(\sum_{a,b=0}^2e_{ab}(G)^2\right)^{1/2},
\qquad
\underline\lambda_G
=\frac{\det\widehat G(0)}{\operatorname{tr}(\widehat G(0))^2}.
$$

Taylor's integral formula applied separately to each forward difference
gives

$$
\|\widehat G(h)-\widehat G(0)\|_{\rm op}
\le E_G|h|.
$$

Since \(\underline\lambda_G\le\lambda_{\min}(\widehat G(0))\), the explicit
radius

$$
r_G
=\min\left\{1,
\frac{\underline\lambda_G}{2(1+E_G)}\right\}
$$

ensures \(\widehat G(h)\succ0\), hence \(G(h)\succ0\), for every
\(0<|h|\le r_G\).  Only derivatives through
\(a+b+1\le5\) occur.

Thus the three-time rank obstruction can be closed by taking the final
fixed-step radius below \(r_Q\wedge r_K\).  To turn this note by itself into
an actual-network theorem, one must still instantiate the finite-query
convergence proof of Section 4.2 for the seven actions

$$
Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3,
$$

and extend the explicit activation-envelope chronology through the third
terminal top node.  The block response cancellations were proved in Section
1 above, and the rank estimates needed by that instantiation are now
explicit.  Until that finite seven-action ledger and compiler extension are
written into the theorem, the boxed coefficients remain an unconditional
operator-DAG result rather than, by themselves, a completed actual-network
result.
