# Arbitrary finite inputs: the three-input basin proof does not lift directly

2026-09-18. Lead synthesis of this study's finite-input continuation.
Review status is recorded in the study README; no promotion. The exact target is the p=1
population closure, with its canonical correlated Gaussian-derived marks,
odd state sector, full trainable matrix and actual transpose, physical
L2/L2/Frobenius metric, and unhalved probability-weighted square loss.
There is no finite-network or closure-order limit in these statements.

## 1. Answer and the distinction it requires

The universal finite-input exceptional-bad-point-basin theorem has not been
proved. The extension is not a routine replacement of three by m: a key
premise of the three-input proof is false for seven equally weighted inputs
in dimension three, even though the inputs are pairwise distinct and never
antipodal.

There is an explicit equilibrium with loss 48/49 whose actual physical
Hilbert Hessian is positive semidefinite of rank one. Its flow linearization
has one stable eigenvalue and no unstable eigenvalue. The readout can also
be chosen so the equilibrium has an explicit cubic descent direction.
Thus absence of negative second-order curvature here is compatible with
actual nonlinear descent. A further construction gives nonconstant exact
trajectories decreasing to loss 48/49 from specially chosen states.

These facts disprove the universal strict-saddle premise. They do not show
that the basin of this equilibrium, or the union of bad basins, has positive
probability. The arbitrary-finite-input basin-null statement remains open.

The two independent initial routes are `finite_basin_geometry.md` and
`finite_basin_tail.md`. Their post-freeze additions explicitly record the
comparison boundary and the lead's readout and strong-stable suggestions.
The lead's separate `finite_critical_loss_gap.md` proves a finite-input
small-loss result without assumptions on linear dependencies.

## 2. Explicit obstruction and why it works

Take C,S>0 with C^2+S^2=1 and set

\[
x(\alpha)=\sqrt3\,(C,S\cos\alpha,S\sin\alpha).
\]

Choose three positive-label angles 0,2pi/3,4pi/3 and four negative-label
angles pi/4,3pi/4,5pi/4,7pi/4, with mass 1/7 at each input. The positive
first coordinate excludes antipodes; the seven angles are different.
The triangle and square have the same classwise mean and second moment.
Consequently, for unit directions u_i=x_i/sqrt3, common prediction
F=-1/7 and rho_i=(F-y_i)/7,

\[
\sum_i\rho_i=0,\qquad
\sum_i\rho_i u_i=0,\qquad
\sum_i\rho_i u_i u_i^T=0.
\tag{1}
\]

On the unchanged lower mark carrier choose a nonzero coefficient q, put
epsilon=sign(q dot b_1), A=E_1[b_1 epsilon], and
kappa=q dot A=E_1|q dot b_1|>0. Take

\[
w=a\epsilon e_1,\qquad M=e_1q^T,\qquad a>0.
\tag{2}
\]

Here the first e_1 is an input coordinate and the second is the first upper
coefficient coordinate. The fields have the prescribed odd parity. Every
lower effective input equals a_i=phi(aC)A, so every upper activation equals

\[
H=\phi(zB),\qquad z=\kappa\phi(aC)>0,\qquad B=b_{2,1}.
\]

Choose the bounded odd readout so that

\[
E_2[cH]=-1/7,\qquad E_2[cB\phi'(zB)]=0.
\tag{3}
\]

This is explicit: project H orthogonally off J=B phi'(zB), and rescale
the remaining nonzero function to have pairing -1/7 with H. H and J are
linearly independent, as their analytic extensions have different
large-B asymptotics. Thus the necessary Gram inverse exists. Independent
centered upper coordinates make every backward vector d_i zero.

The lower and matrix gradients therefore vanish individually; the readout
gradient vanishes by the first identity in (1). All predictions are F, so

\[
L=\frac17\{3(-8/7)^2+4(6/7)^2\}=\frac{48}{49}.
\tag{4}
\]

All three blocks remain trainable. Rank one describes the chosen point M,
not a constraint on perturbations or the dynamics. The actual lower field
w is bounded, whereas w-g is unbounded but square integrable. The example
therefore belongs to the same unrestricted physical Hilbert endpoint class
as the latest three-input theorem, but not to the bounded-displacement
endpoint class of the separate tail theorem.

For arbitrary physical perturbations (h,k,N), the first effective-vector
variation is affine in u_i. Its residual-weighted linear and quadratic
sums vanish by (1). The residual-weighted second effective-vector
variation vanishes by the same moments. Therefore every residual term
in the loss Hessian cancels. Since d_i=0, the first prediction variation
is just E_2[kH] at every input. The complete result is

\[
D^2L[(h,k,N),(h,k,N)]=2(E_2[kH])^2,
\qquad
\nabla^2L(h,k,N)=(0,2E_2[kH]H,0).
\tag{5}
\]

This is an actual Hilbert Frechet Hessian: d_i=0 makes each lower critical
coefficient zero, and the gradient's product remainder has Lipschitz
constant O(r) on radius-r Hilbert balls. The full proof and estimates are
in `finite_basin_geometry.md`, Sections 4 and 7. Its only nonzero Hessian
eigenvalue is 2||H||_2^2>0; the flow has no unstable linear subspace.

The strengthened readout in `finite_basin_tail.md`, Section 8, imposes a
third explicit moment. Let

\[
K_3(B)=\left.\frac{d^3}{ds^3}\phi(\kappa B\phi(s))\right|_{s=aC}.
\]

The functions H,J,K_3 are linearly independent: after the constant term
is removed, their analytic positive-infinity asymptotics have respectively
the relevant first and third powers of B multiplying exp(-2zB). Their
3-by-3 Gram thus constructs c satisfying (3) and E_2[cK_3]=1.
Along the bounded odd lower perturbation h=epsilon e_2,

\[
L'(0)=L''(0)=0,\qquad L'''(0)=-12S^3/49<0.
\tag{6}
\]

The square's cubed-cosine sum is zero at any rotation, and the triangle's
is 3/4; hence this calculation applies to the angles above as well as
the pi/8 rotation used by the independent tail report. Equation (6)
exhibits a regular, non-minimizing, degenerate positive-loss equilibrium.

The complete strong-stable contraction in `finite_basin_geometry.md`,
Section 8, uses only the d_i=0 structure (5) and smoothness in the affine
bounded-increment chart around this state. It constructs a one-parameter
set of nonstationary trajectories with

\[
48/49<L(t)<1,\qquad L'(t)<0,\qquad
\theta(t)\longrightarrow\theta_*,\qquad L(\theta_*)=48/49.
\tag{7}
\]

The original two-moment projected readout already suffices for (7);
the third-moment condition separately verifies a nonlinear descent direction.
Neither result determines the probability of the entire basin.

## 3. Positive conclusions that do extend

For any finite compatible input list, regardless of dependence, the earlier
`dependent_finite_fitting.md` gives an explicit fit and a nonempty open
basin with exponential fitting and a state endpoint. This remains valid.

For any finite list with positive masses, `finite_critical_loss_gap.md`
proves that every equilibrium has L=0 or L>=min_i p_i. Readout stationarity
groups upper effective vectors by signed equality, and tanh-feature
independence fixes each group's prediction to its oriented label mean.
The resulting finite loss list gives the gap. Consequently

\[
L(0)<\min_i p_i\quad\hbox{and physical state convergence}
\quad\Longrightarrow\quad L_\infty=0.
\tag{8}
\]

For equal weights the threshold is 1/m. This implication is deterministic
and imposes no endpoint regularity, but does not prove that canonical
training reaches the threshold or that the state converges.

There are also two new restricted basin results in `finite_basin_tail.md`:

* The input spans may form any finite direct sum of blocks, each with at
  most one independent input relation. With bounded limiting lower
  displacement, blockwise cancellation gives the full null-basin theorem.
  For example m=3k inputs in k independent planes in R^(2k) have k
  independent relations. Weights may be arbitrary positive numbers.
* For arbitrary finite dependence, full support of the limiting w law and
  a positive-definite conditional second-moment matrix
  E[b_1 b_1^T | w] give cancellation and the full null-basin theorem.
  These are extra endpoint assumptions, not consequences of convergence;
  the conditional condition does not even hold at w=g when d>1.

Both basin claims use exactly the previous population-field randomization
and physical Hilbert convergence. Neither is a replacement for the requested
unrestricted data-only extension.

## 4. The precise missing theorem

For three equally weighted nonaligned inputs, every positive endpoint below
loss one has an unstable linear direction. The existing proof places all
trajectories approaching such endpoints on a countable hypersurface hull.
Equations (4)--(6) show that this premise is false for larger finite lists,
even at a Frechet-regular equilibrium. The missing ingredient is control of
nonlinear motion in the degenerate directions, sufficient to prove that
all their positive-loss point-convergence basins are null, or a construction
showing that such a basin has positive probability.

A cubic descent direction does not resolve that issue. Nor does the special
stable curve (7) show positive basin probability. The requested unrestricted
finite-input theorem is open at this checkpoint, and has not been declared
false. Canonical deterministic initialization and positive-loss behavior
without a state endpoint remain separate unresolved questions.
