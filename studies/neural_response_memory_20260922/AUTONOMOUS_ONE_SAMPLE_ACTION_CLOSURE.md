# An explicit autonomous one-sample response closure

2026-09-22. The user explicitly authorizes a hypothetical law of motion for
the learned middle matrix's forward and backward actions, with the rest
derived from canonical one-sample gradient flow. This continues the current
response-state investigation. It replaces the earlier incomplete illustrative
acceleration laws with an actual specified approximate response model.

This is a construction, not evidence of accuracy or an exact compression of
the original network. There are no training experiments or external sources.

## Canonical equations and state

Equal widths n, fixed nonzero sample x in R^d with scalar label y, loss
(f-y)^2, block mobilities (W1,W2,W3)=(n,1,n). Use <u,v>=u^T v/n,
chi=||x||^2/d, and componentwise products where indicated. The activation is
at least C^3 for local Lipschitzness of the displayed closed vector field.
The actual initialized operator W0=W2(0) and its transpose are retained.

For the original network:

    h=phi(z1), z2=W2 h, h2=phi(z2), f=<W3,h2>, r=f-y,
    delta=W3 .* phi'(z2), b=W2^T delta,
    delta1=phi'(z1) .* b,
    z1'=-2r chi delta1, W3'=-2r h2,
    W2'=-2r delta h^T/n.

Introduce two n-vectors A and B, targeting respectively

    A=DeltaW h, B=DeltaW^T delta, DeltaW=W2-W0.

In the surrogate these are independent stored response coordinates, not
matrix products with a stored learned matrix. The complete evolving state
is (z1,W3,A,B), of dimension 4n. Reconstruct the current fields algebraically:

    h=phi(z1), z2=W0 h+A, h2=phi(z2),
    f=<W3,h2>, r=f-y,
    delta=W3 .* phi'(z2),
    b=W0^T delta+B, delta1=phi'(z1) .* b.

For one sample, storing z1 suffices in place of W1: the components of W1
orthogonal to x do not affect the sample and do not move under its gradient.

## Exact identities before approximation

Let p=h' and q=delta'. The product rule gives

    A'=-2r delta <h,h> + DeltaW p,
    B'=-2r h <delta,delta> + DeltaW^T q.

The velocity actions have two exact scalar pairings:

    <delta,DeltaW p>=<B,p>,
    <h,DeltaW^T q>=<A,q>.

Thus only their components orthogonal to delta and h, respectively, are
undetermined by these pairings. This observation identifies a precise
place to impose the authorized hypothetical response law.

## The single closure assumption

Set those two orthogonal components to zero:

    DeltaW p  approximately T=delta <B,p>/<delta,delta>,
    DeltaW^T q approximately S=h <A,q>/<h,h>.

The approximation is a modeling choice, not a consequence of finite state
sufficiency. Equivalently, T and S are the unique minimum Euclidean norm
vectors obeying the respective scalar pairings. To prove this, decompose
any feasible T as delta <B,p>/<delta,delta> + T_perp with
<delta,T_perp>=0. Its squared norm is the squared norm of the first term
plus ||T_perp||^2, minimized uniquely by T_perp=0. The other case is identical.

This is an action approximation, not a claim that the true learned matrix
has small rank or that the neuron trajectories are independent.

## Complete autonomous evaluation order

At any current state with <h,h>>0 and <delta,delta>>0:

    1. Compute all algebraic fields above.

    2. z1'=-2r chi delta1,
       W3'=-2r h2,
       p=phi'(z1) .* z1'.

    3. A'=-2r delta <h,h> + delta <B,p>/<delta,delta>.

    4. z2'=W0 p+A',
       q=W3' .* phi'(z2)+W3 .* phi''(z2) .* z2'.

    5. B'=-2r h <delta,delta> + h <A,q>/<h,h>.

Return the four derivatives (z1',W3',A',B'). All intermediate values depend
only on the current state, fixed W0, x and y. There is no implicit derivative
loop, externally supplied residual, historical trajectory, missing terminal
action, or learned n-by-n matrix.

Initialization is explicit:

    z1(0)=W1(0)x/sqrt(d), W3(0)=original initialized readout,
    A(0)=0, B(0)=0.

The initial z2, delta and backward fields are computed by the algebraic
readout. Their initial derivatives agree with the canonical network because
both omitted velocity actions are zero when DeltaW=0.

## Preserved identities

Define the scalar compatibility defect C=<delta,A>-<h,B>. Differentiating
with the displayed closed equations gives

    C'=<q,A>-2r<delta,delta><h,h>+<B,p>
       -<p,B>+2r<h,h><delta,delta>-<A,q>=0.

Therefore C=0 for the prescribed initialization. This is the necessary
instantaneous adjoint identity of the two stored actions. For nonzero h,
delta, it also suffices for existence of some instantaneous matrix giving
those two actions. For example, using ordinary unnormalized products, one
such matrix is

    A h^T/(h^T h) + delta B^T/(delta^T delta)
      -delta (delta^T A) h^T/[(delta^T delta)(h^T h)].

This matrix is only a realizability witness and is never stored or used by
the surrogate. Its existence makes no assertion about the rank or dynamics
of the true learned matrix.

For the output, differentiate f=<W3,phi(z2)>:

    f'=-2r<h2,h2>+<delta,W0 p+A'>
       =-2r[<h2,h2>+<h,h><delta,delta>]+<W0^T delta+B,p>
       =-2r[<h2,h2>+<h,h><delta,delta>+chi<delta1,delta1>].

The second equality uses the scalar pairing enforced by the forward closure.
The last uses p=-2r chi phi'(z1)^2 .* b. Consequently

    ((f-y)^2)'=-4r^2[
        <h2,h2>+<h,h><delta,delta>+chi<delta1,delta1>] <= 0.

All four state derivatives vanish at r=0. These are genuine identities of
this explicitly approximate system; matching this scalar dissipation law
does not prove matching predictions or states of the original network.

For width n=1 on the nondegenerate domain, the scalar constraints determine
the whole transport actions, so the closure is exact. This check does not
extend to larger widths, where orthogonal components exist.

## Limits of the construction

The model is locally an autonomous ODE on the open domain
<h,h>>0, <delta,delta>>0. C^3 activation gives local Lipschitzness there.
No global existence or invariance of this domain is established. Assigning
0/0=0 at a degenerate population is not a justified continuous extension.

It uses rational functions of current moments and the canonical activation
and derivatives. This is not a claim of rational trajectories in time.
Zero residual is an equilibrium; universal trajectory plateau or convergence
to zero loss has not been proved.

Only the scalar pairings needed for the displayed response equations and
loss identity are imposed. A single matrix realizing the four simultaneous
actions on h,p and delta,q would also require, among other consistency
conditions, <q,T>=<p,S>. That is not generally enforced. In particular this
is not a proof that a matrix evolving by the original rank-one update
produces these approximate response trajectories. Do not upgrade the
instantaneous A/B realizability statement to that stronger claim.

There are 4n evolving real coordinates and ordinary current population
contractions. Retaining the dense W0 still costs n^2 storage/work in a
direct implementation; the construction compresses learned state and its
history, not the authorized initialized operator. No empirical usefulness,
population limit, or error bound is claimed.

## Internal check provenance

Root derived the action identities, scalar projections, sequential closed
system and invariant/dissipation calculations from the canonical equations
in COUPLED_CURRENT_STATE_SYNTHESIS.md. Established notation files were
hash-checked unchanged; relevant workflow and skills were read. A fresh
prompt-only scoped agent, closed_action_model_check, independently verified
the projections, non-circular evaluation order, adjoint invariant, scalar
loss identity, residual-zero stationarity and n=1 check. It explicitly
identified the unforced additional cross-pairing and zero-denominator
limitations, incorporated above. This is a collaborative internal algebraic
check, not a promotion review. No experiments, web sources, other studies,
maintained-code changes or Git-index writes were used.
