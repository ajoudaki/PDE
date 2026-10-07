# Independent check of the certified transfer construction

2026-10-06. **PASS for the conditional constructive transfer theorem in
Sections 1–5, and for the stated retained-state and arithmetic-cost claims,
with the boundaries below.** No unresolved mathematical defect was found
in the checked version. This is a scoped internal check, not promotion or
verification of the inherited neural existence and concentration inputs.

The assignment was to check the reduction assuming its paired compact and
independent-dense inputs, including that the paired compact witness follows
the actual corrected-readout equations in Section 2. An arbitrary compact
predictor would not suffice for those hypotheses. I read the three complete
assigned proof files and the maintained notation contract only. I did not
read the study README, study history, other reviews, linked studies, or
`old_docs/`; no experiments or Git operations were performed. The rigorous
math skill was read. The required canonical-notation skill was unreadable
at its specified path (`Permission denied`), so the supervisor's authorized
fallback of explicit notation and the maintained contract was used. Its
linked neural-network reference could not be accessed through that skill.

The checked source hashes are:

| File | SHA-256 |
| --- | --- |
| `DIRECT_CERTIFIED_CONSTRUCTION.md` | `db6a744b0ca1c45b23f58f5705c5b1078ca590971a9c9780c213d67509a0cce1` |
| `FINITE_WIDTH_EXPECTATION_COMPILER.md` | `d78ac0bbff53cd60829b01f17b228114211716f8d17ee2701acdc382100536ec` |
| `COMPUTABLE_TAIL_CERTIFICATES.md` | `c605ad12f7308568770a03d47c78305d5f01c29af37ed354dcf2f1434bfcf9d9` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

## 1. Finite-time computation and the expectation module

The canonical reference uses unit inputs, loss
\(m^{-1}\sum_a(f_n(v_a)-y_a)^2\), zero stored readout, and mobilities
\((n,1,n)\). Its parameter norm is
\[
 \|(A,W,w)\|_{\rm par}^2
 =\|A\|_F^2/n+\|W\|_F^2+\|w\|_2^2/n.
\]
The gradient-flow energy identity gives total squared speed at most
\(Y^2=\|y\|_2^2/m\), hence path length at most \(Y\sqrt T\) on
\([0,T]\). On the truncated initialization box, the initial norm is at
most \(B\sqrt{d+n}\), giving the stated bound \(P\). In particular the
readout bound used here is \(\|w\|_2/\sqrt n\le Y\sqrt T\).
The query derivative bound follows from
\(\|A\|_{\rm op}\le\sqrt nP\), \(\|W\|_{\rm op}\le P\), and the
readout bound. The three dual parameter-gradient blocks are bounded by
\(1,P,P^2\); Cauchy–Schwarz with the training residuals then gives the
stated time-derivative bound. These bounds justify finite time and sphere
nets uniformly over the Gaussian box.

The compiler's indexed-monomial reduction and typed equality-partition
formula are correct. A fixed partition with \(k\) blocks of a neuron type
has exactly \((n)_k\) injective assignments; equal ordered coordinate
keys use one Gaussian moment with the full repeated multiplicity.
Different neuron populations remain different types even when both have
size \(n\). This preserves both transpose reuse and cyclic contractions.
The displayed cyclic example also has the correct value
\(2(1-1/n)\mu_2^2+\mu_4/n\).

The approximation argument establishes effective integration of the actual
finite-time tanh flow. Its componentwise bounds prevent finite-time
escape; the enlarged box gives computable vector-field magnitude and
Lipschitz bounds. The Euler error recurrence uses the true field's
Lipschitz bound and a separate uniform polynomial-field error. Choosing
the resulting error below the enlargement margin closes the induction
that keeps the iterates in that box. Bernstein approximation supplies
effective gate polynomials and a polynomial approximation of the finite
observable score. The score used in the transfer has an effective modulus:
maxima and ramps are Lipschitz, square roots have a square-root modulus,
and the minimum eigenvalue of the fixed \(m\)-dimensional Gram is
Lipschitz in its entries. No inversion near a singular dense Gram occurs.

The compiler computes a conditional expectation under coordinatewise
truncated Gaussians. The checked transfer text explicitly multiplies it
by the computable Gaussian box mass
\(Z_B^{nd+n^2}\), where
\(Z_B=\int_{-B}^{B}e^{-s^2/2}/\sqrt{2\pi}\,ds\).
This yields the unnormalized integral used in the probability proof.
Adding the outside-box union bound is therefore justified. Uniform
approximation, finite sums, and certified numerical errors suffice;
neither an infinite expected Taylor expansion nor a population-response
oracle is being used.

## 2. Tail certificates and rational openness

For the compact equations, multiplication of the corrected-readout formula
by \(F^TH_2\) gives exactly
\(F^TH_2\widehat w=y-c\). Thus \(c\) is this model's own negative
residual. Each term of \(K-Q\) is a Gram matrix, and expansion of the raw
velocities gives
\[
 K\succeq Q,
 \qquad
 \|\dot\theta\|_{\rm par}^2
 =\frac4{m^2}c^TKc
 =-\frac{d}{dt}\rho^2,
 \qquad \rho=\|c\|_2/\sqrt m.
\]
This calculation remains valid for non-diagonal positive metrics because
the stated transformed matrix norm produces the required middle term.
It does not assume that the corrected optimizer is ordinary gradient
flow.

Writing \(q(t)=Q(t)/m\) in this paragraph only, if
\(q(t)\succeq gI\), then
\(-\rho'\ge2g\rho\) and
\(\|\dot\theta\|_{\rm par}\le-\rho'/\sqrt g\).
The feature Lipschitz estimate in the tail module therefore makes the
remaining displacement smaller than the radius that could close the
Gram gap. The strict finite-state test prevents an exit from this ball.
Bounded raw parameters, bounded residual, and a positive inverse-Gram
margin place the state in a compact subset of the smooth domain, which
justifies global continuation and convergence.

The corrected readout needs its own control; the module supplies it.
With \(V=F/\sqrt m\), \(q=V^*V\),
\(\mathcal T=Vq^{-1}\), and \(P=\mathcal TV^*\), it writes
\[
 \widehat w=(I-P)w+\mathcal T(y-c)/\sqrt m.
\]
Here the adjoint uses the \(H_2\) inner product, and \(P\) is its
orthogonal projection. The derivative bounds for \(\mathcal T,P\) and
the remaining residual contribution give exactly the stated compact
tail constant. The endpoint and every later time are both controlled;
only bounding raw \(w\) would not have established this conclusion.

The two dense gate margins are exactly the dense path-length and tail
tests after substituting \(g=\lambda_+/4\). The Frobenius bound on the
middle matrix is conservative and uses a scalar contraction. A bounded,
uniformly gapped fitting trajectory makes both margins eventually
bounded below by positive constants, so multiplication by \(1+T\)
makes the gate eventually equal to one.

The compact all-time continuity argument is valid with metrics included
as constant coordinates: finite-time continuous dependence preserves a
strict tail certificate at a sufficiently late common time, and two
small tails complete the all-time estimate. This proves the existence
of rational hidden weights and rational symmetric positive metrics
within any prescribed prediction tolerance. It does not require exact
isometry constraints to survive rational perturbation. Although the
paired hypothesis does not separately repeat residual convergence for
the compact witness, its uniform Gram gap and residual equation already
imply exponential decay.

## 3. Selection, soundness, and termination

Set \(a=\delta/100\), and let \(E\) be the good paired event with
probability at least \(1-a\). For a source initialization \(z\), let
\(p(z)\) be the probability that a fresh independent dense trajectory is
farther than the supplied dense-copy tolerance. Since
\(\mathbb E p\le a\),
\[
 \mathbb E[p\mid E]\le a/(1-a)<2a.
\]
This remains true if the paired construction uses additional randomness:
lift \(p(z)\) to that joint probability space. There is therefore a paired
witness whose compact trajectory is within \(\varepsilon/16\) of a
fresh reference except with probability \(2a\). All-time rational
approximation supplies a fixed rational candidate within
\(\varepsilon/8\) of that reference with the same probability bound.
This is an existence argument; it does not require computing the witness.

For any accepted candidate, the score
\(S=1-G_T\chi(2-4D/\varepsilon)\) satisfies \(0\le S\le1\).
Inside the box, \(S<1\) forces a valid dense tail and
\(D<\varepsilon/2\). The grid margin bounds the finite-time error by
\(5\varepsilon/8\), and adding the two tails at the final grid time
bounds every later error, including the endpoint, by
\(7\varepsilon/8\). Hence the failure indicator inside the box is at
most \(S\). The acceptance inequality proves the requested probability
bound for every accepted output, without the termination hypotheses.

For the good rational candidate, the prediction ramp equals one on the
event of error at most \(\varepsilon/8\), for every choice of the grids.
Intersecting that event with the good dense fitting event loses at most
\(3a\) probability. The dense gate tends to one on the intersection;
bounded convergence gives
\(\limsup_T\mathbb E S\le3a<\delta/10\).
The outside-box bound is below \(\delta/32\). Thus some finite integer
horizon and finite precision satisfy the strict acceptance inequality.
The compact certificate also succeeds by then. Dovetailing candidate,
horizon, and precision computations reaches that finite successful job;
uncertifiable candidates cannot block it.

All selection and integration are deterministic computations from the
input law and data. The fresh reference is not sampled during selection,
so no union bound over the candidate enumeration is required.

## 4. Resource claims and remaining boundaries

The current theorem explicitly requires \(1\le q<n\), so every realized
candidate trained during setup has both widths below \(n\). The dense
object appears only through formal tensor expressions and scalar
finite-width counts. Expanding those expressions may consume more space
than dense simulation, but it does not assign values to or train a
realized dense network.

The moving coordinate count
\(dq_1+q_1q_2+q_2+m\), the two packed symmetric metric counts, and the
stated optional cache counts are correct. The vector-field arithmetic
bound accounts for hidden matrix products, cross-sample Gram products,
rank-one updates, and the \(m\)-dimensional solve. It is a cost per field
evaluation, not a certified solver complexity bound. In the setup bound,
the final definition of \(V\) counts both abstract indices and random
factor occurrences; this is sufficient to cover grouping and moment
multiplicities. The compiler's factorwise precision budget also controls
cancellation in its finite moment sum.

No bounds on rational denominators, weight magnitudes, metric conditioning,
peak setup memory, or useful total runtime have been proved. The retained
storage conclusion is a real-coordinate count only. Computability is
relative to the supplied computable-real presentations; arbitrary
noncomputable data require coordinate oracles. Sound partial search does
not make the inherited eventual width threshold effective.

I have not verified Section 6's external paired-width, dense-copy,
label-allowance, or exact source-count inputs. Conditional on its stated
width order, squaring the compact width gives the reported retained
logarithmic exponent. The transfer itself preserves the supplied error
order and cannot improve \(n^{-1/2+o(1)}\) to a constant times
\(n^{-1/2}\). Dataset-blind initialization, efficient preprocessing, and
the strict root-width target remain outside this PASS.
