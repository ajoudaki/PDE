### C.4.8. Sampling fluctuations of the trained prediction

Unqualified equation labels below belong to this proof unit. The finite-source and statistical lemmas state their local notation explicitly.

##### Model and theorem


Use exactly the population carrier, initialization, and physical gradient flow
of C.4.7. Write \(u=x/\sqrt2\), \(\phi=\tanh\), and
\(\theta=(w,K,c)\), with \(A=A_0+K\). The retained fields are
\[
 h_\theta(u)=\phi(w\cdot u),\quad Z_\theta(u)=Ah_\theta(u),\quad
 b_\theta(u)=\phi(Z_\theta(u)),\quad
 \Delta_\theta(u)=c\phi'(Z_\theta(u)),\quad Q_\theta(u)=A^*\Delta_\theta(u),
 \quad f_\theta(u)=\langle c,b_\theta(u)\rangle.
\]
For \(r_\theta(u,y)=f_\theta(u)-y\), the actual population equation is
\[
 \dot\theta=-2\int r_\theta(u,y)
 \bigl(\phi'(w\cdot u)Q_\theta(u)u,
             \Delta_\theta(u)\otimes h_\theta(u),b_\theta(u)\bigr)
 \,d\mu(u,y),\qquad \theta(0)=(g,0,0).                 \tag{C.4.8.P1}
\]
The first state component is the full two-dimensional first row, the second
is the learned Hilbert--Schmidt middle increment, and the third is the trained
readout. The initialized Gaussian action and its actual adjoint in (C.4.8.P1) are
the common prescribed construction, not arbitrary operators with the same
norm. The zero population initial readout is its width limit. At finite width
the actual independent Gaussian stored readout is retained throughout.
Population predictions are deterministic expectations on this prescribed
carrier; no additional random environment is left outside those expectations.

The finite networks have two equal-width bias-free tanh hidden layers, output
divided by \(n\), independent centered Gaussian stored variances
\((1,1/n,1/n^2)\), mobilities \((n,1,n)\), and unhalved squared loss integrated
against the labeled training law. No initialization is reset when laws change.

Fix \(Y\ge1\), \(T=40\), the data space and its metric
\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|,
\]
and \(\nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}+
\tfrac12\delta_{(\sqrt2e_2,-1)}\). Let \(\delta_Y\) be the C.4.7 radius,
\(U_Y=\{\mu:W_1(\mu,\nu_*)<\delta_Y\}\). Its construction chooses this
radius inside the neighborhood with uniform finite-Euler source caps.
Let \(\rho\) be normalized circle arc length,
\(H=L^2(\sqrt2S^1,\rho;\mathbb R)\), and
\(F(\mu)=f_\mu(T,\cdot)\). We also use the stronger output space
\(\mathcal C=C(\sqrt2S^1;\mathbb R)\) with its supremum norm.

Set \(\delta'_Y=\delta_Y/4\). For every separately fixed Borel law
\(\mu\) with \(W_1(\mu,\nu_*)<\delta'_Y\), the following conclusions hold:
there is a bounded continuous \(\mathcal C\)-valued atom response
\(I_\mu(z)\), given by the full source recursion below, such that
\[
 I_\mu(z)=\lim_{\epsilon\downarrow0}
 \frac{F((1-\epsilon)\mu+\epsilon\delta_z)-F(\mu)}{\epsilon},
 \qquad \int I_\mu(z)\,d\mu(z)=0.                       \tag{C.4.8.P2}
\]
The derivative holds in \(\mathcal C\), hence in \(H\), for every \(z\).
For iid observations with empirical law \(\mu_m\), define the bounded
measurable extension
\[
 \overline F(Q)=F(Q)\quad(Q\in U_Y),\qquad
 \overline F(Q)=0\quad(Q\notin U_Y).                    \tag{C.4.8.P3}
\]
Then, with \(r_m=\overline F(\mu_m)-F(\mu)-m^{-1}\sum_i I_\mu(Z_i)\),
\[
 m\,\mathbb E\|r_m\|_H^2\longrightarrow0.              \tag{C.4.8.P4}
\]
In particular \(\sqrt m\,r_m\to0\) in probability. Its covariance and
whole-function limit are
\[
 \Sigma_\mu v=\int\langle I_\mu(z),v\rangle_H I_\mu(z)\,d\mu(z),
 \qquad \sqrt m\,[\overline F(\mu_m)-F(\mu)]
                  \Rightarrow\mathcal N_H(0,\Sigma_\mu).              \tag{C.4.8.P5}
\]
The finite-network conclusion is the width-first assertion
\[
 \lim_{m\to\infty}\limsup_{n\to\infty}
 d_{\rm BL}\!\left(\operatorname{Law}\!\left[
 \sqrt m\,(f_{n,\mu_m}(T,\cdot)-F(\mu))\right],
                  \mathcal N_H(0,\Sigma_\mu)\right)=0,                \tag{C.4.8.P6}
\]
where sampling and initialization are independent and both are included in
the law. Here bounded-Lipschitz tests have absolute value and Lipschitz constant
at most one. No simultaneous width/sample rate is asserted.

##### C.4.8.1. Uniform first and second finite-program responses


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
       \le C\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.             \tag{C.4.8.S1}
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

###### 1. Exact finite source recursion and its uniform bounds

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
 \end{aligned}                                                   \tag{C.4.8.S2}
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
 (C_\zeta)_{ij}=\mathbb E_2[\Delta_i\Delta_j].                  \tag{C.4.8.S3}
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
 \end{aligned}                                                   \tag{C.4.8.S4}
\]
In particular
\[
 \beta_{i,i}=\mathbb E_2[c_k\phi''(Z_i)],                       \tag{C.4.8.S5}
\]
and all other current coefficients are zero, including for duplicated
queries. The slots retain their names even if their Gaussian covariance
has rank zero or two slots agree almost surely. Thus a named derivative
means the derivative of the prescribed coordinate expression, not a
derivative reconstructed from its values on a singular Gaussian support.

For completeness, the first frozen-source equations following from
(C.4.8.S2)–(C.4.8.S4) are as follows. For a reverse pulse \(p\), put
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
 \end{aligned}                                                   \tag{C.4.8.S6}
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
 \end{aligned}                                                   \tag{C.4.8.S7}
\]
Equations (C.4.8.S2)–(C.4.8.S7) restate C.4.7.N2–N8 with local notation.

C.4.7.N-cap and N9–N17 give constants \(C_0,R_0,D_0,f_0<\infty\) such that
\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 |\gamma_{ka}|\le2R_0h_kp_a,\quad
 \sum_q|D_{i,q}|\le D_0,\quad |F_{i,(s,a)}|\le f_0h_sp_a.    \tag{C.4.8.S8}
\]
The D row bound is valid at every passive input. In particular
\[
 Q_i=\zeta_i+J_i,\qquad |J_i|\le D_0,
 \qquad \mathbb E_1\zeta_i^2\le C_0^2.                        \tag{C.4.8.S9}
\]
Write \(q_k=\sum_ap_a|Q_{ka}|\) and \(J=\sum_kh_kq_k\). For every fixed
\(a\ge0\), Jensen's inequality with weights \(h_kp_a/T\), adding a zero
term if the total time is smaller than \(T\), and the scalar Gaussian
exponential moment give
\[
 \mathbb E_1e^{aJ}
       \le2\exp\{aTD_0+a^2T^2C_0^2/2\}.                     \tag{C.4.8.S10}
\]
No independence across times or query inputs is used. Each individual Q
has every finite moment uniformly. The same is true of Z by (C.4.8.S4),
(C.4.8.S8), bounded Delta, and its forward Gaussian of variance at most one.
The raw update and Gaussian root moments also give all finite moments
of \(\max_k|w_k|\).

###### 2. All fixed orders of frozen source derivatives

For a vector-valued coordinate expression \(V\), use its Euclidean norm
inside
\[
 J_j(V)=\sum_{p_1,...,p_j}|\partial_{p_1}\cdots\partial_{p_j}V|
       \quad(j\ge1),\qquad J_0(V)=|V|.                        \tag{C.4.8.S11}
\]
The finite source list can be enlarged with unused coordinates, whose
derivatives are zero. The product and scalar composition inequalities are
\[
 J_j(UV)\le\sum_{r=0}^j{j\choose r}J_r(U)J_{j-r}(V),
\]
\[
 J_j(a(V))\le\sum_{\pi\in\mathfrak P_j}
       \|a^{(|\pi|)}\|_\infty\prod_{B\in\pi}J_{|B|}(V),     \tag{C.4.8.S12}
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
      \sup_{k,u}\|J_j(Q_{ku})\|_p\le C_{j,p},                \tag{C.4.8.S13}
\]
and each of \(J_j(c_k),J_j(Z_{ku}),J_j(\Delta_{ku})\) and
\(J_j(\phi(Z_{ku}))\) is bounded pointwise by \(C_j\), uniformly over its
node and input. The pointwise statement means that the bound holds for
every coordinate expression, for all its Gaussian source values. It
requires no jointly continuous version of a passive Gaussian process.

Here is an induction proving these assertions at every fixed order. Put
\(S_j(k)=\max_{l\le k}J_j(w_l)\). The one-block partition in (C.4.8.S12) is the
only term containing \(S_j\), so
\[
 J_j(H_{lu})\le S_j(k)+P_j(S_1(k),...,S_{j-1}(k)),\quad l\le k,
\]
where \(P_j\) is a fixed polynomial with nonnegative coefficients and
\(P_1=0\). It follows from (C.4.8.S4) that
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
 +C_jh_k(1+D_0+q_k)P_j^+(S_1(k),...,S_{j-1}(k)).             \tag{C.4.8.S14}
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
                  P_j^+(\max_kS_1(k),...,\max_kS_{j-1}(k)). \tag{C.4.8.S15}
\]
Equation (C.4.8.S10), induction on \(j\), and Holder's inequality prove all
finite moments in (C.4.8.S15), and hence (C.4.8.S13). This also shows that the lower
feature jets, uniformly in input, have a common pointwise envelope with
every finite moment.

For the upper population, let \(U_j(k)\) be the maximum of
\(J_j(Z_{lu})\) over nodes \(l\le k\) and the query under consideration.
By (C.4.8.S4) and the time/atom density of F,
\[
 J_j(Z_{ku})\le\mathbf1_{j=1}
              +f_0\sum_{s<k}h_s\max_aJ_j(\Delta_{sa}).      \tag{C.4.8.S16}
\]
The highest terms in c and Delta are
\[
 J_j(c_k)\le2R_0\sum_{s<k}h_s
                    [\max_aJ_j(Z_{sa})+P_j^c],
\]
\[
 J_j(\Delta_{ku})\le J_j(c_k)+2C_0J_j(Z_{ku})+P_j^\Delta.
                                                                    \tag{C.4.8.S17}
\]
The polynomials in (C.4.8.S17) use only smaller positive derivative orders and
are pointwise bounded by induction. Inserting (C.4.8.S17) into (C.4.8.S16), and
bounding the double time sum by \(T\) times its single sum, gives
\[
 U_j(k)\le C_j+f_0(2R_0T+2C_0)\sum_{s<k}h_sU_j(s).
\]
Iteration of this scalar inequality bounds it by a finite exponential
series, uniformly in the mesh. Equation (C.4.8.S17) and then (C.4.8.S12) prove all
the other upper assertions. In particular the proof never assigns a
product of masses to repeated old source derivatives: the derivative of
\(h_sp_a\phi(\xi_{sa})\) of any order still has only one factor \(h_sp_a\).

We also need derivatives of lower increments. If \(b\le k\) and
\(\sum_{l=b}^{k-1}h_l\le\ell\), then for every fixed \(j\ge0,p<\infty\),
\[
 \|J_j(w_k-w_b)\|_p+
       \sup_u\|J_j(H_{ku}-H_{bu})\|_p\le C_{j,p}\ell.       \tag{C.4.8.S18}
\]
For w, sum the differentiated updates (C.4.8.S2). Each summand without its
\(h_lp_a\) factor has bounded \(L^p\) norm by (C.4.8.S12)–(C.4.8.S13), (C.4.8.S9), and
Holder. Minkowski costs only \(\sum h_lp_a\le\ell\). For H use
\[
 H_{ku}-H_{bu}=\int_0^1
 \phi'((w_b+v(w_k-w_b))\cdot u)((w_k-w_b)\cdot u)\,dv.
\]
After any fixed number of source derivatives every term contains a jet of
\(w_k-w_b\). The remaining factors are bounded gates and base jets at the
two endpoints. Holder at larger finite moment orders proves (C.4.8.S18).
The estimates also hold for the maximum over k within this interval:
the differentiated sum of absolute update terms bounds that maximum.

For a product \(H_iH_j\), replace every endpoint with time at least b by
\(H_{bu}\) at the same input and retain earlier endpoints. The resulting
boundary product depends only on reverse slots with time strictly below b.
Its difference from \(H_iH_j\) satisfies (C.4.8.S18) at each fixed jet order,
by product subtraction and (C.4.8.S12).

###### 3. Gaussian differentiation at singular covariance

Let \(C(a,b)\) be a twice continuously differentiable positive semidefinite
matrix family on a parameter rectangle, with one-sided derivatives allowed
at its boundary. Let \(G(a,b,x)\) have continuous derivatives twice in
parameters and four times in x, including the mixed derivatives displayed
below. Assume they have a common polynomial growth bound on compact
parameter sets. With \(X\sim N(0,C)\), write \(M=\mathbb E G(a,b,X)\).
Then
\[
 M_a=\mathbb E G_a+\frac12\sum_{ij}C_{a,ij}\mathbb E G_{ij},\tag{C.4.8.S19}
\]
\[
 \begin{aligned}
 M_{ab}={}&\mathbb E G_{ab}
   +\tfrac12\sum_{ij}C_{ab,ij}\mathbb E G_{ij}\\
 &+\tfrac12\sum_{ij}C_{a,ij}\mathbb E G_{bij}
  +\tfrac12\sum_{ij}C_{b,ij}\mathbb E G_{aij}\\
 &+\tfrac14\sum_{ij,lr}C_{a,ij}C_{b,lr}\mathbb E G_{ijlr}.
 \end{aligned}                                                   \tag{C.4.8.S20}
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
Two integrations by parts prove (C.4.8.S19); polynomial growth and Gaussian
decay remove the boundary terms. Differentiating once more proves (C.4.8.S20),
including both separate mixed terms.

On a compact parameter set, all covariance eigenvalues have a common upper
bound, so every fixed Gaussian moment is uniformly bounded for
\(0<\eta\le1\). Couple the regularized variable as \(X+\sqrt\eta Z\), with
an independent standard Gaussian Z. Restrict the arguments to a fixed
compact set, use uniform continuity there, and use a larger moment for its
complement. This proves uniform convergence, as \(\eta\downarrow0\), of
the expectations in (C.4.8.S19)–(C.4.8.S20) and of M itself. Integrate the regularized
identities over parameter intervals and pass to their uniform limits.
The fundamental theorem of calculus gives both identities at \(\eta=0\),
including one-sided endpoints. The identical argument integrates unchanged
Gaussian roots. No covariance square root has been differentiated.

The dimension-free form used below is, for example,
\[
 \left|\sum_{ij}C_{a,ij}\mathbb E G_{ij}\right|
      \le\|C_a\|_{\max}\mathbb E J_2(G),                     \tag{C.4.8.S21}
\]
where \(\|M\|_{\max}=\max_{ij}|M_{ij}|\). If G already is a first
source derivative and its source index is also summed, the required tensor
orders in (C.4.8.S19) and (C.4.8.S20) are three and five. They are covered by
(C.4.8.S13)–(C.4.8.S17).

These formulas also prove existence of the finite-program mass derivatives.
Induct chronologically in (C.4.8.S2)–(C.4.8.S7). The current lower coordinate
expressions depend on earlier deterministic coefficients. Their
expectations give the current forward covariances and alpha rows. These
give the forward expressions, upper fields, beta, and reverse covariances;
only then is the lower raw state updated. At each fixed stage all coordinate
expressions and their fixed derivatives have polynomial envelopes in the
finite Gaussian source list, locally uniformly in the mass parameters.
Indeed Q is Gaussian plus a finite bounded sum, tanh derivatives are
bounded, and differentiation of each finite lower update makes only finite
products of these quantities. The coefficients already constructed are
smooth by the induction hypothesis. Formulas (C.4.8.S19)–(C.4.8.S20) therefore give
the next derivatives, even at a singular covariance. This is a finite
chronological construction, without a current-node algebraic fixed point.

###### 4. The full first mass-response equations

Superscript \(\sigma\) on a deterministic scalar or coefficient denotes
its full mass derivative. On a coordinate expression it denotes the
explicit mass derivative with all Gaussian source coordinates held fixed.
The distinction is resolved by writing, for each lower or upper expression,
\[
 \mathfrak D_\ell^\sigma[G]
   =\mathbb E_\ell G^\sigma
      +\tfrac12\sum_{pq}(C_\ell^\sigma)_{pq}
                                      \mathbb E_\ell\partial_{pq}G,
 \quad C_1=C_\zeta,\quad C_2=C_\xi.                           \tag{C.4.8.S22}
\]
Thus \(\mathfrak D_\ell^\sigma[G]\) is the full derivative of its
expectation. Put \(W_k^\sigma=w_k^\sigma\) and
\(d_k^\sigma=c_k^\sigma\). The exact explicit recursions are
\[
 \gamma_{ka}^\sigma=-2h_k(s_ar_{ka}+p_ar_{ka}^\sigma),
 \qquad H_i^\sigma=\phi'(w_k\cdot u_i)(W_k^\sigma\cdot u_i),
                                                                    \tag{C.4.8.S23}
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
 \end{aligned}                                                   \tag{C.4.8.S24}
\]
\[
 \begin{aligned}
 Z_i^\sigma&=\sum_{q<i}(F_{i,q}^\sigma\Delta_q+F_{i,q}\Delta_q^\sigma),\\
 d_k^\sigma&=\sum_{q<k}
        [\gamma_q^\sigma\phi(Z_q)+\gamma_q\phi'(Z_q)Z_q^\sigma],\\
 \Delta_i^\sigma&=\phi'(Z_i)d_k^\sigma
                                 +c_k\phi''(Z_i)Z_i^\sigma.
 \end{aligned}                                                   \tag{C.4.8.S25}
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
 \end{aligned}                                                   \tag{C.4.8.S26}
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
 \end{aligned}                                                   \tag{C.4.8.S27}
\]
Equations (C.4.8.S22)–(C.4.8.S27), in the chronological order already given, form
the full first response. All expectations include the actual residual
feedback, source covariance changes, and response coefficients.

###### 5. A local bound with constants independent of derivative history

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
                         E\le C_{\rm old}+C S+C_*\ell E.  \tag{C.4.8.S28}
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
       \le C_{{\rm old},j,p}+C_{j,p}S+C_{j,p}\ell E.          \tag{C.4.8.S29}
\]
For j=0 take the pointwise maximum of \(|W_k^\sigma|\) over current and
earlier nodes in the interval. The coefficient of this unknown maximum
in (C.4.8.S24) is bounded by \(h_k(2R_0D_0+4R_0q_k)\). Its accumulated
propagator is at most \(e^{\mathcal A}\), with every fixed moment by
(C.4.8.S10). Current D-derivative row forcing contributes at most \(C h_kE\),
and the residual derivative part of \(\gamma^\sigma\) contributes at most
\(C h_k E q_k\). Their total over the interval has \(L^p\) norm at most
\(C_p\ell E\), since \(\|\sum_{b\le k}h_kq_k\|_p\le C_p\ell\).
The direct \(s_a\) term is treated with weights \(|s_a|/S\), omitting it
if S=0, and costs \(C_p\ell S\) using the uniform marginal Q moments.
Holder includes its product with the propagator, without an independence
assumption. The initial explicit response and terms involving old
\(W_q^\sigma\) give an additive history bound.

For positive j, apply source derivatives to (C.4.8.S24). The highest response
jet still has the same coefficient \(h_k(2R_0D_0+4R_0q_k)\). Every other
term is a product of a smaller response jet with base jets, or a derivative
D row with base jets, or a derivative gamma with base jets and one Q value.
This assertion follows directly from (C.4.8.S12): the single partition block
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
additive old bounds and S. This proves (C.4.8.S29) and proves that its coefficient
of \(\ell E\) uses no derivative history. Products with old random response
jets use their already known higher finite moments, all in the additive
term. The constants in (C.4.8.S29) may increase with p, but p is separately fixed.

By (C.4.8.S12), the same bounds hold for explicit derivatives of \(H_i\), of
\(H_iH_j\), and their required source jets. To close the deterministic
inequality (C.4.8.S28), only source orders zero and one in these explicit
derivatives are required, in expectation. A fixed finite number of larger
base moments suffices for their Holder estimates.

Next consider the lower Gaussian terms in (C.4.8.S26). Split
\(C_\zeta^\sigma\) into its old-old block and its complement. The old-old
entries have the known prefix bound. Contraction against a full absolute
source tensor sum is therefore an additive old term by (C.4.8.S13). On the
complement at least one differentiated source is new. A boundary lower
expression, constructed after (C.4.8.S18), depends only on old sources. Its
derivative in that new source is zero. Hence, for \(G=H_iH_j\),
\[
 \begin{aligned}
 &\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}\mathbb E_1\partial_{pq}G\right|\\
 &\hspace{12mm}\le E\,\mathbb E_1J_2(G-G_{\rm boundary})
                      \le C\ell E.                          \tag{C.4.8.S30}
 \end{aligned}
\]
For alpha the required row sum is bounded by
\[
 \sum_l\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}
           \mathbb E_1\partial_{pql}H_i\right|
 \le E\,\mathbb E_1J_3(H_i-H_{bu_i})\le C\ell E.             \tag{C.4.8.S31}
\]
This cancellation also holds when l is old: the pair \(p,q\) still
contains a new source. When l is new its boundary derivative vanishes
as well. Formula (C.4.8.S29) controls the explicit terms in (C.4.8.S26). Together
these estimates give
\[
 \|C_\xi^\sigma\|_{\max}
        +\sup_i\sum_q|\alpha_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{C.4.8.S32}
\]
The covariance norm here includes old-old entries with their old bound.

Insert (C.4.8.S32) into the first line of (C.4.8.S27). Old gamma derivatives are
bounded in total absolute mass by
\(2T(R_0S+\sup_{q\text{ old}}|r_q^\sigma|)\); old base gamma values have
sum at most \(2R_0T\). Current gamma derivatives have sum at most
\(C\ell(S+E)\) by (C.4.8.S23). Since base lower contractions are at most one,
\[
                     \sup_i\sum_q|F_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{C.4.8.S33}
\]

For the upper explicit response, use (C.4.8.S25), (C.4.8.S33), and the entrywise
density \(|F_{i,(s,a)}|\le f_0h_sp_a\). Base upper jets are pointwise
bounded. At source order zero the new unknown response obeys a Volterra
inequality with coefficient \(f_0(2R_0T+2C_0)\), after the readout sum
is substituted and its double time sum bounded by T times its single sum.
The F-derivative row forcing has (C.4.8.S33); direct current gamma derivatives
cost \(C\ell(S+E)\), and old terms are known. At a higher source order,
the same highest-order coefficient applies, with bounded lower-order
response contributions. Induction on the source order and iteration of
the scalar Volterra inequality therefore give, pointwise,
\[
 \max_{i\text{ in interval}}
       [J_j(Z_i^\sigma)+J_j(\Delta_i^\sigma)+J_j(d_{t(i)}^\sigma)]
             \le C_{{\rm old},j}+C_jS+C_j\ell E.             \tag{C.4.8.S34}
\]
Linearity again separates the history and current-E contributions. Its
\(\ell E\) coefficient depends only on base upper jets, \(f_0,R_0,C_0,T\),
and the fixed order. Upper repeated source diagonals are covered by their
full tensor sums; they require no product of injection masses.

Apply (C.4.8.S22) to the upper expressions in (C.4.8.S26). The explicit part is
bounded by (C.4.8.S34) with source orders zero and one. The covariance term
uses the entry supremum (C.4.8.S32) and the base upper tensors of order two,
or three for the beta row. Thus
\[
 \sup_{i,u}|r_{iu}^\sigma|+\|C_\zeta^\sigma\|_{\max}
         +\sup_i\sum_q|\beta_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{C.4.8.S35}
\]
Finally substitute (C.4.8.S35) into the D line of (C.4.8.S27). Base upper
contractions are bounded by \(C_0^2\), base gamma has total mass at most
\(2R_0T\), old gamma derivatives are known, and new gamma derivatives
sum to \(C\ell(S+E)\). This gives
\[
                       \sup_i\sum_q|D_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{C.4.8.S36}
\]
Equations (C.4.8.S32)–(C.4.8.S36) bound all components defining E and prove (C.4.8.S28).

Only finitely many low-order estimates determine \(C_*\): expectations
of explicit jets through order one, base increment jets through order
three, and upper base tensors through order three. Their Holder steps use
finitely many specified finite base moments. Choose \(\ell>0\) with
\(C_*\ell\le1/2\), using those estimates alone. There is no requirement
that this same \(\ell\) make \(C_{j,p}\ell\) small for all j or p. Once E
is bounded by absorption, (C.4.8.S29) and (C.4.8.S34) furnish any higher separately
fixed moment/order bound without a further absorption step.

Decrease the maximum step to \(\ell/2\). Consecutive groups of steps can
be chosen with total lengths between \(\ell/2\) and \(\ell\), except for
the final group, so their number is at most \(2T/\ell+1\). The first group
has zero derivative history. Absorption in (C.4.8.S28) bounds E there by CS.
Afterward obtain all higher finite moments of explicit lower response
jets through order three and upper response jets through order three
from (C.4.8.S29)–(C.4.8.S34). These give the next group's old bounds. Iterate over
the bounded number of groups. The first derivative system is linear in
\(\sigma\), so every bound remains proportional to S. The number of groups
and all resulting constants are independent of the mesh and support. The
output equation in (C.4.8.S26) proves the first assertion of (C.4.8.S1).

###### 6. The mixed second response and the same absorption constant

Fix the first responses in directions \(\sigma,\tau\), now uniformly
bounded through T. Write \(R=\|\tau\|_{\rm TV}\). The exact weight formula is
\[
 \gamma_{ka}^{\sigma\tau}
    =-2h_k(s_ar_{ka}^\tau+v_ar_{ka}^\sigma+p_ar_{ka}^{\sigma\tau}).
                                                                    \tag{C.4.8.S37}
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
 \end{aligned}                                                   \tag{C.4.8.S38}
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
                                                                    \tag{C.4.8.S39}
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
 \end{aligned}                                                   \tag{C.4.8.S40}
\]
Let \(L_{ka}=\phi'(w_k\cdot u_a)Q_{ka}u_a\). Its explicit first derivative
is the bracketed summand of (C.4.8.S24), and its mixed derivative is
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
       +\gamma_{ka}^\tau L_{ka}^\sigma].                       \tag{C.4.8.S41}
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
 \end{aligned}                                                   \tag{C.4.8.S42}
\]
Second derivatives of covariances, alpha, beta and residuals are given by
(C.4.8.S26) with \(\mathfrak D^{\sigma\tau}\) from (C.4.8.S38). This completely
specifies the second recurrence.

Every occurrence of a mixed second unknown in (C.4.8.S37)–(C.4.8.S42) is linear,
with exactly the base coefficient occurring in (C.4.8.S23)–(C.4.8.S27). All other
terms contain two first responses or a mass direction times a first
response. Their source-jet norms are bounded by CSR using the first
bounds and Holder; scalar coefficient rows use their absolute row sums.
For terms in raw updates the outside factor is still \(h_kp_a\),
\(h_ks_a\), or \(h_kv_a\). For example, the two coefficient cross terms
in (C.4.8.S42) sum to at most a first covariance supremum times the total
absolute first gamma sum. Thus no source count occurs in these known
inhomogeneous terms.

Let \(E_2\) be the deterministic norm of Section 5 for mixed second
derivatives. Its explicit history needs only source jets through order
one, at all finite moments needed. The first two terms of (C.4.8.S38) form
the same linear Gaussian part as before. For the unknown new block of
\(C_\zeta^{\sigma\tau}\), subtract the same boundary lower expression.
Equations (C.4.8.S30)–(C.4.8.S31) give \(C\ell E_2\), because they use unchanged
base increment tensors. The last three terms of (C.4.8.S38) are known CSR.
The explicit linear propagation and all other deterministic rows have
the same coefficients as Section 5, by (C.4.8.S39)–(C.4.8.S42). Therefore
\[
                     E_2\le C_{{\rm old},2}+CSR+C_*\ell E_2.\tag{C.4.8.S43}
\]
The coefficient of \(\ell E_2\) is a base constant. First-response bounds
enter only the additive term; they do not change the chosen interval
length. Absorb with the same \(\ell\), obtain the necessary higher
explicit moments afterward, and iterate over the same bounded number
of intervals. Initial second derivatives vanish. Bilinearity in
\((\sigma,\tau)\) preserves the factor SR throughout this induction.
The output expectation in (C.4.8.S38) proves the second assertion of (C.4.8.S1).

###### 7. Zero masses and the observation interval

For a fixed support and fixed graph, the derivative expressions obtained
chronologically from (C.4.8.S19)–(C.4.8.S20) extend continuously as positive masses
approach zero while the law stays in the ball. To verify this, use the
finite construction order again. Each coefficient already constructed has
a continuous derivative extension. Its descendants have common polynomial
Gaussian envelopes locally on the closed mass parameter set. Bounded
covariances and the regularization argument in Section 3 pass their
expectations and derivative expressions continuously to the boundary.
Unused zero-mass updates vanish, and introducing their unused source names
does not change the value recursion. Integrating the interior derivative
identities on admissible segments or rectangles and taking the boundary
limit gives their one-sided versions. Constants in (C.4.8.S1) did not depend
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

##### C.4.8.2. Actual influence for Borel laws

###### Finite estimate and actual value completion


Choose a closed law ball of radius \(3\delta_Y/4\). The lemma in C.4.8.1 applies
to all finite laws in a slightly larger ball still inside the C.4.7 source-cap
neighborhood, and all sufficiently fine population raw Euler meshes. It gives
constants \(L,M<\infty\), independent of the mesh, support size, minimum mass,
and covariance rank, such that its endpoint map \(F_h\) obeys
\[
 \|\partial_\sigma F_h(\lambda)\|_{\mathcal C}\le L\|\sigma\|_{\rm TV},
 \qquad
 \|\partial_\sigma\partial_\tau F_h(\lambda)\|_{\mathcal C}
                    \le M\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.        \tag{C.4.8.P7}
\]
Directions have zero total mass. They are taken in the finite simplex, with
continuous one-sided extensions at zero masses. The total-variation norm is
the total mass of the variation measure, so \(\|\delta_z-\delta_{z'}\|_{\rm TV}
\le2\). The estimates concern only probability-preserving segments and
rectangles lying in the stated region.

C.4.7 gives \(F_h(\lambda)\to F(\lambda)\) in \(\mathcal C\) for every
fixed finite law there. Its proof also gives uniform value completion on
smaller balls, but the first passage below only needs pointwise value
convergence, including at the finitely many law arguments in each comparison.
The actual map \(F:U_Y\to\mathcal C\) is \(W_1\)-continuous and bounded.
Boundedness follows already from \(\|c(t)\|_\infty\le2Yt\) in C.4.7; a
larger Euler bound \(Y(e^{2T}-1)\) would suffice as well.

###### 3. Actual atom response, centering, and general directions

Let \(\mathcal K=\{Q:W_1(Q,\nu_*)\le\delta_Y/2\}\) and
\(D_Y=2+2Y\), an upper bound for the data diameter. Choose
\(\epsilon_0=\min(1/2,\delta_Y/(4D_Y))\). Every contamination of a law
in \(\mathcal K\) of size at most \(\epsilon_0\) remains in the larger
ball of Section 2. Finite-support Taylor's formula from (C.4.8.P7) gives
\[
 \|F_h((1-\epsilon)\lambda+\epsilon\delta_z)-F_h(\lambda)
       -\epsilon I_{h,\lambda}(z)\|_{\mathcal C}
                  \le2M\epsilon^2,\qquad
 I_{h,\lambda}(z)=\partial_{\delta_z-\lambda}F_h(\lambda).             \tag{C.4.8.P8}
\]
To add a new observation, include its slot with mass zero and use the
one-sided source derivative. No strictly positive lower mass is required.

Fix \(\lambda,z\). Comparing two derivatives to the same forward quotient
in (C.4.8.P8) shows that their limsup difference as both meshes vanish is at most
\(4M\epsilon\). The quotient values converge by C.4.7. Letting \(\epsilon\)
decrease proves that \(I_{h,\lambda}(z)\) has a limit in \(\mathcal C\),
denoted \(I_\lambda(z)\). It satisfies \(\|I_\lambda(z)\|\le2L\), and
passing to the limit in (C.4.8.P8) gives its actual contamination derivative with
the same remainder. This argument uses arbitrary vanishing mesh sequences;
the result does not depend on a chosen sequence.

For arbitrary \(Q\in\mathcal K\), define the continuous forward quotient
\[
 J_\epsilon(Q,z)=
   \epsilon^{-1}\{F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)\}.
\]
For finite \(Q\), (C.4.8.P8) gives
\(\|J_\epsilon(Q,z)-J_\eta(Q,z)\|\le2M(\epsilon+\eta)\).
Finite laws are \(W_1\)-dense in \(\mathcal K\): approximate by finite
quantization and, if necessary, mix a vanishing amount of \(\nu_*\) to move
strictly inside the ball. Continuity of \(F\) passes this inequality to every
\(Q\). Thus the quotients converge uniformly in \((Q,z)\) to
\(I_Q(z)\), with
\[
 \|F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)-\epsilon I_Q(z)\|_{\mathcal C}
                         \le2M\epsilon^2.                            \tag{C.4.8.P9}
\]
The map \((Q,z)\mapsto(1-\epsilon)Q+\epsilon\delta_z\) is continuous in
\(W_1\), by the mixture coupling. Each \(J_\epsilon\) is therefore jointly
continuous. Its uniform limit \(I\) is jointly continuous on the compact
set \(\mathcal K\times\mathcal Z\), and is bounded by \(2L\). In particular
it is a Bochner-measurable, square-integrable \(H\)-valued field.

For each finite law \(\lambda=\sum_a p_a\delta_{z_a}\), linearity of the
finite derivative gives
\[
 \sum_a p_a I_{h,\lambda}(z_a)=
 \partial_{\sum_a p_a(\delta_{z_a}-\lambda)}F_h(\lambda)=0.
\]
The mesh limit preserves this equality. If \(\lambda_j\to Q\) weakly,
joint continuity implies \(I_{\lambda_j}\to I_Q\) uniformly in the atom.
For any continuous Banach-valued function on a compact metric space its
integrals converge in norm under weak convergence of probability laws: choose
a finite continuous partition of unity whose weighted point values uniformly
approximate that function, and apply weak convergence to its finitely many
scalar weights. Applying this fact to \(I_Q\) proves
\[
                         \int I_Q\,dQ=0.                             \tag{C.4.8.P10}
\]
This proves centering for the actual trained response, not just for a formal
linearized equation.

At the reference law this response agrees with C.4.6:
\(I_{\nu_*}(z)=\mathscr D_{\delta_z-\nu_*}f(T,\cdot)\).
Indeed C.4.7 identifies the latter with the same actual contamination
derivative, and a norm limit has only one value. This does not extend the
finite-network derivative conclusions of C.4.6 to other base laws.

The same argument supplies the integral representation in every admissible
law direction. For finite \(\lambda,\nu\), the derivative of a mixture has
value \(\int I_{h,\lambda}\,d(\nu-\lambda)\) and Taylor remainder at most
\(M\epsilon^2\|\nu-\lambda\|_{\rm TV}^2/2\). Pass first through the mesh
limit. Next approximate both laws by the same finite quantization map.
Quantization contracts total variation and has uniformly vanishing transport
error. The displayed integral converges by joint continuity, so
\[
 \left.\frac d{dt}F((1-t)Q+t\nu)\right|_{t=0+}
                  =\int I_Q(z)\,d(\nu-Q)(z).                         \tag{C.4.8.P11}
\]
Here the segment is restricted to the region where the estimate applies;
\(\nu\) need not itself lie there if only a short initial part is used.
Apply this identity at every point of an admissible segment. Joint continuity
of \(I\) makes its directional derivative continuous, hence gives the
fundamental theorem of calculus on that segment. For a general zero-mass
direction \(\eta\) admitting a positive segment length \(a\), set
\(\nu=Q+a\eta\) and rescale (C.4.8.P11). This covers all directions used in
replacement rectangles and in conditional-expectation telescoping.

Likewise the mixed finite-difference bound
\[
 \|F(Q+s\sigma+t\tau)-F(Q+s\sigma)-F(Q+t\tau)+F(Q)\|_{\mathcal C}
             \le Mst\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}              \tag{C.4.8.P12}
\]
passes from (C.4.8.P7) first in mesh and then through common quantization. All laws
on the rectangle must be probabilities in the open ball of radius
\(\delta_Y/2\). Its compact image has positive distance from the boundary;
fine quantizations therefore remain in the larger analytic region. The
argument takes only four value limits. No second derivative of the limiting
population flow is assumed or needed.

###### 4. A usable characterization of the signed field

For a finite law \(\lambda\), the source lemma in C.4.8.1 supplies an explicit
chronological Gaussian recursion for \(I_{h,\lambda}(z)\): append the atom
\(z\), differentiate its mass vector in direction \(\delta_z-\lambda\), and
propagate the displayed lower and upper coordinate responses together with
both covariance responses, all residual responses, and both response
coefficient arrays. Expectations are differentiated by the Gaussian covariance
formula, including at singular covariance. All initial mass responses are
zero. At the last node the resulting full derivative of
\(\mathbb E_2[c\phi(Z(u))]\) is \(I_{h,\lambda}(z)(\sqrt2u)\).

For any finite quantizations \(q_j:\mathcal Z\to\mathcal Z\) with
\(\sup_z d(q_jz,z)\to0\), chosen so the base laws stay in the admitted ball,
the actual field is characterized by
\[
 I_\mu(z)=\lim_{j\to\infty}\lim_{h\to0}
       I_{h,(q_j)_\#\mu}(q_jz)\quad\hbox{in }\mathcal C.             \tag{C.4.8.P13}
\]
The inner limit exists by (C.4.8.P8), and the outer limit follows uniformly in
\(z\) from joint continuity. The result is independent of the quantizations
and meshes by (C.4.8.P9). Thus (C.4.8.P13), with the complete source derivative recursion,
defines a well-posed evolution-and-limit procedure for the influence. It
retains all three trained blocks and both initialized action orientations.
It does not replace those objects by an undetermined endpoint derivative.


##### C.4.8.3. A Hilbert sampling lemma

###### Statement


Let \(\mathcal Z\) be a compact metric space, let \(H\) be a separable real Hilbert space, and let \(\mu\in\mathcal P(\mathcal Z)\). Equip the probability laws with \(W_1\). Let \(U\) be a \(W_1\)-open neighborhood of \(\mu\), and let \(F:U\to H\) be bounded and \(W_1\)-continuous. Use the total-variation norm convention \(\|\delta_z-\delta_{z'}\|_{\rm TV}\le2\).

Assume the following three properties.

1. **Actual first mixture response.** There is a jointly Borel kernel \(I:U\times\mathcal Z\to H\), with \(\int I_Q\,dQ=0\), such that on every affine probability segment \(Q_t=Q+t\eta\) contained in \(U\), \(t\mapsto F(Q_t)\) is continuously differentiable, including one-sided endpoint derivatives, and

   \[
   \frac d{dt}F(Q_t)=\int I_{Q_t}(z)\,\eta(dz).
   \tag{C.4.8.R1}
   \]

   Here \(\eta\) is a zero-mass finite signed measure, and the stated Bochner integrals exist. In particular,

   \[
   I_Q(z)=\left.\frac d{d\epsilon}
   F((1-\epsilon)Q+\epsilon\delta_z)\right|_{\epsilon=0+}.
   \tag{C.4.8.R2}
   \]

2. **Uniform mixed second differences.** There is \(M<\infty\) such that, whenever the affine rectangle \(Q+s\eta+t\xi\), \(0\le s,t\le1\), consists of probability laws in \(U\),

   \[
   \|F(Q+\eta+\xi)-F(Q+\eta)-F(Q+\xi)+F(Q)\|_H
   \le M\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}.
   \tag{C.4.8.R3}
   \]

3. **Continuity at the sampling law.** As \(Q\to\mu\) in \(W_1\), with \(Q\in U\),

   \[
   \|I_Q-I_\mu\|_{L^2(\mu;H)}\longrightarrow0.
   \tag{C.4.8.R4}
   \]

The norm in (C.4.8.R4) uses the fixed law \(\mu\). Joint continuity of \((Q,z)\mapsto I_Q(z)\) near \(\{\mu\}\times\mathcal Z\) is a sufficient condition. The uniform local bounds needed for its integrability follow in the proof. A bounded second derivative in total variation implies (C.4.8.R3), but no second derivative of \(F\) is assumed here.

Let \(Z_1,Z_2,\ldots\) be iid with law \(\mu\), and put \(\mu_m=m^{-1}\sum_{i=1}^m\delta_{Z_i}\). There exist a \(W_1\)-open neighborhood \(V\) of \(\mu\), with \(V\subset U\), and a bounded Borel function \(\widetilde F:\mathcal P(\mathcal Z)\to H\), equal to \(F\) on \(V\), such that

\[
 \widetilde F(\mu_m)-F(\mu)
       =\frac1m\sum_{i=1}^m I_\mu(Z_i)+r_m,
 \qquad m\mathbb E\|r_m\|_H^2\longrightarrow0.
 \tag{C.4.8.R5}
\]

Moreover, \(\mathbb P(\mu_m\notin V)\le c_1e^{-c_2m}\) for constants \(c_1,c_2>0\). Consequently any globally defined finite-valued Borel extension \(\widehat F\) of \(F\) has the same expansion with \(\sqrt m\,r_m\to0\) in probability. The \(L^2\) assertion also holds for \(\widehat F\) if it is bounded, or more generally if

\[
 m\mathbb E\|\widehat F(\mu_m)-\widetilde F(\mu_m)\|_H^2
       \longrightarrow0.
 \tag{C.4.8.R6}
\]

In particular, the assertion for an actual endpoint statistic presupposes that this statistic is defined on all sample outcomes, or that an extension has explicitly been chosen.

The covariance operator of the limiting Gaussian is

\[
 C_\mu h=\int\langle I_\mu(z),h\rangle_H I_\mu(z)\,\mu(dz),
 \qquad \operatorname{tr}C_\mu=\int\|I_\mu(z)\|_H^2\,\mu(dz),
 \tag{C.4.8.R7}
\]

and

\[
 \sqrt m\,[\widetilde F(\mu_m)-F(\mu)]
      \Rightarrow\mathcal N_H(0,C_\mu),\qquad
 m\mathbb E\|\widetilde F(\mu_m)-F(\mu)\|_H^2
      \longrightarrow\operatorname{tr}C_\mu.
 \tag{C.4.8.R8}
\]

The distributional conclusion transfers to every extension above; the second-moment conclusion transfers under (C.4.8.R6).

###### Proof: line estimates and localization

If \(\mathcal Z\) has one point, every empirical law equals \(\mu\), and centering gives \(I_\mu=0\). All conclusions then hold directly. Assume its diameter \(D\) is positive.

First, (C.4.8.R3) gives the required Taylor estimate using only the first derivative. On a segment \(Q_t=Q+t\eta\), write \(f(t)=F(Q_t)\). For \(0\le a<b<1\), apply (C.4.8.R3) to the rectangle with base \(Q_a\) and increments \((b-a)\eta\) and \(h\eta\). Divide by \(h>0\) and let \(h\downarrow0\). Equation (C.4.8.R1) gives

\[
 \|f'(b)-f'(a)\|_H\le M(b-a)\|\eta\|_{\rm TV}^2.
\]

One-sided continuity covers the endpoints. Integrating the inequality proves

\[
 \left\|F(Q+\eta)-F(Q)-\int I_Q\,d\eta\right\|_H
       \le\frac M2\|\eta\|_{\rm TV}^2.
 \tag{C.4.8.R9}
\]

Choose \(r_{\rm loc}>0\) such that \(B_{W_1}(\mu,r_{\rm loc})\subset U\). Write \(B=\sup_U\|F\|_H\) and let \(\tau=\min\{1/2,r_{\rm loc}/(8D)\}\). If \(W_1(Q,\mu)<3r_{\rm loc}/4\), the contaminations \((1-s)Q+s\delta_z\), \(0\le s\le\tau\), stay in \(U\), since their distance from \(Q\) is at most \(sD\). By (C.4.8.R2) and (C.4.8.R9),

\[
 \|I_Q(z)\|_H\le 2B/\tau+2M\tau=:L
 \quad\text{for all such }Q\text{ and all }z.
 \tag{C.4.8.R10}
\]

This also proves the local square integrability used in (C.4.8.R4).

To construct a cutoff, choose a finite \(\epsilon\)-net \(z_1,\ldots,z_N\) in \(\mathcal Z\), with \(\epsilon=r_{\rm loc}/16\), and define

\[
 a_j(z)=(2\epsilon-d(z,z_j))_+,\qquad
 \psi_j(z)=\frac{a_j(z)}{\sum_k a_k(z)}.
\]

The denominator is at least \(\epsilon\). Thus the \(\psi_j\) are continuous, take values in \([0,1]\), and sum to one. Sending \(z\) to \(z_j\) with probabilities \(\psi_j(z)\) couples any law \(Q\) with \(Q^d=\sum_j(Q\psi_j)\delta_{z_j}\) at cost at most \(2\epsilon\). Coupling common discrete mass identically and the remainder at cost at most \(D\) gives

\[
 W_1(Q,\mu)\le4\epsilon+
              \frac D2\sum_j|Q\psi_j-\mu\psi_j|.
 \tag{C.4.8.R11}
\]

Put \(b=r_{\rm loc}/(2DN)\). Choose a smooth \(\chi_0:\mathbb R\to[0,1]\) equal to one on \([-1/2,1/2]\), positive on \((-1,1)\), and zero off that interval. Define

\[
 \chi(Q)=\prod_j\chi_0\bigl((Q\psi_j-\mu\psi_j)/b\bigr),
 \qquad V=\{Q:\max_j|Q\psi_j-\mu\psi_j|<b/2\}.
 \tag{C.4.8.R12}
\]

The support of \(\chi\) is contained in \(\{Q:W_1(Q,\mu)\ler_{\rm loc}/2\}\) by (C.4.8.R11); \(\chi=1\) on \(V\). Its first and second law derivatives have bounded scalar kernels, since they are finite sums of products of the \(\psi_j\) and derivatives of \(\chi_0\). Let \(a_Q(z)\) denote its first kernel. Define

\[
 \widetilde F(Q)=\chi(Q)F(Q)\quad(Q\in U),\qquad
 \widetilde F(Q)=0\quad(Q\notin U).
\]

Its centered first kernel is obtained by subtracting its \(Q\)-mean from

\[
 A_Q(z)=\chi(Q)I_Q(z)+F(Q)a_Q(z)
 \tag{C.4.8.R13}
\]

on \(U\), and setting it to zero elsewhere. This kernel is uniformly bounded by (C.4.8.R10), boundedness of \(F\), and the cutoff derivative bounds. The product and its first derivatives extend across the cutoff boundary because \(\chi\) and its derivatives vanish there and the other factors are uniformly bounded on a larger open neighborhood. Thus the first mixture calculus remains valid globally. On \(V\), the centered first kernel of \(\widetilde F\) is exactly \(I_Q\), so (C.4.8.R4) is preserved.

For completeness, the mixed finite-difference bound also survives this extension without any second derivative of \(F\). On a rectangle whose corners are indexed by \(00,10,01,11\), the exact product identity is

\[
\begin{aligned}
 \Delta_{12}(\chi F)
  ={}&\chi_{11}\Delta_{12}F
    +(\chi_{11}-\chi_{10})(F_{10}-F_{00})\\
   &+(\chi_{11}-\chi_{01})(F_{01}-F_{00})
    +(\Delta_{12}\chi)F_{00}.
\end{aligned}
 \tag{C.4.8.R14}
\]

On any rectangle in \(B_{W_1}(\mu,3r_{\rm loc}/4)\), (C.4.8.R3), the first derivative bound (C.4.8.R10), the bounded first and second derivatives of \(\chi\), and boundedness of \(F\) bound (C.4.8.R14) by

\[
 M_*\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}
 \tag{C.4.8.R15}
\]

for a constant \(M_*\) independent of the rectangle.

For a general probability rectangle, its parameter domain is compact. The inverse images of \(B_{W_1}(\mu,3r_{\rm loc}/4)\) and of the complement of the support of \(\chi\) are an open cover of that domain. A sufficiently fine rectangular grid has every cell inside one member of this cover: choose parameter balls whose doubled balls lie in a member of the cover, take a finite subcover of the original balls, and use cells of diameter smaller than their minimum radius. In the first kind of cell (C.4.8.R15) applies; in the second the extended function is zero. Summing mixed cell differences telescopes to the difference on the whole rectangle. The products of cell side lengths sum to one, giving the global bound (C.4.8.R15). Hence \(\widetilde F\) has globally bounded first kernel and second mixed differences.

Finally, a variable in \([0,1]\) has centered log moment-generating function at most \(\lambda^2/8\): its second derivative is a tilted variance, at most \(1/4\), and its value and first derivative vanish at zero. Exponential Markov and independence therefore give

\[
 \mathbb P\bigl(|\mu_m\psi_j-\mu\psi_j|\ge b/2\bigr)
       \le2e^{-mb^2/2}.
\]

The union bound yields

\[
 \mathbb P(\mu_m\notin V)\le2N e^{-mb^2/2}.
 \tag{C.4.8.R16}
\]

###### Proof: the global sampling calculation

It remains to prove (C.4.8.R5) for a bounded functional defined on all probability laws, with a uniformly bounded centered first kernel and mixed difference bound \(M_*\). In this part write \(G\) for that functional and \(J_Q\) for its first kernel. We will apply the result to \(G=\widetilde F\), whose kernel satisfies \(J_\mu=I_\mu\).

The finite-test construction (C.4.8.R11), repeated with an arbitrarily small \(\epsilon\), shows that empirical laws converge to \(\mu\) in \(W_1\) in probability. Indeed, each finite set of bounded continuous empirical averages converges by its variance bound; (C.4.8.R11) then makes the remaining deterministic error arbitrarily small. The same conclusion holds for \(m^{-1}\mu+m^{-1}\sum_{i=2}^m\delta_{Z_i}\).

###### Bias

Define

\[
 \nu_i=(1-i/m)\mu+m^{-1}\sum_{j=1}^i\delta_{Z_j},
 \qquad 0\le i\le m.
\]

Every segment from \(\nu_{i-1}\) to \(\nu_i\) consists of probability laws. Equation (C.4.8.R9), now with constant \(M_*\), gives

\[
 G(\nu_i)-G(\nu_{i-1})
 =m^{-1}\int J_{\nu_{i-1}}(z)(\delta_{Z_i}-\mu)(dz)+R_i,
 \qquad\|R_i\|_H\le2M_*/m^2.
\]

Conditional on the previous samples, the first term has mean zero. Consequently

\[
 b_m:=\mathbb EG(\mu_m)-G(\mu),\qquad
 \|b_m\|_H\le2M_*/m.
 \tag{C.4.8.R17}
\]

###### Higher-order Hoeffding components

For any square-integrable \(H\)-valued statistic \(T=T(Z_1,\ldots,Z_m)\), define

\[
 T_S=\sum_{A\subset S}(-1)^{|S|-|A|}
                 \mathbb E[T\mid Z_i:i\in A],
 \qquad S\subset\{1,\ldots,m\}.
 \tag{C.4.8.R18}
\]

Finite inclusion--exclusion gives \(T=\sum_ST_S\). Each nonempty component has zero conditional mean when any coordinate in its index set is integrated out: terms in (C.4.8.R18) that include that coordinate cancel the terms that omit it. Choosing a coordinate in the symmetric difference of two distinct index sets proves their orthogonality in \(L^2\). Thus

\[
 R^{\rm H}:=T-\mathbb ET-
       \sum_i(\mathbb E[T\mid Z_i]-\mathbb ET)=\sum_{|S|\ge2}T_S
\]

is orthogonal to constants and to all sums of one-coordinate functions.

Let \(T^{(i)}\) replace \(Z_i\) by an independent copy, and let
\(D_{ij}T=T-T^{(i)}-T^{(j)}+T^{(ij)}\). A double replacement kills components not containing both indices. For a component containing both, the four replacement terms have equal second moments and are pairwise orthogonal, by conditioning on a coordinate where they differ. Components with distinct index sets also remain orthogonal after replacement. Hence

\[
 \mathbb E\|D_{ij}T\|_H^2
       =4\sum_{S\supset\{i,j\}}\mathbb E\|T_S\|_H^2,
\]

and summing over pairs gives

\[
 \mathbb E\|R^{\rm H}\|_H^2
       \le\frac14\sum_{i<j}\mathbb E\|D_{ij}T\|_H^2.
 \tag{C.4.8.R19}
\]

Apply this with \(T_m=G(\mu_m)\). Replacing observations \(i\) and \(j\) gives a probability rectangle with edge measures \(m^{-1}(\delta_{Z_i'}-\delta_{Z_i})\) and \(m^{-1}(\delta_{Z_j'}-\delta_{Z_j})\). Therefore

\[
 \|D_{ij}T_m\|_H\le4M_*/m^2,
 \qquad
 \mathbb E\|R_m^{\rm H}\|_H^2\le2M_*^2/m^2.
 \tag{C.4.8.R20}
\]

###### The first projection

By symmetry, using the version of conditional expectation obtained by integrating over the other samples, write

\[
 h_m(z)=m\{\mathbb E[T_m\mid Z_1=z]-\mathbb ET_m\},
 \qquad \int h_m\,d\mu=0.
\]

Let \(Q_m=m^{-1}\mu+m^{-1}\sum_{j=2}^m\delta_{Z_j}\). The law \(Q_m+m^{-1}(\delta_z-\mu)\) is a probability measure for every \(z\). Its Taylor expansion around \(Q_m\) has remainder at most \(2M_*/m^2\). Averaging over the other samples, subtracting the \(\mu\)-average over \(z\), and multiplying by \(m\) gives

\[
 h_m(z)=\mathbb E\left[J_{Q_m}(z)-\int J_{Q_m}\,d\mu\right]+e_m(z),
 \qquad \sup_z\|e_m(z)\|_H\le4M_*/m.
 \tag{C.4.8.R21}
\]

The laws \(Q_m\to\mu\) in \(W_1\) in probability. Assumption (C.4.8.R4), preserved near \(\mu\) by localization, and the globally bounded first kernel imply

\[
 \mathbb E\|J_{Q_m}-J_\mu\|_{L^2(\mu;H)}^2\longrightarrow0.
\]

To justify the expectation, the norm tends to zero in probability by continuity and is uniformly bounded; splitting at any fixed threshold proves convergence of its expectation. Jensen's inequality in (C.4.8.R21), together with \(\mu J_\mu=0\), now proves

\[
 \|h_m-J_\mu\|_{L^2(\mu;H)}\longrightarrow0.
 \tag{C.4.8.R22}
\]

###### The exact remainder identity

The Hoeffding decomposition gives

\[
 T_m-G(\mu)=b_m+m^{-1}\sum_i h_m(Z_i)+R_m^{\rm H}.
\]

Define \(r_m\) by subtracting \(m^{-1}\sum_iJ_\mu(Z_i)\). The bias, higher-order component, and centered one-coordinate sum are mutually orthogonal in \(L^2\). Independence of the summands gives the exact identity

\[
 m\mathbb E\|r_m\|_H^2
   =m\|b_m\|_H^2+m\mathbb E\|R_m^{\rm H}\|_H^2
                         +\|h_m-J_\mu\|_{L^2(\mu;H)}^2.
 \tag{C.4.8.R23}
\]

The first two terms are at most \(6M_*^2/m\) in total by (C.4.8.R17) and (C.4.8.R20), and the last tends to zero by (C.4.8.R22). This proves (C.4.8.R5). No quantitative modulus in (C.4.8.R4) is needed.

On \(\{\mu_m\in V\}\), any extension \(\widehat F\) in the statement equals \(\widetilde F\). Equation (C.4.8.R16) therefore proves the transfer in probability. If \(\widehat F\) is bounded, multiplying its squared uniform difference from \(\widetilde F\) by \(m\mathbb P(\mu_m\notin V)\) proves (C.4.8.R6). This completes the sampling expansion and its localization claims.

###### Covariance, spatial tests, and the Hilbert CLT

Set \(X=I_\mu(Z)\). It is centered and square integrable by (C.4.8.R10). The operator \(C_\mu h=\mathbb E[\langle X,h\rangle X]\) is positive and self-adjoint. For any orthonormal basis \((e_j)\), Tonelli and Parseval give

\[
 \sum_j\langle C_\mu e_j,e_j\rangle
       =\mathbb E\sum_j|\langle X,e_j\rangle|^2
       =\mathbb E\|X\|_H^2<\infty.
\]

Thus \(C_\mu\) is trace class and has the trace in (C.4.8.R7). Its nonnegative eigenvalues \(\lambda_j\), with an orthonormal eigenbasis supplemented in its kernel if needed, define a centered Gaussian \(\mathcal G=\sum_j\sqrt{\lambda_j}\,N_je_j\), where the \(N_j\) are independent standard normals. Summability of \(\lambda_j\) gives convergence in \(L^2(H)\), and its covariance is \(C_\mu\). Degenerate covariance is allowed.

Here is a direct projection proof of the Hilbert CLT. Put \(S_m=m^{-1/2}\sum_iI_\mu(Z_i)\). For any scalar projection \(Y=\langle X,h\rangle\), centering and finite variance give

\[
 \mathbb E e^{itY/\sqrt m}
       =1-\frac{t^2\mathbb EY^2}{2m}+o(m^{-1}).
\]

For the remainder, set \(q(u)=e^{iu}-1-iu+u^2/2\). Then \(q(u)=o(u^2)\) at zero and \(|q(u)|\le C u^2\) for all real \(u\). For fixed \(t\), \(mq(tY/\sqrt m)\to0\) pointwise and its absolute value is at most \(Ct^2Y^2\); dominated convergence proves the displayed expansion. Taking the \(m\)-th power proves the scalar Gaussian characteristic-function limit. Applied to every linear combination of a fixed finite number of coordinates, this proves the finite-dimensional CLT.

For a finite-dimensional orthogonal projection \(\Pi_N\) increasing to the identity, independence and centering give

\[
 \mathbb E\|(1-\Pi_N)S_m\|_H^2
       =\mathbb E\|(1-\Pi_N)X\|_H^2\longrightarrow0
\]

uniformly in \(m\). The Gaussian has the same tail second moment. For any bounded 1-Lipschitz function on \(H\), replacing its argument by \(\Pi_N\) changes either expectation by at most the square root of that tail second moment. Let \(m\to\infty\) at fixed \(N\), using the finite-dimensional conclusion, and then let \(N\to\infty\). This proves weak convergence \(S_m\Rightarrow\mathcal G\) on the separable Hilbert space. Equation (C.4.8.R5) supplies an error tending to zero in \(L^2\) after multiplication by \(\sqrt m\), so proves the first part of (C.4.8.R8). Cauchy--Schwarz, \(\mathbb E\|S_m\|^2=\operatorname{tr}C_\mu\), and (C.4.8.R5) prove its second part.

If \(H=L^2(\mathbb S^1,\lambda)\) for a finite circle measure \(\lambda\), these statements apply to spatial tests. For \(\psi_1,\ldots,\psi_k\in H\), the limiting covariance matrix of the integrals against these tests is

\[
 \Sigma_{ab}=\int_{\mathcal Z}
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_a(x)\,\lambda(dx)\right)
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_b(x)\,\lambda(dx)\right)
      \mu(dz)=\langle C_\mu\psi_a,\psi_b\rangle_H.
 \tag{C.4.8.R24}
\]

A jointly measurable representative of \(I_\mu\in L^2(\mu;H)\) defines the spatial covariance kernel

\[
 c_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,\mu(dz)
 \tag{C.4.8.R25}
\]

as an element of \(L^2(\lambda\otimes\lambda)\): the integrand's norm in that space is \(\|I_\mu(z)\|_H^2\), which is integrable. Its integral operator is \(C_\mu\), by Fubini and Cauchy--Schwarz. Formula (C.4.8.R24) concerns continuous linear spatial tests; point evaluation requires additional regularity beyond \(L^2\).

All statements treat \(F\) and its kernel as deterministic. If they retain a random initialization environment independent of the samples, the theorem applies conditional on that environment when its hypotheses hold there. An unconditional Gaussian limit additionally requires the conditional covariance to be deterministic; otherwise the conditional limits generally form a Gaussian mixture.

##### C.4.8.4. Covariance and finite-network interpretation

###### Sampling and the mean-square strengthening


Apply the sampling lemma in C.4.8.3 to the actual map on
\(\{Q:W_1(Q,\nu_*)<\delta_Y/2\}\), with kernel (C.4.8.P9)--(C.4.8.P11) and second
difference bound (C.4.8.P12). For each fixed \(\mu\) in the smaller requested
ball, choose a \(W_1\)-ball around \(\mu\) whose closure is inside this
analytic region. The lemma's finite-continuous-test cutoff defines a global
bounded map \(G_\mu\), equal to \(F\) near \(\mu\), with the same actual
influence there. Its proof gives
\[
 m\mathbb E\left\|G_\mu(\mu_m)-F(\mu)
                  -\frac1m\sum_iI_\mu(Z_i)\right\|_H^2\to0,
 \qquad
 \Pr\{G_\mu(\mu_m)\ne\overline F(\mu_m)\}\le C_\mu e^{-c_\mu m}.    \tag{C.4.8.P14}
\]
The mismatch bound refers to the cutoff's finite-test neighborhood, which
lies inside \(U_Y\). Both maps are uniformly bounded, so
\[
 m\mathbb E\|G_\mu(\mu_m)-\overline F(\mu_m)\|_H^2
                         \le C_\mu m e^{-c_\mu m}\to0.
\]
This proves (C.4.8.P4) with exactly the extension (C.4.8.P3). In particular empirical
laws outside \(U_Y\) are exponentially rare and do not change any asserted
limit. No labels on the testing circle have been introduced.

For arbitrary \(g,h\in H\), the covariance acts as
\[
 \langle\Sigma_\mu g,h\rangle_H
   =\int\langle I_\mu(z),g\rangle_H
                \langle I_\mu(z),h\rangle_H\,d\mu(z).                 \tag{C.4.8.P15}
\]
Thus the joint limiting fluctuations of the spatial averages against any
finite collection of tests are centered Gaussian with these covariances.
Since the field is continuous and bounded on the compact atom/input product,
one may equivalently use the continuous kernel
\[
 K_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,d\mu(z),
\quad (\Sigma_\mu g)(x)=\int K_\mu(x,x')g(x')\,d\rho(x').             \tag{C.4.8.P16}
\]
Fubini is justified by boundedness and the finite measures. The operator is
positive, self-adjoint and trace class, with
\(\operatorname{Tr}\Sigma_\mu=\int\|I_\mu(z)\|_H^2d\mu(z)\).
No diagonal form, positive rank, or nondegeneracy is imposed.

The sampling lemma proves the Hilbert CLT, giving (C.4.8.P5). It also gives the
separate strengthening requested here without further label or density
assumptions: put \(S_m=m^{-1}\sum_iI_\mu(Z_i)\). Independence and centering
give \(\mathbb E\|S_m\|_H^2=\operatorname{Tr}\Sigma_\mu/m\). By
Cauchy--Schwarz and (C.4.8.P4),
\[
 m|\mathbb E\langle S_m,r_m\rangle_H|
 \le\sqrt{\operatorname{Tr}\Sigma_\mu}\,
                \sqrt{m\mathbb E\|r_m\|_H^2}\to0.
\]
Expanding the squared norm therefore proves
\[
 \mathbb E\|\overline F(\mu_m)-F(\mu)\|_H^2
                 =\frac{\operatorname{Tr}\Sigma_\mu}{m}+o(m^{-1}).   \tag{C.4.8.P17}
\]
The bounded extension and exponential exceptional-event estimate are essential
parts of this statement. It is not a moment theorem for finite-width errors.

###### 6. Actual finite gradient flow, including exceptional laws

For every finite labeled law and every finite initialized array, the smooth
finite-dimensional physical GF exists through \(T\). Here is a direct bound
that also covers laws outside \(U_Y\). Use the normalized finite norms matching
(C.4.8.P1), write \(c_{n,0}\) for the actual initialized readout, and
\(A_n=A_{n,0}+K_n\). Explicitly, vector and full-row norms below are
\(\|v\|_{(n)}=(n^{-1}\sum_{j=1}^n|v_j|^2)^{1/2}\), with the Euclidean
two-vector norm inside the sum for a first row. The matrix increment norm is
the ordinary Frobenius norm \(\|K_n\|_{\rm HS}=\|K_n\|_F\), and the
action norm is the ordinary spectral norm. These are precisely the finite
raw metric conventions of C.4.7; the middle update is
\(-2n^{-1}\int r\Delta h^T\,d\mu_m\), whose Frobenius norm is bounded by
the product of the two normalized vector norms. Since the gates have absolute
value at most one,
\[
 \|\dot c_n\|\le2(\|c_n\|+Y),\qquad
 \|\dot K_n\|_{\rm HS}\le2(\|c_n\|+Y)\|c_n\|,
\]
\[
 \|\dot w_n\|\le2(\|c_n\|+Y)
             (\|A_{n,0}\|+\|K_n\|_{\rm HS})\|c_n\|.               \tag{C.4.8.P18}
\]
The first inequality gives
\(\|c_n(t)\|\le(\|c_{n,0}\|+Y)e^{2t}-Y\); integration then bounds
\(K_n\) and \(w_n\) on each finite time interval. These constants may
depend on the initialized array and \(n\); no uniform bound is needed here.
A solution of a locally Lipschitz finite-dimensional equation that remains
bounded on each such interval extends through its endpoint: on a containing
compact ball the vector field is bounded and locally Lipschitz, giving a
Cauchy endpoint and a local continuation. This proves global finite-time
existence. Smooth dependence on the finite data and initialization gives
measurability of the \(H\)-valued prediction statistic; the bounds ensure the
local dependence can be continued through \(T\).

Fix \(m\), and condition on \((Z_1,\ldots,Z_m)\). On the event
\(E_m=\{\mu_m\in U_Y\}\), this is a separately fixed finite training law,
and independence leaves the specified initialization distribution unchanged.
C.4.7.NW1 therefore gives
\[
 \|f_{n,\mu_m}(T,\cdot)-F(\mu_m)\|_H\to0
 \quad\hbox{in initialization probability, conditionally on each such law}.
\]
For every fixed \(m\), bounded convergence after conditioning implies
\[
 \mathbb E\left[\mathbf1_{E_m}
     \min\{2,\sqrt m\|f_{n,\mu_m}(T)-F(\mu_m)\|_H\}\right]\to0.    \tag{C.4.8.P19}
\]
On \(E_m^c\), the difference of any two bounded-Lipschitz test values is at
most two. No width limit on that event is asserted. With
\(X_{n,m}=\sqrt m(f_{n,\mu_m}(T)-F(\mu))\) and
\(X_m=\sqrt m(\overline F(\mu_m)-F(\mu))\), (C.4.8.P19) yields
\[
 \limsup_{n\to\infty}
 d_{\rm BL}(\operatorname{Law}(X_{n,m}),\operatorname{Law}(X_m))
                         \le2\Pr(E_m^c).                             \tag{C.4.8.P20}
\]
The right-hand side tends to zero exponentially by (C.4.8.P14). The triangle
inequality, (C.4.8.P5), and then \(m\to\infty\) prove (C.4.8.P6). This argument keeps
the actual finite random initial readout and invokes no finite-network tangent
limit, no rate in width, and no simultaneous width/sample scaling.
