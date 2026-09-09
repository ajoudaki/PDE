# Frozen-mask gap and actual canonical L2 learned memories

2026-09-06. Bounded theoretical research sidecar. No experiments,
subagents, external mathematical imports, or continuum-limit claims.

## Result and scope

The frozen-mask strict gap **does apply** to the canonical finite-mesh
Gaussian population program with the specified first activation and top
arctan, ordinary raw updates, zero initial readout, and every fixed
\(-1<\rho<1\). Both the independent-root requirement and the
frozen-coefficient derivative convention can be checked in this program.

There is a useful correction to the generic support warning: **both
actual learned memories preserve the covariance supports** in this
particular program. At every finite positive mesh, the only linear
history constraints are the forced startup identities
\(H^{(1)}_1=H^{(1)}_0\) and \(\delta^{(2)}_0=0\). We prove this below.
The shifted-activation, antiparallel example in the harmonic dependency
is not an example for the present activations or correlation range.

A new actual-program obstruction nevertheless survives. On the attained
prefix \(k=0,1,2\), at \(\rho=0\), for every specified \(0<R<1/4\),

\[
 \lim_{\lambda\downarrow0}
 \|M_B\|_{\operatorname{Ran}\Gamma\to\operatorname{Ran}\Sigma}
 >\frac{361}{220}>1.64.                                      \tag{A}
\]

The norms here are exactly the covariance norms of the candidate, on
their supports. Thus reverse learned memory need not be a contraction
and does not become small in that norm on a vanishing time horizon.
This is an attained two-update construction, not an arbitrary matrix
example. We also obtain exact two-update formulas and finite, strictly
positive small-step limits for **both** memory norms, at every interior
correlation.

These results do not settle existence of finite upper bounds for the
memory norms uniform over all meshes on a fixed horizon. Such bounds
are neither proved nor disproved here. We give uniform bounds with
ordinary coordinate/time-weighted Euclidean outputs, and state precisely
the stronger matrix inequalities still needed. In particular, (A) is
not a claim that those stronger norms diverge under mesh refinement,
nor a claim about the full feedback product.

## 1. Exact dependencies and provenance

The following three mathematical dependencies were read in full:

| File | SHA-256 |
|---|---|
| `/tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md` | `a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a` |
| `/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md` | `cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5` |
| `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |

No mathematical files referenced inside those dependencies were read.
The procedural skill `/etc/codex/skills/investigate-conjectures/SKILL.md`
was read; its additional reference files were not imported, in accordance
with the explicit dependency restriction. This is the only deliverable
written. The candidate's previous UNVERIFIED status is resolved here
only for the finite-program statements expressly proved below.

We use the supplied raw label-update convention: \(\lambda y_b\) is
the coefficient of sample \(b\), so \(\lambda=\Delta/2\) when the
two-sample averaging factor is included in a step denoted by \(\Delta\).
This is a notation conversion, not a change of learning rates or metric.
No different loss-dependent forcing, random readout initialization,
preconditioner, or division by an activation derivative is introduced.

## 2. The actual raw program, all memories, and all formal derivatives

Write

\[
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad
 y=(1,-1)^T,\quad Y=\operatorname{diag}(y),\quad -1<\rho<1,
\]
\[
 \psi(z)=\phi_1'(z)=
 \begin{cases}
 \exp[-1/(1-(z/R)^2)],&|z|<R,\\
 0,&|z|\ge R,
 \end{cases}
 \qquad \phi_1(z)=\int_0^z\psi(u)\,du,
\]
\[
 \beta=\int_0^R\psi(u)\,du,\qquad
 \phi_2(z)=\arctan z,\quad
 p(z)=\phi_2'(z)=\frac1{1+z^2},\quad
 p'(z)=\phi_2''(z)=\frac{-2z}{(1+z^2)^2}.                \tag{1}
\]

Thus \(|\phi_1|\le\beta\le R/e\), \(0\le\psi\le e^{-1}\),
and all derivatives of both activations are bounded. The flat extension
at \(\pm R\) is smooth: each differentiated bump is an exponential
times a rational power of the distance expression, tending to zero.

For completeness, the finite-width ordinary raw updates underlying the
population law are

\[
 \begin{aligned}
 h^{(1)}_{ka}&=\phi_1(z^{(1)}_{ka}),&
 z^{(2)}_{ka}&=W^{(2)}_k h^{(1)}_{ka},&
 h^{(2)}_{ka}&=\phi_2(z^{(2)}_{ka}),\\
 \delta^{(2)}_{ka}&=w_kp(z^{(2)}_{ka}),&
 q^{(1)}_{ka}&=(W^{(2)}_k)^T\delta^{(2)}_{ka},&
 \delta^{(1)}_{ka}&=\psi(z^{(1)}_{ka})q^{(1)}_{ka},\\
 z^{(1)}_{k+1,a}&=z^{(1)}_{ka}
       +\lambda\sum_b C_{ab}y_b\delta^{(1)}_{kb},\\
 W^{(2)}_{k+1}&=W^{(2)}_k+
       \frac\lambda n\sum_b y_b\delta^{(2)}_{kb}(h^{(1)}_{kb})^T,\\
 w_{k+1}&=w_k+\lambda\sum_b y_bh^{(2)}_{kb}.
 \end{aligned}                                                   \tag{2}
\]

The initialization is the supplied one: iid first-neuron pairs
\(G\sim N(0,C)\), an independent matrix with iid \(N(0,1/n)\)
entries, and exactly \(w_0=0\). Products in (2) are coordinatewise
where appropriate. No caps are present in (2).

Fix \(k=0,\ldots,N\) and \(\lambda>0\). Set \(i=(k,a)\),
\(j=(r,b)\), with \(j<i\) meaning \(r<k\). The population law is

\[
 \begin{aligned}
 Z^{(1)}_{ka}&=G_a+\lambda\sum_{r<k,b}C_{ab}y_b
              \psi(Z^{(1)}_{rb})Q^{(1)}_{rb},&
 H^{(1)}_i&=\phi_1(Z^{(1)}_i),\\
 Z^{(2)}_i&=\xi^{(2)}_i+\sum_{j<i}A_{ij}\delta^{(2)}_j,&
 H^{(2)}_i&=\phi_2(Z^{(2)}_i),\\
 \mathsf W_k&=\lambda\sum_{r<k,b}y_bH^{(2)}_{rb},&
 \delta^{(2)}_i&=\mathsf W_kp(Z^{(2)}_i),\\
 Q^{(1)}_i&=\zeta^{(1)}_i+\sum_{r\le k,b}B_{i,rb}H^{(1)}_{rb}.
 \end{aligned}                                                   \tag{3}
\]

The independent Gaussian groups are \(G\), \(\zeta^{(1)}\), and
\(\xi^{(2)}\). Population 1 uses \((G,\zeta^{(1)})\); population 2
uses \(\xi^{(2)}\). The covariance selections are uncentered query
second moments:

\[
 \Gamma_{ij}=\mathbb E_1[H^{(1)}_iH^{(1)}_j]
       =\operatorname{Cov}(\xi^{(2)})_{ij},\qquad
 \Sigma_{ij}=\mathbb E_2[\delta^{(2)}_i\delta^{(2)}_j]
       =\operatorname{Cov}(\zeta^{(1)})_{ij}.                    \tag{4}
\]

The complete matrices are

\[
 \begin{aligned}
 S_{ij}&=\mathbb E_1[\partial_{\zeta^{(1)}_j}H^{(1)}_i],&
 (M_A)_{ij}&=\lambda\mathbf1_{r<k}\Gamma_{ij}y_b,& A&=S+M_A,\\
 D_{ij}&=\mathbb E_2[\partial_{\xi^{(2)}_j}\delta^{(2)}_i],&
 (M_B)_{ij}&=\lambda\mathbf1_{r<k}\Sigma_{ij}y_b,& B&=D+M_B.
 \end{aligned}                                                   \tag{5}
\]

These memories follow directly by unrolling the trained matrix in (2):
the forward learned term is
\(\lambda\sum_{r<k,b}y_b\delta^{(2)}_{rb}
\langle h^{(1)}_{rb},h^{(1)}_{ka}\rangle_n\), and the reverse term is
\(\lambda\sum_{r<k,b}y_bh^{(1)}_{rb}
\langle\delta^{(2)}_{rb},\delta^{(2)}_{ka}\rangle_n\).
The initial-matrix responses supply exactly \(S\) and \(D\).
There is no current learned-rank term, but there is a current derivative
term in \(D\).

Here are explicit recursions specifying every derivative in (5). For a
formal bottom-source slot \(j\), put
\(U^{(1)}_{ka,j}=\partial_{\zeta^{(1)}_j}Z^{(1)}_{ka}\) and
\(V^{(1)}_{ka,j}=\partial_{\zeta^{(1)}_j}Q^{(1)}_{ka}\). Then

\[
 \begin{aligned}
 U^{(1)}_{0a,j}&=0,\\
 V^{(1)}_{ka,j}&=\mathbf1_{(k,a)=j}
       +\sum_{r\le k,b}B_{ka,rb}\psi(Z^{(1)}_{rb})U^{(1)}_{rb,j},\\
 U^{(1)}_{k+1,a,j}&=U^{(1)}_{ka,j}
   +\lambda\sum_b C_{ab}y_b
       \bigl[\psi'(Z^{(1)}_{kb})Q^{(1)}_{kb}U^{(1)}_{kb,j}
              +\psi(Z^{(1)}_{kb})V^{(1)}_{kb,j}\bigr],\\
 S_{ka,j}&=\mathbb E_1[\psi(Z^{(1)}_{ka})U^{(1)}_{ka,j}].
 \end{aligned}                                                   \tag{6}
\]

For a formal top-source slot \(j\), put
\(U^{(2)}_{i,j}=\partial_{\xi^{(2)}_j}Z^{(2)}_i\) and
\(T^{(2)}_{i,j}=\partial_{\xi^{(2)}_j}\delta^{(2)}_i\). Then

\[
 \begin{aligned}
 U^{(2)}_{i,j}&=\mathbf1_{i=j}+\sum_{l<i}A_{il}T^{(2)}_{l,j},\\
 \partial_{\xi^{(2)}_j}\mathsf W_k
    &=\lambda\sum_{r<k,b}y_bp(Z^{(2)}_{rb})U^{(2)}_{rb,j},\\
 T^{(2)}_{ka,j}&=p(Z^{(2)}_{ka})\partial_{\xi^{(2)}_j}\mathsf W_k
           +\mathsf W_kp'(Z^{(2)}_{ka})U^{(2)}_{ka,j},\\
 D_{ka,j}&=\mathbb E_2 T^{(2)}_{ka,j}.
 \end{aligned}                                                   \tag{7}
\]

In particular,

\[
 D_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[\mathsf W_kp'(Z^{(2)}_{ka})].
                                                                  \tag{8}
\]

Every selected covariance, coefficient, and scalar expectation in
(3)--(7) is held fixed during differentiation. We differentiate the
complete earlier coordinate expressions, including the readout history;
we do not differentiate the statistical operation selecting the
coefficients. The formal slots remain separate even when their values
coincide. In particular \(\zeta^{(1)}_0=0\) and
\(\xi^{(2)}_1=\xi^{(2)}_0\) do not authorize deleting those slots.
For example, at startup

\[
 S_{1a,0b}=\lambda C_{ab}y_b\mathbb E[\psi(G_a)\psi(G_b)],           \tag{9}
\]

although the source in that column has zero attained variance. The
initial readout is held fixed at zero; a derivative with respect to a
formal readout root is a different direction and is not given a
zero-cost covariance norm here.

## 3. Why the finite Gaussian rule transfers to these activations

The softplus dependency cannot be invoked by simply substituting
activation names. In particular, the uncapped bottom map
\((z,q)\mapsto\psi(z)q\) is not globally Lipschitz:
its first derivative in \(z\) is \(\psi'(z)q\). The following finite
argument addresses that issue; it is not a uniform cap-removal theorem.

First, the remaining query maps are bounded or Lipschitz on their
attained ranges. At every width and in (3),

\[
 |\mathsf W_k|\le\pi\lambda k,\qquad
 |\delta^{(2)}_{ka}|\le\pi\lambda k.                         \tag{10}
\]

Thus, for a fixed prefix, the map \(w p(z)\) can be given a smooth
globally Lipschitz extension outside the deterministic attained readout
interval without changing a single actual value. Both matrix input
families \(H^{(1)}\) and \(\delta^{(2)}\) have deterministic coordinate
bounds. The finite rank expansions bound the trained matrix operator
norm by the initial operator norm plus a deterministic finite sum.
Consequently all raw and bounded-bottom auxiliary programs have RMS
bounds depending only on that operator norm and the fixed prefix.

For the identification proof only, replace \(q\) in the bottom update
by a smooth cutoff \(\tau_L(q)\), equal to \(q\) on \([-L,L]\),
with \(|\tau_L(q)|\le|q|\), bounded value and first derivative.
For each fixed \(L\), all required maps are globally Lipschitz, so the
self-contained conditioning, finite-rank feedback, and singular-Gram
arguments in the softplus dependency apply with one matrix and the
checked maps above. No softplus identity is used in those arguments.

At the scalar-law level let \(L\to\infty\) in causal instruction
order. For every fixed compact set of preceding coefficients,
\(Q^{(1)}\) is a Gaussian coordinate plus a bounded linear combination
of bounded features. Bottom coordinate expressions and their formal
first derivatives have polynomial bounds in the finite Gaussian source
tuple, uniformly for large cutoff levels. One can choose
\(\tau_L(q)=L\tau(q/L)\), with uniformly bounded first derivatives.
Finite induction, Gaussian square-root coupling, and dominated
convergence therefore give convergence of all selected second moments
and expected derivatives. The limiting recursion is exactly (3)--(7).
The induction also bounds its coefficients, and hence the auxiliary
scalar \(Q^{(1)}\) tails are uniformly Gaussian up to a bounded shift
for all sufficiently large \(L\).

Here is the needed transfer back to the uncapped finite-width program,
without assuming its higher coordinate moments. Compare raw and
cutoff programs with identical initialization. If \(\widetilde q\)
is a cutoff-program reverse answer, the exceptional product is bounded
in normalized Euclidean norm, for any fixed \(K>0\), by

\[
 \begin{aligned}
 \|\psi(z)q-\psi(\widetilde z)\tau_L(\widetilde q)\|_{n,2}
 \le{}& e^{-1}\|q-\widetilde q\|_{n,2}
   +K\|\psi'\|_\infty\|z-\widetilde z\|_{n,2}\\
 &+2e^{-1}\|\widetilde q\mathbf1_{|\widetilde q|>K}\|_{n,2}
   +2e^{-1}\|\widetilde q\mathbf1_{|\widetilde q|>L}\|_{n,2}.
 \end{aligned}                                                   \tag{11}
\]

This follows by adding and subtracting \(\psi(z)\widetilde q\) and
\(\psi(\widetilde z)\widetilde q\), then splitting the middle product
at \(K\). All other differences use bounded gates, the matrix
operator bound, and the ordinary contraction Cauchy--Schwarz estimate.
On an event bounding the initial operator norm, finite induction bounds
the full RMS discrepancy by a polynomial in \(K\), of fixed degree,
times the finite sum of the tail terms in (11).

For fixed \(K,L\), the cutoff identification supplies those empirical
tail estimates, using continuous upper bounds of the tail indicators.
After the width limit, let \(L\to\infty\), then \(K\to\infty\).
The uniform Gaussian tails just established dominate every fixed
polynomial in \(K\). Finally release the initial-operator bound using
the elementary Gaussian operator tail proved in the dependency.
This transfers the finite law and the bounded query second moments to
the original uncapped program. Only a fixed number of instructions is
involved; no assertion uniform in the prefix is obtained from (11).

The same conditioning proof explains independence precisely. A new
Gaussian source is a deterministic linear combination of earlier
sources of its own orientation and an innovation independent of all
previous source groups and roots. Thus the entire reverse group
\(\zeta^{(1)}\) is independent of \(G\), although the actual
\(Q^{(1)}\) and trained first features are not. The singular-Gram
transfer preserves this product Gaussian representation. The covariance
parameters depend on the law of \(G\), not its sampled value.
The auxiliary cutoffs and query regularizations in this proof leave no
change to initialization or to the final raw program (2)--(3).

## 4. Verified strict gap and its exact boundary

Let \(H\) stack \(H^{(1)}\), and put

\[
 \mathcal F=\{|G_1|\ge R,\ |G_2|\ge R\},\qquad
 \alpha=\Pr(\mathcal F^c)
 \le\frac{4R}{\sqrt{2\pi}}<1.                              \tag{12}
\]

On \(\mathcal F\), both bottom gates vanish. Induction in (3) gives
\(Z^{(1)}_{ka}=G_a\) and
\(H^{(1)}_{ka}=\beta\operatorname{sign}(G_a)\) for every formal
reverse-source value. This uses the full actual \(B=D+M_B\) and
requires no bound or sign on it.

Write \(\zeta^{(1)}=\Sigma^{1/2}Z\) with standard Gaussian \(Z\)
independent of \(G\). For any vector \(v\), finite-recursion
polynomial derivative bounds justify Gaussian integration by parts:

\[
 \mathbb E[Z(v^TH)]=\Sigma^{1/2}S^Tv.
\]

The contribution on \(\mathcal F\) is zero by independence. Testing
against a unit vector \(u\) and applying Cauchy--Schwarz gives

\[
 |\mathbb E[\mathbf1_{\mathcal F^c}(u^TZ)(v^TH)]|^2
 \le\alpha\mathbb E[\mathbf1_{\mathcal F^c}(v^TH)^2].
\]

Taking the supremum over \(u\) proves

\[
 S\Sigma S^T\preceq
 \alpha\mathbb E[\mathbf1_{\mathcal F^c}HH^T]
 \preceq\alpha\Gamma.                                     \tag{13}
\]

The top version of the same integration-by-parts calculation gives
\(D\Gamma D^T\preceq\Sigma\). Define, only on their ranges,

\[
 \|x\|_V=\|V^{\dagger/2}x\|_2,
 \qquad x\in\operatorname{Ran}V.                           \tag{14}
\]

These are ordinary finite-dimensional weighted Euclidean norms.
The inequalities imply the range inclusions for \(S,D\), and

\[
 \|S\|_{\Sigma\to\Gamma}\le\sqrt\alpha,\quad
 \|D\|_{\Gamma\to\Sigma}\le1,\quad
 \max\{\|(I-DS)^{-1}\|_{\Sigma\to\Sigma},
 \|(I-SD)^{-1}\|_{\Gamma\to\Gamma}\}
       \le\frac1{1-\sqrt\alpha}.                          \tag{15}
\]

For example, covariance domination annihilates every destination kernel
vector, giving range inclusion; conjugation by the square roots then
gives the norm bounds. The inverse bound is the convergent geometric
series. It is independent of mesh and node count. This argument controls
the expected derivatives in (5), not mean squares of pathwise
derivatives, derivatives of coefficient selection, or the full product
\((D+M_B)(S+M_A)\).

## 5. Exact covariance supports in the attained program

For every \(N\ge1\) and \(\lambda>0\),

\[
 \operatorname{Ran}\Gamma
    =\{v:\ v_1=v_0\},\qquad
 \operatorname{Ran}\Sigma
    =\{u:\ u_0=0\}.                                      \tag{16}
\]

Each time block has two coordinates. Later blocks on the right sides
are unrestricted. At \(N=0\), \(\Gamma\) is positive definite and
\(\Sigma=0\).

To prove (16), put \(F=\phi_1(G)\) and \(K=\mathbb E[FF^T]\).
Since the bivariate root has strictly positive density, every saturated
sign quadrant has positive probability. A linear combination of \(F\)
vanishing almost surely must vanish on all four such quadrants; hence
\(K\) is positive definite. Startup gives exactly

\[
 \delta^{(2)}_0=Q^{(1)}_0=0,\quad H^{(1)}_1=H^{(1)}_0=F,
 \quad \xi^{(2)}_0=\xi^{(2)}_1=X\sim N(0,K).
\]

Let \(d(X)=\arctan X_1-\arctan X_2\), and define

\[
 g_a(X)=d(X)p(X_a),\qquad J=\mathbb E[gg^T].             \tag{17}
\]

Then \(\delta^{(2)}_1=\lambda g\), and \(J\) is positive definite.
Indeed \(d\ne0\) off the diagonal, and
\(c_1p(x_1)+c_2p(x_2)\) cannot vanish on an open dense set unless
\(c_1=c_2=0\). Use the full density of \(X\) and continuity.

We now alternate two induction steps.

1. Suppose the reverse history through time \(k-1\) has no further
   linear relation. Conditional on its past, \(\zeta^{(1)}_{k-1}\)
   has a strictly positive definite Gaussian innovation. There is
   positive probability that both first preactivations at time \(k-1\)
   lie in \((-R,R)\): start with \(G\) in a smaller interior square,
   and at each previous step choose the full-support source sufficiently
   near the value making \(Q^{(1)}\) zero. Continuity and the finite
   number of steps give a positive-probability neighborhood of these
   choices. On that event, conditional on \(G\) and all earlier
   reverse sources, the affine map from the new innovation to
   \(Z^{(1)}_k\) has invertible linear part
   \(\lambda C Y\operatorname{diag}(\psi(Z^{(1)}_{k-1}))\).
   No nonzero linear combination of the two resulting \(\phi_1\)
   coordinates can be constant on all of \(\mathbb R^2\). Thus no
   new first-feature relation with the past is possible. The new
   feature Gram Schur complement is positive definite.

2. The resulting forward-source innovation at time \(k\ge2\) is
   positive definite. Conditional on earlier top sources,
   \(\mathsf W_k\) is fixed and \(Z^{(2)}_k\) has full density.
   Moreover \(\mathsf W_k\ne0\) almost surely. For \(k=1,2\) it is
   respectively \(\lambda d\) and \(2\lambda d\). For later times,
   condition one step earlier: the newest arctan difference is strictly
   increasing in its first source coordinate, so its sum with the old
   readout equals zero on a set of conditional measure zero. Since
   \(c_1p(z_1)+c_2p(z_2)\) is nonconstant for every nonzero \(c\),
   the current \(\delta^{(2)}_k\) has no linear relation with its
   past. Its new Gram Schur complement is positive definite.

The base for the first step is \(\Sigma_{11}=\lambda^2J>0\).
This proves that the reduced feature list
\((H^{(1)}_0,H^{(1)}_2,\ldots,H^{(1)}_N)\) and reduced backward list
\((\delta^{(2)}_1,\ldots,\delta^{(2)}_N)\) have positive definite
uncentered Grams, proving (16).

Now \((M_Au)_0=0\) and
\((M_Au)_1=\lambda\Gamma_{10}Yu_0=0\) for every supported \(u\).
Also \((M_Bv)_0=0\) for every \(v\). Therefore

\[
 M_A\operatorname{Ran}\Sigma\subseteq\operatorname{Ran}\Gamma,
 \qquad
 M_B\operatorname{Ran}\Gamma\subseteq\operatorname{Ran}\Sigma.
                                                                  \tag{18}
\]

There is consequently no finite-program support counterexample in this
interior-correlation family. This conclusion uses the actual activation,
startup, and source innovations; it does not follow from (13) alone.

## 6. Uniform ordinary-output estimates; the stronger question

Put \(t_k=\lambda k\), \(f_i=\sqrt{\Gamma_{ii}}\le\beta\),
\(d_i=\sqrt{\Sigma_{ii}}\le\pi t_k\), and

\[
 s_k=\lambda\sum_{r<k,b}f_{rb}d_{rb}
     \le\pi\beta\lambda^2 k(k-1)\le\pi\beta t_k^2.       \tag{19}
\]

For supported inputs, covariance Cauchy--Schwarz gives
\(|u_j|\le d_j\|u\|_\Sigma\),
\(|v_j|\le f_j\|v\|_\Gamma\), and hence the full actual memory bounds

\[
 |(M_Au)_i|\le f_i s_k\|u\|_\Sigma,\qquad
 |(M_Bv)_i|\le d_i s_k\|v\|_\Gamma.                      \tag{20}
\]

Combining them with the strict gap gives

\[
 |(Au)_i|\le f_i(\sqrt\alpha+s_k)\|u\|_\Sigma,\qquad
 |(Bv)_i|\le d_i(1+s_k)\|v\|_\Gamma.                     \tag{21}
\]

For \(T=\lambda N\) and
\(\|z\|_{\lambda,2}^2=\lambda\sum_{k,a}|z_{ka}|^2\), for example,

\[
 \|M_Au\|_{\lambda,2}
 \le\pi\beta^2 T^2\sqrt{2(T+\lambda)}\|u\|_\Sigma,
\]
\[
 \|M_Bv\|_{\lambda,2}
 \le\pi^2\beta T^3\sqrt{2(T+\lambda)}\|v\|_\Gamma.       \tag{22}
\]

These constants are uniform along \(\lambda=T/N\), \(N\ge1\).
The outputs include every coordinate; there is no projection discarding
an output component. Equivalently, applying the row estimates to the
actual random query inputs gives

\[
 \|(M_A\delta^{(2)})_i\|_{L^2}\le f_i s_k,\quad
 \|(M_BH^{(1)})_i\|_{L^2}\le d_i s_k,
\]
\[
 \|Z^{(2)}_i\|_{L^2}\le f_i(1+\sqrt\alpha+s_k),\qquad
 \|Q^{(1)}_i\|_{L^2}\le d_i(2+s_k).                      \tag{23}
\]

The covariance-norm question is stronger. Its exact necessary and
sufficient formulation is the existence, for every fixed horizon,
of finite constants independent of mesh such that

\[
 M_A\Sigma M_A^T\preceq C_A(T)^2\Gamma,\qquad
 M_B\Gamma M_B^T\preceq C_B(T)^2\Sigma.                  \tag{24}
\]

Support preservation proves finiteness at each fixed finite mesh.
It supplies no uniform lower bound on the reduced Gram Schur
complements. Neither (13) nor (20)--(23) proves (24). In particular,
the powers of \(T\) in (22) cannot be carried over to covariance
output norms. The next calculation gives an actual obstruction to
precisely that small-time inference.

## 7. Exact two-update memory norms and their small-step limits

Keep any \(-1<\rho<1\), and use only the actual prefix \(0,1,2\).
Keep \(F,K,X,d,g,J\) from (17). Define the deterministic matrices

\[
 P_{ab}=\mathbb E[p(X_a)p(X_b)],\quad
 t_a=\mathbb E[d(X)p'(X_a)],\quad T_0=PY+\operatorname{diag}(t),
\]
\[
 J^{(1)}_{ab}=C_{ab}\mathbb E[\psi(G_a)\psi(G_b)].         \tag{25}
\]

The exact first-return blocks, including the readout derivative and
the current block, are

\[
 B_{10}=D_{10}=\lambda PY,\qquad
 B_{11}=D_{11}=\lambda\operatorname{diag}(t).
\]

The learned reverse term on these blocks vanishes because
\(\delta^{(2)}_0=0\). With \(V\sim N(0,J)\) independent of \(G\),

\[
 Q^{(1)}_1=\lambda(V+T_0F),\qquad
 Z^{(1)}_2=G+\lambda^2 C Y\operatorname{diag}(\psi(G))(V+T_0F).
                                                                  \tag{26}
\]

Introduce the actual leading first-feature increment

\[
 L^{(1)}=\operatorname{diag}(\psi(G))C Y
               \operatorname{diag}(\psi(G))(V+T_0F).
\]

Taylor's formula and bounded derivatives give, in every finite \(L^p\),

\[
 H^{(1)}_2=F+\lambda^2L^{(1)}+O_{L^p}(\lambda^4).         \tag{27}
\]

Let \((X,E)\) be the centered Gaussian pair whose covariance blocks
are the uncentered Gram blocks of \((F,L^{(1)})\). This is the limit
of the *actual scaled source increment*
\((\xi^{(2)}_0,(\xi^{(2)}_2-\xi^{(2)}_0)/\lambda^2)\), not a new
initialization. Gaussian regression and square-root coupling give
convergence in every finite \(L^p\). Its conditional innovation
covariance is

\[
 V_1=\mathbb E[L^{(1)}(L^{(1)})^T]
       -\mathbb E[L^{(1)}F^T]K^{-1}\mathbb E[F(L^{(1)})^T]>0.       \tag{28}
\]

Strict positivity follows already from the \(V\)-dependent term on
the event where both root gates are positive: \(J,C\) and both gates
are nonsingular there. A function of \(F\) cannot cancel that
independent conditional variation.

Equation (6) gives
\(S_{21}=\lambda J^{(1)}Y+O(\lambda^3)\). Thus, retaining both
pieces of \(A_{21}\),

\[
 A_{21}=\lambda(J^{(1)}+K)Y+O(\lambda^3),\qquad
 Z^{(2)}_2=X+\lambda^2U+o_{L^p}(\lambda^2),
\]
\[
 U=E+(J^{(1)}+K)Yg.
\]

Since \(\mathsf W_2=2\lambda d\) exactly, define

\[
 L^{(2)}_a=d(X)p'(X_a)U_a.
\]

Then

\[
 \delta^{(2)}_2=2\lambda g+2\lambda^3L^{(2)}
                         +o_{L^p}(\lambda^3).            \tag{29}
\]

Also

\[
 V_2=\mathbb E[L^{(2)}(L^{(2)})^T]
       -\mathbb E[L^{(2)}g^T]J^{-1}\mathbb E[g(L^{(2)})^T]>0.       \tag{30}
\]

Indeed, condition on \(X\). The conditional covariance contributed
by \(E\) is
\(\operatorname{diag}(d p'(X))V_1\operatorname{diag}(d p'(X))\),
which is positive definite almost surely, since \(d\ne0\) and
\(X_a\ne0\) almost surely. Subtracting a linear function of \(g(X)\)
cannot remove it.

Here is also an exact, nonasymptotic expression for the two memory
norms. Write \(\Gamma_{21}=\mathbb E[H^{(1)}_2F^T]\),
\(\Sigma_{21}=\mathbb E[\delta^{(2)}_2(\delta^{(2)}_1)^T]\), and

\[
 V_{1,\lambda}=\Gamma_{22}-\Gamma_{21}K^{-1}\Gamma_{12},\qquad
 V_{2,\lambda}=\Sigma_{22}
                  -\Sigma_{21}(\lambda^2J)^{-1}\Sigma_{12}.
\]

Both are positive definite by Section 5. The only nonzero action of
\(M_A\) on supported inputs is
\((M_Au)_2=\lambda\Gamma_{21}Yu_1\); that of \(M_B\) is
\((M_Bv)_2=\lambda\Sigma_{21}Yv_1\). Block inversion therefore gives

\[
 \|M_A\|_{\Sigma\to\Gamma}
   =\lambda^2\|V_{1,\lambda}^{-1/2}\Gamma_{21}YJ^{1/2}\|_{\rm op},
\]
\[
 \|M_B\|_{\Gamma\to\Sigma}
   =\lambda\|V_{2,\lambda}^{-1/2}\Sigma_{21}YK^{1/2}\|_{\rm op}.
                                                                  \tag{31}
\]

For clarity about support and optimization: after deleting the repeated
feature block, an output with first block zero has covariance norm
given by the inverse Schur complement. For a prescribed input block
\(u_1\), its minimum-norm supported extension has squared norm
\(u_1^T(\lambda^2J)^{-1}u_1\); the later block is its covariance
regression extension. The analogous assertion for \(v_1\) uses \(K\).
Thus (31) optimizes over actually supported vectors, with the correct
cost of their later components.

Equations (27)--(30) give
\(V_{1,\lambda}/\lambda^4\to V_1\),
\(V_{2,\lambda}/(4\lambda^6)\to V_2\),
\(\Gamma_{21}\to K\), and \(\Sigma_{21}/(2\lambda^2)\to J\).
Consequently

\[
 \boxed{
 \begin{aligned}
 \|M_A\|_{\Sigma\to\Gamma}
    &\longrightarrow\|V_1^{-1/2}KYJ^{1/2}\|_{\rm op}\in(0,\infty),\\
 \|M_B\|_{\Gamma\to\Sigma}
    &\longrightarrow\|V_2^{-1/2}JYK^{1/2}\|_{\rm op}\in(0,\infty).
 \end{aligned}}                                                 \tag{32}
\]

This supplies new actual learned-memory estimates without pretending
that small matrix entries imply small covariance-norm operators.

## 8. A quantitative attained obstruction at rho = 0

We now prove (A), with conservative constants and no numerical
experiment. Set \(\rho=0\). Then \(G_1,G_2\) are independent,
\(K=kI\), and \(X_1,X_2\) are independent \(N(0,k)\). Put

\[
 p_0=\Pr(|G_1|<R)<\frac15,\quad
 a=\mathbb E\psi(G_1)^2<\frac1{35},\quad
 q_4=\mathbb E\psi(G_1)^4<\frac1{250}.
\]

These bounds use \(e^{-2}<1/7\), \(e^{-4}<1/50\), and
\(2R/\sqrt{2\pi}<1/5\). Saturation also gives

\[
 0<k\le\beta^2<\frac1{100},\qquad
 k\ge(1-p_0)\beta^2>\frac45\beta^2,
 \qquad b:=a+k<\frac1{25}.                               \tag{33}
\]

Here \(J^{(1)}=aI\) and \(U=E+bYg\). Let
\(e_+=(1,1)^T/\sqrt2\), and write \(j_+=e_+^TJe_+\).
Exchange symmetry makes \(e_+\) an eigenvector of \(J\). We first
bound this eigenvalue from below. Since
\(|\arctan x-x|\le|x|^3/3\), \(1-p(x)\le x^2\), and
\(|d(X)|\le|X_1-X_2|\), elementary independent Gaussian moments give

\[
 \|e_+^Tg-\sqrt2(X_1-X_2)\|_{L^2}
 \le\left(\frac{\sqrt{60}}3+\sqrt{24}\right)k^{3/2}
 <\frac{15}{2}k^{3/2}.
\]

For the first term use the independent, centered arctan remainders;
for the second use
\(\mathbb E[(X_1-X_2)^2(X_1^2+X_2^2)^2]=48k^3\).
Since \(\|\sqrt2(X_1-X_2)\|_2=2\sqrt{k}\), (33) implies

\[
 j_+>\left(\frac{19}{10}\right)^2k=\frac{361}{100}k.       \tag{34}
\]

Next bound the second moment of the actual first-feature increment.
Let \(\bar p=\mathbb E p(X_1)\) and
\(a_0=\mathbb E p(X_1)^2+\mathbb E[\arctan(X_1)p'(X_1)]\).
Independence and oddness give

\[
 T_0=\begin{pmatrix}a_0&-\bar p^2\\\bar p^2&-a_0\end{pmatrix},
 \qquad 1-4k\le a_0\le1.
\]

The lower bound follows from \(p(x)^2\ge1-2x^2\) and
\(|\arctan x\,p'(x)|\le2x^2\), with the latter product nonpositive.
Thus all displayed absolute coefficients are at most one. Moreover
\(J_{aa}\le\mathbb E d^2\le2k\). In this independent-root case,
\(L^{(1)}_a=\psi(G_a)^2y_a(V_a+(T_0F)_a)\). The cross term
involving \(V\) vanishes, as does the mixed \(F_1F_2\) term.
Therefore

\[
 \operatorname{tr}\operatorname{Cov}(E)
   =\mathbb E|L^{(1)}|^2
   \le2q_4(3k+\beta^2)
   \le\frac{17}{2}q_4k<\frac{17}{500}k.                  \tag{35}
\]

Write \(e_+^TL^{(2)}\) as its \(E\) part and its \(bYg\) part.
For the first part, \(|p'(x)|\le2|x|\) gives

\[
 \left|\frac{d}{\sqrt2}\sum_a p'(X_a)E_a\right|^2
 \le2(X_1-X_2)^2|X|^2|E|^2.
\]

For any centered Gaussian vector \(E\) jointly Gaussian with this
\(X\),

\[
 \mathbb E[(X_1-X_2)^2|X|^2|E|^2]
 \le36k^2\mathbb E|E|^2.                                \tag{36}
\]

Here is a direct verification, so no Gaussian moment theorem is being
imported. Set \(X_-=(X_1-X_2)/\sqrt2\),
\(X_+=(X_1+X_2)/\sqrt2\). They are independent \(N(0,k)\).
For each coordinate write \(E_a=c_aX_-+d_aX_++\eta_a\), with Gaussian
\(\eta_a\) independent of \((X_-,X_+)\), by ordinary Gaussian
regression. Against the weight \(2X_-^2(X_-^2+X_+^2)\), the three diagonal
second-moment multipliers, per unit variance, are respectively
\(36k^2,12k^2,8k^2\); cross terms vanish by parity. These values
use only \(\mathbb E X_-^2=k\), \(\mathbb E X_-^4=3k^2\), and
\(\mathbb E X_-^6=15k^3\), obtained by Gaussian integration by parts.
Summing proves (36).

By (35)--(36), the \(E\) part has \(L^2\) norm at most
\(\sqrt{306/125}\,k^{3/2}\). For the other part, the scalar function
\(p'p=-2x/(1+x^2)^3\) has derivative of absolute value at most two.
Indeed its derivative is \((-2+10x^2)/(1+x^2)^4\); the stated bound
follows directly for \(x^2\ge0\). Hence

\[
 \left|\frac{bd^2}{\sqrt2}
        [p'(X_1)p(X_1)-p'(X_2)p(X_2)]\right|
 \le\sqrt2 b|X_1-X_2|^3.
\]

Its \(L^2\) norm is at most
\(\sqrt{240}\,b k^{3/2}<\sqrt{240}\,k^{3/2}/25\).
Combining these estimates,

\[
 \|e_+^TL^{(2)}\|_{L^2}
 <\left(\sqrt{306/125}+\frac{\sqrt{240}}{25}\right)k^{3/2}
 <\frac{11}{5}k^{3/2}.                                  \tag{37}
\]

Finally, (30) gives
\(e_+^TV_2e_+\le\mathbb E(e_+^TL^{(2)})^2\), whereas
\(e_+^TJYKYJe_+=k j_+^2\). Testing the matrix norm in (32) in this
destination direction and using (34)--(37) yields

\[
 \|V_2^{-1/2}JYK^{1/2}\|_{\rm op}
 \ge\frac{j_+\sqrt{k}}{\|e_+^TL^{(2)}\|_{L^2}}
 >\frac{361/100}{11/5}=\frac{361}{220}.                   \tag{38}
\]

This proves (A). In particular, for each fixed allowed \(R\),
\(\|M_B\|_{\Gamma\to\Sigma}>8/5\) at all sufficiently small
positive steps on this attained two-update prefix. All directions used
in (31) and (38) have covariance-supported extensions; no independent
choice of an impossible time slot is used.

The obstruction also persists inside any fixed-horizon refinement.
For a longer actual history, test the matrix inequality
\(M_B\Gamma M_B^T\preceq c^2\Sigma\) on vectors supported in the
first three time blocks. Causality makes this exactly the corresponding
inequality for the attained two-update prefix. Therefore the full-history
memory norm is at least its prefix norm. In particular, for every fixed
\(T>0\), at \(\rho=0\),

\[
 \liminf_{N\to\infty,\ \lambda=T/N}
 \|M_B^{[0:N]}\|_{\Gamma^{[0:N]}\to\Sigma^{[0:N]}}
 >\frac{361}{220}.                                      \tag{39}
\]

The strict inequality follows because the prefix norms converge to the
fixed limit in (38), which is strictly larger than the displayed bound.
This excludes a mesh-uniform contraction constant for that memory; it
does not exclude a larger finite mesh-uniform bound.

The feature horizon here is \(2\lambda\downarrow0\). Thus any bound
of the form \(\|M_B\|\le\varepsilon(T)\), uniform over prefixes
with horizon at most \(T\), must have
\(\liminf_{T\downarrow0}\varepsilon(T)\ge361/220\). It cannot be
a perturbation estimate tending to zero. This does not refute a finite,
non-small bound in (24), or a different argument controlling the full
feedback product while retaining cancellation between its terms.

## 9. Research-state update

| Claim | Result for the present canonical program |
|---|---|
| Correct first/root Gaussian independence and frozen derivative convention | Verified, with uncapped activation-transfer issue addressed in Section 3 |
| Frozen-mask inequality \(S\Sigma S^T\preceq\alpha\Gamma\) | Proved uniformly in mesh, prefix, and interior correlation; stronger masked inequality retained |
| Supported inverses for derivative-only \(DS,SD\) | Proved with bound \((1-\sqrt\alpha)^{-1}\) |
| Actual memories preserve covariance supports | Proved for every finite positive mesh and every \(-1<\rho<1\) |
| Generic/harmonic support warnings yield a counterexample here | They do not; the exact supports (16) exclude one |
| Complete memory bounds with ordinary coordinate/time-weighted outputs | Proved uniformly on fixed horizons, (20)--(23) |
| Actual two-update covariance memory norms | Exact formulas (31); finite positive small-step limits (32) |
| Reverse memory is a contraction or vanishes on short horizons | Falsified by the attained \(\rho=0\) estimate (38) |
| Finite covariance-norm upper bounds for both memories uniform over all meshes at a fixed horizon | Open here; exact missing inequalities are (24) |
| Uniform bound for full feedback, pathwise sensitivity second moments, or cavity-trace time integrals | Not supplied by this result |
| Full globalMF, continuum construction, or all-time raw-GD convergence | Not claimed |

The candidate therefore closes a genuine derivative-only mesh-uniform
gap in this activation family. For the actual learned terms, the next
obligation is quantitative control of the reduced history Gram Schur
complements in (24), with the non-small reverse-memory effect (38)
retained. Support leakage is not that obligation in the present
interior-correlation program.
