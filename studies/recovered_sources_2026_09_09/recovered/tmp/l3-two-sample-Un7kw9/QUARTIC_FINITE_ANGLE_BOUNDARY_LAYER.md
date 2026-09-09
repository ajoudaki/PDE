# Quartic gate: a finite-angle boundary-layer check

Status: unaudited main exact calculation. This is not a network
counterexample. It limits a proposed uniform POLYNOMIAL local response
estimate while leaving uniform Gaussian moment bounds possible.

For phi'(z)=1+e/(1+z^4), define the finite-angle pure-q channel as in
FINITE_ANGLE_Q_CHANNEL_ROUTE.md, with delta in (0,1], mu^2=1-delta^2:

    M_r=mu^2 b_delta(M,V), V_r=a_delta(M,V),
    b_delta=-4e M V(M^2+delta^2 V^2)/
              [(1+(M+delta V)^4)(1+(M-delta V)^4)].

On the exact solution M=0, write a(V)=1+e/(1+delta^4 V^4). The
initial common-coordinate linearization obeys

    d(log J)/dV
      =-4e mu^2 delta^2 V^3/
          [(1+delta^4 V^4)(1+delta^4 V^4+e)]
      =(mu^2/delta^2) d(log a(V))/dV.

Thus its Jacobian at fixed driver is exactly

    J=[a(V)/a(V0)]^(mu^2/delta^2).

There is no extra clock correction in this entry at M=0: a_delta is
even in M, so partial_{M0} V vanishes on this reference solution.
Since a(V) is maximal at V=0 and the flow traverses every V, the
largest common response from initial V0 is

    sup_r J=[(1+e)/a(V0)]^(mu^2/delta^2).                (1)

For |V0|>=1 choose delta=1/|V0|. Equation (1) becomes

    [(1+e)/(1+e/2)]^(V0^2-1).

This grows exponentially in V0^2, excluding a polynomial bound
simultaneously uniform over all finite angles and all initial states,
even though the exactly tangent delta=0 system may have such a
polynomial bound. This boundary layer is not seen by taking delta to
zero at a fixed V0.

The same formula nevertheless admits a useful Gaussian envelope.
Put u=delta^2 V0^2. For V0!=0, using log(1+x)<=x gives

    log sup_r J
       <= (V0^2/u) log[(1+e)(1+u^2)/(1+u^2+e)]
       <= e V0^2 u/(1+u^2+e)
       <= [e/(2sqrt(1+e))] V0^2.                       (2)

For V0=0 the response is at most one and the bound is immediate.
Therefore this particular uniform-angle Jacobian entry has a finite
p-th moment under Gaussian V0 of variance v whenever

    p e v/(2sqrt(1+e)) < 1/2.

At fixed e=1/10 and v=1 this includes p=4. This is only one entry on
the zero-common-coordinate orbit, not the entire finite-angle
Jacobian and not any coupled-network response. The field example
M0=0 is also not the canonical near-coincident initial common field,
which has nonzero Gaussian variance. The calculation invalidates the
general deterministic polynomial-envelope shortcut, not the user goal.
