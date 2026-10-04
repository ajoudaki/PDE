# Internal audit of the assembled tanh transfer

Date: 2026-10-02.

**Final verdict: PASS for the stated finite-step tanh universality
theorem, using the frozen Lipschitz-program lemma and the published
theorem imports identified below.** The integration no longer has an
unproved premise (P). No substantive mathematical gap was found in the
assigned statements. This is an internal same-context review, not a
fresh isolated promotion review or a certification of all published
source proofs.

This is an internal same-study audit. The reviewer has prior controlled-flow
review context from another study, but no scientific finding or input from
that study was used. The previously reviewed polynomial-transfer result in
this same fast-mixing study is an explicitly authorized dependency.

## Input boundary, hashes, and actual coverage

Read in full:

- TANH_TRANSFER.md, 137 lines, final reviewed SHA256
  06b2bdb0ebcae7a6e2cb87673be72e5e648874a09590bf560cceac73f2693ca6.
- TANH_CLIPPING_REVIEW.md, 336 lines, SHA256
  c3bffd1f7af089202d49240a0520fc9db13c0201bb36c87cb322dbfa1632edde.
- LIPSCHITZ_PROGRAM_TRANSFER.md, 240 lines, frozen SHA256
  5923211811d231f223e530099d1ca0d9dad967bd8fd2b6c167c4bd751fcde8f6.

The earlier same-study polynomial candidate, 192 lines, was previously
read completely at SHA256
9738334f29fb09f2123f075e3e94cb759fa419fc426bc46123296eb9d10c6c6c.
Its finite polynomial conclusion is not being substituted for (P).
The notation, neural-network convention, and rigorous-proof instructions
already read remain in use.

No other study, author history, implementation, training output, or GPU
resource was accessed for this audit. No code or experiment was run.
At the start of this review, the program lemma was still being written
and was explicitly not an available proved input. The initial assembly
hash was 090e3d0741d27797e83b6f01751d639825eb58f91e4ac9a2aa9689f69012a132.
The final assembled and program files were reread and rehashed after
the lemma arrived. The reviewer edited only this report.

Primary-source checks in this continuation were:

- [Wang–Zhong–Fan, arXiv v5](https://arxiv.org/html/2206.13037v5):
  the rectangular recursion, Assumption 2.17, Theorem 2.22, Gaussian
  and invariant prescriptions D.1–D.5, Proposition D.1's statement,
  complete D.3, complete section 3.3, and Appendix A. The previous
  same-study polynomial review checked the matrix and tree imports
  against v3; the relevant v5 statements were checked here.
- [Fan, arXiv v5](https://arxiv.org/html/2008.11892v5):
  section 2.4's moment-cumulant relation, the rectangular recursion
  and complete section 5.1, Assumption 5.2 and Theorem 5.3,
  and the corrected finite-dimensional Haar-conditioning identity F.1.

These are checks of the exact imported statements and the relevant
approximation mechanism. The author note's assertion that its author
read all of Fan's Appendix B is not an assertion that this reviewer
repeated that reading. This review does not independently rederive
every block identity and conditioning induction in that appendix, or
every combinatorial bound in WZF. The published theorems remain
identified external theorem inputs.

The manuscript and implementation were outside the assigned inputs.
Consequently the theorem is checked for the equations actually displayed
in TANH_TRANSFER.md; the phrase identifying them with the manuscript
and their agreement with executed code are not independently certified.
No additional scientific input is missing for the scoped mathematical
integration.

## The theorem being checked

Fix the sample count \(m\), input dimension \(d\), data, finite query
list, positive step size \(\eta\), and step count \(J\), independently
of width. The network has two hidden coordinate spaces: \(A,H_a\)
belong to the first, \(w,D_a\) to the second, and

\[
B=W_0-\frac{2}{mn\tau}\sum_aD_aH_a^\top.
\]

The forward, backward, raw \(q=1\) memory equations, and both explicit
Heun stages are the equations in the assembly. This audit checks
common deterministic limits in probability for the stated finite
observable collection. No agreement between the dense and \(q=1\)
algorithms is part of that statement.

The required premise must cover finite typed programs with repeated
actions of the same \(W_0\) and its true transpose, allowed independent
initial channels, globally Lipschitz same-side coordinate maps with
finite retained history, and causal scalar empirical feedback. It must
allow zero and redundant channels. Its conclusion must cover bounded
Lipschitz empirical tests, with continuous functions of a finite
convergent scalar list obtained afterward. A theorem only for a literal
AMP recursion, polynomial maps, nondegenerate covariance, or a restricted
feedback class would leave an integration gap. The frozen program
lemma supplies the required broader statement, as checked next.

## Audit of the Lipschitz-program lemma

The matrices have two typed coordinate spaces. The proof never
identifies their coordinates merely because both dimensions equal
\(n\). Sample-dependent maps are permitted: the finitely many inputs
and labels are fixed coefficients in local functions, not functions
selected by a hidden-unit index. Empirical scalar averages can
communicate between the spaces. Matrix dependence of those averages
is explicitly allowed.

The structured spectrum, four independent signed permutations, and
Hadamard factors match the already checked classification. Gaussian
and structured matrices share the required limiting diagonal law,
not just a second moment. Both have the eventual operator-norm
bound proved below. At aspect ratio one, the moment-cumulant relation
specializes the quarter-circle law to the Gaussian prescription.
The transposition and factor-of-aspect-ratio conventions in the
candidate agree with the primary formulas.

For fixed scalar registers, eliminating local instructions gives a
globally Lipschitz function of same-side roots and previous raw
matrix outputs at each query. Alternating matrix directions with
ignored slots handles arbitrary query order. The first ignored pair
is needed: it makes the first AMP message Gaussian even if the first
desired query is a nonlinear function of the original roots.

For this embedding, \(u_t,v_t\) denote left and right queried
messages; \(y_t,z_t\) are the corresponding corrected left and
right AMP fields, and bars denote raw matrix outputs. The
same-side Gaussian root lists are \(F,G\), respectively.
The AMP decoding is causal. When \(u_t\) is defined, the coefficients
\(b_{ts}\), \(s<t\), are determined. The right-side local map can
recover the raw field by
\[
\bar z_t=z_t+\sum_{s<t}b_{ts}v_s,
\]
because each \(v_s\) is a previously defined right-side function.
Only then is \(v_t\) defined and its coefficients \(a_{ts}\) determined.
The left-side decoding
\[
\bar y_t=y_t+\sum_{s\le t}a_{ts}u_s
\]
uses \(u_t\), which depends only on older left fields. Thus no
unknown current message is solved for implicitly. These identities
hold at finite width; raw fields are not asserted to be Gaussian.
All correction coefficients are deterministic expectations under
the recursively defined state evolution.

For each fixed auxiliary-noise level \(\varepsilon>0\), the decoded
maps remain globally Lipschitz. For every fixed side-root value their
slices in the AMP fields are Lipschitz, hence have bounded weak
derivatives. Nonsingular Gaussian field laws allow the expected
derivatives to be defined even when the side-root law is degenerate.
No unjustified continuity of empirical derivatives is used.
The target theorem is WZF's Lipschitz theorem; Fan's stronger
derivative-continuity condition is used only for the auxiliary
polynomial proof input, where it holds.

Fresh query noise ensures nondegeneracy in this construction.
Writing \(V_t,Z_t\) for right-side state-evolution limits and
\(\zeta_t\) for a fresh standard Gaussian right root,
\[
V_t=B_t(Z_{1:t},G\text{ without current/future noise})
       +\varepsilon\zeta_t.
\]
For a nonzero coefficient vector \(c\), let \(r\) be its last nonzero
index. Earlier messages and \(B_r\) do not consume \(\zeta_r\).
Conditional on the Gaussian fields and all other roots, the variance
of \(\sum_s c_sV_s\) is \(\varepsilon^2c_r^2\). Thus its second
moment is positive. This proves positive definiteness of the
uncentered message Gram matrix; the same proof works on the left.
It is not a claim about centered message covariances. Future roots
appearing in the list of side information do not invalidate this
argument, because the coordinate functions do not use them early.

The dummy initialization has positive second moment and is jointly
Gaussian with the augmented roots, including duplicates and constants.
Chebyshev bounds for each root monomial are summable along dyadic
widths. Countably many such bounds, Gaussian moment determinacy, and
higher moments give all-order empirical Wasserstein convergence.
The candidate's entire-Laplace-transform argument proves polynomial
density for nondegenerate Gaussian roots; the affine-support argument
correctly includes singular covariances. Root independence from the
matrix is preserved. These facts verify the initialization hypotheses
without requiring the actual learner to have nonzero initial
readout or independent duplicate channels.

If one reads WZF's infinite-sequence notation literally, the finite
noisy prefix can be extended without adding more root channels.
After its last pair take \(u_{t+1}=\tanh(y_t)\) and
\(v_{t+1}=\tanh(z_{t+1})\). A positive-definite Gaussian field
covariance gives positive conditional variance for its newest
coordinate given all earlier fields. Conditioning additionally on
the side roots, tanh of that coordinate cannot lie in the span of
the earlier messages. This successively preserves both message
Gram matrices' positive definiteness. The extension does not alter
the finite prefix. A short explicit paragraph would remove a
formal ambiguity in the frozen text; no separate appendix or new
mathematical assumption is needed.

The removal of query noise is performed in the raw program, where
the original local Lipschitz constants apply. It does not require
the decoding constants, covariance inverses, or Onsager coefficients
to remain bounded as \(\varepsilon\) vanishes. Original saved
messages are kept distinct from noisy matrix-query arguments.
Consequently finite induction gives
\[
\max_j E_j\le K\varepsilon\sum_r\|\eta_r\|_n
\]
with \(K\) independent of width and noise level. Here \(E_j\) sums
the normalized Euclidean discrepancies of the stored channels and
\(\eta_r\) are the finitely many auxiliary Gaussian vectors.
The normalization is \(\|X\|_n^2=n^{-1}\sum_i\|X_i\|_2^2\).
At countably many noise levels, the almost-sure convergence events
can be intersected. The deterministic noisy-program limits are
Cauchy by comparison with the same raw zero-noise run. This proves
the zero-noise limit without exchanging width and noise limits.
The result descends to the original probability space because the
zero-noise output does not depend on auxiliary roots.

Finally, feedback is handled in causal order, not by treating a
random coefficient as independent of the matrix. Before the next
average, every earlier scalar register already converges to a
finite deterministic value. Freeze those values only in that
prefix. They eventually lie in compact neighborhoods, and condition
(3) gives the local comparison bound
\[
L_K\|X-X'\|_n+
L_K(1+\|X'\|_n)\|c_n-c\|.
\]
The frozen and actual finite prefixes have bounded normalized
norms by linear growth and the operator-norm bound. Induction
makes their difference vanish. The next bounded Lipschitz average
therefore has the same limit as its frozen version. Continuous
scalar operations then converge on the specified neighborhoods.
This supplies exactly the adaptive feedback needed by the clipped
tanh learner.

For application, \(A(0)\) is a Gaussian root and initial
\(H_a=\tanh(A(0)x_a/\sqrt d)\) is a local instruction. It is not
incorrectly declared an additional Gaussian root. A finite list
of sample channels and Heun stages is covered by finite vector
outputs or equivalent scalar channels. The clock reciprocal is
evaluated away from zero. With the assembly's bounded extensions,
every clipped product satisfies the program lemma's local
regularity conditions. Thus the lemma closes premise (P).

## Uniform bounds include every predictor and hybrid

Let \(Y=\max_a|y_a|\). At a state with \(|w_i|\le M_k\),
boundedness of tanh gives
\[
|f_a|\le M_k,\qquad |r_a|\le M_k+Y,\qquad
|\dot w_i|\le2(M_k+Y).
\]
The predictor is bounded by
\[
M_k^*=(1+2\eta)M_k+2\eta Y.
\]
The accepted Heun readout is therefore bounded by
\[
M_{k+1}
=M_k+\eta[(M_k+Y)+(M_k^*+Y)]
=(1+2\eta+2\eta^2)M_k+(2\eta+2\eta^2)Y.
\]
The difference \(M_{k+1}-M_k^*=2\eta^2(M_k+Y)\) is nonnegative.
Since \(M_k\) increases from zero, \(M=M_J\) bounds all accepted and
predictor readouts through the requested computation.

This argument does not use \(A\), a clipping threshold, or an
operator-norm bound. It therefore applies to every clipping hybrid.
At both stages,
\[
\rho\le M+Y,\qquad |\delta_{ai}|\le M.
\]
Writing \(T=J\eta\), positive Heun coefficients and the initial prefix
give
\[
1\le\tau\le1+T(M+Y),\quad
|H_{ai}|\le1+T(M+Y),\quad
|D_{ai}|\le TM(M+Y).
\]
A predictor at step \(k<J\) has accumulated at most \((k+1)\eta\le T\)
of these bounded increments, so no extra predictor factor was omitted.
No division by \(\rho\) occurs. When \(J=0\), no clipping is needed;
when \(Y=0\), the zero readout and residual make the updates stationary.

The Gaussian operator-norm constant eight is sufficient: a pair of
\(1/4\)-nets has at most \(9^{2n}\) pairs, and
\[
\Pr(\|W_0^G\|>8)
\le2\,9^{2n}e^{-8n}.
\]
This is summable. The structured norm is its largest singular value,
eventually below three by the specified bounded quantiles and
normalization. Thus one fixed \(C=8\) supplies the required
probability-tending-to-one norm event for both ensembles.

## The sparse local estimate needs no adaptive tail hypothesis

For
\[
p_a=W_0^\top\delta_a,\qquad
b_a=\frac{2}{mn\tau}\sum_bH_b(D_b^\top\delta_a),
\]
the proved component bounds give
\[
|b_{ai}|\le2B_HB_DM,\qquad
\|p_a\|_2^2/n\le C^2M^2
\]
on the operator-norm event. These are deterministic estimates even
though \(\delta_a\) depends on the same matrix.

At a write of the first-layer velocity, clipping each \(p_{ai}\) to
\([-R,R]\) changes the output only on
\[
\bigcup_a\{i:|p_{ai}|>R\},
\]
whose row fraction is at most \(mC^2M^2/R^2\). In the capped row
metric
\[
d_c(U,V)^2=\frac1n\sum_i\min\{\|U_i-V_i\|^2,1\},
\]
the write error is at most \(\sqrt m\,CM/R\). No claim that the
ordinary normalized squared clipping error tends to zero is used.
In particular, a bounded second moment has not been mistaken for
uniform integrability of the squared adaptive response.

## Heun buffers and the clipped suffix

Both first-layer velocity buffers must be retained in the augmented
state until
\[
A^*=A+\eta\dot A^{(1)},\qquad
A^+=A+\frac\eta2(\dot A^{(1)}+\dot A^{(2)})
\]
have been formed. Every accepted, predictor, and saved \(A\) copy and
every retained first-layer velocity must use \(d_c\). The bridge
explicitly does this. It would be invalid to measure either old
velocity in ordinary Euclidean distance and use its sparse clipping
bound as though it were small in that stronger norm.

For fixed real coefficients,
\[
d_c\!\left(\sum_jc_jU_j,\sum_jc_jV_j\right)
\le\sum_j\max(1,|c_j|)\,d_c(U_j,V_j).
\]
Thus the later reuse of an old, possibly unclipped velocity is
Lipschitz without any bound on its row magnitudes. The Heun coefficients
in these operations are fixed; the argument is not silently applying
this inequality to changing scalar coefficients multiplying an
unbounded stored buffer.

For a fixed data or query input \(x\),
\[
|\tanh(U_ix/\sqrt d)-\tanh(V_ix/\sqrt d)|
\le\max(\|x\|/\sqrt d,2)\min(\|U_i-V_i\|,1).
\]
Consequently first-layer features and their bounded activation gates
are Lipschitz from the capped metric to normalized Euclidean distance.
The finite different inputs merely specify different fixed
same-row maps. They introduce no width-dependent map or forbidden
dependence on the neuron index.

Subsequent matrix actions cost at most \(C\) in normalized Euclidean
distance. The history corrections use only bounded channels and
normalized empirical products. In a clipped velocity write, the only
previously problematic product is now a bounded gate times a bounded
clipped response. Its difference has a finite Lipschitz constant
depending on that write's threshold, but not on width or incoming
\(A\)-row magnitudes. The stored unbounded matrix-action temporary
\(p_a\) itself can use normalized Euclidean distance, because its
later nonlinear use in these writes is through clipping.

For literal global Lipschitz hypotheses, bounded extensions must apply
to all bounded arguments used in products, including the relevant
scalar coefficient reads. Clamping only \(w,H,D,\tau\) is shorthand:
predictions, residuals, residual norms, and moment contractions have
deterministic valid-path bounds and can be projected to those bounds
before multiplication too. These projections preserve every hybrid.
The residual norm is Lipschitz as a function of its residual vector;
no Lipschitz assertion about scalar square root at zero is needed.

The observable class must also be precise. Retained \(A,H,w,D\)
state channels and their finite histories are covered. An unbounded
intermediate such as an unclipped
\(\ell_a=(1-h_a^2)(p_a-b_a)\) is not automatically an ordinary
Euclidean-Lipschitz channel of the augmented program. Covering arbitrary
tests of that additional field would require a specified metric or
an additional clipping argument. The refreshed assembly explicitly
restricts the claim to retained state channels.

## Threshold order and passage to the limit

There are \(N=2J\) first-layer velocity writes. Replace them from the
last to the first. At the comparison for write \(j\), both programs
have identical incoming augmented states and hence identical local
response \(p_a\); only the new velocity differs. Every later write is
already clipped at a fixed threshold.

The suffix Lipschitz constant \(S_j\) includes all retained-buffer
reuse, copies, future stage computations, and saved basic observables.
It depends on later thresholds but not on the current \(R_j\).
This independence is justified by the capped metric on the incoming
velocity and every later \(A\) copy. Choosing \(R_j\) only after the
later thresholds, so that
\[
S_j\sqrt m\,CM/R_j\le\varepsilon/N,
\]
gives a deterministic total error at most \(\varepsilon\) for the
basic finite Lipschitz observable vector. The hybrid bounds used in
the local estimate are uniform over all these choices. A single
threshold tending to infinity with an uncontrolled threshold-dependent
suffix constant would not justify this step; the bridge avoids it.

Reverse thresholds should be chosen for the finite vector of basic
bounded Lipschitz averages, not for an arbitrary continuous function
of that vector. Such a function need not itself have a suffix
Lipschitz constant. RMS quantities and general continuous functions are
obtained after the basic convergence statement, by continuity.

By the now-checked program lemma, each fully clipped program has a deterministic
common limit \(a_k\). Coupling two clipped programs to the same original
run gives their distance at most \(\varepsilon_k+\varepsilon_l\)
on the common norm event. Their deterministic probability limits
therefore satisfy the same inequality. The sequence \(a_k\) is Cauchy.
Taking width to infinity at each fixed clipping program and then
letting its tolerance vanish proves the claimed convergence in
probability. This argument makes no exchange of width and clipping
limits and does not produce an almost-sure conclusion.

A bounded globally Euclidean-Lipschitz row test of retained state
channels is Lipschitz in the capped metric for its unbounded arguments:
boundedness controls large changes, and its Euclidean Lipschitz constant
controls small changes. Averaging is then controlled by
Cauchy–Schwarz. Unbounded \(A\)-moments do not follow.

Predictions and feature Gram entries have bounded Lipschitz extensions.
Squared feature displacements are bounded polynomial functions of
bounded initial and current features. Their RMS values follow by
continuity of square root; classification at zero limiting margin
does not follow. These conclusions are for the fixed finite collection,
not a continuum of queries or a growing time grid.

## Counterexample attempts, consequences, and final limits

The main attacks checked were: zero and duplicated messages; a nonlinear
first desired matrix query; two successive queries in the same direction;
matrix-dependent scalar coefficients; a zero residual norm; a rare
arbitrarily large adaptive backward response; reuse of an old Heun
velocity after the local clipping comparison; and nonlinear final
observables with a non-Lipschitz derivative at the limiting value.
The dummy pair, query serialization, fresh noise, causal freezing,
norm formulation of the residual, capped metric, augmented buffers,
and final continuous mapping respectively address these cases.

Three clarifications found at the conditional checkpoint are all
present in the refreshed assembly:

1. Bounded scalar reads are projected before products, alongside
   bounded vector reads.
2. Empirical state tests concern retained same-layer channels; they
   do not silently include arbitrary unbounded intermediate credit.
3. Reverse threshold selection targets the basic bounded Lipschitz
   average vector. Arbitrary continuous final functions are applied
   only after that vector converges.

There is no remaining substantive proof gap in the assigned
finite-step result. The strongest limitations concern what it does
not quantify: no convergence rate, width-dependent time horizon,
step-refinement limit, fixed-precision guarantee, or uniform family
of queries follows. The construction gives no Euclidean convergence
of read-in rows or their unbounded moments. A discontinuous
classification decision at a zero limiting margin remains outside
the theorem.

The fast transform and retained moment counts support the stated
absence of a dense \(n\times n\) source matrix. The arithmetic count
\(O(mn\log n+m^2n+mnd)\) follows by counting matrix actions, moment
contractions, and first-layer evaluations for a fixed query list.
The accepted state has \(nd+n+2mn+1\) moving coordinates.
An explicit Heun implementation also retains a constant number of
\(nd\)-sized stage/velocity buffers. These fit an \(O(n)\) workspace
statement with fixed \(m,d\); if displaying their separate dependence,
write \(O(nd+mn+m^2)\) workspace. No implementation or timing
measurement was checked here.

Finite-history dense learning can fall within the same program class.
Consequently this theorem establishes ensemble transfer for the
specified response-memory learner; it does not establish an exclusive
universality property, an accuracy advantage, or agreement with dense
training. The storage distinction as the step count grows is separate
from a theorem whose step count is fixed.

Final disposition: **internal PASS** for the frozen program lemma's
application and the assembled tanh theorem. The optional finite-prefix
extension paragraph above removes a formal presentation ambiguity.
The primary theorem imports and the unverified manuscript/code
correspondence remain disclosed limits of this review. No promotion
status is conferred, and the frozen inputs were not edited by the
reviewer.
