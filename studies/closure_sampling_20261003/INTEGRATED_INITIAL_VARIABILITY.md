# Initialized fluctuations and the exact small-label response

2026-10-04. Author: coordinator. New continuation of the user's integrated
compression/variability question. This note proves initialized and
infinitesimal-label statements, not a root-width theorem for a fixed nonzero
label. A separate nonlinear remainder estimate is required for that transfer.
No numerical experiment or external theorem is a proof dependency below.

## 1. Canonical model and finite-query covariance

There are L hidden layers of common width n, independent N(0,1) read-in
entries, independent N(0,1/n) hidden entries, and exactly zero readout.
For v=x/sqrt(d), the forward map is h1=phi1(Av),
hℓ=phiℓ(Wℓ hℓ−1), f=wᵀhL/n. The loss is the mean squared residual
and the mobilities are (n,1,...,1,n). The activations are C² with bounded
first and second derivatives and finite value at zero. In particular, they
have at most linear growth; bounded activation values are unnecessary.

Fix finitely many normalized inputs v0,...,vm; index 0 may be an unseen
query. Set p=m+1 and

\[
 K_{n,ab}^{(\ell)}=n^{-1}h_0^{(\ell)}(x_a)^\top
 h_0^{(\ell)}(x_b),\qquad Q^{(0)}_{ab}=v_a^\top v_b.
\]

All h in this definition are evaluated at initialization. For a positive
semidefinite p-by-p matrix Q define

\[
 F_\ell(Q)_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q),\qquad Q^{(\ell)}=F_\ell(Q^{(\ell-1)}).
 \tag{1}
\]

Use upper-triangular entries to identify symmetric matrices with vectors.
This convention merely specifies ordinary covariance matrices; it does not
change the full-matrix directional derivatives below. Let Bℓ be the
covariance of the random symmetric matrix phiℓ(Z)phiℓ(Z)ᵀ at
Z~N(0,Qℓ−1):

\[
 B_{\ell,ab,cd}=
 \mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)
             \phi_\ell(Z_c)\phi_\ell(Z_d)]
 -Q^{(\ell)}_{ab}Q^{(\ell)}_{cd}.
 \tag{2}
\]

Define the linear operator Tℓ on symmetric matrices H by

\[
 \begin{split}
 (T_\ell H)_{ab}={}&
 \tfrac12 H_{aa}\mathbb E[\phi_\ell''(Z_a)\phi_\ell(Z_b)]
 +H_{ab}\mathbb E[\phi_\ell'(Z_a)\phi_\ell'(Z_b)]\\
 &+\tfrac12 H_{bb}\mathbb E[\phi_\ell(Z_a)\phi_\ell''(Z_b)].
 \end{split}\tag{3}
\]

The formula also holds for a=b; its coefficient is
E[(phiℓ')²+phiℓ phiℓ'']. Every expectation in (1)--(3) is an explicitly
specified finite-dimensional Gaussian integral depending only on the input
Gram and the activations.

## 2. Finite-depth covariance fluctuation theorem

For every fixed p,L, the following joint convergence in distribution holds:

\[
 \sqrt n(K_n^{(\ell)}-Q^{(\ell)})\ \Longrightarrow\ \Xi_\ell,
 \quad \Xi_0=0,\quad
 \Xi_\ell=T_\ell\Xi_{\ell-1}+G_\ell,
 \tag{4}
\]

where G1,...,GL are independent centered Gaussian symmetric matrices with
covariances B1,...,BL. Thus, if Cℓ denotes the covariance of Xiℓ,

\[
 C_0=0,\qquad C_\ell=T_\ell C_{\ell-1}T_\ell^\top+B_\ell.
 \tag{5}
\]

This holds also when the input Gram is singular. It is a distributional
statement at fixed p,L, not a simultaneous growing-m, growing-L theorem.

### Proof

Conditional on all earlier layers, the rows of layer ℓ's initialized
preactivations are independent N(0,K_nℓ−1). For ℓ=1, their covariance is
the deterministic Q0. Consequently K_nℓ is an average of n conditionally
iid matrices with conditional mean Fℓ(K_nℓ−1). On any bounded set of
covariance matrices, all moments of these matrices are bounded uniformly:
|phiℓ(z)|≤|phiℓ(0)|+||phiℓ'||∞ |z| and Gaussian moments suffice.

The conditional variance bound and continuity of F imply K_nℓ→Qℓ in
probability by induction. To identify the fluctuations, fix a linear
functional u on symmetric matrices. If X_i are the centered conditional
summands, their conditional characteristic function satisfies

\[
 \mathbb E[e^{i\langle u,X_i\rangle/\sqrt n}\mid\mathcal F_{\ell-1}]
 =1-\frac{\operatorname{Var}(\langle u,X_i\rangle\mid
                    \mathcal F_{\ell-1})}{2n}+O(n^{-3/2})
 \tag{6}
\]

uniformly on every bounded covariance set. The remainder follows from
|e^{iv}-1-iv+v²/2|≤|v|³/6 and the uniform third absolute moment.
Raising (6) to the nth power gives the Gaussian characteristic function
with covariance Bℓ, in probability. Since conditional characteristic
functions have modulus at most one, this convergence also holds in L1.
Multiplication by the characteristic function of previous-layer
fluctuations proves joint convergence with an independent new Gaussian
innovation. This argument for arbitrary joint linear functionals gives
the vector statement.

For completeness, Fℓ has the directional derivative (3) on the positive
semidefinite cone, with a first-order remainder o(||H||). To prove it,
first add epsilon I to each endpoint covariance and interpolate linearly.
Differentiating the nonsingular Gaussian density and integrating twice
by parts gives

\[
 F_\ell(Q+H+\varepsilon I)-F_\ell(Q+\varepsilon I)
 =\frac12\int_0^1\sum_{u,v}H_{uv}
  \mathbb E[\partial_{uv}(\phi_\ell(Z_a)\phi_\ell(Z_b))],ds.
 \tag{7}
\]

Here Z has covariance Q+sH+epsilon I. The derivatives have at most linear
growth. Gaussian integration tails justify the integrations by parts;
uniform Gaussian moments and convergence of symmetric positive square
roots permit epsilon↓0 and make the integrand continuous in Q+sH.
Equation (7) proves (3) and the claimed remainder, including singular Q.

Inductively the previous fluctuation is tight; Taylor expansion gives
sqrt(n)[Fℓ(K_nℓ−1)−Fℓ(Qℓ−1)]=Tℓ sqrt(n)(K_nℓ−1−Qℓ−1)+oP(1).
Together with (6) this proves (4) and (5). No independence of trained
features is asserted or used. ∎

## 3. Exact onset and label-response observables

Let y be the fixed m-vector of training labels. Write K_n for the training
block of K_nL and κ_n=(K_nL_{0a})a=1,...,m. Since w0=0, hidden initial
velocities vanish and

\[
 \dot f_n(0,x_0)=\frac2m\kappa_n^\top y.
 \tag{8}
\]

For two independent dense initializations, (4) implies

\[
 \sqrt n[\dot f_n(0,x_0)-\dot{\widetilde f}_n(0,x_0)]
 \Longrightarrow N(0,\sigma_{\rm onset}^2),\qquad
 \sigma_{\rm onset}^2=rac8{m^2}
    \sum_{a,b=1}^m y_a C_{L,0a,0b}y_b.
 \tag{9}
\]

The formula is a nondegenerate lower scale exactly when its displayed
variance is positive. It is not yet a lower bound on the predictor itself.

Now replace the labels by ηy and denote the resulting actual dense
predictor by f_n^η. Define its exact derivative at zero label by
F_n(t,x)=∂η f_n^η(t,x)|η=0. Smooth dependence of the finite-dimensional
ODE on η gives, for every finite t,

\[
 F_n(t,x_0)=\kappa_n^\top K_n^{-1}
       (I-e^{-2tK_n/m})y,
 \tag{10}
\]

whenever K_n is positive definite. This is a derivative of the actual
feature-learning flow, not a replacement training algorithm. The hidden
derivatives with respect to η vanish at η=0 because their updates contain
both a residual and a readout. The readout derivative therefore solves
the constant-coefficient linear ODE giving (10).

At each fixed finite n with K_n positive definite, this derivative also
exists for the fitted predictor and

\[
 F_n(\infty,x_0)=\kappa_n^\top K_n^{-1}y.
 \tag{11}
\]

Here is the endpoint justification. On a fixed small neighborhood of the
initialized finite state, positivity of K_n persists. For sufficiently
small |η| the energy/readout bootstrap gives ||w||≤C_n|η|,
|r(t)|≤C_n|η|e^{-c_n t}, and integrated hidden velocity O_n(η²).
Indeed the readout velocity is bounded by C_n|r| and each hidden
velocity by C_n|r| ||w||; these estimates close the neighborhood before
any exit. Hence h^η(t,x)=h0(x)+O_n(η²) uniformly in time on a fixed
bounded query set. The training residual equation is
dot r=−(2/m)[K_n+O_n(η²)]r; variation of constants and its exponential
decay give ∫[r^η−ηr_lin]dt=O_n(η³), where
r_lin(t)=−exp(−2tK_n/m)y is the residual derivative at η=0.
Integrating dot w and multiplying by
h^η(x)/n yields f_n^η(∞,x)=ηκ_nᵀK_n−1y+O_n(η³).
All constants here may depend on n. This proves (11), but precisely does
not justify a fixed-η root-width comparison.

Let Q be the training block of QL and κ its query vector. Assume Q>0.
Then K_n>0 with probability tending to one. For the distributional
statements only, define the endpoint derivative observable to be zero on
the exceptional singular event. Its probability tends to zero, so this
convention does not change any limiting distribution. No actual fitted
network or endpoint is asserted on that exceptional event.
The endpoint functional in (11) has derivative

\[
 H\longmapsto H_{0X}Q^{-1}y
       -\kappa^\top Q^{-1}H_{XX}Q^{-1}y.
 \tag{12}
\]

Thus (4) and a first-order expansion of the inverse give a completely
specified centered Gaussian limit for the difference of two independent
F_n(∞,x0)'s: its variance is twice the variance of (12) applied to XiL.
The corresponding finite-time formula follows by differentiating (10),
using the identity
D(e^A)[H]=∫0¹ e^{(1-s)A}H e^{sA} ds, which follows by differentiating
the power series or solving the linearized matrix ODE.

At a training query, (12) vanishes exactly: (11) equals the fixed training
label for every invertible K_n. This is a direct cancellation at fitting,
even when (9) is nonzero. It forbids an automatic inference from onset
fluctuation to endpoint fluctuation.

## 4. Explicit dependence on m and L for orthogonal data

Take d≥m+1, v_a=e_a (a=1,...,m), and v0=e_{m+1}. The activations may
be different across layers but are odd. Define scalar Gaussian integrals

\[
 q_0=1,\quad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2>0,
 \quad a_\ell=\mathbb E\phi_\ell'(\sqrt{q_{\ell-1}}Z),
 \quad Z\sim N(0,1),
\]
\[
 \nu_0=0,\qquad \nu_\ell=q_\ell^2+a_\ell^4\nu_{\ell-1}.
 \tag{13}
\]

Then Qℓ=qℓ I, gamma=qL, and the query cross-covariance block is
C_{L,0a,0b}=νL 1{a=b}. To verify this, at diagonal covariance oddness
makes both diagonal-perturbation terms in (3) zero for a≠b. Its remaining
coefficient is aℓ². Independence of Gaussian coordinates gives
Bℓ,0a,0b=qℓ² 1{a=b}. Equations (5) and (13) follow by induction.

For Y=||y||/sqrt(m), the two-copy onset variance is exactly

\[
 \sigma_{\rm onset}^2=8\nu_LY^2/m.
 \tag{14}
\]

The population query vector κ is zero. Therefore the derivative of the
training block in (10)--(12) contributes zero to the leading fluctuation,
and for every fixed t∈[0,∞],

\[
 \sqrt n\,[F_n(t,x_0)-\widetilde F_n(t,x_0)]
 \Longrightarrow
 N\!\left(0,
 2mY^2\frac{\nu_L}{q_L^2}
          (1-e^{-2q_Lt/m})^2\right),
 \tag{15}
\]

where the final factor is 1 at t=∞. In particular, at the population
fitting timescale t=m/(2 gamma) it is (1−e−1)².

Gaussian integration by parts in one dimension gives
aℓ=E[Z phiℓ(sqrt(qℓ−1)Z)]/sqrt(qℓ−1). Cauchy--Schwarz consequently
implies aℓ⁴≤qℓ²/qℓ−1². Applying this to (13) yields

\[
 1\le\frac{\nu_L}{q_L^2}\le L.
 \tag{16}
\]

Thus the standard deviation of the **limiting Gaussian in (15)** at the
endpoint lies between sqrt(2m)Y and sqrt(2Lm)Y. This is not a convergence
claim for finite-width variances: rare poorly conditioned initializations
can destroy uniform integrability, and the hypotheses do not exclude that.
The absolute forward Gram scale cancels in this example. The
onset limiting-Gaussian standard deviation instead scales as Y/sqrt(m); the fitting
timescale m/gamma explains why these are different statements.

If every layer uses the same odd forward-normalized activation with
E phi(Z)²=1, then qℓ=1 and

\[
 \nu_L=\sum_{j=0}^{L-1}a^{4j},\qquad a=\mathbb E\phi'(Z).
 \tag{17}
\]

For a nonlinear continuous activation |a|<1: equality in Cauchy--Schwarz
would force phi(Z)=±Z almost surely and hence everywhere. Consequently
νL≤1/(1−a⁴), uniformly in depth, for this initialized label-response
observable. For identity νL=L. This distinction does not claim uniformly
bounded depth dependence for the actual nonlinear trained fluctuations.

## 5. Exact scope and next bridge

Equations (4)--(17) are initialized or exact zero-label derivative results.
The n-limit holds for each fixed m,d,L, not for an unquantified growing
family. A nonzero Gaussian limit supplies explicit limiting quantiles via
the one-dimensional standard normal CDF; it is stronger than a bare
variance heuristic. It still does not control a fixed nonzero-label
network unless the nonlinear two-copy remainder is o(Y/sqrt(n)) or is
bounded by a small multiple of that scale. An O_n(Y³) or even O(Y³)
single-run remainder cannot provide this bridge.

The route identifies a concrete target for such a bridge: at orthogonal
queries and the fitted endpoint, the Gaussian distributional fluctuation
scale is Y sqrt(m/n), up to the explicitly defined depth factor
sqrt(2νL/qL²).
This is diagnostic evidence for the fixed-label lower-bound program,
not that lower bound itself. No assertion is made that correlations under
learning can only increase variance.
