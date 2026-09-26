# Scoped check of the customized order-one population

This is an internal mathematical check, not a promotion review. Inputs were
complete `docs/observable_p1.md` and `docs/NOTATION.md`, Section 3 of
`docs/global_nonlinear.md`, and its finite-closure equations, represented-state
examples and bounded-increment existence argument in C.4.7.10. The preferred
construction below was supplied in the supervisory assignment; its Fourier
normalization was checked independently.

## Verdict

The construction gives exact circle functions in the established order-one
static population representation. It keeps the entire frozen dictionary law,
uses only its original Gaussian coordinates, and can give the current read-in
exactly the standard two-dimensional Gaussian marginal. It also preserves the
canonical simultaneous-mark sign symmetry. It does not describe
an endpoint reached from the prescribed initialization. That distinction is
essential even when the current read-in marginal is Gaussian.

## Joint-law construction and active lower features

Keep the canonical lower coordinates `G_1,G_2,Z_1,Z_2`, with

\[
h_i=\tanh G_i,\qquad
k_i=\tanh(\sqrt\tau Z_i+\alpha h_i),\qquad
\psi_1=(1,h_1,h_2,k_1,k_2)^T.
\]

The separate upper population and its raw column
`psi_2=(1,H_1,H_2)^T` are unchanged. For a positive odd integer `k` and
`0<epsilon<1/sqrt(2)`, define the conditional angular density given
`S=(G_1,Z_1)` by

\[
p(\phi\mid S)=\frac{1+\epsilon[h_1\cos(k\phi)+k_1\sin(k\phi)]}{2\pi}.
\]

It integrates to one and is at least `(1-epsilon sqrt(2))/(2 pi)>0`.
Use polar coordinates of the independent unused Gaussian pair `(G_2,Z_2)`:

\[
\Psi=\operatorname{atan2}(Z_2,G_2),\qquad
\mathcal R=\sigma\sqrt{G_2^2+Z_2^2},\quad\sigma>0.
\]

Their joint polar density shows that `Psi` is uniform, `mathcal R` has
Rayleigh density `r exp(-r^2/(2 sigma^2))/sigma^2`, and they are independent.
Both are independent of `S`. Define the increasing circle lift

\[
F_S(\phi)=\phi+\frac\epsilon k
 [h_1\sin(k\phi)-k_1\cos(k\phi)],\qquad
\phi=F_S^{-1}(\Psi)\pmod {2\pi}.
\]

Its derivative is strictly positive, and `F_S(phi+2 pi)=F_S(phi)+2 pi`, so
this inverse is well-defined on the circle. Change of variables gives exactly
the desired conditional density. Symmetry gives `E h_1=E k_1=0`, so `phi` is
marginally uniform and independent of `mathcal R`. Thus
`w=mathcal R(cos(phi),sin(phi))` has marginal `N(0,sigma^2 I_2)`; `sigma=1`
retains the standard Gaussian marginal. Alternatively replace `mathcal R`
by any fixed radius `rho>0`. The full frozen joint law is unchanged.

For odd `k`, `F_{-S}(phi+pi)=F_S(phi)+pi`. Simultaneous negation of all four
Gaussian marks sends `Psi` to `Psi+pi`, keeps the radius, and hence sends `w`
to `-w`. This verifies the canonical lower sign condition. At the
probability-zero polar origin assign `w=0` for the Gaussian-radius version;
an arbitrary angle suffices for the fixed-radius version, with the sign
identity holding almost surely.

For the input `u=r(cos(theta),sin(theta))`, put

\[
A_k(s)=\frac1{2\pi}\int_0^{2\pi}\tanh(s\cos t)\cos(kt)\,dt,
\qquad a=E_{\mathcal R}A_k(r\mathcal R),
\]

where the expectation means evaluation at `rho` for fixed radius. The uniform
angular mean vanishes by a half-circle shift and the sine integral vanishes
by reflection. Conditioning first on `(S,mathcal R)` gives

\[
E[\tanh(w\cdot u)\mid S,\mathcal R]
=\epsilon A_k(r\mathcal R)
 [h_1\cos(k\theta)+k_1\sin(k\theta)].
\]

Therefore

\[
E_1\left[\begin{pmatrix}h_1\\k_1\end{pmatrix}\tanh(w\cdot u)\right]
=\epsilon a\Sigma
 \begin{pmatrix}\cos(k\theta)\\\sin(k\theta)\end{pmatrix},
\qquad \Sigma=\begin{pmatrix}v&\beta\\\beta&s\end{pmatrix}.
\]

The matrix is strictly positive definite. Indeed `v>0`, and equality in
`beta^2<=vs` would force `k_1` to be a deterministic scalar multiple of `h_1`.
But `Var(k_1|G_1)>0`, because `tau>0` and tanh is strictly increasing.
The other lower-feature contractions need not be evaluated and are not being
assigned any unproved harmonic form.

## Nonzero Fourier normalization

Write `k=2j+1`, `c_n=pi(n-1/2)`, and, for `s>0`,

\[
q_n=\frac{\sqrt{s^2+c_n^2}-c_n}{s}\in(0,1).
\]

The partial fraction expansion and its Fourier coefficient give

\[
\tanh z=2z\sum_{n\ge1}\frac1{z^2+c_n^2},\qquad
A_{2j+1}(s)=2(-1)^j\sum_{n\ge1}
 \frac{q_n^{2j+1}}{\sqrt{s^2+c_n^2}}.
\]

For completeness, the first identity follows by expanding the solution
`u(x)=sinh(zx)/(z cosh z)` of `u(0)=0,u'(1)=1,u''=z^2u` in the complete mixed
sine basis `sqrt(2) sin(c_n x)`. Integration by parts gives coefficients
`sqrt(2)(-1)^(n-1)/(z^2+c_n^2)`. They are absolutely summable, so evaluation
at `x=1` is legitimate and yields `tanh z/z=2 sum_n(z^2+c_n^2)^(-1)`;
the value at `z=0` is obtained by continuity.

To check the second identity, expand
`1/(b^2+cos^2 t)` as the Poisson series with parameter
`-Q`, where `Q=(sqrt(1+b^2)-b)^2`. Multiplication by `cos t` gives its
`(2j+1)`st complex Fourier coefficient
`(-1)^j Q^(j+1/2)/sqrt(1+b^2)`. Apply this with `b=c_n/s` to the first identity.
The series is absolutely convergent: its terms are `O(n^(-2j-2))`.
Every summand magnitude is positive, hence

\[
\operatorname{sign}A_k(s)=(-1)^{(k-1)/2}\quad(s>0).
\]

Thus `a` is nonzero for every `r>0`, both fixed positive radius and every
positive Gaussian scale. Averaging cannot cancel terms of one strict sign.

## Matrix normalization and exact upper integral

Since `b_l=L_l^{-1}psi_l`, the raw middle matrix and the actual evolving
matrix are related by

\[
K=L_2^{-T}ML_1^{-1},\qquad M=L_2^T K L_1.
\]

Positive ridge makes this a bijection; no dictionary changes. Set all raw
entries of `K` to zero except the `H_1` row and `h_1,k_1` columns, whose
row vector is

\[
\frac{(\lambda,\mu)\Sigma^{-1}}{\epsilon a}.
\]

Then the upper preactivation equals
`H_1 t(theta)`, where `t(theta)=lambda cos(k theta)+mu sin(k theta)`.
Inactive lower-feature correlations cannot affect it. This is an exact
static reparameterization, not an assertion that the raw matrix has the
normalized matrix's gradient-flow metric.

Let `H=H_1`. Its density is

\[
p_H(h)=\frac{\exp[-\operatorname{atanh}(h)^2/(2v)]}
 {\sqrt{2\pi v}(1-h^2)},\qquad -1<h<1.
\]

For any `0<b<1`, the odd readout

\[
c(H)=\frac{\operatorname{sign}(H)\mathbf1_{\{|H|\le b\}}}{2b p_H(H)}
\]

is bounded, since `p_H` is continuous and strictly positive on `[-b,b]`.
Its value at zero may be defined as zero. Direct integration gives

\[
f(\theta)=\frac1b\int_0^b\tanh(h t(\theta))\,dh
=\begin{cases}
\log\cosh(b t(\theta))/(b t(\theta)),&t(\theta)\ne0,\\
0,&t(\theta)=0.
\end{cases}
\]

All integrands are absolutely integrable. The value at zero is the analytic
extension. Every expectation contracts objects in its own population.

## Precise limitation

Canonical training starts with `w=g,c=0,M=D` and has bounded `w-g` at every
finite time. A fixed-radius choice has unbounded `w-g` because `g` is
unbounded. The Gaussian-radius choice here also has unbounded `w-g`:
`mathcal R<=1` and `|G_1|>N` have positive joint probability for every `N`,
by independence, and there `|w-g|>=N-1`. Thus neither particular static
state is a finite-time canonical training endpoint. Gaussian marginal
agreement does not repair the different joint relation between `w` and its
frozen initialization marks. The customized readout likewise replaces the
prescribed zero readout. These are representation statements only.

## Final assembled-artifact audit, 2026-09-21

Outcome: **PASS for the stated static representation identities and bounds.**
The complete final `DERIVATION.md` was read and checked, including all sixteen
numbered equations and its amended scope paragraph. No mathematical correction
or missing hypothesis was found within that scope. This is an internal scoped
check by an agent involved in developing the construction, not a fresh isolated
review or approval for promotion.

In particular, the normalized cost in (15) has both required ridge factors.
Let `J` select the lower coordinates `(h_1,k_1)` and set
`d=(lambda,mu) Sigma^{-1}/(epsilon A_q)`. Then

\[
K=e_{H_1}dJ,\qquad
\|M\|_F^2
=\|L_2^Te_{H_1}\|^2\|dJL_1\|^2
=(\tau+\eta)d(\Sigma+\eta I)d^T.
\]

Here the first equality uses the Euclidean norm of each factor of a rank-one
matrix, and `J L_1 L_1^T J^T=Sigma+eta I` follows from the actual uncentered
Gram. Substituting `d` gives (15); replacing this by the raw `K` norm would be
incorrect. The fixed-radius exponential lower bound on this particular
construction's cost and the weaker Gaussian-radius divergence both follow
from the proved signed Fourier series as stated.

The finite-polynomial extension was checked separately. A finite sum makes
`B` bounded, `epsilon ||B||_infinity<1` makes the lift strictly increasing,
and the zero Fourier mean of `B` normalizes the density. The primitive's
half-circle antisymmetry proves the same mark-sign equivariance. Independence
of the unused polar radius gives exactly `epsilon h_1 T(theta)` after angular
and radial integration. The single selected raw column yields
`L(b lambda T)` as claimed. Finally the pointwise bound
`|L(x)-x/2|<=|x|^3/12`, divided by `|b lambda|/2`, gives (16) with constant
`1/6`. The derivation explicitly states that the customized coupling depends
on `T`; it does not claim one fixed population can vary through every such
polynomial using the small matrix alone.

Remaining limitations are the ones declared in the artifact: no finite-time
canonical reachability for these particular states, no uniform parameter-cost
bound over frequency or polynomial complexity, no finite-population error or
conditioning guarantee, and no finite-width neural approximation statement.
The discontinuous bounded readout is admissible for these integrals, but a
smooth-readout restriction would require a modified theorem. No computation
or training experiment was used to establish the exact identities.

Read coverage and source provenance:

* `DERIVATION.md`: complete final artifact, Sections 1–7, read after the final
  scope amendment; its SHA-256 is below.
* `docs/observable_p1.md`: complete file, including canonical joint marks,
  ridge factors, finite closure, and state/metric interpretation.
* `docs/NOTATION.md`: complete file.
* `docs/global_nonlinear.md`: complete Section 3 (lines 281–504); selected
  finite-closure and represented-state material at lines 13380–13732; and
  source-law, bounded-mark, existence and stability material at lines
  13890–14040. The rest of this large source was not read. These are the exact
  line intervals in the hashed version below.
* The NIST URL in the derivation was not fetched in this scoped check. Its
  required partial-fraction identity was independently derived above from
  the mixed-boundary sine expansion, so no mathematical step of this audit
  depends on uninspected web content. URL attribution itself is outside this
  check's coverage.

SHA-256 values measured for the reviewed versions:

```text
f3bda59f24de70d139cbf06c679e29c6a087293dc1229fba3be9a3157d399219  studies/p1_circle_population_design_20260921/DERIVATION.md
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba  docs/observable_p1.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c  docs/global_nonlinear.md
```
