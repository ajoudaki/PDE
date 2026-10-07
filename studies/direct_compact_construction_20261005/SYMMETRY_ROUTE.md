# Orthogonal tanh symmetry: an exact reduction, a perturbative compact model, and the nonclosure boundary

## Status and conclusion

This is a scoped independent theoretical route.  No experiment was run.  The
scientific inputs were the maintained `docs/index.qmd`, `docs/notation.qmd`,
`docs/04-continuing-flows.qmd` (especially B.1), and a limited orientation
passage in `docs/09-trainability.qmd`, together with the assigned
three `closure_sampling_20261003` reports and the assigned READMEs in
`integrated_general_compression_20261004` and
`orthogonal_tanh_time_legendre_20261005`.  No other study was used.
The derivations below are author-checked only; they have not received an
independent internal check or promotion review.

The strongest conclusion is mixed.

1. Orthogonality and odd tanh give an exact signed-permutation equivariance,
   freeze the unused input directions, and reduce the deterministic population
   predictor on the sphere to a function of the \(m\) training correlations.
2. They also give a genuinely direct compact **small-label approximation**:
   an \(m\)-scalar frozen-feature flow, initialized only from bivariate Gaussian
   integrals, approximates the full population gradient flow uniformly for all
   physical times and all sphere queries with error \(O(Y^3)\), where
   \(Y=\lVert y\rVert_2/\sqrt{m}\).  Its endpoint has the same error.
3. This is not the requested fixed-label root-width construction.  For fixed
   nonzero \(Y\), the \(O(Y^3)\) bias does not tend to zero with width.
4. Exact samplewise decoupling is false.  Although the initialized tangent
   Gram is diagonal, the shared readout injects every label into every sample's
   reverse field, and mixed \(y_a y_b\) terms occur in the second physical-time
   derivative of both the middle operator and the first-layer fields.
5. The finite family consisting of residuals, feature Grams, and backward
   Grams is not closed.  Its derivatives require new response-feature moments
   and new actions of the reused Gaussian operator and its adjoint.  Fixed-degree
   polynomial moment truncations are not invariant.  This does not prove that
   every conceivable finite nonlinear encoding is impossible; it identifies
   the exact feedback a successful encoding would still have to generate.

Thus symmetry supplies a complete perturbative theorem and a useful input-orbit
reduction, but not a directly initialized \(O(n^{-1/2})\)-accurate autonomous
model for arbitrary fixed small labels.

## 1. Canonical population flow

Put \(v_a=x_a/\sqrt{d}\), so \(v_a^\top v_b=\delta_{ab}\), and let
\(v\in S^{d-1}\) denote a passive query.  Use the mean squared loss,
\(m^{-1}\sum_a r_a^2\), with \(r_a=f_a-y_a\), and the canonical
mobilities.  Equivalently, in the sum-loss formulation of maintained
Section B.1, take all three block constants equal to \(1/m\).  Write

\[
                         \alpha=\frac{2}{m},\qquad \phi=\tanh .
\]

There are separate probability spaces for the two neuron populations, with
expectations \(\mathbb E_1,\mathbb E_2\).  The state is a first-row field
\(A\in L^2(\Omega_1;\mathbb R^d)\), the canonical Gaussian action plus its
trained Hilbert--Schmidt increment
\(W:L^2(\Omega_1)\to L^2(\Omega_2)\), and the readout
\(w\in L^2(\Omega_2)\).  For training sample \(a\), define

\[
\begin{aligned}
 Z_a^{(1)}&=A\!\cdot v_a,& H_a^{(1)}&=\phi(Z_a^{(1)}),\\
 Z_a^{(2)}&=WH_a^{(1)},& H_a^{(2)}&=\phi(Z_a^{(2)}),\\
 f_a&=\mathbb E_2[wH_a^{(2)}],&
 \Delta_a^{(2)}&=w\phi'(Z_a^{(2)}),\\
 \Delta_a^{(1)}&=\phi'(Z_a^{(1)})W^*\Delta_a^{(2)}.&&
\end{aligned}                                                    \tag{1}
\]

The autonomous population gradient flow is

\[
\begin{aligned}
 \dot A&=-\alpha\sum_a r_a\Delta_a^{(1)}v_a^\top,\\
 \dot W&=-\alpha\sum_a r_a\Delta_a^{(2)}\otimes H_a^{(1)},\\
 \dot w&=-\alpha\sum_a r_aH_a^{(2)}.
\end{aligned}                                                    \tag{2}
\]

Here \((U\otimes V)g=U\mathbb E_1[Vg]\), and \(W^*\) is the actual
adjoint of the same action.  Initially \(A_0\) is a standard Gaussian row,
\(W_0\) is the canonical bounded Gaussian action obtained from the finite
matrices, and \(w_0=0\).  The maintained theorem proves global existence and
uniqueness on every finite horizon, restartability from the full action state,
and the qualitative compact-time finite-width/GD limit.  It does not replace
\(W_0\) by finitely many scalar moments.

For later use, the exact residual equation is

\[
 \dot r=-\alpha\mathcal K r,                                    \tag{3}
\]

where

\[
 \mathcal K_{ab}
 =\mathbb E_2[H_a^{(2)}H_b^{(2)}]
 +\mathbb E_1[H_a^{(1)}H_b^{(1)}]
       \mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}]
 +\delta_{ab}\mathbb E_1[\Delta_a^{(1)}\Delta_b^{(1)}].       \tag{4}
\]

Every term is a Gram block, so \(\mathcal K\succeq0\).  Equation (3)
is finite dimensional only after the changing matrix (4) is supplied; it is
not by itself a closure.

## 2. What the exact symmetries do give

### 2.1 Signed data equivariance

At every parameter state the bias-free two-tanh network is odd:

\[
                              f_\theta(-v)=-f_\theta(v).        \tag{5}
\]

Consequently replacing any collection of data pairs by
\((v_a,y_a)\mapsto(\sigma_av_a,\sigma_ay_a)\),
\(\sigma_a\in\{-1,1\}\), leaves the loss as a function of the parameters
identically unchanged.  A permutation of the pairs does too.  The complete
gradient-flow parameter path is therefore unchanged under a signed permutation
of the data pairs.  Arbitrary label signs may be moved into the orientation of
the orthogonal inputs, but unequal label magnitudes are not removed.  In
particular this equivariance relates different presentations of the task; it
does not impose an exchange symmetry on a fixed task with arbitrary
\((|y_1|,\ldots,|y_m|)\).

For fixed inputs there is one further exact symmetry: under the global label
reversal \(y\mapsto-y\), the solution transforms as
\((A,W,w)\mapsto(A,W,-w)\).  Hence \(f,r,\Delta^{(1)},\Delta^{(2)}\)
change sign while both hidden parameter paths are unchanged.  In a common
label-amplitude expansion, hidden fields are even and predictions are odd;
this is consistent with the cubic leading error in Theorem 1.  It does not
permit independent reversal of labels while the input orientations are held
fixed.

### 2.2 Frozen input complement and arbitrary queries

Let \(P=\sum_av_av_a^\top\).  Equation (2) gives

\[
                         A(t)(I-P)=A_0(I-P).                    \tag{6}
\]

For \(\xi_a=v_a^\top v\) and \(v_\perp=(I-P)v\), every passive query
satisfies the exact identity

\[
 Z^{(1)}(t,v)=A_0\!\cdot v_\perp+\sum_a\xi_aZ_a^{(1)}(t).      \tag{7}
\]

At initialization the first term is independent of the \(m\) training
coordinates and is Gaussian with variance \(\lVert v_\perp\rVert_2^2\).  Thus
orthogonality removes motion in the unused input directions, but the nonlinear
map in (7) still uses the joint law of all moving training coordinates.

There is also an orbit reduction at population level.  Every orthogonal map
fixing all \(v_a\) leaves the dataset and the initialization law invariant.
Uniqueness of the deterministic population action law therefore implies that
\(f(t,v)\) depends on a sphere query only through
\(\xi=(\xi_1,\ldots,\xi_m)\); write it as \(\Psi_t(\xi)\).  Moreover
\(\Psi_t(-\xi)=-\Psi_t(\xi)\).  This is a reduction from the ambient
sphere to the training-span orbit space.  It is an exact law statement for the
population predictor, not a pathwise rotation invariance of one realized
finite network.

## 3. A complete positive theorem: direct all-time cubic-label approximation

The following result is the useful part of the symmetry route.  It deliberately
states its approximation axis: label size, not width.

### Theorem 1 (direct frozen-feature model)

Fix \(m,d\), the orthonormal inputs, and the canonical initial action \(W_0\).
There are constants \(c,C>0\), depending only on these fixed structural data
and on the operator bound for \(W_0\), such that the following holds for every
signed label vector with \(Y=\lVert y\rVert_2/\sqrt{m}\le c\).

Let \(G,G'\) be standard jointly Gaussian with correlation \(s\), and set

\[
 k_1(s)=\mathbb E[\tanh(G)\tanh(G')],
 \qquad \mu=k_1(1).
\]

For \(q\in[-\mu,\mu]\), let \((U,U')\) be centered Gaussian with variances
\(\mu\) and covariance \(q\), and set

\[
 k_2(q)=\mathbb E[\tanh(U)\tanh(U')],
 \qquad \nu=k_2(\mu)>0.                                   \tag{8}
\]

The directly initialized compact model is

\[
 \dot{\bar r}_a=-\frac{2\nu}{m}\bar r_a,qquad
 \bar r_a(0)=-y_a,                                      \tag{9}
\]

with passive prediction

\[
 \bar f(t,v)
 =\frac1\nu\sum_{a=1}^m
   k_2\!\left(k_1(v^\top v_a)\right)(y_a+\bar r_a(t))
 =\frac{1-e^{-2\nu t/m}}{\nu}
   \sum_{a=1}^m k_2\!\left(k_1(v^\top v_a)\right)y_a.    \tag{10}
\]

Then the full population flow (1)--(2) exists for all \(t\ge0\), fits the
training data exponentially, has a sphere-uniform endpoint, and obeys

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
       |f(t,v)-\bar f(t,v)|\le CY^3.                     \tag{11}
\]

In particular,

\[
 \sup_{v\in S^{d-1}}
 \left|f(\infty,v)-
 \frac1\nu\sum_a k_2(k_1(v^\top v_a))y_a\right|
 \le CY^3.                                               \tag{12}
\]

The model (9)--(10) stores \(m\) moving scalars, the data and labels, and
initialization-only Gaussian-integral coefficients.  It uses no realized
width-\(n\) array, trained trajectory, or population-response oracle.  The
first expression in (10) is its current-state observation map, so the
exponential closed form is not a time-indexed playback table.  The functions
\(k_1,k_2\) are evaluated from the displayed scalar-correlation Gaussian
integrals; they are not learned or supplied from the target trajectory.

### Proof

At initialization the \(m\) first preactivations are independent standard
Gaussians.  Oddness gives centered first features with Gram \(\mu I_m\).
The canonical initial Gaussian action therefore gives independent second
preactivations of variance \(\mu\), and their tanh features have Gram
\(\nu I_m\).  Since \(w_0=0\), both backward blocks in (4) vanish, so

\[
                              \mathcal K(0)=\nu I_m.       \tag{13}
\]

The same Gaussian calculation for a passive \(v\) gives its initial
top-feature covariance with sample \(a\) as
\(k_2(k_1(v^\top v_a))\).  Thus (9)--(10) is exactly the gradient flow
obtained by freezing both hidden layers at initialization.  At a training
query \(v_b\), oddness and independence give
\(k_2(k_1(v_b^\top v_a))=\nu\delta_{ab}\), so (10) agrees with (9).

It remains to control the feature-learning correction uniformly in time.
Temporarily stop the full flow when the top-feature Gram falls below
\((\nu/2)I_m\) or when \(\lVert W-W_0\rVert_{\rm op}\) reaches one.  On this
stopped interval, (3)--(4) imply, with \(R=\lVert r\rVert_2\),

\[
 R(t)\le \sqrt{m}\,Y e^{-\nu t/m},
 \qquad \int_0^\infty R(t)\,dt\le C Y.                  \tag{14}
\]

All constants below may depend on fixed \(m\) and \(\nu^{-1}\).  Since
\(|H_a^{(2)}|\le1\), the readout equation and (14) give the pointwise,
hence \(L^2\), bound

\[
                              \sup_t\|w(t)\|\le CY.       \tag{15}
\]

Because \(0<\phi'\le1\), the same stopped operator bound gives

\[
 \sup_{t,a}\|\Delta_a^{(2)}(t)\|\le CY,
 \qquad
 \sup_{t,a}\|\Delta_a^{(1)}(t)\|\le CY.                \tag{16}
\]

Integrating the first two equations in (2), using (14)--(16) and the
rank-one operator norm, yields

\[
 \sup_t\|W(t)-W_0\|_{\rm op}
 +\max_a\sup_t\|Z_a^{(1)}(t)-Z_a^{(1)}(0)\|_{L^2}
 \le CY^2.                                               \tag{17}
\]

Equation (7), the one-Lipschitz property of tanh, and (17) make this
uniform over all sphere queries at the first layer.  Applying \(W(t)\),
then tanh once more, gives

\[
 \sup_{t,v}\|H^{(2)}(t,v)-H^{(2)}(0,v)\|_{L^2}\le CY^2. \tag{18}
\]

Each top-Gram entry consequently moves by at most \(CY^2\), and its
operator norm moves by at most \(CY^2\) because \(m\) is fixed.  Choose
\(c\) so that this is below \(\nu/2\), and also so that the first term
in (17) is below one.  A first-exit argument closes both stopped bounds
for every finite time.  The estimates are time independent, so the flow
continues for all time and (14)--(18) hold globally.

The two backward blocks in (4) are \(O(Y^2)\) by (16), while (18) makes
the top block \(\nu I_m+O(Y^2)\).  Hence

\[
                         \sup_t\|\mathcal K(t)-\nu I_m\|_{\rm op}
                         \le CY^2.                       \tag{19}
\]

Let \(e=r-\bar r\).  Subtracting (9) from (3) gives

\[
 \dot e=-\alpha\nu e-\alpha(\mathcal K-\nu I_m)r,
 \qquad e(0)=0.
\]

Variation of constants, (14), and (19) prove both

\[
                     \sup_t\|e(t)\|_2+\int_0^\infty\|e(t)\|_2dt
                     \le CY^3.                           \tag{20}
\]

Let \(S_a=H_a^{(2)}(0)\) and let
\(\bar w(t)=-\alpha\sum_a\int_0^t\bar r_a(s)S_a\,ds\).  This is the
readout realizing (10).  Subtracting its equation from the last equation
of (2), then using (18), (20), and
\(\int_0^\infty\lVert\bar r\rVert_2dt=O(Y)\), gives

\[
                              \sup_t\|w(t)-\bar w(t)\|_{L^2}\le CY^3.
                                                                  \tag{21}
\]

Finally, \(\sup_t\lVert\bar w(t)\rVert_{L^2}=O(Y)\).  Combine this with
(18) and (21) in

\[
 |\mathbb E_2[wH^{(2)}(t,v)-\bar wH^{(2)}(0,v)]|
 \le\|w-\bar w\|_{L^2}
    +\|\bar w\|_{L^2}\|H^{(2)}(t,v)-H^{(2)}(0,v)\|_{L^2}
\]

to obtain (11).  The velocities of \(w,W,Z_a^{(1)}\) are integrable by
(14)--(16), so these fields converge; (7) and the forward equations give
sphere-uniform feature and prediction convergence.  Passing to the limit
in (11) proves (12).  This also proves the asserted fitting and endpoint
claims.  □

### What Theorem 1 does not provide

For fixed \(Y>0\), the right side of (11) is a nonvanishing population
bias.  It is eventually much larger than \(n^{-1/2}\).  If labels were
allowed to shrink as \(Y_n=O(n^{-1/6})\), the population bias would have
root-width size, but an all-time whole-sphere bridge from the realized
finite network to the population would still be required.  The maintained
B.1 theorem supplies qualitative compact-time convergence, not that bridge.

## 4. Orthogonal samples do not decouple

Orthogonality makes only the raw first-layer kinematics diagonal:

\[
                         \dot Z_a^{(1)}=-\alpha r_a\Delta_a^{(1)}. \tag{22}
\]

The reverse field on the right is shared.  The failure of samplewise
decoupling is already exact at the second derivative at initialization.

For this calculation only, put

\[
 X_a=Z_a^{(1)}(0),\quad H_a=\tanh X_a,\quad
 U_a=W_0H_a,\quad S_a=\tanh U_a,\quad D_a=\operatorname{sech}^2U_a.
\]

The \(U_a\) are independent \(N(0,\mu)\).  Since \(w_0=0\),

\[
 \dot w(0)=\alpha\sum_b y_bS_b,qquad
 \dot\Delta_a^{(2)}(0)=\alpha D_a\sum_b y_bS_b,qquad
 \dot W(0)=0.
\]

Differentiating (2) once more gives the exact mixed-label identities

\[
 \ddot W(0)
 =\alpha^2\sum_{a,b}y_ay_b(D_aS_b)\otimes H_a,            \tag{23}
\]

\[
 \ddot Z_a^{(1)}(0)
 =\alpha^2y_a\operatorname{sech}^2(X_a)
 W_0^*\!\left[D_a\sum_b y_bS_b\right].                   \tag{24}
\]

The coefficient of \(y_ay_b\) in (24) is nonzero for every \(b\ne a\).
Indeed, by adjunction and independence,

\[
 \mathbb E_1\!\left[H_bW_0^*(D_aS_b)\right]
 =\mathbb E_2[U_bD_aS_b]
 =\mathbb E[D_a]\,\mathbb E[U_b\tanh U_b]>0.             \tag{25}
\]

The remaining multiplier \(\operatorname{sech}^2(X_a)\) in (24) is strictly
positive almost surely, so it cannot annihilate this nonzero field.
Thus a sample-\(a\) first-layer coordinate has a genuine mixed response to
label \(b\).  Equation (23) shows the same phenomenon directly in the shared
middle operator.  These are nonzero mixed coefficients as functions of the
arbitrary signed labels, so no identity can decompose the full flow into
\(m\) autonomous one-sample flows.  Special cases with a single nonzero label,
or additional equal-label exchange symmetries, do not establish the claimed
decoupling for the stated label class.

The coupling is also visible in a named training observable.  The middle
kernel block on sample \(a\) has the expansion

\[
 \mathcal K^{(2)}_{aa}(t)
 =\mu\alpha^2t^2\,
   \mathbb E_2\!\left[D_a^2\left(\sum_b y_bS_b\right)^2\right]
   +o(t^2).                                                \tag{25a}
\]

For every \(b\ne a\), the coefficient of \(y_b^2t^2\) in (25a) is
\(\mu\alpha^2\mathbb E[D_a^2]\nu>0\).  Hence even the sample-\(a\)
gradient-kernel block depends on the other label magnitudes immediately after
initialization.  Initial diagonalization is not persistent samplewise
independence.

## 5. Why the natural finite moments do not close

Let
\(C^{(\ell)}_{ab}=\mathbb E_\ell[H_a^{(\ell)}H_b^{(\ell)}]\) and
\(D^{(\ell)}_{ab}=\mathbb E_\ell[\Delta_a^{(\ell)}\Delta_b^{(\ell)}]\).
The residual equation (3) uses only \(C^{(1)},C^{(2)},D^{(1)},D^{(2)}\),
but their evolution does not.  For example,

\[
 \dot C^{(1)}_{ab}
 =-\alpha r_a\mathbb E_1[\phi'(Z_a^{(1)})\Delta_a^{(1)}H_b^{(1)}]
  -\alpha r_b\mathbb E_1[H_a^{(1)}\phi'(Z_b^{(1)})\Delta_b^{(1)}].
                                                                  \tag{26}
\]

The exact second-preactivation equation is

\[
 \dot Z_a^{(2)}
 =-\alpha\sum_c r_c C^{(1)}_{ca}\Delta_c^{(2)}
  -\alpha r_aW[\phi'(Z_a^{(1)})\Delta_a^{(1)}].           \tag{27}
\]

Therefore \(\dot C^{(2)}\) additionally needs moments such as
\(\mathbb E_2[\phi'(Z_a^{(2)})\Delta_c^{(2)}H_b^{(2)}]\) and
\(\mathbb E_2[\phi'(Z_a^{(2)})W(\phi'(Z_a^{(1)})\Delta_a^{(1)})H_b^{(2)}]\).
Differentiating \(D^{(2)}\) introduces

\[
 \dot\Delta_a^{(2)}
 =-\alpha\sum_c r_cH_c^{(2)}\phi'(Z_a^{(2)})
   +w\phi''(Z_a^{(2)})\dot Z_a^{(2)},                   \tag{28}
\]

and differentiating \(D^{(1)}\) introduces both \(W^*\dot\Delta^{(2)}\)
and \(\dot W^*\Delta^{(2)}\).  Equations (26)--(28) are an exact hierarchy,
not a closed ODE for the four Gram matrices.

There is also a simple algebraic obstruction to every fixed polynomial-degree
moment cutoff.  Since \(\phi'(Z)=1-H^2\), for any positive integer \(p\),

\[
 \frac d{dt}\mathbb E_1[(H_a^{(1)})^p]
 =-\alpha p r_a
 \left\{
  \mathbb E_1[(H_a^{(1)})^{p-1}\Delta_a^{(1)}]
 -\mathbb E_1[(H_a^{(1)})^{p+1}\Delta_a^{(1)}]
 \right\}.                                               \tag{29}
\]

The generator raises degree.  Tanh values range over an interval and obey no
finite polynomial identity that could reduce the last moment to lower ones.
Thus the algebra of all mixed moments up to any fixed degree is not invariant
under the vector field.  This falsifies the usual finite-degree moment closure.
It does not rule out an especially designed finite nonpolynomial encoding on
the one reached trajectory.

The action-level obstruction is sharper.  Integrating the middle equation gives

\[
 W(t)=W_0-\alpha\sum_a\int_0^t
          r_a(s)\Delta_a^{(2)}(s)\otimes H_a^{(1)}(s)\,ds. \tag{30}
\]

For an arbitrary passive query,

\[
\begin{aligned}
 Z^{(2)}(t,v)
 ={}&W_0H^{(1)}(t,v)\\
 &-\alpha\sum_a\int_0^t r_a(s)\Delta_a^{(2)}(s)
   \mathbb E_1[H_a^{(1)}(s)H^{(1)}(t,v)]\,ds,             \tag{31}\\
 f(t,v)
 ={}&-\alpha\sum_a\int_0^t r_a(s)
   \mathbb E_2[H_a^{(2)}(s)H^{(2)}(t,v)]\,ds.             \tag{32}
\end{aligned}
\]

Thus even exact passive prediction uses adaptive \(W_0\) actions and two-time,
query-dependent feature correlations.  Gaussian conditioning evaluates a new
action as an old-history regression plus a fresh orthogonal Gaussian innovation.
At the first reverse call this is already visible in (24)--(25); later nonlinear
queries generally enlarge both the history Gram and the innovation covariance.
Initialization orthogonality diagonalizes the first forward Gram only.  It does
not determine these subsequent regression and innovation terms from the
same-time training Grams.

This is the precise missing feedback for a direct compact construction: it must
autonomously generate the forward and adjoint response of \(W_0\) to every new
adaptive field, or prove a uniform truncation theorem for those responses.
Supplying the needed contractions from the realized population trajectory would
be a population-response oracle and would fail the provenance and restartability
contract.

## 6. Endpoint and root-width audit

The exact equivariances in Section 2 persist for all time, but they do not imply
fitting, an endpoint, or endpoint selection.  Loss dissipation gives only
\(d(m^{-1}\lVert r\rVert_2^2)/dt\le0\).  Theorem 1 obtains fitting and an endpoint from
the additional quantitative fact that the labels are small enough to keep the
top Gram within \(O(Y^2)\) of its initialized gap.  It then determines the
endpoint only through cubic order in label size.

For the desired fixed-label comparison, one would need at least one of the
following bridges, neither of which follows from symmetry:

1. an all-time convergent label-response expansion whose directly computable
   truncation error is \(O(n^{-1/2})\) at order growing with \(n\); or
2. a different finite autonomous state that closes the adaptive Gaussian
   forward/adjoint feedback in (30)--(32), together with an all-time
   whole-sphere comparison to the realized dense flow.

The first route needs uniform control of high-order response coefficients and
their tail through the fitted endpoint.  The second needs a finite sufficient
statistic for the growing Gaussian history, not merely diagonal initialized
covariances.  Equations (23)--(29) show why neither bridge is supplied by
orthogonal inputs and odd tanh alone.

Accordingly, the direct \(m\)-scalar model (9)--(10) is a proved compact
all-time approximation in the small-label axis, while a directly initialized
root-width model for arbitrary fixed small signed labels remains open.  Failure
of this symmetry/moment witness is not a no-go theorem for every admissible
compact autonomous model.
