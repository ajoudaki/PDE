# Protocol: nonlinear three-hidden-layer autonomous operator IDE

Status: finite model and research contract frozen before activation selection,
22 August 2026.

## 1. Canonical finite model

For \(j=1,2,3\), let
\[
H_{j,n}=(\mathbb R^n,\langle v,w\rangle_{j,n}=n^{-1}v^{\mathsf T}w).
\]
The trainable parameters are
\[
u\in H_{1,n},\quad G_1:H_{1,n}\to H_{2,n},\quad
G_2:H_{2,n}\to H_{3,n},\quad A\in H_{3,n}.
\]
For one fixed deterministic scalar activation \(\phi:\mathbb R\to\mathbb R\),
used in all three hidden layers, define
\[
\begin{aligned}
X_1&=\phi(u),&
Z_2&=G_1X_1,&X_2&=\phi(Z_2),\\
Z_3&=G_2X_2,&X_3&=\phi(Z_3),&
f_n&=\langle A,X_3\rangle_{3,n}.
\end{aligned}
\]
The vector blocks \(u,A\) use the normalized Hilbert metrics.  Both matrix
blocks use ordinary Frobenius metric.  Thus
\[
(b\otimes x)v=b\langle x,v\rangle_n=n^{-1}bx^{\mathsf T}v
\]
is the matrix-block gradient convention.

Initialization is mutually independent:
\[
A_{0,i},u_{0,i}\sim N(0,1),\qquad
(G_{\ell,0})_{ij}\sim N(0,1/n),\quad \ell=1,2.
\]
All four blocks train by gradient flow on
\(\mathcal L_n=(y_\star-f_n)^2\), with fixed \(\eta>0\).

Freezing a layer, changing a metric or initialization, replacing a transpose
by a fresh Gaussian action, changing the data, or allowing \(\phi\) to
depend on width, time, initialization, or trajectory is outside the contract.

## 2. Admissible activations

The discovery class contains:

1. fixed \(C^2_{\rm loc}\) activations for which \(\phi,\phi'\), and
   \(\phi''\) have at most polynomial growth and the finite vector field is
   locally Lipschitz;
2. globally Lipschitz \(C^1\) activations with locally Lipschitz derivative;
3. piecewise-smooth activations only if a route proves existence, uniqueness,
   stability, and almost-sure compatibility of the intended finite-width
   gradient flow at every switching surface.

The selected \(\phi\) must be genuinely nonlinear on a set of positive
Gaussian measure and fixed independently of \(n,t\), and the trajectory.
It is inadmissible if it is affine, becomes affine in the limit, has
derivative zero almost everywhere, makes the nonlinear term or any trained
layer vanish in the width limit, or otherwise produces a lazy/frozen model.

This discovery class is broader than the class eventually used by a positive
theorem.  Narrowing is allowed only by selecting one fixed witness after the
comparison; the architecture and convergence target may not be weakened.

## 3. Exact finite causal skeleton

At any differentiability point put
\[
\begin{aligned}
D_3&=\phi'(Z_3),&B_3&=A D_3,&R_2&=G_2^*B_3,\\
D_2&=\phi'(Z_2),&B_2&=D_2R_2,&Q_1&=G_1^*B_2,\\
D_1&=\phi'(u).
\end{aligned}
\]
Feature ascent, denoted by a prime, is exactly
\[
A'=X_3,\qquad G_2'=B_3\otimes X_2,\qquad
G_1'=B_2\otimes X_1,\qquad u'=D_1Q_1.                 \tag{3.1}
\]
Its raw tangent kernel is
\[
K_n=f_n'
=\|X_3\|_2^2+\|B_3\|_2^2\|X_2\|_2^2
 +\|B_2\|_2^2\|X_1\|_2^2+\|D_1Q_1\|_2^2.             \tag{3.2}
\]
Physical time multiplies (3.1) by \(2\eta e_n\), where
\[
e_n=y_\star-f_n,\qquad
\dot e_n=-2\eta e_nK_n,\qquad \mathcal L_n=e_n^2.      \tag{3.3}
\]

For a strictly monotone candidate with \(\phi'\ne0\), the optional exact
bottom natural coordinate is
\[
\Theta(u)=\int_0^u\frac{d\xi}{\phi'(\xi)},\quad
r=\Theta(u),\quad \iota=\Theta^{-1},\quad
\Psi(r)=\phi(\iota(r)).
\]
Then \(r'=Q_1\) and \(\Psi'(r)=\phi'(\iota(r))^2\).
This changes coordinates but not the parameter metric or the network.

## 4. Admissible limiting contract

An admissible positive result has:

1. finitely many immutable initialization sources, with every reused
   \(G_{\ell,0}\) and its genuine adjoint represented jointly before
   training;
2. an absolutely constant number and species of current vector fields,
   operators, probability laws, measures, and scalars on fixed spaces;
3. exactly one current training-time argument;
4. an autonomous vector field using only the present state and fixed source;
5. a restart map from an intermediate state using the same realized source;
6. direct current-state observations of \(f,K,e,\mathcal L\);
7. a named topology in which the IDE is well posed and every displayed
   nonlinear contraction and raw square is continuous; and
8. canonical-iid compact-horizon convergence in probability of the finite
   state actions and of \(f_n,K_n,e_n,\mathcal L_n\).

Current trace-class or bounded operators are allowed extensionally: future
evolution may apply the present operator, but may not inspect a time-labelled
decomposition.  Program depth may be a proof approximation index, not a
dynamical state coordinate.

Forbidden are two-training-time kernels, DMFT responses/covariances, stored
paths, delay histories, growing moment or response lists, trajectory
playback, future-dependent sources, real-number encodings of a path, and
time-dependent forcing that is not fixed model data.

## 5. Limit order and topology

The proof order is:

1. fix every source/readout cutoff and one finite time mesh;
2. send \(n\to\infty\);
3. remove the mesh by a width-uniform stability estimate;
4. remove cutoffs by a width-uniform tail estimate.

The theorem may claim convergence in probability on each fixed physical
horizon.  Expectation convergence, operator-norm convergence, joint
long-time/width limits, and \(t\to\infty\) interpolation require separate
proofs and are not implicit.

Bare energy bounds do not control the raw kernel.  The topology or reachable
class must rule out coordinate concentration in \(B_3,R_2,B_2,Q_1\), and
must make the middle product
\[
(Z_2,R_2)\longmapsto \phi'(Z_2)R_2
\]
stable along exact and comparison trajectories.

## 6. Claim ladder

| Level | Required result |
|---|---|
| C0 | Exact finite gradient equations and \(f_n'=K_n\) |
| C1 | Exact finite-species algebraic operator closure with source provenance |
| C2 | Well-posed, autonomous, restartable limiting IDE in a named class |
| C3 | Fixed-cutoff, fixed-mesh source-program identification |
| C4 | Width-uniform mesh removal and continuous feature-time convergence |
| C5 | Cutoff removal, tail tightness, and defect-free raw-kernel convergence |
| C6 | Physical-clock identification of \(f,K,e,\mathcal L\) on compact time |
| C7 | Independent reconstruction and hostile audit of C0--C6 |

No claim is promoted without its bridge.  Fixed-mesh convergence is C3, not
C4 or C5.

## 7. Activation-selection criteria and falsifiers

Each candidate is scored on:

- exact IDE complexity and source provenance;
- finite and limiting well-posedness;
- boundedness and tail behavior of forward/backward fields;
- whether derivatives vanish, switch, or create degeneracy;
- adaptive reuse of both matrices and adjoints;
- continuity of the middle multiplier;
- uniform integrability of all four kernel terms;
- dimension-free Euler stability and cutoff removal; and
- absence of hidden memory or architecture substitution.

A candidate is witness-fatal if it needs an unproved delocalization,
uniform-integrability, or stability lemma of essentially the final theorem's
strength.  A nonsmooth candidate is witness-fatal if finite-width uniqueness
or stability fails.  Failure of one candidate does not prove impossibility
for the discovery class.

## 8. Terminal outcomes

Success is either:

1. one fixed admissible nonlinear activation and an exact autonomous
   operator IDE satisfying C0--C7; or
2. a rigorous impossibility theorem over an explicitly frozen activation
   subclass broad enough to answer the scoped alternative.

Several failed witnesses, formal algebra, fixed meshes, simulations, or an
assumed tail lemma are not terminal successes.
