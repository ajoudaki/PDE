# Mean and disagreement modes near the three-coordinate solution

2026-09-16. Independent scoped analytic proposal, frozen before comparison.
No experiment, generic convergence theorem, or promotion is claimed.

Inputs read: `docs/NOTATION.md`, complete `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 state/dynamics/existence and C.4.7.10 D.3,
and complete `three_coordinate_candidate.md`. The investigate-conjectures
and solve-math-rigorously skills govern the claim levels and derivation.
References named by the candidate to other studies were not followed.

The object is the same full p=1 population flow, with three equally weighted
unit inputs and labels in {+1,-1}. Inputs may be perturbed from the candidate's
permutation-symmetric triple; the feature dictionary and initialized matrix
are unchanged. All formulas below are current-state identities. Constants
may use the specified initialization; no fitting endpoint or future path is
an input. Finite-time perturbation statements mean each separately fixed
T<infinity. The final matrix inequality is a sufficient, unproved estimate
for an all-time extension, not a conclusion of this calculation.

## 1. Signed outputs and all three tangent blocks

Absorb each sign into its input: v_i=y_i u_i. Oddness of this bias-free
network gives m_i=y_i f(u_i)=f(v_i), with target one. At a current state
X=(w,c,M), write

\[
 h_i^1=\tanh(w\cdot v_i),\quad t_i=1-(h_i^1)^2,
 \quad a_i=E_1[b_1h_i^1],
\]
\[
 Z_i=b_2^TMa_i,\quad H_i=\tanh Z_i,\quad s_i=1-H_i^2,
 \quad d_i=E_2[b_2c s_i],\quad Q_i=b_1^TM^Td_i.
\]

In the physical metric E_1|dw|^2+E_2|dc|^2+||dM||_F^2, the full
gradient g_i=grad m_i has blocks

\[
 g_i^c=H_i,\qquad g_i^M=d_i a_i^T,\qquad
 g_i^w=t_iQ_i v_i.                                           \tag{1}
\]

Consequently its ordinary 3-by-3 tangent Gram G_ij=<g_i,g_j> is exactly

\[
 \begin{split}
 G_{ij}&=G^c_{ij}+G^M_{ij}+G^w_{ij},\\
 G^c_{ij}&=E_2[H_iH_j],\\
 G^M_{ij}&=(d_i\cdot d_j)(a_i\cdot a_j),\\
 G^w_{ij}&=(v_i\cdot v_j)E_1[t_i t_j Q_iQ_j].
 \end{split}                                                \tag{2}
\]

The two factors in G^M are ordinary coefficient inner products. The last
line retains first-layer gates, backward interactions, and input geometry.
There is no independent reverse matrix: Q_i uses this same M transposed.
Each block is positive semidefinite as a Gram, but its off-diagonal entries
and its mean/disagreement couplings need not have a sign.

## 2. Exact mean/disagreement decomposition

Define

\[
 F=\tfrac13\sum_i m_i,\quad e=1-F,\quad
 \delta_i=m_i-F,\quad V=\tfrac13|\delta|^2,
 \quad q=E_2c^2,
\]
\[
 \bar g=\tfrac13\sum_i g_i,\quad
 z=\tfrac13\sum_i\delta_i g_i,\quad
 K=\|\bar g\|^2,\quad B=\langle\bar g,z\rangle,
 \quad D_\delta=\|z\|^2.
\]

Thus sum_i delta_i=0 and mathcal L=e^2+V. The symbol D_delta is a
scalar and is unrelated to the fixed initialized matrix D. The exact flow is

\[
 \dot X=2e\bar g-2z,\qquad
 \dot m=-\tfrac23G(m-\mathbf1).                            \tag{3}
\]

In particular

\[
 \dot F=2eK-2B,\qquad \dot V=4eB-4D_\delta,                 \tag{4}
\]
\[
 \dot q=4eF-4V,\qquad
 \dot{\mathcal L}=-4(e^2K-2eB+D_\delta)=-\|\dot X\|^2.
                                                               \tag{5}
\]

For (4), differentiate |delta|^2/3 and use sum delta_i=0. For (5),
the c block of z is sum_i delta_i H_i/3 and
<c,z_c>=sum_i delta_i m_i/3=V. These facts give every coefficient.
The Gram expressions are

\[
 K=\tfrac19\mathbf1^TG\mathbf1,\quad
 B=\tfrac19\mathbf1^TG\delta,\quad
 D_\delta=\tfrac19\delta^TG\delta.                         \tag{6}
\]

In particular the first-layer part of the new coupling is

\[
 B^w=\tfrac19\sum_{i,j}\delta_j(v_i\cdot v_j)
                E_1[t_i t_j Q_iQ_j].                         \tag{7}
\]

If U=sum_i H_i/3 and C=E_2U^2, then F=<c,U> and

\[
 K=C+\|\nabla_M F\|_F^2+\|\nabla_wF\|_2^2,\qquad
 qK-F^2\ge0.                                                 \tag{8}
\]

Inequality (8) holds at every state by Cauchy--Schwarz. It does not imply
K>=C_0 at every state.

## 3. Derivative of the frozen scalar potential

Keep the candidate's positive initialized symmetric constant C_0 fixed.
Put

\[
 d=C_0+F^2,\quad \Psi=(1+q)/d,\quad
 a=1+C_0\Psi,\quad \Phi=a\mathcal L,
 \quad A=(1+q)K-d=(qK-F^2)+(K-C_0).
\]

The letter a in this section is a scalar weight, not the input-coordinate
parameter of the candidate or the coefficient vectors a_i. Quotient
differentiation using (4)--(5) gives

\[
 \dot\Psi=-\frac{4eFA}{d^2}-\frac{4V}{d}
                 +\frac{4(1+q)FB}{d^2}.                     \tag{9}
\]

Therefore the complete off-symmetry derivative is

\[
 \begin{split}
 \dot\Phi={}&-4a(e^2K-2eB+D_\delta)
       -\frac{4C_0\mathcal L eFA}{d^2}
       -\frac{4C_0\mathcal L V}{d}
       +\frac{4C_0\mathcal L(1+q)FB}{d^2}.                  \tag{10}
 \end{split}
\]

At delta=0 this reduces to the frozen candidate's formula. Away from
symmetry, B is the first genuine coupling with uncontrolled sign; its
coefficient includes both 8ae and 4C_0 mathcal L(1+q)F/d^2. The term
-4C_0 mathcal L V/d is favorable. Independently, the symmetric proof of
K>=C_0 no longer applies, so the sign of A is not supplied by (8).
Neither F>=0 nor e>=0 follows from the vector-valued dynamics alone.

The exact failure point in the old normalized-readout argument is also
visible, whenever F>0:

\[
 \frac d{dt}\frac q{F^2}
 =-\frac4{F^3}\left[e(qK-F^2)+FV-qB\right].              \tag{11}
\]

Thus merely adding V to the loss does not recover its scalar barrier.
Equation (11) diagnoses a proof gap; it does not prove the barrier is
false along any particular perturbed trajectory.

## 4. Perturbation order on a fixed horizon

Let v_i^epsilon be unit vectors with |v_i^epsilon-v_i^0|<=C|epsilon|,
and initialize all systems at the same (g,0,D) on the same frozen marks.
The symmetric reference satisfies delta^0=0. On every fixed [0,T], the
existence estimates bound c in L-infinity, M in norm, and w in L2 uniformly
for these nearby data. Subtract the vector fields: bounded features/gates
and |tanh'|<=1 bound their state differences by the L2/Frobenius state
difference; input errors have the bound

\[
 \|w\cdot(v_i^epsilon-v_i^0)\|_2
 \le\|w\|_2|v_i^epsilon-v_i^0|.
\]

The backward factors Q_i have a common supremum bound on [0,T], so
subtracting lower gates does not multiply two unrestricted L2 factors.
The integral comparison and the elementary integrating-factor inequality
give ||X^epsilon-X^0||<=C_T|epsilon|. Applying the same product estimates
to (1) yields ||G^epsilon-G^0||<=C_T|epsilon|. This argument uses L2 for
w differences: varying the input against unbounded g need not be small
in the essential-supremum norm.

At the symmetric state G^0 commutes with every input permutation, hence
G^0=alpha(t)I+beta(t)11^T. Its row sums agree, so 1^TG^0 delta=0 for
every zero-sum delta. Equations (6) then imply, uniformly on [0,T],

\[
 \delta=O_T(\epsilon),\quad V=O_T(\epsilon^2),\quad
 B=\tfrac19\mathbf1^T(G^epsilon-G^0)\delta
       =O_T(\epsilon^2),\quad D_\delta=O_T(\epsilon^2).
                                                               \tag{12}
\]

By contrast F-F^0, q-q^0 and K-K^0 may be O_T(epsilon). In particular
freezing C_0 does not remove a first-order change of the mean metric.
Also mathcal L-mathcal L^0=-2e^0(F-F^0)+(F-F^0)^2+V may be first
order. Only a purely non-invariant first variation, whose group average
vanishes, annihilates first variations of invariant scalar observables.
That is an additional symmetry condition on the perturbation.

For a differentiable one-parameter family, the more precise transverse
equation below explains the quadratic term. Let E be any fixed 3-by-2
matrix with E^TE=I and E^T1=0, and define

\[
 \zeta=E^T\delta/\sqrt3,\quad
 b=E^TG\mathbf1/(3\sqrt3),\quad H_\perp=E^TGE/3.
\]

Then V=|zeta|^2, B=b^Tzeta, D_delta=zeta^TH_perp zeta and

\[
 \dot\zeta=2eb-2H_\perp\zeta.                            \tag{13}
\]

At symmetry b^0=0 and H_perp^0=nu(t)I_2. Writing zeta=epsilon zeta_1
and b=epsilon b_1 to first order gives

\[
 \dot\zeta_1=2e^0b_1-2\nu\zeta_1,\qquad
 \frac d{dt}|\zeta_1|^2=4e^0b_1^T\zeta_1-4\nu|\zeta_1|^2.
                                                               \tag{14}
\]

The coefficient b_1 depends on the first variation of the complete state
and on the input perturbation; it is not an independently prescribed
forcing. Since c(0)=0, zeta(0)=0. If the perturbed initial tangent Gram
has b(0)!=0, (13) gives zeta(t)=2tb(0)+o(t), V(t)=4t^2|b(0)|^2+o(t^2).
Disagreement can therefore be produced while total loss is decreasing.
No estimate in (12) is uniform as T tends to infinity.

## 5. A concrete disagreement correction and its missing estimate

Let H_perp be positive definite on the region under consideration and
R=H_perp^{-1}. The following candidate is defined only on that region:

\[
 \Phi_\kappa=\Phi+\kappa\zeta^TR\zeta,\qquad\kappa>0.    \tag{15}
\]

It is a current-state expression, vanishes as a correction on the
symmetric path, and is O_T(epsilon^2) on a fixed interval where R stays
bounded. At initialization positive definiteness follows from the
candidate's rank-three upper-field Gram. Persistence is not established
by that initial fact. A ridge inverse would be globally defined but
would change the following dissipation identity and would not itself
prove transverse noncollapse.

Differentiating R gives dot R=-R dot H_perp R. Equations (13) and (15)
therefore give exactly

\[
 \dot\Phi_\kappa=\dot\Phi-4\kappa V
      +4\kappa e\zeta^TRb
      -\kappa\zeta^TR\dot H_\perp R\zeta.                 \tag{16}
\]

The last term is essential. An instantaneous positive tangent Gram does
not control a potential using its inverse if the Gram evolves rapidly.

Here is a precise sufficient inequality, with all normalizations fixed.
Set xi=(-e,zeta)^T, so mathcal L=|xi|^2, and

\[
 \mathsf H=\begin{pmatrix}K&b^T\\ b&H_\perp\end{pmatrix},
 \qquad P=\begin{pmatrix}a&0\\0&aI_2+\kappa R\end{pmatrix}.
\]

Then dot xi=-2 mathsf H xi and Phi_kappa=xi^TPxi. Consequently

\[
 2(\mathsf HP+P\mathsf H)-\dot P\succeq\lambda P
 \quad\Longrightarrow\quad
 \dot\Phi_\kappa\le-\lambda\Phi_\kappa.                  \tag{17}
\]

Everything in dot P is a current-state directional derivative along the
given physical flow, including dot a=C_0 dot Psi from (9). More explicitly,
define

\[
 s=4aK-\dot a-\lambda a,
 \quad v=(4aI_2+2\kappa R)b,
\]
\[
 T=4aH_\perp+4\kappa I_2-\dot aI_2
       +\kappa R\dot H_\perp R
       -\lambda(aI_2+\kappa R).
\]

For s>0, condition (17) is equivalent to the explicit 2-by-2 test

\[
 T\succeq vv^T/s.                                           \tag{18}
\]

This equivalence follows by completing the square in the scalar first
coordinate of the block quadratic form. To turn this route into an
all-time theorem one must prove H_perp stays invertible and (18) with
some fixed lambda>0 and kappa>0 on the reached states. Those estimates
are **open here**. They include the first-layer terms through G, b,
H_perp and dot H_perp; discarding G^w would test a different condition.
If established for all time, (17) gives loss decay because
Phi_kappa>=mathcal L. Together with the exact energy identity, this
would also give a full physical-Hilbert-state limit without a separate
uniform tangent coercivity estimate: on successive intervals of length
one, Cauchy--Schwarz gives

\[
 \int_t^\infty\|\dot X(s)\|\,ds
 \le\sum_{n=0}^\infty\sqrt{\mathcal L(t+n)}
 \le\frac{\sqrt{\Phi_\kappa(0)}e^{-\lambda t/2}}
                  {1-e^{-\lambda/2}}.
\]

Completeness then gives a strong L2/Frobenius limit. The network map is
continuous in these norms at a convergent sequence (use bounded tanh
and its Lipschitz bound), so its limiting predictions fit the data.
This conditional argument does not prove (17), or an L-infinity limit.

## 6. The metric derivative is explicitly computable from the present state

For fixed data v_i the following product rules contain every layer:

\[
 \dot a_i=E_1[b_1t_i(\dot w\cdot v_i)],\quad
 \dot Z_i=b_2^T(\dot M a_i+M\dot a_i),\quad
 \dot H_i=s_i\dot Z_i,
\]
\[
 \dot d_i=E_2[b_2(\dot c\,s_i-2cH_i s_i\dot Z_i)],\quad
 \dot Q_i=b_1^T(\dot M^Td_i+M^T\dot d_i),\quad
 \dot t_i=-2h_i^1t_i(\dot w\cdot v_i),
\]
\[
 \dot g_i^c=\dot H_i,\quad
 \dot g_i^M=\dot d_i a_i^T+d_i\dot a_i^T,\quad
 \dot g_i^w=(\dot t_iQ_i+t_i\dot Q_i)v_i,
\]
\[
 \dot G_{ij}=\langle\dot g_i,g_j\rangle
                  +\langle g_i,\dot g_j\rangle,\qquad
 \dot H_\perp=E^T\dot GE/3.                                \tag{19}
\]

Insert the three block velocities from (3). This uses no history or
unavailable derivative data. The finite-horizon boundedness already
listed justifies differentiation of these population integrals.

The established output is (1)--(14), (16), and the equivalence/implication
(17)--(19). The proposed witness is (15). The unresolved mechanism is
control of transverse metric decay and mean/transverse coupling over
all time. Epsilon expansion identifies the missing quadratic terms and
their first-layer content; it does not supply that control by itself.
