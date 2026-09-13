# Tanh polynomial core: synthesis after independent freeze

2026-09-13. This is an author synthesis, not an independent review. It adapts
the construction in `H3_v2_route_basis.md` after reading the full frozen
`H3_v2_route_coordinator.md` and the draft `H3_v2_arithmetic.py`. The original
basis report is unchanged. No trajectory, numerical experiment or Git operation
was performed for this supplement.

The tanh core has the same proved finite dimensions and exact contraction
reduction as the original sine core. It additionally places the actual
initialized hidden activations at the two reference directions in the raw
feature spans. Inverse-Cholesky normalization gives exactly the same positive
filter as symmetric normalization and the same population dynamics after an
orthogonal coefficient change. No finite-order accuracy advantage is asserted.

## 1. Exact joint initialization and contraction

Use the canonical H6 source rule with the frozen words

\[
h_i=\tanh g_i,\quad \xi_i=A_0h_i,\quad
H_i=\tanh\xi_i,\quad p_i=A_0^*H_i,\qquad i=1,2.
\]

Set

\[
v=E\tanh^2G,\quad
\alpha=E\operatorname{sech}^2(\sqrt v\,G),\quad
\tau_{\rm core}=E\tanh^2(\sqrt v\,G),\qquad G\sim N(0,1).
\tag{S1}
\]

All three constants are strictly positive, and `0<v<1`, `0<tau_core<1`.
Positivity follows because the Gaussian is nondegenerate, tanh vanishes only
at zero, and sech squared is positive everywhere. Oddness and independence
give `E[h_i h_j]=v delta_ij`. Therefore the two forward sources are independent
`N(0,v)` variables. The reverse source covariance is
`E[H_i H_j]=tau_core delta_ij`. Its only nonzero expected named-source
derivative is `E[partial_(xi_i) H_i]=alpha`. Thus the exact joint law is

\[
\xi_1,\xi_2\stackrel{\rm iid}{\sim}N(0,v),\qquad
p_i=\zeta_i+\alpha\tanh g_i,\qquad
\zeta_1,\zeta_2\stackrel{\rm iid}{\sim}N(0,\tau_{\rm core}),
\tag{S2}
\]

with the reverse Gaussian group independent of `g`. Population expectations
remain separate; no index pairing of the two populations is introduced.

Use the bounded core coordinates

\[
X_1=(\tanh g_1,\tanh g_2,\tanh p_1,\tanh p_2),\qquad
X_2=(\tanh\xi_1,\tanh\xi_2).
\tag{S3}
\]

For a polynomial raw feature `F(X_1)` and a raw feature `B(X_2)`, define

\[
\beta_i=E_1[Fh_i],\qquad
\gamma_i=E_1[\partial_{\zeta_i}F].
\]

Append the call `A0 F` to the same causal program, after constructing the two
reverse probes. H6 gives

\[
A_0F=\xi_F+\sum_i\gamma_i H_i,\qquad
E[\xi_F\xi_i]=\beta_i.
\]

The centered Gaussian
`xi_F-sum_i(beta_i/v)xi_i` is independent of the old forward pair, since all
its covariances with that pair are zero. Its variance can be zero; this case
also has zero conditional mean. Consequently

\[
E_2[B A_0F]
=\sum_i\frac{E_1[Fh_i]}{v}E_2[B\xi_i]
 +\sum_i E_1[\partial_{\zeta_i}F]E_2[BH_i].
\tag{S4}
\]

The fresh forward innovation is integrated out of this particular contraction,
not deleted from the Gaussian action law. The second term is the actual
reverse-to-forward response and cannot be omitted. By actual adjunction,
(S4) is also `E_1[(A0* B)F]`; there is no independently supplied reverse matrix.

A useful equivalent form has only bounded integrands. Gaussian integration
by parts gives `E[B xi_i]=v E[partial_(xi_i) B]`, hence

\[
E_2[B A_0F]
=\sum_i E_1[Fh_i]E_2[\partial_{\xi_i}B]
 +\sum_i E_1[\partial_{\zeta_i}F]E_2[BH_i].
\tag{S5}
\]

To verify the integration by parts, hold the other coordinate fixed and use
the derivative `-x/v` of the one-dimensional Gaussian log density. The boundary
term vanishes because `B` is bounded. Its derivative is bounded at every
fixed polynomial degree, because it is a polynomial derivative on a compact
cube times a bounded tanh derivative. Fubini applies to these bounded or
Gaussian-integrable factors. The same bounded-derivative reasoning applies
to `partial_(zeta_i) F`.

All first-population expectations in (S4)–(S5) use four independent scalar
Gaussians `(g1,g2,zeta1,zeta2)`, and all second-population expectations use
two `(xi1,xi2)`. No added Gaussian dimension is needed to form the contraction
matrix. This reduction covers the polynomial core; an exhaustive tail that
introduces additional action words requires the full finite source program.

Here `tau_core` is the strictly positive *model variance* in (S1). A numerical
covariance regularizer in the general source compiler should instead be named,
for example, `epsilon_cov`; it has a separate zero limit. Sending `tau_core`
to zero would alter the canonical initialization.

## 2. Strict enrichment and density

For degree order `N>=1`, retain all products

\[
\prod_{j=1}^{d_\ell} T_{a_j}(X_{\ell,j}),\qquad
a_j\ge0,\quad\sum_j a_j\le N,\qquad(d_1,d_2)=(4,2),
\tag{S6}
\]

where `T_0=1`, `T_1=x`, `T_(j+1)=2xT_j-T_(j-1)`. Each feature is an
admissible finite bounded word and has absolute value at most one. Append
the bounded valid outputs of the original exhaustive code prefix through `N`,
omitting only literal syntax duplicates. Compile dependencies but do not
automatically add them as new retained columns. No empirical rank decision
enters the definition.

The joint density of `(g1,g2,p1,p2)` from (S2) is strictly positive on all of
`R4`, since it is the Gaussian density of `g` times the positive conditional
Gaussian density of `p-alpha tanh(g)`. Coordinatewise tanh is a diffeomorphism
onto the open cube. The law of `X1` therefore has a positive density there;
the analogous statement holds for `X2`. A polynomial vanishing almost surely
under either law vanishes on that open cube by continuity and must be the zero
polynomial. The products in (S6) have distinct leading monomials and form a
basis for polynomials of total degree at most `N`, so their feature Grams
are positive definite in exact arithmetic.

At `N=1,2,3`, the appended code prefix contributes only the constants already
present; its nonconstant seeds are unbounded and are not retained as bounded
features. Thus the retained counts and actual span dimensions are exactly

| N | First population | Second population | Action matrix entries |
|---:|---:|---:|---:|
| 1 | 5 | 3 | 15 |
| 2 | 15 | 6 | 90 |
| 3 | 35 | 10 | 350 |

Both spans strictly enrich at both transitions. A finite quadrature can still
have a singular or poorly conditioned empirical raw Gram; that numerical fact
does not contradict exact span independence, and the ridge below handles it
without deleting coordinates.

At higher orders the exhaustive bounded-word prefix ensures density in the
full initialized observable spaces by the established rational-word and
Fourier-cylinder arguments. No claim that this finite Gaussian core alone
generates the full canonical observable space is needed.

## 3. Inverse-Cholesky normalization and the correct matrix orientation

Let `psi_l` be the raw feature column and choose the fixed schedule

\[
\eta_N=\frac{1}{1024(N+1)^2},\qquad
G_\ell=E_\ell[\psi_\ell\psi_\ell^T],\qquad
G_\ell+\eta_N I=L_\ell L_\ell^T,\qquad
T_\ell=L_\ell^{-1},\qquad b_\ell=T_\ell\psi_\ell.
\tag{S7}
\]

`L_l` is lower triangular with positive diagonal. The ridge makes this defined
even when raw words are redundant or a finite quadrature Gram is singular.
Writing `S_l a=psi_l^T a` gives `U_l=S_l L_l^(-T)`, hence

\[
U_\ell^*U_\ell
=L_\ell^{-1}G_\ell L_\ell^{-T}
=I-\eta_N L_\ell^{-1}L_\ell^{-T}\le I,
\]
\[
Q_\ell=U_\ell U_\ell^*
=S_\ell(G_\ell+\eta_N I)^{-1}S_\ell^*.
\tag{S8}
\]

Thus this is exactly the positive filter of symmetric normalization. It has
the same strong-density proof: an earlier raw-span vector with coefficient
`a` has error at most `sqrt(eta_N)|a|/2`, and the nested raw spans are dense.
Only `eta_N>0` and `eta_N -> 0` are needed. The factor 1024 is a fixed design
choice, not a tolerance or a fitted coefficient. Moreover
`|b_l| <= eta_N^(-1/2)|psi_l|`, because the smallest eigenvalue of
`L_l L_l^T` is at least `eta_N`. The fixed-order bounded-feature stability
lemma in the original report therefore remains applicable.

Let `C_raw[i,j]=E_2[psi_2,i A0 psi_1,j]`. The correct transformed action matrix
and row-oriented feature tables are

\[
D=T_2 C_{\rm raw}T_1^T,\qquad
\text{feature_table}_\ell
=\text{raw_table}_\ell\,T_\ell^T.
\tag{S9}
\]

The right transpose in `D` is essential. The old prototype's symmetric
normalization allowed writing its right transform without a transpose; that
formula must change when `T_l=L_l^(-1)` is nonsymmetric. The arithmetic draft's
`inverse_lower` returns this `T_l`, so (S9) is its compatible convention.

For an explicit dynamics check, let `R_l=G_l+eta_N I`, let
`b_l^s=R_l^(-1/2)psi_l` be symmetric features, and set
`O_l=L_l^(-1)R_l^(1/2)`. Then `O_l O_l^T=I`, so `O_l` is orthogonal and
`b_l=O_l b_l^s`. Transform coefficient matrices by

\[
M=O_2 M^s O_1^T,\qquad D=O_2 D^s O_1^T.
\]

The contractions satisfy `a=O1 a^s`, `d=O2 d^s`. Substitution gives identical
`z2=b2^T M a`, `q=b1^T M^T d` and predictions at every circle input. The
middle velocity transforms as
`M'=O2 (M^s)' O1^T`; Frobenius norm and Euclidean coefficient gradient flow
are invariant under this transformation. Row and readout dynamics are
unchanged. The same static coordinate transformation pushes forward the full
joint population laws and preserves own-state restart. This proves genuine
dynamical equivalence, not just matching initial kernels.

At each fixed `N`, Gram convergence implies Cholesky and inverse-triangular
factor convergence by the finite scalar recursion: positive pivots persist,
and each division/square root occurs away from zero in the limiting positive
definite matrix. Finite precision may leave a pivot unresolved; raising a
numerical failure preserves the coordinate definition, whereas deleting the
direction would change it. Increasing arithmetic precision is a separate
limit. Cholesky on a potentially singular *source covariance* still requires
the coordinator's separate positive numerical covariance regularizer; the
feature ridge is not a substitute for that source-compiler argument.

## 4. Scope of the improvement

Compared with the original sine core, the raw degree-one lists now contain
the exact initialized `tanh(g dot e_i)` and `tanh(A0 tanh(g dot e_i))`.
The selected forward/reverse probes therefore follow the model's actual tanh
activation at the two reference directions. The construction retains the
same low integration dimensions, strict span enrichments and full response
formula. Formula (S5) permits core contractions through bounded integrands
without explicitly integrating an extra forward source.

These are structural advantages. They do not prove smaller prediction error,
better conditioning, faster convergence or visible learned motion at any
fixed degree. Containing the exact initial hidden fields as *raw features*
does not make the ridge-filtered initialized action exact, and does not change
C-H2's whole-circle frozen-observation reconstruction rule. The exhaustive
tail remains necessary for the full density proof and may introduce substantial
cost. No conclusion about practical density-tail cost follows here.

This supplement is compatible with any proved W2-convergent joint Gaussian
rule. It does not independently certify the draft Halton implementation or
the coordinator's pending Halton proof. The bounded-integrand version (S5)
needs only convergence of these particular coefficient integrals; full mark-law
and Gaussian-row consistency still needs the W2 argument. The fixed horizon
`T=1/200`, fixed represented law family, whole-circle nonlinear evolution and
ordered numerical limits are those of the original report and coordinator
synthesis, with no new trajectory assumptions.

## Provenance

Read-time SHA-256 hashes:

- Original route, unchanged:
  `0f9d504cf205934b407901b162dda490d2f2cd0652df4b9b39adcba1bec81583`.
- Coordinator frozen route:
  `66bead19680f8cd83b3769836ed32c260d8d3096923ba119197080358eee5908`.
- Arithmetic draft:
  `80f937397fede74a4c39c585d20854491bd03e4125850b25106753921bd644c0`.

Shared instructions were unchanged from the original report's recorded hashes.
The newly authorized cross-route exposure is explicit; this supplement carries
no independence claim.
