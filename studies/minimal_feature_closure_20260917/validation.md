# Author audit of minimal dictionary closures

Date: 2026-09-17. Checker: current primary agent, also the author.
Outcome: internally checked for the stated claims; not independent review
or promotion. This is an analytic study with no empirical conclusions.

## Inputs and version

HEAD during the audit was 019e3630237e33f58b9636c0aa67a039bebf0182.
Established scientific inputs are docs/NOTATION.md, docs/observable_p1.md,
and docs/global_nonlinear.md Section 3 and C.4.7.10.B/C.1/C.3. The source
manifest records exact bytes, including the shared instructions and reading
guide. Complete applicable source portions and required skills were read;
truncated tool reads were repaired. No other study was used.

## Checks and observed outcomes

1. **Initialization and retained correlations.** Compared the scalar and
   (2,2) probes with the exact Cholesky coefficients in observable_p1.md.
   The retained forward coordinates are phi(g_i)/sqrt(nu+eta) and
   phi(sqrt(nu) Z_i)/sqrt(tau+eta), with the same eta=1/4096. Their raw
   coupling is nu(1-tau), hence the stated normalized D. The lower b1
   uses the same g as w0. Omitting reverse-probe features explicitly
   changes the model and legitimately removes their additional lower
   Gaussian roots; it is not an independence approximation to p=1.

2. **Dynamics and physical factors.** Compared each block with H3.N2,
   replacing its normalized input by x/sqrt(2). Independently differentiated
   the unhalved loss in each block of the declared metric. All three
   velocities have the required -2 factor. M's actual transpose is used.
   On the reflected pair, directly summing the three squared velocities
   gives 4e^2 K_s, exactly matching the differentiated loss e^2.

3. **Well-posedness.** Checked bounded-mark Lipschitz estimates in the
   increments w-g and c, with finite M. Loss monotonicity bounds residual
   L1 by Y. The resulting c, M, and w increment bounds are finite on every
   finite time interval. No compactness or boundedness at infinite time
   is inferred. Gaussian tails do not enter the increment sup norm.

4. **Scalar fitting proof.** Substituted the reflection symmetry directly
   into the full vector field. Verified the gate cross term Q=C-rho B,
   including negative rho and the antipodal endpoint delta=1. Positivity
   follows from B<=C and rho<1. The e equation proves finite-time e>0
   before the monotonicity bootstrap, avoiding a circular sign assumption.
   Positive A,M preserve b2*c>=0; strict d>0 then follows for every t>0.
   Growth of A and MA proves actual paired activation motion in both
   layers, not just middle-parameter motion. The rate K0 is explicit
   and positive for delta>0; no uniform bound survives delta down to zero.

5. **Obstructions.** For reflected inputs with equal first coordinate and
   opposite labels, the initial upper features agree. The readout gradient
   cancels; c0=0 makes the other two gradients vanish. Uniqueness gives
   exact stationarity, not a slow-rate claim. For the axis-orthogonal
   antipodal pair, the bounded weight perturbation and bounded readout
   displayed in Section 5 fit exactly, establishing that this particular
   obstruction is dynamical at initialization rather than representation.

6. **Finite-data initial Grams.** Checked the elementary Gaussian
   integration-by-parts cancellation yielding A'(r)>0, including endpoint
   handling by continuity. Verified tanh's nonzero odd Taylor coefficients
   through its differential equation. The scalar Vandermonde system is
   invertible exactly under the stated nonzero/distinct-square condition.
   Generic direction selection excludes finitely many lines because
   x_j, x_i-x_j, and x_i+x_j are nonzero. For (2,2), the corresponding
   injective feature vectors and open support reduce to the same system
   after restriction to a line. These prove initial descent only; a
   time-dependent Gram lower bound is not supplied or assumed.

7. **(2,2) feature learning.** Verified the axis-pair invariant subsystem:
   transverse w is unchanged, cross entries of M have zero drift,
   and both unused feature contractions vanish by independence and
   oddness. The scalar all-time theorem applies on this subsystem.
   Continuity of the explicit initial accelerations under finite-data
   perturbation establishes local feature motion near that example;
   no perturbative long-time fitting claim is made.

8. **Dimensions and minimality.** Counted autonomous marginal coordinates
   (b1,w) and (b2,c) separately from frozen Gaussian carriers. The laws
   are typically singular on their ambient domains. In particular,
   scalar b1 retains g1 but generic training still depends on g2.
   The area covering argument rules out a 1D locally Lipschitz
   parametrization of the full 2D Gaussian initialization. Constant-only
   dictionaries give a0=0 and an initialized equilibrium. Minimality
   is restricted to positive dictionary sizes in this architecture and
   regular carriers, not all possible models or measurable encodings.

No unresolved correctness objection remains for these precisely scoped
statements. Generic long-time fitting and comparison to full p=1 are open.

## Verification record

Read back the complete proof, including the added generic-direction argument,
and compared the equations and coefficients to their established producers.
Input hashes were checked against the earlier read versions and were unchanged.
`git status --short -- studies/minimal_feature_closure_20260917 docs code`
showed only the new study and no modified established material. The closing
manifest is verified with `sha256sum -c` from the repository root. No training
jobs, numerical quadratures, timing comparisons, or code tests were run;
none are needed for the analytic claims above.
