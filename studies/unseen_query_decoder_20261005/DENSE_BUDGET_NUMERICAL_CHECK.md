# Independent numerical and compilation audit

2026-10-06. **Scoped PASS.** This verdict covers the finite compilation,
cached Gram acquisition, compiled-law change of reference, finite-seed
covariance-norm cubature, and resource accounting needed by Sections 3 and 7
of `DENSE_BUDGET_DECODER_CANDIDATE.md`. It is conditional on the statistical
and physical interfaces supplied in the neutral assignment and stated in
the frozen candidate. It does not certify their proofs or the complete
physical-decoder theorem.

The reconstruction below closes the possible extra term in collective
relative entropy caused by the compiler's multiplier bound, and explains
how to acquire the cached Grams without a normalizer or integration oracle.
No decisive defect was found in the scoped claims. Preprocessing time is
unrestricted; primitive query time and bit time are distinct claims.

## 1. Scope and frozen inputs

The complete scientific inputs were exactly the following five files,
all in `studies/unseen_query_decoder_20261005/`:

| Input | SHA-256 |
|---|---|
| `DENSE_BUDGET_TILT_COMPILATION.md` | `e66ec00d90f58d75e329cca97b4fa59123d52607563125543ec93999417face3` |
| `DENSE_BUDGET_ROBUST_CUBATURE.md` | `a9dc2b37d41c78387c8d479a2a630916d25534b5ccb77f6d5227c88ed00a518e` |
| `DENSE_BUDGET_DECODER_CANDIDATE.md` | `e34fbff0633d020010256a72beaf313c216afe789f51720f3c6df525c93bffdc` |
| `FAST_SMALL_MATRIX_FUNCTIONS.md` | `3f2a2edb247853d55a64bb3812828d2e57f0ceca2f5effbce56cb31bfdbab47c` |
| `EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md` | `4ba0ae280ca73a53c9bf4f2d02009d1ff8a1d649236c36a72c556ca96c64c17e` |

All five hashes were rechecked unchanged after the reconstruction.

The assigned interfaces include absolute-polylogarithmic row-circuit
dimensions and logarithmic amplitude/sensitivity bounds; an all-prefix
posterior entropy/noise event; the rounded-prefix feasibility estimate;
the added raw pair-product observations; the regularized covariance
geometry; the full guarded query-moment domain; the fixed-depth weak
propagation estimate; and finite physical patches with a frozen tail.
Here “absolute-polylogarithmic” means bounded by a fixed absolute power
of \(\log(en)\), with the multiplicative constant allowed to depend on
the fixed admissible problem and confidence. The assignment additionally
specifies that, writing \(\delta=\eta T\) for the scalar-noise tolerance,
eventually \(h/\delta\gg1\). This condition is used explicitly below.

Only the required proof and research-contract/audit instructions were read
in addition to these inputs. The canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned permission denied; the assignment's authorized fallback was used:
reuse source notation, define the local quantities, and display every
nontrivial comparison. No linked scientific sources, study history, prior
reviews, other studies, experiments, or Git operations were used. Only
this report was written.

## 2. Finite compilation is constructive with the claimed space bound

Fix a prefix. Let \(\mu=N(0,I_D)\), let the bounded moment vector be
\(F:\mathbb R^D\to\mathbb R^P\), and suppose a witness \(\nu_0\)
has \(D(\nu_0\Vert\mu)\le h\) and moment error at most \(a\).
For strict slack \(s>0\), define
\[
 \psi(\lambda)=\log\mu(e^{\lambda^TF}),\qquad
 J(\lambda)=\lambda^Tc-(a+s)\|\lambda\|_1-\psi(\lambda).
\]
The relative-entropy comparison with \(\nu_0\) gives
\(J(\lambda)\le h-s\|\lambda\|_1\). Since \(J(0)=0\),
continuity and this coercive upper bound give an attained maximum with
\(\|\lambda_*\|_1\le h/s\). Boundedness of \(F\) justifies
differentiation of the exponential integral. The coordinate optimality
conditions give
\[
 \nu_{\lambda_*}F=c-(a+s)v,
 \quad |v_r|\le1,
 \quad \lambda_*^Tv=\|\lambda_*\|_1,
 \quad D(\nu_{\lambda_*}\Vert\mu)=J(\lambda_*)\le h.
\]
No covariance rank assumption is needed.

Let \(B\) be the compiler's bound on \(|F_r|\). Rounding the exact
maximizer toward zero by the prescribed grid changes it in \(\ell^1\)
by at most \(\theta\). The log density ratio is bounded by
\(2B\theta\), so the moment change is at most \(8B^2\theta\),
and the entropy change is at most
\((2B+8\Lambda B^2)\theta\). The three choices defining
\(\theta\) make these at most \(s/8\) and \(h/8\).
The stated certified numerical errors then guarantee that this grid
point passes the tests and that every accepted point has entropy
\(<2h\) and moment error \(<a+3s/2\). Thus the search uses strict
acceptance margins, rather than an undecidable exact boundary test.
The empty-moment and \(h=0\) cases have the stated zero-tilt solution.

The log-domain quadrature also has the claimed space bound. With
\(K=\Lambda B\), the box choice gives prior tail
\(p\le t e^{-2K}\), hence tilted tail at most \(t\).
The mesh controls variation of both the log weight and the row moments,
which yields the displayed moment and log-normalizer errors. Although
the number of nodes may be enormous, its logarithm is polynomial in the
dimensions and logarithmic bounds. A first pass finds the maximum
computed log weight; a second pass sums only exponentials with arguments
in \([-G,0]\), where \(G=O(\log N+\log(1/t))\).
The discarded total weight is at most \(t/100\), and the retained sum
is at least one before rounding. The same deterministic evaluations in
the two passes are essential and are specified in the input.

The signed moment accumulators have magnitude at most \((B+1)N\).
Their integer and fractional precision, the current row, counters, and
candidate vector therefore have polynomial bit length in the stated
parameters. Subtracting the two large log sums requires their integer
bits and the requested fractional bits; it does not require a number of
bits proportional to the magnitude of the logs. The supplied elementary
exponential and logarithm routines suffice on the bounded arguments.
No table of quadrature nodes is retained. On infeasible bad states the
bounded search still terminates, after which the candidate specifies a
guarded default. Unrestricted preprocessing time is necessary here.

For the rounded circuit \(\widehat F\) and rounded center
\(\widehat c\), the witness error is at most \(2\delta\)
by the prescribed prefix precision. Setting \(a=2\delta\) and
\(s=\delta\) therefore returns an exact law at a dyadic multiplier
with
\[
 D(\nu\Vert\mu)<2h,
 \qquad \|\nu\widehat F-\widehat c\|_\infty<\tfrac72\delta,
 \qquad \|\widehat\lambda\|_1\le2(1+h/\delta).
\]
This conclusion does not require continuity of the optimizing multiplier.

## 3. Collective entropy remains polylogarithmic after compilation

Let \(\pi_c\) be the supplied exchangeable full-array posterior given
the ideal prefix and let
\(H_c=D(\pi_c\Vert\mu^{\otimes n})\). Fix **any** retained
\(\widehat c\) in the permitted rounding ball around \(c\), and
use its circuit \(\widehat F\) and compiled law \(\nu\).
The uniform rounded-prefix witness estimate gives
\[
 \|\pi_c^1\widehat F-\widehat c\|_\infty\le2\delta,
 \qquad
 \|\pi_c^1\widehat F-\nu\widehat F\|_\infty
       <\tfrac{11}{2}\delta.
\]
Using the **exact** normalizer of the returned multiplier in the
mathematical law, the change-of-reference identity is
\[
 D(\pi_c\Vert\nu^{\otimes n})
 =H_c-nD(\nu\Vert\mu)
       -n\widehat\lambda^T(\pi_c^1\widehat F-\nu\widehat F).
\]
It follows that
\[
 D(\pi_c\Vert\nu^{\otimes n})
 \le H_c+11n(h+\delta).
\]
The compiler's additive \(1\) in its multiplier bound is therefore
not silently discarded. The assigned eventual condition \(\delta\le h\)
gives the explicit sufficient bound \(H_c+22nh\), which is
absolute-polylogarithmic. Equivalently, when \(h/\delta\ge1\),
the compiler has \(\|\widehat\lambda\|_1\le4h/\delta\),
as required by the candidate's asymptotic multiplier estimate.

Without either \(n\delta=\operatorname{polylog}(n)\) or the supplied
eventual \(\delta\le h\), this inference would not follow from the
compiler's displayed bound alone. That is a real hypothesis of this
reconstruction, and it is satisfied by the assigned tiny-noise regime.
The cached approximate normalizer is an evaluation device; it is not used
to redefine \(\nu\) as an unnormalized probability law in this identity.

All these bounds hold for every admissible \(\widehat c\) on the
same ideal-prefix event. They do not require the actual retained prefix
to be a deterministic function of \(c\): it may also depend on private
acquisition packets. One first fixes an arbitrary admissible
\(\widehat c\), uses \(\pi_c\) in the identity, and then invokes
the uniform conclusion at the actually retained value. In particular this
does not replace \(\pi_c\) by a posterior conditioned on
\(\widehat c\). The final posterior-interval application of this
parameterwise statement is outside the numerical audit's assigned scope.

## 4. Cached raw Grams and whitening can be acquired offline

The candidate includes every required raw history pair product in the
finite list of row tests. After accepting a multiplier, the compiler's
quadrature routine can be rerun at any requested moment precision, with
that multiplier fixed. It therefore computes each entry of the exact
raw Gram \(Q=\nu(FF^T)\) for the relevant history vector. This
refinement is deterministic preprocessing and is independent of the
cubature seed; it is not clipped-density sampling. Products notationally
represented by \(FF^T\) here are precisely the already included
history-product tests, rather than additional query-dependent observables.

For a Gram of dimension \(r\), symmetric entrywise error at most
\(\tau/(4r)\) gives
\(\|\widehat Q-Q\|_{\rm op}\le\tau/4\). One explicit
permitted buffer is
\[
 A=\widehat Q+2\tau I,
 \qquad Q+\tfrac74\tau I\preceq A
                 \preceq Q+\tfrac94\tau I.
\]
If the supplied empirical-Gram comparison is made at most \(\tau/4\)
in operator norm by choosing \(\eta\) sufficiently small, the same
\(A\) dominates that empirical Gram. This realizes the candidate's
reserved fixed-factor ridge buffer. It imposes no lower eigenvalue
assumption on \(Q\).

There are only polylogarithmically many entries to cache; their requested
logarithmic precision and their magnitude bits are absolute-polylogarithmic.
The inverse gap of \(A\) is controlled by \(\tau\). The small-matrix
input gives a complete polynomial-cost construction: exact rational
elimination has polynomial intermediate bit length because Schur entries
are ratios of minors, and its rounded Newton square-root iteration uses
only logarithmically many iterations with a polynomial precision budget.
The rounding argument does not assume that computed iterates commute
with the input matrix. Inversion and square root give \(A^{-1/2}\)
and \(A^{1/2}\) to the assigned tolerances. A recomposition error
\(\le\varepsilon\sqrt\tau/8\) in Euclidean norm is
\(\le\varepsilon/8\) in the required covariance norm.

Accordingly, “exact cached Grams” in candidate Section 7 means exact
mathematical Grams represented to the assigned certified precision. It
does not provide or require infinite-precision cached constants. The
conclusion uses the regularized \(A^{-1}\) norm throughout, not an
uncertified pseudoinverse norm.

## 5. Finite-variance cubature and one uniform finite-seed event

For the compiled exact law let \(r=d\nu/d\mu\),
\(w=\min(r,4)\), and \(e=\mu(r-w)\). Nonnegativity of
\(r\log r-r+1\) and its bound by \((\log4-1)r\) from below
on \(r>4\) imply
\[
 e\le D(\nu\Vert\mu)/(\log4-1)<2h/(\log4-1).
\]
Thus the robust-cubature lemma is applied with its entropy parameter
equal to \(2h\), if \(h\) denotes the compiler witness budget.
This is only a fixed-factor change.

For history vector \(F\), let \(U=A^{-1/2}F\); then
\(\nu(UU^T)\preceq I\). For \(|G|\le B\), testing against
each unit vector and applying Cauchy--Schwarz under the removed measure
gives
\[
 \|\nu(UG)-\mu(wUG)\|_2\le B\sqrt e,
 \qquad
 \mu[(wUG)(wUG)^T]\preceq4B^2 I.
\]
The second inequality uses \(w^2\le4r\). It requires neither a
relative sub-Gaussian bound nor a coordinate cap for the history marks.
The target is the unnormalized capped integral, so no noisy denominator
or self-normalization step occurs. A scalar feature-second-moment test
uses bound \(B^2\); its sample variance bound is of order \(B^4\)
and its clipping bias is at most \(B^2e\). This only changes an
absolute logarithmic exponent in the resource count.

In a block of \(s\) pairwise-independent exact Gaussian rows, each
coordinate mean has variance at most \(4B^2/s\). With
\(s\ge64RB^2\varepsilon_0^{-2}\), Chebyshev bounds a coordinate
failure at tolerance \(\varepsilon_0/\sqrt R\) by \(1/16\).
For \(K\) independent blocks, a bad coordinate median needs a majority
of bad blocks. Summing over subsets bounds its probability by \(2^{-K}\).
Union over coordinates and all proof-net points gives exactly the stated
condition \(R\sum_jM_j2^{-K}\le\beta/2\).

The finite field construction supplies the independence actually used:
within each block, two distinct affine evaluations of its two uniform
field seeds are independent uniform field elements; distinct blocks
have independent seeds. Appending proof-only independent within-cell
uniforms produces pairwise-independent exact Gaussian rows in each block.
The Gaussian tail union and the clipped-quantile Lipschitz estimate
then couple the finite implementation to these exact rows. No truncation
bias for the population integral is inserted. A finite seed whose output
fails cannot have any coupled within-cell uniforms satisfying all the
sufficient good events, which transfers the joint failure bound to the
finite seed alone.

Across different prefixes and instructions, use the common maximum row
dimension and sample bounds, padding unused coordinates and reusing rows.
No independence across these different tests is needed; the union bound
already covers them. The one Gaussian-tail event then concerns the same
maximum row collection, not a new uncountable set of Gaussian draws.

All intermediate query moments are independent coordinates of the guarded
parameter domain for this proof. The net therefore controls the oracle
at computed, seed-dependent moment arguments. Coordinatewise medians are
one-Lipschitz under uniform changes of their input lists, so local row
Hölder bounds extend the net estimate. The supplied mean bounds extend
the exact integral at the same time. When a query variance is
\(\max\{0,c-b^TCb\}\), positive part is one-Lipschitz and square
root is one-half-Hölder, including at zero. This squares the mesh
tolerance. It does not introduce a width-power loss or a repeated
Hölder composition through all query instructions: the moment arguments
are separately covered coordinates.

More precisely, on the common event the approximate oracle obeys
\(\|\widehat T(u)-T(u)\|\le\varepsilon\) for every guarded
\(u\), so at a computed argument
\[
 \|\widehat T(\widehat u)-T(u)\|
 \le\varepsilon+\|T(\widehat u)-T(u)\|.
\]
If \(T\) is the exact original-law expectation, add the displayed
clipping bias to the local tolerance. Error propagation therefore uses
the supplied exact weak-expectation stability, not an empirical
rowwise square-root modulus. The elementary Gaussian derivative identity
in the cubature input does extend continuously to zero variance; the
global physical propagation bound remains an assigned interface.

Conditioning first on the complete training tape makes all compiled
tilts, Grams, and proof nets independent of the cubature seed. Averaging
the conditional bound produces one joint event for the finite prefixes,
the sphere, physical patches and frozen endpoint, and all guarded
intermediate arguments. Repeated and adaptively selected late inputs
are covered on this same event.

## 6. Precision, storage, and complete primitive query work

Large history amplitudes do enter row-evaluation precision. For example,
the map \(u\mapsto\exp(\min(u,\log4))\) is four-Lipschitz, so
the normalizer and log-density tolerance must be divided by the local
bound on the full whitened integrand, not merely by \(B\). These
local amplitudes and sensitivities have absolute-polylogarithmic
logarithms by the supplied circuit interface. On the coupled Gaussian
cube this costs absolute-polylogarithmic additional precision. Normalizer
accuracy can be set offline for this global guarded domain. Extremely
negative log densities require no huge exponential: below the logarithm
of the allocated absolute weight error, returning zero has that certified
error; all remaining exponential arguments have polynomial bit magnitude.

For a provisional cap of at most \(n^2\) generated rows, take the
Gaussian cutoff with \(T^2=O(\log n)\). The quantile bit precision is
polynomial in \(T^2\), logarithmic row sensitivities, and
\(\log(1/\varepsilon)\), as follows from the explicit CDF/Taylor/
bisection construction in the frozen randomized-integration input.
The parameter dimension is absolute-polylogarithmic; hence its covering
number has absolute-polylogarithmic logarithm and the required block
count \(K\) is absolute-polylogarithmic. The field degree
\(q=\max\{Db,\lceil\log_2(s+1)\rceil\}\) is too.

Choose \(\varepsilon=n^{-3/4}\). The complete vector-integral cost is
\[
 T_0+C K[1+RB^2n^{3/2}]W_n,
\]
where \(W_n\) includes field arithmetic, quantiles, whitening,
the complete row circuit, activation primitives and numerical arithmetic.
Scalar second moments use \(B^4\) in place of \(B^2\). Summing over
the absolute-polylogarithmic number of moment calls still gives
\(n^{3/2}\log^C(en)\) for an absolute \(C\). This verifies the
provisional row cap eventually, and is \(o(n^2)\). It is therefore
eventually within the stated dense-forward budget. The width threshold
may depend on fixed depth, data and confidence.

The seed uses \(2Kq\) random bits plus the field polynomial. The live
state consists of this seed, \(K\) vectors of block means, one row,
small matrices, current query moments, counters and numerical scratch.
Each has absolute-polylogarithmic dimension and precision. Sorting the
block means also has polynomial cost in these quantities. Neither the
\(n^{3/2}\)-scale row collection nor the parameter net is stored.
The fixed-degree polynomial algorithms compose to an absolute storage
exponent; no depth-dependent power of \(\log n\) is introduced by
the sample tolerance.

The supplied propagation factor \(A_n\le C\log^{C_L}(en)\)
gives numerical error
\(A_n n^{-3/4}=o(n^{-1/2})\) for every fixed depth. Its large
value is not squared into the sample count. Its logarithm enters any
needed local precision, where fixed-depth dependence is compatible with
an absolute logarithmic storage exponent. Clipping contributes the
separate statistical-scale term asserted in the candidate, rather than
the old literal \(1/n\) remainder.

The time statement counts the original activation primitives. The supplied
polynomial-space precision interface supports the finite-bit storage claim
and unrestricted preprocessing. It does **not** establish polynomial bit
time for activation or input evaluation. A Turing bit-time version of the
query-work claim requires the stronger polynomial-time precision access
explicitly identified in the candidate and cubature input. Strip analyticity
alone is not such an interface.

## 7. Exact verdict boundary

PASS for the stated compilation and numerical obligations: a finite
offline compiler, certified cached Grams with a regularized whitening
interface, a polylogarithmic collective KL bound in the assigned tiny-noise
regime, a single finite-seed uniform cubature event including adaptive
guarded moments and zero variance, absolute-polylogarithmic retained/live
space, and eventual \(n^{3/2}\operatorname{polylog}(n)\) primitive
query work.

The verdict does not promote the candidate to a complete decoder theorem.
The source posterior interfaces, physical cap, conditional query
representation, empirical-to-population comparison, weak propagation,
and final probability/physical-error assembly were supplied inputs to
this audit. The exact regularized norm and the primitive-versus-bit-time
qualification must remain attached to any use of this verdict.

## 8. Recheck of the revised frozen assembly

2026-10-06. **Scoped PASS maintained.** The revised
`DENSE_BUDGET_DECODER_CANDIDATE.md` was read completely. Its SHA-256 is
`931227ba250cb442013f1ecd42e1fea314b1efa22879cdd12055220fb7769c93`.
The four numerical source-lemma hashes in Section 1 were rechecked and
are unchanged. No other review or scientific input was read.

The additions in candidate Sections 2, 3 and 8 now make the quantifier
explicit: fix an ideal prefix, prove the comparison for every retained
prefix in its certified error ball, and only then substitute the actual
privately acquired value. The numerical argument requires no measurability
of that value with respect to the ideal prefix, no posterior conditioned
on private packets, and no continuity of the optimizing multiplier.
The compiled-law estimate is now explicitly
\(D(\pi_c\Vert\mu^{\otimes n})+11n(h+s)\), where the candidate's
local slack \(s\) is this report's \(\delta=\eta T\), and the
stated eventual \(s\le h\) gives the checked \(+22nh\) bound.

Candidate Section 4 incorporates the checked Gram refinement and buffer:
entrywise error \(\tau/(4r)\), symmetrization and addition of
\(2\tau I\) yield bounds between \(Q_\nu+7\tau I/4\) and
\(Q_\nu+9\tau I/4\). The master-history/principal-block description
uses the same cached finite matrices and gapped matrix operations already
covered by this audit. Separate output and outgoing-moment history bases
do not require a new integration mechanism. The revised readout-span
description similarly uses the supplied retained coefficient circuit;
its physical amplification remains part of the assigned propagation
interface, rather than a new conclusion of this numerical report.

The explicit outer probability allocation assigns \(\delta/4\) to
the single numerical seed event. Applying the cubature lemma with
\(\beta=\delta/4\) is valid and changes only its logarithmic
confidence parameter. Its complete-tape, information, noise and seed
allocations sum to \(3\delta/4\), with \(\delta/4\) left as
specified. This arithmetic and the seed interface are consistent; the
appended-indicator and posterior-interval arguments are not independently
recertified by this scoped numerical recheck.

The revised final resource claims remain the checked absolute-power
storage/workspace bounds and eventual
\(n^{3/2}\operatorname{polylog}(n)\) activation-primitive query work.
They retain the stronger precision-interface requirement for bit time,
an unquantified sufficient-width threshold, and no claim of polynomial
time in compact description size. No new numerical theorem beyond the
scoped claims reconstructed above is asserted. The author's complete
physical assembly is a separate conclusion and does not enlarge this
report's verdict boundary.
