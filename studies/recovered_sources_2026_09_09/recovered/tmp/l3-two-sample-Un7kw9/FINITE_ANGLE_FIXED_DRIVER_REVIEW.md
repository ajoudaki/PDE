# PASS — isolated finite-angle fixed-driver proof audit

Candidate: `/tmp/l3-two-sample-Un7kw9/FINITE_ANGLE_FIXED_DRIVER_PROOF.md`

Candidate SHA-256:
`eae75509d43eb50ca10a8a5401d3100f38dd8f67985eb54e2d6b5d575d0e5bc1`

Verdict: **PASS for the stated local two-coordinate pure-q theorem.** No
substantive gap was found in the uniform clock estimates, the four initial-state
derivatives at fixed driver, the driver derivative, or the asserted sufficient
Gaussian moment condition. No correction to the candidate is required.

This is an analytic audit using the candidate and only the orbit, radius, and
fixed-terminal-contrast results through equation (10) of
`/tmp/l3-two-sample-Un7kw9/FINITE_ANGLE_Q_CHANNEL_ROUTE.md` as its mathematical
dependency. The candidate's reference to another review supplies no evidence
for this verdict. No other review, history, theorem assembly, or separate
network notes were consulted. No agents or numerical experiments were used.
The candidate was not edited.

## Exact scope

For each fixed `e>0`, put `L=1+e`, `gamma=e/L`, and

    C_0 = 4/sqrt(L) + 2(2+e)/L,
    B   = 1 + |M0| + sqrt(e)|V0|,
    E   = exp(C_0|M0|) + exp(gamma V0^2).

For the autonomous vector field `(mu^2 b_delta, a_delta)`, with
`mu^2=1-delta^2`, the candidate establishes, for every real initial pair,

    sup_{delta in [0,1], r in R}
      ( ||D_(M0,V0) Psi_(delta,r)|| + ||partial_r Psi_(delta,r)|| )
      <= C_e B^10 E.

Here `C_e` depends only on the fixed activation parameter and the choice of a
fixed finite-dimensional norm. The derivative matrix contains all four ambient
initial-coordinate derivatives, including at `delta=1`. Initial-state
differentiation holds the integrated driver `r` fixed. The estimate includes
both signs of `r`; it does not differentiate the angle.

The claimed sufficient moment condition is valid for jointly Gaussian initial
coordinates: for `p>0`, it is `p gamma Var(V0)<1/2`. If `Var(V0)=0`, all positive
moments of the displayed majorant are finite. For the specified root
`M0=mu G1`, `V0=G2`, the fourth moment is uniform in the angle at `e=1/10`.

This verdict makes no assertion about the actual network's p channel, arbitrary
late injections, trained-operator responses, or derivatives of a driver
selection rule. Those are outside the candidate's theorem, not defects in it.

User scope clarification: the ultimate target is ONE data-independent
activation. Proof constants may depend on every fixed input/label
configuration and on the physical time horizon `T`. Angle-uniform constants,
speeds, and horizons are not required for that target. The local candidate's
uniform-angle estimate is therefore a stronger sufficient estimate, not an
obligation imposed on the ultimate theorem. This clarification changes only
the recorded scope; the audit still checks the candidate's own stated bound
and does not undertake further research or a full-network audit.

## 1. Orbit input and its constants

Let `X=m^2`, `Z=delta^2 v^2`, and

    P = (1+(m+delta v)^2)(1+(m-delta v)^2).

Direct algebra gives `a=F/P`, `b=-2e m v/P`, and

    F = (X-Z)^2 + (2+e)(X+Z) + L
      = (X-Z-1)^2 + 4X + e(1+X+Z).

In particular,

    F >= 4X,
    F >= L(1+X),
    F-L(1+X) = (X-Z)^2 + X + (2+e)Z >= 0.

These identities justify the candidate's strengthened denominator bound and
its explicit `C_0`, rather than merely an unspecified constant from the
dependency. The scalar equation is

    m_Y = -e mu^2 m/F(m^2,delta^2 Y),
    X_Y = -2e mu^2 X/F.

Thus `-e mu^2/2 <= X_Y <= 0`. Integrating back to `Y=0` gives
`|m(v)|^2 <= M0^2+(e mu^2/2)V0^2`, which implies the stated bound by `B`.
The function `m(v)=S(v^2,Y0,M0)` solves the smooth equation in `v` on both
sides of zero; passage through zero does not require division by `v`.

The fixed-terminal derivative is positive and satisfies `J_Y=f_m J`, with

    f_m = e mu^2(-F+2X F_X)/F^2.

The dependency's lower bound `f_m>=-e/L` checks algebraically. When `F_X>=0`,
use `f_m>=-e mu^2/F`. When `F_X<0`, set `u=Z-X>A=1+e/2` and
`D=(u+1)(u+1+e)`. Then

    F = D+4AX,       F-2X F_X = D+4uX,
    F^2-L(F-2X F_X)
      = D(D-L) + (8AD-4uL)X + 16A^2 X^2 >= 0.

The last sign follows from `D>=L` and `2AD>=4A^2u>=Lu`.
Backward integration therefore bounds `J` by `exp(gamma Y0)`.

For forward integration, when `mu M0` is nonzero, the change from `Y` to the
strictly decreasing `X` gives

    integral (f_m)_+ dY
      <= integral_0^(M0^2) sup_{Z>=0} |F_X|/F dX.

Since `|X-Z|<=sqrt(F)`,

    |F_X|/F
      <= [2+(2+e)/sqrt(L)] / [sqrt(L) sqrt(1+X)].

Its integral is exactly bounded by
`C_0(sqrt(1+M0^2)-1) <= C_0|M0|`. If `mu=0`, then `J=1`; if `M0=0`,
the forward linearization has `f_m<=0`. Consequently `0<J<=E` in all cases.
No assertion of decay of `m` at positive angle is needed here.

Global flow existence also checks: `1<=a<=L` bounds `V` on finite driver
intervals, and `|b|<=2e|V|` then bounds `M`. Smooth local ODE solutions extend
over every such interval. The lower bound on `a` makes the contrast range all
of the real line as `r` does.

## 2. The uniform clock integral and the slope

The cancellation in the clock integrand is valid. Explicitly,

    phi'''(z) = 2e(3z^2-1)/(1+z^2)^3,
    a_M(m,v) = [phi''(delta v+m)-phi''(delta v-m)]/2.

The bounds `||phi'''||_infinity=2e` and `||phi''||_infinity<=2e` give
`|a_M|<=2e|m|` and `|a_M|<=2e`. If `|delta v|>=D=2(B+1)`, all arguments
in that difference have absolute value at least `|delta v|/2>=1`.
Using `|phi'''(z)|<=8e/|z|^4` gives precisely the valid upper bound
`128e|m|/|delta v|^4`. Each factor of `P` is at least `|delta v|^2/4`,
so `F>=|delta v|^4/16` on these tails.

For `0<delta<=1/2`, `B>=1` implies, on `|v|<=1/delta`,

    F <= (B^2+2)(B^2+2+e) <= K_e B^4,
    K_e = 3(3+e).

Since `mu^2>=3/4`, integration from the radius maximum at `Y=0` yields

    |m(v)| <= B exp(-alpha v^2),
    alpha = 3e/(4K_e B^4).

For larger `|v|`, monotonicity in `Y` yields
`|m(v)|<=B exp(-alpha/delta^2)`. The crucial uniform estimate is

    delta^(-1) exp(-alpha/delta^2)
      <= (2 alpha exp(1))^(-1/2) <= C_e B^2.

Thus the three pieces of the integral of `|a_M|` have the following bounds:

| Region | Bound before simplifying powers | Result |
| --- | --- | --- |
| `|v|<=1/delta` | `2eB sqrt(pi/alpha)` | `C_e B^3` |
| `1/delta<|v|<=D/delta` | `4eBD delta^(-1) exp(-alpha/delta^2)` | `C_e B^4` |
| `|v|>D/delta` | `256eB exp(-alpha/delta^2)/(3delta D^3)` | `C_e B^4` |

Here `D<=4B`. The tail coefficient follows by integrating `|v|^-4` over
both tails. In particular, the proof does not accidentally integrate the
possibly nonzero plateau of `|m|` over an infinite interval.

For the slope, use the exact identity

    |m_v| = 2e mu^2 |v m|/F.

On the core, `F>=L` and the maximum of `|v|exp(-alpha v^2)` give
`C_e B^3`. On the middle region, the bound is
`(2e/L)BD delta^(-1)exp(-alpha/delta^2) <= C_e B^4`.
On the tails, it is at most
`32eB exp(-alpha/delta^2)/(delta D^3) <= C_e B^4`.
There is no lost extra inverse power of `delta` in either tail calculation.

At `delta=0`, the same Gaussian estimate holds for every `v`; the core
calculations alone apply. For `1/2<=delta<=1`, the inner interval has length
at most `4D`, giving integral bound `8eD`, while `|v|<=2D` gives slope
bound `C_e B^2`. The tail bounds above apply without the plateau factor,
and `delta^(-1)<=2`. This proves both estimates in candidate equation (2)
uniformly, including both angle endpoints.

## 3. Initial time, moving endpoint, and all four entries

For the nonautonomous scalar flow, differentiation of

    S(Y,Y0+h,S(Y0+h,Y0,M0)) = S(Y,Y0,M0)

gives the correct identity

    partial_(Y0) S = -J f(M0,Y0),
    m_(V0)(v) = -2V0 J(v) f(M0,Y0).

It is the vector field at the initial point. Substitution of the terminal
vector field without its flow derivative would be invalid at general positive
angle, and the candidate does not make that substitution. Since `F>=L`,

    |m_(V0)(v)| <= 2 gamma |V0 M0| E <= C_e B^2 E.

Differentiation is at fixed terminal `v`. Smooth dependence on `V0^2` gives
zero for this derivative at `V0=0`; the scalar equation is also smooth at
`M0=0`. A local extension in initial scalar time around zero is available
because the denominator is positive there.

For the signed clock, differentiation at fixed `r` gives

    V_(M0) = a_end integral_(V0)^V a_M J/a^2 dv,
    V_(V0) = a_end/a_start
             + a_end integral_(V0)^V a_M m_(V0)/a^2 dv.

The sign and the lower-endpoint contribution `a_end/a_start` are correct.
These are finite-interval differentiations justified by smooth dependence and
the strictly positive terminal clock derivative `1/a_end`. Absolute values
of the signed integrals are bounded by the full-line integral, so the same
estimates apply to negative and positive drivers.

Consequently, the estimates for the terminal contrast are `C_e B^4 E` and
`C_e B^6 E`. Applying the terminal chain rule to `M=m(V;M0,V0)` gives:

| Entry at fixed driver | Formula | Upper bound |
| --- | --- | --- |
| `V_(M0)` | clock derivative above | `C_e B^4 E` |
| `V_(V0)` | clock derivative including lower endpoint | `C_e B^6 E` |
| `M_(M0)` | `J(V)+m_v(V)V_(M0)` | `C_e B^8 E` |
| `M_(V0)` | `m_(V0)(V)+m_v(V)V_(V0)` | `C_e B^10 E` |

There is only one factor `E` in every entry: the terminal slope bound is
polynomial in `B`. Also `V_r=a` and `M_r=a m_v`, giving a driver derivative
bound `C_e B^4`. Since `B>=1` and `E>=2`, these estimates imply (11).

As an endpoint check, at `r=0` the integrals vanish, `J=1`, and
`m_(V0)(V0)=-2V0 f(M0,Y0)` cancels `m_v(V0)=2V0 f(M0,Y0)`.
The full initial-state Jacobian is therefore the identity, as required.

At `M0=0`, `m=a_M=m_v=m_(V0)=0`, while `J` remains the nontrivial scalar
linearization already bounded above. At `delta=1`, `mu=0`, hence `m=M0`,
`J=1`, and `m_v=m_(V0)=0`; the contrast clock formulas still apply. These
cases do not require a missing division or an excluded coordinate.

## 4. Gaussian moments and the fixed activation

For every `p>0`, raising the majorant to the p-th power reduces, up to a
constant, to the sum

    B^(10p) exp(p C_0|M0|) + B^(10p) exp(p gamma V0^2).

The first term is integrable for every jointly Gaussian pair, including
correlated or degenerate pairs: Gaussian polynomial moments and linear
exponential moments are finite. For the second, if `Var(V0)>0`, write the
Gaussian conditional representation `M0=c+d V0+sigma Z`, where `Z` is
independent standard Gaussian; `sigma=0` is allowed. Integrating over `Z`
bounds the conditional polynomial factor by `C(1+|V0|^(10p))`. The remaining
one-dimensional Gaussian integral is finite under
`p gamma Var(V0)<1/2`, also for nonzero means. If `Var(V0)=0`, the quadratic
exponential is constant and all positive moments are finite. No independence
assumption was silently added to the general Gaussian assertion.

For the specified common Gaussian root, the same random variables give the
pointwise bounds, simultaneously for every angle,

    B <= 1+|G1|+sqrt(e)|G2|,
    E <= exp(C_0|G1|)+exp(gamma G2^2).

This proves uniformity even for the moment of the supremum of the evaluated
responses over angle and driver. The supremum is measurable, by continuity
of the finite-time flow derivatives and reduction to a countable dense set
of angles and drivers. At `e=1/10`, `gamma=1/11`, so

    4 gamma = 4/11 < 1/2,
    1/2 - 4/11 = 3/22 > 0.

The remaining strictly negative Gaussian quadratic coefficient absorbs the
degree-40 polynomial factor. Thus the uniform fourth-moment statement holds
with this single fixed activation. This is a sufficient condition for the
actual response moments; no necessity or sharpness assertion about those
responses is needed.

Finally, a locally integrable signed q driver produces an absolutely
continuous integrated driver. Composition with the global flow solves the
driven equation almost everywhere. Holding that driver fixed leaves exactly
the initial-state derivatives audited above, irrespective of its reversals.
