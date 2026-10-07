# Cross-route check of streamed local-continuation assembly

2026-10-06. Verdict: PASS for the candidate's explicit conditional Taylor-jet
interface and exact-real arithmetic model. No required correction was found.
This is a cross-route internal check, not an isolated promotion review and not
a proof that a backend supplies the assumed node errors.

## Assignment and complete read coverage

The frozen candidate was LOCAL_CONTINUATION_ASSEMBLY.md, all 622 lines, SHA-256
488216678b1ea31fcfb8da5f396c8323eae3a38be067c2e431de21a600df2fe2.
Its hash was checked before and after the audit and was unchanged.

The reviewer authored LOCAL_CONTINUATION_ALTERNATIVE.md before seeing this
assembly candidate. The supervisor's assignment authorized this subsequent
cross-route audit. Thus the review is distinct-author checking with disclosed
prior route knowledge, not a blind independent promotion review.

Permitted scientific dependencies read were the complete existing
POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md and POLYNOMIAL_SETUP_ODE_ROUTE.md,
docs/notation.qmd, and the relevant RESULT.md sections. In addition to the
previously read model, source-domain, source expansion, finite construction,
all-horizon extension, and arithmetic/factored-jet sections, this audit read
the complete selected architecture/exact initialization section, learned and
retained storage section, coordinate-selection/source-metric proof, and
source-selection/assembly cost proof. The original analytic source event,
global source-comparison theorem, and backend correctness are imported
dependencies, not freshly re-proved in this check. The quadrature check
mentioned in the candidate's provenance was not used.

No other candidate, study, history, archived book, numerical experiment, or
implementation was read or run. Required accessible rigorous-math and
conjecture instructions, the shared research process, and the canonical
notation contract were applied. The unavailable canonical-notation skill and
its neural-network reference remain the previously disclosed permission
limitation.

## 1. Accuracy, exact pairing, and final source dimension

The candidate requires the base feature and backward source polynomial at
each assigned quadrature node to have unnormalized Euclidean error at most
\(\delta_{\rm node}/8\). Since the initialized matrix has operator norm
at most eight,

\[
\|W_0(\widetilde g-g)\|_\infty
 \le \|W_0(\widetilde g-g)\|_2
 \le 8\|\widetilde g-g\|_2
 \le\delta_{\rm node}.
\]

The same bound applies to transposed initialized images. The base coordinate
error is also at most \(\delta_{\rm node}\). This avoids the incorrect
inference that a coordinate error can be multiplied by a dimension-independent
operator norm without paying a Euclidean conversion. If only coordinatewise
base estimates are supplied, the candidate correctly requires
\(\delta_{\rm node}/(8\sqrt n)\).

Moving \(W_0\) outside the finite scalar projection is an exact algebraic
operation. Thus coefficient-level image formation equals nodal image
formation followed by quadrature, even though nodal image vectors are not
actually materialized. The initialized matrix must be \(W_0\), not the
learned panel anchor \(W_b\); the candidate expressly distinguishes them.

For \(d\ge2\), the magnitude of each scalar temporal multiplier is at most
two, the real harmonic multiplier at most \(\mathcal Y\), and the positive
spatial weights have mass at most \(A_d\). Hence the error in each coefficient
from inaccurate nodes is at most

\[
2A_d\mathcal Y\,\delta_{\rm node}=\epsilon_c/2.
\]

This argument applies separately to each exact base or image source; no
analyticity of the numerical polynomial is assumed. Adding the independently
bounded exact-value quadrature error gives coefficient error
\(\epsilon_c\). The finite retained reconstruction then adds at most
\(N\mathcal Y\epsilon_c=\eta/16\) to the original tail \(\eta/16\).
The claimed \(\eta/8\) error is therefore valid.

In dimension one the same reasoning has time multiplier at most two,
no angular multiplier, and node allowance \(\epsilon_c/4\). Each of the two
point families has coefficient error at most \(\epsilon_c\) and reconstruction
error at most \(\eta/8\). The separate count \(R=2m+d+1+8N_1\) is correct.

Panel contributions are summed into the same globally retained modes, not
adjoined as independent source generators. Thus neither panel count nor local
polynomial degree multiplies the rank certificate. Forming paired images
after projection adds exactly the image columns already included in the
four-family bound. With at most \(2(L-1)N\) such columns, the explicit
\(O(Ln^2N)\) image charge is correct.

## 2. Scalar moments and streaming reconstruction

Expand each local source polynomial at each assigned time node and interchange
finite sums over panels, times, spatial nodes, and local powers. This gives
the candidate's moment table

\[
B^{(b)}_{kc}=\frac{\gamma_k}{N_t}
 \sum_{a\in I_b}\cos(ku_a)
 \left(\frac{t_a-\tau_b}{\Delta_b}\right)^c
\]

and its coefficient formula exactly. Repeated physical times from the cosine
map remain distinct quadrature indices; counting their weights separately is
correct. A boundary node is assigned once. Its prescribed accuracy interface
is enough regardless of which adjacent panel owns it.

For each time node, constructing powers, temporal cosines and their outer
product is bounded by \(O((p+1)K)\), since \(K\ge1\). Clearing each panel table
costs the same order. Thus \(O((N_t+J)(p+1)K)\) covers all moment work.
Sorting costs \(O(N_t\log(2+N_t))\), or the grid's two monotone halves can
be merged directly. Both options are explicitly charged.

Temporal-first projection transforms \(K+1\) vector coefficients into \(p+1\)
modes for every streamed query, then touches only the \(N\) retained harmonic
pairs. Its bound

\[
O(LnJN_x[(p+1)K+N])
\]

is correct. Spatial-first projection first accumulates all \(K+1\) jets against
\(H_{\rm sph}\) harmonics, then transforms only retained pairs; its bound

\[
O(LnJK[N_xH_{\rm sph}+N])
\]

and extra \(O(LnKH_{\rm sph})\) vector buffer are correct. These are alternative
implementations, not unproved simultaneous minima.

The stated panel-major ordering computes dense training jets once per panel,
processes all spatial nodes while those jets are live, advances the anchor,
then discards the panel. No \(N_x\)-fold repetition of the dense continuation
is hidden. Panels with no coefficient-quadrature nodes can skip passive work;
charging all panels only enlarges the upper bound.

The scalar geometry can either be recomputed per panel or cached with
\(O(N_x(H_{\rm sph}+d))\) additional words. The candidate attaches the
appropriate work and memory to each choice. Input-node mapping on repeated
passes is covered by the displayed basis/geometry envelopes. Dimension one
has only its two fixed inputs.

## 3. Factorized jets and dense-anchor update

At an arbitrary learned anchor, coefficient comparison in the dense rank-one
ODE gives, for \(s\ge1\),

\[
[W^{(j)}]_s=-\frac2{mns}
 \sum_a\sum_{i+k=s-1}[r_a\delta_a^{(j)}]_i
                         [h_a^{(j-1)}]_k^T.
\]

Zero readout is not needed for this identity. The constant mixer action is
the current anchor; the remaining coefficient action on a query series
contains indices \(i+k+c=s-1\), so every increment uses only lower orders.
This confirms causality of the shared training recursion and of the cached
contractions. Transpose actions interchange the two training factors.

The inherited cached-factor arithmetic therefore gives, over all panels,

\[
O\!\left(J\{P(m+N_x)K+
 Lm(m+N_x)K^2(n+K)\}\right).
\]

The live dense anchor and original initialized arrays cost a numerical
multiple of \(P\), and the jets/contractions use
\(O(LmnK+Lm^2K^2)\) further words. One passive query can reuse the same
scratch across all spatial nodes. This verifies the stated memory bound.

Anchor advancement deserves a separate check because generating factored jets
does not itself write a new dense matrix. Summing all Taylor terms through
degree \(K\) and grouping by the weighted-response order gives

\[
\Delta W^{(j)}
 =-\frac2{mn}\sum_{i=0}^{K-1}U_iV_i^T,\qquad
V_i=\sum_{k=0}^{K-1-i}
 \frac{\Delta_b^{i+k+1}}{i+k+1}H_k.
\]

This is the exact triangular endpoint sum. Forming the \(K\) vectors or
\(n\)-by-\(m\) blocks \(V_i\) costs \(O(nmK^2)\); applying their \(K\)
rank-at-most-\(m\) outer products costs \(O(n^2mK)\), per hidden layer.
The vectors can be formed one at a time after the panel's passive-source
processing. Updating the dense anchor then cannot invalidate a still-needed
query. First-matrix and readout endpoint updates fit the stated
\(O(PmK+LnmK^2)\) bound. This is absorbed by the training term and introduces
no omitted \(n^2mK^2\) charge.

For \(K=1\), the formula reduces to the single Euler/Taylor increment with
\(V_0=\Delta_bH_0\), confirming its normalization and boundary indexing.
The materialized alternative is also valid but is not needed for the sharper
factorized bound.

Activation composition and scalar derivative generation are explicitly
outside non-activation arithmetic and are charged through the four backend
functions. No fast high-order derivative oracle is inferred from analyticity.

## 4. Exact initialization, selection, and peak storage

The exact initialized training features, their initialized forward images,
the constant, and first-weight columns are retained from the first panel.
The first anchor is the original initialization, so these are the exact
vectors required by RESULT.md. Later approximate anchors do not replace them.

The source bases and paired initialized actions therefore meet the same
selection and exact-initialization assumptions. The existing charges

\[
O(LnRr+Lnr^3+Ln^2r+Lq^2r)
\]

are all retained. In particular the basis action \(W_0U\) is not assumed to be
supplied by the paired source columns for free. It is correct to charge both
\(Ln^2N\) for image coefficient formation and \(Ln^2r\) for full-basis assembly.

All coefficient blocks need \(O(LnR)\) words. Panel jets and dense continuation
anchors can be discarded before selection; the original initialized matrices
must remain until assembly. Their storage stays inside \(O(P)\).
The candidate's peak bound is a safe sum of buffers, not a claim that they are
all simultaneously necessary. It avoids \(JP\), \(JPK\), and \(N_tN_x\)
dense-state/source caches.

The learned-state and all-retained inventory formulas match the exact
selected-dimension formulas in RESULT.md. The final compressed model starts
from the original initialization. The last dense anchor is not silently
substituted as the compressed initial state.

## 5. Fixed-parameter exponents and baseline

Put \(s=\log(en)\) only in this paragraph. The assumed counts are

\[
J=O(s^{3/2}),\quad K=O(s),\quad
N_x,H_{\rm sph}=O_d(s^{3(d-1)/2}),\quad
N,R,r=O_d(s^{3d/2+1}),\quad p+1,N_t=O(s^{5/2}).
\]

For fixed \(L,m,d\), the dense cached-jet term has exponent
\(3/2+1+3(d-1)/2=3d/2+1\). Image formation and full-basis assembly have
the same or a smaller dense exponent. With \(q\le n\), the retained metric
term \(q^2r\) also fits \(n^2s^{3d/2+1}\).

The largest explicitly displayed term linear in \(n\) is the conservative
selector \(nr^3=O_d(ns^{9d/2+3})\). Both projection orders, lower-rank
contractions, and quadratic/cubic activation composition fit this second
term. Scalar moments, geometry and sorting are fixed powers of \(s\).
This verifies the candidate's explicit work bound, including \(d=1\), where
the dense exponent is \(5/2\) and selector exponent \(15/2\).

The stated memory formula follows from the live-jet, coefficient, geometry,
and selected-array bounds. Polynomial activation workspace and the supplied
certification workspace remain explicit. No source complexity growing
polynomially in \(n\) is hidden under a polylogarithm.

Dividing the work bound by \(mPT/h\), with fixed problem parameters and
\(T=\Theta(\log n)\), gives the three terms in the displayed Euler ratio.
For \(h=n^{-1/2}\), all tend to zero. The note correctly distinguishes this
specified benchmark from a claim that Euler requires that step, or that the
step attains a stated accuracy. It also correctly states that using the same
high-order backend for dense training avoids the passive-query/selection
overhead, so the argument does not beat every optimized dense solver.

## 6. Integration limits and final verdict

No required correction was found in the frozen conditional assembly argument.
The assumed local source accuracy and panel/degree bounds remain a separate
backend obligation, as stated in the candidate. Activation derivative
generation, certification, sampling, and finite precision retain their
displayed qualifications.

One integration constraint matters: this assembly implementation consumes
dense-ODE Taylor jets. Real-node Picard output is a polynomial approximant,
not automatically the same Taylor jet. Thus the Picard route cannot inherit
the assembly's sharper Taylor work exponent merely because both use
\(O(\log n)\) degrees. Its separately proved nodal-evaluation/streaming
envelope remains valid; an adapter or another cost argument would be needed
to transfer this candidate's factorized-jet bound. This is not a flaw in the
assembly candidate's explicitly conditional statement.

Check method: complete mathematical reading, direct reconstruction of the
finite coefficient identities and errors, symbolic endpoint regrouping,
term-by-term operation/memory accounting, dimension-one and \(K=1\) checks,
and fixed-parameter exponent comparison. No numerical evidence is claimed.

