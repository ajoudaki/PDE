# Isolated adversarial audit of the finite-network variational route

Verdict: **PASS within the requested scope.** I found no substantive mathematical gap in the exact Hessian decomposition, its operator/Hilbert--Schmidt bounds, the GF and exact-GD logarithmic response estimates, descent, GF gradient alignment, or the error reduction (29). The large-width and initialization-event qualifications in Section 7 supply the hypotheses needed for the stated application to exact GD. Equation (29) remains a sufficient reduction with an explicitly uncontrolled term; it does not establish GD/GF convergence.

## Scope and provenance

Audited candidate, read in full:

- `/tmp/l3-two-sample-Un7kw9/INDEPENDENT_GLOBAL_ACTIVATION_ROUTE.md`
- SHA-256: `f348cbf0daf4d06c71c81ab7ee5403c1fda781c03fb33b454ebf2df89b273d74`
- The supplied hash matched before the audit and again before writing this review. Candidate line references below refer to that content.

Sole model dependency, read in full:

- `/tmp/l3-two-sample-Un7kw9/CONTRACT.md`
- SHA-256: `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd`

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md`. I did not read histories, other notes, other reviews, or the documents referenced inside the candidate or contract. No experiments, agents, external research, or candidate edits were used. Historical assertions about other routes and certificates were not verified or used.

This audit covers finite networks with the contract's metric, initialization, two residuals, and physical step size, using exactly `phi(z)=1+z+(1/10) arctan(z)`. Population existence, population identification, persistent nonaffinity, restart, and the full observable contract are outside the certification below.

The audit derives the metric and Hessian formulas first, checks the noncommuting matrix argument independently, and then checks that the initialization and GD induction actually supply its hypotheses. Finally it verifies alignment and the averaged-Hessian error calculation.

## 1. Raw metric, physical scaling, and deterministic bounds

The contract has

\[
f_a=\langle C,h_a^3\rangle_n,
\qquad L=\tfrac12\sum_{a=1}^2 r_a^2,
\qquad r_a=f_a-y_a.
\]

Thus its loss derivative is `sum_a r_a df_a`; there is no additional averaging factor. Relative to the metric (1), the four blocks of the gradient of one prediction are exactly

\[
\nabla_{W^1}f_a=\frac{\delta_a^1x_a^*}{d},\qquad
\nabla_{W^2}f_a=\frac{\delta_a^2(h_a^1)^*}{n},\qquad
\nabla_{W^3}f_a=\frac{\delta_a^3(h_a^2)^*}{n},\qquad
\nabla_C f_a=h_a^3.
\]

For example, the Euclidean first-block derivative is `delta^1 x_a^*/n`; multiplying by the inverse metric coefficient `n/d` gives the first formula. The Euclidean readout derivative `h^3/n` similarly becomes `h^3`. These reproduce CONTRACT.md lines 34--41, including

\[
\dot z_a^1=-\sum_b r_b\rho_{ab}\delta_b^1.
\]

Consequently (2) has the correct physical time and no missing width or input-dimension factor.

The activation bounds used are valid. In particular

\[
\phi'(z)=1+\frac{e}{1+z^2},\qquad
\phi''(z)=-\frac{2ez}{(1+z^2)^2},\qquad e=\tfrac1{10},
\]

and `2|z| <= 1+z^2` implies `|phi''| <= e`. The looser bounds `|phi'| <= 2` and `|phi(z)| <= 2+2|z|` hold globally.

For a state in (3), with `B >= 1`, the successive activation bounds are

\[
2+2B\le4B,\quad
2+2B(4B)\le10B^2,\quad
2+2B(10B^2)\le22B^3.
\]

The backwards recursion uses the actual transposes on the separate neuron spaces. It gives precisely (5), and additionally `||delta_a^1||_n <= 8B^3`.

For the first variation,

\[
\|(vW^1)x_a\|_n
\le\sqrt{d/n}\,\|vW^1\|_F\le\|v\|_{H_n}.
\]

The inequality `||Mh||_n <= ||M||_F ||h||_n` then gives

\[
\|T_a^2\|_{\rm op}\le4B+2B=6B,\qquad
\|T_a^3\|_{\rm op}\le10B^2+2B(6B)=22B^2.
\]

Finally,

\[
df_a[v]=\langle vC,h_a^3\rangle_n
+\langle C,D_a^3T_a^3v\rangle_n
\]

has norm at most `22B^3+44B^3=66B^3`. Equations (4)--(7) and the gradient bound are correct. No inverse input Gram matrix is involved, so antipodal inputs and either label sector cause no degeneracy in these arguments.

## 2. Exact Hessian, mixed terms, and every width factor

Differentiating the first-variation recursion once more gives

\[
\begin{split}
d^2z_a^2[v,v]&=2(vW^2)D_a^1T_a^1v
+W^2[\phi''(z_a^1)(T_a^1v)^2],\\
d^2z_a^3[v,v]&=2(vW^3)D_a^2T_a^2v
+W^3[\phi''(z_a^2)(T_a^2v)^2]
+W^3D_a^2d^2z_a^2[v,v].
\end{split}
\]

Inserting these into the second derivative of `<C,phi(z_a^3)>_n` gives (8). To check the off-diagonal parameter blocks explicitly, its polarized form is

\[
\begin{split}
d^2f_a[v,w]={}&\langle vC,D_a^3T_a^3w\rangle_n
+\langle wC,D_a^3T_a^3v\rangle_n\\
&+\sum_{\ell=1}^3
\langle b_a^\ell\phi''(z_a^\ell),
(T_a^\ell v)(T_a^\ell w)\rangle_n\\
&+\sum_{\ell=2}^3\left[
\langle\delta_a^\ell,(vW^\ell)D_a^{\ell-1}T_a^{\ell-1}w\rangle_n
+\langle\delta_a^\ell,(wW^\ell)D_a^{\ell-1}T_a^{\ell-1}v\rangle_n
\right].
\end{split}
\]

Thus both occurrences of each trained matrix are present, including variations through all earlier layers. There is no missing mixed Hessian term or missing factor two.

On a neuron Hilbert space with normalized norm, the orthonormal coordinate basis is `sqrt(n)e_i`. Therefore

\[
\|M_q\|_{\rm HS}^2=\sum_iq_i^2=n\|q\|_n^2.
\]

This is the crucial width factor: normalization of the vector inner product does not normalize the Hilbert--Schmidt trace by `n`. The curvature operator for layer `ell` is exactly

\[
(T_a^\ell)^*M_{b_a^\ell\phi''(z_a^\ell)}T_a^\ell.
\]

The inequality `||ABC||_HS <= ||A||_op ||B||_HS ||C||_op` follows by orthonormal-basis summation, using adjoints for the right multiplication. Applying it gives the three bounds

\[
e\sqrt n\,4B^3,\qquad
e\sqrt n\,72B^4,\qquad
e\sqrt n\,484B^5.
\]

Their sum is at most `560e sqrt(n) B^5`, as claimed.

For a trained hidden-matrix block, define `R_ell v=(vW^ell)^* delta_a^ell`. Its adjoint into the Frobenius matrix block is

\[
R_\ell^*u=\delta_a^\ell u^*/n.
\]

In particular

\[
\|R_\ell\|_{\rm op}=\|\delta_a^\ell\|_n,\qquad
\|R_\ell\|_{\rm HS}^2
=\sum_{i,j}\|\delta_{a,i}^\ell e_j\|_n^2
=n\|\delta_a^\ell\|_n^2.
\]

The mixed operator is `R_ell^* D_a^{ell-1} T_a^{ell-1}` plus its adjoint. Its operator norm is bounded by the stated product with factor two. The separate contributions are:

| Term | Operator-norm bound | Hilbert--Schmidt bound |
|---|---:|---:|
| Readout mixed term | `88B^2` | `88 sqrt(n) B^2` |
| Layer 2 mixed term | `16B^2` | `16 sqrt(n) B^2` |
| Layer 3 mixed term | `48B^2` | `48 sqrt(n) B^2` |
| All activation-curvature terms | bounded by their HS norm | `560e sqrt(n) B^5` |

For the readout line, the projection onto the readout field has operator norm one and Hilbert--Schmidt norm `sqrt(n)` in the raw metric. Thus `||S_a||_op <= 152B^2` is correct. These computations also give the stronger bound

\[
\|\operatorname{Hess}f_a\|_{\rm HS}
\le\sqrt n(152B^2+560eB^5)
\le208\sqrt n B^5
\le800\sqrt n B^5
\]

at the fixed amplitude `e=1/10`. Hence the constant in (10) is conservative.

Each of the three curvature operators factors through an `n`-dimensional space, so has rank at most `n`. Each of the three mixed operators is the sum of two rank-at-most-`n` maps. Rank subadditivity proves the `9n` bound; no shared or paired neuron population is assumed.

The loss Hessian is exactly

\[
H=\sum_a\nabla f_a\otimes\nabla f_a+\sum_a r_a\operatorname{Hess}f_a.
\]

The first term is positive semidefinite even with opposite labels. The triangle inequality, applied only after forming the signed residual terms, proves (11)--(12). The candidate correctly keeps operator control of `S` separate from the `sqrt(n)` Hilbert--Schmidt control of `K`.

## 3. Noncommuting logarithmic strain and the GF response

For the actual finite-dimensional variational equations, the generators are continuous; the auxiliary GD construction below is piecewise continuous. Their fundamental matrices are invertible. Accordingly `P=JJ^*>0` and its spectrum lies in a compact subset of `(0,infinity)` on each local compact time interval.

Let `F(x)=(log_+ x)^2`. This is continuously differentiable, including at one, with

\[
F'(x)=2\log_+(x)/x.
\]

The spectral trace chain rule used in the candidate needs only this regularity. Its polynomial argument can be completed by uniformly approximating `F'` on the spectral interval and integrating the approximating polynomials to approximate `F` and its derivative simultaneously. Polynomial trace differentiation follows from cyclicity. Integrating along the matrix path and passing to these uniform limits gives the asserted chain rule, including when eigenvalues cross one or have multiplicity.

As `A=A^*`, one has `P'=AP+PA`. Since `P` commutes with its own spectral functions,

\[
\begin{split}
\mathcal E'
&=\tfrac12\operatorname{tr}
\{P^{-1}\log_+(P)(AP+PA)\}\\
&=\operatorname{tr}\{A\log_+(P)\}.
\end{split}
\]

For `A=-Q+E`, with `Q >= 0`, positivity gives

\[
\operatorname{tr}\{Q\log_+(P)\}
=\operatorname{tr}\{Q^{1/2}\log_+(P)Q^{1/2}\}\ge0.
\]

Hilbert--Schmidt Cauchy--Schwarz therefore yields

\[
\mathcal E'\le2\|E\|_{\rm HS}\sqrt{\mathcal E}.
\]

Dividing by `2 sqrt(mathcal E+epsilon)` gives an upper derivative bound by `||E||_HS`. Integrating from `J(s,s)=I`, and then sending `epsilon` to zero, proves (15) with the stated constant. It is not necessary that `A` commute with `P` or that generators at different times commute. The argument uses cyclicity precisely where needed.

For GF, set `a=152B^2 R`. The scalar-rescaled propagator has generator

\[
-(G+S+aI)-K,
\qquad G+S+aI\succeq0.
\]

Thus (15) applies with `E=-K`. Scalar rescaling multiplies every singular value by `exp(-A_B)`. Squaring the integral bound and dividing by `n` gives (17), including its exact factor `560eB^5`. Counting terms exceeding a positive threshold gives (18).

The normalization is by `n`, although the trace runs over all `m_n=nd+2n^2+n` raw directions. Neither a width-uniform bound on `||K||_op` nor a moment bound for the singular values is being inserted into this argument. The formal `e=0` check is also correct: the sum in (17) is then zero, so no singular value can exceed `exp(A_B)`.

Minor terminology only: the opening phrase “trace norm” should be understood through (13). The proved quantity is a squared Hilbert--Schmidt norm of the positive logarithmic strain, not a Schatten-one/nuclear-norm estimate. The subsequent equations specify the quantity unambiguously.

## 4. Exact GD factors, positivity, and the logarithm

At a node where `eta ||H_k||_op < 1`, every eigenvalue of `I-eta H_k` is strictly positive. Dividing by `1+eta a_k > 0` preserves this property, and algebra gives exactly

\[
\frac{I-\eta H_k}{1+\eta a_k}
=I-\eta\overline H_k,\qquad
\overline H_k=\frac{H_k+a_kI}{1+\eta a_k}.
\]

Here the notation `overline H_k` is the Section 6 rescaled nodal Hessian, distinct from the chord average in Section 9. Decompose it as

\[
\overline H_k=Q_k+E_k,\qquad
Q_k=\frac{G_k+S_k+a_kI}{1+\eta a_k}\succeq0,\qquad
E_k=\frac{K_k}{1+\eta a_k}.
\]

If `v_i` are orthonormal eigenvectors for its negative eigenvalues `-mu_i`, then

\[
\langle v_i,E_kv_i\rangle
=-\mu_i-\langle v_i,Q_kv_i\rangle\le-\mu_i.
\]

After completing them to an orthonormal basis, the sum of these diagonal entries squared is bounded by the full Hilbert--Schmidt norm squared. Hence `||overline H_{k,-}||_HS <= ||E_k||_HS`; this does not require `Q_k` and `E_k` to commute.

Because the factor is positive definite, its real symmetric logarithm exists. The positive eigenvalues of

\[
D_k=\eta^{-1}\log(I-\eta\overline H_k)
\]

are exactly `log(1+eta mu_i)/eta`, each at most `mu_i`. Applying (15) to the piecewise constant generators `D_k=-D_{k,-}+D_{k,+}`, each acting for time `eta`, bounds the positive logarithmic strain by

\[
\sum_{j=l}^{k-1}\eta\|D_{j,+}\|_{\rm HS}
\le\sum_{j=l}^{k-1}\frac{\eta\|K_j\|_{\rm HS}}{1+\eta a_j}.
\]

The time-ordered product at these auxiliary interval endpoints is exactly

\[
\prod_{j=k-1}^{l}\frac{I-\eta H_j}{1+\eta a_j}
=e^{-A^{GD}_{k,l}}J^{GD}_{k,l},
\]

with the product in the order specified in the candidate. This is a matrix proof and does not alter the raw GD interpolation. Dropping the denominators on the right gives (20), while retaining them gives the stated sharper version. Negative eigenvalues of the logarithm can be large; the proof correctly drops their contribution rather than bounding them in Hilbert--Schmidt norm.

## 5. Initialization, finite GF continuation, and exact-GD first exit

The elementary initialization claims in lines 355--366 are correct:

- For either fixed RMS-unit input, the first-layer coordinates are independent `N(0,1)` across neurons. The squared RMS has mean one and variance `2/n`. Applying this separately to both samples and using a union bound needs no independence between the samples, including at `rho=-1`.
- The readout has `E ||C||_n^2=n^-2`, so its RMS tends to zero in probability by Markov's inequality.
- A maximal `1/4`-separated subset of the unit sphere is a `1/4`-net. Comparing volumes of the disjoint balls of radius `1/8` with a ball of radius `9/8` gives cardinality at most `9^n`. Approximating both vectors in `u^*Wv` gives `||W||_op <= 2 max_net |u^*Wv|`.
- For each fixed unit pair, `u^*Wv` is Gaussian with variance `1/n`. Its exponential moment gives `P(|u^*Wv|>5) <= 2 exp(-25n/2)`. The union bound over both nets is exactly `2 exp[(2 log 9-25/2)n]` for each hidden matrix; a further union bound treats both matrices.

On the event that the first-layer RMS norms and hidden operator norms are at most ten, (4) gives `||h_a^3||_n <= 22000`. Thus `|f_a(0)| <= 22000 ||C(0)||_n` there, proving `f_a(0) -> 0` in probability. Consequently `L(0) -> 1` for either label choice. This establishes events `E_n` with probability tending to one on which all of (3) initially hold with `B_0=10` and `L_0 <= 4`. It uses precisely the prescribed Gaussian initialization.

For finite GF, differentiating the loss gives

\[
\frac{d}{dt}L=-\|\nabla L\|_{H_n}^2=-\|\dot\theta\|_{H_n}^2.
\]

Integration and Cauchy--Schwarz give (21). On any bounded physical interval this bounds the full raw displacement, including parameter directions not measured separately in (3). In finite dimension a maximal solution with a finite endpoint would have a limit there: its increments are at most `sqrt(|t-s| L_0)`. Smoothness of the vector field then extends it from that limit. Finite GF is therefore global.

Each quantity in (3) is Lipschitz with constant at most one with respect to raw displacement: use the already checked `T_a^1` bound, the inequality `||Delta W||_op <= ||Delta W||_F`, and the readout block norm. This justifies the deterministic region used for GF.

For GD, the bounds needed before descent are available throughout (3), without assuming the loss is small on a segment:

\[
|r_a|\le22B^4+1\le23B^4,
\]

\[
\begin{split}
\|H\|_{\rm op}
&\le2(66B^3)^2+(46B^4)(800\sqrt n B^5)\\
&\le45512\sqrt n B^9
\le50000\sqrt n B^9.
\end{split}
\]

At a node with `L_k <= 4`, `R_k <= 2 sqrt(L_k) <= 4`, so `||g_k|| <= 264B^3`, where `g_k=grad L(theta_k)`.

Here is an explicit induction that checks the potential first-exit circularity. Fix `T`, put

\[
D=\sqrt{8(T+1)},\quad B=10+D+1,\quad
N=\lceil T/\eta_n\rceil,
\]

and take `n` large enough that

\[
264B^3n^{-2}\le1,\qquad
50000B^9n^{-3/2}<1.
\]

Also `N eta_n <= T+1`. Suppose descent has been proved through node `k`, so

\[
\sum_{j<k}\eta_n\|g_j\|^2\le2L_0,
\qquad
\|\theta_k-\theta_0\|\le\sqrt{2k\eta_n L_0}\le D.
\]

This places every monitored quantity at that node at most `B-1`. The nodal gradient bound now gives a proposed step of norm at most one. Every point of that segment therefore satisfies (3), independently of any assertion about its loss. The region Hessian bound and the second inequality above can consequently be used in Taylor's formula:

\[
\begin{split}
L_{k+1}
&=L_k-\eta_n\|g_k\|^2
+\eta_n^2\int_0^1(1-u)
\langle g_k,H(\theta_k-u\eta_ng_k)g_k\rangle\,du\\
&\le L_k-\tfrac{\eta_n}{2}\|g_k\|^2.
\end{split}
\]

This proves the next energy bound. Cauchy--Schwarz then gives

\[
\|\theta_{k+1}-\theta_0\|
\le\sum_{j\le k}\eta_n\|g_j\|
\le\sqrt{2(k+1)\eta_n L_0}\le D.
\]

The induction starts at the initialization and covers all segments intersecting `[0,T]`. Thus the unit margin is established before each Taylor argument. It also proves strict positivity of every GD derivative factor used in (20). There is no reliance on a GF-to-GD comparison.

On `E_n`, GF has `R(t) <= 4`, and GD has `R_k <= 4`. Therefore the constants in (17) and (20) are finite at each fixed `T` and independent of width for sufficiently large `n`. No assumption of small `e` depending on `T`, or any lower bound on `1-rho` or `1+rho`, entered the proof.

## 6. GF gradient alignment

Along finite GF, `g(t)=grad L(theta(t))` satisfies

\[
g'(t)=H_t\dot\theta(t)=-H_tg(t).
\]

The vector `J_n(t,s)g(s)` solves the same linear initial-value problem with the same value at `s`. Uniqueness proves (22). In the raw-metric singular-value decomposition, orthonormality of the left singular vectors gives exactly

\[
\|g(t)\|_{H_n}^2
=\sum_j\sigma_j^2|\langle v_j,g(s)\rangle_{H_n}|^2.
\]

On the Section 7 event, `L(t) <= 4` and hence `||g(t)|| <= 264B^3`; this is the required qualification on the numerical bound in (23). Restricting the sum to `sigma_j>M`, for `M>0`, proves (24).

These statements concern the full GF gradient. They do not establish the same identity for an exact-GD gradient, a block projection, or the averaged-Hessian propagator. The candidate explicitly observes these restrictions in lines 423--427, so there is no illicit extension of the identity.

## 7. Interpolation defect, averaged Hessian, and reduction (29)

On a GD step write `u=t-k eta_n`. Then `theta_h(t)-theta_k=-u g_k`, and the mean-value formula gives

\[
\tau_h(t)
=\nabla L(\theta_h(t))-g_k
=-u\int_0^1H(\theta_k-vu g_k)g_k\,dv.
\]

The entire step segment is in (3), by the induction above. Consequently

\[
\|\tau_h(t)\|_{H_n}
\le\eta_n(50000\sqrt n B^9)(264B^3)
=13200000B^{12}n^{-3/2}.
\]

This verifies the physical-time defect (26), including its width exponent. The linear interpolation is differentiable off nodes. The equations hold almost everywhere, with the specified one-sided node conventions; both one-sided defect values obey this bound. Node conventions do not affect Duhamel's integral.

For `e_h=theta_h-theta`, the exact differential equation is

\[
e_h'=V(\theta_h)-V(\theta)+\tau_h
=-\overline H(t)e_h+\tau_h,
\qquad e_h(0)=0,
\]

where `overline H(t)` is exactly the chord average (27), not the Hessian of either endpoint trajectory.

The region (3) is convex: the first-layer preactivation constraints are norms of linear maps of `W^1`, and the other constraints are operator or vector norm balls. Thus the entire chord between GF and interpolated GD stays in (3). The loss need not stay below four on that chord. The preceding region bound instead gives `sum_a |r_a| <= 46B^4` at every chord point. It follows that the averaged decomposition satisfies

\[
\overline G\succeq0,\qquad
\|\overline S\|_{\rm op}\le6992B^6,\qquad
\|\overline K\|_{\rm HS}\le25760e\sqrt n B^9.
\]

These conclusions use positivity under integration and the norm triangle inequality. Averaging can increase rank beyond the pointwise rank bound, but no rank bound is needed here.

For the propagator `Psi_n(t,s)` of `-overline H`, the already proved logarithmic argument therefore gives, for `0 <= s <= t <= T`,

\[
\frac1n\sum_j
[\log\sigma_j(\Psi_n(t,s))-6992B^6(t-s)]_+^2
\le[25760eB^9(t-s)]^2.
\]

One may consequently take

\[
A_T=6992B^6T,\qquad C_T^{\rm strain}=(25760eB^9T)^2
\]

in the uniform tail count. Whenever `alpha log n > A_T`, every singular value above `n^alpha` contributes more than `(alpha log n-A_T)^2` to the corresponding sum with the larger shift `A_T`. Hence

\[
\frac{\operatorname{rank}P_{\rm bad}(t,s)}n
\le\frac{C_T^{\rm strain}}{(\alpha\log n-A_T)^2},
\]

which proves (28). The requirement that `n` be sufficiently large ensures positivity of the unsquared threshold before this counting argument is applied.

For completeness, the projector is intrinsically the spectral projector

\[
P_{\rm bad}(t,s)
=\mathbf 1_{(n^{2\alpha},\infty)}(\Psi_n(t,s)^*\Psi_n(t,s)).
\]

It is measurable even when singular values coincide or cross the threshold; no continuous choice of singular vectors is needed. On its orthogonal complement,

\[
\|\Psi_n(t,s)(I-P_{\rm bad}(t,s))\|_{\rm op}\le n^\alpha.
\]

Duhamel's formula and the triangle inequality now give

\[
\begin{split}
\|e_h(t)\|_{H_n}
&\le\int_0^t\|\Psi_n(t,s)(I-P_{\rm bad}(t,s))\tau_h(s)\|_{H_n}\,ds\\
&\quad+\int_0^t\|\Psi_n(t,s)P_{\rm bad}(t,s)\tau_h(s)\|_{H_n}\,ds\\
&\le13200000TB^{12}n^{\alpha-3/2}
+\int_0^t\|\Psi_n(t,s)P_{\rm bad}(t,s)\tau_h(s)\|_{H_n}\,ds.
\end{split}
\]

Taking the supremum in `t` proves (29). Any fixed `0<alpha<3/2` makes the first term vanish. Constants denoted `C_T` in different estimates can be enlarged to a common finite constant, as in the candidate.

The remaining integral is unproved, as the candidate says. Its vanishing would be sufficient for same-width GD/GF convergence in probability, since `P(E_n)->1`. The derivation establishes sufficiency, not necessity or equivalence: taking the norm inside the time integral loses potential cancellation. The wording “exact reduction” is valid as an exact inequality from the actual error equation, not as an if-and-only-if convergence criterion.

The rank estimate cannot itself bound that integral: it limits the number of expanding directions, while the integrand also contains their singular values and the components of the dependent forcing. The GF identity (22) does not apply to this chord-averaged propagator or to the defect above. The candidate does not claim otherwise. These are explicitly retained open implications, not defects in the proved reduction.

## Final scoped assessment

| Audited claim | Result |
|---|---|
| Raw metric and exact GF/GD scaling | Verified, including `1/d`, `1/n`, readout rescaling, and physical `eta_n=n^-2` |
| Exact mixed and activation-curvature Hessian formulas | Verified by the full polarized second variation |
| Operator/HS split, rank, and constants | Verified; the `800 sqrt(n) B^5` bound is conservative |
| Noncommuting positive logarithmic strain | Verified, including the spectral threshold at one |
| GF response bound (17) | Verified on the stated bounded region, supplied at finite horizons by energy |
| Exact-GD response bound (20) | Verified for sufficiently large widths on the initialization events; all factors are positive definite |
| Elementary high-probability initialization | Verified from marginal moments, Gaussian tails, and the stated net sizes |
| Exact-GD descent and first-exit induction | Verified without comparison to GF |
| Full-GF gradient alignment (22)--(24) | Verified under the Section 7 loss bound |
| Defect rate, chord average, and reduction (26)--(29) | Verified with explicit constants and the actual propagator |
| Vanishing of the exceptional-direction integral | Explicitly open in the candidate; not certified |
| Global population theorem or full contract | Outside the requested scope; not certified |

No correction to a scoped mathematical estimate is required by this audit. The only wording qualifications identified are the Schatten-two nature of the logarithmic quantity and the sufficient, rather than equivalent, character of the final error criterion. Neither invalidates the candidate's displayed finite-network results.
