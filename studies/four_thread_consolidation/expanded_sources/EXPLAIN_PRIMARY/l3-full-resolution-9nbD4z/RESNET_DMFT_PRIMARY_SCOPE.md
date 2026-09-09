# ResNet/DMFT primary-source applicability check

Checked 2026-09-05. This is a bounded check of the specified source's model, main theorems, and the relevant stability argument; it is not a full paper audit or a new proof search.

**Conclusion:** The inspected Chaintron–Chizat–Maass results do **not** directly prove the all-fixed-training-horizon, continuous-time width limit for the specified three-hidden-layer nonresidual arctan MLP. Their proof does handle an analogous derivative-difference times backward-field term, but through a conditional-expectation/independence argument plus higher moments in a different model. It does not supply the missing estimate for the target's trained field `W3^T δ3` from its currently available RMS/L2 bound.

## Primary sources and version scope

- [Warwick programme](https://warwick.ac.uk/fac/sci/statistics/news/probai-scaling-laws-2026/programme/), June 23 research talk, slides link 21.
- [Louis-Pierre Chaintron, Warwick slides](https://warwick.ac.uk/fac/sci/statistics/news/probai-scaling-laws-2026/programme/lp_talk.pdf): slide 8 (PDF page 9), main limit theorem; slide 19 (PDF page 20), Mean ODE high-dimensional limit; slide 20, cavity argument; slide 21 identifies arXiv:2603.18168 and the Chizat companion paper.
- [Chaintron, Chizat, Maass, arXiv:2603.18168v1 PDF](https://arxiv.org/pdf/2603.18168v1), *ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit*. The downloaded PDF is 85 pages, with first-page date March 20, 2026 and arXiv v1 stamp March 18, 2026. All paper page/equation references below refer to this PDF. The web HTML rendering had different equation numbering and a different displayed date; it was not used for final equation/page references.

Local read-only copies: `resnet-paper.pdf`, `resnet-paper.txt`, `resnet-slides.pdf`, `resnet-slides.txt` in this note's directory. Selected statements/proofs read: paper §1.1–1.2, Theorems 2.4–2.5 and their assumptions, Lemmas 3.1–3.4/Remark 9, §5.1.1, Proposition 5.8, Lemma 5.10, proof of Lemma 5.15 and the moment estimates it invokes, Appendix B. No claim of verifying every proof is made.

## Exact theorem scope versus the target

The target is the supplied arctan model

`f = W4^T phi(W3 phi(W2 phi(z1))) / n`,

with the supplied feature-clock ODE, `z1(0)` iid `N(0,1)`, `W2(0),W3(0)` iid `N(0,1/n)`, and `W4(0)` iid `N(0,n^-2)`. These are treated as fixed requirements, including the extra `/n` in the readout.

1. **Architecture and scaling.** Paper equation (1), p.3, is

   `h^0 = Win x`,
   `h^ell = h^(ell-1) + (ML)^-1 V^ell rho(D^-1 (U^ell)^T h^(ell-1))`,
   `y = D^-1 Wout^T h^L`.

   Raw `U,V` entries have variance `D sigma_u^2,D sigma_v^2`; raw embedding/readout entries have dimension-independent variance parameters. The internal learning-rate multipliers are `LMD`, the embedding/readout multipliers `D`. Converting to unit-variance raw block weights gives a residual prefactor `sqrt(D)/(ML)` with the inner `1/sqrt(D)` multiplication. This exact parametrization, rather than a loosely described “residual scale” in a talk abstract, is the comparison object. An ordinary nonresidual three-layer composition is not this residual block recursion. Matching one effective matrix-entry variance does not identify the full network or its parameter ODE. In particular, setting `D=M=n` and holding a finite number of blocks leaves both `1/L` and `sqrt(D/(ML))=1/sqrt(L)` nonvanishing in the stated error estimate.

2. **Training algorithm and horizon.** Theorem 1.1, p.4, and slide 8 are for **ClippedGD at each fixed integer training step** `k`. Their hypotheses require bounded activation derivatives of orders 1–5, Lipschitz loss gradient, and `log L ∨ D <= C0 M`; the stated high-probability error is

   `c_k [1/L + sqrt(D/(ML)) + (1+log(1/delta))/sqrt(D)]`,

   subject to a small-error threshold. The clipping functions must be bounded with bounded derivatives through order 4 (p.4, footnote 2). This is not the target's unclipped continuous-time flow. The arctan regularity and squared-loss regularity do meet the corresponding smoothness requirements; those are not the obstruction.

3. **What “ODE” means here.** Theorem 2.4, p.16, constructs the limit system for a fixed finite number `K` of training steps; its continuous variable `s in [0,1]` is **network depth**. Theorem 2.5, p.17, gives high-probability RMS coupling convergence of the already depth-continuous Mean ODE as `D -> infinity`, uniformly over `s` and `k<K`. It does not start from a finite-depth MLP. Its assumptions (A.1)–(A.2), pp.16–17, include independent centered subgaussian raw block initialization and subgaussian iid embedding rows. The large-`D` theorem itself does not require clipping; clipping enters the finite-ResNet-to-Mean-ODE bridge. Thus “all of their DMFT arguments require clipping” would be inaccurate.

4. **Embedding training is not a decisive exclusion.** Although Theorem 1.1 is stated with frozen `Win,Wout` for simplicity, Appendix B, pp.78–79, describes the extension to trainable embeddings. This does not remove the architecture, scale, or training-time-limit mismatches. The target's width-dependent vanishing readout initialization would also need to be tracked in an exact model identification; no such identification is supplied by these results.

5. **No justified GD-to-GF interchange.** Lemma 3.4, pp.24–25, and Remark 9, p.25, explicitly produce constants growing by iterated exponentials in `k`, and their stated purpose is a fixed finite `K`. Some skeleton estimates separately track `k eta`, but the full a priori/convergence constants are not established uniformly under `K -> infinity, eta -> 0, K eta = T`. Consequently, a fixed-step theorem cannot simply be invoked for every fixed continuous training horizon. This is a missing bridge, not a claim that such an extension is impossible.

## The relevant product estimate: real mechanism, unverified transfer

The proof of Lemma 5.15, pp.65–66, explicitly encounters

`|rho'(P)-rho'(P_hat)| |Q| <= ||rho''||_infty |P-P_hat| |Q|`.

It treats a conditional expectation of this expression multiplied by the **iid initialization vector**. Lemma 5.10, pp.47–48, bounds such an expectation using the conditional L2 norm of the first factor and conditional L4 norm of the second, exploiting independent centered coordinates of the initialization vector (independent of the conditioning sigma-field, although the scalar factors may depend on that vector). Conditional subgaussian sums, Lemmas 5.1–5.3, pp.41–42, and skeleton bounds provide the required moments; see also equation (30), p.56, and its use on p.65. This avoids demanding independence of the two scalar factors themselves.

Proposition 5.8, pp.45–47, supplies stability of the corresponding **skeleton maps** with a factor `exp(C_k R)` when the finite noise path is bounded by `R` (the paper calls this cutoff `M`, which should not be confused with network hidden width). The expectation and moment arguments then integrate these factors. These maps encode finite histories of the Mean ODE's scalar inner-product interactions; they are not a uniform local-Lipschitz theorem for every deep-MLP state in an RMS ball.

The target's unresolved quantity is the RMS norm of

`(phi'(z2)-phi'(z2_hat)) ⊙ (W3^T δ3)`.

It is a coordinatewise product involving a **trained, correlated random matrix field**. A conditional-expectation estimate for the source model does not by itself bound this realized RMS product. Applying the source mechanism would require a valid cavity/skeleton representation for this exact architecture, the corresponding independence or decorrelation structure, adequate higher-moment/tail control for this field and its errors, and bounds uniform in the training discretization. None of those target-specific bridges is established by the inspected theorem or the cited proof passages. Simply taking `X=W3^T δ3` in Lemma 5.10 would not verify its independent-coordinate hypothesis.

**Research-state effect:** this primary source provides a concrete, relevant technique to investigate, but no upgrade of the target's continuous-time, all-fixed-horizon width-limit claim to “proved.” The currently identified global stability gap remains open under the stated target and available estimates.
