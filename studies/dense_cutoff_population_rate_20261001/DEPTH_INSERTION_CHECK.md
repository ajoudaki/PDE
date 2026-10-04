# Reconstruction of the arbitrary-depth insertion argument

2026-10-03. Coordinator's internal reconstruction. This is collaborative
study validation, not an isolated promotion review. The following local
calculations were reconstructed while the complete cavity candidate was
being written. The complete 751-line frozen candidate was subsequently
read and reconstructed at SHA-256
32c2c67bbd13b26e46a590cb2a01d7bd1ac360cd174ddd2494b5d38d29677487.
The repaired final source is
e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478.
**Verdict: PASS for the complete local insertion lemma and its trace
conclusion.** The separate probability reconstruction supplies the
removal of the proof stops.
No experiment, manuscript edit, or other study is used.

## 1. Both directions of an omitted neuron

Use the manuscript's mobility-Euclidean coordinates
\(\Theta=(W^{(1)},H^{(2)},\ldots,H^{(L)},w)\), with
\(H^{(\ell)}=\sqrt n W^{(\ell)}\), and define
\(\mathcal F_a=n f_a\). The retained dense vector field is
\(-2\sum_a p_a r_a\nabla_\Theta\mathcal F_a\), where the fixed
positive sample weights sum to one.

Delete a neuron in an interior layer \(j\), along with its incoming
initialized row \(y\) and outgoing initialized column \(x\).
Conditional on all retained initialization these are independent
\(N(0,I_n/n)\) vectors. All retained normalizations stay at \(n\).
Deletion means a rectangular retained layer, or a zero embedding of the
omitted activation. Setting its preactivation to zero is a different
operation when \(\phi_j(0)\ne0\).
The neuron's forward activation supplies the external preactivation
\(x a_a(t)\) at layer \(j+1\). Its backward response
\(b_a(t)=\delta_{a,i}^{(j)}(t)\) supplies the additional lower force

\[
 -2\sum_a p_a r_a(t)b_a(t)
       D_\Theta h_a^{(j-1)}{}^\top y.
 \tag{1}
\]

Equation (1) is essential: differentiating the retained network at fixed
external preactivation alone omits the derivative through the deleted
neuron's incoming row. The learned increments of the incoming row and
outgoing column have Euclidean size at most a fixed polylogarithmic
factor times \(n^{-1/2}\) before the intended stopping time. Their
resulting vector-field errors have the same small order up to another
fixed polylogarithmic factor. The finite-depth forward derivative maps
have bounded operator norm because their matrix variations are
\(U_H h/\sqrt n\) and the feature RMS is bounded.

The dependence of the residual in (1) on the full path does not produce
an omitted order-one linear term: the residual difference is bounded by
\(C\|\Delta\Theta\|/\sqrt n\), plus the analogous external-field
term. Its product with (1)'s bounded-Euclidean Gaussian probe is small
on the proposed \(\|\Delta\Theta\|\le n^{1/100}\) event.

## 2. Why the reverse nonlinear remainder is small

For fixed sample and independent omitted row \(y\), introduce only for
this calculation the scalar lower-network function

\[
 P_y(\Theta)=y^\top h^{(j-1)}(\Theta).
\]

Its lower adjoint probes are the vectors obtained by backpropagating
\(y\) through the retained layers below \(j\). At a fixed reference
path, every probe is a bounded linear transformation of \(y\).
Its individual coordinates therefore have conditional variance at most
\(C/n\). A uniform Gaussian event can include these coordinates along
with the usual linearized forward and backward variations.

Suppose these reference probes have coordinate maximum at most
\(n^{-b}\), with \(b=1/10\). Let a parameter perturbation have
Euclidean norm at most \(N=n^a+u\), where \(a=1/100\) and \(u\)
is the nonlinear remainder cap. Along the segment to that perturbation,
forward preactivation changes have Euclidean norm at most \(CN\),
and hidden operator changes are at most \(N/\sqrt n\).
Subtracting the lower adjoint recursions, always multiplying a changed
gate by the reference probe, gives

\[
 \|q_{\rm segment}-q_{\rm reference}\|_2
 \le C\bigl(n^{-b}N+N/\sqrt n\bigr).
 \tag{2}
\]

Propagation of an already estimated difference uses only bounded
operators and slopes. Hence no power \(N\) is accumulated per layer
in (2). The segment probe coordinate maximum is at most
\(C n^{-b}(1+N)+CN/\sqrt n\).

The Hessian of \(P_y\) has the standard sum of activation-curvature
terms, whose diagonal weights are these probes, and mixed weight terms
carrying the factor \(n^{-1/2}\). Its operator norm is bounded by

\[
 C n^{-b}(1+N)+C(1+N)/\sqrt n.
\]

Integrating this Hessian along the segment proves

\[
 \|D_\Theta h^{(j-1)}(\Theta+\Delta\Theta)^\top y
       -D_\Theta h^{(j-1)}(\Theta)^\top y\|_2
 \le C n^{-b}(N+N^2)
          +C(N+N^2)/\sqrt n.
 \tag{3}
\]

For \(N\lesssim n^a\), the leading power in (3) is
\(n^{2a-b}=n^{-0.08}\). Multiplication by the stopped scalar
controls and integration of the residual adds only fixed constants and
polylogarithmic factors. A weak propagator bound \(n^{1/400}\)
therefore still leaves a vanishing error. The tempting estimate using
only \(\|y\|_2\) loses this coordinate smallness and does not close
the nonlinear remainder.

This argument needs bounded first and second activation derivatives.
The complete vector-field Taylor remainder also needs the bounded third
derivative used in the candidate activation class.

For that complete remainder it is essential to separate the Gaussian
linear variation from the nonlinear error before bounding a coordinate
product. If \(\|v\|_2\le Cn^a\), \(\|v\|_\infty\le n^{-b}\),
and \(\|u\|_2\le u_*\), then
\[
 \|(v+u)\odot(v+u)\|_2
 \le C n^{a-b}+2n^{-b}u_*+u_*^2.
 \tag{4}
\]
The coarser product bound
\((n^{-b}+u_*)n^a\) introduces an unjustified growing coefficient
\(n^a u_*\) in the closing inequality. Applying (4) to all forward
and backward linear coordinate variations avoids it. Mixed matrix
variation terms retain their factor \(n^{-1/2}\). Thus the intended
nonlinear source bound has a polylogarithmic multiple of
\(n^{a-b}+u_*^2+n^{2a-1/2}\), together with the reverse-source
term \(n^{2a-b}\). With \(u_*=n^{-0.04}\) and propagator bound
\(n^{1/400}\), each resulting power is strictly smaller than the cap.

For clarity, the full gradient-block calculation behind that assertion
uses
\[
 \nabla_{W^{(1)}}\mathcal F_a=\delta_a^{(1)}v_a^\top,
 \qquad
 \nabla_{H^{(\ell)}}\mathcal F_a
       =\delta_a^{(\ell)}h_a^{(\ell-1)\top}/\sqrt n,
 \qquad
 \nabla_w\mathcal F_a=h_a^{(L)}.
 \tag{5}
\]
Forward induction and then backward induction give a polylogarithmic
multiple of
\(n^{a-b}+u_*^2+n^{2a-1/2}\) for the nonlinear response
remainders. In (5), a remainder times an unperturbed feature has norm
at most its own norm times the bounded feature RMS. A remainder times
an unperturbed backward response has the analogous bounded backward
RMS factor. Every product of two changed hidden factors retains
\(1/\sqrt n\). This accounts for all hidden gradient-block terms;
the first and last blocks have no extra outer product.

The residual also changes. Its first variation is
\(O(n^{a-1/2})\), because the unnormalized prediction gradient
has norm \(O(\sqrt n)\). Its scalar second remainder is bounded
by \(\operatorname{polylog}(n)n^{2a-1}\), using the augmented
prediction Hessian, including the external preactivation coordinate.
Multiplying this last remainder by the unperturbed gradient contributes
\(\operatorname{polylog}(n)n^{2a-1/2}\) to the vector field.
The product of the first residual variation and changed gradient has
the same bound. Thus changing the residual has not been omitted or
replaced by a prescribed control.

Integrating the terms multiplied by the reference residual costs its
bounded total activity; integrating the other small terms costs at
most \(T_n=O(\log n)\). Applying the weak propagator estimate
therefore multiplies the displayed powers by at most
\(n^{1/400}\operatorname{polylog}(n)\). At a putative first
attainment of \(u_*=n^{-0.04}\), the resulting bound is
\(o(n^{-0.04})\), which closes this particular remainder cap.

## 3. Uniform controls and independent Gaussian forms

The physical coordinate speeds at an interior layer give Lipschitz
control constants of order \(\sqrt n\) times a polylogarithm.
For sup-norm accuracy \(n^{-1/8}\), an elementary time mesh and
amplitude quantization produce a control net with log cardinality
\(O(n^{5/8}\operatorname{polylog}n)\). Fixed sample, layer, and
deletion counts enter its constant only.

If linear operator norms are at most
\(n^{1/400}\operatorname{polylog}n\), Gaussian coordinate and
quadratic-form tails at threshold \(n^{-1/10}\) have exponents at
least \(n^{0.78}\) for all sufficiently large widths. They dominate
this net entropy. A fine polynomial time mesh adds only \(O(\log n)\)
to the log cardinality. The control-net interpolation error is at most
\(n^{-1/8+1/400}\operatorname{polylog}n=o(n^{-1/10})\).

The linear retained variation contains terms linear in both \(x\)
and \(y\). Pairing its backward response with \(x\) yields a
quadratic form in \(x\) and a centered bilinear form in \((x,y)\).
Conditional independence justifies the zero mean of the latter. The
quadratic mean is its normalized trace, not zero. The separate checked
endpoint trace estimate is required for that contribution.

## 4. Scope of the initial reconstruction

These calculations initially justified the treatment of the additional
reverse source before the complete source was available. They do not
alone remove the finite-network stops. The subsequent complete
reconstruction and its relation to the probability check follow.

## 5. Complete source reconstruction

The source's exact retained equation (4) agrees with (1) above. Both
omitted initialized directions remain Gaussian and independent after
conditioning on all retained initialization. The omitted learned column
and row bounds in source (10) follow directly from the canonical dense
gradient updates and respectively cost \(CS^2/\sqrt n\) and
\(CSM_n/\sqrt n\). Their multiplied source remainders have the
required inverse-square-root-width size up to logarithms.

Source (11) includes all mixed weight-block terms of the full-depth
Hessian. Each large term is a bounded-map contraction of one carrier
diagonal. Each remaining term factors through a width-dimensional
vector space, so rank is \(O_L(n)\), rather than the ambient
parameter dimension. Its deterministic normalized Hilbert--Schmidt
bound uses the carrier RMS; its higher Schatten bound uses the stopped
exponential budget. This verifies (12), the negative-Gram variational
decomposition (13), and the weak propagator bound (14).

The exact external derivatives (15) include the rank-one adaptive
residual contribution. Their Gaussian images include both forward
and backward linear variations, and the independent incoming-row
adjoint probes. Source Sections 4–5 use the split described above,
with \(n^{0.01}\) Euclidean linear radius, \(n^{-0.1}\) coordinate
radius and \(n^{-0.04}\) nonlinear cap. The stated net entropy
\(n^{0.625}\operatorname{polylog}n\) is strictly below the Gaussian
tail exponent \(n^{0.79}\). The joining segment's carrier bound follows
from the same block expansions; it is not an assumed intermediate
maximum. The residual Taylor terms retain the extra \(1/\sqrt n\).
Source (23) therefore closes the claimed remainder cap with its weaker
\(n^{0.001}\) propagator loss. In particular the uniform retained
coordinate error in (24) tends to zero.

Section 6's normalized trace keeps both response endpoints. A term with
\(h\) residual Hessians has \(h+2\) noncontraction factors, so the
Schatten normalization exactly cancels the displayed \(1/n\).
For \(h\ge1\), the budget-dependent series begins at \(S^4B\)
before the exterior residual integral and at \(S^5B\) afterward.
The zeroth term instead uses the deterministic Hilbert--Schmidt
endpoint bounds. The stated looser singleton shift
\(CS(1+S^2B)\) follows. The direct external trace is \(CS\) by
carrier RMS, the adaptive rank-one trace vanishes with width, and
the mixed incoming/outgoing quadratic form is centered because those
two Gaussian vectors are independent. The simultaneous control event
justifies substituting the actual adaptive histories. Thus (28) is
proved, with a constant independent of the later empirical moment degree.

I also read Sections 7–9 completely. The separately persisted
DEPTH_CAVITY_PROBABILITY_CHECK.md reconstructs their time modulus,
whole-path Gaussian bounds, initialization transfer, stopping-time
comparison, fixed-block moments, collision terms, order of limits, and
all-time tail. I agree with that reconstruction. Together these are a
complete internal check of the finite carrier theorem.

The final source repairs restore mathematical delimiters, explicitly
define the strict full initialization event, and state rectangular
activation deletion when \(\phi(0)\ne0\). Its final comparison equation
uses the separately checked deterministic depth-tracking theorem rather
than attributing that new result to the manuscript. Its fixed-positive-
weight variant has the correct Gram \(D_pH_L^\top H_LD_p/n\).
These repairs are incorporated in the final hash at the start.

## 6. Extension to activation values with linear growth

After this bounded local check, I read and reconstructed all 442 lines of
UNBOUNDED_INSERTION_CHECK.md at initial hash
b9bfdd910f3dd103feaf1e9a94a09db782dc3cda63b9354142d8fb5585def061.
Its source is the coordinator's joint-budget derivation. The local
extension also passes: forward Jacobians, all block Taylor bounds and
gradient products use feature RMS, while deleted forward amplitudes
gain only logarithmic factors on the joint cap. Bounded first three
activation derivatives suffice for the Taylor and time-grid estimates.
The joint budget includes the top carrier, so the earlier deterministic
coordinate bound on the readout is not silently reused.

Both actual-amplitude trace estimates (11) and (13)–(15) check.
The backward response uses the two-endpoint trace already proved.
The forward response uses bounded forward endpoints and the normalized
Hilbert--Schmidt estimate for \(J-U_0\), with no norm taken of the
full-dimensional identity. This gives the two reciprocal inequalities
with coefficients \(C(1+S^2B)\) and
\(CS^2(1+S^2\sqrt B)\), respectively.

At the top, the omitted prediction offset \(d_a\) multiplies both
the retained gradient and the reverse force. Its exact source equation
(17) correctly includes both. The extra product
\(d_a D_\Theta h_a^{(L-1)\top}q_a\) is
\(n^{-1}\operatorname{polylog}n\), smaller than the permitted
\(n^{-1/2}\operatorname{polylog}n\) source remainder.
The coordinator's original candidate prose is corrected accordingly.

The local estimates control retained preactivations as well as carriers.
Thus joint stopping budgets transfer with a multiplicative \(1+o(1)\).
Both incoming-row forward and outgoing-column backward comparisons
preserve omitted-root independence under projection of the entire
frozen difference path. The Gaussian projection radius vanishes after
division by \(\sqrt n\), as required. The initialized joint-budget
and fixed-size-cavity transfer use conditional Gaussian estimates on
bounded preceding covariance sets, not an unstopped deep-network
Gaussian tail.

These estimates supply all local hypotheses of
UNBOUNDED_ACTIVATION_CHECK.md, whose complete conditional probability
reconstruction was also read and checked. Combining the local extension
with that report removes the local condition. No bounded-value
assumption or additional trained-moment hypothesis remains. Final source
versions and the combined theorem are recorded in DEPTH_EXTENSION_RESULT.md.

The unbounded local report's final formatting-only version is
bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578.
The coordinator's completed joint-budget source, including the exact
top residual offset, is
e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713.
The complete enlarged activation/initialization note and its separate
check cover the nonaffine class with bounded first three derivatives.
Together these establish the broad activation scope used in the final
theorem, while retaining the fixed-depth and small-label assumptions.
