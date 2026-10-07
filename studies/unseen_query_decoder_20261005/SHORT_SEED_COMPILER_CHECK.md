# Cross-check of the short-seed row compiler and its explicit exponents

2026-10-06. Scoped author cross-check, not an isolated promotion review.
The complete `SHORT_SEED_PRIOR_BLOCKS.md` and
`EXPLICIT_COMPILER_EXPONENT.md` were read. Relevant observed-Gram,
posterior-entropy, block-estimation, and guarded-context passages of
`RECALIBRATION_FREE_MOMENTS.md` were read to check their interface. Its
subsequently added Section 10 was also read completely and checked against
the explicit ridge reconstruction below. The previously read permitted
source, matrix, and acquisition notes were reused.
The original Nisan block-generator definitions and theorem were checked
against the linked paper. Other studies, experiments, code, and Git were
not used. The initialization note is frozen and unchanged. The inaccessible
custom notation skill has the same recorded fallback as that note.

**Finding.** The generator access pattern, persistent-state bound, matrix
bit arithmetic, and final additions of exponents are sound in the stated
activation-primitive model. The two assigned notes originally left one
interface insufficiently numerical: whitening uses an artificial ridge
\(\tau\), whereas the compiler's explicit amplitude table only mentioned
the matrix noise \(\sigma\). Section 2 below supplies that missing
extension with an explicit ridge and guards. With that extension and the
finite implementation conventions recorded here, the claimed

\[
 Cn\log^{2052}(en)\quad\hbox{work},\qquad
 C\log^{722}(en)\quad\hbox{retained plus peak query space}
                                                               \tag{1}
\]

do follow. This check does not re-prove the dense-trajectory/statistical
bridge, and does not turn primitive-model bounds into unconditional bounds
for arbitrary activation evaluators.

## 1. Reconstructing the compiler rather than assuming a polynomial

Put \(\ell=\log(en)\), and use the compiler's source bounds

\[
 R\le C\ell^8,
 \quad P\le CR^2,
 \quad N\le CR^7,
 \quad r\le CR^2,
 \quad \log X=O(\ell^2).                                \tag{2}
\]

Here \(R\) bounds named physical fields and initialized-matrix calls,
\(P\) counts empirical summaries, \(N\) counts row/scalar instructions
and matrix macros, and \(r\) is the largest materialized matrix dimension.
The \(R^7\) bound is obtained by \(O(R)\) conditioning calls, each using
at most \(O(R^6)\) padded dense-matrix scalar instructions. Physical
displacement norms cost \(O(R^2)\) per evaluation, for \(O(R^3)\)
instructions overall, and fit underneath it. The low-rank lists append
committed gradients; they do not expand the Picard nesting into a tree.

For a matrix macro, let

\[
 h_0=2+r+p+b_0+\log_2 M+\log_2(1/a),                    \tag{3}
\]

where \(p\) is its input fractional precision, \(2^{-b_0}\) its
requested error, \(M\) its norm bound and \(a\) its positive spectral
floor where one is needed. The following are bit bounds, excluding only
the named external activation/data precision primitives.

| Operation | Reconstruction | Time | Peak scratch |
| --- | --- | --- | --- |
| Exact rational inverse followed by rounding | Cleared integer entries have \(O(h_0)\) bits; minors and reduced Schur entries have \(O(h_0^2)\) bits; all cofactors take \(O(r^5)\) rational operations, each at most cubic in bit length | \(O(h_0^{11})\) | \(O(h_0^4)\) bits |
| Rounded positive root | \(O(h_0)\) Newton steps, each with an \(O(h_0^2)\)-bit iterate grid; inverse minors have \(O(h_0^3)\) bits | \(O(h_0^{15})\) | \(O(h_0^5)\) bits |
| Positive part | Apply that root to \(A^2+v^2I\), with \(v\asymp 2^{-b_0}/r\); the new logarithmic inverse gap is \(O(h_0)\) | \(O(h_0^{15})\) | \(O(h_0^5)\) bits |
| PSD radial cap / Sylvester solve | Scalar root and conservative dyadic scaling / inversion of the already-counted Kronecker matrix | Within the same bounds | Within the same bounds |

The inverse operation count uses elimination, not factorial determinant
enumeration. The determinant expansion only bounds integer lengths. In
the root iteration, multiply an inverse using its common adjugate
denominator; otherwise an unnecessary product of entrywise denominators
would spoil the displayed intermediate-bit argument. Return the root on
the requested ordinary output grid: its private \(O(h_0^2)\) precision
must not become the next macro's requested input precision.

The PSD interface also needs its stated discipline. Produce the positive
part with its positive buffer and use a nonnegative dyadic radial factor.
An unprotected entrywise rounding after that operation can destroy PSD and
is not permitted. Inputs to each such fixed macro composition come from
the ordinary operand grid; its returned grid has a fixed multiple of that
precision. There is no chain of unrestricted rational outputs or growing
precision requests. The displayed source schedule meets this condition:
Gram tables are fresh scalar-grid inputs, and consecutive PSD/radial
operations form a fixed-size composition.

On bounded operands with noise floors, one instruction has Lipschitz
constant \(X^{C_0}\) for an absolute fixed \(C_0\). Consequently local
precision

\[
 w=b+CN\log_2X+C\log_2(N+2)                             \tag{4}
\]

suffices for final error \(2^{-b}\). With
\(\mathcal H=2+b+CR^7\log_2X\), every macro has
\(h_0=O(\mathcal H)\), and there are at most \(O(\mathcal H)\)
instructions/macros. This proves time \(O(\mathcal H^{16})\).
Caching the shared graph, even with padded matrices, costs
\(O(Nr^2w)=O(\mathcal H^4)\) bits; one matrix scratch area costs
\(O(\mathcal H^5)\). The claimed \(O(\mathcal H^6)\) space is
therefore conservative.

In particular, at \(b=C\ell^{120}\), the row bounds are
\(C\ell^{1920}\) and \(C\ell^{720}\). There is room for ordinary
instruction addressing: before replacing \(N\) by \(\mathcal H\),
the macro sum is at most \(C\ell^{56+1800}=C\ell^{1856}\).
Logarithmic indexing overhead does not consume the slack up to 1920.

## 2. The missing whitening interface, with explicit constants

This extension is necessary. The sentence
\(\log(1/\tau)=\operatorname{polylog}(n)\), by itself, does not imply
the particular degrees 58, 74, 100 or 120. Nor can one retain the literal
source cap \(X^{100}\) for arbitrarily whitened marks. The following
choice establishes those degrees without an unspecified polynomial.

Replace the compiler's \(X\) by a dyadic upper bound
\(\bar X\in[X,2X]\), increasing fixed constants if needed. Then
\(\bar X\ge n,R,\sigma^{-1},2\) and
\(\log\bar X=O(\ell^2)\). Scalar raw history marks and constituent
conditioning-coefficient entries are bounded by \(\bar X^{100}\).
Concatenating histories and adding at most \(CR\) contributions gives
raw mean-coefficient entries at most \(\bar X^{101}\), in dimension
at most \(CR\le\bar X\) after enlarging constants. Generic macro
dimensions are allowed the larger bound \(\bar X^2\). Thus, for the
raw mean coefficient matrix \(A_0\) and any relevant raw history moment,

\[
 \|A_0\|\le\bar X^{102},
 \qquad q:=\max\{\|Q_{S,0}\|,\|Q_{T,0}\|\}
                   \le\bar X^{202}.                    \tag{5}
\]

These intentionally coarse bounds also cover a larger master history than
the physical query subset. No fixed \(O(R)\) Gram bound is silently
required for this step. Take the explicit dyadic ridge

\[
 \tau=\bar X^{-512}.                                    \tag{6}
\]

The observed-Gram argument gives perturbation distance \(D\le3\tau\)
after a small numerical allowance. Its displayed mean-operator estimate
then yields

\[
 2\|A_0\|\sqrt{D(q+D)}
    \le C\bar X^{102+101-256}
    =C\bar X^{-53}.                                    \tag{7}
\]

Every fixed-depth propagation factor used there is a fixed constant times
a fixed power of \(B=C\ell^{3/2}\). At sufficiently large width it is
at most \(\bar X\), regardless of the fixed depth. Its exponent does
not become a power of \(n\). Thus (7) after propagation is at most
\(C\bar X^{-52}\), smaller than \(n^{-10}\) eventually. Similarly,
the variance error \((D/\sigma^2)c_{\rm in}\), even allowing
\(c_{\rm in}\le\bar X^{200}\), is at most
\(C\bar X^{-310}\), and at most \(C\bar X^{-309}\) after the same
propagation. An accuracy order different from ten can use a larger fixed
exponent in (6); it is unnecessary for the current root-width error target.

The matrices actually used are

\[
 Q_S^*=Q_{S,\mathrm{obs}}+2\tau I,
 \quad U_S=(Q_S^*)^{-1/2}S,
 \quad A=(Q_T^*)^{1/2}A_0(Q_S^*)^{1/2},
                                                               \tag{8}
\]

and, with \(J\) the selector of the forward-query columns,

\[
 P_{\rm var}=(\sigma^2I+JQ_S^*J^T)^{-1/2}J(Q_S^*)^{1/2}.
                                                               \tag{9}
\]

An inverse square root is an inverse and a positive root in succession.
These add no new matrix primitive, and their dimensions are at most
\(O(R)\). All history marks use the same cached training DAG. The
additional arrays, products and operations over all relevant field
collections fit in \(O(R^7)\), including an intentionally redundant
\(O(R^2)\) list of collections with \(O(R^3)\) dense products per
collection. The principal-block relation in (9) gives
\(P_{\rm var}P_{\rm var}^T\preceq I\), directly by conjugating
\(JQ_S^*J^T\preceq\sigma^2I+JQ_S^*J^T\).

Since the source mark vector has Euclidean norm at most
\(\bar X^{101}\), its whitened version has norm at most
\(C\bar X^{357}\). The mean coefficient in (8) is bounded by
\(C\bar X^{304}\) even without its much better physical bound. A
guarded query-moment vector has norm at most \(B\le\bar X^{100}\).
Consequently even an untruncated scalar mean term is bounded by a fixed
power such as \(C\bar X^{800}\). A fixed enlarged operand cap, for
example \(\bar X^{4096}\), suffices for these extra products and sums.
The inverse and root sensitivities use floors at least \(\tau\) or
\(\sigma^2\), so their logarithms remain \(O(\log\bar X)\).
Increasing the fixed cap exponent changes constants, not logarithmic
degrees. In particular the augmented row and full-summary sensitivities are

\[
 \log\Lambda_{\rm query}\le CR^7\log\bar X=O(\ell^{58}),
 \qquad
 \log\operatorname{Lip}(\text{full capped summary recursion})
       \le CR^9\log\bar X=O(\ell^{74}).                 \tag{10}
\]

At a zero-variance square root the corresponding assertion is a
one-half-Hölder modulus in that variance coordinate. The actual guard
\(\sigma^2+\max(0,v)\) supplies a positive floor and makes it Lipschitz
with the same type of logarithmic bound.

### Guards and precision at the new ridge

Use symmetric dyadic observed Grams. A convenient globally defined
extension is

\[
 Q_{S,\rm safe}^*=\tau I+(Q_{S,\mathrm{obs}}+\tau I)_+.
                                                               \tag{11a}
\]

It has floor \(\tau\) everywhere and equals (8) on the good event,
because there \(Q_{S,\mathrm{obs}}+\tau I\succeq3\tau I/4\).
Cap the positive part radially at a fixed radius such as
\(\bar X^{203}\) before adding the final ridge if a global norm bound
is needed. This is also the identity on the good domain. It preserves
the Lipschitz argument instead of extending a discontinuous default branch
across a spectral boundary. The slightly larger global root norm changes
the coarse bound on \(A\) from \(C\bar X^{304}\) to at most
\(C\bar X^{306}\), still inside the displayed scalar cap.

An optional final guard may certify the symmetric numerical matrix minus
\(\tau I/2\) is positive definite and meets its magnitude cap;
otherwise return the default. Positivity can be decided by exact
rational symmetric elimination: recursively test a positive pivot and its
Schur complement. The decomposition
\(\left(\begin{smallmatrix}a&b^T\\b&C\end{smallmatrix}\right)
\succ0\) iff \(a>0\) and \(C-bb^T/a\succ0\) proves this criterion.
The matrix arithmetic is already covered by Section 1. Frobenius bounds
are comparisons of exact rational sums of squares. These guards need no
test of an inaccessible real eigenvalue.

On the companion's good event, the exact buffered Gram has floor
\(7\tau/4\); allowing operator error \(\tau/4\) still leaves floor
\(3\tau/2\), so the guard never rejects a good input. Allocate internal
errors well below \(\tau/(Cr)\) entrywise, then below the requested
final error divided by the augmented circuit sensitivity. The required
precision is \(b+CR^7\log\bar X\), as in (4).

For completeness the scalar noise and acquisition tolerances can be fixed
without circular choices. Let \(T_\rho=\sqrt{P/(\beta\rho)}\), using
the companion's fixed failure shares \(\beta,\rho>0\), and let
\(L_{\rm pair}\) be the row-pair Lipschitz bound in (10). Choose dyadic
\(\eta\) and a history tolerance satisfying

\[
 \eta\le\min\left\{
 \frac{\tau}{16R T_\rho},
 \frac{n^{-12}}{nP(1+\Lambda_{\rm query})^{P+1}}
 \right\},
 \quad
 \varepsilon_{\rm hist}\le
 \frac{\tau}{16R(1+L_{\rm pair})}.                      \tag{11}
\]

Decrease the second tolerance further to meet the same physical output
budget; this adds at most \(CR^9\log\bar X\) precision bits. Choosing
each dyadic within a factor of two of its sufficient upper bound gives
\(\log(1/\eta)=O(\ell^{74})\). History fractional precision
\(C\ell^{100}\) and internal precision \(C\ell^{120}\) more than
suffice, with constants chosen for the displayed margins. In particular
\(Re_G\le\tau/8\), leaving room for the numerical allowance above.

Thus the whitening extension has exactly the row interface the seed note
needs: \(\mathcal H=2+b+C\ell^{58}\), row time
\(C\mathcal H^{16}\), row space \(C\mathcal H^6\), and full-context
logarithmic sensitivity at most \(C\ell^{74}\). The literal original
cap \(X^{100}\) should not be quoted for this augmented circuit.

## 3. The randomness theorem matches this access pattern

The form checked in the primary source is the following. For an absolute
\(c>0\), Nisan's depth-\(j\) generator with \(m\)-bit blocks fools
every finite-state machine with at most \(2^{cm}\) states to error
\(2^{-cm}\), provided \(j\le cm\). It outputs \(2^j\) blocks,
using an \(m\)-bit root and \(j\) affine universal hashes with linear
descriptions. The state bound is imposed between blocks; each block's
transition function may be arbitrary. This is Definition 1 and Lemma 3,
not an assumption about repeatedly reading a random tape. [Nisan,
Sections 2--4](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).

For one fixed source and context, the test starts with a fixed finite
description of its coefficients, consumes one whole random block per
Gaussian row, evaluates that row, updates its mean accumulator, and clears
its row-local scratch. Its boundary state consists of the accumulated
block means, current sum, context, coefficients and counters. The large
within-row matrix scratch therefore does not determine the generator's
finite-state parameter. It still counts in the actual algorithm's peak
workspace. The proof test's moment threshold may be hardwired after
fixing the context; no threshold oracle is added to the decoder.

Restarting the stored seed for another context defines another one-pass
test. Accuracy for all such tests follows by a finite union bound. One
must not condition on the seed-dependent query context and apply only a
single-context guarantee; the context union below is indispensable.

For random-access row generation, follow the recursion's left/right path
to the desired leaf. A right branch applies the stored hash at that depth,
and a left branch leaves the current \(m\)-bit string unchanged. At most
\(j\) hashes are evaluated. An affine Toeplitz hash is a binary
convolution plus a binary translation, so schoolbook evaluation costs
\(O(m^2)\) bit operations with \(O(m)\) temporary bits. A row therefore
costs \(O(m^2j)\) operations and does not require storing earlier rows.
Only the seed and the current root-to-leaf value are retained.

## 4. Finite contexts and finite Gaussians

Condition on the complete source and its actual numerical prefixes, before
drawing the decoder seed. The ideal posterior reference laws and all
prefix coefficients are then fixed. At most \(C\ell^{16}\) varying
context coordinates are needed, with range logarithms at most
\(C\ell^{74}\). Encoding them with \(C\ell^{100}\) fractional bits
gives a finite family with

\[
 \log N_{\rm ctx}\le C\ell^{116}.                      \tag{12}
\]

Including the finite prefix/call indices only changes the constant. Fixed
source coefficients are not unioned over all possible training sources:
the probability bound is conditional and uniform in every source meeting
the interfaces. Guarded intermediate query moments are included, so actual
seed-dependent contexts belong to this same family.

The mesh error is deterministic. Applying (10), or its one-half-Hölder
version, bounds the exact moment change by
\(\exp(C\ell^{74}-c\ell^{100})\). It is not a probability multiplied
by \(N_{\rm ctx}\). No continuity of a rounded median or a rounded
branch decision is asserted or needed. A rounded sphere input can be
slightly off the sphere; the capped row circuit is defined there, and its
moment modulus transfers the result back to the actual sphere input.

For each context, let \(h_+=\max(h,1/n)\), and take block size
\(s\asymp1/h_+\), with \(s h\le1/128\) and \(s\le n\).
For a literal finite implementation, use a computable dyadic upper bound
\(h_+\le\widehat h\le2h_+\) and set
\(s=\lfloor1/(128\widehat h)\rfloor\). This avoids an exact floor
decision involving a transcendental entropy-bound expression and changes
only the constant in the block accuracy. At sufficiently large width,
the integer part still gives the stated comparison. The deterministic
entropy bound supplies such an upper approximation; an unknown realized
posterior entropy must not be used to choose \(s\). In fact (11) gives
\(\log(1/\eta)=O(\ell^{74})\), so the companion's information bound
\(H=(P/2)\log(1+B_F^2/\eta^2)\) is \(O(\ell^{90})\). Its
deterministic \(h=H/(\alpha n)\) therefore tends to zero, as required
for a nonempty statistical block at sufficiently large width.

The companion's verified elementary calculation is: under the product
reference \(\nu^{\otimes s}\), coordinate Chebyshev failure at threshold
\(4B/\sqrt s\) is at most \(1/16\). The block relative entropy is
at most \(1/128\), so total variation costs at most another \(1/16\).
Independent prior blocks consequently fail with probability at most
\(1/8\) each. The median over odd \(J\) blocks has coordinate failure
at most \(2^{-J/2}\). Union over coordinates gives vector error
\(CB\sqrt{Rh_+}\). This calculation genuinely requires iid rows inside
each reference experiment; pairwise independence does not establish it.

Take \(J=C\ell^{116}\), rounded up to an odd integer, with the constant
covering (12) and the assigned confidence. Couple finite prior Gaussians
to exact prior Gaussians using clipped quantiles at
\(T^2=C\ell^{120}\). The inverse-CDF Lipschitz bound on that interval
is \(\sqrt{2\pi}e^{T^2/2}\). Uniform-cell and quantile precisions with
larger constants in the same degree 120 make the coupled row error
negligible after the row modulus (10). The tail bound per context is

\[
 2JsD e^{-T^2/2}
 \le\exp(-c\ell^{120}),\qquad D\le C\ell^8,            \tag{13}
\]

eventually. This can be summed over (12). Unlike the deterministic mesh
error, this failure probability must be included in that union.

The Gaussian quantile evaluation fits well inside the row allowance:
its CDF Taylor polynomial on the bounded interval and bisection need a
polynomial number of operations in \(T^2\) and precision. For example,
write \(v=\Theta(\ell^{120})\). A Taylor degree \(O(v)\),
\(O(v)\) bisection steps and \(O(v^2)\)-bit rational intermediates
give the coarse bounds \(O(v^8)\) time and \(O(v^3)\) space per
coordinate, below the row bounds after multiplying by \(D\). Resetting
the numerical integration to a common grid is another admissible
implementation. A stored Gaussian lookup table is unnecessary.

## 5. State, seed, work, and the final exponent sum

All entries below include integer parts: augmented row magnitudes have
logarithm \(O(\ell^2)\), far below the fractional degree 120. An exact
dyadic sum of at most \(n\) terms only adds \(O(\log n)\) bits.

| Resource | Bound | Reason |
| --- | --- | --- |
| Gaussian bits for one row | \(C\ell^{128}\) | \(D\le C\ell^8\) coordinates, each with \(C\ell^{120}\) bits |
| Completed statistical block means | \(C\ell^{244}\) bits | \(J\le C\ell^{116}\), \(R\le C\ell^8\), \(C\ell^{120}\) bits per mean coordinate |
| Remaining boundary state | At most \(C\ell^{244}\) bits | Context, prefix, fixed matrices, current sum, instruction description and counters |
| Generator block length \(m\) | \(C\ell^{244}\) | Covers boundary state, row bits, depth and logarithmic fooling accuracy |
| Number of row blocks per integral | At most \(Cn\ell^{116}\) | \(Js\), with \(s\le n\) |
| Generator depth \(j\) | \(C\ell\) | Next power-of-two padding of \(Js\) |
| Stored seed | \(C\ell^{245}\) bits | Root plus \(O(j)\) linear-size hash descriptions |
| Generated row cost | \(C\ell^{489}\) | \(m^2j\) |
| All generator work | \(Cn\ell^{621}\) | \(489+116+16\) |
| All row-interpreter work | \(Cn\ell^{2052}\) | \(1920+116+16\) |

For the boundary-state row, a padded cache of all graph outputs would cost
only \(C\ell^{56+32+120}=C\ell^{208}\) bits; it can be cleared
between rows in any case. The ordinary stored program description at
precision 120 costs \(C\ell^{176}\) bits. Even the exact rational
selection weights of the initialization note fit below degree 244:
there are \(O(\ell^{16})\) weights of at most
\(O(\ell^{136})\) bits each. Thus using exact weights does not invalidate
the simpler quantized-panel resource bound assumed by the seed note.

Choose the block-length constant so the theorem gives
\(S\le cm\), \(j\le cm\), and per-test fooling error
\(2^{-cm}\). This error is much smaller than
\(\delta/N_{\rm ctx}\), since \(244>116\). Discard unused bits
within a generator block. Pad the final row count to the next power of two
with dummy transitions; this costs at most a factor two. No dense history
or long random tape is stored.

The row interpreter has \(C\ell^{720}\) peak scratch. Adding the
\(C\ell^{245}\)-bit generator seed, \(C\ell^{244}\)-bit block storage,
the current generated block, program/panel state and counters still costs
\(C\ell^{720}\) before the conservative bookkeeping allowance. Thus
the claimed \(C\ell^{722}\) upper bound holds. Clearing the large
scratch costs at most its size per row, already below the row-work bound.
Sorting block means can even use quadratic insertion sorting:
\(J^2R\) comparisons of \(O(\ell^{120})\)-bit values cost
\(C\ell^{360}\) per integral, also below (1).

Apply the generator to every fixed-context Boolean failure test with a
finite target threshold and separated error margins. Add its fooling
failure to the truly random finite-row median and coupling failures, then
sum over (12). One seed succeeds for all contexts and prefixes with the
assigned conditional probability. The same seed can therefore be reused
for adaptive late queries. No statistical independence of different calls
under that reused seed is claimed.

## 6. Qualifications that must remain in the assembly

The original two-note interface required the explicit whitening extension
in Section 2; quoting the unspecified ridge polylogarithm would not have
certified the numbered exponents. Likewise, retaining the old literal
\(X^{100}\) cap for whitened marks would be incorrect. The larger fixed
cap and unchanged logarithmic degrees resolve that issue here.

The resource claim is in the stipulated activation/data-primitive model.
If a primitive takes \(T_{\rm prim}(w)\) time or
\(S_{\rm prim}(w)\) space at precision \(w\), include its actual costs
at \(w=C\ell^{120}\), multiplied by the counted number of calls for
time. Merely knowing an arbitrary polynomial degree does not justify the
universal number 722. Analyticity alone supplies no numerical evaluator.

This check addresses the compiler/randomness interface, not independent
validity of the posterior neural comparison or the entire dense theorem.
Subject to that supplied statistical interface, it establishes the explicit
work and memory counts, including their probability union and new ridge.
Since \(\log^{2052}(en)/n\to0\), (1) is eventually below a dense
quadratic budget; no practical crossover or uniform small-width claim follows.
