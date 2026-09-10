# Controlled matched-loss expansion; sign remains open

This result is for the exact model and fixed design in the README. It does
not establish a positive or negative finite-time risk comparison. Its useful
conclusion is a controlled reduction of that question to one explicit scalar
Gaussian/angle integral. Study results are not established book material.

## The exact local statement

There exist `T>0` and finite `M>=1`, independent of width and GD step,
such that the unique population loss-matching clock exists on `[0,T]` and

\[
 \tau(t)=t+\beta t^3+O(t^4),\qquad \beta>0,
 \qquad |\Delta(t)-\chi t^3|\le M t^4\quad(0\le t\le T).
\]

Here `T` is inside the established C.1 interval and is shortened to keep
the frozen clock inside that interval too. Constants depend only on this
fixed architecture, activation, data, initialized Gaussian law and the
source theorem's norm bounds. Neither a numerical radius nor a quantitative
width requirement is asserted.

Use `p=y/3` and the initialized fields and expectations of
[CUBIC_DERIVATION.md](CUBIC_DERIVATION.md), equations (1), (6), (9):

\[
 a(x)=2E_2[S H_x],\quad B_0=E_2[S^2]>0,\quad
 \mathcal A=p^\top(G\circ D+Q\circ V)p>0,
\]
\[
 J(x)=4E_2[S E_x]+\frac43\sum_b p_bE_2[H_xE_b],\quad
 \beta=\frac{8\mathcal A}{3B_0},\quad
 \chi=2\int_0^{2\pi}\cos(3\alpha)
                 [J(x(\alpha))-\beta a(x(\alpha))]\frac{d\alpha}{2\pi}.
\]

Equations (14)--(22) of that proof express every scalar here in at most
four upper Gaussian coordinates and the original two lower Gaussian roots,
without an operator oracle or a Gram inverse at a passive degeneracy.
Both trained hidden blocks and the moving readout are included. The
reused-matrix response mean product is retained. The identities

\[
 p^\top J_{\rm train}=\frac{16}{3}\mathcal A,
 \qquad p^\top(J_{\rm train}-\beta a_{\rm train})=0
\]

show why a positive hidden training contraction does not decide the
matched-risk sign. The positive cubic clock shift removes the advantage
in training speed before the teacher projection is taken.

The full proofs are split by role. CUBIC_DERIVATION gives the exact cubic
and Gaussian contraction; [MATCHING_AND_REMAINDER.md](MATCHING_AND_REMAINDER.md)
gives unique matching, passive-input capture and the uniform fourth-order
bound by integral estimates on the actual population flow. In its notation
the predictor coefficient `D(alpha)` equals `J(x(alpha))` here, its clock
coefficient `gamma` equals `beta`, and `C_Delta` equals `chi`.

If a rigorous scalar bound proves `chi>0`, then

\[
 \Delta(t)\ge\tfrac12\chi t^3>0\quad
 (0<t\le\min\{T,\chi/(2M)\}).
\]

If it proves `chi<0`, the same argument gives
`Delta(t)<=-|chi|t^3/2` on the corresponding interval. This implication is
proved; its sign premise is unproved. If `chi=0`, a later coefficient is
needed. Thus cubic is the first possible contribution, not a proved first
nonzero contribution.

## Hidden movement and activation nonaffinity at their supported scale

For each of the three training inputs, use the weighted initial fields
`T_a`, `R_a^hid` in CUBIC_DERIVATION (1). The integral estimates prove

\[
 Z_a^{(1)}(t)-Z_a^{(1)}(0)=2t^2T_a+O_{L^2}(t^3),\qquad
 Z_a^{(2)}(t)-Z_a^{(2)}(0)=2t^2R_a^{\rm hid}+O_{L^2}(t^3).
\]

Their squared RMS displacements are respectively
`4 E_1[T_a^2] t^4+O(t^5)` and
`4 E_2[(R_a^hid)^2] t^4+O(t^5)`. Their squared integrated speeds are
`(16/3)E_1[T_a^2] t^3+o(t^3)` and
`(16/3)E_2[(R_a^hid)^2] t^3+o(t^3)`. Both leading constants are strictly
positive. For completeness, C.3 proves `D=E[B B^T]` positive definite via
the nondegenerate Gaussian transpose innovation. The coefficient of `B_a`
in `T_a` is `p_a!=0`, proving `E[T_a^2]>0`. For the second layer,
`A_a=phi'(Z_a)T_a` has positive conditional variance in that same innovation:
its coefficient at index `a` is `p_a phi'(Z_a)^2!=0`. Projection on the finite
initial forward span cannot remove that conditional variance. The next
forward use of the same matrix therefore has a Gaussian innovation with
positive variance, which the training-only term `M_a` cannot cancel.
This proves `E[(R_a^hid)^2]>0`. All hypotheses are satisfied: tanh gates
are strictly positive, the training directions are pairwise nonparallel,
and all three labels are nonzero. No positive input-Gram eigenvalue is used.

The activation displacements have leading fields
`2 tanh'(Z_a)T_a` and `2 tanh'(Y_a)R_a^hid`, also nonzero in L2 because
the gates are everywhere positive. Thus activation and preactivation
displacements are order `t^2`, speeds order `t`; speed is zero at time zero.
The connector increment is
`2t^2 sum_b p_b U_b tensor h_b+O_op(t^3)` and its action on each fixed
training feature has a nonzero leading coefficient (`V` is positive definite
and `p_a Q_aa!=0`). This does not claim order-one displacement at arbitrarily
small time, global feature speed, or usefulness on unseen inputs by itself.

There is also a direct nonaffinity certificate. Put
`q=E[tanh(N)^2]`, where `N` is standard normal. The initialized hidden
preactivation variances are `1` and `q>0`. At variance `v>0`, the best
affine-fit error of tanh under `sqrt(v)N` is

\[
 \varepsilon(v)=E[\tanh(\sqrt v N)^2]
     -v\{E[\operatorname{sech}^2(\sqrt v N)]\}^2>0.
\]

Oddness removes the means; Gaussian integration by parts gives the displayed
covariance term. Strict Cauchy--Schwarz holds because tanh cannot agree with
an affine function on a full-support Gaussian law. Along each of the six
training hidden marginals, the variance and best-affine-fit error are
continuous by L2 continuity and Lipschitz tanh. After shortening `T`, the
variances stay at least `min(1,q)/2` and the affine-fit errors stay at least
`min(epsilon(1),epsilon(q))/2`. These are absolute, fixed-model local bounds,
not a depth-uniform or relative nonlinear-strength theorem.

## Evidence, effect size and terminal obligation

The finite deterministic cubic identities passed; the complete record is in
[SOURCE_AND_CHECKS.md](SOURCE_AND_CHECKS.md). The Gaussian contraction check
and the fixed integration resolutions are recorded in
[QUADRATURE.md](QUADRATURE.md). The final diagnostic value of `chi` is about
`+2.73e-4`; the last relative resolution change is about 1.69 percent and
no integration-error certificate exists. Numerical convergence is therefore
inconclusive under the predeclared gate. No sign, nonzero coefficient or
finite-time benefit is claimed from these values. The initial test risk is
exactly `1/2`; even a subsequently proved effect would be an early-time
cubic difference for this fixed witness, not a universal explanation of
feature learning.

The sole decisive obligation left by the current calculation is to prove a
nonzero signed bound for the explicit `chi` above, including the Gaussian
moments and circle integration errors if numerical certification is used.
A nonzero bound together with the proved fourth-order remainder completes
the local sign theorem. An exact zero requires a higher-order calculation.
The prescribed deterministic budget is exhausted and this bounded study
stops here; it does not switch teacher, dataset or architecture.

Finite-network consequences keep the actual small random initial readout.
The whole-circle predictions and risks converge with the established scope.
Exact finite loss-matching and any subsequently proved sign transfer are
asserted only on fixed `[delta,T]` with `delta>0`, in probability as width
tends to infinity and for every deterministic vanishing raw-GD step. No
width rate, fixed-width sign down to zero time or joint `delta_n->0` claim
is available. See MATCHING_AND_REMAINDER section 8 for the full argument.
