# Scoped implementation: fitting, Legendre, and actual dense variability

Owned files: paper/compact_fitting.tex and paper/compact_legendre.tex.
The maintained manuscript and other authors' compact modules were not edited.

The source mathematics was taken only from the current active paper. The
canonical-notation and rigorous-mathematics skills were applied. This is a
theorem-focused rewrite, not a new claim of independent peer review.

## Implemented interfaces

- cp:fit: initialized Gaussian operator/feature/Gram event, covariance LLN
  allowing singular intermediate covariance, dense all-time fitting and
  parameter/output tails. The initialization argument covers simultaneous
  rectangular cavities deleting a fixed bounded number of coordinates per
  layer while retaining the original variance and normalization n.
- cp:signed: the residual-weighted parameter-energy calculation, with
  an explicit norm-regularization justification at zero discrepancy.
- cp:legendre: complete moment state, initial prefix, autonomous equations,
  physical-time reconstruction defect, global fitting, projection identities,
  signed comparison, coefficient ledger, and chosen-order error/storage result.
- cp:dense-lower: innovation variance, conditional scalar last-layer
  anti-concentration, deterministic analytic derivative transfer, and the
  confidence conversion with the original lower coefficient.

## Source-module contracts used

- cp:carrier: with probability tending to one, the maximum over training
  samples, layers, coordinates and all real times is at most
  32 K_src (Y/lambda) sqrt(log(en)), with K_src <= beta^(21L).
- cp:finite-time: for every fixed finite real query list, holomorphy on the
  rectangle with time horizon 32 log(en)/lambda and radius
  1/(lambda sqrt(log(en))), with each prediction bounded by
  16 beta^(6L)Y/lambda.

These are forward dependencies on the compact source module, not imports
from the old appendix. Their proofs remain the source-module owner's scope.

## Preserved rates and changes of proof route

The comparison ledger retains
14(K0+K1 M)z <= X^10 z + X^36 z^2 sqrt(log(en)),
where X=beta^L and z=Y/lambda <= X^-30. Thus the amplification is at
most e X exp(sqrt(log(en))). There is no additional structural factor
in that exponential; the prescribed order retains exactly
exp(sqrt(log(en))/2).

Only the large-order approximation estimate is claimed. The independent
physical fitting lemma holds at every finite order because it is used to
control the nonlinear clock and histories. The prescribed headline order
eventually exceeds the absorption threshold q_abs=n^{o(1)}. The stronger
all-order factorized numerical approximation certificate is not restated.
The displayed cubic sample/gap storage power is retained without using the
label cap to lower it.

The recursive matrix Gram CLT was replaced by a conditional scalar argument.
After conditioning on both preceding-layer initializations, the centered
last-layer velocity difference converges conditionally to a Gaussian.
Uniform CDF convergence bounds interval probabilities uniformly in the
arbitrary conditional mean shift. This gives the same confidence margin and
lower variance coefficient. No claim of a full matrix CLT is made.

## Checks and remaining integration work

A standalone pdflatex halt-on-error harness compiled the two modules
successfully (11 pages after small line-break repairs). Its output is in
/tmp/compact_paper_20261009_legendre_2jmlyK/. The harness deliberately
omitted the source module, so its two external labels were unresolved.
The coefficient block's initial line-separator typo was repaired before
the successful compile. Minor overfull lines were reflowed, and the second
compile had no overfull boxes. A later interface pass also defined the
whole-sphere star norm explicitly and repaired a missing equation-space
backslash; the whole-document build will resolve cp:norm as well.

No unclosed local mathematical obligation was identified in the scoped
implementation. Full-document integration must still verify the two source
contracts above, resolve cross-references, and rerun the document build.
This scoped verification is not a fresh independent audit of the source
foundation or the selected-model proofs.
