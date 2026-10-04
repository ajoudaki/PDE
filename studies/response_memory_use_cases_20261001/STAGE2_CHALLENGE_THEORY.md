# Input projection can turn descent into an oscillator

Revision 2 complete: the supervisor requested checking and proving the
same obstruction for every fixed finite memory order, with the actual prefix
and activity clock. Frozen revision 1 is preserved at
data/generated/response_memory_use_cases_20261001/stage2_challenge/finite_q_v2_20261002/STAGE2_CHALLENGE_THEORY_V1.md
with SHA-256
100f4b4e4dfec236e1834559ffcd282d6597a2a600a9239e0d96ec5ef76bb567.

### Finite-order numerical check: frozen protocol before execution

This is a deterministic validation of the derived asymptotic coefficient,
not a performance experiment. Use the exact scalar-width binary construction
below with $\alpha=1$, $q\in\{1,2,4\}$ and
$\varepsilon\in\{0.02,0.01\}$; keep all canonical outer equations, the raw
Legendre equations, unit prefix, and actual residual-RMS clock.
Integrate with SciPy solve_ivp, DOP853, to
$t_*=3\pi\sqrt{3/5}$, once at rtol=1e-10, atol=1e-12, once at
rtol=1e-12, atol=1e-14. Twelve total scalar ODE solves are authorized.

Primary metric: the exact chain-rule endpoint loss derivative divided by
$\varepsilon^2/36$. H1 predicts convergence to one at fixed $q$ as
$\varepsilon$ decreases; the competing possibility is that finite temporal
order changes the leading direction or coefficient.
Pass requires all derivatives positive, all normalized values within 0.01
of one, and the deviation from one at $\varepsilon=0.01$ no larger than
0.35 times its value at $\varepsilon=0.02$ plus $10^{-7}$.
Fail means a valid negative derivative or normalized value outside that
interval. Other outcomes are inconclusive.

Validity gates: every solve succeeds; coarse/fine normalized loss derivatives
agree within $10^{-7}$; independently differentiating the reconstruction and
using the rank-two formula (12) agree within $10^{-10}$ in absolute hidden
velocity; and loss derivatives from the prediction chain rule agree with
outer dissipation plus the hidden contribution within $10^{-10}$.
No randomness, no tolerance-selection pilot, no branch or additional run.
Use at most one CPU thread and three CPU-minutes; stop after these twelve
solves. Preserve script, environment, exact outputs, and hashes in the owned
generated namespace; include the full script in this report so reproduction
does not depend on generated scratch. A pass validates the coefficient only
for these numerical instances and does not prove the finite-order theorem.

Scoped theoretical challenge, 2026-10-02. Author: `challenge_stage2`.
Status: complete derivations and internal analytic checks, with a bounded
CPU ODE validation; no independent audit or promotion. The strengthened main
result applies to every fixed finite memory order with the actual prefix and
activity clock. The untruncated flow provides a preliminary derivation.

The strongest conclusion is that input compression is an optimizer change even
with exact temporal memory, and also at every fixed finite memory order. In a two-hidden-layer tanh network started with
exactly zero readout, projecting onto the constant input function can replace a
dissipative learning mode by a small-amplitude oscillator. The **total training
loss increases at a specified finite time**, with all outer layers still
following their canonical gradient equations. This is an actual trajectory
statement, not just an arbitrary-history or arbitrary-backward-signal example.
A cheap exact loss-direction certificate applies to every finite memory order
and suggests a new, explicitly different optimizer that prevents this ascent.

## Scope, sources, and notation

Allowed scientific inputs actually read: complete `paper/main.tex`, complete
included `paper/results.tex`, `docs/notation.qmd`, and the three assigned study
files `MODEL_RECONCILIATION.md`, `INPUT_FIELD_DERIVATION.md`, and
`HISTORY_PROTOCOL_INITIAL.md`. No result report, other study, stage-two route
note, or generated experiment was read. The additional included proof files
are not dependencies: no all-time, population, or temporal-convergence theorem
is imported. Required canonical-notation, conjecture-investigation, and
rigorous-proof skills were applied. No external theorem beyond elementary
finite-dimensional linear algebra and local smooth ODE theory is used.

The initial loss-ascent criterion and oscillator construction were developed
before communication from the supervisor. Subsequently the supervisor supplied
the criterion that an input projection commutes with the current feature Gram
exactly when it is descent-preserving for every backward matrix. Section 4
proves and quantifies that disclosed criterion; it is not claimed as an
independent rediscovery. The supervisor also disclosed the existence, but not
the proof or outcome, of a separate route about moving input dictionaries.
After the first complete draft, the supervisor suggested the binary-label
variant below. Its constants and reduction were checked here; it is explicitly
credited rather than presented as an independently selected example.

Write the stored readout as $w=W^{(L+1)}$, following the paper. For a fixed
input law $\mu$, labels $y(x)$, width $n$, and $L\ge2$ hidden layers,

\[
\begin{aligned}
z^{(1)}(x)&=W^{(1)}x/\sqrt d,&h^{(1)}(x)&=\tanh z^{(1)}(x),\\
z^{(\ell)}(x)&=W^{(\ell)}h^{(\ell-1)}(x),&
h^{(\ell)}(x)&=\tanh z^{(\ell)}(x),\\
f(x)&=w^\top h^{(L)}(x)/n,&r(x)&=f(x)-y(x),\qquad
\mathcal L=\mathbb E_\mu r^2.
\end{aligned}
\]

Backward responses exclude the residual:

\[
\delta^{(L)}=w\odot\tanh'(z^{(L)}),\qquad
\delta^{(\ell)}=\tanh'(z^{(\ell)})\odot
W^{(\ell+1)\top}\delta^{(\ell+1)}.
\]

All results are finite-width and deterministic, with the canonical block
mobilities $(n,1,\ldots,1,n)$. An expectation is an exact finite average in
the counterexample and practical certificate. Population integrals can replace
these averages whenever the displayed quantities are integrable. There is no
stochastic-minibatch assertion, width limit, or asymptotic fitting assertion.
In every ungated and gated construction below, the outer equations are

\[
\dot W^{(1)}=-2\mathbb E[r\delta^{(1)}x^\top/\sqrt d],
\qquad \dot w=-2\mathbb E[rh^{(L)}].
\]

## 1. What exact temporal memory converges toward algebraically

Let $\psi_1,\ldots,\psi_C$ be fixed orthonormal functions in
$L^2(\mu)$. Their orthogonal projection, acting coordinatewise, is

\[
(P u)(x)=\sum_{c=1}^C\psi_c(x)\mathbb E_\mu[\psi_c u].
\]

For one hidden link suppress layer indices. With activity clock
$\dot\tau=\rho=(\mathbb E r^2)^{1/2}$, the history signal is
$b=r\delta/\rho$ where $\rho>0$. The prefix has zero backward response.
If temporal projection is omitted while input projection is retained, the
reconstructed matrix is exactly

\[
W(t)=W_0-\frac2n\int_0^t
\mathbb E_\mu[(P(r\delta))(P h)^\top]\,ds.
\tag{1}
\]

This follows from the activity-history formula by $d\xi=\rho\,ds$;
$P$ acts only on $x$, so the scalar $\rho(s)$ cancels. Orthogonality gives

\[
M_P:=\mathbb E[(P(r\delta))(P h)^\top]
=\mathbb E[r\delta(P h)^\top],\qquad
\dot W=-2M_P/n.
\tag{2}
\]

Equation (1), with responses recomputed through its own network, defines a
finite-dimensional autonomous filtered flow. It is the exact input-projected
history relation. Identifying it as a limit of self-consistent finite-$q$
trajectories would require a separate temporal-convergence proof; none is
assumed here.

The genuine loss gradient is $\nabla_W\mathcal L=2M/n$, where

\[
M=\mathbb E[r\delta h^\top]=M_P+M_\perp,\qquad
M_\perp=\mathbb E[((I-P)(r\delta))((I-P)h)^\top].
\]

Therefore the hidden block's contribution to loss motion is

\[
\langle\nabla_W\mathcal L,\dot W\rangle_F
=-\frac4{n^2}\bigl(\|M_P\|_F^2+
\langle M_\perp,M_P\rangle_F\bigr).
\tag{3}
\]

Orthogonality in input space annihilates mixed input pairings; it does **not**
make the resulting matrices $M_P,M_\perp$ Frobenius-orthogonal. Their inner
product can be negative enough to reverse descent. This is the precise point
where a tensor-product projection identity fails to supply a gradient-flow
interpretation.

## 2. A zero-readout trajectory with increasing total loss

**Theorem.** Fix any label scale $\alpha>0$. For every finite width
$n\ge1$, use two hidden tanh layers, no biases, two normalized inputs

\[
d=m=2,\qquad x_1=\sqrt2(1,0)^\top,\quad
x_2=\sqrt2(0,1)^\top,\qquad (y_1,y_2)=\alpha(-1,2),
\]

and the constant dictionary $C=1,\psi_1=1$. There are deterministic initial
weights with $w(0)=0$, and a nonempty open neighborhood of those first and
hidden weights, such that the filtered flow (1) has

\[
\dot{\mathcal L}(t_*)>0,
\qquad t_*={\pi\sqrt2\over\alpha}.
\tag{4}
\]

Consequently, for every fixed width this event has strictly positive
probability under independent canonical Gaussian first and hidden weights
and exactly zero readout. This is a support statement, with no lower bound
uniform in width and no assertion about typical wide initializations.

**Construction and proof.** Start first with $n=1$, writing the first row
as $u=(u_1,u_2)$, hidden weight as $v$, and readout as $w$. Set

\[
u(0)=\bigl(\operatorname{arctanh}(3/4),
\operatorname{arctanh}(1/4)\bigr),\qquad v(0)=\varepsilon,
\qquad w(0)=0.
\tag{5}
\]

Write $h_a=\tanh u_a$. Predictions and residuals are
$f_a=w\tanh(vh_a)$, $r_a=f_a-y_a$. The exact equations, including both
outer updates, are

\[
\begin{aligned}
\dot u_a&=-r_a v w\tanh'(vh_a)\tanh'(u_a),\quad a=1,2,\\
\dot w&=-\sum_{a=1}^2r_a\tanh(vh_a),\\
\dot v&=-2\left(\frac12\sum_{a=1}^2r_aw\tanh'(vh_a)\right)
\left(\frac12\sum_{a=1}^2h_a\right).
\end{aligned}
\tag{6}
\]

At $\varepsilon=0$, $v=w=0$ and $u=u(0)$ form an equilibrium, even
though the labels are nonzero. Its two relevant input contractions are

\[
\frac12\sum_a(-y_a)h_a(0)=\frac\alpha8,
\qquad
\left(\frac12\sum_a(-y_a)\right)
\left(\frac12\sum_a h_a(0)\right)=-\frac\alpha4.
\tag{7}
\]

Thus the linearization of (6) in $(v,w)$ is

\[
\dot v=\frac\alpha2 w,\qquad
\dot w=-\frac\alpha4 v.
\tag{8}
\]

The opposite signs are essential: the exact input correlation in the readout
equation and the product of input means in the hidden equation disagree.

Here is the required uniform remainder control. Fix $T=t_*$ and fix
$\alpha>0$. On a small neighborhood of the equilibrium, Taylor expansion
of the smooth right-hand side of (6), using the bounded derivatives of tanh,
gives for $z=(v,w)^\top$

\[
|\dot u|\le C|z|^2,\qquad
\dot z=A z+R,\qquad
A=\begin{pmatrix}0&\alpha/2\\-\alpha/4&0\end{pmatrix},\qquad
|R|\le C\bigl(|z|\,|u-u(0)|+|z|^3\bigr).
\tag{9}
\]

Constants here and below can depend on $\alpha,T,u(0)$, not on
$\varepsilon$. To justify (9), note that
$r_a=-y_a+O(|vw|)$,
$\tanh(vh_a)=vh_a+O(|v|^3)$,
$\tanh'(vh_a)=1+O(v^2)$, and
$h_a=h_a(0)+O(|u-u(0)|)$. There are no quadratic terms in the $z$
equation at fixed $u$.

Let $K=\sup_{0\le t\le T}\|e^{At}\|<\infty$. Stop the local solution
before $|z|=2K\varepsilon$ or $|u-u(0)|=1$. Integrating the first
inequality gives $|u-u(0)|\le C_T\varepsilon^2$. Variation of constants
then gives $|z-\varepsilon e^{At}(1,0)^\top|\le C_T\varepsilon^3$.
For sufficiently small positive $\varepsilon$, both bounds are strictly
inside the stopping thresholds. The solution therefore continues through
$T$ within this neighborhood. This uses the elementary local ODE theorem:
a locally Lipschitz vector field has a unique local solution, and a solution
remaining in a compact subset of its domain extends through a finite endpoint.
The vector field (6) is smooth on all of its finite-dimensional domain.

Putting $\omega=\alpha/(2\sqrt2)$, we have uniformly for $0\le t\le T$

\[
u(t)=u(0)+O(\varepsilon^2),\quad
v(t)=\varepsilon\cos(\omega t)+O(\varepsilon^3),\quad
w(t)=-\frac\varepsilon{\sqrt2}\sin(\omega t)
+O(\varepsilon^3).
\tag{10}
\]

The true hidden gradient and the readout velocity satisfy

\[
\partial_v\mathcal L=\frac\alpha4 w+O(\varepsilon^3),
\qquad \dot w=-\frac\alpha4 v+O(\varepsilon^3).
\]

The first-layer loss contribution is $-\|\dot u\|^2=O(\varepsilon^4)$
with nonpositive sign, and the readout contribution is $-\dot w^2$.
Combining these with (8)--(10) gives the total, physical-time loss derivative

\[
\begin{aligned}
\dot{\mathcal L}(t)
&=\frac{\alpha^2}{8}w(t)^2
-\frac{\alpha^2}{16}v(t)^2+O(\varepsilon^4)\\
&=-\frac{\alpha^2\varepsilon^2}{16}\cos(2\omega t)
+O(\varepsilon^4).
\end{aligned}
\tag{11}
\]

Since $\omega t_*=\pi/2$,

\[
\dot{\mathcal L}(t_*)=
\frac{\alpha^2\varepsilon^2}{16}+O(\varepsilon^4)>0
\]

for sufficiently small $\varepsilon>0$. In particular, the increase is
not hidden ascent masked by a larger outer-layer decrease.

For arbitrary width $n$, initialize every row of $W^{(1)}$ at $u(0)$,

\[
W^{(2)}(0)=\frac\varepsilon n\mathbf1\mathbf1^\top,
\qquad w(0)=0.
\]

The subspace with all first rows equal, hidden matrix
$v\mathbf1\mathbf1^\top/n$, and stored readout $w\mathbf1$ is invariant.
Indeed every hidden preactivation equals $v h_a$, the normalized output is
$w\tanh(vh_a)$, and the canonical mobilities reduce the full equations
exactly to (6). Thus (11) holds at every fixed width. Smooth dependence on
initial conditions through the compact interval, together with the strict
inequality at $t_*$, gives an open neighborhood of first and hidden weights
with the same inequality, holding the zero readout fixed. The canonical
Gaussian laws have strictly positive density everywhere in these finite
weight spaces, so this open neighborhood has positive probability. This
proves the theorem.

For comparison, the canonical dense hidden equation in the same small-
amplitude calculation is $\dot v=-\alpha w/4+O(\varepsilon^3)$, while
the readout equation remains $\dot w=-\alpha v/4+O(\varepsilon^3)$.
The filtered oscillator is therefore a change in the training mechanism.

**Limits of the theorem.** It proves neither a periodic orbit nor failure to
fit at arbitrarily long times. The expansion fixes $\alpha>0$, then sends
$\varepsilon\to0$, on the fixed horizon $t_*(\alpha)$. The symmetric
reference initialization is atypical at large width, and its initial
readout-feature Gram is rank deficient. No probability-uniform or population
claim follows. The original sample-indexed paper algorithm is unchanged and
is not contradicted. No finite-$q$ trajectory claim follows merely by calling (1) an untruncated
history relation. Section 3 proves the corresponding finite-order result
directly from the raw moment equations.

**Binary-label corollary, suggested by the supervisor.** The same failure
occurs with labels of equal magnitude. Take $d=m=3$, inputs
$x_a=\sqrt3 e_a$, labels $\alpha(-1,1,1)$, and initial first activations
$(3/4,1/4,1/4)$. Keep the constant dictionary and initialization
$v(0)=\varepsilon$, $w(0)=0$. The first row is given by the componentwise
inverse tanh of these activations. For a uniform three-point expectation,

\[
\mathbb E[y]=\frac\alpha3,\qquad
\mathbb E[h(0)]=\frac5{12},\qquad
\mathbb E[yh(0)]=-\frac\alpha{12}.
\]

Expanding the exact canonical outer and projected hidden equations gives

\[
\dot v=\frac{5\alpha}{18}w+O(\varepsilon^3),\qquad
\dot w=-\frac\alpha6v+O(\varepsilon^3),\qquad
u-u(0)=O(\varepsilon^2).
\]

The identical stopped-neighborhood argument (9) gives uniform remainders on
every fixed horizon. With $\omega=\alpha\sqrt{5/108}$ it yields

\[
v(t)=\varepsilon\cos(\omega t)+O(\varepsilon^3),\qquad
w(t)=-\sqrt{\frac35}\,\varepsilon\sin(\omega t)
+O(\varepsilon^3).
\]

Here $\mathcal L=\alpha^2+\alpha vw/6+O(\varepsilon^4)$ and
$\partial_v\mathcal L=\alpha w/6+O(\varepsilon^3)$. At the quarter period
$t_*=3\pi\sqrt{3/5}/\alpha$, the readout dissipation is $O(\varepsilon^6)$,
the first-layer dissipation is $O(\varepsilon^4)$, and

\[
\dot{\mathcal L}(t_*)=
\frac{5\alpha^2}{108}w(t_*)^2+O(\varepsilon^4)
=\frac{\alpha^2\varepsilon^2}{36}+O(\varepsilon^4)>0.
\]

Width replication and the open Gaussian-support event work exactly as above.
In particular $\alpha=1$ gives ordinary labels in $\{-1,+1\}$. This remains
a finite-time, potentially rare-initialization result, with the same limits
of interpretation as the theorem.

## 3. A finite-order certificate and a safeguard with unchanged state dimension

Here $q<\infty$, and the state is exactly the input-field moments in the
assigned derivation. For one hidden link it consists of the $n$-vectors
$\bar h_{c,j},\bar\delta_{c,j}$ for $1\le c\le C$, $0\le j<q$, together
with the outer weights and a common clock $\tau$. Define

\[
H_c=\mathbb E[h\psi_c],\qquad R_c=\mathbb E[r\delta\psi_c],\qquad
h_c^*=\frac1\tau\sum_{j<q}(2j+1)\bar h_{c,j},\qquad
b_c^*=\frac1\tau\sum_{j<q}(2j+1)\bar\delta_{c,j}.
\]

The reconstruction and moment equations are

\[
\begin{aligned}
W&=W_0-\frac2{n\tau}\sum_{c=1}^C\sum_{j<q}
(2j+1)\bar\delta_{c,j}\bar h_{c,j}^\top,\qquad \dot\tau=\rho,\\
\dot{\bar h}_{c,j}
&=\rho H_c-\frac\rho\tau\left[
j\bar h_{c,j}+\sum_{k<j}(2k+1)\bar h_{c,k}\right],\\
\dot{\bar\delta}_{c,j}
&=R_c-\frac\rho\tau\left[
j\bar\delta_{c,j}+\sum_{k<j}(2k+1)\bar\delta_{c,k}\right].
\end{aligned}
\]

Initialize $\tau=1$, $\bar h_{c,0}=H_c(0)$, all higher forward moments
zero, and all backward moments zero. The initialized matrices $W_0$ remain
fixed. Every current response is recomputed through the reconstructed network.

### The ascent persists at every fixed finite order

**Finite-order theorem.** Fix $\alpha>0$, an integer $q\ge1$, and a finite
width $n\ge1$. Use the binary construction of Section 2 and the exact
finite-order initialization and equations just specified, including the unit
prefix and residual-RMS clock. For sufficiently small $\varepsilon>0$,
depending on $q,\alpha$, the solution exists through
$t_*=3\pi\sqrt{3/5}/\alpha$ and

\[
\dot{\mathcal L}(t_*)=\frac{\alpha^2\varepsilon^2}{36}
+O_{q,\alpha}(\varepsilon^4)>0.
\tag{21}
\]

At each fixed $q,n,\alpha$, an open neighborhood of first and initialized
hidden matrices also has strict ascent, with zero initial readout. The event
therefore has positive probability under the canonical finite-width Gaussian
initialization. No lower bound on that probability, no common choice of
$\varepsilon$ for all $q$, and no width or memory-order limit is asserted.

**Proof.** First take $n=1$. In the three-sample construction, let
$H_0=(3/4+1/4+1/4)/3=5/12$. View the initialized hidden scalar
$W_0=\varepsilon$ as a parameter of the finite moment vector field. At
$\varepsilon=0$, the exact solution is the nonstationary prefix background

\[
\begin{aligned}
u(t)&=u(0),& w(t)&=0,&v(t)&=0,&
\tau_0(t)&=1+\alpha t,\\
\bar h_0(t)&=\tau_0(t)H_0,&
\bar h_j(t)&=0\quad(j\ge1),&
\bar\delta_j(t)&=0\quad(j\ge0).
\end{aligned}
\tag{22}
\]

Indeed $\rho=\alpha$ because every label has magnitude $\alpha$; the
zeroth forward equation is $\dot{\bar h}_0=\alpha H_0$. For $j\ge1$ the
incoming source $\alpha H_0$ cancels the $k=0$ dilation term
$\alpha\bar h_0/\tau_0=\alpha H_0$. All backward sources and both outer
velocities vanish. Thus the higher forward modes are zero throughout the
entire background, not just initially.

Fix the compact horizon $[0,t_*]$ and fixed $q$. The background (22) lies
in a compact set with $\tau\ge1$ and $\rho=\alpha>0$. In a neighborhood with
$\tau>1/2$ and $\rho>\alpha/2$, the finite vector field is smooth in its
state and in $\varepsilon$: reconstruction divides only by $\tau$, tanh is
smooth, and the square root defining $\rho$ stays away from zero. The local
ODE theorem with smooth parameter dependence therefore gives a common
solution interval covering $[0,t_*]$ for sufficiently small
$|\varepsilon|$, and Taylor expansions in $\varepsilon$ uniform in the
$C^1([0,t_*])$ norm. Explicitly, smooth dependence follows by differentiating
the integral equation with respect to the parameter on the compact tube;
the parameter derivatives solve linear inhomogeneous variational equations
with bounded coefficients. Repeating through order four and applying the
integral inequality $g(t)\le A+B\int_0^t g(s)ds\Rightarrow
g(t)\le Ae^{Bt}$ bounds their remainders. Continuous dependence first
keeps the solution inside the chosen tube, which justifies continuation and
these differentiations.

There is also an exact parity. Replacing
$(\varepsilon,w,\bar\delta)$ by
$(-\varepsilon,-w,-\bar\delta)$ and leaving
$(u,\bar h,\tau)$ fixed changes reconstructed $v$ to $-v$.
The second-layer activation is odd in $v$, predictions $w\tanh(vh)$ and
residuals are even, backward responses and backward sources are odd, and the
first-layer velocity contains the even product $vw$. Both the equations and
initial conditions obey this transformation. Uniqueness therefore makes
$(u,\bar h,\tau)$ even functions of $\varepsilon$ and
$(w,\bar\delta,v)$ odd. Consequently, uniformly in the stated $C^1$ norm,

\[
\begin{aligned}
u-u(0)&=O_{q,\alpha}(\varepsilon^2),&
\tau-\tau_0&=O_{q,\alpha}(\varepsilon^2),\\
\bar h_0-\tau H_0&=O_{q,\alpha}(\varepsilon^2),&
\bar h_j&=O_{q,\alpha}(\varepsilon^2)\quad(j\ge1),\\
\bar\delta_j&=O_{q,\alpha}(\varepsilon),&
w&=O_{q,\alpha}(\varepsilon).
\end{aligned}
\tag{23}
\]

Only the zeroth backward moment can enter the reconstruction at first order:

\[
v=\varepsilon-\frac2\tau
\sum_{j<q}(2j+1)\bar\delta_j\bar h_j
=\varepsilon-2H_0\bar\delta_0+
O_{q,\alpha}(\varepsilon^3).
\tag{24}
\]

The same estimate holds after a physical-time derivative. The zeroth
backward equation has no dilation term. Since
$r_a=-y_a+O(\varepsilon^2)$ and
$\delta_a=w+O(\varepsilon^3)$, it gives
$\dot{\bar\delta}_0=-\alpha w/3+O_{q,\alpha}(\varepsilon^3)$.
The canonical readout equation gives
$\dot w=2v\mathbb E[yh(0)]+O_{q,\alpha}(\varepsilon^3)
=-\alpha v/6+O_{q,\alpha}(\varepsilon^3)$. Differentiating (24) therefore
yields

\[
\dot v=\frac{5\alpha}{18}w+O_{q,\alpha}(\varepsilon^3),
\qquad
\dot w=-\frac\alpha6v+O_{q,\alpha}(\varepsilon^3).
\tag{25}
\]

With $v(0)=\varepsilon,w(0)=0$, variation of constants in this
two-dimensional system gives exactly the leading oscillator and uniform
$O_{q,\alpha}(\varepsilon^3)$ remainders from the binary corollary.
At $t_*$, $v=O(\varepsilon^3)$ and
$w=-\sqrt{3/5}\varepsilon+O(\varepsilon^3)$.
The true hidden loss gradient is
$\partial_v\mathcal L=\alpha w/6+O(\varepsilon^3)$.
The outer contribution remains $-\|\dot u\|^2-\dot w^2$, irrespective
of the hidden moment mechanism. Substitution proves (21).

For arbitrary fixed width, replicate first rows and readout coordinates,
and take $W_0=\varepsilon\mathbf1\mathbf1^\top/n$. All coordinates of
each forward and backward moment remain identical. Reconstruction then has
the form $W=v\mathbf1\mathbf1^\top/n$, and the normalized network and
canonical outer equations reduce exactly to the scalar system above.
Finally, smooth dependence on first and initialized hidden weights and
strict positivity at $t_*$ give the asserted open Gaussian-support event.
This completes the proof.

The supervisor proposed this finite-order upgrade after revision 1; the
background, parity, remainder bounds, and constants were verified here.
This establishes failure of universal monotonicity separately for every
fixed order, rather than transferring a conclusion through an unproved
temporal limit. Increasing temporal order alone cannot guarantee descent
for the fixed constant input dictionary. It does not claim an order-uniform
ascent example at one fixed $\varepsilon$.

### Exact velocity and loss certificate

The starred quantities are current endpoint evaluations of the projected
histories, not current forward or backward responses. All are $n$-vectors.
The reconstructed hidden-matrix velocity is exactly

\[
V:=\dot W=-\frac2n\sum_{c=1}^C
\left[R_c h_c^{*\top}
+\rho b_c^*(H_c-h_c^*)^\top\right].
\tag{12}
\]

In particular, its rank is at most $2C$, independently of $q$, even
though the reconstructed accumulated correction has rank at most $Cq$.

For completeness, differentiate
$\tau^{-1}\sum_j(2j+1)\bar\delta_j\bar h_j^\top$ for one $c$.
Source terms give $R_c h_c^{*\top}+\rho b_c^*H_c^\top$. If
$a_j=2j+1$, differentiating $1/\tau$, the two diagonal mode terms,
and the two triangular sums gives

\[
-\frac\rho{\tau^2}\left[
\sum_j a_j^2\bar\delta_j\bar h_j^\top+
\sum_{k<j}a_ja_k
(\bar\delta_k\bar h_j^\top+
\bar\delta_j\bar h_k^\top)\right]
=-\rho b_c^*h_c^{*\top}.
\]

The diagonal coefficient is $a_j(1+2j)=a_j^2$; the remaining terms cover
every off-diagonal ordered pair once. This proves (12), including all clock
terms. It contains no division by $\rho$, so remains valid at zero residual.

For $m$ equally weighted samples, define the scalar contribution of each
hidden link and the canonical outer dissipation by

\[
S_\ell=\frac2{nm}\sum_a
r_a\delta_a^{(\ell)\top}V_\ell h_a^{(\ell-1)},\qquad
S=\sum_{\ell=2}^L S_\ell,\qquad
D_{\rm out}=\frac{\|\dot W^{(1)}\|_F^2+\|\dot w\|_2^2}{n}.
\]

The chain rule gives the exact certificate

\[
\dot{\mathcal L}=-D_{\rm out}+S.
\tag{13}
\]

Use (12) to apply $V_\ell$ to the current features. This evaluates (13)
without forming $V_\ell$ or a dense hidden gradient: after ordinary network
responses are available, the added contractions cost $O(LmnC)$, together
with $O(LnCq)$ to combine stored modes. A directional forward pass gives
the equivalent certificate $2m^{-1}\sum_a r_a\dot f_a$. The initialized
dense matrices and ordinary forward/backward cost remain; this is a gradient-
storage saving, not a claim to eliminate dense fixed storage or runtime.

The certificate also produces an exact continuous-time safeguard without
adding moving coordinates. Compute the **ungated** moments/clock velocity
and $S$ from the current state. Fix $\kappa>0$, with the same units as a
loss derivative, and set

\[
\gamma(S)=\min\{1,\max\{0,-S/\kappa\}\}.
\tag{14}
\]

Multiply **all** forward-moment, backward-moment, and common-clock
derivatives by this same $\gamma$; leave both outer weight equations
canonical. Since every hidden reconstruction depends only on its moments
and the common clock, its derivative becomes exactly $\gamma V_\ell$.
Consequently

\[
\dot{\mathcal L}=-D_{\rm out}+\gamma(S)S\le-D_{\rm out}\le0.
\tag{15}
\]

It is necessary to gate the clock and all dilation terms too: gating only
the incoming backward sources does not scale the physical hidden velocity.
The gate is locally Lipschitz in the finite moment state on $\tau\ge1$,
including at $\rho=0$, and $\dot\tau=\gamma\rho\ge0$. Thus the modified
finite-dimensional vector field is locally well posed. The guarantee holds
through its existence interval. It does not prove global existence, fitting,
or tracking of dense training. An explicit Euler step needs its own step
control; a nonpositive continuous derivative alone does not certify a finite
step. The construction is a new optimizer, with more conservative hidden
motion near $S=0$, not a repaired proof for the original algorithm.

## 4. A quantitative matrix warning from the current input geometry

This section develops the criterion disclosed by the supervisor. On $m$
uniform atoms let $H\in\mathbb R^{n\times m}$ have columns $h_a$,
$B\in\mathbb R^{n\times m}$ have columns $r_a\delta_a$, and let
$P\in\mathbb R^{m\times m}$ be the Euclidean orthogonal projection induced
by the input dictionary. Write $A=H^\top H\succeq0$. Then

\[
\langle BH^\top,BPH^\top\rangle_F
=\operatorname{tr}(BAPB^\top)
=\operatorname{tr}\left(B\frac{AP+PA}{2}B^\top\right).
\tag{16}
\]

Hence this quantity is nonnegative for every backward matrix $B$ if and
only if $AP=PA$. To prove the nontrivial direction, decompose input space
as $\operatorname{ran}P\oplus\ker P$. In these coordinates,

\[
A=\begin{pmatrix}A_{11}&A_{12}\\A_{12}^\top&A_{22}\end{pmatrix},
\qquad
\frac{AP+PA}{2}=
\begin{pmatrix}A_{11}&A_{12}/2\\A_{12}^\top/2&0\end{pmatrix}.
\]

If $u^\top A_{12}v\ne0$, the quadratic form at $(u,tv)$ is
$u^\top A_{11}u+t u^\top A_{12}v$, which is negative for one sufficiently
large signed $t$. Thus positivity forces $A_{12}=0$, equivalently
$AP=PA$. Conversely $A_{12}=0$ leaves the positive semidefinite block
$A_{11}$. A negative direction can be placed in one row of $B$, so this
argument covers any number of backward coordinates.

The size of the obstruction is also controlled explicitly. Set

\[
a=\|PAP\|_{\rm op},\qquad
b=\|PA(I-P)\|_{\rm op}=\|AP-PA\|_{\rm op}.
\]

If $b>0$, unit singular vectors for $A_{12}$ give a two-dimensional
restriction with matrix
$\left(\begin{smallmatrix}a_u&b/2\\b/2&0\end{smallmatrix}\right)$,
where $0\le a_u\le a$. Its smaller eigenvalue is
$(a_u-\sqrt{a_u^2+b^2})/2$, increasing as a function of $a_u$.
The minimum quadratic form on the full unit sphere is no greater than on
this two-dimensional circle. Therefore

\[
\lambda_{\min}\!\left(\frac{AP+PA}{2}\right)
\le-\frac{\sqrt{a^2+b^2}-a}{2}
=-\frac{b^2}{2(\sqrt{a^2+b^2}+a)}<0.
\tag{17}
\]

The denominator is positive because $b>0$. When $b=0$, the matrix is
positive semidefinite and no division is needed. This is a worst-backward-
direction warning, not a claim that the actual current $B=r\delta$
occupies that direction. Equation (13) is the actual-trajectory check;
Theorem (4) supplies an explicit dynamically realized failure. Computing
the full $m\times m$ warning matrix is optional and not needed for (13).

## 5. What a temporal pairing intervention can identify

The same issue appears when interpreting direction-two history surgery.
Fix one trained network and one hidden link. Represent the centered recorded
forward and backward histories in an orthonormal temporal basis. Stack modes
and samples, absorbing square-root integration and sample weights, to obtain
$\mathsf H,\mathsf B\in\mathbb R^{n\times k}$. Their centered interaction
is $\mathsf B\mathsf H^\top$. Means contribute a separate matrix held fixed.
An orthogonal matrix $O\in\mathbb R^{k\times k}$ produces the surgery

\[
E_O=-\frac2n\mathsf B(O-I)\mathsf H^\top.
\tag{18}
\]

It preserves both centered Gram matrices because
$(\mathsf BO)(\mathsf BO)^\top=\mathsf B\mathsf B^\top$, and leaves the
forward history unchanged. A simultaneous common orthogonal rotation of
both histories preserves the cross product exactly. If the protocol only
permits independent rotations within each sample, $O$ is block diagonal;
the argument below applies to each block and sums its bounds. Allowing all
of $O(k)$ may additionally mix samples and is a larger intervention class.

For any differentiable endpoint loss, let
$G=\nabla_{W^{(\ell)}}\mathcal L$ and define the small
$k\times k$ contraction $K=\mathsf H^\top G^\top\mathsf B$. The exact
first variation under fractional surgery is

\[
\left.\frac{d}{d\eta}\mathcal L(W^{(\ell)}+\eta E_O)
\right|_{\eta=0}
=-\frac2n\{\operatorname{tr}(KO)-\operatorname{tr}K\}.
\tag{19}
\]

If $K=U\Sigma V^\top$ is a singular-value decomposition, then
$\operatorname{tr}(KO)=\operatorname{tr}(\Sigma V^\top O U)$.
Every diagonal entry of an orthogonal matrix lies in $[-1,1]$. Therefore

\[
-\|K\|_*\le\operatorname{tr}(KO)\le\|K\|_*.
\]

Both endpoints are attained, respectively by $O=-VU^\top$ and
$O=VU^\top$. Thus the maximum and minimum possible first-order loss
changes under these matched marginal moments depend only on the current
gradient contraction $K$. They do not require a claim about which altered
histories are realizable by gradient training. If $K=0$, every such
intervention has zero first-order effect, although finite surgery can matter.

This gives a concrete ordinary explanation that singular-value-matched
random matrix perturbations do not remove: they need not match alignment
with the endpoint loss gradient. At an exactly fitted training endpoint,
that gradient vanishes. For twice differentiable predictions and a fixed
matrix perturbation $E$, direct expansion of the squared loss gives

\[
\begin{aligned}
\mathcal L(W+\eta E)
={}&\mathcal L(W)+2\eta\,\mathbb E[r\,Df[E]]\\
&+\eta^2\mathbb E\bigl[(Df[E])^2+rD^2f[E,E]\bigr]
+o(\eta^2).
\end{aligned}
\tag{20}
\]

At exact training fit, the leading change is
$\eta^2\mathbb E[(Df[E])^2]$. Singular values of $E$ do not determine
its alignment with this current prediction Jacobian either. Evaluation loss
need not be at a fitted endpoint and retains the first-order term.

**Practical discriminator.** For every surgery and its random control,
compute the same-state quantities $2\mathbb E[rDf[E]]$ and
$\mathbb E[(Df[E])^2+rD^2f[E,E]]$, with training and evaluation objectives
kept distinct. A small-amplitude intervention whose effect is predicted by
these quantities establishes endpoint sensitivity to the chosen cross
pairing. Evidence for an additional history-specific mechanism requires
going beyond an explanation matched for these local sensitivities. The
rotation calculation itself supplies no causal retraining, leave-one-out,
or reachable-history interpretation. This is an experimental design
recommendation only; no intervention was run here.

## Claim ledger and remaining decision

| Claim | Status and scope | What it does not establish |
|---|---|---|
| Exact input projection changes the hidden vector field as in (2) | Proved finite-dimensional identity | Self-consistent finite-$q$ convergence |
| Projected training can increase total loss from zero readout | Proved for every fixed finite q, (21)--(25), as well as untruncated flow | Uniform-in-q epsilon threshold, typical-width probability, periodicity, eventual nonfitting |
| Finite-$q$ instantaneous hidden velocity has rank at most $2C$ | Proved, including clock terms | Small rank of accumulated dense learning |
| Certificate (13) and common gate (14) give (15) | Proved for the stated modified dynamics | Dense tracking, fitting, or finite-step descent |
| Gram commutation characterizes every-backward-matrix descent | Proved with quantitative bound (17); supervisor-disclosed starting criterion | Realization of every backward matrix by a network |
| Marginal-preserving temporal rotations have the exact local range (19) | Proved at the fixed endpoint | Causally reachable alternate training histories |

The highest-leverage next check is the certificate (13) on an already
authorized input-field trajectory, alongside its per-layer terms and a step
refinement. It distinguishes a harmful input/temporal vector-field direction
from discrete integrator damage without requiring a dense learned-gradient
buffer. Only the separately authorized finite-order scalar ODE check was executed;
no additional trajectory or intervention campaign was launched. If a gated
algorithm is investigated later, it must be named and assessed as a new
optimizer, with its own accuracy and fitting questions.

## Provenance and checks

HEAD at start: `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`. Existing modified
and untracked paths were observed only as metadata and preserved. Only this assigned report and its owned generated namespace are written.
No Git staging, commits, or GPU work were performed. Revision 1 used no
numerical evidence; revision 2 includes the bounded CPU validation below. Checks performed by this
author: direct moment differentiation, exact width-replication reduction,
variation-of-constants remainder bound, independent chain-rule check of
the loss derivative, zero-residual boundary of (12), block-matrix quadratic
forms, and SVD extremizers. These are internal analytic checks, not a fresh
independent review.

| Input | SHA-256 |
|---|---|
| `paper/main.tex` | `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95` |
| `paper/results.tex` | `6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `MODEL_RECONCILIATION.md` | `864c0b875cd1ea25c3228fd8dba9c6f6af71c045695bb55ec3657c3a9cc75a20` |
| `INPUT_FIELD_DERIVATION.md` | `b220127e6cb6c7aaeae880824528345e088db11a79bf96dd86da7226301b8f6e` |
| `HISTORY_PROTOCOL_INITIAL.md` | `14cd38e3a460d9bd925ed69140ec1d184a2facc3f9701aa306dbff2d970c7e0b` |


## Revision 2 deterministic numerical validation

The preregistered check passed all scientific and numerical gates. The actual
finite-order moment equations, both canonical outer layers, and the
residual-RMS clock were integrated at width one with the binary labels
$(-1,1,1)$. At $t_*=7.300401616752501$, the positive loss derivative divided
by its predicted leading value $ε^2/36$ was:

| q | epsilon | Loss derivative | Ratio to epsilon squared / 36 |
|---:|---:|---:|---:|
| 1 | 0.02 | 1.1163017951e-05 | 1.004671615592 |
| 1 | 0.01 | 2.78102026308e-06 | 1.001167294710 |
| 2 | 0.02 | 1.11627209783e-05 | 1.004644888051 |
| 2 | 0.01 | 2.78100146509e-06 | 1.001160527432 |
| 4 | 0.02 | 1.11626484269e-05 | 1.004638358421 |
| 4 | 0.01 | 2.78099694424e-06 | 1.001158899927 |

The deviation of the ratio from one contracted by factors
0.2498696, 0.2498505, and 0.2498513 for q=1,2,4 respectively when epsilon
halved, consistent with the predicted $O_{q,\alpha}(\varepsilon^2)$
normalized remainder. This does not estimate a bound uniform in q.

All twelve retained solves succeeded. Maximum coarse/fine change in the
normalized derivative was $8.53\times10^{-12}$. Across all solver RHS
evaluations, the differentiated reconstruction and rank-two velocity formula
differed by at most $2.61\times10^{-18}$, and the two loss-derivative
calculations differed by at most $1.53\times10^{-20}$.
The successful check used 0.254 CPU-seconds after imports, one CPU thread,
Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0, and Linux x86_64. Exit status 0.

The first identical attempt completed twelve scalar solves but failed while
serializing a NumPy boolean, before writing its result file. The supervisor
then explicitly authorized twelve identical rerun solves after a
serialization-only conversion to Python scalar types. The failed source and
failure record are retained. Total executed validation solves: 24; no
scientific parameters, tolerances, gates, or initial conditions changed.
Both command invocations took less than one wall-clock second each. These are
small deterministic validation ODEs, not additional full training campaign
runs.

The exact successful command, from /home/amir/Codes/PDE, was:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python data/generated/response_memory_use_cases_20261001/stage2_challenge/finite_q_v2_20261002/check_finite_q.py
```

For fresh reproduction, save the complete script below as check_finite_q.py
in a new output directory and run it with those same three thread environment
variables. It writes results.json beside itself. No original generated output
is needed as an input.

All paths in the table are relative to
data/generated/response_memory_use_cases_20261001/stage2_challenge/finite_q_v2_20261002/.

| Artifact | SHA-256 |
|---|---|
| check_finite_q.py | d823acedf820c214c4c443c82db7a3be0c1064c5ab752f437a3b693395ac0845 |
| check_finite_q_serialization_failed.py | c21c71acb35d59973266cc8aee6548eff19b2254fedb0e2cb96ac56e44a86473 |
| results.json | 452816b1d1541385187909c3b95f1abf5d1d9dc228c9da6358bca451af32f77d |
| PREREGISTERED_CHECK.md | 7d36aa62af3c7efbceb784f9a2f9f866dae62b9447a1b09b462bbafdc1b4eccf |
| SERIALIZATION_FAILURE.txt | 45a9c9102cb2ab4fffda9b879645186a73f9506f9f31f26bf55ed1634ae46e7c |

### Complete validation source

```python
"""Deterministic check of the finite-q binary-label ascent coefficient."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
import numpy as np
import scipy
from scipy.integrate import solve_ivp

run = Path(__file__).resolve().parent
started = time.process_time()
labels = np.array([-1.0, 1.0, 1.0])
initial_h = np.array([0.75, 0.25, 0.25])
endpoint = 3 * np.pi * np.sqrt(3 / 5)
rows = []

for q in (1, 2, 4):
    modes = np.arange(q, dtype=float)
    weights = 2 * modes + 1
    triangular = np.diag(modes)
    for j in range(q):
        triangular[j, :j] = weights[:j]
    for epsilon in (0.02, 0.01):
        initial = np.zeros(5 + 2 * q)
        initial[:3] = np.arctanh(initial_h)
        initial[4] = 1
        initial[5] = initial_h.mean()
        for rtol, atol in ((1e-10, 1e-12), (1e-12, 1e-14)):
            errors = {"velocity": 0.0, "loss": 0.0}

            def quantities(state):
                u, w, tau = state[:3], state[3], state[4]
                forward = state[5:5+q]
                backward = state[5+q:]
                pairing = np.dot(weights * forward, backward)
                v = epsilon - 2 * pairing / tau
                h = np.tanh(u)
                h2 = np.tanh(v * h)
                gate = 1 - h2**2
                residual = w * h2 - labels
                rho = np.sqrt(np.mean(residual**2))
                hmean = h.mean()
                source = np.mean(residual * w * gate)
                du = -(2/3) * residual * v * w * gate * (1-h**2)
                dw = -2 * np.mean(residual * h2)
                dforward = rho * hmean - rho/tau * (triangular @ forward)
                dbackward = source - rho/tau * (triangular @ backward)
                vdot = (-2/tau * np.dot(
                    weights, dforward*backward + forward*dbackward
                ) + 2*rho/tau**2 * pairing)
                hstar = np.dot(weights, forward)/tau
                bstar = np.dot(weights, backward)/tau
                vdot_lowrank = -2 * (
                    source*hstar + rho*bstar*(hmean-hstar)
                )
                fvelocity = dw*h2 + w*gate*(
                    vdot*h + v*(1-h**2)*du
                )
                lossdot = 2*np.mean(residual*fvelocity)
                gradient_v = 2*np.mean(residual*w*gate*h)
                lossdot_blocks = -np.dot(du,du)-dw**2+gradient_v*vdot
                errors["velocity"] = max(
                    errors["velocity"], abs(vdot-vdot_lowrank)
                )
                errors["loss"] = max(
                    errors["loss"], abs(lossdot-lossdot_blocks)
                )
                velocity = np.concatenate((
                    du, [dw, rho], dforward, dbackward
                ))
                return velocity, lossdot, v, w, tau

            def rhs(t, state):
                return quantities(state)[0]

            solution = solve_ivp(
                rhs, (0, endpoint), initial, method="DOP853",
                rtol=rtol, atol=atol,
            )
            _, lossdot, v, w, tau = quantities(solution.y[:, -1])
            rows.append({
                "q": q, "epsilon": epsilon, "rtol": rtol, "atol": atol,
                "success": bool(solution.success), "message": solution.message,
                "nfev": int(solution.nfev), "loss_derivative": float(lossdot),
                "normalized": float(lossdot/(epsilon**2/36)),
                "v": float(v), "w": float(w), "tau": float(tau),
                "max_velocity_identity_error": errors["velocity"],
                "max_loss_identity_error": errors["loss"],
            })

fine = {(r["q"],r["epsilon"]):r for r in rows if r["rtol"] == 1e-12}
coarse = {(r["q"],r["epsilon"]):r for r in rows if r["rtol"] == 1e-10}
tolerance_change = max(
    abs(fine[k]["normalized"]-coarse[k]["normalized"]) for k in fine
)
valid = (
    all(r["success"] for r in rows)
    and tolerance_change < 1e-7
    and max(r["max_velocity_identity_error"] for r in rows) < 1e-10
    and max(r["max_loss_identity_error"] for r in rows) < 1e-10
)
contraction = {
    str(q): abs(fine[q,.01]["normalized"]-1)
        / max(abs(fine[q,.02]["normalized"]-1), np.finfo(float).tiny)
    for q in (1,2,4)
}
passed = valid and all(
    r["loss_derivative"] > 0 and abs(r["normalized"]-1) < .01
    for r in rows
) and all(
    abs(fine[q,.01]["normalized"]-1)
    <= .35*abs(fine[q,.02]["normalized"]-1)+1e-7
    for q in (1,2,4)
)
report = {
    "python": sys.version, "numpy": np.__version__,
    "scipy": scipy.__version__, "platform": platform.platform(),
    "cpu_threads": {
        k: os.environ.get(k) for k in (
            "OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"
        )
    },
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "endpoint": float(endpoint), "rows": rows, "valid": bool(valid),
    "pass": bool(passed), "max_normalized_tolerance_change": float(tolerance_change),
    "deviation_contraction": contraction,
    "cpu_seconds": time.process_time()-started,
}
(run/"results.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
if not passed:
    raise SystemExit(1)
```
