# What the full p=1 closure protects, and where it can be singular

This is a study result about the original canonical p=1 population closure,
not the scalar one-channel model, a frozen-feature evolution, or a neural-width
limit. Its mathematical status and independent checks are in `validation.md`.
The two main conclusions are unconditional: a complete initialization
classification for finite circle data, and a finite-state singularity/saddle
classification for three nonparallel inputs in the canonical parity class.
The requested global exponential fitting theorem remains open.

## Exact model

Use phi=tanh, x_i in sqrt(2) S1, v_i=x_i/sqrt(2), positive masses p_i
summing to one, labels y_i, residuals r_i=f_i-y_i, and unhalved loss
L=sum_i p_i r_i^2. Canonical p=1 initialization is precisely the correlated
Gaussian construction and inverse-Cholesky normalization in
`docs/observable_p1.md`; its full derivation is reproduced in
`initial_geometry.md`, equations (1)--(3). In particular eta=1/4096 and the
reverse-action response term tau gamma is retained.

The full retained feature dimensions are five and three, including constants.
Canonical odd parity keeps the constant row and column inactive, exactly as
proved in the established source. Removing only these inactive coordinates
leaves b_1 in R4, b_2 in R2, and a full M in R^(2x4). The lower joint law
keeps both initial Gaussian g and its correlated reverse probes. The upper
population has its own separate Gaussian variables. Initially w=g, c=0,
M=D; the two nonzero bands of D are given in the source and in the proof.

The saved laws are Gamma_1=Law(b_1,g,w), Gamma_2=Law(b_2,c), together with
M and the fixed data. They need not have Lebesgue densities. The equations
are equivalently integrals against those laws or characteristics on their
fixed mark spaces. Define current vectors and fields

\[
a_i=\mathbb E_1[b_1\phi(w\cdot v_i)],\qquad z_i=Ma_i\in\mathbb R^2,
\qquad H_i=\phi(b_2^Tz_i),\qquad f_i=\mathbb E_2[cH_i],
\]
\[
d_i=\mathbb E_2[b_2c\phi'(b_2^Tz_i)]\in\mathbb R^2.
\]

The complete physical-time dynamics are

\[
\begin{aligned}
\dot w&=-2\sum_i p_i r_i\phi'(w\cdot v_i)
                    (b_1^TM^Td_i)v_i,\\
\dot c&=-2\sum_i p_i r_iH_i,\\
\dot M&=-2\sum_i p_i r_i d_i a_i^T.
\end{aligned}                                                   \tag{1}
\]

All matrix entries evolve and the reverse action uses the actual transpose.
The metric is population L2 for w,c and Frobenius for M. The established
fixed-order well-posedness proof applies through every finite time to these
bounded-label laws and gives w-g and c bounded on each finite horizon.
Its exact energy identity is

\[
\dot L=-\|\dot w\|_2^2-\|\dot c\|_2^2-\|\dot M\|_F^2.        \tag{2}
\]

## 1. Initial hidden geometry preserves every circle direction

**Theorem 1.** At this exact initialization there is an odd strictly
increasing function F on [-1,1], defined solely by the fixed Gaussian
integrals, such that

\[
z_0(v)=M_0a_0(v)=(F(v_1),F(v_2)).                            \tag{3}
\]

Consequently z_0(v) is never zero on S1, and

\[
z_0(v)=z_0(u)\iff v=u,\qquad
z_0(v)=-z_0(u)\iff v=-u.                                    \tag{4}
\]

The complete proof in `initial_geometry.md` retains both lower forward and
reverse marks. Its critical estimate proves positivity of the derivative
of their combined regression function, rather than assuming its two separate
coefficients have the same sign. Conditional Gaussian variance, the exact
response coefficient, and the elementary bound alpha<6/7 give that estimate.
Gaussian integration by parts then proves F'>0. No coefficient sign was
inferred numerically.

The upper mark law has positive density on an open square. A finite set of
functions b -> phi(b^T z_i) is linearly independent whenever all z_i are
nonzero and distinct up to sign. Restriction to a generic line reduces a
presumed identity to distinct one-dimensional tanh scales, whose exponential
tails are independent. Thus for any finite number of distinct, nonantipodal
inputs the initialized readout Gram

\[
G_{ij}(0)=\mathbb E_2[H_i(0)H_j(0)]
\]

is strictly positive definite. The two-dimensional code does not limit the
number of independent upper activation fields to two.

This also gives a finite fitting readout while keeping initialized hidden
features fixed:

\[
c_*=\sum_j (G(0)^{-1}y)_j H_j(0),\qquad
\mathbb E_2[c_*H_i(0)]=y_i.                                 \tag{5}
\]

Equation (5) is an explicit representation witness, not the evolution used
in (1) and not an assumption that feature learning selects this readout.
Both hidden blocks remain trainable throughout the analysis.

For general finite data allowing duplicate and antipodal inputs, choose one
representative v_C per unoriented class and write v_i=epsilon_i v_C. Then
the initialized state is stationary if and only if

\[
\sum_{i\in C}p_i\epsilon_i y_i=0\quad\text{for every class }C. \tag{6}
\]

This exactly classifies initial stalls, not later asymptotic failures. It
follows from dot c(0)=2 sum p_i y_i H_i(0), the independence above, and
dot w(0)=dot M(0)=0. Uniqueness then makes each such stall permanent.

There is a useful additional interpretation of (6). Every predictor in this
bias-free odd-activation architecture is odd in its input. Write
m_C=sum_(i in C) p_i and sigma_C=sum_(i in C) p_i epsilon_i y_i. For any
odd predictor taking value t_C at v_C, the contribution of this class is

\[
\sum_{i\in C}p_i(t_C-\epsilon_i y_i)^2
=m_C(t_C-\sigma_C/m_C)^2
 +\sum_{i\in C}p_i y_i^2-\sigma_C^2/m_C.                    \tag{7}
\]

The independent initialized fields realize every vector of class values
t_C by the same Gram construction as (5). Thus (6) occurs exactly when
the zero predictor is already globally optimal among all odd predictors
on these data. There are no additional initial stalls caused by loss of
an input direction in this p=1 dictionary.

## 2. Consequence for the rotated equilateral triple

Take

\[
x_i(\theta)=\sqrt2\left(\cos\left(\theta+\frac{2\pi(i-1)}3\right),
\sin\left(\theta+\frac{2\pi(i-1)}3\right)\right),
\quad y=(1,1,-1),\quad p=(3/8,1/8,1/2).                     \tag{8}
\]

For every theta, (3)--(4) give an invertible initial upper Gram. By
continuity and compactness, its least eigenvalue even has a common positive
lower bound over this fixed rotation family. Therefore L'(0)<0 for every
rotation, with a common strictly negative upper bound.

No such trajectory reaches a stationary state at a finite later time:
otherwise local uniqueness, applied backward from that state, would force
the initial state to have been stationary. Hence L'(t)<0 at every finite
t, and M(t) cannot be zero after strict descent because M=0 gives f=0,L=1.
These statements do not exclude a positive limiting loss at infinite time.

The scalar sign-change argument has no vector analogue here. A continuous
two-dimensional code can connect z to -z without vanishing. At initialization
the stronger statement (4) actually proves that it avoids zero at every
orientation. The proof does not rely on full rotation covariance: that
covariance is false for the fixed p=1 dictionary. Only signed coordinate
permutations have the exact stated symmetry; `initial_geometry.md` proves
the distinction directly.

Thus the equilateral family is rigorously free of initial stalls and initial
feature degeneracy. Whether every member tends to zero loss remains open.
The existence of a finite fitting readout (5) alone cannot answer that
dynamical question.

## 3. Complete finite-state singularity test for three genuine inputs

Fix three pairwise nonparallel inputs. Work in the canonical state class:
odd w,c under their respective simultaneous mark negations, bounded w-g and
c, and finite full M. Every initialized trajectory is in this class at each
finite time. Bounds here need not be uniform as time tends to infinity.
The unrestricted full model outside this parity class can activate constant
coordinates and is not classified by the reduced equations below.

A central fact is that the lower map

\[
w\longmapsto(a_1,a_2,a_3)\in\mathbb R^{4\times3}
\]

has a surjective differential everywhere in this class. Its proof in
`stationary_geometry.md`, Lemma 2, uses both the four-dimensional positive
mark density and the unchanged Gaussian tails in w=g+bounded. It holds
at the current state, without any assumption that hidden features stay
near their initialized values. The right inverse supplies bounded odd
perturbations, so it preserves the canonical parity class.

To describe singularity, partition the nonzero vectors z_i=Ma_i into
classes modulo sign. In class C write z_i=epsilon_i z_C. Zero vectors
belong to a separate zero set. A vector xi in R3 annihilates the full
prediction differential if and only if

\[
\begin{cases}
\sum_{i\in C}\epsilon_i\xi_i=0 &\text{for every nonzero class }C,\\
\xi_i M^T d_i=0 &\text{for every sample }i,\\
\sum_i\xi_i d_i a_i^T=0.&
\end{cases}                                                   \tag{9}
\]

The full tangent Gram is singular exactly when (9) has a nonzero solution.
This is a necessary and sufficient current-state test, including all ranks
of M. It retains the readout, lower, and middle gradient blocks separately.

For rank(M)=2, the classification becomes particularly simple. Singularity
occurs exactly when at least one of the following holds:

* Some z_i=0 and its backward vector d_i=0.
* Some nonzero sign class contains at least two samples and its common
  backward vector d_C=0.

Forward collapse alone is therefore insufficient to make the full dynamics
singular. If the backward vector is nonzero, first-layer variations can
separate the samples to first order. Conversely, a vanishing backward vector
at distinct nonzero codes does not cause singularity because the readout
features remain independent. For rank one the last equation in (9) is an
additional transverse constraint; for rank zero, the exact cases are given
in the complete report.

This distinction is realized by an explicit class of finite fitting states.
For any such input triple, lower submersion permits a bounded odd perturbation
of w=g for which a_1,a_2,a_3 are linearly independent, as proved in the
representability argument of `stationary_geometry.md`. Complete these to a
basis of R4. Choose any nonzero z in R2 and a vector z_perp independent of z,
and define M on this basis by

\[
Ma_1=Ma_2=z,\qquad Ma_3=-z,\qquad Ma_4=z_{\perp}.
\]

Then M has rank two. With H=phi(b_2^Tz) and c=H/E[H^2], the predictions
are exactly (+1,+1,-1). The three upper fields have rank one, but their
common backward vector satisfies

\[
z^Td=\frac{\mathbb E[(b_2^Tz)\phi(b_2^Tz)\phi'(b_2^Tz)]}
              {\mathbb E[\phi(b_2^Tz)^2]}>0.
\]

The strict sign follows pointwise away from the null hyperplane b_2^Tz=0.
Thus d is nonzero and (9) gives full prediction-differential rank three.
Perfect within-class code collapse and opposite class codes are compatible
with a nonsingular full tangent geometry. These are explicitly constructed
fitting states, not oracle endpoints or a claim of canonical accessibility.

Stationarity is obtained by inserting xi_i=p_i(f_i-y_i) into (9). In each
nonzero class it requires the signed weighted-mean prediction

\[
\mathbb E_2[c\phi(b_2^Tz_C)]
=\frac{\sum_{i\in C}p_i\epsilon_i y_i}{\sum_{i\in C}p_i}.      \tag{10}
\]

For rank two, this and r_i d_i=0 for every sample are necessary and
sufficient. For rank one the transverse matrix constraint remains necessary.
For M=0 all predictions vanish; stationarity is exactly

\[
\mathbb E_2[b_2c]\left(\sum_i p_i y_i a_i\right)^T=0.          \tag{11}
\]

Thus (9)--(11) give a full finite-state classification in the declared
three-input canonical class. They do not classify limits at infinity.

## 4. Every positive-loss stationary point is a saddle

**Theorem 2.** In the same three-input class, every positive-loss stationary
point with M nonzero has a negative second variation of L. At M=0 it is
also a strict saddle unless both factors in (11) vanish. When both vanish,
the Hessian is zero but a cubic descent curve exists. In particular every
local minimum in this class has zero loss.

The complete proof is `stationary_geometry.md`, Theorem 5. Its mechanism
uses both layers. At a positive-loss stationary point choose a sample with
nonzero residual. Lower surjectivity permits an independent variation of
its code in the image of M. The resulting derivative ridge
(b_2^T z_i) phi'(b_2^T z_i), or a nonzero linear function when z_i=0,
is outside the current upper feature span. Varying c in its component
orthogonal to that span keeps all first prediction variations zero and
creates a mixed second-variation term of either sign. This proves the
saddle property even when the upper Gram is singular. At M=0 the same
calculation gives the explicit strict-saddle and cubic cases in the report.

Stationary loss values have another restriction. A nonzero code class
with positive and negative signed-target masses P_C,N_C contributes
4 P_C N_C/(P_C+N_C); each zero-code sample contributes its mass. Thus
every positive stationary loss for binary labels is at least min_i p_i.
For (8), this gap is 1/8. The report gives the complete finite necessary
list of stationary loss values, without asserting every partition is
realizable by a stationary state.

Strict saddles can still have stable trajectories, and a deterministic
initialization is not automatically excluded from their stable sets.
Furthermore a trajectory can escape without having a finite stationary
limit. Neither possibility is eliminated by Theorem 2.

## 5. What this says about a potential

Let R_i=sqrt(p_i)r_i. With gradients in the physical metric, define the
full weighted tangent Gram

\[
\Theta_{ij}=\sqrt{p_ip_j}\left[
\mathbb E_2[H_iH_j]
+(d_i^Td_j)(a_i^Ta_j)
+(v_i^Tv_j)\mathbb E_1[
  \phi'(w\cdot v_i)\phi'(w\cdot v_j)
  (b_1^TM^Td_i)(b_1^TM^Td_j)]\right].                        \tag{12}
\]

Exactly, dot R=-2 Theta R. The geometric obstruction to a full tangent
metric is precisely (9), which can be substantially smaller than the
singular set of the readout Gram alone. This identifies what a potential
based solely on second-layer separation omits.

On nonsingular states the natural inverse-metric residual quantity has
the complete derivative

\[
\Phi=R^T\Theta^{-1}R,\qquad
\dot\Phi=-4L-R^T\Theta^{-1}\dot\Theta\Theta^{-1}R.             \tag{13}
\]

No sign for the second term has been proved. Equations (9) and (13) do
not establish exponential decay; they isolate the remaining evolving
geometry instead of hiding it in a future conditioning assumption.

An independently derived finite-state trapping theorem in
`positive_potential.md` proves exponential decay of the ordinary loss and
finite full-state travel once a quantitative current-state smallness test
holds. It includes all moving blocks and proves its future conditioning
bound by a first-exit argument. However, the required entrance has not been
proved from the unit-label initialization, where L(0)=1. That conditional
theorem is retained as a tool and is not counted as the requested positive
initialized theorem.

The affirmative target still requires a data-only proof that the initialized
trajectory avoids a positive-loss stable set and asymptotic degeneration,
or a different current-state potential that directly controls those
possibilities. The lower differential is qualitatively onto at every
finite time, but its least singular value has no proved all-time bound.

## 6. Numerical evidence and precise remaining scope

The precommitted diagnostic used the exact p=1 coefficient formulas, tensor
Gaussian populations with 8/12/16 nodes per independent coordinate, three
rotations of (8), and a tighter time-integrator repeat. All ten solves
finished in 18.83 seconds under the 120-second one-thread cap. At T=120
the finest grids gave losses approximately 0.000308,0.000331,0.000490.
Time refinement passed, but population refinement did not satisfy the
predeclared agreement thresholds. No angle met the predeclared resolved
fitting criterion. These observations do not prove population fitting,
exponential asymptotics, or absence of a bad angle. Complete commands,
metrics and limitations are in `diagnostic_result.md`.

The exact progress is: full initial separation and a classification of
initial stalls for every finite circle dataset; a complete current-state
singularity criterion and saddle theorem for three genuine inputs; and a
precise identification of the missing initialized convergence estimate.
Whether the requested equilateral trajectories fit for every orientation,
and an unconditional exponential potential for a general unit-label triple,
remain unresolved. No result here identifies the full network at fixed p,
changes the dictionary, or promotes another study's findings.
