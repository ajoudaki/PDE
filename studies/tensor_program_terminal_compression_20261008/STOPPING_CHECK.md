# Scoped check of stopping, finite Euler simulation, and retained storage

This check uses only the supervisor's mathematical assignment and the required proof and notation instructions. It does not inspect the study's construction or establish its compression theorem. The stopping estimate is valid, with the threshold and zero-residual conventions below. The Euler claim is valid after making initialization, tube, mesh-rounding, and output bounds explicit.

## 1. Comparing each system at its own stopping time

Let the training inputs and labels be \((x_b,y_b)_{b=1}^m\), and let \(\mathcal P\) be a finite prediction panel containing every training input. The dense prediction is \(f(t,x)\), its training residual is \(r_b(t)=f(t,x_b)-y_b\), and its training root mean square is

\[
\rho(t)=\left(\frac1m\sum_{b=1}^m r_b(t)^2\right)^{1/2}.
\]

Assume that, while \(\rho(t)>0\),

\[
-\dot\rho(t)\ge \frac\lambda2\rho(t),\qquad
|\partial_t f(t,x)|\le B\rho(t)
\quad(x\in\mathcal P),\qquad \lambda>0.
\]

If zero residual is attained, assume the dense flow is stationary thereafter, as holds for smooth gradient flow of squared training loss. For \(s\le t\), integrating the two inequalities gives

\[
\begin{aligned}
|f(t,x)-f(s,x)|
&\le B\int_s^t\rho(u)\,du\\
&\le \frac{2B}{\lambda}\int_s^t-\dot\rho(u)\,du
=\frac{2B}{\lambda}\bigl(\rho(s)-\rho(t)\bigr).
\end{aligned}
\]

Thus for either order of the times,

\[
|f(t,x)-f(s,x)|\le\frac{2B}{\lambda}|\rho(t)-\rho(s)|.
\tag{1}
\]

This estimate controls displacement by residual decrease and has no inverse-threshold factor.

Fix a threshold \(a>0\). Define the dense stopping time by

\[
\tau_a=\inf\{t\ge0:\rho(t)\le a\}.
\]

When \(\rho(0)>a\), integrating the differential inequality gives \(\rho(t)\le\rho(0)e^{-\lambda t/2}\), so \(\tau_a\) is finite and continuity gives \(\rho(\tau_a)=a\). When \(\rho(0)\le a\), set \(\tau_a=0\); an equality time \(\rho=a\) need not exist.

Let \(\widetilde f(t,x)\) be the compressed exact prediction, and let \(f_h^j(x)\) be its numerical prediction at physical time \(t_j=jh\). Suppose, at all relevant times and grid points,

\[
\max_{x\in\mathcal P}|\widetilde f(t_j,x)-f(t_j,x)|\le e_0,
\qquad
\max_{x\in\mathcal P}|f_h^j(x)-\widetilde f(t_j,x)|\le e_1.
\]

Write \(e=e_0+e_1\), and compute

\[
\rho_h^j=\left(\frac1m\sum_{b=1}^m(f_h^j(x_b)-y_b)^2\right)^{1/2}.
\]

The reverse triangle inequality in normalized Euclidean norm gives

\[
|\rho_h^j-\rho(t_j)|
\le\left(\frac1m\sum_b|f_h^j(x_b)-f(t_j,x_b)|^2\right)^{1/2}
\le e.
\tag{2}
\]

Suppose \(k\) is the first numerical index with \(\rho_h^k\le a\). If \(k\ge1\), also suppose its last decrease satisfies

\[
\rho_h^{k-1}-\rho_h^k\le e.
\tag{3}
\]

First crossing gives \(\rho_h^{k-1}>a\), hence

\[
a-e<\rho_h^k\le a,
\qquad a-2e<\rho(t_k)\le a+e.
\tag{4}
\]

If \(\rho(0)>a\), (4) implies \(|\rho(t_k)-\rho(\tau_a)|\le2e\). If \(\rho(0)\le a\), monotonicity and (4) instead give

\[
0\le\rho(0)-\rho(t_k)\le a-\rho(t_k)<2e.
\]

In both cases, (1), the same-time prediction estimate, and the triangle inequality prove

\[
\max_{x\in\mathcal P}|f_h^k(x)-f(\tau_a,x)|
\le e+\frac{4B}{\lambda}e.
\tag{5}
\]

No monotonicity of the numerical residual is needed before the crossing.

If \(k=0\), (3) is unnecessary. When \(\rho(0)\le a\), the error is at most \(e\). Otherwise (2) gives \(0<\rho(0)-a\le e\), so (1) gives the stronger bound \(e+2Be/\lambda\). Consequently (5) covers initial stopping too, provided the reference is the dense first-threshold time.

The mesh construction below uses a positive error budget \(e>0\). If actual errors vanish, they may still be bounded by an arbitrarily small positive budget. With the literal budget \(e=0\), a positive first-crossing decrease cannot satisfy (3).

## 2. Euler approximation on a fixed finite interval

Write the compressed state as \(z(t)\in\mathbb R^d\), with autonomous ODE and prediction map

\[
\dot z(t)=G(z(t)),\qquad \widetilde f(t,x)=F(z(t),x).
\]

Assume \(G\) and every \(F(\cdot,x)\), \(x\in\mathcal P\), are continuously differentiable on an open domain \(D\). Let the exact solution exist on \([0,T]\) inside \(D\), where \(T>0\), and suppose its training RMS satisfies \(\widetilde\rho(T)\le a/2\). All statements here are conditional on this finite exact trajectory and residual guarantee. For a squared-loss flow, a uniformly positive training Gram matrix yields residual decay; a statement merely that a matrix is positive at each finite time does not by itself supply a uniform decay rate. Convergence to a point inside the smooth domain with a positive limiting training Gram does supply a positive lower eigenvalue bound on its tail.

The exact orbit segment is compact. Choose \(r>0\) such that its closed tube

\[
K_r=\{z:\operatorname{dist}(z,z([0,T]))\le r\}
\]

is contained in \(D\). Such an \(r\) exists because a compact subset of an open set has positive distance from its closed complement. On this fixed compact tube choose finite bounds

\[
\|G(z)\|_2\le M,\qquad
\|DG(z)\|_{2\to2}\le L,\qquad
\max_{x\in\mathcal P}\|D_zF(z,x)\|_2\le C.
\tag{6}
\]

These constants are chosen from the exact trajectory and the domain before analyzing the numerical trajectory. If the implementation must choose its own certified step size, effective upper bounds for them and an effective admissible \(T,r\) must be supplied; compactness alone is an existence argument, not a complexity bound for finding those certificates.

Use exact initialization and explicit Euler:

\[
z_0=z(0),\qquad z_{j+1}=z_j+hG(z_j),\qquad N=\lfloor T/h\rfloor.
\]

Set

\[
E_* = \frac{Mh}{2}(e^{LT}-1).
\tag{7}
\]

Choose \(h\) small enough that

\[
E_*<r/2,\qquad Mh<r/2.
\tag{8}
\]

Then every grid point \(j\le N\) is well defined, belongs to \(K_r\), and satisfies

\[
\|z_j-z(t_j)\|_2
\le\frac{Mh}{2}\bigl((1+hL)^j-1\bigr)
\le E_*.
\tag{9}
\]

Here is the bootstrap proof, without assuming the numerical trajectory stays in the tube. If \(z_j\) is within \(r\) of \(z(t_j)\), the line segment joining them lies in the ball of radius \(r\) around that exact orbit point, hence in \(K_r\). Therefore the derivative bound in (6) gives

\[
\|G(z_j)-G(z(t_j))\|_2\le L\|z_j-z(t_j)\|_2.
\]

Along the exact solution, \(\ddot z=DG(z)G(z)\), so its one-step Taylor remainder has norm at most \(LMh^2/2\). For \(j<N\), subtraction of exact and Euler updates gives

\[
\|z_{j+1}-z(t_{j+1})\|_2
\le(1+hL)\|z_j-z(t_j)\|_2+LMh^2/2.
\]

Starting from zero error, this recurrence proves (9). Its upper bound is less than \(r/2\), verifying the induction hypothesis at the next point. The formula includes \(L=0\): then the defect and all grid errors vanish. With nonexact initialization, one must add \((1+hL)^j\|z_0-z(0)\|_2\) to (9).

The same line-segment argument gives panel prediction error at most \(CE_*\). Moreover, each Euler line segment lies within distance \(E_*+Mh<r\) of \(z(t_j)\), so (6) gives

\[
|\rho_h^{j+1}-\rho_h^j|
\le\max_{x\in\mathcal P}|F(z_{j+1},x)-F(z_j,x)|
\le CMh.
\tag{10}
\]

Thus \(CE_*\le e_1\) supplies the numerical error budget and \(CMh\le e\) supplies (3), including any last-step overshoot. These requirements do not assume numerical residual monotonicity.

Rounding the horizon down requires one further bound. Along the exact orbit, each panel output changes at speed at most \(CM\), so

\[
\widetilde\rho(t_N)
\le\widetilde\rho(T)+CM(T-t_N)
\le a/2+CMh.
\]

Consequently, if

\[
CE_*<a/4,\qquad CMh<a/4,
\tag{11}
\]

then \(\rho_h^N<a\), and some first stopping index \(k\le N\) exists. One may also choose \(h<T\) to ensure \(N\ge1\) whenever needed. All conditions (8), (10), and (11) are satisfied by sufficiently small positive \(h\), because \(T,r,M,L,C\) are fixed and the desired positive error budgets are fixed. If \(M=0\) or \(C=0\), the relevant outputs are constant along this orbit; the assumed small final residual then already forces an initial stop. A horizon \(T=0\) with exact initialization also gives an immediate stop.

This proves finite Euler existence. It does not bound the necessary number of steps, arithmetic precision, or the cost of discovering the tube and field bounds.

## 3. Retained scalar storage and the compression target

A sequential Euler implementation retains its current \(d\)-coordinate state, an old-state or derivative buffer of \(O(d)\) coordinates as required for a simultaneous Euler update, the fixed coefficients needed to evaluate \(G\) and \(F\), and the workspace of those evaluations. Training RMS can be accumulated sample by sample using one accumulator, while the previous RMS and the loop state require only \(O(1)\) additional exact-real registers. Thus retained storage is

\[
O(d+\text{fixed coefficient storage}+\text{RHS/output workspace}),
\]

independent of the number of loop iterations. This statement assumes the arithmetic model treats loop counters and real registers as scalar cells and counts every fixed coefficient actually retained. It does not count an unrolled computational graph or a stored trajectory. In bit complexity, the counter and real approximations need precision-dependent storage; no such guarantee follows here. A claimed compression bound must also account for the provenance and storage of any retained dense initialization or coefficients.

For \(Y>0\), a desired terminal error \(Y/n\) is obtained by choosing

\[
e\le\frac{Y}{n(1+4B/\lambda)}.
\]

If the underlying compression theorem has scalar storage \(O(\log^3(Y/e))\), this changes its argument to

\[
\log\bigl(n(1+4B/\lambda)\bigr).
\]

It preserves \(O(\log^3 n)\) at fixed data when \(B/\lambda\) is independent of \(n\); it also preserves the order when this ratio is at most a fixed-degree polynomial in \(n\). The same conclusion holds for any fixed polynomial factor in \(B/\lambda\). Arbitrary width dependence, for example exponential growth, would invalidate that inference. This is conditional on the underlying logarithmic compression theorem, which is outside this check's supplied inputs. For all small widths one can write \(\log(2+n)\) to avoid a degenerate logarithm.

If \(Y=0\), the target \(Y/n=0\) cannot be justified by this positive-threshold argument. When zero labels also imply exact zero initial predictions in both constructions, the initial residuals vanish and squared-loss gradient flow is stationary, giving an immediate exact branch. Zero labels alone, with nonzero initial predictions, do not imply this branch or a finite exact-zero stopping time.

## 4. Endpoint benchmark limitation

A lower bound for representing two dense trajectories throughout an interval does not imply a lower bound for representing only their stopped predictions. The elementary trajectories \(u(t)=e^{-t}\) and \(v(t)=e^{-2t}\) have positive separation at interior times but the same limit. More closely matching threshold stopping, with one zero training label and \(a\in(0,1)\), each trajectory's first residual-\(a\) endpoint is exactly \(a\), despite their unequal trajectories. The endpoint task may discard information that the path task must retain. A terminal lower bound needs its own argument or a reduction that reconstructs the hard path information from the permitted endpoint data; the all-time lower bound alone supplies neither.

The remaining construction-specific obligations are therefore the same-time dense/compressed estimate on the chosen interval, effective certificates if required by the intended algorithmic claim, the full retained-state accounting, and a separate endpoint benchmark if one is asserted.
