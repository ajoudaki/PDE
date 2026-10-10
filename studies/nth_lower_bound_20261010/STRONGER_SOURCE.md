# Factorial source derivatives and a polynomial direct-array lower bound

Status: author-derived strengthening within the existing study; not yet
independently checked or promoted. Author: /root/nth_lower_scalar,
2026-10-10.

The scientific input scope was the supervisor's proposed invariant/source
comparison, the existing normalized deep linear witness in RESULT.md,
the common analytic-disk argument and endpoint inequality in
ANALYTIC_ROUTE.md, and this author's earlier same-study work. No other
study, established-book source, or external scientific source was read.
The consulted versions have SHA256

- RESULT.md:
  8ee19b4517f5e90c31f67cc02f143ba62dc35d2794eca7cde961efbacfa55bb1;
- ANALYTIC_ROUTE.md:
  1770611b10f1909c9fcd6540dceafda65bd51e6c97a37845fd2553eca86b1cf4.

The two new ingredients are proved below. First, retaining the motion of
the second hidden matrix gives factorially large source derivatives,
rather than the constant lower bound obtained by freezing that matrix.
Second, those factorial derivatives yield a geometric physical-time error
bound. The resulting necessary order is proportional to \(\log n\),
and explicit tensor arrays require at least \(n^{\alpha_\eta-o(1)}\)
coordinates for a fixed positive exponent \(\alpha_\eta\). No claim that
\(\alpha_\eta\geq1\), or that every reduced model needs this storage, follows.

## Setup and inherited facts

The normalized network and loss are

\[
f(v)=c^\top WBv,\qquad
B\in\mathbb R^{n\times2},\quad W\in\mathbb R^{n\times n},
\quad c\in\mathbb R^n,
\qquad
\mathcal L=\frac14\bigl[(f(e_1)-\eta)^2+f(e_2)^2\bigr],
\]

with the Euclidean metric on all three parameter blocks, \(c_0=0\),
and \(0<\eta\leq10^{-62}\) fixed independently of width. The two columns
of \(B_0\), and all entries of \(W_0\), have the independent
\(N(0,1/n)\) initialization specified in RESULT.md. Define \(K_1=f\),
and obtain \(K_{r+1}\) by taking a directional derivative of \(K_r\)
along the gradient of the prediction at its appended training index.
The order-\(q\) closure copies the initial coefficients through rank \(q\),
freezes its top rank, and evolves all lower ranks with its own residual.

The following already proved facts are used with precisely these hypotheses.

1. On one event of probability at least \(1-Ce^{-cn}\),
   \[
   \frac12I\preceq B_0^\top B_0\preceq2I,\qquad
   \|W_0\|_{\mathrm{op}}\leq4,\qquad
   \sigma_{\min}(W_0B_0)\geq\frac34.
   \tag{1}
   \]
   This event is independent of the hierarchy order.
2. Odd top ranks are initially zero, so order \(q\) has the same output
   as its effective even order \(2\lfloor q/2\rfloor\). Writing
   \[
   j=2\lfloor q/2\rfloor+1,
   \qquad g_{n,q}(t)=f_{n,1}(t)-f^{(q)}_{n,1}(t),
   \]
   the first unmatched physical-time derivative is exactly
   \[
   g_{n,q}^{(j)}(0)
   =\left(\frac\eta2\right)^j
       K_{j+1}(1,\ldots,1)(0).
   \tag{2}
   \]
   Its proof includes the feedback from the closure's own residual;
   it does not equate dense and closure clocks.
3. On (1), all these discrepancy functions are holomorphic on a
   neighborhood of the closed disk \(|t|\leq R\), with
   \[
   R=\frac1{8192},\qquad |g_{n,q}(t)|\leq2.
   \tag{3}
   \]
   The bounds hold simultaneously for every finite \(q\), with no width
   dependence. This is the ordered-Volterra contraction in
   ANALYTIC_ROUTE.md.
4. The actual all-time, whole-sphere discrepancy \(D_n\) between two
   independent dense initializations is \(O_{\mathbb P}(n^{-1/2})\),
   by the global sensitivity and Gaussian-extension proof in RESULT.md.

The new source estimate only needs the first two positive lower bounds
in (1); the operator upper bounds enter through (3).

## A coefficientwise lower bound retaining both trained hidden layers

Follow gradient ascent for the first prediction with unit residual,
using an auxiliary source variable \(s\). Put \(a=Be_1\), so this source
flow is

\[
a'=W^\top c,\qquad W'=ca^\top,\qquad c'=Wa,
\qquad (a,W,c)(0)=(a_0,W_0,0).
\tag{4}
\]

Primes in (4) and until (14) mean source derivatives, not physical-time
derivatives. Let

\[
A=\|a_0\|^2,\qquad
G=W_0W_0^\top,\qquad
h=W_0a_0,\qquad H=\|h\|^2.
\]

On (1), \(A\geq1/2\) and \(H\geq(3/4)^2\geq1/2\).
Direct differentiation of (4) gives the exact invariants

\[
WW^\top-cc^\top=G,\qquad
\|a\|^2-\|c\|^2=A.
\tag{5}
\]

Indeed the derivative of the first difference is
\(ca^\top W^\top+Wac^\top-c'c^\top-cc'^\top=0\);
the second follows from
\(a^\top W^\top c=c^\top Wa\). Therefore

\[
c''=W'a+Wa'
=(AI+G)c+2\|c\|^2c,
\qquad c(0)=0,\quad c'(0)=h.
\tag{6}
\]

Diagonalize the symmetric positive semidefinite matrix \(G\) by an
orthogonal change of coordinates. Independent sign changes in its
eigenvectors make every component of the transformed \(h\) nonnegative
without changing the nonnegative diagonal entries of \(G\). Orthogonality
preserves \(c^\top c'\), \(H\), and (6), so work in these coordinates.

For analytic power series, write \(p\succeq r\) if every Taylor
coefficient of \(p-r\) is nonnegative, componentwise for vectors.
The solution of (6) has nonnegative Taylor coefficients: if
\(c(s)=\sum_m c_m s^m\), its recurrence is

\[
(m+2)(m+1)c_{i,m+2}
=(A+G_{ii})c_{i,m}
+2\sum_{\ell}\ \sum_{p+q+r=m}c_{\ell,p}c_{\ell,q}c_{i,r}.
\tag{7}
\]

Its initial coefficients are \(c_0=0\), \(c_1=h\geq0\), and every
quantity on the right is a nonnegative combination of previously
determined coefficients. The same recurrence also shows that only odd
powers occur. Polynomial ODEs have local analytic solutions, so these
formal recurrences are their actual local Taylor coefficients.

Let \(u\) solve the scalar initial-value problem

\[
u''=Au+2Hu^3,\qquad u(0)=0,\quad u'(0)=1.
\tag{8}
\]

Its coefficients are nonnegative as well. Substituting \(hu\) into
the right side of (6) gives the right side of \(h u''\), plus the
componentwise nonnegative term \(Ghu\). Induction in the recurrence
(7) therefore proves

\[
c\succeq hu.
\tag{9}
\]

This argument does not divide by \(h_i\); zero components cause no
exception.

The function \(v(s)=2\tan(s/2)\) has the same initial derivative as \(u\)
and satisfies

\[
v''=\frac12v+\frac18v^3,\qquad v(0)=0,\quad v'(0)=1.
\tag{10}
\]

Since \(A\geq1/2\), \(2H\geq1\geq1/8\), and the scalar Taylor
recurrences have nonnegative coefficients, the same induction gives
\(u\succeq v\). This comparison is stronger than the sufficient
\(u\succeq\tan(s/2)\) proposed in the assignment.

For an elementary quantitative tangent bound, write

\[
\tan z=\sum_{k=0}^\infty t_k z^{2k+1}.
\]

The identity \((\tan z)'=1+\tan^2z\) gives

\[
t_0=1,\qquad
(2k+1)t_k=\sum_{i=0}^{k-1}t_i t_{k-1-i}\quad(k\geq1).
\]

Inductively, if \(t_i\geq3^{-i}\) for \(i<k\), then

\[
t_k\geq\frac{k\,3^{-(k-1)}}{2k+1}
\geq3^{-k},
\]

because \(3k\geq2k+1\) for \(k\geq1\). Hence

\[
v(s)\succeq w(s):=\frac{s}{1-s^2/12}.
\tag{11}
\]

The source prediction is

\[
F(s)=c^\top Wa=c^\top c'.
\]

Differentiation and multiplication preserve coefficientwise inequalities
between series with nonnegative coefficients. Equations (9)--(11) yield

\[
F\succeq H w w'
=H\,s\,\frac{1+s^2/12}{(1-s^2/12)^3}.
\tag{12}
\]

For \(j=2k+1\), the coefficient of \(s^j\) in this last series is
\(H(k+1)^2\,12^{-k}\), since the coefficient of \(x^k\) in
\((1+x)/(1-x)^3\) is \((k+1)^2\). Thus, simultaneously for every
odd \(j\geq1\),

\[
F^{(j)}(0)
\geq j!\,\frac{(k+1)^2}{2\,12^k}
\geq j!\,8^{-j}.
\tag{13}
\]

The final, deliberately weaker inequality follows because the ratio
of its preceding coefficient to \(8^{-(2k+1)}\) is
\(4(k+1)^2(64/12)^k\geq1\).

Successive source derivatives are successive all-first-sample Lie
derivatives, so
\(F^{(j)}(0)=K_{j+1}(1,\ldots,1)(0)\). Combining (13) with the exact
physical jet (2) proves

\[
g_{n,q}^{(j)}(0)\geq
j!\left(\frac\eta{16}\right)^j,
\qquad j=2\lfloor q/2\rfloor+1.
\tag{14}
\]

This is deterministic on (1) and simultaneous in the order. The
factorial is essential to the improvement below.

## A factorial derivative forces a geometric real-interval error

Here is the scalar analytic statement with explicit constants. Suppose
\(g\) is holomorphic on a neighborhood of the closed disk \(|z|\leq R\),
\(|g|\leq M\) there, and, for some integer \(j\geq1\) and \(\rho>0\),

\[
|g^{(j)}(0)|\geq j!\rho^j.
\tag{15}
\]

Define

\[
\theta=\frac{\rho R}{8},\quad
b=\max\{0,\log(1/\theta)\},\quad
d=\max\{0,\log(4M/3)\},\quad
\kappa=16(1+b+d),\quad N=\lceil\kappa j\rceil.
\tag{16}
\]

Then

\[
\sup_{0\leq t\leq R/4}|g(t)|
\geq\frac{\theta^j(j!)^2}{4N^{2j+1}}
\geq\frac1{8\kappa}
       \left(\frac{\theta}{8e^2\kappa^2}\right)^j.
\tag{17}
\]

To prove it, let \(P_N\) be the Taylor polynomial of \(g\) of degree
\(N\). Cauchy's coefficient bound gives

\[
\|g-P_N\|_{[0,R/4]}\leq\frac M3\,4^{-N}.
\tag{18}
\]

The required polynomial endpoint estimate, proved in ANALYTIC_ROUTE.md,
is

\[
|P_N^{(j)}(0)|
\leq\frac{2N}{j!}
       \left(\frac{8N^2}{R}\right)^j
       \|P_N\|_{[0,R/4]}.
\tag{19}
\]

Its relevant mechanism can be restated briefly: after mapping the interval
to \([-1,1]\), every nonconstant Chebyshev coefficient is bounded by twice
the polynomial supremum, while

\[
|T_k^{(j)}(-1)|
=\prod_{r=0}^{j-1}\frac{k^2-r^2}{2r+1}
\leq\frac{k^{2j}}{j!}
\quad(j\leq k).
\]

Summing over at most \(N\) coefficients and applying the affine
derivative factor \((8/R)^j\) gives (19), including for complex
coefficients.

Since \(N\geq j\), the Taylor polynomial has exactly the same \(j\)-th
derivative as \(g\). Put \(S=\|g\|_{[0,R/4]}\). Equations
(15), (18), and (19) imply

\[
S\geq\frac{\theta^j(j!)^2}{2N^{2j+1}}
        -\frac M3\,4^{-N}.
\tag{20}
\]

There are two factorials in (20): one comes from the assumed derivative,
the other from the polynomial endpoint estimate. This permits a Taylor
degree linear in \(j\).

We verify the tail comparison without suppressing its \(j\)-dependence.
The inequalities

\[
N\leq2\kappa j,\qquad
\log(j!)\geq j\log j-j,\qquad \log j\leq j
\]

give

\[
\begin{aligned}
&j\log(1/\theta)+(2j+1)\log N-2\log(j!)
                  +\log(4M/3)\\
&\quad\leq
 jb+(2j+1)\log(2\kappa)+\log j+2j+d\\
&\quad\leq
 j\,[b+d+3\log(2\kappa)+3].
\end{aligned}
\tag{21}
\]

Set \(D=1+b+d\geq1\). Since \(\kappa=16D\),
\(\log32<4\), and \(\log D\leq D-1\),

\[
b+d+3\log(2\kappa)+3
=D+2+3\log(32D)
\leq4D+11
\leq15D
<\kappa\log4.
\tag{22}
\]

Here \(\log4>1\). Combining (21)--(22) with \(N\geq\kappa j\)
and exponentiating proves

\[
\frac M3\,4^{-N}
\leq\frac{\theta^j(j!)^2}{4N^{2j+1}}.
\tag{23}
\]

This proves the first inequality in (17). The elementary factorial bound
used above also gives \(j!\geq(j/e)^j\), so

\[
\frac{\theta^j(j!)^2}{4N^{2j+1}}
\geq\frac1{8\kappa j}
       \left(\frac{\theta}{4e^2\kappa^2}\right)^j
\geq\frac1{8\kappa}
       \left(\frac{\theta}{8e^2\kappa^2}\right)^j,
\]

where the last step uses \(j\leq2^j\). This proves (17) for every
\(j\geq1\), including the smallest derivative order. The maxima in
(16) make the tail argument valid even when \(\theta>1\) or \(M<3/4\);
in the present network specialization neither exception occurs.

## Application: order proportional to log width

Use (14), (3), and (17) with
\(\rho=\eta/16\), \(R=1/8192\), and \(M=2\). Define the fixed constants

\[
\theta_\eta=\frac{\eta}{2^{20}},\qquad
\kappa_\eta=
16\left[1+\log\frac{2^{20}}{\eta}+\log\frac83\right],
\qquad
C_\eta=\log\left(\frac{8e^2\kappa_\eta^2}{\theta_\eta}\right)>0.
\tag{24}
\]

On the same initialization event (1), simultaneously for every \(q\geq2\),

\[
\begin{aligned}
\sup_{0\leq t\leq1/32768}
|f_{n,1}(t)-f^{(q)}_{n,1}(t)|
&\geq
\frac{\theta_\eta^j(j!)^2}
     {4\lceil\kappa_\eta j\rceil^{2j+1}}\\
&\geq\frac1{8\kappa_\eta}\,e^{-C_\eta j},
\qquad j=2\lfloor q/2\rfloor+1.
\end{aligned}
\tag{25}
\]

This is a physical-time discrepancy with the closure's own residual.
It also lower-bounds the all-time, whole-sphere error \(E_n(q)\).
Failure of a closure to exist at later times remains a failure, as in
the original setup, and cannot invalidate the short-time lower bound.

If a deterministic sequence \(q_n\) satisfies

\[
\limsup_{n\to\infty}\frac{q_n}{\log n}
<\frac1{2C_\eta},
\tag{26}
\]

then the deterministic right side of (25), multiplied by \(\sqrt n\),
tends to infinity. The already proved \(D_n=O_{\mathbb P}(n^{-1/2})\)
therefore implies, for every fixed finite comparison factor \(A_0>0\),

\[
\mathbb P\{E_n(q_n)\leq A_0D_n\}\longrightarrow0.
\tag{27}
\]

Explicitly, with
\(b_n=(8\kappa_\eta)^{-1}e^{-C_\eta j(q_n)}\),
the probability in (27) is at most
\[
Ce^{-cn}
+\mathbb P\{\sqrt nD_n\geq\sqrt n b_n/A_0\}.
\]
The second term vanishes by tightness. No lower-tail estimate or
anti-concentration assumption for \(D_n\) is used.

Consequently, any deterministic order choice attaining a fixed positive
success probability for that constant-factor comparison at every
sufficiently large width must obey

\[
\liminf_{n\to\infty}\frac{q_n}{\log n}
\geq\frac1{2C_\eta}.
\tag{28}
\]

The same condition follows from \(E_n(q_n)=O_{\mathbb P}(n^{-1/2})\).
In that latter formulation, tightness and the deterministic lower bound
even give \(q_n\geq(\log n)/(2C_\eta)-O_\eta(1)\).

For the direct tensor-array implementation with two training samples,
retaining the effective even order still uses at least \(2^{q-1}\)
coordinates; its declared nonfrozen arrays use at least \(2^{q-2}\).
Thus (28) gives the explicit polynomial necessary size

\[
\text{retained coordinates}\ \geq\
n^{\alpha_\eta-o(1)},\qquad
\alpha_\eta=\frac{\log2}{2C_\eta}>0.
\tag{29}
\]

The same exponent applies to its declared moving arrays, with a fixed
factor difference. The two fixed unseen queries from RESULT.md inherit
(25) with the extra factor \(1/\sqrt2\), which leaves (28)--(29) unchanged.

This strengthens the earlier necessary \(\log n/\log\log n\) order and
subpolynomial direct-array bound. It does not prove a linear-in-width
storage lower bound: the explicit exponent in (29) is small. Nor does it
rule out compressed tensors, on-demand coefficient generation, a different
top closure, or another autonomous reduced model. The target \(\eta\) is
fixed; if it were allowed to vanish with width, then \(C_\eta\) would change
and the stated fixed polynomial exponent would not follow.

## Check record

The source invariants, transformed coefficient recurrences, tangent
coefficient induction, physical residual factor, and the all-\(j\) tail
comparison were derived and checked algebraically by this author.
The checks include zero components of \(h\), parity, the first possible
odd derivative, \(j=1\) in the scalar analytic lemma, and the two maxima
in (16). A requested fresh helper for the tail constants could not be
started because the agent-thread limit was reached; this file therefore
does not claim an additional independent check.

No numerical experiment was run. The uniform analytic disk, probability of
the good event, and all-time dense-pair comparison are explicit same-study
dependencies, as stated above. This file changes no main study artifact.

As a deterministic arithmetic check only, evaluating (24) and (29) with
awk at \(\eta=10^{-62}\) gave
\[
\kappa_\eta=2537.66477808,\qquad
C_\eta=176.38066004,\qquad
\alpha_\eta=0.0019649183.
\]
These rounded values illustrate the size of the proved positive exponent;
the symbolic formulas, not the numerical evaluation, establish the bound.
