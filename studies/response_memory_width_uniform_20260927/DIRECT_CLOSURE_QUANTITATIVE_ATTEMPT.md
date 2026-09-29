# Direct closure width analysis: completed estimates and remaining gap

28 September 2026. Continuation of this study's quantitative width question.
This is an internally checked author derivation, not a promoted theorem.
The maintained paper and book have not been changed.

**Outcome.** The direct route gives an order-uniform comparison of the
two actual clocks, an order-uniform root-width estimate for all learned
empirical contractions of an independent population reference, and an
all-time residual L1 comparison driven by a covariance-variation source.
It does **not** yet give the joint quantitative initialized-matrix response
law for the actual autonomous closure. Consequently the requested
`epsilon^(-5/2+o(1))` moving-state corollary remains unproved.

The clocks and finite coefficient count are no longer merely suggestions:
the estimates below are proved. They must not be mistaken for a proof
that the trained neurons themselves are independent Monte Carlo samples.

## 1. Unchanged target and model

Use fixed depth L, fixed m training samples, canonical Gaussian hidden
matrices with entries of variance 1/n, exactly zero initial readout,
and the canonical first-layer/hidden/readout mobilities. Activations have
bounded slope and globally Lipschitz derivative, with linear growth
allowed. Assume the positive initial limiting feature-Gram gap and the
same sufficiently small, fixed label RMS Y as in
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`.

The actual autonomous old-clock closure has

\[
 \tau(t)=1+\int_0^t\rho(s)ds,\qquad
 \rho=\left(m^{-1}\sum_a r_a^2\right)^{1/2}.
\]

Its orthonormal forward and backward moments are H and B. The backward
clock density is `b_a=(r_a/rho) delta_a`, implemented through the raw
physical source `r_a delta_a` without division at zero residual. The
forward prefix of length one is constant; the backward prefix is zero.

\[
 \widehat W_\ell=W_{\ell,0}
     -\frac2{mn}\sum_{a,k<q}B_{\ell,a,k}H_{\ell-1,a,k}^{T}.
 \tag{1}
\]

The initialized matrices are retained and used in both directions.
All histories are the closure's own histories. The established physical
bounds give, simultaneously in q on common initialization events,

\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 \int_0^\infty\rho\le CY,\qquad
 \|\delta_a\|_{\rm RMS}\le CY,\qquad
 \|\dot h_a\|_{\rm RMS}\le CY\rho.
 \tag{2}
\]

The desired new conclusion is a numerical width remainder in

\[
 \left[\int\sup_{t\ge0}
   |\widehat f_{n,q}(t,x)-f_\infty(t,x)|^2\,\mu(dx)\right]^{1/2}
 \lesssim q^{-2+o(1)}+n^{-1/2+o(1)},
 \tag{3}
\]

with quantitative probabilities and width thresholds valid as q grows.
Equation (3) is the target, **not a result of this note**.

## 2. The exact order-uniform moment energy

Write `u_k=sqrt(2k+1)` and let A be lower triangular with
`A_kk=k+1/2` and `A_kj=u_k u_j` for j<k. For one Hilbert-valued
response v its orthonormal moment vector a satisfies

\[
 \partial_\tau a=\frac{u}{\sqrt\tau}v-\frac A\tau a,
 \qquad A+A^T=uu^T.
\]

Completing the square proves

\[
 \frac d{d\tau}\|a\|_{\ell^2}^2
   =\|v\|^2-
      \left\|v-\frac{u^Ta}{\sqrt\tau}\right\|^2.
 \tag{4}
\]

Thus the homogeneous transport is contractive and the integrated input
gain is one, independently of q. Moreover,

\[
 \left\|\frac1n\sum_{a,k}B_{a,k}H_{a,k}^T\right\|_F
 \le \left(\frac1n\sum_{a,k}\|B_{a,k}\|^2\right)^{1/2}
      \left(\frac1n\sum_{a,k}\|H_{a,k}\|^2\right)^{1/2}.
 \tag{5}
\]

These bounds avoid summing q unrelated coordinate errors.
The derivation and exact computational contractions are in
`DIRECT_CLOSURE_WIDTH_ROUTE.md`.

## 3. New result: clock comparison has no order loss

Let two physical histories have clock speeds rho_j, forward histories
h_j, and raw backward measures R_j(t)dt, for j=0,1. Assume

\[
 \int\rho_j\le S,\quad \|h_j\|\le H,\quad
 \|\dot h_j\|\le L_h\rho_j,\quad \|R_j\|\le B\rho_j.
\]

Each history uses its **own** clock, with constant forward and zero
backward prefixes. Let M_q be its paired projected history integral,
so that the learned matrix is `-(2/m) sum_a M_q` in population-scaled
Hilbert norms. Set

\[
 E_h^2=\|h_1(0)-h_0(0)\|^2
       +\max_j\int\rho_j\|h_1-h_0\|^2dt,
\]
\[
 \Delta_R=\int\|R_1-R_0\|dt,\qquad
 \Delta_\rho=\int|\rho_1-\rho_0|dt.
\]

The completed bound is

\[
 \boxed{\|M_{q,1}-M_{q,0}\|_{\rm HS}
 \le B\sqrt S E_h+
       [H+C(1+S)L_h]\Delta_R+
       C(1+S)BL_h\Delta_\rho.}
 \tag{6}
\]

The constant is independent of q, width, and physical terminal time.
The backward histories need not be differentiable. No bounded residual
ratio or common oracle clock is assumed.

The key exact calculation inserts clock length at a position a while
holding the physical forward values and raw backward measure fixed.
If p_h and p_b are their projections on the current interval [0,A],
the derivative of M_q is

\[
 p_b(A)\otimes[h(A)-p_h(A)]
 +\int_a^A[b\otimes p_h'-p_b\otimes h']ds.
 \tag{7}
\]

The two endpoint factors have bounds `CB sqrt(q)` and
`C A L_h/sqrt(q)`. Their q powers cancel. The other terms use

\[
 \int_0^A\|p_h'\|ds\le C A L_h,
 \qquad \|p_h\|_\infty\le H+C A L_h.
 \tag{8}
\]

A complete elementary proof of (8), including
`integral_{-1}^1 |P_k'|<=C sqrt(k)`, appears in Section 6 of
`DIRECT_CLOSURE_CLOCK_STABILITY.md`. Interpolating the two physical
triples and integrating (7) proves (6).

For the actual small-label networks, `S=CY`, `L_h=CY`, `B=CY`.
The clock contribution is therefore `CY^2 Delta_r`, where
`Delta_r=integral ||r_1-r_0||_m`; its coefficient has no q dependence.
Equation (6) compares complete physical-history reconstructions. It
cannot automatically be applied to a reference history repacked under
the other clock: that reference history need not have bounded speed
in the other clock coordinate.

## 4. New result: all learned empirical contractions at once

Take independent copies `(v_i,u_i)` of a population reference pair of
response histories. Within each row v_i and u_i may be correlated.
Put

\[
 K_n(s,t)=\frac1n\sum_i v_i(s)u_i(t)-\mathbb E[v(s)u(t)].
\]

Use the deterministic measure consisting of prefix Lebesgue measure
plus `Y exp(-kappa t)dt` on physical time. It dominates every actual
clock measure on the event (2). If the mixed fourth moment
`V=E[||v||_history^2 ||u||_activity^2]` is finite, independence gives

\[
 \mathbb E\|K_n\|_{\rm HS}^2\le V/n.
 \tag{9}
\]

Every empirical moment/current-field contraction error is the projection
of a column of K_n. Projection contraction therefore gives, pathwise,

\[
 \int_0^\infty\rho_n(t)
           \sum_{k<q}|\xi_{n,k}(t)|^2dt\le\|K_n\|_{\rm HS}^2.
 \tag{10}
\]

The clock and projection may depend on the entire finite network and
on the reference samples themselves. They need not be independent of
K_n. This is why the random clock does not create a new empirical
process complexity or a factor of q.

For one fixed reference law the statement holds simultaneously for all
orders and admissible clocks. If the reference law varies with q,
uniform moment constants give the same estimate along any deterministic
sequence q_n; a simultaneous event for infinitely many different laws
does not follow without another argument.

The exact subtraction between actual learned fields and reference fields
has three types of terms: actual/reference moment differences, field
differences, and (10). It does **not** assume actual trained neurons are
iid. All details, mixed-moment requirements, and the initialized-action
terms left over are in `DIRECT_CLOSURE_EMPIRICAL_RATE.md`.

## 5. New result: the residual norm needed for clock control

Zero readout gives the exact residual equation

\[
 r(t)=-y-2\int_0^t Q(t,s)r(s)ds,
 \qquad Q(t,s)=\frac{H_L(t)^T H_L(s)}{mn}.
\]

Suppose a reference kernel has `Q_*(t,t)>=lambda I` and
`sup_{s<=t}||partial_t Q_*(t,s)||<=a(t)` with integrable a. Subtraction
of the two residual equations has the exact form

\[
 e(t)=D(t)-2\int_0^t Q_*(t,s)e(s)ds,
\]
\[
 D(t)=-2\int_0^t[Q_n(t,s)-Q_*(t,s)]r_n(s)ds.
\]

If D is absolutely continuous with finite total variation, then

\[
 \boxed{\int_0^\infty\|e(t)\|_m dt
 \le\frac{\|D(0)\|_m+\operatorname{TV}(D)}{2\lambda}
           \exp\left(\frac1\lambda\int_0^\infty a(t)dt\right).}
 \tag{11}
\]

Indeed differentiation gives `e'=-2Q_*(t,t)e-2 integral partial_t Q_* e+D'`.
The first term has propagator norm at most `exp(-2lambda(t-s))`.
Variation of constants and integration imply, for `V(T)=integral_0^T||e||`,

\[
 V(T)\le\frac{\|D(0)\|+\operatorname{TV}(D)}{2\lambda}
          +\frac1\lambda\int_0^T a(u)V(u)du.
\]

Gronwall proves (11). In the present small-label setting, the established
reference forward bounds give `integral a<=CY^2`. This step needs no
additional small-label threshold.

Equation (11) controls the time L1 norm of the residual difference, hence
`integral |rho_n-rho_*|`. A bound on the signed primitive of the residual
difference alone would not suffice.

For the iid empirical covariance component of D, its total variation
is also `O_Pr(n^-1/2)` when the explicitly weighted mixed moments of h
and its physical derivative are finite. The proof differentiates K_n
in its current-time argument, uses the iid variance identity at each
(t,s), and integrates by Minkowski; it remains valid when r_n is
adaptive because its deterministic exponential envelope is used.
Section 5 of `DIRECT_CLOSURE_EMPIRICAL_RATE.md` gives the exact constants.
These derivative moments and the actual Gaussian coupling must be
checked separately; an RMS moment-energy bound is not a fourth-moment
or coupling theorem.

## 6. What still prevents (3)

For a correctly identified population reference, let U_* and V_* be its
initialized forward and transpose responses, including matrix reuse.
A coupling to the canonical finite Gaussian arrays must control

\[
 A_F=W_0h_*-U_*,\qquad A_B=W_0^T\delta_*-V_*.
 \tag{12}
\]

These are not empirical scalar averages. Equations (4)--(11) do not
construct a joint coupling of (12), nor give their near-root-width size
and derivative source in (11). This is a direct initialized-operator
problem; the dense-carrier remainder has not been silently assumed small.

The persistence of correlations is visible even before complicated
training. For deterministic h with `||h||^2/n=v^2`, let `z=W_0h` and
let psi be Lipschitz. Gaussian integration by parts gives exactly

\[
 \mathbb E[W_0^T\psi(W_0h)]
       =h\,\mathbb E[\psi'(vZ)],\qquad Z\sim N(0,1).
 \tag{13}
\]

For each entry, integrate the Gaussian `W_{ij}` by parts with variance
1/n, obtaining `h_j E psi'(z_i)/n`, then sum i. Thus reusing the
transpose produces an order-one response term even though W_0 never
changes. During training, differentiating the backward response with
respect to an initialized entry also differentiates the evolving moments
and outer weights. Finite moment state does not remove that response.

Equation (13) is not a counterexample to (3). It explains why iid-reference
variance estimates cannot replace a proof of (12). A bounded state or
contractive history filter does not alone supply that proof either.

A separate finite-query Gaussian-program derivation is recorded in
`DIRECT_CLOSURE_GAUSSIAN_RATE.md`. Its caps, query regularization, and
finite time discretization are proof auxiliaries. A result for that
regularized program is not asserted for the unchanged closure unless
all removal errors are controlled quantitatively.

That auxiliary result preserves the original Gaussian blocks and their
transpose reuse through an exact larger-GOE embedding. Independent query
noise supplies a deterministic covariance lower bound, so a finite-query
coupling theorem applies without an assumed history Gram margin. Its
constants are explicit and its oracle-source Lipschitz estimate is
independent of q. It still uses prescribed population feedback, caps and
query noise. In particular the available full response-mean bound grows
with query count and inverse noise variance; Gaussian innovation tails
alone do not justify removing the caps. No slow logarithmic rate for the
original continuous-time closure follows from that calculation either.

## 7. Consequence for the compression claim

The current proved all-time predictor bound remains

\[
 \mathcal E_\mu(\widehat f_{n,q},f_\infty)
 \le C_\mu q^{-2}\exp\{K\sqrt{\log(e+q)}\}+\eta_{n,\mu},
 \qquad \eta_{n,\mu}\longrightarrow0\quad\hbox{in probability}.
 \tag{14}
\]

There is still no proved numerical near-root-width bound on eta under
exactly the stated hypotheses. If (3) were proved, the choices
`q=epsilon^(-1/2+o(1))` and `n=epsilon^(-2+o(1))` would give the
moving-state count

\[
 2(L-1)mnq+n(d+1)=\varepsilon^{-5/2+o(1)}
\]

for fixed data dimension, sample count and depth. This implication is
algebraically correct, but its missing premise is not established by
the new empirical estimates. Fixed W_0 storage and dense matrix actions
remain outside that moving-state count.

The precise advance of this attempt is removal of the order-dependent
clock loss and of any moment-count loss in reference empirical sampling,
together with identification of a sufficient all-time residual source
norm. The complete direct quantitative width theorem remains open.

## Verification and provenance

The coordinator checked the complete clock proof, including the
Mehler--Dirichlet derivation, the two-boundary-coefficient derivative
identity, the physical-history interpolation, and the residual resolvent.
A deterministic numerical algebra check of the insertion identity at
q=1,2,7,16,32 had maximum discrepancy 2.36e-11; the polynomial derivative
identity at degrees 1,2,7,16,30 had maximum discrepancy 1.64e-11.
These are normalization checks, not substitutes for the analytic proofs.
No model training or manuscript experiment was run.

Three existing scoped author agents continued the clock, empirical,
and Gaussian-response calculations. They were not independent reviews.
The existing complete text of
[Reeves's Gaussian coupling paper](https://arxiv.org/abs/2508.10782) was
revisited for the finite-query comparison; a narrow external search did
not supply an applicable continuous-time theorem. No new result was
promoted or committed.
