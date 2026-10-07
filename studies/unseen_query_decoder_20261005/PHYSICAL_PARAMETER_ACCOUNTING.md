# Explicit parameter costs of the physical causal program

2026-10-06. Scoped derivation for the current parameter-accounting request.
This note concerns the numerical physical source and its noise tolerances.
It is conditional on the inherited fitting and finite-query analytic-source
events. It does not make their unquantified stochastic width threshold
effective, and it is not a proof of the complete decoder's resource bound.

The physical matrix-call count can have an explicit cubic dependence on
the inverse normalized training gap. No inverse power of the label size
is needed in that count. A logarithmic Chebyshev interpolation bound and
accuracy-dependent choices of the degree and artificial noise are needed:
the old fixed choices `K = log(en)^2` and `sigma = exp(-log(en)^2)` hide
these parameter costs in their sufficient-width qualifications.

## 1. Quantities and scope

Use the network and normalized displacement sum norm of
`SHORT_CAUSAL_TRAINING_PROGRAM.md`. Set

\[
 \lambda=\gamma/m,\qquad r=\lambda^{-1}=m/\gamma,
 \qquad Y=\|y\|_2/\sqrt m>0,\qquad S=16Yr,\qquad
 \ell=\log(en).
 \tag{1}
\]

The case `Y = 0` uses the exact zero predictor and no training solver.
Retain the full inherited intersection of label allowances. In particular
the source allowance gives `S <= S_*^src <= 1`; no smaller label condition
is used here. Let

\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,1\le k\le2}\sup_{|\operatorname{Im}z|<a/2}
                     |\phi_j^{(k)}(z)|\right\},\qquad
 B=\beta^{100L}.
 \tag{2}
\]

Here `a` is the original activation strip width. The exponent 100 is a
conservative envelope, not an optimized scientific constant. All unnamed
constants below are numerical. The explicit integer `a_0 >= 1` specifies
the desired normalized prediction accuracy `n^{-a_0}`. Define

\[
 Z=(a_0+1)\ell+\log(e+B(1+r)).
 \tag{3}
\]

The inputs used are the assigned short-program proof and reconstruction,
the physical noisy-program bridge, the fitting estimates in
`GENERAL_EXPLICIT_FITTING.md`, the explicit source recurrences in
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, the finite-query localization in
`GENERAL_TRAJECTORY_LOWER_BRIDGE.md` §§2–3, and the deterministic late-time
continuation in `ANALYTIC_TAIL_EXTENSION.md` §§2–4. References in those
files to other studies are inherited interfaces; they were not fetched.

## 2. An extension with explicit bounds

The dense fitting theorem gives normalized parameter path length at most
`2Y/sqrt(lambda)`. Its original label condition and `lambda <= H^2` give

\[
 \frac{2Y}{\sqrt\lambda}
 \le \frac{\sqrt\lambda}{4H\sqrt F}\le\frac14.
 \tag{4}
\]

Thus project each learned first/hidden displacement onto its normalized
Frobenius ball of radius `1/2`. Initialized operator bounds eight then
give projected operator bounds below nine. Project the readout onto its
RMS ball of radius `SH_L`; the source bound
`2Y/sqrt(lambda) <= SH_L/8` gives strict slack. Use the protected backward
recursion in the short-program note, with the carrier clip

\[
 M=2K_{\rm src}S\sqrt\ell.
 \tag{5}
\]

One useful numerical-extension change is to project the whole residual
vector onto its Euclidean ball of radius `sqrt(m) Y`. This projection is
nonexpansive in residual RMS norm and fixes the actual residual vector.
It avoids the extra `sqrt(m)` that would result from merely bounding
every numerical residual coordinate by `sqrt(m) Y`. It requires only
the `m` computed outputs and ordinary scalar sums. The projections and
clips do not alter the actual good trajectory. Optional forward/backward
RMS projections from the noisy bridge preserve all the bounds below.

For completeness, let `H_j, P_j, k_j, tau_j, f_j` denote source (5)–(6).
If `D` is the normalized parameter difference, forward subtraction gives

\[
 \|\Delta z^j\|_{2,n}\le P_jD,\qquad
 \|\Delta h^j\|_{2,n}\le f_jD,\qquad
 |\Delta f(v)|\le (H_L+SH_Lf_L)D.
 \tag{6}
\]

For a backward-response difference use coefficients

\[
 C_L=s+tMP_L,\qquad
 C_j=s(10C_{j+1}+S\tau_{j+1})+tMP_j\quad(j<L).
 \tag{7}
\]

These follow by separating the changed carrier, changed matrix, and
changed gate. The gate term is bounded by `t M` times the preactivation
RMS difference; this is why the carrier must be clipped before the gate.
Each backward-response difference is at most `C_j D`. In a rank-one
gradient, subtract its residual, backward response, and forward feature
in turn. Since the residual projection has RMS norm at most `Y`, the
resulting field `F` has

\[
 \begin{split}
 \|F\|&\le Y\beta^{12L},\\
 \operatorname{Lip}(F)&\le
      \beta^{70L}(1+Y+YS\sqrt\ell),\\
 \operatorname{Lip}_{u}f(\cdot,v)&\le\beta^{8L}
                    \quad(\|v\|=1).
 \end{split}
 \tag{8}
\]

The complex derivative of the actual trajectory, rather than a complex
extension of the clipped field, obeys the same first bound with a
numerical factor four. This follows directly from the complex gradient
formula and residual bound `rho(z) <= 2Y`.

Here is a reproducible loose power ledger. The source recurrences and
`beta >= 10, L >= 2` imply

\[
 \begin{gathered}
 H_j,P_j\le\beta^{3L},\quad f_j\le\beta^{4L},\quad
 k_j\le\beta^{5L},\quad\tau_j\le\beta^{6L},\\
 A_*\le\beta^{7L},\quad D_*\le\beta^{8L},\quad
 H_*\le\beta^{12L},\quad D_0\le\beta^{27L},\quad
 K_{\rm src}\le\beta^{40L}.
 \end{gathered}
 \tag{9}
\]

For example, `10s <= beta^2` propagates the layer recurrences, and the
factor `L` in a layer sum is at most `beta^L`. The mixed-response
recurrences in source (24) then give `T_Q <= beta^{27L}`. Inserting
these estimates in the *finite-query* response recurrence (9) of the
trajectory-lower note gives

\[
 U_{\rm fin}(S)\le\beta^{72L}\qquad(0<S\le1).
 \tag{10}
\]

In particular this calculation does not use that note's stronger optional
small-label cap or its simplified power estimate restricted to that cap.
Equations (6)–(7), summed over the gradient blocks, give (8) with slack.

## 3. Normalize time and amplitude, and retain all parameter factors

Write `u(t)` for the learned displacement, and introduce

\[
 \tau=\lambda t,\qquad \bar u(\tau)=u(\tau/\lambda)/Y,
 \qquad \overline f(\tau,x)=f(\tau/\lambda,x)/Y.
 \tag{11}
\]

The normalized labels have RMS one. Equations (8) imply a field/complex
derivative bound `B r`, observation sensitivity at most `B`, and a valid
global field Lipschitz upper bound

\[
 \Lambda\le B[r+Yr+(Yr)^2\sqrt\ell]
             \le B(1+r)\sqrt\ell.
 \tag{12}
\]

Numerical factors are included in `B` using the slack between exponents
70 and 100. This normalization removes inverse-label factors from the
accuracy requirement. It does not remove the conditioning product:
under a time rescaling, `Lip(F) T` is unchanged.

Only the parameter trajectory and its derivative need complex-time
analyticity. The initialized first matrix, real operator bounds, and
(6) handle every later real sphere query without an analytic query net.
The finite-query source, applied just to the training set, supplies

\[
 \chi(S)=\min\{1,a/(4S^2U_{\rm fin}(S))\},\qquad
 r_\tau=\chi(S)/\sqrt\ell.
 \tag{13}
\]

By (10), `a^{-1} <= beta/16`, and `S <= 1`,

\[
 r_\tau^{-1}\le\beta^{75L}\sqrt\ell\le B\sqrt\ell.
 \tag{14}
\]

There is no dimension factor in this radius. The deterministic late-time
continuation proof applies to this finite collection of training queries:
its parameter ball, residual equation, and parameter-tail estimate use
only the same finite forward/backward bounds. This extends the parameter
trajectory and derivative with this radius near every real time.

The fitting tail divided by `Y` is at most
`(65/4) H^2 r exp(-tau/2)`. Consequently one may choose the normalized
horizon explicitly as

\[
 T=2\{a_0\log n+\log(1+66H^2r)\}\le C Z.
 \tag{15}
\]

The frozen endpoint then has normalized output-tail error at most
`n^{-a_0}/4`. A physical horizon is `r T`; it has not been dropped
from a cost estimate.

## 4. A logarithmic interpolation bound and adaptive degree

The old proof used the elementary interpolation norm `2K-1`. The following
equally elementary stronger estimate reduces the gap degree by one:

\[
 \|I_K\|_{\infty\to\infty}\le A_K:=8(1+\log K).
 \tag{16}
\]

To prove it, write `x=cos(theta)` and
`x_j=cos(theta_j)`, `theta_j=(j+1/2) pi/K`. The Lagrange cardinal
polynomial is

\[
 l_j(\cos\theta)=
 \frac{(-1)^j\sin\theta_j\cos(K\theta)}
      {K(\cos\theta-\cos\theta_j)}.
\]

Using `sin(theta_j) <= 2 sin((theta+theta_j)/2)` and
`sin(|theta-theta_j|/2) >= |theta-theta_j|/pi` gives
`|l_j| <= pi |cos(K theta)|/(K |theta-theta_j|)`.
For the closest node `j_*`, use
`|cos(K theta)| <= K |theta-theta_{j_*}|`, so its contribution is
at most `pi`. For all other nodes, their distances are at least
`(|j-j_*|-1/2) pi/K`, giving contributions at most `2/|j-j_*|`.
There are at most two nodes at each index distance. Summing the harmonic
series proves (16), including the value at a node by continuity. This
argument works for Banach-valued interpolation by the triangle inequality.

Use the positive endpoint weights already proved in the short-program
note. Choose `J=K`, choose `K` as a power of two above

\[
 C\left[1+\Lambda T+
  \log\{1+B^2r(1+T)n^{a_0}\}\right],
 \tag{17}
\]

and set the ordinary patch length to

\[
 h=\min\{(16\Lambda A_K)^{-1},r_\tau/4\}.
 \tag{18}
\]

Here `Lambda = B(1+r) sqrt(ell)` may be used as a supplied upper bound;
it is at least one. Shorten only the last patch. The node map contracts
by at most `1/16`. The true derivative's interpolation error is at most
`C B r A_K 2^{-K}`, while the `J`-iteration error is at most
`C B r h A_K 8^{-J}`. The positive endpoint recurrence from the checked
short-program proof now gives state error bounded by

\[
 CBr(1+T)A_K e^{2\Lambda T}2^{-K}.
 \tag{19}
\]

It includes interior times: their interpolation factor is multiplied by
`h Lambda`, which is at most `1/(16 A_K)`. Multiplying (19) by
observation sensitivity `B`, (17) makes it at most a chosen numerical
fraction of `n^{-a_0}`. To see that a finite numerical `C` suffices in
(17), use `A_K <= 8(1+K)` and
`K 2^{-K} <= C 2^{-K/2}`. No parameter-dependent lower bound on `n`
is used in this accuracy step.

Equations (12), (15), and (17) give

\[
 K=J\le C B(1+r) Z^{3/2},\qquad A_K\le C Z,
 \qquad
 H\le1+C T(\Lambda A_K+r_\tau^{-1}),
 \tag{20}
\]

where `H` is the number of patches. Each node field evaluation uses
`O(mL)` initialized-matrix calls. Including the initialized first-layer
row coordinates, the count of named row fields and calls is therefore

\[
 R\le C\{d+mLHK(J+1)\}
   \le C\{d+\beta^{300L}mL(1+m/\gamma)^3 Z^6\}.
 \tag{21}
\]

The logarithmic power six is rounded upwards. Since
`m(1+m/gamma)^3` contains `m^4/gamma^3`, (21) is cubic in the inverse
normalized gap and at most quartic in sample count when gamma is held
fixed. It is not cubic in every primitive parameter separately. No
inverse power of `Y` occurs. A late query adds `O(L)` calls; its given
`d` coordinates and finite input descriptions must still be counted.

## 5. Explicit matrix and scalar noise precisions

The old fixed choice `sigma = exp(-ell^2)` only beats physical amplification
when `ell^2` dominates `Lambda T`. That is a parameter-dependent threshold,
not a parameter-uniform numerical estimate.

Instead set `sigma = 2^{-b_sigma}` with

\[
 b_\sigma\ge C\left[
 1+\Lambda T+(a_0+4)\ell+
 \log\{1+B^2(1+r)^2(1+T)A_K\}\right].
 \tag{22}
\]

This has the explicit sufficient bound

\[
 b_\sigma\le C\beta^{100L}(1+m/\gamma)Z^2
 \tag{23}
\]

when the least integer meeting (22) is taken. To check the amplitude
dependence, a matrix-answer perturbation of RMS `O(sigma)` gives forward
error at most `B sigma`, normalized output error at most
`B r sigma`, and normalized, time-rescaled field error at most
`B r(1+r) sqrt(ell) sigma`. In the latter estimate the extra
`r` may arise from an output error divided by `Y`: the readout is capped
by `SH_L`, and `S/Y = 16r`. There is no `1/Y` loss. The same positive
endpoint recurrence gives the amplification `exp(2 Lambda T)`;
(22) pays for it directly. Fresh Gaussian RMS failures are still bounded
by `R exp(-c n)`, rather than by a deterministic accuracy qualification.

For a row program with `P` summaries and global scalar-history sensitivity
`Lambda_row`, the bridge's elementary perturbation recurrence gives the
explicit scalar-noise requirement

\[
 \log(\eta^{-1})\ge
 a_0\log n+\log(nP)+P\log(1+\Lambda_{\rm row})
                 +\log(1+C_{\rm out}).
 \tag{24}
\]

Here `C_out` is the explicitly counted appended-query sensitivity; if the
query has additional summaries, include them in `P`. This formula does
not assert a small degree for the full decoder. The existing compiler's
polynomial dependence on `R`, `b_sigma`, and operand-description lengths
must be substituted, including `P = O(R^2)`. A claim about the final
resource prefactor cannot stop at the physical bound (21).

## 6. Offline source generation and passive source accuracy

The normalized state construction gives physical parameter accuracy
`Y n^{-a_0}`. Training feature and protected backward-response RMS errors
are at most `B(1+sqrt(ell))` times the physical state error, with the
explicit `B = beta^{100L}` from (2).
For an arbitrary fixed passive real query, an actual backward carrier
may only have the RMS bound `S k_j`; its coordinate bound can be as large
as `sqrt(n) S k_j`. Evaluate passive source responses by their original
backward recursion at the projected numerical parameters. Direct
backward subtraction therefore gives the
conservative uniform bound

\[
 \text{source-coordinate error}
 \le B(\sqrt n+Sn)\,
                    \text{physical parameter error}.
 \tag{25}
\]

Initialized forward and transposed images obey the same bound by their
operator caps. The response recurrence adds the gate-coordinate factor
once and propagates it down the fixed number of layers; it does not
multiply a new `sqrt(n)` at every layer. Let `Q >= 2` be the number of
temporal Chebyshev samples for coefficient production. Request physical
state error

\[
 \epsilon_{\rm par}=\frac{Y\beta^{-200L}}{(Q+1)n^3}.
 \tag{25a}
\]

This is a concrete finite accuracy target. The fitting allowance gives
`Y <= H/(8 sqrt(F)) <= beta^{3L}`, while `S <= 1`. Thus (25) bounds
every sample-coordinate error by

\[
 \frac{2Y\beta^{-100L}}{(Q+1)n^2}
 \le\frac{2\beta^{-97L}}{(Q+1)n^2}
 \le\frac1{64Qn}.
 \tag{25b}
\]

The last inequality holds for all `n >= 1`, `beta >= 10`, and `L >= 2`;
no eventual-width absorption of a coefficient is involved. The DCT
constant coefficient has sample-error amplification one, and every
other coefficient has amplification at most two. Summing the `Q`
Chebyshev terms therefore gives total function error at most `1/(32n)`.
If the analytic truncation error is allocated a separate `1/(4n)`,
these numerical errors leave strict slack within source tolerance `1/n`.

Replace `Z` in (20)–(21), (23), and (26) by

\[
 Z_Q=4\ell+\log(e+B(1+r))+\log(Q+1).
 \tag{25c}
\]

Equation (17), with normalized target
`beta^{-200L}/((Q+1)n^3)`, then proves (25a) with the same parameter
powers. The term `200L log(beta)` is at most `2 log(B)` and is already
covered by a numerical multiple of `Z_Q`.

For explicit DCT arithmetic targets, every genuine source sample has
modulus at most `B sqrt(n)`. Round samples and each retained coefficient
to absolute error at most `1/(64Qn)`, and round every cosine weight to
error at most `1/(64Q B n^{3/2})`. The DCT sums and the final sum of
`Q` basis functions then add at most a numerical fraction of `1/n`.
These targets require `O(log(Q+1)+log(B)+log(en))` fractional/guard bits
for the transform, in addition to the physical integrator and primitive
precision. An assertion of `n^{-3/2}` state accuracy for all passive
backward coordinates would require a stronger carrier bound than the
current inputs supply.

During offline preprocessing dense matrices may be retained. Write
`N_F=HK(J+1)`. A full field evaluation costs
`O(m L n^2 + m d n)` arithmetic operations. Direct evaluation of every
collocation sum adds a further factor `K` to the state-coordinate work:
an honest simple bound is

\[
 W_{\rm physical}\le
 C N_F(L n^2+dn)(m+K).
 \tag{26}
\]

It has degree at most four in `1+r`, before charged arithmetic precision.
The extra `K` can be reduced to `log K`: on each state coordinate, use
the DCT to form Chebyshev coefficients of all nodal derivatives, integrate
their coefficient recurrence, and evaluate the antiderivative by another
DCT. At root nodes the degree-`K` term vanishes. This gives

\[
 W_{\rm physical}\le
 C N_F(L n^2+dn)(m+\log K)
 \tag{27}
\]

with explicitly rounded trigonometric coefficients and enough guard bits.
Formula (26) is available without relying on this fast-transform option.
The nonmaterializing implementation is specified in
[COST_INTERFACE_PANEL.md](COST_INTERFACE_PANEL.md), Section 1: use naive
cosine sums and the antiderivative recurrence per state coordinate, with
`O(K^2)` work and `O(K)` scratch. It computes the same Picard map and
does not store the `K^2` integration weights. Caching those weights would
require a separate `O(K^2)` memory term not assumed here.
The direct implementation retains `O((L n^2+dn) K)` dense stage
coordinates, including the first-layer stage arrays, in addition to its
initialized matrices and the output coefficient array.
If the latter has `Q` temporal coefficients on `p` inputs, it contains
`O(n p L Q)` coordinates. Thus a direct source-generation peak bound is
`O((L n^2+dn) K + n p L Q)` real coordinates, before bit precision.
If `p` fixed inputs are requested at `Q` additional time nodes, generating
their source fields from stored dense patch data costs at most
`C Q(L n^2+dn)(K+p)`; a naive coordinate DCT costs
`C n p L Q^2`. These are costs of generation only. Selection, input
precision, and scalar arithmetic bit costs must be added separately.

## 7. Remaining qualifications

The finite-query source explicitly retains its original deterministic
width gates, with physical radius coefficient `c = chi(S)/lambda`:

\[
 n^{-1}\le Y,\qquad
 \sqrt\ell\ge c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
 \tag{28}
\]

Its stochastic success width remains unquantified. The analytic tail
extension adds its explicit parameter-ball and carrier-tail conditions.
Equations (17), (22), and (24) do not move numerical-conditioning costs
into any of those qualifications. They also do not prove that the
inherited scientific event, or a dense-cost crossover, occurs at a
polynomial width in all problem parameters. That would require a
quantitative version of the stochastic insertion/source theorem.

Finally, a bound on analytic derivatives does not specify the bit cost of
evaluating an activation or its fixed constants. The activation/data
precision interfaces in `RECOMPUTATION_SPACE.md` remain necessary.
Normalizing labels removes inverse powers of `Y` from the arithmetic
count, but the actual input encoding length is still charged. The
full decoder's powers 245 and 722 alone give no low-degree prefactor;
the complete coefficient, conditioning, selection, and seed calculations
must be composed with (21)–(24).
