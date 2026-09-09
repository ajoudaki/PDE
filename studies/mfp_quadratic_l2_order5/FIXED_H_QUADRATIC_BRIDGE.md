# Fixed-horizon width-first bridge for the quadratic \(L=2\) network

> **Audit status.**  The polynomial bad-event removal in Section 5 is valid,
> but an independent audit did not accept Sections 2--4 as a self-contained
> reconstruction of the entire reused-action coupling: the response-bundle
> count and arbitrary-moment stopped estimate would need further expansion.
> This document is therefore not used as the sole width bridge.  The released
> no-go theorem instead uses `FIXED_H_QUADRATIC_WIDTH_LEMMA.md`, which maps the
> exact finite trained network to the already established polynomially-smooth
> finite-program theorem.

## Theorem

Let

\[
 \psi(x)=px+qx^2,\qquad p^2+3q^2=1,\qquad q\ne0.
\]

Fix an integer \(N\ge1\) and a real \(h\ne0\). For the one-input,
two-hidden-layer network and the simultaneous feature/output ascent update
stated in \`UNIFORM_NO_GO_THEOREM.md\`, every empirical feature Gram,
cotangent Gram, response cross-moment, and terminal output converges to the
chronological OMFP Gaussian DAG. The convergence holds in every fixed finite
\(L^r\). In particular,

\[
 \lim_{n\to\infty}E f_n^N=F_N(h).
\]

The result is pointwise in the separately fixed pair \((N,h)\). No bound
uniform in \(N\), and no \(h\to0\) interchange, is asserted.

## 1. Exact chronology

Put

\[
 H^s=\psi(u^s),\quad
 Y^s=W^0H^s/\sqrt n,\quad
 C^s=a^s\psi'(z^s),\quad
 D^s=(W^0)^\top C^s/\sqrt n.
\]

The trained connector satisfies exactly

\[
 W^s=W^0+\frac h{\sqrt n}\sum_{r<s}C^r(H^r)^\top,
\]

and consequently

\[
\begin{aligned}
 z^s&=Y^s+h\sum_{r<s}Q_{rs}^{(n)}C^r,\\
 b^s&=D^s+h\sum_{r<s}K_{rs}^{(n)}H^r,
\end{aligned}
\]

where

\[
 Q_{rs}^{(n)}=\frac1n(H^r)^\top H^s,\qquad
 K_{rs}^{(n)}=\frac1n(C^r)^\top C^s.
\]

Thus the reused matrix is exposed predictably in the finite order

\[
 Y^0,D^0,Y^1,D^1,\ldots,Y^{N-1},D^{N-1},Y^N.
\]

The adaptive row/column Gaussian-conditioning identity applies at each of
these \(2N+1\) actions. It yields the exact response terms

\[
\begin{aligned}
 z_s&=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})C_r,
 &\rho_{sr}&=E[\partial_{\chi_r}H_s],\\
 b_s&=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
                +h\sum_{r<s}K_{rs}H_r,
 &\sigma_{sr}&=E[\partial_{\xi_r}C_s].
\end{aligned}
\]

This is the same finite conditional-kernel calculation as for the
at-most-linear activation class; it uses no activation bound. The new work is
to prove strict rank, moment closure, and removal of spectral stopping for the
quadratic coordinate maps.

## 2. Strict full-history rank

We prove simultaneously that

\[
 Q^{[s]}=(E H_rH_v)_{r,v\le s}>0,\qquad
 K^{[s]}=(E C_rC_v)_{r,v\le s}>0.
\]

At \(s=0\), \(Q_{00}=E\psi(G)^2=1\), and

\[
 K_{00}=E[A^2\psi'(G)^2]>0
\]

because \(\psi'(x)=p+2qx\) is not identically zero.

Assume \(Q^{[s]},K^{[s]}>0\). Gaussian regression writes the newest
transpose source as

\[
 \chi_s=m_s(\chi_{<s})+\tau_sG_s,\qquad \tau_s>0,
\]

where \(G_s\) is fresh. Conditional on the old lower history,

\[
 u_{s+1}=x_s+h\tau_s\psi'(u_s)G_s.
\]

The event \(\{\psi'(u_s)\ne0\}\) has positive probability. At \(s=0\) this
follows from the full support of \(u_0\). At later times, on the preceding
positive-probability event the update contains a nondegenerate fresh
Gaussian, so \(u_{s+1}\) cannot be concentrated at the single zero of the
affine function \(\psi'\). On this event \(u_{s+1}\) is a nondegenerate
Gaussian conditionally on the past. A nonconstant quadratic of such a
Gaussian has positive conditional variance. Hence \(H_{s+1}\) has a
component orthogonal to the span of \(H_0,\ldots,H_s\), proving
\(Q^{[s+1]}>0\).

After this forward extension, regress

\[
 \xi_{s+1}=\widetilde m_{s+1}(\xi_{\le s})
             +\upsilon_{s+1}E_{s+1},\qquad\upsilon_{s+1}>0.
\]

Conditional on the old top history,

\[
 C_{s+1}=a_{s+1}\psi'(x+\upsilon_{s+1}E_{s+1}).
\]

The event \(\{a_{s+1}\ne0\}\) has positive probability. For \(s+1=0\) this
is \(a_0=A\). For later times, condition just before the newest forward
source in

\[
 a_{s+1}=a_s+h\psi(z_s).
\]

The variable \(z_s\) contains a nondegenerate fresh Gaussian and
\(\psi\) is nonconstant, so the right side is not almost surely zero. On
\(\{a_{s+1}\ne0\}\), the affine nonconstant function
\(\psi'(x+\upsilon E)\) has positive conditional variance. Thus
\(C_{s+1}\) has a component orthogonal to the old cotangent span and
\(K^{[s+1]}>0\).

The alternating induction proves strict rank for the entire finite history,
including the terminal forward Gram. Since the list is finite, the minimum
of all inverted population eigenvalues and nonterminal Schur complements is
a positive number \(4\gamma_{N,h}\).

## 3. Quadratic mixed-moment calculus

For a random coordinate array \(X\), define

\[
 {\cal N}_r(X)=
 \left(E\frac1n\sum_{i=1}^n|X_i|^r\right)^{1/r}.
\]

Normalized Hölder gives

\[
\begin{aligned}
 {\cal N}_r(XY)&\le{\cal N}_{2r}(X){\cal N}_{2r}(Y),\\
 \left\|\frac1nX^\top Y\right\|_{L^r}
 &\le{\cal N}_{2r}(X){\cal N}_{2r}(Y).
\end{aligned}
\]

For the quadratic activation,

\[
\begin{aligned}
 {\cal N}_r(\psi(X))
 &\le |p|{\cal N}_r(X)+|q|{\cal N}_{2r}(X)^2,\\
 {\cal N}_r(\psi(X)-\psi(Y))
 &\le |p|{\cal N}_r(X-Y)\\
 &\quad+|q|{\cal N}_{2r}(X-Y)
       \bigl({\cal N}_{2r}(X)+{\cal N}_{2r}(Y)\bigr),\\
 {\cal N}_r(\psi'(X))
 &\le |p|+2|q|{\cal N}_r(X),\\
 {\cal N}_r(\psi'(X)-\psi'(Y))
 &=2|q|{\cal N}_r(X-Y).
\end{aligned}
\]

The same inequalities hold for ideal iid arrays and for differences between
coupled raw/extended and ideal arrays.

Use the standard three-bundle ledger: one matrix action, its ensuing
coordinate assignments, and the empirical pair moments needed by the next
action. There are at most

\[
 \Lambda=3(2N+1)+1=6N+4
\]

bundles. A pair-moment bundle consumes moment order \(2r\). The adaptive
matrix-action estimate consumes \(8r\): inverse differences are evaluated
only above the spectral threshold, the Schur formula has at most two
unbounded empirical factors, and the removed finite-dimensional Gaussian
projection is \(O(n^{-1/2})\).

For a coordinate bundle, split its displayed formulas into elementary
binary product or quadratic-composition gates. Between two consecutive
matrix actions there are at most six such gates:

1. a learned Gram scalar times an old field;
2. addition to the raw matrix action;
3. one application of \(\psi\) or \(\psi'\);
4. multiplication by \(a\) or by a backpropagated field;
5. one Euler scalar-field product; and
6. the optional terminal readout product.

Each gate at most doubles the required moment order by the inequalities
above. Thus every coordinate bundle consumes at most \(2^6r=64r\).
This deliberately overcounts; it covers both value and error estimates.

For any desired terminal order \(r_*\ge2\), set

\[
 R_\Lambda=r_*,\qquad R_{j-1}=64R_j
 \quad(1\le j\le\Lambda).
\]

Then

\[
 R_0=64^\Lambda r_*<\infty.
\]

All initialization moments of order \(R_0\) are finite. Induction over the
finite ledger, using the four inequalities above, normalized
Cauchy--Schwarz for empirical moments, and the stopped matrix-action
estimate, proves

\[
 \sup_n{\cal M}_{j,r}(n)<\infty,\qquad
 {\cal E}_{j,r}(n)\le C_{j,r}n^{-1/2}
\]

for every bundle, where \({\cal M}\) is the largest extended/ideal moment
already constructed and \({\cal E}\) the largest coupled field, Gram, or
cross-moment error. No infinite source or moment hierarchy occurs.

## 4. Spectral stopping

Immediately before an inverse is needed, test that every empirical old Gram
has least eigenvalue at least \(2\gamma_{N,h}\); after forming a Schur
complement, test that it is at least \(2\gamma_{N,h}\). On this predictable
good event use the exact adaptive Gaussian conditional kernel. Off it, define
an extended process using the deterministic population coefficients and a
full fresh Gaussian residual. The raw process itself is never modified.

On the good event, the inverse identity and the fixed spectral bound give

\[
 \max_j|\alpha_{j,n}-\alpha_j|
 +|\tau_n^2-\tau^2|
 \le C_{N,h}{\cal Z}_n^2\delta_n,
\]

where \(\delta_n\) is the largest preceding Gram/cross-moment error and
\({\cal Z}_n\) one plus their absolute values. Since both variances are at
least \(2\gamma_{N,h}\),

\[
 |\tau_n-\tau|
 \le(2\sqrt{2\gamma_{N,h}})^{-1}|\tau_n^2-\tau^2|.
\]

The finite-rank projected part of a fresh Gaussian vector has mixed
normalized \(L^r\) norm \(O(n^{-1/2})\). These estimates give the
matrix-action implication used above:

\[
 \text{input errors and moments at order }8r
 \Longrightarrow
 \text{new action error at order }r=O(n^{-1/2}).
\]

Run the \(64^\Lambda\) tower with terminal order \(2m\). Weyl's inequality
and Markov's inequality give, at each possible first failed test,

\[
 P(\text{first failure here})\le C_m n^{-m}.
\]

A union bound over the finite chronology yields

\[
 P(\mathrm{stop})\le C_{N,h,m}n^{-m}
\]

for every prescribed \(m\ge1\).

## 5. Removing stopping for an unbounded quadratic

The bounded-activation proof used an \(n\)-independent Euclidean majorant.
For a quadratic activation a polynomial-in-\(n\) majorant suffices because
the stopping exponent \(m\) is arbitrary.

For normalized empirical Euclidean norms,

\[
\begin{aligned}
 \|\psi(x)\|_{n,2}
 &\le |p|\|x\|_{n,2}+|q|n^{1/2}\|x\|_{n,2}^2,\\
 \|xy\|_{n,2}
 &\le n^{1/2}\|x\|_{n,2}\|y\|_{n,2}.
\end{aligned}
\]

Let

\[
 {\cal R}_n=1+\|a^0\|_{n,2}+\|u^0\|_{n,2}
              +\|W^0/\sqrt n\|_{\rm op}.
\]

Suppose at time \(s\) the Euclidean norms of \(a^s,u^s\) and
\(W^s/\sqrt n\) are bounded by
\(n^{B_s}P_s({\cal R}_n)\), where \(P_s\) is a deterministic polynomial
with nonnegative coefficients. The exact forward/backward/update formulas
and the two inequalities above give

\[
 B_{s+1}=6B_s+\frac32,\qquad B_0=0.
\]

Indeed, successively, the exponent bounds for the bottom feature, middle
preactivation, top feature, top cotangent, lower backpropagated field, and
the three updated parameter blocks are

\[
\begin{array}{c|c}
\text{field}&\text{\(n\)-exponent}\\ \hline
H^s&\frac12+2B_s\\
z^s&\frac12+3B_s\\
\psi(z^s)&\frac32+6B_s\\
C^s&1+4B_s\\
b^s&1+5B_s\\
b^s\psi'(u^s)&\frac32+6B_s .
\end{array}
\]

The rank-one update obeys

\[
 \left\|\frac h n C^s(H^s)^\top\right\|_{\rm op}
 \le |h|\|C^s\|_{n,2}\|H^s\|_{n,2},
\]

and has the same final exponent \(\frac32+6B_s\). Therefore

\[
 B_s=\frac3{10}(6^s-1).
\]

After the terminal forward pass,

\[
 |f_n^N|
 \le n^{B_{\rm out}}P_{\rm out}({\cal R}_n),
\qquad
 B_{\rm out}=\frac32+7B_N<3\cdot6^N.
\]

Normalized Gaussian vector norms and
\(\|W^0/\sqrt n\|_{\rm op}\) have moments of every fixed order uniformly in
\(n\). Hence \(P_{\rm out}({\cal R}_n)\) also has every uniform finite
moment.

Fix any desired output exponent \(P\ge1\). Choose the stopping estimate with

\[
 m>2P(B_{\rm out}+1).
\]

Hölder gives

\[
\begin{aligned}
 \|f_n^N{\bf1}_{\{\rm stop\}}\|_{L^P}
 &\le n^{B_{\rm out}}
 \|P_{\rm out}({\cal R}_n)\|_{L^{2P}}
 P(\mathrm{stop})^{1/(2P)}\\
 &\le C n^{B_{\rm out}-m/(2P)}\longrightarrow0.
\end{aligned}
\]

On the complementary event, the raw and extended processes agree. The
extended process has every fixed terminal moment by the finite tower, and its
stopped-event piece also vanishes by Hölder. Therefore every raw terminal
field, Gram, response cross-moment, and output converges to its ideal OMFP
counterpart in each fixed finite \(L^P\). The extended regression
coefficients converge in every finite moment. No moment assertion is made for
an arbitrarily selected Moore--Penrose coefficient of the raw conditional
kernel on the failed spectral event; such a coefficient is not a network
observable and is not needed for the coupling.

Taking \(P>1\) gives uniform integrability. The ideal top coordinates are iid,
so their empirical terminal average converges in \(L^1\) to
\(F_N(h)\). This proves the theorem.

## Audit notes

1. The moment tower is finite but enormous:
   \(64^{6N+4}r_*\). Its size is irrelevant; only finiteness is used.
2. The spectral constant may deteriorate arbitrarily with \((N,h)\). The
   theorem is pointwise in those fixed values.
3. The raw bad-event bound may grow like \(n^{3\cdot6^N}\). Arbitrarily high
   stopping exponents absorb this because \(N\) is fixed before
   \(n\to\infty\).
4. The proof uses the actual alternating \(W/W^\top\) chronology and retains
   every response term. It does not replace the network by an independent
   Gaussian program.
5. Nothing in this bridge supplies a time-uniform small-step bound. It only
   validates the width-first passage used by the nonlocal no-go theorem.
