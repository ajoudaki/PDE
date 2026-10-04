# Unit Gaussian moments: what improves, what cannot be called beta equals one

2026-10-04. Continuation of the activation/depth-constant investigation in
closure_sampling_20261003. The user explicitly confirmed the condition

\[
\mathbb E[\phi(Z)^2]=\mathbb E[(\phi'(Z))^2]=1,
\qquad Z\sim N(0,1).
\tag{1}
\]

No zero-mean condition on phi(Z) is imposed. The ultimate target remains
the all-time, whole-sphere, root-width comparison with the same canonical
finite dense network. No new all-time compression theorem or compression
lower bound is claimed in this note. The substantive new results are
exact activation constructions, initialization geometry, and a polynomial
complex moment radius for an explicit normalized erf activation.

## 1. The numerical floor is not a propagation gain

The old beta=max(10,B_0,B_1,B_2,16/a) combines different quantities.
The number ten dominates coarse initialized/real/complex Gaussian operator
tubes and absorbs universal numerical constants and layer sums. The 16/a
entry absorbs inverse complex strip radius when converting source counts
to powers of beta. Neither number states a physical amplification of ten
or sixteen at each layer. Removing their appearance by displaying those
constants separately is legitimate; deleting them from the inequalities
without a new proof is not.

There is even a redundancy in the Cauchy-based version: for B>=1,
max(10,32B/a^2)>=sqrt(320B)/a>16/a. Dropping that explicit last entry
does not change the maximum. With certified derivative bounds, however,
it can dominate, as in the old tanh certificate. The audit traces these
uses to their actual source and runtime inequalities.

There is a stronger obstruction to interpreting the same beta as one.
If a continuously differentiable activation satisfies (1) and
sup_R|phi'|<=1, then Gaussian full support forces |phi'|=1 everywhere.
Continuity fixes its sign, so phi=+/-x+b. The first equality in (1)
then forces b=0. Thus every normalized nonlinear activation has
sup_R|phi'|>1. A bounded such activation also has sup_R|phi|>1.
Consequently the existing supremum-based beta cannot equal one for a
nonlinear normalized activation, even if ten and 16/a were removed.

This is a statement about that definition and proof. It does not establish
that the optimal compression bound needs an exponential depth coefficient.
The relevant alternative is to replace products of supremums by actual
Gaussian and adaptive-response estimates, with their own named gains.

## 2. Bounded activation values can be removed, including for exact GELU

The existing qualitative extension replaces a bounded activation value by
a finite value at zero and a bounded holomorphic derivative on a strip.
Exact GELU g(z)=z Phi(z) satisfies that requirement. For any a>0,

\[
\sup_{|\operatorname{Im}z|<a}|g'(z)|
\le1+\frac{e^{a^2/2}}{\sqrt{2\pi}}(2a+e^{-1/2}).
\tag{2}
\]

This follows by integrating Phi vertically from the real axis and using
g'=Phi+z exp(-z^2/2)/sqrt(2pi). Identity also qualifies. These admissions
do not import the bounded-class numerical exponents or constants into
the qualitative extension.

Normalization itself is broadly achievable. For nonconstant smooth g
with bounded first two real derivatives, put

\[
\mu=\mathbb Eg(Z),\quad D=\mathbb Eg'(Z)^2,\quad
V=\mathbb E[g(Z)-\mu]^2.
\]

Gaussian integration by parts proves V<=D, with equality only for affine
g. Both activations

\[
\phi_\pm(z)=\frac{g(z)-\mu\pm\sqrt{D-V}}{\sqrt D}
\tag{3}
\]

satisfy (1). Thus this is not restricted to tiny outputs or nearly
constant activations. The proof and exact tanh, erf, GELU and unbounded
near-identity examples are in NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md.
Centering would force affinity, but centering is not part of the user's
condition or of the new nonlinear examples.

## 3. A concrete normalized erf with polynomial initialization depth costs

Use the same activation at every hidden layer:

\[
\phi(z)=\sqrt{\frac{\pi\sqrt3}{2}}\,
\operatorname{erf}(z/\sqrt2)
 +\sqrt{1-\frac{\pi}{2\sqrt3}}.
\tag{4}
\]

The scale is about 1.64945 and the offset about 0.30512. This smooth
monotone activation has unit feature second moment at every layer of
the initialized Gaussian recursion, and exactly

\[
\mathbb E\phi'(Z)^2=1,\qquad
\mathbb E\phi''(Z)^2=1/3.
\]

Two maps diagnose different perturbations. With correlated standard
Gaussians X,Y of correlation c, define F(c)=E phi(X)phi(Y); define
V(q)=E phi(sqrt(q)Z)^2 for q>=0. Direct Gaussian integration gives

\[
F(c)=1-\frac{\pi}{2\sqrt3}+\sqrt3\arcsin(c/2),
\qquad F(1)=F'(1)=1,
\]
\[
V(q)=1-\frac{\pi}{2\sqrt3}
 +\sqrt3\arcsin\!\left(\frac{q}{1+q}\right),
\qquad V'(1)=1/2.
\tag{5}
\]

Thus angular first-order propagation is critical while marginal variance
errors contract. These properties do not rely on vanishing forward norms.

For d>=2, the actual initialized width-n features on any fixed great-circle
query, at each fixed hidden depth L,

\[
\frac1n\|\partial_\theta h_n^{(L)}\|_2^2\ \longrightarrow\ 1,
\qquad
\frac1n\|\partial_\theta^2 h_n^{(L)}\|_2^2
\ \longrightarrow\ 1+L
\tag{6}
\]

in probability. No exponential depth factor appears in these limits.
Their complete finite-jet derivation uses conditional Gaussian rows,
not differentiation of an unsupported pointwise limit.

The analytic source question has an equally concrete answer. For a complex
preactivation U with E U^2=1 and E|U|^2=r, 1<=r<2,

\[
\mathbb E|\phi(U)|^2=F(r),\qquad
\mathbb E|\phi'(U)|^2=\frac{\sqrt3}{\sqrt{4-r^2}}.
\tag{7}
\]

On a complex great circle at imaginary angle tau, r_0=cosh(2tau) and
r_(j+1)=F(r_j). A direct comparison proves that |tau|<=1/(8 sqrt(L))
keeps these moments bounded through L layers and keeps the derivative
of the scalar moment recursion below exp(1/2). Conversely, finite
derivative moments through L>=2 layers require
|tau|<sqrt(7/[2(L-1)]). This establishes an L^-1/2 complex moment
radius with explicit constants. It is much larger than an exponential
radius, but it is not independent of depth.

At fixed m>=2 and pairwise distinct normalized inputs, the same activation
has initialized covariance gap gamma_L~6/L as L grows. The order of
limits is fixed depth followed by width infinity to define the covariance,
then depth growth of that deterministic covariance. This is not a joint
growing-depth finite-network statement.

## 4. What extends beyond this example

For a common activation satisfying (1), expand it in normalized Gaussian
Hermite polynomials. If p_k is the squared coefficient of degree k,
then sum p_k=sum k p_k=1 and the correlation map is F(c)=sum p_k c^k.
For finite chi_2=E phi''(Z)^2, the exact depth-L correlation map obeys

\[
(F^{\circ L})'(1)=1,\qquad
(F^{\circ L})''(1)=L\chi_2.
\tag{8}
\]

Its deterministic limiting sphere-feature map has first derivative norm
one and second derivative norm sqrt(1+3L chi_2). More generally every
fixed derivative order has polynomial depth dependence when its needed
Gaussian derivative moments are finite. This does not supply estimates
uniform over derivative order, as required by a summed response expansion.

An additional scoped gap bound is available if the input Gram itself has
positive smallest eigenvalue gamma_0:

\[
\gamma_L\ge\frac1{\gamma_0^{-1}+L\chi_2}.
\tag{9}
\]

That extra premise belongs only to (9); it is not imposed on the original
general compatible-data problem. The proof uses positive Hermite coefficients
and a Schur-power comparison, avoiding repeated multiplication by a fixed
gap contraction. For fixed nonaffine activation and m>=2 under this premise,
gamma_L~2/(chi_2 L). The normalized erf's asymptotic above also covers
distinct inputs whose input Gram is singular.

The two moments in (1) alone provide no uniform bound on chi_2, fourth
moments, or the complex strip norms. Explicit bounded analytic examples
in BETA_ENVELOPE_AUDIT.md keep both moments one while their actual
first-layer angular-tangent fourth moments diverge across the family.
These counterexamples attack an inference from the two moments, not
compression for well-controlled fixed activations.

## 5. Variance stability is a separate necessary diagnostic

For any of the smooth examples above, Gaussian integration by parts gives

\[
V'(1)=1+\mathbb E[\phi(Z)\phi''(Z)].
\tag{10}
\]

Therefore unit derivative second moment need not make marginal variance
perturbations stable. The normalized positive-offset exact GELU is

\[
\phi_+(z)=\frac{z\Phi(z)+b_+}{\sqrt D},
\quad D=\frac13+\frac2{3\pi\sqrt3},
\]
\[
b_+=-\frac1{2\sqrt\pi}
 +\sqrt{\frac1{4\pi}+\frac1{6\pi\sqrt3}}.
\]

It satisfies (1) but V'(1)=1.1134920638...>1. The negative root for the
offset gives V'(1)=0.4971840106... in (0,1). Both signs and values follow
from exact Gaussian integrals. The conditions (1), |V'(1)|<1 and controlled
higher/complex Gaussian moments are therefore a much more informative
initialization criterion than beta=1. The normalized erf meets these
tests with explicit small numbers. No sufficiency theorem for all-time
compression is asserted for this proposed criterion.

This diagnostic also controls an actual finite-network fluctuation. For
a fixed query, let q_(n,L)=n^-1 sum_i h_i^(L)^2 at initialization, and
sigma^2=Var(phi(Z)^2). The complete finite-network proof in
NORMALIZED_VARIANCE_FLUCTUATIONS_ROUTE.md establishes, for the GELU
branches and normalized erf,

\[
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L})
 =\sigma^2\sum_{j=0}^{L-1}[V'(1)]^{2j}.
\tag{11}
\]

The proof uses the exact conditional Gaussian transition law, a conditional
characteristic-function expansion, and uniform integrability. It is not
a heuristic substitution of the population law into a finite trained model.
For each fixed depth, the positive-offset GELU coefficient therefore grows
exponentially as depth subsequently grows, whereas the negative branch is
bounded. This rules out a polynomial-depth bound for this initialized
feature-norm fluctuation coefficient under only the two moment conditions.
It does not give an output or compression lower bound.

For the erf in (4), put alpha=pi/(2 sqrt(3)). Since erf(Z/sqrt(2)) is
uniform on [-1,1], its exact innovation variance is
sigma^2=4 alpha-(16/5)alpha^2. Its finite-network variance limit is

\[
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L})
 =\frac43\left(4\alpha-\frac{16}{5}\alpha^2\right)(1-4^{-L}).
\tag{12}
\]

Thus this initialized fluctuation coefficient is uniformly bounded in depth
as well as the first tangent coefficient, while higher tangents and complex
query resolution have the explicit polynomial costs already described.

## 6. What remains open in the original task

During training a query tangent J at a hidden layer satisfies a recursion
containing W[phi''(z) dot(z) J]. In the actual mean-square-loss flow,
dot(z)=-(2/m)sum_a r_a R_a, where R_a is the residual-free parameter
response in the original mobility. One must therefore control the actual
mixed normalized RMS of phi''(z) R_a J, together with its repeated
responses. Neither marginal normalization at a Gaussian input nor the
initialized covariance identities bound that adaptive product.

Training also reuses Gaussian mixers, so the independent-row argument at
initialization is no longer available without an insertion comparison.
The entire response-order summation and the corrected-readout stability
must be checked with any improved gains. These are the exact remaining
obligations; they are not assumed as new hypotheses and then called a
solution.

The proved evidence favors studying polynomial depth dependence for
normalized, variance-stable activations. It does not prove the old bounds
with beta=1, and it does not show that every exponential depth factor in
the optimal all-time compressor is necessary. Existing all-time numerical
claims are unchanged.

## 7. Evidence and status

The source proofs are CRITICAL_NORMALIZATION_GEOMETRY_ROUTE.md,
NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md, BETA_ENVELOPE_AUDIT.md, and
NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md, followed by
NORMALIZED_VARIANCE_FLUCTUATIONS_ROUTE.md. The coordinator read all five in
full and reconstructed the independently authored routes in
NORMALIZED_ACTIVATION_ASSEMBLY_CHECK.md. The root-authored erf calculation
has a complete separate check in NORMALIZED_ERF_COMPLEX_GAIN_CHECK.md,
including its finite-width moment bridge. The activation examples and beta
audit also have the complete cross-route reconstruction
NORMALIZED_ACTIVATION_COMPONENT_CHECK.md. These are internal study checks,
not promotion reviews. Frozen hashes and exact scopes are in the reports.

The current canonical dense target, fixed dataset, physical clock and
same-width comparison remain the scientific contract. No clipping, learned
normalization operation, residual architecture, or changed matrix law was
inserted into a theorem about the original model. Output offsets in the
activation examples are explicit choices of activation. No trained-network
experiment, manuscript edit, Git mutation or concurrent-work reset was made.
