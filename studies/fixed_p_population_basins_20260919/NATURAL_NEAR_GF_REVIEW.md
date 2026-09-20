# Informed internal review of the continuous near-GF combination

2026-09-19. **PASS for the explicitly defined continuous corrected
optimizer with rare activation and fitted-boundary absorption.** No
blocking mathematical error was found. The exponential expected actual
loss bound, unconditional compact-time GF coupling, global continuation,
and almost-sure finite strong fitted endpoint are supported by the
complete proofs reviewed below. This is an informed expanded internal
review, not a blind promotion review.

The random readout force is uniformly small along the process. The full
modification need not be small: the conditioning correction can be large
near a singular feature Gram, and the unconditional GF approximation also
uses delayed activation. The synthesis states these limitations correctly.

## 1. Frozen inputs and scope

The complete new inputs were read, with the following verified hashes:

| File | SHA-256 |
|---|---|
| NATURAL_NEAR_GF_RESULTS.md | `8b8c67b482a5a850284b0ac0013e3d25aa4c6534bd2556abafdc94a1a56f5742` |
| NATURAL_CONDITIONING_FLOW.md | `0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0` |
| NATURAL_TANGENT_NOISE.md | `12272146e901e97014a035ab2a9079d8161c55d0d838fe14c234396ae3ddd0b0` |

The initial complete reads used combination hash
`aade8ff1f8715535fe82e55bf52e17ac7cf7a578e01155d74741709d18e98ebf`
and tangent hash
`f261c48ace7332331c2363adf3c6534bce7435744ec7cf4e26f6daf820477fb2`.
The supervisor subsequently supplied narrow scope clarifications: small
noise is bounded uniformly along initialized nonincreasing-loss paths,
not over unbounded-loss ambient states, and the P=I tangent comparison
says “forcing realization” rather than “mobility/forcing realization.”
The changed passages were checked directly. Reversing exactly those
text changes reconstructs both initial hashes, verifying that all
definitions, estimates, and proofs are otherwise unchanged. The PASS
applies to the final hashes in the table.

The analytic activation lemma is in the corrected
`NATURAL_CONTINUOUS_ROUTE.md`, SHA-256
`64cd681fbe3eda3ead3486e8c6437852e434f12e4259fc6f45121fd75d87d216`.
Its only changes from the version fully read in the preceding scoped
review are the two checked hidden-regularity wording repairs; reversing
them reconstructs the original frozen hash. The lemma itself is unchanged.

The already-read scientific model and initialization inputs are the
complete `ESCAPE_AND_LIMITS.md`, `INITIAL_EXCLUSION.md`, the explicitly
supplied `INITIAL_REVIEW.md` including its order-one extension, the exact
assigned `docs/global_nonlinear.md` spans 13161–13786 and 15146–15528,
and `docs/NOTATION.md`. Their proofs and definitions, rather than earlier
verdicts, support the present checks. The previous scoped assignment also
exposed the rare-refresh and deadline candidates and their named
dependencies, as recorded in `NATURAL_JUMP_REVIEW.md`; this follow-up is
therefore informed rather than a fresh blind attempt.

No other review or study was read. No experiment, numerical computation,
Git-index operation, or candidate-file edit was performed. The required
rigorous-math and adversarial-audit skill instructions remain in force.

## 2. Exact domain, gradients, and local regularity

Use the original physical Hilbert state S=(w,c,M), finite compatible
binary data, positive masses, and the unhalved weighted squared loss.
After exact duplicate/antipode aggregation, define A, K=AA*, e and L=|e|²
as in the candidate. The readout gradient is

\[
z=\nabla_cL=2A^*e,\qquad \|z\|^2=4e^TKe.
\]

On the open domain D={K>0}, put R=tr(K^{-1}), h=1+epsilon R and
Phi=hL. R is independent of c. Thus

\[
\nabla\Phi=h\nabla L+\varepsilon L\nabla R,
\qquad \nabla_c\Phi=hz.
\]

These identities are in the unchanged population/Frobenius metric; no
extra particle factor or change of loss normalization appears.

The gradient regularity used in NATURAL_CONDITIONING_FLOW.md is valid.
The maps a_i:L2->R^(d1) are C1 with Lipschitz derivative: bounded tanh''
controls the Taylor remainder by C||delta w||² and controls the operator
norm difference of their derivatives by C||delta w||. The upper features
and Gram entries are smooth functions of the finite a_i and M, with
bounded derivatives on bounded sets. Matrix inversion preserves the
required C1,1 estimates on K>=k0 I. Consequently R and Phi have locally
Lipschitz Hilbert gradients there. This argument does not require C2
regularity for a general L2-valued tanh Nemytskii map.

The safeguard beta also has a valid locally Lipschitz extension at zero
loss inside D. To make the source's claim explicit, write
q=<nabla L,nabla R>=v(S)·e, with locally Lipschitz finite-dimensional
coefficient v(S); the prediction Jacobian and nabla R give that
coefficient. Then

\[
\beta=\frac{\varepsilon |e|^2[-v(S)\cdot e]_+}
                    {4e^TK(S)e}.
\]

On a local domain K>=k0 I, this is homogeneous of degree one in e,
with a uniformly Lipschitz angular factor and value O(|e|). For two
comparable nonzero radii the angular bound proves Lipschitzness; for
noncomparable radii the O(|e|) bound and the reverse triangle inequality
do so. Differences of K and v contribute at most C|e| times their
differences. Extending beta=0 at e=0 therefore yields local Lipschitzness
in the full state. At zero loss every drift term is zero.

The tangent operator B(z) is a locally Lipschitz operator-valued map:
its numerator ||z||²I-z tensor z is polynomial in z and its denominator
is bounded below by one. Since sqrt(L)=|e| is locally Lipschitz, each
fixed-noise interval has a locally Lipschitz ODE on D, including at
zero loss. State paths are locally absolutely continuous and the ODE
holds almost everywhere/in integral form; refresh and activation times
need not admit a classical derivative.

## 3. Potential, actual loss, and tangent forcing

Let k=lambda_min(K)>0. Since R>=1/k,

\[
k h\ge\varepsilon,\qquad
\|\nabla\Phi\|^2\ge h^2\|z\|^2
\ge4kh\Phi\ge4\varepsilon\Phi.
\]

This lower bound uses the readout component alone and holds throughout
D. It does not assume a uniform lower bound on k along a trajectory.

For the general readout mobility in NATURAL_CONDITIONING_FLOW.md, let
a=1-nu>0 and b=1+nu. Because the mobility is the identity on the hidden
blocks, P nabla R=nabla R. Direct differentiation gives

\[
\dot L=-h\langle\nabla L,P\nabla L\rangle
        -\varepsilon L[q]_+
\le-4a\varepsilon L,
\]
\[
\dot\Phi=-\langle\nabla\Phi,P\nabla\Phi\rangle
          -\beta h\|z\|^2
\le-4a\varepsilon\Phi.
\]

Here the identity q+[-q]_+=[q]_+ verifies the safeguard sign exactly.
The bounds and the readout-mobility construction in that dependency
therefore hold for every admissible realization, including nu=0.

The combined candidate uses P=I and adds the different forcing
n=(0,nu sqrt(L)B(S)U_t,0). For z!=0, B is zero along z and equals
||z||²/(1+||z||²) times the identity on z-perpendicular; it is zero
at z=0. Hence ||B||<=1 and

\[
\langle\nabla L,n\rangle=0,
\qquad\langle\nabla\Phi,n\rangle=0,
\qquad\|n\|\le\nu\sqrt L.
\]

These are pathwise identities, unaffected by correlations between held
noise and the evolving state. The process is an ODE with colored forcing,
so there is no Itô quadratic-variation term. Therefore after activation

\[
L(t)\le L_*e^{-4\varepsilon(t-T_\varepsilon)},
\qquad
\Phi(t)\le\Phi_*e^{-4\varepsilon(t-T_\varepsilon)}.
\]

No smallness restriction on nu is needed for these inequalities. The
combined choice 0<=nu<=epsilon ensures a small noise velocity; it does
not import the separate nu<1 restriction of the mobility variant.

## 4. Finite travel and global continuation

Write D_t=-dot(Phi). For the general mobility drift,
D_t>=a||nabla Phi||² and D_t>=beta h||z||². Using the previous lower
bounds yields separately

\[
\|P\nabla\Phi\|\le\frac{bD_t}{2a\sqrt{\varepsilon\Phi}},
\qquad
\beta\|z\|\le\frac{D_t}{2\sqrt{\varepsilon\Phi}}.
\]

Integration of -dot(Phi)/sqrt(Phi) proves the dependency's finite-travel
bound (15) and its subinterval version. For P=I with tangent noise,
that noise contributes nothing to D_t, so the deterministic part travels
at most 2sqrt(Phi_*/epsilon). Its added variation is bounded by

\[
\int_{T_\varepsilon}^{\infty}\nu\sqrt{L(t)}\,dt
\le\frac{\nu\sqrt{L_*}}{2\varepsilon}.
\]

All these inequalities apply first on partial maximal intervals in D;
global existence is not being assumed to prove its own travel bound.
Finite travel makes the state Cauchy at every finite maximal endpoint,
so norm blowup is excluded. If the limiting K is positive, the limiting
finite state lies in D and local existence continues the solution.
If K becomes singular, R diverges and bounded Phi=L(1+epsilon R)
forces the limiting actual loss to be zero by continuity. The stated
absorbing convention then provides a unique continuation of the defined
process. It is a convention at the singular endpoint, not a claim that
the inverse-Gram formula extends there. The potential may have the
explicitly allowed downward jump, while the state and loss remain
continuous. The same argument excludes positive-loss boundary exits.

If no finite boundary exit occurs, total variation on the infinite
interval is finite. Completeness of the physical Hilbert space gives a
finite strong endpoint, and the actual-loss exponential bound makes
its loss zero. This proves the continuous conditioning and tangent-noise
dependencies from any finite starting state in D, not only canonical
bounded fields. The fitted-boundary absorption is an essential part of
the global theorem as formulated.

## 5. Random activation and the combined bounds

The initialization inputs prove K(S0)>0 at p=1,2. For the original
canonical GF, bounded shifted L-infinity coordinates (w-g,c,M) remain
available on every finite interval. Their small complex neighborhoods
keep both layers' preactivations in common pole-free tanh strips.
Holomorphic Picard iteration therefore gives local time analyticity.
The bilinear analytic extension of each Gram entry makes det K(t)
real analytic. Since det K(0)>0, its zeros are isolated and locally
finite, hence countable. An independent exponential activation time
avoids them almost surely. No uniform coercivity or absence of isolated
deterministic-time zeros has been inferred.

Let T_*=T_epsilon and S_*=S^0(T_*). Almost surely T_* is finite and
S_* is a finite state in D. Its L_*<=L0 and Phi_* are finite, although
Phi_* need not have a finite expectation. The results of Sections 3–4
apply pathwise from S_*. In particular the prefactor in the postactivation
actual-loss estimate is L_*, bounded deterministically by L0. Thus

\[
\begin{aligned}
E L_\varepsilon(t)
&\le L_0e^{-\varepsilon t}
  +L_0\int_0^t\varepsilon e^{-\varepsilon s}
                         e^{-4\varepsilon(t-s)}\,ds\\
&=L_0\left(\frac43e^{-\varepsilon t}
                  -\frac13e^{-4\varepsilon t}\right).
\end{aligned}
\]

This computation needs no moment of Phi_* and no expected bound on
postactivation state norm or variation. The actual hitting-time bound
follows pathwise from
tau_a<=T_*+(4epsilon)^(-1)log(L0/a), and the displayed probability
bound follows from monotonicity and Markov's inequality.

The combined full-path variation has the almost-sure finite bound

\[
\operatorname{Var}S
\le\sqrt{T_*L_0}
    +2\sqrt{\Phi_*/\varepsilon}
    +\frac{\nu\sqrt{L_*}}{2\varepsilon}.
\]

The first term is original-GF energy and Cauchy–Schwarz before
activation. This explicitly verifies the global strong endpoint without
silently replacing almost-sure finiteness by integrability. The
probability-zero singular-activation convention does not change these
almost-sure or expected-loss conclusions.

Before activation the modified and original trajectories coincide by
uniqueness. Consequently for every fixed horizon T and threshold d>0,

\[
P\{\sup_{t\le T}\|S_\varepsilon(t)-S^0(t)\|>d\}
\le P(T_\varepsilon\le T)=1-e^{-\varepsilon T}.
\]

The coupling T_epsilon=E/epsilon with one positive Exp(1) variable
makes the paths eventually exactly equal on each prescribed compact
interval. Countably many integer horizons give the asserted almost-sure
local uniform coupling. It requires neither control of activated-path
moments nor approximation across an activated Gram degeneracy.

## 6. Scope audit and remaining claims

| Claim under attack | Strongest obstruction | Check and consequence |
|---|---|---|
| Safeguard well-posedness | Division by a vanishing readout gradient | On K>0 it is a degree-one Lipschitz residual function extended by zero; local uniqueness holds |
| Global continuation | Singular K or unbounded state before fitting | Finite travel excludes norm blowup; bounded potential forces zero loss at a singular endpoint; explicit absorption closes the process |
| Tangent forcing preserves rates | Colored noise can correlate with the current state | Orthogonality is pointwise, so no mean-independence assertion is needed |
| Expected loss bound | Activation may give an enormous random inverse Gram | Actual-loss prefactor is bounded by L0; no moment of the activation potential is used |
| Compact-time closeness | Strong postactivation correction might destroy approximation | Exact no-activation coupling proves the claimed mode; no stronger state-moment or all-time approximation is inferred |
| Small-noise interpretation | Small forcing could be confused with a uniformly small full correction | Only the noise is bounded by epsilon sqrt(L0); inverse-Gram correction can be large |

Immediate-activation comparison on regular reference intervals is also
valid. A compact original-GF path with K>0 throughout has a positive
minimum eigenvalue. On a fixed neighborhood, the conditioning correction
is uniformly O(epsilon), the tangent forcing is uniformly O(nu), and
ordinary GF is Lipschitz. Gronwall plus the stated first-exit argument
gives O(epsilon+nu) state error. This argument does not extend through
an isolated reference Gram zero merely because such zeros have measure
zero. The synthesis keeps these two approximation mechanisms distinct.

The nondegenerating-rate diagnostic in Section 5 is correct: fixed-time
state convergence in probability gives loss convergence in probability;
an almost-sure subsequence and Fatou transfer any epsilon-uniform
expected exponential upper bound to deterministic original GF at that
time. This identifies the strength of such an unproved theorem without
asserting its impossibility.

The construction changes every block's deterministic drift after
activation, preserves continuous state paths, and has no proposal clock.
Its physical-time rate is for that changed vector field, which can
accelerate strongly near degeneracy. It gives no finite-precision or
computational-cost theorem. Taking nu=0 keeps every fitting guarantee:
the conditioning correction, rather than ordinary random noise alone,
provides the convergence mechanism. The canonical orders remain p=1,2.

The wording that equations “run at every physical time” in the tangent
note is understood in the explicitly stated piecewise-ODE sense: the
state is continuous and the equation holds almost everywhere/in integral
form. No classical derivative at activation or a noise refresh is needed
or proved. This is a harmless regularity clarification, not a gap in the
combined result.

Under the stated rare activation, continuous conditioning correction,
bounded tangent colored forcing, and singular fitted-endpoint absorption,
the combined candidate passes this informed internal check. Original GF
and original GF plus only a uniformly small ordinary random perturbation
retain their unresolved all-time fitting status.
