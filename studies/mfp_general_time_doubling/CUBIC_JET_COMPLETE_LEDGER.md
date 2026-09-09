# Complete arbitrary-time cubic-jet ledger

This supplement proves the arbitrary-time identity used in Section 7 of
`PROOF.md`.  Every derivative below is taken in the already identified
width-first Gaussian operator DAG.  No finite-width Taylor coefficient is
used.

## 1. Notation and finite sums

Let (A,G) be independent standard Gaussians and put

\[
g=\phi(G),\qquad p=\phi'(G),\qquad q=\phi''(G),
\qquad r_3=\phi'''(G).
\]

The RMS normalization is \(\mathbb E g^2=1\).  We use

\[
\begin{aligned}
d&=\mathbb Ep^2,&e&=\mathbb Ep^4,
&m&=\mathbb E(gqp^2),&j&=\mathbb E(r_3p^3),\\
s&=\mathbb E(q^2p^2),&\ell&=\mathbb E(g^2p^2),
&b&=\mathbb E(gq),&r&=\mathbb E(pr_3),
&v&=\mathbb E q^2,
\end{aligned}
\]

and

\[
c=1+d,\qquad \beta=b+cr,\qquad \delta=d+cv,
\qquad k=d+\beta+\delta.
\tag{1.1}
\]

For an integer \(N\ge1\), define

\[
C_2=\frac{N(N-1)}2,\qquad
T_2=\frac{N(N-1)(2N-1)}6,\qquad
C_3=\frac{N(N-1)(N-2)}6.
\tag{1.2}
\]

The sums used below are

\[
\sum_{a=0}^{N-1}a=C_2,
\qquad
\sum_{a=0}^{N-1}a^2=T_2,
\qquad
\sum_{a=0}^{N-1}\frac{a(a-1)}2=C_3.
\tag{1.3}
\]

For completeness, each identity follows by induction on \(N\): its
right-hand side is zero at \(N=1\), and replacing \(N\) by \(N+1\)
changes the three right-hand sides by, respectively,
\(N\), \(N^2\), and \(N(N-1)/2\), which are exactly the newly added
summands.  We shall also use the consequences

\[
\sum_{a<N}a(a-1)=2C_3,
\quad
\sum_{a<N}\frac{a(a-1)}2=C_3,
\quad
3T_2-C_2=N(N-1)^2.
\tag{1.4}
\]

## 2. The lower first and second jets

For the lower recursion, write a dot for one \(h\)-derivative evaluated at
\(h=0\).  Before coalescing the source coordinates, put

\[
S_a=\sum_{i<a}\chi_i.
\]

At \(h=0\), all lower preactivations equal \(G\), all lower features equal
\(g\), and the source covariance coalesces
\((\chi_0,\ldots,\chi_{N-1})\) to \((X,\ldots,X)\), where
\(X\sim N(0,d)\) is independent of \(G\).

The response coefficients needed in the lower drift satisfy

\[
\dot\sigma_{ai}=\delta\quad(i<a),
\qquad
\dot\sigma_{aa}=a\beta.
\tag{2.1}
\]

Here is the calculation.  At fixed top source coordinates
\(x_0,\ldots,x_a\),

\[
\dot C_a
=\left(\sum_{i<a}\phi(x_i)\right)\phi'(x_a)
+cA^2\left(\sum_{i<a}\phi'(x_i)\right)\phi''(x_a).
\]

For \(i<a\), differentiating in \(x_i\), coalescing all \(x\)'s to
\(G\), and taking expectation gives \(d+cv=\delta\).  Differentiating
in \(x_a\) gives \(a(b+cr)=a\beta\).  Since the top covariance is even
in \(h\), its first derivative is zero, so there is no Price term in
(2.1).  The parity involution of the DAG makes \(\sigma\) odd and the
lower covariance \(K\) even; hence

\[
\sigma_{ai}(0)=\ddot\sigma_{ai}(0)=0,
\qquad K_{ij}(0)=d,qquad \dot K_{ij}(0)=0.
\tag{2.2}
\]

The lower update is

\[
u_{a+1}=u_a+h b_a\phi'(u_a),
\quad
b_a=\chi_a+\sum_{i\le a}\sigma_{ai}H_i
+h\sum_{i<a}K_{ia}H_i,
\quad H_i=\phi(u_i).
\tag{2.3}
\]

Using (2.1)--(2.3) at coalescence gives

\[
\dot b_a
=a\delta g+a\beta g+adg=akg.
\tag{2.4}
\]

Differentiating the update once and then twice gives

\[
\dot u_{a+1}=\dot u_a+\chi_ap,
\tag{2.5}
\]

\[
\ddot u_{a+1}
=\ddot u_a+2\{\dot b_ap+\chi_aq\dot u_a\}.
\tag{2.6}
\]

Starting from \(u_0=G\), (2.5) yields

\[
\dot u_a=pS_a.
\tag{2.7}
\]

Summing (2.6), first before and then after coalescence, yields

\[
\ddot u_a
=a(a-1)kgp+2pq\sum_{i<a}\chi_iS_i,
\tag{2.8}
\]

\[
\dot u_a=aXp,
\qquad
\ddot u_a=a(a-1)(kgp+X^2pq).
\tag{2.9}
\]

Indeed, the drift part in (2.6) sums to
\(2kgp\sum_{i<a}i=a(a-1)kgp\), and the remaining terms give the
second term in (2.8).  Consequently

\[
\dot H_a=aXp^2,
\qquad
\ddot H_a=a(2a-1)X^2p^2q+a(a-1)kgp^2.
\tag{2.10}
\]

For \(Q_{ab}=\mathbb E(H_aH_b)\), the possible second-order covariance
correction is

\[
\frac12K''(0):\mathbb E D_\chi^2(H_aH_b)|_{h=0}.
\]

The zeroth integrand is \(g^2\), independent of every \(\chi_i\), so this
term is zero.  Substituting (2.10) into
\(\ddot H_ag+2\dot H_a\dot H_b+g\ddot H_b\) therefore proves

\[
\boxed{
Q_{ab}''(0)
=dm\{a(2a-1)+b(2b-1)\}
+k\ell\{a(a-1)+b(b-1)\}
+2abde.}
\tag{2.11}
\]

## 3. Complete lower-response calculation

Let

\[
D_N=\sum_{i=0}^{N-1}\partial_{\chi_i},
\qquad
R_N(h)=\sum_{i<N}\rho_{Ni}(h)
=\mathbb E_{K(h)}[D_NH_N(h,\chi)].
\tag{3.1}
\]

When \(D_N\) acts on a time-\(a\) node, only \(\chi_0,\ldots,\chi_{a-1}\)
occur.  From (2.7)--(2.9), at coalescence,

\[
D_N\dot u_a=ap,
\qquad
D_N\ddot u_a=2a(a-1)Xpq.
\tag{3.2}
\]

To compute the third jet, we first retain the second derivative of the
drift.  Equations (2.1)--(2.2) give

\[
\ddot b_a
=2\sum_{i\le a}\dot\sigma_{ai}\dot H_i
+2d\sum_{i<a}\dot H_i.
\tag{3.3}
\]

Since \(\dot H_i=p^2S_i\), (1.3) and coalescence give

\[
\ddot b_a
=2Xp^2\left\{(\delta+d)\frac{a(a-1)}2+\beta a^2\right\},
\tag{3.4}
\]

\[
D_N\ddot b_a
=2p^2\left\{(\delta+d)\frac{a(a-1)}2+\beta a^2\right\}.
\tag{3.5}
\]

Also \(D_N\dot b_a=0\), because (2.4) contains no \(\chi\)-coordinate.
Three differentiations of (2.3) now give

\[
\dddot u_{a+1}-\dddot u_a
=3\left\{
\ddot b_ap+2\dot b_aq\dot u_a
+\chi_a\bigl(r_3\dot u_a^2+q\ddot u_a\bigr)
\right\}.
\tag{3.6}
\]

There are exactly four directional product-rule atoms inside the braces.
Using (2.4), (2.9), and (3.2)--(3.5), their \(D_N\)-derivatives at
coalescence are

\[
\begin{array}{c|c}
\text{atom}&D_N(\text{atom})\\ \hline
\ddot b_ap
&2p^3\{(\delta+d)a(a-1)/2+\beta a^2\}\\
2\dot b_aq\dot u_a
&2a^2kgpq\\
\chi_ar_3\dot u_a^2
&3a^2X^2p^2r_3\\
\chi_aq\ddot u_a
&a(a-1)kgpq+3a(a-1)X^2pq^2.
\end{array}
\tag{3.7}
\]

For example, the third row is
\(r_3\{\dot u_a^2+2\chi_a\dot u_aD_N\dot u_a\}\), which becomes
\(3a^2X^2p^2r_3\).  The fourth row is
\(q\{\ddot u_a+\chi_aD_N\ddot u_a\}\), which becomes the displayed
sum.  Thus no product-rule term is suppressed.

Summing (3.6)--(3.7) over \(0\le a<N\), and using (1.2)--(1.4), proves

\[
\begin{aligned}
D_N\dddot u_N={}&
6p^3\{(\delta+d)C_3+\beta T_2\}\\
&+3kgpq(3T_2-C_2)
+9X^2p^2r_3T_2+18X^2pq^2C_3.
\end{aligned}
\tag{3.8}
\]

Indeed, the coefficient of \(kgpq\) before simplification is
\(6T_2+6C_3\), and
\(2(T_2+C_3)=3T_2-C_2\) follows from
\(2C_3=T_2-C_2\).

At \(h=0\), \(D_Nu_N=0\).  Applying \(D_N\) to the third chain
derivative of \(H_N=\phi(u_N)\) therefore gives exactly

\[
D_N\dddot H_N
=3r_3\dot u_N^2D_N\dot u_N
+3q\{D_N\dot u_N\ddot u_N
+\dot u_ND_N\ddot u_N\}
+pD_N\dddot u_N.
\tag{3.9}
\]

The expectation of each atom in (3.9) is listed here:

\[
\begin{array}{c|c}
\text{source}&\text{expectation}\\ \hline
3r_3\dot u_N^2D_N\dot u_N&3N^3dj\\
3qD_N\dot u_N\ddot u_N
&3N^2(N-1)km+3N^2(N-1)ds\\
3q\dot u_ND_N\ddot u_N&6N^2(N-1)ds\\
pD_N\dddot u_N
&6e\{(\delta+d)C_3+\beta T_2\}\\
&\quad+3km(3T_2-C_2)+9djT_2+18dsC_3.
\end{array}
\tag{3.10}
\]

Combining the rows and using (1.2) gives

\[
\boxed{
\begin{aligned}
\mathbb E[D_N\dddot H_N]={}&
\frac32N(4N^2-3N+1)dj\\
&+6N(N-1)(2N-1)ds\\
&+3N(N-1)(2N-1)km\\
&+N(N-1)e\{(\delta+d)(N-2)+\beta(2N-1)\}.
\end{aligned}}
\tag{3.11}
\]

The four coefficient reductions are, explicitly,

\[
\begin{aligned}
3N^3+9T_2&=\tfrac32N(4N^2-3N+1),\\
9N^2(N-1)+18C_3&=6N(N-1)(2N-1),\\
3N^2(N-1)+3(3T_2-C_2)&=3N(N-1)(2N-1),\\
6C_3&=N(N-1)(N-2),\qquad
6T_2=N(N-1)(2N-1).
\end{aligned}
\tag{3.12}
\]

It remains to account for the changing, singular Gaussian source law.
For a covariance path with \(K'(0)=K'''(0)=0\), the third-order Price
formula is

\[
\left.\frac{d^3}{dh^3}\mathbb E_{K(h)}f(h,\chi)\right|_{0}
=\mathbb E\partial_h^3f(0,\chi)
+\frac32K''(0):\mathbb E D_\chi^2\partial_hf(0,\chi).
\tag{3.13}
\]

Apply (3.13) to \(f=D_NH_N\).  From (2.7),

\[
\partial_h(D_NH_N)|_{0}=D_N(p^2S_N)=Np^2,
\]

which is independent of all \(\chi_i\).  The Hessian in (3.13) is
therefore zero.  Consequently (3.11) is the full response derivative:

\[
\boxed{
\begin{aligned}
R_N'''(0)={}&
\frac32N(4N^2-3N+1)dj\\
&+6N(N-1)(2N-1)ds\\
&+3N(N-1)(2N-1)km\\
&+N(N-1)e\{(\delta+d)(N-2)+\beta(2N-1)\}.
\end{aligned}}
\tag{3.14}
\]

## 4. The feature and effective-response sums

Summing (2.11) with \(b=N\) and \(0\le a<N\) gives

\[
\boxed{
\begin{aligned}
\sum_{a<N}Q_{aN}''(0)={}&
\frac{N(16N^2-15N+5)}6dm\\
&+\frac{2N(N-1)(2N-1)}3k\ell
+N^2(N-1)de.
\end{aligned}}
\tag{4.1}
\]

To verify the coefficients directly, use

\[
\begin{aligned}
\sum_{a<N}(2a^2-a)+N^2(2N-1)
&=\frac{N(16N^2-15N+5)}6,\\
\sum_{a<N}a(a-1)+N^2(N-1)
&=\frac{2N(N-1)(2N-1)}3,\\
2N\sum_{a<N}a&=N^2(N-1).
\end{aligned}
\]

Each equality results by inserting (1.2)--(1.3) and collecting the
numerator; hence (4.1) contains every summand of (2.11).

Since \(L_{Na}=\rho_{Na}+hQ_{aN}\), ordinary differentiation gives

\[
L_N^{(3)}:=\sum_{a<N}L_{Na}'''(0)
=R_N'''(0)+3\sum_{a<N}Q_{aN}''(0).
\tag{4.2}
\]

We shall also need

\[
\boxed{
\begin{aligned}
\sum_{a<N}Q_{aa}''(0)+NQ_{NN}''(0)
={}&\frac{N(16N^2-15N+5)}3dm\\
&+\frac{4N(N-1)(2N-1)}3k\ell\\
&+\frac{N(8N^2-3N+1)}3de.
\end{aligned}}
\tag{4.3}
\]

Indeed, setting the two indices equal in (2.11) and summing gives twice
the first two sums used for (4.1), while the last coefficient is

\[
2\left(T_2+N^3\right)
=\frac{N(8N^2-3N+1)}3.
\]

## 5. Complete terminal-node jets

At \(h=0\), \(\rho_{Na}'(0)=d\): by (2.7),
\(\partial_{\chi_a}\dot H_N=p^2\), whose expectation is \(d\).
Since \(Q_{aN}(0)=1\),

\[
L_{Na}'(0)=c,qquad L_{Na}''(0)=0.
\tag{5.1}
\]

The second identity follows from the parity of \(L\).  For every
\(a\ge0\), the already established first and second top jets are

\[
\dot a_a=ag,qquad
\ddot a_a=a(a-1)cAp^2,
\tag{5.2}
\]

\[
\dot z_a=acAp,qquad
\ddot z_a=ca(a-1)(gp+cA^2pq).
\tag{5.3}
\]

They can also be verified directly from

\[
a_a=A+h\sum_{i<a}\phi(z_i),qquad
z_a=x_a+\sum_{i<a}L_{ai}C_i,qquad
C_i=a_i\phi'(z_i).
\tag{5.4}
\]

In detail, (5.1) gives \(\dot z_a=caAp\).  Then

\[
\dot C_a=agp+acA^2pq,
\tag{5.5}
\]

so \(\ddot z_a=2c\sum_{i<a}\dot C_i\), which is (5.3).
Similarly,

\[
\dot a_N=\sum_{a<N}g=Ng,
\]

\[
\ddot a_N=2\sum_{a<N}p\dot z_a
=2cAp^2C_2=N(N-1)cAp^2.
\]

One more derivative gives

\[
\dddot a_N
=3\sum_{a<N}\{q\dot z_a^2+p\ddot z_a\}.
\tag{5.6}
\]

The \(gp^2\) coefficient in (5.6) is
\(6cC_3=cN(N-1)(N-2)\).  Its \(A^2p^2q\) coefficient is

\[
c^2(3T_2+6C_3)
=\frac12c^2N(N-1)(4N-5).
\]

Thus

\[
\boxed{
\dddot a_N
=cN(N-1)(N-2)gp^2
+\frac12c^2N(N-1)(4N-5)A^2p^2q.}
\tag{5.7}
\]

For \(z_N'''\), first differentiate \(C_a=a_a\phi'(z_a)\) twice:

\[
\ddot C_a
=\ddot a_ap+2\dot a_aq\dot z_a
+A\{r_3\dot z_a^2+q\ddot z_a\}.
\]

Substitution of (5.2)--(5.3) gives the unsummed five-atom identity

\[
\begin{aligned}
\ddot C_a={}&
ca(a-1)Ap^3
+c(3a^2-a)Agpq\\
&+c^2a^2A^3p^2r_3
+c^2a(a-1)A^3pq^2.
\end{aligned}
\tag{5.8}
\]

(The two \(gpq\) atoms, with coefficients \(2a^2\) and \(a(a-1)\),
have merely been added.)  From (5.1) and (5.4),

\[
\dddot z_N
=\sum_{a<N}\{L_{Na}'''(0)Ap+3c\ddot C_a\}.
\tag{5.9}
\]

Using (1.2)--(1.4) in (5.8)--(5.9) gives

\[
\boxed{
\begin{aligned}
\dddot z_N={}&ApL_N^{(3)}
+c^2N(N-1)(N-2)Ap^3\\
&+3c^2N(N-1)^2Agpq\\
&+\frac12c^3N(N-1)(2N-1)A^3p^2r_3\\
&+c^3N(N-1)(N-2)A^3pq^2.
\end{aligned}}
\tag{5.10}
\]

For example, the second line uses
\(3\sum_{a<N}(3a^2-a)=3(3T_2-C_2)=3N(N-1)^2\).

## 6. Every fixed-coordinate terminal atom

At fixed top source coordinates, the third derivative of the terminal
integrand is

\[
\begin{aligned}
\partial_h^3\{a_N\phi(z_N)\}={}&
\dddot a_Ng
+3\ddot a_Np\dot z_N\\
&+3\dot a_N\{q\dot z_N^2+p\ddot z_N\}\\
&+A\{r_3\dot z_N^3+3q\dot z_N\ddot z_N
+p\dddot z_N\}.
\end{aligned}
\tag{6.1}
\]

After coalescence, (5.2)--(5.3), (5.7), and (5.10) give the following
complete expectation ledger.  We use
\(\mathbb EA^2=1\) and \(\mathbb EA^4=3\).

\[
\begin{array}{c|l}
\text{atom in (6.1)}&\text{expectation}\\ \hline
\dddot a_Ng
&cN(N-1)(N-2)\ell
+\tfrac12c^2N(N-1)(4N-5)m\\
3\ddot a_Np\dot z_N
&3c^2N^2(N-1)e\\
3\dot a_Nq\dot z_N^2
&3c^2N^3m\\
3\dot a_Np\ddot z_N
&3cN^2(N-1)\ell+3c^2N^2(N-1)m\\
Ar_3\dot z_N^3
&3c^3N^3j\\
3Aq\dot z_N\ddot z_N
&3c^2N^2(N-1)m+9c^3N^2(N-1)s\\
Ap\dddot z_N
&dL_N^{(3)}+c^2N(N-1)(N-2)e\\
&\quad+3c^2N(N-1)^2m\\
&\quad+\tfrac32c^3N(N-1)(2N-1)j\\
&\quad+3c^3N(N-1)(N-2)s.
\end{array}
\tag{6.2}
\]

Adding the \(\ell,e,m,j,s\) columns separately gives

\[
\boxed{
\begin{aligned}
E_{3,N}:=\mathbb E\partial_h^3\{a_N\phi(z_N)\}|_{0}
={}&2cN(N-1)(2N-1)\ell\\
&+2c^2N(N-1)(2N-1)e\\
&+\frac12c^2N(28N^2-33N+11)m\\
&+\frac32c^3N(4N^2-3N+1)j\\
&+6c^3N(N-1)(2N-1)s+dL_N^{(3)}.
\end{aligned}}
\tag{6.3}
\]

For explicit verification of the only long coefficient, the coefficient
of \(c^2Nm\) in (6.2) is

\[
\frac12(N-1)(4N-5)+3N^2+6N(N-1)+3(N-1)^2
=\frac12(28N^2-33N+11).
\]

The other four reductions are

\[
\begin{aligned}
N(N-1)(N-2)+3N^2(N-1)&=2N(N-1)(2N-1),\\
3N^2(N-1)+N(N-1)(N-2)&=2N(N-1)(2N-1),\\
3N^3+\tfrac32N(N-1)(2N-1)&=\tfrac32N(4N^2-3N+1),\\
9N^2(N-1)+3N(N-1)(N-2)&=6N(N-1)(2N-1).
\end{aligned}
\tag{6.4}
\]

Thus (6.3) is obtained by displaying and summing every product/chain-rule
atom, not by symbolic interpolation.

## 7. The complete Price correction

The first fixed-coordinate derivative of the terminal integrand, before
coalescence, is

\[
\psi_1
=\left(\sum_{a<N}\phi(x_a)\right)\phi(x_N)
+cA^2\left(\sum_{a<N}\phi'(x_a)\right)\phi'(x_N).
\tag{7.1}
\]

For a historical index \(a<N\), direct differentiation gives

\[
\begin{aligned}
\mathbb E\partial_{aa}\psi_1&=b+cr=\beta,\\
\mathbb E\partial_{NN}\psi_1&=N(b+cr)=N\beta,\\
\mathbb E\partial_{aN}\psi_1&=d+cv=\delta.
\end{aligned}
\tag{7.2}
\]

For distinct historical indices \(a\ne b<N\),
\(\partial_{ab}\psi_1=0\), because each part of (7.1) is a sum in the
historical coordinates.  Since \(Q'(0)=Q'''(0)=0\), (3.13), now with
the top covariance \(Q\), gives exactly

\[
\boxed{
P_N
=\frac32\beta\left\{\sum_{a<N}Q_{aa}''(0)+NQ_{NN}''(0)\right\}
+3\delta\sum_{a<N}Q_{aN}''(0).}
\tag{7.3}
\]

The factor \(3\) in the second term is
\((3/2)\times2\): both ordered covariance entries \((a,N)\) and
\((N,a)\) occur in the contraction.  Equations (7.1)--(7.3) exhaust all
Hessian entries, so there is no unlisted covariance contribution.  Hence

\[
F_N'''(0)=E_{3,N}+P_N.
\tag{7.4}
\]

## 8. Final algebra without an omitted cancellation

Define

\[
\mathcal A_N=\frac{N(4N^2-3N+1)}2,
\qquad
\mathcal B_N=2N(N-1)(2N-1),
\tag{8.1}
\]

and the three auxiliary integer polynomials

\[
U_N=\frac{N(16N^2-15N+5)}6,
\quad
V_N=\frac{N(8N^2-3N+1)}3,
\quad
W_N=N^2(N-1).
\tag{8.2}
\]

Expanding the right sides verifies

\[
U_N=\mathcal A_N+\frac{\mathcal B_N}{6},
\qquad
V_N=2\mathcal A_N-\frac{\mathcal B_N}{3},
\tag{8.3}
\]

\[
N(N-1)(N-2)+3W_N=\mathcal B_N.
\tag{8.4}
\]

In this notation, (3.14), (4.1), and (4.3) become

\[
\begin{aligned}
R_N'''={}&3\mathcal A_Ndj+3\mathcal B_Nds
+\frac32\mathcal B_Nkm\\
&+e\left\{N(N-1)(N-2)(\delta+d)
+\frac12\mathcal B_N\beta\right\},
\end{aligned}
\tag{8.5}
\]

\[
\sum_{a<N}Q_{aN}''
=U_Ndm+\frac{\mathcal B_N}{3}k\ell+W_Nde,
\tag{8.6}
\]

\[
\sum_{a<N}Q_{aa}''+NQ_{NN}''
=2U_Ndm+\frac{2\mathcal B_N}{3}k\ell+V_Nde.
\tag{8.7}
\]

First remove \(dL_N^{(3)}\) from (6.3).  Equations (6.3)--(6.4) give

\[
\begin{aligned}
E_{3,N}-dL_N^{(3)}={}&
\mathcal B_Nc\ell+\mathcal B_Nc^2e
+(3\mathcal A_N+2\mathcal B_N)c^2m\\
&+3\mathcal A_Nc^3j+3\mathcal B_Nc^3s.
\end{aligned}
\tag{8.8}
\]

It remains only to add \(dL_N^{(3)}+P_N\).  Substitute
\(L_N^{(3)}=R_N'''+3\sum Q_{aN}''\) and (8.5)--(8.7).  Grouping first
by \(m,\ell,e,j,s\) gives:

* the \(j\)-term is \(3\mathcal A_Nd^2j\);
* the \(s\)-term is \(3\mathcal B_Nd^2s\);
* the \(m\)-terms are
  \[
  \frac32\mathcal B_Ndkm
  +3U_Ndm(d+\beta+\delta)
  =(3\mathcal A_N+2\mathcal B_N)dkm;
  \]
  here (1.1) and (8.3) were used;
* the \(\ell\)-terms are
  \[
  \mathcal B_Nk\ell(d+\beta+\delta)
  =\mathcal B_Nk^2\ell;
  \]
* the \(e\)-terms are
  \[
  de\left\{
  \left(\frac{\mathcal B_N}{2}+\frac32V_N\right)\beta
  +\left(N(N-1)(N-2)+3W_N\right)(\delta+d)
  \right\}.
  \]

By (8.3)--(8.4), the last line equals

\[
3\mathcal A_Nde\beta
+\mathcal B_Nde(\delta+d)
=3\mathcal A_Nde\beta
+\mathcal B_Ncedv+2\mathcal B_Ned^2,
\tag{8.9}
\]

where the last equality uses \(\delta=d+cv\).  Therefore

\[
\begin{aligned}
dL_N^{(3)}+P_N={}&
3\mathcal A_Nde\beta+3\mathcal A_Ndkm
+3\mathcal A_Nd^2j\\
&+\mathcal B_Ncedv+2\mathcal B_Ned^2
+3\mathcal B_Nd^2s\\
&+\mathcal B_Nk^2\ell+2\mathcal B_Ndkm.
\end{aligned}
\tag{8.10}
\]

Combining (8.8) and (8.10), term for term, proves

\[
\boxed{
F_N'''(0)=\mathcal A_NS_\phi+\mathcal B_NH_\phi,}
\tag{8.11}
\]

where

\[
S_\phi=3c^2m+3c^3j+3de\beta+3dkm+3d^2j,
\]

\[
H_\phi=c^2e+c\ell+2c^2m+3c^3s+cedv
+2ed^2+3d^2s+k^2\ell+2dkm.
\]

This proves the universal formula for every finite integer \(N\ge1\).
Every recurrence atom, Gaussian covariance correction, finite sum, and
final coefficient grouping has been displayed.

Finally, the first terminal derivative is

\[
\partial_h\{a_N\phi(z_N)\}|_0=Ng^2+NcA^2p^2,
\]

and there is no first-order Price term because \(Q'(0)=0\).  Thus

\[
F_N'(0)=N(1+cd)=N(1+d+d^2).
\tag{8.12}
\]
