# Bounded feasibility audit of a genuine Eulerian histogram pilot

2026-09-27. Scoped internal design audit. Inputs were the complete aggregate
construction, `block_scalar_closure.py`, and `circle_tasks.py`. No training,
timing benchmark, reference trajectory, or other study was inspected or run.
The estimates below are arithmetic and mechanism analysis, not measurements.

## Recommendation and scope

A generic listed two-input task at k=1, H=1 requires eight histogram axes:
g,w1,w2,c,A1,A2,B1,B2. Both training directions span the input plane, so
there is no frozen perpendicular weight to remove. Five nodes per axis is
executable in principle but spatially very coarse; seven per axis already
needs 5,764,801 masses. A failure of that grid would be inconclusive about
the aggregate construction.

If a single-direction circle task is permitted, use one input u=(1,0),
label y=1, and evaluate predictions on the entire circle. Equivalently an
antipodal pair with odd labels reduces to this same problem. This is a new
explicit task simplification: none of the listed `TASKS` has one input.
It retains moving first-layer features, readout learning, both nonlinear
layers, learned middle feedback, and the joint correlation with the frozen
Gaussian middle weight. It does not test cross-sample geometry or k>1 block
mixing. The k=1 transpose is still the actual transpose, but is scalar.

The latter problem has an exact five-axis reduction and a plausible
9-to-13-node-per-axis pilot under a 60-second trajectory limit. Do not claim
the limit is guaranteed without a measured run. Stop inconclusive if the
deadline, boundary checks, or refinement checks fail.

## Exact single-direction reduction

Write w=(x,eta). Training changes only x; eta remains an independent
standard Gaussian and need not be an evolving histogram coordinate.
There are two exact law symmetries:

* (g,c,A) maps to (-g,-c,-A), with x,B unchanged.
* (x,eta,c,A,B) maps to (-x,-eta,-c,-A,-B), with g unchanged.

They permit folding the independent initial g,x into half-normal laws and
using g,x,c,a=-A nonnegative. Introduce b=B/L, which stays in [0,1]. The
Eulerian state is the joint histogram p(g,x,c,a,b), plus L. Define

    h = tanh(x)
    S = E[b*h]
    z = g*h + 2*a*S
    t = tanh(z)
    d = c*(1-t*t)
    f = E[c*t]
    M = E[a*d]
    r = f-y,  rho = abs(r).

The exact reduced velocities are

    g' = 0
    x' = -2*r*(1-h*h)*(g*d + 2*b*M)
    c' = -2*r*t
    a' = -r*d
    b' = rho/L*(h-b)
    L' = rho.

Initially c=a=0, b=tanh(x), L=1. For y>0 the exact solution has r<=0:
the surface f=y consists of equilibria, and local uniqueness prevents
crossing it. Thus x,c,a remain nonnegative. At b=0 the b drift is inward,
and at b=1 it is inward. For the exact reachable solution b<=h and its
drift is nonnegative, but a Cartesian histogram develops masses off that
submanifold. Therefore the numerical b flux must allow BOTH signs; do not
hard-code nonnegative b velocity.

This is a change of coordinates of the continuous law before discretizing.
Its finite grid is a genuine conservative scalar aggregate ODE, although
it is not literally the uniform-grid ODE in the original B coordinate.
Grid nodes remain fixed and only their masses evolve.

## Passive circle evaluation

Do not substitute E_eta[h1] inside the second tanh. Both nonlinearities
must be integrated over the frozen independent Gaussian coordinate.
For direction (cos(theta),sin(theta)), write

    h_theta(x,eta) = tanh(x*cos(theta) + eta*sin(theta))
    S_theta = E_p[b * E_eta[h_theta]]
    f_theta = E_p[c * E_eta[tanh(g*h_theta + 2*a*S_theta)]].

Fixed Gaussian quadrature integrates eta. It is initialization/evaluation
quadrature, not an independently evolving population. First marginalize
p to sum_{g,c,a}(b*p) as a function of x for S_theta, and to
W(g,x,a)=sum_{c,b}(c*p) for f_theta. This leaves only three active grid
axes inside the circle evaluator and avoids a full five-dimensional
tensor for each angle and eta node. Quadrature-order comparison is cheap
and must be distinguished from histogram resolution comparison.

## Initialization and references

The population construction requires c=0. The supplied `initial_pool`
instead uses c~N(0,1)/width. At width 2048 this is small but nonzero, and
it breaks the exact sign folding of a particular empirical realization.
Use c=0 for BOTH the population pilot and its comparison when claiming
this exact reduction. Otherwise retain a full signed grid and histogram
that same empirical initialization.

For the reduced population pilot, use known half-normal CDF cell masses,
not finite-width pool frequencies. The joint initial (x,b) mass can be
integrated exactly at cell level: intersect the x-cell interval with the
inverse-tanh image of the b-cell interval, then take the half-normal CDF
difference. Multiply by the independent g-bin probabilities. Handle
cutoff tails explicitly and report their omitted mass. This avoids
rounding a coarse representative set and calling it exact population
initialization. All seed quadrature nodes are discarded before training.

A width-2048 moving-block calculation is a reference only, never the
aggregate candidate. Its initialization sampling error is separate from
histogram error. A population histogram versus one empirical pool cannot
attribute every observed difference to spatial discretization. For a
strict matched-empirical comparison, initialize the histogram by binning
that same pool once, discard it from the candidate, and compare against
the original pool evolved separately. That validates finite-empirical
transport approximation, not population accuracy. Finite-width noise is
not established just by saying its formal scale is width^{-1/2}.

## Storage and arithmetic estimates

Float64 costs are listed below. Twelve full-length buffers are an example
implementation estimate; broadcasting and staged contractions can need
fewer. They are not a promised peak-memory measurement.

| Dimensions | Nodes per axis | Masses | One mass array MiB | Twelve arrays MiB |
|---|---:|---:|---:|---:|
| 5 | 9 | 59,049 | 0.45 | 5.41 |
| 5 | 13 | 371,293 | 2.83 | 33.99 |
| 5 | 17 | 1,419,857 | 10.83 | 129.99 |
| 8 | 5 | 390,625 | 2.98 | 35.76 |
| 8 | 7 | 5,764,801 | 43.98 | 527.78 |

With one static g coordinate there are four or seven dynamic flux axes.
A rough traffic model of eight scalar reads/writes per active axis gives
0.095 GB per RHS for 13^5 and 2.583 GB per RHS for 7^8, before field
evaluation, temporary arrays, reductions, or time integrator stages. At
an illustrative effective 5 GB/s these alone cost about 0.019 and 0.517
seconds per RHS, respectively. This is a conditional scaling estimate,
not a hardware benchmark. Hundreds of 7^8 RHS calls are unlikely to fit
60 seconds; hundreds of 13^5 calls may fit. Tanh evaluation and tensor
allocation can dominate over this simple model.

## Conservative implementation

Use sparse broadcast coordinate arrays, not meshgrid-expanded coordinates.
For the reduced system, h depends only on x and tanh(z) only on g,x,a.
Obtain S,f,M by contractions of the current mass tensor and broadcast the
resulting lower-dimensional field factors. Stream one coordinate's flux
at a time, retaining no dense N-by-d velocity or neighbor matrix.

For uniform spacing h_j the exact semidiscrete scheme is
outgoing positive and negative flux p_i*(v_ij)^+/h_j and
p_i*(-v_ij)^+/h_j to fixed neighboring cells. Add the same edge transfer
with opposite signs at its two endpoints. This gives conservation by
construction. Enforce no outward flux at physical or stated cutoff
boundaries and monitor mass near any artificial cutoff.

Forward Euler with dt*max_i(sum_j |v_ij|/h_j)<=0.8 preserves positivity;
SSP-RK2 preserves it under a checked CFL bound at BOTH stages. An ordinary
adaptive RK tolerance is not a positivity guarantee. Splitting the flux
by coordinate is an approximation to this ODE and introduces a separate
time error; it should not silently replace the defined solver. Time-step
refinement, grid refinement, seed integration, and query quadrature are
distinct error axes.

For a short predeclared clock interval L<=1+s_max, exact c<=2*s_max and
a<=s_max^2. With a seed cutoff x0<=x_cut and g<=g_cut, define
F(x)=x/2+sinh(2*x)/4. The continuous reduced solution satisfies

    F(x)-F(x0) <= 2*g_cut*s_max^2 + 2*s_max^4.

This follows by multiplying x_s<=sech(x)^2*(4*g*s+8*s^3)
by cosh(x)^2 and integrating. It gives principled finite boxes for a
clock-capped pilot. Histogram diffusion can still reach the artificial
boundary, so the boundary-mass gate remains necessary.

Numerical validity gates should include conserved mass, minimum mass,
cutoff-boundary mass, finite fields and clock, no deadline overrun,
matched stop rule, and at least one resolution comparison before a result
is called good enough to authorize the wider task branch. A coarse-grid
fit alone establishes neither circle accuracy nor hierarchy convergence.
