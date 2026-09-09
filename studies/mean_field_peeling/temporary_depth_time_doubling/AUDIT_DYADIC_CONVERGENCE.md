# Dyadic feature-time convergence: exact implication and limitations

## Proposition

For integers \(m\ge1\), let \(F_m\) be real-valued and define

\[
 G_m(T)=F_m(T/m).
\]

Fix \(\rho>0\). Suppose that, for every dyadic \(m=2^j\), there are
\(\kappa_m\in\mathbb R\) and \(B_m\ge0\) such that

\[
 \left|F_{2m}(\eta)-F_m(2\eta)-\kappa_m\eta^3\right|
 \le B_m|\eta|^5,
 \qquad |\eta|\le \rho/m,                         \tag{1}
\]

\[
 |\kappa_m|\le K m^2,                              \tag{2}
\]

and

\[
 \sum_{j=0}^{\infty}\frac{B_{2^j}}{2^{5j}}<\infty. \tag{3}
\]

Then, for every \(R\le2\rho\), the sequence
\(\{G_{2^j}\}_{j\ge0}\) is uniformly Cauchy on \([-R,R]\). More
precisely,

\[
 \|G_{2m}-G_m\|_{\infty,[-R,R]}
 \le \frac{KR^3}{8m}+\frac{B_mR^5}{32m^5},         \tag{4}
\]

and its uniform limit \(G\) satisfies

\[
 \|G-G_{2^p}\|_{\infty,[-R,R]}
 \le \frac{KR^3}{4\,2^p}
 +\frac{R^5}{32}
   \sum_{j=p}^{\infty}\frac{B_{2^j}}{2^{5j}}.       \tag{5}
\]

If every \(G_{2^j}\) is continuous on \([-R,R]\), then \(G\) is
continuous there. If, in addition,

\[
 \sup_j\operatorname{Lip}(G_{2^j};[-R,R])<\infty, \tag{6}
\]

then \(G\) is Lipschitz, with Lipschitz constant bounded by the left side
of (6). A weaker sufficient condition is that one \(G_{2^{j_0}}\) is
Lipschitz and the Lipschitz constants of all subsequent dyadic increments
are summable.

## Proof and exact factors

To compare the two discretizations at the same feature time \(T\), set

\[
 \eta=\frac{T}{2m}.
\]

Then

\[
 F_{2m}(\eta)=G_{2m}(T),\qquad
 F_m(2\eta)=G_m(T).
\]

The admissible-step condition in (1) becomes

\[
 |T|/(2m)\le\rho/m,
\]

which is exactly \(|T|\le2\rho\). Substitution into (1) gives

\[
\begin{aligned}
 |G_{2m}(T)-G_m(T)|
 &\le |\kappa_m|\frac{|T|^3}{(2m)^3}
 +B_m\frac{|T|^5}{(2m)^5}\\
 &\le \frac{K|T|^3}{8m}
 +\frac{B_m|T|^5}{32m^5}.
\end{aligned}
\]

This proves (4). For \(q>p\), telescope the dyadic increments:

\[
 G_{2^q}-G_{2^p}
 =\sum_{j=p}^{q-1}(G_{2^{j+1}}-G_{2^j}).
\]

The cubic contribution is summable because

\[
 \sum_{j=p}^{\infty}2^{-j}=2^{1-p},
\]

and the fifth-order contribution is summable by (3). For each \(T\),
completeness of \(\mathbb R\) gives a pointwise limit; the same tail bound
then proves uniform convergence and (5). The continuity and Lipschitz
claims are the standard uniform-limit arguments.

## Sign under the convention used in the depth--time study

The main depth--time files define

\[
 D_m(\eta)=F_m(2\eta)-F_{2m}(\eta)
\]

and prove the cubic coefficient

\[
 \kappa_m^{D}
 =-\frac{m(2m-1)}2J_{\phi,L}.
\]

The increment used in (1) has the opposite sign:

\[
 F_{2m}(\eta)-F_m(2\eta)=-D_m(\eta),
\]

so its cubic coefficient is

\[
 \kappa_m
 =\frac{m(2m-1)}2J_{\phi,L}.                       \tag{7}
\]

At equal feature time, its exact cubic contribution is therefore

\[
 \kappa_m\left(\frac{T}{2m}\right)^3
 =J_{\phi,L}T^3\,\frac{2m-1}{16m^2}
 =J_{\phi,L}T^3
   \left(\frac1{8m}-\frac1{16m^2}\right).          \tag{8}
\]

Thus (2) holds with \(K=|J_{\phi,L}|\). Reversing the discrepancy
convention reverses (7)--(8) but does not change any norm bound.

## What the implication does not prove

### 1. The time interval

A single fixed \(\rho\) proves convergence only on compact subsets of
\([-2\rho,2\rho]\), not on every compact feature-time interval. To obtain
all compact intervals, one needs (1)--(3) for every desired radius, with
radius-dependent constants, or a state-level restart theorem.

### 2. Continuity and Lipschitzness

The size estimate (4) controls differences between resolutions, not
differences between two time arguments. Without continuity of the
approximants, the uniform limit need not be continuous. In this project
each fixed-horizon Gaussian DAG is locally \(C^5\), so continuity is
available on its certified interval and uniform convergence preserves it.

The discrepancy bound alone does not imply a uniform Lipschitz constant.
Continuous increments can have summable amplitudes and arbitrarily large
slopes. A condition such as (6), or summable Lipschitz constants for the
increments, is genuinely additional.

### 3. A restartable state evolution or IDE

Scalar convergence of \(F_m(T/m)\) at one initialization does not recover
the hidden population state, prove a semigroup law, or identify an
integral/differential equation. Distinct states can have the same scalar
output and different futures.

A sufficient state-level upgrade requires:

1. a complete state space \((\mathcal X,d)\) containing all population
   features, cotangents, learned operators, and reused-response data;
2. state approximants
   \[
   S_m(T,x)=E_{T/m}^{\,m}x
   \]
   satisfying a dyadic estimate analogous to (4), uniformly for \(x\) in
   a restart-invariant bounded set;
3. uniform time continuity and stability with respect to \(x\);
4. partition independence, or equivalently an approximate restart law
   whose defect tends to zero uniformly:
   \[
   d\!\left(S_m(T+S,x),
   S_m(S,S_m(T,x))\right)\longrightarrow0;
   \]
5. a state generator \(g\) with uniform one-step consistency and enough
   local Lipschitzness for uniqueness:
   \[
   \frac{E_hx-x}{h}\longrightarrow g(x).
   \]

Under these conditions, the state limits form a restartable local
semigroup and the Euler sums pass to

\[
 X(T)=x+\int_0^Tg(X(s))\,ds.
\]

The scalar limit is then \(G(T)=\mathcal F(X(T))\) for a continuous
readout \(\mathcal F\). The scalar assumptions (1)--(3) alone supply none
of items 1--5.

## Audit verdict

The dyadic scalar convergence implication is correct after:

- evaluating the discrepancy at \(\eta=T/(2m)\);
- using the factors \(2^{-3}=1/8\) and \(2^{-5}=1/32\);
- reversing the sign of the cubic coefficient relative to
  \(D_m=F_m(2\eta)-F_{2m}(\eta)\); and
- restricting a fixed-radius result to \(|T|\le2\rho\).

Continuity follows if the fixed-resolution functions are continuous.
Lipschitzness and a restartable IDE require the additional conditions
listed above.
