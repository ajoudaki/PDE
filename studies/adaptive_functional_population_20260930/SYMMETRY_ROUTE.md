# Symmetry and task quotients for deep feature-learning populations

**Status:** independent prompt-only theoretical analysis, 2026-09-30. These are study results, not promoted theory. No experiments, external sources, or other studies were used.

The strongest positive statement is exact: for a rotationally invariant population task with a $k$-dimensional teacher, a deterministic equivariant limiting predictor depends on $k$ teacher coordinates and one transverse radius. On a fixed-radius sphere the radius is determined, leaving $k$ coordinates. This does **not** close the evolving deep population. Two-input statistics retain a transverse angle, higher response moments retain transverse Gram matrices, and backward propagation retains correlations with the same initialized matrices used forward.

An exact finite-width calculation makes the distinction concrete. The Gaussian population risk and its gradient flow admit a quotient using first-layer teacher projections and a neuron-by-neuron transverse Gram matrix. This removes the explicit input coordinate frame, but the Gram state grows with width and remains a kernel in a continuum population description. It is a useful structural reduction, not yet the requested efficient autonomous functional encoding.

## 1. Contract and assumptions

Let $U\in\mathbb R^{d\times k}$ have orthonormal columns, let $q=d-k\geq1$, and write

\[
x=Uz+Vv,\qquad z=U^Tx,\quad v=V^Tx,\quad r=\|v\|,
\]

where $V\in\mathbb R^{d\times q}$ completes $U$ to an orthogonal matrix. The data law is either $x\sim N(0,I_d)$ or the uniform law on a fixed-radius sphere, and $y=g(z)$. The supplied architecture is

\[
h^1=\phi(W^1x/\sqrt d),\qquad
h^\ell=\phi(W^\ell h^{\ell-1}),\qquad
f_\theta(x)=n^{-1}w^Th^L(x).
\]

All weights follow squared-loss gradient flow, with positive layer learning rates. These rates may depend on width. The displayed architecture alone does not specify their scaling; the arguments below hold at finite width for every such choice. They do not prove that any unspecified scaling has a nontrivial feature-learning limit.

The limiting-predictor result assumes that the canonical IID Gaussian initialization and the equivariant finite-width dynamics have a deterministic limit in a trajectory space such as $C([0,T];L^2(P_x))$, with sufficient uniqueness to identify the rotated construction with the same canonical limit. Zero or vanishing readout helps make the initial predictor deterministic but is not itself a proof of deterministic evolution, limit existence, or feature movement.

The goal is an autonomous, restartable state whose coefficients come from initialization and the task, whose error controls the evolving predictor on a fixed finite horizon, and whose effective complexity avoids ambient input dimension $d$ and empirical sample count $m$. A function-valued coordinate, Gaussian process, arbitrary population kernel, or unbounded response hierarchy is not counted as a finite efficient state merely because it has a short name.

The teacher subspace $U$ is assumed known for statements about a constructive quotient algorithm. Existence of a latent subspace is weaker than computational access to it. Reading $U$, reading $m$ arbitrary $d$-dimensional samples, or projecting them has its ordinary input cost; symmetry does not remove that cost.

## 2. Exact predictor quotient

For $Q\in O(q)$, define $R_Q=UU^T+VQV^T$. This group fixes $z$, preserves the input law, and preserves the label. It acts on network parameters by

\[
W^1\mapsto W^1R_Q^T,
\]

with the other parameters unchanged. The transformed network satisfies

\[
f_{R_Q\cdot\theta}(x)=f_\theta(R_Q^Tx).
\]

The parameter transformation is an isometry for the Euclidean layer metrics, so the population loss is invariant and its gradient flow is equivariant. IID isotropic Gaussian first-layer initialization has an invariant law. Consequently a deterministic canonical limiting predictor satisfies, as an $L^2(P_x)$ trajectory,

\[
f_t(R_Qx)=f_t(x)\quad\text{for every }Q\in O(q).
\]

To see why determinism matters, the rotated finite-width construction has exactly the same law as the original construction; a deterministic limit therefore equals its rotated version. A random limit need only have a rotation-invariant law. An individual realization of a Gaussian field generally does not have invariant sample paths. Likewise, invariance of the finite-width ensemble mean does not establish invariance of a trained finite-width realization.

Two transverse vectors are in the same $O(q)$ orbit exactly when they have the same norm: an isometry between their one-dimensional spans extends to an orthogonal map. Therefore the invariant predictor has a measurable representative

\[
f_t(x)=F_t(z,r).
\]

For Gaussian inputs the quotient law is

\[
\overline P(dz,dr)=N(0,I_k)(dz)\,\chi_q(dr).
\]

For a sphere of radius $a$, $r^2=a^2-\|z\|^2$, so $f_t(x)=\widetilde F_t(z)$. There is no additional free radius on that support. For Gaussian inputs symmetry alone cannot remove $r$: the invariant function $\|V^Tx\|^2$ is a direct counterexample to that stronger inference.

The conclusion is exact for genuinely moving features. It uses the symmetry of the complete flow, not a frozen tangent kernel or a linearization. It does not say that the quotient function is smooth, cheap to evaluate, or determined by a finite collection of coefficients. Without a regularity class for $g$ and the reachable $F_t$, even a one-dimensional function class has no uniform finite approximation complexity.

## 3. Two-input kernels and higher moments

Suppose a scalar $p$-input population observable is deterministic and equivariant in the same sense. Examples include appropriately defined activation moments or scalar response kernels, provided their limits exist. Write its inputs as $x_i=Uz_i+Vv_i$. Its complete orbit data are

\[
(z_1,\ldots,z_p),\qquad G_{ij}=v_i^Tv_j.
\]

Indeed, equality of the two Gram matrices makes the map sending each $v_i$ to its counterpart a well-defined isometry of their spans; it extends to an element of $O(q)$. Conversely rotations preserve every listed quantity. The Gram matrix must be positive semidefinite with rank at most $q$.

When $q\geq p$, this gives $kp+p(p+1)/2$ continuous variables on the Gaussian input domain. On a fixed-radius sphere the $p$ diagonal Gram entries are determined by the $z_i$, leaving $kp+p(p-1)/2$ variables. When $p>q$, rank constraints reduce the dimension, but the Gram data are still required. Tensor-valued equivariant observables also need appropriate tensor directions; the scalar orbit statement must not be applied to their components as if they were invariant scalars.

In particular, an invariant two-input tangent kernel has the form

\[
K_t(x,x')=\kappa_t(z,r,z',r',c),\qquad
c=\frac{v^Tv'}{rr'},
\]

with the zero-radius cases interpreted by continuity or directly through the Gram entries. There are $2k+3$ variables for Gaussian inputs when $q\geq2$, and $2k+1$ on the sphere. The angle $c$ cannot be inferred from the individual input quotients $(z,r)$ and $(z',r')$.

At finite width the exact tangent kernel, including the layer learning rates, is

\[
K_\theta(x,x')=\sum_a\eta_a\,
\partial_{\theta_a}f_\theta(x)\,
\partial_{\theta_a}f_\theta(x').
\]

The exact predictor equation is

\[
\partial_t f_t(x)
=-\int K_t(x,x')\,[f_t(x')-g(z')]\,P_x(dx').
\]

Using this equation for a population limit additionally requires convergence and integrability sufficient to pass to the limit. Predictor determinism by itself does not prove a deterministic tangent-kernel limit. An averaged limiting kernel can be used when the limiting residual is deterministic and the requisite passage of expectations is justified. At finite width, one generally cannot replace $\mathbb E[K_t(f_t-y)]$ by $\mathbb E[K_t](\mathbb E[f_t]-y)$.

Conditioned on $(z',r')$, the transverse direction of $x'$ is uniform. Thus define

\[
\overline K_t(z,r;z',r')
=\mathbb E_{c\sim\nu_q}\kappa_t(z,r,z',r',c),
\]

where $\nu_q$ is the law of the first coordinate of a uniform point on $S^{q-1}$. For $q\geq2$ its density is proportional to $(1-c^2)^{(q-3)/2}$; for $q=1$ it assigns probability $1/2$ to each of $\{-1,1\}$. The quotient predictor equation becomes

\[
\partial_tF_t(z,r)
=-\int \overline K_t(z,r;z',r')
 [F_t(z',r')-g(z')]\,\overline P(dz',dr').
\]

This is an exact reduction of the integration domain under the stated limit assumptions. It is not an autonomous equation for $F_t$, because the evolving $\overline K_t$ is additional state.

There are two distinct closure obstructions:

1. **The predictor does not determine its kernel.** At zero readout, different hidden feature configurations all have predictor zero, but their readout contributions to $K_0$ differ. A fixed canonical initialization supplies its particular initial kernel, yet an autonomous equation or restart rule still needs the information controlling subsequent kernel evolution.
2. **Angular averaging does not commute with products.** For independent uniform transverse directions, $\mathbb E c=0$ and $\mathbb E c^2=1/q$. Thus two functions with zero angular average can have a product with nonzero angular average. Deep response equations contain products and contractions, so retaining only individually averaged fields can discard contributions to invariant observables. This identity disproves closure by angular averages alone; it does not prove that every richer finite closure fails.

Rotational symmetry therefore removes the input frame at each fixed response order, but it does not bound the necessary response order. The number of invariant variables grows quadratically in that order while $q\geq p$. Calling the resulting infinite hierarchy a fixed-dimensional functional encoding hides a separate complexity problem.

## 4. An exact all-weight Gaussian quotient at finite width

This calculation gives a concrete positive construction and identifies what it retains. Let the first layer have width $n$, set

\[
A=W^1U\in\mathbb R^{n\times k},\qquad
B=W^1V\in\mathbb R^{n\times q},\qquad
C=BB^T,
\]

and collect all later weights and the readout into $\Lambda$. Define

\[
\ell(A,\xi,\Lambda;z)
=\frac12\left[
f_{\Lambda}\!\left(\phi((Az+\xi)/\sqrt d)\right)-g(z)
\right]^2,
\]

where $f_\Lambda$ is the remaining network with its original readout normalization. For Gaussian inputs, $z\sim N(0,I_k)$ and $Bv\sim N(0,C)$ are independent. Hence the exact population risk is

\[
\Psi(A,C,\Lambda)
=\mathbb E_{z\sim N(0,I_k),\,\xi\sim N(0,C)}
\ell(A,\xi,\Lambda;z).
\]

Assume here sufficient twice differentiability and integrability to differentiate the risk and perform Gaussian integration by parts. These regularity hypotheses are additional for this calculation; the basic symmetry theorem did not need a smooth activation. Put

\[
H(A,C,\Lambda)=\mathbb E\,\nabla^2_\xi\ell(A,\xi,\Lambda;z).
\]

Writing $R(A,B,\Lambda)=\Psi(A,BB^T,\Lambda)$ for the risk in the original first-layer coordinates, we have

\[
\nabla_BR
=\mathbb E[\nabla_\xi\ell\,v^T]
=H B.
\]

For the second equality, componentwise Gaussian integration by parts gives

\[
\mathbb E[(\partial_{\xi_i}\ell)v_a]
=\mathbb E[\partial_{v_a}\partial_{\xi_i}\ell]
=\sum_j\mathbb E[\partial_{\xi_j}\partial_{\xi_i}\ell]B_{ja}.
\]

With first-layer rate $\eta_1$, the exact quotient dynamics are consequently

\[
\dot A=-\eta_1\nabla_A\Psi,\qquad
\dot C=-\eta_1(HC+CH),\qquad
\dot\Lambda_a=-\eta_a\partial_{\Lambda_a}\Psi.
\]

When $C$ is positive definite, $H=2\nabla_C\Psi$ with the symmetric-matrix inner product convention. The displayed equation remains meaningful at singular $C$ through the Gaussian expectation defining $H$, so this identity does not require assuming full rank.

This is autonomous and restartable for the parameter trajectory **modulo transverse input rotations**, the population risk, and other invariant parameter observables. All layers remain trainable, and the equations retain their exact gradients. It also shows precisely why a first-layer neuron generally cannot retain only its own transverse radius: $\dot B=-\eta_1HB$ mixes different rows of $B$, and $H$ need not be diagonal.

The retained state is not small in width. Besides later dense weight matrices, $C$ is an $n\times n$ Gram matrix. Its generic rank is $\min(n,q)$, and its rank-$r_0$ manifold has dimension $nr_0-r_0(r_0-1)/2$. For $q\geq n$, this is $n(n+1)/2$. For $n>q$, the global quotient has removed only the common transverse rotation, not the individual transverse degrees of freedom. A continuum-width version generally retains a two-neuron Gram kernel $C(\alpha,\beta)$ plus the later population structure.

The Gaussian integral has at most $k+n$ integration coordinates, rather than $d$, but evaluating it exactly is another unresolved computational problem as $n$ grows. Initializing $A,C$ from supplied finite matrices also has its ordinary matrix-operation cost. The parameter quotient determines a network only up to input rotation: it does not recover a particular finite-width realization's value at a prescribed $x$ without retaining its relative orientation to the query. The deterministic invariant limiting predictor is a separate result from Section 2.

As a simple diagnostic for discarded correlations, let two unit transverse weights have overlap $\rho=b_1^Tb_2$. For Gaussian $v$, writing $b_2^Tv=\rho Z+\sqrt{1-\rho^2}Z'$ with independent standard normals yields

\[
\mathbb E[(b_1^Tv)^2(b_2^Tv)^2]
=3\rho^2+(1-\rho^2)=1+2\rho^2.
\]

The individual radii do not determine even this basic nonlinear moment. Randomly applying a common global rotation makes these examples rotation-invariant in law without erasing their distinct overlap. This is a nonclosure example for marginal-radius descriptions, not a claim that both examples arise from the same canonical initialization.

## 5. Initialized matrices and exact transpose reuse survive the quotient

For any hidden matrix, write its exact finite-time decomposition as

\[
W_t=W_0+\int_0^t\dot W_s\,ds.
\]

Forward fields contain $W_0h_t$, backward fields contain $W_0^T\delta_t$, and the learned $h_t,\delta_t$ depend on this same $W_0$. Input-space symmetry neither removes that dependence nor replaces the transpose by an independent matrix. The elementwise nonlinearity also prevents treating arbitrary hidden-channel rotations as a symmetry of the network.

A direct algebraic diagnostic is a square IID Gaussian matrix $W_0$ with variance $1/n$ entries and a deterministic vector $u$:

\[
h=W_0^Tu
\quad\Longrightarrow\quad
\mathbb E[W_0h]=\mathbb E[W_0W_0^T]u=u.
\]

Replacing the forward matrix by an independent centered copy $\widetilde W_0$ gives $\mathbb E[\widetilde W_0h]=0$. This diagnostic is not asserted to be a particular reachable network state; it shows why Gaussian initialization and isotropy alone cannot license independence in a transpose-reuse contraction.

An exact functional population proposal must preserve the joint initialization and its induced response dependencies, or derive and retain sufficient response variables. Orbit reduction can simplify the input arguments of those variables. It does not supply the missing response identities or a finite memory bound.

## 6. Finite samples generically destroy the task symmetry

For empirical gradient flow, the objective uses the realized sample, not the isotropic population law. Let $v_a=V^Tx_a$ and let $s=\dim\operatorname{span}\{v_1,\ldots,v_m\}$. The subgroup of teacher-preserving rotations that fixes every sample point is $O(q-s)$, acting on the orthogonal complement of that span. For Gaussian samples, $s=\min(m,q)$ almost surely.

If the canonical predictor at this fixed dataset also has a deterministic equivariant width limit, this smaller stabilizer is what the symmetry argument provides. Its quotient may depend on $z$, all $s$ nuisance coordinates in the sample span, and one remaining radius when $s<q$. On a fixed-radius sphere that final radius is determined. In particular, for $m\leq q$, the number of free Gaussian quotient variables is $k+m+1$ when $m<q$, rather than $k+1$. Once $s=q$, this subgroup is trivial. Using the full stabilizer of the sample in $O(d)$ gives an alternative quotient by its complete sample span; neither construction generally removes dependence on $m$.

This is a statement about the realized empirical objective. Averaging the predictor over independently resampled datasets restores a symmetry in law, but produces a different observable. Replacing each sample by its full rotation orbit also changes the empirical objective. Neither operation establishes a compact closure for the original trained predictor.

Population integration can genuinely avoid storing $m$ if the population distribution, teacher subspace, and teacher function are available as the problem inputs. A theorem for that setting must not be presented as a theorem for arbitrary empirical training sets.

## 7. Approximate symmetry: a conditional finite-time guarantee

The appropriate perturbation metric measures the change in the **training force**, rather than merely the change in labels or a convenient input covariance. The following lemma isolates a sufficient condition.

Let $u_t$ be a state in a Banach space with an isometric group action, let the baseline initialization $u_0^0$ be invariant, and assume unique equivariant baseline dynamics

\[
\dot u^0=\mathcal V_{\mu_0}(u^0).
\]

Let $\dot u=\mathcal V_\mu(u)$ be the perturbed dynamics. On a specified invariant admissible region $\mathcal A_T$ containing both trajectories, assume

\[
\|\mathcal V_\mu(u)-\mathcal V_\mu(v)\|
\leq L_T\|u-v\|,
\]

\[
\Delta_T(\mu,\mu_0)
:=\sup_{u\in\mathcal A_T}
\|\mathcal V_\mu(u)-\mathcal V_{\mu_0}(u)\|
\leq\delta,
\qquad \|u_0-u_0^0\|\leq\epsilon_0.
\]

The region and its constants must be specified from admissible inputs and a priori bounds; selecting them from the unknown future trajectory would not give a constructive uniform guarantee. Integrating the difference equation gives

\[
D(t)\leq\epsilon_0+\int_0^t[L_TD(s)+\delta]ds,
\]

and comparison with the scalar solution of $a'=L_Ta+\delta$ yields

\[
\|u_t-u_t^0\|
\leq e^{L_Tt}\epsilon_0
+\delta\frac{e^{L_Tt}-1}{L_T}
=:a(t),
\]

with the quotient interpreted as $t$ when $L_T=0$.

If the predictor observation map is equivariant and $B_T$-Lipschitz into $L^2(\mu_{0,x})$, then

\[
\|f_t-f_t^0\|_{L^2(\mu_{0,x})}\leq B_Ta(t).
\]

Let $P_Gf=\int f\circ R\,dR$ be Haar averaging over the baseline compact symmetry group. The invariant input measure makes $P_G$ the orthogonal projection onto invariant functions: each rotation is unitary, averaging fixes exactly the invariant functions, and averaging twice equals averaging once. Since $f_t^0$ is invariant,

\[
\|f_t-P_Gf_t\|_{L^2(\mu_{0,x})}
\leq B_Ta(t),
\qquad
\sup_R\|f_t-f_t\circ R\|_{L^2(\mu_{0,x})}
\leq2B_Ta(t).
\]

For gradient flows linear in the data measure,

\[
\mathcal V_\mu(u)=\int\psi(u;x,y)\,\mu(dx,dy),
\]

$\Delta_T$ is an integral probability pseudometric over the actual vector-valued force class. If these force functions are uniformly $C_T$-Lipschitz in data, any coupling of $\mu$ and $\mu_0$ gives $\Delta_T\leq C_TW_1(\mu,\mu_0)$: integrate the Lipschitz difference under the coupling, then take the infimum. The unbounded Gaussian input case requires appropriate integrability or a weighted variant; global bounded Lipschitz constants are not automatic.

A more directly useful example keeps $P_x$ fixed and changes the teacher to $g(z)+e(x)$. In learning-rate-whitened parameter coordinates for squared loss,

\[
\mathcal V_\mu(u)-\mathcal V_{\mu_0}(u)
=\mathbb E[e(x)J_u(x)],
\]

where $J_u(x)$ is the parameter derivative of the predictor in those coordinates. Cauchy--Schwarz gives

\[
\delta\leq\|e\|_{L^2(P_x)}
\sup_{u\in\mathcal A_T}
\left(\mathbb E\|J_u(x)\|^2\right)^{1/2}.
\]

This bound controls symmetry breaking for a finite horizon when the displayed constants are finite and uniform. Establishing these conditions for the canonical deep population state is a separate obligation. The lemma is a propagation estimate; it does not prove that the empirical force error is small independently of $d,m$, or that finite functional truncations produce a small force residual. In particular, an empirical-measure Wasserstein estimate can carry a severe ambient-dimensional cost.

## 8. What an actual efficient algorithm would still require

The exact predictor quotient removes the combinatorial input-coordinate factor from approximating an already known invariant function. It does not by itself produce that function. A constructive finite-horizon algorithm would need all of the following:

1. An autonomous closed state on finitely many invariant domains, with a justified maximum response order or another controlled memory representation.
2. Initialization and coefficients computable from the canonical IID law and the task, while retaining initialized-matrix correlations and exact transposes.
3. Reachable-state regularity and tail estimates on those domains, uniform in the ambient scales the algorithm is meant to avoid.
4. A source bound for discarded modes or responses, followed by a stability bound such as Section 7.
5. A stated data model: population access, or an empirical force approximation with its own justified sample and dimension dependence.

If a closed hierarchy of maximal order $p_*$ and uniformly regular invariant coefficient functions were proved, its largest generic Gaussian input domain would have at most

\[
D_*=kp_*+p_*(p_*+1)/2
\]

variables when $q\geq p_*$. On a bounded domain, a tensor grid of spacing $h$ would then use $O(h^{-D_*})$ values per scalar coefficient; a uniform Lipschitz estimate would control interpolation error by a constant times $h$. This is a conditional complexity accounting, not a proved algorithm. Neither a finite $p_*$, its closure equations, nor the necessary uniform regularity has been established here. Additional time or neuron-label variables must also be counted if the proposed state uses them.

There is a modest large-$q$ estimate for a *known* angular kernel. Since $\mathbb E c=0$ and $\mathbb E c^2=1/q$,

\[
|\mathbb E\kappa(c)-\kappa(0)|
\leq\operatorname{Lip}(\kappa)/\sqrt q,
\]

and, if $\sup|\kappa''|\leq M$, Taylor's formula improves this to $M/(2q)$. These estimates do not assume orthogonal data. But the derivatives of the evolving kernel may depend on $q$, radii, normalization, and training time. Replacing angular dependence by its value at zero without uniform derivative and dynamical source bounds remains unjustified, and supplies no response closure by itself.

## 9. Claim ledger and decisive bottleneck

| Claim | Status | Necessary qualification |
|---|---|---|
| Deterministic population predictor has $k+1$ Gaussian quotient variables, or $k$ on a sphere | Exact under the stated limit and equivariance assumptions | Does not establish the limit, regularity, or an algorithm |
| Fixed-order invariant scalar responses reduce to teacher coordinates and transverse Gram entries | Exact orbit classification | Their number of variables grows with order; tensor observables need tensor directions |
| Angular averaging gives the reduced predictor equation | Exact under justified kernel/predictor limiting operations | Its evolving averaged kernel is additional state |
| Gaussian finite-width all-weight GF has an autonomous $(A,C,\Lambda)$ quotient | Exact under stated differentiability and integrability | Controls the parameter orbit and invariant observables; state and quadrature grow with width |
| Per-neuron transverse radii or individual angular averages suffice for deep closure | Disproved as a general inference from symmetry | Pair-overlap and product counterexamples invalidate those particular representations |
| Initialized forward and transpose fields become independent after quotienting | Unsupported; the inference from isotropy is invalid | Exact initialized-matrix reuse must be retained |
| Teacher symmetry yields the same low-dimensional quotient for a realized empirical dataset | False in general | Generic samples introduce their nuisance span into the stabilizer quotient |
| Small force perturbations give small finite-time symmetry breaking | Conditional stability theorem proved above | Requires uniform state, force, and observation estimates |
| A finite autonomous deep population encoding efficient in $d$ and $m$ follows | Open | Symmetry alone supplies no response-order or function-complexity bound |

The highest-leverage next proof obligation is a **mechanism-preserving response closure or compressibility theorem on the invariant domains**, with coefficients derived from the shared initialized fields. A candidate must show why omitted angular/response information has small forcing on the retained variables, not merely observe that the final predictor is invariant. This route offers a rigorous reduction in input geometry; the unclosed deep response structure is the remaining central obstacle.
