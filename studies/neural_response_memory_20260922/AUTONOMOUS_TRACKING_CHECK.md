# Autonomous reconstruction and trajectory tracking

Status: proved conditional statements from the supervisor's explicit mathematical
assignment. The initial derivation used no repository scientific inputs;
subsequent authorized inputs and their audits are recorded in Sections 6–7.
No external sources or experiments were used. This note does not construct a
convergent compression hierarchy.

## 1. Physical state, information contract, and normalization

Fix the width \(n\geq1\), input statistic \(\chi=\|x\|^2/d\geq0\), target
\(y\in\mathbb R\), and initial matrix \(W^0\in\mathbb R^{n\times n}\).
All statements below are deterministic conditional on this fixed matrix;
Gaussian initialization alone supplies none of the uniform bounds used below.
Write \(a=W_3\), \(z=z_1\), \(U=\Delta W\), and \(X=(z,a,U)\). Define

\[
\begin{aligned}
 W&=W^0+U,& h_1&=\phi(z),& z_2&=Wh_1,\\
 h_2&=\phi(z_2),& f(X)&=\langle a,h_2\rangle_n,&r(X)&=f(X)-y,\\
 \delta_2&=a\odot\phi'(z_2),&&
 \delta_1=\phi'(z)\odot(W^\top\delta_2),
\end{aligned}
\]

where \(\langle u,v\rangle_n=n^{-1}\sum_i u_iv_i\), and activation functions
act coordinatewise. The prescribed physical vector field is

\[
 V(X)=\left(-2r\chi\delta_1,\;-2rh_2,\;
             -\frac{2r}{n}\delta_2h_1^\top\right).
 \tag{1}
\]

Assume \(\phi\in C^2\) on the activation ranges in an open physical domain
containing the trajectories considered. Then \(f\in C^2\) and \(V\in C^1\)
there, so \(V\) is locally Lipschitz. Every result is restricted to intervals on
which the stated solutions exist; global existence is not an automatic claim.

The requested norm and inner product are

\[
 \|X\|_*^2=\|z\|_n^2+\|a\|_n^2+\|U\|_F^2,
 \qquad
 \langle X,\widetilde X\rangle_*
 =\langle z,\widetilde z\rangle_n+
   \langle a,\widetilde a\rangle_n+
   \operatorname{tr}(U^\top\widetilde U).
 \tag{2}
\]

The matrix Frobenius norm is **not** divided by \(n\). Indeed,

\[
 df[\dot X]=\langle\delta_1,\dot z\rangle_n
 +\langle h_2,\dot a\rangle_n
 +\left\langle\frac{\delta_2h_1^\top}{n},\dot U\right\rangle_F.
 \tag{3}
\]

For the squared loss \(L=r^2\), (1) is therefore the preconditioned gradient
flow \(V=-M\nabla_*L\), with \(M=\operatorname{diag}(\chi I,I,I)\).
It is ordinary gradient flow in (2) only when \(\chi=1\) (or on directions
where the distinction vanishes). When \(\chi>0\), its natural gradient metric is

\[
 \|X\|_g^2=\chi^{-1}\|z\|_n^2+\|a\|_n^2+\|U\|_F^2,
 \qquad V=-\nabla_gL=-2r\nabla_g f.
 \tag{4}
\]

In particular, with

\[
 K(X)=\|\nabla_g f(X)\|_g^2
 =\chi\|\delta_1\|_n^2+\|h_2\|_n^2+
   \|\delta_2\|_n^2\|h_1\|_n^2,
 \tag{5}
\]

the exact identities are \(\dot r=-2Kr\), \(\dot L=-4r^2K\), and
\(\|V\|_g^2=4r^2K\). The same loss derivative follows directly from (3)
when \(\chi=0\); the \(z\) coordinate is then frozen and (4) is used only on
the remaining coordinates. For \(\chi>0\),

\[
 \min(1,\chi^{-1})\|X\|_*^2
 \leq\|X\|_g^2
 \leq\max(1,\chi^{-1})\|X\|_*^2.
 \tag{6}
\]

Thus metric conversion is harmless only to the extent that the needed bounds
on \(\chi\) hold.

An admissible candidate has a full collective state \(S\) consisting of
\(O(P)\) coordinates per neuron and explicitly specified current aggregates
\(Q\). Their entire number, update cost, and precision count toward any
complexity claim. The fixed \(W^0\), and declared actions by \(W^0\) or its
transpose, are allowed static data. Let

\[
 \dot S=F_P(S),\qquad
 R_P(S)=(z(S),a(S),\widehat U(S)),\qquad
 \widehat U_{ij}(S)=\frac1n\kappa_P(m_{2,i},m_{1,j},Q).
 \tag{7}
\]

Fixed problem parameters, including any permitted dependence on \(W^0\), are
suppressed in the notation. All state arguments in (7) are current values.
The maps and initialization must be supplied from admissible data, without
solving and storing the target trajectory. There is no supplied function of
training time, explicit clock, or clock encoded as a state variable with a
precomputed trajectory decoder. An autonomous ODE by itself does not enforce
this last condition: \(\dot s=1\), \(R(s)=X_{\mathrm{target}}(s)\) would pass
an intertwining identity while violating the information contract. Complexity
of map descriptions and precomputed constants also matters.

The theorem below checks a supplied candidate. It neither supplies \(F_P\) and
\(\kappa_P\) nor proves that admissible finite \(P\) achieves a desired error.
An arbitrary nonlinear pair kernel can give a full-rank matrix, so (7) makes
no low-rank assumption. Evaluating its pair sums may still cost \(O(n^2)\),
even if additional dynamical storage is \(O(nP)\).

## 2. Exact autonomous realization

Let the reduced states lie in an open set, or in a smooth finite-dimensional
manifold \(\mathcal M\) with all aggregate-consistency constraints included.
Assume \(F_P\) is locally Lipschitz and tangent to \(\mathcal M\), and \(R_P\)
is \(C^1\). The symbols \(DR_P\) and \(F_P\) below include **every** collective
coordinate and aggregate, not just the two neuron labels appearing in one
matrix entry. Let \(\mathcal I\subset\mathcal M\) be the allowed initial
states, with prescribed physical initialization \(X_0(S_0)\), and let
\(\mathcal A\) be their forward reachable set on the intervals considered.

**Exactness criterion.** For every \(S_0\in\mathcal I\), the readout
\(R_P(S(t;S_0))\) is the canonical solution of (1) with initial value
\(X_0(S_0)\), if and only if

\[
 R_P(S_0)=X_0(S_0)\quad(S_0\in\mathcal I),\qquad
 DR_P(S)F_P(S)=V(R_P(S))\quad(S\in\mathcal A).
 \tag{8}
\]

For the intended \(U(0)=0\), initial compatibility includes
\(\kappa_P(m_{2,i}(0),m_{1,j}(0),Q(0))=0\) for every \(i,j\), as well as
the correct \(z(0)\) and \(a(0)\). Aggregate constraints must hold initially
and remain invariant under \(F_P\).

Proof: if (8) holds, the chain rule gives
\(\frac{d}{dt}R_P(S(t))=V(R_P(S(t)))\) with the correct initial value.
Local uniqueness of (1) identifies this with the physical solution throughout
their common interval. To see the needed uniqueness explicitly, two solutions
inside a common neighborhood where \(V\) has Lipschitz constant \(L_0\) obey
\(\frac{d}{dt}\|X-\widetilde X\|_*^2\leq2L_0\|X-\widetilde X\|_*^2\);
multiplying by \(e^{-2L_0t}\) proves equality if they agree initially.
Covering their common interval by such neighborhoods continues the equality.
Conversely, differentiating the assumed equality of trajectories at each
reachable state gives the second condition in (8); equality at time zero
gives the first. This proves both directions.

Geometrically, the graph
\(\Gamma=\{(S,X):X=R_P(S)\}\) has tangent vectors
\((v,DR_P(S)v)\). Thus the product field \((F_P,V)\) is tangent to this
graph exactly when the second condition of (8) holds. The proof establishes
invariance through admissible initial states. The identity on all of
\(\mathcal M\) is sufficient, and is necessary if every reduced state may
be initialized. With a restricted initialization class it is necessary only
on the reachable set. No identity away from that set follows from successful
trajectory tracking.

This statement does not require an injective decoder. If two reduced states
have the same readout, exactness requires their *pushed-forward* velocities
to agree with \(V\) at that readout; their invisible internal velocities need
not agree.

## 3. Reconstruction versus projectability

A different, often conflated question begins with a prescribed current-state
encoder \(C:\mathcal N\to\mathcal M\), where \(\mathcal N\) is an invariant
physical-state manifold. Autonomous closure requires

\[
 DC(X)V(X)=F_P(C(X)).
 \tag{9}
\]

Consequently, \(C(X)=C(X')\) must imply
\(DC(X)V(X)=DC(X')V(X')\): the encoded velocity is constant on each
encoder fiber. Conversely, this fiber condition defines \(F_P\) on the image
of \(C\); it yields an admissible ODE only if the resulting field has the
required regularity and an admissible computable description. The chain rule
then proves (9) along physical trajectories.

Closure alone does not give physical reconstruction: the constant encoder
\(C(X)=0\) always closes with zero velocity. Full reconstruction additionally
requires \(R_P(C(X))=X\). Therefore identical encoded states must have
identical physical states. On a smooth physical-state patch, differentiation
gives \(DR_P(C(X))DC(X)=I\) on its tangent space, hence

\[
 \dim\mathcal M\geq\dim\mathcal N.
 \tag{10}
\]

One cannot insert the ambient dimension \(n^2+2n\) into (10) without proving
that the admissible physical family contains a patch of that dimension.
Fixed \(W^0\), zero initial update, and a restricted initialization class can
give a much smaller reachable family. Conversely, parameterizing one already
known trajectory does not establish admissible compression of the family.

If memory coordinates are not uniquely determined by the current physical
state, no physical-state encoder \(C(X)\) should be assumed. A broader fiber
test can be stated on an admissible augmented-state space \(\mathcal Y\)
with dynamics \(B\), physical projection \(\pi\), and an encoder \(C\):

\[
 D\pi\,B=V\circ\pi,\qquad
 \pi=R_P\circ C,\qquad DC\,B=F_P\circ C.
 \tag{11}
\]

On any two points of the same \(C\)-fiber, both \(\pi\) and \(DC\,B\)
must coincide. Subject to regularity, the two fiber conditions respectively
define a decoder and a closed vector field. Differentiating
\(\pi=R_P\circ C\) proves the intertwining identity on the image.
This is an analytical test; inventing an augmented space containing the
unknown trajectory does not satisfy the information contract. The direct
criterion (8) remains applicable when no preferred encoder is given.

All these conditions concern the full collective state. Failure to close one
chosen collection of row summaries disproves that collection, not every
admissible neuron-state construction with other current aggregates.

## 4. One defect and a finite-horizon estimate

For any supplied candidate define its reconstruction defect by

\[
 E(S)=DR_P(S)F_P(S)-V(R_P(S)).
 \tag{12}
\]

Suppose the \(z,a\) readout velocities are exactly the first two blocks of
(1), evaluated at the reconstructed current state. Then \(E=(0,0,H)\), with

\[
 H_{ij}(S)=\frac1n\left(
      D_S\kappa_{P,ij}(S)F_P(S)+2\widehat r\,
                  \widehat\delta_{2,i}\widehat h_{1,j}\right).
 \tag{13}
\]

Hats mean evaluation at \(R_P(S)\). The total derivative in (13) includes
\(\partial_{m_2}\kappa\,\dot m_{2,i}\),
\(\partial_{m_1}\kappa\,\dot m_{1,j}\), and
\(\partial_Q\kappa\,\dot Q\), and every further declared state argument.
There is no time derivative of the fixed \(W^0\). Thus

\[
 \|E\|_*^2=\|E\|_g^2=\|H\|_F^2
 =\frac1{n^2}\sum_{i,j}
  \left|D_S\kappa_{P,ij}F_P+
         2\widehat r\widehat\delta_{2,i}\widehat h_{1,j}\right|^2.
 \tag{14}
\]

The matrix defect norm is exactly the empirical root-mean-square pair defect
before multiplication by \(1/n\). A pointwise pair defect at most \(\varepsilon\)
therefore gives \(\|E\|_*\leq\varepsilon\), without an extra factor of \(n\).

Let \(X(t)\) solve (1), \(\widehat X(t)=R_P(S(t))\),
\(e(t)=\widehat X(t)-X(t)\), and \(q(t)=\|e(t)\|\). Here \(\|\cdot\|\)
may be either fixed metric (2) or, when available, (4). Assume on \([0,T]\)
that both trajectories exist, \(\eta(t)=\|E(S(t))\|\) is integrable, and
an integrable scalar \(\lambda(t)\) satisfies

\[
 \langle e(t),V(\widehat X(t))-V(X(t))\rangle
 \leq\lambda(t)q(t)^2.
 \tag{15}
\]

Then

\[
 q(t)\leq e^{\int_0^t\lambda(u)\,du}q(0)
  +\int_0^t e^{\int_s^t\lambda(u)\,du}\eta(s)\,ds.
 \tag{16}
\]

Proof: \(\dot e=V(\widehat X)-V(X)+E\), so
\(\tfrac12(q^2)'\leq\lambda q^2+q\eta\). Away from zero this gives
\(q'\leq\lambda q+\eta\). For a completely uniform justification, put
\(q_\rho=(q^2+\rho^2)^{1/2}\). Since
\(q_\rho'\leq\lambda q^2/q_\rho+\eta q/q_\rho
=\lambda q_\rho-\lambda\rho^2/q_\rho+\eta q/q_\rho\),
one obtains
\(q_\rho'\leq\lambda q_\rho+|\lambda|\rho+\eta\).
Multiply by \(e^{-\int_0^t\lambda}\), integrate, and let \(\rho\downarrow0\)
to obtain (16). The extra integral tends to zero because \(\lambda\) is
integrable on this interval.

A Lipschitz constant \(L_T\geq0\) for \(V\) on a neighborhood containing
the two paths implies (15) with \(\lambda=L_T\). If
\(\sup_{[0,T]}\eta\leq\varepsilon\), then

\[
 \sup_{0\leq t\leq T}q(t)
 \leq e^{L_TT}q(0)+
 \begin{cases}
  \varepsilon(e^{L_TT}-1)/L_T,&L_T>0,\\
  \varepsilon T,&L_T=0.
 \end{cases}
 \tag{17}
\]

For a \(C^1\) field, another sufficient choice for (15) is an upper bound
on the largest eigenvalue of its symmetric Jacobian in the chosen metric,
throughout each line segment between the two states. The integral identity
\(V(\widehat X)-V(X)=\int_0^1DV(X+se)e\,ds\) proves this directly.
Bounds only on either endpoint need not control the connector.

No width-independent \(L_T\) is asserted. For example, if \(\phi\) has
Lipschitz constant \(L_\phi\) on the relevant intervals,

\[
 \|\widehat z_2-z_2\|_n
 \leq\|W^0+U\|_{\rm op}L_\phi\|\widehat z-z\|_n
    +\|\widehat U-U\|_F\|\widehat h_1\|_n.
 \tag{18}
\]

This follows by expanding the difference as
\((W^0+U)(\widehat h_1-h_1)+(\widehat U-U)\widehat h_1\)
and using \(\|A\|_{\rm op}\leq\|A\|_F\). The normalization in (2)
therefore controls induced second-layer activation errors at their natural
empirical scale, given the displayed bounds. Dividing the matrix norm by
\(n\) would lose that property. Similarly,

\[
 |\widehat f-f|
 \leq\|\widehat a-a\|_n\|\widehat h_2\|_n
   +\|a\|_nL_\phi\|\widehat z_2-z_2\|_n.
 \tag{19}
\]

Thus physical-state tracking implies prediction tracking under these bounds;
small loss or prediction error does not conversely reconstruct the state.

## 5. What a uniform-in-time conclusion additionally requires

With global solutions, (16) yields a uniform bound if its amplification and
forced-error integral are uniformly controlled. Two sufficient cases are:

* If \(\lambda\leq-\gamma<0\) and \(\eta\leq\varepsilon\), then
  \(q(t)\leq e^{-\gamma t}q(0)+
  \varepsilon(1-e^{-\gamma t})/\gamma\).
* If \(A=\int_0^\infty\lambda_+(s)\,ds<\infty\) and
  \(\int_0^\infty\eta(s)\,ds\leq\varepsilon\), then
  \(\sup_{t\geq0}q(t)\leq e^A(q(0)+\varepsilon)\).

Here \(\lambda_+=\max(\lambda,0)\). These are sufficient conditions, not
necessary alternatives. In particular a uniformly bounded nonzero defect
with merely zero expansion can accumulate linearly in time.

Loss dissipation \(\int r^2K\,dt<\infty\) alone supplies neither condition.
In the natural metric,

\[
 DV=-2\left(\nabla_g f\otimes_g\nabla_g f+
                     r\,\operatorname{Hess}_g f\right).
 \tag{20}
\]

The first term is negative semidefinite, but the residual-weighted Hessian
can cause expansion. Loss decay gives no bound on its integral on connectors
and no bound on the time integral of the reconstruction defect. Full-state
strict contraction is particularly strong: if the interpolation set contains
two distinct equilibria in a proposed contraction domain, their distance is
constant, contradicting \(\lambda\leq-\gamma\). At a regular interpolating
state, (20) also has zero eigenvalues on all directions orthogonal to
\(\nabla_g f\).

Any useful width-uniform conclusion must separately establish the relevant
bounds on matrix operators, neuron states, activation derivatives, aggregate
maps, the defect, and amplification. The exactness and stability identities
do not establish those bounds.

Initial derivation frozen before evaluating the supervisor's subsequent
residual-decay proposal; its audit follows below.

## 6. Audit of the subsequent residual-decay proposal

Additional input: after the preceding derivation was frozen, the supervisor
proposed a uniform-in-time theorem using a defect proportional to the current
residual, a positive gradient-norm lower bound on both paths, and bounded
curvature on their connectors. The proposal is correct with the assumptions
made explicit below. Write \(H_f\) for its Hessian bound, to distinguish it
from the matrix defect \(H\) in (13).

Assume \(\chi>0\), use metric (4), and suppose the exact and reconstructed
solutions exist for all \(t\geq0\). In addition to the regularity above, assume
finite constants \(H_f\geq0\), \(G>0\), \(k>0\), and \(\varepsilon\geq0\)
such that, at every time,

\[
\begin{aligned}
 &\|\operatorname{Hess}_g f(X(t)+u e(t))\|_{g\to g}\leq H_f
                      &&(0\leq u\leq1),\\
 &k\leq K(X(t)),\qquad k\leq K(\widehat X(t)),\\
 &\|\nabla_g f(X(t))\|_g,\;
       \|\nabla_g f(\widehat X(t))\|_g\leq G,\\
 &\|E(S(t))\|_g\leq\varepsilon|\widehat r(t)|,\qquad
       \gamma=2k-G\varepsilon>0 .
\end{aligned}
\tag{21}
\]

Every connector must lie in the \(C^2\) physical domain. The gradient upper
bound is needed only on the reconstructed path for the proof, but assuming
it on both paths is consistent with the proposal. Then

\[
\begin{aligned}
 |r(t)|&\leq |r(0)|e^{-2kt},\\
 |\widehat r(t)|&\leq|\widehat r(0)|e^{-\gamma t},\\
 \sup_{t\geq0}\|\widehat X(t)-X(t)\|_g
 &\leq e^A\left(
       \|\widehat X(0)-X(0)\|_g+
       \frac{\varepsilon|\widehat r(0)|}{\gamma}\right),\\
 A&=2H_f\left(\frac{|r(0)|}{2k}
                +\frac{|\widehat r(0)|}{\gamma}\right).
\end{aligned}
\tag{22}
\]

Here is a direct proof. Put \(b(X)=\nabla_g f(X)\). The exact residual
obeys \(r'=-2Kr\). The reconstructed residual obeys

\[
 \widehat r'=-2\widehat r\,K(\widehat X)
                         +\langle b(\widehat X),E\rangle_g.
\]

Consequently
\((r^2)'\leq-4kr^2\) and
\((\widehat r^2)'\leq-2(2k-G\varepsilon)\widehat r^2\).
Multiplication by the corresponding exponential integrating factors proves
the first two estimates in (22), including the case of zero residual.

For the required stability estimate, fix a time and abbreviate
\(b_0=b(X)\), \(b_1=b(\widehat X)\), and
\(\Delta r=\widehat r-r\). The exact algebraic identity is

\[
 V(\widehat X)-V(X)
 =-\Delta r(b_1+b_0)-(\widehat r+r)(b_1-b_0).
 \tag{23}
\]

Let \(p(u)=f(X+ue)\), \(0\leq u\leq1\). Since
\(p'(u)=\langle b(X+ue),e\rangle_g\) and
\(|p''(u)|\leq H_f\|e\|_g^2\), integration by parts gives

\[
\begin{aligned}
 \langle e,b_1+b_0\rangle_g
 &=2\Delta r+\mathcal R,\\
 \mathcal R&=\int_0^1(2u-1)p''(u)\,du,\qquad
 |\mathcal R|\leq\frac{H_f}{2}\|e\|_g^2.
\end{aligned}
\tag{24}
\]

Also,
\(b_1-b_0=\int_0^1\operatorname{Hess}_g f(X+ue)e\,du\), hence
\(|\langle e,b_1-b_0\rangle_g|\leq H_f\|e\|_g^2\).
Taking the inner product of (23) with \(e\) therefore yields

\[
\begin{aligned}
 \langle e,V(\widehat X)-V(X)\rangle_g
 &\leq-2(\Delta r)^2+
 H_f\left(\tfrac12|\Delta r|+|\widehat r+r|\right)\|e\|_g^2\\
 &\leq2H_f\max(|r|,|\widehat r|)\|e\|_g^2.
\end{aligned}
\tag{25}
\]

The second inequality uses
\(|a-b|+|a+b|=2\max(|a|,|b|)\) for real \(a,b\), and discards the
nonpositive square. This verifies the proposed endpoint estimate, with a
stronger factor \(1/2\) in the intermediate trapezoid remainder.

Apply (16) with
\(\lambda(t)=2H_f\max(|r(t)|,|\widehat r(t)|)\).
The residual bounds and \(\max(v,w)\leq v+w\) for \(v,w\geq0\) imply

\[
 \int_0^\infty\lambda(t)\,dt\leq A,\qquad
 \int_0^\infty\|E(S(t))\|_g\,dt
 \leq\frac{\varepsilon|\widehat r(0)|}{\gamma}.
 \tag{26}
\]

Substitution proves (22). No convexity of the loss or strict contraction in
all state directions was used.

For example, if initialization is exact and
\(0\leq\varepsilon\leq k/G\), then \(\gamma\geq k\), and (22) gives
the explicit uniform bound

\[
 \sup_{t\geq0}\|\widehat X(t)-X(t)\|_g
 \leq
 \exp\!\left(\frac{3H_f|r(0)|}{k}\right)
 \frac{\varepsilon|r(0)|}{k}.
 \tag{27}
\]

This is a conditional all-time \(O(\varepsilon)\) theorem. It becomes a
width-uniform or hierarchy-convergence theorem only after proving common
bounds for \(H_f,G,k,|r(0)|,\chi\), globally valid solutions, and the
relative defect in (21), for the admissible candidates under consideration.
In particular:

* The lower bound \(K\geq k\) is required on the reconstructed path as well
  as the exact path. Exact-flow loss decay does not establish it.
* Curvature control is required on entire connectors. Bounds only along
  the two paths do not establish (24).
* The relative defect condition makes error production integrable. An
  absolute defect bound \(\|E\|\leq\varepsilon\) does not give (26).
* Global physical readout bounds need not prevent invisible reduced memory
  coordinates from blowing up. Existence of the reduced trajectory still
  requires a separate argument.
* Gaussian initial data have unbounded support. No fixed deterministic
  bounds over all Gaussian draws follow from the initialization label;
  any probabilistic or width-uniform bounds require an explicit theorem.
* Even valid constants can make (27) numerically uninformative. The result
  asserts no useful constant for the proposed neuron-state hierarchy.

When \(\chi=0\), the same proof applies on a common fixed-\(z\) slice after
removing that frozen coordinate and using the metric on the remaining
blocks. Otherwise (6) converts the stated \(g\)-metric error to the requested
physical norm.

## 7. Cross-check of the supervisor's synthesis

After the derivation above was frozen, the supervisor authorized a read-only
audit of Sections 1–5 of AUTONOMOUS_CLOSURE_CERTIFICATES.md. This cross-check
does not add an independent research source or change the initial input scope.
The canonical equations, gradient metric, sole physical defect, exact
reachable-set iff criterion, finite-horizon estimate, all-time sufficient
theorem, and prediction estimate agree with the derivation here.

Two precision corrections were sent to the supervisor:

1. The finite-horizon integrating-factor argument should explicitly require
   locally integrable amplification \(\ell\). The differential norm
   inequality holds almost everywhere; an upper-right pointwise statement
   requires corresponding pointwise regularity. The reconstruction defect is
   continuous under the already stated \(C^1\) readout and continuous
   vector-field assumptions.
2. For exact initialization, a uniform \(O(\varepsilon)\) coefficient in
   (22) is supplied by uniform bounds on \(A\) and
   \(|\widehat r(0)|/\gamma\). Positive lower bounds on \(k,\gamma\), with
   upper bounds on curvature, gradient, and initial residuals, are
   convenient sufficient conditions. Positivity of \(\gamma\) for each
   family member is insufficient. Uniform positive lower bounds are not
   necessary if the displayed residual-to-rate ratios stay bounded as
   the rates vanish. The convenient condition
   \(\varepsilon\leq k/G\), together with common bounds on
   \(H_f,|r(0)|\) and a positive lower bound for \(k\), yields (27).

The synthesis's observable estimate is valid: Taylor expansion from
\(\widehat X\), with the gradient bound \(G\) there and connector curvature
bound \(H_f\), gives

\[
 |f(\widehat X)-f(X)|
 \leq G\|\widehat X-X\|_g+
       \frac{H_f}{2}\|\widehat X-X\|_g^2.
\]

The synthesis's weaker trapezoid remainder bound is also valid; the factor
\(1/2\) proved in (24) is an optional refinement that does not alter its
displayed all-time conclusion.
