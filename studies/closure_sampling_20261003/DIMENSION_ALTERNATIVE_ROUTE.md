# What coefficient structure alone can and cannot save

2026-10-04. Scoped alternative route in `closure_sampling_20261003`.
**Complete elementary obstruction proofs; not independently checked.**
This file freezes the candidate before exchanging scientific findings with
the training-span or complex-sphere routes. It supplies no new compression
theorem for the canonical neural flow. Its positive result is an exact finite
coefficient count. Its negative results identify why analytic source bounds
alone do not justify an adaptive low-dimensional neuron span or a fixed-cut
separable output representation.

The input scope was `ARCHITECTURE_CONSTANT_REFINEMENT.md`,
`DIMENSION_PREFACTOR_OPTIMIZATION.md`, `STORAGE_QUADRATIC_IMPROVEMENT.md`,
and `GENERAL_ANALYTIC_COMPRESSION.md`; all were read completely. Shared
workflow and the canonical-notation, neural-response-memory,
investigate-conjectures, research-contract, adversarial-audit, and
solve-math-rigorously instructions were also read. No other route's new
file, other study, external mathematical source, experiment, Git operation,
or maintained-manuscript material was used. The supervisor was told the
chosen obstruction direction, but no result from another route was received
before this freeze.

## 1. Contract and the distinction made here

The actual research target is the same initialized finite dense network,
trained with the canonical physical-time flow, approximated by a smaller
autonomous model with its own residuals and genuinely moving hidden
parameters. The requested error is uniform over physical time, including
the fitted endpoint, and every sphere query, at order $n^{-1/2}$.
The inherited small-label and initialized-Gram-gap conditions are retained.
All fixed and moving real coordinates count; original-width arrays and
trained-trajectory oracles are inadmissible at runtime.

The current source construction first approximates several vector-valued
functions by scalar Fourier/Chebyshev modes and then uses their coefficient
span as a neuron space. After the time cosine substitution its quantitative
analytic input has $d$ periodic variables, one time variable and $d-1$
angular variables, with strip widths

\[
 \alpha=\frac{c_t\lambda}{128\ell_n^{3/2}},\qquad
 r=\frac{c_a}{\sqrt{\ell_n}},\qquad
 \ell_n=\log(en),\qquad \lambda=\min(1,\gamma/m).
 \tag{1}
\]

Here $c_t,c_a>0$ are the actual radius constants, and $\gamma$ is the
smallest eigenvalue of the unnormalized limiting top-feature Gram. The
source coefficient estimate is

\[
 |\widehat G(k_0,k')|
 \le M\exp[-\alpha |k_0|-r\|k'\|_1].
 \tag{2}
\]

The following results concern what can be inferred from this analytic
information, or from bounded analytic dependence on the sphere, **without
additional neural structure**. They are not lower bounds for the set of
source functions realized by Gaussian neural training. In particular they
do not prove that the remaining factors \(\beta^{O(Ld)}\), \((d+3)^d\),
or the current logarithmic exponent are necessary for arbitrary autonomous
compression. Such a statement would require a neural realizability or
neural metric-entropy theorem not supplied here.

## 2. An exact finite replacement for the simplex upper count

For $D=d-1\ge0$, nonnegative cutoff $H$, and positive $\alpha,r$,
let $N(H)$ count the real modes used in the current construction:

\[
 N(H)=\#\{(j_0,j')\in\mathbb Z_{\ge0}\times\mathbb Z^D:
                     \alpha j_0+r\|j'\|_1\le H\}.
 \tag{3}
\]

The nonnegative temporal index is a cosine mode. Each pair $j',-j'$
contributes its real sine and cosine coefficients, so this is exactly the
number of real coefficient vectors in the symmetric angular frequency set.
For $D=0$, interpret the inner expression below as one. In every finite
dimension and at every cutoff,

\[
 N(H)=\sum_{j_0=0}^{\lfloor H/\alpha\rfloor}
       \sum_{s=0}^{\min\{D,q_{j_0}\}}
          2^s{D\choose s}{q_{j_0}\choose s},\qquad
 q_{j_0}=\left\lfloor\frac{H-\alpha j_0}{r}\right\rfloor .
 \tag{4}
\]

To prove (4), fix $j_0$ and the number $s$ of nonzero angular
coordinates. There are \({D\choose s}\) supports and $2^s$ sign
choices. Their $s$ positive integer magnitudes have sum at most
$q=q_{j_0}$. Subtract one from each magnitude and add a slack
coordinate. The resulting $s+1$ nonnegative integers have total
$q-s$, giving \({q\choose s}\) possibilities by placing $s$
separators among $q$ positions. For $s=0$ there is exactly the zero
vector. Summing proves the formula, including $q=0$ and $D=0$.

Thus the exact source inventory can use

\[
 R\le4N(H)+2m+d+1 \quad(d\ge2)
 \tag{5}
\]

in place of its simplex envelope; for $d=1$, both sphere points give
$R\le8N(H)+2m+2$. These are unchanged source constructions: the
same retained index set and the same initialization-only scalar linear
operations produce the coefficients. Only the reported count changes.
Using the inherited runtime inventory with the actual maximum layer rank
$R$ gives

\[
 \operatorname{size}(C)
 \le1020(L+1)R^2+10m(d+1).
 \tag{6}
\]

No data, fixed metrics, learned dense edges, first-layer weights, readout,
residual coordinates, or solve caches are removed from (6). The identity
(4) can be substantially smaller when many angular indices must vanish.
It is not a claim that the fixed-$d$, large-$n$ exponent or the persistent
radius dependence has improved. In particular it does not discard a
coefficient by imposing $p\gg d$.

## 3. Adaptive neuron spans can have the full analytic dimension

The next statement is stronger than an obstruction to a fixed Fourier
dictionary: its approximating neuron subspace may depend arbitrarily on
the entire vector-valued function.

Fix an integer $d\ge1$, strip widths $\omega_0,\ldots,\omega_{d-1}>0$,
coordinate bound $M>0$, and accuracy $\epsilon>0$. Assume

\[
 H_*:=\log\frac{M}{2^{d/2+1}\epsilon}>0.
 \tag{7}
\]

Define the finite nonnegative mode set and its cardinality by

\[
 \mathcal I=\{k\in\mathbb Z_{\ge0}^{d}:
                      \textstyle\sum_j\omega_jk_j\le H_*\},
 \qquad J=|\mathcal I|.
 \tag{8}
\]

For every integer neuron width $n\ge2J$, there is a real-valued,
coordinatewise entire, periodic vector source
$G:\mathbb R^d\to\mathbb R^n$, even in its temporal variable, with

\[
 \sup_{|\Im z_j|\le\omega_j}\|G(z)\|_\infty\le M,
 \tag{9}
\]

such that every subspace $S\subseteq\mathbb R^n$ permitting coordinate
error at most $\epsilon$ uniformly on the real torus satisfies

\[
 \dim S\ge J/2,\qquad
 J\ge\frac{H_*^d}{d!\prod_{j=0}^{d-1}\omega_j}.
 \tag{10}
\]

“Permitting” means that for every real $z$ there is a vector $s(z)\in S$
with \(\|G(z)-s(z)\|_\infty\le\epsilon\); no linearity, continuity,
or prescribed formula for the coefficient map $z\mapsto s(z)$ is
required. Thus adaptive choices of the neuron span are included.

**Proof.** On the normalized $d$-torus define

\[
 \psi_0(u)=1,\qquad \psi_j(u)=\sqrt2\cos(ju)\ (j\ge1),
 \qquad \Psi_k(z)=\prod_{j=0}^{d-1}\psi_{k_j}(z_j).
 \tag{11}
\]

The $\Psi_k$ are orthonormal in real $L^2$: the one-variable cosine
integrals are zero between distinct indices and one on equal indices,
and repeated integration factors the product. Since
$|\cos(j(u+iv))|\le e^{j|v|}$, every $k\in\mathcal I$ obeys

\[
 |\Psi_k(z)|\le2^{d/2}e^{H_*}
 \quad\text{on the complex strip.}
 \tag{12}
\]

Let $b=\lfloor n/J\rfloor$. For each $k\in\mathcal I$, use a
block of $b$ coordinates of $G$, all equal to $2\epsilon\Psi_k$,
and set the remaining $n-bJ$ coordinates to zero. Equations (7) and
(12) give (9), and the coordinate functions are entire and even.

For each mode let $e_k\in\mathbb R^n$ be the unit vector that is
constant $b^{-1/2}$ on its block and zero elsewhere. These $J$ vectors
are orthonormal. With real-torus expectation $\mathbb E_z$, the empirical
covariance is exactly

\[
 \frac1n\mathbb E_z[G(z)G(z)^\top]
   =\frac{4\epsilon^2b}{n}\sum_{k\in\mathcal I}e_ke_k^\top.
 \tag{13}
\]

Write $P_S$ for Euclidean orthogonal projection onto $S$ and
$q=\dim S$. Coordinate error at most $\epsilon$ implies Euclidean
distance from $G(z)$ to $S$ at most $\sqrt n\epsilon$, hence

\[
 \epsilon^2\ge\frac1n\mathbb E_z\|(I-P_S)G(z)\|_2^2
 =\frac{4\epsilon^2b}{n}
     \sum_{k\in\mathcal I}\|(I-P_S)e_k\|_2^2
 \ge\frac{4\epsilon^2b}{n}(J-q).
 \tag{14}
\]

For the final inequality, extend the $e_k$ to an orthonormal basis;
the sum of \(\|P_Se_k\|^2\) over this partial basis is at most
\(\operatorname{tr}P_S=q\). Because $n\ge2J$,
$b\ge n/(2J)$. Substitution into (14) gives $q\ge J/2$.

For the count, each point $x\in\mathbb R_{\ge0}^{d}$ with
$\sum_j\omega_jx_j\le H_*$ lies in the unit cube based at
$\lfloor x\rfloor\in\mathcal I$. These cubes have disjoint
interiors and unit volume. The simplex therefore has volume at most
$J$. Substituting $y_j=\omega_jx_j/H_*$ makes that volume
$H_*^d/(d!\prod_j\omega_j)$, proving (10). This argument needs no
large-degree or fixed-dimension approximation. ∎

Apply this statement to the analytic-information class with
$\omega_0=\alpha$, $\omega_j=r$ for $j\ge1$,
$\epsilon=n^{-1}$, and the supplied bound $M=M_0\sqrt n$, with
fixed $M_0\ge1$. For fixed data, eventually
$H_*\ge\ell_n/2$ and $n\ge2J$: $H_*$ is logarithmic and
$J\le\prod_j(1+H_*/\omega_j)$ is a fixed power of $\ell_n$.
Consequently the examples satisfy

\[
 \dim S\ge
 \frac{64}{2^d d!}\,
 c_t^{-1}c_a^{-(d-1)}\lambda^{-1}
 \ell_n^{3d/2+1}.
 \tag{15}
\]

The exponent and the product of the actual inverse radii match the
current source-span upper bound, up to fixed constants and the angular
sign conventions. Hence a universally smaller neuron span cannot be
deduced just by reexpressing arbitrary functions satisfying the same
strip/magnitude assumptions. A new neural identity, a larger analytic
domain, or a change that avoids requiring such neuron spans is necessary
to bypass this particular obstruction.

Two limitations matter. First, arbitrary angular torus functions need
not descend through the noninjective sphere parameterization; (15) is an
obstruction to using the strip input alone, not a sphere lower bound.
Second, the $\beta$ and dimension envelopes for $c_t^{-1},c_a^{-1}$
are upper bounds, so substituting those envelopes into the lower bound
(15) would reverse the needed logical implication. That substitution is
invalid and is not made here.

## 4. A scalar output can have large separation rank on the sphere

The angular-consistency concern can be avoided for a weaker but genuine
sphere obstruction. This result applies even to polynomial functions of
the sphere coordinates. It prevents an unconditional low-rank claim for
a scalar query map across a specified coordinate cut; it does not cover
every arithmetic circuit or every reordering of a tensor representation.

Let $d\ge3$, $D=d-1$, $k=\lfloor D/2\rfloor\ge1$,
$a=(2D)^{-1/2}$, and $p\ge0$ an integer. Define

\[
 J=(p+1)^k,\qquad C_D=1+4\sqrt{2D},\qquad
 A=\frac{M}{J\,2^k C_D^{2kp}}.
 \tag{16}
\]

There is a real polynomial $F(v)$, $v\in\mathbb R^d$, bounded
by $M$ throughout the complex box \(|v_i|\le2\), such that a
uniform approximation on $S^{d-1}$ by a function whose restriction to
the chart below is a sum of $q$ separated terms must satisfy

\[
 q\ge J-(\epsilon/A)^2.
 \tag{17}
\]

In particular, if

\[
 \epsilon\le\frac{M}{2^k C_D^{2kp}\sqrt{2J}},
 \tag{18}
\]

then $q\ge J/2$. All these bounds are finite and explicit.

**Construction and proof.** Define the Chebyshev polynomials recursively
by $T_0(z)=1$, $T_1(z)=z$,
$T_{j+1}(z)=2zT_j(z)-T_{j-1}(z)$, and put
$P_0(z)=1$, $P_j(z)=\sqrt2T_j(z/a)$ for $j\ge1$.
The cosine addition formula proves inductively that
$P_j(a\cos u)=\psi_j(u)$, with $\psi_j$ from (11).
For every $z\in\mathbb C$, the same recurrence proves

\[
 |T_j(z)|\le(1+2|z|)^j.
 \tag{19}
\]

The base cases hold. For the induction step let $b=1+2|z|$;
$2|z|b+1\le b^2$ bounds the recurrence by $b^{j+1}$.
For \(|z|\le2\), (19) gives
$|P_j(z)|\le\sqrt2 C_D^p$ for $0\le j\le p$.

For multi-indices $j=(j_1,\ldots,j_k)\in\{0,\ldots,p\}^k$, set

\[
 F(v)=A\sum_j
          \prod_{i=1}^{k}P_{j_i}(v_i)
          \prod_{i=1}^{k}P_{j_i}(v_{k+i}).
 \tag{20}
\]

Each product is bounded by $2^kC_D^{2kp}$ on the complex box,
and there are $J$ terms. Equation (16) proves the bound $M$.
Thus $F$ is bounded on the real sphere and on every standard complex
angular strip with \(\sum|\Im\theta_i|\le1/8\): the sphere
coordinates there have magnitude at most $e^{1/8}<2$.

To exhibit a sphere chart with independent left and right variables,
take $u,\vartheta\in[0,2\pi]^k$ and set the first $2k$ coordinates of
the sphere point equal to

\[
 (a\cos u_1,\ldots,a\cos u_k,
   a\cos\vartheta_1,\ldots,a\cos\vartheta_k).
\]

Set coordinates $2k+1,\ldots,d-1$ to zero and take the last
coordinate to be the positive square root that makes the norm one.
The sum of the first $2k$ squares is at most $2ka^2=k/D\le1/2$,
so this is a well-defined subset of the sphere. On that subset,

\[
 F=A\sum_{j\in\{0,\ldots,p\}^k}\Psi_j(u)\Psi_j(\vartheta).
 \tag{21}
\]

Here $\Psi_j$ is the $k$-variable product basis from (11), not
a newly normalized family. Both left and right bases are orthonormal
under normalized torus measure.

Let a proposed approximation on the chart be
$\widetilde F(u,\vartheta)=\sum_{\nu=1}^{q}f_\nu(u)g_\nu(\vartheta)$, with
square-integrable factors. Project its coefficient array to the $J$
left and $J$ right basis functions in (21). The resulting $J\times J$
matrix $B$ has rank at most $q$: its entries are sums of outer
products of the left and right Fourier coefficients. Projection onto
an orthonormal finite family cannot increase squared $L^2$ norm,
as is seen by expanding the squared norm of the remainder. Therefore

\[
 \|F-\widetilde F\|_{L^2}^2\ge\|A I_J-B\|_F^2
                                      \ge A^2(J-q).
 \tag{22}
\]

For the last inequality choose an orthonormal basis of the nullspace
of $B$, which has dimension at least $J-q$, and extend it to an
orthonormal basis of \(\mathbb R^J\). On each nullspace vector,
$(AI_J-B)e=Ae$. The Frobenius norm squared is the sum of the
squared images over the whole orthonormal basis, proving the bound.
Uniform sphere error $\epsilon$ bounds the chart $L^2$ error by
$\epsilon$, proving (17); (18) then gives $q\ge J/2$. ∎

For fixed $d$, write $E=\log(M/\epsilon)$. Taking

\[
 p=\left\lfloor\frac{E}{4k\log C_D}\right\rfloor
 \tag{23}
\]

makes $C_D^{2kp}\le e^{E/2}$. Condition (18) then holds whenever
$M/\epsilon\ge2^{2k+1}(p+1)^k$, an explicit finite condition that
eventually holds as $\epsilon\downarrow0$. Thus separation rank can
grow as a positive multiple of

\[
 [\log(M/\epsilon)]^{\lfloor(d-1)/2\rfloor}
 \tag{24}
\]

for bounded analytic scalar functions on the sphere. A scalar observable
by itself does not imply dimension-independent tensor rank. The
constructed polynomial may have a short alternative circuit, and an
interleaved variable ordering can avoid this particular cut. Consequently
(24) is not a lower bound for all circuit descriptions, all tensor orders,
all real-coordinate encodings, or neural outputs under the canonical
initialization law.

## 5. Consequences and outstanding bridge

The exact count (4) is immediately usable by the existing autonomous
construction, with its unchanged initialization-only provenance and the
complete inventory (6). It improves a finite numerical bound whenever the
simplex envelope wastes support/sign combinations. It does not by itself
solve the requested asymptotic dimension-prefactor problem.

The complete new obstructions establish two narrower conclusions:

1. The current product-strip regularity class can require a neuron span
   of order \(c_t^{-1}c_a^{-(d-1)}\lambda^{-1}
   \ell_n^{3d/2+1}/d!\), even when the span is chosen adaptively.
2. Bounded analytic scalar sphere functions can require separation rank
   with a logarithmic-accuracy exponent proportional to dimension across
   a specified cut.

Neither proof simulates or supplies a future trained trajectory, and both
construct their examples by finite explicit formulas. But they are
obstruction examples, not autonomous surrogate models. They therefore do
not replace the required same-run, all-time neural comparison theorem.

The decisive missing ingredient for the attempted structured-coefficient
route is a **neural-specific low-rank or circuit theorem**, quantitatively
strong enough to survive the initialized forward and transpose image
pairing, the moving hidden updates, and the whole-sphere output comparison.
Analyticity, small labels, and a training Gram gap alone have not been
converted here into such a theorem. No storage improvement beyond the
exact finite count is claimed, and the broader compression target remains
open from this route's perspective.
