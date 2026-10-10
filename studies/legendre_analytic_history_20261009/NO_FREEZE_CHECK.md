# Fresh scoped check of the no-freeze continuation

Date: 2026-10-10.

**Verdict: PASS within the stated scope.** I find no unresolved mathematical
objection to the deterministic tail lemma, its application after the prescribed
growing-horizon first stage, or the resulting all-time `Y/n` approximation and
retained learned-state count. This is an internal usage and reconstruction
check, not promotion and not a new certification of the entire probabilistic
cavity/source proof.

The checked candidate is `NO_FREEZE_TAIL.md`, SHA-256
`ed15f9dd811e9e4a84700ff15fa6d35de3f297bac6f6ee7a6a006c4381af34da`.
Inputs were that candidate, its complete direct dependency
`OBLIVIOUS_WINDOWS.md`, and the relevant setup, fitting, signed-comparison,
projection, source-interface and dense-variability material in
`paper/compact.tex`, `compact_fitting.tex`, `compact_legendre.tex`, and
`compact_foundations.tex`. No other study or previous check report was used.
The dependency's embedded check-status paragraph supplies no premise here.
The current paper's analytic-source proposition is imported as stated; its
application below is checked, while its full probabilistic cavity argument
is not re-certified. The rigorous-proof and canonical neural-network notation
skills were applied.

The fresh result checked here is the new deterministic tail and its assembly.
The existing first-stage theorem is used as a dependency; Section 1 verifies
the particular growing horizon and the deterministic comparison route that
the candidate imports. It does not claim to re-prove all of that theorem's
probabilistic carrier and cavity inputs.

## 1. The finite stage really covers the required growing horizon

Write `lambda = gamma/m` and `ell = log(en)`. The relevant first-stage
result is the final single-interval construction in `OBLIVIOUS_WINDOWS.md`,
on the particular horizon

\[
T=32\ell/\lambda,\qquad
r_t=\frac{\lambda}{\beta^{30L}Y^2\sqrt{(d+3)\ell}},\qquad
A=\max\{1,T/r_t\},\qquad q=\lceil16A\ell\rceil.
\]

These are exactly the candidate's prescribed parameters. The imported
source proposition supplies the whole rectangle
`[-r_t,T+r_t]+i[-r_t,r_t]`, forward RMS bounds, backward RMS bounds, and
the all-time dense training-carrier bound. No fixed-horizon theorem is being
evaluated at an increasing horizon.

For every `0<t<=T`, the Bernstein ellipse with parameter `exp(1/A)`
lies strictly within that rectangle: its imaginary half-height is
`t sinh(1/A)/2 < r_t`, and its extra real half-width is
`t(cosh(1/A)-1)/2 < r_t`. If a relevant vector history is bounded by `B`
there, its degree-below-`q` Chebyshev approximation has error at most
`4BA exp(-q/A)`. The Legendre endpoint operator then gives error at most
`4(1+64 sqrt(q))BA exp(-q/A)`. Since `A,q` are polylogarithmic and all
problem parameters are fixed, this is at most `epsilon=(en)^(-8)`
eventually. The physical backward history here is `r_a delta_a`, not the
residual-normalized history used by the original residual-clock method.
Its required complex bound follows from the source bounds and
`||r||_m <= max_a |f(x_a)|+Y`.

For completeness, the inherited nonlinear comparison closes on this same
growing interval. Let `D(t)` be the supremum up to `t` of the Euclidean
mobility-parameter discrepancy. Stop at `D<=epsilon`. Forward subtraction
costs `C D`; backward subtraction costs
`C(1+sqrt(ell))D`, using only the dense coordinate carrier bound in the
changed-gate term. The exact projected-pairing defect therefore satisfies

\[
\sum_{\ell'=2}^L\|\mathcal E_{\ell'}\|_F
 \le Cq(1+\sqrt\ell)(\epsilon+D)^2.
\]

The same segment subtraction verifies the two Taylor assumptions of the
paper's signed perturbation lemma with `K=O(1+sqrt(ell))`. Dense residual
activity is at most `2Y/lambda`; compressed activity is at most
`2Y/lambda+CT epsilon <=3Y/lambda` eventually. Hence its stability factor
is `exp(11KY/lambda)=n^(o(1))`, and integration of the quadratic defect
gives

\[
\sup_{t\le T}\|\theta_{\rm Leg}(t)-\theta_n(t)\|_{\rm par}
\le n^{-16+o(1)}.
\]

This strictly improves the stop. The direct dependency's Volterra
contraction defines the regular zero-moment branch at `t=0`: projection
contraction bounds the reconstructed increment and its path Lipschitz
constant by the interval length times a finite constant. Thus no positive
startup step is missing. Bounded physical paths bound the moment integrals
and give continuation through `T`. Forward subtraction also gives the same
order of whole-sphere prediction error. The real operator/readout tube
required by the signed comparison has a strict dense margin, preserved by
the vanishing discrepancy. No extra label condition is needed.

## 2. Exact tail defect and width-independent constants

All quantities in this section belong to the fresh order-one block.
Use the candidate's normalized physical parameters
`theta=(W^(1)/sqrt(n),W^(2),...,W^(L),w/sqrt(n))` and sum of block
Frobenius/Euclidean norms. Put

\[
A(t)=\int_{t_*}^t\rho(u)\,du,\quad \tau=1+A,\quad
V(t)=\int_{t_*}^t\|\dot\theta(u)\|_{\rm blocks}\,du.
\]

The constants `H,D,F,J,C_v,C_E,C_r,eta,epsilon_*` are those explicitly
defined in candidate equation (11). Their recurrences are sufficient:
on the unit parameter tube, feature RMS is at most `H`, backward-response
RMS is at most `D`, and a feature's RMS change is at most `F` times
parameter block distance. The output-gradient blocks have norms at most
`D`, `DH` at each hidden interface, and `H`; their sum is at most `J`.
Linear growth of activation values suffices. These calculations contain
no coordinate maximum or Hessian bound and no unnormalized sample sum.

Direct differentiation gives

\[
\partial_t\frac{\bar h_a}{\tau}
=\frac\rho\tau\left(h_a-\frac{\bar h_a}{\tau}\right),
\qquad
\mathcal E_\ell
=\frac2{mn}\sum_a
\left(r_a\delta_a^{(\ell)}-\frac\rho\tau\bar\delta_a^{(\ell)}\right)
\left(h_a^{(\ell-1)}-\frac{\bar h_a^{(\ell-1)}}\tau\right)^\top.
\]

Here `mathcal E_ell` is added to the ordinary hidden gradient-flow
velocity `-2 sum_a r_a delta_a h_a^top/(mn)`. This verifies the sign,
the factor `2/(mn)`, and the factor `rho/tau` in equation (15).
It is an identity in physical parameter space; the stored-state ODE need
not itself be a gradient flow.

The forward memory divided by `tau` is a convex average of the initial
and subsequent features. Consequently its RMS is at most `H`, and its
difference from the current feature has RMS at most `2FV`. Minkowski
and sample Cauchy--Schwarz give exactly

\[
\left(\frac1{mn}\sum_a\|\bar\delta_a\|^2\right)^{1/2}
\le D\int_{t_*}^t\rho=D A.
\]

Thus, while `A<=1` and `V<=eta<=1`,

\[
\sum_{\ell=2}^L\|\mathcal E_\ell\|_F
\le4(L-1)DF(1+A/\tau)\rho V\le C_E\rho V.
\]

Using the differentiated reconstruction before subtracting the dense
velocity gives the sharper speed estimate

\[
\|\dot\theta\|_{\rm blocks}
\le2J\rho+4(L-1)DF(A/\tau)\rho V\le C_v\rho.
\]

The candidate's versions replace `A/tau` by the larger `A`; their constants
are therefore valid. No factor of `m` or `n` has been lost.

The normalized feature-matrix perturbation has operator norm at most `FV`.
The threshold `V<=sqrt(lambda_0)/(2F)` preserves a readout Gram gap of
`lambda_0/4`. Ordinary gradient flow therefore contracts residual RMS
at rate at least `lambda_0/2`. The hidden defect changes prediction
velocity by at most `DH sum_ell ||mathcal E_ell||_F` in sample RMS.
The second threshold `V<=lambda_0/(4C_r)` yields

\[
\dot\rho\le-\lambda_0\rho/4.
\]

Finally the stated `epsilon_*` gives

\[
A(t)\le4\rho(t_*)/\lambda_0\le\tfrac12,
\qquad
V(t)\le4C_v\rho(t_*)/\lambda_0\le\eta/2.
\]

Both provisional stops improve strictly. The stored-state vector field
is locally Lipschitz for `tau>=1`, including residual zero; all memory
variables remain bounded and have integrable velocities. This proves
global existence, moment and physical-parameter convergence, and fitting.
At residual zero the entire active state is stationary. The sphere output
movement is at most `4JC_v rho(t_*)/lambda_0`, including the limit.
These conclusions do not require a zero restart readout, continuity of
a residual-normalized backward prefix, bounded activation values, or
Gaussian restart weights. The analytic activation class of the original
problem supplies all the lemma's regularity assumptions.

## 3. Trigger, Gram transfer and all-time error

Let `e_n=n^(-16+o(1))` bound both first-stage discrepancies, enlarging a
fixed-problem constant if necessary. Initially the compressed residual
RMS is `Y`; at `T`, it is at most `Y(en)^(-16)+e_n`. For fixed `Y>0`
this is below `Y/n^2` eventually. Continuity therefore gives a first
trigger `0<t_*<=T`, with residual exactly `Y/n^2`. No monotonicity of the
first-stage compressed residual is required. The uniform deterministic
interval estimate is valid at this random time without an optional-stopping
argument or information about the later trajectory.

The dense normalized top-feature matrix has smallest singular value at
least `sqrt(gamma/m)/2` throughout. First-stage parameter accuracy and
forward subtraction perturb that matrix by `O(e_n)` in operator norm.
For perturbation below
`(1/2-1/sqrt(8))sqrt(gamma/m)`, the switching Gram therefore has gap
`lambda_0=gamma/(8m)`, exactly as claimed. The operator/readout bounds
also transfer with a fixed bound `B`. All tail constants are then fixed
as width grows; `Y/n^2<=epsilon_*` holds eventually. This is a width
qualification, not a new restriction on the initial labels or data.

At the same trigger the dense residual RMS is at most `Y/n^2+e_n`.
The dense fitting proof supplies finite remaining parameter length and
a uniform sphere output bound by a fixed constant times that residual.
The bound applies to every later time, as follows either by integrating
the speed bound in that proof or by using its endpoint bound twice.
Combining the two output tails with the discrepancy at the trigger gives

\[
\sup_{t\in[t_*,\infty],\ \|x\|=\sqrt d}
|f_{\rm Leg}(t,x)-f_n(t,x)|
\le C\left(Y/n^2+e_n\right)\le Y/n
\]

eventually. Before the trigger the stronger first-stage bound applies.
Both fitted endpoints exist and satisfy the same estimate. The deterministic
choice `t_*=T` also works, with its smaller starting residual.

The actual dense-variability lower bound used by the candidate is the
paper's positive-time lower bound
`cY sqrt(gamma)/(sqrt(n) log(en)^(5/2))`. The resulting ratio is bounded
by `log(en)^(5/2)/(c sqrt(gamma*n))`, tending to zero. Intersecting
the fixed-confidence events and then letting their failure budgets tend
to zero proves convergence in probability. No independence between the
approximation and variability events is needed. There is no assertion
uniform in vanishing `Y`, growing data, or infinitely many independently
sampled widths.

## 4. Information and the remaining algorithm change

The archived first-block moments reconstruct the trained baseline by
candidate equation (7); they need not produce a retained dense matrix.
Both a baseline matrix and its transpose can be applied using the original
fixed mixer and the retained outer-product factors. The tail uses only
current compressed forward/backward evaluations, its residual, its live
moments and that archive. The qualification parameters and first-stage
degree are fixed before training. No dense continuation, future prediction,
initialization jet compiler or fitted response subspace enters the algorithm.

The first block retains `2(L-1)mnq` learned coordinates even after it stops
changing. The fresh block adds `2(L-1)mn`; first layer and readout retain
`n(d+1)`. Interval length, live clock and phase require `O(1)` more.
Thus the complete retained learned storage is exactly of the claimed form
`n(d+1)+2(L-1)mn(q+1)+O(1)=n^(1+o(1))`. Initialized mixers still require
`(L-1)n^2` fixed entries. The claim is not about subquadratic total storage,
practical runtime or finite-precision implementation.

At rollover the physical weights are continuous, and the fresh hidden
velocity equals the ordinary gradient velocity because
`bar h_a/tau=h_a` and `bar delta_a=0`. Every physical layer subsequently
has an active update; a particular velocity may vanish naturally. This
does remove imposed physical-layer freezing.

The remaining modification is substantive and disclosed: a zero-prefix
physical-time block is archived once, and a fresh residual-clock block
with `tau=1`, current forward seeds and zero backward seeds takes over.
The representation and generally the physical derivative change at that
event. The result is a continuous physical trajectory generated by a
hybrid online memory method. It does not establish the same memory order
for the original unchanged single-block residual-clock method or for one
globally smooth switch-free ODE. The original method's fitting was not
the obstruction repaired here; dense-trajectory approximation was.
