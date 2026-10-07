# Can the dimension-dependent power of log(n) be removed?

## Bottom line

This study does **not** yet prove either an autonomous sublinear-exponent
compressor or its impossibility for the requested deep feature-learning model.
The dimension-dependent exponent in an existing construction is not, by
itself, a storage lower bound. The calculations below explain precisely why
two tempting lower-bound arguments fail and identify a constructive mechanism
that avoids a spatial coefficient table, but still lacks a dynamics theorem.

## One shared target

Here n is dense hidden width, d the input dimension, m the number of training
examples, L the hidden depth, and delta the failure probability. Keep L >= 2,
nonlinear activations, genuinely evolving hidden features, Gaussian
initialization, the positive initialized feature-Gram gap and the admissible
small-label regime. Inputs have norm sqrt(d), with m >= d and actual linear
span R^d; they are not restricted to an orthogonal or low-rank configuration.

For the dense and compressed predictions, respectively f_n and f_comp, use

\[
\|f_{\mathrm{comp}}-f_n\|_*
=\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
 |f_{\mathrm{comp}}(t,x)-f_n(t,x)|.
\]

The requested accuracy is the dense model's self-variability scale with
probability at least 1-delta, including the endpoint. A deterministic
tolerance C/sqrt(n), a tolerance with positive or negative logarithmic
factors, and comparison to the actual random discrepancy of two runs must
be distinguished. No new identification of those scales is proved here.
The root-width cases below diagnose candidate proof routes; they do not
silently redefine the user's error contract. A generic n^(-1/2+o(1)) upper
bound can be larger than every root-width polylogarithmic envelope.

Count all retained instance-specific coefficients, moving state, fixed decoder
information and live workspace. Initialization may use the data and dense
initial weights, never the future trajectory. The representation must evolve
autonomously and restart from its own state. Fixed functions or Gaussian
expectations are not free oracles. Arbitrary-real bit packing is not a
compression theorem.

All asymptotics first fix the data, d,m,L, activation and confidence, then
let n grow. Constants may depend on those fixed quantities. An exponent
a(d) with a(d)/d -> 0 is an additional statement across dimensions, not a
uniform joint dimension/width bound.

## 1. What the spatial count proves—and what it does not

For a local polynomial degree k, the exact number of independent polynomial
restrictions to the sphere is

\[
\binom{d+k}{d}-\binom{d+k-2}{d}
=\Theta(k^{d-1})\qquad(d\text{ fixed}).
\]

Thus a full table at degree proportional to log(n) has size proportional to
(log(n))^(d-1). Working intrinsically on the sphere removes one exponent,
not a dimension-linear exponent. More importantly, this is a table count,
not a lower bound for arbitrary nonlinear representations. A function such
as sin(v^T x) has a nonlinear representation storing only v, irrespective
of the size of its polynomial expansion. It is an illustration of the
logical distinction, not a substitute trained-network construction.

A rigorous lower-bound route exists for bounded Lipschitz decoders or
finite-precision representations. If actual reachable neural snapshots
contain independently variable spherical-polynomial coefficient balls with
radius exp(-c k), for a fixed c>0 independent of n, then uniform worst-case approximation at root-width
accuracy forces at least a constant times
(log(n))^(d-1) real parameters with polynomially bounded descriptor range
and decoder sensitivity, or words
with O(log(n)) bits. The full proof is in LOWER_BOUND_ROUTE.md, sections 3–4.

**The coefficient-ball hypothesis is unproved for the neural model.** Neither
analyticity, a positive training Gram gap nor spanning inputs proves it.
Even a worst-case reachable ball would not automatically yield the required
high-probability Gaussian-initialization lower bound. Rare initializations
are not enough.

## 2. Why the variability scale changes the lower-bound problem

Suppose, conditionally, that there is a deterministic reference trajectory
f_infty and that the normalized complete-trajectory fluctuations
sqrt(n)(f_n-f_infty) are tight in the norm above. This means that for each
fixed confidence, a compact set of functions contains these fluctuations
with that confidence, uniformly in sufficiently large n.

At error C/sqrt(n), a finite fixed-accuracy cover of that compact set gives
a number of possible centers independent of n. Therefore fluctuations alone
cannot then force an increasing (log(n))^(constant times d) information bound
at that scale. This is **not** a compact autonomous evaluator: the centers
may themselves be very complicated complete trajectories.

A more quantitative conditional statement is useful. If the normalized
fluctuations have a width-uniform exponential spherical-mode tail, up to a
polylogarithmic envelope, then even tolerance
n^(-1/2)(log(n))^(-b), for a fixed b >= 0, needs only degree O(log log(n)).
The instantaneous spatial coefficient count is consequently

\[
O\bigl((1+\log\log(en))^{d-1}\bigr).
\]

For every fixed d this is smaller than every positive power of log(n).
Its constants and onset may be severe in d. No autonomous evolution of
those coefficients, no decoder for the deterministic learned predictor,
and no such actual-network fluctuation bound have been established here.
The statement concerns only the conditional spatial truncation, not total
compressed-model storage.

Proofs and exact qualifications: SCALE_AUDIT.md, sections 3–7, and
LOWER_BOUND_ROUTE.md, section 5. STRUCTURAL_CHECKS.md also proves directly
that a dense-vs-dense upper discrepancy bound yields an accurate deterministic
center by averaging ball probabilities, without saying that this center is
cheap to represent.

## 3. A constructive mechanism that avoids storing the spatial table

A high-dimensional Gaussian integral can be evaluated by visiting tensor
quadrature nodes one at a time. One retains the current source coordinates,
loop counters, an accumulator, and the integrand's program—not every node
and value. CONSTRUCTIVE_ROUTE.md proves a finite-bit workspace bound under
explicit moment, continuity and evaluator assumptions. Arithmetic work may
be enormous; no runtime efficiency is claimed.

This suggests storing a short causal program for the nonlinear Gaussian
training dynamics, and evaluating its expectations serially. If its program
length, coefficient count, precision and workspace were all bounded by a
power of log(1/epsilon) with exponent independent of d, then substituting a
root-width polylogarithmic tolerance would give a constant power of log(n)
in total storage. Every source-response coefficient and both orientations
of each reused matrix must be retained correctly.

**The necessary short-program theorem is missing.** It must provide all of:

- Controlled high-order evolution of the actual feature-learning state,
  with an appropriate norm and polynomial program-size bounds whose degrees
  do not grow with d.
- Whole-sphere error control, an autonomous restartable implementation, and
  stability through the fitted endpoint.
- A quantitative comparison to the actual finite dense reference at the
  selected variability tolerance as program order and horizon grow.

A fixed-number-of-steps Gaussian limit does not establish this. Neither does
the fact that a Gaussian integral is low-memory. A causal numerical history
is also not automatically a smooth autonomous ODE; that distinction is kept
explicit in the route report.

## Current conclusion

There is no justified impossibility claim below a dimension-linear power of
log(n) in this study, and there is no completed construction meeting all the
requested requirements. The most promising constructive branch here is an
implicit causal Gaussian program with counted evaluation workspace. The most
important negative finding is that generic analytic mode counting is not a
valid substitute for a lower bound on actual learned trajectories at their
own variability scale.

The exact auxiliary statements and conditional implications are retained with
their checks in this study. They have not been promoted to the maintained book
or used to replace any existing compression bound. No training experiment,
Git commit or modification of another study was performed.
