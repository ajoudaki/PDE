# Oracle and trained-reference source scope check

Status: **collaborative scoped source check; not an independent review or promotion audit**.

Prepared by the scoped `oracle_book_scope` agent for the supervising task. The assignment supplied the closure identity and requested an assessment of designated established-book arguments. This report does not certify a finite closure theorem, its implementation, or a promotion candidate. No experiments were run and no other study artifacts were read. This is the only file written by this scoped task.

## Source identity and reading coverage

SHA-256 hashes below were captured at persistence time, **2026-09-25 15:28:47 UTC**. No pre-reading hash snapshot was taken; these hashes identify the files when the report was saved rather than claiming an independently frozen input package.

| Source | SHA-256 | Scientific reading coverage |
| --- | --- | --- |
| `docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` | Lines 56–173: the two-hidden-layer model, theorem, and transformed-flow/matrix-memory setup. Lines 341–544: complete §§1.4–1.5, including population well-posedness, proof-mesh stability, deterministic oracle, empirical-feedback comparison, and measured-law identification. |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` | Lines 3836–4208: complete C.4 introduction and C.4.1 state, common ball, transport statement and proof. Lines 4632–4816: complete first three proof units of C.4.3, through direct comparison and limit order. Lines 6904–7652: complete C.4.6 introduction, C.4.6.1 statement/setup, and C.4.6.2 propagator proof, including passive evaluation and endpoint projection. |

The file headings were searched to locate the assigned passages. Unassigned later scientific sections were not read. Dependencies invoked by these passages but outside the authorized source scope were not independently audited. `docs/NOTATION.md` was permitted if needed but was not needed or read.

The required mathematical-process skill was read completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, SHA-256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

Source links below use the recorded line numbers in the shared checkout.

## Conclusion

The oracle argument supports a compact-time closure comparison, but does not itself provide uniform-in-time nonlinear stability. There is also an important refinement: **the full structure proved in C.4.6.2 implies bounded response to a bounded accumulated defect for its particular linear tangent equation**, although the stated forced estimate uses an `L1` forcing norm.

That linear corollary still does not establish a generic finite tanh moment closure versus dense-network all-time error theorem. Its reference, norm, linearization, and finite-width scope must all be retained.

## 1. What the oracle arguments establish

In [arctan §1.5](/home/amir/Codes/PDE/docs/arctan_limits.md:468), the oracle uses the exact population Euler residuals and contractions, with `T` and `Delta` fixed. Its discrepancy from its own accumulated matrix is the exact empirical-minus-population contraction identity (L2.30). The largest error `zeta_n` concerns finitely many contractions and moments; the resulting recurrence is

\[
e_{n,k+1}\le(1+C_{T,\Delta}\Delta)e_{n,k}
                +C_{T,\Delta}\Delta\zeta_n.
\]

See [the exact memory identity and recurrence](/home/amir/Codes/PDE/docs/arctan_limits.md:500). The proof takes width to infinity at a fixed finite program, then refines the proof mesh. Constants depend on `T,Delta`. It proves consistency and compact-time propagation, not an approximation rate uniform in program length, closure dimension, or time. The [global compact-time theorem](/home/amir/Codes/PDE/docs/arctan_limits.md:56) explicitly excludes arbitrary growing horizons.

The tanh reference proxy similarly uses a fixed finite law `nu` and fixed mesh `Delta`, exact population contractions, the actual initialized matrix and its transpose, and accumulated rank-one parameter updates. See [C.4.3's proxy construction](/home/amir/Codes/PDE/docs/global_nonlinear.md:4654). Its comparison with actual GD is local on `[0,T_*]`, using reference Gaussian tails and a Gronwall factor:

\[
\sup_{t\le T_*}D_n
\le Ce^{aR}\big[(1+R)(\eta+\Delta+W_1(\lambda,\nu))
                       +e^{-cR^2}+o_{\mathbb P}(1)\big].
\]

Here `R` is the tail cutoff, not the accumulated closure defect used below. See [the direct comparison](/home/amir/Codes/PDE/docs/global_nonlinear.md:4750). The [explicit limit order](/home/amir/Codes/PDE/docs/global_nonlinear.md:4806) keeps the reference program fixed during width convergence.

Thus the transferable idea is: form the exact matrix accumulator along the approximate histories, identify its defect, then compare coupled states. A generic finite moment closure still needs its own defect bound. The oracle's contraction convergence theorem is not a bound on an arbitrary finite closure rule.

## 2. The one-reference estimate is not a universal Lipschitz theorem

The bound is

\[
\|F_\mu(\theta)-F_\nu(\bar\theta)\|
\le C(1+R)\bigl(D(\theta,\bar\theta)+W_1(\mu,\nu)\bigr)
     +C\mathfrak T_{\nu,R}(\bar\theta),
\]

on a common bounded ball and common carrier. The reference-tail functional contains readout and individual backward-field RMS tails. See [the full transport statement](/home/amir/Codes/PDE/docs/global_nonlinear.md:4087). Only the reference needs these tails, which is useful, but taking the tail cutoff `R` to infinity does not give a fixed global Lipschitz constant. The underlying state metric uses the middle operator norm, and the surrounding flow result is local in physical time.

The assignment supplies the closure identity

\[
\widehat\theta(t)=\theta_0+\int_0^tF(\widehat\theta(s))\,ds+(0,R(t),0),
\]

where `R(t)` now denotes the accumulated middle-block closure defect. If the exact dense state starts from the same initial state and the vector field has Lipschitz constant `K` on a common region containing both paths through `T`, subtraction and Gronwall yield

\[
\sup_{s\le T}\|\widehat\theta(s)-\theta(s)\|
\le e^{KT}\sup_{s\le T}\|R(s)\|.
\]

The cited tanh population transport lemma must not silently substitute for the required Lipschitz hypothesis. Nor does a favorable or “compatible” task name establish that hypothesis or its uniform-in-time counterpart.

## 3. What the trained propagator theorem covers

The theorem concerns the **population linear response at the specified two-atom opposite-label fitted tanh reference**, with training law

\[
\nu_* = \tfrac12\delta_{(\sqrt2 e_1,+1)}
       +\tfrac12\delta_{(\sqrt2 e_2,-1)},
\]

two tanh hidden layers, no biases, the stated Gaussian initialization, stored-weight mobilities `(n,1,n)`, and unhalved mean-square loss. It does not cover arbitrary compatible tasks or finite nonlinear perturbations. The [section introduction](/home/amir/Codes/PDE/docs/global_nonlinear.md:6904) explicitly states its infinitesimal scope.

Its norm is

\[
\mathcal V=L^2(\Omega_1;\mathbb R^2)\oplus
    \mathcal S_2(H_1,H_2)\oplus L^2(\Omega_2),
\]

with first coordinates transformed by `delta w_a = phi'(w_a) xi_a`; the inverse conversion need not be bounded. In particular, the middle component uses **Hilbert–Schmidt norm**, not operator norm. See [the clock-coordinate and tangent-space definitions](/home/amir/Codes/PDE/docs/global_nonlinear.md:6963). At finite width the middle tangent norm is ordinary Frobenius norm, with row/readout squared norms divided by `n`.

Its explicit forced conclusion is

\[
\sup_{t\le T}\|v(t)\|_{\mathcal V}
   \le C_U\int_0^T\|F(s)\|_{\mathcal V}\,ds.
\]

See [P27](/home/amir/Codes/PDE/docs/global_nonlinear.md:7554). General bounded forcing therefore gives a bound proportional to `T`; this is also the [stated data-response estimate](/home/amir/Codes/PDE/docs/global_nonlinear.md:7137). Uniform boundedness of the homogeneous propagator is not, by itself, an all-time bound for arbitrary bounded instantaneous forcing.

The proof uses the actual reference's exponential residual and endpoint-distance decay, uniformly bounded action and readout, and an active endpoint backward-field fourth moment. See [the reference bounds](/home/amir/Codes/PDE/docs/global_nonlinear.md:7172). These give an integrable operator-norm perturbation of a finite-rank endpoint generator. Endpoint compatibility follows from the canonical metric; a spectral gap lower bound and full-rank training Gram are not assumed. The resulting constants depend on the reference endpoint pseudoinverse and are finite but not evaluated as useful numerical bounds.

## 4. Derived bounded-primitive linear corollary

This subsection derives a consequence of the cited proof; it is not a quotation or restatement of its displayed P27 estimate.

The proof establishes

\[
\mathcal L(t)=A_\infty+\mathcal B(t),\qquad
A_\infty=-2S_\infty E_\infty,\qquad
\int_0^\infty\|\mathcal B(t)\|\,dt\le J_0<\infty.
\]

See [P21–P22](/home/amir/Codes/PDE/docs/global_nonlinear.md:7467). Zero-mode compatibility and the finite-dimensional positive training Gram give

\[
V_\infty(\tau)=e^{\tau A_\infty}
 =I+S_\infty\Gamma_\infty^+
   (e^{-2\tau\Gamma_\infty}-I)E_\infty,
\qquad
\sup_{\tau\ge0}\|V_\infty(\tau)\|\le B_\infty,
\]

\[
B_\infty=1+\|S_\infty\|\|\Gamma_\infty^+\|\|E_\infty\|.
\]

See [P15–P17](/home/amir/Codes/PDE/docs/global_nonlinear.md:7363). In particular, `ran E_infty` is contained in `ran Gamma_infty`, so the zero eigenvalue contributes no term to the derivative of this semigroup.

Let `p=rank Gamma_infty<=2`. Choose an orthonormal eigenbasis of the training Gram and write its positive-eigenvalue rank-one projections as `Pi_j`, with eigenvalues `lambda_j>0`. Differentiating the explicit semigroup gives

\[
V_\infty'(\tau)
 =-2\sum_{j=1}^{p}e^{-2\lambda_j\tau}
                  S_\infty\Pi_jE_\infty.
\]

Consequently,

\[
H:=\int_0^\infty\|V_\infty'(\tau)\|\,d\tau
\le\sum_{j=1}^{p}\frac{\|S_\infty\Pi_jE_\infty\|}{\lambda_j}
\le p\|S_\infty\|\|\Gamma_\infty^+\|\|E_\infty\|
=p(B_\infty-1)<\infty.
\]

If `p=0`, the sum is empty and `H=0`; compatibility makes the endpoint semigroup the identity.

For a continuous `mathcal V`-valued accumulated defect `R` with `R(0)=0`, consider the linear integral equation

\[
v(t)=R(t)+\int_0^t\mathcal L(s)v(s)\,ds.
\]

Define

\[
z(t)=R(t)+\int_0^tV_\infty'(t-s)R(s)\,ds.
\]

Integration by parts when `R` is absolutely continuous, or direct substitution and Fubini when `R` is merely continuous, gives

\[
v(t)=z(t)+\int_0^tV_\infty(t-s)\mathcal B(s)v(s)\,ds.
\]

For the continuous case, the direct substitution first verifies `z=R+integral A_infty z`; the constant-generator variation formula then verifies the last display. All kernels are bounded on compact intervals, so the strong integrals and Fubini exchanges are justified there.

Fix any finite `T` and put `epsilon_T=sup_(s<=T)||R(s)||_V`. Then `||z(t)||_V <= (1+H)epsilon_T` for `t<=T`. Taking norms in the last display and applying the scalar integral Gronwall inequality yields

\[
\sup_{t\le T}\|v(t)\|_{\mathcal V}
\le [1+p(B_\infty-1)]e^{B_\infty J_0}
                  \sup_{t\le T}\|R(t)\|_{\mathcal V}.
\]

The constant is independent of `T`. If `R` is absolutely continuous, its derivative need only be locally integrable to interpret the differential equation; no bound on `integral ||R'||` is used in this corollary. If `R` is uniformly bounded on all nonnegative times, the same inequality controls `v` uniformly on all nonnegative times.

This constant still depends on unevaluated endpoint conditioning and the large reference constants. The result is restricted to the exact reference linear equation in the displayed tangent space.

A bounded homogeneous propagator alone would not suffice. Let

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad a\ne0,
\qquad F(t)=e^{Jt}a.
\]

The homogeneous propagator has norm one and

\[
R(t)=\int_0^tF(s)\,ds=J^{-1}(e^{Jt}-I)a
\]

is bounded by `2||a||`. Nevertheless, the solution of `v'=Jv+F`, `v(0)=0`, is `v(t)=t e^{Jt}a`, which is unbounded. The finite-rank dissipative endpoint together with its integrable perturbation, not homogeneous boundedness alone, is what permits the corollary above.

## 5. Obligations before applying this to a finite nonlinear closure

1. **Defect identification and norm.** Establish that the closure defect enters the correct state equation and belongs to the stronger tangent space with a controlled norm. Operator-norm smallness of its middle component alone does not give a dimension-uniform Hilbert–Schmidt bound. The first-coordinate conversion is also not boundedly invertible in general.

2. **Reference applicability.** Identify the exact opposite-label fitted population reference, or prove the corresponding endpoint, zero-mode compatibility, and integrable-perturbation properties for the different reference actually used. Calling a task “compatible” supplies none of these estimates.

3. **Nonlinear control.** Control the nonlinear difference from the reference tangent equation uniformly over all time. A mere quadratic remainder `O(||e||^2)` can accumulate as `T||e||_infty^2`, especially in neutral directions. The cited argument does not assert ambient Frechet differentiability of the nonlinear `L2` field; a formal linearization alone is insufficient. The finite closure requires an additional nonlinear stability argument in an appropriate common region.

4. **Finite-width scope.** A population propagator bound does not give a width-uniform finite-network all-time bound. Finite-width response capture is explicitly for each fixed `T`, separately from uniform population propagation. See [the fixed-horizon capture and propagation statements](/home/amir/Codes/PDE/docs/global_nonlinear.md:7105). No quantitative convergence rate or growing-horizon transfer is supplied there.

Thus the cited sources support the proposed accumulator-and-comparison architecture and, at the specific reference's linear population level, a uniform bounded-primitive estimate. They do not close the missing nonlinear, norm-transfer, defect-size, or all-time finite-width obligations for a generic finite tanh moment closure.
