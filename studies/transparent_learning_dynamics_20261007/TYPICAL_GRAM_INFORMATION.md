# Typical information missing from initialization Grams

This is a scoped, prompt-only theory audit. Scientific inputs are the supervisor's
specified one-layer flow and Gaussian initialization. No book passages, other
study artifacts, literature, experiments, or Git history were used. Required
research, rigorous-proof, and canonical-notation instructions were read, including
the neural-network notation reference. This file is an independently derived
candidate, frozen for comparison on completion; it is not promoted material or an
independent promotion review. The original comparison freeze had SHA256
`ad68a8a0ba9d8a67fe5f96b00f4233b213bcba0a9c5c521980e51f4d45af6b02`.
Subsequent changes remove a notation conflict and state fixed-label rescaling;
the trajectory extension is separately recorded in
`TYPICAL_GRAM_TRAJECTORY.md` and uses an idea supplied after this freeze.

The conclusion is specific: feature and derivative-feature Grams leave random
information of order \(n^{-1/2}\) in a fourth-order initialization moment and in
the third time derivative of prediction. This holds even for arbitrary measurable
estimators using those Grams. It does not show larger errors, failure of an
arbitrarily enriched finite summary, or a fixed-positive-time trajectory lower
bound.

## 1. Model and information available to a predictor

There are two unit orthogonal inputs \(v_1,v_2\in\mathbb R^d\), so
\(Q_{ab}=v_a^\top v_b=\delta_{ab}\). The width is \(n\). At initialization,
the rows of \(A_0\in\mathbb R^{n\times d}\) are independent standard Gaussian
vectors, \(z_a=A v_a\in\mathbb R^n\), and \(w_0=0\in\mathbb R^n\).
The activation is \(\phi(z)=\sin z\), applied componentwise. Predictions,
residuals, and loss are

\[
h_a=\sin z_a,\qquad
f_a=\frac1n w^\top h_a,\qquad
c_a=y_a-f_a,\qquad
\mathcal L=\frac1m\sum_{a=1}^m c_a^2,\quad m=2.
\]

The prescribed physical-time flow, retaining its normalization, is

\[
\dot z_a=\frac2m\sum_b c_b Q_{ab}\,w\odot\phi'(z_b),
\qquad
\dot w=\frac2m\sum_b c_b h_b.
\]

All moments below are evaluated at time zero unless time is displayed.
For neuron \(i\), write

\[
X_i=z_{1i}(0),\quad Y_i=z_{2i}(0),\qquad
U_i=\sin X_i,\quad V_i=\sin Y_i,\quad
C_i=\cos X_i,\quad D_i=\cos Y_i.
\]

The pairs \((X_i,Y_i)\) are iid with two independent \(N(0,1)\) coordinates.
The feature Gram is

\[
G=\frac1n\sum_i
\begin{pmatrix}U_i^2&U_iV_i\\U_iV_i&V_i^2\end{pmatrix}.
\]

To give the Gram predictor more information, let

\[
r_i=(U_i,V_i,C_i,D_i)^\top,\qquad
\Gamma_n=\frac1n\sum_i r_i r_i^\top.
\]

This includes the feature Gram, the derivative-feature Gram, and every mixed
feature/derivative Gram. A lower bound for predictors based on \(\Gamma_n\)
therefore also applies to either smaller collection. It does not apply to a
predictor supplied with additional fourth-order statistics.

The target fourth-order moment is

\[
M_n=M_{22;11}
=\frac1n\sum_i h_{2i}^2\phi'(z_{1i})^2
=\frac1n\sum_i V_i^2(1-U_i^2).
\]

We ask whether a function of the retained Gram can estimate this *same realized
network's* \(M_n\) with error \(o_p(n^{-1/2})\). The limit is \(n\to\infty\)
with data and labels fixed. Matching the marginal distribution of \(M_n\), or
estimating its expectation to \(o(1)\), is a different objective.

## 2. Exact covariance regression and its Gaussian limit

For one standard Gaussian coordinate set

\[
\mu=\mathbb E\sin^2X=\frac{1-e^{-2}}2,
\qquad
\nu=\operatorname{Var}(\sin^2X)=\frac{(1-e^{-4})^2}{8}>0.
\]

These follow from \(\mathbb E e^{itX}=e^{-t^2/2}\),
\(\sin^2x=(1-\cos2x)/2\), and
\(\sin^4x=(3-4\cos2x+\cos4x)/8\).
Put \(A_i=U_i^2-\mu\), \(B_i=V_i^2-\mu\). Direct multiplication gives the
finite-width identity

\[
M_n=\mu(1-\mu)-\mu(G_{11}-\mu)
 +(1-\mu)(G_{22}-\mu)+\frac1n\sum_i R_i,
\qquad R_i=-A_iB_i.
\]

The centered per-neuron Gram statistics are
\((A_i,B_i,U_iV_i)\). Independence makes \(R_i\) orthogonal in population
\(L^2\) to \(A_i,B_i\); parity makes it orthogonal to \(U_iV_i\). Its mean
is zero and its variance is \(\nu^2\). Consequently the displayed affine
Gram formula is the exact population least-squares affine predictor for every
\(n\), with mean-square error

\[
\mathbb E\left|M_n-\widehat M_n^{\rm affine}\right|^2
=\frac{\nu^2}{n}.
\]

All per-neuron variables are bounded. Applying the iid multivariate central
limit theorem (finite second moments suffice) gives

\[
\sqrt n\left(G_{11}-\mu,G_{22}-\mu,G_{12},
M_n-\widehat M_n^{\rm affine}\right)
\ \Longrightarrow\ (Z_1,Z_2,Z_3,Z_R),
\]

where the limit is centered Gaussian and

\[
\operatorname{Var}(Z_1)=\operatorname{Var}(Z_2)=\nu,
\quad \operatorname{Var}(Z_3)=\mu^2,
\quad \operatorname{Var}(Z_R)=\nu^2,
\]

with all cross covariances zero. Thus the limiting residual is independent of
the limiting Gram fluctuation. Its variance is not negligible relative to the
\(n^{-1/2}\) scale of the Gram fluctuations themselves.

This CLT alone does **not** imply convergence of finite-width conditional laws
given the exact Gram, nor rule out every width-dependent measurable predictor.
Section 4 supplies a separate argument for that stronger conclusion.

For a fixed continuously differentiable predictor \(F\) near the population
Gram, the delta method already suffices: its first-order change is a linear
combination of the three Gaussian Gram fluctuations. No such combination
eliminates the independent \(Z_R\). The least possible limiting error variance
is \(\nu^2\), attained by the affine regression above. A wrong population
value \(F(\mu I)\ne\mu(1-\mu)\) creates an order-one error instead.

## 3. Adding derivative Grams still leaves positive residual variance

The conclusion persists even for all of \(\Gamma_n\). For an explicit
covariance calculation define

\[
k=\operatorname{Cov}(\sin^2X,\cos X)
=-\frac{e^{-1/2}(1-e^{-2})^2}{4}.
\]

Here \(\mathbb E\cos X=e^{-1/2}\), and
\(\sin^2x\cos x=(\cos x-\cos3x)/4\). By parity, the only additional
Gram statistic that correlates with the even-in-each-coordinate residual
\(R=-(U^2-\mu)(V^2-\mu)\) is \(CD\). Its residual after regression on the
two diagonal feature statistics is

\[
H=CD-e^{-1}
-\frac{e^{-1/2}k}{\nu}\big[(U^2-\mu)+(V^2-\mu)\big].
\]

Direct covariance calculations give

\[
\tau=\mathbb E H^2
=(1-\mu)^2-e^{-2}-\frac{2e^{-1}k^2}{\nu}>0,
\qquad \mathbb E RH=-k^2.
\]

Hence the full-Gram affine prediction residual per neuron is

\[
R_*=R+\frac{k^2}{\tau}H,
\qquad
\sigma_*^2=\mathbb E R_*^2
=\nu^2-\frac{k^4}{\tau}>0.
\]

For completeness, both strict inequalities have structural proofs, so they do
not depend on decimal evaluation of the constants. The statistic \(CD\)
cannot be affine in \(U^2,V^2\): its Fourier frequencies \((1,1),(1,-1)\)
are absent from the latter functions. Thus \(\tau>0\). If
\(\sigma_*^2=0\), continuity and the positive Gaussian density imply that
\(V^2C^2\) is everywhere an affine combination of the full per-neuron Gram
statistics. But

\[
\sin^2y\cos^2x
=\frac14+\frac14\cos2x-\frac14\cos2y
-\frac18\cos2(x+y)-\frac18\cos2(x-y).
\]

The frequencies \((2,2),(2,-2)\) do not occur in any Gram statistic.
Linear independence of distinct trigonometric frequencies rules out that
identity. One elementary proof of this independence is to integrate a putative
identity against each corresponding exponential over \([0,2\pi]^2\).

The iid CLT applied to \((r r^\top,R_*)\) therefore gives a nondegenerate
Gaussian residual independent of the limiting full-Gram fluctuation, with
variance \(\sigma_*^2\). The exact affine mean-square error is
\(\sigma_*^2/n\).

## 4. A stronger conditional argument for arbitrary Gram-only predictors

The full Gram contains exactly the same information as the average of these
eight trigonometric functions:

\[
t(x,y)=\big(\cos2x,\sin2x,\cos2y,\sin2y,
\cos(x+y),\sin(x+y),\cos(x-y),\sin(x-y)\big).
\]

This follows from the double-angle and product-to-sum identities, in both
directions. Let \(\psi(x,y)\) be a bounded smooth function for which
\(1,t_1,\ldots,t_8,\psi\) are linearly independent. Both
\(\psi(x,y)=\sin^2y\cos^2x\) and the cubic prediction statistic in Section 5
have this property.

**Conditional-information proposition.** Write
\(\overline\psi_n=n^{-1}\sum_i\psi(X_i,Y_i)\). There is a constant
\(s_\psi>0\), independent of \(n\), such that for every sequence of measurable
estimators \(F_n(\Gamma_n)\) and every fixed \(\delta>0\),

\[
\limsup_{n\to\infty}
\mathbb P\!\left(\sqrt n\,
|F_n(\Gamma_n)-\overline\psi_n|\le\delta\right)
\le 2\Phi(\delta/s_\psi)-1<1,
\]

where \(\Phi\) is the standard Gaussian distribution function. In particular,
no such estimator has error \(o_p(n^{-1/2})\).

Here is a proof using a strictly more informative observation than the global
Gram. Set the block size to \(b=9\). For independent blocks of \(b\) neurons
define

\[
T_j=\sum_{i\in j}t(X_i,Y_i),\qquad
B_j=\sum_{i\in j}\psi(X_i,Y_i),\qquad
\kappa=\mathbb E\operatorname{Var}(B_j\mid T_j).
\]

First, \(\kappa>0\). Consider the nine-component map
\(F=(t_1,\ldots,t_8,\psi)\). The collection of vectors
\(\partial_xF(x,y),\partial_yF(x,y)\), as \((x,y)\) ranges over the plane,
spans \(\mathbb R^9\). Otherwise a nonzero vector would annihilate all these
gradients, making a nontrivial linear combination of the components of \(F\)
constant on the connected plane. That contradicts the assumed independence.
Select nine independent derivative vectors and use their associated points as
the nine neuron locations in a block. At this configuration the Jacobian of
the block map \((X_i,Y_i)_{i=1}^9\mapsto(T_j,B_j)\) has rank nine.

The inverse function theorem, applied to nine domain coordinates with a
nonsingular minor while the others vary in a small box, shows that the law of
\((T_j,B_j)\) has a component with positive density on a nonempty open set in
\(\mathbb R^9\). The Gaussian input density is continuous and strictly
positive there, which supplies this positive probability component. If
\(\kappa=0\), \(B_j\) would be a measurable function of \(T_j\) almost
surely. The graph of any such function has nine-dimensional Lebesgue measure
zero by Fubini's theorem, contradicting that positive density component.
Thus \(\kappa>0\).

Now reveal every \(T_j\), and reveal the individual coordinates of the fewer
than \(b\) leftover neurons. Call this information \(\mathcal H_n\). It
determines the global Gram, so any Gram-based estimator is also
\(\mathcal H_n\)-measurable. Conditional on this richer information, the
centered block variables

\[
Z_j=B_j-\mathbb E(B_j\mid T_j)
\]

are independent, have mean zero, and are uniformly bounded. The block
conditional variances are iid bounded functions of the iid \(T_j\), so the
strong law gives, with \(K=\lfloor n/b\rfloor\),

\[
\frac1n\sum_{j=1}^K\operatorname{Var}(B_j\mid T_j)
\longrightarrow\frac\kappa b
\quad\text{almost surely}.
\]

The conditional characteristic function of \(n^{-1/2}\sum_j Z_j\) converges
almost surely to that of \(N(0,\kappa/b)\). To check the conditional CLT
directly, expand each conditional characteristic function to second order.
For a fixed Fourier argument its third-order remainder is bounded by
\(C n^{-3/2}\), uniformly in blocks and conditioning, because \(Z_j\) is
bounded. Summing \(K\) remainders gives \(O(n^{-1/2})\); the quadratic terms
converge by the displayed strong law. Multiplying the factors, or taking their
logarithms for sufficiently large \(n\), gives the asserted Gaussian limit.

Convergence to a continuous Gaussian distribution implies uniform convergence
of the conditional distribution functions; monotonicity and a finite grid of
continuity points give this implication. Therefore the largest conditional
probability of any interval of length \(2\delta\) tends to
\(2\Phi(\delta/\sqrt{\kappa/b})-1\). Conditional on \(\mathcal H_n\), the
estimation error is precisely this centered random sum minus a possibly
width-dependent, arbitrary \(\mathcal H_n\)-measurable number. Taking the
largest interval probability handles every such number. Bounded convergence
after averaging the conditional bound proves the proposition with
\(s_\psi=\sqrt{\kappa/b}>0\).

The same richer conditioning gives the finite-width mean-square lower bound

\[
\mathbb E\operatorname{Var}(\overline\psi_n\mid\Gamma_n)
\ge \mathbb E\operatorname{Var}(\overline\psi_n\mid\mathcal H_n)
=\frac{\lfloor n/b\rfloor\kappa}{n^2}.
\]

This proves a conditional-variance statement averaged over the Gram and an
estimation lower bound in probability. It does not assert that the exact
conditional law given only \(\Gamma_n\) has been identified, or that its
conditional variance converges to the affine-regression variance.

## 5. What enters the first nonlinear prediction derivative

For this calculation temporarily keep \(m\) and \(Q\) general and set
\(\alpha=2/m\). Define at initialization

\[
p_a=\phi'(z_a),\qquad S=\sum_b y_bh_b,\qquad
M_{bc;ad}=\frac1n\sum_i h_{bi}h_{ci}p_{ai}p_{di}.
\]

Since \(w=0\), the flow gives

\[
\dot z_a=\dot h_a=0,\quad
\dot w=\alpha S,\quad
\dot f=\alpha Gy,\quad
\ddot w=-\alpha^2\sum_b(Gy)_b h_b,\quad
\ddot f=-\alpha^2G^2y.
\]

Differentiating the preactivation flow once gives

\[
\ddot h_a
=\alpha^2\sum_d Q_{ad}y_d\,S\odot p_a\odot p_d.
\]

Differentiating \(\dot w=\alpha\sum_b c_bh_b\) twice, using
\(\ddot c=-\ddot f\), and differentiating \(f_a=n^{-1}w^\top h_a\)
three times now yields the exact identity

\[
f_a^{(3)}(0)=\alpha^3(G^3y)_a
+\alpha^3\sum_{b,d,e}y_by_dy_eQ_{bd}M_{ae;bd}
+3\alpha^3\sum_{b,c,d}y_by_cy_dQ_{ad}M_{bc;ad}.
\]

Indeed the nonzero product-rule terms are
\(n^{-1}w^{(3)\top}h_a+3n^{-1}\dot w^\top\ddot h_a\), and
\(w^{(3)}=\alpha^3\sum_b(G^2y)_bh_b+\alpha\sum_b y_b\ddot h_b\).
These identities account for both cubic terms and their factors.

Return to \(m=2,Q=I\), and choose the fixed labels \(y=(1,1)^\top\), with
no width dependence. Then

\[
f_1^{(3)}(0)=(G^3y)_1+\frac1n\sum_i J(X_i,Y_i),
\]

where the completely defined per-neuron statistic is

\[
\begin{aligned}
J(x,y)
={}&4\sin^2x\cos^2x+7\sin x\sin y\cos^2x
+\sin^2x\cos^2y\\
&+\sin x\sin y\cos^2y+3\sin^2y\cos^2x\\
={}&5U^2+3V^2+8UV-4U^4-7U^3V-UV^3-4U^2V^2,
\end{aligned}
\]

with \(U=\sin x,V=\sin y\) in the last line. In particular the coefficient
of \(\cos4x\) in \(J\) is \(-1/2\), a frequency absent from all eight
Gram functions. The mixed frequencies \((2,2),(2,-2)\) also occur with
nonzero coefficients. Thus \(1,t_1,\ldots,t_8,J\) are linearly independent.
The proposition in Section 4 applies to \(J\). Subtracting the known
\((G^3y)_1\) term shows that no \(\Gamma_n\)-based estimator can recover
\(f_1^{(3)}(0)\) to \(o_p(n^{-1/2})\).

There is also a quantitative feature-Gram regression check. The residual
\(R=-(U^2-\mu)(V^2-\mu)\) is orthogonal to every centered feature-Gram
statistic, and the last expansion gives
\(\mathbb E[(J-\mathbb EJ)R]=4\nu^2\). Independence kills the terms
depending on only one squared feature; parity kills the odd terms. Therefore
the squared norm of the feature-Gram regression residual of \(J\) is at
least \((4\nu^2)^2/\nu^2=16\nu^2>0\), by Cauchy--Schwarz. The unknown
cubic fluctuation does not cancel in this fixed-label observable.

The same conclusion holds for arbitrarily small, fixed nonzero labels
\(y=\eta(1,1)^\top\), with \(\eta>0\) independent of width. The exact
formula becomes

\[
f_1^{(3)}(0)=\eta(G^3\mathbf 1)_1
+\eta^3\frac1n\sum_iJ(X_i,Y_i),\qquad \mathbf 1=(1,1)^\top.
\]

Thus the missing derivative fluctuation has size
\(\eta^3n^{-1/2}\), with its variance multiplied by \(\eta^6\).
For every fixed \(\eta>0\), this is still a nondegenerate obstruction to
\(o_p(n^{-1/2})\) recovery. No label is made to vanish as \(n\) increases.

## 6. Scope of the obstruction and a useful positive closure principle

The derivative result concerns the initialization jet, not a positive-time
trajectory norm. Matching \(f(0),\dot f(0),\ddot f(0)\) leaves a random
cubic derivative of order \(n^{-1/2}\). Formally this contributes
\(t^3/6\) times that derivative to a short-time prediction difference. To
deduce a lower bound at a fixed \(t>0\), one must additionally control the
remaining random Taylor terms on the same \(n^{-1/2}\) scale and rule out
cancellation. A deterministic \(O(t^4)\) remainder is insufficient after
multiplication by \(\sqrt n\). No such trajectory bridge is proved here.

At initialization, population moments and covariance regression still give
useful approximations: the discarded moments are \(O_p(n^{-1/2})\), hence
\(o_p(1)\). The obstruction is to making their error *negligible compared
with* the dense finite-width variability. It is not an obstruction to an
order-one deterministic large-width description, or to accepting errors of
the same order as that variability.

A general aggregate principle is to evolve the distribution of neuron states.
For \(z=(z_1,\ldots,z_m)\) and scalar readout coordinate \(w\), let
\(\rho_t\) be a probability measure on \(\mathbb R^{m+1}\), set

\[
f_a[\rho_t]=\int w\phi(z_a)\,d\rho_t(z,w),\qquad
c_a[\rho_t]=y_a-f_a[\rho_t],
\]

and transport \(\rho_t\) by the per-neuron velocity in Section 1 with these
residuals. This probability-law evolution is exact for the empirical measure
of the finite network. Replacing its empirical Gaussian initial law by the
population Gaussian law is the first approximation. This state is a full
probability measure, so the exact statement is not a finite Gram closure.

For finite horizons and bounded smooth activations such as sine, finite
quadrature of the initial law gives an autonomous finite-particle aggregate
whose dimension depends on the requested absolute tolerance and horizon, not
on the reference network width. The precise elementary principle is:
if the law evolution and its prediction map are Lipschitz in initial
\(W_1\) distance with constant \(C_T\) on the relevant horizon, and a
finite measure \(\rho_0^{(K)}\) satisfies
\(W_1(\rho_0^{(K)},\rho_0)\le\varepsilon/C_T\), its predictions differ
from the law predictions by at most \(\varepsilon\). Finite Gaussian
quantizers with this accuracy exist by truncating the integrable Gaussian
tails and partitioning a bounded box into small cells. With
\(K\) quadrature atoms, the moving state has \(K(m+1)\) coordinates plus
fixed masses; no trajectory data enter the initialization.

For the present sine flow the ingredients behind finite-horizon Lipschitz
stability are available: the loss decreases since its derivative is a negative
sum of squared parameter gradients with the prescribed positive mobilities;
therefore \(\|c(t)\|_2\le\|y\|_2\),
\(|\dot w|\le2\|y\|_2/\sqrt m\), and \(|w(t)|\) is uniformly bounded
on every finite horizon. On this bounded readout region, the sine velocity and
prediction functions are Lipschitz in neuron coordinates and residuals.
Coupling initial laws and applying the integral Gronwall inequality yields
the asserted finite \(C_T\). These constants can depend on \(T,m,Q,y\)
and are not asserted uniform as \(T\to\infty\).

This provides an absolute-error route when finite-width fluctuations may be
discarded. It does not make a fixed collection of Grams closed during nonlinear
feature learning: even the population neuron law need not remain Gaussian.
Nor does it approximate each realization to \(o(n^{-1/2})\). Achieving that
stronger coupled objective requires retaining or reconstructing the relevant
fluctuations; for the cubic jet, retaining the required \(M\) contractions
would directly remove the particular information obstruction proved here.

## 7. Check record and remaining boundaries

The arguments above were checked algebraically by their author, including
the regression decomposition, parity sectors, Gaussian trigonometric moments,
Jacobian-rank argument, conditional characteristic-function remainder, and
third-derivative product-rule factors. No numerical experiment or external
theorem retrieval was performed. The probability tools used were stated in
their needed finite-moment or bounded-variable forms; the conditional CLT
was derived directly to avoid inferring it from an unconditional CLT.

This is a complete scoped candidate awaiting the supervisor's comparison.
The exact conditional limiting law given only the global Gram, any fixed-time
trajectory lower bound, and any all-time approximation theorem remain outside
the proved claims. A deterministic same-Gram/different-moment example alone
would establish less than the typical Gaussian result proved here.
