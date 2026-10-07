# Cross-route audit of real-node polynomial Picard continuation

2026-10-06. Full mathematical reconstruction audit of the frozen candidate.
No numerical experiment or implementation was run. This is an internal
cross-route check, not an independent original discovery or promotion review.
The reviewer authored the streamed-assembly route and had already audited the
separate Taylor route. The supervisor supplied the candidate and mentioned
that no defect had yet been found; the calculations below were reconstructed
directly.

**Verdict:** no outstanding substantive defect was found in the frozen Picard
candidate for its stated source event and exact-real operation model. It
constructs the paired nodal source values using only real activation and
first-derivative evaluations, with the explicit non-activation work and
storage bounds given there. It removes the high-order activation-derivative
backend condition of the Taylor route. It does not remove the requirement
that ordinary activation evaluations be available, or prove their bit cost.

## Inputs, hashes and complete reading

Read LOCAL_CONTINUATION_ALTERNATIVE.md completely, all 596 lines, at SHA-256

a41c246981d22abe002a5870934690ac254e2f427984661bfef048650f1a9e34.

Its scientific dependencies used in this audit were:

- RESULT.md:
  c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278.
- POLYNOMIAL_SETUP_ODE_ROUTE.md:
  46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6.
- POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md:
  2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42.
- docs/notation.qmd:
  78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023.

Both route notes were read in full. The relevant complete RESULT.md passages
checked were the shared and dense-model setup; source coefficients, complex
training maxima and source domain; all-horizon extension and its width gates;
source families, expansion, rank and pairing; and the complete setup and
selection/assembly cost derivations. The source probability event is an
imported hypothesis, not independently re-proved by this audit.

The inherited model has \(L\ge2\), positive fixed \(Y,\gamma\), normalized
inputs, possibly unbounded activation values, and the full original label
allowance. No new small-label cap is used. The zero-label branch is separate.

Applied the accessible rigorous-math and conjecture-audit instructions and
the repository notation contract. The prescribed canonical-notation skill
remained inaccessible; the already reported fallback was retained. No other
study, archived book, previous chat or research history was read.

## 1. Parameter estimates and analytic restart

The conservative coefficients in (2) dominate the finite forward/backward
recursions at operator cap twelve. Feature RMS obeys the recurrence with
forcing \(b\) and factor \(12s\), below the stated \(H\). Carrier RMS
is below \(B\). The sum of first and hidden parameter-block discrepancies is
at most \(\sqrt L\|e\|_2\), giving the displayed \(D_z\).

In backward subtraction, the reference carrier's coordinate bound \(M\)
is sufficient. The changed gate costs \(t_2MD_z\|e\|_2\), a changed
mixer costs \(sB\) times its block discrepancy, and propagation costs
\(12s\). The stated \(D_b(M)\) bounds the sum of at most \(L\) such
terms as well as the top readout and derivative gate.

The gradient blocks have norms bounded by \(sB,sBH,H\). Their Euclidean
block norm is at most the stated \(G\). For a hidden gradient difference,
the two outer-product terms cost \(HD_b(M)\|e\|_2\) and
\(s^2BD_z\|e\|_2\); the first-layer and readout blocks fit inside the
stated \(J(M)\). Taking directional limits gives the Hessian estimate in
the complex admissible domain.

At a passive real query the carrier maximum is at most \(\sqrt nB\).
Because \(D_b(M)\) is affine with nonnegative coefficients,

\[
\sqrt nD_b(\sqrt nB)\le nD_b(B).
\]

The initialized operator bound eight therefore gives the stated coordinate
bound \(C_{\rm qry}n\|u-v\|_2\), separately for the base and image families.
This argument does not confuse coordinate error with a dimension-free
operator estimate.

For the exact trajectory, early complex carrier control comes from RESULT.md
S.23, and late control comes from its parameter-tail extension. Applying the
endpoint estimate along the segment from \(\theta(T_0)\) gives precisely

\[
M=M_0+\sqrt nD_b(M_0)D_{\rm late}.
\]

The \((en)^{-16}\) factor makes the extra term negligible at fixed parameters.
The candidate explicitly uses the late imaginary bound \(3a/8\), not an
unavailable late \(a/4\) bound.

The radius \(\mathfrak b_n\) permits preactivation change at most \(a/32\)
and carrier-coordinate change at most \(1/4\). A first-strip-exit argument
closes since \(3a/8+a/32<a/2\). Operator/readout caps have ample slack.
The algebraic formula

\[
DF=-\frac2m\sum_a(\xi_a\xi_a^T+r_aD\xi_a)
\]

has norm at most \(\mathscr L\) throughout each such ball. This is an
absolute complex norm bound, with no assertion of complex Gram positivity.

The approximate-anchor error map contracts by at most
\(R_t\mathscr L\le1/8\) on the radius-\(\mathfrak b_n/2\) function ball.
Its image lies within
\(\mathfrak b_n/4+\mathfrak b_n/16<\mathfrak b_n/2\).
Uniform limits and Cauchy's formula give a holomorphic fixed point. Its
discrepancy is at most \(8/7\) of the anchor discrepancy, below the stated
factor two. This proves an analytic restarted solution from the computed
anchor without a new source event at a learned initialization.

Finally,
\(\|F(\theta)\|\le4YG\) and
\(\mathscr L\mathfrak b_n/2\le1/8\), so the candidate's
\(\|F(v)\|<Q=1+4YG\) holds on the restart disk.

## 2. Integrated interpolation has no degree growth

At \(K+1\) Chebyshev roots, the constant discrete cosine mode has squared
norm \(K+1\), and the other modes through \(K\) have squared norm
\((K+1)/2\). The interpolation coefficient formula consequently gives
\(\|I_Kg\|_\infty\le(2K+1)\max_j\|g(x_j)\|_2\), including vector data.

For \(b_k(x)=\int_{-1}^xT_k(u)\,du\), the integrated interpolant is a
linear combination of nodal data with scalar weights

\[
w_j(x)=\frac{b_0(x)+2\sum_{k=1}^Kb_k(x)\cos(k\theta_j)}{K+1}.
\]

Discrete orthogonality and Cauchy--Schwarz give

\[
\sum_j|w_j(x)|
\le\bigl(b_0(x)^2+2\sum_{k=1}^Kb_k(x)^2\bigr)^{1/2}.
\]

Here \(|b_0|\le2\), \(|b_1|\le1/2\). For \(k\ge2\), differentiating
the stated Chebyshev primitive verifies it directly. Bounding its value at
the upper endpoint and at \(-1\) gives

\[
|b_k|\le\frac1{k+1}+\frac1{k-1}\le\frac2{k-1}.
\]

With \(\sum_{j\ge1}j^{-2}\le1+\int_1^\infty x^{-2}dx=2\), the squared
weight bound is at most \(4+1/2+16<36\). This proves the integrated
operator norm bound six, independently of \(K\). Scaling by \(h/2\)
gives \(3h\). The vector-valued extension uses the triangle inequality
against \(\sum|w_j|\); it needs no coordinatewise norm conversion.

Thus the Picard contraction does not inherit the growing interpolation
constant \(2K+1\). That factor reappears only in the final defect estimate.

## 3. Real iterates and the analytic interpolation tail

The parameter-two Bernstein ellipse satisfies \(|x|\le5/4\). Its physical
coordinate \(t=h(1+x)/2\) has magnitude at most \(9h/8\), strictly below
\(R_t\) because \(h\le R_t/4\). The bound on \(F(v)\) therefore applies
on the entire ellipse. Vector-valued Cauchy applied to its symmetric Laurent
representation gives Chebyshev coefficient norms at most \(2Q2^{-k}\).
The degree-\(K\) tail is bounded by
\(2Q\sum_{k>K}2^{-k}=2Q2^{-K}=\zeta_K\).

For a real state \(u\) within distance one of \(v(t)\), operator and
readout norms stay below twelve and \(R_w\): \(v\) is within
\(\mathfrak b_n/2\le1/8\) of a true real state, whose operator caps are
below ten, and \(R_w\) includes more than one unit of real readout slack.
All real preactivations are automatically in the strip. The straight real
parameter segment is admissible.

Consequently prediction differences are bounded by \(G\|u-v\|_2\).
Using the controlled carrier at \(v(t)\) in the mixed vector-field
subtraction gives (19). This requires no carrier bound or complex analyticity
for a general Picard iterate outside the small complex tube.

Interpolation exactness on the approximating polynomial gives

\[
E_{i+1}\le3h\mathscr L E_i+(3h+h)\zeta_K
          \le\tfrac14E_i+4h\zeta_K.
\]

Here \(h\mathscr L\le1/32\), and
\(E_0\le Qh\le1/8\). For \(K\ge4\),
\(h\zeta_K=2Qh2^{-K}\le2^{-K}/4\); the recurrence keeps every iterate
within distance \(1/4\) of \(v\), validating the mixed endpoint estimate
at each step. Summing the geometric recurrence yields exactly (21).

## 4. Final defect constants and logarithmic iteration count

The final polynomial has degree at most \(K+1\), with
\(U_I'=I_KF(U_{I-1})\). Degree \(K+1\) instead of \(K\) changes none of
the stated arithmetic orders. Direct subtraction gives

\[
\|U_I'-F(U_I)\|_\infty
\le\Lambda_K\mathscr L E_{I-1}
 +(\Lambda_K+1)\zeta_K+\mathscr L E_I.
\]

Substituting (21) bounds the geometric part by
\((\Lambda_K+1)\mathscr L4^{-(I-1)}/8\). The remaining coefficient of
\((\Lambda_K+1)\zeta_K\) is at most

\[
1+\frac{16}{3}h\mathscr L\le1+\frac16=\frac76<2.
\]

This proves (22) with its stated conservative constant. The degree inequality
in (23) makes its second term at most \(\varepsilon_{\rm def}/2\).
The stated choice of \(I\) bounds its first term by
\(\varepsilon_{\rm def}/64\), so there is additional slack.

The degree search terminates exponentially fast. To check the proposed
explicit upper cutoff, put
\(A=64Q(1+\mathscr L)/\varepsilon_{\rm def}\ge128\).
For \(K=4+\lceil4\log_2 A\rceil\),
\(2^{-K}\le(16A^4)^{-1}\) and \(2K+2\le12+8\log_2 A\le9A\).
Therefore
\(4Q(2K+2)2^{-K}\le9Q/(4A^3)\le\varepsilon_{\rm def}/2\).
Both \(K\) and \(I\) have the claimed logarithmic bound.

## 5. Global prefix induction and source construction

The imported real defect lemma is used with its own constants \(A_n,J_0,C_0\),
not the larger local complex constants. For integrated defect at most \(\nu\),
the candidate's minimum in (25) gives the first smallness condition with
strict slack. Its quadratic condition is bounded by

\[
8(C_0+J_0)^2T e^{2A_n}\nu^2
\le\frac{T}{4T_+}\le\frac14.
\]

The bound \(T\varepsilon_{\rm def}\le\nu\) holds by definition. The lemma
then gives error at most
\(\min\{\mathfrak b_n/8,\delta_{\rm node}/(2C_{\rm qry}n)\}\).
The next anchor satisfies the analytic-restart hypothesis with room to spare.

This is a finite induction on completed prefixes: the first anchor is exact,
each established local defect controls that prefix, and only then is the next
panel constructed. The path is continuous and piecewise polynomial; finite
derivative jumps preserve absolute continuity and add no defect atoms.
No uncomputed numerical trajectory is assumed accurate in order to prove
its own accuracy.

The source estimate gives nodal coordinate error at most
\(\delta_{\rm node}/2\), including separate initialized-image error.
Images are formed using \(W_0\) or \(W_0^T\), not the trained mixer.
Applying the same scalar quadrature preserves exact pairing. Quadrature
accuracy concerns the exact analytic source and is then perturbed by these
finite nodal errors, so restart nonanalyticity is irrelevant. The global
weighted-simplex coefficients alone generate the source space; Picard nodes
and panel endpoints add no source generators.

## 6. Work, memory and comparison scope

Each Picard iteration evaluates the dense vector field at \(K+1\) nodes,
costing \(O(mPK)\) arithmetic and the separately stated scalar calls.
The direct integration/interpolation transform costs \(O(PK^2)\).
Generating the scalar integration matrix once in \(O(K^3)\) is a valid
conservative bound. No implicit solve, high activation derivative, or parameter
Hessian computation is needed by the algorithm.

Current node/coefficient arrays fit in \(O(PK)\), training workspaces in
\(O(LmnK)\), and the scalar matrix in \(O(K^2)\). Evaluating completed
panels at global time nodes costs \(O(PN_tK)\). Passive forward/backward
and initialized-image actions cost \(O(PN_tN_x)\), with their activation
and first-derivative calls additional.

Time-major streaming retains one temporal accumulator per spatial query:
\(O(LnN_x(p+1))\) words, explicitly included in (29). Temporal accumulation
and final harmonic projection have the cost stated in (28).
Source orthogonalization, selection, dense basis-to-basis initialization,
and metric assembly retain their full terms. Thus no missing dense work,
path replay, whole-trajectory storage, or free matrix-image evaluation is
needed to realize the displayed envelope.

At fixed admissible parameters,
\(N_{\rm pan}=O(\log(en)^{3/2})\) and \(K,I=O(\log(en))\).
The flow term is consequently \(O(P\log(en)^{9/2})\).
The quadrature and source ranks have their inherited polylogarithmic orders.
Every displayed non-activation setup term is \(n^{2+o(1)}\), with its
explicit dimension dependence retained before specialization.

For the inherited \(L\ge2\), \(P=\Theta(n^2)\) at fixed parameters.
Dividing (28) by the declared Euler cost \(PmT/h_{\rm E}\), with
\(T\asymp\log n\) and any inverse-polynomial step, gives a ratio tending
to zero. This comparison does not establish that Euler needs that step or
attains a particular accuracy with it, and gives no separation from a dense
solver using the same efficient continuation. These qualifications are
explicit in the candidate.

## Remaining qualifications

The result is constructive on the imported source event. That event's
confidence-to-width threshold is not made effective here. It uses exact real
activation and first-derivative values as separately charged operations.
Neither arbitrary activation computability, floating-point stability,
primitive-evaluation error, numerical rank detection, selector conditioning
nor bit complexity follows from the proof.

No new source event, small-label cap, fixed-feature approximation or hidden
true-trajectory oracle was found. The exact-real algorithm and full original
activation class are compatible with the stated ordinary scalar-evaluation
contract. No further must-fix defect was identified in the frozen candidate.
