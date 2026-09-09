# Follow-up after the signed-driver candidate: even-channel forcing

This is a separate research handoff, not an addition to the completed
local response theorem. The candidate
\`TANGENT_SIGNED_DRIVER_RESPONSE.md\` was completed at 758 lines with
SHA-256
\`36fa3bbad7df00a6916712e23fb132489c498abd73b2e8cb382ad1780c5e701b\`.
It requires fresh independent audit. The frozen
\`UNIVERSAL_ANGLE_ROUTE.md\` remains unchanged.

## Finite-angle work recorded by the main worker

The main worker has written \`FINITE_ANGLE_Q_CHANNEL_ROUTE.md\`.
I have not read or audited that note. The main worker reports that the
finite-angle radius bound, lower bound for the scalar variational
coefficient, and forward-contrast subexponential response bound are
derived there, while the conversion to a uniform fixed-driver Jacobian
remains a proposal.

The proposed extension concerns the pure normalized bottom q-channel,
with \(\delta=\sqrt{(1-\rho)/2}\), \(\mu^2=1-\delta^2\), and
\[
 a_\delta=\frac{\phi'(M+\delta V)+\phi'(M-\delta V)}2,\qquad
 b_\delta=\frac{\phi'(M+\delta V)-\phi'(M-\delta V)}{2\delta},
 \qquad M_r=\mu^2b_\delta,\quad V_r=a_\delta.
\]
The reported scalar orbit equation uses
\[
 F_\delta(X,Y)=(1+X+\delta^2Y)(1+X+\delta^2Y+e)-4\delta^2XY,
 \qquad X_Y=-\frac{2e\mu^2X}{F_\delta(X,Y)}.
\]
The proof and the current claim statuses belong to that separate note;
this handoff does not promote its pending clock step to a theorem.

## The affine common fields are frozen

The following is the main worker's additional structural observation,
with its short algebraic verification. Work in the symmetric population
realization for opposite labels and the affine activation \(1+z\).
Use \(A,B\) for the two hidden operators. The common preactivations are
\[
 M_1=w\cdot(x_1+x_2)/2,\qquad
 M_2=A(1+M_1),\qquad M_3=B(1+M_2).
\]
The common fields are even under the exchange involution, while
\(D_1,D_2,D_3,C\) are odd. The operator actions intertwine these
involutions, so \(B^*C\) is also odd. The exact affine scalar feature
updates are
\[
 M_1'=0,\qquad A'=B^*C\otimes D_1,\qquad
 B'=C\otimes D_2.
\]
An odd field is orthogonal to every even field: applying the
measure-preserving involution changes the sign of their inner product
and also preserves it. Therefore both displayed rank-one updates
annihilate the entire even input subspace. Their time integrals do so
as well, wherever this affine flow is constructed. Consequently
\[
 M_1(s)=M_{1,0},\qquad
 M_2(s)=A_0(1+M_{1,0})=M_{2,0},\qquad
 M_3(s)=B_0(1+M_{2,0})=M_{3,0}.
\]
This is stronger than parity alone. The Gaussian initialization gives
the frozen common variances
\[
 \operatorname{Var}(M_1)=\mu^2,\qquad
 \operatorname{Var}(M_2)=1+\mu^2,\qquad
 \operatorname{Var}(M_3)=2+\mu^2.
\]
They are bounded independently of the angle. The first variance may
vanish at the antipodal endpoint. Growth of the trained affine operator
increments is confined to the odd-to-odd blocks; the initial even
blocks remain present.

The assertion uses the exact symmetric population decomposition.
It does not assert exact sample symmetry or orthogonality in an
individual independently initialized finite-width realization.

## What the nonlinear even channel adds

For any activation, on a symmetric opposite-label feature path define
the sample averages and differences
\[
 h_M=(h_1+h_2)/2,\quad h_D=(h_1-h_2)/2,\qquad
 \delta_M=(\delta_1+\delta_2)/2,\quad
 \delta_D=(\delta_1-\delta_2)/2.
\]
At a hidden matrix the exact update is
\[
 W'=\delta_M\otimes h_D+\delta_D\otimes h_M.
\]
The first term is odd-to-odd. The second is even-to-even and vanishes
in the affine opposite-label baseline. For the nonlinear candidate it
need not vanish. In normalized feature time \(u=\delta s\), the same
identity is
\[
 \frac{dW}{du}=Q\otimes k+P\otimes h,
 \qquad
 Q=\delta_M,\quad P=\delta_D/\delta,\quad
 k=h_D/\delta,\quad h=h_M.
\]
These are exactly the two operator-gradient terms in the completed
tangent candidate. The common backward input \(p\) is the normalized
difference of the original backward inputs. Its top nonzero generation
is \(p_2=B^*[C\phi''(M_3)V_3]\), with the lower-layer propagation
spelled out in that candidate.

The next obligation is therefore control of the actual even-channel
updates \(P\otimes h\), their common backward inputs, and their causal
source derivatives, while retaining the favorable frozen-even affine
baseline. Bounds for the full operator norm discard that distinction.
No quantitative nonlinear even-channel bound is established here.

The local signed-driver theorem also does not control arbitrary late
forcing by its original-initial-state bound. Starting at \((0,0)\),
advancing to driver \(R\), and reversing gives a reached state
\((0,(1+e)R)\) whose return-map common derivative is
\(\exp(e(1+e)R^2)\). The completed candidate records this exact example.
It prevents treating the uniform original-initial-state Jacobian as
a uniform propagator for late \(p\)-injections. A driver-source
perturbation instead changes total driver time and uses
\(\partial_r\Psi\); these two response mechanisms must remain distinct.

No experiments, agents, or additional proof search were performed in
making this handoff.
