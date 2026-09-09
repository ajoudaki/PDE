# Research contract

**Frozen for the exploratory probe:** 24 August 2026. A material change is
recorded as a new contract rather than silently weakening this one.

## 1. Canonical model family

Fix one unit-normalized scalar input, one label (y_\star\in\mathbb R), a
learning multiplier \(\eta>0\), equal hidden width (n), and a fixed hidden
depth (H\). On

\[
 \mathcal H_{\ell,n}=(\mathbb R^n,\langle v,w\rangle_n
 =n^{-1}v^{\mathsf T}w)
\]

let (u_n,A_n) have iid (N(0,1)) coordinates and let
(G_{\ell,0,n}=n^{-1/2}W_{\ell,n}), (1\leq\ell<H), have mutually
independent iid standard-Gaussian raw entries. Put

\[
 z_{1,n}=u_n,\quad x_{1,n}=\phi(z_{1,n}),\qquad
 z_{\ell,n}=G_{\ell-1,n}x_{\ell-1,n},\quad
 x_{\ell,n}=\phi(z_{\ell,n})
\]

and

\[
 f_n=\langle A_n,x_{H,n}\rangle_n,\qquad e_n=y_\star-f_n.
\]

Define backward fields

\[
 b_{H,n}=A_n\phi'(z_{H,n}),\qquad
 q_{\ell,n}=G_{\ell,n}^*b_{\ell+1,n},\qquad
 b_{\ell,n}=\phi'(z_{\ell,n})q_{\ell,n}.
\]

The parameter metric is part of the model. The endpoint blocks (A_n,u_n)
use the normalized Hilbert metrics \(\langle\cdot,\cdot\rangle_n\), while
each effective action (G_{\ell,n}) uses the ordinary Frobenius metric. The
exact feature-gradient vector field in this product metric is

\[
 A_n'=x_{H,n},\qquad u_n'=b_{1,n},\qquad
 G_{\ell,n}'=b_{\ell+1,n}\otimes_n x_{\ell,n},
\tag{1.1}
\]

where ((b\otimes_nx)v=b\langle x,v\rangle_n). Exact physical full-MSE
flow is (2\eta e_n) times (1.1), and

\[
 K_n=\|x_{H,n}\|_n^2+
 \sum_{\ell=1}^{H-1}\|b_{\ell+1,n}\|_n^2\|x_{\ell,n}\|_n^2
 +\|b_{1,n}\|_n^2,
\quad \dot e_n=-2\eta e_nK_n.                 \tag{1.2}
\]

Equivalently, the endpoint velocities are (n) times their ordinary
Euclidean coordinate gradients, whereas the effective matrix velocities are
their ordinary Frobenius gradients. A literal all-block Euclidean
\(n\nabla f_n\) is **not** the model and would make the matrix contribution
to the kernel order (n). No layer, readout, or gradient is frozen. Depth
always means the number of nonlinear hidden vectors, so the first matrix
action appears at (H=2).

## 2. Validation classes

- **Linear ladder:** \(\phi(x)=x\), (H=1,2,3).
- **Generic shallow gate:** (H=1) and
  \(\phi\in\mathcal A_{\rm sh}\), where
  \(\phi\in C^2(\mathbb R)\), \(\|\phi'\|_\infty+
  \|\phi''\|_\infty<\infty\), and
  \(|\phi(x)|\le C(1+|x|)\). This class is activation-generic and contains
  all standard bounded smooth activations as well as identity.
- **Nonlinear action gate:** \(\phi(x)=\arctan x\), (H=2).
- **Unresolved target:** the same unscaled arctangent, (H=3).

The generic shallow theorem may later be enlarged, but a narrower theorem is
not reported as covering an unspecified “generic activation.”

## 3. Required limiting object and observables

The permitted limit is a deterministic isomorphism class consisting of a
fixed, initialization-only pointed Gaussian action source; finitely many
current one-time fields; finitely many current trace-class action
perturbations; and the scalar residual. It must be autonomous and
restartable. Prediction, every raw block-gradient energy, (K), residual,
and loss must be current-state readouts.

For every fixed (T<\infty), the theorem must give full-sequence convergence
in probability, uniformly on ([0,T]), of (f_n,K_n,e_n,e_n^2). At the
three-hidden-layer target it must also meet the current-action/nuclear
topology of the frozen D3 contract. The width limit precedes any long-time
limit. No all-time width-uniform assertion or convergence rate is required.

## 4. What the calculus itself must establish

For each stage the calculus, not an imported model-specific proof, must
produce:

1. the exact finite-width typed program and its normalization;
2. the immutable limiting source and current-state equation;
3. an explicit solution/envelope class and well-posedness theorem;
4. fixed-mesh finite-program identification;
5. a mesh- and cutoff-uniform error certificate that removes all proof
   auxiliaries; and
6. compact-time convergence of all named raw observables.

Agreement with a previously proved formula is a regression test, not a proof
step.

## 5. Non-ad-hoc rule

A rule is reusable only if its statement is quantified over a declared IR
type or activation/envelope class and its proof uses only that type's
certificates. Its constants may depend on fixed depth, horizon, activation
bounds, label, and learning multiplier, but not on the model name, width,
mesh after removal, a future trajectory, or a closed form known in advance.

The following old solution devices are forbidden as axioms:

- the depth-two linear spectral invariant;
- the depth-three linear cyclic/free trace lift;
- the arctangent coordinate change stated only for one selected layer;
- a depth-two cutoff theorem whose assumptions already encode its orbit; and
- the depth-three middle-query tail or multi-cavity estimate.

They may reappear only as outputs of generic rules, and no stage may need a
new rule whose statement is just that stage's theorem in different notation.

## 6. Promotion gates

| Gate | Required certificate |
|---|---|
| G0: syntax | Type checking, exact scaling, adjoints, outer products, and raw kernel identity |
| G1: source | Full-sequence fixed-program law, bounded actions, genuine adjoints, non-oracular provenance |
| G2: internal flow | Current-state equation, local/global well-posedness, restartability, exact readouts |
| G3: discrete identification | Every fixed Euler/Picard truncation identified by the source theorem |
| G4: uniformization | Dimension-free mesh/cutoff error production and propagation; no theorem-strength hidden lemma |
| G5: direct limit | Uniform compact-time convergence of state signatures and every raw observable |

Failure of any gate blocks promotion to the next validation model. A
conditional implication is recorded but does not pass.

## 7. Anti-escape clauses

The following do not resolve a stage:

- a Taylor jet, fixed time grid, predictor-only limit, expectation-only
  result, or subsequence;
- a width-dependent atomic source, growing history, response kernel, or
  two-time state;
- clipping or normalization left in the final equation;
- changing activation, architecture, parameter metric, optimizer, or limit
  order;
- assuming uniform integrability, propagation of chaos, low influence, or a
  tensor-program limit with the desired continuous-time conclusion;
- hiding an arbitrary trajectory or full finite state in a real coordinate,
  source representative, or “closure operator”; or
- calling a reduction progress when its missing lemma is equivalent in
  strength to the original stage.

## 8. Terminal outcomes

The probe terminates a route with one of four exact outcomes: passed stage;
falsified calculus rule; blocked route with a precise reopen condition; or a
canonical counterexample to the stage theorem. Empirical evidence can
select among routes but cannot change these proof statuses.
