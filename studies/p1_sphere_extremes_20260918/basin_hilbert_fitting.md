# The fitting basin is also open in the physical Hilbert norm

Lead-author follow-up, 2026-09-18. This uses the complete frozen
basin_open_fitting.md (corrected hash dea26f190a47d292a3de27d9e15ad645f5ff2e5444b4825c986d52ecb7ed9175)
and the exact global Hilbert flow proved in basin_spectral_route.md.
It changes neither population laws nor the metric. No experiment.

The fitted center theta_*, and all constants in equations (5), (11)--(14)
of the open-fitting report, remain unchanged. In particular
gamma=beta p_min, rho=min{1,gamma/(4D_H)}, and C is the stated sum
of block speed bounds. Set d=||theta-theta_*||_H.

All estimates used in the trapping proof also hold with this d, without
any bound on the essential suprema of the current fields. The lower
moment estimate is

\[
 |a_i-a_i^*|
 \le E[|b_1|\,|(w-w_*)\cdot u_i|]
 \le B_{1,\max}\|w-w_*\|_2
 \le B_{1,\max}d.
\]

Also |a_i|<=B_{1,max}. Splitting M a_i-M_*a_i^* as in the source,
and using bounded upper marks, gives

\[
                    \|H_i-H_i^*\|_\infty\le D_H d.
\]

The weighted upper synthesis-operator argument is unchanged. Thus in
the H-ball d<rho the weighted readout Gram is at least (gamma/2)I.
For the prediction estimate, Cauchy--Schwarz replaces the supremum
readout estimate:

\[
 |f_i-f_i^*|
 \le\|c-c_*\|_2\|H_i\|_2+
                   \|c_*\|_2\|H_i-H_i^*\|_2
 \le (1+C_*D_H)d.
\]

Here C_*=3/beta is the same valid upper bound for ||c_*||_2.
Inside d<rho<=1, ||c||_2<=C_*+1=R_c and ||M||_F<=R_M.
Consequently |d_i|<=B_{2,max}R_c. The full canonical equations give
exactly the earlier block speed bounds, now in L2 for the two fields:

\[
 \|\dot c\|_2\le2\sqrt L,\quad
 \|\dot M\|_F\le2B_{1,\max}B_{2,\max}R_c\sqrt L,\quad
 \|\dot w\|_2\le
                 2B_{1,\max}B_{2,\max}R_MR_c\sqrt L.
\]

The product Hilbert norm is at most the sum of these block norms. Hence
throughout this known Hilbert ball

\[
              L'\le-2\gamma L,\qquad
              \|\dot\theta\|_H\le C\sqrt L.
\]

Define the nonempty H-open set

\[
 \mathcal U_H=\{\theta:\|\theta-\theta_*\|_H+
                            (C/\gamma)\sqrt{L(\theta)}<\rho\}.
\]

It contains the H-ball of radius rho/[2(1+(C/gamma)K_f)] using the
same K_f=1+C_*D_H. Apply the source's first-exit proof verbatim in H:
while inside the radius-rho ball, q=sqrt L satisfies q'<=-gamma q,
and integration of the speed gives

\[
 \|\theta(t)-\theta_*\|_H+(C/\gamma)q(t)
 \le\|\theta(0)-\theta_*\|_H+(C/\gamma)q(0)<\rho.
\]

The exact global Hilbert flow therefore never exits and U_H is forward
invariant. The trajectory has finite Hilbert length and a fitted endpoint,
with

\[
 L(t)\le L(0)e^{-2\gamma t},\qquad
 \|\theta(t)-\theta_\infty\|_H
 \le(C/\gamma)\sqrt{L(0)}e^{-\gamma t},
 \qquad L(\theta_\infty)=0.
\]

Its finite-time backward saturation is another nonempty H-open fitting
basin. If a starting state has bounded fields, its trajectory agrees with
the original canonical-carrier field equations at every finite time.
The source's separate X-open region additionally guarantees convergence
in the stronger continuous-field norm; that stronger conclusion is not
asserted from U_H alone.

This proves a nonempty open fitting basin in the *same physical topology*
in which the convergent bad basin is thin. No statement places canonical
initialization inside it or asserts it exhausts all other initial states.
