# Author reconstruction and scope check

2026-10-05. Checker: the same Codex task that authored these notes. This is
an author check, **not an independent review or a promotion review**. No
other agent was assigned or consulted for the new derivation.

## Frozen sources checked

- `RESULT.md`: SHA-256
  `49d6998a07bdc6c45b1ac6b7e411314656c321a9992105fe568baf16b0ce0322`.
- `TIME_AND_PREDICTION_ROUTES.md`: SHA-256
  `38e09aff3191e5b2ff477877d7ebcf6dcf63598bc746f8fbc8f7e5cc3f0300a1`.
- Imported architecture definition,
  `../closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`:
  `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2`.
- Imported historical coefficient count,
  `../closure_sampling_20261003/SPHERICAL_SOURCE_DIMENSION_ROUTE.md`:
  `bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8`.

The latter sources were read completely for their source contract and
counting argument. This check does not independently reprove their entire
ancestral all-time upper theorem. The new initialization lower theorem
does not depend on that upper theorem's truth: it uses only the canonical
first-layer initialization. Its application to the historical construction
uses the explicitly stated source/isometry/storage interface.

## Mathematical reconstruction

1. **Normalization.** The input v=x/sqrt(d) is unit length, so a dot v is
   standard normal. Row entries of A have variance one. The feature norm
   in the theorem is ||h||_2/sqrt(n). The theorem's root-width accuracy
   gives integrated squared error C^2/n, not C^2/n^2. The historical
   coordinate error 1/n is stronger and implies its hypothesis.

2. **Contour and sign.** The contour for exp(-itz), t>0, closes downward.
   Its orientation is clockwise. The double-pole residue is
   i*t*exp(-pi*t/2); multiplying by -2*pi*i gives positive
   2*pi*t*exp(-pi*t/2). The resulting transform is pi*t/sinh(pi*t/2).
   Fourier inversion has factor 1/(2*pi), so evenness cancels the two;
   integration gives the sine formula with coefficient exactly one.

3. **Hermite lower bound.** For odd degree all terms in the sine-integral
   formula have the same sign. Restriction to [sqrt(p),sqrt(p)+1]
   preserves a lower bound. The elementary upper bound on p! gives a
   factor p^-1 after squaring, and exponential exp(-C sqrt(p)). No
   cancellation estimate or asymptotic equality is assumed.

4. **Spherical eigenvalues.** Reconstructed via Gaussian mean shift and
   the radial moment. Low cases are 1/d at p=k=1,
   3/[d(d+2)] at p=3,k=1, and 6/[d(d+2)(d+4)] at p=k=3. The parity
   zeros and normalized-surface convention are consistent. For odd p,k,
   the quotient telescopes as stated. The cap integral for the k=1
   eigenvalue also works for the negative density exponent when d=2.

5. **Balancing exponents.** With p comparable to k^(4/3), both sqrt(p)
   and k^2/p have order k^(2/3). The polynomial factor is
   p^(-1-(d-1)/2)=p^(-(d+1)/2), hence k^(-2(d+1)/3). The condition
   p>=C_d k holds for all sufficiently large k at fixed d. Every
   remaining odd k has a positive p=k contribution.

6. **Finite-network transfer.** Every row of B has squared norm at most
   one by Bessel. Rows, not columns, are independent. The entrywise
   concentration tolerance n^-1/4/(2D_n) and a union bound yield failure
   at most 2D_n^2 exp(-sqrt(n)/(8D_n^2)). This goes to zero for each
   fixed d. No dense-to-population trajectory estimate is used.

7. **Adaptively chosen spaces.** The one concentration event bounds all
   D_n singular values of B/sqrt(n). The Bessel/trace argument then
   applies to every orthogonal projector, including ones chosen from B,
   all original rows, W, labels, or a trained trajectory. Thus no
   independence between the selected space and the neurons is assumed.
   If its rank is below D_n, the integrated error is at least
   n^-1/4/2, exceeding C^2/n for all sufficiently large n.

8. **Rank count and storage.** Odd spherical degrees through k have
   total dimension of order k^(d-1) for fixed d>=2; d=2 gives an
   elementary linear count. A source isometry into N selected coordinates
   is injective, so N cannot be below the source dimension. Storing a
   full symmetric N-by-N metric takes N(N+1)/2 slots. This is the
   precise premise for the quadratic storage consequence; a more compact
   encoding of that matrix is not ruled out.

9. **Output escape route.** Differentiation at w=0 makes the exact initial
   output derivative depend only on readout motion. Rotational invariance
   makes its expectation a sum of m copies of a univariate K_n. For
   orthogonal data the sign-reflection argument gives K_n(0)=0. The
   factors 4/(mn) and 4/m in the hidden second derivatives follow from
   differentiating the residual-free gates at w=0. This is not an
   all-time decoupling.

## Executed deterministic verification

From `/home/amir/Codes/PDE`:

```sh
python studies/orthogonal_tanh_time_legendre_20261005/check_harmonic_formula.py
```

Observed exit status: 0. Output:

```text
PASS: 8019 exact rational identities; no trained-network experiment.
```

The script uses only Python's standard-library exact fractions. It checks
the spherical eigenvalue formula against independent circle Fourier
coefficients and S^2 Legendre integrals, checks the quotient product for
d=2,...,12 and odd p up to 63, and checks the three low-degree identities.
It is a check of algebraic components, not empirical evidence for the
asymptotic theorem and not a substitute for its proof.

## Adversarial scope audit and outcome

- **Not restricted to iid compressed sampling:** selection of V is arbitrary.
- **Not an argument from the largest row:** the lower bound uses a positive
  spectral sum and concentration of bounded coefficient vectors.
- **Not just the population:** the final event concerns n actual neurons.
- **Not a prediction lower bound:** the initial prediction is identically
  zero. This is expressly disclosed in the result and route assessment.
- **Not an endpoint or Omega(n) lower bound:** neither is established.
- **Not a learned-state quadratic lower bound:** the proof uses fixed
  metric storage. The distinction is retained throughout.
- **No hidden growing-d claim:** d is fixed before n tends to infinity;
  the constants and width threshold can depend on d.
- **No sign or label-size loophole:** labels are absent from the lower
  proof; in particular both sign patterns and all small labels are covered.
- **No claim that an activity clock is nonanalytic for this network:** the
  two-exponential curve is explicitly a diagnostic example only.
- **No new efficient initialization or runtime theorem:** neither follows
  from the onset identity.

Outcome: the author reconstruction found no remaining correctness objection
to the stated source-space theorem and its implementation-specific storage
consequence. The desired new smaller all-time predictor remains unproved.
The notes are internally checked at this author-check level and unpromoted.
