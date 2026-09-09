# Clean-slate hostile audit 01

**Date:** 24 August 2026.  
**Provenance:** isolated agent given only a self-contained model prompt; it
was forbidden to inspect the repository or other agents.  
**Claim level:** adversarial route audit, not a theorem about the canonical
D3 orbit.

## 1. Accepted correction

The prompt's shorthand “feature vector field (n\nabla f)” admits a literal
all-block Euclidean reading. Under that reading,

\[
 \nabla_G f_n=n^{-1}b x^{\mathsf T},\qquad
 n\|\nabla_Gf_n\|_F^2
 =n^{-1}\|b\|_2^2\|x\|_2^2=\Theta(n),
\]

so the claimed order-one raw kernel is impossible. The canonical project
model instead uses normalized endpoint Hilbert metrics and the ordinary
Frobenius metric on each effective matrix action. Then

\[
 \operatorname{grad}_G f_n=b\otimes_nx=n^{-1}b x^{\mathsf T}
\]

and its squared Frobenius norm is the intended order-one term. The frozen
research contract has been clarified accordingly. This is a wording repair,
not an architectural change.

## 2. Mandatory hostile regression tests

The audit supplied the following examples. Every future “fresh Gaussian,”
state-sufficiency, response, or compactness rule must survive them.

1. **Adaptive transpose query.** If (x=G^{\mathsf T}v), then (x) may have
   the same marginal Gaussian law as an independent vector, while
   (n^{-1}v^{\mathsf T}Gx=n^{-1}\|G^{\mathsf T}v\|^2\) has a different
   limit. Marginal Gaussianity never licenses independence.
2. **Fixed query versus adaptive supremum.** Fixed deterministic unit queries
   see the variance-one law, whereas the top singular query sees the edge
   near two. A fixed-program theorem is not mesh-uniform control of an
   adaptive query class.
3. **Weak versus square observables.** Weak field convergence does not imply
   convergence of its norm or the raw tangent kernel. Strong energy/UI must
   be proved separately.
4. **Nearly singular query Grams.** Adjacent mesh queries can have a Gram
   eigenvalue of order (h^2). Gaussian regression must be phrased through
   projections or Moore--Penrose geometry, not a uniform inverse-Gram bound.
5. **Repeated Wishart loops.** Reuse of (G,G^*\) generates all powers of
   (G^*G). A finite local Onsager subtraction cannot be declared complete;
   order-one returns must be resummed nonperturbatively.
6. **Hilbert--Schmidt versus nuclear control.** A sequence of finite-rank
   operators can have bounded Hilbert--Schmidt norm and escaping trace norm.
   Current nuclear tails require the explicit Riemann-rank estimate, not
   aggregate energy alone.
7. **Error production versus propagation.** Stability of a retained system
   is useless without a small omitted source, and a small local defect is
   useless without a mesh-uniform propagator.

## 3. Audit conclusions not promoted

The agent argued that an exact nonlinear calculus must retain an explicit
history/response state and that finite-rank mesh updates need not have a
trace-class continuum limit. Those statements are valid warnings for a
generic Volterra construction but do not refute the current-state operator
contract:

- (P_\ell(t)) is the Bochner integral of rank-one velocities with an
  explicit integrable trace norm, so its trace-class property is a separate
  theorem rather than a finite-rank inference; and
- the current operator (P_\ell(t)) may encode the action of all past
  updates extensionally without exposing a time-indexed decomposition.

Accordingly these are recorded as **major competing objections**, not fatal
results. A later state-sufficiency/restart audit must decide them in the
actual calculus topology.

## 4. Promotion impact

- G0 wording was corrected.
- G1--G5 remain unchanged.
- The seven examples above are now compulsory tests for the linear transfer
  lemma, the nonlinear one-action theorem, and the dynamic excursion rule.
- No D3 theorem claim was upgraded or downgraded.

