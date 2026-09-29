# Initial Gaussian feature Gram for general activations

28 September 2026. Scoped continuation of the activation extension in this
study. This is an internally checked initialization result, not a promoted
training theorem. Inputs were `docs/notation.qmd`, the setting in
`paper/main.tex`, and the initial-Gram argument in `LOSS_DECAY_SYNTHESIS.md`.
No other study or training experiment was used.

## Result and conventions

Fix the sample count \(m\ge1\), input dimension \(d\ge1\), hidden depth
\(L\ge1\), and inputs \(v_a=x_a/\sqrt d\in\mathbb R^d\). The initialization
has independent first-layer entries \(N(0,1)\), independent hidden entries
\(N(0,1/n)\), and independence between layers. The readout initialization is
irrelevant to the present result. There are no biases. Write the fixed
layer-dependent activations as \(\phi^{(1)},\ldots,\phi^{(L)}\).

Assume each activation is globally Lipschitz and nonconstant. Either of the
following data/activation conditions suffices:

1. The inputs are nonzero and pairwise nonproportional, and
   \(\phi^{(1)}\) is nonpolynomial. There is no restriction \(m\le d\).
2. The inputs are linearly independent. Here \(m\le d\), and the first
   activation may be any nonconstant globally Lipschitz function, including
   a nonconstant affine function.

For \(m=1\), a nonzero input and any nonconstant globally Lipschitz first
activation suffice. For \(m>1\), the first condition implicitly requires
\(d\ge2\). All conditions concern fixed inputs and fixed activations as
width grows.

Define the deterministic initial feature second-moment matrices by

\[
 Q^{(1)}_{ab}
 =\mathbb E_{g\sim N(0,I_d)}
 [\phi^{(1)}(g^\top v_a)\phi^{(1)}(g^\top v_b)],
 \qquad
 Q^{(\ell)}_{ab}
 =\mathbb E_{Z\sim N(0,Q^{(\ell-1)})}
 [\phi^{(\ell)}(Z_a)\phi^{(\ell)}(Z_b)],\quad \ell\ge2.
 \tag{1}
\]

These are **uncentered** second moments, as required by the feature Gram;
centering would change the affine and nonzero-mean cases. Then every
\(Q^{(\ell)}\) is strictly positive definite. If \(H_{\ell,n}\) is the
\(n\times m\) matrix of initialized features, then

\[
 Q_n^{(\ell)}:=\frac{H_{\ell,n}^\top H_{\ell,n}}n
 \longrightarrow Q^{(\ell)}
 \quad\text{in probability in operator norm}.
 \tag{2}
\]

Consequently, in the manuscript's normalization,

\[
 \Gamma_{w,n}(0)=\frac{Q_n^{(L)}}m,\qquad
 \lambda_*:=\lambda_{\min}(Q^{(L)}/m)>0,
 \qquad
 \mathbb P\!\left\{
   \lambda_{\min}(\Gamma_{w,n}(0))\ge\lambda_*/2
 \right\}\longrightarrow1.
 \tag{3}
\]

The constant is independent of width and closure order. It may depend on
the data, depth, and every activation. This is not a uniform lower bound
over all separated data sets or all nonpolynomial activations: those
families can approach degeneracy. Nothing here bounds the Gram during
training or proves training-flow regularity.

The proof first separates continuous ridge functions by finite differences,
then propagates positivity using full Gaussian support, and finally proves
the empirical covariance recursion with fourth moments. Analyticity and
bounded activations are unnecessary.

## 1. Continuous nonpolynomial ridge functions are independent

We prove a slightly stronger finite-family statement. Suppose \(m\ge2\),
the vectors \(v_1,\ldots,v_m\) are nonzero and pairwise nonproportional,
and a continuous function \(\psi:\mathbb R\to\mathbb R\) is not a
polynomial of degree at most \(m-2\). Then the functions

\[
 g\longmapsto\psi(v_a^\top g),\qquad a=1,\ldots,m,
 \tag{4}
\]

are linearly independent as functions on \(\mathbb R^d\).

Suppose instead that

\[
 \sum_{j=1}^m c_j\psi(v_j^\top g)=0
 \quad\text{for every }g\in\mathbb R^d,
 \tag{5}
\]

and fix an \(a\) with \(c_a\ne0\). For every \(b\ne a\), set

\[
 u_b=v_a-\frac{v_a^\top v_b}{\|v_b\|_2^2}v_b.
 \tag{6}
\]

Nonproportionality gives \(u_b\ne0\), while
\(v_b^\top u_b=0\) and \(v_a^\top u_b=\|u_b\|_2^2>0\).
For a function \(F\) on \(\mathbb R^d\), define the difference operator
\(\Delta_hF(g)=F(g+h)-F(g)\). Translation operators commute, so their
differences commute. Apply \(\prod_{b\ne a}\Delta_{t_bu_b}\) to (5).
Every summand with index \(j\ne a\) vanishes because the factor with
\(b=j\) shifts perpendicular to \(v_j\). Thus, with \(k=m-1\),

\[
 \Delta_{s_1}\cdots\Delta_{s_k}\psi(t)=0
 \quad\text{for every }t,s_1,\ldots,s_k\in\mathbb R.
 \tag{7}
\]

Here each scalar \(s_b=t_bv_a^\top u_b\) can be chosen arbitrarily, and
\(t=v_a^\top g\) can be chosen arbitrarily because \(v_a\ne0\).

For completeness, (7) forces a continuous \(\psi\) to be a polynomial
of degree at most \(k-1\). Choose a smooth, nonnegative, compactly
supported function \(\eta\) of integral one, set
\(\eta_\epsilon(t)=\epsilon^{-1}\eta(t/\epsilon)\), and let
\(\psi_\epsilon=\psi*\eta_\epsilon\). The convolution is well-defined
even without growth bounds because the kernel has compact support.
Differences commute with this convolution, so (7) holds for the smooth
function \(\psi_\epsilon\). Differentiating once in each \(s_j\) at
\(s_1=\cdots=s_k=0\) gives
\(\psi_\epsilon^{(k)}(t)=0\). Repeated integration makes
\(\psi_\epsilon\) a polynomial of degree at most \(k-1\).

Continuity implies \(\psi_\epsilon\to\psi\) uniformly on every compact
interval. Fix \(k\) distinct real interpolation points. The coefficients
of a polynomial of degree at most \(k-1\) are a fixed linear function of
its values at these points, because the corresponding Vandermonde matrix
is invertible. The coefficients of \(\psi_\epsilon\) therefore converge
to coefficients of one polynomial \(p\) of degree at most \(k-1\).
At every real \(t\), both coefficient convergence and local uniform
convergence apply, giving \(p(t)=\psi(t)\). This contradicts the hypothesis
on \(\psi\), proving independence.

Apply the result with \(\psi=\phi^{(1)}\). A null quadratic form of the
first matrix in (1) is

\[
 c^\top Q^{(1)}c
 =\mathbb E\left|
      \sum_a c_a\phi^{(1)}(g^\top v_a)
   \right|^2=0.
 \tag{8}
\]

The expression inside the absolute value vanishes Gaussian-almost
everywhere. It is continuous, and every nonempty open ball has positive
standard Gaussian measure. If it were nonzero anywhere, continuity would
make it bounded away from zero on such a ball, contradicting (8).
It therefore vanishes everywhere. Ridge-function independence gives
\(c=0\), so \(Q^{(1)}\succ0\).

For \(m=1\), \(g^\top v_1\) is a nondegenerate scalar Gaussian. A
continuous nonconstant \(\phi^{(1)}\) is not identically zero and is
nonzero on some open interval. That interval has positive Gaussian
probability, giving \(Q^{(1)}_{11}>0\) directly.

This argument includes continuous nonanalytic and nonsmooth activations.
It avoids the invalid inference that a smooth nonpolynomial function must
have infinitely many nonzero derivatives at the origin; a smooth function
can be flat there without vanishing elsewhere.

## 2. Full Gaussian support propagates positivity

Let \(Q\succ0\) be an \(m\times m\) matrix, and let \(\psi\) be continuous,
nonconstant, and square-integrable for each scalar Gaussian marginal of
\(Z\sim N(0,Q)\). Define
\(T_\psi(Q)_{ab}=\mathbb E[\psi(Z_a)\psi(Z_b)]\).
Then \(T_\psi(Q)\succ0\).

A zero quadratic form would give
\(\sum_a c_a\psi(z_a)=0\) for every \(z\in\mathbb R^m\), by continuity
and the full support of a Gaussian with positive definite covariance.
Choose \(s,t\in\mathbb R\) with \(\psi(s)\ne\psi(t)\). Compare two
vectors that agree in all coordinates except coordinate \(a\), whose values
are \(s\) and \(t\). Subtraction gives

\[
 c_a[\psi(s)-\psi(t)]=0.
 \tag{9}
\]

Thus \(c_a=0\) for every \(a\). No condition \(\psi(0)=0\) is needed;
in particular sigmoid, cosine, and softplus are covered. Induction proves
positivity of every later matrix in (1).

If the inputs are linearly independent, their Gram
\(G_{ab}=v_a^\top v_b\) is positive definite. The first preactivation
vector is already \(N(0,G)\), so the same argument starts at layer one.
This proves the alternative that permits any nonconstant globally
Lipschitz first activation, including linear and affine functions.

## 3. Finite-width convergence for unbounded Lipschitz activations

For a particular layer write \(A=|\psi(0)|\) and choose a finite global
Lipschitz constant \(B\). Then

\[
 |\psi(t)|\le A+B|t|,\qquad
 \mathbb E|\psi(Z_a)|^4
 \le8A^4+24B^4Q_{aa}^2
 \quad (Z\sim N(0,Q)),
 \tag{10}
\]

using \((u+v)^4\le8(u^4+v^4)\) and the scalar Gaussian fourth moment
\(\mathbb EZ_a^4=3Q_{aa}^2\). Cauchy--Schwarz bounds
\(\mathbb E|\psi(Z_a)\psi(Z_b)|^2\) by the square root of the two fourth
moments. In particular all covariance entries in (1) are finite.

The map \(Q\mapsto T_\psi(Q)\) is continuous on the cone of positive
semidefinite matrices, including singular matrices. To verify this, let
\(Q_j\to Q\) and couple \(Z_j=Q_j^{1/2}U\), \(Z=Q^{1/2}U\), using one
\(U\sim N(0,I_m)\). The square roots converge in operator norm: they form
a bounded sequence, and any convergent subsequence has a positive
semidefinite limit whose square is \(Q\); uniqueness of the positive
semidefinite square root forces that limit to be \(Q^{1/2}\).
Thus \(Z_j\to Z\) pointwise in \(U\). Their activation products are
bounded by a constant times \(1+\|U\|_2^2\), uniformly in \(j\), by the
boundedness of \(\|Q_j^{1/2}\|_{\rm op}\) and the linear growth bound.
This integrable majorant justifies dominated convergence entry by entry.

At layer one the feature rows are independent and identically distributed.
For each pair \(a,b\), the summands in \((Q_n^{(1)})_{ab}\) have finite
variance by (10), so Chebyshev's inequality gives convergence to
\(Q^{(1)}_{ab}\) in probability. There are finitely many entries, and
\(\|M\|_{\rm op}\le m\max_{a,b}|M_{ab}|\), giving (2) for the first
layer.

For \(\ell\ge2\), condition on all previous layers. Independence of the
new Gaussian matrix makes its \(n\) preactivation rows independent
\(N(0,Q_n^{(\ell-1)})\) vectors. Conditional empirical means therefore
have mean \(T_{\phi^{(\ell)}}(Q_n^{(\ell-1)})\). On the event
\(\|Q_n^{(\ell-1)}\|_{\rm op}\le M\), (10) bounds each conditional
variance of an empirical entry by

\[
 \frac{C_\ell(M)}n,
 \qquad C_\ell(M)=8|\phi^{(\ell)}(0)|^4+24B_\ell^4M^2.
 \tag{11}
\]

Conditional Chebyshev and a union bound consequently yield, for any
\(\epsilon>0\),

\[
 \begin{aligned}
 &\mathbb P\!\left\{
 \max_{a,b}\left|
 (Q_n^{(\ell)}-T_{\phi^{(\ell)}}(Q_n^{(\ell-1)}))_{ab}
 \right|>\epsilon\right\}\\
 &\qquad\le
 \mathbb P\{\|Q_n^{(\ell-1)}\|_{\rm op}>M\}
 +\frac{m^2C_\ell(M)}{n\epsilon^2}.
 \end{aligned}
 \tag{12}
\]

By induction \(Q_n^{(\ell-1)}\to Q^{(\ell-1)}\) in probability.
Choose any fixed \(M>\|Q^{(\ell-1)}\|_{\rm op}\). Both terms on the
right of (12) tend to zero. Continuity of \(T_{\phi^{(\ell)}}\) then
proves (2) at layer \(\ell\). The induction uses fixed finite depth.

Finally the minimum-eigenvalue inequality

\[
 |\lambda_{\min}(A)-\lambda_{\min}(B)|
 \le\|A-B\|_{\rm op}
 \tag{13}
\]

for symmetric matrices follows by taking the infimum over unit vectors of
their quadratic forms. Apply it to \(Q_n^{(L)}/m\) and \(Q^{(L)}/m\) to
obtain (3). Neither training-time neuron independence nor a trained
population limit enters this argument.

## 4. Eligibility of the named activations

All definitions below are scalar functions on the entire real line. Put
\(s(t)=(1+e^{-t})^{-1}\), \(p(t)=(2\pi)^{-1/2}e^{-t^2/2}\), and
\(\Phi(t)=\int_{-\infty}^t p(u)\,du\). The derivative formulas also verify
the required growth and regularity directly.

| Activation | Formula or derivative check | Eligibility |
| --- | --- | --- |
| tanh | \(\psi'=1-\tanh^2t\), \(0<\psi'\le1\). | Smooth, globally Lipschitz, bounded nonconstant; nonpolynomial. |
| sigmoid | \(\psi=s\), \(\psi'=s(1-s)\le1/4\). | Smooth, globally Lipschitz, bounded nonconstant; nonpolynomial. |
| arctan | \(\psi'=(1+t^2)^{-1}\le1\). | Smooth, globally Lipschitz, bounded nonconstant; nonpolynomial. |
| sine and cosine | \(\psi' =\cos t\) or \(-\sin t\), respectively. | Smooth, globally Lipschitz, bounded nonconstant; nonpolynomial. |
| erf | \(\psi(t)=\frac2{\sqrt\pi}\int_0^t e^{-u^2}\,du\), \(\psi'=\frac2{\sqrt\pi}e^{-t^2}\). | Smooth, globally Lipschitz, bounded nonconstant; nonpolynomial. |
| softplus | \(\psi(t)=\log(1+e^t)\), \(\psi'=s\), \(\psi''=s(1-s)>0\). | Smooth, globally Lipschitz, unbounded and nonaffine; nonpolynomial. |
| exact GELU | \(\psi(t)=t\Phi(t)\), \(\psi'=\Phi+tp\), \(\psi''=(2-t^2)p\). | Smooth and nonaffine; \(\lvert\psi'\rvert\le1+(2\pi e)^{-1/2}\); nonpolynomial. |
| SiLU / swish with unit scale | \(\psi(t)=ts(t)\), \(\psi'=s+ts(1-s)\), \(\psi''=2s(1-s)+ts(1-s)(1-2s)\). | Smooth and nonaffine; \(\lvert\psi'\rvert\le1+e^{-1}\); nonpolynomial. |
| ELU with parameter one | \(\psi(t)=t\) for \(t\ge0\), \(e^t-1\) for \(t<0\). Its derivative is \(1\) for \(t\ge0\), \(e^t\) for \(t<0\). | Nonaffine, globally 1-Lipschitz and \(C^{1,1}\); nonpolynomial, but not \(C^2\). |
| Nonconstant affine | \(\psi(t)=at+b\), \(a\ne0\). | Smooth and globally Lipschitz. Eligible in later layers; first-layer positivity needs an extra rank condition, for example linearly independent inputs. |
| ReLU | \(\psi(t)=\max(t,0)\). | Continuous, globally 1-Lipschitz and nonpolynomial: the initialization theorem applies. It is not \(C^1\), so this does not put it inside a \(C^{1,1}_{\rm loc}\) training theorem. |

A bounded nonconstant polynomial on the real line is impossible, proving
nonpolynomiality in the bounded rows. A globally Lipschitz polynomial has
degree at most one, so nonaffinity proves nonpolynomiality for the
unbounded rows. Softplus has positive second derivative; GELU has
\(\psi''(0)=2p(0)>0\); SiLU has \(\psi''(0)=1/2\); and ELU and ReLU
have different behavior on the two half-lines.

For the displayed GELU slope bound,
\(\sup_t|t|p(t)=(2\pi e)^{-1/2}\). For SiLU, the identity
\(s(-t)=1-s(t)\) gives \(s(t)(1-s(t))\le e^{-|t|}\), and
\(\sup_{u\ge0}ue^{-u}=e^{-1}\). Each smooth row is automatically
\(C^{1,1}_{\rm loc}\), since its continuous second derivative is bounded
on compact intervals. ELU's derivative is continuous at zero and
globally 1-Lipschitz: on the negative half-line this follows from
\(0<e^t\le1\), on the positive half-line it is constant, and across zero
the estimates add. Thus ELU satisfies the same local regularity without
having a continuous second derivative. These are properties of the exact
formulas shown; approximations carrying the same activation name require
their own formula check.

Under the nonproportional-data assumption, every nonaffine row above can
be used as the first activation and every nonconstant globally Lipschitz
row can be used later. Activation choices can differ between layers.
Only ReLU lacks the smoothness required by the proposed training theorem.

## 5. Rank and geometry limitations

**Polynomial and affine first activations.** If
\(\psi(t)=\sum_{k=0}^p a_kt^k\), each ridge function is a polynomial in
\(g\in\mathbb R^d\). The dimension of its possible coefficient space
gives

\[
 \operatorname{rank}Q^{(1)}
 \le\sum_{k:a_k\ne0}\binom{d+k-1}{k}
 \le\binom{d+p}{p}.
 \tag{14}
\]

Indeed homogeneous polynomials of degree \(k\) have one coordinate for
each degree-\(k\) monomial, and the feature Gram is the Gram of the
corresponding ridge functions in Gaussian \(L^2\). The first bound can
be smaller still for particular data. The finite-difference lemma shows
that a polynomial of degree at least \(m-1\) nevertheless suffices for
independence of \(m\) nonproportional ridges; global Lipschitzness is then
unavailable if the degree exceeds one.

For an affine first activation \(\psi(t)=at+b\),

\[
 Q^{(1)}=a^2G+b^2\mathbf1\mathbf1^\top,
 \qquad
 c^\top Q^{(1)}c
 =a^2\left\|\sum_jc_jv_j\right\|_2^2
  +b^2\left(\sum_jc_j\right)^2.
 \tag{15}
\]

For \(a\ne0,b\ne0\), positivity is equivalent to the augmented vectors
\((v_j,1)\in\mathbb R^{d+1}\) being linearly independent. For
\(a\ne0,b=0\), it is equivalent to linear independence of the inputs.
For \(a=0\) the rank is at most one. Thus pairwise nonproportional inputs
alone do not justify the first-layer claim for a linear activation:
take more than \(d\) such inputs. If every activation is linear through
the origin, that rank defect persists at the top layer at every width.
A later nonlinearity may repair a singular first covariance; our
sufficient conditions do not classify those additional cases.

**Proportional and antipodal samples.** Duplicate inputs force identical
feature columns through every layer. For an odd first activation and
\(v_b=-v_a\), the first feature columns are negatives, so \(Q^{(1)}\)
is singular; if all later activations are odd, the defect persists at the
top. For an even first activation, that antipodal pair has equal first
features and remains indistinguishable in every later layer. For sigmoid,
\(s(t)+s(-t)=1\), so two antipodal pairs already give a linear dependence
among their four first-layer feature columns. ReLU additionally satisfies
\(\psi(ct)=c\psi(t)\) for \(c>0\), which makes positively proportional
inputs dependent at the first layer.

These are reasons for the explicit nonproportionality hypothesis, not a
claim that every proportional data set fails for every activation.
Sufficiency for one nonpolynomial activation must not be upgraded to an
activation-independent characterization of allowable data.
