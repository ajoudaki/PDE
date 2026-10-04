# Coordinator reconstruction of the sample-exponent refinements

2026-10-04. Check by the root coordinator after the three scoped
derivations were written. The root and authors exchanged candidate
arguments, so this is an internal reconstruction, not an isolated
independent review or promotion gate.

## Inputs and coverage

The coordinator read every mathematical line of:

- DENSE_SAMPLE_EXPONENT_REFINEMENT.md:
  bca07e44bd5238bd17384a67714a704a2839bd43ac214db88e5c8bd7b7fe6a9d
- LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md:
  93f09aff3f97b13e0361494ce0c9c1ab89917e7dbef323216c850b6e2d96b8a4
- COMPACT_SAMPLE_EXPONENT_REFINEMENT.md:
  7e777ed6881e339f62576e763bf9b126aa0b69ed8145c1f9cacc7c2eb189c84a

The current source constants, complete dense fitting proof, complete
numerical Legendre comparison, its projection/defect interface, and
complete compact runtime fitting and source comparison sections were
read/reconstructed in this continuation. Earlier complete checks of
the same source-fitting and power-envelope files were retained.
The new argument imports their previously checked source event; it
does not reprove the Gaussian insertion theorem or improve its rate.

Relevant dependency versions:

- GENERAL_EXPLICIT_FITTING.md:
  5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6
- GENERAL_EXPLICIT_CLOSURE_FITTING.md:
  2247f0d4b189b8d38f1c996db3438a55d562ca6b0e6c82c8ae71b3110e708cbd
- EXPLICIT_LEGENDRE_COMPARISON.md:
  7834b325b31aa667d9c751a2c180439399433d82d77cdd078b38ea54e0168a1c
- SIMPLE_CONSTANTS_SOURCE_CHECK.md:
  cc1096f354e38c97b5cab8fe2000323ca21811c9801a4a33a4c5dbaf0a08938a
- SIMPLE_CONSTANTS_DENSE_CHECK.md:
  a099bc20dafe47467985667d767f274321188f96f0605bb4fff3589bc45342cb
- SIMPLE_CONSTANTS_LEGENDRE_CHECK.md:
  62c59eb811dfc6049842f028b3f90180cb52f246cbfc1c264e96389e418e8a98
- UNBOUNDED_COMPRESSOR_BRIDGE.md:
  63b0613ca4c028f780e3342fb3ddf21efc739fa9257f903691ee967276f8cc08

## Dense reconstruction

The normalized Hilbert parameter coordinates generate the original
mobilities exactly. The initial distance equals the standard Gaussian-root
distance divided by \(\sqrt n\); the full block-sum norm needs
\(\sqrt{L+1}\), not \(\sqrt L\).

The finite-difference Taylor remainder was reconstructed by subtracting
the forward recursions at their actual endpoints. Its hidden product
remainder has the negative sign
\(-\Delta W^{(\ell)}\Delta h^{(\ell-1)}\); the readout product
remainder is \(-\Delta w^\top\Delta h^{(L)}/n\).
Backward expansion pairs the activation remainder only with the
unprimed actual carrier. The second derivative bound is global on the
real line. No trained-carrier event for a parameter segment is needed.

Substituting this identity into parameter-distance energy gives the
negative square \(-2\|r-r'\|_m^2\). The remaining terms are bounded by
residual RMS times squared parameter distance. The integrated exponent
is at most
\[
\beta^{14L}s+\beta^{36L}s^2\sqrt{\log(en)},\qquad s=Ym/\gamma.
\]
Every power and numerical coefficient in the displayed ledger was
checked, including the \(L^2\) activation-curvature remainder.

Residual-gap integration is used only after this energy estimate has
closed, to recover a label-proportional readout discrepancy. Hence its
inverse gaps enter a prefactor and do not recur in a Gronwall exponent.
The same-data labels give exactly zero initial residual discrepancy.

The actual good-set pairwise Lipschitz estimate, scalar extension,
product-Gaussian concentration, time compactification and sphere net
were checked against their existing normalization. There is no
conditional Gaussian concentration or differentiation of an event.
The physical endpoint and off-net remainder have the stated control.

## Legendre reconstruction

The alternate proof of the Taylor estimate uses a parameter segment
whose matrix and readout caps follow by convexity. Its feature norms
are bounded by the explicit affine recursion, while the backward
subtraction uses only dense endpoint carriers. Thus it does not
silently assume a carrier bound on that segment.

The reconstructed closure is canonical gradient motion plus a physical
hidden-block defect in these proof coordinates. It remains the original
autonomous memory model; no independent dense layer is added.
The energy estimate uses
\(\int\rho_D\le2s\), \(\int\widehat\rho\le4s\), producing the
factor \(14s\) and a stability exponent bounded by
\(\beta^{10L}s+\beta^{36L}s^2\sqrt{\log(en)}\).

A critical interface was checked separately: the needed forcing is the
integral of the norm of the physical defect, not merely the norm of an
integrated reconstruction error. For a history projected on polynomials
on \([0,A]\), its squared tail energy has derivative equal to the
squared endpoint projection error. The interior derivative vanishes by
orthogonality. The prefixes give zero initial tail energies.
Sample and clock Cauchy--Schwarz therefore bound the absolute integrated
physical defect by twice the product of terminal tail norms. This is
exactly the defect input used in the energy estimate.

The projection constants retain \(F_h=O(s^2)\),
\(F_h/Y=O(s/\sqrt\lambda)\), and the backward terms' actual
label factors. The numerical ledgers yield the absorption and error
coefficient
\[
P_n=3Bs^2(1+m/\gamma)F_n.
\]
The common factor follows from
\((1+su)(1+Bs)\le3(1+Bsu)\), valid for \(s\le1\), \(u\ge1\).
The inverse order uses a fourth root of the logarithm: with
\(Q=\max(3,P_n,n^{1/4}\sqrt{P_n})\), the prescribed ceiling has
\(\log(eq)\le4\log(e+Q)\) and
\(q^2\ge16Q^2\sqrt{\log(e+Q)}\).
It yields \(Y/(8\sqrt n)\), stronger than the displayed benchmark.
There is no new order-dependent source event or width condition.

## Convexity and the label constraint

For both proofs the cap verifies
\(0\le\beta^{36L}s^2\le1\). The inequality
\[
e^{\theta u}\le1+\theta(e^u-1),\qquad 0\le\theta\le1,
\]
retains the actual \(\theta\), rather than replacing it by one.
The width-independent exponential is treated similarly. This proves the
polynomial envelope in the actual \(Y\) under the same stability
assumption. It does not show stability for arbitrary labels.

The improvement is not obtained merely by substituting the label cap
into the old estimate: the old exponent had an extra inverse-gap
multiplier that remains unbounded even at fixed admissible \(s\).
The new signed energy inequality is the necessary preceding step.
The raw new exponent can be retained when numerically sharper; the
convex envelope serves the explicit polynomial-data statement.

## Compact reconstruction and scope of its obstruction

The coefficient bounds
\[
a_0\le Bsh(1+s\sqrt h),\quad
b_0\le Bs^2h(1+s\sqrt h),\quad
C_{\rm out}\le B\sqrt h,\quad
C_{\rm tail}\le Bs\sqrt h,\qquad h=1+m/\gamma
\]
were checked term by term against the six contributions to the existing
Gram-difference coefficient. Substitution into the existing all-time
comparison and order inversion proves the new deterministic threshold.
The smaller polynomial threshold also dominates the tail requirement.
No source rank, approximation accuracy, or retained storage has changed.

At fixed admissible \(s>0\), the current exact positive comparison
coefficient satisfies \(b_0\ge c s^3\lambda^{-3/2}\).
The two nearly coincident identity-activation inputs exhibit an admissible
parameter family for this coefficient calculation. They do not supply
a lower bound on network discrepancy. The new upper bound has the
corresponding cubic large-inverse-gap exponent after squaring \(b_0\).

The corrected-readout projector identity is exact, but its non-diagonal
neuron metric makes the specified gate's metric adjoint different from
the gate itself. Consequently the canonical-gradient cancellation cannot
be transferred without a new coupled comparison proof.
The separate analytic-radius construction gate was also checked;
it can still be exponential in inverse gap even if the comparison were
improved. No polynomial full-width threshold is claimed.

## Assembly and outcome

SAMPLE_POLYNOMIAL_STATEMENT.md preserves the common setup and all
probability qualifications. Stirling's formula removes the factorial;
the factor \(m^4/d\) becomes \(O(m^3)\) only outside the dimension
power when \(m\asymp d\). No replacement of \(d\) inside that power
or of actual \(Y^4\) by its cap is made.

Outcome: internal PASS for the new dense and Legendre polynomial-data
envelopes and the compact threshold refinement, conditional only on the
same inherited, previously checked source/fitting components. No new
scientific assumption is added. Strict dense root width, a numerical
stochastic threshold, and polynomial compact source/comparison thresholds
remain open. This is not a promotion review. No experiment was run.

Final mechanical validation used Python to scan all three proof files,
the new statement/check, README, and the two supersession entry points
for non-newline control bytes, balanced inline/display math delimiters,
balanced display braces, and existing local Markdown links. All eight
files passed. Five preexisting carriage-return corruptions of TeX
commands in RESULT.md were repaired as typography only; no mathematical
claim in that older entry point was changed beyond the new refinement link.
The three frozen proof hashes above were unchanged by this validation.
