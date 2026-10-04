# Activation classes and automatic initialization gaps

2026-10-03. Coordinator derivation for the fixed-depth extension of the
same-width theorem. This note proves the initialization and symmetry
statements below and specifies a wider class for the finite insertion
proof. It does not by itself prove the deeper finite probability bound.
Inputs: current manuscript initialization, model and closure definitions;
the study's DATA_QUOTIENT_CLOCK/CHECK and Q_ORDER_POSITIVE_ROUTE with its
checks. No other study, experiment, manuscript edit, or Git operation.
Section 5 extends the initialization conclusions to the now-checked
finite-insertion class with unbounded activation values.

## 1. A smooth bounded class

Let a scalar activation belong to the class
\[
 \phi\in C^3(\mathbb R),\qquad
 \max_{0\le j\le3}\|\phi^{(j)}\|_\infty<\infty,
 \qquad \phi\ \hbox{nonconstant}.
 \tag{1}
\]
The convention phi^(0)=phi includes bounded values. Layer-dependent
activations may have different finite bounds; depth is fixed. Bounded
nonconstant functions are nonpolynomial. No monotonicity, analyticity,
positive derivative, or positive homogeneity is imposed.

Examples are tanh, arctan, erf, logistic sigmoid, sin, cos, and exp(-s^2).
For erf and exp(-s^2), each of the relevant derivatives is a polynomial
times exp(-s^2), hence bounded. Arctan derivatives are bounded rational
functions. Logistic derivatives are polynomials in sigma(s) in (0,1),
and tanh derivatives are polynomials in tanh(s) in (-1,1). Trigonometric
derivatives are bounded. Each displayed example is nonconstant.

The deterministic all-depth comparison in DEPTH_TRACKING_ROUTE.md only
needs bounded slopes and Lipschitz derivatives, and allows unbounded
values. The proposed finite reinsertion proof uses bounded values to
bound deleted activations, the coordinatewise readout, and learned omitted
columns; its Taylor remainders and response time nets use the first three
derivatives. Thus (1) is a sufficient class for that proof, not a claimed
minimal activation hypothesis.

## 2. A Gaussian feature lemma with singular preactivation covariance

Let u_1,...,u_m be nonzero pairwise nonproportional vectors in a finite
Euclidean space, let G be a standard Gaussian in that space, and let
psi be continuous and nonpolynomial. Suppose psi(G^T u_a) is square
integrable for every a. Then the uncentered feature covariance
\[
 Q_{ab}=\mathbb E[\psi(G^\top u_a)\psi(G^\top u_b)]
 \tag{2}
\]
is positive definite.

If c^TQc=0, continuity and Gaussian full support imply
sum_a c_a psi(u_a^T x)=0 for every x. Fix an index a with c_a not zero.
For each b not equal to a, pairwise nonproportionality supplies a vector
v_b perpendicular to u_b but not perpendicular to u_a. Apply finite
differences with arbitrary steps in all directions v_b. Every summand
other than a is eliminated. Varying the base point and steps yields
\[
 \Delta_{s_1}\cdots\Delta_{s_{m-1}}\psi(t)=0
 \quad\hbox{for all }t,s_1,\ldots,s_{m-1}.
\]
For m>=2, convolve with a compact smooth approximate identity and
differentiate in all the steps at zero. Every mollification is a
polynomial of degree at most m-2. Interpolation at m-1 fixed distinct
points shows convergence of its coefficients; local uniform convergence
of the mollifications then makes psi itself such a polynomial, a
contradiction. For m=1, nonzero u_1 gives a scalar Gaussian of full
support, and a nonzero continuous nonpolynomial psi has positive
uncentered second moment.

This lemma applies to any positive semidefinite covariance C for which
some Gram representation C_ab=u_a^T u_b has nonzero pairwise
nonproportional vectors. C itself need not be positive definite.
The representation follows by taking rows of a square root and deleting
zero ambient directions. This observation is useful for antipodal data.

If C is positive definite, a weaker activation hypothesis suffices for
the next layer: any continuous nonconstant psi with finite Gaussian
second moments preserves positive definiteness. A null combination
sum_a c_a psi(Z_a)=0 for Z~N(0,C) holds everywhere by full support.
Varying a single coordinate gives c_a=0 for every a.

## 3. Same activation at every hidden layer: all sphere geometries

Use any fixed depth L>=2, the canonical independent Gaussian initialization,
and the same activation phi satisfying (1) in every hidden layer.
Inputs have norm sqrt(d), and v_a=x_a/sqrt(d) are unit vectors.
Repeated identical inputs can first be combined with their positive sample
weights when their labels agree. The remaining antipodal issue depends
on phi's actual parity.

### 3.1 Odd activations

If phi(-s)=-phi(s), forward evaluation gives f(-x)=-f(x) for every
parameter state. Its derivative is even, and the exact signed quotient in
DATA_QUOTIENT_CLOCK applies at every depth. Antipodal class labels must
have opposite signs and equal magnitude for interpolation to be possible.
One representative per class is a collection of nonzero pairwise
nonproportional unit vectors. The lemma in Section 2 makes its first
feature covariance positive definite; later layers preserve it.
Positive class weights preserve the gap.

Thus no independent initialization-Gram assumption is needed for each
fixed compatible sphere dataset in this class. It includes tanh,
arctan, erf, and sin.

### 3.2 Even activations

If phi(-s)=phi(s), the first hidden feature obeys h^(1)(-x)=h^(1)(x).
All later hidden features and the output therefore agree at antipodes.
Compatible labels are equal on each antipodal class.

The quotient is exact for both trained systems, not only for initialized
features. For an antipodal input, the first gate changes sign because
phi' is odd. Its first backward response and input both change sign,
so their outer product in the read-in update is unchanged. At every
hidden link ell>=2, forward and backward responses agree within the
class. The stored forward moments agree, and the class average of
backward moments gives the weighted reconstruction. The residual RMS
and hence original clock are preserved under compatible labels.

The representative inputs are pairwise nonproportional. The same
positive-covariance lemma and propagation prove the quotient Gram gap.
This class includes cos and exp(-s^2). The feature evolution need not
be monotone for the covariance argument or the comparison proof.

### 3.3 Activations that are neither even nor odd

For such a phi, no antipodal identification is needed. In fact the
limiting feature covariance is positive definite by the second hidden
layer for every finite collection of distinct sphere inputs.

To prove it, consider the first-layer feature functions in Gaussian L2,
\[
 U_a(G)=\phi(G^\top v_a).
\]
Each is nonzero. Two such functions cannot be proportional. If v_a,v_b
are nonparallel, the map x -> (v_a^T x,v_b^T x) is onto R^2.
Proportionality and Gaussian full support would imply phi(s)=c phi(t)
for every s,t, forcing phi to be constant. If v_b=-v_a,
proportionality instead says phi(-s)=c phi(s) for every s, with c
nonzero. Applying it twice gives c^2=1 because phi is not identically
zero; c=1 or -1 would make phi even or odd, respectively.

Consequently the finite family U_a has a Gram representation by
nonzero pairwise nonproportional Euclidean vectors, even if its first
covariance is singular. The second-layer activation phi is
nonpolynomial, so Section 2 makes the second covariance positive
definite. All subsequent nonconstant layers preserve it.

For logistic sigmoid this handles every finite set of distinct sphere
inputs, including antipodal pairs, with arbitrary sufficiently small
labels. Duplicate inputs still require equal labels. There is no
odd-output constraint for this activation.

## 4. Layer-dependent variants and quantitative qualifications

For arbitrary layer-dependent nonconstant activations in (1), the
manuscript's nonproportional-input criterion makes the first covariance
positive definite and all later covariances stay positive definite.
Thus every finite nonzero pairwise nonproportional input configuration
is covered, without requiring orthogonality or linear independence.

The sphere geometry can be more general in the following cases.

- If every activation is odd, the signed quotient of Section 3.1 works.
- If the first activation is even, the unsigned quotient of Section 3.2
  works regardless of the parity of later activations.
- If the first activation is neither even nor odd, Section 3.3 makes
  its first feature vectors pairwise nonproportional on distinct sphere
  inputs. Any nonconstant bounded second activation is nonpolynomial,
  so the second covariance is positive definite. Later activations
  need only be nonconstant for its preservation.

These are sufficient cases, not an exhaustive classification of mixed
parities. For remaining architectures one should state the actual
limiting feature-Gram condition rather than invent a quotient. For
example, an odd first activation followed by an affine shift of an odd
top activation can give additional relations among several antipodal
pairs; absence of a simple odd/even output symmetry does not itself
prove a full feature Gram.

The strictly positive covariance gap is a fact for each fixed compatible
dataset. It is not uniform over datasets whose distinct inputs approach
coincidence. The allowed small-label threshold and all comparison
constants may depend on this fixed gap, activation bounds and fixed depth.
Finite-width Gram concentration follows by the manuscript's conditional
law-of-large-numbers induction, whose bounded-value hypotheses hold here.

ReLU and leaky ReLU fail the required gate regularity. Softplus, GELU and
SiLU have unbounded values and are outside (1); Section 5 covers them
using the separately completed joint-budget insertion argument.

## 5. Unbounded values with bounded first three derivatives

The larger sufficient class is
\[
 \phi\in C^3(\mathbb R),\qquad
 \max_{1\le j\le3}\|\phi^{(j)}\|_\infty<\infty,\qquad
 \phi\ \hbox{nonaffine}.
 \tag{8}
\]
The finite carrier proof requires only the derivative conditions and an
initial Gram gap; nonaffinity is used here to establish that gap
automatically for the stated data classes. The finite-insertion extension
is proved in UNBOUNDED_ACTIVATION_CANDIDATE.md, with local and probability
reconstructions identified there. It uses a joint forward/backward
supremum budget, including the top readout, rather than assuming bounded
activation values.

Bounded slope gives
\[
 |\phi(s)|\le|\phi(0)|+\|\phi'\|_\infty |s|.
\]
All Gaussian moments needed in Section 2 are therefore finite.
A polynomial with bounded derivative on the real line has degree at
most one. Thus a nonaffine function in (8) is nonpolynomial, exactly as
required by the ridge-independence lemma.

Every initialization and quotient proof above consequently extends as
follows. Pairwise nonproportional nonzero inputs have a strictly positive
first feature covariance when the first activation satisfies (8).
Every subsequent nonconstant continuous activation of at most linear
growth preserves that positive covariance. For the same activation (8)
at all hidden layers, the odd, even, and neither-parity alternatives of
Section 3 apply to all fixed sphere configurations, with the same
compatibility rules. The neither-parity case gives a positive second
feature covariance even when the first one is singular.

To verify the latter assertion, the first-layer feature vectors
\(\phi(G^\top v_a)\) belong to Gaussian \(L^2\) by linear growth.
The proof that two such vectors cannot be proportional uses only
continuity, nonconstancy, Gaussian full support, and the exclusion of
even/odd parity. It never uses bounded activation values. The second
layer ridge argument then applies because (8) is nonpolynomial.
For layer-dependent activations, the sufficient cases in Section 4
remain valid when each use of “nonconstant bounded” to obtain
nonpolynomiality is replaced by “nonaffine with bounded slope.”

Finite initialized feature covariance convergence also persists.
Conditionally on the preceding covariance in a bounded set, linear
growth gives uniform Gaussian fourth moments. Conditional laws of large
numbers and continuity in covariance prove the same finite-depth
induction, including at singular preceding covariances. This establishes
the initialization gap in probability; it does not assert unstopped
exponential moments for finite deep products of Gaussian matrices.

For explicit examples in the larger class, write
\(\sigma(s)=(1+e^{-s})^{-1}\), and let \(\varphi,\Phi\) denote the
standard Gaussian density and distribution function.

- **Softplus:** \(\phi(s)=\log(1+e^s)\).
  Its first three derivatives are
  \(\sigma\), \(\sigma(1-\sigma)\), and
  \(\sigma(1-\sigma)(1-2\sigma)\), hence bounded.
- **GELU:** \(\phi(s)=s\Phi(s)\).
  Its derivatives are
  \(\Phi(s)+s\varphi(s)\), \((2-s^2)\varphi(s)\), and
  \((s^3-4s)\varphi(s)\), hence bounded.
- **SiLU:** \(\phi(s)=s\sigma(s)\).
  Its derivatives through order three are
  \(\sigma+s\sigma'\), \(2\sigma'+s\sigma''\), and
  \(3\sigma''+s\sigma'''\). Each \(\sigma^{(j)}\), \(j\ge1\)
  appearing here decays exponentially in both tails; these expressions
  are bounded.

All three are nonaffine and neither even nor odd. Using any one of them
at every layer, with at least two hidden layers, therefore covers any
fixed distinct sphere inputs, including antipodal pairs. Duplicate
inputs still require equal labels. Arbitrary small fixed label vectors
on those distinct inputs are allowed.

This does not include ReLU or leaky ReLU, does not make constants uniform
under a smoothing parameter tending to zero, and does not remove the
small-label or fixed-depth qualifications of the training theorem.
