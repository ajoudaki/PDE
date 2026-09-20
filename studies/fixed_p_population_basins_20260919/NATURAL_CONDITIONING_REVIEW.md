# Internal isolated review of the continuous conditioning flow

2026-09-19. **PASS for the stated corrected optimizer and its explicitly
restricted comparison with ordinary gradient flow.** No unresolved blocking
mathematical error was found. This is an internal check, not a promotion
review or approval to add the result to established theory.

The theorem proves pathwise exponential decay of the actual loss and of
the declared potential, finite total physical-state travel, and convergence
to a finite fitted state. Global existence and uniqueness refer to the
piecewise smooth flow in the positive-Gram domain together with the stated
absorbing continuation at a singular fitted endpoint. They do not assert a
globally regular vector field across the singular set.

## 1. Frozen scope and provenance

The final candidate was read completely. Its hash is
0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0.
The originally assigned hash was
ffe5305edcb38393e54dffe3db71a186e8fa1451826ad4981c8fd13f22407ffa.
The sole intervening revision explicitly restricts admissible mobilities
to piecewise constant paths with finitely many changes on each bounded
time interval. That revision resolves the review's minor clarification
about time regularity; the complete revised candidate was reread.

All three assigned study dependencies were read completely. The canonical
source was read only in its assigned complete ranges 13161–13786 and
15146–15528. INITIAL_REVIEW.md was expressly authorized as a scientific
dependency because its Section 6 supplies the order-one extension; its
prior verdict was not treated as evidence replacing verification. No study
README, other study, other route, task history, unassigned review, or
experiment was consulted. No candidate or dependency was edited.
The required solve-math-rigorously skill and the supplied
investigate-conjectures/references/adversarial-audit.md instructions were
read and applied. No numerical experiment was run.

Exact SHA256 fingerprints:

| Input | SHA256 |
|---|---|
| NATURAL_CONDITIONING_FLOW.md | 0cb163ae98d35a741fbcaee0cacd48ce6381f8746d0ed2f164f54d5eba82e3c0 |
| ESCAPE_AND_LIMITS.md | 544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2 |
| INITIAL_EXCLUSION.md | 34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c |
| INITIAL_REVIEW.md | 6fd58a9faa1b07a0eaa53fe9595b63180b225e72df35a7f50fe9f6e629d64baf |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md (whole-file fingerprint) | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/global_nonlinear.md:13161–13786 (exact bytes including line endings) | 0a00ff65642c57068bc3cbf8dcda5a3024edd8e12213a521168fb4db9b303bb1 |
| docs/global_nonlinear.md:15146–15528 (exact bytes including line endings) | 3815d81705fac51fcd5b5489b6f6f961021cba525acf88e74bdc82fe818ae386 |

## 2. Model, nonvacuity, and initialized positive Gram

The dynamics use the population \(L^2\oplus L^2\oplus\) Frobenius
metric, the unhalved probability-weighted loss, the complete fixed joint
mark laws, and the actual transpose. The factors of two in the gradients
and four in the decay estimates agree with the canonical equations.

For every state, bias-free odd activations give

\[
a(-u)=-a(u),\qquad H(-u)=-H(u),\qquad f(-u)=-f(u).
\]

Thus merging an input class modulo antipodes, adding its masses, and
transforming each label by the same sign preserves the loss and its
gradient exactly. Compatibility makes the representative label unique.
This reduction is necessary: retaining duplicate or antipodal rows would
make the unmerged Gram singular for a purely representational reason.

The supplied initialization argument establishes more than one nonzero
initial residual direction. Its functions \(H_0(v_i)\) are linearly
independent for every finite list of directions distinct modulo antipodes.
Consequently, for every nonzero \(z\in\mathbb R^m\),

\[
z^TK_0z=\left\|\sum_i z_i\sqrt{\mu_i}H_0(v_i)\right\|_2^2>0.
\]

I checked the relevant initialization chain against the canonical source:
the order-one and order-two active odd lists are the same, parity removes
the other initialized contraction blocks, and the raw-filter identity
uses both full ridged inverses. The contraction row is

\[
(\alpha v,\alpha\kappa+\tau\beta),
\]

including the reverse-source response \(\tau\beta\). The lower covariance
between \(h\) and \(t\) is retained. In the monotonicity calculation,

\[
b_*\ge\frac{529}{1024}b^*,\qquad
2b_*-b^*\ge\frac{17}{512}b^*>0,
\]

and the numerator of \(\ell+\alpha r b(h)\) is bounded below by
\(\alpha v\tau\beta(2b_*-b^*)>0\). All ridge terms discarded in that
lower bound are nonnegative for every positive ridge. Hence the proof
applies separately to the prescribed
\(\eta_1=1/4096\) and \(\eta_2=1/9216\).

The resulting strictly increasing odd scalar response makes the vector
response injective and identifies opposite vectors precisely with
antipodal inputs. The ridge-function independence proof remains valid
for parallel vectors of different magnitudes: choose distinct nonzero
absolute projections, extend the analytic identity along the real line,
and successively isolate its slowest exponential at infinity. The upper
Gaussian transform has positive density on the open square. This proves
the required \(K_0>0\) without a genericity assumption or a bound on the
number of distinct data points. The finite-dimensional mark coordinate
does not bound the dimension of the span of its nonlinear ridge functions.
The canonical Gaussian first field has finite \(L^2\) norm and all
initialized matrices are finite, so the starting Hilbert state is valid.

## 3. Exact descent and the safeguard

Write \(h=1+\varepsilon R\), \(g=\nabla L\), \(v=\nabla R\),
\(a=1-\nu>0\), and \(b=1+\nu\) in this report.
Since \(A^*e=\sum_i\sqrt{\mu_i}e_iH_i\),

\[
\nabla_cL=2A^*e,\qquad
\|\nabla_cL\|_2^2=4e^TKe\ge4kL.
\]

The minimum-norm fitting correction is indeed \(-A^*K^{-1}e\), of
squared norm \(e^TK^{-1}e\le LR\); this interpretation does not supply
an unknown future object to the algorithm. The inverse differential is

\[
dR=-\operatorname{tr}(K^{-1}(dK)K^{-1})
   =-\operatorname{tr}(K^{-2}dK).
\]

It depends only on the current hidden features. Its readout derivative
is zero, so \(Pv=v\) and the hidden/readout split used by the safeguard
is exact. In particular, with \(q=\langle g,v\rangle\),

\[
\beta\|\nabla_cL\|^2=\varepsilon L[-q]_+,
\]
\[
\dot L=-h\langle g,Pg\rangle-\varepsilon Lq
        -\varepsilon L[-q]_+
       =-h\langle g,Pg\rangle-\varepsilon L[q]_+.
\]

This checks both possible signs of the hidden conditioning contribution.
No stochastic cross term is omitted because the mobility acts as the
identity on the hidden blocks. Since \(R\ge1/k\), \(kh\ge\varepsilon\),
and therefore

\[
\dot L\le-4akhL\le-4a\varepsilon L.
\]

For the potential,

\[
\|\nabla\Phi\|^2\ge h^2\|\nabla_cL\|^2
 \ge4kh^2L=4kh\Phi\ge4\varepsilon\Phi,
\]
\[
-\dot\Phi=\langle\nabla\Phi,P\nabla\Phi\rangle
             +\beta h\|\nabla_cL\|^2
 \ge a\|\nabla\Phi\|^2\ge4a\varepsilon\Phi.
\]

The correction that preserves actual-loss descent also dissipates the
potential. These are pathwise inequalities; independence, centering, or
any special sign distribution is unnecessary. In the concrete construction,
the mobility eigenvalues are \(1\pm\nu\) on the chosen orthonormal
directions and one on their orthogonal complement, so its asserted
operator bounds hold exactly even when the features later move.

## 4. Hilbert regularity, including zero residual

The loss regularity in the authorized dependency applies on the full
physical Hilbert space. Specifically, for \(u_i=x_i/\sqrt2\),

\[
Da_i(w)[\delta w]
 =E_1[b_1\phi'(w\cdot u_i)(\delta w\cdot u_i)].
\]

Bounded \(b_1,\phi''\) bound its Taylor remainder by
\(C\|\delta w\|_2^2\) and give

\[
\|Da_i(w)-Da_i(\widetilde w)\|_{\rm op}
 \le C\|w-\widetilde w\|_2.
\]

The map \(M a_i\mapsto\phi(b_2^TM a_i)\) is a smooth map from a finite
Euclidean space into \(L^\infty\), since \(b_2\) is bounded. Its products
and expectations give \(C^{1,1}\) Gram entries on bounded state sets.
Finite-matrix inversion on \(K\ge k_0I\) then gives the stated bounded,
locally Lipschitz gradients of \(R\) and \(\Phi\). Pairing \(H_i\) with
\(c\in L^2\) retains the same local regularity for the residual map.
This argument does not require a twice Fréchet differentiable
\(L^2\)-to-\(L^2\) Nemytskii operator.

For the zero-residual issue, write \(J=De(S):\mathcal H\to\mathbb R^m\)
and \(B(S)=J\nabla R(S)\). Both \(J\) and \(B\) are locally Lipschitz
where the state is bounded and \(K\ge k_0I\). Holding these coefficients
fixed and writing \(e=r u\), \(r>0\), \(|u|=1\), gives exactly

\[
\beta=\frac{\varepsilon}{2}
 r\frac{[-u\cdot B]_+}{u^TKu}.
\]

The angular factor is bounded and Lipschitz on the unit sphere, uniformly
over the indicated neighborhood. Its degree-one radial extension is
Lipschitz: if \(r\ge s>0\), then

\[
|r-s|\le|ru-sv|,\qquad s|u-v|\le2|ru-sv|.
\]

These estimates control radial and angular changes; the case \(s=0\)
uses the bounded angular factor. Changing \(B,K\) contributes a locally
bounded residual factor times their Lipschitz differences. Composing with
the locally Lipschitz residual map proves the asserted extension
\(\beta(S)=0\) at zero loss. The vector correction
\(\beta\nabla_cL\) is locally Lipschitz as well. At a zero-loss state in
the domain, the entire vector field vanishes.

For each fixed mobility, the local integral equation on a small Hilbert
ball is a contraction when its time length times the local Lipschitz
constant is below one; boundedness of the vector field keeps that integral
map in the ball. This supplies the local existence and uniqueness used
in the candidate. The final explicit local finiteness of switching times
permits concatenation without an accumulation of switches at finite time.

## 5. Finite travel and the singular boundary

Let \(D_t=-\dot\Phi\) while the state lies in the domain at positive
loss. The two dissipation terms separately give

\[
D_t\ge a\|\nabla\Phi\|^2,\qquad
D_t\ge\beta h\|\nabla_cL\|^2.
\]

Using both lower bounds

\[
\|\nabla\Phi\|\ge2\sqrt{\varepsilon\Phi},\qquad
h\|\nabla_cL\|\ge2\sqrt{\varepsilon\Phi}
\]

proves precisely

\[
\|P\nabla\Phi\|\le\frac ba
\frac{D_t}{2\sqrt{\varepsilon\Phi}},\qquad
\beta\|\nabla_cL\|\le
\frac{D_t}{2\sqrt{\varepsilon\Phi}}.
\]

The summation is an upper bound and need not assign the same dissipation
exclusively to one velocity term. Integrating
\(-\dot\Phi/(2\sqrt\Phi)=-d\sqrt\Phi/dt\) gives the candidate's
finite-travel constant \((b/a+1)/\sqrt\varepsilon\), including its
subinterval version. Switches preserve the state and hence the potential
inside the domain, so these integrated bounds also cross switches.

At a finite maximal time, monotonicity gives a limit of \(\Phi\), and
the subinterval travel bound makes the state Cauchy. Completeness of the
Hilbert space supplies a strong state limit. This is stronger than a
bounded-norm assertion and makes no false compactness inference. State
continuity implies continuity of the finite Gram and actual loss. A
positive limiting Gram permits local continuation. If it is singular,
\(R\to\infty\), and

\[
L\le\frac{\Phi(S_0)}{1+\varepsilon R}\longrightarrow0.
\]

Thus the only possible finite domain exit is at a fitted state. The
absorbing extension is continuous in state and loss. The finite integral
of state speed also makes that extension absolutely continuous across
the exit time. It is unique under the stipulated absorption rule; it
does not claim unrestricted ODE uniqueness on the singular set, where
the positive-Gram formula is undefined.

The potential itself may have a nonzero left limit there. Defining it
to be zero at and after absorption causes only a downward jump, so it
preserves both monotonicity and the claimed exponential upper bound.
No assertion of continuous extension of the formula for \(\Phi\) is
needed or made. On an infinite trajectory within the domain, the same
travel estimate and exponential decay make the tail length tend to zero.
The strong endpoint therefore exists and has zero loss by continuity.
An initially fitted state is the immediate constant-solution case.

## 6. Physical time and the exact small-correction scope

The rates

\[
L(t)\le L(0)e^{-4(1-\nu)\varepsilon t},\qquad
\Phi(t)\le\Phi(0)e^{-4(1-\nu)\varepsilon t}
\]

hold in the continuously running clock of the new differential equation.
There is no proposal counter or accepted-time clock. The coefficient
\(1+\varepsilon R\) accelerates part of the vector field when the Gram
is poorly conditioned, and the conditioning force can be large. Thus
the geometry-free displayed exponent does not establish a geometry-free
computational cost or a globally weak change to ordinary physical GF.
The candidate explicitly acknowledges this.

For a fixed ordinary-GF horizon with \(K(S^0(t))>0\), the image of the
continuous reference path is compact. Its smallest eigenvalue therefore
has a strictly positive minimum. Continuity of the Gram, or its uniform
Lipschitz bound on a containing state ball, gives a fixed tubular
neighborhood with \(K\ge k_0I\). The coefficients and ordinary-GF
Lipschitz constant are bounded there. Cancellation of \(L\) against the
denominator bound gives

\[
\beta\le\frac{\varepsilon\|\nabla L\|\|\nabla R\|}{4k_0},
\]

also with value zero at a fitted state. Hence the complete vector-field
difference is uniformly \(O(\varepsilon+\nu)\) in that neighborhood,
independently of the mobility realization or its switching schedule.
The integral difference inequality and scalar integrating factor give
\(O_T(\varepsilon+\nu)\) state error before first exit. Choosing this
error smaller than the neighborhood radius excludes first exit and also
excludes a corrected-flow singular absorption on that interval.

The hypothesis concerns the ordinary reference path and is essential.
Nothing in this proof establishes positivity of its Gram at all finite
times, uniform approximation after a reference singularity, or any
interchange of the small-correction and infinite-time limits. Taking
only \(\varepsilon\to0\) at fixed nonzero \(\nu\) does not recover
ordinary GF; the candidate correctly takes both parameters to zero.

## 7. Adversarial checks and final claim boundary

| Target under attack | Strongest obstruction | Decisive check and outcome |
|---|---|---|
| Universal stated initialization | Symmetry, repeated data, or finite mark dimension forces rank deficiency | Exact antipodal aggregation and the initialized ridge-function independence prove \(K_0>0\). |
| Actual-loss descent | Hidden conditioning descent can increase the training loss | The exact positive-part cancellation leaves \(-\varepsilon L[q]_+\le0\). |
| Hilbert local uniqueness | Division by the residual quadratic form causes a singular correction at zero loss | Degree-one radial/angular representation gives a locally Lipschitz extension. |
| Global endpoint | Infinite-dimensional bounded paths need not have strong limits | The full speed, including the safeguard, is controlled by the decrease of \(\sqrt\Phi\), giving Cauchy tails. |
| Avoiding bad finite termination | The flow could hit singular Gram with positive loss | Bounded \(\Phi\) and diverging \(R\) force \(L\to0\) before absorption. |
| Stochastic robustness | Mobility cross terms spoil the safeguard or dissipation | The hidden identity blocks and coercive readout mobility give the exact pathwise estimates. |
| Weak perturbation interpretation | A singular barrier or a changed speed invalidates global near-GF claims | The proof is uniform only on a reference tube with a positive Gram gap; the candidate states precisely that restriction. |
| No hidden oracle | The correction requires a fitted endpoint or future trajectory | It uses current finite Gram integrals, their derivatives, the residual, and fixed initial mobility directions only. |

The sole clarification raised during this review was the need to specify
time regularity of the mobility: the spectral inequality alone cannot
define dynamics for arbitrary nonmeasurable operator families. The final
candidate's explicit piecewise-constant, locally finite switching
assumption fully closes that issue.

No claim is thereby obtained for additive Brownian perturbations,
minibatch noise, plain canonical GF at long times, finite-width networks,
numerical discretizations, efficient implementations, or a larger closure
order. The deterministic conditioning correction already suffices for the
proved theorem; optional bounded readout randomness is tolerated by that
mechanism. Subject to these stated boundaries, the final candidate is
mathematically sound.
