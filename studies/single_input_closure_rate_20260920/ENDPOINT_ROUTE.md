# Endpoint comparison through normalized tangent directions

2026-09-20. Scoped surgical derivation; internally checked, not promoted.
No experiment, optimizer change, Git operation, or maintained-file edit.

Scientific inputs were this study's `RESULT.md` and `ROUTE_DYNAMICS.md`,
the relevant scalar-transform, fitting, endpoint and H3-filter proofs in
`docs/global_nonlinear.md` B.1, C.4.5.1 and C.4.7.10.B, and the
user-authorized consultations of `closure_lyapunov_p1_20260916` and
`fixed_p_predictor_uniqueness_20260919`. In the former, the complete
normalized-readout argument in `all_angles_result.md` §§1–3 and the
complete `resolution_open_family.md`, including its finite-length trapping
argument, were inspected after `resolution_synthesis.md`; no unverified
all-angle initialization or three-dimensional theorem is imported here.
The state-continuity, finite-travel and nullspace arguments in
`PASSIVE_LIMITS.md` were checked. Required math skills and their research
contract/adversarial-audit references were read.

The useful new conclusion is an exact endpoint formula which removes pure
training-speed errors, together with a small-constant endpoint-tail bound.
It isolates a substantially sharper defect to estimate than the full-state
supremum used in `ROUTE_DYNAMICS.md`. It does **not** yet prove that this
defect is bounded by the accumulated H3 source without a stability factor.

## 1. Same systems, a coordinate used only in the proof

Keep the exact single-input problem and maintained H3 closure of
`ROUTE_DYNAMICS.md`, including the actual adjoint, positive ridge filters
and Frobenius metric on the closure matrix. Write their feature curves as
`theta(s)` and `theta_N(s)`. Their training predictions are `b(s)` and
`b_N(s)`, starting at zero. Put

\[
 m=\|h(0)\|_2^2>1/5,\qquad
 m_N=\|h_N(0)\|_2^2.
\]

Assume only `m_N>0` for now. The already checked gradient/readout argument
proves

\[
 b_s=\|\theta_s\|^2\ge m,\qquad
 (b_N)_s=\|(\theta_N)_s\|_N^2\ge m_N.                 \tag{1}
\]

The exact norm is row L2 plus increment HS plus readout L2 in quadrature;
the closure norm uses the coefficient-matrix Frobenius norm in place of
increment HS. Thus each curve reaches level one once, at a finite feature
time, and this level is its original physical gradient-flow endpoint.

For `0<=z<=1`, evaluate each curve at its own unique training level `z`.
Denote those states by `theta[z]`, `theta_N[z]` and the passive outputs by
`F(z,u)`, `F_N(z,u)`. This definition compares two actual trajectories and
does not alter either physical update rule. In particular, it is not an
identical-physical-time comparison before the endpoint.

Let `G_u` be the exact raw gradient of the passive prediction at `u`, and
let `G_u^N` be the closure gradient in its own physical metric. At the
appropriate training level define

\[
 k(z)=\|G_{e_1}\|^2,\quad
 k_N(z)=\|G_{e_1}^N\|_N^2,\qquad
 \kappa(z,u)=\langle G_u,G_{e_1}\rangle,\quad
 \kappa_N(z,u)=\langle G_u^N,G_{e_1}^N\rangle_N.
\]

These are scalar kernel entries; no identification of the two state metrics
is needed. The strong scalar chain rule used in the source proofs gives

\[
 \partial_zF(z,u)=R(z,u):={\kappa(z,u)\over k(z)},\qquad
 \partial_zF_N(z,u)=R_N(z,u):={\kappa_N(z,u)\over k_N(z)}.  \tag{2}
\]

Indeed the feature velocities are their respective training gradients,
and division by (1) is legitimate, including the one-sided endpoint
derivatives. No unrestricted L2 Frechet differentiability is asserted.

## 2. Exact accumulated endpoint defect

Both initial readouts vanish, so integration of (2) proves

\[
 f_N^\infty(u)-f^\infty(u)
       =\int_0^1[R_N(z,u)-R(z,u)]\,dz.                 \tag{3}
\]

Set `Delta k=k_N-k` and `Delta kappa=kappa_N-kappa`, always at equal
training level. Direct common-denominator subtraction gives

\[
 R_N-R={\Delta\kappa-R\Delta k\over k_N}.             \tag{4}
\]

Consequently

\[
 \|f_N^\infty-f^\infty\|_{C(S^1)}
 \le\int_0^1\sup_{u\in S^1}
       { |\Delta\kappa(z,u)-R(z,u)\Delta k(z)|\over k_N(z)}\,dz.
                                                               \tag{5}
\]

Equation (3), with the supremum outside the signed integral, is stronger
than (5) when defects cancel along the path. Equation (4) removes the part
of the kernel error which merely changes training speed. If, at matched
levels, `kappa_N(z,u)=a(z) kappa(z,u)` for every query and
`k_N(z)=a(z)k(z)` with `a(z)>0`, the endpoints agree exactly regardless of
the size of the speed error. This is an algebraic conditional statement,
not a claim that H3 has this property.

The numerator in (5) vanishes identically at `u=e_1`; bias-free oddness
makes it vanish at `u=-e_1` too. The formula therefore retains the passive
prediction question that training loss cannot answer.

For explicit evaluation, at a common exact state write
`H_u=tanh(w.u)`, `h_u=tanh(AH_u)`,
`delta_u=c sech^2(AH_u)` and `p_u=A*delta_u`. Then

\[
 \begin{split}
 \kappa(u,e_1)={}&\langle h_u,h_{e_1}\rangle
 +\langle\delta_u,\delta_{e_1}\rangle
                      \langle H_u,H_{e_1}\rangle\\
 &+u_1\,\mathbb E_1[
       \operatorname{sech}^2(w.u)\operatorname{sech}^2(w_1)
       p_u p_{e_1}].
 \end{split}                                                   \tag{6}
\]

The three terms are readout, middle and first-row contributions. With
`p_u^N=A_N*delta_u^N`, the complete closure kernel is

\[
 \begin{split}
 \kappa_N(u,e_1)={}&\langle h_u^N,h_{e_1}^N\rangle
 +\langle\delta_u^N,Q_2\delta_{e_1}^N\rangle
                         \langle H_u^N,Q_1H_{e_1}^N\rangle\\
 &+u_1\,\mathbb E_1[
       \operatorname{sech}^2(w_N.u)\operatorname{sech}^2((w_N)_1)
       p_u^Np_{e_1}^N].
 \end{split}                                                   \tag{7}
\]

Every field in (7) is evaluated from its current closure state. Its middle
term follows by pairing the two coefficient gradients
`(U_2*delta_u)(U_1*H_u)^T` in Frobenius norm. Replacing it by a filtered
increment HS pairing would give the wrong kernel. The reference ratio in
(4) remains an unknown exact-flow quantity. No convergence of normalized
kernels in N is inferred here from prediction or state convergence.

## 3. A certified tail bound with modest constants

Changing variable in the exact path length and using (1) gives, for
`0<=z_0<=z_1<=1`,

\[
 \int_{s(z_0)}^{s(z_1)}\|\theta_s\|\,ds
    =\int_{z_0}^{z_1}{dz\over\sqrt{k(z)}}
    \le{z_1-z_0\over\sqrt m}.                            \tag{8}
\]

The identical proof holds in the closure's coefficient metric with `m_N`.
Starting from the prescribed initial state yields

\[
 \|c[z]\|_2\le z/\sqrt m,\qquad
 \|K[z]\|_{HS}\le z/\sqrt m,\qquad
 \|A[z]\|_{op}\le2+z/\sqrt m.                           \tag{9}
\]

For the closure, (9) holds with `m_N` and
`||M_N[z]-D_N||_F<=z/sqrt(m_N)`. The contractions `U_l` imply the stated
action bound. These are much smaller than applying the polynomial
feature-time envelopes all the way to feature time six.

The three passive gradient blocks have norms at most
`||A||op ||c||2`, `||c||2`, and one, in the correct metric of either
system. For the closure's middle block this uses
`||U_2*delta_u|| ||U_1*H_u||<=||c||2`. Thus, putting

\[
 C(a)=\sqrt{1+a^{-1}\{1+(2+a^{-1/2})^2\}},
 \qquad T(a)=C(a)/\sqrt a,
\]

Cauchy--Schwarz in (2) gives

\[
 |R(z,u)|\le T(m),\qquad |R_N(z,u)|\le T(m_N).
\]

Integration on the last training-level interval proves the whole-circle
tail estimate

\[
 \|f^\infty-F(1-\alpha,\cdot)\|_{C(S^1)}\le T(m)\alpha,
 \quad
 \|f_N^\infty-F_N(1-\alpha,\cdot)\|_{C(S^1)}\le T(m_N)\alpha.
                                                               \tag{10}
\]

Therefore, for every `alpha in [0,1]`,

\[
 \begin{split}
 \|f_N^\infty-f^\infty\|_{C(S^1)}
 &\le\left\|\int_0^{1-\alpha}(R_N-R)\,dz\right\|_{C(S^1)}
                   +[T(m)+T(m_N)]\alpha\\
 &=\|F_N(1-\alpha,\cdot)-F(1-\alpha,\cdot)\|_{C(S^1)}
                   +[T(m)+T(m_N)]\alpha.                 \tag{11}
 \end{split}
\]

Under the existing sufficient fitting condition `m_N>=9/50`,
`T(m)<22` and `T(m_N)<25`, hence the tail term in (11) is at most
`47 alpha` (strictly less when `alpha>0`). To check these constants without a training calculation,
`T(1/5)^2=255+100 sqrt(5)<484`, while
`T(9/50)^2=(241550+150000 sqrt(2))/729<625`, using
`sqrt(5)<9/4` and `sqrt(2)<17/12`. The displayed expression for `T` is
decreasing in its positive argument. The condition on `m_N` is an
initialization condition and can be checked directly; one need not verify
an all-time source supremum to use (11).

For `alpha>0` these are finite physical stopping times. At `alpha=0`
the formula uses the fitted endpoints, reached only at infinite physical
time. The certificate has no exponential propagation constant. It requires
their actual passive prediction discrepancy, not only their identical
training predictions; no finite-mesh or numerical-integration certificate
is implicit in this exact-population statement.

There is also a concrete identical-physical-time consequence. Since
`1-b(t)<=exp(-2mt)` and `1-b_N(t)<=exp(-2m_Nt)`, the triangle
inequality and (10), now with separate residuals, give

\[
 \|f_N^\infty-f^\infty\|_{C(S^1)}
 \le \|f_N(t,\cdot)-f(t,\cdot)\|_{C(S^1)}
        +T(m)e^{-2mt}+T(m_N)e^{-2m_Nt}.                 \tag{11a}
\]

In particular, if `m_N>=9/50`, at the existing physical horizon `t=40`,

\[
 \|f_N^\infty-f^\infty\|_{C(S^1)}
 \le \|f_N(40,\cdot)-f(40,\cdot)\|_{C(S^1)}
        +1.7\,10^{-5}.                                \tag{11b}
\]

Indeed the tail is at most `22 exp(-16)+25 exp(-72/5)<17/10^6`.
The companion exact-arithmetic check certifies this inequality by lower
bounds on the positive exponential series and reciprocal upper bounds.
This transfers a finite-horizon approximation bound to the fitted predictor;
it does not provide the finite-horizon discrepancy itself or an all-time
finite-neural-width limit.

## 4. The part of the omitted-mode defect that matters instantaneously

There is a useful exact local version of (4) for the middle-update source.
Freeze one exact raw state, its action, and all forward/backward fields.
Define a hypothetical tangent kernel `tilde kappa` by replacing only the
middle metric term of (6) with the Q-filtered middle pairing in (7),
using the frozen exact fields. This is a diagnostic at a fixed state,
not a new closure or optimizer. Put

\[
 J_u=\delta_u\otimes H_u,\qquad
 E=Q_2J_{e_1}Q_1-J_{e_1},\qquad
 \widetilde k=\widetilde\kappa(e_1,e_1).
\]

Actual adjunction gives

\[
 \widetilde\kappa(u,e_1)-\kappa(u,e_1)
                 =\langle J_u,E\rangle_{HS}.
\]

The filtered middle diagonal is nonnegative because it equals
`<delta,Q_2delta><H,Q_1H>`. In particular, along the exact feature curve,
`tilde k>=||h||2^2>=m`. Applying (4) at this fixed state proves

\[
 {\widetilde\kappa(u,e_1)\over\widetilde k}
       -{\kappa(u,e_1)\over k}
   ={\langle J_u-R(u)J_{e_1},E\rangle_{HS}\over\widetilde k}.
                                                               \tag{12}
\]

Here `E` is exactly the omitted-rank source in `ROUTE_DYNAMICS.md`,
equation (15), before taking its norm and supremum. Formula (12) says
which scalar contractions of that source affect passive motion after
normalizing training progress. It can be much smaller than `||E||HS`.
For example a component whose contractions satisfy
`<J_u,E>=R(u)<J_e1,E>` contributes zero. Cauchy--Schwarz also gives the
fully rigorous, if less selective, bound

\[
 \left|{\widetilde\kappa(u,e_1)\over\widetilde k}-R(u)\right|
 \le {\|J_u-R(u)J_{e_1}\|_{HS}\,\|E\|_{HS}\over\widetilde k}.
                                                               \tag{13}
\]

## 5. What remains open and the smallest discriminant

Equations (3)–(13) are proved for the original single-input GF and unchanged
H3 closure. They give a signed accumulated observable defect and a rigorous
small tail. They do not by themselves turn the three exact-path H3 source
norms into a sharp a priori endpoint rate: the actual kernels in (4) are
evaluated at two different trained states. Their difference includes both
the immediate filtered source and its effect on subsequent feature motion.
Equation (12) isolates one direct contribution only; the initialized-action
defects and this feedback remain necessary.

Finite length and tangent coercivity do not control the transverse
sensitivity of the endpoint map. The cited nullspace constructions explain
why exact fitting and endpoint existence are insufficient premises for a
cross-predictor estimate. Those constructions are represented states or
specified frozen-feature forcing examples, not counterexamples to the
canonical initialized GF. Likewise the three-dimensional trapping result
keeps each nearby trajectory in a tube; it supplies no common-endpoint or
small Lipschitz-factor theorem for this comparison.

The smallest useful follow-up is to bound or measure, at matched training
levels up to `1-alpha`, the quantity

\[
 D_N(z,u)=\Delta\kappa(z,u)-R(z,u)\Delta k(z),           \tag{14}
\]

and its signed integral divided by `k_N`, alongside the raw kernel error.
If the normalized quantity is small while raw kernel/state errors are not,
the observed endpoint accuracy is explained by direction preservation or
signed cancellation. If (12) is small but (14) is large, feature-motion
feedback is the remaining mechanism to control. A tolerance `epsilon`
can use `alpha=epsilon/94` (when this is at most one), leaving half its
budget for the early whole-circle discrepancy in (11). No experiment was
run or scheduled in this scoped task.

For a pair of inputs this scalar coordinate requires a proved invariant
one-residual family. The p=1 reflection families have such a proof, but a
generic near-orthogonal pair need not. In the latter case the training
prediction follows a curve in R2, and loss level alone does not determine
its direction. Neither the scalar formula nor the p=1 symmetry is silently
transferred to an arbitrary H3 code-prefix dictionary or arbitrary pair.
