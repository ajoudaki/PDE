# Check of a single-coefficient Legendre bound

2026-10-04. Scoped algebraic compression of the current study's explicit
fitting and Legendre comparison constants. This note proves no new
probabilistic source theorem. It takes the two source-envelope inequalities
in (2) below as dependencies supplied for separate verification by the
coordinator. No earlier study or maintained source is modified.

## 1. Assumptions and concise conclusion

Fix hidden depth \(L\ge2\), sample count \(m\), input dimension \(d\),
and sphere inputs \(x_a\in\mathbb R^d\), \(\|x_a\|=\sqrt d\).
Use the canonical Gaussian initialization, zero initial readout, mean
squared loss, block mobilities \((n,1,\ldots,1,n)\), and the original
residual-RMS-clock Legendre closure from this study. Dense and closure
have the same width and the same initialization. All comparisons below
are in their unchanged physical time.

Let \(a>0\) be a common holomorphic strip width, and let
\[
 b=\max_\ell|\phi_\ell(0)|,\qquad
 s=\max\left\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
                       |\phi_\ell'(z)|\right\},
\]
\[
 t_2=\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
                         |\phi_\ell''(z)|,\qquad
 \beta=\max\{10,1+b,16/a,s,\max(1,t_2)\}.
\]
The first derivative is assumed bounded on the full open strip, as in
the source theorem. These half-strip constants therefore exist. Activation
values may be unbounded. Real derivative constants in the fitting and
comparison notes are no larger than the displayed \(s,t_2\), so these
larger constants can be used in all their nonnegative recurrences.

Define the Gaussian feature covariance by
\[
 Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}).
\]
Let
\[
 \gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m.
\]
In particular \(\gamma\) is the unweighted covariance gap. Assume
\[
                 0<Y\le\lambda\beta^{-30L}.             \tag{1}
\]
The two source-envelope dependencies are
\[
 S_*^{\rm src}\ge\beta^{-26L},\qquad
 K_{\rm src}\le\beta^{21L},                              \tag{2}
\]
with the source activity parameter \(S_{\rm src}=16Y/\lambda\).
The actual all-time dense carrier bound on the source event is
\[
 \max_{a,\ell,i}\sup_{t\ge0}|k_{D,a,i}^{(\ell)}(t)|
 \le M:=2K_{\rm src}S_{\rm src}\sqrt{\log(en)}.            \tag{3}
\]
The factor two is the all-time enlargement in the explicit comparison
note, not a newly proved source estimate here.

Put
\[
 B=\beta^{100L}(1+\lambda^{-1})^4,
 \qquad
 q_n=\left\lceil n^{1/4}
                   e^{B\sqrt{\log(en)}}\right\rceil.    \tag{4}
\]
On the common initialization/fitting and source event, the conclusion is
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
      |f_{n,q_n}(t,x)-f_n(t,x)|\le Y/\sqrt n.             \tag{5}
\]
The endpoint \(t=\infty\) is included using the physical convergence
already proved by the fitting theorems. More generally, the following
fixed-order envelope holds simultaneously for every integer in its range:
\[
 q\ge e^{(B/8)\sqrt{\log(en)}}
 \quad\Longrightarrow\quad
 \|f_{n,q}-f_n\|_*
 \le\frac{Y e^{(B/8)\sqrt{\log(en)}}\sqrt{\log(eq)}}{q^2},
                                                               \tag{6}
\]
where \(\|f-g\|_*\) denotes the two suprema in (5).

The deterministic algebra in (4)--(6) holds for every integer \(n\ge1\)
for which the stated events hold. It introduces no additional eventual
width condition. The source theorem's stochastic sufficient width remains
unquantified. Accordingly this is not a claim that the source event has
the desired probability at every width.

## 2. The common label allowance

Write \(P_\beta=\beta^L\), so \(P_\beta\ge100\).
The dense and closure fitting notes have the sufficient allowances
\(Y\le\lambda\beta^{-5L}\) and
\(Y\le\lambda\beta^{-10L}\), respectively. Condition (1) implies both.
For the source,
\[
 S_{\rm src}=16Y/\lambda
 \le16P_\beta^{-30}\le P_\beta^{-26}
 \le S_*^{\rm src},                                    \tag{7}
\]
since \(16\le P_\beta^4\). Thus the claimed common label allowance
follows once the first dependency in (2) is verified. This check does
not replace that verification.

## 3. Bounds on the physical constants

For the remaining proof set
\[
 \chi=1+\lambda^{-1},\qquad u=\sqrt{\log(en)}.
\]
Both are at least one. All exponents below refer to the single quantity
\(P_\beta\), not to width.

The fitting notes define
\[
 q_0=1,\quad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
 \quad Z\sim N(0,1),\qquad
 H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}).
\]
Their elementary Gaussian recursion and closure-energy recurrence give
\[
 H\le P_\beta^2,\quad \lambda\le H^2\le P_\beta^4,
 \quad D_\ell=s(9s)^{L-\ell}\le P_\beta^2,
 \quad \sqrt{C_\ell}\le P_\beta^8,                        \tag{8}
\]
where
\[
 C_1=4s^2D_1^2,\qquad
 C_\ell=3s^2(64H^4D_\ell^2+82C_{\ell-1}).
\]
Here (8) uses the already established sharper bound
\(H\le\beta^{3L/2}\) when invoking the closure note's bound
\(\sqrt{C_L}\le\beta^{8L}\); its displayed weakening to
\(H\le P_\beta^2\) is only for subsequent algebra.

Use exactly the comparison's choices
\[
 \kappa=\lambda/4,\quad R=8Y/\sqrt\lambda,
 \quad S_{\rm cl}=8Y/\lambda,\quad a_0=Y/\kappa.
\]
Condition (1) and (8) imply
\[
 R\le8P_\beta^{-28}\le P_\beta^{-27},\qquad
 S_{\rm cl}\le1,\qquad a_0\le1.                         \tag{9}
\]
Equation (3) and the second dependency in (2) imply
\[
 M\le32P_\beta^{21}(Y/\lambda)u
   \le32P_\beta^{-9}u\le u.                            \tag{10}
\]

The closure speed outputs are defined by
\[
 T_1=2D_1R,\qquad
 T_\ell=4HD_\ell R+
   130D_\ell\sqrt{C_{\ell-1}S_{\rm cl}}\,R^2\quad(\ell\ge2),
\]
\[
 V_1=sT_1,\quad V_\ell=s(2HT_\ell+9V_{\ell-1}),
 \qquad V_h=\max_\ell V_\ell.
\]
Since \(R,S_{\rm cl}\le1\),
\[
 T_1\le P_\beta^3R,\qquad
 T_\ell\le(4P_\beta^4+130P_\beta^{10})R
            \le P_\beta^{12}R.
\]
The forcing in the recurrence for \(V_\ell\) is at most
\(2P_\beta^{15}R\). Its propagation factor over all layers is at most
\((9s)^L\le P_\beta^2\). Summing at most \(L\) terms, and using
\(3L\le P_\beta^2\), proves the conservative bound
\[
                         V_h\le P_\beta^{20}R.          \tag{11}
\]
The other closure output is
\[
 C_c=4G_{\rm cl}+\lambda/2,\qquad
 G_{\rm cl}=4H^2+D_1^2R^2+
                  4H^2R^2\sum_{\ell=2}^LD_\ell^2.
\]
Using \(9L\le P_\beta^2\) gives
\[
 G_{\rm cl}\le9LP_\beta^8\le P_\beta^{10},\qquad
 C_c\le P_\beta^{11}.                                  \tag{12}
\]

## 4. Bounds on the comparison constants

To distinguish it from the new coefficient \(B\) in (4), denote the
quantity named \(B\) in `EXPLICIT_LEGENDRE_COMPARISON.md` by \(B_\delta\).
The exact definitions are
\[
 T_0=9s,\quad F_z=2HT_0^{L-1},\quad
 B_\delta=sT_0^{L-1}R,\quad P=1+2H(L-1),\quad G=PB_\delta+2H,
\]
\[
 B_d=sT_0^{L-1}(1+B_\delta)+Lt_2F_zT_0^{L-1}M,
 \qquad J=PB_d+[1+(L-1)B_\delta]sF_z.
\]
Equations (8)--(10), together with \(s,t_2\le P_\beta\), yield
\[
 F_z\le P_\beta^5,\quad B_\delta\le P_\beta^{-24}\le1,
 \quad P\le P_\beta^4,\quad G\le P_\beta^5,
\]
\[
 B_d\le P_\beta^{11}u,\qquad J\le P_\beta^{16}u.         \tag{13}
\]
For example the two contributions to \(B_d\) are bounded by
\(2P_\beta^3\) and \(LP_\beta^8u\); the two contributions to \(J\)
are then bounded by \(P_\beta^{15}u\) and \(LP_\beta^6\).

The stability coefficient is
\[
 \mathcal A=\left(1+\frac{4GHB_\delta}{\kappa}\right)
 \exp\left\{2J\left(1+\frac{4G^2}{\kappa}\right)
                       \frac Y\kappa\right\}.
\]
Its prefactor is at most \(1+16P_\beta^7\chi\le P_\beta^9\chi\).
Using only \(Y/\lambda\le1\) in the exponent gives
\[
 2J(1+4G^2/\kappa)Y/\kappa
 \le136P_\beta^{26}\chi u\le P_\beta^{28}\chi u.
\]
Consequently
\[
 \mathcal A\le P_\beta^9\chi
                     e^{P_\beta^{28}\chi u}.            \tag{14}
\]

The remaining exact definitions are
\[
 V_z=2F_zB_\delta P,
 \quad V_\delta=T_0^{L-1}
 [4sH+4sH(L-1)B_\delta^2+Lt_2MV_z],
\]
\[
 F_h=V_h a_0\sqrt{(1+a_0)/2},\qquad
 b_1=\frac{2\sqrt{1+a_0}}\kappa C_cB_\delta,
\]
\[
 b_0=\frac{\sqrt{1+a_0}Y}\kappa V_\delta
                       +2B_\delta\sqrt{a_0},\qquad
 C_f=2H+RsF_z.
\]
Their bounds, retaining the factor of \(Y\) needed for the final error,
are
\[
 V_z\le P_\beta^{10},\quad V_\delta\le P_\beta^{16}u,
 \quad F_h/Y\le P_\beta^{21}\chi,\quad F_h\le P_\beta^{20},
\]
\[
 b_0\le P_\beta^{17}u,\quad
 b_1\le P_\beta^{12}\chi,\quad C_f\le P_\beta^7.          \tag{15}
\]
For \(F_h/Y\), use \(a_0/Y=4/\lambda\), (11), and \(R\le1\).
For \(b_0\), use \(Y/\lambda\le1\) and \(a_0,B_\delta\le1\).
There is therefore no hidden division by an uncontrolled small label.

The actual absorption threshold is
\[
 q_{\rm abs}=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A.
\]
The inequalities \(4(L-1)\le P_\beta^2\), (13)--(15) give
\[
 q_{\rm abs}\le P_\beta^{42}\chi u
                       e^{P_\beta^{28}\chi u}.           \tag{16}
\]
For \(q\ge1\), both \(u\) and \(\sqrt{\log(eq)}\) are at least one.
Thus
\[
 b_0+b_1\sqrt{\log q}
 \le P_\beta^{18}\chi u\sqrt{\log(eq)}.
\]
The numerator of the existing error estimate is bounded by
\[
 4(L-1)C_f\mathcal A F_h(b_0+b_1\sqrt{\log q})
 \le YP_\beta^{57}\chi^3u
        e^{P_\beta^{28}\chi u}\sqrt{\log(eq)}.            \tag{17}
\]

For \(P_\beta\ge100\) and \(\chi,u\ge1\),
\[
 57\log P_\beta\le P_\beta^2,
 \quad3\log\chi\le3\chi\le P_\beta^2\chi,
 \quad\log u\le u\le P_\beta^2\chi u.
\]
Taking logarithms in the prefactors of (16)--(17) therefore proves
\[
 q_{\rm abs}\le e^{P_\beta^{31}\chi u},
\]
\[
 \|f_{n,q}-f_n\|_*
 \le\frac{Y e^{P_\beta^{31}\chi u}\sqrt{\log(eq)}}{q^2}
 \quad(q\ge q_{\rm abs}).                              \tag{18}
\]
Finally \(B=P_\beta^{100}\chi^4\) satisfies
\(P_\beta^{31}\chi\le B/8\). Equations (16)--(18) prove the
fixed-order implication (6), including its absorption condition.

## 5. Inverting the envelope without an additional width threshold

The expression inside the ceiling in (4) is at least one, so
\[
 n^{1/4}e^{Bu}\le q_n\le2n^{1/4}e^{Bu}.
\]
In particular \(q_n\ge e^{Bu}\ge q_{\rm abs}\). Also
\[
 \log(eq_n)\le1+\log2+\tfrac14\log n+Bu
                    \le2Bu^2,                         \tag{19}
\]
using \(u\ge1\), \(\log n\le u^2\), and \(B\ge3\).
Substitution into (6) gives
\[
 \|f_{n,q_n}-f_n\|_*
 \le\frac{Y}{\sqrt n}\sqrt{2B}\,u\,e^{-15Bu/8}
 \le\frac{Y}{\sqrt n}.                                \tag{20}
\]
For the last inequality, \(u\mapsto u e^{-Bu}\) is decreasing on
\([1,\infty)\) when \(B\ge1\), and
\(\sqrt{2B}e^{-B}\le1\); the remaining exponential is at most one.
This proves (5) for every width on which the original event bounds hold.

For fixed problem parameters, \(B\) is independent of \(n,q,t\), and
\[
 \frac{\log q_n}{\log n}\longrightarrow\frac14,
 \qquad q_n/n\longrightarrow0.
\]
The moving state has exactly
\[
 2(L-1)mnq_n+n(d+1)+1=n^{5/4+o(1)}
\]
coordinates. The fixed mixers still contribute \((L-1)n^2\) stored
entries. The asymptotic relation \(q_n=o(n)\) is not a claim that
\(q_n<n\) at every finite width.

When \(Y=0\), both systems are stationary with identically zero
predictor, so the comparison is exact and no division by \(Y\) is used.

## 6. Dependencies and probability qualification

The algebra uses the current study's
`GENERAL_EXPLICIT_FITTING.md`,
`GENERAL_EXPLICIT_CLOSURE_FITTING.md`, and
`EXPLICIT_LEGENDRE_COMPARISON.md`.
The bounds (2) on the source recurrence are explicit dependencies for
the coordinator's separate check. The common event and its all-time
carrier estimate are inherited from the source theorem, not established
by the present calculation.

At each fixed confidence, the combined theorem holds at every sufficiently
large individual width. The initialization threshold is explicit in the
dense fitting note; the source's stochastic threshold remains implicit.
There is one event per width for all the orders covered by (6), without
a union bound over orders. No simultaneous event for infinitely many
independently initialized widths is asserted.
