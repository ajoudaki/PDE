# Three-residual search: exact upper balance defect and a low-gradient obstruction

Frozen independent analytical round, 2026-09-16. This is study material,
not an established result. No other current route, other study, numerical
experiment, or external convergence theorem was used. The assigned skills
were `investigate-conjectures` and `solve-math-rigorously`.

**Outcome.** The requested canonical-initialization exponential certificate
is not proved. Two complete results sharpen the obstruction facing a mixed
potential: an exact matrix/readout balance formula with a non-exact
circulation term, and an explicit family of states of the *actual canonical
order-one model* having a fixed arbitrarily small positive loss, zero
hidden velocity, and arbitrarily small full gradient. The latter states
retain the correct marks and parity, keep the lower field exactly at its
initial value, and keep the middle matrix bounded. Their readout norms
diverge. They are not proved reachable from canonical initialization and
are not counterexamples to the requested theorem.

## 1. Contract and exact equations

The data are three unit directions with no coincident or antipodal pair,
equal weights, and labels `y=(1,1,-1)`. The state, ridge `eta=1/4096`,
Cholesky normalization, population laws, actual transpose, and physical
unhalved-loss metric remain those of the supplied sources. Initially
`w=g`, `M=D`, `c=0`. The target is a formula in this saved current state
for `Phi>=0`, a constant `lambda>0`, and an increasing comparison function
`h` with `h(0)=0`, such that along every such canonical trajectory

\[
 \dot\Phi\le-\lambda\Phi,\qquad \mathcal L\le h(\Phi).
\]

No future integral, reconstructed training time, trajectory lookup, or
additional accumulated-residual variable is admissible. Geometry-dependent
constants and exact initialized integrals are allowed. All claims below
refer to the full equations, not a readout-only replacement.

Write `r_i=f_i-y_i`, `H_i=tanh(b_2^TMa_i)`,
`a_i=E_1[b_1 tanh(w.u_i)]`, and
`d_i=E_2[b_2 c(1-H_i^2)]`. Then

\[
 \dot c=-\frac23\sum_i r_iH_i,
 \quad\dot M=-\frac23\sum_i r_i d_i a_i^T,
 \quad\dot w=-\frac23\sum_i r_i\operatorname{sech}^2(w\cdot u_i)
                  (b_1^TM^Td_i)u_i.                 \tag{1}
\]

For the data pairing `〈z,v〉_mu=(1/3)sum_i z_i v_i`, let
`T c=(E[cH_i])_i`, and let `J` be the hidden derivative at fixed readout.
The exact equations and dissipation identity are

\[
 \dot r=-2Kr,\quad K=TT^*+JJ^*,\qquad
 \dot{\mathcal L}=-4\langle r,Kr\rangle_\mu
 =-\|\dot c\|_2^2-\|\dot M\|_F^2-\|\dot w\|_2^2.       \tag{2}
\]

All cross-residual terms remain in `K`. No sign of an off-diagonal entry
or of an individual residual is assumed.

## 2. An exact matrix/readout balance with a circulation defect

The canonical parity subspace is preserved by (1), as proved in the
supplied C.4.7.10.C.1. On this subspace the active upper marks are
`Z=(tanh xi_1,tanh xi_2)`, with `xi_i` independent `N(0,v_0)`,
`v_0=E tanh^2 G`. Put

\[
 \tau=E\tanh^2(\sqrt{v_0}G),\quad s=\sqrt{\tau+\eta},
 \qquad v_i=Ma_i/s,
\]

where `M` denotes only its active two-by-four block in the formulas of
this section. Then `H_i=tanh(Z.v_i)` and

\[
 d_i=s^{-1}E[Zc\operatorname{sech}^2(Z\cdot v_i)].
\]

The saved upper readout is a function of the upper marks, so its derivative
in `Z` is well-defined along the canonical finite-time solution. Indeed
integrating the first equation of (1) expresses `c(t,Z)` as a finite-time
integral of smooth ridge functions; on a fixed finite interval their
coefficient vectors are bounded. Differentiation under this integral is
therefore justified. Differentiating (1) in `Z` gives

\[
 \nabla_Z\dot c=-\frac23\sum_i r_i v_i
                  \operatorname{sech}^2(Z\cdot v_i).
\]

Contracting the middle equation with the *same* matrix gives the exact
identity

\[
 \dot M M^T=E[Zc(\nabla_Z\dot c)^T].                  \tag{3}
\]

In particular, the two normalization factors `s` cancel; replacing the
upper Cholesky scale or changing the middle metric would spoil this check.
Define the symmetric matrix-valued quadratic expression

\[
 B(c)=\frac12E[c\{Z(\nabla_Zc)^T+(\nabla_Zc)Z^T\}].
\]

The product rule in (3) gives

\[
 \begin{aligned}
 \frac d{dt}\{MM^T-B(c)\}
 =\frac12E[&c\{Z(\nabla_Z\dot c)^T+(\nabla_Z\dot c)Z^T\}\\
            &-\dot c\{Z(\nabla_Zc)^T+(\nabla_Zc)Z^T\}].
 \end{aligned}                                                     \tag{4}
\]

This is a genuine mixed-block identity. Its right side is antisymmetric
under exchange of `c` and `dot c`; it is a circulation term, not a square.
Formula (4) does not assert a sign or an invariant. It exposes the precise
extra term that a proposed nonlinear replacement for balancedness must
control. Both `B(c)` and its derivative are finite at finite canonical time
by the bounded-coefficient observation above.

### Why the missing term cannot be removed by a fixed quadratic readout correction

Already the trace of (3) would require a fixed self-adjoint operator `A`
on the readout space to satisfy

\[
 A\tanh(Z\cdot v)=(Z\cdot v)\operatorname{sech}^2(Z\cdot v)
                                                               \tag{5}
\]

for all coefficient vectors `v` if a quadratic readout correction were
to cancel the middle radial derivative universally. More explicitly, a
readout primitive `Q` satisfying
`DQ(c)[H_v]=2E[c(Z.v)sech^2(Z.v)]` for every `c,v` would have, at
`c=0`, a symmetric second derivative with this property. Thus the same
obstruction applies to any twice differentiable readout-only primitive
with that universal cancellation property, not just an assumed quadratic.

Here is a direct failure of the required symmetry. Set `X=Z_1`, and use
coefficient vectors `(a,0)` and `(b,0)`. For small `a,b`, boundedness of
`X` and Taylor's formula give

\[
 \begin{aligned}
 &E[\tanh(aX)bX\operatorname{sech}^2(bX)]
   -E[\tanh(bX)aX\operatorname{sech}^2(aX)]\\
 &\hspace{15mm}=\frac23ab(a^2-b^2)E[X^4]
       +O((|a|+|b|)^6).                              \tag{6}
 \end{aligned}
\]

Take `a=epsilon`, `b=2epsilon`. Its leading term is
`-4 epsilon^4 E[X^4]`, which is nonzero for sufficiently small positive
`epsilon`. A self-adjoint `A` would force the difference in (6) to be zero.
For a twice differentiable `Q`, symmetry of its Hessian at zero forces
the same equality. This rules out precisely that universal readout-only
primitive. It does not rule out a joint functional depending essentially
on `c,w,M`, nor a sign available only on the initialized trajectory.

## 3. Independence of the nine upper value-and-derivative functions

The next result permits an exact construction inside this canonical model.
Let `v_1,v_2,v_3` be nonzero pairwise nonparallel vectors in `R^2`. On
the open square `(-1,1)^2`, the following nine odd functions are linearly
independent:

\[
 \tanh(Z\cdot v_i),\quad
 Z_1\operatorname{sech}^2(Z\cdot v_i),\quad
 Z_2\operatorname{sech}^2(Z\cdot v_i),\qquad i=1,2,3.    \tag{7}
\]

To prove this, write a putative identity as

\[
 \sum_i\{A_i\phi(Z\cdot v_i)+(B_i\cdot Z)\phi'(Z\cdot v_i)\}=0,
 \qquad\phi=\tanh.                                  \tag{8}
\]

Fix `i`. For each `j!=i`, choose a nonzero vector `n_j` perpendicular
to `v_j`. The constant-coefficient differential operator
`product_(j!=i) (n_j.grad)^2` annihilates the entire `j` summand: the
ridge argument is constant in direction `n_j`, and its prefactor is at
most linear. All these operators commute. Pairwise nonparallelity makes
`P_i=product_(j!=i)(v_i.n_j)^2` nonzero. Applying the operator and
dividing by `P_i` leaves

\[
 \left(A_i+2\sum_{j\ne i}\frac{B_i\cdot n_j}{v_i\cdot n_j}\right)
        \phi^{(4)}(z)+(B_i\cdot Z)\phi^{(5)}(z)=0,
 \qquad z=Z\cdot v_i.                              \tag{9}
\]

For `z` in a neighborhood of zero, `phi^(5)(z)` is nonzero because
`phi^(5)(0)=16`. Varying `Z` in the direction perpendicular to `v_i`
while holding `z` fixed in (9) therefore forces `B_i=b_i v_i`.
Equation (9) becomes

\[
 (A_i+4b_i)\phi^{(4)}(z)+b_i z\phi^{(5)}(z)=0.
\]

The expansion
`tanh z=z-z^3/3+2z^5/15-17z^7/315+O(z^9)` gives the coefficients
`16(A_i+5b_i)` at `z` and `-(136/3)(A_i+7b_i)` at `z^3`.
Thus `b_i=A_i=0`. Repeating for each `i` proves independence.

The actual law of `Z` has positive density on the open square. An
almost-sure linear identity among (7) would consequently hold everywhere
there by continuity. Thus their nine-by-nine population Gram matrix is
strictly positive definite. The proof uses neither a numerical rank test
nor an unproved genericity assertion.

## 4. Fixed positive loss with arbitrarily small full gradient

Fix *any* admitted triple and choose `0<delta<1/sqrt(3)`. The supplied
initialized map theorem gives

\[
 H_{i,0}(Z)=\tanh(Z\cdot\nu_i),\quad
 \nu_i=(\varphi(u_{i,1}),\varphi(u_{i,2})),
\]

where `varphi` is odd and strictly increasing and the three vectors
`nu_i` are nonzero and pairwise nonparallel. The last conclusion is the
complete noncollision proof in `arbitrary_pair_local.md`, not a symmetry
assumption.

For `0<epsilon<=1`, set

\[
 w_\epsilon=g,\qquad M_\epsilon=\epsilon D,
 \qquad H_{i,\epsilon}=\tanh(\epsilon Z\cdot\nu_i).
                                                               \tag{10}
\]

List the nine functions (7) at `v_i=epsilon nu_i` in a column `F_epsilon`,
with the first three entries the value functions. Its positive definite
Gram is `G_epsilon=E[F_epsilon F_epsilon^T]`. Define the readout using
only these finite population integrals:

\[
 b=((1-\delta)y_1,(1-\delta)y_2,(1-\delta)y_3,0,\ldots,0)^T,
 \qquad c_\epsilon=F_\epsilon^TG_\epsilon^{-1}b.       \tag{11}
\]

Every function in this expression is bounded and odd. For each fixed
`epsilon`, the readout is bounded and lies in the canonical parity
subspace. The saved mark laws have not changed. By construction,

\[
 E[c_\epsilon H_{i,\epsilon}]=(1-\delta)y_i,
 \qquad E[c_\epsilon Z_a\operatorname{sech}^2(
                  \epsilon Z\cdot\nu_i)]=0
       \quad(a=1,2).                                 \tag{12}
\]

The constant upper component of `d_i` also vanishes: its integrand is odd.
The other two vanish by (12), including their prescribed Cholesky scale.
Thus `d_i=0` exactly for all three data. Substituting into the full
equations (1), at this state,

\[
 \mathcal L=\delta^2<1/3,\qquad
 \dot w=0,\quad\dot M=0,\quad
 \dot c=\frac{2\delta}{3}\sum_i y_iH_{i,\epsilon}.      \tag{13}
\]

Since tanh is 1-Lipschitz, `E[ZZ^T]=tau I`, and all three `nu_i` are
fixed,

\[
 \begin{aligned}
 0<\|\nabla\mathcal L\|^2=-\dot{\mathcal L}
 &=\frac{4\delta^2}{9}
      \left\|\sum_i y_iH_{i,\epsilon}\right\|_2^2\\
 &\le \frac{4\delta^2\tau}{9}\epsilon^2
                   \left(\sum_i|\nu_i|\right)^2
 \longrightarrow0.                                  \tag{14}
 \end{aligned}
\]

The strict inequality follows from the independence just proved. This is
an exact low-gradient family for every allowed triple, with `w=g` and
`||M||op<=||D||op`. It lies below the earlier incompatible-coefficient
loss barrier. At each fixed `epsilon`, its coefficient vectors are
nonzero and pairwise nonparallel; they approach zero together as
`epsilon` decreases.

The readout necessarily becomes large. Put
`Psi(z)=tanh z-z sech^2 z`. The identity
`Psi'(z)=2z sech^2 z tanh z` gives
`|Psi(z)|<=2|z|^3/3`. By (12),

\[
 \begin{aligned}
 1-\delta
 &=|E[c_\epsilon\Psi(\epsilon Z\cdot\nu_i)]|\\
 &\le \frac23\epsilon^3\|c_\epsilon\|_2
               \|(Z\cdot\nu_i)^3\|_2.
 \end{aligned}                                                     \tag{15}
\]

The denominator on the right is finite and strictly positive, so
`||c_epsilon||_2` grows at least as a positive multiple of `epsilon^-3`.
The exact readout radial derivative at this same state is

\[
 \frac d{dt}\|c\|_2^2
 =4\langle y-f,f\rangle_\mu=4\delta(1-\delta)>0.       \tag{16}
\]

Equations (14) and (16) are compatible: the norm is very large, so its
squared radial derivative may be order one while the Hilbert velocity is
small. This is not a metric contradiction.

## 5. Consequences, limits, and the remaining proof obligation

Equations (10)–(14) disprove any full-state inequality
`||grad L||^2>=beta(L)` with `beta(ell)>0` for positive loss, even on
the canonical marked parity subspace with `L<1/3`, `w=g`, and bounded
middle matrix. Consequently a differentiable loss-only transform
`Phi=psi(L)` cannot satisfy the requested strict exponential inequality
uniformly on that state class: at a fixed `ell=delta^2`, its derivative
is `-psi'(ell)||grad L||^2`, while loss domination with `h(0)=0` requires
`psi(ell)>0`.

This is a **candidate-class obstruction**, not a reachable-state or
existence obstruction. In particular:

* The constructed `c_epsilon` is not the prescribed zero readout and has
  not been shown to occur on any initialized trajectory.
* A state-dependent mixed potential can respond to the growing readout
  norm. The permitted non-power comparison `h` leaves substantial room
  for such a potential; (14) does not rule it out.
* The circulation formula (4) gives neither a sign nor a bound excluding
  (10)–(11) from a canonical trajectory. The no-primitive argument rules
  out one universal cancellation mechanism, not all mixed potentials.
* No rotation of the fixed dictionary, alteration of the labels, change
  of metric, or suppression of a trained block occurs in these arguments.

The missing implication is therefore concrete: obtain a canonical-reachable
constraint tying the upper readout to its *current* feature coefficients,
strong enough to prevent the large readout cancellations in (12), or
control the circulation in (4) by a coercive current-state expression.
The initial condition `c=0` is decisive information not used by the ambient
obstruction. The identities alone do not yet propagate a sufficiently
strong constraint from it. Global existence and finite dissipated energy
do not supply that propagation.

| Claim | Status | Exact scope |
|---|---|---|
| Upper matrix/readout identity (3) and circulation formula (4) | Proved | Full canonical finite-time parity trajectory |
| Readout-only twice differentiable primitive universally cancelling upper radial balance | Ruled out | The universal cancellation property (5)–(6) |
| Independence of the nine upper functions | Proved | Any three nonzero pairwise nonparallel coefficients |
| Fixed small loss, bounded middle matrix, arbitrarily small full gradient | Proved | Exact canonical marked states (10)–(11), not established reachable |
| Loss-only exponential certificate on the whole marked state class | Ruled out | Differentiable loss transforms, arbitrary admissible comparison `h` |
| Requested mixed certificate on each canonical initialized trajectory | Open | Missing reachable-state cancellation/circulation control |

## 6. Source freeze and checks

Scientific inputs read: all of `docs/NOTATION.md`; the exact state,
dynamics and existence/energy proof in C.4.7.9; C.4.7.10 B, C.1 and D.3;
and the four assigned study artifacts below. Links in those artifacts
were not followed outside the assigned scope. Source SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `all_angles_result.md` | `33ce17ba0be80836ba13862eb3ba76b579cabfe2bba1cb4f076be4e2f9de9ec7` |
| `arbitrary_pair_local.md` | `4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a` |
| `generic3_metric_route.md` | `c089546aa52eae67f4e9ee75621766d2429475729822d9bcbcd5f32086ffd801` |
| `generic3_metric_second_pass.md` | `104ed0fe6a7ee9e58cbe5d5c9f5c97598523e57649229993e5f7747efb446b4e` |

Internal checks: the middle normalization factors cancel in (3); (4)
follows by differentiating both terms of `B`; the degree-four coefficient
in (6) is nonzero for `(a,b)=(epsilon,2epsilon)`; the differential
elimination in (9) kills each entire competing value-and-derivative group;
both constant and odd coordinates of every `d_i` vanish in (12); (14)
matches the complete physical energy identity; and (15) independently
checks the required readout escape. No numerical quadrature, trajectory
experiment, formal prover, or independent reviewer was used in this round.
