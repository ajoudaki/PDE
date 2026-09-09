# Degree-\(d\) polynomial extension: exact sectors and audit boundary

## Result that is actually proved

Let

\[
 P(x)=\sum_{k=0}^d c_kx^k,\qquad d\ge2,\qquad c_d=\lambda>0,
 \qquad \mathbb E P(G)^2=1.
\]

Assume first that all \(c_k\ge0\).  For the same width-first \(L=2\)
feature-ascent network, put

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h).
\]

Then, for every \(\rho>0\),

\[
 \Delta_t(\rho/t)\longrightarrow+\infty .                 \tag{1}
\]

Consequently no bound whose right side is a fixed polynomial in \(t\)
times a fixed power of \(h\) can control the step-doubling remainder on
\(0<h\le\rho/t\).  In particular, if
\(\kappa_t=[h^3]\Delta_t(h)\), then

\[
 \sup_{t\ge1}\sup_{0<h\le\rho/t}
 \frac{|\Delta_t(h)-\kappa_th^3|}{t^4h^5}=\infty.          \tag{2}
\]

The same conclusion holds whenever one of the four exact activation
conjugates \(\varepsilon P(\sigma x)\),
\(\varepsilon,\sigma\in\{\pm1\}\), has nonnegative coefficients.

For arbitrary signs of the lower coefficients, the degree recurrences below
remain exact, but (1) is **not proved by this argument**.  Section 5 gives a
normalized quadratic counterexample to the tempting claim that a positive
leading coefficient makes the expected top-\(h\) coefficient positive.

## 1. Frozen scalar block

Deleting the bottom-coordinate update freezes the first-layer features.  As
in the quadratic proof, their empirical square norm converges to one, and a
top row converges at each fixed horizon to

\[
 A^+=A+hP(Z),\qquad Z^+=Z+hA P'(Z),                       \tag{3}
\]

with independent standard Gaussians \(A,Z\).  Write

\[
 \delta_N=\frac{d^N-1}{d-1},\qquad
 M_N=(d+1)\delta_N.                                      \tag{4}
\]

The greatest \(h\)-degree of both \(A_N\) and \(Z_N\) is \(\delta_N\),
and the greatest possible output degree is \(M_N\).  Indeed, if the two
current degrees are equal to \(\delta_N\), the leading branches in (3) give

\[
 \deg_h A_{N+1}=1+d\delta_N,qquad
 \deg_h Z_{N+1}=1+\delta_N+(d-1)\delta_N.
\]

Both equal \(\delta_{N+1}\).  Selecting only the leading monomial
\(\lambda x^d\) gives exponent vectors

\[
 a_{N+1}=d z_N,\qquad z_{N+1}=a_N+(d-1)z_N,               \tag{5}
\]

where \(a_0=(1,0)\) and \(z_0=(0,1)\) record powers of
\((A,Z)\).  Therefore the selected outer branch
\(\lambda A_NZ_N^d\) has exponent vector

\[
 o_N:=a_N+dz_N=d^N(1,d)=(d^N,d^{N+1}).                   \tag{6}
\]

The identity follows directly from

\[
 o_{N+1}=dz_N+d\{a_N+(d-1)z_N\}=d\,o_N.
\]

Every term of \(h\)-degree \(k\) in the pure-leading branch contains
exactly \(k+1\) factors \(\lambda\): one for every selected Euler update
and one in the terminal activation.  Hence the term in (6) has coefficient

\[
 b_N\lambda^{M_N+1},\qquad b_N\in\mathbb N,\qquad b_N\ge1. \tag{7}
\]

All statements are containments when lower activation monomials are present;
the joint maximal raw-degree sector cannot use a lower monomial.

### Even degree

If \(d\) is even, both exponents in (6) are even.  Thus the coefficient of
\(h^{M_N}\) in the expected output contains the strictly positive term

\[
 b_N\lambda^{M_N+1}
 \mathbb E G^{d^N}\,\mathbb E G^{d^{N+1}}.                \tag{8}
\]

### Odd degree

If \(d\) is odd, the two exponents in (6) are odd, so this particular top
term has zero Gaussian expectation.  The correct first surviving pure-leading
sector is one \(h\)-degree lower.

At time one, the degree-zero alternatives \(A\) and \(Z\) have exponent
offsets, relative to the leading terms,

\[
 e_A=(1,-d),\qquad e_Z=(-1,2-d).                          \tag{9}
\]

These offsets persist.  If an \(h\)-deficient term with offset \(e\) occurs
in \(Z_N\), selecting it once in \(Z_N^d\) puts the same offset in
\(A_{N+1}\).  Selecting a deficient \(A_N\), or one deficient \(Z_N\), in
\(A_NZ_N^{d-1}\) puts the same offset in \(Z_{N+1}\).  Induction therefore
shows that the coefficient of \(h^{M_N-1}\) in the output contains both

\[
 \begin{aligned}
 &(d^N+1,\ d^{N+1}-d),\\
 &(d^N-1,\ d^{N+1}-d+2),
 \end{aligned}                                           \tag{10}
\]

with positive integer multiples of \(\lambda^{M_N}\).  All four exponents
in (10) are even when \(d\) is odd.  Retaining either term gives a strictly
positive expected coefficient at degree \(M_N-1\).

## 2. Quantitative divergence of the retained term

Set \(N=2t\) and \(X=d^{2t}\).  Define

\[
 k_t=\begin{cases}
 M_{2t},&d\text{ even},\\
 M_{2t}-1,&d\text{ odd},
 \end{cases}
\qquad
 S_t=\begin{cases}
 (d+1)X,&d\text{ even},\\
 (d+1)X-(d-1),&d\text{ odd}.
 \end{cases}                                             \tag{11}
\]

Here \(S_t\) is the sum of the two even Gaussian exponents in the retained
term.  The larger exponent \(K_t\) satisfies \(K_t\ge S_t/2\).  For even
\(K=2m\),

\[
 \mathbb E G^K=(2m-1)!!\ge m!\ge(m/e)^m.                 \tag{12}
\]

The other even moment is at least one.  Thus the retained fine-grid term at
\(h=\rho/t\) is at least

\[
 L_t=\lambda^{k_t+1}\left(\frac\rho t\right)^{k_t}
 \left(\frac{S_t}{4e}\right)^{S_t/4}.                    \tag{13}
\]

The omitted integer coefficient is at least one.  Since

\[
 \frac{k_t}{X}\to\frac{d+1}{d-1},\qquad
 \frac{S_t}{X}\to d+1,
\]

division of the logarithm in (13) by \(X\) yields

\[
 \frac{\log L_t}{X}
 \ge \frac{d+1}{2}\,t\log d
   -\frac{d+1}{d-1}\log t+O_{d,\lambda,\rho}(1)
 \longrightarrow+\infty.                                \tag{14}
\]

Hence \(L_t\to\infty\).

For even \(d\), \(M_{2t}>M_t\).  For odd \(d\ge3\),

\[
 M_{2t}-1-M_t
 =\frac{d+1}{d-1}(d^{2t}-d^t)-1>0.                       \tag{15}
\]

Thus the coarse \(t\)-step output has no term at the retained fine-grid
degree.

## 3. Passage from the frozen block to the full network

When all activation coefficients are nonnegative, the network vector field
and output are positive-coefficient polynomials in the initialized raw
coordinates.  The exact step-doubling and deletion lemma from the quadratic
proof applies without change: the full paired defect has nonnegative
coefficients, and its coefficient with zero uses of the bottom-update block
is precisely the frozen paired defect.  Gaussian expectation preserves the
coefficientwise order.  At finite width,

\[
 \Delta_{t,n}(h)\ge D_{t,n}(h),\qquad h\ge0.              \tag{16}
\]

For every separately fixed \((t,h)\), a polynomial activation is
polynomially smooth.  The fixed-program width theorem therefore identifies
both limits in (16), including the reused matrix and transpose responses.
Taking \(n\to\infty\) first gives

\[
 \Delta_t(h)\ge D_t(h).                                  \tag{17}
\]

Equations (13)--(17) prove (1).  The coefficient of \(h^3\) in an
\(N\)-fold Euler composition is a sum over at most three update placements;
there are at most \(N^3\) placements, and every associated Gaussian
activation moment is fixed and finite.  Therefore
\(|\kappa_t|\le C_Pt^3\).  At \(h=\rho/t\), the subtracted cubic is bounded,
whereas \(L_t\to\infty\); this proves (2), and also defeats every fixed
polynomial in \(t\).

The limit order is, for each fixed integer \(t\),

\[
 n\to\infty\quad\text{at the fixed value }h=\rho/t,
 \qquad\text{then}\qquad t\to\infty.                    \tag{18}
\]

No joint width/time limit is used.

The conjugacies are the same at every degree.  Replacing \(P\) by
\(-P(-x)\) is implemented by \((a,W,u)\mapsto(-a,W,-u)\), and replacing
\(P\) by \(-P\) by \((a,W,u)\mapsto(-a,-W,u)\).  They are orthogonal, so
they conjugate the exact Euler maps and preserve Gaussian initialization.

## 4. Exact leading degrees in the unfrozen \(L=2\) network

This calculation is independent of the positivity assumption.  Put

\[
 r=d(d+1),\qquad
 \widehat\delta_N=\frac{r^N-1}{r-1}.                     \tag{19}
\]

Inside the top-\(h\)-degree coefficient, select the greatest raw-degree
branch.  The \(a,W,u\) parameter blocks all have

\[
 \deg_h=\widehat\delta_N,qquad
 \deg_{\rm raw}=r^N.                                     \tag{20}
\]

To verify this, suppose the common pair at time \(N\) is
\((\delta,R)\).  Then

\[
 H=P(u),\quad z=WH,\quad C=aP'(z),\quad
 b=W^TC
\]

and the three selected update branches have degree pairs

\[
 (1+r\delta,rR).
\]

For example, their raw degrees are

\[
 \begin{aligned}
 a^+ &: d(R+dR)=rR,\\
 W^+ &: R+(d-1)(R+dR)+dR=rR,\\
 u^+ &: R+R+(d-1)(R+dR)+(d-1)R=rR.
 \end{aligned}
\]

The same substitutions give the common \(h\)-degree \(1+r\delta\), proving
(20) by induction.

The terminal selected output sector has

\[
 \deg_h=(r+1)\widehat\delta_N,qquad
 \deg_{\rm raw}=(r+1)r^N.                               \tag{21}
\]

The activation-coefficient degree is explicit as well.  Each parameter
block has \(\lambda\)-degree

\[
 e_N=(d+1)\widehat\delta_N,
\]

because \(e_{N+1}=d+1+re_N\).  The terminal selected sector therefore
contains

\[
 (d+1)\{1+(r+1)\widehat\delta_N\}
\]

factors of \(\lambda\).

At width one, or at the level of total powers in the three initialization
groups, its exponent vector is

\[
 r^N(1,d,d^2)                                            \tag{22}
\]

for \((a^0,W^0,u^0)\).  Indeed, if \(v_a,v_W,v_u\) are the current exponent
vectors, the selected updates give

\[
 \begin{aligned}
 v_a^+&=dv_W+d^2v_u,\\
 v_W^+&=v_a+(d-1)v_W+d^2v_u,\\
 v_u^+&=v_a+dv_W+(d^2-1)v_u.
 \end{aligned}                                           \tag{23}
\]

The terminal functional is \(v_a+dv_W+d^2v_u\), and (23) multiplies it by
\(r\).  Its initial value is \((1,d,d^2)\), proving (22).

Since \(r\) is even for every \(d\ge2\), all three group powers in (22) are
even for \(N\ge1\).  The selected finite-width sector has nonnegative raw
coefficients and contains an all-same-index monomial with even powers, so its
finite-width Gaussian expectation is strictly positive.  This statement is
about the joint maximal \((h,\mathrm{raw})\) sector.  It does **not** by
itself give a positive lower bound after \(n\to\infty\), nor does it prevent
lower raw-degree sectors at the same \(h\)-degree from cancelling it after
Gaussian integration.

## 5. Fatal gap for arbitrary lower-coefficient signs

Positive leading coefficient alone does not imply positivity of the expected
top-\(h\) coefficient.  A one-step frozen calculation already disproves it.
For \(K\in\mathbb R\), let

\[
 P_K(x)=q_K(x^2-K),\qquad
 q_K=(K^2-2K+3)^{-1/2}.                                  \tag{24}
\]

Then \(\mathbb EP_K(G)^2=1\) and the leading coefficient \(q_K\) is positive.
From (3), the coefficient of \(h^3\) in
\(\mathbb E[A_1P_K(Z_1)]\) is

\[
 q_K\,\mathbb E A^2\,
 \mathbb E\{P_K(G)P_K'(G)^2\}
 =4q_K^4(3-K).                                           \tag{25}
\]

It is zero at \(K=3\) and negative for \(K>3\).  Thus neither the sign nor
strict nonvanishing of the integrated leading \(h\)-coefficient follows from
\(c_d>0\).

For arbitrary lower signs, deletion monotonicity also fails: the vector
field is no longer a positive-coefficient polynomial.  The exact degree
recurrences (4)--(7) and (19)--(23) isolate a positive leading **bidegree**
sector, but evaluating at the fixed initialization variance sums all raw
degrees.  A proof that the leading sector dominates that signed sum uniformly
as \(t\to\infty\) would be a new nonlocal Gaussian-tail theorem; it is not a
consequence of degree counting.  Therefore the arbitrary-sign version of
(1) remains open here.  Equation (25) is a counterexample to the missing
positivity lemma, not a counterexample to the eventual nonlocal no-go
conclusion itself.

## 6. Chebyshev repair for arbitrary signs in the frozen block

> **Supersession note.**  The restriction \(c_{d-1}=0\) in the odd-degree
> route below has since been removed by the exact translation
> \(Y=Z+c_{d-1}/(dc_d)\).  The complete arbitrary-sign scalar theorem and
> its independent audit are in
> `../temporary_polynomial_uniform_no_go/SIGNED_SCALAR_CHEBYSHEV_THEOREM.md`
> and `../temporary_polynomial_uniform_no_go/AUDIT_SIGNED_SCALAR_CHEBYSHEV.md`.
> The full-network boundary stated here is unchanged.

Although (25) defeats coefficientwise positivity, a Chebyshev extremal
argument removes cancellation between different powers of \(h\).  It gives a
complete arbitrary-sign no-go theorem for the scalar frozen recursion (3),
in every degree \(d\ge2\).  Chebyshev does not restore the comparison (16)
with the full network.

Let \(\bar F_N(h)=\mathbb E[A_NP(Z_N)]\) for (3), and put

\[
 \bar\Delta_t(h)=\bar F_{2t}(h)-\bar F_t(2h).
\]

For every fixed polynomial \(P\) of degree \(d\ge2\) with leading
coefficient \(\lambda>0\), every \(\rho>0\), and every fixed
\(r,s\ge0\),

\[
 \sup_{t\ge1}\sup_{0<h\le\rho/t}
 \frac{|\bar\Delta_t(h)-\bar\kappa_t h^3|}{t^rh^s}=\infty,
 \qquad \bar\kappa_t=[h^3]\bar\Delta_t(h).               \tag{26}
\]

### 6.1 Exact top coefficients

Let \(N\ge1\), \(m=d^{N-1}\), and \(n=d^N\).  After the first update, the
top-\(h\) coefficients are

\[
 X=P(Z),\qquad Y=A P'(Z).
\]

All later top-degree choices must use the leading monomial of \(P\) and
\(P'\).  The exponent recursion (5) therefore gives the exact identity

\[
 [h^{M_N}]\{A_NP(Z_N)\}
 =\Gamma_N X^mY^n,                                      \tag{27}
\]

where

\[
 \Gamma_N=d^{q_N}\lambda^{L_N}>0,
 \qquad
 L_N=M_N+1-(m+n),\qquad q_N\in\mathbb N_0.              \tag{28}
\]

The value of \(q_N\) is immaterial; (28) follows by counting the derivative
factor \(d\) and the factors \(\lambda\) in every post-first-step leading
node.  The total activation-scaling degree on both sides of (27) is
\(M_N+1\), which gives the displayed \(L_N\).

Taking expectation in (27) yields

\[
 a_{N,M_N}
 =\Gamma_N\,\mathbb E A^n\,
   \mathbb E\{P(G)^mP'(G)^n\}.                           \tag{29}
\]

If \(d\) and \(N\) are even, then \(m,n\) are even.  The integrand in
(29) is nonnegative and not almost surely zero, so
\(a_{N,M_N}>0\).

If \(d\) is odd, then \(n\) is odd and (29) vanishes.  Replacing one copy
of \(hX\) by \(A\), or one copy of \(hY\) by \(Z\), gives

\[
\begin{aligned}
 a_{N,M_N-1}
 =\Gamma_N\{&m\,\mathbb E A^{n+1}
       \mathbb E[P(G)^{m-1}P'(G)^n]\\
 &+n\,\mathbb E A^{n-1}
       \mathbb E[G P(G)^mP'(G)^{n-1}]\}.
                                                               \tag{30}
\end{aligned}
\]

These are the two old-variable contributions from (10).

If \(c_{d-1}\ne0\), there is one additional, equally high \(h\)-degree
source: at the second Euler step, the \(c_{d-1}Z^{d-1}\) branch of \(P\)
and the \((d-1)c_{d-1}Z^{d-2}\) branch of \(P'\) each lose exactly one
power of \(h\).  Direct differentiation of the post-second-step leading
monomial gives the exact correction

\[
 \Gamma_N\frac{m c_{d-1}}{\lambda}\,
 \mathbb E A^{n-1}
 \mathbb E[P(G)^mP'(G)^{n-1}].                          \tag{30a}
\]

Thus the exact coefficient is (30) plus (30a).  The independent exact checker
`audit_general_polynomial_chebyshev.py` verifies (29), (30), and (30a)
coefficientwise for signed quadratic, cubic, and quartic examples.

### 6.2 Activation-defined tail bounds

Choose \(R\ge1\), computably from the coefficients of \(P\), so that for
\(|x|\ge R\),

\[
 |P(x)|\ge\frac\lambda2|x|^d,qquad
 |P'(x)|\ge\frac{d\lambda}{2}|x|^{d-1}.                  \tag{31}
\]

When \(d\) is odd, enlarge \(R\) so that also

\[
 P'(x)>0,qquad xP(x)>0,qquad |x|\ge R.                 \tag{32}
\]

For instance, it suffices to increase \(R\) until the sum of the absolute
values of all lower monomials in \(P\), respectively \(P'\), is at most
half the leading monomial.  Put

\[
 B=\max\{1,\sup_{|x|\le R}|P(x)|,
             \sup_{|x|\le R}|P'(x)|\},\qquad
 c=\min\{1,\lambda/2,d\lambda/2\}.                       \tag{33}
\]

For an even integer \(K\),

\[
 \mathbb E|G|^K\ge\left(\frac K{2e}\right)^{K/2}.       \tag{34}
\]

If \(K\ge8eR^2\), the right side is at least \((2R)^K\), so

\[
 \mathbb E[|G|^K\mathbf1_{\{|G|\ge R\}}]
 \ge\frac12\mathbb E|G|^K.                              \tag{35}
\]

For even \(d\) and even \(N\), (29)--(35) give, with
\(K=d^{N+1}\),

\[
 a_{N,M_N}
 \ge\frac{\Gamma_N}{2}
 c^{m+n}
 \left(\frac n{2e}\right)^{n/2}
 \left(\frac K{2e}\right)^{K/2}                        \tag{36}
\]

as soon as \(K\ge8eR^2\).

For odd \(d\) with \(c_{d-1}=0\), use
\(\mathbb EA^{n+1}=n\mathbb EA^{n-1}\) in (30).  With

\[
 I_1=\mathbb E[P(G)^{m-1}P'(G)^n],\qquad
 I_2=\mathbb E[G P(G)^mP'(G)^{n-1}],
\]

equation (30) becomes

\[
 a_{N,M_N-1}=\Gamma_N n\mathbb EA^{n-1}(mI_1+I_2).      \tag{37}
\]

Both integrands are nonnegative on \(|G|\ge R\) by (32).  On
\(|G|<R\), their combined absolute contribution is at most

\[
 (m+R)B^{m+n}.                                          \tag{38}
\]

The first tail term alone is at least

\[
 \frac m2c^{m+n}
 \left(\frac{K_1}{2e}\right)^{K_1/2},\qquad
 K_1=d^{N+1}-d,                                         \tag{39}
\]

provided \(K_1\ge8eR^2\).  Define \(N_0(P)\) to be the least integer such
that for every \(N\ge N_0(P)\),

\[
 K_1\ge8eR^2,qquad
 \frac m4c^{m+n}
 \left(\frac{K_1}{2e}\right)^{K_1/2}
 \ge(m+R)B^{m+n}.                                      \tag{40}
\]

This is a finite, activation-defined integer.  Indeed, after division by
\(d^N\), the logarithm of the left side in the second inequality has the
term \(\frac d2N\log d\), whereas the logarithm of the right side divided
by \(d^N\) is bounded.  Equations (37)--(40) then give

\[
 a_{N,M_N-1}
 \ge\frac{\Gamma_Nmn}{4}c^{m+n}
 \left(\frac{n-1}{2e}\right)^{(n-1)/2}
 \left(\frac{K_1}{2e}\right)^{K_1/2}>0.                 \tag{41}
\]

### 6.3 Chebyshev extremality

If \(Q(h)=a_kh^k+\cdots\) is a real polynomial of exact degree \(k\), then
mapping \([0,H]\) to \([-1,1]\) and using the extremality of the Chebyshev
polynomial gives

\[
 \sup_{0\le h\le H}|Q(h)|
 \ge\frac{|a_k|H^k}{2^{2k-1}}.                          \tag{42}
\]

Indeed, the leading coefficient after the affine change is
\(a_k(H/2)^k\), while a degree-\(k\) polynomial bounded by one on
\([-1,1]\) has leading coefficient at most \(2^{k-1}\).

Take \(N=2t\).  For even \(d\), the degree retained in
\(\bar\Delta_t-\bar\kappa_th^3\) is \(k=M_{2t}\), by (29).  For odd
\(d\) with \(c_{d-1}=0\), its top coefficient vanishes and the retained degree is
\(k=M_{2t}-1\), by (37)--(41).  In both cases \(k>M_t\), so neither the
coarse output nor the cubic subtraction changes the retained coefficient.

With \(H=\rho/t\), (36) or (41), followed by (42), gives

\[
 \frac1{d^{2t}}
 \log\sup_{0\le h\le\rho/t}
 |\bar\Delta_t(h)-\bar\kappa_th^3|
 \ge(d+1)t\log d-\frac{d+1}{d-1}\log t-O_{P,\rho}(1).
                                                               \tag{43}
\]

The penalty \(2^{2k-1}\) contributes only \(O(d^{2t})\) to the logarithm;
the Gaussian factorials contribute the positive
\(t d^{2t}\) term.  The right side of (43) tends to infinity.  At the point
where the supremum is attained, \(h^s\le(\rho/t)^s\); division by any fixed
\(t^rh^s\) therefore changes (43) only by \(O(\log t)\).  This proves
(26).

### 6.4 What Chebyshev does not prove

For the full \(L=2\) network with signed lower coefficients, (42) would work
once a nonzero, quantitatively bounded top coefficient of the **width-first
full-network** polynomial were identified.  Equations (19)--(23) identify
only its maximal joint \((h,\mathrm{raw})\) sector at finite width.  They do
not show that this sector survives with a nonzero lower bound after
\(n\to\infty\), nor control cancellation with lower raw degrees in the same
\(h\)-coefficient.  Moreover, signed coefficients invalidate the frozen/full
deletion inequality (16).  Chebyshev acts in \(h\); it cannot repair either
of those two missing bridges.  Thus (26) is proved for every even degree,
and for odd degree under \(c_{d-1}=0\).  For odd degree with
\(c_{d-1}\ne0\), controlling the signed correction (30a) requires a
paired-tail asymptotic not supplied here.  The arbitrary-sign full-network
theorem remains open in every degree.

## Audit verdict

* Frozen \(h\)-degree and source-exponent recurrences: **pass**.
* Odd/even Gaussian parity and the odd-degree one-defect repair: **pass**.
* Nonnegative-coefficient (up to conjugacy) uniform no-go: **pass**, with the
  fixed-horizon polynomial width theorem and the width-first order (18).
* Full-network joint \((h,\mathrm{raw})\) degree recurrence: **pass** as a
  finite-width algebraic statement.
* Arbitrary-sign frozen scalar no-go: **pass for even \(d\), and for odd
  \(d\) with \(c_{d-1}=0\)**, by the exact coefficients, activation-tail
  bounds, and Chebyshev extremality.  The signed correction (30a) is the
  remaining general odd-degree gap.
* Strict positivity of the width-limit full leading sector: **not inferred**
  from the finite-width calculation.
* Arbitrary signed lower coefficients in the full network: **open by this
  route**; (25) rules out the naive positivity step, and Section 6 explains
  why its scalar Chebyshev repair does not supply the missing full-network
  bridge.
