# General-dimensional p=1 initialized coefficients and finite computation

This is a finite initialized-algebra specialization of
[Global nonlinear learning, C.4.7.10.B](global_nonlinear.md#c4710-finite-numerical-autonomous-observable-closure).
The notation contract is [NOTATION.md](NOTATION.md). Here p=1 is closure
order, P is population integration count, n is neural width, d is input
dimension, and m is sample count. These quantities are independent. The older
hierarchy uses N for order and p for arithmetic digits; those are not the p
and P used here. No general-d trained-network limit, general-d higher-order
hierarchy, fixed-p rotation invariance, or approximation guarantee is asserted.

The network is bias-free with two tanh hidden layers, first weights N(0,1),
stored middle entries N(0,1/n), stored readout N(0,1/n²), and output cᵀh2/n.
All entries are mutually independent at initialization. Inputs are U rows
u=x/sqrt(d); arbitrary finite rows, including zero and duplicates, are allowed.
Loss is the unhalved weighted square sum sum_a mu_a(f_a-y_a)² with fixed
nonnegative mu of total mass one; uniform mu gives the ordinary mean. Physical
block mobilities are (n,1,n). The population readout starts at zero, the limit
of the random finite readout; a finite comparator retains that random readout.
Equal seed integers do not couple these different initial finite objects.

The proof has three steps: use the finite Gaussian source rule to compute the
joint initialized coordinates and raw contraction; normalize repeated scalar
Gram blocks; then identify the invariant sign-paired finite representation.
All coefficient identities below concern exact expectations. The executable
quadrature and population rules are distinct finite approximations.

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
In the finite source rule of [Section 3](global_nonlinear.md#3-finite-gaussian-calculations-with-adaptive-reuse), \(E h_i h_j=v\delta_{ij}\), so the forward
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
Indeed T0=1 and T1(z)=z, and graded descending-lexicographic exponent order
lists the zero exponent followed by each coordinate in the displayed order.
The decoder's codes 0 and 1 are the constants on populations 1 and 2, already
the first retained entries. There are therefore no extra tails at this order;
all action dependencies are the displayed forward/reverse core. The complete
maintained dictionary/decoder definitions are in `observable_initialization.py`
and `observable_words.py`. Their core dispatch does not invoke the generic
source compiler here. Every source-rule input is a finite composition
of tanh and linear maps with bounded first derivatives. The roots are Gaussian
and have all moments. Thus the finite smooth-program hypotheses of Section 3
hold; no evolving-time program or unbounded query count is imported.

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

`pde.observable_p1_initialization.initialize(d, particles, seed, ...)` returns b1,g,p1,b2,p2,D
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
or d³ Cholesky in production. The maintained deterministic test reconstructs the full exact-block Gram and
performs dense Cholesky for small verification cases.
Population sampling is a separate resolution axis from coefficient quadrature.

The maintained d=2 initializer estimates all coefficients and full Grams using
a finite Q-node joint Halton rule. Its finite-Q Gram generally has nonzero
cross-coordinate and constant pairings, so it has a different normalization
from the population-expectation target at finite Q. This implementation does
not claim bitwise equality to that finite-Q initializer. Comparisons between those implementations must distinguish coefficient-rule
error from population replay error; the two finite initializers are not identical.

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

## Finite equations, metric and numerical meaning

Allow arbitrary finite feature dimensions K1,K2 and stored population counts
P1,P2. Freeze the row tables B1 in R^(P1×K1), g in R^(P1×d), B2 in
R^(P2×K2), D in R^(K2×K1), and population weights pi1,pi2 of total mass
one. Rows of B1,B2 are the transposes of the feature columns b1,b2 above.
The moving state is w in R^(P1×d), c in R^P2, M in R^(K2×K1).
For each input u define, writing diag(pi) for a diagonal weight matrix,

\[
 h_1=\tanh(wu),\quad a=B_1^T\operatorname{diag}(\pi_1)h_1,
 \quad h_2=\tanh(B_2Ma),\quad f=\pi_2^T(c\odot h_2),
\]
\[
 \upsilon=B_2^T\operatorname{diag}(\pi_2)
             [c\odot(1-h_2^2)],\qquad q=B_1M^T\upsilon.
\]

The executable names for a, upsilon, q are `a,d,q`; that `d` is an array
name, not input dimension. With r_a=f(u_a)-y_a and all input-indexed quantities
evaluated at u_a, the exact finite vector field is

\[
 \dot w_i=-2\sum_a\mu_a r_a(1-h_{1,ia}^2)q_{ia}u_a^T,
 \qquad \dot c_j=-2\sum_a\mu_a r_a h_{2,ja},\qquad
 \dot M=-2\sum_a\mu_a r_a\upsilon_a a_a^T.
\]

These are the H3.N2 equations with arbitrary supplied finite dimensions. Both
orientations use this same full M. To verify the metric, differentiate f:
its c_j derivative is pi2_j h2_j; its M derivative is upsilon aᵀ; its w_i
row derivative is pi1_i(1-h1_i²)q_i uᵀ. Differentiating the weighted loss
multiplies by 2 mu_a r_a and sums over inputs. Thus at positive population
weights the row/readout equations are negative population-L2 gradients and
the matrix equation is the negative Frobenius gradient. Substitution,
including zero-weight rows by direct multiplication rather than division,
gives the exact real-arithmetic identity

\[
 \frac{d\mathcal L}{dt}
 =-\sum_i\pi_{1i}|\dot w_i|^2
  -\sum_j\pi_{2j}|\dot c_j|^2-\|\dot M\|_F^2.
\]

No global numerical stability or general-dimensional network identification is
inferred. The implementation uses simultaneous explicit Heun:
Y*=Y+h V(Y), Ynew=Y+(h/2)[V(Y)+V(Y*)]. All three moving blocks use
the same old state at each stage. This is a numerical GF integrator, not an
exact finite-time flow or literal raw GD step. Finite steps need not decrease
loss. Float32/64, quadrature, finite population integration, closure order and
finite network width are separate error sources. No tolerance selector or
combined limit follows from a successful deterministic check.

For the comparator, write delta2=c(1-h2²),
delta1=(Mᵀdelta2)(1-h1²). Direct differentiation of f=cᵀh2/n gives
w_dot=-2 sum mu r delta1 uᵀ,
c_dot=-2 sum mu r h2,
M_dot=-(2/n) sum mu r delta2 h1ᵀ after multiplying the gradients by
(n,1,n). These retain the complete n×n matrix and its actual transpose.
Ordinary Torch derivatives use 1-tanh²; cancellation at saturation and
intermediate matrix overflow remain possible, unlike some specialized range
protection in the NumPy reference.

## Observations, restart and cost

Hidden pairs are (initial,current) on the same population marks and same input.
The upper initial activation is reconstructed with g and D. Pair weights are
the product of the returned population and input probabilities. For a folded
state the observation API explicitly returns both signs with half base
weights; returning only positive-half pairs would not give the full signed
joint law. Grams are uncentered E_l[h_l(u)h_l(v)], with initial/current cross
Grams ordered initial rows and current columns. RMS is the square root of the
weighted paired squared displacement. A finite panel supplies no full-domain
norm bound. The current/frozen arrays and complete representation/arithmetic
metadata determine continuation; no source program, prior predictions or
history is required. Exact working-state replay requires identical device
and reduction environment, arithmetic policy, association, blocks and steps.

The closure moving state uses P1*d+P2+K1*K2 scalar entries. Frozen marks,
probabilities, D, cached weighted b1 transpose and b2 transpose add
2*P1*K1+P1*d+2*P2*K2+P1+P2+K1*K2. For equal unfolded P,
K1=2d+1,K2=d+1, their total is P(8d+7)+2(d+1)(2d+1).
For folded nominal P with B=P/2 base rows, K1=2d,K2=d, it is
8Bd+3B+4d²; moving entries alone are B(d+1)+2d². These count tensor
entries even if an allocator shares a transpose. Python metadata and allocator
workspaces are additional. The network moving count is nd+n²+n; its retained
initial state adds another copy. Data add O(md+m). Heun uses a bounded number
of state copies. A k-input observation panel can add O((P1+P2)k+k²), doubled
pair rows when unfolded for output. Saved trajectories grow with observations;
they are not needed by the autonomous current state.

Direct RHS work at p=1 and equal populations is O(m(Pd+d²)); input blocks
bound activation workspace. Optional precontractions b1 Mᵀ or b2 M cost
O(Pd²) to form and store their full O(Pd) output. Actual step count multiplies
cost over a physical horizon. At P=n, removing a neural n² term is useful at
fixed d; there is no uniform joint (d,n) advantage or cost-to-accuracy result.

The [implementation guide](../code/GENERAL_P1.md) supplies complete examples,
finite checks and interpretation of prediction/Gram comparisons. Equal-time,
separately selected checkpoint, fixed-reference training-loss matching, and
common training-loss matching of every system are different comparisons.
Attained-loss matching alone proves neither equality of maps nor a pure
change of clock. No MNIST/PCA numerical result or performance ratio is claimed
by this addition.
