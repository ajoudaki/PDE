# Polynomial-width continuation: checked improvements and remaining gaps

**Later continuation, 2026-10-07:**
[TWO_GAP_CLOSURE_RESULT.md](TWO_GAP_CLOSURE_RESULT.md) closes the
finite training-source probability and gives a different source-seeded
decoder with a polynomial final-error gate. Its costs are different.
The unchanged passive estimator's error gap below is not declared solved
by that construction. The original component proofs and scoped check
record for this note remain intact.

2026-10-07. Current-study theoretical continuation; no experiment, promotion,
or change to the physical model.

**The full polynomial-width compression theorem is not yet proved.** Two
previously exponential sufficient conditions have been replaced, with
fresh bounded checks. A third checked lemma controls finite-order complex
Gaussian corrections. The trained-source probability and the fast
decoder's error comparison still have unresolved dependencies. They are
not absorbed into a constant or deleted from the current theorem.

## Shared setup

Use the original network and optimizer: hidden width \(n\), depth
\(L\ge2\), \(m\ge d\) training inputs spanning the radius-\(\sqrt d\)
sphere, independent Gaussian hidden initialization, zero readout, and
nonlinear learning in every layer. Set

\[
 Y=\|y\|_2/\sqrt m,\qquad
 \gamma=\lambda_{\min}(Q^{(L)})>0,
\]

where \(Q^{(L)}\) is the original population feature Gram matrix without
division by \(m\). Confidence is \(1-\delta\), with \(0<\delta<1/4\).
For activations analytic on the common strip of width \(a\), use the same
regularity envelope

\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,\,k=1,2}\sup_{|\Im z|<a/2}|\phi_j^{(k)}(z)|\right\}.
\]

Activation values need not be bounded. Keep the entire original
intersection of fitting and source upper label allowances; none of the
improvements below substitutes a smaller label cap. At \(Y=0\), the
physical predictor is exactly zero for all time. The decoder target is
unchanged: current-state unseen-input evaluation, the entire real sphere,
all physical training times including the endpoint, and the original
independent-dense-pair upper-certificate error scale.

## 1. Initialization and global fitting now have a polynomial width

A sufficient width for the initial operator/Gram event and subsequent
global dense fitting is

\[
 \boxed{
 n\ge\left\lceil
 \beta^{32L}\left(1+\frac m\gamma\right)^2
 \left[dL\log\beta+
       \log\frac{16L(m+1)^2}{\delta}\right]
 \right\rceil.}
 \tag{1}
\]

This gives probability at least \(1-\delta\) at each individual width.
The same initialization event works for every label vector satisfying the
original fitting allowance. On it, the actual nonlinear gradient flow
exists globally, fits the labels, converges in parameters, and has the
proved whole-sphere tail through the endpoint.

The improvement is in the proof, not the model. Gaussian concentration
pays only the logarithm of a sphere cover's size. Separately tracking
marginal standard deviations and off-diagonal covariances prevents the
old depth-squared covariance amplification, including at singular
intermediate covariances.

Complete proof: [EXPLICIT_FITTING_WIDTH.md](EXPLICIT_FITTING_WIDTH.md),
Sections 1--5. Fresh reconstruction:
[EXPLICIT_FITTING_WIDTH_CHECK.md](EXPLICIT_FITTING_WIDTH_CHECK.md).
Their scope is fitting, not the full compression source.

## 2. The large complex-time radius is unnecessary

The physical source may use complex-time half-width

\[
 \boxed{\frac{1}
 {\beta^{100L}(1+\gamma/m)\sqrt{\log(en)}}.}             \tag{2}
\]

With this choice, the formerly exponential short-contour gate holds for
every \(n\ge1\). All residual-growth, operator, and pole margins improve.
Crucially, the Taylor integrator's existing step was already smaller than
needed for (2): its patch count, degree, retained size and phase costs
are unchanged by this replacement. Real whole-sphere and endpoint
comparisons remain the same.

The late-tail and variational gates also have explicit polynomial
replacements. Their large numerical factors are absolute; their dependence
on activation regularity and depth is a fixed power of \(\beta^L\).

Complete proof: [POLYNOMIAL_SOURCE_WIDTH.md](POLYNOMIAL_SOURCE_WIDTH.md).
Fresh reconstruction:
[POLYNOMIAL_SOURCE_WIDTH_CHECK.md](POLYNOMIAL_SOURCE_WIDTH_CHECK.md).
Both retain the stopped-source and stated numerical interfaces as
conditions; neither infers a source probability from a contour inequality.

## 3. Finite confidence no longer requires waiting for complex corrections

For the moment argument, choose the integer order

\[
 p=\max\left\{1,
 \left\lceil\frac{\log(4emL/\delta)}{\log(64e^2)}
 \right\rceil\right\}.
\]

Shrinking (2) by \(p\) controls the required complex Gaussian correction
moments at every width, conditional on the stopped cavity derivative
bounds. This avoids an exponential width threshold obtained by waiting
for a complex correction to vanish at each fixed moment order. The
sample RMS estimate needs no independence between training samples.

Unlike the basic repair (2), this optional refinement has a cost: at most
\(p\) times as many Taylor patches and an additional \(O(\log p)\) in
the degree. These factors are explicit in sample count and confidence.
At fixed problem parameters they do not change the power of \(\log n\).
The final table has not been silently reused for this modified partition.

Complete conditional proof:
[FINITE_COMPLEX_MOMENT_GATE.md](FINITE_COMPLEX_MOMENT_GATE.md).
Fresh reconstruction:
[FINITE_COMPLEX_MOMENT_GATE_CHECK.md](FINITE_COMPLEX_MOMENT_GATE_CHECK.md).

The separate finite-order collision calculation gives the simple gate
\(n\ge4p^3\), conditional on the distinct-neuron moment estimate. It
avoids using a high Gaussian moment for repeated copies of one neuron.
Its proof, exact label-scaled flow, and explicit linear-response
recurrences are in
[QUANTITATIVE_INSERTION_WIDTH.md](QUANTITATIVE_INSERTION_WIDTH.md).
Those conditional reductions have their own
[bounded reconstruction](QUANTITATIVE_INSERTION_WIDTH_CHECK.md).
The local nonlinear insertion and common-cavity error bounds needed to
finish that argument are not claimed there.

## 4. The ordinary numerical gates are polynomial too

For the unchanged current cost table, write its existing logarithm as

\[
 Z=\log(en)+
 \log\left(e+\frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
\]

Its block-sampling condition is

\[
 n\ge C\delta^{-1}\beta^{512L}(m+d+2)^2
                    (1+m/\gamma)^2Z^6,               \tag{3}
\]

with an absolute \(C\). This implicit logarithmic inequality does not
conceal an exponential width dependence. An explicit sufficient envelope is

\[
 n\ge C\delta^{-2}\beta^{1024L}(m+d+2)^4(1+m/\gamma)^4
 \left[1+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right)\right]^{12}.
 \tag{4}
\]

To verify (4), put \(\ell=\log(en)\ge1\) locally. If the second
logarithm in \(Z\) is \(z\ge0\), then \(Z\le(1+z)\ell\).
Also

\[
 \frac{\ell^6}{\sqrt n}
 =e^{1/2}\ell^6e^{-\ell/2}
 \le e^{1/2}(12/e)^6.
\]

Thus squaring the prefactor in (3), multiplied by this absolute squared
constant and by \((1+z)^{12}\), suffices. No parameter is part of that
numerical constant. This is a conservative width envelope, not a proposed
practical crossover.

Confidence is not logarithmic throughout: (3) is algebraic in
\(\delta^{-1}\), and the conservative explicit version (4) is quadratic
in \(\delta^{-1}\), apart from its logarithm. A sufficient width
polynomial in \(\log(1/\delta)\) is a stronger, unresolved target. Neither
this report nor the component radius repair establishes it.

The separate conditions \(n\ge d\), \(nY\ge1\), and the stated
polynomial horizon gate retain their displayed meaning. An optional
numerical refinement pays \(\log_+(1/Y)\) in precision and removes
the *numerical* use of \(nY\ge1\); it does not by itself prove the
scientific source event uniformly for vanishing labels.

These observations concern only (3) and the other displayed numerical
conditions. They do not replace either missing scientific bound below.

## 5. Two indispensable scientific gaps remain

| Part of the full theorem | Current status |
|---|---|
| Initial Gram event and global fitting | Polynomial sufficient width proved and checked, (1) |
| Deterministic time domain and numerical gates | Exponential radius gate removed; displayed numerical gates polynomial |
| Trained-source success probability | Finite-order and local remainder bounds available; all-deletion nonlinear bootstrap, initialization/stop transfer and probability composition still missing |
| Fast decoder at the unchanged dense-error certificate | Current bias/error bound still needs an uncontrolled asymptotic absorption |

The original insertion proofs have now been read completely. They give
the nonlinear local structure but leave coefficients and eventual
absorptions unspecified. Their fixed-\(p\) limiting argument cannot be
turned into a polynomial threshold merely by writing
\(p=O(\log(mL/\delta))\). The finite-order results above resolve specific
parts of that problem, not the entire missing local estimate.

For decoding, more prior samples reduce random sampling error, but do not
remove the difference between the sampled prior and the training-conditioned
one-row distribution. Exact evaluation of the latter would still leave a
separate population-to-dense comparison. A proposed second-order scalar
argument also needs derivative and higher-moment bounds not supplied by
the current operator, Gram and entropy estimates. See
[POLYNOMIAL_ACCURACY_ONSET.md](POLYNOMIAL_ACCURACY_ONSET.md) and
[WEAK_PASSIVE_WIDTH_ROUTE.md](WEAK_PASSIVE_WIDTH_ROUTE.md).
Their abstract counterexamples concern proof interfaces, not reachable
neural trajectories or an impossibility theorem for compact decoding.

Accordingly [GAP_REFINED_PHASE_COSTS.md](GAP_REFINED_PHASE_COSTS.md)
remains a conditional phase-cost theorem with the improved component
thresholds above, not an unconditional polynomial-width theorem. Actual
activation evaluation, input/label descriptions, gap/strip certificate
acquisition, and output writing remain charged interfaces. Analytic
regularity alone supplies no bit-complexity bound for an arbitrary
activation evaluator.

The checked improvements preserve the original scientific scope. The
research and rigorous-proof workflow was used to keep the conditional
components distinct from the unresolved full claim. No full-resolution
claim, smaller storage exponent, or faster query theorem is made here.

## 6. Further local improvement: the cutoff power no longer grows with depth

The local nonlinear calculation has also been completed and independently
checked in [FIXED_ORDER_INSERTION_JETS.md](FIXED_ORDER_INSERTION_JETS.md)
and [its reconstruction](FIXED_ORDER_INSERTION_JETS_CHECK.md).
For a local carrier-coordinate bound \(M\) and at most \(p\) deleted
neurons, its retained-vector-field remainder uses coefficient
\(\beta^{120L}(1+p)(1+M)\). Learned-source corrections and the complete
top-layer residual offset need at most \((1+M)^3\). The conditional
complex version uses \(\beta^{240L}\) and its displayed strip margin.

Thus the old depth-dependent power of a logarithmic coordinate cutoff is
not necessary for this local remainder. The proof propagates remainders
through bounded perturbed weights and slopes, keeping reference-carrier
factors in additive terms. It preserves the reverse deletion force and
the changing residual, rather than replacing them by a simpler dynamics.

The author corollary
[SCALED_INSERTION_REMAINDER.md](SCALED_INSERTION_REMAINDER.md) transfers
that estimate to label-normalized coordinates with no inverse activity
factor. This follows from an explicit blockwise contraction: hidden
parameter increments acquire factors at most one, the forward ports are
unscaled, and zero initial readout permits the normalized readout.
It is conditional on the localized normalized variations, not a probability
bound uniform in small labels.

Finally [INSERTION_MAP_MODULI.md](INSERTION_MAP_MODULI.md) gives
author-derived control and time interpolation recurrences for the Gaussian
linear and quadratic maps. Their logarithmic powers are at most two and
four respectively; their coefficients are explicit recurrences and have
no inverse label-amplitude factor. The main horizon's \(m/\gamma\)
factor cancels the reciprocal factor in the control-speed estimate.
This note has not had a separate independent reconstruction.

These are additional inputs toward a quantitative source theorem. The
complete stopped-event composition, cavity initialization and transfer,
and common-cavity probability estimate remain to be assembled and checked.
They do not remove the separate decoder bias identified in Section 5.
The earlier assembly check verifies equations (1)--(4) and their scope;
the local remainder's independent check has the separate scope just stated.
