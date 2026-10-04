# Coordinator reconstruction of the activation/depth refinement

2026-10-04. Internal assembly check, not a promotion review. The coordinator
owns ACTIVITY_SENSITIVE_DEPTH_REFINEMENT.md and the separate initialization
lemma. Thus this is not represented as an independent review of either
of those two files. The component checks identify their own scopes and
source dependencies.

## 1. Exact reference and constants

The reference is the canonical finite width-n dense network with all L
hidden layers of width n, A_0 entries N(0,1), W_0 entries N(0,1/n),
independent blocks and zero readout. The mean loss and mobilities
(n,1,...,1,n) agree in every candidate. Unit queries are x/sqrt(d).
The compressor remains the previously constructed weighted selected-neuron
system with fixed metrics and corrected readout. These new source bounds
do not replace it by an iid reduced model, population limit, or ordinary
gradient flow.

For ordinary tanh and c tanh, the real feature variance is at most one,
so gamma<=1 and lambda=min(1,gamma/m)=gamma/m. Consequently every use
of Y/lambda, lambda^-2 and lambda^-3/2 in the components is converted
exactly to Ym/gamma, (m/gamma)^2 and (m/gamma)^(3/2), without an
extra activation-value factor. Arbitrary fixed signed labels remain
allowed subject to the displayed RMS restriction and positive gap.

## 2. Tanh source and storage algebra

The complete candidate ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md was
read at SHA-256
407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660.
The coordinator also read the complete relevant exact source, label,
spherical, runtime and depth-separation interfaces, reusing unchanged
previous complete reads of the original construction and local source
proofs. This is a quantitative implication from those explicit proofs,
not an independent promotion review of the entire earlier program.

The tanh formulas for value, slope and curvature imply the stated strip
bounds a=1/2, B=1, s=16/15, t=1. Maximizing curvature over
sinh^2(Re z)>=0 on |Im z|<=1/4 gives
4/(3 sqrt(3) cos(2 Im z))<1. The one-sphere Gaussian norm net
gives a strictly negative exponent after multiplication by 17^n:
at image threshold 49/16, its squared threshold is 2401/256 and
[(2401/256)-1-log(2401/256)]/2>log17. Thus the initialized cap
7/2 and subsequent strict real/complex tubes 15/4 and 4 have the
required probability and margins.

In the actual row-insertion identity, the learned query correction is
S*s*(K_src*S*sqrt(log(en))) times its mixed endpoint coefficient.
There are two activity factors and no inverse S in that endpoint.
The first-row update likewise contains S^2. Therefore candidate (13)
is the original formula before discarding S<=1. The angular cap (14)
makes both correction coefficients at most one. Its time cap uses
YS=16Y^2/lambda<=16c_L^2 because lambda<=1. These are genuine
smallness inequalities, not factors moved into a width threshold.

The Gaussian union at coefficient G_d=4 sqrt(d+3) leaves n^-2
after the stated n^(4d+10) net; the factor two in the response caps
provides room for its vanishing interpolation and insertion defects.
The deterministic query RMS coefficient entering the Gaussian variance
is b_*=(32/5)(64/15)^(L-2). The response radius calculation is

\[
c_t=G_d^{-1},\qquad
c_q=\frac{1/2}{16G_db_*+32},\qquad
8c_tYSU_*+c_qV_*\le a/4<a/2.
\]

The strict final inequality is the pole margin; all derivative estimates
used by the argument were certified on the larger safe strip a/2.
It does not infer a new analytic domain merely by enlarging the old
radius after the fact: the stopped source argument runs on the new
nested domains using these bounds. The dedicated component check further
reconstructs that continuation.

The spherical count gives the leading source term

\[
\frac{1024\,9^dG_d}{d!}
\left[\frac{16G_db_*+32}{a}\right]^{d-1}
\frac m\gamma\log^{3d/2+1}(en).
\]

Substitute a=1/2, G_d=4 sqrt(d+3), and the displayed b_*.
Since 64<=32 sqrt(d+3), this is bounded by a_(L,d) times
(m/gamma) log^(3d/2+1)(en), with a_(L,d) exactly synthesis (2).
The coefficient 2040(L+1) in its storage follows from the actual
inventory 1020(L+1)R^2 and (a+b)^2<=2a^2+2b^2; exact additions
2m+d+1 and data storage 10m(d+1) remain visible.

The synthesis describes the depth growth of the explicit bracket, not
an equality obtained by dropping its +32. It does not silently replace
d by data rank. The remaining numerical-base-to-dimension powers and
the fixed-dimension logarithmic thresholds are disclosed. For d=1,
the two-query time-only bound is used separately.

## 3. First runtime refinement and numerical diagnostics

The approximation tolerance of every source and its initialized image is
epsilon=n^-1 with coefficient one. Initialized operator norm 7/2 and
carrier coefficient K_src are different inputs. The initialized action
defect is bounded by 2(7/2+1)epsilon; the pairing coefficients use
the approximation coefficient one. Only the carrier term contributes
64K_src G_rt in the width-dependent exponent. This matches the exact
positions of those constants in EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md.

The comparison still has exponent C_1 u+C_2 u^2 sqrt(log(en)),
u=Ym/gamma. At the stated finite cap c_L, the elementary Gaussian
square completion converts epsilon=n^-1 to a strict C/sqrt(n) bound.
Both models' integrated prediction-speed tails use the same positive
Gram margin and physical clock, so increasing the source horizon to
32 lambda^-1 log(en) includes the fitted endpoint. No matched-loss or
rescaled-time conclusion is substituted.

The coordinator executed both complete embedded Python evaluators from
the frozen candidate once. The five depth rows and five storage rows
reproduced its displayed numbers. This checks arithmetic only, not the
Gaussian/local-interface proof. The exact formulas, rather than rounded
decimal values, are the certified theorem constants. In particular the
source-only cap 2.858e-7 at depth two was not confused with the joint cap
4.756e-16 needed by that first moderate-exponent error certificate.
The subsequent complete runtime reconstruction in Section 7 replaces
this intermediate certificate and retains the source cap at depth two.

## 4. Contractive subclass and the corrected premise

The candidate was read completely at
88f9a621c918bf8b9dbf210bd79085b8650a3533ad08655638afdd03a92787ac.
Its complete corrected reconstruction was read at
aa97669520cbc881511ac63fb1c5f0ae0ea5da5f0c2053aead5d129f7571c714.
The original unchanged-candidate PASS is superseded by its explicit
Section 9 correction. The synthesis takes that correction as part of
the result, preserving the frozen original.

For q_src<1 an external preactivation introduced at layer p cannot be
moved to the first layer in a geometric upper bound. The correct trace
coefficient is max_p t sum_(ell>=p) q_src^(2(ell-p)) K_ell, at most
t sum K_ell<=0.4. Recomputing D_0 with this coefficient preserves its
bound 512, hence all chosen budget, activity, radius and runtime constants.
The augmented P_ell recurrence has a fresh external allowance at every
layer. The actual query derivative j_ell starts at layer one. They are
not interchangeable and their separate uses were checked. The reversed
ordering of real b_ell is harmless only because the selected envelope
C_*=1 dominates their actual maximum. The runtime preactivation and
geometric-sum replacements F,C_f,Z_0 are essential when gate gains are
below one; the old formulas cannot be used unchanged.

The resulting storage has no extra C^(Ld) factor, but gamma<=c^(2L)
follows from the actual covariance recursion. The synthesis retains this
limitation and does not claim overall polynomial-depth complexity or a
depth-independent absolute label scale.

## 5. Initialization lemma versus unresolved training estimate

NONEXPANSIVE_INITIAL_QUERY_ROUTE.md is a coordinator derivation and
self-check. Its real-query induction conditions on lower initialized
layers, to which the next Gaussian matrix is independent. Polynomial
nets can be filled using a deliberately coarse C_L sqrt(n) Hessian
bound. That coefficient occurs in an error tending to zero and does not
replace the final normalized derivative constant. Conditional chi-square
concentration therefore yields 1+epsilon uniformly in every real query
and direction at fixed depth. The separate coordinate-tail union has
exponent 8(d+3), exceeding its 4d+1 net/row exponent.

During training the matrix is reused; that conditioning fails. Direct
differentiation displays the required product R_a J in normalized RMS.
The note expressly does not infer a bound on that product from its
separate RMS factors, or infer a negative result from failing to bound
the neuron maximum. This initialization result is not used as a premise
in any new all-time compression statement.

## 6. Completed broader-class reconstruction and scope

The broad activation candidate was read completely at
5c7877faece19eaac50c9fe9e7439027a02176d137ccc3c43a091f1410f4e5ba;
a truncated tool segment was reread in full. Its complete dedicated check
was read at SHA-256
083ae2981e62a4a347ca49c91b1d4eb1e8e03a378c8a5bdcd970166fad609bcf.
The nonlinear extension passes relative to the explicitly authorized real
and local insertion inputs. Its new complex joint budget keeps the top
carrier, both actual-amplitude reciprocal traces, and the passive-query
preactivation cap. The check reconstructs the moment/stop-removal order,
rather than importing a real-only bound as a complex premise. The new
activation requirement is a bounded strip derivative and finite value at
zero. Neither the sharp tanh numerical constants nor its improved source
radius are inferred for this class.

The affine child reconstruction is incorporated into that report with
its provenance. The reduced normalized adjoint and denominator in each
hidden update preserve physical time even at unequal reduced widths.
Readout projection error follows by integrating features, including when
the top affine slope is zero. Affine covariance has rank at most d+1;
identity reduces to the input Gram, so the scope restrictions stated in
the synthesis follow. The joint nonlinear proof and this affine proof
are distinct. Three harmless formatting defects in the frozen candidate
are recorded in its check; the synthesis uses the corrected exponent
2[d(L+5)+1] and clean prose without changing the frozen evidence.

The final dedicated tanh report was read completely, including its
check-only arithmetic correction, at
40b18c9c05a3b657753d30bad4e1b57ff1f813d47b764fca66366c13369b73e6.
It independently reconstructs the new scalar estimates and nested
full/cavity pole stops, and reproduces all finite arithmetic. The two
component refinements therefore have complete internal checks within
their stated inherited-interface scopes.

The report's Section 9 corrects its manual depth-two F from 34 to 19
and five dependent displayed constants. Its frozen candidate and both
evaluators already used F=19; all candidate theorem formulas and tables
are unchanged. The corrected report is the one cited by the synthesis.

## 7. Final activity-sensitive runtime refinement

The complete later candidate was read at
061d46972a7b026bd6b6b5176fc411214e82bd1e9d9e18ec5bd8e119fedbeaa2.
The coordinator's complete reconstruction is
RUNTIME_SMALL_ACTIVITY_CONSTANT_CHECK.md. It checks the true unit
readout-error coefficient, separate inhomogeneous source terms, actual
carrier activity, single allocation of lifted damping, width conversion,
and integrated endpoint speeds. The exponent is not bounded by imposing
the earlier extra C_1^-1 or C_2^-1/2 label restrictions.

All source, runtime, angular and time caps exceed 2.8e-7 at depth two.
The independent rational certificate in check_small_activity_constants.py
verifies that assertion and C_all<273202<280000, using rational brackets
for e and square comparisons for the source recurrences. Its source
evaluator is frozen and hash checked; the new runtime evaluator separately
implements the displayed later recurrences. Both derivation authors
also separately verified the conservative source-cap comparisons.

Thus the current synthesis reports Y<=(gamma/m)2.8e-7 and error
2.8e5 Y(m/gamma)^(3/2)/sqrt(n) as a certified simple depth-two pair.
The more detailed depth table is clearly labeled as a rounded evaluation
of exact formulas. The older first-pass table remains a correct weaker
bound but is no longer the primary result. Storage, algorithm, reference,
physical time and all-time probability scope are unchanged.

All artifacts belong to the existing closure_sampling_20261003 study.
The current manuscript and existing tracked changes were preserved. No
Git mutation, training experiment, promotion, or public claim was made.
