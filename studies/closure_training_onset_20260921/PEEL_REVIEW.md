# Internal mathematical review of Gaussian peeling

Date: 2026-09-21. This is a fresh internal mathematical check of the frozen
inputs below, not a promotion review. The solve-math-rigorously skill was
read and applied. No study history, other study, prior review, implementation,
or numerical output was used. No numerical experiment was run.

## Outcome and claim level

**PASS for the stated convergent Gaussian-atom representation.** I found no
mathematical error in identification of the initialized p=1 closure kernel,
the lower series, the coherent finite Gram construction, the inverse error
bound, the global argument bound, the Chebyshev approximation, or the final
uniform limit. The independent Bernstein construction in PEEL_DIRECT.md is
also valid at its stated rate.

**An exact finite terminating reduction of the full tanh kernel remains
unproved.** The finite source contraction is exact, and each prescribed
truncation is a finite expression in simple Gaussian moments and deterministic
scalar operations. The complete result requires an infinite-degree limit.
Neither the polynomial nontermination observation nor Gaussian-calculus E.1
proves that every other finite scalar representation is impossible. This
review does not upgrade the result to fulfillment of a finite-termination
request.

## Frozen inputs actually checked

Complete files, with SHA-256 verified against the assignment:

- PEELING.md: `5eb8af10ae0d41f3af01de62deae06315519bf41b27142b71de9fa870ffac7d2`.
- PEEL_ATOMS.md: `65b67d9e39c93f00f0c739a00b3574f569a12830a23aaad687c646385459f43f`.
- PEEL_DIRECT.md: `58136a3e1bf21896ca513a8d59c8c13695bae9164834337724cbd372a805047a`.

Established sources actually used:

- docs/observable_p1.md, complete:
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
- docs/global_nonlinear.md, Section 3, lines 281–504, and the supplied H3.1
  excerpt, lines 13265–13300:
  `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
- docs/gaussian_calculus.md, complete E.1 excerpt, lines 5474–5564:
  `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e`.

An initial read also printed global_nonlinear.md lines 5474–5564 while locating
the Gaussian-calculus excerpt; those unrelated established-source lines were
not used in the argument or verdict. No additional referenced material was
followed.

## Proof attacks and resolutions

1. **Wrong kernel or missing reverse response.** The retained feature Grams
   and normalized contraction in observable_p1.md give the two-coordinate
   block
   `M=[[v+eta,beta],[beta,s+eta]]` and row
   `h=(alpha*v,alpha*beta+tau*gamma)`. Thus
   `Lambda=(tau+eta)^(-1) h M^(-1) (A,B)^T`.
   Direct multiplication gives exactly the displayed q_A and q_B, including
   the negative `beta*tau*gamma` term in q_A and positive reverse-response
   term in q_B. The H3.1 derivatives are taken with source coordinates and
   scalar parameters fixed, as required by Section 3. At c=0 the derivatives
   of the output with respect to hidden parameters vanish, so the initialized
   tangent kernel equals the readout Gram. This identifies the projected p=1
   population kernel; it does not identify it with an unprojected network
   kernel.

2. **Taylor series outside its domain or invalid expectation exchange.**
   Every radius-r disk centered on the real line lies within the pole-free
   strip for `alpha<r<pi/2`. The exact modulus formula bounds tanh there by
   `max(1,tan(r))`; the corresponding bound for its first derivative is
   `sec(r)^2`. Cauchy's formula therefore provides a uniform summable
   geometric majorant for the bounded shift `alpha*tanh(G)`. It justifies
   both factorization and expectation exchange, including the gamma series.
   The bounds are independent of the correlation parameter. Degenerate
   correlations +1 and -1 require no density or covariance inverse.

3. **Loss of positive definiteness at finite truncation.** The proposed
   beta_N and s_N are entries of the actual Gram of `(tanh(G),k_N)`, not
   separately truncated inconsistent entries. Adding eta I proves
   `M_N >= eta I` at every degree, including degree zero and cases with
   `s_N>1`. The bounds `|s_N-s|<=epsilon*(2+epsilon)` and
   `||M_N-M||<=sqrt(2*epsilon^2+delta^2)` follow from the uniform k-error and
   the Frobenius norm. Applying the inverse identity to the three displayed
   difference terms gives exactly ell_N. No assumption that gamma_N stays
   nonnegative is used. The inverse constants are conservative but valid.

4. **An angular grid substituted for a global argument bound.** Each L_i in
   PEEL_ATOMS.md is centered: simultaneous reversal of its two Gaussian
   roots negates every summand of k_N. Independent coordinate pairs give
   `E(epsilon_1 L_1+epsilon_2 L_2)^2=2*kappa_N`. The common lower activation
   at a unit-circle input has second moment v, and its pairing with L_i is
   Lambda_N(u_i), also on coordinate axes. Cauchy–Schwarz then proves the
   stated l1 coefficient bound for all angles. Conditional averaging over Z
   leaves those pairings unchanged and justifies the optional sharper bound.

5. **Incorrect Chebyshev aliasing or ellipse constants.** The Joukowski
   image of the closed annulus has imaginary part bounded by b<pi/2, giving
   a holomorphic neighborhood and the stated modulus bound. Laurent
   coefficients yield Chebyshev coefficients of magnitude at most
   `2*M_b*varrho^(-j)` for j>=1. At the L=m+1 root nodes, every higher T_j
   aliases to zero or a signed T_r with r<=m; hence its interpolant has
   interval sup norm at most one. Twice the absolutely convergent tail is
   precisely `4*M_b*varrho^(-m)/(varrho-1)`. The cosine normalization,
   constant coefficient, m=0 case, and separately treated R=0 case agree.

6. **Hidden nonlinear random arguments left in the terminal contraction.**
   Expanding both outer polynomials and using independence of H_1 and H_2
   gives the displayed finite double-binomial moment formula. Its remaining
   random arguments are Gaussian. Derivative products are finite polynomial
   combinations of activation powers under the Q_j recurrence. Deterministic
   interpolation-node evaluations and ridge inverses are additional scalar
   operations; the result is not claimed to be a polynomial in a fixed finite
   list of moments.

7. **Unjustified diagonal limit or product error.** Each coefficient changes
   by at most ell_N; each outer argument changes by at most 2*ell_N. Real
   tanh is 1-Lipschitz and bounded by one, giving total kernel error
   4*ell_N before the outer approximation. Polynomial product error is
   `e_theta+e_phi+e_theta*e_phi`. The global R_N converge to a finite R,
   since all Gram entries and their ridge inverses converge. Their boundedness
   keeps the ellipse parameter uniformly above one, proving convergence along
   every diagonal N,m tending to infinity, uniformly in both angles.

8. **Finite Stein termination conflated with the full activation composition.**
   E.1 removes explicit non-Z Gaussian polynomial factors and terminates
   within its finite jet algebra, even for smooth nonpolynomial activations
   satisfying its derivative bounds. The present nested tanh composition is
   not such a finite polynomial factor expression. The texts correctly
   retain finite-order remainders and do not deduce general impossibility
   from this mismatch. The nonpolynomiality argument only rules out a finite
   universal pointwise polynomial peeling identity of the proposed kind.

## Remaining limitations

The numerical coefficients, quoted discrepancies, quadrature refinements,
implementation, and execution provenance in PEELING.md were not validated by
this mathematical review. The analytic bounds assume exact Gaussian moments
and exact scalar arithmetic. They do not certify quadrature or roundoff, a
practical cost-to-accuracy rate, training behavior, a closure-order limit, or
the user's stronger finite-only request. The result remains unpromoted.
