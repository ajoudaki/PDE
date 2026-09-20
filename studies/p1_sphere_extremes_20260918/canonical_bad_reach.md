# Given canonical convergence: necessary transport and delayed escape

2026-09-18. Scoped analytical route, frozen before comparison with another
current route. This is an internally derived candidate, not an independent
review or promoted result. No experiment or external scientific source was
used. The assignment initially concerned canonical reachability; the lead
then relayed the user's correction: **assume convergence at the base data
and investigate whether input perturbations break that connection**. The
main results below adopt that hypothesis. The independently derived
reflection check is retained separately because it identifies one exact
carrier realization for which that hypothesis would be inconsistent.

Complete scientific inputs read: `docs/observable_p1.md` and this study's
`INPUT_PERTURBATION_RESULTS.md`, `input_perturb_persist.md`,
`input_perturb_bounded_continuation.md`, `input_perturb_cubic.md`,
`finite_critical_loss_gap.md`, `dependent_basin_functional.md`,
`basin_escape_route.md`, `protected_family.md`, `cyclic_uniformity.md`,
and `initialization_positivity.md`. The investigate-conjectures and
solve-math-rigorously skills, research-contract and adversarial-audit
references, and shared workflow instructions were read. No linked source
outside this assignment, study history, README, or other agent report was
read. The proofs below use the exact equations and complete regularity
arguments in these inputs and do not rely on their unread dependencies.

## 1. Contract and conclusions

Use the exact dimension-three canonical p=1 population system, its
correlated fixed marks, ridge 1/4096, all three trained blocks, actual
matrix transpose, and physical population-L2/Frobenius gradient metric.
Let `phi=tanh`, `u_i in S2`, and keep the seven labels and masses `1/7`.
The physical state is

\[
 \theta=(w-g,c,M)\in\mathcal H,
 \qquad\theta_{\rm in}=(0,0,D).
\]

In particular the canonical state is independent of the input data.
Write

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\]
\[
 \rho_i=(f_i-y_i)/7,\qquad
 d_i=E_2[b_2c\phi'(b_2\cdot v_i)].
\]

Assume that for specified base data \(X_0\) the canonical trajectory
converges in \(\mathcal H\) to a specified loss-48/49 equilibrium
\(\theta_*\). No argument below establishes that assumption.

Two conclusions follow.

1. If the actual lower field \(w_*\) is bounded, as in every finite-support
   construction under discussion, then
   \(\|w(t)-g\|_\infty\to\infty\). The integrated lower-force
   coefficients must diverge, even though the state converges in
   \(\mathcal H\) and those coefficients may tend to zero. Consequently
   a uniform bound on lower displacement, or an integrable supremum
   bound on lower velocity, is incompatible with this base hypothesis.
2. Fix a sufficiently late entrance time and a fixed physical Hilbert
   ball about \(\theta_*\). If a nearby input perturbation makes its
   canonical trajectory leave that ball, its first subsequent exit time
   tends to infinity as the input perturbation tends to zero. More
   precisely it has a lower bound of order \(\log(1/\delta)\), where
   \(\delta\) is the input displacement. This proves delayed escape
   **if escape occurs**, not escape itself or genericity of escape.

The central question remains open in this route: neither result decides
whether almost every small input perturbation breaks the assumed bad
connection. They identify concrete restrictions on a proposed proof.

## 2. A bounded endpoint requires divergent accumulated transport

Let \(B_\ell=\operatorname*{ess\,sup}|b_\ell|<\infty\). The exact
lower equation is

\[
 \dot w=-2\sum_i\rho_i\phi'(w\cdot u_i)
                         (b_1^TM^Td_i)u_i.
\tag{1}
\]

Thus, with

\[
 A(t)=2B_1\int_0^t\sum_i|\rho_i(s)|\,|M(s)^Td_i(s)|\,ds,
\tag{2}
\]

we have

\[
 K(t):=\|w(t)-g\|_\infty
 \le\int_0^t\|\dot w(s)\|_\infty ds\le A(t)<\infty
 \quad(t<\infty).
\tag{3}
\]

Here finiteness is a consequence of the actual finite-time equations.
Indeed canonical initial loss is one and exact energy dissipation gives
\(\sum_i|\rho_i|\le\sqrt L\le1\). Hence

\[
 \|c(t)\|_2\le2t,\qquad
 \|M(t)\|_F\le\|D\|_F+2B_1B_2t^2,
\]
\[
 K(t)\le2B_1B_2\|D\|_Ft^2+2(B_1B_2)^2t^4.
\tag{4}
\]

For the matrix bound use
\(|a_i|\le B_1\), \(|d_i|\le B_2\|c\|_2\), and
\(\dot M=-2\sum_i\rho_i d_i a_i^T\); inserting the resulting
bound in (1) and integrating proves the last estimate. No all-time
uniform bound is claimed.

Suppose now \(|w_*|\le R\) almost surely and
\(\|w(t)-w_*\|_2\to0\). The triangle inequality gives pointwise

\[
 |w(t)-w_*|\ge (|g|-K(t)-R)_+.
\]

Therefore

\[
 \|w(t)-w_*\|_2^2
 \ge E\big[(|g|-K(t)-R)_+^2\big].
\tag{5}
\]

For every finite constant \(K_0\), the right side with \(K(t)\)
replaced by \(K_0\) is strictly positive: a standard Gaussian vector
has positive probability outside every finite ball. If \(K(t)\) failed
to tend to infinity, some sequence \(t_n\to\infty\) would have
\(K(t_n)\le K_0\), contradicting (5) and strong convergence. This proves

\[
 K(t)\longrightarrow\infty,\qquad
 \int_0^\infty\|\dot w(s)\|_\infty ds=\infty,
 \qquad A(\infty)=\infty.
\tag{6}
\]

Strong Hilbert convergence of the full state implies a finite all-time
bound \(M_{\max}=\sup_t\|M(t)\|_F\): the tail converges and the finite
prefix is continuous. Since \(\sum_i|\rho_i|\le1\), (2) also yields

\[
 A(t)\le2B_1M_{\max}\int_0^t\max_i|d_i(s)|\,ds.
\]

Consequently

\[
                       \int_0^\infty\max_i|d_i(s)|\,ds=\infty.
\tag{7}
\]

At the particular projected-readout endpoints of the input-perturbation
construction, every \(d_{i,*}=0\). Continuity of the finite moments in
the physical Hilbert topology gives \(d_i(t)\to0\). Thus (7) says
that their approach to zero cannot have an integrable envelope.
Equation (7) is a necessary condition, not a sufficient construction of
an orbit: cancellations in (1) can make the actual lower motion much
smaller than the coefficient envelope.

This does not conflict with finite total gradient dissipation
\(\int_0^\infty\|\dot\theta\|_{\mathcal H}^2dt<\infty\), or with
the assumed Hilbert convergence. A bounded actual lower field satisfies
\(w_*-g\in L^2\) and \(w_*-g\notin L^\infty\). Finite-time
bounded displacement and a Hilbert limit outside the bounded-displacement
class are compatible. Nor does finite-time persistence of Gaussian tails
show that a limiting lower-field law retains full support.

## 3. Any perturbation-induced exit is delayed

Let

\[
 \delta=\max_{1\le i\le7}|u_i-u_i^0|.
\]

Labels and masses stay fixed. We first verify the needed data regularity
in the topology in which convergence is assumed. On every fixed bounded
physical Hilbert ball and sufficiently small data neighborhood, there is
a finite constant \(C\) such that

\[
 \|F_X(\theta)-F_{X_0}(\widetilde\theta)\|_{\mathcal H}
       \le C\big(\|\theta-\widetilde\theta\|_{\mathcal H}+\delta\big).
\tag{8}
\]

Here \(F_X\) is the complete exact vector field. For example,

\[
 |a(w,u)-a(\widetilde w,\widetilde u)|
 \le B_1\big(\|w-\widetilde w\|_2
                    +|u-\widetilde u|\,\|\widetilde w\|_2\big).
\tag{9}
\]

The identical bound with factor two controls the lower gate difference
in L2, because \(|\phi''|\le2\). Upper gates depend on finite
effective vectors and bounded marks, so their differences are bounded
pointwise by the corresponding finite-vector differences. Pairing them
with \(c\in L^2\) gives the required bounds on predictions and \(d_i\).
In (1), the reverse factor is uniformly bounded pointwise by
\(B_1\|M\|_FB_2\|c\|_2\); subtraction of its factors and the explicit
input vector completes (8). These estimates use a bound on
\(\|w\|_2\le\|g\|_2+\|w-g\|_2\), not on \(g\) in supremum norm.

Fix \(r>0\). By the assumed base convergence choose a finite \(T\) with

\[
 \|\theta_0(t)-\theta_*\|_{\mathcal H}<r/4
                       \quad(t\ge T).
\tag{10}
\]

Let \(\theta_X\) be the perturbed canonical trajectory. Applying (8)
on a bounded tube about the finite base segment \([0,T]\), integrating
the difference equation, and the elementary Gronwall inequality gives

\[
 \|\theta_X(T)-\theta_0(T)\|_{\mathcal H}\le C_T\delta
\tag{11}
\]

for all sufficiently small \(\delta\). The tube assumption closes by
choosing \(\delta\) small enough that the resulting bound is less than
its radius; this is finite-horizon continuous dependence, not an endpoint
continuity assumption. The initial difference is exactly zero.

Define the first exit after T by

\[
 \tau_X=\inf\{t\ge T:\|\theta_X(t)-\theta_*\|_{\mathcal H}=r\},
\tag{12}
\]

with value infinity if the set is empty. For small \(\delta\), (10)--(11)
put the time-T state inside the ball. Until exit, both trajectories lie
in its bounded neighborhood, so (8) holds with one uniform constant
\(C>0\). Writing \(e(t)=\|\theta_X(t)-\theta_0(t)\|_{\mathcal H}\),
integration from T yields

\[
 e(t)\le C_T\delta+C\int_T^t(e(s)+\delta)ds
 \le\delta\big[(C_T+1)e^{C(t-T)}-1\big].
\tag{13}
\]

If \(\tau_X<\infty\), continuity and (10) give
\(e(\tau_X)\ge3r/4\). Therefore

\[
 \tau_X\ge T+\frac1C
     \log\!\left(\frac{1+3r/(4\delta)}{C_T+1}\right).
\tag{14}
\]

The constants depend on the specified base trajectory's finite prefix,
the chosen endpoint ball and model/data bounds; they are independent of
the perturbation size and of any perturbed endpoint. If no exit occurs,
the same lower bound holds with \(\tau_X=\infty\). Hence
\(\tau_X\to\infty\) as \(\delta\to0\), whether or not escape is
eventually proved by another argument. Along a fixed nonzero normalized
spherical perturbation direction, \(\delta\) is comparable to its
amplitude, so the same logarithmic lower bound applies to that amplitude.

This necessary delay blocks an argument based solely on continuity at a
fixed observation time. It supplies no upper bound on escape time, no
proof that the perturbed trajectory converges, and no measure statement
for the set of directions that escape. Strict saddles among nearby
perturbed equilibria also do not settle intersection of their stable
sets with the data-dependent canonical trajectory.

## 4. Secondary exact reflection check on one proposed base endpoint

This observation predates the corrected assignment and is not a proposed
solution to generic perturbation-induced escape. It checks consistency
if the base state is chosen to be the explicit positive-amplitude
reflection-symmetric seed realization.

Let \(R=\operatorname{diag}(1,1,-1)\) and
\(R_1=\operatorname{diag}(R,R)\). Simultaneously reflect the third
lower Gaussian coordinate and its reverse noise; denote this
measure-preserving lower-carrier map by S. The marks satisfy

\[
 g(S\omega)=Rg(\omega),\quad b_1(S\omega)=R_1b_1(\omega),
                    RD=DR_1.
\]

On states define the linear isometric involution

\[
 \mathcal T(w-g,c,M)
 =\big(R(w-g)\circ S,\ c\circ R,\ RMR_1\big),
\tag{15}
\]

where \(c\circ R\) means reflecting the third upper coordinate.
The exact upper law is invariant under that reflection. Direct changes
of variables give

\[
 a_{\mathcal T\theta}(u)=R_1a_\theta(Ru),\qquad
                    f_{\mathcal T\theta}(u)=f_\theta(Ru).
\tag{16}
\]

On the seed data, R permutes inputs with the same labels and weights.
Thus the loss is invariant under the isometry \(\mathcal T\);
differentiating this identity in the physical metric makes its gradient
equivariant. The canonical state is fixed by \(\mathcal T\), so
uniqueness of the exact flow implies

\[
                      \mathcal T\theta(t)=\theta(t)
                        \quad\text{for every finite }t.
\tag{17}
\]

The fixed space is closed in \(\mathcal H\), and consequently contains
every strong Hilbert limit of that canonical trajectory.

The positive-slack carrier realization of the supplied bounded
continuation instead has

\[
 w_*(\omega)=\operatorname{sign}(G_1)
                 \sigma(|G_2|)s_{J(|G_2|)},
 \qquad M_*=e_1q^T,
\tag{18}
\]

with \(q\) selecting the coordinate-one lower feature and upper readout
depending only on \(b_{2,1}\). Its matrix and readout are fixed by
\(\mathcal T\). Its lower field is independent of \((G_3,Z_3)\), so
\(w_*\circ S=w_*\) and the antisymmetric projection of its displacement
is exactly \((w_*)_3e_3\). Hence for every canonical trajectory state,

\[
 \|\theta(t)-\theta_*\|_{\mathcal H}
       \ge\|(w_*)_3\|_2>0.
\tag{19}
\]

The strict inequality holds at every sufficiently small positive seed
amplitude: the constructed off-plane critical points have nonzero third
coordinate and their assigned probabilities are strictly positive. On
the uniformly positive-slack continuation these probabilities are bounded
below, the four off-plane branches near \(t_*\) have third coordinates
of order \(\epsilon^{1/3}\), and the remaining two have order
\(\sqrt\epsilon\). Thus this distance is of order
\(\epsilon^{1/3}\), with positive constants at the fixed seed path.

Accordingly the given-base-convergence premise cannot hold for this
particular positive-amplitude seed realization. It can still be posed
for the original axial states, the axial limiting state at zero
amplitude, or a different realization. Generic free input perturbations
break this reflection symmetry. Equation (19) therefore yields no open
data-neighborhood exclusion, no prohibition of symmetry-compatible
carrier realizations, and no measure-zero theorem for the requested
input perturbation event.

## 5. Frozen disposition and checks

| Statement | Status and scope |
|---|---|
| Assumed canonical convergence to a bounded actual lower field forces (6)--(7) | Proved necessary condition, full physical Hilbert convergence |
| Perturbation-induced escape from a fixed endpoint ball obeys (14) | Proved conditional lower bound, all sufficiently small data perturbations |
| The explicit positive-amplitude reflection-seed realization is a canonical endpoint | Excluded by (19), for this carrier realization and symmetric data only |
| Small generic input perturbations cause escape from a given bad connection | Open in this route |
| Finite-time bounded displacement excludes an atomic Hilbert endpoint | Invalid inference; (5)--(7) identify the missing uniform control |
| Local strict saddles automatically imply the canonical data section avoids their basins | Not established; requires a section-transversality or nonlinear escape argument |

Self-checks performed in this scoped derivation: all three original block
equations and the physical metric were retained; the explicit polynomial
finite-time constants were integrated from those equations; the Gaussian
tail lower bound was checked without independence between g and b1;
Gronwall was applied only on a verified bounded Hilbert tube; the reflection
action was checked on the correlated lower marks, upper marks, actual full
matrix and canonical D. No full-support endpoint assertion, interchange
of infinite time with input perturbation, or random-initial-state theorem
was used. This file is frozen for supervisor comparison; independent
review and the generic escape implication remain outstanding.

## 6. Informed post-freeze corollary: state convergence is not integrable

The lead suggested this consequence after reading the candidate frozen at
SHA256 `d860ca85798fb46a5c5a011d41e14f3afc3c6ce6da67c05a3b1ee68502174b87`.
The preceding frozen text is unchanged. This addendum uses only its exact
equations, hypotheses and proved estimates; no further source or experiment
was used. The reflection branch assumptions in Section 4 are not rechecked
by this corollary.

Assume, as in Section 2, that the canonical trajectory converges in the
physical Hilbert norm to an equilibrium with bounded actual lower field,
and additionally assume \(d_{i,*}=0\) for every input. Then

\[
             \int_0^\infty
                  \|\theta(t)-\theta_*\|_{\mathcal H}\,dt=\infty.
\tag{20}
\]

Here is the complete continuity estimate needed to infer this from (7).
For fixed input \(u_i\), put \(v_i=Ma_i\) as before. On a bounded
physical Hilbert neighborhood of the endpoint,

\[
 |a_i-a_{i,*}|\le B_1\|w-w_*\|_2,
\]
\[
 |v_i-v_{i,*}|
 \le B_1\|M-M_*\|_F
              +\|M_*\|_FB_1\|w-w_*\|_2.
\tag{21}
\]

The second bound follows by writing
\(Ma_i-M_*a_{i,*}=(M-M_*)a_i+M_*(a_i-a_{i,*})\).
Subtract the definitions of \(d_i\), using \(|\phi'|\le1\),
\(|\phi''|\le2\), bounded upper marks and Cauchy--Schwarz:

\[
\begin{aligned}
 |d_i-d_{i,*}|
 &\le E_2[|b_2||c-c_*|]
       +2E_2[|b_2|^2|c_*|]\,|v_i-v_{i,*}|\\
 &\le B_2\|c-c_*\|_2
       +2B_2^2\|c_*\|_2\,|v_i-v_{i,*}|\\
 &\le C\|\theta-\theta_*\|_{\mathcal H}.
\end{aligned}
\tag{22}
\]

One finite constant C works for all seven inputs. Since the trajectory
eventually lies in this neighborhood and \(d_{i,*}=0\), we have
\(\max_i|d_i(t)|\le C\|\theta(t)-\theta_*\|_{\mathcal H}\) for all
sufficiently late times. The integral of \(\max_i|d_i|\) on every finite
prefix is finite by finite-time continuity. Its total integral diverges
by (7), so its tail integral diverges. Equation (22) now proves (20).

In particular there cannot be constants \(A,\lambda>0\) with
\(\|\theta(t)-\theta_*\|_{\mathcal H}\le Ae^{-\lambda t}\) for all
sufficiently large t. Nor can this norm be \(O(t^{-1-\eta})\) for
any \(\eta>0\). Either bound would make the tail integral in (20)
finite. More generally every integrable envelope for the state distance
is excluded. The conclusion permits nonintegrable convergence rates
and places no lower bound on the state distance at each individual time.

This is a restriction on **state convergence**, not on the scalar loss
rate. No lower comparison of state distance with
\(|L(t)-L(\theta_*)|\) has been proved, so exponential convergence of
the loss to 48/49 is not excluded. The corollary also does not decide
whether generic small input perturbations break the assumed connection.
