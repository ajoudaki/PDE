# Pham–Nguyen (2021): fluctuations and trajectorial stability

**Superseded assessment.** This is the initial full-reading report. Use [AUDIT_FLUCTUATIONS.md](AUDIT_FLUCTUATIONS.md) for the fresh proof audit: the claimed sharp coupling rate and long-time proof have material gaps. Do not quote the initial report's language as independent verification of those theorems.

**Source and coverage.** Huy Tuan Pham and Phan-Minh Nguyen, *Limiting fluctuation and trajectorial stability of multilayer neural networks with mean field training*, NeurIPS 2021, 4843–4855. [Official record](https://papers.nips.cc/paper_files/paper/2021/hash/2639ba2137371773aa1e64e7735cdb30-Abstract.html), [main paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/2639ba2137371773aa1e64e7735cdb30-Paper.pdf), [supplement](https://papers.nips.cc/paper_files/paper/2021/file/2639ba2137371773aa1e64e7735cdb30-Supplemental.pdf). Access checked 2026-10-11. Read the complete main paper, numbered pp. 1–13, including references/checklist, and complete supplement, numbered pp. 14–58, Appendices A–G. Visually inspected main pp. 7, 9 and 10 and supplement p. 50. Cached PDFs, full extracted texts and inspection images are in `data/generated/compression_literature_positioning_20261011/meanfield/`.

This is the one authorized direct follow-up to the separately assessed Nguyen–Pham framework. Comparison inputs remain `paper/main.tex` and `paper/feature_learning_theorem.tex`. No additional references were retrieved, no external code was inspected, and no experiments were run. The review skill, severity rubric and canonical-notation skill were applied in this assigned single-report format. Complete reading does not mean that all proofs have been independently reconstructed.

## Assessment

This belongs on the closest-prior-work shortlist. It is not merely a first-order population limit: it proves a quantitative second-order, sample-coupled approximation, a Gaussian output-fluctuation theorem, and conditional decay of width-scaled output variance. It explicitly investigates variability caused by random initialization and supports its predictions with repeated-seed experiments. Any statement that rigorous multilayer mean-field theory has no account of seed fluctuations or no below-leading-fluctuation correction would be inaccurate.

The remaining distinction is precise: its correction is function-valued and uses the mean-field trajectory plus a sampled-neuron process; its quantitative finite-width bounds have a fixed finite horizon; its infinite-time conclusion takes width to infinity first. It does not give a small, finite-coordinate, autonomous retained-state model coupled to the manuscript's differently normalized Gaussian network, with complete-trajectory and fitted-endpoint fidelity below a realized independent-seed discrepancy. This difference is not a flaw in the paper.

## Model, scaling and retained state

Use $D$ for the source paper's depth, which it calls $L$ and which counts the scalar output layer. The manuscript counts hidden layers, so its depth $L$ corresponds to source depth $D=L+1$. Write $f_N$ for the finite-network output, $f$ for the mean-field output, and $\widetilde f_N$ for the output obtained by evaluating the mean-field weights on sampled neurons; the source distinguishes these mainly by boldface and tildes on $\widehat y$. All hidden widths equal $N$; the output width is one. The data are $(X,Y)$, with input marginal law $P_X$, and $\varphi_i$ is the activation at layer $i$.

The source uses first-layer inner products and normalized averages at every later layer:

$$
H_1(t,j,x)=\langle w_1^N(t,j),x\rangle,
\qquad
H_i(t,j,x)=\frac1N\sum_{k=1}^N
w_i^N(t,k,j)\varphi_{i-1}(H_{i-1}(t,k,x)),
\qquad f_N(t,x)=\varphi_D(H_D(t,1,x)).
$$

The weight evolution is continuous-time, full-population gradient descent with the layer-normalized perturbative derivatives defined in §2, pp. 3–4. The theorem is not for minibatch SGD or a discretization error bound. The authors explicitly state this limitation on p. 2. The averaging normalization nevertheless admits nonlinear feature learning; “Gaussian fluctuation” does not mean “lazy first-order dynamics.”

Assumption 1, pp. 4–5, requires bounded hidden activations; bounded Lipschitz first and second activation derivatives; bounded Lipschitz first and second prediction derivatives of the loss; bounded inputs; width-uniform sub-Gaussian initialization moments; separable neuronal $L^2$ spaces; and equal hidden widths. The authors discuss proportional widths as an extension, not the displayed theorem. The loss need not be convex. A smooth Huber loss and tanh hidden activations are their explicit example.

As in the 2023 framework, the neuronal ensemble is a fixed product probability space with independent labels $C_i\sim P_i$, and the population weights are functions $w_i(t,c_{i-1},c_i)$. Endpoint labels $C_0$ and $C_D$ equal one; the first-layer weight is vector-valued and the later weights are scalar. One samples $C_i(j)$ once and initializes

$$
w_i^N(0,j,k)=w_i(0,C_{i-1}(j),C_i(k)).
$$

Independent sampled labels need not make all edge weights independent. The framework is designed to accommodate both i.i.d. and correlated initialization through the embedding; the paper does not require the particular bidirectional-diversity initialization used for some global-convergence theorems. Nor does it prove unconditional convergence from an arbitrary embedding.

The fluctuation description has two components (§3, pp. 5–9):

- A sampled-neuron process $\widetilde G_N=(\widetilde G_N^y,\widetilde G_{N,i}^w)$, with $\widetilde G_N^y=\sqrt N(\widetilde f_N-f)$ and analogous scaled perturbations of the output derivatives. It converges in the stated polynomial-moment sense to a centered Gaussian process $G$ with time-, input- and layer-dependent covariance.
- The second-order response $R_i(G,t,c_{i-1},c_i)$, initialized at zero and solving a linear equation in $R$ and the forcing $G$, with coefficients supplied by the evolving nonlinear mean-field network. Theorem 3, p. 6, and Theorem 21, pp. 26–30, place $R_i$ in $L^2(P_{i-1}\times P_i)$ and prove existence, uniqueness and continuity/linearity in $G$. Equation (6), p. 15, explicitly includes adjacent-layer derivative terms suppressed by the main paper's concise notation.

Thus the first-order dynamics are nonlinear, while the fluctuation evolution is a linear response along that nonlinear trajectory. Neither the index $i\in\{1,\ldots,D\}$ nor the phrase “system of ODEs” makes the state finite-dimensional: each $R_i$ is a function on a neuronal product space, and $G$ is a process indexed also by input and time. Theorem 19, pp. 25–26, gives a dynamical form for the Gaussian component; it does not give a finite-coordinate closure. A joint infinite-dimensional representation may be evolved, but the paper proves no numerical truncation, finite coefficient count or compression/storage bound. Sampling a finite number of neurons does not remove the full mean-field functions and expectations required by this construction.

**Exact normalization mismatch with the manuscript.** For a manuscript hidden matrix with $W_{kj}^{(\ell)}(0)\sim\mathcal N(0,1/N)$ and forward map $W^{(\ell)}h^{(\ell-1)}$, identifying the same forward map with the source's averaged coordinates requires $w_\ell(j,k)=N W_{kj}^{(\ell)}$. The latter has variance $N$, not the width-uniform sub-Gaussian scale of Assumption 1. Consequently the source's constants cannot simply be treated as uniform for this identification. Squared loss and potentially unbounded activation values in the manuscript also require extensions beyond the globally bounded derivative/activation assumptions as stated. The shared words “Gaussian initialization” and “feature learning” do not eliminate these differences.

## What is quantitatively coupled

Fix a finite terminal time $T$. Let $\mathbb E$ average the random neuron samples and let $\mathbb E_J$ average uniform finite-network indices. Constants $K_T$ may depend on $T$ and the fixed model assumptions, but not on $N$. Define the coupled weight fluctuation

$$
R_i^N(t,j,k)=\sqrt N\bigl(w_i^N(t,j,k)-w_i(t,C_{i-1}(j),C_i(k))\bigr).
$$

Theorem 5, p. 7, proves, for every $t\le T$,

$$
\mathbb E\mathbb E_J
\left|R_i^N(t,J_{i-1},J_i)
-R_i(\widetilde G_N,t,C_{i-1}(J_{i-1}),C_i(J_i))\right|^2
\le \frac{K_T}{N}.
$$

In original weight units, the mean-field trajectory plus this sampled second-order correction has root-mean-square remainder $O_T(N^{-1})$, smaller than the leading $N^{-1/2}$ fluctuation scale. This is an actual coupling using the same sampled labels, not merely a comparison of marginal distributions. Appendix D, pp. 31–45, proves it using high moments, truncation, sample-replacement estimates and Gronwall control; shared randomness is explicitly handled rather than assumed away (main §3.4, p. 9; supplementary Lemmas 12 and 31).

The output counterpart appears at the start of Appendix E.2, p. 46. Define the sample-coupled correction

$$
\mathcal C_N(t,x)=\widetilde G_N^y(t,x)
+\sum_{i=1}^{D}\mathbb E_C\left[
R_i(\widetilde G_N,t,C_{i-1},C_i)
\frac{\partial f(t,x)}{\partial w_i(C_{i-1},C_i)}\right],
$$

where the derivative is the paper's normalized perturbative derivative. The proof gives

$$
\sqrt N(f_N-f)=\mathcal C_N+O_T(N^{-1/2}).
$$

Here $O_T$ is the integrated root-mean-square convention defined on p. 16, not a supremum over all inputs or sample paths. Thus it yields an $O_T(N^{-1})$ root-mean-square error for $f+N^{-1/2}\mathcal C_N$ at fixed time. It would be wrong to deny the paper any sub-fluctuation-scale predictor. The crucial caveat is its representation, horizon and normalization—not the absence of a correction.

Theorem 2, pp. 5–6, gives Gaussian-process convergence in the defined polynomial-moment tests at rate $N^{-1/8}$. Proposition 8, p. 8, extends this to the joint pair $(R(\widetilde G_N),\widetilde G_N)$ at rate $N^{-1/8+o(1)}$. Theorem 6, p. 7, gives the output limit

$$
\sqrt N(f_N(t,x)-f(t,x))\ \Longrightarrow
\widehat G(t,x)
=G^y(t,x)+\sum_{i=1}^{D}\mathbb E_C\left[
R_i(G,t,C_{i-1},C_i)
\frac{\partial f(t,x)}{\partial w_i(C_{i-1},C_i)}\right].
$$

It also states an explicit $K_{T,m}N^{-1/8+o(1)}$ bound for differences of data-integrated $m$th output-fluctuation moments against any measurable test $h(x)$ bounded by one. It is not a $N^{-1/8}$ prediction-error rate and not a pathwise coupling to an independently generated Gaussian process. Time-dependent moment tests in the definitions capture joint temporal structure, but the displayed quantitative theorems do not state $\mathbb E\sup_{t\ge0,x}|\cdot|$ control. Constants depend on $T$; none of these finite-width statements licenses setting $T=\infty$.

## Infinite-time variance: exact statement and order

Section 4, p. 9, defines

$$
V^*(t)=\lim_{N\to\infty}N\,\mathbb E\mathbb E_X|f_N(t,X)-f(t,X)|^2
=\lim_{N\to\infty}N\,\mathbb E\mathbb E_X|f_N(t,X)-\mathbb E f_N(t,X)|^2.
$$

The equal limits follow from the preceding fluctuation results. Assumption 2 requires that the conditional expected second prediction derivative of the loss, at every prediction where the conditional first derivative vanishes, is a positive constant almost surely. Define the conditional loss derivative along the mean-field trajectory by

$$
r_t(X)=\mathbb E_{Y\mid X}[\partial_2\mathcal L(Y,f(t,X))].
$$

Theorem 9 assumes $r_0=0$ almost surely. Under Assumptions 1–2, $V^*(t)$ is non-increasing and tends to zero. At first order the mean-field network is stationary; the finite-width fluctuation still evolves and is damped. The proof in Appendix F.1–F.2, pp. 47–49, places the initial output fluctuation in the orthogonal complement of the kernel of a negative semidefinite compact response operator, then applies its semigroup. This allows convergence without assuming a spectral gap and supplies no uniform positive decay rate.

Theorem 10 assumes, for some $\delta>0$,

$$
\int_0^\infty t^{2+\delta}\|r_t\|_{L^2(P_X)}\,dt<\infty.
$$

Under Assumptions 1–2 it concludes $V^*(t)\to0$. This is an assumed sufficiently fast convergence condition, not a global-convergence-rate theorem. For example, an eventual bound $\|r_t\|_2\lesssim(1+t)^{-q}$ satisfies this displayed condition when $q>3+\delta$. The theorem does not claim variance is monotone throughout a nonstationary initial transient. Nonconvex losses are allowed; the authors note that the conclusions also concern stationary predictions satisfying Assumption 2, with a global optimum being the main motivating case. Unregularized dynamics matter to their argument (p. 2).

The quantifier is

$$
\lim_{t\to\infty}\lim_{N\to\infty}
N\,\mathbb E\|f_N(t,\cdot)-\mathbb E f_N(t,\cdot)\|_{L^2(P_X)}^2=0.
$$

It is not a theorem interchanging those limits, controlling the finite-width remainder uniformly to infinite time, proving the fitted endpoint exists for each sufficiently wide finite network, or identifying a coupled reduced model's fitted endpoint. Uniform-in-time estimates inside Appendix F concern the limiting system used to prove variance decay; they are not an all-time upgrade of Theorems 5–6.

The main theorem's conditional-root residual condition above was checked directly in the rendered p. 9. Appendix F.3, Eq. (8), p. 50, writes a differently expressed weighted square of the unconditioned loss derivative in its proof development. This assessment reports the exact main statement; it does not assert that all notational reductions and terminal-comparison estimates in that lengthy argument have been independently verified. The positioning does not require rejecting or weakening the stated theorem.

## Relation to actual independent-seed discrepancy

There is a direct and useful connection, but it must be stated at the correct level. For independent identically initialized copies $f_N^{(1)}$ and $f_N^{(2)}$, independence alone gives

$$
\mathbb E\|f_N^{(1)}-f_N^{(2)}\|_{L^2(P_X)}^2
=2\mathbb E\|f_N-\mathbb E f_N\|_{L^2(P_X)}^2.
$$

Consequently, at each fixed $t$, the paper's second-moment limit implies that $N$ times this expected squared independent-seed discrepancy tends to $2V^*(t)$. This is a deduction from its result, not an additional theorem printed in the source. It shows why the follow-up is essential prior work for seed variability.

Nevertheless, an expected squared discrepancy is not a high-probability lower bound for the realized discrepancy of a particular pair, nor a small-ball estimate in the manuscript's prediction norm. No covariance nondegeneracy or such lower bound is part of Theorems 5–10. Indeed the endpoint theorem deliberately drives the leading variance to zero, so a fixed positive $N^{-1/2}$ denominator cannot be assumed uniformly through fitting. Combining the coupled $N^{-1}$ correction with a suitable nondegenerate fixed-time CLT could support a below-seed statement in a matched setting, but that requires extra denominator and representation arguments, and would still not establish the manuscript's complete-trajectory/endpoint contract.

## Numerical evidence

Figure 1, p. 10, and Appendix G, pp. 57–58, provide original numerical illustrations:

- A three-weight-layer network (two hidden layers), tanh hidden activations, identity output and widths $N\in\{50,100,200,400\}$; 100 MNIST images of digits 0/4 versus 5/9; full-batch discrete GD with learning rate $7\times10^{-3}$ and a Huber loss.
- Random initialization uses first-layer variance $1/785$ and independent middle/readout weights with law $\mathcal N(0.1,1)$, in the averaged source coordinates. This is neither the manuscript's centered hidden $\mathcal N(0,1/N)$ initialization nor its zero readout.
- Panel (a): one training trajectory per width. Panel (b): 1000 random seeds, a single held-out image, iteration $10^3$, and centered width-scaled output histograms.
- Panel (c): output variance estimated using 10 independent runs and all 100 training inputs. Panel (d): Monte Carlo sampling variance from neuron subsamples of a reference network of width 5000, using 10 repetitions at each reference time.
- Panel (e): one width-5000 network is trained for $10^5$ iterations, then neuron-subsampled to initialize all repetitions at the smaller widths; subsequent training suppresses the residual variance. This is an approximate stationary-population initialization, not independent training of multiple width-5000 references.

The plots show compatible width-rescaled histograms and late-stage suppression of trained-output variance, in contrast to the plateau of the Monte Carlo sampling component. They are evidence consistent with the claimed fluctuation and damping phenomena, not measurements of a finite compressed state's error, a realized error/seed-discrepancy ratio, a population supremum norm, or a rigorous fitted-endpoint tolerance.

The checklist, pp. 12–13, explicitly reports no error bars. The main mathematical example asks for a smooth Huber loss, whereas Appendix G writes the ordinary piecewise Huber loss; no smoothing is specified there, so the illustration should not be presented as an exact implementation of every regularity hypothesis. A GitHub code link is supplied on p. 58, but inspecting or running that repository was outside this bounded review. No numerical claims were independently reproduced.

## Evidence ledger and safe positioning

| Claim | Assessment and exact evidence |
|---|---|
| Rigorous finite-width fluctuation coupling exists. | Supported by Theorem 5, p. 7, and its complete Appendix D proof, pp. 31–45. The leading fluctuation is coupled to the same sampled neurons; the unscaled RMS remainder is $O_T(N^{-1})$. |
| An output CLT with quantitative rates exists. | Supported by Theorems 2 and 6, pp. 5–7; Proposition 8, p. 8; Appendices B and E. The explicit rate is for moment tests, not uniform prediction error. |
| Training damps seed-driven fluctuations even at a stationary mean-field predictor. | Theorem 9 and Appendix F.1–F.2; Figure 1(e) is a finite experiment using a trained reference network. |
| Generic training variance vanishes at the fitted endpoint of a fixed finite network. | Not the stated theorem. Theorem 10 assumes a weighted convergence rate and takes width first, time second. |
| A finite-coordinate autonomous compressed simulator is furnished. | Not established. The defining state and corrections are functions/processes on neuronal and input spaces; no retained-coordinate/storage bound is given. |
| The manuscript's realized below-seed ratio is already proved. | Not established in this source. Scaling, norm, finite representation, time quantifiers and random-denominator control need separate arguments. |

Confidence is high in these scope distinctions and exact theorem quantifiers. The Gaussian covariance construction, sample-replacement mechanism, second-order expansion, and stationary-operator mechanism were followed through their full presentations. The combinatorial moment estimates, truncation arguments and nonstationary terminal comparison were read but not re-proved line by line. No unsupported fatal/major/minor flaw classification is made. A comparison target absent from the source is not itself a paper weakness.

**Suggested related-work wording:** “Pham and Nguyen further establish quantitative, sample-coupled second-order mean-field corrections and a Gaussian limit for multilayer output fluctuations. They also prove decay of width-scaled output variance under stationary initialization or sufficiently fast population convergence. These results rigorously characterize initialization-driven variability, but use function-valued mean-field states and fixed-horizon finite-width estimates; their long-time variance conclusion takes the width limit first. Our question additionally requires a finite autonomous retained representation for the specified finite Gaussian network, with complete-trajectory and fitted-endpoint prediction error below its actual independent-run variability.”

This source strengthens the prior-work baseline. It narrows the defensible novelty distinction to the full combination of representation, coupling, scaling, observables and order of limits, rather than the existence of rigorous nonlinear dynamics or seed-fluctuation theory.
