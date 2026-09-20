# Informed internal review of the lead comparison

Reviewer: `order_selection_route`, 2026-09-20.

Reviewed file: `LEAD_COMPARISON.md`.
Reviewed SHA-256:
`161a0826011641a1dfa37838adc818d0e3576bfddbe0ad6866d19eb8b6a53189`.

Verdict: no unresolved mathematical objection within the stated scopes.
This is an informed internal check, not an isolated independent promotion
review. The reviewer first developed and froze its separate selected-optimizer
candidate and then received explicit authorization to inspect this lead
derivation. No endpoint or operator-route artifact was read. The complete
current lead file was reread for this report after the correction described
below. The applicable source scope already read comprises `docs/NOTATION.md`
and `docs/global_nonlinear.md` C.4.7.9, C.4.7.10.A–C, and D.3.

## Checked claims

1. **Monotone positive filters.** Completion of the ridge square gives
   `E_p(v)=<v,(I-Q_p)v>`. Zero-padding along the genuinely nested raw feature
   lists and the decreasing ridge prove the Loewner ordering, even for
   singular raw Grams. The consecutive-difference positive contraction
   satisfies `R²<=R`, so its squared norm bound telescopes for each fixed
   field. The text correctly excludes changing trained fields from that
   telescoping conclusion. The coefficient penalty in equation (4) is
   `sqrt(eta_p)/2=1/[64(p+1)]`.

2. **Initialized-action approximation.** The decomposition
   `B_p-A_0=Q_(2,p)A_0(Q_(1,p)-I)+(Q_(2,p)-I)A_0` gives equation (5) with
   precisely the stated factors. Neither this estimate nor its adjoint
   version assumes small action operator-norm error.

3. **Unchanged-GF small-loss certificate.** Inside the radius-`r` physical
   ball, the feature perturbation is bounded by `(A_*+2)r`, so the weighted
   training Gram changes by at most `2(A_*+2)r<=kappa/2`. The unhalved loss
   and weighted readout gradient give
   `||grad L||²>=2 kappa L`. The exact energy identity then gives the
   path-length estimate in equation (8), with coefficient `sqrt(2/kappa)`.
   The strict initial inequality excludes a first exit from the ball and
   establishes the claimed endpoint and exponential loss tail. The three
   passive prediction-gradient block bounds combine to exactly the stated
   constant `B`, giving the whole-circle output tail.

4. **Consecutive endpoints and conditional order limit.** Equation (9)
   follows by placing both finite-order endpoints around their predictors
   at the common finite time. The all-order conclusion explicitly assumes
   uniform certificates and finite-horizon convergence on every finite
   interval. Under those assumptions the uniform tail constructs the
   reference endpoint and justifies commuting the limits. The argument
   does not assert those assumptions for every canonical trajectory.
   The optional rate-transfer choice balances the stated exponential
   finite-time error and endpoint tail correctly.

## Correction checked in the current version

The earlier version chose `r_(p_j)<=2^(-j)` in Section 4. That only gave
`||(I-Q_(p_j))v||>=r_(p_j)` and did not, by itself, exclude an `O(r_p)`
bound with a larger constant. The current file instead chooses

\[
 r_{p_j}\le2^{-2j},\qquad v=\sum_j2^{-j}e_j.
\]

The vectors `e_j` are orthonormal, so the sum converges in the Hilbert
space. Since `e_j` is orthogonal to `V_(p_j)` and `Q_(p_j)v` lies in that
space,

\[
 \|(I-Q_{p_j})v\|
 \ge|\langle e_j,v-Q_{p_j}v\rangle|
 =2^{-j}\ge2^j r_{p_j}.
\]

The error-to-rate ratio therefore diverges along this subsequence, which
does exclude `O(r_p)` for the constructed field. The correction closes the
identified issue. The text also correctly limits this construction to
arbitrary Hilbert-space fields: it does not produce a slowly approximated
reachable canonical training trajectory.

No computation was needed. The review does not establish unconditional
full-GF endpoint convergence, a rate in dictionary degree on the reachable
family, or any additional extension beyond the reviewed file's claims.
