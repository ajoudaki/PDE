# Width-first time-doubling theorem

## 1. The result

Let (G\sim N(0,1)).  Assume

\[
\phi\in C^{12}(\mathbb R),\qquad
\mathbb E\phi(G)^2=1,
\]

and

\[
M_\phi=
\max\left\{
1,
\sup_x\frac{|\phi(x)|}{1+|x|},
\max_{1\le r\le12}\|\phi^{(r)}\|_\infty
\right\}<\infty .
\]

For the two-hidden-layer network in Section 2, let (F_{N,n}(h)) be the
expected output after (N) recomputed simultaneous ascent steps of size
(h).  The limit order throughout is

\[
F_N(h)=\lim_{n\to\infty}F_{N,n}(h)
\quad\text{at each fixed }h,
\qquad\text{then }h\to0.
\]

Write (\phi_r=\phi^{(r)}(G)), and define

\[
\begin{aligned}
d&=\mathbb E\phi_1^2,
&e&=\mathbb E\phi_1^4,
&m&=\mathbb E(\phi_0\phi_2\phi_1^2),\\
j&=\mathbb E(\phi_3\phi_1^3),
&s&=\mathbb E(\phi_2^2\phi_1^2),
&\ell&=\mathbb E(\phi_0^2\phi_1^2),\\
b&=\mathbb E(\phi_0\phi_2),
&r&=\mathbb E(\phi_1\phi_3),
&v&=\mathbb E\phi_2^2.
\end{aligned}
\]

Set

\[
c=1+d,\qquad
\beta=b+cr,\qquad
\delta=d+cv,\qquad
k=d+\beta+\delta,
\]

\[
S_\phi
=3c^2m+3c^3j+3de\beta+3dkm+3d^2j,
\]

\[
H_\phi
=c^2e+c\ell+2c^2m+3c^3s+cedv
+2ed^2+3d^2s+k^2\ell+2dkm,
\]

and use the single shared cubic invariant

\[
\boxed{J_\phi=S_\phi+4H_\phi.}
\]

For every fixed integer (t\ge1), the finite envelope compiler in Section
6 returns finite activation-defined numbers

\[
\overline{\mathcal J}_{t,5},\qquad
\overline{\mathcal J}_{2t,5}.
\]

Define

\[
B_{\phi,t}
=\frac{32\overline{\mathcal J}_{t,5}
+\overline{\mathcal J}_{2t,5}}{120},
\qquad
\kappa_{\phi,t}
=-\frac{t(2t-1)}2J_\phi .
\]

Then the actual width-first outputs satisfy

\[
\boxed{
\left|
F_t(2\eta)-F_{2t}(\eta)-\kappa_{\phi,t}\eta^3
\right|
\le B_{\phi,t}|\eta|^5,
\qquad |\eta|\le\frac12 .}
\tag{1.1}
\]

Consequently, for every (\varepsilon>0),

\[
|\eta|\le
\eta_{\phi,t}(\varepsilon)
:=
\min\left\{
\frac12,
\sqrt{\frac{\varepsilon}{1+B_{\phi,t}}}
\right\}
\tag{1.2}
\]

implies

\[
\boxed{
|F_t(2\eta)-F_{2t}(\eta)|
\le
\left(
\frac{t(2t-1)}2|J_\phi|+\varepsilon
\right)|\eta|^3 .}
\tag{1.3}
\]

A coarser explicitly quadratic consequence is

\[
\boxed{
|F_t(2\eta)-F_{2t}(\eta)|
\le (|J_\phi|+\varepsilon)t^2|\eta|^3}
\tag{1.3a}
\]

whenever

\[
|\eta|\le
\min\left\{
\frac12,
t\sqrt{\frac{\varepsilon}{1+B_{\phi,t}}}
\right\}.
\tag{1.3b}
\]

Indeed (t(2t-1)/2\le t^2), and under (1.3b) the fifth-order
contribution is at most (\varepsilon t^2|\eta|^3).

Thus the sharp leading coefficient is exactly quadratic in (t).  The
fifth-order remainder constant is not generally quadratic in (t); Section
9 gives a same-network obstruction.

For the requested concrete case (t=2),

\[
\boxed{
\left|
F_2(2\eta)-F_4(\eta)+3J_\phi\eta^3
\right|
\le
\frac{32\overline{\mathcal J}_{2,5}
+\overline{\mathcal J}_{4,5}}{120}|\eta|^5,
\qquad |\eta|\le\frac12 .}
\tag{1.4}
\]

If \(\phi\) is constant, all discrepancies in this note vanish identically
and \(J_\phi=0\).  The displayed inequalities hold with the compiler
overbound above; on this separate branch one may sharpen it to
\(B_{\phi,t}=0\).

## 2. Exact finite-width network

Let both hidden layers have width (n), let (x\in\mathbb R^p) be
deterministic with (\|x\|^2/p=1), and initialize independently

\[
w_j^0\sim N(0,I_p),\qquad
W_{ij}^0\sim N(0,1),\qquad
a_i^0\sim N(0,1).
\]

At time (s), put

\[
u_j^s=\frac{(w_j^s)^Tx}{\sqrt p},\qquad
H_j^s=\phi(u_j^s),
\]

\[
z_i^s=\frac1{\sqrt n}\sum_jW_{ij}^sH_j^s,
\qquad
f_n^s=\frac1n\sum_i a_i^s\phi(z_i^s),
\]

\[
C_i^s=a_i^s\phi'(z_i^s),\qquad
b_j^s=\frac1{\sqrt n}\sum_iW_{ij}^sC_i^s.
\]

One simultaneous ascent step is

\[
\theta^{s+1}=\theta^s+hn\nabla_\theta f_n^s,
\]

or, exactly,

\[
\begin{aligned}
a_i^{s+1}&=a_i^s+h\phi(z_i^s),\\
W_{ij}^{s+1}&=W_{ij}^s+\frac h{\sqrt n}C_i^sH_j^s,\\
u_j^{s+1}&=u_j^s+h b_j^s\phi'(u_j^s).
\end{aligned}
\tag{2.1}
\]

Every right-hand side in (2.1) is evaluated at time (s).  With

\[
Q_{rs}^{(n)}=\frac1n(H^r)^TH^s,
\qquad
K_{rs}^{(n)}=\frac1n(C^r)^TC^s,
\]

and (W=W^0), the learned rank-one pieces separate exactly as

\[
z^s=\frac{WH^s}{\sqrt n}
+h\sum_{r<s}Q_{rs}^{(n)}C^r,
\]

\[
b^s=\frac{W^TC^s}{\sqrt n}
+h\sum_{r<s}K_{rs}^{(n)}H^r.
\tag{2.2}
\]

The expected finite-width output is (F_{N,n}(h)=\mathbb E f_n^N).

## 3. Inverse-free Gaussian operator DAG

For a fixed terminal index (N), start with independent
(A,U\sim N(0,1)).  The lower Gaussian source
((\chi_0,\ldots,\chi_s)) has covariance

\[
K^{[s]}=(K_{rq})_{0\le r,q\le s},
\qquad K_{rq}=\mathbb E(C_rC_q),
\]

and is independent of (U).  The top source
((\xi_0,\ldots,\xi_s)) has covariance

\[
Q^{[s]}=(Q_{rq})_{0\le r,q\le s},
\qquad Q_{rq}=\mathbb E(H_rH_q),
\]

and is independent of (A).  Different layerwise expectations use fresh
Gaussian blocks; they communicate only through the deterministic (Q,K)
and response coefficients below.  Coordinates within one time block retain
their full covariance.

Set (u_0=U) and (H_s=\phi(u_s)).  At time (s), the already constructed
feature block first supplies the top source (\xi_s).  Define

\[
\rho_{sr}=\mathbb E[\partial_{\chi_r}H_s],
\qquad 0\le r<s,
\]

\[
z_s=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,
\]

\[
a_s=A+h\sum_{r<s}\phi(z_r),
\qquad
C_s=a_s\phi'(z_s).
\tag{3.1}
\]

Now compile (K^{[s]}) and

\[
\sigma_{sr}=\mathbb E[\partial_{\xi_r}C_s],
\qquad 0\le r\le s.
\]

This supplies the lower source (\chi_s).  Define

\[
b_s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
+h\sum_{r<s}K_{rs}H_r,
\qquad
u_{s+1}=u_s+h b_s\phi'(u_s).
\tag{3.2}
\]

Then construct (H_{s+1}), the new entries of (Q^{[s+1]}), and the new
(\rho_{s+1,r}).  Thus the noncircular chronological order at every time is

\[
\xi_s\to z_s,a_s,C_s\to K^{[s]},\sigma_s
\to\chi_s\to b_s,u_{s+1},H_{s+1}
\to Q^{[s+1]},\rho_{s+1}.
\]

It starts from (H_0=\phi(U)) and terminates after (z_N,a_N), without
constructing an unused (C_N) or lower update.

The terminal operator output is

\[
F_N(h)=\mathbb E[a_N\phi(z_N)].
\tag{3.3}
\]

This recursion contains no inverse Gram, so it is defined at (h=0), where
all time coordinates within a source block coalesce.

## 4. Fixed-​(h) identification for arbitrary finite time

This section proves that (3.3) is the width-first limit of the actual
network, rather than merely a formal Gaussian program.

### 4.1 All finite population Grams have full rank

Assume first that (\phi) is nonconstant and (h\ne0).  We prove by
mutual induction that

\[
Q^{[s]}\succ0,
\qquad K^{[s]}\succ0
\qquad(s\ge0).
\tag{4.1}
\]

The base is

\[
Q_{00}=\mathbb E\phi(U)^2=1,
\qquad
K_{00}=\mathbb E[A^2\phi'(\xi_0)^2]
=d>0.
\]

For the induction step, suppose (K^{[s]}\succ0).  Gaussian regression
gives

\[
\chi_s=m_s(\chi_{<s})+\tau_sG_s,
\qquad \tau_s>0,
\]

where (G_s\sim N(0,1)) is fresh.  Conditional on
(\mathcal L_s=\sigma(U,\chi_{<s})), (3.2) has the form

\[
u_{s+1}=r_s+h\tau_s\phi'(u_s)G_s.
\tag{4.2}
\]

The event (\{\phi'(u_s)\ne0\}) has positive probability.  This holds at
(s=0) because a nonconstant (C^1) function has
(\phi'\not\equiv0) and (U) has full support.  If it holds at (s),
then (4.2) has full conditional support on that event, and therefore it
holds at (s+1) as well.

A continuous nonconstant function of a full-support Gaussian has positive
variance.  Hence

\[
\mathbb E\operatorname{Var}(H_{s+1}\mid\mathcal L_s)>0.
\]

Every (H_r), (r\le s), is (\mathcal L_s)-measurable.  Thus, for
all deterministic (v_0,\ldots,v_s),

\[
\mathbb E\left(H_{s+1}-\sum_{r\le s}v_rH_r\right)^2
\ge
\mathbb E\operatorname{Var}(H_{s+1}\mid\mathcal L_s)>0.
\]

This is exactly positivity of the new Schur complement, so
(Q^{[s+1]}\succ0).

If (\phi') is nonconstant, regress the newest top source as

\[
\xi_{s+1}=n_{s+1}(\xi_{\le s})+\upsilon_{s+1}E_{s+1},
\qquad \upsilon_{s+1}>0,
\]

with (E_{s+1}) fresh.  Conditional on
(\mathcal T_{s+1}=\sigma(A,\xi_{\le s})),

\[
C_{s+1}
=a_{s+1}\phi'(q_{s+1}+\upsilon_{s+1}E_{s+1}).
\tag{4.3}
\]

Moreover (\mathbb P(a_{s+1}\ne0)>0).  For (s+1=1), this follows
from (a_1=A+h\phi(\xi_0)).  Later, conditional on
(A,\xi_0,\ldots,\xi_{s-1}), the new term
(h\phi(z_s)) is a nonconstant function of the fresh innovation in
(\xi_s), so it cannot make (a_{s+1}) identically zero.  Since
(\phi') is continuous and nonconstant, (4.3) has positive conditional
variance on a positive-probability event.  The old (C_r)'s are
(\mathcal T_{s+1})-measurable, proving (K^{[s+1]}\succ0).

If (\phi') is constant, write (\phi(x)=px+q), (p\ne0).  The lower
argument above is even simpler, because the fresh conditional variance of
(H_{s+1}) is (h^2p^4\tau_s^2>0).  For (s\ge1), condition on
(A,\xi_0,\ldots,\xi_{s-2}).  Since

\[
C_s=pa_s=pa_{s-1}+hp^2z_{s-1}+hpq,
\]

its fresh conditional variance is (h^2p^4) times the newest Schur
complement of (Q^{[s-1]}), which is positive.  This proves the affine
branch and closes the mutual induction (4.1).  No expansion in (h) has
been used.

Chronologically, the induction is

\[
(Q^{[s]},K^{[s]})
\Longrightarrow Q^{[s+1]}
\Longrightarrow K^{[s+1]},
\]

which is the same order as the operator construction in Section 3.

### 4.2 Adaptive reused-matrix conditioning

Expose the initial (W) in the predictable order

\[
Y^0,D^0,Y^1,D^1,\ldots,Y^{N-1},D^{N-1},Y^N,
\]

where

\[
Y^s=WH^s/\sqrt n,
\qquad D^s=W^TC^s/\sqrt n.
\]

After (Y^s), (C^s) is known; after (D^s), (H^{s+1}) is known.
Thus every new query is measurable before its matrix action is revealed,
including the dependence of (H^1) on the reused column action (D^0).

Let \(\mathcal F\) be the full filtration generated by the external marks,
the old row and column queries, and their revealed actions.  If \(H,C\)
collect those queries, then the following is an equality in conditional law
given \(\mathcal F\):

\[
W\ \overset d=\ P_CW+WP_H-P_CWP_H
   +P_C^\perp\widetilde W P_H^\perp,
\tag{4.4}
\]

where (\widetilde W) is a fresh standard Gaussian matrix.  This follows
inductively by decomposing each predictable new query into its old-span and
orthogonal parts.  Revealing the corresponding action fixes one Gaussian
projection of the last term in (4.4), and Gaussian orthogonality leaves a
fresh double-orthogonal block for the next action.

More explicitly, immediately before (Y^s), the filtration contains the
external marks, (H^0,\ldots,H^s), (C^0,\ldots,C^{s-1}), and all earlier
actions through (D^{s-1}).  Immediately before (D^s), it additionally
contains (Y^s,z^s,a^s,C^s).  Thus the row query (H^s) and the column
query (C^s) are predictable with respect to their respective filtrations.

If

\[
Q=H^TH/n,\qquad K=C^TC/n,
\qquad R=C^T(WH/\sqrt n)/n,
\]

the exact new-row regression for a predictable \(v\), realized on a
conditional coupling, is

\[
\frac{Wv}{\sqrt n}
=YQ^{-1}q
+CK^{-1}(s-RQ^{-1}q)
+\tau_vP_C^\perp g,
\tag{4.5a}
\]

where

\[
q=H^Tv/n,
\qquad s=(W^TC/\sqrt n)^Tv/n,
\qquad
\tau_v^2=v^TP_H^\perp v/n,
\]

and \(g\sim N(0,I_n)\) is fresh conditionally on \(\mathcal F\).

The transposed new-column regression for a predictable (c_*) is

\[
\frac{W^Tc_*}{\sqrt n}
=DK^{-1}k
+HQ^{-1}(r-R^TK^{-1}k)
+\tau_{c_*}P_H^\perp g,
\tag{4.5b}
\]

where

\[
k=C^Tc_*/n,
\qquad r=Y^Tc_*/n,
\qquad
\tau_{c_*}^2=c_*^TP_C^\perp c_*/n,
\]

with a fresh conditional \(N(0,I_n)\) vector for this action.

At a rank-deficient finite-width query block, (4.5a)--(4.5b) hold with
Moore--Penrose inverses because they are identities between orthogonal
projectors.  In the convergence proof the rational inverse formulas are
used only on the stopped full-rank event; off it, the proof returns to the
raw network (2.1) and never asserts that an untruncated empirical inverse
coefficient is defined or uniformly integrable.

It remains to identify every deterministic regression response.  At an
arbitrary stage write the already exposed population actions in block form

\[
y=\xi+Pc,
\qquad
d_0=\chi+Sh_0,
\tag{4.5c}
\]

where (P) contains the strictly causal (\rho)'s and (S) contains the
causal (\sigma)'s.  Put

\[
Q=\mathbb E(h_0h_0^T),
\qquad K=\mathbb E(cc^T).
\]

We use Gaussian integration by parts in the following explicit form.  If
\(X=BG\), \(G\sim N(0,I)\), and \(f\) is \(C^1\) with polynomially
bounded value and gradient, coordinate integration by parts for \(G\)
gives

\[
\mathbb E[Xf(X)^T]
=B\mathbb E[Gf(BG)^T]
=BB^T\mathbb E[Df(X)^T].
\]

All current fields and first derivatives have the required polynomial
envelopes.  Applying this identity gives the complete old cross block

\[
R:=\mathbb E(cy^T)=SQ+KP^T.
\tag{4.6}
\]

For a new feature query (H_*), let

\[
q=\mathbb E(h_0H_*),
\qquad
\rho=\mathbb E\nabla_\chi H_*.
\]

Then

\[
v:=\mathbb E(d_0H_*)=K\rho+Sq.
\tag{4.7}
\]

Substitution of (4.5c)--(4.7) into the exact row-regression formula from
(4.4) cancels the two (P^TQ^{-1}q) terms and leaves

\[
Y^s\Longrightarrow\xi_s+\sum_{r<s}\rho_{sr}C_r.
\tag{4.8}
\]

For a new cotangent query (C_*), set

\[
k=\mathbb E(cC_*),
\qquad
\sigma=\mathbb E\nabla_\xi C_*.
\]

Integration by parts gives

\[
r:=\mathbb E(yC_*)=Q\sigma+Pk.
\tag{4.9}
\]

The exact column-regression formula (4.5b) now cancels the two
(S^TK^{-1}k) terms and leaves

\[
D^s\Longrightarrow\chi_s+\sum_{r\le s}\sigma_{sr}H_r.
\tag{4.10}
\]

Adding the exact learned-(W) terms from (2.2) gives precisely (3.1) and
(3.2).  Equations (4.6)--(4.10) hold for blocks of every finite size, so
they include all later reused-row and reused-column effects without an
additional cavity assumption.

### 4.3 Concentration and uniform integrability

**Proposition 4.3 (fixed-step probabilistic bridge).**  Fix \(N<\infty\)
and \(h\ne0\).  For the action list

\[
Y^0,D^0,Y^1,D^1,\ldots,Y^{N-1},D^{N-1},Y^N,
\]

there is one joint coupling of the raw finite-width network, an extended
stopped ledger, and iid population particles with the following properties.

1. On the nested good event through action \(q\), the extended ledger equals
   the raw network through that action.
2. Every extended value field has normalized mixed-\(L^p\) error
   \(O(n^{-1/2})\), and every empirical Gram and raw cross-moment has
   \(L^p\) error \(O(n^{-1/2})\), at every prescribed finite moment order.
3. Every conditional-regression coefficient, extended by its population
   value off the good event, converges in every finite \(L^p\) and is
   uniformly integrable.
4. If \({\cal G}\) is the final good event, then for every \(m<\infty\),

   \[
   \mathbb P({\cal G}^c)\le C_{N,h,\phi,m}n^{-m}.
   \tag{4.11}
   \]

5. Stopping can be removed from all raw fields, Grams, cross-moments, and
   the terminal output.  The terminal outputs are uniformly integrable and

   \[
   \lim_{n\to\infty}F_{N,n}(h)=F_N(h).
   \tag{4.12}
   \]

**Proof.**  The complete proof is in
WIDTH_CONCENTRATION_CLOSURE.md; here we record its exact dependencies so
that no different stopping convention is implicit.  Its Section 2 lists at
most \(L_N=6N+4\) micro-steps.  Lemmas 3.1--3.3 prove respectively the iid
average estimate, pair-moment transfer, and one adaptive Gaussian-action
estimate.  The last lemma uses the exact conditioning identities
(4.4)--(4.5b) above.

The spectral margin in equation (4.1) of that supplement is one fourth of
the minimum over **all** population Grams and query Schur complements in the
finite ledger, including the terminal \(Y^N\) innovation.  Positivity is
provided by Section 4.1 above.  The construction generates the raw action
from its exact Moore--Penrose conditional kernel on every event; it defines
the extended action separately, using the exact coefficients on the good
event and the population coefficients off it.  Thus the raw network is
never set to zero or altered.

For a target moment \(r_*\), the explicit backward tower is

\[
R_{L_N}=r_*,
\qquad R_{\ell-1}=8R_\ell,
\qquad R_0=8^{6N+4}r_*.
\tag{4.13}
\]

Taking \(r_*=2m\), the \(L^{2m}\) Gram and Schur-complement errors and
Markov's inequality give (4.11), action by action.  Section 7 of the
supplement gives a finite seven-assignment energy recursion for the raw
network and proves the Gaussian initialization bounds by a sphere-net
argument.  With target mixed orders \(p,P\), it takes
\(r=\max\{p,P,2\}\) and \(m=2r\); the discarded-event exponent is

\[
d_p-\frac{m}{2P}
\le \frac12-\frac rP\le-\frac12,
\qquad
d_p=\max\{0,\tfrac12-\tfrac1p\}.
\tag{4.14}
\]

This removes stopping.  Its terminal polynomial majorant has moments of
every finite order, proving uniform integrability and (4.12).  Finally,
Section 8 substitutes the converged raw cross-moments into
(4.6)--(4.10), identifying every reused-matrix response and hence exactly
the inverse-free DAG (3.1)--(3.3).  This proves the proposition.  \(\square\)

For \(h=0\), the update is the identity and both sides of (4.12) are zero
by the centered readout.  If \(\phi\) is constant, normalization gives
\(\phi\equiv\pm1\) and the direct finite-width identity
\(\mathbb E f_n^N=Nh\), so no cotangent Gram is inverted.

## 5. Singular-covariance regularity

The cutoff--mollifier passage, uniform Gaussian-tail domination, and the
fivefold fundamental-theorem-of-calculus closure used in this section are
proved in full in `REGULARITY_SUPPLEMENT.md`, Lemma S.1.  In particular,
that proof establishes joint continuity of every limiting differentiated
integrand and never uses an inverse covariance or a continuous choice of a
covariance square root.

For a positive-semidefinite covariance (C), including a singular one,
write

\[
\Gamma_C[\psi]=\mathbb E\psi(X),
\qquad X\sim N(0,C).
\]

If (C(h)\) is (C^5) and every mixed derivative

\[
\partial_h^j\partial_x^\alpha\psi(h,x),
\qquad
j+\left\lceil\frac{|\alpha|}{2}\right\rceil\le5,
\]

exists, is jointly continuous in ((h,x)), and has a common polynomial
envelope, then

\[
\frac d{dh}\Gamma_{C(h)}[\psi_h]
=\Gamma_{C(h)}\left[
\partial_h\psi_h+\frac12C'(h):D_x^2\psi_h
\right],
\tag{5.1}
\]

and the node is (C^5), even when (C(h)) is singular or changes rank.

For completeness, (5.1) does not use (C^{-1}).  For a Schwartz integrand,
Fourier inversion differentiates
(\exp(-\zeta^TC(h)\zeta/2)) and gives (5.1) directly.  For a
polynomial-growth integrand, multiply by a smooth cutoff, mollify, and use
the common polynomial envelope plus the uniform Gaussian moment bound

\[
\sup_{|h|\le1}\mathbb E(1+\|X_{C(h)}\|)^q<\infty
\]

to pass first through the mollification and then through the cutoff.
Repeating the same argument five times proves (5.1) at every required order.
Applied chronologically to (3.1)--(3.3), it proves (F_N\in C^5([-1,1]))
for every fixed (N).  Section 6 supplies the domination rather than
assuming it.

## 6. Explicit finite activation-envelope compiler

This section defines (\overline{\mathcal J}_{N,5}) without using an
output supremum or a trained-trajectory modulus.

An envelope pair ((A,p)) denotes

\[
|g(x)|\le A(1+\|x\|)^p.
\]

Use

\[
(A,p)\oplus(B,q)=(A+B,\max\{p,q\}),
\qquad
(A,p)\odot(B,q)=(AB,p+q).
\]

For a scalar (\lambda), also define

\[
\lambda\odot(A,p)=(|\lambda|A,p).
\]

On (|h|\le1), initialize

\[
\mathcal E(1)=\mathcal E(h)=(1,0),
\qquad
\mathcal E(x_i)=(1,1).
\]

For a syntactic expression (g), set

\[
\mathcal E(\phi(g))=(M_\phi(1+A),p)
\quad\text{if }\mathcal E(g)=(A,p),
\]

and

\[
\mathcal E(\phi^{(r)}(g))=(M_\phi,0),
\qquad1\le r\le12.
\]

Generate derivatives by the primitive rules

\[
\partial_hh=1,
\qquad
\partial_{x_i}x_j=\mathbf1_{\{i=j\}},
\]

with every other primitive derivative zero, and by

\[
\partial(uv)=(\partial u)v+u(\partial v),
\qquad
\partial(\phi^{(r)}(u))
=\phi^{(r+1)}(u)\partial u.
\]

If an earlier
scalar node (S(h)) has already received numerical bounds
(\bar S_0,\ldots,\bar S_5), represent its (j)-th derivative by a token
(S^{[j]}) with

\[
\mathcal E(S^{[j]})=(\bar S_j,0),
\qquad
\partial_hS^{[j]}=S^{[j+1]},
\qquad
\partial_{x_i}S^{[j]}=0.
\]

The first rule is used only for (0\le j<5); the guarded recursion below
never differentiates (S^{[5]}).

For a Gaussian node

\[
N(h)=\Gamma_{C(h)}[\psi_h]
\]

of dimension (m), suppose earlier passes have constructed

\[
\bar c_j\ge
\sup_{|h|\le1}\|C^{(j)}(h)\|_\Sigma,
\qquad0\le j\le5,
\]

where (\|A\|_\Sigma=\sum_{i,j}|A_{ij}|).  Put

\[
R^{(0)}_{j,q}
=\bigoplus_{|\alpha|=q}
\mathcal E(\partial_h^j\partial_x^\alpha\psi)
\]

for (j+\lceil q/2\rceil\le5), and, only when

\[
r+j+\left\lceil\frac q2\right\rceil<5,
\]

recurse on the finite index set by

\[
R^{(r+1)}_{j,q}
=R^{(r)}_{j+1,q}
\oplus
\bigoplus_{\ell=0}^j
\left[
\frac12\binom j\ell\bar c_{\ell+1}
\odot R^{(r)}_{j-\ell,q+2}
\right].
\tag{6.1}
\]

If (R^{(r)}_{0,0}=(A_r,p_r)), define

\[
\overline{\mathcal J}_r(N)
=A_r\mu_{m,p_r}(\bar c_0),
\]

where

\[
\mu_{m,p}(v)
=\mathbb E(1+\sqrt v\|G_m\|)^p
=\sum_{q=0}^p
\binom pqv^{q/2}2^{q/2}
\frac{\Gamma((m+q)/2)}{\Gamma(m/2)}.
\tag{6.2}
\]

To verify the majorant, set

\[
\Psi_0=\psi,
\qquad
\Psi_{r+1}=\partial_h\Psi_r+\frac12C':D_x^2\Psi_r.
\]

Leibniz's rule shows inductively that (6.1) envelopes every required
(\partial_h^j\partial_x^\alpha\Psi_r).  Formula (5.1) gives
(N^{(r)}=\Gamma_C[\Psi_r]), and (6.2) therefore proves

\[
|N^{(r)}(h)|\le\overline{\mathcal J}_r(N),
\qquad |h|\le1.
\tag{6.3}
\]

For a newly constructed covariance with entries (N_{ab}), set

\[
\bar c_j^{\rm new}
=\sum_{a,b}\overline{\mathcal J}_j(N_{ab}).
\]

In particular, whenever a Gram entry is compiled, define explicitly

\[
\bar Q_{rq,j}=\overline{\mathcal J}_j(Q_{rq}),
\qquad
\bar K_{rq,j}=\overline{\mathcal J}_j(K_{rq}),
\]

and for responses use

\[
\bar\rho_{rq,j}=\overline{\mathcal J}_j(\rho_{rq}),
\qquad
\bar\sigma_{rq,j}=\overline{\mathcal J}_j(\sigma_{rq}).
\]

For (L=\rho+hQ), use

\[
\bar L_j=\bar\rho_j+\bar Q_j+j\bar Q_{j-1},
\qquad \bar Q_{-1}=0.
\tag{6.4}
\]

The general chronological compiler is now completely specified:

1. Construct (H_0=\phi(U)), so (Q_{00}=1).  With top covariance
   (\operatorname{diag}(1,Q_{00})), whose derivative bounds are
   (\bar c_0=2) and (\bar c_j=0) for (j\ge1), construct
   (z_0=\xi_0), (a_0=A), and (C_0=A\phi'(\xi_0)).  Compile
   (K_{00}=d) and (\sigma_{00}=0).
2. For (s=0,\ldots,N-1), use the lower covariance
   (\operatorname{diag}(1,K^{[s]})), with numerical bounds

   \[
   \bar c_j=\mathbf1_{\{j=0\}}
   +\sum_{r,q\le s}\bar K_{rq,j},
   \]

   to construct (b_s,u_{s+1},H_{s+1}).  Compile every new
   (Q_{r,s+1}), (0\le r\le s+1), every
   (\rho_{s+1,r}), (0\le r\le s), and the corresponding (L)'s.
3. With top covariance (\operatorname{diag}(1,Q^{[s+1]})), whose bounds
   are

   \[
   \bar c_j=\mathbf1_{\{j=0\}}
   +\sum_{r,q\le s+1}\bar Q_{rq,j},
   \]

   construct (z_{s+1},a_{s+1}) and compile the terminal integrand
   (F_{s+1}=\mathbb E[a_{s+1}\phi(z_{s+1})]).  If (s+1<N), also
   construct (C_{s+1}), compile every new (K_{r,s+1}), and compile
   every (\sigma_{s+1,r}), (0\le r\le s+1), before returning to
   step 2.
4. At the final top pass define

   \[
   \overline{\mathcal J}_{N,5}
   :=\overline{\mathcal J}_5(F_N).
   \]

This is an algorithm, not a circular definition.  It has (2N) internal
passes and one terminal pass.  The Price index set

\[
\{(r,j,q):r+j+\lceil q/2\rceil\le5\}
\]

is finite.  On it (j+q\le10).  A response integrand starts with an
activation derivative of order at most two, so no derivative beyond
(\phi^{(12)}) occurs.  More explicitly, Lemmas S.2--S.3 of
`REGULARITY_SUPPLEMENT.md` prove by chronological structural induction that
all raw state integrands have activation order at most one, responses have
order at most two, and a reachable term applies at most
(2r+j+q\le10) additional formal derivatives.  Every node is compiled only
after all of its scalar
coefficients and covariance entries.  Hence the compiler terminates for
each fixed (N) and uses only (M_\phi), finite Gaussian moments, and
integer arithmetic.  In particular, (6.3) proves

\[
|F_N^{(5)}(h)|\le\overline{\mathcal J}_{N,5},
\qquad |h|\le1,
\tag{6.5}
\]

without defining the right side through (F_N) or its trajectory.

## 7. Cubic jet of the width-first DAG

The complete product-rule and finite-sum ledger for this section is
`CUBIC_JET_COMPLETE_LEDGER.md`.  That supplement is part of the proof: it
derives (7.1)--(7.9) from the operator recursion, displays every atom in
the calculations of \(R_N'''(0)\) and \(E_{3,N}\), proves all finite-sum
identities by induction, accounts for both singular-covariance Price
terms, and performs the final coefficient grouping without computer
algebra.  The shorter presentation here records its outputs in the order
in which the DAG produces them.

Under

\[
h\mapsto-h,
\qquad A\mapsto-A,
\qquad \chi\mapsto-\chi,
\]

the recursion leaves (u,H,z,Q,K) unchanged and changes the sign of
(a,C,b,\rho,\sigma,L).  The Gaussian laws are invariant, so every
(F_N) is odd.  In particular all even derivatives at zero vanish.

We now differentiate only the already identified inverse-free DAG.  At
(h=0), the lower source coordinates coalesce to (X\sim N(0,d)), and
activation arguments in each layerwise expectation coalesce to a standard
Gaussian (G).  Write

\[
g=\phi(G),\qquad p=\phi'(G),\qquad q=\phi''(G).
\]

Direct differentiation of (3.2) gives, for a time index (v),

\[
u_v'=vXp,
\qquad
u_v''=v(v-1)(kgp+X^2pq),
\]

and hence

\[
H_v'=vXp^2,
\qquad
H_v''=v(2v-1)X^2p^2q+v(v-1)kgp^2.
\]

Therefore the complete feature-Gram second derivative is

\[
\boxed{
Q_{rv}''(0)
=dm\{r(2r-1)+v(2v-1)\}
+k\ell\{r(r-1)+v(v-1)\}
+2rvde.}
\tag{7.1}
\]

To keep every response contribution visible, set

\[
R_N=\sum_{r<N}\rho_{Nr},
\quad
T_2(N)=\frac{N(N-1)(2N-1)}6,
\quad
C_2(N)=\frac{N(N-1)}2,
\quad
C_3(N)=\frac{N(N-1)(N-2)}6.
\]

Differentiate (3.2) with respect to every old \(\chi_r\), then three times
in \(h\).  Equations (3.3)--(3.12) of the complete ledger enumerate the
four directional product-rule atoms, their expectations, and their finite
sums.  They give

\[
\boxed{
\begin{aligned}
R_N'''(0)={}&
\frac32N(4N^2-3N+1)dj\\
&+6N(N-1)(2N-1)ds\\
&+3N(N-1)(2N-1)km\\
&+N(N-1)e\{(\delta+d)(N-2)+\beta(2N-1)\}.
\end{aligned}}
\tag{7.2}
\]

There is no omitted (K'')-Price term in (7.2): the possible correction
differentiates

\[
\left.\partial_h\sum_{r<N}\partial_{\chi_r}H_N\right|_{h=0}
=Np^2,
\]

which is independent of (\chi).  Since
(L_{Nr}=\rho_{Nr}+hQ_{rN}),

\[
\sum_{r<N}L_{Nr}'''(0)
=R_N'''(0)+3\sum_{r<N}Q_{rN}''(0),
\tag{7.3}
\]

and summing (7.1) gives

\[
\boxed{
\begin{aligned}
\sum_{r<N}Q_{rN}''(0)={}&
\frac{N(16N^2-15N+5)}6dm\\
&+\frac{2N(N-1)(2N-1)}3k\ell
+N^2(N-1)de.
\end{aligned}}
\tag{7.4}
\]

At the terminal top node, equations (5.1)--(5.10) of the complete ledger
derive, from the \(a,z,C,L\) recursions,

\[
a_N'=Ng,
\qquad
a_N''=N(N-1)cAp^2,
\]

\[
a_N'''
=cN(N-1)(N-2)gp^2
+\frac12c^2N(N-1)(4N-5)A^2p^2q,
\]

\[
z_N'=NcAp,
\qquad
z_N''=cN(N-1)(gp+cA^2pq).
\]

Writing \(L_N^{(3)}=\sum_{r<N}L_{Nr}'''(0)\), equation (6.1) of the complete
ledger has seven displayed atoms (the two summands inside its third
brace are kept separate).  The expectation of every atom is listed in
its equation (6.2); summing them before the source-law Price correction
gives

\[
\boxed{
\begin{aligned}
E_{3,N}={}&
2cN(N-1)(2N-1)\ell\\
&+2c^2N(N-1)(2N-1)e\\
&+\frac12c^2N(28N^2-33N+11)m\\
&+\frac32c^3N(4N^2-3N+1)j\\
&+6c^3N(N-1)(2N-1)s+dL_N^{(3)}.
\end{aligned}}
\tag{7.5}
\]

The first terminal integrand derivative, before coalescing the top source
coordinates, is

\[
\psi_1
=\left(\sum_{r<N}\phi(x_r)\right)\phi(x_N)
+cA^2\left(\sum_{r<N}\phi'(x_r)\right)\phi'(x_N).
\]

Its historical diagonal Hessians have expectation (\beta), its terminal
diagonal Hessian (N\beta), its historical-terminal Hessians (\delta),
and its distinct historical Hessians zero.  Thus the entire singular
source-covariance correction is

\[
\boxed{
P_N
=\frac32\beta\left{
\sum_{r<N}Q_{rr}''(0)+NQ_{NN}''(0)
\right}
+3\delta\sum_{r<N}Q_{rN}''(0).}
\tag{7.6}
\]

The remaining sum from (7.1) is

\[
\begin{aligned}
\sum_{r<N}Q_{rr}''(0)+NQ_{NN}''(0)
={}&\frac{N(16N^2-15N+5)}3dm\\
&+\frac{4N(N-1)(2N-1)}3k\ell\\
&+\frac{N(8N^2-3N+1)}3de.
\end{aligned}
\tag{7.7}
\]

Substituting (7.2)--(7.4) and (7.7) into (7.5)--(7.6), and using
(k=d+\beta+\delta), yields the following two-polynomial decomposition.
For completeness, equations (8.1)--(8.10) of the ledger give the full
coefficient proof: after defining \(\mathcal A_N,\mathcal B_N,U_N,V_N,W_N\),
they separately group the (j,s,m,\ell,e) terms and verify the three
polynomial identities needed for the grouping.

\[
\boxed{
F_N'''(0)
=\frac{N(4N^2-3N+1)}2S_\phi
+2N(N-1)(2N-1)H_\phi.}
\tag{7.8}
\]

At first order (Q'(0)=0), and direct differentiation of the terminal
integrand gives

\[
\boxed{F_N'(0)=N(1+d+d^2).}
\tag{7.9}
\]

Every term in (7.8) arose from (7.1)--(7.7); no finite-width initialization
jet or opposite-order limit was inserted.

## 8. Time doubling and the three concrete comparisons

Let

\[
D_t(\eta)=F_t(2\eta)-F_{2t}(\eta).
\]

Equation (7.9) gives (D_t'(0)=0).  If

\[
A_N=\frac{N(4N^2-3N+1)}2,
\qquad
B_N=2N(N-1)(2N-1),
\]

then direct algebra gives

\[
8A_t-A_{2t}=-3t(2t-1),
\qquad
8B_t-B_{2t}=-12t(2t-1).
\]

Therefore (7.8) yields

\[
\frac{D_t'''(0)}6
=-\frac{t(2t-1)}2(S_\phi+4H_\phi)
=\kappa_{\phi,t}.
\tag{8.1}
\]

Oddness gives

\[
D_t(0)=D_t''(0)=D_t^{(4)}(0)=0.
\]

For (|\eta|\le1/2), both arguments (\eta) and (2\eta) lie in the
compiler interval.  By (6.5),

\[
|D_t^{(5)}(x)|
\le32\overline{\mathcal J}_{t,5}
+\overline{\mathcal J}_{2t,5}.
\tag{8.2}
\]

Taylor's integral formula through order four, applied only after the
width-first identification, gives

\[
D_t(\eta)-\kappa_{\phi,t}\eta^3
=\frac1{24}\int_0^\eta
(\eta-x)^4D_t^{(5)}(x)\,dx.
\]

Since

\[
\frac1{24}\int_0^{|\eta|}(|\eta|-x)^4\,dx
=\frac{|\eta|^5}{120},
\]

(8.2) proves (1.1).  Under (1.2),

\[
B_{\phi,t}|\eta|^2
\le\frac{B_{\phi,t}}{1+B_{\phi,t}}\varepsilon
\le\varepsilon,
\]

which proves (1.3).

For the first four terminal indices, run the compiler once and define the
three shared activation quantities

\[
\boxed{
J_\phi=S_\phi+4H_\phi,
\qquad
R_\phi=\frac1{120}
\max_{1\le N\le4}\overline{\mathcal J}_{N,5},
\qquad
h_*=\frac13.}
\tag{8.3}
\]

They give all three concrete estimates on the same interval
(|\eta|\le h_*):

\[
\begin{array}{c|c|c}
\text{discrepancy }D(\eta)
&\text{cubic coefficient }\kappa
&\text{remainder }|D-\kappa\eta^3|\\ \hline
F_2(\eta/2)-F_1(\eta)
&J_\phi/16
&(33/32)R_\phi|\eta|^5\\
F_3(\eta)-F_1(3\eta)
&(5/2)J_\phi
&244R_\phi|\eta|^5\\
F_2(2\eta)-F_4(\eta)
&-3J_\phi
&33R_\phi|\eta|^5.
\end{array}
\tag{8.4}
\]

The three numerical remainder multipliers are exactly

\[
1+2^{-5}=\frac{33}{32},
\qquad
1+3^5=244,
\qquad
2^5+1=33.
\]

Thus the only changing quantities in the three concrete bounds are explicit
numbers.  A single simultaneous (\varepsilon)-radius is

\[
|\eta|\le
\min\left\{
\frac13,
\sqrt{\frac{\varepsilon}{1+244R_\phi}}
\right\}.
\tag{8.5}
\]

On (8.5), each discrepancy is at most
((|\kappa|+\varepsilon)|\eta|^3).

The same finite-horizon sharing works for the general theorem.  For a chosen
integer (T\ge1), run one compiler through time (2T) and set

\[
R_{\phi,T}
=\frac1{120}\max_{1\le N\le2T}
\overline{\mathcal J}_{N,5}.
\]

Then, simultaneously for every (1\le t\le T),

\[
\left|D_t(\eta)-\kappa_{\phi,t}\eta^3\right|
\le33R_{\phi,T}|\eta|^5,
\qquad |\eta|\le\frac12.
\tag{8.6}
\]

Thus one numerical activation-envelope constant is shared over every fixed
finite time horizon.  Passing from all finite horizons to one constant valid
for unbounded (t) is precisely the uniform-stability issue audited next.

## 9. Audit of uniform dependence on (t)

The exact coefficient in (8.1) is quadratic in (t), as conjectured.
There are two different possible claims about the remainder:

1. The fixed-​(t) theorem (1.1) is proved for every integer (t), using
   the same activation data and the same terminating compiler rules.
2. A stronger estimate with one numerical (C_\phi), such as

   \[
   |D_t(\eta)-\kappa_{\phi,t}\eta^3|
   \le C_\phi t^\alpha|\eta|^5
   \quad\text{for all }t,
   \tag{9.1}
   \]

   requires a uniform-in-time estimate for the compiler outputs.  The
   finite chronological proof in Section 6 does not supply one merely by
   terminating separately for each (t).

In particular, (\alpha=2) in (9.1) is false.  This can already be seen
inside the same network with the admissible activation (\phi(x)=x).
For that activation the Gaussian DAG is linear.  A direct truncated
covariance recursion, stated and proved in
[the linear-activation audit](./LINEAR_ACTIVATION_AUDIT.md), gives

\[
[\eta^5]F_N(\eta)
=20\binom N2+465\binom N3
+1702\binom N4+1464\binom N5.
\tag{9.2}
\]

Consequently,

\[
\boxed{
[\eta^5]D_t(\eta)
=-\frac{2452}{3}t^4+1896t^3
-\frac{4403}{3}t^2+369t.}
\tag{9.3}
\]

If (9.1) held on any punctured neighborhood of zero with (\alpha<4),
divide by (|\eta|^5) after subtracting the cubic term and let
(\eta\to0) at each fixed (t).  Equation (9.3) would give a quartic
polynomial bounded by (C_\phi t^\alpha), a contradiction as
(t\to\infty).  Thus quartic dependence is necessary for a shared
fifth-order coefficient.

There is an abstract sufficient condition for the natural sharp scale.  Let
(P_h) be a (C^5) family on a fixed Banach space for (|h|\le r), satisfying

\[
P_0=I,
\qquad
\|P_h\|\le1,
\qquad
\|P_h^{(j)}\|\le L_{\phi,j}
\quad(1\le j\le5),
\]

and suppose (F_N(h)=\Lambda(P_h^Ng)) with
(\|\Lambda\|\,\|g\|\le R_\phi).  Fix (0<c_\phi\le r/2).  Under these
hypotheses,

\[
P_{2h}^t-P_h^{2t}
=\sum_{q=0}^{t-1}
P_{2h}^{t-1-q}(P_{2h}-P_h^2)P_h^{2q}.
\tag{9.4}
\]

The local defect \(E_h=P_{2h}-P_h^2\) has zero derivatives of orders zero
and one because \(P_0=I\).  Put

\[
L_{\phi,0}=1,\qquad
\Lambda_\phi=\max\left\{1,
\max_{1\le j\le5}(2^jL_{\phi,j})^{1/j}\right\},
\]

and, for \(2\le j\le5\),

\[
D_j=2^jL_{\phi,j}
+\sum_{a=0}^j\binom jaL_{\phi,a}L_{\phi,j-a}.
\]

Thus

\[
\|E_h\|\le\frac{D_2}{2}|h|^2,qquad
\|E_h'\|\le D_2|h|,qquad
\|E_h^{(j)}\|\le D_j\quad(2\le j\le5),
\tag{9.5a}
\]

where the first two inequalities are the integral Taylor formulas for
\(E_h\) and \(E_h'\).  A product of at most \(2t\) factors, each equal to
some \(P_h\) or \(P_{2h}\), has \(r\)-th derivative bounded by
\((2t\Lambda_\phi)^r\): expand the product rule over derivative allocations
\((r_1,\ldots,r_m)\), use
\(\|\partial_h^{r_i}P_h\|,\|\partial_h^{r_i}P_{2h}\|
\le\Lambda_\phi^{r_i}\), and sum the multinomial coefficients to obtain
\(m^r\le(2t)^r\).

In a summand of (9.4), choose \(b\) of the five derivatives to hit \(E_h\)
and distribute the other \(5-b\) derivatives among its at most \(2t\)
outer factors.  On \(|h|\le c_\phi/t\), (9.5a), followed by the sum over
the \(t\) telescoping terms, gives

\[
\left\|\partial_h^5(P_{2h}^t-P_h^{2t})\right\|
\le C_{\phi}^{\rm op}t^4,
\qquad |h|\le c_\phi/t.
\tag{9.5}
\]

Here the completely explicit product-rule constant is

\[
\begin{aligned}
C_{\phi}^{\rm op}={}&
\frac{D_2c_\phi^2}{2}(2\Lambda_\phi)^5
+5D_2c_\phi(2\Lambda_\phi)^4
+10D_2(2\Lambda_\phi)^3\\
&+10D_3(2\Lambda_\phi)^2
+5D_4(2\Lambda_\phi)+D_5.
\end{aligned}
\tag{9.5b}
\]

It would follow that

\[
|D_t(h)-\kappa_{\phi,t}h^3|
\le \frac{R_\phi C_{\phi}^{\rm op}}{120}
t^4|h|^5,
\qquad |h|\le c_\phi/t,
\tag{9.6}
\]

and then the whole discrepancy would indeed be bounded by a quadratic
multiple of (|h|^3), because
(t^4h^5\le c_\phi^2t^2|h|^3) on that interval.

However, the actual reused-matrix width-first DAG has not been proved in
this study to be a single uniformly (C^5) bounded-operator family on a
fixed Banach space.  Section 4 proves the exact network-to-DAG bridge at
every finite time, but Section 6 gives only a finite-time envelope.  Thus
(9.5)--(9.6) are a conditional operator theorem, not an unconditional claim
about the network.  The unconditional general result is (1.1)--(1.3), and
the requested quadratic fifth-order remainder is disproved by (9.3).
