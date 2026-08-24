# Post-selection independent audit

Status: arctangent contract passed after one material kernel-proof repair,
21 August 2026.

## Frozen decision

The selected activation is

\[
\phi(x)=\arctan x.
\]

The admissible state is the immutable marked two-sided Gaussian action
\(\mathfrak G=(H_R,H_C;a_0,r_0,\Gamma)\), two current vector fields
\((A,r)\), one current trace-class operator \(q\), and one physical residual
\(e\).  Every field has one training-time argument.  There is no response
kernel, second training time, growing moment list, or trajectory-dependent
source.

## Isolated selection round

Three routes received only the finite-width equations and the frozen
contract, with no project artifacts or other route outputs.

1. **Smooth bounded route.**  It independently ranked arctangent first and
   derived the natural coordinate
   \(r=u+u^3/3\), which makes \(r'=G^*B\).  It identified adaptive
   square-energy concentration in \(Q=G^*B\) as the sole unresolved bridge
   in its own proof.
2. **Piecewise-linear/homogeneous route.**  It found the exact sectorwise
   deep-linear conjugacy for \(|x|\), but also explicit open attracting-kink
   configurations for absolute value, ReLU, leaky ReLU, and hard clipping.
   No fixed value of \(\phi'(0)\) supplies a classical continuation at all
   such contacts.  A Filippov or local-time rule would change the model.
3. **Mechanism-classification route.**  It proved that a finite-dimensional
   unital algebra of continuous pointwise multipliers on a connected
   interval contains only constants.  This rules out finite scalar
   multiplier-basis closures, but explicitly does not rule out the retained
   operator state.  Its a.e.-flat sign/quantizer witness was rejected as a
   frozen-feature easier-model substitution.

These routes distinguish the quadratic obstruction from generic
nonlinearity: bounded \(\phi\) gives
\(A(s)=a_0+\alpha(s)\) with \(\alpha\) uniformly bounded pointwise, while
the quadratic equation \(A'=Z^2\) destroys that Gaussian envelope.

## Isolated proof-audit round

Three fresh routes then received the arctangent candidate in self-contained
form and no project files.

### Static source: PASS

The source auditor verified Appendix B, Theorem B.4 of Yang--Littwin's
`NETSOR^{T+}` master theorem.  It permits one fixed Gaussian matrix and its
actual transpose, adaptive normalized MOMENT scalars, jointly
pseudo-Lipschitz nonlinearities, and singular limiting query covariance.
For every fixed cutoff and fixed finite Euler mesh, elimination of the
trained operator makes the whole mesh one admissible finite program.

Projective consistency follows by putting any two finite term sets in one
common extension program.  Kolmogorov extension gives the two generated
probability spaces.  The finite inequality

\[
\|G_{0,n}v_n\|_2\le\|G_{0,n}\|_{\rm op}\|v_n\|_2,
\qquad \|G_{0,n}\|_{\rm op}\to2,
\]

then defines a bounded \(\Gamma:H_C\to H_R\), and exact finite transpose
duality gives its Hilbert adjoint.  This is an ordinary pretrajectory
projective/GNS construction, not an ultralimit and not a fresh-Gaussian
oracle.

### Raw kernel: FAIL as written, PASS after repair

The old direct Hölder mesh-removal step was invalid: its
\((2+\varepsilon)\)-moment constant could diverge as the number of Euler
steps grows.  The corrected proof uses two separate quantifier orders.

For one fixed auxiliary mesh, the finite-program high moment and

\[
q^2\mathbf1_{\{|q|>R\}}
\le4(q-v)^2+2v^2\mathbf1_{\{|v|>R/2\}}
\]

give square-tail tightness in probability for the exact continuous cutoff
trajectory.  Once that statement is established, a separate comparison
mesh is removed by truncating

\[
\{c(r)-c(r^h)\}Q^h
\]

at a fixed coordinate level \(R\), choosing \(R\) from the square-tail
statement, and only then sending the mesh to zero.  No high-moment bound
uniform in mesh size is used.  The same inequality transfers the result
through Gaussian readout-cutoff removal.  This proves uniform-on-compact
convergence in probability of the raw kernel; it does not assert convergence
of its outer expectation.

### Whole theorem: conditions discharged

The whole-proof reconstruction passed the continuum algebra,
Gaussian-envelope/Osgood uniqueness, asymmetric cutoff comparison,
trace-class closure, chain rule, negative-label clock, and restartability.
It classified the width theorem as conditional on exactly the static-source
and square-tail lemmas above.  The two dedicated audits establish those
lemmas, after the displayed repair.

## Final post-repair audit round

Three further isolated routes received the repaired theorem but no project
files or prior agent outputs.

1. **Contract audit: PASS.**  It verified that the phase space
   \(L^2_R\times L^2_C\times\mathfrak S_1(H_C,H_R)\times\mathbb R\) is fixed
   at time zero.  The immutable Gaussian action is a quenched coefficient,
   program depth is an approximation coordinate rather than a dynamical
   species, and increasing rank of the single current \(q\) does not add
   state variables.  Restarting uses only the current quadruple and the same
   realized source.  Eliminating \(q\) would create a Volterra history, but
   retaining it is a genuine Markovianization because the vector field never
   accesses a time-labelled decomposition of \(q\).
2. **Rare-tail counterexample search: PASS.**  It attacked extreme rows,
   columns, singular-vector alignment, Gaussian readout tails, vanishing-time
   layers, and the physical-clock change.  The pathwise bounds

   \[
   \sup_{|s|\le S}\|G(s)\|_{\rm op}=O_{\mathbb P}(1),
   \qquad
   \sup_{|s|\le S}\|Q(s)\|_2=O_{\mathbb P}(1)
   \]

   survive adaptive selection.  More decisively, the fixed-mesh
   \(2+\varepsilon\) moment plus the repaired square-tail transfer rules out
   a spike of height \(H_n\) and mass \(p_n\) with
   \(p_nH_n^2\not\to0\).  No canonical-iid reachable counterexample was
   found.
3. **Clean-room proof reconstruction: PASS.**  It independently recovered
   the row/column types and normalization, exact finite feature algebra,
   genuine-adjoint identity, finite-program Euler reduction, Osgood
   continuum limit, both tail quantifier orders, Gaussian cutoff removal,
   signed physical clock, and restart property.  Its only clarification was
   to read the dimension-free Euler statement in the standard ordered-limit
   sense used in the theorem: fix cutoff and mesh, send width to infinity,
   then remove the mesh and cutoff.

This round found no remaining theorem-strength dependency or circular use of
the claimed width limit.

## Final claim boundary

For canonical mutually independent Gaussian initialization and every fixed
physical horizon, the predictor, raw tangent kernel, residual, and squared
loss converge uniformly in probability to the current-state readouts of the
arctangent operator IDE.  The theorem is not a claim of operator-norm
convergence, robustness to arbitrary deterministic spike states,
finite-dimensional scalar closure, or long-time interpolation.
