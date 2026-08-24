# Protocol: three-hidden-layer arctangent operator IDE

Status: frozen before candidate-proof selection, 21 August 2026.

## 1. Canonical finite model

For \(j=1,2,3\), let \(H_{j,n}=\mathbb R^n\) with

\[
\langle v,w\rangle_{j,n}=\frac1n v^{\mathsf T}w .
\]

The trainable parameters are

\[
u\in H_{1,n},\quad G_1:H_{1,n}\to H_{2,n},\quad
G_2:H_{2,n}\to H_{3,n},\quad A\in H_{3,n}.
\]

With \(\phi(x)=\arctan x\) coordinatewise, define

\[
\begin{aligned}
X_1&=\phi(u),&
Z_2&=G_1X_1,&X_2&=\phi(Z_2),\\
Z_3&=G_2X_2,&X_3&=\phi(Z_3),&
f_n&=\langle A,X_3\rangle_{3,n}.
\end{aligned}
\]

The vector blocks \(A,u\) use their normalized Hilbert metrics.  The two
matrix blocks use the ordinary Frobenius metric.  Thus, for
\((b\otimes x)v=b\langle x,v\rangle_n\), the matrix gradient is the
normalized rank-one map \(b\otimes x=n^{-1}bx^{\mathsf T}\).

Initialization is mutually independent:

\[
A_{0,i},u_{0,i}\sim N(0,1),\qquad
(G_{\ell,0})_{ij}\sim N(0,1/n),\quad \ell=1,2.
\]

Every block is trained by gradient flow on the full one-sample squared loss
\((y_\star-f_n)^2\).  Freezing a layer, changing an activation, changing a
metric, or replacing a transpose by an independent Gaussian action is an
easier-model substitution and does not answer the contract.

## 2. Exact finite causal skeleton

Put

\[
\begin{aligned}
D_2&=(1+Z_2^2)^{-1},&D_3&=(1+Z_3^2)^{-1},\\
B_3&=A D_3,&R_2&=G_2^*B_3,\\
B_2&=D_2R_2,&Q_1&=G_1^*B_2 .
\end{aligned}
\]

Feature ascent is exactly

\[
A'=X_3,\qquad
G_2'=B_3\otimes X_2,\qquad
G_1'=B_2\otimes X_1,\qquad
u'=(1+u^2)^{-1}Q_1 .
\]

The feature kernel is

\[
K_n=\|X_3\|_2^2
+\|B_3\|_2^2\|X_2\|_2^2
+\|B_2\|_2^2\|X_1\|_2^2
+\|(1+u^2)^{-1}Q_1\|_2^2=f_n'.
\]

Physical time multiplies every feature-ascent right-hand side by
\(2\eta e_n\), where \(e_n=y_\star-f_n\), and

\[
\dot e_n=-2\eta e_nK_n,\qquad \mathcal L_n=e_n^2.
\]

These identities are C0 obligations and will receive an independent finite
algebra check.

## 3. Admissible closure contract

An admissible answer must have:

1. a finite collection of immutable Gaussian action sources constructed
   before training from \((G_{1,0},G_{2,0})\), their genuine adjoints, and
   the two endpoint marks;
2. a width-independent, absolutely constant number of current vector,
   operator, scalar, or probability-density fields on fixed spatial
   domains;
3. exactly one training-time coordinate on every current field;
4. an autonomous vector field and restart map using only the present state
   and the same realized immutable source;
5. direct present-state formulas for \(f,K,e,\mathcal L\);
6. a named restart-stable class with existence and uniqueness; and
7. for every \(T<\infty\), uniform-on-\([0,T]\) convergence in probability
   of finite \(f_n,K_n,e_n,\mathcal L_n\) under the stated initialization.

The source and individual fields may be infinite-dimensional.  The number
and mathematical types of fields may not grow with width, elapsed time,
Euler depth, Taylor order, or requested accuracy.

Forbidden constructions include DMFT, response kernels, two-training-time
covariances, a stored path, a time-labelled rank-one decomposition, future
trajectory playback, a projective hierarchy without proved uniqueness and
readout continuity, or an infinite list of moment variables disguised as
new state species.

A current trace-class operator is admissible only extensionally: future
evolution may apply the operator as a whole, but may not inspect when its
rank-one components were created.

## 4. Limit and topology

The primary limit order is:

1. freeze every source cutoff and time discretization;
2. send \(n\to\infty\);
3. remove the time discretization;
4. remove source/readout cutoffs.

The theorem may claim convergence in probability on each fixed physical
horizon.  It may not infer expectation convergence, joint
\(n,T\to\infty\) convergence, or long-time interpolation without separate
uniform-integrability or coercivity estimates.

The state topology must control every displayed product and the raw
quadratic kernel.  Bare \(L^2\) boundedness is not enough if an adaptive
coordinate tail can carry nonvanishing square energy.

## 5. Claim ladder

| Level | Required result |
|---|---|
| C0 | Exact finite algebra, natural-coordinate identities, and \(f_n'=K_n\) |
| C1 | One immutable joint two-matrix pointed source with actual adjoints and fixed-program convergence |
| C2 | Exact O(1)-species autonomous current-state IDE and raw readouts |
| C3 | Global or compact-horizon well-posedness and restartability in a named class |
| C4 | Fixed-cutoff, fixed-mesh finite-width identification |
| C5 | Mesh and all cutoffs removed; raw \(K_n\) identified uniformly on compact feature time |
| C6 | Physical clock, residual, predictor, kernel, and loss identified uniformly on compact physical time |

The conjecture is resolved only if C0--C6 all pass.

## 6. Prespecified hostile checks

The candidate fails unless it survives all of the following.

1. The two reused matrices and their transposes are represented jointly;
   fresh independent Gaussian proxies are forbidden.
2. The middle backpropagated field
   \(B_2=D_2G_2^*(AD_3)\) is defined and stable in the claimed topology.
3. Multiplication by the unbounded middle field cannot destroy uniqueness
   or Euler convergence.
4. Both \(\|B_2\|_2^2\) and
   \(\|(1+u^2)^{-1}Q_1\|_2^2\) are square-uniformly integrable along the
   canonical trajectories; an energy bound alone is insufficient.
5. Extreme rows, columns, singular-vector alignment, and vanishing-time
   boundary layers cannot create an \(O(1)\) raw-kernel defect.
6. Every cutoff has a width-uniform removal estimate with the correct order
   of limits.
7. Restarting at an intermediate time does not require a pre-restart path,
   a fresh source, or a growing set of program coordinates.
8. Program depth used in a proof is an approximation index and not a
   dynamical state coordinate.

## 7. Terminal outcomes

The successful terminal outcome is a complete proof surviving independent
source, regularity/tail, Markov-contract, and clean-room reconstruction
audits.  If a theorem-strength dependency survives, the honest terminal
status is open or conditional, together with the exact proved algebra and
gap; persistence does not authorize relabeling a gap as a theorem.
