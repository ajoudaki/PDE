# Direct source/energy route for three inputs and three hidden layers

2026-09-08. Independent bounded investigation of the original L3 odd-mixture target. No existing proof files changed and no experiments performed.

## Scope and verdict

The activation is `phi(z)=a z+e atan(z)`, `a=1-e`, `0<e<=1/2`, in all **three** hidden layers, with the original raw metric, initialized bounded actions, zero population readout, and three RMS-unit inputs with pairwise absolute correlations at most `1-delta`. This note does not change the architecture, add an offset, assume a nonsingular input Gram, freeze hidden weights, or modify the target dynamics.

The new directory `three_sample_odd_activation_depth2` contains only `CONTRACT.md` at the time of inspection; it supplies no proved source/energy method to transfer. The existing three-input analysis correctly leaves the full odd-mixture theorem open.

**This route proves no horizon-independent positive interval of amplitudes e.** In particular it presently gives no sufficient polynomial `e<=c delta^p`, no stretched-exponential alternative, and no positive existential `e_delta` for the complete original theorem. This is a limitation of the argument, not a counterexample to the positive-e statement. The inverse-free Gaussian regression lemma below is a useful additional exact fact, but its conclusion is L2 control and does not fill the strong-continuation/source-tail gap.

## 1. Exact conditional energy information

Use the population parameter Hilbert space and scalar predictor differentiability from Appendix C, Part F, Theorem F.7 of `odd_mixture_separation_quantitative/REPORT.md`. For an already constructed true strong GF, the chain rule gives

\[
 L'(t)=-\|\dot\Theta(t)\|_{\rm raw}^2.
\]

Consequently, for `0<=s<t<=T` in its existence interval,

\[
 \|\Theta(t)-\Theta(s)\|_{\rm raw}
 \le \sqrt{(t-s)\{L(s)-L(t)\}}
 \le\sqrt{(t-s)L(0)}.                                      \tag{1}
\]

Here Cauchy--Schwarz applies to the Bochner integral of the strong derivative; the energy identity supplies its square-integral norm. In particular

\[
 \sup_{t\le T}\|\Theta(t)-\Theta(0)\|_{\rm raw}
 \le\sqrt{TL(0)}.
\]

With `L(0)=3/2` and initialized action norms at most 10, write `R_T=sqrt(3T/2)` and `B_T=10+R_T`. Each action norm is at most `B_T`; the first-weight and readout increments are bounded by `R_T`. Since `|phi(z)|<=|z|` and `|phi'(z)|<=1`, forward and incoming L2 norms are bounded by explicit polynomials in `B_T`. Thus all Gaussian innovations of any already identified finite query program have bounded variances on such a ball.

If the existence interval has a finite endpoint T, (1) makes the raw state Cauchy as `t` approaches T. Completeness supplies a strong state limit. Continuity of the scalar gradient at that limit supplies a limit of the vector field along the curve. This gives a candidate endpoint with the correct state and limiting derivative. It does **not** furnish a new uncut solution from that state: the supplied theorem proves continuity, not local Lipschitzness, of the uncut Hilbert vector field.

At finite width the vector field is smooth, so the same length bound does give global existence. That finite-dimensional continuation implication cannot simply be reused in the Hilbert population space.

The incoming-field regularization used in Part F is locally Lipschitz, but it is not the gradient of the original loss. Therefore (1) cannot be assigned to its capped reference paths without a separate argument. A smooth finite-dimensional/Galerkin loss regularization does preserve energy, but its bounds supply weak compactness and time equicontinuity; they do not identify nonlinear action/Nemytskii limits strongly.

## 2. An exact inverse-free regression bound

Let `H` be a real Hilbert space, `u_1,...,u_m` elements of H, and let `U:R^m->H` be `Uc=sum c_j u_j`. Put `Sigma=U*U`, and let `G~N(0,Sigma)`. For a scalar function F with square-integrable value and integrable formal first derivatives, assume Gaussian integration by parts is justified. This is true for the fixed capped finite programs under examination, and may be proved by the existing bounded-derivative truncation for individual admissible observations. Set

\[
 d=E\nabla F(G).
\]

Extra random arguments independent of G may be included in F. Gaussian integration by parts gives

\[
 E[G F(G)]=\Sigma d.                                       \tag{2}
\]

The random linear variable `d^T G` is the orthogonal projection of F onto the finite Gaussian linear span `{b^T G:b in R^m}`: for every b,

\[
 E[(F-d^TG)b^TG]
 =b^T(E[GF]-\Sigma d)=0.
\]

Thus

\[
 \boxed{\quad
 \|Ud\|_H^2=d^T\Sigma d
       =\|d^TG\|_{L^2}^2
       \le \operatorname{Var}(F)\le E F^2.
 \quad}                                                   \tag{3}
\]

The centering in the penultimate inequality is legitimate because every `b^T G` has mean zero. No inverse or lower eigenvalue bound is used; singular Sigma is allowed.

This has the precise form of an actual initialized matrix response. The covariance of a named Gaussian source family is the Gram of the corresponding query fields, and the response is `sum_j u_j E partial_{G_j} F`. Its **combined L2 norm** is therefore bounded by the L2 norm of F. This is stronger and more accurate than claiming that singular named-source slots by themselves make Gaussian regression unusable.

If d is changed by a vector in `ker Sigma`, the combined response is unchanged, since `||U v||^2=v^T Sigma v=0`. Formal derivatives off Gaussian support need not be identified individually to recover this combined Hilbert vector. At a fixed finite program, the pseudoinverse formula can describe the same projection, although it is unnecessary for (3).

## 3. What regression does not control

### 3.1 No coefficient or absolute-row control from L2 field norms

For `Sigma=diag(1,epsilon^2)` and `F(x,y)=y/epsilon`, one has `||F(G)||_2=1` but `d_2=1/epsilon`. Hence recovering a derivative coefficient from L2 data costs the inverse square root of a covariance eigenvalue. For `Sigma=diag(1,0)`, the functions `F_k(x,y)=k y` all vanish on the Gaussian support and yet have arbitrary second formal derivative coefficient k. The latter ambiguity cancels in `Ud`, as explained above, but rules out bounds on separately named derivative rows based solely on F's realized L2 law.

Pairwise separation of the **three initial spatial inputs** supplies no positive lower bound for the minimum eigenvalues of the **arbitrarily long temporal query Grams** as the time mesh is refined. Near repeated times, even a smooth nonstationary query path produces nearly dependent columns. Therefore pseudoinverse coefficient estimates do not produce the required mesh-independent absolute response rows.

### 3.2 An L2-isometric response transfer need not preserve any higher moment

The map `d^TG -> Ud` is an L2 isometry between a Gaussian linear span and a span of actual query fields. It need not be bounded from Lp to Lp, even if Sigma is perfectly conditioned and every individual query field is uniformly bounded.

Here is an explicit finite example. Let Omega be the N-point probability space with N a power of two, and let `u_1,...,u_N` be all Walsh characters, normalized so they take values in `{+1,-1}` and are orthonormal in L2. Choose the indexing/signs so every `u_j` equals 1 at one distinguished point. Define

\[
 v_N=N^{-1/2}\sum_{j=1}^N u_j.
\]

Character orthogonality implies that `v_N` is `sqrt(N)` at that point and zero at every other point. Hence

\[
 \|v_N\|_2=1,\qquad
 \|v_N\|_p=N^{1/2-1/p}\quad(p>2).                         \tag{4}
\]

Take independent standard Gaussian `G_1,...,G_N` and `F=N^{-1/2}sum_j G_j`. Then `||F||_2=1`, F is standard Gaussian, `d_j=N^{-1/2}`, and the combined response is exactly `Ud=v_N`. Sigma is `I_N`. Thus no dimension-independent Lp or sub-Gaussian bound for the response follows from its L2 projection interpretation or from separate bounds on the individual query fields.

The actual neural query fields are a special family; this example is not a neural counterexample. It identifies exactly the extra structural assertion a regression-based proof would have to establish: a uniform higher-moment estimate on the relevant normalized query spans, or a more restrictive description of the response coefficients than arbitrary L2 projection coefficients. The existing energy and initialization geometry lemmas supply neither.

## 4. Why source tails remain a separate obligation

Part F's fixed-program theorem identifies each fixed capped finite transcript. Part R then constructs **mesh- and cap-independent** response coefficient bounds and uses them to prove `||q_k||_p<=K sqrt(p)`. These tail estimates are not a consequence of the fixed-program theorem or (3).

The usual cap comparison on a bounded primal ball has a Lipschitz factor growing like `exp(C_T R)` with cap level R. Uniform sub-Gaussian incoming tails supply an error of order `exp(-c_T R^2)`, which defeats that growth. Mere bounded second moments provide no such decay, and (3) cannot supply it. For example, the responses in (4) have bounded second moments but no uniform integrability of their squared magnitudes as N increases.

Likewise, the full Gaussian source derivative estimates depend on factors such as

\[
 \exp\left(e C\int_0^T |q(s)|\,ds\right).
\]

A bounded L2 norm of q, even uniformly in time, gives no finite exponential moment for this factor. Bounding q in L2 by energy and then silently applying a sub-Gaussian exponential estimate would be circular.

The fact that the affine amplitude criterion can be satisfied on a particular short, bounded clock does not resolve all physical horizons. For a singular equal-label equilateral triple the symmetric nonlinear clock certificate already scales as `e^{-2}` at fixed separation, whereas the old affine-controlled source sufficient condition contains `e exp(K S)`. Its substitution is circular and fails for all sufficiently small e. Direct finite-horizon construction could avoid this clock, but still needs the uniform tail/continuation assertion described above.

## 5. Consequence for the requested small-delta amplitude scale

The pairwise geometric bound

\[
 Q_1(0)\succeq e^2 b_3^2\,[\delta(2-\delta)]^2 I_3/3
\]

is positive for every `e>0` and is sharp as an initialization statement in the small-delta regime. It does not presently imply a sufficient amplitude scale for the complete three-hidden-layer theorem.

The direct source/energy route has now been sharpened by the exact regression estimate (3), but the missing strong construction and cap-independent source tails remain. There is therefore **no justified answer of the form `e<=c delta^p` from this route**, for any finite p, nor a justified smaller positive asymptotic threshold. Any positive-threshold claim must first add a nonlinear continuation/source theorem that controls the actual neural query spans, not merely their L2 Grams.
