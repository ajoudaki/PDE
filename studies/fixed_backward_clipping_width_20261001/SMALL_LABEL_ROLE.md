# Small labels: exact uses, obstacles, and a cap-dependent fitting extension

2026-10-01. Continuation of the same smooth-clipping width investigation.
The user asks whether the small-label assumption can be removed. The full
all-time width theorem is not extended here. This note identifies its two
uses of small activity and proves a useful arbitrary-label fitting result
after choosing a smaller fixed positive cap. No experiments or manuscript
changes are involved.

Inputs are the exact SMOOTH_SETUP.md, complete SMOOTH_RESULT.md,
SMOOTH_ALLINIT_ROUTE.md, SMOOTH_FEEDBACK_COMPLETION.md, and the small-activity
map proof in SMOOTH_MEAN_MAP_ROUTE.md. The notation and model are unchanged.
The root derived the fitting extension below. A fresh scoped agent
label_size_obstacles read the complete assigned inputs, independently checked
the displayed cap-dependent estimates and stopping argument after receiving
the candidate calculation, and assessed the separate causal-map extension.
Its check and limitations are recorded at the end. This is an internal
calculation, not promotion.

## 1. Why the present all-time theorem needs small labels

Let Y=(m^(-1) sum_a y_a^2)^(1/2), let rho(t) be the residual RMS, and put
S(t)=integral_0^t rho(s) ds. At either finite width or on the canonical
population spaces, the exact residual identity is

\[
\dot r=-2\Gamma(t)r+e(t),\qquad
\Gamma_{ab}(t)=\langle g_a(t),g_b(t)\rangle/m,\qquad
e_a(t)=\langle w(t),\dot g_a(t)\rangle.
\tag{1}
\]

Pairings are u^T v/n at finite width and E_2[uv] in the population.
The ordinary output derivative in e is retained; it is not replaced by
the trained clipped backward signal.

The existing fitting proof has, on its activity interval,

\[
\|\Gamma(t)-\Gamma(0)\|_{\rm op}\le C S(t)^2,
\qquad \|e(t)\|_m\le C S(t)^2\rho(t),
\tag{2}
\]

where ||b||_m=(m^(-1)sum_a b_a^2)^(1/2). A positive initial Gram gap
therefore gives rho'<=(-2lambda+C S^2)rho. Small Y closes the stopping
argument and gives S(infinity)<=Y/lambda. It also makes the hidden
contributions in the two-trajectory residual equation smaller than the
readout damping. For larger fixed Y these estimates do not guarantee
preservation of the Gram gap or stability of the complete residual flow.
Failure of these bounds is not a counterexample to fitting or to a width
rate. No such counterexample has been proved here.

Separately, SMOOTH_MEAN_MAP_ROUTE (26) bounds the two population-map
directions by c_L S and c_U in normalized covariance/response norms.
The proved contraction requires c_L c_U S<1. This is an additional
quantitative identification condition, not a consequence of smoothness.

The whole-interval contraction might be replaced by causal continuation
over short activity intervals. A correct continuation must retain the
complete earlier histories, their cross-covariances with new sources,
and the learned response kernels. At a restart the readout is nonzero,
and the upper instantaneous response atom is generally nonzero. One
cannot restart the zero-readout proof with independent Gaussian neurons.
The necessary causal comparison with those earlier histories retained
has not been proved in the current notes.

Even a successful arbitrary-finite-activity comparison would still need
bounded total activity and stable training to give a uniform infinite-time
rate for arbitrary labels at the originally fixed M. Smooth bounded
backward signals do not bound their time integrals or ensure damping.

Finite total activity by itself is not the required error-stability result.
The state comparison contains integral_0^t R(s) ds, where R is the
finite/population residual discrepancy, with no additional residual factor.
Bounding both trajectories' activities by S_* only bounds this integral
by 2S_*, not by C/sqrt(n). The proved residual damping supplies the latter
bound. A replacement could use a uniformly integrable residual-response
propagator, but that is a substantive new estimate.

## 2. A proved fitting extension for any fixed label magnitude

Use the exact two-layer smooth-clipped q=1 closure. Assume
||W0||_op<=K and Gamma(0)>=lambda I_m for lambda>0. Define

\[
X=\max_a\|x_a/\sqrt d\|_2,\qquad
H=6+2X^2(K+2).
\tag{3}
\]

For every fixed Y>0, choose a fixed positive clipping level satisfying

\[
\frac{2MY}{\lambda}
 \le \min\left\{1,\frac{\lambda}{6H}\right\}.
\tag{4}
\]

Then the actual closure has a global solution, every state converges,
and

\[
\rho(t)\le Y e^{-\lambda t},\qquad
S(\infty)\le Y/\lambda.
\tag{5}
\]

There is no smallness assumption on Y in this statement. The choice of
M depends on Y, K, lambda and the fixed inputs, and is independent of
width and time. The same proof holds on the already constructed canonical
population spaces with their bounded common action and actual adjoint.

### Proof

The memory formula gives ||k_a||_infinity<=1 and
||dot k_a||_infinity<=2rho/(1+S). Since both trained backward signals
have magnitude at most M, the exact equations give

\[
\|w\|_\infty\le2S,\quad
\frac1m\sum_a\|v_a\|_\infty\le2MS,\quad
\|B-W_0\|_F\le2MS,\quad
\frac{\|\dot A\|_F}{\sqrt n}\le2MX\rho.
\tag{6}
\]

Here B=W0+sum_a v_a k_a^T/(mn) is only the memory reconstruction.
The first bound follows from the unchanged readout equation and bounded
g. The second follows by integrating mean_a |r_a|<=rho in the value
equation. The remaining two follow from normalized outer-product norms
and the lower clipped update. Differentiating B gives

\[
\|\dot B\|_F
 \le 2M\rho+\frac{4MS}{1+S}\rho\le6M\rho.
\tag{7}
\]

Provisionally stop when S reaches 2Y/lambda. By (4), MS<=1 before the
stop, so ||B||_op<=K+2. For every training input,

\[
\frac{\|\dot h_a\|_2}{\sqrt n}\le2MX^2\rho,
\qquad
\frac{\|\dot z_a\|_2}{\sqrt n}
 \le\|\dot B\|_{\rm op}\frac{\|h_a\|_2}{\sqrt n}
       +\|B\|_{\rm op}\frac{\|\dot h_a\|_2}{\sqrt n}
 \le MH\rho.
\tag{8}
\]

The last bound also holds for dot g_a. Write G=[g_a]. Its normalized
Frobenius displacement obeys ||G-G0||_F/sqrt(mn)<=MHS, while
||G||_op,||G0||_op<=sqrt(mn). Subtraction of the two Gram products
therefore gives

\[
\|\Gamma(t)-\Gamma(0)\|_{\rm op}\le2MHS,
\qquad \|e(t)\|_m\le2MHS\rho.
\tag{9}
\]

Take the residual inner product in (1). For rho>0, (9) yields

\[
\dot\rho
 \le[-2(\lambda-2MHS)+2MHS]\rho
 =(-2\lambda+6MHS)\rho\le-\lambda\rho.
\tag{10}
\]

The last inequality holds throughout the provisional interval by (4).
Thus S(t)<=Y/lambda, strictly below the proposed stop. Bounded state
coordinates and the locally Lipschitz vector field extend the solution
globally. At zero residual every state velocity vanishes, so the same
comparison holds by uniqueness. Every state speed is integrable by
(5)--(8) and the key/readout equations; hence the states converge and
the endpoint fits. The population proof replaces normalized norms and
pairings by their Hilbert counterparts. For Y=0 the state is stationary.

## 3. Interpretation and limit of this extension

Equation (4) replaces small labels by sufficiently strong clipping. For
fixed data and initial margin, it permits M of order 1/Y with a fixed
positive coefficient. In particular, it covers Y=1 and thus unit binary
labels whenever the stated initial feature-Gram condition holds and M
is chosen small enough. For Gaussian initialization, K and lambda may
be fixed from the population margin and a high-probability initial event;
M need not be selected from a realized width-n trajectory.

This keeps the feature and memory updates in the actual equations. It
also controls their accumulated movement by a small quantity of order
MS(infinity). It does not prove that arbitrary labels fit with an
already specified cap such as M=1, or that large representation movement
is harmless. M=0 is not used.

The root-width theorem does not follow by substituting (5) into its
current proof. Total activity Y/lambda can now be large. In addition,
high derivatives of the smooth cap depend on inverse powers of M, so
small M is not automatically a contraction parameter for the statistical
response map. Extending that map causally, or developing another
quantitative comparison valid at this larger activity, is still required.

The sharp current diagnosis is therefore: the all-time root-width theorem
for arbitrary labels at a fixed general cap remains open. The fitting
part has the explicit cap-dependent extension above. There is no proved
slower-width-rate example here. The principal unresolved dynamical issue
at a general fixed cap is preservation or recovery of stable learning
after the representations have moved substantially.

## Check and next scope

The scoped agent independently confirmed (6)--(10), the stopping constant
in (4), and the distinction between retuning M and keeping an originally
fixed cap. It also independently identified the possibility of causal
activity-interval continuation and the need to preserve past Gaussian
dependence; it did not claim that continuation proved. The coordinator
checked zero labels, normalized Gram factors, both matrix-product terms,
finite and population versions, and the exact unclipped output derivative.
The persisted argument above is complete for (4)--(5).

The agent then read the complete persisted file and returned PASS for
SHA-256 d8cd5b1907890d466bd9bb8f470d8af368923d4d4c292a55a2af1588d639df09,
confirming all constants, the stopping argument, convergence, and the
population qualification. A subsequent explanatory paragraph in Section1
records its separately supplied observation that finite activity does not
alone bound the integrated residual discrepancy at root width. The fitting
statement and proof were unchanged. This paragraph and this check record
are the only changes after that complete-file check.

No full arbitrary-label width theorem is claimed. Any further proof search
should first specify whether M is held at its existing value or may be
chosen for the fixed label magnitude; these are different mathematical
questions. No manuscript change or numerical experiment was performed.
