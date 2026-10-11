# Full-source checks: DEIM pruning and DMD acceleration

Root read, 2026-10-11. Both complete papers and all their appendices were read. No code execution or experimental reproduction. These were formerly abstract-screened leads; they are now closed at full-text level. They have no theorem claiming the contract of our manuscript.

## Freitag–Nicolaus–Redmann (2023): DEIM pruning

Version: the eight-page published open-access article, DOI 10.1002/pamm.202300078, retrieved from https://d-nb.info/1303073978/34. Cache: reductions/freitag_deim.pdf and .txt.

The preliminary POD/DEIM discussion is genuine model reduction. But the implemented neural-network method is **not** a closed DEIM approximation to the gradient-flow equations. Section 2 explicitly switches to pruning because a generic neural-network gradient is not componentwise separable and retaining the network architecture is desired. They collect gradient snapshots, compute a full left singular basis, and use DEIM to order parameter indices. That ordering is then used for repeated pruning and fine-tuning after convergence (Algorithms 1–3, pp.5–6).

The setup uses a 10,000-step full training trajectory plus optionally 10 or 100 additional trajectories of 10 steps each. Its sole neural-network example has 984 parameters, sigmoid activations, and 100 samples from a two-dimensional four-class toy problem; 128 repeats quantify variability. This is much narrower evidence than the abstract's mention of various state-of-the-art networks. The conclusion itself explicitly acknowledges the simple architecture and need for further experiments.

No theorem proves a gradient-trajectory approximation, rank decay as width grows, closed prediction dynamics, or a dense-seed comparison. The singular values of the observed snapshot matrix control approximation to those snapshots; they do not by themselves bound subsequent gradient-flow shadowing. The DEIM selection ordering may be reused across random starts in their experiment, but it was obtained from trained trajectories, not solely from an untrained dense realization.

Correct use in related work: evidence for data-driven gradient-coordinate selection and pruning informed by dynamics. Do not present it as a proved autonomous complete-trajectory compression, or as a failed attempt to prove one. The relevant omission is a different scientific contract, not a refuted central theorem.

## Tano–Portwood–Ragusa (2020): DMD-accelerated training

Version: arXiv:2006.14371v1, 13 pages including the pollutant-transport appendix, all read. Cache: reductions/tano_dmd.pdf and .txt.

The method alternates ordinary full-network updates with DMD extrapolations fitted to recent full weight snapshots. It does not discard the dense model after an initialization phase. For D full parameters, s recorded steps and r retained modes, the snapshot and mode storage is O(Ds+Dr), in addition to the dense weights and optimizer state. A small number of DMD coefficients is not the total retained model size. The source's local symbols differ: its n is a layer's parameter count, not our network width.

The empirical case is a three-hidden-layer soft-sign network with widths 40, 200 and 1000, about 2.9 million parameters, trained to predict a simulated pollutant field. The method tunes snapshot count and forecast length (selected 14 and 55) using finite-run losses. It reports roughly two orders of magnitude lower loss after the same count of ordinary epochs, but also **1.41 times the wall time** for that comparison (p.8). It therefore demonstrates a loss/compute tradeoff, not the claimed speedup at identical error by that single wall-time figure. The paper acknowledges overhead and possible overfitting/generalization limits.

There is no proved neural-training approximation theorem in the paper, despite the abstract's “theoretical justification” wording. The mathematical section derives standard DMD algebra and operation counts. In particular, it supplies no bound ensuring a finite linear operator shadows nonlinear training outside its fitted snapshot window.

Two local formula issues further limit a literal algorithmic reading. First, after comparing a DMD cost proportional to 3s²+r² with a backpropagation cost proportional to the number of training samples, p.4 prints the speedup inequality in the opposite direction; its surrounding explanation assumes the intended larger sample count. Second, the mode coefficient formula uses the transpose of the DMD mode matrix as its inverse. Generic DMD eigenmodes are not orthonormal, so a least-squares inverse is needed. For example, with square mode matrix [[1,1],[0,1]], applying transpose instead of inverse does not reconstruct the starting vector (0,1). This demonstrates the formula's general failure, not a reproduced failure of their code. The SVD and eigendecomposition displays contain additional transpose/order typographical issues; these are not needed for the novelty comparison.

Correct use in related work: trained-trajectory extrapolation can accelerate optimization empirically; it neither compresses total dense state to polylogarithmic size nor proves fidelity to the same dense trajectory. The distinction holds even if all of these algebraic typos are repaired.
