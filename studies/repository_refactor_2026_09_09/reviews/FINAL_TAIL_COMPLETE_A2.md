# Independent complete mathematical audit

**Separate verdicts**

| Candidate | Verdict |
|---|---|
| **LAST A–I** | **Pass within the explicitly stated scopes.** No required mathematical correction found. |
| **SCOPE A–E** | **Pass within the explicitly stated scopes.** Conditional implications and formal coefficients remain conditional and formal, respectively. |
| **IDENTITY §§1–8** | **Pass.** The fixed-program width limits, uniform step-doubling estimate, local operator flow, and separate activation-stability obstruction are justified. |

I checked all five scientific files, including every proof in the dependency packet. These verdicts do **not** promote conditional constructions to unconditional theorems, initialization coefficients to positive-time results, or ambient-state counterexamples to counterexamples along canonical training.

Below, **DEP**, **LAST**, **SCOPE**, and **IDENTITY** denote the correspondingly named files in this directory. Line references refer to the audited, unchanged inputs.

## 1. Reading, isolation, and verification record

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and every line of these scientific inputs:

| File | Lines |
|---|---:|
| `NOTATION.md` | 98 |
| `FINAL_LAST_ADDITION.md` | 2,229 |
| `FINAL_SCOPE_ADDITION.md` | 1,256 |
| `FINAL_IDENTITY_UNIFORM_ADDITION.md` | 1,032 |
| `FINAL_LAST_R2_DEPENDENCIES.md` | 4,861 |
| **Total** | **9,476** |

Two dependency displays were truncated by the output layer. I resolved them by bounded rereads of **DEP 2036–2136** and **DEP 3411–3435**. No scientific span remained unread.

The only content read outside these five scientific inputs was the explicitly authorized skill and `INPUTS.json`. A directory listing exposed filenames and metadata; I did not read the other listed files. I used no project history, Git, previous review, external scientific source, network, memory lookup, or delegation. I did not access `/home/amir/Codes/PDE`.

Tools were used only for reading, listing, counting, hashing, and bounded exact arithmetic. There were no experiments, simulations, implementation tests, or file writes. This attestation concerns the actual reads and actions in this session, not physical inaccessibility of excluded locations.

## 2. Shared model and complete dependency audit

### 2.1 Notation and finite dynamics

**NOTATION 8–98; DEP 8–213 — correct.**

The normalization contract is internally consistent:

\[
z_a^1=W^1x_a/\sqrt d,\qquad
f_{n,a}=(W^{L+1})^Th_a^L/n,\qquad
\delta_a^\ell=n\,\partial f_{n,a}/\partial z_a^\ell.
\]

The residual is excluded from \(\delta\). With mean-square loss and mobilities
\[
(n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}),
\]
the displayed raw gradients produce exactly DEP (2), including the first-block \(1/\sqrt d\), middle-block \(1/n\), and loss factor \(2/m\).

The kernel blocks follow from the Frobenius identity
\[
\langle uv^T,pq^T\rangle=(u^Tp)(v^Tq).
\]
Their positivity is positivity of gradient Grams, including singular input Grams. Consequently
\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr
=-\|D^{-1/2}\dot\theta\|^2
\]
has the stated normalization.

Finite global existence follows from the energy-controlled Cauchy endpoint and finite-dimensional local Lipschitzness. It does not require bounded activations and does not prove global GD stability.

The width-uniform RMS induction uses precisely bounded activation slopes, bounded initial endpoint RMS norms, bounded connector operator norms, fixed data, and fixed depth. The Gaussian net estimate supplies the stated high-probability initialization event. None of these estimates supplies an \(L^2\) multiplier bound for an unbounded population coordinate.

The alternative storage \(V^1=W^1/\sqrt d\) is consistently accompanied by first-block metric \(d\|\Delta V^1\|_F^2/n\).

### 2.2 Two-sample, three-hidden-layer dependency

**DEP 219–1629 — correct, with the stated equal-label global scope.**

I checked every stage of Parts II.A–II.D.

- **Exact geometry and symmetry, 277–471.** The four raw kernel blocks and summed-loss factor are correct. The first-field metric is \(G^{-1}\) when invertible and the one-field metric at \(\rho=-1\). Finite exchange symmetry is only equality in law. Deterministic population limits justify the label-mode relation; the argument does not assume finite pathwise residual symmetry.
- **Scalar source equations, 473–572.** Learned forward and reverse terms have the correct \(\Delta/2\) coefficients. Reverse responses retain current forward calls. Formal derivatives freeze coefficients and covariances and retain singular source slots.
- **Response induction, 574–789.** The current-row order is noncircular: forward rows are bounded using past queries, then current reverse rows are constructed downward. Both sample correlations remain present. The constants check:
  \[
  V_*=\frac{3067}{3200},\qquad
  Q_*=\frac{24829}{19200},
  \]
  \[
  \frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
  +\frac3{200}Q_*^2
  =\frac{71063018523}{73728000000}<\frac{97}{100}.
  \]
  The upper forward-response margin is
  \[
  \frac32-\frac{49}{36}-\frac3{25}=\frac{17}{900}>0.
  \]
  The exponential-square bound uses a Gaussian source plus a bounded correction; it needs no independence between those two terms.
- **Construction and cap removal, 791–984.** The smaller-cap reference supplies the pointwise readout bound and both query tails. The backward comparison costs \(C(1+R)\), not a product of cap factors. Its \(e^{CR}\) amplification is dominated by \(e^{-R^2/256}\). Completeness gives the strong state limit, and the same estimates identify actual uncut directions and Hilbert–Schmidt increments.
- **Physical clock and uniqueness, 985–1046.** For equal labels,
  \[
  g_s\ge25/36,\qquad s_t=4(1-g).
  \]
  Hence \(s_*\le36/25<3/2\), while bounded \(g_s\) forces the physical-time integral to diverge at \(s_*\). This proves global physical time and the constants \(25/9\), \(50/9\). Physical uniqueness against nonsymmetric competitors is obtained by comparison, without assigning those competitors the symmetric clock.
- **Actual algorithms, 1048–1117.** The reference clock is deterministic and is not asserted to be the finite process’s clock. The full finite residual difference controls the off-mode component. The initial readout discrepancy is \(O_{\mathbb P}(n^{-1})\). Fixed-cap Euler defects, first-exit slack, and the width-then-cap order justify actual GF/GD convergence. The within-step estimate \(\eta_n\sqrt n=n^{-3/2}\) is sufficient.
- **Observations, 1119–1288.** Ordered clipping establishes the unbounded backward and velocity observations. Compact \(L^2\) reference curves supply uniformly removable square tails. The upward velocity comparison introduces one truncation factor multiplying state error. The path interpolation bound
  \[
  \|z-I_\pi z\|_\infty^2\le4|\pi|\int|\dot z|^2
  \]
  supplies the additional path topology and second moments. Increment contractions follow from rank-one cross-time pairings and Riemann approximation.
- **Nonaffinity and motion, 1292–1629.** Independent displacement dominators establish lower-layer separation and unbounded marginal tails; the top correction is bounded. Closed-set passage preserves the needed positive probabilities. Bounded strict monotonicity then rules out affine regression identities. Reverse-source signed quadrants establish positive-definite backward second-moment matrices, including at the antipodal endpoint. Gradient/velocity telescoping and sample exchange prove motion of both samples, not merely one. The initialization calculation separately proves every hidden leading coefficient nonzero. The physical feature coefficient \(8t^2\), readout-mode kernel coefficient \(16\Gamma t^2\), and total-mode coefficient \(32\Gamma t^2\) are consistent.

The broader label identities and feature-flow construction do not by themselves establish global opposite-label physical fitting.

### 2.3 Fixed finite Gaussian programs and common actions

**DEP 1913–2453 — correct.**

This is a proved dependency, not an imported verdict.

The adaptive-conditioning argument conditions successively on each transcript. Given that transcript, a new input is fixed and reveals a linear observation of only the queried matrix. Thus the residual matrix factors retain the conditional product structure needed for subsequent calls.

The conditional mean
\[
Y(V^TV)^{-1}V^T+
U(U^TU)^{-1}Q^TP_{V^\perp}
\]
satisfies both observations and is Frobenius-orthogonal to the homogeneous constraint space. Gaussian projection therefore gives the stated residual law. Removing a finite-rank projection from a fresh Gaussian costs vanishing normalized mean square.

Conditional averaging proves weak convergence and second-moment convergence. The supplied partition-and-tail argument upgrades these to \(\mathcal W_2\).

The source-response formula follows by:

1. projecting the new input off previous same-orientation inputs;
2. using orthogonality to eliminate old return terms;
3. applying Gaussian integration by parts to the opposite source group;
4. canceling derivatives of the same-orientation regression.

This produces **full input second moments** as source covariances. Independent oriented source groups do not mean independent matrix answers.

For singular queries, fresh input noises make limiting query Grams positive definite. Finite-array Lipschitz propagation bounds the perturbation by \(C\varepsilon\). The scalar recursion passes to zero noise through covariance square roots and bounded continuous source derivatives, without continuity of pseudoinverses.

The common-space construction verifies density, well-defined linear action assignments, bounded extensions, and actual adjunction by passing finite transpose pairings. It does not replace initialized matrices by arbitrary bounded operators.

The Hilbert–Schmidt completeness, rank-one identities, strong multiplier lemma, curve chain rule, and scalar Fréchet differentiation arguments are sufficient for their uses. In particular, scalar predictor differentiability does not require Fréchet differentiability of a nonlinear map \(L^2\to L^2\).

### 2.4 Three-sample, every-fixed-depth dependency

**DEP 1635–1911 and 2455–4510 — correct under its explicit activation and data hypotheses.**

The model uses half-summed loss, zero population readout, and the stated raw metric. Hidden-field normalization introduces
\[
f_i=a^LF_i,\qquad \nabla_{\rm raw}f_i=a^L\nabla_{\rm raw}F_i;
\]
it does not rescale stored readout, metric, or actual GD step.

The controlled estimates in III.S retain the actual coefficient arrays. Independent primal estimates precede the source induction. The Gaussian-part elimination includes the affine offset, and its \(1/K_\ell\) scale compensates for the possible curvature factor \(K_\ell\). The local Jacobian recursion retains the current reverse return while the forward memory remains strictly causal.

The explicit coefficient boxes dominate both forward and reverse production. Their depth-dependent sizes are absorbed by the single gain condition \(a\ge10^{12}(1+T_0)\); no uniform bound on growing transcript length or \(L=L(n)\) is inferred.

The geometric proof
\[
G+\mathbf1\mathbf1^T\succeq\delta^2I/4
\]
is valid for the three distinct normalized inputs under the one-sided separation assumption. Gaussian constant/linear projections yield a summable loss of normalized Gram margin with depth. The controlled displacement and hidden predictor/update bounds give
\[
Q_L\succeq3\lambda I/4,\qquad \|J_hU_{h,R}\|<\lambda/4.
\]
The capped hidden term need not be symmetric; its absolute norm bound is sufficient for residual decay.

The accumulated control time satisfies
\[
v(t)=a^L\int_0^t\|r\|_1\le\frac6{\lambda a^L}=S/2.
\]
This closes the continuation argument and transfers controlled source moments to capped physical paths without sampling arbitrary measurable controls at Euler nodes.

Part III.V supplies the missing bridges explicitly:

- strong cap removal and comparison against competitors using reference tails only;
- finite primal events before response-probe estimates;
- fixed-cap expected derivative rows and pointwise source bounds;
- derivative-valid nested clipping for ascending velocity queries;
- separate descending closure for true backward observations;
- width, mesh, training-cap, and observation-tail limits in the stated order;
- actual raw GD directions at preceding nodes;
- uniform kernel entries, velocity laws, integrated speeds, path laws, and fixed generated probes.

The regression estimate
\[
|\sqrt{\mathcal R_\psi(X)}-\sqrt{\mathcal R_\psi(Y)}|
\le2\|X-Y\|_2
\]
correctly uses the optimal slope bound \(|c_X|\le1\). The finite-interval Gaussian density bound and gain arithmetic prove the asserted positive margin.

Part III.N independently establishes initial motion: positive forward Grams, positive backward Grams, nonzero raw blocks, and a fresh forward innovation for every upper sample. The coherent clipping schedule justifies the unbounded source products. For half-summed loss and \(p=y/3\), the accelerations are \(9\mathscr V\), \(9U\), \(9T\), and the kernel coefficient is \(18\|\mathscr V\|^2\).

The activation-class refinements are also justified:

- a common interval margin gives a common gain;
- compactly supported perturbations disprove a positive margin uniform over all depths for the broad class;
- distinct tail limits give a positive Gaussian regression floor over \(\sigma\ge1\);
- the \(C_b^2\) ball about \(\frac14\arctan\) inherits that floor;
- disjoint translates give infinitely many independent perturbation directions.

These statements do not assert uniform finite-width convergence over that infinite function class.

### 2.5 Trace class and Gaussian words

**DEP 4514–4861 — correct.**

The trace-space proof establishes the singular expansion, approximation-number formula, partial singular-value variational formula, triangle inequality, completeness, ideal bounds, basis-independent trace, cyclicity, and Hilbert–Schmidt comparison. The finite-rank Gram formula handles singular Grams through partial isometries. The trace-tail inequality controls the entire tail.

The Gaussian-word proof supplies Wick’s formula internally. A paired trace word contributes \(n^{v-k-1}\); only tree quotients survive. Leaf removal identifies these with noncrossing, same-label, opposite-transpose pairings. The creation/annihilation calculation gives the same vacuum moments.

For trace variance, pairings joining the two walks give connected quotients and \(O(n^{-1})\) contributions. Conditional Gaussian quadratic/bilinear forms then identify rooted words. Two full orthogonal rooted sectors, not merely two orthogonal initial vectors, are correctly used.

The mention of `gaussian_calculus.md` is not an operative dependency: Wick’s identity is already derived immediately before it. No excluded file is needed.

## 3. LAST: individual verdicts A–I

### A — Trained affine strong/weak coupling

**LAST 19–262: pass.**

The all-block affine equations yield the second-order marginal variance coefficients
\[
(d_1,d_2,d_3)=(1,3,6).
\]
The required word contractions are \(1,2,3,2\), justified by the contained Wick proof and uniform moment bounds.

The exact null identity \(v^Tf_e=eN_{v,e}\) holds on the entire raw state space. Joint Gaussian integration by parts along the affine trajectory, followed by cancellation of the exact affine null relation, gives
\[
N_v(t)=10m'(1)\sum_i v_i(\Gamma y)_i^3\,t^3+O(t^4).
\]
For the displayed realizable triple the sum is \(7/2+5/\sqrt2>0\).

Strong continuity of the branched scalar gradients justifies the null-row derivative. Pairing it with the actual affine training direction proves a nonzero order-\(e\) mixed block at sufficiently small positive affine times.

**Clean scope:** a calculation on the evolving affine reference. It neither identifies a global nonlinear trajectory nor refutes a Schur method retaining order-\(e\) mixing and moving-constraint derivatives.

### B — Conditional sub-exponential construction

**LAST 265–627: pass as a conditional theorem.**

The Hölder estimate yields \(pD^{1-1/p}\); choosing \(p=2+\log(1/D)\) gives the Osgood modulus \(D\log(e^2/D)\). The explicit block constants are sufficient.

Capped incoming moments \(\|q\|_p\le Kp\) give exponentially small cap errors. Approximate energy is correctly derived for the nongradient capped field:
\[
\mathcal L'\le-\tfrac12\|F_R\|^2+\tfrac12d_R^2.
\]
This prevents escape from the selected prospective ball for sufficiently large caps. Direct capped-recursion comparison gives Osgood Cauchy convergence without a cap-dependent Gronwall exponential.

**Essential premise:** the actual reachable capped incoming fields satisfy the stated cap-uniform moment bounds on every stopped finite horizon. The file does not prove that premise. Finite algorithms, full observations, fitting, and nonaffinity do not follow from this theorem alone.

### C — Strong Gaussian-norm obstruction

**LAST 630–698: pass.**

For every positive perturbation size,
\[
x\bigl[g(1+\varepsilon x)-1/2\bigr]\sim-x/2
\]
in the tails. The Gaussian integral therefore forces the stated \(\psi_2\)-norm lower bound, although every fixed finite \(L^p\) difference vanishes.

The weaker \(\psi_1\) product estimate follows without independence from the elementary squared-product inequality and Cauchy–Schwarz.

**Clean scope:** failure of the proposed same-space strong-Orlicz contraction, not failure of population flow.

### D — Signed response focusing and Hessian energy

**LAST 701–968: pass.**

The pulse queries have exact instantaneous Gram \(I\), bounded values, and uniform temporal \(H^1\) bounds. The signed Gaussian observation cancels the common Gaussian component. Transport of its expected derivative gives the normalized alternating cosine sum.

Its concentration on an interval of measure \(1/(3N)\) proves divergence of every fixed \(L^p\), \(p>2\), of the \(\psi_1\) norm, and failure of square uniform integrability. A literal step factor does not supply a bounded response density.

The separate raw-ball example uses an individually bounded concentrated readout and a unit rank-one direction. The positive predictor-gradient term stays bounded while negative residual curvature diverges.

**Clean scope:** the first example is a designed causal query program; the second is an ambient raw state. Neither is asserted canonically reachable.

### E — Stationary obstruction for smooth positive metrics

**LAST 971–1280: pass.**

The scalar inverse-gate transform is valid for the toy flow. The row-field bracket has the displayed nonzero real eigenvalues, excluding simultaneous Killing cancellation. The inverse feature mobility fails the Hessian integrability condition when the inverse Gram has an off-diagonal entry.

The equal-elasticity crossing follows from the small- and large-argument expansions. Three successive choices produce the exact four stationary gradient cancellations.

The two-valued subspaces and finite-rank modifications embed the pattern inside the canonical affine raw space with a radius independent of concentration. The states have nonzero loss strictly below \(3/2\).

The unit first-row direction has curvature tending to \(-\infty\). On the invariant finite-dimensional restriction, the gradient-flow linearization therefore has positive eigenvalues tending to infinity. At a stationary point, metric-derivative terms along the flow vanish; positivity of any restricted metric forces its differential one-sided constant to dominate those eigenvalues.

**Clean scope:** no finite differential one-sided-Lipschitz constant on that whole ball for any smooth positive metric. No reachability claim is made.

### F — Order-one Gaussian readout theorem

**LAST 1282–1734: pass.**

The initialization is genuinely different from tiny readout: both endpoint coordinates have variance one.

The natural-coordinate equations and complete kernel preserve the original metric. The transformed root tuple satisfies the finite-program root hypotheses; it need not be Gaussian. Initial readout clipping plus inactive current saturation supplies legitimate bounded-derivative programs.

Trace-norm completeness, slabwise primal bounds, and
\[
e^{C_SM}\|A_0-\operatorname{clip}_M A_0\|_2\to0
\]
give the global signed feature flow. The Gaussian-envelope Osgood argument proves uniqueness in the specified class and restart with the immutable source retained.

The two mesh arguments have distinct roles: establishing square-tail control and then passing the gate-weighted kernel term. This avoids assuming an all-moment program theorem.

The physical clock has the correct factor \(2\eta(y-F)\), works for either label sign, and remains on compact feature intervals over finite physical horizons. The stationary cases \(y=0\) and \(\eta=0\) are covered. Arctangent and reciprocal-polynomial examples satisfy the class hypotheses.

**Clean scope:** compact-time GF and listed current-field observations. No raw-GD theorem, complete hidden-velocity bundle, or asymptotic fitting theorem is asserted.

### G — Equal-label sech transfer

**LAST 1736–1984: pass.**

All construction hypotheses of Part II are verified for the fixed sech activation. The two formula-sensitive replacements—feature separation and top gate-ratio rectangles—are proved explicitly. The remaining response, cap, clock, algorithm, and observation arguments use the verified bounds.

Both equal-label signs and \(\rho=-1\) are covered. Positive-time speeds and nonzero initial quadratic coefficients have separate proofs.

### H — Prescribed fixed-sign controls

**LAST 1987–2122: pass.**

Integrable spatial Lipschitz bounds establish the characteristic and its frozen-control derivative. The \(C_r^{-1}\) energy calculation is correct. The cutoff potential controls negative-coordinate expansion; for negative correlation, monotonicity of \(x+y\) bounds time spent in the central strip, including level-set boundary cases.

This proves the stated polynomial bound and the random-control moment implication.

**Clean scope:** prescribed controls with fixed component signs. Feedback variations and network control moments are not supplied.

### I — First-Euler neighborhood obstruction

**LAST 2125–2229: pass.**

The auxiliary readout is explicitly zero initially. The first Euler state, residual interval, conditional transpose law, and positive-probability large-query event are correct.

The rank-one perturbation changes one second-layer coordinate by \(A^{-1}\). Its gate effect dominates the controlled query and residual changes. The velocity/state ratio grows at least linearly in \(A\), with \(A\) chosen before width.

**Clean scope:** no width-uniform local Lipschitz estimate in the displayed transformed-coordinate/operator distance near those fixed-mesh states. No continuous-trajectory or uniqueness conclusion follows.

## 4. SCOPE: individual verdicts A–E

### A — Tanh vanishing-time continuity

**SCOPE 11–257: pass.**

The order-one Gaussian readout is retained. The clipped initialization calculation correctly gives zero reverse responses and the variances \(s_3,s_2,s_1\), hence the stated \(K_0\).

Conditional Gaussian tails control initialized queries without requiring coordinate independence. The entropy/Jensen multiplier inequality transfers those tails through every gate against a **fixed initialized multiplier**, so no logarithm is iterated.

The signed feature clock gives vanishing-time kernel and field continuity. For zero label its compact physical horizon has a vanishing feature clock, yielding the stationary limit.

Both coordinate balance identities and the inverse-gate RMS estimate are correct. They do not imply square-tail control of the ungated reverse query.

### B — Sin-plus-cosine initialization

**SCOPE 259–413: pass at the stated initialization/formal level.**

The Gaussian identities, iterated feature Grams, and strict positivity for distinct inputs are correct. Polynomial interpolation proves strictness even when the input Gram is singular.

The matrices \(J_3,J_2\) are the actual expected source derivatives. The Gaussian innovations and bounded response terms give positive-definite \(R_j\); the tensor argument proves the needed strict Hadamard-product positivity.

The hidden degree-two kernel coefficients and doubled label-mode coefficient have the correct mean-loss factor \(\gamma=2/m\). The trigonometric integral formula and residual \(1-2/e\) are correct.

The first-step Gaussian calculation disproves the specified purported tail estimate.

**Clean scope:** formal initialization coefficients, without an analytic remainder or constructed positive-time trajectory.

### C — Fixed-offset affine reference

**SCOPE 415–595: pass.**

The given-space polynomial Hilbert ODE is globally well posed by energy and the complete-space endpoint argument. Canonical initialization gives \(Q_\ell(0)=G+\ell\mathbf1\mathbf1^T\).

The full kernel, augmented-Gram lower bound, offset balance defects, and projected invariants are correct. Stationary prediction classification follows from the four block equations and affine independence of three distinct unit inputs.

The fitting implication correctly assumes both positive raw Gram and entry below \(4/3\). Its residual-length clock yields
\[
R_u=-\|\theta_u\|^2,
\]
a finite total clock, a bounded state, and eventual uniform kernel positivity.

**Clean scope:** no unconditional crossing of the mixed-label threshold and no positive-nonlinearity continuation theorem.

### D — Same-array causal response lemma

**SCOPE 598–795: pass.**

The inverse bounds respect the difference between row control and column-density control. In particular, the proof does not falsely assign a column-density estimate to \(AB\).

Elimination uses the same actual arrays and covariance. Actual second moments bound the Gaussian parts; a Volterra estimate gives \(C\sqrt p\) moments without a smallness assumption on \(\varepsilon S\).

The eigenvalue separation argument, initialized decomposition \(Q_3=\kappa G+\varepsilon^2R\), and initial mixed-block bounds are valid. The Schur-coordinate equation retains \(\dot L\), and the readout projection identity retains both the moving offset and orthogonal component.

**Clean scope:** the response and second-moment premises are hypotheses, not consequences of raw energy.

### E — Reached positive-time non-Lipschitzness

**SCOPE 797–1256: pass.**

The local sech construction is valid for either label pair. Symmetry gives the population label mode, and a sufficiently short interval keeps the physical clock positive.

The lower-tail proof establishes dependence-sensitive joint events rather than presuming independence of trained fields:

- a mesh-uniform Gaussian increment estimate controls the reverse residual path;
- scalar regression isolates a large terminal reverse source;
- independent forward-source regression leaves zero terminal remainder;
- a bounded displacement and Lipschitz bound for its scalar input produce a preimage interval of positive Gaussian measure;
- closed-set passage preserves the lower bound through mesh and cap limits.

The sample-isolating rank-one direction has unit Hilbert–Schmidt norm. The lower curvature term has both unbounded signs. The upper-layer contribution is uniformly bounded because the reached readout is pointwise bounded. Its scalar second derivative is justified with only an \(L^2\) upper variation.

The full summed-loss identity
\[
-D^2\mathcal L[v,v]
=4(1-g)D^2g[v,v]-2\sum_a(Df_a[v])^2
\]
then proves failure of raw-Hilbert local Lipschitzness at those actual reached states.

This is compatible with the separately proved strong existence, uniqueness, and restart. It supplies neither a finite-width positive-time Hessian limit nor global opposite-label continuation.

## 5. IDENTITY: individual verdicts §§1–8

**IDENTITY 1–1032: pass.**

1. **Normalization and quantifiers.** Dividing endpoint vectors by \(\sqrt n\) gives precisely the displayed Euclidean endpoint/ordinary connector update. Signed feature time contains no residual or loss factor. Depth and program length are fixed before width.

2. **Source and state space.** The two-sector Fock construction matches the proved Gaussian-word dependency, including \(L=1\). Trace-class increments form a complete Banach space; the gradient identity is separately placed in the Hilbert–Schmidt Hilbert space. The derivative bounds yield
   \[
   K_1=6,\quad K_2=27,\quad K_3=108.
   \]

3. **Fixed Euler programs.** Rank-one unrolling expresses each fixed program through finitely many initial rooted Gram entries. Polynomial moment bounds justify convergence in every fixed finite \(L^p\), including expected outputs. Finite-rank singular-value observations pass through Gram square roots. Oddness follows from initialization-law symmetry, not from falsely fixing the deterministic representative under readout sign reversal.

4. **Cubic coefficient.** The differentiated Euler recurrence and Hilbert gradient identities are correct. Orthogonal root sectors give \(S_0=0\). Creation/annihilation returns give
   \[
   H_0^{\rm sc}
   =2\sum_{q=1}^L(L-q+1)q^2
   =\frac{L(L+1)^2(L+2)}6.
   \]
   Hence the coarse-minus-fine cubic coefficient is exactly
   \[
   -\frac{t(2t-1)L(L+1)^2(L+2)}3.
   \]

5. **Uniform transported defect.** The noncommutative telescoping order is correct. Removing the exact \(h^2\) local-defect factor leaves a \(C^3\) quantity. The explicit majorants bound state derivatives, interpolation derivatives, and transported tangent derivatives using only the stated fourth derivatives. Oddness eliminates its constant and quadratic terms. The integral Taylor remainder gives \(C_Kt^4|h|^5\) on \(|h|\le1/(16Kt)\), including negative steps.

6. **Local operator flow.** Picard contraction on the signed interval \(T_L=1/(8K_L)\), the first-exit argument, and Euler defect estimate prove unique local flow and uniform trace-norm/endpoint-norm convergence after the fixed-program width limit.

7. **Dyadic consequence.** Substitution \(h=T/(2t)\) meets the radius condition. The \(1/t\) bound and its geometric summation have the stated constants. Identification uses the independently constructed operator flow.

8. **Activation-stability obstruction.** The two activations have distance \(n^{-1/2}\) and identical bounded positive slopes. At the displayed bounded-energy state, the exact bottom updates are \(4h\mathbf1\) and \(3h\mathbf1\). Their RMS discrepancy is \(|h|\), disproving the proposed width-uniform activation stability estimate.

The identity theorem remains local in feature time and sequential in its limits. Its deterministic energy-ball obstruction does not concern Gaussian-typical initialization or expected-output continuity.

## 6. Corrections and final integrity

**No required mathematical corrections were found.** The clean scope is exactly the collection audited above. In particular, the files do not establish:

- unconditional three-input nonlinear continuation from LAST B’s unproved moment premise;
- positive-time dynamics from SCOPE B’s formal coefficients;
- global opposite-label physical continuation from the local two-sample construction;
- global feature-time existence for IDENTITY;
- simultaneous growing-depth/width limits or infinite-time/width exchanges.

Final SHA-256 hashes equal both the observed starting hashes and `INPUTS.json`:

| File | Unchanged SHA-256 |
|---|---|
| `NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `FINAL_LAST_ADDITION.md` | `bb28eb597f0e6a230e90674eb379e2a901e2038f8aa1138b1e236e137c212976` |
| `FINAL_SCOPE_ADDITION.md` | `b85476dd8886365c292de1cd19463f988971d6f472800d838a8a1cd6d7b166d6` |
| `FINAL_IDENTITY_UNIFORM_ADDITION.md` | `d26113499bb36349cbb95fe7c78bedc74e694b4ae57ffcc862c7351103081bce` |
| `FINAL_LAST_R2_DEPENDENCIES.md` | `d98b98ce35bf3f2f16d55be8ded7c1d10dd4f713abb49169f07bd3b82b808753` |

**Attestation:** complete every-line reading of all **9,476 scientific lines**, complete reading of the **4,861-line dependency packet**, resolved truncated displays, no excluded content reads, no delegation or experiments, and unchanged final inputs.