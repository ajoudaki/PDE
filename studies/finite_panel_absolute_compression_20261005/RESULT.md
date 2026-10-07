# Autonomous compression for a predeclared finite test panel

2026-10-05. New extension of the explicitly authorized integrated compact
proof. Internal research result, not established-book promotion. The new
argument is the finite-panel source construction and its transfer to the
existing nonlinear optimizer. The stochastic insertion, selection, fitting,
and dense-variability theorems remain inherited inputs; their source-success
width is not made effective here.

## 1. Setup and headline theorem

Fix a panel of **p total inputs**, including **m training inputs**, before
initialization. They lie on the radius-sqrt(d) sphere. The training inputs
span R^d and p >= m >= d; depth L >= 2 is arbitrary and fixed. The panel
may contain repeated or correlated points. No positive Gram gap is required
on the passive points.

The dense reference has hidden width n, first weights with independent
N(0,1) entries, hidden mixers with independent N(0,1/n) entries, and zero
readout. Its architecture is

\[
z^1(x)=Ax/\sqrt d,\qquad z^j(x)=W^jh^{j-1}(x),\qquad
h^j(x)=\phi_j(z^j(x)),\qquad f_n(x)=w^Th^L(x)/n.
\]

All blocks train, using loss m^(-1) sum over the m training squared errors
and block mobilities (n,1,...,1,n). Passive inputs have zero loss weight:
they do not change the denominator m or physical time.

Activations are real on the real axis, holomorphic on a common strip
|Im z| < a, and have bounded first derivative there. Their values may be
unbounded. Define the activation envelope, label size, and training gap by

\[
\begin{split}
\beta&=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}|\phi_j^{(k)}(z)|\right\},\\
Y&=\|y\|_2/\sqrt m,\qquad
\gamma=\lambda_{\min}(Q^L)>0,\\
Q^0_{ab}&=x_a^Tx_b/d,\qquad
Q^j_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad Z\sim N(0,Q^{j-1}).
\end{split}
\tag{1}
\]

Only training indices enter Q. The clean numerical statement uses the
same existing sufficient label condition

\[
0<Y\le(\gamma/m)\beta^{-30L}.
\tag{2}
\]

The construction also preserves the full, larger existing recurrence
allowance; its statement is in Section 6. Thus (2) is a convenient display
case, not an additional restriction on the general construction.

For each confidence 1-delta, at every sufficiently large individual n,
with probability at least 1-delta, an initialization-only construction
produces an autonomous compact model f_C whose layer widths are at most

\[
\boxed{q=\left\lceil30000p[\log(en)]^{5/2}\right\rceil.}
\tag{3}
\]

The core parameter-and-residual moving-state count is at most

\[
(L-1)q^2+q(d+1)+m.
\tag{4}
\]

If passive feature values are also kept as dynamical variables rather than
recomputed, their additional coordinates are counted in (5), not in (4).

Counting fixed metrics and coefficients, inputs, labels, current feature
and response arrays, solve caches, and live observation workspace as well,
a conservative bound on **all retained real coordinates** is

\[
\boxed{
2^{36}(L+1)p^2[\log(en)]^5+16p(d+1)
\quad\text{plus the fixed activation/runtime evaluator.}}
\tag{5}
\]

The numerical constant is deliberately not optimized. In particular, the
exponent five is absolute, independent of d,m,p,L and the activations.
There is no hidden exponential-in-d storage coefficient in (5).

At the same physical times, including the limiting fitted state,

\[
\boxed{
\sup_{t\in[0,\infty]}\max_{1\le i\le p}
 |f_C(t,x_i)-f_n(t,x_i)|
\le
10\beta^{40L}Y\frac m\gamma
\left(1+\sqrt{\frac m\gamma}\right)
\frac{e^{2\sqrt{\log(en)}}}{n}.}
\tag{6}
\]

The coefficient retains polynomial sample/gap and beta^L dependence.
There is no such dependence inside exp. Only the p declared inputs are
covered by the error guarantee. The smaller network happens to admit a
forward pass at other inputs too; no accuracy there is asserted.

The construction uses the inherited **corrected-readout optimizer**,
not ordinary gradient flow on an iid smaller network. Its hidden layers
and nonlinear features evolve; they are neither frozen nor linearized.
As usual, degenerate data can produce stationary blocks, so preservation
of feature learning is an architectural/dynamical statement, not a claim
that every admissible trajectory moves every coordinate.

## 2. Why the dimension-dependent exponent disappears

The old source space approximated vector-valued functions of both physical
time and an arbitrary sphere query. Here it only needs a finite list of
vector-valued functions of time. One does not interpolate the panel by a
spatial polynomial or cover the sphere by a net.

For this proof write lambda=gamma/m, ell=log(en), S=16Y/lambda, and
T=32ell/lambda. The authorized finite-query localization in
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md, Sections 2–3](../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md)
gives, with probability tending to one, holomorphic continuation to a
neighborhood of

\[
[-r,T+r]+i[-r,r],\qquad r=\frac{\chi}{\lambda\sqrt\ell}.
\tag{7}
\]

Here chi=1 under (2). On the full allowance,

\[
\chi=\min\left\{1,\frac{a}{4S^2U_{\rm fin}(S)}\right\}>0,
\tag{8}
\]

where U_fin is exactly recurrence (9) of that source, with its fixed
Gaussian-union coefficient 64. It contains no input dimension or panel
count. The same source proves chi >= chi_act > 0, where chi_act depends
only on the activations and depth, throughout the original allowance.

At each layer the needed sources are the forward features and their
initialized forward images at every panel point, and backward responses
and their initialized reverse images at training points. Using all four
families at every panel point is a harmless upper count of 4p curves.
The training backward carrier maximum is unchanged. Passive backward
carriers do not need a new coordinate-maximum estimate.

For completeness, the localization also supplies the four-family bounds,
not just output holomorphy. Its unchanged complex operator caps are ten,
feature RMS bounds are H_j, and readout RMS is at most S H_L. Backward
recursion with bounded derivative gates gives response RMS at most
S tau_j. Initialized images have at most eight times these bounds.
All are holomorphic algebraic compositions on (7). Since S <= 1, every
coordinate has modulus at most M_0 sqrt(n), where

\[
H_1=\max(1,b+20s),\quad H_j=\max(1,b+10sH_{j-1}),\quad
\tau_j=sH_L(10s)^{L-j},\quad
M_0=10\max_j\{H_j,\tau_j\}.
\tag{9}
\]

Here b=max_j|phi_j(0)| and s is the half-strip first-derivative bound,
enlarged to at least one. These are local source coefficients, not new
model parameters. This derivation uses RMS and linear growth, not bounded
activation values.

Map time by t=T(1+cos u)/2 and put alpha=r/(4T)=chi/(128ell^(3/2)).
For alpha <= 1 the strip |Im u| <= alpha maps inside (7). Even Fourier
expansion is a real Chebyshev expansion; its kth vector coefficient has
coordinate magnitude at most 2 M_0 sqrt(n) exp(-alpha k). Consequently
the tail after degree K has coordinate norm at most

\[
\frac{4M_0\sqrt n}{\alpha}e^{-\alpha K}.
\]

Choose

\[
K=\left\lceil\frac1\alpha
 \log\frac{64M_0n^{3/2}}\alpha\right\rceil.
\tag{10}
\]

The truncation error is at most 1/(16n). Finite coefficient computation
uses part of the remaining error budget, so each actual source has an
approximant with coordinate error at most 1/n. As in the inherited
construction, apply identical scalar operations to a source and its
initialized image, preserving their image identity exactly.

If log_+(8192M_0/chi) <= ell, then the logarithm in (10) is at most
3.5ell: use log n <= ell and 1.5log ell <= ell. Ceilings and alpha <= 1
therefore give K+1 <= 6ell/alpha. Including all 4p curves and the original
exact initialized additions gives a source-dimension budget

\[
R=\left\lceil\frac{3072p}{\chi}\ell^{5/2}\right\rceil+2m+d+1.
\tag{11}
\]

The additions are initialized training features and their forward images,
first-weight columns and the constant vector. The coefficient vectors
themselves have n entries but exist only during preprocessing; they are
not retained. Source rank, rather than coefficient-array length, governs
the selected runtime.

This is the origin of the absolute exponent:

\[
\underbrace{T/r}_{\text{time interval / analytic radius}}
 \underbrace{\log n}_{\text{accuracy}}
 =O(\chi^{-1}\log^{5/2}n)
\quad\Longrightarrow\quad
\text{matrix storage}=O(\chi^{-2}\log^5 n).
\tag{12}
\]

No spatial basis occurs. Depth affects the source coefficients and width
threshold, not the exponent in (12).

## 3. From temporal sources to an autonomous nonlinear model

Apply the inherited deterministic coordinate-selection construction to
the finite source spaces. It gives at most 9R selected coordinates per
layer and positive metrics M_j, with positive diagonal D_j satisfying

\[
D_j/4\preceq M_j\preceq D_j,\qquad
\|\mathbf1\|_{M_j}=1.
\tag{13}
\]

Restriction is an exact isometry on each source space, for the original
neuron inner product u^Tv/n. The selected initialized forward maps and
their metric adjoints preserve the paired source-image identities and
have norm at most eight. Including initialized training sources exactly
preserves their Gram and its initial gap. First-weight columns are also
exact. These are the same selection interfaces used by the authorized
compact proof; no new sparsification theorem is assumed.

Here are explicit runtime equations. Normalize inputs by v_i=x_i/sqrt(d).
Let A_C, B_C^j, w_C be the moving selected network arrays and c in R^m
its moving residual. Initialize them by selected initialization, w_C=0,
and c=y. Compute the nonlinear forward pass with these arrays. If H is
the matrix of its m training top features and G=H^T M_L H, define

\[
\widehat w_C=w_C+HG^{-1}(y-c-H^TM_Lw_C),\qquad
f_C(v_i)=\widehat w_C^TM_Lh_C^L(v_i).
\tag{14}
\]

Thus y_a-f_C(v_a)=c_a exactly for training indices. Use backward signals
k_a^L=widehat w_C, delta_a^j=phi'_j(z_a^j) componentwise times k_a^j,
and k_a^j=(B_C^{j+1})*delta_a^{j+1}, with metric adjoints.
For training a,b only, define the algebraic Gram

\[
\begin{split}
K_{ab}={}&\langle h_a^L,h_b^L\rangle_{M_L}
 +\langle\delta_a^1,\delta_b^1\rangle_{M_1}(v_a^Tv_b)\\
&+\sum_{j=2}^L
 \langle\delta_a^j,\delta_b^j\rangle_{M_j}
 \langle h_a^{j-1},h_b^{j-1}\rangle_{M_{j-1}}.
\end{split}
\]

The closed autonomous system is

\[
\dot A_C=\frac2m\sum_{a\le m}c_a\delta_a^1v_a^T,\quad
\dot B_C^j=\frac2m\sum_{a\le m}c_a\delta_a^j(h_a^{j-1})^TM_{j-1},
\quad
\dot w_C=\frac2m\sum_{a\le m}c_ah_a^L,\quad
\dot c=-\frac2mKc.
\tag{15}
\]

No dense weights, time coefficients, future predictions, or external
forcing occur in (14)–(15). The only inverse is the m-by-m training Gram.
Passive inputs have no residual, backward update, or label. They may be
evaluated from the current smaller network, or explicitly evolved by

\[
\dot z_i^1=\dot A_Cv_i,\qquad
\dot z_i^j=\dot B_C^jh_i^{j-1}
 +B_C^j[\phi'_{j-1}(z_i^{j-1})\odot\dot z_i^{j-1}].
\tag{16}
\]

Consistent initialization makes (16) equal the current forward pass.
Its retained panel features and workspace fit the count below. Even when
using (16), no passive point changes (15).

The original real fitting proof uses only exact initial training Gram,
operator bounds, (13), and its original label allowance. It gives global
existence, Gram/m >= (gamma/(4m))I, exponentially decaying training
residual, convergence of every parameter, and endpoint interpolation.
Non-diagonal metric gates are not self-adjoint; (15) is a specified
optimizer, not falsely identified with ordinary gradient flow.

Finite jet continuation and temporal quadrature construct the source
coefficients from initialization, inputs and training labels, with the
positive radius (7). This is the same finite initialization-only
compilation interface as the existing proof, with the spatial quadrature
removed. Discard the jets, quadratures, original-width vectors and dense
arrays after forming the selected initialization and metrics. The
resulting runtime is restartable from its counted state; it is not
trajectory playback. No efficient preprocessing-time bound is proved.

## 4. Error, full physical time, and actual dense variability

The existing improved source-to-runtime comparison only needs forward
source control at a query where an output error is requested. Its backward
subtraction, carrier maxima, right inverse, and residual/readout
cancellation all involve training indices only. Replacing the whole-sphere
forward supremum by a maximum over p declared inputs therefore changes
no comparison coefficient. No factor p enters the error bound.

More explicitly, exact source isometry and coordinate accuracy 1/n imply
the original source-pairing and paired-action error bounds, for all
training/training and training/panel pairs. The raw selected dense readout
and its integrated velocity are O(Y sqrt(m/gamma)) by the existing energy
argument. Lifting the residual difference with the compact training
right inverse cancels the leading residual/readout feedback. The
remaining integrated coefficient is bounded by 1+sqrt(log(en)) under
(2), or 44+32sqrt(log(en)) on the full allowance. These are exactly the
proved reductions in the two imported comparison files, with no source
error differentiated and no passive Gram inverse introduced.

This proves (6) through T. Independent dense and compact fitting bounds
make their remaining tails at most a fixed polynomial task coefficient
times exp(-8ell). The same-time triangle inequality after T proves (6)
on the entire half-line and at its limit. The runtime continues to train
after T; it is not frozen at T.

For m >= 2 and Y > 0, the existing general dense lower bound is witnessed
at a **training input**. It consequently holds in the same panel norm:
with probability at least 1-delta at every sufficiently large individual n,

\[
\sup_{t\in[0,\infty]}\max_{i\le p}
 |f_n(t,x_i)-\widetilde f_n(t,x_i)|
\ge c_{\phi,L,\delta}
\frac{Y\sqrt\gamma}{\sqrt n[\log(en)]^{5/2}}.
\tag{17}
\]

The second dense run is independent. Combining (6) with (17), their
ratio is bounded by a fixed coefficient times
n^(-1/2) log(en)^(5/2) exp(2sqrt(log(en))), which tends to zero.
For the full allowance the additional factor 1+sqrt(log(en)) and constant
32 in the exponential do not change this limit. Therefore

\[
\boxed{
\frac{\sup_{t\in[0,\infty]}\max_{i\le p}|f_C(t,x_i)-f_n(t,x_i)|}
 {\sup_{t\in[0,\infty]}\max_{i\le p}|f_n(t,x_i)-\widetilde f_n(t,x_i)|}
\ \xrightarrow{\mathbb P}\ 0.}
\tag{18}
\]

To verify the probability quantifiers, for any desired failure probability
choose (17) at half that probability, then intersect with compression
success. The deterministic ratio tends to zero. No independence between
compression and the lower-bound event is needed. The denominator-zero
event has vanishing probability; assign any value to the ratio there.

This is stronger than calibration only to a dense upper bound. It is a
ratio of two whole-trajectory norms, not a pointwise relative error or an
endpoint separation theorem. If m=1 the compression still holds, but
positive uncentered gap alone does not guarantee a positive dense lower
bound for the full activation class. If Y=0, both predictors are exactly
zero and no variability ratio is asserted.

## 5. Honest storage and width conditions

The inherited training-runtime inventory is
1020(L+1)R^2+10m(d+1), including fixed metrics, copies and solve caches.
Add all passive inputs, their current features or sequential evaluation
workspace, and all p outputs. Since q_j <= 9R, d,m,p <= R, even the
simultaneously stored panel version fits

\[
2048(L+1)R^2+16p(d+1)
\quad\text{plus the fixed activation/runtime evaluator.}
\tag{19}
\]

For example, eight p-by-q_j buffers per layer for values, derivatives,
velocities and observation scratch cost at most 72 L p R <= 72 L R^2.
Additional O(R) output buffers and O(m^2) solves are covered by the stated
slack. Dense coefficient vectors and preprocessing workspace are explicitly
not retained and not part of a runtime-storage claim.

Using p >= m >= d >= 1, ell >= 1 and chi <= 1 in (11) gives
R <= 3077p chi^(-1)ell^(5/2). Hence q_j <= 27693p chi^(-1)ell^(5/2),
and 2048*3077^2 < 2^36. This proves (3) and (5) when chi=1. It also
proves the same bounds with chi^(-1) in q and chi^(-2) in leading
storage on the full allowance.

For every fixed problem and confidence, a finite sufficient width exists.
The explicit deterministic construction gates, in the proof-local
notation above, are

\[
\begin{gathered}
n^{-1}\le\min\{1,Y,S\},\qquad
\ell\ge2048e^2L,\qquad
\sqrt\ell\ge\frac\chi\lambda
 \max\{8,\lambda,4\mathcal K/\log2,32YSD_W\},\\
\log_+(8192M_0/\chi)\le\ell,\qquad
\mathcal K=H_L^2+S^2\left[\tau_1^2+
 \sum_{j=2}^L\tau_j^2H_{j-1}^2\right],\quad
D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\}.
\end{gathered}
\tag{20}
\]

Here log_+(u)=max(0,log u). The temporal-strip condition alpha<=1
is automatic from ell>=1 and chi<=1. The source construction, finite
initialization, and selection events must also hold. Their stochastic
success threshold is inherited and unquantified; it can depend on all
fixed parameters, panel geometry, activations and delta. It is not claimed
polynomial, nor absorbed into the error coefficient. Effective portions
such as initialization can be stated separately, but do not make the
overall threshold effective.

If one requires the displayed width budget itself to be below n, additionally
check ceil(30000p chi^(-1)ell^(5/2)) <= n. This holds eventually.
For a prescribed error epsilon, (6) being <= epsilon is the explicit
accuracy test. For actual-variability calibration (18), intersect also
with the eventual-width conditions of (17).

The confidence statement is for each sufficiently large individual width,
not a simultaneous event over infinitely many independently sampled widths.
All task parameters, including p, are fixed in this limit. The displayed
storage tracks p explicitly, but a theorem for growing p(n),d(n),m(n)
requires rechecking probability and width estimates. An exponentially
large supplied panel is not dimension-free data storage.

Counts are real-coordinate counts in the same computational convention
as the dense network and inherited compact model. They do not bound bits,
conditioning, arithmetic precision, preprocessing time, or full simulation
time. Activation evaluation uses the same specified evaluator/interface
as the original dense model; its retained implementation and workspace
must be counted, not replaced by a hidden width-dependent oracle.

## 6. Full original label allowance and provenance

The unchanged larger allowance is, in the original recurrence notation,

\[
Y\frac m\gamma\le
\min\{(8H_d\sqrt{F_d})^{-1},
       (16H_c\sqrt{F_c})^{-1},S_*^{\rm src}/16\}.
\tag{21}
\]

The definitions are exactly
[GENERAL_EXPLICIT_FITTING.md (2),(4)](../integrated_general_compression_20261004/GENERAL_EXPLICIT_FITTING.md),
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](../integrated_general_compression_20261004/EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md),
and [UNBOUNDED_COMPRESSOR_BRIDGE.md (5)–(10)](../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md).
No entry is tightened. This is the dense/compact/source intersection;
retaining an additional Legendre allowance from the integrated common
interface is harmless but unnecessary for the present model.

Use chi from (8), or its activation/depth-only lower bound chi_act,
in (3),(5),(20). The all-time error becomes the inherited full-range bound

\[
\sup_{t\in[0,\infty]}\max_{i\le p}|f_C(t,x_i)-f_n(t,x_i)|
\le C\beta^{42L}Y\frac m\gamma
 \max\left(1,\sqrt{\frac m\gamma}\right)
 \frac{(1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}}{n},
\tag{22}
\]

where C is universal. Thus the full label scope, absolute exponent five,
polynomial error prefactor, and actual-variability comparison all survive.
Only the particularly simple leading storage constant and numerical
error exponent in (5),(6) use the simpler existing cap (2).

The new temporal approximation, localization transfer, runtime dependency
audit and retained-state count are documented independently in
[PANEL_SOURCE.md](PANEL_SOURCE.md), [PANEL_RUNTIME.md](PANEL_RUNTIME.md),
and [PANEL_AUDIT.md](PANEL_AUDIT.md). These routes first froze separate
analyses and only then checked the stronger localized radius.

Other inherited components read for this synthesis are
[COMPACT_SOURCE_ENERGY.md](../integrated_general_compression_20261004/COMPACT_SOURCE_ENERGY.md),
[COMPACT_POLYNOMIAL_COMPARISON.md](../integrated_general_compression_20261004/COMPACT_POLYNOMIAL_COMPARISON.md),
[COMPACT_FULL_LABEL_RANGE.md](../integrated_general_compression_20261004/COMPACT_FULL_LABEL_RANGE.md),
[SIMPLE_CONSTANTS_SOURCE_CHECK.md](../integrated_general_compression_20261004/SIMPLE_CONSTANTS_SOURCE_CHECK.md),
and [GENERAL_VARIABILITY_LOWER_RESULT.md](../integrated_general_compression_20261004/GENERAL_VARIABILITY_LOWER_RESULT.md).
The exact finite-query source proof is the lower bridge linked in Section 2.
This study does not independently reconstruct its inherited insertion
theorem or claim a fresh promotion audit of the integrated program.
