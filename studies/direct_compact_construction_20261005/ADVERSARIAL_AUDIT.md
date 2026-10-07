# Independent adversarial audit of the symmetry route

Date: 2026-10-05.

Frozen primary input: `SYMMETRY_ROUTE.md`, SHA-256
`87fe86793402a03f2f64ee892f6bb83c7e8f8c8bb87ae934962af5488b14ef87`.
No experiment was run.  This report audits the assigned route against the
maintained notation and Section B.1, and against only the five authorized
source notes.  It does not use either of the other route reports in this
study.  The configured `explain-with-canonical-notation` skill was not
readable in this review environment; the notation was therefore checked
directly against `docs/notation.qmd`.

## Bottom line

The main positive result in the route is sound, with its stated population
scope.  For fixed $m,d$, orthonormal normalized inputs, two tanh hidden
layers, zero population readout, and sufficiently small
$Y=\lVert y\rVert_2/\sqrt m$, the directly computable frozen-feature model
does satisfy

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f(t,v)-\bar f(t,v)|\le C Y^3,
\]

and both population predictors have sphere-uniform endpoints.  The signs,
the factor $2/m$, the exact tangent-kernel formula, the composed Gaussian
kernel in the compact model, the stopping argument, and the endpoint passage
all check.

This theorem does **not** solve the requested root-width problem.  Its error
bound has no width decay for fixed labels, and Section B.1 supplies neither a
quantitative $n^{-1/2}$ finite-width-to-population estimate nor an all-time,
whole-sphere finite-width passage.  The authorized compression notes that do
have root-width comparisons construct their sources from the realized
width-$n$ initialization.  They therefore do not meet the stricter
dataset-plus-law-plus-$n$ provenance contract.

There is nevertheless a precise conditional finite-width corollary.  The
same perturbative argument applies to a finite network relative to its own
frozen initialization.  A strict
\(C_\eta(Y/\sqrt n+Y^3)\) comparison to the direct model would then follow
from one two-level, whole-sphere \(n^{-1/2}\) concentration lemma for the
initialized top-feature Gram and passive cross-kernel.  None of the current
inputs proves that empirical-process lemma.  If it were proved, the result
would have root-width scale for \(Y=O(n^{-1/6})\), but it would still not
solve the fixed-label target.

Two claims in the route need narrowing.

1. The estimate $O(Y^3)$ is an upper bound.  It does not prove that the
   population-surrogate difference has a nonzero cubic coefficient, or even
   that it is nonzero for every nonzero label vector.  Thus “cubic leading
   error,” “nonvanishing bias,” and “eventually larger than $n^{-1/2}$” are
   not established as statements about the actual error.  The safe statement
   is that the proved estimate does not certify any width-decaying accuracy at
   fixed $Y$.
2. Equations (26)--(29) prove that direct differentiation generates additional
   response-feature moments and leaves every formal fixed polynomial-degree
   moment algebra.  Appearance of these moments alone is not a proof that no
   function of the listed Grams closes on the reached trajectory.  Such a
   no-closure theorem would require, for example, two admissible reached
   states with the same proposed statistics and different derivatives, or an
   equivalent separation argument.  The route correctly does not claim a
   no-go theorem for all finite nonlinear encodings, but several categorical
   “is not closed” phrasings are stronger than the supplied proof.

Accordingly, the strongest overall verdict is:

| Claim | Verdict |
|---|---|
| Population equations, signs, and scaling | **Pass** |
| Exact kernel (3)--(4) | **Pass** |
| Signed symmetries and frozen input complement | **Pass**, with the orbit domain qualification below |
| All-time, whole-sphere $O(Y^3)$ theorem | **Pass** as an upper-bound theorem |
| Existence and sphere-uniform endpoint | **Pass** |
| Nonzero cubic leading term for every nonzero label | **Not proved** |
| Second-derivative witness against samplewise direct-product dynamics | **Pass** |
| Formal fixed-degree moment algebra is invariant | **Falsified by (29)** |
| No closure of the listed Grams on the reached set | **Not proved**; a hierarchy obstruction is proved |
| No finite nonlinear encoding can work | **Not claimed and not proved** |
| \(C(Y/\sqrt n+Y^3)\) finite-flow comparison | **Conditional on the missing initialized empirical-process lemma (A12)** |
| Direct strict-$C/\sqrt n$ finite-width construction | **Open; not supplied by this route** |

## 1. Exact contract being audited

Write $v_a=x_a/\sqrt d$, so $v_a^\top v_b=\delta_{ab}$, and let
$v\in S^{d-1}$ be a passive query.  The loss is
$m^{-1}\sum_a r_a^2$, with $r_a=f_a-y_a$, and the three canonical
block mobilities are used.  In the sum-loss notation of maintained Section
B.1, setting all three block constants to $1/m$ gives

\[
                         \alpha=\frac2m.
\]

The route's population state is the first-row field $A$, the common
forward/adjoint action $W$, and the readout $w$.  Its direct surrogate is
the $m$-scalar residual state $\bar r$ in (9), together with the fixed
observation map (10).  This surrogate is deterministic from the data and the
Gaussian initialization law; it does not use a realized finite network.

The stronger target is different.  If $F_n$ denotes a realized width-$n$
dense predictor and $C_n$ a direct compact construction, define

\[
 \lVert g\rVert_\star
 :=\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}|g(t,v)|,
\]

where $t=\infty$ denotes the fitted endpoint.  The requested theorem needs
a probability mode, for example

\[
 \mathbb P\!\left(\lVert F_n-C_n\rVert_\star
              \le C_\eta n^{-1/2}\right)\ge1-\eta,
\]

for every sufficiently large $n$, with all retained coefficients and the
initial compact state computable from the dataset, the initialization law,
and $n$, but not from the realized arrays or trajectory of $F_n$.  If the
intended $C$ is independent of a confidence level, that stronger probability
quantifier must be stated.  Neither Section B.1 nor the symmetry route fixes
this missing finite-width probability contract.

The symmetry theorem itself is a population gradient-flow theorem.  If the
finite reference in the stronger target is raw GD rather than finite
gradient flow, the theorem must additionally specify the step sequence,
interpolation convention, and joint width/step limit.  Section B.1's
$\eta_n\sqrt n\to0$ bridge is again only on each fixed compact horizon.

## 2. Population flow and tangent kernel

The route's equations (1)--(2) agree with maintained Section B.1.  In
particular, with the mean loss,

\[
\begin{aligned}
 \dot A&=-\alpha\sum_a r_a\Delta_a^{(1)}v_a^\top,\\
 \dot W&=-\alpha\sum_a r_a\Delta_a^{(2)}\otimes H_a^{(1)},\\
 \dot w&=-\alpha\sum_a r_aH_a^{(2)}.
\end{aligned}
\]

Differentiating $f_a=\mathbb E_2[wH_a^{(2)}]$ gives

\[
                         \dot r=-\alpha\mathcal K r,
\]

with

\[
\begin{aligned}
 \mathcal K_{ab}
 ={}&\mathbb E_2[H_a^{(2)}H_b^{(2)}]\\
 &+\mathbb E_1[H_a^{(1)}H_b^{(1)}]
       \mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}]\\
 &+\delta_{ab}\mathbb E_1[\Delta_a^{(1)}\Delta_b^{(1)}].
\end{aligned}
\]

There is no missing factor of $m$, no sign error, and no transpose/adjoint
error.  The Kronecker factor in the last line is exactly the orthonormal input
Gram.  Each summand is a parameter-gradient Gram, so
$\mathcal K\succeq0$.  The residual equation is not a closed residual ODE
unless the changing matrix $\mathcal K$ is also generated.

At initialization the first coordinates $X_a=A_0\cdot v_a$ are independent
standard Gaussians.  Since tanh is odd,

\[
 \mathbb E[\tanh X_a\tanh X_b]=\mu\delta_{ab},
 \qquad \mu=\mathbb E[\tanh^2G]>0.
\]

The common Gaussian action therefore makes the second preactivations jointly
Gaussian with covariance $\mu I_m$.  Their top-feature Gram is
$\nu I_m$, where

\[
 \nu=\mathbb E[\tanh^2U]>0,
 \qquad U\sim N(0,\mu).
\]

Because $w_0=0$, both backward blocks vanish initially.  Hence
$\mathcal K(0)=\nu I_m$, exactly as claimed.

For a passive query $v$, the initial first-feature covariance with sample
$a$ is $k_1(v^\top v_a)$.  Applying the same Gaussian action once more
gives the exact top-feature covariance

\[
              k_2\!\left(k_1(v^\top v_a)\right).
\]

Thus (8)--(10), including the exponent $e^{-2\nu t/m}$ and the factor
$1/\nu$, are correct.  At $v=v_b$, the off-diagonal values vanish by
oddness and independence and the diagonal value is $\nu$, so the model's
observation and residual states agree on the training set.

## 3. Reconstruction of the all-time \(O(Y^3)\) proof

The proof closes without an elapsed-time factor.  Let
$R(t)=\lVert r(t)\rVert_2$, and stop only if the top-feature Gram loses the
margin \((\nu/2)I_m\) or if
$\lVert W-W_0\rVert_{\mathrm{op}}=1$.  On the stopped interval,

\[
 \frac d{dt}R^2
 =-2\alpha r^\top\mathcal K r
 \le-\alpha\nu R^2.
\]

Since $R(0)=\sqrt mY$,

\[
 R(t)\le\sqrt mY e^{-\nu t/m},
 \qquad
 \int_0^\infty R(t)\,dt\le C Y.                 \tag{A1}
\]

Here and below $C$ may depend on the fixed $m,d,\nu^{-1}$ and the
initial action bound, but not on $t$ or $Y$.

The pointwise readout equation and $|H_a^{(2)}|\le1$ give

\[
 \sup_t\lVert w(t)\rVert_{L^\infty(\Omega_2)}\le CY.
\]

Consequently

\[
 \sup_{t,a}\lVert\Delta_a^{(2)}(t)\rVert_{L^2}\le CY,
 \qquad
 \sup_{t,a}\lVert\Delta_a^{(1)}(t)\rVert_{L^2}\le CY,  \tag{A2}
\]

because $0<\tanh'\le1$ and the stopped operator norm of $W$ is bounded.
The rank-one operator norm and (A1)--(A2) then yield

\[
 \sup_t\lVert W(t)-W_0\rVert_{\mathrm{op}}
 +\max_a\sup_t
 \lVert Z_a^{(1)}(t)-Z_a^{(1)}(0)\rVert_{L^2}
 \le CY^2.                                               \tag{A3}
\]

Let $P=\sum_av_av_a^\top$, write
$\xi_a=v_a^\top v$, and put $v_\perp=(I-P)v$.  Since
$A(t)(I-P)=A_0(I-P)$,

\[
 Z^{(1)}(t,v)-Z^{(1)}(0,v)
 =\sum_a\xi_a\bigl(Z_a^{(1)}(t)-Z_a^{(1)}(0)\bigr).
\]

As $\sum_a\xi_a^2\le1$, (A3) is uniform over the whole sphere.  The
one-Lipschitz property of tanh and the operator bound for $W_0$ therefore
give

\[
 \sup_{t,v}
 \lVert H^{(2)}(t,v)-H^{(2)}(0,v)\rVert_{L^2}\le CY^2.   \tag{A4}
\]

One implicit functional-analytic detail should be made explicit in the route:
the bounded initial action must act on the closure containing all passive
fields $H^{(1)}(t,v)$.  This follows from the Section B.1 construction by
including a countable dense set of sphere queries and extending with the
displayed $L^2$-Lipschitz dependence on $v$.  No uncountable independent
Gaussian family or Hilbert--Schmidt kernel is being assumed.

Equation (A4) moves each top-Gram entry by $O(Y^2)$.  Since $m$ is fixed,
the matrix operator perturbation is also $O(Y^2)$.  Choosing $Y\le c$
closes both stopping conditions by first exit on every finite interval.
Maintained Section B.1 supplies existence on every finite interval, so the
same estimates hold for all $t\ge0$.

The two backward kernel blocks are $O(Y^2)$ by (A2), while (A4) makes the
top block \(\nu I_m+O(Y^2)\).  Therefore

\[
             \sup_{t\ge0}\lVert\mathcal K(t)-\nu I_m\rVert_{\mathrm{op}}
             \le CY^2.                                  \tag{A5}
\]

For $e=r-\bar r$,

\[
 \dot e=-\alpha\nu e-\alpha(\mathcal K-\nu I_m)r,
 \qquad e(0)=0.
\]

Variation of constants, (A1), and (A5) give both

\[
 \sup_{t\ge0}\lVert e(t)\rVert_2
 +\int_0^\infty\lVert e(t)\rVert_2\,dt\le CY^3.         \tag{A6}
\]

Subtracting the frozen-feature readout equation then gives

\[
             \sup_t\lVert w(t)-\bar w(t)\rVert_{L^2}\le CY^3, \tag{A7}
\]

because the two sources are $eH^{(2)}(t)$ and
$\bar r[H^{(2)}(t)-H^{(2)}(0)]$.  Their time integrals are respectively
$O(Y^3)$ by (A6) and $O(Y)O(Y^2)$ by (A1) and (A4).  Finally,

\[
\begin{aligned}
 |f(t,v)-\bar f(t,v)|
 \le{}&\lVert w(t)-\bar w(t)\rVert_{L^2}
       \lVert H^{(2)}(t,v)\rVert_{L^2}\\
 &+\lVert\bar w(t)\rVert_{L^2}
       \lVert H^{(2)}(t,v)-H^{(2)}(0,v)\rVert_{L^2}
 \le CY^3.
\end{aligned}
\]

This proves the claimed all-time and whole-sphere **upper bound**.

The velocities of $w$, $W$, and every training
$Z_a^{(1)}$ are norm-integrable by (A1)--(A2).  Hence those fields converge.
The frozen-complement identity makes first-layer convergence uniform over
the sphere, and the operator convergence of $W$ then does the same at the
second layer.  The readout pairing therefore converges uniformly in $v$.
Also $R(t)\to0$ exponentially.  The fitting and endpoint assertions, and
the passage of the preceding estimate to $t=\infty$, are valid.

### Necessary wording correction

Neither (A5)--(A7) nor label-reversal parity proves a nonzero cubic
coefficient.  Parity says that, if a label-amplitude expansion is available,
the hidden fields are even and the predictions are odd.  Together with the
linear frozen model and the proved bound, this makes cubic the first
*permitted* correction order.  It does not make cubic the proved leading
order.

For fixed $y$, both $f$ and $\bar f$ in this population theorem are
independent of $n$.  If their difference is nonzero, it cannot decay with
width; however, the route gives no lower bound proving such nonvanishing for
every nonzero $y$.  The conclusion needed here is only that
$CY^3\not\le C'n^{-1/2}$ uniformly at fixed $Y>0$ for all large $n$.
Thus the theorem's **guarantee** cannot establish the desired root-width
claim.  Calling the actual difference a proved nonvanishing bias is stronger
than the result.

## 4. Exact symmetry claims

The signed-data equivariance is correct.  A bias-free two-tanh network obeys
$f_\theta(-v)=-f_\theta(v)$ at every parameter state.  Replacing any pair
$(v_a,y_a)$ by $(\sigma_av_a,\sigma_ay_a)$ therefore leaves each squared
residual, and hence the entire loss as a parameter function, unchanged.
With the same initialization, uniqueness gives the same parameter path.
This changes a presentation of the dataset; it is not an independent-label
symmetry of one fixed oriented dataset.

Under global label reversal, the transformation

\[
 (A,W,w,r,\Delta^{(1)},\Delta^{(2)})
 \longmapsto
 (A,W,-w,-r,-\Delta^{(1)},-\Delta^{(2)})
\]

preserves all three flow equations.  Thus the hidden paths are even and the
readout and predictor odd under common label reversal.  Again, this does not
permit reversal of one label while keeping its input orientation fixed.

The frozen-complement identity (6)--(7) is exact.  At population level,
orthogonal transformations that fix every training vector preserve both the
dataset and the initialization law.  Uniqueness then makes the deterministic
population prediction constant on their query orbits.  On the unit sphere,
these orbits are indexed by

\[
 \xi=(v_1^\top v,\ldots,v_m^\top v)
 \quad\text{in}\quad
 \{\xi\in\mathbb R^m:\lVert\xi\rVert_2\le1\},
\]

with the boundary forced when the training vectors span all of
\(\mathbb R^d\).  Thus the route's \(\Psi_t(\xi)\) should be understood on
this feasible orbit domain, not on all of \(\mathbb R^m\).  Its oddness is
correct.  This is a population-law statement and gives no pathwise rotational
invariance for a realized finite network.

## 5. The false-decoupling witness

Equations (23)--(25a) are correct.  At initialization,

\[
 \dot w(0)=\alpha\sum_b y_bS_b,
 \qquad
 \dot\Delta_a^{(2)}(0)
   =\alpha D_a\sum_b y_bS_b,
 \qquad
 \dot W(0)=0.
\]

Differentiating once more gives

\[
 \ddot W(0)
 =\alpha^2\sum_{a,b}y_ay_b(D_aS_b)\otimes H_a
\]

and

\[
 \ddot Z_a^{(1)}(0)
 =\alpha^2y_a\operatorname{sech}^2(X_a)
   W_0^*\!\left[D_a\sum_b y_bS_b\right].
\]

For $b\ne a$, adjunction and independence give

\[
 \mathbb E_1[H_bW_0^*(D_aS_b)]
 =\mathbb E_2[U_bD_aS_b]
 =\mathbb E[D_a]\,\mathbb E[U_b\tanh U_b]>0.
\]

Hence the coefficient field multiplying $y_ay_b$ is nonzero.  Multiplication
by \(\operatorname{sech}^2(X_a)>0\) almost surely cannot annihilate it.  This
is a decisive counterexample to a direct-product decomposition in which the
sample-$a$ hidden coordinate evolves independently of the other labels.

The middle kernel block also has

\[
 \mathcal K_{aa}^{(2)}(t)
 =\mu\alpha^2t^2
 \mathbb E_2\!\left[D_a^2\left(\sum_b y_bS_b\right)^2\right]
 +o(t^2),
\]

and the coefficient of $y_b^2t^2$, $b\ne a$, is
$\mu\alpha^2\mathbb E[D_a^2]\nu>0$.  Thus diagonalization of the initialized
kernel does not persist as samplewise independence.

This witness does **not** rule out a coupled compact state with $m$ or more
coordinates.  It rules out the claimed independent one-sample factorization,
which is exactly the safe conclusion stated at the end of Section 4.

## 6. Moment hierarchy and action feedback

The differentiated identities (26)--(28) are exact.  In particular, the
derivative of a same-layer feature Gram requires mixed response-feature
moments, and the derivative of the second-layer Gram requires both new mixed
moments and a new action of $W$.  The four displayed Gram families therefore
do not produce a closed ODE by direct differentiation.

For tanh,

\[
 \frac d{dt}\mathbb E_1[(H_a^{(1)})^p]
 =-\alpha p r_a\left{
   \mathbb E_1[(H_a^{(1)})^{p-1}\Delta_a^{(1)}]
  -\mathbb E_1[(H_a^{(1)})^{p+1}\Delta_a^{(1)}]
 \right}.
\]

Because tanh takes every value in an interval, no pointwise polynomial
identity reduces the last power to finitely many lower powers.  Therefore the
formal algebra generated by mixed moments up to a fixed polynomial degree is
not invariant under the vector field.  This invalidates an **exact formal
degree cutoff**.

The stronger conclusion that the lower moments cannot determine the higher
moment on the particular reached family is not established by degree raising
alone.  Nor does (29) exclude an approximate truncation with a proved tail,
or a finite nonpolynomial sufficient statistic.  The strongest safe wording
is:

> Direct differentiation of the proposed Gram/moment state generates an
> unbounded hierarchy; no exact closure formula for that state has been
> supplied.

The integral identities

\[
 W(t)=W_0-\alpha\sum_a\int_0^t
 r_a(s)\Delta_a^{(2)}(s)\otimes H_a^{(1)}(s)\,ds
\]

and (31)--(32) are also exact.  They expose the actual causal burden: passive
prediction needs current actions of $W_0$, its adjoint in reverse dynamics,
and adaptive two-time feature correlations.  A direct compact model must
generate sufficient approximations to these quantities from its own state.
Supplying them from the target trajectory would be an oracle.

The sentence that Gaussian conditioning always turns each new adaptive action
into old-history regression plus a fresh independent Gaussian innovation is
not proved in this route.  For an input selected adaptively from the same
Gaussian action, ordinary fixed-vector Gaussian regression is insufficient;
one needs a cavity/conditioning theorem with its measurability and independence
hypotheses checked.  Likewise, the assertion that later nonlinear queries
“generally enlarge” the history Gram is a useful mechanism description, not a
theorem here.  Neither statement is needed for the valid identities or for
Theorem 1.

## 7. Why the broader root-width target remains open

### 7.1 Dense-versus-dense variability is not dense-to-population bias

Let $F_n,F_n'$ be independent, identically distributed dense predictors and
let $F_\infty$ be the population predictor.  Formally decomposing around the
finite-width mean gives

\[
 F_n-F_n'
 =(F_n-\mathbb EF_n)-(F_n'-\mathbb EF_n),
\]

whereas

\[
 F_n-F_\infty
 =(F_n-\mathbb EF_n)+(\mathbb EF_n-F_\infty).
\]

The common finite-width bias cancels in the first difference.  Consequently,
a dense-versus-dense variability lower bound identifies an unavoidable
fluctuation scale, but does not bound the dense-to-population bias.  A
dense-versus-dense upper bound also does not by itself identify the population
center.  The integrated source note reports a transient prediction-variability
lower bound, not a fitted-endpoint theorem, and it cannot fill this bridge.

The $f-\bar f$ difference in Theorem 1 is a third object: it is a
population-to-surrogate truncation error.  Calling it “dense-to-population
bias” would conflate two logically independent terms.

### 7.2 The required error decomposition has two distinct terms

For the direct frozen-feature model,

\[
 \lVert F_n-\bar F\rVert_\star
 \le
 \lVert F_n-F_\infty\rVert_\star
 +\lVert F_\infty-\bar F\rVert_\star.                   \tag{A8}
\]

The second term is bounded by $CY^3$, not by $C/\sqrt n$ at fixed $Y$.
The first term has no quantitative estimate in the assigned maintained
theorem.  Section B.1 proves convergence in probability on each fixed finite
horizon, for stated pointwise measurements and finite measurement families.
It does not prove a rate, a whole-sphere supremum, a growing horizon, or an
endpoint comparison.

If $C_n$ itself uses fresh randomness independent of $F_n$, its own
fluctuation and bias terms must be added to (A8).  Independence does not couple
away either fluctuation; at best it changes the root-width constant once both
upper bounds have been proved.

### 7.3 Exact missing empirical-process lemma for the shrinking-label corollary

There is a sharper route to the proposed
\(C(Y/\sqrt n+Y^3)\) estimate than a quantitative comparison of the entire
adaptive finite and population action states.  Define the initialized finite
top features

\[
 S_{n,a}=h_{n,a}^{(2)}(0),
 \qquad S_n(v)=h_n^{(2)}(0,v),
\]

their normalized training Gram, and their passive cross-kernel by

\[
 (Q_n)_{ab}=\frac{S_{n,a}^{\top}S_{n,b}}n,
 \qquad
 (q_n(v))_a=\frac{S_{n,a}^{\top}S_n(v)}n.
\]

Let

\[
 q_a(v)=k_2\!\left(k_1(v^\top v_a)\right).
\]

On an event where \(Q_n\succeq(\nu/2)I_m\) and
\(\lVert W_{n,0}^{(2)}\rVert_{\mathrm{op}}\le M\), the proof in Section 3
transfers verbatim to normalized finite Euclidean norms.  In particular, if
\(\widetilde F_n\) is the finite network with both hidden layers frozen at
their own initialization, then

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |F_n(t,v)-\widetilde F_n(t,v)|\le CY^3.                 \tag{A9}
\]

The reason no trained empirical-process estimate is needed in (A9) is that
all feature-learning corrections are controlled deterministically by the
finite residual activity, the initialized Gram gap, and the initialized
matrix operator norm.  The frozen input-complement identity is exact at
finite width as well.

The finite frozen flow has the explicit formula

\[
 \widetilde F_n(t,v)
 =q_n(v)^\top\Phi_t(Q_n)y,
 \qquad
 \Phi_t(Q)=Q^{-1}(I-e^{-\alpha Qt}).
                                                               \tag{A10}
\]

The direct population model is

\[
 \bar F(t,v)=q(v)^\top\Phi_t(\nu I_m)y.
\]

For \(Q\succeq(\nu/2)I_m\), the integral representation

\[
 \Phi_t(Q)=\alpha\int_0^t e^{-\alpha Qs}\,ds
\]

and Duhamel's identity give, uniformly for \(t\in[0,\infty]\),

\[
 \lVert\Phi_t(Q)\rVert_{\mathrm{op}}\le\frac2\nu,
 \qquad
 \lVert\Phi_t(Q)-\Phi_t(\nu I_m)\rVert_{\mathrm{op}}
 \le C_\nu\lVert Q-\nu I_m\rVert_{\mathrm{op}}.          \tag{A11}
\]

Consequently the exact missing stochastic statement is the following
initialized, time-free empirical-process lemma: for every fixed confidence
\(\eta>0\),

\[
\begin{aligned}
 \mathbb P\Bigg(
 &\lVert Q_n-\nu I_m\rVert_{\mathrm{op}}
 +\sup_{v\in S^{d-1}}\lVert q_n(v)-q(v)\rVert_2
 \le \frac{C_\eta}{\sqrt n},\\
 &\lVert W_{n,0}^{(2)}\rVert_{\mathrm{op}}
 +\frac{\lVert A_{n,0}\rVert_{\mathrm{op}}}{\sqrt n}\le M_\eta
 \Bigg)\ge1-\eta.                                       \tag{A12}
\end{aligned}
\]

For fixed \(m,d\), (A11)--(A12) imply

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |\widetilde F_n(t,v)-\bar F(t,v)|
 \le C_\eta\frac{Y}{\sqrt n}.                            \tag{A13}
\]

Combining (A9) and (A13) would give the complete finite-gradient-flow
comparison

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |F_n(t,v)-\bar F(t,v)|
 \le C_\eta\left(\frac{Y}{\sqrt n}+Y^3\right),           \tag{A14}
\]

including the endpoint.  If \(Y=O(n^{-1/6})\), the second term is
\(O(n^{-1/2})\) and the first is \(O(n^{-2/3})\), so (A14) would indeed be
root-width.

The current inputs do **not** prove (A12).  Maintained Section B.1 supplies
only qualitative convergence for fixed finite value programs and fixed
finite collections of measurements, not a rate or a sphere supremum.  The
exact required proof has two empirical levels:

1. a uniform \(n^{-1/2}\) bound for the first-layer empirical covariance and
   variance functions indexed by \(v\in S^{d-1}\); and
2. conditional on the first layer, a uniform \(n^{-1/2}\) bound for the
   second-layer iid-row empirical process defining \(q_n(v)\), together with
   the finitely indexed training Gram \(Q_n\), followed by stability of the
   Gaussian tanh covariance under the first-layer covariance errors.

The same high-probability event must retain constant initialized operator
bounds for both hidden layers.  The authorized source constructions
approximate realization-dependent feature fields; they do not state this
law-centered uniform concentration lemma.  Thus (A14) is a precise
conditional corollary, not a theorem available from the current inputs.  This
gap is an initialized two-level empirical-process estimate, not an unspecified
need to control every adaptive trained field.

This finite-frozen decomposition bypasses the unknown bias between the full
finite trained flow and the full population trained flow; it does not
estimate that bias.  Dense-versus-dense variability results therefore neither
prove nor obstruct (A12).

### 7.4 Compact time cannot substitute for the missing lemma

The finite-to-finite perturbative estimate (A9) and the frozen semigroup
formula (A10) are already all-time statements, so the route through (A12)
would not require a growing-horizon population theorem.  It is important not
to replace (A12) by maintained Section B.1, however.  Choosing a horizon
$T_n\asymp\log n$ inside a theorem stated only for each fixed $T$ is an
unjustified interchange of $n\to\infty$ and $T\to\infty$.  Population fitting
does not by itself imply finite-width fitting or endpoint selection.  Thus,
without the initialized uniform rate (A12) and the finite perturbative
reduction above, the population endpoint in Theorem 1 cannot be combined with
B.1's compact-time qualitative limit to obtain (A14).

### 7.5 Initialization-only is not law-only

The authorized storage and spherical-source notes construct finite source
spaces, selected coordinates, metrics, and paired forward/adjoint actions from
the **realized** width-$n$ initialization of the reference dense network.
They then discard the full arrays and retain only polylogarithmically many
coordinates.  This meets a “no retained width-$n$ array” contract, but not
the present “dataset plus law plus $n$, no realized width-$n$ input”
contract.  The refined error-prefactor note changes the comparison estimate,
not that provenance.  The integrated README likewise states comparison to the
same realized initialization.

Those constructions therefore cannot be imported as the missing direct
bridge.  Conversely, the direct model (9)--(10) does meet the law-only and
causal-runtime requirements and has only $m$ moving scalars in addition to
the stored data, but its proved accuracy is on the label-amplitude axis.
The displayed bounded Gaussian integrals are genuine law-defined
coefficients, not response oracles.  Under the exact-real storage convention
they are directly specified.  If bit complexity or numerical quadrature is
part of “computable,” an error-controlled evaluation and precision count
would still have to be added; the route makes no such complexity claim.

### 7.6 The source-space obstruction is not a predictor no-go theorem

The orthogonal-tanh source note reports a lower bound for a fixed linear space
that approximates the full initialized first-layer feature field, and hence
for the particular construction that stores a full quadratic metric on such a
space.  It explicitly does not lower-bound arbitrary autonomous predictors or
prediction-only representations.  It cannot be used to rule out the direct
observable-only target.

## 8. Logical shortcuts that would falsely claim success

Any of the following inferences would be invalid.

1. **Upper bound to nonzero leading bias.**  From
   \(\lVert F_\infty-\bar F\rVert_\star\le CY^3\), infer that the actual
   difference is asymptotic to a nonzero cubic term.
2. **Shrinking-label substitution.**  Set $Y_n=O(n^{-1/6})$ and present the
   resulting $O(n^{-1/2})$ population bound as a fixed-label theorem.
3. **Qualitative-to-quantitative width passage.**  Combine B.1's
   fixed-$T$ convergence in probability with the population theorem and
   assert a strict $C/\sqrt n$ rate.
4. **Fixed-query-to-sphere substitution.**  Treat convergence for every fixed
   value program or every fixed query as the uniform \(n^{-1/2}\)
   initialized kernel estimate (A12), without a two-level empirical-process
   or chaining argument.
5. **Growing-horizon substitution.**  Insert $T_n\asymp\log n$ into a theorem
   whose constants and probability statement are only controlled for fixed
   $T$, then pass to the endpoint.
6. **Variability-to-bias substitution.**  Use a dense-versus-dense estimate to
   control \(\mathbb EF_n-F_\infty\), which cancels from that comparison.
7. **Seed-coupled-to-direct substitution.**  Call preprocessing from the
   realized dense initialization “direct” merely because the full arrays are
   discarded after preprocessing.
8. **Diagonal-kernel decoupling.**  Infer independent sample flows from
   \(\mathcal K(0)=\nu I_m\); equations (23)--(25a) explicitly refute it.
9. **Hierarchy-to-no-go substitution.**  Infer impossibility of every finite
   nonlinear encoding from the failure of the displayed Gram or polynomial
   moment cutoff.
10. **Prediction obstruction from feature obstruction.**  Apply the
   first-layer source-space lower bound to an arbitrary prediction-only
   autonomous model.
11. **Oracle closure.**  Evaluate the adaptive forward/adjoint contractions or
    two-time kernels from the target population/dense trajectory and count
    only the resulting scalar outputs as retained state.

## 9. Strongest safe conclusions

1. Orthogonality and odd tanh give exact signed-data equivariance, a frozen
   input complement, and a population query-orbit reduction to the feasible
   training-correlation ball.
2. The exact initialized passive kernel is
   $k_2(k_1(v^\top v_a))$, with all variances and the $2/m$ clock scaling as
   stated.
3. The $m$-scalar frozen-feature residual flow is direct, autonomous,
   restartable, and law-computable.  For sufficiently small fixed label norm
   it approximates the full **population** flow uniformly for all physical
   times, all sphere queries, and the endpoint with error at most $CY^3$.
4. The route proves no nonzero cubic lower term.  Its theorem is an
   approximation guarantee in label size, not a width theorem.
5. Orthogonal samples do not yield independent one-sample hidden dynamics:
   mixed label coefficients appear at second physical-time derivative in the
   shared middle action, first-layer coordinates, and a named kernel block.
6. The listed residual/feature/backward Grams and every formal fixed-degree
   polynomial moment cutoff generate additional observables under
   differentiation.  No exact finite closure for them is supplied; no general
   finite-encoding impossibility is established.
7. For finite gradient flow, the same perturbative proof gives the all-time
   finite-to-finite bound (A9).  The precise missing stochastic step for
   \(C_\eta(Y/\sqrt n+Y^3)\) is the initialized two-level whole-sphere
   empirical-process lemma (A12).  Proving it would give a root-width theorem
   in the shrinking-label regime \(Y=O(n^{-1/6})\).
8. At fixed nonzero label scale, even (A14) retains the \(CY^3\) term.  A
   successful direct fixed-label theorem still needs a law-only autonomous
   model that captures or uniformly truncates the causal feature-learning
   feedback, together with its all-time finite-width comparison.  Raw GD
   would additionally need an all-time discretization bridge.
9. None of the assigned sources supplies all of those bridges under the
   no-realized-width-$n$ provenance restriction.  The strict direct
   $C/\sqrt n$, all-time, whole-sphere, endpoint construction with polylog
   retained storage therefore remains open.
