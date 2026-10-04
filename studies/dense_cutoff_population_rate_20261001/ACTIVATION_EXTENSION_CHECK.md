# Check of activation classes, feature gaps, and exact parity quotients

2026-10-03. Internal collaborator reconstruction, not a promotion review.
The complete checked source is ACTIVATION_EXTENSION_ROUTE.md at SHA-256
82f3d3a747b2a48a6addbff5cee904527b058b392bd2fde809a83bd0878d3b7c.
Its current-paper definitions and complete DATA_QUOTIENT_CLOCK.md and
DATA_QUOTIENT_CHECK.md dependencies were also read. The checker had already
read the complete Q_ORDER_POSITIVE_ROUTE.md and relevant mathematical
manuscript. Required mathematical skills and current instructions were
applied. The initial bounded-class check used no cavity-extension
candidate. The final enlarged-class source was subsequently read completely;
its finite-carrier dependencies were checked separately in this study.
No other study, experiment, manuscript edit, or Git write was used.

**Verdict: PASS for the initialization, activation-class and symmetry
claims as stated.** The automatic second-layer gap for an activation that
is neither even nor odd remains valid when the first covariance is
singular. The odd and even quotients preserve both trained systems and
the original residual-RMS clock for compatible labels. No finite trained
carrier theorem follows from this note alone.

## 1. Activation class and the Gaussian feature lemma

The candidate's sufficient finite-insertion class is

\[
\phi\in C^3(\mathbb R),\qquad
\max_{0\le j\le3}\|\phi^{(j)}\|_\infty<\infty,\qquad
\phi\text{ nonconstant}.
\tag{A1}
\]

Every such function is nonpolynomial, since a real polynomial bounded on
the full real line is constant. It has bounded slope and globally
Lipschitz derivative, so it lies within the paper's deterministic
comparison class. The implication in the opposite direction is not
asserted: bounded slope and Lipschitz derivative do not imply bounded
values or a third derivative.

The listed examples meet (A1). Derivatives of tanh and the logistic
sigmoid through order three are polynomials in their bounded function
values. The derivatives of arctan are bounded rational functions.
Derivatives of the error function and of $e^{-s^2}$ are bounded
polynomials times $e^{-s^2}$. Trigonometric derivatives are bounded.
All of these functions are nonconstant. No monotonicity or positive
derivative is needed.

Here is the feature-positivity argument in its precise generality. Let
$u_1,\ldots,u_m$ be nonzero pairwise nonproportional vectors in a finite
real Euclidean space, $G$ a standard Gaussian, and $\psi$ a continuous
nonpolynomial function whose listed Gaussian ridge features belong to
$L^2$. Set

\[
Q_{ab}=\mathbb E[\psi(G^\top u_a)\psi(G^\top u_b)].
\]

If $c^\top Qc=0$, the continuous function
$\sum_a c_a\psi(u_a^\top x)$ vanishes almost everywhere for a Gaussian
of full support and hence vanishes everywhere. If $m\ge2$, fix $a$
with $c_a\ne0$. For every $b\ne a$, the projection of $u_a$ onto
$u_b^\perp$ is nonzero, so choose $v_b\in u_b^\perp$ with
$v_b^\top u_a\ne0$. Apply the product of finite differences along
$t_bv_b$. The $b$th difference annihilates the $b$th ridge; therefore
all ridges except the $a$th are eliminated. Since every $t_b$ and the
base point may vary independently,

\[
\Delta_{s_1}\cdots\Delta_{s_{m-1}}\psi(t)=0
\quad\text{for all }t,s_1,\ldots,s_{m-1}\in\mathbb R.
\tag{A2}
\]

Convolution with a compact smooth approximate identity preserves (A2).
For its smooth result, differentiation once in every step at zero gives
the zero $(m-1)$st derivative. Thus each mollification is a polynomial
of degree at most $m-2$. Fix $m-1$ distinct real interpolation points.
Local uniform convergence of mollifications gives convergence of their
values at those points, hence convergence of the coefficients through
the fixed invertible Vandermonde system. It follows that $\psi$ itself
is such a polynomial, a contradiction.

For $m=1$, the scalar Gaussian $G^\top u_1$ has full support because
$u_1\ne0$. A continuous nonpolynomial function is not identically zero,
so its uncentered second moment is positive. In ambient dimension one,
pairwise nonproportionality already forces $m=1$; no nonexistent
perpendicular vector is used.

This proves $Q\succ0$. The required covariance is uncentered throughout:
there is no subtraction of the activation mean, which would change the
claim for sigmoid and other offset activations.

If a positive semidefinite covariance $C$ has a Gram representation
$C_{ab}=u_a^\top u_b$ by such vectors, $Z_a=G^\top u_a$ realizes
$N(0,C)$ and the preceding proof applies even if $C$ is singular.
Once $C\succ0$, every continuous nonconstant scalar activation with
finite Gaussian second moments preserves strict positivity: a putative
identity $\sum_a c_a\psi(Z_a)=0$ holds on all of $\mathbb R^m$ by
full support, and subtracting two points that differ in only coordinate
$a$ forces $c_a=0$. This checks both parts of the candidate's Section 2.

## 2. Distinct sphere inputs when the first activation has no parity

Let the fixed inputs obey $\|x_a\|_2=\sqrt d$ and put
$v_a=x_a/\sqrt d$. Assume they are pairwise distinct and the first
activation $\phi$ is neither even nor odd. In the first Gaussian
layer define the Hilbert-space vectors

\[
U_a(G)=\phi(G^\top v_a)\in L^2(N(0,I_d)).
\]

Each $U_a$ is nonzero: $G^\top v_a$ is a nondegenerate scalar
Gaussian, $\phi$ is continuous, and $\phi$ is not identically zero.

Suppose two feature vectors are proportional. Neither is zero, so their
proportionality factor is nonzero. Equality in Gaussian $L^2$ extends
to equality for every $G$ by continuity and full support. If $v_a$
and $v_b$ are not parallel, the map

\[
x\longmapsto(v_a^\top x,v_b^\top x)
\]

has rank two and is onto $\mathbb R^2$. The identity would give
$\phi(s)=c\phi(t)$ for all $s,t$, forcing $\phi$ to be constant.
If the distinct unit vectors are parallel, they are antipodal.
Proportionality then gives $\phi(-s)=c\phi(s)$ for all $s$.
Applying it twice and using $\phi\not\equiv0$ gives $c^2=1$.
The choices $c=1,-1$ make $\phi$ even or odd, respectively. Both
contradict the hypothesis.

The finite-dimensional span of the $U_a$ admits an orthonormal basis.
Take each $u_a$ to be the vector of coordinates of $U_a$ in that
basis. Then

\[
Q_{ab}^{(1)}=\langle U_a,U_b\rangle=u_a^\top u_b,
\]

and the $u_a$ are nonzero and pairwise nonproportional. This reasoning
does not require the whole family to be linearly independent.
The covariance $Q^{(1)}$ may therefore be singular without causing a
gap in the argument.

Any bounded nonconstant second activation is continuous nonpolynomial
and has finite Gaussian moments. Applying the lemma of Section 1 to
these $u_a$ gives $Q^{(2)}\succ0$. Every later continuous nonconstant
activation with the required moments preserves this gap. In particular,
using the same activation satisfying (A1) in every layer proves the
candidate's claim for every fixed $L\ge2$.

For logistic sigmoid, the necessity of handling singular $Q^{(1)}$
is concrete. The identity $\phi(s)+\phi(-s)=1$ makes the first-layer
features of two antipodal pairs obey
$U_v+U_{-v}-U_u-U_{-u}=0$. This is a linear relation among four
vectors, but no pair of them is proportional when $u\ne\pm v$.
The second nonpolynomial layer therefore restores a positive-definite
feature covariance by the proved lemma. There is no odd-output
constraint for this architecture. Duplicate inputs remain identical
under every parameter state and must have equal labels for interpolation.

## 3. Exact odd quotient at every fixed depth

Assume every hidden activation is odd and differentiable; its derivative
is then even. Partition normalized inputs by equality up to sign. Let
$I_j$ be a class, $u_j$ its representative, and
$v_a=s_au_j$ for $a\in I_j$, with $s_a\in\{-1,1\}$. Define
$p_j=|I_j|/m$. Compatible labels have the form
$y_a=s_a\bar y_j$.

At every physical parameter state, induction through the forward and
backward passes gives

\[
z_a^{(\ell)}=s_az_j^{(\ell)},\qquad
h_a^{(\ell)}=s_ah_j^{(\ell)},\qquad
f_a=s_af_j,\qquad
\delta_a^{(\ell)}=\delta_j^{(\ell)}.
\tag{A3}
\]

The backward equality starts from the same readout and even top gate
and propagates downward. Thus $r_a=s_a e_j$ with
$e_j=f_j-\bar y_j$, and

\[
\rho^2=\sum_jp_je_j^2,\qquad
Y^2=\sum_jp_j\bar y_j^2.
\tag{A4}
\]

Each dense gradient product contains exactly one sign from the input or
forward response, canceled by the sign in its residual. Consequently
the full sample average equals the canonical gradient update on the
representatives with positive weights $p_j$.

For the actual closure, the forward raw moments obey
$\bar h_{a,k}^{(\ell-1)}=s_a\bar h_{j,k}^{(\ell-1)}$. Under compatible
labels the backward moments obey
$\bar\delta_{a,k}^{(\ell)}=s_a\bar\delta_{j,k}^{(\ell)}$ as well:
their source is $r_a\delta_a^{(\ell)}=s_ae_j\delta_j^{(\ell)}$
and their initial value is zero. Equivalently, the effective representative
moment is the signed class average

\[
\bar\delta_{j,k}^{(\ell)}
=|I_j|^{-1}\sum_{a\in I_j}s_a\bar\delta_{a,k}^{(\ell)}.
\]

Substitution in the exact reconstruction gives

\[
\widehat W^{(\ell)}=W_0^{(\ell)}
-\frac2{n\tau}\sum_jp_j\sum_{k<q}(2k+1)
\bar\delta_{j,k}^{(\ell)}\bar h_{j,k}^{(\ell-1)\top}.
\tag{A5}
\]

The moment sources and first-layer/readout updates likewise reduce
exactly to their weighted representatives. Equation (A4) preserves
$\dot\tau=\rho$ and its unit prefix. This is an identity of the
autonomous dynamics, not only of initialized features.

The representatives are nonzero pairwise nonproportional unit vectors.
The first nonpolynomial activation gives a positive first feature
covariance by Section 1, and subsequent nonconstant layers preserve it.
Multiplication by the invertible diagonal matrix
$\operatorname{diag}(\sqrt{p_j})$ preserves strict positivity of the
weighted covariance.

## 4. Exact even-first-layer quotient

Suppose the first activation is even; later activations may have any
parity. Its first derivative is odd. For the same sign-class notation,
the forward relations at every parameter state are

\[
z_a^{(1)}=s_az_j^{(1)},\qquad
h_a^{(1)}=h_j^{(1)},\qquad
z_a^{(\ell)}=z_j^{(\ell)},\ h_a^{(\ell)}=h_j^{(\ell)}
\quad(\ell\ge2),\qquad f_a=f_j.
\tag{A6}
\]

The backward responses satisfy
$\delta_a^{(\ell)}=\delta_j^{(\ell)}$ for $\ell\ge2$ and
$\delta_a^{(1)}=s_a\delta_j^{(1)}$. The first carrier is unchanged;
the sign in the first backward response comes only from the odd first
gate.

Compatible labels are $y_a=\bar y_j$, so $r_a=e_j$ throughout the
class. The first-layer gradient product is unchanged because both
$\delta_a^{(1)}$ and $v_a$ change sign. Every later update product
has no sign change. Thus the dense dynamics reduce to the positive
weighted representatives, and (A4) again holds.

All closure-stored forward histories are $h^{(\ell-1)}$ with
$\ell\ge2$, so they agree within a class. All stored backward sources
are $r_a\delta_a^{(\ell)}$ with $\ell\ge2$, so those agree as well.
Unsigned class averages of the backward moments and their common
forward moments give the weighted reconstruction (A5). The raw moment
ODE, first-layer/readout equations, residual RMS and original clock
are therefore preserved. The candidate's even quotient is exact.

The first-feature gap on representatives follows from the same
nonpolynomial ridge lemma; subsequent nonconstant layers preserve it.
The argument includes cosine and $e^{-s^2}$ despite their nonmonotonicity.

## 5. Scope and remaining implications

For arbitrary layer-dependent activations satisfying (A1), fixed
nonzero pairwise nonproportional inputs need no parity argument:
the first Gaussian covariance is positive definite by the ridge lemma,
and later layers preserve it. The broader sphere cases stated in the
candidate also check:

- Every activation odd gives the signed quotient in Section 3.
- An even first activation gives the unsigned quotient in Section 4
  regardless of subsequent parity.
- A first activation that is neither even nor odd gives nonproportional
  first feature vectors on distinct sphere inputs, and any second
  bounded nonconstant activation gives a positive-definite second
  covariance.

These are sufficient cases, not an exhaustive classification of
mixed-parity architectures. The candidate's caution is valid: an odd
first activation followed by $\phi_2(s)=c+\psi(s)$ with odd $\psi$
has $h^{(2)}(v)+h^{(2)}(-v)=2c\mathbf1$. With two antipodal pairs
this creates a four-feature linear dependence, although the output
need be neither even nor odd. It is therefore correct to retain an
explicit feature-Gram assumption outside the proved sufficient cases.

At fixed dataset, depth and activation, a strictly positive limiting
Gram has some positive margin. Its weighted version does too, since
all class weights are fixed and positive. The paper's conditional
law-of-large-numbers induction applies: initialized next-layer rows
are conditionally independent Gaussian vectors with empirical
previous-layer covariance, bounded activations have bounded fourth
moments, and covariance square roots are continuous, including at
singular matrices. Thus the asserted finite-width initial Gram margin
holds with probability tending to one.

The gap may tend to zero as inputs collide, so no geometry-uniform
small-label threshold is obtained. Compatible labels ensure the quotient
clock stays the original residual RMS. Conflicting labels are excluded
from these fitting consequences; substituting a smaller effective
residual clock would define another algorithm.

The initialization and parity calculations are logically separate from the
finite trained-carrier estimate. That estimate is now supplied by the
separately reconstructed bounded and unbounded insertion/probability
arguments. This note certifies the automatic Gram and symmetry inputs;
it does not replace those finite-width proofs.

## 6. Final extension to bounded derivatives and unbounded values

The enlarged source was read completely at its final hash above.
Its Section 5 permits
\[
 \phi\in C^3(\mathbb R),\qquad
 \max_{1\le j\le3}\|\phi^{(j)}\|_\infty<\infty,\qquad
 \phi\ \text{nonaffine}.
 \tag{A7}
\]
The finite trained-carrier theorem needs the derivative conditions and an
initial Gram gap. Nonaffinity is imposed here only to obtain the gap
automatically for the stated data geometries.

Bounded slope gives
\[
 |\phi(s)|\le|\phi(0)|+\|\phi'\|_\infty|s|.
\]
Thus all Gaussian feature second moments and covariance-induction fourth
moments are finite. A real polynomial with globally bounded derivative
has degree at most one. Hence every function in (A7) is nonpolynomial,
which is the precise hypothesis used in (A2); bounded values were not
used in the finite-difference proof.

For distinct sphere inputs, the nonproportionality of their first-layer
Gaussian features also used only continuity, nonconstancy, full support,
and the absence of even/odd parity. Linear growth makes those features
elements of the same Gaussian \(L^2\) space. Their finite Gram
representation therefore again consists of nonzero pairwise
nonproportional vectors, even when that first Gram is singular.
The nonpolynomial second activation gives a strictly positive second
Gram. Once positivity holds, a subsequent continuous nonconstant
activation of at most linear growth preserves it by the full-support
coordinate-variation argument.

The odd and even quotient identities in Sections 3–4 are algebraic;
their derivation never used bounded activation values. They remain exact
for the dense and actual autonomous closure dynamics and preserve the
weighted residual RMS clock. Thus a common activation satisfying (A7)
has the same three parity alternatives as in the bounded source.
For layer-dependent activations, each use of a bounded nonconstant
activation to obtain nonpolynomiality can be replaced by a nonaffine
activation with bounded slope. The source does not claim that every
mixed-parity architecture has an automatic gap.

The conditional feature covariance induction is also valid. On bounded
preceding covariance sets, Gaussian fourth moments are uniformly bounded
by linear growth. Conditional Chebyshev proves convergence of each
empirical feature product. Realizing the Gaussian vector as \(Q^{1/2}G\),
continuity of the square root and a Gaussian polynomial dominator prove
continuity of the limiting moment at every positive semidefinite \(Q\),
including singular matrices. Induction gives the fixed-depth Gram limit
in probability. No unstopped deep-network exponential moment is used.

The three newly listed examples were checked directly:

* For softplus \(\phi(s)=\log(1+e^s)\), write
  \(\sigma(s)=(1+e^{-s})^{-1}\). Its first three derivatives are
  \(\sigma\), \(\sigma(1-\sigma)\), and
  \(\sigma(1-\sigma)(1-2\sigma)\), all bounded.
* For GELU \(\phi(s)=s\Phi(s)\), with standard Gaussian density
  \(\varphi\) and distribution function \(\Phi\), those derivatives
  are \(\Phi+s\varphi\), \((2-s^2)\varphi\), and
  \((s^3-4s)\varphi\), all bounded.
* For SiLU \(\phi(s)=s\sigma(s)\), they are
  \(\sigma+s\sigma'\), \(2\sigma'+s\sigma''\), and
  \(3\sigma''+s\sigma'''\). Each appearing positive-order logistic
  derivative decays exponentially at both infinities, so multiplication
  by \(s\) preserves boundedness.

All are nonaffine and neither even nor odd. Each obeys
\(\phi(s)-\phi(-s)=s\); this identity can create first-layer dependencies
among several antipodal pairs, but does not create proportional feature
pairs. The second-layer argument, rather than an assumed first-layer
gap, is what covers arbitrary distinct sphere inputs. With one of these
activations at every hidden layer and \(L\ge2\), sufficiently small
arbitrary fixed labels are therefore allowed on distinct inputs.
Identical inputs still require identical labels.

Nonaffinity cannot simply be deleted from this automatic-gap argument:
an affine activation may leave the feature span at dimension at most
\(d+1\), so sufficiently large distinct input sets can have singular
feature Grams. Such activations remain covered by the finite-carrier
theorem whenever its separate positive-Gram hypothesis is met.
The source's exclusions of ReLU/leaky ReLU and of uniformity as a
smoothing parameter vanishes are correct.

**Final verdict:** PASS for the enlarged initialization and quotient
claims. Combined with the separately checked finite-insertion and
probability arguments, these give the advertised activation examples;
the initial bounded-only review is superseded in class scope.
