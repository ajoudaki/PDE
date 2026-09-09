# The four-versus-two width-first rung

This note uses exactly the finite-width network and normalization of
`../temporary_quantitative_width_first_bound_rung3/PROOF.md`.  It closes the
only new fixed-width issue at the fourth iterate: the nonterminal four-time
feature and cotangent Grams.  In fact, a conditional-innovation argument
proves their strict positivity for every nonzero step and avoids taking seven
derivatives of a Gram.  Consequently the same (C^{12}) activation class is
enough.

## Theorem

Let

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

and suppose

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
\]

At every fixed step (h), first take the width limit of the actual network,
and call the limiting expected output after (N) recomputed ascent steps
(F_N(h)).  Set

\[
 \Delta_{42}(\eta)=F_4(\eta)-F_2(2\eta).
\]

Use the Gaussian activation moments and the quantities (S_\phi,H_\phi)
defined in the preceding proof, and put

\[
 K_\phi=S_\phi+4H_\phi .
\]

The finite envelope recursion in Section 4 below returns activation-only
numbers \(\overline{\mathcal J}_{2,5}\) and
\(\overline{\mathcal J}_{4,5}\).  Define

\[
 \kappa_{42}=3K_\phi,
 \qquad
 B_{42}=\frac{\overline{\mathcal J}_{4,5}
                  +2^5\overline{\mathcal J}_{2,5}}{120},
 \qquad h_{42}=\frac12 .
\]

Then

\[
 \boxed{
 |F_4(\eta)-F_2(2\eta)-3K_\phi\eta^3|
 \le B_{42}|\eta|^5,
 \qquad |\eta|\le\frac12 .}
\]

For the orientation requested as (F_2(2\eta)-F_4(\eta)), replace
\(\kappa_{42}\) by \(-3K_\phi\); the absolute remainder bound is unchanged.
In particular, for every \(\varepsilon>0\),

\[
 |\eta|\le
 \min\left\{\frac12,
 \sqrt{\frac{\varepsilon}{1+B_{42}}}\right\}
\]

implies

\[
 |F_4(\eta)-F_2(2\eta)|
 \le (3|K_\phi|+\varepsilon)|\eta|^3.
\]

If \(\phi\) is constant, both discrepancies vanish identically and one may
take \(K_\phi=B_{42}=0\).

## 1. Exact four-step chronology and operator DAG

At finite width, with the same notation as in the preceding proof,

\[
\begin{aligned}
 a_i^{s+1}&=a_i^s+h\phi(z_i^s),\\
 W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}C_i^sH_j^s,\\
 u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s),
\end{aligned}
\]

where

\[
 H_j^s=\phi(u_j^s),\quad C_i^s=a_i^s\phi'(z_i^s),
\]

\[
 z^s=\frac{WH^s}{\sqrt n}+h\sum_{r<s}Q_{rs}^{(n)}C^r,
 \qquad
 b^s=\frac{W^TC^s}{\sqrt n}+h\sum_{r<s}K_{rs}^{(n)}H^r .
\]

For (F_{4,n}), expose the initial matrix (W) through the nine predictable
actions

\[
 Y^0,D^0,Y^1,D^1,Y^2,D^2,Y^3,D^3,Y^4,
\]

where (Y^s=WH^s/\sqrt n), (D^s=W^TC^s/\sqrt n).  The newly revealed
queries are, in the same order,

\[
 H^0,C^0,H^1,C^1,H^2,C^2,H^3,C^3,H^4.
\]

The complete new empirical ledger is

\[
\begin{array}{c|c|l}
\text{action}&\text{query}&\text{new scalar data}\\ \hline
Y^0&H^0&Q^{(n)}_{00}\\
D^0&C^0&K^{(n)}_{00},\ (Y^0)^TC^0/n\\
Y^1&H^1&Q^{(n)}_{01},Q^{(n)}_{11},\ (D^0)^TH^1/n\\
D^1&C^1&K^{(n)}_{01},K^{(n)}_{11},\ (Y^{0:1})^TC^1/n\\
Y^2&H^2&Q^{(n)}_{02},Q^{(n)}_{12},Q^{(n)}_{22},\
                  (D^{0:1})^TH^2/n\\
D^2&C^2&K^{(n)}_{02},K^{(n)}_{12},K^{(n)}_{22},\
                  (Y^{0:2})^TC^2/n\\
Y^3&H^3&Q^{(n)}_{03},Q^{(n)}_{13},Q^{(n)}_{23},Q^{(n)}_{33},\
                  (D^{0:2})^TH^3/n\\
D^3&C^3&K^{(n)}_{03},K^{(n)}_{13},K^{(n)}_{23},K^{(n)}_{33},\
                  (Y^{0:3})^TC^3/n\\
Y^4&H^4&Q^{(n)}_{04},Q^{(n)}_{14},Q^{(n)}_{24},Q^{(n)}_{34},Q^{(n)}_{44},\
                  (D^{0:3})^TH^4/n.
\end{array}
\]

At every line the already accumulated block
\((C^{\mathrm{old}})^TY^{\mathrm{old}}/n
=(D^{\mathrm{old}})^TH^{\mathrm{old}}/n\) is also present.  It was generated
by earlier lines, so the table contains every new regression input and no
unlisted response overlap.

The limiting DAG is the recursion, for (s=0,1,2,3),

\[
\begin{aligned}
 H_s&=\phi(u_s),\\
 b_s&=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
          +h\sum_{r<s}K_{rs}H_r,\\
 u_{s+1}&=u_s+h b_s\phi'(u_s),\\
 z_s&=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,\\
 a_s&=A+h\sum_{r<s}\phi(z_r),\\
 C_s&=a_s\phi'(z_s),
\end{aligned}
\]

with

\[
 Q_{rs}=\mathbb E[H_rH_s],\qquad
 K_{rs}=\mathbb E[C_rC_s],
\]

\[
 \rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],\qquad
 \sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s].
\]

Here (U,A\) are independent standard Gaussians,
((\chi_0,\ldots,\chi_s)) has covariance (K^{[s]}) and is independent of
(U), while ((\xi_0,\ldots,\xi_s)) has covariance (Q^{[s]}) and is
independent of (A).  After the (s=3) lower update, construct

\[
 H_4=\phi(u_4),
\]

then a terminal top Gaussian block with covariance (Q^{[4]}), and set

\[
 z_4=\xi_4+\sum_{r<4}(\rho_{4r}+hQ_{r4})C_r,
 \qquad
 a_4=A+h\sum_{r<4}\phi(z_r),
\]

\[
 F_4(h)=\mathbb E[a_4\phi(z_4)].
\]

This inverse-free recursion is defined also at (h=0).

## 2. Strict rank from conditional innovations

We prove a statement stronger than the four-time rank needed here.

### Lemma 2.1 (all finite query Grams)

If \(\phi\) is nonconstant, then, for every fixed (h\ne0) and every finite
(s), both

\[
 Q^{[s]}=(Q_{rv})_{0\le r,v\le s},\qquad
 K^{[s]}=(K_{rv})_{0\le r,v\le s}
\]

are positive definite.

#### Proof: non-affine activation

Since \(\phi\) is nonconstant,

\[
 d=\mathbb E[\phi'(G)^2]>0,
\]

so (Q^{[0]}=(1)) and (K^{[0]}=(d)) are positive definite.  Suppose
(Q^{[s]}) and (K^{[s]}) are positive definite.  Let

\[
 \mathfrak k_s
 =K_{ss}-K_{s,<s}(K^{[s-1]})^{-1}K_{<s,s}>0.
\]

On one Gaussian realization of the lower block,

\[
 \chi_s=m_s(\chi_{<s})+\sqrt{\mathfrak k_s}\,Z_s,
\]

where (Z_s\) is a fresh standard Gaussian.  Conditional on
(\mathcal L_s=\sigma(U,\chi_0,\ldots,\chi_{s-1})),

\[
 u_{s+1}=r_s+h\phi'(u_s)\sqrt{\mathfrak k_s}\,Z_s
\]

for an \(\mathcal L_s\)-measurable (r_s).  On the event
(\phi'(u_s)\ne0), this conditional Gaussian has full support.  A continuous
nonconstant function cannot be constant under a full-support Gaussian, so

\[
 \operatorname{Var}(H_{s+1}\mid\mathcal L_s)>0
 \quad\hbox{on }\{\phi'(u_s)\ne0\}.
\]

The event has positive probability for every (s).  At (s=0) this is the
identity (d>0).  If it has positive probability at (s), the preceding
full-support conditional law and the fact that
(\{x:\phi'(x)\ne0\}) is a nonempty open set show that it has positive
probability at (s+1).  Since every (H_r, r\le s), is
(\mathcal L_s\)-measurable, for arbitrary coefficients \(c_r\),

\[
 \mathbb E\left(H_{s+1}-\sum_{r\le s}c_rH_r\right)^2
 \ge \mathbb E\operatorname{Var}(H_{s+1}\mid\mathcal L_s)>0.
\]

Thus the new Schur complement is positive and (Q^{[s+1]}\succ0).

Now assume \(\phi\) is non-affine, so \(\phi'\) is nonconstant.  Write the
new top source as

\[
 \xi_{s+1}=n_{s+1}(\xi_{\le s})
        +\sqrt{\mathfrak q_{s+1}}\,E_{s+1},
\]

where (E_{s+1}\) is fresh and \(\mathfrak q_{s+1}>0\) is the new Schur
complement of (Q^{[s+1]}).  Conditional on

\[
 \mathcal T_{s+1}=\sigma(A,\xi_0,\ldots,\xi_s),
\]

(a_{s+1}) is measurable and

\[
 C_{s+1}=a_{s+1}\phi'(r_{s+1}
          +\sqrt{\mathfrak q_{s+1}}E_{s+1}).
\]

For every real (r) and every \(q>0\),

\[
 \operatorname{Var}[\phi'(r+\sqrt qG)]>0;
\]

otherwise continuity and Gaussian full support would make \(\phi'\)
constant on \(\mathbb R\).  Also
(\mathbb P(a_{s+1}\ne0)>0\).  For (s+1=1), this follows from
(a_1=A+h\phi(\xi_0)) and independence of (A,\xi_0).  In general,

\[
 a_{s+1}=a_s+h\phi(z_s),
\]

and, conditional on (A,\xi_0,\ldots,\xi_{s-1}), the last term is a
nonconstant function of the fresh innovation in \(\xi_s\); hence it cannot
make (a_{s+1}) identically zero.  Consequently

\[
 \mathbb E\operatorname{Var}(C_{s+1}\mid\mathcal T_{s+1})>0.
\]

Every (C_r, r\le s), is \(\mathcal T_{s+1}\)-measurable, so the same
conditional-variance inequality proves (K^{[s+1]}\succ0).  This closes the
induction.

#### Proof: affine activation

Let \(\phi(x)=\alpha x+\beta\), with \(\alpha\ne0\).  If
(\mathfrak k_s>0\) is the newest (K)-Schur complement, then, conditional
on the old lower sources,

\[
 H_{s+1}=\text{old}+h\alpha^2\sqrt{\mathfrak k_s}\,Z_s.
\]

Therefore its conditional variance is
(h^2\alpha^4\mathfrak k_s>0), proving the next (Q)-rank.  For (s\ge1),
(C_s=\alpha a_s\), and the fresh innovation in \(\xi_{s-1}\) enters
(a_s=a_{s-1}+h(\alpha z_{s-1}+\beta)) with coefficient
(h\alpha\sqrt{\mathfrak q_{s-1}}).  Hence

\[
 \operatorname{Var}(C_s\mid A,\xi_0,\ldots,\xi_{s-2})
 =h^2\alpha^4\mathfrak q_{s-1}>0.
\]

Together with (Q^{[0]}=(1)), (K^{[0]}=(\alpha^2)), this alternately
proves every (Q^{[s]}) and (K^{[s]}).  \(\square\)

In particular, (Q^{[3]}) and (K^{[3]}), the only nonterminal Grams in
the nine-action exposure, are positive at every fixed (h\ne0).  Notice
that this proof used no Taylor expansion, no Gram derivative, and no
learning-rate limit.

Thus, relative to the compiler domain \(|h|\le1\), an explicit punctured
rank radius is simply

\[
 r_{\mathrm{rank},4}=1.
\]

The comparison also evaluates (F_2) at (2\eta), so its final radius is

\[
 h_{42}=\min\{r_{\mathrm{rank},4},1/2\}=1/2.
\]

## 3. Fixed-step identification of the actual network

We spell out the generic response cancellation, since it proves both new
actions (D^3,Y^4), and indeed every later action.

Before a column action (D^s), collect

\[
 H=(H_0,\ldots,H_s),\qquad C=(C_0,\ldots,C_{s-1}),
\]

and write the already exposed source actions as

\[
 Y=\xi+PC,\qquad D=\chi+SH.
\]

Here (P_{vr}=\rho_{vr}\mathbf1_{r<v}) and
(S_{vr}=\sigma_{vr}\mathbf1_{r\le v}).  Let

\[
 Q=\mathbb E[HH^T],\quad K=\mathbb E[CC^T],\quad
 k=\mathbb E[CC_s],\quad
 \sigma_s=(\sigma_{s0},\ldots,\sigma_{ss})^T.
\]

Gaussian integration by parts gives, entry by entry,

\[
 R:=\mathbb E[CY^T]=SQ+KP^T,
 \qquad r:=\mathbb E[YC_s]=Q\sigma_s+Pk.
\]

The adaptive Gaussian conditioning formula has an (H)-coefficient

\[
 Q^{-1}(r-R^TK^{-1}k)
 =\sigma_s-S^TK^{-1}k.
\]

Its first regression term contributes (S^TK^{-1}k), so these pieces
cancel and the limit is

\[
 D^s\ \Longrightarrow\
 \chi_s+\sum_{r\le s}\sigma_{sr}H_r.
\]

Adding the exact learned-matrix pieces gives (b_s) in Section 1.

After this column action, collect (H=(H_0,\ldots,H_s)) and
(C=(C_0,\ldots,C_s)).  For the next row query (H_{s+1}), let

\[
 q=\mathbb E[HH_{s+1}],\qquad
 \rho_{s+1}=(\rho_{s+1,0},\ldots,\rho_{s+1,s})^T.
\]

Integration by parts gives

\[
 v:=\mathbb E[DH_{s+1}]=K\rho_{s+1}+Sq,
 \qquad R=SQ+KP^T.
\]

The direct (C)-coefficient in row conditioning is

\[
 K^{-1}(v-RQ^{-1}q)
 =\rho_{s+1}-P^TQ^{-1}q.
\]

The row-projection term contributes the opposite
(P^TQ^{-1}q).  Therefore

\[
 Y^{s+1}\ \Longrightarrow\
 \xi_{s+1}+\sum_{r\le s}\rho_{s+1,r}C_r,
\]

and the learned pieces give (z_{s+1}).

For (s=3), these are precisely the two new cancellations at (D^3,Y^4).
They retain all column dependence of (H^3) inside the joint \(\chi\)-block;
no independence approximation is made.

For completeness, the convergence proof is the finite induction used for
seven actions, with two more rows.  At each action stop if an empirical
nonterminal Gram eigenvalue or Schur complement is below half its strictly
positive population value.  On the stopped event, inverse Gram maps and
nonterminal square roots are Lipschitz.  Couple the orthogonal Gaussian
residual to the fresh innovation of the population Gram--Schmidt block;
projection onto a fixed-dimensional old span costs (O_{L^p}(n^{-1/2})).
Every new empirical Gram and response overlap is an iid empirical average
of a polynomial-growth coordinate function, so Rosenthal's inequality gives
(O_{L^p}(n^{-1/2})).  The bounded derivatives and linear growth of
\(\phi\) transfer this estimate through the next coordinate update by the
mean-value theorem and Hölder.  These statements prove, successively, all
nine rows, including every cross block (C^TY/n=D^TH/n).

The stopping probability tends to zero faster than any prescribed fixed
power by taking the moment order in Rosenthal and applying Weyl plus Markov.
To remove stopping, extend the finite norm-majorant recursion of the
seven-action proof from (s\le2) to (s\le3).  Every resulting norm is a
fixed polynomial of

\[
 1+\|W\|_{\rm op}/\sqrt n+\|A\|_2/\sqrt n+\|U\|_2/\sqrt n,
\]

which has moments of all orders uniformly in (n).  Hölder therefore makes
the stopped complement vanish, proves uniform integrability of every
terminal output, and yields, separately at every fixed (h\ne0),

\[
 \lim_{n\to\infty}F_{4,n}(h)=F_4(h).
\]

The identical argument stopped at (Y^2) identifies (F_2(2h)) at the
fixed step (2h\).  At zero, the equality follows directly from the
untrained network.  Thus the width limit has been taken before any
(h\)-derivative.

## 4. (C^5) operator regularity and an explicit envelope constant

Use the envelope-pair arithmetic and the finite Price recursion of Section
5 of the preceding proof.  Replace its formerly terminal top-3 pass by an
internal top-3 pass, and then append two passes:

1. with covariance \(\operatorname{diag}(1,Q^{[3]})\), construct
   (z_3,a_3,C_3), compile (K^{[3]}), and compile every
   \(\sigma_{3r}\), (0\le r\le3);
2. with covariance \(\operatorname{diag}(1,K^{[3]})\), construct
   (b_3,u_4,H_4), all (Q_{r4}), and all \(\rho_{4r},L_{4r});
3. with covariance \(\operatorname{diag}(1,Q^{[4]})\), construct
   (z_4,a_4) and compile (F_4=\mathbb E[a_4\phi(z_4)]).

Equivalently, starting from initialization, this is the finite eight-pass
alternation lower-1, top-1, lower-2, top-2, lower-3, top-3, lower-4,
terminal-top-4.  At every pass use

\[
 \bar c_j=\mathbf1_{j=0}+\sum_{r,v}\bar G_{rv,j},
 \qquad 0\le j\le5,
\]

for the current Gaussian covariance, and use

\[
 \bar L_j=\bar\rho_j+\bar Q_j+j\bar Q_{j-1},
 \qquad \bar Q_{-1}=0.
\]

Whenever a top-(N) node has been constructed, also submit the terminal
integrand (a_N\phi(z_N)) to the same Price recursion and denote its fifth
majorant by \(\overline{\mathcal J}_{N,5}\).  This does not alter any later
node and supplies one common compiler run for (N=1,2,3,4).

The Price recursion has the finite index set

\[
 \{(r,j,m):r+j+\lceil m/2\rceil\le5\}.
\]

Thus (j+m\le10).  A response integrand starts with activation derivative
order at most two, so no derivative beyond \(\phi^{(12)}\) occurs.  There
are eight passes and finitely many scalar nodes, so the recursion terminates.
It produces explicit numbers, made only from (M_\phi), integer arithmetic,
and the stated Gaussian moment formula, satisfying

\[
 |F_N^{(5)}(h)|\le\overline{\mathcal J}_{N,5},
 \qquad |h|\le1,\quad N=2,4.
\]

These symbols denote the output of that syntactic envelope recursion; they
are not defined as suprema of (F_N^{(5)}).  Repeated singular-covariance
Price differentiation is valid because every mixed derivative generated by
the finite recursion has the displayed common polynomial envelope.  The
cutoff-and-ε-regularization proof in the preceding note therefore applies
at (h=0), even though all source coordinates coalesce there.

## 5. Cubic coefficient and fifth-order remainder

The nodewise width-first DAG calculation already proves, for every fixed
integer (N),

\[
 F_N'(0)=N(1+d+d^2),
\]

and

\[
 F_N'''(0)
 =\frac{N(4N^2-3N+1)}2S_\phi
 +2N(N-1)(2N-1)H_\phi .
\]

The proof differentiates the inverse-free Gaussian recursion and includes
all Price covariance terms.  Lemma 2.1 and Section 3 above now supply the
missing fixed-width intertwining for (N=4).

Consequently,

\[
 F_4'''(0)=106S_\phi+168H_\phi,
 \qquad
 F_2'''(0)=11S_\phi+12H_\phi,
\]

and hence

\[
 \frac{\Delta_{42}'''(0)}6
 =\frac{106S_\phi+168H_\phi
       -8(11S_\phi+12H_\phi)}6
 =3(S_\phi+4H_\phi).
\]

Also \(\Delta_{42}'(0)=0\).  The sign involution

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad \chi\mapsto-\chi
\]

leaves (u,H,z,Q,K) invariant and changes the sign of (a,C,b,F_N).
Therefore every (F_N), and hence \(\Delta_{42}\), is odd.  Its zeroth,
second, and fourth derivatives at zero vanish.

For \(|\eta|\le1/2\), both \(\eta\) and (2\eta\) lie in the compiler
interval.  Therefore

\[
 |\Delta_{42}^{(5)}(t)|
 \le\overline{\mathcal J}_{4,5}
      +2^5\overline{\mathcal J}_{2,5}.
\]

Taylor's integral formula through order four gives

\[
 \Delta_{42}(\eta)-3K_\phi\eta^3
 =\frac1{24}\int_0^\eta(\eta-t)^4
             \Delta_{42}^{(5)}(t)\,dt,
\]

and proves the theorem because

\[
 \frac1{24}\int_0^{|\eta|}(|\eta|-t)^4dt
 =\frac{|\eta|^5}{120}.
\]

## 6. Shared constants for the three concrete comparisons

Define

\[
 \mathcal R_\phi
 =\frac1{120}\max_{1\le N\le4}
    \overline{\mathcal J}_{N,5},
 \qquad
 \mathfrak h=\frac13,
 \qquad K_\phi=S_\phi+4H_\phi.
\]

These are shared activation-only quantities.  On the common interval
\(|\eta|\le\mathfrak h\), the three concrete bounds may be written

\[
\begin{array}{c|c|c}
\text{discrepancy}&\text{cubic coefficient}&
 \text{valid remainder coefficient}\\ \hline
F_2(\eta/2)-F_1(\eta)&K_\phi/16&(33/32)\mathcal R_\phi\\
F_3(\eta)-F_1(3\eta)&(5/2)K_\phi&244\mathcal R_\phi\\
F_4(\eta)-F_2(2\eta)&3K_\phi&33\mathcal R_\phi.
\end{array}
\]

Indeed these remainder multipliers are respectively

\[
 2^{-5}+1=\frac{33}{32},\qquad
 1+3^5=244,\qquad 1+2^5=33.
\]

Thus the same (K_\phi,\mathcal R_\phi,\mathfrak h) work in all three
results; only explicit numerical coefficients change.
