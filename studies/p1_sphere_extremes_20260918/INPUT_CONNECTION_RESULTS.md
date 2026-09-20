# Does input noise break a given bad training connection?

2026-09-18. Continuation of the same input-perturbation investigation.
These are study results, not established book material. No experiment or
finite-network replacement was used.

## The question now being answered

Take as a hypothesis that, at special input data X_0, canonical p=1
training converges in its physical Hilbert state space to a specified
positive-loss equilibrium. The question is whether almost every
arbitrarily small spherical input perturbation breaks that connection
and eventually makes the trajectory escape the nearby bad states.
Establishing which base connections occur is not the task here.

The preceding construction of PSD bad equilibria for freely perturbed
inputs does not refute this proposal. Their existence does not determine
whether the perturbed canonical trajectory approaches them. Equally,
destruction of the old fixed equilibrium does not settle the question:
the endpoint and its attraction set may move.

## A concrete p=1 theorem along the presumed connection

Keep the original seven equally weighted inputs on a common latitude:
three positives at angular positions 0, 2pi/3, 4pi/3 and four negatives
at pi/4, 3pi/4, 5pi/4, 7pi/4. The exact normalized input convention is

\[
 x_i=\sqrt3(C,S\cos\alpha_i,S\sin\alpha_i),
 \qquad C,S>0,\quad C^2+S^2=1.
\]

Use the canonical correlated Gaussian carriers, full p=1 dictionary,
odd invariant sector, all trained blocks and physical gradient metric.
Let theta=(w-g,c,M). The specified old bad state has

\[
 w_*=a\operatorname{sign}(q\cdot b_1)e_1,\quad
 M_*=e_1q^T,\quad a>0,\quad q\ne0,
\]

with the bounded odd readout c_* depending only on b_{2,1}, predicting
-1/7 at all seven inputs and having every backward vector d_i=0.
Its loss is 48/49. All first-layer dictionary moments and effective
second-layer vectors coincide across the seven inputs. Its actual
Hilbert loss Hessian is rank-one PSD.

**Assume the canonical trajectory at X_0 converges strongly to this
state.** For tangent input perturbations xi_i set

\[
 x_i(\epsilon)=
 \frac{x_i+\epsilon\xi_i}
      {\sqrt{1+\epsilon^2|\xi_i|^2/3}},\qquad
 \rho_i=(-1/7-y_i)/7.
\]

If sum_i rho_i xi_{i,1} is nonzero, the first input response exists at
every finite time and satisfies

\[
 \boxed{\displaystyle
 \sup_{t\ge0}
 \left\|\left.\frac{\partial\theta_{X(\epsilon)}(t)}
                    {\partial\epsilon}\right|_{\epsilon=0}
 \right\|_{\mathcal H}=\infty.}
\]

The excluded directions form one proper hyperplane in the
fourteen-dimensional tangent space. Thus the conclusion holds for
almost every tangent direction. It has no exceptional positive a
values, including the two amplitudes excluded by the earlier local
strict-saddle argument. It concerns the original single-amplitude
endpoint, not every later multi-amplitude construction.

In particular the entire perturbed training trajectory cannot stay
within K|epsilon| of the base trajectory for one fixed K and all times,
uniformly for sufficiently small epsilon. This is an actual dynamical
conclusion under the stipulated base connection, not only a derivative
of the field at a frozen state.

The proof in [input_connection_response.md](input_connection_response.md)
derives the finite-time sensitivity from the exact closure. If Z is
that sensitivity, then Z'=A(t)Z+B(t), Z(0)=0. Strong base convergence
and d_i,*=0 imply operator-norm convergence of A(t) to the rank-one
negative loss Hessian. There is a readout direction orthogonal to the
common hidden feature, hence neutral for that limiting operator. The
limiting input force has a nonzero component in this direction exactly
when the displayed residual-weighted input displacement is nonzero.
If Z stayed bounded, its projection onto this direction would have a
derivative tending to a nonzero constant, a contradiction.

## The remaining nonlinear issue is real

Unbounded first response is weaker than escape from a fixed state
neighborhood. The displacement could eventually be of size
|epsilon|^(1/3), for example: much larger than |epsilon| but still
arbitrarily small, with convergence to a nearby bad endpoint.

[input_connection_response_example.md](input_connection_response_example.md)
proves this distinction in an explicit analytic square-loss gradient
system. It has a fixed nonstationary initialization, PSD bad equilibria,
cubic descent, and attainable zero-loss states. Its first input response
grows exactly like t, yet all perturbed trajectories remain uniformly
within |epsilon|^(1/3) and converge to nearby positive-loss equilibria.
This is a counterexample to the inference from response to escape,
**not a p=1 counterexample**.

The stronger geometric route is developed in
[input_basin_transverse.md](input_basin_transverse.md). At a strict-saddle
endpoint, a local joint trapping graph for data and state can be
constructed from the exact p=1 equations. If its defining constraint,
evaluated on a finite-time canonical trajectory, has a nonzero input
derivative, then almost every sufficiently small input perturbation
causes finite exit from that neighborhood. The derivative includes
both the accumulated trajectory response and the movement of the
trapping graph. The report proves the implication and the required
finite-time sensitivity; it does not verify that nonzero derivative
for the canonical p=1 bad connection. PSD endpoints additionally need
a nonlinear local trapping or escape argument.

Countably many joint trapping neighborhoods can cover an uncountable
set of endpoints. To exclude every later bad convergence, the
transverse-intersection condition must control every possible trapped
tail. A single local exit does not exclude reentry or convergence to a
different bad state. No claim about loss tending to zero follows yet.

## Two further restrictions on a proof

[canonical_bad_reach.md](canonical_bad_reach.md) proves, still assuming
the stipulated strong base convergence:

* A bounded actual lower-field endpoint requires unbounded accumulated
  displacement from the initial Gaussian field. At an endpoint with
  d_i,*=0 the physical distance to the endpoint cannot be integrable
  over time. In particular the full state cannot converge exponentially
  to these endpoints. This does not rule out exponential convergence
  of the loss alone.
* Fix a sufficiently late entrance time of the base trajectory into a
  fixed endpoint neighborhood. If a perturbed trajectory subsequently
  exits that neighborhood, its first such exit time is at least
  c log(1/delta)-C for small input displacement
  delta. The constants depend on the base trajectory and neighborhood.
  This is a lower bound conditional on escape, not a proof of escape.

The separate symmetry observation in that report concerns one
particular carrier realization at a different positive-amplitude seed.
It is not used to answer the user's assumed-connection question.

## Disposition

The user's mechanism remains viable for p=1. The old equilibrium-existence
counterexample did not settle it. The new theorem verifies a generic,
unbounded first-order response of the entire presumed connection for
the original bad state. What remains unresolved is whether nonlinear
adjustment can absorb that response into a nearby bad endpoint, or
whether almost every input perturbation instead escapes. Neither
generic escape nor a canonical p=1 counterexample to it is claimed.

The README records complete proof/check versions and separates fresh
isolated review from informed cross-checks. No material was promoted.
