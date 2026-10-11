# Chen–He–Su: Label-Aware Neural Tangent Kernel

## Sources and complete-reading boundary

Root read all 32 pages of [arXiv:2010.11775v2](https://arxiv.org/pdf/2010.11775v2), including references and Appendices A–D, on 2026-10-11. The [arXiv record](https://arxiv.org/abs/2010.11775) labels this 29 October 2020 revision the NeurIPS camera-ready version. The official [12-page paper](https://papers.nips.cc/paper_files/paper/2020/file/b6b90237b3ebd1e462a5d11dbc5c4dae-Paper.pdf) and [20-page supplement](https://papers.nips.cc/paper_files/paper/2020/file/b6b90237b3ebd1e462a5d11dbc5c4dae-Supplemental.pdf) were also obtained. Their text layer has defective mathematical-font extraction; the complete, legible camera-ready arXiv text is the proof-audit target. No assertion of byte-identical versions is made. Earlier v1 was downloaded and its complete textual diff against v2 inspected: changes are exposition/citations and line wrapping, with no substantive repair to the reviewed Appendix B formulas. Searches for the exact title plus correction/erratum did not locate a separate correction.

Generated files are in `data/generated/mfp_literature_positioning_20261011/root/`:

| File | SHA-256 |
|---|---|
| `lantk.pdf` (v2, 32 pages) | `18bea8db97fa1154a7f418d617bb566b57d62c9add7f7ba4952003c88ccccebc` |
| `lantk_v1.pdf` | `361f2520efc084613b22ff8f3e3215ad58231369de6bdc1235addda4e40754aa` |
| `lantk_published.pdf` | `20a45b1b962d1950ec478d1eee525bcda1016c626fdde44a098daa78d5b47dcd` |
| `lantk_supp.pdf` | `12304799fa8f8d6ea0e2ac79b253140cae9dce90dfc186ae1591abcd0242dd54` |

This is a direct competitor for symbolic higher-kernel calculations with labels, not a broad background citation. Its inherited NTH estimates were checked against the complete Huang–Yau source in this study; that dependency is not treated as automatically verified. No experiments or repository code from LANTK were executed.

## Actual problem and strongest overlap

The paper seeks a label-dependent kernel that better approximates trained neural-network behavior and improves kernel prediction. It gives two constructions: higher-order regression on pairs of examples (LANTK-HR), and a truncation motivated by the neural tangent hierarchy (LANTK-NTH). Both contain quadratic forms in the label vector. Labels are binary in the main setup, with a multiclass extension in the experiments. The regime is the NTK normalization, not MFP's showcased maximal-update normalization.

Appendix B.1, pp17–19, explicitly gives a **recursive symbolic program for every finite NTH order**. Starting from the gradient Gram K^(2), append a new gradient of f and differentiate every existing gradient factor in turn. In ordinary notation,

    K^(r+1)(x_1,...,x_(r+1))
      = <grad_theta K^(r)(x_1,...,x_r), grad_theta f(x_(r+1))>.

The tensor-index recipe implements the product rule exactly for smooth finite networks at arbitrary fixed depth; its correctness is an elementary induction. It does not rely on an infinite-width approximation. Appendix B.2, pp19–23, expands K^(2), K^(3) and K^(4) explicitly for a one-hidden-layer model f=a^T sigma(Wx)/sqrt(width). Appendix B.3, pp23–30, reduces selected initial expectations to low-dimensional Gaussian integrals. This is substantial overlap with the **idea** of symbolic derivative compilation followed by Gaussian calculation. MFP should not claim to introduce that idea or label-dependent quadratic kernel corrections.

The difference is the transformation's scope. This source's symbolic program generates one particular gradient-contraction hierarchy. The displayed Gaussian evaluation is specialized to a shallow model, selected orders, and ReLU, with qualifications below. It does not give a general source-response compiler for an arbitrary admitted smooth program with reused/transposed deep matrices, scalar feedback, represented updates and requested moving-flow jets. A fixed-label kernel approximation is also not the same observable as MFP's final hidden feature-kernel jet.

## What the theorem proves, and what it does not

Theorem 2.1, p5, bounds the difference between the actual time-dependent tangent kernel and a finite-time proxy obtained by retaining initial K^(2), K^(3), K^(4) and replacing the residual trajectory by fixed-kernel flow. Appendix A.4, pp15–16, expands that difference into four integrals. Cauchy–Schwarz and matrix operator bounds reduce them to Huang–Yau estimates for K^(3), K^(4), K^(5), and the prediction discrepancy. That reduction is a reasonable conditional argument; the inherited a priori estimates and probability mode remain a substantive dependency, with the proof qualifications recorded in this study's NTH review.

Assumption A, p15, requires bounded derivatives through order 2p+1 with p>=4; input norms bounded above and away from zero; and uniform lower singular values for distinct input subsets through that order. It does not cover arbitrary singular data geometry or ReLU. The parameter lambda in the displayed time interval refers to the inherited tangent-kernel gap, although this is not defined explicitly in the printed Assumption A. These are real restrictions, not automatic consequences of Gaussian initialization.

Equation (5), pp5–6, defines a deterministic label-aware kernel by replacing initial quantities with expectations and formally sending the proxy's time to infinity. This is **not** itself the object bounded by Theorem 2.1. Footnote 2 explicitly omits the additional concentration argument. Inversion and matrix exponentiation do not commute with expectation, and a finite width-dependent time bound does not by itself justify the t-to-infinity step. The text at the start of §3 loosely attributes a theorem guarantee to K^(NTH); a careful comparison should retain the narrower object actually treated in Theorem 2.1. This does not invalidate K^(NTH) as a proposed kernel construction.

Proposition A.2, p14, integrates the finite-time proxy explicitly under f_0=0 and invertibility of the initial kernel. Its final double-integral formula follows from integrating matrix exponentials in an eigenbasis. The §2.2 display for general h_0=f_0 should instead read h_t=y+exp(-tK_0/n)(f_0-y); its printed expression lacks decay on f_0. The f_0=0 specialization used in A.2 avoids that particular error. General iid Gaussian initialization does not have identically zero initial prediction in this normalization.

The Hoeffding decomposition, Lemma 2.2, concerns finite label randomness conditional on iid input samples. Conditional label independence gives the product-measure decomposition; it is a structural decomposition, not proof that either truncated construction approximates trained networks accurately. The authors expressly characterize the relation between HR and NTH as heuristic at the end of §2.3.

## Gaussian-expectation formulas: precise audit issues

The smooth symbolic hierarchy itself is sound. Its subsequent ReLU specialization changes derivative semantics: pp23–24 introduce sigma''=delta and sigma'''=delta' distributionally. At a finite network with continuous Gaussian initialization, preactivations are almost surely nonzero, and **classical** higher derivatives of ReLU at those values vanish. Distributional expectations can include boundary terms that are not expectations of those classical finite-network derivatives. They require a separate regularization/weak-derivative interpretation. MFP explicitly uses smooth activations and differentiates at finite width first; the two outputs cannot be identified without an argument.

A literal coefficient error occurs in B.3.2: term III is defined on p25 with a squared readout factor a^2, but its expectation on pp26–27 is assigned coefficient 3m. For independent standard Gaussian a, E[a^2]=1, so that coefficient must be m. The coefficient 3m is appropriate for the neighboring a^4 terms IV and V. For four orthonormal inputs, the remaining distributional integral is strictly positive (1/(8*pi)), making the discrepancy testable: m/(8*pi) versus 3m/(8*pi). This is a local repair, not a refutation of the general symbolic recurrence.

The rotation/inverse formulas on pp25–30 also presuppose independent directions and nonzero intermediate denominators. Repeated indices occur naturally in a full K^(4) array; the asserted invertibility of the four-direction matrix does not hold there. Gaussian orthant expectations themselves still exist with singular covariance, but delta products require further care. Consequently these formulas are not a singular-safe general calculus as written. The fresh [independent check](independent_proof_checks.md) confirms the derivative semantics and coefficient issue, and gives a stronger singular-boundary test: under Gaussian smoothing of ReLU, the expected full diagonal fourth kernel diverges as a negative constant divided by width times smoothing scale, whereas classical fixed-gate finite AD gives 4/width. Thus merely averaging or replacing an inverse with a pseudoinverse is not a general repair.

The independent check also identifies a local error in the p25 triangular rotation: the third coordinate of Qx_xi omits the product of the first coordinates of Qx_gamma and Qx_xi. Its explicit four-independent-input example fails to preserve their Gram matrix. Correcting that product repairs this algebraic error, separately from the intrinsic repeated-input distributional issue.

The broad introductory claim that every label-agnostic kernel must be arbitrarily bad under some relabeling is motivational, not a valid unrestricted theorem established by Appendix A.1. Its XOR drawing assumes feature support fills the relevant quadrants without other separating coordinates. On a finite input support with feature vectors equal to standard basis vectors, every binary labeling is linearly realizable. This observation does not deny finite-sample generalization difficulties or the possible benefit of a label-dependent kernel. The positioning does not rely on this collateral criticism.

## Experimental evidence and cost

All substantial classification experiments in §3 use **HR**, not the theoretically motivated NTH kernel, whose full fourth-order sample array costs at least sample_count^4. The NTH illustration uses just five planes and five ships. Thus reported HR gains are evidence for an engineered label-dependent predictor; they do not validate the omitted NTH concentration/long-time argument.

Tables 1–2 report improvements over CNTK, with the best among several variants highlighted. Appendix D.3 constructs pairwise training data of quadratic sample count, uses a sketch for scale, and introduces hand-engineered geometry features. The favorable result is not attributable uniquely to truncating the neural derivative hierarchy. D.4 chooses the neural-network checkpoint with best **test** performance; D.3 says the best lambda is chosen among four values without specifying an independent validation split. The results are exploratory comparisons, not clean estimates from an untouched test set. They still provide empirical evidence that the proposed HR construction can be useful.

The local-elasticity statistic is an intra-/inter-class ratio of normalized kernel similarities; it quantifies the stated notion, not a general proof that training trajectories or generalization laws match. The trained nets use Adam whereas the theorem concerns squared-loss gradient flow. No stronger equivalence follows from those plots.

## Positioning consequence

Credit the recursive symbolic NTH program and Gaussian initial-moment calculations directly. MFP's defensible advance is their generalization and integration into its precise smooth program language and width-limit compiler, with unrestricted finite named-matrix/transpose reuse within that language, explicit scalar feedback, singular formal-source bookkeeping, and moving-flow queries. Do not imply prior work lacked labels, symbolic kernel derivatives, or Gaussian moment formulas. Conversely, do not treat this shallow distributional calculation as already providing MFP's entire smooth deep-program theorem. Neither paper supplies a demonstrated efficient arbitrary-order solver.
