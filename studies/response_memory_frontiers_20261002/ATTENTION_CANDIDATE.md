# Frozen attention candidate: invariant-compatible paired response memory

Date: 2026-10-02. Status: **HOLD as a flagship direction.** Exact construction and a cheap algebra check are complete; utility, trained-trajectory mechanism, and distinctiveness from recent geometry methods are unproved. No training campaign was run. This is an independently developed scoped candidate, not established book material.

## Recommendation and scientific target

The defensible target is to reproduce **continued training of learned attention routing**, with the same standard softmax attention, initialization, loss, and gradient-flow metric as the dense reference. Compressing token caches or replacing softmax by a linear attention kernel would change the question.

The narrow new construction worth retaining is a paired response-memory closure with a small evolving head-space coordinate transformation. The transformation cancels the closure's explicit defect in a known query/key conservation law. It changes no instantaneous attention logits but can change subsequent learning. It keeps a compact evolving state when head dimension stays fixed as model width increases.

Neither attention balance invariants nor loss-preserving gauge projections are new. Recent primary work occupies both areas. The remaining research question is whether **paired temporal projection produces a practically important drift in invisible optimizer coordinates**, and whether transporting the response memories while restoring the original invariant level set improves trajectory fidelity beyond generic balancing or stronger low-rank solvers. There is no evidence for that empirical premise yet. The highest-value next step would be a small factorial continuation experiment, not transformer pretraining.

Two tempting routes were rejected. A worst-case square-root-head-width sensitivity bound does not establish that learned trajectories attain that sensitivity; changing the score scaling from inverse square root to inverse head dimension also changes the reference model. Ordinary Q/K/V moment compression alone is a valid architectural extension but is not enough scientific novelty for a flagship proposal.

## Actual inputs read

Repository scientific input was restricted to the user-authorized current paper and maintained notation/entry material. Read in full: `paper/main.tex`, including its inline fixed-width learning-speed and joint-clock proofs; all included text files `paper/results.tex`, `paper/proof_alltime.tex`, `paper/proof_tracking.tex`, `paper/proof_finite_time.tex`, `paper/comparison_appendix.tex`, and `paper/sphere_appendix.tex`; `docs/index.qmd` and `docs/notation.qmd`. No other study was read. Figures were read through their captions; their saved numerical arrays were not independently audited. The paper's linear-operator benchmark is stated with a proof outline in the supplied source, not a complete proof that this note independently reconstructs.

Process inputs: canonical-notation skill and its neural-response-memory reference; investigate-conjectures skill with research-contract, decisive-experiments, and adversarial-audit references; solve-math-rigorously skill. External primary sources actually inspected, with scope:

1. Bordelon, Chaudhry, Pehlevan, [Infinite Limits of Multi-head Transformer Dynamics](https://arxiv.org/html/2405.15712v2), introduction, parameterization, Results 1–3, and the identified backward-stability discussion. It already studies feature-learning transformer limits. Head dimension and number of heads yield different limits; therefore no new transformer-limit claim is made here.
2. Xu et al., [Stabilizing the Dynamic Low-Rank Training](https://arxiv.org/html/2609.32615v1), abstract, introduction, low-rank-flow setup and curvature-coupling/compensation mechanism. Its neglected-direction buffer is a materially stronger comparator than naive Euclidean factors.
3. Sun et al., [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/html/2407.04620v1), inner-loop definition and linear-attention equivalence theorem/proof. This candidate is a representation of a specified training flow; it does not claim novelty merely from an adaptive hidden state or test-time learning.
4. [GP-LoRA authors' repository](https://github.com/dhruvjatkar/GP-LoRA), README's gauge/imbalance construction. It already proposes loss-preserving imbalance projection for factored adaptation. Its objective is not the particular temporal closure below, but it defeats any broad claim that projecting invisible factor coordinates is new.
5. Wang and Wang, [Complete Characterization of Gauge Symmetries in Transformer Architectures](https://proceedings.mlr.press/v282/wang26a.html), primary abstract and linked RoPE commutant theorem/explanation. The proposed correction respects that reduction; no maximality result is needed or claimed here.
6. Nguyen and Montúfar, [On Parameter Symmetries and Conservation Laws in Gradient Flow](https://arxiv.org/html/2609.34549v1), introduction and framework, including attention applications and the distinction between symmetries and conservation laws. The elementary balance identity below is independently derived, not attributed as a new conservation theorem.
7. [Conservation Laws for Modern Neural Architectures](https://arxiv.org/html/2606.17816v1), attention/RoPE definitions and Theorem 4.4's conditions with its relevant derivation. Full query/key matrix balance must not be imposed on generic RoPE attention.
8. [Broken Symmetry in BF16 Attention](https://arxiv.org/html/2609.34272v1), gauge-projection mechanism and Appendix C exact identities. That work repairs score-gradient row-sum/translation symmetry, rather than the head-space balance below. Nonetheless it is close precedent for repairing a numerical attention approximation by an exact identity.

These are targeted novelty checks, not a comprehensive priority search. Only the indicated sections of external papers were read; none supplies an unproved hypothesis for our construction.

## Exact foothold in the current paper

For an internal linear block the paper integrates the canonical update into a forward/backward history pairing, projects both signals in the same growing polynomial space, then evaluates the next responses in the reconstructed network. Its key identity is the product defect, not low rank alone. Its all-time result is for a specific deep MLP, Gaussian initialization, zero readout, small fixed labels, and a preserved initial feature-Gram gap. None of that all-time theorem automatically transfers to attention, an arbitrary pretrained model, Adam, or noisy online adaptation.

Here is the direct attention translation. Let there be $m$ training sequences, $s$ tokens per sequence, hidden width $n$, and head dimension $d_h$. For one head, $W_Q,W_K,W_V\in\mathbb R^{d_h\times n}$ map the current token representation $h_{a,i}\in\mathbb R^n$ to query, key, and value vectors. This representation may be a layer-normalized residual stream; its exact definition is part of the chosen dense architecture. Suppress the layer/head index in the equations below. Standard scores and probabilities are

\[
 z_{a,ij}=\frac{(W_Qh_{a,i})^\top W_Kh_{a,j}}{\sqrt{d_h}},\qquad
 P_{a,ij}=\frac{e^{z_{a,ij}}}{\sum_{k\ \mathrm{allowed}}e^{z_{a,ik}}},
 \qquad o_{a,i}=\sum_{j\ \mathrm{allowed}}P_{a,ij}W_Vh_{a,j}.
\]

A fixed causal mask can restrict allowed entries. A scalar network output $f_a$, residual $r_a=f_a-y_a$, unhalved loss $\mathcal L=m^{-1}\sum_a r_a^2$, and RMS $\rho=\sqrt{\mathcal L}$ complete the forward/loss convention. All other layers remain part of the same reference network. Define the residual-free backward response at projection $X\in\{Q,K,V\}$ by $\delta^X_{a,i}=n\,\partial f_a/\partial(W_Xh_{a,i})$. This is the paper's scaled derivative convention even when its length is $d_h$. Equal Q/K block mobility $\eta>0$ gives

\[
 \dot W_X=-c\sum_{a,i}r_a\delta^X_{a,i}h_{a,i}^\top,
 \qquad c=\frac{2\eta}{mn}.
\]

Weight sharing only creates the token sum; it does not spoil the outer-product identity. Define the clock by $\dot\tau=\rho,\tau(0)=1$. For shifted Legendre polynomials $p_j$, normalized by $p_j(1)=1$ and $\int_0^1p_jp_k=\mathbf1_{j=k}/(2j+1)$, retain

\[
 \bar h_{a,i,j}=\int_0^\tau h_{a,i}(\xi)p_j(\xi/\tau)d\xi,\qquad
 \bar\delta^X_{a,i,j}=\int_0^\tau b^X_{a,i}(\xi)p_j(\xi/\tau)d\xi,
 \quad b^X_{a,i}=r_a\delta^X_{a,i}/\rho.
\]

The prefix has constant initial $h$ and zero $b^X$. Raw moment equations use sources $\rho h$ and $r\delta^X$, respectively, minus $\rho/\tau$ times $jM_j+\sum_{k<j}(2k+1)M_k$; thus the implemented ODE does not divide by zero residual. The reconstruction is

\[
 \widehat W_X=W_{X,0}-\frac c\tau
       \sum_{a,i,j<q}(2j+1)\bar\delta^X_{a,i,j}\bar h_{a,i,j}^\top.
\]

Every forward/backward response comes from this reconstructed network. Let $h^*,b^{X,*}$ denote endpoint evaluations of the corresponding history projections. Differentiation gives exactly

\[
 \dot{\widehat W}_X=F_X(\widehat\theta)+E_X,\qquad
 E_X=c\rho\sum_{a,i}(b^X_{a,i}-b^{X,*}_{a,i})
                         (h_{a,i}-h^*_{a,i})^\top. \tag{1}
\]

The derivation uses only the common temporal projection and the shared linear-block gradient, not a pointwise activation assumption. Both the softmax nonlinearity and its complete backward dependence remain inside the current responses. If $D_u=\|(I-\Pi_q)u\|_{L^2(0,\tau)}^2$, the paper's energy argument also gives

\[
 \int_0^T\|E_X\|_Fdt\le c\sum_{a,i}\sqrt{D_{b^X_{a,i}}(T)D_{h_{a,i}}(T)}. \tag{2}
\]

**Nondegeneracy warning, proved:** if the inputs $h_{a,i}$ to a compressed block stay constant during training, every $h-h^*$ is zero already at $q=1$, so that block's closure is exact. A fixed-embedding, single-attention-layer Q/K/V experiment can therefore return a misleadingly spectacular success. The decisive test must train upstream representations (or use at least a second contextual block), and must measure their motion.

## The invisible defect and a small correction

For ordinary attention without RoPE/QK normalization, the loss depends on this head's Q/K weights through $M=W_Q^\top W_K$. This remains true when upstream features and all other layers learn: a partial derivative with respect to Q/K holds the other parameters fixed. Write $G=\partial\mathcal L/\partial M$. Equal mobility gives

\[
 F_Q=-\eta W_KG^\top,\qquad F_K=-\eta W_QG.
\]

Consequently $B=W_QW_Q^\top-W_KW_K^\top$ has derivative zero: the four terms in $F_QW_Q^\top+W_QF_Q^\top-F_KW_K^\top-W_KF_K^\top$ cancel pairwise. This is a known factorization invariant. Its target is the actual initialized (B(0)), which need not be zero.

For the uncorrected closure (1), define its computable invariant defect and Gram sum by

\[
 D=E_QW_Q^\top+W_QE_Q^\top-E_KW_K^\top-W_KE_K^\top,
 \qquad S=W_QW_Q^\top+W_KW_K^\top.
\]

Thus $\dot B=D$. If $S\succ0$, the symmetric Sylvester equation

\[
 AS+SA=-D \tag{3}
\]

has a unique symmetric solution: in an orthonormal eigenbasis $S=U\operatorname{diag}(s_i)U^\top$, set $(U^\top AU)_{ij}=-(U^\top DU)_{ij}/(s_i+s_j)$. Modify the two velocities by

\[
 \dot W_Q=F_Q+E_Q+AW_Q,\qquad
 \dot W_K=F_K+E_K-AW_K. \tag{4}
\]

Their added contribution to $\dot B$ is (AS+SA), proving exact preservation of (B(0)). Their added contribution to $\dot M$ is $W_Q^\top A^\top W_K-W_Q^\top AW_K=0$. Therefore the correction does no instantaneous work on the loss and changes no current attention logit velocity at a fixed complete state. It removes one specific part of the truncation defect; it does not restore the entire dense vector field.

There is an explicit conditional size bound: if $S\succeq\sigma I$ and $\|W_Q\|_{op},\|W_K\|_{op}\le R_0$, then

\[
 \|A\|_F\le\frac{\|D\|_F}{2\sigma}
 \le\frac{R_0}{\sigma}(\|E_Q\|_F+\|E_K\|_F).
\]

Thus the added physical velocity has norm at most $2R_0^2/\sigma$ times the original summed defect. On a common compact tube with these bounds and a Lipschitz dense vector field, the ordinary finite-horizon perturbation estimate still propagates a small integrated defect. This is a conditional propagation statement, not a proof of small source errors, width uniformity, all-time fitting, or favorable constants.

The defect also supplies a limited reference-free diagnostic. For any dense reference on the original invariant level set, writing $C_X=\|\widehat W_X\|_{op}+\|W_{X,D}\|_{op}$,

\[
 \|\widehat B-B(0)\|_F
 \le C_Q\|\widehat W_Q-W_{Q,D}\|_F+C_K\|\widehat W_K-W_{K,D}\|_F. \tag{5}
\]

This follows by expanding each difference of quadratic products. A dense operator bound is obtainable conservatively from initial norms and gradient-flow energy: $\|W_{X,D}(t)\|_{op}\le\|W_{X,0}\|_{op}+\sqrt{\eta t\mathcal L(0)}$. Equation (5) certifies some physical parameter mismatch, not prediction error: the whole issue is that a gauge displacement can be invisible to current predictions.

Why future routing can notice such an invisible displacement is explicit. At a fixed ordinary-attention state,

\[
 \dot M=-\eta\{G W_K^\top W_K+W_Q^\top W_QG\}.
\]

For the loss-preserving change (W_Q\mapsto e^{\epsilon A}W_Q,
W_K\mapsto e^{-\epsilon A}W_K), with $A=A^\top$, $M$ and $G$ are unchanged but

\[
 \left.\frac d{d\epsilon}\dot M\right|_{\epsilon=0}
 =2\eta\{G W_K^\top A W_K-W_Q^\top A W_QG\}. \tag{6}
\]

This exact formula supplies a continuation observable more discriminating than current loss. It is not evidence that temporal truncation typically creates a large displacement of this kind.

## Keeping the correction inside a finite memory

Adding $AW_Q$ to a low-rank increment naively rotates the initialized matrix and may destroy the original rank claim. Do not hide that change. Introduce one invertible head-space matrix (R(t)), initially (I), with $\dot R=AR$, and write

\[
 W_Q=R X_Q,\qquad W_K=R^{-\top}X_K.
\]

Reconstruct $X_Q,X_K$ by the same paired moments, with fixed sources $W_{Q,0},W_{K,0}$, shared forward histories $h$, and backward signals now recorded as

\[
 \widetilde b^Q=R^{-1}b^Q,\qquad
 \widetilde b^K=R^\top b^K.
\]

Their raw sources are $R^{-1}r\delta^Q$ and $R^\top r\delta^K$; no residual quotient is used by the raw ODE. The stored backward moments retain the name $\bar\delta$, but explicitly refer to these transported signals. Differentiation of $RX_Q$ and $R^{-\top}X_K$ gives (4), with

\[
 E_Q=c\rho\sum R(\widetilde b^Q-\widetilde b^{Q,*})(h-h^*)^\top,
 \quad E_K=c\rho\sum R^{-\top}(\widetilde b^K-\widetilde b^{K,*})(h-h^*)^\top.
\]

At each state: reconstruct; perform the true forward/backward passes; evaluate the endpoint projection errors; form (D,S); solve (3); update $R$, the clock, and moments. No derivative-dependent implicit solve occurs. The initialization and moments determine future evolution without a stored target trajectory. Local well-posedness holds on the finite-dimensional open set $\tau>0, R\in GL(d_h), S\succ0$, assuming a smooth architecture and a locally Lipschitz loss gradient. Staying in this set uniformly in order/time is an open obligation.

For $H$ heads with $n=Hd_h$, gauge state costs $Hd_h^2=nd_h$, in addition to (O(msnq)) response moments per block. Initial dense weights are retained exactly and their forward/transpose actions are still paid for. An (O(n)) evolving-state claim therefore requires fixed $d_h,m,s,q$ as $H$ grows. If $H$ is fixed and $d_h\sim n$, gauge storage is $O(n^2)$ and defeats that claim. The physical learned increment no longer has the paper's rank-(msq) guarantee, because $RW_{Q,0}-W_{Q,0}$ need not be low rank. Moving-state compression, correction rank, total storage and runtime are distinct.

## RoPE version and exclusions

With position rotations $R_i^{pos}$, scores contain $W_Q^\top(R_i^{pos})^\top R_j^{pos}W_K$. A general head-space correction (3) then changes the logits and is invalid. For distinct two-dimensional RoPE planes, let $P_j$ be the orthogonal coordinate projector onto plane (j). The symmetric allowed generators are $A=\sum_j a_jP_j$, which commute with every position rotation. The conserved quantities relevant here are $\operatorname{tr}(P_jB)$, not the full matrix $B$. For the defect $D$ above, set

\[
 a_j=-\frac{\operatorname{tr}(P_jD)}{2\operatorname{tr}(P_jS)}. \tag{7}
\]

Whenever the denominator is positive, (7) cancels the plane's invariant derivative while preserving every RoPE logit. Its finite transport $R$ is block-scalar and costs only $d_h/2$ state coordinates per head. A zero denominator means both corresponding Q/K row blocks vanish; that plane needs a separately defined zero update or a local regularity analysis, not numerical division by zero. Frequency coincidences can enlarge the admissible correction space, but the plane-wise scheme remains valid.

The stated invariant assumes equal Q/K Euclidean gradient-flow mobilities, no Q/K weight decay, and no extra Q/K normalization. It is not an Adam conservation law. Adding arbitrary optimizer dynamics and then forcibly restoring (B(0)) would change the intended reference. A finite-step SGD comparison must separately bound or explicitly subtract its discretization drift. Biases can be included by augmenting the common input if the architecture admits the corresponding gauge action; they are omitted from the first test.

## Bounded algebra result

Preregistration: `ATTENTION_ALGEBRA_PREREG.md`. Implementation: `attention_algebra.py`. Raw result: `data/generated/response_memory_frontiers_20261002/attention_algebra/metrics.json`. Exact command was `/home/amir/miniconda3/bin/python studies/response_memory_frontiers_20261002/attention_algebra.py`. Python 3.10.14, NumPy 1.26.4, float64, seed 20261002; no GPU and no training.

The preregistered test passed. Dense ordinary-attention balance residual was $5.13\times10^{-16}$; the synthetic paired defect produced balance drift norm (0.597), and correction reduced the identity residual to $9.28\times10^{-16}$. RoPE plane correction residual was $3.79\times10^{-16}$; its logit-velocity contribution was $1.41\times10^{-17}$. An invalid full-matrix RoPE correction instead changed logit velocity by norm (0.294). The finite-difference check of (6) had relative discrepancy $2.01\times10^{-10}$ at step $10^{-5}$. Gram-sum condition number was 3.47. Code SHA256: `1ec4f87633eedf1dcf84e1ca684be93aeff8ff6278bd836a13a30d86c266ceaf`.

The endpoint residual arrays in this check were synthetic. This verifies signs, contractions and implementation of exact identities. It does not show the defects are reached in training or favor the corrected closure.

## Proposed decisive experiment, pending selection

**Central empirical conjecture.** On a small learned-representation attention task where the uncorrected paired closure has resolved routing mismatch, preserving the original invariant level set through transported moments reduces subsequent dense-reference routing/prediction discrepancy at the same total evolving-state budget. The benefit persists after matching scalar norm stabilization and a modern low-rank solver. This is a falsifiable witness claim, not a universal theorem.

Use a two-block causal transformer, width 128, four heads of dimension 32, smooth GELU and fixed layer-norm epsilon. Use standard inverse-square-root head scaling, fixed Gaussian initialization and a zero scalar readout. Train all upstream representations and Q/K/V/O maps by the same full-batch gradient flow on 32 fixed sequences of 16 tokens. An associative-retrieval task with repeated symbols and two-hop distractors is preferable to a manufactured score tie. Use 128 held-out sequences from a separately fixed generator. Freeze generator, initialization seeds 0–2, labels and time horizon before any comparison. The exact learning-rate/time calibration may use one dense numerical-validity pilot; it cannot select an unusually favorable seed. Use ordinary positional embeddings first; RoPE is a separately preregistered follow-up only if the mechanism survives.

Compare six arms from the same physical initialization: dense; paired memory; transported/invariant-corrected paired memory; paired memory with only trace balancing $A=aI$; a rank-adaptive DLRA/SDLRT-style solver with its neglected-direction buffer; and that same solver with original-level-set invariant repair. A naive LoRA arm is optional, not decisive. Count all factor, buffer, gauge and moment coordinates when matching memory. Fix orders $q=1,3,5$, but conduct the first mechanism comparison only at $q=3$; further orders are a predeclared branch if error exceeds numerical sensitivity.

Primary metric is the maximum over 40 shared physical times of held-out prediction RMS difference from a refined dense trajectory, normalized by dense output RMS plus a fixed $10^{-3}$ scale. Coprimary mechanism metric is attention-probability Frobenius RMS discrepancy over the same sequence/head/token list. Current training loss is insufficient. Record representation motion, Q/K invariant drift, the norm and integrated norm of $D$, minimum eigenvalue of $S$, transport condition number, and the scalar/full correction norm ratio.

At one predeclared midpoint, fork **evaluation-only dense continuations** from the uncorrected and corrected physical checkpoints for a short fixed horizon, discarding memory state in both. Also create a function-identical gauge-repaired copy of the uncorrected checkpoint and a trace-only copy. These are mechanistic probes, charged to the budget; no arm trains on the future dense reference. Agreement of initial logits with divergence of subsequent routing would directly test (6). The strongest mundane explanation is generic factor conditioning; the solver-by-repair factorial design and trace-only control address it.

Validity gates: the dense reference fits and attention probabilities change by RMS at least 0.05 from initialization; at least one learned block's input representations move by relative RMS 0.05; closure discrepancy is at least ten times coarse/fine solver sensitivity; corrected constraint residual is below $10^{-6}$ in normalized units; transport condition number below $10^4$; no balance assertion is imposed on an optimizer without that invariant. If these gates fail, report inconclusive and stop rather than redesigning after seeing the result.

Support threshold: corrected paired memory improves both primary prediction and routing errors by at least twofold in at least two of three seeds, does not worsen either metric by more than 20% on the third, and improves by at least 25% beyond trace-only repair at matched storage. A benefit common equally to DLRA plus repair supports generic structure preservation; it does **not** establish a special paired-memory advantage. A corrected-vs-uncorrected ratio above 0.8 on both metrics across all valid seeds rejects the practical premise at this scale. Intermediate outcomes remain inconclusive. No claim about generalization quality follows from fidelity to dense training.

Hard proposed budget: one GPU, at most 90 minutes and 8 GiB, three seeds, one scientific task configuration, the six arms at $q=3$, plus only the stated solver refinement/continuation probes. Stop at the budget whether or not fitting occurs. The $q=1,5$ or RoPE branch requires explicit subsequent selection; it is not authorized by this note. No such run has been launched.

## Claim ledger and remaining bottleneck

| Claim | Status | Evidence or unresolved obligation |
|---|---|---|
| Shared attention linear blocks admit exact paired defect (1) | Proved algebraically | Linear-block chain rule and the paper's common projection identity |
| Fixed block inputs give exact $q=1$ updates | Proved | Forward endpoint residual vanishes |
| Correction (3) preserves original ordinary-attention balance and instantaneous logits | Proved under $S\succ0$ | Sylvester identity; algebra check |
| RoPE correction (7) preserves the plane laws and logits | Proved with positive plane energy | Commutation and trace calculation; algebra check |
| Transported moments realize corrected autonomous dynamics with small moving state | Exact finite construction locally | Gauge matrix/inverse and moment representation; no global bounds |
| Current function equality can hide different future routing velocities | Proved | Equation (6), finite-difference check |
| This drift is a leading practical response-memory error in trained transformers | Open | No trained-trajectory evidence |
| Repair helps beyond scalar balancing and modern low-rank controls | Open | Factorial continuation experiment needed |
| Width-independent all-time transformer approximation | Open; not claimed | Source regularity, stability, fitting, heads and gauge conditioning all missing |
| Gauge repair alone is a new research contribution | Rejected as a novelty framing | Direct primary precedents above |

The main bottleneck is not more formal algebra. It is whether the invisible invariant defect is large and causally important on a genuinely learned attention trajectory. If the proposed controlled experiment does not show that, archive this as an exact structure-preserving option rather than a research flagship. Even a positive result needs comparison with occupied balancing methods before a priority or broad novelty claim.
