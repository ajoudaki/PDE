# Small fixed nonlinear perturbation: response route under development

Status: research derivation, NOT a proved full two-sample theorem. The
affine baseline response-bound bridge and the detailed perturbation lemma
below are not yet independently audited. See CONTRACT.md for the exact
model and normalization. Nothing here upgrades the one-sample theorem to
two samples without the missing bridges.

## Candidate and exact useful perturbation

Consider the one-parameter family, in all three hidden layers,
\[
 \phi_\epsilon(z)=1+z+\epsilon\arctan z,
 \quad 0<\epsilon\le1,
 \qquad D_{\epsilon,R}(z,q)
   =q+\frac{\epsilon}{1+z^2}\tau_R(q).
\]
Here \(\tau_R\) is smooth, identity for \(|q|\le R\), bounded by
\(\min(|q|,2R)\), and has derivative between zero and one. It clips
ONLY the nonlinear part of the backwards gate. Thus
\(D_{\epsilon,\infty}(z,q)=\phi'_\epsilon(z)q\) exactly,
and the final model would contain no clipping. The affine baseline is
\(\phi_0=1+z\), NOT the proposed final activation.

Use \(D\) in all three backwards gates: the top input is \(W^{(4)}\),
the middle input is \(q^{(2)}=(W^{(3)})^*\delta^{(3)}\), and the
bottom input is \(q^{(1)}=(W^{(2)})^*\delta^{(2)}\).
Forward activations are never clipped. Work in the raw first-layer
coordinate; the old single-sample F transformation does not decouple
the two-sample input Gram matrix.

For any bounded-primal state ball, these exact bounds hold uniformly in R:
\[
 |\phi_\epsilon(z)-(1+z)|\le\pi\epsilon/2,
 \quad |D_{\epsilon,R}(z,q)-q|\le\epsilon|q|,
 \quad |D_{\epsilon,R}(z,q)|\le2|q|.
\]
Successive forward and backward differences at the SAME raw state give
\[
 \|\mathcal V_{\epsilon,R}(\theta)-\mathcal V_0(\theta)\|
       \le C_B\epsilon.                                      \tag{1}
\]
Here the feature vector field is the gradient direction of
\(g=(y_1 f_1+y_2f_2)/2\), with gates D in its auxiliary clipped version.
The norm uses the scaled first-layer L2 field, HS or operator norms of
matrix increments, and the readout L2 norm. Rank-one differences are
controlled by L2 norms of their two factors; bounded activation is not
needed. All constants may depend on the fixed primal radius and d.

The affine vector field is a polynomial in bounded operators and L2
fields, so it is locally Lipschitz in that norm. Comparing at the same
state as in (1), then using its Lipschitz estimate between states, gives
\[
 \sup_{s\le S}\|\theta_{\epsilon,R}(s)-\theta_0(s)\|
       \le C_{B,S}\epsilon                                  \tag{2}
\]
on any compact affine-baseline feature interval with a fixed primal
margin. This is a stopped comparison that prevents exit for sufficiently
small epsilon. The same estimate holds for finite-width flows and Euler
programs, when compared to their own affine references, and for the
population action Euler programs. Fixed-mesh/Euler errors can be added
separately. All forward and backward query L2 norms and their second-
moment kernels are then bounded and differ from baseline by O(epsilon),
uniformly in clip and sufficiently fine mesh. In particular there is no
need to compare square roots of large time-covariance matrices.

This closeness is NOT by itself an uncut existence or stability theorem:
an O(epsilon) L2 error does not produce uniformly vanishing tails.
The next step must control the actual finite-program responses.

## Finite-program response perturbation: proposed precise lemma

Let the exact two-sample scalar program use independent oriented Gaussian
source groups, arbitrary correlations over samples and times, and the
frozen-coefficient derivative convention. Its forward rows have blocks
\(a^{(\ell)}_{ks}\in\mathbb R^{2\times2}\), s<k; backwards rows
\(b^{(\ell)}_{ks}\) include s=k. The first-layer raw update contains
the fixed matrix \(\Gamma\operatorname{diag}(y)/2\), where
\(\Gamma_{ab}=x_a^Tx_b/d\). Learned forward/backward contractions
have the column label factor y_b/2. They must not be omitted from signs.

Wanted lemma: if the affine programs on [0,S] obey
\[
 \|a^{(\ell),0}_{ks}\|\le A_0\Delta,
 \quad \max_k\sum_{s\le k}\|b^{(\ell),0}_{ks}\|\le M_0
                                                               \tag{3}
\]
in a fixed finite-dimensional block row norm, and their primal norms
are uniformly bounded, then there is epsilon_*>0 independent of R,
mesh and width such that the actual epsilon programs for
0<epsilon<=epsilon_* obey the same bounds with fixed enlarged A,M.
The affine row bound (3) must be proved, not assumed to follow from
an operator-norm bound on the trained matrices. A separate worker is
checking that specific baseline bridge.

Here is the proposed proof mechanism, with the required quantitative
steps exposed for verification.

1. Stop before the first response-row exit from enlarged bounds A,M.
   Query source variances are uniformly bounded by (2). Under A,M, the
   scalar coordinate equations have at most linear growth. For example
   q2_k=zeta2_k+sum_{v<=k}b3_kv H2_v, while
   H2_k=1+xi2_k+sum_{r<k}a2_kr delta2_r+epsilon arctan(Z2_k),
   and |delta2_r|<=2|q2_r|. Minkowski in Lp and discrete Gronwall give
   max_k ||H2_k||_p+||q2_k||_p <= C(A,M,B,S) sqrt(p), p>=2.
   Bottom raw integration and q1=zeta1+b2 H1 give the same result.
   At the top C_k=Delta sum_{r<k} sum_a y_a H3_{a,r}/2,
   |delta3|<=2|C|, and Z3=xi3+a3 delta3 give the same bound.
   No maximum over Gaussian source times is needed: use row sums and
   Minkowski for each weighted sum, followed by Gronwall on Lp norms.

2. Formal gate derivatives satisfy
   \[
   \partial D_{\epsilon,R}(Z,q)
    =[1+\epsilon g'(Z)\tau'_R(q)]\partial q
       +\epsilon g''(Z)\tau_R(q)\partial Z,
   \quad g=\arctan.
   \]
   The first coefficient differs from 1 by at most epsilon; the second
   is bounded by 2 epsilon |q|. Forward derivatives differ from 1 by
   at most epsilon. Thus source-response envelopes have the form
   \[
    C\exp\{C\epsilon\Delta\sum_{r<k,a}|q_{a,r}|\}
   \]
   times the affine Gronwall factor. At the top q is C. At the bottom
   use the fixed input Gram matrix and its finite row norm. Step 1 and
   Jensen over times imply finite envelope Lp bounds independent of
   mesh/clip. Individual past source forcings carry one Delta; row
   sums for forward xi derivatives have direct forcing 1.

3. Compare these formal derivatives with the AFFINE scalar derivative
   system evaluated at the SAME deterministic coefficient arrays a,b,
   not necessarily the actual baseline arrays. In the equations the
   difference is epsilon times the envelope and at most one of the
   subGaussian coordinate fields. Variation of constants and Holder
   give error <=C epsilon Delta for an individual forward response,
   and <=C epsilon for a full backwards derivative row. Current source
   terms, zero at epsilon=0, contribute O(epsilon) and are retained.
   Every constant depends only on the enlarged A,M,B,S.

4. The affine frozen-coefficient response system is deterministic and
   Volterra. Its exact elementary recursions are as follows, with sample
   indices expressed as compatible 2-by-2 blocks. Put P=Gamma diag(y)/2.
   A bottom zeta1 source at s has derivative
   \[
    P^{(1)}_{k,s}=\Delta P\mathbf1_{s<k}
       +\Delta\sum_{r<k}P\sum_{v\le r}b^{(2)}_{rv}P^{(1)}_{v,s}.
   \]
   Its forward coefficient is P1 plus the learned Delta moment block.
   The middle zeta2 derivative has forcing a2_{ks} and recurrence
   \[
    P^{(2)}_{k,s}=a^{(2)}_{ks}\mathbf1_{s<k}
       +\sum_{r<k}a^{(2)}_{kr}
                         \sum_{v\le r}b^{(3)}_{rv}P^{(2)}_{v,s}.
   \]
   Its forward coefficient is P2 plus the learned Delta moment block.
   The top delta3 derivative is the common readout derivative, because
   every affine delta3_a equals C. The readout derivative has direct
   forcing Delta*y_b/2 at an earlier source and Volterra feedback
   obtained by inserting Z3=xi3+sum a3*(1,1)^T C in the readout sum.
   Finally the middle xi2 derivative is
   \[
    D^{(2)}_{k,s}=I\mathbf1_{k=s}
       +\sum_{r<k}a^{(2)}_{kr}
                         \sum_{v\le r}b^{(3)}_{rv}D^{(2)}_{v,s},
   \]
   and the affine b2 response is sum_{v<=k} b3_kv D2_vs.

5. Subtract the baseline coefficient equations from these deterministic
   recursions. Step 3 and the O(epsilon) learned-moment errors from (2)
   are forcing errors. If E_k is the maximum backwards row discrepancy,
   discrete variation of constants should give
   \[
    \max_s\|a2_{ks}-a2^0_{ks}\|/\Delta
       \le C\epsilon+C\Delta\sum_{r<k}E_r,
   \]
   and the identical type of bound for a3. The current b3 row discrepancy
   is bounded by C epsilon plus an integral of the prior a3 discrepancies;
   the current b2 discrepancy is bounded by C times the current b3
   discrepancy plus integrals of prior a2/b3 discrepancies. Therefore
   \[
    E_k\le C\epsilon+C\Delta\sum_{r<k}E_r.                \tag{4}
   \]
   Gronwall would give uniform O(epsilon) row closeness and close the
   first-exit bootstrap for epsilon small enough. Precise block norms,
   all summation factors and the current-row boundary need to be checked
   in the full lemma, not hidden in an assertion of continuity.

This route would control actual canonical two-sample program fields;
it does not postulate bounded Gaussian matrix actions on whole Lp spaces.

## Downstream bridge if the response lemma is completed

Step 1 then provides uniform subGaussian tails for C, q2 and q1 in all
actual auxiliary programs, hence in their fixed-clip flows. The asymmetric
gate comparison is exactly
\[
 \begin{split}
 D_{\epsilon,R'}(Z_A,q_A)-D_{\epsilon,R}(Z_B,q_B)
 ={}&(q_A-q_B)+\epsilon g'(Z_A)[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
 &+\epsilon[g'(Z_A)-g'(Z_B)]\tau_R(q_B)\\
 &+\epsilon g'(Z_A)[\tau_{R'}(q_B)-\tau_R(q_B)].
 \end{split}
\]
Thus its norm is at most
(1+epsilon)||q_A-q_B||+C epsilon R||Z_A-Z_B||
plus C epsilon times the reference tail norm. Chaining top, middle,
bottom gives a LINEAR-in-R Lipschitz loss C_B(1+epsilon R), not R cubed,
because each coefficient of the incoming q difference is at most 2.
The reference tails are the three fields C,q2,q1. Gaussian decay defeats
the exp(CR) Gronwall loss and yields uncut existence and uniqueness against
any bounded-primal competing solution, with reached-state restart.

The affine baseline interval can be chosen to end when its label
projection g first reaches 3/2. The separate radial/coercivity check is
intended to prove that this is a finite feature time S with finite primal
bounds. Then small-epsilon closeness makes g_e(S)>1 with a margin.
Population symmetry would identify f_a=y_a g_e, so its physical clock
s'=2(1-g_e) stays within that interval for all finite physical times.

IMPORTANT: finite-width sample predictions are not exactly symmetric.
Their GF or exact GD must NOT be replaced by a scalar computational clock.
Instead use the genuine TWO-residual physical vector field and compare
against its same-width full clipped reference. The population clipped
reference has the symmetric scalar description; fixed-clip finite-program
limits and local ODE/Euler stability provide its width limit on each [0,T].
Uniform primal bounds can be certified through stopped finite Euler
rank-memory length estimates and converging empirical velocity norms.
The asymmetric comparison then transfers the true finite full-residual
flow/GD. In raw first-layer coordinates there is no F-coordinate defect;
GD is already exact Euler for its physical raw field. Final proofs must
include this symmetry-error bridge and not inherit the one-sample clock
argument unchanged.

## Nonlinearity and non-laziness obligations

For fixed epsilon>0,
\[
 \inf_{a,b}E[\phi_\epsilon(Z)-aZ-b]^2
   =\epsilon^2\inf_{a,b}E[\arctan Z-aZ-b]^2.
\]
If the affine baseline hidden laws are nondegenerate Gaussians throughout
the compact feature interval, their arctan affine-approximation errors
have positive minima. The O(epsilon) state closeness could preserve these
errors for epsilon chosen small once, BEFORE width/time limits. This
would rule out effective affine collapse without needing unbounded lower
tails for the perturbed fields. Baseline Gaussianity and nondegeneracy
must be established; a separate worker is checking the latter mechanism.

Non-laziness must be proved for the final epsilon model, not inferred from
its distance to an affine model. A promising initial certificate is the
positive definiteness of the initial pair of top backward sources:
delta3_a'(0)=Hbar3_0 phi'_epsilon(Z3_a0). The initial Z3 pair should have
a nonsingular Gaussian law even at rho=-1, because the offset makes the
first feature pair noncollinear. The nonconstant positive gate gives a
nonconstant ratio between these two top derivatives, so their 2-by-2
second-moment matrix is positive definite. Two backwards Gaussian query
calculations then propagate positive conditional noise covariance to
the middle and first layers; multiplication by the input Gram cannot
annihilate every component even at its rank-one antipodal boundary.
This would give positive initial hidden movement in all layers and a
positive second-order change of the label-projected output kernel.
These details remain to be proved and independently audited.

No full result or universally fixed activation has yet been certified.
