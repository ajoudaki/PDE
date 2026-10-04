# Independent check of the first-layer centroid history construction

Scoped audit, 2026-09-30. Input: the supervisor's stated first-layer lemma and canonical gradient-flow dissipation. No other study, scientific source, training run, or agent was used. This checks a driven-history representation; it does not assume that its compressed histories close the original deep training dynamics.

**Verdict.** The normalized zeroth-history estimate and total descriptor count are correct with the stated constant \(M_2R^2/2\). The construction is causal and admits a capacity fixed from the initial loss and prescribed horizon. That capacity must be allocated as a global pool: the energy estimate controls the sum of neuron path lengths, not a uniform constant path length for every neuron. The error is uniform in neurons and normalized inputs, whereas the total storage is linear in width. The higher-mode fixed-anchor jet extension is also valid coefficientwise under the stated bounded polynomial basis; it does not establish a \(q\)-independent reconstruction error.

## 1. Precise hypotheses

Let \(a_i:[0,T]\to\mathbb R^d\), \(i=1,\ldots,n\), be absolutely continuous, with finite arclength

\[
V_i(t)=\int_0^t\|\dot a_i(s)\|\,ds.
\]

Let \(\rho\ge0\) be integrable, set

\[
\tau(t)=1+\int_0^t\rho(s)ds,
\qquad
h_i(t,x)=\phi\left(a_i(t)\cdot\frac{x}{\sqrt d}\right),
\]

and assume \(\phi\in C^2(\mathbb R)\), \(\sup|\phi''|\le M_2\). It is enough for the second-derivative bound to hold on every scalar interval used in the Taylor expansions below. The input set is

\[
\mathcal X_R=\{x:\|x\|/\sqrt d\le R\}.
\]

The driven forward history is exactly

\[
H_i(t,x)=h_i(0,x)+\int_0^t\rho(s)h_i(s,x)ds.
\tag{1}
\]

These hypotheses suffice for the approximation theorem. Canonical gradient flow is used only later to replace the realized path lengths by an a priori storage budget.

## 2. Online cells and exact first moments

Fix \(\delta>0\). Start a new cell whenever a neuron's accumulated arclength has increased by \(\delta\) since its previous cell boundary. Its current partial cell is included at every time. Every cell thus has arclength at most \(\delta\), and any two weights occurring in that cell differ in Euclidean norm by at most \(\delta\).

For a cell \(I_{ij}\), clipped at the current time \(t\), store

\[
\alpha_{ij}(t)=\int_{I_{ij}\cap[0,t]}\rho(s)ds,
\qquad
\mu_{ij}(t)=\int_{I_{ij}\cap[0,t]}\rho(s)a_i(s)ds.
\]

If \(\alpha_{ij}>0\), let \(\bar a_{ij}=\mu_{ij}/\alpha_{ij}\). A zero-mass cell contributes zero and needs no centroid evaluation. In particular, the implementation need not divide by zero at a cell's birth. Use accumulated mass and first moment as the active state; for the current cell they obey

\[
\dot\alpha_{ij}=\rho,\qquad \dot\mu_{ij}=\rho a_i.
\tag{2}
\]

For completed cells these quantities are constant. This state uses only the past and the present weight. No final centroid of an unfinished future segment is used.

The approximated normalized history is

\[
\widehat{\mathcal H}_i(t,x)=
\frac{h_i(0,x)+\sum_{j:\alpha_{ij}>0}
\alpha_{ij}\phi(\bar a_{ij}\cdot x/\sqrt d)}{\tau(t)}.
\tag{3}
\]

The initial feature is retained exactly. The result concerns this normalized history; multiplying back by \(\tau\) also multiplies the error bound.

## 3. Cancellation and the uniform estimate

Write \(z=x/\sqrt d\), so \(\|z\|\le R\). On a positive-mass cell, Taylor's theorem with the integral remainder implies

\[
\phi(a_i(s)\cdot z)=
\phi(\bar a_{ij}\cdot z)
+\phi'(\bar a_{ij}\cdot z)(a_i(s)-\bar a_{ij})\cdot z
+\mathcal R_{ij}(s,z),
\]

where

\[
|\mathcal R_{ij}(s,z)|
\le\frac{M_2}{2}|(a_i(s)-\bar a_{ij})\cdot z|^2
\le\frac{M_2R^2}{2}\|a_i(s)-\bar a_{ij}\|^2.
\tag{4}
\]

The linear term vanishes after integration because

\[
\int_{I_{ij}\cap[0,t]}\rho(s)(a_i(s)-\bar a_{ij})ds
=\mu_{ij}-\alpha_{ij}\bar a_{ij}=0.
\tag{5}
\]

Nonnegative \(\rho\) is important here: \(\bar a_{ij}\) belongs to the closed convex hull of the weights in that cell. Since the cell diameter is at most \(\delta\), for every weight in it,

\[
\|a_i(s)-\bar a_{ij}\|
\le\frac1{\alpha_{ij}}\int_{I_{ij}\cap[0,t]}
\rho(v)\|a_i(s)-a_i(v)\|dv\le\delta.
\tag{6}
\]

Combining (4)--(6), summing the cells, and using \(\sum_j\alpha_{ij}=\tau-1\) yields

\[
\boxed{
\sup_{i\le n}\sup_{0\le t\le T}\sup_{x\in\mathcal X_R}
\left|\frac{H_i(t,x)}{\tau(t)}-
\widehat{\mathcal H}_i(t,x)\right|
\le\frac{M_2R^2}{2}\delta^2.}
\tag{7}
\]

More precisely, at each time the bound is \((M_2R^2/2)\delta^2(\tau(t)-1)/\tau(t)\). The proof is deterministic and uses the same cells for every input. Thus no input covering number or probability union bound is hidden in the simultaneous input/time/neuron claim. The displayed constant is safe; sharpness is not needed for the claimed rate.

If the optional second norm moment

\[
\nu_{ij}=\int_{I_{ij}\cap[0,t]}\rho(s)\|a_i(s)\|^2ds
\]

is stored, the same proof gives the computable, possibly smaller uniform certificate

\[
\left|H_i/\tau-\widehat{\mathcal H}_i\right|
\le\frac{M_2R^2}{2\tau}
\sum_{j:\alpha_{ij}>0}
\left(\nu_{ij}-\frac{\|\mu_{ij}\|^2}{\alpha_{ij}}\right).
\tag{8}
\]

The quantity in parentheses equals \(\int\rho\|a_i-\bar a_{ij}\|^2\), so it is nonnegative in exact arithmetic.

## 4. Loss dissipation and total storage

For the canonical flow and the squared loss \(L(t)=\mathbb E(f_{\theta(t)}-Y)^2\), the stated preconditioner gives

\[
\frac{dL}{dt}
=-\|\dot\theta\|_{D^{-1}}^2,
\qquad
\int_0^T\frac{\|\dot W_1(t)\|_F^2}{n}dt
\le L(0)-L(T)\le L_0.
\tag{9}
\]

There is no extra factor of two in (9): \(\nabla L=2\mathbb E[r\nabla f]\), \(\dot\theta=-D\nabla L\), and \(\nabla L\cdot\dot\theta=-\dot\theta^TD^{-1}\dot\theta\).

By Cauchy--Schwarz first in time and then over rows,

\[
\begin{aligned}
\frac1n\sum_i V_i(T)
&\le\left(\frac1n\sum_iV_i(T)^2\right)^{1/2}\\
&\le\left(\frac Tn\int_0^T\|\dot W_1(t)\|_F^2dt\right)^{1/2}
\le\sqrt{T L_0}=\rho_0\sqrt T,
\end{aligned}
\tag{10}
\]

where \(\rho_0=\sqrt{L_0}\).

Each completed cell consumes exactly \(\delta\) of row arclength. Counting one active cell per neuron, including a temporarily empty one, gives

\[
N_{\rm cells}(t)
\le n+\sum_i\left\lfloor\frac{V_i(t)}\delta\right\rfloor
\le n+\left\lfloor\frac{n\rho_0\sqrt T}{\delta}\right\rfloor.
\tag{11}
\]

An atom needs \(d\) centroid or first-moment coordinates, one mass, and constant-sized metadata; the optional norm moment is one additional scalar. Active arclength counters and row-to-cell indices add order \(n+N_{\rm cells}\) entries. Consequently storage for this history representation is

\[
O\left(n(d+1)\left[1+\frac{\rho_0\sqrt T}{\delta}\right]\right).
\tag{12}
\]

The original exact initialization is a separately retained input. The current \(a_i(t)\) and \(\rho(t)\) are supplied by the driver; the count in (12) does not pretend to encode the rest of the deep training state.

For \(M_2R^2>0\), choosing

\[
\delta=\sqrt{\frac{2\varepsilon}{M_2R^2}}
\]

proves uniform error at most \(\varepsilon\), with descriptor count

\[
O\left(nd\left[1+\rho_0R\sqrt{\frac{M_2T}{\varepsilon}}\right]\right)
\quad(d\ge1).
\tag{13}
\]

This count is independent of the number of training examples. It has an explicit linear input-dimension factor and no dimension exponent generated by approximating functions on a grid. To call its constants dimension independent, the normalized radius \(R\), activation bound \(M_2\), and initial residual \(\rho_0\) must themselves have dimension-independent bounds. This qualification is also necessary for a width-uniform complexity constant.

If \(M_2=0\), the activation is affine and a single mass/first-moment accumulator per neuron is exact; no arclength splitting is needed. If \(R=0\), only the zero input is being tested and the history is immediate. If \(L_0=0\), canonical gradient flow is stationary.

## 5. Online fixed capacity: valid globally, not equally per neuron

Equation (11) supplies an a priori capacity from \(n,L_0,T,\delta\). Reserve one active record per neuron and a global pool of

\[
\left\lfloor n\rho_0\sqrt T/\delta\right\rfloor
\]

completed-cell records. When a row consumes \(\delta\) arclength, freeze its current mass and centroid into the pool, reset its active accumulators, and continue. The energy bound guarantees that the pool cannot overflow before \(T\). No future trajectory information is required to set its capacity or choose a cell boundary. Event counts are finite because every event consumes positive arclength and the total arclength is finite.

One must not allocate only \(1+\rho_0\sqrt T/\delta\) records to *each* neuron and infer success from (10). Energy can be concentrated in a few rows. From (9) alone the individual bound is merely

\[
V_i(T)\le\sqrt{nT L_0},
\]

so an individual row may need order \(1+\sqrt n\,\rho_0\sqrt T/\delta\) cells. Global pooling preserves the width-linear total count without a per-neuron path assumption.

At a cell boundary, moving the old active atom into the completed pool leaves (3) unchanged, and the new active atom starts with mass zero. Thus the approximation is continuous at events, though its time derivative need not be continuous. The state evolution is a finite-capacity hybrid accumulator on the prescribed horizon. It is a driven system until an evolution law for the compressed deep state is proved.

## 6. Check of the higher-mode fixed-anchor extension

This extension is valid with a different, fixed cell anchor \(c_{ij}=a_i(t_{ij})\). For every point in the cell, \(\|a_i(s)-c_{ij}\|\le\delta\), so

\[
\phi(a_i(s)\cdot z)
=\phi(c_{ij}\cdot z)
+\phi'(c_{ij}\cdot z)(a_i(s)-c_{ij})\cdot z
+R_{ij}(s,z),
\qquad |R_{ij}|\le M_2R^2\delta^2/2.
\tag{14}
\]

Let \(p_k\) be a polynomial of degree \(k\) with \(\sup_{v\in[0,1]}|p_k(v)|\le1\). For each cell retain

\[
A_{ijk}(t)=\int_{I_{ij}\cap[0,t]}\rho(s)
p_k\left(\frac{\tau(s)}{\tau(t)}\right)ds,
\]

\[
C_{ijk}(t)=\int_{I_{ij}\cap[0,t]}\rho(s)
p_k\left(\frac{\tau(s)}{\tau(t)}\right)(a_i(s)-c_{ij})ds.
\]

The corresponding cell output is

\[
A_{ijk}\phi(c_{ij}\cdot z)
+\phi'(c_{ij}\cdot z)C_{ijk}\cdot z.
\tag{15}
\]

Integrating (14) against the possibly signed polynomial weight and using \(|p_k|\le1\) proves the same error bound (7) for each normalized history mode, provided the initial prefix is included exactly in the definition of that mode. There is no need to define a centroid using a signed mass, which could vanish or place its putative centroid outside the cell.

The transport statement is exact. Since \(v p_k'(v)\) is a polynomial of degree at most \(k\), write

\[
v p_k'(v)=\sum_{\ell=0}^k\mathsf T_{k\ell}p_\ell(v).
\]

If \(\chi_{ij}(t)\) indicates the active cell, differentiation gives, away from the finite event times,

\[
\dot A_{ijk}=\rho\chi_{ij}p_k(1)
-\frac\rho\tau\sum_{\ell\le k}\mathsf T_{k\ell}A_{ij\ell},
\]

\[
\dot C_{ijk}=\rho\chi_{ij}p_k(1)(a_i-c_{ij})
-\frac\rho\tau\sum_{\ell\le k}\mathsf T_{k\ell}C_{ij\ell}.
\tag{16}
\]

For the usual unnormalized shifted Legendre polynomials \(p_k(1)=1\), this has the supplied triangular transport form. Completed-cell moments must continue to evolve under the transport term, because their polynomial clock weights change as \(\tau\) changes. Freezing those modal moments at cell completion would be wrong. Only their source term turns off. Anchors must remain fixed for (16); moving an anchor adds derivative terms.

Retaining \(q\) scalar and \(q\) vector moments, together with the fixed anchor, costs \(O(q(d+1))\) entries per cell. The error bound is uniform in \(k<q\) for the specified basis normalization. It does not directly control a sum of \(q\) errors, a weighted modal norm, or a reconstruction with weights \(2k+1\); those uses require their own factors or Parseval estimate. A basis normalized to have larger suprema would multiply the error by those suprema.

## 7. Boundary of the proved result

The construction proves functional approximation of first-layer driven histories, uniformly over a continuous normalized input domain, with a sample-count-independent finite descriptor budget. It is stronger than a snapshot existence result because one causal algorithm and one fixed capacity work for all times in the prescribed interval.

It does not show that the approximate histories provide accurate gradients, backward fields, or weight trajectories when fed back into the entire deep system. In that use, the arclength and loss dissipation of the *surrogate* driver must also be controlled, and the errors introduced into the other fields and reconstruction must be propagated. The exact driver's energy bound cannot simply be reassigned to an unproved approximate closed flow.
