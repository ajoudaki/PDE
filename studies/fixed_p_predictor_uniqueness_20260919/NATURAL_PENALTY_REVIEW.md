# Informed internal review of the fixed-projection penalty route

2026-09-19. **Verdict: PASS for the stated continuous-time candidates and
bounded regular tangent-noise class.** No substantive mathematical correction
is required. This is an informed internal check, not an isolated review or a
promotion review.

The reviewer read the complete 607-line `NATURAL_PENALTY_ROUTE.md` and used only
the assigned `MODEL_AND_GEOMETRY.md`, `CANONICAL_FEATURES.md`, and elementary
derivations. The original input files had already been read completely and
their hashes were verified unchanged before this check. No other scientific
source, study, experiment, parallel report, or agent-list tool was retrieved
for this review. The reviewer previously authored the natural-noise
obstructions route, so this review makes no independence claim. Only this
report was written; the candidate and Git index were not changed.

Frozen input SHA-256 values:

- `NATURAL_PENALTY_ROUTE.md`:
  `1c2a1d2a9dc217ba61af75fc66768e48044f7686ce7725bd4ed81d9c7ef17416`.
- `MODEL_AND_GEOMETRY.md`:
  `d3ed7af3baadbb55e190e2423f0751b11da5ba24ef0c8fcc5c47f627ef57ff89`.
- `CANONICAL_FEATURES.md`:
  `5eab1371afaca04719bcd78a88c586f33042a008a28bbf1f3a07f0a0f6075b91`.

## What passes, and the exact interpretation

For every finite compatible circle dataset in the assigned exact order-one
population model, the explicit penalties produce a unique interpolating
endpoint inside an explicitly invariant neighborhood. Every admitted bounded
tangent perturbation has the same endpoint and the same proved exponential
upper bounds. The Hilbert metric, trained middle matrix, and its actual
transpose are retained.

The objective driving the flow is deliberately changed. Candidate A returns
the hidden state to \(h_0\), and its endpoint is the minimum-norm interpolant
for the initial features. Candidate B adds \(\varepsilon J(h)\), selects a
possibly changed hidden state, and chooses the unique interpolating readout
in the **initial** readout span. The latter is generally not the minimum-norm
readout in the final feature space. These qualifications are necessary and
are already acknowledged in the candidate.

The monotone quantity is \(U\), not necessarily the original loss \(L\).
The proved statement is
\(L(t)\le (U(S_0)-U_*)e^{-2\mu t}\); this permits temporary increases in
\(L\) beneath that envelope. The phrase “exponentially decaying loss” should
be understood in this precise sense whenever the result is summarized.

## 1. Initial-span invertibility and exact interpolation

The canonical-feature input gives \(K_0>0\) after compatible constraints
are merged. Since \(\|A_0\|\le1\), its smallest eigenvalue satisfies
\(0<\sigma\le1\). On \(\operatorname{ran}Q_0\), the isometry
\(E_0=A_0^*K_0^{-1/2}\) gives
\(\|A_0q\|\ge\sqrt\sigma\|q\|\).

The candidate's radius gives

\[
\|A_h-A_0\|\le a_1R\le\sigma/8\le\sqrt\sigma/2.
\]

Therefore \(A_h\) restricted to this fixed \(m\)-dimensional initial span
has lower bound \(\sqrt\sigma/2\). It is injective, hence bijective onto
\(\mathbb R^m\), with inverse norm at most \(2/\sqrt\sigma\).
This verifies equation (6) without assuming that the initial and current
feature spans coincide.

Consequently, for every hidden state in the ball, the conditions
\(A_hc=Y\) and \(P_0c=0\) have exactly one simultaneous solution. This
is the key reason the fixed nullspace penalty can vanish at an exact fit
even for Candidate B. It would be incorrect to replace this solution with
the final-space minimum-norm interpolant, but the candidate does not do so.

## 2. Strong convexity and constants

I checked the residual Hessian estimate using only derivatives along
one-dimensional segments. Since the residual is finite-dimensional and
its derivative is Lipschitz, its second segment derivative exists almost
everywhere. No unsupported second Fréchet derivative of an \(L^2\)
Nemytskii map is needed.

The principal estimates in equations (7)--(10) are valid:

\[
|A_hd|^2+2\|P_0d\|^2\ge\frac\sigma4\|d\|^2,
\]

and

\[
L''\ge |A_hd|^2
 -(2a_1^2C^2+2Ea_3C)\|v\|^2
 -4Ea_1\|v\|\|d\|.
\]

For the first inequality, write
\(A_hd=A_0Q_0d+(A_h-A_0)d\) and use
\(|x+y|^2\ge |x|^2/2-|y|^2\). The resulting coefficients of the
orthogonal \(Q_0\) and \(P_0\) components exceed \(\sigma/4\), because
\(a_1^2R^2\le\sigma^2/64\le\sigma/4\).
For the second inequality, differentiate \(|e|^2\), use the stated bound
on \(e''\), and use
\(2|x+y|^2\ge |x|^2-2|y|^2\).

The cross term is correctly absorbed by

\[
4Ea_1\|v\|\|d\|
 \le\frac\sigma8\|d\|^2
       +\frac{32E^2a_1^2}{\sigma}\|v\|^2.
\]

The explicit \(\rho\) exceeds every negative hidden coefficient, including
\(\varepsilon C_J\), by more than one. Since
\(\mu=\sigma/8\le1/8\), the asserted product-space lower curvature
\(\mu\) follows. Integrating the almost-everywhere segment inequality
proves strong convexity on the whole open convex domain \(\Omega\).
No assertion of convexity of a nonlinear sublevel set is being used.

The stated \(L_U\) and \(G_U\) are conservative valid bounds. In particular,
the residual derivative has Lipschitz constant at most
\(a_3C+2a_1\), and subtracting the two factors in
\(\nabla L=2(De)^*e\) gives the displayed gradient bound. These constants
are sufficient for the later Hilbert-space existence argument.

## 3. Construction and uniqueness of the target

The map
\(h\mapsto h_0-(\varepsilon/\rho)\nabla J(h)\) strictly maps the
closed \(R/2\) hidden ball into itself and has Lipschitz constant below
one. The two necessary inequalities follow separately from
\(\rho>2\varepsilon G_J/R\) and \(\rho>\varepsilon C_J\).
The geometric-series argument for successive iterates supplies a fixed
point in the complete closed Hilbert ball.

The scalar hidden objective
\(F=\rho\|h-h_0\|^2/2+\varepsilon J(h)\) is strongly convex in the
radius-\(R\) ball with lower curvature \(\rho-\varepsilon C_J>0\).
Thus this fixed point is its unique minimizer there. Combining it with
the fixed-span inverse from Section 1 gives the claimed \(c_\dagger\),
with norm at most \(2/\sqrt\sigma<C\). Both readout penalties vanish
at this constructed point, so it is a critical point of the full objective
inside \(\Omega\).

This proves both inequalities required by the dynamics:

\[
U-U_*\ge L+\|P_0c\|^2,
\qquad
\|\nabla U\|^2\ge2\mu(U-U_*).
\]

The first uses minimization of \(F\) throughout the hidden ball, not just
stationarity. The second follows directly from strong convexity with the
constructed target as the comparison point. There is no circular use of a
future flow limit to establish either inequality.

For Candidate A, \(\varepsilon=0\) forces \(h_\dagger=h_0\), and the
readout is \(A_0^*K_0^{-1}Y\). The global nonnegative objective has no
other zero: all three nonnegative terms must vanish, fixing the hidden
state and the readout in its initial span. Local strong convexity is all
that is needed for the stated trajectory theorem.

## 4. Noise regularity, confinement, and infinite time

Equation (21) defines a legitimate bounded, locally Lipschitz tangent
forcing. Its undivided numerator is
\(\|g\|(I-\hat g\otimes\hat g)z\), so its norm is at most \(\|g\|\).
The homogeneous term
\(g\langle g,z\rangle/\|g\|\), extended by zero, is at most
\(3\)-Lipschitz; adding \(\|g\|z\) and dividing by \(1+\|g\|\)
gives the stated conservative \(5b\) bound. At zero gradient the formula
vanishes continuously. Thus the singular unregularized projection problem
has actually been repaired, not hidden in a definition at the minimizer.

For any admitted strongly measurable time dependence, local solutions can
be constructed by contraction of the Bochner integral equation. State
Lipschitzness on bounded time intervals and the uniform bound on the vector
field are sufficient. The ordinary chain rule for absolutely continuous
solutions gives the exact identity

\[
\frac{d}{dt}U=-\|\nabla U\|^2
\]

almost everywhere, because the forcing is tangent to the **full** objective.
This is a pathwise random-ODE statement. It is not an Itô diffusion result,
and neither ordinary SGD noise nor arbitrary additive noise is covered.

The energy bounds give the strict margins
\(\|h-h_0\|<R/2\) and \(\|c\|\le C-1\). The readout estimate correctly
uses the inverse on the initial span:

\[
\|Q_0c\|\le\frac2{\sqrt\sigma}
   (|A_hc|+|A_hP_0c|)
 \le\frac{2(1+2\sqrt W)}{\sqrt\sigma}.
\]

Consequently no coordinate can reach the boundary of \(\Omega\).
The bound \(\|\dot S\|\le G_U+b\) makes the trajectory Cauchy at every
finite putative maximal time. Its Hilbert-space limit remains strictly in
the domain and supplies initial data for continuation. This correctly
proves global existence without using compactness of bounded
infinite-dimensional balls.

The energy identity and the verified gradient inequality yield equation
(25), including exponential convergence in the original state norm.
The uniform-in-input feature derivative bound then proves (27), so the
entire predictor on the circle converges to the same function for every
admitted noise realization. Arbitrary finite amplitude is compatible with
this proof because tangency preserves exactly the same energy identity.

## 5. Candidate B's learned geometry and the loss qualification

For \(\varepsilon>0\), the critical-point equation makes
\(h_\dagger=h_0\) equivalent to \(\nabla J(h_0)=0\). When that gradient
is nonzero, a small step against it lowers \(F\), so
\(F(h_\dagger)<F(h_0)\). Subtracting the nonnegative anchor penalty gives
\(J(h_\dagger)<J(h_0)\). Thus the feature Gram matrix really changes;
this is not merely movement in a parameter symmetry.

The one-representative proof of nonvanishing is valid. Scaling the actual
initial middle matrix by \(1+s\) yields

\[
K'(0)=2E[z\tanh z\operatorname{sech}^2z]>0.
\]

Here \(K(0)>0\) guarantees positive probability of \(z\ne0\), on which
the integrand is strictly positive. Boundedness of \(z\) justifies
differentiation. Therefore the derivative of \(J=1/(2K)\) is negative.
The candidate correctly leaves universal nonvanishing for larger datasets
unproved. It also correctly makes no generalization-benefit claim.

One presentation qualification should remain explicit in any synthesis.
Writing \(U=L+R\), the original loss satisfies

\[
\dot L=-\|\nabla L\|^2
        -\langle\nabla L,\nabla R\rangle
        +\langle\nabla L,\xi\rangle.
\]

Neither of the last two terms has a fixed sign, and tangency to \(\nabla U\)
does not imply tangency to \(\nabla L\). Accordingly the theorem proves
an exponential envelope for \(L\), not monotonicity of \(L\). This does
not undermine any displayed bound or endpoint statement in the candidate.

## Disposition

No required mathematical corrections. The candidate establishes its stated
modified-optimizer theorem. Its practical and scientific boundaries remain:
dataset-dependent possibly very large penalties; initial terminal geometry
for A; a current Gram inverse and an initial-span readout selector for B;
bounded regular forcing tangent to the selected objective; and no automatic
extension to Brownian noise, SGD, discretization, finite quadrature,
finite-width dynamics, or the unmodified physical loss flow.
