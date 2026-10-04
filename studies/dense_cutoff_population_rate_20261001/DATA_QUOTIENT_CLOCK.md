# Exact data quotient and the persistent residual clock

2026-10-03. Scoped internal mathematical audit. This note uses the current
manuscript's setting, learning-speed closure, results, initialization argument,
all-order fitting proof, and finite-time bounded-activation continuation proof,
together with this study's `SAME_WIDTH_COMPARISON_CHECK.md` and
`NONORTHOGONAL_DIRECT_ROUTE.md`. It does not use another study, experiments,
Git operations, or manuscript edits. The canonical-notation and rigorous-math
skills, including the neural-response reference, were applied.

The conclusions are exact quotient identities, automatic positivity of the
quotient initialization Gram, and a fixed-order small-label convergence result
for the original clock even with inconsistent labels. The last result has an
order-dependent smallness threshold. The endpoint identity below exposes a
possible all-time obstruction, but this note does not prove a prediction-error
counterexample or a uniform-in-order smallness threshold.

## 1. Setup and exact quotient

Consider the manuscript's bias-free network with tanh at every hidden layer,
zero initial readout, normalized nonzero training inputs
\(v_a=x_a/\sqrt d\) satisfying \(\|v_a\|_2=1\), and loss
\(\mathcal L=m^{-1}\sum_a(f_a-y_a)^2\). Its weights are
\(W^{(1)},\ldots,W^{(L)},w\), and
\[
z_a^{(1)}=W^{(1)}v_a,\quad h_a^{(1)}=\tanh z_a^{(1)},\quad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\tanh z_a^{(\ell)},\quad
f_a=n^{-1}w^\top h_a^{(L)}.
\]
Write \(g=\tanh'=\operatorname{sech}^2\). The backward responses exclude
the residual:
\[
\delta_a^{(L)}=w\odot g(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=g(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Partition the data into classes \(I_1,\ldots,I_J\) under equality up to
sign. Choose one unit representative \(u_j\) per class and write
\(v_a=s_a u_j\), with \(s_a\in\{-1,1\}\), for \(a\in I_j\).
Define
\[
N_j=|I_j|,\qquad p_j=N_j/m,\qquad
\bar y_j=N_j^{-1}\sum_{a\in I_j}s_a y_a,\qquad
\eta_a=y_a-s_a\bar y_j,
\]
and the irreducible residual RMS
\[
\sigma^2=m^{-1}\sum_a\eta_a^2.
\]
Then \(\sum_{a\in I_j}s_a\eta_a=0\).

For every parameter state, oddness of tanh and evenness of \(g\) imply
\[
h_a^{(\ell)}=s_a h_j^{(\ell)},\quad
z_a^{(\ell)}=s_a z_j^{(\ell)},\quad
f_a=s_a f_j,\quad \delta_a^{(\ell)}=\delta_j^{(\ell)},
\]
where subscript \(j\) denotes evaluation at \(u_j\). With
\(e_j=f_j-\bar y_j\) and \(u=(\sum_jp_j e_j^2)^{1/2}\), the residuals
and loss decompose exactly as
\[
r_a=s_a e_j-\eta_a,\qquad \rho^2=u^2+\sigma^2.
\tag{1}
\]
Every dense parameter update depends only on the effective residuals:
\[
\begin{aligned}
\dot W^{(1)}&=-2\sum_jp_j e_j\delta_j^{(1)}u_j^\top,\\
\dot W^{(\ell)}&=-\frac2n\sum_jp_j e_j\delta_j^{(\ell)}
h_j^{(\ell-1)\top},\qquad \ell\ge2,\\
\dot w&=-2\sum_jp_j e_jh_j^{(L)}.
\end{aligned}
\tag{2}
\]
Indeed each relevant original summand has one odd factor, so its class sum
contains \(\sum_{a\in I_j}s_ar_a=N_je_j\).

The autonomous closure has the same exact quotient. Its forward moments
satisfy \(\bar h_{a,k}^{(\ell-1)}=s_a\bar h_{j,k}^{(\ell-1)}\).
Define its effective backward moments by
\[
\bar\delta_{j,k}^{(\ell)}
 =N_j^{-1}\sum_{a\in I_j}s_a\bar\delta_{a,k}^{(\ell)}.
\]
Taking this signed sum in the original moment ODE gives
\[
\begin{aligned}
\dot{\bar h}_{j,k}^{(\ell-1)}
 &=\rho h_j^{(\ell-1)}-\frac\rho\tau
 \left[k\bar h_{j,k}^{(\ell-1)}+
 \sum_{i<k}(2i+1)\bar h_{j,i}^{(\ell-1)}\right],\\
\dot{\bar\delta}_{j,k}^{(\ell)}
 &=e_j\delta_j^{(\ell)}-\frac\rho\tau
 \left[k\bar\delta_{j,k}^{(\ell)}+
 \sum_{i<k}(2i+1)\bar\delta_{j,i}^{(\ell)}\right],\\
\widehat W^{(\ell)}
 &=W_0^{(\ell)}-\frac2{n\tau}\sum_jp_j
 \sum_{k<q}(2k+1)\bar\delta_{j,k}^{(\ell)}
 \bar h_{j,k}^{(\ell-1)\top},\\
\dot\tau&=\sqrt{\sum_jp_je_j^2+\sigma^2},\qquad \tau(0)=1.
\end{aligned}
\tag{3}
\]
The first layer and readout use (2), evaluated in the reconstructed network.
The initial forward prefix is the initialized feature; its only nonzero raw
moment is mode zero. The initial backward prefix and all its moments are zero.
Consequently (3) preserves the original physical trajectory and clock exactly.
Replacing its clock by \(\dot\tau=u\) when \(\sigma>0\) defines a
different algorithm.

If \(\bar y_j=0\) for every class, then \(w=0\), all backward responses
vanish, all physical parameters remain initialized, and both dense and closure
predictions vanish identically. Their original clock is
\(\tau(t)=1+\sigma t\). Thus inconsistent labels or a divergent clock alone
do not give a tracking counterexample.

## 2. The quotient feature Gram is automatically positive

The representatives \(u_j\) are nonzero and pairwise nonproportional:
normalization means proportionality would be equality up to sign. The first
Gaussian feature covariance is
\[
Q^{(1)}_{ij}=\mathbb E[\tanh(G^\top u_i)\tanh(G^\top u_j)],
\qquad G\sim N(0,I_d).
\]
It is positive definite. Here is the complete relevant argument. If a null
quadratic form existed, Gaussian full support and continuity would imply
\(\sum_jc_j\tanh(u_j^\top x)=0\) for every \(x\). Fix \(i\) with
\(c_i\ne0\). For each \(j\ne i\), choose a vector perpendicular to
\(u_j\) but not to \(u_i\), and apply a finite difference along that
vector. The product of these \(J-1\) differences eliminates all summands
except the \(i\)-th. Varying the steps and base point gives
\[
\Delta_{t_1}\cdots\Delta_{t_{J-1}}\tanh(s)=0
\quad\text{for every }s,t_1,\ldots,t_{J-1}.
\]
Convolving with a smooth compactly supported approximate identity and
differentiating in the steps at zero shows that each mollification is a
polynomial of degree at most \(J-2\). Interpolation at \(J-1\) distinct
points and local uniform convergence imply that tanh itself is such a
polynomial. This contradicts its nonconstancy and boundedness. For \(J=1\),
the positive variance of \(\tanh(G^\top u_1)\) proves the assertion directly.

For later layers, if \(Q\succ0\), a Gaussian vector with covariance \(Q\)
has full support. An identity \(\sum_jc_j\tanh(Z_j)=0\) almost surely
therefore holds for every \(Z\); varying one coordinate proves every
\(c_j=0\). Induction proves \(Q^{(L)}\succ0\) at every fixed depth.
The weighted covariance
\(\operatorname{diag}(\sqrt p)Q^{(L)}\operatorname{diag}(\sqrt p)\)
is also positive definite. The conditional law-of-large-numbers argument in
the manuscript then gives a positive finite-width quotient Gram margin with
probability tending to one.

To identify all original degeneracies, let \(S\in\mathbb R^{m\times J}\)
have entry \(S_{aj}=s_a\) for \(a\in I_j\), and zero otherwise. The original
population feature covariance is exactly \(SQ^{(L)}S^\top\), and its
nullspace is exactly \(\ker S^\top\). Thus duplicate/antipodal symmetries are
the only feature-Gram degeneracies for this normalized tanh setup. The constants
and small-label threshold can still depend on the actual quotient geometry;
there is no geometry-uniform positive margin over arbitrarily close inputs.

When \(\sigma=0\), the weighted quotient uses its ordinary residual clock,
and the manuscript's fitting proof applies with weighted sample sums. This
removes an extra nondegeneracy assumption for each fixed normalized dataset
whose labels respect its duplicate/antipodal identities. When \(\sigma>0\),
the original RMS does not decay to zero even if the effective labels fit.

## 3. Small-label convergence at each fixed order with the original clock

This section concerns two tanh hidden layers and a fixed finite order \(q\).
Assume the initialized weighted quotient readout-feature Gram has a positive
gap and the initialized hidden matrix has bounded operator norm. For each
fixed \(q\), sufficiently small effective labels give global physical
convergence and \(\int_0^\infty u(t)dt<\infty\), even when \(\sigma>0\).
The threshold here may depend on \(q\); the proof supplies no uniform
small-label theorem as \(q\to\infty\).

We give the bootstrap because convergence cannot simply be assumed from the
existing theorem, whose clock has finite total mass. Let
\(Y_0=(\sum_jp_j\bar y_j^2)^{1/2}\), and stop the solution when
\(\int_0^t u(s)ds\) first reaches a cap \(S\), or the hidden operator
norm leaves a fixed tube. Constants \(C\) below may depend on the data and
tube, but not on width; constants \(C_q\) may also depend on order. Bounded
tanh and (2) imply on this stopped interval
\[
\|w\|_\infty\le2S,\qquad
\max_j\frac{\|\delta_j^{(2)}\|_2+\|\delta_j^{(1)}\|_2}{\sqrt n}
\le CS,\qquad
\max_j\frac{\|\dot h_j^{(1)}\|_2}{\sqrt n}\le CSu(t).
\tag{4}
\]
The \(L^\infty\)-to-\(L^\infty\) norm of degree-below-\(q\) Legendre
projection is at most \(q^2\): expand its kernel and use
\(|p_k(x)|\le1\) on \([0,1]\). Writing the reconstruction as a pairing of
the effective backward history with the projected forward history therefore
gives
\[
\|\widehat W^{(2)}-W_0^{(2)}\|_F\le C_qS^2,
\qquad
\frac{\|\widehat W^{(1)}-W_0^{(1)}\|_F}{\sqrt n}\le CS^2.
\tag{5}
\]
Forward subtraction then bounds the change of the weighted readout-feature
Gram by \(C_qS^2\). Small \(S\) preserves the tube and a fixed positive
Gram margin.

For completeness, the accumulated defect remains integrable despite the
unbounded clock. Write \(A(t)=\tau(t)\), and let stars denote projected
endpoint values. In the effective quotient,
\[
E_2(t)=\frac{2\rho(t)}n\sum_jp_j
\left(\frac{e_j(t)\delta_j^{(2)}(t)}{\rho(t)}-b_j^*(t)\right)
\left(h_j^{(1)}(t)-h_j^{(1)*}(t)\right)^\top,
\quad E_1=E_w=0.
\tag{6}
\]
The effective backward endpoint satisfies
\[
\frac{\|b_j^*(t)\|_2}{\sqrt n}
\le \frac{q^2}{A(t)}\int_0^t
 |e_j(s)|\frac{\|\delta_j^{(2)}(s)\|_2}{\sqrt n}\,ds
\le\frac{C_qS^2}{A(t)}.
\tag{7}
\]
The forward endpoint formula from the manuscript, integrated against the
physical-time derivative, is
\[
h_j^{(1)}(t)-h_j^{(1)*}(t)
=\int_0^t L_q\left(\frac{A(s)}{A(t)}\right)\dot h_j^{(1)}(s)\,ds,
\quad L_q(x)=\frac{p_q(x)+p_{q-1}(x)}2.
\tag{8}
\]
The initialized constant prefix has zero derivative. Since \(L_q(0)=0\)
and \(L_q\) is a fixed polynomial bounded by one on \([0,1]\), choose
\(B_q\ge1\) with
\(|L_q(x)|\le\min(1,B_qx)\). Equations (4) and (8) give
\[
\max_j\frac{\|h_j^{(1)}(t)-h_j^{(1)*}(t)\|_2}{\sqrt n}
\le CS\int_0^t u(s)
\min\left(1,\frac{B_qA(s)}{A(t)}\right)ds.
\tag{9}
\]
For each \(s\), changing variables \(A=A(t)\), using
\(dA=\rho(t)dt\), and extending the upper endpoint to infinity yield
\[
\int_s^\infty\frac{\rho(t)}{A(t)}
 \min\left(1,\frac{B_qA(s)}{A(t)}\right)dt
\le\int_{A(s)}^\infty\frac1A
 \min\left(1,\frac{B_qA(s)}A\right)dA
=1+\log B_q.
\tag{10}
\]
This estimate also holds with a finite terminal time and requires no lower
bound on \(\sigma\). Inserting (7)--(9) into (6), the current backward
factor contributes at most \(CS^4\) to the integrated Frobenius norm; the
projected factor contributes at most \(C_qS^4\) by Tonelli and (10).
Consequently, on every stopped interval,
\[
\int_0^t\|E_2(s)\|_Fds\le C_qS^4.
\tag{11}
\]

In the weighted residual coordinates \(\sqrt{p_j}e_j\), the dense tangent
Gram is symmetric and dominates the readout-feature Gram. The residual
equation is the dense dissipative equation plus the prediction differential
of \(E_2\). By (4), that forcing has weighted RMS at most
\(CS\|E_2\|_F\). With the positive gap written as \(\kappa>0\),
\[
u(t)+\kappa\int_0^t u(s)ds
\le Y_0+CS\int_0^t\|E_2(s)\|_Fds
\le Y_0+C_qS^5.
\tag{12}
\]
The norm inequality holds in the upper Dini-derivative sense at zeros of
\(u\), so no division by a vanishing effective residual is required.
Choose \(S=2Y_0/\kappa\), then choose \(Y_0\) small enough that (5)
preserves strict tube and Gram margins and \(C_qS^5<Y_0/2\). Equation
(12) excludes the first attainment of the activity cap. The bounded-activation
continuation argument in the manuscript gives global existence at each fixed
width and order. Equation (11), (2), and (4) give finite total variation of
all physical parameter blocks. Hence the parameters converge; their residual
norm converges and belongs to \(L^1(0,\infty)\), so \(u(t)\to0\).

For \(Y_0=0\), use the exact stationary solution from Section 1. If
\(\sigma>0\), the proof also gives \(\tau(t)\to\infty\). It proves
effective fitting, not fitting of inconsistent original labels.

## 4. Fixed-order endpoint identity when the clock does not stop

For any fixed \(q\), suppose the physical closure parameters converge,
\(\sigma>0\), and
\(\int_0^\infty |e_j(t)|\|\delta_j^{(\ell)}(t)\|_2dt<\infty\).
These hypotheses hold in the fixed-order two-layer regime just proved.
Define the effective integrated backward response
\[
D_j^{(\ell)}=\int_0^\infty e_j(t)\delta_j^{(\ell)}(t)dt.
\]
The effective backward moment has the exact integral representation
\[
\bar\delta_{j,k}^{(\ell)}(t)
=\int_0^t e_j(s)\delta_j^{(\ell)}(s)
p_k\left(\frac{\tau(s)}{\tau(t)}\right)ds.
\]
Because \(\tau(t)\to\infty\), \(|p_k|\le1\), and the integrand without
the polynomial is absolutely integrable, dominated convergence gives
\[
\bar\delta_{j,k}^{(\ell)}(t)\longrightarrow
(-1)^kD_j^{(\ell)}.
\tag{13}
\]
Writing the forward history in clock coordinates and rescaling to \([0,1]\),
\[
\frac{\bar h_{j,k}^{(\ell-1)}(t)}{\tau(t)}
=\int_0^1h_j^{(\ell-1)}(\tau(t)v)p_k(v)dv
\longrightarrow h_j^{(\ell-1)}(\infty)\mathbf1_{k=0}.
\tag{14}
\]
The history is bounded and converges as its clock coordinate tends to infinity;
dominated convergence applies at every \(v>0\). No integrability assumption
on the difference from the final forward feature is needed.

Substitution in the exact reconstruction gives
\[
\widehat W^{(\ell)}(\infty)
=W_0^{(\ell)}-\frac2n\sum_jp_jD_j^{(\ell)}
h_j^{(\ell-1)}(\infty)^\top.
\tag{15}
\]
Every fixed finite order has this final-feature pairing. The paths and the
integrals \(D_j^{(\ell)}\) can still depend on \(q\); equation (15) does
not prove that the endpoints are order independent.

For comparison, dense training retains
\[
W_D^{(\ell)}(\infty)=W_0^{(\ell)}-\frac2n\sum_jp_j
\int_0^\infty e_{D,j}(t)\delta_{D,j}^{(\ell)}(t)
h_{D,j}^{(\ell-1)}(t)^\top dt.
\tag{16}
\]
The difference between (15) and (16) is a possible mechanism for
noncommutation of the infinite-time and infinite-order limits. To turn it into
a tracking counterexample, one must control the actual closed trajectories and
show a surviving discrepancy in the requested observable, rather than merely
compare integrands or note inconsistent labels. In particular, the fixed-order
smallness thresholds in Section 3 cannot silently be made uniform in order.

Individual original backward moments need not converge: their forcing includes
the nonzero irreducible residual. Formula (13) applies to the signed class
average defined in Section 1, where those terms cancel exactly. Formula (15)
does not say that the learned matrix returns to initialization; its mode-zero
pairing generally survives.

## 5. An exact endpoint-error isometry, uniform in order

This additional identity was obtained after the coordinator suggested examining
the endpoint filter by a Mellin transform. It strengthens the analytic tools,
but does not by itself close the uniform-in-order convergence gap.

For a scalar or Hilbert-valued history \(v\in L^2(0,\infty)\), define
\[
(T_qv)(A)=(\Pi_q^Av)(A)
=\frac1A\int_0^A K_q(\xi/A)v(\xi)d\xi,
\quad K_q(x)=\sum_{k<q}(2k+1)p_k(x),
\quad R_q=I-T_q.
\]
Then, at every fixed finite order,
\[
\|R_qv\|_{L^2(0,\infty)}=\|v\|_{L^2(0,\infty)},
\qquad \|T_qv\|_{L^2(0,\infty)}\le2\|v\|_{L^2(0,\infty)}.
\tag{17}
\]
To prove it without transform theory, integrate the manuscript's growing
projection-energy identity from zero to \(A\):
\[
\int_0^A\|R_qv(\xi)\|^2d\xi
=\|v\|_{L^2(0,A)}^2-\|\Pi_q^Av\|_{L^2(0,A)}^2.
\]
For a compactly supported integrable history, every raw moment is bounded
as \(A\to\infty\), so
\(\|\Pi_q^Av\|_2^2=A^{-1}\sum_{k<q}(2k+1)
\|\int_0^Av(\xi)p_k(\xi/A)d\xi\|^2\to0\).
Approximate an arbitrary \(L^2\) history by bounded compactly supported
histories and use projection contraction to obtain the same limit. This proves
the equality in (17); the triangle inequality proves its second assertion.

The Mellin multiplier gives the same identity explicitly. For
\(s=1/2+i\omega\), with real frequency \(\omega\), direct integration of
the Legendre polynomial gives
\[
\int_0^1K_q(x)x^{s-1}dx
=1-\prod_{k=1}^q\frac{s-k}{s+k-1}.
\tag{18}
\]
One can obtain (18) by integrating the shifted Rodrigues formula against
\(x^{s-1}\), first where repeated integration by parts is valid and then
extending the resulting rational identity to \(\operatorname{Re}s>0\).
For \(\operatorname{Re}s=1/2\), each ratio in the product has modulus one.
Thus the residual filter has unit modulus on every logarithmic frequency.

Since \(R_q\) annihilates constant histories, polarization of (17) yields
\[
\int_0^\infty (R_qb)(A)(R_qh)(A)^\top dA
=\int_0^\infty b(A)(h(A)-h_\infty)^\top dA
\tag{19}
\]
whenever \(b\) and \(h-h_\infty\) are square integrable. For the actual
quotient closure, if these hypotheses hold for the histories in (6),
\[
\int_0^\infty E_2(t)dt
=\frac2n\sum_jp_j\int_0^\infty
e_j(t)\delta_j^{(2)}(t)
\bigl(h_j^{(1)}(t)-h_j^{(1)}(\infty)\bigr)^\top dt.
\tag{20}
\]
This signed identity agrees with (15) minus the dense-form accumulated update
along the closure's own path. It is independent of the projection order as an
operator identity; its actual histories still depend on order.

The square-integrability hypotheses can also be proved in the fixed-order
small-effective-label regime above, after reducing its threshold. Retain
\(\sigma>0\), as in the endpoint identity; no smallness assumption on
\(\sigma\) is needed for this fixed-order conclusion. Here are the details
needed to see the remaining order dependence. Let \(1/2<\alpha<1\), and put
\(M_\alpha(T)=\int_0^T A(t)^\alpha u(t)dt\). Equations (6)--(9), the
uniform bound \(\|h_j-h_j^*\|_2/\sqrt n\le CS^2\), and Tonelli give
\[
\int_0^T A(t)^\alpha\|E_2(t)\|_Fdt
\le C_{q,\alpha}S^3M_\alpha(T).
\]
For the term involving the projected backward response this uses
\[
\int_{A(s)}^\infty A^{\alpha-1}
\min\left(1,\frac{B_qA(s)}A\right)dA
=A(s)^\alpha\left[
\frac{B_q^\alpha-1}{\alpha}+
\frac{B_q^\alpha}{1-\alpha}\right].
\]
In the residual inequality, the factor from differentiating \(A^\alpha\)
is \(\alpha\rho/A\). Equation (12) gives
\[
\rho(t)\le\rho_*:=\sqrt{\sigma^2+(Y_0+C_qS^5)^2},
\qquad A(t)\ge1+\sigma t.
\]
Thus there is a finite \(T_0\), depending only on these fixed constants,
such that \(\alpha\rho(t)/A(t)\le\kappa/2\) for \(t\ge T_0\).
The initial contribution
\[
C_{\mathrm{pre}}
=\alpha\int_0^{T_0}A(t)^{\alpha-1}\rho(t)u(t)dt
\]
is finite. Multiplying the residual inequality by \(A^\alpha\), integrating,
and using the weighted defect estimate therefore gives
\[
\left(\frac\kappa2-C_{q,\alpha}S^4\right)M_\alpha(T)
\le Y_0+C_{\mathrm{pre}}.
\]
The additional factor \(S\) in the defect contribution comes from the
prediction differential. Reducing the fixed-order effective-label threshold
so \(C_{q,\alpha}S^4\le\kappa/4\) proves
\(\sup_T M_\alpha(T)<\infty\). Equations (4) and monotonicity of \(A\)
then imply
\[
\frac{\|h_j^{(1)}(t)-h_j^{(1)}(\infty)\|_2}{\sqrt n}
\le CS\int_t^\infty u(s)ds
\le CS M_\alpha(\infty) A(t)^{-\alpha}.
\]
This is square integrable in the clock because \(2\alpha>1\). The effective
backward history is square integrable since
\(n^{-1}\int\|b_j\|^2dA\le C S^2\int u(t)^2/\rho(t)dt
\le CS^3\). Thus (20) applies to these actual trajectories.

The isometry alone does not bound the forward error uniformly on an unbounded
clock from total variation. For example, at order one a scalar history with a
unit upward step at clock \(A_0\) has endpoint error \(A_0/A\) for
\(A>A_0\), and its squared error integral is \(A_0\). Smooth approximations
give the same scaling. Therefore a late feature change can have large
\(L^2\) endpoint error even with fixed total variation. Controlling when the
actual changes occur remains necessary for a uniform-in-order bootstrap.
