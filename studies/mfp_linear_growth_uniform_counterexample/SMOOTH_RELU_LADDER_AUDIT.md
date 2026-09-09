# Independent audit of the smooth ReLU-like ladder

## Verdict

`SMOOTH_RELU_LADDER.md` correctly inherits the full-`L=2` compact insertion
theorem.  Its normalization, closeness, regularity, and growth quantifiers
close without any hard-ReLU limit.  The result is

\[
 \mathcal B_{\widetilde\phi}(N,\rho)
 \ge {3\over5}N^{N+6}-2\ge N^N,
 \qquad N\ge2.
\]

It therefore gives a genuine smooth `Omega(N^N)` counterexample arbitrarily
close in weighted `C^1` to a fixed smooth ReLU or leaky-ReLU base.

## 1. Base and affine-tail check

The cutoff in (1.1) satisfies `S(-x)=1-S(x)`.  Therefore

\[
 \int_{-1}^1S(x)dx=1.
\]

For `x<=-tau`, the integral in (1.2) is zero, so `b=lambda x`.  For
`x>=tau`, changing variables gives

\[
 \int_{-\infty}^xS(y/\tau)dy
 =\tau\int_{-1}^1S(r)dr+x-\tau=x,
\]

and hence `b=x`.  Every future compact transition is placed in this exact
right affine tail.  Thus the arbitrary-old-ladder insertion lemma applies
literally; no asymptotically-affine approximation is being substituted for
its hypothesis.

## 2. Smoothness and slope check

Both `p` and its primitive `P` vanish with all derivatives at their compact
support boundary.  Disjoint supports tending to infinity make (2.1) locally
finite.  Hence every derivative exists and is continuous at every finite
point.

At most one derivative bump is active at a point.  Under (2.3), on a bump
support

\[
 \Phi'\ge1-\delta_m\|p\|_\infty\ge\tfrac12;
\]

off all bump supports, `Phi'=b' in [lambda,1]`.  Thus the slope is globally
bounded and nonnegative, and for `lambda>0` is bounded away from zero.  The
function perturbation is bounded because its supports are disjoint and
`sup delta_m w_m<infinity`; consequently `Phi` has at most linear growth.

## 3. RMS normalization and weighted `C^1` distance

Let

\[
 B=\|b(G)\|_2>0,
 \quad K=\|1+|G|\|_2,
 \quad \eta=d_1(\Phi,b).
\]

Then

\[
 \|\Phi(G)-b(G)\|_2\le K\eta,
 \qquad |\|\Phi(G)\|_2-B|\le K\eta.
\]

If `K eta<=B/2`, writing `N=||Phi(G)||_2` gives `N>=B/2` and

\[
 \left|{1\over N}-{1\over B}\right|
 \le {2K\eta\over B^2}.
\]

The triangle inequality in the two components of `d_1` now yields

\[
 d_1(\Phi/N,b/B)
 \le {2\eta\over B}
 +{2K\eta\over B^2}d_1(b,0).
\]

This is exactly (2.6).  Since the insertion lemma permits every new
amplitude below an arbitrary positive ceiling, the recursive ceilings may
make `eta` smaller than both `B/(2K)` and
`epsilon/C_(lambda,tau)`.  RMS normalization therefore does not spoil the
claimed closeness.

## 4. Quantifier and termination check

At stage `N`, only finitely many obligations exist:

1. the target fifth coefficient at `t=N`;
2. the global amplitude and `d_1` ceiling;
3. finitely many tail budgets belonging to earlier selected rates;
4. the next item in an enumeration of finite schedules and compact rational
   step intervals used to secure every fixed-schedule width limit.

The insertion lemma first chooses `X_N` and then `delta_N` below the minimum
of these finitely many positive ceilings.  It finally sets
`w_N=delta_N sqrt(gamma(X_N))`.  Thus every stage terminates.  Geometric
amplitude ceilings make the final tail satisfy every old budget.

The exact two-rate minimax inequality loses only the factor `3/5` and the
fixed normalized error two, giving the first inequality above.  For `N>=2`,

\[
 {3\over5}N^{N+6}-2
 =N^N\left({3\over5}N^6-{2\over N^N}\right)
 \ge N^N,
\]

because the bracket is increasing from a value greater than one at `N=2`.
This proves `Omega(N^N)` with constant one, rather than merely along an
unspecified subsequence.

## 5. Claim boundary

The proof relies on higher derivatives becoming arbitrarily large on remote,
narrow intervals.  It does not classify ordinary softplus, the unperturbed
compact smoothing (1.2), or any class with a fixed global higher-derivative
envelope.  It also does not use the still-open hard-ReLU width-first bridge.

