# A rigorous scalar instability and the exact missing `L=2` lift

## 1. Activation

Let

\[
 T(y)=\arcsin(\sin y).
\]

Then `T` is continuous, `2 pi`-periodic, `|T|<=pi/2`, and

\[
 |T'(y)|=1
\]

outside the countable set `pi/2 + pi Z`.  Fix
`0<lambda<=1/pi` and define

\[
 \Phi(x)=2+\sqrt{1+x^2}+\lambda T(x^3),\qquad
 \phi(x)=\Phi(x)/s,qquad
 s^2=\mathbb E\Phi(G)^2.
\]

The activation is RMS-normalized and there are explicit constants

\[
 m=s^{-1},\qquad M=(4+\lambda\pi/2)s^{-1},
 \qquad c=\frac{3\lambda}{2s},\qquad
 D=\frac{1+3\lambda}{s},
\]

and `R_*=(2/(3 lambda))^(1/2)` such that

\[
 m(1+|x|)\le\phi(x)\le M(1+|x|),                 \tag{1.1}
\]

and, at every differentiability point,

\[
 |\phi'(x)|\le D(1+x^2),\qquad
 |x|\ge R_*\Longrightarrow |\phi'(x)|\ge c x^2. \tag{1.2}
\]

Indeed, `sqrt(1+x^2)>=|x|`, `Phi>=1+sqrt(1+x^2)` under the
chosen restriction on `lambda`, and

\[
 \Phi'(x)=\frac{x}{\sqrt{1+x^2}}+3\lambda x^2T'(x^3).
\]

The reverse triangle inequality gives the second assertion in (1.2).
Thus `phi` is positive, linearly growing, and has a quadratically growing
first derivative almost everywhere.  Its nondifferentiability set is
countable.  Defining `phi'` arbitrarily there makes all recursions below
well defined, and a Gaussian initialization hits that set with probability
zero at every fixed finite schedule (on every phase cell the iterated map
is nonconstant and real analytic, so the preimage of a point has Lebesgue
measure zero unless the map is constant; the displayed update has a
nonzero identity term and is not constant).

## 2. Exact scalar particle model

This section concerns the one-hidden-layer particle recursion

\[
 a_{r+1}=a_r+h\phi(z_r),\qquad
 z_{r+1}=z_r+h a_r\phi'(z_r),                    \tag{2.1}
\]

with independent standard Gaussian `(a_0,z_0)`, and

\[
 F_N^{\rm sc}(h)=\mathbb E[a_N\phi(z_N)].        \tag{2.2}
\]

It is a rigorous mechanism theorem, not an identification with the
two-hidden-layer OMFP DAG.

### Theorem 2.1 (super-polynomial paired instability)

Fix `rho in (0,1/2]` and put `h_t=rho/t`.  Then

\[
 F_{2t}^{\rm sc}(h_t)-F_t^{\rm sc}(2h_t)
 \longrightarrow+\infty
\]

faster than every polynomial in `t`.  More precisely, there are explicit
activation-dependent positive constants `C_i` and an integer `t_0` such
that

\[
 F_{2t}^{\rm sc}(h_t)
 \ge
 \exp\{C_1 4^t-C_2t^2\}-C_3t,                  \tag{2.3}
\]

whereas

\[
 |F_t^{\rm sc}(2h_t)|
 \le \exp\{C_4t3^t\}.                           \tag{2.4}
\]

Consequently, subtracting any `kappa_t h_t^3` with
`log(1+|kappa_t|)=o(4^t)` still leaves a discrepancy whose quotient by
`t^5 h_t^5=rho^5` is unbounded.  In particular this applies to the exact
cubic paired Euler coefficient, which is a polynomial of degree at most
two in `t` whenever that coefficient is defined.

#### Proof

Set `beta=c/2`.  Choose

\[
 K>\max\{2/c,1/\beta,R_*\rho\}.                 \tag{2.5}
\]

For `0<h<=rho` consider

\[
 E_h=\{1\le a_0\le2,\ K/h\le z_0\le K/h+1\}.
\]

Since `phi>0`, (2.1) gives `a_r>=1` on `E_h`.  If
`|z_r|>= K/h`, then (1.2), the reverse triangle inequality, and (2.5)
give

\[
 \begin{aligned}
 |z_{r+1}|
 &\ge h a_r|\phi'(z_r)|-|z_r|\\
 &\ge hc|z_r|^2-|z_r|
 \ge \beta h|z_r|^2.                            \tag{2.6}
 \end{aligned}
\]

Moreover `beta h|z_r|>=beta K>1`, so (2.6) also preserves
`|z_{r+1}|>=K/h`.  Writing `y_r=beta h|z_r|`, induction gives

\[
 y_r\ge y_0^{2^r}\ge(\beta K)^{2^r},
\quad
 |z_r|\ge\frac{(\beta K)^{2^r}}{\beta h}.       \tag{2.7}
\]

The Gaussian density is decreasing on the positive half-line.  Hence,
with `p_a=P(1<=G<=2)>0`,

\[
 \mathbb P(E_h)
 \ge \frac{p_a}{\sqrt{2\pi}}
 \exp\left[-\frac12(K/h+1)^2\right].            \tag{2.8}
\]

On `E_h`, `a_N phi(z_N)>=m|z_N|`.  The contribution outside this
event is not automatically positive only when `a_N<0`.  Since `phi>0`,
`a_r` is increasing.  On `{a_N<0}` one has `a_r<0`,
`|a_r|<=|a_0|`, and

\[
 h\phi(z_r)\le |a_0|\quad(0\le r<N).            \tag{2.9}
\]

By the lower bound in (1.1),

\[
 |z_r|\le |a_0|/(mh)\quad(0\le r<N).            \tag{2.10}
\]

Using (1.2) in the last `z` update, and `h<=1`, yields an explicit
constant `C_-` depending only on `(m,M,D)` such that

\[
 |a_N\phi(z_N)|1_{\{a_N<0\}}
 \le \frac{C_-}{h}(1+|a_0|^4).                  \tag{2.11}
\]

For example, (2.10) gives

\[
 |z_N|
 \le\frac{|a_0|}{mh}
 +h|a_0|D\left(1+\frac{|a_0|^2}{m^2h^2}\right),
\]

and (2.11) follows from `|a_N|<=|a_0|` and the upper bound in
(1.1).  Gaussian integration makes the right side integrable, and hence

\[
 F_N^{\rm sc}(h)
 \ge
 \frac{m\,\mathbb P(E_h)}{\beta h}
 (\beta K)^{2^N}-\frac{C'_-}{h}.                 \tag{2.12}
\]

Take `N=2t` and `h=rho/t`.  The logarithm of the first term on the
right of (2.12) is at least

\[
 4^t\log(\beta K)-\frac{(K+\rho)^2}{2\rho^2}t^2
 -C\log t,                                      \tag{2.13}
\]

which proves (2.3) after decreasing the positive coefficient of `4^t`.

It remains to prove a genuinely global upper bound for the coarse
schedule.  Put `H=2h<=1` and

\[
 R_r=1+|a_r|+|z_r|.
\]

Equations (1.1), (1.2), and (2.1) give

\[
 R_{r+1}\le C_0R_r^3,\qquad
 C_0=3+M+D.                                      \tag{2.14}
\]

Therefore

\[
 R_t\le C_0^{(3^t-1)/2}R_0^{3^t}.               \tag{2.15}
\]

Also `|a_t phi(z_t)|<=M R_t^2`.  If
`q=2*3^t`, then

\[
 \mathbb E R_0^q
 \le 3^q\{1+2\mathbb E|G|^q\}
 \le3^q\{1+2q^{q/2}\}.                          \tag{2.16}
\]

The last inequality follows from
`E|G|^q=2^{q/2}Gamma((q+1)/2)/sqrt(pi)<=q^{q/2}`;
for integer `q` it also follows by comparing even Gaussian moments and
using monotonicity of `L^p` norms.  Substitution of (2.15) into (2.16)
gives

\[
 \log(1+|F_t^{\rm sc}(2h)|)\le C_4t3^t,          \tag{2.17}
\]

with, for example, any fixed `C_4` larger than
`4+2log C_0+4log 3`.  Since `4^t/(t3^t)->infinity`, (2.3)--(2.4)
prove the theorem.  All estimates are expectations of explicit
integrable envelopes, so no exchange of a width and learning-rate limit is
present.  \(\square\)

## 3. Why this is not yet the requested `L=2` counterexample

For the two-hidden-layer network, the exact finite-width top preactivation
after one simultaneous update is

\[
 z_i^{r+1}
 =\frac1{\sqrt n}\sum_jW_{ij}^r\phi(u_j^{r+1})
 +h a_i^r\phi'(z_i^r)
   \frac1n\sum_j\phi(u_j^r)\phi(u_j^{r+1}).      \tag{3.1}
\]

The last coefficient is positive for the activation above and is bounded
below by `m^2`.  If the first term in (3.1) were an independent controlled
noise, the proof of Theorem 2.1 would survive.  It is not: `u^{r+1}` uses
the backfield `(W^r)^T(a^r phi'(z^r))`, so the first term reuses the same
row and produces OMFP response terms proportional to the current and all
past top gradients.  Their signs are not controlled because `phi'`
alternates sign.  On precisely the rare trajectories used in (2.7), these
response terms can be of the same or larger algebraic size than the
positive explicit term in (3.1).

Thus the scalar comparison does not prove a lower bound for the full
`L=2` output.  A valid lift needs one of the following new statements:

1. a lower comparison showing that the aggregate reused response in
   (3.1) cannot cancel a fixed fraction of the explicit current-gradient
   term on the rare-tail event; or
2. a signed positive decomposition of the terminal expected output which
   absorbs all lower-feature responses.

Neither statement follows from Gram positivity or from
`J^*V=E[D_JV]`: the latter is an equality with no sign.  Consequently the
activation above is a rigorous counterexample to the scalar proxy and a
mechanism-preserving candidate for `L=2`, but not a proved counterexample
to the actual two-hidden-layer OMFP theorem.

## 4. Higher phase powers and the useful exponent inequality

The same construction works with `T(x^(d+1))` for any integer `d>=2`.
After changing the explicit constants, (1.2) becomes

\[
 c_d|x|^d\le|\phi_d'(x)|\le D_d(1+|x|^d)         \tag{4.1}
\]

for large `|x|`.  The fine scalar lower event then obeys

\[
 y_{r+1}\ge y_r^d,
\]

and its terminal logarithmic amplitude is `Theta(d^(2t))`.

There is a reason to prefer `d>=5` when trying to lift the mechanism to
the full two-hidden-layer network.  A direct algebraic envelope for one
full feature-ascent step has exponent

\[
 P_d=3d+4.                                       \tag{4.2}
\]

To see this, assign current polynomial-growth exponents `A,W,U,Z` to
`a,W,u,z`.  Since `phi` has degree envelope one and `phi'` degree envelope
`d`, the exact update gives

\[
\begin{aligned}
 A^+&\le\max\{A,Z\},\\
 W^+&\le\max\{W,A+dZ+U\},\\
 U^+&\le\max\{U,W+A+dZ+dU\},\\
 Z^+&\le W^++U^+.
\end{aligned}                                   \tag{4.3}
\]

If all four incoming exponents are at most `R`, then all outgoing ones
are at most `(3d+4)R`.  Thus a coarse `t`-step absolute moment envelope has
logarithmic scale at most `O(t P_d^t)`.  A fine rare-tail comparison of
the form (2.6), if proved inside the full DAG, has logarithmic scale
`Theta(d^(2t))`.  The strict separation needed to beat the coarse envelope
is

\[
 d^2>3d+4,                                      \tag{4.4}
\]

which holds exactly for integers `d>=5`.  Hence the most robust concrete
candidate is the positive RMS-normalized activation

\[
 2+\sqrt{1+x^2}+\lambda T(x^6)
\]

(`d=5`), or a higher phase power.  Equation (4.4) does not repair the
signed-response gap in Section 3; it proves that once that single lower
comparison is available, the rest of the fine/coarse growth separation is
strong enough even under a crude full-network envelope.
