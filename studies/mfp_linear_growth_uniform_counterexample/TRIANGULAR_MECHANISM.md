# A rigorous linearly-growing tail-squaring mechanism

This note isolates the mechanism without claiming that it has already been
transferred through every response edge of the full `L=2` OMFP DAG.

Let `T` be the triangular wave of period `2 pi`, normalized by

\[
T'(y)\in\{-1,1\}\quad\hbox{for a.e. }y,
\qquad |T(y)|\le \pi/2,
\]

and, for `0<eps<=1`, put

\[
\phi_\varepsilon(x)=x+\varepsilon T(x^3).
\]

It has linear growth and, away from a countable set,

\[
\phi_\varepsilon'(x)=1+3\varepsilon x^2T'(x^3),
\qquad
|\phi_\varepsilon'(x)|\ge3\varepsilon x^2-1.
\tag{1}
\]

The RMS normalization only multiplies all constants below by a fixed
positive activation-defined factor.

## Exact scalar theorem

Consider the deterministic Euler map

\[
X_{k+1}=X_k+h\phi_\varepsilon'(X_k),\qquad X_0=G\sim N(0,1),
\tag{2}
\]

and `Q_N(h)=E X_N^2`.  For every fixed `rho>0`, with `h=rho/t`,

\[
Q_{2t}(h)-Q_t(2h)\longrightarrow+\infty
\]

faster than every polynomial in `t`.

### Lower bound for the fine path

Set `a=3 eps h/4`.  If

\[
|x|\ge R_h={8\over3\varepsilon h}={2\over a},
\]

then (1) and the reverse triangle inequality give

\[
|x+h\phi_\varepsilon'(x)|
\ge h(3\varepsilon x^2-1)-|x|
\ge a|x|^2.
\tag{3}
\]

The last quantity is at least `2|x|`, so the condition propagates.  Hence,
for `X_0 in [R_h,R_h+1]`,

\[
|X_N|\ge a^{-1}(aR_h)^{2^N}=a^{-1}2^{2^N}.
\tag{4}
\]

For `R>=1`, the elementary Gaussian-density bound

\[
P\{G\in[R,R+1]\}
\ge (2\pi)^{-1/2}e^{-(R+1)^2/2}
\tag{5}
\]

therefore yields

\[
Q_{2t}(\rho/t)
\ge {2^{2^{2t+1}}\over a^2\sqrt{2\pi}}
e^{-(R_h+1)^2/2}.
\tag{6}
\]

Thus `log Q_{2t} >= 2 log(2) 4^t-O(t^2)`.

### Upper bound for the coarse path

There is an activation-defined `C>=1` such that

\[
1+|x+2h\phi_\varepsilon'(x)|
\le (1+2Ch)(1+|x|)^2.
\]

Iteration gives

\[
1+|X_t|
\le (1+2Ch)^{2^t-1}(1+|G|)^{2^t}.
\]

Using `(1+x)^m<=2^{m-1}(1+x^m)` and
`E|G|^m<=m^{m/2}` for `m>=2`,

\[
\log(1+Q_t(2\rho/t))\le C_{\varepsilon,\rho}\,t2^t.
\tag{7}
\]

Equations (6)--(7) prove the scalar assertion.

## Smooth version

Choose a smooth periodic zero-mean function `s_delta` which equals `+1`
or `-1` outside phase intervals of total relative length `delta`, and let
`T_delta` be its bounded periodic primitive.  Then

\[
\phi_{\varepsilon,\delta}(x)
=x+\varepsilon T_\delta(x^3)
\]

is `C^infty`, linearly growing, and every derivative has polynomial growth,
so every fixed Gaussian derivative moment is finite.  On trajectories whose
phases avoid the transition intervals, (3)--(7) are unchanged up to a fixed
factor.  What is *not* automatic is a lower bound on the measure of the
multi-time phase-avoidance set after the adaptive OMFP response maps.

## Full-network transfer audit

The scalar theorem is not yet a theorem about `F_N`.  In the exact OMFP
recursion the multiplier in the lower update is

\[
b_s=\chi_s+\sum_{r\le s}\sigma_{sr}H_r
       +h\sum_{r<s}K_{rs}H_r,
\]

not the constant `1`.  Moreover the terminal output is
`E[a_N phi(z_N)]`, not `E u_N^2`.  A valid transfer must prove both:

1. a positive-measure source event on which `|b_s|` stays uniformly away
   from zero through the squaring chain, with its probability quantified;
2. a sign-safe lower bound carrying the exploding lower feature Gram into
   the terminal readout, without discarding the reused-matrix response
   terms.

Neither assertion follows from the scalar inequalities.  They are the
precise remaining bridge for this candidate.
