# Quantitative construction for Theorem T.1

The symbols and equations in this chapter have prefix Q. The sharper affine inputs are proved in Section 3 of the main text; the remaining response equations and estimates are reproduced in Appendix C, Part R.

## 2. An explicit Gaussian margin and a sharper transfer inequality

Write

\[
\mathcal R(Z)=\inf_{\alpha,\beta}
E[\arctan Z-\alpha-\beta Z]^2.
\]

For \(G\sim N(0,1)\), the Hermite polynomial \(H_3(G)=G^3-3G\)
is orthogonal to \(1,G\) and has squared norm six. Thus, by
Cauchy--Schwarz applied to the affine-regression residual,

\[
\mathcal R(\nu G)\ge\frac16
\bigl(E[H_3(G)\arctan(\nu G)]\bigr)^2.                 \tag{Q.1}
\]

Gaussian integration by parts gives

\[
E[H_3(G)\arctan(\nu G)]
=\nu E\frac{G^2-1}{1+\nu^2G^2}.
\]

Use \((1+\nu^2G^2)^{-1}=\int_0^\infty e^{-t}e^{-t\nu^2G^2}\,dt\).
Fubini is justified by the integrable bound \(|G^2-1|\), and the
Gaussian integrals give

\[
E[H_3(G)\arctan(\nu G)]
=-2\nu^3\int_0^\infty
      \frac{t e^{-t}}{(1+2\nu^2t)^{3/2}}\,dt.          \tag{Q.2}
\]

The measure \(t e^{-t}dt\) is a probability measure of mean two.
The integrand factor \((1+2\nu^2t)^{-3/2}\) is convex in \(t\),
so Jensen's inequality yields

\[
\mathcal R(\nu G)\ge
\frac{2\nu^6}{3(1+4\nu^2)^3}.                          \tag{Q.3}
\]

The right side is increasing in \(\nu>0\), since
\(\nu^2/(1+4\nu^2)\) is increasing. With \(m^2=\delta/32\),
one may therefore replace the unspecified Gaussian minimum by

\[
\bar\eta_\delta
=\frac{\delta^3}{49152(1+\delta/8)^3}>0.                \tag{Q.4}
\]

No upper-variance bound is needed for this particular margin.

There is also a uniform regression stability estimate with no inverse
variance loss. Let \(Z'\) be an independent copy of \(Z\). Since
arctangent is increasing and 1-Lipschitz,

\[
0\le\operatorname{Cov}(Z,\arctan Z)
=\tfrac12 E[(Z-Z')(\arctan Z-\arctan Z')]
\le\operatorname{Var}(Z).
\]

For nonconstant \(Z\), its optimal regression slope therefore belongs
to \([0,1]\). For constant \(Z\), choose slope zero. Use the optimal
intercept and slope for \(Z\) as a competitor for \(Z_0\). The
triangle inequality and the Lipschitz bound give

\[
\sqrt{\mathcal R(Z_0)}
\le\sqrt{\mathcal R(Z)}+2\|Z-Z_0\|_2.
\]

Interchanging the variables proves

\[
|\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
\le2\|Z-Z_0\|_2.                                      \tag{Q.5}
\]

Thus the sufficient transfer restriction is simply

\[
\|Z-Z_0\|_2\le\sqrt{\bar\eta_\delta}/4
\quad\Longrightarrow\quad
\mathcal R(Z)\ge\bar\eta_\delta/4.                    \tag{Q.6}
\]

Absorbing \((1-e)Z\) into the affine approximant gives the exact
activation-regression identity

\[
\inf_{\alpha,\beta}E[\psi_e(Z)-\alpha-\beta Z]^2
=e^2\mathcal R(Z).                                    \tag{Q.7}
\]

This improves the variance-dependent transfer coefficient in Appendix A from order
\(\delta^2/J\) to order \(\delta^{3/2}/J\), although the source
cutoff below is much more restrictive overall.

## 3. Literal explicit response chain available without any new estimate

Here is the safest direct specialization of Appendix C's complete (R.90) chain. It is included literally so that no
undefined instruction to enlarge a constant is part of the cutoff.
Fix \(P\ge1,S\ge1\), and define

\[
b_r=2P,\quad q=100b_r^3,\quad F_0=e^{qS},\quad T_0=qSF_0,
\]
\[
A_0=3q^2(F_0+1),\quad M_0=3Sq^2(F_0+1),\quad
\sigma=q,\quad D_0=q(1+T_0),\quad m_0=2qD_0,
\]
\[
A=A_0+1,\qquad M=M_0+1,\qquad k_0=3+6\sigma,
\]
\[
K_1=(k_0+12\sigma S)e^{2MS},\quad
K_2=(k_0+12A\sigma S)e^{2AMS},\quad
K_C=k_0S e^{2AS^2},
\]
\[
K_{q1}=6\sigma+MK_1,\quad K_{q2}=6\sigma+MK_2,\quad
K_q=1+K_C+K_{q1}+K_{q2},\quad
L_q=\sqrt{8\exp(1)}K_q,
\]
\[
H=40(1+A)(1+M)(1+S),\quad
X_0=2(1+2K_q)\exp(HS+H^2S^2L_q^2).                    \tag{Q.8}
\]

For any specified positive \(X\), continue the chain by

\[
R_0=200H^{11}e^{HS}[1+(S+1)X]+m_0(1+S),
\]
\[
K_F=e^{MS},\quad K_V=Ae^{AMS},\quad K_U=e^{AMS},\quad
K_T=S e^{AS^2},
\]
\[
D_2=R_0+K_F e^{M_0S},
\]
\[
C_V=[(1+MSK_V)D_2+A_0K_V]e^{A_0M_0S},\quad D_3=R_0+C_V,
\]
\[
C_T=S^2K_TD_3e^{A_0S^2},\quad E_3=R_0+C_T,
\]
\[
C_U=[MSK_UD_2+A_0K_U]e^{A_0M_0S},
\]
\[
E_2=R_0+K_UE_3+M_0C_U,\qquad
K_*=2\max\{1,D_2,D_3,E_2,E_3\}.                        \tag{Q.9}
\]

Taking \(X=X_0\), a literal valid source cutoff is

\[
E_{\rm lit}(P,S)=
\min\left\{1,\frac{P}{2T_0},
                 \frac1{2K_*\exp(K_*S)}\right\}.       \tag{Q.10}
\]

This is exactly \(\epsilon_*(1,P,S)\) in the manuscript, with its
whole constant chain displayed. The factor three in \(A_0,M_0\) and
the Gaussian maximum constant six safely dominate the two-sample
problem.

### Why the zero-offset/gain change is valid

The actual affine comparison is still with \(az\), at its actual
\(a\in[1/2,1]\). Setting \(a=1\) in the numerical chain is an
upper-bound operation on estimates, not a change in the comparator.
The source equations and derivative recursions contain the same formal
slots and array products. The removed offset has derivative zero and
only decreases the constant term in the growth estimate. Every actual
factor \(a\) or \(a^2\) in a norm estimate is at most one; both
\(|\phi'|\) and \(|D_q|\) are at most two, while
\(|D_z|\le e|q|\) in the response envelopes.

More concretely, on the ball \(b_r\ge2\), the tables (R.20)–(R.22)
at numerical gain one dominate every query and affine derivative of the
zero-offset network. The same-state perturbations obey
\(2e,3b_re,4b_r^2e\) in the forward layers and
\(b_re,b_r^2e,3b_r^2e,3b_r^3e,7b_r^3e\) in the listed backward
queries; these use only actual gain at most one. For example
\(2(1+ab_r)e\le3b_re\) because \(a\le1,b_r\ge2\).
The first-layer root maximum over two samples has the bound used for
three. Control norms remain at most one. Every estimate (R.38)–(R.89)
then holds with the gain-one numerical constants above.

There is no lower-gain premise in those upper estimates. Neither a
covariance inverse nor a positive offset is used. The low-gain bound is
needed separately for the affine variance/coercivity argument, proved
in Appendix A.

## 4. A fully explicit improved source cutoff

Two verified changes sharpen the literal chain. Neither uses an
unspecified replacement constant.

### 4.1 Retain the small coefficient in the exponential envelope

The exact envelope in (R.50) is

\[
\mathcal E_k=\exp\left(Hs_k+He\sum_{r<k}h_rQ_r\right).
\]

The derivation of (R.56), before dropping \(e\le1\), gives

\[
E\mathcal E_k^p\le
2\exp\left(pHS+\frac{p^2H^2e^2S^2L_q^2}{4}\right).
                                                               \tag{Q.11}
\]

Indeed the convexity bound (R.55) followed by
\(Ee^{uQ_r}\le2e^{u^2L_q^2/4}\) uses
\(u=pHeS\). This requires no time independence and no random
supremum. Add the explicit amplitude restriction

\[
e\le(HSL_q)^{-1}.                                      \tag{Q.12}
\]

Then (Q.11) with \(p=2\), Cauchy--Schwarz, and
\(\|1+Q_k\|_2\le1+\sqrt2K_q\) give

\[
E\mathcal E_k\le X_1,\qquad
E[(1+Q_k)\mathcal E_k]\le X_1,
\]
\[
X_1=2(1+2K_q)\exp(HS+1).                               \tag{Q.13}
\]

For the second bound the direct calculation is at most
\(\sqrt2(1+\sqrt2K_q)e^{HS+1/2}\), which is smaller than
\(X_1\). Higher finite moments also remain finite by (Q.11).

All same-array derivative remainders (R.59)–(R.67) use only the two
expectations in (R.58). Consequently the same displayed
\(R_0\) in (Q.9), now with \(X=X_1\), bounds them exactly as before:
the reverse-source remainder has its factor \(e h_j\), and a full
backward time row has its factor \(e\). In particular the current
terms \(L_kJ_k\) in both (R.65) and (R.66) are bounded by
\(eE[Q_k\mathcal E_k]\); they have not been discarded.

The chronological constants (Q.9) and their induction are unchanged.
Thus, even with the literal initial definitions from Section 3,

\[
\min\left\{1,\frac{P}{2T_0},\frac1{HSL_q},
                 \frac1{2K_*\exp(K_*S)}\right\}        \tag{Q.14}
\]

is an explicit valid threshold using \(X_1\). This reduces the tower
height of the crude sufficient dependence by one.

### 4.2 Use the sharper two-input affine estimates already proved

For the actual constant controls \(c_i=y_i/2\), Section 3 of the main text proves sharper affine coefficients, and
(T.21) proves the sharper primal comparison, than the single oversized
\(q\) in Appendix C.
Replace only the initial definitions of Section 3 by

\[
b_r=2P,\quad F=\exp(36P^2S),\quad q=100b_r^3,
\]
\[
T_0=40b_r^3S F,
\quad A_0=2(24P^2F+\tfrac92P^4),
\quad M_0=2S(8P^2F+P^4),
\]
\[
\sigma=q,\quad D_0=q(1+T_0),\quad m_0=2qD_0.           \tag{Q.15}
\]

The initial numerical bound \(q\) still bounds every query,
same-state query perturbation coefficient, and affine query Lipschitz
constant. Therefore \(D_0=q(1+T_0)\) and
\(m_0=2qD_0\) still bound the actual query and learned-moment errors.
The improved \(T_0\) is exactly the proved comparison
\(40b_r^3S e^{9b_r^2S}\). The displayed \(A_0,M_0\) are exactly
the two-input block/time-row bounds, including the factor two needed
for the time-row norm. Thus no inference from operator norm to formal
response norm is introduced here.

Starting with (Q.15), use all subsequent definitions
\(A,M,k_0,K_1,K_2,K_C,K_{q1},K_{q2},K_q,L_q,H\) in (Q.8),
use \(X=X_1\) from (Q.13), and use the entire finite chain (Q.9).
Define

\[
E_{\rm src}(P,S)=
\min\left\{1,\frac{P}{2T_0},\frac1{HSL_q},
                 \frac1{2K_*\exp(K_*S)}\right\}.       \tag{Q.16}
\]

Equations (Q.8), (Q.9), (Q.13), (Q.15), (Q.16) are a fully specified
finite elementary recipe. There is no hidden \(K\), compact
optimization, numerical experiment, or pointwise infimum over gains.

For completeness, the closure uses the exact inequalities
\(\alpha^2_k\le D_2(e+I_k)\),
\(\alpha^3_k\le D_3(e+I_k)\),
\(\beta^3_k\le E_3(e+I_k)\),
\(\beta^2_k\le E_2(e+I_k)\). Since
\(E_k=\beta^2_k+\beta^3_k\le K_*(e+I_k)\), the finite product
identity gives
\(e+I_k\le e\prod_{r<k}(1+K_*h_r)\le e e^{K_*S}\).
The last restriction in (Q.16) makes each new row differ from its
affine bound by at most one half. Construction proceeds in the exact
order \(A^2_k,A^3_k,B^3_k,B^2_k\). The moment and derivative
estimates at each stage require only the rows available at that stage,
as specified in (R.91)–(R.94); the added restriction (Q.12) concerns
only numerical constants and does not change this order.

## 5. One explicit monotone cutoff for the complete theorem

For \(0<\delta\le1\), retain the affine constants proved in Appendix A

\[
S_\delta=192/\delta,\quad
U_\delta=11+12\sqrt{2/\delta},\quad b=4U_\delta,
\]
\[
Q=40b^3S_\delta\exp(9b^2S_\delta),\quad
J=12b^2Q+\pi b^2,
\]
\[
O=10b^3Q+b(J+\pi/2),\quad
P_\delta=11+2U_\delta+4S_\delta(2U_\delta)^3.            \tag{Q.17}
\]

These \(Q,J\) are state/forward comparison constants, distinct from
the lower-case \(q\) used inside the source recipe. Define

\[
e_\delta=\min\left\{
\frac14,\ E_{\rm src}(P_\delta,S_\delta),\
\frac{b}{4Q},\ \frac1{4O},\
\frac{\sqrt{\bar\eta_\delta}}{4J}\right\}>0.            \tag{Q.18}
\]

One can also use the fully literal \(E_{\rm lit}\) from (Q.10)
in this formula; the rest of Theorem T.1 and its all-time margin are
unchanged, with a weaker sufficient dependence on \(\delta\).

For every fixed \(0<e\le e_\delta\), choose \(a=1-e\).
Then \(a\in[3/4,1]\subset[1/2,1]\). The raw state comparison
is at most \(Qe\le b/4\), so it closes strictly inside the primal
ball. Its endpoint prediction differs from \(3/2\) by at most
\(Oe\le1/4\), ensuring a hit of one. The forward discrepancy is
at most \(Je\le\sqrt{\bar\eta_\delta}/4\), so (Q.6)–(Q.7)
and the clock yield the explicit theorem conclusion

\[
\inf_{t\ge0}\min_{i=1,2}\min_{\ell=1,2,3}
\inf_{\alpha,\beta}
E[\psi_e(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
\ge\frac{e^2\delta^3}{196608(1+\delta/8)^3}>0.          \tag{Q.19}
\]

The source restriction supplies all other existence, uniqueness,
finite-GF/raw-GD, velocity, kernel, and path-law bridges proved in
Sections 4--6 of the main text. The initial nontriviality proof needs only \(e>0\), not
an additional quantitative lower or upper restriction.

### Monotonicity

The cutoff (Q.18) is nondecreasing in \(\delta\); equivalently it
decreases when the permitted inputs approach the excluded endpoints.
All of \(S_\delta,U_\delta,P_\delta,b,Q,J,O\) are nonincreasing
functions of \(\delta\), whereas \(\bar\eta_\delta\) is
increasing. In the source chain, every constant apart from a displayed
reciprocal is increasing in \(P,S\), through sums, products,
positive powers, exponentials and maxima. The only reciprocal with an
apparently increasing numerator simplifies to

\[
\frac{P}{2T_0}
=\frac1{640P^2S\exp(36P^2S)}
\]

for the improved chain, and to
\([1600P^2S\exp(800P^3S)]^{-1}\) for the literal chain. Both
decrease in \(P,S\). Finally
\(b/(4Q)=[160b^2S_\delta\exp(9b^2S_\delta)]^{-1}\)
also has the required monotonicity. Taking the minimum preserves it.

## 6. What sufficient asymptotic dependence has actually been proved

The explicit improved recipe is very conservative. Its asymptotic
scale can nonetheless be stated precisely as a sufficient bound.
As \(\delta\downarrow0\),

\[
S_\delta=O(\delta^{-1}),\quad
U_\delta=O(\delta^{-1/2}),\quad
P_\delta=O(\delta^{-5/2}),\quad
P_\delta^2S_\delta=O(\delta^{-6}).                       \tag{Q.20}
\]

In the improved source chain (Q.15), \(A_0,M_0,T_0\) and all
primitive constants are bounded by \(\exp(C\delta^{-6})\) for
some universal \(C\), enlarged finitely many times. Hence \(H\)
has that bound, whereas \(K_q,L_q,X_1,R_0,K_F,K_V,K_U,K_T\) and
the complete chronological \(K_*\) are bounded by

\[
\exp\bigl(\exp(C\delta^{-6})\bigr).
\]

The last denominator \(\exp(K_*S)\) adds one more exponential.
The other terms of (Q.18) are larger than a bound of this scale.
Therefore there are numerical constants \(C,\delta_0>0\) such that

\[
e_\delta\ge
\exp\{-\exp[\exp(C\delta^{-6})]\}
\qquad(0<\delta\le\delta_0).                           \tag{Q.21}
\]

In particular the displayed triple-exponentially small function itself
is a sufficient choice after fixing a large enough universal \(C\).
Equivalently the recipe has
\(\log\log\log(1/e_\delta)=O(\delta^{-6})\).
These statements give a sufficient allowed amplitude; they do not
provide an upper bound on the largest amplitude for which the theorem
could hold.

For comparison, the wholly literal chain (Q.8)–(Q.10) has
\(qS=O(\delta^{-17/2})\), and its \(X_0\), which discarded the
small factor \(e\) in the envelope, adds an extra exponential.
It yields the weaker but immediate sufficient scale

\[
\exp\{-\exp[\exp(\exp(C\delta^{-17/2}))]\}.
\]

Retaining the small coefficient as in (Q.11)–(Q.14) alone reduces this
to three exponentials with the same inner power \(17/2\). Using
the proved sharper two-input affine estimates reduces that power to
six, as in (Q.21).

No claim of necessity, optimality, or sharp endpoint behavior follows.
In particular this does not prove that the true admissible coefficient
must vanish at any such rate, that no polynomial lower bound exists,
or that one positive coefficient cannot work for all strictly
nonendpoint input pairs. The exact incompatible endpoint examples
remain valid, but they do not by themselves settle any of these
interior quantitative questions.


The chosen cutoff tends to zero as delta tends to zero: (Q.18) bounds it above by b/(4Q), whose reciprocal is 160 b² S_delta exp(9 b² S_delta) and tends to infinity. Its value is strictly positive at every fixed delta>0 in the nonvacuous range.
