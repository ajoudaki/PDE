# Current Gaussian readout–preactivation closure

2026-09-30. Frozen candidate B, scoped independent derivation. Allowed scientific
inputs actually read: `CUBIC_ENERGY_REPAIR_ROUTE_20260930.md`,
`CUBIC_DENSE_DIAGNOSTIC_20260930.md`,
`CUBIC_FEEDBACK_REPAIR_RESULTS_20260930.md`, and `docs/notation.qmd`.
The rigorous mathematics skill and shared research process were applied. No
sibling draft, other study, external scientific source, fitted trajectory, or
training run was used. This is an explicitly approximate moment closure with
proved internal identities, not a fidelity theorem or promoted result.

The candidate retains a current readout–preactivation correlation vector and
preactivation covariance, instead of multiplying the previous fixed response
by another diagonal gate. The covariance form has `1+m+m(m+1)/2` training states; the implemented
exact transport form has `m^2+m` states and **zero query states**. Its positivity,
loss, readout energy, bounded outputs, and training aliases are exact internal
properties. It discards higher Gaussian Hermite modes of the initial tanh
feature kernel and freezes an isotropic hidden mobility. Both are substantial
approximations; the initial weak-mode defect must be inspected before fitting.

## Exact dense equations and the unclosed correlations

Write `alpha=2/m`, `r=f-y`, `h1_a=tanh(z1_a)`, `h_a=tanh(z_a)`, where
`z1_a=W1 x_a/sqrt(d)` and `z_a=W h1_a`. Let `c` be the stored readout,
`d1_a=1-h1_a^2`, `d_a=1-h_a^2`, and `G_ab=x_a.T x_b/d`. The circle
implementation instead uses `z1=W1 x` and hence `G_ab=x_a.T x_b`; the
initializer takes this input scaling explicitly. All vector products inside
`diag` or `odot` are coordinatewise. A bracket below is the finite upper-layer
average `v.T w/n` or `mean` of a scalar-valued upper-layer expression.

The canonical mobilities `(n,1,n)` give exactly

\[
 \dot c=-\alpha\sum_b r_b h_b,\qquad
 \dot z_a=-\alpha\sum_b r_b\mathcal M_{ab}(c\odot d_b),
\]
\[
 \mathcal M_{ab}=K^{(1)}_{ab}I+
 G_{ab}W\operatorname{diag}(d1_a\odot d1_b)W^T,
 \qquad K^{(1)}_{ab}=h1_a^Th1_b/n.                 \tag{1}
\]

Indeed `Wdot=-alpha sum_b r_b(c odot d_b)h1_b.T/n` gives the first
term; `W h1dot_a` gives the second. Thus both hidden-block mobilities are
present before closing. The operator is current and is not in general a
scalar times the identity.

Define the exact uncentered moments

\[
 q=\langle c^2\rangle,\quad u_a=\langle cz_a\rangle,
 \quad V_{ad}=\langle z_a z_d\rangle.               \tag{2}
\]

Their exact dense evolution is

\[
\begin{aligned}
 \dot q&=-2\alpha\sum_b r_b\langle c h_b\rangle,\\
 \dot u_a&=-\alpha\sum_b r_b\{
       \langle z_a h_b\rangle+
       n^{-1}c^T\mathcal M_{ab}(c\odot d_b)\},\\
 \dot V_{ad}&=-\alpha\sum_b r_b\{
       n^{-1}z_d^T\mathcal M_{ab}(c\odot d_b)+
       n^{-1}z_a^T\mathcal M_{db}(c\odot d_b)\}.
\end{aligned}                                                    \tag{3}
\]

These are not closed: `(q,u,V)` does not determine tanh moments or the
current operator. Merely storing (2) is not an exact finite reduction.

## The two explicit closures

First replace the current block operator by `A_ab I`, with **one frozen**
positive semidefinite matrix

\[
 A_{ab}=K^{(1),0}_{ab}+G_{ab}J^0_{ab},\qquad
 J^0_{ab}=\frac1n\sum_j d1^0_{j,a}d1^0_{j,b}
                            \sum_i W^0_{ij}{}^2.                \tag{4}
\]

This is the exact initial normalized trace of (1). It keeps the initial
column norms, rather than replacing them by their expectation. Each term is
a Gram or a Schur product of Grams, so `A` is positive semidefinite. Equation
(4) includes a contribution from first-layer training but does **not** track
its later anisotropy or feature Gram. No assertion that this discarded
information is negligible is made.

Second close the centered joint law of `(C,Z_1,...,Z_m)` by a Gaussian with
covariance

\[
 \Sigma=\begin{pmatrix}q&u^T\\u&V\end{pmatrix}.
\]

The finite initialization may have nonzero empirical preactivation means;
regarding its uncentered second moment as a centered Gaussian covariance
is another part of this approximation. Start with `q=u=0` and
`V_ab=(z_a^0).T z_b^0/n`. The model receives no finite readout noise.

For an exact Gaussian define

\[
 s(v)=\mathbb E[\operatorname{sech}^2(\sqrt v\,\xi)],\quad
 t(v)=2s'(v)=\mathbb E[4\operatorname{sech}^2(\sqrt v\xi)
                         -6\operatorname{sech}^4(\sqrt v\xi)],
 \quad \xi\sim\mathcal N(0,1).                                  \tag{5}
\]

Integration by parts against the one-dimensional Gaussian density proves
`E[C tanh Z_a]=u_a s(V_aa)`. Repeating it twice gives

\[
\begin{aligned}
 E[Z_a\tanh Z_b]&=V_{ab}s_b,\\
 E[C^2\operatorname{sech}^2 Z_b]&=q s_b+u_b^2 t_b,\\
 E[C Z_d\operatorname{sech}^2 Z_b]&=u_d s_b+u_b V_{db}t_b,
\end{aligned}                                                     \tag{6}
\]

where `s_a=s(V_aa)` and `t_a=t(V_aa)`. All boundary terms vanish since
tanh and its derivatives are bounded and a polynomial times a Gaussian
density decays at infinity. These formulas retain current mixed correlations;
setting `u=0` in the weighted gate term discards them.

Substitute (6) into (3), after (4), and set `f_a=u_a s_a`. The resulting
autonomous ODE is

\[
\begin{aligned}
 \dot q&=-2\alpha\sum_b r_b f_b,\\
 \dot u_a&=-\alpha\sum_b r_b\{V_{ab}s_b+
                          A_{ab}(q s_b+u_b^2t_b)\},\\
 \dot V_{ad}&=-\alpha\sum_b r_b\{
 A_{ab}(u_d s_b+u_b V_{db}t_b)+
 A_{db}(u_a s_b+u_b V_{ab}t_b)\}.
\end{aligned}                                                     \tag{7}
\]

These are covariance projection equations. A Gaussian law is not invariant
under the original nonlinear particle flow. Equations (7) continuously
replace the generated non-Gaussian law by the specified Gaussian ansatz.

## Why the surrogate has a positive loss kernel and exact energy

A constructive check also avoids relying on a Gaussian moment closure to
preserve positivity by accident. Represent the covariance, for this proof
only, as the Gram of abstract Euclidean vectors `b,v_1,...,v_m`:
`q=||b||^2`, `u_a=b.T v_a`, `V_ad=v_a.T v_d`. No such vectors are stored by
the implementation. For the prediction `f_a=u_a s(V_aa)`, its gradients are

\[
 \nabla_b f_a=s_a v_a,\qquad
 \nabla_{v_a}f_a=s_a b+u_a t_a v_a=:p_a.            \tag{8}
\]

The gradient flow with readout mobility one and feature mobility `A` is

\[
 \dot b=-\alpha\sum_a r_a s_a v_a,\qquad
 \dot v_a=-\alpha\sum_b A_{ab}r_b p_b.             \tag{9}
\]

Taking the three Gram derivatives gives exactly (7). Thus `Sigma` stays
positive semidefinite. Differentiating the predictions yields

\[
 \dot f=-\alpha\Theta r,\qquad
 \Theta_{ab}=s_as_b V_{ab}+A_{ab}B_{ab},
\]
\[
 B_{ab}=q s_as_b+s_a u_b^2t_b+s_bu_a^2t_a
                         +u_au_b t_at_bV_{ab}=p_a^Tp_b.          \tag{10}
\]

Both terms of `Theta` are positive semidefinite: the first is a diagonal
congruence of `V`, and the second is a Schur product of two Grams (equivalently
its entries are pairings of tensor products). Therefore

\[
 \frac{d}{dt}\frac{\|r\|^2}{m}
   =-\frac4{m^2}r^T\Theta r\le0,\qquad
 \dot q=-\frac4m r^Tf.                             \tag{11}
\]

`B` is a Gram of **projected** backward signals (8), not the exact Gaussian
moment `E[C^2 sech^2 Z_a sech^2 Z_b]`. Confusing those two quantities would
produce a different and generally inconsistent kernel. The projection
has a precise variational interpretation and supplies one current
backward-correlation channel instead of a mean-gate factorization.

For the exact Gaussian link, `|f_a|^2<=q E[tanh^2 Z_a]<=q`. The numerical
link below has the same bound exactly, up to arithmetic. At `r=0` all
training and query derivatives vanish. These statements do not imply a
small error against the original dense trajectory.

## Frozen scalar special-function evaluator

A runtime multivariate population quadrature is unnecessary. Only the one
scalar function (5) and its derivative are needed. The implementation uses
128 Gauss–Legendre nodes on `[0,12]` for the positive half-normal measure,
normalizes the positive weights to sum to one, and rescales the nodes to
have weighted second moment one. These nodes evaluate a univariate link;
no node carries a neural state, evolves in time, represents a joint sample,
or stores a training/query-dependent feature dictionary.

To make gradient identities exact even for this numerical approximation,
the implemented link is defined by the finite formula

\[
 s_J(v)=\sum_{j=1}^J w_j\xi_j\frac{\tanh(\sqrt v\xi_j)}{\sqrt v},
 \qquad t_J(v)=2s_J'(v),\quad s_J(0)=1,\quad
 t_J(0)=-\tfrac23\sum_j w_j\xi_j^4.                \tag{12}
\]

The Gaussian integration-by-parts identity identifies the limit with (5).
The finite formula (12), including its derivative, is the frozen numerical
candidate; use it everywhere in (7)--(10). Its small-argument removable
singularities are evaluated by convergent local scalar formulas, solely as
special-function evaluation, not as a Taylor approximation of the neural
feature trajectory. There is no increase in feature-response Taylor order.

Cauchy–Schwarz gives `v s_J(v)^2 <= sum_j w_j tanh^2(sqrt(v)xi_j)<=1`.
Together with `u_a^2<=q V_aa`, this proves the output bound for the finite
formula too. The tangential and radial eigenvalues of the derivative of
`v_a s_J(||v_a||^2)` are `s_J` and
`sum_j w_j xi_j^2 sech^2(sqrt(V_aa)xi_j)`, both in `[0,1]`.
Thus (9) has `||p_a||<=sqrt(q)`. Loss bounds the residual; (11) bounds
`sqrt(q)` by a function growing at most linearly on finite intervals; (9)
then bounds all feature-vector norms on finite intervals. The finite-link
ODE is globally well posed from its positive semidefinite initial covariance.
This is a surrogate existence argument, not a dense approximation theorem.

The retained 128-node scalar evaluation costs `O(Jm)` per training RHS and
`O(J)` per requested output. Accuracy is checked against 256 nodes and direct
one-dimensional integration. This numerical integration cost is disclosed;
the procedure is not an elementary rational closed form. No hidden growing
population or width enters the training vector field.

## Passive query equations and exact aliases

For a query `x`, initialize its row `A_xb` by (4), and add
`u_x`, `V_xb` (`b=1,...,m`), and `V_xx`. These are `m+2` passive scalars in the covariance representation only.
The exact transport construction below eliminates their integration. Start from its exact initial preactivation Gram and `u_x=0`. Its ODE is

\[
\begin{aligned}
 \dot u_x&=-\alpha\sum_b r_b\{V_{xb}s_b+
                      A_{xb}(q s_b+u_b^2t_b)\},\\
 \dot V_{xa}&=-\alpha\sum_b r_b\{
 A_{xb}(u_a s_b+u_bV_{ab}t_b)+
 A_{ab}(u_x s_b+u_bV_{xb}t_b)\},\\
 \dot V_{xx}&=-2\alpha\sum_b A_{xb}r_b
                         (u_x s_b+u_bV_{xb}t_b),\\
 \widehat f_x&=u_x s_J(V_{xx}).
\end{aligned}                                                     \tag{13}
\]

These follow by giving `v_x` the same passive evolution
`vdot_x=-alpha sum_b A_xb r_b p_b`. Hence the augmented covariance is a
Gram, `|f_x|^2<=q`, and the training ODE is independent of all query states.
When `x=x_a`, identical initialization and static rows give identical
state derivatives; uniqueness proves aliases. The covariance equations alone would require co-integrating every query.
The following transport identity supplies a fixed-state decoder without
changing those query trajectories. Antipodal inputs have odd outputs under
the corresponding initial and mobility signs.

## Exact transport eliminates all passive query states

After the covariance candidate was frozen, the supervisor supplied an exact
representation improvement before any fitting. This is the same vector field
and query evolution, not another candidate or an additional closure. Assume
`A` is positive definite; the implementation checks this and discards no
positive eigenvalue. Query decoding inherits the conditioning of this fixed
solve. The derivative and covariance construction itself also make sense for
semidefinite `A`, but that extension is not the frozen implementation.

Let `F` have the initial abstract vectors as columns. Since (9) is linear in
`b` and the `v_a`, their span stays within the initial training span. Write

\[
 (v_1,\ldots,v_m)=FR,\quad b=F\beta,\quad F^TF=V^0,
 \qquad R(0)=I,\quad\beta(0)=0.
\]

The aggregate equations are

\[
 \dot R=-\alpha\{\beta(r\odot s)^T+
                 R\operatorname{diag}(r\odot u\odot t)\}A,
 \qquad\dot\beta=-\alpha R(r\odot s),                 \tag{15}
\]

and the current correlations are decoded exactly by
`q=beta.T V0 beta`, `u=R.T V0 beta`, `V=R.T V0 R`.
`R` retains initial/current correlation information; when `V0` is invertible,
`R=(V0)^(-1) E[Z^0 Z^T]`. This interpretation is optional and no evolving
inverse is used. The implementation stores `R,beta`, not `F`, Gaussian
samples, neurons, or pointwise activation dictionaries. Its nonlinear link
acts on aggregate variances, rather than on the entries of `R`.

For any initialized query, let `ell_x=A^(-1) A_x` and
`d_x=(R-I)ell_x`, with `k0_x=E[Z^0 Z_x^0]`. Then

\[
 v_x=v_x^0+F d_x,\quad
 u_x=\beta^T(k0_x+V^0d_x),\quad
 V_{xx}=V^0_{xx}+2k0_x^T d_x+d_x^T V^0d_x.              \tag{16}
\]

Indeed `vdot_train ell_x=-alpha sum_b A_xb r_b p_b=vdot_x`, and the
initial values agree. Thus (16) differentiates to (13). At a training alias,
`ell_x=e_a`, so (16) gives exactly the training covariance and output.
No query states, saved training history, or final interpolation correction
are needed. Only the original static query contractions are required.
An entirely new query still requires its initialization contractions; this
construction does not turn the finite initial weight realization itself
into a width-independent function oracle.

## Initialization defect and costs

At zero readout the new training kernel is

\[
 K_{\rm lin,0}=\operatorname{diag}(s_J(V^0_{aa}))V^0
                         \operatorname{diag}(s_J(V^0_{aa})),     \tag{14}
\]

not the initial tanh Gram `K0`. For an actually Gaussian `Z`, write
`tanh Z_a=s(V_aa)Z_a+epsilon_a`. Gaussian integration by parts gives
`E[epsilon_a Z_b]=0`, and therefore
`K_tanh=K_lin+E[epsilon epsilon.T]`. The discarded higher Hermite modes
have a positive semidefinite Gram. Their relative size can be large in the
weakest clustered direction even when the overall norm change is small.
At finite empirical initialization there is also a Gaussian-law error, so
`K0-Klin` need not be positive semidefinite. The constructor reports both
the full relative change and the Rayleigh ratio in the weakest `K0`
eigendirection, as well as the residual Gram and regression cross defect.
No claim of preserved initial cubic response is made.

The implemented dynamic storage is `m^2+m`, independent of query count.
Training static storage is `O(m^2+J)` including the scalar quadrature rule.
A training RHS uses `O(m^3+Jm)` arithmetic with dense matrix products. Each
query needs `O(m)` static coefficients (`A_x`, its solve, `k0_x`, and
`V0_xx`) and `O(m^2+J)` output work, with **zero dynamic scalars**. Batched
`Q`-query decoding uses `O(Qm^2+QJ)` work and `O(Qm+QJ)` temporary memory;
no pairwise query covariance is stored. Queries never enter the RHS.

Initialization from width-`n` weights uses `O(n^2 m+n d m+n m^2)` work
for training (including the initial upper preactivations) and `O(n^2+n m)`
per query, plus reading `O(n^2+nd)` weights. It may use `O(nm+n^2)` temporary
storage and releases all neurons and weights before returning the model.
Static coefficients and their hashes are sufficient to reproduce its RHS.
No targets except the training labels are read.

## Frozen implementation and status

The supervisor authorized the additional implementation files
`current_gaussian_correlation.py` and
`check_current_gaussian_correlation.py` after the derivation was selected.
API: `initialize_with_queries(w,W,inputs,labels,queries,input_scale=1)`;
the returned model has `initial_state`, `rhs`, `residual`, `predict`,
`diagnostics`, `coefficient_dict`, `blocks`, `size`, `training_size`, and
JSON-compatible `metadata`. `from_coefficients` reconstructs the same model
with its saved quadrature nodes and weights. `RadialTanhLink.evaluate`
exposes the link for separate same-state diagnostics. This document freezes exactly one candidate;
there is no matched fit, coefficient selection, or alternate initialization.

Only deterministic non-training checks are authorized for this subagent:
scalar expectation accuracy, covariance derivatives against (9), loss and
energy identities, positive kernels, query independence, and aliases.
The supervisor owns any fitting decision and its bounded protocol. An
accurate fit or improved unseen circle discrepancy remains an open empirical
question. Failure can arise from initial Hermite loss, frozen isotropic
hidden mobility, or departure from the Gaussian ansatz; it would reject
this candidate, not prove that every finite current-correlation closure fails.


### Deterministic check result

Executed with `OPENBLAS_NUM_THREADS=1 python
studies/structured_full_rank_scalar_20260926/check_current_gaussian_correlation.py`.
No ODE integration or training was performed. The check passed in 0.032 seconds
on this run. Across twelve deterministic generic transport states, covariance
and query derivative discrepancies were at most `1.67e-16`; energy derivative
error was `1.67e-16`; prediction/kernel derivative error was `7.63e-17`;
physical alias and antipodal errors were `1.67e-16`; no bound violation was
observed, and the smallest checked kernel eigenvalue was `0.00866`.
The finite-difference output-gradient check differed by at most `1.27e-10`.
Training/query independence and saved-coefficient roundtrips were bitwise
exact for the checked inputs. The initial operator trace agreed within
`2.23e-16` with its literal finite-network evaluation.

For fifteen declared variances between zero and 1000, direct adaptive scalar
integration gave maximum absolute errors `3.47e-14` for `s` and `2.19e-13`
for `t`; the 128/256-node discrepancy was `8.31e-14`. This finite grid is
not a certified uniform quadrature theorem. Endpoint diagnostics repeat the
128/256 comparison at actual variances, so departure from the checked range
or unexpected scalar integration error remains visible. Positive weights,
unit second moment, and use of the exact derivative of the finite link retain
the algebraic gradient and output-bound properties independently of its
closeness to the exact Gaussian expectation.

The implementation and source check are internally checked for these
identities only. Dense fidelity, success at fitting, and unseen-circle
improvement remain untested in this subagent's work.
