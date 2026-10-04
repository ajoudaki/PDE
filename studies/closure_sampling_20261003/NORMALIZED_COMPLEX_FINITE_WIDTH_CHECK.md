# Check of the finite-width complex-moment obstruction

2026-10-04. Checker: scoped agent `nearcritical_geometry`.

Verdict: **PASS for the stated finite-width initialization theorem.**
The complete argument proves that for every finite width `n>=1`, every
`d>=2`, and every nonzero real imaginary angle `tau`, the second hidden
feature of the stated real-Gaussian two-layer network has infinite
unconditional complex second moment for

\[
\phi(z)=az+c\operatorname{erf}(z/\sqrt2)+b,
\qquad a,b\in\mathbb R,\quad c\in\mathbb R\setminus\{0\}.
\]

No mathematical correction is required. This check supplies no all-time
training theorem and no compression or high-probability lower bound.

## Input, provenance and actual check

I read every line of the frozen input
`NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md`, SHA-256
`36019c9384307fd7a933419cba3ebf937f652f7635947ff3b50c9e24ece91e57`.
The hash was checked before and after mathematical reconstruction and was
unchanged. No source, experiment, other study, or code was retrieved for
this check. The required canonical-notation, neural-network, rigorous-proof,
research-process, and adversarial-audit instructions were applied.

This is a nonauthor internal mathematical check, not a fresh isolated
promotion review. The checker had just authored
`NEARCRITICAL_GEOMETRY_ROUTE.md` and previously read the four explicitly
assigned population-geometry/activation notes for that separate scoped
derivation. The supervisor's assignment identified the proposed rare-event
mechanism. None of that prior population material is needed for the
finite-width proof checked here. The scalar estimates and conditional
integration below were reconstructed directly from the frozen audit.

Actual tools used for this check were a complete `cat` read of the audit,
`sha256sum` identity checks, and reading the required audit instructions.
No numerical test can establish the asserted infinite expectation, and
none was used. Only this check report was written during the check.

## 1. Uniform imaginary-sector lower bound

The identity

\[
\operatorname{erf}(z/\sqrt2)
=\sqrt{2/\pi}\,z\int_0^1 e^{u s^2}\,ds,
\qquad u=-z^2/2
\]

is the entire defining integral along the straight segment. For
`R=Re u>0`, differentiate the proposed integration-by-parts primitive:

\[
\frac d{ds}\frac{e^{us^2}}{2us}
=e^{us^2}-\frac{e^{us^2}}{2us^2}.
\]

It gives exactly the sign and both endpoint terms in the audit's
equation (6). On `[1/2,1]`, `1/s^2<=4` and
`s^2<=1-(1-s)`. Therefore the remainder is at most

\[
\frac2{|u|}\int_{1/2}^1 e^{Rs^2}\,ds
\le\frac{2e^R}{|u|R}.
\]

The interval `[0,1/2]` contributes at most `e^(R/4)/2`, and the
lower boundary term contributes at most `e^(R/4)/|u|`. Dividing their
sum and the remainder by the leading magnitude `e^R/(2|u|)` gives
exactly

\[
|u|e^{-3R/4}+2e^{-3R/4}+4/R.
\]

When `R>=kappa|u|` with fixed `kappa>0`, this tends to zero uniformly.
Thus the integral has magnitude at least `e^R/(4|u|)` eventually.
Since `|u|=|z|^2/2`, its multiplication by `sqrt(2/pi)|z|` yields
the audit's lower-bound constant `(1/2)sqrt(2/pi)` exactly.
There is no unproved sector asymptotic or cancellation assumption.

In the same cone, the bound grows at least as a positive constant times
`exp(kappa|z|^2/2)/|z|`. This dominates `|a||z|+|b|`, so nonzero
`c` cannot be cancelled by the affine term for all sufficiently large
`|z|`. This validates the subsequent factor-of-two allowance, including
negative `a`, negative `c`, and zero `b`.

## 2. Positive probability of the required first-row event

For `tau!=0`, the real and imaginary parts of

\[
Z=A_{11}\cosh\tau+iA_{12}\sinh\tau
\]

are independent real Gaussians with strictly positive variances.
Consequently every nonempty open subset of the complex plane has positive
probability. At `z=iR`, the real part of `phi(z)` equals `b`, while
its imaginary part is

\[
aR+c\sqrt{2/\pi}\int_0^R e^{s^2/2}\,ds.
\]

The integral dominates `R`, so its magnitude tends to infinity for
`c!=0` irrespective of `a`. For each finite `n`, one can choose `R`
so both strict inequalities
`|Q|>2|P|` and `Q^2-P^2>n/2+1` hold for `phi(iR)=P+iQ`.
Continuity preserves them on an open neighborhood. This establishes a
strictly positive probability event, with no uniform-in-`n` probability
lower bound being inferred.

The event uses a genuinely open neighborhood, not the probability-zero
condition `Re Z=0`. The proof also works for negative `tau`: its sign
does not alter the full-support assertion.

## 3. Conditional Gaussian divergence and the exact threshold

Condition on the entire first-layer matrix and all second-layer first-row
weights except `T=W_11`. The other weighted coordinates form a finite
fixed complex number `C`; independence leaves `T~N(0,1/n)`.
For `H=P+iQ` on the event above, put `z(t)=tH+C`. Direct expansion gives

\[
-\operatorname{Re} z(t)^2
=(Q^2-P^2)t^2-2\operatorname{Re}(HC)t-\operatorname{Re}(C^2).
\]

The quadratic coefficient is positive. Also

\[
\frac{-\operatorname{Re}(H^2)}{|H|^2}
=\frac{Q^2-P^2}{Q^2+P^2}>\frac35.
\]

Hence `-z(t)^2/2` eventually belongs to the fixed cone with
`kappa=1/2`. The threshold may depend on `H,C`, which is permitted
because the divergence is proved after conditioning. The sector bound,
the affine-term domination, and `|z(t)|<=C_*t` for large `t` give

\[
|\phi(tH+C)|^2\ge C_1t^{-2}
\exp\{(Q^2-P^2)t^2-C_2t-C_3\}.
\]

The Gaussian density of `T` contains exactly `exp(-nt^2/2)`, so
the remaining quadratic coefficient is `Q^2-P^2-n/2`. The event makes
this coefficient greater than one. Its positive quadratic term dominates
the negative linear term and `t^(-2)`, proving the one-dimensional
integral is infinite. The audit's threshold `n/2` is correct for weight
variance `1/n`; it would have been different for a differently scaled
weight, but no normalization is changed here.

This proof is valid for every finite value of the other conditioned
weights. When `n=1`, the omitted-coordinate sum is zero and the same
argument applies. Nonnegative integrands permit Tonelli's iterated
integration even with infinite values. Integrating the conditional
infinite value on the positive-probability first-layer event proves
the infinite second moment of one second-layer coordinate. Averaging
nonnegative coordinate squares preserves infinity.

## 4. Real-axis and population comparisons

On the real axis, the activation satisfies
`|phi(x)|<=|a||x|+|c|+|b|`. Conditional Gaussian moments therefore
give finite moments of every fixed order for each coordinate at every
fixed finite depth and width. For example a linear-layer coordinate
has conditional `p`th absolute moment
`C_p(n^(-1)||h||^2)^(p/2)`; finite-dimensional norm inequalities and
induction preserve its finiteness. Thus the complex result does not
conceal a real finite-moment defect.

The normalized bounded erf constants in the audit are consistent:
`E erf(Z/sqrt(2))^2=1/3` and
`E[(d/dz)erf(Z/sqrt(2))|_(z=Z)]^2=2/(pi sqrt(3))` give both unit
moments directly after the displayed rescaling and offset. The former
identity follows from `erf(Z/sqrt(2))=2Phi(Z)-1`, which is uniform
on `(-1,1)`; the latter is a single Gaussian integral.

For the complex population comparison one does not need to assume a
finite-width Gaussian law. At a population complex Gaussian with
`E U^2=1` and `E|U|^2=r<2`, the elementary vertical-segment estimate

\[
|\operatorname{erf}((X+iY)/\sqrt2)|
\le1+\sqrt{2/\pi}|Y|e^{-X^2/2+Y^2/2}
\]

makes its square integrable since `Var(Y)=(r-1)/2<1/2`.
Gaussian variance differentiation gives the derivative moment
`sqrt(3)/sqrt(4-r^2)` for the normalized activation and its integral
is the stated `F(r)`, with `F(1)=1`. Continuity then gives
`r_0=cosh(2tau)<2` and `r_1=F(r_0)<2` for all sufficiently small
nonzero `tau`. This verifies the claimed finite population two-layer
moment comparison without identifying it with a finite-network
unconditional expectation.

An empirical quantity can converge in probability to a finite constant
while having infinite expectation at every finite width. The proof
exhibits exactly the missing integrability control. It makes no claim
that its positive-probability event stays probable as width grows.

## 5. Consequence and limits of the verdict

The audit correctly refutes the proposed inference from a finite
population complex second moment to an unconditional finite-network
complex second-moment bound, for the stated activation class and queries.
The quantifiers include arbitrary fixed nonzero imaginary angle and every
finite width; no width limit is taken inside the divergence proof.

No step rules out a stopped estimate, convergence in probability, a
high-probability source bound, a polynomial-depth construction, or an
autonomous compressed runtime. The statements in the audit explicitly
retain those distinctions. Its references to existing stopped proofs
are contextual; this report does not independently audit those external
source theorems or any all-time claim. The canonical zero readout gives
zero initial prediction despite the feature-moment divergence, so the
audit also correctly avoids a prediction-error lower bound.

There are no unresolved mathematical objections to the frozen local
theorem. Its check status is independent of the unresolved trained-flow
and compression targets, and it is not promoted material.
