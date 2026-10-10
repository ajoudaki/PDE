# A tight-scale upper bound for independent identity-network trajectories

This internally checked proof is dated 2026-10-10. Its scientific inputs
are the canonical setup and dense fitting lemma in `paper/compact.tex`
and `paper/compact_fitting.tex`, together with the scaled identity
equations in `ORIGINAL_OUTPUT_ANALYSIS.md`. No source-carrier estimate,
Legendre approximation estimate, other study, or experiment is used.

For the identity-activation problem with \(m=d=L=2\), normalized
training inputs \(v_1=e_1,v_2=e_2\), and a fixed nonzero label vector
\(y\in\mathbb R^2\) obeying the paper's sufficient small-label condition,
two independent canonical dense runs satisfy

\[
\sup_{t\in[0,\infty],\ \|x\|_2=\sqrt2}
 |f_n(t,x)-\widetilde f_n(t,x)|=O_{\mathbb P}(n^{-1/2}).       \tag{1}
\]

The constant in this fixed-problem statement may depend on \(y\).
Here \(t=\infty\) denotes the fitted limit; a missing global trajectory
or fitted limit is counted as failure. The conclusion is an upper
bound, not by itself a matching lower bound.

The proof first controls the dependence of prediction velocities on
initialization. Their Lipschitz constants decay integrably in time.
Extending each scalar velocity from the good initialization set to the
full Gaussian space then permits an integrated variance estimate.
There is no discretization of time and no logarithmic loss.

## The scaled flow and its deterministic good set

Write the mobility coordinates and their Euclidean norm as

\[
\theta=(A,B,c)=\left(W^{(1)}/\sqrt n,W^{(2)},w/\sqrt n\right),
\qquad
\|\theta\|^2=\|A\|_F^2+\|B\|_F^2+\|c\|_2^2,
\]

where \(A\in\mathbb R^{n\times2}\),
\(B\in\mathbb R^{n\times n}\), and \(c\in\mathbb R^n\).
The training prediction vector, residual, and loss are

\[
F(\theta)=A^\top B^\top c\in\mathbb R^2,
\qquad r=F(\theta)-y,
\qquad \mathcal L=\tfrac12\|r\|_2^2.
\]

At a normalized query \(v\in\mathbb R^2\),
\(f_n(t,\sqrt2v)=v^\top F(\theta(t))\). Thus the whole-sphere
discrepancy of two runs is exactly the Euclidean discrepancy of their
two training predictions at each time.

If \(J(\theta)=DF(\theta)\) uses the displayed Euclidean parameter
norm and the ordinary Euclidean sample norm, the canonical flow is

\[
\begin{aligned}
\dot A&=-B^\top c r^\top, &
\dot B&=-c(Ar)^\top, &
\dot c&=-BAr,
\end{aligned}
\qquad \dot\theta=-J(\theta)^\top r.                        \tag{2}
\]

All factors agree with the paper: \(2/m=1\), and its mobilities become
the Euclidean metric after this scaling.

Let \(Z=(Z_A,Z_B)\in\mathbb R^{2n+n^2}\) have independent standard
Gaussian entries. Initialization is

\[
A_0=Z_A/\sqrt n,\qquad B_0=Z_B/\sqrt n,\qquad c_0=0.        \tag{3}
\]

Let \(\mathcal G_n\) be the set of roots \(z\) whose matrices in
(3) satisfy

\[
\|A_0\|_{\mathrm{op}}\le8,\quad
\|B_0\|_{\mathrm{op}}\le8,\quad
\max\{\|A_0\|_{\mathrm{op}},\|B_0A_0\|_{\mathrm{op}}\}
 \le\tfrac32,\quad
A_0^\top B_0^\top B_0A_0\succeq\tfrac12 I_2.               \tag{4}
\]

This is precisely the initialization event of the dense fitting lemma
for the present identity network: its population feature Grams are
\(I_2\), hence \(H=\gamma=1\). That lemma gives
\(\mathbb P(Z\in\mathcal G_n)\to1\). The set \(\mathcal G_n\)
is closed and bounded in the finite-dimensional root space, hence
compact. For \(n\ge2\), it is nonempty: choose \(A_0\) with its
columns the first two coordinate vectors and \(B_0=I_n\).

Set \(R=\|y\|_2>0\) and \(\kappa=1/4\). For every root in
\(\mathcal G_n\), the dense fitting lemma gives a global, convergent
trajectory satisfying, for every \(t\ge0\),

\[
\begin{gathered}
\|A(t)\|_{\mathrm{op}}\le9,\qquad
\|B(t)\|_{\mathrm{op}}\le9,\qquad \|c(t)\|_2\le2R,\\
\|r(t)\|_2\le Re^{-\kappa t},\qquad
A(t)^\top B(t)^\top B(t)A(t)\succeq\kappa I_2.
\end{gathered}                                                \tag{5}
\]

The readout block of \(J\) is \(A^\top B^\top\). Consequently,
with the unnormalized tangent Gram \(K(\theta)=J(\theta)J(\theta)^\top\),

\[
\dot r=-Kr,\qquad K\succeq A^\top B^\top BA\succeq\kappa I_2.
                                                               \tag{6}
\]

## Dimension-free stability and velocity sensitivity

The set of states obeying the first line of (5) is convex. On that
set, both the output Jacobian and output Hessian have bounds independent
of \(n\). Indeed, for an increment \(u=(U_A,U_B,u_c)\),

\[
DF(\theta)[u]
 =U_A^\top B^\top c+A^\top U_B^\top c+A^\top B^\top u_c,
\]

so \(\|J(\theta)\|_{\mathrm{op}}\le M_1:=81+36R\). For another
increment \(v=(V_A,V_B,v_c)\), differentiation gives all six terms

\[
\begin{aligned}
D^2F(\theta)[u,v]
={}&U_A^\top V_B^\top c+V_A^\top U_B^\top c
  +U_A^\top B^\top v_c+V_A^\top B^\top u_c\\
 &+A^\top U_B^\top v_c+A^\top V_B^\top u_c.
\end{aligned}
\]

Each term is bounded by the appropriate physical norm in (5), times
\(\|u\|\|v\|\). Therefore

\[
\|D^2F(\theta)[u,v]\|_2\le M_2\|u\|\|v\|,
\qquad M_2:=36+4R.                                         \tag{7}
\]

In particular, no bound on the width-dependent quantity
\(\|B\|_F\) is required.

Compare any two trajectories from \(\mathcal G_n\), denoting the
second by tildes. Write \(d=\theta-\widetilde\theta\),
\(e=\|d\|\), and \(\Delta r=r-\widetilde r\). The segment joining
their states lies in the convex set above. Taylor's integral formula
and (7) imply

\[
\|\Delta r-\widetilde Jd\|_2\le\tfrac12M_2 e^2,
\qquad \|(J-\widetilde J)d\|_2\le M_2e^2.                  \tag{8}
\]

Subtracting the two gradient flows, retaining the negative square, gives

\[
\begin{aligned}
\tfrac12\partial_t e^2
 &=-\|\Delta r\|_2^2
   +\langle\Delta r,\Delta r-\widetilde Jd\rangle
   -\langle r,(J-\widetilde J)d\rangle\\
 &\le\tfrac12 M_2(3\|r\|_2+\|\widetilde r\|_2)e^2.
\end{aligned}
\]

Integrating this inequality and (5), with the usual
\(\sqrt{e^2+\varepsilon^2}\) regularization at zeros if needed,
proves

\[
e(t)\le C_0e(0),\qquad C_0=\exp(2M_2R/\kappa).             \tag{9}
\]

Also, integrating (7) along the same segment gives

\[
\|K-\widetilde K\|_{\mathrm{op}}
 \le 2M_1M_2 e(t)\le2M_1M_2 C_0e(0).                       \tag{10}
\]

Every initialization has zero readout, so
\(\Delta r(0)=0\). Equation (6) yields

\[
\partial_t\Delta r=-K\Delta r-(K-\widetilde K)\widetilde r.
\]

The evolution operator for \(\dot u=-K(t)u\) has norm at most
\(e^{-\kappa(t-s)}\) from time \(s\) to time \(t\): differentiation
gives \(\partial_t\|u\|_2^2\le-2\kappa\|u\|_2^2\).
Variation of constants, (5), and (10) therefore give

\[
\|\Delta r(t)\|_2
 \le C_1 e(0)t e^{-\kappa t},\qquad
C_1=2M_1M_2C_0R.                                         \tag{11}
\]

Since \(\|K\|_{\mathrm{op}}\le M_1^2\), substituting (11) into
the residual difference equation proves

\[
\|\dot F(\theta(t))-\dot F(\widetilde\theta(t))\|_2
 \le C_2 e(0)(1+t)e^{-\kappa t},
\qquad C_2=C_1\max\{1,M_1^2\}.                            \tag{12}
\]

Here \(\dot F(\theta(t))\) denotes the actual time derivative of the
training prediction vector along (2), not an independent state
function without its flow. Equivalently it is \(-K(\theta(t))r(t)\).

For roots \(z,\widetilde z\) in (3),
\(e(0)=\|z-\widetilde z\|_2/\sqrt n\). Hence, for each coordinate
\(a\in\{1,2\}\), the scalar function

\[
V_a(t,z)=\frac d{dt}F_a(\theta_z(t)),\qquad z\in\mathcal G_n,
\]

is Lipschitz in \(z\), with the deterministic constant

\[
L_n(t)=\frac{C_2}{\sqrt n}(1+t)e^{-\kappa t}.                \tag{13}
\]

## Gaussian extension and the all-time estimate

For \(t\ge0\) and any root \(z\in\mathbb R^{2n+n^2}\), define
the scalar McShane extension

\[
\overline V_a(t,z)
 =\min_{u\in\mathcal G_n}\{V_a(t,u)+L_n(t)\|z-u\|_2\}.     \tag{14}
\]

The minimum is finite and attained because \(\mathcal G_n\) is
nonempty and compact. The Lipschitz inequality (13) shows that
\(\overline V_a=V_a\) on \(\mathcal G_n\), and the triangle
inequality shows that \(\overline V_a(t,\cdot)\) is globally
\(L_n(t)\)-Lipschitz.

There is no measurability or conditioning assumption hidden here.
The polynomial ODE (2) is locally Lipschitz. Its solutions from the
compact good set exist globally and stay bounded on every finite
time interval. Continuous dependence for that ODE makes
\((t,u)\mapsto V_a(t,u)\) continuous on
\([0,T]\times\mathcal G_n\) for every finite \(T\).
Taking a minimum over the fixed compact set in (14) then gives a
jointly continuous function of \((t,z)\). In particular the integrals
below are measurable.

For a globally \(L\)-Lipschitz scalar function \(g\) on a standard
Gaussian space, the Gaussian Poincare inequality gives

\[
\operatorname{Var}(g(Z))\le L^2.                            \tag{15}
\]

Its dimension-free form is recalled below. The function (14) has at
most linear growth in \(z\), hence belongs to Gaussian \(L^2\),
and satisfies all hypotheses of (15). For independent standard roots
\(Z,\widetilde Z\), independence and identical distribution give

\[
\begin{aligned}
\mathbb E|\overline V_a(t,Z)-\overline V_a(t,\widetilde Z)|
 &\le\big(2\operatorname{Var}(\overline V_a(t,Z))\big)^{1/2}\\
 &\le\sqrt2 L_n(t).
\end{aligned}                                                \tag{16}
\]

This applies to the unconditioned Gaussian roots. It does not apply
a Gaussian inequality to their distribution conditioned on (4).

Define the nonnegative random variable

\[
Q_n=\sum_{a=1}^2\int_0^\infty
 |\overline V_a(t,Z)-\overline V_a(t,\widetilde Z)|\,dt.
\]

Tonelli's theorem, (13), and (16) give

\[
\mathbb E Q_n
 \le\frac{2\sqrt2 C_2}{\sqrt n}
       \left(\frac1\kappa+\frac1{\kappa^2}\right)
 =\frac{C_3}{\sqrt n}.                                    \tag{17}
\]

On the event \(Z,\widetilde Z\in\mathcal G_n\), both prediction
vectors start at zero and (14) equals their actual velocities.
For every finite \(T\), the fundamental theorem of calculus and the
Euclidean triangle inequality therefore give

\[
\|F(\theta_Z(T))-F(\theta_{\widetilde Z}(T))\|_2\le Q_n.
\]

Both vectors converge to \(y\), so this bound also holds at the
fitted endpoint. The identity-query formula preceding (2) consequently
gives the whole-sphere, all-time discrepancy bound by \(Q_n\) on
this event.

Write that discrepancy as \(D_n\), allowing \(D_n=+\infty\) when
a required trajectory or fitted limit is missing. For every \(M>0\),
the union bound and Markov's inequality now give

\[
\mathbb P\{\sqrt n D_n>M\}
 \le2\mathbb P\{Z\notin\mathcal G_n\}+\frac{C_3}{M}.         \tag{18}
\]

The first term tends to zero. Taking the limiting superior in \(n\)
and then letting \(M\to\infty\) proves (1). In particular, for
each fixed failure probability, its eventual bound has a constant
times \(n^{-1/2}\), with no power of \(\log n\).

## The Gaussian inequality used above

For completeness, (15) follows directly from Gaussian integration by
parts. In any finite dimension, define

\[
P_sg(z)=\mathbb E g(e^{-s}z+\sqrt{1-e^{-2s}}\,Z'),
\]

where \(Z'\) is an independent standard Gaussian vector. First let
\(g\) be smooth and globally \(L\)-Lipschitz. The Gaussian law is
invariant under \(P_s\), its generator is
\(\Delta-z\cdot\nabla\), and integration by parts gives

\[
\frac d{ds}\mathbb E(P_sg(Z))^2
 =-2\mathbb E\|\nabla P_sg(Z)\|_2^2,
\qquad
\nabla P_sg=e^{-s}P_s(\nabla g).
\]

Linear growth ensures all integrals exist; Gaussian integration by
parts can be justified by smooth compact cutoffs and Gaussian tail
decay. The displayed integral definition and the Lipschitz bound give
\(P_sg\to\mathbb Eg(Z)\) in Gaussian \(L^2\) as \(s\to\infty\).
Integrating the derivative identity therefore gives

\[
\operatorname{Var}(g(Z))
 =2\int_0^\infty\mathbb E\|\nabla P_sg(Z)\|_2^2\,ds
 \le2L^2\int_0^\infty e^{-2s}\,ds=L^2.
\]

For an arbitrary globally Lipschitz \(g\), convolution with a smooth
compactly supported approximate identity preserves its Lipschitz
constant and converges uniformly to \(g\). Passing to the limit in
Gaussian \(L^2\) proves (15) in the exact form used in (16).
