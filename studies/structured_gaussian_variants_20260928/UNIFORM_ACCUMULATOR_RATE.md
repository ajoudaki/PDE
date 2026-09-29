# Uniform rate for the accumulator of the closure's own responses

Frozen bounded continuation, 2026-09-29. Inputs: the scoped assignment and
this route's BLOCK_PARTICLE_RATE.md. This is an internally checked source
estimate. It does not compare two trained trajectories or identify a dense
population limit.

**Result.** Under the operator cap, common initial Gram gap, and uniform
small-label condition in Sections 1--3 of BLOCK_PARTICLE_RATE.md, the
response-memory closure satisfies

\[
 \sup_{t\ge0}
 \|W_\ell^{\rm corr}(t)-A_\ell^{\rm own}(t)\|_{\rm op}
 \le \int_0^\infty\|\mathcal D_\ell(t)\|_{\rm op}\,dt
 \le \frac{C_{\rm acc}S_\infty^3}{q}
 \le \frac{C_{\rm acc}}q\left(\frac{2Y_0}{\gamma}\right)^3.
\tag{1}
\]

The constant is explicit below and independent of \(B,k,q\). Here

\[
 A_\ell^{\rm own}(t)
 =-\frac{2\kappa_\ell}m\sum_a\int_0^t
      r_a(v)\delta_a^{(\ell)}(v)\otimes h_a^{(\ell-1)}(v)\,dv
\tag{2}
\]

integrates the responses of the **same finite-\(q\) closure**, and

\(\mathcal D_\ell=\dot W_\ell^{\rm corr}-\dot A_\ell^{\rm own}\).
Neither \(A_\ell^{\rm own}\) nor its sources are taken from exact gradient
flow. The operator in (2) is an analytical comparator, not extra stored
state in the closure.

## 1. Setup and already established bounds

Use the notation and equations of BLOCK_PARTICLE_RATE.md. In particular,

\[
 S(t)=\int_0^t\rho(v)\,dv,\qquad \tau(t)=1+S(t),\qquad
 \kappa=\max_\ell\kappa_\ell,\qquad
 g=\max_{a,b}|G_{ab}|.
\]

The initial blocks have norm at most \(M\), the activation is tanh, the
stored readout starts at zero, and the forward and backward history prefixes
are respectively \(h(0)\) and zero. There are \(q\ge1\) modes numbered
\(0,\ldots,q-1\). Set

\[
 D_*=2\kappa(M+1)^{L-1},\qquad
 J=2\kappa\sqrt{2m}\,D_*.
\tag{3}
\]

The uniform fitting theorem supplies, with the same \(s_0,\gamma,Y_0\)
defined there,

\[
 S_\infty\le 2Y_0/\gamma\le s_0/2,\qquad
 s_0\le1,\qquad J s_0^{3/2}\le1,
\tag{4}
\]

and, whenever \(s=S(t)\le s_0\),

\[
\begin{aligned}
 \sup_\omega\|\delta_a^{(\ell)}(t,\omega)\|_2/\sqrt k
   &\le D_*s,\\
 \sup_\omega\|X_{\ell-1,a}(t,\omega)\|_F/\sqrt k
   &\le\sqrt{1+s}\le\sqrt2,\\
 \sup_\omega\|Y_{\ell,a}(t,\omega)\|_F/\sqrt k
   &\le\sqrt{m/3}\,D_*s^{3/2}.
\end{aligned}
\tag{5}
\]

The law \(\mu\) can be the capped block law or any empirical law satisfying
the initial Gram assumption. A common positive Gram lower bound is needed
when varying \(k\). No additional coordinatewise backward bound is imposed.

For operator estimates use

\[
 \mathcal H=L^2(\mu;\mathbb R^k),\qquad
 \|v\|_{\mathcal H}^2=\mathbb E_\mu\|v\|_2^2/k.
\]

Then \(v\otimes w\) means \(g\mapsto
v\,\mathbb E_\mu(w^Tg/k)\), and
\(\|v\otimes w\|_{\rm op}=\|v\|_{\mathcal H}\|w\|_{\mathcal H}\).
For an empirical law this is precisely the ordinary finite operator with
rank-one matrix \(vw^T/n\); multiplying the vector norm by \(1/\sqrt n\)
does not change its operator norm.

We use activity \(s\) as the independent variable on intervals where
\(\rho>0\). If the residual reaches zero, the autonomous physical flow
stops, and no later interval contributes to any estimate. For each fixed
finite \(k,q\), the activity-parametrized state has locally bounded
derivative: \(r/\rho\) is bounded and all the remaining factors in its
equations are bounded on the region (4)--(5). No derivative of \(r/\rho\)
will be used. The estimates below extend to limiting activity endpoints
by monotone convergence.

## 2. The final-interval projection identity

For fixed terminal activity \(S\), put \(T=1+S\). Let

\[
 e_{j,T}(x)=\sqrt{\frac{2j+1}{T}}\,
              P_j(2x/T-1),\qquad 0\le x\le T,
\]

where \(P_j\) is the ordinary Legendre polynomial. Write \(\Pi_{q,T}\)
for orthogonal projection onto these first \(q\) modes, componentwise for
vector-valued histories.

Take a vector-valued activity source \(v(s)\), with zero history on
\([0,1]\), and define its final history

\[
 v^{[S]}(x)=
 \begin{cases}
 0,&0\le x\le1,\\
 v(x-1),&1<x\le1+S.
 \end{cases}
\]

Its moment coefficients at intermediate activity \(s\) are

\[
 Z_j(s)=\int_0^{1+s} e_{j,1+s}(x)v^{[s]}(x)\,dx.
\tag{6}
\]

Differentiating this expression, or differentiating the unnormalized
Legendre integrals first, gives

\[
 Z'=\frac1{1+s}DZ+\frac1{\sqrt{1+s}}bv,\qquad
 Z(0)=0,\qquad
 \widehat v(s)=\frac{b^TZ(s)}{\sqrt{1+s}},
\tag{7}
\]

where \(D+D^T=-bb^T\) and \(b_j=\sqrt{2j+1}\). These are exactly the
closure's old-clock coefficient equations after division by \(\rho\).
Formula (6) also follows for merely square-integrable sources from the
linear integral equation, so no derivative of \(v\) is required.

The endpoint-error identity and orthogonality at the **final** interval
give

\[
\begin{aligned}
 \int_0^S\|v(s)-\widehat v(s)\|_2^2\,ds
 &=\int_0^S\|v(s)\|_2^2\,ds-\sum_{j<q}\|Z_j(S)\|_2^2\\
 &=\|(I-\Pi_{q,T})v^{[S]}\|_{L^2([0,T])}^2.
\end{aligned}
\tag{8}
\]

Indeed, differentiating \(\sum_j\|Z_j\|_2^2\) using (7) yields
\(-\|\widehat v\|_2^2+2\langle v,\widehat v\rangle\); integrate and
complete the square. Formula (6) identifies the terminal sum as the norm
of the final orthogonal projection.

This identity does **not** say that \(\widehat v(s)\) is the value of the
final-\(T\) projection at \(1+s\). At each intermediate time it is the
endpoint value of the projection on \([0,1+s]\). The equality of the
integrated error to the final projection tail is the energy identity.

For a forward feature put \(v(s)=h(s)-h(0)\). Its zero-prefix coefficients
are \(X(s)-\sqrt{1+s}\,e_0h(0)\), and its endpoint error is
\(v-\widehat v=h-\widehat h\). Thus (8) applies exactly, with
the prescribed constant forward prefix; it does not introduce a different
initializer or clock.

## 3. Weighted Legendre \(H^1\) estimate

For any finite-dimensional Hilbert-valued \(f\in H^1([0,T])\),

\[
 \|(I-\Pi_{q,T})f\|_{L^2([0,T])}
 \le \frac{T}{2\sqrt{q(q+1)}}\,
                  \|f'\|_{L^2([0,T])}.
\tag{9}
\]

The normalization of the Hilbert norm is immaterial; in particular it can
be block RMS. Here is a proof retaining the weight and endpoints.

The normalized Legendre polynomials satisfy

\[
 -\frac d{dx}\left[x(T-x)e_{j,T}'(x)\right]
       =j(j+1)e_{j,T}(x).
\tag{10}
\]

This is the ordinary Legendre differential equation after the affine
change of variable. The polynomial identity follows, for example, by
differentiating Rodrigues' formula
\(P_j(z)=(2^jj!)^{-1}(d/dz)^j(z^2-1)^j\).
They are orthonormal on \([0,T]\). Let
\(c_j=\int_0^T f e_{j,T}\), and
\(p_N=\sum_{j=1}^N c_j e_{j,T}\). Since the weight \(x(T-x)\) vanishes
at both endpoints, integration by parts in (10) has no boundary term,
including for \(H^1\) functions by their absolutely continuous
representatives. It gives

\[
\begin{aligned}
 \sum_{j=1}^N j(j+1)\|c_j\|^2
 &=\int_0^T x(T-x)\langle f',p_N'\rangle\,dx,\\
 \int_0^T x(T-x)\|p_N'\|^2\,dx
 &=\sum_{j=1}^N j(j+1)\|c_j\|^2.
\end{aligned}
\]

Cauchy--Schwarz therefore implies

\[
 \sum_{j=1}^N j(j+1)\|c_j\|^2
 \le\int_0^T x(T-x)\|f'\|^2dx
 \le\frac{T^2}4\int_0^T\|f'\|^2dx.
\]

Let \(N\to\infty\). Polynomials are dense in \(L^2([0,T])\), componentwise:
continuous functions are dense, and their Bernstein polynomial
approximations converge uniformly after rescaling to \([0,1]\). Parseval
and \(j(j+1)\ge q(q+1)\) for \(j\ge q\) now prove (9).
The same inequality averaged over marks follows by Tonelli.

For the forward zero-prefix history in Section 2, its value at the
prefix/training interface is zero. Hence this history belongs to \(H^1\)
whenever the activity feature does, and its derivative norm is just the
derivative norm on the training interval. Combining (8) and (9),

\[
 \left(\int_0^S
       \|h(s)-\widehat h(s)\|_2^2/k\,ds\right)^{1/2}
 \le\frac{1+S}{2\sqrt{q(q+1)}}
       \left(\int_0^S\|\partial_s h(s)\|_2^2/k\,ds\right)^{1/2}.
\tag{11}
\]

## 4. A uniform activity-derivative bound

Define

\[
 H_\ell(S)=\max_a\sup_\omega
       \left(\int_0^S
           \|\partial_s h_a^{(\ell)}(s,\omega)\|_2^2/k\,ds
       \right)^{1/2}.
\tag{12}
\]

The supremum is outside the integral. For each fixed finite \(k,q\) this
quantity is initially finite on bounded activity intervals, by the local
boundedness noted in Section 1. We now bound it uniformly in \(k,q\).

Set \(U_a=(r_a/\rho)\delta_a^{(\ell)}\) and
\(E_{U,a}=U_a-\widehat U_a\). Bounds (5), \(|r_a|/\rho\le\sqrt m\),
and \(\|b\|_2=q\) give the deterministic bound

\[
 \sup_{0\le s\le S,\,a,\omega}
      \|E_{U,a}(s,\omega)\|_2/\sqrt k
 \le\sqrt m\,D_*
           \left(S+\frac{qS^{3/2}}{\sqrt3}\right).
\tag{13}
\]

This deliberately retains the endpoint factor \(q\). It will cancel
against the forward projection estimate, rather than being discarded.

At the first layer, division of its raw equation by \(\rho\) gives

\[
 \|\partial_s u_a\|_2/\sqrt k\le2\kappa gD_*s,
 \qquad
 H_1(S)\le\frac{2\kappa gD_*}{\sqrt3}S^{3/2}.
\tag{14}
\]

At a higher layer differentiate the forward equation with respect to
activity. The initialized block acting on the preceding derivative costs
\(M H_{\ell-1}\). The learned operator acting on that derivative costs
\(J S^{3/2}H_{\ell-1}\). To justify the latter without exchanging
supremum and integral, apply the uniform moment bounds (5), then use

\[
 \int_0^S\mathbb E_\mu
      \|\partial_s h_a^{(\ell-1)}\|_2^2/k\,ds
 \le H_{\ell-1}(S)^2.
\]

The exact matrix-velocity defect identity, in activity variables, is

\[
 \partial_s W_\ell^{\rm corr}
 =-\frac{2\kappa_\ell}m\sum_a
            U_a\otimes h_a^{(\ell-1)}
   +\frac{2\kappa_\ell}m\sum_a
            E_{U,a}\otimes E_{h,a},
 \quad
 E_{h,a}=h_a^{(\ell-1)}-\widehat h_a^{(\ell-1)}.
\tag{15}
\]

Applied to a current feature, whose block RMS is at most one, the first
term in (15) has activity \(L^2\) norm at most
\(2\kappa D_*S^{3/2}/\sqrt3\). Indeed
\(m^{-1}\sum_a|r_a|/\rho\le1\).

For the defect term applied to the feature of any evaluation sample, its
block RMS at mark \(\omega\) is bounded by

\[
 \frac{2\kappa}m\sum_a
       \|E_{U,a}(s,\omega)\|_2/\sqrt k
       \left(\mathbb E_\mu\|E_{h,a}(s)\|_2^2/k\right)^{1/2}.
\]

Take its activity \(L^2\) norm, use (13), then (11) averaged over marks.
The resulting bound is

\[
 \kappa\sqrt m\,D_*(1+S)
 \left[
 \frac{S}{\sqrt{q(q+1)}}+
 \frac{qS^{3/2}}{\sqrt{3q(q+1)}}
 \right]H_{\ell-1}(S)
 \le
 \kappa\sqrt m\,D_*(1+S)
       \left(\frac Sq+\frac{S^{3/2}}{\sqrt3}\right)
       H_{\ell-1}(S).
\tag{16}
\]

Because \(\|\tanh'\|_\infty\le1\), these estimates prove

\[
\begin{aligned}
 H_\ell(S)\le&
 \left[M+J S^{3/2}
   +\kappa\sqrt m\,D_*(1+S)
       \left(\frac Sq+\frac{S^{3/2}}{\sqrt3}\right)\right]
       H_{\ell-1}(S)\\
 &+\frac{2\kappa D_*}{\sqrt3}S^{3/2}.
\end{aligned}
\tag{17}
\]

Only the preceding layer's derivative appears. In particular no
activity derivative of \(U\), of the residual direction, or of a backward
feature is being assumed.

For an explicit uniform constant, put

\[
 R=M+2+4\kappa\sqrt m\,D_*,
 \qquad
 C_H=\frac{2\kappa D_*}{\sqrt3}(g+L)R^{L-1}.
\tag{18}
\]

By (4), \(S\le1\) and \(J S^{3/2}\le1\), so the coefficient in (17) is
at most \(R\). Induction from (14) gives

\[
 H_\ell(S)\le C_H S^{3/2},\qquad 1\le\ell\le L,
\tag{19}
\]

uniformly in \(B,k,q\), for every activity endpoint of the global fitting
solution. This induction also verifies all the \(H^1\) hypotheses used
successively in (11).

## 5. Integrated operator defect and the own-response accumulator

The zero-prefix backward error has the stronger integrated estimate
from (8) or the gain-one energy identity:

\[
\begin{aligned}
 \int_0^S\|E_{U,a}(s)\|_{\mathcal H}^2ds
 &\le\int_0^S\|U_a(s)\|_{\mathcal H}^2ds\\
 &\le mD_*^2 S^3/3.
\end{aligned}
\tag{20}
\]

The forward estimate (11) and (19) give

\[
 \left(\int_0^S\|E_{h,a}(s)\|_{\mathcal H}^2ds\right)^{1/2}
 \le \frac{(1+S)C_H S^{3/2}}{2\sqrt{q(q+1)}}.
\tag{21}
\]

Apply the rank-one operator norm formula and Cauchy--Schwarz in activity
to the second term of (15). Returning to physical time merely uses
\(ds=\rho\,dt\). Therefore

\[
\begin{aligned}
 \int_0^t\|\mathcal D_\ell(v)\|_{\rm op}dv
 &\le\frac{2\kappa}m\sum_a
       \left(\int_0^{S(t)}\|E_{U,a}\|_{\mathcal H}^2ds\right)^{1/2}
       \left(\int_0^{S(t)}\|E_{h,a}\|_{\mathcal H}^2ds\right)^{1/2}\\
 &\le
  \frac{\kappa\sqrt{m/3}\,D_*(1+S(t))C_H S(t)^3}
       {\sqrt{q(q+1)}}\\
 &\le \frac{C_{\rm acc}S(t)^3}{q},
 \qquad C_{\rm acc}=2\kappa\sqrt{m/3}\,D_*C_H.
\end{aligned}
\tag{22}
\]

Both \(W_\ell^{\rm corr}\) and \(A_\ell^{\rm own}\) initially vanish.
Their difference is the time integral of \(\mathcal D_\ell\), which proves
(1) by letting \(t\to\infty\) in (22).

As a separate check, at a fixed terminal activity the reconstructed
operator contracts the temporal projections of the two histories.
Orthogonality makes its difference from the own-response integral the
contraction of their two projection tails. Applying (9) only to the forward
tail and the elementary \(L^2\) bound to the backward tail gives the same
\(S^3/q\) bound for the terminal operator difference. The integrated
velocity-defect estimate (22) is stronger than that terminal check.

## 6. Scope of the new estimate

The source and accumulator bounds (19) and (22) hold at the single
small-label threshold of the uniform fitting theorem, with a common cap
and initial Gram gap. Their constants do not deteriorate with width, block
size, or memory order. They require only ordinary finite-\(k,q\) local
well-posedness to start the argument.

The conclusion concerns the accumulator of the closure's own responses.
It does not control propagation of this source error through nonlinear
training, compare residual clocks of two trajectories, establish a
finite-block population rate for fixed labels, remove the initialization
cap, or identify any trained block limit with the ordinary dense Gaussian
population. Those remain separate proof obligations. In particular, no
trajectory \(O(q^{-1})\) assertion is made.
