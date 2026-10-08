# Continuous reciprocal susceptibility: measures, instantaneous response, and a proved local case

2026-10-07. Scoped derivation. There are two results:

1. A conditional passage from the finite Gaussian-response identity to
   continuous response measures, with explicit conditions identifying those
   measures as expected total functional derivatives.
2. An actual small-activity theorem for the canonical two-hidden-layer
   linear-activation network with one training input. Its response kernels
   exist and are limits of the Euler derivatives; derivative convergence is
   proved rather than assumed.

The second result does not prove the corresponding susceptibility bounds
for general nonlinear activations. Finite-depth scalar circuits and finite
residual activity alone do not supply the missing uniform derivative estimate.

Scientific inputs were the complete RESPONSE_GAUSSIAN_CLOSURE.md at SHA-256
2da1253b43750e6d641e26298dee3ba9acd74527d97651bb1c180013a61ea73c,
RESPONSE_HILBERT_REALIZATION.md at
09e36b34b0172aa88040d575cf1cab1baa0a73d3e51c98eb9970c2f04e14dc07,
CONTINUOUS_RESPONSE_LIMIT.md at
cd2121787ad56a6acd6643879e827320851cbb4d9dfa3e84401138c8ee34a6fd,
the exact equations in FINITE_RESPONSE_MEMORY.md, and my own Osgood note.
No external source or other study was used. The instantaneous recursion
below was also communicated by the lead after I had derived its matrix
version; the derivation here checks it directly.

## 1. One interface and the meaning of response

Fix a hidden interface \(G_\ell:H_{\ell-1}\to H_\ell\), with \(\ell\ge2\).
There are \(m\) training samples, indexed by \(a,b\); passive inputs can be
added without changing the argument. Put
\[
H_a(t)=h_{\ell-1,a}(t),\qquad
D_a(t)=\delta_{\ell,a}(t),\qquad
g_a(t)=G_\ell H_a(t),\qquad x_a(t)=G_\ell^*D_a(t).
\]
All fields are elements of their population's probability \(L^2\) space.
The forward and backward two-time Grams are
\[
C_{ab}(t,s)=\mathbb E[H_a(t)H_b(s)],\qquad
Q_{ab}(t,s)=\mathbb E[D_a(t)D_b(s)].
\]

For a physical Euler mesh \(t_k=kh\), the finite response theorem gives
\[
\begin{aligned}
g_a^k&=\eta_a^k+
\sum_{j<k,b}D_b^j\,r^h_{ab}(k,j),\\
x_a^k&=\xi_a^k+
\sum_{j\le k,b}H_b^j\,r^\delta_{ab}(k,j),
\end{aligned}
\tag{1}
\]
where
\[
r^h_{ab}(k,j)=
\mathbb E\frac{\partial H_a^k}{\partial\xi_b^j},\qquad
r^\delta_{ab}(k,j)=
\mathbb E\frac{\partial D_a^k}{\partial\eta_b^j}.
\tag{2}
\]
Forward evaluation at a step precedes backward evaluation. The derivatives
are total derivatives through that local population's formal scalar circuit.
Every deterministic moment, residual, covariance, and already constructed
response coefficient is held fixed. These are not derivatives of the
globally self-consistent law when all its moments are simultaneously changed.
They are also not derivatives with respect to whitened Gaussian innovations.

The primitive families are centered Gaussian, with
\[
\mathbb E[\eta_a^k\eta_b^j]=C_{ab}(t_k,t_j),\qquad
\mathbb E[\xi_a^k\xi_b^j]=Q_{ab}(t_k,t_j).
\tag{3}
\]
Distinct primitive families and the Gaussian roots are independent, with
the population conventions of the finite theorem. Singular covariance is
allowed.

The measures corresponding to (2) are
\[
\mu^{h,h}_{ab,t_k}=\sum_{j<k}r^h_{ab}(k,j)\,\delta_{t_j},\qquad
\mu^{\delta,h}_{ab,t_k}=\sum_{j\le k}r^\delta_{ab}(k,j)\,\delta_{t_j}.
\tag{4}
\]
There is no extra factor \(h\) in (4). A regular response density requires
the derivative itself to be \(h\) times that density. A same-time derivative
of order one instead becomes a Dirac mass.

## 2. The current-time Dirac coefficient

Assume \(C^2\) activations with bounded \(\phi'\) and \(\phi''\), as supplied
by the stipulated strip regularity. Write \(k_{\ell,a}(t)\) for the carrier
before the derivative gate:
\[
\delta_{\ell,a}(t)=\phi_\ell'(z_{\ell,a}(t))k_{\ell,a}(t).
\]
At a fixed Euler time, the current forward field satisfies
\[
\frac{\partial z_{\ell,a}^k}{\partial\eta_{\ell,b}^k}
=\mathbf1_{\{a=b\}},
\tag{5}
\]
when deterministic global coefficients are frozen. Learned forward terms
and reciprocal forward terms contain only earlier local fields.

At the top layer \(k_{L,a}=w\), and \(w^k\) was constructed from earlier
steps. Therefore the current response is diagonal:
\[
r^\delta_{L;ab}(k,k)=\mathbf1_{\{a=b\}}\chi_{L,a}^k,\qquad
\chi_{L,a}^k=\mathbb E[w^k\phi_L''(z_{L,a}^k)].
\tag{6}
\]
Induct down the layers. At layer \(\ell\), the current part of its carrier
arising from the next initialized transpose is
\(\chi_{\ell+1,a}^k h_{\ell,a}^k\).
The fresh reverse primitive is held fixed, and every other local term
depends only on earlier local fields. The chain rule yields
\[
\boxed{
\chi_{\ell,a}^k=
\mathbb E[k_{\ell,a}^k\phi_\ell''(z_{\ell,a}^k)]
+\chi_{\ell+1,a}^k
\mathbb E[(\phi_\ell'(z_{\ell,a}^k))^2].
}
\tag{7}
\]
Off-diagonal entries remain zero. More generally, before using the diagonal
induction, the matrix formula is
\[
\chi_{\ell;ab}
=\mathbf1_{\{a=b\}}\mathbb E[k_{\ell,a}\phi_\ell''(z_{\ell,a})]
+\chi_{\ell+1;ab}
\mathbb E[\phi_\ell'(z_{\ell,a})\phi_\ell'(z_{\ell,b})].
\]
It reduces to (7) because the top matrix is diagonal.

Equation (7) is an exact finite-circuit identity, not a formal continuum
differentiation. If the mesh fields converge in \(L^2\), its coefficients
converge to the same expressions without superscripts. Bounded continuous
\(\phi''\), bounded \(\phi'\), and \(L^2\) carrier convergence suffice:
truncate the carrier, use convergence in probability for the gate, then
remove the truncation. No derivative of a limiting path functional is
needed for this atom calculation.

Forward responses have no current-step term in (1). Nevertheless, the
fact that \(j<k\) at every mesh does not alone rule out a new diagonal
atom in a limit: strict-past masses might concentrate near \(t\). Excluding
such additional atoms requires a quantitative absolute-continuity bound,
as specified next.

## 3. Conditional measure-limit theorem

Fix a bounded horizon \([0,T]\). Use the common Hilbert realization so that
all mesh query and answer fields have a common \(L^2\) meaning. Suppose:

1. \(H^h,D^h,g^h,x^h\) converge uniformly in time in population \(L^2\)
   to continuous fields \(H,D,g,x\). Evaluation is at mesh times approaching
   the requested time, or through a consistent interpolation.
2. For each \(a,b,t\), the deterministic signed measures in (4) converge
   weakly against continuous functions on \([0,T]\) to
   \(\mu^h_{ab,t},\mu^\delta_{ab,t}\), and their total variations are uniformly
   bounded. This superscript \(h\) on the limiting first measure denotes
   feature response, not a mesh size.
3. To assert that the only diagonal atom is (7), the strict-past parts have
   uniform absolute continuity. One sufficient version is a nonnegative
   integrable activity envelope \(a(s)\), Riemann-consistent discrete
   measures \(\lambda_h=\sum_j h a(t_j)\delta_{t_j}\), and a constant \(K_T\)
   such that the absolute strict-past response measures are at most
   \(K_T\lambda_h\). More generally it suffices that their absolute measures
   converge along subsequences only to measures absolutely continuous
   with respect to one fixed nonatomic finite measure.

Then there are centered Gaussian primitive fields with covariances
\[
\mathbb E[\eta_a(t)\eta_b(s)]=C_{ab}(t,s),\qquad
\mathbb E[\xi_a(t)\xi_b(s)]=Q_{ab}(t,s),
\tag{8}
\]
and the continuous reciprocal response identities are
\[
\boxed{
\begin{aligned}
g_a(t)&=\eta_a(t)+
\sum_b\int_{[0,t)}D_b(s)\,\mu^h_{ab,t}(ds),\\
x_a(t)&=\xi_a(t)+\chi_{\ell,a}(t)H_a(t)
+\sum_b\int_{[0,t)}H_b(s)\,\mu^{\delta,\mathrm{past}}_{ab,t}(ds).
\end{aligned}}
\tag{9}
\]
The integrals are Bochner integrals in population \(L^2\). Under condition
3 the feature response has no diagonal atom, and
\[
\mu^\delta_{ab,t}
=\mathbf1_{\{a=b\}}\chi_{\ell,a}(t)\delta_t
+\mu^{\delta,\mathrm{past}}_{ab,t}.
\]
Without condition 3, the same measure identity holds over \([0,t]\),
but one cannot identify its entire diagonal mass with (7).

### Proof

If \(U_h\to U\) uniformly in \(L^2\), \(\nu_h\) have bounded total variation,
and \(\nu_h\) converge weakly to \(\nu\), then
\[
\left\|\int U_h\,d\nu_h-\int U\,d\nu\right\|_2\longrightarrow0.
\tag{10}
\]
The replacement \(U_h\mapsto U\) costs at most the uniform \(L^2\) error
times total variation. Approximate the continuous \(L^2\)-valued function
\(U\) uniformly by a finite sum of fixed \(L^2\) vectors times continuous
scalar functions, using a finite time partition and interpolation.
Weak convergence applies to those scalar functions; the two uniform
approximation errors are again controlled by total variation. This proves
(10).

Apply (10) to the finite reaction sums. Subtract those sums from the
convergent actual answers. The primitive fields then converge in \(L^2\)
at every finite collection of times. Each such vector was Gaussian with
the covariance in (3), so its limit is Gaussian with covariance (8).
Finite-dimensional independence between the primitive families and roots
is preserved. This argument does not need Gaussian primitives belonging
to different meshes to be jointly Gaussian.

For condition 3, domination passes to the weak limit when tested against
nonnegative continuous functions. The limiting strict-past measures are
therefore dominated by a nonatomic measure and cannot acquire a diagonal
atom. The explicit current coefficients converge by (6)--(7), proving (9).
This completes the conditional passage.

Bounded total variation by itself yields weakly convergent subsequences
at countably many fixed times by a diagonal compactness argument. It does
not yield uniqueness of the limiting response measures, their time
regularity, or their identification as derivatives.

## 4. When the limiting measure really is a functional derivative

For a deterministic continuous probe \(q:[0,T]\to\mathbb R^m\), replace
\(\xi_b(t_j)\) by \(\xi_b(t_j)+\varepsilon q_b(t_j)\) in the formal mesh
local circuit, keeping all deterministic coefficients frozen. Denote the
resulting query by \(H_{a,h}^{\varepsilon,q}(t)\).
The finite chain rule gives
\[
\left.\frac{d}{d\varepsilon}
\mathbb E H_{a,h}^{\varepsilon,q}(t)\right|_{\varepsilon=0}
=\sum_b\int q_b(s)\,\mu^{h,h}_{ab,t}(ds).
\tag{11}
\]

A sufficient, explicit derivative-passage condition is:

- The shifted queries converge in \(L^1\), for each small fixed
  \(\varepsilon\), to \(H_a^{\varepsilon,q}(t)\).
- The limiting shifted query is \(L^1\)-differentiable at zero.
- There is a modulus \(\rho_q(r)\to0\), independent of the mesh, such that
  \[
  \left\|
  \frac{H_{a,h}^{\varepsilon,q}(t)-H_{a,h}^{0,q}(t)}{\varepsilon}
  -\left.\partial_\varepsilon
  H_{a,h}^{\varepsilon,q}(t)\right|_0
  \right\|_1
  \le \rho_q(|\varepsilon|).
  \tag{12}
  \]

Pass the mesh limit in the difference quotient and in (11), then let
\(\varepsilon\to0\). This proves
\[
\sum_b\int q_b(s)\,\mu^h_{ab,t}(ds)
=\mathbb E\left[
\left.\partial_\varepsilon H_a^{\varepsilon,q}(t)\right|_0\right].
\tag{13}
\]
The reverse formula follows by perturbing \(\eta\) and replacing \(H\) by
\(D\). Thus (9) has exactly the requested expected total functional
derivatives, interpreted as finite signed response measures. In particular,
evaluation \(q_a(t)\chi_{\ell,a}(t)\) is the Dirac component.

Conditions on one mesh's Gaussian moments do not imply (12) uniformly as
the number of gates grows. Uniform convergence of unperturbed fields also
does not imply convergence of derivatives. This distinction is essential.
On a singular primitive covariance support the individual measures may
depend on the formal off-support extension. As in the finite theorem,
only the resulting reaction fields are intrinsically forced by the
unperturbed Gaussian law.

## 5. Exact learned memory is separate from reciprocal response

Put \(\beta_b(s)=2c_b(s)/m\). Integrating the Hilbert parameter ODE gives,
without any susceptibility assumption,
\[
\begin{aligned}
z_{\ell,a}(t)
&=g_a(t)+\sum_{b\le m}\int_0^t
\beta_b(s)C_{\ell-1;ba}(s,t)\delta_{\ell,b}(s)\,ds,\\
k_{\ell-1,a}(t)
&=x_a(t)+\sum_{b\le m}\int_0^t
\beta_b(s)Q_{\ell;ba}(s,t)h_{\ell-1,b}(s)\,ds.
\end{aligned}
\tag{14}
\]
These are Hilbert--Schmidt rank-one integral identities. They describe
learned weights. Equations (9) describe repeated use of the initialized
Gaussian operator. Neither may be dropped or identified with the other.

## 6. An actual canonical small-activity theorem

Now take exactly two hidden layers, one unit training input, one label
\(y\), and \(\phi_1=\phi_2=\mathrm{id}\). This is an allowed analytic
activation, not a clipped proxy. In the common realization let
\(H_0=Z\) be a standard Gaussian lower-population root, let \(G\) be the
initialized bounded interface, and put
\[
H(t)=A(t)v,\quad W(t)=G+B(t),\quad
z(t)=W(t)H(t),\quad D(t)=w(t),\quad
f(t)=\langle w(t),z(t)\rangle,\quad \beta(t)=2(y-f(t)).
\]
The actual physical gradient flow is
\[
\dot H=\beta W^*w,\qquad
\dot B=\beta w\otimes H,\qquad
\dot w=\beta WH,\qquad (H,B,w)(0)=(Z,0,0).
\tag{15}
\]

### Global flow and deterministic coefficients

This vector field is polynomial in the Hilbert variables and is locally
Lipschitz on every bounded ball; operator application and rank-one products
are bounded multilinear maps. The integral equation is therefore a
contraction on a sufficiently short time interval in a bounded ball.
Moreover the exact gradient identity gives
\[
\frac{d}{dt}(y-f(t))^2
=-\|(\dot H,\dot B,\dot w)\|_{\mathcal H}^2.
\]
Consequently
\[
|\beta(t)|\le2|y|,\qquad
\|\theta(t)-\theta(0)\|_{\mathcal H}\le |y|\sqrt t.
\tag{16}
\]
The polynomial local Lipschitz constants are bounded on each resulting
finite-horizon ball, so continuation yields a unique global strong flow.
No carrier exponential budget is used for this linear-activation result.

The fixed Euler laws converge to this flow in the common Hilbert space by
the usual integral contraction/error estimate for this locally Lipschitz
vector field. The same bounds and Gaussian initial operator/root bounds
give width-uniform Euler comparison on each fixed horizon. Thus the
coefficients below are genuine canonical flow moments, not external
trajectory data:
\[
C(u,r)=\mathbb E[H(u)H(r)],\qquad
Q(u,r)=\mathbb E[w(u)w(r)].
\]
They and \(\beta\) are continuous.

### Kernel theorem

Fix \(T\). Let
\[
\alpha=\int_0^T|\beta(s)|\,ds,\qquad
K_0\ge\sup_{u,r\le T}\max\{|C(u,r)|,|Q(u,r)|\},
\]
and assume the strict small-activity condition
\[
\boxed{\alpha^2(4+K_0)<1.}
\tag{17}
\]
There exist unique continuous kernels \(K_h,K_\delta\), bounded in
absolute value by \(2\), on \(0\le s\le t\le T\), satisfying
\[
\begin{aligned}
K_h(t,s)
&=1+\int_s^t\beta(r)\int_s^r
\beta(u)\,[K_\delta(r,u)+Q(u,r)]K_h(u,s)\,du\,dr,\\
K_\delta(t,s)
&=1+\int_s^t\beta(r)\int_s^r
\beta(u)\,[K_h(r,u)+C(u,r)]K_\delta(u,s)\,du\,dr.
\end{aligned}
\tag{18}
\]
The reciprocal-response law is
\[
\boxed{
\begin{aligned}
g(t)&=\eta(t)+\int_0^t w(s)\beta(s)K_h(t,s)\,ds,\\
x(t)&=\xi(t)+\int_0^t H(s)\beta(s)K_\delta(t,s)\,ds,\\
\mathbb E[\eta(t)\eta(s)]&=C(t,s),\qquad
\mathbb E[\xi(t)\xi(s)]=Q(t,s).
\end{aligned}}
\tag{19}
\]
Both measures are absolutely continuous. The instantaneous coefficient
vanishes because \(\phi''=0\). The kernels in (18) are the actual frozen
local functional derivatives:
\[
\frac{\delta H(t)}{\delta \xi(s)}=\beta(s)K_h(t,s),\qquad
\frac{\delta w(t)}{\delta \eta(s)}=\beta(s)K_\delta(t,s),\qquad s<t.
\tag{20}
\]
They are deterministic in this linear local circuit, so expectation does
not change them.

### Proof of kernel existence and mesh convergence

On the closed sup-norm ball \(|K_h|,|K_\delta|\le2\), the integral map in
(18) differs from the pair of constant-one kernels by at most
\[
2(2+K_0)\int_0^T|\beta(r)|
\int_0^r|\beta(u)|\,du\,dr=(2+K_0)\alpha^2<1.
\]
It maps that ball into itself. For two kernel pairs the difference of
\((K_\delta+Q)K_h\), or its dual, is at most
\((4+K_0)\) times their sup distance. Thus the map's contraction constant
is at most
\[
q=\tfrac12(4+K_0)\alpha^2<\tfrac12.
\tag{21}
\]
Iterating the map gives a uniformly Cauchy sequence of continuous kernels;
its limit is the unique fixed point in the ball.

At a fixed Euler mesh, exact chain-rule induction gives
\[
r^h(k,j)=h\beta_j K_h^{(h)}(k,j),\qquad
r^\delta(k,j)=h\beta_j K_\delta^{(h)}(k,j),\qquad j<k,
\tag{22}
\]
where the discrete kernels satisfy
\[
\begin{aligned}
K_h^{(h)}(k,j)
&=1+h^2\sum_{j<u<r<k}
\beta_r\beta_u
[K_\delta^{(h)}(r,u)+Q_h(u,r)]K_h^{(h)}(u,j),\\
K_\delta^{(h)}(k,j)
&=1+h^2\sum_{j<u<r<k}
\beta_r\beta_u
[K_h^{(h)}(r,u)+C_h(u,r)]K_\delta^{(h)}(u,j).
\end{aligned}
\tag{23}
\]
This definition never divides by \(\beta_j\); when it is zero, (22) is
still valid. The sums are chronological, so these arrays are uniquely
defined algebraically.

Uniform Euler convergence makes \(\beta_h,C_h,Q_h\) converge uniformly
to \(\beta,C,Q\). The strict margin in (17) gives the same ball and a
contraction constant less than one for all sufficiently fine meshes.
Sample (18) on each grid. Uniform continuity of its integrands makes the
Riemann-sum consistency error tend uniformly to zero on the triangular
grid. Subtracting (23) from these sampled equations and using the
contraction bound gives
\[
\max_{j<k}
\bigl|K^{(h)}(k,j)-K(t_k,t_j)\bigr|
\le\frac{\text{consistency error}}{1-q_h}\longrightarrow0
\]
for the pair of kernels. In particular the response measures converge,
and their absolute masses are dominated by
\(2\sum_j h|\beta_j|\delta_{t_j}\).
The conditional measure theorem therefore proves (19).

For completeness, the frozen limiting local equations are linear Volterra
equations:
\[
\begin{aligned}
H(t)&=Z+\int_0^t\beta(r)\xi(r)\,dr\\
&\quad+\int_0^t\beta(r)\int_0^r
\beta(u)[K_\delta(r,u)+Q(u,r)]H(u)\,du\,dr,\\
w(t)&=\int_0^t\beta(r)\eta(r)\,dr\\
&\quad+\int_0^t\beta(r)\int_0^r
\beta(u)[K_h(r,u)+C(u,r)]w(u)\,du\,dr.
\end{aligned}
\tag{24}
\]
Their integral operator has norm at most
\((2+K_0)\alpha^2/2<1\) on continuous \(L^2\)-valued paths.
They therefore have unique solutions by a convergent geometric iteration.
Differentiating with respect to an added deterministic primitive probe is
now justified by bounded linearity, and the resulting equations are
exactly (18). This proves (20) and the uniform derivative passage, rather
than assuming either.

The small-activity condition is nonvacuous for every finite nonzero label.
From (16) one can take
\[
K_0=(1+|y|\sqrt T)^2,\qquad \alpha\le2|y|T.
\]
Thus it suffices to choose \(T>0\) such that
\[
4y^2T^2[4+(1+|y|\sqrt T)^2]<1.
\tag{25}
\]
The readout immediately moves when \(y\ne0\), and subsequent feature and
hidden-operator evolution is retained. This is not a frozen-feature or
zero-learning example. It remains a restricted linear-activation case,
not the requested general nonlinear all-time theorem.

## 7. Why the nonlinear extension is not proved by the same words

At every fixed mesh, the analytic canonical circuit has polynomially
bounded derivatives in finitely many Gaussian primitives. That proves
integrability for that mesh. It gives no bound uniform as the number of
Euler steps tends to infinity. Differentiating a gated product introduces
the unbounded carrier multiplied by \(\phi''\); repeated time propagation
can exponentiate its accumulated magnitude.

The Osgood flow estimate controls values, not these first derivatives.
A modulus \(e\log(\exp(1)/e)\) permits finite differences to grow like
\(e^{\,\exp(-Ct)}\), whose ratio to \(e\) diverges as \(e\downarrow0\).
It therefore cannot be used as a uniform differentiability estimate.

An elementary gated evolution illustrates the missing implication. Let
\(Z\) have density \(e^{-z}\) on \(z\ge0\), and solve
\[
\dot u=Z\sin u,\qquad u(0)=0.
\]
The unperturbed solution is identically zero, the gate has bounded
derivatives of every order, and
\(\mathbb E e^{Z/2}=2\). Yet sensitivity to an initial probe is
\[
\partial_{u(0)}u(t)\big|_0=e^{tZ},
\]
whose expectation is infinite for \(t\ge1\).
This is not claimed to be a canonical Gaussian-initialized neural
counterexample. It proves that finite activity and even a fixed
exponential carrier budget do not, as abstract estimates, justify an
arbitrarily long expected-derivative passage. Additional canonical
structure or a suitable small-activity bound must be used.

A potential nonlinear local proof would control the linearized Volterra
circuit in an integrable norm, then close the deterministic expected
response kernels by a contraction. Exponential carrier bounds could
control a small accumulated coefficient: Jensen's inequality bounds
\(\mathbb E\exp(\int a(s)|k(s)|\,ds)\) by a weighted average of
\(\mathbb E\exp(\alpha|k(s)|)\), where \(\alpha=\int a\).
But deriving a closed linearized inequality whose coefficient depends
only on already controlled quantities remains necessary. Putting the
unknown response norm inside that coefficient and then asserting it
bounded would be circular.

The present note proves the measure-transfer criterion, the exact
instantaneous coefficient, and an actual small-activity canonical case.
It does not establish nonlinear uniform susceptibility bounds, global
response-kernel existence, autonomous finite memory, or a width rate.
