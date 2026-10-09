# A small retained numerical program through loss-based stopping

This note proves two deterministic additions to the authorized finite-panel
compression theorem: an Euler compiler that does not retain its history,
and a stopping comparison that does not divide by the stopping loss.
It imports, rather than re-proves, the neural source/selection theorem.
Its resource convention is retained real scalar coordinates and arithmetic
workspace. It is not a polynomial bit-complexity or total-work theorem.

## 1. Dense flow and the imported compression

There are `m` training examples and `p` passive query inputs, all supplied
at initialization; query labels are never used. The dense reference is the
canonical width `n`, depth `L`, Gaussian zero-readout nonlinear gradient
flow, with the same strip-analytic activations, positive feature-Gram gap
`gamma`, and full original label allowance. Activation values need not be
bounded. Write

\[
Y=\|y\|_2/\sqrt m>0,\qquad \lambda=\gamma/m,\qquad
\rho(t)=\left[\frac1m\sum_{a=1}^m(f_n(t,x_a)-y_a)^2\right]^{1/2}.
\]

The zero-label predictor is stationary and can be returned exactly. In
the nonzero-label case the imported real fitting argument gives

\[
-\rho'(t)\ge\frac\lambda2\rho(t).
\tag{1}
\]

Here is the other dense estimate needed below, with its normalization
made explicit. For each panel input let `g(t,x)` be the gradient of its
prediction in mobility-whitened dense parameter coordinates. On the
imported event its squared norm is at most

\[
\mathcal K=H_L^2+
 (16Y/\lambda)^2\left[\tau_1^2+
                 \sum_{j=2}^L\tau_j^2 H_{j-1}^2\right]
\le\beta^{14L}.
\tag{2}
\]

The source coefficients `H_j,tau_j` are exactly those of
`adaptive_clock_compression_20261008/FLARING_ROUTE.md` (F.4); they are
local proof quantities, not additional input parameters. The readout,
first-layer, and hidden-layer gradient blocks respectively contribute
the three terms displayed in (2). The operator taking normalized
training residuals to their gradient combination also has norm at most
`sqrt(Kcal)`, by the sum of squared column norms. Therefore the exact
gradient-flow identity gives, for every declared query,

\[
|\partial_t f_n(t,x)|
=\left|\frac2m\sum_a(f_n(t,x_a)-y_a)
                      \langle g(t,x),g(t,x_a)\rangle\right|
\le2\mathcal K\rho(t).
\tag{3}
\]

Equations (1) and (3), not a lower bound on terminal variance, are the
only dense ingredients in the new stopping lemma.

The imported enlarged-domain source theorem supplies an autonomous
compressed flow with arbitrarily prescribed source tolerance. At panel
prediction target `Y/n` its total retained inventory is

\[
\begin{split}
C\beta^{CL}(m+p)^2\bigg[
 &\left(\frac{Ym}{\gamma}\right)^4[\log(en)]^3\\
 &+\left(\frac m\gamma\right)^2[\log(en)]^2
             [\log(e+\log(en))]^2\bigg]
 +C(m+p)d+D_{\rm alg}.
\end{split}
\tag{4}
\]

It includes current matrices/readouts/deficits, fixed mixers and metrics,
input/panel data, and ordinary evaluation buffers. `D_alg` separately
charges the scalar activation evaluator and its workspace. See the exact
rank and inventory in that study's RESULT (B), and its full proof in
FLARING_ROUTE and scoped check in FLARING_CHECK. The construction uses
finite initialization jets; dense weights, source coefficient arrays,
jet arrays and selection scratch are discarded before execution.

Multiplying the requested prediction tolerance by any fixed positive
factor depending on the problem changes only the eventual polynomial
degree gate and sufficient width threshold. More generally replacing
`Y/n` by `c Y/n^a`, with fixed `a>0,c>0`, still gives (4), with a constant
depending on `a` and an eventual threshold depending on `c`. This follows
directly from the inherited degree prescription
`ceil(log_2(8 M_0 sqrt(n)/eta))`: its logarithm changes by
`(a-1)log_2(n)+log_2(1/c)`. The temporal-panel count is unchanged after
choosing the corresponding fixed multiple of the logarithmic horizon.
For the stopping application below, only a fixed factor change at `a=1`
is used, so even that horizon adjustment is unnecessary.

All asymptotics are for a fixed admissible problem and fixed confidence.
The sufficient width threshold can depend on every such parameter and
has not been proved polynomial. This is not a uniform joint-growth
theorem in `m,d,L,gamma^{-1}`. The displayed prefactor retains their
dependence; no label inequality is used to cancel a displayed power of
`Y` or `m/gamma`.

## 2. Stopping transfer without inverse-loss amplification

Here is a general deterministic lemma. Suppose a prediction path `f`
and positive training RMS `rho` satisfy

\[
-\rho'\ge\lambda\rho/2,\qquad |\partial_t f(t,x)|\le B\rho(t).
\tag{5}
\]

For any two finite times `s,t`, direct integration, with their order
reversed if necessary, gives

\[
|f(t,x)-f(s,x)|
\le B\int_{\min(s,t)}^{\max(s,t)}\rho(u)\,du
\le\frac{2B}{\lambda}|\rho(t)-\rho(s)|.
\tag{6}
\]

In particular it is not necessary to estimate a time displacement by
dividing a loss error by a small terminal loss.

Choose `0<a<rho(0)`, and let the dense reference stop when its RMS
first equals `a`. Suppose a numerical predictor evaluated at times
`k h` has maximum panel error at most `e>0` from that reference at the
same physical time. Its training RMS differs from `rho(kh)` by at most
`e`: this is the reverse triangle inequality on the normalized residual
vector. Stop the numerical predictor at its first grid RMS at most `a`.
If its last RMS decrement is at most `e`, its stopping RMS lies in
`(a-e,a]`. Thus at its physical stopping time

\[
|\rho(kh)-a|\le2e.
\]

The triangle inequality and (6) prove

\[
\max_{x\text{ in panel}}
|f_{\rm num}(kh,x)-f_n(\tau_a,x)|
\le e\left(1+\frac{4B}{\lambda}\right),
\qquad \rho(\tau_a)=a.
\tag{7}
\]

For the dense neural path, (3) permits `B=2 Kcal`. The coefficient in
(7) is therefore at most `1+8 beta^{14L}m/gamma`. There is no factor
`1/a` or `1/a^2`. In words, slow motion near the stopping threshold
compensates for slow crossing of that threshold.

At a trivial initial stop use `tau_a=inf{t>=0:rho(t)<=a}`. If both
systems start below `a`, the error is just the initial prediction error.
If only the numerical system starts below, (6) with the initial RMS
error gives `e(1+2B/lambda)`. Exact zero-loss stopping is not a finite
crossing and must instead be handled by the fitted-tail theorem.

## 3. Finite Euler realization with a reusable buffer

This paragraph is an exact-real arithmetic statement, with activation
value/derivative evaluation counted explicitly. A finite-bit version
needs the additional precision accounting in Section 5.

Let `u'=F(u)` be the finite compressed ODE, including its deficit
coordinates. The initialized training feature Gram is positive, and
the inherited real fitting proof keeps its eigenvalues bounded away
from zero with a strict margin along the whole trajectory. Fix a finite
horizon `T`. The trajectory lies in a compact subset of the smooth
domain of `F`; the effective readout and output map are smooth there.
Choose a positive-radius neighborhood of the trajectory lying within
that domain. On a slightly larger neighborhood, let `M` bound the field
norm, `K` its derivative norm, and `C_out` the maximum panel-output
derivative norm. These are finite constants. In numerical use the
selected metric condition numbers and all field/output derivative
bounds must be included in these constants; they are not silently set
equal to the activation envelope.

For `K>0`, exact Euler started at the same state satisfies on this
neighborhood

\[
\|u_k-u(kh)\|\le\frac{Mh}{2}\big(e^{Kkh}-1\big).
\tag{8}
\]

Indeed the one-step truncation error is at most `K M h^2/2` and
the recurrence is `e_{k+1}<=(1+Kh)e_k+KMh^2/2`. Summing its geometric
series proves (8). For `K=0` the field is constant on the relevant
neighborhood, so Euler is exact until exit. Choose `h` so that the
right side of (8) stays below both half the neighborhood radius and
the desired output tolerance divided by `C_out`. Induction at the
first possible exit then closes the use of the local bounds: the
segment between the exact and numerical state is inside the larger
neighborhood of the exact state, where the derivative bound holds.
The exact one-step segment is on the exact trajectory. Thus no global
convexity of the entire trajectory tube is assumed.

The deficit update is computed simultaneously with all other blocks;
the current state is not overwritten before its derivative has been
evaluated. Its normalized Euclidean step length bounds the change in
its RMS norm. A finite bound `M_c` on this deficit derivative gives
the sufficient additional condition `h M_c<=e` for the last-decrement
condition of Section 2. The exact identity between the compressed
training predictor and `y-c` holds algebraically at every numerical
state in the positive-Gram domain, not just on the ODE solution.

The compressed exact RMS is at most `Y exp(-lambda t/2)`. To stop
at `a>0`, take

\[
T=\frac2\lambda\log\frac{4Y}{a}.
\tag{9}
\]

Use `h=T/N` for a sufficiently large integer `N`; this avoids a final
grid-rounding ambiguity. If the numerical training error from the
compressed flow is at most `a/4`, its RMS at `T` is at most `a/2`.
It must therefore have stopped by that grid point. No monotonicity
claim for a too-large Euler step is needed. The first-crossing
argument and decrement bound suffice.

Consequently some finite `N` gives every claimed positive tolerance.
This proof does not bound `N` by a polynomial in `n`. For this particular
optimizer the fitting certificates also provide a way to obtain field
bounds without knowing the future trajectory. Retained metrics are
positive definite and finite dimensional. Their positive minimum
eigenvalues convert the proved weighted parameter caps and path-length
caps into finite Euclidean parameter bounds. Enlarge these bounds and
use the domain where the training Gram is at least `lambda/8`; the
exact flow has gap at least `lambda/4`. On that bounded region, layerwise
forward/backward differentiation, the inverse identity
`d(Q^{-1})=-Q^{-1}(dQ)Q^{-1}`, and `||Q^{-1}||<=8/lambda` give finite
upper bounds on the field, its derivative and output derivatives.
Cauchy bounds on a smaller activation strip supply the required higher
activation derivatives. A bound on the derivative of the Gram and its
positive gap margin then gives a positive Euclidean tube radius.
The dependence on the retained metric condition numbers is charged;
it is not bounded polynomially here. These finite arithmetic bounds
allow (8) and the decrement test to select an integer `N`.

This is relative to effective activation/data evaluation, as is any
numerical implementation of the dense network; mere analyticity of an
unspecified noncomputable function is not an algorithmic input model.
Finite precision additionally perturbs initialization, coefficients,
RHS and loss tests. Their continuous finite-time error bounds allow
further tolerance allocation, but no small word-length bound is
asserted. The exact-real inventory theorem does not hide this extra
precision cost. Failures of an initialization event are not
reclassified as successful computations.

If the ODE has `D` counted state/coefficient scalars and its RHS uses
`W` work scalars, its Euler execution needs at most `2D+W+O(1)` real
registers: current state, one derivative buffer, work arrays, clock,
and a loop counter. A fixed-size loss-test routine is reused after
every update. There is no `N`-fold history table. This is a program
with a loop, not a claim that its fully unrolled operation graph has
size independent of `N`.

## 4. Concrete stopped-output corollary

For a useful fixed choice stop at training MSE `Y^2/n`, i.e. RMS
`a=Y/sqrt(n)`. This is a stopping tolerance; `Y` itself and the
allowable labels do not shrink with width. Define the local error budget

\[
e=\frac{Y}{n(1+8\mathcal K/\lambda)}.
\tag{10}
\]

Ask the source compiler for panel error at most `e/2` and choose the
Euler step so the numerical error from the compressed flow is at most
`e/2`, the last deficit decrement is at most `e`, and the tube
conditions hold. For sufficiently large `n`, `e/2<a/4`.
Equations (7)--(10) prove

\[
\max_{i\le p}
|f_{\rm num}(\tau_{\rm num},x_{m+i})
                   -f_n(\tau_n,x_{m+i})|\le\frac Yn,
\tag{11}
\]

where each system stops using its own training loss. The loop retains
the inventory (4), up to a constant factor for buffers already charged
by the imported inventory. It remains a reusable compressed model,
not merely a cache of `p` final answers. Query evaluation and a later
continuation of the numerical model use the same counted arrays.

At any other fixed positive loss threshold below the initial loss,
the same proof works. Inverse-polynomially small thresholds require
the minimum numerical tolerance and, if necessary, a corresponding
inverse-polynomial source target; their constant power changes
logarithmic degrees, not the type of storage bound. No claim is made
here for thresholds superpolynomially smaller than the requested
prediction accuracy, or for exact finite-time interpolation.

The source probability statement is inherited: for fixed admissible
data, activation, depth, panel and confidence, all sufficiently large
individual widths have the asserted success probability. The numerical
transfer is deterministic on that event and does not require another
independent random projection.

## 5. What this establishes, and what it does not

**Established extension.** On the imported neural source event there
is a streamed arithmetic program with polynomial parameter dependence
and third-power logarithmic retained real-coordinate size. It computes
the declared stopped predictions to (11), and its state does not grow
with the number of Euler steps. This is an execution-space result, not
merely a short description of a dense simulator.

For `m>=2`, the inherited lower bound on independent dense discrepancy
over the entire panel trajectory is of order
`Y sqrt(gamma)/(sqrt(n) log(en)^{5/2})` at fixed confidence. Thus (11)
is negligible compared with that particular whole-trajectory benchmark.
It does not lower-bound or compare to the possibly smaller discrepancy
of predictions at the two dense runs' respective loss stopping times.
An endpoint-specific relative theorem requires an additional argument.

The program consists of small matrix operations, scalar activations,
metric adjoints, Gram solves and a reused Euler loop. Its selected
matrices are data-dependent and are not independent Gaussian matrices.
Therefore this is a response-compressed tensor-arithmetic program,
**not** a new application of the standard population tensor-program
master theorem. Its error certificate comes from the imported source,
selection and corrected-dynamics arguments.

Setup may still be expensive. A finite zero-time-jet compiler establishes
initialization-only information provenance, not polylogarithmic setup
work. The numerical step count and coefficient precision can also be
large. `N` steps take `N` times the RHS work, and an unrolled graph
contains those repeated instructions. Word-length and loop-counter
bits must be charged in a bit model. No bound of the form
`poly(log n,m,d,1/gamma)` has been proved for all those bits, or for
total setup/integration work, in this note.

For reference, with selected maximum width `q` the inherited RHS work
is

\[
O(Lm q^2+mdq+Lqm^2+m^3+LmqA_\phi),
\]

and one query after refreshing the effective readout costs
`O(Lq^2+dq+Lq A_phi)`. Here `A_phi` is the charged activation/derivative
evaluation work; `q` is fixed by the source rank giving (4). These
counts are polynomial in the retained source size, not in the number
of past Euler steps. Fixed matrices, their caches and both work buffers
must all remain in (4); no dense random-access oracle is retained.
