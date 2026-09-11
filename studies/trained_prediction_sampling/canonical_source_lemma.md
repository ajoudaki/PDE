# Source calculus for trained prediction — draft awaiting checks

## Uniform first and second derivatives of the population Euler output

Fix \(Y\ge1\), \(T=40\), and the two-hidden-layer tanh model, initialization,
loss normalization and Gaussian action spaces of C.4.7. Choose a fixed smaller
law ball whose closure is contained in the neighborhood of C.4.7.N-cap.
All constants below may depend on this choice, \(Y,T\), and a separately
specified source-derivative or moment order. They do not depend on the number
of atoms, their minimum positive mass, covariance rank, or the number of
Euler steps. Only finitely many low-order moment constants will determine
the step threshold in the conclusion.

Let
\[
 \lambda=\sum_{a=1}^N p_a\delta_{(\sqrt2u_a,y_a)},\qquad
 p_a>0,\quad\sum_ap_a=1,\quad |u_a|=1,\quad |y_a|\le Y,
\]
and let \(f_h(\lambda;t,u)\) denote the prediction of its population raw
Euler program, using its actual population residuals, through time
\(t\le T\). The program may end in a shorter final step. A mass direction
\(\sigma=(s_a)_{a=1}^N\) has \(\sum_as_a=0\) and norm
\(\|\sigma\|_{\rm TV}=\sum_a|s_a|\). Inputs and labels remain fixed when
taking these derivatives. A second direction is denoted \(\tau=(v_a)\).

**Lemma.** There are \(h_*>0\) and \(C<\infty\) such that every program in
this ball with maximum step at most \(h_*\) satisfies
\[
 \sup_{t\le T,\,u\in S^1}
       |\partial_\sigma f_h(\lambda;t,u)|
       \le C\|\sigma\|_{\rm TV},
 \qquad
 \sup_{t\le T,\,u\in S^1}
       |\partial_\sigma\partial_\tau f_h(\lambda;t,u)|
       \le C\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.             \tag{S1}
\]
On positive masses these are ordinary derivatives on the relative open
probability simplex intersected with the law ball. They extend continuously
to one-sided derivatives on admissible finite-law segments and rectangles
at zero masses. No nonsingularity of a Gaussian covariance is required.
The same bounds hold for the prediction in \(L^2(S^1)\) with normalized
circle measure.

The proof retains both Gaussian source orientations and the response
corrections representing the actual initialized action and its adjoint.
It first bounds source derivatives with deterministic coefficients frozen,
then differentiates the full coefficient and covariance recursions. Short
time intervals supply an absorbable factor for the latter derivatives.

### 1. Exact finite source recursion and its uniform bounds

Write \(\phi=\tanh\), \(A=A_0+K\), with \(A_0:H_1\to H_2\) and its actual
Hilbert adjoint on the canonical spaces of III.F. The initial state is
\((w_0,K_0,c_0)=(g,0,0)\), with \(g\sim N(0,I_2)\). Only \(K\) is
Hilbert–Schmidt. At a time node \(k\), abbreviate the fields by
\[
 H_{ku}=\phi(w_k\cdot u),\quad Z_{ku}=A_kH_{ku},\quad
 \Delta_{ku}=c_k\phi'(Z_{ku}),\quad Q_{ku}=A_k^*\Delta_{ku},
 \quad f_{ku}=\mathbb E_2[c_k\phi(Z_{ku})],
\]
and put \(r_{ka}=f_{ku_a}-y_a\). For a step \(h_k>0\), set
\(m_{ka}=h_kp_a\) and \(\gamma_{ka}=-2m_{ka}r_{ka}\). The exact Euler updates
are
\[
 \begin{aligned}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}\phi'(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\Delta_{ka}\otimes H_{ka}.
 \end{aligned}                                                   \tag{S2}
\]
Here \(a\otimes b\) acts as \(v\mapsto a\mathbb E_1[bv]\).

A source slot is \(i=(k,a)\), or one distinguished current slot \(i=(k,u)\)
for an appended passive query. The notation \(q<i\) means that the time
index of \(q\) is strictly smaller than \(k\). A sum \(q\le i\) includes
the old training slots and the distinguished current slot; other current
slots have zero response coefficient for this output. Earlier unused
passive slots also have coefficient zero. Let \(\xi_i\) be the centered
forward Gaussian source on population 2 and \(\zeta_i\) the centered reverse
Gaussian source on population 1. Their source covariances are
\[
 (C_\xi)_{ij}=\mathbb E_1[H_iH_j],\qquad
 (C_\zeta)_{ij}=\mathbb E_2[\Delta_i\Delta_j].                  \tag{S3}
\]
The two orientation families are independent; the lower root \(g\) has its
fixed independent Gaussian law. These are the source families of the
retained action construction in III.F and C.4.7, not independent replacements
for \(A_0\) and \(A_0^*\).

The coordinate derivatives in the next display freeze all residuals,
contractions, covariance laws and deterministic coefficients. On the full
Euclidean space of named source coordinates define
\[
 \alpha_{i,q}=\mathbb E_1[\partial_{\zeta_q}H_i]\quad(q<i),
 \qquad
 \beta_{i,q}=\mathbb E_2[\partial_{\xi_q}\Delta_i]\quad(q\le i).
\]
The exact source representation is
\[
 \begin{aligned}
 F_{i,q}&=\alpha_{i,q}+\gamma_q(C_\xi)_{iq}\quad(q<i),\\
 D_{i,q}&=\beta_{i,q}+\mathbf1_{q<i}\gamma_q(C_\zeta)_{iq},\\
 Z_i&=\xi_i+\sum_{q<i}F_{i,q}\Delta_q,\\
 Q_i&=\zeta_i+\sum_{q\le i}D_{i,q}H_q.
 \end{aligned}                                                   \tag{S4}
\]
In particular
\[
 \beta_{i,i}=\mathbb E_2[c_k\phi''(Z_i)],                       \tag{S5}
\]
and all other current coefficients are zero, including for duplicated
queries. The slots retain their names even if their Gaussian covariance
has rank zero or two slots agree almost surely. Thus a named derivative
means the derivative of the prescribed coordinate expression, not a
derivative reconstructed from its values on a singular Gaussian support.

For completeness, the first frozen-source equations following from
(S2)–(S4) are as follows. For a reverse pulse \(p\), put
\(v_{k;p}=\partial_{\zeta_p}w_k\), which vanishes up to its injection step.
Then
\[
 \begin{aligned}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_a)
   \bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le(k,a)}D_{ka,q}\phi'(w_{t(q)}\cdot u_q)
                          (u_q\cdot v_{t(q);p})\bigg\}\bigg].
 \end{aligned}                                                   \tag{S6}
\]
For a forward pulse \(p\), put
\(U_{i;p}=\partial_{\xi_p}Z_i\),
\(c_{k;p}=\partial_{\xi_p}c_k\),
\(V_{i;p}=\partial_{\xi_p}\Delta_i\). Their equations are
\[
 \begin{aligned}
 c_{k;p}&=\sum_{q<k}\gamma_q\phi'(Z_q)U_{q;p},\\
 U_{i;p}&=\mathbf1_{i=p}+\sum_{q<i}F_{i,q}V_{q;p},\\
 V_{i;p}&=\phi'(Z_i)c_{k;p}+c_k\phi''(Z_i)U_{i;p}.
 \end{aligned}                                                   \tag{S7}
\]
Equations (S2)–(S7) restate C.4.7.N2–N8 with local notation.

C.4.7.N-cap and N9–N17 give constants \(C_0,R_0,D_0,f_0<\infty\) such that
\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 |\gamma_{ka}|\le2R_0h_kp_a,\quad
 \sum_q|D_{i,q}|\le D_0,\quad |F_{i,(s,a)}|\le f_0h_sp_a.    \tag{S8}
\]
The D row bound is valid at every passive input. In particular
\[
 Q_i=\zeta_i+J_i,\qquad |J_i|\le D_0,
 \qquad \mathbb E_1\zeta_i^2\le C_0^2.                        \tag{S9}
\]
Write \(q_k=\sum_ap_a|Q_{ka}|\) and \(J=\sum_kh_kq_k\). For every fixed
\(a\ge0\), Jensen's inequality with weights \(h_kp_a/T\), adding a zero
term if the total time is smaller than \(T\), and the scalar Gaussian
exponential moment give
\[
 \mathbb E_1e^{aJ}
       \le2\exp\{aTD_0+a^2T^2C_0^2/2\}.                     \tag{S10}
\]
No independence across times or query inputs is used. Each individual Q
has every finite moment uniformly. The same is true of Z by (S4),
(S8), bounded Delta, and its forward Gaussian of variance at most one.
The raw update and Gaussian root moments also give all finite moments
of \(\max_k|w_k|\).

### 2. All fixed orders of frozen source derivatives

For a vector-valued coordinate expression \(V\), use its Euclidean norm
inside
\[
 J_j(V)=\sum_{p_1,...,p_j}|\partial_{p_1}\cdots\partial_{p_j}V|
       \quad(j\ge1),\qquad J_0(V)=|V|.                        \tag{S11}
\]
The finite source list can be enlarged with unused coordinates, whose
derivatives are zero. The product and scalar composition inequalities are
\[
 J_j(UV)\le\sum_{r=0}^j{j\choose r}J_r(U)J_{j-r}(V),
\]
\[
 J_j(a(V))\le\sum_{\pi\in\mathfrak P_j}
       \|a^{(|\pi|)}\|_\infty\prod_{B\in\pi}J_{|B|}(V),     \tag{S12}
\]
where \(\mathfrak P_j\) denotes the partitions of \(\{1,...,j\}\).
To verify the second formula, differentiate successively and group the
indices that differentiate the same factor; summing absolute values over
all source indices factors each product into the displayed product of
sums. For a linear projection \(w\cdot u\), every \(J_j\) is at most
\(J_j(w)\) when \(|u|=1\).

For every fixed \(j\ge1\) and finite \(p\ge1\),
\[
 \left\|\max_kJ_j(w_k)\right\|_p+
      \sup_{k,u}\|J_j(H_{ku})\|_p+
      \sup_{k,u}\|J_j(Q_{ku})\|_p\le C_{j,p},                \tag{S13}
\]
and each of \(J_j(c_k),J_j(Z_{ku}),J_j(\Delta_{ku})\) and
\(J_j(\phi(Z_{ku}))\) is bounded pointwise by \(C_j\), uniformly over its
node and input. The pointwise statement means that the bound holds for
every coordinate expression, for all its Gaussian source values. It
requires no jointly continuous version of a passive Gaussian process.

Here is an induction proving these assertions at every fixed order. Put
\(S_j(k)=\max_{l\le k}J_j(w_l)\). The one-block partition in (S12) is the
only term containing \(S_j\), so
\[
 J_j(H_{lu})\le S_j(k)+P_j(S_1(k),...,S_{j-1}(k)),\quad l\le k,
\]
where \(P_j\) is a fixed polynomial with nonnegative coefficients and
\(P_1=0\). It follows from (S4) that
\[
 J_j(Q_{ka})\le\mathbf1_{j=1}
        +D_0\{S_j(k)+P_j(S_1(k),...,S_{j-1}(k))\}.
\]
The two highest-order terms in a derivative of
\(\phi'(w_k\cdot u_a)Q_{ka}\) are bounded by
\((D_0+2|Q_{ka}|)S_j(k)\). Every other term uses lower orders, with a
factor bounded by a constant times \(1+D_0+|Q_{ka}|\). Thus
\[
 S_j(k+1)\le[1+h_k(2R_0D_0+4R_0q_k)]S_j(k)
 +C_jh_k(1+D_0+q_k)P_j^+(S_1(k),...,S_{j-1}(k)).             \tag{S14}
\]
The polynomial \(P_j^+\) may include a constant. At order one the
inhomogeneous term is \(2R_0h_k\). All initial source derivatives vanish.
With
\[
 \mathcal A=2R_0D_0T+4R_0J,
\]
iteration using \(\prod(1+x_i)\le e^{\sum x_i}\) gives
\[
 \max_k S_1(k)\le2R_0Te^{\mathcal A},
\]
\[
 \max_kS_j(k)\le C_je^{\mathcal A}((1+D_0)T+J)
                  P_j^+(\max_kS_1(k),...,\max_kS_{j-1}(k)). \tag{S15}
\]
Equation (S10), induction on \(j\), and Holder's inequality prove all
finite moments in (S15), and hence (S13). This also shows that the lower
feature jets, uniformly in input, have a common pointwise envelope with
every finite moment.

For the upper population, let \(U_j(k)\) be the maximum of
\(J_j(Z_{lu})\) over nodes \(l\le k\) and the query under consideration.
By (S4) and the time/atom density of F,
\[
 J_j(Z_{ku})\le\mathbf1_{j=1}
              +f_0\sum_{s<k}h_s\max_aJ_j(\Delta_{sa}).      \tag{S16}
\]
The highest terms in c and Delta are
\[
 J_j(c_k)\le2R_0\sum_{s<k}h_s
                    [\max_aJ_j(Z_{sa})+P_j^c],
\]
\[
 J_j(\Delta_{ku})\le J_j(c_k)+2C_0J_j(Z_{ku})+P_j^\Delta.
                                                                    \tag{S17}
\]
The polynomials in (S17) use only smaller positive derivative orders and
are pointwise bounded by induction. Inserting (S17) into (S16), and
bounding the double time sum by \(T\) times its single sum, gives
\[
 U_j(k)\le C_j+f_0(2R_0T+2C_0)\sum_{s<k}h_sU_j(s).
\]
Iteration of this scalar inequality bounds it by a finite exponential
series, uniformly in the mesh. Equation (S17) and then (S12) prove all
the other upper assertions. In particular the proof never assigns a
product of masses to repeated old source derivatives: the derivative of
\(h_sp_a\phi(\xi_{sa})\) of any order still has only one factor \(h_sp_a\).

We also need derivatives of lower increments. If \(b\le k\) and
\(\sum_{l=b}^{k-1}h_l\le\ell\), then for every fixed \(j\ge0,p<\infty\),
\[
 \|J_j(w_k-w_b)\|_p+
       \sup_u\|J_j(H_{ku}-H_{bu})\|_p\le C_{j,p}\ell.       \tag{S18}
\]
For w, sum the differentiated updates (S2). Each summand without its
\(h_lp_a\) factor has bounded \(L^p\) norm by (S12)–(S13), (S9), and
Holder. Minkowski costs only \(\sum h_lp_a\le\ell\). For H use
\[
 H_{ku}-H_{bu}=\int_0^1
 \phi'((w_b+v(w_k-w_b))\cdot u)((w_k-w_b)\cdot u)\,dv.
\]
After any fixed number of source derivatives every term contains a jet of
\(w_k-w_b\). The remaining factors are bounded gates and base jets at the
two endpoints. Holder at larger finite moment orders proves (S18).
The estimates also hold for the maximum over k within this interval:
the differentiated sum of absolute update terms bounds that maximum.

For a product \(H_iH_j\), replace every endpoint with time at least b by
\(H_{bu}\) at the same input and retain earlier endpoints. The resulting
boundary product depends only on reverse slots with time strictly below b.
Its difference from \(H_iH_j\) satisfies (S18) at each fixed jet order,
by product subtraction and (S12).

### 3. Gaussian differentiation at singular covariance

Let \(C(a,b)\) be a twice continuously differentiable positive semidefinite
matrix family on a parameter rectangle, with one-sided derivatives allowed
at its boundary. Let \(G(a,b,x)\) have continuous derivatives twice in
parameters and four times in x, including the mixed derivatives displayed
below. Assume they have a common polynomial growth bound on compact
parameter sets. With \(X\sim N(0,C)\), write \(M=\mathbb E G(a,b,X)\).
Then
\[
 M_a=\mathbb E G_a+\frac12\sum_{ij}C_{a,ij}\mathbb E G_{ij},\tag{S19}
\]
\[
 \begin{aligned}
 M_{ab}={}&\mathbb E G_{ab}
   +\tfrac12\sum_{ij}C_{ab,ij}\mathbb E G_{ij}\\
 &+\tfrac12\sum_{ij}C_{a,ij}\mathbb E G_{bij}
  +\tfrac12\sum_{ij}C_{b,ij}\mathbb E G_{aij}\\
 &+\tfrac14\sum_{ij,lr}C_{a,ij}C_{b,lr}\mathbb E G_{ijlr}.
 \end{aligned}                                                   \tag{S20}
\]
There is no rank assumption. Fixed independent Gaussian roots can be
included as extra arguments of G and integrated as well.

To prove the formulas, first replace C by \(C+\eta I\), \(\eta>0\).
For its density \(p_C(x)\), direct differentiation, with \(L=C^{-1}\),
gives
\[
 \partial_a p_C=\tfrac12p_C
       (x^TLC_aLx-\operatorname{tr}(LC_a)),\qquad
 \partial_{ij}p_C=p_C((Lx)_i(Lx)_j-L_{ij}).
\]
Thus \(\partial_a p_C=\frac12\sum_{ij}C_{a,ij}\partial_{ij}p_C\).
Two integrations by parts prove (S19); polynomial growth and Gaussian
decay remove the boundary terms. Differentiating once more proves (S20),
including both separate mixed terms.

On a compact parameter set, all covariance eigenvalues have a common upper
bound, so every fixed Gaussian moment is uniformly bounded for
\(0<\eta\le1\). Couple the regularized variable as \(X+\sqrt\eta Z\), with
an independent standard Gaussian Z. Restrict the arguments to a fixed
compact set, use uniform continuity there, and use a larger moment for its
complement. This proves uniform convergence, as \(\eta\downarrow0\), of
the expectations in (S19)–(S20) and of M itself. Integrate the regularized
identities over parameter intervals and pass to their uniform limits.
The fundamental theorem of calculus gives both identities at \(\eta=0\),
including one-sided endpoints. The identical argument integrates unchanged
Gaussian roots. No covariance square root has been differentiated.

The dimension-free form used below is, for example,
\[
 \left|\sum_{ij}C_{a,ij}\mathbb E G_{ij}\right|
      \le\|C_a\|_{\max}\mathbb E J_2(G),                     \tag{S21}
\]
where \(\|M\|_{\max}=\max_{ij}|M_{ij}|\). If G already is a first
source derivative and its source index is also summed, the required tensor
orders in (S19) and (S20) are three and five. They are covered by
(S13)–(S17).

These formulas also prove existence of the finite-program mass derivatives.
Induct chronologically in (S2)–(S7). The current lower coordinate
expressions depend on earlier deterministic coefficients. Their
expectations give the current forward covariances and alpha rows. These
give the forward expressions, upper fields, beta, and reverse covariances;
only then is the lower raw state updated. At each fixed stage all coordinate
expressions and their fixed derivatives have polynomial envelopes in the
finite Gaussian source list, locally uniformly in the mass parameters.
Indeed Q is Gaussian plus a finite bounded sum, tanh derivatives are
bounded, and differentiation of each finite lower update makes only finite
products of these quantities. The coefficients already constructed are
smooth by the induction hypothesis. Formulas (S19)–(S20) therefore give
the next derivatives, even at a singular covariance. This is a finite
chronological construction, without a current-node algebraic fixed point.

### 4. The full first mass-response equations

Superscript \(\sigma\) on a deterministic scalar or coefficient denotes
its full mass derivative. On a coordinate expression it denotes the
explicit mass derivative with all Gaussian source coordinates held fixed.
The distinction is resolved by writing, for each lower or upper expression,
\[
 \mathfrak D_\ell^\sigma[G]
   =\mathbb E_\ell G^\sigma
      +\tfrac12\sum_{pq}(C_\ell^\sigma)_{pq}
                                      \mathbb E_\ell\partial_{pq}G,
 \quad C_1=C_\zeta,\quad C_2=C_\xi.                           \tag{S22}
\]
Thus \(\mathfrak D_\ell^\sigma[G]\) is the full derivative of its
expectation. Put \(W_k^\sigma=w_k^\sigma\) and
\(d_k^\sigma=c_k^\sigma\). The exact explicit recursions are
\[
 \gamma_{ka}^\sigma=-2h_k(s_ar_{ka}+p_ar_{ka}^\sigma),
 \qquad H_i^\sigma=\phi'(w_k\cdot u_i)(W_k^\sigma\cdot u_i),
                                                                    \tag{S23}
\]
\[
 Q_i^\sigma=\sum_{q\le i}
                 (D_{i,q}^\sigma H_q+D_{i,q}H_q^\sigma),
\]
\[
 \begin{aligned}
 W_{k+1}^\sigma=W_k^\sigma
 &+\sum_a\gamma_{ka}^\sigma\phi'(w_k\cdot u_a)Q_{ka}u_a\\
 &+\sum_a\gamma_{ka}u_a
   [\phi''(w_k\cdot u_a)Q_{ka}(W_k^\sigma\cdot u_a)
                      +\phi'(w_k\cdot u_a)Q_{ka}^\sigma],
 \end{aligned}                                                   \tag{S24}
\]
\[
 \begin{aligned}
 Z_i^\sigma&=\sum_{q<i}(F_{i,q}^\sigma\Delta_q+F_{i,q}\Delta_q^\sigma),\\
 d_k^\sigma&=\sum_{q<k}
        [\gamma_q^\sigma\phi(Z_q)+\gamma_q\phi'(Z_q)Z_q^\sigma],\\
 \Delta_i^\sigma&=\phi'(Z_i)d_k^\sigma
                                 +c_k\phi''(Z_i)Z_i^\sigma.
 \end{aligned}                                                   \tag{S25}
\]
There is no \(\xi^\sigma\) or \(\zeta^\sigma\) term in these explicit
equations. The changing source covariance enters through all of
\[
 \begin{aligned}
 (C_\xi^\sigma)_{ij}&=\mathfrak D_1^\sigma[H_iH_j],&
 (C_\zeta^\sigma)_{ij}&=\mathfrak D_2^\sigma[\Delta_i\Delta_j],\\
 \alpha_{i,q}^\sigma&=\mathfrak D_1^\sigma[\partial_{\zeta_q}H_i],&
 \beta_{i,q}^\sigma&=\mathfrak D_2^\sigma[\partial_{\xi_q}\Delta_i],\\
 r_{ku}^\sigma&=\mathfrak D_2^\sigma[c_k\phi(Z_{ku})],&&
 \end{aligned}                                                   \tag{S26}
\]
where a passive residual may use any fixed label, whose derivative is zero.
The deterministic rows are differentiated as
\[
 \begin{aligned}
 F_{i,q}^\sigma
   &=\alpha_{i,q}^\sigma+\gamma_q^\sigma(C_\xi)_{iq}
                                      +\gamma_q(C_\xi^\sigma)_{iq},\\
 D_{i,q}^\sigma
   &=\beta_{i,q}^\sigma+\mathbf1_{q<i}
       [\gamma_q^\sigma(C_\zeta)_{iq}
                                      +\gamma_q(C_\zeta^\sigma)_{iq}].
 \end{aligned}                                                   \tag{S27}
\]
Equations (S22)–(S27), in the chronological order already given, form
the full first response. All expectations include the actual residual
feedback, source covariance changes, and response coefficients.

### 5. A local bound with constants independent of derivative history

Fix a starting node b and a consecutive interval of nodes with total
length at most \(\ell\). Source slots with time strictly less than b are
called old; all other slots in this interval are new. Assume derivatives
on the old prefix and explicit state derivatives at b have already been
bounded uniformly. The known deterministic bounds comprise residual
derivatives, covariance entry suprema, and the absolute row sums of
derivative F,D,alpha,beta arrays. The known random bounds comprise lower
explicit source jets at every finite moment needed and upper explicit
source jets pointwise. Enlarging a source list leaves all old marginal
Gaussian laws unchanged, so their known bounds remain applicable.

For a fixed finite graph let E be the maximum over the current interval
of the following deterministic quantities: absolute residual derivatives,
entry suprema of the two covariance derivative arrays for pairs with at
least one new endpoint, and absolute row sums of F,D,alpha,beta derivatives
at a new output node. All passive inputs in these quantities are compared
at that same input, not against an old axis. The bound may first be proved
for a fixed finite list of passive queries; its constants are independent
of that list and its query values, so the resulting bound is uniform over
the circle. The fixed graph's quantities are finite by the preceding
derivative construction. Write \(S=\|\sigma\|_{\rm TV}\).

We prove
\[
                         E\le C_{\rm old}+C S+C_*\ell E.  \tag{S28}
\]
The coefficient \(C_*\) depends only on the base constants and finitely
many fixed base moment/jet bounds. It is independent of all derivative
history bounds. The finite additive constant \(C_{\rm old}\) depends on
those bounds and vanishes with them. The following estimates prove this
separation explicitly.

First, for each separately fixed source order j and moment p, the lower
explicit response obeys
\[
 \left\|\max_{b\le k}J_j(W_k^\sigma)\right\|_p
       \le C_{{\rm old},j,p}+C_{j,p}S+C_{j,p}\ell E.          \tag{S29}
\]
For j=0 take the pointwise maximum of \(|W_k^\sigma|\) over current and
earlier nodes in the interval. The coefficient of this unknown maximum
in (S24) is bounded by \(h_k(2R_0D_0+4R_0q_k)\). Its accumulated
propagator is at most \(e^{\mathcal A}\), with every fixed moment by
(S10). Current D-derivative row forcing contributes at most \(C h_kE\),
and the residual derivative part of \(\gamma^\sigma\) contributes at most
\(C h_k E q_k\). Their total over the interval has \(L^p\) norm at most
\(C_p\ell E\), since \(\|\sum_{b\le k}h_kq_k\|_p\le C_p\ell\).
The direct \(s_a\) term is treated with weights \(|s_a|/S\), omitting it
if S=0, and costs \(C_p\ell S\) using the uniform marginal Q moments.
Holder includes its product with the propagator, without an independence
assumption. The initial explicit response and terms involving old
\(W_q^\sigma\) give an additive history bound.

For positive j, apply source derivatives to (S24). The highest response
jet still has the same coefficient \(h_k(2R_0D_0+4R_0q_k)\). Every other
term is a product of a smaller response jet with base jets, or a derivative
D row with base jets, or a derivative gamma with base jets and one Q value.
This assertion follows directly from (S12): the single partition block
containing all response derivatives supplies the highest jet; every other
partition places at least one derivative on a base factor. The direct
source derivative of Q has sum one at order one and zero at larger orders.
Consequently there is no factor equal to the number of source slots.

Induct on j with the same propagator. The dependence on current E is
linear. One may separate the explicit linear recursion into the part with
zero derivative history and forcing from current E, and the part with old
history and direct \(s_a\) forcing. In the former part all terms contain
one interval sum; the product rule, Holder and induction preserve its
\(C_{j,p}\ell E\) bound. For instance the next lower-jet forcing is an
interval sum of base-jet products times a smaller response already bounded
by \(C\ell E\); its extra interval length is at most T and can be absorbed
in the constant. In the latter part the same linear estimates give only
additive old bounds and S. This proves (S29) and proves that its coefficient
of \(\ell E\) uses no derivative history. Products with old random response
jets use their already known higher finite moments, all in the additive
term. The constants in (S29) may increase with p, but p is separately fixed.

By (S12), the same bounds hold for explicit derivatives of \(H_i\), of
\(H_iH_j\), and their required source jets. To close the deterministic
inequality (S28), only source orders zero and one in these explicit
derivatives are required, in expectation. A fixed finite number of larger
base moments suffices for their Holder estimates.

Next consider the lower Gaussian terms in (S26). Split
\(C_\zeta^\sigma\) into its old-old block and its complement. The old-old
entries have the known prefix bound. Contraction against a full absolute
source tensor sum is therefore an additive old term by (S13). On the
complement at least one differentiated source is new. A boundary lower
expression, constructed after (S18), depends only on old sources. Its
derivative in that new source is zero. Hence, for \(G=H_iH_j\),
\[
 \begin{aligned}
 &\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}\mathbb E_1\partial_{pq}G\right|\\
 &\hspace{12mm}\le E\,\mathbb E_1J_2(G-G_{\rm boundary})
                      \le C\ell E.                          \tag{S30}
 \end{aligned}
\]
For alpha the required row sum is bounded by
\[
 \sum_l\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}
           \mathbb E_1\partial_{pql}H_i\right|
 \le E\,\mathbb E_1J_3(H_i-H_{bu_i})\le C\ell E.             \tag{S31}
\]
This cancellation also holds when l is old: the pair \(p,q\) still
contains a new source. When l is new its boundary derivative vanishes
as well. Formula (S29) controls the explicit terms in (S26). Together
these estimates give
\[
 \|C_\xi^\sigma\|_{\max}
        +\sup_i\sum_q|\alpha_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{S32}
\]
The covariance norm here includes old-old entries with their old bound.

Insert (S32) into the first line of (S27). Old gamma derivatives are
bounded in total absolute mass by
\(2T(R_0S+\sup_{q\text{ old}}|r_q^\sigma|)\); old base gamma values have
sum at most \(2R_0T\). Current gamma derivatives have sum at most
\(C\ell(S+E)\) by (S23). Since base lower contractions are at most one,
\[
                     \sup_i\sum_q|F_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{S33}
\]

For the upper explicit response, use (S25), (S33), and the entrywise
density \(|F_{i,(s,a)}|\le f_0h_sp_a\). Base upper jets are pointwise
bounded. At source order zero the new unknown response obeys a Volterra
inequality with coefficient \(f_0(2R_0T+2C_0)\), after the readout sum
is substituted and its double time sum bounded by T times its single sum.
The F-derivative row forcing has (S33); direct current gamma derivatives
cost \(C\ell(S+E)\), and old terms are known. At a higher source order,
the same highest-order coefficient applies, with bounded lower-order
response contributions. Induction on the source order and iteration of
the scalar Volterra inequality therefore give, pointwise,
\[
 \max_{i\text{ in interval}}
       [J_j(Z_i^\sigma)+J_j(\Delta_i^\sigma)+J_j(d_{t(i)}^\sigma)]
             \le C_{{\rm old},j}+C_jS+C_j\ell E.             \tag{S34}
\]
Linearity again separates the history and current-E contributions. Its
\(\ell E\) coefficient depends only on base upper jets, \(f_0,R_0,C_0,T\),
and the fixed order. Upper repeated source diagonals are covered by their
full tensor sums; they require no product of injection masses.

Apply (S22) to the upper expressions in (S26). The explicit part is
bounded by (S34) with source orders zero and one. The covariance term
uses the entry supremum (S32) and the base upper tensors of order two,
or three for the beta row. Thus
\[
 \sup_{i,u}|r_{iu}^\sigma|+\|C_\zeta^\sigma\|_{\max}
         +\sup_i\sum_q|\beta_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{S35}
\]
Finally substitute (S35) into the D line of (S27). Base upper
contractions are bounded by \(C_0^2\), base gamma has total mass at most
\(2R_0T\), old gamma derivatives are known, and new gamma derivatives
sum to \(C\ell(S+E)\). This gives
\[
                       \sup_i\sum_q|D_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{S36}
\]
Equations (S32)–(S36) bound all components defining E and prove (S28).

Only finitely many low-order estimates determine \(C_*\): expectations
of explicit jets through order one, base increment jets through order
three, and upper base tensors through order three. Their Holder steps use
finitely many specified finite base moments. Choose \(\ell>0\) with
\(C_*\ell\le1/2\), using those estimates alone. There is no requirement
that this same \(\ell\) make \(C_{j,p}\ell\) small for all j or p. Once E
is bounded by absorption, (S29) and (S34) furnish any higher separately
fixed moment/order bound without a further absorption step.

Decrease the maximum step to \(\ell/2\). Consecutive groups of steps can
be chosen with total lengths between \(\ell/2\) and \(\ell\), except for
the final group, so their number is at most \(2T/\ell+1\). The first group
has zero derivative history. Absorption in (S28) bounds E there by CS.
Afterward obtain all higher finite moments of explicit lower response
jets through order three and upper response jets through order three
from (S29)–(S34). These give the next group's old bounds. Iterate over
the bounded number of groups. The first derivative system is linear in
\(\sigma\), so every bound remains proportional to S. The number of groups
and all resulting constants are independent of the mesh and support. The
output equation in (S26) proves the first assertion of (S1).

### 6. The mixed second response and the same absorption constant

Fix the first responses in directions \(\sigma,\tau\), now uniformly
bounded through T. Write \(R=\|\tau\|_{\rm TV}\). The exact weight formula is
\[
 \gamma_{ka}^{\sigma\tau}
    =-2h_k(s_ar_{ka}^\tau+v_ar_{ka}^\sigma+p_ar_{ka}^{\sigma\tau}).
                                                                    \tag{S37}
\]
The first two terms have total absolute size at most \(C\ell SR\) on a
group of length \(\ell\); the last has exactly the first response's
linear unknown coefficient.

For every lower or upper expectation the full mixed derivative is
\[
 \begin{aligned}
 \mathfrak D_\ell^{\sigma\tau}[G]
 ={}&\mathbb E_\ell G^{\sigma\tau}
   +\tfrac12\sum_{pq}(C_\ell^{\sigma\tau})_{pq}
                                      \mathbb E_\ell\partial_{pq}G\\
 &+\tfrac12\sum_{pq}(C_\ell^\sigma)_{pq}
                                      \mathbb E_\ell\partial_{pq}G^\tau
  +\tfrac12\sum_{pq}(C_\ell^\tau)_{pq}
                                      \mathbb E_\ell\partial_{pq}G^\sigma\\
 &+\tfrac14\sum_{pq,lr}(C_\ell^\sigma)_{pq}(C_\ell^\tau)_{lr}
                                      \mathbb E_\ell\partial_{pqlr}G.
 \end{aligned}                                                   \tag{S38}
\]
The last three terms are already bounded by CSR. For alpha and beta,
G is a first source derivative whose index is also summed: the mixed
first-response term uses explicit source order three, and the last term
uses base source order five. Scalar products and output expectations need
no larger orders. All required first response moments were obtained after
the first-order absorption and are now known constants.

Here are the explicit second identities, which specify the highest-order
linear part without dropping product terms:
\[
 H_i^{\sigma\tau}=\phi'(w_k\cdot u_i)(W_k^{\sigma\tau}\cdot u_i)
       +\phi''(w_k\cdot u_i)(W_k^\sigma\cdot u_i)(W_k^\tau\cdot u_i),
\]
\[
 Q_i^{\sigma\tau}=\sum_{q\le i}
 [D_{i,q}^{\sigma\tau}H_q+D_{i,q}H_q^{\sigma\tau}
                    +D_{i,q}^\sigma H_q^\tau+D_{i,q}^\tau H_q^\sigma],
\]
\[
 Z_i^{\sigma\tau}=\sum_{q<i}
 [F_{i,q}^{\sigma\tau}\Delta_q+F_{i,q}\Delta_q^{\sigma\tau}
          +F_{i,q}^\sigma\Delta_q^\tau+F_{i,q}^\tau\Delta_q^\sigma],
                                                                    \tag{S39}
\]
\[
 \begin{aligned}
 d_k^{\sigma\tau}=\sum_{q<k}[&\gamma_q^{\sigma\tau}\phi(Z_q)
            +\gamma_q\phi'(Z_q)Z_q^{\sigma\tau}
            +\gamma_q\phi''(Z_q)Z_q^\sigma Z_q^\tau\\
            &+\gamma_q^\sigma\phi'(Z_q)Z_q^\tau
             +\gamma_q^\tau\phi'(Z_q)Z_q^\sigma],\\
 \Delta_i^{\sigma\tau}={}&\phi'(Z_i)d_k^{\sigma\tau}
              +c_k\phi''(Z_i)Z_i^{\sigma\tau}
              +\phi''(Z_i)(d_k^\sigma Z_i^\tau+d_k^\tau Z_i^\sigma)
              +c_k\phi'''(Z_i)Z_i^\sigma Z_i^\tau.
 \end{aligned}                                                   \tag{S40}
\]
Let \(L_{ka}=\phi'(w_k\cdot u_a)Q_{ka}u_a\). Its explicit first derivative
is the bracketed summand of (S24), and its mixed derivative is
\[
 \begin{aligned}
 L_{ka}^{\sigma\tau}=u_a[&\phi''(w_k\cdot u_a)Q_{ka}
                                      (W_k^{\sigma\tau}\cdot u_a)
                          +\phi'(w_k\cdot u_a)Q_{ka}^{\sigma\tau}\\
 &+\phi'''(w_k\cdot u_a)Q_{ka}
                  (W_k^\sigma\cdot u_a)(W_k^\tau\cdot u_a)\\
 &+\phi''(w_k\cdot u_a)
       ((W_k^\sigma\cdot u_a)Q_{ka}^\tau
                         +(W_k^\tau\cdot u_a)Q_{ka}^\sigma)].
 \end{aligned}
\]
Consequently
\[
 W_{k+1}^{\sigma\tau}=W_k^{\sigma\tau}+\sum_a
 [\gamma_{ka}^{\sigma\tau}L_{ka}+\gamma_{ka}L_{ka}^{\sigma\tau}
       +\gamma_{ka}^\sigma L_{ka}^\tau
       +\gamma_{ka}^\tau L_{ka}^\sigma].                       \tag{S41}
\]
The deterministic coefficients satisfy
\[
 \begin{aligned}
 F_{i,q}^{\sigma\tau}={}&\alpha_{i,q}^{\sigma\tau}
   +\gamma_q^{\sigma\tau}(C_\xi)_{iq}
   +\gamma_q(C_\xi^{\sigma\tau})_{iq}
   +\gamma_q^\sigma(C_\xi^\tau)_{iq}
   +\gamma_q^\tau(C_\xi^\sigma)_{iq},\\
 D_{i,q}^{\sigma\tau}={}&\beta_{i,q}^{\sigma\tau}+\mathbf1_{q<i}
 [\gamma_q^{\sigma\tau}(C_\zeta)_{iq}
   +\gamma_q(C_\zeta^{\sigma\tau})_{iq}
   +\gamma_q^\sigma(C_\zeta^\tau)_{iq}
   +\gamma_q^\tau(C_\zeta^\sigma)_{iq}].
 \end{aligned}                                                   \tag{S42}
\]
Second derivatives of covariances, alpha, beta and residuals are given by
(S26) with \(\mathfrak D^{\sigma\tau}\) from (S38). This completely
specifies the second recurrence.

Every occurrence of a mixed second unknown in (S37)–(S42) is linear,
with exactly the base coefficient occurring in (S23)–(S27). All other
terms contain two first responses or a mass direction times a first
response. Their source-jet norms are bounded by CSR using the first
bounds and Holder; scalar coefficient rows use their absolute row sums.
For terms in raw updates the outside factor is still \(h_kp_a\),
\(h_ks_a\), or \(h_kv_a\). For example, the two coefficient cross terms
in (S42) sum to at most a first covariance supremum times the total
absolute first gamma sum. Thus no source count occurs in these known
inhomogeneous terms.

Let \(E_2\) be the deterministic norm of Section 5 for mixed second
derivatives. Its explicit history needs only source jets through order
one, at all finite moments needed. The first two terms of (S38) form
the same linear Gaussian part as before. For the unknown new block of
\(C_\zeta^{\sigma\tau}\), subtract the same boundary lower expression.
Equations (S30)–(S31) give \(C\ell E_2\), because they use unchanged
base increment tensors. The last three terms of (S38) are known CSR.
The explicit linear propagation and all other deterministic rows have
the same coefficients as Section 5, by (S39)–(S42). Therefore
\[
                     E_2\le C_{{\rm old},2}+CSR+C_*\ell E_2.\tag{S43}
\]
The coefficient of \(\ell E_2\) is a base constant. First-response bounds
enter only the additive term; they do not change the chosen interval
length. Absorb with the same \(\ell\), obtain the necessary higher
explicit moments afterward, and iterate over the same bounded number
of intervals. Initial second derivatives vanish. Bilinearity in
\((\sigma,\tau)\) preserves the factor SR throughout this induction.
The output expectation in (S38) proves the second assertion of (S1).

### 7. Zero masses and the observation interval

For a fixed support and fixed graph, the derivative expressions obtained
chronologically from (S19)–(S20) extend continuously as positive masses
approach zero while the law stays in the ball. To verify this, use the
finite construction order again. Each coefficient already constructed has
a continuous derivative extension. Its descendants have common polynomial
Gaussian envelopes locally on the closed mass parameter set. Bounded
covariances and the regularization argument in Section 3 pass their
expectations and derivative expressions continuously to the boundary.
Unused zero-mass updates vanish, and introducing their unused source names
does not change the value recursion. Integrating the interior derivative
identities on admissible segments or rectangles and taking the boundary
limit gives their one-sided versions. Constants in (S1) did not depend
on the minimum positive mass. This proves the stated boundary extension,
including adding a new atom. It does not approximate a singular covariance
by a nonsingular law; covariance rank was unrestricted at every step.

At a non-node time, the affine raw Euler state equals the state obtained
by appending the appropriate shorter final Euler step, followed by
recomputation of its observations. C.4.7.N-cap applies to this program as
well. All estimates are uniform over the passive input and over such
final steps. They therefore hold on the whole physical interval
\([0,40]\), and imply the normalized-circle \(L^2\) bounds.

The lemma concerns derivatives of the exact population Euler algorithms,
with all three trained blocks and both orientations of the initialized
Gaussian action. Its proof uses the C.4.7 cap and the III.F source
representation, with source moments derived above. No bounded action of
\(A_0\) or \(A_0^*\) on arbitrary \(L^p\) inputs, no ambient raw-\(L^2\)
Fréchet derivative, and no interchange with a finite-width derivative are
needed.
