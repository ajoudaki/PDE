# Feature-mobility audit: plateau depth is missing state

2026-09-08. Independent follow-up to `PLATEAU_HOSTILE.md`. This is an exact finite-field analysis, with no experiments. It does not repeat the ambient raw-Hessian objection.

## Main finding

For the flat-plateau activation and nonorthogonal inputs, replacing the raw first-layer state by its sample features loses information needed for the future. The formal feature equation

\[
\dot h=-D(h)\Gamma D(h)F(h,A,C),\qquad
F_i=r_iq_i,
\tag{1}
\]

is exact along true trajectories, but its initial-value problem can be nonunique even at finite width with bounded smooth physical forces. Two different depths in the same plateau give identical initial \((h,A,C)\) and different subsequent feature paths. Thus an autonomous uniqueness or contractivity proof in a distance depending only on \((h,U,C)\) cannot be valid on this state space.

This does not refute the contract, which retains \(w\). An approach that keeps the missing plateau depths or imposes compatibility with the full raw trajectory may still work. The obstruction below is to the proposed feature-only reduction, not to the full population theorem.

## 1. Why the formal equation loses information

For the monotone activation of `PLATEAU_HOSTILE.md`, define

\[
D(s)=\phi'(\phi^{-1}(s))\quad(0<s<M),
\qquad D(0)=D(M)=0.
\]

This is single-valued and continuous, including the plateau values. Applying the chain rule to the true preactivation equation gives (1), neuron by neuron. Nonetheless, when \(h_i=M\), the value of \(z_i\ge R_*\) is absent from \(h_i\).

The exact raw equation is

\[
\dot z_i=-\sum_j\Gamma_{ij}\phi'(z_j)F_j.
\tag{2}
\]

If \(\Gamma\) is diagonal, a vanished gate freezes its own preactivation. If \(\Gamma\) has an off-diagonal entry, a different active sample can move \(z_i\) through its plateau while \(h_i\) stays exactly constant. The time at which \(h_i\) starts changing again depends on the unrecorded depth.

## 2. Exact original-architecture construction

Take an admitted positive-definite input Gram

\[
\Gamma=\begin{pmatrix}1&\rho&0\\\rho&1&0\\0&0&1\end{pmatrix},
\qquad 0<\rho<1-\delta.
\]

It is realized, for example, by

\[
u_1=e_1,\quad u_2=\rho e_1+\sqrt{1-\rho^2}e_2,
\quad u_3=e_3.
\]

Use width one, with the original two-hidden-layer architecture. Set

\[
z(0)=(R_*+s,0,R_*+1),\qquad A(0)=\tfrac14,
\qquad C(0)=2,
\tag{3}
\]

where \(s>0\). These are ordinary finite parameter states: positive-definiteness of \(\Gamma\) permits every displayed \(z\). There is no alteration of the model or of a training block.

Every value of \(s>0\) gives the same initial feature triple

\[
h(0)=(M,1,M).
\]

For the activation in the preceding note, \(M=2\), \(\phi(0)=1\), and all second-layer preactivations at (3) lie strictly in the transition interval. Moreover,

\[
f_2(0)=2\phi(1/4)>2,
\quad q_2(0)=\tfrac12\phi'(1/4)>0.
\]

For either conventional binary-label set \(\{0,1\}\) or \(\{-1,1\}\), this gives

\[
F_2(0)=r_2(0)q_2(0)>0.
\]

Initially only sample 2 has an active first-layer gate. Until sample 1 leaves its plateau, the exact equations reduce, for this first-layer neuron, to

\[
\dot z_1=-\rho\phi'(z_2)F_2,
\qquad
\dot z_2=-\phi'(z_2)F_2,
\qquad \dot z_3=0.
\tag{4}
\]

The equations for \(z_2,A,C\) depend on the common features \((M,\phi(z_2),M)\) and are identical for every plateau depth. All three training blocks continue to follow their original equations.

By continuity, there is a fixed short interval on which

\[
\rho\phi'(z_2)F_2\ge c>0
\]

for this common subsystem. Choose one initial depth \(s\) small enough that sample 1 reaches \(R_*\) within that interval, and another depth large enough to remain above \(R_*\) over the interval. At the shallow trajectory's hitting time, (4) still gives \(\dot z_1<0\). It therefore enters the transition interval and its feature becomes strictly less than \(M\). The deeper trajectory's first feature remains equal to \(M\).

The two trajectories have identical initial \((h,A,C)\), satisfy the same autonomous feature equation (1) coupled to the same original \(A,C\) equations, and have different feature paths. The full raw finite ODE remains smooth and unique for each of the two distinct raw initial states.

The phenomenon is not peculiar to width one. The same construction can be made in one first-layer neuron of any finite width, with all other initial parameters identical, choosing positive small second-layer weights and a positive readout so that the selected neuron's \(F_2\) is positive. Extra first-layer neurons can occupy protected cells spanning the three samples. The protected sample-feature Gram can therefore be positive while the feature-only nonuniqueness persists.

**Scope.** The chosen parameters are bounded ordinary states in the original architecture. This is not a claim about typical Gaussian initializations, a fixed-horizon limit, or failure of full-state uniqueness. It is a concrete falsifier of autonomous restartability after discarding plateau depths.

## 3. The diagonal entropy coordinate blows up on an actual finite-time path

In the diagonal case, one can attempt the componentwise coordinate

\[
p(s)=\int^s\frac{da}{D(a)^2}.
\]

Inside the transition interval this satisfies

\[
p(\phi(z))=\int^z\frac{dt}{\phi'(t)}+\text{constant}.
\]

Because \(\phi'\) is Lipschitz and vanishes at \(R_*\),

\[
0<\phi'(t)\le\|\phi''\|_\infty(R_*-t)
\qquad(t<R_*\text{ near }R_*),
\]

so the integral diverges as \(z\uparrow R_*\). For nonorthogonal \(\Gamma\), equation (2) permits crossing the same boundary in finite physical time with bounded \(A,C,z\) and bounded forces. To obtain an upward crossing in the original field, choose \(y_2=1\), retain \(A=1/4\), and take \(C>0\) sufficiently small that \(f_2<1\). Then \(q_2>0\), \(F_2<0\), and at \(z_1=R_*\) the cross term gives \(\dot z_1>0\). By continuity, starting just below that boundary gives a finite-time upward crossing with a positive derivative throughout a short interval. The first sample's own force tends to zero at the boundary and does not prevent this argument. Alternatively, the departure in Section 2 already starts at infinite \(p\)-coordinate. Thus this entropy coordinate is not a finite coordinate on all reached raw states and cannot by itself give a global continuation space for the flat activation.

The transformed equation also shows exactly where the diagonal cancellation fails:

\[
\dot p_i=-\sum_j\Gamma_{ij}\frac{D(h_j)}{D(h_i)}F_j
\tag{5}
\]

whenever all relevant gates are positive. For diagonal \(\Gamma\), the right side contains only the fixed diagonal factor times \(F_i\). In general, a common force at two states does not cancel, and the ratios in (5) can diverge near a plateau.

## 4. A natural cross-weighted Bregman substitute is not a distance

Even strictly inside the transition region, simply inserting \(\Gamma^{-1}\) into the componentwise entropy pairing can destroy positivity. Consider

\[
\mathcal D(h,\widetilde h)
=(h-\widetilde h)^T\Gamma^{-1}
\big(p(h)-p(\widetilde h)\big).
\tag{6}
\]

In the correlated two-coordinate block, suppose the componentwise secant slopes of \(p\) are \(a,b>0\). The quadratic expression in (6) is proportional to

\[
a x^2+b y^2-\rho(a+b)xy.
\]

It is indefinite as soon as

\[
ab-\frac{\rho^2(a+b)^2}{4}<0.
\]

Because \(p'=D^{-2}\) is unbounded near a plateau and finite in the interior, the ratio \(a/b\) can be arbitrarily large. For every \(\rho\ne0\), the displayed strict inequality can therefore be realized by nearby interior states, and \(\mathcal D\) is negative for some such pair. This is an explicit positivity failure, beyond the failure of a mixed-partial integrability condition.

This calculation also applies to strictly monotone bounded activations whose derivative tends to zero at the ends of their feature range. For those activations there is no finite-plateau depth loss, so Section 2 does not apply; the cross-weighted pairing (6) still fails.

## Remaining possibility

A successful argument would need either a comparison quantity that retains the missing raw information and controls the off-diagonal forcing terms, or a genuinely different monotonicity structure verified for the particular physical gradient. This note does not rule out such a quantity. It rules out treating (1) as a uniquely evolving autonomous replacement state and rules out the simple cross-weighted entropy pairing (6).
