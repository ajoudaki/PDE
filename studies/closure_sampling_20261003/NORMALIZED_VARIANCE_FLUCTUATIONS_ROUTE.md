# Finite-network variance fluctuations under Gaussian activation normalization

2026-10-04. Scoped continuation of the normalized-activation route. The
scientific inputs are the supervisor's finite-network assignment and
`NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md`, frozen at SHA-256
`1e14c318bb8352007c8326d601cd654b865cf40c71d7f0156c2d50305510b4b8`.
No sibling new route, other study, maintained source, or external reference
was read for this continuation. The canonical-notation, neural-network, and
rigorous-proof instructions remain current. No training experiment was run.

The exact finite Gaussian network has a scalar Markov recursion for a single
query's empirical feature norm. Its fixed-depth central limit theorem has
variance coefficient
\[
\sigma^2\sum_{j=0}^{L-1}a^{2j},\qquad
a=\left.\frac d{dq}\mathbb E\phi(\sqrt q Z)^2\right|_{q=1},
\quad \sigma^2=\operatorname{Var}(\phi(Z)^2).
\tag{1}
\]
The two normalized exact GELU branches previously constructed have `a>1`
and `0<a<1`, respectively. Thus the first branch has an exponential-depth
leading fluctuation coefficient for this actual finite-network observable;
the second has a bounded coefficient. This is an initialization statement
for a feature norm, not an output or compression lower bound.

## 1. Network, normalization, and exact transition law

Fix a real input `v` in `R^d` with Euclidean norm one. At initialization
consider `L` hidden layers, each of width `n`:
\[
z^{(1)}=Av,\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\quad(2\le\ell\le L),
\qquad h^{(\ell)}=\phi(z^{(\ell)}).
\tag{2}
\]
The entries of `A` are independent `N(0,1)`, the entries of each
`W^(ell)` are independent `N(0,1/n)`, and all these matrices are
independent. The activation acts coordinatewise. Define the empirical
feature second moment and its depth-zero value by
\[
q_{n,\ell}=\frac1n\sum_{i=1}^n(h_i^{(\ell)})^2,
\qquad q_{n,0}=1.
\tag{3}
\]
This is the squared normalized Euclidean feature norm. The activation
mean is not subtracted.

Assume `phi:R->R` is twice continuously differentiable, its first two
derivatives are bounded, and
\[
\mathbb E[\phi(Z)^2]=\mathbb E[(\phi'(Z))^2]=1,
\qquad Z\sim N(0,1).
\tag{4}
\]
Bounded first derivative gives `|phi(z)|<=C(1+|z|)`. Put
\[
H(z)=\phi(z)^2,\quad
V(q)=\mathbb E H(\sqrt q Z),\quad
\Sigma^2(q)=\operatorname{Var}(H(\sqrt q Z)),\quad q\ge0.
\tag{5}
\]
All fixed moments are finite. In particular `V(1)=1`, and
`sigma^2=Sigma^2(1)` in (1). We use the same activation at all layers.

Conditionally on all preceding layers, the entries of `z^(ell)` are
independent `N(0,q_(n,ell-1))`. This follows directly from the independent
Gaussian rows of `W^(ell)` and
\[
\operatorname{Var}(W_{i,:}^{(\ell)}h^{(\ell-1)}
 \mid h^{(\ell-1)})
=\frac1n\|h^{(\ell-1)}\|_2^2=q_{n,\ell-1}.
\]
At the first layer the variance is `||v||^2=1`.
Thus the process `(q_(n,ell))_(ell=0)^L` has exactly the same joint
distribution as the recursion
\[
q_{n,\ell}=\frac1n\sum_{i=1}^n
 H(\sqrt{q_{n,\ell-1}}Z_{\ell,i}),
\qquad Z_{\ell,i}\overset{\mathrm{iid}}\sim N(0,1).
\tag{6}
\]
The independent Gaussian array in (6) constructs a scalar process with the
same transition kernel and initial value as (3). This distributional
representation remains valid if a variance is zero. It conditions only on
preceding layers, without any matrix-norm event or Gaussian approximation.

## 2. Fixed-depth theorem

Define
\[
\Delta_{n,\ell}=\sqrt n(q_{n,\ell}-1),\qquad
a=V'(1),\qquad \sigma^2=\Sigma^2(1).
\tag{7}
\]
For every fixed finite `L`, as `n->infinity`,
\[
(\Delta_{n,1},\ldots,\Delta_{n,L})
\ \Longrightarrow\ (G_1,\ldots,G_L),
\qquad
G_0=0,\quad G_\ell=aG_{\ell-1}+\xi_\ell,
\tag{8}
\]
where `xi_1,...,xi_L` are independent centered normal variables with
variance `sigma^2`. In particular
\[
\sqrt n(q_{n,L}-1)
\ \Longrightarrow\ N(0,S_L),\qquad
S_L=\sigma^2\sum_{j=0}^{L-1}a^{2j}.
\tag{9}
\]
All limits hold for fixed input dimension, input, activation, and depth.
The notation does not assert a simultaneous or growing-depth central
limit theorem.

The coefficient `a` is
\[
a=\mathbb E[(\phi'(Z))^2+\phi(Z)\phi''(Z)]
=1+\mathbb E[\phi(Z)\phi''(Z)].
\tag{10}
\]
Indeed, differentiating `V(q)` near `q=1` under the Gaussian integral and
integrating by parts gives
\[
V'(q)=\frac1{2\sqrt q}\mathbb E[ZH'(\sqrt q Z)]
=\frac12\mathbb E H''(\sqrt q Z).
\tag{11}
\]
The first two derivative bounds and linear growth imply
`|H'(z)|+|H''(z)|<=C(1+|z|)`, which supplies integrable domination
locally in positive `q`. Thus `V` is continuously differentiable near
one, proving both (10) and the differentiability required below.

The innovation variance is strictly positive. If `sigma^2=0`, then
`phi(Z)^2=1` almost surely by (4); full Gaussian support and continuity
give `phi(z)^2=1` for all `z`. A continuous real function with values
in `{+1,-1}` is constant, contradicting `E phi'(Z)^2=1`.

## 3. Elementary conditional central limit argument

The proof first identifies the new fluctuation contributed by each fresh
Gaussian layer, then linearizes its conditional mean around `q=1`.
Let `F_(n,ell)` be the sigma-algebra generated by the Gaussian rows in
(6) through layer `ell`, and define
\[
\eta_{n,\ell}
=\sqrt n\,[q_{n,\ell}-V(q_{n,\ell-1})].
\tag{12}
\]
Conditionally on `F_(n,ell-1)`, this is the normalized sum of `n`
independent centered variables
`H(sqrt(q_(n,ell-1)) Z)-V(q_(n,ell-1))`.

For a deterministic `q` in a compact interval containing one, quadratic
growth of `H` implies a uniform bound on the third absolute moment of
`H(sqrt(q)Z)-V(q)`. For each fixed real `t`, Taylor's formula for
`exp(ix)`, with third-order remainder bounded by `|x|^3/6`, gives
\[
\mathbb E\exp\!\left\{\frac{it}{\sqrt n}
 [H(\sqrt q Z)-V(q)]\right\}
=1-\frac{t^2\Sigma^2(q)}{2n}+O_t(n^{-3/2}),
\tag{13}
\]
uniformly on that compact interval. Raising to the `n`th power and
using `log(1+u)=u+O(|u|^2)` for small complex `u` gives
\[
\mathbb E[e^{it\eta_{n,\ell}}\mid\mathcal F_{n,\ell-1}]
=\exp\!\left[-\frac{t^2\Sigma^2(q_{n,\ell-1})}{2}
 +O_t(n^{-1/2})\right]
\tag{14}
\]
whenever `q_(n,ell-1)` is in the chosen compact interval.
Gaussian domination makes `Sigma^2(q)` continuous near one.
Consequently, if `q_(n,ell-1)->1` in probability, the conditional
characteristic function in (14) converges in probability to
`exp(-t^2 sigma^2/2)`. Both the conditional characteristic function and
the limit have modulus at most one, so this convergence also holds in
`L^1`: outside an arbitrarily small error event the difference is small,
and its remaining contribution is bounded by twice that event's probability.

We now induct on depth, starting from `Delta_(n,0)=0`. Suppose the vector
of preceding fluctuations already has its claimed joint Gaussian limit.
It is tight, so `q_(n,ell-1)=1+Delta_(n,ell-1)/sqrt(n)->1` in
probability. For every fixed vector of real coefficients `s_j`, the
conditional expectation identity gives
\[
\begin{aligned}
&\mathbb E\exp\!\left(i\sum_{j<\ell}s_j\Delta_{n,j}
                         +it\eta_{n,\ell}\right)\\
&\quad-
e^{-t^2\sigma^2/2}\,
\mathbb E\exp\!\left(i\sum_{j<\ell}s_j\Delta_{n,j}\right)
\longrightarrow0.
\end{aligned}
\tag{15}
\]
The absolute difference is at most the `L^1` conditional-characteristic
function error just proved. Thus the preceding fluctuations and the new
innovation converge jointly, and the new limiting innovation is independent
of all preceding ones. Here the ordinary characteristic-function continuity
criterion is used in its exact form: pointwise convergence to a characteristic
function continuous at the origin implies weak convergence of the corresponding
laws. The candidate limit in (15) is the product of Gaussian characteristic
functions, which satisfies that criterion.

Finally, differentiability of `V` at one gives
\[
\Delta_{n,\ell}
=a\Delta_{n,\ell-1}+\eta_{n,\ell}+o_{\mathbb P}(1).
\tag{16}
\]
To check the remainder explicitly, write
`V(q)-1-a(q-1)=(q-1)r(q)` with `r(q)->0` as `q->1`.
After multiplication by `sqrt(n)` the error is
`Delta_(n,ell-1) r(q_(n,ell-1))`, which tends to zero in probability
because the first factor is tight and the second tends to zero.
Taking the continuous linear map in (16), with this vanishing error,
completes the induction. Iterating the limiting recursion yields
`G_L=sum_(r=1)^L a^(L-r) xi_r`, proving (9). It also yields the
cross-depth covariance
\[
\operatorname{Cov}(G_k,G_\ell)
=\sigma^2\sum_{r=1}^{\min(k,\ell)}a^{k+\ell-2r}.
\tag{17}
\]

## 4. Convergence of the actual finite-network variance

For the GELU applications below, more than convergence in distribution
holds:
\[
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L})=S_L.
\tag{18}
\]
A sufficient additional condition is a globally bounded `H''`; this is
verified below. Under that condition (11) bounds `|V'(q)|` by
`K=(1/2)sup|H''|` for `q>0`. Continuity at zero extends the Lipschitz
bound to all `q>=0`, so
`|V(q)-1|<=K|q-1|`.

Here are the moment details required for (18). Since
`H(sqrt(q)Z)<=C(1+q Z^2)`, Jensen's inequality applied to the average
in (6) gives
\[
\mathbb E[q_{n,\ell}^4\mid\mathcal F_{n,\ell-1}]
\le C(1+q_{n,\ell-1}^4).
\]
Induction shows `sup_n E q_(n,ell)^4<infinity` at every fixed depth.
For the centered summands
`X_i=H(sqrt(q)Z_i)-V(q)`, independence and zero means give the exact
fourth-moment identity
\[
\mathbb E\left[\left(\frac1{\sqrt n}\sum_{i=1}^nX_i\right)^4\right]
=\frac1n\mathbb E X_1^4
 +3\left(1-\frac1n\right)(\mathbb E X_1^2)^2
\le C(1+q^4).
\tag{19}
\]
Consequently `sup_n E eta_(n,ell)^4` is finite for each fixed layer.
The exact definition (12) and the global Lipschitz bound imply
\[
|\Delta_{n,\ell}|\le K|\Delta_{n,\ell-1}|+|\eta_{n,\ell}|.
\]
Using `(x+y)^4<=8(x^4+y^4)` proves
`sup_n E Delta_(n,ell)^4<infinity` by induction. In particular
\[
\sup_n\mathbb E[\Delta_{n,\ell}^2
 1_{\{|\Delta_{n,\ell}|>R\}}]
\le\frac{\sup_n\mathbb E\Delta_{n,\ell}^4}{R^2}
\longrightarrow0.
\]
Truncating the first and second moments, using (8) for bounded continuous
truncations, and then sending `R->infinity` now gives
`E Delta_(n,L)->0` and `E Delta_(n,L)^2->S_L`.
Since `n Var(q_(n,L))=Var(Delta_(n,L))`, this proves (18).

These moment bounds may depend on the fixed depth. No bound uniform in
`L` was used to obtain the fixed-depth limit.

## 5. Exact normalized GELU gives both regimes

Let `varphi(z)=(2pi)^(-1/2)exp(-z^2/2)` and
`Phi(z)=int_(-infinity)^z varphi(x)dx` on the real axis. Write
\[
D=\frac13+\frac2{3\pi\sqrt3},\qquad
b_\pm=-\frac1{2\sqrt\pi}
 \pm\sqrt{\frac1{4\pi}+\frac1{6\pi\sqrt3}},\qquad
\phi_\pm(z)=\frac{z\Phi(z)+b_\pm}{\sqrt D}.
\tag{20}
\]
The preceding frozen route proves both identities (4) exactly, together
with bounded derivatives on every fixed complex strip. In particular the
real first two derivatives required here are bounded.

For completeness the ingredients that determine the new coefficient are
\[
g(z)=z\Phi(z),\quad g'(z)=\Phi(z)+z\varphi(z),\quad
g''(z)=(2-z^2)\varphi(z),
\]
\[
\mathbb E g''(Z)=\frac3{4\sqrt\pi},\qquad
\mathbb E[g(Z)g''(Z)]=\frac1{6\pi\sqrt3}.
\]
These are Gaussian integrals, proved in the frozen route. Substitution
into (10) gives the exact values
\[
a_\pm
=1+\frac{\frac1{6\pi\sqrt3}+
                \frac{3b_\pm}{4\sqrt\pi}}D.
\tag{21}
\]
Their innovation variances are the explicit positive finite Gaussian
integrals
\[
\sigma_\pm^2
=\frac1{D^2}\int_{\mathbb R}
  (z\Phi(z)+b_\pm)^4\varphi(z)\,dz-1.
\tag{22}
\]
Finiteness follows from linear growth, and strict positivity was proved
after (11).

The signs of (21) do not depend on numerical approximation. Set
`A=1/(4pi)` and `c=1/(6pi sqrt(3))`. Then
`b_+=sqrt(A+c)-sqrt(A)>0`, so `a_+>1`. For the minus branch the
numerator added to `D` in (21) is
\[
c-\frac32\sqrt A(\sqrt A+\sqrt{A+c})<0,
\]
because `c<3A`. Its negative is less than `D`: the arithmetic-geometric
mean bound `sqrt(A(A+c))<=A+c/2` makes it at most
`3A-c/4<1/3<D`. Hence `0<a_-<1` exactly. The previously checked
decimal values are
\[
a_+=1.1134920638\ldots,\qquad a_-=0.4971840106\ldots.
\tag{23}
\]

The stronger moment assertion (18) also applies. Indeed
\[
(\phi_\pm^2)''
=\frac2D\left[(g')^2+(g+b_\pm)g''\right]
\]
is bounded on the real axis: `g'` is bounded, `|g(z)|<=|z|`, and
`g''(z)=(2-z^2)varphi(z)` decays faster than any polynomial.

Combining (9), (18), and (21)--(22) gives
\[
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L}^{\,+})
=\sigma_+^2\frac{a_+^{2L}-1}{a_+^2-1},
\qquad
\lim_{n\to\infty}n\operatorname{Var}(q_{n,L}^{\,-})
=\sigma_-^2\frac{1-a_-^{2L}}{1-a_-^2}.
\tag{24}
\]
Here the superscripts identify the activation branch; every other part of
the canonical initialization is unchanged. First take width to infinity
at each fixed `L`. The resulting variance coefficient then grows
exponentially as `L->infinity` for the plus branch, and remains bounded
by `sigma_-^2/(1-a_-^2)` for the minus branch. The limiting standard
deviation coefficient for the plus branch grows proportionally to `a_+^L`.

As an exact boundary check, identity has `H(z)=z^2`, `a=1`, and
`sigma^2=2`, hence `S_L=2L`. In this case (6) also gives exactly a
product of `L` independent copies of `chi_n^2/n`, so
`Var(q_(n,L))=(1+2/n)^L-1`. Its fixed-depth limit after multiplication
by `n` is indeed `2L`.

## 6. Meaning and limits of the obstruction

The plus-branch GELU example rules out a universal polynomial in depth
bound on the coefficient
`lim_(n->infinity) n Var(q_(n,L))` under only the two moment identities
(4), even with the supplied analytic-strip derivative regularity. More
concretely, no constants `C,k` independent of depth can bound this
coefficient by `C(1+L)^k` for that fixed activation. Allowing a
depth-dependent threshold for sufficiently large width does not change
this conclusion, since (24) is already the fixed-depth width limit.

The additional scalar condition `|V'(1)|<=1` precisely prevents this
specific initialized fluctuation coefficient from growing exponentially:
it gives `S_L<=sigma^2 L`, and strict inequality `|V'(1)|<1` makes
`sup_L S_L` finite. It is a necessary diagnostic for that coefficient,
not a sufficient criterion for an all-time polynomial-depth compressor.

In particular the canonical readout is initialized at zero. Its output
is then identically zero for every realization, despite the feature-norm
fluctuations established here. A compressor compares against the same
realized reference and may retain its initial features exactly. Thus (24)
is neither a lower bound on output error nor a lower bound on retained
coordinates or runtime. It does not address training, joint limits in
depth and width, the whole query sphere, higher response-moment summation,
or stability of the compressed optimizer. It identifies a concrete
finite-network estimate that cannot be obtained merely by replacing all
layer gains with one from (4).
