# Smooth closure: a concrete conditional completion of scalar feedback

2026-10-01. This note proves the deterministic final implication needed by
the smooth cavity and mean-map routes. Its statistical inputs are stated
explicitly. Until those inputs pass the combined bridge check, this is a
conditional completion, not a claimed full width theorem.

Scientific inputs are the exact SMOOTH_SETUP, the complete smooth cavity,
mean-map, all-initialization and interpolation routes, and the current
study's fitting, concentration and common-action population construction.
No other study, experiment, manuscript change, or Git write is used.

## 1. Actual finite-width mean histories are admissible

Let G_n be the initialized fitting event, let E_n denote expectation
conditional on G_n, and set

\[
\bar r=E_n r_n,\quad \bar\rho=E_n\rho_n,\quad
\bar\tau=E_n\tau_n,\quad
\bar K_{ba}=E_n\langle k_b,h_a\rangle_n,\quad
\bar V_{ba}=E_n\langle v_b,d_a\rangle_n.
\tag{1}
\]

Here <u,v>_n=u^T v/n, and all vectors in (1) come from the actual smooth
closure. Put s_n(t)=integral_0^t rho_n and bar s=integral_0^t bar rho.
The fitting bounds give rho_n<=Y exp(-lambda t). The exact residual
identity also gives ||dot r_n||_m<=C rho_n on G_n, because the readout
Gram is bounded by one and the hidden-motion term is at most C s_n^2 rho_n.
For Y>0, the residual never reaches zero at a finite time by ODE uniqueness.
Thus dot rho_n>=-C rho_n and

\[
Y e^{-Ct}\le\rho_n(t)\le Y e^{-\lambda t},\qquad
\frac{Y}{C}(1-e^{-Ct})\le\bar s(t),\qquad
s_n(t)\le Y\min(t,\lambda^{-1}).
\tag{2}
\]

The ratio of the last upper bound to the preceding lower bound is bounded
uniformly for t>0: use 1-e^{-Ct}>=Ct/2 for Ct<=1 and its positive lower
bound for Ct>=1. Consequently s_n(t)<=C_1 bar s(t) on G_n. Since
|v_b d_a|<=C s_n^3, this proves

\[
|\bar V_{ba}(t)|\le C_2\bar s(t)^3.
\tag{3}
\]

This argument is needed; Jensen's inequality alone gives the opposite
direction for the cubic moment. Also |bar K|<=1, bar tau=1+bar s, and
|bar r_a|<=sqrt(m) bar rho. Differentiating the actual scalar contractions
and using the fitting/operator bounds gives |dot K|+|dot V|<=C rho.
For V, use dot d=F_w dot w+F_z dot z and normalized Cauchy--Schwarz;
dot z has normalized norm <=C rho and all scalar gate derivatives are
bounded. Averaging proves |dot bar K|+|dot bar V|<=C bar rho. Thus K,V
are Lipschitz in the bar s activity coordinate. At Y=0 all paths are
stationary and all comparison statements are immediate.

## 2. Statistical hypotheses sufficient for the full feedback comparison

On the canonical population spaces use the bounded common Gaussian action
W and its actual adjoint from the study's population construction. Run the
forced population U=(A,w,v,k) with the supplied histories (1), exactly as
the forced finite system in SMOOTH_CAVITY_ROUTE, replacing normalized
pairings by expectations. All population comparisons below use the same
common action and initial first-layer root.

Write h=tanh(Au), z^e=W h+sum_b v_b bar K_ba/m, g^e=tanh z^e,
d^e=c_M(w sech^2 z^e), and

\[
K^U_{ba}=E_1[k_bh_a],\qquad V^U_{ba}=E_2[v_bd_a^e],\qquad
f^e_a=E_2[w g_a^e].
\tag{4}
\]

Superscript e only marks the supplied scalar coefficients. Assume that the
completed forced-law comparison and scalar freezing provide, with
epsilon=n^(-1/2),

\[
\sup_t(|\bar K-K^U|+|\bar V-V^U|)\le C\epsilon,
\tag{5}
\]
\[
|\bar\rho-\|\bar r\|_m|\le e_\rho(t),\qquad
|\dot{\bar r}-\dot f^e|\le e_f(t),\qquad
|\dot{\bar K}-\dot K^U|\le e_K(t),
\tag{6}
\]
\[
\int_0^\infty(e_\rho+e_f+e_K)\,dt\le C\epsilon.
\tag{7}
\]

All norms on the fixed sample indices are equivalent, with constants
depending only on m. The K derivative in (6) is along the forced population
state. It is a bounded-observable statistic:

\[
\dot K^U_{ba}=\bar\rho\,E_1[(h_b-k_b)h_a]/\bar\tau
                         +E_1[k_b\dot h_a].
\tag{8}
\]

Thus it uses the same passive dot h/bar rho observable as the prediction
velocity and no derivative of a Gaussian covariance path. The needed
statistical estimates must hold for the own forced population; replacing
it by a finite-width mean would be circular.

## 3. Convert the forced population into a controlled exact closure

From U reconstruct B=W+sum_b v_b tensor k_b/m and the corresponding
true forward features g^0, clipped signals d^0,ell^0, and prediction f^0.
Pairings here are population expectations. The differences between the
supplied z^e and reconstructed z^0 are
sum_b v_b(bar K_ba-K^U_ba)/m. By (5), bounded state coordinates, the
bounded common action, and the joint gate Lipschitz estimate, every forced
state velocity differs from the exact reconstructed velocity with controls
(bar r,bar rho) by a Hilbert norm at most C bar rho epsilon. For the lower
carrier, first replace d^e by d^0, then replace bar V by the actual
pairings E[v d^0]; both errors are controlled by (5). The key equation
already has the exact supplied clock bar tau.

There is also the velocity estimate

\[
|\dot f^e-\dot f^0|\le C\bar\rho\epsilon+C e_K(t).
\tag{9}
\]

To check it, subtract z^e-z^0=sum_b v_b(bar K_ba-K^U_ba)/m and
differentiate this identity. Its derivative is bounded in L2 by
C bar rho epsilon+C e_K, since |dot v_b|<=C bar rho.
Use dot f=E[dot w tanh z+w sech^2(z) dot z], the bounded activation
derivatives, bounded w,dot w/bar rho, and ||dot z^0||_2<=C bar rho.
This verifies (9) with the ordinary output derivative, without identifying
it with d. Changing the state velocity to the exact controlled velocity
adds at most C bar rho epsilon to the derivative of f^0, because this
prediction has a bounded first derivative on the present bounded set.

Consequently the mean residual obeys

\[
\dot{\bar r}=G(U)\bar r+Q(U,\bar\tau)\bar\rho+e(t),\qquad
\int_0^\infty\|e(t)\|_m\,dt\le C\epsilon.
\tag{10}
\]

G and Q are exactly the reconstructed smooth-closure residual coefficients
in SMOOTH_CAVITY_ROUTE equation (5). Q includes its clock factor 1/tau.
In particular G=-2 Gamma plus the
two hidden-motion terms, and Q is the key-motion term. Equation (10) is
an estimate for a derivative proved from (6),(8),(9), not inferred from
the uniform value estimate (5).

## 4. Damped comparison with the autonomous population

Let U_infinity,tau_infinity,r_infinity be the own autonomous population
flow on the same common-action spaces. Choose fixed labels sufficiently
small for the fitting bootstrap and the mean-map small-activity bounds.
The forced state also stays in that small-activity region: |bar r|<=C bar rho,
the canonical action is bounded, bar V=O(bar s^3), and cap contraction
give ||A-A0||_2<=C bar s^2, ||w||_infinity<=C bar s, and
||v||_infinity<=C bar s^2. Its reconstructed Gram therefore stays within
C bar s^2 of the positive initial Gram.

Let D be the sum of population L2 distances between the four state blocks
and the absolute clock distance, and let R=||bar r-r_infinity||_m.
The controlled state difference, (5), and the norm inequality give

\[
D(t)\le C\int_0^t[\bar\rho(s)D(s)+R(s)+e_\rho(s)
                                  +\bar\rho(s)\epsilon]ds.
\tag{11}
\]

Subtract the two residual equations using (10). On the small-activity
region Gamma>=lambda I, the hidden part of G has norm <=C S^2, and
||Q||<=C S^3. Every residual kernel is Lipschitz in the population L2
state distance, by bounded joint-gate derivatives and the bounded common
action. Moreover |bar rho-rho_infinity|<=R+e_rho. Absorb the C S^2 R
and C S^3 R terms into the readout damping by decreasing the fixed label
threshold. The resulting differential inequality is

\[
D^+R\le-\kappa R+C\rho_\infty D+\|e\|_m+C e_\rho,
\qquad\kappa>0.
\tag{12}
\]

Both initial discrepancies are zero. Integrate (12) first, substitute its
integral into (11), and apply Gronwall with the integrable coefficient
C(bar rho+rho_infinity). Equivalently apply SMOOTH_RESTORATION (1)--(4).
This proves

\[
\sup_{t\ge0}D(t)+\int_0^\infty R(t)dt\le C/\sqrt n.
\tag{13}
\]

No population L2 Hessian or all-time second derivative of the residual norm
is needed. Current-time coefficient differences cannot in general be
replaced by integrals of those differences; (5) retains them explicitly.

For a fixed passive input x, adjoin its K_bx coefficient and the corresponding
versions of (5)--(7), as well as the mean prediction-velocity comparison.
Then the same bounded-action forward estimate and (13)
give |E_n f_n(t,x)-f_infinity,M(t,x)|<=C_x/sqrt(n), uniformly in t.
The constants are uniform for x in a fixed bounded set provided the
statistical hypotheses have constants uniform on that set as well.
Combining this
with the previously proved conditional all-time centered concentration
would yield the full conditional mean-square root-width theorem, and
SMOOTH_RESTORATION (8) would yield the unconditional fixed-confidence form.

## 5. Exact remaining boundary

This proves (13) and the population-rate implication from the explicit
statistical hypotheses (5)--(7), together with their passive-query versions.
The two-sided cavity and deterministic mean-map arguments are intended to
establish those hypotheses. Their combined validity, admissible-domain
bookkeeping, and identification with the common-action population must be
checked before the implication is declared an actual-model theorem.
The stronger all-initialization all-time mean-square estimate also needs
the separate exceptional-initialization moment bound; it is not implied
by exponential failure probability alone.

The scoped SMOOTH_FEEDBACK_CHECK.md validates the conditional implication.
The subsequent changes explicitly display Q's clock argument and the
uniform-query statistical premise; they do not remove any statistical
hypothesis or alter the controlled dynamics.
