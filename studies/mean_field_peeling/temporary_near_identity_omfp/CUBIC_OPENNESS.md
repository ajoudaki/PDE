# Unconditional openness of the cubic OMFP invariant

Date: 25 August 2026.

This note proves only openness of the explicit cubic invariant.  It does not
infer openness of the horizon-uniform fifth-order remainder.

## 1. Activation family

Let \(R\geq1\), let

\[
 \varphi\in C^{12}(\mathbb R),\qquad
 \max_{0\leq r\leq12}\|\varphi^{(r)}\|_\infty\leq R,
\]

and put, for \(G\sim N(0,1)\),

\[
 s_\epsilon=\|G+\epsilon\varphi(G)\|_2,
 \qquad
 \psi_\epsilon(x)=\frac{x+\epsilon\varphi(x)}{s_\epsilon},
 \qquad
 \delta=|\epsilon|R.
 \tag{1.1}
\]

Throughout, \(0\leq\delta\leq1/4\).  The reverse triangle inequality gives

\[
 |s_\epsilon-1|\leq\delta,
 \qquad
 \frac34\leq s_\epsilon\leq\frac54,
 \qquad
 \left|\frac1{s_\epsilon}-1\right|\leq\frac43\delta.
 \tag{1.2}
\]

Write

\[
 g=\psi_\epsilon(G),\quad p=\psi_\epsilon'(G),\quad
 q=\psi_\epsilon''(G),\quad r_3=\psi_\epsilon'''(G),
 \qquad H=1+|G|.
\]

Then pointwise

\[
 |g|\leq\frac43H,\qquad
 |g-G|\leq\frac43\delta H,
 \tag{1.3}
\]

\[
 |p|\leq\frac53,\qquad
 |p-1|\leq\frac83\delta,
 \qquad |q|,|r_3|\leq\frac43\delta.
 \tag{1.4}
\]

## 2. A finite interval-arithmetic compiler

For a scalar quantity \(X_\epsilon\) with identity value \(X_0\), a pair
\((A_X,L_X)\) certifies

\[
 |X_\epsilon|\leq A_X,
 \qquad |X_\epsilon-X_0|\leq L_X\delta.
 \tag{2.1}
\]

The following rules preserve (2.1):

\[
 \mathcal P(cX)=(|c|A_X,|c|L_X),
 \tag{2.2}
\]

\[
 \mathcal P(X+Y)=(A_X+A_Y,L_X+L_Y),
 \tag{2.3}
\]

\[
 \mathcal P(XY)=(A_XA_Y,L_XA_Y+A_XL_Y).
 \tag{2.4}
\]

Indeed,

\[
 |X_\epsilon Y_\epsilon-X_0Y_0|
 \leq |X_\epsilon-X_0|\,|Y_\epsilon|
      +|X_0|\,|Y_\epsilon-Y_0|,
\]

and \(|X_0|\leq A_X\).  Thus (2.2)--(2.4) are rigorous, if deliberately
non-sharp, interval rules.

Let \(\mu_k=\mathbb E(1+|G|)^k\).  For the nine one-dimensional activation
moments

\[
\begin{array}{lll}
 d=\mathbb Ep^2,&u=\mathbb Ep^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pr_3],&s=\mathbb Eq^2,\\
 j=\mathbb E[p^3r_3],&e=\mathbb E[p^2q^2],
 &\ell=\mathbb E[g^2p^2],
\end{array}
\tag{2.5}
\]

use the following initial pairs:

\[
\begin{array}{c|c|c|c}
X&X_0&A_X&L_X\\ \hline
d&1&25/9&64/9\\
u&1&625/81&2176/81\\
v&0&(4/9)\mu_1&(16/9)\mu_1\\
m&0&(100/81)\mu_1&(400/81)\mu_1\\
r&0&5/9&20/9\\
s&0&1/9&4/9\\
j&0&125/81&500/81\\
e&0&25/81&100/81\\
\ell&1&(400/81)\mu_2&(700/81)\mu_2+64/9.
\end{array}
\tag{2.6}
\]

For example,

\[
 |d-1|\leq\|p-1\|_\infty(\|p\|_\infty+1)
 \leq\frac{64}{9}\delta,
\]

and

\[
 |\ell-1|
 \leq \mathbb E|g^2-G^2|p^2
      +\mathbb E G^2|p^2-1|
 \leq
 \left(\frac{700}{81}\mu_2+\frac{64}{9}\right)\delta.
\]

The other seven rows follow immediately from (1.3)--(1.4), using
\(\delta^2\leq\delta/4\).  Their absolute bounds are the same estimates
with \(\delta\leq1/4\).

The width-first OMFP cubic theorem proved in
`../temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md`, equations
(1.6), (1.9), and (6.1)--(6.9), identifies the actual network/DAG cubic
coefficient with the following nine-moment recursion.  Run that recursion,
replacing every scalar addition and multiplication by (2.2)--(2.4):

\[
 \Theta_0=1,qquad \Theta_a=1+d\Theta_{a-1},qquad
 b_a=d^{L-a},\qquad \pi_a=db_a,
 \tag{2.7}
\]

\[
 V_0=M_0=T_0=0,
\]

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2b_au,
 \tag{2.8}
\]

\[
 M_a=vV_{a-1}+\Theta_{a-1}^2b_am+(d+v)M_{a-1},
 \tag{2.9}
\]

\[
\begin{aligned}
 T_a={}&3\Theta_{a-1}V_{a-1}r
 +3\Theta_{a-1}^3b_aj\\
 &+3\Theta_{a-1}M_{a-1}(r+s)
 +d(T_{a-1}+3M_{a-1}),
\end{aligned}
\tag{2.10}
\]

for \(a=1,\ldots,L\), followed by

\[
 \beta_{L+1}=0,\qquad\gamma_{L+1}=1,
\]

\[
\begin{aligned}
 \beta_a={}&b_aV_{a-1}s+3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}
 +\gamma_{a+1}^2\ell\\
 &+2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}
\tag{2.11}
\]

\[
 \gamma_a=\pi_a+\Theta_{a-1}b_a(r+s)+\gamma_{a+1}(v+d),
 \tag{2.12}
\]

for \(a=L,\ldots,1\).  Finally set

\[
 \mathsf S=T_L+3M_L,
 \qquad
 \mathsf H=V_L+\beta_1+
 \sum_{a=2}^L(\beta_a+\pi_aV_{a-1}),
 \qquad
 J_{\psi_\epsilon,L}=\mathsf S+4\mathsf H.
 \tag{2.13}
\]

Powers in (2.7)--(2.13) mean repeated applications of (2.4).  Starting
with the nine rows (2.6), there are finitely many assignments: \(L\)
forward assignments, \(L\) reverse assignments, and a finite number of
arithmetic operations per assignment.  The compiler therefore terminates
for every fixed finite \(L\).  Denote its final Lipschitz component by
\(\mathcal L_L\).

## 3. Theorem and proof

### Theorem 3.1

For every finite \(L\geq1\), every activation in (1.1), and
\(|\epsilon|R\leq1/4\),

\[
 \boxed{
 |J_{\psi_\epsilon,L}-J_{\mathrm{id},L}|
 \leq \mathcal L_L|\epsilon|R.}
 \tag{3.1}
\]

Here \(\mathcal L_L<\infty\) is computed solely by the finite recursion
(2.2)--(2.13) from numerical Gaussian moments.  Moreover,

\[
 J_{\mathrm{id},L}
 =\frac{2L(L+1)^2(L+2)}3.
 \tag{3.2}
\]

Consequently, if

\[
 0<|\epsilon|<\epsilon_{\mathrm{cub}}(R,L)
 :=\min\left\{
 \frac1{4R},
 \frac{J_{\mathrm{id},L}}{2R\mathcal L_L}
 \right\},
 \tag{3.3}
\]

and \(\varphi''\not\equiv0\), then \(\psi_\epsilon\) is genuinely
nonlinear and

\[
 J_{\psi_\epsilon,L}\geq\frac12J_{\mathrm{id},L}>0.
 \tag{3.4}
\]

For \(L=2\), \(J_{\mathrm{id},2}=48\); for \(L=3\),
\(J_{\mathrm{id},3}=160\).

For completely numerical (coarse) choices, use
\(\mu_1\le2\) and \(\mu_2\le4\) in (2.6).  The monotone pair recursion
then gives

\[
 \mathcal L_2
 \le \frac{560797732}{6561}<85475,
 \qquad
 \mathcal L_3
 \le \frac{370650356035708}{43046721}<8610421.
 \tag{3.5}
\]

Thus the following simpler activation-only intervals are sufficient:

\[
 0<|\epsilon|<\frac{24}{85475R}\quad(L=2),
 \qquad
 0<|\epsilon|<\frac{80}{8610421R}\quad(L=3).
 \tag{3.6}
\]

#### Proof

Equations (1.2)--(1.4) prove every row of (2.6).  Rules
(2.2)--(2.4) preserve their advertised absolute and Lipschitz bounds.
Induction through the finite assignments (2.7)--(2.13) therefore gives
(3.1).  Substitution of the identity moment tuple

\[
 (d,u,v,m,r,s,j,e,\ell)=(1,1,0,0,0,0,0,0,1)
\]

into the same exact recursion gives, more explicitly,

\[
 \Theta_a=a+1,\qquad
 V_a=\sum_{i=1}^a i^2,\qquad M_a=T_a=0,
\]

\[
 \gamma_a=L-a+2,\qquad
 \beta_a=\sum_{i=1}^{L-a+1}i^2.
\]

Consequently

\[
 \mathsf H
 =2\sum_{a=1}^L\sum_{i=1}^a i^2
 =\frac{L(L+1)^2(L+2)}6,
 \qquad \mathsf S=0,
\]

which proves (3.2).  The cited width-first cubic theorem proves both the
intertwining with the actual OMFP DAG and, for the convention used below,
the factor and sign of its step-doubling coefficient.  Inequalities
(3.3)--(3.4) follow from (3.1).  Finally,

\[
 \psi_\epsilon''=\frac{\epsilon\varphi''}{s_\epsilon},
\]

so \(\varphi''\not\equiv0\) and \(\epsilon\ne0\) make the normalized
activation genuinely nonlinear.  For the numerical corollary,
\(\mu_1=1+\sqrt{2/\pi}<2\) and
\(\mu_2=2+2\sqrt{2/\pi}<4\).  All entries and operations in the
absolute/Lipschitz components of (2.2)--(2.13) are nonnegative and monotone.
Exact rational evaluation with \((\mu_1,\mu_2)=(2,4)\) gives (3.5), and
(3.6) follows from (3.3). \(\square\)

## 4. What this theorem does not prove

The exact step-doubling cubic coefficient is

\[
 \kappa_{\epsilon,L,t}
 =\frac{t(2t-1)}2J_{\psi_\epsilon,L}
\]

for the convention
\(F_{2t,L}(h)-F_{t,L}(2h)\).  Theorem 3.1 proves a genuine nonlinear
open interval for this coefficient at \(L=2\) and \(L=3\).

It does not bound the fifth-order remainder uniformly in \(t\).  Such a
conclusion would require continuity in the intrinsic horizon-weighted OMFP
response norm.  Ordinary fixed-\(t\) continuity cannot supply that missing
quantifier.
