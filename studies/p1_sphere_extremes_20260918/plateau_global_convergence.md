# Global-convergence route: strict descent, saddle geometry, and the remaining gap

Status: **analytical candidate**, originally frozen 2026-09-18. After
cross-audit its overbroad gap list was corrected: a finite initialized
endpoint with M=0 is excluded by strict descent below loss one. The
proved theorems and constructions are unchanged. No experiment was run.
This is an internal derivation, not promoted theory or an independent review.
The universal initialized convergence claim remains open in this route.

Scientific input scope: `docs/observable_p1.md` in full;
`docs/global_nonlinear.md` C.4.7.9.3--4 and the equations/existence material
of C.4.7.10.D.3; and this study's complete `architectural_loss_floor.md`,
`protected_family.md`, `terminal_geometry.md`, and
`initialization_positivity.md`. The research and rigorous-mathematics skills,
including their contract and adversarial-audit instructions, were applied.
No other study, current route, review, experimental result, or conversation
history supplied a scientific premise. This file was frozen before sending
its findings to the supervisor.

## 1. Contract and conclusions

The target is the exact canonical population p=1, d=3 flow with
`w(0)=g`, `c(0)=0`, `M(0)=D`, joint Gaussian-derived lower marks, ridge
`eta=1/4096`, all entries of the middle matrix trained, its actual transpose,
and unhalved weighted square loss. The normalized inputs are
`u_i=x_i/sqrt(3)` on S2, labels are +/-1, and the active weights `mu_i` are
positive and sum to one. Zero-weight atoms may first be discarded. All
population integrals are exact. Nothing here concerns a time discretization,
finite population rule, neural-width limit, or frozen-feature replacement.

The proposed universal statement is

`lim_(t->infinity) L(t) = L_odd`

for every such weighted triple, with the exact architectural minimum
`L_odd` given by the signed-duplicate decomposition in
`architectural_loss_floor.md`. For independent inputs `L_odd=0`.

This route proves three narrower facts.

1. Every nonstationary canonical trajectory has `L'(t)<0` at every finite
   time. Exact finite-time stopping is impossible; this does not preclude
   a positive asymptotic loss limit.
2. For independent active inputs, every finite positive-loss critical
   state in the initialized odd sector with `M!=0` is a strict saddle:
   a bounded admissible perturbation
   has negative second directional derivative of the loss. No full-row-rank
   assumption on M is needed.
3. There is an explicit finite critical state with full-row-rank M and
   loss `8/9` on the uniformly weighted positive coordinate-axis triple.
   It uses the exact canonical mark spaces and even retains `w=g`.
   The canonical initialized trajectory for that same data fits, by the
   supplied protected-family/terminal results. Thus this critical state
   is a counterexample to an ambient landscape lemma, not an initialized
   counterexample.

The remaining obstruction to a universal proof is concrete: one must
exclude approach to nonoptimal saddles and absence of a finite strong
endpoint along the prescribed initialized trajectory. A finite endpoint
with M=0 has loss one, so strict initial descent already excludes it.
Strict initial feature separation, strict finite-time loss decrease,
and the saddle theorem below do not by themselves exclude these events.

## 2. Actual equations and finite-time strict descent

Use the exact odd sector, omitting only its inactive constant coordinates.
The static marks are `b_1 in R6`, `b_2 in R3`, with the canonical laws, and
the complete trainable matrix is `M in R^(3 x 6)`. Put

\[
\begin{gathered}
 h_{1i}=\tanh(w\cdot u_i),\quad a_i=E_1[b_1h_{1i}],\quad
 v_i=Ma_i,\quad H_i=\tanh(b_2\cdot v_i),\quad
 f_i=E_2[cH_i],\quad r_i=f_i-y_i,\quad \lambda_i=\mu_i r_i,\\
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot v_i)],\quad
 q_i=b_1^TM^Td_i.
\end{gathered}
\]

In the population-L2/Frobenius metric,

\[
 \nabla f_i=
 \bigl(\operatorname{sech}^2(w\cdot u_i)q_i u_i,
       H_i,d_i a_i^T\bigr),\qquad
 \theta'=-2\sum_i\lambda_i\nabla f_i,
 \qquad L'=-\|\theta'\|^2.
 \tag{1}
\]

A finite state means bounded `w-g`, bounded c, and finite M. The allowed
existence source gives local Lipschitz continuity in these norms, unique
solutions, and finite-time continuation. The same argument works in three
input dimensions: the bounds use `|u|=1`, bounded marks, and finitely many
matrix entries, without a dimension-two-specific step.

If `L'(t_0)=0` at a finite time, (1) makes that reached state stationary.
The constant trajectory through it is a solution. Local uniqueness for
the reversed equation identifies the original solution with that constant
trajectory on a left neighborhood of `t_0`. Repeating backward to time
zero, or applying the local Lipschitz Gronwall estimate on the bounded
finite prefix, shows that initialization was stationary as well.

The supplied architectural argument proves that canonical initialization
is stationary exactly when every signed-duplicate class has zero signed
label mean, equivalently `L_odd=1`; it is then already globally minimizing.
For every other law, `L'(0)<0`, so the preceding uniqueness argument gives

\[
                     L'(t)<0\qquad (0\le t<\infty).
 \tag{2}
\]

This is a pointwise statement; it provides no uniform lower bound on
`-L'` as time tends to infinity.

## 3. A strict-saddle theorem for independent inputs

Assume the active `u_i`, at most three, are linearly independent and
consider finite states in the initialized odd sector. At a critical
state, the lower component of (1) vanishes almost surely. Input
independence and the strictly positive finite lower gates imply

\[
             \lambda_i M^Td_i=0\quad\hbox{for every }i.
 \tag{3}
\]

Here the equivalence between a vanishing linear function of b1 and its
vanishing coefficient uses positive definiteness of `E_1[b_1b_1^T]`.
To verify it with the actual initialization, each raw pair `(h_j,k_j)`
has positive definite covariance: h_j has positive variance, and k_j
has positive conditional variance given h_j because the reverse Gaussian
noise has positive variance. Distinct coordinate pairs are independent
and centered. The invertible ridge normalization preserves definiteness.

### 3.1. A lower perturbation can change exactly one coefficient vector

Let `t_i in R3` be a dual vector with `t_i dot u_j=delta_ij`. At any
finite state set

\[
 S_i=E_1[b_1b_1^T\operatorname{sech}^4(w\cdot u_i)].
\]

This finite matrix is positive definite: for every nonzero a, the
nonnegative integrand `(a dot b_1)^2 sech^4(w dot u_i)` has positive
integral because the unweighted integral is positive and its gate is
strictly positive almost surely. Given any `A in R6`, choose

\[
 \delta w(b_1,g)=t_i\operatorname{sech}^2(w\cdot u_i)
                           b_1^TS_i^{-1}A.
 \tag{4}
\]

The perturbation is bounded and has exactly
`delta a_i=A`, `delta a_j=0` for `j!=i`. It is odd under the canonical
simultaneous mark negation, so it remains in the same invariant sector.
No surrogate hidden-feature dynamics has been introduced: (4) is an
admissible direction in the actual w state space.

### 3.2. A derivative feature is outside the current readout span

Let `V=span{H_j}` in the upper L2 space. For an index i with `v_i!=0`,
the function

\[
 G_i(b)=(b\cdot v_i)\operatorname{sech}^2(b\cdot v_i)
 \tag{5}
\]

does not belong to V. For `v_i=0`, the same conclusion holds for
`G_i(b)=b dot z` with every nonzero `z in R3`.

Here is a contained proof. Group the nonzero vectors v_j modulo sign,
with representatives `z_1,...,z_k`, `k<=3`. Their ridge functions span V.
The upper mark density is positive on an open cube about zero. Thus an
almost-sure relation among these continuous functions is an identity
on that cube. Choose e avoiding the finitely many hyperplanes where
`e dot z_j=0` or two such products have equal absolute values, and also
`e dot z=0` when needed. Restrict the identity to `b=s e` near zero.

For (5), take `z_1=v_i`, put `t_j=e dot z_j` and `x_j=t_j^2`, and
compare odd coefficients through degree `2k+1`. The required tanh
coefficients are `1,-1/3,2/15,-17/315`, all nonzero. The resulting
system, after absorbing nonzero t_j into constants, has the form

\[
 \sum_{j=1}^k C_jx_j^n+B(2n+1)x_1^n=0,
 \qquad n=0,\ldots,k.
\]

Apply the coefficient combination associated with
`P(x)=product_j(x-x_j)`. It gives
`2B x_1 P'(x_1)=0`. The distinct nonzero x_j force `B=0`, and the
remaining Vandermonde system forces every C_j to vanish. This excludes
a relation with a nonzero coefficient of (5).

When `v_i=0`, there are at most two nonzero feature representatives.
A proposed relation involving `s(e dot z)` has, at odd degrees
`3,...,2k+1`, a Vandermonde system with nonzero x_j. It forces every
ridge coefficient to vanish. The linear coefficient then contradicts
`e dot z!=0`. The case `k=0` is immediate.

### 3.3. Negative curvature

Take a finite positive-loss critical state with `M!=0`, and choose i
with `lambda_i!=0`. If `v_i!=0`, choose `A=a_i` in (4), so
`delta v_i=v_i`. If `v_i=0`, choose A such that `z=MA!=0`, possible
because `M!=0`, and use that z instead. Write the resulting nonzero
upper derivative feature as G_i. In both cases (3) implies

`delta f_i=d_i dot MA=0`,

and the other predictions also have zero first variation. Thus this
lower perturbation lies in the nullspace of the full prediction
differential.

Let

\[
             \psi=G_i-P_VG_i,
 \tag{6}
\]

where P_V is orthogonal projection onto the finite-dimensional space V.
Section 3.2 gives `||psi||_2>0`. All these functions are bounded and odd,
so `delta c=psi` is an admissible bounded perturbation in the canonical
sector. Also `E_2[psi H_j]=0` for every j, so it has zero first prediction
variation and zero pure-c second loss derivative.

Only input i changes under the lower perturbation, and the mixed
prediction derivative is

\[
 D^2f_i[\delta w,\psi]=E_2[\psi G_i]=\|\psi\|_2^2.
\]

Consequently

\[
 D^2L[\delta w,\psi]=2\lambda_i\|\psi\|_2^2\ne0,
 \qquad D^2L[\psi,\psi]=0.
\]

For real s the second derivative in the joint direction
`(delta w,s psi,0)` is therefore

\[
 D^2L[\delta w,\delta w]+4s\lambda_i\|\psi\|_2^2.
 \tag{7}
\]

Choosing a finite s with the opposite sign and sufficiently large
magnitude makes (7) negative. All directional derivatives exist by
bounded marks and bounded derivatives of tanh; the chosen directions
are bounded. Taylor expansion along this fixed direction now gives
strictly smaller loss at arbitrarily nearby states.

This proves: **every finite positive-loss critical state in the initialized
odd sector for independent active inputs with M nonzero is a strict saddle**,
including rank-one
and rank-two matrices. The theorem supplies no uniform negative-curvature
constant as M, the lower gates, or the feature separation degenerate.

## 4. Explicit failure of the no-bad-critical-point lemma

Take `u_i=e_i`, `y_i=1`, `mu_i=1/3`. Use exactly `w=g` and the canonical
static mark distributions. The initialized lower columns are

\[
 a_i=Ae_i^{h}+Be_i^{k},\quad
 A=\nu/a>0,\quad B=\frac{\beta\eta}{b(\nu+\eta)}>0,
 \quad R=\sqrt{A^2+B^2},
\]

where the constants are those of `docs/observable_p1.md`, with nu naming
its variance v. Set `p_i=a_i/R^2` and
`n_i=(B e_i^h-A e_i^k)/R`. Define the full matrix

\[
 M=e_1(p_1-p_2+p_3)^T+e_2n_1^T+e_3n_2^T.
 \tag{8}
\]

Its three rows are nonzero and mutually orthogonal, so M has full row
rank. Nevertheless

`Ma_1=e_1`, `Ma_2=-e_1`, `Ma_3=e_1`.

For `Z=b_(2,1)`, write `H=tanh Z`, `K=Z sech^2 Z`, and

\[
 U=H-\frac{E_2[HK]}{E_2[K^2]}K,
 \quad \Delta=E_2[UH]=\|U\|_2^2>0,
 \quad c=\frac{U}{3\Delta}.
 \tag{9}
\]

The denominator `E K^2` is positive. The strict positivity of Delta
follows because H and K are not proportional on an interval about zero:
their linear coefficients agree, whereas their cubic coefficients are
`-1/3` and `-1`. The upper density is positive there. Thus (9) is a
bounded odd readout on the actual upper mark space.

The predictions are `(1/3,-1/3,1/3)`. All three upper gates are identical.
The first component of each d_i is `E[cK]=0`; its other components
vanish by independence and the zero means of the other upper marks.
Hence `d_i=0`, every lower and matrix velocity is zero, and

\[
 \sum_i\mu_i r_i H_i
 =\tfrac13[-\tfrac23H+(-\tfrac43)(-H)-\tfrac23H]=0.
\]

The readout velocity is also zero. This finite state therefore has

\[
                         L=\frac89>0=L_{\rm odd}.
 \tag{10}
\]

It is a strict saddle by Section 3. It falsifies the possible lemma
that all finite critical states fit independent compatible data, even
with full-row-rank M, the canonical joint marks, and unchanged lower
weights `w=g`. It does **not** falsify canonical initialized convergence:
M and c in (8)--(9) are not the prescribed initial values. Indeed the
supplied initialized axis-family theorem proves that the prescribed
trajectory for precisely this triple converges to zero loss.

## 5. Why the saddle result does not close global convergence

The following tempting bridge is false as a general gradient-flow
principle: strict initial descent and only saddle-type nonoptimal
critical endpoints force a specified deterministic initialization to
avoid those endpoints. For example the nonnegative potential

`E(x,y)=x^2+(y^2-1)^2`

has gradient flow `x'=-2x`, `y'=4y(1-y^2)`. Starting at `(1,0)` gives
`(x(t),y(t))=(exp(-2t),0)` and
`E(t)=1+exp(-4t)`, strictly decreasing at every finite time toward the
positive-loss saddle `(0,0)`. This elementary example is solely a
logical audit of that bridge, not a replacement model or a claim about
the p=1 trajectory.

For the canonical problem, a strong finite endpoint must be critical:
if the continuous autonomous vector field had a nonzero limit there,
its projection on that nonzero vector would retain a fixed positive
speed, contradicting convergence. Thus Section 3 classifies every
nonfitting strong endpoint with `M_*!=0` as a strict saddle. But no
argument here puts the canonical initial point outside its stable set.
The initialization is prescribed, not a draw from a state-space measure
to which a generic saddle-avoidance assertion could be applied.

The negative-curvature construction does not cover ambient M=0 states,
but a finite initialized endpoint with M_*=0 would have loss one. Every
nonstationary initialized trajectory has limiting loss strictly below
one, so this is not a remaining finite-endpoint alternative. A sequence
with M tending to zero and unbounded c is different and is not excluded.
The permitted existence/energy bounds hold on each finite time interval,
without giving all-time boundedness or strong precompactness. In an
infinite-dimensional population state space, boundedness alone would
not supply that compactness either. A positive loss limit could therefore
fail to produce a finite strong endpoint at all. This noncompact case
and deterministic approach to a strict saddle remain unruled out.

For dependent but architecturally compatible triples, the dual-vector
construction (4) is unavailable. The strict-saddle theorem is not claimed
there. Exact finite-time strict descent (2) continues to hold.

## 6. Claim ledger and decisive remaining obligation

| Claim | Status | Exact scope or obstruction |
|---|---|---|
| Canonical nonstationary loss decreases strictly at every finite time | Proved here | All weighted triples; stationary initialization is already at L_odd |
| Every finite positive-loss critical state with M nonzero is a strict saddle | Proved here | Independent active inputs, actual full population flow |
| Full row rank of M rules out positive-loss critical states | Falsified here | Explicit state (8)--(10), loss 8/9 |
| The explicit saddle is reached from canonical initialization | False for the constructed data | Supplied axis-family theorem gives fitting |
| Strict saddle geometry alone excludes deterministic approach to a saddle | Falsified as a general proof principle | Explicit nonnegative two-variable potential above |
| Every compatible initialized triple reaches its architectural minimum | Open | Canonical stable-set exclusion and endpoint control remain unproved |

The highest-leverage next analytical obligation for this route is a
**canonical reachability restriction** that excludes the residual-active
conditions `M^Td_i=0` at nonoptimal limiting states, or else a construction
showing that the prescribed trajectory actually approaches such a state.
The explicit saddle demonstrates that this restriction must use the
initialized dynamics. It cannot be a statement about all finite states,
and it cannot be replaced by a future kernel integral condition.
