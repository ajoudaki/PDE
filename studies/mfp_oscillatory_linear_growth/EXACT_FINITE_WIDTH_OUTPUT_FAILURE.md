# Exact finite-width output failure for the smooth exponential-phase activation

## 1. Statement

Let

\[
 \Phi_c(x)=3+\sqrt{1+x^2}+\varepsilon\sin(e^{cx}),
 \qquad \phi_c=\Phi_c/s_c,
 \qquad s_c^2=\mathbb E\Phi_c(G)^2,               \tag{1.1}
\]

where `0<epsilon<=1`.  Then `phi_c` is smooth, positive,
RMS-normalized, and linearly growing.  Write `p=phi_c'`.

Consider the exact `q=1`, two-hidden-layer network at width one.  With
independent standard Gaussians `(A,W,U)`, its state is

\[
 X_r=\phi_c(U_r),\qquad Z_r=W_rX_r,
 \qquad f_r=A_r\phi_c(Z_r),                       \tag{1.2}
\]

and one simultaneous ascent step of size `h>0` is

\[
\begin{aligned}
 A_{r+1}&=A_r+h\phi_c(Z_r),\\
 W_{r+1}&=W_r+hA_rp(Z_r)X_r,\\
 U_{r+1}&=U_r+hW_rA_rp(Z_r)p(U_r).                \tag{1.3}
\end{aligned}
\]

### Theorem 1.1

For every fixed `h>0`, there is an explicit `c_*(epsilon,h)>0` such
that, for `0<c<c_*`,

\[
 \mathbb E|f_1|<\infty,
 \qquad
 \mathbb E(f_2)_+=\infty.                        \tag{1.4}
\]

Thus the earliest exact finite-output failure at width one is the second
recomputed gradient step.  This is an actual finite-width statement; it is
not a Taylor-jet or Gaussian-DAG assertion.

The same rare-path construction applies at every fixed finite width after
conditioning all variables except one connector in compact boxes.  Section
5 records precisely what is needed before promoting that observation to a
width-first assertion.

## 2. Activation bounds

There are finite positive constants `m,M,C`, uniform for `0<c<=1`, such
that

\[
 m(1+|x|)\le\phi_c(x)\le M(1+|x|),               \tag{2.1}
\]

and

\[
 |p(x)|\le C(1+e^{cx}).                           \tag{2.2}
\]

Moreover, on every interval on which `cos(e^(cx))>=3/4`, and for all
sufficiently large positive `x`,

\[
 p(x)\ge k e^{cx}                                \tag{2.3}
\]

with `k>0`.  These follow directly from

\[
 p(x)=s_c^{-1}\left\{
 \frac{x}{\sqrt{1+x^2}}+arepsilon c e^{cx}cos(e^{cx})
 \right\}.                                      \tag{2.4}
\]

The constants are explicit from `epsilon,c` and the elementary bounds
`2+sqrt(1+x^2)<=Phi_c(x)<=4+sqrt(1+x^2)`.

## 3. An oscillatory area lemma

### Lemma 3.1

Let `g` be `C^1` on a compact interval `I`, let
`J=sup_I|g'|`, and suppose the range of `g` contains `[L,R]`.  For every
nonnegative Borel function `q`,

\[
 \int_I q(g(w))\,dw
 \ge\frac1J\int_L^Rq(y)\,dy.                    \tag{3.1}
\]

If `J=0`, the assertion is used only with `L=R` and is trivial.

#### Proof

The one-dimensional area formula gives

\[
 \int_Iq(g(w))|g'(w)|\,dw
 =\int_{\mathbb R}q(y)N(g,I,y)\,dy,              \tag{3.2}
\]

where `N` is the number of preimages, counted without sign.  Every
`y` strictly between two attained values has at least one preimage by the
intermediate-value theorem.  Hence the right side of (3.2) is at least
`int_L^R q`.  The left side is at most
`J int_I q(g(w))dw`, proving (3.1).  \(\square\)

### Lemma 3.2

There are constants `a,b>0` such that, for all sufficiently large
`R>L>=0`,

\[
 \int_L^R |p(y)|\,dy
 \ge a e^{cR}-b(R-L+1).                          \tag{3.3}
\]

#### Proof

By (2.4) and `|r+s|>=|s|-|r|`,

\[
 \int_L^R|p(y)|dy
 \ge \frac{\varepsilon c}{s_c}
 \int_L^Re^{cy}|\cos(e^{cy})|dy-\frac{R-L}{s_c}.
\]

With `v=e^(cy)`, the oscillatory integral is

\[
 c^{-1}\int_{e^{cL}}^{e^{cR}}|\cos v|dv.
\]

On every interval of length `pi`, the integral of `|cos|` is two.
Consequently it is bounded below by a fixed positive multiple of
`e^(cR)-e^(cL)-1`, which gives (3.3).  \(\square\)

## 4. Width-one proof

Fix compact intervals

\[
 A\in[a_-,a_+],\qquad U\in[u_-,u_+]             \tag{4.1}
\]

with `0<a_-<a_+`, `u_->0`, and

\[
 p(U)\ge p_->0                                  \tag{4.2}
\]

throughout the second interval.  Such an interval exists because `p` is
continuous and not identically zero.  All constants below are uniform in
this rectangle, whose Gaussian probability is positive.

Put `X_0=phi_c(U)`.  For each sufficiently large integer `n`, define a
connector interval `I_n(U)` by

\[
 e^{cWX_0}\in[2\pi n-\delta,2\pi n],            \tag{4.3}
\]

where `delta in (0,pi/3)` is fixed.  On this interval
`cos(e^(cZ_0))>=cos(delta)>1/2`.  Uniformly over (4.1),

\[
 |I_n(U)|\asymp n^{-1},\qquad
 W\asymp\log n,
 \qquad p(Z_0)\asymp n.                         \tag{4.4}
\]

Here and below the comparison constants depend only on the fixed compact
rectangle and on `(c,epsilon,h)`.

Let `P_0=p(Z_0)`.  The first update is exactly

\[
 W_1=W+hAP_0X_0,qquad
 U_1=U+hWAP_0p(U),qquad
 Z_1=W_1\phi_c(U_1).                             \tag{4.5}

All quantities in (4.5) are positive for large `n`.  Equations
(2.1), (4.4), and (4.5) imply

\[
 Z_1\asymp n^2\log n.                            \tag{4.6}
\]

More is needed than its size.  As the phase in (4.3) moves from
`2pi n-delta` to `2pi n`, `cos` changes by the fixed amount
`1-cos(delta)`.  The leading product in (4.5) is a positive constant
times `W P_0^2`; all terms with fewer factors of `P_0` are lower by a
factor tending to zero.  Consequently there are `r_2>r_1>0`, independent
of `n,A,U`, such that the range of `W -> Z_1(W)` over `I_n(U)` contains

\[
 [r_1n^2\log n,r_2n^2\log n].                   \tag{4.7}
\]

For completeness, differentiation of (4.5) gives

\[
 \sup_{I_n(U)}\left|\frac{dZ_1}{dW}\right|
 \le \exp(C_1 n\log n).                         \tag{4.8}
\]

Indeed `P_0'=X_0p'(Z_0)=O(n^2)`, so
`W_1'=O(n^2)` and `U_1'=O(n^2 log n)`.  From (2.4),
`|p(U_1)|<=exp(C n log n)`, and differentiating
`Z_1=W_1 phi_c(U_1)` yields (4.8).

Apply Lemmas 3.1 and 3.2 with `g=Z_1` and `q=|p|`.  Equations
(4.7)--(4.8) give

\[
 \int_{I_n(U)}|p(Z_1(W))|dW
 \ge
 \exp\{c_1n^2\log n-C_2n\log n\}.               \tag{4.9}

The Gaussian density of `W` on `I_n(U)` is bounded below by
`exp[-C_3(log n)^2]`.  Integrating first in `W`, then over the fixed
positive-probability rectangle (4.1), proves

\[
 \mathbb E\!left[
 |p(Z_1)|1_{\{(A,U)\text{ satisfies }(4.1)\}}
 \right]=\infty.                                \tag{4.10}

Now perform the second exact update and abbreviate `P_1=p(Z_1)`:

\[
\begin{aligned}
 A_2&=A_1+h\phi_c(Z_1),\\
 W_2&=W_1+hA_1X_1P_1,\\
 U_2&=U_1+hW_1A_1p(U_1)P_1.                     \tag{4.11}
\end{aligned}

On (4.1), positivity of `phi_c` gives
`A_2>=A_1>=a_-` and `X_1>=m`.  Hence

\[
\begin{aligned}
 f_2
 &=A_2\phi_c(W_2\phi_c(U_2))\\
 &\ge a_-m^2|W_2|\\
 &\ge a_-m^2\{hm a_-|P_1|-|W_1|\}.              \tag{4.12}
\end{aligned}

The expectation of `|W_1|` on (4.1) is finite: it grows only like
`1+|W|+e^(cX_0W)`, whose Gaussian integral is finite.  Equation (4.10)
and (4.12) therefore prove

\[
 \mathbb E(f_2)_+=\infty.                        \tag{4.13}
\]

There is no cancellation inside the positive part: `phi_c>0`, and on
(4.1) both `A_1` and `A_2` are positive.  The lower bound uses `|W_2|`,
not its sign.  We do **not** assert that the negative part is finite;
therefore the audited conclusion is that `f_2` is not integrable, rather
than that its extended expectation is necessarily `+infinity`.

It remains to locate the earliest failure.  From (2.1)--(2.2), the first
state satisfies

\[
 |Z_1|\le P(A,W,U)
 \exp\{2cM|W|(1+|U|)+c|U|\},                    \tag{4.14}
\]

where `P` is a fixed polynomial (depending on `h`).  The product-normal
integral

\[
 \mathbb E e^{\alpha|W||U|}<\infty
 \quad\text{for }0\le\alpha<1                   \tag{4.15}
\]

follows by conditioning on `U` and using the Gaussian moment-generating
function, with a small extra Young inequality for the absolute values.
Thus choosing, for example,

\[
 0<c<c_*:=\min\{1,(8M)^{-1}\}                   \tag{4.16}
\]

makes the right side of (4.14), multiplied by every polynomial factor in
`A_1`, integrable.  By (2.1), `E|f_1|<infinity`.  Initialization is plainly
integrable.  This completes the proof of Theorem 1.1.  \(\square\)

## 5. Every fixed finite width fails at the second output

### Theorem 5.1

Fix any width `N>=1`, any `c,epsilon,h>0`, and use the exact normalized
two-hidden-layer network.  Then

\[
 \mathbb E(f_{2,N})_+=\infty.                    \tag{5.1}
\]

Hence `F_(2,N)(h)` is not a finite Lebesgue expectation at any fixed
width.  For small `c`, Theorem 1.1 additionally proves at `N=1` that the
preceding output is integrable.

#### Proof

Use indices `i,j in {1,...,N}` and leave only `w=W_(11)^0`
unconditioned.  Condition all readouts in `[1,2]`, all bottom
preactivations in a compact interval on which `phi>=x_->0` and
`p>=p_->0`, and every other connector in a sufficiently small positive
compact interval.  This conditioning event has positive Gaussian
probability.  It can be chosen so that all nontarget initial top
preactivations lie in a fixed interval where `p>0`.

As `w->infinity`,

\[
 z_1^0=N^{-1/2}(w\phi(u_1^0)+O(1)).              \tag{5.2}
\]

Choose disjoint intervals `I_k` on which

\[
 e^{cz_1^0}\in[2\pi k-\delta,2\pi k].           \tag{5.3}
\]

Uniformly over the compact conditioning event,

\[
 |I_k|\asymp k^{-1},\quad
 w\asymp\log k,\quad
 c_1^0=a_1^0p(z_1^0)\asymp k.                   \tag{5.4}
\]

In the first backward multiplication the target row therefore gives

\[
 b_1^0\asymp wk,qquad b_j^0\asymp k\ (j>1).     \tag{5.5}
\]

All signs in (5.5) are positive.  The first bottom and connector updates
then give

\[
 h_1^1=\phi(u_1^1)\asymp wk,quad
 h_j^1\asymp k\ (j>1),quad
 W_{1j}^1\asymp k\ (1\le j\le N).               \tag{5.6}
\]

Consequently

\[
 z_1^1=N^{-1/2}\sum_jW_{1j}^1h_j^1
 \asymp wk^2\asymp k^2\log k.                  \tag{5.7}
\]

Exactly as in (4.7), the fixed variation of the cosine across (5.3)
makes the range of `w -> z_1^1` contain

\[
 [r_1k^2\log k,r_2k^2\log k],\qquad r_2>r_1>0. \tag{5.8}
\]

The finite number of additional coordinates changes only constants in
the derivative estimate:

\[
 \sup_{I_k}|\partial_wz_1^1|
 \le\exp(C_Nk\log k).                            \tag{5.9}
\]

For rows `i>1`, the first-state top preactivation is only
`O(k log k)`: their connectors have bounded first updates, while their
bottom features have the sizes in (5.6).  Thus their first-state
derivatives are at most `exp(C_N k log k)`, exponentially smaller than
the positive target phases selected below.

Apply Lemma 3.1 with

\[
 q(y)=p(y)_+=\max\{p(y),0\}.                     \tag{5.10}
\]

The proof of Lemma 3.2, restricted to the subintervals where
`cos(e^(cy))>=1/2`, gives

\[
 \int_L^Rq(y)dy\ge a e^{cR}-b(R-L+1).           \tag{5.11}
\]

Equations (5.8)--(5.11) and the Gaussian density cost
`exp[-C_N(log k)^2]` imply

\[
 \mathbb E\!left[p(z_1^1)_+
  1_{\{\text{compact conditioning event}\}}\right]=\infty.     \tag{5.12}
\]

On these positive target phases, `c_1^1=a_1^1p(z_1^1)>0`.
Every target-row connector has the exact second update

\[
 W_{1j}^2=W_{1j}^1+\frac h{\sqrt N}c_1^1h_j^1>0.\tag{5.13}
\]

All second bottom activations are positive, irrespective of the signs of
their preactivations.  Hence

\[
 z_1^2=\frac1{\sqrt N}\sum_jW_{1j}^2h_j^2
 \ge C_Np(z_1^1)_+.                             \tag{5.14}
\]

All readouts remain positive because they start in `[1,2]` and their
increments are `h phi(z)>0`.  Therefore every row contributes
nonnegatively to `f_(2,N)`, and the target row, using (2.1), satisfies

\[
 f_{2,N}\ge C_Np(z_1^1)_+                       \tag{5.15}
\]

on the conditioned event.  Equations (5.12) and (5.15) prove (5.1).
\(\square\)

The proof uses only finitely many exact simultaneous-update equations for
each fixed `N`.  Its constants may depend on `N`; no uniform-in-width
cavity or limit exchange is used.

## 6. Width-first status and exact obstruction

Theorem 5.1 is stronger than a width-one example: the expected output is
not a finite real number at any finite width.  Thus the usual definition
`F_2(h)=lim_(N->infinity) E f_(2,N)` cannot even be initiated as a limit of
finite expectations.  This refutes the literal linear-growth-only
statement.  It does not supply a finite-output super-`t^5` counterexample.

There is nevertheless an independent width-first obstruction already in
the lower OMFP state.  The exact first lower update is

\[
 U_1=U+hB p(U),                                  \tag{6.1}
\]

where `B` is a nondegenerate Gaussian independent of `U`.  The calculation
in `SMOOTH_FIXED_STEP_BREAKDOWN.md` strengthens to

\[
 \mathbb E|p(U_1)|=\infty.                       \tag{6.2}
\]

Indeed, after conditioning on favorable initial phases and integrating
`B in [1,2]`, the change of variables `q=e^(cU_1)` gives
`int |cos q|dq`, rather than `int q cos^2(q)dq`; its upper endpoint is
still double exponential in `U`.

Suppose, for contradiction, that the step-one width-first state and the
second backward field have all finite Gram and response coefficients.  In
the exact two-step DAG,

\[
 b_1=g(U,B)+\sqrt v\,E,                          \tag{6.3}
\]

where `E` is an independent standard Gaussian and

\[
 v=K_{11}-K_{01}^2/K_{00}.                       \tag{6.4}
\]

Here `v>0`.  Equality would imply that the top gradients `c_1` and
`c_0` are proportional in `L^2`.  But `c_0=A p(Z_0)`, whereas at `A=0`
one has `c_0=0` and

\[
 c_1=h\phi_c(Z_0)p(Z_1)\ne0                     \tag{6.5}
\]

for almost every value of the remaining continuous Gaussian sources.
Continuity in `A` turns an almost-sure proportionality into the
contradiction (5.5).

For every real `g`, the centered Gaussian minimizes
`E|g+sqrt(v)E|` at `g=0`.  Hence

\[
 \mathbb E[|b_1|\mid U,B]\ge\sqrt{2v/\pi}.       \tag{6.6}
\]

Equations (5.2) and (5.6) imply

\[
 \mathbb E|b_1p(U_1)|=\infty,
 \qquad
 U_2=U_1+hb_1p(U_1),
 \qquad
 \mathbb E|U_2|=\infty.                         \tag{6.7}
\]

Since `phi_c>=m(1+|x|)`,

\[
 Q_{12}=\mathbb E[\phi_c(U_1)\phi_c(U_2)]=\infty.\tag{6.8}
\]

The explicit second connector update contributes `h Q_12 c_1` to the
next top preactivation.  Thus no finite Gaussian operator state and no
finite width-first `F_2(h)` can continue from the assumed finite step-one
state.  If instead `K`, a response coefficient, or the step-one
identification is already nonintegrable, the width-first construction
fails earlier.  Therefore the exp-phase activation has the exhaustive
dichotomy

\[
 \boxed{\text{the width-first OMFP state is undefined at step one, or }
        F_2(h)\text{ is undefined at step two}.}                 \tag{6.9}
\]

Equation (6.9) is an operator-state nonexistence result independent of the
raw finite-width positive-part divergence in Theorem 5.1.  Neither theorem
constructs a finite-output activation with a super-`t^5` effective
remainder; they instead prove that linear growth alone is not an
admissibility condition.
