# Shared evidence packet

This file inventories frozen evidence and points to exact locations. It intentionally
contains no novelty, significance, or breakthrough verdict.

## Candidate version zero

| Item | SHA-256 |
|---|---|
| `studies/response_memory_significance_20260926/FROZEN_MANUSCRIPT.tex` | `daa583a94be0c32103761d3391bde7292e5d2c5d3fe6b2ea5f1530a411a36f21` |
| `studies/response_memory_significance_20260926/FROZEN_MANUSCRIPT.pdf` | `f49ede7be2a271333c9ccf43e408b465b7081d3792ef966e0c6fb1e4509d935c` |

## Local theorem, implementation, and experiment evidence

All paths begin with
`data/generated/response_memory_significance_20260926/`.

| File | SHA-256 | Contents to inspect |
|---|---|---|
| `DEEP_ACTIVATION_ERROR_THEOREM.md` | `57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd` | Deep fixed-width statements and proofs for both clocks; activation scope; exact complexity accounting |
| `RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md` | `dda4d7b386b13129f30a64e6012b553b6ba783c41ed932874d98a93788ca7027` | Two-hidden-layer response-speed theorem with explicit constants, bootstrap, Gram continuation, and `P_0(T)` |
| `ORACLE_FINITE_HORIZON_BOUND.md` | `bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1` | Accumulator identity and finite-horizon feedback comparison |
| `CANONICAL_FLOW.md` | `4b86a47ba0a1d19315ee8ddc5e220f1f717ab2d551f807ce422246f2e1291830` | Network scaling and dense gradient-flow conventions |
| `compact_flow.py` | `f908c03cb63be0286d8505c2ce7959ea2377ccbcb8f740a10fac9dac8c49a67d` | Dense, ordinary-clock, weighted response-clock, dictionary, and low-rank implementations plus deterministic checks |
| `DEEP_CIRCLE_RESULTS.md` | `5ba8dd3668ce77ce3a99e4cef09ff77af21f5b1dc0836a816c121b4ffca853ec` | Three-hidden-layer circle protocol, metrics, feature movement, numerical checks, memory, and runtime |
| `MNIST100_RESULTS.md` | `31146d381a143ed01f8be0c2badabac1396cdf9f34a695ec842544fe9e215f49` | MNIST 3-vs-8 protocol, held-out predictions, numerical checks, memory, and runtime |
| `deep_circle_metrics.csv` | `c2fee597a50bcd4adf00789445f58420e111740f93daef904cc61659b56b7f78` | Machine-readable circle comparisons |
| `mnist100_metrics.csv` | `57524ada4165ee2383b6697323534fc6b3848646e1b03381e5c8544608247c6f` | Machine-readable MNIST comparisons |
| `response_clock_metrics.csv` | `9ed5d2138d40f26caf7018e8228a7d81eb126beb6a6110030f2562165524cd4a` | Ordinary and response-clock task/order results, Gram conditions, memory, and runtime |
| `BOOK_OBSERVABLE_CLOSURE.qmd` | `792aadb9fed6cf0e988ae5376c559bed14cbb0cdb2566fb29ad30c6d4d9fc6d2` | Established distinctions among scalar, field, and operator closure |
| `BOOK_TRAINABILITY.qmd` | `b2f57e5adf7e0314bc738d99b7f959caa0037287ce5844fbbab39de63914bcc1` | Established stability and compact-horizon comparison material |

### Existing shallow-circle and factor-control evidence added after Round 0

These files freeze already completed experiments; no new training was run for the
authoring loop.  All paths begin with
`data/generated/response_memory_significance_20260926/existing_experiments/`.

| File | SHA-256 | Contents to inspect |
|---|---|---|
| `MOMENT_RESULTS.md` | `4ae06686a5a244dd715aa1768ea5423f119d12e5a501c93f003432d213f7fe9b` | Two-hidden-layer circle results, protocols, state counts, refinement limits, and artifact inventory |
| `MOMENT_EXPERIMENT_PROTOCOL.md` | `696ba1d1322ddb5ced274e872efa0808c28f96e543354fa618e156391435f8a3` | Prospectively specified tasks, stopping rules, accuracy gates, and run budget |
| `MOMENT_INDEPENDENT_CHECK.md` | `960fc9cbb46dad08d0d7e0a17cf186565891d7064ccd6219efecf7c03257ab6f` | Independent algebra, endpoint, reference, grid, and refinement checks |
| `moment_metrics.json` | `f6df60f8c17d6acc6d68217845ca999e25258eb46b8ca9f753d7ae589fc9adfd` | Machine-readable shallow-circle results and numerical diagnostics |
| `moment_summary.md` | `721b43fe6a0366a0102a176e7d6d6fdea72dd759aa7bfad47d8f0dd40519f07f` | Generated analysis summary for the same campaign |
| `FACTOR_CONTROL_RESULTS.md` | `ee6020e9af196689750207deba415d01f91951be9e2ee9bbbb192661fc455057` | Rank-matched trained-factor comparison, all fitted/non-fit outcomes, resource and interpretation limits |
| `FACTOR_CONTROL_PROTOCOL.md` | `0d560b6788b45d2708656134a6c60f5c929df336fddcafe08bec1a97adb6f1f2` | Frozen factor baseline, ranks, seeds, stopping and refinement protocol |
| `FACTOR_CONTROL_CHECK.md` | `def168459b0bd84e381c5be7eae011a7f675b877cc4975b5dbcdfd106780f9dd` | Independent implementation and endpoint audit |
| `factor_metrics.json` | `2d11a1d0e80ba61a064c5db8381601de609472f7bf49b131684c07dc3f39b54c` | Complete machine-readable factor/moment comparisons |
| `factor_summary.md` | `7d82ef876a853a741217f19619c8086df1540bc66a3835b282519b08efc56bd1` | Generated analysis summary for the factor-control campaign |

## Primary literature PDFs

All paths begin with
`data/generated/response_memory_significance_20260926/literature/`.

| PDF | Primary source | Exact anchors |
|---|---|---|
| `nngp_1711.00165.pdf` | Lee et al., *Deep Neural Networks as Gaussian Processes*, arXiv:1711.00165 | Abstract; §§1.2, 2.3 |
| `ntk_1806.07572.pdf` | Jacot, Gabriel & Hongler, *Neural Tangent Kernel*, arXiv:1806.07572 | Theorems 1–2; §5 least-squares dynamics |
| `signal_propagation_1611.01232.pdf` | Schoenholz et al., *Deep Information Propagation*, arXiv:1611.01232 | Abstract; §§2–4; depth-scale experiments |
| `dynamical_isometry_1711.04735.pdf` | Pennington, Schoenholz & Ganguli, *Resurrecting the Sigmoid in Deep Learning through Dynamical Isometry*, arXiv:1711.04735 | Abstract; Eq. (2); §§2, 3 |
| `wide_linear_dynamics_1902.06720.pdf` | Lee et al., *Wide Neural Networks of Any Depth Evolve as Linear Models Under Gradient Descent*, arXiv:1902.06720 | Theorem 2.1, linearized-training bounds, and experiments |
| `tensor_programs_iv_2011.14522.pdf` | Yang & Hu, *Tensor Programs IV*, arXiv:2011.14522 | Dynamical Dichotomy, Theorems 3.6/3.8, Cor. 3.9, Definition 5.1, Theorems 5.6/7.4, §2 training-time discussion |
| `feature_learning_dmft_2205.09653.pdf` | Bordelon & Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks*, arXiv:2205.09653 | §§3–4; two-time kernels; §7 and Table 1 complexity |
| `finite_width_dmft_2304.03408.pdf` | Bordelon & Pehlevan, *Dynamics of Finite Width Kernel and Prediction Fluctuations in Mean Field Neural Networks*, arXiv:2304.03408 | Main fluctuation statements and finite-width scaling |
| `multilayer_mean_field_2001.11443.pdf` | Pham & Nguyen, *A Rigorous Framework for the Mean Field Limit of Multilayer Neural Networks*, arXiv:2001.11443 | MF ODEs §2.2; Theorems 7 and 15; neuronal embedding definitions |
| `neural_feature_flow_2007.01452.pdf` | Fang et al., *Modeling from Features*, arXiv:2007.01452 | Definition 1; Theorems 1–4; pair-function state in §3 |
| `sirignano_spiliopoulos_1805.01053.pdf` | Sirignano & Spiliopoulos, *Mean Field Analysis of Neural Networks: A Law of Large Numbers*, arXiv:1805.01053 | Main finite-horizon law-of-large-numbers theorems |
| `mei_montanari_nguyen_1804.06561.pdf` | Mei, Montanari & Nguyen, *A Mean Field View of the Landscape of Two-Layer Neural Networks*, arXiv:1804.06561 | Distributional dynamics and quantitative approximation theorems |
| `chizat_bach_1805.09545.pdf` | Chizat & Bach, *On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport*, arXiv:1805.09545 | Wasserstein gradient-flow setup and convergence statements |
| `neural_tangent_hierarchy_1909.08156.pdf` | Huang & Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, arXiv:1909.08156 | Assumptions 2.1–2.2; Eqs. (2.1), (2.2), (2.7), (2.11); Theorems 2.3 and 2.6 |
| `hippo_2008.07669.pdf` | Gu et al., *HiPPO: Recurrent Memory with Optimal Polynomial Projections*, arXiv:2008.07669 | Definition 1; Theorem 2; Propositions 3–6; Appendix D.3 Eq. (29) |
| `mori_zwanzig_chorin_2000.pdf` | Chorin, Hald & Kupferman, *Optimal Prediction and the Mori–Zwanzig Representation of Irreversible Processes*, PNAS 97 (2000) | Eqs. (2.7), (3.1); Markovian, memory, and noise decomposition |

## Directly checkable state and cost formulas

These formulas are listed as audit targets, not as conclusions about importance.

- Candidate dense internal moving state: `(H-1)n^2` scalars.
- Candidate ordinary-clock history state: `2(H-1)mnP` scalars, plus fixed outer
  state and fixed initialized internal matrices.
- Response-clock additions: one shared symmetric `P x P` Gram state and fixed
  matching-prefix data; its learned correction has the stated extra prefix rank.
- The history state alone is smaller than the dense internal state exactly when
  `2mP < n` (ignoring lower-order shared/prefix terms).
- A direct initialized-matrix action remains `O(n^2)` per vector. The low-rank
  learned action is `O(nmP)` per vector. A total direct closure action includes
  both terms.
- In NTH, the order-`r` kernel evaluated on `m` training samples carries up to
  `m^r` indexed values; the order-`P` hierarchy is therefore dominated by
  `O(m^P)` scalar sample tensors before symmetry reductions. The exact source
  notation uses `n` for sample count and `m` for width.
- Full DMFT Table 1 reports `O(P^2T^2)` kernel memory and `O(P^3T^3)` kernel time
  in that paper's notation.

## Coverage boundary

The packet is a fixed primary-source comparison set, not an exhaustive priority
search over all model reduction, state-space memory, reduced-order neural training,
or approximation theory. Any priority statement must state that limitation.
