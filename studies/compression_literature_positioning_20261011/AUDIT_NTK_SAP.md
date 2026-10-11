# Full-source audit: NTK-SAP

Wang–Li–Sun, *NTK-SAP: Improving neural network pruning by aligning training dynamics*, ICLR 2023, arXiv:2304.02840v1. Root read all 32 pages, including appendices A–O. Cache: reductions/ntk_sap.pdf and .txt. No code execution or reproduction.

## Actual result and assumptions

This is a theory-motivated empirical pruning method, not a theorem of nonlinear dense-path shadowing. It estimates the trace of the initialization NTK using Gaussian parameter perturbations, averages over reinitializations and random inputs, and iteratively removes connections with low saliency. It returns a mask. Sparse-network training follows afterward.

Its theoretical motivation uses the NTK scaling in which the infinite-width kernel is constant, not a general feature-learning scaling. Appendix B.2 then proposes a heuristic for finite networks: a trained parameter trajectory might explore parameter space sufficiently that averaging over random initializations proxies averaging kernels along training. No theorem establishes that replacement. The text explicitly says that alignment to the dense dynamics is only approximate in early training. Appendix G reports that later sparse-network spectra deviate from the dense spectrum.

Appendix O correctly identifies the leading small-noise term ε times the squared Jacobian Frobenius norm. It does not give a width-uniform Taylor remainder, finite-noise error bound, or an error bound after adaptive mask selection. Replacing real inputs by Gaussian noise is experimentally motivated, not certified for arbitrary input configurations.

## Why the proposed surrogate is not a trajectory certificate

Trace preservation does not imply spectral preservation or good conditioning: I₂ and diag(2−a,a), 0<a<1, have identical traces but arbitrarily different condition numbers. Even preserving every eigenvalue does not preserve predictions without preserving the corresponding directions relative to the labels. The kernels diag(1,2) and diag(2,1) have identical spectra; starting from zero with label vector (1,0), their gradient-flow predictions have first coordinates 1−exp(−t) and 1−exp(−2t), respectively.

These are counterexamples to an attempted *inference from the surrogate*, not counterexamples to a theorem the authors actually state. Appendix K itself acknowledges that equal traces can coexist with different spectra. The paper generally describes spectral preservation as potential or empirical, which is the correct claim level.

## Evidence and costs

Experiments span ResNets/VGG, CIFAR, Tiny-ImageNet and ImageNet, with several pruning baselines, useful ablations, and explicit setup-cost tables. Most smaller-dataset plots average three seeds. Sparsity is chosen empirically; no polylogarithmic-in-width retained-state law or same-seed prediction discrepancy is proved. The ImageNet comparisons retain substantial accuracy gaps relative to the dense model even when outperforming other pruning methods. Table 3 reports pruning costs around one or two training epochs for suitable settings; Tables 8–10 charge pruning plus training FLOPs. This is meaningful practical evidence, not evidence for complete-trajectory fidelity below dense-seed variability.

## Positioning

Include alongside NTT as initialization-based, dynamics-informed pruning. Its data/weight-agnostic mask construction is a real distinction and should be credited. Our manuscript's different contribution is a quantitative, coupled prediction guarantee for nonlinear feature-learning dynamics through convergence, with a proved retained-state scaling and a dense-discrepancy lower-bound benchmark. That distinction survives even if the NTK-SAP heuristic is practically excellent.
