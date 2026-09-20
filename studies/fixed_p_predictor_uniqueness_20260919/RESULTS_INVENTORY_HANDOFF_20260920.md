# Historical results inventory — paused 2026-09-20

This is the exact 39-item accounting delivered in this task before the pause. It is a historical index to source proofs, not a fresh proof audit or a promotion to established material. The original studies and their recorded reviews remain authoritative. Do not use this cross-study inventory to import unpromoted mathematics into another study; preserve the study boundaries in AGENTS.md. See [HANDOFF.md](HANDOFF.md) for continuation instructions, model contract, study map and research vision.

Source: current task 01a0bfa3-a35f-7352-b845-3d7063d02a73, inherited completed turn 01a0bb3a-fa48-7f01-baea-81fce828b51c. No later developments from the parent task are included.

---

Here is the **previous 26-item accounting, followed by the results added since**. I’ve retained the distinctions between the original gradient flow, modified optimizers, landscape statements, and counterexamples.

These are **internally checked research results**, not yet promoted to the established book. Throughout, “compatible” means identical inputs have equal labels and antipodal inputs have opposite labels. Unless specified otherwise, labels are \(\pm1\), weights are positive and sum to one, and loss is the unhalved weighted square loss.

1. **No suboptimal local minima at \(p=1,2,3\), for arbitrarily many inputs.**

   For every compatible finite weighted dataset on the circle, every local minimum of the canonical population loss has \(L=0\). No linear independence, separation, balance, or matrix-rank assumption is required. Locality uses the physical population \(L^2/L^2/\)Frobenius norm.

   The separate \(p=1\) theorem also covers normalized sphere inputs in arbitrary \(d\ge2\), within the canonical odd-state space. [Circle theorem](/home/amir/Codes/PDE/studies/fixed_p_population_landscape_20260919/p2_p3_unrestricted_theorem.md:14), [sphere theorem](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/no_bad_local_minima.md:323).

2. **A no-suboptimal-local-minimum theorem for every fixed \(p\).**

   For arbitrary fixed \(p\ge1\), the conclusion holds when
   \[
   m\le\binom{p+2}{2},
   \]
   where \(m\) counts input directions modulo sign. Item 1 removes this restriction at \(p=1,2,3\); removing it at all higher orders remains open. [Theorem](/home/amir/Codes/PDE/studies/fixed_p_population_landscape_20260919/finite_sample_theorem.md:10).

3. **Exact representability and the architectural loss floor.**

   Compatible finite datasets admit finite-norm zero-loss states. For incompatible data, the architectural floor is the weighted variance of signed labels within duplicate/antipodal groups. Under the applicable landscape theorems, every local minimum attains that floor.

   At \(p=1\), compatible data can already be fitted by changing only the readout of the initialized hidden representation. This is representability, not a statement about the training trajectory. [Loss floor](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/no_bad_local_minima.md:329), [initialized interpolation](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/dependent_finite_fitting.md:49).

4. **Three-input negative curvature without linear independence.**

   At \(p=1\), for three inputs with no parallel or antiparallel pair, every equilibrium with
   \[
   0<L<1
   \]
   has a negative second-variation direction.

   Equal weights give a Hilbert Hessian with a negative eigenvalue and the corresponding basin theorem. Arbitrary weights retain directional negative curvature, with a regularity qualification for certain exceptional configurations. [Result](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/DEPENDENT_BASIN_RESULTS.md:239).

5. **Strict saddles for arbitrary linearly independent input lists.**

   For any finite linearly independent input list with positive weights, the \(p=1\) strict-saddle and null-basin argument applies throughout \(0<L<1\), without assuming bounded endpoint fields. [Theorem](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/INPUT_CONDITION_RESULTS.md:321).

6. **A quantitative instability threshold allowing linear dependence.**

   For \(n\) equally weighted inputs, if every subset of at most \(r\) inputs is linearly independent, \(2\le r<n\), every equilibrium with
   \[
   0<L<\frac{4r}{n(r+1)}
   \]
   has the required negative curvature and null point-convergence basin.

   Pairwise nonparallel inputs give the threshold \(8/(3n)\). [Theorem](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/INPUT_CONDITION_RESULTS.md:251).

7. **Precisely defined bad basins are null.**

   Under those basin-theorem hypotheses, states converging strongly to bad equilibria lie in a countable union of Lipschitz hypersurfaces. They are meagre and null under the constructed full-support Gaussian perturbation laws, including translations and positive rescalings.

   This concerns **point-convergent trajectories**. It does not prove convergence of every trajectory or assign randomness to the deterministic canonical population initialization. [Precise statement](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/INPUT_CONDITION_RESULTS.md:68).

8. **The zero-loss set has an open attracting region.**

   For every finite compatible dataset in the \(p=1\) sphere setting, a nonempty open region of states has exponential loss decay, finite remaining state travel, and convergence to fitted endpoints.

   This region has positive probability under the stated full-support laws. Different starting states can converge to different interpolants. [Theorem](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/DEPENDENT_BASIN_RESULTS.md:391).

9. **Canonical initialization always starts learning on compatible circle data.**

   For \(p=1,2\), with arbitrary finite sample count,
   \[
   L(0)=1,\qquad L'(0)<0,\qquad L(t)<1\quad(t>0).
   \]
   Therefore loss-one equilibria and zero training predictions cannot be limiting states of that trajectory. [Proof](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/INITIAL_REVIEW.md).

10. **Original gradient flow fits several substantial initialized data families exponentially.**

    The \(p=1\) families include antipodal pairs at every orientation; equal-weight opposite-label pairs related by coordinate or diagonal reflections, covering every separation angle; arbitrary orientations with sufficiently small label amplitude; genuine three-input cyclic families in three dimensions; and open neighborhoods of selected reference configurations.

    These results include full-state convergence. **Every arbitrarily oriented unit-label pair, and every compatible triple, are not covered.** [Pairs](/home/amir/Codes/PDE/studies/closure_lyapunov_p1_20260916/all_angles_result.md), [cyclic triples](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/cyclic_uniformity.md), [open families](/home/amir/Codes/PDE/studies/closure_lyapunov_p1_20260916/resolution_synthesis.md).

11. **A geometric potential protects useful hidden contrast.**

    On the proved scalar-residual families, signed prediction per readout norm improves, preventing useful upper-layer contrast from collapsing. With initialized squared contrast \(C_0>0\),
    \[
    L(t)\le L(0)e^{-4C_0t}.
    \]
    The fitted endpoint has strictly greater hidden contrast than initialization, and remaining physical travel is controlled by \(\sqrt{L/C_0}\). Individual pairwise distances need not move monotonically. [Potential](/home/amir/Codes/PDE/studies/closure_lyapunov_p1_20260916/all_angles_result.md:35).

12. **First-layer and backward geometry can compensate for upper-feature collapse.**

    We constructed fitted states with upper-feature Gram rank one but full three-output tangent-map rank three. First-layer variations and forward–backward coupling provide the missing directions.

    Thus a singular upper-feature Gram alone does not establish a learning obstruction. [Construction](/home/amir/Codes/PDE/studies/p1_three_input_geometry_20260918/result.md:230).

13. **Rigorous input perturbations and corrections to potentials.**

    We derived first- and second-order input responses of the complete flow, including sphere curvature and both hidden layers. Current-state cubic and quartic corrections cancel successive moving-metric defects, leaving a quintic residual.

    These give local exponential certificates near regular fitted states; they do not establish a global potential for arbitrary initialized data. [Results](/home/amir/Codes/PDE/studies/closure_lyapunov_p1_20260916/correction_synthesis.md).

14. **Necessary-and-sufficient asymptotic slow-onset classification for weighted triples.**

    Along sequences of configurations, vanishing initial slope, vanishing learning on every fixed horizon, diverging fixed-drop hitting times, and approach to the characterized signed-cancellation locus are equivalent.

    Equal thirds have uniformly positive initial progress over all geometries. A balanced family nevertheless has initial slope of order \(\varepsilon^4\) and fixed-drop time at least order \(\varepsilon^{-2}\), forcing very large initial values for any uniform-rate, loss-controlling exponential potential. [Classification](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/WEIGHTED_THREE_INPUT_RESULTS.md:57), [delay bound](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/MAIN_RESULTS.md:64).

15. **A canonical trajectory genuinely decreases to a positive architectural floor.**

    The weighted triple
    \[
    (\sqrt3e_1,+1),\quad(-\sqrt3e_1,+1),\quad(\sqrt3e_2,-1),
    \qquad \mu=(1/4,1/4,1/2)
    \]
    decreases from loss one to \(1/2\), with exponential decay of excess loss and movement in both hidden blocks.

    Its floor comes from incompatible same-label antipodes. [Theorem](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/WEIGHTED_THREE_INPUT_RESULTS.md:220).

16. **Stationary-loss gaps and restrictions on plateaus.**

    For finite binary-label \(p=1\) data, every equilibrium satisfies
    \[
    L=0\quad\text{or}\quad L\ge\mu_{\min}.
    \]
    Thus state convergence after reaching \(L<\mu_{\min}\) guarantees fitting.

    For triples, bounded returns of the readout and middle-matrix norms restrict positive limiting loss to a finite signed-partition list; otherwise their combined norm must diverge. [Gap](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/finite_critical_loss_gap.md), [plateau restrictions](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/PLATEAU_CLASSIFICATION.md:187).

17. **Bad equilibria need not have negative quadratic curvature—or cubic descent.**

    Seven nonparallel inputs admit a loss-\(48/49\) equilibrium with positive-semidefinite Hessian and cubic descent. Some noncanonical trajectories converge to that loss. Related equilibria persist under open sets of input perturbations.

    Other examples have no cubic term but admit quartic or quintic descent. These disprove universal strict-saddle arguments, not canonical convergence or nullity of all bad basins. [Construction](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/FINITE_BASIN_EXTENSION.md), [perturbations](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/INPUT_PERTURBATION_RESULTS.md), [higher orders](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/cubic_and_higher_descent.md).

18. **Fixed-direction Taylor tests can miss nearby descent entirely.**

    A compatible \(p=1\) example has positive quadratic leading behavior along every nonflat fixed direction and exactly flat remaining directions, yet lower-loss states exist arbitrarily nearby in the physical norm.

    Its directional quadratic form is not a Fréchet Hessian. [Counterexample](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/straight_line_geometry_attempt.md).

19. **Saturation at infinity obstructs uniform progress.**

    At \(p=1,2,3\), compatible three-input data admit states with
    \[
    L(S_R)\to\frac34,\qquad
    \|\nabla L(S_R)\|\to0,\qquad
    \|w_R\|\to\infty,
    \]
    while readout and middle-matrix norms remain bounded. Fixed-radius perturbations and fixed proposal laws yield vanishing improvement.

    This is a state sequence, not a proved canonically reached trajectory. [Construction](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NOISE_CLOSURE_ROUTE.md).

20. **Actual minibatch SGD has a local fitting theorem for general compatible data.**

    In the \(p=1\) sphere setting, explicit open starting regions and step-size bounds give convergence to a finite fitted state with probability at least \(1-\delta\), with geometric conditional expected-loss decay. Every fixed batch size is covered, including three.

    Entry from canonical initialization remains unproved. [Theorem](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/local_minibatch_fitting.md).

21. **Minibatch noise does not automatically escape bad states.**

    Some bad equilibria have every individual sample gradient equal to zero, even though higher-order descent directions exist. Every minibatch leaves them fixed.

    Conversely, a finite limit of constant-step iid SGD must be stationary for every sample. Batch size three does not automatically supply missing escape directions. [Results](/home/amir/Codes/PDE/studies/p1_stochastic_escape_20260918/sgd_geometry.md).

22. **Persistent accepted perturbations exclude nonminimum accumulation points.**

    For independent Gaussian proposals conditioned to a fixed-radius ball, accepting only loss decreases, almost surely no non-local-minimum state is an accumulation point at proposal times.

    This handles the whole potentially uncountable set, but does not prove an accumulation point exists. [Theorem](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/ESCAPE_AND_LIMITS.md).

23. **Accepting every improving full-support proposal gives fitting or norm escape.**

    For \(p=1,2,3\) and compatible finite circle data,
    \[
    L_\infty>0\Longrightarrow\|S_k\|_{\mathcal H}\to\infty
    \quad\text{almost surely}.
    \]
    Infinitely many returns to a bounded region therefore suffice for fitting. [Theorem](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NOISE_GLOBAL_PROGRESS.md:180).

24. **Fractional acceptance gives unconditional almost-sure fitting.**

    Hold the state during unsuccessful trials and accept only a fixed fractional reduction:
    \[
    L_J\le\vartheta^J L_0,\qquad L(t)\to0\quad\text{almost surely},
    \qquad 0<\vartheta<1.
    \]
    This works at \(p=1,2,3\) without boundedness, recurrence, or parameter-convergence assumptions. Every positive accuracy is reached in finite algorithm time almost surely.

    The geometric bound counts successful stages. Later quantitative refinements are recorded below. [Theorem](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NOISE_GLOBAL_PROGRESS.md:236).

25. **An exact Gaussian/kernel reformulation of initialized \(p=1\).**

    We obtained explicit data-independent \(M(0)\), an exact active \(2\times4\) matrix reduction, fixed four- and two-dimensional Gaussian carriers, and an autonomous functional representation preserving the physical metric and both hidden layers.

    Every finite initialization time jet is a finite Gaussian computation, with a positive local analytic radius. The evolving state remains functional, not finitely many scalar moments. [Reformulation](/home/amir/Codes/PDE/studies/closure_gaussian_reduction_p1_20260917/exact_reduction.md).

26. **The separate scalar-dictionary closure has genuine learning and genuine failures.**

    Scalar dictionaries permit feature learning. A reflected opposite-label pair has an exponentially decaying geometric potential and full-state convergence.

    But compatible, representable triples can stall at initialization; others move while retaining loss at least \(1/2\) forever. These are failures of the compressed model, not the canonical \(p=1\) closure. [Positive result](/home/amir/Codes/PDE/studies/scalar_density_potential_20260917/potential.md), [moving failure](/home/amir/Codes/PDE/studies/scalar_density_potential_20260917/rotation_obstruction.md).

The following results were added after that inventory.

27. **Quantitative guarantees for several accepted-noise variants.**

    For the original fixed-Gaussian fractional-acceptance rule, we obtained explicit finite high-probability hitting-time bounds. Unconditional expected hitting time remains unproved for that rule.

    Other constructions give polynomial expected-loss decay through occasional global refreshes, or exponential decay through prediction-isotropic readout proposals and auxiliary fixed-feature searches. Their tradeoffs include global replacements, Gram inverses, or potentially large physical movements. [Rate-results accounting](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/RATE_RESULTS.md).

28. **Small current-feature readout noise gives exponential expected loss in a specified elapsed clock.**

    For \(p=1,2\) and every compatible finite circle dataset, propose readout changes proportional to
    \[
    \sqrt L\sum_i\sqrt{\mu_i}\,G_iH_i,
    \]
    accept sufficient fractional improvements, then run full gradient flow for a fixed short duration \(h\).

    The initial Gram and the schedule give proved constants \(\gamma,\lambda>0\) with
    \[
    \mathbb E L_k\le L_0e^{-\gamma k},
    \qquad
    \mathbb E L(t)\le e^\gamma L_0e^{-\lambda t}.
    \]
    Here \(k\) counts all proposals, including rejections; assigning each proposal duration \(\Delta\) gives \(\lambda=\gamma/(\Delta+h)\).

    The state converges strongly to a fitted endpoint almost surely. The proof deliberately controls total hidden movement, and \(\Delta\) is an algorithmic clock—not a computational-runtime theorem. [Proof](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/RATE_SMALL_READOUT_NOISE.md).

29. **A continuous conditioning-corrected flow gives pathwise exponential fitting.**

    For \(p=1,2\), define the current weighted upper-feature Gram \(K\) and
    \[
    R=\operatorname{tr}K^{-1},\qquad
    \Phi_\varepsilon=L(1+\varepsilon R).
    \]
    Descending this potential, with an explicit readout safeguard and tangent readout noise, gives
    \[
    L(t)\le L_0e^{-4\varepsilon t},
    \qquad
    \Phi_\varepsilon(t)\le\Phi_\varepsilon(0)e^{-4\varepsilon t}.
    \]

    All layers evolve continuously. Every allowed noise realization has finite total state travel and a finite fitted endpoint. No acceptance phases are needed. The deterministic correction supplies the convergence guarantee; noise preserves it.

    The correction can become large near singular feature geometry. [Complete result](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NATURAL_NEAR_GF_RESULTS.md), [potential proof](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NATURAL_CONDITIONING_FLOW.md).

30. **The corrected flow approaches ordinary GF on finite horizons.**

    With immediate activation, the deviation is \(O(\varepsilon)\) on fixed intervals where ordinary GF stays bounded and its feature Gram remains uniformly positive definite.

    With an independent exponential activation time of mean \(1/\varepsilon\), the modified process agrees exactly with GF on \([0,T]\) with probability at least \(e^{-\varepsilon T}\), while
    \[
    \mathbb E L(t)\le\frac43L_0e^{-\varepsilon t}.
    \]
    Thus finite-horizon approximation and unconditional eventual fitting coexist, although the guaranteed rate weakens as \(\varepsilon\to0\). [Theorem](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NATURAL_NEAR_GF_RESULTS.md).

31. **A fixed exponential rate is possible with a logarithmic startup cost.**

    Delaying a fixed-strength correction until approximately \(\lambda^{-1}\log(1/\varepsilon)\) gives
    \[
    \mathbb E L(t)\le
    L_0\min\!\left\{1,\frac{e-1}{\varepsilon}e^{-\lambda t}\right\}.
    \]
    The exponent stays fixed while the startup cost diverges logarithmically. A timer-augmented potential satisfies an exact exponential inequality.

    We also proved the limiting implication: a GF-approximating family with **both uniformly bounded prefactor and uniformly positive rate** would itself prove the corresponding exponential theorem for ordinary GF. We have not established that stronger bound. [Results](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NONVANISHING_RATE_RESULTS.md), [timer potential](/home/amir/Codes/PDE/studies/fixed_p_population_basins_20260919/NONVANISHING_CLOCK_POTENTIAL.md).

32. **Exact initialized features reveal unrestricted freedom at unseen inputs.**

    The newer canonical \(p=1\) Gaussian calculation proves initial upper-feature independence for every finite circle set distinct modulo antipodes.

    Consequently, even with hidden layers fixed at initialization, bounded readouts can fit all training labels and assign **any prescribed real value** at an additional input outside those antipodal classes. Training labels alone therefore do not determine a unique predictor. This is representability, not canonical reachability. [Proof](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/CANONICAL_FEATURES.md).

33. **Physical state convergence controls predictions everywhere.**

    Strong state convergence yields predictor convergence uniformly on the circle and locally uniformly on \(\mathbb R^2\), through explicit estimates. Finite physical travel suffices for a state endpoint.

    However, convergence along each separate run does not imply agreement between runs. Evaluating more passive inputs or using a mesh cannot replace a selection theorem. [Results](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/PASSIVE_LIMITS.md).

34. **A noisy optimizer selects one fitted state and one function for every compatible circle dataset.**

    At \(p=1\), let \(h=(w,M)\), and define
    \[
    J(h)=\frac12\min_{c:\,f_{h,c}(x_i)=y_i}\|c\|_{L^2}^2,
    \qquad
    F(h)=J(h)+\frac\rho2\|h-h_0\|^2.
    \]
    For an explicit sufficiently large \(\rho\), \(F\) has a unique minimizer \(h_*\) in a certified neighborhood.

    The constructed noisy flow, including exact transport for changing features, has potential
    \[
    \Phi=F(h)-F(h_*)+L+\|q\|^2,
    \]
    where \(q\) is the readout component invisible to current training features. It satisfies exponential decay and controls physical distance to one selected state.

    **Every allowed noise realization converges exponentially to the same state and whole-input predictor.** The price is strong anchoring and a modified optimizer. [Theorem](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/UNIQUE_NOISY_SELECTOR.md).

35. **A simpler projected optimizer retains fitting and common-function convergence.**

    Using your preferred notation,
    \[
    \theta=\bigl(\sqrt\rho(w-g),\sqrt\rho(M-D),c\bigr),
    \]
    let \(e\) be the weighted residual, \(T_\theta=De\), and
    \[
    P_\theta=I-T_\theta^*(T_\theta T_\theta^*)^{-1}T_\theta.
    \]
    The rule is
    \[
    \dot\theta
    =-2T_\theta^*e-\epsilon P_\theta\theta
      +\eta\sqrt L\,P_\theta U_t.
    \]

    For every compatible finite circle dataset at \(p=1\), explicit parameter choices prove
    \[
    L(t)\le L_0e^{-2\sigma t},
    \qquad
    \|\theta(t)-\theta_*\|
       \le\|\theta_*\|e^{-\epsilon t/2},
    \]
    where \(\sigma=\lambda_{\min}(K_0)>0\). The potential
    \[
    \Psi=\tfrac12\|\theta-\theta_*\|^2
    \]
    satisfies \(\dot\Psi\le-\epsilon\Psi-L\) and controls loss.

    The same deterministic endpoint is reached for every allowed noise realization. The rule eliminates explicit readout transport and evaluation of \(\nabla J\). It still requires a full-Jacobian Gram inverse and potentially very slow hidden learning relative to readout learning. [Proof](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/PROJECTED_SELECTOR_LEAD.md).

36. **The selected optimizers permit genuine movement in both hidden blocks.**

    For the canonical coordinate-input pair, every binary label pair and every positive mass pair give nonzero initialized derivatives in both \(w\) and \(M\) of the selection objective. This persists in an open neighborhood of nonorthogonal configurations.

    Thus the construction permits actual learned hidden geometry. Nontrivial movement for every possible finite dataset, or large hidden movement, is not asserted. [Proof](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/HIDDEN_MOVEMENT.md).

37. **Ordinary physical-gradient alternatives also give unique fitted predictors.**

    Adding a strong hidden anchor and a fixed penalty on the initialized readout nullspace gives a physical-gradient flow with tangent noise, exponential fitting, and one common endpoint. Its hidden endpoint returns to initialization, selecting the initial-feature kernel predictor.

    Adding \(J(h)\) permits learned terminal geometry with the same guarantees, but requires its gradient. These objectives decrease; loss alone need not be monotone in the learned variant. [Both constructions](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/NATURAL_PENALTY_ROUTE.md).

38. **Arbitrarily small, eventually vanishing noise can still produce different limiting functions.**

    We constructed an exact canonical-start \(p=1\) example where full coupled training fits exponentially and the state converges, but readout noise leaves a random prediction at an unseen orthogonal input.

    The perturbation can be uniformly arbitrarily small and vanish completely after time one. Both Brownian and bounded random-ODE versions are proved.

    Therefore smallness, disappearance of noise, exponential fitting, and state convergence do **not** by themselves establish a common predictor. This does not rule out carefully designed selectors such as items 34–35. [Counterexample](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/NATURAL_NOISE_OBSTRUCTIONS.md:52).

39. **Simple selection mechanisms have precise limitations.**

    Constant isotropic readout weight decay biases fitting. In an explicit linear model, nonnegative time-dependent isotropic decay cannot both erase arbitrary readout-nullspace memory and retain an exponential zero-loss tail.

    A hidden anchor alone leaves readout ambiguity, while a random clock only reparameterizes ordinary GF. These are scoped obstructions explaining why prediction-preserving selection is useful—not a universal impossibility theorem for simpler optimizers. [Proofs](/home/amir/Codes/PDE/studies/fixed_p_predictor_uniqueness_20260919/NATURAL_NOISE_OBSTRUCTIONS.md:400).

The **numerical evidence remains separate**: two width-1024 networks fitted the seven-input example below \(10^{-6}\), with a tighter replay checked. This does not prove population-closure or infinite-time convergence. [Experiment](/home/amir/Codes/PDE/studies/p1_sphere_extremes_20260918/WIDE_NETWORK_GF_RESULTS.md).

The main unresolved claims remain: universal fitting from canonical initialization under **ordinary GF or SGD**; universal nullity of positive-loss basins; unrestricted landscape results for every higher fixed \(p\); and transferring the designed continuous-population guarantees to finite-width, finite-step algorithms. The new uniqueness theorems concern their explicitly selected optimizers, whose limiting function depends on the declared selection rule.

