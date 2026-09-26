# Internal mathematical check of the initialization-calculus answer

Checked on 2026-09-21. The complete checked input is
`INITIALIZATION_CALCULUS.md`, SHA256
`a3d17e362d18b4fe1f4efdbdccdd9787231e66c6e93e89b4e137eaafe09f865a`.

Verdict: PASS for the stated static representation and convergence claims.
There is no remaining substantive mathematical correction identified in the
frozen input. A raw-versus-normalized matrix notation ambiguity in the earlier
version of (11) was corrected before this hash was frozen.

This is an internal scoped check by a contributor to the derivation, not a
fresh independent isolated review, a promotion decision, or user approval.
No experiments, numerical approximations, or trained trajectories were used.

## Input and source coverage

The entire checked note was read, including all equations (1)–(15), its source
and scope declarations, and its final limitations. Scientific sources actually
read for this check and the preceding scoped derivation were:

- Complete `docs/observable_p1.md` and `docs/NOTATION.md`.
- `docs/gaussian_calculus.md`, complete Sections 1–4: Gaussian reuse,
  conditioning, finite differentiation, and Gaussian integration by parts.
- `docs/global_nonlinear.md`, complete Section 3, including the singular-source
  convention and the source/response rule.
- The relevant H3 definitions in `docs/global_nonlinear.md`: the dense compatible
  hierarchy, polynomial-core dictionaries and degree-three enrichment,
  contraction (H3.1), ridge normalization (H3.2), and the finite closure
  definitions (H3.N1)–(H3.N2).

No older artifact in this study, another study, or its research history was
read. The note's references to additional Gaussian-calculus sections are not
claimed as additional source coverage by this check. The displayed series
convergence is checked directly, without importing a temporal analyticity or
infinite-forest theorem from those sections.

## Equation-by-equation checks

### Initialization and equations (1)–(2)

The lower reverse coordinate is `sqrt(tau) Z_i + alpha h_i`, with
`alpha = E tanh'(Xi_i) = 1 - tau`. This preserves the response from the actual
reused action. Lower pairs and upper coordinates have exactly the independent
Gaussian sources specified by the book; lower and upper population indices
are not paired.

The dictionaries through degree three have no added nonpolynomial code-prefix
feature. Each retained raw Chebyshev product is bounded by one. Positive ridge
makes each Cholesky factor invertible. Substitution gives

`b2^T M E[b1 h] = psi2^T L2^{-T} M L1^{-1} E[psi1 h]`.

Thus both directions of (1) and the prediction (2) have the correct transpose
and multiplication order. The unit circle is in the normalized input `u`.

### Equations (3)–(5): scalar derivative and covariance expansions

For every fixed derivative order, the tanh compositions and all their
derivatives are bounded. Gaussian integration by parts has vanishing boundary
terms, and conditioning/differentiating the function `j` is justified by a
bounded integrable majorant. The scalar Hermite coefficients are therefore
exactly the derivative expectations written in (3).

The stated Hermite generating functions give orthogonality and the correlated
pair identity. Completeness is justified by the entire-transform argument:
on each compact complex set, Gaussian exponential moments and Cauchy–Schwarz
dominate the transform and its derivatives. Orthogonality forces its entire
power series to vanish, and Fourier uniqueness applies to the integrable
density `F` times the Gaussian density. These hypotheses are satisfied.

Parseval and Cauchy–Schwarz prove absolute uniform convergence in (4), including
the degenerate correlations `rho = +1` and `rho = -1`. The lower vector (5)
then follows by conditioning on `G_i` in the reverse coordinate. Its constant
entry vanishes by symmetry. The function `B` retains the response term; it is
not a fresh-noise replacement.

### Equation (6): multivariate series and uniformity

For each retained lower dictionary word, conditional expectation over `Z`
leaves a bounded smooth function of `G`; differentiation under that expectation
is justified at every fixed order. The multivariate Hermite coefficients of
`tanh(G dot u)` are `d_{|a|} u^a`, since `|u| = 1`. Integration by parts gives
the other coefficient in (6).

For the absolute tail over `|a| > N`, Cauchy–Schwarz gives exactly

`||Fbar||_2 (sum_{m>N} d_m^2/m!)^(1/2)`.

Here the multinomial identity
`sum_{|a|=m} u^{2a}/a! = (u1^2 + u2^2)^m/m! = 1/m!`
holds also when a coordinate of `u` is zero. This proves absolute convergence
and a tail uniform over the whole circle. There is no temporal Taylor-series
claim or exchange of a width limit with differentiation.

### Equations (7)–(8): all finite matrices

Each raw lower contraction has absolute value at most one, so
`|psi2^T K A_p(theta)| <= sum_ij |K_ij| = S` uniformly in both the circle and
upper marks. The `S = 0` branch is correct.

For `g(phi) = tanh(S cos(phi))`, the first derivative vanishes at both
endpoints, and direct differentiation gives `|g''| <= S + 2 S^2`.
Twice integrating the cosine coefficient by parts therefore proves the
`2(S + 2 S^2)/k^2` bound. Symmetry removes every even coefficient. Absolute
uniform convergence and uniqueness of Fourier coefficients identify the
series with `g` for every finite positive `S`.

On the actual argument, `|T_k(Q/S)| <= 1`. Thus summation through the readout
expectation is dominated by `E|c| sum_k |gamma_k|`, and the uniform degree-`N`
tail is at most `2(S + 2 S^2) E|c|/N`. Every term expands to finitely many
initialized bounded-word moments and a polynomial in the lower channels.
This establishes (8) for arbitrary finite normalized `M` through (1); no small
matrix assumption is present. The infinite sum itself is correctly not called
a finite forest evaluation. Polynomial coefficient expansion need not be a
numerically well-conditioned evaluation method, and no such claim is made.

### Equations (9)–(11): the readout and the first-response obstruction

`mu2 > 0`, and the definition `lambda0 = mu4/mu2` makes `P3` orthogonal to
`H`. Symmetry gives orthogonality to `1` and `H^2`. Positive density of `H` on
`(-1,1)` makes the squared norm `nu` strictly positive. Expansion verifies
`nu = mu6 - mu4^2/mu2`.

Since `tanh''(Xi) = 2H^3 - 2H`, equation (10) is exact. The real coefficient
`lambda0` is obtained from finitely many initialized moments. Thus this is
a finite moment/activation/derivative construction; it does not require a
target-encoding rearrangement. It is a real linear combination of initialized
words, not an assertion that an irrational scalar must itself have a literal
rational grammar code.

Independence of `H1` and `H2` proves orthogonality to every upper feature at
`p = 1,2`, including the constant and mixed quadratic feature. The linear
matrix variation of the output therefore vanishes for every matrix direction.
The final version of (11) correctly inserts
`K0 = L2^{-T} M0 L1^{-1}`. Differentiation is dominated by bounded features
and the fixed readout. The cubic remainder bound follows from
`|tanh z - z| <= |z|^3/3`, obtained by integrating
`1 - tanh'(z) = tanh(z)^2 <= z^2` on the real line.

This is explicitly a statement at `M = 0` with the chosen nonzero readout,
not at the canonical initialized state `M = D, c = 0`.

### Equations (12)–(15): explicit matrices and exact circle functions

The Chebyshev coefficient vector for `P3` is correct because
`T3(H) = 4H^3 - 3H`. Its only nonzero entries are `1/4` at `T3(H1)` and
`3/4 - lambda0` at `T1(H1)`. Choosing the stated raw `h1` column therefore
produces the two preactivations (12) exactly. In particular, the retained
lower coordinate `h1` has the same raw contraction `A(cos(theta))` at every
order even though its normalized coordinates differ.

The distinction between the raw coefficient `t` and normalized Frobenius
matrix cost is material and correctly stated. More explicitly, if `r3` is
that two-entry upper coefficient vector, the squared costs per `t^2` are

- `p = 1`: `(tau + eta1)(v + eta1)`;
- `p = 3`: `(nu + eta3 ||r3||^2)(v + eta3)`.

Thus the construction does not assert equal matrix norms. Formula (13) is
the exact output after integrating away the unused upper coordinate.

The poles of `tanh(z) = (exp(2z)-1)/(exp(2z)+1)` nearest the origin are at
`z = +/- i pi/2`. The stated strict uniform argument bound therefore places
the entire real integration range inside a compact subset of its Taylor
disk. Absolute uniform convergence permits the expectations in (14).
For the first expression,
`E[P3(H) H^(2j+1)] = mu_(2j+4) - lambda0 mu_(2j+2)`;
for the second, the coefficient is `E[P3(H)^(2j+2)]`.

The linear term of the first expression vanishes, and its cubic moment is
`E[P3(H) H^3] = nu`. The linear and cubic terms of the second expression are
`nu` and `E[P3^4]`, respectively. This verifies every coefficient and sign in
(15). Bounded arguments make the displayed fifth-order remainders uniform
in the circle variable. At `theta = 0`, `A(1) = v > 0` and `nu > 0`, so the
different first nonzero orders describe a nontrivial family.

## Boundaries of this verdict

The input proves exact static closure formulas, convergent coefficient series,
and a local matrix-response distinction with a fixed initialization-derived
readout. It proves neither global representational separation between orders,
unrestricted equality of the `p = 1` and `p = 2` function classes, matched-cost
accuracy ordering, training reachability, nor learned performance. It does
not supply elementary closed forms for generic tanh Gaussian moments or a
certified numerical cost-to-accuracy comparison. These boundaries are respected
by the checked note.
