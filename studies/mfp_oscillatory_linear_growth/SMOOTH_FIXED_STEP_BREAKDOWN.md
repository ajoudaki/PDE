# Smooth linear-growth activation whose second fixed-step gradient is not integrable

This proposition separates a literal linear-growth assertion from the
intended finite-output assertion.

### Proposition

Fix `c>0` and `0<epsilon<=1`.  Let

\[
 \Phi(x)=3+\sqrt{1+x^2}+\epsilon\sin(e^{cx}),
 \qquad \phi=\Phi/\|\Phi(G)\|_2.                 \tag{1}
\]

Then:

1. `phi` is `C^infinity`, positive, RMS-normalized, and has at most
   linear growth.
2. For every pair of integers `r,m>=0`,
   `E|phi^(r)(G)|^m<infinity`.
3. If `U` and `B` are independent nondegenerate centered Gaussians and

   \[
   U_1=U+hB\phi'(U),\qquad h\ne0,                \tag{2}
   \]

   then

   \[
   \mathbb E|\phi'(U_1)|^2=\infty.               \tag{3}
   \]

Consequently linear growth, smoothness, and all initialization Gaussian
derivative moments do not even guarantee that the second fixed-step OMFP
gradient field is square-integrable.  This is not a finite-output
super-`t^5` counterexample; it shows that fixed-schedule integrability must
be an explicit hypothesis in any such universal statement.

### Proof

The first assertion follows from `|sin(e^(cx))|<=1`.  Repeated chain rule
shows, for every `r`,

\[
 |\phi^{(r)}(x)|\le C_r(1+e^{rcx})               \tag{4}
\]

(the derivatives of `sqrt(1+x^2)` are bounded for `r>=1`).  Gaussian
exponential moments are finite, proving assertion 2.

It remains to prove (3).  Scaling by the positive RMS constant only changes
the constants below, so write

\[
 p(x)=\phi'(x)
 =s^{-1}\left\{\frac{x}{\sqrt{1+x^2}}
 +\epsilon c e^{cx}\cos(e^{cx})\right\}.         \tag{5}
\]

Assume first `h>0`; for `h<0` use `B in [-2,-1]` instead of
`B in [1,2]`.  Let `B` have variance `sigma^2>0`.  Its density has a
strictly positive minimum `b_0` on `[1,2]`.

Put `y=e^(cx)`.  On each interval where `cos y>=3/4`, and for all
sufficiently large `y`, (5) gives

\[
 p(x)\ge k_0y                                  \tag{6}
\]

for an explicit `k_0>0`.  Conditional on such a value `U=x`, set
`v_b=x+hbp(x)`.  From `(A+B)^2>=A^2/2-B^2`, (5), and the lower bound on
the Gaussian density of `B`,

\[
 \begin{aligned}
 \mathbb E_B[p(U_1)^2\mid U=x]
 &\ge k_1\int_1^2 e^{2cv_b}\cos^2(e^{cv_b})\,db-k_2\\
 &=\frac{k_1}{chp(x)}
   \int_{Y_1}^{Y_2}q\cos^2q\,dq-k_2,            \tag{7}
 \end{aligned}
\]

where `Y_j=e^(c(x+jhp(x)))`.  The elementary identity

\[
 \int_0^Yq\cos^2q\,dq
 =\frac{Y^2}{4}+\frac{Y\sin(2Y)}4
 +\frac{\cos(2Y)-1}{8}                          \tag{8}
\]

implies

\[
 \int_{Y_1}^{Y_2}q\cos^2q\,dq\ge Y_2^2/8       \tag{9}
\]

once `Y_2/Y_1=e^(chp(x))` and `Y_2` are sufficiently large.  By (6),
(7)--(9) yield

\[
 \mathbb E_B[p(U_1)^2\mid U=x]
 \ge \exp(k_3 e^{cx})                            \tag{10}
\]

for all sufficiently large `x` satisfying `cos(e^(cx))>=3/4`, after
decreasing `k_3>0`.

For large integers `n`, choose a fixed `delta>0` so that
`cos y>=3/4` on `[2pi n-delta,2pi n+delta]`, and let

\[
 I_n=\{x:e^{cx}\in[2\pi n-\delta,2\pi n+\delta]\}.
\]

The length of `I_n` is at least `k_4/n`, and throughout it
`x=(\log n+O(1))/c`.  The standard Gaussian density therefore gives

\[
 \mathbb P(U\in I_n)
 \ge \frac{k_5}{n}
 \exp\{-k_6(\log n)^2\}.                         \tag{11}
\]

Combining (10) and (11),

\[
 \mathbb E p(U_1)^2
 \ge\sum_{n\ge n_0}
 \frac{k_5}{n}
 \exp\{k_7n-k_6(\log n)^2\}=\infty.             \tag{12}
\]

This proves (3).  In the first lower-layer OMFP update, `B` is precisely a
nondegenerate Gaussian backward field.  Thus the next gradient contains a
factor `phi'(U_1)` with infinite second moment, proving the final claim.
\(\square\)

