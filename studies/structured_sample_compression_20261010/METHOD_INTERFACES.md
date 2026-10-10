# Sample compression at the three construction interfaces

This scoped analysis asks whether retained complexity can remain bounded as the training count $m$ grows, at a prescribed accuracy, when labels and input or pair geometry are simple. The answer is conditional: the sources identify useful places to compress the sample axis, but none of the three stated theorems permits replacing $m$ by an effective count without changing its construction and proof. Harmonic already shares most analytic coefficients across samples. Its remaining sample dependence is the exact fitting/readout interface.

Scientific inputs were only the complete current files `paper/compact.tex`, `paper/compact_legendre.tex`, `paper/compact_selected.tex`, and `paper/methods.tex`. All construction, statement, proof, and explanatory sections in those four files were read. References to the fitting/source lemmas in other files are treated as imported assumptions at the interfaces; their proofs were outside this assignment and were not read. No other study, archived book, external source, experiment, or code was consulted. The derived identities below are supplied with arguments; proposed trajectory extensions remain unproved. This is a study note, not a promotion or independent review.

## Scope and normalization

For normalized inputs $v_a=x_a/\sqrt d\in S^{d-1}$, the dense network is

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=\frac{w^\top h_a^{(L)}}n.
\]

The residual is $r_a=f_a-y_a$, the loss is $m^{-1}\sum_a r_a^2$, and the block mobilities are $(n,1,\ldots,1,n)$. The residual-free backward responses satisfy

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Consequently hidden updates are

\[
\dot W^{(\ell)}=-\frac2{nm}\sum_a r_a\delta_a^{(\ell)}
h_a^{(\ell-1)\top},\qquad 2\le\ell\le L,
\]

with corresponding factors $-2/m$ in the first-layer and readout updates. Sample compression must preserve these averaged forces and their feedback through the moving features.

The paper fixes $m,d,L$, the data, and the positive label scale separately as $n\to\infty$. Its accuracy is uniform over all physical times, including the fitted endpoint. Legendre and Harmonic cover the whole sphere; Taylor covers only an $(m+p)$-point panel declared before initialization. Neither its eventual width thresholds nor its comparison constants constitute a uniform growing-$m$ theorem.

Here an $m$-independent claim should mean that, for fixed accuracy, width or width tolerance, structural regularity bounds, and the declared time/query domain, both moving and fixed retained real-coordinate counts are bounded independently of $m$. It may permit reading the original data during initialization and then discarding them. Counting only a reduced moving vector while keeping the full dataset, a sample basis matrix, or a full Gram does not meet that interpretation. The paper does not assert bounded initialization time, initialization scratch, coordinate precision, or bit complexity.

## What the current constructions retain

| Method | Explicit sample dependence | What already has a shared representation |
|---|---|---|
| Legendre | Two $n$-vectors for each sample, hidden interface, and time mode: $2(L-1)mnq$ moving coordinates; labels and inputs are additional; evaluating the clock and writes visits all samples. | A common time basis and common clock. Original-width neurons and $(L-1)n^2$ fixed initialized mixers remain. |
| Harmonic | Exact initialized training features and forward images add at most $2m$ source vectors per layer; selected runtime retains $m$ deficits, sample features/responses, $V_C$, full sample Grams and inverse/factorization, and data. | Four joint time–sphere source families use one coefficient set for all inputs, including passive backward queries. No analytic coefficient list per training input is needed. |
| Taylor | Exact additions as above, plus up to $2(2m+p)$ source curves per layer, each with $J(K+1)$ temporal coefficients; runtime training storage is the same as Harmonic. | Temporal basis construction and selected dynamics are shared, but source coefficients are still indexed by the declared inputs. |

The exact Legendre inventory is

\[
S_{\rm moving}=n(d+1)+1+2(L-1)mnq,\qquad
S_{\rm fixed}=(L-1)n^2,
\]

excluding data. Its chosen order contains $(m/\gamma)^3$, in addition to the explicit $m$ moment factor. A lower temporal order alone does not eliminate this sample factor.

In the selected transfer proposition, $q$ bounds source-space dimension and satisfies $q\ge\max(m,d)$. The selected widths are at most $9q$. The retained inventory includes first matrices $O(qd)$, metrics and mixers $O(Lq^2)$, training feature/response arrays $O(Lmq)$, sample matrices $O(m^2)$, deficits $O(m)$, and inputs/labels $O(m(d+1))$. The $O(q^2)$ presentation absorbs these terms using $m,d\le q$; it does not remove them.

The source-rank bounds are

\[
R_{\rm Harm}=2m+d+1+4N\quad(d\ge2),
\]

where $N$ is the joint time–sphere coefficient count, and

\[
R_{\rm Taylor}=2m+k+1+2(2m+p)J(K+1),\qquad
k\le\min(d,m+p),
\]

after the exact input-span reduction. Low linear input rank reduces $d$ to $k$ on the panel; it does not reduce $m+p$, the training deficit count, or the full feature-Gram dimension.

These facts occur in `compact_legendre.tex`, equations `cp:eq-legendre-reconstruction`–`cp:eq-legendre-count`; `compact_selected.tex`, proposition `cp:selected` and its “Retained inventory” paragraph; and the proofs of `cp:harmonic` and `cp:panel`.

## Why the full readout inverse is structural

At the selected top layer, let $V_C\in\mathbb R^{q_L\times m}$ have columns $h_{C,a}^{(L)}/\sqrt m$. Its adjoint is $V_C^*=V_C^\top M_L$, with $M_L\succ0$, and $Q_C=V_C^*V_C$. The moving deficit $c_C\in\mathbb R^m$ and corrected readout are related by

\[
\widehat w_C=w_C+V_CQ_C^{-1}
\left(\frac{y-c_C}{\sqrt m}-V_C^*w_C\right).
\]

Multiplication by $V_C^*$ proves $f_C(x_a)=y_a-c_{C,a}$ for every sample. Thus the correction requires all $m$ training constraints simultaneously. Since

\[
\operatorname{rank}Q_C=\operatorname{rank}V_C\le q_L,
\]

invertibility entails $q_L\ge m$. Moreover, preserving the entire initialized dense training Gram, which is positive definite on the theorem event, forces the exact initialized top features to span at least $m$ dimensions. This explains the exact sample-sized source additions independently of their upper-bound count.

The inverse also supplies the comparison cancellation. If $e=(c_C-c_n)/\sqrt m$, where $c_n=y-f_n$, and $T_C=V_CQ_C^{-1}$, the raw readout error has a forcing $2V_Ce$, while the lifted deficit has $-2T_CQ_Ce=-2V_Ce$. Dropping the condition $q\ge m$, or replacing the inverse by a pseudoinverse, does not preserve the stated fitting and comparison proof. With a pseudoinverse, $Q_CQ_C^+$ is only a projection; the required output vector must lie in its range, and the full-gap and full-deficit estimates are lost. A ridge inverse likewise changes the exact constraint and introduces a bias term. These are possible new models, not instances already covered by `cp:selected`.

## The full-gap condition cannot be uniform in the sample count

The population feature Gram is defined recursively by $Q^{(0)}_{ab}=v_a^\top v_b$ and Gaussian feature expectations. Because all $v_a$ have unit norm, each diagonal entry of $Q^{(L)}$ is the same activation/depth-dependent number, say $\mu_{2,L}>0$. Define

\[
\gamma=\lambda_{\min}(Q^{(L)}),\qquad
\lambda=\frac\gamma m,\qquad
Y=\frac{\|y\|_2}{\sqrt m}.
\]

The trace bound gives the exact inequalities

\[
\gamma\le\frac{\operatorname{tr}Q^{(L)}}m=\mu_{2,L},
\qquad
\lambda\le\frac{\mu_{2,L}}m.
\]

Therefore the paper's sufficient label condition

\[
0<Y\le\lambda\beta^{-30L}
\]

forces $Y\to0$ as $m\to\infty$. One cannot assume a fixed positive lower bound for the normalized full gap while keeping bounded feature variance and increasing the number of samples.

Low-dimensional compact geometry can additionally shrink the unnormalized gap. Put $s_\ell=\sup_{z\in\mathbb R}|\phi_\ell'(z)|$. For $a\ne b$, let $e_a,e_b$ be standard coordinate vectors in $\mathbb R^m$. The Rayleigh quotient of $(e_a-e_b)/\sqrt2$, followed by the Lipschitz bound at each Gaussian layer, yields

\[
\begin{aligned}
\gamma
&\le\frac12\big(Q^{(L)}_{aa}+Q^{(L)}_{bb}-2Q^{(L)}_{ab}\big)\\
&\le\frac12\left(\prod_{\ell=1}^Ls_\ell^2\right)
\|v_a-v_b\|_2^2.
\end{aligned}
\]

Indeed the parenthesis is the expectation of the squared difference of the two top features; applying $|\phi_\ell(u)-\phi_\ell(v)|\le s_\ell|u-v|$ reduces it one layer at a time to $Q^{(0)}_{aa}+Q^{(0)}_{bb}-2Q^{(0)}_{ab}=\|v_a-v_b\|^2$. Any sequence of increasingly many distinct points in a fixed compact input set has pairs with distance tending to zero. Exact duplicates already make $\gamma=0$.

This matters for non-vacuity. Under the imported fitting event, the dense bounds used in `compact_selected.tex` give $\|w\|/\sqrt n\le2Y/\sqrt\lambda$ and a uniform feature-RMS bound depending only on activation and depth. Thus the label cap itself implies a whole-sphere output bound of order $m^{-1/2}$. A fixed *absolute* tolerance can eventually be met by a zero predictor along that shrinking-label family. That does not resolve a nonvanishing-signal sample-compression question. A meaningful extension should retain a nontrivial label/output scale or specify an error relative to that scale, and replace the full-gap assumption by an appropriate effective stability condition.

## Modification 1: weighted representatives before source construction

Write the empirical training measure as

\[
\mu_m=\frac1m\sum_{a=1}^m\delta_{(v_a,y_a)}.
\]

Replace it by $\nu_s=\sum_{j=1}^s\omega_j\delta_{(\widetilde v_j,\widetilde y_j)}$, with $\omega_j>0$, $\sum_j\omega_j=1$, and $s$ chosen from accuracy and uniform regularity rather than $m$. The representative training loss is $\sum_j\omega_j(f(\widetilde v_j)-\widetilde y_j)^2$. Each $m^{-1}\sum_a$ in the dense force becomes $\sum_j\omega_j$. In the corresponding selected readout, the feature columns and deficit coordinates are $\sqrt{\omega_j}h_j$ and $\sqrt{\omega_j}c_j$, so the relevant normalized feature Gram is

\[
G_{\omega,jk}=\sqrt{\omega_j\omega_k}
\langle h_j,h_k\rangle.
\]

No factor $1/s$ should be inserted unless the weights are actually equal. A stability gap would concern $G_\omega$, not a formal replacement $m\mapsto s$ in $\gamma/m$.

There is an exact special case: grouping repeated identical input locations, using their empirical frequencies and the average label within each group, changes the loss only by a parameter-independent within-group label variance. Expanding the squares proves equality of the parameter gradients and hence of the coupled dense trajectories from the same initialization. This identity holds at the canonical ODE level; duplicates violate the original positive full-Gram hypothesis, so that theorem cannot simply be invoked on the unreduced duplicated dataset.

For nonidentical representatives, a new approximation statement is required. For example, in the mobility coordinates of the paper, suppose both trajectories remain in a common parameter set, the vector field $F(\theta;\mu_m)$ is $A$-Lipschitz there, and

\[
\sup_\theta\|F(\theta;\mu_m)-F(\theta;\nu_s)\|
\le\varepsilon_F.
\]

Define $e(t)=\|\theta_{\mu_m}(t)-\theta_{\nu_s}(t)\|$, where both parameter trajectories start from the same initialization. Subtracting the ODEs and integrating the inequality $\dot e\le Ae+\varepsilon_F$, with $e(0)=0$, gives $e(t)\le\varepsilon_F(e^{At}-1)/A$; use $t\varepsilon_F$ when $A=0$. This elementary conditional bound is only finite-horizon. Proving a uniform force approximation from simple labels or low-dimensional geometry, controlling the nonlinear reachable states, and obtaining an all-time comparison with fitting tails are new obligations.

The natural composition is original dense flow → weighted-representative dense flow → compressed representative flow. Both errors must be bounded against the original dense reference. The original theorem does not supply the first arrow or its weighted all-time extension.

For Legendre this upstream change replaces sample-specific moment copies by $s$ representative copies, while retaining the dense mixers. For Harmonic it reduces the exact initialized additions, deficit count, and Gram dimension to the representative count while keeping whole-sphere query coverage. For Taylor it helps only when the requested query panel is also controlled: if every original training point must still be covered, the $m-s$ omitted training points become passive inputs and the declared total panel remains $m+p$. The Taylor source multiplier then remains sample-sized. A spatial interpolation theorem or shared sample basis is needed to remove it.

## Modification 2: projected residuals and a smaller readout solve

This is an algebraic replacement of the selected readout interface. Fix a sample subspace represented by $U\in\mathbb R^{m\times s}$, $U^\top U=I_s$. Let $b(t)\in\mathbb R^s$ be its retained normalized deficit, and define

\[
V_{C,s}=V_CU,\qquad Q_{C,s}=V_{C,s}^*V_{C,s}.
\]

Assuming $Q_{C,s}\succ0$, use

\[
\widehat w_C=w_C+V_{C,s}Q_{C,s}^{-1}
\left(U^\top\frac y{\sqrt m}-b-V_{C,s}^*w_C\right).
\]

Multiplication by $V_{C,s}^*$ gives the exact *projected* training constraint

\[
U^\top\frac{f_C-y}{\sqrt m}=-b.
\]

Let $\mathcal J_C$ be the hidden-parameter source map whose sample columns are the selected first-layer and hidden-layer update directions divided by $\sqrt m$, as in the transfer proof. Thus $K_C/m=V_C^*V_C+\mathcal J_C^*\mathcal J_C$. Prescribe

\[
\dot w_C=2V_{C,s}b,\qquad
\dot\theta_{h,C}=2\mathcal J_CUb,\qquad
\dot b=-2\left(Q_{C,s}+(\mathcal J_CU)^*(\mathcal J_CU)\right)b,
\]

with zero raw readout and $b(0)=U^\top y/\sqrt m$. Here $\theta_{h,C}$ uses the hidden parameter metric specified in the selected proof, and the responses entering $\mathcal J_C$ use the corrected readout. Direct multiplication proves

\[
-\frac d{dt}\|b\|^2
=\|\dot w_C\|^2+\|\dot\theta_{h,C}\|^2.
\]

The cancellation has the same exact algebra, with lift $V_{C,s}Q_{C,s}^{-1}$: $(V_{C,s}Q_{C,s}^{-1})Q_{C,s}=V_{C,s}$. A positive gap on this $s$-dimensional Gram is compatible with an $m$-independent lower bound. These statements establish projected consistency and an energy identity, not comparison with the original network.

The omitted deficit is a real dynamical obligation. Even if $y/\sqrt m\in\operatorname{ran}U$, the exact dense deficit $\bar c_n=c_n/\sqrt m$ obeys

\[
\frac d{dt}(U^\top\bar c_n)
=-2U^\top(K_n/m)U(U^\top\bar c_n)
-2U^\top(K_n/m)(I-UU^\top)\bar c_n.
\]

The last term is absent from the projected model. Label smoothness does not make it zero. Exact invariance of the retained sample subspace under $K_n(t)/m$ would eliminate leakage from initially retained residuals; otherwise a quantified tail/feedback bound is needed throughout training. Uniform query prediction bounds also require control of the omitted parameter forces, not only the retained residual norm.

This replacement alone still retains $U$, $V_C$, and all sample contractions unless they receive compact functional or quadrature representations. An explicit $m\times s$ matrix costs $ms$ coordinates. Exact initialized additions must also change: preserving a projected initialization gap by a controlled source approximation is plausible, but nonlinear forward propagation prevents treating averaged intermediate features as exact averages of a small forward network. A new initialization and transfer proof is required.

## Modification 3: a joint sample/time source basis

For Legendre, the sample direction can be projected without losing its central orthogonality identity. Take fixed sample functions $\psi_1,\ldots,\psi_s$ orthonormal under the empirical average, $m^{-1}\sum_a\psi_i(a)\psi_j(a)=\delta_{ij}$. For the clock histories $h_a(\xi)$ and $b_a(\xi)=r_a\delta_a/\rho$ used in the paper, define

\[
h_i(\xi)=\frac1m\sum_a\psi_i(a)h_a(\xi),\qquad
b_i(\xi)=\frac1m\sum_a\psi_i(a)b_a(\xi).
\]

Let $P_s$ be sample projection onto those functions and $\Pi_q^\tau$ the paper's degree-below-$q$ time projection on $[0,\tau]$. They commute because they act on different variables. Their product $P=P_s\Pi_q^\tau$ is an orthogonal projector for the measure $m^{-1}\sum_a\delta_a\otimes d\xi$. Componentwise orthogonality therefore gives the exact identity

\[
\frac1m\sum_a\int_0^\tau b_a h_a^\top d\xi
-\frac1m\sum_a\int_0^\tau(Pb)_a(Ph)_a^\top d\xi
=\frac1m\sum_a\int_0^\tau((I-P)b)_a((I-P)h)_a^\top d\xi.
\]

The retained mixer correction is

\[
-\frac2{n\tau}\sum_{i=1}^s\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{i,j}\bar h_{i,j}^\top,
\]

where each bar is the corresponding unnormalized Legendre integral of $b_i$ or $h_i$. Thus its moment count is $2(L-1)nsq$. Differentiating those moments gives forward writes $\rho m^{-1}\sum_a\psi_i(a)h_a$ and backward writes $m^{-1}\sum_a\psi_i(a)r_a\delta_a$, plus the same triangular time-mode mixing as the original model. The runtime has no residual division.

This identity exposes the needed estimates: control both forward and backward histories outside the *same* joint sample/time space, and supply compact evaluations of the next writes. Smooth labels alone control neither the learned feature tail nor the residual-weighted backward tail. The original growing-interval proof handles temporal tails; sample tails, their nonlinear feedback, and their effects on fitting require new estimates. Exact sample contractions still cost dependence on $m$ unless reduced upstream or represented by finite sufficient statistics.

For Harmonic, the analytic coefficient sharing already implements much of this idea: $h(t,v)$, $\delta(t,v)$, and paired initialized images have one joint time–input expansion over the sphere. A known low-dimensional parametrization can reduce the spatial coefficient count only if all required query/source maps have uniformly controlled regularity in those coordinates. Training inputs lying on a low-dimensional set does not change the promised whole-sphere forward query domain. A nonlinear latent pair description is not by itself a replacement for the coordinatewise source estimates and paired forward/transpose actions required by the selection lemma.

For Taylor, sharing spatial/sample modes across the declared curves would replace the factor $2(2m+p)$ by a controlled basis count, but that is a new joint source construction. Its existing flaring time disks prove temporal approximation for a fixed list; they do not prove such a spatial approximation or whole-sphere accuracy. Combining flaring time domains with harmonic spatial modes also needs a joint analytic-domain theorem: the finite-panel flaring result cannot simply be attached to the whole-sphere harmonic basis.

## What is exact, and what remains open

The rank obstruction, trace/close-pair gap bounds, grouping identity, projected readout/energy/cancellation identities, and joint projection tail identity above follow directly from the displayed equations. None requires a new asymptotic neural-network theorem.

The substantive open bridge is uniform control of the training force and omitted feedback under sample compression, with constants independent of $m$, on the requested time and query domain. It must also replace the full-feature-gap/small-label condition without forcing the signal to vanish. Smoothness should be quantified by fixed regularity bounds, and low-dimensional coordinates should be known or initialization-computable; neither may be inferred from a later dense trajectory. All fixed arrays, query obligations, and initialization information must be counted. Subject to those conditions, representative compression is the cleanest common upstream interface; projected readout and joint source bases are complementary repairs when exact interpolation at every sample is intentionally relaxed to controlled error.

Source hashes at analysis time (SHA-256):

- `paper/compact.tex`: `c5c3738c4a2ca7b45c2631033b3384ba95adf2ccbfdb623e21fdcf835e533a17`
- `paper/compact_legendre.tex`: `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9`
- `paper/compact_selected.tex`: `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885`
- `paper/methods.tex`: `d3a6e1d6bb1ef888086b6e0dac5f966b1c4fc1b766d12b2691f951d5f46ce4c3`

Metadata-only pre-edit check: HEAD `af9ee2765187a9d53539b60e81575a7c02d252a5`; no staged files; unrelated concurrent changes preserved. Only this assigned note was written. No tests or experiments were run; validation was a direct normalization, dimensions, rank, and algebra check against the four source files.
