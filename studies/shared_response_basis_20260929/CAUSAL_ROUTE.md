# Causal streaming route for a shared learned basis

Scoped theoretical report, 2026-09-29. Inputs were the supervisor's neutral assignment and the canonical equations supplied in this task. No other study, dense trajectory, experiment, or external scientific source was used. This is an internally derived result, not established book material.

## Result and scope

There is a deterministic, autonomous **discrete** shared-basis scheme with two rank-r buffers per middle layer, exact static initialization, and no sample-indexed moving moments. A single pass over the samples at each explicit time step suffices. Its cumulative compression defect is bounded by total nuclear variation divided by r+1 in operator norm, with no factor equal to the number of steps or samples. A nonlinear stability argument then proves compact-time tracking of the canonical gradient flow.

The construction is not a smooth fixed-dimensional moment ODE, ordinary gradient descent on factors, or a collection of snapshot SVDs. It is a streaming singular-value shrinkage integrator. It is restartable from its own finite state. The theorem is uniform in sample count under bounded normalized inputs and a label RMS bound, at fixed width and depth. Width-uniform stability constants, a unique continuous-time limit of the compressed dynamics, and useful compression r much smaller than n in every instance are not proved.

The proof has three independent parts: an algebraic streaming lemma; an exact cumulative-defect identity for an approximate trajectory using its own residuals and features; and a finite-dimensional nonlinear feedback estimate. The original PSD-lift route is recorded at the end; direct signed shrinkage gives a simpler and sharper theorem.

## 1. Canonical target and admissible information

Let n,d,m be positive integers and let the number of hidden layers be L≥2. The parameters are

\[
\theta=(W_1,W_2,\ldots,W_L,w),\qquad
W_1\in\mathbb R^{n\times d},\quad W_\ell\in\mathbb R^{n\times n}\ (\ell\ge2),\quad w\in\mathbb R^n.
\]

For sample \(x_a\),

\[
z_{1,a}=W_1x_a/\sqrt d,\quad h_{1,a}=\phi(z_{1,a}),\qquad
z_{\ell,a}=W_\ell h_{\ell-1,a},\quad h_{\ell,a}=\phi(z_{\ell,a}),\qquad
f_a=w^Th_{L,a}/n.
\]

The activation acts componentwise and satisfies \(\phi\in C^{1,1}_{\rm loc}(\mathbb R)\). Write \(r_a=f_a-y_a\), \(\mathcal L=m^{-1}\sum_a r_a^2\), and

\[
\delta_{L,a}=w\odot\phi'(z_{L,a}),\qquad
\delta_{\ell,a}=\phi'(z_{\ell,a})\odot W_{\ell+1}^T\delta_{\ell+1,a}.
\]

The target flow is \(\dot\theta=F(\theta)\), with

\[
\dot W_1=-\frac2m\sum_a r_a\delta_{1,a}x_a^T/\sqrt d,\qquad
\dot w=-\frac2m\sum_a r_a h_{L,a},\qquad
\dot W_\ell=-\frac2{mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T\quad(2\le\ell\le L).
\tag{1}
\]

The admissible data class satisfies

\[
\|x_a\|_2/\sqrt d\le X,\qquad
\left(m^{-1}\sum_a y_a^2\right)^{1/2}\le Y.
\tag{2}
\]

Initial parameters are fixed and are available statically. In particular every dense initialized middle matrix \(W_{\ell,0}\) is retained exactly. The learned increment alone is compressed:

\[
\widehat W_\ell=W_{\ell,0}+M_\ell,\qquad
M_\ell=U_\ell V_\ell^T,\qquad \operatorname{rank}M_\ell\le r.
\tag{3}
\]

One factor pair is shared across all samples in a layer. Different layers may use different pairs. The full dataset is statically accessible. Runtime may depend on m; the retained moving state may not contain m feature or adjoint vectors. Neither coefficients nor initialization may depend on the future target trajectory.

## 2. A streaming compression lemma proved from scratch

Let \(A_1,A_2,\ldots\in\mathbb R^{n\times n}\) be any causally supplied rank-at-most-one matrices; they may depend arbitrarily on earlier sketch states. Fix \(0\le r<n\). Set \(M_0=0\). Given \(M_{q-1}\) and \(A_q\), form conceptually

\[
B_q=M_{q-1}+A_q.
\]

Its rank is at most r+1. Let \(\delta_q=\sigma_{r+1}(B_q)\), taking absent singular values to be zero, and set

\[
M_q=\mathcal S_{\delta_q}(B_q),\qquad
\mathcal S_\delta(U\operatorname{diag}(\sigma_i)V^T)
 =U\operatorname{diag}((\sigma_i-\delta)_+)V^T.
\tag{4}
\]

This has rank at most r. Define the discarded matrix \(D_q=B_q-M_q\), the cumulative discard \(E_q=\sum_{i\le q}D_i\), and the supplied nuclear variation \(V_q=\sum_{i\le q}\|A_i\|_*\). Then

\[
M_q=\sum_{i\le q}A_i-E_q,
\tag{5}
\]

and simultaneously for every prefix q,

\[
\|E_q\|_{\rm op}\le \frac{V_q}{r+1},\qquad
\|E_q\|_F\le \frac{V_q}{\sqrt{r+1}}.
\tag{6}
\]

**Proof.** If \(\delta_q=0\), then \(D_q=0\). If \(\delta_q>0\), the matrix \(B_q\) has exactly r+1 positive singular values, each at least \(\delta_q\). All r+1 singular values of \(D_q\) equal \(\delta_q\), including when the smallest singular value is repeated. Consequently

\[
\|D_q\|_{\rm op}=\delta_q,\qquad
\|D_q\|_F=\sqrt{r+1}\,\delta_q,
\qquad
\|M_q\|_* = \|B_q\|_*-(r+1)\delta_q.
\]

These equalities also hold when \(\delta_q=0\). The nuclear-norm triangle inequality gives

\[
\|M_q\|_*+(r+1)\delta_q\le\|M_{q-1}\|_*+\|A_q\|_*.
\]

Summing over q steps telescopes the stored nuclear norm:

\[
\|M_q\|_*+(r+1)\sum_{i\le q}\delta_i\le V_q.
\tag{7}
\]

Equation (5) follows by summing \(M_q=M_{q-1}+A_q-D_q\). Applying the operator and Frobenius triangle inequalities to \(E_q\), then using (7), proves (6). No probabilistic independence, source smoothness, or fixed source sequence was needed. □

This is precisely the source estimate missing from an argument that merely sums unrelated truncation tolerances. It uses total supplied variation once. Strong cancellation among the supplied matrices does not invalidate the estimate, though it can make the variation bound pessimistic.

For \(r\ge n\), retain every singular value and set every discard to zero. All compression estimates may then be replaced by zero. The case r=0 is mathematically valid, although it freezes all learned middle increments.

### Implementation without a dense learned matrix

Maintain a thin SVD or any equivalent rank-r factorization of \(M_{q-1}\). For \(A_q=ab^T\), augment the column and row spaces by a and b. Orthogonalize these two augmented skinny matrices and take the SVD of the resulting core, whose two dimensions are at most r+1. Apply (4) to this core and update the skinny factors. This computes (4) exactly in exact arithmetic; no n by n learned accumulator is needed.

At initialization the factors have zero columns. A zero atom is skipped. Rank deficiencies and singular-value ties cause no ambiguity in the matrix \(\mathcal S_\delta(B)\): on a tied singular subspace, the same scalar function is applied to every singular value. Factor gauges can be chosen deterministically, but the matrix update and all future network computations do not depend on that gauge. No inverse of a retained singular value occurs in the mathematical update. Finite-precision stability is separate from this exact-arithmetic theorem.

## 3. Executable causal network integrator

Choose a time step \(h>0\) and rank cap r. At time \(t_k=kh\), the state consists of outer parameters \((\widehat W_{1,k},\widehat w_k)\) and the factors of \(M_{\ell,k}\), for \(2\le\ell\le L\). Initialize these outer parameters exactly and put every \(M_{\ell,0}=0\).

For one macro-step:

1. Freeze the entire current approximate network as a read-only buffer. Make a working copy of its middle factors, and initialize two outer-gradient accumulators to zero.
2. Stream the samples in a fixed order. Compute that sample's residual, all activations, and all backpropagated vectors **in the frozen approximate network**.
3. For every middle layer insert the rank-one atom
   \[
   A_{\ell,k,a}=-\frac{2h}{mn}\widehat r_{k,a}\,
      \widehat\delta_{\ell,k,a}\widehat h_{\ell-1,k,a}^T
   \tag{8}
   \]
   into the working factors using (4). Accumulate the corresponding two outer updates from (1), multiplied by h.
4. After the pass, install the working middle factors and the simultaneously updated outer parameters as the next state.

All sources in (8) are evaluated at the same frozen network. Evaluating later samples in already-mutated working factors would define a different method and would invalidate the exact Euler identity below.

The output trajectory is the held state

\[
\widehat\theta_h(t)=\widehat\theta_k,
\qquad kh\le t<(k+1)h.
\tag{9}
\]

This is an autonomous recursion: only the current finite state, fixed data, fixed initialized matrices, h, and the fixed sample ordering determine the next state. Adding a clock and the finite inner-loop phase gives an autonomous hybrid implementation. Restarting during a sample pass additionally retains the frozen buffer, working buffer, outer accumulators, and current sample index; these are already part of the specified bounded working state. This statement does not assert a smooth ODE for the factors or a unique limit as \(h\downarrow0\) at fixed r.

Persistent and working middle storage is \(O(Lnr)\). The exact outer parameters and their buffers require \(O(nd+n)\), and one-sample forward/backward scratch requires \(O(Ln+d)\). Dataset size and the dense initialized matrices are static storage. A loop index has \(O(\log m)\) bits; the real-valued moving-state dimension is independent of m. No list of past atoms, residuals, features, or adjoints is retained. One step requires a full data pass and skinny matrix operations, so runtime is intentionally not independent of m.

## 4. Explicit constants free of sample count

Write \(\|\cdot\|_E\) for the Euclidean norm on the full parameter vector, using Frobenius norms for matrices. Let

\[
F_0=\sup_{\|x\|/\sqrt d\le X}|f(x;\theta_0)|,
\qquad \overline{\mathcal L}_0=(F_0+Y)^2,
\qquad R_0=\sqrt{nT\overline{\mathcal L}_0}.
\tag{10}
\]

The initial empirical loss is at most \(\overline{\mathcal L}_0\), because the RMS norm of \((f(x_a;\theta_0)-y_a)_a\) is at most \(F_0+Y\).

The canonical flow has block learning rate n in \(W_1,w\) and rate 1 in the middle matrices. The chain rule applied to (1) therefore gives the exact dissipation identity

\[
-\frac{d\mathcal L}{dt}
=\frac1n\bigl(\|\dot W_1\|_F^2+\|\dot w\|_2^2\bigr)
  +\sum_{\ell=2}^L\|\dot W_\ell\|_F^2.
\tag{11}
\]

As \(n\ge1\), this implies

\[
\int_0^T\|\dot\theta(t)\|_E^2dt\le n\mathcal L(0),\qquad
\|\theta(t)-\theta_0\|_E
\le\sqrt{t}\left(\int_0^t\|\dot\theta(s)\|_E^2ds\right)^{1/2}
\le R_0.
\tag{12}
\]

The vector field is locally Lipschitz because \(\phi\in C^{1,1}_{\rm loc}\). The elementary finite-dimensional existence theorem used here states that a locally Lipschitz vector field has a unique maximal solution and that a solution with a finite maximal endpoint must leave every compact set. Bound (12) prevents this on every finite horizon, so the canonical solution exists uniquely on \([0,T]\).

Define the known parameter ball

\[
\mathcal B=\{\theta:\|\theta-\theta_0\|_E\le R_0+1\}.
\]

All following suprema concern \(\theta\in\mathcal B\) and \(\|x\|/\sqrt d\le X\). Let

\[
F_* =\sup |f(x;\theta)|,
\qquad G=\sup\|\nabla_\theta f(x;\theta)\|_E,
\]

and choose H such that

\[
\|\nabla f(x;\theta)-\nabla f(x;\vartheta)\|_E
\le H\|\theta-\vartheta\|_E
\qquad(\theta,\vartheta\in\mathcal B).
\tag{13}
\]

These constants are finite: the parameter/input domain is compact, activations are continuously differentiable there, their derivatives are Lipschitz on the bounded preactivation ranges, and finite compositions and products preserve these properties. A uniform constant H follows by applying those same bounded derivative and product estimates on the whole convex ball. No supremum over labels is used.

The field is \(F(\theta)=-2m^{-1}\sum_a r_a A\nabla f_a\), where A multiplies the first/last blocks by n and the middle blocks by 1. Since \(\|A\|_{E\to E}=n\),

\[
\|F(\theta)\|_E\le M_E:=2n(F_*+Y)G,
\tag{14}
\]

and

\[
\|F(\theta)-F(\vartheta)\|_E
\le K_E\|\theta-\vartheta\|_E,
\quad
K_E:=2n\bigl[G^2+(F_*+Y)H\bigr].
\tag{15}
\]

For (15), write \(r_\theta\nabla f_\theta-r_\vartheta\nabla f_\vartheta
=(f_\theta-f_\vartheta)\nabla f_\theta+r_\vartheta(\nabla f_\theta-\nabla f_\vartheta)\), use \(|f_\theta-f_\vartheta|\le G\|\theta-\vartheta\|_E\), and average \(|r_\vartheta|\le F_*+m^{-1}\sum_a|y_a|\le F_*+Y\).

For a middle layer define

\[
H_{\ell-1,*}=\sup\|h_{\ell-1}(x;\theta)\|_2,
\qquad D_{\ell,*}=\sup\|\delta_\ell(x;\theta)\|_2,
\]

and

\[
b_\ell=\frac{2(F_*+Y)}nD_{\ell,*}H_{\ell-1,*},
\qquad b_* =\max_{2\le\ell\le L}b_\ell.
\tag{16}
\]

For every frozen approximate state in \(\mathcal B\), the atoms in one full pass satisfy

\[
\sum_a\|A_{\ell,k,a}\|_*
=\frac{2h}{mn}\sum_a|\widehat r_{k,a}|\,
     \|\widehat\delta_{\ell,k,a}\|_2\|\widehat h_{\ell-1,k,a}\|_2
\le h b_\ell.
\tag{17}
\]

This displays the exact sample and width normalizations. If normalized feature and adjoint bounds \(H_{\ell-1,*}/\sqrt n\) and \(D_{\ell,*}/\sqrt n\) are uniform in width, then b is uniform in width. The present compact-ball argument alone does not establish those uniform bounds or a width-uniform K.

Finally use the mixed norm

\[
\|\Delta\theta\|_X
=\max\left\{
\bigl(\|\Delta W_1\|_F^2+\|\Delta w\|_2^2\bigr)^{1/2},
\max_{2\le\ell\le L}\|\Delta W_\ell\|_{\rm op}\right\}.
\tag{18}
\]

With \(c=\sqrt{1+(L-1)n}\),

\[
\|\Delta\theta\|_X\le\|\Delta\theta\|_E\le c\|\Delta\theta\|_X.
\tag{19}
\]

Thus one valid mixed-norm field Lipschitz constant is \(K=cK_E\), and one valid field-size bound is \(M=M_E\). All quantities (10), (13)--(19) depend on the stated activation, initialization, n,d,L,X,Y,T, and are independent of m. They are intentionally conservative. They can be upper-bounded from activation and initial-parameter bounds without running the dense target trajectory.

## 5. Complete compact-time tracking theorem

For \(0\le r<n\), put \(\beta=Tb_* /(r+1)\). For \(r\ge n\), put \(\beta=0\). Suppose

\[
c\,e^{KT}(\beta+hM)<1.
\tag{20}
\]

Then every approximate state needed through time T lies in \(\mathcal B\), and the fully executable algorithm of Section 3 obeys

\[
\sup_{0\le t\le T}\|\widehat\theta_h(t)-\theta(t)\|_X
\le e^{KT}\left(\frac{Tb_*}{r+1}+hM\right)
\tag{21}
\]

when \(r<n\); replace the compression term by zero when \(r\ge n\). In particular

\[
\sup_{0\le t\le T}\|\widehat\theta_h(t)-\theta(t)\|_E
\le c e^{KT}(\beta+hM),
\tag{22}
\]

and, uniformly over every input satisfying the input bound,

\[
\sup_{0\le t\le T}
|f(x;\widehat\theta_h(t))-f(x;\theta(t))|
\le Gc e^{KT}(\beta+hM).
\tag{23}
\]

**Proof.** First suppose the approximate states remain in \(\mathcal B\) up to the time considered. Concatenate the atoms of each layer over all completed sample passes. By (17), their supplied variation through \(t_k\le T\) is at most \(t_kb_\ell\). The streaming lemma gives a cumulative middle-layer discard \(E_{\ell,k}\) with

\[
\|E_{\ell,k}\|_{\rm op}\le\frac{t_kb_\ell}{r+1}.
\]

Put these discards in the middle blocks of a parameter vector \(E_k\), with zero outer blocks. Simultaneous frozen-state evaluation in the algorithm gives the **exact** identity

\[
\widehat\theta_k=\theta_0+h\sum_{j<k}F(\widehat\theta_j)-E_k,
\qquad\|E_k\|_X\le\beta.
\tag{24}
\]

For \(t_k\le t<t_{k+1}\), (9) and (24) imply

\[
\widehat\theta_h(t)
=\theta_0+\int_0^tF(\widehat\theta_h(s))\,ds
 -E_k-(t-t_k)F(\widehat\theta_k).
\tag{25}
\]

Subtract the original flow's integral equation and use (14), (15), and (19). For \(e(t)=\|\widehat\theta_h(t)-\theta(t)\|_X\),

\[
e(t)\le\beta+hM+K\int_0^te(s)\,ds.
\tag{26}
\]

For completeness, if \(a=\beta+hM\) and \(u(t)=a+K\int_0^te(s)ds\), then \(e\le u\) and \(u'\le Ku\) almost everywhere. Multiplication by \(e^{-Kt}\) and integration give \(e(t)\le ae^{Kt}\), proving (21). The same argument is valid at grid jumps because (24) is valid there and the integral is unaffected by single time points.

To remove the provisional ball assumption, take the first grid state leaving \(\mathcal B\), if any. Its source atoms were all evaluated at earlier states in \(\mathcal B\), so the preceding argument remains valid through that grid time. Equations (19)--(21) and (20) put this state at Euclidean distance less than 1 from the exact state, which by (12) has distance at most \(R_0\) from \(\theta_0\). The state therefore still belongs to \(\mathcal B\), a contradiction. This proves the required bootstrap. Equations (22) and (23) follow from (19) and the gradient bound on the convex ball. □

For a requested mixed-norm error \(\varepsilon<1/c\), it suffices to choose

\[
\frac{Tb_*}{r+1}\le\frac{\varepsilon e^{-KT}}2,
\qquad hM\le\frac{\varepsilon e^{-KT}}2,
\tag{27}
\]

using exact rank n if the first condition would demand a larger rank. If \(M=0\), no restriction on h is needed for this term. These choices are independent of sample count. Different layer caps are allowed by replacing \(Tb_* /(r+1)\) with \(T\max_\ell b_\ell/(r_\ell+1)\), with zero contribution from fully retained layers.

There is also a useful uncompressed Euclidean version: concatenate the Frobenius estimates in (6) and obtain compression defect at most

\[
\frac{T(\sum_{\ell=2}^Lb_\ell^2)^{1/2}}{\sqrt{r+1}}.
\tag{28}
\]

Then apply the same proof in Euclidean norm with \(K_E,M_E\). This has an inferior rank rate but avoids the norm-equivalence factor in the exponential. Depending on n,L,T, it can provide a better numerical certificate than (21). Both estimates are rigorously available; neither should be discarded solely because its formal rank exponent is worse.

## 6. What the result resolves and what it does not

* **Causal closure, proved:** all nonlinear residuals, features, and adjoints come from the current approximate network and statically accessible samples. There is no dense oracle source.
* **Sample-independent moving state, proved:** factors, outer parameters, one-sample scratch, fixed-size buffers, and counters suffice. Full-batch runtime and static dataset storage still depend on sample count.
* **Compression production, proved:** (6) is a uniform prefix bound for arbitrary adaptive rank-one streams. It closes the repeated-truncation accumulation gap through (7).
* **Nonlinear feedback, proved:** (21)--(23), including the bootstrap, track the canonical nonlinear flow rather than only a supplied matrix history.
* **Rank-zero initialization and crossings, resolved algebraically:** the sketch starts empty, uses no reciprocal singular values, and the matrix shrinkage map is independent of singular-vector gauge.
* **Uniformity in sample count, proved at fixed width:** all constants use bounded inputs and a label RMS bound, not a maximum label or a data Gram inverse.
* **A genuinely small rank in all regimes, open/not claimed:** worst-case stability bounds may demand r near n. Exact rank saturation gives convergence but is not evidence of useful width compression.
* **Uniformity in width, open:** the explicit energy ball and norm equivalence have width dependence, and compactness alone does not control normalized features, adjoints, or nonlinear stability uniformly in width.
* **A smooth finite-state ODE, not claimed:** the proved witness is an executable discrete/hybrid system. The estimate lets h and compression accuracy be chosen jointly; it does not identify a unique fixed-rank continuous-time dynamics.
* **Finite precision, unproved here:** the skinny implementation is exact algebraically. Roundoff, numerical rank thresholds, and accumulated floating-point drift need a separate implementation error budget.

The strongest surviving obstruction to the intended ambitious compression claim is therefore quantitative width/stability control, not causality or sample-indexed hidden memory. The next useful theorem would establish a forward/backward regularity region giving uniform \(b_\ell\) and a suitable dimension-independent nonlinear stability estimate. That is a stronger research question than the finite-width theorem proved here.

## 7. Stronger unconditional bounded-activation variant

The supervisor additionally supplied the bounded-activation route, checked here. Suppose globally \(|\phi|\le H_0\) and \(|\phi'|\le s\), in addition to the local Lipschitz assumption on \(\phi'\). The case \(H_0=0\) has identically zero activation and zero training vector field and is exact at every rank. Assume \(H_0>0\) below.

In this setting both the exact and approximate trajectories have finite-time bounds independent of rank and step size, so the small-error bootstrap (20) is unnecessary. Let

\[
B_0=\|w_0\|_2/\sqrt n,\qquad
\overline B=e^{2H_0^2T}(B_0+2H_0YT),\qquad
\rho=H_0\overline B+Y.
\tag{29}
\]

Indeed, for the approximate flow let \(B_k=\|\widehat w_k\|/\sqrt n\). Bounded features and the sample RMS bound give

\[
B_{k+1}\le B_k+2hH_0(H_0B_k+Y).
\]

Iterating this scalar inequality and using \((1+2hH_0^2)^k\le e^{2H_0^2kh}\) gives \(B_k\le\overline B\) for every \(kh\le T\). The same integrating-factor argument gives this bound for the exact continuous flow. All exact and approximate residuals have sample mean absolute value at most \(\rho\).

Starting from the top layer, define the following constants by backward induction:

\[
\mathcal D_\ell
=\overline B\,s^{L-\ell+1}\prod_{j=\ell+1}^L C_j,
\qquad b_\ell=2\rho H_0\mathcal D_\ell,
\qquad V_\ell=Tb_\ell,
\qquad C_\ell=\|W_{\ell,0}\|_{\rm op}+V_\ell
\quad(\ell=L,L-1,\ldots,2),
\tag{30}
\]

where an empty product equals 1. These definitions are not circular: the formula at layer \(\ell\) only uses already defined layers above it. Both trajectories satisfy

\[
\|\delta_\ell\|_2/\sqrt n\le\mathcal D_\ell,
\qquad \|W_\ell\|_{\rm op}\le C_\ell,
\qquad \|h_\ell\|_2/\sqrt n\le H_0.
\tag{31}
\]

For the approximate trajectory, the nuclear potential inequality (7) gives \(\|M_{\ell,k}\|_*\le\sum_{j<k,a}\|A_{\ell,j,a}\|_*\). Thus (31) follows by backward induction: first \(\delta_L\) is bounded directly using \(w\); its source variation is at most \(V_L\), hence \(\|W_L\|_{\rm op}\le C_L\); then the same reasoning applies one layer below. For the exact trajectory, the integral of the nuclear norm of its velocity gives the identical estimate. This also verifies that every layer's total supplied nuclear variation through T is at most \(V_\ell\), for every rank cap and every step size.

Set

\[
\mathcal D_1=\overline B s^L\prod_{j=2}^L C_j,
\qquad V_1=2T\rho X\mathcal D_1.
\tag{32}
\]

The first-layer update then gives, for both trajectories,

\[
\|W_1-W_{1,0}\|_F/\sqrt n\le V_1.
\tag{33}
\]

Consequently both trajectories belong to the same convex compact set

\[
\mathcal K_T=\left\{\theta:
\|w\|/\sqrt n\le\overline B,
\ \|W_1-W_{1,0}\|_F/\sqrt n\le V_1,
\ \|W_\ell-W_{\ell,0}\|_{\rm op}\le V_\ell\ (\ell\ge2)
\right\}.
\tag{34}
\]

Use the normalized mixed norm

\[
\|\Delta\theta\|_N
=\max\left\{
\frac{(\|\Delta W_1\|_F^2+\|\Delta w\|_2^2)^{1/2}}{\sqrt n},
\ \max_{\ell\ge2}\|\Delta W_\ell\|_{\rm op}
\right\}.
\tag{35}
\]

One explicit bound on field size in this norm is

\[
M_N=\max\left\{
2\rho\sqrt{X^2\mathcal D_1^2+H_0^2},\ \max_{\ell\ge2}b_\ell
\right\}.
\tag{36}
\]

There is a finite Lipschitz constant \(K_{T,n}\) for F on \(\mathcal K_T\) in this norm, uniformly over the data class (2). To see this without assuming a Hessian exists everywhere, use the same bounded local-Lipschitz estimates on \(\nabla f\) as in (13), now on the convex compact set (34). The Euclidean bound (15) applies with the constants for this set; norm equivalence \(\|\Delta\theta\|_E\le\sqrt{nL}\|\Delta\theta\|_N\) then supplies one admissible \(K_{T,n}\). This bound may depend on width.

The exact defect identity and proof (24)--(26) now apply without a stopping time or (20), and yield for **every** \(h>0\) and \(0\le r<n\),

\[
\sup_{0\le t\le T}\|\widehat\theta_h(t)-\theta(t)\|_N
\le e^{K_{T,n}T}
\left[\frac{T\max_{\ell\ge2}b_\ell}{r+1}+hM_N\right].
\tag{37}
\]

As before, set the compression term to zero for \(r\ge n\). Large right-hand sides are possible, but every quantity and the algorithm remain well defined.

A width-uniform forward observable estimate is also available. Define

\[
a_1=sX,\qquad a_\ell=s(C_\ell a_{\ell-1}+H_0)\quad(\ell\ge2),
\qquad P_T=H_0+\overline B a_L.
\tag{38}
\]

For two parameters in \(\mathcal K_T\), let \(e=\|\theta-\vartheta\|_N\). The first-layer difference satisfies \(\|h_1(\theta)-h_1(\vartheta)\|/\sqrt n\le sX e=a_1e\). At each later layer, add and subtract \(W_\ell(\theta)h_{\ell-1}(\vartheta)\), use (31), and obtain

\[
\|h_\ell(\theta)-h_\ell(\vartheta)\|/\sqrt n
\le s[C_\ell a_{\ell-1}+H_0]e=a_\ell e.
\]

Splitting the output difference between the change of w and the change of \(h_L\) gives \(|f(x;\theta)-f(x;\vartheta)|\le P_T e\). Therefore multiplying (37) by \(P_T\) gives a uniform-in-input prediction estimate.

If \(B_0\), \(\|W_{\ell,0}\|_{\rm op}\), X,Y,L,T,H_0,s are bounded independently of width, the variation constants \(V_\ell\), field-size constant \(M_N\), and prediction constant \(P_T\) above are independent of both sample count and width. The remaining possible width dependence in the accuracy theorem is the nonlinear feedback constant \(K_{T,n}\). A globally bounded \(\phi'\) alone does not prove that this constant is width uniform; a backpropagated-coordinate product can require additional control. This distinction is essential.

## 8. Independently derived PSD-lift alternative

Before the direct signed shrinkage route was supplied by the supervisor, this route used a positive-semidefinite lift. It is valid but less economical in its Frobenius constant.

For a nonzero rank-one atom \(A=\gamma uv^T\), define

\[
p=\sqrt{\frac{|\gamma|\|v\|}{\|u\|}}u,
\qquad q=\operatorname{sgn}(\gamma)
\sqrt{\frac{|\gamma|\|u\|}{\|v\|}}v,
\qquad z=(p,q)\in\mathbb R^{2n}.
\]

Then the upper-right block of \(zz^T\) is A and \(\operatorname{tr}(zz^T)=2\|A\|_*\). Zero atoms are skipped. Maintain a rank-at-most-r PSD matrix \(Q=ZZ^T\) on \(\mathbb R^{2n}\). After inserting \(zz^T\), if the rank is r+1, let \(\delta\) be the smallest positive eigenvalue and subtract \(\delta P\), where P is the orthogonal projector onto the current range. Otherwise discard zero. The result is PSD of rank at most r and can be computed using only the skinny factor \([Z,z]\).

Each nonzero discard has the form \(D_i=\delta_iP_i\), with

\[
0\preceq D_i\preceq\delta_i I,
\qquad \operatorname{tr}D_i=(r+1)\delta_i.
\]

If \(C=\sum zz^T\), \(E=\sum D_i\), and \(\Delta=\sum\delta_i\), the exact relation is \(Q=C-E\). Positivity and the trace identity give

\[
0\preceq E\preceq\Delta I,
\qquad (r+1)\Delta=\operatorname{tr}E\le\operatorname{tr}C=2V.
\]

The upper-right block \(E_{12}\) satisfies

\[
\|E_{12}\|_{\rm op}\le\Delta/2\le\frac V{r+1}.
\]

Indeed \(E-\Delta I/2\) has operator norm at most \(\Delta/2\), and taking an off-diagonal block cannot increase that norm. Moreover

\[
2\|E_{12}\|_F^2\le\|E\|_F^2
\le\Delta\operatorname{tr}E
=(r+1)\Delta^2,
\]

so \(\|E_{12}\|_F\le\sqrt2 V/\sqrt{r+1}\). Taking the learned matrix to be \(Q_{12}\) gives the same operator estimate and the same feedback proof as above, with a factor pair obtained by splitting Z into its two n-row blocks. The unformed covariance C is only an analytic comparison object, never stored by the algorithm.

This alternative independently confirms that a nuclear-variation budget can support an online sample-shared basis. Direct signed shrinkage removes the auxiliary covariance interpretation and improves the Frobenius constant from \(\sqrt2\) to 1.
