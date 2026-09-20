# Joint rank-one stationarity: exact classification and obstruction

Status: frozen analytical candidate, 2026-09-18, before reporting to the supervisor. No experiment was run. This is study-owned, unpromoted material.

Scientific input scope: all of `docs/observable_p1.md`, the exact state/equations/existence material of C.4.7.9.3–4 and C.4.7.10.D.3 in `docs/global_nonlinear.md`, and this study's complete `terminal_geometry.md` and `architectural_loss_floor.md`. No other study, newer plateau argument, prior review, history, or other agent's findings was used. The investigate-conjectures and solve-math-rigorously skills and the research-contract and adversarial-audit references were applied.

## 1. Result and its scope

Combining readout, lower, and middle stationarity does **not** force an architectural input conflict. There are exact finite critical states on the canonical correlated mark spaces, with bounded `w-g`, bounded odd readout, the prescribed ridge, the actual full transpose, three independent unit inputs, balanced label mass, positive loss strictly below the initialized loss, and **every residual-weighted middle rank-one term nonzero**. An explicit construction below has loss `3/4` and `rank M=2`.

The sharper exclusion is conditional: for three linearly independent inputs, every residual-active upper derivative `d_i` belongs to `ker M^T`. If `M` has full row rank, every such `d_i` is zero. Thus full row rank rules out the nonzero-`d_i` cancellation branch, but does not rule out compatible positive-loss critical states on the zero-`d_i` branch. An explicit full-row-rank modification has the same loss `3/4`.

These are exact ambient stationary-state statements. Neither construction is asserted to be attained from `(w,c,M)=(g,0,D)`. Consequently the proposed initialized endpoint theorem remains open here. What fails is the claim that the three stationarity equations alone establish that theorem.

## 2. Exact canonical equations

Use the initialized odd sector, which removes only the invariant inactive constant row and column. In dimension three the exact lower mark is `b_1 in R^6`, the upper mark is `b_2 in R^3`, and all entries of `M in R^(3 x 6)` remain trainable. These are the exact marks of `docs/observable_p1.md`, including `R_j=sqrt(tau) Z_j+alpha tanh(G_j)` and `eta=1/4096`. No marginal is replaced by an independent approximation.

Let the three distinct training inputs `u_i` be linearly independent unit vectors, let `p_i>0` sum to one, and let `y_i in {+1,-1}`. At a finite state write

\[
\begin{gathered}
a_i=E_1[b_1\tanh(w\cdot u_i)],\qquad v_i=Ma_i,
\qquad h_i=\tanh(b_2\cdot v_i),\qquad f_i=E_2[ch_i],\\
d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_i)],
\qquad q_i=b_1^TM^Td_i,\qquad
\lambda_i=p_i(f_i-y_i).
\end{gathered}
\tag{1}
\]

Here finite means `w-g` and `c` are essentially bounded and `M` is finite. The unhalved physical loss is `L=sum_i p_i(f_i-y_i)^2`, and the exact equations are

\[
\begin{split}
\dot c&=-2\sum_i\lambda_i h_i,\\
\dot w&=-2\sum_i\lambda_i\operatorname{sech}^2(w\cdot u_i)q_i u_i,\\
\dot M&=-2\sum_i\lambda_i d_i a_i^T.
\end{split}
\tag{2}
\]

The constant-coordinate formulation gives the same equations: odd parity makes the constant entries of both `a_i` and `d_i` zero. The lower Gram `G=E_1[b_1b_1^T]` is positive definite. To verify this, condition on all `G_j`. A nonzero coefficient of any `k_j=tanh(R_j)` has positive conditional variance because its independent reverse Gaussian has variance `tau>0`; independence across coordinate pairs prevents cancellation of these variances. If all such coefficients vanish, independence and positive variance of `tanh(G_j)` force all remaining coefficients to vanish. The ridge normalization is an invertible linear transformation, so it preserves positive definiteness. Therefore

\[
b_1^TM^Td_i=0\text{ almost surely}
\quad\Longleftrightarrow\quad M^Td_i=0.
\tag{3}
\]

At any stationary state, independence of the input vectors in the lower equation, strict positivity of every finite tanh gate, and (3) give `lambda_i M^T d_i=0` separately for each `i`. Conversely these equations make the lower velocity vanish. Thus stationarity is exactly

\[
\sum_i\lambda_i h_i=0,\qquad
\lambda_iM^Td_i=0\ (i=1,2,3),\qquad
\sum_i\lambda_i d_i a_i^T=0.
\tag{4}
\]

In particular, if `rank M=3`, every nonzero residual forces `d_i=0`. If `rank M=r<3`, each residual-active `d_i` lies in the `(3-r)`-dimensional space `ker M^T`. This conclusion uses the evolving matrix itself, not the initialized matrix or a substitute transpose.

If an initialized trajectory converges in the bounded-increment/readout/Frobenius norms to a finite state, continuity of the vector field makes that state stationary. Indeed a nonzero limiting velocity has a continuous linear functional with strictly positive value on a neighborhood of that velocity; integrating this functional would contradict convergence. This observation supplies a necessary endpoint condition, but supplies no converse reachability claim.

## 3. Complete readout reduction and the remaining middle constraints

Partition the nonzero `v_i` into signed-equality groups. For each group `G` choose `v_G!=0` and signs `sigma_i` such that `v_i=sigma_i v_G`. Let `Z` be the zero-vector group. Set

\[
W_G=\sum_{i\in G}p_i,\quad
A_i=\sigma_i a_i,\quad t_i=\sigma_i y_i,\quad
F_G=E_2[c\tanh(b_2\cdot v_G)],\quad
d_G=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_G)].
\]

For at most three nonzero vectors, the tanh functions from different signed-equality groups are linearly independent. Here is the needed proof. The upper mark law has positive density on an open cube about zero. An almost-sure functional identity extends to that cube by continuity. Choose a direction `e` such that the nonzero numbers `e.v_G` have distinct squares; only finitely many proper hyperplanes are excluded. Restrict to a small segment `b_2=s e`. The first three odd Taylor coefficients of tanh are nonzero. The required first one, two, or three coefficient equations form a Vandermonde system in `(e.v_G)^2`, so every group coefficient vanishes.

Consequently readout stationarity is equivalent to

\[
F_G=m_G:=\frac{\sum_{i\in G}p_it_i}{W_G}
\quad\text{for each nonzero group }G.
\tag{5}
\]

There is no readout condition on `Z`, since its upper features and predictions are zero. Define

\[
\gamma_i=p_i(m_G-t_i)\quad(i\in G),\qquad
B_G=\sum_{i\in G}\gamma_iA_i,\qquad
B_0=-\sum_{i\in Z}p_i y_i a_i,\qquad
d_0=E_2[b_2c].
\]

All three equations in (4) are now equivalent to (5) together with

\[
\begin{gathered}
M^Td_G=0\quad\text{for each group containing a nonzero residual},\\
M^Td_0=0\quad\text{if }Z\ne\varnothing,\\
\sum_G d_GB_G^T+d_0B_0^T=0.
\end{gathered}
\tag{6}
\]

For a nonzero group, a residual is nonzero precisely when its oriented labels `t_i` are mixed; then every residual in that group is nonzero. At such a state,

\[
\mathcal L=\sum_{i\in Z}p_i+
\sum_G W_G(1-m_G^2).
\tag{7}
\]

These are groups of **current coefficient vectors**, not groups of the original inputs. Equation (7) does not identify their positive contribution with the architectural loss floor.

For three inputs with all `v_i!=0`, the reduction is particularly sharp:

* Three separate signed-equality groups force fitting.
* A mixed group of two and a separate singleton forces the singleton to fit. For the pair, `gamma_1=-gamma_2!=0`; if its `d_G!=0`, middle stationarity forces `A_1=A_2`, in addition to `M^Td_G=0`.
* A mixed group of three has a common `d`. If `d!=0`, middle stationarity forces `sum_i gamma_i A_i=0`. Since the labels are binary, the weighted mean of the `A_i` with `t_i=+1` equals the weighted mean with `t_i=-1`. For three atoms this says that the lone member of one label class equals a strict convex combination of the other two (or they all agree). This is a condition on the lower feature coefficients, not on the original unit vectors.

With zero upper coefficients, (6) also covers cancellation between a mixed nonzero pair and a zero singleton. If both aggregate rank-one terms are nonzero, their left factors must be proportional and their right factors must be proportional with the opposite scale. Neither proportionality identifies the original inputs. If `rank M=2`, all residual-active left factors already lie on the single line `ker M^T`.

## 4. Exact lower-feature interpolation inside the finite-state class

The following construction ensures that the obstruction below is a state on the exact canonical carrier with bounded `w-g`, rather than a formal assignment of unrelated `a_i`.

For the independent axis inputs `u_j=e_j`, every sufficiently small triple of target vectors `A_j in R^6` is realizable as

\[
E_1[b_1\tanh(w_j)]=A_j
\tag{8}
\]

by an odd `w` with bounded `w-g`.

To prove this, write `b=b_1`, `G=E_1[bb^T]>0`, and let `B` be a finite bound on `|b|`. Define the odd Gaussian tail remainder

\[
r_R(g_j)=g_j-\operatorname{clip}(g_j,-R,R),\qquad
F_{R,j}(z)=E_1[b\tanh(r_R(g_j)+b^Tz)].
\]

As `R` tends to infinity, these maps converge uniformly on every bounded `z`-ball to `F_infty(z)=E_1[b tanh(b^Tz)]`; their derivatives converge uniformly there too. Indeed the integrands agree off the event `|g_j|>R`, are bounded by `2B` and `2B^2`, respectively, and that event has probability tending to zero. Moreover `D F_infty(0)=G`.

Choose a radius `rho>0` so small that

\[
\sup_{|z|\le\rho}
\|I-G^{-1}D F_\infty(z)\|\le\tfrac14.
\]

Then choose one finite `R` large enough for all three coordinates that

\[
\sup_{|z|\le\rho}
\|I-G^{-1}D F_{R,j}(z)\|\le\tfrac12,
\qquad |G^{-1}F_{R,j}(0)|\le\rho/4.
\]

For any targets satisfying `|G^{-1}A_j|<=rho/4`, the map

\[
T_j(z)=z-G^{-1}(F_{R,j}(z)-A_j)
\]

is a contraction of the closed radius-`rho` ball into itself: its Lipschitz constant is at most `1/2`, and `|T_j(0)|<=rho/2`. Iteration is Cauchy and its limit `z_j` solves `F_{R,j}(z_j)=A_j`. Set

\[
w_j=r_R(g_j)+b^Tz_j.
\tag{9}
\]

Then (8) holds exactly, and `|w_j-g_j|<=R+B rho`. Simultaneous negation of all lower Gaussian marks negates both summands in (9), so the lower state has the required odd parity. Every expectation in this argument uses the unchanged joint law of `(b_1,g)`; in particular it retains the correlated reverse marks.

## 5. Balanced, compatible, nonzero-factor critical state

Take

\[
u_1=e_1,\quad u_2=e_2,\quad u_3=e_3,
\qquad (p_1,p_2,p_3)=(1/4,1/4,1/2),
\qquad (y_1,y_2,y_3)=(+1,+1,-1).
\tag{10}
\]

The input vectors are independent; no pair coincides or is antipodal. Label mass is exactly balanced. This is an architecturally compatible law, with exact architectural loss floor zero by `architectural_loss_floor.md`. For these axes, zero floor also follows directly from the nonzero independent initialized upper features derived in `terminal_geometry.md` and an arbitrary fitted readout in their span.

Let `ell_1,ell_2,ell_3` denote distinct coordinate basis vectors of `R^6`. Choose `delta>0` small enough for (8) to give

\[
a_1=\delta\ell_1,\qquad a_2=-\delta\ell_1,\qquad
a_3=\delta\ell_1.
\tag{11}
\]

Select the finite full matrix

\[
M=\delta^{-1}(e_1\ell_1^T+e_3\ell_2^T).
\tag{12}
\]

It has rank two and gives `v_1=e_1`, `v_2=-e_1`, `v_3=e_1`.

Write the exact upper marks as `b_2=(X,Y,Z)`. They are independent, identically distributed, bounded symmetric variables whose common law has positive density on an interval around zero. Put

\[
H(X)=\tanh X,\qquad J(X)=X\operatorname{sech}^2X,
\qquad
z(X)=H(X)-\frac{E[H(X)J(X)]}{E[J(X)^2]}J(X),
\qquad N=E[z(X)^2].
\]

The denominator `E J^2` is positive. Also `N>0`: proportionality of `H` and `J` on the support interval would, by their linear Taylor coefficients, have proportionality constant one; their cubic coefficients are `-1/3` and `-1`, a contradiction. Hence

\[
E[zJ]=0,\qquad E[zH]=N.
\]

For any `kappa>0`, choose the bounded odd readout

\[
c=-\frac{z(X)}{2N}+\kappa Y.
\tag{13}
\]

Independence and symmetry give

\[
(f_1,f_2,f_3)=(-1/2,+1/2,-1/2),
\qquad
(\lambda_1,\lambda_2,\lambda_3)=(-3/8,-1/8,1/4).
\tag{14}
\]

All three gates in `d_i` equal `sech^2 X`, so all three upper derivative vectors are the same. Their first coordinate is `-E[zJ]/(2N)=0`; their second coordinate is `kappa E[Y^2]E[sech^2 X]>0`; and their third coordinate is zero. Thus

\[
d_1=d_2=d_3=d
=\kappa E[Y^2]E[\operatorname{sech}^2X]\,e_2\ne0,
\qquad M^Td=0.
\tag{15}
\]

Now verify every velocity directly:

\[
\sum_i\lambda_i h_i
=(-3/8+1/8+1/4)H(X)=0,
\]

\[
q_i=b_1^TM^Td=0\quad\text{for every }i,
\]

\[
\sum_i\lambda_i d_i a_i^T
=\delta(-3/8+1/8+1/4)d\ell_1^T=0.
\tag{16}
\]

Each individual `lambda_i d_i a_i^T` is nonzero. Each `a_i`, `d_i`, `v_i`, and residual is nonzero. Hence this is cancellation among three nonzero middle rank-one terms, with simultaneous exact readout and lower stationarity. Its unhalved physical loss is

\[
\mathcal L=\tfrac14(\tfrac32)^2+\tfrac14(\tfrac12)^2
+\tfrac12(\tfrac12)^2=\tfrac34.
\tag{17}
\]

Equations (9), (12), and (13) make this a finite state in exactly the existence norms of the canonical closure. It respects the canonical mark correlations, ridge, odd parity, full matrix state, actual transpose, and physical metric. All three blocks are stationary because their full equations vanish, not because any block has been removed from training.

The state is also a saddle, rather than a local minimum. The weighted Gram `H_1=E_1[b_1b_1^T sech^2(w_1)]` is positive definite: its quadratic form has a strictly positive gate, and the ungated Gram is positive definite. Change only `w_1` infinitesimally by the bounded odd function `b_1^T H_1^{-1} ell_3`; call this parameter direction `U`. Then its lower-feature variation is exactly `delta a_1=ell_3`, and `M delta a_1=0`. Choose the matrix direction `V=e_2 ell_3^T`. Its first upper-vector variations are zero because `ell_3.a_i=0`. Both parameter directions therefore have zero first prediction variation. Their pure second prediction variations are also zero: for `V` the upper vectors are unchanged along the entire straight line; for `U` the second derivative is `d^T M delta^2 a_1=0`, since the first upper-vector variation vanishes and `M^T d=0`. The mixed prediction derivative for sample 1 is `d^T V ell_3=d.e_2!=0`; all other mixed derivatives vanish because only `w_1` changes. Thus the loss Hessian has zero diagonal on `U,V` and nonzero mixed entry `2 lambda_1(d.e_2)`. Choosing the relative sign of these directions gives strictly negative second variation. This saddle property still does not exclude convergence to it from a specially prescribed trajectory.

## 6. Full-row-rank branch and endpoint limitation

Set `kappa=0` in (13) and replace (12) by

\[
\widetilde M=\delta^{-1}
(e_1\ell_1^T+e_3\ell_2^T+e_2\ell_3^T).
\]

The three upper vectors and predictions are unchanged, `rank M=3`, and all `d_i=0`. Readout cancellation remains (16), while lower and middle stationarity hold separately. This is a finite compatible positive-loss critical state on the zero-`d_i` branch. It is consistent with, and shows the sharpness of, the full-row-rank exclusion of nonzero residual-active `d_i`.

The rank-two construction defeats even the strengthened algebraic claim that nonzero rank-one cancellation, readout stationarity, lower stationarity, balanced labels, independent spherical inputs, bounded finite state, and loss below one together force an architectural conflict. It does not defeat a theorem specifically about endpoints reached from the prescribed initialization. Such a theorem needs an additional dynamically proved property excluding these collision/degeneracy states, or an argument that the initialized trajectory cannot converge to them. Rank preservation, absence of current lower-feature collisions, and avoidance of the relevant saddle sets have not been proved here.


## Display-only correction record

On 2026-09-18, after the independent report was frozen and reported, only the following display corrections were made: equation (11), restored the missing backslash on both `\qquad` commands; equation (15), changed the literal comma before `e_2` to the LaTeX thin-space command `\,`; equation (17), replaced all six literal-tab-plus-`frac` occurrences by `\tfrac`. No mathematical statements, constructions, or proofs were changed.

Original frozen SHA256: `f7866bb684590c525e73e7c867f69b0ff4285c12621a79312b8623d7c8a2d7f2`. The SHA256 of this corrected file, including this record, is reported to the supervisor separately to avoid a self-referential file hash.
