# Regular population tasks: exact reductions and the remaining closure

Frozen independent scoped theory note, 2026-09-30. Scientific inputs were the supervisor's prompt only. No book, code, other study, other route, or external scientific source was consulted. The required conjecture and rigorous-mathematics skills were read. All arguments below are derived here; no numerical evidence is claimed.

## Conclusion

There are concrete, non-oracular population classes with an exact, width-independent population order:

1. A positively homogeneous nonlinear network on a fixed finite union of positive input rays reduces exactly to finitely many weighted examples, even when its radial input laws and labels are continuous.
2. A fixed-depth polynomial-activation network depends on finitely many moments of the input law and of the label-weighted law. This permits an exact, constructive population quadrature. The order is independent of width but generally suffers the input-dimensional curse.

Neither result proves the requested arbitrary-accuracy deep temporal closure by itself. They remove the population obstruction and leave precisely the finite-example temporal problem.

For a genuinely full-dimensional Gaussian input and a smooth fixed-dimensional teacher, teacher regularity controls the label forcing in the natural parameter metric. It does **not** by itself close the student self-interaction, make a realized random-neuron field a function of teacher coordinates, or supply width-uniform trajectory stability. An explicit analytic shallow calculation already exposes the missing realized Gram information. That obstruction invalidates a proposed symmetry proof, not the general existence of a surrogate that retains and uses the exact initial matrices.

The clearest sufficient theorem is conditional: width-uniform population quadrature error plus width-uniform flow stability gives an autonomous, restartable sampled-gradient construction with learned state `O(L n p q + n d)`. The construction below uses no dense evolving matrix. Its two difficult uniform hypotheses are stated rather than attributed to teacher smoothness.

## 1. Contract and exact gradient structure

Let widths equal `n`, depth `L` be fixed, and

\[
z_1(x)=W_1x/\sqrt d,\qquad h_1(x)=\phi(z_1(x)),
\]
\[
z_\ell(x)=W_\ell h_{\ell-1}(x),\qquad
h_\ell(x)=\phi(z_\ell(x)),\quad 2\leq\ell\leq L,
\qquad f_\theta(x)=n^{-1}w^\top h_L(x).
\]

The exact initialized matrices remain available, and `w(0)=0`. No matrix initialization is replaced by its mean, covariance, or a newly sampled matrix. With square loss

\[
R(\theta)=\tfrac12\int (f_\theta-f_*)^2\,d\mu,
\qquad r_\theta=f_*-f_\theta,
\]

define the unnormalized adjoints

\[
b_L=w\odot\phi'(z_L),\qquad
b_\ell=\phi'(z_\ell)\odot W_{\ell+1}^{\top}b_{\ell+1}.
\]

For learning-rate factors `gamma_w,gamma_1,...,gamma_L`, the exact flow is

\[
\dot w={\gamma_w\over n}\int r_\theta h_L\,d\mu,
\]
\[
\dot W_\ell={\gamma_\ell\over n}\int r_\theta b_\ell h_{\ell-1}^{\top}\,d\mu
\quad(2\leq\ell\leq L),\qquad
\dot W_1={\gamma_1\over n\sqrt d}\int r_\theta b_1x^\top\,d\mu. \tag{1}
\]

Thus every hidden-matrix population integrand is rank one. The algebraic reductions below hold for every choice of these fixed rate factors. Where metric bounds are needed, the explicitly stated normalization is

\[
\gamma_w=\gamma_1=n,\qquad \gamma_\ell=1\quad(\ell\geq2). \tag{2}
\]

If the canonical model uses another scaling, its metric and all uniform constants must be checked anew; (2) is not silently imposed on it.

The target is a fixed horizon `[0,T]`, fixed depth, and arbitrary specified accuracy. `p` counts retained population contributions and `q` counts stored temporal contributions. They may depend on accuracy, horizon, depth, and declared task bounds, but not on width. Exact initialization is immutable source data, including its Gaussian randomness. Learned-state accounting excludes immutable initialized matrices only if the main contract does so; storing those matrices explicitly still costs `O(L n^2)` total memory. The construction does not make that cost disappear.

The surrogate must be causal and restartable from its finite current state. Neither precomputed canonical trajectories nor current dense learned matrices are permitted. Results below distinguish exact identities, conditional approximation theorems, and open uniform estimates.

## 2. What the label-weighted measure buys

Let

\[
d\nu(x)=f_*(x)\,d\mu(x).
\]

Writing `grad_E` for the gradient in the training metric, the vector field splits exactly as

\[
F(\theta)=\int \operatorname{grad}_E f_\theta\,d\nu
-\int f_\theta\operatorname{grad}_E f_\theta\,d\mu. \tag{3}
\]

The first term is linear in the teacher. The second term remains even if the teacher has one Hermite coefficient. In particular, knowing a finite list of moments of `nu` does not evaluate its action on an arbitrary evolving feature. One must also know why the relevant test functions are controlled by those moments.

There is nevertheless a useful width-uniform **forcing-error** lemma.

For (2), use the Hilbert norm

\[
\|\delta\theta\|_E^2
={\|\delta w\|_2^2\over n}
+{\|\delta W_1\|_F^2\over n}
+\sum_{\ell=2}^L\|\delta W_\ell\|_F^2.
\]

Suppose `phi` and `phi'` are bounded by `B` and `B_1`, respectively; `int ||x||^2/d dmu <= M_2`; `f_*` is square integrable; and the initialized hidden matrices have operator norms at most `K_0`. These are explicit hypotheses, not a claim about all activations. Gradient flow gives

\[
\dot R=-\|\dot\theta\|_E^2,\qquad
\|\theta(t)-\theta(0)\|_E
\leq \sqrt{tR(0)},\qquad R(0)=\tfrac12\|f_*\|_{L^2(\mu)}^2. \tag{4}
\]

The second inequality follows from Cauchy--Schwarz applied to the time integral of `theta_dot`. Consequently, on `[0,T]`, writing `A=sqrt(T R(0))`,

\[
\|w\|_2/\sqrt n\leq A,
\qquad \|W_\ell\|_{\mathrm{op}}\leq K_0+A\quad(\ell\geq2).
\]

Also `||h_l(x)||_2/sqrt(n) <= B` and

\[
\|b_\ell(x)\|_2/\sqrt n
\leq B_1^{L-\ell+1}(K_0+A)^{L-\ell}A=:D_\ell.
\]

The metric-gradient blocks of a single output are `h_L`, `b_1 x^T/sqrt(d)`, and `b_l h_(l-1)^T/n`, in their respective scaled norms. Therefore

\[
\int\|\operatorname{grad}_E f_\theta(x)\|_E^2\,d\mu(x)
\leq B^2+M_2D_1^2+B^2\sum_{\ell=2}^L D_\ell^2=:C_T^2. \tag{5}
\]

The same bound holds throughout the specified metric ball about initialization. It is independent of width on the stated operator-norm event. No bound on the maximum initialized first-layer row is required here.

Replacing `f_*` by `g` hence changes the vector field, at a fixed parameter state in this ball, by at most

\[
\left\|\int(f_*-g)\operatorname{grad}_E f_\theta\,d\mu\right\|_E
\leq C_T\|f_*-g\|_{L^2(\mu)}. \tag{6}
\]

This proves error production control for teacher approximation. It does not prove stability of the resulting trajectories.

For example, let `x` be standard Gaussian, `U^T U=I_r`, and `f_*(x)=g(U^T x)`, with known `U`. Expand `g` in orthonormal `r`-dimensional Hermite polynomials:

\[
g(z)=\sum_\alpha c_\alpha H_\alpha(z).
\]

If `sum (1+|alpha|)^(2s)|c_alpha|^2 <= R_g^2`, truncation at total degree `m` has error at most `R_g (m+2)^(-s)`. If `sum exp(2 tau |alpha|)|c_alpha|^2 <= R_g^2`, the error is at most `R_g exp(-tau(m+1))`. These estimates follow by bounding the weight from below on the omitted coefficient set and using orthogonality. The number of retained teacher coefficients is `binom(r+m,m)`, independent of ambient dimension and width.

Equation (6) transfers these estimates to the label forcing. But coefficients such as

\[
\int H_\alpha(U^\top x)\operatorname{grad}_E f_\theta(x)\,d\mu(x)
\]

are still expectations of the current random network. Treating their values as available finite-state coordinates without an evolution/evaluation rule is a hidden oracle. If `U` is not supplied by the task, using it as the basis also requires a separately accounted identification method.

## 3. Why input symmetry does not remove realized nuisance variables

The issue is visible in a shallower special case, so it cannot be repaired merely by invoking the same symmetry at greater depth. This example diagnoses an inference; it is not offered as a replacement deep model.

Take `L=1`, `phi(s)=sin(s)`, `x ~ N(0,I_d)`, and the analytic one-index teacher `f_*(x)=u^T x`, `||u||=1`. Put `a_i=W_(1,i)/sqrt(d)`. The exact readout flow under (2) is

\[
\dot w_i=A_i-\frac1n\sum_j w_j K_{ij},
\qquad A_i=(u^\top a_i)e^{-\|a_i\|^2/2}, \tag{7}
\]
\[
K_{ij}=\tfrac12\left(e^{-\|a_i-a_j\|^2/2}-e^{-\|a_i+a_j\|^2/2}\right)
=e^{-(\|a_i\|^2+\|a_j\|^2)/2}\sinh(a_i^\top a_j). \tag{8}
\]

To verify these formulas, use `sin s sin t=(cos(s-t)-cos(s+t))/2` and the Gaussian characteristic function `E exp(i a^T x)=exp(-||a||^2/2)`; differentiating the latter in direction `u` gives (7)'s forcing term.

At zero readout, the hidden weights have zero velocity. Consequently

\[
\dot w_i(0)=A_i^0,\qquad
\ddot w_i(0)=-\frac1n\sum_j K_{ij}^0 A_j^0. \tag{9}
\]

Even the first derivative depends on the full row norm, not just its teacher projection. The second derivative depends on realized mutual inner products. For `d>=3`, fixing each row's teacher projection and perpendicular norm still leaves its relative perpendicular angles free; these change (8), and generically (9), while preserving those one-neuron invariants.

Rotating the **whole** configuration by a symmetry of the input law gives an equivariant copy of the dynamics. Averaging over an invariant initialization law may produce an invariant deterministic output in a suitable width limit. Neither statement makes an individual initialized field invariant. A deep initialized feature already depends on many rows, so its nuisance information is more substantial.

This does not rule out using the exact initialization to compute contractions on demand; for (7), the Gram terms can even be streamed without storing a dense kernel. It does rule out the claimed deduction that smooth one-index labels and rotational input symmetry alone make all realized feature fields functions of a fixed list of teacher coordinates. Any asymptotic self-averaging or equivariant-law closure needed to repair that deduction must be proved and must control the observables actually requested.

## 4. Exact regular population reduction on finitely many rays

Assume there are no biases and `phi` is positively homogeneous of degree `k>0`:

\[
\phi(s z)=s^k\phi(z),\qquad s>0.
\]

Then

\[
f_\theta(sv)=s^D f_\theta(v),\qquad D=k^L. \tag{10}
\]

This follows inductively, because the successive feature degrees are `k,k^2,...,k^L`. Since the scalar factor in (10) is independent of parameters, `grad f_theta(sv)=s^D grad f_theta(v)` at differentiability points. For ReLU (`k=1`), use a consistent derivative convention at zero and the same conclusion holds for its chosen gradient dynamics.

Let the input law be

\[
\mu=\sum_{j=1}^J\pi_j\,\mathcal L(S_jv_j),\qquad S_j>0,
\]

where `J` is fixed, the directions are supplied as part of the input law, and the radial distributions can have smooth densities on compact positive intervals. Labels can be any square-integrable functions along these rays. Define

\[
B_j=\pi_j\,\mathbb E S_j^{2D},\qquad
A_j=\pi_j\,\mathbb E[S_j^D f_*(S_jv_j)].
\]

Discard any zero-mass ray. Completing the square yields, for every parameter state,

\[
R(\theta)=\frac12\sum_{j=1}^J B_j\left(f_\theta(v_j)-\frac{A_j}{B_j}\right)^2+C,
\]
\[
C=\tfrac12\int f_*^2\,d\mu-\tfrac12\sum_j A_j^2/B_j. \tag{11}
\]

Thus the entire canonical gradient vector field is **exactly** that of the weighted finite task with inputs `v_j`, weights `B_j`, and labels `A_j/B_j`. Every initialized Gaussian matrix remains unchanged. Hidden feature learning is retained: for several rays, the hidden activations, gates, and all trained matrices can move. All radial information relevant to this loss has been integrated by the known homogeneity identity, not fitted from a dense trajectory.

Here `p=J` is exact, independent of width and ambient input dimension. A nonlinear smooth example is the homogeneous polynomial activation `phi(z)=z^k` with integer `k>=2`; a practically familiar nonsmooth example is ReLU or leaky ReLU.

Limits of the claim are material. The population is supported on finitely many one-dimensional sets and is generally singular in the ambient space. For `J=1`, the observable learning problem has only one output coefficient. These are exact population tasks but do not establish a full-dimensional density result. A nonconstant scalar activation that is differentiable at zero and positively homogeneous of degree one must be linear: taking `s -> 0` in `phi(sz)/s=phi(z)` identifies it with `phi'(0)z`. Consequently smooth bounded nonlinear activations cannot be quietly included in this exact degree-one reduction.

Equation (11) is a complete population reduction. A width-uniform temporal-memory theorem for its resulting finite task remains a separate obligation.

## 5. Polynomial activations: exact finite moment closure

Suppose `phi` is a polynomial of degree at most `k` and `L` is fixed. Then `f_theta(x)` and every parameter derivative of it are polynomials in `x` of degree at most `D=k^L`. Differentiating coefficients with respect to parameters does not increase the input degree. Equation (3) therefore requires only

\[
m_\alpha=\int x^\alpha\,d\mu,\quad |\alpha|\leq2D,
\qquad
\ell_\alpha=\int x^\alpha f_*(x)\,d\mu,\quad |\alpha|\leq D. \tag{12}
\]

These moments give the vector field exactly for all widths and all parameter states for which the indicated moments exist. The teacher need not be polynomial: only its action on these finitely many polynomials matters. This is a precise setting where the label-weighted-measure route succeeds.

A concrete constructive class is Gaussian input with an explicitly evaluable finite intrinsic-dimensional teacher. Let `P_D f_*` be the total-degree-`D` Gaussian polynomial projection. For every polynomial `v` of degree at most `D`, orthogonality gives

\[
\int f_*v\,d\mu=\int(P_Df_*)v\,d\mu. \tag{13}
\]

Choose a tensor product Gaussian quadrature with `D+1` nodes in each coordinate. Such a one-dimensional rule integrates every polynomial up to degree `2D+1`: divide a polynomial by the degree-`D+1` orthogonal polynomial, use orthogonality for the multiple, and interpolate the degree-at-most-`D` remainder at its roots. Tensorization integrates every total-degree-`2D` polynomial. Hence the weighted finite task at these nodes with labels `P_D f_*` has exactly the same gradient field as the population task, because both `f grad f` and `(P_D f_*) grad f` have degree at most `2D`. The number of nodes is

\[
p=(D+1)^d. \tag{14}
\]

The elementary ingredients of that quadrature are available directly from the Gaussian moments. The moment inner product is positive definite on polynomials, so Gram elimination constructs the monic orthogonal polynomial `P` of degree `D+1`. It has `D+1` simple real roots: otherwise multiplying it by the product of its distinct real roots of odd multiplicity, a polynomial of degree at most `D`, would produce a nonzero function of constant sign and contradict orthogonality. If `L_i` is a root's degree-`D` cardinal interpolation polynomial, set its weight to `int L_i dmu`. This weight equals `int L_i^2 dmu>0`, because `L_i^2-L_i` is divisible by `P` with quotient degree at most `D-1`. These facts justify the rule and its positive weights without a basis oracle.

For `f_*(x)=g(U^T x)`, the teacher projection itself has only `binom(r+D,D)` intrinsic coefficients, after expressing coordinates in a basis extending `U`. The Gaussian data quadrature still sees all `d` input coordinates of the student.

More economical moment rules can improve (14), but exact generic polynomial cubature has an unavoidable dimension cost. For any positive input law with strictly positive integral of the square of every nonzero polynomial of degree at most `D`, a `p`-node rule exact up to degree `2D` must satisfy

\[
p\geq \dim\mathcal P_D(\mathbb R^d)=\binom{d+D}{D}. \tag{15}
\]

Indeed, if there were fewer nodes, the evaluation map from `P_D` to `R^p` would have a nonzero kernel polynomial `v`; exactness for `v^2` would give `int v^2 dmu=0`, a contradiction. This is a lower bound on the universal polynomial-cubature route. It is **not** asserted to be a lower bound for every surrogate or for the smaller collection of fields reachable from a specified initialization.

If the **input support**, not merely the teacher, is contained in a supplied `r`-dimensional linear subspace, replace `d` by `r` in the polynomial construction. This gives a useful genuine continuous-population class with `p=(D+1)^r`, full nonlinear depth, exact Gaussian initialization, and no teacher smoothness requirement beyond the moments. The projected initialized rows can be computed from the actual initialized `W_1`; no initialization is resampled. Unlike a low-dimensional teacher under full-dimensional input, low-dimensional support removes the nuisance input coordinates themselves.

For a general compact support in that subspace, first project the teacher onto the finite-dimensional polynomial subspace of `L^2(mu)` of degree at most `D`. This supplies the analogue of (13), including when different polynomials agree on the support. Finite exact moment rules also exist: the vector of monomials through degree `2D` maps the compact support into a compact subset of a finite-dimensional space; its mean lies in the convex hull and can be represented by finitely many points through the elementary affine-dependence elimination argument. Applying that rule with the projected teacher as labels gives the same gradient field. This proves existence from the task law, not an efficient node-discovery algorithm. The Gaussian tensor rule above gives an explicit construction and avoids relying on an unknown optimal basis.

Again, exact population closure leaves temporal approximation and its uniform constants to be proved. Polynomial activation has unbounded derivatives, so the bounded-activation estimates in Section 2 do not apply to it without additional moment bounds.

## 6. A transparent autonomous construction, conditional on the missing bounds

The following statement isolates what would suffice; it does not assume that task regularity has already established its hypotheses.

Let `E_n` be a specified parameter metric and let `F_n` be the canonical vector field. On a common reachable tube, suppose:

1. A population rule with `p` current-state rank-one contributions defines `F_(n,p)` with `sup_theta ||F_n(theta)-F_(n,p)(theta)|| <= a_p`, where `a_p -> 0` independently of width.
2. `F_n` and `F_(n,p)` are Lipschitz with a common constant `C`, and their norms are at most `M`, all independently of width.
3. The exact and numerical paths stay in that tube, or the same bounds hold on a specified enclosing set.

For a positive quadrature rule, a typical hidden block is

\[
F_{\ell,p}(\theta)=\sum_{j=1}^p c_{\ell j}(\theta)u_{\ell j}(\theta)v_{\ell j}(\theta)^\top. \tag{16}
\]

Use step size `h=T/q` and the autonomous update `theta_(k+1)=theta_k+h F_(n,p)(theta_k)`. Store `W_1` and `w` directly, and for each hidden layer store only the rank-one increments:

\[
\widehat W_\ell^{(k)}
=W_\ell^0+\sum_{s<k}\sum_{j=1}^p
U_{\ell sj}V_{\ell sj}^{\top}. \tag{17}
\]

Each factor pair is created by evaluating (16) at the **current compressed state**. A matrix action is evaluated as `W_l^0 v + sum U (V^T v)`, and the transpose action similarly. Neither action materializes a dense learned matrix. Work may still involve dense immutable-matrix multiplication; no claim of linear computational time is made.

The learned state after `q` steps is `O(L n p q + n d)`. Temporary forward and adjoint values at the `p` nodes cost `O(L n p)`. The method never queries the exact future path. The discrete map is autonomous and restartable; its step counter is only needed to impose the chosen finite storage horizon. If a continuous interpolation is required, augment the state with a clock, the last sampled slope, and a phase and integrate that slope between deterministic resets. This gives an autonomous **hybrid** system with the same storage order. A requirement of a smooth autonomous ODE would need a further construction and is not claimed here.

For completeness, one-step comparison with the exact flow gives

\[
e_{k+1}\leq(1+Ch)e_k+h a_p+\tfrac12CMh^2,
\]

because `||theta(t_k+s)-theta(t_k)|| <= Ms` bounds the exact local integral remainder. Summing the geometric series yields the convenient bound

\[
\max_{k\leq q}e_k
\leq e^{CT}\left(Ta_p+{CM T^2\over2q}\right). \tag{18}
\]

Continuous piecewise-linear comparison adds an error bounded by constants times `h`; its order is the same. If the requested observable is Lipschitz in this metric on the same tube, multiply by its Lipschitz constant. Thus both orders can be chosen independently of width **once** the hypotheses hold. This is a sufficient two-order theorem with all coefficients obtained causally.

For Sections 4 and 5, `a_p=0` at the stated finite population orders. They therefore reduce the problem to a width-uniform temporal stability/integration estimate. If such a finite-task theorem is already available elsewhere under the canonical scaling, it can be applied after checking its activation and task hypotheses; this independent note has not read or presumed one.

## 7. Why the uniform hypotheses are still substantive

The path bound (4) and gradient bound (5) do not establish the Lipschitz hypothesis in Section 6. In deep backpropagation, differentiating a gate produces terms of the form

\[
\delta b_\ell
\supset \phi''(z_\ell)\odot\delta z_\ell
\odot (W_{\ell+1}^{\top}b_{\ell+1}). \tag{19}
\]

A norm bound on `b/sqrt(n)` does not bound its largest coordinate. A direct normalized-`ell_2` estimate of (19) asks for a maximum-coordinate bound or stronger joint moments of the two factors. Bounded hidden operator norms alone do not supply those estimates uniformly over an entire parameter ball. One must use more information about the states actually reached from the exact random initialization. This is a missing proof, not a demonstrated instability or an impossibility theorem.

A generic smooth low-dimensional input distribution also does not automatically give the uniform quadrature hypothesis. For example, on a supplied compact `r`-dimensional input parameter domain, a mesh rule of spacing `delta` would give

\[
\left\|\int V_\theta\,d\mu-Q_pV_\theta\right\|_E
\leq \operatorname{Lip}_z(V_\theta)\,\delta,
\qquad p=O(\delta^{-r}),
\]

if the vector-valued integrand's Lipschitz constant were uniform over the reachable states and widths. Derivatives of the adjoints again contain (19). Teacher regularity is not a substitute for that integrand estimate. Analytic quadrature similarly requires a width-uniform analytic neighborhood and norm for these current fields, not just an analytic teacher.

ANOVA or sparse-compositional regularity of the labels encounters the same distinction. The degree or interaction order of the teacher can stay small while products and nonlinear compositions in `f grad f` generate higher orders. Declaring a fixed sparse basis valid for all reachable fields would be an added neural-dynamics hypothesis. It needs a tail estimate and a bound on feedback from discarded modes. Barron-type bounds would need to apply to the evolving vector-valued gradient integrands, with their norm and coefficient provenance specified; a scalar teacher Barron bound does not imply them.

Monte Carlo does give a width-independent error for a **single fixed-state** integral whenever its Hilbert-valued second moment is uniformly bounded. For independent samples, the mean-square error is exactly the centered second moment divided by sample count. But the reused-rule surrogate state depends on those samples. A fixed-state estimate is not a uniform reachable-state estimate, and resampling at each step introduces a separate stochastic approximation analysis. Neither issue should be hidden by writing `p ~ epsilon^(-2)` without specifying what is approximated and how errors propagate.

## 8. Claim ledger and sharp remaining question

| Claim | Status | Consequence |
|---|---|---|
| Outer-product gradient structure and split by `mu,nu` | Exact | Population and temporal approximations are distinct axes. |
| `L^2` teacher approximation controls label-forcing error under (2) and Section 2's bounds | Proved | Intrinsic teacher smoothness gives a useful source estimate. |
| Rotational symmetry makes realized features teacher-coordinate functions | False as stated | Equations (7)--(9) retain nuisance norms and pairwise Gram information. |
| Homogeneous finite-ray population reduces to `J` weighted examples | Exact | A continuous radial class with exact `p=J`. |
| Polynomial fixed-depth population depends only on (12) | Exact | Explicit finite-width-independent population rules exist. |
| Low-dimensional support removes the ambient population curse for that polynomial class | Proved | `p=(D+1)^r` for Gaussian intrinsic inputs. |
| Low-dimensional teacher alone removes the same curse | Not established | Student self-interaction still uses full input geometry. |
| Uniform quadrature + uniform stability implies autonomous hybrid `O(Lnpq+nd)` construction | Proved conditional statement | Equation (18) gives independent choices of `p,q`. |
| Those uniform hypotheses hold for general deep bounded analytic activations under a smooth one-index Gaussian task | Open | Needs a reachable-state estimate, not symmetry of averaged outputs. |

The strongest clean next question for this route is therefore:

> For a supplied fixed-dimensional Gaussian input subspace and a fixed polynomial activation/depth, does the canonical finite weighted task obtained by exact moment quadrature admit a width-uniform fixed-horizon temporal approximation in a metric controlling predictions and feature learning, while retaining the exact initialized matrices and never evolving a dense learned matrix?

This question has an explicit finite population rule and no task-basis oracle. Its remaining difficulty is the deep temporal estimate. A theorem for it would establish a concrete regular continuous-population class. Extending it to full-dimensional Gaussian input with only a low-dimensional teacher would require an additional self-interaction closure; the signed label measure alone does not provide that bridge.
