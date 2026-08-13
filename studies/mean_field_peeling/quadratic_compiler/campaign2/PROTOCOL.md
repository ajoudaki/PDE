# Campaign 2: two-input natural-loss channels

## Frozen mathematical object

For two unit-RMS inputs with cosine similarity $\theta\in[-1,1]$, the
first-hidden preactivations in a fixed neuron have covariance

$$
Q(\theta)=\begin{pmatrix}1&\theta\\ \theta&1\end{pmatrix}.
$$

The same matrix is used in both places where the input geometry occurs:

1. the initialization law of $(u_j^1,u_j^2)$; and
2. the first-layer gradient metric in the $u$-hit rewrite.

For $\sigma\in\{+1,-1\}$ define

$$
g_\sigma=\frac{f_1+\sigma f_2}{2},
\qquad
D_\sigma=n\nabla g_\sigma\mathbin\cdot\nabla.
$$

These are exactly the symmetry-reduced feature-ascent directions for the
average squared loss with labels $(1,\sigma)$.  On the invariant channel
$(f_1,f_2)=(g_\sigma,\sigma g_\sigma)$, the loss is
$L_\sigma=(1-g_\sigma)^2$ and

$$
\dot g_\sigma=2(1-g_\sigma)K_\sigma(g_\sigma;\theta).
$$

The compiler internally removes fractions by using

$$
A_\sigma=f_1+\sigma f_2=2g_\sigma,
\qquad
\widetilde D_\sigma=2D_\sigma.
$$

If $J_{\sigma,k}=\mathbb E[\widetilde D_\sigma^k A_\sigma]$, the desired
feature jet is recovered exactly as

$$
F_\sigma^{(k)}(0)=\frac{J_{\sigma,k}}{2^{k+1}}.
$$

No numerical fitting is used.

## Precommitted gates

The order-seven run is accepted only if all of the following pass exactly.

- Odd feature parity: every even jet is zero.
- Input-exchange parity: every surviving answer is even in $\theta$, hence a
  polynomial in $t=\theta^2$.
- First derivatives:

  $$K_+(0;t)=63+20t+28t^2,$$

  $$K_-(0;t)=48-20t-28t^2=4(1-t)(7t+12).$$

- At $t=1$, the plus channel agrees with the accepted one-input derivatives
  through every computed order.
- For order $2r+1$, the minus-channel polynomial is divisible by
  $(1-t)^{r+1}$.
- A transparent exhaustive-Wick implementation and the connected checked
  implementation agree through at least order three.
- All arithmetic in the production calculation is checked signed integer
  arithmetic.  Overflow or a resource-limit failure makes the result
  inconclusive, never negative evidence.

After a valid order-seven jet, exact reversion constructs
$\mu_0,\mu_1,\mu_2$ and

$$
\Delta_1=\mu_0\mu_2-\mu_1^2.
$$

The sign test is over the complete admissible interval $t\in[0,1]$ using
exact factorization and/or Sturm root isolation.  Point sampling is not a
certificate.

For the minus channel, the endpoint must be normalized before this test.  If
$\delta=1-t$, define the nondegenerate feature jet $h_-$ by

$$
F_-^{(2r+1)}(0;t)=\delta^{r+1}F_{h_-}^{(2r+1)}(0;t).
$$

The moment and Hankel certificates are constructed from $h_-$ on the closed
interval.  The raw $g_-$ moments have the same signs for $0\le t<1$, while
$t=1$ is the degenerate zero feature direction and has no locally invertible
output coordinate.

## Frozen resource boundary

- Reference route: orders $0$ through $3$ only.
- Production target: both channels through order $7$.
- Per-process memory cap: 4 GiB.
- Wall-clock cap: 20 minutes for the combined order-seven production run.
- Order $9$ is not started until the order-seven gate is reported and a new
  bound is explicitly authorized.

These were the original precommitments for the first dense route.  The
post-timeout amended route and its separate per-channel caps are recorded
below; they must not be retroactively described as the original precommitment.

## Attempt ledger

The first production attempt used the quotient-Wick terminal contraction.  It
hit the frozen 20-minute timeout during plus-channel order seven (exit status
124).  This attempt is classified **inconclusive**.  A separate plus-channel
order-five run completed in 2.35 seconds using 25.8 MB and was preserved.

An exact bivariate vertex-partition contraction was then added.  It enumerates
the same leading-width Wick quotients directly.  Before any second order-seven
attempt, it was required to reproduce every coefficient of both channels
through order three and every coefficient of the independently completed plus
order-five polynomial.  It passed those gates; plus order five took 0.73
seconds using 25.5 MB.  Any second order-seven attempt retains the same 4 GiB
and 20-minute resource caps **per channel**.  The plus and minus calculations
are separate processes; a channel that times out is inconclusive even if the
other finishes.  No third production route or enlarged cap is attempted if
this accelerated route times out.
