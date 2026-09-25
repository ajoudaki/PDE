# Gaussian initialization checks for an autonomous reconstructed block

Status: a prompt-scoped mathematical derivation. No particular proposed closure has been evaluated. The explicit frozen-block example below is illustrative. No scientific sources, other study material, experiments, or numerical Gaussian integrals were used.

The main necessary condition is exact at finite width: the mean-square initialization residual must vanish. Positive residual rejects the specified exact reconstruction on a set of Gaussian initializations of positive probability. Zero residual, even together with every finite-order initialization derivative test, does not by itself establish an exact smooth closure.

## Setup and the block residual

Fix width (n), one sample, and the supplied canonical equations

\[
\begin{gathered}
z_1=W_1x/\sqrt d,\quad h_1=\phi(z_1),\quad
z_2=W_2h_1,\quad h_2=\phi(z_2),\\
f=W_3^Th_2/n,\quad r=f-y,\quad
\delta_2=W_3\odot\phi'(z_2),\quad b_1=W_2^T\delta_2,\\
\dot z_1=-2r\chi\,\phi'(z_1)\odot b_1,\quad
\dot W_3=-2rh_2,\quad
\dot W_2=-2r\delta_2h_1^T/n.
\end{gathered}
\]

Here (z_1,W_3,h_1,h_2,\delta_2,b_1\in\mathbb R^n), (W_2\in\mathbb R^{n\times n}), and (\chi) is the fixed scalar in the supplied equations. The frozen baseline has independent entries ((W_0)_{ij}\sim N(0,1/n)). The same realized matrix (W_0), with its actual transpose, is used throughout.

Let (S) contain the proposed finitely many coordinates per neuron and the specified current aggregate coordinates (Q). Write the proposed autonomous equation as

\[
\dot S=F(S;W_0),\qquad
\widetilde W_{2,ij}(S)=(W_0)_{ij}+\frac1n\kappa(m_{2,i},m_{1,j},Q).
\]

The displayed (W_0) argument allows the frozen-matrix access declared by the proposal; it is a fixed parameter, not an independently resampled random matrix or an additional time argument. Suppress that argument below. Assume all reconstructed fields are well defined, the reconstruction is differentiable, and candidate trajectories exist on the interval under discussion. The basic test requires only the relevant first derivatives. Higher-order tests require the corresponding higher regularity.

Denote the complete represented canonical state by

\[
E(S)=(z_1(S),W_3(S),\widetilde W_2(S)).
\]

All quantities in the residual are evaluated from this same state. In particular,

\[
z_2=W_0h_1+\Delta W_2h_1,\qquad
b_1=W_0^T\delta_2+\Delta W_2^T\delta_2.
\]

Assume the reconstructed (z_1,W_3) obey the displayed canonical outer equations along the candidate trajectory. If (Q) represents current aggregates, their defining identities must also hold: declaring extra coordinates to be aggregates does not prove their consistency.

The chain rule gives

\[
\dot{\widetilde W}_{2,ij}=\frac1nD_S\kappa_{ij}[F],\qquad
\rho_{ij}(S)=D_S\kappa_{ij}[F]+2r\delta_{2,i}h_{1,j}.
\]

For the stated reconstruction,

\[
D_S\kappa_{ij}[F]
=D_{m_2}\kappa[\dot m_{2,i}]
+D_{m_1}\kappa[\dot m_{1,j}]
+D_Q\kappa[\dot Q].
\]

Thus (ho/n) is exactly the error in the reconstructed (W_2) velocity. If (V) denotes the canonical vector field on ((z_1,W_3,W_2)), the outer-equation assumption gives

\[
D_SE[F]-V(E(S))=(0,0,\rho(S)/n).
\tag{1}
\]

This is a tangency requirement for the reconstructed state set, not merely an equality of expected updates.

## Initialization certificate and what its sign proves

Let (G) collect the Gaussian initialization inputs actually specified by a proposal, including the standardized entries (sqrt n(W_0)_{ij}). Other prescribed initialization values can be fixed; no distribution for them is assumed here. Require correct initialization,

\[
E(S_0(G))=X_0(G),\qquad \kappa_{ij}(S_0(G))=0.
\]

Define the nonnegative, possibly extended-valued certificate

\[
C_0=\mathbb E_G\left[\frac1{n^2}\sum_{i,j=1}^n
\rho_{ij}(S_0(G))^2\right].
\tag{2}
\]

The normalization has an exact interpretation:

\[
C_0=\mathbb E_G\|\dot{\widetilde W}_2(0)-\dot W_2(0)\|_F^2.
\tag{3}
\]

If the proposed reconstruction reproduces the canonical trajectory on a nontrivial interval for almost every initialization, differentiating at zero in (1) shows that every initialization residual is zero almost surely. Consequently (C_0=0).

Conversely, a nonnegative random variable has zero expectation only if it vanishes almost surely: if it were positive with positive probability, one of the events where it exceeds (1/k) would have positive probability and yield a positive expectation. Applying this fact to (2) proves

\[
C_0=0\quad\Longleftrightarrow\quad
\rho_{ij}(S_0(G))=0\ \text{for every }i,j\text{ almost surely}.
\]

Therefore (C_0>0), including (C_0=+\infty), rejects the specified almost-sure exact closure. It proves a nonzero residual on a set of initializations of positive probability, not necessarily at every initialization. It rejects a universal exact closure as well. If the residual depends continuously on a nondegenerate Gaussian input and is nonzero at one point of its support, continuity supplies an open neighborhood of positive Gaussian probability and hence (C_0>0).

In contrast, (mathbb E\rho_{ij}=0) is insufficient. A standard Gaussian scalar has zero mean and strictly positive mean square. Products such as (r\delta_{2,i}h_{1,j}) also cannot be factored into expectations without a proved independence statement.

### A zero initial correction need not have zero initial velocity

The identity (kappa(S_0(G))=0) constrains values on the initialization set. It does not force (D\kappa[F](S_0(G))=0): an initialized coordinate can be zero and have a nonzero prescribed initial derivative. In fact exactness requires

\[
D_S\kappa_{ij}[F](S_0(G))=-2r_0\delta_{2,i,0}h_{1,j,0}.
\tag{4}
\]

When (r_0\ne0) and both vectors (\delta_{2,0},h_{1,0}) are nonzero, the required matrix in (4) is nonzero. A nonzero loss residual alone does not imply this: a derivative or activation vector could vanish.

There is a useful, more restrictive tangency obstruction. Suppose the initialization set is a differentiable manifold (M), (kappa|_M=0), and (F(S_0)\in T_{S_0}M). Choose a differentiable curve in (M) with initial velocity (F(S_0)). Differentiating the identity that (kappa) vanishes on that curve proves (D\kappa[F](S_0)=0). Such tangency is incompatible with (4) wherever its right side is nonzero. An exact candidate can instead leave the initialization manifold immediately; zero initialization values alone do not rule that out.

### Explicit rejection of a frozen correction

If every argument of (kappa) is constant along the candidate dynamics, then (D\kappa[F]=0). Correct zero initialization therefore leaves the reconstructed correction zero forever.

For a concrete instance take (n=d=1), (x=\chi=1), (phi(u)=u), (z_1(0)=W_3(0)=1), (y=0), and (W_0=G\sim N(0,1)). At zero,

\[
h_1=1,\quad z_2=h_2=f=r=G,\quad\delta_2=1,
\quad\dot W_2=-2G.
\]

A frozen zero correction gives (dot{\widetilde W}_2=0), even if the candidate evolves both outer blocks by their canonical equations. Hence

\[
\rho(0)=2G,\qquad C_0=4\mathbb E G^2=4.
\]

This rules out that explicitly defined frozen-block proposal. It makes no assertion that any other proposed neuron-state reconstruction is frozen or has been tested.

## Lie-derivative tests and the smooth-flat obstruction

For a differentiable scalar function (a), write (L_Fa=D_Sa[F]), keeping the frozen realization fixed. Along candidate trajectories,

\[
\frac{d^k}{dt^k}\rho_{ij}(S(t))\bigg|_{t=0}
=(L_F^k\rho_{ij})(S_0).
\]

Exact reconstruction requires every existing derivative on the right to vanish. In particular, for any finite (K) and positive fixed weights (a_0,\ldots,a_K),

\[
C_{0,K}=\mathbb E_G\left[\frac1{n^2}\sum_{i,j}
\sum_{k=0}^{K}a_k\big((L_F^k\rho_{ij})(S_0(G))\big)^2\right]
\tag{5}
\]

must vanish. Positivity rejects exactness without any Taylor-series assumption. Each test is computable from the specified current-state program, if its required derivatives and Gaussian expectations are defined. The formula does not assert that this computation is tractable.

Even vanishing tests for every finite (K) are insufficient under smoothness alone. The elementary autonomous example

\[
\dot s=1,\quad s(0)=0,\qquad
\kappa(s)=
\begin{cases}e^{-1/s^2},&s>0,\\0,&s\le0\end{cases}
\]

with target scalar motion (dot w=0, w(0)=0), has defect (ho(s)=\kappa'(s)). Each derivative of (e^{-1/s^2}) for (s>0) is a polynomial in (1/s) times that exponential, which tends to zero as (s\downarrow0). Thus (kappa) is smooth and all (L_F^k\rho(0)=0), yet (kappa(s(t))=e^{-1/t^2}>0) for every (t>0). This is a counterexample to a general smooth-ODE inference, not a proposed neural closure. The obstruction is absent if the time-dependent residual has a convergent Taylor series about zero, but that is an additional hypothesis.

A different sufficient route is defect invariance. Set

\[
R(S)=\frac1{n^2}\sum_{i,j}\rho_{ij}(S)^2.
\]

Suppose along a candidate trajectory (R) is absolutely continuous, (R(S_0)=0), and

\[
\frac d{dt}R(S(t))\le a(t)R(S(t))
\tag{6}
\]

almost everywhere, where (a) is integrable on every compact time interval. Multiplying by (exp(-\int_0^t a(s)\,ds)) makes the derivative nonpositive. Its initial value is zero, and its values are nonnegative, so (R(S(t))=0) throughout that interval. For example, (L_F\rho=B(S)\rho), with integrably bounded operator norm along trajectories, implies (6) with (a(t)=2\|B(S(t))\|\).

Together with correct initialization, consistent aggregates, and exact outer equations, this proves that (E(S(t))) solves the canonical ODE. If that ODE is locally unique on the interval—satisfied, for example, by a (C^2) activation on an open domain containing the trajectories, since the finite-dimensional vector field is then locally Lipschitz—it equals the canonical solution. Thus a proved invariant-defect inequality can turn a zero initialization test into a sufficient result; initialization jets alone cannot.

## Conditional variance: use the full permitted current information

Let (U) be any square-integrable exact velocity that a deterministic proposed closure must produce. Let (mathcal I) be the sigma-algebra generated by all of its permitted current information: the whole relevant current collective state, its specified current aggregates, fixed data and parameters, and the actual frozen (W_0) information that the program is allowed to use. An exact autonomous output (b) must be (mathcal I)-measurable.

Writing (m=\mathbb E[U\mid\mathcal I]), expand (U-b=(U-m)+(m-b)). The cross term has expectation zero because its conditional expectation is

\[
\mathbb E[\langle U-m,m-b\rangle\mid\mathcal I]
=\langle\mathbb E[U-m\mid\mathcal I],m-b\rangle=0.
\]

Consequently

\[
\mathbb E\|U-b\|^2
=\mathbb E\|U-\mathbb E[U\mid\mathcal I]\|^2
+\mathbb E\|\mathbb E[U\mid\mathcal I]-b\|^2.
\tag{7}
\]

The first term, equivalently the expected trace of the conditional covariance, must vanish for any exact deterministic closure using that information. Strict positivity excludes even unrestricted measurable closure functions with that information, and hence excludes any more constrained smooth or neuron-local program.

Several boundaries matter:

- Conditioning only on (m_{2,i},m_{1,j}) is generally too restrictive when their velocities use (Q), other current coordinates, or (W_0). Positive variance after discarding permitted information is not an obstruction for the actual proposal.
- Replacing (W_0^T) by an independent backward Gaussian matrix changes the required joint law. A variance calculation under that substitution is not a certificate for the stated canonical dynamics.
- Vanishing conditional variance is only an information condition. It does not prove the existence of a smooth shared function, the prescribed finite-coordinate architecture, or the tangency equation (D\kappa[F]=-2r\delta_2h_1^T).
- In particular, if the full candidate information determines (r,\delta_2,h_1), the required (W_2) velocity already has zero conditional variance. This can make (7) vacuous for that block while (2) still detects failure to integrate its motion through the prescribed reconstruction.
- A condition checked separately at each fixed time need not produce one common time-independent function. To test autonomy across times, one may choose an independent random observation time (T), set (U=U_T), and condition on the permitted information at (T), excluding (T) itself when time is not an allowed input. Equation (7) then also tests compatibility of velocities at indistinguishable current states reached at different times. Zero variance still proves no regularity or architectural sufficiency.

No positive conditional variance for the full declared information is established here; its sign is a candidate-specific mathematical question.

## Finite-width Gaussian expectation and limiting Gaussian programs

Equations (1)–(5) are finite-width statements and require no Gaussian mean-field limit. Gaussianity determines the initialization averaging law; it does not remove correlations created by reusing the same random matrix.

Measurability suffices to define the extended nonnegative certificates. Finite values require integrability. A residual of at most polynomial growth in the finite Gaussian input has finite second moment, since Gaussian variables have moments of every polynomial order. Smoothness alone is insufficient: smooth functions can grow faster than their square is integrable under a Gaussian density.

A separate limiting calculation needs a proved limiting joint law and a moment passage. For a precise formulation, choose a uniformly random entry ((I_n,J_n)), independently of initialization, and put

\[
Z_n=\rho_{I_nJ_n}(S_0(G_n)).
\]

Then (C_{0,n}=\mathbb E Z_n^2) without an exchangeability assumption. If (Z_n) converges in distribution to (Z_\infty) and the family (Z_n^2) is uniformly integrable, then (C_{0,n}\to\mathbb E Z_\infty^2). To see the moment passage, first use the bounded continuous function (z\mapsto\min(z^2,M)) to pass to the limit at fixed (M), then let (M\to\infty); uniform integrability controls the truncation error uniformly in (n). A limiting finite program may express (Z_\infty) as a nonlinear function of finitely many jointly Gaussian variables. That representation, their covariance, the validity of shared-matrix transpose reuse, and the required integrability all need separate justification.

The fact that (C_{0,n}>0) at every finite (n) does not imply a positive limiting defect. Even a positive limit obstructs the corresponding limiting derivative-matching claim, rather than automatically every claim about output trajectories. The normalization matters: (3) is the unnormalized Frobenius velocity error for (W_2), whereas the squared Frobenius error divided by (n) is (C_{0,n}/n).

## Exactness, derivative errors, and approximate trajectories

For a fixed initialization with differentiable trajectories and matching initial states, (1) gives

\[
\widetilde W_2(t)-W_2(t)=\frac t n\rho(S_0)+o(t)
\tag{8}
\]

in finite-dimensional Frobenius norm. A nonzero initial residual therefore proves failure of exact parameter trajectories. Under a common almost-sure existence interval, applying the elementary nonnegative Fatou inequality along any sequence (t\downarrow0) to the squared norm in (8) gives

\[
\liminf_{t\downarrow0}\frac{\mathbb E\|\widetilde W_2(t)-W_2(t)\|_F^2}{t^2}
\ge C_0.
\]

Equality requires an additional moment passage, for example differentiability in mean square. No differentiation under Gaussian expectation is assumed in the inequality.

This local parameter statement has limited consequences for approximate tracking. Under a canonical vector-field Lipschitz bound (L) on a common convex region containing both trajectories and their connecting segments, variation of the norm of the full-state difference yields

\[
\|E(S(t))-X(t)\|
\le \int_0^t e^{L(t-s)}\,\|\rho(S(s))/n\|_F\,ds.
\tag{9}
\]

Indeed the difference satisfies (dot e=V(E(S))-V(X)+(0,0,\rho/n)), so its norm has upper derivative at most (L\|e\|+\|\rho/n\|_F); multiplying the resulting scalar inequality by (e^{-Lt}) and integrating proves (9). This is a sufficient tracking estimate from the time-integrated defect, not a converse.

A derivative discrepancy at a single instant need not force a large uniform trajectory error. As an elementary illustration, (u_\varepsilon(t)=\varepsilon\sin(t/\varepsilon)) has (u_\varepsilon'(0)=1) but (sup_t|u_\varepsilon(t)|\le\varepsilon\). Additional uniform time-regularity assumptions would be needed to convert the initial derivative discrepancy into a width-independent finite-time lower bound. This example is a logical boundary, not a claimed admissible neural closure.

Output tracking is weaker still. At fixed outer blocks, a (W_2)-direction (H) changes the output to first order by

\[
D_{W_2}f[H]=\delta_2^THh_1/n.
\]

This scalar map generally has a large kernel. A nonzero block-velocity residual can therefore be invisible to the instantaneous output derivative, and (2) supplies no lower bound on output error without an additional observability or sensitivity argument. Nor does a small output error prove a small derivative defect.

The justified use of the certificate is consequently narrow and decisive: a positive correctly computed value rejects the specified exact autonomous reconstruction under its stated initialization law. Establishing an exact closure requires its defect to remain zero and all other state identities to remain consistent. Establishing an approximate closure requires error estimates in the claimed norm and time regime.
