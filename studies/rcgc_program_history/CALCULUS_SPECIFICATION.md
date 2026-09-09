# Calculus specification, version 0.2

This file defines the proposed machinery before the validation proofs are
credited. “Rule” below means a proposed rule schema; its soundness status is
tracked separately in the evidence ledger.

## 0. Two semantic levels

The calculus now distinguishes objects that may occur in the final IDE from
objects used only to prove convergence.

The **final current-state language** is exactly the frozen contract:
immutable pointed Gaussian actions, current \(L^2\) fields, current
trace-class perturbations, scalars, and current coordinate functional
calculus. A final theorem may not retain an Euler mesh, a growing query
history, a covariance/response kernel, or a second time coordinate.

The **proof language** may additionally contain finite query histories,
two-time covariance charts, causal response measures, cavity derivatives,
and promoted traffic words. Every such object must be eliminated from the
final state after it has certified convergence of the current-state
readouts. Calling a response/history process the final autonomous IDE does
not pass the contract.

## 1. Typed intermediate language

The IR has three kinds of objects.

### Static source objects

- `Mark[l,p]`: a coordinate field in (L^p(\Omega_l));
- `GaussAction[l->m]`: an immutable bounded Gaussian action
  \(\Gamma:H_l\to H_m\) with a typed true adjoint;
- `Moment[U_1,...,U_k]`: a normalized scalar inner product or coordinate
  moment of typed fields; and
- `SourceProgram`: a finite acyclic expression made from marks, actions,
  adjoints, coordinate maps, and moments.

### Current objects

- `Field[l,p]`: a current one-time coordinate field;
- `Nuclear[l->m]`: a current trace-class perturbation (P);
- `Action[l->m]`: the split action (G=\Gamma+P);
- `Scalar`: a current scalar such as residual or Gram;
- `RankOne[b,x]`: (b\otimes x), with
  \(\|b\otimes x\|_1=\|b\|_2\|x\|_2\); and
- `CausalIntegral[V]`: the present value (\int_0^tV(s)ds), stored
  extensionally as a current field/operator, never as an inspectable history.

### Certificate objects

- `WidthGrade`: free-index count minus covariance/normalization cost;
- `Envelope[p,omega]`: moment, Orlicz, or Osgood tail control;
- `Influence[S->U,q]`: a first or higher source-block response bound;
- `ResponseKernel[tag]`: an order-one same-source return resummed as a
  causal linear propagator; and
- `Defect[k]`: an unresolved off-diagonal source excursion count.

The proof-only certificate language is enlarged by:

- a covariance type for deterministic two-time charts;
- a response type for finite signed causal response measures, with a
  permitted atom at the current time;
- a traffic type for a centred degree-zero multi-edge operator component
  that has not reduced to scalar covariance/response data; and
- a history-signature type for a finite query transcript used by exact
  Gaussian conditioning at one fixed discretization.

Finite-width and limiting expressions have identical types. Their
semantics differ only in whether fields are empirical vectors and matrices
or elements/actions of probability Hilbert spaces.

## 2. Exact compilation rules

`Forward`, `Reverse`, and `Gradient` compile the architecture syntax to the
fields (z,x,b,q), the rank-one block velocities, and the raw tangent kernel.
These rules are just chain rule plus the declared Hilbert metrics and are
exact before any limit.

`SourceSplit` rewrites every trained Gaussian action as

\[
G(t)=\Gamma+P(t),\qquad
\dot P(t)=\text{a finite sum of typed rank-one velocities}. \tag{2.1}
\]

It is architecture-generic: it applies to every trained dense Gaussian
block. `NaturalCoordinate` may be applied when a scalar gate has one sign
and

\[
\Theta'(z)=1/\phi'(z)                                  \tag{2.2}
\]

defines a global diffeomorphism with declared seed and multiplier envelopes.
The compiler proves the transformed equation by the ordinary chain rule and
records every new envelope obligation. Thus arctangent's

\[
\Theta(z)=z+z^3/3
\]

is an instance, not a primitive.

`ScalarLossClock` is available for every one-sample squared-loss model. If
(V) is the unit feature-gradient field, physical flow is
(\dot S=2\eta eV(S)). The proof-only clock

\[
 s(t)=2\eta\int_0^te(\tau)d\tau                         \tag{2.3}
\]

gives (S(t)=\widehat S(s(t))), where
(\partial_s\widehat S=V(\widehat S)), and

\[
 \dot s=2\eta\{y_\star-F(s)\},\qquad F'(s)=K(s)\ge0.  \tag{2.4}
\]

This is a generic exact rewrite on the maximal feature-flow interval, not an
external time forcing. Feature flow need not be global: the linear ladder
already blows up in finite unit feature time for every \(H\ge2\). A proof
using this chart must show that the physical clock stays in a compact
subinterval of the maximal feature domain. Alternatively it may work
directly in physical time, as the common linear theorem does. In either case
the final state remains the autonomous physical state and residual, and the
clock must disappear from the final state.

## 3. Fixed-program Gaussian semantics

For any fixed acyclic `SourceProgram`, `GaussianPeel` conditions on the
highest unused Gaussian block, enumerates equality partitions, and applies
the exact Wick--Stein partial-matching identity. Width grades are computed
only after all lower boundary indices created by Stein differentiation are
known. The output is a deterministic joint law of finitely many source
programs with all forward/adjoint correlations retained.

The proposed source theorem has two versions:

1. `PolynomialPointedSource`: fixed rooted words in independent Ginibre
   actions and Gaussian endpoint marks converge jointly, with operator-norm
   tightness. This is sufficient for the entire linear ladder.
2. `NonlinearFiniteProgramSource`: fixed pseudo-Lipschitz action programs
   converge jointly in the required empirical (W_2) signatures. This is
   the nonlinear fixed-mesh backend and may be discharged by a rigorously
   applicable unrestricted tensor-program theorem or by direct sequential
   Gaussian conditioning.

Neither theorem contains a growing mesh or continuous-time conclusion.

## 4. Causal time compilation

For a fixed Euler mesh (h), `Unroll[h,N]` produces a finite acyclic
program, so fixed-mesh identification follows from Section 3. Continuous
time requires two logically separate certificates.

### Error production

On a stopped envelope ball, `LocalDefect` must prove

\[
\|S(t+h)-S(t)-hV(S(t))\|_{\mathsf X}
\le C h^2                                             \tag{4.1}
\]

or an Osgood analogue, in a state norm/topology that controls every named raw
observable. Constants must be independent of width and cutoff.

### Error propagation

`CausalStability` must prove a mesh-independent Lipschitz or Osgood estimate
for two current states driven by the same immutable source. Combining it
with (4.1) gives an (O(h)) global mesh error. Stability without a small
source defect, or a defect estimate without propagation, does not pass.

## 5. Renormalized dynamic Gaussian rules

Naive iteration of Wick--Stein at a growing number of time nodes creates
order-one returns when a queried field feeds back through the same Gaussian
row/column. `DiagonalReturn` therefore does **not** assign these loops a
negative width grade. It collects all repeated returns with the same tagged
source block into a causal linear response equation

\[
R=R^{\rm in}+\mathcal K\star R                         \tag{5.1}
\]

and replaces them by the resolvent of (I-\mathcal K\star\), once a generic
resolvent certificate has been proved.

Only after this resummation does `ExcursionCharge` grade remaining passages
between distinct private Gaussian blocks. A proposed dynamic low-influence
theorem must show that every unresolved excursion pays its nominal
(n^{-1/2}) carrier, jointly for distinct tags and moments up to
(q\lesssim\log n). The rule is invalid if its proof assumes the target
query tail or differentiates a concentration constant containing the same
response.

The desired generic certificate has the schematic form

\[
\mathbb E\prod_{a=1}^k
  \big(n\|D_{g_j}U\,e_{i_a}\|_2^2\big)^{m_a}
\le K_T^M\exp\!\left(C_T\sum_am_a^2\right),
\quad M=\sum_am_a\le c_T\log n.                       \tag{5.2}
\]

Equation (5.2) is presently a target theorem, not an accepted rule. To be
calculus-level it must be quantified over a structural IR class and proved
by induction on causal action blocks, not asserted for the depth-three
network alone.

### 5.1 Exact conditional Gaussian channel

For one frozen source matrix, suppose a finite transcript contains right
queries \(V\), left queries \(W\), and answers \(Y=GV\), \(Z=G^*W\).
The exact finite conditional law is

\[
 G\mid(Y,Z)=M+P_W^\perp\widetilde G P_V^\perp,
\]

\[
 M=Y(V^*V)^+V^*+W(W^*W)^+Z^*P_V^\perp .
\]

This is an exact proof rule at fixed finite query depth. Degenerate Grams
are interpreted on the quotient by zero-norm query directions. This rule
does not supply bounds uniform in a growing transcript.

### 5.2 Causal response rewrite

For forward channels \(V^\alpha\) and transpose channels \(W^\beta\), the
formal continuum rewrite is

\[
 G_e^0V^\alpha(t)\rightsquigarrow
 \Xi_{e,+}^\alpha(t)+
 \sum_\beta\int_{[0,t]}W^\beta(s)
 \mathbb E[D_{e,-,\beta,s}V^\alpha(t)],
\]

with the transpose analogue. The response is measure-valued because
same-time Stein terms can be nonzero. The source derivative holds the
macroscopic covariance chart fixed.

This rewrite becomes a sound rule only after a cavity remainder theorem,
conditional covariance/Lindeberg certificate, and mesh-uniform response
bound have been proved.

### 5.3 Degree-zero registry

After Wick centring, glue two replicas of every proposed remainder and
perform the full equality-partition/free-index count.

- negative glued degree may be charged as a vanishing defect after its
  moment bound is proved;
- zero glued degree must reduce to an existing scalar/response object or be
  registered as a traffic promotion; and
- positive degree rejects the proposed scaling.

No centred zero-degree term may be discarded merely by invoking
“asymptotic Gaussianity.”

At depth three the current compiler emits, before learned/strict-time
terms, the nested operator

\[
 D_1G_2^{0*}D_2G_3^{0*}E_3G_3^0D_2G_2^0D_1,
\]

whose edge word is \(2^-3^-3^+2^+\). Its nonvanishing and its semantic
meaning have now been separated by an independent audit. Writing

\[
 B=G_3^0D_2G_2^0D_1,
\]

the word is \(B^*E_3B\), and its centred gluing has generically order-one
normalized Hilbert--Schmidt mass. It therefore cannot be discarded as a
negative-grade defect. Its first gluing is encoded by a two-copy first
tangent susceptibility, but no theorem yet shows that a finite second-order
response state determines every mixed word required by the D3 proof. Nor
does nonvanishing alone prove that a new traffic operator is necessary.
See `arctan_l3/TWO_COLOUR_FRONTIER_AUDIT.md`.

### 5.4 Quantitative Osgood-tail certificate

The D3 execution falsifies continuity of the middle multiplier on bounded
\(L^2\) sets. It also falsifies every shortcut that replaces \(L^2\) by one
fixed \(L^p\): the best generic multiplier modulus is Hölder with exponent
below one and is not Osgood. Nor is a Gaussian action uniformly bounded on
arbitrary source-dependent \(L^p\) inputs.

The source split gives the sharper identity

\[
 Q_2=\Gamma_3^*B_3+q_3^*B_3.
\]

The learned term is bounded on compact time by its rank-one-history
representation. A proposed `OsgoodTail` certificate must therefore control
the dependent immutable-action term and its tangent returns. A sufficient
form is

\[
 \sup_{n,\pi,t\le T}
 \|Q_2^\pi(t){\bf1}_{\{|Q_2^\pi(t)|>R\}}\|_2
 \le C_T(1+R)e^{-c_TR}.                               \tag{5.3}
\]

It would imply

\[
 \|Q_2\{d(Z)-d(\widetilde Z)\}\|_2
 \le C_T s\log(e/s),qquad s=\|Z-\widetilde Z\|_2,
\]

an Osgood modulus. Equation (5.3) is a target theorem, not an accepted
rule. It must be proved uniformly in the Euler mesh without first assuming
exact/Euler comparison. See `arctan_l3/D3_CALCULUS_EXECUTION.md`.

## 6. Termination and promotion

Syntactic compilation terminates because the architecture, fixed mesh, and
each source program are finite. Renormalized compilation terminates only if:

1. all order-one returns fall into finitely many response-kernel types per
   layer;
2. the response resolvents have mesh-uniform bounds;
3. every non-resummed connected excursion has strictly negative total width
   grade after equality partitions; and
4. the envelope grammar is closed under the coordinate maps and weighted
   products actually generated by the vector field.

These are theorem obligations. Finite notation alone is not termination of
the proof.

## 7. Current expected stage behavior

- Linear fixed depth should use only `PolynomialPointedSource`,
  `SourceSplit`, ordinary Banach-space stability, and energy control. No
  response renormalization is needed.
- Generic (H=1) should use only a mark source, `ScalarLossClock`, and a
  uniform characteristic-law rule.
- Arctan (H=2) is represented by a theorem over the frozen
  tame-natural-gate class. It adds `NaturalCoordinate`, Gaussian-envelope
  Osgood stability, fixed-program source semantics, raw-square uniform
  integrability, and cutoff removal.
- Arctan (H=3) is the first stage requiring `DiagonalReturn` plus a proved
  local correlated-multiplier/gluing rule. The earlier proposal to assume
  that the state and its first two variations were uniformly Cauchy across
  meshes has been rejected as circular: that is already the hard global
  uniformization theorem. The replacement must control one synchronized
  Euler increment by a linear/Osgood discrepancy plus a width remainder
  multiplied by the step size. Cross-mesh Cauchy must then be **derived** by
  discrete Grönwall/Bihari. If finite response differentiation generates an
  unavoidable higher hierarchy, the surviving degree-zero words force a
  traffic promotion. The old middle-query obstruction and the emitted
  two-colour word are direct soundness tests of the calculus, not lemmas the
  specification is allowed to assume. See
  `arctan_l3/SECOND_ORDER_REDUCTION_HOSTILE_AUDIT.md`.
