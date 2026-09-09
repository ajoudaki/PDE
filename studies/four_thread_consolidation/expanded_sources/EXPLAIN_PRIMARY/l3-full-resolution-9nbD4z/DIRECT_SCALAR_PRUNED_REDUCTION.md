# Direct scalar comparison and accumulated rare forcing

This note gives two scalar comparison identities and an exact
rank-memory cancellation for the actual versus fully pruned lower flow.
It does not prove global population existence or uniqueness. Its new
consequence is that accumulated rare-row training and accumulated rare
forcing of the transformed first layer can be controlled without a tail
bound on the rare backward field, provided the explicit residual below
is controlled.

All inner products and vector norms use normalized Euclidean measure.
Matrix norms are operator or Hilbert--Schmidt norms. Write
\(d(z)=1/(1+z^2)\), \(F(z)=z+z^3/3\), and \(a=\pi/2\).

## 1. A scalar flow-map identity with reference-only gain

Consider scalar absolutely continuous solutions of
\[
 z'=\alpha(s)d(z)q+g,\qquad
 \widehat z'=\alpha(s)d(\widehat z)\widehat q+\widehat g.
\]
Here \(\alpha\) is bounded and the scalar controls are integrable in
time. Such scalar equations have unique global solutions on finite
intervals: their drift has an integrable state-Lipschitz bound and
\(|z'|\le|\alpha q|+|g|\).

Set \(e=z-\widehat z\), \(V=F(z)-F(\widehat z)\), and
\[
 L=1+\frac{z^2+z\widehat z+\widehat z^2}{3},
 \qquad c(z,\widehat z)=\frac{z+\widehat z}{L}.
\]
Then \(V=eL\) and the exact finite-pair identity is
\[
 V'=\alpha(q-\widehat q)
       +(1+z^2)(g-\widehat g)
       +c(z,\widehat z)\widehat g\,V.                    \tag{1}
\]
Indeed \(F(z)'=\alpha q+(1+z^2)g\). Moreover \(|c|\le1\):
with \(u=z+\widehat z\), \(v=z-\widehat z\),
\(L=1+u^2/4+v^2/12\ge |u|\).

Thus the propagator in (1) is bounded by
\(\exp(\int|\widehat g|)\), involving only the reference forcing.
For equal initial states and \(g=\widehat g\),
\[
 |z(t)-\widehat z(t)|
 \le e^{\int_0^t|g|}
           \int_0^t|\alpha(q-\widehat q)|\,ds.           \tag{2}
\]
In particular when \(g=0\), this is a global \(L^1_tL^2_x\)-to-\(L^2_x\)
Lipschitz input-to-state estimate, with no \(L^p\), exponential, or
Osgood tail condition on \(q\). It concerns the scalar mobility module,
not the full nonlocal action flow.

If the forcings differ, the remaining term is exactly
\((1+z_{\rm actual}^2)(g-\widehat g)\). Replacing this actual-state factor
by the reference factor changes the transport coefficient from
\(\widehat g\) to \(g\); both improvements cannot simply be taken at once.

## 2. Fully pruned reference and a direct amplitude bound

Fix a middle index set \(E\), of normalized mass \(p\), and use the fully
pruned network of PRUNED_GAUSSIAN_SUBSET_BOUND.md. Its middle backward
field vanishes on \(E\). Its unused rare preactivation is
\[
 \widehat z_E=P_EW^{(2)}_0\widehat h^{(1)},\qquad
 \widehat z_E'=\widehat g_E
       :=P_EW^{(2)}_0(\widehat h^{(1)})'.
                                                               \tag{3}
\]
In particular its scalar backward control in the rare-coordinate
comparison is zero, not the unused top transpose query.

Choose the scalar reference coefficient
\[
 \alpha(s)=\|\widehat h^{(1)}(s)\|_2^2
              +\mathbb E[d(\widehat z^{(1)}(s))^2].
\]
The elementary arctangent bound gives
\[
 1/4\le\alpha\le a^2+1.
\]
Its derivative is uniformly bounded on a finite horizon:
\[
 |\alpha'|
 \le 2a\|(\widehat h^{(1)})'\|_2
       +4\|(\widehat z^{(1)})'\|_2\le C_S.
\]
Thus \(\beta=1/\alpha\) and \(\beta'\) are uniformly bounded.

For the actual network, let
\[
 \delta_E=P_E\delta^{(2)},\quad
 e=P_Ez^{(2)}-\widehat z_E,\quad
 B_E=P_EA_2P_E-\alpha I_E,
\]
and define the exact residual
\[
 \rho=B_E\delta_E+
    P_EA_2(I-P_E)\delta^{(2)}-\widehat g_E.                \tag{4}
\]
Then, with shared initialization,
\[
 e'=\alpha\delta_E+\rho,\qquad e(0)=0,\qquad
 \delta_E=d(\widehat z_E+e)q_E.                           \tag{5}
\]
The middle nonlocality has not been discarded: it is exactly (4).

A useful pointwise bound for (5) avoids exponential gains altogether.
For each coordinate, put
\[
 B=\sup_{s\le S}|\widehat z_E(s)|,\quad
 R=\int_0^S|\rho(s)|\,ds,\quad
 Q=\int_0^S\alpha(s)|q_E(s)|\,ds.
\]
Then
\[
 \sup_{s\le S}|e(s)|\le B+2R+(3Q)^{1/3}.                 \tag{6}
\]
To prove it, write \(r(t)=\int_0^t\rho\) and \(y=e-r\).
Thus \(y'=\alpha d(y+r+\widehat z_E)q_E\).
For \(K=B+R\), the positive part \(w=(|y|-K)_+\) obeys
\[
 w'\le\frac{\alpha|q_E|}{1+w^2}\quad\hbox{a.e.}
\]
Since \(w(0)=0\), integrating gives \(F(w)\le Q\), hence
\(w\le(3Q)^{1/3}\). This proves (6).

Hölder and Minkowski now give the normalized bound
\[
 \begin{split}
 \left\|\sup_{s\le S}|e(s)|\right\|_2
 \le{}&\left\|\sup_{s\le S}|\widehat z_E(s)|\right\|_2
       +2\int_0^S\|\rho(s)\|_2\,ds\\
 &+3^{1/3}p^{1/3}
       \left(\int_0^S\alpha(s)\|q_E(s)\|_2\,ds\right)^{1/3}.
                                                               \tag{7}
 \end{split}
\]
The last factor is bounded by the existing primal estimates. This is
a rare-displacement estimate, not a bound on the time derivative \(e'\)
or on \(\delta_E^2\).

## 3. Exact integration of the rare rank updates

Write \(W_E=P_EW^{(2)}\), \(h=h^{(1)}\), and retain the actual training
equation \(W_E'=\delta_E\otimes h\). From (5),
\(\delta_E=\beta e'-\beta\rho\). Integration by parts yields exactly
\[
 W_E(t)-W_E(0)
 =\beta(t)e(t)\otimes h(t)
  -\int_0^t e\otimes(\beta h)'\,ds
  -\int_0^t\beta\rho\otimes h\,ds.                        \tag{8}
\]
There is no initial boundary contribution because \(e(0)=0\).

The contribution of the rare coordinates to the transformed first-layer
velocity \(X^{(1)\prime}=(W^{(2)})^*\delta^{(2)}\) is
\(W_E^*\delta_E\). A second exact integration by parts gives
\[
 \begin{split}
 \int_0^tW_E^*\delta_E\,ds
 ={}&\beta W_E^*e-\frac12\beta^2h\|e\|_2^2\\
 &-\int_0^t\beta'W_E^*e\,ds
   +\frac12\int_0^t(\beta^2h)'\|e\|_2^2\,ds\\
 &+\int_0^t\beta^2h\langle\rho,e\rangle\,ds
   -\int_0^t\beta W_E^*\rho\,ds.                          \tag{9}
 \end{split}
\]
To check the nontrivial term, use
\[
 (W_E^*)'=h\otimes\delta_E,\qquad
 \langle\delta_E,e\rangle
       =\frac{\beta}{2}(\|e\|_2^2)'
           -\beta\langle\rho,e\rangle.
\]
These are the actual rank update and (5); no independence is used.

Let \(E_*=\sup_{s\le S}\|e(s)\|_2\) and
\(R_1=\int_0^S\|\rho(s)\|_2\,ds\). The established bounds on
\(\beta,\beta',h,h'\), and \(W_E\) imply from (8)--(9)
\[
 \sup_{t\le S}\|W_E(t)-W_E(0)\|_{\rm HS}
       \le C_S(E_*+R_1),                                 \tag{10}
\]
\[
 \sup_{t\le S}\left\|\int_0^tW_E^*\delta_E\,ds\right\|_2
       \le C_S\big[E_*+E_*^2+(1+E_*)R_1\big].             \tag{11}
\]
Since the primal bounds also bound \(E_*\), (11) is at most
\(C_S(E_*+R_1)\). Large instantaneous rare backward values therefore
need not imply large accumulated rare parameter forcing.

## 4. The reference path amplitude has a simultaneous Gaussian bound

This supplies the reference quantity in (7), not a bound on the actual
path. Conditional on the fully pruned active initialization, the rows
\(P_EW^{(2)}_0\) are independent Gaussian rows and are independent of
the entire path \(\widehat h^{(1)}\). On an active-data norm event,
\[
 \|\widehat h^{(1)}(0)\|_2+
       \int_0^S\|(\widehat h^{(1)})'\|_2\,ds\le C_S.
\]
Use here the event
\(\|(I-P_E)W^{(2)}_0\|_{\rm op}\le M\) and
\(\|W^{(3)}_0(I-P_E)\|_{\rm op}\le M\). Deleted rows may be set to zero
when deriving the active-trajectory bounds, since they never enter the
pruned first-layer velocity. Select the zero path outside this event;
in particular the selection does not involve the deleted incoming rows.
For each \(i\in E\), define
\[
 B_i=\left|(W^{(2)}_0\widehat h^{(1)}(0))_i\right|
       +\int_0^S
        \left|(W^{(2)}_0(\widehat h^{(1)})'(s))_i\right|ds.
\]
Then \(B_i\ge\sup_s|\widehat z_{E,i}(s)|\), and conditional Gaussian
moments plus Minkowski imply
\[
 \|B_i\|_{L^r({\rm conditional})}\le C_S\sqrt r,\quad r\ge2.
\]
No time derivative of \((\widehat h^{(1)})'\) is required.
For a larger constant \(K_S\),
\(\mathbb E[\exp(B_i^2/K_S^2)\mid{\rm active\ data}]\le2\).
The \(B_i\) are conditionally independent across the deleted rows.
Consequently
\[
 \mathbb P\left(
    \sum_{i\in E}B_i^2>K_S^2(|E|\log2+u)\right)\le e^{-u}.
\]
A union bound with
\(u_m=m\log(en/m)+\log(n/\eta)\) gives, with probability at least
\(1-\eta\), simultaneously for all nonempty \(E\),
\[
 \frac1n\sum_{i\in E}\sup_{s\le S}|\widehat z_{E,i}(s)|^2
 \le K_S^2\left[
       \frac{|E|}{n}\log\frac{en}{|E|}
       +\frac{|E|}{n}\log2+\frac{\log(n/\eta)}n\right].
                                                               \tag{12}
\]
On the additional full initial operator-norm event all selected paths
are the genuine pruned paths. Its failure probability is the same
exponentially small Gaussian norm bound used in the existing pruned
lemma. Equation (12) is valid after choosing \(E\) from the full
trajectory because it holds simultaneously. It is stronger than
interchanging a time supremum and an empirical norm without proof.

## 5. Optional scalar shadow and the exact remaining obligation

One can also construct a globally defined scalar shadow driven by the
pruned Gaussian probes
\[
 Q_i(s)=[(W^{(3)}_0)^*\widehat\delta^{(3)}(s)]_i,\qquad
 G_i(s)=[W^{(2)}_0(\widehat h^{(1)})'(s)]_i,
\]
with initial value \(Z_i(0)=[W^{(2)}_0h^{(1)}(0)]_i\), by solving
\[
 Z_i'=\alpha(s)d(Z_i)Q_i+G_i.
\]
Conditional on the pruned active data, its controls are Gaussian.
The pointwise bound
\[
 \sup_{s\le S}|Z_i(s)|
 \le |Z_i(0)|+\int_0^S(|\alpha Q_i|+|G_i|)\,ds
\]
and Gaussian Minkowski bounds give Gaussian supremum tails for this
scalar shadow. This auxiliary shadow is not the pruned network:
the genuine pruned rare field obeys (3), with zero backward control.
The direct cancellation (8)--(11) uses the genuine pruned reference.

For the target network, the explicit unresolved term is (4).
The new Gaussian rare-block geometry can bound
\(\|B_E\|_{\rm op}\); multiplying this by the already bounded
\(\|\delta_E\|_2\) controls its contribution to \(R_1\).
What is still needed is a full/pruned estimate on the off-block forcing
\[
 P_EA_2(I-P_E)\delta^{(2)}-\widehat g_E,
\]
coupled to the active bulk differences. Equations (7), (10), and (11)
then turn that estimate into small accumulated rare forcing, without
first proving an exponential tail for the actual rare backward field.
No estimate closing that bulk feedback, and hence no all-time
population well-posedness theorem, is proved here.
