# A superpolynomial joint width--sample lower bound for explicit frozen-top NTH

Status: internally checked theorem, 2026-10-10; complete scoped proof and
version checks are recorded in [WORST_CASE_CHECK.md](WORST_CASE_CHECK.md).
The separate dense-concentration and storage check is
[WORST_CASE_DENSE_CHECK.md](WORST_CASE_DENSE_CHECK.md); its only local
premise, the truncation-error inequality (10), is proved below and covered
by the complete check. It is not an unresolved external dependency.
This is not an independent promotion review or an established-book result.
This concerns
the original frozen-top rule in the canonical feature-learning metric, not
the native NTK parameterization of Huang--Yau. No alternative closure,
experiment, or future dense trajectory is used.

## Headline, with the growth regime exposed

For a concrete full-rank correlated binary-label dataset, a fixed admitted
activation, and fixed nonzero bounded labels, matching the actual dense-pair
worst-time test discrepancy requires explicit NTH tensor storage at least

\[
\exp\!\left[
c_\eta\log m\,
\log\frac{n}{m+\log(en)}
\right],\qquad 4\le m\le\sqrt n,
\tag{1}
\]

for sufficiently large width. In particular, for any fixed
`0<a<=1/2`, take `m=4 floor(n^a/4)` and `d=m+1`. Then (1) is

\[
\exp\big[c_{\eta,a}(\log n)^2\big].
\tag{2}
\]

This is genuinely superpolynomial in width. It is **not** exponential in
width, and it is not superpolynomial when `m,d` are fixed. It charges the
literal tensors of the specified NTH, not every possible algebraic encoding.

The activation is the identity in both hidden layers. This is admitted by
[Huang--Yau Assumption 2.1](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf), and all layers train and change
their features; however, the represented input--output functions are linear.
The theorem is not a nonlinear-activation substitute. The dataset has a
uniform positive Gram gap, both label signs, positive label variance, and
nonzero responses at every even hierarchy rank. It does not stall training.

Labels have fixed magnitude `eta`, `0<eta<=1`, independently of `n,m`.
The earlier compression theorem's additional restriction
`Y<=gamma beta^(-30L)/m` is **not** imposed here. Keeping that restriction
as `m` grows would force `eta` to shrink, change the order constant, and
invalidate this derivation of the superpolynomial conclusion (2). This is
not a proof that no such conclusion is possible under that restriction.
The NTH paper does not
impose this sample-dependent small-label restriction. This qualification
is part of the theorem, not a suppressed constant.

## Model and hard dataset

Let `m` be divisible by four, `4<=m<=sqrt(n)`, and `d=m+1`. With
orthonormal coordinate vectors `e_0,...,e_m` in `R^d`, set

\[
v_a=\frac{e_0+e_a}{\sqrt2},\qquad x_a=\sqrt d\,v_a,
\qquad
y_a=\begin{cases}
\eta,&1\le a\le3m/4,\\
-\eta,&3m/4<a\le m.
\end{cases}
\tag{3}
\]

Write `s_a=y_a/eta`, so the signs have average `1/2`. The two-hidden-layer
network and half-MSE loss are

\[
f_n(v)=\frac1n u^\top W^{(2)}W^{(1)}v,
\qquad
\mathcal L=\frac1{2m}\sum_{a=1}^m(f_n(v_a)-y_a)^2.
\tag{4}
\]

The independent initial entries of `W^(1)` and `W^(2)` have laws
`N(0,1)` and `N(0,1/n)`, and `u_0=0`. Mobilities are `(n,1,n)`.
Equivalently, in the normalized coordinates

\[
B=W^{(1)}/\sqrt n,\quad W=W^{(2)},\quad c=u/\sqrt n,
\qquad f_n(v)=c^\top WBv,
\tag{5}
\]

all three blocks have the Euclidean/Frobenius training metric. The entries
of `B_0,W_0` are independent `N(0,1/n)`.

The original NTH uses `K_1(v)=f_n(v)`, `V_a=grad f_n(v_a)` in (5),
and `K_{r+1,...a}=D K_r[V_a]`. It copies initialized tensors through
rank `q`, freezes rank `q`, and evolves lower ranks by

\[
\dot K^{(q)}_{r,a_1\ldots a_r}
=\frac1m\sum_{b=1}^m
(y_b-f_{n,q}(v_b))K^{(q)}_{r+1,a_1\ldots a_r b},
\quad r<q.
\tag{6}
\]

The residual in (6) is the closure's own residual. No dense control is
substituted.

The single declared passive query is

\[
v_*=\frac{\bar v}{\|\bar v\|_2},\qquad
\bar v=\frac1m\sum_a s_av_a,
\qquad
\|\bar v\|_2^2=\frac18+\frac1{2m}.
\tag{7}
\]

It is distinct from every training input and has no training label. Its
physical input is `sqrt(d)v_*`.

Fix the finite physical window `T=1/32768`. Let

\[
E_n(q)=\sup_{0\le t\le T}|f_n(t,v_*)-f_{n,q}(t,v_*)|,
\qquad
D_n=\sup_{0\le t\le T}\sup_{\|v\|_2=1}
 |f_n(t,v)-\widetilde f_n(t,v)|,
\tag{8}
\]

where the tilde denotes an independent dense initialization. Using the
larger, whole-sphere dense discrepancy in the denominator strengthens
the failure statement. Neither norm uses the fitted endpoint.

## Quantitative statement

There are absolute `c,C>0` and explicit positive constants depending
only on the fixed label magnitude,

\[
\begin{aligned}
\kappa_\eta&=16\left(1+\log\frac{2^{22}}\eta+\log\frac83\right),\\
A_\eta&=(8\kappa_\eta)^{-1},\\
C_\eta&=\log\frac{2^{25}e^2\kappa_\eta^2}{\eta},
\end{aligned}
\tag{9}
\]

such that, with probability at least `1-C exp(-cn)`, simultaneously
for every finite `q>=2`,

\[
E_n(q)\ge A_\eta e^{-C_\eta j},
\qquad j=2\lfloor q/2\rfloor+1.
\tag{10}
\]

The dense and all these closures exist on the window in (8). For the
independent dense pair, with probability at least
`1-1/n-C exp(-cn)`,

\[
D_n\le C\sqrt{\frac{m+\log(en)}n}.
\tag{11}
\]

Constants and onset in (10)--(11) are uniform over the displayed sample
range; `eta` is not decreased as `m` grows.

For any fixed comparison factor, the probability that *any* order with

\[
q\le \frac1{4C_\eta}
\log\frac{n}{m+\log(en)}
\tag{12}
\]

achieves that factor times `D_n` tends to zero. This is simultaneous in
orders and therefore also excludes initialization-dependent order choice
within that deterministic budget. The literal rank arrays contain at least
`m^(q-1)` entries, allowing omission of a zero frozen odd top. Equations
(12) and this count give (1), after reducing `c_eta` to absorb lower-order
integer and prefactor terms. Initialization and coefficient-generation
costs are additional, not included in this retained-array lower bound.
The nonfrozen literal arrays also contain at least `m^(q-2)` entries, so
their count has the same headline lower bound after reducing `c_eta`.
This observation does not charge the constant frozen top as learned state.

## Proof

### 1. Nondegeneracy and Gaussian initialization

The input Gram is exactly

\[
(v_a^\top v_b)_{ab}=\tfrac12(I_m+\mathbf1\mathbf1^\top).
\tag{13}
\]

Its smallest eigenvalue is `1/2`, and every subset has smallest singular
value at least `1/sqrt(2)`. Identity activations preserve this population
feature Gram at both hidden layers, so `gamma=1/2`. Label RMS is `Y=eta`
and label variance is `3 eta^2/4`.

Let `b=B_0v_*`. With probability at least `1-C exp(-cn)`,

\[
\|B_0\|_{\rm op},\|W_0\|_{\rm op}\le4,
\qquad \|b\|_2^2\ge\tfrac12,
\qquad \|W_0b\|_2^2\ge\tfrac12.
\tag{14}
\]

The first assertion follows from rectangular Gaussian operator-norm
concentration, since `d<=sqrt(n)+1<=n` for the relevant widths. For the
last two, `b` has independent `N(0,1/n)` coordinates; conditionally on `b`,
`W_0b` has independent `N(0,||b||^2/n)` coordinates. Taking both norm
ratios at least `3/4` gives the displayed lower bounds. Their failure
probabilities follow from the chi-square moment-generating function
`E exp(t sum G_i^2)=(1-2t)^(-n/2)` by exponential Markov.

If an empirical feature-gap certificate is desired as well, an independent
Gaussian matrix is nearly isometric on a fixed `d`-dimensional subspace
with failure `exp(Cd-cn)`: take a fixed `1/8` net of that sphere, use the
same chi-square tails, and pass from the net to the quadratic form.
Apply this to `B_0`, and conditionally to `W_0` on the image of `B_0`.
As `d<=sqrt(n)+1`, this gives `B_0^T W_0^T W_0 B_0 >= (9/16)I_d`
with exponentially high probability for sufficiently large `n`. Together
with (13), the initialized final-feature Gram is at least `(9/32)I_m`.
Thus the sample growth does not hide a collapsing initial Gram gap.

### 2. A nonzero omitted physical derivative at every effective order

Each odd initialized NTH rank vanishes by readout reflection. An odd
frozen top consequently gives the same output as the preceding even top.
Set `j=2 floor(q/2)+1` and form the signed mean prediction discrepancy

\[
g(t)=\frac1m\sum_a s_a\{f_n(t,v_a)-f_{n,q}(t,v_a)\}.
\]

Its derivatives below `j` vanish at zero. Differentiating (6) and the
exact dense hierarchy gives

\[
g^{(j)}(0)=\eta^j
K_{j+1}(\bar v,\ldots,\bar v)(0).
\tag{15}
\]

To check feedback, at the effective even top the first derivative
difference is zero by parity. Its second derivative contracts the first
nonzero omitted tensor against two initial residuals. Each subsequent
lower equation propagates this difference with one more initial residual.
Differentiated-residual terms contain only lower-order prediction
differences, which vanish. Every initial control is `eta s_a/m`.
The output contraction contributes the remaining `s_a/m`. Since the
prediction and its source vector fields are linear in their input,
all contractions equal evaluation at `bar v`, proving (15). No equality
of residuals at later times is assumed.

Write `lambda=||bar v||`. For unit-residual ascent of
`F=c^T W B bar v`, let `b=Bv_*` and rescale its source clock by
`tau=lambda s`. The exact source equations become

\[
\frac{db}{d\tau}=W^\top c,\qquad
\frac{dW}{d\tau}=cb^\top,\qquad
\frac{dc}{d\tau}=Wb.
\tag{16}
\]

Only in this local source calculation are primes below source derivatives.
The invariants `WW^T-cc^T=W_0W_0^T` and
`||b||^2-||c||^2=||b_0||^2` imply

\[
c''=(\|b_0\|^2 I+W_0W_0^\top)c+2\|c\|^2c,
\quad c(0)=0,\quad c'(0)=W_0b_0.
\tag{17}
\]

Diagonalize the positive semidefinite matrix and choose eigenvector signs
so the initial velocity is nonnegative coordinatewise. Its Taylor
recurrence then has only nonnegative coefficients. If `H=||W_0b_0||^2`
and `A=||b_0||^2`, comparison in that recurrence with
`u''=Au+2Hu^3`, `u(0)=0,u'(0)=1`, gives `c >= (W_0b_0)u`
coefficientwise. On (14), `A,H>=1/2`, so another coefficientwise
comparison gives `u >= 2 tan(tau/2) >= tau/(1-tau^2/12)`.
The last inequality follows from the tangent recurrence
`(2k+1)t_k=sum_{i=0}^{k-1}t_i t_{k-1-i}`, which inductively yields
`t_k>=3^(-k)`.

The standard source prediction is `c^T Wb=c^T c'`. Thus its odd
degree `j=2k+1` coefficient is at least
`H(k+1)^2 12^(-k) >= 8^(-j)`. Rescaling back to `F` multiplies its
degree-`j` derivative by `lambda^(j+1)`. By (7), `lambda>=2^(-3/2)`,
so, for every odd `j>=1`,

\[
K_{j+1}(\bar v,\ldots,\bar v)(0)
\ge j!\lambda^{j+1}8^{-j}\ge j!64^{-j}.
\tag{18}
\]

The bounds are simultaneous at all orders on (14). Equations (15)--(18)
give `g^(j)(0)>=j!(eta/64)^j`. This is not merely a frozen-feature or
second-order obstruction.

### 3. Uniform analytic control and physical-time transfer

For completeness, the dimension-free analytic argument extends to `m`
without introducing a sample-count factor. In the parameter norm
`max(||B||op,||W||op,||c||2)`, a cubic prediction has `3` variable leaves.
Each source derivative replaces one leaf by a quadratic product. After
`k` derivatives the sum has at most `(k+2)!/2` terms, each with norm
at most `s^(k+3)` on the norm-`s` ball. On (14), therefore,

\[
\max_{a,b_1,\ldots,b_k}
|K_{k+1,a b_1\ldots b_k}(0)|
\le32\,4^k(k+2)!.
\tag{19}
\]

The finite hierarchy has the exact ordered-integral representation
obtained by integrating (6) repeatedly. Its controls are
`u_b=(y_b-f_b)/m`. On the unit ball of complex prediction paths,
`sum_b|u_b|<=2`; a difference of two control lists has summed magnitude
at most the maximum prediction difference. The time simplex has volume
`|t|^k/k!`. Consequently the prediction fixed-point map on
`|t|<=R_0=1/4096` has norm at most

\[
32\sum_{k\ge1}(k+1)(k+2)(8R_0)^k<0.38
\]

and Lipschitz constant at most

\[
16\sum_{k\ge1}k(k+1)(k+2)(8R_0)^k<0.2.
\]

These sums bound every finite truncation. Hence every original finite
NTH prediction is analytic and bounded by one on this common disk.
Its own residual, including its dependence on predictions, is retained
inside the fixed-point map.

For the dense flow, within distance one of the initial state in the same
parameter norm, all block norms are at most five. Its vector field has
norm at most `3150` and derivative norm at most `3135`. Picard contraction
on the disk `R_0` therefore stays in this ball. The output integral
inequality is `max|f(t)|<=1875 integral_0^|t| (1+max|f(s)|) ds`,
giving a bound below one. This argument uses only
`(1/m)sum|y_a|<=1` and unit inputs, not a fixed sample count.

Thus `g` is analytic on a neighborhood of `|t|<=R=1/8192` and bounded
by two. The following scalar estimate converts its derivative to a real
error. If `|g^(j)(0)|>=j!rho^j`, put
`theta=rho R/8` and
`kappa=16[1+log(1/theta)+log(8/3)]`. Taylor truncation at
`N=ceil(kappa j)`, together with the endpoint Chebyshev estimate

\[
|P^{(j)}(0)|\le
\frac{2N}{j!}\left(\frac{8N^2}{R}\right)^j
\|P\|_{[0,R/4]},
\]

gives

\[
\|g\|_{[0,R/4]}\ge
\frac1{8\kappa}\left(\frac{\theta}{8e^2\kappa^2}\right)^j.
\tag{20}
\]

Here is the scalar argument, including the tail comparison. Mapping
`[0,R/4]` to `[-1,1]`, each nonconstant Chebyshev coefficient of `P`
has modulus at most `2||P||`. Also

\[
|T_k^{(j)}(-1)|
=\prod_{r=0}^{j-1}\frac{k^2-r^2}{2r+1}
\le\frac{k^{2j}}{j!}.
\]

Summing at most `N` coefficients and multiplying by the affine derivative
factor `(8/R)^j` proves the displayed endpoint inequality. For the Taylor
polynomial of `g`, Cauchy's coefficient bound gives a tail at most
`(2/3)4^(-N)` on this interval. It follows that

\[
\|g\|_{[0,R/4]}
\ge\frac{\theta^j(j!)^2}{2N^{2j+1}}-\frac23\,4^{-N}.
\]

In the present application `0<theta<1`. Put, just for this estimate,
`b=log(1/theta)`, `d_0=log(8/3)` and `D=1+b+d_0`, so
`kappa=16D`. Since `N<=2 kappa j`, `log(j!)>=j log j-j`, and
`log j<=j`,

\[
\begin{aligned}
j\log(1/\theta)+(2j+1)\log N-2\log(j!)+\log(8/3)
&\le j[b+d_0+3\log(2\kappa)+3]\\
&\le15jD<\kappa j\log4\le N\log4.
\end{aligned}
\]

For the second inequality use `log32<4` and `log D<=D-1`.
Exponentiating proves that the tail is at most
`theta^j(j!)^2/(4N^(2j+1))`. Applying the factorial and degree bounds
once more and using `j<=2^j` gives (20). Thus there is no unproved
tail or noncancellation premise in that estimate. The two factorials,
one in the assumed derivative and one in the Chebyshev inequality,
are what make `N` linear in `j`, rather than `j log j`.
Here `rho=eta/64`, so `theta=eta/2^22` and (20) is exactly (9)--(10).
Finally input linearity in the first tensor index is preserved by (6),
and therefore the query discrepancy equals `g(t)/lambda`. Since
`lambda<=1`, its magnitude is at least `|g(t)|`. This proves (10)
for the actual passive query in physical time.

### 4. Dense-pair variability with growing input dimension

Write, only within this calculation,
`Q=(1/m)sum_a v_a v_a^T` and `b=(1/m)sum_a y_av_a`.
Then `||Q||op<=1`, `||b||<=1`, and the exact physical equations are

\[
\dot B=W^\top c(b-QB^\top W^\top c)^\top,\quad
\dot W=c[B(b-QB^\top W^\top c)]^\top,\quad
\dot c=WB(b-QB^\top W^\top c).
\tag{21}
\]

The bounded-state argument above holds on `[0,T]`. For two states with
all block operator/vector norms at most five, measure their difference
by `||Delta B||F+||Delta W||F+||Delta c||2`. The predictor coefficient
vector `B^T W^T c` differs by at most `25` times this norm. The residual
vector in (21) has norm at most `126` and differs by at most `25` times
this norm. Expanding each product in (21) bounds each block's vector-field
difference by `1255` times the same norm. Gronwall gives the factor
`exp(3765t)` in the sum norm. Consequently every unit-query output is
`50 exp(4000T)`-Lipschitz in the Euclidean list of Gaussian initial
entries on the good event, uniformly in `m,d,n`.

The output coefficient vector is `250000`-Lipschitz in physical time:
each block velocity has norm at most `3150`, and differentiating the
three-factor output costs at most `3*25*3150<250000`.

Extend each fixed-query, fixed-time scalar observable from the good event
with its same Lipschitz constant. The initial entries have variance `1/n`,
so Gaussian concentration gives a two-copy discrepancy tail
`4 exp(-n s^2/(2L_T^2))` at threshold `2s`, where
`L_T=50 exp(4000T)`. This is Proposition 5.34 of
[Vershynin's notes](https://arxiv.org/pdf/1011.3027), applied to each
copy and each sign; the common extension mean cancels.

Take a deterministic `1/2` net of the unit sphere with at most `5^d`
points, and a time grid of mesh at most `1/n`. A linear functional's
sphere supremum is at most twice its maximum on that net. Setting

\[
s=L_T\sqrt{\frac{2\log(4\,5^d(\lceil nT\rceil+1)/\delta)}n}
\]

and taking a union bound therefore bounds `D_n` by
`4s+500000/n`, with failure at most `delta+C exp(-cn)`.
For `delta=1/n` and `d=m+1`, this proves (11).
No all-time Gaussian concentration or population-flow theorem is used.

### 5. Actual feature learning and the storage implication

This dataset does not remove hidden learning. Let `a=B_0 bar v`.
At time zero, the exact physical equations give

\[
\dot c(0)=\eta W_0a,\qquad
\ddot B(0)=\eta^2 W_0^\top W_0a\,\bar v^\top,
\qquad
\ddot W(0)=\eta^2 W_0a\,a^\top.
\tag{22}
\]

In particular the normalized signed-mean first feature `B(t)bar v`
has squared norm whose second derivative is
`2 eta^2 lambda^2 ||W_0a||^2`, bounded below by a positive multiple of
`eta^2` on (14), uniformly in `n,m`. The signed-mean second feature
`W(t)B(t)bar v` has squared-norm second derivative

\[
2\eta^2\left(
\|W_0a\|^2\|a\|^2+
\lambda^2\|W_0^\top W_0a\|^2\right)>0,
\tag{23}
\]

again bounded below uniformly by `c eta^2`. The common analytic state disk
also bounds the Taylor remainders of these scalar feature-Gram contractions
uniformly in `n,m`. Since their first derivatives vanish, their positive
second derivatives give a fixed sufficiently small `t_eta>0`, independent
of `n,m`, at which both changes are bounded below by a positive constant
depending only on `eta`. These are changes of
representations, not just parameter motion under a function-preserving
gauge. The query has positive initial prediction velocity
`eta ||W_0a||^2/lambda`. Equation (18) separately certifies nonzero
responses at every relevant hierarchy order.

For the ratio, put `r_n=n/(m+log(en))`, which tends to infinity uniformly
in the sample range. If (12) holds, (10) and `j<=q+1` imply
`E_n(q)>=A_eta exp(-C_eta) r_n^(-1/4)`, whereas (11) gives
`D_n<=C r_n^(-1/2)`. Their ratio diverges uniformly over all those
orders. Since a useful even top has `m^q` literal entries, or at least
`m^(q-1)` after removing a zero odd top, this proves the stated necessary
budget. Inserting `m=4 floor(n^a/4)` yields (2).

## Exact boundary of the conclusion

The theorem answers a worst-case **joint width--sample**, explicit-array
question. It does not establish `exp(cn)`, a fixed-data superpolynomial
bound, a nonlinear-activation version, or a lower bound for arbitrary
structured tensor encodings. Indeed the linear input map gives algebraic
structure that another representation may exploit. Counting the arrays
in (6) is not an information-theoretic memory argument.

It also does not contradict Huang--Yau's native fixed-order upper theorem:
their normalization, parameter mobility and random readout initialization
are different. Only their admitted activation and data conditions are
used to classify this witness, not to transfer a theorem between regimes.
Finally, retaining the older `Y=O(1/m)` small-label restriction in the
joint limit changes `C_eta=O(log m)`; the bound then need not be
superpolynomial. These distinctions must accompany every headline use.
