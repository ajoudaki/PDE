# Actual all-angle first-layer compactness at depth two

Self-contained theorem and proof assembly, 2026-09-06.

This document proves compactness for the actual finite gradient flow and
the actual simultaneous raw gradient descent specified below. It includes
both samples in each neuron law, strong velocity compactness, raw first-row
reconstruction, and convergence of every entry of the node-controlled first
kernel along any convergent subsequence. It does not identify a mean-field
equation or a unique limit. It supplies a first-layer result to support,
without replacing, a broader mean-field research program.

## 1. Model, conventions, and theorem

Fix an integer input dimension \(d\ge1\), deterministic inputs
\(x_1,x_2\in\mathbb R^d\), and opposite labels
\((y_1,y_2)=(1,-1)\), with
\[
 |x_1|^2=|x_2|^2=d,\qquad
 X=[x_1,x_2],\qquad
 C=\frac{X^TX}{d}=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad -1\le\rho<1.
 \tag{1}
\]
The reversed label ordering is covered by interchanging the sample names.
The pair of inputs, including its correlation, is fixed independently of
initialization. No input chosen after observing the weights is allowed in
the probability assertions. Throughout the theorem \(0\le T<\infty\) is fixed.

All vector norms \(|\cdot|\), or \(\|\cdot\|\) on finite vectors, are
ordinary Euclidean norms. Matrix norms \(\|\cdot\|_F\) and
\(\|\cdot\|_{\rm op}\) are the ordinary Frobenius and spectral norms.
Every normalization by \(n\) or \(d\) is displayed explicitly.
For neuron-indexed two-vectors we use the explicitly defined notation
\[
 \langle a_i\rangle_n=\frac1n\sum_{i=1}^n a_i,\qquad
 \|a\|_{n,2}=\left(\frac1n\sum_i|a_i|^2\right)^{1/2},
 \qquad
 \|a\|_{p;n,I}=
 \left(\frac1n\sum_i\int_I|a_i(t)|^pdt\right)^{1/p}.
 \tag{2}
\]
These are explicitly normalized array norms, not a change in the meaning
of any matrix or vector norm.

Both hidden activations are
\[
 \phi(s)=\arctan s,\qquad p(s)=\phi'(s)=\frac1{1+s^2},
 \qquad B=\frac\pi2.
 \tag{3}
\]
Thus \(|\phi|\le B\), \(0<p\le1\), and
\(|p'(s)|=2|s|/(1+s^2)^2\le1\), using \(2|s|\le1+s^2\).
The readout is linear. All finite network fields use lowercase symbols
and hidden-layer superscripts; population coordinate fields introduced
below use capitals. Suppress the width index when no confusion is possible.
At width \(n\), let
\[
 w^{(1)}\in\mathbb R^{n\times d},\quad
 w^{(2)}\in\mathbb R^{n\times n},\quad w^{(3)}\in\mathbb R^n.
\]
Here \(w^{(3)}\) is the rescaled readout that occurs in the following
actual prediction, with the displayed factor \(1/n\):
\[
\begin{aligned}
 z^{(1)}_a&=w^{(1)}x_a,& h^{(1)}_a&=\phi(z^{(1)}_a),\\
 z^{(2)}_a&=w^{(2)}h^{(1)}_a,& h^{(2)}_a&=\phi(z^{(2)}_a),\\
 f_a&=\frac1n(w^{(3)})^Th^{(2)}_a,&r_a&=f_a-y_a,\\
 \delta^{(2)}_a&=w^{(3)}\odot p(z^{(2)}_a),&
 q^{(1)}_a&=(w^{(2)})^T\delta^{(2)}_a,\\
 \delta^{(1)}_a&=p(z^{(1)}_a)\odot q^{(1)}_a,&c_a&=-2r_a.
\end{aligned}
\tag{4}
\]
The symbol \(\odot\) denotes coordinatewise multiplication. The physical
loss is the **sum**, without a factor \(1/2\) or a sample average:
\[
 \ell(w)=r_1^2+r_2^2.
 \tag{5}
\]
Gradient flow (GF) means the exact equations
\[
\begin{aligned}
 \dot w^{(1)}&=\frac1d\sum_{a=1}^2c_a\delta^{(1)}_a x_a^T,\\
 \dot w^{(2)}&=\frac1n\sum_{a=1}^2c_a\delta^{(2)}_a(h^{(1)}_a)^T,\\
 \dot w^{(3)}&=\sum_{a=1}^2c_a h^{(2)}_a.
\end{aligned}
\tag{6}
\]
Raw gradient descent (GD) means the simultaneous updates, all right-hand
sides evaluated at the old node \(k\),
\[
\begin{aligned}
 w^{(1)}_{k+1}&=w^{(1)}_k+\frac\eta d\sum_a
                    c_{k,a}\delta^{(1)}_{k,a}x_a^T,\\
 w^{(2)}_{k+1}&=w^{(2)}_k+\frac\eta n\sum_a
                    c_{k,a}\delta^{(2)}_{k,a}(h^{(1)}_{k,a})^T,\\
 w^{(3)}_{k+1}&=w^{(3)}_k+\eta\sum_a c_{k,a}h^{(2)}_{k,a},
 \qquad \eta=\eta_n=n^{-2}.
\end{aligned}
\tag{7}
\]
Put \(N=\lceil T/\eta\rceil\). On \([k\eta,(k+1)\eta]\), interpolate
the raw parameters affinely between their two nodes. Unless a bar is
specified, all nonlinear fields on that interpolation are recomputed
using (4). In particular \(h^{(1)}(t)=\phi(z^{(1)}(t))\), and is generally
not affine. A bar denotes the held left-node value on a cell; the value at
the final endpoint is immaterial to integrated statements.

For each first neuron keep the two sample coordinates together and define
\[
 z^{(1)}_i=(z^{(1)}_{1,i},z^{(1)}_{2,i}),\quad
 h^{(1)}_i=(h^{(1)}_{1,i},h^{(1)}_{2,i}),\quad
 v^{(1)}_i=\dot z^{(1)}_i,\quad s^{(1)}_i=\dot h^{(1)}_i.
 \tag{8}
\]
For GD the derivatives in (8) are taken almost everywhere along the raw
interpolation. Set
\[
 \mathcal E_T=C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)
              \times C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2),
\]
\[
 \|(z,v,h,s)\|_{\mathcal E_T}^2
   =\|z\|_\infty^2+\|v\|_2^2+\|h\|_\infty^2+\|s\|_2^2,
 \qquad
 \mu_n=\frac1n\sum_i
       \delta_{(z^{(1)}_i,v^{(1)}_i,h^{(1)}_i,s^{(1)}_i)}.
 \tag{9}
\]
The \(L^2\) norms in (9) use Lebesgue time measure without normalization.
For probability measures with finite second moment, \(W_2\) is the
infimum over couplings of the square root of the expected squared
\(\mathcal E_T\) distance. It uses the strong \(L^2\) norm in both
velocity coordinates.

**Theorem.** The following conclusions hold.

1. **Deterministic actual dynamics and compact containment.** Fix finite
   constants \(\alpha,\beta,m\ge0\), and impose only
   \[
    \|w^{(2)}_0\|_{\rm op}\le\alpha,\qquad
    \|w^{(3)}_0\|_\infty\le\beta,\qquad
    \frac1n\sum_i|z^{(1)}_i(0)|^4\le m.
    \tag{10}
   \]
   GF exists globally at every finite width. There is a deterministic
   threshold \(n_0=n_0(T,\alpha,\beta)\) such that the actual GD nodes
   through \(N\) have nonincreasing loss for \(n\ge n_0\). Both schemes
   satisfy the primal, reverse-query, action, and moment bounds proved
   in Sections 2–5. There is a single deterministic compact set
   \[
    \mathcal K_{T,\rho;\alpha,\beta,m}
       \subset\mathcal P_2(\mathcal E_T)
    \tag{11}
   \]
   containing every GF law satisfying (10), at every width, and every
   GD law satisfying (10), at every \(n\ge n_0\). This quantifies over
   **all** initial outcomes satisfying (10), not one selected outcome
   per width. The moment and stability constants are independent of
   \(d,n,\rho\); the strong compactness constants may depend on the
   fixed \(\rho\). At \(\rho=-1\) the asserted endpoint uses the exact
   antiparallel identities proved in Section 6.

2. **Actual Gaussian initialization.** Initialize all entries independently
   with
   \[
    w^{(1)}_{0,ij}\sim N(0,d^{-1}),\quad
    w^{(2)}_{0,ij}\sim N(0,n^{-1}),\quad
    w^{(3)}_{0,i}\sim N(0,n^{-2}).
    \tag{12}
   \]
   In particular the finite readout is not replaced by zero. Let
   \[
    E_n=\left\{\|w^{(2)}_0\|_{\rm op}\le8,
                  \ \|w^{(3)}_0\|_\infty\le1,
                  \ \frac1n\sum_i|z^{(1)}_i(0)|^4\le13\right\}.
   \]
   Then
   \[
    \mathbb P(E_n^c)\le b_n:={1680\over n}
             +2e^{-(8-2\log9)n}+2ne^{-n^2/2}\longrightarrow0.
    \tag{13}
   \]
   With \(\mathcal K_{T,\rho}=\mathcal K_{T,\rho;8,1,13}\), for either
   scheme \(S\in\{\mathrm{GF},\mathrm{GD}\}\),
   \[
    \mathbb P\{\mu_n^S\notin\mathcal K_{T,\rho}\}\le b_n,
                       \qquad n\ge n_0(T,8,1).
    \tag{14}
   \]
   For common initialization the failure probability for joint containment
   of both schemes is at most \(b_n\); for separate initializations it is
   at most \(2b_n\). The same events work for each fixed finite horizon.

3. **Consequences along any \(W_2\)-convergent subsequence.** For any
   deterministic selection of trajectories from the preceding families,
   and along any subsequence on which \(\mu_n\to\mu\) in \(W_2\), let
   \((Z^{(1)},V^{(1)},H^{(1)},S^{(1)})\) be the coordinate fields on
   \((\mathcal E_T,\mu)\). Then, \(\mu\)-almost surely,
   \[
   \begin{gathered}
    Z^{(1)}(t)=Z^{(1)}(0)+\int_0^t V^{(1)}(u)du,\qquad
    H^{(1)}=\phi(Z^{(1)}),\\
    S^{(1)}=p(Z^{(1)})\odot V^{(1)}\quad\text{in }L^2,\qquad
    H^{(1)}(t)=H^{(1)}(0)+\int_0^t S^{(1)}(u)du.
   \end{gathered}
   \tag{15}
   \]
   Define the fixed matrices
   \[
    D=\begin{cases}C^{-1},&-1<\rho<1,\\ C/4,&\rho=-1,\end{cases}
    \qquad A_{\rm row}=XD/d.
    \tag{16}
   \]
   The empirical laws of the actual first-row increments and velocities
   converge in \(W_2(C([0,T];\mathbb R^d)\times L^2([0,T];\mathbb R^d))\)
   to the law of
   \[
    R^{(1)}=A_{\rm row}[Z^{(1)}-Z^{(1)}(0)],\qquad
    B^{(1)}=A_{\rm row}V^{(1)}.
    \tag{17}
   \]
   This convergence may also be taken jointly with the four fields in (9).
   There is no kinetic defect: all three speed densities converge in
   \(L^1([0,T])\),
   \[
   \begin{aligned}
    \frac1n\sum_i|v^{(1)}_i(t)|^2&\longrightarrow
                       \mathbb E_\mu|V^{(1)}(t)|^2,\\
    \frac1n\sum_i|s^{(1)}_i(t)|^2&\longrightarrow
                       \mathbb E_\mu|S^{(1)}(t)|^2,\\
    g_n^{(1)}(t):=\frac d n\|\dot w_n^{(1)}(t)\|_F^2&\longrightarrow
       G^{(1)}(t):=\mathbb E_\mu[(V^{(1)}(t))^TDV^{(1)}(t)].
   \end{aligned}
   \tag{18}
   \]
   In particular their integrals converge on every fixed measurable time
   subset of \([0,T]\).

   For GF use the actual instantaneous fields in the following definition;
   for GD use the held **node** fields on each cell:
   \[
   \begin{aligned}
    k^{(1)}_{n,ab}(t)&=C_{ab}\frac1n\sum_i
                         \delta^{(1)}_{n,a,i}(t)\delta^{(1)}_{n,b,i}(t),\\
    j^{(1)}_{n,ab}(t)&=c_{n,a}(t)c_{n,b}(t)k^{(1)}_{n,ab}(t).
   \end{aligned}
   \tag{19}
   \]
   Thus every finite symbol on the right of (19) is barred in GD.
   The entire two-by-two matrix converges in matrix-valued \(L^1\), using
   the ordinary Frobenius norm inside the time integral:
   \[
    j_n^{(1)}\longrightarrow J^{(1)},\qquad
    J^{(1)}_{ab}(t)=C_{ab}\mathbb E_\mu[
                (DV^{(1)}(t))_a(DV^{(1)}(t))_b].
    \tag{20}
   \]
   The formula specifies an almost-everywhere representative of the
   limiting \(L^1\) function. It does not assert almost-everywhere
   convergence of the full kernel sequence. The speed identities are
   \[
    \sum_{a,b}j^{(1)}_{n,ab}=g_n^{(1)},\qquad
    \sum_{a,b}J^{(1)}_{ab}=G^{(1)}.
    \tag{21}
   \]
   The sum is over all four entries, not just the trace.

Every expectation \(\mathbb E_\mu\) here concerns the population neuron
law \(\mu\). It is not an expectation over the original initialization.
Section 12 states the precise limits of the conclusions.

The proof first establishes actual finite stability and regularity of the
transpose query. A row work identity converts those bounds into stronger
moments. The relative arctan gate then supplies strong velocity time
regularity. A step-function estimate makes that regularity uniform over
all admissible GD widths. Finite time projections and explicit couplings
give compact containment; fixed linear and quadratic maps give (17)–(21).

## 2. The raw metric and global finite gradient flow

For a raw tangent \(\xi=(\xi^{(1)},\xi^{(2)},\xi^{(3)})\), define
\[
 \|\xi\|_{\rm raw}^2=\frac d n\|\xi^{(1)}\|_F^2
                     +\|\xi^{(2)}\|_F^2
                     +\frac1n\|\xi^{(3)}\|^2.
 \tag{22}
\]
Differentiating (4) gives the ordinary Euclidean gradients
\[
 \nabla_{w^{(1)}}\ell=\frac2n\sum_a r_a\delta^{(1)}_a x_a^T,
 \quad
 \nabla_{w^{(2)}}\ell=\frac2n\sum_a r_a\delta^{(2)}_a(h^{(1)}_a)^T,
 \quad
 \nabla_{w^{(3)}}\ell=\frac2n\sum_a r_a h^{(2)}_a.
 \tag{23}
\]
Dividing these three blocks by the weights \(d/n,1,1/n\) in (22)
shows that (6) is \(-\operatorname{grad}_{\rm raw}\ell\), and (7) is
its exact Euler update in the raw parameters. Consequently, along GF,
\[
 \dot\ell=-\|\dot w\|_{\rm raw}^2
       =-\frac d n\|\dot w^{(1)}\|_F^2
        -\|\dot w^{(2)}\|_F^2-\frac1n\|\dot w^{(3)}\|^2.
 \tag{24}
\]

For completeness, the finite vector field is continuously differentiable.
On a sufficiently small closed parameter ball it is bounded by a constant
and Lipschitz with a constant \(L\). On a sufficiently short interval the
map \(w(\cdot)\mapsto w_0+\int_0^\cdot F(w(s))ds\) preserves that ball
and is a contraction with constant less than one. Its successive iterates
converge geometrically in the uniform norm to the unique local solution.
At any putative finite terminal time \(t_*\), (24) implies
\[
 \int_0^{t_*}\|\dot w\|_{\rm raw}^2dt\le\ell(0),\qquad
 \|w(t)-w(s)\|_{\rm raw}\le\sqrt{|t-s|\ell(0)}.
 \tag{25}
\]
At fixed \(n,d\) this is a positive definite finite-dimensional metric.
The solution has a finite endpoint limit, and the same local construction
extends it from that limit. This excludes a finite terminal time and proves
global existence and uniqueness at finite width.

Here and in the next two sections first assume just the first two bounds
in (10). Put
\[
\begin{aligned}
 R_0&=\sqrt2(B\beta+1),&K_c^{\rm F}&=2\sqrt2R_0,\\
 M_{\rm F}&=\beta+BK_c^{\rm F}T,&
 A_{\rm F}&=\alpha+B\left(\beta K_c^{\rm F}T
                                  +B(K_c^{\rm F})^2T^2/2\right),\\
 Q_{\rm F}&=A_{\rm F}M_{\rm F}.
\end{aligned}
\tag{26}
\]
Initially \(|f_a|\le B\beta\). By (24), \(|r(t)|\le R_0\) and
\(\sum_a|c_a(t)|\le K_c^{\rm F}\). Integrating the readout equation
bounds every coordinate by \(\beta+BK_c^{\rm F}t\). For vectors \(u,v\),
\(\|uv^T\|_{\rm op}=\|uv^T\|_F=|u||v|\): the matrix has image in
the span of \(u\) and reaches this norm on \(v/|v|\) when both are
nonzero. Applying this fact to the rank-one updates in (6), using
\(|h^{(1)}_a|\le B\sqrt n\), gives \(A_{\rm F}\) in (26).
Thus, at every \(t\in[0,T]\),
\[
\begin{gathered}
 \|w^{(3)}\|_\infty\le M_{\rm F},\qquad
 \|w^{(2)}\|_{\rm op}\le A_{\rm F},\qquad
 \frac{\|h^{(\ell)}_a\|}{\sqrt n}\le B\quad(\ell=1,2),\\
 \frac{\|z^{(2)}_a\|}{\sqrt n}\le A_{\rm F}B,
 \quad \frac{\|\delta^{(2)}_a\|}{\sqrt n}\le M_{\rm F},
 \quad \frac{\|q^{(1)}_a\|}{\sqrt n}\le Q_{\rm F},
 \quad \frac{\|\delta^{(1)}_a\|}{\sqrt n}\le Q_{\rm F},\\
 \frac{\|\dot z^{(1)}_a\|}{\sqrt n}\le K_c^{\rm F}Q_{\rm F},
 \qquad \frac{\|\dot h^{(1)}_a\|}{\sqrt n}
                              \le K_c^{\rm F}Q_{\rm F}.
\end{gathered}
\tag{27}
\]
The last line uses the exact equation
\(\dot z^{(1)}_a=\sum_b C_{ab}c_b\delta^{(1)}_b\) and
\(|C_{ab}|\le1\). If the last bound in (10) also holds, Minkowski and
Cauchy–Schwarz give the explicit first-primal bound
\[
 \frac{\|z^{(1)}_a(t)\|}{\sqrt n}
       \le m^{1/4}+T K_c^{\rm F}Q_{\rm F}.
 \tag{28}
\]
No coordinate bound on \(w^{(1)}_0\) or \(q^{(1)}\) was used.

Write temporarily \(K_c=K_c^{\rm F},M=M_{\rm F},A=A_{\rm F},Q=Q_{\rm F}\)
and set
\[
\begin{aligned}
 D_A&=K_cMB,&D_w&=K_cB,\\
 D_Z&=D_AB+AK_cQ,&D_\delta&=D_w+MD_Z,\\
 D_q&=D_AM+AD_\delta.
\end{aligned}
\tag{29}
\]
The rank-one bound gives \(\|\dot w^{(2)}\|_{\rm op}\le D_A\),
and \(\|\dot w^{(3)}\|_\infty\le D_w\). The exact product rules are
\[
\begin{aligned}
 \dot z^{(2)}_a&=\dot w^{(2)}h^{(1)}_a+w^{(2)}\dot h^{(1)}_a,\\
 \dot\delta^{(2)}_a
   &=\dot w^{(3)}\odot p(z^{(2)}_a)
            +w^{(3)}\odot p'(z^{(2)}_a)\odot\dot z^{(2)}_a,\\
 \dot q^{(1)}_a&=(\dot w^{(2)})^T\delta^{(2)}_a
                          +(w^{(2)})^T\dot\delta^{(2)}_a.
\end{aligned}
\tag{30}
\]
Using the coordinatewise readout bound in the middle line, these prove
\[
 \frac{\|\dot z^{(2)}_a\|}{\sqrt n}\le D_Z,
 \qquad \frac{\|\dot\delta^{(2)}_a\|}{\sqrt n}\le D_\delta,
 \qquad \frac{\|\dot q^{(1)}_a\|}{\sqrt n}\le D_q.
 \tag{31}
\]
This differentiates the actual transpose query. In particular there is
no product here of an uncontrolled hidden reverse field and a hidden
velocity.

Differentiating the prediction in each parameter block yields
\(\dot r=-2kr\), with finite kernel
\[
 k_{ab}=C_{ab}\frac{(\delta^{(1)}_a)^T\delta^{(1)}_b}{n}
       +\frac{(\delta^{(2)}_a)^T\delta^{(2)}_b}{n}
                           \frac{(h^{(1)}_a)^Th^{(1)}_b}{n}
       +\frac{(h^{(2)}_a)^Th^{(2)}_b}{n}.
 \tag{32}
\]
Each term is obtained by inserting its corresponding equation in (6)
into the differential of \(f_a\); thus all factors of \(d,n\) and the
sum-loss factor two are retained. Each entry has absolute value at most
\(K_*=Q^2+M^2B^2+B^2\). Its operator norm is at most its Frobenius norm,
which is at most \(2K_*\). Therefore
\[
 \sum_a|\dot c_a|\le8\sqrt2K_*R_0=:D_c^{\rm F}.
 \tag{33}
\]

## 3. GF row work and the gain in moments

Define the controlled query and its gated version by
\[
 u^{(1)}_{a,i}=c_aq^{(1)}_{a,i},\qquad
 e^{(1)}_{a,i}=p(z^{(1)}_{a,i})u^{(1)}_{a,i}
                         =c_a\delta^{(1)}_{a,i}.
 \tag{34}
\]
Use the GF constants from (26)–(33) and put
\[
 K_u^{\rm F}=D_c^{\rm F}Q_{\rm F}+K_c^{\rm F}D_q,
 \qquad
 V_{\rm F}=K_c^{\rm F}Q_{\rm F}+T K_u^{\rm F}.
 \tag{35}
\]
In (35), the scalar \(V_{\rm F}\) is an envelope constant, distinct from
the population velocity \(V^{(1)}\). The product rule and (31),(33) give
\[
 \left(\frac1n\sum_i
          \left(\sum_a|\dot u^{(1)}_{a,i}|\right)^2\right)^{1/2}
       \le K_u^{\rm F}.
 \tag{36}
\]
For each neuron define the auxiliary first-layer scalar envelope
\[
 \upsilon_i^{(1)}=\sum_a|u^{(1)}_{a,i}(0)|
                   +\int_0^T\sum_a|\dot u^{(1)}_{a,i}(t)|dt.
 \tag{37}
\]
The triangle inequality in finite-dimensional Euclidean space, applied
also to Riemann sums and then their integrals, proves
\[
 \sum_a|u^{(1)}_{a,i}(t)|\le\upsilon_i^{(1)},\qquad
 \left(\frac1n\sum_i(\upsilon_i^{(1)})^2\right)^{1/2}\le V_{\rm F}.
 \tag{38}
\]

Treat row \(i\) of \(w^{(1)}\) as a column vector when multiplying by
\(X\). Equations (6) and (34) give
\[
 \dot w^{(1)}_i=Xe^{(1)}_i/d,\qquad
 v^{(1)}_i=Ce^{(1)}_i,\qquad
 d|\dot w^{(1)}_i|^2=(e^{(1)}_i)^TCe^{(1)}_i
                         =\sum_a u^{(1)}_{a,i}s^{(1)}_{a,i}.
 \tag{39}
\]
The last equality uses \(s^{(1)}_{a,i}=p(z^{(1)}_{a,i})v^{(1)}_{a,i}\).
The left side is nonnegative for every correlation in (1).
Integration by parts, including both boundary terms, proves that the
one-row raw action
\[
 \mathcal A_i^{\rm F}:=\int_0^T d|\dot w^{(1)}_i|^2dt
\]
satisfies
\[
\begin{aligned}
 0\le\mathcal A_i^{\rm F}
 &\le B\left(\sum_a|u^{(1)}_{a,i}(T)|+
                   \sum_a|u^{(1)}_{a,i}(0)|+
                   \int_0^T\sum_a|\dot u^{(1)}_{a,i}|dt\right)\\
 &\le2B\upsilon_i^{(1)}.
\end{aligned}
\tag{40}
\]
This linear bound in \(\upsilon_i^{(1)}\) is the moment gain.

The eigenvalues of \(C\) are \(1+\rho\) and \(1-\rho\), in \([0,2]\).
Diagonalizing this explicit symmetric matrix gives
\(|Ce|^2\le2e^TCe\). Also \(|e^{(1)}_i|\le\upsilon_i^{(1)}\). Hence
\[
 |v^{(1)}_i|^2\le2d|\dot w^{(1)}_i|^2,\quad
 |v^{(1)}_i|\le2\upsilon_i^{(1)},\quad
 \int_0^T|v^{(1)}_i|^2dt\le4B\upsilon_i^{(1)},
 \quad \int_0^T|v^{(1)}_i|^3dt\le8B(\upsilon_i^{(1)})^2.
 \tag{41}
\]
The chain rule gives \(|s^{(1)}_i|\le|v^{(1)}_i|\). Moreover,
\[
 \sup_{t\le T}|z^{(1)}_i(t)|
       \le |z^{(1)}_i(0)|+\sqrt{2T\mathcal A_i^{\rm F}}.
\]
Using \((a+b)^4\le8(a^4+b^4)\) and (40), we obtain the actual GF bounds
\[
\begin{aligned}
 \frac1n\sum_i\|z^{(1)}_i\|_\infty^4
       &\le8m+128B^2T^2V_{\rm F}^2,\\
 \frac1n\sum_i\int_0^T|v^{(1)}_i|^3dt&\le8BV_{\rm F}^2,\qquad
 \frac1n\sum_i\int_0^T|s^{(1)}_i|^3dt\le8BV_{\rm F}^2,\\
 \left(\frac1n\sum_i\|v^{(1)}_i\|_2^4\right)^{1/2}
       &\le4BV_{\rm F}.
\end{aligned}
\tag{42}
\]
All these calculations remain valid for singular \(C\); no inverse has
yet been used.

## 4. Exact raw GD: a closed descent and primal estimate

Assume \(T>0\), put \(H=T+1\), and define
\[
\begin{aligned}
 R&=R_0+1,& K_c^{\rm G}&=2\sqrt2R,\\
 M_{\rm G}&=\beta+BK_c^{\rm G}H,&
 A_{\rm G}&=\alpha+H K_c^{\rm G}M_{\rm G}B,&
 Q_{\rm G}&=A_{\rm G}M_{\rm G}.
\end{aligned}
\tag{43}
\]
Stop just before the first node with residual norm exceeding \(R\).
Every preceding update has \(\sum_a|c_{k,a}|\le K_c^{\rm G}\). Since
\(N\eta\le H\) for \(\eta\le1\), summing its exact readout and
rank-one matrix increments gives the bounds \(M_{\rm G},A_{\rm G}\)
at every endpoint up to and including a candidate exit endpoint.
By convexity of the two norms these bounds hold throughout each raw
segment as well. At these parameters, all the nondifferential bounds
in (27) hold with GF constants replaced by GD constants.

We prove descent before using it. Abbreviate \(K_c=K_c^{\rm G}\),
\(M=M_{\rm G}, A=A_{\rm G},Q=Q_{\rm G}\) in this section. For a unit
raw tangent \(\xi\) set
\[
 a_1=\sqrt{d/n}\|\xi^{(1)}\|_F,\quad
 a_2=\|\xi^{(2)}\|_F,\quad a_3=\|\xi^{(3)}\|/\sqrt n.
\]
Each \(a_\ell\le1\), and input normalization gives
\[
 \frac{\|D_\xi z^{(1)}_a\|}{\sqrt n}\le a_1,
 \qquad
 \frac{\|D_\xi z^{(2)}_a\|}{\sqrt n}\le Ba_2+Aa_1.
 \tag{44}
\]
Put \(J_0=B+A\) and \(F_*=B+MJ_0\). Differentiating \(f_a\)
and using the ordinary Cauchy–Schwarz inequality gives
\( |D_\xi f_a|\le F_*\).

For another unit tangent \(\zeta\), the mixed hidden derivative is
exactly
\[
\begin{aligned}
 D_\zeta D_\xi z^{(2)}_a
   ={}&\xi^{(2)}[p(z^{(1)}_a)\odot\zeta^{(1)}x_a]
       +\zeta^{(2)}[p(z^{(1)}_a)\odot\xi^{(1)}x_a]\\
      &+w^{(2)}[p'(z^{(1)}_a)\odot(\zeta^{(1)}x_a)
                                      \odot(\xi^{(1)}x_a)].
\end{aligned}
\tag{45}
\]
The first two terms have RMS norm at most one each. For the last use
\[
 \frac{\|u\odot v\|}{\sqrt n}
 \le\sqrt n\left(\frac{\|u\|}{\sqrt n}\right)
              \left(\frac{\|v\|}{\sqrt n}\right),
\]
which follows by expanding the nonnegative double sum
\((\sum_i u_i^2)(\sum_jv_j^2)\). Thus (45) has RMS norm at most
\(2+A\sqrt n\). The full second prediction derivative consists of
\[
\begin{aligned}
 D_\zeta D_\xi f_a=\frac1n\bigl(&
  (\xi^{(3)})^T[p(z^{(2)}_a)\odot D_\zeta z^{(2)}_a]
 +(\zeta^{(3)})^T[p(z^{(2)}_a)\odot D_\xi z^{(2)}_a]\\
 &+(w^{(3)})^T[p'(z^{(2)}_a)\odot D_\zeta z^{(2)}_a
                                           \odot D_\xi z^{(2)}_a]
 +(w^{(3)})^T[p(z^{(2)}_a)\odot D_\zeta D_\xi z^{(2)}_a]\bigr).
\end{aligned}
\]
The coordinate bound \(M\) and Cauchy–Schwarz bound the third term
by \(MJ_0^2\), without a factor \(\sqrt n\). Consequently
\[
 |D_\zeta D_\xi f_a|\le
       2J_0+MJ_0^2+M(2+A\sqrt n)=:F_{**}(n).
 \tag{46}
\]

At an admissible old node the update direction has raw norm at most
\(K_cF_*\), by (23). Integrating the first prediction differential
along its segment bounds each prediction change by \(\eta K_cF_*^2\).
The residual norm throughout that segment is therefore at most
\(R+\sqrt2\eta K_cF_*^2\), hence at most \(R+1\) once
\(\sqrt2\eta K_cF_*^2\le1\). The identity
\[
 D^2\ell=2\sum_a(Df_a\otimes Df_a+r_aD^2f_a)
\]
and (46) bound the raw Hessian norm there by
\[
 H_*(n)=4F_*^2+2\sqrt2(R+1)F_{**}(n).
 \tag{47}
\]
For \(g_k=\operatorname{grad}_{\rm raw}\ell(w_k)\), the scalar integral
Taylor formula along \(w_k-tg_k\), \(0\le t\le\eta\), now proves
\[
 \ell_{k+1}\le\ell_k-\eta\|g_k\|_{\rm raw}^2
                  +\frac{\eta^2H_*(n)}2\|g_k\|_{\rm raw}^2
       \le\ell_k-\frac\eta2\|g_k\|_{\rm raw}^2
 \tag{48}
\]
provided \(\eta H_*(n)\le1\). Since \(H_*(n)\) is a fixed constant
plus a fixed constant times \(\sqrt n\), these two conditions hold
for all sufficiently large \(n\) with \(\eta=n^{-2}\).
Induction in (48) keeps the candidate exit node at
\(|r_{k+1}|\le R_0<R\), contradicting exit. Hence no exit occurs.

This proves actual GD stability through \(N\), including
\[
 \ell_k\le\ell_0,\qquad
 \frac12\sum_{k=0}^{N-1}\eta
       \left[\frac d n\left\|\frac{w^{(1)}_{k+1}-w^{(1)}_k}{\eta}\right\|_F^2
        +\left\|\frac{w^{(2)}_{k+1}-w^{(2)}_k}{\eta}\right\|_F^2
        +\frac1n\left\|\frac{w^{(3)}_{k+1}-w^{(3)}_k}{\eta}\right\|^2
       \right]\le\ell_0.
 \tag{49}
\]
Node loss decrease is not an exact loss-dissipation identity inside a
raw affine cell.

## 5. Actual GD query regularity and discrete row work

Continue with the constants in (43) and use (29) with those constants.
On each actual raw cell the held update gives
\[
 \|\dot w^{(2)}\|_{\rm op}\le D_A,
 \quad \|\dot w^{(3)}\|_\infty\le D_w,
 \quad \frac{\|\dot z^{(1)}_a\|}{\sqrt n}\le K_c^{\rm G}Q_{\rm G}.
 \tag{50}
\]
For the **recomputed** nonlinear fields, the product rules (30) hold
almost everywhere on each cell. The same calculation proves the genuine
bounds
\[
 \frac{\|q^{(1)}_a(t)\|}{\sqrt n}\le Q_{\rm G},\quad
 \frac{\|\dot z^{(2)}_a(t)\|}{\sqrt n}\le D_Z,\quad
 \frac{\|\dot\delta^{(2)}_a(t)\|}{\sqrt n}\le D_\delta,\quad
 \frac{\|\dot q^{(1)}_a(t)\|}{\sqrt n}\le D_q.
 \tag{51}
\]
The recomputed \(c_a(t)\) satisfies
\(\sum_a|\dot c_a(t)|\le4K_c^{\rm G}F_*^2=:D_c^{\rm G}\), by the
first prediction differential and the raw speed bound used above.
All recomputed fields are continuous across nodes, so integration on
one cell also yields their node increment bounds. Explicitly, the exact
product differences are
\[
\begin{aligned}
 \Delta z^{(2)}_a&=\Delta w^{(2)}h^{(1)}_{k,a}
                                 +w^{(2)}_{k+1}\Delta h^{(1)}_a,\\
 \Delta\delta^{(2)}_a&=\Delta w^{(3)}\odot p(z^{(2)}_{k,a})
             +w^{(3)}_{k+1}\odot[p(z^{(2)}_{k+1,a})-p(z^{(2)}_{k,a})],\\
 \Delta q^{(1)}_a&=(\Delta w^{(2)})^T\delta^{(2)}_{k,a}
                            +(w^{(2)}_{k+1})^T\Delta\delta^{(2)}_a.
\end{aligned}
\tag{52}
\]
They give, respectively, RMS increment bounds \(\eta D_Z\),
\(\eta D_\delta\), \(\eta D_q\), while
\(\sum_a|\Delta c_a|\le\eta D_c^{\rm G}\). The first preactivation
also satisfies
\[
 \frac{\|z^{(1)}_a(t)\|}{\sqrt n}
     \le m^{1/4}+H K_c^{\rm G}Q_{\rm G}.
 \tag{53}
\]
The remaining actual primal bounds are exactly the nondifferential
inequalities (27) with the constants in (43); along segments the residual
is bounded by \(R+1\), and at nodes by \(R_0\).

For the node controlled fields \(u^{(1)}_{k,a,i}=c_{k,a}q^{(1)}_{k,a,i}\),
use
\(\Delta(c_aq^{(1)}_a)=(\Delta c_a)q^{(1)}_{k,a}
                                  +c_{k+1,a}\Delta q^{(1)}_a\).
Both endpoint controls are bounded after (48), so
\[
 \left(\frac1n\sum_i\left(\sum_a
     |u^{(1)}_{k+1,a,i}-u^{(1)}_{k,a,i}|\right)^2\right)^{1/2}
       \le\eta K_u^{\rm G},\qquad
 K_u^{\rm G}=D_c^{\rm G}Q_{\rm G}+K_c^{\rm G}D_q.
 \tag{54}
\]
Define the envelope using precisely the nodes that generate velocities,
\[
 \upsilon_i^{(1)}=\sum_a|u^{(1)}_{0,a,i}|+
      \sum_{k=1}^{N-1}\sum_a|u^{(1)}_{k,a,i}-u^{(1)}_{k-1,a,i}|,
 \qquad V_{\rm G}=K_c^{\rm G}Q_{\rm G}+H K_u^{\rm G}.
 \tag{55}
\]
An empty sum is zero. The triangle inequality proves
\[
 \sum_a|u^{(1)}_{k,a,i}|\le\upsilon_i^{(1)}\quad(0\le k<N),\qquad
 \frac1n\sum_i(\upsilon_i^{(1)})^2\le V_{\rm G}^2,
 \qquad \max_i\upsilon_i^{(1)}\le\sqrt n V_{\rm G}.
 \tag{56}
\]

At node \(k\) put \(e^{(1)}_{k,a,i}=p(z^{(1)}_{k,a,i})u^{(1)}_{k,a,i}\)
and \(a_{k,i}=(e^{(1)}_{k,i})^TCe^{(1)}_{k,i}\). The exact raw update gives
\[
 d\left|\frac{w^{(1)}_{k+1,i}-w^{(1)}_{k,i}}\eta\right|^2=a_{k,i},
 \qquad \Delta z^{(1)}_i=\eta Ce^{(1)}_{k,i},\qquad
 |\Delta z^{(1)}_i|^2\le2\eta^2a_{k,i}.
 \tag{57}
\]
Taylor's integral remainder and \(|\phi''|\le1\) give
\[
 \sum_a u^{(1)}_{k,a,i}\Delta h^{(1)}_{a,i}
       =\eta a_{k,i}+r_{k,i}^{\rm Tay},\qquad
 |r_{k,i}^{\rm Tay}|\le\tfrac12\upsilon_i^{(1)}|\Delta z^{(1)}_i|^2
                          \le\eta^2\upsilon_i^{(1)}a_{k,i}.
 \tag{58}
\]
Increase the deterministic width threshold to ensure
\(\eta\max_i\upsilon_i^{(1)}\le V_{\rm G}n^{-3/2}\le1/2\). This uses (56),
which was proved before the work estimate. Summation by parts says
\[
\begin{aligned}
 \sum_{k=0}^{N-1}\sum_a u^{(1)}_{k,a,i}\Delta h^{(1)}_{a,i}
 ={}&\sum_a[u^{(1)}_{N-1,a,i}h^{(1)}_{N,a,i}
                              -u^{(1)}_{0,a,i}h^{(1)}_{0,a,i}]\\
 &-\sum_{k=1}^{N-1}\sum_a
          (u^{(1)}_{k,a,i}-u^{(1)}_{k-1,a,i})h^{(1)}_{k,a,i}.
\end{aligned}
\]
Its absolute value is at most \(2B\upsilon_i^{(1)}\). Summing (58) and retaining
the error on the left therefore proves
\[
 \mathcal A_i^{\rm G}:=\sum_{k=0}^{N-1}\eta a_{k,i}\le4B\upsilon_i^{(1)}.
 \tag{59}
\]
For clarity, a valid \(n_0(T,\alpha,\beta)\) is any integer such that,
for all \(n\ge n_0\),
\[
 \sqrt2 n^{-2}K_c^{\rm G}F_*^2\le1,\qquad
 n^{-2}H_*(n)\le1,\qquad V_{\rm G}n^{-3/2}\le\tfrac12.
 \tag{60}
\]
All scalar coefficients in these three conditions were explicitly defined
and are independent of \(m,d,\rho,n\); the displayed function \(H_*(n)\)
has the growth stated in (47).
Thus such an integer exists, without any stability assumption.

On the raw interpolation \(v^{(1)}_i=Ce^{(1)}_{k,i}\) on each cell.
Equations (56)–(59) give, also on a partial terminal cell,
\[
 |v^{(1)}_i|\le2\upsilon_i^{(1)},\qquad
 \int_0^T|v^{(1)}_i|^2dt\le8B\upsilon_i^{(1)},\qquad
 \int_0^T|v^{(1)}_i|^3dt\le16B(\upsilon_i^{(1)})^2.
 \tag{61}
\]
Furthermore \(s^{(1)}_i=p(z^{(1)}_i)\odot v^{(1)}_i\), with the
**recomputed** \(z^{(1)}_i\), so \(|s^{(1)}_i|\le|v^{(1)}_i|\).
The displacement is at most \(\sqrt{2H\mathcal A_i^{\rm G}}\).
Consequently the actual GD estimates are
\[
\begin{aligned}
 \frac1n\sum_i\|z^{(1)}_i\|_\infty^4&\le8m+512B^2H^2V_{\rm G}^2,\\
 \frac1n\sum_i\int_0^T|v^{(1)}_i|^3dt&\le16BV_{\rm G}^2,\qquad
 \frac1n\sum_i\int_0^T|s^{(1)}_i|^3dt\le16BV_{\rm G}^2,\\
 \left(\frac1n\sum_i\|v^{(1)}_i\|_2^4\right)^{1/2}&\le8BV_{\rm G}.
\end{aligned}
\tag{62}
\]

## 6. Exact antiparallel identities with the actual readout

At \(\rho=-1\), (1) gives \(|x_1+x_2|^2=0\), so \(x_2=-x_1\).
For **every** raw parameter state, with no restriction on its readout,
successive use of linearity and oddness gives
\[
 z^{(1)}_2=-z^{(1)}_1,\quad h^{(1)}_2=-h^{(1)}_1,\quad
 z^{(2)}_2=-z^{(2)}_1,\quad h^{(2)}_2=-h^{(2)}_1,\quad f_2=-f_1.
 \tag{63}
\]
Since \(p\) is even, (4) then gives
\[
 \delta^{(2)}_2=\delta^{(2)}_1,\qquad q^{(1)}_2=q^{(1)}_1,
 \qquad \delta^{(1)}_2=\delta^{(1)}_1.
 \tag{64}
\]
In particular multiplication by the common, arbitrary \(w^{(3)}\)
preserves the first equality in (64). With the actual opposite labels,
\[
 r_2=-f_1+1=-r_1,\qquad c_2=-c_1.
 \tag{65}
\]
There is no assertion that \(f_1(0)=0\), or that the readout is zero.
Substituting (63)–(65) into the full GF equations gives
\[
 \dot w^{(1)}=\frac{2c_1}{d}\delta^{(1)}_1x_1^T,\qquad
 \dot w^{(2)}=\frac{2c_1}{n}\delta^{(2)}_1(h^{(1)}_1)^T,\qquad
 \dot w^{(3)}=2c_1h^{(2)}_1.
 \tag{66}
\]
For GD the increments are exactly \(\eta\) times these expressions at
the old node. Every new state, and every raw parameter state inside a
cell, again satisfies (63)–(65), because those identities hold for every
parameter choice. Thus this is an exact architecture-enforced relation,
including the actual nonzero Gaussian readout (12).

It follows that \(z^{(1)}_i,h^{(1)}_i,u^{(1)}_i,e^{(1)}_i\) take
values in \(E_-:=\{(b,-b):b\in\mathbb R\}\). For the controlled
fields use instantaneous values in GF and held node values in GD.
The matrix \(C\) acts as multiplication by two on \(E_-\), so
\[
 v^{(1)}_i=2e^{(1)}_i,\qquad e^{(1)}_i=Dv^{(1)}_i,
 \qquad D=C/4,\qquad |e^{(1)}_i|=|v^{(1)}_i|/2.
 \tag{67}
\]
Also \(s^{(1)}_i\in E_-\). In the interior case \(-1<\rho<1\),
\[
 D=C^{-1}=\frac1{1-\rho^2}
          \begin{pmatrix}1&-\rho\\-\rho&1\end{pmatrix},
 \qquad e^{(1)}_i=Dv^{(1)}_i.
 \tag{68}
\]
In either case put
\[
 \kappa_\rho=\|D\|_{\rm op}
       =\begin{cases}(1-|\rho|)^{-1},&-1<\rho<1,\\1/2,&\rho=-1.
         \end{cases}
 \tag{69}
\]
This is finite for each allowed fixed angle. We do not take a limit of
the interior constants as the angle approaches an endpoint.

## 7. Strong velocity translations, uniformly over all GD widths

We now assemble bounds already proved for the actual schemes, with no
new dynamical hypotheses. Choose constants large enough for both schemes:
\[
\begin{aligned}
 K_z&=\max\{\sqrt2K_c^{\rm F}Q_{\rm F},
                          \sqrt2K_c^{\rm G}Q_{\rm G}\},\\
 K_u&=\max\{K_u^{\rm F},K_u^{\rm G}\},\\
 J^3&=\max\{8BV_{\rm F}^2,16BV_{\rm G}^2\},\\
 A_{\rm kin}&=\max\{4BV_{\rm F},8BV_{\rm G}\},\\
 B_{\rm path}&=8m+\max\{128B^2T^2V_{\rm F}^2,
                                      512B^2H^2V_{\rm G}^2\}.
\end{aligned}
\tag{70}
\]
For GF at every time, and GD almost everywhere with its node velocity,
\[
\begin{gathered}
 \|v^{(1)}(t)\|_{n,2}\le K_z,\qquad
 \|v^{(1)}\|_{3;n,[0,T]}\le J,\\
 \left(\frac1n\sum_i\|v^{(1)}_i\|_2^4\right)^{1/2}\le A_{\rm kin},
 \qquad \frac1n\sum_i\|z^{(1)}_i\|_\infty^4\le B_{\rm path}.
\end{gathered}
\tag{71}
\]
The same velocity bounds hold for \(s^{(1)}\), and
\(\|h^{(1)}_i\|_\infty\le\sqrt2 B\). Equations (36),(54) give the
derivative bound \(K_u\) for GF controlled queries and the increment
bound \(\eta K_u\) for GD node controlled queries.

For \(0<\tau<T\), all shifted norms below integrate over
\(I_\tau=[0,T-\tau]\); no extension outside the available trajectory is
made. Put \(\epsilon=0\) for GF and \(\epsilon=\eta\) for GD. In this
section \(u^{(1)}\) means the step field \(\bar u^{(1)}\) in GD, and
let \(z^{(1)}_{\rm gate}\) denote \(z^{(1)}\) in GF and
\(\bar z^{(1)}\) in GD. Integration of the derivative bound in GF, or
summation over at most \(\tau/\eta+1\) crossed node increments in GD,
gives
\[
\begin{aligned}
 \|u^{(1)}(\cdot+\tau)-u^{(1)}\|_{2;n,I_\tau}
                     &\le\sqrt T K_u(\tau+\epsilon),\\
 \|z^{(1)}_{\rm gate}(\cdot+\tau)-z^{(1)}_{\rm gate}\|_{2;n,I_\tau}
                     &\le\sqrt T K_z(\tau+\epsilon),\\
 \|z^{(1)}(\cdot+\tau)-z^{(1)}\|_{2;n,I_\tau}
                     &\le\sqrt T K_z\tau.
\end{aligned}
\tag{72}
\]
For the second GD bound, each first-node difference is \(\eta\) times
the corresponding cell velocity, so its empirical RMS is at most
\(\eta K_z\). The last line integrates the actual affine velocity.

We derive the special arctan gate estimate. The logarithmic derivative
\((\log p)'(x)=-2x/(1+x^2)\) has absolute value at most one. For positive
numbers \(a,b\), division by their geometric mean gives
\(|a-b|/(a+b)=\tanh(|\log a-\log b|/2)\). Since
\(0\le\tanh t\le\min(1,t)\) for \(t\ge0\),
\[
 \theta(x,y):=\frac{|p(x)-p(y)|}{p(x)+p(y)}
                \le\min(1,|x-y|/2).
 \tag{73}
\]
If \(a=p(x)u\), \(b=p(y)v\), then
\[
\begin{aligned}
 |a-b|&\le p(x)|u-v|+\theta(p(x)+p(y))|v|\\
       &\le p(x)(1+\theta)|u-v|+\theta(|a|+|b|)\\
       &\le2|u-v|+\theta(|a|+|b|).
\end{aligned}
\tag{74}
\]
Here the second line uses \(p(x)|v|\le|a|+p(x)|u-v|\). Thus (74)
does not divide by a residual, controlled query, or gate lower bound.
For the two sample coordinates take the maximum of their two \(\theta\)
values and apply the Euclidean triangle inequality. The resulting
two-vector inequality has the same constants.

Apply (74) at \(t,t+\tau\) to
\(e^{(1)}_i=p(z^{(1)}_{{\rm gate},i})\odot u^{(1)}_i\).
By (67)–(71),
\(\|e^{(1)}\|_{3;n,[0,T]}\le\kappa_\rho J\).
The maximum gate ratio \(\theta_i(t)\) lies in \([0,1]\), and (72),(73)
give
\[
 \|\theta\|_{6;n,I_\tau}^6
    \le\|\theta\|_{2;n,I_\tau}^2
    \le\tfrac14TK_z^2(\tau+\epsilon)^2.
\]
Hölder's inequality with \(1/2=1/6+1/3\) therefore proves
\[
 \|e^{(1)}(\cdot+\tau)-e^{(1)}\|_{2;n,I_\tau}
 \le2\sqrt T K_u(\tau+\epsilon)
       +2\kappa_\rho J(TK_z^2/4)^{1/6}(\tau+\epsilon)^{1/3}.
 \tag{75}
\]
Multiplication by \(C\), whose norm is at most two, gives the same
estimate for the velocity with the right side multiplied by two. Since
\(\tau+\epsilon\le T+1\), the linear term can be absorbed into a
constant times the one-third power. There is consequently a finite
constant \(C_0\), depending only on the fixed constants in (70) and on
\(\rho,T\), such that
\[
 \|v^{(1)}(\cdot+\tau)-v^{(1)}\|_{2;n,I_\tau}^2
                                      \le C_0(\tau+\epsilon)^{2/3}.
 \tag{76}
\]

For the **recomputed** activation derivative, the exact difference is
\[
\begin{aligned}
 s^{(1)}(t+\tau)-s^{(1)}(t)
   ={}&p(z^{(1)}(t+\tau))\odot[v^{(1)}(t+\tau)-v^{(1)}(t)]\\
     &+[p(z^{(1)}(t+\tau))-p(z^{(1)}(t))]\odot v^{(1)}(t).
\end{aligned}
\]
The largest coordinate gate difference is at most
\(\min(1,|z^{(1)}_i(t+\tau)-z^{(1)}_i(t)|)\), since \(p\in(0,1]\)
and \(|p'|\le1\). Its sixth norm is at most
\((TK_z^2)^{1/6}\tau^{1/3}\), by (72). Another application of Hölder
proves
\[
 \|s^{(1)}(\cdot+\tau)-s^{(1)}\|_{2;n,I_\tau}
 \le\|v^{(1)}(\cdot+\tau)-v^{(1)}\|_{2;n,I_\tau}
                          +J(TK_z^2)^{1/6}\tau^{1/3}.
 \tag{77}
\]
This calculation preserves the distinction between the node gate in the
GD update and the recomputed gate in the activation derivative.

The \(\eta\) in (76) must be removed uniformly to prove (11) for all
outcomes at every admissible width. The actual GD preactivation velocity
is a step function on cells of length \(\eta\). If \(0<\tau\le\eta\),
its two shifted values differ only on intervals of starting times that
cross an internal node. There are at most \(T/\eta\) such nodes, each
contributing length at most \(\tau\). At every starting time the empirical
squared difference is at most \(4K_z^2\). Hence
\[
 \|v^{(1)}(\cdot+\tau)-v^{(1)}\|_{2;n,I_\tau}^2
                       \le4TK_z^2\tau/\eta\quad(0<\tau\le\eta).
 \tag{78}
\]
For larger shifts the trivial bound is \(4TK_z^2\). Combining both with
(76) gives, for GD, the useful minimum bound
\[
 \|v^{(1)}(\cdot+\tau)-v^{(1)}\|_{2;n,I_\tau}^2
 \le\min\left\{C_0(\tau+\eta)^{2/3},
                    4TK_z^2\min(1,\tau/\eta)\right\}.
 \tag{79}
\]
For \(0<\tau<\min(1,T)\), split at \(\delta=\tau^{3/5}\).
If \(\eta\le\delta\), the first term in (79) is at most
\(C_0(2\tau^{3/5})^{2/3}=2^{2/3}C_0\tau^{2/5}\).
If \(\eta>\delta\), then \(\tau\le\eta\) and the second is at most
\(4TK_z^2\tau^{2/5}\). Therefore a fixed constant \(C_1\) gives
\[
 \|v^{(1)}(\cdot+\tau)-v^{(1)}\|_{2;n,I_\tau}^2
 +\|s^{(1)}(\cdot+\tau)-s^{(1)}\|_{2;n,I_\tau}^2
                         \le C_1\tau^{2/5}.
 \tag{80}
\]
For GF, (76) has \(\epsilon=0\), and implies this weaker exponent too.
Equation (77) supplies the activation term because
\(\tau^{2/3}\le\tau^{2/5}\) when \(\tau\le1\).
Thus (80) is uniform over every outcome satisfying (10), every GF width,
and every GD width \(n\ge n_0\). The exponent \(2/5\) bounds the
**squared** space-time \(L^2\) shift norm. No optimal exponent is claimed.

## 8. Elementary strong joint compactness and tightness

Use a uniform partition of \([0,T]\) into \(m_0\) cells of length
\(h=T/m_0<\min(1,T)\). Let \(P_h\) take a velocity to its average on
each cell, and let \(\Pi_h\) take a continuous position to the polygon
through its partition-node values. Define the bounded finite-rank map
\[
 \mathcal Q_h(z,v,h_1,s)=(\Pi_h z,P_hv,\Pi_h h_1,P_hs).
 \tag{81}
\]
Here \(h_1\) denotes the activation argument of the map, not the mesh.
For a cell \(I\) of length \(h\), expansion of the square gives exactly
\[
 \int_I\left|v(t)-\frac1h\int_Iv\right|^2dt
      =\frac1{2h}\int_I\int_I|v(t)-v(s)|^2dsdt.
\]
Split the double integral into ordered pairs, set \(\tau=|t-s|\), and
enlarge within-cell pairs to all pairs at separation \(\tau<h\). Averaging
over neurons and using (80) proves
\[
 \frac1n\sum_i\left(\|v^{(1)}_i-P_hv^{(1)}_i\|_2^2
                    +\|s^{(1)}_i-P_hs^{(1)}_i\|_2^2\right)
       \le\frac{C_1}{h}\int_0^h\tau^{2/5}d\tau
       =\frac{5C_1}{7}h^{2/5}.
 \tag{82}
\]
On a cell \([a,b]\) and for \(t\in[a,b]\), absolute continuity gives
\[
 z(t)-\Pi_hz(t)=\int_a^t v(u)du
                    -\frac{t-a}{h}\int_a^b v(u)du.
\]
Each integral term is bounded by \(\sqrt h\|v\|_{L^2([a,b])}\).
Consequently
\[
 \frac1n\sum_i\|z^{(1)}_i-\Pi_hz^{(1)}_i\|_\infty^2
            \le4h\frac1n\sum_i\|v^{(1)}_i\|_2^2\le4hTK_z^2.
 \tag{83}
\]
The identical estimate for \(h^{(1)}_i\) uses its derivative
\(s^{(1)}_i\), whose squared norm is no larger. Couple each atom to its
own projection. Equations (82),(83) yield the uniform bound
\[
 W_2(\mu_n,\mathcal Q_{h\#}\mu_n)^2
       \le8hTK_z^2+\frac{5C_1}{7}h^{2/5}=:\varepsilon(h),
       \qquad \varepsilon(h)\longrightarrow0.
 \tag{84}
\]
Every coordinate and both samples stay in the same neuron tuple in this
coupling.

The complete tuple has a uniform fourth moment. Indeed, by (71),
\[
 \int\|\xi\|_{\mathcal E_T}^4d\mu_n(\xi)
 \le4\left(B_{\rm path}+2A_{\rm kin}^2+4B^4\right)=:M_4.
 \tag{85}
\]
We used \((a+b+c+d)^2\le4(a^2+b^2+c^2+d^2)\) on the four squared
coordinate norms. Time averaging contracts the \(L^2\) norm by
Cauchy–Schwarz, and polygonal interpolation contracts the supremum norm
by convexity. Thus the projected laws satisfy the same fourth-moment bound.

Here is a finite-cover proof that requires no probability-measure
compactness theorem. For a fixed mesh the range of \(\mathcal Q_h\) is
finite dimensional. Move its mass outside a norm ball of radius \(R\) to
zero. By (85) the squared transport cost is at most \(M_4/R^2\).
The remaining finite-dimensional ball has a finite cover by sets of
diameter at most \(\delta\): choosing a basis, equivalence of its norm
with a Euclidean norm follows by taking the minimum and maximum of that
norm on the Euclidean unit sphere, and a finite rectangular grid then
supplies the cover. Move each cell's mass to a representative at cost
at most \(\delta^2\). The resulting law is supported on a fixed finite
set. Its mass vectors lie in a bounded closed simplex. Approximating
their coordinates by a finite grid gives finitely many approximating
mass vectors. If two mass vectors differ by total unmatched mass \(a\),
couple common masses identically and distribute the remainder; the squared
cost is at most \(a\) times the squared diameter of the finite set.
This proves total boundedness of the projected laws in \(W_2\).
Together with (84), it proves total boundedness of the union of **all**
the original GF and admissible GD laws. It does not discard the possible
outcomes at any fixed admissible width.

We give the needed existence of subsequential measure limits explicitly.
From any sequence in this totally bounded union, nested finite covers
select a Cauchy subsequence of the finite empirical measures. Select a
further subsequence \(\nu_j\) with
\(W_2(\nu_j,\nu_{j+1})<2^{-j-1}\). By the definition of the infimum,
choose finite transport tables with root-mean-square costs at most
\(2^{-j}\). Glue adjacent tables by dividing each row by its marginal
mass to form transition probabilities, ignoring rows of zero mass. This
construction needs only finite probabilities: split \([0,1]\) first
according to the masses of \(\nu_1\), and recursively split each interval
according to the appropriate next transition. A uniform point in
\([0,1]\) then defines random points \(\xi_j\) with the required
successive joint tables and marginal laws \(\nu_j\).
They satisfy
\[
 \sum_j\left(\mathbb E\|\xi_{j+1}-\xi_j\|_{\mathcal E_T}^2\right)^{1/2}
                                      \le\sum_j2^{-j}<\infty.
 \tag{86}
\]
The expected sum of their distances is finite by Cauchy–Schwarz, so this
sum is finite almost surely. The space \(\mathcal E_T\) is complete:
uniform Cauchy sequences of continuous functions have continuous uniform
limits, and a summable-increment subsequence of an \(L^2\)-Cauchy sequence
has an almost-everywhere sum with an \(L^2\) tail bounded by the sum of
the increment norms. These facts also prove completeness of the finite
product norm in (9). Thus \(\xi_j\) has a measurable limit \(\xi\);
the space is separable, as rational polygonal paths and rational step
functions are dense in its two types of coordinates. By the triangle
inequality in \(L^2\), or its finite version followed by the nonnegative
integral limit inequality,
\[
 \left(\mathbb E\|\xi_j-\xi\|_{\mathcal E_T}^2\right)^{1/2}
       \le\sum_{k\ge j}2^{-k}\longrightarrow0.
\]
The limit has finite second moment and its law is the required \(W_2\)
limit. Coupling triangle inequalities used here can themselves be checked
by the same finite-table gluing and the \(L^2\) triangle inequality.

It follows that the closure of our union in \(\mathcal P_2(\mathcal E_T)\)
is compact: a sequence of points in the closure can first be approximated
within \(1/j\) by points of the union, to which the preceding subsequence
argument applies. To verify compactness in the open-cover sense, fix an
open cover of this closure. If no positive radius worked uniformly so
that each relative ball of that radius lay in some member of the cover,
there would be points whose relative radius-\(1/j\) balls lay in no member.
A convergent subsequence of these points has a limit in an open member;
eventually those small balls lie in that member, a contradiction. A finite
net, available by total boundedness, at half the resulting uniform radius
then gives a finite subcover. This proves (11).

One can also exhibit tightness directly on the path space. Fix a desired
mass error \(a>0\), choose meshes \(h_j\) so small that
\(\varepsilon(h_j)\le a2^{-3j-1}\), and choose \(R\) with
\(M_4/R^4\le a/2\). The closed subset
\[
 \mathcal C=\{\xi:\|\xi\|_{\mathcal E_T}\le R,
          \ \|\xi-\mathcal Q_{h_j}\xi\|_{\mathcal E_T}\le2^{-j}
                         \text{ for every }j\ge1\}
\]
is totally bounded because, for every \(j\), its points are within
\(2^{-j}\) of a bounded subset of a finite-dimensional range. Completeness
makes \(\mathcal C\) compact. Markov's inequality and the union bound give
\[
 \mu_n(\mathcal C^c)\le M_4/R^4+
          \sum_{j\ge1}2^{2j}\varepsilon(h_j)\le a.
\]
This is uniform tightness of the same-neuron tuple laws themselves.
Together with (85) it also explicitly controls their quadratic tails.

For \(T=0\), both velocity spaces are zero spaces and the laws reduce
to the initial pair and its arctan. The fourth-moment bound and the same
finite-dimensional covering argument prove the theorem; all action and
kernel assertions are identities in the zero time-integral space.

## 9. Gaussian good events and probability quantifiers

Under (12), different first rows give independent Gaussian pairs with
covariance \(C\). Write one such pair as
\((G,\rho G+\sqrt{1-\rho^2}G')\) for independent standard normals
\(G,G'\); this formula remains valid at \(\rho=-1\).
Gaussian integration by parts gives
\(\mathbb E G^{2k}=(2k-1)\mathbb E G^{2k-2}\), starting from one:
differentiate \(e^{-x^2/2}\), integrate \(x^{2k-1}\) against its
derivative, and use its vanishing boundary terms. Thus
\(\mathbb E G^4=3\), \(\mathbb E G^8=105\). Expanding the above
representation gives
\(\mathbb E[G^2(\rho G+\sqrt{1-\rho^2}G')^2]=1+2\rho^2\).
Therefore
\[
 \mathbb E|z^{(1)}_i(0)|^4=8+4\rho^2\le12,\qquad
 \mathbb E|z^{(1)}_i(0)|^8
       \le8\mathbb E(|z^{(1)}_{1,i}(0)|^8+|z^{(1)}_{2,i}(0)|^8)
       =1680.
 \tag{87}
\]
Independence across rows bounds the variance of the empirical fourth
moment by \(1680/n\). For completeness, the inequality
\(\mathbb P(|Y-\mathbb EY|\ge t)\le\mathbb E|Y-\mathbb EY|^2/t^2\)
follows by integrating \(|Y-\mathbb EY|^2\ge t^2\) on that event.
Applying it with \(t=1\) proves
\[
 \mathbb P\left\{\frac1n\sum_i|z^{(1)}_i(0)|^4>13\right\}
                                                    \le1680/n.
 \tag{88}
\]

For the middle matrix, take a maximal \(1/4\)-separated subset of the
unit sphere in \(\mathbb R^n\). The disjoint radius-\(1/8\) balls
around its points lie inside a radius-\(9/8\) ball, so comparison of
Euclidean volumes gives at most \(9^n\) points. Maximality makes it a
\(1/4\)-net. Approximating both unit test vectors by net points yields
\[
 \|w^{(2)}_0\|_{\rm op}
       \le2\max_{u,v\text{ in the net}}|u^Tw^{(2)}_0v|:
\]
each of the two replacement errors is at most
\(\|w^{(2)}_0\|_{\rm op}/4\). For each fixed \(u,v\) the scalar is
Gaussian of variance \(1/n\), since its variance is
\(n^{-1}\sum_{i,j}u_i^2v_j^2=1/n\). A centered Gaussian of variance
\(\sigma^2\) has moment generating function
\(e^{\lambda^2\sigma^2/2}\), as follows by completing the square in
its density. Exponential Markov inequality, optimized at
\(\lambda=t/\sigma^2\), bounds its two-sided tail by
\(2e^{-t^2/(2\sigma^2)}\). At threshold four, a union bound over the
two nets therefore gives
\[
 \mathbb P\{\|w^{(2)}_0\|_{\rm op}>8\}
                          \le2e^{-(8-2\log9)n}.
 \tag{89}
\]
The same scalar estimate at threshold one and variance \(n^{-2}\),
followed by a union bound over the readout coordinates, gives
\[
 \mathbb P\{\|w^{(3)}_0\|_\infty>1\}\le2ne^{-n^2/2}.
 \tag{90}
\]
No independence between the three events is needed to add (88)–(90).
This proves (13). Take \((\alpha,\beta,m)=(8,1,13)\) in the deterministic
construction (11). Every point of \(E_n\) belongs to its hypotheses,
for both schemes at the same initialization, proving (14) and the stated
joint probability bounds.

The random empirical laws used in (14) are measurable. At fixed width,
GD is a finite composition of continuous maps of its initial parameters;
the partition is fixed, so positions and their \(L^2\) velocities depend
continuously on those parameters. For GF, on a bounded neighborhood of a
given initial point, (25) bounds the finite-dimensional solutions through
\(T\) in a common ball. The smooth vector field is Lipschitz there.
Iteration of the difference-integral inequality bounds the difference
of solutions by their initial difference times
\(\sum_{k\ge0}(LT)^k/k!=e^{LT}\); evaluating the vector field also
bounds their velocity difference. Thus its paths and velocities depend
continuously on the initial point. Pairing equal finite neuron indices
turns these statements into continuity of \(\mu_n\) in \(W_2\).

To make the empirical integrability statement precise, define
\[
 F_n(R)=\int\|\xi\|_{\mathcal E_T}^2
                       \mathbf1_{\{\|\xi\|_{\mathcal E_T}>R\}}d\mu_n(\xi),
 \qquad
 L_n(R)=\frac1n\sum_i\int_0^T|v^{(1)}_i(t)|^2
                                  \mathbf1_{\{|v^{(1)}_i(t)|>R\}}dt.
\]
On \(E_n\), (85) and the cubic bound give
\(F_n(R)\le M_4/R^2\), \(L_n(R)\le J^3/R\), respectively; the latter
holds for \(s^{(1)}\) as well. Hence for each \(a>0\),
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}\mathbb P\{F_n(R)>a\}=0,
 \qquad
 \lim_{R\to\infty}\limsup_{n\to\infty}\mathbb P\{L_n(R)>a\}=0.
 \tag{91}
\]
One quantity truncates the norm of a whole tuple, the other a velocity
value under empirical space-time measure. Neither estimates a tail
expectation on \(E_n^c\).

The bound (13) is uniform over deterministic normalized input pairs and
dimensions. Compact containment is stated for a fixed \(\rho\); its
constant is not uniform for varying correlations near an endpoint.
An event controlling every adaptively chosen input pair in a single
realization is not asserted. Nor does (13), whose leading term is not
summable over all widths, assert eventual goodness almost surely along
the whole width sequence.

## 10. Population compatibility and raw first-row reconstruction

Fix any deterministic subsequence for which \(\mu_n\to\mu\) in
\(W_2(\mathcal E_T)\). All assertions in this and the next section are
along that subsequence. Choose couplings between \(\mu_n\) and \(\mu\)
with squared expected distance \(\varepsilon_n^2\to0\); near-minimizers
of the defining infimum suffice. In those couplings use lowercase
\((z^{(1)}_n,v^{(1)}_n,h^{(1)}_n,s^{(1)}_n)\) for the finite random atom
and capitals for the population coordinate. This is an auxiliary neuron
coupling, not a matching of original neuron indices across widths and
not external initialization randomness.

The integral defect map
\(z(t)-z(0)-\int_0^t v(u)du\) is continuous from \(C\times L^2\)
to \(C\), because its difference is bounded in the uniform norm by
\(2\|z-z'\|_\infty+\sqrt T\|v-v'\|_2\).
Also \(z\mapsto\phi(z)\) is continuous in the uniform norm. Finally,
if \(z_j\to z\) uniformly and \(v_j\to v\) in \(L^2\), then
\[
 \|p(z_j)\odot v_j-p(z)\odot v\|_2
     \le\|v_j-v\|_2+\|p(z_j)-p(z)\|_\infty\|v\|_2\longrightarrow0.
 \tag{92}
\]
Thus the set of tuples obeying all of (15) is closed. Every empirical
atom belongs to it. To see directly that the limit does too, integrate
the bounded continuous function \(\min(1,\operatorname{dist}(\xi,\mathcal S))\)
for this closed set \(\mathcal S\). Its integral under the population
marginal is at most the expected coupled distance, hence at most
\(\varepsilon_n\), and is therefore zero. This proves (15).
The same argument preserves at \(\rho=-1\) the closed constraints
that continuous positions take values in \(E_-\) at every time and
velocity classes take values there almost everywhere.

For each finite row, (39) holds in GF and (57) gives its GD cell version.
With the held node \(e^{(1)}\) in GD, (67),(68) therefore prove
\[
 e^{(1)}_i=Dv^{(1)}_i,\qquad
 \dot w^{(1)}_i=A_{\rm row}v^{(1)}_i,\qquad
 d|\dot w^{(1)}_i|^2=(v^{(1)}_i)^TDv^{(1)}_i.
 \tag{93}
\]
Indeed \(DCD=D\) in both cases, so
\[
 A_{\rm row}^TA_{\rm row}=DCD/d=D/d,\qquad
 \|A_{\rm row}\|_{\rm op}^2=\kappa_\rho/d.
 \tag{94}
\]
At the antiparallel endpoint, write \(e^{(1)}_i=(b,-b)\). Then
\(v^{(1)}_i=(2b,-2b)\),
\(\dot w^{(1)}_i=2bx_1/d\), and
\[
 d|\dot w^{(1)}_i|^2=4b^2
                 =|v^{(1)}_i|^2/2=(v^{(1)}_i)^TDv^{(1)}_i.
 \tag{95}
\]
This is one actual row energy; there is no second row energy to add.
The exact invariance in Section 6 is essential for reconstructing
\(e^{(1)}\) at this endpoint. Without it a component in the nullspace
of \(C\) would be invisible to \(v^{(1)}\) but could change individual
controlled kernel entries.

Integrating (93) and using (8) proves
\[
 w^{(1)}_i(t)-w^{(1)}_i(0)
       =A_{\rm row}[z^{(1)}_i(t)-z^{(1)}_i(0)].
 \tag{96}
\]
The map from \((z,v,h,s)\) to the two right-hand sides of (96),(93)
is Lipschitz into \(C([0,T];\mathbb R^d)\times L^2([0,T];\mathbb R^d)\),
with squared Lipschitz constant at most \(4\|A_{\rm row}\|_{\rm op}^2\).
Push the chosen couplings through that map to get squared costs at most
\(4\|A_{\rm row}\|_{\rm op}^2\varepsilon_n^2\to0\). Keeping the original
tuple as extra coordinates adds just its original cost. This proves (17),
including joint convergence, with every \(n,d\) factor explicit.

This reconstructs increments and velocities. To see exactly why it does
not reconstruct full rows, put \(P=XD X^T/d\). Symmetry and \(DCD=D\)
give \(P^2=P\). Its range is the span of the inputs: in the interior
case \(PX=X\), and at \(\rho=-1\) the same equality follows by checking
the two opposite columns. Thus \(P\) is their orthogonal projection and
\[
 w^{(1)}_i(t)=A_{\rm row}z^{(1)}_i(t)+(I-P)w^{(1)}_i(0).
 \tag{97}
\]
The second term is constant and is not encoded by the two evaluations.
Including full-row laws would require joint information about that
initial orthogonal component. No such enlargement is part of this theorem.

## 11. No kinetic defect and every node-controlled kernel entry

We first explain the meaning of timewise population formulas without
using point evaluation on \(L^2\). For an \(L^2\) path, successive
uniform time averages converge in \(L^2\). To verify this, step functions
on finitely many intervals are dense: approximate a measurable function
first by bounded simple functions and approximate their measurable sets
in measure by finite unions of intervals; the squared error is controlled
by the set errors and bounded coefficients. Time averages contract
\(L^2\), and on each fixed interval-step function their error is supported
on shrinking neighborhoods of its finitely many endpoints. Density then
gives the claim for every \(L^2\) path. The averaged paths are jointly
measurable in the path and time, since each averaging coefficient is a
bounded linear functional of the path. Their convergence holds in
\(L^2(\mu\times dt)\) as well: their squared error tends pointwise in
the path variable to zero and is bounded by \(4\|V^{(1)}\|_2^2\), which
is integrable. Truncating this integrable majorant and using bounded
convergence justifies that passage.

A subsequence with summable \(L^2(\mu\times dt)\) increments gives a
jointly measurable representative of \(V^{(1)}\); for \(\mu\)-almost
every path its section equals that path as an \(L^2\) class. In
particular
\[
 \int_0^T\mathbb E_\mu|V^{(1)}(t)|^2dt
                         =\mathbb E_\mu\|V^{(1)}\|_2^2<\infty.
 \tag{98}
\]
The same holds for \(S^{(1)}\). Products of these representatives
define the \(L^1\) functions below. A change of representatives changes
none of them as \(L^1\) classes. Nonnegative integration and then the
absolute-integrability bound justify exchanging the time and neuron
integrals. No assertion is made about a chosen single time evaluation of
an arbitrary \(L^2\) element.

In the coupling of Section 10 put
\[
 M_n=\left(\mathbb E\|v^{(1)}_n\|_2^2\right)^{1/2},\qquad
 M=\left(\mathbb E_\mu\|V^{(1)}\|_2^2\right)^{1/2}.
\]
The \(L^2\) triangle inequality gives \(|M_n-M|\le\varepsilon_n\),
so the sum \(M_n+M\) stays bounded. Expansion of a difference of squared
norms and Cauchy–Schwarz in time and coupling give
\[
 \left\|\mathbb E|v^{(1)}_n(\cdot)|^2
                    -\mathbb E_\mu|V^{(1)}(\cdot)|^2\right\|_{L^1}
                \le\varepsilon_n(M_n+M)\longrightarrow0.
 \tag{99}
\]
The identical argument for the fourth coordinate gives the second line
of (18). For the raw row form, for any two vectors \(v,w\),
\[
 |v^TDv-w^TDw|\le\|D\|_{\rm op}|v-w|(|v|+|w|).
\]
By (93) and the same coupling estimate,
\[
 \|g_n^{(1)}-G^{(1)}\|_{L^1}
        \le\kappa_\rho\varepsilon_n(M_n+M)\longrightarrow0.
 \tag{100}
\]
This proves all of (18). For a measurable \(A\subset[0,T]\), the
difference of integrals over \(A\) is bounded by the corresponding
\(L^1\) error. In particular the precise raw first-matrix action limit is
\[
 \lim_n\frac d n\int_A\|\dot w^{(1)}_n(t)\|_F^2dt
       =\int_A\mathbb E_\mu[(V^{(1)}(t))^TDV^{(1)}(t)]dt.
 \tag{101}
\]
The ordinary unnormalized matrix speed is \(n/d\) times \(g_n^{(1)}\).
There is no hidden normalized Frobenius norm in this formula.

For the kernel, controls are common to all neurons for each sample, so
they can be placed inside the finite sum in (19). With the node
convention in GD, (93) gives the exact identity
\[
 j^{(1)}_{n,ab}=C_{ab}\frac1n\sum_i
              e^{(1)}_{n,a,i}e^{(1)}_{n,b,i}
             =C_{ab}\frac1n\sum_i
              (Dv^{(1)}_{n,i})_a(Dv^{(1)}_{n,i})_b.
 \tag{102}
\]
Define on \(L^2([0,T];\mathbb R^2)\) the matrix-valued \(L^1\) map
\[
 \mathcal H(v)(t)=C\odot[(Dv(t))(Dv(t))^T].
 \tag{103}
\]
For vectors \(e,f\),
\(ee^T-ff^T=(e-f)e^T+f(e-f)^T\), so
\(\|ee^T-ff^T\|_F\le|e-f|(|e|+|f|)\).
Entrywise multiplication by \(C\) does not increase the Frobenius norm,
because every \(|C_{ab}|\le1\). Integrating in time therefore proves
\[
\begin{aligned}
 \|\mathcal H(v)-\mathcal H(w)\|_{L^1(F)}
      &\le\kappa_\rho^2\|v-w\|_2(\|v\|_2+\|w\|_2),\\
 \|\mathcal H(v)\|_{L^1(F)}&\le\kappa_\rho^2\|v\|_2^2.
\end{aligned}
\tag{104}
\]
Here \(\|A\|_{L^1(F)}=\int_0^T\|A(t)\|_Fdt\). Equation (98) and
the second inequality make \(J^{(1)}=\mathbb E_\mu\mathcal H(V^{(1)})\)
well-defined entrywise as an \(L^1\) function, with the representative
formula (20). Taking its difference from (102) inside the coupling and
using (104) gives the full-matrix estimate
\[
 \|j_n^{(1)}-J^{(1)}\|_{L^1(F)}
       \le\kappa_\rho^2\varepsilon_n(M_n+M)\longrightarrow0.
 \tag{105}
\]
This controls all four entries simultaneously, including the off-diagonal
ones, without requiring convergence of the controls or of unweighted
reverse fields separately.

Finally
\[
 \sum_{a,b}\mathcal H(v)_{ab}
       =(Dv)^TC(Dv)=v^TDCDv=v^TDv,
\]
which proves (21). As a useful endpoint check, at \(\rho=-1\) a row
with \(e^{(1)}=(b,-b)\) contributes
\(b^2\begin{pmatrix}1&1\\1&1\end{pmatrix}\) to the controlled matrix.
The sum of its four entries is \(4b^2\), exactly (95).
For every angle the controlled matrix is positive semidefinite, since
\(a^T\mathcal H(v)a=(a\odot Dv)^TC(a\odot Dv)\ge0\);
this statement also holds for an almost-everywhere representative of
its expectation. Neither positivity nor its trace replaces the
full-entry identity and convergence proof above.

These identities concern the raw speed. In GF the first speed contributes
to the exact dissipation (24). In a GD cell, if
\(g_k=\operatorname{grad}_{\rm raw}\ell(w_k)\), the actual loss derivative
is instead
\[
 \frac d{dt}\ell(w(t))
        =-\langle\operatorname{grad}_{\rm raw}\ell(w(t)),g_k\rangle_{\rm raw}.
 \tag{106}
\]
It need not equal \(-\|g_k\|_{\rm raw}^2\). Equations (102),(105)
refer to held node deltas and controls, not to a kernel recomputed from
the nonlinear fields inside the raw interpolation.

The corresponding observables also have deterministic compact containment.
Indeed the maps taking a law to its raw increment/velocity pushforward,
its three speed densities, and its full controlled matrix are continuous
in \(W_2\), by the coupling bounds in (94),(99),(100),(105). Take the
joint image of the compact set (11) under these maps, retaining the
original law as another coordinate. Any sequence of image points has
preimages with a convergent subsequence, whose images converge by these
bounds. The image is therefore compact in the product of the two
\(W_2\) spaces, three scalar \(L^1\) spaces, and matrix-valued \(L^1\).
It contains all the actual good-outcome observables, so their joint
failure probability has the same bound (13). This conclusion supplies
controlled-kernel compactness without requiring convergence of residuals
or of the unweighted kernel as separate objects.

## 12. Exact scope of the result

The compact set (11) contains all good deterministic outcomes, not just
one trajectory per width. Therefore any sequence of such outcomes at
widths tending to infinity, with either scheme or with both schemes
interleaved, has a \(W_2\)-convergent subsequence. Along **any** actual
\(W_2\)-convergent subsequence, (15)–(21) hold for its own limiting law.
For the original random laws, (14) is compact containment in probability.
It is not convergence in probability to an identified law. Even when a
deterministic selection has a deterministic measure limit, that measure
may be non-Dirac and may depend on the chosen sequence; the expectation
over it does not identify a deterministic mean-field evolution.

In particular the theorem makes none of the following stronger claims:

- A deterministic identified mean-field limit, uniqueness of a population
  equation, convergence of the full width sequence, or equality of GF and
  GD subsequential limits.
- An all-layer limit, second-layer strong kinetic compactness, a limit
  law for reused forward and transpose Gaussian queries along the whole
  trajectory, or unrestricted higher-moment matrix-action bounds.
- Reconstruction of the unweighted first kernel when a control vanishes.
  The proof reconstructs \(e^{(1)}=c\odot\delta^{(1)}\) and never divides
  by \(c_a\). Vanishing \(c_a\) can erase information about
  \(\delta^{(1)}_a\). Even division on a nonvanishing region would need
  additional reciprocal-control and convergence assumptions.
- Equality, or asymptotic equality, of the node-controlled GD kernel
  and a kernel recomputed inside its raw affine cells.
- Almost-everywhere time convergence of the entire kernel sequence.
  The conclusion is \(L^1\) convergence with an almost-everywhere formula
  for its limit. A further subsequence can have almost-everywhere
  convergence: choose its \(L^1\) errors summable; the integrated sum of
  pointwise errors is then finite, hence those errors tend to zero almost
  everywhere. No such implication is claimed for the original sequence.
- Bounds on expectations over external initialization randomness on bad
  events, expectation-level uniform integrability, or convergence of
  expected kinetic energies over that randomness. The probability bounds
  (13),(14),(91) do not supply those assertions.

There is also no result here at \(\rho=1\), no assertion uniform in a
varying sequence of correlations approaching an endpoint, no matching of
neuron identities across widths, and no whole-row reconstruction without
the initial orthogonal component in (97). None of these additional
conclusions is needed for the actual all-angle, fixed-input, first-layer
compactness proved above.

## Appendix. Permitted-source provenance

The following six mathematical dependencies were read in full. The five
supplied hashes were checked and matched; the sixth hash records the
version read. This table records provenance only. No theorem or lemma
in the proof above is invoked from these files: the finite dynamics,
moment estimates, antiparallel supplement, uniform-in-step translation
supplement, elementary compactness arguments, and controlled-observable
arguments have all been supplied within this document.

All files are in `/tmp/l2-two-sample-proof-0ywjpp/`.

| Permitted dependency | SHA-256 |
|---|---|
| `ALL_ANGLE_FIRST_LAYER_ACTION.md` | `9c0349c8aa76a6d7b260c34fd45a9e1d5dd8caf637a5ecbee0b16028bbd72ac9` |
| `ALL_ANGLE_RAW_GD_ACTION.md` | `95dd9f24b44245737bfd3cdcf4692383c24cacae84290d100deb2c21140a08e2` |
| `ALL_ANGLE_FIRST_VELOCITY_COMPACTNESS.md` | `a78c7439023d51e19e17b57e0105521a81fb09ccfc1920b32e97f376fdf6d742` |
| `ALL_ANGLE_FIRST_COMPACTNESS_INTEGRATION_REVIEW.md` | `6594f13797fb5b85982fbb499410ee19e010ec7c9efb333b10b0a124abc00ba1` |
| `FIRST_RAW_METRIC_AND_CONTROLLED_KERNEL_COMPACTNESS.md` | `372110271ecdbd8df79dabaca56114014ecdd25732e599222b0b82797aa58d06` |
| `FIRST_RAW_METRIC_CONTROLLED_KERNEL_REVIEW_ROUND2.md` | `742f17e4739590acd672f0317658048ce4fc364e5cf18603d4c7212e599b24b1` |

No history, master document, other-agent material, experiment, external
mathematical source, or additional mathematical dependency was used.
The source files were not edited. This document is a proof assembly,
not a claim that the assembled document has received an independent audit.
