# Root internal check of the independent local route

Checker: root; date 2026-09-16. This is a complete author-side analytical
check, not a fresh isolated review or promotion gate. The route was frozen
before root read it. No numerical experiments or machine proof verification.

Input SHA256: d91c3c6d2e0b17d0ad7d5ee7882bca4aeced662a12a7a46d24e718c10b1d1cc3  route_local.md
Canonical source SHA256: 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c  docs/global_nonlinear.md

Coverage: every section and equation (1)–(24) of route_local.md, checked
against the canonical p=1 initialization in C.4.7.10 B and the exact
characteristic equations/physical metric in C.4.7.9 and D.3. Root had read
those complete relevant source sections before this check.

Observed outcome: the stated small-label basin theorem and its geometric
corollaries pass this internal analytical check. No missing proof estimate
was found for the stated scope. The following were reconstructed.

- The initialized gamma includes both ridge inverses and the transpose
  response term tau*b_0. Its numerator is positive from k>0 and
  v_0*(ell+eta)-k^2>=v_0*eta. It agrees with k_0/sqrt(tau+eta)
  in the separate axis calculation. The coordinate-axis upper features
  are independent and odd, hence their weighted Gram is m_0 I/2.
- The angular singular-value perturbation costs at most sqrt(2) times
  input displacement. At sqrt(m_0)/4 this leaves a least singular value
  sqrt(m_0/8). Thus lambda=m_0/8 is valid uniformly on the declared interval.
- The current upper-feature deviation is at most ||M-D||+2||w-g||,
  and therefore at most sqrt(5) times physical state displacement.
  The ball rho=sqrt(lambda)/(2sqrt(5)) gives TT*>=lambda I/4.
- The physical gradient and probability normalization give exactly
  L'= -||S'||^2 and ||S'||^2>=lambda L. Dividing energy by speed yields
  physical length <=2sqrt(L)/sqrt(lambda), not merely finite energy.
  The label bound lambda/(8sqrt(5)) makes total length at most rho/2,
  which closes the first-exit argument. The exponent and all factors of
  two in (14) and (15) agree with the unhalved loss.
- The characteristic velocity supremum bounds multiply sqrt(L) only by
  bounded M,c and fixed feature envelopes. They are integrable, proving
  the stronger topology and convergence of the full correlated laws.
- Finite b-moments make the integrated lower-feature map C1 on L2:
  its remainder is O(E|delta w|^2), and its derivative varies continuously
  in operator norm. The potentially false blanket assertion that a tanh
  Nemytskii map L2->L2 is Frechet C1 is not used. The remaining map acts
  through finite vectors and bounded marks. The stated local Lipschitz
  bound on the output gradient is justified.
- The current readout correction T*(TT*)^{-1}R has squared norm
  R^T(TT*)^{-1}R and fits exactly. The Hilbert graph formula decomposes
  c into ker T_* and the range of its right inverse. Invertibility of
  T(h)P_* follows from its distance to I being below one. Thus the local
  fitting set has codimension two. At a fit, local Lipschitz continuity
  of J plus first-order differentiability of the residual suffices to
  differentiate the loss gradient as 2J*J even without a full global C2
  assertion for the output map. Surjectivity of J gives exactly two
  positive normal eigenvalues and the infinite tangent kernel.
- The initial matrix acceleration uses c'=a(F_1-F_2) and M'=w'=0;
  independence removes the unwanted term in d'_1. The active lower
  vectors have disjoint Cholesky supports, so M''a_1 is nonzero as claimed.
  The nearby-angle nonzero statement is existential, accurately labelled.

Limitations: label amplitudes are small; the input-angle neighborhood is
near pi/2; no unit-label theorem is inferred from this argument. The
finite-state distance certificate and manifold claim concern the physical
carrier metric. Ordinary joint-law W2 is controlled by the common-mark
coupling and is not identified with that carrier distance. No generalization
or full-network accuracy assertion follows. The separate unit-label angular
extension is checked in other files.
