# Independent accuracy review of the Borel–Padé PDF appendices

Date: 2026-09-06.

Reviewer: independent destination subagent `borel_pdf_accuracy`.

## Scope and materials

Read the full source notes:

- `BOREL_HYPOTHESIS_AND_LOCAL_IMPLICATIONS.md`;
- `PADE_BOREL_UNIFORM_APPROXIMATION.md`;
- `PADE_STIELTJES_GUARANTEE.md`.

Read the written appendices in full:

- `gf_exposition/borel_population.tex`;
- `gf_exposition/pade_stieltjes.tex`.

Also checked the original August project document's scalar all-time bound
and named conjecture directly. This is an independent mathematical audit
of the written exposition and its conditional conclusions, not a new proof
of neural Borel reconstructibility or a fresh literature-priority survey.

## Verdict

Final mathematical verdict: **PASS**. The two appendices faithfully cover
the discussions, with no substantive mathematical gap found in the reviewed
claims. The one requested hypothesis clarification has been applied and
independently rechecked: `C > 0, b >= 0` is now explicit in both the
Borel-growth envelope and the conformal exponential-bound example.
The final text also explicitly distinguishes the scalar function kappa from
the layer learning multipliers kappa_ell. No required fix remains.
This file is not a visual typesetting review.

## Claims checked

1. **Population object and scalar clock.** The one-input kernel equation has
   the correct physical factor 2; tau=2t, so d_p=2^(-p) f^(p)(0). The
   output-dependent kernel exists locally on the initialized orbit under
   nonzero residual and K(0)>0. The exposition does not claim arbitrary
   hidden states are determined by their outputs. The stationary zero
   residual case is separated.

2. **Jet coefficients.** The c_0, c_1 and c_2 formulas were checked by
   differentiating f_tau=(y-f) kappa(f). Their denominators are legitimate
   under the stated positivity. Degree-q kernel truncation matches the
   first q+1 prediction derivatives formally. This is not promoted to
   positive-time convergence.

3. **Borel meaning and identification.** Gevrey germ convergence,
   continuation, growth, actual-observable identification and convergence
   of a declared rational/quadrature construction remain distinct. The
   Gamma-integral calculation showing that exact integration of a Borel
   polynomial returns the raw Taylor polynomial is correct. The smooth
   flat-function ODE is globally Lipschitz, has a unique solution, and its
   jet's sum t fails the ODE; it is correctly described as a logical
   obstruction rather than a neural counterexample.

4. **Scalar local error.** The separated-clock proof is valid for merely
   continuous positive kernels. Its factor 1±epsilon/min(kappa), its time
   margin, and prediction/loss bounds are correct. The all-time logarithmic
   loss bound follows by maximizing t times the loss derivative. Its full
   output-to-target positivity assumption is clearly additional.

5. **Several inputs.** The weighted kernel operator error controls the
   approximate residual energy, the prediction error and the stated loss
   error. No commutation or strictly positive smallest eigenvalue is used.
   A nonsymmetric approximation is covered because the symmetric part has
   lower bound -epsilon_N I. The PSD improvement and the normalized-weight
   entrywise-to-operator bound are correct. The matrix reconstruction is
   explicitly an additional conjecture.

6. **Population-to-network implication.** The triangle inequality has the
   proper order of quantifiers: a finite reconstruction is chosen for
   accuracy first, then width tends to infinity with eta_n tending to zero.
   Covering every t<T_* requires reconstruction on every smaller compact
   interval; a shrinking interval gives no fixed-positive-time conclusion.

7. **Compact Stieltjes Padé theorem.** Gaussian quadrature uses exactly
   the first 2M moments, gives a rational function of type [M-1/M], and
   supplies positive weights and negative poles. The centered geometric
   polynomial has remainder at most [tR/(2+tR)]^(2M), giving the stated
   factor 2m_0 uniform bound. The finite-order epsilon formula is correct.
   Finite-support and zero-mass cases are accounted for.

8. **Unbounded determinate Stieltjes theorem.** The proof of weak
   convergence of quadrature measures passes moments using the next moment
   as a uniform tail bound. Determinacy identifies the limit. A common
   first moment proves the Lipschitz bounds required to include t=0 in
   compact uniform convergence. The Euler example has coefficients
   (-1)^p p!, right derivatives (-1)^p(p!)^2, zero Taylor radius, and an
   exactly rational Borel transform.

9. **Borel transfer.** A true tail bound plus compact rational convergence
   suffices for cutoff integration. Full Laplace integrals additionally
   need an approximant envelope. The stated cutoff error is correct. The
   finite quadrature derivative bound follows from the Hölder/Lipschitz
   modulus of u^sigma and the total weight at most one. The result is a
   rational function of t but generally not direct Padé of F. Full Laplace
   integration of a rational B_M is correctly allowed to be nonrational.

10. **Borel Stieltjes sufficient assumptions.** Compact positive-measure
    structure gives the displayed full-integral uniform bound, with a
    valid sequential U-then-M finite-order choice. The pushforward measure
    under v=xu^sigma proves F is itself Stieltjes. Its moment growth makes
    the Stieltjes Carleman series diverge for 0<sigma<=2. For sigma>2 only
    this particular direct-Padé argument stops; Borel–Padé still works.

11. **Coefficient conditions.** The Hausdorff inequalities have the right
    signs, normalization and quantifiers. They are equivalent to compact
    positive-measure moments. The alternate strict Stieltjes moment-matrix
    criterion plus geometric moment growth is a valid sufficient test;
    growth excludes mass above R. Neither is presented as a finite test or
    as sufficient identification of a separately defined GF observable.

12. **Other approximation routes.** The de Montessus statement is for a
    fixed denominator row with the exact number of poles, not generic
    diagonals. Capacity convergence is appropriately separated from
    uniform maximum error. The conditional locally bounded holomorphic
    family argument via Montel, Cauchy and the identity theorem is sound.
    The half-plane conformal map, coefficient conversion and geometric
    error bound are correct. The resulting rational functions match only
    M+1 coefficients and are not mislabeled as [M/M] Padé.

## Coverage and limits

Both the original one-input conjecture and its extension needed for the
fixed multiple-input configuration are included. The exposition retains
the stronger all-time conditional scalar statement without asserting that
the local GF theorem proves it. It covers direct Padé, Borel–Padé, finite
quadrature, Stieltjes compact and determinate cases, coefficient criteria,
nonpositive analytic alternatives, finite-width implications and the
remaining neural hypotheses. It does not claim neural Stieltjes structure,
all-order regularity for C^{1,1} activations, arbitrary restart closure,
or a universal diagonal-Padé convergence theorem.
