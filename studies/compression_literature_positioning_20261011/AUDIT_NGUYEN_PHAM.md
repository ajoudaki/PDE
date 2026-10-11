# Independent source-first audit: Nguyen–Pham (2023)

## Scope and verdict

Source: P.-M. Nguyen and H. T. Pham, *A rigorous framework for the mean field limit of multilayer neural networks*, Mathematical Statistics and Learning 6 (2023), 201–357, DOI [10.4171/MSL/42](https://doi.org/10.4171/MSL/42). Frozen inputs: `data/generated/compression_literature_positioning_20261011/meanfield/nguyen_pham_2023.pdf` and `.txt`. All 157 pages were read, including Appendices A–G and references. Printed pages 265 and 325 were also rendered and visually checked. This is a venue-neutral mathematical audit, not a score or an experiment reproduction. No submitted code, training, manuscript editing, or Git operations were performed.

The principal finite-horizon neuronal-embedding approximation is substantial and survives the reconstructed high-leverage checks below. It couples actual initialized finite parameters to a continuum trajectory, handles simultaneous width growth, and explicitly accommodates both correlated initialization and a separate construction for independent edge initialization. It is not a theorem about arbitrary conventional Gaussian/NTK scaling. Its continuum state is generally infinite-dimensional.

The long-time results have much stronger hypotheses than finite-time approximation: convergence of weighted parameter moments, uniform terminal-layer stationarity or replacement Morse–Sard conditions, and feature-diversity assumptions. Moreover, the arbitrary-depth endpoint proof contains a demonstrably invalid use of an unrestricted cross-layer coupling. A product-of-layerwise-couplings restriction repairs that particular step but is stronger than the printed hypothesis. Theorem 8.4 has additional unresolved uniformity/compactness steps. These findings do not invalidate the finite-horizon theorem and are not counterexamples to the full global-convergence conclusions.

Evidence levels used below: **checked** means a calculation or proof step reconstructed here; **source theorem** means a result stated in the fully read source whose entire proof has not been independently reproduced; **gap** means a specific displayed inference is unjustified or false; **not established** is not an assertion of falsity.

## Model and exact normalization

For the fully connected specialization (Sections 6–7), the paper counts weight layers by (L), with hidden widths (n_1,\ldots,n_{L-1}) and scalar terminal width (n_L=1). Writing (f_n) for its prediction,

\[
 H_1(x,j)=w_1(j)\cdot x,\qquad
 H_i(x,j)=\frac1{n_{i-1}}\sum_k w_i(k,j)\varphi_{i-1}(H_{i-1}(x,k)),\qquad
 f_n(x)=\varphi_L(H_L(x,1)).
\]

The SGD update is (w_i(k+1)=w_i(k)-\epsilon\xi_i(k\epsilon)\Delta_i^w(Z_k;W(k))), with independent (Z_k=(X_k,Y_k)\sim P\), independent of initialization. The backward recursion averages over the next-layer width. Consequently, relative to the ordinary Euclidean parameter gradient, the mobility is (n_1\xi_1) for first-layer vectors and (n_{i-1}n_i\xi_i) for edge weights (i\ge2). Thus both the forward normalization and compensating learning rates matter. Time is (t=k\epsilon); the continuum equation averages over the fixed data law (P). An empirical data law is admissible, but a finite training set is not required.

The broader Section 2 model uses separable Hilbert parameter/feature spaces and forward maps (\phi_i(w,b,h)), including biases and suitable convolutions, with specified backward maps (\sigma_i). It is not an unrestricted architecture class. Assumptions 2.4–2.6 require bounded Lipschitz schedules; first-layer forward Lipschitz control; higher-layer growth at most (K(1+|w|+|b|)), with controlled weight-dependent Lipschitz factors in hidden features; bounded/Lipschitz terminal backward signal; and linear-growth, controlled-Lipschitz update maps. For fully connected networks, bounded inputs, bounded hidden activations and bounded Lipschitz activation/loss derivatives supply these conditions. Raw ReLU and a globally unbounded squared-loss derivative do not automatically satisfy them. Bounded-derivative smooth losses such as pseudo-Huber do. The regularized examples still have to satisfy the stated update-map assumptions; the examples are not blanket permission for arbitrary regularizers.

For optimization, the learning-rate schedules are nonnegative; the relevant terminal schedules are additionally fixed to one in the theorems. The general approximation formalism is broader than gradient descent and does not itself assert decreasing risk.

The neuronal ensemble is a product probability space (\prod_{i=1}^L(\Omega_i,P_i)), with (\Omega_L=\{1\}). Continuum weights are deterministic functions (w_1(t,c_1)) and (w_i(t,c_{i-1},c_i)). Replace finite neuron averages by integration against (P_i), then evolve

\[
 \partial_t w_i(t,c_{i-1},c_i)
 =-\xi_i(t)\mathbb E_Z\Delta_i^w(Z;c_{i-1},c_i;W(t)).
\]

Initialization is coupled by evaluating these functions at sampled labels (C_i(j)). This shares the finite network's initial realization, not merely its marginal distribution. Sampling rules are independent between layers and satisfy the paper's quantitative near-independence condition within each layer. Assumption 4.4 uses a scale (\eta_i=n_i^{-0.501}); independent sampling has zero error. Assumption 4.6 imposes uniformly sub-Gaussian marginal parameter norms, equivalently (\sup_{p\ge1}p^{-1/2}\|w_i^0\|_{L^p}<\infty), and similarly for biases. It does not require all entries to be independent.

## What finite-width approximation actually says

Theorem 3.1 (pp. 217–220; Appendix B) gives global existence and uniqueness on each finite horizon in the paper's moment-controlled trajectory space. Its initial norm requires 50th moments and sub-Gaussian higher-layer weights; the first-layer/bias requirements for this existence statement are weaker than the fully sub-Gaussian assumption used for quantitative sampling.

Theorem 4.7 (p. 224; Sections 4.3–4.4 and Appendix C) gives positive constants (c_1<1/2), (c_2<1/52), independent of horizon and depth, but **horizon- and depth-dependent thresholds** (n_*(T,L,c_1,c_2)), (\epsilon_*(T,L,c_1,c_2)). Once these thresholds hold, its coupled parameter error obeys the form

\[
 \mathbb P\!\left(D_T\ge K(n_{\min}^{-c_1}+\epsilon^{c_1})
 \sqrt{\log(n_{\max}^2/\delta+e)}\right)
 \le2\delta+KL n_{\max}e^{-K n_{\min}^{c_2}}.
\]

Here (D_T) is the maximum over layers/types of empirical root-mean-square parameter discrepancies along the matched labels, with trajectory suprema as specified in (4.1). It is not a Gaussian fluctuation expansion. Some auxiliary displayed definitions omit a time supremum in an edge-weight line; the intended trajectory metric is given in (4.1) and the surrounding proof. No claim here depends on interpreting those omissions as a stronger result.

The proof separates finite population-gradient-flow particles from discrete SGD: Theorem 4.12 handles particle/continuum error, Theorem 4.13 handles particle/SGD error, and the triangle inequality combines them. Corollary 4.9 transfers approximation to bounded Lipschitz tests of hidden features and Lipschitz tests of prediction/loss, on a fixed horizon. Its printed proof has the missing term identified below; the desired finite-time transfer can be recovered by reusing the earlier forward concentration argument.

The statement is compatible with unequal widths, but the failure probability and logarithmic factor still involve (n_{\max}). A sufficient asymptotic regime used elsewhere in the paper is (n_{\min}\to\infty) with (n_{\min}^{-c}\log n_{\max}\to0) for every (c>0). It is not a width-ratio-free numerical guarantee at arbitrary finite sizes. There is no uniform-in-(T\to\infty) estimate in this theorem.

### Reconstructed finite-horizon proof checks

1. **Moment induction.** Starting from bounded terminal backward signal, the terminal weights grow at most linearly in time. Cauchy–Schwarz in the next-neuron variable gives, schematically,
   \(\|\Delta_i^H\|_{L^p}\le K(1+\|\Delta_{i+1}^H\|_{L^2})(1+\|w_{i+1}\|_{L^p}+\|b_{i+1}\|_{L^2})\).
   Integrating backward layer by layer bounds the 50th moments and preserves sub-Gaussian higher-layer weights on every fixed horizon. Constants may grow rapidly with depth/time. This verifies the mechanism in Lemma 3.2 and Appendix B.1, not a uniform-time moment bound.

2. **Existence despite unbounded weights.** The truncated Lipschitz estimate for the Picard map is of the form
   \(\|F(U)-F(V)\|_t\le C_{T,L}\int_0^t[(1+B)\|U-V\|_s+e^{-cB^2}]\,ds\).
   Iterating (m) times and choosing (B\asymp\sqrt m) gives the factorial-controlled term ((C\sqrt m)^m/m!) and an exponentially small truncation remainder. Both are summable. This is why ordinary globally Lipschitz ODE theory is not being silently assumed.

3. **Bounded-initialization approximation.** Propositions 4.14–4.15 establish errors of scale
   \([n_{\min}^{-1/2}\sqrt{\log(\cdot)}+\sqrt\epsilon\sqrt{\log(\cdot)}]\exp(C_{T,L}(1+B))\).
   The forward recursion separates parameter error from empirical quadrature; the backward recursion then propagates both errors. A time grid and time-Lipschitz estimates give finite-horizon control. The SGD term is a martingale over data draws, conditional on the initialization. No independence between trained weights is claimed.

4. **Truncation balance.** Proposition 4.16 contributes \(\exp[-cB^2+C_{T,L}(1+B)]\), with a sampling failure term involving \(e^{-c'B^2}n_{\min}^{1/52}\). Set (B=a\sqrt{\log n_{\min}}), with fixed sufficiently small (a>0). Then (e^{C_{T,L}B}=n_{\min}^{o(1)}), while the tail is (n_{\min}^{-ca^2+o(1)}) and the failure exponent remains a positive power of (n_{\min}). This gives positive universal exponents only after allowing the thresholds to depend on (T,L). The analogous balance with \(\log(1/\epsilon)\) handles SGD. The calculation explains both the sub-root-width rate and its finite-horizon character.

5. **Dependent edge averages.** Appendix C.2 does not count all (n_{i-1}n_i) edges as independent. It decomposes a rectangular edge average into cyclic matchings with distinct endpoints and then applies the near-independence estimate along each matching. This gives concentration governed by the smaller neuron count. A conditional-mean step should retain both layers' near-independence errors, rather than just one; their sum is at most twice the larger one and is absorbed by the generic constants. This does not change the stated rate.

## Independent initialization and the actual degeneracy result

Section 5 and Appendix D construct a canonical embedding for ordinary *independent edge weights under this paper's mean-field normalization*. This is distinct from asserting that a fixed atomless neuronal kernel can encode arbitrary independent dense edge arrays by iid endpoint samples.

The construction uses (\Omega_i^M=\Lambda\times[M]), independent countable coordinate processes on (\Lambda), and discrete labels sampled without replacement within a layer. It realizes the exact desired independent initialization for widths at most (M). Proposition 5.2 bounds the dependence error by (2(n_i-1)/M); choosing (M) sufficiently large permits Theorem 4.7. There is no nonexistent uniform probability measure on the positive integers: (M\to\infty) is a second limiting construction.

Theorem 5.3, in full Theorem D.1 (pp. 334–343), approximates the canonical continuum by deterministic functions of a few *initial parameter arguments*, with
\(\sup_{t\le T}\|W^M(t)-W^\infty(t)\|_{L^2}\le K_{T,L}M^{-0.499}\)
for sufficiently large (M). This is a supremum of mean-square norms, not automatically the mean of a trajectory supremum. The collision calculation in Appendix D.2 has probability (1/M), giving a squared forward error (O(1/M)); truncation and Gronwall turn root-(M) error with logarithmic/subpolynomial losses into the stated (M^{-0.499}). Repeated backward recursions can accumulate depth-dependent powers of \(\log M\), so the intermediate universal \(\sqrt{\log M}/M\) display needs care; any fixed-depth logarithmic power is still absorbed by (M^{0.001}). This does not refute D.1's stated exponent.

For constant initialized biases, Corollary 5.5 says that the preactivations of layers (2,\ldots,L-2) become neuron-independent for (L\ge4). For (L\ge5), with update maps independent of the edge's own weight, Corollary 5.6 says interior edge matrices (i=3,\ldots,L-2) move by a shared deterministic offset. Directly integrating the displayed ODE verifies this: its right side loses both neuron labels once adjacent biases and hidden/backward signals are deterministic. These are genuine degeneracy statements under the designated scaling and initialization. They neither say that every layer collapses nor give a fixed finite-dimensional autonomous state for the entire trained network: boundary-layer functions still evolve over their continuous initialization arguments, and their integrals drive the scalar offsets.

## Endpoint assumptions and what can be reconstructed

For two layers, Assumption 6.1 requires sub-Gaussian initialization; support containing the graph of a bounded continuous map (u\mapsto F(u)) over all first-layer weights (u\in\mathbb R^d); bounded hidden activation, bounded Lipschitz derivatives and loss derivative, bounded input, nowhere-zero output derivative; density of the span of (\varphi_1(u\cdot x)) in (L^2(P_X)); and the assumed convergence

\[
 \mathbb E_{\pi_t}[|\bar w_2(C)|\,|w_1(t,C')-\bar w_1(C)|
       +|w_2(t,C')-\bar w_2(C)|]\to0,
 \qquad \operatorname{ess\,sup}_{C}|\partial_t w_2(t,C)|\to0.
\]

Theorem 6.2 concludes global population-risk optimality for convex loss, or zero loss for deterministic labels and a nonnegative loss whose zero derivative implies zero loss. It **assumes**, rather than proves, the convergence/stationarity premises. First-layer universality may require an appended constant coordinate to represent biases; it should not be inferred for an arbitrary bias-free data domain.

The full-support proof can be reconstructed without relying on the cited topology informally. On the bounded initial graph, the first-layer characteristic (M_t(u)) is continuous and has uniformly bounded displacement, (|M_t(u)-u|\le R_t). For any target (v), the map (u\mapsto v-(M_t(u)-u)) sends the closed ball centered at (v) of radius (R_t) into itself. Brouwer's fixed-point theorem therefore gives (M_t(u)=v). Continuity of the full two-parameter characteristic map transfers positive initial mass near the graph point to a neighborhood of (v); one must use the joint initial distribution here, not assume the entire distribution lies on the graph. Thus first-layer full support persists at finite time.

Uniform smallness of the terminal-weight velocity then bounds the inner product of the conditional loss residual with *every* current first-layer feature. Passing to the assumed limit and using density annihilates the residual. Convexity supplies the pointwise supporting-line inequality, and conditional expectation gives global risk optimality. This reconstruction supports Theorem 6.2 under its actual hypotheses.

Three-layer Theorem 6.6 uses first-layer full support, smooth bounded hidden activations, appropriate weighted convergence and uniform middle-layer stationarity. It additionally requires either a frozen, nontrivial readout or, for a trained readout, initial risk strictly below the zero-output baseline. That condition prevents the limiting readout from vanishing in the argument. It is not an arbitrary-depth independent-initialization theorem.

For arbitrary depth, Assumption 7.1 replaces ordinary iid initialization by **bidirectional full support in function spaces**:

\[
 \operatorname{supp}(w_1^0(C_1),w_2^0(C_1,\cdot))
 =\mathbb R^d\times L^2(P_2),\quad
 \operatorname{supp}(w_i^0(\cdot,C_i),w_{i+1}^0(C_i,\cdot))
 =L^2(P_{i-1})\times L^2(P_{i+1}).
\]

It also assumes weighted pathwise parameter convergence under a coupling (\pi_t) of \(\prod_iP_i\) with itself, uniform terminal-layer velocity convergence to zero, and non-obstructiveness of higher activations: the span of \(\{\varphi_i\circ g:g\in L^2(P_X)\}\) is dense. Theorem 7.2's proof uses the reversible finite-time flow of adjacent incoming/outgoing function pairs to preserve support, then an annihilator argument to propagate feature density. These are rich function-space assumptions, not a statement that iid Gaussian dense initialization automatically supplies the desired diversity.

The risk corollaries (6.3, 6.7, 7.4) take the small-step and large-width limits before the large-time limit. They do not permit interchanging a fitted finite-network endpoint with the infinite-width limit, and they do not supply a seedwise fixed-width training-to-convergence error bound.

## Specific proof defects and their impact

### F1. Missing quadrature in the output-corollary proof — minor/local, high confidence

Appendix C.2, p. 325, bounds its (Q_{1,i}(t)), comparing finite-network hidden features with continuum hidden features at sampled labels, solely by the coupled parameter discrepancy (D_t). This is false even at initialization. Take (L=2), (X=1), (w_1^0=1), (w_2^0(C)=C\in\{-1,1\}) symmetric, hidden activation \(\tanh\), identity output, and zero biases. Exact parameter coupling gives (D_0=0), but
\[
 H_2^n(0,1)=\tanh(1)\frac1n\sum_jC_j,
 \qquad H_2(0,1)=0.
\]
For odd (n), the discrepancy is nonzero for every sample. All parameters are bounded. A bounded smooth loss with zero derivative at the chosen trajectory can be used if an update law is desired. The displayed zero-error conclusion is therefore an actual false intermediate bound.

Repair: insert the sampled-continuum forward network and keep the empirical integration remainder at each layer. The argument already carried out in Proposition 4.14, Steps 3–4, supplies precisely this term, of order root-width times the truncation factor. The target sub-root-width Corollary 4.9 can survive this repair. This is not a counterexample to Theorem 4.7 or Corollary 4.9 itself.

### F2. Arbitrary cross-layer couplings do not justify the endpoint telescoping — major proof gap, high confidence

Assumption 7.1(4), p. 257, permits **any** coupling of the two product measures. The proof on p. 265 iterates integrations over paired layer variables as if those pairs were independent. A coupling of product marginals need not be a product of layerwise couplings.

Here is an explicit test of the disputed parameter-to-output implication. Let (L=3), (P_1=P_2=\operatorname{Unif}\{-1,1\}), (X=1), both first weights equal (1), and both readouts equal (1). Let the proposed limit have \(\bar w_2(a,b)=a\), while the other network has \(w_2(a',b')=b'\). Choose \(\varphi_1(s)=\tanh(s)\), \(\varphi_2(s)=\tanh(s+1)\), and identity output. Couple \((C_1',C_2')=(C_2,C_1)\). Each marginal is the correct product law. Every parameter difference inside the weighted convergence assumption is identically zero. Nevertheless, with (q=\tanh(1)>0\),
\[
 f_{\bar W}(1)=\tanh(1),\qquad
 f_W(1)=\tfrac12[\tanh(1+q)+\tanh(1-q)]<\tanh(1).
\]
The strict inequality follows from strict concavity of \(\tanh\) on the positive interval \([1-q,1+q]\). Thus zero cost under the stated unrestricted coupling does not identify the represented function. The same example has zero squared weighted cost and therefore also tests the analogous convergence premise in Assumption 8.3.

This example is **not** a full counterexample to Theorem 7.2: it does not satisfy bidirectional diversity or exhibit the required training trajectory. It conclusively falsifies the generic convergence-to-output inequality used in that proof. Requiring \(\pi_t=\bigotimes_i\pi_{i,t}\) makes the telescoping valid; alternatively an additional argument must show that the actual trajectories and stated diversity admit such a coupling. Neither implication is supplied in the printed proof. Theorem 7.2 and 8.4 should therefore be cited with this unresolved proof qualification, not as independently verified endpoint theorems under the literal unrestricted-coupling hypothesis. The two-layer coupling has only one nontrivial layer pair and is unaffected.

### F3. Additional Morse–Sard proof obligations remain unresolved — do not treat as a certified endpoint extension

Theorem 8.4 replaces uniform terminal stationarity by weighted squared-moment convergence plus a strong radial (C^1) limit and superlevel-boundary gradient conditions on an infinite-dimensional sphere. The proof on pp. 268–269 claims convergence of the potentials uniformly over all (u\in L^2(P_{L-2})\), although changing lower-layer features generally gives only a bound proportional to \(\|u\|\). The elementary test (a_t\to0\), (a_t\ne0\), has \(\sup_u|\tanh(a_tu)-\tanh(0)|=1\): convergence of the feature coefficient alone does not give this uniformity. Also, boundedness and continuity alone do not ensure the asserted positive local maximum of the potential or its radial limit on a noncompact Hilbert sphere. I did not construct a counterexample satisfying the paper's entire neural potential and Morse–Sard assumptions, so these remain explicit missing arguments rather than theorem falsifications. The source's potential definition also uses lower preactivations where the forward formula ordinarily uses their activated features; the intended identification should be clarified before reusing the proof.

The finite-dimensional two-layer argument in Appendix G has a more plausible compactification mechanism, but its final transfer from a sphere-at-infinity gradient bound to a uniform Euclidean gradient bound on an unbounded superlevel boundary also needs justification: angular gradients scale as (1/r). No complete independent certification of the Morse–Sard alternatives is claimed here. These concerns are localized to the endpoint extension, not imported into the finite-time limit.

## External dependencies and independent coverage

The important probabilistic dependency is Pinelis [30]. I inspected the primary [author preprint](https://arxiv.org/pdf/1208.2200), definitions of martingales and 2-smooth spaces, Theorems 3.1–3.2 with their cosh-supermartingale proof, and Theorem 4.1 and its local proof. A Hilbert space is 2-smooth with constant one by the parallelogram identity; finite-horizon increments satisfy the integrability requirements. The bounded-increment application is therefore legitimate. The entire 44-page dependency and its recursively cited results were not read. A later correction was discoverable, but its primary text was not retrieved; no claim of auditing all corrections is made.

The weaker moment estimate actually needed here can also be recovered directly. For (p\ge2\), the function \(F(U)=\|U\|_{L^p(\Omega;H)}^2\) satisfies \(D^2F(U)[V,V]\le2(p-1)\|V\|_{L^p}^2\), by differentiating and applying Hölder (with smoothing at zero). For Hilbert martingale differences (d_j\), the first derivative averages to zero conditionally, so Taylor's formula gives \(\|\sum_jd_j\|_{L^p}^2\le(p-1)\sum_j\|d_j\|_{L^p}^2\). If \(\|X_j\|_{L^p}\le Kp^{k/2}\), then \(\|d_j\|_{L^p}\le2Kp^{k/2}\), yielding at most \(Kp^{(k+1)/2}\sqrt n\). The drift caused by near-independence is bounded by truncating at (B): \(n\eta B+Kn p^{k/2}e^{-cB^{2/k}/p}\). Taking (B^{2/k}\asymp p\log n\) gives the looser (Kp^{1+k/2}\max(\eta n^{0.01},n^{-1/2})\) average bound used in Theorem A.3. This replaces any need here to certify every dependency in Pinelis's optimal Rosenthal argument.

The moment-to-tail equivalence cited to Vershynin [37] is reconstructed by Markov optimization: \(\|Z\|_{L^p}\le K\sqrt p\) and (p\asymp r^2/K^2\) give \(\mathbb P(|Z|>r)\le Ce^{-cr^2/K^2}\); integration gives the converse moment bound. The bounded-displacement full-support argument above replaces the paper's sphere-homotopy appeal, except for standard finite-dimensional Brouwer. Universal approximation is an explicit hypothesis in the optimization results, so no external universal-approximation theorem was silently substituted. Literature comparisons in Section 9 were read but not used as evidence of priority or validity.

## Surviving claims relevant to finite retained-state comparisons

- A quantitatively controlled, initialization-coupled finite-horizon nonlinear mean-field approximation exists for the stated all-layer averaging and rescaled training regime; it is not merely a static representation theorem.
- Independent edge initialization is genuinely treated through an auxiliary finite-(M) embedding, with demonstrated interior degeneracy under specific conditions. Correlated initialization supports a richer continuum.
- The retained state in the general theorem is a collection of functions over neuronal probability spaces. A finite tuple of initial arguments per particle is not the same as finitely many scalar coordinates for the whole evolving model; Appendix D explicitly retains functions and integrals of those arguments.
- The paper supplies no root-width Gaussian seed fluctuation process or finite-state autonomous seedwise closure. This conclusion follows from its explicit retained variables, coupling metric, and rates, not from a search failing to find a slogan.
- Finite-time approximation must not be promoted to a fitted-endpoint certificate. Two-layer conditional global optimality has a reconstructable mechanism; arbitrary-depth endpoint statements require the stated rich initialization and convergence assumptions, and the coupling/proof qualifications above remain material.

Review process: the required paper-review/severity, rigorous-mathematics, and canonical-neural-notation skills were applied. They motivated separating exact counterexamples to intermediate inequalities from unresolved theorem truth, and preserving the source's depth/scaling conventions rather than silently translating to another wide-network regime.
