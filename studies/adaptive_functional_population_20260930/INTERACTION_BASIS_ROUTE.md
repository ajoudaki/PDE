# Interaction-source population modes and autonomous time memory

Independent scoped route; frozen before reading other routes. Inputs are the supervisor's prompt only. No book, code, other study, external scientific source, or other route was inspected. This is a theoretical construction, not an empirical claim. The investigate-conjectures and solve-math-rigorously process instructions were applied.

## Result and scope

There is a concrete autonomous construction with two approximation orders: a population-interaction rank $p$, and a time-memory order $q$. It retains the exact fixed initialization matrices and uses $2(L-1)npq+nd+O(Lnp+Lp^2+n)$ evolving or working scalars. Population interactions are evaluated from the **current reconstructed network**, using matrix-free expectation products. No full trained hidden matrix or stored past network drives the construction.

The strongest unconditional statements established here are exact memory identities, a smooth source sketch with no spectral-gap assumption, a nuclear-mass source approximation bound, and a finite-horizon conditional error theorem. **There is no full efficient width-uniform trajectory theorem here:** reducing ridge error can increase the factor time-derivative and stability constants, and the separate bounds have not been balanced uniformly in width. These results do not prove that regularity of $f_*$ alone gives subquadratic memory at a specified accuracy. A concrete network example with constant $f_*$ prevents deducing small interaction rank from target simplicity alone, at relative source/weight accuracy. It does not give an output-error lower bound or a high-probability Gaussian-initialization lower bound.

All width-dependent constants remain explicit dependencies. The result concerns fixed $T<\infty$, fixed $L$, and fixed $n$. It is not a width limit, an all-time claim, or a total-storage claim: the unchanged dense Gaussian initialization itself remains stored.

## 1. Exact system and access assumptions

Put $h_0(x)=x/\sqrt d$, $h_\ell=\phi(W_\ell h_{\ell-1})$, and

\[
 f_\theta(x)=n^{-1}w^\top h_L(x),\qquad r_\theta=f_\theta-f_*,
 \qquad \mathcal E(\theta)=\mathbb E_\mu r_\theta^2.
\]

Use the backward fields in the assignment,

\[
 \delta_L=w\odot\phi'(W_Lh_{L-1}),\qquad
 \delta_\ell=\phi'(W_\ell h_{\ell-1})\odot W_{\ell+1}^\top\delta_{\ell+1}.
\]

The canonical learning-rate convention, clarified by the supervisor after the first freeze, accelerates the first layer and readout by a factor $n$ relative to the hidden layers. The actual sources are

\[
 G_\ell(\theta)=-\frac2n\mathbb E_\mu[r_\theta\delta_\ell h_{\ell-1}^\top],
 \qquad \ell=2,\ldots,L,
\]

\[
 F_1(\theta)=-2\mathbb E_\mu[r_\theta\delta_1h_0^\top],
 \qquad H(\theta)=-2\mathbb E_\mu[r_\theta h_L].
\]

Thus $\dot W_\ell=G_\ell$ for interior layers, $\dot W_1=F_1$, and $\dot w=H$, with $w(0)=0$. This convention includes the first-layer $1/\sqrt d$ in $h_0$. All parameter-state norms in this document use the canonical normalized metric

\[
 \|d\theta\|^2=\frac{\|dW_1\|_F^2}{n}
       +\sum_{\ell=2}^L\|dW_\ell\|_F^2
       +\frac{\|dw\|^2}{n}. \tag{1.1}
\]

Matrix-factor and source norms continue to mean unnormalized Frobenius norms. This correction supersedes the initial draft's outer-layer scaling; none of its Euclidean-metric energy claims are retained.

A sufficient data hypothesis for the theorem below is

\[
 \|x\|\le R_x\sqrt d\quad\mu\text{-a.s.},\qquad |f_*(x)|\le R_f,
 \qquad \phi\in C_b^2(\mathbb R).
\]

The data law can have any finite cardinality or infinite support. Target smoothness is not needed for the identities or the estimates under these boundedness assumptions. The expectation maps are continuously differentiable and locally Lipschitz in the finite-dimensional parameters: first parameter derivatives introduce bounded input factors, bounded activation derivatives, and finite products of bounded-on-compacts matrices. Dominated differentiation therefore applies.

For the exact flow, $d\mathcal E/dt=-\|\dot\theta\|^2$, so

\[
 \int_0^T\|\dot\theta\|^2dt\le\mathcal E(0),\qquad
 \|\theta(t)-\theta(0)\|\le\sqrt{T\mathcal E(0)}.
\]

All local constants can consequently be taken on a specified ball around the actual, unchanged initialization. They can depend strongly on its operator norms, on $n,d,L,T,R_x,R_f$, and on the sketch regularization below.

An abstract probability measure is not an algorithmic input. A computational implementation additionally needs a streamable finite dataset, or a specified computable integration/sampling interface for $\mu$. Integration accuracy is a separate numerical parameter. Exact expectation access is used only to state the analytic construction; Section 7 accounts for its replacement.

## 2. Why cross interactions can compress when fields do not

For one interior layer, define Hilbert-space operators on $\mathcal H=L^2(\mu)$,

\[
 a(x)=-\frac{2}{\sqrt n}r(x)\delta_\ell(x),\quad
 b(x)=\frac{h_{\ell-1}(x)}{\sqrt n},\quad
 A\psi=\mathbb E[a\psi],\quad B\psi=\mathbb E[b\psi].
\]

Then $G_\ell=AB^*$. For any rank-$p$ orthogonal population projector $P$,

\[
 G_\ell=APB^*+A(I-P)B^*,\qquad
 APB^*=\sum_{k=1}^p\mathbb E[a e_k]\mathbb E[b e_k]^\top
\]

when $e_1,\ldots,e_p$ is an orthonormal frame for $P\mathcal H$. This is an exact identity, including its cross residual. It does not replace either field by a pointwise approximation.

Choose $P$ as the top right singular subspace of $B$. Its ((p+1))-st singular value is at most $\|B\|_{\mathrm{HS}}/\sqrt{p+1}$, because the preceding (p+1) squared singular values are at least as large. Therefore

\[
 \|A(I-P)B^*\|_F
 \le \|A\|_{\mathrm{HS}}\|(I-P)B^*\|_{\mathrm{op}}
 \le \frac{\|A\|_{\mathrm{HS}}\|B\|_{\mathrm{HS}}}{\sqrt{p+1}}. \tag{2.1}
\]

The corresponding population functions have finite descriptions:

\[
 e_k(x)=v_k^\top b(x)/\sigma_k,
\]

where $v_k\in\mathbb R^n$ is a left singular vector of $B$ and $\sigma_k>0$. Only positive singular directions use this formula; if the rank is smaller than p, null directions contribute nothing and need not be stored. Their descriptions cost (np+O(p)), and their evaluation uses the current network. A dense covariance is unnecessary: its product with (v) is $\mathbb E[b(b^\top v)]$. Eigenvalue crossings and small singular values nevertheless make this particular frame a poor unconditional dynamical implementation.

Even stronger cross compression is possible. Define the source nuclear mass

\[
 \mathcal B_\ell(\theta)=\mathbb E\bigl[\|a(x)\|\|b(x)\|\bigr].
\]

An outer product has nuclear norm $\|a\|\|b\|$; finite-sum approximation and the triangle inequality give

\[
 \|G_\ell\|_*\le\mathcal B_\ell
 \le\|A\|_{\mathrm{HS}}\|B\|_{\mathrm{HS}}.
\]

If $\tau_p(G)^2=\sum_{j>p}\sigma_j(G)^2$, then

\[
 \tau_p(G)^2\le\sigma_{p+1}(G)\sum_{j>p}\sigma_j(G)
 \le\frac{\|G\|_*^2}{p+1}. \tag{2.2}
\]

Thus a nuclear-mass bound suffices for **existence** of an accurate low-rank source in Frobenius norm. It does not imply that every noisy field has a small Hilbert-space tail. For example, $A=B=I_N/\sqrt N$ has order-one Hilbert--Schmidt field energy outside every $p\ll N$ subspace, whereas $AB^*=I_N/N$ has Frobenius norm $N^{-1/2}$. Large field tails can have a small contraction. Conversely, cancellation-specific source SVD can outperform the forward-only estimate (2.1).

## 3. A smooth matrix-free interaction sketch without spectral gaps

For each interior layer fix a read-only Gaussian sketch $\Omega\in\mathbb R^{n\times p}$, independent of the initialization, and a regularization $\lambda>0$. Its entries have variance one; changing their scaling changes the interpretation of $\lambda$. At the current reconstructed parameter state compute

\[
 J=G(\theta)\Omega,\qquad
 R=(J^\top J+\lambda I_p)^{-1/2},\qquad
 A_p=JR,\qquad B_p=G(\theta)^\top A_p. \tag{3.1}
\]

Here $A_p,B_p\in\mathbb R^{n\times p}$; these symbols denote matrix factors, not the Hilbert-space operators in Section 2. Their source is

\[
 S_{p,\lambda}(\theta)=A_p B_p^\top
 =J(J^\top J+\lambda I_p)^{-1}J^\top G(\theta). \tag{3.2}
\]

This map and these particular factors are continuously differentiable on every parameter compact set. The positive shift avoids eigenvector choices, spectral gaps, rank changes, and frame discontinuities. Only a $p\times p$ positive-definite inverse square root is taken. In particular $A_p(0)=B_p(0)=0$, because the hidden sources vanish when $w=0$.

The two population product calls are exactly

\[
 G V=-\frac2n\mathbb E[r\delta(h^\top V)],\qquad
 G^\top U=-\frac2n\mathbb E[r h(\delta^\top U)]. \tag{3.3}
\]

They can be streamed with (O(np)) accumulators. The current $G$ itself is never assembled. Network evaluation uses the unchanged dense $W_{\ell,0}$ plus the stored low-rank correction from Section 4. Dense fixed-matrix query runtime is allowed; a dense evolving trained matrix is not present.

### Source error, with proof

For any fixed matrix $G$, any integer (k<p-1), and Gaussian $\Omega$,

\[
 \mathbb E_\Omega\|G-S_{p,\lambda}\|_F^2
 \le\left(1+\frac{k}{p-k-1}\right)\tau_k(G)^2
       +\lambda\frac{k}{p-k-1}. \tag{3.4}
\]

To prove this, write $G=U\Sigma V^\top$ and split $V^\top\Omega=(\Omega_1^\top,\Omega_2^\top)^\top$ after $k$ rows. The ridge solution $Z=(J^\top J+\lambda I)^{-1}J^\top G$ minimizes

\[
 \|G-JZ\|_F^2+\lambda\|Z\|_F^2.
\]

Use $Z_0=\Omega_1^\dagger[I_k\;0]V^\top$ as a trial matrix. Since $\Omega_1\Omega_1^\dagger=I_k$ almost surely, direct block multiplication gives

\[
 \|G-S_{p,\lambda}\|_F^2
 \le\|\Sigma_2\|_F^2+
 \|\Sigma_2\Omega_2\Omega_1^\dagger\|_F^2+
 \lambda\|\Omega_1^\dagger\|_F^2. \tag{3.5}
\]

Conditional on $\Omega_1$, independence and unit Gaussian variance give expectation $\|\Sigma_2\|_F^2\|\Omega_1^\dagger\|_F^2$ for the middle term. For completeness,

\[
 \mathbb E\|\Omega_1^\dagger\|_F^2=\frac{k}{p-k-1}.
\]

Indeed, the (i)-th diagonal entry of $(\Omega_1\Omega_1^\top)^{-1}$ is the reciprocal squared distance of row (i) from the span of the other (k-1) rows. Conditional on those rows, this squared distance is a sum of (p-k+1) independent squared standard Gaussians. For such a sum with $\nu>2$ terms, integrating its density proportional to $z^{\nu/2-1}e^{-z/2}$ gives $\mathbb E[1/z]=1/(\nu-2)$. Summing the $k$ diagonal expectations proves the formula and (3.4).

Taking $p=2k+2$, (2.2) gives the simpler bound

\[
 \mathbb E_\Omega\|G-S_{p,\lambda}\|_F^2
 \le\frac{2\mathcal B^2}{k+1}+\lambda. \tag{3.6}
\]

The exact trajectory is independent of these additional sketches. Therefore (3.4) can be integrated along it without an adaptive-data assumption. If $R_\ell(t)$ denotes its right side, then with probability at least $1-\alpha$,

\[
 \sup_{t\le T}\left\|\int_0^t(G-S_{p,\lambda})(\theta(s))ds\right\|
 \le\left[\frac{T}{\alpha}\int_0^T\sum_{\ell=2}^L R_\ell(s)ds\right]^{1/2}. \tag{3.7}
\]

The norm combines layer Frobenius norms. This follows from Cauchy--Schwarz in time and Markov's inequality. It is a bound on an omitted source evaluated along the exact path; stability is still needed to compare the autonomous surrogate.

The factor Lipschitz constants are finite but can increase as $\lambda\downarrow0$. For example, if $K\succeq\lambda I$ and $Q=K^{1/2}$, its differential obeys $Q\,dQ+dQ\,Q=dK$. Diagonalizing $Q$ bounds $\|dQ\|_F\le\|dK\|_F/(2\sqrt\lambda)$. Since $d(K^{-1/2})=-Q^{-1}(dQ)Q^{-1}$, its norm is at most $\|dK\|_F/(2\lambda^{3/2})$. The chain rule in (3.1) then yields finite constants depending on $\|\Omega\|,\|G\|,\lambda,p$. No width-independent or regularization-independent stability is asserted.

As a useful well-posedness check, the $q=\infty$ projected flow remains dissipative. Write $S_{p,\lambda}=P_\lambda G$, where $0\preceq P_\lambda\preceq I$. Then

\[
 \langle G,P_\lambda G\rangle_F\ge\|P_\lambda G\|_F^2.
\]

Together with exact first-layer and readout evolution, this implies $d\mathcal E/dt\le-\|\dot\theta\|^2$ for that projected flow. The same finite-horizon parameter ball suffices. Finite $q$ need not preserve this dissipation identity.

## 4. Exact finite-state time moments

Let $P_j$ be the ordinary Legendre polynomial and define orthonormal polynomials on $[0,1]$ by

\[
 \ell_j(u)=\sqrt{2j+1}\,P_j(2u-1),\qquad j=0,1,\ldots.
\]

For arbitrary square-integrable source factor paths $A_p(s),B_p(s)$, define

\[
 U_j(t)=\int_0^t A_p(s)\ell_j(s/t)ds,\qquad
 V_j(t)=\int_0^t B_p(s)\ell_j(s/t)ds. \tag{4.1}
\]

Parseval's identity, applied entrywise, gives the exact matrix identity

\[
 \int_0^t A_p(s)B_p(s)^\top ds
   =\frac1t\sum_{j=0}^\infty U_j(t)V_j(t)^\top. \tag{4.2}
\]

The series converges in Frobenius norm: the norm of a tail is bounded by the product of the two corresponding square-summable coefficient tails. This encodes the product average; neither factor is reconstructed pointwise in time.

Define the lower-triangular constants $D_{jk}$ by the polynomial identity

\[
 u\ell_j'(u)=\sum_{k=0}^jD_{jk}\ell_k(u).
\]

Differentiation of (4.1) for (t>0) gives

\[
 \dot U_j=\ell_j(1)A_p(t)-t^{-1}\sum_{k=0}^jD_{jk}U_k,\qquad
 \dot V_j=\ell_j(1)B_p(t)-t^{-1}\sum_{k=0}^jD_{jk}V_k. \tag{4.3}
\]

There is no omitted higher moment in these equations. For example $D_{00}=0$; $D_{10}=\sqrt3,D_{11}=1$, so $\dot U_0=A_p$ and $\dot U_1=\sqrt3A_p-(\sqrt3U_0+U_1)/t$.

The $q$-memory reconstruction is

\[
 \widehat W_\ell(t)=W_{\ell,0}+
   t^{-1}\sum_{j=0}^{q-1}U_{\ell,j}(t)V_{\ell,j}(t)^\top,
 \qquad \ell=2,\ldots,L. \tag{4.4}
\]

Evolve $W_1,w$ with their exact population gradients evaluated on this reconstructed network. Evaluate (3.1) on that same network to drive (4.3). A scalar clock satisfying $\dot t=1$ makes the system autonomous. Its current $W_1,w,U,V,t$, plus the fixed initialization and fixed sketches, determine its continuation; no history is needed.

The apparent singularity at $t=0$ has the prescribed continuous integral solution (4.1). In general $U_j/t\to A_p(0)\mathbf1_{j=0}$, and likewise for $V_j$. Here both source factors vanish initially. On a short interval the corresponding integral map is a contraction: orthogonal time projection is an $L^2$ contraction, and the factor maps are locally Lipschitz. This gives a unique regular solution near zero; for (t>0) the displayed finite ODE is locally Lipschitz. Restarting at positive time uses the stored moments, not a reconstructed prefix.

The learned correction in (4.4) has rank at most $pq$. Its action on a vector is a sequence of (2pq) dot products and vector additions. First-layer storage is $nd$. Moment storage is (2(L-1)npq). The fixed (D)-operator can be applied by prefix sums in (O(npq)) arithmetic with (O(np)) scratch; no $q^2$ table is needed. The proof of this post-freeze implementation refinement is given in Section 10. Population-query and dense-fixed-matrix runtime remain separate from state complexity.

### A quantitative time-tail bound

If $\|\dot A_p(s)\|_F\le K_A$ and $\|\dot B_p(s)\|_F\le K_B$ on $[0,T]$, then

\[
 \left\|\int_0^t A_pB_p^\top ds-
  t^{-1}\sum_{j<q}U_jV_j^\top\right\|_F
 \le\frac{t^3 K_AK_B}{6q(q+1)}. \tag{4.5}
\]

Here is a derivation. The shifted Legendre equation is

\[
 -\frac d{du}\left(u(1-u)\ell_j'(u)\right)=j(j+1)\ell_j(u).
\]

Integration by parts, with zero boundary weight, shows that the weighted derivative energy of a polynomial expansion is the sum of (j(j+1)) times its squared coefficients. Approximation of an $H^1$ function by polynomials, or Bessel's inequality applied to the orthogonal derivatives, gives

\[
 \sum_{j\ge q}\|a_j\|_F^2
 \le\frac1{q(q+1)}\int_0^1u(1-u)\|a'(u)\|_F^2du.
\]

Apply this to $a(u)=A_p(tu)$, and then to $B_p(tu)$. Their right sides are at most $t^2K_A^2/[6q(q+1)]$ and its $B$ analogue. Multiply the square roots and the outer factor (t) from the integrated product to obtain (4.5). Only one time derivative of each source factor is needed. The $C_b^2$ activation assumption suffices on the parameter compact set; arbitrary high network derivatives are not being assumed.

## 5. Moving population frames and the connection term

The same exact memory mechanism applies to a moving orthonormal frame $e(t)=(e_1(t),\ldots,e_p(t))^\top\in L^2(\mu)^p$. Write

\[
 \dot e=\Omega_e e+\rho,\qquad
 (\Omega_e)_{ij}=\langle\dot e_i,e_j\rangle,
 \Omega_e^\top=-\Omega_e,\qquad \langle\rho_i,e_j\rangle=0.
\]

The cross coefficients are $A_e(t)=\mathbb E[a(t)e(t)^\top]$ and $B_e(t)=\mathbb E[b(t)e(t)^\top]$. Their derivatives, when they exist in $L^2$, are exactly

\[
 \dot A_e=\mathbb E[\dot a\,e^\top]+A_e\Omega_e^\top+
            \mathbb E[a\rho^\top],
\]

and the corresponding equation for $B_e$. Normal frame motion cannot be discarded from these instantaneous coefficient derivatives.

For memory, let $Q(t,s)$ solve

\[
 \partial_t Q(t,s)=\Omega_e(t)Q(t,s),\qquad Q(s,s)=I_p.
\]

It is orthogonal. Replace (4.1) by the covariant moments

\[
 U_j(t)=\int_0^t A_e(s)Q(t,s)^\top\ell_j(s/t)ds,
 \quad V_j(t)=\int_0^t B_e(s)Q(t,s)^\top\ell_j(s/t)ds.
\]

The exact moment equations are

\[
 \dot U_j=\ell_j(1)A_e+U_j\Omega_e^\top
          -t^{-1}\sum_{k\le j}D_{jk}U_k,
\]

and similarly for $V_j$. Orthogonality cancels the two transports inside the product, so (4.2) still equals $\int_0^t A_e(s)B_e(s)^\top ds$. The connection costs $O(p^2)$ state, not a functional history. Normal movement changes the newly injected source; the moment construction does not falsely reinterpret every old projector as the present projector.

For (4.5) in this gauge, replace ordinary derivatives by the covariant derivatives $\dot A_e-A_e\Omega_e^\top$ and $\dot B_e-B_e\Omega_e^\top$. Differentiating the transported past factors with respect to the past time gives precisely these derivatives times the orthogonal transport.

This is the requested exact moving-basis transport formula. The smooth sketch (3.1) is preferable for an unconditional implementation because it avoids choosing an orthonormal population frame altogether.

## 6. Finite-horizon comparison theorem

Fix a compact parameter ball containing the exact path and an open neighborhood of it. Fix the sketches, $p,q,\lambda>0$. Suppose on this ball that every factor map in (3.1) is bounded by $M_A,M_B$ and Lipschitz with constants $K_A^{\rm par},K_B^{\rm par}$; include the exact $W_1,w$ vector fields in the same finite bound. Let $\varepsilon_\mu$ be the numerical integration contribution specified below. Define

\[
 \varepsilon_{\rm pop}=\sup_{t\le T}\left\|\int_0^t(G-S_{p,\lambda})(\theta(s))ds\right\|,
\]

and let $\varepsilon_{\rm time}$ be the aggregate bound (4.5) computed **along the exact trajectory**, with the actual smooth source factors (3.1). Then there is a finite constant $C$, depending on the displayed local bounds and number of layers but not on $q$, such that, as long as the surrogate remains in that ball,

\[
 \sup_{t\le T}\|\widehat\theta(t)-\theta(t)\|
 \le\sqrt2\,e^{C^2T^2}
  (\varepsilon_{\rm pop}+\varepsilon_{\rm time}+\varepsilon_\mu). \tag{6.1}
\]

If this right side is smaller than the distance of the exact path to the boundary of the ball, continuation closes the hypothesis and proves existence and the estimate on all of $[0,T]$. The same parameter error controls $\|f_{\widehat\theta}-f_\theta\|_{L^2(\mu)}$ by the finite local Lipschitz constant of the network map.

To prove (6.1), view each $q$-memory reconstruction as

\[
 M_q[z](t)=\int_0^t (Q_{q,t}A_p(z))(s)
                    (Q_{q,t}B_p(z))(s)^\top ds,
\]

where $Q_{q,t}$ is orthogonal polynomial projection on ([0,t]). For two parameter paths (z,z'), its $L^2$ contraction property gives

\[
 \|M_q[z](t)-M_q[z'](t)\|_F
 \le (K_A^{\rm par}M_B+M_AK_B^{\rm par})\sqrt t
       \left(\int_0^t\|z(s)-z'(s)\|^2ds\right)^{1/2}.
\]

The exact-gradient blocks satisfy an estimate of the same form. Add the source and time-truncation defects evaluated on the exact path. Thus the state error (e(t)) satisfies

\[
 e(t)\le\varepsilon+C\sqrt t\left(\int_0^te(s)^2ds\right)^{1/2}.
\]

Squaring, using $t\le T$, and integrating the scalar inequality yields

\[
 e(t)^2\le2\varepsilon^2+2C^2T\int_0^te(s)^2ds
 \le2\varepsilon^2e^{2C^2Tt},
\]

which proves (6.1). This comparison avoids assuming a uniform-in-$q$ time-derivative bound for the surrogate itself. It uses time derivatives only along the fixed exact reference path.

For fixed $p,\lambda$, the same proof compared against the projected $q=\infty$ flow has zero population defect and proves $q\to\infty$ convergence on each finite horizon. That projected flow is well posed and dissipative as noted above. This is a valid hierarchy convergence statement. It does not identify a fixed $p,\lambda$ projected flow with the original gradient flow.

At $p=n$, an invertible square sketch permits the ridge trial $Z_0=\Omega^{-1}$, so $\|G-S_{n,\lambda}\|_F\le\sqrt\lambda\|\Omega^{-1}\|_F$, uniformly in $G$. Combining ordinary stability of the original vector field with this uniform forcing bound gives the iterated convergence: first $q\to\infty$ at fixed $n,p=n,\lambda$, then $\lambda\downarrow0$. This is an existence check at full source rank, not a subquadratic theorem.

## 7. Integration accuracy, physical time, and counted descriptions

Integration cannot disappear into the source oracle. Suppose the two current-state factor computations return errors at most $\eta_A,\eta_B$ in Frobenius norm, uniformly for states visited, and the first-layer/readout gradient integrator has error at most $\eta_0$ in the normalized metric (1.1). Orthogonal time projection gives a pathwise product-error contribution bounded by

\[
 \varepsilon_\mu\le T\eta_0+
    T\sum_{\ell=2}^L(M_{A,\ell}\eta_{B,\ell}
                   +M_{B,\ell}\eta_{A,\ell}
                   +\eta_{A,\ell}\eta_{B,\ell}). \tag{7.1}
\]

Errors in the raw products $G\Omega$ and $G^\top A_p$ propagate to these factor errors through the explicitly regularized $p\times p$ algebra. Conditioning worsens for small $\lambda$. A finite dataset can be summed exactly in a stream. For an infinite law, a requested integration tolerance or sampling budget must be stated separately. Single-call Monte Carlo concentration does not by itself establish the uniform adaptive-in-time bound required in (7.1). A proved uniform quadrature bound, a suitable controlled integration routine, or a stochastic-dynamics analysis is needed.

The integral definition gives startup in physical time $t=0$. No accelerated clock, fitted prefix, future trajectory, or burn-in from the exact trained network is used. With fixed positive $\lambda$, the source sketch is smaller than the true source near zero: generically $G(t)=O(t)$, while (3.1)--(3.2) give $S_{p,\lambda}(t)=O(t^3/\lambda)$. This early discrepancy is included in $\varepsilon_{\rm pop}$; it must not be claimed away. Taking small $\lambda$ shortens its scale while increasing numerical conditioning costs.

A numerical implementation can avoid evaluating (1/t) at zero by using the continuous moment startup or by deliberately suppressing hidden-layer learning on a specified short physical prefix $[0,t_0]$. In the latter option the readout and first layer still evolve using the current approximate network; start hidden moments at $t_0$ using interval length $t-t_0$. The extra omitted-source term must be added explicitly. Along the exact path it is at most $\int_0^{t_0}\|G(s)\|ds$, which is $O(t_0^2)$ here because $G(0)=0$ and the source is differentiable. This is an approximation with a declared prefix error, not exact initialization from an inaccessible path.

The only functional descriptions are the known architecture and activation, the supplied data/target integration interface, fixed $W_0$, fixed $\Omega$, and finite current coefficient arrays. The source atoms are evaluated from these arrays, not retained as arbitrary functions. Moment reconstruction, source products, and backward evaluation require no dense learned hidden matrix. The storage claim includes transient $np$ products and $p^2$ algebra for $p\le n$, and the fully evolved first layer $nd$. It excludes neither the fixed initialization's dense storage nor the data interface's input storage from a claim about total system resources; those resources are simply distinct from evolving learned state.

## 8. A target-regularity obstruction, with exact network construction

Smooth or constant $f_*$ alone does not force low relative interaction rank. Here is a concrete $L=2,d=n$ example in the exact assigned architecture. Select a fixed bounded smooth activation with

\[
 \phi(0)=\phi(1)=\phi(3)=1,\quad \phi(2)=0,
 \qquad \phi'(0)=0,\quad\phi'(1)=1.
\]

Such an activation is obtained by finitely many smooth compactly supported interpolation bumps around (0,1,2,3), with disjoint supports. Let $\mu$ be uniform on $x_j=e_j$, let $f_*(x)=1$, choose $W_{1,0}$ with diagonal entries $3\sqrt n$ and off-diagonal entries $2\sqrt n$, and put $W_{2,0}=I_n$. Then

\[
 h_1(x_j)=e_j,\quad h_2(x_j)=\mathbf1,
 \quad\dot w(0)=2\mathbf1,
 \quad\dot\delta_2(0,x_j)=2e_j.
\]

Because $w(0)=0$, both hidden weights have zero first derivative initially. Differentiating their source, all terms containing $\delta_2(0)$ vanish, and

\[
 \dot G_2(0)=\frac2n\mathbb E[\dot\delta_2(0,x)h_1(x)^\top]
           =\frac4{n^2}I_n. \tag{8.1}
\]

Consequently $G_2(t)=4tI_n/n^2+o(t)$ and

\[
 W_2(t)-W_{2,0}=\frac{2t^2}{n^2}I_n+o(t^2).
\]

The best rank-(r) approximation to a scalar multiple of $I_n$ has relative Frobenius error $\sqrt{1-r/n}$: the error is exactly the square root of the (n-r) discarded equal squared singular values divided by the norm of all $n$. Thus the construction's learned rank bound $r\le pq$ requires $pq$ proportional to $n$ for any fixed nontrivial relative Frobenius accuracy on this short-time example. Its evolving matrix storage then need not be subquadratic.

These displayed matrices are not a replacement initialization law. An iid nondegenerate Gaussian matrix has positive probability in every neighborhood of them; continuity of the initial source derivative gives the same approximate flat-spectrum obstruction on such a neighborhood. This disproves a deterministic/all-draw conclusion from $f_*$ regularity alone. The event can be extremely rare and the absolute source norm shrinks with $n$. Accordingly this is **not** a high-probability typical-Gaussian obstruction, **not** an absolute-error lower bound uniform in $n$, and **not** a lower bound for scalar network-output accuracy. Smooth data densities can replace the atoms by narrow smooth bumps, preserving (8.1) approximately by continuity, if qualitative density smoothness without uniform derivative constants is desired.

The example identifies the missing assumption: an appropriate source spectral-tail or nuclear-mass bound with the right width normalization and stability constants, or a weaker output metric together with a proved error-observability estimate. Merely labeling the target function regular leaves these points unresolved.

## 9. Claim ledger and remaining bottleneck

| Claim | Status | Necessary qualification |
|---|---|---|
| Cross-population projector identity and $p^{-1/2}$ mass bound | Proved | Frobenius source metric; finite factor energies |
| Smooth source sketch without a spectral gap | Proved | Fixed $\lambda>0$; two streamed population products |
| Randomized source error bound | Proved | Extra sketch independent of the exact trajectory |
| Exact polynomial memory and moving-frame transport | Proved | Square-integrable factors; derivatives only for the ODE/rate |
| Autonomous (O(Lnpq+nd)) evolving state | Proved for the construction | Initialization and integration input are retained; runtime is separate |
| Fixed-$p,\lambda$, $q\to\infty$ finite-horizon convergence | Proved by local stability and continuation | Converges to the projected flow |
| Original-flow comparison | Conditional theorem (6.1) | Small measured/bounded source tail and integration error; finite stability constants |
| Efficient $p,q$ from $f_*$ regularity alone | Unsupported; deterministic relative-rank version obstructed | Requires source geometry and width-uniform estimates |
| Subquadratic matched output accuracy for typical Gaussian $W_0$ | Open | No output lower bound or matching upper rate was proved |

The leading research bottleneck is now concrete: prove, in the stated Gaussian network and a specified regular data class, a source-tail estimate and a stability estimate that together keep the required $pq=o(n)$ at the same declared observable accuracy. The exact time-memory construction and the spectral-gap-free source factorization remove hidden-history and hidden-dense-driver objections, but they do not supply that statistical theorem.

## 10. Post-freeze refinements and supervisor-supplied geometry lemma

Sections 1--9 were first frozen independently. After that freeze, the supervisor supplied the quantization-to-source-tail argument verified below. Its provenance is therefore distinct from the independent route. The prefix-sum refinement is an independent algebraic correction found after that freeze; the main text now uses its stronger cost bound.

### Exact prefix-sum evaluation of the moment connection

The diagonal coefficient is $D_{jj}=j$, by comparing highest-degree coefficients of $u\ell_j'$ and $\ell_j$. For (k<j), integration by parts gives

\[
 D_{jk}=\int_0^1u\ell_j'(u)\ell_k(u)du
       =\ell_j(1)\ell_k(1)
        -\int_0^1\ell_j(u)[\ell_k(u)+u\ell_k'(u)]du
       =\sqrt{(2j+1)(2k+1)},
\]

because the remaining integrand pairs $\ell_j$ with a polynomial of degree at most (k<j). Therefore

\[
 \sum_{k\le j}D_{jk}U_k
 =jU_j+\sqrt{2j+1}\sum_{k<j}\sqrt{2k+1}\,U_k.
\]

Maintain the final sum while increasing (j). This applies the entire connection to all $q$ matrix moments with (O(npq)) work and one $n\times p$ running sum. The same applies to $V$.

### Verified quantization-to-source spectral-tail lemma

Let $A,B:\mathcal H\to\mathbb R^n$ be the actual source factors of Section 2, so that the factor (-2) is already included in (a). Assume

\[
 \|A\|_{\mathrm{HS}}\le M_A,
 \qquad \|b(x)-b(y)\|\le L_b\|x-y\|.
\]

For the input law define its $k$-point squared quantization distortion

\[
 Q_k(\mu)=\inf_{c_1,\ldots,c_k}
    \mathbb E\min_{1\le i\le k}\|x-c_i\|^2.
\]

Use nearest-center cells and let $\Pi_k$ be conditional expectation onto functions constant on those cells. This is an orthogonal projector of rank at most $k$, including when some cells have zero mass. Conditional means minimize squared error, hence for any selected centers

\[
 \|B(I-\Pi_k)\|_{\mathrm{HS}}^2
  =\mathbb E\|b-\mathbb E[b\mid\text{cell}]\|^2
  \le L_b^2\mathbb E\min_i\|x-c_i\|^2.
\]

Split the source as

\[
 G=A\Pi_kB^*+A(I-\Pi_k)B^*.
\]

The first term has rank at most $k$. The remainder $E_k$ has nuclear norm at most

\[
 \|E_k\|_*\le\|A\|_{\mathrm{HS}}\|B(I-\Pi_k)\|_{\mathrm{HS}}
             \le M_AL_b\sqrt{Q_k+o(1)}.
\]

To justify the product inequality, choose an orthonormal basis in the common Hilbert domain and write the product as a sum of outer products; sum their nuclear norms and use Cauchy--Schwarz. Approximating $E_k$ by its rank-$k$ singular truncation and adding the rank-$k$ first term yields a rank-(2k) approximation. Equation (2.2), applied to $E_k$, proves after taking the infimum over centers

\[
 \boxed{\tau_{2k}(G)^2\le\frac{M_A^2L_b^2Q_k(\mu)}{k+1}.} \tag{10.1}
\]

The source sign and constant must be counted consistently: if instead one defines $a=r\delta/\sqrt n$, then $G=-2AB^*$, and the right side for $G$ has an additional factor (4).

The same argument can use distortion in any supplied input metric for which (b) has the stated Lipschitz bound. Quantization is a proof device; the algorithm stores no cells, centers, partition functions, or polynomial input basis.

For example, assume explicitly

\[
 Q_k(\mu)\le D^2 k^{-2/s}
\]

with constants (D,s) independent of width and data cardinality. This is a substantive condition on the data geometry, not a consequence of target smoothness. Then

\[
 \tau_{2k}(G)\le M_AL_bD\,k^{-1/s}(k+1)^{-1/2}.
\]

Thus the source singular-tail exponent is (1/2+1/s), even though no backward-field spatial derivative was assumed. The only backward requirement here is the Hilbert--Schmidt energy bound $M_A$.

### Direct specialization of the smooth sketch

Choose the target rank in (3.4) to be (2k), and the actual Gaussian sketch width to be $p=4k+2\le n$. Then

\[
 \mathbb E_\Omega\|G-S_{p,\lambda}\|_F^2
 \le\frac{2M_A^2L_b^2Q_k(\mu)}{k+1}+\lambda
 \le 2M_A^2L_b^2D^2 k^{-2/s}(k+1)^{-1}+\lambda. \tag{10.2}
\]

This source bound plugs directly into (3.7) and (6.1). Its source approximation exponent is stronger than the generic nuclear-mass estimate.

For the network's normalized forward field $b=h_{\ell-1}/\sqrt n$, a sufficient explicit Lipschitz bound is

\[
 L_b\le
  \frac{\|\phi'\|_\infty^{\ell-1}\|W_1\|_{\mathrm{op}}}{\sqrt{nd}}
  \prod_{j=2}^{\ell-1}\|W_j\|_{\mathrm{op}}. \tag{10.3}
\]

This follows directly by composing the layerwise Lipschitz inequalities. Put $V_T=\sqrt{T\mathcal E(0)}$. The normalized energy estimate gives $\|W_1(t)-W_{1,0}\|_{\mathrm{op}}/\sqrt n\le V_T$, $\|w(t)\|/\sqrt n\le V_T$, and $\|W_\ell(t)-W_{\ell,0}\|_{\mathrm{op}}\le V_T$ for $\ell\ge2$. To claim width-independent constants, the initial Gaussian scaling must actually give bounded hidden-layer operator norms and bounded $\|W_{1,0}\|_{\mathrm{op}}/\sqrt n$. The original scoped prompt's phrase “iid Gaussian” without its variance does not alone establish that normalization. This route does not replace or rescale the specified initialization.

Finally, (10.2) alone does not give a trajectory rate $p^{-1/2-1/s}+q^{-2}$ with width-independent constants. For example, choosing $\lambda$ as small as the spectral-tail term also changes the factor derivatives in (4.5) and the stability constant in (6.1). Their joint dependence must be controlled before concluding $pq=o(n)$ at matched trajectory or output accuracy. The geometry lemma closes a meaningful source-production gap; it leaves the quantitative propagation and memory-rate balance open.


## 11. Internal verification and minor corrections

INTERACTION_BASIS_CHECK.md checked all preceding sections at SHA256 adad55396cacb7e7d300701a0c23c48aa74ae33e6a6e07defdb00427c16878f6. It found no substantive mathematical defect in the fixed-width construction or conditional comparison. The present revision adds its positive-singular-value qualification to the optional population frame and fixes four math delimiters. For arbitrary square-integrable source histories the moment differential identities hold almost everywhere; they hold classically for the continuous factor histories of the actual construction. This internal check does not establish width/regularization-uniform tracking or a universal population integration algorithm, and is not a promotion review.
