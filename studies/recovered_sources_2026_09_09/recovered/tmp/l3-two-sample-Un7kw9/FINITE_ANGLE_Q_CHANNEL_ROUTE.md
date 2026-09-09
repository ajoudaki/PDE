# Exact finite-angle pure-contrast driver: partial main derivation

Status: unaudited partial result. This controls a local two-coordinate
channel, not the full trained network. It extends the pure-driver
tangent calculation currently being written by Dirac. The fixed-driver
Jacobian estimate described at the end still needs its detailed proof.
No theorem promotion or activation choice is made here.

Fix e>0 and phi(z)=1+z+e arctan z. Write
delta=sqrt((1-rho)/2), mu^2=1-delta^2, so 0<delta<=1. The formulas also
have a continuous tangent interpretation at delta=0. For one neuron put

    a(M,V)=[phi'(M+delta V)+phi'(M-delta V)]/2,
    b(M,V)=[phi'(M+delta V)-phi'(M-delta V)]/(2delta).

The pure common-backward-input channel in normalized bottom coordinates
is the autonomous flow

    dM/dr=mu^2 b(M,V),       dV/dr=a(M,V),                (1)

where r is the integrated scalar driver. Its sign may be arbitrary.
The omitted independent common-channel forcing is stated below. This
coordinate reduction retains the raw input Gram metric; it is not two
independent copies of the one-sample F transform.

Since 1<=a<=1+e, V is strictly increasing with r, ranges over all R on
a globally defined flow, and can be used as coordinate along (1).
The first equation has smooth coefficients and at most linear growth
in M,V, so global existence also follows directly on every finite r
interval from |b|<=2e|V|. For M_0=0, M remains zero. For M_0!=0 its
sign is invariant, by the multiplicative equation below.

Set X=M^2, Y=V^2, and Z=delta^2 Y. Exact subtraction gives

    b=-2e M V/[(1+(M+delta V)^2)(1+(M-delta V)^2)],
    dX/dY=-2e mu^2 X/F(X,Z),
    F(X,Z)=(1+X+Z)(1+X+Z+e)-4XZ.                       (2)

The passage through V=0 is justified by the smooth equation
dM/dV=-2e mu^2 M V/F(M^2,delta^2 V^2), an even-in-V scalar flow
when parameterized by Y. Its solution m(Y) with m(V_0^2)=M_0 obeys

    dm/dY=f(m,Y)=-e mu^2 m/F(m^2,delta^2 Y).             (3)

Two useful denominator identities are

    F=(X-Z-1)^2+4X+e(1+X+Z),
    F=(X-Z)^2+(2+e)(X+Z)+1+e.

Thus F>=4X, F>=1+e, and F>=c_e(1+X). Consequently

    -e mu^2/2 <= dX/dY <=0,
    sup_{r in R} M(r)^2 <=M_0^2+(e mu^2/2)V_0^2.         (4)

The maximum occurs at Y=0. This conclusion requires no sign assumption
on the driver times the contrast, and holds uniformly in the angle.

## Response at fixed terminal contrast

Let J(Y)=partial m(Y)/partial M_0 with V_0 and delta fixed. Smooth
scalar ODE differentiation gives J>0 and

    J'=f_m J,
    f_m=e mu^2[-F+2X F_X]/F^2,                         (5)

where F_X is differentiated with Z fixed. The lower bound

    f_m >= -e/(1+e)                                    (6)

is uniform in X,Z>=0. If F_X>=0, it follows from F>=1+e. If F_X<0,
put u=Z-X>1+e/2 and A=1+e/2. Then

    D=(u+1)(u+1+e),  F=D+4AX,  F-2X F_X=D+4uX.

Expansion gives

    F^2-(1+e)(F-2X F_X)
      =D[D-(1+e)]+[8AD-4u(1+e)]X+16A^2X^2 >=0.

Indeed D>=1+e and 2AD>=4A^2u>=(1+e)u. This proves (6).
For 0<=Y<=V_0^2, integrating backwards therefore gives

    J(Y)<=exp[e V_0^2/(1+e)].                           (7)

For Y>=V_0^2, use the forward decrease of X. For M_0!=0,
positive parts in (5) and (2) give

    integral_{V_0^2}^Y (f_m)_+ dY
       <= integral_{X(Y)}^{X_0} (F_X)_+/F dX.           (8)

Here the integrand follows the actual trajectory Z(Y), but can be
bounded uniformly over Z. The second identity for F implies
|X-Z|<=sqrt(F). Hence

    |F_X|=|2(X-Z)+2+e|<=C_e sqrt(F),
    |F_X|/F<=C_e/sqrt(1+X).

Inserting this in (8) gives

    J(Y)<=exp[C_e(sqrt(1+M_0^2)-1)]
           <=exp(C_e|M_0|),       Y>=V_0^2.             (9)

If mu=0 then m is constant and J=1; if M_0=0 the scalar linearization
has f_m=-e mu^2/F(0,delta^2Y)<=0, so (7),(9) hold directly. Combining
the cases yields the angle-uniform fixed-terminal-contrast estimate

    sup_{Y>=0} J(Y)
      <=exp(C_e|M_0|)+exp[e V_0^2/(1+e)].               (10)

For jointly Gaussian initial coordinates this right side has a finite
p-th moment whenever p e Var(V_0)/(1+e)<1/2. A linear exponential in
|M_0| does not change the strict Gaussian quadratic-moment threshold;
condition on V_0 and use the one-dimensional Gaussian density, or
absorb linear terms into an arbitrarily small additional quadratic.
Equation (10) concerns fixed terminal contrast, not yet fixed driver.

## Missing clock step and canonical forcing

The correct signed-driver clock is

    r=integral_{V_0}^V dv/a(m(v^2),v).                  (11)

Its differentiation involves integrals of a_M times J. To make the
bound uniform in delta, a plausible explicit decomposition is:
for delta<=1/2, (4) bounds |m| by B=1+|M_0|+sqrt(e)|V_0|,
and F<=C_e B^4 while |v|<=1/delta. Thus
|m(v^2)|<=|m(0)| exp(-c_e v^2/B^4) on that interval. For larger v,
|m| cannot increase and already has exp(-c_e/(delta^2 B^4)) decay.
After |v|> (2B+1)/delta, the odd-in-M difference expression gives
|a_M|<=C e|m|/(delta |v|)^4. The exponential beats the remaining
inverse-delta integral lengths. For delta>=1/2 one can split directly
at |v|=2(2B+1) and integrate the rational tails. This should yield a
polynomial-in-B bound on integral |a_M|dv, and then a fixed-driver
Jacobian bound using (10). This paragraph is a route, NOT a completed
uniform Jacobian proof. Its constants, initial-time derivatives, and
both components of the clock inversion must still be verified.

The actual normalized first-layer equation in rescaled feature time
u=delta s contains a second driver. With q=q_M^(1) and
p=q_D^(1)/delta it is exactly

    M_u=mu^2(a p+b q),    V_u=a q+delta^2 b p.            (12)

Thus (1) captures only the q vector field. Trained higher operators
also add their rank-update forcing to the other layers. Neither (10)
nor an eventual fixed-driver estimate controls arbitrary late p-channel
injections: a strongly contracting q flow can have a large inverse
derivative on driver reversal. Perturbing the external q driver alone
only changes its total integral and is a different, easier response.
No full-network continuation follows until these distinctions are
resolved for actual canonical responses.

One further exact affine observation may help that task. In the
opposite-label affine baseline (overall label sign absorbed into C),
updates (W^(2))'=[(W^(3))^* C] tensor D_1 and
(W^(3))'=C tensor D_2 have odd range and odd input under sample exchange.
They annihilate the even common features. Consequently all three affine
common preactivation fields are frozen at initialization; the growing
trained operator part lies in the odd sector. In the nonlinear model,
the even-sector updates are delta_D tensor H_M. Their actual response
control, not a bound on the entire operator by its growing odd sector,
is a more precise next universal-angle obligation. This observation
needs no assertion that finite coordinates are independently paired.
