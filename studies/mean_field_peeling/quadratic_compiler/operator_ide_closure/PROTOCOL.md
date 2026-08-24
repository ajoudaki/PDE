# Protocol: quadratic depth-two operator-IDE closure

Status: frozen before candidate-source comparison, 21 August 2026.

## Canonical network

Let \(H_n=\mathbb R^n\) with

\[
\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w.
\]

At initialization \(A_n,u_n\) have iid \(N(0,1)\) coordinates and
\(G_n=W_n/\sqrt n\), where \(W_n\) has iid \(N(0,1)\) entries; all sources
are independent.  Put

\[
X=u^{\odot2},\qquad Z=GX,\qquad B=A\odot Z,\qquad
R=G^*B,\qquad f=\langle A,Z^{\odot2}\rangle_n.
\]

Feature ascent is exactly

\[
A'=Z^{\odot2},\qquad X'=8X\odot R,\qquad
G'=2B\otimes X,
\]

where \((p\otimes q)v=p\langle q,v\rangle_n\).  Its kernel is

\[
K=\langle Z^{\odot4},1\rangle_n
 +4\langle B^{\odot2},1\rangle_n\langle X^{\odot2},1\rangle_n
 +16\langle X\odot R^{\odot2},1\rangle_n,
\qquad f'=K.
\]

Physical full-MSE time multiplies the first three right-hand sides by
\(2\eta e\), where \(e=y_\star-f\), and obeys

\[
\dot e=-2\eta eK.
\]

## Admissible closure

A successful result may use a fixed finite number of scalar, vector,
measure, spatial-kernel, traffic, or operator fields.  It must satisfy all of
the following.

1. Every field lives on a completely specified source domain independent of
   width, derivative order, elapsed time, and requested horizon.
2. The immutable source law is derived before observing the positive-time
   trajectory and is explicitly determined by the Gaussian initialization.
3. The current state is autonomous and restartable.  No two-training-time
   response/correlation kernel, Volterra playback, or stored path is allowed.
4. Prediction, kernel, residual, and loss are continuous current-state
   readouts in a named topology.
5. The limiting evolution is well posed on every finite physical-time
   interval.
6. For every deterministic \(T<\infty\), the finite-width output and loss
   converge in probability uniformly on \([0,T]\).  Fixed-order Wick or
   traffic convergence alone is insufficient.
7. A generic operator renamed as one field is inadmissible unless its source,
   operations, ideal/function space, initialization, and positive-time
   identification are all constructed.  An ultraproduct chosen after the
   finite trajectories, a width-sized atomic source, or a real-number oracle
   is not a solution.

The phrase \(O(1)\)-field means that the number and type of fields are fixed;
it does not require finite numerical storage.  Infinite-dimensional fields
are permitted precisely as in a genuine PDE or measure-valued equation.

## Claim ladder

- C1: exact finite-width algebra and current-state readouts;
- C2: explicit deterministic Gaussian traffic/operator source;
- C3: closed autonomous one-time operator/IDE vector field;
- C4: local and global physical-time well-posedness;
- C5: fixed-source Picard or characteristic no-leakage theorem;
- C6: compact-physical-time finite-width identification;
- C7: loss convergence or its sharpest justified long-time statement;
- C8: a compression-boundary theorem for any rejected smaller class.

## Preregistered validity gates

- The source and equations must give \(f(0)=0\) and \(K(0)=111\).
- Their feature jet must reproduce

\[
F'(0)=111,
\quad F^{(3)}(0)=1\,685\,184,
\quad F^{(5)}(0)=77\,400\,633\,120.
\]

- Matrix action and coordinatewise multiplication must coexist in the same
  source; replacing coordinatewise square by free multiplication is a fatal
  model substitution.
- Any cutoff argument must remove the cutoff in a topology controlling the
  displayed output and kernel.
- Any external infinite-width theorem must be quoted with hypotheses and
  shown to cover weight reuse/transposes, polynomial activation, and the
  relevant time limit.

## Decisive outcomes

The program stops only after either:

1. a construction passes independent source, well-posedness, no-leakage, and
   positive-time audits; or
2. the natural finite-current-field classes are separated by a rigorous
   obstruction and every surviving broader class is recorded as open.
