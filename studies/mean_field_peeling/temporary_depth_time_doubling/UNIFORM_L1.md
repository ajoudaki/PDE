# Uniform time-doubling remainder at one hidden layer

This note proves the actual-network, width-first estimate at hidden depth
one.  There is no reused matrix at this depth.  The only point not covered
by the bounded-vector-field argument in `UNIFORM_BSERIES.md` is that the
Gaussian initial coordinate is unbounded.  We handle it below by a
pathwise weighted envelope and then integrate that envelope.

## 1. The theorem and its explicit constants

Let $G\sim N(0,1)$, and assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

\[
 M=M_\phi:=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le q\le12}\|\phi^{(q)}\|_\infty\right\}<\infty .
 \tag{1.1}
\]

For independent $A,U\sim N(0,1)$, define

\[
 u_0=U,\qquad a_0=A,
\]

\[
 a_{s+1}=a_s+h\phi(u_s),\qquad
 u_{s+1}=u_s+ha_s\phi'(u_s),                         \tag{1.2}
\]

and

\[
 F_{N,1}(h)=\mathbb E[a_N\phi(u_N)].                 \tag{1.3}
\]

The following recursion defines the remainder constant.  Put

\[
 c_\phi=\frac1{16M}.                                 \tag{1.4}
\]

For $r\ge1$, set

\[
 K(r)=12Mr,\qquad P(r)=\exp(4c_\phi K(r))=e^{3r}.     \tag{1.5}
\]

In the next assignments $K=K(r)$, $P=P(r)$, and $c=c_\phi$.
Define, in the displayed order,

\[
 X_1=4PK,                                             \tag{1.6}
\]

\[
 X_2=P\{8KX_1+4cKX_1^2\},                           \tag{1.7}
\]

\[
 X_3=P\{12K(X_1^2+X_2)
          +4cK(X_1^3+3X_1X_2)\}.                    \tag{1.8}
\]

Put

\[
 G_0=K,\quad G_1=KX_1,\quad
 G_2=K(X_2+X_1^2),
\]

\[
 G_3=K(X_3+3X_1X_2+X_1^3),                           \tag{1.9}
\]

and, for $0\le q\le3$,

\[
 A_q=\sum_{v=0}^q {q\choose v}G_vG_{q-v}.            \tag{1.10}
\]

With $A_{-1}=A_{-2}=0$, define, for $1\le q\le3$,

\[
 Z_q=X_q+c^2A_q+2qcA_{q-1}+q(q-1)A_{q-2}.            \tag{1.11}
\]

Next set

\[
 T_1=P(Z_1+2K),                                      \tag{1.12}
\]

\[
 T_2=P\{Z_2+4KT_1+2cKT_1^2\},                       \tag{1.13}
\]

\[
 T_3=P\{Z_3+6K(T_1^2+T_2)
          +2cK(T_1^3+3T_1T_2)\}.                    \tag{1.14}
\]

Put

\[
 H_0=K,\quad H_1=KT_1,\quad
 H_2=K(T_2+T_1^2),
\]

\[
 H_3=K(T_3+3T_1T_2+T_1^3).                           \tag{1.15}
\]

Finally, set $W_0=PA_0$, and successively, for $1\le q\le3$,

\[
\begin{aligned}
 W_q=P\bigg\{A_q
 &+2c\sum_{v=1}^q{q\choose v}H_vW_{q-v}\\
 &+2q\sum_{v=0}^{q-1}{q-1\choose v}H_vW_{q-1-v}
 \bigg\},                                           \tag{1.16}
\end{aligned}
\]

and

\[
 \mathcal C_M(r)=\frac16\sum_{v=0}^3{3\choose v}H_vW_{3-v}.
 \tag{1.17}
\]

The activation-only constant used below is the explicit two-dimensional
Gaussian integral

\[
 B_{\phi,1}
 :=\mathbb E_{A,U}\mathcal C_M(1+|A|+|U|).           \tag{1.18}
\]

Every assignment in (1.6)--(1.17) uses only quantities already assigned,
and every sum has at most four terms.  Thus (1.18) is a completely
specified terminating formula.  Lemma 4.1 below proves that it is finite.

For the cubic coefficient, write, with all expectations over one standard
Gaussian $G$,

\[
\begin{aligned}
 u&=\mathbb E\phi'(G)^4,
 &m&=\mathbb E[\phi(G)\phi'(G)^2\phi''(G)],\\
 j&=\mathbb E[\phi'(G)^3\phi'''(G)],
 &e&=\mathbb E[\phi'(G)^2\phi''(G)^2],\\
 \ell&=\mathbb E[\phi(G)^2\phi'(G)^2],
\end{aligned}                                        \tag{1.19}
\]

and define

\[
 J_{\phi,1}=3(j+m)+4(u+\ell+2m+3e)
            =3j+11m+4u+4\ell+12e.                  \tag{1.20}
\]

**Theorem 1.1.**  For every integer $t\ge1$ and every

\[
 |\eta|\le \frac{c_\phi}{t},                         \tag{1.21}
\]

the width-first outputs satisfy

\[
\left|
 F_{t,1}(2\eta)-F_{2t,1}(\eta)
 +\frac{t(2t-1)}2J_{\phi,1}\eta^3
\right|
 \le B_{\phi,1}t^4|\eta|^5.                         \tag{1.22}
\]

Neither $B_{\phi,1}$ nor $c_\phi$ is defined from an output, a
trained trajectory, or an output continuity modulus.

## 2. The fixed-step width limit is exact

The finite-width one-hidden-layer network is

\[
 f_{n,1}^s=\frac1n\sum_{i=1}^na_i^s\phi(u_i^s),       \tag{2.1}
\]

where the pairs $(a_i^0,u_i^0)$ are iid $N(0,I_2)$.  The simultaneous
mean-field ascent update (\theta^{s+1}=\theta^s+hn\nabla f_{n,1}^s)
is exactly

\[
 a_i^{s+1}=a_i^s+h\phi(u_i^s),\qquad
 u_i^{s+1}=u_i^s+ha_i^s\phi'(u_i^s).                 \tag{2.2}
\]

Thus the pairs remain iid and each has recursion (1.2).  For every fixed
$N$ and fixed $h$, repeated use of

\[
 1+|a^+|+|u^+|
 \le(1+M|h|)(1+|a|+|u|)                              \tag{2.3}
\]

shows that the terminal summand is bounded by a deterministic polynomial
of $1+|A|+|U|$.  It is integrable.  Consequently, for every $n$,

\[
 \mathbb E f_{n,1}^N(h)=\mathbb E[a_N\phi(u_N)]
 =F_{N,1}(h).                                        \tag{2.4}
\]

In particular, the $n\to\infty$ limit at each fixed nonzero $h$
exists and equals (1.3); indeed no limiting approximation is present.
All remaining arguments are applied only after (2.4).

## 3. Exact defect factorization

On (\mathbb R^2), use the (\ell^1) norm and put

\[
 z=(a,u),\qquad
 f(z)=a\phi(u),\qquad
 g(z)=(\phi(u),a\phi'(u)),\qquad E_hz=z+hg(z).         \tag{3.1}
\]

Let $C_h=E_{2h}$ and $B_h=E_h^2$.  The fundamental theorem of
calculus gives the exact identity

\[
 B_hz=C_hz+h^2b_h(z),\qquad
 b_h(z)=\int_0^1Dg(z+shg(z))g(z)\,ds.                \tag{3.2}
\]

For $0\le q<t$, set

\[
 x_q=C_h^{t-1-q}z,\qquad v_q=f\circ B_h^q.           \tag{3.3}
\]

The hybrid sequence

\[
 H_q=f\bigl(B_h^q(C_h^{t-q}z)\bigr),\qquad0\le q\le t,
\]

satisfies $H_0=f(C_h^tz)$, $H_t=f(B_h^tz)$, and

\[
 H_q-H_{q+1}=v_q(C_hx_q)-v_q(B_hx_q).
\]

Using (3.2) once more,

\[
 f(C_h^tz)-f(B_h^tz)=h^2Q_t(h,z),                    \tag{3.4}
\]

where

\[
 Q_t(h,z)=-\sum_{q=0}^{t-1}\int_0^1
 Dv_q\bigl(C_hx_q+sh^2b_h(x_q)\bigr)[b_h(x_q)]\,ds.
 \tag{3.5}
\]

This is an identity at fixed, possibly noninfinitesimal $h$.

## 4. The weighted transported-defect estimate

We prove the estimate that explains the recursion (1.6)--(1.17).

### Lemma 4.1

Let $z_0=(a_0,u_0)$, $r=1+|a_0|+|u_0|$, and let
$|h|t\le c_\phi$.  Then $Q_t(\cdot,z_0)$ is $C^3$ on that interval
and

\[
 \sup_{|h|\le c_\phi/t}
 |\partial_h^3Q_t(h,z_0)|
 \le6\mathcal C_M(r)t^4.                             \tag{4.1}
\]

Moreover, $\mathcal C_M(1+|A|+|U|)$ is integrable.

### Proof

Write $R(z)=1+\|z\|_1$.  From (1.1),

\[
 R(E_{\alpha h}z)\le(1+\alpha M|h|)R(z),
 \qquad0\le\alpha\le2.                               \tag{4.2}
\]

Every pre-defect path in (3.5), including the point
$x+shg(x)$, has total Euler coefficient at most $4t$.  The point
$C_hx+sh^2b_h(x)$ is the convex combination

\[
 (1-s)C_hx+sB_hx,                                    \tag{4.3}
\]

and both endpoints have total Euler coefficient at most $4t$.
Transport after this interpolation uses at most $2t$ further Euler
coefficient.  Therefore (4.2), convexity of the norm, and (1.4) give at
every point occurring in (3.5)

\[
 R(z)\le e^{6M|h|t}r\le e^{3/8}r<2r.                \tag{4.4}
\]

The exponent \(6M|h|t\) is a deliberate overestimate: first bound the
two endpoints of the convex interpolation by \(e^{4M|h|t}r\), then
restart (4.2) from the interpolated point for the post-defect path and
multiply by \(e^{2M|h|t}\).  This does not assert that the interpolation
is an Euler step and does not double-count a required trajectory.  If
one uses the complementary lengths \(2(t-q)\) and \(2q\), the sharper
\(e^{2M|h|t}r\) follows, but it is not needed.

For $0\le q\le4$, direct differentiation of (3.1) gives

\[
 \|D^qg(z)\|\le6MR(z),                               \tag{4.5}
\]

and, for $1\le q\le4$,

\[
 \|D^qf(z)\|\le5MR(z).                              \tag{4.6}
\]

For example, the second coordinate of $D^qg$ is the sum of
$a\phi^{(q+1)}(u)$ applied to the $q$ (u)-directions and $q$
terms containing one $a$-direction and $\phi^{(q)}(u)$.  Its norm is
at most $M(|a|+q)$; the first coordinate adds at most $M$.
The derivatives of $f=a\phi(u)$ have the same form, with one lower
activation derivative.  Equations (4.4)--(4.6) are consequently bounded
by

\[
 K=12Mr.                                             \tag{4.7}
\]

Consider any of the variable-step Euler paths used before the defect:

\[
 y_{m+1}=y_m+\alpha_mh g(y_m),\qquad
 0\le\alpha_m\le2,\qquad \sum_m\alpha_m\le4t.      \tag{4.8}
\]

The product of its homogeneous tangent factors satisfies

\[
 \prod_m(1+\alpha_m|h|K)
 \le e^{K|h|\sum_m\alpha_m}
 \le P=e^{4c_\phi K}.                               \tag{4.9}
\]

Differentiate (4.8) with respect to $h$.  With all derivatives of
$g$ evaluated at $y_m$,

\[
 y_{m+1}'=(I+\alpha_mhDg)y_m'+\alpha_mg,             \tag{4.10}
\]

\[
 y_{m+1}''=(I+\alpha_mhDg)y_m''
 +2\alpha_mDg[y_m']
 +\alpha_mhD^2g[y_m',y_m'],                          \tag{4.11}
\]

\[
\begin{aligned}
 y_{m+1}'''=(I+\alpha_mhDg)y_m'''
 &+3\alpha_m\{D^2g[y_m',y_m']+Dg[y_m'']\}\\
 &+\alpha_mh\{D^3g[y_m'^3]
                 +3D^2g[y_m',y_m'']\}.             \tag{4.12}
\end{aligned}
\]

Iterating these recurrences, using (4.9),
$\sum\alpha_m/t\le4$, and $|h|t\le c_\phi$, yields successively

\[
 \sup_m\|y_m^{(q)}\|\le X_qt^q,\qquad1\le q\le3.  \tag{4.13}
\]

Indeed, (4.10) gives (4PKt=X_1t).  After division by (t^2), the
inhomogeneous part of (4.11) is bounded by
(8KX_1+4cKX_1^2), followed by the factor (P); this is (1.7).
Likewise (4.12), divided by (t^3), gives the expression inside braces
in (1.8), followed by (P).  Hence (4.13) proves, rather than assumes,
(1.6)--(1.8).

The curve (y(h)+shg(y(h))) in (3.2) is one such path with one
additional Euler coefficient (s\le1\), still below (4t).  The chain
rule therefore bounds the first three derivatives of (g(y(h))) and of
(Dg(y(h)+shg(y(h)))), after division by (t^q), by (G_q) in
(1.9).  Leibniz's rule in (3.2) then gives

\[
 \|\partial_h^qb_h(y(h))\|\le A_qt^q,
 \qquad0\le q\le3,                                  \tag{4.14}
\]

because (1.10) is precisely the convolution of the two chain-rule
envelopes.

For (w(h)=h^2b_h(y(h))),

\[
 w^{(q)}=h^2b_h^{(q)}+2qh b_h^{(q-1)}
          +q(q-1)b_h^{(q-2)}.                       \tag{4.15}
\]

Combining (4.13)--(4.15) proves that the derivatives through order three
of the interpolation point in (4.3) are bounded by (Z_qt^q), with
(Z_q) exactly as in (1.11).

Starting from that interpolation point, there are at most (2t) fine
Euler coefficients.  Applying (4.10)--(4.12) again, now with
(\sum\alpha_m/t\le2), proves

\[
 \|z^{(q)}\|\le T_qt^q,\qquad1\le q\le3,           \tag{4.16}
\]

where (1.12)--(1.14) are respectively the three inhomogeneous bounds,
followed by the harmless larger amplification (P).  The chain rule for
either (Dg(z(h))) or (Df(z(h))) gives the bounds (H_qt^q) in
(1.15).

It remains to transport the direction (b_h).  Across one fine Euler
step its tangent obeys

\[
 \omega^+=\omega+hDg(z)\omega.                       \tag{4.17}
\]

For (0\le q\le3), Leibniz's rule gives

\[
\begin{aligned}
 (\omega^+)^{(q)}=\omega^{(q)}
 &+h\sum_{v=0}^q{q\choose v}(Dg(z))^{(v)}
                  \omega^{(q-v)}\\
 &+q\sum_{v=0}^{q-1}{q-1\choose v}(Dg(z))^{(v)}
                  \omega^{(q-1-v)}.                 \tag{4.18}
\end{aligned}
\]

The (v=0) part of the first sum forms the homogeneous product (4.9).
The other terms are summed over at most (2t) coefficients.  Starting
from (4.14), induction on (q=0,1,2,3) gives

\[
 \|\omega^{(q)}\|\le W_qt^q,                        \tag{4.19}
\]

and the induction recurrence is exactly (1.16).

The integrand of a summand in (3.5), after its fine transport, is
$Df(z(h))[\omega(h)]$.  A final Leibniz rule, (1.15), and (4.19) show

\[
 \left|\partial_h^3\{Df(z(h))[\omega(h)]\}\right|
 \le t^3\sum_{v=0}^3{3\choose v}H_vW_{3-v}
 =6\mathcal C_M(r)t^3.                               \tag{4.20}
\]

For \(0\le q\le3\), the identical Leibniz calculation at derivative
order \(q\) gives the explicit bound

\[
 t^q\sum_{v=0}^q{q\choose v}H_vW_{q-v}.              \tag{4.20a}
\]

Thus, for fixed \(t\), the integrand and each of its first three
\(h\)-derivatives are dominated by

\[
 t^3\mathcal D_M(r),\qquad
 \mathcal D_M(r):=
 \sum_{q=0}^3\sum_{v=0}^q{q\choose v}H_vW_{q-v}.      \tag{4.20b}
\]

Like \(\mathcal C_M\), this is a polynomial with nonnegative
coefficients in the finite list \(K,P,X,G,A,Z,T,H,W\), and the argument
below proves that it is Gaussian-integrable.

Integration in $s$ has mass one, and (3.5) has exactly $t$ summands.
This proves (4.1).

Finally, all entries in (1.6)--(1.17) are polynomials with nonnegative
coefficients in (c,K,P).  Since (c\le1), (K(r)=12Mr), and
(P(r)=e^{3r}), the finite list of assignments implies, by induction
through that list, the existence of finite numerical integers
(C_0,p,q) such that

\[
 \mathcal C_M(r)\le C_0(1+12M)^p(1+r)^p e^{3qr}.     \tag{4.21}
\]

No limiting argument is used here: (p,q) are simply the largest degrees
and powers produced by the explicitly displayed finite arithmetic
expression (1.6)--(1.17).  A standard Gaussian has

\[
 \mathbb E[(1+|G|)^p e^{\lambda|G|}]<\infty
\quad(\lambda<\infty),                               \tag{4.22}
\]

because completing the square makes the integrand bounded by a polynomial
times (e^{-x^2/4}) outside a finite interval.  Applying (4.22) twice
proves that (1.18) is finite.  This completes the lemma. \(\square\)

## 5. Population parity, differentiation, and the remainder

Let

\[
 D_{t,1}(h)=F_{t,1}(2h)-F_{2t,1}(h).
\]

Taking expectation in (3.4) gives

\[
 D_{t,1}(h)=h^2\overline Q_t(h),\qquad
 \overline Q_t(h)=\mathbb E Q_t(h,(A,U)).             \tag{5.1}
\]

Lemma 4.1 supplies an integrable envelope for the first three derivatives
of the integrand.  The dominated-convergence theorem therefore proves
that (\overline Q_t\in C^3([-c_\phi/t,c_\phi/t])), permits all three
derivatives to pass through the Gaussian expectation, and gives

\[
 \sup_{|h|\le c_\phi/t}|\overline Q_t'''(h)|
 \le6B_{\phi,1}t^4.                                  \tag{5.2}
\]

Under (h\mapsto-h), (A\mapsto-A), the recursion (1.2) leaves every
(u_s) unchanged and negates every (a_s).  The Gaussian law is
invariant, so (F_{N,1}(-h)=-F_{N,1}(h)).  Hence (D_{t,1}) is odd.
Equation (5.1) and continuity show that (\overline Q_t) is odd as well;
in particular

\[
 \overline Q_t(0)=\overline Q_t''(0)=0.              \tag{5.3}
\]

Taylor's formula with integral remainder, applied to (\overline Q_t),
now gives

\[
 \overline Q_t(h)-\overline Q_t'(0)h
 =\frac12\int_0^h(h-s)^2\overline Q_t'''(s)\,ds.     \tag{5.4}
\]

Combining (5.1), (5.2), and (5.4),

\[
 |D_{t,1}(h)-\overline Q_t'(0)h^3|
 \le B_{\phi,1}t^4|h|^5.                            \tag{5.5}
\]

This proves the remainder without taking five derivatives of an unknown
output.

## 6. Direct Gaussian calculation of the cubic coefficient

For completeness, we reduce (\overline Q_t'(0)) independently to the
Gaussian activation integrals (1.19).  At a fixed initial point let

\[
 \mathbf h=Dg[g],\qquad
 \mathbf k=Dg[\mathbf h],\qquad
 \mathbf r=D^2g[g,g].                                \tag{6.1}
\]

Direct differentiation of
(z_{s+1}(h)=z_s(h)+hg(z_s(h))) at (h=0), followed by summation over
(s=0,\ldots,N-1), gives

\[
 z_N'(0)=Ng,\qquad z_N''(0)=N(N-1)\mathbf h,          \tag{6.2}
\]

\[
 z_N'''(0)=6{N\choose3}\mathbf k
 +\frac{N(N-1)(2N-1)}2\mathbf r.                    \tag{6.3}
\]

Here the third-derivative increment at time (s) is
(3s(s-1)\mathbf k+3s^2\mathbf r); the identities

\[
 \sum_{s<N}s(s-1)=2{N\choose3},\qquad
 \sum_{s<N}s^2=\frac{N(N-1)(2N-1)}6
\]

prove (6.3).

Since (g=\nabla f), define

\[
 \mathsf S=\mathbb E D^3f[g,g,g],\qquad
 \mathsf H=\mathbb E\|Dg[g]\|_2^2.                  \tag{6.4}
\]

The third-order chain rule applied to (f(z_N(h))), using symmetry of
the Hessian of (f), gives

\[
 F_{N,1}^{(3)}(0)
 =\frac{N(4N^2-3N+1)}2\mathsf S
  +2N(N-1)(2N-1)\mathsf H.                           \tag{6.5}
\]

Indeed,

\[
 Df[\mathbf k]=D^2f[g,\mathbf h]=\|\mathbf h\|_2^2,
 \qquad
 Df[\mathbf r]=D^3f[g,g,g],                          \tag{6.6}
\]

which accounts for every term in (6.5).  All differentiations under the
expectation are justified by the same Gaussian envelope as in Lemma 4.1
(with fixed (N), or directly by (6.2)--(6.3)).

Writing (p=\phi'(U)), (q=\phi''(U)), and
(r_3=\phi'''(U)), one has

\[
 g=(\phi(U),Ap),\qquad
 Dg[g]=(Ap^2,\phi(U)p+A^2pq).                         \tag{6.7}
\]

Because (A) and (U) are independent, with
(\mathbb EA^2=1) and (\mathbb EA^4=3),

\[
 \mathsf S=3(j+m),\qquad
 \mathsf H=u+\ell+2m+3e.                             \tag{6.8}
\]

Thus (J_{\phi,1}=\mathsf S+4\mathsf H), exactly (1.20).  Substitution
of (6.5) at (N=t) and (N=2t) yields

\[
 \overline Q_t'(0)
 =\frac{8F_{t,1}^{(3)}(0)-F_{2t,1}^{(3)}(0)}6
 =-\frac{t(2t-1)}2J_{\phi,1}.                        \tag{6.9}
\]

Equations (5.5) and (6.9) prove Theorem 1.1.

## 7. Checks and sharpness

If (\phi\equiv\pm1), then (F_{N,1}(h)=Nh), all five moments in
(1.19) vanish, and (1.22) holds with zero left-hand side.

For (\phi(x)=x), diagonalizing the update gives exactly

\[
 F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2.
\]

The fifth-order coefficient of the discrepancy is

\[
 32{2t\choose5}-{4t\choose5}
 =-\frac43t(t-1)(2t-1)(8t-9),
\]

which is of order (t^4).  Hence the exponent (t^4) in (1.22) cannot
be replaced uniformly by a smaller power of (t).
