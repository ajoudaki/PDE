# An explicit rate in the maintained H3 order

Internal theoretical derivation, 2026-09-20. Scientific inputs are the complete
`RESULT.md`, `ROUTE_DICTIONARY.md`, `ROUTE_DYNAMICS.md`, the maintained
C.4.7.10.B dictionary, and the supervising author's supplied inverse-gate
lemma, proved again below. No experiments or maintained-file edits were made.

Write

\[
 \mathcal E(N)=\sup_{t\ge0,\ u\in S^1}|f_N(t,u)-f(t,u)|.
\]

Here `N` is exactly the maintained order: degree-`N` core, bounded word codes
through `N`, ridge `1/[1024(N+1)^2]`, and the unchanged autonomous equations.
The predictions are compared at the same physical time. All logarithms below
are base two.

The existing recursive proof implies an inverse triple-logarithmic rate.
A sharper elementary estimate for its inverse gate improves the conclusion to

\[
 \mathcal E(N)\le
 \frac{2^{433448}}{(\log_2\log_2 N)^{1/28}}
 \quad\text{if}\quad
 \log_2\log_2\log_2 N\ge28\cdot433448.                 \tag{1}
\]

In particular, the unchanged H3 closure has the named asymptotic rate
`O((log log N)^(-1/28))`, uniformly through all training and on the whole
circle, including the trained endpoints. This is an upper bound, not a
lower bound or a practical estimate. The enormous constant and threshold
are explicitly inherited from conservative proof witnesses.

## 1. A polynomial bound for the inverse gate

As in the dictionary proof, let

\[
 F(z)=z/2+\sinh(2z)/4,\qquad J(g,V)=F^{-1}(F(g)+V).
\]

Since `F'=cosh^2>=1`, its inverse is globally defined. Put
`a(z)=cosh^2(F^{-1}(z))`. Direct differentiation gives

\[
 a'(z)=2\tanh(F^{-1}(z)),\qquad |a'(z)|\le2.
\]

Consequently

\[
 \partial_gJ(g,V)
 =\frac{\cosh^2g}{\cosh^2J(g,V)}
 \le1+\frac{2|V|}{\cosh^2J(g,V)}\le1+2|V|.          \tag{2}
\]

Also `|partial_V J|<=1`. For `|u_1|,|u_2|<=1`, the function
`Psi_u(g_1,g_2,V)=tanh(u_1 J(g_1,V)+u_2 g_2)` therefore has coordinate
derivative bounds `1+2R,1,1` on the box `[-R,R]^3`.

Use the same clamped map `r_R` and tensor Bernstein compiler as Section 2
of `ROUTE_DICTIONARY.md`. Since `Lip(r_R)<4R` and `R>=1`, the resulting
function on `[-1,1]^3` is Lipschitz for the sum metric with constant at most
`12R^2`. The Bernstein fluctuation estimate in that proof now gives error
at most `36R^2/sqrt(n)`. Thus replace only its auxiliary degree by

\[
 n=\left(\frac{2^{10}R^2}{\lambda}\right)^2
   =2^{84}\lambda^{-6},\qquad R=2^{16}/\lambda.        \tag{3}
\]

Then `36R^2/sqrt(n)=36 lambda/1024<lambda/16`.
The exceptional-set error, rational sample error, global output bound,
node count `P=100(n+1)^4`, and rational-size bound
`Acoef=2^(3n+10) R/lambda^2` in the original compiler are unchanged.
No additional distributional or tail hypothesis is used. In particular,
the smaller degree satisfies every requirement used by the rest of that
proof; the former factor exponential in `R` was only its derivative bound.

Let `Nhat_k` denote its integer threshold after substitution (3), with all
other recursions literally unchanged. This is a new sufficient threshold
for the same closure, not a new closure index. The original source estimate
and physical-time composition consequently give

\[
 N\ge\widehat P_j:=\widehat N_{j+62004}
 \quad\Longrightarrow\quad \mathcal E(N)\le2^{-j},
 \qquad j\ge1.                                        \tag{4}
\]

This uses the same `rho<=13*2^(-k)` source production and the same fixed
all-time stability constant as `RESULT.md`. Nothing in those arguments
requires the earlier, larger Bernstein degree.

## 2. What the two squaring recursions actually cost

This calculation applies both to the original and to the improved degree.
Set `L=k+400000`, so `lambda=2^(-L)`, and abbreviate `A=Acoef`.
Then

\[
 \log_2 A=3n+3L+26\le W,\qquad k+10\le W,\qquad W\ge8. \tag{5}
\]

Indeed both degrees satisfy `n>=L`, while the displayed definition of `W`
in the dictionary proof gives `W>=10000(n+1)^4`.

For its moment recursion write `e_r=log_2 E_r`. Its multiplier has logarithm
at most `2W+4`, and `e_0<=W`. Since `log_2(x+1)<=log_2 x+1` for `x>=1`,

\[
 2e_r\le e_{r+1}\le2e_r+2W+6,
 \qquad 2^W\le e_W\le4W2^W.                           \tag{6}
\]

The latter upper bound follows by summing the geometric series:
`e_W<=2^W(e_0+2W+6)<=2^W(3W+6)<=4W2^W`.

As `E_W>=A`, the saturation radius is the final coefficient bound:
`Afinal=Rb=2^(k+10) E_W^2`. Its logarithm is at most `9W2^W`.
Write `m_r=log_2 M_r` for the code recursion. Its initial value and update
satisfy

\[
 4e_W\le m_0\le18W2^W+6,
 \qquad 2m_r\le m_{r+1}\le2m_r+8.
\]

Also `M_0>=2^(k+10)`, so `N_k=M_(4W)` in either recipe. Iterating gives

\[
 4\,2^{5W}\le\log_2 N_k\le20W2^{5W},
\]
\[
 5W+2\le\log_2\log_2 N_k
       \le5W+\log_2(20W)\le8W.                         \tag{7}
\]

The same statements hold with hats. In particular the exact tower count
is governed by `log log N=5W+O(log W)`. Iterating a squaring operation `W`
times does not create a tower of height `W`.

## 3. Explicit inversion after the gate improvement

Keep the actual proof input-grid size `m=2^(k+20)`. From (3),

\[
 \begin{split}
 P+1&\le1616n^4,\\
 Jstep+1&\le7/\lambda,\qquad m+1\le2m,\\
 W&\le100\cdot49\cdot4\cdot1616\ n^4m^2\lambda^{-2}\\
  &<2^{25}\,2^{336}\lambda^{-24}\,2^{2k+40}\lambda^{-2}
   =2^{28k+10400401}.
 \end{split}                                           \tag{8}
\]

Thus (7), with `k=j+62004`, yields

\[
 \log_2\log_2\widehat P_j
 \le2^{28j+12136516}=2^{28(j+433447)}.                   \tag{9}
\]

For `N` in (1), choose

\[
 j=\left\lfloor
     \frac{\log_2\log_2\log_2 N}{28}-433447
   \right\rfloor\ge1.
\]

Equation (9) implies `N>=Phat_j`. Equation (4), and the elementary inequality
`floor(x)>x-1`, then give (1). This works at every sufficiently large order,
without assuming monotonicity of the actual errors.

For the exact asymptotic count, the factors in `W` also give

\[
 \widehat W_k\sim360000\,2^{10400376}\,2^{28k},\qquad
 \log_2\log_2\widehat N_k
     \sim1800000\,2^{10400376}\,2^{28k}.                \tag{10}
\]

For example, the first constant follows from
`100*(6/lambda)^2*m^2*100*n^4`, with the lower-order `+1` terms tending to
one in relative size. Equation (7) then proves the second equivalence.
Hence the sufficient order has three exponentials in the accuracy index
`k`, or two exponentials in `epsilon^(-28)` when the error is `epsilon`.
The staircase upper bound itself is of order
`(log log N)^(-1/28)`; (10) does not give a matching lower bound for the
prediction error. The exponent `28` comes from this particular witness
count: `24` from the Bernstein compiler, `2` from the Euler-step bound,
and `2` from the passive input grid. It is not a proved optimal exponent.

## 4. The original threshold and actual retained dimensions

For comparison, keep the degree printed in the original route. Its exact
logarithm is

\[
 D:=\log_2 n=2^{L+19}+4L+48.
\]

Substitution into the definition of `W` gives

\[
 \log_2 W
 =2^{k+400021}+20k+7200232+2\log_2 600+o(1).
\]

Using (7) once more,

\[
 \log_2\log_2\log_2 N_k\sim2^{k+400021},\qquad
 \log_2^{\circ4}N_k=k+400021+o(1).                     \tag{11}
\]

Thus the originally printed recipe alone gives
`E(N)=O(1/(log log log N))`. Its tower height is four in `k`, or three in
`epsilon^(-1)`. The gate improvement removes one exponential level.
These statements classify the proof's thresholds, not intrinsic hardness
of the population dynamics or optimality of the maintained index.

Let `r_1(N),r_2(N)` be the actual retained raw feature counts. The maintained
dictionary, with its literal-syntax rule, gives

\[
 \binom{N+4}{4}\le r_1(N)\le\binom{N+4}{4}+N+1,
 \qquad
 \binom{N+2}{2}\le r_2(N)\le\binom{N+2}{2}+N+1.
\]

There are at most `N+1` appended codes even when both populations are counted
together. In particular,

\[
 r_1+r_2\sim N^4/24,\qquad r_1r_2\sim N^6/48.
\]

If `p` means polynomial order, it is `N`. If it means total retained raw
features, it is asymptotic to `N^4/24`; if it means coefficient-matrix entries,
it is asymptotic to `N^6/48`. The rate class in (1) is unchanged under either
polynomial conversion, since `log log p=log log N+O(1)`.
Raw feature count is not necessarily functional rank: syntactically distinct
copies of the same function are intentionally retained. None of these counts
includes the separate numerical discretization of the population measures.

The witnesses themselves have `O(epsilon^(-28))` causal grammar nodes after
the gate improvement, so they exhibit polynomial approximation complexity
when exact rational coefficients are counted at unit cost. This is useful
structural information, but it does not give polynomial runtime for H3:
its actual order includes the full numeric prefix and the entire core.
Moreover the particular saturation coefficient above already uses between
`2^(W+1)` and `9W2^W` binary digits up to integer-rounding constants.
A direct stored DAG has total bit cost at most `O(W^2 2^W)` and at least
`2^W`; expectations are a further cost not bounded by this node count.
Replacing H3 by a dictionary consisting only of the selected witnesses
would require stating and checking a different hierarchy. It is not used
in (1).

Only the exact population truncation axis is controlled here. Numerical
quadrature, arithmetic, time integration, and finite neural width retain
the separate status stated in `RESULT.md`. The result remains an internally
derived study result, without promotion or a sharpness claim.
