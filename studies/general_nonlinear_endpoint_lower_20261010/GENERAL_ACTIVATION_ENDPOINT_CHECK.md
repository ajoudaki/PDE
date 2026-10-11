# Adversarial reconstruction of the full activation-class extension

2026-10-11. Internal coordinator audit; not an independent promotion review.

**Verdict: PASS.** The Gaussian-oracle endpoint theorem extends from the
previous GELU/SiLU statement to arbitrary layerwise nonaffine activations in
the compact paper's analytic class. The generalization changes only fixed
activation-dependent constants. It does not change the network, label cap,
query geometry, endpoint, confidence quantifier, or root-width exponent.

## Frozen inputs

The audit reconstructed the activation-dependent steps in the following
bytes. The older check reports remain relevant only to the unchanged parts
of the oracle, source, conditioning and transfer arguments.

| Input | SHA-256 |
|---|---|
| `GAUSSIAN_ORACLE_ENDPOINT.md` | `8088619ca61fadf70871f3f96af907602097acc3a74f7b3ca742f6a553dfba3d` |
| `GELU_SILU_FLOW_ROUTE.md` | `f3b33474289c38cc38bfbb9eeb90d5aed7652b7a025f4c3171f11e5140908c1c` |
| `GELU_SILU_PROJECTED_SCALAR.md` | `65571cb900e1ba791f56a95a78b00ef72c6d4a43954d6c8e8602bc5f4e45c5f2` |
| `GELU_SILU_PROJECTED_INNOVATION.md` | `4ddb7d8ff0c6a7235bbf8292e565d08525bba70bd39ea3393292987f861417e4` |
| `NONODD_MOMENT_ROUTE.md` | `882de8bf0e33e7d7c6a62cb1afd29d633531ccc7a6b4cdb1942cccef98c4fa93` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |

## 1. Exact activation assumptions

For each layer, the paper assumes that the activation is real on the real
axis, holomorphic on one common horizontal strip, and has bounded first
derivative there. The paper's definition of \(\beta\), together with
Cauchy's formula on the smaller strip, gives finite constants

\[
 c=|\phi(0)|,\qquad
 s=\sup_{x\in\mathbb R}|\phi'(x)|,\qquad
 t=\sup_{x\in\mathbb R}|\phi''(x)|.
\]

The mean-value theorem gives \(|\phi(x)|\le c+s|x|\). Thus every use of
bounded GELU/SiLU derivatives and their former special growth bound has a
valid class-wide replacement. No boundedness of \(\phi\) follows or is
used.

The theorem adds one activation condition: every layer activation is
nonaffine. This implies nonconstancy at the intermediate layers. It is not a
centering, oddness, normalization, monotonicity, sign or named-family
condition.

## 2. Intermediate-layer innovation

Let \(G\) be standard normal. For any nonconstant continuous \(\phi\),

\[
 \operatorname{Var}(\phi(a+\sigma G))>0\qquad(\sigma>0).
\]

If the variance vanished, \(\phi(a+\sigma G)\) would be constant almost
surely. Continuity and the full support of the Gaussian law would make
\(\phi\) constant on \(\mathbb R\). Coupling all variables with the same
\(G\), the Lipschitz estimate gives continuity of this variance in
\((a,\sigma)\). Hence its minimum is positive whenever \(a\) and \(\sigma\)
range over a compact set with \(\sigma\) bounded away from zero.

At the first layer put

\[
 \nu_1=\operatorname{Var}(\phi_1(G))>0,
 \qquad H_1=|\phi_1(0)|+2s_1,
 \qquad \kappa_1=\nu_1/32.
\]

For a removed subspace of rank at most \(r_n=o(n)\), the projected feature
has second moment at least \(\nu_1(n-r_n)\). Its norm is
\(s_1\)-Lipschitz. Gaussian Poincare and Chebyshev therefore give

\[
 \Pr\left\{\frac{\|(I-Q_1)\phi_1(G_n)\|^2}{n}<\kappa_1\right\}
 \le \frac{16s_1^2}{\nu_1n}
\]

for all sufficiently large widths. The independent event
\(\|G_n\|\le2\sqrt n\) gives the upper bound \(H_1\).

Suppose the preceding feature has RMS at most \(H_{j-1}\), and its fresh
component has squared RMS at least \(\kappa_{j-1}\). If the known matrix
part has operator norm at most \(a\), define

\[
 H_j=|\phi_j(0)|+s_j(a+2)H_{j-1}
\]

and minimize \(\operatorname{Var}(\phi_j(b+\sigma G))\) over

\[
 |b|\le2aH_{j-1}+1,qquad
 \sqrt{\kappa_{j-1}/2}\le\sigma\le H_{j-1}.
\]

The preceding compactness argument makes this minimum positive. The
one-layer projected-Gaussian lemma then gives the next positive innovation
constant. Gaussian Poincare also bounds that minimum above by
\(s_j^2H_{j-1}^2\); therefore the recursively defined lower scale never
exceeds the next upper scale. The induction is well-defined at every fixed
depth, and its total failure probability is \(O(1/n)\). This reconstructs
the only depth step formerly using the identities
\(|\phi(z)|\le|z|\) and \(\operatorname{Var}\phi(G)\ge1/4\).

## 3. Final-layer nonlinearity

For bounded \(a\) and \(0<\sigma_-\le\sigma\le\sigma_+\), define the
Hermite energy above degree one by

\[
 d(a,\sigma)=\operatorname{Var}(\phi(a+\sigma G))
 -\bigl(\mathbb E[G\phi(a+\sigma G)]\bigr)^2.
\]

This is the squared Gaussian \(L^2\) norm after removing Hermite degrees
zero and one. If it vanished, \(\phi(a+\sigma x)\) would agree almost
everywhere with an affine function of \(x\). Continuity and full Gaussian
support would make \(\phi\) affine on \(\mathbb R\), contradicting the sole
added activation condition. Lipschitz Gaussian domination makes
\(d(a,\sigma)\) continuous, so it has a positive minimum on every compact
parameter rectangle used by the endpoint proof.

The rest of the scalar lemma needs only the finite bounds on \(s\) and
\(t\). Its covariance argument uses the positive Hermite tail just proved;
its Stein estimate uses the bounded gradient and Hessian. The generic
linear-growth estimate also supplies the feature upper bound. Arbitrary
conditioned means, unbounded activation values, a sublinear projection rank
defect and the existing empirical readout fourth moment remain allowed.

## 4. Assembly and adversarial checks

Section 6 of `GELU_SILU_FLOW_ROUTE.md` already states and proves its finite
oracle integrator for the paper's whole activation class. The fitting,
analytic-source and readout-moment inputs also use that class. Exact adaptive
Gaussian conditioning is activation-independent. Replacing the two former
named-family constants by Sections 2--3 above therefore leaves every other
interface unchanged.

The following possible loopholes were checked explicitly:

1. **Almost affine is not affine.** The positive constants can become
   arbitrarily small as an activation approaches an affine function, but the
   activation is fixed before \(n\to\infty\). The theorem permits the
   coefficient and onset width to depend on it.
2. **A nonzero uncentered moment is insufficient.** The proof uses centered
   variance at intermediate layers and degree-at-least-two Hermite energy at
   the final layer; both are strictly positive for the stated reasons.
3. **Unbounded values cause no gap.** Bounded derivative gives linear growth,
   which is enough for every Gaussian moment and upper-RMS estimate used.
4. **Conditioned biases may be large coordinatewise.** The scalar lemma
   retains its mean-RMS truncation plus empirical fourth-moment argument; it
   does not require a coordinatewise bias bound.
5. **The fresh final Gaussian is not conditioned away.** The assembly stops
   the lower-layer exposure before the final Gaussian and applies the scalar
   lemma uniformly in the resulting center.
6. **Affine activations really are excluded for a reason.** For an affine
   final activation the higher-Hermite constant is zero, so this proof cannot
   claim a nonlinear endpoint fluctuation. No weaker notion of nonlinearity
   is silently substituted.

Consequently, for the proper-training-span geometry and a fixed orthogonal
query, every fixed confidence \(1-\delta\) admits a fixed
\(C>0\), independent of width, such that two independent actual fitted dense
runs differ by at least \(C/\sqrt n\) at all sufficiently large individual
widths. The original label cap is unchanged. The audit does not extend this
theorem to full-span training data, make the onset width quantitative, or
promote it into the paper or book.
