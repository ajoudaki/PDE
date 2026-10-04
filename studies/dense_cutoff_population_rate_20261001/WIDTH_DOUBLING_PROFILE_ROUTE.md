# Width doubling through a matched block profile

2026-10-03. **Frozen bounded attempt; the trained contrast is open.**
This scoped note investigates the requested all-physical-time comparison
between independent canonical widths \(n\) and \(2n\), under the exact
fixed-depth, compatible-data, small-label, \(C^3\) bounded-derivative
assumptions of DEPTH_EXTENSION_RESULT.md. Activation values may grow
linearly. No theorem with an additional moment, derivative, or query-law
assumption is asserted.

The complete DECISIVE_CONDITIONAL_ROUTE.md was read for this continuation.
The completed depth sources and the complete GENERAL_SELF_AVERAGING.md
were read in the preceding continuation. Required process and canonical
notation instructions remain in force. No other study, experiment,
manuscript edit, or Git mutation is used. This file is the only write.
The coordinator supplied the bounded-variation control idea developed
in Section 4 after the initial profile calculation.

## 1. The exact autonomous interpolation

Set \(N=2n\). Split each hidden layer into two blocks of size \(n\), and
for every hidden edge \(e=(\ell,i,j)\), \(2\le\ell\le L\), set
\[
 c_e(s)=
 \begin{cases}
  2(1-s),&i,j\text{ have the same block label},\\
  2s,&i,j\text{ have opposite block labels},
 \end{cases}
 \qquad 0\le s\le\tfrac12.
 \tag{1}
\]
Initialize \(W_e(0)\sim N(0,c_e(s)/N)\), independently, and give that
hidden weight mobility \(c_e(s)\). First-layer and readout mobilities
remain \(N\), with their canonical initialization and zero readout.
Thus, for fixed positive training weights \(p_a\) summing to one,
\[
 \begin{aligned}
 \dot W^{(1)}&=-2\sum_a p_ar_a\delta_a^{(1)}v_a^\top,\\
 \dot W_e&=-{2c_e\over N}\sum_a p_ar_a
                         \delta_{a,i}^{(\ell)}h_{a,j}^{(\ell-1)},\\
 \dot w&=-2\sum_a p_ar_ah_a^{(L)},\qquad
 r_a=f_{N,s}(t,x_a)-y_a,\qquad v_a=x_a/\sqrt d .
 \end{aligned}
 \tag{2}
\]
The residual in (2) is the actual residual of this profiled network.

At \(s=1/2\) this is the canonical autonomous width-\(N\) flow. At
\(s=0\), the off-block weights vanish permanently. Its two canonical
width-\(n\) blocks satisfy
\[
 f_{N,0}=\tfrac12(f^{[1]}+f^{[2]}),\qquad
 r_a=\tfrac12(f^{[1]}(x_a)+f^{[2]}(x_a))-y_a .
 \tag{3}
\]
Both blocks are driven by this shared residual. Their initialized roots
are independent, but their trained paths are not independent autonomous
width-\(n\) flows. Equating the left endpoint mean with the canonical
width-\(n\) autonomous mean would be incorrect. The separate feedback
comparison at this endpoint is now proved in
WIDTH_DOUBLING_BLOCK_ROUTE.md and checked in
WIDTH_DOUBLING_BLOCK_CHECK.md. This note uses that completed bridge
as reported by the coordinator; it does not identify the two endpoint
laws exactly.

For \(0<s<1/2\), one convenient mobility-Euclidean coordinate is
\[
 \Theta_c=(W^{(1)},\widetilde H^{(2)},\ldots,
             \widetilde H^{(L)},w),\qquad
 W_e=\sqrt{c_e/N}\,\widetilde H_e .
 \tag{4}
\]
The initialized \(\widetilde H_e\) are standard Gaussians and the
training field is the Euclidean gradient field
\(-2\sum_a p_ar_a\nabla_{\Theta_c}(Nf_a)\).
This preserves the negative-Gram contraction used in response bounds.
Working instead in \(\sqrt N W\) coordinates and treating the
nonuniform mobility as if it were the identity would lose that
contraction. At the zero-variance endpoint, (4) is interpreted through
the original equations (2), not by dividing by zero.

## 2. Exact signed response identity and its obligations

Let \(Z=(W_e(0))_e\), before averaging over hidden initialization.
For fixed \(c,Z,W^{(1)}(0)\), let
\[
 q_N(t,x;c,Z,W^{(1)}(0))=\partial_t f_{N,c}(t,x).
 \tag{5}
\]
The derivatives below differentiate the entire autonomous trajectory,
including its residual feedback. In \(\partial_{c_e}\), initialized
entries \(Z\) are held fixed. Put
\[
 \mathcal R_e(t,x;s)=N^2\mathbb E
 \left[\partial_{c_e}q_N+{1\over2N}\partial_{Z_e}^2q_N\right]_{c=c(s)}.
 \tag{6}
\]
If the displayed derivatives are integrable and covariance
differentiation is justified, Gaussian integration by parts gives
\[
 {d\over ds}\mathbb E q_N(t,x;s)
 =\sum_{\ell=2}^L
       [\mathcal R_{\mathrm{out}}^{(\ell)}(t,x;s)
        -\mathcal R_{\mathrm{in}}^{(\ell)}(t,x;s)] .
 \tag{7}
\]
Each type has \(N^2/2\) edges in each layer, and \(c'_e=+2,-2\),
respectively. These counts give exactly (7). Block permutation symmetry
identifies the two expected values, but does not make them equal.
Equation (7) is conditional on its analytic hypotheses; the previously
proved high-probability canonical tube does not itself verify them.

A sufficient bias bridge for the profiled endpoints is
\[
 \int_0^\infty\int_0^{1/2}
 |\mathcal R_{\mathrm{out}}^{(\ell)}(t,x;s)
       -\mathcal R_{\mathrm{in}}^{(\ell)}(t,x;s)|\,ds\,dt
 \le {C B(x)\over\sqrt N}e^{C\sqrt{\log(e+N)}},
 \quad B(x)=1+\|x\|_2/\sqrt d.
 \tag{8}
\]
Indeed \(f_{N,s}(0,x)=0\), so integrating (7) gives a uniform physical
time bound of this size on the difference between the endpoint means.
The linear envelope \(B\) makes the prescribed finite second query
moment sufficient. A larger polynomial envelope is not an acceptable
replacement without an additional hypothesis on the query law.

The same covariance identity can instead be written directly for
\(f_N(t,x)\). That avoids the time derivative but then needs uniform
control in terminal time of its signed response. Neither version
allows an a priori bound on an unsigned response to stand in for the
signed contrast in (8).

## 3. A positive initialization calculation using only three derivatives

Here take two hidden layers and bounded \(C^3\) activations with bounded
first three derivatives. This paragraph is a partial calculation on a
subclass, not a restriction inserted into the requested final theorem.
At the zero-readout initialization and for a fixed instantaneous control
direction \(\beta=(\beta_a)\), \(\sum_a|\beta_a|\le1\),
\[
 q_{N,\beta}(0,x)
 ={1\over N}\sum_{a,i}\beta_a
       \phi_2(z_{a,i}^{(2)})\phi_2(z_{x,i}^{(2)}).
 \tag{9}
\]
The actual autonomous initial direction is \(\beta_a=2p_ay_a\);
rescaling accommodates its fixed norm.

For one training-query pair put
\[
 H_j=(h_{a,j}^{(1)},h_{x,j}^{(1)})^\top,\quad
 Q_i={1\over N}\sum_jc_{ij}H_jH_j^\top,\quad
 F(z)=\phi_2(z_1)\phi_2(z_2),\quad
 A(Q)=\mathbb E D^2F(Q^{1/2}G),
 \tag{10}
\]
where \(G\) is standard Gaussian in \(\mathbb R^2\).
Conditioning on the first layer and differentiating the tagged edge
twice yields
\[
 \mathcal R_{(i,j)}^{a,x}(0;s)
      ={1\over2}\mathbb E[H_j^\top A(Q_i)H_j].
 \tag{11}
\]
There is no mobility derivative at zero readout for (9).

Three bounded activation derivatives make \(D^2F\) globally Lipschitz.
The elementary positive-matrix square-root estimate
\(\|Q^{1/2}-\widetilde Q^{1/2}\|_F
 \le C\|Q-\widetilde Q\|_F^{1/2}\), in fixed dimension, therefore gives
\[
 \|A(Q)-A(\widetilde Q)\|
       \le C\|Q-\widetilde Q\|^{1/2}.
 \tag{12}
\]
One proof of the square-root estimate uses the resolvent formula
\[
 Q^{1/2}={1\over\pi}\int_0^\infty
               t^{-1/2}Q(Q+tI)^{-1}\,dt.
\]
For a difference \(E=Q-\widetilde Q\), the difference of integrands
has operator norm at most
\(t^{-1/2}\min\{2,\|E\|/t\}\). Splitting the integral at
\(t=\|E\|\) proves the claim, including singular matrices; fixed
dimension converts operator and Frobenius norms.

For tags \(j,k\) in opposite blocks, exchange the iid first-layer
vectors \(H_j,H_k\). The tagged vector becomes the same one in both
expectations, while the covariance changes by
\[
 \widetilde Q_i-Q_i
 ={2(1-2s)\over N}(H_kH_k^\top-H_jH_j^\top).
 \tag{13}
\]
Bounded features give \(\|\widetilde Q_i-Q_i\|\le C/N\). Hence
\[
 |\mathcal R_{\mathrm{out}}(0,x;s)
       -\mathcal R_{\mathrm{in}}(0,x;s)|\le C N^{-1/2}.
 \tag{14}
\]
Thus the initialization argument in DECISIVE_CONDITIONAL_ROUTE.md
does not need a fourth derivative at the requested root-width scale.
Its stronger \(O(N^{-1})\) conclusion used a Lipschitz covariance
response and hence four derivatives. Equation (14) is uniform in the
query for bounded first-layer activations.

For unbounded activation values, (10)--(13) remain meaningful for each
fixed input, but \(D^2F\) has a polynomially growing Lipschitz envelope
and \(H_j\) is unbounded. Gaussian moments then give a fixed-query
version with a polynomial query envelope. This calculation alone does
not establish the required linear envelope in (8), and is not claimed
to do so.

## 4. A bounded-variation improvement for linearized cavity probes

This section proves an abstract estimate for the actual linearized
probe kernels, conditional on their stated deterministic bounds.
It is not yet a theorem for the nonlinear trained edge contrast.

Normalize an activity interval to \([0,1]\). Let
\(\mathcal C_{A,R}\) consist of scalar controls \(b\) with
\(\|b\|_\infty\le A\) and total variation at most \(R\).
Piecewise-constant approximation on a uniform mesh of
\(m=\max\{1,\lceil 2R/\varepsilon\rceil\}\) intervals has \(L^1\) error at most
\(R/m\). Quantizing each value to mesh \(\varepsilon/2\) then proves
\[
 \log N(\varepsilon,\mathcal C_{A,R},L^1)
 \le C(1+R/\varepsilon)\log(2+A/\varepsilon).
 \tag{15}
\]
The same estimate, up to fixed-dimensional constants, applies to
finitely many training controls. Values at a specified terminal time
can be included as separate scalar coordinates of the index.

Let \(X\sim N(0,I_d/N)\), with \(d\le C_0N\), independent of the cavity.
Suppose a linearized retained-coordinate probe has the representation
\[
 L_b=X^\top a_b,\qquad
 a_b=\int_0^1 b(u)a(u)\,du,\qquad
 \sup_u\|a(u)\|_2\le K .
 \tag{16}
\]
Then its Gaussian increment metric is at most
\(K N^{-1/2}\|b-\widetilde b\|_{L^1}\).
Use nets of radii \(\varepsilon_j=A2^{-j}\). The Gaussian tail bound
and a union bound over pairs of successive net points bound the
expected maximum increment by
\(CKN^{-1/2}\varepsilon_j
 \sqrt{1+\log N(\varepsilon_j)}\).
The sum converges, because
\(\sum_j2^{-j/2}\sqrt{1+j}<\infty\). Consequently
\[
 \mathbb E\sup_{b\in\mathcal C_{A,R}}|L_b|
 \le {CK\over\sqrt N}\,[A+\sqrt{AR}].
 \tag{17}
\]
The same net proof gives Gaussian tails with an additional term
\(CKA\sqrt u/\sqrt N\) at failure probability \(Ce^{-u}\).
This is the sharp width power, unlike the single coarse net used to
prove polynomially small coordinate reinsertion errors.

For a centered quadratic probe
\[
 Q_b=X^\top T_bX-\operatorname{tr}(T_b)/N,
 \tag{18}
\]
suppose \(T_b\) is symmetric and its increments satisfy
\[
 \|T_b-T_{\widetilde b}\|_{\rm op}\le K\|b-\widetilde b\|_1,\qquad
 {\|T_b-T_{\widetilde b}\|_{\rm HS}\over\sqrt N}
                 \le K\|b-\widetilde b\|_1 .
 \tag{19}
\]
Diagonalizing a Gaussian quadratic form and multiplying its scalar
moment-generating functions gives the increment tail
\[
 |Q_b-Q_{\widetilde b}|
 \le CK\|b-\widetilde b\|_1
          \left(\sqrt{u/N}+u/N\right)
 \tag{20}
\]
outside probability \(2e^{-u}\). Chaining as above, stopped at
\(\varepsilon_J=N^{-1/2}\), gives the conditional expectation bound
\[
 \mathbb E\sup_{b\in\mathcal C_{A,R}}|Q_b|
 \le CK\left[
 {A+\sqrt{AR}+1\over\sqrt N}
 +{(A+R)\log^2(e+AN)\over N}\right],
 \tag{21}
\]
provided \(T_0=0\). The remaining approximation error is at most
\(KN^{-1/2}(\|X\|_2^2+d/N)\) by the operator estimate in (19).
If \(A<N^{-1/2}\), no chaining levels are needed: compare directly
with the zero control and use the same remainder estimate.
The extra squared logarithm in (21) is harmless for the requested
near-root rate. It comes from the elementary entropy bound (15);
no unproved finite gamma-one integral is used.
Equation (21) controls the centered quadratic form only. Its
uncentered trace mean \(\operatorname{tr}(T_b)/N\) must be retained
and bounded separately; it is not an error controlled by (21).

The exact linearized cavity forcing is
\[
 V(t)=\sum_{a,i}\int_0^tJ(t,u)
       [(P_a+Q_a)X_i a_{a,i}(u)+T_aY_i b_{a,i}(u)]\,du,
 \tag{22}
\]
where \(g_a=\nabla_\Theta(Nf_a)\),
\(d_a=\delta_a^{(j+1)}\), \(B_a=D_\Theta d_a\),
\(C_a=D_\Theta h_a^{(j-1)}\), and
\[
 P_a=-{2p_a\over N}g_ad_a^\top,\qquad
 Q_a=-2p_ar_aB_a^\top,\qquad
 T_a=-2p_ar_aC_a^\top .
 \tag{23}
\]
Crucially, \(P_a\) has no residual factor. An \(L^1\) norm in residual
activity alone is therefore not justified for the full kernel.
On a horizon \(T=C_T\log N\), use \(u/T\in[0,1]\) instead. The
operator bounds for the coefficients, the endpoint derivatives, and
\(J\) give \(K=e^{C\sqrt{\log N}}\) times powers of \(\log N\) in
(16), including the harmless additional factor \(T\).
Total variation is unchanged by this time reparametrization.
This verifies the claimed metric for the *linear* probes on that
horizon, conditionally on the required physical and carrier bounds.
It does not prove those bounds for the profiled network.

Time and retained-coordinate maxima add entropy factors. To invoke
(21) for a particular quadratic response, both estimates (19) must
be checked for that exact kernel; an operator bound alone is not the
Hilbert--Schmidt estimate. For the existing carrier reinsertion kernels,
the matrices have \(O(N)\) rows and columns, so an operator increment
bound \(K\|b-\widetilde b\|_1\) also bounds their Hilbert--Schmidt
increments by \(C\sqrt N K\|b-\widetilde b\|_1\). This verifies (19)
for those kernels. It does not verify a representation of the entire
second edge response (6) as one of those kernels.

These estimates permit bounded variation instead of a pointwise
Lipschitz control net. Their application to random actual controls
also needs a bound for their variation, dependence handled by the
uniform supremum, and the rare-event terms. Those are separate
conditions, not consequences of the abstract Gaussian calculation.

## 5. Conditional effect on the nonlinear state surgery

On a physical tube with carrier maximum \(M\), the exact forward and
backward time differentiations give
\[
 \int_0^\infty\|\dot h_a^{(\ell)}(t)\|_{\rm RMS}\,dt\le CS^2,\qquad
 \int_0^\infty\|\dot\delta_a^{(\ell)}(t)\|_{\rm RMS}\,dt
                                         \le CS(1+M).
 \tag{24}
\]
For the second estimate use
\[
 \dot\delta^{(\ell)}
 =\phi_\ell''(z^{(\ell)})\odot\dot z^{(\ell)}\odot k^{(\ell)}
 +\phi_\ell'(z^{(\ell)})\odot
   [\dot W^{(\ell+1)\top}\delta^{(\ell+1)}
                  +W^{(\ell+1)\top}\dot\delta^{(\ell+1)}],
\]
with the analogous top-layer formula. The term involving
\(\dot w\) is \(O(\rho)\), and all other terms are controlled by the
physical matrix speeds, \(M\), and finite depth.
Minkowski's inequality then yields
\[
 {1\over N}\sum_i\operatorname{TV}(h_{a,i}^{(\ell)})^2\le CS^4,\qquad
 {1\over N}\sum_i\operatorname{TV}(\delta_{a,i}^{(\ell)})^2
                                                \le CS^2(1+M)^2.
 \tag{25}
\]
These are deterministic implications of the tube. They apply to a
profiled tube if that tube is proved.

Let \(R_i\) be the sum of the variations of the finitely many controls
for tag \(i\). Under the logarithmic maximum bounds, their amplitudes
are bounded by a power of \(\log N\), while (25) gives
\[
 {1\over N}\sum_iR_i^2\le(\log N)^C,\qquad
                   \max_i R_i\le\sqrt N(\log N)^C.
 \tag{26}
\]
Dyadic variation classes and the tails behind (17), (21) permit one
Gaussian event of probability \(1-N^{-D}\), for any fixed \(D\), with
an extra logarithmic factor and uniform control over all classes up
to the second bound in (26). The kernels must be measurable with
respect to the cavity and independent of the deleted Gaussian roots.
The stated kernel representations and time-index control must also
be verified before adding time and coordinate maxima.
Conditional on these properties and the cavity operator bounds,
the resulting estimates have the form
\[
 \|V_i\|_2\le K,\qquad
 \max|\text{linear forward/backward coordinates of }V_i|
                   \le {K(1+\sqrt{R_i})\over\sqrt N},
 \qquad K=e^{C_D\sqrt{\log N}}(\log N)^{C_D}.
 \tag{27}
\]
The Euclidean bound also follows directly from (22), uniform control
amplitudes, and bounded Euclidean norms of the deleted Gaussian
rows/columns. The centered quadratic error has the additional term
\(KR_i\log^2 N/N\); for \(R_i\le\sqrt N(\log N)^C\) it can be
absorbed into the displayed scale by increasing \(K\).

Here is the precise conditional improvement of the old remainder
calculation. If (27) and the corresponding lower Gaussian-probe bounds
hold, each gate-square remainder costs
\(\|V_i\|_\infty\|V_i\|_2\), every mixed linear/remainder product uses
the coordinate bound on \(V_i\), and matrix cross products retain their
\(N^{-1/2}\) factor. The reverse-source curvature is treated by its
lower Gaussian probes exactly as in DEPTH_CAVITY_ROUTE.md.
Let \(u_i(t)\) be the running supremum of the Euclidean nonlinear
state remainder. On the horizon \(C_T\log N\), the resulting
remainder inequality must hold at every stopped time, on the
continuous branch starting from \(u_i(0)=0\), in the form
\[
 u_i\le K\left[{1+\sqrt{R_i}\over\sqrt N}+u_i^2\right].
 \tag{28}
\]
This statement reuses the checked nonlinear algebra; it is conditional
on the sharper Gaussian event and the full/cavity tubes. It does not
assert an unconditional profile insertion theorem.
Since the largest forcing in (28) is \(N^{-1/4+o(1)}\), continuity
from zero prevents crossing out of its small bootstrap branch for
large \(N\). Consequently that branch
satisfies
\[
 u_i\le {2K(1+\sqrt{R_i})\over\sqrt N},\qquad
 {1\over N}\sum_i u_i^2\le {e^{C\sqrt{\log N}}(\log N)^C\over N}.
 \tag{29}
\]
Thus variation control can repair the exponent lost by the old coarse
control net at the level of state surgery. The Gaussian conditional
events, profile-uniform tube, all-time continuation, and rare-event
integration still must be assembled before (29) is used in an expected
edge-response comparison.

## 6. What trace surgery would and would not prove

There is a useful deterministic trace calculation. Suppose two
linearized coefficients differ by \(A_{\rm small}+A_{\rm rank}\),
with \(\|A_{\rm small}\|_{\rm op}\le N^{-1/2+o(1)}\), and with
\(A_{\rm rank}\) of bounded rank and operator norm \(N^{o(1)}\).
Assume endpoint operator bounds \(N^{o(1)}\) and normalized
Hilbert--Schmidt bounds
\(\|B\|_{\rm HS}/\sqrt N=N^{o(1)}\) for each endpoint factor \(B\).
The trace normalization here is \(N^{-1}\operatorname{tr}\), even
though the ambient parameter dimension is \(O(N^2)\).
Duhamel's formula shows that this normalized endpoint response trace
changes by
\[
 N^{-1/2+o(1)}+N^{-1+o(1)}
 \tag{30}
\]
on a logarithmic horizon: use the endpoint Hilbert--Schmidt factors
on \(A_{\rm small}\), and rank times operator norm on
\(A_{\rm rank}\).
The bound is conditional on this decomposition; arbitrary deletion of
parameter coordinates is not automatically a bounded-rank perturbation.
For example an omitted incoming-row cross-Hessian term can have
unbounded rank, but its operator norm is
\(O(|\delta_i|/\sqrt N)\), so it belongs in \(A_{\rm small}\).

The scalar carrier curvature uses \(\phi''\), whose Lipschitz constant
is controlled by the assumed bound on \(\phi'''\). Thus near-root
coordinate surgery is compatible with this first-response trace
comparison. The full edge response in (6) also contains flow second
variations, including a third output derivative contracted against a
transported query gradient. Their coefficients contain
\(\phi'''(z)\). Merely comparing their values at nearby trained
preactivations does not yield a near-root difference: the assumptions
give continuity, but no quantitative modulus of continuity for
\(\phi'''\).
A Gaussian weak comparison or an exact cancellation may remove that
need. Equation (30) by itself does not remove it and is not a proof of
the contrast (8).

## 7. The signed factorization idea

For square-integrable scalar block functionals whose joint law is
invariant under simultaneous block interchange,
\[
 \mathbb E[A_+B_+-A_+B_-]
 ={1\over2}\mathbb E[(A_+-A_-)(B_+-B_-)].
 \tag{31}
\]
Expanding the right side and using
\(\mathbb E A_-B_-=\mathbb E A_+B_+\),
\(\mathbb E A_-B_+=\mathbb E A_+B_-\), proves it.
The same identity holds for an inner product of matrix-valued
functionals. Two \(L^2\) differences of order \(N^{-1/4+o(1)}\) would
therefore suffice for a contrast of order \(N^{-1/2+o(1)}\).
This can compensate for a square-root loss in Gaussian covariance
coupling, if the required factorization is proved.

There is an exact instance at initialization. With (10), let
\(\Sigma_\pm\) be the first-layer empirical covariance in the two
blocks. Then
\[
 Q_+=(1-s)\Sigma_++s\Sigma_-,\qquad
 Q_-=s\Sigma_++(1-s)\Sigma_-,
\]
and averaging the tagged identity (11) within each block gives
\[
 \mathcal R_{\rm out}-\mathcal R_{\rm in}
 =-{1\over4}\mathbb E\operatorname{tr}
       [(\Sigma_+-\Sigma_-)(A(Q_+)-A(Q_-))].
 \tag{32}
\]
For bounded features,
\(\mathbb E\|\Sigma_+-\Sigma_-\|^2=O(N^{-1})\).
The \(1/2\)-Hölder bound (12) then even gives \(O(N^{-3/4})\) in
(32). For root width alone, the unsymmetrized version of (32) and
boundedness of \(A\) already suffice. This is a positive finite
initialization calculation, not a trained factorization theorem.

The actual trained mobility response exposes the missing object.
Use unweighted coordinates
\(\Theta=(W^{(1)},\sqrt N W^{(2)},\ldots,w)\) here, and let
\(J_c\) be the exact variational propagator of (2) in these coordinates.
For fixed terminal \(t,x\), define
\[
 v_c(u)=J_c(t,u)^\top\nabla_\Theta[Nf_x(t)],\qquad
 \psi_e(u)=\sqrt N\,(v_c(u))_e .
 \tag{33}
\]
For the prediction observable itself, rather than its velocity, exact
mobility differentiation gives
\[
 N^2\mathbb E\,\partial_{c_e}f_x(t)
 =-2\sum_a p_a\int_0^t
        \mathbb E[r_a(u)\psi_e(u)
               \delta_{a,i}^{(\ell)}(u)h_{a,j}^{(\ell-1)}(u)]\,du .
 \tag{34}
\]
Here the initialized raw weights are fixed. Formula (34) follows by
differentiating the \(e\)-coordinate mobility in the field and then
applying the terminal prediction gradient.

At terminal time \(\psi_e(t)=\delta_{x,i}^{(\ell)}h_{x,j}^{(\ell-1)}\)
factorizes into endpoint fields. At earlier times \(\psi_e(u)\) is a
transported query adjoint and depends on the entire trained network.
The covariance part additionally has the second-flow-variation terms.
To apply (31), one must derive a common-cavity representation of their
sum in which the source and target endpoint functionals factor
conditionally, with a near-root remainder. The existing primal
deletion theorem and (29)--(30) do not provide that representation.
In particular, treating \(\psi_e(u)\) as a product of independent
endpoint carriers would discard the learned return responses and
residual feedback. No such factorization is asserted here.

## 8. Frozen proof boundary

The exact autonomous endpoints are (3), and the exact signed
variance-plus-mobility response is (6)--(7). The initialization contrast
has the positive \(C^3\) improvements (14), (32). Equations (17), (21)
are conditional Gaussian probe estimates with proved entropy metrics.
Equations (28)--(30) record their conditional state/trace consequences.
The signed factorization identity (31) is exact, but its use for the
trained mobility-plus-covariance response is the unproved
representation problem made explicit by (33)--(34).

The trained theorem is not proved. Its outstanding steps include:

- Extend the canonical physical/carrier estimates to every block
  profile, with constants uniform at the zero-variance endpoint.
- Complete nonlinear finite-vertex surgery at near-root precision,
  using the sharper probe estimates rather than assuming the old
  \(N^{-b}\) insertion error has improved merely from the operator bound.
- Compare the two *normalized trained edge responses*, including both
  initialization covariance and mobility derivatives. A small
  prediction change under surgery is not this derivative-level estimate.
- Justify the expectation/covariance identity and its terminal-time
  integration, including rare initializations.
- Recover the required linear query envelope.

The shared-residual endpoint comparison with actual autonomous
width-\(n\) training is no longer outstanding: it is supplied by
WIDTH_DOUBLING_BLOCK_ROUTE.md and WIDTH_DOUBLING_BLOCK_CHECK.md.

These are obligations inside the present route, not extra assumptions
on the requested theorem. No cross-width rate is asserted by this
bounded attempt.
