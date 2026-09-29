# Finite-block initialization: kernel bias and sampling fluctuations

This is a self-contained, internally checked initialization result for the
assigned study. It does not make a training claim. Its inputs are the scoped
assignment and the solve-math-rigorously skill; it uses no other study or
external research result.

## Model and assumptions

Fix inputs \(x^1,\ldots,x^m\in\mathbb R^d\), a depth \(L\geq1\), and
integers \(B,k\geq1\), with hidden width \(n=Bk\). There are no biases.
The rows of the first weight matrix are independent \(N(0,I_d)\), and

\[
h_{1,i}(x)=\phi_1\!\left(W_{1,i}x/\sqrt d\right).
\]

At every later layer the weight matrix is block diagonal, using the same
partition into \(B\) blocks of size \(k\). Every block has independent
\(N(0,1/k)\) entries. All blocks, layers, and first-layer rows are mutually
independent. At these layers the normalization is already in the weights:
\(h_\ell=\phi_\ell(W_\ell h_{\ell-1})\).

The standard first-row covariance is an explicit normalization choice.
For any other centered Gaussian row covariance, replace the deterministic
matrix below by its actual first-layer preactivation covariance. The proof
is otherwise unchanged. Layer independence and block alignment are essential
model assumptions; rowwise Gaussianity alone does not supply them.

For a representative block write its feature vectors across the inputs as
\(Y_{\ell,i}=(h_{\ell,i}(x^a))_{a=1}^m\), and define

\[
S_\ell=\frac1k\sum_{i=1}^kY_{\ell,i}Y_{\ell,i}^{\mathsf T},\qquad
S_0=K_0,\qquad (K_0)_{ab}=\frac{\langle x^a,x^b\rangle}{d}.
\]

For a positive semidefinite \(m\times m\) matrix \(Q\), let

\[
T_\ell(Q)_{ab}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\qquad Z\sim N(0,Q),\qquad K_\ell=T_\ell(K_{\ell-1}).
\]

The matrix \(K_\ell\) is the dense infinite-width covariance recursion;
the block-population kernel is
\(K_\ell^{(k)}=\mathbb E S_\ell\). Positive semidefinite here permits
singular matrices. In particular, neither distinct inputs nor \(k\geq m\)
is assumed.

For the main theorem, assume
\(\phi_\ell\in C_b^4(\mathbb R)\), meaning that the activation and its
derivatives through order four are continuous and bounded. Put

\[
M_{\ell,r}=\|\phi_\ell^{(r)}\|_\infty\quad(0\leq r\leq4),
\qquad
A_\ell=M_{\ell,0}M_{\ell,2}+M_{\ell,1}^2,
\]
\[
C_\ell
=\frac12M_{\ell,0}M_{\ell,4}
 +2M_{\ell,1}M_{\ell,3}
 +\frac32M_{\ell,2}^2.
\]

These are sufficient hypotheses, not a claim that four derivatives are
necessary. A bounded \(C^{1,1}\) variant appears below. ReLU is not covered
by either stated activation assumption.

The first-layer activation needs no derivatives for these results: it
may instead be any bounded Borel function. In that case set
\(V_1=M_{1,0}^4\), \(D_1=0\), and introduce the derivative bounds and
recursions only at layers \(\ell\geq2\).

## Main estimates

Define explicit depth constants by

\[
V_0=D_0=0,\qquad
V_\ell=M_{\ell,0}^4+A_\ell^2V_{\ell-1},\qquad
D_\ell=A_\ell D_{\ell-1}+\frac{C_\ell}{2}V_{\ell-1}.
\tag{1}
\]

For every \(B,k,m,d,L\) and every \(1\leq\ell\leq L\),

\[
\max_{a,b}\mathbb E|(S_\ell-K_\ell)_{ab}|^2
\leq \frac{V_\ell}{k},\qquad
\max_{a,b}|(K_\ell^{(k)}-K_\ell)_{ab}|
\leq\frac{D_\ell}{k}.
\tag{2}
\]

Consequently,

\[
\mathbb E\|S_\ell-K_\ell\|_F^2
\leq\frac{m^2V_\ell}{k},\qquad
\|K_\ell^{(k)}-K_\ell\|_F
\leq\frac{mD_\ell}{k}.
\tag{3}
\]

The constants in (1) do not depend on \(B,k,m,d\), or the input values.
The displayed \(m\)-factors account for all input-dimension dependence in
the Frobenius estimates. The first layer is exactly unbiased: \(D_1=0\).

Let \(S_\ell^{[1]},\ldots,S_\ell^{[B]}\) denote the actual block Grams
and let \(\widehat K_{\ell,B,k}=B^{-1}\sum_{q=1}^B S_\ell^{[q]}\),
the empirical Gram of all \(n\) hidden neurons. Then

\[
\mathbb E\widehat K_{\ell,B,k}=K_\ell^{(k)},\qquad
\mathbb E\|\widehat K_{\ell,B,k}-K_\ell^{(k)}\|_F^2
\leq\frac{m^2V_\ell}{Bk},
\tag{4}
\]
\[
\mathbb E\|\widehat K_{\ell,B,k}-K_\ell\|_F^2
\leq\frac{m^2V_\ell}{Bk}+\frac{m^2D_\ell^2}{k^2}.
\tag{5}
\]

Thus the requested sample-block variance \(O(B^{-1})\) has the stronger
bound \(O((Bk)^{-1})\). Increasing \(B\) removes block sampling noise;
the expectation \(K_\ell^{(k)}\) itself is independent of \(B\).
At fixed \(k\), (5) is a bias bound and does not assert that this bias
vanishes as \(B\to\infty\).

Because the constants do not depend on the inputs, the population bound
is uniform on the entire input space. More precisely, for each layer,

\[
\sup_{x,x'\in\mathbb R^d}
 |K_\ell^{(k)}(x,x')-K_\ell(x,x')|
\leq\frac{D_\ell}{k}.
\tag{5a}
\]

Indeed, apply the two-input form of (2) to each fixed pair \((x,x')\)
with the same constant. Similarly, writing \(n=Bk\), the empirical
kernel satisfies the uniform pointwise root-mean-square estimate

\[
\sup_{x,x'\in\mathbb R^d}
 \left(\mathbb E|\widehat K_{\ell,B,k}(x,x')
                         -K_\ell(x,x')|^2\right)^{1/2}
\leq\left(\frac{V_\ell}{n}+\frac{D_\ell^2}{k^2}\right)^{1/2}
\leq\frac{D_\ell}{k}+\sqrt{\frac{V_\ell}{n}}.
\tag{5b}
\]

The supremum in (5b) is outside the expectation. These arguments do
not bound the expected supremum of empirical errors over an input
class; that is a different sampling question. Inputs in the preceding
finite-matrix bounds are deterministic, or independent of the network
initialization after conditioning on the inputs.

For example, Markov's inequality applied to (4) gives, for every \(t>0\),

\[
\mathbb P\!\left(
 \|\widehat K_{\ell,B,k}-K_\ell\|_F>
 \frac{mD_\ell}{k}+t\right)
\leq\frac{m^2V_\ell}{Bk\,t^2}.
\tag{6}
\]

If the activation bounds are uniform across layers, with
\(M_{\ell,0}\leq M\), \(A_\ell\leq A\), and \(C_\ell\leq C\), then
the completely explicit choices

\[
V_\ell\leq M^4\sum_{j=0}^{\ell-1}A^{2j},\qquad
D_\ell\leq\frac{CM^4}{2}
\sum_{r=1}^{\ell-1}A^{\ell-1-r}
 \sum_{j=0}^{r-1}A^{2j}
\tag{7}
\]

follow by substitution into (1). Empty sums are zero and a zeroth power
is one. At \(A=1\), these are
\(V_\ell\leq M^4\ell\) and
\(D_\ell\leq CM^4\ell(\ell-1)/4\).
If \(0\leq A<1\), the depth-uniform bounds
\(V_\ell\leq M^4/(1-A^2)\) and
\(D_\ell\leq CM^4/[2(1-A)(1-A^2)]\) are valid.
Without such a stability condition, (1) or (7), rather than an implicit
depth-uniform constant, specifies the depth dependence.

## Proof

The proof uses the exact conditional Gaussian law inside one block. A
covariance interpolation formula gives a Lipschitz estimate for its mean
and a quadratic Taylor remainder. Conditional sampling noise contributes
\(k^{-1}\); its first-order mean is zero. The Taylor remainder therefore
propagates a \(k^{-1}\) bias rather than the \(k^{-1/2}\) scale of a
typical block fluctuation.

### Gaussian interpolation, including singular endpoints

For \(f\in C_b^4(\mathbb R^p)\), positive semidefinite \(Q_0,Q_1\),
\(H=Q_1-Q_0\), and \(Q_t=Q_0+tH\), write
\(G_f(Q)=\mathbb E f(N(0,Q))\). Along this segment,

\[
\frac{d}{dt}G_f(Q_t)
=\frac12\sum_{i,j=1}^p H_{ij}
  \mathbb E[\partial_{ij}f(N(0,Q_t))],
\tag{8}
\]
\[
\frac{d^2}{dt^2}G_f(Q_t)
=\frac14\sum_{i,j,r,s=1}^p H_{ij}H_{rs}
 \mathbb E[\partial_{ijrs}f(N(0,Q_t))].
\tag{9}
\]

To verify these identities first replace \(Q_t\) by
\(Q_{t,\varepsilon}=Q_t+\varepsilon I\). Its Gaussian density
\(p_t(z)\) satisfies

\[
\partial_t p_t(z)=\frac12
 \left[z^{\mathsf T}Q_{t,\varepsilon}^{-1}H
 Q_{t,\varepsilon}^{-1}z-
 \operatorname{tr}(Q_{t,\varepsilon}^{-1}H)\right]p_t(z)
=\frac12\sum_{i,j}H_{ij}\partial_{ij}p_t(z).
\]

This follows by differentiating the determinant and quadratic exponent
in the Gaussian density. Integrating twice by parts proves (8); applying
the same argument to each \(\partial_{ij}f\) proves (9). Gaussian tails
and bounded derivatives justify the integrations by parts, for example
by first multiplying by compact cutoffs and then sending their support
to infinity. For fixed \(\varepsilon>0\), differentiation under the
integral is justified by Gaussian integrable bounds, uniform for
\(t\in[0,1]\).

To remove \(\varepsilon\), couple each Gaussian as
\((Q_t+\varepsilon I)^{1/2}U\), \(U\sim N(0,I_p)\).
The positive semidefinite square root is continuous, including at
singular matrices: on a common bounded spectral interval it is the
uniform limit of polynomials approximating the scalar square root.
Every expectation in (8)–(9) therefore converges by bounded convergence.
The derivative right-hand sides are bounded uniformly in
\(t,\varepsilon\), so their integral identities and Taylor formulas pass
to the limit by dominated convergence. Continuity of the limiting
right-hand sides gives (8)–(9), with one-sided derivatives at endpoints.
This proves the formulas on the entire positive semidefinite cone; an
inverse of a sample Gram is never used.

### Entrywise covariance-map bounds

Suppress the layer subscript temporarily. For \(a\ne b\), the entry
\(T(Q)_{ab}\) is the two-dimensional Gaussian expectation of
\(f(u,v)=\phi(u)\phi(v)\). Define

\[
w_{ab}(H)=\frac{M_0M_2}{2}(|H_{aa}|+|H_{bb}|)
                         +M_1^2|H_{ab}|.
\]

Formula (8) gives

\[
\left|T(Q+H)_{ab}-T(Q)_{ab}\right|\leq w_{ab}(H),
\qquad
\left|DT(Q)_{ab}[H]\right|\leq w_{ab}(H),
\tag{10}
\]

whenever \(Q,Q+H\) are positive semidefinite. Here \(DT(Q)[H]\)
means the linear expression in (8), so it is defined at singular \(Q\)
as well. For \(a=b\), use the scalar function \(f(u)=\phi(u)^2\):
\(f''=2(\phi')^2+2\phi\phi''\), and replace
\(w_{aa}(H)\) by \(A|H_{aa}|\).

For a two-dimensional covariance direction, the second directional
derivative in (9) is obtained by applying
\((\tfrac12H_{aa}\partial_{uu}+H_{ab}\partial_{uv}
+\tfrac12H_{bb}\partial_{vv})^2\) to \(f\). Its absolute value is at
most

\[
\begin{split}
q_{ab}(H)={}&\frac{M_0M_4}{4}(H_{aa}^2+H_{bb}^2)
 +M_2^2\left(H_{ab}^2+\frac12|H_{aa}H_{bb}|\right)\\
&+M_1M_3\left(|H_{aa}H_{ab}|+|H_{bb}H_{ab}|\right).
\end{split}
\tag{11}
\]

For a diagonal entry the bound is \(q_{aa}(H)=CH_{aa}^2\), since
\((\phi^2)''''=2\phi\phi''''+8\phi'\phi'''+6(\phi'')^2\).
Consequently the Taylor remainder

\[
R_{ab}(Q,H)=T(Q+H)_{ab}-T(Q)_{ab}-DT(Q)_{ab}[H]
\]

satisfies \(|R_{ab}(Q,H)|\leq q_{ab}(H)/2\).

In particular, let \(H\) be a random symmetric matrix such that
\(Q+H\) is positive semidefinite almost surely, and suppose
\(\max_{i,j}\mathbb E H_{ij}^2\leq v\). Minkowski's inequality applied
to (10), and Cauchy–Schwarz applied to every product in (11), imply

\[
\mathbb E|T(Q+H)_{ab}-T(Q)_{ab}|^2\leq A^2v,
\qquad
\mathbb E|R_{ab}(Q,H)|\leq\frac C2v.
\tag{12}
\]

The second inequality uses that the coefficients in (11) sum to
\(C\). This step avoids bounding the expectation of a maximum over all
\(m^2\) entries and is the reason the per-entry constants are
dimension free. If \(b=\max_{i,j}|\mathbb E H_{ij}|\), the deterministic
linear functional in (10) also gives

\[
|DT(Q)_{ab}[\mathbb E H]|\leq Ab.
\tag{13}
\]

### Exact block recursion and induction

Condition on all features in a block through layer \(\ell-1\). For
each new row, its preactivation vector across the \(m\) inputs is a
linear combination of independent centered Gaussian weights. Its
conditional covariance is

\[
\mathbb E[z_{\ell,i,a}z_{\ell,i,b}\mid\mathcal F_{\ell-1}]
=\frac1k\sum_{j=1}^k h_{\ell-1,j}(x^a)h_{\ell-1,j}(x^b)
=(S_{\ell-1})_{ab}.
\]

Different new rows use independent weights, so their preactivation
vectors are conditionally independent. Their joint conditional law
depends on the past only through \(S_{\ell-1}\). For the first layer
the same statement holds with the deterministic covariance \(K_0\).
Thus, exactly at every layer,

\[
\mathbb E[S_\ell\mid\mathcal F_{\ell-1}]
=T_\ell(S_{\ell-1}),\qquad
S_\ell=T_\ell(S_{\ell-1})+\xi_\ell,
\quad\mathbb E[\xi_\ell\mid\mathcal F_{\ell-1}]=0.
\tag{14}
\]

Each entry of \(S_\ell\) is a mean of \(k\) conditionally independent
variables of absolute value at most \(M_{\ell,0}^2\). Therefore

\[
\mathbb E[\xi_{\ell,ab}^2\mid\mathcal F_{\ell-1}]
=\frac1k\operatorname{Var}
  (Y_{\ell,1,a}Y_{\ell,1,b}\mid\mathcal F_{\ell-1})
\leq\frac{M_{\ell,0}^4}{k}.
\tag{15}
\]

Let
\(v_\ell=\max_{a,b}\mathbb E|(S_\ell-K_\ell)_{ab}|^2\) and
\(b_\ell=\max_{a,b}|\mathbb E(S_\ell-K_\ell)_{ab}|\).
The cross term between \(\xi_\ell\) and any measurable function of
the past has expectation zero by (14). Applying (12) to
\(H=S_{\ell-1}-K_{\ell-1}\) therefore gives

\[
v_\ell\leq\frac{M_{\ell,0}^4}{k}+A_\ell^2v_{\ell-1}.
\tag{16}
\]

Taking expectations in the Taylor expansion and then using (12)–(13)
gives

\[
b_\ell\leq A_\ell b_{\ell-1}+\frac{C_\ell}{2}v_{\ell-1}.
\tag{17}
\]

Since \(v_0=b_0=0\), induction in (16)–(17) proves (1)–(2).
Summing entrywise squares proves (3).

Every block uses its own disjoint first-layer rows and later-layer
weights. The block Grams at a given layer are therefore independent and
identically distributed. Hence their entrywise variances average with
an exact factor \(B^{-1}\), and

\[
\mathbb E\|\widehat K_{\ell,B,k}-K_\ell^{(k)}\|_F^2
=\frac1B\sum_{a,b}\operatorname{Var}(S_{\ell,ab})
\leq\frac1B\sum_{a,b}\mathbb E|(S_\ell-K_\ell)_{ab}|^2.
\]

This proves (4). The centered fluctuation is orthogonal in expectation
to the deterministic bias, so the squared error relative to \(K_\ell\)
is the sum of variance and squared bias. Equation (3) then proves (5).

## A general smooth weak-observable estimate

The same reasoning applies beyond entries of the forward kernel. Let
\(Z_\ell^{(k)}\) be one preactivation vector from layer \(\ell\), so
conditionally it is \(N(0,S_{\ell-1})\). For
\(f\in C_b^4(\mathbb R^m)\), define

\[
a_f=\frac12\sum_{i,j}\|\partial_{ij}f\|_\infty,
\qquad
c_f=\frac18\sum_{i,j,r,s}\|\partial_{ijrs}f\|_\infty.
\]

Equations (8)–(9), Taylor's formula, and
\(\mathbb E|H_{ij}H_{rs}|\leq V_{\ell-1}/k\) give

\[
\left|\mathbb E f(Z_\ell^{(k)})
 -\mathbb E f(N(0,K_{\ell-1}))\right|
\leq\frac{a_fD_{\ell-1}+c_fV_{\ell-1}}{k}.
\tag{18}
\]

The constants are explicit: if all second and fourth partial
derivatives are bounded by \(F_2,F_4\), respectively, then
\(a_f\leq m^2F_2/2\) and \(c_f\leq m^4F_4/8\).
If \(f\) depends on only \(r\) specified inputs, replace \(m\) by
\(r\) in these counts. Equation (18) follows directly from the stated
Taylor coefficients and does not require a limit theorem for individual
neurons.

## Bounded \(C^{1,1}\) activations under pairwise nondegeneracy

There is a weaker regularity version with the same \(k^{-1}\) rates.
Assume now that each \(\phi_\ell\) is bounded and continuously
differentiable, with bounded derivative and globally Lipschitz
derivative. Define
\(M_{\ell,0}=\|\phi_\ell\|_\infty\),
\(M_{\ell,1}=\|\phi_\ell'\|_\infty\), and
\(M_{\ell,2}=\operatorname{Lip}(\phi_\ell')\), and retain
\(A_\ell=M_{\ell,0}M_{\ell,2}+M_{\ell,1}^2\).

For each \(\ell\geq2\), suppose there is a specified
\(\lambda_{\ell-1}>0\) such that every two-input principal submatrix
of \(K_{\ell-1}\) is at least \(\lambda_{\ell-1}I_2\), and every
diagonal entry is at least \(\lambda_{\ell-1}\). When \(m=1\), only
the scalar condition is needed. These conditions concern the dense
reference covariances, not the random finite-block Grams. They must be
checked in an application; duplicated inputs generally violate the
two-input condition. Full \(m\times m\) positive definiteness is not
needed.

Use the same \(V_\ell\) recursion in (1), set \(D_0=D_1=0\), and for
\(\ell\geq2\) replace its bias recursion by

\[
D_\ell=A_\ell D_{\ell-1}
 +\frac{\sqrt2 A_\ell}{\lambda_{\ell-1}}V_{\ell-1}.
\tag{19}
\]

Then the finite-input estimates (2)–(5) and (6) hold with these constants.
The input-uniform conclusions (5a)–(5b) require nondegeneracy bounds
uniform over the input pairs under consideration; they do not follow
from nondegeneracy on a fixed input array. In the one-input case the
coefficient \(\sqrt2\) in (19) can be replaced by \(1/\sqrt2\).
The first layer remains exactly unbiased and requires no nondegeneracy
assumption. Mixed layers may use either their \(C_b^4\) coefficient
\(C_\ell/2\) or, if available, their coefficient in (19).

Here is a proof with the endpoint issue made explicit. Convolving an
activation with a nonnegative smooth compactly supported mollifier
gives smooth bounded activations with the same bounds on
\(M_0,M_1,M_2\). The activations and first derivatives converge
uniformly. Applying (10) to these approximations and taking the limit
proves the same global covariance Lipschitz estimate. Thus (15)–(16)
and the \(V_\ell\) bounds remain valid even at singular covariances.

It remains to obtain a quadratic Taylor bound at a nondegenerate
reference pair \(Q\succeq\lambda I_p\), with \(p=2\) off the diagonal
and \(p=1\) on it. Put \(Q_t=Q+tH\), assume \(Q+H\succeq0\), and
consider first a smooth mollified activation. For \(t<1\),
\(Q_t\succeq(1-t)\lambda I_p\). If
\(\mathcal L_Hf=\tfrac12\sum H_{ij}\partial_{ij}f\), differentiating
its Gaussian expectation using the density gives

\[
\frac{d^2}{dt^2}G_f(Q_t)
=\frac12\mathbb E\left[
 (\mathcal L_H f)(Q_t^{1/2}U)
 \left\{U^{\mathsf T}Q_t^{-1/2}HQ_t^{-1/2}U
       -\operatorname{tr}(Q_t^{-1/2}HQ_t^{-1/2})\right\}\right].
\tag{20}
\]

For any symmetric \(R\), orthogonal diagonalization and independent
standard normal coordinates show
\(\mathbb E(U^{\mathsf T}RU-\operatorname{tr}R)^2=2\|R\|_F^2\):
each squared coordinate has variance two and different coordinates
are independent. Since
\(\|\mathcal L_H f\|_\infty\leq w_{ab}(H)\), Cauchy–Schwarz in
(20) gives

\[
\left|\frac{d^2}{dt^2}G_f(Q_t)\right|
\leq\frac{w_{ab}(H)\|H\|_F}
 {\sqrt2(1-t)\lambda}.
\tag{21}
\]

Taylor's integral remainder at an endpoint \(r<1\) is bounded by the
right-hand constant times
\(\int_0^r(r-t)/(1-t)\,dt\leq1\). Letting \(r\uparrow1\) yields

\[
|G_f(Q+H)-G_f(Q)-DG_f(Q)[H]|
\leq\frac{w_{ab}(H)\|H\|_F}{\sqrt2\lambda}.
\tag{22}
\]

No inverse at the potentially singular endpoint appears. For the
original \(C^{1,1}\) activation, the function values converge
uniformly under mollification. At the strictly positive definite
reference \(Q\), the derivative also converges, as follows directly
by differentiating the Gaussian density: its derivative is an
integrable quadratic polynomial times that density. Hence (22)
passes to the limit with exactly the same constants. This argument
avoids assigning pointwise values to a merely almost-everywhere second
activation derivative at singular Gaussian laws.

Finally, let the entries of the random two-dimensional direction
\(H\) have second moments at most \(v\). Then

\[
\|w_{ab}(H)\|_{L^2}\leq Av^{1/2},\qquad
\mathbb E\|H\|_F^2
=\mathbb E(H_{aa}^2+2H_{ab}^2+H_{bb}^2)\leq4v.
\]

Taking expectations in (22) gives a remainder of at most
\(\sqrt2 Av/\lambda\). For the scalar diagonal problem the same
calculation gives \(Av/(\sqrt2\lambda)\). The first derivative at
\(Q\) still obeys (13), by the same mollification limit. Substitute
these bounds into (17) to obtain (19), completing the variant.

The nondegeneracy constants in (19) are genuine assumptions. No claim
is made here that arbitrary bounded \(C^{1,1}\) activations satisfy a
uniform quadratic covariance remainder at every singular reference
matrix. Conversely, the \(C_b^4\) theorem needs no such assumption and
allows all the dense and finite-sample Grams to be singular.
