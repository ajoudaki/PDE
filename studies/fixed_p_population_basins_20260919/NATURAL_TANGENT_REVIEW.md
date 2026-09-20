# Internal mathematical review of the tangent-noise extension

2026-09-19. **PASS for the explicitly defined colored-forcing ODE and its
absorbing continuation.** No unresolved mathematical issue was found.
This is an informed continuation of the separate internal conditioning-flow
review, not a fresh independent promotion review.

The bounded tangent force preserves both exact dissipation inequalities.
Its extra travel is integrable, including on a partial maximal interval,
so the global existence, strong endpoint, and fitted singular-absorption
arguments remain valid. The comparison with ordinary GF retains the
reference positive-Gram hypothesis.

## 1. Inputs and correction record

The complete final NATURAL_TANGENT_NOISE.md was read and checked at SHA256
12272146e901e97014a035ab2a9079d8161c55d0d838fe14c234396ae3ddd0b0.
Its complete conditioning-flow dependency was previously checked and
remains unchanged. All scientific inputs are exactly those authorized for
the conditioning-flow review, plus this tangent-noise note. No other
study, route, review, task history, experiment, or external stochastic
result was used.

The initial assigned tangent-note hash was
f261c48ace7332331c2363adf3c6534bce7435744ec7cf4e26f6daf820477fb2.
The revision clarifies that the noise bound is uniform along initialized
loss-decreasing trajectories, not over arbitrary ambient states of
unbounded loss, and changes “mobility/forcing realization” to “forcing
realization” because the displayed extension sets \(P=I\). No estimate
changed. The complete revised note was reread, and these wording
clarifications are closed.

Exact final fingerprints:

| Input | SHA256 |
|---|---|
| NATURAL_TANGENT_NOISE.md | 12272146e901e97014a035ab2a9079d8161c55d0d838fe14c234396ae3ddd0b0 |
| NATURAL_CONDITIONING_FLOW.md | 0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0 |
| ESCAPE_AND_LIMITS.md | 544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2 |
| INITIAL_EXCLUSION.md | 34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c |
| INITIAL_REVIEW.md | 6fd58a9faa1b07a0eaa53fe9595b63180b225e72df35a7f50fe9f6e629d64baf |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md (whole-file fingerprint; only assigned ranges read) | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/global_nonlinear.md:13161–13786 | 0a00ff65642c57068bc3cbf8dcda5a3024edd8e12213a521168fb4db9b303bb1 |
| docs/global_nonlinear.md:15146–15528 | 3815d81705fac51fcd5b5489b6f6f961021cba525acf88e74bdc82fe818ae386 |

The required rigorous-math skill and adversarial-audit instructions were
applied. No candidate or dependency was edited. The prior authorized
INITIAL_REVIEW.md is used for its order-one scientific extension, not as
a substitute for verifying that extension.

## 2. Tangency, operator bound, and nonvacuity

For a readout vector \(z\), let \(z\otimes z\) denote
\(u\mapsto z\langle z,u\rangle\). Then

\[
B(z)=\frac{\|z\|^2I-z\otimes z}{1+\|z\|^2}.
\]

Its selfadjoint numerator is zero on \(\operatorname{span}\{z\}\)
and equals \(\|z\|^2I\) on the orthogonal complement. Thus

\[
\langle z,B(z)u\rangle=0,\qquad
\|B(z)\|_{\rm op}\le\frac{\|z\|^2}{1+\|z\|^2}\le1,
\]

including \(z=0\), where \(B=0\). In the present infinite-dimensional
readout space the first norm inequality is equality for \(z\ne0\).
For \(N(S,U)=\nu\sqrt L\,B(z)U\) and \(\|U\|\le1\), this proves

\[
\|N(S,U)\|\le\nu\sqrt L.
\]

Along the initialized process, \(L_0=1\), so the actual physical noise
velocity is at most \(\nu\), with no Gram lower bound needed. The same
statement for a general starting state has constant \(\sqrt{L_0}\).
There is no uniform constant over arbitrary states with unbounded loss.

The construction can supply a nonzero force without future information.
Under the canonical initialization, each \(H_i\) is odd under the upper
mark reversal, and

\[
z_0=-2\sum_i\mu_i y_iH_i
\]

is a nonzero odd field: nonzero follows from \(K_0>0\) and nonzero labels.
The fixed constant field \(q=1\) has norm one and is orthogonal to \(z_0\).
Choosing the permitted independent signs \(U_j=\pm1\) gives

\[
N(S_0,U_0)
 =\pm\nu\,\frac{\|z_0\|^2}{1+\|z_0\|^2},
\]

which is nonzero for \(\nu>0\). This verifies nonvacuity of the random
force. It does not assert that every permitted forcing law has nonzero
effect, or that this exploration improves training.

## 3. Local regularity at zero loss

The map \(z\mapsto z\otimes z\) is a continuous quadratic map into bounded
operators; explicitly,

\[
\|z\otimes z-\widetilde z\otimes\widetilde z\|_{\rm op}
\le(\|z\|+\|\widetilde z\|)\|z-\widetilde z\|.
\]

Its denominator \(1+\|z\|^2\) is everywhere positive. Therefore \(B\)
is smooth as an operator-valued map and locally Lipschitz in operator
norm, including at zero. The residual norm \(\sqrt L=|e|\) is locally
Lipschitz despite its possible failure to be differentiable at \(e=0\).
The already checked \(C^{1,1}\) loss gives a locally Lipschitz \(z(S)\).
Products of these locally bounded Lipschitz maps prove local
Lipschitzness of \(N(S,U)\), uniformly for \(\|U\|\le1\).

There is also a direct vanishing check. Since
\(\|z\|=\|2A^*e\|\le C|e|\) on every bounded state neighborhood,

\[
\|N(S,U)\|\le\nu |e|\,\|z\|^2=O(\nu|e|^3)
\]

near a fitted state. No denominator involving \(\|z\|\) or \(L\) is
introduced. Together with the reviewed zero-loss extension of the
safeguard, this supplies a locally Lipschitz full drift on \(K>0\).
At zero loss it vanishes.

Each refresh interval has a unique local Hilbert-space solution by
the contraction argument for its integral equation. The fixed positive
refresh interval prevents finite-time accumulation of changes. State
paths are continuous across refresh times; their velocities and the
prescribed forcing may jump there. The term “continuous” refers to
continuous-time state evolution, not to continuity of \(U_t\).

## 4. Exact loss and potential derivatives

Set \(h=1+\varepsilon R\). Since \(R\) has no readout dependence,

\[
\nabla_cL=z,\qquad \nabla_c\Phi=hz.
\]

The added force therefore contributes exactly

\[
\langle z,N\rangle=0,\qquad
\langle hz,N\rangle=0
\]

to the two chain rules. These equalities hold at the current, possibly
randomly perturbed state, so state/forcing correlations do not affect
them. With \(P=I\), the reviewed deterministic algebra yields

\[
\dot L=-h\|\nabla L\|^2
        -\varepsilon L[\langle\nabla L,\nabla R\rangle]_+
       \le-4\varepsilon L,
\]
\[
\dot\Phi=-\|\nabla\Phi\|^2-\beta h\|z\|^2
       \le-4\varepsilon\Phi.
\]

The rate is independent of \(\nu\), so no upper restriction on the
noise amplitude is needed for these estimates. The bounds hold on
each sample path, not merely in expectation. The symmetry and
independence of fresh draws give their stated conditional mean-zero
property but are not needed for the dissipation proof.

The equation is an ordinary differential equation with a bounded,
piecewise constant driving field and state-dependent noise coefficient.
The state is differentiable between switches and locally absolutely
continuous. The ordinary first-order chain rule applies; there is no
Itô correction or stochastic-integral assertion.

## 5. Total travel and global continuation

Along this perturbed path, \(D_t=-\dot\Phi\) still satisfies exactly

\[
D_t=\|\nabla\Phi\|^2+\beta h\|z\|^2.
\]

The core inequalities
\(\|\nabla\Phi\|\ge2\sqrt{\varepsilon\Phi}\) and
\(h\|z\|\ge2\sqrt{\varepsilon\Phi}\) therefore give

\[
\|-\nabla\Phi-\beta(0,z,0)\|
\le\frac{D_t}{\sqrt{\varepsilon\Phi}}.
\]

Integrating on any domain-contained subinterval \([s,t]\) gives a
deterministic-part travel bound

\[
\frac2{\sqrt\varepsilon}
 \bigl(\sqrt{\Phi(s)}-\sqrt{\Phi(t)}\bigr).
\]

The exponential loss estimate gives a separate noise-travel bound

\[
\int_s^t\|N\|\,dr
\le\nu\sqrt{L_0}\int_s^t e^{-2\varepsilon r}\,dr.
\]

Both estimates apply before an arbitrary maximal endpoint, so using
them to prove continuation is not circular. Their sum is integrable.
At a finite endpoint the first bound has vanishing tails because
\(\Phi\) is monotone, and the second does because its integrand is
bounded and integrable. Thus the state is Cauchy in the complete
Hilbert space; finite norm blowup is excluded.

If the limiting Gram is positive, local existence continues the solution.
If it is singular, continuity of \(K\) gives \(R\to\infty\) and bounded
\(L(1+\varepsilon R)\) forces \(L\to0\). The stipulated absorbing
continuation is therefore fitted, and no positive-loss singular exit
occurs. Its state path remains continuous and absolutely continuous;
only the declared extension of \(\Phi\) may have a downward jump.
Uniqueness is that of the piecewise ODE with this explicit absorption
rule, not a claim of regular ODE uniqueness at all singular states.

After continuation, the total variation estimate is exactly

\[
\operatorname{Var}_{[0,\infty)}S
\le2\sqrt{\Phi(0)/\varepsilon}
  +\frac{\nu\sqrt{L_0}}{2\varepsilon}.
\]

If the domain is never exited, the same subinterval estimates give
Cauchy tails at infinity and hence a finite strong endpoint. The
exponential bound and loss continuity make it fitted. If absorption
occurs earlier, the conclusion is immediate. This covers every
admissible realization and also \(\nu=0\).

## 6. Near-GF scope and adversarial outcome

For a fixed ordinary-GF reference interval with positive Gram at every
time, compactness of that path gives a positive minimum eigenvalue
and a bounded tube with a uniform Gram gap. The deterministic drift
difference is \(O(\varepsilon)\) there by the checked core argument.
The new force is \(O(\nu)\) there, uniformly over all \(\|U_j\|\le1\).
Subtracting the integral equations and using the ordinary-GF local
Lipschitz bound therefore gives

\[
\sup_{t\le T}\|S^{\varepsilon,\nu}(t)-S^0(t)\|
\le C_T(\varepsilon+\nu)
\]

for sufficiently small \(\varepsilon+\nu\), with the first-exit
argument extending the comparison over the entire reference interval.
No derivative of the forcing, or of its switching times, enters this
argument. The constants are independent of the chosen directions and
signs with norm at most one.

The strongest potential obstructions were: singular normalization at
zero residual; a missing second-order stochastic term; tangent noise
destroying the finite-travel proof; finite exit at positive loss; and
an unjustified ambient or all-horizon small-perturbation assertion.
They are respectively resolved by the nonsingular quadratic formula
for \(B\), the explicitly ordinary piecewise-ODE interpretation, the
integrable \(\nu\sqrt L\) travel estimate, the bounded-potential boundary
argument, and the final explicit trajectory/positive-Gram restrictions.
The only wording clarification raised during the review is closed in
the final hashed input.

No claim is proved for a Brownian diffusion, ordinary minibatch noise,
an arbitrary untargeted additive force, or globally small total drift
relative to ordinary GF. The forcing enters the ODE additively but its
coefficient is state dependent. Almost-everywhere positivity of the
reference Gram cannot replace its positivity throughout the compact
comparison interval. The global travel bound may diverge as
\(\varepsilon\to0\), and no interchange with the infinite-time limit
is justified. The deterministic conditioning correction already gives
fitting; the tangent force preserves that guarantee without proving
a benefit from random exploration.
