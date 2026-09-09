# Quantitative width-first half-step theorem

## Theorem

Let both hidden layers have width $n$.  Let the input dimension be $p$ and
let the deterministic input satisfy

$$
q=\frac{\lVert x\rVert^2}{p}=1,
$$

and let all raw parameters at initialization be independent standard
Gaussians.  Assume $\phi\in C^{12}(\mathbb R)$,

$$
G\sim\mathcal N(0,1),
\qquad
\mathbb E[\phi(G)^2]=1,
$$

and

$$
M_\phi
=
\max\left\{
1,
\sup_{x\in\mathbb R}\frac{|\phi(x)|}{1+|x|},
\max_{1\le r\le12}\lVert\phi^{(r)}\rVert_\infty
\right\}
<\infty.
$$

For a fixed step size $h$, let $F_{k,n}(h)$ be the expected output after
$k$ recomputed simultaneous gradient-ascent steps, each of size $h$.
Section 3 defines operator functions $F_k:[-1,1]\to\mathbb R$ without
using a width limit, and Section 5 proves their $C^5$ regularity.  The
quantities defined in Sections 6--8 below are computable from $M_\phi$ and
finitely many one-dimensional Gaussian
activation moments.  They satisfy

$$
0<h_\phi\le1,
\qquad
0\le B_\phi<\infty.
$$

For every fixed nonzero $h$ with $|h|\le h_\phi$, the one-step and
two-step finite-width expected outputs converge to the four-stage Gaussian
operator program in Section 3, and hence to $F_k(h)$.  The same statement at
$h=0$ follows directly from the initialized network.  Thus, throughout the
claimed interval, $F_k$ is exactly the width-first limit.  If

$$
\Delta(\eta)=F_2(\eta/2)-F_1(\eta),
$$

then, for every $|\eta|\le h_\phi$,

$$
\left|
\Delta(\eta)-\kappa_\phi\eta^3
\right|
\le
B_\phi|\eta|^5.
$$

Consequently, for every $\varepsilon>0$,

$$
|\eta|
\le
\eta_0(\phi,\varepsilon)
:=
\min\left\{
h_\phi,
\sqrt{\frac{\varepsilon}{1+B_\phi}}
\right\}
$$

implies

$$
|\Delta(\eta)|
\le
(|\kappa_\phi|+\varepsilon)|\eta|^3.
$$

The proof always takes (n\to\infty) at fixed nonzero step size first.  All
differentiation in the learning rate is performed only after the limiting
Gaussian program has been identified.

## 1. Exact finite-width network

For each width $n$, take

$$
w_j^0\overset{\mathrm{iid}}\sim\mathcal N(0,I_p),
\qquad
W_{ij}^0\overset{\mathrm{iid}}\sim\mathcal N(0,1),
\qquad
a_i^0\overset{\mathrm{iid}}\sim\mathcal N(0,1),
$$

with all three families mutually independent and $x\in\mathbb R^p$
deterministic.  There are no biases.  Write

Write

$$
u_j^s=\frac{(w_j^s)^\top x}{\sqrt p},
\qquad
H_j^s=\phi(u_j^s),
$$

$$
z_i^s
=\frac1{\sqrt n}\sum_{j=1}^nW_{ij}^sH_j^s,
\qquad
f_n^s
=\frac1n\sum_{i=1}^na_i^s\phi(z_i^s).
$$

The ascent rule is

$$
\theta^{s+1}=\theta^s+hn\nabla_\theta f_n^s.
$$

Set

$$
C_i^s=a_i^s\phi'(z_i^s),
\qquad
b_j^s=\frac1{\sqrt n}\sum_{i=1}^nW_{ij}^sC_i^s.
$$

Because $q=1$, direct differentiation gives the exact simultaneous update

$$
\begin{aligned}
a_i^{s+1}&=a_i^s+h\phi(z_i^s),\\
W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}C_i^sH_j^s,\\
w_j^{s+1}&=w_j^s+\frac h{\sqrt p}b_j^s\phi'(u_j^s)x,\\
u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s).
\end{aligned}
$$

These formulas are applied for $s=0,1$; every right-hand side uses only
time-$s$ quantities.  The last line follows from the preceding parameter
update and $\lVert x\rVert^2/p=1$.

Let (W=W^0), and
use

$$
Q_{rs}^{(n)}=\frac1n(H^r)^\top H^s,
\qquad
K_{rs}^{(n)}=\frac1n(C^r)^\top C^s.
$$

Keeping the learned rank-one terms separate from the source matrix (W)
gives the exact identities

$$
\begin{aligned}
z^0&=WH^0/\sqrt n,\\
b^0&=W^\top C^0/\sqrt n,\\
z^1&=WH^1/\sqrt n+hQ_{01}^{(n)}C^0,\\
b^1&=W^\top C^1/\sqrt n+hK_{01}^{(n)}H^0,\\
z^2&=WH^2/\sqrt n
 +hQ_{02}^{(n)}C^0+hQ_{12}^{(n)}C^1.
\end{aligned}
$$

There is no (hK_{11}^{(n)}H^1) term in (b^1), because the second update
of (W) occurs only after (b^1) has been used.

The annealed outputs used in the theorem are

$$
F_{k,n}(h)=\mathbb E[f_n^k].
$$

## 2. Gaussian notation

For every positive-semidefinite matrix (C), including a singular one, let

$$
\Gamma_C[\psi]
=\mathbb E[\psi(X_C)],
\qquad
X_C\sim\mathcal N(0,C).
$$

Put

$$
d=\mathbb E[\phi'(G)^2].
$$

The nonconstant case has (d>0).  The case (d=0) is treated separately in
Section 8.

## 3. The four-stage limiting operator program

All Gaussian variables appearing together below have exactly the stated joint
law; time copies are never replaced by independent copies.

### 3.1 First lower operator

Let

$$
(U,\chi_0)\sim\mathcal N(0,\operatorname{diag}(1,d)),
$$

and define

$$
u_0=U,
\qquad
u_1=U+h\chi_0\phi'(U),
\qquad
H_r=\phi(u_r).
$$

Set

$$
Q_{rs}=\mathbb E[H_rH_s],
\qquad r,s\in\{0,1\},
$$

$$
\rho_{10}=\mathbb E[\partial_{\chi_0}H_1],
\qquad
L_{10}=\rho_{10}+hQ_{01}.
$$

### 3.2 First top operator

Let (A\sim\mathcal N(0,1)) be independent of a centered Gaussian pair
((\xi_0,\xi_1)) with covariance (Q).  Define

$$
z_0=\xi_0,
\qquad
C_0=A\phi'(z_0),
$$

$$
a_1=A+h\phi(z_0),
\qquad
z_1=\xi_1+L_{10}C_0,
\qquad
C_1=a_1\phi'(z_1).
$$

Then

$$
F_1(h)=\mathbb E[a_1\phi(z_1)],
$$

$$
K_{rs}=\mathbb E[C_rC_s],
\qquad
\sigma_{1r}=\mathbb E[\partial_{\xi_r}C_1],
\qquad r,s\in\{0,1\}.
$$

### 3.3 Second lower operator

Let $(\chi_0,\chi_1)$ be centered Gaussian with covariance $K$, independent
of $U$.  Jointly recompute $u_0,u_1,H_0,H_1$, and set

$$
b_1
=\chi_1+(\sigma_{10}+hK_{01})H_0+\sigma_{11}H_1,
$$

$$
u_2=u_1+h b_1\phi'(u_1),
\qquad
H_2=\phi(u_2).
$$

Extend the feature Gram by

$$
Q_{r2}=\mathbb E[H_rH_2],
\qquad
\rho_{2r}=\mathbb E[\partial_{\chi_r}H_2],
\qquad r\in\{0,1\},
$$

and set

$$
L_{2r}=\rho_{2r}+hQ_{r2}.
$$

### 3.4 Final top operator

Let $(\xi_0,\xi_1,\xi_2)$ be centered Gaussian with the full $3\times3$
feature Gram $Q^{(2)}$, independent of $A$.  With the same
$A,\xi_0,\xi_1$, recompute
(z_0,z_1,C_0,C_1), and define

$$
z_2=\xi_2+L_{20}C_0+L_{21}C_1,
$$

$$
a_2=A+h\bigl(\phi(z_0)+\phi(z_1)\bigr).
$$

The two-step limiting output is

$$
F_2(h)=\mathbb E[a_2\phi(z_2)].
$$

## 4. Fixed-step finite-width identification

### 4.1 Exact adaptive row/column conditioning

We first prove the only matrix-conditioning result used below.

**Lemma 4.1.**  Let (W\in\mathbb R^{n\times n}) have independent standard
Gaussian entries and be independent of an external sigma-field
(\mathcal E).  Suppose that, in a finite chronological program, $H$ and $C$
contain all accumulated row and column query vectors, respectively, and that
their columns are measurable functions of $\mathcal E$ and matrix actions
revealed earlier in the program.  Every new query $h$ or $c$ is required to
be measurable before its corresponding new matrix action is revealed.  Put

$$
Y=WH/\sqrt n,
\qquad
D=W^\top C/\sqrt n.
$$

Conditionally on the current filtration, the following is an equality in
conditional law:

$$
W
=P_CW+WP_H-P_CWP_H
 +P_C^\perp\widetilde W P_H^\perp,
$$

where $\widetilde W$ is an independent standard Gaussian matrix and
$P_H,P_C$ are the orthogonal projectors onto the displayed column spans.

If

$$
Q=H^\top H/n,
\qquad
K=C^\top C/n,
\qquad
R=C^\top Y/n=D^\top H/n
$$

have $Q$ and $K$ invertible, then a new column query $c\in\mathbb R^n$
obeys

$$
\begin{aligned}
W^\top c/\sqrt n
={}&DK^{-1}k
 +HQ^{-1}(r-R^\top K^{-1}k)\\
&+\tau_cP_H^\perp g,
\end{aligned}
$$

where

$$
k=C^\top c/n,
\qquad
r=Y^\top c/n,
$$

$$
\tau_c^2=c^\top c/n-k^\top K^{-1}k,
$$

and (g\sim\mathcal N(0,I_n)) is independent of the current filtration.
Likewise, a new row query (h\in\mathbb R^n) obeys

$$
\begin{aligned}
Wh/\sqrt n
={}&YQ^{-1}q
 +CK^{-1}(v-RQ^{-1}q)\\
&+\tau_hP_C^\perp g,
\end{aligned}
$$

where

$$
q=H^\top h/n,
\qquad
v=D^\top h/n,
$$

$$
\tau_h^2=h^\top h/n-q^\top Q^{-1}q.
$$

Empty (H)- or (C)-blocks are simply omitted.

**Proof.**  We first prove the adaptive statement, rather than conditioning
on random projectors as though they were deterministic in advance.  After
$t$ actions, let $H_t,C_t$ contain all row and column queries already made,
and let $\mathcal F_t$ contain the external marks, those queries, and their
revealed actions.  We claim inductively that

$$
\mathcal L(W\mid\mathcal F_t)
=
\mathcal L\!\left(
M_t+P_{C_t}^{\perp}G_tP_{H_t}^{\perp}
\,\middle|\,\mathcal F_t
\right),
$$

where

$$
M_t=P_{C_t}W+WP_{H_t}-P_{C_t}WP_{H_t}
$$

is determined by the revealed actions, and $G_t$ is a fresh standard
Gaussian matrix independent of $\mathcal F_t$.  The claim is immediate at
$t=0$, with empty query blocks.

Suppose first that the next predictable query is a row query $h$.  Given
$\mathcal F_t$, write

$$
h=P_{H_t}h+h_\perp.
$$

The only unrevealed part of $Wh/\sqrt n$ is
$P_{C_t}^{\perp}G_th_\perp/\sqrt n$.  If $h_\perp\ne0$, put
$e=h_\perp/\lVert h_\perp\rVert$.  The two Gaussian projections
$G_t e e^\top$ and $G_t(I-ee^\top)$ are independent.  Revealing the new action
therefore fixes the former projection (after $P_{C_t}^{\perp}$), while

$$
P_{C_t}^{\perp}G_tP_{\operatorname{span}(H_t,h)}^{\perp}
$$

remains an independent double-orthogonal Gaussian residual.  This is the
induction claim with $h$ appended to $H_t$.  If $h_\perp=0$, no residual is
revealed and the same conclusion is immediate.  A column query is identical
after transposition: decompose it orthogonally to $C_t$, reveal the
corresponding left Gaussian direction, and append it to $C_t$.  Since each
new query is $\mathcal F_t$-measurable, adjoining the query itself reveals no
extra information.  This proves the conditional-law claim for every stage.

For completeness, once $H,C$ are fixed, the algebra behind $M_t$ is the
orthogonal decomposition below.  With the Frobenius inner product, the four
subspaces

$$
P_C\mathbb R^{n\times n}P_H,
\quad
P_C\mathbb R^{n\times n}P_H^\perp,
\quad
P_C^\perp\mathbb R^{n\times n}P_H,
\quad
P_C^\perp\mathbb R^{n\times n}P_H^\perp
$$

are mutually orthogonal.  The actions $Y,D$ determine the first three
projections: $WP_H$ is determined by $Y$, $P_CW$ by $D$, and their common
part was counted twice.  The fourth projection is exactly the residual in
the proved conditional-law invariant.

For the column formula, decompose

$$
c=CK^{-1}k+c_\perp,
\qquad
C^\top c_\perp=0.
$$

The first part gives (DK^{-1}k).  The projection of
(W^\top c_\perp/\sqrt n) onto the span of (H) is

$$
HQ^{-1}\frac{Y^\top c_\perp}{n}
=HQ^{-1}(r-R^\top K^{-1}k).
$$

Its remaining conditional covariance is

$$
\frac{\lVert c_\perp\rVert^2}{n}P_H^\perp
=\tau_c^2P_H^\perp.
$$

This proves the column formula.  Decomposing
(h=HQ^{-1}q+h_\perp) and exchanging rows with columns gives the row formula.
If a finite-width span is singular, the same identities hold with
Moore--Penrose inverses because the proof only uses orthogonal projectors.

### 4.2 A finite-query convergence lemma

For (p\ge1), write

$$
\lVert x\rVert_{n,p}
=\left(\frac1n\sum_{i=1}^n|x_i|^p\right)^{1/p}.
$$

We use the following two inequalities.

First, if (X_1,\ldots,X_n) are independent, centered, and (p\ge2),
Rosenthal's inequality states

$$
\left\lVert
\frac1n\sum_{i=1}^nX_i
\right\rVert_{L^p}
\le
C_p\left(
n^{-1/2}\lVert X_1\rVert_{L^2}
 +n^{-1+1/p}\lVert X_1\rVert_{L^p}
\right)
$$

in the identically distributed case.  Every variable to which it is applied
below has all finite moments, as verified in the moment step of the proof.

Second, an (n\times n) standard Gaussian matrix satisfies

$$
\mathbb P\left(
\lVert W\rVert_{\mathrm{op}}>2\sqrt n+t
\right)
\le2e^{-t^2/2},
\qquad t\ge0.
$$

In particular, (\lVert W\rVert_{\mathrm{op}}/\sqrt n) has moments of every
fixed order bounded uniformly in (n).

**Lemma 4.2 (the five-query network).**  Fix $0<|h|\le1$ and consider the
actual network in Section 1, exposed in the order

$$
Y^0,\quad D^0,\quad Y^1,\quad D^1,\quad Y^2.
$$

Assume that every population Gram inverted in these five actions and every
nonterminal population innovation Schur complement is at least some
$\gamma>0$.  Then the program can be coupled to the finite-dimensional iid
Gaussian recursion obtained from Lemma 4.1 so that every value field
converges in normalized $L^p$, for every fixed $p<\infty$.  Every empirical
Gram and cross-moment appearing in one of the five regression formulas
converges in $L^p$.  The two terminal output averages converge in expectation.

More explicitly, the empirical list covered by the assertion consists of

$$
Q_{rs}^{(n)}\ (0\le r,s\le2),
\qquad
K_{rs}^{(n)}\ (0\le r,s\le1),
$$

and, at each action, the entries of

$$
Y^\top c/n,\quad C^\top c/n,\quad
D^\top h/n,\quad H^\top h/n
$$

that occur in Lemma 4.1.  No finite-width derivative field is asserted or
needed.  The symbols $\rho$ and $\sigma$ below are exact Gaussian
integration-by-parts rewritings of limits of these cross-moments.

**Proof.**  We give the complete finite-stage argument.

**One compatible coupling.**  Use the conditional residual induction proved
in Lemma 4.1.  At each of the five actions, realize the new orthogonal
residual with one fresh standard Gaussian vector, independent of all earlier
marks and innovations, and use that same vector in the population regression.
Thus the ideal fields are built by a single chronological Gram--Schmidt
recursion.  Its row coordinates are iid copies of one finite Gaussian-marked
recursion, and its column coordinates are iid copies of the other; the
dependence between different times is retained through the regression terms.
The construction uses only inner products, orthogonal projectors, and fresh
iid vectors, so induction also shows that it is equivariant under independent
permutations of row and column indices.  This establishes compatibility and
exchangeability before either is used below.

Here is that population recursion explicitly.  Take independent iid arrays

$$
(U_j,g_{0j},g_{1j})\sim\mathcal N(0,I_3),
\qquad
(A_i,e_{0i},e_{1i},e_{2i})\sim\mathcal N(0,I_4).
$$

Set

$$
\xi_{0i}=e_{0i},
\qquad
\chi_{0j}=\sqrt d\,g_{0j}.
$$

After $H_1$ and its two-time Gram $Q$ have been constructed, set

$$
\xi_{1i}
=Q_{01}\xi_{0i}+\sqrt{Q_{11}-Q_{01}^2}\,e_{1i}.
$$

After $C_1$ and its two-time Gram $K$ have been constructed, set

$$
\chi_{1j}
=\frac{K_{01}}d\chi_{0j}
 +\sqrt{K_{11}-\frac{K_{01}^2}{d}}\,g_{1j}.
$$

Finally, with

$$
q_2=(Q_{02},Q_{12})^\top,
\qquad
\xi_{01,i}=(\xi_{0i},\xi_{1i})^\top,
$$

put

$$
\xi_{2i}
=q_2^\top Q^{-1}\xi_{01,i}
 +\sqrt{Q_{22}-q_2^\top Q^{-1}q_2}\,e_{2i}.
$$

The five ideal raw actions, in their actual reveal order, are

$$
\begin{aligned}
\bar Y_i^0&=\xi_{0i},\\
\bar D_j^0&=\chi_{0j},\\
\bar Y_i^1&=\xi_{1i}+\rho_{10}C_{0i},\\
\bar D_j^1&=\chi_{1j}+\sigma_{10}H_{0j}+\sigma_{11}H_{1j},\\
\bar Y_i^2&=\xi_{2i}+\rho_{20}C_{0i}+\rho_{21}C_{1i}.
\end{aligned}
$$

Between consecutive lines, apply exactly the scalar coordinate updates in
Section 3, including the learned-matrix terms that turn the raw actions into
$z_1,b_1,z_2$.  These formulas prove directly that every row
tuple is the same measurable function of the iid row marks
$(A_i,e_{0i},e_{1i},e_{2i})$, and every column tuple is the same measurable
function of the iid column marks $(U_j,g_{0j},g_{1j})$.  Thus coordinates are
iid within each layer.  The Gaussian source blocks
$(\xi_0,\xi_1,\xi_2)$ and $(\chi_0,\chi_1)$ have covariance $Q^{(2)}$ and
$K$, respectively, by the displayed Gram--Schmidt formulas.  Using the same $e$- and $g$-arrays
for the conditional innovations from Lemma 4.1 defines the promised single,
compatible, permutation-equivariant coupling action by action.

**Base action.**  Let (H^0_j=\phi(U_j)).  The variables (U_j) are iid
standard Gaussians, so Rosenthal gives, for every (p<\infty),

$$
Q_{00}^{(n)}
=\lVert H^0\rVert_{n,2}^2
\longrightarrow
\mathbb E[\phi(G)^2]=1
$$

in $L^p$, with error at most $C_pn^{-1/2}$.  Conditional on $H^0$,
(WH^0/\sqrt n) has iid coordinates with law
(\sqrt{Q_{00}^{(n)}}Z_i).  Use the same iid (Z_i\) for the limiting field
(\xi_i^0=Z_i).  On
({Q_{00}^{(n)}\ge1/2}),

$$
\left|
\sqrt{Q_{00}^{(n)}}-1
\right|
\le
|Q_{00}^{(n)}-1|,
$$

so the normalized $L^p$ coupling error is at most $C_pn^{-1/2}$.  The complement
has arbitrarily high polynomially small probability by applying Rosenthal at
an arbitrarily high moment order.

**Projection error.**  Let (H\in\mathbb R^{n\times r}), with fixed (r),
and suppose (Q=H^\top H/n\) has smallest eigenvalue at least
(\gamma/2).  For (g\sim\mathcal N(0,I_n)),

$$
P_Hg
=HQ^{-1}\frac{H^\top g}{n}.
$$

Conditionally on (H),

$$
Q^{-1}\frac{H^\top g}{n}
\sim
\mathcal N\left(0,\frac{Q^{-1}}n\right).
$$

The triangle inequality therefore gives, for all finite (p,s),

$$
\left\lVert
\lVert P_Hg\rVert_{n,p}
\right\rVert_{L^s(g\mid H)}
\le
C_{p,s,r,\gamma}n^{-1/2}
\sum_{a=1}^r\lVert H_a\rVert_{n,p}.
$$

The same estimate holds for $P_Cg$.  A conditional innovation is
$\tau P_H^\perp g$ or $\tau P_C^\perp g$, so replacing it by $\tau g$ has
error bounded by the preceding display multiplied by $|\tau|$.  The Schur
formula bounds $|\tau|$ by the normalized norm of the current query, whose
moments are part of the induction invariant.  Hölder therefore gives the
claimed $C_{p,s,r,\gamma}n^{-1/2}$ normalized error, with the innovation scale
included.

**Induction invariant and good events.**  Order the five actions
chronologically and put $\mathcal G_{-1}=\Omega$.  After the query for action
$t$ has been constructed but before its matrix action is revealed, define
$\mathcal G_t\subseteq\mathcal G_{t-1}$ by requiring:

1. every empirical Gram inverted in action $t$ has smallest eigenvalue at
   least $\gamma/2$;
2. if the action is nonterminal, the empirical Schur complement of its new
   query is at least $\gamma/2$.

Write

$$
\lVert X\rVert_{L^P(\mathcal G)}
=\left(\mathbb E[|X|^P\mathbf1_{\mathcal G}]\right)^{1/P}.
$$

All quantities defining $\mathcal G_t$ are pre-action observables.  Define a
stopped process which agrees with the exact network while the events hold and,
at the first failure, sets the current and all future stopped action and
coordinate fields to zero.  This convention is only for the proof; the
original network is unchanged.  For every desired moment order $P$, we prove
simultaneously after action $t$, on $\mathcal G_t$,

$$
\left\lVert
\lVert X_n^a-\bar X^a\rVert_{n,P}
\mathbf1_{\mathcal G_t}
\right\rVert_{L^P}
\le \epsilon_{n,P,t},
$$

where $\epsilon_{n,P,t}=O(n^{-1/2})$ before the terminal action and
$\epsilon_{n,P,t}\to0$ at the terminal action, for every field already
constructed, uniform $P$-moment bounds for the corresponding ideal fields
and stopped actual fields, and

$$
\left\lVert A_n-A\right\rVert_{L^P(\mathcal G_t)}
\le \epsilon_{n,P,t}
$$

for every empirical Gram, cross-moment, or coordinate observable already
constructed.

Suppose the invariant holds after action $t-1$.  The next query is a
coordinate function of fields already constructed.  Its squared norm and
all overlaps with the old query blocks are therefore controlled empirical
observables.  First intersect $\mathcal G_{t-1}$ with the event that every
Gram used in action $t$ is within operator norm $\gamma/2$ of its population
Gram.  Entrywise $L^P$ convergence, Weyl's inequality, and Markov's
inequality show that the discarded event has probability at most
$C_{M,t}n^{-M}$ for arbitrary $M$.  On this intersection the current inverse
norms are at most $2/\gamma$.  The current Schur complement is then a
Lipschitz rational function of the controlled norm, overlap, and Gram
entries, by the inverse identity below.  A second application of the same
high-moment Markov bound controls failure of its $\gamma/2$ condition.
Since every relevant population quantity is at least $\gamma$, altogether

$$
\mathbb P(\mathcal G_t^c\cap\mathcal G_{t-1})
\le C_{M,t}n^{-M}.
$$

In either regression formula
of Lemma 4.1, each regression coefficient is a rational function of a fixed
number of empirical Gram and cross-moment entries.  On
$\mathcal G_t$, inversion is Lipschitz because

$$
\lVert A^{-1}-B^{-1}\rVert
\le
\lVert A^{-1}\rVert\,
\lVert A-B\rVert\,
\lVert B^{-1}\rVert,
$$

and both inverse norms are at most $2/\gamma$.  At a nonterminal action the
square root is Lipschitz on $[\gamma/2,\infty)$.  Thus every conditional-mean
coefficient and nonterminal innovation standard deviation has $L^P$ error at
most $C_{P,t}n^{-1/2}$.  For the terminal action no lower bound on the new
Schur complement is required: if its population value is zero, use

$$
|\sqrt x-\sqrt y|\le\sqrt{|x-y|},
\qquad x,y\ge0,
$$

which still gives convergence of the innovation standard deviation.

Use the same fresh iid Gaussian vector for the actual conditional innovation
and the next ideal Gram--Schmidt innovation.  The projection estimate above,
the coefficient errors, and Hölder's inequality give normalized $L^P$
error at most $C_{P,t}n^{-1/2}$ for a nonterminal action.  For the terminal
action the error still tends to zero (and is $O(n^{-1/4})$ when the limiting
Schur complement vanishes), which is sufficient because it is never used in
another regression.

Every coordinate map in this particular network is polynomial-Lipschitz:
this follows by repeated use of the mean-value theorem, bounded derivatives
of $\phi$, and the at-most-linear bound for an undifferentiated $\phi$.
If one such map has polynomial degree $r$, replace $r$ by $r\vee1$ if
necessary.  Hölder gives the precise transfer
estimate

$$
\begin{aligned}
&\left\lVert
\Psi(X_n;\theta_n)-\Psi(\bar X;\theta)
\right\rVert_{n,P}\\
&\quad\le C
\left(1+\lVert X_n\rVert_{n,2Pr}^r
        +\lVert\bar X\rVert_{n,2Pr}^r\right)
\left(
\lVert X_n-\bar X\rVert_{n,2P}
 +|\theta_n-\theta|
\right).
\end{aligned}
$$

The high-moment invariant bounds the first factor.  Applying the induction
at orders $2P$ and $2Pr$ shows that the second factor tends to zero, at rate
$n^{-1/2}$ before the terminal action.  This proves the field estimate at the
next stage.

For any of the finite polynomial-Lipschitz coordinate observables
$\Psi(\bar X_i)$ listed in the lemma, Rosenthal gives

$$
\left\lVert
\frac1n\sum_i\Psi(\bar X_i)
-\mathbb E[\Psi(\bar X)]
\right\rVert_{L^P}
\le C_Pn^{-1/2}.
$$

The preceding coordinate coupling and Hölder bound the $L^P$ norm of the
difference between the actual and ideal empirical averages by a quantity
tending to zero (at rate $n^{-1/2}$ before the terminal action).  This proves
the new Gram and cross-moment estimates.  It also proves
the moment invariant for the new field because the ideal field has all
moments and the coupling error has the chosen higher moment.

This completes one action.  Construct the next query, define
$\mathcal G_{t+1}$ by the two pre-action conditions above, and repeat.  The
list has five actions, so the recursion terminates; no limiting or infinite
induction is involved.

**Probability of leaving the good event.**  Fix any $M>0$ and run the
preceding estimates at moment order $P>2M$.  The pre-action estimate just
proved, entrywise Gram errors, and Weyl's inequality imply

$$
\mathbb P(
\mathcal G_{t+1}^c\cap\mathcal G_t
)
\le C_{M,t}n^{-M}.
$$

There are finitely many stages, so

$$
\mathbb P(\mathcal G_T^c)
\le C_Mn^{-M}
$$

for every prescribed (M).  This argument never asks for an unconditional
moment of an inverse Gram matrix.

**Empirical response coefficients.**  Let $\Theta_{t,n}$ denote the finite
vector of all conditional-mean regression coefficients and innovation
standard deviations in Lemma 4.1 at action $t$, and let $\Theta_t$ be its
population value.  The only empirical coefficient vector used in the stopped
identification is

$$
\widetilde\Theta_{t,n}
=\Theta_{t,n}\mathbf1_{\mathcal G_t}
 +\Theta_t\mathbf1_{\mathcal G_t^c}.
$$

The inverse- and square-root estimates on $\mathcal G_t$ give, for every
finite $P$,

$$
\lVert\widetilde\Theta_{t,n}-\Theta_t\rVert_{L^P}
=\lVert(\Theta_{t,n}-\Theta_t)\mathbf1_{\mathcal G_t}\rVert_{L^P}
\le \epsilon_{n,P,t},
$$

where $\epsilon_{n,P,t}=O(n^{-1/2})$ except for a terminal vanishing
innovation standard deviation, for which it is $O(n^{-1/4})$.  Thus every
empirical response/regression coefficient and innovation scale used in the
identification is uniformly integrable (indeed bounded in every $L^P$) and
converges in every $L^P$.  The activation-response names $\rho,\sigma$ in
Section 3 are exact Gaussian integration-by-parts forms of their population
values, as verified node by node in Section 4.3.  This stopped definition
changes no network variable: on $\mathcal G_t$ it is the exact conditional
coefficient, while on the discarded event the proof works with the raw
network fields and the energy estimate below.  The actual network has no
inverse-Gram coefficient parameter off that representation; it consists only
of the raw fields in Section 1, which are recovered unmodified below.

**Removal of stopping.**  Define

$$
R_n
=1+\frac{\lVert W\rVert_{\mathrm{op}}}{\sqrt n}
 +\frac{\lVert A\rVert_2}{\sqrt n}
 +\frac{\lVert U\rVert_2}{\sqrt n}.
$$

The Gaussian operator-norm tail and Gaussian vector moments imply

$$
\sup_n\mathbb E[R_n^m]<\infty
$$

for every fixed $m$.  Because $|h|\le1$, here is an explicit raw-energy
recursion.  Starting
from

$$
\mathsf u_0=\lVert U\rVert_{n,2},
\qquad
\mathsf a_0=\lVert A\rVert_{n,2},
\qquad
\mathsf w_0=\lVert W\rVert_{\mathrm{op}}/\sqrt n,
$$

define, for $s=0,1$,

$$
\begin{aligned}
\mathsf h_s&=M_\phi(1+\mathsf u_s),\\
\mathsf z_s&=\mathsf w_s\mathsf h_s,\\
\mathsf c_s&=M_\phi\mathsf a_s,\\
\mathsf b_s&=\mathsf w_s\mathsf c_s,\\
\mathsf a_{s+1}&=\mathsf a_s+M_\phi(1+\mathsf z_s),\\
\mathsf u_{s+1}&=\mathsf u_s+M_\phi\mathsf b_s,\\
\mathsf w_{s+1}&=\mathsf w_s+\mathsf c_s\mathsf h_s.
\end{aligned}
$$

For $s=2$, define $\mathsf h_2,\mathsf z_2,\mathsf c_2,\mathsf b_2$ by the
first four rules.  The exact network updates and the inequalities below prove
successively

$$
\lVert u^s\rVert_{n,2}\le\mathsf u_s,\quad
\lVert a^s\rVert_{n,2}\le\mathsf a_s,\quad
\lVert W^s/\sqrt n\rVert_{\mathrm{op}}\le\mathsf w_s,
$$

and the analogous bounds for $H^s,z^s,C^s,b^s$.  Each majorant is a fixed
polynomial with nonnegative coefficients in
$M_\phi,\mathsf u_0,\mathsf a_0,\mathsf w_0$.

For each value field, traverse its exact finite expression tree from the
leaves upward.  At a sum node add the two Euclidean majorants and at a product
node use $\lVert x\odot y\rVert_2\le\lVert x\rVert_2\lVert y\rVert_2$.
This finite traversal produces, for every value field $X$, an explicit
integer $a_X$ and a polynomial $P_X$, independent of $n$, such that

$$
\lVert X\rVert_2
\le n^{a_X}P_X(R_n).
$$

Every step in this traversal uses one of

$$
\lVert (W/\sqrt n)x\rVert_2
\le
\frac{\lVert W\rVert_{\mathrm{op}}}{\sqrt n}\lVert x\rVert_2,
$$

$$
\lVert x\odot y\rVert_2
\le\lVert x\rVert_2\lVert y\rVert_2,
$$

$$
\lVert\phi(x)\rVert_2
\le M_\phi(\sqrt n+\lVert x\rVert_2),
\qquad
\lVert\phi^{(r)}(x)\rVert_\infty\le M_\phi
\quad(1\le r\le12),
$$

and the fact that a scaled rank-one matrix update has norm

$$
\left\lVert\frac h nCH^\top\right\rVert_{\mathrm{op}}
\le |h|\lVert C\rVert_{n,2}\lVert H\rVert_{n,2}.
$$

For (p\ge2),

$$
\lVert X\rVert_{n,p}
\le n^{-1/p}\lVert X\rVert_2.
$$

Choose the power $M$ in
$\mathbb P(\mathcal G_T^c)\le C_Mn^{-M}$ larger than every polynomial power
introduced by the finite list of raw bounds.  Hölder's inequality then makes
the contribution of $\mathcal G_T^c$ tend to zero for every actual value
field and raw empirical observable in the lemma.  Thus those stopped
convergence statements hold for the original network.  The untruncated
rational representation of a conditional coefficient on the discarded event
is neither used nor confused with an actual network parameter.
In particular, every actual empirical Gram and raw cross-moment listed in the
lemma converges in every finite $L^P$ and is therefore uniformly integrable.

**Joint innovations and terminal zero variance.**  At each chronological
stage use a new independent standard Gaussian vector for the orthogonal
innovation.  Define the ideal time block by the same finite Gram--Schmidt
regression on the earlier ideal block.  Induction on the block size shows
that its covariance is exactly the prescribed population Gram; hence this is
one joint coupling, not a collection of incompatible one-query couplings.
If only the final innovation variance is zero, use

$$
|\sqrt{x}-\sqrt y|\le\sqrt{|x-y|},
\qquad x,y\ge0.
$$

The empirical variance still converges, so the terminal innovation converges
in normalized (L^p), possibly at a slower rate.  No later inverse or
response uses that terminal innovation variance.

**Tagged convergence and expectations.**  The construction is equivariant
under independent permutations of row and column indices.  Therefore, for a
coupled exchangeable field,

$$
\mathbb E|X_{n,1}-\bar X_1|^p
=\mathbb E\lVert X_n-\bar X\rVert_{n,p}^p.
$$

This gives joint tagged convergence.  For a terminal coordinate map of
polynomial growth, choose the induction moment order strictly larger than its
growth degree.  More explicitly, the raw-energy recursion gives

$$
|f_n^s|
\le
\lVert a^s\rVert_{n,2}\lVert\phi(z^s)\rVert_{n,2}
\le
M_\phi\mathsf a_s(1+\mathsf z_s).
$$

The right-hand side is a fixed polynomial in random variables having moments
of every order uniformly in $n$.  It therefore gives a uniform
$L^{1+\delta}$ bound for every fixed $\delta>0$.  Hence the empirical
convergence is uniformly integrable and passes to annealed expectations.
This proves the lemma.

### 4.3 Application to the two-step network

Use the raw source-matrix actions

$$
Y^s=WH^s/\sqrt n,
\qquad
D^s=W^\top C^s/\sqrt n.
$$

With $\mathcal E=\sigma(U,A)$, reveal the fields in the order

$$
Y^0,\quad D^0,\quad Y^1,\quad D^1,\quad Y^2.
$$

After (Y^0), the vector (C^0) is measurable; after (D^0), (H^1) is
measurable; after (Y^1) and addition of the known rank-one term in (z^1),
(C^1) is measurable; and after (D^1), (H^2) is measurable.  Hence every
query satisfies the chronological hypothesis of Lemma 4.1.

For reference, the complete finite-action ledger is

| action | new query | new empirical data, besides previously listed Grams | ideal raw action |
|---|---|---|---|
| $Y^0$ | $H^0$ | $Q_{00}^{(n)}$ | $\xi_0$ |
| $D^0$ | $C^0$ | $K_{00}^{(n)},\ (Y^0)^\top C^0/n$ | $\chi_0$ |
| $Y^1$ | $H^1$ | $Q_{01}^{(n)},Q_{11}^{(n)},\ (D^0)^\top H^1/n,\ (C^0)^\top Y^0/n$ | $\xi_1+\rho_{10}C_0$ |
| $D^1$ | $C^1$ | $K_{01}^{(n)},K_{11}^{(n)},\ (Y^s)^\top C^1/n,\ (C^0)^\top Y^s/n$ for $s=0,1$ | $\chi_1+\sigma_{10}H_0+\sigma_{11}H_1$ |
| $Y^2$ | $H^2$ | $Q_{02}^{(n)},Q_{12}^{(n)},Q_{22}^{(n)},\ (D^r)^\top H^2/n,\ (C^r)^\top Y^s/n$ for $r,s=0,1$ | $\xi_2+\rho_{20}C_0+\rho_{21}C_1$ |

Every entry in the third column is an empirical average of one of the
finite polynomial-Lipschitz coordinate maps covered in Lemma 4.2.  The
calculations below evaluate every nontrivial limiting response in the fourth
column; no action or overlap is hidden behind an additional induction.

Section 7 proves that, for (d>0) and every fixed
(0<|h|\le h_\phi), the two population Grams that are inverted before the
terminal action are positive definite.  Lemma 4.2 therefore applies.  It
remains to identify its regression coefficients; this is where reuse of the
same (W) and (W^\top) matters.

Here is the complete rank audit.  The $Y^0$ action uses $Q_{00}=1$.
The $D^0$ action uses $Q_{00}$ and has nonterminal innovation variance
$K_{00}=d$.  The $Y^1$ action uses $Q_{00},K_{00}$ and has nonterminal row
Schur complement

$$
Q_{11}-Q_{01}^2=\det Q.
$$

The $D^1$ action uses the two-time $Q$ and $K_{00}$ and has nonterminal
column Schur complement

$$
K_{11}-K_{01}^2/d=\det K/d.
$$

Finally, $Y^2$ uses the two-time $Q,K$; its new feature innovation is
terminal, so the three-time $Q^{(2)}$ need not be invertible.  Section 7
gives a positive lower bound for every quantity in this list at each fixed
$0<|h|\le h_\phi$.

**Initial transpose action.**  Conditional on (Y^0), Lemma 4.1 gives

$$
D^0
=H^0(Q_{00}^{(n)})^{-1}\frac{(Y^0)^\top C^0}{n}
 +\sqrt{K_{00}^{(n)}}P_{H^0}^\perp g.
$$

The empirical overlap in the first term converges to

$$
\mathbb E[\xi_0A\phi'(\xi_0)]=0
$$

because (A) is centered and independent of (\xi_0).  Also

$$
K_{00}^{(n)}\longrightarrow
\mathbb E[A^2\phi'(G)^2]=d.
$$

The projection error tends to zero by Lemma 4.2, so

$$
D^0\longrightarrow\chi_0,
\qquad
\chi_0\sim\mathcal N(0,d).
$$

This proves rather than assumes the vanishing of the possible initial
transpose response.

**First reused row.**  Apply the row formula with the previously queried
(H^0,C^0).  The coefficient of (C^0) converges to

$$
d^{-1}\mathbb E[\chi_0H_1].
$$

For a centered Gaussian (X\) of variance (d), integration by parts follows
from differentiating its density and gives

$$
\mathbb E[Xg(X)]=d\mathbb E[g'(X)]
$$

for every (C^1) function with polynomial growth.  Applying it conditionally
on (U) yields

$$
\mathbb E[\chi_0H_1]
=d\mathbb E[\partial_{\chi_0}H_1]
=d\rho_{10}.
$$

The remaining row projection and orthogonal innovation combine into a
Gaussian (\xi_1) whose joint covariance with (\xi_0) is (Q).  Hence the
raw source action satisfies

$$
Y^1\longrightarrow\xi_1+\rho_{10}C_0.
$$

Adding the exact learned-matrix term gives

$$
z^1\longrightarrow
\xi_1+(\rho_{10}+hQ_{01})C_0
=\xi_1+L_{10}C_0.
$$

**Critical reused column.**  Let

$$
H=[H^0,H^1],
\qquad
Y=[Y^0,Y^1].
$$

The limiting overlaps with (C_0) are

$$
r_0:=\mathbb E[YC_0]
=
\begin{pmatrix}
0\\
\rho_{10}d
\end{pmatrix}.
$$

The second component is nonzero and cannot be discarded.  Define

$$
\sigma
=
\begin{pmatrix}
\sigma_{10}\\
\sigma_{11}
\end{pmatrix}
=
\begin{pmatrix}
\mathbb E[\partial_{\xi_0}C_1]\\
\mathbb E[\partial_{\xi_1}C_1]
\end{pmatrix}.
$$

Multivariate Gaussian integration by parts says

$$
\mathbb E[\xi C_1]=Q\sigma.
$$

Since only (Y^1) contains the earlier response (\rho_{10}C_0),

$$
r_1:=\mathbb E[YC_1]
=Q\sigma
 +
\begin{pmatrix}
0\\
\rho_{10}K_{01}
\end{pmatrix}.
$$

The column-regression formula of Lemma 4.1 therefore contains

$$
Q^{-1}
\left(
r_1-\frac{K_{01}}d r_0
\right)
=\sigma.
$$

The term proportional to the earlier (D^0), together with the new
orthogonal innovation, forms a centered Gaussian pair
((\chi_0,\chi_1)) with covariance (K).  Thus

$$
D^1
\longrightarrow
\chi_1+\sigma_{10}H_0+\sigma_{11}H_1.
$$

Adding the exact first rank-one matrix update gives

$$
b^1
\longrightarrow
\chi_1+(\sigma_{10}+hK_{01})H_0+\sigma_{11}H_1,
$$

which is precisely the second lower operator.

The response integrands used above are explicit coordinate functions:

$$
\partial_{\xi_0}C_1
=h\phi'(z_0)\phi'(z_1)
 +L_{10}Aa_1\phi''(z_0)\phi''(z_1),
$$

$$
\partial_{\xi_1}C_1=a_1\phi''(z_1).
$$

Bounded activation derivatives and Gaussian moments make both derivatives
integrable.  Thus multivariate Gaussian integration by parts is justified and
identifies $\sigma$ exactly from the already-converged limiting
cross-moment $\mathbb E[\xi C_1]$; no finite-width tangent or empirical
derivative average is being introduced.

**Second lower responses.**  For (r\in\{0,1\}), differentiate the displayed
lower coordinate recursion while holding the other Gaussian coordinate
fixed:

$$
\partial_r u_1
=h\mathbf1_{\{r=0\}}\phi'(u_0),
$$

$$
\partial_r b_1
=\mathbf1_{\{r=1\}}
 +\sigma_{11}\partial_rH_1,
$$

$$
\partial_r u_2
=\partial_r u_1
 +h\left[
(\partial_r b_1)\phi'(u_1)
 +b_1\phi''(u_1)\partial_r u_1
\right],
$$

$$
\partial_rH_2=\phi'(u_2)\partial_r u_2.
$$

Here $H_0$ is independent of both $\chi$-coordinates, and the
$(\sigma_{10}+hK_{01})H_0$ term consequently has zero derivative.  These
formulas define the population quantities $\rho_{2r}$.  They have polynomial
growth, so Gaussian integration by parts is justified.  Lemma 4.2 proves
convergence of every $Q_{r2}^{(n)}$ and of the raw cross-moments in the
terminal regression; $\rho_{2r}$ is the exact integration-by-parts rewriting
of their limits, not an undefined finite-width response.

**Terminal reused row.**  We now compute the second row cancellation rather
than referring to it by analogy.  At a representative coordinate, write

$$
y=
\begin{pmatrix}Y^0\\Y^1\end{pmatrix},
\quad
\xi=
\begin{pmatrix}\xi_0\\\xi_1\end{pmatrix},
\quad
c=
\begin{pmatrix}C_0\\C_1\end{pmatrix},
$$

$$
h_\mathrm{low}
=
\begin{pmatrix}H_0\\H_1\end{pmatrix},
\quad
d_\mathrm{raw}
=
\begin{pmatrix}D^0\\D^1\end{pmatrix},
\quad
\chi=
\begin{pmatrix}\chi_0\\\chi_1\end{pmatrix}.
$$

Let

$$
A_f=
\begin{pmatrix}
0&\rho_{10}\\
0&0
\end{pmatrix},
\qquad
\Sigma^\top=
\begin{pmatrix}
0&0\\
\sigma_{10}&\sigma_{11}
\end{pmatrix}.
$$

The already proved raw limits are exactly

$$
y=\xi+A_f^\top c,
\qquad
d_\mathrm{raw}=\chi+\Sigma^\top h_\mathrm{low}.
$$

Put

$$
q=\mathbb E[h_\mathrm{low}H_2],
\qquad
\rho=
\begin{pmatrix}\rho_{20}\\\rho_{21}\end{pmatrix}.
$$

Gaussian integration by parts in (\xi) and (\chi) gives

$$
R:=\mathbb E[cy^\top]
=\Sigma^\top Q+KA_f,
$$

and

$$
\mathbb E[d_\mathrm{raw}H_2]
=K\rho+\Sigma^\top q.
$$

The coefficient of (c) supplied directly by the row-regression formula is

$$
\begin{aligned}
K^{-1}
\left(
\mathbb E[d_\mathrm{raw}H_2]-RQ^{-1}q
\right)
&=K^{-1}
\left(
K\rho-KA_fQ^{-1}q
\right)\\
&=\rho-A_fQ^{-1}q.
\end{aligned}
$$

The separate row-projection term (y^\top Q^{-1}q) contains

$$
c^\top A_fQ^{-1}q.
$$

It cancels the negative response exactly.  Therefore the total response is
(c^\top\rho), and

$$
Y^2
\longrightarrow
\xi_2+\rho_{20}C_0+\rho_{21}C_1.
$$

The row projection and its final orthogonal innovation construct (\xi_2)
jointly with (\xi_0,\xi_1), with covariance (Q^{(2)}).  A zero final Schur
complement is allowed by the final-variance part of Lemma 4.2.  Adding the two
exact learned-matrix terms yields

$$
z^2
\longrightarrow
\xi_2+(\rho_{20}+hQ_{02})C_0
 +(\rho_{21}+hQ_{12})C_1.
$$

This is the terminal node in Section 3.

All value fields, Grams, and raw cross-moments used in these five queries
have now been covered by Lemma 4.2; every response symbol was obtained by a
justified Gaussian integration by parts from one of those limiting
cross-moments.  Its final uniform-integrability
step applies to (a_1\phi(z_1)) and (a_2\phi(z_2)), because (a_1,a_2,z_1,z_2)
have moments of every fixed order and (\phi) has at most linear growth.
Consequently, for every fixed (0<|h|\le h_\phi),

$$
\lim_{n\to\infty}F_{1,n}(h)=F_1(h),
\qquad
\lim_{n\to\infty}F_{2,n}(h)=F_2(h).
$$

At $h=0$ every finite-width update is the identity and the centered readout
gives $F_{1,n}(0)=F_{2,n}(0)=0$.  The operator definitions give the same
value.  Thus the width-first identification holds at every point of the
closed claimed interval, with no limit exchange at zero.

## 5. Price differentiation at singular covariance

**Lemma 5.1.**  Let $C:[-1,1]\to\mathbb S_+^m$ be $C^5$.  Suppose
$\psi(h,x)$ has all mixed derivatives

$$
\partial_h^j\partial_x^\alpha\psi(h,x),
\qquad
j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5,
$$

that these derivatives are jointly continuous in $(h,x)$, and that each is
bounded, uniformly in $|h|\le1$, by a constant times a fixed polynomial in
$1+\lVert x\rVert$.  Then

$$
N(h)=\Gamma_{C(h)}[\psi_h]
$$

is (C^5), even when (C(h)) changes rank, and

$$
N'(h)
=\Gamma_{C(h)}
\left[
\partial_h\psi_h+\frac12C'(h):D_x^2\psi_h
\right].
$$

Repeated derivatives are obtained by recursively applying the operator on
the right.

**Proof.**  First suppose (\psi_h) is Schwartz in (x), uniformly with its
required (h)-derivatives.  Fourier inversion gives

$$
N(h)
=\frac1{(2\pi)^m}
\int_{\mathbb R^m}
\widehat\psi_h(\zeta)
e^{-\zeta^\top C(h)\zeta/2}\,d\zeta.
$$

Differentiation under the integral is justified by Schwartz decay.  The
derivative of the exponential is

$$
-\frac12\zeta^\top C'(h)\zeta
e^{-\zeta^\top C(h)\zeta/2},
$$

which is the Fourier multiplier of
(\frac12C'(h):D_x^2).  This proves the first derivative formula without
using (C^{-1}).  Repeating the same calculation five times proves all
formal Price derivatives for Schwartz integrands, regardless of the rank of
(C(h)).

For the stated polynomial-growth integrand, choose $R\ge1$ and a smooth cutoff
$\vartheta_R(x)$ equal to one on $\lVert x\rVert\le R$, zero on
$\lVert x\rVert\ge2R$, and with

$$
|D^a\vartheta_R(x)|\le C_aR^{-|a|}.
$$

Mollify $\vartheta_R\psi_h$ in $x$ with a standard mollifier
$\varrho_\epsilon$ supported on $\lVert y\rVert\le\epsilon\le1$.  On each compact set

$$
[-1,1]\times\{x:\lVert x\rVert\le2R\},
$$

joint continuity makes every required mixed derivative uniformly continuous,
so mollification converges uniformly there.  The resulting functions are
Schwartz.  For every required $(j,\alpha)$, product differentiation gives

$$
\partial_h^jD^\alpha(\vartheta_R\psi_h)
=\sum_{\beta\le\alpha}
\binom\alpha\beta
D^\beta\vartheta_R\,
\partial_h^jD^{\alpha-\beta}\psi_h.
$$

Since $R\ge1$, the cutoff derivative bound and the assumed polynomial
envelope bound this sum by $C(1+\lVert x\rVert)^P$, uniformly in $R,h$.
Convolution changes this by at most a fixed factor because
$1+\lVert x-y\rVert\le2(1+\lVert x\rVert)$ on the support of the mollifier.
Thus every approximating derivative is bounded by

$$
C(1+\lVert x\rVert)^P
$$

with $C,P$ independent of $R,\epsilon$, and $|h|\le1$.

Because (C) is continuous on a compact interval,

$$
V:=\sup_{|h|\le1}\operatorname{tr}C(h)<\infty.
$$

If (X_h\sim\mathcal N(0,C(h))), then

$$
\sup_{|h|\le1}\mathbb E(1+\lVert X_h\rVert)^P
\le
\mathbb E(1+\sqrt V\lVert G_m\rVert)^P
<\infty.
$$

Moreover,

$$
\begin{aligned}
&\sup_{|h|\le1}
\mathbb E\left[
(1+\lVert X_h\rVert)^P
\mathbf1_{\{\lVert X_h\rVert>R\}}
\right]\\
&\qquad\le
\mathbb E\left[
(1+\sqrt V\lVert G_m\rVert)^P
\mathbf1_{\{\sqrt V\lVert G_m\rVert>R\}}
\right]
\longrightarrow0.
\end{aligned}
$$

Thus compact uniform convergence and the displayed uniform tail estimate pass
every candidate differentiated expectation, at every order zero through
five, first as $\epsilon\downarrow0$ and then as $R\to\infty$, uniformly in
$h\in[-1,1]$.
Finally, if continuously differentiable
functions and their derivatives converge uniformly, the fundamental theorem
of calculus passes the derivative identity to the limit:

$$
f_k(h)-f_k(0)=\int_0^hf_k'(t),dt
\longrightarrow
\int_0^hg(t),dt.
$$

Applying this observation successively to derivative orders one through five
proves that (N\in C^5) and establishes every repeated Price identity.

## 6. Closed activation-envelope recursion

This section constructs (B_\phi) without using a supremum of an output or
of an unknown covariance trajectory.

### 6.1 Envelope arithmetic

An envelope pair is

$$
(A,p)\in[0,\infty)\times\mathbb N,
$$

representing the bound

$$
|g(x)|\le A(1+\lVert x\rVert)^p.
$$

Define

$$
(A,p)\oplus(B,q)
=(A+B,\max\{p,q\}),
$$

$$
(A,p)\odot(B,q)
=(AB,p+q),
$$

and, for a scalar (\lambda),

$$
\lambda\odot(A,p)=(|\lambda|A,p).
$$

On (|h|\le1), initialize

$$
\mathcal E(1)=(1,0),
\qquad
\mathcal E(h)=(1,0),
\qquad
\mathcal E(x_i)=(1,1).
$$

Use (\oplus) and (\odot) for exact syntactic sums and products.  If
(\mathcal E(g)=(A,p)), use

$$
\mathcal E(\phi(g))
=\bigl(M_\phi(1+A),p\bigr),
$$

because

$$
1+|g(x)|\le(1+A)(1+\lVert x\rVert)^p,
$$

and, for (1\le r\le12), use

$$
\mathcal E(\phi^{(r)}(g))=(M_\phi,0).
$$

Mixed derivatives are generated exactly by the finite rules

$$
\partial(uv)=(\partial u)v+u(\partial v),
$$

$$
\partial\bigl(\phi^{(r)}(u)\bigr)
=\phi^{(r+1)}(u)\partial u,
$$

$$
\partial_h h=1,
\qquad
\partial_{x_i}x_j=\mathbf1_{\{i=j\}},
$$

with all other primitive derivatives zero.  A scalar coefficient (S(h))
constructed at an earlier chronological stage is represented by tokens
(S^{[j]}); once numerical bounds (\bar S_j) have been produced, set

$$
\mathcal E(S^{[j]})=(\bar S_j,0).
$$

The token differentiation rule is

$$
\partial_hS^{[j]}=S^{[j+1]},
\qquad
\partial_{x_i}S^{[j]}=0,
\qquad
0\le j<5.
$$

No derivative of $S^{[5]}$ is requested by the reachable index set.

Thus, for every integrand (\psi_h(x)), every formal mixed derivative is a
finite expression to which (\mathcal E) applies.  Write

$$
E_{j,\alpha}(\psi)
=\mathcal E(\partial_h^j\partial_x^\alpha\psi).
$$

No Bell polynomial is left unspecified: the two displayed derivative rules
generate every term and its integer multiplicity by repeated application.

### 6.2 Gaussian moment and Price majorants

For integers (m\ge1,p\ge0) and (v\ge0), define the explicit Gaussian
moment

$$
\mu_{m,p}(v)
=\mathbb E(1+\sqrt v\lVert G_m\rVert)^p.
$$

It has the finite formula

$$
\mu_{m,p}(v)
=\sum_{r=0}^p
\binom pr
v^{r/2}2^{r/2}
\frac{\Gamma((m+r)/2)}{\Gamma(m/2)}.
$$

For a matrix (A), use the entry-sum norm

$$
\lVert A\rVert_\Sigma=\sum_{i,j}|A_{ij}|.
$$

Consider a chronological Gaussian node

$$
N(h)=\Gamma_{C(h)}[\psi_h]
$$

of dimension (m\).  Suppose the preceding stages have already produced
numbers

$$
\bar c_j\ge
\sup_{|h|\le1}\lVert C^{(j)}(h)\rVert_\Sigma,
\qquad 0\le j\le5.
$$

The occurrence of a supremum here states the property proved by the numerical
majorant; it is not a definition of (\bar c_j).  The numbers themselves are
constructed below from earlier nodes.

For (r=0), and every pair satisfying

$$
j+\left\lceil\frac s2\right\rceil\le5,
$$

define the pair

$$
R^{(0)}_{j,s}
=\bigoplus_{|\alpha|=s}E_{j,\alpha}(\psi).
$$

For

$$
r+j+\left\lceil\frac s2\right\rceil<5,
$$

recurse by

$$
\begin{aligned}
R^{(r+1)}_{j,s}
={}&R^{(r)}_{j+1,s}\\
&\oplus
\bigoplus_{\ell=0}^j
\left[
\frac12\binom j\ell\bar c_{\ell+1}
\odot R^{(r)}_{j-\ell,s+2}
\right].
\end{aligned}
$$

If

$$
R^{(r)}_{0,0}=(A_r,p_r),
$$

define

$$
\overline{\mathcal J}_r(N)
=A_r\mu_{m,p_r}(\bar c_0).
$$

These rules are valid majorants.  To prove this, let

$$
\Psi_0=\psi,
\qquad
\Psi_{r+1}
=\partial_h\Psi_r+\frac12C'(h):D_x^2\Psi_r.
$$

The induction invariant is explicit: if
$R^{(r)}_{j,s}=(A,p)$, then for every multi-index $\alpha$ with
$|\alpha|=s$,

$$
|\partial_h^j\partial_x^\alpha\Psi_r(h,x)|
\le A(1+\lVert x\rVert)^p,
\qquad |h|\le1.
$$

At $r=0$ this holds because the $\oplus$ over all $|\alpha|=s$ dominates
each individual syntactic envelope.  If it holds at $r$, then

$$
\begin{aligned}
\partial_h^j\partial_x^\alpha\Psi_{r+1}
={}&\partial_h^{j+1}\partial_x^\alpha\Psi_r\\
&+\frac12\sum_{\ell=0}^j\binom j\ell
\sum_{a,b}C_{ab}^{(\ell+1)}
\partial_h^{j-\ell}
\partial_x^{\alpha+e_a+e_b}\Psi_r.
\end{aligned}
$$

The entry-sum bound on $C^{(\ell+1)}$ and the envelope sum/product rules give
exactly $R^{(r+1)}_{j,s}$.  Thus the invariant holds by induction; the
$\sum_{a,b}$ contraction introduces no omitted dimension factor because it
is already absorbed by $\lVert C^{(\ell+1)}\rVert_\Sigma$.

Lemma 5.1 gives

$$
N^{(r)}(h)=\Gamma_{C(h)}[\Psi_r(h,\cdot)].
$$

Leibniz differentiation of (C':D^2\Psi_r) gives exactly the displayed
recursion for (R^{(r+1)}_{j,s}).  The entry-sum norm bounds every matrix
contraction.  If (X=C^{1/2}G_m), then

$$
\lVert X\rVert
\le\sqrt{\lVert C\rVert_{\mathrm{op}}}\lVert G_m\rVert
\le\sqrt{\bar c_0}\lVert G_m\rVert.
$$

Consequently,

$$
\sup_{|h|\le1}|N^{(r)}(h)|
\le\overline{\mathcal J}_r(N).
$$

### 6.3 Covariance and response constructors

If the entries of a new covariance matrix are earlier Gaussian nodes

$$
C_{ab}(h)=N_{ab}(h),
$$

define, numerically,

$$
\bar c_j^{\mathrm{new}}
=\sum_{a,b}\overline{\mathcal J}_j(N_{ab}),
\qquad 0\le j\le5.
$$

The preceding bound proves that these numbers have the required covariance
property.  If a response coefficient is an earlier Gaussian node (S), set

$$
\bar S_j=\overline{\mathcal J}_j(S).
$$

For

$$
L(h)=S(h)+hQ(h),
$$

define

$$
\bar L_j
=\bar S_j+\bar Q_j+j\bar Q_{j-1},
\qquad
\bar Q_{-1}=0.
$$

Indeed,

$$
\frac{d^j}{dh^j}(hQ)
=hQ^{(j)}+jQ^{(j-1)},
$$

and (|h|\le1).

### 6.4 Finite chronological evaluation

The following list completely specifies the numerical recursion.

1. Compute the Gaussian moment

   $$
   d=\mathbb E[\phi'(G)^2].
   $$

   For the first lower block (C=\operatorname{diag}(1,d)), initialize

   $$
   \bar c_0^{\mathcal L_1}=1+M_\phi^2,
   \qquad
   \bar c_j^{\mathcal L_1}=0
   \quad(1\le j\le5).
   $$

2. Generate the exact expressions in Section 3.1.  Apply Sections 6.1--6.2
   to every

   $$
   Q_{rs}=\Gamma_{\operatorname{diag}(1,d)}[H_rH_s]
   $$

   and to

   $$
   \rho_{10}
   =\Gamma_{\operatorname{diag}(1,d)}
   [\partial_{\chi_0}H_1].
   $$

   Denote their numerical derivative bounds by
   (\bar Q_{rs,j}) and (\bar\rho_{10,j}), and construct
   (\bar L_{10,j}) by Section 6.3.

3. Generate the exact expressions in Section 3.2, treating the already
   bounded scalar jets as coefficient tokens.  For the covariance
   (\operatorname{diag}(1,Q)), set

   $$
   \bar c_j^{\mathcal T_1}
   =\mathbf1_{\{j=0\}}
   +\sum_{r,s=0}^1\bar Q_{rs,j}.
   $$

   Apply the Price majorant to

   $$
   F_1,
   \qquad
   K_{rs}=\mathbb E[C_rC_s],
   \qquad
   \sigma_{1r}=\mathbb E[\partial_{\xi_r}C_1].
   $$

   This produces numerical bounds for every derivative through order five of
   (F_1,K,\sigma).

4. Generate (b_1,u_2,H_2) from Section 3.3.  For the second lower covariance
   (\operatorname{diag}(1,K)), set

   $$
   \bar c_j^{\mathcal L_2}
   =\mathbf1_{\{j=0\}}
   +\sum_{r,s=0}^1\bar K_{rs,j}.
   $$

   Apply the majorant to every (Q_{r2}) and (\rho_{2r}), and construct
   (L_{20},L_{21}) with the (L)-rule.  Together with the old (Q)-entries,
   these are numerical derivative bounds for all entries of (Q^{(2)}).

5. Generate (z_2,a_2) from Section 3.4.  For
   (\operatorname{diag}(1,Q^{(2)})), set

   $$
   \bar c_j^{\mathcal T_2}
   =\mathbf1_{\{j=0\}}
   +\sum_{r,s=0}^2\bar Q_{rs,j}.
   $$

   Apply the majorant to (F_2=\mathbb E[a_2\phi(z_2)]).

Finally define

$$
\overline{\mathcal J}_{1,5}
=\overline{\mathcal J}_5(F_1),
\qquad
\overline{\mathcal J}_{2,5}
=\overline{\mathcal J}_5(F_2),
$$

and

$$
B_\phi
=\frac1{120}
\left(
\overline{\mathcal J}_{1,5}
 +\frac{\overline{\mathcal J}_{2,5}}{32}
\right).
$$

This is a completely specified finite recursion.  Each Gaussian covariance is
constructed strictly before the node that uses it, so there is no cycle.  The
index set

$$
\left\{(r,j,s):
r+j+\left\lceil\frac s2\right\rceil\le5
\right\}
$$

is finite.  Each formal derivative produces a finite sum.  On the reachable
set $j+\lceil s/2\rceil\le5$ one has $j+s\le10$.  Each direct $h$-derivative
or spatial derivative raises the order of a composed activation derivative
by at most one.  A response integrand starts at derivative order at most two,
so no activation derivative above $\phi^{(12)}$ occurs.  Therefore the
recursion terminates and returns a
finite number using only (M_\phi), integer arithmetic, and the explicitly
displayed Gaussian moments (\mu_{m,p}), with (m\le4).

The same recursion verifies all domination hypotheses of Lemma 5.1 at every
chronological node.  It therefore proves, rather than assumes, that the
limiting (F_1,F_2) are (C^5) at the singular covariance (h=0).

## 7. Explicit fixed-step rank radius

The cavity proof only inverts the two-time feature Gram (Q) and the
two-time cotangent Gram (K).  Their rank is certified quantitatively from
the same activation data.

Let

$$
\begin{aligned}
e&=\mathbb E[\phi'(G)^4],
&m&=\mathbb E[\phi(G)\phi''(G)\phi'(G)^2],\\
s&=\mathbb E[\phi''(G)^2\phi'(G)^2],
&\ell&=\mathbb E[\phi(G)^2\phi'(G)^2],\\
t&=\mathbb E[\phi''(G)^2],
&c&=1+d,
\end{aligned}
$$

and define

$$
\tau=\ell+2cm+3c^2s+edt.
$$

The direct derivatives in Section 8 give

$$
Q_{01}''(0)=dm,
\qquad
Q_{11}''(0)=2d(e+m),
$$

and hence

$$
(\det Q)''(0)=2de.
$$

They also give the (K)-derivatives displayed in Section 8, whose direct
substitution yields

$$
(\det K)''(0)=2d\tau.
$$

Both determinants are even functions of (h).

The numerical recursion in Section 6 already supplies bounds
(\bar Q_{rs,j}) and (\bar K_{rs,j}) for (|h|\le1).  Define

$$
D_Q
=\bar Q_{11,4}
 +\sum_{a=0}^4
\binom4a\bar Q_{01,a}\bar Q_{01,4-a},
$$

and

$$
D_K
=d\bar K_{11,4}
 +\sum_{a=0}^4
\binom4a\bar K_{01,a}\bar K_{01,4-a}.
$$

Since

$$
\det Q=Q_{11}-Q_{01}^2,
\qquad
\det K=dK_{11}-K_{01}^2,
$$

Leibniz's rule proves

$$
\sup_{|h|\le1}|(\det Q)^{(4)}(h)|\le D_Q,
\qquad
\sup_{|h|\le1}|(\det K)^{(4)}(h)|\le D_K.
$$

For (d>0), define

$$
r_Q
=\min\left\{
1,
\sqrt{\frac{12de}{1+D_Q}}
\right\},
$$

$$
r_K
=\min\left\{
1,
\sqrt{\frac{12d\tau}{1+D_K}}
\right\},
$$

and

$$
h_\phi=\min\{r_Q,r_K\}.
$$

These numbers are strictly positive.  Indeed, (d>0) implies (e>0).
Moreover, if (A,B,G) are independent standard Gaussians and

$$
V
=\phi(G)\phi'(G)
 +\sqrt{de}\,AB\phi''(G)
 +cA^2\phi'(G)\phi''(G),
$$

then expansion using
$\mathbb E[A^2]=1$, $\mathbb E[A^4]=3$, and the centered independent
(B) gives

$$
\mathbb E[V^2]=\tau.
$$

If $t>0$, the component containing $B$ has positive squared expectation
$d e t>0$, so $\tau>0$.  If $t=0$, continuity gives
$\phi''\equiv0$, so $\phi$ is affine; since $d>0$ and
$\mathbb E[\phi(G)^2]=1$, one then has
$\tau=\ell=d>0$.

Taylor's formula through order three and evenness give

$$
\left|
\det Q(h)-deh^2
\right|
\le\frac{D_Q}{24}|h|^4,
$$

$$
\left|
\det K(h)-d\tau h^2
\right|
\le\frac{D_K}{24}|h|^4.
$$

Therefore, for (0<|h|\le h_\phi),

$$
\det Q(h)\ge\frac12deh^2>0,
$$

$$
\det K(h)\ge\frac12d\tau h^2>0.
$$

For an explicit eigenvalue lower bound, let

$$
T_Q=1+\bar Q_{11,0},
\qquad
T_K=d+\bar K_{11,0}.
$$

A positive-semidefinite (2\times2) matrix satisfies
(\lambda_{\min}\ge\det/\operatorname{tr}).  Hence, at each fixed nonzero
(h) in the interval, all inverses in Section 4 are controlled by

$$
\gamma_\phi(h)
=\min\left\{
1,d,
\frac{deh^2}{2T_Q},
\frac{d\tau h^2}{2T_K}
\right\}>0.
$$

The constants in the finite-width coupling may diverge as (h\to0).  This
does not exchange the limits: Section 4 is applied separately at each fixed
nonzero (h), and only afterward is the already identified operator program
differentiated at zero.

## 8. Direct third derivatives of the limiting operators

Let

$$
\phi_r=\phi^{(r)}(G).
$$

In addition to the moments already defined, set

$$
j=\mathbb E[\phi_3\phi_1^3],
\qquad
b=\mathbb E[\phi_0\phi_2],
\qquad
r=\mathbb E[\phi_1\phi_3].
$$

Thus the nine activation moments are

$$
\begin{aligned}
d&=\mathbb E[\phi_1^2],
&e&=\mathbb E[\phi_1^4],
&m&=\mathbb E[\phi_0\phi_2\phi_1^2],\\
j&=\mathbb E[\phi_3\phi_1^3],
&s&=\mathbb E[\phi_2^2\phi_1^2],
&\ell&=\mathbb E[\phi_0^2\phi_1^2],\\
b&=\mathbb E[\phi_0\phi_2],
&r&=\mathbb E[\phi_1\phi_3],
&t&=\mathbb E[\phi_2^2].
\end{aligned}
$$

Define

$$
c=1+d,
\qquad
\beta=b+cr,
\qquad
\delta=d+ct,
$$

$$
k=d+\beta+\delta=2d+b+c(r+t).
$$

The parity can be checked without differentiating.  Under

$$
h\mapsto-h,
\qquad
A\mapsto-A,
\qquad
(\chi_0,\chi_1)\mapsto(-\chi_0,-\chi_1).
$$

the first lower fields $u_1,H_1$ are unchanged, so $Q$ is even, while the
$\chi$-derivative defining $\rho_{10}$ changes sign and hence $L_{10}$ is
odd.  In the first top stage, $z_0,z_1$ are unchanged while
$C_0,C_1,a_1$ change sign.  Thus $K$ is even, $\sigma$ is odd, and $F_1$ is
odd.  In the second lower stage $b_1$ changes sign, so $u_2,H_2$ are
unchanged; hence the enlarged $Q$ is even and $\rho_2,L_2$ are odd.  In the
last top stage $z_2$ is unchanged and $a_2$ changes sign, so $F_2$ is odd.
The Gaussian laws are invariant under the two sign changes above.  Therefore
$Q,K$ are even, every $\rho,\sigma,L$ is odd, and $F_1,F_2$ are odd.  All covariance
first and third derivatives vanish at zero.

If (C) is even, the third Price derivative at zero reduces to

$$
\left.
\frac{d^3}{dh^3}\Gamma_{C(h)}[\psi_h]
\right|_{h=0}
=\mathbb E[\partial_h^3\psi_0]
 +\frac32C''(0):\mathbb E[D_x^2\partial_h\psi_0].
$$

This follows by applying the recursion in Lemma 5.1 three times.  An
off-diagonal covariance entry occurs twice in the colon product.

### 8.1 First lower node

At a fixed (U), put

$$
g=\phi(U),
\quad
p=\phi'(U),
\quad
q=\phi''(U),
\quad
r_3=\phi'''(U).
$$

Since

$$
H_1=\phi(U+h\chi_0p),
\qquad
\mathbb E[\chi_0^2]=d,
$$

two direct derivatives give

$$
Q_{01}''(0)
=\mathbb E[gq(\chi_0p)^2]
=dm,
$$

$$
Q_{11}''(0)
=\mathbb E[2(p^2+gq)(\chi_0p)^2]
=2d(e+m).
$$

Also

$$
\rho_{10}
=h\mathbb E[\phi'(U+h\chi_0p)p].
$$

Direct differentiation at zero, with all odd Gaussian moments vanishing,
gives

$$
\rho_{10}'(0)=d,
\qquad
\rho_{10}'''(0)=3dj.
$$

Because (L_{10}=\rho_{10}+hQ_{01}),

$$
L_{10}'(0)=c,
\qquad
L_{10}'''(0)=3d(m+j).
$$

### 8.2 First top covariance and responses

For fixed Gaussian coordinates (x,y), write

$$
C_0=A\phi'(x),
$$

$$
C_1
=\bigl(A+h\phi(x)\bigr)
\phi'\bigl(y+L_{10}A\phi'(x)\bigr).
$$

At fixed (x,y,A), direct differentiation gives

$$
\mathbb E[\partial_h^2(C_0C_1)]_{h=0}
=2cm+3c^2j.
$$

Indeed, before expectation the two surviving terms are

$$
2cA^2\phi(x)\phi'(x)^2\phi''(y)
$$

and

$$
c^2A^4\phi'(x)^3\phi'''(y),
$$

and (\mathbb E[A^2]=1), (\mathbb E[A^4]=3).  The zeroth integrand is

$$
A^2\phi'(x)\phi'(y).
$$

Its relevant Hessian expectations at (x=y=G) are (t) in the mixed
direction and (r) in the (y,y) direction.  The second-order Price formula
therefore gives

$$
K_{01}''(0)
=2cm+3c^2j+dmt+d(e+m)r.
$$

For (K_{11}), the fixed-coordinate integrand is

$$
\bigl(A+h\phi(x)\bigr)^2
\phi'\bigl(y+L_{10}A\phi'(x)\bigr)^2.
$$

Its direct second derivative has expectation

$$
2\ell+8cm+6c^2(s+j).
$$

Indeed, its three fixed-coordinate terms are

$$
2\phi(x)^2\phi'(y)^2,
$$

$$
8cA^2\phi(x)\phi'(x)\phi'(y)\phi''(y),
$$

and

$$
2c^2A^4\phi'(x)^2
\left(\phi''(y)^2+\phi'(y)\phi'''(y)\right).
$$

After coalescing $x=y=G$, their expectations are respectively
$2\ell$, $8cm$, and $6c^2(s+j)$.

At zero the integrand is (A^2\phi'(y)^2), whose (y,y) Hessian has
expectation (2(t+r)).  Hence

$$
K_{11}''(0)
=2\ell+8cm+6c^2(s+j)
 +2d(e+m)(t+r).
$$

The response derivatives follow directly from

$$
\partial_{\xi_0}C_1
=h\phi'(z_0)\phi'(z_1)
 +L_{10}Aa_1\phi''(z_0)\phi''(z_1),
$$

and

$$
\partial_{\xi_1}C_1=a_1\phi''(z_1).
$$

Using (L_{10}'(0)=c) gives

$$
\sigma_{10}'(0)=d+ct=\delta,
\qquad
\sigma_{11}'(0)=b+cr=\beta.
$$

For clarity, the first formula consists of the expectations of
$\phi'(x)\phi'(y)$ and $cA^2\phi''(x)\phi''(y)$, namely $d+ct$; the second
consists of $\phi(x)\phi''(y)$ and
$cA^2\phi'(x)\phi'''(y)$, namely $b+cr$.

Consequently the first derivative of the deterministic part of (b_1) is

$$
K_{01}(0)+\sigma_{10}'(0)+\sigma_{11}'(0)
=d+\delta+\beta=k.
$$

### 8.3 One-step output

For fixed (x,y,A), let

$$
\psi_h
=\bigl(A+h\phi(x)\bigr)
\phi\bigl(y+L_{10}A\phi'(x)\bigr).
$$

At zero its first integrand derivative is

$$
\psi_1
=\phi(x)\phi(y)
 +cA^2\phi'(x)\phi'(y).
$$

At (x=y=G),

$$
\mathbb E[\partial_{xy}\psi_1]=\delta,
\qquad
\mathbb E[\partial_{yy}\psi_1]=\beta.
$$

The first equality is $d+ct$: differentiating once in each coordinate gives
$\phi'(x)\phi'(y)+cA^2\phi''(x)\phi''(y)$.  The second is $b+cr$:
differentiating twice in $y$ gives
$\phi(x)\phi''(y)+cA^2\phi'(x)\phi'''(y)$.

The fixed-coordinate third derivative is obtained from

$$
z_1'(0)=cA\phi'(x),
\qquad
z_1''(0)=0,
\qquad
z_1'''(0)=3d(m+j)A\phi'(x).
$$

Product and chain differentiation give

$$
\mathbb E[\partial_h^3\psi_0]
=3c^2m+3c^3j+3d^2(m+j).
$$

Explicitly, the three fixed-coordinate atoms are

$$
3c^2A^2\phi(x)\phi'(x)^2\phi''(y),
$$

$$
c^3A^4\phi'(x)^3\phi'''(y),
$$

and

$$
L_{10}'''(0)A^2\phi'(x)\phi'(y).
$$

Their expectations are $3c^2m$, $3c^3j$, and
$dL_{10}'''(0)=3d^2(m+j)$, respectively.

The third Price formula now gives

$$
\begin{aligned}
F_1'''(0)
={}&3c^2m+3c^3j+3d^2(m+j)\\
&+3dm\delta+3d(e+m)\beta.
\end{aligned}
$$

Define

$$
S_\phi
=3c^2m+3c^3j+3de\beta+3dkm+3d^2j.
$$

Using (k=d+\beta+\delta) in the previous display proves

$$
F_1'''(0)=S_\phi.
$$

At first order there is no covariance correction because $Q'(0)=0$, and
$\mathbb E[\psi_1]=1+cd$.  Hence

$$
F_1'(0)=1+d+d^2.
$$

### 8.4 Second lower node

At (h=0), the pair ((\chi_0,\chi_1)) collapses to
((X,X)), where (X\sim\mathcal N(0,d)).  Direct differentiation of the
lower recursion gives

$$
u_1'(0)=\chi_0p,
$$

$$
u_2'(0)=(\chi_0+\chi_1)p,
$$

and

$$
u_2''(0)=2kgp+2\chi_0\chi_1pq.
$$

Substitution into the second derivatives of
(\phi(u_r)\phi(u_2)) gives

$$
Q_{02}''(0)=2k\ell+6dm,
$$

$$
Q_{12}''(0)=2k\ell+7dm+4de,
$$

$$
Q_{22}''(0)=4k\ell+12dm+8de.
$$

For completeness, the individual contributions are as follows.  The second
derivative of (\phi(u_2)) at the collapsed state is

$$
6X^2p^2q+2kgp^2.
$$

Multiplication by (g) gives the (Q_{02}) formula.  In (Q_{12}), the
second derivative of (\phi(u_1)) contributes (dm), the cross product of
the two first derivatives contributes (4de), and the (Q_{02}) terms remain.
Doubling the square and product contributions gives (Q_{22}).

The response (\rho_{21}) has the exact form

$$
\rho_{21}
=h\mathbb E[\phi'(u_2)\phi'(u_1)].
$$

The second derivative at zero of its expectation after removing the leading
(h) is

$$
6ds+5dj+2km.
$$

Indeed, differentiating the product produces respectively

$$
6X^2p^2q^2,
\qquad
5X^2p^3r_3,
\qquad
2kgp^2q.
$$

Therefore

$$
\rho_{21}'''(0)=18ds+15dj+6km.
$$

For (\rho_{20}), direct differentiation in (\chi_0) gives

$$
\rho_{20}
=h\mathbb E\left[
\phi'(u_2)p
\left(
1+h b_1\phi''(u_1)
 +h\sigma_{11}\phi'(u_1)^2
\right)
\right].
$$

The second derivative at zero of the expectation after removing the leading
(h) is

$$
6d(s+j)+4km+2\beta e.
$$

The four contributions before expectation are

$$
6X^2p^2q^2,
\qquad
6X^2p^3r_3,
\qquad
4kgp^2q,
\qquad
2\beta p^4.
$$

Thus

$$
\rho_{20}'''(0)
=18d(s+j)+12km+6\beta e.
$$

The covariance-(K'') Price corrections at this node vanish: the zeroth
integrands for the (Q_{r2}) calculations are independent of
((\chi_0,\chi_1)), and the first response integrands are (p^2), also
independent of those coordinates.

Since (L_{2r}=\rho_{2r}+hQ_{r2}),

$$
\begin{aligned}
L_{20}'''(0)
={}&18ds+18dj+18dm\\
&+12km+6k\ell+6\beta e,
\end{aligned}
$$

and

$$
\begin{aligned}
L_{21}'''(0)
={}&18ds+15dj+21dm\\
&+6km+6k\ell+12de.
\end{aligned}
$$

Also

$$
L_{20}'(0)=L_{21}'(0)=c.
$$

### 8.5 Two-step output

At fixed $(x_0,x_1,x_2,A)$, coalescence at $h=0$ gives
$x_0=x_1=x_2=G$.  The first top cotangent has fixed-coordinate derivatives

$$
C_1'(0)=\phi(G)\phi'(G)
 +cA^2\phi'(G)\phi''(G),
$$

$$
C_1''(0)=2cA\phi(G)\phi'(G)\phi''(G)
 +c^2A^3\phi'(G)^2\phi'''(G).
$$

Using $z_2=x_2+L_{20}C_0+L_{21}C_1$ now gives, term by term,

$$
z_1'(0)=cA\phi'(x_0),
$$

$$
z_2'(0)=cA\bigl(\phi'(x_0)+\phi'(x_1)\bigr),
$$

$$
z_2''(0)
=2c\left[
\phi(x_0)\phi'(x_1)
 +cA^2\phi'(x_0)\phi''(x_1)
\right]
$$

after coalescing the coordinates at zero, and

$$
\begin{aligned}
z_2'''(0)
={}&\bigl(L_{20}'''(0)+L_{21}'''(0)\bigr)A\phi'(G)\\
&+6c^2A\phi(G)\phi'(G)\phi''(G)\\
&+3c^3A^3\phi'(G)^2\phi'''(G).
\end{aligned}
$$

The readout derivatives are

$$
a_2'(0)=2\phi(G),
\qquad
a_2''(0)=2cA\phi'(G)^2,
$$

$$
a_2'''(0)=3c^2A^2\phi'(G)^2\phi''(G).
$$

Substituting these expressions into

$$
\begin{aligned}
\partial_h^3(a_2\phi(z_2))
={}&a_2'''\phi(z_2)
 +3a_2''\phi'(z_2)z_2'\\
&+3a_2'\left(
\phi''(z_2)(z_2')^2+\phi'(z_2)z_2''
\right)\\
&+a_2\left(
\phi'''(z_2)(z_2')^3
 +3\phi''(z_2)z_2'z_2''
 +\phi'(z_2)z_2'''
\right)
\end{aligned}
$$

and using (\mathbb E[A^2]=1), (\mathbb E[A^4]=3) gives the fixed-coordinate
contribution

$$
\begin{aligned}
E_3={}&12c^2e+12c\ell+57c^2m
 +33c^3j+36c^3s\\
&+d\bigl(L_{20}'''(0)+L_{21}'''(0)\bigr).
\end{aligned}
$$

Here no term is suppressed.  In the order of the six summands in the
preceding product-rule display, their expectations are

$$
\begin{array}{c|l}
\text{summand}&\text{expectation}\\\hline
a_2'''\phi(z_2)&3c^2m\\
3a_2''\phi'(z_2)z_2'&12c^2e\\
3a_2'\{\phi''(z_2)(z_2')^2+\phi'(z_2)z_2''\}
&36c^2m+12c\ell\\
a_2\phi'''(z_2)(z_2')^3&24c^3j\\
3a_2\phi''(z_2)z_2'z_2''&12c^2m+36c^3s\\
a_2\phi'(z_2)z_2'''&d(L_{20}'''+L_{21}''')+6c^2m+9c^3j.
\end{array}
$$

Adding the right column gives exactly $E_3$.

The first terminal integrand derivative before coalescing the Gaussian
coordinates is

$$
\psi_1
=\bigl(\phi(x_0)+\phi(x_1)\bigr)\phi(x_2)
 +cA^2
\bigl(\phi'(x_0)+\phi'(x_1)\bigr)\phi'(x_2).
$$

Its only relevant Hessian expectations are

$$
\mathbb E[\partial_{01}\psi_1]=0,
$$

$$
\mathbb E[\partial_{11}\psi_1]=\beta,
\qquad
\mathbb E[\partial_{22}\psi_1]=2\beta,
$$

$$
\mathbb E[\partial_{02}\psi_1]
=\mathbb E[\partial_{12}\psi_1]
=\delta.
$$

Indeed, the $(0,1)$ derivative vanishes because both terms of $\psi_1$ are
sums, rather than products, in $x_0,x_1$; $\partial_{11}$ gives
$b+cr=\beta$; $\partial_{22}$ gives twice that; and each of
$\partial_{02},\partial_{12}$ gives $d+ct=\delta$.

The third Price correction is therefore

$$
3\left(
\frac{Q_{11}''(0)}2+Q_{22}''(0)
\right)\beta
 +3\bigl(Q_{02}''(0)+Q_{12}''(0)\bigr)\delta.
$$

First, the already derived response and feature terms sum to

$$
\begin{aligned}
L_{20}'''(0)+L_{21}'''(0)
={}&36ds+33dj+39dm+18km\\
&+12k\ell+6\beta e+12de.
\end{aligned}
$$

Second, substituting the three feature-covariance derivatives into the Price
correction gives

$$
\begin{aligned}
&3\{d(e+m)+4k\ell+12dm+8de\}\beta\\
&\qquad+3\{4k\ell+13dm+4de\}\delta.
\end{aligned}
$$

Adding these two displays to $E_3$ and using
$k=d+\beta+\delta$ gives

$$
\begin{aligned}
F_2'''(0)={}&
12c^2e+12c\ell+57c^2m
 +33c^3j+36c^3s\\
&+36d^2s+33d^2j+57dkm+33de\beta\\
&+12cedt+24ed^2+12k^2\ell.
\end{aligned}
$$

Define the activation polynomial

$$
\begin{aligned}
H_\phi={}&
c^2e+c\ell+2c^2m+3c^3s+cedt\\
&+2ed^2+3d^2s+k^2\ell+2dkm.
\end{aligned}
$$

There is no further implicit cancellation.  Expanding the two proposed
pieces gives

$$
\begin{aligned}
11S_\phi={}&33c^2m+33c^3j+33de\beta
 +33dkm+33d^2j,\\
12H_\phi={}&12c^2e+12c\ell+24c^2m+36c^3s
 +12cedt\\
&+24ed^2+36d^2s+12k^2\ell+24dkm.
\end{aligned}
$$

Their sum is exactly the preceding formula for $F_2'''(0)$.  Hence

$$
F_2'''(0)=11S_\phi+12H_\phi.
$$

At first order the terminal covariance has zero derivative, while the fixed
integrand derivative has expectation $2+2cd$.  Therefore

$$
F_2'(0)=2(1+d+d^2).
$$

No initialization derivative of a finite-width network has been used in this
section.

It follows that

$$
\Delta'(0)=0,
$$

and

$$
\Delta'''(0)
=\frac18F_2'''(0)-F_1'''(0)
=\frac38S_\phi+\frac32H_\phi.
$$

Therefore the explicit cubic coefficient is

$$
\kappa_\phi
=\frac{\Delta'''(0)}6
=\frac{4H_\phi+S_\phi}{16}.
$$

## 9. Explicit fifth-order remainder and conclusion

Sections 5 and 6 prove that $F_1,F_2\in C^5([-1,1])$.  Their parity proves
that $\Delta$ is odd, while Section 8 proves

$$
\Delta'(0)=0,
\qquad
\frac{\Delta'''(0)}6=\kappa_\phi.
$$

Oddness also gives

$$
\Delta(0)=\Delta''(0)=\Delta^{(4)}(0)=0.
$$

Taylor's formula with integral remainder through order four therefore gives,
for every $|\eta|\le h_\phi$,

$$
\Delta(\eta)-\kappa_\phi\eta^3
=\frac1{24}
\int_0^\eta
(\eta-t)^4\Delta^{(5)}(t)\,dt.
$$

The numerical majorants in Section 6 give, without reference to an output
supremum,

$$
|F_1^{(5)}(t)|
\le\overline{\mathcal J}_{1,5}
\qquad(|t|\le1),
$$

and

$$
|F_2^{(5)}(t/2)|
\le\overline{\mathcal J}_{2,5}
\qquad(|t|\le1).
$$

Consequently,

$$
|\Delta^{(5)}(t)|
\le
\overline{\mathcal J}_{1,5}
+\frac1{32}\overline{\mathcal J}_{2,5}.
$$

Taking absolute values in the integral and using

$$
\frac1{24}\int_0^{|\eta|}(|\eta|-t)^4\,dt
=\frac{|\eta|^5}{120}
$$

proves

$$
\left|
\Delta(\eta)-\kappa_\phi\eta^3
\right|
\le
B_\phi|\eta|^5,
$$

where $B_\phi$ is the finite, explicitly terminating recursion in Section
6.4.

Now suppose

$$
|\eta|
\le
\min\left\{
h_\phi,
\sqrt{\frac{\varepsilon}{1+B_\phi}}
\right\}.
$$

Then

$$
B_\phi|\eta|^2
\le
\frac{B_\phi}{1+B_\phi}\varepsilon
\le\varepsilon.
$$

Therefore

$$
\begin{aligned}
|\Delta(\eta)|
&\le|\kappa_\phi||\eta|^3+B_\phi|\eta|^5\\
&\le(|\kappa_\phi|+\varepsilon)|\eta|^3.
\end{aligned}
$$

Finally, if $d=0$, continuity and full support of the Gaussian law imply
$\phi'\equiv0$.  RMS normalization then gives the constant activation
$\phi\equiv1$ or $\phi\equiv-1$.  The hidden weights never move, and only
the readout changes.  Directly,

$$
F_1(h)=h,
\qquad
F_2(h)=2h.
$$

Thus

$$
F_2(\eta/2)-F_1(\eta)=0.
$$

In this case set

$$
\kappa_\phi=0,
\qquad
B_\phi=0,
\qquad
h_\phi=1.
$$

This completes both the pointwise fixed-step width identification and the
activation-explicit quantitative remainder estimate.
