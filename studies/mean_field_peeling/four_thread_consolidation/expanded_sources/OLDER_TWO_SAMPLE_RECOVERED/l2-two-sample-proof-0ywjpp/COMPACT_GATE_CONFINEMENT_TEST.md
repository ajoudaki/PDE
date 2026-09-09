# Compact first gates: confinement, a frozen reservoir, and the remaining top-layer gap

This is a bounded activation-design assessment of the system in the prompt. Its mathematical source is only that prompt. No project material, history, other agents, experiments, or external mathematical sources were used. The procedural math skills guided the claim separation and adversarial checks. No limiting equation, sufficient convergence criterion, control-integrability conclusion, or uniqueness result is asserted.

Fixed smooth saturation is an activation candidate only. It is not being called an accepted relaxation of a no-clipping requirement, and this note claims no successful activation design. Such a result would still require a frozen reservoir to coexist with a positive-mass moving population at the intended trajectory and width scales, together with the full nonlazy and nonaffine obligations. The initial finite-width motion verified below does not discharge those obligations. Near-linear alternatives are outside this sidecar.

The main geometric claim is correct. Write \(\eta=|\rho|\). Every absolutely continuous solution of the controlled two-coordinate equation below satisfies
\[
 |z_a(t)|\le \max\{R,|z_a(0)|\}+2\eta R
 \le |z_a(0)|+(1+2\eta)R.                                      \tag{1}
\]
For \(0<\eta<1\), the constants are optimal when only the displayed initial coordinate is retained; a sharper, initial-state-dependent classification is given below. Initially saturated pairs are an actual frozen reservoir. For \(-1<\rho<1\), its same-sign and opposite-sign groups give a strictly positive, time-uniform first-feature Gram bound, subject to the explicit finite-sample occupancy condition. At antiparallel inputs the population Gram has rank one, precisely in the label direction; the empirical reservoir guarantees a positive coefficient when its frozen group is occupied.

These results do yield an exact conserved part of the second-layer weights and a stronger weighted dissipation estimate. The conserved part is invisible on the two samples. Neither result bounds the dynamically relevant upper-layer states uniformly in time, supplies a uniform upper-layer learning rate, or establishes persistent nonlinear feature learning.

## 1. Fixed activation and exact first-coordinate equation

Fix \(R>0\), independently of width, inputs, and their correlation. Let \(p\in C^\infty(\mathbb R)\) be even, nonnegative, supported on \([-R,R]\), and positive on \((-R,R)\). Set
\[
 \phi_1(s)=\int_0^s p(u)\,du,\qquad
 A=\int_0^R p(u)\,du>0.
\]
Thus \(\phi_1\) is odd and nondecreasing, strictly increasing in the interior, and equals \(\pm A\) on the two saturation intervals. It is globally nonlinear, although necessarily constant outside the support of its derivative. For example, a fixed even smooth bump provides such a \(p\); no parameter clipping or width-dependent activation is involved.

Use \(z^1_{ja}=W^1_jx_a\), \(h^1_{ja}=\phi_1(z^1_{ja})\), \(z^2_{ia}=(W^2h^1_a)_i\), and \(h^2_{ia}=g(z^2_{ia})\), where \(g=\phi_2\). Let \(r_a=f_a-y_a\), write \(r=(r_1,r_2)^T\), and take \(y=(1,-1)^T\). Both hidden layers have width \(n\), and
\[
 f_a=\frac1n w^Th^2_a,\qquad
 W^1_{ij}(0)\sim N(0,1/d),\quad
 W^2_{ij}(0)\sim N(0,1/n),\quad
 w_i(0)\sim N(0,n^{-2}),
\]
with all initial entries independent. The inputs satisfy \(\|x_a\|^2=d\) and \(x_1^Tx_2/d=\rho\). The prescribed dynamics, with entrywise products denoted by \(\odot\), are
\[
\begin{aligned}
 \delta^2_a&=w\odot g'(z^2_a),&
 \delta^1_a&=p(z^1_a)\odot (W^2)^T\delta^2_a,\\
 \dot W^1&=-\frac2d\sum_a r_a\delta^1_ax_a^T,&
 \dot W^2&=-\frac2n\sum_a r_a\delta^2_a(h^1_a)^T,&
 \dot w&=-2\sum_a r_ah^2_a.
\end{aligned}
\]
For a first-layer neuron \(j\), define
\[
 b_{ja}=\left[(W^2)^T\bigl(w\odot g'(z^2_a)\bigr)\right]_j,
 \qquad q_{ja}=-2r_a b_{ja}.
\]
The prescribed RawGF gives, exactly,
\[
 \frac{d}{dt}\binom{z^1_{j1}}{z^1_{j2}}
 =C\,\operatorname{diag}\bigl(p(z^1_{j1}),p(z^1_{j2})\bigr)
   \binom{q_{j1}}{q_{j2}},\qquad
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.              \tag{2}
\]
Indeed, multiplying the first-layer update by \(x_b\) replaces \(x_a^Tx_b/d\) by \(C_{ba}\). In particular, all scaling factors in (2) come from the stated dynamics.

The geometric argument treats an arbitrary \(q\in L^1([0,T];\mathbb R^2)\) and an absolutely continuous solution of (2), for each finite \(T\). There is no bound on the size of this integral and no restriction on switching. This is a hypothesis of the abstract control test, not a conclusion that the network's effective \(q_j\) belongs to any global \(L^p\) space. For a finite classical network trajectory the argument applies on each compact interval on which its parameters are finite.

## 2. Frozen pairs and confinement under arbitrary switching

Call
\[
 \mathcal F=\{(u,v): |u|\ge R,\ |v|\ge R\}
\]
the frozen set. Equality at a support endpoint is included because \(p(\pm R)=0\).

First, a solution starting at any \(z_*\in\mathcal F\) stays there. Here is a direct argument that does not require a uniqueness assertion. Since \(p\) is globally Lipschitz and vanishes in both coordinates of \(z_*\), there is a fixed \(K\) such that
\[
 |\dot z(t)|\le K|q(t)|\,|z(t)-z_*|.
\]
The associated integral inequality, with zero initial distance, forces that distance to remain zero: multiplying the usual scalar integral majorant by \(\exp(-K\int_0^t|q|)\) proves this directly. Applying the same argument backwards from a hypothetical finite hitting time shows that a solution starting outside \(\mathcal F\) cannot enter \(\mathcal F\) in finite time. These statements concern the specified controlled paths only.

Consider any connected time interval on which \(z_1>R\). There \(p(z_1)=0\), so almost everywhere
\[
 \dot z_1=\rho p(z_2)q_2,\qquad
 \dot z_2=p(z_2)q_2,\qquad
 z_1-\rho z_2=\text{constant}.                              \tag{3}
\]
Unless the whole path is frozen, \(z_2\in(-R,R)\) throughout this interval. If the excursion starts after time zero, continuity gives \(z_1=R\) at its left endpoint. Consequently,
\[
 z_1(t)\le R+|\rho|\,|z_2(t)-z_2(\text{entry})|
          \le (1+2\eta)R.
\]
If it starts at time zero with \(z_1(0)\ge R\), the corresponding bound is \(z_1(t)\le z_1(0)+2\eta R\), including equality at the initial endpoint. Negative excursions use the same invariant and yield the analogous bound for \(-z_1\). Interchanging the coordinates proves (1).

This proof applies to each connected excursion interval separately. It does not sum excursion lengths or assume finitely many switches. Repeated returns therefore cannot accumulate an outward drift beyond (1). Negative correlations cause no problem because the excursion estimate uses \(|\rho|\). In particular, there is no \(1/(1-|\rho|)\) loss in this confinement bound.

### Sharp initial-state-dependent classification for \(-1<\rho<1\)

The following suprema range over all admissible controls and all finite times. A boundary supremum need not be attained.

* If \(z(0)\in\mathcal F\), the path is constant.
* If \(\rho=0\), each coordinate is scalar: an initially active coordinate stays in \((-R,R)\) and has supremum of its absolute value \(R\); an initially inactive coordinate stays at its initial value.
* Suppose \(0<\eta<1\). If both coordinates are initially active, the supremum of either coordinate's absolute value is exactly \((1+2\eta)R\).
* Suppose \(0<\eta<1\), coordinate \(a\) is initially inactive, and coordinate \(b\ne a\) is initially active. Put
  \[
  s=\operatorname{sign}(z_a(0)),\qquad
  k=s\bigl(z_a(0)-\rho z_b(0)\bigr).
  \]
  If \(k\ge(1+\eta)R\), the path is trapped on the initial line in that side strip, and the exact suprema are
  \[
  \sup |z_a|=k+\eta R,\qquad \sup |z_b|=R.                     \tag{4}
  \]
  If \(k<(1+\eta)R\), the path can reach the interior square; the exact supremum for either coordinate is \((1+2\eta)R\).

To verify the last alternatives, while coordinate \(a\) is inactive its signed value is \(k+s\rho z_b\). Its smallest possible limiting value with \(z_b\in(-R,R)\) is \(k-\eta R\). If this is at least \(R\), the side strip cannot be left. At equality, the only possible contact with the square would be a frozen corner, which cannot be reached in finite time. Varying \(z_b\) over the open interval gives (4). If \(k-\eta R<R\), the crossing \(z_a=sR\) occurs with \(z_b\) strictly inside its support, so a control acting through coordinate \(b\) can carry the path into the square.

Inside \((-R,R)^2\), both \(C\) and the gate matrix are invertible. Any smooth path in a compact subset of this square can be followed using
\[
 q=\operatorname{diag}(p(z))^{-1}C^{-1}\dot z.
\]
To reach a side strip, start just inside the desired side and use only the other coordinate's control; it crosses the side while that other gate remains positive. Choosing an exit near one corner and then moving the active coordinate almost to the opposite end gives \(|z_a|\) arbitrarily close to \(R+2\eta R\). All such constructions can keep the controlling gate a positive distance from its endpoints, so each approximating control has finite integral. They prove the asserted sharpness, without claiming an attainable frozen endpoint.

In particular, from \(z(0)=(0,0)\) the additive constant \(1+2\eta\) in a bound \(|z_a(t)|\le |z_a(0)|+cR\) cannot be lowered when \(\eta<1\). For initially far-out coordinates the additional \(2\eta R\) in (1) is also sharp, by choosing the other initial coordinate near the appropriate endpoint and traversing its active interval.

### Rank-one endpoints, including the physical antiparallel case

For \(\rho=\varepsilon\in\{-1,1\}\), there is a global invariant
\[
 k=z_1-\varepsilon z_2.
\]
Parameterize its line by \(u=z_1\), so \(z_2=\varepsilon(u-k)\). Motion is possible exactly on
\[
 (-R,R)\ \cup\ (k-R,k+R).                                \tag{5}
\]
If \(u(0)\) is outside this open union, the path is frozen. Otherwise its exact reachable set is the connected component of this union containing \(u(0)\), with the closure giving the sharp limiting bounds. To see attainability within a component, on any compact subinterval at least one gate is positive; choosing the two controls proportional to the two available gate coefficients realizes any prescribed scalar velocity with finite integral. A gap, or a touching point where both gates vanish, cannot be crossed. Thus merely touching open intervals are separate components.

This handles arbitrary initial states at both endpoints and also implies (1). Physical network coordinates have \(k=0\): at \(\rho=-1\), \(x_2=-x_1\) and \(z_2=-z_1\); at \(\rho=1\), \(x_2=x_1\) and \(z_2=z_1\). The physical bound improves to
\[
 |z_a(t)|\le\max\{R,|z_a(0)|\}.                           \tag{6}
\]
An initially active physical endpoint neuron remains active at every finite time to which the controlled argument applies. Its gate may nevertheless tend to zero as time tends to infinity. The \(\rho=1\) endpoint, excluded in the prompt, cannot fit distinct labels on identical inputs.

## 3. An actual frozen initial-neuron reservoir

Let \(F\) consist of first-layer neurons whose two initial coordinates lie in \(\mathcal F\). The preceding argument gives
\[
 z^1_{ja}(t)=z^1_{ja}(0),\quad
 p(z^1_{ja}(t))=0,\quad
 h^1_{ja}(t)=A\operatorname{sign}(z^1_{ja}(0))
 \qquad(j\in F).
\]
In fact the entire row \(W^1_j\) is fixed, since both terms in its RawGF update are zero. This is a reservoir selected at initialization and frozen by the fixed activation itself, not by an imposed constraint. Other first-layer rows and all second-layer rows remain governed by the stated trainable dynamics.

Let \(H^1(t)\in\mathbb R^{n\times2}\) have columns \(h^1_1,h^1_2\), and normalize the first-feature Gram by
\[
 G_1(t)=\frac1n(H^1(t))^TH^1(t).
\]
Among frozen neurons, let \(N_s\) count the same-sign corners \((+,+),(-,-)\), and \(N_o\) the opposite-sign corners \((+,-),(-,+)\). Their fixed contribution is
\[
 G_F=\frac{A^2}{n}
 \begin{pmatrix}N_s+N_o&N_s-N_o\\N_s-N_o&N_s+N_o\end{pmatrix},
 \qquad G_1(t)\succeq G_F.                                \tag{7}
\]
Its eigenvalues in the directions \((1,1)\) and \((1,-1)\) are \(2A^2N_s/n\) and \(2A^2N_o/n\). Hence
\[
 G_1(t)\succeq\gamma_n I_2,\qquad
 \gamma_n=\frac{2A^2}{n}\min(N_s,N_o),                    \tag{8}
\]
simultaneously for every time of the trajectory. Positivity requires both counts to be nonzero. A deterministic positive empirical bound for every finite Gaussian draw would be false. All four corner groups need not be occupied; one same-sign and one opposite-sign neuron suffice.

For \(-1<\rho<1\), each initial pair has density
\[
 \frac{1}{2\pi\sqrt{1-\rho^2}}
 \exp\!\left[-\frac{u^2-2\rho uv+v^2}{2(1-\rho^2)}\right],
\]
which is strictly positive everywhere. Each of the four open saturation corners therefore has positive probability. Write \(m_s>0\) and \(m_o>0\) for the total same-sign and opposite-sign saturation probabilities. Central symmetry makes the two probabilities within each pair equal, although equality between \(m_s\) and \(m_o\) is not needed. The population reservoir bound is
\[
 G_{1,\mathrm{pop}}(t)\succeq
 A^2\begin{pmatrix}m_s+m_o&m_s-m_o\\m_s-m_o&m_s+m_o\end{pmatrix}
 \succeq 2A^2\min(m_s,m_o)I_2.                             \tag{9}
\]
Here a population Gram means an expectation over an initial-neuron population evolved by the specified gate mechanism. Equation (9) uses only its unchanged frozen subset; it does not construct or identify an infinite-width limit.

The independent initial first-layer rows also give the elementary occupancy estimate
\[
 \Pr(\gamma_n>0)\ge
 1-(1-m_s)^n-(1-m_o)^n.
\]
For a quantitative lower bound, the variance of \(N_s/n\) is \(m_s(1-m_s)/n\); Markov's inequality applied to its squared centered value, and then the same argument for \(N_o\), gives
\[
 \Pr\!\left(\gamma_n\ge A^2\min(m_s,m_o)\right)
 \ge 1-\frac4n\left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right).
                                                               \tag{10}
\]
A negative right side is simply uninformative. These are time-uniform conclusions on initialization events, without a union bound over time. The constants depend on the fixed \(R,p,\rho\); they are not asserted uniform as \(\rho\) approaches an endpoint.

At \(\rho=-1\), write the initial pair as \((G,-G)\), with \(G\sim N(0,1)\). All first-feature pairs remain antipodal. If \(m_F=\Pr(|G|\ge R)>0\), then
\[
 G_{1,\mathrm{pop}}(t)=\alpha(t)
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
 \alpha(t)\ge A^2m_F.                                    \tag{11}
\]
Empirically, replace \(m_F\) by \(N_F/n\). There is no full two-dimensional coercivity: the eigenvalues are (0) and \(2\alpha(t)\). The positive direction is exactly the target direction \((1,-1)\).

For completeness, confinement also bounds each full first-layer row at fixed nondegenerate input geometry. Its motion lies in the span of \(x_1,x_2\), and for \(|\rho|<1\)
\[
 \|W^1_j(t)-W^1_j(0)\|^2
 =\frac1d\bigl(z^1_j(t)-z^1_j(0)\bigr)^TC^{-1}
          \bigl(z^1_j(t)-z^1_j(0)\bigr).                  \tag{12}
\]
Indeed, writing a row increment as \(\sum_a c_ax_a^T\) gives a coordinate increment \(dCc\), which yields (12). Unlike (1), this parameter-space conversion deteriorates near singular input geometry. It is a finite-width, initialization-dependent bound, not a width-uniform maximum over Gaussian neurons.

## 4. What the active population can learn, and what is not preserved

For \(-1<\rho<1\), let \((\xi_1,\xi_2)\) denote a Gaussian initial pair with covariance \(C\). The event \(|\xi_1|<R,|\xi_2|<R\) has positive mass. More strongly, for every fixed \(0<r_0<R\), the square \(|\xi_1|,|\xi_2|\le r_0\) has positive mass and both initial gates are at least
\[
 p_* = \min_{|s|\le r_0}p(s)>0.
\]
On this group, the map from a first-row perturbation to its two feature perturbations has rank two:
\[
 \delta h^1_{ja}=p(z^1_{ja})\,\delta W^1_jx_a.
\]
The inputs are linearly independent and both gates are positive. Thus both sample directions are locally available in the first layer; saturation has not removed first-layer learning everywhere.

This availability also reaches the predictions at initialization. Conditional on \(W^1,W^2\), each \(b_{ja}\) is a linear form in the independent Gaussian \(w\), with coefficients \(W^2_{ij}g'(z^2_{ia})\). For either proposed \(g\), its derivative is strictly positive at finite arguments, so this coefficient vector is nonzero almost surely under Gaussian \(W^2\). The linear form is then a nondegenerate scalar Gaussian and is nonzero with probability one. Consequently, for an initially doubly active neuron, the two-output differential
\[
 \delta f_a=\frac1n b_{ja}p(z^1_{ja})\,\delta W^1_jx_a
\]
has rank two almost surely. This is a local, finite-width statement, not a lower bound on its scale as width grows.

There is also actual initial motion, rather than just an available differential. Conditional on the hidden weights, each residual is either a nonconstant affine Gaussian function of \(w\), or the nonzero constant \(-y_a\) if its feature vector vanishes. Thus \(r_a\ne0\) almost surely. On a doubly active neuron both coefficients \(p(z^1_{ja})r_ab_{ja}\) are consequently nonzero almost surely. Linear independence of the two inputs then makes its actual RawGF row velocity nonzero; invertibility of \(C\) and of its gate matrix makes its feature-pair velocity nonzero as well. These statements hold simultaneously for the finitely many initially doubly active rows.

Let \(m_A=\Pr(|\xi_1|<R,|\xi_2|<R)>0\) and let \(N_A\) be the corresponding initial count. The reservoir and moving group coexist with probability at least
\[
 1-(1-m_s)^n-(1-m_o)^n-(1-m_A)^n.
\]
On this event their empirical masses are positive, and the moving group's mass is \(N_A/n\); its variance about \(m_A\) is \(m_A(1-m_A)/n\). Continuity preserves nonzero velocities and positive gates on some short interval for that finite realization. Neither the duration of the interval nor the velocity scale has been bounded uniformly in width. This proves coexistence with actual local motion, not coexistence with persistent motion in a nonlinear limiting trajectory.

There are three distinct persistence statements:

* An initially active pair cannot become doubly inactive in finite time under the abstract integrable-control hypothesis. At least one gate remains active at each such time.
* When \(\rho=0\), every initially active coordinate remains active at finite times. At the physical antiparallel endpoint both gates of an initially active neuron likewise remain positive, by the scalar barrier argument.
* When \(0<|\rho|<1\), being active on both samples is not invariant. The side-excursion construction in Section 2 carries a doubly active neuron to a state with one gate exactly zero in finite time. With unrestricted neuron-dependent controls, an entire chosen initially active group can be moved into the same side strip.

The last observation disproves a universal two-gate persistence inference from the geometry alone when \(0<|\rho|<1\). It is not a construction of that event under the coupled random network's RawGF. For a fixed finite realization, continuity preserves its initially strictly positive gates on some short interval. For \(0<|\rho|<1\), a group active on both samples throughout the trajectory has not been established. In the scalar cases the initial active group does remain active at every finite time of a continued trajectory, but its gates may decay to zero asymptotically. Across these cases, no time-uniform gate floor or all-time nonlazy behavior follows from the initial active mass.

At \(\rho=-1\), the active mass is \(\Pr(|G|<R)>0\). Its first features are \((h,-h)\), so it has one differential direction, not two independent sample directions. That direction can support the labels. To check representability explicitly, take a nonzero first-feature vector \(h\), and choose second-layer rows with preactivations \((t,-t)\) and \((-t,t)\), \(t>0\). For any strictly increasing \(g\), the two readout weights
\[
 w_1=\frac{n}{g(t)-g(-t)},\qquad w_2=-w_1
\]
produce \((f_1,f_2)=(1,-1)\); unused readout weights can be zero. This construction uses \(n\ge2\). For \(g=\arctan\), one nonzero row already suffices because \(g\) is odd. It demonstrates representability and compatibility of the active direction, not convergence of the stated random initialization to these parameters.

Actual initial first-layer motion holds almost surely here too. The scalar coefficient of an active row's velocity is proportional to \(r_1b_{j1}-r_2b_{j2}\). Conditional on the hidden weights, this is a polynomial in \(w\) whose linear part is
\[
 -\sum_i W^2_{ij}\bigl[g'(t_i)+g'(-t_i)\bigr]w_i.
\]
It is nonzero almost surely over the hidden weights because the derivatives are positive and a Gaussian column is not identically zero. The polynomial is therefore not identically zero. Its zero set has Gaussian measure zero: this follows by induction on the number of variables from the finite root set of a nonzero one-variable polynomial, integrating over the remaining variables. Hence, conditional on the finite draw containing active rows, those rows have nonzero finite-width row and feature velocities almost surely. The same short-interval and width-scale qualifications apply. The first-feature differential lies in the label direction; a prediction differential need not do so for a nonodd top activation, since its two backward coefficients need not agree. The separate upper-parameter construction above proves representability.

## 5. What passes to the top dynamics exactly

For each second-layer neuron, let \(Z_i=(z^2_{i1},z^2_{i2})^T\). Differentiating \(z^2_{ia}=\sum_jW^2_{ij}h^1_{ja}\) yields
\[
 \dot Z_i=-2w_iG_1(t)\operatorname{diag}(g'(Z_i))r+B_i,
 \qquad (B_i)_a=\sum_jW^2_{ij}\dot h^1_{ja}.               \tag{13}
\]
Thus a positive lower bound on \(G_1\) is not a confinement argument for \(Z_i\). The first-feature transport term \(B_i\) remains, and neither candidate \(g'\) has a compact support boundary.

There is a genuine exact invariant from the frozen columns. Let \(S=H^1_F\in\mathbb R^{|F|\times2}\), which is constant, and let \(V=W^2_{:,F}\). Let \(P\) be the orthogonal projection in \(\mathbb R^{|F|}\) onto the column space of \(S\). The update gives
\[
 \dot V=-\frac2n\sum_a r_a\bigl(w\odot g'(z^2_a)\bigr)S_{:,a}^T,
 \qquad V(t)(I-P)=V(0)(I-P).                              \tag{14}
\]
This remains true at rank one. The invariant part makes no contribution to \(VS\), and its first-layer backpropagation is killed by the frozen gates. It controls only directions invisible to these two samples.

The visible frozen contribution \(U_i=(V_iS)^T\in\mathbb R^2\), instead obeys
\[
 \dot U_i=-2w_iG_F\operatorname{diag}(g'(Z_i))r.             \tag{15}
\]
The derivative is evaluated at the total \(Z_i=U_i+\sum_{j\notin F}W^2_{ij}(h^1_{j1},h^1_{j2})^T\), not just at \(U_i\). Freezing the rest or replacing \(Z_i\) by \(U_i\) would change the requested model.

There is also a useful quantitative dissipation consequence. With
\[
 L=r_1^2+r_2^2,
\]
direct differentiation using the stated rates gives
\[
\begin{aligned}
 -\dot L={}&\frac4n\left\|\sum_a r_ah^2_a\right\|^2
 +\frac4{n^2}\left\|\sum_a r_a\delta^2_a(h^1_a)^T\right\|_F^2\\
 &+\frac4{nd}\left\|\sum_a r_a\delta^1_ax_a^T\right\|_F^2.
\end{aligned}                                                    \tag{16}
\]
For the second term, set \(v_i=w_i(r_1g'(z^2_{i1}),r_2g'(z^2_{i2}))^T\). Its squared matrix norm is \(n\sum_i v_i^TG_1v_i\). Restrict to the occupancy event \(N_s>0\) and \(N_o>0\), so that \(\gamma_n=(2A^2/n)\min(N_s,N_o)>0\). Since \(G_1(t)\succeq\gamma_nI\) throughout every continued trajectory, on this event
\[
 -\dot L\ge\frac{4\gamma_n}{n}
      \sum_{i,a}w_i^2r_a^2g'(z^2_{ia})^2,
\]
and for every \(T\) on the trajectory,
\[
 \int_0^T\frac1n\sum_{i,a}w_i^2r_a^2g'(z^2_{ia})^2\,dt
 \le\frac{L(0)-L(T)}{4\gamma_n}
 \le\frac{L(0)}{4\gamma_n}.                              \tag{17}
\]
If \(\gamma_n=0\), retain the undivided identity (16); (17) is not asserted. This is an actual controlled top-layer activity integral on its positive-occupancy event. Its weights may vanish or degenerate; it does not control the unweighted residual integral or the original first-layer controls \(q_{ja}\), which include a multiplication by \((W^2)^T\). No \(L^p\) assertion about those controls is made.

At any finite state with \(\gamma_n>0\) and \(w\ne0\), both \(g'\)'s are positive, so (16) gives strictly decreasing loss when \(r\ne0\). This pointwise strictness is not a time-uniform rate: no positive uniform lower bound has been proved for
\[
 \frac1n\sum_iw_i^2g'(z^2_{ia})^2.
\]

Some finite-horizon parameter estimates are available without the reservoir and should not be credited to it. Rewriting (16) in terms of velocities gives
\[
 -\dot L=\frac{\|\dot w\|^2}{n}
          +\|\dot W^2\|_F^2
          +\frac{d\|\dot W^1\|_F^2}{n}.
\]
Consequently,
\[
 \|W^2(t)-W^2(0)\|_F\le\sqrt{tL(0)},\qquad
 \|w(t)-w(0)\|\le\sqrt{ntL(0)}.                           \tag{18}
\]
Also,
\[
 \frac d{dt}\|w\|^2=-4n\langle r,f\rangle\le2n,            \tag{19}
\]
since \(\langle f-y,f\rangle=\|f-y/2\|^2-\|y\|^2/4\ge-1/2\). These bounds grow with the horizon. They do not supply the desired all-time control of the upper layer.

## 6. Arctan and shifted softplus: what their shape does and does not add

Take first \(g(s)=\arctan s\). Then
\[
 |g(s)|\le\pi/2,\qquad g'(s)=\frac1{1+s^2}>0,\qquad
 |s g'(s)|\le\tfrac12.
\]
The second-feature values are bounded, but their Gram need not have a positive lower eigenvalue. The derivative tends to zero in both tails, without an exact boundary that could freeze a coordinate or support the excursion argument.

For shifted monotone softplus, use the explicit fixed family
\[
 g(s)=\log(1+e^{s+b})-c,
\]
where \(b,c\) are constants independent of width and input geometry. The usual centered vertical shift is \(b=0,c=\log2\). Here
\[
 g'(s)=\sigma(s+b)\in(0,1),\qquad
 \sigma(u)=\frac1{1+e^{-u}}.
\]
There is no uniform positive derivative bound; the negative tail closes the gate asymptotically. The positive tail is unbounded and asymptotically affine. A fixed shift does not remove either fact.

Even the scalar control equation \(\dot z=g'(z)q\) has no control-amplitude-independent confinement for either activation. For arctan, integration gives \(z+z^3/3=\int_0^tq\), starting from zero. A constant control on \([0,1]\) of size \(M+M^3/3\), zero afterwards, reaches any prescribed \(M>0\). For softplus, an antiderivative of \(1/g'(z)\) is \(F(z)=z-e^{-z-b}\). The constant control \(F(-M)-F(0)\) on \([0,1]\), zero afterwards, reaches \(-M\). Each control is integrable with finite support. These are counterexamples to transferring the first-gate geometric mechanism to \(g'\), not examples of unbounded canonical RawGF trajectories.

One tempting balance calculation also stops short. Directly from the two upper updates,
\[
 \frac d{dt}\bigl(\|w\|^2-n\|W^2\|_F^2\bigr)
 =4\sum_{a,i}r_aw_iD(z^2_{ia}),\qquad D(s)=sg'(s)-g(s).    \tag{20}
\]
For arctan, \(D(s)=s/(1+s^2)-\arctan s\) is bounded in absolute value by \(\pi/2\). For softplus, putting \(u=\sigma(s+b)\), elementary algebra gives
\[
 D(s)=c-\mathcal H(u)-bu,\qquad
 \mathcal H(u)=-u\log u-(1-u)\log(1-u)\in[0,\log2].
\]
Thus both defects are bounded. They are not zero. Even for centered softplus, where \(D\ge0\), the products \(r_aw_i\) have no prescribed sign. Equation (20) provides only
\[
 |\dot{(\|w\|^2-n\|W^2\|_F^2)}|
 \le4\|D\|_\infty\|r\|_1\|w\|_1.
\]
The reservoir and confinement estimates do not give a time-uniform integral bound on this right side. Nor would a bound on the difference alone bound both positive norms. Bounded homogeneity defect is therefore not a conserved balance or a closed upper-layer estimate here.

## 7. A direct obstruction to upgrading the first Gram to top control

For \(-1<\rho<1\), fix a first-layer configuration with \(G_F\succ0\) and with some other neurons active. It can be chosen with strict inequalities in all saturation and activity conditions. Because the frozen feature matrix \(S\) has rank two, a row supported on its coordinates can realize any prescribed pair of second preactivations.

Choose all second-layer rows identical, with pair \((M,M)\) for arctan, or \((-M,-M)\) for softplus. Choose paired readout weights \(+B,-B\), with remaining weights zero if needed, so \(\sum_iw_i=0\) and \(\|w\|^2=2B^2\). At this state,
\[
 f=(0,0),\qquad r=(-1,1),\qquad L=2.
\]
Each row has equal second features on the samples, so \(\dot w=0\). Identical second-layer rows and zero summed readout weight give \(b_{ja}=0\), hence \(\dot W^1=0\), at this instant. Only the second-layer term contributes to the loss derivative, giving exactly
\[
 -\dot L=\frac4n\|w\|^2 g'(\pm M)^2
             (1,-1)G_1(1,-1)^T.                         \tag{21}
\]
With \(B=M\), both relevant upper-layer norms become arbitrarily large while the first states, first Gram, and loss stay fixed. Nevertheless (21) tends to zero: its gate factor scales as \(M^2/(1+M^2)^2\) for arctan and as \(M^2\sigma(-M+b)^2\) for softplus.

Taking \(w=0\) in the same equal-pair construction gives an exact positive-loss stationary state of the full RawGF. Thus coercive first features and an available active group alone cannot exclude stalled upper dynamics. These states are diagnostic counterexamples to that implication; a frozen network is not being offered as the activation-design solution.

The exact cancellations have probability zero under continuous Gaussian initialization. For any tolerance \(\epsilon>0\), choose a finite \(M\) sufficiently large that the tail state's loss decrease is less than \(\epsilon/2\), and then choose a small open neighborhood on which it is less than \(\epsilon\), preserving strict first-layer occupancy and activity. Alternatively, about a stationary center with \(w=0\), any fixed finite \(M\) admits such a neighborhood for each \(\epsilon>0\). These neighborhoods have positive, potentially extremely small, Gaussian probability because all parameter entries have nonzero-variance Gaussian laws. Intersecting them with the probability-one initial-motion event of Section 4 retains active first-layer neurons with actual nonzero motion and arbitrarily weak loss decrease. This construction uses at least three first-layer rows: two frozen sign groups and a distinct active row. Thus the local obstruction does not require every hidden neuron to be motionless. This does not disprove an initialization-dependent or high-probability convergence result. Nor does the unbounded family prove that a single canonical trajectory has unbounded upper norms. What it rules out is a pointwise upper-norm bound or uniform top learning rate derived only from the first confinement bound, first Gram coercivity, and bounded loss.

## 8. Antiparallel top dynamics require their own conclusion

The equal-pair tail construction of Section 7 is unavailable at \(\rho=-1\): all second preactivation pairs have the form \((t_i,-t_i)\).

For arctan, oddness gives \(f_2=-f_1\) exactly and \(r=e(1,-1)\), where \(e=f_1-1\). Put \(h=h^1_1=-h^1_2\) and \(\alpha=\|h\|^2/n\). The two upper-layer contributions to the scalar prediction dynamics are
\[
 \dot f_1=-\kappa(t)e,\qquad
 \kappa(t)\ge\frac4n\sum_i\left[
       \arctan(t_i)^2+\alpha w_i^2(1+t_i^2)^{-2}\right]\ge0.       \tag{22}
\]
The omitted first-layer contribution to \(\kappa\) is nonnegative, by the same squared-gradient calculation as (16). The reservoir gives \(\alpha\ge A^2N_F/n\). Hence \(f_1\) moves monotonically toward (1) without crossing it; (22) alone does not establish that the remaining distance tends to zero.

Large \(|t_i|\) closes the arctan derivative but opens a nonzero readout feature, so the general equal-pair obstruction should not be transplanted to this scalar setting. On the other hand, \(w=0,t_i=0\) for all \(i\) is a positive-loss stationary state even when \(\alpha>0\), and the present argument does not establish a uniform positive lower bound for \(\kappa\) along random trajectories or a time-uniform bound on their top parameters. No such assertion is needed for the confinement and reservoir claims.

For the common vertical-shift softplus family \((b=0)\), there is an additional exact identity:
\[
 g(t)-g(-t)=t,\qquad
 g(t)+g(-t)=2\bigl[\log(2\cosh(t/2))-c\bigr].
\]
Consequently,
\[
 f_1-f_2=\frac1n\sum_iw_it_i,\qquad
 f_1+f_2=\frac2n\sum_iw_i\bigl[\log(2\cosh(t_i/2))-c\bigr].       \tag{23}
\]
The contrast channel is exactly affine in the second preactivations, while the common-output channel retains nonlinear coupling. This is a structural limitation of this particular activation at antiparallel inputs. It is not evidence that an effectively affine channel meets the requested nonlinear-learning objective. A horizontal shift \(b\ne0\) generally removes the first identity in (23), but not the derivative-tail issue.

## 9. A separate first-layer distributional nonaffinity consequence

This paragraph is a root supplement to the author's geometric test.
It assumes an initial-neuron probability space with the prescribed
Gaussian pair and any measurable continued controlled trajectories
satisfying (2), with integrable controls on each finite interval for
almost every neuron. It does not construct such a population network.

For every fixed sample and time, its first preactivation Z has finite
second moment by (1). It has both unbounded tails: for -1<rho<1,
the strictly positive Gaussian density assigns positive mass to the
event that that coordinate exceeds any specified threshold and the
other coordinate is also outside [-R,R]. These neurons are frozen.
The negative event has positive mass too. At rho=-1 the same claim
uses the frozen pair (G,-G) with |G|>=R. On positive and negative
frozen tails the activation values are respectively A and -A.

Consequently phi_1(Z) is not almost surely affine in Z at any such
finite time. An affine slope other than zero would contradict the
bounded activation on an unbounded frozen tail, and slope zero would
contradict the two different frozen values. This gives a strictly
positive least-squares affine-fit error: the Gram of (1,Z) has
determinant Var(Z)>0, so the two-dimensional affine span is closed
in L^2; if the distance were zero it would be attained.

This is distributional nonaffinity of the FIRST activation only.
It does not establish persistent moving positive mass, a nonlazy
predictor, second-layer nonaffinity, or a population limit. A frozen
nonlinear feature reservoir alone would not satisfy the user's goal.

## 10. Exact status and stopping point

| Claim | Status and scope |
|---|---|
| Amplitude-independent first-state confinement | Established, with the sharp bound (1), the sharper initial-state classification, arbitrary switching, and both endpoint geometries. |
| Initially doubly saturated neurons remain frozen | Established for the actual first-layer rows along the specified dynamics. |
| Time-uniform first-feature coercivity | Established for fixed \(-1<\rho<1\): expectation bound for any supplied measurable evolved population with the stated Gaussian initial law, and empirical bound on explicit occupancy events. No population existence assertion. |
| Antiparallel first-feature coercivity | Rank one only; uniformly positive on the label direction when the reservoir is present. |
| Active group coexisting with the reservoir | Positive initial mass and actual nonzero finite-width motion almost surely on the corresponding occupancy event, persisting on a realization-dependent short interval; no width-uniform duration or motion scale. |
| Learning directions of that group | Both local sample directions available for nondegenerate inputs. At antiparallel inputs the first-feature differential lies in the label direction, and the explicit upper-layer construction establishes label representability. |
| Both gates remain active on that group | False for arbitrary controls when \(0<|\rho|<1\). Finite-time positivity holds in the scalar cases, without a uniform gate floor. |
| New top quantities furnished by the reservoir | The sample-invisible projection invariant (14) and weighted activity integral (17). Neither closes the visible top dynamics. |
| Uniform top coercivity or top-state bounds from the first Gram alone | The pointwise implication is disproved by Section 7; no unbounded canonical trajectory is claimed. |
| Arctan antiparallel refinement | Exact scalar monotonicity (22); the general equal-pair counterexample does not apply there. |
| First-layer distributional nonaffinity along a continued controlled population | Established in Section 9 from unchanged Gaussian frozen tails; no population existence is inferred. |
| Accepted relaxation or successful activation design | Not claimed. Saturation remains a candidate; full trajectory coexistence, nonlazy, and second-layer nonaffine obligations remain open. |
| All-time learning, a nonlinear width limit, or persistent nonlazy behavior | Not established. No acceptance of an affine or fully frozen replacement is presumed. |
| A new sufficient criterion, global \(q\in L^p\), or uniqueness | Not claimed. |

The bounded search stops here. Compact first gates settle the proposed first-layer geometry and produce a genuine frozen reservoir. They leave the dynamically visible upper-layer control and the intended nonlazy behavior unresolved; the valid invariants and dissipative estimates above specify exactly what has, and has not, been gained.
