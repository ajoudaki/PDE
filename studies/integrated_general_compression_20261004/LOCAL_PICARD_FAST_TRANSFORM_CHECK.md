# Check of the fast Picard integration-transform refinement

2026-10-06. Verdict: PASS for the exact-arithmetic transform identities,
preservation of the Picard iteration, revised operation/memory envelopes, and
fixed-parameter exponents. No required mathematical correction was found.
This is an internal cross-route check, not an isolated promotion review.

## Scope and provenance

The complete frozen LOCAL_PICARD_FAST_TRANSFORM.md was read, all 226 lines,
at SHA-256
769968780b90cf5593fda70683bb577411952faacf9d2c86297fdd4574a092cb.
It was checked against the complete original Picard construction,
LOCAL_CONTINUATION_ALTERNATIVE.md, SHA-256
a41c246981d22abe002a5870934690ac254e2f427984661bfef048650f1a9e34,
which this reviewer authored, and the previously read complete quadrature
route and relevant source/count/cost sections of RESULT.md.
The original source event and Picard correctness theorem are imported here.
No other candidate, study, history, or archived book was used.

Accessible rigorous-math/conjecture instructions, the shared process, and the
book notation contract were applied. The canonical-notation skill remains
unavailable under the previously reported filesystem permission restriction.
No numerical test or implementation was executed for this report; the
supervisor's separate deterministic transform check is not evidence used here.

## 1. Degree rounding and unchanged Picard proof

For the sufficient degree \(K_0\ge4\), the chosen power of two
\(Q=2^{\lceil\log_2(K_0+1)\rceil}\) and \(K=Q-1\) satisfy

\[
K_0\le K,\qquad K+1<2(K_0+1).
\]

The ratio of successive degree factors is

\[
\frac{(2K+4)2^{-(K+1)}}{(2K+2)2^{-K}}
 =\frac{K+2}{2(K+1)}<1
\]

for \(K\ge1\). The original sufficient tail inequality remains true.
Recomputing the prescribed iteration count with the new degree accounts for
the increased interpolation factor. The original panel size depends on its
source/derivative bounds, not on the degree, because its integrated
interpolation norm is degree independent. Hence panel, degree and iteration
orders remain as stated.

The new local \(Q\) denotes a transform length. It must not be substituted
for the unrelated bound named \(Q\) in the original Picard proof; the
refinement expressly distinguishes the meanings.

## 2. Analysis-transform identity

The assigned indices \(2j+1\), \(0\le j<Q\), are the odd integers between
one and \(2Q-1\). Their mirrors \(4Q-(2j+1)\) are the odd integers between
\(2Q+1\) and \(4Q-1\). Thus all assignments are distinct; no value is
overwritten or double-counted.

Pairing the two assigned terms in the length-\(4Q\) Fourier sum gives

\[
v_j\left(e^{-2\pi ik(2j+1)/(4Q)}
          +e^{2\pi ik(2j+1)/(4Q)}\right)
 =2v_j\cos(k\theta_j),
\qquad \theta_j=\frac{(2j+1)\pi}{2Q}.
\]

Therefore
\(\widehat y_k=2\sum_jv_j\cos(k\theta_j)\). The proposed recovery

\[
a_0=\widehat y_0/(2Q),\qquad a_k=\widehat y_k/Q\quad(1\le k<Q)
\]

has exactly the constant and nonconstant normalizations required by
Gauss--Chebyshev interpolation. It agrees with the original dense discrete
cosine transform component by component.

Splitting Fourier input indices into even and odd terms proves the two
butterfly formulas directly. Since \(4Q\) is a power of two, repeated
splitting reaches length one after \(\log_2(4Q)\) levels.
Each level requires \(O(Q)\) real arithmetic; complex multiplication is a
fixed number of real operations. The resulting work is \(O(Q\log Q)\).
Depth-first recursion with reusable buffers has a geometric sum of live
array sizes and hence \(O(Q)\) scratch. Twiddle factors for all levels
need only \(O(Q)\) storage and scalar trigonometric evaluations, generated
once. This argument does not import an external FFT complexity theorem.

## 3. Integration, synthesis, and the top-degree term

The primitive identities are valid modulo constants. In particular
\(T_2/4=x^2/2-1/4\) has derivative \(T_1=x\); its missing constant is
properly restored by the prescribed value at \(x=-1\).
For \(k\ge2\), differentiate the stated combination of \(T_{k+1}\) and
\(T_{k-1}\), or use the cosine definition and angle addition, to obtain
\(T_k\). Each coefficient contributes to at most two primitive coefficients,
so primitive formation costs \(O(Q)\). Evaluating its value at \(-1\)
and correcting the constant also costs \(O(Q)\).

For synthesis, the symmetric coefficients
\(c_0=b_0\), \(c_k=c_{4Q-k}=b_k/2\) give the unnormalized inverse sum

\[
\sum_{\ell=0}^{4Q-1}c_\ell e^{2\pi i\ell(2j+1)/(4Q)}
 =b_0+\sum_{k=1}^{Q-1}b_k\cos(k\theta_j).
\]

The qualifier “unnormalized” matters: an implementation returning the usual
inverse transform divided by \(4Q\) must multiply its output by \(4Q\),
or omit that normalization. The note specifies the correct unnormalized sum.
Either execution adds at most linear work.

Integration of a degree-\(Q-1\) interpolant produces a degree-\(Q\)
polynomial. Its highest term vanishes at every iteration node:

\[
T_Q(x_j)=\cos((2j+1)\pi/2)=0.
\]

It is therefore correct to omit that coefficient only during synthesis of the
nodal values supplied to the next vector-field evaluation. The candidate
retains it in the actual polynomial, in the integration constant, at the next
panel endpoint, and at arbitrary source-query times. This retention is
essential. In particular, the constant that enforces the left anchor must be
computed from the full primitive before exploiting the top term's nodal zero.

The stated implementation does exactly that. It thus computes the same
finite Picard integral map as the original direct transform, including the
full continuous path used in the defect proof. Endpoint evaluation uses
\(T_k(1)=1\); arbitrary interior evaluation follows the three-term
Chebyshev recurrence in \(O(Q)\) per parameter coordinate.
No monomial conversion is needed.

All transforms implement real linear maps. Their complex intermediate
arithmetic does not introduce complex activation evaluations. In exact
arithmetic the node values passed to the network remain real; numerical
roundoff is outside the stated model.

## 4. Complete cost and memory

Per Picard iteration, the dense vector-field evaluations still cost
\(O(PmK)\), and analysis/integration/synthesis now cost
\(O(PK\log(2+K))\). The direct \(PK^2\) transform and \(K^3\)
preprocessing terms are legitimately removed. Their replacements include
twiddle generation, allocation, scalar primitive construction and scaling.
No matrix factorization is hidden.

The source phase still charges:

- \(PN_tK\) for evaluation of the stored panel polynomials;
- \(PN_tN_x\) for all passive queries and initialized-matrix images;
- \(LnN_x(p+1)(N_t+H_{\rm harm})\) for the temporal/spatial coefficients;
- \(LnR_{\rm src}r+Lnr^3+Ln^2r+Lq^2r\) for orthogonalization,
  selection, full-basis initialized actions and retained assembly;
- the explicit quadrature/basis geometry terms.

Exact initial training features can require one additional training pass.
Its \(O(mP)\) arithmetic is absorbed by the displayed Picard term, while
its scalar activations are included explicitly in the additional \(m\) term
of the call count.

No dense integration matrix is stored. Streaming parameter coordinates through
one transform buffer while retaining the nodal and polynomial arrays costs
\(O(PK)\) words. The candidate also retains all required training activations,
source accumulators, source coefficients, selected arrays and geometric
workspace in the peak bound. The former \(K^2\) matrix-storage term is
unnecessary under this algorithm.

Activation value/first-derivative calls are separately counted, as are
Gaussian draws. No computational bound for an arbitrary analytic activation
description follows from regularity. Coefficient magnitude and conditioning
do not create additional operations in this exact-real model, but no
finite-precision or bit-cost conclusion is licensed.

## 5. Width exponents and economic qualification

Write \(s=\log(en)\) for this calculation. At fixed admissible parameters,

\[
N_{\rm pan}=O(s^{3/2}),\quad I,K=O(s),\quad
N_t,p+1=O(s^{5/2}),\quad
N_x,H_{\rm harm}=O_d(s^{3(d-1)/2}),
\]
\[
R_{\rm src},r=O_d(s^{3d/2+1}).
\]

The dense reconstruction term has order

\[
P\,s^{7/2}(m+\log s).
\]

The arbitrary-time polynomial evaluations cost \(Ps^{7/2}\), which fit the
same term. Passive sources and initialized images cost
\(Ps^{5/2+3(d-1)/2}=Ps^{3d/2+1}\).
The complete-basis assembly term has this same dense exponent. The conservative
selector contributes \(Ln\,s^{9d/2+3}\), which also dominates the other terms
linear in \(n\). Remaining geometric and polylogarithmic selected-model terms
are fixed powers of \(s\). These computations verify the note's unsimplified
bound.

For \(d\ge2\), \(3d/2+1\ge4\), and
\(s^{7/2}\log s=O(s^{3d/2+1})\). Moreover

\[
\frac{n\,s^{9d/2+3}}{n^2s^{3d/2+1}}
 =\frac{s^{3d+2}}n\longrightarrow0
\]

for every fixed \(d\). Thus the full arithmetic simplifies to the claimed
\(O(n^2s^{3d/2+1})\). For \(d=1\), the valid dominant bound is
\(O(n^2s^{7/2}\log s)\). These conclusions explicitly use fixed dimension.

The peak source accumulators and coefficients have order
\(n\,s^{3d/2+1}\), the dense polynomial arrays have order \(n^2s\),
and the remaining selected/geometric arrays are polylogarithmic or smaller.
Hence the common peak bound \(O(n^2\log(en))\) is valid eventually at each
fixed \(d\), with polylogarithmic selected width.

Dividing by the stated dense Euler benchmark \(mPT/h\), with
\(T=\Theta(\log n)\), gives
\(O(h\log(en)^{3d/2})\) for fixed \(d\ge2\), and the claimed
\(O(h\log(en)^{5/2}\log\log(e^e n))\) for \(d=1\).
Every fixed inverse-polynomial step makes the ratio tend to zero.

A presentation qualification when including fresh initialization: the ratio
bound includes sampling costs only under the inherited bounded-cost sampling
model, or when the supplied reference initialization makes generation
unnecessary. An arbitrarily expensive external Gaussian-generation routine
cannot be absorbed merely by assuming bounded activation-call cost. The note
already charges actual sampling costs separately; this is an interpretation
of its arithmetic contract, not an algebraic defect.

The candidate correctly avoids claiming that Euler requires the benchmark step
or that source setup is cheaper than dense training with the same high-order
integrator.

## Final assessment

The finite identities, full-path preservation, work and memory accounting,
and exponent simplifications all pass this check. The original Picard
correctness/accuracy result remains a dependency. The refinement needs no
new activation oracle and no new scientific assumption beyond the previously
stated exact-arithmetic and fixed-parameter qualifications.

Check method: complete mathematical reading; derivation of both Fourier
normalizations, index disjointness, primitive identities, top-degree handling
and radix-two recurrence; term-by-term work/memory reconstruction; dimension-one
and minimum-degree boundary inspection; and explicit asymptotic division.
No empirical or floating-point validation is claimed.

