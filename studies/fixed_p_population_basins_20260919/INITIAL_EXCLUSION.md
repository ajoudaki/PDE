# Canonical initial descent excludes all loss-one limits at order two

Status: complete internally checked theoretical argument; frozen scoped report.
This is not promoted canonical theory or an independent review. No numerical
experiment or approximation of Gaussian expectations is used.

## Scope and conclusion

The scientific inputs are only the complete sections C.4.7.10.B,
C.4.7.10.C.1, and C.4.7.10.D.3 of `docs/global_nonlinear.md`, specifically
the assigned ranges 13161–13786 and 15146–15528. The model is their exact
population closure at order \(p=N=2\), with its prescribed ridge
\(\eta=\eta_2=1/9216\), complete correlated Gaussian initialization,
unhalved probability-weighted square loss, and physical gradient-flow time.
The statement is about this fixed closure, not an interchange of closure,
width, particle, precision, or long-time limits.

Let
\[
 \mu=\sum_{i=1}^m\omega_i\delta_{(u_i,y_i)},\qquad
 u_i\in S^1,\quad y_i\in\{-1,1\},\quad
 \omega_i>0,\quad\sum_i\omega_i=1.
\]
Assume compatibility: identical inputs have identical labels, and antipodal
inputs, when both occur, have opposite labels. Start at the canonical state
\(w=g,c=0,M=D\). Then
\[
 \mathcal L'(0)
 =-4\left\|\sum_i\omega_i y_iH_0(u_i)\right\|_{L^2(\Omega_2)}^2<0.
 \tag{1}
\]
Consequently \(\mathcal L(t)<1\) for every \(t>0\), and no zero-predictor
state can be a long-time limit in the topology of the finitely many training
predictions. In particular, no loss-one stationary state is a strong state
limit of this canonical trajectory. This excludes all such stationary states
at once, independently of their local Hessians or ambient basin measures.
It does not exclude positive-loss stationary limits with loss strictly below
one, and does not prove convergence to a global minimizer.

The substantive step is proved below: the initialized upper functions
\(H_0(u)\) are linearly independent after identifying \(u\) and \(-u\).
The proof retains the response term in \(p_i\), the complete lower Gram,
and the positive ridge throughout.

## 1. Exact reduction to the active odd block

Use the source's constants and Gaussian program:
\[
 v=E\tanh^2G,\qquad
 \tau=E\tanh^2(\sqrt vG),\qquad \alpha=1-\tau,
\]
\[
 g_1,g_2\overset{\mathrm{iid}}\sim N(0,1),\quad
 \zeta_1,\zeta_2\overset{\mathrm{iid}}\sim N(0,\tau),\quad
 p_j=\zeta_j+\alpha\tanh g_j.
 \tag{2}
\]
The lower \(g\) and \(\zeta\) are independent. On the separate upper
population, \(\xi_1,\xi_2\) are independent \(N(0,v)\), and write
\(Z_j=\tanh\xi_j\). The lower odd raw features are exactly
\(h_1,h_2,t_1,t_2\), where \(h_j=\tanh g_j\) and \(t_j=\tanh p_j\).
All remaining order-two features are even under simultaneous reversal of
their population's Gaussian coordinates.

The Gram matrices, their ridged inverses, and the initialized contraction
preserve this parity. The contraction has only an odd-to-odd block, by
(H3.1)/(H3.CS7). Since \(\tanh(g\cdot u)\) is odd under lower reversal,
only the odd block contributes to \(H_0(u)\). Permute the lower odd features
into pairs \((h_1,t_1),(h_2,t_2)\). Define
\[
 \kappa=E[h_1t_1],\quad \nu=E[t_1^2],\quad
 \beta=E[\operatorname{sech}^2p_1],\quad
 R=\begin{pmatrix}v+\eta&\kappa\\\kappa&\nu+\eta\end{pmatrix}.
 \tag{3}
\]
Different coordinate pairs have zero cross Gram entries. The upper odd Gram
is \(\tau I_2\). The initialized contraction row for \(Z_j\), restricted
to its lower pair, is
\[
 q=(\alpha v,\ \alpha\kappa+\tau\beta).
 \tag{4}
\]
Indeed (H3.1) gives its first component as
\(E[\partial_{\xi_j}Z_j]E[h_j^2]=\alpha v\); its second is
\(\alpha E[t_jh_j]+E[Z_j^2]E[\partial_{\zeta_j}t_j]
=\alpha\kappa+\tau\beta\). Cross-coordinate entries vanish by independence
and oddness. In particular the term \(\tau\beta\) is retained.

The inverse-Cholesky implementation has the exact raw-filter identity
\(Q_\ell=S_\ell(G_\ell+\eta I)^{-1}S_\ell^*\). Therefore the initial
upper preactivation is
\[
 b_2^TD a_0(u)
 =Z_1F(u_1)+Z_2F(u_2),
 \qquad H_0(u)=\tanh\big(Z_1F(u_1)+Z_2F(u_2)\big),
 \tag{5}
\]
where the following single-coordinate formula defines \(F\) exactly. Put
\[
 (\ell,r)=qR^{-1},\qquad
 k(h)=E_\zeta\tanh(\zeta+\alpha h),\qquad
 \psi(g)=\ell\tanh g+r k(\tanh g).
 \tag{6}
\]
For independent standard \(G,V\) and \(-1\le s\le1\), set
\[
 F(s)=\frac1{\tau+\eta}
 E\!\left[\psi(G)\tanh\big(sG+\sqrt{1-s^2}V\big)\right].
 \tag{7}
\]
To obtain (5), condition each lower-pair correlation on \(g_j\), and use
\(|u|=1\): the conditional second Gaussian in \(g\cdot u\) has variance
\(1-u_j^2\). The sign of its coefficient is immaterial. No independence
between \(h_j\) and \(t_j\) is introduced.

## 2. A quantitative monotonicity bound that handles either sign of \(\ell\)

The coefficient \(\ell\) need not be assumed nonnegative. We instead prove
directly that \(\psi'(g)>0\) for every real \(g\).

First, for \(a>0\),
\[
 E\tanh^2(\sqrt aG)
 \ge E\frac{aG^2}{1+aG^2}
 \ge\frac{a}{1+3a}.
 \tag{8}
\]
The first inequality follows from \(\sinh^2x\ge x^2\) and
\(\tanh^2x=\sinh^2x/(1+\sinh^2x)\). For the second apply Cauchy–Schwarz
to \(\sqrt{W/(1+W)}\) and \(\sqrt{W(1+W)}\), with \(W=aG^2\), using
\(EW=a\), \(EW^2=3a^2\). Taking \(a=1\), then \(a=v\), gives
\[
 v\ge\tfrac14,\qquad \tau\ge\tfrac17,\qquad 0<\alpha\le\tfrac67.
 \tag{9}
\]

For \(-1\le h\le1\), define
\[
 b(h)=E_\zeta\operatorname{sech}^2(\zeta+\alpha h),\qquad
 b^*=b(0),\qquad b_* =\inf_{|h|\le1}b(h).
\]
Convolution with a centered Gaussian preserves the fact that
\(\operatorname{sech}^2\) is even and nonincreasing on the positive half-line,
so \(b(h)\le b^*\). Here is a direct proof of this particular fact.
Write \(\operatorname{sech}^2x=\int_0^1
1_{\{|x|<\operatorname{artanh}\sqrt{1-t}\}}\,dt\).
For each symmetric interval \((-R,R)\), the probability
\(P(|\zeta+a|<R)\) is even in \(a\) and nonincreasing for \(a\ge0\):
its derivative is
\(\tau^{-1/2}[\varphi((R+a)/\sqrt\tau)
-\varphi((R-a)/\sqrt\tau)]\le0\), where \(\varphi\) is the standard
normal density. Integrating this inequality proves the assertion.

The tanh addition formula also gives, for real \(z,a\),
\[
 \frac{\operatorname{sech}^2(z+a)+\operatorname{sech}^2(z-a)}2
 =\operatorname{sech}^2z\operatorname{sech}^2a
 \frac{1+\tanh^2z\tanh^2a}{(1-\tanh^2z\tanh^2a)^2}
 \ge\operatorname{sech}^2z\operatorname{sech}^2a.
\]
Gaussian symmetry hence gives
\(b(h)\ge\operatorname{sech}^2(\alpha h)b^*
\ge\operatorname{sech}^2(6/7)b^*\).
For \(t=6/7\), successive nonconstant terms of the cosh series have ratio
at most \(t^2/12\), so
\[
 \cosh(6/7)\le1+\frac{(6/7)^2/2}{1-(6/7)^2/12}
 =\frac{32}{23},\qquad
 b_*\ge\frac{529}{1024}b^*>\frac12b^*.
 \tag{10}
\]
In particular \(\beta=E[b(h_1)]\ge b_*>0\).

Because \(k(0)=0\) and \(k'(h)=\alpha b(h)\),
\[
 0<\kappa=E[h_1k(h_1)]\le\alpha v b^*.
 \tag{11}
\]
For fixed \(h\), integration by parts in \(\zeta\sim N(0,\tau)\) gives
\(E[\zeta\tanh(\zeta+\alpha h)]=\tau b(h)\); boundedness of tanh
justifies the vanishing boundary term. Cauchy–Schwarz then gives
\[
 \operatorname{Var}_\zeta\tanh(\zeta+\alpha h)\ge\tau b(h)^2.
\]
Decompose \(\nu\) by conditioning on \(h_1\), and use
\(\kappa^2\le vE[k(h_1)^2]\). It follows that
\[
 v\nu-\kappa^2
 \ge vE\operatorname{Var}_\zeta\tanh(\zeta+\alpha h_1)
 \ge v\tau E[b(h_1)^2]\ge v\tau\beta^2>0.
 \tag{12}
\]

Let \(\Delta=(v+\eta)(\nu+\eta)-\kappa^2>0\). Formula (6) becomes
\[
 \Delta\ell=\alpha(v\nu-\kappa^2)+\alpha v\eta-\tau\beta\kappa,
 \qquad
 \Delta r=\alpha\kappa\eta+\tau\beta(v+\eta)>0.
 \tag{13}
\]
For every \(|h|\le1\), (10)–(13) imply
\[
\begin{aligned}
 \Delta(\ell+\alpha r b(h))
 &\ge \alpha(v\nu-\kappa^2)-\tau\beta\kappa
                  +\alpha\tau\beta v b_*\\
 &\ge \alpha v\tau\beta(\beta-b^*+b_*)\\
 &\ge \alpha v\tau\beta(2b_*-b^*)>0.
\end{aligned}
 \tag{14}
\]
In the first inequality the terms proportional to the prescribed positive
\(\eta\) were dropped because they are nonnegative, and \(b(h)\) was
replaced by its lower bound \(b_*\). The ridge remains in the actual
coefficients and in \(\Delta\). Thus
\[
 \psi'(g)=\operatorname{sech}^2g
              [\ell+\alpha r b(\tanh g)]>0
 \quad(g\in\mathbb R).
 \tag{15}
\]

The function \(\psi\) is bounded, odd, and has bounded derivative.
For \(-1<s<1\), differentiate (7), then integrate by parts separately
in \(G\) and \(V\). With \(T=sG+\sqrt{1-s^2}V\), the derivative before
integration by parts is
\[
 (\tau+\eta)F'(s)
 =E[\psi(G)\operatorname{sech}^2T
                 (G-sV/\sqrt{1-s^2})].
\]
The two terms involving the derivative of \(\operatorname{sech}^2T\)
cancel: the \(G\) term contributes \(sE[\psi(G)(\operatorname{sech}^2)'(T)]\),
and the \(V\) term its negative. Consequently
\[
 F'(s)=\frac1{\tau+\eta}
 E[\psi'(G)\operatorname{sech}^2T]>0.
 \tag{16}
\]
All differentiations are dominated on each compact subinterval of \((-1,1)\)
by a constant times \(1+|G|+|V|\); all integration-by-parts factors and
their derivatives are bounded. Dominated convergence gives continuity at
\(s=\pm1\). Symmetry gives \(F(-s)=-F(s)\) and \(F(0)=0\).
Thus \(F\) is strictly increasing on the entire closed interval
\([-1,1]\). Strictness involving an endpoint follows by inserting an
intermediate interior point and using continuity.

In particular
\[
 A(u):=(F(u_1),F(u_2))
 \tag{17}
\]
is nonzero on \(S^1\), is injective, and satisfies
\(A(u)=-A(v)\) if and only if \(u=-v\).

## 3. Independence of upper features modulo antipodes

We prove the elementary ridge-function statement needed here. Suppose
\(a_1,\ldots,a_k\in\mathbb R^2\setminus\{0\}\) and
\(a_i\ne\pm a_j\) for \(i\ne j\). Then
\(z\mapsto\tanh(a_j\cdot z)\) are linearly independent on every open
neighborhood of zero.

Choose \(e\in\mathbb R^2\) avoiding the finitely many lines
\(a_j\cdot e=0\) and \((a_i\pm a_j)\cdot e=0\).
Then the numbers \(|a_j\cdot e|\) are positive and distinct.
A putative relation, restricted to \(z=te\) near zero, becomes
\(\sum_j d_j\tanh(\lambda_jt)=0\), with distinct positive \(\lambda_j\),
after incorporating the signs into \(d_j\). Real analyticity extends this
identity to every real \(t\): at an endpoint of an interval of equality,
all derivatives vanish by continuity, and the convergent Taylor series
extends equality to a neighborhood.

Order \(0<\lambda_1<\cdots<\lambda_k\). Taking \(t\to\infty\) first
gives \(\sum_jd_j=0\). Subtract that constant relation and multiply by
\(e^{2\lambda_1t}\). Since
\[
 e^{2\lambda_1t}(\tanh(\lambda_1t)-1)\to-2,
 \qquad
 e^{2\lambda_1t}(\tanh(\lambda_jt)-1)\to0\quad(j>1),
\]
we get \(d_1=0\). Repeating with the remaining terms proves all
coefficients zero.

The upper random vector \(Z=(\tanh\xi_1,\tanh\xi_2)\) has a strictly
positive density on \((-1,1)^2\). A continuous function zero almost surely
under this law is zero on that open square: a point where it were nonzero
would have a neighborhood of positive measure where it stayed nonzero.
Apply the preceding independence result with \(a_j=A(v_j)\), using (17).
For any finite collection of circle directions distinct modulo antipodes,
\[
 H_0(v_1),\ldots,H_0(v_k)
 \quad\text{are linearly independent in }L^2(\Omega_2).
 \tag{18}
\]
This proves the required kernel nondegeneracy from the full initialized
Gaussian program, rather than assuming it as a generic kernel property.

## 4. Exact initial-descent criterion and energy exclusion

Choose one representative \(v_j\) for each input class modulo antipodes,
and write \(u_i=\sigma_i v_j\), \(\sigma_i\in\{-1,1\}\), in that class.
Since \(H_0(-u)=-H_0(u)\),
\[
 \sum_i\omega_i y_iH_0(u_i)
 =\sum_j\gamma_jH_0(v_j),\qquad
 \gamma_j=\sum_{i:u_i=\pm v_j}\omega_i y_i\sigma_i.
 \tag{19}
\]
By (18), this function vanishes if and only if every \(\gamma_j=0\).
Thus, even without compatibility, the exact condition for strict initial
descent is that at least one of these signed class sums be nonzero.
Under compatibility, all \(y_i\sigma_i\) within one class equal a common
\(\varepsilon_j\in\{-1,1\}\), and
\(\gamma_j=\varepsilon_j\sum_{i\text{ in class }j}\omega_i\ne0\).

At initialization, \(c=0\) implies \(d=q=0\), hence
\(w'(0)=M'(0)=0\) and
\(c'(0)=2\sum_i\omega_i y_iH_0(u_i)\). Differentiating the loss in its
actual population/Frobenius metric gives (1). If
\(Q=\|\sum_i\omega_i y_iH_0(u_i)\|_2^2>0\), then
\[
 \mathcal L(t)=1-4Qt+o(t).
 \tag{20}
\]

For completeness, fixed-order global existence needed for the long-time
exclusion is available for these arbitrary finite data, without the
small-arc hypothesis of the order-to-infinity approximation theorem.
In the characteristic variables \((w-g,c,M)\), the fixed features are
bounded and the vector field is locally Lipschitz on bounded supremum-norm
balls. The gradient identity gives \(\mathcal L(t)\le1\) locally, so
\(\int|r|\,d\mu\le1\). The raw filter contractions give
\(|a(u)|\le1\), \(|d(u)|\le\|c\|_2\), and therefore
\[
 \|c(t)\|_\infty\le2t,\qquad
 \|M(t)-D\|_F\le2t^2,
\]
\[
 \|w'(t)\|_\infty
 \le4t\|b_1\|_{L^\infty(\ell^2)}(\|D\|_{\rm op}+2t^2).
 \tag{21}
\]
These are finite on every bounded time interval, as are the speeds in the
local existence norm. Thus Cauchy endpoints and local continuation give a
unique solution on every finite interval. This repeats the fixed-order
continuation argument of D.3 using only \(|u|=|y|=1\), and does not assert
an all-time neural-width or closure-order approximation.

The energy identity is
\[
 \mathcal L'(t)=-\|w'(t)\|_2^2-\|c'(t)\|_2^2-\|M'(t)\|_F^2\le0.
 \tag{22}
\]
Combining (20) and (22) yields \(\mathcal L(t)<1\) for every positive
time. Fix one \(t_*>0\), and put \(\delta=1-\mathcal L(t_*)>0\).
For all \(t\ge t_*\),
\[
 \mathcal L(t)\le1-\delta,\qquad
 \|f(t,\cdot)\|_{L^2(\mu)}\ge1-\sqrt{1-\delta}>0.
 \tag{23}
\]
The second inequality is the triangle inequality applied to
\(y=(y-f)+f\), using \(\|y\|_2=1\). Hence there is not even a sequence
of times tending to infinity along which all training predictions tend to
zero. Any state convergence making the finite training predictions continuous
inherits this exclusion. In particular, strong \(L^2\) convergence of
\(w,c\) together with matrix convergence of \(M\) does: bounded features
and the Lipschitz property of tanh give continuity of \(a,H\), and then
of \(f=E[cH]\). More generally no prediction limit with loss one is possible.

## 5. Invariant symmetry and limits of the conclusion

The canonical order-two trajectory stays in the closed parity subsystem
\[
 w\circ S_1=-w,\qquad c\circ S_2=-c,\qquad
 M\text{ supported on the odd-to-odd block},
\]
where \(S_1(g,\zeta)=(-g,-\zeta)\) and \(S_2\xi=-\xi\).
At such a state, \(h,q,w'\) are odd in lower marks, \(H,c'\) are odd
in upper marks, \(a,d\) have only odd coordinates, and \(M'\) has only
the odd block. The local uniqueness and continuation just used therefore
preserve this subsystem, as in C.1. This is compatible with the active-block
calculation above and uses the actual order-two ridge, not the order-one
ridge.

An ambient measure-zero basin theorem alone would not exclude the canonical
initial condition: the whole initialized trajectory lies in this invariant
subspace. The exclusion established here instead uses a strict and permanent
energy gap. Conversely, this energy argument leaves all stationary states
of loss below one, including possible stationary states inside the parity
subsystem, unresolved. It gives neither a basin-size theorem for them nor
an eventual vanishing of the training error.

Adversarial checks discharged by the proof: the reverse-source response is
included in (2)/(4); no lower correlations are discarded; \(\eta_2\) stays
in (3), (5)–(7), and (13); feature independence is proved in (18); same and
antipodal duplicates are treated exactly by (19); the long-time statement
uses only fixed-order continuation and energy, without exchanging limits.
No claim is made for finite asymmetric particle rules, which need not retain
the exact Gaussian parity or the independence result.
