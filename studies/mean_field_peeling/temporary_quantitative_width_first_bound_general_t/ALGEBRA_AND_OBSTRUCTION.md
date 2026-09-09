# General step-doubling algebra and the uniform-in-time obstruction

This note concerns

$$
\Delta_t(h)=F_t(2h)-F_{2t}(h),\qquad t\in\mathbb N.
$$

It separates the algebra, which is unconditional for the already-defined
finite-time Gaussian operator DAG, from the additional uniform state-evolution
statement needed to turn it into an actual-network theorem simultaneously for
all (t).

## 1. Exact cubic coefficient

The nodewise width-first calculation gives, for every fixed terminal index
(N),

$$
F_N'(0)=N(1+d+d^2)
$$

and

$$
F_N'''(0)
=\frac{N(4N^2-3N+1)}2S_\phi
+2N(N-1)(2N-1)H_\phi.
$$

Consequently the linear terms of 
(Delta_t) cancel.  The coefficient multiplying (S_\phi) in
(8F_t'''(0)-F_{2t}'''(0)) is

$$
8\frac{t(4t^2-3t+1)}2
-\frac{2t(16t^2-6t+1)}2
=-3t(2t-1),
$$

and the coefficient multiplying (H_\phi) is

$$
16t(t-1)(2t-1)
-4t(2t-1)(4t-1)
=-12t(2t-1).
$$

Thus, writing

$$
K_\phi=S_\phi+4H_\phi,
$$

one has

$$
\boxed{
\kappa_t:=\frac{\Delta_t'''(0)}6
=-\frac{t(2t-1)}2K_\phi.
}
$$

For the reverse orientation (F_{2t}(h)-F_t(2h)), the sign is positive.
In particular,

$$
F_2(2h)-F_4(h)
=-3K_\phi h^3+O(h^5)
$$

at the level of the width-first operator DAG.

## 2. Universal composition formula

Let (E_h(x)=x+hV(x)), let

$$
P_hg=g\circ E_h,
$$

and put

$$
A_rg=\frac1{r!}D^rg[V,\ldots,V].
$$

At any state at which the indicated derivatives exist,

$$
P_h=I+\sum_{r=1}^5h^rA_r+o(h^5).
$$

For (1\le m\le r), define the elementary-differential sum

$$
\Theta_{r,m}
=\sum_{\substack{r_1+\cdots+r_m=r\\r_i\ge1}}
\mathcal L\!left(A_{r_m}\cdots A_{r_1}g\right),
$$

where (mathcal L) is the initial expectation functional.  Expanding the
(N) identical factors in (P_h^N), choosing the (m) nonidentity factors,
and retaining their chronological order proves

$$
\boxed{
\frac{F_N^{(r)}(0)}{r!}
=\sum_{m=1}^r\binom Nm\Theta_{r,m}.
}
$$

There is no commutativity assumption: the sum over ordered compositions in
(Theta_{r,m}) keeps the operator order.  The binomial coefficient occurs
because identities may be inserted in any (m) of the (N) positions.

At order five this gives

$$
[h^5]\Delta_t(h)
=\sum_{m=1}^5p_m(t)\Theta_{5,m},
\qquad
p_m(t)=32\binom tm-\binom{2t}m.
$$

Direct expansion gives

$$
\begin{aligned}
p_1(t)&=30t,\\
p_2(t)&=14t^2-15t,\\
p_3(t)&=2t(t-1)(2t-5),\\
p_4(t)&=\frac{t(t-1)(4t^2-32t+45)}6,\\
p_5(t)&=-\frac{t(t-1)(t-2)(4t-9)}3.
\end{aligned}
$$

The degree-five terms cancel, but the degree-four terms do not cancel in
general.  Therefore the natural shared-constant scale of the fifth-order
term is (t^4), not (t^2).

The use of this formula for the neural width-first limit requires an
intertwining theorem identifying the local differential operators of its
one-step mean-field evolution with the directly differentiated Gaussian DAG.
The cubic nodewise ledger proves the required identity at order three.  No
order-five intertwining theorem has yet been proved in the present study.

## 3. A same-network witness that the quartic degree is necessary

Take the admissible RMS-normalized activation

$$
\phi(x)=x.
$$

The Gaussian operator DAG becomes linear.  Its variables obey

$$
\begin{aligned}
a_s&=A+h\sum_{r<s}z_r,
&z_s&=\xi_s+\sum_{r<s}(\rho_{sr}+hQ_{rs})a_r,\\
u_{s+1}&=u_s+hb_s,
&b_s&=\chi_s+\sum_{r\le s}\sigma_{sr}u_r
+h\sum_{r<s}K_{rs}u_r,
\end{aligned}
$$

with

$$
Q_{rs}=\mathbb E[u_ru_s],\qquad
K_{rs}=\mathbb E[a_ra_s],
$$

and, because every variable is linear in its Gaussian source,

$$
\rho_{sr}=\partial_{\chi_r}u_s,
\qquad
\sigma_{sr}=\partial_{\xi_r}a_s.
$$

These displayed equations are a finite exact covariance recursion.  Repeated
substitution through order five gives

$$
\begin{array}{c|rrrrrr}
N&0&1&2&3&4&5\\ \hline
[h^5]F_N&0&0&20&525&3682&14824.
\end{array}
$$

The composition formula proves beforehand that this row is a polynomial in
(N) of degree at most five in the binomial basis.  Its five forward
differences at zero are

$$
0,\quad20,\quad465,\quad1702,\quad1464.
$$

Hence the finite recursion is equivalently summarized, for every (N), by

$$
\boxed{
[h^5]F_N
=20\binom N2+465\binom N3
+1702\binom N4+1464\binom N5.
}
$$

Substitution into the polynomials (p_m) yields

$$
\boxed{
[h^5]\Delta_t
=-\frac{2452}{3}t^4+1896t^3
-\frac{4403}{3}t^2+369t.
}
$$

Thus an (O_\phi(t^2|h|^5)) remainder is false even for the linear
activation.  Any general bound which captures the fifth-order remainder at a
fixed (t)-independent microscopic scale must allow at least quartic growth
in (t).

## 4. An abstract quantitative (t^4) lemma

The quartic upper bound itself follows from a short operator argument once a
uniform one-step mean-field operator has been constructed.

Let (mathcal B) be a Banach space, let
(P_h\in\mathcal L(\mathcal B)) be (C^5) for (|h|\le r), and assume

$$
P_0=I,\qquad \|P_h\|\le1,
\qquad \|P_h^{(j)}\|\le L_j\quad(1\le j\le5).
$$

Set (L_0=1),

$$
U_j=\max\left\{
2^jL_j,
\sum_{i=0}^j\binom jiL_iL_{j-i}
\right\},
$$

$$
\lambda=\max\left\{1,
\max_{1\le j\le5}(U_j/j!)^{1/j}
\right\},
$$

and, for (2\le j\le5),

$$
D_j=2^jL_j+
\sum_{i=0}^j\binom jiL_iL_{j-i}.
$$

For any (0<c\le r/2), define

$$
\begin{aligned}
C(P,c)={}&512D_2c^2\lambda^5
+1280D_2c\lambda^4
+640D_2\lambda^3\\
&+160D_3\lambda^2+20D_4\lambda+D_5.
\end{aligned}
$$

Then, for every (t\ge1) and (|h|\le c/t),

$$
\boxed{
\left\|\frac{d^5}{dh^5}
\{P_{2h}^{,t}-P_h^{,2t}\}\right\|
\le C(P,c)t^4.
}
$$

To prove this, put

$$
C_h=P_{2h},\qquad A_h=P_h^2,\qquad D_h=C_h-A_h.
$$

Then (D_0=D_0'=0), and Taylor's integral formula gives

$$
\|D_h\|\le\frac12D_2h^2,qquad
\|D_h'\|\le D_2|h|,qquad
\|D_h^{(j)}\|\le D_j\quad(2\le j\le5).
$$

Moreover,

$$
C_h^t-A_h^t
=\sum_{q=0}^{t-1}C_h^{,t-1-q}D_hA_h^q.
$$

If (X_1,\ldots,X_m) are factors, each equal to (A_h) or (C_h),
then the definition of (lambda) and the multinomial rule give

$$
\frac1{s!}
\left\|\partial_h^s(X_1\cdots X_m)\right\|
\le\binom{m+s-1}{s}\lambda^s.
$$

Indeed, the left side is bounded coefficientwise by the coefficient of
(x^s) in ((1-\lambda x)^{-m}).  Differentiate each telescoping summand
five times and assign (j) derivatives to (D_h).  There are
(inom5j) assignments.  Since (m=t-1) and
(inom{m+s-1}{s}\le(4t)^s/s!) for (0\le s\le5), their sum is bounded
by

$$
t\sum_{j=0}^5
\binom5j(4t)^{5-j}\lambda^{5-j}\|D_h^{(j)}\|.
$$

For (j=0) insert (rac12D_2c^2/t^2); for (j=1) insert
(D_2c/t); and for (j\ge2) insert (D_j).  Since (t^{6-j}\le t^4)
for (j\ge2), collecting the six numerical coefficients gives exactly
(C(P,c)t^4).

If (F_N(h)=\Lambda_0(P_h^Ng)), with
(|\Lambda_0\|\|g\|\le R_\phi), all (F_N) are odd, and the cubic
coefficient is the one in Section 1, Taylor's integral formula therefore
gives

$$
\boxed{
|\Delta_t(h)-\kappa_th^3|
\le \frac{R_\phi C(P,c)}{120},t^4|h|^5,
\qquad |h|\le c/t.
}
$$

Every constant in this abstract statement is shared across all (t).

## 5. What is and is not proved for the actual network

For every *fixed* (t), if the fixed-nonzero-step identification has been
proved through time (2t), the finite activation-envelope compiler extends
chronologically through those finitely many nodes.  Let
(overline{\mathcal J}_{N,5}) be its explicit output and let (r_N) be
its explicit fixed-step identification radius.  Then the already proved
singular Price lemma and Taylor's integral remainder give

$$
\boxed{
|\Delta_t(h)-\kappa_th^3|
\le B_t|h|^5,
}
$$

where

$$
B_t=\frac{32\overline{\mathcal J}_{t,5}
+\overline{\mathcal J}_{2t,5}}{120},
\qquad
|h|\le
h_t:=\min\left\{\frac12,\frac{r_t}{2},r_{2t}\right\}.
$$

This is a finite, terminating activation-only formula for each fixed (t),
but it is not a uniform-in-(t) theorem.

Two bridges are missing for the actual-network bound claimed uniformly over
all (t):

1. The present adaptive row/column conditioning ledger proves fixed-step
   identification only for finitely many displayed actions.  For arbitrary
   (t), one needs either population-rank bounds for all time Grams, with an
   explicit radius, or a complete singular/pseudoinverse conditioning
   theorem.  The three-time forward-difference rank lemma does not imply
   this.

2. The chronological envelope compiler terminates for each fixed (N), but
   its output is (N)-dependent.  It has not been reorganized as a single
   Koopman family on a fixed Banach ladder satisfying the uniform bounds
   (L_1,\ldots,L_5) in Section 4.  Consequently it does not by itself
   produce shared (c_\phi,C_\phi).

Until both bridges are proved, the uniform actual-network assertion

$$
|\Delta_t(h)-\kappa_th^3|
\le C_\phi t^4|h|^5,
\qquad |h|\le c_\phi/t,
$$

is a conditional operator theorem, not a completed width-first network
theorem.  The quadratic cubic coefficient is proved; a quadratic fifth-order
remainder is disproved by Section 3.
