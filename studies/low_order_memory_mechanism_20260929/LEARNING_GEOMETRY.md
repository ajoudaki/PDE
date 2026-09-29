# Learning geometry of the one-mode model

This is a scoped theoretical analysis of `MODEL.md`, with its exact nonlinear,
multi-input, finite-width dynamics and initialization. There is no comparison
trajectory, width limit, experiment, or independence assumption after training.
All general identities below retain arbitrary depth and the same fixed
operators in forward and transpose propagation. The scalar convergence theorem
is explicitly a narrower analytic benchmark. These are internally derived
results, not promoted book material.

## 1. A changing feature address for accumulated error credit

For q=1, define, at each hidden link and sample,

\[
u_{\ell,a}=B_{\ell,a,0}/\tau,
\qquad C_{\ell,a}=C_{\ell,a,0},\qquad
\gamma=\rho/\tau.
\]

Writing \(h_a=h_a^{\ell-1}\) within a fixed link gives the exact system

\[
\dot u_a=\gamma(h_a-u_a),\qquad
\dot C_a=r_a\delta_a^\ell,\qquad
W_\ell=W_{0,\ell}-\frac{2}{mn}\sum_a C_a u_a^T.
\tag{1}
\]

In particular,

\[
u_a(t)=\frac{h_a(0)+\int_0^t\rho(s)h_a(s)\,ds}{\tau(t)},
\qquad C_a(t)=\int_0^t r_a(s)\delta_a^\ell(s)\,ds.
\tag{2}
\]

The first is a residual-activity weighted feature average including the
specified initial interval. The second is accumulated signed error credit.
They are not a feature and its velocity. Differentiating the reconstruction,

\[
\dot W_\ell=-\frac{2}{mn}\sum_a
\left[r_a\delta_a^\ell u_a^T+
\gamma C_a(h_a-u_a)^T\right].
\tag{3}
\]

There are two distinct operations: attaching fresh error credit to the current
average feature, and changing the feature associated with all previously
accumulated credit. The latter can move a link even when its fresh credit is
zero. This is a stronger characterization than the rank bound.

Specifically, for a current sample b, the forward and backward operations are

\[
z_b^\ell=W_{0,\ell}h_b-
\frac2m\sum_a C_a\frac{u_a^T h_b}{n},
\tag{4}
\]

\[
\delta_b^{\ell-1}=\phi'(z_b^{\ell-1})\odot
\left[W_{0,\ell}^T\delta_b^\ell-
\frac2m\sum_a u_a\frac{C_a^T\delta_b^\ell}{n}\right].
\tag{5}
\]

Thus the learned part is an associative map: similarity of the current feature
to stored average features selects accumulated error directions. The same
associations operate in reverse when assigning credit. Neither direction
replaces the fixed operator by fresh randomness. The similarities change with
the network, so this is generally not a fixed-kernel model. Also,
\(\operatorname{rank}(W_\ell-W_{0,\ell})\le m\) says nothing by itself about
which associations help learning.

## 2. Exact residual and loss laws

Let \(\mathcal L=m^{-1}\sum_a r_a^2\). Use ordinary Euclidean/Frobenius norms.
For each link define the n-by-n matrices

\[
A_\ell=\sum_a r_a\delta_a^\ell(h_a^{\ell-1})^T,
\quad D_\ell=\sum_a r_a\delta_a^\ell u_{\ell,a}^T,
\quad T_\ell=\gamma\sum_a C_{\ell,a}
 (h_a^{\ell-1}-u_{\ell,a})^T.
\]

Also set

\[
Q_{\rm out}=\left\|\sum_a r_a h_a^L\right\|_2^2+
\left\|\sum_a r_a\delta_a^1x_a^T/\sqrt d\right\|_F^2.
\]

The derivatives of the loss with respect to the readout, first weight and a
hidden link are respectively

\[
\frac{2}{mn}\sum_a r_a h_a^L,\quad
\frac{2}{mn}\sum_a r_a\delta_a^1x_a^T/\sqrt d,\quad
\frac{2}{mn}A_\ell.
\]

Substitution of the actual velocities, including (3), gives

\[
\dot{\mathcal L}=-\frac{4}{m^2n}Q_{\rm out}
-\frac{4}{m^2n^2}\sum_{\ell=2}^L
\langle A_\ell,D_\ell+T_\ell\rangle_F.
\tag{6}
\]

In residual coordinates, define

\[
K^{\rm out}_{ba}=\frac1n\left[(h_b^L)^Th_a^L+
(\delta_b^1)^T\delta_a^1\frac{x_b^Tx_a}{d}\right],
\]

\[
K^{\rm credit}_{ba}=K^{\rm out}_{ba}+
\frac1{n^2}\sum_{\ell=2}^L
((\delta_b^\ell)^T\delta_a^\ell)
((h_b^{\ell-1})^Tu_{\ell,a}),
\]

\[
g_b=\frac{2\gamma}{mn^2}\sum_{\ell=2}^L\sum_a
((\delta_b^\ell)^TC_{\ell,a})
((h_b^{\ell-1})^T(h_a^{\ell-1}-u_{\ell,a})).
\]

The chain rule for \(f_b\) then yields

\[
\dot r=-\frac2m K^{\rm credit}r-g,
\qquad
\dot{\mathcal L}=-\frac4{m^2}r^T
\operatorname{sym}(K^{\rm credit})r-\frac2m r^Tg.
\tag{7}
\]

The current/average-feature kernel is generally nonsymmetric. The term g is
transport of accumulated credit, not external noise. At zero residual both
terms vanish: every interpolating state is absorbing. This fact alone does
not establish stability of a nearby state.

## 3. What guarantees that these associations improve the fit?

One diagnostic separates feature alignment from transport. At a given link,
put the vectors \(h_a,u_a,\delta_a^\ell\) into columns of \(H,U,\Delta\), and
write \(R=\operatorname{diag}(r_1,\ldots,r_m)\). Then

\[
\langle A_\ell,D_\ell\rangle_F
=\operatorname{tr}\!\left[R\Delta^T\Delta R\,
\operatorname{sym}(U^TH)\right].
\tag{8}
\]

The first matrix in the trace is positive semidefinite. If
\(\operatorname{sym}(U^TH)\succeq0\), the trace is nonnegative: writing
\(R\Delta^T\Delta R=\sum_i v_i v_i^T\) expresses it as a sum of
\(v_i^T\operatorname{sym}(U^TH)v_i\). Thus positive current/average feature
alignment guarantees that *fresh credit* does not increase loss at this link. Transport
still needs its own control. Neither condition follows from low rank.

A more quantitative sufficient statement keeps the entire nonlinear model.
Set \(E_\ell=D_\ell+T_\ell-A_\ell\), and suppose on an interval

\[
\left(\sum_\ell\|E_\ell\|_F^2\right)^{1/2}
\le\theta\left(\sum_\ell\|A_\ell\|_F^2\right)^{1/2},
\qquad 0\le\theta<1.
\tag{9}
\]

Cauchy--Schwarz in the collection of link matrices gives
\(\sum_\ell\langle A_\ell,A_\ell+E_\ell\rangle_F
\ge(1-\theta)\sum_\ell\|A_\ell\|_F^2\). Consequently,

\[
\dot{\mathcal L}\le-\frac4{m^2}
(1-\theta)r^TK^{\rm inst}r,
\tag{10}
\]

where the positive semidefinite instantaneous-gradient kernel is

\[
K^{\rm inst}_{ba}=K^{\rm out}_{ba}+
\frac1{n^2}\sum_{\ell=2}^L
((\delta_b^\ell)^T\delta_a^\ell)
((h_b^{\ell-1})^Th_a^{\ell-1}).
\]

Indeed \(r^TK^{\rm inst}r=Q_{\rm out}/n+
\sum_\ell\|A_\ell\|_F^2/n^2\), which verifies (10) and positivity directly.
If additionally \(K^{\rm inst}\succeq\lambda I_m\) for fixed \(\lambda>0\)
throughout this interval, integration of (10) proves

\[
\mathcal L(t)\le\mathcal L(t_0)
\exp[-4(1-\theta)\lambda(t-t_0)/m].
\tag{11}
\]

These are genuine sufficient conditions, not claims that the model
automatically satisfies them. Both feature mismatch and old-credit transport
enter (9); a bound on just one does not suffice.

## 4. A nonlinear all-depth benchmark with genuine feature learning

**Proposition.** Take m=n=d=1, x=1, y>0, tanh activation, any hidden depth
\(L\ge2\), \(W_1(0)>0\), and \(W_{0,\ell}>0\) for every hidden link. Use
the specified q=1 initialization, including w(0)=0. The solution exists for
all physical time, every hidden activation is nondecreasing, and

\[
0\le y-f(t)\le y\exp[-2h^L(0)^2t].
\tag{12}
\]

Every trainable layer changes for positive time while the residual is nonzero.
Thus one memory mode can support nonlinear feature learning through arbitrary
depth; it does not force a lazy or frozen-feature regime.

**Proof.** Write e=y-f and \(a_\ell=-C_\ell\). While e>0,

\[
\dot w=2eh^L,\quad \dot W_1=2e\delta^1,
\quad\dot a_\ell=e\delta^\ell,\quad
W_\ell=W_{0,\ell}+2a_\ell u_\ell.
\]

The positive initial features, the averaging formula (2), and
\(\tanh'>0\) preserve \(w\ge0,a_\ell\ge0,u_\ell>0,W_\ell>0\).
The exact backward recursion then gives \(\delta^\ell\ge0\), so \(W_1\)
and \(h^1\) are nondecreasing. If \(h^{\ell-1}\) is nondecreasing, (2)
implies \(u_\ell\le h^{\ell-1}\), whence \(\dot u_\ell\ge0\).
Both factors in \(2a_\ell u_\ell\) are nondecreasing, so \(W_\ell\)
and \(h^\ell=\tanh(W_\ell h^{\ell-1})\) are nondecreasing. This proves
the assertion through all layers by induction. Positivity is preserved at
each boundary because the displayed derivatives cannot point out of the
nonnegative region.

It follows that

\[
\dot f=\dot w h^L+w\dot h^L\ge2e(h^L)^2
\ge2e h^L(0)^2.
\]

At e=0 every raw velocity vanishes, and local uniqueness prevents crossing
this equilibrium. Therefore e stays nonnegative, and integrating
\(\dot e\le-2h^L(0)^2e\) proves (12) on the existence interval.

For completeness, the vector field is locally Lipschitz wherever \(\tau>0\),
including e=0, since \(\rho=|e|\). No finite-time escape occurs: (12) gives
\(\int_0^\infty e\,dt\le y/[2h^L(0)^2]\) and bounds \(\tau\).
Moreover \(w\le y/h^L(0)\), so \(\delta^L=w\tanh'(z^L)\) is bounded.
Integrating \(\dot a_L=e\delta^L\) bounds \(a_L\), and \(0<u_L\le1\)
then bounds \(W_L\). The recursion
\(\delta^{\ell-1}=\tanh'(z^{\ell-1})W_\ell\delta^\ell\), with
\(0<\tanh'\le1\), repeats this bound down all links. Finally
\(\dot W_1=2e\delta^1\) is integrable. All stored states stay bounded,
and \(\tau\ge1\), so the local solution extends globally. For t>0 with
e>0, w and all backward derivatives are strictly positive, making
\(\dot W_1>0\), \(\dot a_\ell>0\), and \(\dot W_\ell>0\). □

The proof uses scalar positive-sign order. It does not extend automatically
to vector features, competing samples, or arbitrary random signs.

## 5. Sharp limitations and falsifiers

**The equations have no unconditional gradient-flow sign.** An algebraic
state of the scalar two-hidden-layer model makes this explicit. Choose x=1,
\(h^1=-c<0\), \(u_2=v>0\), \(C_2=0\), \(W_{0,2}=W_2=0\), w>0,
and y nonzero. Then \(h^2=0\), \(\delta^1=0\), \(\delta^2=w\), and
\(r=-y\). All outer-loss dissipation is zero, while (6) gives

\[
\dot{\mathcal L}=4r^2w^2cv>0.
\]

The strict sign persists under sufficiently small perturbations of this
state. This refutes a state-independent Lyapunov claim based only on the
q=1 vector field. It is **not** a demonstrated reachable trajectory from the
mandatory initialization: reachability remains a separate obligation.

**Feature learning requires a seed error/feature correlation.** For the exact
mandatory initialization, if

\[
\sum_a y_a h_a^L(0)=0,
\tag{13}
\]

then w=0, all backward derivatives are zero, and all C remain zero. The
first and hidden weights therefore remain initial, all features stay fixed,
and \(\dot w=(2/m)\sum_a y_a h_a^L(0)=0\) closes the argument. Here
\(B_a=\tau h_a(0)\) and the clock may grow, but predictions remain zero
and nonzero loss never improves. This is an exact solution; local uniqueness
makes it the initialized solution. For example, tanh with input pair x,-x
and equal nonzero labels satisfies (13) for every realization of the initial
weights. That particular example also has an architectural odd-symmetry
obstruction, so it should not be presented as a memory-specific failure.

The defensible organizing statement is therefore conditional: q=1 learns by
repeatedly updating a small set of sample-associated average feature addresses
and their accumulated error directions. It can produce substantial nonlinear
feature adaptation; beneficial learning depends on current/address alignment
and how already stored credit is transported. General convergence, monotone
loss from all admissible initializations, implicit norm minimization, and a
preferred interpolating solution have not been established by these identities.
