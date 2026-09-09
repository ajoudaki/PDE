# Fixed-step concentration closure

This supplement supplies the quantitative finite-action induction used in
Section 4.3 of `PROOF.md`.  It is deliberately restricted to the
probabilistic bridge.  The exact adaptive Gaussian conditioning identity and
the population response algebra are those proved in Sections 4.1--4.2 of
`PROOF.md`.

## 1. Statement

Fix an integer \(N\geq1\), a step size \(h\ne0\), and a nonconstant
activation \(\phi\) satisfying, for some \(M\ge1\),

\[
 |\phi(x)|\le M(1+|x|),\qquad
 \|\phi'\|_\infty\le M,\qquad \|\phi''\|_\infty\le M . \tag{1.1}
\]

As in `PROOF.md`, assume also \(\mathbb E\phi(G)^2=1\) for
\(G\sim N(0,1)\).

The stronger \(C^{12}\) hypothesis in `PROOF.md` implies (1.1).  Couple the
finite-width network to the inverse-free population DAG in the chronological
action order

\[
 Y^0,D^0,Y^1,D^1,\ldots,Y^{N-1},D^{N-1},Y^N .             \tag{1.2}
\]

For every finite \(p,P\ge2\), every value field \(X_n\) constructed in this
ledger has a population-particle counterpart \(\bar X\) such that

\[
 \left\|\|X_n-\bar X\|_{n,p}\right\|_{L^P}\longrightarrow0,
 \qquad
 \|x\|_{n,p}:=\left(n^{-1}\sum_i|x_i|^p\right)^{1/p}.    \tag{1.3}
\]

The same conclusion for \(0<p<2\) or \(0<P<2\) follows from the normalized
power-mean inequality and monotonicity of probability \(L^r\)-norms, so all
positive finite mixed orders are covered.

Every empirical Gram and every raw cross-moment used in an adaptive
regression converges in every finite \(L^P\) to its population value.  The
empirical regression coefficients, extended by their population values off
the stopped full-rank event, converge in every finite \(L^P\); in particular
they are uniformly integrable.  The raw terminal outputs are uniformly
integrable and

\[
 \lim_{n\to\infty}\mathbb E f_n^N
 =\mathbb E[a_N\phi(z_N)]=F_N(h).                         \tag{1.4}
\]

More quantitatively, before stopping all field, Gram, raw-cross-moment, and
extended-coefficient errors are \(O(n^{-1/2})\) at every prescribed finite
moment order.  For each \(m\ge1\), the probability that stopping occurs is
\(O(n^{-m})\).  The moment order used to obtain either assertion is specified
in Section 6 below.

No assertion is made about moments of an arbitrarily chosen Moore--Penrose
coordinate vector on a rank-deficient exceptional event.  Such coordinates
are noncanonical and do not occur in the network.  The coefficients actually
used in the identification are the extended coefficients just described;
they agree with the exact conditional-regression coefficients whenever the
coupling has not stopped.

If \(\phi\) is constant, normalization gives \(\phi\equiv\pm1\), all
cotangents vanish, and \(\mathbb E f_n^N=Nh\) exactly.  Hence only the
nonconstant case needs the argument below.

## 2. The finite list of objects

There are two physical populations.  A *top field* is indexed by \(i\) and a
*lower field* by \(j\).  For each population take an infinite supply of iid
standard-normal coordinate marks.  Top and lower supplies are independent.
Within a population, reuse the same coordinate through time.  Thus the ideal
top coordinate contains \((A,\xi_0,\ldots,\xi_N)\), and the ideal lower
coordinate contains \((U,\chi_0,\ldots,\chi_{N-1})\), with the chronological
Gaussian extensions prescribed by the population conditional regressions.
Coordinates are iid within either population, while their time coordinates
are not independent.

The following finite micro-ledger contains every object needed by (1.2).

1. Construct \(U,A,H^0=\phi(U)\), and the initial feature moment.
2. For each \(0\le s<N\), perform, in order:
   (a) the row action \(Y^s\);
   (b) the coordinate maps producing \(z^s,a^s,C^s\);
   (c) all top-population pair moments needed before \(D^s\);
   (d) the column action \(D^s\);
   (e) the coordinate maps producing \(b^s,u^{s+1},H^{s+1}\);
   (f) all lower-population pair moments needed before \(Y^{s+1}\).
3. Perform \(Y^N\), construct \(z^N,a^N,a^N\phi(z^N)\), and form its
   empirical average.

Empty or already known blocks are simply retained.  A pair-moment block
contains all entries of

\[
 n^{-1}H^TH,\quad n^{-1}C^TC,\quad
 n^{-1}C^TY=n^{-1}D^TH,                                  \tag{2.1}
\]

and the query cross-moments \(q,k,r,s\) appearing in (4.5a)--(4.5b) of
`PROOF.md`.  Every entry of (2.1) is an average of a product of two fields
from one physical population.  The ledger has at most

\[
 L_N:=6N+4                                                   \tag{2.2}
\]

micro-steps: one initial moment step, six steps for each nonterminal time,
and three terminal steps.  Some entries are redundant, which only lowers the
actual number.  This explicit upper bound will be used in the moment tower.

## 3. Three quantitative lemmas

All constants below may depend on the fixed \((N,h,M)\), the population
spectral gap defined in Section 4, and the displayed moment order, but never
on \(n\).

### Lemma 3.1 (iid averages)

If \(Z_1,\ldots,Z_n\) are iid, centered, and \(r\ge2\), then

\[
 \left\|n^{-1}\sum_{i=1}^nZ_i\right\|_{L^r}
 \le C_r n^{-1/2}\|Z_1\|_{L^r}.                          \tag{3.1}
\]

Indeed, Rosenthal's inequality gives

\[
 \left\|\sum_i Z_i\right\|_{L^r}
 \le C_r\left(n^{1/2}\|Z_1\|_{L^2}
                  +n^{1/r}\|Z_1\|_{L^r}\right).
\]

Divide by \(n\), use \(\|Z_1\|_2\le\|Z_1\|_r\), and note that
\(n^{-1+1/r}\le n^{-1/2}\).

### Lemma 3.2 (pair moments)

Suppose top- or lower-population fields \(X_n,Y_n\) are coupled to iid
coordinate pairs \((\bar X_i,\bar Y_i)\).  If

\[
 \left\|\|X_n-\bar X\|_{n,2r}\right\|_{L^{2r}}
 +\left\|\|Y_n-\bar Y\|_{n,2r}\right\|_{L^{2r}}
 \le Cn^{-1/2}                                             \tag{3.2}
\]

and all four normalized \(2r\)-moments are uniformly bounded, then

\[
 \left\|n^{-1}X_n^TY_n-\mathbb E[\bar X_1\bar Y_1]
 \right\|_{L^r}\le C'n^{-1/2}.                           \tag{3.3}
\]

To prove it, insert \(n^{-1}\bar X^T\bar Y\).  Normalized
Cauchy--Schwarz followed by Holder gives

\[
 \begin{aligned}
 \left\|n^{-1}(X_n-\bar X)^TY_n\right\|_{L^r}
 &\le
 \left\|\|X_n-\bar X\|_{n,2r}\right\|_{L^{2r}}
 \left\|\|Y_n\|_{n,2r}\right\|_{L^{2r}},\\
 \left\|n^{-1}\bar X^T(Y_n-\bar Y)\right\|_{L^r}
 &\le
 \left\|\|\bar X\|_{n,2r}\right\|_{L^{2r}}
 \left\|\|Y_n-\bar Y\|_{n,2r}\right\|_{L^{2r}}.
 \end{aligned}                                             \tag{3.4}
\]

The remaining iid average is covered by Lemma 3.1 applied to
\(\bar X_i\bar Y_i-\mathbb E\bar X_1\bar Y_1\), whose \(L^r\) norm is
finite by Holder.  This proves (3.3).

### Lemma 3.3 (one adaptive Gaussian action)

Consider one row action; the column case is its transpose.  Conditional on
the preceding ledger, the exact conditioning identity has the form

\[
 T_n=\sum_{\ell=1}^{d}\alpha_{\ell,n}X_{\ell,n}
       +\tau_nP_{V_n}^{\perp}g,                           \tag{3.5}
\]

where \(d\le2N+2\), \(g\sim N(0,I_n)\) is conditionally fresh,
\(V_n\) is the old opposite-population query block, and the
\(\alpha_{\ell,n}\) and \(\tau_n^2\) are the rational Gram/cross-moment
expressions in (4.5a) of `PROOF.md`.  Its population version is

\[
 \bar T=\sum_{\ell=1}^{d}\alpha_\ell\bar X_\ell+\tau g. \tag{3.6}
\]

Suppose every Gram inverse in (3.5) is bounded by \((2\gamma)^{-1}\),
and \(\tau_n^2,\tau^2\ge2\gamma\).  If all input field and empirical
observable errors are \(O(n^{-1/2})\) at moment order \(8r\), and their
moments are uniformly bounded there, then

\[
 \left\|\|T_n-\bar T\|_{n,r}\right\|_{L^r}
 \le C_rn^{-1/2}.                                        \tag{3.7}
\]

The same conclusion holds for the extended version of (3.5) defined in
Section 4.

Here is the full estimate.  On the stated spectral set, the inverse identity

\[
 A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}                         \tag{3.8}
\]

and expansion of the finitely many products in (4.5a) give

\[
 |\alpha_n-\alpha|
 \le C\,(1+|q_n|+|s_n|+|R_n|)^2
       (|Q_n-Q|+|K_n-K|+|q_n-q|+|s_n-s|+|R_n-R|).         \tag{3.9}
\]

Matrix norms may be used in (3.9); all dimensions are at most \(N+1\),
so they are equivalent up to an \(N\)-dependent constant.  Formula (3.9)
follows term by term: replace one factor at a time in
\(Q_n^{-1}q_n\), \(K_n^{-1}s_n\), and
\(K_n^{-1}R_nQ_n^{-1}q_n\); (3.8) controls the inverse replacement.
There are at most four nonconstant factors in any term.  Holder with four
factors therefore proves

\[
 \|\alpha_n-\alpha\|_{L^{2r}}\le C_rn^{-1/2}.             \tag{3.10}
\]

The query innovation variance is

\[
 v_n=q_{**}^{(n)}-(q_n)^TQ_n^{-1}q_n                     \tag{3.11}
\]

(with the transposed analogue for a column query).  The same one-factor
replacement gives \(\|v_n-v\|_{L^{2r}}\le Cn^{-1/2}\).
Since \(v_n,v\ge2\gamma\),

\[
 |\tau_n-\tau|=|\sqrt{v_n}-\sqrt v|
 \le (2\sqrt{2\gamma})^{-1}|v_n-v|.                     \tag{3.12}
\]

Because (3.11) is a squared orthogonal-residual norm,
\(0\le v_n\le q_{**}^{(n)}\).  Thus the input query moment bound controls
every moment of \(\tau_n=\sqrt{v_n}\); no upper spectral cutoff is needed.

For completeness, if \(X\) has \(d\) fixed columns,
\(\lambda_{\min}(X^TX/n)\ge2\gamma\), and \(g\) is conditionally fresh,
then

\[
 P_Xg=X(X^TX/n)^{-1}(X^Tg/n),                            \tag{3.13}
\]

and, conditionally on \(X\),

\[
 (X^Tg/n)\sim N(0,X^TX/n^2).
\]

Equivalently the coefficient in (3.13) has covariance
\((X^TX/n)^{-1}/n\).  Gaussian moments and Minkowski therefore give

\[
 \left(\mathbb E_g\|P_Xg\|_{n,r}^r\right)^{1/r}
 \le C_{r,d,\gamma}n^{-1/2}\sum_{k=1}^{d}\|X_k\|_{n,r}. \tag{3.14}
\]

Subtracting (3.6) from (3.5), using
\(P_{V_n}^{\perp}g=g-P_{V_n}g\), yields

\[
 \begin{aligned}
 \|T_n-\bar T\|_{n,r}
 \le{}&\sum_\ell |\alpha_{\ell,n}|
                 \|X_{\ell,n}-\bar X_\ell\|_{n,r}\\
 &+\sum_\ell|\alpha_{\ell,n}-\alpha_\ell|
                 \|\bar X_\ell\|_{n,r}
   +|\tau_n-\tau|\|g\|_{n,r}
   +|\tau_n|\|P_{V_n}g\|_{n,r}.                        \tag{3.15}
 \end{aligned}
\]

Apply Holder to each product, then (3.10), (3.12), and (3.14).  Moment order
\(8r\) covers every factor in (3.9)--(3.15), proving (3.7).  The column
formula contains the same number of factors and is identical after
transposition.

The global extended-action estimate does not apply (3.9) on a failed
spectral event.  If \({\cal G}\) is the current good event, its definition is

\[
 T_n^{\rm ext}
 =\mathbf1_{\cal G}\left(
       \sum_\ell\alpha_{\ell,n}X_{\ell,n}^{\rm ext}
       +\tau_nP_{V_n}^{\perp}g\right)
 +\mathbf1_{{\cal G}^c}\left(
       \sum_\ell\alpha_\ell X_{\ell,n}^{\rm ext}+\tau g\right). \tag{3.16}
\]

On \({\cal G}\), subtraction of (3.6) is bounded by (3.15).  On
\({\cal G}^c\), the Gaussian terms cancel exactly and

\[
 T_n^{\rm ext}-\bar T
 =\sum_\ell\alpha_\ell(X_{\ell,n}^{\rm ext}-\bar X_\ell). \tag{3.17}
\]

Taking the \(L^r(\|\cdot\|_{n,r})\) norm of the two indicator pieces and
using the input induction bound proves (3.7) globally.  Thus no inverse,
empirical coefficient, or unproved moment bound is used off \({\cal G}\).

## 4. The stopped joint coupling

By strict population rank, every Gram inverse and every query innovation
variance appearing in the finite action list is positive.  Let

\[
 4\gamma=\min\left\{
 1,\ \lambda_{\min}(G),\ v:
 G\text{ is a population Gram inverted in (1.2), and }
 v\text{ is a population query Schur complement in (1.2)}
 \right\}>0.                                               \tag{4.1}
\]

The minimum is over a nonempty finite set; including \(1\) handles an
otherwise empty inverse block.  Unlike the abbreviated definition in
`PROOF.md`, (4.1) includes the terminal \(Y^N\) innovation.  Its positivity
follows from the strict rank of \(Q^{[N]}\).

Set \({\cal G}_{-1}=\Omega\).  Immediately before action \(q\), all raw data
needed by its conditional regression are measurable.  Let \({\cal G}_q\)
be \({\cal G}_{q-1}\) intersected with the conditions

\[
 \lambda_{\min}(G_n)\ge2\gamma,qquad v_n\ge2\gamma       \tag{4.2}
\]

for every Gram and query Schur complement first needed at that action.
Within an action, test the old Grams first.  Define \(v_n\) by its Schur
formula only on the branch where those Grams pass, and set \(v_n=v\) on the
other branch before testing the second condition in (4.2).  Thus no inverse
of a failed Gram is ever evaluated, and the resulting event is predictable.
On \({\cal G}_q\), use the exact
conditional-regression coefficients and residual projection.  Off
\({\cal G}_q\), replace every coefficient and innovation scale by its
population value and replace the residual projection by the identity.
Call the resulting globally defined quantities and fields *extended*.

At action \(q\), take a fresh iid Gaussian vector \(g_q\), independent of
the joint raw/extended/ideal past.  First generate the **raw** action from the
exact Moore--Penrose conditional representation, on every event, using
\(g_q\).  The adaptive conditioning theorem proves that this is the correct
raw-network conditional law.  Formally, induction on \(q\) proves equality
of the finite-dimensional joint law: the external marks have their prescribed
law at \(q=-1\), and integration of the common next-action kernel against the
common past law proves equality after action \(q\).  This finite recursion
terminates after \(2N+1\) actions.

Next generate the **extended** action with the same \(g_q\): on
\({\cal G}_q\) use the raw coefficients and residual projection, while off
\({\cal G}_q\) use the population coefficients and the identity projection.
Use \(g_q\) also in the ideal population action.  Apply the coordinate
updates separately to the raw and extended fields, then continue to the next
action.  This constructs one joint coupling of the complete raw, extended,
and ideal ledgers.  Inductively, on \({\cal G}_q\) every extended field
through action \(q\) equals its raw-network counterpart, because the queries
are predictable and all earlier representations agree there.

Off \({\cal G}_q\), an extended inverse coefficient is a fixed population
number.  On \({\cal G}_q\), (4.2) bounds every inverse, and formulas
(3.9)--(3.12) bound the remaining coefficients by polynomials in empirical
pair moments.  Consequently all extended fields and coefficients have every
finite moment once the preceding fields do.

## 5. The action-indexed rate induction

For \(r\ge2\), let \({\cal E}_{\ell,r}(n)\) be the maximum of

\[
 \left\|\|X_n-\bar X\|_{n,r}\right\|_{L^r},
 \qquad
 \|T_n-T\|_{L^r}                                          \tag{5.1}
\]

over all extended fields \(X_n\) and empirical pair moments \(T_n\)
constructed through micro-step \(\ell\).  Let \({\cal M}_{\ell,r}(n)\)
be the maximum of their corresponding \(r\)-moments, with \(1\) included.
We prove, successively for \(0\le\ell\le L_N\), that

\[
 \sup_n{\cal M}_{\ell,r}(n)<\infty,qquad
 {\cal E}_{\ell,r}(n)\le C_{\ell,r}n^{-1/2}              \tag{5.2}
\]

for every finite \(r\).  The quantifier order is important: the induction
is over the finite ledger index \(\ell\), and at each fixed \(\ell\) the
assertion is simultaneous over all finite \(r\).  Hence using a larger
moment at the preceding micro-step is not circular.

At \(\ell=0\), couple finite and ideal \(A,U,H^0\) identically.  All their
moments are finite by Gaussianity and (1.1).  Every initial empirical pair
moment has error \(O(n^{-1/2})\) by Lemma 3.1, so (5.2) holds.

Assume (5.2) through micro-step \(\ell-1\) at every finite order.  There are
only three possible next steps.

* **A coordinate step.**  Each elementary map in (2.1) of `PROOF.md` is a
  finite sum of the following maps:

  \[
  x+y,\quad \theta x,\quad \phi(x),\quad
  a\phi'(z),\quad b\phi'(u).                              \tag{5.3}
  \]

  The first two use the triangle inequality and Holder.  The last three use

  \[
  |\phi(x)-\phi(y)|\le M|x-y|,
  \]

  \[
  |a\phi'(z)-\bar a\phi'(\bar z)|
  \le M|a-\bar a|+M|\bar a|\,|z-\bar z|,                 \tag{5.4}
  \]

  and the identical inequality with \((a,z)\) replaced by \((b,u)\).
  If \(\theta\) is empirical, split
  \(\theta x-\bar\theta\bar x
   =\theta(x-\bar x)+(\theta-\bar\theta)\bar x\).
  Normalized Holder in the coordinate index and ordinary Holder in
  probability give the following direct order count for the bundled maps in
  Section 2.  In the top bundle, controlling \(C^s=a^s\phi'(z^s)\) at order
  \(r\) needs \(a^s,z^s\) at order \(2r\); controlling
  \(z^s=Y^s+h\sum_{q<s}Q_{qs}^{(n)}C^q\) at order \(2r\) needs its inputs at
  order \(4r\).  The map defining \(a^s\) is Lipschitz in already constructed
  \(z\)'s.  In the lower bundle, controlling
  \(u^{s+1}=u^s+hb^s\phi'(u^s)\) at order \(r\) needs \(b^s,u^s\) at order
  \(2r\); controlling \(b^s=D^s+h\sum_{q<s}K_{qs}^{(n)}H^q\) at order
  \(2r\) needs its inputs at order \(4r\), and \(H^{s+1}=\phi(u^{s+1})\) is
  Lipschitz.  The terminal product needs \(a^N,z^N\) at order \(2r\), whose
  construction needs inputs at order at most \(4r\).  Thus an entire
  coordinate micro-step at target order \(r\), not merely one elementary
  node, consumes at most order \(4r\) from the preceding micro-step.  Those
  moments are available by the simultaneous induction hypothesis.  Every
  term retains the \(n^{-1/2}\) rate, and the same inequalities without
  differences give the moment bound.

* **A pair-moment step.**  Lemma 3.2 proves (5.2) at order \(r\) from the
  field assertion at order \(2r\).  Ideal coordinates are iid within the
  relevant physical population by construction in Section 2.

* **A matrix-action step.**  Extend coefficients as in Section 4 and apply
  Lemma 3.3.  Its hypotheses at target order \(r\) are exactly (5.2) at
  order \(8r\) for the preceding micro-step.  The same estimate without
  differences proves uniform moments for the new action.

These cases exhaust the ledger in Section 2.  Thus (5.2) propagates through
at most \(L_N\) explicitly listed micro-steps and terminates at the terminal
output.  In particular, this proves the claimed \(O(n^{-1/2})\) rates without
an invocation of an unspecified state-evolution induction.

Every extended regression coefficient is a finite rational expression of
the empirical moments, with inverse denominators bounded on \({\cal G}_q\)
and replaced by population values outside it.  Equations (3.8)--(3.12) and
(5.2) therefore give convergence in every finite \(L^r\).  Taking any
larger moment than \(1\) proves uniform integrability of all these extended
coefficients.

## 6. Explicit moment tower and stopping probabilities

The preceding simultaneous formulation can be reduced to a single finite
backward tower.  Suppose a conclusion is wanted at moment order \(r_*\ge2\).
Set

\[
 R_{L_N}=r_*,\qquad R_{\ell-1}=8R_\ell
 \quad(1\le\ell\le L_N).                                 \tag{6.1}
\]

Thus

\[
 R_0=8^{L_N}r_*,\qquad L_N=6N+4.                         \tag{6.2}
\]

The three bullets in Section 5 consume respectively at most \(4r\),
\(2r\), and \(8r\) at the preceding step.  Hence (6.1) supplies every
moment used in the proof.  The initialization has moment \(R_0<\infty\),
because it consists of finitely many Gaussian coordinates and an activation
with linear growth.  This proves termination and rules out a hidden
all-orders limit.

We now derive the advertised polynomial failure probability rather than
inferring it from qualitative convergence.  Fix \(m\ge1\), use (6.1) with
terminal order

\[
 r_*=2m.                                                   \tag{6.3}
\]

Before action \(q\), (5.2), entrywise norm equivalence in fixed dimension,
and Weyl's inequality give

\[
 \left\|\lambda_{\min}(G_n)-\lambda_{\min}(G)\right\|_{L^{2m}}
 +\|v_n-v\|_{L^{2m}}
 \le C_{m,q}n^{-1/2}                                     \tag{6.4}
\]

for the extended data.  On \({\cal G}_{q-1}\), those data equal the raw
data.  Since every population quantity in (4.1) is at least \(4\gamma\), a
first failure of (4.2) forces one error in (6.4) to be at least
\(2\gamma\).  Markov's inequality therefore gives

\[
 \mathbb P({\cal G}_q^c\cap{\cal G}_{q-1})
 \le (2\gamma)^{-2m}C_{m,q}^{2m}n^{-m}.                  \tag{6.5}
\]

There are \(2N+1\) actions and finitely many tests per action.  A union bound
gives

\[
 \mathbb P({\cal G}_{2N}^c)\le C_{N,h,M,m}n^{-m}.        \tag{6.6}
\]

This establishes every claimed failure exponent from the explicit finite
initial moment order

\[
 2m\,8^{6N+4}.                                            \tag{6.7}
\]

## 7. Removing stopping, with exponents

Write

\[
 A_s=\|a^s\|_{n,2},\quad U_s=\|u^s\|_{n,2},\quad
 M_s=\|W^s\|_{\mathrm{op}}/\sqrt n .                     \tag{7.1}
\]

The exact finite-width equations imply the deterministic recursion

\[
 \begin{aligned}
 H_s&:=\|H^s\|_{n,2}\le M(1+U_s),\\
 Z_s&:=\|z^s\|_{n,2}\le M_sH_s,\\
 C_s&:=\|C^s\|_{n,2}\le MA_s,\\
 B_s&:=\|b^s\|_{n,2}\le M_sC_s,\\
 A_{s+1}&\le A_s+|h|M(1+Z_s),\\
 U_{s+1}&\le U_s+|h|MB_s,\\
 M_{s+1}&\le M_s+|h|C_sH_s .                             \tag{7.2}
 \end{aligned}
\]

For example,

\[
 \|z^s\|_{n,2}
 =n^{-1/2}\|(W^s/\sqrt n)H^s\|_2
 \le M_s\|H^s\|_{n,2},
\]

and

\[
 \frac1{\sqrt n}\left\|\frac h{\sqrt n}C^s(H^s)^T
 \right\|_{\mathrm{op}}
 =|h|C_sH_s,
\]

which verify the two normalization-sensitive lines of (7.2).

Let

\[
 R_n=1+A_0+U_0+M_0.                                      \tag{7.3}
\]

For an explicit dominating polynomial recursion, initialize

\[
 \widehat A_0=\widehat U_0=\widehat M_0=R_n,
\]

and, for \(0\le s<N\), define in the displayed order

\[
 \begin{aligned}
 \widehat H_s&=M(1+\widehat U_s),&
 \widehat Z_s&=\widehat M_s\widehat H_s,&
 \widehat C_s&=M\widehat A_s,&
 \widehat B_s&=\widehat M_s\widehat C_s,\\
 \widehat A_{s+1}&=\widehat A_s+|h|M(1+\widehat Z_s),&
 \widehat U_{s+1}&=\widehat U_s+|h|M\widehat B_s,&
 \widehat M_{s+1}&=\widehat M_s+|h|\widehat C_s\widehat H_s.
                                                               \tag{7.3a}
 \end{aligned}
\]

After the last update set

\[
 \widehat H_N=M(1+\widehat U_N),\qquad
 \widehat Z_N=\widehat M_N\widehat H_N,
\]

and let \(P_{N,h,M}(R_n)\) be one plus the sum of all hatted quantities in
this finite list.  Induction in (7.2) proves that each unhatted quantity is
bounded by its hatted partner.  The raw conditioning actions also obey

\[
 \|Y^s\|_{n,2}\le M_0H_s,
 \qquad \|D^s\|_{n,2}\le M_0C_s,                         \tag{7.3b}
\]

so they are bounded by the same polynomial.  Recursion (7.3a) performs
exactly seven assignments per nonterminal time and then two terminal
assignments; it therefore terminates and constructs a polynomial with
nonnegative coefficients.

We now prove the initialization moment bound.  Let \(G_n\) be an
\(n\times n\) iid standard Gaussian matrix.  A \(1/4\)-net \({\cal N}\)
of the Euclidean unit sphere exists with \(|{\cal N}|\le9^n\): take a
maximal \(1/4\)-separated set, observe that the disjoint radius-\(1/8\)
balls around its points lie in the radius-\(9/8\) ball, and compare volumes.
For unit \(x,y\), choose net points \(x_0,y_0\) within \(1/4\).  Then

\[
 |y^TG_nx|
 \le |y_0^TG_nx_0|+\tfrac12\|G_n\|_{\rm op},
\]

and consequently

\[
 \|G_n\|_{\rm op}
 \le2\max_{x_0,y_0\in{\cal N}}|y_0^TG_nx_0|.             \tag{7.3c}
\]

For fixed net points, \(y_0^TG_nx_0\sim N(0,1)\), whose exponential
Markov bound is \(\mathbb P(|Z|>t)\le2e^{-t^2/2}\).  A union bound and
(7.3c) give

\[
 \mathbb P\{\|G_n\|_{\rm op}/\sqrt n>y\}
 \le2\exp\{n\log81-ny^2/8\}.                            \tag{7.3d}
\]

For \(y\ge y_0:=4\sqrt{\log81}\), the right side is at most
\(2e^{-ny^2/16}\le2e^{-y^2/16}\).  Integrating the tail gives

\[
 \begin{aligned}
 \mathbb E(\|G_n\|_{\rm op}/\sqrt n)^r
 &=r\int_0^\infty y^{r-1}
     \mathbb P\{\|G_n\|_{\rm op}/\sqrt n>y\}\,dy\\
 &\le y_0^r+2r\int_{y_0}^\infty y^{r-1}e^{-y^2/16}\,dy<\infty, \tag{7.3e}
 \end{aligned}
\]

uniformly in \(n\).  If \(g_1,\ldots,g_n\) are iid standard Gaussians,
then, for \(r\ge2\), convexity gives

\[
 \mathbb E\left(n^{-1}\sum_i g_i^2\right)^{r/2}
 \le n^{-1}\sum_i\mathbb E|g_i|^r=\mathbb E|g_1|^r,     \tag{7.3f}
\]

while for \(0<r<2\), concavity gives an upper bound of \(1\).  This applies
to both \(A_0\) and \(U_0\).  More generally, every normalized
\(\ell^p\)-norm of a fresh Gaussian vector has every fixed outer moment
uniformly in \(n\), by applying the same convexity/concavity argument to
\(n^{-1}\sum_i|g_i|^p\).  Equations (7.3e)--(7.3f) prove

\[
 \sup_n\mathbb E R_n^r<\infty\qquad(r<\infty).            \tag{7.4}
\]

For \(p\ge2\),

\[
 \|x\|_{n,p}\le n^{1/2-1/p}\|x\|_{n,2};                 \tag{7.5}
\]

for \(p\le2\), the factor on the right is unnecessary.  Consequently each
raw field \(X_n\) satisfies

\[
 \|X_n\|_{n,p}
 \le n^{d_p}P_{N,h,M}(R_n),\qquad
 d_p:=\max\{0,\tfrac12-\tfrac1p\}.                       \tag{7.6}
\]

Fix desired mixed orders \(p,P\), and put

\[
 r=\max\{p,P,2\},\qquad m=2r.                            \tag{7.7}
\]

Use the stopped induction at all orders supplied by (6.1) with terminal
order \(2m=4r\).  From (6.6), Holder, (7.4), and (7.6),

\[
 \begin{aligned}
 &\left\|\|X_n\|_{n,p}\mathbf1_{{\cal G}_{2N}^c}
        \right\|_{L^P}\\
 &\quad\le
 n^{d_p}\|P_{N,h,M}(R_n)\|_{L^{2P}}
 \mathbb P({\cal G}_{2N}^c)^{1/(2P)}\\
 &\quad\le C n^{d_p-m/(2P)}
 \le Cn^{-1/2}.                                          \tag{7.8}
\end{aligned}
\]

The last inequality uses \(m=2r\), \(P\le r\), and \(d_p\le1/2\):

\[
 d_p-\frac{m}{2P}
 \le\frac12-\frac rP\le-\frac12.                       \tag{7.9}
\]

Extended and ideal fields have uniformly bounded \(L^{2P}(\|\cdot\|_{n,p})\)
moments by Section 5: apply its diagonal assertion at
\(s=\max\{p,2P,2\}\le2r\) (which is covered by the terminal order
\(4r\) chosen above), then use
\(\|x\|_{n,p}\le\|x\|_{n,s}\) and \(\|Z\|_{L^{2P}}\le\|Z\|_{L^s}\).
Their exceptional-event contributions therefore vanish as well.  On
\({\cal G}_{2N}\) the raw and extended fields agree.  Combining
these facts with (5.2) proves (1.3) for the raw network.  The same argument,
using normalized Cauchy--Schwarz and (7.2), removes stopping from every raw
Gram and cross-moment.

Finally,

\[
 |f_n^N|
 \le \|a^N\|_{n,2}\|\phi(z^N)\|_{n,2}
 \le MA_N(1+Z_N)
 \le M P_{N,h,M}(R_n)\bigl(1+P_{N,h,M}(R_n)\bigr).        \tag{7.10}
\]

By (7.4), the right side is uniformly bounded in \(L^q\) for every finite
\(q\).  Hence \((f_n^N)_n\) is uniformly integrable.  On the coupling,
the coordinate inequalities (5.4), normalized Holder, and the just-proved
raw field convergence show

\[
 f_n^N-n^{-1}\sum_{i=1}^n\bar a_i^N\phi(\bar z_i^N)
 \longrightarrow0\quad\text{in }L^1.                    \tag{7.11}
\]

The summands in the ideal average are iid and integrable, and their common
expectation is \(F_N(h)\).  Taking expectations in (7.11) proves (1.4).
Moreover, every raw Gram or raw cross-moment is bounded in absolute value by
the product of two normalized Euclidean field norms, hence by
\(P_{N,h,M}(R_n)^2\).  Equation (7.4) therefore bounds each such observable
in every finite \(L^q\), proving its uniform integrability in addition to its
convergence.

## 8. Identification of the limiting coefficients

The action induction gives convergence of every entry in (2.1), including
the raw cross blocks \(R,q,k,r,s\).  Equations (4.6)--(4.10) of `PROOF.md`
are finite-dimensional Gaussian integration-by-parts identities for the
ideal particles.  Substituting those identities into the limits of the exact
row and column regression formulas cancels the old-span terms and gives,
respectively,

\[
 Y^s\Longrightarrow \xi_s+\sum_{r<s}\rho_{sr}C_r,
 \qquad
 D^s\Longrightarrow \chi_s+\sum_{r\le s}\sigma_{sr}H_r. \tag{8.1}
\]

The learned rank-one terms are empirical \(Q\)'s and \(K\)'s, already
covered by Lemma 3.2.  Adding them gives exactly the inverse-free operator
DAG.  Thus the coupling identifies the actual fixed-\(h\) network, every
reused-matrix response, and the terminal expectation before any limit
\(h\to0\) is considered.
