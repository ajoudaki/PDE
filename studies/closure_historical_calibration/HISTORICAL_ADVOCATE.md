# Historical advocate: Phase 1 case record

Status: final proposed freeze version; joint approval is recorded against an external hash manifest after the four-file audit. No target work has been read. Scope is the neutral Phase 1 assignment and public literature. This record uses the investigate-conjectures skill, evidence-ledger and adversarial-audit references. It is an assessment of contributions, not a full proof re-audit.

The critic and advocate jointly selected H01–H24, then added H25 to cover a concrete corrective extension. H08 and H15 are explicitly composite contemporary contributions; neither fuses the hypotheses of its component papers. The selection is purposive, not representative of all theory publications. It overrepresents wide-network theory because that is an assigned area, but includes approximation, optimization and a model-reduction comparison.

Each entry states a contribution, its predecessor-relative capability, the strongest objection and my response, publication-time significance, later evidence, and actual reading. Significance labels are judgments, not claims made by cited papers. S = significant, H = highly significant, B = breakthrough; ranges preserve uncertainty. Historical landmark status is a separate retrospective qualification. The amount of text devoted to limitations is not a score.

<a id="H01"></a>

## H01 — Cybenko (1989), universal approximation

**Result and advance.** Finite sums of a continuous sigmoidal activation composed with affine forms are dense in continuous functions on the cube. A functional-analytic discriminatory-function argument established that one hidden layer suffices. Predecessors included special constructions and two-hidden-layer results; contemporary Hornik, Funahashi and others prevent sole-origin attribution. [Primary paper](https://papers.baulab.info/papers/Cybenko-1989.pdf).

**Challenge and response.** The critic identified absent width, weight, approximation-rate and training guarantees. I accept all four. They block efficient-learning conclusions, not the solved representability question. A qualitative answer to an important previously unresolved possibility question can be a breakthrough. An arbitrary-accuracy theorem is neither an algorithm nor an explanation of depth efficiency.

**Assessment and influence.** B specialist and broad at publication, with attribution to the contemporary development. A later landmark qualification is supported by its foundational role in modern theory, including the independent survey's theorem and derivation, rather than a citation count. [Berner et al., §1.2.2](https://arxiv.org/pdf/2105.04026).

**Reading/uncertainty.** Primary introduction, discriminatory setup, Theorems 1–2 and discussion; survey theorem inspected. No proof re-audit. High confidence in the scoped result; historical priority within the contemporary wave is not adjudicated.

<a id="H02"></a>

## H02 — Hornik (1991), approximation capabilities

**Result and advance.** Bounded nonconstant activations support density in Lp for finite input measures; continuity gives uniform approximation on compact sets. Smoothness assumptions give approximation of derivatives, including weighted Sobolev settings. Earlier universal approximation and Hornik et al. (1990) derivative results already existed; the advance broadens admissible activations and measures. [Primary paper](https://web.njit.edu/~usman/courses/cs675_summer19/hornik-nn-1991.pdf).

**Challenge and response.** The critic correctly rejected both 'all activations' and first-derivative-approximation claims. Polynomial activations illustrate the boundary. I accept the lower novelty relative to H01 while crediting a reusable extension: assumptions were relaxed in ways relevant to several approximation norms. Lack of rates is a scope limit shared with the earlier density theorem, not the reason for the lower comparison.

**Assessment and influence.** H specialist, S–H broad at publication. Independent follow-on evidence is direct: Leshno et al. (1993), pp. 861–862, restate its two theorems and generalize the uniform result to a necessary-and-sufficient nonpolynomial criterion. [Follow-on paper](https://pinkus.net.technion.ac.il/files/2021/02/neural.pdf). This is a substantive extension, not a separate landmark claim.

**Reading/uncertainty.** Primary pp. 251–254, Theorems 1–4 and discussion, using the partner's primary-PDF extraction after browser failure. OCR ambiguities were interpreted against surrounding text. No proof re-audit.

<a id="H03"></a>

## H03 — Barron (1993), approximation rates

**Result and advance.** On an identified Fourier-moment class, shallow sigmoidal networks attain integrated squared approximation error of order 1/n, with explicit dependence on the function norm. This changes qualitative density into a useful dimension-independent exponent and compares adaptive ridge approximation with fixed linear approximation. [Primary paper](https://pages.cs.wisc.edu/~brecht/cs838docs/93.Barron.Universal.pdf).

**Challenge and response.** The critic emphasized that the Fourier norm can grow exponentially with dimension and efficient parameter search is not guaranteed. The paper itself makes these points. I agree: generic curse-of-dimensionality abolition is false. The surviving result is a major structural-class approximation theorem; it need not solve optimization to matter.

**Assessment and influence.** B specialist, H–B broad at publication. The subsequent Barron-space program supplies substantive influence evidence: the independent survey develops the theorem and records compositional/generalized extensions. [Berner et al., §4.2](https://arxiv.org/pdf/2105.04026). Landmark within neural approximation is defensible, not a claim that this paper solved deep learning.

**Reading/uncertainty.** Primary pp. 930–933 via scoped OCR, including Theorem 1 and the author's dimension/computation caveats; survey §4.2. Scanned mathematical notation limits exact constant verification.

<a id="H04"></a>

## H04 — Telgarsky (2016), benefits of depth

**Result and advance.** Repeated composition constructs small deep networks with oscillations that substantially shallower semi-algebraic networks require exponentially many units to approximate. This gives an explicit efficiency obstruction beyond universality and extends reasoning beyond a single activation. Circuit depth hierarchy and earlier neural separations are predecessors. [Primary paper](https://proceedings.mlr.press/v49/telgarsky16.pdf).

**Challenge and response.** The critic noted the selected oscillatory witness, the roughly k³-versus-k depth comparison, and absent learning algorithm. I accept these: it is not an adjacent-depth hierarchy or typical-data theorem. The lower bound remains a meaningful capability separation because it defeats a large comparator class. Requiring a trained benchmark would change the question being answered.

**Assessment and influence.** H–B specialist, H broad at publication. Independent Safran–Lee (2022), introduction and related work, develops optimization-based separation in response to the expressivity/learnability gap, including this construction. [Follow-on paper](https://proceedings.mlr.press/v178/safran22a/safran22a.pdf). Critical follow-on engagement supports influence without upgrading the original claim to learnability.

**Reading/uncertainty.** Introduction, Theorem 1.1 and companion-result limitations, setup of semi-algebraic gates and construction overview. No full lower-bound proof audit. Remaining disagreement concerns how much a worst-case separation changes broader theory, not its theorem statement.

<a id="H05"></a>

## H05 — Eldan–Shamir (2016), power of depth

**Result and advance.** A constructed target and input measure admit polynomial-size depth-three representation but require exponential width at depth two for constant L2 accuracy, under specified activation conditions. This establishes a separation at a fixed small depth; the shallow comparator is not saved by unrestricted weights. [Primary paper](https://proceedings.mlr.press/v49/eldan16.pdf).

**Challenge and response.** The critic stressed selected measure/target and no optimization guarantee. I agree; this is no claim about every task or arbitrary depth pairs. Unlike mere representation existence, the result identifies a quantitative obstruction. Those restrictions do not undo the solved fixed-depth question.

**Assessment and influence.** B specialist is defensible; H broad. Subsequent independent exposition reproduces the result and Fourier mechanism as a principal depth example, supporting lasting specialist influence. [Berner et al., §3.1](https://arxiv.org/pdf/2105.04026). That is stronger evidence than a bibliography entry, but does not by itself force a landmark label.

**Reading/uncertainty.** Primary assumptions and Theorem 1, introductory comparison and mechanism; survey theorem. Proof not re-audited. Rating uncertainty arises from breadth, not rigor concerns.

<a id="H06"></a>

## H06 — Rahimi–Recht (2007), random features

**Result and advance.** Random explicit features approximate shift-invariant kernels and permit linear learning computations in feature space; uniform kernel approximation and computational demonstrations accompany the construction. Bochner's theorem and kernel methods predate it. The advance is making kernel approximation an accessible scalable learning representation. [Primary paper](https://pages.cs.wisc.edu/~brecht/papers/07.rah.rec.nips.pdf).

**Challenge and response.** Fixed features do not learn representations; uniform kernel error alone is not a complete prediction/generalization guarantee. I accept the critic's objection to attributing all later statistical guarantees to the original paper. Existing Fourier mathematics does not erase the new computational capability. Later error-analysis corrections concern precise guarantees, not the viability of random-feature computation.

**Assessment and influence.** B computational-learning specialist, H–B broad. H25 independently analyzes competing feature maps and downstream kernel-ridge error, demonstrating a substantive follow-on program. [Sutherland–Schneider](https://www.cs.cmu.edu/~dsutherl/papers/rff_uai15.pdf). Landmark within scalable kernel methods is plausible; the calibration does not equate that with deep-feature-learning theory.

**Reading/uncertainty.** Primary feature construction, §3 Claim 1, §4 and experimental discussion; H25 relevant propositions. Original bound constants were not re-proved.

<a id="H07"></a>

## H07 — Williams (1997), computing with infinite networks

**Result and advance.** Neal's GP limit is explicitly a predecessor. Williams derives analytic erf and Gaussian-unit covariance functions, enabling Gaussian-noise Bayesian prediction by kernel matrix computation, of cubic cost in sample count. [Primary paper](https://proceedings.neurips.cc/paper_files/paper/1996/file/ae5e3ce40e0404a45ecacaaf05e5f735-Paper.pdf).

**Challenge and response.** The critic identifies fixed hyperparameters, selected activations and no general hyperprior integration or feature learning. I accept these and reject credit for inventing the GP limit. The residual contribution is a concrete conversion from existence to computation. Missing finite-width rates do not compromise exact inference in the limiting model.

**Assessment and influence.** H specialist, S–H broad at publication. H08's independent papers explicitly build from this shallow GP correspondence to deep models, establishing a clear lineage. No separate claim that Williams alone originated the historical program.

**Reading/uncertainty.** All main sections of the seven-page primary paper, including covariance formulas and hyperprior discussion; H08 primary predecessor discussion. Confidence high for the narrow computational contribution.

<a id="H08"></a>

## H08 — Deep GP correspondence (Lee et al.; Matthews et al., 2018)

**Result and advance.** Lee et al. supply deep covariance recursion and practical Bayesian computation; Matthews et al. prove weak convergence on countable input sets for simultaneous increasing widths with continuous linear-envelope nonlinearities. Their hypotheses and results remain distinct. Shallow GP theory and compositional kernels are predecessors. [Lee](https://arxiv.org/pdf/1711.00165), [Matthews](https://arxiv.org/pdf/1804.11271).

**Challenge and response.** The critic rejects treating prior convergence as a feature-training or uniform finite-width prediction theorem. Agreed. The remaining capability—well-defined deep random priors and computable limiting inference—is substantial. Lee's sequential argument must not be substituted for Matthews's simultaneous theorem; recurrence formulas were not entirely unprecedented.

**Assessment and influence.** H specialist and broad; B boundary for a reader emphasizing the new deep-inference capability. H19 independently extends architecture coverage, while H09/H10 distinguish training kernels from prior kernels. These are demonstrated conceptual uses, not mere citations.

**Reading/uncertainty.** Lee §2 and inference discussion; Matthews setup and Theorem 4. No entire appendix audit. Related versions count once here. Precise finite-width convergence rates are not attributed to Matthews's qualitative theorem.

<a id="H09"></a>

## H09 — Jacot–Gabriel–Hongler (2018), NTK

**Result and advance.** The parameter-gradient kernel governs function evolution; with sequential infinite widths it approaches a deterministic kernel and stays fixed over eligible finite training horizons. This converts a nonlinear parameter optimization problem into a function-space kernel evolution in a defined regime. GP priors and kernel descent predate it. [Primary paper](https://papers.nips.cc/paper/8076-neural-tangent-kernel-convergence-and-generalization-in-neural-networks.pdf).

**Challenge and response.** The critic correctly reconstructs fixed depth, scaling, smoothness for the training theorem, and bounded integrated training direction. ReLU is not directly covered by that smooth theorem. Kernel freezing excludes rich feature learning; it does not invalidate identification of the kernel regime. I therefore retain B rather than demand an all-regime theory.

**Assessment and influence.** B specialist and broad at publication. H10, H11, H20–H23 and independent work on limits of NTK demonstrate that the result changed both tools and questions. An independent statistical survey develops the regime as an organizing framework. [Bartlett et al., §5](https://arxiv.org/pdf/2103.09177). Landmark retrospectively is supported.

**Reading/uncertainty.** Theorems 1–2, parameterization, training hypotheses, least-squares discussion and survey passage. No proof re-audit; attribution excludes every later extension.

<a id="H10"></a>

## H10 — Lee et al. (2019), wide networks evolve linearly

**Result and advance.** Wide equal-width networks follow their first-order parameter linearization; positive-definite limiting NTK, suitable smoothness, squared loss and small steps give global-in-time control, with output/NTK discrepancies of order n^(-1/2). Prediction distributions are characterized. H09 is the decisive predecessor. [Primary paper](https://arxiv.org/pdf/1902.06720).

**Challenge and response.** The critic objects to treating a sharpened NTK consequence as a second original discovery and to extending MSE guarantees to every empirical experiment. Agreed. Simultaneous width and uniform-time quantitative control are useful added capabilities. They justify H even though the conceptual regime already existed.

**Assessment and influence.** H specialist and broad. H21 explicitly addresses the observed finer kernel-change scale, showing substantive follow-on use. That influence does not retroactively grant priority over H09.

**Reading/uncertainty.** Main setup, Theorems 2.1–2.2, empirical comparison and discussion. Formal smoothness/conditioning details checked at theorem-summary level; full appendix not audited. Scope of the experiments is broader than the theorem.

<a id="H11"></a>

## H11 — Chizat–Oyallon–Bach (2019), lazy training

**Result and advance.** A general smooth-model scaling parameter yields finite-horizon proximity to linearization; stronger convexity and derivative-rank hypotheses give uniform-time results. This explains laziness as a scaling phenomenon extending beyond very wide neural networks. [Primary paper](https://papers.neurips.cc/paper/8559-on-lazy-training-in-differentiable-programming.pdf).

**Challenge and response.** The critic emphasizes zero-output initialization in the simple comparison, strong convexity/surjectivity for global control, and selected empirical evidence of performance loss. I accept these. The paper does not prove lazy methods are universally inferior. Its central contribution is the causal diagnosis of a regime, which survives those restrictions.

**Assessment and influence.** H specialist and broad, with B specialist a reasonable upper boundary. H20's explicit parameterization classification and H23's rich/lazy interpolation use the distinction; these independent constructions establish influence beyond terminology.

**Reading/uncertainty.** Scaling setup, Theorems 2.2 and 2.4, finite-versus-uniform-time discussion and experimental interpretation. No proof re-audit. No rating change solely from the number of assumptions.

<a id="H12"></a>

## H12 — Mei–Montanari–Nguyen (2018), mean-field learning

**Result and advance.** Two-layer small-step SGD admits a nonlinear probability-distribution PDE with quantitative finite-time approximation under boundedness/regularity assumptions. Examples and noisy-SGD results analyze optimization beyond frozen features. Particle limits and convex measure formulations predate this adaptation; contemporaneous neural mean-field papers share credit. [Primary paper](https://web.stanford.edu/~montanar/RESEARCH/FILEPAP/mean_field.pdf).

**Challenge and response.** The critic identifies the exponential-in-horizon error, shallow model and absence of unconditional global convergence. Agreed. The PDE state truly permits feature motion; finite-horizon convergence is sufficient to establish that new description, though insufficient for arbitrary long training. Efficient numerical PDE solution in large parameter dimension is not automatic.

**Assessment and influence.** B specialist, H–B broad at publication. H22 uses a dimension-reduced mean-field approach to prove structured learnability, a concrete descendant. This is not exclusive priority or a claim to have solved deep learning.

**Reading/uncertainty.** General setup, examples and failure discussion, A1–A3, Theorem 3 and its explicit horizon caveat. The 103-page supplement was not fully read or re-audited.

<a id="H13"></a>

## H13 — Rotskoff–Vanden-Eijnden (2018), interacting-particle training

**Result and advance.** The contribution studies mean-field training together with fluctuations and a proposed long-time suppression of initial sampling error. Relative to a law-of-large-numbers description alone, the positive case is a particle/fluctuation account of approximation after training. [Conference paper](https://papers.neurips.cc/paper_files/paper/2018/file/196f5641aa9dc87067da4ff90fd81e7b-Paper.pdf).

**Challenge and response.** The critic reconstructed discriminatory-kernel, smooth full-support initialization and long-time stability requirements, and verified inconsistent normalization signs in the printed propositions. The setup uses population/large-data loss and online resampling, so generic finite-dataset generalization is not established. I accept a source-verification uncertainty for precise rates. A likely typographical inconsistency is not a proved failure of the contribution. We do not present clean universal finite-n O(1/n) training accuracy as verified.

**Assessment and influence.** H specialist, S–H broad at publication, judged for the particle/fluctuation contribution. Evidence confidence on the exact long-time rate is lower than on the representation. Independent historical influence of the specific rate is not established by this reading; the broader contemporary mean-field lineage is shared.

**Reading/uncertainty.** Conference p2 Key assumptions, §§2–3, Propositions 3.1–3.3 and nearby discussion; critic checked page image. Supplementary arguments and later full-paper reconciliation were not audited. This uncertainty is not silently converted into a lower scientific-significance score.

<a id="H14"></a>

## H14 — Chizat–Bach (2018), optimal-transport global optimality

**Result and advance.** Under homogeneity, regularity and topological support separation, a Wasserstein gradient-flow limit, **if it converges in W2**, is globally optimal; the paper also connects many-particle approximations. Convex optimization over measures alone did not imply that particle transport avoids nonglobal stationary states. [Primary paper](https://proceedings.neurips.cc/paper/2018/file/a1afc58c6ca9540d057299ec3016d726-Paper.pdf).

**Challenge and response.** The critic correctly emphasizes assumed convergence and continuum initialization. These materially narrow the advertised optimization conclusion: this is no unconditional finite-network solver theorem. The surviving homogeneity/topology mechanism is nonetheless a significant new bridge. I retain H broad and H–B specialist rather than treating conditionality as automatic insignificance.

**Assessment and influence.** Publication-time scope above. Separate independent subsequent influence of this exact theorem was not fully traced here; it is not assigned landmark status on reputation.

**Reading/uncertainty.** Assumptions 3.2/3.4 and Theorems 3.3/3.5, stationarity-versus-optimality and limit discussion. Full proofs not re-audited. Convergence condition is a central qualification, not a footnote.

<a id="H15"></a>

## H15 — Du et al.; Allen-Zhu–Li–Song (2019), overparameterized optimization

**Result and advance.** This grouped wave proves successful gradient training of sufficiently overparameterized deep models near random initialization. Du's smooth-activation Gram-based results and Allen-Zhu et al.'s ReLU GD/SGD results have different architecture, width and data conditions. Prior shallow results and kernel mechanisms are predecessors. [Du](https://proceedings.mlr.press/v97/du19c/du19c.pdf), [Allen-Zhu et al.](https://proceedings.mlr.press/v97/allen-zhu19a/allen-zhu19a.pdf).

**Challenge and response.** Very large width bounds, data/Gram nondegeneracy and small learning rates limit practical coverage. Near-initialization interpolation is not generic generalization or representation learning. The positive case is an algorithmic convergence guarantee through nonlinear deep parameters, not just existence of fitting weights. Removing those overclaims leaves a major advance; pooling assumptions would fabricate a stronger theorem.

**Assessment and influence.** B specialist, H–B broad for the grouped contribution. H10/H21 develop the quantitative kernel-controlled optimization program. This shows follow-on development without assigning every improvement to the first wave.

**Reading/uncertainty.** Du setup, Theorem 5.1 and comparison of depth/width dependencies; Allen-Zhu Theorems 1–2 and near-initialization discussion. Full proofs not re-audited. Composite case counts once.

<a id="H16"></a>

## H16 — Soudry et al. (2018), implicit max-margin bias

**Result and advance.** For separable homogeneous linear prediction with exponential-tail losses and suitable GD steps, iterates diverge in norm while their direction approaches the L2 maximum-margin separator. The journal treatment includes degenerate data omitted from the earlier version. Boosting margin results and explicit regularization paths are predecessors. [Primary paper](https://jmlr.org/papers/volume19/18-188/18-188.pdf).

**Challenge and response.** The critic emphasizes linearity, separability, loss tail and slow logarithmic directional convergence. I accept these. The algorithm itself selecting a specific interpolating direction remains the core mechanism; a nonlinear-network theorem or fast asymptotic rate is not required to make that discovery substantial.

**Assessment and influence.** B specialist, H–B broad at publication. Independent survey treatment states the theorem and discusses subsequent optimization-geometry and multilayer extensions. [Bartlett et al., §3](https://arxiv.org/pdf/2103.09177). This supports durable influence; broader landmark status remains a retrospective judgment with a range.

**Reading/uncertainty.** Assumptions, Theorems 3/5, earlier-version correction and boosting comparison. No appendix re-audit. Versions are one contribution, not independent calibration votes.

<a id="H17"></a>

## H17 — Gunasekar et al. (2017), matrix-factorization implicit bias

**Result and advance.** The paper proposes initialization-dependent implicit regularization in factorized matrix optimization, with experiments and a nuclear-norm result for commuting observation matrices, conditional on existence and interpolation in a small-initialization limit. The wider nuclear-norm statement is a conjecture. [Primary paper](https://papers.nips.cc/paper_files/paper/2017/file/58191d2a914c6dae66371c9dcdc91b41-Paper.pdf).

**Challenge and response.** The critic distinguishes the conditional theorem from the general conjecture. I agree: the latter is refuted by later work and must not be promoted to a theorem. The useful capability that survives is a demonstrated mechanism by which parameterization and initialization affect solution selection, plus a fertile question. [Li et al., introduction and Example 5.9](https://arxiv.org/pdf/2012.09839).

**Assessment and influence.** H specialist, S–H broad at publication for the supported contribution. The independent greedy-low-rank follow-on both revises the explanation and demonstrates influence. A false broad conjecture can motivate valuable work without becoming a true result retrospectively.

**Reading/uncertainty.** Primary §§3–4, Conjecture versus Theorem 1; later primary introduction/counterexample identification. Counterexample proof not re-audited. Central claim levels kept separate.

<a id="H18"></a>

## H18 — Saxe–McClelland–Ganguli (2014), deep linear dynamics

**Result and advance.** Singular-mode reductions yield exact nonlinear weight-training trajectories for structured deep linear networks and illuminate staged learning and initialization. Earlier linear-network landscape/SVD analyses did not provide the same time-resolved mechanism. [Primary paper](https://www.saxelab.org/assets/papers/Saxe2014.pdf).

**Challenge and response.** Linear input-output maps, whitened or suitably structured covariances, aligned invariant trajectories and continuous-time/small-step dynamics constrain the exact solution. Arbitrary initial-condition coupled dynamics remain difficult. They prevent a generic nonlinear-network solution. The positive case is that nonlinear optimization dynamics can be solved and understood in a controlled model; a tractable special family may expose a mechanism without establishing universality.

**Assessment and influence.** H–B specialist, H broad at publication. H23 revisits exact deep-linear kernel dynamics as a tractable comparison, but detailed independent influence tracing for Saxe's specific formulas remains incomplete here. No automatic historical-landmark label.

**Reading/uncertainty.** Primary introduction, §§2–3 modal/whitening setup, initialization discussion, selected non-whitened extension. Exact solutions were not independently rederived. Breadth uncertainty dominates the assessment.

<a id="H19"></a>

## H19 — Yang (2019), Tensor Programs I

**Result and advance.** A computation language and master theorem deliver wide random-network Gaussian behavior and empirical-average limits across expressive architecture classes, including repeated weights. This unifies previously architecture-specific GP analyses. [Primary paper](https://papers.neurips.cc/paper/2019/file/5e69fda38cda2060819766569fd93aa5-Paper.pdf).

**Challenge and response.** The core is initialization with controlled nonlinearities and finite admissible programs; the title does not cover every architecture, attention scaling, transpose operation or growing horizon. Accepting these restrictions leaves a reusable method with real cross-architecture reach. Lack of a finite-width rate is not fatal to a limit-calculus contribution.

**Assessment and influence.** H–B specialist, H broad. H20 is a same-author continuation, not independent reception. H23 independently recovers the tensor-program feature process, demonstrating external uptake of the framework; it does not validate every architectural slogan.

**Reading/uncertainty.** NETSOR/NETSOR+ setup, Assumption 5.1, Theorem 5.4, Corollary 5.5, future-transpose caveat. Appendices not fully read. Scope of later tensor-program installments is not backdated to this one.

<a id="H20"></a>

## H20 — Yang–Hu (2021), infinite-width feature learning

**Result and advance.** Stable nontrivial abc parameterizations are classified into feature-learning versus kernel regimes; maximal-update scaling supplies explicit feature-learning limits. Earlier shallow mean-field limits already learned features. The advance is a systematic deep parameterization classification and computable limit construction. [Primary paper](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf).

**Challenge and response.** It is not a classification of every conceivable parameterization or optimizer, nor uniform convergence for unbounded training duration. The activation hypotheses matter: the paper explicitly excludes linear activation from its dichotomy. Feature learning in a limit is not proof of superior performance on every task. These restrictions preserve the central conceptual alternative to treating all infinite-width networks as kernel machines.

**Assessment and influence.** B specialist, H–B broad. H23 explicitly recovers its recursive process and builds another computational formulation, an independent substantive use. Later practical hyperparameter-transfer claims require their own sources and are not backdated here.

**Reading/uncertainty.** abc setup, Theorems 3.2/3.3/3.5/3.7, Corollary 3.8 and its activation caveat, function-space and transfer-learning remarks, experiment summary. Full technical appendix not audited. Classification scope is explicit.

<a id="H21"></a>

## H21 — Huang–Yau (2020), neural tangent hierarchy

**Result and advance.** An exact hierarchy for training kernels is paired with quantitative truncation estimates and improved control of NTK variation in a wide regime. Unlike writing an infinite hierarchy alone, the error bounds provide an approximation capability beyond static NTK. [Primary paper](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf).

**Challenge and response.** Smoothness and input nondegeneracy requirements grow with order; constants are not tracked uniformly in order, and time/width conditions matter. Thus fixed-width convergence as truncation order goes to infinity, efficient computation, or arbitrary rich-feature-learning closure do not follow. I accept these boundaries while retaining the value of the finite-order quantitative theorem.

**Assessment and influence.** H specialist, S–H broad. Independent survey discussion develops its higher-order kernel hierarchy as a distinct beyond-linear approximation with increasing accuracy and cost, demonstrating scoped intellectual uptake. [Bartlett et al., §5.3](https://arxiv.org/pdf/2103.09177). This does not establish landmark status. The gap below H09 reflects predecessor-relative capability, not an arbitrary demand for all-time validity.

**Reading/uncertainty.** Assumptions 2.1–2.2, Theorem 2.3, Corollaries 2.4–2.5, truncation definition and Theorem 2.6 with discussion of constants/horizon; the independent survey's §5.3 hierarchy discussion. Full proof not audited.

<a id="H22"></a>

## H22 — Abbe–Boix-Adserà–Misiakiewicz (2022), merged staircase

**Result and advance.** For sparse functions on binary inputs in a two-layer mean-field SGD regime, a structural property is necessary and nearly sufficient for learning with sample dependence linear in ambient dimension; fixed-feature methods face separations. Sufficiency includes generic coefficients and specified activations. [Primary paper](https://proceedings.mlr.press/v178/abbe22a/abbe22a.pdf).

**Challenge and response.** Fixed latent sparsity is crucial: dependence on that sparsity can be extremely large. Boolean inputs, optimization scaling, genericity and activation qualifications block a generic efficient-feature-learning theorem. Still, proving actual algorithmic adaptation and a structural learnability boundary is more than expressivity or an informal rich-limit description.

**Assessment and influence.** H–B specialist, H broad. Subsequent independent influence has not been sufficiently traced in this assessment; no historical upper-tier claim follows from recency or enthusiasm.

**Reading/uncertainty.** Setup, Theorems 7/9, separation section, complexity discussion and selected activation/genericity appendix statements. The 106-page paper was not fully audited. Nearly sufficient is not sufficient for every coefficient choice.

<a id="H23"></a>

## H23 — Bordelon–Pehlevan (2022), dynamical field theory

**Result and advance.** Deterministic two-time kernels and response quantities define a self-consistent stochastic-process description of wide feature-learning dynamics. The paper gives an alternating sampling computation and linear-network simplifications, recovering Yang–Hu's earlier process. [Primary paper](https://arxiv.org/pdf/2205.09653).

**Challenge and response.** A width-independent state description can still retain growing time histories and sample-pair arrays. Saddle-point derivation and empirical agreement are not a general rigorous finite-width convergence theorem or certified solver. These qualifications leave a useful computational and mechanistic reformulation. Missing all-time certification is material only to such a stronger claim.

**Assessment and influence.** H specialist, S–H broad; specialist B is a possible disputed upper boundary if computational unification is weighted strongly. Independent subsequent influence was not established sufficiently in the inspected sources; no landmark claim.

**Reading/uncertainty.** Main self-consistency construction, two-time/causal-operator equations, linear-network reduction, Algorithm 1 and discussion. Formal versus proved status is preserved; the full field-theory derivation and numerical convergence were not re-audited.

<a id="H24"></a>

## H24 — Schmid (2010), dynamic mode decomposition

**Result and advance.** Snapshot data yield a low-dimensional approximation of an intersnapshot map and its dynamic modes through Krylov/SVD reasoning. This enables temporal modal analysis directly from simulations and measurements. POD, Arnoldi and Koopman ideas are predecessors. [Author-uploaded primary paper](https://www.researchgate.net/profile/Peter-Schmid-5/publication/278621822_Dynamic_mode_decomposition_of_experimental_data/links/5602b96708ae849b3c0e4bef/Dynamic-mode-decomposition-of-experimental-data.pdf).

**Challenge and response.** The approximately fixed linear map across the observed interval is a consequential assumption for nonlinear data. Noise, sampling and extrapolation can matter; no general autonomous nonlinear closure theorem follows. The positive capability is a usable observational analysis method, not new foundational linear algebra. Its fluid-dynamics value cannot simply be transferred to deep-learning theory.

**Assessment and influence.** B model-reduction specialist, S as an adjacent broader-DL-theory comparison. Independent work supplies definitions, analysis and extensions, demonstrating substantial uptake. [Tu et al.](https://arxiv.org/pdf/1312.0041). Specialist landmark status is plausible, with a lower confidence than the technical contribution.

**Reading/uncertainty.** Primary §2 including map assumption, projected implementation and relation to decompositions, conclusions; Tu introduction. No full experiment or spectral-convergence audit.

<a id="H25"></a>

## H25 — Sutherland–Schneider (2015), random-feature error analysis

**Result and advance.** The paper distinguishes feature-map variants, analyzes variance and uniform error, and connects kernel approximation to prediction with approximated test features. It refines and corrects the earlier random-feature analysis rather than creating a new learning paradigm. [Primary paper](https://www.cs.cmu.edu/~dsutherl/papers/rff_uai15.pdf).

**Challenge and response.** Improved bounds and estimator choice are narrower than H06's computational representation. The clean variance advantage is kernel-specific (Gaussian), not universal over kernels. Fixed kernels and estimator-specific conditions remain; better constants are not automatically broad conceptual advances. Nevertheless, consequences for which approximation to use and for valid prediction bounds make this more than cosmetic algebra.

**Assessment and influence.** S specialist; below-S–S broad. This is a concrete lower anchor without imposing a category quota. Independent Sriperumbudur–Szabó (2015), §1 footnote 1 and §3, explicitly compares its refined constants/feature variants and improves the remaining rate bound. [Follow-on paper](https://www.gatsby.ucl.ac.uk/~szabo/publications/sriperumbudurszabo15optimal.pdf). This demonstrates concrete influence without a broad-field transformation.

**Reading/uncertainty.** Feature definitions/variance comparison, Propositions 1–2 and prediction discussion around Proposition 9. No full concentration-proof audit. Confidence high about incremental scope; exact allocation of all corrected original constants remains unverified.

## Equal-scrutiny confirmation and debate provenance

The user clarified equal scrutiny during Phase 1. No category was mechanically changed. H01/H03 limitations remain compatible with their main approximation discoveries; H14's convergence assumption limits the central optimizer guarantee; H17's theorem/conjecture distinction changes which claim can be credited; H13's source issue changes evidence confidence, without proving a mathematical failure. Historical papers are assessed for relevant unstated restrictions as well as disclosed ones. More candid reporting cannot count against a future contribution by itself.

All individual challenges received substantive advocate responses. Direct advocate/critic exchanges covered H01–H06, H07–H11, H12–H14, H15–H18, H19–H23, H24 and H25 by stable ID. The critic's independent case record and final audit remain companion evidence. The final calibration must preserve any differences between ranges or roles and can freeze only after both approve the same exact files.
