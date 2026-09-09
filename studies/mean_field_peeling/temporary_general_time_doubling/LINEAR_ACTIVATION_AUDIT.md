# Linear-activation fifth-order audit

This note proves the fifth-order obstruction for the admissible activation

\[
\phi(x)=x
\]

without assuming that the nonlinear width-first Gaussian DAG is intertwined
with a time-homogeneous population Koopman operator. The only width theorem
used is the pointwise fixed-nonzero-step identification of the actual network
with its finite-time Gaussian DAG.

## 1. Width-first polynomial lemma

Let \(F_{N,n}(h)\) be the annealed output of the width-\(n\),
two-hidden-layer network after \(N\) simultaneous Euler ascent steps of size
\(h\), and let

\[
F_N(h)=\lim_{n\to\infty}F_{N,n}(h)
\tag{1.1}
\]

at each fixed \(h\ne0\). For \(\phi(x)=x\), \(F_N\) is a polynomial and

\[
c_5(N):=[h^5]F_N(h)
\]

is a polynomial sequence in \(N\) of Newton degree at most five.

**Proof.** At finite width write the parameter state as \(X\), its ascent
vector field as \(V_n(X)\), and the output as \(g_n(X)\). One update is the
exact polynomial map

\[
E_{h,n}(X)=X+hV_n(X).
\]

All three parameter blocks start with \(h\)-degree zero. If their degrees
after \(s\) steps are at most \(d_s\), each update has degree at most
\(1+2d_s\). Thus \(d_s\le 2^s-1\), and

\[
F_{N,n}(h)=\mathbb E\,g_n(E_{h,n}^NX_0)
\]

has degree at most \(D_N:=3(2^N-1)\), independently of \(n\).

Choose \(D_N+1\) distinct nonzero real numbers
\(h_0,\ldots,h_{D_N}\). By (1.1), the value vector

\[
\bigl(F_{N,n}(h_j)\bigr)_{j=0}^{D_N}
\]

converges. Multiplication by the inverse Vandermonde matrix therefore shows
that every coefficient of the exact polynomial \(F_{N,n}\) converges. For
an arbitrary fixed nonzero \(h\), the coefficient limit has the same value
as (1.1), so \(F_N\) is precisely the resulting polynomial. In particular,

\[
[h^5]F_N=\lim_{n\to\infty}[h^5]F_{N,n}.
\tag{1.2}
\]

This conclusion used fixed-\(h\) width limits at finitely many nonzero
arguments; it did not exchange \(n\to\infty\) with \(h\to0\).

It remains to prove the time-degree assertion. At finite width define the
exact pullback \(P_{h,n}g=g\circ E_{h,n}\). Polynomial Taylor's identity is
finite on each polynomial and gives

\[
P_{h,n}=I+\sum_{r\ge1}h^rA_{r,n},
\qquad
A_{r,n}g=\frac1{r!}D^rg[V_n,\ldots,V_n].
\tag{1.3}
\]

In a term of total \(h\)-degree five in \(P_{h,n}^N\), at most five of the
\(N\) factors can be nonidentity factors. Choosing their time locations and
retaining their chronological order yields the exact algebraic identity

\[
[h^5]F_{N,n}
=\sum_{m=1}^5\binom Nm\theta_{m,n},
\tag{1.4}
\]

where

\[
\theta_{m,n}
=\sum_{\substack{r_1+\cdots+r_m=5\\r_j\ge1}}
\mathbb E\!\left[
(A_{r_m,n}\cdots A_{r_1,n}g_n)(X_0)
\right].
\]

No commutativity is used in (1.4). Equivalently,

\[
\theta_{m,n}
=\Delta_N^m\bigl([h^5]F_{N,n}\bigr)\big|_{N=0}.
\]

Equation (1.2) for \(N=0,\ldots,5\) lets us pass to the limit in these
finite differences and then in the finite sum (1.4). Hence

\[
c_5(N)=\sum_{m=1}^5\binom Nm\,\Delta_N^mc_5(0),
\tag{1.5}
\]

which proves the claim. Notice that (1.3)--(1.5) are finite-width algebra
used only after (1.2) was obtained from fixed-nonzero-\(h\) convergence. No
population Koopman operator, and no unproved population intertwining, has
been invoked. \(\square\)

## 2. Direct width-first covariance calculation

We now compute \(c_5(0),\ldots,c_5(5)\) directly from the identified
Gaussian DAG. Work in

\[
\mathcal R_5=\mathbb Q[h]/(h^6).
\]

For the identity activation, the top and bottom halves of the DAG are
isomorphic: their initial marks are standard Gaussian, their source Grams
coincide, and their response coefficients coincide. Induction in the
chronological DAG therefore reduces both halves to the following one-block
recursion.

At time (s), (x_s) depends only on (e_0,\ldots,e_{s-1}), so the
current-coordinate response is explicitly
(\sigma_{ss}=\partial_{e_s}x_s=0); the remaining top and lower responses
match under the stated isomorphism.

Let \(A,e_0,e_1,\ldots\) be formal centered Gaussian coordinates. Their
covariance pairing is defined recursively by

\[
\langle A,A\rangle=1,
\qquad
\langle A,e_s\rangle=0,
\qquad
\langle e_r,e_s\rangle=q_{rs}.
\tag{2.1}
\]

Put \(x_0=A\). Once \(x_0,\ldots,x_s\) have been constructed, set

\[
q_{rs}=\langle x_r,x_s\rangle,
\qquad
\gamma_{sr}=[e_r]x_s,
\tag{2.2}
\]

and define

\[
y_s=e_s+\sum_{r<s}(\gamma_{sr}+hq_{rs})x_r,
\qquad
x_{s+1}=x_s+hy_s.
\tag{2.3}
\]

Here \([e_r]x_s\) is the coefficient of \(e_r\) in the linear Gaussian
coordinate \(x_s\). Equations (2.1)--(2.3) are exactly the specialization

\[
\rho_{sr}=\partial_{e_r}x_s,
\qquad
z_s=e_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})x_r
\]

of the fixed-\(h\) response DAG. The width-first output is

\[
F_s(h)=\langle x_s,y_s\rangle.
\tag{2.4}
\]

The full identity-activation DAG and (2.1)--(2.4) are polynomial recursions,
and they agree for every fixed \(h\ne0\); hence their polynomial extensions
also agree at \(h=0\). Performing (2.1)--(2.4) in the finite ring
\(\mathcal R_5\) is therefore an exact, terminating width-first calculation.
The following ledger records every new state, action, and Gram row needed to
check it. All equalities in the ledger are in \(\mathcal R_5\).

\[
\begin{array}{c|l|l}
s&x_s&y_s\\ \hline
0&A&e_0\\
1&A+he_0&e_1+2hA\\
2&(1+2h^2)A+h(e_0+e_1)
 &e_2+(4h+6h^3)A+(2h^2+4h^4)e_0\\
3&(1+6h^2+6h^4)A+(h+2h^3+4h^5)e_0+h(e_1+e_2)
 &e_3+(6h+35h^3+77h^5)A
 +(4h^2+23h^4)e_0+(2h^2+14h^4)e_1\\
4&(1+12h^2+41h^4)A+(h+6h^3+27h^5)e_0
 +(h+2h^3+14h^5)e_1+h(e_2+e_3)
 &e_4+(8h+104h^3+679h^5)A
 +(6h^2+74h^4)e_0+(4h^2+52h^4)e_1
 +(2h^2+30h^4)e_2\\
5&(1+20h^2+145h^4)A+(h+12h^3+101h^5)e_0
 +(h+6h^3+66h^5)e_1+(h+2h^3+30h^5)e_2+h(e_3+e_4)
 &e_5+(10h+230h^3+3001h^5)A
 +(8h^2+174h^4)e_0+(6h^2+131h^4)e_1
 +(4h^2+93h^4)e_2+(2h^2+52h^4)e_3
\end{array}
\tag{2.5}
\]

The new Gram rows used in obtaining (2.5) are

\[
\begin{array}{c|llllll}
s&q_{0s}&q_{1s}&q_{2s}&q_{3s}&q_{4s}&q_{5s}\\ \hline
0&1\\
1&1&1+h^2\\
2&1+2h^2&1+4h^2&1+8h^2+5h^4\\
3&1+6h^2+6h^4&1+9h^2+10h^4&1+14h^2+29h^4
 &1+21h^2+81h^4\\
4&1+12h^2+41h^4&1+16h^2+57h^4&1+22h^2+103h^4
 &1+30h^2+201h^4&1+40h^2+390h^4\\
5&1+20h^2+145h^4&1+25h^2+185h^4&1+32h^2+275h^4
 &1+41h^2+441h^4&1+52h^2+726h^4&1+65h^2+1190h^4
\end{array}
\tag{2.6}
\]

Substitution in (2.4) gives

\[
\begin{array}{c|rrrrrr}
s&0&1&2&3&4&5\\ \hline
F_s(h)
&0&3h&6h+24h^3+20h^5
&9h+120h^3+525h^5
&12h+336h^3+3682h^5
&15h+720h^3+14824h^5
\end{array}
\pmod {h^6}.
\tag{2.7}
\]

This is a direct calculation in the width-first DAG; it does not insert
initialization jets into a symbolic population evolution.

## 3. Exact Newton formula and the obstruction

From (2.7), the fifth-order row and its forward-difference triangle begin

\[
\begin{array}{c|rrrrrr}
&0&1&2&3&4&5\\ \hline
c_5&0&0&20&525&3682&14824\\
\Delta c_5&0&20&505&3157&11142\\
\Delta^2c_5&20&485&2652&7985\\
\Delta^3c_5&465&2167&5333\\
\Delta^4c_5&1702&3166\\
\Delta^5c_5&1464
\end{array}
\]

and (1.5) therefore proves, for every integer \(N\ge0\),

\[
\boxed{
c_5(N)
=20\binom N2+465\binom N3
+1702\binom N4+1464\binom N5.
}
\tag{3.1}
\]

For

\[
D_t(h)=F_t(2h)-F_{2t}(h),
\]

equation (3.1) gives

\[
\begin{aligned}
[h^5]D_t
&=20\left(32\binom t2-\binom{2t}2\right)
+465\left(32\binom t3-\binom{2t}3\right)\\
&\quad+1702\left(32\binom t4-\binom{2t}4\right)
+1464\left(32\binom t5-\binom{2t}5\right)\\
&=-\frac{2452}{3}t^4+1896t^3
-\frac{4403}{3}t^2+369t.
\end{aligned}
\tag{3.2}
\]

For this activation,
\(d=e=\ell=1\), \(c=k=2\), and all terms in \(S_\phi\) vanish. The
surviving terms in \(H_\phi\) are
\(c^2e+c\ell+2ed^2+k^2\ell=4+2+2+4=12\). Thus

\[
J_\phi=S_\phi+4H_\phi=48,
\qquad
\kappa_{\phi,t}=-24t(2t-1).
\tag{3.3}
\]

The output polynomials are odd. Indeed, under simultaneous sign reversal
\(X\mapsto-X\), the trilinear output obeys \(g_n(-X)=-g_n(X)\), while its
gradient obeys \(V_n(-X)=V_n(X)\). Hence
\(E_{h,n}^N(-X)=-E_{-h,n}^N(X)\); invariance of the centered Gaussian
initialization under \(X\mapsto-X\) gives
\(F_{N,n}(-h)=-F_{N,n}(h)\), and the same identity passes to \(F_N\).

In particular,

\[
F_2(2h)-F_4(h)=-144h^3-3042h^5+\text{higher odd powers}.
\tag{3.4}
\]

Finally, suppose a shared activation-only constant \(C_\phi\) satisfied

\[
|D_t(h)-\kappa_{\phi,t}h^3|
\le C_\phi t^2|h|^5
\tag{3.5}
\]

for every \(t\), on any positive interval about zero (the interval may even
shrink with \(t\)). Divide (3.5) by \(|h|^5\) and take \(h\to0\) only after
the width-first polynomial \(D_t\) has been identified. Equations
(3.2)--(3.3) would imply

\[
\left|-\frac{2452}{3}t^4+1896t^3
-\frac{4403}{3}t^2+369t\right|
\le C_\phi t^2
\]

for all \(t\), which is impossible. Hence a shared fifth-order remainder
coefficient must have at least quartic time growth.

This does **not** rule out a total discrepancy bound of the form

\[
|D_t(h)|\le C_\phi t^2|h|^3
\]

on a total-time window \(|h|\le c_\phi/t\): a quartic remainder
\(C_\phi t^4|h|^5\) has precisely quadratic size relative to \(|h|^3\) on
that window.
