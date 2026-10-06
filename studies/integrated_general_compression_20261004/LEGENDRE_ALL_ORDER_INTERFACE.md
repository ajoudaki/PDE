# An all-order Legendre error and storage interface

2026-10-05. Internal continuation of this study. This note proves that the
coefficient already displayed in `LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md`
controls every positive memory order. It removes the order restriction
without enlarging that coefficient, changing the closure, reducing the
existing label allowance, or adding a deterministic width threshold.
The probabilistic carrier event is inherited, with its existing implicit
sufficient width. This is a new deterministic derivation, not promotion.

## Model and conclusion

Fix hidden depth \(L\ge2\), width \(n\ge1\), sample count \(m\ge1\),
and inputs \(x_a\in\mathbb R^d\) with \(\|x_a\|_2=\sqrt d\).
For \(v=x/\sqrt d\), the dense network is
\[
 z^{(1)}=Av,\qquad
 z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\quad(2\le\ell\le L),
 \qquad h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n=w^\top h^{(L)}/n.
\]
The first matrix \(A\in\mathbb R^{n\times d}\) starts with independent
standard Gaussian entries; each later hidden matrix starts with independent
\(N(0,1/n)\) entries. All initialized blocks are independent, and
\(w(0)=0\). The loss is
\(m^{-1}\sum_a(f_n(x_a)-y_a)^2\), with block mobilities
\((n,1,\ldots,1,n)\).

For each positive integer \(q\), \(\widehat f_{n,q}\) is precisely the
original order-\(q\) Legendre closure defined in
`GENERAL_LEGENDRE_TRANSFER.md` §2. It retains the initialized hidden
mixers and evolves the first matrix, readout, scalar clock, and the two
families of \(q\) Legendre moments per hidden interface and training
sample. Its clock satisfies \(\dot\tau=\widehat\rho\), \(\tau(0)=1\),
where \(\widehat\rho^2=m^{-1}\sum_a(\widehat f_{n,q}(x_a)-y_a)^2\).
Its forward history has the constant unit prefix, and its backward
history has the zero prefix. The two predictors below use the same
initialization and the same physical time.

Assume every \(\phi_\ell\) is real on the real axis, holomorphic on
\(|\operatorname{Im}\zeta|<a\) for a common \(a>0\), and has bounded
first derivative on that strip. No bound on activation values is imposed.
Define
\[
 b=\max_\ell|\phi_\ell(0)|,\qquad
 s=\max\left\{1,\max_\ell\sup_{|\operatorname{Im}\zeta|\le a/2}
                                      |\phi_\ell'(\zeta)|\right\},
\]
\[
 t_2=\max_\ell\sup_{|\operatorname{Im}\zeta|\le a/2}
                                      |\phi_\ell''(\zeta)|,
 \qquad
 \beta=\max\{10,1+b,16/a,s,\max(1,t_2)\}.
\]
The derivative bounds are finite by the strip hypothesis. Define the
Gaussian covariance recursion and its unweighted final gap by
\[
 Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),\qquad
 \gamma=\lambda_{\min}(Q^{(L)})>0.
\]
Use the existing scalar abbreviations
\[
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,\qquad z=Y/\lambda,
 \qquad 0<z\le\beta^{-30L}.
 \tag{1}
\]
The unindexed scalar \(z\) is the label-to-gap ratio; the vectors
\(z^{(\ell)}\) are the layer preactivations.

Set, exactly as in the sample-exponent refinement,
\[
 B=\beta^{100L},\qquad u_n=\sqrt{\log(en)},
\]
\[
 P_n=3Bz^2(1+\lambda^{-1})(1+Bzu_n)
                      [1+Bz^2(e^{u_n}-1)].
 \tag{2}
\]
On the common initialization and dense-carrier event in that note,
simultaneously for every integer \(q\ge1\),
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |\widehat f_{n,q}(t,x)-f_n(t,x)|
 \le YP_n\frac{\sqrt{\log(eq)}}{q^2}.
 \tag{3}
\]
The time set includes the fitted limits. There is no further condition
on \(q\). All appearances of \(Y\) in (1)–(3) are its actual value.
The activation class, Gaussian initialization, original dynamics, label
cap, event, and error coefficient are unchanged.

For zero labels both systems are stationary and have zero prediction, so
every positive order is exact. All formulas involving division by \(Y\)
below are restricted to \(Y>0\).

The proof has two parts. The existing projection argument controls orders
above its actual absorption threshold. Below that threshold, the all-order
fitting theorem gives a uniform prediction bound. Retaining the label
powers in the threshold shows that this second bound is already covered
by the same coefficient \(P_n\).

## Proof of the all-order extension

The required outputs of the existing fitting and comparison arguments are
listed explicitly here. Define
\[
 q_0=1,\quad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
 \quad Z\sim N(0,1),\qquad
 H=\max\{1,\sqrt{q_1},\ldots,\sqrt{q_L}\}.
\]
These \(q_\ell\) are Gaussian scalar second moments, distinct from the
memory order \(q\). Dense fitting gives
\(\|w_D\|_2/\sqrt n\le2Y/\sqrt\lambda\); all-order closure fitting
gives \(\|\widehat w\|_2/\sqrt n\le4Y/\sqrt\lambda\).
Both give \(\|h^{(L)}(t,x)\|_2/\sqrt n\le2H\) for every sphere
query and all physical times, including the limits. Cauchy–Schwarz
therefore gives the order-independent prediction bound
\[
 \sup_{t,x}|\widehat f_{n,q}(t,x)-f_n(t,x)|
 \le \frac{12HY}{\sqrt\lambda}.
 \tag{4}
\]
Here and below the query supremum is over \(\|x\|_2=\sqrt d\).

For the projection comparison, let \(F_h\) be its forward-history
projection numerator, \(B_d\) its backward-response difference coefficient,
and \(\mathcal A_{\rm new}\) its parameter stability coefficient.
The source definitions are, with \(T_0=9s\),
\[
 R=8Y/\sqrt\lambda,\quad B_\delta=sT_0^{L-1}R,
 \quad F_z=2HT_0^{L-1},\quad a_0=4z,
\]
\[
 B_d=sT_0^{L-1}(1+B_\delta)+Lt_2F_zT_0^{L-1}M,
 \qquad F_h=V_h a_0\sqrt{(1+a_0)/2}.
\]
Here \(M\) is the actual dense training-carrier envelope, and \(V_h\)
is the explicit closure feature-speed bound. The complete definitions and
their verified recurrences are in the sample-exponent refinement §§2–6;
only the bounds stated next are used in this extension.

Write \(X=\beta^L\ge100\) and \(\chi=1+\lambda^{-1}\ge1\).
Equations (19), (26) of that refinement give
\[
 H\le X^2,\qquad F_h\le X^{24}z^2,\qquad
 B_d\le X^{33}(1+zu_n),
\]
\[
 \mathcal A_{\rm new}
 \le\sqrt{L+1}\exp\{X^{10}z+X^{36}z^2u_n\}.
 \tag{5}
\]
The actual absorption threshold is
\[
 T_n=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A_{\rm new}.
 \tag{6}
\]
For every integer \(q\ge T_n\), the existing projection absorption
estimate (25), followed by its coefficient estimate (27), proves (3).
This implication uses the actual threshold (6), not the enlarged
sufficient threshold \(P_n\) used in the earlier theorem statement.
It is valid on each finite time interval before passage to all time.

It remains to show that (4) implies (3) when \(1\le q<T_n\).
Since \(4(L-1)\le X^2\), \(\sqrt{L+1}\le X\), and
\(\sqrt{a_0}=2\sqrt z\), (5)–(6) give
\[
 T_n\le2X^{60}z^{5/2}(1+zu_n)
                \exp\{X^{10}z+X^{36}z^2u_n\}.
 \tag{7}
\]
Retaining the factor \(\sqrt z\) in this step is useful.

We now bound the square of (7) before replacing its exponential by a
larger one. Put \(\alpha=X^{10}z\) and \(\vartheta=X^{36}z^2\).
Assumption (1) implies
\[
 0<\alpha\le X^{-20},\qquad
 0<\vartheta\le X^{-24},\qquad
 e^{2\alpha}\le2,\qquad 2\vartheta\le\tfrac12.
 \tag{8}
\]
The exponential inequality follows, for example, from
\(e^v\le1+2v\) for \(0\le v\le1\), applied with
\(v=2\alpha\), and \(4\alpha\le1\).
For \(u\ge1\), the exponential series gives
\(u^2\le8e^{u/2}\), and \(e^u\le2(e^u-1)\), hence
\[
 u^2e^{u/2}\le16(e^u-1).
 \tag{9}
\]
Convexity gives
\(e^{2\vartheta u}\le1+2\vartheta(e^u-1)\), because
\(0\le2\vartheta\le1\). Combining this with
\((1+zu)^2\le2+2z^2u^2\), (8), and (9), yields
\[
 \begin{aligned}
 (1+zu)^2e^{2\alpha+2\vartheta u}
 &\le 2\left[2e^{2\vartheta u}
                     +2z^2u^2e^{u/2}\right]\\
 &\le4+(8\vartheta+64z^2)(e^u-1)\\
 &\le4[1+18X^{36}z^2(e^u-1)]\\
 &\le4[1+Bz^2(e^u-1)].
 \end{aligned}
 \tag{10}
\]
The last step uses \(18X^{36}\le X^{100}=B\).
In particular, squaring the stability factor has not doubled the width
exponent in the final envelope. The small-label condition verifies the
convexity range before that square is bounded.

Since \(12\le X\) and \(\lambda^{-1/2}\le\sqrt\chi\),
(7) and (10) give
\[
 \frac{12H}{\sqrt\lambda}T_n^2
 \le16X^{123}z^5\sqrt\chi
                       [1+Bz^2(e^{u_n}-1)].
 \tag{11}
\]
On the other hand,
\[
 16X^{23}z^3\le16X^{-67}\le3
                   \le3\sqrt\chi(1+Bzu_n).
\]
Multiplying this inequality by
\(X^{100}z^2\sqrt\chi[1+Bz^2(e^{u_n}-1)]\)
proves from (2), (11) that
\[
 \frac{12H}{\sqrt\lambda}T_n^2\le P_n.
 \tag{12}
\]
If \(1\le q<T_n\), (4), (12), and \(\sqrt{\log(eq)}\ge1\)
therefore imply
\[
 \sup_{t,x}|\widehat f_{n,q}-f_n|
 \le\frac{12HY}{\sqrt\lambda}
 \le\frac{YP_n}{T_n^2}
 \le\frac{YP_n}{q^2}
 \le YP_n\frac{\sqrt{\log(eq)}}{q^2}.
\]
Together with the already proved \(q\ge T_n\) case, this proves (3)
for every positive order. If \(T_n<1\), only the latter case is needed.
The proof introduces no new trajectory or carrier bound.

## Inverse order and storage certificates

Fix \(Y>0\), a width on the inherited event, and a requested absolute
error \(\varepsilon>0\). Let
\[
 r_{n,\varepsilon}=\frac{YP_n}{\varepsilon}.
\]
The least integer order certified by (3) is exactly
\[
 q_{\min}(n,\varepsilon)
 =\min\left\{q\in\mathbb N:\ q\ge1,\quad
          r_{n,\varepsilon}\sqrt{\log(eq)}\le q^2\right\}.
 \tag{13}
\]
This is a scalar inverse of the error bound, not an optimization over
the closure dynamics. There is no additional absorption or lower-order
test. The function \(g(q)=\sqrt{\log(eq)}/q^2\) is strictly decreasing
for real \(q\ge1\), because
\[
 \frac{g'(q)}{g(q)}
 =\frac1{2q\log(eq)}-\frac2q<0.
\]
It tends to zero; hence (13) exists, and every larger integer also meets
the target. If \(r_{n,\varepsilon}\le1\), then \(q_{\min}=1\).

For a direct sufficient formula, if \(r=r_{n,\varepsilon}>1\), set
\[
 q_{\rm suff}(n,\varepsilon)
 =\left\lceil2\sqrt r\,[\log(e+r)]^{1/4}\right\rceil.
 \tag{14}
\]
Put \(\ell=\log(e+r)>1\). Then
\(2\sqrt r\ell^{1/4}\le q_{\rm suff}\le3\sqrt r\ell^{1/4}\).
Moreover
\[
 \log(eq_{\rm suff})
 \le\log(3e)+\tfrac12\log r+\tfrac14\log\ell
 \le4\ell.
\]
Here \(\log(3e)\le2\log(e+1)\le2\ell\),
\(\log r\le\ell\), and \(\log\ell\le\ell\).
Consequently
\[
 r\frac{\sqrt{\log(eq_{\rm suff})}}{q_{\rm suff}^2}
 \le\frac{2r\sqrt\ell}{4r\sqrt\ell}=\frac12.
\]
Thus (14) even gives error at most \(\varepsilon/2\).
Use order one when \(r\le1\). In particular the sufficient order
has the dependence
\(O(\sqrt{YP_n/\varepsilon}\,[\log(e+YP_n/\varepsilon)]^{1/4})\)
when \(YP_n/\varepsilon>1\).

For any chosen order \(q\), the exact number of moving real coordinates
and the additional fixed mixer entries are
\[
 S_{\rm moving}(n,q)=n(d+1)+1+2(L-1)mnq,
 \qquad S_{\rm fixed}(n)=(L-1)n^2.
 \tag{15}
\]
Substituting (13) gives the smallest moving-state count certified by this
error envelope; substituting (14) gives a fully explicit sufficient count.
Neither is a lower bound on the actual approximation error or on other
representations.

Conversely, a moving-coordinate budget \(S\) admits
\[
 q_S=\left\lfloor\frac{S-n(d+1)-1}{2(L-1)mn}\right\rfloor
 \tag{16}
\]
orders whenever \(q_S\ge1\). At that order the certified error is
\(YP_n\sqrt{\log(eq_S)}/q_S^2\). Formula (16) concerns moving
coordinates; a total-storage budget must first reserve the fixed entries
in (15). Exact real arithmetic storage is being counted, with no claim
about a bit-complexity or numerical rounding bound.

For the existing root-width target, the earlier prescription simplifies to
\[
 Q_n=\max\{3,n^{1/4}\sqrt{P_n}\},\qquad
 q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil.
 \tag{17}
\]
The former entry \(P_n\) in the maximum is unnecessary. The same
elementary logarithm bound gives
\[
 \sup_{t,x}|\widehat f_{n,q_n}-f_n|
 \le\frac{YP_n}{8Q_n^2}\le\frac{Y}{8\sqrt n}.
 \tag{18}
\]
For fixed positive labels and the other fixed problem parameters,
\(\log P_n=O(\sqrt{\log n}+\log\log n)\), so
\(q_n=n^{1/4+o(1)}\) and
\(S_{\rm moving}(n,q_n)=n^{5/4+o(1)}\).
The fixed retained mixers remain quadratic in width.

## The complete recurrence-defined label allowance

The simple label cap (1) is sufficient for the stronger unchanged-coefficient
conclusion (3). An all-order interface is also available throughout the
larger, original intersection of the dense, closure, and source allowances
in `EXPLICIT_LEGENDRE_COMPARISON.md`. This paragraph does not impose (1).
Keep the same activations, model, initialization, dynamics, and common
event, and assume instead
\[
 0<Y\le\frac{\lambda}{8H\sqrt F},\qquad
 8Y/\lambda\le S_*^{\rm cl},\qquad
 16Y/\lambda\le S_*^{\rm src}.
 \tag{19}
\]
Here \(F\) and \(S_*^{\rm cl}\) are the existing dense and closure
constants, explicitly
\[
 F=s^2\left[(9s)^{2L-2}
                 +4H^2\sum_{j=0}^{L-2}(9s)^{2j}\right],
 \qquad D_\ell=s(9s)^{L-\ell},
\]
\[
 C_1=4s^2D_1^2,\qquad
 C_\ell=3s^2(64H^4D_\ell^2+82C_{\ell-1}),\qquad
 E=130\sum_{\ell=2}^LD_\ell\sqrt{C_{\ell-1}},
\]
\[
 S_*^{\rm cl}=\min\left\{1,\frac1{64H^2D_1},
        \frac1{\sqrt{8\sqrt{C_L}}},
        \left(\frac1{8H^2D_1E}\right)^{2/7}\right\}.
\]
The symbol \(S_*^{\rm src}\) denotes the numerical source activity
allowance already used in the existing comparison; it and
\(K_{\rm src}\) are inherited source-recurrence outputs, not additional
trajectory assumptions. This scoped note does not reread or alter that
source recurrence. On its event the dense carrier envelope is
\(M=32K_{\rm src}(Y/\lambda)u_n\).

For precision, all deterministic constants needed by the extended
comparison can be assembled as follows. Set
\[
 z=Y/\lambda,\quad\kappa=\lambda/4,\quad R=8Y/\sqrt\lambda,
 \quad S=8z,\quad a_0=4z,\quad T_0=9s,
 \quad B_\delta=sT_0^{L-1}R,\quad F_z=2HT_0^{L-1},
\]
\[
 P_0=1+2H(L-1),\quad
 B_d=sT_0^{L-1}(1+B_\delta)+Lt_2F_zT_0^{L-1}M,
 \quad V_z=2F_zB_\delta P_0,
\]
\[
 V_\delta=T_0^{L-1}
       [4sH+4sH(L-1)B_\delta^2+Lt_2MV_z].
\]
The closure speed and residual-direction constants are obtained from
\[
 T_1=2D_1R,\qquad
 T_\ell=4HD_\ell R+130D_\ell\sqrt{SC_{\ell-1}}\,R^2,
\]
\[
 V_1=sT_1,\quad V_\ell=s(2HT_\ell+9V_{\ell-1}),
 \quad V_h=\max_\ell V_\ell,
\]
\[
 C_c=4\left(4H^2+D_1^2R^2
                 +4H^2R^2\sum_{\ell=2}^LD_\ell^2\right)+\lambda/2.
\]
Define
\[
 F_h=V_ha_0\sqrt{(1+a_0)/2},\quad
 b_1=\frac{2\sqrt{1+a_0}}\kappa C_cB_\delta,
\]
\[
 b_0=\frac{\sqrt{1+a_0}Y}\kappa V_\delta
                             +2B_\delta\sqrt{a_0},
 \qquad C_f=2H+RsF_z.
\]

The signed stability proof of the sample-exponent refinement §§3–4
applies under (19): it requires only the physical fitting bounds,
\(\int\rho_D\le2z\), \(\int\widehat\rho\le4z\), and the dense
carrier envelope. The stronger cap (1) enters only its later power
envelopes and exponential interpolation. To specify that stability
constant here, define the segment feature bounds
\[
 Q_1=b+9s,\qquad Q_\ell=b+9sQ_{\ell-1},\qquad
 Q=\max\{1,Q_1,\ldots,Q_L\},\qquad F_{\rm seg}=QT_0^{L-1},
\]
\[
 d_0=sT_0^{L-1}(1+B_\delta),\qquad
 d_1=Lt_2F_{\rm seg}T_0^{L-1},\qquad p=1+Q(L-1),
\]
\[
 K_0=\sqrt{L+1}\{pd_0+[1+(L-1)B_\delta]sF_{\rm seg}\},
 \qquad K_1=\sqrt{L+1}\,pd_1,
\]
\[
 \mathcal A=\sqrt{L+1}\exp\{14(K_0+K_1M)z\}.
 \tag{20}
\]
The temporary \(d_1\) here is a scalar coefficient, not a parameter
distance. Set
\[
 T_n=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A,\qquad
 C_n=4(L-1)C_f\mathcal A F_h(b_0+b_1),\qquad
 U=12HY/\sqrt\lambda.
 \tag{21}
\]
Then the smooth two-term bound
\[
 \sup_{t,x}|\widehat f_{n,q}(t,x)-f_n(t,x)|
 \le C_n\frac{\sqrt{\log(eq)}}{q^2}
                         +U\left(\frac{T_n}{q}\right)^4
 \qquad(q=1,2,\ldots)
 \tag{22}
\]
holds simultaneously on the same event. To prove it, when \(q\ge T_n\)
the first term is already the inherited projection estimate, since
\(b_0+b_1\sqrt{\log q}\le(b_0+b_1)\sqrt{\log(eq)}\).
When \(q<T_n\), the second term is at least the unconditional cap
\(U\) in (4). Thus no lower-order condition appears in (22), and the
extra term decays faster than the original large-order error. This proof
does not replace (19) by a smaller label cap.

For the inverse, let \(q_1\) be the least positive integer satisfying
\[
 (2C_n/\varepsilon)\sqrt{\log(eq_1)}\le q_1^2,
\]
and choose
\[
 q\ge\max\left\{q_1,
       \left\lceil T_n(2U/\varepsilon)^{1/4}\right\rceil\right\}.
 \tag{23}
\]
Both terms of (22) are then at most \(\varepsilon/2\). The first
scalar inverse can use (14) with \(r=2C_n/\varepsilon\), and uses
one if that ratio is at most one. The second entry of (23) is an error
allocation, not an absorption gate: if \(\varepsilon>2U\), it is
strictly below \(T_n\) before rounding. The moving and fixed storage
certificates are again exactly (15)–(16), now with error (22).

At fixed admissible positive labels and all other fixed parameters,
\(C_n,T_n=n^{o(1)}\) because \(M=O(\sqrt{\log n})\), while \(U\)
is width independent. For a target \(\varepsilon=Y n^{-\alpha}\)
with fixed \(\alpha>0\), (23) therefore gives
\(q=n^{\alpha/2+o(1)}\): its second order requirement is only
\(n^{\alpha/4+o(1)}\). In particular the root-width target still
admits \(q=n^{1/4+o(1)}\) throughout (19). The simple coefficient
\(P_n\) and its polynomial sample dependence are established here only
under (1); the broader explicit recurrence interface (22) retains its
fully displayed data-dependent exponential in (20).

## Source scope and limitations

The scientific inputs read completely for this scoped extension were
the study's `LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md`,
`EXPLICIT_LEGENDRE_COMPARISON.md`,
`GENERAL_EXPLICIT_CLOSURE_FITTING.md`,
`GENERAL_EXPLICIT_FITTING.md`, `GENERAL_LEGENDRE_TRANSFER.md`,
`GENERAL_EXPLICIT_FITTING_CHECK.md`,
`GENERAL_EXPLICIT_CLOSURE_FITTING_CHECK.md`,
`EXPLICIT_LEGENDRE_COMPARISON_CHECK.md`,
`SIMPLE_CONSTANTS_LEGENDRE_CHECK.md`,
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`, and `docs/notation.qmd`.
Their statements about earlier work were treated as inherited interfaces;
no earlier study, frozen-book passage, or external scientific source was
accessed. The rigorous-math skill was read completely. The required
canonical-notation skill path returned `Permission denied`; this scoped
attempt used the supplied repository notation instructions and the
maintained notation contract.

The fitting and carrier events are common to all orders at one width, so
the extension needs no union bound over orders. At any fixed confidence,
the inherited event holds for every sufficiently large individual width.
Its stochastic carrier-width threshold remains implicit, and this note
does not claim one event for infinitely many independent widths.
The inverse is a deterministic certificate conditional on that same event.
The small-label cap (1) is used essentially in (8) and (12). The unchanged
coefficient conclusion (3) retains that cap, and the two-term extension
(22) retains exactly the existing larger allowance (19). Neither enlarges
its source theorem's label scope. No result has been promoted into `docs/`.
