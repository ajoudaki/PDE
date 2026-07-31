# Hostile referee report: what would count as a simulation of the conjectured finite PDE?

## Executive verdict

The existing long-horizon bundle is scientifically useful evidence for the
finite-matrix chronological \(q/r\) truncation, but it is **not** a simulation
of the finite Liouville PDE in the conjecture. This is not a semantic
objection:

- `FieldState.W` stores an array of shape \((L,n,n)\);
- the projected velocity explicitly evaluates
  `state.W[ell] @ q` and `state.W[ell].T @ r`;
- its memory is \(O(Ln^2)\);
- all 19 raw traces have
  `actual_compiled_liouville_pde_run=false`;
- the bundle itself reports zero compiled Liouville-PDE runs.

Renaming the neuron index a “particle” does not change this classification.
A lawful particle or grid discretization of the PDE may have a numerical
resolution \(M\), but each numerical particle must live in the fixed
compiler-emitted coordinate space
\(\mathbb R^{D_{K,J,N}}\), and its evolution may use only the finite current
moments and deterministic \(\kappa\)-coordinates. It may not carry a second
neuron index or call an \(n\times n\) matrix action.

The written conjecture has the right high-level anti-oracle intent. However,
Sections 6.1--6.2 are not yet an executable mathematical compiler. In
particular, the width-free multiple-query Gaussian/Onsager rule and the
historical-\(\kappa\) construction are asserted rather than enumerated.
Consequently, a new program can honestly be called a simulation of the
**formal first-response PDE design** only after it supplies the missing
finite rules in a frozen manifest. It cannot yet claim to be a literal
implementation of a uniquely specified compiler merely by citing the prose.

A scientifically valid claim should be staged:

1. **Formal PDE realization:** a complete, width-independent finite
   McKean--Vlasov PDE/ODE has actually been emitted and numerically solved.
2. **Finite-horizon evidence:** its solver-converged observables agree with
   an independently estimated ordered width-then-depth limit over a full
   transient.
3. **Global-in-simulated-time evidence:** the same fixed PDE continues to
   agree through an audit-fixed horizon-doubling plateau.
4. **Evidence for the conjectured cofinal family:** the preceding agreement
   improves along the predeclared diagonal
   \((K,J,N)=(\ell,\ell,\ell)\).

Anything stopping before item 1 is not a PDE simulation. A single successful
PDE order establishes item 1 but not item 4.

## I. Non-negotiable definition of a qualifying numerical state

For fixed \(\ell=(K,J,N)\), a permissible numerical approximation has the
form

\[
Z_{\ell,M}
=
\left\{(\xi_i,w_i)\right\}_{i=1}^{M}
\times \kappa,
\qquad
\xi_i\in\mathbb R^{D_\ell},
\]

or a grid/spectral density representation on the same
\(\mathbb R^{D_\ell}\). Here:

- \(D_\ell\), the number of \(\kappa\)'s, all expression DAGs, and all
  observable formulas are fixed by \((m,K,J,N)\);
- \(M\) is solely a numerical density/cubature resolution;
- the only collective inputs to a particle velocity are the finite declared
  moments \(\mathcal M[\rho_M]\) and \(\kappa\);
- increasing a reference-network width \(n\) or depth \(L\) does not change
  the PDE state, source dimension, or drift;
- no state object has two indices whose ranges are both a network width, and
  no object stores one \(n\times n\) matrix per physical layer.

An \(M\times M\) array is not automatically forbidden: a generic density
solver can use one. Its dataflow must be numerical quadrature/interpolation
for a fixed-dimensional PDE, not a learned dense operator acting between
neuron coordinates. In the present finite-moment PDE, an unexplained
\(M\times M\) learned matrix is presumptively disqualifying.

## II. Hard acceptance gates

The following are gates, not optional diagnostics. Failure of any one means
the run must not be described as a simulation of
\((\mathrm{PDE}\text{-}K,J,N)\).

### Gate 1: width and original-depth independence

**Static test**

Compile the same \((K,J,N,\vartheta)\) while setting external reference
network options to at least two values of \(n\) and \(L\). The compiler
artifact must be byte-identical. Its manifest must list:

- \(D_{K,J,N}\);
- every particle tag with grade and complexity;
- every \(\kappa\) with type, initial value, and ODE DAG;
- every requested moment;
- the fast-query filtration and covariance DAG;
- the depth basis, \(Q_{K,J,N}\), and ridge \(\tau_{K,J,N}\);
- the observable DAGs.

Neither `n` nor `L` may occur as a runtime or structural input to the PDE.
They may occur only in the completely separate reference-network runner.

**Dynamic test**

Run the PDE executable with every reference file removed and reference code
unimportable. The serialized initial state, RHS evaluations at fixed test
states, and final output hashes must be unchanged.

**Resource test**

For fixed \((K,J,N,M)\), measured PDE memory and RHS cost must remain
unchanged when only the reference \(n,L\) settings change.

### Gate 2: no dense microscopic state or action

Instrument every state allocation and linear operation. Reject the
implementation if any of the following occurs inside the PDE runner:

- allocation of \(W_\ell\), \(W_\ell^\top\), a Jacobian \(J\), or an array
  with \(O(n^2)\) microscopic entries;
- evaluation of \(Wu\) or \(W^\top u\) using a realized network matrix;
- storage of a neuron-pair-indexed history or response;
- importing a finite-network checkpoint to initialize or continue the PDE;
- setting the PDE particle count equal to reference width and using
  particle-pair parameters as network weights.

Fast tags such as “\(Wq\)” are legal only as finite-dimensional conditional
random variables generated by the emitted \(\Gamma\), never as matrix
multiplications.

### Gate 3: a complete, finite, frozen compiler

Before generating target trajectories, freeze and hash:

- the AST constructor and canonicalization rules;
- the exact finite RHS template list;
- the least-fixed-point queue order;
- the SCC-promotion rule;
- the zero-closure rule;
- all query-filtration rules;
- all Gaussian/Onsager formulas;
- all \(\kappa\)-generation and differentiation rules;
- the diagonal resolution schedule;
- numerical PDE/cubature solvers and stopping tolerances.

The emitted drift must be a closed finite DAG. It may use only arithmetic,
declared \(\tanh^{(j)}\)'s, prescribed Legendre/Gauss--Legendre data, the
fixed ridge/PSD operations, finite Gaussian integrals, current declared
moments, \(\kappa\), and \(\vartheta\).

Reject any artifact containing:

- an unevaluated “DMFT,” “tensor program,” “graph limit,” or
  \(\mathscr G\) callback;
- a generic root solver whose branch is selected by target behavior;
- opaque callable code or a learned black-box closure;
- constants fitted from positive-time network data;
- a table indexed by physical time or a target hitting time;
- a callback evaluating an omitted exact response word.

The PDE run must succeed when exact-network outputs are unavailable.

### Gate 4: autonomous and genuinely restartable evolution

The mathematical RHS must have the signature

\[
F_\ell(\rho,\kappa;\vartheta),
\]

not \(F_\ell(t,\rho,\kappa;\vartheta)\). An integrator may pass `t`, but a
unit test must show the returned RHS is bitwise or tolerance-identical at
different `t` values for the same state. An absolute-time/phase coordinate
is forbidden unless it is one of the architecture-derived tags in the
frozen manifest.

Perform all four restart tests:

1. **Semigroup split:** compare \(0\to T\) with
   \(0\to t_0\), serialize only \((\rho,\kappa)\), start a fresh process,
   then \(t_0\to T\). The discrepancy must be no larger than the independent
   time-discretization estimate.
2. **Cache purge:** clear all query and Gaussian caches before evaluating
   the restarted RHS. It must agree with a no-purge evaluation.
3. **Same-state/two-history:** construct or copy the identical serialized
   \((\rho,\kappa)\) through two different program histories. Subsequent
   RHS values must agree.
4. **Off-trajectory perturbation:** perturb several admissible moments and
   historical \(\kappa\)'s by a predeclared small amount, recheck the
   algebraic/boundary constraints, and restart. The vector field must remain
   single-valued and stable; it may not consult a canonical trajectory.

As a stronger non-playback test, change \(y\) at a positive-time state and
continue using the same compiler template with the new residual. This is
not required by Clause B as written, but it is highly probative because all
emitted velocities are supposed to be label-separated and linear in \(e\).

Fresh random Gaussian samples at every RHS call would define a stochastic
algorithm, not the deterministic Liouville PDE. Use deterministic Gaussian
quadrature/frozen QMC, or separately prove convergence of the stochastic
inner estimator. The latter's complete random state must be included in
restart tests and its error must be separated from PDE model error.

### Gate 5: correct oriented Gaussian/Onsager semantics

Replacing every \(W^\top\)-query by an independent Gaussian is an automatic
failure even if curve agreement looks good.

At minimum, the emitted \(\Gamma\) must pass:

1. **Stein/Onsager unit test.** For independent \(h\) with
   \(\|h\|_n^2\to q\), verify
   \[
   \mathbb E[(W^0)^\top\varphi(W^0h)\mid h]
   =
   \sigma_w^2\mathbb E[\varphi'(Z)]h+o_n(1)
   \]
   for several smooth bounded \(\varphi\), including the actual
   \(\tanh'\)-derived functions.
2. **Multiple adaptive query test.** For a frozen finite query DAG containing
   both row and column queries, compare every emitted conditional mean and
   covariance against direct large-\(n\) Gaussian-matrix Monte Carlo.
   Test correlated and rank-deficient queries.
3. **Orientation mutation test.** Deliberately replace one transpose query
   by an independent tag. At least one Onsager diagnostic must fail. A test
   suite unable to detect this mutation is inadequate.
4. **Ridge limit test.** For the prescribed
   \(\tau_{K,J,N}\), verify PSD covariance and continuity through rank
   changes; along the fixed diagonal, verify convergence toward the
   pseudoinverse conditioning result in cases where the latter is
   unambiguous.
5. **Distinct-depth test.** Confirm the unlearned fast innovations are
   independent across distinct iid-depth slots before the declared learned
   corrections, while all learned cross-depth dependence enters only
   through emitted current state.

### Gate 6: learned-history closure is current-state closure

For every retained \(W(t)-W^0\) or transpose query, the manifest must name
the exact \(\kappa\)-coordinates that determine its conditional law and the
ODEs updating them. No past integral or hidden trajectory array may be
evaluated.

Tests:

- differentiate each emitted \(\kappa\)'s defining contraction by automatic
  differentiation and compare it to its emitted
  \(\sum_q e_qB_\alpha^{(q)}\) DAG at random admissible states;
- at initialization, compare emitted values with analytic Gaussian moments;
- on small finite-\(n,L\) checkpoints used only as an external diagnostic,
  compare retained learned-query contractions with ensemble estimates and
  check convergence in width;
- serialize \((\rho,\kappa)\), delete all earlier time samples, and verify
  the same retained learned-query answers after restart;
- inject a coherent rank-one perturbation of the type used in the
  continuation witness and verify that a retained response/history
  coordinate detects it. If it is invisible to every retained coordinate,
  its contribution must be explicitly in the outgoing residual rather than
  silently discarded.

### Gate 7: the simulated observables are exactly the conjectured readouts

Record, at every stored time:

- all \(m\) outputs and loss;
- all entries of \(G^h(s,t)\) on an independent dense depth-check mesh,
  including both endpoints;
- the full reconstructed \(\widehat\Theta(t)\);
- its smallest eigenvalue;
- the generator-derived \(\partial_tf\) and the defect
  \(\|\partial_tf+\widehat\Theta e\|\);
- mass, called moments, boundary-lift defects, covariance PSD defects, and
  \(\kappa\)-Dirac/common-population defects.

The depth-check mesh must not be only the compiler's Gauss--Legendre nodes.
The primary observable metric is

\[
\max_{t_i\le T}
\left[
\|f_\ell(t_i)-f_{\rm ref}(t_i)\|_2
+
\max_{s\in\mathcal S_{\rm check}}
\|G_\ell^h(s,t_i)-G_{\rm ref}^h(s,t_i)\|_F
+
\|\widehat\Theta_\ell(t_i)-\Theta_{\rm ref}(t_i)\|_F
\right].
\]

Loss-only, endpoint-only, or terminal-time comparisons fail this gate.
PSD of \(\widehat\Theta\) is necessary but not sufficient. Because the
written finite response PDE does not prove that its proxy kernel exactly
drives its output at finite \(\ell\), the identity defect must be reported
and must decrease under compiler refinement before a gradient-flow-like
interpretation is claimed.

## III. Numerical convergence tests for the PDE itself

Passing the hard gates says the correct finite PDE was attempted. It does
not show its numerical solution is accurate.

For each compiler index used in a scientific comparison:

1. Use at least three time resolutions and report common-grid differences.
2. Use at least three density/cubature resolutions \(M\). With Monte Carlo
   particles, use independent replicates, confidence intervals, and verify
   the expected self-averaging trend. With deterministic cubature, show
   successive differences.
3. Separately refine any inner Gaussian quadrature/QMC used to evaluate
   \(\Gamma\).
4. Compare two integration schemes on a representative run.
5. Require the total numerical uncertainty in the primary observable norm
   to be materially below the claimed PDE-versus-target discrepancy;
   a useful preregistered rule is at most \(20\%\) of that discrepancy.
6. Verify conservation of probability mass, finite called moments, boundary
   constraints, and covariance PSD to the declared solver tolerance.

Particle count \(M\), time step, and Gaussian quadrature order are numerical
solver resolutions. \(K,J,N\) are model/compiler resolutions. They must not
be pooled into one favorable-looking “resolution” axis.

## IV. The only valid finite-network reference comparison

The target in the conjecture is the ordered limit

\[
n\to\infty\ \text{at fixed }L,
\qquad\text{then}\qquad L\to\infty.
\]

A single \(n,L\), or a joint diagonal \(n=L\to\infty\), is not the target.
Use an independently frozen reference grid:

1. For each of at least three or preferably four depths \(L\), run at least
   three or preferably four widths and enough seeds to resolve ensemble
   uncertainty.
2. At each fixed \(L\), establish self-averaging and extrapolate the
   observable curve to \(n=\infty\). Report bootstrap/fit uncertainty and
   sensitivity to the extrapolation model.
3. Only then extrapolate the width-limit curves in \(L\). Preserve the full
   time and depth dependence.
4. Use held-out widths and depths to test the extrapolation.
5. Keep all reference code and data outside the PDE process. Comparison is a
   post-processing step.

For any claimed tolerance \(\varepsilon\), separately report:

\[
\text{PDE solver error},\quad
\text{finite-\(n\) reference error},\quad
\text{finite-\(L\) reference error},\quad
\text{finite compiler error}.
\]

The target comparison is scientifically resolved only if the first three
are smaller than the fourth or are jointly included in a conservative
uncertainty interval.

The existing bundle's one-seed width pair \(n=32,96\) and one-seed depth pair
\(L=8,32\) do not estimate this ordered limit. They were suitable stress
checks for the finite-matrix surrogate, not an asymptotic PDE reference.

## V. Compiler-resolution convergence

The core conjecture concerns the fixed diagonal

\[
(K,J,N)=(\ell,\ell,\ell),
\]

not an order chosen after inspecting a trajectory.

Required evidence:

- freeze a consecutive set of at least three cofinal indices
  \(\ell_1<\ell_2<\ell_3\);
- compile all of them before reference curves are opened;
- solve each to tighter numerical error than its difference from adjacent
  compiler levels;
- report both the target errors and the PDE Cauchy differences
  \(d_{\rm obs}(\mathcal O_{\ell+1},\mathcal O_\ell)\);
- retain the same diagonal schedule for every \(\vartheta\) and every
  horizon.

Strict monotonicity is not a theorem and should not be imposed as a logical
requirement. But a single successful order, or alternating/cherry-picked
\((K,J,N)\), is not evidence for (38). Credible evidence needs a stable
Cauchy trend and decreasing target discrepancy across more than one
refinement, within uncertainty.

One-axis \(K\), \(J\), and \(N\) sweeps are valuable diagnostics for locating
the dominant error but do not replace the fixed-diagonal result.

## VI. Long-horizon and plateau audit

Reuse the strongest ideas from the existing long-horizon protocol, now for
the actual PDE:

1. Freeze horizons \(T,2T,4T,\ldots,T_{\max}\), plateau thresholds, compiler
   levels, PDE numerical resolutions, and reference grid before the final
   extension.
2. For both the PDE and the extrapolated reference, require on the final
   half-horizon:
   - small residual relative to a fixed output scale;
   - small output and every-depth Gram distance to the endpoint;
   - small analytic output and Gram speeds;
   - small tail arclength.
3. Accept a plateau first seen at \(T\) only if every later doubling remains
   flat and successive endpoint drift stays within the earlier tolerance.
4. Report prefix-uniform output, all-depth Gram, and tangent-kernel errors at
   every doubling, plus the increment of each prefix maximum.
5. Keep \((K,J,N)\) fixed throughout each trajectory. Do not reset,
   recalibrate, or increase order after observing a difficult time segment.
6. Include boundary points of \(\mathcal U\), multiple seeds for the
   reference, and at least one deliberately slower/ill-conditioned
   in-family case if one exists.
7. Verify zero-residual gating: when \(e=0\), every emitted particle and
   \(\kappa\) velocity must be zero up to solver tolerance. Persistent
   hidden-state drift after fit is a failure of the claimed residual-gated
   closure.

Passing this test is evidence for global-in-**simulated**-time behavior. It
does not prove the literal \(\sup_{t\ge0}\) in (38), and the report must say
so.

## VII. Undefined or underdetermined clauses in the present compiler

These gaps must be closed in code and in a machine-readable specification
before a run can be called a literal implementation of Section 6.

### 1. The least-fixed-point rewrite system is not enumerated

Phrases such as “every budget-admissible chain-rule child,” “the finitely
many emitted right-hand-side templates,” and “the query DAG emits” do not
specify a unique AST rewrite system. Canonicalization modulo scalar
algebra, tag identity, duplicate queries, and derivative expansion order can
change the retained table. A valid implementation must publish the exact
rewrite rules and its complete emitted table; two independent
implementations should reproduce its hash.

### 2. The width-free Gaussian conditioning rule is missing

The displayed semantic derivation conditions
\(\operatorname{vec}(W^0)\in\mathbb R^{n^2}\) on \(n\)-dimensional query
vectors and contains explicit \(1/n\) cross blocks. The text then says the
finite compiler eliminates these by query-count Gram matrices and
ridge/Woodbury identities. The actual finite scalar/block formulas for an
arbitrary adaptive mixture of row and column queries are not given.

This is the most dangerous gap: an implementation can silently drop the
\(O(1/n)\)-entry cross block whose coherent effect is the \(O(1)\) Onsager
term. “We sample a joint Gaussian” is not sufficient. The precise limiting
conditional mean, covariance, and innovation coupling must be emitted for
every query tuple and unit-tested as in Gate 5.

### 3. The historical-\(\kappa\) sector is asserted, not constructed

The text states that SCCs are promoted, their defining moments are
differentiated, and the resulting
\(\dot\kappa_\alpha=\sum_qe_qB_\alpha^{(q)}\) records return to the budgeted
queue. It does not give:

- the exact definition of each learned-matrix query coefficient;
- how a current query vector that itself evolves is expanded in retained
  history coordinates;
- the complete differentiation rules;
- the termination argument after SCC promotion creates new records;
- explicit initial and depth-boundary values.

This is where two-training-time memory could be hidden. An implementation
must show that every retained learned action is reconstructed from current
\((\rho,\kappa)\), with no unlisted path integral.

### 4. \(\Gamma_{K,J,N}\) is not explicitly emitted in the note

“A deterministic \(\tanh\)-expression pushforward of one finite Gaussian
base” does not specify the dimension, covariance factorization, query order,
or cross-node coupling. The map from iid physical layers to
Gauss--Legendre depth nodes is especially delicate: raw iid matrices do not
possess a smooth depth interpolation. The implementation must state which
variables are Young-measure innovations and which correlations are learned
slow-state effects.

### 5. The compiled initial pair is not explicit

The note calls \(\rho_{K,J,N}(0)\) a finite-dimensional Gaussian pushforward
but does not list its base Gaussian vector or pushforward DAG for the coupled
forward, backward, \(q/r\), fast-tag, and \(\kappa\) coordinates. This must
be emitted rather than inferred from a positive-time finite network.

### 6. \(J_*\), \(\mathcal M[\rho]\), and \(\mathcal A_{K,J,N}\) are semantic

\(J_*\) is defined as a minimum over a verbally described table, not
computed. The called-moment list is not printed. The admissible restart set
is described by “all moments called by the DAGs” and “algebraic moment
identities,” but those are not enumerated. A program must emit all three
objects explicitly and expose a validator for \(\mathcal A\).

### 7. The numerical realization of the law is unspecified

The conjecture defines a continuity equation, not whether it is solved by
particles, grids, sparse grids, spectral density coefficients, or cubature.
That freedom is legitimate, but solver convergence is a separate numerical
obligation. A finite particle count is not itself the finite PDE promised by
the conjecture; it is a discretization of that PDE.

### 8. PSD reconstruction is weaker than sensitivity consistency

Equation (29) makes a PSD proxy, but the note does not establish
\(\partial_tf=-\widehat\Theta e\) for a finite truncated PDE. The existing
finite-matrix bundle correctly records this defect. A new implementation
must do the same and may not infer loss monotonicity or coercivity from PSD
alone.

### 9. The semantic outgoing residual is not executable

Equation (42) contains the conjectural graph-limit operator \(\mathscr G\).
It may appear in a proof audit, never in the PDE drift or a claimed
computable error bar. Without a separate finite majorant and domination
theorem, no numerical run is “certified to accuracy \(\varepsilon\)” in the
strict sense of Section 8.4.

### 10. Global well-posedness and the exact target remain conjectural

A numerical solver reaching \(T\) does not establish Clause A or B, and
finite network extrapolation only estimates the target. These limitations
do not invalidate a careful experiment, but they constrain its language.

## VIII. Assessment of the existing \(q/r\) bundle

### What it validly establishes

- The finite-\((n,L)\) Euclidean \(\mu\)P equations are implemented and
  algebraically audited.
- \(K=L\) recovers the exact differentiated \(H,P\) dynamics to roundoff.
- Fixed low \(K\) predicts full finite-network output and every-depth Gram
  curves with a clear order hierarchy.
- Those finite-matrix predictions persist through an operational
  horizon-doubling plateau at \(T=32\).
- Time-step refinement, zero-residual freezing, and hostile plateau
  detector tests are present.
- The bundle explicitly avoids claiming a PDE run.

### Why it cannot answer the current request

- It retains \(W_\ell\in\mathbb R^{n\times n}\).
- It has no \(J\)-grammar truncation.
- It has no \(N\)-Galerkin depth-law compiler.
- It has no \(\Gamma\), Onsager conditional kernel, or \(\kappa\) history
  sector.
- It has no numerical density/cubature convergence study for a law PDE.
- Its restarts use the full finite-matrix state.
- It does not estimate the ordered width-then-depth target.
- It contains zero diagonal-\(\ell\) Liouville-PDE comparisons.

Therefore its reported errors must never be relabeled “PDE errors.” They are
valuable prior evidence that the chronological \(K\)-axis may converge, and
nothing more.

## IX. Minimum publishable experiment

A minimal honest first result would contain:

1. one fully printed compiler artifact at a nontrivial \((K,J,N)\), with an
   explicit \(J_*\) if the first-response block is used;
2. a width-independent particle or grid solver passing Gates 1--7;
3. solver refinement in time, particle/cubature resolution, and inner
   Gaussian integration;
4. oriented Gaussian/Onsager and historical-\(\kappa\) unit tests;
5. comparison of \(f\), every-depth \(G^h\), and \(\Theta\) against an
   independently extrapolated ordered width-then-depth reference;
6. at least three fixed-diagonal compiler levels, or, if only one level is
   computationally feasible, an explicit statement that this demonstrates
   a formal PDE run but does not test convergence (38);
7. an audit-fixed horizon-doubling extension through plateau;
8. source hashes, compiler-manifest hashes, raw data, and negative mutation
   tests.

If the first honest implementation simplifies the written compiler—for
example by retaining only a demonstrably closed subset of the \(K=1\)
queries—it must be labeled a **new explicit candidate PDE**, not
\((\mathrm{PDE}\text{-}1,J_*,N)\). It can still be excellent evidence if it
is width-independent, autonomous, non-oracular, and compared under the full
protocol above.

## Final referee decision

At present, no available executable qualifies as a simulation of the
conjectured finite PDE. The previous numerical evidence is strong for a
matrix-response mechanism but leaves the central width-law compression
untested.

A claimed implementation can be scientifically valid, but only if it makes
the missing conditioning/history compiler explicit and passes the hard
gates before curve agreement is examined. The decisive falsification checks
are:

\[
\boxed{
\text{remove }W,\quad
\text{remove reference access},\quad
\text{restart from }(\rho,\kappa),\quad
\text{pass Onsager},\quad
\text{refine the PDE},\quad
\text{compare to the ordered limit}.
}
\]

Those tests distinguish a genuine finite neural-PDE experiment from another
accurate finite-network response surrogate.

---

## Addendum: hostile audit of the explicit operator--Galerkin alternative

### Conditional verdict

The proposed Hermite/isonormal construction **does qualify as a genuine
candidate finite PDE**, provided it is derived in the correct order and
passes the gates below. It is not yet an implementation of the particular
response-word compiler in Section 6, so it should initially be called the
**operator--Galerkin candidate PDE**.

Its finite rank is not automatically a forbidden low-rank architecture.
There is a sharp distinction:

- **Legitimate:** first take the dense network's width limit, represent the
  iid Gaussian matrix as a cylindrical isonormal action on the neuron-law
  Hilbert space, and then apply a fixed Galerkin projection
  \(\Pi_P\). The original reference network remains fully dense, and
  \(P\to\infty\) is an accuracy axis.
- **Illegitimate:** replace the original finite network by
  \(W=E_P\Phi_P^\top\), train that factorized rank-\(P\) network, and present
  its curve as the dense model's PDE limit.

The former is no more a change of architecture than a spectral truncation of
a kinetic PDE. The latter is exactly the low-rank-backbone loophole excluded
by the project.

### The minimum explicit candidate

Use a fixed standardized Gaussian base latent
\[
x=(B^0_{\rm row},a^0/A)\sim\mu_0
\]
and a predeclared complete orthonormal basis
\(\{\phi_j\}_{j\ge0}\) of \(L^2(\mu_0)\), with a fixed multi-index
enumeration. For a slow column field \(u(x)\), define
\[
H_j[u]:=\mathbb E_x[\phi_j(x)u(x)].
\]

At Galerkin order \(P\), the local iid initialization operator must be
interpreted cylindrically:
\[
(\mathcal W^0_Pu)(x,\varepsilon)
=
\sigma_w\sum_{j<P}\varepsilon_jH_j[u],
\qquad
\varepsilon\sim N(0,I_P).
\]

Let the learned row coefficients be
\[
c_j=c_j(s,x,\varepsilon,t),
\]
not global scalars. Then
\[
(\mathcal W_Pu)(s,x,\varepsilon,t)
=
\sum_{j<P}
\bigl(\sigma_w\varepsilon_j+c_j(s,x,\varepsilon,t)\bigr)H_j[u].
\tag{OG-1}
\]

Its exact shared transpose is
\[
(\mathcal W_P^*\beta)(s,x,t)
=
\sum_{j<P}\phi_j(x)
\mathbb E_{x',\varepsilon}
\left[
\bigl(\sigma_w\varepsilon_j+c_j(s,x',\varepsilon,t)\bigr)
\beta(s,x',\varepsilon,t)
\right].
\tag{OG-2}
\]

The proposal is not adequately specified unless both the initialization and
learned pieces in (OG-2) are present.

For the residual-tanh model, a closed candidate has slow fields
\(b(x,t)\), \(a(x,t)\), \(h_r(s,x,t)\), and \(p_r(s,x,t)\), and fast local
fields
\[
z_r(s,x,\varepsilon,t)
=\mathcal W_Ph_r,\qquad
\beta_r(s,x,\varepsilon,t)
=\tanh'(z_r)p_r(s,x,t).
\]

The depth equations are
\[
\partial_sh_r
=
\gamma\mathbb E_\varepsilon[\tanh(z_r)],
\qquad
h_r(0,x,t)=b(x,t)^\top x_r,
\tag{OG-3}
\]

\[
-\partial_sp_r
=
\gamma\mathcal W_P^*\beta_r,
\qquad
p_r(1,x,t)=a(x,t).
\tag{OG-4}
\]

The projected Euclidean parameter flow is
\[
\dot a(x)
=-\sum_qe_qh_q(1,x),
\tag{OG-5}
\]

\[
\dot b(x)
=-\sum_qe_qp_q(0,x)x_q,
\tag{OG-6}
\]

\[
\boxed{
\dot c_j(s,x,\varepsilon)
=
-\gamma\sum_qe_q\,
\beta_q(s,x,\varepsilon)\,
H_j[h_q(s,\cdot)].
}
\tag{OG-7}
\]

The output is
\[
f_r=\mathbb E_x[a(x)h_r(1,x)].
\tag{OG-8}
\]

Equations (OG-1)--(OG-8), plus a fixed depth discretization and an explicit
law/characteristic formulation, are a finite, autonomous, width-independent
PDE/integral system for every \(P\). A code that instead makes \(c_j\) a
single population scalar, drops its \(\varepsilon\)-dependence, or samples a
new \(\varepsilon\) after every training step is not this system.

### Why the Gaussian part is faithful

For any finite collection \(u^1,\ldots,u^r\in L^2(\mu_0)\),
\[
\operatorname{Cov}
\left(\mathcal W_P^0u^a,\mathcal W_P^0u^b\right)
=
\sigma_w^2
\langle\Pi_Pu^a,\Pi_Pu^b\rangle_{L^2(\mu_0)}
\longrightarrow
\sigma_w^2\langle u^a,u^b\rangle.
\tag{OG-9}
\]

Thus the forward cylindrical laws converge by Parseval. Moreover (OG-2) is
the exact adjoint of (OG-1):
\[
\mathbb E_{x,\varepsilon}
\left[
\beta\,\mathcal W_Pu
\right]
=
\mathbb E_x
\left[
u\,\mathcal W_P^*\beta
\right].
\tag{OG-10}
\]

This identity is the operator-Galerkin version of the row/column
conditioning and Onsager requirement. It is much stronger than assigning an
independent Gaussian to a transpose query.

One must **not** claim that
\(\mathcal W_P^0\to\mathcal W^0\) in operator norm or that the infinite iid
Gaussian matrix is a Hilbert--Schmidt kernel on
\(L^2(\mu_0)\). It is a cylindrical isonormal operator: convergence is
initially only on finite families of query functions. Uniform trajectory
control requires a separate compactness/Hermite-tail theorem.

### Exact projected-gradient diagnostic

If (OG-3)--(OG-7) are discretized with one positive quadrature rule and the
backward equation is the exact discrete adjoint of the forward equation,
then the finite-\(P\) system should itself be a Euclidean projected gradient
flow. Its \(c\)-block tangent kernel is
\[
\Theta^{c,P}_{rq}
=
\gamma^2\int_0^1
\mathbb E_{x,\varepsilon}[\beta_r\beta_q]
\sum_{j<P}H_j[h_r]H_j[h_q]\,ds.
\tag{OG-11}
\]

Together with the \(a\)- and \(b\)-blocks this must give
\[
\dot f=-\Theta_Pe,
\qquad
\Theta_P\succeq0,
\tag{OG-12}
\]
to the algebraic/discretization tolerance. This is a required mutation test:
changing (OG-2), quadrature weights, or the coefficient in (OG-7) must make
the identity fail. If the actual program does not pass (OG-10)--(OG-12), it
is not standard Euclidean \(\mu\)P projected onto the stated basis.

### Additional hard gates specific to this candidate

#### OG Gate 1: projection occurs after the dense limit

Provide a derivation from the original
\(W_{ij}^0\sim N(0,\sigma_w^2/n)\) action showing (OG-9) for arbitrary
finite cavity query families. The dense finite-network reference code must
contain no Hermite factorization. The PDE process must contain no reference
width.

#### OG Gate 2: correct ordered depth limit

The target takes width first at fixed \(L\), then \(L\to\infty\). Derive the
operator system from that fixed-\(L\) causal law and only then homogenize.
Deriving it by taking an \(L\)-first law of large numbers at finite width is
not enough unless equality of the limits is independently established.

Numerically, compare against the ordered reference grid described earlier;
a joint \(n,L\) diagonal does not pass.

#### OG Gate 3: local fast-type cavity test

Equations (OG-3)--(OG-4) assume \(h_r(s,x,t)\) and \(p_r(s,x,t)\) are slow
functions of \(x\), while the persistent local layer randomness enters only
through \(\varepsilon\) and \(c(s,x,\varepsilon,t)\).

Test this directly:

- pair networks with identical \(B^0,a^0\) and independently resampled iid
  \(W^0\)'s;
- estimate the conditional variance of \(h_i(s,t)\) and \(p_i(s,t)\) given
  the base latent;
- verify that it vanishes as \(L\to\infty\), after first resolving width;
- resample one physical layer and verify its influence on the cavity
  \(h^\ell,p^{\ell+1}\) vanishes at the predicted depth rate.

If a nonvanishing fast-history dependence remains, the source latent
\(x=(B^0,a^0)\) is incomplete and the candidate must be enlarged.

#### OG Gate 4: iid Young type, not a tied depth path

The \(\varepsilon\) at different physical depths represents independent iid
layer types. It is integrated locally at each depth. Do not evolve one
smooth \(\varepsilon(s)\) path or use one particle's same random mode as a
physical identity connecting all depths.

Reusing deterministic Gaussian quadrature nodes at different depth points
is numerically fine only if the equations treat them as copies of the same
marginal integral, not as cross-depth-correlated layer identities. A
mutation that deliberately ties the layer type across depth should change a
diagnostic and be rejected.

#### OG Gate 5: fixed complete basis and correct normalization

- Freeze the Hermite multi-index order before target data.
- Orthonormalize with respect to the static standardized base law, not the
  evolving particle law.
- Use \(\varepsilon_j\sim N(0,1)\) with no ad hoc \(P^{-1/2}\).
- Verify (OG-9) for constants, linear functions, and nonlinear held-out
  functions.
- If \(A\) varies over \(\mathcal U\), use a standardized readout latent or
  explicitly account for the \(A\)-dependent base measure without changing
  the structural basis order.

#### OG Gate 6: row-dependent learned coefficients

The exact learned action is
\[
\dot W\,u
=-\gamma\sum_qe_q\,\beta_q\,\langle h_q,u\rangle.
\]
Therefore \(c_j\) must be a dynamic row field carrying the same local
\((x,\varepsilon)\)-dependence as \(\beta\). A global deterministic
coefficient \(c_j(s,t)\) would erase feature-distribution learning and is a
false closure.

Check (OG-7) by:

- finite differences of the projected loss with respect to random
  \(c_j(s,x,\varepsilon)\) degrees of freedom;
- the exact energy identity for the \(a,b,c\) metric;
- comparison of learned operator actions and transpose actions against
  large-width dense ensembles.

#### OG Gate 7: exact shared transpose

At random numerical states and held-out functions \(u,\beta\), verify the
discrete version of (OG-10) to roundoff. This test must use the same
particles/quadrature weights on both sides.

Also verify the simple Stein case and multiple-query Onsager cases against
dense Gaussian Monte Carlo. Independent resampling in (OG-2) is forbidden.

#### OG Gate 8: separate all numerical and model resolutions

Track independently:

- \(P\): operator/Hermite model resolution;
- \(N\): depth Galerkin/collocation model resolution;
- \(M\): base-\(x\) law quadrature or particle resolution;
- \(R\): fast-\(\varepsilon\) Gaussian quadrature;
- \(\Delta t\): training-time solver resolution.

Show convergence in \(M,R,\Delta t\) at each fixed \(P,N\), then show
cofinal convergence in \(P,N\). Increasing \(M\) while leaving \(P\) fixed
does not test recovery of the dense operator.

#### OG Gate 9: Hermite tail and held-out modes

At each time and depth, report
\[
\sum_{j=P_{\rm train}}^{P_{\rm check}-1}
|H_j[h_r]|^2
\]
and analogous coefficients for every slow query function used by the
operator. Use \(P_{\rm check}>P_{\rm train}\) only as an external diagnostic,
never in the drift. Verify that held-out energy and observable changes
decrease with \(P\).

This is still empirical. A proof of uniform all-time convergence would need
a uniform compactness/regularity theorem for the trajectory's query
functions.

#### OG Gate 10: full observable, restart, and plateau protocol

All general Gates 4 and 7 and Sections III--VI remain in force. In
particular:

- restart data are the current \(a,b,c\) fields/law, not a finite network or
  a stored trajectory;
- \(h,p\) are recomputed by the same forward/backward boundary solver;
- output, every-depth Gram, and the same-system tangent kernel are compared;
- fixed \(P,N\) runs continue unchanged through horizon doubling and
  plateau.

### Principal failure risks

1. **Wrong limit order.** The elegant equations may describe an
   \(L\)-first homogenization rather than the declared width-first target.
2. **Incomplete base latent.** Positive-time slow fields may retain local
   fast-history variables not measurable with respect to
   \(x=(B^0,a^0)\).
3. **Depth tying.** Carrying one \(\varepsilon\) identity along depth changes
   iid layers into tied or depth-correlated weights.
4. **False bounded-operator claim.** Gaussian white noise is cylindrical;
   operator-norm or Hilbert--Schmidt convergence of
   \(\mathcal W_P^0\) is false.
5. **Missing transpose response.** Independent transpose noise can fit
   forward curves while destroying Onsager terms and gradient dynamics.
6. **Collapsed learned state.** Population-scalar \(c_j\)'s erase the
   row-dependent rank-one updates of Euclidean feature learning.
7. **Metric mismatch.** A plausible \(c_j\) ODE with the wrong normalization
   or a non-adjoint depth discretization silently changes the optimizer.
8. **Hermite-tail leakage.** Nonlinear training can move energy to modes
   above \(P\); bounded \(\tanh\) alone does not give a uniform Hermite-tail
   theorem.
9. **Quadrature aliasing.** Underresolved \(\varepsilon\) or \(x\) quadrature
   can make low \(P\) look accurate and can break the exact adjoint.
10. **Low-rank relabeling.** Running a rank-\(P\) finite network and calling
    \(P\) “PDE resolution” fails, regardless of its curve accuracy.
11. **Reference leakage.** Selecting the Hermite order, basis rotation, or
    closure constants from exact positive-time curves reopens the oracle
    loophole.
12. **Fixed-\(P\) overclaim.** One accurate \(P\) is a successful candidate
    PDE simulation, not evidence of arbitrary-accuracy existence until a
    cofinal \(P,N\) trend is shown.

### Referee conclusion on this alternative

This construction is more directly executable than the response-word
compiler because it replaces every dense action and its transpose by one
explicit finite operator pair. It is therefore a serious strategy for the
user's requested PDE simulation.

The decisive audit identities are
\[
\boxed{
\text{Parseval covariance (OG-9)}
\quad+\quad
\text{shared adjoint (OG-10)}
\quad+\quad
\text{Euclidean loss flow (OG-12)}.
}
\]

If those identities hold, the state is width-independent, the local
fast-type/correct-limit tests pass, and convergence is shown in
\((P,N,M,R,\Delta t)\) against the ordered dense reference, then the result
is a genuine operator--Galerkin neural-PDE simulation rather than a disguised
low-rank architecture.

### Audit of the first executable prototype

I subsequently inspected
`agent_outputs/numerics/operator_hermite_pde.py`. Its current state is
\[
(b_x,\ a_x,\ c_{\ell,x,e,j}),
\]
where \(x,e\) are positive quadrature nodes and \(j<P\). It contains no
network width, no \(n\times n\) matrix, and no realized \(W\)-action. The
same `state.c` is used in the forward contraction and transpose contraction.
The code therefore passes the basic structural no-matrix/no-independent-
transpose screen.

I independently checked a small \(m=2,P=4,N=4\) instance:

- shared discrete adjoint defect:
  \(6.25\times10^{-17}\);
- directional loss derivative versus the negative projected metric norm:
  \(5.62\times10^{-11}\);
- directional output derivative versus
  \(-\Theta_Pe\):
  \(5.90\times10^{-11}\);
- tangent-kernel eigenvalues in that test:
  \((2.70624,2.70624)\).

The author then added permanent unit tests for the weighted \(b/a/c\)
gradients, shared forward/transpose adjoint, PSD tangent-kernel/output
identity, and a numerical semigroup split. All four pass locally. This is
material evidence that the prototype is an exact projected Euclidean
gradient system, not an arbitrary curve closure.

The first stored \(m=2,P=4,N=16\) curve is only a pilot. Against the larger
finite-width ensembles at fixed \(L=16\), its maximum output discrepancy is
roughly \(1.5\)--\(1.6\times10^{-2}\), and its maximum all-depth Gram
discrepancy roughly \(2.4\)--\(2.6\times10^{-2}\), comparable to the current
ensemble uncertainty. Its terminal feature motion is nontrivial. These
numbers are promising but do not yet resolve finite-\(P\) bias, finite-width
bias, or the ordered depth limit.

In particular, the code averages the local \(\varepsilon\) at every residual
step. At a genuinely fixed finite \(L\), the width-limit hidden coordinate
still carries the random innovations of earlier layers. Thus the prototype
is a discretization of the **already depth-homogenized** candidate, not the
exact fixed-\(L\) width-limit law. Matching its `depth=16` to a reference
\(L=16\) is a useful approximation check, but it does not establish the first
limit in the conjecture. The omitted conditional variance must be shown to
vanish as \(L\to\infty\), after resolving width.

The initial row-quadrature cross-check is also unresolved. At the same
\(P=4,N=16\), tensor GH\(3^4\) (81 nodes) and scrambled Sobol 256 nodes
differ by
\[
\max_t\|\Delta f(t)\|_2=9.36\times10^{-3},
\]
\[
\max_{t,s}\|\Delta G^h(s,t)\|_F=1.889\times10^{-2},
\qquad
\max_s\|\Delta G^h(s,T)\|_F=1.757\times10^{-2}.
\]
This is the same order as the current PDE-versus-ensemble discrepancy.
Therefore none of the present curve agreement may yet be attributed to
finite-\(P\) model accuracy; fast-Gaussian quadrature must be refined first.
The raw Sobol-256 nodes have mean-norm \(1.33\times10^{-3}\) and covariance
operator error \(2.17\times10^{-2}\), whereas GH\(3^4\) integrates these two
moments to roundoff. This alone can explain an \(O(10^{-2})\) Gram shift and
must be fixed or included in the numerical uncertainty.

Holding that same QMC-256 rule fixed, increasing the Hermite space from
degree one (\(P=4\)) to degree two (\(P=10\)) changes the maximum output by
\(2.75\times10^{-4}\) and the maximum all-depth Gram by
\(8.75\times10^{-4}\). This is encouraging evidence that the first four
modes capture most of this pilot trajectory, but it is not a clean
\(P\)-convergence result until the \(R\)-quadrature error is smaller.

Remaining prototype blockers are precisely:

- cofinal \(P,N\) convergence;
- base/row quadrature and time-step convergence;
- an ordered width-then-depth reference rather than fixed \(L=16\);
- fast/slow cavity and iid-depth tests;
- serialized fresh-process restarts and complete run metadata;
- \(m=3\), neighborhood, and long-horizon plateau runs.

Until those are complete, the correct label is “first genuine
width-independent operator--Galerkin PDE pilot,” not “numerical confirmation
of conjecture (38).”

---

## Final hostile code audit of `dense_mup_pde_repro`

### Scope

I inspected:

- `src/dense_pde/operator_galerkin.py`;
- `run_pde.py`;
- `run_exact_reference.py`;
- `tests/test_operator_galerkin.py`;
- every currently stored PDE trace's state schema and metadata; and
- the available serialized restart pairs.

I reran both the new PDE tests and the earlier exact-network algebra tests.
All 7 PDE tests and all 8 exact/reference-core tests pass.

### Final implementation verdict

\[
\boxed{
\text{The code genuinely simulates a width-independent finite
operator--Galerkin neural PDE.}
}
\]

This conclusion concerns the identity of the numerical object, not its
convergence to the dense width-then-depth target.

The decisive source-level facts are:

- `PDESpec` has no network-width parameter;
- `PDEState` contains only \(B\), \(a\), and
  \(c\in\mathbb R^{N\times M\times R\times P}\);
- there is no \(n\times n\) array, realized \(W\), or neuron-pair parameter;
- \(P,N\) are Galerkin/depth-model resolutions and \(M,R\) are quadrature
  resolutions;
- the forward operator and transpose use the same
  \(\sigma_w\varepsilon+c\);
- `run_pde.py` imports only the operator-PDE module and never imports or
  reads the finite-network reference;
- `run_exact_reference.py` is a separate executable which imports the
  fully dense reference model and never feeds data back into the PDE drift.

The hard-coded \(X,y,\sigma_w,A,\gamma\) in the runner are legal architecture
and dataset inputs, not fitted positive-time data.

### Independent normalization derivation

Write
\[
H_{r,p}^\ell
=
\langle\phi_p,h_r^\ell\rangle_{\mu_M},
\qquad
r_{\ell,i,\epsilon,p}
=
\sigma_w\epsilon_p+c_{\ell,i,\epsilon,p}.
\]
The code implements
\[
z_{r}^{\ell}(i,\epsilon)
=
\sum_{p<P}r_{\ell,i,\epsilon,p}H_{r,p}^\ell,
\]
\[
h_r^{\ell+1}(i)
=
h_r^\ell(i)
+
\frac{\gamma}{N}
\mathbb E_{\epsilon,R}\tanh z_r^\ell(i,\epsilon).
\]

The exact discrete adjoint is
\[
p_r^\ell(i)
=
p_r^{\ell+1}(i)
+
\frac{\gamma}{N}
\sum_{p<P}\phi_p(i)
\mathbb E_{i',\epsilon}
\left[
r_{\ell,i',\epsilon,p}
\beta_r^\ell(i',\epsilon)
\right],
\]
with
\(\beta_r^\ell=\tanh'(z_r^\ell)p_r^{\ell+1}\). This is exactly the
transpose implemented in `solve_fields`.

The standard dense Euclidean \(\mu\)P update is
\[
\dot W_\ell
=-\frac{\gamma}{n}\sum_qe_q\beta_q^\ell(h_q^\ell)^\top.
\]
Projecting its column action onto \(\phi_p\) gives
\[
\boxed{
\dot c_{\ell,i,\epsilon,p}
=
-\gamma\sum_qe_q\,
\beta_q^\ell(i,\epsilon)H_{q,p}^\ell,
}
\]
with no factor \(1/N\): the hidden learning-rate multiplier \(N\) cancels
the residual block's \(1/N\). This is the `cdot` in the code. The remaining
rates are
\[
\dot B(i)
=-\sum_qe_qp_q^0(i)x_q^\top,
\qquad
\dot a(i)
=-\sum_qe_qh_q^N(i),
\]
also exactly as implemented.

The projected metric is
\[
\|\dot a\|_{\mu_M}^2
+
\|\dot B\|_{\mu_M}^2
+
\frac1N\sum_{\ell=0}^{N-1}
\|\dot c_\ell\|_{\mu_M\otimes\nu_R}^2.
\tag{FA-1}
\]
The tangent kernel in `observe` is
\[
\Theta^P_{rq}
=
\langle h_r^N,h_q^N\rangle
+
(x_r^\top x_q)\langle p_r^0,p_q^0\rangle
+
\frac{\gamma^2}{N}
\sum_\ell
\left(
\sum_pH_{r,p}^\ell H_{q,p}^\ell
\right)
\langle\beta_r^\ell,\beta_q^\ell\rangle.
\tag{FA-2}
\]
Every block is PSD, and the exact finite-cubature identity is
\[
\dot f=-\Theta^Pe,
\qquad
\dot{\mathcal L}
=-e^\top\Theta^Pe
=-\|\dot\theta\|_{\text{metric (FA-1)}}^2.
\tag{FA-3}
\]

No normalization, \(N\)-factor, \(\gamma\)-factor, readout factor, or
transpose orientation error was found.

### Fresh independent numerical checks

I tested a nonorthogonal \(m=3\) dataset, nonunit
\((\sigma_w,A,\gamma)=(0.7,1.05,0.93)\), and a state reached after four
positive training steps. This avoids an initialization-only identity.

Individual weighted central finite differences gave:

| block | maximum absolute defect |
|---|---:|
| two \(B\) coordinates | \(1.09\times10^{-11}\) |
| one \(a\) coordinate | \(1.76\times10^{-11}\) |
| two \(c\) coordinates, including \(1/N\) metric factor | \(1.41\times10^{-11}\) |

The full directional energy test gave
\[
\frac d{d\eta}\mathcal L(\theta+\eta\dot\theta)\big|_{\eta=0}
=-2.115023533935667,
\]
\[
-\|\dot\theta\|_{\rm projected}^2
=-2.115023533936429,
\]
an absolute defect \(7.62\times10^{-13}\).

The directional output test gave
\[
\left\|
\frac d{d\eta}f(\theta+\eta\dot\theta)\big|_{\eta=0}
+
\Theta^Pe
\right\|_2
=2.36\times10^{-11}.
\]
The tested kernel eigenvalues were
\[
(2.65765,\ 2.72128,\ 2.84352).
\]

At the same generic learned state, three independent shared-transpose
pairing defects were between \(8.67\times10^{-19}\) and
\(3.47\times10^{-18}\).

Across 20 additional random datasets, hyperparameters, and deliberately
perturbed learned states:

- the smallest observed \(\lambda_{\min}(\Theta^P)\) was
  \(8.68\times10^{-3}>0\);
- the largest directional \(\dot f+\Theta^Pe\) defect was
  \(1.70\times10^{-10}\).

Thus PSD and the output identity are structural, not artifacts of the
central initialization.

### Independent implementation reproduction

The separately written
`agent_outputs/numerics/operator_hermite_pde.py` and the final
`operator_galerkin.py` agree for
\[
m=3,\quad P=5,\quad N=16,\quad
M=3^4=81,\quad R=3^5=243
\]
through \(T=1\):

| quantity | maximum common-grid difference |
|---|---:|
| every output coordinate | \(2.78\times10^{-16}\) |
| every time/depth Gram entry | \(8.88\times10^{-16}\) |

The implementations use different state conventions—one stores the total
row coefficient and one stores the learned part \(c\)—so this is a useful
independent algebra/code-path check.

### No dense-state or oracle leakage

A source and import audit found:

- no `n` model field;
- no `state.W`, `W @ u`, finite-network checkpoint, response-matrix import,
  or reference-data callback in the PDE module;
- no `dense_mup` import in `run_pde.py`;
- no file read in the PDE path except an explicitly requested PDE-state
  restart;
- no `dense_pde` import in the reference runner.

All stored current PDE states have
\[
\operatorname{shape}(c)=(N,M,R,P),
\]
exactly matching their metadata. Changing a reference-network width cannot
change the PDE state or RHS because no such input exists.

This passes the hard width-independence and reference-isolation gates.

### Restart and metadata audit

For the same static compiler and quadrature, rebuilding the quadrature in a
fresh context is byte-identical. A nine-step direct integration and a
four-plus-five-step split restart agree exactly in \(B,a,c\).

The stored direct-\(T=2\) and serialized \(T=1\to2\) traces agree at the
restart point to:

| quantity | maximum difference |
|---|---:|
| output | \(2.22\times10^{-16}\) |
| loss | \(4.45\times10^{-18}\) |
| every depth-Gram entry | \(4.44\times10^{-16}\) |
| tangent kernel | \(0\) |

The \(T=8\to32\) restart also reconstructs its \(T=8\) observables exactly.
This establishes numerical semigroup restartability for matched static
data.

The initial code accepted any restart with the same `c` shape. I constructed
a counterexample: changing only the quadrature seed while preserving all
shapes changed the immediate RHS by \(0.943\), yet was silently accepted.
This was a real integrity bug.

It has now been fixed. `run_pde.py` hashes:

- the full static architecture/compiler tuple;
- basis multi-indices;
- every quadrature node/weight array;
- the empirically orthonormal basis array.

It validates that hash and the \(B,a,c\) shapes before restart. A same-shape
wrong-seed restart now fails with
`restart static compiler/quadrature hash mismatch`. The runner also now
requires the duration to be a multiple of the sample interval, closing an
edge case where a final state at \(T\) could previously have been labeled by
the last sample time \(<T\).

New traces carry both a static-compiler hash and a complete run-config hash.
For the audited new direct/restart pair, the static hashes agree and the
start/end metadata are \(0\to0.2\) and \(0.2\to0.4\), respectively.

### Quadrature conditioning warning

Centering/whitening is fixed before training and is applied identically in
the forward and transpose. It is scientifically legal and makes the
finite-cubature gradient identities exact. It does **not** make a sparse
high-dimensional cubature accurate in higher moments.

The stored \(P=35,M=64,R=64\) trace is severely underresolved:

| block before whitening | minimum eigenvalue | maximum eigenvalue | condition number |
|---|---:|---:|---:|
| base Hermite Gram | \(0.0174\) | \(6.443\) | \(371\) |
| fast Gaussian covariance | \(0.0280\) | \(2.762\) | \(98.8\) |

Whitening maps both to the identity algebraically, but performs a large
distortion of the intended Gaussian/Hermite quadrature. Therefore:

- this \(P=35\) trace is an execution/stability stress test only;
- it is not valid evidence for \(P\)-convergence;
- its near-one `projected_energy` is not a trustworthy continuum Hermite-tail
  estimate.

For comparison, at \(P=15,M=128,R=64\), the raw base and fast condition
numbers are approximately \(2.76\) and \(3.77\). These are materially
better, but \(M,R\) refinement is still required.

Future metadata should retain raw minimum eigenvalues and condition numbers,
not only the post-whitening defects.

### Homogenization evidence

The paired-\(W\) audit now measures both forward and adjoint conditional
variance. At \(n=128\), 24 pairs per depth shared \(B^0,a^0\) and independently
redrew every dense \(W_\ell^0\). The log--log slopes versus \(L\) were:

| conditional variance | \(t=0\) | \(t=0.5\) |
|---|---:|---:|
| terminal \(H\) | \(-1.0193\) | \(-1.0039\) |
| input adjoint \(P^0\) | \(-0.9993\) | \(-0.9924\) |

This is strong direct evidence for the candidate's premise that local fast
depth randomness has \(O(L^{-1})\) conditional variance and disappears from
the slow \(h,p\) fields, including after feature learning begins.

It is still one fixed-width diagnostic. It does not prove the ordered
\(n\to\infty\), then \(L\to\infty\) homogenization theorem.

### Reference-runner audit

`run_exact_reference.py` uses the separately audited canonical dense model:

- every \(W_\ell\) is fully dense and unconstrained;
- every \(B,W,a\) block is trained;
- the rates are \(\eta_W=L,\eta_B=\eta_a=n\);
- output scaling is \(a^\top h/n\);
- the tangent kernel is the exact same-model sensitivity Gram.

The inherited finite-difference, exact-kernel, and \(K=L\) derivative tests
all pass.

Reference samples are independent seeds, and the runner records every
output, every depthwise Gram, and every tangent kernel before calculating
ensemble means and standard errors.

No scaling or reference-generation bug was found. The runner should still
add the same duration/sample-grid validation as `run_pde.py` and include
source/environment hashes in a final frozen bundle.

### What the current files do and do not establish

#### Established

- A finite width-independent PDE has actually been run.
- It is autonomous and restartable from its complete current state.
- It uses the correct shared forward/transpose operator.
- Its finite-\(P,N,M,R\) flow is exactly standard projected Euclidean
  \(\mu\)P gradient flow.
- It has a same-system PSD tangent kernel satisfying
  \(\dot f=-\Theta^Pe\).
- It shows \(O(1)\) nonlazy Gram motion and reaches a numerical plateau.
- Two independent implementations reproduce its curves to roundoff.
- The fast/slow depth-homogenization premise has unusually clean
  \(1/L\)-variance evidence.

#### Not established

- The available dense references do not yet form the required ordered grid.
  Current central files include \(n=64,L=16\) and
  \(n=96,128,L=32\), rather than several widths at every fixed depth followed
  by several depths.
- The PDE has not therefore been compared to a statistically resolved
  \(n\to\infty\), then \(L\to\infty\) observable target.
- A cofinal, well-resolved \(P,N\to\infty\) sequence has not been shown.
- The \(P=35\) run is quadrature-underresolved.
- Uniformity on the full neighborhood \(\mathcal U\) has not been tested.
- The full all-time statement and an effective error certificate remain
  unproved.
- This operator--Galerkin family is a new explicit candidate family; it is
  not an implementation of the prose-level response-word compiler from the
  original note.

### Final referee classification

| Claim | Verdict |
|---|---|
| “An actual finite neural PDE was simulated” | **Pass** |
| “It has no hidden network width or dense matrix” | **Pass** |
| “It uses standard dense Euclidean \(\mu\)P scaling after Galerkin projection” | **Pass** |
| “Forward and transpose reuse the same operator” | **Pass** |
| “It is autonomous/restartable and non-oracular” | **Pass after the restart-hash fix** |
| “Its numerical curves are internally reproducible” | **Pass at the audited low order** |
| “It has converged in all PDE solver resolutions” | **Partial; not yet** |
| “It converges to the canonical dense width-then-depth target” | **Unresolved** |
| “It validates the arbitrary-accuracy/all-time conjecture” | **No; not yet** |

The scientifically accurate headline is:

\[
\boxed{
\begin{array}{c}
\text{The central missing experiment has finally crossed the first hard
threshold:}\\
\text{a genuine, autonomous, width-independent neural PDE was actually
simulated.}\\
\text{Its dense-limit accuracy remains an open numerical question.}
\end{array}
}
\]
