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

# Appendix A: frozen forward transition

### `j_next`

```text
j_next = 3*M002000*l1*u + 3*M010100*l1*u + 3*M010100*l1*w + M020000*l3 + 3*M030100*b*l1^3
```

### `k_next`

```text
k_next = 15*M000200*l1*u^2 + 30*M001010*l1*u^2 + 30*M001010*l1*u*w + 5*M002000*l1*v + 10*M002000*l3*u + 15*M010001*l1*u^2 + 30*M010001*l1*u*w + 15*M010001*l1*w^2 + 5*M010100*l1*v + 20*M010100*l1*x + 15*M010100*l1*y + 10*M010100*l3*u + 10*M010100*l3*w + M020000*l5 + 90*M021010*b*l1^3*u + 30*M030001*b*l1^3*u + 30*M030001*b*l1^3*w + 30*M030100*b*l1^2*l3 + 15*M050001*b^2*l1^5
```

### `u_next`

```text
u_next = M020000*u + M101000*u + M101000*w + M121000*b*l1^2
```

### `v_next`

```text
v_next = 3*M002000*u^2 + 6*M010100*u^2 + 6*M010100*u*w + M020000*v + 6*M030100*b*l1^2*u + 3*M100010*u^2 + 6*M100010*u*w + 3*M100010*w^2 + M101000*v + 4*M101000*x + 3*M101000*y + 12*M111100*b*l1^2*u + 6*M120010*b*l1^2*u + 6*M120010*b*l1^2*w + 4*M121000*b*l1*l3 + 3*M140010*b^2*l1^4
```

### `w_next`

```text
w_next = M020000*w + M040000*b*l1^2
```

### `x_next`

```text
x_next = 3*M002000*u*w + 3*M010100*u*w + 3*M010100*w^2 + M020000*x + 9*M022000*b*l1^2*u + 3*M030100*b*l1^2*u + 6*M030100*b*l1^2*w + M040000*b*l1*l3 + 3*M050100*b^2*l1^4
```

### `y_next`

```text
y_next = 2*M002000*u^2 + 2*M002000*u*w + 3*M002000*w^2 + 2*M010100*u^2 + 2*M010100*u*w + M020000*y + 6*M022000*b*l1^2*u + 6*M022000*b*l1^2*w + 2*M030100*b*l1^2*u + 3*M042000*b^2*l1^4
```

# Appendix B: frozen reverse transition

### `c10_next`

```text
c10_next = M002000*b*l1 + M010100*b*l1 + M020000*b + M020000*c10 + M101000*c10
```

### `c21_next`

```text
c21_next = 2*M010100*b*l1 + M020000*c21 + 2*M101000*c10
```

### `c30_next`

```text
c30_next = 3*M000200*b*l1*u + 6*M001010*b*l1*u + 3*M001010*b*l1*w + M002000*b*l3 + 3*M002000*b*u + 3*M002000*c10*u + 3*M002000*c21*w + 2*M002000*c32*u + M002000*c32*w + 3*M002000*e02*l1 + 3*M010001*b*l1*u + 3*M010001*b*l1*w + M010100*b*l3 + 3*M010100*b*u + 3*M010100*b*w + 6*M010100*c10*u + 3*M010100*c10*w + 3*M010100*c21*w + 2*M010100*c32*u + M010100*c32*w + 3*M010100*e02*l1 + M020000*c30 + 3*M020000*e02 + 9*M021010*b^2*l1^3 + 9*M022000*b*c21*l1^2 + 3*M022000*b*c32*l1^2 + 3*M030001*b^2*l1^3 + 9*M030100*b^2*l1^2 + 3*M030100*b*c10*l1^2 + 3*M030100*b*c21*l1^2 + M030100*b*c32*l1^2 + 3*M040000*b*c21*l1 + 3*M100010*c10*u + 3*M100010*c10*w + M101000*c30 + 6*M111100*b*c10*l1^2 + 3*M120010*b*c10*l1^2 + 6*M121000*b*c10*l1
```

### `c32_next`

```text
c32_next = 3*M010100*b*l1 + M020000*c32 + 3*M101000*c10
```

### `e02_next`

```text
e02_next = M002000*b*u + M010100*b*u + M010100*b*w + M020000*e02 + 3*M030100*b^2*l1^2 + M040000*b*c21*l1 + 2*M121000*b*c10*l1
```

### `e11_next`

```text
e11_next = M002000*b*w + M020000*e11 + 3*M022000*b^2*l1^2 + 2*M121000*b*c10*l1 + M220000*c10^2
```

### `e13_next`

```text
e13_next = 3*M000200*b*u*w + 3*M001010*b*u*w + 3*M001010*b*w^2 + M002000*b*x + 3*M002000*e02*w + 3*M002000*e11*u + 3*M010100*e11*u + 3*M010100*e11*w + 18*M012100*b^2*l1^2*u + M020000*e13 + 9*M020200*b^2*l1^2*u + 9*M021010*b^2*l1^2*u + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l3 + 3*M022000*b*c10*l1*u + 9*M022000*b*c21*l1*w + 3*M022000*b*c32*l1*u + 3*M022000*b*c32*l1*w + 9*M022000*b*e02*l1^2 + 3*M030100*b*c10*l1*u + M030100*b*c32*l1*u + 3*M030100*b*e11*l1^2 + M040000*c10*c32*u + 15*M041010*b^3*l1^4 + 9*M042000*b^2*c21*l1^3 + 3*M042000*b^2*c32*l1^3 + 3*M103000*b*c10*l1*u + 12*M111100*b*c10*l1*u + 9*M111100*b*c10*l1*w + 3*M120010*b*c10*l1*u + 3*M120010*b*c10*l1*w + M121000*b*c10*l3 + M121000*b*c30*l1 + 6*M121000*c10^2*u + 3*M121000*c10*c21*w + 3*M121000*c10*c32*u + M121000*c10*c32*w + 3*M121000*c10*e02*l1 + 9*M131100*b^2*c10*l1^3 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*c21*l1^2 + M141000*b*c10*c32*l1^2 + 3*M202000*c10^2*u + 3*M210100*c10^2*u + 3*M210100*c10^2*w + M220000*c10*c30 + 3*M230100*b*c10^2*l1^2
```

### `e22_next`

```text
e22_next = 2*M000200*b*u^2 + 2*M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*u^2 + 2*M001010*b*u*w + M002000*b*y + 2*M002000*e02*u + 4*M002000*e11*w + 2*M010100*e02*u + 2*M010100*e02*w + 12*M012100*b^2*l1^2*u + M020000*e22 + 6*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*u + 4*M022000*b*c10*l1*u + 6*M022000*b*c21*l1*u + 4*M022000*b*e11*l1^2 + 2*M030100*b*c21*l1*u + 6*M030100*b*c21*l1*w + 6*M030100*b*e02*l1^2 + M040000*c21^2*w + 2*M040000*c21*e02*l1 + 15*M040200*b^3*l1^4 + 6*M050100*b^2*c21*l1^3 + M060000*b*c21^2*l1^2 + 4*M103000*b*c10*l1*u + 8*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 4*M121000*c10*c21*w + 4*M121000*c10*e02*l1 + 12*M131100*b^2*c10*l1^3 + 4*M141000*b*c10*c21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2
```

### `source00`

```text
source00 = M020000*b
```

### `source02`

```text
source02 = M002000*b*u + M010100*b*u + M010100*b*w + M020000*e02 + 3*M030100*b^2*l1^2 + M040000*b*c21*l1 + 2*M121000*b*c10*l1
```

### `source11`

```text
source11 = M002000*b*w + M020000*e11 + 3*M022000*b^2*l1^2 + 2*M121000*b*c10*l1 + M220000*c10^2
```

### `source13`

```text
source13 = 3*M000200*b*u*w + 3*M001010*b*u*w + 3*M001010*b*w^2 + M002000*b*x + 3*M002000*e02*w + 3*M002000*e11*u + 3*M010100*e11*u + 3*M010100*e11*w + 18*M012100*b^2*l1^2*u + M020000*e13 + 9*M020200*b^2*l1^2*u + 9*M021010*b^2*l1^2*u + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l3 + 3*M022000*b*c10*l1*u + 9*M022000*b*c21*l1*w + 3*M022000*b*c32*l1*u + 3*M022000*b*c32*l1*w + 9*M022000*b*e02*l1^2 + 3*M030100*b*c10*l1*u + M030100*b*c32*l1*u + 3*M030100*b*e11*l1^2 + M040000*c10*c32*u + 15*M041010*b^3*l1^4 + 9*M042000*b^2*c21*l1^3 + 3*M042000*b^2*c32*l1^3 + 3*M103000*b*c10*l1*u + 12*M111100*b*c10*l1*u + 9*M111100*b*c10*l1*w + 3*M120010*b*c10*l1*u + 3*M120010*b*c10*l1*w + M121000*b*c10*l3 + M121000*b*c30*l1 + 6*M121000*c10^2*u + 3*M121000*c10*c21*w + 3*M121000*c10*c32*u + M121000*c10*c32*w + 3*M121000*c10*e02*l1 + 9*M131100*b^2*c10*l1^3 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*c21*l1^2 + M141000*b*c10*c32*l1^2 + 3*M202000*c10^2*u + 3*M210100*c10^2*u + 3*M210100*c10^2*w + M220000*c10*c30 + 3*M230100*b*c10^2*l1^2
```

### `source22`

```text
source22 = 2*M000200*b*u^2 + 2*M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*u^2 + 2*M001010*b*u*w + M002000*b*y + 2*M002000*e02*u + 4*M002000*e11*w + 2*M010100*e02*u + 2*M010100*e02*w + 12*M012100*b^2*l1^2*u + M020000*e22 + 6*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*u + 4*M022000*b*c10*l1*u + 6*M022000*b*c21*l1*u + 4*M022000*b*e11*l1^2 + 2*M030100*b*c21*l1*u + 6*M030100*b*c21*l1*w + 6*M030100*b*e02*l1^2 + M040000*c21^2*w + 2*M040000*c21*e02*l1 + 15*M040200*b^3*l1^4 + 6*M050100*b^2*c21*l1^3 + M060000*b*c21^2*l1^2 + 4*M103000*b*c10*l1*u + 8*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 4*M121000*c10*c21*w + 4*M121000*c10*e02*l1 + 12*M131100*b^2*c10*l1^3 + 4*M141000*b*c10*c21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2
```

# Appendix C: moving-gradient transitions

## feature2

### `a2_next`

```text
a2_next = M020000*l2
```

### `q02_next`

```text
q02_next = M020000*q02 + M101000*q02 + M101000*w + M121000*b*l1^2 + M121000*b*l1*l2 + M220000*c10*l2
```

### `q22_next`

```text
q22_next = 2*M002000*q02^2 + 2*M002000*q02*w + 3*M002000*w^2 + 2*M010100*q02^2 + 2*M010100*q02*w + M020000*q22 + 6*M022000*b*l1^2*q02 + 6*M022000*b*l1^2*w + 6*M022000*b*l1*l2*q02 + 6*M022000*b*l1*l2*w + M022000*b*l2^2*w + 2*M030100*b*l1^2*q02 + 2*M030100*b*l1*l2*q02 + 2*M040000*c10*l2*q02 + M040000*e11*l2^2 + 3*M042000*b^2*l1^4 + 6*M042000*b^2*l1^3*l2 + 3*M042000*b^2*l1^2*l2^2 + 6*M121000*c10*l2*q02 + 2*M121000*c10*l2*w + 2*M141000*b*c10*l1^2*l2 + 2*M141000*b*c10*l1*l2^2 + M240000*c10^2*l2^2
```

### `qfm_next`

```text
qfm_next = 2*M002000*q02*u + M002000*q02*w + M002000*u*w + 3*M002000*w^2 + 2*M010100*q02*u + M010100*q02*w + M010100*u*w + M020000*qfm + 3*M022000*b*l1^2*q02 + 3*M022000*b*l1^2*u + 6*M022000*b*l1^2*w + 3*M022000*b*l1*l2*u + 3*M022000*b*l1*l2*w + M030100*b*l1^2*q02 + M030100*b*l1^2*u + M030100*b*l1*l2*u + M040000*c10*l2*u + 3*M042000*b^2*l1^4 + 3*M042000*b^2*l1^3*l2 + 3*M121000*c10*l2*u + M121000*c10*l2*w + M141000*b*c10*l1^2*l2
```

## gradient2

### `d21_next`

```text
d21_next = M002000*b*l2 + 2*M010100*b*l1 + M020000*b + M020000*d21 + 2*M101000*c10
```

### `r02_next`

```text
r02_next = M002000*b*q02 + M010100*b*q02 + M010100*b*w + M020000*r02 + 3*M022000*b^2*l1*l2 + 3*M030100*b^2*l1^2 + M040000*b*d21*l1 + 2*M121000*b*c10*l1 + M121000*b*c10*l2
```

### `r22_next`

```text
r22_next = 2*M000200*b*q02^2 + 2*M000200*b*q02*w + 3*M000200*b*w^2 + 2*M001010*b*q02^2 + 2*M001010*b*q02*w + M002000*b*q22 + 4*M002000*e11*w + 2*M002000*q02*r02 + 6*M004000*b^2*l1*l2*q02 + 3*M004000*b^2*l2^2*w + 2*M010100*q02*r02 + 2*M010100*r02*w + 12*M012100*b^2*l1^2*q02 + 18*M012100*b^2*l1*l2*q02 + 18*M012100*b^2*l1*l2*w + M020000*r22 + 6*M020200*b^2*l1^2*q02 + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*q02 + 4*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l2*q02 + 6*M022000*b*d21*l1*q02 + 2*M022000*b*d21*l2*w + 4*M022000*b*e11*l1^2 + 4*M022000*b*e11*l1*l2 + M022000*b*e11*l2^2 + 6*M022000*b*l1*l2*r02 + 15*M024000*b^3*l1^2*l2^2 + 2*M030100*b*d21*l1*q02 + 6*M030100*b*d21*l1*w + 6*M030100*b*l1^2*r02 + 30*M032100*b^3*l1^3*l2 + M040000*d21^2*w + 2*M040000*d21*l1*r02 + 15*M040200*b^3*l1^4 + 6*M042000*b^2*d21*l1^2*l2 + 6*M050100*b^2*d21*l1^3 + M060000*b*d21^2*l1^2 + 4*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l2*q02 + 4*M103000*b*c10*l2*w + 8*M111100*b*c10*l1*q02 + 12*M111100*b*c10*l1*w + 4*M111100*b*c10*l2*q02 + 2*M111100*b*c10*l2*w + 4*M121000*c10*d21*w + 4*M121000*c10*l1*r02 + 2*M121000*c10*l2*r02 + 12*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1*l2^2 + 12*M131100*b^2*c10*l1^3 + 6*M131100*b^2*c10*l1^2*l2 + 4*M141000*b*c10*d21*l1^2 + 2*M141000*b*c10*d21*l1*l2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 4*M222000*b*c10^2*l1*l2 + M222000*b*c10^2*l2^2
```

### `rfm_next`

```text
rfm_next = 2*M000200*b*q02*u + M000200*b*q02*w + M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*q02*u + M001010*b*q02*w + M001010*b*u*w + M002000*b*qfm + M002000*e02*q02 + 4*M002000*e11*w + M002000*r02*u + 3*M004000*b^2*l1*l2*u + M010100*e02*q02 + M010100*e02*w + M010100*r02*u + M010100*r02*w + 6*M012100*b^2*l1^2*q02 + 6*M012100*b^2*l1^2*u + 9*M012100*b^2*l1*l2*u + 9*M012100*b^2*l1*l2*w + M020000*rfm + 3*M020200*b^2*l1^2*q02 + 3*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 3*M021010*b^2*l1^2*q02 + 3*M021010*b^2*l1^2*u + 2*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l1*u + M022000*b*c10*l2*u + 3*M022000*b*c21*l1*q02 + M022000*b*c21*l2*w + 3*M022000*b*d21*l1*u + 3*M022000*b*e02*l1*l2 + 4*M022000*b*e11*l1^2 + 2*M022000*b*e11*l1*l2 + M030100*b*c21*l1*q02 + 3*M030100*b*c21*l1*w + M030100*b*d21*l1*u + 3*M030100*b*d21*l1*w + 3*M030100*b*e02*l1^2 + 3*M030100*b*l1^2*r02 + 15*M032100*b^3*l1^3*l2 + M040000*c21*d21*w + M040000*c21*l1*r02 + M040000*d21*e02*l1 + 15*M040200*b^3*l1^4 + 3*M042000*b^2*c21*l1^2*l2 + 3*M050100*b^2*c21*l1^3 + 3*M050100*b^2*d21*l1^3 + M060000*b*c21*d21*l1^2 + 2*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l1*u + M103000*b*c10*l2*u + 2*M103000*b*c10*l2*w + 4*M111100*b*c10*l1*q02 + 4*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 2*M111100*b*c10*l2*u + M111100*b*c10*l2*w + 2*M121000*c10*c21*w + 2*M121000*c10*d21*w + 2*M121000*c10*e02*l1 + M121000*c10*e02*l2 + 2*M121000*c10*l1*r02 + 6*M123000*b^2*c10*l1^2*l2 + 12*M131100*b^2*c10*l1^3 + 3*M131100*b^2*c10*l1^2*l2 + 2*M141000*b*c10*c21*l1^2 + M141000*b*c10*c21*l1*l2 + 2*M141000*b*c10*d21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 2*M222000*b*c10^2*l1*l2
```

### `source02m`

```text
source02m = M002000*b*q02 + M010100*b*q02 + M010100*b*w + M020000*r02 + 3*M022000*b^2*l1*l2 + 3*M030100*b^2*l1^2 + M040000*b*d21*l1 + 2*M121000*b*c10*l1 + M121000*b*c10*l2
```

### `source22m`

```text
source22m = 2*M000200*b*q02^2 + 2*M000200*b*q02*w + 3*M000200*b*w^2 + 2*M001010*b*q02^2 + 2*M001010*b*q02*w + M002000*b*q22 + 4*M002000*e11*w + 2*M002000*q02*r02 + 6*M004000*b^2*l1*l2*q02 + 3*M004000*b^2*l2^2*w + 2*M010100*q02*r02 + 2*M010100*r02*w + 12*M012100*b^2*l1^2*q02 + 18*M012100*b^2*l1*l2*q02 + 18*M012100*b^2*l1*l2*w + M020000*r22 + 6*M020200*b^2*l1^2*q02 + 18*M020200*b^2*l1^2*w + 6*M021010*b^2*l1^2*q02 + 4*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l2*q02 + 6*M022000*b*d21*l1*q02 + 2*M022000*b*d21*l2*w + 4*M022000*b*e11*l1^2 + 4*M022000*b*e11*l1*l2 + M022000*b*e11*l2^2 + 6*M022000*b*l1*l2*r02 + 15*M024000*b^3*l1^2*l2^2 + 2*M030100*b*d21*l1*q02 + 6*M030100*b*d21*l1*w + 6*M030100*b*l1^2*r02 + 30*M032100*b^3*l1^3*l2 + M040000*d21^2*w + 2*M040000*d21*l1*r02 + 15*M040200*b^3*l1^4 + 6*M042000*b^2*d21*l1^2*l2 + 6*M050100*b^2*d21*l1^3 + M060000*b*d21^2*l1^2 + 4*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l2*q02 + 4*M103000*b*c10*l2*w + 8*M111100*b*c10*l1*q02 + 12*M111100*b*c10*l1*w + 4*M111100*b*c10*l2*q02 + 2*M111100*b*c10*l2*w + 4*M121000*c10*d21*w + 4*M121000*c10*l1*r02 + 2*M121000*c10*l2*r02 + 12*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1*l2^2 + 12*M131100*b^2*c10*l1^3 + 6*M131100*b^2*c10*l1^2*l2 + 4*M141000*b*c10*d21*l1^2 + 2*M141000*b*c10*d21*l1*l2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 4*M222000*b*c10^2*l1*l2 + M222000*b*c10^2*l2^2
```

### `sourcefm`

```text
sourcefm = 2*M000200*b*q02*u + M000200*b*q02*w + M000200*b*u*w + 3*M000200*b*w^2 + 2*M001010*b*q02*u + M001010*b*q02*w + M001010*b*u*w + M002000*b*qfm + M002000*e02*q02 + 4*M002000*e11*w + M002000*r02*u + 3*M004000*b^2*l1*l2*u + M010100*e02*q02 + M010100*e02*w + M010100*r02*u + M010100*r02*w + 6*M012100*b^2*l1^2*q02 + 6*M012100*b^2*l1^2*u + 9*M012100*b^2*l1*l2*u + 9*M012100*b^2*l1*l2*w + M020000*rfm + 3*M020200*b^2*l1^2*q02 + 3*M020200*b^2*l1^2*u + 18*M020200*b^2*l1^2*w + 3*M021010*b^2*l1^2*q02 + 3*M021010*b^2*l1^2*u + 2*M022000*b*c10*l1*q02 + 2*M022000*b*c10*l1*u + M022000*b*c10*l2*u + 3*M022000*b*c21*l1*q02 + M022000*b*c21*l2*w + 3*M022000*b*d21*l1*u + 3*M022000*b*e02*l1*l2 + 4*M022000*b*e11*l1^2 + 2*M022000*b*e11*l1*l2 + M030100*b*c21*l1*q02 + 3*M030100*b*c21*l1*w + M030100*b*d21*l1*u + 3*M030100*b*d21*l1*w + 3*M030100*b*e02*l1^2 + 3*M030100*b*l1^2*r02 + 15*M032100*b^3*l1^3*l2 + M040000*c21*d21*w + M040000*c21*l1*r02 + M040000*d21*e02*l1 + 15*M040200*b^3*l1^4 + 3*M042000*b^2*c21*l1^2*l2 + 3*M050100*b^2*c21*l1^3 + 3*M050100*b^2*d21*l1^3 + M060000*b*c21*d21*l1^2 + 2*M103000*b*c10*l1*q02 + 2*M103000*b*c10*l1*u + M103000*b*c10*l2*u + 2*M103000*b*c10*l2*w + 4*M111100*b*c10*l1*q02 + 4*M111100*b*c10*l1*u + 12*M111100*b*c10*l1*w + 2*M111100*b*c10*l2*u + M111100*b*c10*l2*w + 2*M121000*c10*c21*w + 2*M121000*c10*d21*w + 2*M121000*c10*e02*l1 + M121000*c10*e02*l2 + 2*M121000*c10*l1*r02 + 6*M123000*b^2*c10*l1^2*l2 + 12*M131100*b^2*c10*l1^3 + 3*M131100*b^2*c10*l1^2*l2 + 2*M141000*b*c10*c21*l1^2 + M141000*b*c10*c21*l1*l2 + 2*M141000*b*c10*d21*l1^2 + 4*M202000*c10^2*w + 4*M222000*b*c10^2*l1^2 + 2*M222000*b*c10^2*l1*l2
```

## feature3

### `a30_next`

```text
a30_next = 3*M002000*l1*q02 + 3*M002000*l2*w + M002000*l32*q02 + 3*M010100*l1*q02 + 3*M010100*l1*w + M010100*l32*q02 + M010100*l32*w + M020000*l30 + 9*M022000*b*l1^2*l2 + 3*M022000*b*l1*l2*l32 + 3*M030100*b*l1^3 + 3*M030100*b*l1^2*l32 + M040000*d21*l1*l32 + 3*M121000*c10*l1*l2 + 2*M121000*c10*l1*l32 + M121000*c10*l2*l32
```

### `a32_next`

```text
a32_next = M020000*l32
```

### `q13_next`

```text
q13_next = 3*M002000*q02*w + 3*M010100*q02*w + 3*M010100*w^2 + M020000*q13 + 9*M022000*b*l1^2*q02 + 9*M022000*b*l1*l2*w + 3*M022000*b*l1*l32*q02 + M022000*b*l2*l32*w + 3*M030100*b*l1^2*q02 + 6*M030100*b*l1^2*w + M030100*b*l1*l32*q02 + 3*M030100*b*l1*l32*w + M040000*b*l1*l30 + M040000*d21*l32*w + M040000*l1*l32*r02 + 9*M042000*b^2*l1^3*l2 + 3*M042000*b^2*l1^2*l2*l32 + 3*M050100*b^2*l1^4 + 3*M050100*b^2*l1^3*l32 + M060000*b*d21*l1^2*l32 + 3*M121000*c10*l2*w + 2*M121000*c10*l32*w + 3*M141000*b*c10*l1^2*l2 + 2*M141000*b*c10*l1^2*l32 + M141000*b*c10*l1*l2*l32
```

## gradient3

### `d30_next`

```text
d30_next = 3*M000200*b*l1*q02 + 3*M000200*b*l2*w + 2*M000200*b*l32*q02 + M000200*b*l32*w + 6*M001010*b*l1*q02 + 3*M001010*b*l1*w + 3*M001010*b*l2*w + 2*M001010*b*l32*q02 + M001010*b*l32*w + M002000*b*l30 + 4*M002000*b*q02 + 3*M002000*b*w + 3*M002000*c10*q02 + 3*M002000*d21*w + 2*M002000*d32*q02 + M002000*d32*w + 3*M002000*e11*l2 + 3*M002000*l1*r02 + M002000*l32*r02 + 3*M004000*b^2*l1*l2*l32 + 3*M010001*b*l1*q02 + 3*M010001*b*l1*w + M010100*b*l30 + 4*M010100*b*q02 + 4*M010100*b*w + 6*M010100*c10*q02 + 3*M010100*c10*w + 3*M010100*d21*w + 2*M010100*d32*q02 + M010100*d32*w + 3*M010100*e11*l2 + 3*M010100*l1*r02 + M010100*l32*r02 + 18*M012100*b^2*l1^2*l2 + 6*M012100*b^2*l1^2*l32 + 9*M012100*b^2*l1*l2*l32 + M020000*d30 + 3*M020000*e11 + 4*M020000*r02 + 9*M020200*b^2*l1^2*l2 + 3*M020200*b^2*l1^2*l32 + 9*M021010*b^2*l1^3 + 9*M021010*b^2*l1^2*l2 + 3*M021010*b^2*l1^2*l32 + 9*M022000*b^2*l1^2 + 12*M022000*b^2*l1*l2 + 3*M022000*b*c10*l1*l2 + 2*M022000*b*c10*l1*l32 + M022000*b*c10*l2*l32 + 9*M022000*b*d21*l1^2 + 3*M022000*b*d21*l1*l32 + 3*M022000*b*d32*l1^2 + 3*M022000*b*d32*l1*l2 + 3*M030001*b^2*l1^3 + 12*M030100*b^2*l1^2 + 3*M030100*b*c10*l1^2 + 3*M030100*b*c10*l1*l2 + 3*M030100*b*d21*l1^2 + M030100*b*d21*l1*l32 + M030100*b*d32*l1^2 + M030100*b*d32*l1*l2 + 4*M040000*b*d21*l1 + M040000*c10*d32*l2 + 3*M100010*c10*q02 + 3*M100010*c10*w + M101000*d30 + 3*M103000*b*c10*l1*l2 + 2*M103000*b*c10*l1*l32 + M103000*b*c10*l2*l32 + 6*M111100*b*c10*l1^2 + 12*M111100*b*c10*l1*l2 + 4*M111100*b*c10*l1*l32 + 2*M111100*b*c10*l2*l32 + 3*M120010*b*c10*l1^2 + 3*M120010*b*c10*l1*l2 + 14*M121000*b*c10*l1 + 4*M121000*b*c10*l2 + 6*M121000*c10^2*l2 + 3*M121000*c10*d32*l2 + 3*M202000*c10^2*l2 + 3*M210100*c10^2*l2 + 3*M220000*c10^2
```

### `d32_next`

```text
d32_next = M002000*b*l32 + 3*M010100*b*l1 + M020000*b + M020000*d32 + 3*M101000*c10
```

### `r13_next`

```text
r13_next = 3*M000200*b*q02*w + 3*M001010*b*q02*w + 3*M001010*b*w^2 + M002000*b*q13 + 3*M002000*e11*q02 + 3*M002000*r02*w + 3*M004000*b^2*l1*l32*q02 + 3*M004000*b^2*l2*l32*w + 3*M010100*e11*q02 + 3*M010100*e11*w + 18*M012100*b^2*l1^2*q02 + 27*M012100*b^2*l1*l2*w + 9*M012100*b^2*l1*l32*q02 + 9*M012100*b^2*l1*l32*w + M020000*r13 + 9*M020200*b^2*l1^2*q02 + 9*M021010*b^2*l1^2*q02 + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l30 + 3*M022000*b*c10*l1*q02 + M022000*b*c10*l32*q02 + 9*M022000*b*d21*l1*w + M022000*b*d21*l32*w + 3*M022000*b*d32*l1*q02 + 3*M022000*b*d32*l1*w + M022000*b*d32*l2*w + 6*M022000*b*e11*l1*l2 + 2*M022000*b*e11*l1*l32 + M022000*b*e11*l2*l32 + 9*M022000*b*l1^2*r02 + 3*M022000*b*l1*l32*r02 + 15*M024000*b^3*l1^2*l2*l32 + 3*M030100*b*c10*l1*q02 + M030100*b*d32*l1*q02 + 3*M030100*b*e11*l1^2 + 3*M030100*b*e11*l1*l2 + 45*M032100*b^3*l1^3*l2 + 15*M032100*b^3*l1^3*l32 + M040000*c10*d32*q02 + M040000*d32*e11*l2 + 15*M041010*b^3*l1^4 + 9*M042000*b^2*d21*l1^3 + 3*M042000*b^2*d21*l1^2*l32 + 3*M042000*b^2*d32*l1^3 + 3*M042000*b^2*d32*l1^2*l2 + 3*M103000*b*c10*l1*q02 + 3*M103000*b*c10*l2*w + M103000*b*c10*l32*q02 + 2*M103000*b*c10*l32*w + 12*M111100*b*c10*l1*q02 + 9*M111100*b*c10*l1*w + 6*M111100*b*c10*l2*w + 2*M111100*b*c10*l32*q02 + M111100*b*c10*l32*w + 3*M120010*b*c10*l1*q02 + 3*M120010*b*c10*l1*w + M121000*b*c10*l30 + M121000*b*d30*l1 + 6*M121000*c10^2*q02 + 3*M121000*c10*d21*w + 3*M121000*c10*d32*q02 + M121000*c10*d32*w + 9*M121000*c10*e11*l2 + 3*M121000*c10*l1*r02 + M121000*c10*l32*r02 + 9*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1^2*l32 + 6*M123000*b^2*c10*l1*l2*l32 + 9*M131100*b^2*c10*l1^3 + 18*M131100*b^2*c10*l1^2*l2 + 3*M131100*b^2*c10*l1^2*l32 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*d21*l1^2 + M141000*b*c10*d21*l1*l32 + M141000*b*c10*d32*l1^2 + 2*M141000*b*c10*d32*l1*l2 + 3*M202000*c10^2*q02 + 3*M210100*c10^2*q02 + 3*M210100*c10^2*w + M220000*c10*d30 + 6*M222000*b*c10^2*l1*l2 + 2*M222000*b*c10^2*l1*l32 + M222000*b*c10^2*l2*l32 + 3*M230100*b*c10^2*l1^2 + 3*M230100*b*c10^2*l1*l2 + M240000*c10^2*d32*l2 + 3*M321000*c10^3*l2
```

### `source13m`

```text
source13m = 3*M000200*b*q02*w + 3*M001010*b*q02*w + 3*M001010*b*w^2 + M002000*b*q13 + 3*M002000*e11*q02 + 3*M002000*r02*w + 3*M004000*b^2*l1*l32*q02 + 3*M004000*b^2*l2*l32*w + 3*M010100*e11*q02 + 3*M010100*e11*w + 18*M012100*b^2*l1^2*q02 + 27*M012100*b^2*l1*l2*w + 9*M012100*b^2*l1*l32*q02 + 9*M012100*b^2*l1*l32*w + M020000*r13 + 9*M020200*b^2*l1^2*q02 + 9*M021010*b^2*l1^2*q02 + 18*M021010*b^2*l1^2*w + 3*M022000*b^2*l1*l30 + 3*M022000*b*c10*l1*q02 + M022000*b*c10*l32*q02 + 9*M022000*b*d21*l1*w + M022000*b*d21*l32*w + 3*M022000*b*d32*l1*q02 + 3*M022000*b*d32*l1*w + M022000*b*d32*l2*w + 6*M022000*b*e11*l1*l2 + 2*M022000*b*e11*l1*l32 + M022000*b*e11*l2*l32 + 9*M022000*b*l1^2*r02 + 3*M022000*b*l1*l32*r02 + 15*M024000*b^3*l1^2*l2*l32 + 3*M030100*b*c10*l1*q02 + M030100*b*d32*l1*q02 + 3*M030100*b*e11*l1^2 + 3*M030100*b*e11*l1*l2 + 45*M032100*b^3*l1^3*l2 + 15*M032100*b^3*l1^3*l32 + M040000*c10*d32*q02 + M040000*d32*e11*l2 + 15*M041010*b^3*l1^4 + 9*M042000*b^2*d21*l1^3 + 3*M042000*b^2*d21*l1^2*l32 + 3*M042000*b^2*d32*l1^3 + 3*M042000*b^2*d32*l1^2*l2 + 3*M103000*b*c10*l1*q02 + 3*M103000*b*c10*l2*w + M103000*b*c10*l32*q02 + 2*M103000*b*c10*l32*w + 12*M111100*b*c10*l1*q02 + 9*M111100*b*c10*l1*w + 6*M111100*b*c10*l2*w + 2*M111100*b*c10*l32*q02 + M111100*b*c10*l32*w + 3*M120010*b*c10*l1*q02 + 3*M120010*b*c10*l1*w + M121000*b*c10*l30 + M121000*b*d30*l1 + 6*M121000*c10^2*q02 + 3*M121000*c10*d21*w + 3*M121000*c10*d32*q02 + M121000*c10*d32*w + 9*M121000*c10*e11*l2 + 3*M121000*c10*l1*r02 + M121000*c10*l32*r02 + 9*M123000*b^2*c10*l1^2*l2 + 6*M123000*b^2*c10*l1^2*l32 + 6*M123000*b^2*c10*l1*l2*l32 + 9*M131100*b^2*c10*l1^3 + 18*M131100*b^2*c10*l1^2*l2 + 3*M131100*b^2*c10*l1^2*l32 + 3*M140010*b^2*c10*l1^3 + 3*M141000*b*c10*d21*l1^2 + M141000*b*c10*d21*l1*l32 + M141000*b*c10*d32*l1^2 + 2*M141000*b*c10*d32*l1*l2 + 3*M202000*c10^2*q02 + 3*M210100*c10^2*q02 + 3*M210100*c10^2*w + M220000*c10*d30 + 6*M222000*b*c10^2*l1*l2 + 2*M222000*b*c10^2*l1*l32 + M222000*b*c10^2*l2*l32 + 3*M230100*b*c10^2*l1^2 + 3*M230100*b*c10^2*l1*l2 + M240000*c10^2*d32*l2 + 3*M321000*c10^3*l2
```
