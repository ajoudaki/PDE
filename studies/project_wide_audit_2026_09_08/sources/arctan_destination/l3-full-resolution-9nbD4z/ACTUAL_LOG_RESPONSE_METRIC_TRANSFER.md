# Passing logarithmic response bounds to the transformed first coordinate

Candidate pending independent audit. This note supplies the metric
comparison needed to transfer the new raw-coordinate squared-logarithmic
response bounds to the original transformed coordinate \(F(z^{(1)})\).
It preserves finite-width scope and supplies no width-uniform response
trace, population existence, or population uniqueness bound.

The transformation is \(F(z)=z+z^3/3\). An orthonormal-coordinate
representation for the transformed state metric is
\[
\eta=\bigl(F(z^{(1)})/\sqrt n,\ W^{(2)},\
                  W^{(3)},\ W^{(4)}/\sqrt n\bigr).
\]
The raw Euclidean coordinates used in ACTUAL_SQUARED_LOG_RESPONSE.md are
\[
\theta=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)},W^{(4)}).
\]
At a reached state their derivative relation is
\[
D_\theta\eta=n^{-1/2}H,\qquad
H=\operatorname{diag}\bigl(
 \operatorname{diag}(1+(z^{(1)}_i)^2),I_{n^2},I_{n^2},I_n\bigr).
\tag{1}
\]
Consequently the full propagators at either fixed feature times or
fixed physical times obey
\[
U_\eta(t,t_0)=H_t U_\theta(t,t_0)H_{t_0}^{-1}.
\tag{2}
\]
The scalar factors \(n^{-1/2}\) cancel. This is an exact derivative
of the coordinate conjugacy, not an isometric identification.

## Endpoint factors cost only a second logarithmic moment

If \(H>0\) is symmetric, \(V\) has full column rank, and
\[
\Lambda(V)=\left(\sum_j(\log\sigma_j(V))^2\right)^{1/2},
\]
then
\[
\Lambda(HV)\le\Lambda(V)+\|\log H\|_{\rm F}.
\tag{3}
\]
Indeed let \(V_r=H^rV\), \(0\le r\le1\). Its equation is
\(\partial_r V_r=(\log H)V_r\). The trace differentiation in
ACTUAL_SQUARED_LOG_RESPONSE.md applies without isometric initialization:
regularizing its energy by \(\epsilon>0\) gives
\[
\sqrt{\Lambda(V_r)^2+\epsilon}
\le\sqrt{\Lambda(V)^2+\epsilon}
           +r\|\log H\|_{\rm F}.
\]
Let \(\epsilon\downarrow0\) and take \(r=1\). This proves (3) even
when singular values are repeated or the initial logarithmic energy
vanishes.

For the particular endpoint factor (1),
\[
\|\log H_t\|_{\rm F}^2
=\sum_{i=1}^n[\log(1+(z^{(1)}_i(t))^2)]^2
\le4\|z^{(1)}(t)\|_2^2.
\tag{4}
\]
The scalar inequality follows from \(\log(1+u)\le2\sqrt u\) for
\(u\ge0\): its difference has derivative
\(u^{-1/2}-(1+u)^{-1}>0\) for \(u>0\) and value zero at zero.
The identity matrix blocks in (1) make no contribution.
The inverse \(H^{-1}\) has the same Frobenius norm of its logarithm.
No maximum-coordinate control of \(z^{(1)}\) is required.

## Rectangular feature responses in the transformed metric

Let \(E:\mathbb R^m\to\mathbb R^N\) be isometric in the transformed
orthonormal coordinates, \(E^TE=I_m\). The initial raw rectangular
response is \(V_0=H_{s_0}^{-1}E\). Applying (3) to \(E\) gives
\(\Lambda(V_0)\le\|\log H_{s_0}\|_{\rm F}\).
The same nonzero-initial-energy version of the trace argument, now
along the raw feature propagator, gives
\[
\Lambda(U_\theta(s,s_0)V_0)
\le\|\log H_{s_0}\|_{\rm F}
       +\int_{s_0}^s\|B(u)\|_{\rm F}\,du .
\]
Multiplication by \(H_s\) and (3)--(4) then prove
\[
\Lambda(U_\eta(s,s_0)E)
\le C_B(M,R)\sqrt n(s-s_0)
        +2\|z^{(1)}(s)\|_2+2\|z^{(1)}(s_0)\|_2.
\tag{5}
\]
This holds for every initial subspace on the common primal event.
The endpoint terms make it deliberately nonsharp at \(s=s_0\).

For an independent standard Gaussian perturbation of top column \(i\),
the raw embedding is \(E_i u=(0,0,ue_i^T,0)\). Its transformed
response is \(\widetilde Y_i=H_sY_i/\sqrt n\), where
\(Y_i=U_\theta(s,0)E_i\). Since \(H_0^{-1}E_i=E_i\), the sharper bound is
\[
\Lambda(\sqrt n\,\widetilde Y_i)
=\Lambda(H_sY_i)
\le C_B(M,R)\sqrt n\,s+2\|z^{(1)}(s)\|_2.
\tag{6}
\]
Thus the logarithms concern \(n\) times the nonzero transformed covariance
eigenvalues. The unscaled transformed covariance has initial eigenvalues
\(1/n\), and these factors must not be suppressed.

For its trained-increment response,
\(\sqrt n\,\widetilde Z_i=H_sY_i-E_i\), since \(H_sE_i=E_i\).
The same ordered-eigenvalue argument as (10) of
ACTUAL_SQUARED_LOG_RESPONSE.md gives
\[
\sum_{j=1}^n[\log(1+n\sigma_j(\widetilde Z_i)^2)]^2
\le2n(\log5)^2+
8\left[C_B(M,R)\sqrt n\,s+2\|z^{(1)}(s)\|_2\right]^2.
\tag{7}
\]
These are actual column derivatives; no Gaussian independence of the
trained trajectory and its initialized column is asserted. The auxiliary
derivative probe is independent.

## Uniform physical-time consequence

Use the single canonical high-probability event and constants
\(M,R,S_*\) constructed in ACTUAL_CLOCK_RANK_ONE_RESPONSE.md.
Intersect it with \(\|z^{(1)}(0)\|_2/\sqrt n\le2\), whose probability
tends to one by the Gaussian law of large numbers. The displacement
bound in READOUT_COERCIVITY.md yields, simultaneously for all physical
times and the corresponding feature segment,
\[
\|z^{(1)}(t)\|_2/\sqrt n
\le 2+2(1+a\epsilon_0)/b_0=:R_1.
\]
Here \(b_0,\epsilon_0\) are the same fixed initialization constants as
in the clock note, not new assumptions.

For any reached starting time \(t_0\), the raw fixed-physical-time and
fixed-feature-time propagators differ by rank at most one. Conjugating
both with the same \(H_t,H_{t_0}^{-1}\) preserves that rank. Their
rectangular restrictions to \(E\) therefore still obey the interlacing
and trimmed-log inequality (3) of ACTUAL_CLOCK_RANK_ONE_RESPONSE.md.
Combining with (5) and the feature-length bound \(S_*\) gives
\[
\sup_{0\le t_0\le t<\infty}
\frac1n\sum_{j=2}^{m-1}
[\log\sigma_j(U_{\eta,\rm phys}(t,t_0)E)]^2
\le [C_B(M,R)S_*+4R_1]^2.
\tag{8}
\]
The sum is zero for \(m\le2\). Every endpoint in the supremum is finite.
The estimate holds simultaneously for all initial isometries \(E\);
no derivative of an infinite-time endpoint map is used.

The same argument for \(\sqrt n\,\widetilde Y_i\), using (6), gives
the column-probe version with constant
\([C_B(M,R)S_*+2R_1]^2\). In particular the covariance scaling in (6)
is retained in this all-physical-time statement.

This closes the coordinate-metric comparison for these logarithmic
estimates. It does not transfer an unproved amplitude bound: the
squared-log constraint still permits rare exponentially large singular
values, and the physical result still excludes up to two extremes.
The actual source alignment, clipped-tail estimate, and full canonical
population theorem remain open.

Dependencies: ACTUAL_SQUARED_LOG_RESPONSE.md for the trace differential
and raw Hessian bound; ACTUAL_CLOCK_RANK_ONE_RESPONSE.md for the exact
clock derivative, singular interlacing, and explicit all-time primal
event; READOUT_COERCIVITY.md for the latter's finite-width bounds.
