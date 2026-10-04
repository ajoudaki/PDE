# General independent-dense comparison: checked boundary and strict-rate bridge

2026-10-04. Scoped theoretical continuation. The user authorized relevant
proofs from previous studies. This report writes only the assigned new-study
file; it does not promote a result, modify a source study, run an experiment,
or change the maintained book.

**Outcome.** The requested strict root-width comparison is not established
by the audited sources or by this bounded continuation. The existing theorem
does cover arbitrary fixed depth, general fixed sphere data with a positive
initial top-feature Gram gap, signed small labels, and unbounded activation
values, in the requested all-physical-time and whole-sphere topology. Its
rate retains an unbounded factor \(\exp(C\sqrt{\log n})\). Below, the
zero-readout structure sharpens its label dependence, and an exact damped
sensitivity reduction isolates one mixed tangent-kernel derivative that
would give an integrable all-time bound. A further source audit supplies
the first instantaneous cross-response moments; the remaining adjoint
augmentation has an exact damped projection equation, but its neuronwise
transported response budget is unproved. None of these advances removes
the strict-rate gap. This is a limitation of the completed proof, not a
counterexample to the target. Section 5 assembles a fully specified
near-root coefficient from the new general fitting and unbounded source
components; its stochastic eventual width remains unquantified. No
sensitivity or response-moment hypothesis is appended to a purported theorem.

## 1. Canonical target and constants

Fix \(L\ge2\), \(m,d\), unit vectors \(v_a\in S^{d-1}\), and signed
labels \(y_a\). All are independent of width \(n\). The original inputs
are \(x_a=\sqrt d\,v_a\). With \(W^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and
\(w\in\mathbb R^n\), set
\[
 z^{(1)}(v)=W^{(1)}v,\qquad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n(t,v)=n^{-1}w(t)^\top h^{(L)}(t,v).
 \tag{1}
\]
Let \(r_a=f_n(t,v_a)-y_a\),
\(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\), and
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\). The loss is \(\rho^2\); its
gradient-flow mobilities are \((n,1,\ldots,1,n)\). The first weights
have independent \(N(0,1)\) entries, the other hidden weights independent
\(N(0,1/n)\) entries, all blocks are independent, and \(w(0)=0\).

Each activation is real on the real axis and holomorphic on
\(|\operatorname{Im}z|<a\), with a bounded first derivative on that
strip. Activation values need not be bounded. Write
\[
 \beta_{\partial}=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,
 {16\over a},
 \max_{\ell,\ 1\le j\le3}\sup_{|\operatorname{Im}z|<a/2}
                  |\phi_\ell^{(j)}(z)|\right\}<\infty.
 \tag{2}
\]
The full-strip slope bound, through Cauchy's formula, ensures the finite
derivative suprema in (2). A bound only on the real-axis slope would not
justify that implication. In particular these hypotheses imply the real
\(C^3\) bounded-derivative class of the inherited dense theorem.

Define the deterministic initial feature covariance recursively by
\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}
 =\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],\qquad
 Z\sim N(0,Q^{(\ell-1)}).
 \tag{3}
\]
Assume \(\gamma=\lambda_{\min}(Q^{(L)})>0\), and set
\(\lambda=\gamma/m\). No forward variance
normalization, data orthogonality, parity restriction, or additional
history-covariance gap is imposed.

For independently initialized, independently trained copies define
\[
 \|f_n-f_n'\|_*
 =\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
                |f_n(t,v)-f_n'(t,v)|.
 \tag{4}
\]
The endpoint is the fitted limit; both copies use the same physical time.
The conjectural numerical benchmark is
\[
 \|f_n-f_n'\|_*\le
 {\beta_{\partial}^{124L}
 [d+1+\log(6/\delta)]Y(m/\gamma)^{3/2}\over\sqrt n},
 \qquad
 Y\le {\gamma\over m}\beta_{\partial}^{-62L},
 \tag{5}
\]
with probability at least \(1-\delta\) at sufficiently large width.
Neither the strict rate nor these powers is certified here. Constants
denoted \(C,K,\kappa\) below depend on the fixed data, depth,
activation bounds, and physical margins, but not on width or time. The
inherited probability theorem does not track all those constants through
its finite-neuron stopping argument. Accordingly they cannot simply be
replaced by powers in (5).

## 2. What the existing general proof actually provides

The inherited physical/carrier theorem in
`dense_cutoff_population_rate_20261001/DEPTH_EXTENSION_RESULT.md`
provides events \(\Omega_n\), with \(\mathbb P(\Omega_n)\to1\), for
fixed sufficiently small labels. On these events hidden operator norms,
the first-weight Frobenius RMS, and feature RMS norms stay bounded;
readout and backward RMS norms are \(CY\); and
\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 \int_0^\infty\rho(t)\,dt\le CY,
 \qquad {K(t)\over m}\succeq{\lambda\over4} I_m.
 \tag{6}
\]
Here the tangent matrix \(K\) is defined in Section 3. With
\(k_a^{(L)}=w\),
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\),
and \(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\), its
carrier bound is
\[
 M_n:=\max_{a,\ell,i}\sup_{t\ge0}|k_{a,i}^{(\ell)}(t)|
       \le C Y\sqrt{\log(e+n)}.
 \tag{7}
\]
The full finite-neuron proof underlying this inherited result is not
reproved in this scoped note. Its good-pair comparison, Gaussian extension,
and topology transfer were inspected directly rather than accepted from
their recorded check labels.

Here is a useful label refinement of that comparison. For two actual good
trajectories put
\[
 D_h={\|\Delta W^{(1)}\|_F\over\sqrt n}
       +\sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_F,
 \qquad D_w={\|\Delta w\|_2\over\sqrt n},
 \qquad E(t)=\int_0^t\|\Delta r(s)\|_2/\sqrt m\,ds.
\]
Forward subtraction and the exact backward product rule give
\(\|\Delta h_a^{(\ell)}\|_2/\sqrt n\le CD_h\) and
\[
 {\|\Delta\delta_a^{(\ell)}\|_2\over\sqrt n}
 \le C[D_w+(Y+M_n)D_h].
\]
In the gate-difference term, the carrier belongs to one reference path;
there is no assumption about an interpolating trajectory. Keeping the
factor \(Y\) in hidden parameter gradients gives
\[
 \begin{aligned}
 D_h(t)&\le D_h(0)+CY E(t)
       +C\int_0^t\rho[D_w+(Y+M_n)D_h]\,ds,\\
 D_w(t)&\le C E(t)+C\int_0^t\rho D_h\,ds,\\
 E(t)&\le C\int_0^t\rho[(1+YM_n)D_h+YD_w]\,ds.
 \end{aligned}\tag{8}
\]
For the last line, subtract the two exact residual equations and use the
gap of one path, then integrate its exponentially decaying propagator.
The kernel difference is bounded by
\(C[(1+YM_n)D_h+YD_w]\): the readout term costs \(CD_h\), and every
hidden term pairs a gradient difference with a gradient of RMS \(CY\).
Both initial residuals are \(-y\), and \(D_w(0)=0\).

For \(0<Y\le1\), substitute (8) into the inequality for
\(D_h+D_w/Y\). Its coefficient is at most
\(C(Y^{-1}+M_n)\rho\). Gronwall and (6) therefore give
\[
 \sup_t(D_h+D_w/Y)
 \le C\exp(CYM_n)D_h(0),\qquad
 D_h(0)\le \sqrt L\,\|G-\widetilde G\|_2/\sqrt n,
 \tag{9}
\]
where \(G=(W_0^{(1)},\sqrt nW_0^{(2)},\ldots,\sqrt nW_0^{(L)})\)
is the standard Gaussian root. The width-independent exponential coming
from \(Y^{-1}\int\rho\) has been included in \(C\).
Prediction subtraction costs \(C(D_w+YD_h)\) uniformly on the unit
sphere, so the good-set Lipschitz constant can be taken as
\[
 \ell_n={CY\over\sqrt n}
             \exp\{CY^2\sqrt{\log(e+n)}\}.
 \tag{10}
\]
The case \(Y=0\) has identically zero prediction and is treated separately.
The refinement is deterministic on any events satisfying the displayed
uniform physical constants. It does not claim new uniform probability
control over all label directions simultaneously.

The physical speeds imply \(|\partial_t f_n(t,v)|\le CY e^{-\kappa t}\).
Also
\(\nabla_vf_n=W^{(1)\top}\delta^{(1)}(v)/n\), whose norm is at most
\(CY\) on the unit ball. Consequently the proof coordinate
\(u=1-e^{-\kappa t}\) gives a joint modulus
\[
 |f_n(t(u),v)-f_n(t(u'),v')|
 \le CY(|u-u'|+\|v-v'\|_2),
 \tag{11}
\]
including \(u=1\). This changes no training equation.

At the \(n+1\) time grid points and a sphere \(1/n\)-net, whose joint
cardinality is \(N_n\le(n+1)(1+2n)^d\), extend each scalar prediction
from \(\Omega_n\) by
\[
 F_{u,v}(G)=\inf_{H\in\Omega_n}
   \{f_n(H;t(u),v)+\ell_n\|G-H\|_2\},
\]
and truncate only this auxiliary extension to the physical amplitude
interval. The extensions agree with the flow on \(\Omega_n\) and are
globally \(\ell_n\)-Lipschitz. Gaussian Lipschitz concentration, followed
by a union bound for two copies and (11), gives
\[
 \|f_n-f_n'\|_*
 \le \ell_n\sqrt{8\log(8N_n/\delta)}+CY/n
 \tag{12}
\]
with probability at least \(1-\delta\) once
\(2\mathbb P(\Omega_n^c)\le\delta/2\). The Gaussian concentration
inequality is proved in `GENERAL_SELF_AVERAGING.md`; no conditional
Gaussian Poincare inequality is used. This reproduces the valid whole-sphere
near-root boundary and makes its zero-label scaling explicit.

At every fixed \(Y>0\), the exponential in (10) is unbounded. It is
therefore invalid to absorb it into a width-independent coefficient,
regardless of how large the fixed coefficient in (5) is. The smaller source
errors available in Legendre or analytic compression can absorb such a
factor by choosing a larger approximation order. Independent dense copies
already fluctuate at the root-width scale and have no analogous free
source-accuracy parameter.

## 3. Exact mixed-kernel reduction with the training damping retained

Use mobility-Euclidean coordinates
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w),
 \qquad \mathcal F_v=n f_n(v),\quad
 g_v=\nabla_\Theta\mathcal F_v,\quad
 H_v=D_\Theta^2\mathcal F_v.
\]
Let \(P\) embed the initialized Gaussian blocks with zero readout block.
The autonomous vector field and its derivative are exactly
\[
 \dot\Theta=-{2\over m}\sum_a r_a g_a,\qquad
 A(t)=D_\Theta\dot\Theta
 =-{2\over mn}\sum_a g_ag_a^\top-{2\over m}\sum_a r_aH_a.
 \tag{13}
\]
Let \(J(t,s)\) solve \(\partial_tJ=A(t)J\), \(J(s,s)=I\).
For a unit query \(v\), define
\[
 K_{va}(t)={g_v(t)^\top g_a(t)\over n},\qquad
 d_v(t)=\nabla_G f_n(t,v)={P^\top J(t,0)^\top g_v(t)\over n},
\]
\[
 B_{va}(t)=\nabla_G K_{va}(t)
 ={1\over n}P^\top J(t,0)^\top
                   [H_v(t)g_a(t)+H_a(t)g_v(t)].
 \tag{14}
\]
Here \(g_a=g_{v_a}\), and \(K\) restricted to training queries is the
matrix in (6). Differentiating the exact prediction equation
\(\dot f_v=-(2/m)\sum_a r_aK_{va}\) gives
\[
 \dot d_v=-{2\over m}\sum_a[K_{va}d_a+r_aB_{va}],
 \qquad d_v(0)=0.
 \tag{15}
\]
Both Hessian-gradient terms in (14) have the same sign. They do not cancel.

This also resolves the formal undamped-term issue in the time integral.
Put \(D(t)=(d_a(t)^\top)_{a=1}^m\) and
\(\|D\|_{m,F}=\|D\|_F/\sqrt m\). Define the actual residual contractions
\[
 C_a(t)={1\over m}\sum_b r_b(t)B_{ab}(t),\qquad
 C_v(t)={1\over m}\sum_a r_a(t)B_{va}(t).
\]
With \(C_{\rm tr}\) the matrix with rows \(C_a^\top\), equation (15)
and (6) imply
\[
 \|D(t)\|_{m,F}
 \le2\int_0^t e^{-\lambda(t-s)/2}
                    \|C_{\rm tr}(s)\|_{m,F}\,ds,
 \qquad
 \int_0^\infty\|D(t)\|_{m,F}\,dt
 \le{4\over\lambda}\int_0^\infty\|C_{\rm tr}(s)\|_{m,F}\,ds.
 \tag{16}
\]
Indeed the homogeneous propagator acts on every Gaussian-coordinate
column with norm at most \(e^{-\lambda(t-s)/2}\); Minkowski and Tonelli
then give (16). If \(\|K_{v,:}(t)\|_2/\sqrt m\le K_*\), the query
equation yields
\[
 \int_0^\infty\|\dot d_v(t)\|_2\,dt
 \le {8K_*\over\lambda}
           \int_0^\infty\|C_{\rm tr}(t)\|_{m,F}\,dt
       +2\int_0^\infty\|C_v(t)\|_2\,dt.
 \tag{17}
\]
This is a deterministic exact-to-inequality reduction on the fitting path.
It retains the residual inside the contraction; it does not replace
sample RMS by a maximum. For comparison, Cauchy--Schwarz gives
\[
 \|C_{\rm tr}\|_{m,F}
 \le\rho\left({1\over m^2}\sum_{a,b}\|B_{ab}\|_2^2\right)^{1/2},
 \qquad
 \|C_v\|_2\le\rho
           \left({1\over m}\sum_a\|B_{va}\|_2^2\right)^{1/2}.
 \tag{18}
\]
Thus genuine root-width moments of the mixed derivatives (14), after
valid localization and with query increments, would supply an integrable
all-time Gaussian derivative estimate. Merely bounded \(d_a(t)\) would
not justify integrating the first term of (15); (16) supplies the needed
damping mechanism. Equations (16)--(18) do not prove the moments of (14).

For clarity about the probability implication: if a globally defined
Gaussian-Sobolev prediction family with common initial value zero obeyed
\(\int_0^\infty\|\|\nabla_G\partial_tf_v(t)\|_2\|_{L^2}\,dt
\le C_v/\sqrt n\), Gaussian Poincare, the fundamental theorem of calculus,
and Minkowski would give
\[
 \left\|\sup_t|f_v(t;G)-f_v(t;G')|\right\|_{L^2}
 \le {\sqrt2 C_v\over\sqrt n}.
 \tag{19}
\]
The actual good-set estimates above are not such a global family. A
whole-sphere result additionally needs quantitative query-increment
moments; fixed-query (19) alone does not imply (4).

## 4. Where the promising routes stop

**Adjoint energy.** For
\(q(s;t,v)=J(t,s)^\top g_v(t)\) and
\(\mathsf L=\sqrt{2/(mn)}[g_a]_a\), exact differentiation gives
\[
 \|q(s)\|_2^2+2\int_s^t\|\mathsf L(u)^\top q(u)\|_2^2\,du
 =\|g_v(t)\|_2^2
 -{4\over m}\int_s^t\sum_a r_a(u)q(u)^\top H_a(u)q(u)\,du.
 \tag{20}
\]
The known Hessian decomposition has a bounded operator part and terms
\(Z_{a,\ell}^\top\operatorname{diag}(k_a^{(\ell)}
\odot\phi_\ell''(z_a^{(\ell)}))Z_{a,\ell}\), where
\(Z_{a,\ell}=D_\Theta z_a^{(\ell)}\). Its remaining quadratic form
contains
\[
 {1\over n}\sum_{\ell,i}|k_{a,i}^{(\ell)}|
                       |(Z_{a,\ell}q)_i|^2.
 \tag{21}
\]
Replacing a maximum over samples by the contractions in (18) is useful
for constants, but does not estimate (21): samplewise Cauchy--Schwarz
still introduces products of carriers with fourth powers of the response
coordinates. The existing marginal carrier moments do not control that
joint quantity. Strip holomorphy removes a possible missing-fourth-
derivative issue in a new insertion argument; it does not supply the
required stochastic decoupling or a global extension.

**Gaussian interpolation and second derivatives.** The covariance
interpolation identity pairs \(\nabla_G f\) at two correlated roots.
Its absolute-value bound recovers the same transported prediction
gradient. A second-order Gaussian inequality controls a direct Hessian
composition by the available normalized Schatten estimates, but its flow
second variation contains
\(k\,D_\Theta z\,J(t,s)^\top g_v(t)\). This is the same joint
directional product. Nor does good-event differentiation justify a global
Gaussian inequality: an indicator has a boundary contribution, and the
probability of the bad set tending to zero does not bound that contribution.

**Correction from the forward-response source theorem.** The first
version of this note stopped too early in its marked-endpoint argument.
The supervisor identified `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` Section 4
and `DEPTH_INDEPENDENT_EXPONENT.md`, whose underlying complete insertion
proof is in `DEEP_COMPLEX_SOURCE.md`. They supply actual Gaussian control
of the following field, so it cannot be presented as wholly unprovided.
At every depth \(L\ge2\),
put \(D_a^{(1)}=\operatorname{diag}(\phi_1'(z_a^{(1)}))\). The exact
blocks \((g_v)_{W^{(1)}}=\delta_v^{(1)}v^\top\) and
\((g_v)_{\sqrt nW^{(2)}}=\delta_v^{(2)}h_v^{(1)\top}/\sqrt n\)
give
\[
 Z_{a,2}g_v
 =\delta_v^{(2)}{h_v^{(1)\top}h_a^{(1)}\over n}
  +(v^\top v_a)W^{(2)}D_a^{(1)}D_v^{(1)}
                        W^{(2)\top}\delta_v^{(2)}.
 \tag{22}
\]
For a training driver \(v=v_b\), this is exactly the source's
\(R_b^{(2)}(v_a)\), not a new observable class. The source proves its
coordinate maximum at scale \(S\sqrt{\log n}\), where \(S\) is the
fixed activity allowance. The insertion identity yields more information
before taking that maximum. Here \(\|z\|_{p,n}^p=n^{-1}\sum_i|z_i|^p\).

For any evaluated query \(u\), let
\(R_b^{(\ell)}(u)=D_\Theta z^{(\ell)}(u)g_b\) and
\(Q_b^{(\ell)}(u)=D_\Theta h^{(\ell)}(u)g_b\). On the common stopped
event, singleton row insertion expresses the next-layer coordinate as:
an independent incoming-root pairing with the cavity \(Q_b\); a direct
feature pairing times \(\delta_{b,i}\); a direct reverse trace times
\(\delta_{b,i}\); an integral of training residuals times
\(\delta_{a,i}\) and an asymmetric trace; a learned-row correction;
and a uniformly vanishing remainder. The exact normalized trace is
\[
 {1\over n}\operatorname{tr}
 \{D_\Theta Q_b^{(\ell)}(t,u)J(t,s)
                         D_\Theta h_a^{(\ell)}(s)^\top\}.
\]
Its width-independent bound follows by assigning Schatten exponent 2 to
the first endpoint, infinity to the second endpoint, and \(2h\) to
each of \(h\) training-Hessian insertions. This is the additional
Gaussian structure missing from a bare operator-norm argument.

Keep the actual \(\delta_{a,i}\) in these terms instead of replacing
them by their largest coordinate. The Gaussian pairing has conditional
variance at most \(CS^2\), uniformly in the individual time and query.
The direct and reverse terms have counting \(L^p\) norms at most
\(C_pS\) by the carrier budget. The integral term has such norm at
most \(C_pS^2\), since \((2/m)\sum_a\int|r_a|\le CS\); the
learned-row correction has another factor \(S\), using the RMS of
\(Q_b\). Minkowski, followed by conditional Gaussian moments, therefore
gives on the source event
\[
 \sup_{t\le T_n,\ u\in S^{d-1}}
 \mathbb E\left[\mathbf1_{\Omega_n}
       \|R_b^{(\ell)}(t,u)\|_{p,n}^p\right]
 \le C_pS^p,
 \qquad p<\infty\text{ fixed},
 \tag{23}
\]
for all sufficiently large \(n\). The uniformly vanishing remainder
is at most \(S\) after increasing the width threshold at the fixed
\(S>0\). There is no query or time supremum inside this expectation.
Gaussian indicators are dropped only from nonnegative upper bounds for
cavity references defined using their own retained initialization. No
independence of trained neurons is asserted.

The new reads have bounded-strip activation hypotheses. Their extension
to the current unbounded-value class is being treated by the separate
joint-budget argument in this study; (23) is not declared proved for
that larger class merely because the real physical tube permits it.
Within the source hypotheses, (23) is a newly checked consequence of
the actual insertion identity, not an assumed response moment.

There is also a precise route to passive gradient drivers, needed when
\(v\) in (22) is not a training point. `INTRINSIC_STRICT_ROOT_ROUTE.md`
proves passive backward carrier moments by adding their forward/reverse
observable sources to the same local graph. For
\(Q_v(u)=D_\Theta h(u)g_v\), the endpoint derivative has the same
normalized Hilbert--Schmidt bound as the training-driver endpoint:
\[
 D_\Theta Q_v(u)
 =D_\Theta h(u)H_v+D_\Theta^2h(u)[\,\cdot\,,g_v].
\]
Its proof uses only feature/carrier RMS and the RMS of \(R_v(u)\), all
of which follow deterministically from the physical tube. The direct
reverse observable source becomes
\(D_\Theta h(u)D_\Theta h(v)^\top y_i\delta_i(v)\), while every
state forcing and every Hessian in the asymmetric trace is still a
training term. The existing augmented graph, read in
`DEEP_ACTIVATION_EXTENSION.md` Sections 3--6, has the same primitive
operations and direct sources; two passive query indices enlarge only
the fixed-dimensional polynomial grid. Thus its local comparison applies
with this replacement. The passive carrier moments replace the training
budget for the one direct passive amplitude; the state-source amplitudes
remain training carriers. This supplies the corresponding fixed-query
moment argument in the bounded-strip source class, without adding a
passive loss or requiring a Gram gap on appended queries.

**What those moments already give for the tangent kernel.** Let
\(\eta_{ab}^{(\ell)}=D_\Theta h_a^{(\ell)}[g_b]\) and
\(\zeta_{ab}^{(\ell)}=D_\Theta\delta_a^{(\ell)}[g_b]\). The exact
directional backward recursion is
\[
 \begin{aligned}
 \zeta_{ab}^{(L)}
 &=\phi_L''(z_a^{(L)})\odot w\odot R_b^{(L)}(v_a)
             +\phi_L'(z_a^{(L)})\odot h_b^{(L)},\\
 \zeta_{ab}^{(\ell)}
 &=\phi_\ell''(z_a^{(\ell)})\odot k_a^{(\ell)}
                                  \odot R_b^{(\ell)}(v_a)\\
 &\quad+\phi_\ell'(z_a^{(\ell)})\odot
 \left[h_b^{(\ell)}{\delta_b^{(\ell+1)\top}
                                \delta_a^{(\ell+1)}\over n}
             +W^{(\ell+1)\top}\zeta_{ab}^{(\ell+1)}\right].
 \end{aligned}\tag{24}
\]
Carrier and response fourth moments bound the expected squared RMS of
\(k_a\odot R_b(v_a)\) by \(C S^4\), by Cauchy--Schwarz on the
product probability/counting space. The scalar pairing in (24) is
\(O(S^2)\). Downward induction gives an expected squared RMS bound
\(C\) for every \(\zeta\). The blocks of \(H_ag_b\) are
\[
 (H_ag_b)_w=\eta_{ab}^{(L)},\quad
 (H_ag_b)_{W^{(1)}}=\zeta_{ab}^{(1)}v_a^\top,\quad
 (H_ag_b)_{\sqrt nW^{(\ell)}}
 ={\zeta_{ab}^{(\ell)}h_a^{(\ell-1)\top}
       +\delta_a^{(\ell)}\eta_{ab}^{(\ell-1)\top}\over\sqrt n}.
\]
The physical RMS bounds and (23)--(24) consequently imply
\[
 {1\over n}\mathbb E[
     \mathbf1_{\Omega_n}\|H_a(t)g_b(t)\|_2^2]\le C.
 \tag{25}
\]
The same calculation applies to the passive-driver extension just
described. Thus the *instantaneous state derivative* of a tangent-kernel
entry has the desired root-width norm. This is a substantive positive
input. The Gaussian-root derivative (14) additionally transports that
vector by \(J(t,0)^\top\); (25) does not remove that factor.

**The remaining transported endpoint.** Trying to apply the same
insertion trace directly to
\(q(s;t,v)=J(t,s)^\top g_v(t)\) changes its endpoint derivative.
It is now the Hessian of \(\mathcal F_v\) composed with the flow from
time \(s\) to \(t\). Its exact formula is
\[
 D_{\Theta(s)}q(s;t,v)
 =J(t,s)^\top H_v(t)J(t,s)
  +\int_s^t J(u,s)^\top A_{q(u;t,v)}(u)J(u,s)\,du,
 \tag{26}
\]
where, with \(T_a=D_\Theta^3\mathcal F_a\),
\[
 A_q=-{2\over m}\sum_a\left[
 {g_a(H_aq)^\top+(H_aq)g_a^\top+(g_a^\top q)H_a\over n}
                    +r_a T_a[q,\cdot,\cdot]\right].
 \tag{27}
\]
These formulas follow by differentiating the autonomous vector field
(13) twice and applying the second-variation equation. The new curvature
term contains
\[
 Z_{a,\ell}^\top\operatorname{diag}
   \{\phi_\ell'''(z_a^{(\ell)})\odot k_a^{(\ell)}
                              \odot Z_{a,\ell}q\}Z_{a,\ell}.
 \tag{28}
\]
Neither (23) nor (25) estimates \(Z_{a,\ell}q\) for this transported
terminal gradient. Inserting (26) into the existing trace theorem would
therefore assume its missing endpoint Hilbert--Schmidt estimate. Equally,
expanding \(J\) first requires quantitative mixed-response estimates
at every curvature-insertion order; the sources prove the displayed
first-response endpoint, not uniform order dependence sufficient to sum
that enlarged hierarchy. Fixed-order source identities cannot be promoted
to a summable series by assigning guessed \((C\sqrt h)^h\) constants.

**A concrete adjoint augmentation.** Fix a terminal time \(T\le T_n\)
and a query \(v\), and abbreviate \(q(s;T,v)\) by \(q(s)\).
Write its parameter blocks as \(q^{(1)}\), \(q^{(\ell)}\) for
the \(\sqrt nW^{(\ell)}\) block, and \(q_w\). Define, along the
actual trajectory,
\[
 R_a^{(\ell)}=D_\Theta z_a^{(\ell)}[q],\qquad
 \eta_a^{(\ell)}=D_\Theta h_a^{(\ell)}[q]
       =\phi_\ell'(z_a^{(\ell)})\odot R_a^{(\ell)},\qquad
 \zeta_a^{(\ell)}=D_\Theta\delta_a^{(\ell)}[q],\qquad
 \sigma_a=g_a^\top q/n.
\]
These are transported directional fields; they are distinguished from
the instantaneous \(R_b(u)=D_\Theta z(u)g_b\) in (23).
Their exact layer recursions are
\[
 \begin{aligned}
 R_a^{(1)}&=q^{(1)}v_a,\\
 R_a^{(\ell)}&=q^{(\ell)}h_a^{(\ell-1)}/\sqrt n
                         +W^{(\ell)}\eta_a^{(\ell-1)},\\
 \zeta_a^{(L)}&=\phi_L''(z_a^{(L)})\odot w\odot R_a^{(L)}
                            +\phi_L'(z_a^{(L)})\odot q_w,\\
 \zeta_a^{(\ell)}&=\phi_\ell''(z_a^{(\ell)})\odot k_a^{(\ell)}
                                               \odot R_a^{(\ell)}\\
 &\quad+\phi_\ell'(z_a^{(\ell)})\odot
 \left[{q^{(\ell+1)\top}\delta_a^{(\ell+1)}\over\sqrt n}
                  +W^{(\ell+1)\top}\zeta_a^{(\ell+1)}\right].
 \end{aligned}\tag{29}
\]
In backward elapsed time \(\tau=T-s\), the adjoint equation is
\(\partial_\tau q=A(s)q\). Its blocks therefore satisfy
\[
 \begin{aligned}
 \partial_\tau q^{(1)}
 &=-{2\over m}\sum_a[\sigma_a\delta_a^{(1)}
                                      +r_a\zeta_a^{(1)}]v_a^\top,\\
 \partial_\tau q^{(\ell)}
 &=-{2\over m\sqrt n}\sum_a
 \left[\sigma_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}
 +r_a\{\zeta_a^{(\ell)}h_a^{(\ell-1)\top}
               +\delta_a^{(\ell)}\eta_a^{(\ell-1)\top}\}\right],\\
 \partial_\tau q_w
 &=-{2\over m}\sum_a[\sigma_a h_a^{(L)}+r_a\eta_a^{(L)}].
 \end{aligned}\tag{30}
\]
The terminal condition is \(q(T)=g_v(T)\). Thus the augmentation is
finite at fixed \(m,L\), with forward and backward boundary data;
it does not require postulating an independent response population.

The apparently undamped \(\sigma\) terms admit a useful exact
cancellation. Differentiating \(g_a(s)^\top q(s)/n\) in physical
time, using both equations in (13), gives
\[
 {d\sigma_a\over ds}
 ={2\over m}\sum_bK_{ab}\sigma_b
  +{2\over m}\sum_b r_b\,
       {q^\top(H_bg_a-H_ag_b)\over n},
 \qquad \sigma_a(T)=K_{av}(T).
 \tag{31}
\]
The first term is damping when this terminal-value equation is solved
backward. Put
\[
 V(s)=\left[{1\over m^2}\sum_{a,b}
       \left|{q(s)^\top(H_bg_a-H_ag_b)(s)\over n}\right|^2
          \right]^{1/2}.
\]
Variation of constants, (6), and Tonelli yield
\[
 \int_0^T\|\sigma(s)\|_2/\sqrt m\,ds
 \le {2K_*\over\lambda}
              +{4\over\lambda}\int_0^T\rho(s)V(s)\,ds.
 \tag{32}
\]
This has the actual commutator sign; replacing it by the sum in (14)
would not be the same identity.

For a deterministic \(M\), intersect the source event with the
auxiliary stop
\(\sup_{s\le T}\|q(s)\|_2\le M\sqrt n\), and call the
intersection \(E_M\). Equations (25) and Cauchy--Schwarz imply
\(\|\mathbf1_{E_M}V(s)\|_{L^2}\le CM\), uniformly in the
individual time. Consequently (32) gives
\[
 \left\|\mathbf1_{E_M}
       \int_0^T\|\sigma(s)\|_2/\sqrt m\,ds\right\|_{L^2}
 \le {C\over\lambda}(K_*+SM).
 \tag{33}
\]
Here the deterministic residual envelope in (6) was integrated, with
\(\int\rho\le CS\). This is a newly checked stopped estimate
under the source hypotheses of (25). It controls the integrated
training-gradient projections. It does not remove the \(q\) stop.

The required new insertion terms can also be written without hiding a
vector of free controls. For an interior neuron \(i\) in layer
\(2\le j<L\),
let \(a_i=W^{(j+1)}_{:,i}\) be its outgoing column and
\(b_i=(W^{(j)}_{i,:})^\top\) its incoming row. Their directional
variations are
\(c_i=q^{(j+1)}_{:,i}/\sqrt n\) and
\(d_i=(q^{(j)}_{i,:})^\top/\sqrt n\). Equation (30) gives
\[
 \begin{aligned}
 c_i(s)&={\delta_v^{(j+1)}(T)h_{v,i}^{(j)}(T)\over n}\\
 &\quad-{2\over mn}\sum_a\int_s^T
  [\sigma_a\delta_a^{(j+1)}h_{a,i}^{(j)}
       +r_a\zeta_a^{(j+1)}h_{a,i}^{(j)}
       +r_a\delta_a^{(j+1)}\eta_{a,i}^{(j)}]\,du,\\
 d_i(s)&={\delta_{v,i}^{(j)}(T)h_v^{(j-1)}(T)\over n}\\
 &\quad-{2\over mn}\sum_a\int_s^T
  [\sigma_a\delta_{a,i}^{(j)}h_a^{(j-1)}
       +r_a\zeta_{a,i}^{(j)}h_a^{(j-1)}
       +r_a\delta_{a,i}^{(j)}\eta_a^{(j-1)}]\,du.
 \end{aligned}\tag{34}
\]
All time-dependent integrands in this display are evaluated at \(u\).
The direct deleted forward and reverse sources have variations
\[
 D(a_i h_{a,i}^{(j)})[q]
       =a_i\eta_{a,i}^{(j)}+c_i h_{a,i}^{(j)},\qquad
 D(b_i\delta_{a,i}^{(j)})[q]
       =b_i\zeta_{a,i}^{(j)}+d_i\delta_{a,i}^{(j)}.
 \tag{35}
\]
Thus the new controls are the scalar directional fields and their
terminal values, with the vector terms given by (34). A cavity adjoint
would have to use its own terminal gradient. Taking the terminal
gradient of the full network as fixed cavity data would retain dependence
on the deleted roots and invalidate the conditional Gaussian step.

There is no established obstruction from an automatically repeated
third-derivative loss. The joint linearization in physical time is
block triangular:
\[
 \partial_s\begin{pmatrix}\Delta\Theta\\\Delta q\end{pmatrix}
 =\begin{pmatrix}A&0\\-A_q&-A^\top\end{pmatrix}
                \begin{pmatrix}\Delta\Theta\\\Delta q\end{pmatrix}.
 \tag{36}
\]
Its off-diagonal forcing occurs once in its Green formula, as in (26),
although it is surrounded by two training propagators. Consequently a
generic argument assigning a new high-moment loss at every adjoint
iteration would be too pessimistic. Equations (29)--(36) are a concrete
starting point for an augmented bidirectional insertion proof.

The unresolved step is now specific. The reverse observable in (29)
contains \(k_a^{(\ell)}\odot R_a^{(\ell)}\). Its local insertion
requires the new same-root traces with endpoint (26), including (28),
and the terminal terms in (34). The original asymmetric trace theorem
does not bound those endpoints without a transported-response budget.
Neither (33) nor the physical RMS stop gives the requisite counting
fourth moments of \(R_a^{(\ell)}\). A scalar Volterra comparison
retaining the individual carrier inside the residual integral could
potentially give such a budget; its augmented Gaussian coefficients and
boundary feedback have not been bounded here. Treating this comparison
as already proved would add the missing assumption in another form.

The parallel new-study note `UNBOUNDED_COMPRESSOR_BRIDGE.md`, Section 12,
derives a quadratic-exponential budget for running **training** carriers
from actual Gaussian domination. Conditional on that note's completed
source extension, a single good event gives
\(\|k_a^{(\ell)}\|_{p,n}\le CS\sqrt p\) for every \(p\ge2\).
This substantially improves the unmarked carrier factors and makes a
Gaussian-tail Volterra approach plausible. It supplies neither the
transported second factor in (21) nor its new trace endpoints. In
particular, fixed-order estimates with width thresholds depending on
order cannot justify a Dyson truncation at order \(c\log n\) without
quantitative bounds on those thresholds and remainders. The source's
all-order carrier budget does not remove that separate mixed-response
requirement.

This is the corrected endpoint of the bounded attempt: the instantaneous
cross-response and mixed-gradient estimates are supplied or derivable,
and their adjoint training projections have the damping (31)--(33).
Accumulated neuronwise transport, global Gaussian localization, and index
increments remain unclosed. The earlier orthogonal-mixer example only
refuted a norms-only shortcut. It did not refute the actual Gaussian
response theorem and is withdrawn as evidence for a first-chain gap.

**Incoming-row replacement.** There are \(Ln\) independent Gaussian
incoming-row blocks, so scalar replacement influences \(C/n\) in
\(L^2\) would give variance \(C/n\) by Efron--Stein. Full-neuron
deletion is the correct independent cavity. However, its first scalar
variation is
\(n^{-1}(\xi^\top A_\xi+\eta^\top A_\eta)\), where the omitted
incoming/outgoing Gaussian vectors have covariance \(I/n\). Conditional
variance is therefore
\((\|A_\xi\|_2^2+\|A_\eta\|_2^2)/n^3\). The coefficients contain
\(J(t,s)^\top g_v(t)\), so Gaussian reinsertion exposes, rather than
removes, the directional bound. The existing nonlinear retained-state
remainder \(\|U\|_2\le n^{-1/25}\) gives only
\(|g_v^\top U|/n\le Cn^{-27/50}\) when \(\|g_v\|_2\le C\sqrt n\).
Its squared sum over \(Ln\) blocks is \(O(n^{-2/25})\), not
\(O(n^{-1})\). This is an insufficiency of the bound, not a lower bound
on the actual influence. Uniform adaptive-control and localization
estimates are additional unresolved parts of this route.

**Finite Gaussian programs and label series.** The older
`mfp_general_time_doubling/WIDTH_CONCENTRATION_CLOSURE.md` does contain
an actual strict \(n^{-1/2}\) rate argument: conditional Gaussian
actions, explicit moment induction, and polynomially small stopping
probabilities. Its constants depend on a fixed number \(N\) of discrete
actions, on the step size, and on all inverted history-Gram and innovation
gaps. Its moment tower reaches \(8^{6N+4}\) times the target moment
order. Its parent model is a two-hidden-layer ascent program, not the
present mean-loss flow. Neither its fixed-action theorem nor
\(\gamma>0\) justifies the unbounded-action/continuous-time limit or
the required history gaps. It is a real proof with different hypotheses,
not an overlooked solution of (5).

A small-label expansion could in principle sum finite Gaussian programs,
but it would need summable root-width errors of its increments with
controlled dependence on expansion order. The older quantitative-width
note explicitly leaves this assertion open. The inspected label-series
construction establishes finite-order time-mode identities and only a
shrinking complex label disk; it supplies no width-independent convergent
series at the fixed labels in (5). No special-data theorem is substituted
for the general target.

## 5. Fully specified general near-root fallback

The new fitting and source components make a conservative version of
(12) numerical. This remains a near-root statement and is weaker in
small-label prefactor than the structural refinement (10). Every constant
below is either displayed or given by the finite explicit recurrence
identified here; none denotes an unspecified comparison constant.

Use
\[
 s=\max\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
                     |\phi_\ell'(z)|\},\qquad
 t_2=\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
                     |\phi_\ell''(z)|,
 \qquad b=\max_\ell|\phi_\ell(0)|.
\]
For a standard real Gaussian \(Z\), set
\[
 q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
 \qquad H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),\qquad B=9s,
\]
\[
 F_{\rm dense}=s^2\left[B^{2L-2}
                   +4H^2\sum_{j=0}^{L-2}B^{2j}\right].
 \tag{37}
\]
These are exactly the fitting constants of
[`GENERAL_EXPLICIT_FITTING.md`](GENERAL_EXPLICIT_FITTING.md), with
permitted upper bounds on the real derivatives. Let
\(S_*^{\rm src}\) and \(K_{\rm src}\) be the explicit source
constants in
[`UNBOUNDED_COMPRESSOR_BRIDGE.md`](UNBOUNDED_COMPRESSOR_BRIDGE.md),
equations (5)--(10) and (22), evaluated at \(b,s,\max(1,t_2)\).
Those equations consist of finite sums, recurrences, minima, and elementary
functions of the displayed activation bounds and \(L\). Thus referring
to them retains a numerical constant, rather than an opaque \(C_L\).
Impose the actual combined allowance
\[
 0<Y\le\min\left\{{\lambda\over8H\sqrt{F_{\rm dense}}},
                              {\lambda S_*^{\rm src}\over16}\right\},
 \qquad S=16Y/\lambda,\qquad \kappa=\lambda/2,
 \qquad R=2Y/\sqrt\lambda.
 \tag{38}
\]
This is not an assertion that the benchmark cap in (5) implies every
source condition. The case \(Y=0\) remains exactly zero.

The fitting theorem gives, for all physical time, matrix caps nine,
whole-sphere feature RMS at most \(2H\), readout RMS at most \(R\),
normalized training Gram margin \(\lambda/4\), and
\(\rho(t)\le Ye^{-\kappa t}\). The source event gives its
training-carrier maximum through
\(T_n=32\lambda^{-1}\log(en)\). Its deterministic real tail is
\(O(n^{-7})\) at fixed parameters, by the physical tail estimates used
in the source note's Section 12. Consequently a conservative all-time
bound, at sufficiently large width, is
\[
 M_n=2K_{\rm src}S\sqrt{\log(en)}.
 \tag{39}
\]
The factor two avoids assuming an unstated strict margin at the source's
displayed maximum. The tail threshold is part of the eventual source
width, not a hidden multiplicative constant in (39).

Define
\[
 \begin{aligned}
 F_z&=2HB^{L-1},& B_\delta&=sB^{L-1}R,&
 P_*&=1+2H(L-1),&G_*&=P_*B_\delta+2H,\\
 D_\delta(M)&=sB^{L-1}(1+B_\delta)
                   +Lt_2F_zB^{L-1}M,\\
 J_M&=P_*D_\delta(M)+[1+(L-1)B_\delta]sF_z,
 & C_f&=2H+RsF_z.
 \end{aligned}\tag{40}
\]
For two actual good trajectories let
\(D_\theta=D_h+D_w\), with the block norms of Section 2.
Forward subtraction gives preactivation RMS difference at most
\(F_zD_h\) and feature difference at most \(sF_zD_h\).
Backward subtraction uses the coordinate carrier of one reference path,
so its gate term is at most \(t_2M_nF_zD_h\). Downward induction
therefore bounds every training \(\delta\)-difference in RMS by
\(D_\delta(M_n)D_\theta\). No interpolating path or carrier
bound on a nontraining query is needed for this step.

In normalized parameter coordinates
\((A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), the gradient
field in the parameter equation is \(\xi_a=g_a/\sqrt n\).
Its sum of block norms is at most \(G_*\); its blockwise difference
has sum at most \(J_{M_n}D_\theta\). The three contributions are
the first-layer backward difference, the hidden rank-one product
differences, and the readout feature difference. Hence
\[
 \|\Delta K/m\|_{\rm op}\le2G_*J_{M_n}D_\theta,
 \qquad
 D_\theta(t)\le D_\theta(0)+2G_*\int_0^t\|\Delta r\|_2/\sqrt m\,ds
                      +2J_{M_n}\int_0^t\rho D_\theta\,ds.
\]
Use the gap of one path in the residual-difference equation. Its damping
is \(\kappa\), so Tonelli gives
\[
 \int_0^t\|\Delta r\|_2/\sqrt m\,ds
 \le{4G_*J_{M_n}\over\kappa}\int_0^t\rho D_\theta\,ds.
\]
Gronwall and \(\int\rho\le Y/\kappa\) now prove
\[
 \sup_tD_\theta(t)
 \le D_\theta(0)
     \exp\!\left\{2J_{M_n}
                (1+4G_*^2/\kappa)Y/\kappa\right\}.
 \tag{41}
\]
Prediction subtraction on the entire sphere costs at most
\(C_fD_\theta\), and zero readout at initialization gives
\(D_\theta(0)\le\sqrt L\|G-G'\|_2/\sqrt n\).
Thus the good-set Gaussian-root Lipschitz constant is explicitly
\[
 \mathcal L_n={C_f\sqrt L\over\sqrt n}
     \exp\!\left\{2J_{M_n}
                (1+4G_*^2/\kappa)Y/\kappa\right\}.
 \tag{42}
\]

The fitting proof also gives
\(|\partial_t f_n(t,v)|\le
8(H^2+F_{\rm dense}Y^2/\lambda)Ye^{-\kappa t}\).
For the proof coordinate \(u=1-e^{-\kappa t}\), set
\[
 K_t={8(H^2+F_{\rm dense}Y^2/\lambda)Y\over\kappa},
 \qquad K_x=RB^L.
 \tag{43}
\]
The feature map is Lipschitz on the whole input space with coefficient
at most \(B^L\) in feature RMS, using only the actual matrix caps
and the real slope bound. Thus \(K_x\) bounds the predictor's sphere
increments even if the line segment between queries leaves the sphere.
Equation (43) gives the joint modulus
\(K_t|u-u'|+K_x\|v-v'\|_2\), including the fitted endpoint.

Use the time mesh and sphere net of Section 2, with
\(N_n\le(n+1)(1+2n)^d\), and scalar McShane extensions from the
good set, truncated to \([-2HR,2HR]\). These agree with each actual
good trajectory and are globally \(\mathcal L_n\)-Lipschitz. For
two independent roots, each extension difference has mean zero and
Lipschitz constant \(\sqrt2\mathcal L_n\) on the product Gaussian
space. Its two-sided tail is at most
\(2\exp[-z^2/(4\mathcal L_n^2)]\). Therefore
\[
 \boxed{\displaystyle
 \|f_n-f_n'\|_*
 \le2\mathcal L_n\sqrt{\log(4N_n/\delta)}
                   +{2(K_t+K_x)\over n}}
 \tag{44}
\]
with probability at least \(1-\delta\), once each path's good-event
failure is at most \(\delta/4\). Concretely, take the quantitative
initialization width \(N_{\rm fit}(\delta/8)\) from equation (5)
of the fitting note, and increase width until the source-event failure
and its tail allowance cost at most \(\delta/8\). That latter width
remains unquantified by the inherited stochastic insertion proof. The
two bad paths cost \(\delta/2\); the net Gaussian union costs the
other \(\delta/2\).

This is a general independent-dense comparison with fully specified
multiplicative constants and exact topology, conditional only on the
completed source component's claim level. Since \(J_M\) is affine in
\(M\) and (39) grows as \(\sqrt{\log n}\), (44) retains
\(\exp(c\sqrt{\log n})\) as well as the elementary net factor.
It does not establish the strict benchmark (5).

## 6. Source record and final claim status

The following scientific sources were read completely or reconstructed
from their complete displayed derivations in this pass:

- `dense_cutoff_population_rate_20261001/GENERAL_SELF_AVERAGING.md`,
  `SELF_AVERAGING_FEEDBACK_ROUTE.md`, `SELF_AVERAGING_SENSITIVITY_ROUTE.md`,
  `SELF_AVERAGING_ENERGY_ATTEMPT.md`, `SELF_AVERAGING_ROUTE_CHECK.md`,
  `SELF_AVERAGING_CHECK.md`, and `DEPTH_EXTENSION_RESULT.md`.
- `closure_sampling_20261003/INTEGRATED_DENSE_VARIABILITY_ROUTE.md`,
  `INTEGRATED_NEURON_REPLACEMENT_ROUTE.md`, and
  `INTEGRATED_COMPARISON_CHECK.md`. The latter's special-case lower-bound
  material was not used for a claim in this report.
- The corrective source pass read
  `closure_sampling_20261003/EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`,
  `DEPTH_INDEPENDENT_EXPONENT.md`, `DEPTH_INDEPENDENT_EXPONENT_CHECK.md`,
  `WHOLE_QUERY_RESPONSE_SOURCE.md`, `DEEP_COMPLEX_SOURCE.md`,
  `INPUT_DIMENSION_REFINEMENT.md`, and `INTRINSIC_STRICT_ROOT_ROUTE.md`
  completely. These reads correct the initial first-response gap claim
  and support (23)--(25), under their stated source hypotheses.
- `mfp_general_time_doubling/WIDTH_CONCENTRATION_CLOSURE.md` and
  `response_memory_width_uniform_20260927/QUANTITATIVE_WIDTH_SENSITIVITY.md`.

Scope probes were also made in
`closure_sampling_20261003/TWO_INPUT_LABEL_SERIES.md` (the exact finite-jet
recurrence, shrinking-disk derivation, and sensitivity obstruction;
not used as a proof for the current general model),
`mfp_general_time_doubling/PROOF.md` lines 1--100,
`practical_fixed_depth2/development/CONCENTRATION_DEFECT_ROUTE.md`
lines 1--160, and
`fixed_backward_clipping_width_20261001/CONCENTRATION_ROUTE.md`
lines 1--140. The latter two concern a different concentration-defect
question and modified clipped dynamics, respectively, and supply no bridge
here. Filename-only discovery searched for sensitivity, concentration,
self-averaging, independent-copy, and label-series candidates; no other
study content was imported beyond the specifically listed reads.
The corrective pass also read
`closure_sampling_20261003/DEEP_ACTIVATION_EXTENSION.md` Sections 1--6
and the opening feature-motion discussion (lines 1--565), to check the
augmented local graph. Within the present study,
`UNBOUNDED_COMPRESSOR_BRIDGE.md` Sections 1--5 and 12, and the beginning
of Section 6 through its maximum formula (23), were read. Its actual
Gaussian domination and training quadratic-exponential budget are separate
candidate inputs to the adjoint discussion; its explicit source allowance
and coordinate maximum enter the numerical fallback. Its constants are
not silently substituted for the old bounded-strip hypotheses in
(23)--(25). `GENERAL_EXPLICIT_FITTING.md` was read completely to check
the whole-sphere physical tube, the speed and tail estimates, the
initialization confidence, and every fitting constant used in Section 5.

Required process reads were the canonical-notation skill and its
neural-response reference, the rigorous-math skill, and the conjecture
skill with its research-contract, evidence-ledger, and adversarial-audit
references. The supervisor's scientific input scope replaced author
startup. No archived book material was read.

| Claim | Status in this pass |
|---|---|
| General physical tube and carrier event, bounded real derivatives and linear-growth values | Inherited internally checked theorem, not reproved here |
| Same-physical-time, fitted-endpoint, whole-sphere near-root comparison | Inherited derivation reconstructed; label refinement (8)--(12) newly checked |
| Exact mixed-kernel sensitivity and damping reduction (13)--(18) | Newly derived and checked finite-network identities/inequalities |
| Instantaneous forward-response moments and Hessian-gradient RMS (23)--(25) | Newly extracted from the actual insertion formulas under the bounded-strip source hypotheses; unbounded transfer belongs to the separate source extension |
| Exact adjoint augmentation, damped training projections, and stopped estimate (29)--(36) | Newly derived and checked; the projection estimate uses (25) and does not remove the adjoint stop |
| Quadratic-exponential training-carrier budget | Separate current-study candidate input; improves unmarked carrier moments but does not assert an adjoint budget |
| Numerical general near-root comparison (37)--(44) | Deterministic comparison and Gaussian extension newly checked, assembled with the new fitting/source components; stochastic source width remains eventual |
| Strict root-width mixed sensitivities, valid global localization, and sphere increments | Open |
| Strict comparison (5), including the displayed numerical powers and confidence dependence | Open; not proved or falsified |

The most focused remaining proof obligation is to control the
residual-contracted mixed derivatives in (17), or an equivalent
prediction-adjoint quantity, with strict root-width moments and suitable
query increments on a legitimately localized Gaussian domain. The
available averaged matrix estimates and the newly recovered instantaneous
response theorem do not yet establish it. The finite-network augmentation
identifies the missing same-root traces and terminal-gradient terms, while
removing the earlier supposed first-chain obstruction. A new proof of
that augmented boundary/insertion estimate, followed by localization and
index increments, remains necessary for this route to establish (5).
