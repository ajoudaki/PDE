# Positive convergence continuation: proved mechanisms and the remaining triple gap

Date: 2026-09-18. This continues the exact initialized p=1 question in this
study. It changes neither the circle data domain nor the model, initialization,
physical metric, ridge, or unhalved unit-label square loss. The requested
unconditional exponential potential for a general genuine three-input family
is **still open**. No conditional result below is claimed to complete it.

Three fresh routes developed candidates independently from the established
equations and this study's complete initialized/stationary proofs. Their
frozen reports are `global_positive_route.md`, `open_family_route.md`, and
`energy_geometry_route.md`. Cross-pollination occurred only after initial
candidate freeze and is recorded in the respective reports. No new numerical
experiment was performed. A literature search returned related linear-network
and restricted-training results, but no external theorem is a proof dependency
of this continuation.

## 1. An unconditional global mechanism for a single residual

Let the signed scalar prediction be

\[
 F(w,M,c)=\langle c,H(w,M)\rangle_{L^2(\Omega_2)},
 \qquad L=(1-F)^2,
\]

on a proved invariant reduction of the full closure, with its unchanged
product metric and c(0)=0. If H(0) is nonzero, then

\[
                  L(t)\le \exp[-4\|H(0)\|_2^2t].
\]

This is not a frozen-feature argument. With the proof clock
ds/dt=2(1-F), and hidden variables denoted collectively by theta, the
exact gradient equations give

\[
 c_s=H,\qquad \theta_s=DH^*c,\qquad c_{ss}=DH\,DH^*c.
\]

For q=||c||_2>0,

\[
 q q_{ss}=\|c_s\|_2^2-q_s^2+\|DH^*c\|^2\ge0.
\]

Since q_s(0+)=||H(0)||_2, the readout radius is convex in this clock,
and F_s=(q q_s)_s>=||H(0)||_2^2. This gives the displayed physical-time
inequality, with potential Phi=L. The available signal time is at most
1/||H(0)||_2^2. Direct clock-speed bounds then prove a finite limit for
w-g, c and M; boundedness is a conclusion, not a hypothesis.

The complete proof and function-space justification are in
`global_positive_route.md`, Sections 1--2. It covers an arbitrary single
signed circle direction, not just an axis. It also applies to reflected
equal-weight pairs whenever the exact data symmetry leaves one residual.

## 2. A genuine open two-input family, with all obligations closed

For sufficiently small fixed epsilon>0, take normalized directions

\[
 x_1/\sqrt2=(\cos\epsilon,\sin\epsilon),\qquad
 x_2/\sqrt2=(-\cos\epsilon,\sin\epsilon),
\]

labels (+1,-1) and equal masses. The signed-coordinate reflection is an
exact symmetry of the prescribed dictionary. It forces f_2=-f_1, so
H=(H_1-H_2)/2 and Section 1 applies without changing the metric.

The proof in `open_family_route.md`, Sections 6--8, also establishes that
the two upper codes at the fitting endpoint are nonparallel. Its key
estimate is that the transverse angular derivative at the limiting axis
reference is strictly positive. This follows from the exact initialized
Gaussian regression function, not an assumed rotation covariance. Thus the
endpoint has a positive full two-output tangent Gram.

Consequently an open neighborhood permits independent perturbations of
both input directions and of the positive masses. Every canonical trajectory
in a sufficiently small such neighborhood converges to a finite fitting
state and has exponentially decreasing loss. Here is the additional
prefix-to-tail detail needed to obtain Phi=L from time zero, rather than
only an exponential tail.

Choose a finite T at which the reference is inside the regular fitting
ball, with the strict first-exit margin proved in Section 3 of that report.
The reference has L(t)>0 and -L'(t)/L(t)>=4||H(0)||_2^2 on [0,T].
This ratio is continuous in the state and data wherever L>0. Compactness
of [0,T], finite-time continuous dependence, and positivity of its minimum
loss therefore give a data neighborhood on which the ratio remains at
least 2||H(0)||_2^2 throughout this prefix. Shrink the neighborhood so all
trajectories also satisfy the strict fitting-ball entrance condition at T.
The first-exit proof yields -L'/L>=4k on the entire tail for a common k>0.
Thus with

\[
 \lambda=\min\{2\|H(0)\|_2^2,4k\}>0,
 \qquad \Phi(S)=L(S),
\]

every trajectory in this open data neighborhood satisfies
Phi'<=-lambda Phi and Phi(t)<=e^{-lambda t}Phi(0). If a perturbed
trajectory reaches zero loss, it stays there and the conclusion is unchanged.
The potential uses only the current state and fixed data. The proof constructs
the neighborhood and constants from a proved reference; it assumes no future
conditioning of the perturbed trajectory. Their numerical sizes are not
evaluated. Both hidden blocks and the readout move, as proved by their
nonzero leading velocities and continuity under sufficiently small perturbations.

This is a data-only positive theorem, but it remains a two-input theorem.
It does not resolve the requested genuine-three-input extension.

## 3. Exact extra term for several residuals

Use the probability-weighted data norm. Write e=y-f, rho=||e||, v=e/rho,
H_v=sum_i p_i v_i H_i, and let K be the full physical prediction Gram
operator. It contains all three gradient blocks. In the clock ds/dt=2rho,

\[
 \rho_s=-\langle v,Kv\rangle,\qquad
 v_s=-\frac{Kv-\langle v,Kv\rangle v}{\rho}.
\]

The exact readout-radius equation becomes

\[
 q q_{ss}=\|H_v\|_2^2-q_s^2
       +\|(D H_v)^*c\|^2+\langle y,v_s\rangle.
\]

Only the final term is absent in the single-residual theorem. It is caused
by the actual evolving direction of the residual vector. Positive
semidefiniteness of K does not give that term a sign. This is a concrete
missing estimate for this proof mechanism, not a proof that another potential
cannot exist. Its derivation is complete in `global_positive_route.md`,
Section 3.

Nor does arbitrary splitting of the solved reference repair the gap.
For three nearby signed directions the weakest feature scale is quadratic
in their angular separation, and its Gram scale is quartic. A nonzero
endpoint angular curvature yields a residual in that mode of the same
quadratic order. Correcting it can require a finite change of state even
as the inputs coalesce. The relevant conditional lower bound and its exact
nonzero-curvature premise are in Section 4 of that report. No assertion
that this endpoint curvature is nonzero was needed or made.

## 4. A positive three-code interpolation theorem

There is a useful current-state theorem that avoids treating desirable
class collapse as a singularity. Set z_i=M a_i and sign-fold them as
xi_i=y_i z_i. Fix positive r,R,delta. For at most three codes satisfying

\[
 r\le |\xi_i|\le R,\qquad |\xi_i+\xi_j|\ge\delta\quad(i\ne j),
\]

there is an odd interpolating readout c_* with uniformly bounded L2 and
L-infinity norms, depending only on these constants and the canonical
upper law. No lower bound on |xi_i-xi_j| is required. Exact compatible
collisions and arbitrarily unequal separation scales are allowed.

The complete proof is `energy_geometry_route.md`, Section 8. It constructs
normalized first and second divided differences, proves independence of
the confluent tanh derivatives, and observes that the constant signed
targets transform to (1,0,0). Thus an ill-conditioned ordinary Gram does
not force a large interpolating readout for these compatible targets.

The actual-flow identities

\[
 \frac{d}{dt}\|c\|_2^2
 =1-4\sum_i p_i(f_i-y_i/2)^2\le1,
 \qquad \|c(t)\|_2^2\le t,
\]

and

\[
 \|\dot c\|_2^2\ge
       \frac{4L^2}{(\|c\|_2+\|c_*\|_2)^2}
\]

then give a residual-specific progress estimate at each protected state.
It needs no derivative of the chosen comparator. However, this does not
establish that the displayed geometric constants persist along training.
The conditional logarithmic fitting bound in the report is retained as a
consequence of a precise additional hypothesis, not as the requested theorem.

## 5. Status and stopping boundary

The independent scalar-mechanism audit is `audit_global_positive.md`; the
independent interpolation audit is `audit_collision_interpolation.md`.
The primary agent checked the complete open-family report and reconstructed
the prefix-to-tail argument in Section 2 above. These are internal checks,
not promotion. Source versions and audit limitations are recorded in the
README and validation record.

The strongest completed initialized exponential result in this continuation
is still the open two-input family. For the circle, no genuine-three-input
reference with proved regular fitting endpoint has been established. Nor
has the residual-rotation term been controlled or the three-code protection
proved along the prescribed trajectory. These remain substantive, distinct
obligations. None of the new route obstructions is a counterexample to the
desired initialized three-input theorem.

An optional scope question asked whether the user would like the same study
broadened to the canonical p=1 construction in input dimension three. In the
absence of an answer, this continuation stays on the prescribed circle and
makes no three-dimensional theorem claim.
