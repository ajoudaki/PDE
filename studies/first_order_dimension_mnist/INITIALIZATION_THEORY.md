# General-dimensional first-order initialization

This study construction extends the first-order tanh core of established
`docs/global_nonlinear.md`, C.4.7.10 B, equations (H3.1)–(H3.2), and
`code/pde/observable_initialization.py`. It concerns finite initialized
observable algebra and numerical integration. No general-dimensional trained
network convergence theorem is asserted. The maintained implementation remains
unchanged. The scalar label and two-hidden-layer model are unchanged; input
directions are `u=x/sqrt(d)`.

## Exact coefficient target

Fix a positive integer d. Let G_i and Z_i, i=1,...,d, be independent standard
normal coordinates on the lower population. Put

\[
h_i=\tanh G_i,\quad v=E\tanh^2G,\quad
\Xi_i=\sqrt v\,\widetilde Z_i,\quad H_i=\tanh\Xi_i,
\]

where the upper population has its own independent standard normal coordinates
\(\widetilde Z_i\). Its integration indices have no pairing with lower indices.
Define

\[
\tau=E H_i^2,\quad \alpha=E(1-H_i^2)=1-\tau,
\qquad R_i=\sqrt\tau Z_i+\alpha h_i,\qquad k_i=\tanh R_i.
\]

The `alpha h_i` term is the response of the actual reversed reused action.
In the established source rule, \(E h_i h_j=v\delta_{ij}\), so the forward
sources have covariance \(vI_d\). Their bounded upper outputs have covariance
\(\tau I_d\); the expected derivative of upper output i with respect to forward
source j is \(\alpha\delta_{ij}\). Substituting into that same rule yields the
displayed R jointly with G. Increasing d only repeats this finite calculation.
The joint lower law is the law of every pair (G_i,R_i) together, not independent
sampling of G_i and R_i.

Retain the raw feature columns

\[
\psi_1=(1,h_1,\ldots,h_d,k_1,\ldots,k_d)^T,
\qquad \psi_2=(1,H_1,\ldots,H_d)^T.
\]

These are the total-degree-at-most-one polynomial features. For d=2 their order
is exactly that of `build_dictionary(1)`; codes 0 and 1 add no extra features.
The generic source compiler is not dispatched at this order. The words and
fast branch in the maintained initializer, including their derivatives, were
read completely; no compiler implementation outside that branch is needed.

For one lower coordinate pair write

\[
s=E k_i^2,\qquad \beta=E h_i k_i,\qquad \gamma=E(1-k_i^2)=1-s.
\]

Simultaneous negation of (G_i,Z_i) negates both h_i and k_i; hence each has zero
mean. Independent coordinate pairs have zero cross-coordinate products.
Consequently the full uncentered feature Grams are

\[
G_1=\begin{pmatrix}1&0&0\\0&vI_d&\beta I_d\\0&\beta I_d&sI_d\end{pmatrix},
\qquad G_2=\operatorname{diag}(1,\tau I_d).
\]

The d-dimensional version of (H3.1) is

\[
E_2[B A_0F]=\sum_{i=1}^d
 E_1[Fh_i]E_2[\partial_{\Xi_i}B]
 +\sum_{i=1}^d E_1[\partial_{\zeta_i}F]E_2[BH_i],
\quad \zeta_i=\sqrt\tau Z_i.
\]

To see its scope, append A_0F after the reverse probes in the finite Gaussian
source rule. The response is the second sum. The fresh centered Gaussian source
has covariance E[Fh_i] with Xi_i. Subtract its regression on the independent
Xi_i; the residual centered Gaussian is independent of B and has zero pairing
with it, even if its variance is zero. For the regression contribution,
one-variable integration by parts gives E[B Xi_i]=v E[partial_Xi_i B]. B and
its first derivatives are bounded, so the Gaussian boundary term vanishes and
the integral exists. All F and B used here satisfy these hypotheses.

Applying this identity to the retained features gives the raw contraction

\[
C=E_2[\psi_2(A_0\psi_1)^T]
=\begin{pmatrix}
0&0&0\\
0&\alpha v I_d&(\alpha\beta+\tau\gamma)I_d
\end{pmatrix}.
\]

In particular the second summand \(\tau\gamma\) must be retained. It comes
from reversing and then reusing the same action; it is not a fresh Gaussian
forward approximation.

Use exactly the first-order ridge \(\eta=1/[1024(1+1)^2]=1/4096\). Set

\[
a=\sqrt{v+\eta},\qquad
b=\sqrt{s+\eta-\beta^2/(v+\eta)},\qquad c=\sqrt{\tau+\eta}.
\]

These denominators are positive. Indeed v,tau,s>0 because the relevant Gaussian
or conditional Gaussian law is nondegenerate and tanh is nonzero off zero;
\(\beta^2\le vs\) by Cauchy–Schwarz. Thus
\(b^2\ge\eta+s\eta/(v+\eta)>0\). In the stated ordering, the lower
Cholesky factor has diagonal blocks sqrt(1+eta), a I_d, b I_d, and only the
additional block \(L_{kh}=\beta I_d/a\). Therefore inverse-lower-Cholesky
normalization is exactly

\[
b_1=\left((1+\eta)^{-1/2},\ h/a,
\frac{k-\beta h/(v+\eta)}b\right),\qquad
b_2=\left((1+\eta)^{-1/2},H/c\right).
\]

The two nonzero coordinate-diagonal bands of \(D=L_2^{-1}CL_1^{-T}\) are

\[
D_{H_i,h_i}=\frac{\alpha v}{ac},\qquad
D_{H_i,k_i}=\frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}{bc}.
\]

The right transpose is required: omitting it gives different coefficients.
This reduction is an exact population coefficient identity. It is not diagonal
projection of an empirical Gram. Only D initially has this structure. The
evolving matrix M remains a full arbitrary \((d+1)\times(2d+1)\) matrix, and
its actual transpose is used for the reverse action.

## Numerical construction and cost

`P1_INITIALIZATION.initialize(d, particles, seed, ...)` returns b1,g,p1,b2,p2,D
and metadata. With the ordinary iid population rule their shapes are
(P,1+2d), (P,d), (P), (P,1+d), (P), and (1+d,1+2d). Independent lower G,
lower reverse noise, and upper noise use the three recorded child streams of
NumPy SeedSequence(seed), with PCG64. Seed is mandatory and no global random
generator is changed. Samples preserve the full lower (b1,g) joint tuple.

Constants are evaluated by positive Gauss–Legendre integration against the
normal density on [-10,10], normalized to unit mass. Scalar normal mass omitted
is erfc(10/sqrt(2)), about 1.52e-23. This tail number alone is not a certificate
for the nonlinear derived coefficients. The working rule has 256 scalar nodes;
128-node results provide a recorded refinement diagnostic. Scalar quadrature
provides v,tau,alpha; a two-dimensional tensor rule provides s,beta,gamma. No
d-dimensional tensor grid is built. Finer rules can be explicitly selected;
float64 errors remain, and no automatic tolerance choice is claimed. At a fixed
cutoff, scalar-rule refinement approaches the truncated-normal calculation.
Convergence to the exact Gaussian coefficient target additionally requires
increasing the cutoff with adequate scalar quadrature resolution; this file
does not prove or certify a combined numerical limit.

Once scalar nodes are generated, coefficient integration requires O(q²) scalar
work/storage for q scalar nodes. NumPy's dense node-generation eigensolve can
cost O(q³); it is independent of d and P and the scalar results are cached.
Population generation and
normalization require O(Pd) work/storage; materializing the requested dense D
requires O(d²) storage and zero-fill work. There is no Qd² empirical Gram work
or d³ Cholesky in production. `dense_oracle` deliberately reconstructs the
full exact-block Gram and performs dense Cholesky for small verification cases.
Population sampling is a separate resolution axis from coefficient quadrature.

The maintained d=2 initializer estimates all coefficients and full Grams using
a finite Q-node joint Halton rule. Its finite-Q Gram generally has nonzero
cross-coordinate and constant pairings, so it has a different normalization
from the population-expectation target at finite Q. This implementation does
not claim bitwise equality to that finite-Q initializer. The comparison below
holds its P-node population replay fixed and refines only its coefficient rule.

## Exact folding of an antithetic population rule

For even nominal P, the optional antithetic rule first draws P/2 full joint
Gaussian marks independently in each population, then adds their simultaneous
negatives. This is a P-node integration rule with P/2 independent base draws;
it is not P iid samples. Set `population_rule='antithetic', folded=True` to
store only the base half and omit the inactive constant feature. Shapes become
b1=(P/2,2d), g=(P/2,d), b2=(P/2,d), D=(d,2d), with weights 2/P. Unfolding
uses [base;-base] node order and restores the constant column at index zero.

At initialization g,w and all nonconstant features are odd under mark negation;
c=0 is odd and the constant row/column of M vanish. Suppose this property holds
at a current state. For every input u, h1=tanh(w dot u) is odd, so its constant
feature pairing a0 vanishes. The other b1*h1 pairings are even. Upper z2 and h2
are odd, the upper gate is even, and c is odd. Consequently d0=E[c gate2]=0,
the other b2*c*gate2 pairings are even, and prediction E[c h2] is even. The full
middle velocity is -2 integral r d a^T, so its constant row/column remain zero.
Reverse q is odd; the lower gate is even; hence the lower w velocity is odd.
The c velocity, an integral of h2, is odd. These arguments use arbitrary input
directions and labels: they require no symmetry in the data law.

Thus the vector field preserves this state class. Euler stages, Heun stages,
linear interpolation, and own-state restart preserve it in real arithmetic.
Every required pairing has an even integrand, and its full paired-rule mean
equals its base-half mean. Removing the inactive constants and the negative
half therefore gives exactly the same chosen numerical rule. Floating-point
reduction order can produce roundoff-level discrepancies. Folded dynamics
still require every entry of the full d-by-2d evolving M; no diagonal or rank
constraint is imposed. Sign folding is not applicable to an arbitrary supplied
state outside this invariant class. Defaults remain iid/unfolded in the
initializer; a caller opts into the checked antithetic representation.

## Verification precommitment

Before executing checks, the fixed target is equivalence of block normalization
with dense Cholesky and retention of the source-response term. The competing
failure is an incorrect normalization orientation or missing reverse response.
No training or predictive-accuracy comparison is included in this initializer
check. The engine separately checks nontrivial antithetic folded evolution.

- Dense normalization: d in {1,2,7,17}, P=40, seed=1907, with iid unfolded,
  antithetic unfolded, and antithetic folded rules. Require max absolute error
  below 2e-12 for b1,b2,g,D.
- Initial sign folding: d=7,P=40,seed=1907, require exact matching of stored
  positive-half marks/action and oddness to within 2e-12.
- Coefficient refinement: scalar orders 128 and 256, cutoff10. Require maximum
  difference among the recorded constants/normalization factors below 1e-10.
- Maintained d=2 check: Q=2048,16384,131072, P=256 and identical maintained
  replay clouds. Report every max absolute difference in b1,b2,D. Require final
  maximum below 5e-3; refinement differences are diagnostic, not certified errors.
- Hard execution budget: one check invocation, at most 120 CPU seconds and
  512 MiB process address-space limit, one numerical thread. Failures stop and
  retain the report; a validity failure does not authorize training or searching
  for a favorable configuration.

Command from repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=code \
PYTHONDONTWRITEBYTECODE=1 python -B studies/first_order_dimension_mnist/P1_INITIALIZATION.py \
  --check --output data/generated/first_order_dimension_mnist/initializer_checks
```

`initializer_check.json` records constants, all comparisons, source hash,
environment, runtime and pass/fail. A passing result supports initializer
internal correctness at these cases. General-dimensional approximation quality,
network identification, and learning remain separate unproved questions.

## Recorded initializer checks

The predeclared check passed in 4.70 wall seconds with one numerical thread,
a 120-second CPU limit and a 512-MiB address-space limit. The largest dense
normalization discrepancy was 7.22e-16. Initializer sign folding and unfolding
matched exactly in the checked arrays. The maximum 128-to-256 scalar-rule
change was 1.54e-13 among all constants and normalization coefficients.

| Maintained coefficient nodes Q | Maximum lower-feature difference | Maximum upper-feature difference | Maximum D difference |
| --- | ---: | ---: | ---: |
| 2048 | 0.0105774 | 0.00470397 | 0.00318492 |
| 16384 | 0.00112110 | 0.000392655 | 0.000161994 |
| 131072 | 0.000425679 | 0.0000704167 | 0.000155651 |

These use identical P=256 population replay Gaussian marks across comparisons;
the discrepancy is the maintained finite-Q coefficient/normalization rule.
The reported refinement and matched dense oracle validate the implementation
at the tested finite cases. They do not certify Gaussian integration error or
high-dimensional training accuracy. No training was executed by this check.
