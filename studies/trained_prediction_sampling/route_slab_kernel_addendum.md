# Source interval audit: moment closure and the Borel influence kernel

Comparison-phase addendum by `/root/weak_topology_route`, 2026-09-11.
The frozen independent reconstruction is `route_slab_audit.md`, SHA-256
`3434adc3727e693d514d03911f1d08a2015c62e41e5645a5065ff8143fb3596c`.
After that reconstruction was frozen, the supervisor authorized reading the
complete `route_source_second_phase.md`, SHA-256
`b3c45efde1fc4b22e16b0f49ebf8c0fadf0efdd8146b4dc0400c9fbc6631002e`.
Its interval argument agrees with the independent reconstruction. This
addendum records two remaining checks; it changes neither frozen report.

## Finite moment-order closure

The interval length does not have to work simultaneously for infinitely many
moment exponents. The absorption norm E contains only deterministic quantities:
covariance entry suprema, coefficient absolute row sums and residual derivatives.
Their expectation estimates use a finite collection of source tensor orders
and finite Hölder exponents. Choose ell for precisely that finite collection.

After E is bounded, the explicit lower response equations yield every separately
fixed finite Lp bound using the random integrating factor from N11 and a finite
induction in source order. These higher Lp estimates have larger constants, but
no term needs to be reabsorbed: E is now a known deterministic bound. Hence they
do not require smaller intervals. Upper explicit response source tensors are
bounded pointwise by the deterministic Volterra estimate.

At first law order the deterministic closure needs explicit source tensors
through order three. Their estimates can involve higher finite moments of
lower tensor orders, but the source order strictly decreases in that induction.
Thus, for each requested p, the resulting list of Hölder exponents is finite.
At second law order, explicit second response tensors through order one suffice;
the known first-response tensors through order three and base tensors through
order five control all covariance contractions. Again there is no infinite
moment or source-order induction in the coefficient of ell E.

The constants multiplying ell E depend on the base N-cap constants, T, and
the fixed moment/source orders. Old response data enter additively through
their already known norms. Since the number of intervals is fixed once ell
is chosen, growth in these known norms is finite and independent of mesh size.

## From finite-law derivatives to a Borel atom influence

Use H=L2 of the normalized circle, at the requested time T=40. The same
construction of the derivative works with the continuous time/input output
space when the value convergence is uniform there; only the statistical CLT
distinction at the end changes.

Let `K_r={mu:W1(mu,nu*)<=r}` and choose positive radii r<r1 within the
neighborhood where the uniform finite-program derivative bound holds.
The probability-law space on the compact data domain is compact in W1,
and K_r is closed. Convexity of a W1 ball follows by mixing couplings to nu*.
Take eps0>0 so that every contamination
`(1-eps)mu+eps delta_z`, mu in K_r, 0<=eps<=eps0, belongs to K_r1.
For example any eps0 with `eps0 D_Y<r1-r` works.

At each fixed mesh h, the raw Euler map extends continuously in W1 to every
Borel law by the joint continuity of NF and finite induction. Its output is
therefore a continuous H-valued function F_h on K_r1. The finite-law first
and second derivative estimates give, for the centered atom derivative,

\[
 G_h(\mu,z)=D F_h(\mu)[\delta_z-\mu],\qquad
 Q_{h,\epsilon}(\mu,z)
 ={F_h((1-\epsilon)\mu+\epsilon\delta_z)-F_h(\mu)\over\epsilon},
\]
\[
 \|Q_{h,\epsilon}(\mu,z)-G_h(\mu,z)\|_H\le2C\epsilon,
 \qquad \|G_h(\mu,z)\|_H\le2C.                            \tag{1}
\]

Indeed the direction has TV at most two, and the integral Taylor remainder
is at most `(C/2)epsilon ||delta_z-mu||TV^2`. Constants are independent of
h, finite support and z. Finite laws are dense in K_r after harmless inward
approximation at its boundary: first mix a law slightly with nu*, and then
approximate by finite partitions. Thus the Cauchy estimate

\[
 \|Q_{h,\epsilon}-Q_{h,\epsilon'}\|_H
                       \le2C(\epsilon+\epsilon')            \tag{2}
\]

passes to every Borel mu by continuity of F_h and of the contamination map.
It is uniform on K_r times the compact data domain. The uniform limit of
these continuous difference quotients defines a jointly continuous G_h on
all Borel laws, and (1) still holds there. In particular it is the actual
one-sided contamination derivative of the Borel finite-step output.

The continuous source map G_h is Bochner integrable against any law. For
finite laws mu,nu, derivative linearity gives

\[
 D F_h(\mu)[\nu-\mu]=\int G_h(\mu,z)\,d\nu(z),
 \qquad \int G_h(\mu,z)\,d\mu(z)=0.                         \tag{3}
\]

These identities extend to Borel laws. For the left side define the
directional derivative along the probability segment by its forward quotient.
The same estimate (1) holds with direction nu-mu and TV bound two. Approximate
mu and nu by finite laws, use continuity at each fixed epsilon, and then let
epsilon decrease. For the right side, joint continuity on a compact set gives
uniform convergence of integrands as mu varies; integration against weakly
convergent nu is continuous for continuous H-valued functions. To verify the
latter, approximate the compact range by a finite continuous partition of
unity and reduce to finitely many scalar weak-convergence tests.

Now let F be the actual C.4.7 population output. Its uniform raw Euler
completion implies

\[
 a_{h,h'}:=\sup_{\mu\in K_{r1}}\|F_h(\mu)-F_{h'}(\mu)\|_H
                                                   \longrightarrow0. \tag{4}
\]

For each fixed epsilon, use (1) and the two quotient numerators to get

\[
 \sup_{\mu\in K_r,z}\|G_h(\mu,z)-G_{h'}(\mu,z)\|_H
                        \le4C\epsilon+2a_{h,h'}/\epsilon.    \tag{5}
\]

Choose epsilon proportional to the square root of a_h,h' once it is small
enough to be below eps0. Thus the G_h converge uniformly to a bounded,
jointly continuous kernel G(mu,z). Passing (1),(3) and the fixed-epsilon
quotients to the limit proves

\[
 \partial_{\epsilon+}F((1-\epsilon)\mu+\epsilon\nu)|_{\epsilon=0}
                 =\int G(\mu,z)\,d\nu(z),
 \qquad \int G(\mu,z)\,d\mu(z)=0.                            \tag{6}
\]

Hence G is an actual neural population influence kernel, obtained by
differentiating the full finite Gaussian source programs and removing the
mesh. It retains their actual initialized action, adjoint and scalar feedback.
This constructs an output derivative; it does not identify a bounded raw-L2
parameter tangent or an ambient raw-L2 propagator.

## What survives from the second derivative estimate

An actual continuous second derivative need not survive a uniform limit
under only a uniform second derivative bound. What does survive is the
quadratic Taylor inequality and TV-Lipschitz continuity of the first
derivative along probability segments. More precisely, for finite laws and
a fixed signed zero-mass direction sigma, the mean-value formula gives

\[
 \|D F_h(\rho)[\sigma]-D F_h(\mu)[\sigma]\|_H
                   \le C\|\rho-\mu\|_{TV}\|\sigma\|_{TV},    \tag{7}
\]

when the segment lies in the larger ball. The derivative is represented by
the centered atom kernel, and finite common-part approximations of the signed
measures pass (7) to Borel laws without enlarging their TV distances. One
explicit construction partitions the data domain, moves positive and
negative components to the same representatives, and separately keeps their
common part; the moved difference has TV no larger than the original. Then
use (3),(5) and kernel continuity. Passing h to zero preserves the inequality.

Likewise for probability mu,nu with their segment in the larger ball,

\[
 \|F(\nu)-F(\mu)-D F(\mu)[\nu-\mu]\|_H
                                      \le (C/2)\|\nu-\mu\|_{TV}^2. \tag{8}
\]

These are the derivative controls that replacement arguments can use. They
should not be advertised as a constructed continuous Borel Hessian kernel.

Finally, a bounded H-valued influence has a finite second moment and its iid
average has the usual separable-Hilbert Gaussian CLT. A bounded continuous
kernel into `C([0,T] x S1)` alone does not guarantee a supremum-norm process
CLT; that would require an additional entropy/modulus argument or a bounded
linear image of a separately controlled Hilbert empirical process. This
distinction does not affect the requested endpoint H-valued prediction CLT.
