# Probe-specific correction to the curvature certificate reduction

Author: /root/energy_route, 2026-09-12.
Status: **scope correction for internal review; no curvature sign evaluated**.

This note corrects the residual-dependent constants in the frozen
CURVATURE_CERTIFICATE_REDUCTION.md, whose SHA-256 remains

    24a69ef255c14e15cfb666332ea0f772ed9ae8deeb74938b6450ffb7f9918039

The original allows general bounded probes in §1, but some later constants
were specialized to r=F_*-q with |q|<=1. Those constants cannot be reused
unchanged for an unscaled sum of three probes. The reference approximation,
moment, projector, derivative-product and Gaussian-integration constructions
remain as in the original, with the residual-dependent substitutions below.
The original file and the declared task families are preserved.

## 1. Residual and approximation constants belong to each probe

A probe is an algebraic input to the endpoint force and curvature, not
necessarily a training residual for any member of the declared family.
A convenient representation is

\[
r=A F_*+\psi,\qquad
\bar r=A F_{\bar\theta}+\bar\psi,
\tag{P1}
\]

where A is a fixed known scalar, psi is specified independently of an
unknown changed-law prediction, and bar psi approximates psi with a
certified uniform error e_psi. The original raw endpoint error delta and
prediction Lipschitz bound L give

\[
e_r:=\|r-\bar r\|_\infty
 \le |A|L\delta+e_\psi.
\tag{P2}
\]

Here L is the coarse certificate constant of original (C3), and
||F_*||_infty<=C:=sqrt(10), ||F_bar_theta||_infty<=c:=11.
One may choose separately certified bounds

\[
R=\lvert A\rvert C+\|\psi\|_\infty,\qquad
\bar R=\lvert A\rvert c+\|\bar\psi\|_\infty,\qquad
R_{\rm probe}=\max(R,\bar R).
\tag{P3}
\]

Larger known bounds are harmless. Alternatively R+e_r bounds bar r, so
R_probe=R+e_r is valid when only R and e_r have been certified.
Every use below requires R_probe to bound both exact and approximate
residual suprema.

Two cases must remain distinct:

* For an exactly represented fixed probe independent of F_*, take A=0,
  psi=bar psi=r. Its **endpoint-induced** residual error is e_r=0.
  Any numerical evaluation error for its known expression is still added
  separately as e_psi.
* For r=A F_*+psi with the known psi represented identically, the
  endpoint-induced error is |A|Ldelta. It is Ldelta only when |A|<=1.
  For an actual task r=F_*-q, |q|<=1, one recovers R<=B_0=C+1,
  bar R<=c+1, and e_r<=Ldelta.

For arbitrary bounded measurable probes the algebraic identities and
continuity/error estimates are meaningful conditional on supplied certified
integral errors. The effective procedure is restricted to probes with
computable evaluations and certified spatial approximation/integration moduli.
Boundedness or pointwise evaluability alone supplies no effective integration
oracle. The original computable finite dictionaries and computable rational
Lipschitz-net representatives qualify. Abstract members of the declared
Lipschitz family have its spatial bound, but need not be individually
computable. For (P1), a Lipschitz bound is at most
|A|·76+Lip(psi) at the exact endpoint and
|A|caW_2+Lip(bar psi) at the finite reference. No new task family is introduced.

## 2. Corrected force, anchor and direction bounds

Fix a normalized density p, and use nonnegative quadrature weights with
total mass at most M_q>=1. The original construction permits M_q=2.
Let epsilon_v and epsilon_(v_w,4) be the raw and row-L⁴ quadrature
errors for the finite-reference integrands. Then replace the state/force
bounds after original (C8) and (C12) by

\[
e_v\le L e_r+R_{\rm probe}e_g+\epsilon_v,
\qquad
e_{v_w,4}\le Q_4 e_r+R_{\rm probe}e_{g_w,4}
                                      +\epsilon_{v_w,4}.
\tag{P4}
\]

Proof: before quadrature, subtract
r g-bar r bar g=r(g-bar g)+(r-bar r)bar g, and integrate against p.
Its mass is one. Use ||bar g||<=L or
||(bar g)_w||_4<=Q_4 respectively. This is why the first term is
L e_r, rather than always L²delta. The stated quadrature error accounts
for the remaining difference between the continuum finite-reference force
and its discrete version.

The common force bound must be recomputed as

\[
V_*=L\max\{R,M_q\bar R\}\le L M_q R_{\rm probe}.
\tag{P5}
\]

The endpoint geometry errors e_g,e_G,e_M,e_Pi and the certified anchor
gap gamma depend on the reference, not on the probe. Retain those exact
quantities. The probe-dependent bounds from original (C10) become

\[
B_\beta=\sqrt2L V_*/\gamma,
\]
\[
e_\beta=
\frac{\sqrt2L}{\gamma}e_v+
\frac{\sqrt2e_g}{\gamma}V_*+
\frac{4L e_g}{\gamma^2}\sqrt2L V_*,
\qquad
e_b=e_v+e_\Pi V_*.
\tag{P6}
\]

The original inverse/projection subtraction proves these formulas unchanged
once V_* and e_v have their correct values. They bound both beta and bar beta
by B_beta and the difference between b=Pi v and bar b=bar Pi bar v by e_b.

A sufficient common signed-control mass is now

\[
U=\max\{R,M_q\bar R\}+\sqrt2B_\beta
 \le M_qR_{\rm probe}+\sqrt2B_\beta.
\tag{P7}
\]

It replaces the task-specific example 2(c+1)+sqrt(2)B_beta.
Indeed the exact signed measure has mass at most
||r p||_1+sqrt(2)|beta|, and its quadrature counterpart has mass at
most sum_i w_i|bar r(u_i)|+sqrt(2)|bar beta|.

The row direction error is correspondingly

\[
e_{b_w,4}\le e_{v_w,4}+\sqrt2Q_4e_\beta+
                              \sqrt2B_\beta e_{g_w,4}.
\tag{P8}
\]

Thus all bounds for the direction must be formed from this probe's U:

\[
Z_j=UQ_j\ (j=2,4,8),\qquad Z_K=Uc,\qquad Z_c=U,
\quad e_z=e_b,\quad e_{z,4}=e_{b_w,4}.
\tag{P9}
\]

Substitute (P9) into original (C14)–(C17), including G_*, the projection
derivative bounds, the full D'_0 error and any L_prime used in the
K'_0 error. None of these probe-dependent quantities is inherited from a
different residual.

The finite derivative tail fields also change with the probe and must be
recomputed or enclosed for that probe. For exact scalar rescaling,
B_(lambda b)=lambda B_b and Q_(lambda b)=lambda Q_b, so, for lambda!=0,

\[
\tau_R(\lambda X)=|\lambda|\tau_{R/|\lambda|}(X).
\tag{P10}
\]

At lambda=0 the tail is zero. The same change of cutoff applies to the
soft-tail expectation. Thus a derivative tail bound at an unchanged cutoff
must not silently be reused after increasing the probe amplitude.

Large finite probe mass does not change the reference itself. The derivative
identities are evaluations in one admissible direction at that reference,
using finite signed control mass and its moment bounds. They assert no
finite-episode learning theorem for the enlarged probe.

## 3. Corrected cubic error

Use the original notation

\[
\mathfrak a_r=\int r(u)\dot g_b(u)p(u)d\rho(u)-\dot G_b\beta,
\qquad \mathcal C_p(r)=\langle b,\mathfrak a_r\rangle.
\]

Let bar a_r be the finite-reference quadrature approximation,
and epsilon_I its remaining spatial integration error. In original (C18),
replace the residual factor B_0 and endpoint error convention by

\[
E_{\mathfrak a}\le
G_*e_r+(R_{\rm probe}+\sqrt2B_\beta)e_{\dot g}
                          +\sqrt2G_*e_\beta+\epsilon_I,
\]
\[
|\mathcal C_p(r)-\langle\bar b,\bar{\mathfrak a}_r\rangle|
\le e_b\|\bar{\mathfrak a}_r\|
       +(\|\bar b\|+e_b)E_{\mathfrak a}.
\tag{P11}
\]

For the integral, subtract r dot g_b-bar r dot bar g_bar_b using
the same factor splitting as (P4). For the anchor subtraction use
||dot G||<=sqrt(2)G_*, |beta|,|bar beta|<=B_beta, and the derivative
column error sqrt(2)e_(dot g). The scalar inner-product difference then
gives the second line. This verifies every residual-dependent factor.
In particular e_r is from (P2), not automatically Ldelta.

## 4. Polarization: direct bounds or verified rescaling

Let r_i=A_iF_*+psi_i, i=1,2,3, with known exact bounds R_i, finite-reference
bounds bar R_i, and approximation errors e_(psi_i). For signs eps_i in {±1},
define

\[
r_\varepsilon=\sum_{i=1}^3\varepsilon_i r_i,\quad
A_\varepsilon=\sum_i\varepsilon_i A_i,\quad
\psi_\varepsilon=\sum_i\varepsilon_i\psi_i.
\]

Safe constants for the direct evaluation are

\[
R_\varepsilon\le\sum_iR_i,\qquad
\bar R_\varepsilon\le\sum_i\bar R_i,\qquad
e_{r,\varepsilon}\le |A_\varepsilon|L\delta+
                                      \sum_i e_{\psi_i}.
\tag{P12}
\]

Apply (P4)–(P11) separately with these constants and the corresponding
probe-dependent direction/tail bounds. If all three are actual-task
residuals F_*-q_i with |q_i|<=1 and exactly represented q_i, this gives
R_epsilon<=3B_0, bar R_epsilon<=3(c+1) and
e_(r,epsilon)<=3Ldelta. Cancellation in A_epsilon permits the sharper
|A_epsilon|Ldelta; there is no need to discard that information.

For the symmetric trilinear polarization c_p of the homogeneous cubic,

\[
c_p(r_1,r_2,r_3)=
\frac1{48}\sum_{\varepsilon\in\{\pm1\}^3}
 \varepsilon_1\varepsilon_2\varepsilon_3\,\mathcal C_p(r_\varepsilon).
\tag{P13}
\]

The factor is 2³·3!=48: in the expansion only the term involving all
three arguments survives the signed sum; its multiplicity is 3! and the
sum over signs contributes 2³. If the eight direct cubic enclosures have
absolute errors E_epsilon, the polarization error is at most
sum E_epsilon/48, or E/6 for a common bound E.

An alternative keeps actual-task-sized probe bounds. If
r_i=F_*-q_i, |q_i|<=1, evaluate s_epsilon=r_epsilon/3 instead.
Then its exact bound is B_0, its finite-reference bound is c+1,
and its endpoint approximation error is at most Ldelta. Nevertheless
s_epsilon is an algebraic probe and need not be an actual-task residual:
its coefficient of F_* is A_epsilon/3, possibly different from one.

The cubic is exactly homogeneous:

\[
\mathcal C_p(\lambda r)=\lambda^3\mathcal C_p(r).
\]

This follows because beta and b are linear in r, dot g_b is linear in b,
the vector a_r is quadratic, and its pairing with b is cubic. Hence

\[
c_p(r_1,r_2,r_3)=
\frac{27}{48}\sum_\varepsilon
 \varepsilon_1\varepsilon_2\varepsilon_3\,\mathcal C_p(s_\varepsilon)
=\frac9{16}\sum_\varepsilon
 \varepsilon_1\varepsilon_2\varepsilon_3\,\mathcal C_p(s_\varepsilon).
\tag{P14}
\]

If the eight normalized cubic errors are E_epsilon, the resulting tensor
error is at most (9/16)sum E_epsilon, or (9/2)E for a common bound E.
The factor 27 cannot be omitted. The derivative map D'_0(r) and K'_0(r)
are linear in r at fixed p, so their rescaling factor is lambda, not
lambda³. Neither polarization method chooses a task by observed performance.

## 5. Uniform families and every remaining B_0 occurrence

For the exact endpoint and arbitrary normalized densities, let h=rp and
tilde h=tilde r tilde p. If r and tilde r are bounded by R_probe, then

\[
\|h-\tilde h\|_1
\le \|r-\tilde r\|_\infty+
                         R_{\rm probe}\|p-\tilde p\|_1.
\tag{P15}
\]

This follows by writing h-tilde h=(r-tilde r)p+tilde r(p-tilde p)
and using integral p=1. If an unnormalized comparison measure is used,
replace the first coefficient one by its known mass bound M_q.
For (P1) at the same exact endpoint,

\[
\|r-\tilde r\|_\infty
\le C|A-\tilde A|+\|\psi-\tilde\psi\|_\infty.
\]

When the comparison additionally substitutes the finite reference, add
|tilde A|Ldelta and its known-function evaluation error. For the original
actual-task family A=tilde A=1, one can use B_0 in (P15) and
||r-tilde r||_infty=||q-tilde q||_infty. This even improves the original
conservative factor 5/4 to one for normalized densities. For enlarged
polarization probes use their own R_probe and coefficients.

Original (C27) itself remains valid with

\[
H_1\ge\max(\|rp\|_1,\|\tilde r\tilde p\|_1).
\]

A sufficient choice is H_1=R_probe for probability densities and
H_1=M_qR_probe when the bounding class includes measures of mass M_q.
Recompute this value for each probe or use a common bound over the finitely
many probes. The constant M_cub=LJ_1 C_proj³ remains a reference/geometric
constant: J_1 was defined using unit signed-control mass. It does not absorb
an unrecorded residual bound. The derivative feature-map continuity bound
likewise uses this updated H_1; changes of p in the prediction metric remain
handled by the original common-space square-root conjugation.

The declared geometry-family target and density nets are unchanged.
Uniform coverage uses computable finite nets with their certified covering
errors; it does not require every abstract family member to be individually
computable. Evaluate only those net representatives and extend by (P15)
and the corrected (C27) bound. An individual abstract member outside that
effective input class receives an analytic uniform guarantee if the net
certificate succeeds, not an asserted algorithm for evaluating its integrals.
Their target bound |q|<=1 applies to actual tasks and is not reinterpreted
as a bound for an unscaled polarization sum.

For auditability, all original B_0/task-specialized uses are addressed here:

| Original location | Correct scope or replacement |
|---|---|
| §4, state part of e_v | (P4): L e_r+R_probe e_g |
| §4, example U=2(c+1)+sqrt(2)B_beta | (P5)–(P7), with probe-specific force and mass |
| §4, state part of row-L⁴ force error | (P4): Q_4 e_r+R_probe e_(g_w,4) |
| §6, original (C18) residual multiplier B_0 | (P11), using R_probe |
| §6, “For e_r one may use Ldelta” | Only actual-task / |A|<=1 specialization; use (P2) generally |
| §9, density/target perturbation bound with B_0 | (P15), specialized back to B_0 only for actual tasks |
| §9, H_1 and polarization | Recompute H_1; use (P12)–(P14) with all factors |
| Downstream G_*, L_prime, derivative tails | Recompute from (P5)–(P10); no reuse across amplitudes |

## 6. Preservation, checks and remaining scope

This correction preserves the original reference construction and all task
families. It resolves the identified mismatch between general probes and
actual-task constants; it makes no claim that a negative cubic has been
found. The arbitrary-probe analytic formulas are distinguished from the
additional effective integration inputs needed for a numerical certificate.

Actual checks in this continuation: searched all occurrences of B_0,
residual/error constants, force mass, polarization and uniform-family bounds;
reconstructed the force, anchor, direction and cubic factor subtractions;
verified the 1/48 polarization factor, the normalized factor 27/48=9/16,
their absolute-error factors, and the tail scaling identity. No numerical
reference evaluation, quadrature, training, new family or performance-based
selection occurred.

Input hashes checked before writing:

* Original reduction:
  24a69ef255c14e15cfb666332ea0f772ed9ae8deeb74938b6450ffb7f9918039.
* ROUTE_GEOMETRY.md:
  e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04.
* ROUTE_ENERGY.md:
  01779adf6e60fde92fb6979c3e421b3bc5061850bc3051399714b7d4aa58993b.
* RESEARCH_WORKFLOW.md:
  8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12.

The original full scientific input/read coverage remains recorded in the
frozen reduction and energy report. No additional scientific file or another
current follow-up was read. This separate correction is submitted for review;
it is not a promotion or an independently reviewed positive result.
