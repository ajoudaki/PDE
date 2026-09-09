# Moderate calibrated sine: direct local source bootstrap and the unresolved continuation

2026-09-08. This note studies the exact activation in the request, without decreasing its coefficient. It proves a local source estimate directly and derives the exact sine-specific conditional current return. It does not prove the all-finite-physical-time population theorem. No experiment was run and no preexisting proof was edited.

The original finite model, finite readout and raw metric are those in `studies/mean_field_peeling/two_sample_activation_design/PROOF.md`, Section 1. The exact finite Gaussian source equations, formal derivative convention, all source-time columns and current returns are those in `two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md`, equations (6)--(10), (24), (26), and (28). The generic fixed-program/common-action and cap-removal constructions are in that directory's `L3_LOCAL_COMPLETE_PROOF.md` and `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`. Their mathematical formulas were read; no review verdict was used as a premise.

## 1. Exact activation and auxiliary caps

Write

\[
 s_0=\sqrt{1+4v/25},\qquad
 \alpha=(1-4e^{-2}/5)/s_0,\qquad \beta=2/(5s_0),
 \qquad \Phi(z)=\alpha z+\beta\sin(2z).
\]

Here `v=(1-e^{-8})/2-4e^{-4}>0`. Since `e^{-2}<1/4`,

\[
 \alpha-2\beta=(1-4e^{-2}/5-4/5)/s_0>0.
\]

Thus Phi is a strictly increasing smooth bijection. The estimates

\[
 \Phi(0)=0,\quad |\Phi(z)|\le2|z|,\quad
 |\Phi'(z)|\le2,\quad |\Phi''(z)|\le2                 \tag{1}
\]

are sufficient below. The actual nonlinear coefficient beta is retained.

Use an auxiliary smooth odd contraction tau_R, with `|tau_R(q)|<=|q|`, `|tau_R'|<=1`, equal to q on `[-R,R]`, and bounded by `2R`. The backward gate is

\[
 D_R(z,q)=\alpha q+2\beta\cos(2z)\tau_R(q).             \tag{2}
\]

It obeys `|D_R(z,q)|<=2|q|`, `|partial_q D_R|<=2`, and
`|partial_z D_R|<=2|q|`. For every fixed R its derivatives are bounded. This is the original gate when R is removed; it does not cap the affine part or reset the readout.

Work first in feature time, with `c=(y_1/2,y_2/2)` and `P=Gamma diag(c)`, so `|P|<=1`, `sum|c_a|=1`. At finite width use the actual prescribed finite readout. Its population initial limit is zero; this replacement is made only after fixed-program convergence, not in the finite algorithms.

## 2. A cap-independent small primal interval

Let B=20, L=2 and N=2. The initial operator norms are at most 10 with probability tending to one, and the two first preactivation norms are at most 2. The initial readout norm tends to zero. On a primal ball with each first preactivation norm, both operator norms and the readout norm at most B, direct forward and backward induction gives, for each sample,

\[
 \|h^1\|_2\le LB,\quad \|h^2\|_2\le L^2B^2,
 \quad \|h^3\|_2\le L^3B^3,
\]
\[
 \|\delta^3\|_2\le L\|C\|_2,
 \quad \|q^2\|_2\le LB\|C\|_2,
 \quad \|\delta^2\|_2\le L^2B\|C\|_2,
 \quad \|q^1\|_2\le L^2B^2\|C\|_2.
                                                               \tag{3}
\]

Every one of the four parameter update norms is at most `L^3 B^3`; the first projected fields acquire at most this size per sample because `|P|<=1`. Consequently a sufficiently short interval, for example

\[
 S\le (100L^3B^3)^{-1},                                  \tag{4}
\]

stays inside that primal ball, for every fixed cap and sufficiently fine mesh. This follows directly by summing Euler increments up to the first exit; no nonlinear Lipschitz constant is used. The same estimate holds for the fixed-cap strong flow. In the population,

\[
 \|C(t)\|_2\le L^3B^3S.                                  \tag{5}
\]

The covariance rules for the four Gaussian groups now show that there is one explicit constant

\[
 D=2^{10}B^5                                             \tag{6}
\]

such that the Lp norm of each forward Gaussian source pair and the first root pair is at most `D sqrt(p)`, and the Lp norm of each backward Gaussian source pair is at most `D S sqrt(p)`, for every p>=2. Correlations and singular covariance matrices are retained. Indeed, each scalar Gaussian Lp norm is at most twice its standard deviation times sqrt(p); sum over two samples and use (3)--(5). D also bounds every forward primal L2 norm, and `D S` bounds every backward primal L2 norm used in learned moments. These are actual finite-program source variances, obtained from the bounded primal calculation, not assumed coordinate tails.

## 3. Direct source estimate at fixed moderate amplitude

Set

\[
 A_2=M_3=100D^2,\qquad A_3=M_2=100D^2 A_2,\qquad A=A_3.
                                                               \tag{7}
\]

Consider the exact source programs on `[0,S]`, with arbitrary sufficiently fine positive mesh. A forward coefficient bound means

\[
 |a^2_{kj}|\le A_2h_j,\quad |a^3_{kj}|\le A_3h_j\quad(j<k),
                                                               \tag{8}
\]

and a backward bound means

\[
 \sum_{j\le k}|b^3_{kj}|\le M_3 S,\qquad
 \sum_{j\le k}|b^2_{kj}|\le M_2 S.                    \tag{9}
\]

Here each block uses maximum absolute sample row sum, and the time row uses the sum of these block norms. In particular, the current block is included.

It suffices to take

\[
 S\le S_0:=\min\left\{1,(100L^3B^3)^{-1},
 (4L^6B^6)^{-1},(10000 D A^2)^{-1/2}\right\}.          \tag{10}
\]

All constants are fixed numbers for the actual moderate activation. No separation-dependent reduction of beta is made.

### 3.1 Moments on a bounded coefficient prefix

Let `U_l=max_{k in prefix} ||Z^l_k||_p/sqrt(p)`. From the exact source equations, (1), (8), (9) and the covariance bounds,

\[
 U_1\le D+LD S^2+L^2M_2 S\sum_r h_r U_{1,r},
\]
\[
 U_2\le D+A_2LD S^2+A_2L^2M_3 S\sum_r h_rU_{2,r},
\]
\[
 U_3\le D+A_3L^2S\sum_rh_rU_{3,r}.
\]

The same inequalities apply to deterministic prefix maxima. Iterating the positive Volterra majorant, with (10), gives

\[
 \max_{l,k}\|Z^l_k\|_p\le10D\sqrt p.                  \tag{11}
\]

For example, the middle bound is
`(D+A_2LD S^2) exp(A_2L^2M_3 S^2) sqrt(p)`, which is less than `10D sqrt(p)` under (10). No supremum over Gaussian times is taken.

The current input equations and the integrated readout then give

\[
 \|C_k\|_p\le20D S\sqrt p,
\]
\[
 \|q^2_k\|_p\le21D M_3 S\sqrt p,
 \qquad \|q^1_k\|_p\le21D M_2 S\sqrt p.               \tag{12}
\]

These estimates only use rows already needed to construct the current field; they may therefore be applied in the causal four-stage order below.

### 3.2 Formal derivative bounds with the current multiplier retained

Let `G=Phi'(Z)`, `V=partial_q D_R(Z,Q)`, and `L_curv=partial_z D_R(Z,Q)`. Then

\[
 |G|,|V|\le2,\qquad |L_{\rm curv}|\le2|Q|.             \tag{13}
\]

The exact derivative recursions cited above imply the following bounds. A bottom transpose-source preactivation derivative is at most

\[
 Lh_j\,\mathcal E_k;
\]

a middle transpose-source preactivation derivative is at most

\[
 A_2Lh_j\,\mathcal E_k;
\]

a complete middle or top forward-source preactivation derivative row is at most `mathcal E_k`. The top readout derivative row is at most `L S mathcal E_k`. One common majorant, in the appropriate population, is

\[
 \mathcal E_k=\exp\left\{8A^2S^2+
             2A\sum_{r<k}h_r |Q_r|_\infty\right\}.     \tag{14}
\]

For the top use Q=C; for the middle and bottom use their respective incoming fields. These inequalities follow by substituting (8)--(9) into the exact recursions and iterating
`x_k<=f+sum_{r<k}h_r lambda_r max_{v<=r}x_v`.
The strict source-time factor h_j is retained because the single-source forcing enters once at step j; there is no forcing at unavailable source times.

For clarity, (12) is already a pair-maximum bound, so no extra sample factor is needed in (14). A random variable with `||Q||_p<=K sqrt(p)` satisfies
`E exp(Q^2/(4 e K^2))<=2` by expanding its exponential. Hence
`E exp(uQ)<=2 exp(e K^2u^2)` for u>=0. Jensen with weights h_r/S proves

\[
 E\mathcal E_k^4
 \le2\exp\{32A^2S^2+e(168DA^2S^2)^2\}<16,
                                                               \tag{15}
\]

where (12), `M_2=A`, and (10) were used. Thus `||mathcal E_k||_4<2`, uniformly in cap, mesh and source covariance degeneracy.

The middle backward-output derivative row contains the current term

\[
 L_{{\rm curv},k}J_k,
\]

and the top row contains the corresponding `L_curv,k J_k+V_k 1 T_k`. They cannot be discarded. Cauchy--Schwarz, (12), and (15) give

\[
 E\sum_j|\partial_{\xi^3_j}\delta^3_k|
 \le 2N\|C_k\|_2+2L^2S
 \le (40\sqrt2 ND+2L^2)S,                            \tag{16}
\]

and, once the current b3 row is available,

\[
 E\sum_j|\partial_{\xi^2_j}\delta^2_k|
 \le2N\|q^2_k\|_2+2L^2M_3S
 \le(42\sqrt2 ND M_3+2L^2M_3)S.                     \tag{17}
\]

The complete current blocks are therefore controlled as well. Their actual formulas are

\[
 b^3_{ka,kb}=\mathbf1_{a=b}E[L^3_{{\rm curv},k,a}],
\]
\[
 b^2_{ka,kb}=\mathbf1_{a=b}E[L^2_{{\rm curv},k,a}]
       +b^3_{ka,kb}E[V^2_{k,a}G^2_{k,b}].             \tag{18}
\]

These are computed causally, without an implicit current-time inverse.

### 3.3 Literal closure in the four-stage order

The learned forward density is at most D^2, and a complete learned backward row is at most `D^2 S^3`, by the raw L2 bounds in Section 2 and `sum|c_a|=1`.

At each time k:

1. The bottom transpose response, including its feature derivative, is at most `2L^2 h_j` in expectation. Hence
   `|a2_kj|/h_j<=2L^2+D^2<A_2/2`.
   Only strictly past b2 rows are needed.
2. The middle transpose response is at most `2A_2L^2 h_j` in expectation. Hence
   `|a3_kj|/h_j<=2A_2L^2+D^2<A_3/2`.
   This uses the just bounded current a2 row and past b3 rows.
3. Equations (16) and the learned moment estimate give
   `|b3_k|_row< M_3 S/2`.
   This uses available current a3 but no current backward row. It then constructs q2_k and supplies (12) for that field.
4. Equation (17) plus its learned moment gives
   `|b2_k|_row< M_2 S/2`.
   The available current b3 row is retained. It then constructs q1_k.

All strict inequalities follow from D>=100, the choices (7), N=L=2, and S<=1. At time zero the forward rows are empty, C0=0 and both backward rows vanish. This supplies an induction through every time and every stage. Consequently (8)--(12) hold for the full programs on `[0,S_0]`, uniformly in R and fine mesh.

This is a genuine moderate-amplitude local source estimate. It is not the old affine perturbation argument with a hidden beta restriction.

## 4. Local uncut consequences and their scope

From (12), all three incoming-field tail norms have Gaussian decay, uniformly in cap and mesh. For (2), the reference-only asymmetric gate estimate is

\[
 |D_{R'}(z_A,q_A)-D_R(z_B,q_B)|
 \le L|q_A-q_B|+C R|z_A-z_B|
       +C|q_B|\mathbf1_{|q_B|>R},                    \tag{19}
\]

for R'>=R, including R'=infinity. The forward field is Lipschitz with linear growth. On the primal ball, propagation and rank-one update estimates therefore give the same cap comparison cost `C exp(CR-cR^2)` as the cited bridge. Thus a unique strong uncut feature flow exists on `[0,S_0]`, with restart uniqueness inside that already constructed interval, on the common Gaussian action spaces. The exact fixed-cap GF/GD and observable bridges apply to this activation because their hypotheses are precisely linear growth, bounded first two derivatives, and the established reference tails.

The third restriction in (10) gives `|g_R(s)|<=L^6B^6S<=1/4`, directly from (3),(5). Hence the symmetric physical clock has speed `ds/dt=2(1-g_R)` between 3/2 and 5/2 while this interval is used. In particular the physical interval `[0,S_0/3]` is covered. Both actual finite residuals remain in the finite physical comparison, as in the cited bridge. The local theorem includes the finite readout, reused matrices and the named joint GF/GD observables.

Nothing in this argument bounds source coefficients for all S or all physical T. The small S in (10) is a local construction interval, not an activation choice; selecting it does not prove the requested global result.

## 5. Exact sine averaging at the current return

There is a precise reason why Gaussian sine cancellation at initialization does not automatically control the trained source response.

At top source time k, let F_{k-1} be the sigma field of the strictly past top Gaussian source coordinates. All deterministic coefficient arrays are fixed. The readout C_k and the learned part of Z3_k are measurable with respect to this field. Gaussian regression gives, for each sample a,

\[
 Z^3_{k,a}=\mu_{k,a}+\eta_{k,a},
\]

where mu is past-measurable and eta is independent of the past, centered Gaussian, with deterministic variance sigma_{k,a}^2; this includes sigma=0. Since `Phi''=-4 beta sin(2z)`, the exact uncut conditional return is

\[
 E[\Phi''(Z^3_{k,a})C_k\mid F_{k-1}]
 =-4\beta e^{-2\sigma_{k,a}^2}C_k\sin(2\mu_{k,a}).     \tag{20}
\]

For the capped program replace C_k by tau_R(C_k) in (20). Both signs are possible in this expression as a function of its adapted mean and readout; sine periodicity alone supplies neither zero mean nor a negative sign. This observation is not an assertion that arbitrary adapted means and readouts are attainable by the neural flow.

Moreover,

\[
 \sigma_{k,a}^2
 \le E[(\xi^3_{k,a}-\xi^3_{k-1,a})^2]
 =E[(H^2_{k,a}-H^2_{k-1,a})^2].                       \tag{21}
\]

The first inequality uses the previous source itself as a candidate Gaussian linear predictor; the equality is the exact source covariance rule. On any raw bounded Euler prefix, the last quantity is at most `C_B^2 h_{k-1}^2`: the four update sizes are bounded independently of R by (3), and two forward Lipschitz propagations bound a one-step feature difference by `C_B h`. Therefore the damping factor in (20) is at least

\[
 e^{-2C_B^2 h_{k-1}^2},                               \tag{22}
\]

which approaches one as the mesh is refined. The current innovation is not a fresh variance-one Gaussian at every training instant. Applying the initialization factor e^{-2} at all trained times would be incorrect.

The identity `Phi''=-4(Phi-alpha z)` also does not remove the current multiplier: it rewrites it as `-4(Phi(Z)-alpha Z)Q`, whose second factor is still unbounded. Strict monotonicity does permit a scalar one-control coordinate cancellation. For correlated two-input control the exact Lie bracket obstruction in `BOUNDED_ACTIVATION_ROUTE.md`, Section 3, prevents simultaneous straightening of the two vector fields unless the activation is affine.

## 6. What continuation would require

The local proof gains its small quantities from `C0=0`, backward source variances O(S^2), and backward rows O(S). At a reached positive time, these quantities are nonzero. The existing Gaussian source history must be retained. Restarting the local proof with a fresh independent Gaussian initialization would change the model.

A sufficient global source program would establish, for each finite physical T and a raw stopping radius B, cap- and mesh-independent finite bounds on the actual forward response densities and complete backward response rows (or directly strong enough incoming-field tails). Constants may depend arbitrarily on T,B and this fixed activation. Under such a bound, the moment and derivative estimates above remain valid with finite constants, and the reference-only cap comparison removes the cap. Approximate energy can then remove the raw stop. This last source bound is not proved by the local bootstrap.

A plausible but unproved continuation criterion is that all existing source response row bounds, their moment envelopes and the needed history moduli stay finite at every finite reached time. A rigorous endpoint extension would have to retain the entire causal history and control new responses against every old source column. Bounded primal energy does not supply these quantities, and this note does not claim a generic reached-state local existence theorem from an arbitrary L2 endpoint.

The present mathematical progress is therefore: a direct moderate-sine local population construction and exact obstruction to automatic trained Gaussian phase averaging. The requested strong global joint population/GF/GD limit remains open in this route.
