# Four distinctions needed before a dimension-exponent theorem

These are elementary auxiliary statements, not a resolution of the neural
compression problem. No unpromoted research is an input. Symbols introduced
in a numbered statement are local to it.

## 1. The sphere has a smaller polynomial table, not a small nonlinear decoder

For d >= 2 and an integer k >= 2, restrictions to the radius-sqrt(d) sphere
of real polynomials of total degree at most k form a space of dimension

\[
\binom{d+k}{d}-\binom{d+k-2}{d}
=\binom{d+k-1}{d-1}+\binom{d+k-2}{d-1}
=\Theta_d(k^{d-1}).
\]

Here the subscript on Theta means its constants depend on the fixed dimension;
it is not an additional quantity or a uniform joint dimension/degree estimate.

Proof. Divide a polynomial by the monic polynomial
\(x_d^2+\sum_{j<d}x_j^2-d\), treating it as a polynomial in x_d.
Division preserves the total-degree bound and leaves a remainder
\(A(x_1,\ldots,x_{d-1})x_d+B(x_1,\ldots,x_{d-1})\).
If the original polynomial vanishes on the sphere, evaluate the remainder
at both square roots of \(d-\sum_{j<d}x_j^2\) in the open ball where this
quantity is positive. Subtract and add: A and B both vanish on an open set,
so both are zero polynomials. Thus the restriction kernel consists exactly
of multiples of the sphere equation, with quotient degree at most k-2.
Multiplication by the sphere equation is injective. Counting monomials and
using Pascal's identity proves the formula. For k=0 and k=1 the respective
dimensions are 1 and d+1, as direct counting shows.

Consequently a full coefficient table with k proportional to log(n) has
dimension proportional to (log(n))^(d-1) for fixed d. This only counts the
table; it gives no lower bound for arbitrary nonlinear or implicit decoders.
For example the sphere function sin(v^T x), for v in R^d, is exactly
represented by d real coefficients and one sine evaluation despite its
nonpolynomial spatial dependence. This example refutes the inference from
mode count to universal storage count; it is not proposed as a trained deep
network construction.

## 2. Full input rank removes the elementary rotational shortcut

Let the training inputs span a subspace of dimension r <= d. The orthogonal
transformations fixing every training input act arbitrarily on its orthogonal
complement and trivially on its span. Two sphere queries lie in the same orbit
exactly when their projections on the training span agree: their perpendicular
norms then agree automatically, and an orthogonal transformation maps one
perpendicular component to the other.

An invariant predictor can therefore be parameterized by its r training-span
coordinates. If r=d, the stabilizer is the identity and this observation gives
no dimension reduction. The assertion m >= d alone is not sufficient: repeated
or otherwise dependent samples can still have r < d.

For the Gaussian-initialized dense model this symmetry concerns the law of
the trained predictor, not each finite realization. Indeed replacing the first
matrix A by A R^T and the query x by R x leaves all first preactivations
unchanged. The orthogonal first-layer mobility and the loss preserve this
equivariance along the weight gradient flow, by the chain rule. The Gaussian
law of A is right-orthogonally invariant. An initialization-independent
deterministic limit, if established, inherits the invariance. A finite random
predictor need not itself be invariant. No population limit theorem is assumed
or proved here.

## 3. A finite-dimensional family need not have analytic-ball entropy

Let epsilon > 0. Let a family of functions in the complete trajectory norm be
the image of the parameter cube [-R,R]^p under an A-Lipschitz map, with R > 0
and A > 0, using the maximum norm
on the cube. Cover each coordinate interval by a grid with nearest-grid
distance at most epsilon/A. The images form an epsilon-net with at most

\[
\left(2+\frac{2RA}{\epsilon}\right)^p
\]

elements (enlarging a finite endpoint count if necessary). Thus the logarithm
of its covering number is at most
\(p\log(2+2RA/\epsilon)\). This direct grid proof uses no approximation-width
theorem.
If R=0 or A=0, the image is a single function and one center suffices.

For fixed architecture and activation, a deterministic population predictor
is specified by finitely many data coordinates and labels. If its solution
map on a bounded uniformly gapped data class were uniformly Lipschitz in the
complete trajectory norm, the preceding statement would apply, with at most
m(d+1) input parameters. This sentence is conditional: no such all-time
population solution map or Lipschitz theorem has been supplied in this study.
Even when it applies, the conclusion is about information/covering numbers,
not a finite autonomous evaluator. It does not bound the memory required to
compute or evolve a population predictor.

This identifies a second missing bridge in an analytic-ball no-go argument:
analyticity supplies a containing class, not an inclusion of a hard analytic
ball inside the actual trajectory family. The direction of inclusion matters.

## 4. Pairwise variability is not a code-size lower bound

Let F and its independent copy F' be random bounded complete trajectories,
with a measurable law in the supremum norm under consideration. Assume the
distance-ball indicator is measurable for the product of their laws, so that
Tonelli's theorem applies. This holds for separable metric-valued laws and for
continuous trajectories whose supremum can be taken over countably many dense
time/query evaluations. Suppose
\(\mathbb P(\|F-F'\|\le\epsilon)\ge1-\delta\).
Conditioning on F' shows that the average, over possible centers g=F', of
\(\mathbb P(\|F-g\|\le\epsilon)\) is at least \(1-\delta\).
Consequently there is a deterministic center g with

\[
\mathbb P(\|F-g\|\le\epsilon)\ge1-\delta.
\]

This is an existence statement about a function, not a compact construction.
The center can itself be a whole dense trajectory; generating, storing or
evolving it may cost the full dense size. Its significance is negative: the
mere fact that independent dense runs differ at scale epsilon does not imply
that epsilon-accuracy requires encoding their initialization randomness, nor
does it yield a lower bound on total storage. Any such lower bound must also
control the complexity of the center and the permitted decoder.

## Source and check status

The polynomial division, orbit classification, elementary covering argument
and averaging identity
are proved in full above. Source inputs are the task contract, docs/notation.qmd
and elementary algebra; no external theorem is used. The maintained book's
distinction between a future-trajectory encoding and an initialization-only
construction is also explicitly illustrated in
docs/07-observable-closure.qmd, section ending at equation
eq-docs-linear-dynamics-l1308.

Status: auxiliary proofs written and self-checked; independent reconstruction
is pending. No statement here establishes the requested size lower bound or
constructs the requested autonomous compressed model.
