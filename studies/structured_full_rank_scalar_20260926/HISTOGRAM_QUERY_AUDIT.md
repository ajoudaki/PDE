# Single-input histogram folding and query audit

2026-09-27. Scoped internal mathematical/code audit, with no training runs.
Read only the authorized first-experiment section of this study's README,
`AGGREGATE_SCALAR_CONSTRUCTION.md`, `HISTOGRAM_FEASIBILITY.md`,
`block_scalar_closure.py`, and `run_histogram_candidate.py`. The C++ core
was still under construction and was not audited here. This is not an
independent promotion review.

## Mathematical result

The five-axis reduction, Python characteristic RHS, Gaussian seed rules,
and full passive-circle query are consistent with the original k=1, H=1,
one-input closure. Both reference and candidate use population c=A=0.
Their fitting endpoints target the same first MSE 0.01 crossing. No
reference trajectory or reference prediction enters the tested RHS.

Let sigma be the initial sign of the scalar Gaussian middle weight and
tau the initial sign of the training component of the first weight. For
a folded block (g,x,a,c,b), an original signed block is

    G = sigma*g,
    w = tau*(x,eta),
    A = -sigma*tau*a,
    c_original = sigma*tau*c,
    B = tau*L*b.

Initially the signs are independent of the two half-normal magnitudes;
eta is still an independent standard Gaussian after multiplication by
tau. Training has no perpendicular velocity. The original joint dynamics
preserve these orbits. In particular, with h=tanh(x), t=tanh(g*h+2*a*S),
S=E[b*h], and D=E[a*c*(1-t*t)], the original forward and transpose
contractions give

    x' = -2*r*(1-h*h)*(g*c*(1-t*t)+2*b*D),
    a' = -r*c*(1-t*t),
    c' = -2*r*t,
    b' = abs(r)/L*(h-b),
    L' = abs(r).

The plus sign and factor 2 in both feedback terms are required. The
quotient derivative in b includes the clock derivative; no residual L
factor belongs in the folded z2 or transpose feedback. The implementation
has these signs and normalizations.

For an unseen angle theta, put

    h_theta = tanh(x*cos(theta)+eta*sin(theta)),
    S_theta = E[b*h_theta],
    f_theta = E[c*tanh(g*h_theta+2*a*S_theta)].

The same eta remains inside both nonlinearities. Its expectation may be
taken first when forming S_theta, but cannot replace h_theta inside the
second tanh. `characteristic_predict` performs the complete integral.
The 32/64 comparison checks this passive quadrature separately from the
48/80/(128) Gaussian seed-rule comparison.

An independent algebraic check expanded a three-point, nonuniformly
weighted folded law into all four sign orbits and 32 perpendicular
Gauss-Hermite nodes, then directly evaluated the original formulas.
Maximum transformed velocity discrepancy was 2.220446049250313e-16;
maximum complete-query discrepancy over nine angles was
2.7755575615628914e-17. This check did not evolve a trajectory.

## Fairness and scope

The grid initialization uses exact half-normal probabilities for g and x
cells, followed by the declared node evaluation/interpolation of tanh(x)
onto b. This is a stated initial discretization approximation; it is not
the exact joint (x,b) cell probability suggested as an alternative in the
earlier feasibility note. The last cells include all upper-tail mass.
These choices are fixed before results and are legitimate parts of the
aggregate candidate error.

Both sides are the same k=1/H1 population memory model. Gaussian
characteristics are only the separately resolved numerical reference.
An accuracy result here does not test k16 block mixing, nonparallel
training geometry, higher memory order, or a dense Gaussian limit.
The numerical convergence gates are empirical resolution checks, not
certified uniform quadrature error bounds.

## Actionable findings sent to the supervisor

The initial 337-line driver version had these process gaps:
its SHA-256 was
`b60bab107ecf5bff6000b961a05763e50353da9c3f18ea8f99d5eb89edefece7`.

1. It checked the 60-second complete-trajectory ceiling only after both
   unrestricted passive prediction passes. The reference's 50-second
   training exception also escaped without saving its accepted partial
   state. Enforce the full deadline during passive work and preserve the
   last accepted reference state on a training timeout.
2. Its early reference gate checked only the selected rule's fitted flag
   and seed-rule difference. It could start histogram training after the
   selected reference had already failed passive quadrature or total
   runtime validity. Require those known validity checks before starting
   histograms, and require that both rules used in the final seed-rule
   comparison fitted at the declared endpoint.
3. The mixed-law engineering check asserted conservation and positivity
   only. Its comment claimed a check of current-mass reductions, which
   those assertions do not establish. Compare the mixed-law first
   coordinate moments and passive queries against the weighted
   characteristic formulas to test that claim.

These are findings about the inspected driver version, not assertions
that subsequent supervisor edits remain defective. C++ flux signs,
both-stage CFL enforcement, taper bookkeeping, and accepted-state event
interpolation require the separate core audit.
