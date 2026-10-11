# Internal audit of the independent Gaussian readout extension

2026-10-10. This is a reused-context internal mathematical check, not an
independent promotion review. The complete new scientific input was
`GAUSSIAN_READOUT_EXTENSION.md`, SHA256

```text
3b50955432bec846b76ed728d1818d661aa61136a8455077f30c2f88cafc8d42
```

The permitted supporting input was the already completely read and audited
`GAUSSIAN_NONLINEAR_TOP_POSITIVE.md`, still at SHA256

```text
36258656917ec2ead5a86a9e163e522ec0a39a56772d806e026ae9aa1fe0718f
```

Both hashes were checked before and after the audit and remained unchanged.
No other scientific source was
read, no proof file was edited, and no numerical experiment was run.

## Verdict

**PASS for the stated extension.** I found no substantive mathematical
error or required correction. Independent centered Gaussian readout entries
with standard deviations \(0\le\sigma_n\le\sigma_*<\infty\) are covered,
including zero variance, stored variance \(1/n^2\), and bounded order-one
stored variance, while keeping the forward factor exactly \(1/n\).

The proof establishes the claimed fixed-label, probability-tending-to-one
result for actual finite-width trajectories, including finite parameter
limits and deterministic width-independent exponential decay rates. The
separate zero-label argument is valid. The extension retains a linear first
activation and a top derivative floor; it does not establish tanh/tanh
fitting or a label-uniform initialization event.

## Exact dynamics and the changed initial conditions

Equations (4) and the mobility-metric energy identity (5) agree with direct
differentiation of the stated mean-square loss. Replacing the zero readout
by a nonzero readout changes the initial loss to \(\rho(0)^2\), and (5)
correctly uses that quantity rather than \(Y^2\). The finite-time existence
argument is therefore still valid: at a hypothetical finite terminal time,
the energy bound makes the parameter arrays Cauchy; local smooth existence
at their finite limit extends the solution.

The first-layer invariant (6) is independent of the initial readout. Its
Gaussian negative-subspace event is therefore exactly the previously
verified event, and it protects
\(A(t)^\top A(t)/n\succeq(1/512)I_d\) for every evolving readout.

The trace balance also remains exact. Integrating it now gives

\[
 a^2(t)-q^2(t)
 \le a^2(0)-q^2(0)+4M_\phi S(t).
\]

Dropping \(-q^2(0)\) is an upper bound in the correct direction, so the
same output estimate (8) applies. The constant \(R_0\) includes every
required additive term, including the possible nonzero \(\phi(0)\).
No zero-readout balance identity is silently reused after changing the
initialization.

## Independent Gaussian readout bounds

Because \(w(0)\) is independent of \(A(0),W(0)\), it is independent of
\(H(0)\). Conditional on \(H(0)\), its mean is zero and covariance is
\(\sigma_n^2I_n\). Hence the exact conditional covariance of the initial
predictor is

\[
 \operatorname{Cov}(f(0)\mid H(0))
 =\frac{\sigma_n^2}{n^2}H(0)^\top H(0),
\]

and the trace is the conditional second moment displayed in the proof.

For each unit input column \(x_a\), independence of the Gaussian matrix
entries gives

\[
 \mathbb E Z_{ja}(0)^2
 =\sum_{i=1}^n\frac1n\,\mathbb E(A_i(0)x_a)^2=1.
\]

This calculation requires only second moments. The finite-width
preactivation is not assumed to be an unconditional Gaussian; conditional
Gaussianity given \(A(0)\) is sufficient wherever a Gaussian law is used.

The real-axis derivative bound implies
\(|\phi(z)|^2\le2|\phi(0)|^2+2L_\phi^2|z|^2\), so

\[
 \mathbb E\|H(0)\|_F^2
 \le2nm\bigl(|\phi(0)|^2+L_\phi^2\bigr).
\]

This reproduces (11) exactly and proves \(f(0)\to0\) in mean square,
uniformly over the allowed sequence \(\sigma_n\). The reverse triangle
inequality then gives \(\rho(0)\to Y\) in probability.

For the normalized squared readout norm,

\[
 \mathbb E q^2(0)=\sigma_n^2,\qquad
 \operatorname{Var}(q^2(0))=2\sigma_n^4/n.
\]

If \(q^2(0)>\sigma_*^2+1\), its difference from its mean is greater than
one. Chebyshev therefore bounds this failure probability by
\(2\sigma_*^4/n\), justifying the fixed \(q_*\). These formulas remain
valid when \(\sigma_n=0\); no division by \(\sigma_n\) occurs.

The initial feature Gram is unaffected by readout initialization. Its
positive population limit and convergence in probability follow by the
previous conditional covariance and fourth-moment argument. The event
(12), the first-invariant geometry event, and the needed bounds on initial
prediction may be intersected by a union bound. Their mutual independence
is neither asserted nor required.

## Nonzero labels: deterministic entry below the zero-predictor loss

For fixed \(Y>0\), the bound \(\rho(0)\le R_*=Y+1\) has probability
tending to one. The energy displacement estimate, the top activation's
Lipschitz constant, and the product decomposition give exactly (13):

\[
 \|H(t)-H(0)\|_F/\sqrt n
 \le L_\phi\sqrt m\,R_*\sqrt t\,
      (a_*+w_*+R_*\sqrt t).
\]

A deterministic positive \(t_*\) makes this at most
\(\sqrt\lambda/2\). Singular-value perturbation therefore gives
\(H(t)^\top H(t)/n\succeq\lambda I_m/4\) through \(t_*\), and hence
\(\dot\rho\le-\lambda\rho/(2m)\). The factor
\(g=\lambda/(2m)\) is correct.

Both thresholds in (14) are strictly greater than \(Y\). Their event thus
has probability tending to one even if the initial predictor makes the
initial loss larger than the zero-predictor loss. On this event,

\[
 \rho(t_*)\le Y e^{-gt_*/2}<Y,
\]

which supplies the deterministic positive loss drop required later.
This resolves the principal difference from a zero-readout start.

The bound \(q(t)\le q(0)+\rho(0)\sqrt t\), combined with
\(\rho(t)\le\rho(0)\), gives exactly
\(S(t_*)\le q_*R_*t_*+(2/3)R_*^2t_*^{3/2}\). No width-dependent
initial-norm constant remains in this estimate.

## Nonzero labels: infinite-time fit and finite parameter convergence

The protected first-layer geometry and top derivative floor give the
middle-layer kernel bound in (17), with the same normalization as the
audited zero-readout proof. Loss remaining below the zero-predictor loss
makes \(\|f(t)\|\ge\sqrt m\delta_*\) permanent. Combining this lower
bound with (8), separating \(q\le1\) and \(q>1\), proves (18).

On a positive-loss interval after \(t_*\), both \(q\) and \(\rho\) are
positive, so division by \(S'=q\rho\) is justified. The integrated
logarithmic inequality bounds \(S\), which gives the fixed positive
\(\overline q\), and then the deterministic decay rate
\(\gamma=2b\overline q^2\). Because \(\rho(t_*)\le Y\), the loss
prefactor in (3) is valid. If loss reaches zero sooner, all gradient
velocities vanish and the same conclusion holds.

The exact identity for \((q^2)'\) is unchanged. After \(t_*\),
\(\|r\|\le\|y\|\) and \(\|f\|\le2\|y\|\), so
\(|(q^2)'|\le8Y\rho\). Exponential decay bounds \(q\), the trace balance
bounds \(a\), and the matrix invariant bounds \(\|W\|_{\mathrm{op}}\).
Substitution into (4) makes the scaled velocities integrable. Thus all
finite-width parameter arrays converge to finite limits, whose predictions
are \(y\).

## Zero labels: fitting, capture, and convergence

For \(y=0\), the exact readout identity reduces to

\[
 (q^2)'=-\frac4m\|f\|^2=-4\mathcal L.
\]

At every finite width, global finite-time existence and \(q^2\ge0\)
imply \(\int_0^\infty\mathcal L\le q^2(0)/4\). A nonnegative
nonincreasing function with a finite integral has limit zero. Therefore the
claim of fitting for every finite initial state, without a geometry event,
is correct. This argument alone is not used to claim exponential decay or
finite parameter limits.

For those stronger conclusions, the separately supplied capture argument
is complete. Within mobility distance \(\eta\) of the initial state,

\[
 \|H-H(0)\|_F/\sqrt n
 \le L_\phi\sqrt m\,\eta(a_*+w_*+\eta)<\sqrt\lambda/2.
\]

Thus the output-layer tangent block already gives
\(K\succeq\lambda I_m/4\) throughout the ball, regardless of the size or
coordinates of the current readout. The full mobility speed satisfies

\[
 v^2=-\dot{\mathcal L}
 =\frac4{m^2}r^\top Kr\ge\frac\lambda m\rho^2.
\]

Whenever \(\rho>0\) inside this ball, speed is positive, and

\[
 \int_0^t v
 =\int_0^t\frac{-\dot{\mathcal L}}v
 \le2\sqrt{m/\lambda}\,[\rho(0)-\rho(t)].
\]

At zero loss the gradient is zero, so the omitted division at zero causes
no problem. The assumed initial residual bound makes total path length
at most \(\eta/2\). Distance from the initial state cannot exceed path
length, so continuity rules out a first exit from the radius-\(\eta\)
ball. The kernel gap persists and gives
\(\mathcal L(t)\le\mathcal L(0)e^{-\lambda t/m}\).
Finite total path length makes the parameters Cauchy as \(t\to\infty\).

The capture threshold is a fixed positive constant and
\(\rho(0)\to0\) by (11), so its event has probability tending to one.
The rate \(\lambda/m\) is deterministic and independent of width; the
initial loss is correctly retained as the potentially random prefactor.
If the initial loss is exactly zero, the state is stationary from the start.

## Quantifiers and remaining scope

For each fixed label vector, all controlling constants are deterministic
functions of fixed data, activation, labels, and the upper variance bound.
The finite-width events have probabilities tending to one. On each such
event, the infinite-time conclusions follow from deterministic estimates;
there is no exchange of the width and time limits.

The proof expressly avoids a simultaneous-all-labels claim for this new
initialization. That restraint is appropriate: the event used to cross
below the zero-predictor loss is chosen for the fixed label vector. The result
does not require a limit of \(\sigma_n\), only its fixed upper bound and
the stated independence and centering.

No correction to the extension is required by this audit. Its retained
activation and input-rank restrictions are stated accurately. This check
does not establish novelty or authorize promotion into maintained material.
