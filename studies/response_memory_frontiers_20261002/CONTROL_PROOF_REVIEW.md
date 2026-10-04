# Independent internal review of the controlled-flow candidate

Reviewed on 2026-10-02. This is an isolated internal proof review, not a
promotion review or approval to change maintained material. The frozen
candidate was not edited.

**Verdict: PASS for the stated fixed-width, finite-horizon controlled-flow
proposition and its conditional finite-menu consequence.** I found no
counterexample or unresolved substantive proof gap under its stated
assumptions. The passage from physical time to a possibly paused clock is
valid for arbitrary bounded measurable controls. The constants in the
tracking estimate can indeed be chosen independently of the control and
memory order. A small proof-order clarification would make the existence
argument easier to verify.

**This verdict does not establish the practical small-order conjecture.**
In particular, the frozen pilot's PASS conditions need not exhibit accurate
prediction and inaccurate credit reconstruction at the same order, and
need not establish motion of the feature history actually being compressed.
These are material limitations on interpreting a future pilot PASS, not
counterexamples to the theorem. No training or GPU experiment was run.

## Input boundary and exact coverage

I read the complete candidate, all 1,620 lines of `paper/main.tex`, and
every mathematical file included by it. There are no further `input` or
`include` dependencies in those included files. I did not read the study
README, other route artifacts, other studies, history, other reviews,
archived book sources, or author discussions. The complete paper was read
for dependency coverage; this report does **not** purport to independently
validate every unrelated population theorem or experimental claim in it.

The controlled proposition uses the paper's finite-dimensional Legendre
tail argument, moment equations, projection-energy identity, and
bounded-activation continuation mechanism. I checked those dependencies
directly, including their adaptations to measurable controls. The
small-label, Gaussian, width-uniform, and all-time arguments are not
dependencies of this proposition. No external novelty or priority claim
was audited, and no linked external paper was fetched.

The exact SHA256 values of the scientific inputs read were:

```text
cebe78cac01f339a1abb497982acc4a7ed678cf3ad429022e15c3b9a02acb78d  studies/response_memory_frontiers_20261002/CONTROL_CANDIDATE.md
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1  paper/results.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4  paper/proof_finite_time.tex
14cfb87d7f4932131c984781fc0bc03b955f883d4fc909c4794c2be4bcc1bedf  paper/comparison_appendix.tex
f1a5c87937b1c805faa89edee9fb2ad2809de1f873b4e83888ccf5e5cdf673e2  paper/sphere_appendix.tex
```

Required process sources read: canonical notation and its
`neural-response-memory.md` reference; the rigorous-proof skill; and the
research skill with its adversarial-audit reference. The explicit isolated
assignment replaced author startup reading. No scientific input needed
for the controlled theorem was missing. Implemented event handling,
solver errors, and actual memory use remain unassessed because no
implementation or experiment output was an assigned input.

## What is being proved

The data list, dimensions, checkpoint, activations, control bound \(U\),
and horizon \(T\) are fixed. Every activation has bounded value and
derivative and a locally Lipschitz derivative. For each measurable

\[
u:[0,T]\longrightarrow[0,U]^m,
\]

the dense and reconstructed networks start at the same physical checkpoint
and receive the same function \(u(t)\). Each model evaluates its own
residuals. In the closure, the clock speed is

\[
\rho_u(t)=\left(m^{-1}\sum_a[u_a(t)r_a(t)]^2\right)^{1/2}.
\]

The theorem asserts unique absolutely continuous solutions for all integer
\(q\ge1\), and a common finite constant \(C_T\) with

\[
\sup_u\sup_{t\le T}
\|\widehat\theta_{q,u}(t)-\theta_u(t)\|_2
\le C_T/\sqrt{q(q+1)}.
\]

The norm is the unnormalized product Euclidean/Frobenius norm. Width,
sample count, checkpoint, and horizon may enter \(C_T\). This is neither
a width-uniform result nor a guarantee at a practically small order.
The two physical trajectories need not have equal clock values.

## Local existence, clock pauses, and continuation

At fixed \(q\), reconstruction is smooth in the raw moments and clock
on \(\tau>0\). Network responses are locally Lipschitz there, uniformly
for \(u\in[0,U]^m\); the weighted residual norm is Lipschitz as a norm
of a locally Lipschitz vector. The right-hand side is measurable in time
and is uniformly bounded and Lipschitz in state on each compact subset.
Thus the integral equation on a sufficiently short interval maps a
closed ball of continuous paths to itself and contracts in the supremum
norm. This gives the local Carathéodory solution and uniqueness claimed
in Step 1. No continuity of \(u\) is used.

There is a minor order-of-presentation issue: Step 1 invokes moment
representations to obtain global bounds, while Step 2 establishes the
representations using a bounded raw state. It is enough to first work on
**any compact subinterval of the local maximal solution**. The raw state
is bounded there simply by continuity; global continuation is not needed
for this preliminary bound. Every raw derivative then has norm at most
\(K_q\rho_u\), because

\[
|u_ar_a|\le\sqrt m\,\rho_u
\]

and all other state factors are bounded locally. The same estimate holds
for reconstructed physical parameters and features. After the history
representation is established on such local subintervals, the uniform
bounds in Step 1 apply to the entire maximal interval and give continuation.
This resolves the apparent dependency loop without adding an assumption.

Here is the clock argument in a form that includes zero-activity sets
with positive measure and no interior. For \(s\le t\), the local velocity
bound gives

\[
\|\theta(t)-\theta(s)\|
\le K_q\int_s^t\rho_u(v)\,dv
=K_q[\tau(t)-\tau(s)].
\]

Consequently equal clock values give equal physical states, and the
physical state and forward features factor through Lipschitz functions
of \(\xi=\tau(t)\). Extend forward features constantly over the unit
prefix. They match continuously at \(\xi=1\), hence belong to \(H^1\)
on every finite clock interval. A generalized inverse of the continuous
nondecreasing clock supplies a measurable backward history. Nontrivial
clock fibers are constant intervals; their clock values have zero
Lebesgue measure. For growing integrals the substitution is

\[
\int_0^t \rho_u(s)v(s)p_j(\tau(s)/\tau(t))\,ds
=\int_1^{\tau(t)}\widetilde v(\xi)p_j(\xi/\tau(t))\,d\xi.
\]

For the backward source, \(\rho_u b_a=u_ar_a\delta_a\) almost
everywhere, including the zero-speed set under the stated zero
convention. The change of variables is valid for bounded measurable
histories. Adding the respective prefixes and differentiating gives
exactly (3); uniqueness of this finite linear moment system identifies
its solution with the stored moments.

When \(\rho_u=0\), every raw and physical derivative vanishes almost
everywhere. This does not freeze the future control. A simple admissible
check is \(n=m=d=1,L=2,\phi_1=\phi_2=1,y=1,w(0)=0\), with \(u=1\)
on \([0,1]\), \(u=0\) on \([1,2]\), and \(u=1\) on \([2,3]\). If
\(a(t)=\int_0^t u(s)\,ds\), then

\[
w(t)=1-e^{-2a(t)},\qquad
\rho_u=u e^{-2a(t)},\qquad \tau(t)=1+w(t)/2.
\]

Both models pause and reactivate correctly. If instead every data
residual is zero, all later admissible controls leave the state fixed;
the candidate does not assert otherwise. The paper's autonomous
backward-uniqueness argument against finite-time stopping is not
silently reused for these controlled equations.

The common readout bound is valid even though a time-dependent weighted
loss need not decrease:

\[
\frac d{dt}\|w\|^2
=\frac nm\sum_a u_ay_a^2
 -\frac{4n}m\sum_a u_a(f_a-y_a/2)^2
\le nUY^2.
\]

This proves the candidate's \(B_w,R,S,A\) bounds. Descending from
\(\|\delta^{(L)}_a\|\le s_LB_w\), the normalized weighted drive has
sample RMS one on the active set, so

\[
m^{-1}\sum_a\|b_a^{(\ell)}\|^2\le\beta_\ell^2.
\]

Projection contraction and sample/history Cauchy–Schwarz give

\[
\|\widehat W^{(\ell)}-W_c^{(\ell)}\|_F
\le\frac2n\sqrt{S\beta_\ell^2 A\alpha_{\ell-1}^2}
\le\frac{2A}n\beta_\ell\alpha_{\ell-1}.
\]

Only already bounded upper layers enter the next backward bound, so
this descending induction is not circular. The dense increment has
the stated smaller \(2S\beta_\ell\alpha_{\ell-1}/n\) bound, and
the first-layer bound follows by integrating its exact update.
Individual backward histories are also bounded, since
\(|u_ar_a|/\rho_u\le\sqrt m\). At fixed \(q\), finite history length
and \(\tau\ge1\) bound all raw moments. The raw right-hand side is
then uniformly bounded on the resulting compact region, giving a limit
at a hypothetical finite maximal endpoint and allowing local extension.
This proves existence through \(T\) for every order.

The cases \(U=0\), \(T=0\), or \(S=0\) are harmless: no displayed
estimate divides by \(S\), and zero total activity gives identical
stationary physical paths.

## Reconstruction and the exact energy identities

The \(1/n\), \(1/m\), mobility, and sign factors in (1)–(3) agree with
the paper. The zero backward prefix ensures exact physical initialization
at an arbitrary nonzero checkpoint readout; there is no missing initial
product subtraction for this particular prefix.

A fixed monomial basis gives a direct derivation requiring no derivative
of the inserted histories. Let \(v_q(\xi)=(1,\xi,\ldots,\xi^{q-1})^\top\),
\(G=\int_0^\tau v_qv_q^\top d\xi\), and
\(M_h=\int_0^\tau h v_q^\top d\xi\), with \(M_b\) defined similarly.
The projected pairing is \(M_bG^{-1}M_h^\top\). Since \(\tau\ge1\),
\(G\) is invertible, and differentiating in physical time gives

\[
\frac d{dt}(M_bG^{-1}M_h^\top)
=\rho_u\{b(h^*)^\top+b^*h^\top-b^*(h^*)^\top\}
\]

almost everywhere. Subtracting the exact controlled update yields (6)
with its positive sign. Applying the same calculation to the energy
of one history gives

\[
\frac d{dt}\left[\int_0^\tau\|v\|^2d\xi
 -\operatorname{tr}(M_vG^{-1}M_v^\top)\right]
=\rho_u\|v-v^*\|^2.
\]

The initial projection error is zero for both prefixes, proving (7).
The formulas are identities of absolutely continuous functions; jumps
of \(u\) or \(b\) produce no impulse. Cauchy–Schwarz in the positive
measure \(\rho_u(t)dt\), applied sample by sample, then proves (8).
Thus (8) controls accumulated **absolute** defect, not merely a signed
same-history reconstruction error.

I also checked the raw Legendre algebra directly. With
\(D=\operatorname{diag}(2j+1)\), \(d_j=2j+1\), and the triangular
matrix \(T_{jj}=j,T_{jk}=2k+1\) for \(k<j\), the cancellation is

\[
D+T^\top D+DT=dd^\top.
\]

The exact-arithmetic scratch check verifies every matrix entry at
\(q=1,2,3,7,16,32\). The identity itself also follows immediately
entrywise for arbitrary \(q\).

## Uniform source estimate and propagation

The paper's Legendre estimate applies to the prefix-extended forward
histories just shown to be in \(H^1\). Its proof uses the weighted
Legendre Sturm–Liouville equation, integration by parts, Bessel's
inequality, and polynomial density; no smoothness of the backward
history enters. It gives exactly (9).

Treat all samples of \(b\) as one Hilbert-valued history, with squared
norm \(m^{-1}\sum_a\|b_a\|^2\). Endpoint evaluation on polynomials
of degree below \(q\) has norm \(q/\sqrt\tau\). Its projected
endpoint norm is therefore at most \(q\beta_\ell\), and its
endpoint error at most \((q+1)\beta_\ell\). Consequently

\[
\|E_\ell/\rho_u\|_F^2
\le\frac{4(q+1)^2\beta_\ell^2}{n^2}
       \frac1m\sum_a\|h_a-h_a^*\|^2
\]

on the active set. Integrating, using (7), then (9), leaves the
factor \((q+1)/q\le2\), which gives (10). This is the crucial
order-independent estimate; no credit derivative or switch count has
entered it. Defining the quotient as zero on pauses is legitimate.

The first-layer clock derivative is at most \(s_1v_1X\).
Differentiating subsequent layers, applying the squared three-term
triangle inequality, and using \(\|W^{(\ell)}\|_{\rm op}\le D_\ell\)
gives precisely (11), including the extra
\(\alpha_{\ell-1}^2\) multiplying the squared-defect bound. The
induction goes upward through forward layers and yields \(Z_\ell^*\)
independent of \(q,u\). The preliminary \(q\)-dependent Lipschitz
bound was used only to justify this calculation and is replaced here.

The zero backward prefix gives
\(m^{-1}\sum_aD_{b,\ell,a}\le S\beta_\ell^2\). Applying sample
Cauchy–Schwarz in (8), combining it with (9), and summing block norms
proves (12), with exactly

\[
B=\frac An\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}.
\]

A convex product of the bounded physical balls contains both paths
and all joining segments. On it, the dense vector field is locally
Lipschitz uniformly over \(u\in[0,U]^m\): bounded gates and their
local Lipschitz constants suffice at fixed width. Thus one common
\(\Lambda\) gives

\[
e(t)\le\int_0^t\|E(s)\|\,ds+\Lambda\int_0^t e(s)\,ds,
\qquad
\sup_{t\le T}e(t)\le e^{\Lambda T}B/\sqrt{q(q+1)}.
\]

A uniform bound for the ordinary prediction Jacobian on this region
and a bounded input set proves the prediction conclusion. All constants
were selected from fixed data and bounds before choosing \(u,q\), so
taking the supremum over measurable controls is justified. Values of a
control on a null set do not alter its Carathéodory solution.

## Policy quantifiers and resource consequences

The finite-menu implication is correct under its stated uniform
prediction certificate. Reverse triangle inequalities imply
\(|J-\widehat J|\le\varepsilon_q\) and
\(|C-\widehat C|\le\varepsilon_q\). Any control with
\(C\le c-2\varepsilon_q\) enters the surrogate feasible set; its
comparison with a surrogate minimizer gives two objective-error terms.
Every selected surrogate-feasible control satisfies \(C\le c\).

Clarify the empty-set sentence: if the surrogate feasible set is empty,
there is no selected certified action. If it is nonempty but the
stricter true comparator set is empty, the selected action can still
have certified retention, while the comparator inequality is vacuous
(or its minimum needs the \(+\infty\) convention). This is a minor
presentation issue, not a failure of the argument.

Uniformity over open-loop functions does not by itself compare two
trajectories that each feed their own state into the same feedback
policy. The candidate expressly distinguishes these quantifiers.
The statement about a separate Lipschitz-feedback argument is
appropriately conditional. A discontinuous threshold controller, an
intervention derivative, or a global replanning guarantee is not
established. The physical-checkpoint Markov property and fresh
zero-backward-prefix restart are correctly distinguished from arbitrary
changes to hidden moment coordinates.

The persistent evolving-state and shared fixed-matrix counts are
algebraically correct. A useful total-storage comparison must include
the shared source: for \(B_{\rm trial}\) simultaneous branches, saving
hidden storage against \(B_{\rm trial}\) independent dense branches
requires

\[
2mq/n<1-1/B_{\rm trial},
\]

before workspace and control storage. The candidate's \(2mq\ll n\)
criterion addresses the evolving branch state; it is not an unconditional
total-memory advantage, especially for one branch. The per-evaluation
work still contains fixed dense matrix actions. Arbitrarily measurable
inputs need an evaluation mechanism, and an arbitrary event table can
grow with the number of switches. These restrictions are acknowledged
in the candidate. There is no runtime theorem for arbitrary measurable
controls, nor an implemented resource benchmark in this review.

## Remaining weaknesses and limits of a future pilot PASS

1. **Minor proof presentation:** establish the local clock/history
   representation before using it for global continuation. The local
   compact-subinterval argument above closes this without a new
   mathematical assumption.

2. **Minor mechanistic illustration:** a nonconstant affine history
   has zero order-two tail on an ordinary interval, but cannot be
   the full prefix-extended forward history of this construction.
   A polynomial that is constant on the unit prefix is constant
   everywhere. Affine motion only after the prefix generally leaves
   nonzero error. For example, on \([0,2]\),
   \(h(\xi)=(\xi-1)_+\) has best affine projection
   \(\xi/2-1/4\) and squared tail \(1/24\). Taking \(b=h\) makes
   the pairing error in (14) exactly \(1/24\). Thus the candidate's
   affine example is valid as an abstract same-history illustration,
   but needs this prefix qualification before being used as an exact
   nonstationary witness for the stated algorithm.

3. **Material pilot inference gap:** the accuracy gate is imposed on
   \(q=7\), while the rough-credit gate permits either tested order.
   A result with accurate \(q=7\) prediction and accurate \(q=7\)
   credit, but inaccurate \(q=3\) prediction and rough \(q=3\)
   credit, can pass. That result would not demonstrate the proposed
   accurate-prediction/poor-credit mechanism at one order. A future
   report must require or explicitly exhibit both properties for
   the same \((N,q)\) before claiming that witness.

4. **Material pilot inference gap:** with \(L=2\), the compressed
   forward history is \(h^{(1)}\), while the motion gate accepts
   either hidden layer and does not identify which trajectory must
   satisfy it. Motion of \(h^{(2)}\) alone does not exclude an
   effectively constant recorded \(h^{(1)}\); motion only in an
   inaccurate closure would not establish dense feature learning.
   The nontrivial witness should exhibit motion of the relevant
   retained forward history in the dense continuation and in the
   accurate closure. The frozen gate as written does not ensure it.

5. **Unassessed numerical validity:** one reserved refined trajectory
   cannot by itself assess discretization sensitivity of both members
   of every dense/closure comparison. The candidate does not specify
   how that single refinement supplies a sensitivity scale for all
   gate-critical cases. Report unassessed cases as such; observed
   agreement or one coarse/fine comparison is not a continuous-time
   certificate. This affects empirical interpretation, not the
   exact ODE theorem. No solver implementation was reviewed here.

6. **Open practical consequence:** exponential propagation can make
   the proved \(C_T\) unusable, and an accurate pilot does not supply
   a validated local propagation bound or a useful policy ranking.
   The candidate recognizes these limitations. No claim of efficient
   control, improved continual-learning performance, or broad
   generalization is justified by the present proof review.

The strongest attempted structural counterexamples—zero activity with
later reactivation, control changes on null sets, arbitrary switching,
nonzero-readout prefix jumps, and possible \(q\)-dependent amplification
of projected endpoint values—do not invalidate the stated theorem.
The surviving concerns concern presentation and the bridge from that
theorem to a practical mechanism witness.

## Actual non-training checks

The review-owned script is
`data/generated/response_memory_frontiers_20261002/control_proof_review/check_algebra.py`.
It uses Python's exact rational arithmetic and was executed successfully.
It checks the Legendre dilation matrix identity at the six orders listed
above and the \(1/24\) prefix counterexample exactly. Its output records
zero training runs and zero GPU calls. All inequalities, quantifier
checks, and measurable-clock arguments above were checked analytically;
the finite-order arithmetic check is a supplementary sign/factor check,
not the proof for arbitrary order.

No frozen source was changed, no repository API was modified, and no
result was promoted into the maintained book or paper.
