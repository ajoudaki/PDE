# Universal Euler time-polynomial calculation through order five

## Proposition

Let \(X\) be a Banach space, let \(g:X\to X\), let
\(O:X\to\mathbb R\), and fix \(\theta _0\in X\).  Assume that the jets
appearing below exist (for example, \(g,O\in C^7\) in a neighbourhood of
\(\theta _0\)).  Put

\[
 E_h(x)=x+h g(x),\qquad F_N(h)=O(E_h^N\theta _0).
\]

For a scalar test function \(f\), define the elementary Euler pullback
operators

\[
 \mathcal T_k f(x)
 :=\frac1{k!}D^k f(x)[g(x),\ldots,g(x)],
 \qquad k\geq1,
\]

and, for \(1\le r\le m\), define the ordered elementary-differential sum

\[
 \mathcal W_{m,r}
 :=\sum_{\substack{k_1+\cdots+k_r=m\\k_i\geq1}}
       \mathcal T_{k_1}\cdots\mathcal T_{k_r}.
\]

Composition is read from right to left.  Every summand is an exact finite
aggregate of observable-rooted elementary differentials.  Indeed, repeatedly
applying the Fréchet product rule expands it into terms

\[
 D^qO(\theta _0)[G(\tau _1),\ldots,G(\tau _q)],
\]

where

\[
 G(\bullet)=g(\theta _0),\qquad
 G([\tau _1,\ldots,\tau _s])
 =D^s g(\theta _0)[G(\tau _1),\ldots,G(\tau _s)].
\]

Then the exact coefficient of \(h^m\), for \(1\le m\le5\), is

\[
 [h^m]F_N(h)
 =\sum_{r=1}^m {N\choose r}
   (\mathcal W_{m,r}O)(\theta _0).                 \tag{1}
\]

Consequently, for

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),
\]

one has

\[
 [h^m]\Delta_t(h)
 =\sum_{r=1}^m q_{m,r}(t)
   (\mathcal W_{m,r}O)(\theta _0),                 \tag{2}
\]

where

\[
 q_{m,r}(t)={2t\choose r}-2^m{t\choose r}.         \tag{3}
\]

In particular \([h]\Delta_t=0\), and for every \(m\ge2\), the polynomial
\([h^m]\Delta_t\) has degree at most \(m-1\) in \(t\).  Its homogeneous
part of degree \(m-1\) is

\[
 t^{m-1}\left[
 \frac{2^{m-2}}{(m-2)!}\mathcal T_1^m
 -\frac{2^{m-1}}{(m-1)!}\mathcal W_{m,m-1}
 \right]O(\theta _0).                              \tag{4}
\]

Thus the fifth-order coefficient is always a polynomial of degree at most
four.  No small-nonlinearity assumption is needed for this time-degree
statement.

## Proof of the pullback formula

Let \(P_h\) be the one-step pullback,

\[
 (P_hf)(x)=f(E_hx)=f(x+hg(x)).
\]

Taylor expansion at fixed \(x\) gives

\[
 P_h=I+A_h,
 \qquad
 A_h=\sum_{k=1}^5h^k\mathcal T_k+O(h^6).           \tag{5}
\]

There is only one operator \(A_h\) in (5), so the ordinary binomial identity
is valid even though its homogeneous pieces \(\mathcal T_k\) do not commute:

\[
 P_h^N=(I+A_h)^N=\sum_{r=0}^N{N\choose r}A_h^r.    \tag{6}
\]

The coefficient of \(h^m\) in \(A_h^r\) is obtained by choosing an ordered
composition \(k_1+\cdots+k_r=m\).  It is therefore \(\mathcal W_{m,r}\).
Since

\[
 F_N(h)=(P_h^NO)(\theta _0),
\]

(1) follows.  Replacing \(N\) by \(2t\), and then subtracting \(2^m\) times
the coefficient with \(N=t\), proves (2)--(3).

For completeness, the coefficients of \(F_N\) through order five are

\[
\begin{aligned}
[h]F_N&=N\mathcal T_1O,\\
[h^2]F_N&=N\mathcal T_2O+{N\choose2}\mathcal T_1^2O,\\
[h^3]F_N&=N\mathcal T_3O+{N\choose2}
 (\mathcal T_1\mathcal T_2+\mathcal T_2\mathcal T_1)O
 +{N\choose3}\mathcal T_1^3O,\\
[h^4]F_N&=N\mathcal T_4O+{N\choose2}
 (\mathcal T_1\mathcal T_3+\mathcal T_2^2+
  \mathcal T_3\mathcal T_1)O\\
&\quad+{N\choose3}
 (\mathcal T_1^2\mathcal T_2+
  \mathcal T_1\mathcal T_2\mathcal T_1+
  \mathcal T_2\mathcal T_1^2)O
 +{N\choose4}\mathcal T_1^4O,\\
[h^5]F_N&=N\mathcal T_5O+{N\choose2}\mathcal W_{5,2}O
 +{N\choose3}\mathcal W_{5,3}O
 +{N\choose4}\mathcal W_{5,4}O
 +{N\choose5}\mathcal T_1^5O.
\end{aligned}                                      \tag{7}
\]

All expressions in (7) are evaluated at \(\theta _0\).  The fifth-order
word sums are

\[
\begin{aligned}
\mathcal W_{5,2}&=
 \mathcal T_1\mathcal T_4+\mathcal T_2\mathcal T_3+
 \mathcal T_3\mathcal T_2+\mathcal T_4\mathcal T_1,\\
\mathcal W_{5,3}&=
 \mathcal T_1^2\mathcal T_3+
 \mathcal T_1\mathcal T_3\mathcal T_1+
 \mathcal T_3\mathcal T_1^2+
 \mathcal T_1\mathcal T_2^2+
 \mathcal T_2\mathcal T_1\mathcal T_2+
 \mathcal T_2^2\mathcal T_1,\\
\mathcal W_{5,4}&=
 \mathcal T_2\mathcal T_1^3+
 \mathcal T_1\mathcal T_2\mathcal T_1^2+
 \mathcal T_1^2\mathcal T_2\mathcal T_1+
 \mathcal T_1^3\mathcal T_2.
\end{aligned}                                      \tag{8}
\]

To prove the degree claim, note first that \(q_{m,r}\) has degree at most
\(r\).  Hence only \(r=m-1,m\) can contribute to degree \(m-1\).  The
leading coefficient for \(r=m-1\) is

\[
 \frac{2^{m-1}-2^m}{(m-1)!}
 =-\frac{2^{m-1}}{(m-1)!}.                         \tag{9}
\]

For \(r=m\), use

\[
 (x)_m=x^m-{m\choose2}x^{m-1}+O(x^{m-2}).
\]

The terms of degree \(m\) cancel between \({2t\choose m}\) and
\(2^m{t\choose m}\), while the coefficient of \(t^{m-1}\) in their
difference is

\[
 \frac{{m\choose2}2^{m-1}}{m!}
 =\frac{2^{m-2}}{(m-2)!}.                          \tag{10}
\]

Equations (9)--(10) prove (4).

## Width-first legitimacy for the quadratic two-hidden-layer network

The preceding operator proof can be transferred to the actual width-first
quadratic network without assuming a population Koopman intertwining.

Let

\[
 \psi(x)=c_1x+c_2x^2,
 \qquad c_1^2+3c_2^2=1,                              \tag{11a}
\]

where the normalization follows from
\(\mathbb E(c_1G+c_2G^2)^2=c_1^2+3c_2^2\).  At width \(n\), use the exact
network and ascent map

\[
 f_n(\theta)=\frac1n\sum_i a_i\psi(z_i),
 \qquad E_{h,n}(\theta)=\theta+hn\nabla f_n(\theta),
 \qquad F_{N,n}(h)=\mathbb E f_n(E_{h,n}^N\theta _0).             \tag{11b}
\]

As a polynomial in the raw parameters \((a,W,w)\), \(f_n\) has degree at
most seven: \(u\) has degree one, \(\psi(u)\) degree two, \(z=W\psi(u)\)
degree three, \(\psi(z)\) degree six, and multiplication by \(a\) gives
degree seven.  Hence \(n\nabla f_n\) has degree at most six.

Let \(d_s\) be the largest \(h\)-degree of a parameter coordinate after
\(s\) updates.  Then

\[
 d_0=0,
 \qquad d_{s+1}\le1+6d_s,
 \qquad d_s\le\frac{6^s-1}{5}.                     \tag{11c}
\]

Consequently \(F_{N,n}\) is a polynomial in \(h\) of degree at most

\[
 D_N=7\frac{6^N-1}{5},                              \tag{11d}
\]

independently of \(n\).  Gaussian integration changes coefficients but not
this degree.

Now take the width limit in the required order.  Fix \(N\), choose
\(D_N+1\) distinct nonzero step sizes in the interval on which the
fixed-step width theorem holds, and evaluate \(F_{N,n}\) there.  Those value
vectors converge by the fixed-step theorem.  Multiplication by the inverse
Vandermonde matrix proves convergence of every polynomial coefficient.
Thus the pointwise width-first limit \(F_N\) is the resulting polynomial and

\[
 [h^m]F_N(h)=\lim_{n\to\infty}[h^m]F_{N,n}(h).       \tag{11e}
\]

This is not an interchange of a width limit with differentiation: it is
finite-dimensional interpolation from fixed nonzero step sizes.

At each finite width, apply (1) with \(g=n\nabla f_n\), \(O=f_n\), and then
take expectation.  Write the resulting fifth-order Newton coefficients as
\(\Theta_{5,r,n}\).  They satisfy

\[
 [h^5]F_{N,n}(h)=\sum_{r=1}^5{N\choose r}\Theta_{5,r,n}.          \tag{11f}
\]

Moreover

\[
 \Theta_{5,r,n}=\Delta_N^r([h^5]F_{N,n})\big|_{N=0},             \tag{11g}
\]

so (11e) at the six fixed horizons \(N=0,\ldots,5\) proves convergence of
every \(\Theta_{5,r,n}\).  Denoting the limits by \(\Theta_{5,r}\), (11f)
passes to the width-first limit for every fixed \(N\).  Therefore all the
time polynomials below hold for the actual quadratic width-first network,
without assuming an autonomous population state representation.

At finite width each \(\Theta_{5,r,n}\) is a finite Wick contraction of a
polynomial in the initialized Gaussians.  Hence it is an explicit algebraic
expression in \((c_1,c_2)\) and \(n^{-1/2}\); its width limit is obtained by
retaining the surviving contractions.  In normalized coordinates
\((c_1,c_2)\), the result is polynomial.  In raw coordinates

\[
 c_1=\frac{\alpha}{\sqrt{\alpha^2+3\beta^2}},
 \qquad
 c_2=\frac{\beta}{\sqrt{\alpha^2+3\beta^2}},        \tag{11h}
\]

where \((\alpha,\beta)\ne(0,0)\), it is an explicit algebraic expression (a rational expression after adjoining
\(\sqrt{\alpha^2+3\beta^2}\)).

## Exact third- and fifth-order coefficients

Write

\[
 W_{m,r}=(\mathcal W_{m,r}O)(\theta _0),
 \qquad T_1^m=(\mathcal T_1^mO)(\theta _0),
 \qquad T_m=(\mathcal T_mO)(\theta _0).
\]

The cubic coefficient is

\[
\boxed{\begin{aligned}
K_3(t):=[h^3]\Delta_t(h)
={}&-6tT_3+(-2t^2+3t)W_{3,2}
       +2t(t-1)T_1^3,\\
W_{3,2}={}&((\mathcal T_1\mathcal T_2+
              \mathcal T_2\mathcal T_1)O)(\theta _0).
\end{aligned}}                                     \tag{11}
\]

Its degree-two part is

\[
 2t^2(T_1^3-W_{3,2}).                              \tag{12}
\]

The fifth-order coefficient is

\[
\boxed{\begin{aligned}
K_5(t):=[h^5]\Delta_t(h)
={}&-30tT_5+(-14t^2+15t)W_{5,2}\\
&+(-4t^3+14t^2-10t)W_{5,3}\\
&+\left(-\frac23t^4+6t^3-\frac{77}{6}t^2
          +\frac{15}{2}t\right)W_{5,4}\\
&+\left(\frac43t^4-7t^3+\frac{35}{3}t^2-6t\right)T_1^5.
\end{aligned}}                                     \tag{13}
\]

Equivalently, grouping by time degree,

\[
\begin{aligned}
K_5(t)={}&t^4\left(\frac43T_1^5-\frac23W_{5,4}\right)\\
&+t^3\left(-7T_1^5+6W_{5,4}-4W_{5,3}\right)\\
&+t^2\left(\frac{35}{3}T_1^5-\frac{77}{6}W_{5,4}
             +14W_{5,3}-14W_{5,2}\right)\\
&+t\left(-6T_1^5+\frac{15}{2}W_{5,4}-10W_{5,3}
           +15W_{5,2}-30T_5\right).
                                                               \tag{14}
\end{aligned}
\]

Thus

\[
 \lim_{t\to\infty}\frac{K_5(t)}{t^4}
 =\left[
 \frac43\mathcal T_1^5-\frac23\mathcal W_{5,4}
 \right]O(\theta _0).                              \tag{15}
\]

In particular, a \(t^5\) lower bound for this coefficient is impossible for
any fixed activation: the coefficient is identically a polynomial of degree
at most four.  If (15) is nonzero it is asymptotically of exact order
\(t^4\); if it vanishes, it has degree at most three.

An explicit coefficient bound, useful after inserting Gaussian activation
integrals, is

\[
 |K_5(t)|\le t^4\bigl(
 \frac43|T_1^5|+\frac23|W_{5,4}|+4|W_{5,3}|+
 14|W_{5,2}|+30|T_5|\bigr).                        \tag{16}
\]

To verify every numerical constant, factor

\[
\begin{aligned}
q_{5,2}(t)&=t(15-14t),\\
q_{5,3}(t)&=-2t(t-1)(2t-5),\\
q_{5,4}(t)&=\frac{t(t-1)}6(-4t^2+32t-45),\\
q_{5,5}(t)&=\frac{t(t-1)(t-2)}3(4t-9).
\end{aligned}
\]

For integer \(t\ge1\), these have absolute values at most, respectively,

\[
 14t^4,\qquad4t^4,\qquad\frac23t^4,
 \qquad\frac43t^4.
\]

The first, second, and fourth inequalities follow immediately from the
displayed factors (checking the zero factors at \(t=1,2\)).  For the third,
check \(t=1,\ldots,6\) directly; for \(t\ge7\),
\(|-4t^2+32t-45|\le4t^2\).  Finally
\(|q_{5,1}(t)|=30t\le30t^4\).  This proves (16).

The constant in (16) contains only the order-five jet of the vector field
and observable at initialization.  In a finite polynomial Gaussian OMFP
DAG, every entry is therefore a finite Gaussian moment expression.  Formula
(16) concerns the coefficient of \(h^5\); it does not, by itself, bound the
full finite-\(h\) Taylor tail uniformly in \(t\).

## Newton form, coefficient distinction, and the identity check

Define the fifth coefficient of one trajectory by

\[
 c_5(N):=[h^5]F_N(h),
 \qquad
 \Theta_{5,r}:=(\mathcal W_{5,r}O)(\theta _0).
\]

Formula (1) is the exact Newton polynomial

\[
 \boxed{c_5(N)=\sum_{r=1}^5{N\choose r}\Theta_{5,r}.}            \tag{19}
\]

Equivalently, write \(c_5(N)=\sum_{d=1}^5\gamma_dN^d\), where

\[
\begin{aligned}
\gamma _1&=\Theta_{5,1}-\frac12\Theta_{5,2}
 +\frac13\Theta_{5,3}-\frac14\Theta_{5,4}+\frac15\Theta_{5,5},\\
\gamma _2&=\frac12\Theta_{5,2}-\frac12\Theta_{5,3}
 +\frac{11}{24}\Theta_{5,4}-\frac{5}{12}\Theta_{5,5},\\
\gamma _3&=\frac16\Theta_{5,3}-\frac14\Theta_{5,4}
 +\frac{7}{24}\Theta_{5,5},\\
\gamma _4&=\frac1{24}\Theta_{5,4}-\frac1{12}\Theta_{5,5},\\
\gamma _5&=\frac1{120}\Theta_{5,5}.
\end{aligned}                                                     \tag{19a}
\]

It is essential not to confuse this with the coefficient in the doubled
comparison.  Namely,

\[
 [h^5]F_t(2h)=32c_5(t),
\]

and hence

\[
 \boxed{[h^5]\Delta_t(h)=c_5(2t)-32c_5(t)
 =\sum_{r=1}^5\left({2t\choose r}-32{t\choose r}\right)
 \Theta_{5,r}.}                                      \tag{20}
\]

The same identity in the power basis is

\[
 [h^5]\Delta_t(h)
 =-30\gamma _1t-28\gamma _2t^2-24\gamma _3t^3
   -16\gamma _4t^4.                                  \tag{20a}
\]

The \(t^5\) term is absent because its multiplier is
\(2^5-32=0\).

The five exact Newton multipliers in (20) are

\[
\begin{array}{c|l}
r&q_{5,r}(t)\\ \hline
1&-30t,\\
2&-14t^2+15t,\\
3&-4t^3+14t^2-10t,\\
4&-\frac23t^4+6t^3-\frac{77}{6}t^2+\frac{15}{2}t,\\
5&\frac43t^4-7t^3+\frac{35}{3}t^2-6t.
\end{array}                                           \tag{21}
\]

As a completely independent arithmetic check, specialize to the established
width-first \(L=2\) identity-activation recursion.  Its direct Gaussian
calculation gives

\[
\begin{aligned}
[h^3]F_N(h)&=24{N\choose2}+48{N\choose3},\\
[h^5]F_N(h)&=20{N\choose2}+465{N\choose3}
 +1702{N\choose4}+1464{N\choose5}.                  \tag{22}
\end{aligned}
\]

Thus

\[
 (\Theta_{5,1},\ldots,\Theta_{5,5})
 =(0,20,465,1702,1464).
\]

Substitution into (20)--(21), with no fitted coefficients, yields

\[
\boxed{
[h^5]\Delta_t(h)
=\frac{2452}{3}t^4-1896t^3
+\frac{4403}{3}t^2-369t.}                            \tag{23}
\]

Similarly, substituting the cubic Newton coefficients from (22) into the
three cubic multipliers gives

\[
\boxed{[h^3]\Delta_t(h)=24t(2t-1).}                 \tag{24}
\]

At \(t=2\), (23) is \(3042\), so in the present fine-minus-coarse
orientation

\[
 F_4(h)-F_2(2h)=144h^3+3042h^5+\text{higher odd powers}.
\]

This also audits the sign: formulas written for
\(F_t(2h)-F_{2t}(h)\) have the negatives of (23)--(24).

The leading quartic functional is

\[
 L_5(\psi)=\frac43\Theta_{5,5}(\psi)
            -\frac23\Theta_{5,4}(\psi).             \tag{24a}
\]

At the \(L=2\) identity activation, (22) gives

\[
 L_5(\mathrm{id})=\frac{2452}{3}>0.                 \tag{24b}
\]

For the normalized quadratic family, every \(\Theta_{5,r}\) is a finite
polynomial in \((c_1,c_2)\), by the finite Wick construction following
(11h).  Hence (24a) is polynomial on the normalization ellipse.  It follows
that a whole neighbourhood of \((c_1,c_2)=(1,0)\) retains a nonzero quartic
coefficient.  Thus a small but fixed quadratic component does not generally
reduce the exact time degree below four; it also can never increase it to
five.  Producing a numerical radius for this neighbourhood requires the
explicit finite Wick coefficient ledger, not the universal time algebra.

## Parity audit

The Euler algebra alone does **not** imply that \(\Delta_t\) is odd.  In
general,

\[
 [h^2]\Delta_t
 =t\bigl[(\mathcal T_1^2-2\mathcal T_2)O\bigr](\theta _0),       \tag{25}
\]

and

\[
\begin{aligned}
[h^4]\Delta_t={}&-14tT_4+(-6t^2+7t)W_{4,2}\\
&+\left(-\frac43t^3+6t^2-\frac{14}{3}t\right)W_{4,3}\\
&+\left(2t^3-\frac{11}{2}t^2+\frac72t\right)T_1^4.
                                                               \tag{26}
\end{aligned}
\]

Therefore an OMFP sign involution or another network-specific argument is
needed to assert

\[
 \Delta_t(-h)=-\Delta_t(h).
\]

Here is the exact involution criterion.  Suppose \(X\) is Hilbert, the
training vector field is \(g=\nabla O\), and an orthogonal involution \(S\)
satisfies

\[
 O(Sx)=-O(x),\qquad S\theta _0\stackrel{d}=\theta _0.             \tag{27}
\]

Differentiating the first identity gives

\[
 g(Sx)=-Sg(x).
\]

It follows exactly that

\[
 E_{-h}(Sx)=S E_h(x),
 \qquad E_{-h}^N(Sx)=S E_h^N(x).
\]

Taking expectation over an \(S\)-invariant initialization proves
\(F_N(-h)=-F_N(h)\), and hence the required parity of \(\Delta_t\).

For the exact width-\(n\), two-hidden-layer network, write

\[
 f_n(a,W,w)=\frac1n\sum_i a_i\phi(z_i(W,w)),
 \qquad E_{h,n}(\theta)=\theta+hn\nabla f_n(\theta).
\]

Define

\[
 S(a,W,w)=(-a,W,w).
\]

Then \(S\) is orthogonal,

\[
 f_n(S\theta)=-f_n(\theta),
 \qquad \nabla f_n(S\theta)=-S\nabla f_n(\theta),                 \tag{28}
\]

and therefore

\[
 E_{-h,n}(S\theta)=S E_{h,n}(\theta).                            \tag{29}
\]

For an entirely componentwise check of (27), under \(a\mapsto-a\) one has
\(C_i=a_i\phi'(z_i)\mapsto-C_i\) and
\(b_j=n^{-1/2}\sum_iW_{ij}C_i\mapsto-b_j\).  Replacing \(h\) by \(-h\)
in

\[
\begin{aligned}
a_i^+&=a_i+h\phi(z_i),\\
W_{ij}^+&=W_{ij}+\frac h{\sqrt n}C_iH_j,\\
u_j^+&=u_j+h b_j\phi'(u_j)
\end{aligned}
\]

then gives exactly the \(S\)-image of the \(+h\) update.  The independent
centered Gaussian initialization is invariant under \(S\).  Induction in
the number of steps, followed by expectation, proves at every finite width

\[
 F_{N,n}(-h)=-F_{N,n}(h).                           \tag{30}
\]

Taking the already-established pointwise fixed-\(h\) width limit preserves
(30).  This proof works for every hidden activation; in particular the even
quadratic component causes no problem.

Once that identity has independently been proved, (25)--(26) vanish after
evaluation at \(\theta _0\), and the expansion through order five is

\[
 \Delta_t(h)=K_3(t)h^3+K_5(t)h^5+O(h^7).
\]

The odd parity does not change (11), (13), or the degree-four conclusion.

## Algebraic audit

1. **Noncommutativity.**  No commuting of \(\mathcal T_i\) and
   \(\mathcal T_j\) was used.  Every ordered composition occurs in
   \(\mathcal W_{m,r}\).
2. **Short horizons.**  The polynomial convention \({N\choose r}=0\) for
   integers \(N<r\) makes every formula valid for \(t=1,2,\ldots\).
3. **Consistency order.**  The constant and linear coefficients cancel:
   \(q_{0,0}=0\) and \(q_{1,1}=2t-2t=0\).  The first generic discrepancy is
   (17), as it must be for step doubling of explicit Euler.
4. **Leading-degree cancellation.**  The only apparent \(t^5\) term in
   (13) comes from \(\mathcal T_1^5\), and it cancels exactly because
   \((2t)^5=2^5t^5\).  No norm or activation estimate is involved.
5. **Integer checks.**  For \(t=1\), the coefficients multiplying
   \(W_{5,4}\) and \(T_1^5\) in (13) are both zero, agreeing with
   \({2\choose4}={2\choose5}={1\choose4}={1\choose5}=0\).  For \(t=2\),
   the \(T_1^5\) coefficient is zero and the \(W_{5,4}\) coefficient is
   one, agreeing with \({4\choose5}-32{2\choose5}=0\) and
   \({4\choose4}-32{2\choose4}=1\).
6. **Scope.**  The calculation proves an exact statement about Taylor
   coefficients of an autonomous explicit-Euler iteration.  Applying it to
   a width-first OMFP limit requires the already-established identification
   of that limit as iteration of the same \(h\)-independent vector field and
   observable.  It does not exchange width and learning-rate limits.
7. **Every fifth-order multiplier.**  Direct expansion gives

   \[
   \begin{array}{c|l|l}
   r&{2t\choose r}&32{t\choose r}\\ \hline
   1&2t&32t\\
   2&2t^2-t&16t^2-16t\\
   3&\frac43t^3-2t^2+\frac23t
     &\frac{16}{3}t^3-16t^2+\frac{32}{3}t\\
   4&\frac23t^4-2t^3+\frac{11}{6}t^2-\frac12t
     &\frac43t^4-8t^3+\frac{44}{3}t^2-8t\\
   5&\frac4{15}t^5-\frac43t^4+\frac73t^3-\frac53t^2+\frac25t
     &\frac4{15}t^5-\frac83t^4+\frac{28}{3}t^3
       -\frac{40}{3}t^2+\frac{32}{5}t.
   \end{array}
   \]

   Rowwise subtraction is exactly (21).  In the last row the
   \(\frac4{15}t^5\) terms coincide, which is the advertised fifth-degree
   cancellation.  As a discrete check, for \(t=1\) the multiplier vector is
   \((-30,1,0,0,0)\); for \(t=2\) it is
   \((-60,-26,4,1,0)\).  These are respectively
   \(({2\choose r}-32{1\choose r})_{r=1}^5\) and
   \(({4\choose r}-32{2\choose r})_{r=1}^5\).

## What the fifth coefficient does and does not prove

Assuming the oddness just proved and existence of the fifth derivative,
(13) is exactly

\[
 \lim_{h\to0}
 \frac{\Delta_t(h)-K_3(t)h^3}{h^5}=K_5(t)            \tag{31}
\]

for each fixed integer \(t\).  Equations (13) and (16) prove the sharp
time-degree statement

\[
 |K_5(t)|\le C_5t^4,
\]

with an initialization-jet constant \(C_5\), and the identity example (23)
shows that degree four really occurs at \(L=2\).

They do **not** prove the interval estimate

\[
 |\Delta_t(h)-K_3(t)h^3|\le Ct^4|h|^5,
 \qquad |h|\le\rho/t.                              \tag{32}
\]

Indeed, (32) must simultaneously control every odd order \(m\ge7\).  The
same Euler argument bounds the time degree of the coefficient of \(h^m\) by
\(m-1\), but it supplies no order-uniform bound on the associated
elementary-differential aggregates.  At \(|h|=\rho/t\), a bound of the form

\[
 |[h^m]\Delta_t|\le C_m t^{m-1}
\]

contributes \(C_m\rho^m/t\).  Summability therefore requires a proved
geometric (or better) control of \(C_m\) in the source/order index.  The
order-five calculation contains no such all-order control.  Thus it proves
the desired polynomial bound for the fifth coefficient, but not the uniform
finite-step remainder theorem (32).
