# What the autonomous theorem resolves, and the correlated-input boundary

This note records the coordinator's reconstruction and scope check of the
28 September continuation. The complete autonomous theorem and proof are in
`AUTONOMOUS_ONE_SAMPLE.md`. The general tail oracle and the energy route are
in `TAIL_ORACLE_ROUTE.md` and `ENERGY_STABILITY_ROUTE.md`.
No theorem in the manuscript or maintained book is changed by these notes.

## 1. The new theorem is for the actual algorithm

For two hidden tanh layers and one normalized training input, no gate,
residual, clock, response history, or learned weight is supplied by the dense
reference. Both networks start at the same initialization; the closure uses
the original old-clock moment equations without alteration. The transformed
coordinate used in the proof is an invertible change of state, not a change
of optimizer or a new closure rule.

At every finite width and every order, the normalized parameter discrepancy
and the discrepancy of predictions on any bounded test-input set satisfy

\[
 \sup_{t\le T}\operatorname{error}_{n,P}(t)
 \le C_T\left\{\frac1{P(P+1)}
       +\frac{\|\delta_0\|_2/\sqrt n}{P\sqrt{P+1}}\right\}.
\]

The constant depends only on the fixed time horizon, label, initialized
hidden operator norm, initial readout sup norm, and the test-input radius
when appropriate. It is independent of width and order. The first-layer
and readout parameter norms are RMS; the hidden-matrix difference uses
ordinary Frobenius norm. The corresponding population statement uses
L2 fields and Hilbert--Schmidt increments. With zero initial readout,
the bound is O(P^-2), even though the clock is the original residual clock.

The independent proof ingredients are:

1. The exact readout identity bounds its RMS, the residual, and accumulated
   activity. The bounded top activation also bounds the readout pointwise.
2. The coordinate G(u)=u/2+sinh(2u)/4 cancels the first-layer backward gate.
   Its inverse is 1-Lipschitz. The transformed comparison therefore uses
   only bounded operators and the bounded readout multiplier.
3. Forward-history H1 control and the endpoint evaluation norm P/sqrt(tau)
   bound the squared middle velocity defect uniformly in order.
4. That estimate gives H1 control of the second preactivation and hence of
   the top backward history. At zero initial readout the backward prefix
   is continuous, so both history tails have order P^-1.
5. The exact paired-energy identity bounds the accumulated absolute
   velocity defect by the product of those tails. The transformed
   comparison then transfers O(P^-2) consistency to whole-trajectory
   tracking.

This neither assumes closeness nor prescribes a stability estimate. The
population moment system is constructed by clipping the readout only inside
the backward response for local existence, then proving that clipping never
activates. Its first-layer coordinate is G(u)-G(u_0), so no exponential
moment of G(u_0) is needed.

For uniqueness in original coordinates, any regular original solution has
an almost-everywhere absolutely continuous first preactivation path. The
scalar chain rule gives
`G(u(t))-G(u_0) = -2 integral_0^t r(s) W(s)^*delta(s) ds`.
The right side is a Bochner L2 integral by the operator and response bounds.
Thus every original solution belongs to the transformed state space and
solves the locally unique clipped system, whose clip is inactive. This also
justifies the reverse implication without differentiating G as a map on L2.

## 2. Canonical finite Gaussian readout: explicit probability calculation

Write w_(0,i)=Z_i/n with independent standard normal Z_i. Then

\[
 \frac{\|w_0\|_2}{\sqrt n}
 =\frac1n\sqrt{\frac1n\sum_iZ_i^2}.
\]

For the event that this RMS exceeds 2/n, Chernoff's inequality with
lambda=3/8 and the elementary Gaussian integral
E exp(lambda Z^2)=(1-2lambda)^(-1/2) gives

\[
 \Pr\{\textstyle\sum_i Z_i^2>4n\}
 \le e^{-3n/2}2^n
 =e^{-n(3/2-\log2)}.
\]

The scalar Gaussian tail bound also gives

\[
 \Pr\{\max_i|w_{0,i}|>1\}\le2n e^{-n^2/2}.
\]

For independent N(0,1/n) hidden entries, two 1/4 nets of size at most 9^n
give

\[
 \Pr\{\|W_0\|_{\rm op}>K\}
 \le2\exp\{n(2\log9-K^2/8)\}.
\]

Indeed each bilinear form on the two unit nets is N(0,1/n), and the
operator norm is at most twice their maximum absolute value. A fixed K
with K^2/8>2 log9 makes this bound exponentially small. By a union bound,
outside events of total probability tending to zero exponentially in n,
the autonomous theorem has one common constant and yields

\[
 \sup_{t\le T}\operatorname{error}_{n,P}(t)
 \le C_T\bigl(P^{-2}+n^{-1}P^{-3/2}\bigr).
\]

This assertion holds simultaneously for all orders on each such
initialization event. It does not claim that a deterministic constant
covers every Gaussian draw, or that a new width-convergence rate has been
proved for the dense model. If that model has population prediction error
a_n(T) in the same test norm, triangle inequality adds a_n(T) to this bound.

## 3. Why the scalar cancellation does not extend automatically to correlated inputs

This is a precise obstruction to the same coordinate trick, not a no-go
theorem for the main approximation result.

For one first-layer neuron with weight vector a in R^d and normalized
inputs q_b=x_b/sqrt(d), its exact update has the form

\[
 \dot a=-\frac2m\sum_b r_b c_b\,X_b(a),\qquad
 X_b(a)=\phi'(q_b\cdot a)q_b,
\]

where c_b is the incoming backward carrier before the first activation
derivative. With one sample, the primitive of 1/phi' straightens the one
vector field along that sample. With several samples, making every
coefficient field X_b constant by one C2 coordinate map would require
those fields to commute.

Direct differentiation gives, with z_b=q_b dot a,

\[
 [X_a,X_b]
 =(q_a\cdot q_b)
 \left[\phi'(z_a)\phi''(z_b)q_b
       -\phi'(z_b)\phi''(z_a)q_a\right].
\]

For linearly independent, nonorthogonal q_a,q_b this bracket is generically
nonzero for tanh. For example choose z_a=0 and z_b=1; these values can be
realized simultaneously because the two linear functionals are independent.
Then phi''(0)=0 and phi''(1) is nonzero, so the displayed bracket is nonzero.
A C2 diffeomorphism preserves brackets: applying the chain rule twice to
the pushed-forward fields cancels the symmetric second derivatives of the
map. Constant vector fields have zero bracket. Thus no such simultaneous
straightening map exists near this state.

The actual coefficients r_b c_b are network-generated, so this observation
does not exclude an argument exploiting their structure, a different metric,
or a non-coordinate stability proof. It explains exactly why repeating the
one-sample cancellation is not a proof for arbitrary correlated data.

With additional hidden layers, the same first-layer cancellation still
works for one sample, but varying internal gates multiply initialized
backward carriers. A transformed first-layer coordinate does not remove
those products.

## 4. What the general tail oracle adds, and what it cannot establish

At each initialized backward carrier q, clip its magnitude at M and use
the own gate on the clipped part, retaining the dense gate only on q-clip(q).
All learned branches remain self-gated. The resulting oracle is well posed
and has error at most C exp((a+bM)T)/P. The constant before Gronwall grows
linearly in M at fixed depth, rather than as M to the depth.

For one fixed regular population reference, M(P) tending to infinity more
slowly than log P makes the oracle error and its remaining external-gate
velocity intervention tend to zero. This is a genuine intermediate result.
Each finite member still uses dense data. To identify the actual autonomous
closure, the comparison introduces a dense-carrier tail H_T(M) amplified
by the same exp((a+bM)T). Ordinary L2 continuity makes H_T(M) vanish but
does not control that product. A slowly increasing threshold alone does
not solve this problem. Uniformity over finite widths also needs a common
tail statement, not merely tail convergence for the limiting population.

The energy route separately proves that the actual autonomous old-clock
closure has total positive loss variation at most C_T/P, for arbitrary
fixed depth and finite data. This controls its departure from loss
monotonicity; it does not compare its loss trajectory to dense training.

The unrestricted, arbitrary-depth, correlated-data width-uniform tracking
theorem therefore remains open. No counterexample to the canonical Gaussian
closure is supplied by the multiplier diagnostics. The new positive theorem
is a complete autonomous result in the explicitly stated two-hidden-layer,
one-sample scope, and should be reported as that result rather than as a
solution of the broader conjecture.

## 5. Check provenance

The coordinator read the complete three route reports and reconstructed the
transform, source-energy argument, prefix estimate, probability calculation,
and the scope distinctions above. The complete autonomous candidate was
frozen before an independent agent was assigned its check. That report is
`AUTONOMOUS_ONE_SAMPLE_CHECK.md`; its result is recorded in the study README.
The bracket calculation and probability details here are coordinator
derivations, not claims of additional external review. These are study-level
checks, not promotion reviews or changes to the paper's theorem statements.
