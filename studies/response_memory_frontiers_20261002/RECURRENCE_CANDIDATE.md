# Recurrent route: paired histories of learned slow feedback

Frozen candidate and pilot contract, 2026-10-02. Independent scoped recurrence
route. No other studies, route drafts, or archived book were read. Status:
**secondary candidate; exact conditional foothold, untested mechanism**.

The possible contribution is that autonomous paired training histories preserve
the recurrent response selected by dense training at a rank where generic
low-rank training loses it. Such memories could also expose a small nonlinear
feedback problem for equilibrium inference and exact implicit credit. These
are separate claims. Low-rank equilibrium reduction and critical-mode control
are already prior art. Neither is claimed as new here.

## Source coverage

Read completely: paper/main.tex and its six included mathematical sources:
results.tex, proof_alltime.tex, proof_tracking.tex, proof_finite_time.tex,
comparison_appendix.tex, sphere_appendix.tex. Required canonical-notation,
neural conventions, conjecture, adversarial, experiment-design, and proof
skills were read. The manuscript is an authorized input, not promoted book
material. Its feedforward all-time theorem does not imply the recurrent
claims below.

Primary literature was inspected for the following methods, not exhaustively
reviewed for theorem correctness:

| Source | Consequence for novelty |
|---|---|
| [DEQ, Bai et al. 2019](https://arxiv.org/abs/1909.01377) | Equilibrium prediction, implicit credit, and low-rank Broyden inverse updates already avoid depth-proportional memory. |
| [SHINE, Ramzi et al., v4](https://arxiv.org/pdf/2106.00553) | Forward quasi-Newton matrices are reused for backward inverse actions; §2.3 adds outer-problem-aware secants. Source-aware numerical reuse is a necessary solver control. |
| [Schuessler et al., correlated low-rank recurrent networks](https://arxiv.org/pdf/1909.04358) | Fixed-point manifolds and the effects of correlations with the random background are known. A rank-one perturbation need not produce only one spectral outlier. |
| [Bai et al., Jacobian regularization](https://proceedings.mlr.press/v139/bai21b.html) | Stabilizing equilibrium training is established. Regularization changes the dense training reference. |
| [Silva, response renormalization, 2026-08](https://arxiv.org/html/2608.23725v1) | §2, equations (16)–(18), already uses local-plus-low-rank Jacobians, Woodbury, and a collective denominator. Its singular values are not those of the full Jacobian. |
| [Borisevich, certified DEQ continuation, 2026-09](https://arxiv.org/html/2609.16485v1) | §4.1 gives the determinant/inverse reduction; §3–4 separates branch selection, conditioning, and cost certificates. The remaining distinction here is fidelity to dense learning from endogenous histories. |

SHA256, in the source order listed above:

    60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95
    6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1
    f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d
    e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be
    07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4
    14cfb87d7f4932131c984781fc0bc03b955f883d4fc909c4794c2be4bcc1bedf
    f1a5c87937b1c805faa89edee9fb2ad2809de1f873b4e83888ccf5e5cdf673e2

## Exact recurrent foothold

Training time is \(t\); an inference iteration uses a different index. For
sample \(a=1,\ldots,m\), fixed input injection \(u_a\in\mathbb R^n\), learned
\(W\in\mathbb R^{n\times n}\), and target field \(y_a\in\mathbb R^n\), define a
selected regular equilibrium and vector-output loss:

\[
z_a=Wh_a+u_a,\quad h_a=\phi(z_a),\quad e_a=h_a-y_a,\quad
\mathcal L=\rho^2=\frac1{mn}\sum_a\|e_a\|_2^2 .
\]

Let

\[
D_a=\operatorname{diag}(\phi'(z_a)),\quad K_a=I-D_aW,\quad
\lambda_a=K_a^{-\top}e_a,\quad \delta_a=D_a\lambda_a.
\]

The credit \(\delta_a\) already contains the vector residual. This is the exact
correspondence to the manuscript's product \(r_a\delta_a\), not its
residual-free backward response. Assume each selected branch exists and
\(K_a\) is nonsingular. Differentiation gives

\[
K_a\,\mathrm dh_a=D_a(\mathrm dW)h_a,\qquad
\mathrm d\mathcal L=\frac2{mn}\sum_a\delta_a^\top(\mathrm dW)h_a.
\]

Unit-mobility dense gradient flow therefore satisfies exactly

\[
\dot W=-\frac2{mn}\sum_a\delta_a h_a^\top,\qquad
W(t)=W_0-\frac2{mn}\sum_a\int_0^t\delta_a(s)h_a(s)^\top\,\mathrm ds. \tag{1}
\]

Implicit credit supplies the paired history without RTRL or truncating a
finite-loop adjoint. Training a fixed finite number of loops is a different
reference; its infinite-loop gradient limit requires additional justification.

For the simple residual-speed implementation set \(b_a=\delta_a/\rho\),
\(\dot\tau=\rho,\tau(0)=1\). The constant forward prefix on \([0,1]\) equals
\(h_a(0)\); the backward prefix is zero. Define shifted Legendre moments

\[
\bar h_{a,j}=\int_0^\tau h_a(\xi)p_j(\xi/\tau)\,\mathrm d\xi,\quad
\bar\delta_{a,j}=\int_0^\tau b_a(\xi)p_j(\xi/\tau)\,\mathrm d\xi .
\]

The first \(q\) moments evolve autonomously:

\[
\begin{aligned}
\dot{\bar h}_{a,j}&=\rho h_a-\frac{\rho}{\tau}
 \left(j\bar h_{a,j}+\sum_{k<j}(2k+1)\bar h_{a,k}\right),\\
\dot{\bar\delta}_{a,j}&=\delta_a-\frac{\rho}{\tau}
 \left(j\bar\delta_{a,j}+\sum_{k<j}(2k+1)\bar\delta_{a,k}\right),\\
\widehat W_q&=W_0-\frac2{mn\tau}\sum_{a,j<q}
 (2j+1)\bar\delta_{a,j}\bar h_{a,j}^\top . \tag{2}
\end{aligned}
\]

Only \(\bar h_{a,0}(0)=h_a(0)\) is nonzero initially. All equilibria and credit
in (2) belong to its own current reconstructed network. The raw update divides
by \(\tau\), not \(\rho\), and stays defined at zero loss. With stars denoting
projected endpoint values, differentiation gives the exact product defect

\[
\dot{\widehat W}_q=F(\widehat W_q)+E_q,\qquad
E_q=\frac{2\rho}{mn}\sum_a(b_a-b_a^*)(h_a-h_a^*)^\top . \tag{3}
\]

An equilibrium solver error is additional to \(E_q\); it is not absorbed by
the algebra. The initial backward prefix generally jumps for vector outputs.

## Conditional theorem available with the joint clock

This proposition is internally derived and awaits independent review. It is
not claimed for the residual-speed pilot merely because both use moments.

Suppose \(\phi\in C^{2,1}_{\mathrm{loc}}\), and a compact regular-branch
parameter tube contains the dense path on \([0,T]\) in its interior. On an
open neighborhood of that tube, require a specified \(C^{2,1}\) equilibrium
branch per sample and bounded \(K_a^{-1}\). For the paper's joint-clock
construction with \(\Psi=(h_a,b_a)_a\), \(g=\rho+\|\dot\Psi\|\), mass
\(\rho\,\mathrm dt\), matching constant forward/backward prefixes, and shared
Gram \(G\), use

\[
\widehat W_q=W_0-\frac2{mn}\sum_a
 [\bar\delta_aG^{-1}\bar h_a^\top-b_a(0)h_a(0)^\top].
\tag{4}
\]

Its moment equations are the weighted equations in the paper, with backward
source \(\delta_a\). Then, for sufficiently large \(q\), this flow exists
through \(T\) and

\[
\sup_{t\le T}\|\widehat W_q(t)-W(t)\|_F=O_{n,T}(q^{-2}). \tag{5}
\]

Proof: on the tube, response maps and \(F\) have bounded values and derivatives.
The dense residual has a positive finite-horizon lower bound when initially
positive, since \(|\dot\rho|\le C\rho\). Stop closure at tube exit or half
this bound. For weighted projection error
\(\mathscr D_v=\|v-\Pi_tv\|_{L^2(\mu_t)}^2\), differentiation yields

\[
\dot{\mathscr D}_v=\rho\|v-v^*\|^2,\qquad
\int_0^t\|E_q\|_F\,\mathrm ds
\le\frac2{mn}\sum_a\sqrt{\mathscr D_{b_a}\mathscr D_{h_a}}.
\]

Projection contraction first bounds the right side independently of \(q\).
Thus physical total variation is bounded. Bounded derivative of \(\Psi\)
then bounds \(\tau\le\Lambda_T\), also independently of \(q\).
The matching-prefix history is continuous, its clock speed is at most one,
and \(\mathrm d\mu_t\le\mathrm d\xi\). The Legendre estimate gives

\[
\sum_a(\mathscr D_{b_a}+\mathscr D_{h_a})
\le \frac{\Lambda_T^2(\Lambda_T-1)}{4q(q+1)} .
\]

The defect bound, \(2\sqrt{uv}\le u+v\), and Gronwall prove (5) up to stopping.
For large \(q\) the bound excludes either stop. Positive prefix Gram and
bounded moments give fixed-order continuation. The zero-loss initial case
is stationary. Constants depend on the regularity margin; there is no
width-uniform, all-time, or bifurcation-crossing statement.

This transfers the manuscript's joint-clock proof, avoiding its feedforward
triangular derivative bootstrap. Computing the joint clock requires additional
directional implicit solves. Those would have to be charged in an eventual
runtime claim.

## Exact inference reduction, and why it is not the contribution

At a fixed training state, (2) gives \(\widehat W_q=W_0+UV^\top\), rank at most
\(R=mq\), where columns are scaled backward moments and forward moments.
For (4) the matching-prefix subtraction adds \(m\) fixed columns, so
\(R\le m(q+1)\). If
\(\operatorname{Lip}(\phi)\|W_0\|_{\mathrm op}\le\kappa_0<1\), the inner problem

\[
h_a(c)=\phi(W_0h_a(c)+Uc+u_a),\qquad c\in\mathbb R^R
\]

is uniquely solvable at uniform contraction rate \(\kappa_0\).
The original equilibrium is exactly equivalent to \(c=V^\top h_a(c)\).
Thus difficult learned feedback can be treated in \(R\) variables while
the large reservoir relaxation remains fast. The outer equation need not be
contractive or globally single-valued.

At a solution, put

\[
A_a=I-D_aW_0,\quad S_a=I-V^\top A_a^{-1}D_aU.
\]

Then \(\partial_ch_a=A_a^{-1}D_aU\), and

\[
K_a^{-1}=A_a^{-1}+A_a^{-1}D_aU S_a^{-1}V^\top A_a^{-1},\quad
\det K_a=\det A_a\det S_a . \tag{6}
\]

The adjoint uses the transpose of this same operator. These are established
identities. Gates, base solves and reduced matrices must be recomputed:
\(A_a^{-1}\) is not frozen at initialization. Also

\[
\|K_a^{-1}\|\le\|A_a^{-1}\|+
\|A_a^{-1}D_aU\|\|S_a^{-1}\|\|V^\top A_a^{-1}\|.
\]

Consequently singular values of \(S_a\) alone do not measure full response.
The determinant at zero frequency alone does not certify finite-loop
stability. A low-rank correction need not change only \(R\) eigenvalues.

Representation accuracy becomes more demanding near criticality. Already for
\(h=Wh+u\), \(W=1-\gamma,\widehat W=W+\epsilon\), \(0<\epsilon<\gamma\),
\[
\widehat h-h=\frac{u\epsilon}{\gamma(\gamma-\epsilon)}.
\]
The approximate system becomes singular at \(\epsilon=\gamma\). Thus no
gap-independent response claim follows from a small weight error.

## Scientific conjecture and strongest falsifier

The specific hypothesis is that endogenous paired credit/feature histories
retain the task-induced slow response at a substantially smaller evolving
state than dense training. A useful result must preserve own-state adjoints,
not just outputs. The strong mundane alternative is that ordinary online
truncated SVD of the same rank-one gradients does as well or better.

The decisive eventual comparison gives both low-rank methods the identical
Schur solver and evaluates dense-trajectory fidelity, response fidelity,
and complete runtime. If online SVD matches or beats the response/runtime
frontier, there is no evidence for a special paired-history mechanism.
Matched-rank Euclidean factors are a weaker supplementary control.

Even if history compression passes, end-to-end solver benefit is separate.
Anderson, Broyden/GMRES, and SHINE with refinement to identical tolerances must
be included before claiming speedup. Forming \(S\), solving its \(R\) base
right-hand sides, Gram/QR/SVD work, and any joint-clock directional solves
must all be timed. No such solver advantage is asserted by the pilot below.

## Authorized pilot contract

Supervisor authorization: at most 12 trained runs and 25 GPU-process minutes,
GPU 1. First resolve whether there is learned, compressible, nontrivial
response before implementing accelerated solvers. No other study inputs.

**Task:** nonlinear heterogeneous diffusion inference, with complete-field
targets. On a 16-by-16 Dirichlet grid, \(n=256,m=8\), generate a symmetric
nearest-neighbor conductivity matrix \(P_*\), normalize \(\|P_*\|_{\mathrm op}=1\),
and label fixed forcing fields by the unique solution
\[
y=\tanh(0.985P_*y+u).
\]
Use homogeneous \(P_0\) to initialize \(W_0=0.6P_0/\|P_0\|\). Train all \(n^2\)
entries for dense; apply (2) for memories. Input injection and identity output
are fixed. The teacher correction is a heterogeneous full-rank local operator,
not planted low rank. The model receives labels only.
Forcings mix smooth broad spatial fields and local bumps, with a frozen
amplitude 0.12. Use 8 training and 32 held-out fields, seeds 4101, 4102, 4103.
The setup is deliberately a low-data, complete-field inverse problem; it
does not establish applicability when \(mq\ge n\).

**Initial branch:** one seed, dense and \(q=4\), with Heun step 0.25 through
physical time 40 and checkpoints 0, 5, 10, 20, 40. Time 40 and the forcing
amplitude are frozen. If neither loss improvement nor response growth is
present, stop and report negative headroom. No tuning a new task after results.
If unstable numerically, one step-halved replay is permitted solely for
validity and counts as a trained run. This first branch is capped at eight
GPU-process minutes.

**Subsequent authorized branch:** only if dense reduces loss by 25% and has
at least one checkpoint with full inverse-response norm at least 1.5 times
its initial value, and \(q=4\) has at most 10% dense-prediction discrepancy
relative to target RMS. Then add \(q=2\), rank-32 online SVD, and repeat
dense/\(q=2\)/\(q=4\)/SVD for seeds 4102 and 4103, subject to the cumulative
12-run cap. A refinement replay uses a slot, so the latest complete seed is
omitted if necessary. No missing seed is treated as success.

**State:** dense moves 65,536 weights; \(q=4\) moves
\(2mnq+1=16,385\), or 25.002% including the scalar clock, with rank \(R=32<n\).
\(q=2\) moves 8,193. All arms retain the same fixed \(W_0\); dense and memory
need current equilibrium workspace. Memory evaluation may materialize dense
\(W\) and \(K\) temporarily for this pilot. Such workspace is reported, not
called a total-memory reduction or a speed gain. SVD rank 32 moves 16,384 factor
coordinates plus singular values/orthogonality convention.

**Numerical gates:** float64; equilibrium relative residual below \(10^{-9}\);
adjoint relative linear residual below \(10^{-9}\), measured against the true
current operator. Exact batched linear solves are acceptable in this small
pilot. Track solver failures and branch changes. Check directional gradients
on an independent small deterministic state before training. On one completed
seed, compare step 0.25 against 0.125 if discrepancy is near a decision
threshold; run count and time cap still apply.

**Measurements:** common-time train/test loss and prediction discrepancy;
own-state credit error relative to dense; relative weight increment error;
singular values/effective rank of each increment; gate variation;
\(\|K^{-1}\|_2\), \(\|A^{-1}\|_2\), and loss-directed inverse amplification;
Schur reconstruction residual at saved states; current versus initial
feature movement. Define effective rank as the least \(r\) retaining 99%
of squared singular values, and also report the full singular sequence.
Do not infer response capture from this rank statistic alone.

**Decision:** promising headroom requires dense loss improvement and response
growth above, \(q=4\) prediction discrepancy at most 10%, adjoint discrepancy
at most 20%, and genuine feature movement (RMS at least 0.02) on the completed
seed. Record the share of coordinates with \(1-D_{ii}>0.05\), rather than
claiming nonlinearity from use of tanh alone. Comparable or better SVD results
remove evidence for a special memory advantage. Lack of learned response or
compression is an informative early negative. Invalid numerical gates are
inconclusive. This pilot cannot establish the eventual solver-speed claim.

Hard stop: 12 trained runs, 25 GPU-process minutes, eight minutes for initial
branch, 8 GiB peak GPU memory, or 1 GiB saved data, whichever occurs first.
Generated outputs live only in the study's recurrence-prefixed generated
paths. No increased dataset, larger grid, alternate forcing, or new task.

## Claim ledger and recommendation

| Claim | Status |
|---|---|
| Exact paired equilibrium-gradient history and product defect | Derived on regular selected branches |
| Joint-clock finite-time \(q^{-2}\) tracking | Conditional internal proposition; fresh review pending |
| Exact reduced nonlinear equilibrium and adjoint | Classical mechanism; verified algebra, not novelty |
| Uniform response capture without a conditioning margin | False by scalar obstruction |
| Paired histories preferentially retain useful learned slow modes | Open; central pilot question |
| Same-tolerance full computation is faster | Open; requires later solver comparison |
| Practical advantage for large \(m\) or arbitrary recurrent sequences | Unsupported and outside this route |

Retain as a medium-risk secondary route. If its strongest low-rank control
matches it, preserve the exact extension but do not market generic Schur
machinery as a new mechanism. Do not build adaptive order before headroom:
increasing \(q\) cannot recover discarded history without retained higher
moments, replay, or a stated restart construction.
