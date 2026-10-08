# From finite response programs to a continuous all-time law

2026-10-07. Internally checked lead theorem. This is a **conditional transfer theorem**:
uniform finite-width carrier budgets and fitting tails are hypotheses. It
proves a qualitative all-time law, not a dense-variability width rate. It
uses the finite-program theorem and common Hilbert realization in this
study. The latter has passed a scoped internal audit.

The authorized integrated source states relevant exponential budgets in
(S.11), their removal in (S.29), and real fitting/tail bounds. Their complete
upstream deletion proof has not been independently audited here. The theorem
below states exactly what is needed; source identification is not an extra
unstated premise or a claim that this study verified that upstream proof.

## 1. Assumptions and conclusion

Use the canonical depth-\(L\), width-\(n\) network, fixed training data and
labels, zero initial readout, Gaussian initialization, and physical gradient
flow already specified in FINITE_RESPONSE_MEMORY.md. Activations are globally
Lipschitz, their derivatives are bounded Lipschitz gates, and they have at
most linear growth. Let \(p\ge m\) be a fixed declared input panel.

For each fixed \(T<\infty\), assume events with probability tending to one
on which the dense flow exists on \([0,T]\), and all the following hold
with constants independent of \(n\):

1. Initial/learned hidden operators and the normalized first operator have
   norm at most \(M\). The readout RMS, training residual RMS and all panel
   feature RMS norms are bounded.
2. For every training sample and layer, the backward carrier before its
   derivative gate satisfies
   \[
   \sup_{0\le t\le T}\frac1n\sum_i
   \exp(|k_{a,i}^{(\ell)}(t)|/A)\le B,
   \qquad A>0,\quad B<\infty.
   \tag{1}
   \]
   The top carrier is the readout. Constants may depend on \(T\), data,
   labels, depth and activation bounds.
3. For the all-time conclusion, the flow exists globally on events with
   probability tending to one and has an endpoint with deterministic tail
   \[
   \sup_{v\ {\rm in\ panel}}|f_n(t,v)-f_n(\infty,v)|
   \le \tau(t),\qquad \tau(t)\longrightarrow0.
   \tag{2}
   \]
   The same tail applies at every sufficiently large width on those events.

The finite-program law supplies no part of assumptions 1--3 by itself.

**Conclusion.** The compatible finite-mesh scalar response laws converge to
a unique global strong gradient-flow solution in their common Hilbert
realization. Its predictions \(f_\infty(t,v)\) are deterministic. For the
declared panel,
\[
\sup_{t\in[0,\infty]}\max_v
|f_n(t,v)-f_\infty(t,v)|\longrightarrow0
\quad\hbox{in probability}.
\tag{3}
\]
Without assumption 3, the same statement holds on every fixed compact time
interval. Forward feature Grams and training backward Grams also converge
uniformly on compact time intervals. No all-time hidden-Gram convergence
is claimed.

If the operator/readout bounds and (2) are uniform on the unit input sphere,
the prediction conclusion holds uniformly over that sphere as well. No
validation labels enter the flow.

There is no width rate in (3). In particular it does not assert
\(n^{-1/2+o(1)}\) accuracy, despite the fixed-program width theorem.

## 2. A width-independent one-sided vector-field modulus

Use the physical parameter distance
\[
\|\Delta\theta\|_{\mathcal H}^2
=\|\Delta A\|_F^2/n+
\sum_{\ell=2}^L\|\Delta W_\ell\|_F^2+
\|\Delta w\|_2^2/n.
\tag{4}
\]
Distances compare states with the same initialized operators. In the limiting
realization replace normalized vector norms by probability \(L^2\) norms
and hidden increment norms by Hilbert--Schmidt norms.

A reference state obeying assumption 1 has a width-independent velocity
bound \(V\). Indeed its backward RMS bounds follow recursively from
\(\|\delta_\ell\|_{2,n}\le sM\|\delta_{\ell+1}\|_{2,n}\) and
\(\|\delta_L\|_{2,n}\le s\|w\|_{2,n}\), where \(s\) bounds activation
derivatives. Each hidden gradient block has norm at most
\((2/m)\sum_a|c_a|\|\delta_{\ell,a}\|_{2,n}
\|h_{\ell-1,a}\|_{2,n}\); the first and readout blocks have the analogous
bounds. Their finite sum bounds (4)'s velocity.

Let a second state be at distance \(e\le1\). Its operator norms increase
by at most one, and its readout/feature/backward RMS norms remain bounded
by constants independent of \(n\), by linear growth and forward/backward
recursion. Forward subtraction gives
\[
\|z'_{\ell,a}-z_{\ell,a}\|_{2,n}\le P_\ell e.
\]
For example take \(P_1=1\) and
\(P_\ell=H_{\ell-1}+(M+1)sP_{\ell-1}\), where \(H_{\ell-1}\)
bounds the reference feature RMS. Prediction and deficit differences are
then bounded by another fixed multiple of \(e\).

For the changed derivative gate use only the reference carrier tail.
From (1), for \(R>0\),
\[
\|k\mathbf1_{|k|>R}\|_{2,n}^2
\le B\sup_{x>R}x^2e^{-x/A}.
\]
For \(R\ge2A\) this is at most \(BR^2e^{-R/A}\).
Subtracting the gated product and splitting the reference carrier gives
\[
\begin{aligned}
\|\phi'(z')k'-\phi'(z)k\|_{2,n}
\le{}&s\|k'-k\|_{2,n}
+t_2R\|z'-z\|_{2,n}\\
&+2s\|k\mathbf1_{|k|>R}\|_{2,n},
\end{aligned}
\tag{5}
\]
where \(t_2\) bounds the real second derivative. Choosing
\(R=4A\log(\exp(1)/e)\) shows that the last two terms are at most
\(C e\log(\exp(1)/e)\). At \(e=0\) the conclusion follows directly.

At each lower backward layer, subtraction of its carrier costs at most
\((M+1)\|\Delta\delta_{\ell+1}\|_{2,n}
+e\|\delta_{\ell+1}\|_{2,n}\).
Thus backward recursion adds finitely many copies of the modulus in (5);
it does not compose logarithms at each layer. Subtracting the three factors
in a hidden gradient update and the two in a readout update proves
\[
\|F(\theta')-F(\theta)\|_{\mathcal H}
\le C\,\omega(e),\qquad
\omega(e)=e\log(\exp(1)/e),\quad0<e\le1.
\tag{6}
\]
Set \(\omega(0)=0\). All constants depend only on the stated bounds, depth,
activation constants and fixed data, not width. No exponential budget of
the perturbed state is required. This one-sided feature is crucial below.

## 3. Uniform finite-horizon Euler approximation

Let \(\theta_h\) be the polygonal Euler interpolation on mesh \(h\), and
let \(\theta\) be an exact reference flow on its good event. Stop when
the error envelope \(E\) defined below first reaches one. Before this exit,
\[
\|\theta_h(\lfloor s/h\rfloor h)-\theta(s)\|_{\mathcal H}
\le e(\lfloor s/h\rfloor h)+Vh,
\quad
e(t)=\|\theta_h(t)-\theta(t)\|_{\mathcal H}.
\]
Apply (6) with reference \(\theta(s)\), not with the Euler state. Consequently
the running envelope \(E(t)=(V+1)h+\sup_{u\le t}e(u)\) satisfies
\[
E(t)\le(V+1)h+C\int_0^t\omega(E(s))\,ds
\tag{7}
\]
while \(E\le1\). Monotonicity of \(\omega\) on \([0,1]\) justifies this
replacement of past errors by their running envelope.

The scalar equality \(v'=Cv\log(\exp(1)/v)\), \(v(0)=(V+1)h\), has solution
\[
v(t)=\exp(1)
\left(\frac{(V+1)h}{\exp(1)}\right)^{e^{-Ct}}.
\tag{8}
\]
Its usual integral comparison follows, for example, by replacing the
initial value by a strictly larger one and applying a first-crossing
argument, then taking its decreasing limit. For fixed \(T\), choose \(h\)
so that (8) is below \(1/2\) on \([0,T]\). Equations (7)--(8) prevent the
envelope exit and give
\[
\sup_{t\le T}\|\theta_h(t)-\theta(t)\|_{\mathcal H}
\le \varepsilon_T(h),\qquad
\varepsilon_T(h)=\exp(1)
\left(\frac{(V+1)h}{\exp(1)}\right)^{e^{-CT}}
\longrightarrow0.
\tag{9}
\]
This bound is uniform in width on the source event. Euler states themselves
need no exponential carrier budget.

Forward evaluation is Lipschitz in (4) on these bounded states. Training
backward evaluation has the one-sided modulus from (5). Hence their finite
panel fields and pairings inherit errors tending to zero uniformly in \(n\).
The same argument applies to any bounded horizon endpoint interpolation.

## 4. The meshes converge in one common Hilbert space

Use the common realization constructed in RESPONSE_HILBERT_REALIZATION.md,
including a countable family of rational meshes on all integer horizons.
For two fixed meshes, execute their finite-width Euler programs on the same
initialized matrices. Concatenating them is still an allowed finite program.

Their parameter-distance square has a deterministic limit: readout and
first-layer differences are finite field combinations; hidden increments
are finite sums of rank-one fields; and
\[
\langle u\otimes v,u'\otimes v'\rangle_{\rm HS}
=\langle u,u'\rangle\langle v,v'\rangle.
\]
Every required factor is an empirical pairing covered by the finite-program
law. Its limit is exactly the corresponding Hilbert parameter distance.

On the dense source event, the two meshes are at distance at most
\(\varepsilon_T(h)+\varepsilon_T(h')\), by (9). Convergence in probability
to a deterministic distance passes this inequality to their common Hilbert
realization. It holds at every rational time and hence every time by
continuity. The limiting Euler parameter paths are therefore uniformly
Cauchy on \([0,T]\). Completeness produces a continuous path \(\theta_\infty\).

The parameter vector field is continuous in the Hilbert norm: forward
Lipschitz maps are continuous, the bounded gated product is continuous by
the one-sided truncation argument, bounded-operator application is continuous,
and rank-one products are continuous in Hilbert--Schmidt norm. Along the
compact image of a fixed continuous path, this gives uniform convergence
of the Euler velocities evaluated at their left endpoints to
\(F(\theta_\infty(t))\). To verify uniformity, a contrary sequence of times
has a convergent subsequence; both parameter arguments then approach the
same point, contradicting continuity. Passing through the integral Euler
equations proves that \(\theta_\infty\) is a strong solution.

This is an existence argument by a controlled Cauchy approximation. It does
not incorrectly invoke a finite-dimensional existence theorem for an arbitrary
continuous vector field on an infinite-dimensional space.

## 5. Inherited bounds and uniqueness

Scalar RMS and Gram bounds transfer first at fixed mesh and then as
\(h\to0\). Operator bounds transfer by testing each generated vector in a
countable dense set, using finite-program pairings for
\((G+B_h)u\); the actual operator cap plus (9) gives the same inequality
in the limit. Boundedness and density extend it to all vectors.

To transfer (1), apply a fixed bounded Lipschitz truncation of
\(x\mapsto e^{|x|/A}\) to a training carrier. Its empirical average changes
by at most its Lipschitz constant times the RMS carrier error between the
dense flow and fixed-mesh Euler. That error tends to zero with \(h\) by
Section 3. The finite-program law identifies the Euler average. Passing
\(h\to0\), then increasing the truncation, gives (1) for the limiting
carrier by monotone convergence. This works at each time with the same
constant \(B\), so it yields the required uniform-in-time bound.

The resulting limiting flow can itself serve as the reference in (6).
Any other strong solution with the same initial state stays in a bounded
neighborhood locally. Its distance from the reference obeys the zero-initial
version of (7). The solution (8) started at an arbitrary positive floor tends
to zero when that floor decreases to zero, for every fixed time. Hence the
two solutions coincide locally, and continuation gives uniqueness on every
bounded horizon. Constructions on nested integer horizons consequently agree.
Their union is the asserted global strong flow.

## 6. Prediction convergence and the endpoint

Fix \(T\) and first choose a mesh making (9) and the limiting-mesh error small.
At that fixed mesh, the finite-program theorem gives convergence in probability
of all its finitely many outputs to the deterministic aggregate outputs.
Interpolation is a fixed finite combination; bounded evaluation maps and
a finite time net therefore give uniform convergence over \([0,T]\).
Triangle inequalities with the two mesh errors prove compact-time output
convergence. The same reasoning gives forward Grams and training backward
Grams.

Under assumption 3, for every \(s\ge t\),
\(|f_n(s,v)-f_n(t,v)|\le\tau(s)+\tau(t)\).
No monotonicity of \(\tau\) is assumed. Its decreasing tail envelope
\(\sup_{u\ge t}\tau(u)\) tends to zero and can be used in the next argument.
Pass to the compact-time limit at fixed \(s,t\). The resulting deterministic
limit is Cauchy as \(t\to\infty\), uniformly on the finite panel, and thus has
an endpoint. Passing the original tail inequality through endpoint truncations
gives the limit's corresponding vanishing tail. Combining a large fixed
horizon, its compact-time convergence, and the two tails proves (3).

For the whole sphere, bounded first/hidden operators and readout give a
uniform input Lipschitz bound
\[
|f_n(t,v)-f_n(t,u)|\le R(sM)^L\|v-u\|_2,
\]
where \(R\) bounds readout RMS; the limiting evaluation has the same bound.
Finite sphere nets extend finite-panel convergence to the uniform input norm,
then the common tail extends it to all time.

## 7. Why this still does not meet the final accuracy target

At fixed mesh the width error has an explicit root-width rate, but its
constant and logarithmic exponent depend on that mesh's program and history
gaps. Section 3 chooses finer meshes to reduce a separate discretization
error. No estimate in this note controls how those width constants grow
when the mesh is refined. The proof uses the order: choose horizon and mesh,
then take width large. It gives no simultaneous root-width rate.

Nor does a dense-versus-dense fluctuation bound supply the missing bias rate:
the scalar example \(X_n=X+n^{-1/4}+n^{-1/2}Z\), with independent centered
unit-variance copies of \(Z\), has root-width iid-copy differences but
\(n^{-1/4}\) distance of its mean from its limit. This is a logical warning,
not a model of neural behavior.

The continuous limit can be characterized by its finite causal response
programs and common Hilbert gradient flow. Passing the explicit derivative
response sums to continuous response measures requires additional control.
Neither a finite autonomous memory bound nor the all-time dense-variability
accuracy requirement has been proved here.

Scoped audit: CONTINUOUS_RESPONSE_AUDIT.md checked the complete construction,
including mixed-mesh Hilbert distances, the integral limit, carrier-budget
transfer, uniqueness, passive outputs and endpoints. Its endpoint correction
and stopping-envelope clarification are incorporated above. The upstream
finite-width assumptions and any quantitative width rate remain outside
that verdict.
