# Author audit of the H4 horizon route: weighted metrics and numerical limits

This is a bounded follow-up author check of the frozen
`H4_route_horizon.md`, not an independent promotion review. That route was
preserved byte for byte. No trajectory, experiment, code edit, or Git write
was performed. No other route or agent report was read.

The checked conclusion is affirmative: the fixed-order coupled estimate
(27) is valid at `T=40` for normalized joint mark/data laws with the stated
uniform feature, initial-row and matrix bounds. Singular raw feature Grams
and independent population replay do not invalidate it. Data `W1`, rather
than data `W2`, suffices. Two distinctions should be made explicit when the
route is assembled into a candidate:

* Rounded weights are finite measures whose masses need not be exactly
  one. Apply (27) after the precision limit, or use the mass-defect version
  (A8) below. Validation does not normalize the operational weights.
* The data contribution to a paired-law `W2` bound is generally of order
  `sqrt(W1)`. The state estimate can remain linear in `W1`. The frozen
  route's squared-transport argument already has this distinction, but a
  claim of a linear `W1` bound for the paired `W2` metric would require
  correction.

## 1. Exact maintained conventions

The relevant maintained implementation is `code/pde/observable_solver.py`.
It stores `(b1,g,w,p1)` and `(b2,c,p2)`, the current feature matrix `M`,
fixed initial matrix `D`, and arithmetic metadata. Its `_fields` routine
(lines 168–178) evaluates, with node weights retained literally,

\[
 a(u)=\sum_i p_{1,i}b_{1,i}\phi(w_i\cdot u),\quad
 h_{2,j}(u)=\phi(b_{2,j}^TMa(u)),\quad
 f(u)=\sum_jp_{2,j}c_jh_{2,j}(u),
\]
\[
 d(u)=\sum_jp_{2,j}b_{2,j}c_j\phi'(b_{2,j}^TMa(u)),\quad
 q_i(u)=b_{1,i}^TM^Td(u),\qquad\phi=\tanh.                 \tag{A1}
\]

The `rhs` routine (204–222) integrates the unhalved-loss equations against
the supplied data weights. Both action directions use the same `M` and
its transpose. There are no additional node-weight factors in the
coordinate velocities, because these velocities are gradients for the
weighted population metric, as checked in Section 2.

`paired_observations` (265–295) uses pair order `(initial,current)`.
Its initial lower feature is `phi(g_i·u)`; its initial upper feature is

\[
 h_{2,j}^0(u)=\phi\left(b_{2,j}^TD
                  \sum_i p_{1,i}b_{1,i}\phi(g_i\cdot u)\right).
                                                               \tag{A2}
\]

It retains the same lower/upper joint mark tuples in the initial and
current evaluations. The pair-entry weight is `p_l,i p_data,a`. The
returned RMS is the square root of the sum against these literal weights,
without normalization. `loss` likewise uses the literal data weights.

The data validator (27–64) permits a working-precision mass tolerance and
returns the original weights. State validation (127–145) checks population
weights with a corresponding tolerance and leaves them unchanged. These
tolerances approach zero with precision at fixed array dimensions. They
are not a projection onto exact probability measures. At a fixed finite
precision Heun evolution is not asserted to satisfy an exact GF energy
identity.

## 2. The energy metric is the weighted population metric

First use exact arithmetic and normalized positive measures. Let lower
weights be `alpha_i`, upper weights `beta_j`, and data weights `gamma_a`.
For `L=sum_a gamma_a(f_a-y_a)^2`, differentiation of (A1) gives

\[
 \partial_{w_i}L
  =2\alpha_i\sum_a\gamma_ar_a\phi'(w_i\cdot u_a)q_i(u_a)u_a,
\]
\[
 \partial_{c_j}L=2\beta_j\sum_a\gamma_ar_ah_{2,j}(u_a),\qquad
 \nabla_ML=2\sum_a\gamma_ar_ad(u_a)a(u_a)^T.                \tag{A3}
\]

For the first identity, differentiating `a` contributes `alpha_i`,
differentiating the upper activation/readout contracts to `d`, and
`b_1,i^T M^T d=q_i`. The matrix identity follows from
`delta f=d^T(delta M)a`; its Frobenius gradient is `d a^T`, with that
orientation. Thus the operational velocities are minus the gradients for

\[
 \|(v,z,V)\|_{\rm metric}^2
    =\sum_i\alpha_i|v_i|^2+\sum_j\beta_j|z_j|^2+\|V\|_F^2.
\]

Substituting the velocities into (A3) proves the exact identity

\[
 \dot L=-\sum_i\alpha_i|\dot w_i|^2
           -\sum_j\beta_j|\dot c_j|^2-\|\dot M\|_F^2.       \tag{A4}
\]

The population version follows by the same differentiation under bounded
integrands. It does not require orthonormal features, contraction of an
empirical feature map, or equality of the two population rules. There is
no factor `P`, `1/P`, or training atom count missing from the equations:
the factors are already in their measures. The matrix norm in (A4) is
Frobenius in the coefficients, not the HS norm of their lifted action.

If a supplied node has zero probability, its term in the energy identity
is zero; the identity still holds directly. One can omit that coordinate
from the probability space when interpreting the metric. Its prescribed
ordinary characteristic ODE can still be evaluated. Initializer weights
are positive in the exact finite rules and eventually positive in the
precision limit at fixed population count.

The differential identity remains algebraically valid in exact arithmetic
for nonnegative finite measures of nonunit mass: the same weights must
be used in the contractions, loss and metric. The initial bound then is
`L(0)<=mass(data) Y^2`, not `Y^2`. This observation does not assert an
energy identity for rounded arithmetic or a Heun step.

For normalized measures with `|b_l|<=K_l`, `|y|<=Y`, `c(0)=0`, (A4)
gives `int |r| dmu<=Y`, hence

\[
 \|c(t)\|_\infty\le2Yt,\quad
 |a|\le K_1,\quad |d|\le2YK_2t,
\]
\[
 \|M(t)-D\|_F\le2Y^2K_1K_2t^2,\quad
 \|w'(t)\|_\infty\le4Y^2K_1K_2t\|M(t)\|_F.                \tag{A5}
\]

These bounds close fixed-order existence in bounded increments `w-g`,
bounded `c`, and finite `M` on `[0,40]`. `g` itself need only be square
integrable. The right side is locally Lipschitz in these existence norms,
because the unbounded `g` enters only a bounded gate with bounded
derivative. The constants may depend on fixed order; no order-uniform
supremum estimate is used for the outer limit.

## 3. Complete coupled mark/data stability

Let two normalized lower joint laws for `(b_1,g)` be coupled by `pi_1`,
and let their two normalized upper mark laws be coupled by `pi_2`.
The lower coupling preserves each law's full `b_1,g` dependence. No
coupling of the two different layers is needed. Solve each system on its
marginal of the corresponding coupling space. Its marginal contractions
are exactly those of the original system, so this lift changes no equation.

Assume common finite bounds for `Y,K_1,K_2,||D||F,||g||2` and horizon `T`.
Bounds (A5) imply common bounds for `||w||2`, `||c||infty`, and `||M||F`.
Define on these couplings

\[
 e(t)=\|w-\widetilde w\|_2+\|c-\widetilde c\|_2
                         +\|M-\widetilde M\|_F,\qquad
 \rho_b=\|b_1-\widetilde b_1\|_2+\|b_2-\widetilde b_2\|_2.
\]

At a common input `u`, direct subtraction gives

\[
 |a-\widetilde a|
 \le\|b_1-\widetilde b_1\|_2+K_1\|w-\widetilde w\|_2.
\]

The identity

\[
 b_2^TMa-\widetilde b_2^T\widetilde M\widetilde a
 =(b_2-\widetilde b_2)^TMa
  +\widetilde b_2^T(M-\widetilde M)a
  +\widetilde b_2^T\widetilde M(a-\widetilde a)
\]

bounds the upper preactivation difference in `L2` by `C(e+rho_b)`.
The Lipschitz activation gives the same bound for `h_2`. Subtracting
`c h_2` gives the prediction bound. For `d`, subtract the three factors
`b_2,c,phi'(z_2)`; the first factor difference multiplies the bounded
`c`, and the gate difference is at most twice the preactivation
difference. Each integral is therefore at most `C(e+rho_b)`. Subtracting
`b_1^TM^Td` gives the same bound for `q` in lower `L2`. Also

\[
 \|q\|_\infty\le K_1\|M\|_F K_2\|c\|_\infty.             \tag{A6}
\]

In the lower drift the difference of its first gate times the unchanged
reverse query is at most `2||tilde q||infty ||w-tilde w||2`.
Subtracting the residual and reverse-query factors accounts for the other
terms. The upper drift is handled by the prediction/activation bounds.
For the matrix drift subtract `r d a^T` into its three factors and use
`||d a^T||F=|d||a|`. Consequently the same-law total drift difference
is bounded by `C(e+rho_b)`.

It remains to justify a *linear data-W1* term. At a fixed state,

\[
 \|\phi(w\cdot u)-\phi(w\cdot v)\|_2\le\|w\|_2|u-v|,
 \qquad |a(u)-a(v)|\le K_1\|w\|_2|u-v|.
\]

The upper field then has a pointwise input Lipschitz bound, since it
depends on the finite vector `a`; the same is true of `f,d,q` after
integration/evaluation, using `|b_l|<=K_l`. In the lower drift the
remaining changed gate costs at most
`2||w||2 ||q||infty |u-v|` in `L2`. The explicit terminal vector `u`
and the residual's label `y` contribute `C|u-v|` and `C|y-z|`.
Thus each velocity integrand is Lipschitz from the compact data space
to its respective `L2`/Frobenius space, with constant `C`.

For any coupling `pi_data` of the two training laws, the Bochner triangle
inequality gives the drift difference at a fixed state at most
`C int (|u-v|+|y-z|) dpi_data`. Taking infima over couplings proves a
`C W1` bound. This integrates data differences before taking the final
norm; it does not replace an `L2` data norm by an `L1` norm.

Subtract the two lifted integral equations. Their initial discrepancy is
`||g-tilde g||2+||D-tilde D||F`. The scalar integrating factor for
`e'<=C(e+rho_b+W1)` yields exactly

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 \|g-\widetilde g\|_2+\|D-\widetilde D\|_F
          +CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)\}\right]. \tag{A7}
\]

This confirms frozen equation (27). If mark laws approach in `W2`,
choose couplings with joint quadratic costs approaching zero; then the
two mark terms and initial-row term vanish. Different population node
counts and different node weights cause no problem, since this is a
coupling of laws and does not require matching raw node indices.

## 4. Rounded weights: an explicit mass-defect extension

For clarity write the three exact finite measures associated with
operational weights as

\[
 \alpha_l=s_l\lambda_l,\qquad\beta=s_d\mu,
\]

where `lambda_l,mu` are normalized probability measures and the masses
`s_1,s_2,s_d` lie in `[1/2,2]`. Normalizing here is solely a proof
decomposition. The operational fields still have the factors

\[
 a=s_1E_{\lambda_1}[b_1h_1],\quad
 f=s_2E_{\lambda_2}[ch_2],\quad
 d=s_2E_{\lambda_2}[b_2c\phi'(z_2)],
\]

and every velocity has the outside factor `s_d`. Those factors cannot
be dropped from the dynamics.

The exact finite-measure energy identity gives
`L(0)<=s_dY^2` and `int |r| dbeta<=s_dY`. It follows that
`||c||infty<=2s_dYt`, `|a|<=s_1K_1`, and
`|d|<=s_2K_2||c||infty`. Hence `M-D` and `w-g` obey finite bounds of
the form (A5), with constants enlarged uniformly for masses in `[1/2,2]`.
Repeating Section 3's product subtractions with these scalar factors adds

\[
 \Delta_s=|s_1-\widetilde s_1|+|s_2-\widetilde s_2|
                                     +|s_d-\widetilde s_d|
\]

to the right side. Using the normalized couplings for the `L2` norms,

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 \|g-\widetilde g\|_2+\|D-\widetilde D\|_F
       +CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)+\Delta_s\}\right].
                                                               \tag{A8}
\]

This is the version of (27) applicable to exact ODEs using nonnormalized
rounded weight arrays as fixed coefficients. It does not treat the
arithmetic roundoff of evaluating the RHS; that is removed separately.

At fixed finite `P` and data node count, rounding exact nonnegative weights
to the nearest multiple of `delta=10^-p` changes their total mass by at
most one half the node count times `delta`. The maintained `Fixed` scalar
uses exactly this nearest rounding. Subsequent sums of represented weights
are exact in that backend. Core/generic population probabilities computed
as `1/P` have the same bound. Exact finite positive masses therefore stay
positive and converge to one as `p->infinity`, and the normalized weight
vectors converge in total variation. For a fixed finite cloud, including
its unbounded-but-finitely-many `g` values, this also gives joint `W2`
convergence after direct coordinate convergence.

Rounded circle nodes can temporarily be off the exact circle. At fixed
finite input count they converge to the exact rational nodes and stay in
`|u|<=2`, with bounded labels. All field/subtraction estimates above remain
valid on that enlarged compact input set. Alternatively, normalize only
their locations for a proof coupling; the displacement is `O(delta)`.
Neither operation requires changing the operational data.

The asserted limit order removes `p` at fixed `N,epsilon,Q,P,m,J`.
There are finitely many algebraic/elementary operations, and their
positive denominator/pivot margins are fixed. The canonical H3 arithmetic
proof and the checked conversion/strict-pivot conventions give convergence
of that entire finite computation before any ODE or cubature limit is
taken. Therefore the original route can use (A7) only after this first
limit. It need not assert (A4), (A7), or exact normalization at the actual
rounded Heun states. Formula (A8) shows explicitly why the unnormalized
weights do not leave a residual obstruction if analyzed before that
limit. It gives no assertion for an arbitrary simultaneous growth of node
counts and precision.

## 5. Paired W2, RMS and risk under both refinements

Use the product coupling of the lower or upper joint mark coupling and a
training-law coupling. In each marginal, pair the same initial/current
feature at the same input; retain the joint initial marks in (A2).
The same-input current hidden difference is at most `C(e+rho_b)` in
`L2`; the initial difference adds
`C(||g-tilde g||2+||D-tilde D||F+rho_b)`. With finite-measure inputs it
also adds `C Delta_s` through (A2) and the current contractions.

For the data-only part, each fixed-state hidden field is Lipschitz in
input as an `L2` field, uniformly through `T`, by Section 3. Thus its
contribution to the squared pair transport cost is at most

\[
 C\int |u-v|^2\,d\pi_{\rm data}
       \le2C\int |u-v|\,d\pi_{\rm data}
       \le2C\int d_{\mathcal Z}((u,y),(v,z))\,d\pi_{\rm data}.
\]

The first inequality uses the diameter two of `S1`. After taking the
infimum and square root, this gives the precise bound

\[
 \sup_{t\le T}\mathcal W_2(\mathcal P_l(t),\widetilde{\mathcal P}_l(t))
 \le C\left[
 \sup_te(t)+\rho_b+\|g-\widetilde g\|_2+\|D-\widetilde D\|_F
                      +\Delta_s+\mathcal W_1(\mu,\widetilde\mu)^{1/2}
 \right],                                                   \tag{A9}
\]

where `P_l` uses normalized product measures. Here data `W1` is sufficient
for convergence. Its square-root loss is expected: transporting mass
`epsilon` between two fixed separated observations can cost order
`epsilon` in `W1` but order `sqrt(epsilon)` in `W2`.

Let `D_l(t)=H_l(t,u)-H_l(0,u)` on the coupled product space. The reverse
triangle inequality gives
`| ||D_l||2-||tilde D_l||2 |<=||D_l-tilde D_l||2`, so (A9)'s proof also
gives uniform convergence of normalized RMS, including at zero.
The code's literal weighted square displacement is

\[
 R_{l,\rm raw}^2=s_ls_dR_{l,\rm normalized}^2
\]

in exact arithmetic with its retained weights. Since `s_l,s_d->1` and
the hidden displacements are bounded by two, the raw and normalized RMS
have the same limit. Arithmetic evaluation errors in the reported square
root vanish in the first precision limit by continuity at every
nonnegative argument, including zero. Pair weights are normalized only
when interpreted as probability laws; the vector-field weights stay as
returned by the implementation.

The raw risk is `s_d int(f-y)^2 dmu`. Prediction error is uniformly
controlled by the field subtractions. If predictions and labels have a
common bound, the difference of squared residuals is bounded by a fixed
constant times prediction error. The fixed-state loss integrand is
Lipschitz in normalized input and label, so changing the normalized data
law contributes `C W1`; changing its mass contributes `C|s_d-tilde s_d|`.
Thus the same nested refinements give uniform-time risk convergence.

## 6. Conditioning and independent replay

There are two distinct positive regularizers; neither is removed at the
same point as the first precision limit.

**Feature Grams.** At fixed `N`, the ridge
`eta_N=1/[1024(N+1)^2]` is fixed and strictly positive. In exact arithmetic
an empirical or population raw Gram `G` is positive semidefinite even
with duplicated features. Hence `G+eta_N I>=eta_N I` and for its lower
Cholesky factor

\[
 \|L^{-1}\|_{\rm op}\le\eta_N^{-1/2},\qquad
 |b_l|\le B_l\eta_N^{-1/2},\quad
 D=L_2^{-1}CL_1^{-T}.                                     \tag{A10}
\]

These are the transforms implemented by `_normalize` at
`observable_initialization.py:298–303`. All transposes match the
column-feature convention. The fixed ridge gives continuous normalization
at a singular raw Gram; it provides no useful conditioning bound uniform
in `N`. `D` has a finite common bound whenever the finite raw contraction
`C` does. Initialization convergence supplies that bound at each fixed
order. The stability constant in (A7) may depend on (A10).

The replayed population Gram need not equal the Gram used for normalization,
and its normalized feature map need not be a contraction. This is harmless
for (A4)–(A9), which use only (A10) and common finite matrix/row bounds.
The contraction property needed for the *outer* horizon proof belongs to
the exact limiting initializer, after all these inner limits, not to
each numerical replay.

**Generic source Grams.** `GaussianCompiler._new_source` (407–439)
appends a new row while retaining all old operand values and factors.
At exact finite cubature its covariance prefix is the empirical operand
Gram plus `epsilon I`, because cross entries are computed from those
same retained operand tables and `epsilon` is added to each new
diagonal. Thus it is strictly positive definite at fixed `epsilon>0`,
even for duplicated/zero operands. The exact Cholesky pivots are positive;
arithmetic may reject unresolved pivots but does not remove a direction.
At fixed finite parameters, sufficiently fine precision resolves them.
At fixed `epsilon`, initializer cubature convergence and continuity of
the positive-definite Cholesky map give the stated coefficient limit.

Removing `epsilon` can make the limiting source Gram singular. The
canonical proof uses continuity of its positive semidefinite square root
and polynomial Gaussian envelopes to couple complete named source
vectors, then inducts through the finite expressions and response
expectations. This does not require a Lipschitz matrix square root,
continuous singular Cholesky factors, or a positive lower eigenvalue
after regularizer removal. Named zero-variance derivatives remain in
that argument. Section (A7) requires only the resulting mark-law `W2`
convergence and `D` convergence, not stable source factors themselves.

**Independent replay.** The core initializer computes scalar coefficients,
Grams and contractions on its `Q` cloud, releases those value tables, then
replays complete joint tuples on `P` points with the scalar coefficients
fixed (`observable_initialization.py:331–356`). The generic compiler
likewise freezes its source factors and response coefficients; `_at_count`
(441–465) replays the entire DAG and `compile_raw_dictionary` (488–529)
uses `Q` for `G,C` and `P` for the joint marks. No coefficient is refitted
on the replay cloud. When `P=Q`, reusing the existing cloud is the same
fixed-map rule.

For fixed coefficients this replay is a finite continuous Gaussian map
with the moment control proved in H3.C.2. Its empirical joint law,
including lower `g`, therefore converges in `W2`. When `Q` changes,
the H3 Gaussian integration argument allows coefficients estimated on the
same earlier integration cloud to vary and proves their convergence;
joint mark convergence follows in the prescribed later limits. Independence
of the two population indices is not a missing neural coupling: all
same-layer coordinates use a common point, while all cross-layer
contractions use the two separate population expectations. No claim about
cross-layer paired neuron indices enters (A7) or (A9).

The reverse raw contraction is only a diagnostic in the maintained generic
initializer. The operational `D` uses the forward raw contraction and its
transpose, as required for (A3). The proof does not average independently
estimated forward and reverse matrices or assume the finite regularized
source program is already the exact canonical action law.

## 7. Outcome and provenance

The fixed-order energy, stability and observation bridges used by the
frozen horizon route are confirmed for their exact intended nested limit.
No scientific correction to that route's time-40 conclusion was found.
For assembly, explicitly retain (i) the weighted metric (A4), (ii) the
probability-mass qualification or correction (A8), and (iii) the square-root
data term in the paired bound (A9). Do not apply the exact-law stability
inequality directly to unnormalized floating/rounded arrays, and do not
assume replay contraction or a uniform source/feature eigenvalue gap.

Actual read scope for this follow-up:

* Current `AGENTS.md` and `RESEARCH_WORKFLOW.md`; required proof/research
  skills remained those already read for the horizon route.
* The previously read, unchanged canonical scope: `docs/NOTATION.md` and
  `docs/global_nonlinear.md` C.4.7.1–5, .7–10. The relevant numerical
  analytic dependencies are H3.C.2–5, already read completely.
* `code/README.md` lines 1–132 and 623–940, including the complete H3
  API/initialization/evolution/precision/observation guide. A broad initial
  read was truncated and replaced by these complete relevant sections.
* Complete `observable_solver.py`, `observable_initialization.py`, and
  `observable_arithmetic.py`.
* `observable_compiler.py` lines 94–158 and 280–529, covering constructor,
  finite source evaluation, frozen named-source AD, source append, replay,
  and raw dictionary compilation. Graph canonicalization/resource routines
  outside those ranges were not audited.
* `observable_fixed.py` lines 1–170, covering exact nearest conversion,
  arithmetic weight operations, comparisons and square root. The remaining
  elementary algorithms were not reread; their analytic convergence proof
  remains the complete H3.C.4 already in scope.

No new scientific source was fetched beyond those reported to the
supervisor before retrieval. No maintained tests were run because this
assignment was a direct mathematical and convention audit without
trajectories. This is not a complete software review of all solver
dependencies or a numerical reproduction claim. Only metadata status
checks were made for shared-write safety; no index, branch or commit was
changed. The observed HEAD was
`e32496236aefb04985f00dcf7f421f19043dda22`.

Input SHA-256 values at the audit read/check point:

| Input | SHA-256 |
|---|---|
| Frozen `H4_route_horizon.md` | `b8a708c30802e2fb4d84267a20a76e32724cdc9c33b33e61e986ec9aa6859efe` |
| `docs/global_nonlinear.md` | `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932` |
| `code/README.md` | `30135209fc7bfba9125078cf12efeb1c46471da8979dc0893d59cb8a5691658b` |
| `observable_solver.py` | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `observable_initialization.py` | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `observable_arithmetic.py` | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `observable_compiler.py` | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `observable_fixed.py` | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |

Outcome: **author-confirmed proof supplement, ready for independent
checking**. This does not replace the repository's fresh review requirements.
