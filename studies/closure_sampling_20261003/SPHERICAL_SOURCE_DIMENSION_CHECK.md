# Reconstruction of the intrinsic spherical source refinement

2026-10-04. Checker: root coordinator. This is an internal mathematical
reconstruction, not an independent promotion review. I authored the separate
Euclidean-angle route and suggested the broad sphere route, but did not see
this candidate until it was frozen. The spherical author wrote its proof
independently of my new route. No numerical experiment was used.

Checked candidate: `SPHERICAL_SOURCE_DIMENSION_ROUTE.md`, SHA-256
`bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8`.
I read the complete 662-line candidate and reconstructed its geometry,
directional insertion substitution, harmonic coefficient estimate, finite
initialization-only construction, inventory and all-time theorem interface.
The verdict is **PASS within the inherited study source/insertion/runtime
scope**. This is not a fresh proof or promotion of every older cavity input.

## 1. Source extension and its actual dependencies

For q=u cos(z)+v sin(z), with real orthonormal u,v, the real and imaginary
parts after a real rotation have lengths cosh(Im z), sinh(Im z) and are
orthogonal. Conversely q^Tq=1 gives those identities, so the stated tube
contains exactly the specified complex quadric neighborhood. Its query
path has one imaginary segment of length at most r. Every fixed z
derivative has norm at most exp(|Im z|). These facts remove an angular
triangle inequality without changing the neural forward or backward pass.

I checked the substitution in the old augmented graph directly. Replacing
partial_theta v by q'(z) leaves the following unchanged or smaller:

- the RMS forward directional recurrence, starting from a first-weight
  operator bound 10 and input derivative norm at most two;
- the mixed first-layer map U_A q', with squared Hilbert--Schmidt norm
  n||q'||^2, hence normalized bound two;
- the hidden mixed map U_H partial_z h/sqrt(n), whose normalized
  Hilbert--Schmidt norm is the RMS of partial_z h;
- the gate-curvature term diag(phi'' J)D_Theta z, which requires only
  RMS J and a bounded forward parameter operator;
- the omitted-root source x_i partial_z h_i, with no new force in the
  trained system and no direct reverse-observable term.

Thus the asymmetric endpoint bound T_J=8 f_* E_J is the old one. The
Gaussian source, learned-row correction and same-root integral have the
same three coefficients. Doubling G_d doubles at most each U_j,V_j:
their formulas contain G_d linearly and do not iterate U_j or V_j.
The fixed RMS/mixed constants appearing in those formulas do not depend
on G_d. This checks the specific factor two in equation (13), rather
than assuming it from a qualitative source theorem.

The frame is a subset of a bounded 2d-dimensional Euclidean box. A mesh
of size n^-2 has at most C_d n^(4d) frame points. The three real
time/tube coordinates add at most n^7, since T<=n eventually. After
neurons and fixed multiplicities the exponent 4d+10 is sufficient.
The Gaussian tail at 16sqrt(d+3)sqrt(log(en)) has exponent
64(d+3), strictly larger than 4d+10. The extra frame net therefore
changes no persistent response coefficient beyond the displayed factor.

For off-grid continuation, nearby orthonormal two-frames can be connected
by normalizing their straight interpolation. Its Gram stays near I, so
the normalization and its fixed derivatives are bounded. Differentiating
the query/response graph in the frame entries gives fixed-size input
variations of norm O(1). The operator and stopped diagonal bounds give
sqrt(n) times a fixed polylogarithm for their coordinate derivatives;
mesh n^-2 errors vanish. A full new coordinate maximum theorem for each
frame derivative is not required. The direct controls remain functions
of a one-dimensional time contour, so their insertion-net entropy and
strict n powers remain the old ones.

The budget is still a training-carrier budget; it has no passive-query
index. Thus angular geometry does not alter its moment closure. Each
cavity uses its own retained initialization and doubled stops. The
comparison transfers the full prefix to these stops, and the displacement
3a/128 closes the pole stop. These are the same source-interface
requirements verified in the supplied DEEP_ACTIVATION_EXTENSION and
DEPTH_INDEPENDENT_EXPONENT proofs, with the displayed bounded input
derivative substitution. No finite-to-population estimate is used.

Both inverse radii are bounded by beta^(32L)sqrt(d+3), including
the largest time coefficient 64 beta^(30L+1). The inequality holds
already at beta=10,L=2. Neither radius requires a new label cap.

## 2. Harmonic approximation reconstructed

The homogeneous harmonic decomposition follows by applying the Laplacian
to |x|^(2k)H_l and solving successively for its nonzero scalar
coefficients. Its dimension is the difference of two monomial counts.
Pascal's identity then gives h_j<=2 binom(j+d-2,d-2), also for j=0.
For d=2 the dimensions are one at degree zero and two otherwise.

The projection kernel diagonal equals h_j by rotational invariance and
its integral trace. Cauchy--Schwarz bounds its absolute value by h_j,
so the sup-norm projection estimate used in (18) is valid with normalized
sphere measure.

The spherical mean A_z is bounded on the complex tube because real
rotation of the frame removes Re z. On a harmonic polynomial the tangent
rotation average is its unique zonal harmonic times its value at the
base point. The harmonic equation yields the Gegenbauer ODE, including
the normalization at one. For real z, the pair distribution is symmetric,
so the spherical mean is self-adjoint. Testing against each real harmonic
and analytically continuing z proves the projection multiplier identity
without a possibly divergent expansion at complex points.

At cosh r the Gegenbauer generating function factors into two positive
coefficient series. Retaining the leading e^(rj) term gives a valid lower
bound on the multiplier. The ratio (2nu)_j/(nu)_j is bounded by a
polynomial in j for fixed d by summing log(1+nu/(nu+k)); the candidate's
2^d(j+1)^d envelope is conservative. Multiplying by h_j gives (25).
For the circle the multiplier cosh(jr) proves the separately stated
bound directly. Consequently all harmonic coefficients have a summable
tail. Harmonic decomposition and density of polynomial restrictions on
the sphere show the reconstructed function equals the original continuous
source; the stated real Stone--Weierstrass hypotheses are satisfied by
the real coordinate-polynomial algebra.

The joint time Fourier and spherical decay is valid because a shifted
time contour stays in the time rectangle at every fixed complex query.
The two tail sums are bounded by 6/alpha and
3 b_d! (2/r)^(b_d+1), respectively. Splitting the omitted exponential
into halves therefore gives precisely P and H in (28), with error
epsilon/16. The resulting series is uniformly convergent on the entire
real sphere and time interval, not merely almost everywhere.

The exact retained count is sum_j h_j(1+floor((H-rj)/alpha)). Bounding
h_j by twice the number of nonnegative (d-1)-tuples of sum j reduces
the count to one weighted d-simplex. The disjoint cube enlargement
adds alpha+(d-1)r and gives its volume divided by d!, with factor two.
This is why no 2^(d-1) sign factor or product-angle radius occurs.

## 3. Construction, inventory, and arithmetic

Finite harmonic quadrature and finite initial-jet continuation are linear
scalar operations. Applying exactly the same operations to both members
of each initialized image pair preserves W_0 or W_0^T exactly. Choosing
coefficient accuracy using N max_j sqrt(h_j) controls the full query
error; this multiplier affects setup accuracy, not retained rank. The
harmonic basis is a device to produce source vectors during setup. The
existing runtime evaluates selected neurons and learned arrays, not a
stored spherical polynomial evaluator. No trajectory table or original-n
coefficient array remains in the final inventory.

I checked the logarithmic cutoff formula before simplification:
alpha^-1 contributes ell_n^(3/2), and r^-(b_d+1) contributes
ell_n^((2d-1)/2). Their product is ell_n^(d+1). Thus (32) and
all three explicit eventual requirements (33) have the stated exponents.
They imply H<=7ell_n and lattice radius <=9ell_n. The actual inverse
radius product remains in the retained count. The width threshold is
not asserted uniform in growing dimension.

Multiplying N by four, substituting the inverse radii, and using
1024*9^d<=beta^(2Ld) gives the rank in (1), with slack. For d=1 the
two separate sphere points reproduce its factor two. The additions
2m+d+1 must stay explicit because the factorial term decays with d;
the candidate does so. Squaring with (a+b)^2<=2a^2+2b^2, applying
the retained runtime inventory, and converting lambda^-2 to
B^4(m/gamma)^2 prove (35)--(36). The numerical inequality
2040(L+1)B^4<=beta^(10Ld) holds for beta>=10,L>=2,d>=1.

For a_d=(d+3)^d/(d!)^2, direct values at d=1,2,3,4 are
4,25/4,6,2401/576. The ratio at successive d is bounded by
3(d+4)/(d+1)^2<1 for d>=4. Hence the uniform upper bound 25/4
is correct. The bound d!>=(d/e)^d also gives
a_d<=e^3(e^2/d)^d. Neither calculation removes the separate
beta^(82Ld) coefficient. Maximizing that coefficient over d would
create a doubly exponential depth coefficient; it is not an improvement
uniform in both parameters.

The source accuracy is still 1/n, its coordinate magnitude remains
M_0 sqrt(n), and the true training-carrier coefficient is unchanged.
The supplied runtime result therefore gives the same strict root-width
error at equal physical times, with the same fitting and endpoint
convergence. It is an interface composition, not a new population
comparison. No extra condition on data rank, orthogonality, labels or
activation has been added.

## 4. Frozen scientific dependencies and limitations

Hashes inspected/reconciled for the mathematical interfaces:

| File | SHA-256 |
| --- | --- |
| DEEP_COMPLEX_SOURCE.md | 7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2 |
| DEEP_ACTIVATION_EXTENSION.md | b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141 |
| WHOLE_QUERY_RESPONSE_SOURCE.md | 9222c93f0bb9d0c6943f86192cc4a8ad1bbb6b3f6199dd2b056b15fc3adec0d4 |
| DEPTH_INDEPENDENT_EXPONENT.md | 73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda |
| EXPLICIT_SOURCE_CONSTANTS_ROUTE.md | d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a |
| LABEL_DEPTH_RESCALING_ROUTE.md | d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1 |
| DIMENSION_PREFACTOR_OPTIMIZATION.md | 8e149122bcd83a8f64bceba97a6617f644f10e59fd97456f3cfa0e10273c8f2e |
| ARCHITECTURE_CONSTANT_REFINEMENT.md | b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7 |
| DEPTH_CONSTANT_SEPARATION.md | 6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f |

The check was manual algebraic reconstruction, with shell reads and hashes;
there is no experiment or formal proof assistant. The earlier complete
source reads were reused where hashes were unchanged, and the changed
source hypotheses and exact augmented-graph sections were reread. No
unrelated study was inspected. All statements remain internally checked
research results, not established-book claims. The numerical gain does
not settle polynomial dependence on d or L and does not give practical
large-dimension width thresholds.
