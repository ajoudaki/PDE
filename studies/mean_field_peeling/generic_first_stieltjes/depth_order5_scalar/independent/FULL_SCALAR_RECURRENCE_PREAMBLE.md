# Arbitrary fixed depth, B=1, through order five: deterministic scalar recurrence

**Status.**  This is an independently derived, fully contracted deterministic
recurrence; all local Gaussian coordinates have been Wick--Stein eliminated.
The transition equations were frozen under manifest SHA-256
`0699148b5d5fcd77a821908f333e230e36e148afad710e2421c36ab89c7441f8`
before any accepted-map or Route-S comparison.  Exact rational expansion gives
zero discrepancies against the frozen accepted maps at \(H=2,3,4\), including
all \(17{,}641\) monomials of \(C_4\).

The result is a fixed-dimensional \(M\)-only recurrence, but it is **not** a
single forward sweep followed by a single backward sweep: it uses the six
chronological passes F1/R1/F2/R2/F3/R3 displayed below.  Thus it satisfies the
Gaussian-elimination and arbitrary-fixed-depth obligations, while remaining
an exact multi-pass alternative to the stricter two-sweep schematic in the
request.  Section 9 records the dependency that prevents this realization
from being reordered into one forward/backward pair; no universal minimality
or no-go claim is made.

No Hermite or polynomial approximation of the activation is used.

## 1. Alphabet and deterministic depth data

Let

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}\prod_{r=0}^{5}
 \phi^{(r)}(G)^{\nu_r},\qquad M_{200000}=1,
\]

and put

\[
d=M_{020000},\qquad b_\ell=d^{H-\ell},\qquad
\tau_\ell=\sum_{r=0}^{\ell}d^r.
\tag{1.1}
\]

Every symbol below is a deterministic scalar.  Superscript `+` in an
appendix means the next layer in a bottom-up pass or the next lower layer in
a top-down pass.  Products and powers are ordinary commutative scalar
operations.

The construction uses three bottom-up passes of dimensions 7, 4, and 3 and
three top-down passes of dimensions 8, 4, and 3.  Equivalently, its aggregate
staged state dimensions are 14 forward scalars and 15 reverse scalars.  There
are five terminal folds: the lower-order fold \(\mathcal H\), and the four
order-five folds \(AC,Bm2,M2,Am3\).  The passes are chronological and their
states need not be live simultaneously.  This is the smallest state found by
this route; no mathematical minimality claim is made.

For an implementation that avoids recomputation, the exact census is

| pass | propagated scalars | cached layer outputs | emitted source scalars | terminal folds |
|---|---:|---:|---:|---:|
| F1 | 7 | 7 | 0 | 0 |
| R1 | 8 | 8 | 5 | 2 |
| F2 | 4 | 4 | 0 | 0 |
| R2 | 4 | 4 | 3 | 2 |
| F3 | 3 | 3 | 0 | 0 |
| R3 | 3 | 0 (streamable) | 1 (streamable) | 1 |

Thus the literal cached schedule has 14 forward-state and 12 reverse-state
scalars per layer, eight retained source scalars per layer, one streamable
source, and five scalar folds.  Recomputing sources trades storage for time
without changing the recurrence.

## 2. Pass F1: frozen forward jet (dimension 7)

Write

\[
f_\ell=(u_\ell,v_\ell,w_\ell,x_\ell,y_\ell,j_\ell,k_\ell).
\]

Initialize

\[
\begin{aligned}
u_1&=b_1M_{121000},&v_1&=3b_1^2M_{140010},
&w_1&=b_1M_{040000},\\
x_1&=3b_1^2M_{050100},&y_1&=3b_1^2M_{042000},
&j_1&=3b_1M_{030100},\\
k_1&=15b_1^2M_{050001}.&&
\end{aligned}
\tag{2.1}
\]

For $2\le\ell\le H$, substitute

\[
b=b_\ell,\quad l1=\tau_{\ell-1},\quad
l3=j_{\ell-1}+3u_{\ell-1},\quad
l5=k_{\ell-1}+5v_{\ell-1}
\tag{2.2}
\]

and the prior seven state values into the seven explicit equations in
Appendix A.

The straight frozen derivatives needed later are

\[
S_{3,H}=j_H+3u_H,\qquad S_{5,H}=k_H+5v_H.
\tag{2.3}
\]

The projection $(w,u,j)$ is exactly the previously audited order-three
$(V,M,J)$ recurrence.

## 3. Pass R1: frozen gradient jet (dimension 8)

The top state is

\[
(e02,e11,e13,e22,c10,c21,c30,c32)_H=(0,0,0,0,1,0,0,0).
\tag{3.1}
\]

For $\ell=H,H-1,\ldots,1$, use

\[
b=b_\ell,\quad l1=\tau_{\ell-1},\quad
l3=j_{\ell-1}+3u_{\ell-1},
\tag{3.2}
\]

with $f_0=0$, and evaluate Appendix B.  Store the five scalars

\[
(s00,s02,s11,s13,s22)_\ell
=(source00,source02,source11,source13,source22)_\ell,
\tag{3.3}
\]

then pass the eight `*_next` values to layer $\ell-1$.

Two terminal sums are already available.  Initialize

\[
AC=x_H,\qquad \mathcal H=w_H.
\]

At $\ell\ge2$, add

\[
\begin{aligned}
AC&\mathrel{+}=s13_\ell+3s11_\ell u_{\ell-1}
 +3s02_\ell w_{\ell-1}+s00_\ell x_{\ell-1},\\
\mathcal H&\mathrel{+}=s11_\ell+s00_\ell w_{\ell-1};
\end{aligned}
\tag{3.4}
\]

at $\ell=1$, add $s13_1$ and $s11_1$, respectively.  Then

\[
AC=\langle Hp,U[p,p,p]\rangle,\qquad
B_H=2S_{3,H}+4\mathcal H.
\tag{3.5}
\]

## 4. Pass F2: moving feature derivative two (dimension 4)

Set

\[
(q02,q22,qfm,a2)_0=(0,0,0,0).
\tag{4.1}
\]

For $\ell=1,\ldots,H$, use the stored $f_{\ell-1}$, the current R1
state at layer $\ell$, the prior F2 state, and

\[
b=b_\ell,\qquad l1=\tau_{\ell-1},\qquad l2=1+a2_{\ell-1}.
\tag{4.2}
\]

The four equations in Appendix C, group `feature2`, define the next F2
state.

## 5. Pass R2: moving gradient derivative two (dimension 4)

Initialize at the top

\[
(r02,r22,rfm,d21)_H=(0,0,0,1).
\tag{5.1}
\]

For $\ell=H,\ldots,1$, use (4.2), the stored F1/R1/F2 states, and the
current R2 state in Appendix C, group `gradient2`.  Store

\[
(t02,t22,tfm)_\ell
=(source02m,source22m,sourcefm)_\ell,
\tag{5.2}
\]

and propagate the four `*_next` values downward.

Initialize

\[
Bm2=qfm_H,\qquad M2=q22_H.
\]

For $\ell\ge2$, add

\[
\begin{aligned}
Bm2\mathrel{+}={}&tfm_\ell+s02_\ell q02_{\ell-1}
 +t02_\ell u_{\ell-1}+4s11_\ell w_{\ell-1}
 +s00_\ell qfm_{\ell-1},\\
M2\mathrel{+}={}&t22_\ell+2t02_\ell q02_{\ell-1}
 +4s11_\ell w_{\ell-1}+s00_\ell q22_{\ell-1}.
\end{aligned}
\tag{5.3}
\]

At $\ell=1$, add $tfm_1$ and $t22_1$.  The terminal meanings are

\[
Bm2=\langle T[p,p],D^2p\rangle,\qquad M2=\|D^2p\|^2.
\tag{5.4}
\]

## 6. Pass F3: moving feature derivative three (dimension 3)

Set

\[
(q13,a30,a32)_0=(0,0,0).
\tag{6.1}
\]

For $\ell=1,\ldots,H$, use all stored lower-order states and

\[
\begin{aligned}
l2&=1+a2_{\ell-1},\\
l30&=4q02_{\ell-1}+3w_{\ell-1}+a30_{\ell-1},\\
l32&=1+a32_{\ell-1}.
\end{aligned}
\tag{6.2}
\]

The three equations in Appendix C, group `feature3`, define the next state.

## 7. Pass R3: moving gradient derivative three (dimension 3)

Initialize

\[
(r13,d30,d32)_H=(0,0,1).
\tag{7.1}
\]

For $\ell=H,\ldots,1$, use (6.2) and all stored lower-order states in
Appendix C, group `gradient3`.  Store

\[
z13_\ell=source13m_\ell
\tag{7.2}
\]

and propagate `(r13_next,d30_next,d32_next)` downward.

Initialize $Am3=q13_H$.  For $\ell\ge2$, add

\[
Am3\mathrel{+}=z13_\ell+3s11_\ell q02_{\ell-1}
 +3t02_\ell w_{\ell-1}+s00_\ell q13_{\ell-1};
\tag{7.3}
\]

at $\ell=1$, add $z13_1$.  Then

\[
Am3=\langle Hp,D^3p\rangle.
\tag{7.4}
\]

## 8. Terminal coefficients

Here is the finite-width tensor audit before any large-width limit.  If
\(\theta\) denotes the original parameter vector, set
\(\widetilde\nabla=\sqrt n\,\nabla_\theta\).  Then, exactly at finite width,
\(p=\widetilde\nabla f_n\) and
\(D_n=p\mathbin\cdot\widetilde\nabla\).  In these rescaled coordinates put

\[
H=\widetilde\nabla^2f_n,\quad T=\widetilde\nabla^3f_n,
\quad U=\widetilde\nabla^4f_n,\quad V=\widetilde\nabla^5f_n,
\quad A=Hp,\quad B=T[p,p],\quad c=H^2p.
\]

Repeated ordinary product differentiation gives

\[
\begin{aligned}
D_nf_n&=\langle p,p\rangle,\\
D_n^2f_n&=2H[p,p],\\
D_n^3f_n&=2T[p,p,p]+4\langle A,A\rangle,\\
D_n^4f_n&=2U[p,p,p,p]+14T[A,p,p]+8\langle A,c\rangle.
\end{aligned}
\tag{8.1}
\]

Differentiating the last line once more, and only collecting equal tensor
contractions after differentiation, gives all six families

\[
\boxed{\begin{aligned}
D_n^5f_n={}&2V[p,p,p,p,p]+22U[A,p,p,p]+14\langle B,B\rangle\\
&+30\langle B,c\rangle+36T[A,A,p]+16\langle c,c\rangle .
\end{aligned}}
\tag{8.2}
\]

For an independent coefficient check, define
\(m_2=D_n^2p=B+c\).  Direct differentiation gives

\[
m_3=D_nm_2=U[p,p,p]+3T[A,p]+Hm_2
\]

and therefore

\[
\langle A,m_3\rangle
=U[A,p,p,p]+3T[A,A,p]+\langle B,c\rangle+\langle c,c\rangle.
\tag{8.3}
\]

Substitution into the independently grouped identity

\[
D_n^5f_n=2V[p^5]+10\langle Hp,U[p^3]\rangle
 +10\langle T[p,p],D^2p\rangle+4\|D^2p\|^2
 +12\langle Hp,D^3p\rangle
\tag{8.4}
\]

reproduces the coefficient vector
\((2,22,14,30,36,16)\) in (8.2) exactly.  This is the exact finite-width
product-rule audit.  The subsequent equality-partition, width-counting,
transpose-response, and Wick--Stein audit is displayed in Section 12 and is
then checked by two exact canonicalizations.

The fully contracted scalar answer is

\[
\boxed{
A_H=\tau_H,\qquad
B_H=2S_{3,H}+4\mathcal H,\qquad
C_H=2S_{5,H}+10AC+10Bm2+4M2+12Am3.}
\tag{8.5}
\]

Finally,

\[
\boxed{
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}.}
\tag{8.6}
\]

No Gaussian variable or expectation other than a declared one-dimensional
\(M_\nu\) atom remains in (8.5) or in any transition appendix.

## 9. Why six passes appear

Order three closes after one frozen forward and one differentiated reverse
pass.  At order five, $D^2p=T[p,p]+H^2p$.  The feature tangent in the
secondary direction $Hp$ depends on the first differentiated reverse
carrier, so it is not available during the initial bottom-up pass.  The
chronological resolution is exactly F2/R2, followed by F3/R3.  This proves a
dependency obstruction for collapsing *this realization* to one forward and
one backward pass; it is not a no-go theorem for a different algebraic state.

## 10. Parity, derivative ceiling, and annealed limit

Readout reflection gives exact finite-width parity

\[
\mathbb E f_n=\mathbb E D_n^2f_n=\mathbb E D_n^4f_n=0.
\]

The local Bell polynomials use activation derivatives only through order
five.  Each inverse-free Wick--Stein step differentiates only when pairing an
even forward innovation with the base activation argument.  The construction
raises an exception if this would create $\phi^{(6)}$, and an independent
terminal atom scan over all three frozen transition tables finds maximal
derivative index five.  Hence every terminal atom is $M_{\nu_0\ldots\nu_5}$.

For theorem-level annealed identification, depth \(H\) and batch size one are
held fixed while every hidden width tends to infinity (here all widths are
the common \(n\)); the deterministic input is normalized as assumed by the
forward-Gram construction.  A precise sufficient activation package is

\[
\phi\in C^5(\mathbb R),\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r}),\quad 0\le r\le5,
\tag{10.1}
\]

together with the standard finite tensor-program law of large numbers for
the resulting finite list of coordinates.  To pass from convergence in
probability to the annealed coefficients one additionally needs, for some
\(\epsilon>0\),

\[
\sup_n\mathbb E|D_n^k f_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\}.
\tag{10.2}
\]

Condition (10.2) is exactly the uniform-integrability bridge used here.  It
follows, for example, from a uniform \(L^{1+\epsilon}\) moment bound proved for
the finite tensor program under (10.1); it is not silently inferred from
pointwise convergence.  The stronger convenient assumption
\(\phi\in C^\infty\) with every derivative of polynomial growth also suffices.
No statement is made for \(H=H(n)\), uniform depth bounds, or fixed positive
flow time.

## 11. Exact and empirical controls

The following are exact substitutions into the shared unit-Gram recurrence.
The constant row holds at every depth; the remaining entries are shown at the
three frozen audit depths.

| activation | \(H\) | \(A_H\) | \(B_H\) | \(C_H\) |
|---|---:|---:|---:|---:|
| \(1\) | any | \(1\) | \(0\) | \(0\) |
| \(x\) | 2 | \(3\) | \(48\) | \(1464\) |
| \(x\) | 3 | \(4\) | \(160\) | \(13888\) |
| \(x\) | 4 | \(5\) | \(400\) | \(73240\) |
| \((1+x)/\sqrt2\) | 2 | \(7/4\) | \(31/4\) | \(615/8\) |
| \((1+x)/\sqrt2\) | 3 | \(15/8\) | \(12\) | \(13447/64\) |
| \((1+x)/\sqrt2\) | 4 | \(31/16\) | \(479/32\) | \(179193/512\) |
| \(x^2/\sqrt3\) | 2 | \(37/9\) | \(561728/243\) | \(25800211040/6561\) |
| \(x^2/\sqrt3\) | 3 | \(175/27\) | \(191282624/6561\) | \(655126467433760/1594323\) |
| \(x^2/\sqrt3\) | 4 | \(781/81\) | \(51094842176/177147\) | \(10678160325919415648/387420489\) |

The canonical **unnormalized** quadratic \(\phi(x)=x^2\) does not remain on
\(Q^\ell=1\): its forward Gram chain begins
\(1,3,27,2187,14348907\).  Its accepted controls therefore come from the
separate layer-tagged arbitrary-Gram recurrence, not by substituting moments
into the unit quotient above:

| \(H\) | \(A_H\) | \(B_H\) | \(C_H\) |
|---:|---:|---:|---:|
| 2 | \(111\) | \(1685184\) | \(77400633120\) |
| 3 | \(14175\) | \(139445032896\) | \(4298284752832899360\) |
| 4 | \(138351807\) | \(59385566223611232192\) | \(81427352525619060193821492876576\) |

In particular the companion arbitrary-Gram calculation at \(H=2\) gives
\(\mu_0=280864/4107\) and
\(\mu_1=38443196932/5616860517\), as required.  Extending the present compact
unit-Gram scalar recurrence itself to layer-dependent Grams remains a
separate obligation.

The smooth nonpolynomial regression gate used
\(\phi(x)=\sin(x)/\sqrt{(1-e^{-2})/2}\) and 7,700 independently initialized
finite-width networks.  The preregistered extrapolation results were

| \(H\) | population \(C_H\) | fitted intercept | standard error | \(z\) | \(p_{\chi^2}\) |
|---:|---:|---:|---:|---:|---:|
| 3 | \(1076854.4594\) | \(1276231.4160\) | \(166117.4278\) | \(1.2002\) | \(0.4026\) |
| 4 | \(19488618.5248\) | \(21151695.3853\) | \(3501920.1951\) | \(0.4749\) | \(0.3647\) |

Both registered gates pass.  This is empirical finite-width evidence, not a
proof; it transfers to this recurrence only after the exact map equality in
the next section.

## 12. Exact coefficient audit and claim levels

For completeness, the equality-partition and transpose-response registry used
before taking the width limit is as follows.  At one reused hidden matrix let
\(h_k\) and \(b_k\) denote the order-\(k\) forward and backward Taylor
coefficients, let \(A_0\) be the initialized Gaussian matrix, and let
\(A_m\) be its order-\(m\) rank-one flow update.  With fresh forward and
reverse Gaussians \(F_k,R_k\), put
\(H_{kq}=\mathbb E[h_kh_q]\) and
\(B_{kq}=\mathbb E[b_kb_q]\).  The six exhaustive leading cases are

| occurrence | leading equality family |
|---|---|
| \(A_0h_k\) | fresh forward pairing \(F_k\) |
| \(A_0h_k\) | one earlier transpose response \(\sum_{s<k}b_s\alpha_{ks}\) |
| \(A_mh_{k-m}\) | \(m^{-1}\sum_{p+q=m-1}b_pH_{q,k-m}\) |
| \(A_0^Tb_k\) | fresh reverse pairing \(R_k\) |
| \(A_0^Tb_k\) | one current-or-earlier forward response \(\sum_{s\le k}h_s\beta_{ks}\) |
| \(A_m^Tb_{k-m}\) | \(m^{-1}\sum_{p+q=m-1}h_qB_{p,k-m}\) |

Here

\[
\alpha_{ks}=\mathbb E\,\partial_{R_s}h_k,
\qquad
\beta_{ks}=\mathbb E\,\partial_{F_s}b_k.
\tag{12.1}
\]

The strict ranges \(s<k\) and \(s\le k\) are the transpose-response audit:
the feature jet cannot depend on the current reverse innovation, while the
backward jet already depends on the current forward innovation.  Each
initialized matrix entry costs \(n^{-1/2}\), each free neuron index supplies
\(n\), and each explicit update entry costs \(n^{-1}\).  The six rows above
have net width power zero.  Any additional equality removes a free index
without restoring a matrix-pair factor and is \(o(1)\); nested leading
responses are retained by recursively applying the same six rows.  This
exhausts the leading equality partitions at every fixed chronological order.

After this census, reverse innovations are eliminated by Isserlis pairing.
For a forward innovation correlated with the activation argument, the
inverse-free Wick--Stein step is

\[
\begin{aligned}
\mathbb E\!\left[F_i\prod_{j\ge1}F_j^{m_j}\Psi(F_0)\right]
={}&\sum_{j\ge1}m_j\,\mathbb E[F_iF_j]\,
 \mathbb E\!\left[F_j^{m_j-1}
 \prod_{q\ne j}F_q^{m_q}\Psi(F_0)\right]\\
&+\mathbb E[F_iF_0],
 \mathbb E\!\left[\prod_{j\ge1}F_j^{m_j}\Psi'(F_0)\right].
\end{aligned}
\tag{12.2}
\]

Every application lowers the auxiliary-Gaussian degree, so the reduction
terminates without a covariance inverse.  Appendices A--C are the result after
all such steps and after the response derivatives in (12.1) have been
contracted into scalar states.

There are two independent canonicalization routes.  The frozen reference
maps first enumerate the six-row registry and then apply (12.2).  Route A was
frozen without inspecting those formulas: it contracts typed local polynomial
chaos directly and canonicalizes every result as a sorted multiset of
one-dimensional \(M_\nu\) atoms with a rational coefficient.  The independently
frozen assembler then expanded (8.5) and compared those canonical atom
multisets coefficient by coefficient:

| \(H\) | \(\#A\) | discrepancies | \(\#B\) | discrepancies | \(\#C\) | discrepancies |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 0 | 46 | 0 | 974 | 0 |
| 3 | 4 | 0 | 160 | 0 | 6519 | 0 |
| 4 | 5 | 0 | 350 | 0 | 17641 | 0 |

A second post-freeze implementation compared all eight exported roots
\(A,B,C,S5,AC,Bm2,M2,Am3\) through \(H=4\) and also found zero discrepancies.
The transition-table derivative scan has no residual symbol, no multivariate
Gaussian atom, and maximal activation-derivative index five.

The resulting claim ledger is:

| level | statement | status |
|---|---|---|
| exact finite width | product-rule identities (8.1)--(8.4), including all six contraction families and parity | proved algebraically |
| formal normal form | Appendices A--C after local Wick--Stein elimination | explicit finite polynomial tables |
| algebraically audited normal form | exact canonical comparison at \(H=2,3,4\), lower-order projection, controls, derivative scan | passed |
| theorem-level width limit | \(A_H,B_H,C_H\) equal the annealed limits | conditional on the fixed-depth tensor-program convergence and UI hypotheses (10.1)--(10.2) |

Thus no positive-time or depth-uniform theorem is being inferred from the
coefficient audit.
