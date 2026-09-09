# Campaign 2 result: exact two-input order-seven family

## Outcome

Campaign 2 did not falsify the output-kernel Stieltjes conjecture.  It gave
strict exact positivity over a continuous family, which is materially
stronger than checking one numerical initialization.

For both the equal-label channel and the normalized opposite-label channel,
the exact moment functions $\mu_0(t),\mu_1(t),\mu_2(t)$ and the ordinary
$2\times2$ Hankel determinant

$$
\Delta_1(t)=\mu_0(t)\mu_2(t)-\mu_1(t)^2
$$

are strictly positive for every $t\in[0,1]$.  Here $t=\theta^2$ and $\theta$
is the cosine similarity of two unit-RMS inputs.  Every one of these eight
inequalities has a reduced rational expression whose numerator and
denominator have strictly positive coefficients.  Thus the interval proof is
algebraic; it is not a grid test.

This remains finite-order evidence, not an all-order proof.

## Exact feature jets

The equal-label jets are

$$
F_+'(0)=63+20t+28t^2,
$$

$$
F_+^{(3)}(0)=
279680+423312t+788336t^2+143232t^3+50624t^4,
$$

$$
\begin{aligned}
F_+^{(5)}(0)={}&3759728608+10667493088t+29061262432t^2\\
&+19827259136t^3+12394753280t^4\\
&+1426164224t^5+263972352t^6,
\end{aligned}
$$

and

$$
\begin{aligned}
F_+^{(7)}(0)={}&103914510627840+436169999894016t\\
&+1578861932016128t^2+2050381315906560t^3\\
&+2015077246716928t^4+826020713986048t^5\\
&+279658081259520t^6+22982306742272t^7\\
&+2802325929984t^8.
\end{aligned}
$$

At $t=1$, all four agree exactly with the accepted one-input derivatives.

For the opposite-label channel, write $\delta=1-t$.  The exact calculation
verified the forced factorization

$$
F_-^{(2r+1)}(0;t)=\delta^{r+1}F_{h_-}^{(2r+1)}(0;t),
$$

through $r=0,1,2,3$.  The normalized nondegenerate jets are

$$
F_{h_-}'(0)=48+28t,
$$

$$
F_{h_-}^{(3)}(0)=168192+244480t+50624t^2,
$$

$$
F_{h_-}^{(5)}(0)=
1761101824+4062918656t+2218081280t^2+263972352t^3,
$$

and

$$
\begin{aligned}
F_{h_-}^{(7)}(0)={}&37826438627328+118883223224320t\\
&+109930805641216t^2+34191610462208t^3\\
&+2802325929984t^4.
\end{aligned}
$$

The certificates are constructed from $h_-$ on the closed interval.  The raw
$g_-$ Hankel signs agree for $0\le t<1$; at $t=1$, $g_-$ is the zero feature
direction and no local inverse output coordinate exists.

## Mathematical and implementation audits

The two-input geometry was retained faithfully.  The covariance
$Q=\left(\begin{smallmatrix}1&\theta\\\theta&1\end{smallmatrix}\right)$ was
used both in the initialization law and in the first-layer gradient metric.
Omitting the latter would define a different training problem.

Three validation layers were used.

1. A transparent Python implementation explicitly enumerates every labelled
   Wick pairing through order three.
2. A connected tree recursion uses quotient Wick contraction and agrees with
   the transparent route coefficient-for-coefficient for both channels.
3. The production terminal evaluator enumerates the equivalent surviving
   vertex partitions directly.  An independent hostile audit compared it
   polynomial-for-polynomial against quotient Wick on all 11,236 terminal
   trees reachable through order five; every tree agreed.

The production arithmetic is checked signed 1024-bit integer arithmetic.
Overflow would throw instead of wrapping.  All parity, input-exchange,
endpoint, normalization, forced-factor, canonical-one-input, and moment
reversion tests pass.

## Resource record and failed route

The first dense quotient-Wick order-seven plus run hit its original 20-minute
timeout.  It is recorded as an inconclusive computational route, not evidence
against either conjecture.

After that failure, an explicit amended route was authorized.  The exact
vertex-partition evaluator was frozen after the order-five base-by-base audit;
each channel retained a 4 GiB and 20-minute cap.  Results were:

| channel | recursion time | wall time | peak RSS | value states | terminal trees |
|---|---:|---:|---:|---:|---:|
| plus | 400.524 s | 6:42 | 1.498 GB | 711,818 | 617,838 |
| minus | 402.042 s | 6:44 | 1.498 GB | 711,818 | 617,838 |

Both completed with exit status zero.

## Why order nine was postponed

Order nine was not attempted.  Growth from order five to seven extrapolates
to roughly 38--53 million derivative states, 34--46 million terminal trees,
about 80--112 GB for a monolithic run, and many hours to days per channel.
The normalized whitened formulation exposes endpoint powers but does not
shrink the equal-label DAG.  A sectorized two-color compiler could control
memory, but that is a new substantial implementation campaign.  Since order
nine would add only the next shifted $2\times2$ test, its immediate
information-per-cost ratio is poor.  It is therefore postponed, not failed or
inconclusive.

## Durable artifacts

- `PROTOCOL.md`: setup, gates, resource bounds, and attempt ledger.
- `two_input_reference.py`: transparent labelled-Wick oracle.
- `two_input_connected.cpp`: checked connected production compiler.
- `postprocess.py`: exact endpoint normalization, reversion, and interval
  certificates.
- `certificates_order7.json`: exact jets and all eight rational certificates.
- `frozen/plus_order7_raw.json` and `frozen/minus_order7_raw.json`: raw exact
  production outputs.
- `provenance_order7.json`: hashes, commands, timing, and status.

