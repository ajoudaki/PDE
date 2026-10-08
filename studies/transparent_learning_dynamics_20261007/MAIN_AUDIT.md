# Bounded audit of the assembled geometric result

2026-10-07. This auditor read all 738 lines of the initial assembled `RESULT.md`
(SHA256 `52ee9949c70f6e106dcb9840cca35126fd09a9699ba606e19e47aa9fc717ffc8`),
then reread the revised frame definition and endpoint argument. The revised
version inspected had SHA256
`66bde8857d4f6e016613d8f87685b4c6fd359c4ac87767c8e7af267389686f41`.
The other allowed scientific inputs were the supplied runtime and this author's
prior algebra/polar derivations. Linked counterexample routes and the integrated
source proof were not newly read. This is a scoped internal audit, not an
independent audit of the imported probability theorem or a promotion review.

## Verdict

No mathematical defect was found in the displayed geometric ODE, its exactness
proof, local matrix-function regularity argument, or polynomial complexity
claims. The revised endpoint proof is valid. One small setup correction remains
in the inspected version: explicitly state the imported sphere normalization
\(\|x_a\|=\sqrt d\) before deducing \(\|v_a\|=1\) from
\(v_a=x_a/\sqrt d\). Membership in \(\mathbb R^d\) alone does not imply
that norm. This changes no theorem or imported scope.

## Checks performed by derivation

- **Source metrics and readout.** Equations (2)–(4) reproduce the supplied
  metric update directions, including the intentionally unmodified coordinate
  gate. The factors of \(\sqrt m\) cancel exactly in (11). The terminal
  feature mask excludes the retained earlier blocks from the correction.
- **One indicator per frame.** This reduced state is sufficient. The indicator
  in frame \(\ell\) selects the receiving block, while the already-computed
  feature in frame \(\ell-1\) is the source-block projection for (13).
  No missing indicator or cross-frame overlap is needed.
- **Polar equations and signs.** Differentiating
  \(F_\ell O_{\ell-1}=O_\ell S_\ell\) gives (20). Its symmetry condition
  is exactly (14), including the incoming angular velocity. Differentiation of
  the Gram gives (15). The three index actions in (16) have the correct signs
  and placements. The readout transport term in (17) is also correct.
- **Midpoint identity.** With \(U=E+A\), \(A^\top=-A\), and
  \(\Lambda=\Omega_\ell-\Omega_{\ell-1}\), equation (14) gives
  \([S,A]=[G,\Lambda]/2\). Substitution into (15) proves (19). The stated
  qualification about symmetric off-diagonal deformation is appropriate.
- **Exactness and ranks.** The projected dyads write only the intended shear
  block. The reverse lift therefore preserves \(F=I+N\), \(N^2=0\), and
  \(F^{-1}=I-N\). Bound (21) follows from the norms of this map and inverse.
  Rectangularity, zero maps, and changes of original layer rank require no
  additional assumption. The original correction domain is still required.
- **Local smoothness.** At a compatible state, the finite multiplication
  matrices have real spectrum. Finite contours inside the activation's
  holomorphy strip enclose those spectra and still do so for nearby matrices.
  The contour formula defines a local holomorphic extension even for nearby
  tensors that are not exactly associative. Thus repeated eigenvalues do not
  invalidate local uniqueness. The SPD square root and positive-sum Sylvester
  solve are likewise smooth at repeated positive eigenvalues.
- **Actual feature motion.** Equations (22)–(24) follow by differentiating the
  physical forward pass with the original metric rank-one writes. The two
  product-rule terms in (24) are required for nondiagonal metrics and are present.

## Revised endpoint argument

The added energy argument closes the previously compressed inference. Explicitly,
the parameter norm on a map perturbation \(X_\ell\) is

\[
\|X_\ell\|_{\mathrm{HS}}^2
=\operatorname{tr}\!left(M_{\ell-1}^{-1}X_\ell^\top M_\ell X_\ell\right),
\]

with readout norm \(\|v\|_{M_L}\). The inner product of two update dyads
is the product of their backward and forward feature pairings, precisely as in
(4). For the source maps and raw readout collected in \(\theta\),

\[
\|\dot\theta\|^2=\frac4{m^2}c^\top Kc
=-\frac1m\frac d{dt}\|c\|^2.
\]

Hence the unit-interval Cauchy–Schwarz bound in the revised text is exact.
Exponential residual decay makes the resulting bounds summable and gives finite
parameter length. This reasoning needs neither a hidden backward-response
bound nor a gradient interpretation of the corrected predictor. Continuity of
the polar construction then gives its limiting state. The revised distinction
between evaluating a nonsingular limiting correction and merely transferring
a supplied predictor limit is necessary and correctly stated.

## Complexity and inherited claims

The scalar count in (29) is correct for the declared dense representation:
one symmetric \(D\)-square matrix, one full \(D^3\) tensor, two vectors
per layer, and the readout/residual state. The larger tensor storage does not
claim to be minimal. With \(D=d+\sum_\ell q_\ell\), the headline cubic
storage envelope is correct, with the later explicit dependence on \(d\)
and depth.

Sequential one-index tensor rotations and the tensor differential equation
cost \(O(LD^4)\). The separate remaining arithmetic bound
\(O(mLD^3+m^2LD+m^3)\) covers dense product contractions, kernel formation,
correction, square roots, and angular solves, excluding activation matrix-function
work as stated. Treating that work as a cubic primitive is explicitly conditional.
The workspace bound and the separate initializer costs are consistent. No
precision-uniform complexity claim is established or presented as established.

Exact equality of predictions transfers every valid source certificate on its
actual event, input set, norm, and time domain, including a supplied fitted
predictor limit. The conditional pairing estimate (27) also checks: expanding
two errors of norm at most \(e\) against reference vectors of norm at most
\(H+3\eta\) gives \(2(H+3\eta)e+e^2\), followed by the stated pairing
defect. The imported bounds underlying that defect, the constants and precise
formula in (26), and source formula (28) were not independently verified by
this auditor. The text's separation of inheritance from an independent reproof
is therefore essential.

The reported deterministic script results were read as the lead author's
reported checks. This auditor neither inspected nor executed the script and
does not certify its numerical outputs independently. Its stated interpretation
as local identity checking, rather than statistical or global validation, is
appropriate. The Section 2 counterexample summaries likewise remain reports of
their linked routes within this bounded audit.

The earlier disclosed information-retention limitation is unchanged. No further
scientific correction was identified within the audited scope.
