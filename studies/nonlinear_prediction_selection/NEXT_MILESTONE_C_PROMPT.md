# New task: an independent computable approximation of population feature learning

Work in `/home/amir/Codes/PDE`, the single checkout shared by PDE and PDE-2.
Start a new study, `studies/population_flow_computation/`, for milestone C;
check directory ownership first if that name exists. Read `AGENTS.md`, the
research workflow, `docs/README.md` including the philosophy and roadmap,
`docs/NOTATION.md`, and `code/README.md`. Use `solve-math-rigorously` and
`investigate-conjectures`, reading their required instructions yourself.
Research inputs are this study and established book/code only. Do not read
milestone B's study or other tasks. Keep source, configurations and review
records flat inside this study, and generated products under
`data/generated/population_flow_computation/`.

**Problem.** Construct, prove and implement a numerically manageable finite
causal system that converges to the same nonlinear population gradient flow
as the canonical network, without evolving its raw neural parameters. The
purpose is to compute its whole-circle predictions and retained hidden
learning independently, and enable controlled exploration beyond conservative
theorem bounds. A different mathematical representation with a usable solver
is required; a formal closure or existence theorem alone is insufficient.

Retain exactly C.4.7's bias-free two-hidden-layer tanh model on
`sqrt(2) S^1`, independent Gaussian stored variances `(1,1/n,1/n^2)`,
mobilities `(n,1,n)`, output division by `n`, unhalved squared loss, and
physical GF. Its population state starts at `(w,K,c)=(g,0,0)`, with
`g ~ N(0,I_2)`, and retains the initialized Gaussian action `A_0`, its
actual adjoint and learned increment `K`. Zero population readout is the
proved limit of the actual small finite Gaussian readout, not permission
to replace finite initialization. Every run uses its fixed training law.

The first certified target is the original physical flow on `[0,40]`.
Choose and freeze an explicitly computable, nontrivial family of laws on
`sqrt(2) S^1 x [-Y,Y]`, for a fixed `Y >= 1`, inside C.4.7's neighborhood
of
\[
 \nu_* = \tfrac12\delta_{(\sqrt2e_1,+1)}
          +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]
Include genuinely nonatomic, correlated input laws with a finite description
and controlled data quadrature. The family must be fixed independently of
requested accuracy; it cannot collapse to the reference as accuracy improves.
Prove an effective sufficient admission condition or checkable certificate.
An instance-dependent theorem is acceptable; arbitrary Borel inputs and
uniformly practical accuracy for every tiny perturbation are not required.

Digest C.4.7 and C.4.9 completely, with their necessary complete established
dependencies and observation contracts. Inspect the relevant complete
integrated-query results in `docs/gaussian_calculus.md` and §13 of
`docs/finite_optimization_and_controls.md` before reusing their arguments.
Their three-hidden-layer arctan, feature-clock or clipped conclusions do not
automatically apply to this model.

Milestone A, now C.4.9, supplies Gaussian source-tail and temporal estimates
controlled by accumulated forcing, and nonlinear selection on a slow clock.
It retains the full source history: it proves neither economical compression
nor cheap Gaussian integration. Its projected slow equation still contains
the full initialized action and adjoint. Use these facts where helpful;
no particular representation or proof route is prescribed.

Resolve these connected obligations:

1. **Actual finite construction.** Specify all state variables, initialization,
   coefficients, updates and prediction reconstruction. One physical evolution
   time is required; causal integral memory and finite saved history are allowed
   if included in the state and cost. ODE, PDE, integro-differential or other
   autonomous causal representations are admissible. Reached restart must
   continue from the saved finite state, including numerical random state when
   used, without replaying an unavailable trajectory or resetting Gaussian reuse.

2. **Identification and quantitative accuracy.** For each admitted fixed law
   `mu`, requested error `a > 0`, and failure probability `b > 0` if randomized,
   give a computable refinement/resource rule ensuring
   \[
   \Pr\!\left\{\sup_{0\le t\le40,\,x\in\sqrt2S^1}
      |\widehat f_\mu(t,x)-f_\mu(t,x)|>a\right\}\le b,
   \]
   or a deterministic bound. Randomness here belongs to numerical approximation;
   identify the limit with the established population GF. Also fix and prove an
   internal-observation contract covering both hidden layers, paired
   initialized/current hidden moments, and the forward/backward response
   information needed by the evolution and restart. State metrics and requested
   tolerances for the named joint fields and moments; matching their separate
   marginals alone does not establish Gaussian reuse. Use correctly typed
   observables; do not demand or assume an operator-norm coupling of unlike
   state spaces. Convergence must refine the actual solver, not merely hold
   for each fixed formal program or supplied exact trajectory.

3. **Numerical substance.** Derive all Gaussian action/reuse and response
   quantities from the finite system's own available information. Bound both
   the error it generates and its propagation: data quadrature, numerical
   integration/sampling, omitted state or memory, time stepping and precision.
   Justify required tail or conditioning controls along the generated states.
   Account for total state size, field dimensions, all histories, contractions,
   covariance solves, time steps and precision, independently of neural width.
   Evaluate the bound on a meaningful certified case at a stated useful
   accuracy and feasible resource budget. Distinguish practical approximation
   of a nonlinear learned trajectory from resolving a much smaller changed-law
   effect. An unquantified finite or astronomical construction is partial progress.

4. **Reusable implementation and exploration.** Implement a compact method
   with explicit inputs, restart, tolerances, diagnostics and reproduction
   commands. Necessary bounded solver execution and deterministic validation
   of identities, Gaussian reuse, refinement and restart are authorized by this
   task; record the validation budget before execution. Keep the same equations usable
   for broader law perturbations, correlations and longer physical times wherever
   they remain defined. Prepare a bounded validation protocol separating time,
   state/history, quadrature and precision errors, and independent finite-network
   comparisons. Outside the proved regime, results must remain exploratory;
   stable plots do not prove population existence or generalization. Finite-network
   training experiments and broad sweeps require separate authorization. Do not extend
   depth or activation merely because the interface accepts an argument.

No raw trainable all-to-all hidden matrix, neural training under a new name,
fitted closure, target-trajectory oracle, unevaluated Gaussian expectation,
or hidden high-dimensional quadrature qualifies. Statistical representatives
of a derived population process and finite covariance/response matrices can
qualify if their correlations, closure errors and full costs are justified.
The requirement is computational independence, not a ban on every matrix or
sampling method. Data quadrature is legitimate; training a dense network on
that quadrature law is still the existing simulation route.

A's longer episode at `t=tau/epsilon` is optional future scope. Solving only
its projected singular limit does not resolve this fixed-law GF target.
Any acceleration using it must account for construction of the reference
endpoint, the initial layer and finite-`epsilon` approximation error. Do not
make that additional bridge, all-time training, generalization or architectural
superiority mandatory for the first C result.

Work toward complete resolution with genuinely diverse approaches. Use fresh
`fork_turns="none"` agents and explicit scientific input scopes; give some
creative attempts only a self-contained problem or selected established
material, and keep routes separate until frozen for comparison. Check the
candidate's causal information and resource requirements early, before building
a large implementation. If a route stalls, distinguish a missing generated-error
estimate from a propagation problem and try a structurally different route.
Follow the roadmap's GF/GD reassessment only for a persistent named obstacle
with a concrete demonstrated advantage; changing the time model alone does
not resolve hidden-state computation.

Preserve concurrent work, coordinate the common Git writer lock, and make
scoped study commits. Successful completion requires a complete proof, reusable
implementation and validation, followed by independent relevance screening,
two fresh complete isolated scientific/code reviews and separate integration
review. Prepare the smallest self-contained canonical addition and request
user approval before established files change. If a genuine gap survives,
record precisely what is established and missing; a conditional closure or
documented deferral does not complete C.
