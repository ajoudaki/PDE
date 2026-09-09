# Compactness of bounded observable paths, with the missing identification retained

2026-09-08. This is an a priori result for existing physical or dissipative first-row-capped paths with the distinct smooth plateau activation in `PLATEAU_GEOMETRY.md`. It does not prove cap removal or the contract's full joint limit. In particular, compactness of laws under new couplings is not convergence on the canonical common Gaussian space.

## 1. Hypotheses and uniform bounds

Use the exact normalized model and Hilbert norms in `CONTRACT.md`, with three fixed unit inputs. Suppose on a fixed interval `[0,T]` that

\[
 |\phi|\le B,\quad |\phi'|\le D,\quad |\phi''|\le D_2,
 \qquad \|A_0\|\le a_0,
\]

and that `U(0)=C(0)=0`, the initial loss is `E0=3/2`, and

\[
 E(t)+\int_0^t\|\dot\Theta(s)\|_{\rm raw}^2ds\le E_0.
 \tag{1}
\]

The matrix and readout equations are exact. The first-row equation may be multiplied by a measurable scalar in `[0,1]` at each row. Assume the paths have been constructed strongly, so their field equations and chain rules are justified. The dissipative approximants provide one application once their canonical action has been identified.

Put

\[
 R=\sqrt{6E_0},\quad c_T=BRT,\quad a_T=a_0+\sqrt{TE_0}.
\]

Here `sum_i |r_i| <= R`. Directly integrating the actual readout equation gives

\[
 |C(t)|\le c_T,\quad |h_i|,|k_i|\le B,
 \quad |b_i|\le Dc_T,
 \quad \|q_i\|_2\le a_TDc_T.
 \tag{2}
\]

The estimates are uniform over the caps and over `t<=T`. For example, the operator bound follows from `||U||op <= ||U||HS <= sqrt(TE0)`. No spatial bound for `A0* b` is inferred from (2).

Let

\[
 W_T=RD^2a_Tc_T,\quad U_T=RDBc_T,
 \quad V_T=BU_T+a_TDW_T,
 \quad B_T=RBD+D_2c_TV_T.
\]

The exact equations and the common cap bound imply

\[
 \|\dot w\|_2\le W_T,\qquad
 \|\dot U\|_{HS}\le U_T,\qquad
 \|\dot h_i\|_2\le DW_T,
\]

\[
 \|\dot v_i\|_2
 \le\|\dot U\|_{op}\|h_i\|_2+\|A\|\|\dot h_i\|_2
 \le V_T,
\]

\[
 \|\dot k_i\|_2\le DV_T,\qquad
 \|\dot C\|_2\le RB,\qquad
 \|\dot b_i\|_2\le B_T.
 \tag{3}
\]

For the last bound use `bdot_i=Cdot phi'(v_i)+C phi''(v_i) vdot_i`, with the **pointwise** readout bound from (2). These computations require only bounded activation and bounded first two derivatives, apart from the confinement invoked next.

For the plateau activation, `PLATEAU_CONFINEMENT.md` proves, separately for ranks two and three, a finite data-dependent constant `K_Gamma` for which

\[
 \sup_{t\le T}|w(t,\omega)|\le |w_0(\omega)|+K_\Gamma.
 \tag{4}
\]

It uses integrability of the realized row controls. That condition follows here from (2) and Fubini. Thus (4) is uniform over the cap and even independent of `T`. It is not asserted for arbitrary discrete steps.

## 2. An elementary path-law compactness lemma

Let a family of random absolutely continuous paths `X:[0,T]->R^m` satisfy

\[
 \sup_X\mathbb E\int_0^T|\dot X|^2dt\le M<\infty,
 \qquad
 \lim_{L\to\infty}\sup_X
 \mathbb E[\|X\|_\infty^2\mathbf1_{\{\|X\|_\infty>L\}}]=0.
 \tag{5}
\]

Then their laws form a totally bounded family for the quadratic Wasserstein distance on `C([0,T];R^m)` with its supremum norm.

Here total boundedness means that for every positive tolerance the family can be covered by finitely many Wasserstein balls. The assertion can be verified directly; no compactness theorem for differential equations is used.

**Proof.** Choose a time grid whose largest spacing is at most `eta`, and let `I_eta X` be linear interpolation of the grid values. On one grid interval, write the interpolation error as a convex combination of `X(t)-X(t_j)` and `X(t)-X(t_{j+1})`. Cauchy--Schwarz gives

\[
 \|X-I_\eta X\|_\infty^2
 \le\eta\int_0^T|\dot X|^2dt.
 \tag{6}
\]

Project each grid value onto the radius-`L` Euclidean ball, then round to a finite `epsilon`-net of that ball. Interpolate the rounded values. The result `Y` takes values in a fixed finite set of continuous paths. Projection changes any grid value by at most `||X||infinity 1_{||X||infinity>L}`; rounding adds at most `epsilon`. Therefore

\[
 \mathbb E\|X-Y\|_\infty^2
 \le 3\eta M+
 3\mathbb E[\|X\|_\infty^2\mathbf1_{\{\|X\|_\infty>L\}}]
 +3\epsilon^2.
 \tag{7}
\]

Take first `L` large, then `eta` and `epsilon` small. This uniformly approximates every law by a probability distribution on one finite set of paths. Distributions on a fixed finite metric space are totally bounded for quadratic Wasserstein distance: round their finitely many masses to a sufficiently fine finite simplex grid and couple the common mass identically; the unmatched mass pays at most the squared diameter. This and (7), which itself supplies an explicit coupling, prove the assertion. ∎

## 3. Application to same-layer joint observables

On the first layer define the joint path

\[
 X_1=(w,z_1,z_2,z_3,h_1,h_2,h_3).
\]

On the second layer define

\[
 X_2=(C,k_1,k_2,k_3,b_1,b_2,b_3).
\]

Equations (3) provide the derivative bounds in (5). The paths in `X2` have a deterministic supremum bound by (2). The supremum of `X1` is bounded by a constant times `1+|w0|+K_Gamma`; because the law of `w0` is the same finite-dimensional Gaussian for every cap, its squared envelope is uniformly integrable. The lemma consequently proves:

\[
 \boxed{\text{The families of laws of }X_1\text{ and }X_2
 \text{ are totally bounded in path-space }W_2.}
 \tag{8}
\]

The assertions are joint within each layer. If desired, the standard completeness of path-space `W2` turns total boundedness into sequential relative compactness; the substantive estimate used here is the explicit finite approximation (7).

The predictors `f_i=<C,k_i>` and the readout kernel `<k_i,k_j>` are continuous functions of the second-layer joint path law, uniformly in time. For instance, under a coupling,

\[
 \sup_t|\mathbb E[C(t)k_i(t)-\widetilde C(t)\widetilde k_i(t)]|
 \le B\,\mathbb E\|C-\widetilde C\|_\infty
   +c_T\,\mathbb E\|k_i-\widetilde k_i\|_\infty.
\]

The same product estimate treats `<h_i,h_j>` and `<b_i,b_j>`. Thus any convergent subsequence of these two layer laws identifies, uniformly on `[0,T]`, the predictors, loss, readout kernel, and matrix kernel

\[
 K_{A,ij}=\langle h_i,h_j\rangle\langle b_i,b_j\rangle.
\]

This statement is about subsequences of already-constructed population approximants. It gives neither a unique subsequential limit nor the original finite algorithms' convergence to it.

## 4. What is still missing

The second-layer *raw* preactivations `v_i`, the incoming fields `q_i`, and the first-layer true backpropagated fields `phi'(z_i)q_i` are deliberately absent from (8). Equations (2)--(3) give uniform second moments of `v` and their time derivatives, but not uniform integrability of their squared path amplitudes. Differentiating `q=A* b` also gives bounded `L2` time derivatives; that fact again does not imply spatial uniform integrability.

The missing first kernel block is

\[
 K_{W,ij}=\Gamma_{ij}\langle\phi'(z_i)q_i,\phi'(z_j)q_j\rangle.
\]

Moreover, a coupling chosen to make the two layer laws converge can change the representation of the initialized operator and its adjoint. It does not identify a strong limit on the common canonical Gaussian space. Repeated-matrix returns, source causality, uniqueness, true velocities and the actual GF/GD bridge still require their own proof. Bounded observables can converge while raw second moments concentrate. The compactness above must not be used to erase that distinction.
