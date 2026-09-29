# Check: removing the top dense backward gate

This is a scoped internal analytic check of the proposed strengthening of
`SHARED_RESIDUAL_GATE_ORACLE.md`, especially its own-residual, own-old-clock
corollary. The allowed scientific inputs were that complete note,
`paper/main.tex`, and `docs/notation.qmd`. The mathematical check used the
`solve-math-rigorously` skill. No other study material, external sources,
experiments, or manuscript changes were used.

**Conclusion.** The complete top dense gate can be removed when the common
initial readout has a bounded essential supremum. This includes zero initial
population readout and gives width-uniform probability bounds for the
canonical finite initialization. For arbitrary initial readout in population
L2, a closely related construction removes the dense top gate from the
learned readout increment, retaining it only on the initial readout. Both
constructions retain the closure's own residual, old clock, responses,
moments, and reconstructed weights, and satisfy the same width-independent
O(P^-1) trajectory estimate for every P >= 1. The lower dense backward gates
remain supplied. There is no assumption of orthogonal or independent data.

The additional check in Section 9 strengthens this conclusion: every learned
backward interaction can use its own gate under the original L2-only readout
hypothesis. Dense gates then occur only on initialized branches. This
supersedes Section 8's limitation for the learned portions of lower branches.

## 1. Exact construction and norms

Let each population Hilbert space be H_l = L2(Omega_l), with probability
measure. Use L >= 2 hidden tanh layers and m arbitrary training pairs
q_a = x_a/sqrt(d), y_a. In this note population responses are denoted
Z, H, and Delta. The initialized hidden operators W_{0,l} are bounded and
are retained exactly; the common W_1(0) is an L2 random Euclidean row.
Assume a regular dense canonical flow exists on [0,T], with L2-continuous
preactivations. Its supplied gates are

\[
 D_{l,a}^D(t)=\operatorname{Mult}(\tanh'(Z_{l,a}^D(t))),
 \qquad 1\le l<L.
\]

Every forward response, prediction, and residual of the closure is computed
from its current physical weights. Write bars for closure quantities:

\[
 \bar f_a=\langle\bar w,\bar H_{L,a}\rangle,
 \quad \bar r_a=\bar f_a-y_a,
 \quad \bar\rho=(m^{-1}\sum_a\bar r_a^2)^{1/2},
 \quad\dot{\bar\tau}=\bar\rho,\quad\bar\tau(0)=1.
\]

The top backward response and all lower backward responses are

\[
 \bar\Delta_{L,a}=\bar w\,\tanh'(\bar Z_{L,a}),\qquad
 \bar\Delta_{l,a}=D_{l,a}^D\bar W_{l+1}^*\bar\Delta_{l+1,a}
 \quad(1\le l<L).                                      \tag{1}
\]

The first-layer and readout equations are

\[
 \dot{\bar W}_1=-\frac2m\sum_a\bar r_a\bar\Delta_{1,a}q_a^T,
 \qquad
 \dot{\bar w}=-\frac2m\sum_a\bar r_a\bar H_{L,a}.        \tag{2}
\]

For each hidden link, use the manuscript's raw moment equations with these
own residuals and responses. The histories are the closure's
\(\bar H_{l-1,a}\) and \(\bar B_{l,a}=\bar r_a\bar\Delta_{l,a}/\bar\rho\)
in its own old clock, with constant initial forward prefix and zero backward
prefix. The reconstructed operator is

\[
 \bar W_l=W_{0,l}-\frac2m\sum_a\int_0^{\bar\tau}
    (\Pi_P\bar B_{l,a})(\xi)\otimes
    (\Pi_P\bar H_{l-1,a})(\xi)\,d\xi.                  \tag{3}
\]

The raw ODE does not divide by rho. At zero residual it has zero velocity.
Use the distance

\[
 d(\bar\theta,\theta_D)=
 \|\bar W_1-W_1^D\|_{L^2(\Omega_1;\mathbb R^d)}
 +\sum_{l=2}^L\|\bar W_l-W_l^D\|_{\rm HS}
 +\|\bar w-w_D\|_{L^2(\Omega_L)}.                      \tag{4}
\]

At common width n the first term is ordinary Frobenius norm divided by
sqrt(n), the last is ordinary Euclidean norm divided by sqrt(n), and hidden
HS norms are ordinary Frobenius norms. The population rank-one operator
U tensor V has finite representative uv^T/n. Initial operators need not
be Hilbert--Schmidt: only their differences, which are learned increments,
are measured in that class.

## 2. A priori readout bounds and constants

Set

\[
 X=\max_a\|q_a\|,\quad
 Y=(m^{-1}\sum_a y_a^2)^{1/2},\quad R_0=\|w_0\|_{L^2},
 \quad B_0=\|w_0\|_{L^\infty}<\infty,
\]
\[
 R=\sqrt{R_0^2+TY^2},\qquad Q=R+Y,\qquad
 S=TQ,\qquad A=1+S,\qquad B=B_0+2S.                  \tag{5}
\]

The readout equation alone, with the closure's own residual, gives

\[
 \frac d{dt}\|\bar w\|_{L^2}^2
 =-\frac4m\sum_a(\bar f_a-y_a)\bar f_a
 =Y^2-\frac4m\sum_a(\bar f_a-y_a/2)^2\le Y^2.
                                                               \tag{6}
\]

Since |tanh| <= 1 and the populations have total measure one, this gives
\(\|\bar w\|_{L^2}\le R\), \(\bar\rho\le Q\), and
\(\int_0^T\bar\rho\,dt\le S\). Equation (2) also gives pointwise,
outside a fixed null set,

\[
 |\bar w(t,\omega)-w_0(\omega)|
 \le\frac2m\sum_a\int_0^t|\bar r_a(s)|\,ds
 \le2\int_0^t\bar\rho(s)\,ds\le2S.                  \tag{7}
\]

Thus \(\|\bar w(t)\|_{L^\infty}\le B\). The same bounds hold for
the dense flow. These bounds use neither loss dissipation of the closure nor
closeness to the dense flow.

Define descending constants by

\[
 \beta_L=R,\qquad
 K_l=\|W_{0,l}\|_{\rm op}+2\sqrt{AS}\,\beta_l,
 \qquad\beta_{l-1}=K_l\beta_l\quad(l=L,\ldots,2).      \tag{8}
\]

They bound both flows' backward responses by beta_l and hidden operator
norms by K_l. Indeed, once beta_l is known, the mean over samples of the
squared backward-history norm is at most S beta_l^2, while each forward
history has squared norm at most A. Projection contraction and
Cauchy--Schwarz in clock and sample variables bound (3)'s increment by
2 sqrt(AS) beta_l. The lower supplied gate is a contraction, so it gives
beta_{l-1}. The dense update gives the smaller bound 2S beta_l. Also
\(\|\bar W_1(t)-W_1(0)\|_{L^2}\le2SX\beta_1\).

## 3. Population existence: the clipping repair is necessary and sufficient

The unrestricted map (w,Z) -> w tanh'(Z) is not locally Lipschitz from
L2 x L2 to L2. For example, on a nonatomic probability space choose sets
E_j of mass epsilon_j -> 0 and compare
\((\epsilon_j^{-1/4}\mathbf1_{E_j},\mathbf1_{E_j})\) with
\((\epsilon_j^{-1/4}\mathbf1_{E_j},0)\). Both tend to (0,0), but the
ratio of the output difference to the input difference is
\(\epsilon_j^{-1/4}|\tanh'(1)-1|\), which diverges. Therefore the
previous oracle's unrestricted Hilbert-space local-Lipschitz argument cannot
be copied without a modification.

For existence only, replace w by its pointwise clipping to [-B,B] in the
top backward response. Keep the actual readout in the prediction and keep
its equation (2) unchanged. The clipping map is 1-Lipschitz on L2 and has
absolute value at most B. Since

\[
 c_2:=\|\tanh''\|_\infty=\frac4{3\sqrt3},
\]

the clipped top response satisfies

\[
 \|\operatorname{clip}_B(w)\tanh'(Z)
   -\operatorname{clip}_B(v)\tanh'(V)\|_{L^2}
 \le\|w-v\|_{L^2}+c_2B\|Z-V\|_{L^2}.                \tag{9}
\]

For fixed P, reconstruction is a finite sum of continuous bilinear rank-one
maps divided by tau >= 1. Forward tanh maps are Lipschitz, lower backward
gates are bounded prescribed operators, and predictions and residuals are
locally Lipschitz scalar functions of the state. Hence the clipped raw ODE
is locally Lipschitz on its Hilbert state space, uniformly in time on bounded
sets with tau bounded away from zero. Its time dependence is strongly
continuous: bounded dense gate values and L2 continuity of dense
preactivations imply strong continuity of their multiplication operators,
first on bounded operands and then by L2 truncation.

The usual contraction argument on the integral equation therefore gives a
unique local solution. Equations (6)--(7) remain valid for this clipped
construction, so clipping never changes its top response. The a priori
bounds (5)--(8), together with the integral representations of all finitely
many raw moments, bound the whole state for fixed P through time T.
The vector field is bounded and Lipschitz on this bounded region. Thus any
finite maximal endpoint has a Hilbert-space state limit by the velocity
bound and admits continuation by the same contraction argument. This proves
existence and uniqueness through T for the original unclipped system.

This argument uses boundedness of the vector field on the visited region,
not compactness of bounded subsets of an infinite-dimensional Hilbert space.
The constant clipping level is selected from the horizon solely for the
proof; the dynamics (1)--(3) have no clipping parameter.

## 4. The accumulated defect remains width uniform

Let G(t,theta) be the canonical physical update using theta's own residual,
its own top backward gate, and the supplied lower gates. The dense flow
solves dot(theta_D) = G(t,theta_D). Differentiating (3) gives exactly

\[
 \dot{\bar\theta}=G(t,\bar\theta)+E,
 \quad E_1=E_w=0,
 \quad E_l=\frac{2\bar\rho}{m}\sum_a
       (\bar B_{l,a}-\bar B_{l,a}^*)\otimes
       (\bar H_{l-1,a}-\bar H_{l-1,a}^*).              \tag{10}
\]

Stars denote endpoint evaluations of the current polynomial projections.
For any recorded history V, its squared projection error D_V obeys

\[
 \dot D_V=\bar\rho\|V-V^*\|_{L^2}^2,\qquad D_V(0)=0.
                                                               \tag{11}
\]

To verify these identities, differentiate the best polynomial error on the
growing interval. Terms involving derivatives of its polynomial minimizer
pair to zero with the projection residual. This leaves the boundary value
in (11); applying the same cancellation to the forward/backward tensor
pairing leaves the product of boundary residuals in (10). Neither identity
differentiates any backward gate. Cauchy--Schwarz gives

\[
 \int_0^t\|E_l(s)\|_{\rm HS}\,ds
 \le\frac2m\sum_a\sqrt{D_{B,l,a}(t)D_{H,l-1,a}(t)}.   \tag{12}
\]

For a Hilbert-valued H1 history the Legendre tail estimate is

\[
 \|V-\Pi_PV\|_{L^2(0,\tau;H)}^2
 \le\frac{\tau^2}{4P(P+1)}\|V'\|_{L^2(0,\tau;H)}^2. \tag{13}
\]

It follows from the shifted Legendre eigenvalues k(k+1): integration by
parts and Bessel's inequality bound the tail by
\([P(P+1)]^{-1}\int_0^\tau\xi(\tau-\xi)\|V'(\xi)\|^2d\xi\).
Applying the scalar argument to an orthonormal expansion and summing gives
the Hilbert-valued statement, and xi(tau-xi) <= tau^2/4 gives (13).

Set
\(Z_l(t)=m^{-1}\sum_a\int_0^{\bar\tau(t)}
\|\partial_\xi\bar H_{l,a}\|_{L^2}^2d\xi\).
Constants controlling these derivatives are

\[
 Z_1^*=4SX^4\beta_1^2,\qquad
 Z_l^*=3\left[4S\beta_l^2+
        (K_l^2+2\beta_l^2A^2)Z_{l-1}^*\right].        \tag{14}
\]

Here are the steps establishing Z_l <= Z_l^*. The first-layer old-clock
velocity has row norm at most 2X beta_1, giving the first bound. The endpoint
evaluation norm for degree below P is P/sqrt(tau), because
sum_{k<P}(2k+1)=P^2. The sample RMS of the backward endpoint error is thus
at most (P+1) beta_l. Squaring (10), then using (11) and (13), gives

\[
 \int_0^t\bar\rho\|E_l/\bar\rho\|_{\rm HS}^2ds
 \le\frac{P+1}{P}\beta_l^2A^2Z_{l-1}(t)
 \le2\beta_l^2A^2Z_{l-1}(t).                         \tag{15}
\]

The actual forward chain rule is

\[
 \partial_\xi\bar H_{l,a}
 =\tanh'(\bar Z_{l,a})\left[
   (G_l/\bar\rho+E_l/\bar\rho)\bar H_{l-1,a}
   +\bar W_l\partial_\xi\bar H_{l-1,a}\right].        \tag{16}
\]

The three terms have integrated squared bounds 4S beta_l^2,
2 beta_l^2 A^2 Z_{l-1}, and K_l^2 Z_{l-1}, respectively. The inequality
\(\|u+v+w\|^2\le3(\|u\|^2+\|v\|^2+\|w\|^2)\)
gives (14). The chain rule here is the Hilbert-valued Sobolev chain rule for
a scalar C1 function with bounded derivative, applied pointwise and
integrated; no Frechet differentiability of the L2 Nemytskii map is needed.

Projection contraction bounds the mean D_B by S beta_l^2. Combining this
with (12)--(14) proves

\[
 \int_0^T\sum_{l=2}^L\|E_l(t)\|_{\rm HS}\,dt
 \le\frac{C}{\sqrt{P(P+1)}},\qquad
 C=A\sum_{l=2}^L\beta_l\sqrt{S Z_{l-1}^*}.            \tag{17}
\]

Nonstationary raw solutions cannot first reach zero residual at a finite
regular time: a state with zero residual is a constant solution even for
the supplied time-dependent gates, and backward local uniqueness rules out
arrival from a different state. Thus the clock changes above apply on each
nonstationary compact interval. Initially zero residual gives the stationary
solution and zero comparison error. This also explains extension to a
possible zero-residual endpoint without any division in the algorithm.

## 5. Restored top feedback and the stronger theorem

For two physical states obeying the established bounds, forward subtraction
controls both preactivation and activation differences by U_l times (4),
where

\[
 U_1=X,\qquad U_l=K_lU_{l-1}+1\quad(l\ge2).           \tag{18}
\]

In particular the same U_L bounds the top *preactivation* difference.
Decompose the top backward difference as

\[
 \bar w\tanh'(\bar Z_{L,a})-w_D\tanh'(Z_{L,a}^D)
 =(\bar w-w_D)\tanh'(\bar Z_{L,a})
   +w_D[\tanh'(\bar Z_{L,a})-\tanh'(Z_{L,a}^D)].      \tag{19}
\]

The changed gate now multiplies the bounded dense readout. Therefore

\[
 V_L=1+c_2B U_L,\qquad
 V_l=K_{l+1}V_{l+1}+\beta_{l+1},\qquad
 \max_a\|\bar\Delta_{l,a}-\Delta_{l,a}^D\|_{L^2}
 \le V_l d(\bar\theta,\theta_D).                     \tag{20}
\]

This is the only required change to the previous oracle's common-gate
feedback estimate. The lower-layer recurrence uses the common supplied
gate and the true adjoint of each operator; it introduces no coordinatewise
bound on hidden adjoint carriers.

Define

\[
 \Lambda=2\left[X V_1+
       \sum_{l=2}^L(V_l+\beta_l U_{l-1})+U_L\right],
 \quad C_f=1+R U_L,
 \quad C_r=2\left[X\beta_1+\sum_{l=2}^L\beta_l+1\right],
 \quad K=Q\Lambda+C_rC_f.                             \tag{21}
\]

The training residual difference in sample RMS is at most C_f d, by
\(\Delta f=\langle\Delta w,H\rangle+
\langle w,\Delta H\rangle\). At fixed residual, subtracting the canonical
update products gives at most Q Lambda d in the sum norm (4). At fixed
responses, changing the residual gives at most C_r times its sample RMS.
Consequently \(\|G(t,\theta)-G(t,\widetilde\theta)\|_{\rm sum}
\le Kd(\theta,\widetilde\theta)\).

Subtracting the dense integral equation from (10), using (17), and iterating
the scalar integral inequality gives, for every P >= 1,

\[
 \sup_{0\le t\le T}d(\bar\theta_P(t),\theta_D(t))
 \le\frac{C e^{KT}}{\sqrt{P(P+1)}}.                   \tag{22}
\]

All constants are displayed and depend only on T, X, Y, R_0, B_0, depth,
and initialized hidden operator norms. They are independent of width and P.
No Gram-matrix hypothesis appears. The conclusion holds on arbitrary
probability spaces and at every finite width with the explicit normalization
(4). Test predictions satisfy the previous oracle bound
\(|\bar f_P(t,x)-f_D(t,x)|\le[1+R U_L(\|x\|/\sqrt d)]d\);
therefore (22) also gives the same rate on bounded test sets and in test
L2 for finite second input moment.

The theorem strictly reduces the required oracle input for bounded initial
readout: the entire dense top gate D_{L,a}^D is absent. The closure already
uses its own residual and old clock, so these are not reintroduced as inputs.
This is still a lower-gate-driven closure, not the fully autonomous closure.

## 6. Same L2-only assumptions: release the learned readout increment

If only R_0 < infinity is assumed, retain the top dense gate on w_0 alone:

\[
 \bar\Delta_{L,a}
 =w_0\tanh'(Z_{L,a}^D)
  +(\bar w-w_0)\tanh'(\bar Z_{L,a}).                 \tag{23}
\]

All other definitions remain unchanged. This equals the dense top response
at the dense state. Equations (6)--(7) still apply, because (2) is unchanged.
Set \(J=2S\). In place of (8) and (20), use

\[
 \beta_L=R_0+J,\qquad V_L=1+c_2J U_L,                \tag{24}
\]

and then the same descending recurrences and constants. For (24), the common
term \(w_0\tanh'(Z_L^D)\) cancels; the changed gate multiplies
\(w_D-w_0\), whose essential supremum is at most J by (7).
The triangle inequality bounds (23) by R_0+J in L2. Thus the same defect
estimate and (22) hold, with constants depending on T, X, Y, R_0 and initial
operator norms, and with no initial L-infinity assumption.

For population existence, clip only \(\bar w-w_0\) to [-J,J] in the
second term of (23). The first term is a prescribed continuous L2 field:
bounded gates times the fixed L2 variable w_0 are continuous by truncation.
The clipped second term satisfies (9) with B replaced by J. Bounds (6)--(7)
show that clipping never acts. This proves existence and continuation by the
same argument as above.

This variant weakens the top oracle dependence under exactly the old
L2-readout hypothesis, but for general w_0 it does **not** remove the top
dense input completely. If w_0=0 it coincides with the fully restored top
gate (1). A claim of complete top-gate removal for arbitrary L2 initial
readout does not follow from this proof.

## 7. Canonical small Gaussian readout

Under the notation contract the finite stored readout is w_{0,i}=G_i/n,
with standard Gaussian G_i. For any epsilon in (0,1), a Gaussian tail and
the union bound give

\[
 \Pr\!\left(\max_{i\le n}|w_{0,i}|>
       \frac{\sqrt{2\log(2n/\varepsilon)}}n\right)
 \le\varepsilon.                                    \tag{25}
\]

The displayed threshold is no greater than
\(\sqrt{2\log(2/\varepsilon)}\) for every n >= 1; the squared expression
\(2\log(2n/\varepsilon)/n^2\) decreases for n >= 1. Thus the bounded
initial-readout theorem has a width-uniform deterministic B_0 on events of
probability at least 1-epsilon at each width. These events may be intersected
with the required initialized spectral-norm bounds. This is not a bound on
every Gaussian realization, nor an almost-sure claim simultaneous over every
width. At population initialization w_0=0 the full top-gate theorem applies
directly with B_0=R_0=0.

## 8. Check outcome and remaining limitation

The proposed stronger theorem is valid with the explicit bounded-initial-
readout hypothesis, and with no further data or depth restriction. The
readout energy identity, Hilbert-space clipping construction, accumulated
old-clock defect bound, top-gate feedback estimate, and lower supplied-gate
recursion are compatible. Gate derivatives are never used in the temporal
compression estimate; tanh'' enters only the current-state Lipschitz bound.

The remaining oracle input consists of dense gates at layers 1 through L-1.
There the changed-gate carrier would be
\((W_{l+1}^D)^*\Delta_{l+1}^D\), and its L2 bound alone still does not
control multiplication on L2. The present check establishes no removal of
those lower gates and no fixed-P finite-width-to-population limit theorem.
It is an internal proof check, not an independent promotion review.

## 9. Further check: self-gates on every learned backward interaction

The supervisor supplied the following additional concrete construction after
the preceding check. This section verifies it within the same source scope.
It requires only w_0 in L2, with no initial L-infinity bound.

Write \(\bar A_l=\bar W_l-W_{0,l}\),
\(A_l^D=W_l^D-W_{0,l}\), and let \(\bar D_{l,a}\) denote multiplication
by \(\tanh'(\bar Z_{l,a})\). Supply dense gates at every layer but use
them only on the initialized branches:

\[
 \bar\Delta_{L,a}
 =D_{L,a}^D w_0+\bar D_{L,a}(\bar w-w_0),             \tag{26}
\]
\[
 \bar\Delta_{l,a}
 =D_{l,a}^D W_{0,l+1}^*\bar\Delta_{l+1,a}
   +\bar D_{l,a}\bar A_{l+1}^*\bar\Delta_{l+1,a},
 \qquad 1\le l<L.                                    \tag{27}
\]

Retain the closure's own forward network, residual, old clock, outer-weight
updates, raw histories, and reconstruction (3). At the dense state, (26)
and (27) reduce to exact dense backpropagation, since its self-gate is its
supplied gate. The system thus admits the same dense reference solution in
physical parameter space.

### 9.1 Bounds and accumulated compression defect

Keep the constants R, Q, S, A in (5), which do not require B_0, and put

\[
 J_w=2S,\qquad\beta_L=R_0+J_w,
\]
\[
 J_l=2\sqrt{AS}\,\beta_l,\qquad
 K_l=\|W_{0,l}\|_{\rm op}+J_l,\qquad
 \beta_{l-1}=K_l\beta_l\quad(l=L,\ldots,2).           \tag{28}
\]

The readout identity (6) and the pointwise increment bound (7) still hold.
The top response has L2 norm at most R_0+J_w. Once beta_l is available,
projection contraction bounds \(\|\bar A_l\|_{\rm HS}\le J_l\).
Each gate is a contraction, so (27) bounds the preceding response by
\((\|W_{0,l}\|_{\rm op}+J_l)\beta_l\). The dense trajectory obeys
the same bounds; its increment has norm at most 2S beta_l <= J_l.
This proves (28) by downward induction without assuming trajectory proximity.

Equations (10)--(17) use only the raw moment identities, contraction of
forward tanh, and these L2 response/operator bounds. Their derivation is
unchanged with (26)--(28). In particular, with Z_l^* and C recalculated
using (28),

\[
 \int_0^T\sum_{l=2}^L\|E_l(t)\|_{\rm HS}\,dt
 \le\frac C{\sqrt{P(P+1)}}.                           \tag{29}
\]

No derivative of any supplied or self-computed backward gate is needed for
this estimate.

### 9.2 The dense learned adjoint carrier is bounded pointwise

For fixed current time t and sample a, exact dense integration gives

\[
 (A_{l+1}^D(t))^*\Delta_{l+1,a}^D(t)
 =-\frac2m\sum_b\int_0^t r_b^D(s)H_{l,b}^D(s)
   \langle\Delta_{l+1,b}^D(s),\Delta_{l+1,a}^D(t)\rangle
 \,ds.                                               \tag{30}
\]

The inner product contracts only population l+1; H lives on population l.
The response norms in that inner product are at most beta_{l+1}, while
the pointwise absolute value of H is at most one. Therefore

\[
 \|(A_{l+1}^D(t))^*\Delta_{l+1,a}^D(t)\|_{L^\infty(\Omega_l)}
 \le2\beta_{l+1}^2\int_0^t\rho_D(s)\,ds
 \le2S\beta_{l+1}^2.                                 \tag{31}
\]

This is a bound on the dense learned carrier, not on the full initialized
plus learned adjoint carrier. It uses no independence between populations,
training samples, histories, or the two backward fields in the inner product.
The dense learned operator's exact gradient-history representation is what
supplies its pointwise regularity.

### 9.3 One-reference stability

Let a difference symbol mean closure minus dense. Subtracting (27) gives
the exact decomposition

\[
 \bar\Delta_{l,a}-\Delta_{l,a}^D
 =\left(D_{l,a}^D W_{0,l+1}^*
          +\bar D_{l,a}\bar A_{l+1}^*\right)
       (\bar\Delta_{l+1,a}-\Delta_{l+1,a}^D)
\]
\[
 \hspace{7mm}
  +\bar D_{l,a}(\bar A_{l+1}-A_{l+1}^D)^*
            \Delta_{l+1,a}^D
  +(\bar D_{l,a}-D_{l,a}^D)(A_{l+1}^D)^*
            \Delta_{l+1,a}^D.                        \tag{32}
\]

The first operator has norm at most K_{l+1}; the second term has norm at
most beta_{l+1} times the parameter distance d. By (18) and (31), the third
has norm at most \(2c_2S\beta_{l+1}^2 U_l d\). At the top, subtracting
(26) cancels the common initialized term, and the changed self-gate
multiplies the dense increment w_D-w_0, bounded pointwise by 2S.
Consequently the backward error is at most V_l d with

\[
 V_L=1+2c_2S U_L,
\]
\[
 V_l=K_{l+1}V_{l+1}+\beta_{l+1}
           +2c_2S\beta_{l+1}^2 U_l\quad(l<L).        \tag{33}
\]

The supervisor's simpler coefficients
\(V_L=1+4SU_L\) and
\(V_l=K_{l+1}V_{l+1}+\beta_{l+1}+4S\beta_{l+1}^2U_l\)
are valid because c_2 <= 2. No extra m factor is needed: the mean absolute
dense residual is at most its sample RMS.

Use (21), now with (28) and (33), to define Lambda, C_f, C_r, and K.
The product subtraction in Section 5 then gives

\[
 \|G(t,\bar\theta)-G(t,\theta_D)\|_{\rm sum}
 \le Kd(\bar\theta,\theta_D).                         \tag{34}
\]

This is a comparison to the one dense reference. It is not an assertion
of local Lipschitz continuity of the physical vector field on unrestricted
Hilbert--Schmidt parameter balls: the proof of (31) uses the dense trajectory's
exact history. Estimate (34) is precisely what the error integral inequality
requires. Together with (29), it proves

\[
 \sup_{t\le T}d(\bar\theta_P(t),\theta_D(t))
 \le\frac{C e^{KT}}{\sqrt{P(P+1)}}                   \tag{35}
\]

provided population existence of the moment system is justified. The next
paragraph supplies that justification independently of this comparison.

### 9.4 Locally Lipschitz moment construction and inactive clipping

Let F_{l,a,k} denote the raw forward moment on population l, and
B_{l+1,a,k} the raw backward moment on population l+1. In the backward
calculation alone, replace the learned adjoint action by

\[
 \bar A_{l+1,\mathrm{clip}}^*V
 =-\frac2{m\bar\tau}\sum_{a,k<P}(2k+1)
   \operatorname{clip}_{M_k}(F_{l,a,k})
   \langle B_{l+1,a,k},V\rangle,
 \qquad M_k=\frac A{\sqrt{2k+1}}+1.                  \tag{36}
\]

Use this action in the second term of (27), retaining the original unmodified
reconstructed operator in the forward network. Clip only w-w_0 to
[-J_w,J_w] in the second term of (26), as in Section 6.

For each k the product map
\((F,Z)\mapsto\operatorname{clip}_{M_k}(F)\tanh'(Z)\)
is Lipschitz from L2 x L2 to L2, with respective constants 1 and c_2 M_k.
The coefficients \(\langle B,V\rangle\) are continuous bilinear scalar
maps and hence Lipschitz on bounded sets. Starting at the clipped top
response, (36) and the bounded initialized adjoint therefore give locally
Lipschitz backward responses by downward induction. For fixed P, the
entire clipped raw moment ODE is locally Lipschitz on its Hilbert state
space, with time dependence continuous as in Section 3. It has a unique
local solution by the integral-equation contraction argument.

There is no circularity in proving clipping inactive. On every local
existence interval, (6) holds because neither the actual prediction nor its
readout update was clipped. Thus rho <= Q, tau <= A and |w-w_0| <= J_w
already hold, independently of any backward estimates. Also every actual
forward activation has absolute value at most one. The raw forward moment
equation has its history-integral representation even for the clipped
backward construction. Consequently, almost everywhere in its population,

\[
 |F_{l,a,k}(t)|
 =\left|\int_0^{\bar\tau(t)}
       H_{l,a}(\xi)p_k(\xi/\bar\tau(t))\,d\xi\right|
 \le \sqrt{\bar\tau(t)}
       \left(\int_0^{\bar\tau(t)}
           |p_k(\xi/\bar\tau(t))|^2d\xi\right)^{1/2}
 =\frac{\bar\tau(t)}{\sqrt{2k+1}}<M_k.               \tag{37}
\]

The prefix also satisfies |H| <= 1. Thus every forward-moment clipping in
(36) is inactive on the local solution. The readout-increment clipping is
inactive by (7). The local solution is therefore an exact solution of
(26)--(27) with the original reconstruction.

Bounds (28), the first-layer bound, the readout bounds, and the raw integral
representations now bound all moment coordinates for each fixed P. On a
bounded Hilbert-state region with tau bounded away from zero, the clipped
vector field has a uniform velocity bound and a uniform Lipschitz constant.
As in Section 3, these bounds give a state limit at any finite maximal
endpoint and permit continuation. Hence the unclipped intended system
exists uniquely through T for every P >= 1. Any local solution of the
unclipped system satisfies (6)--(7) and (37), so it also solves the clipped
system; uniqueness is therefore uniqueness for the intended system.

### 9.5 Check outcome

The extension is sound. It proves (35) under the previous oracle's L2-only
initial-readout hypothesis and bounded initialized operator norms, for
arbitrary fixed depth and arbitrary finite correlated data. All learned
backward branches now use their own current gates. Dense gates remain only
on the initialized readout and initialized hidden adjoints. For w_0=0 the
entire dense top-gate input disappears. The test-prediction conclusions of
Section 5 hold with the new constants.

The proof does not justify replacing the remaining initialized-branch gates:
bounded initialized operators need not map the relevant L2 backward response
to L-infinity. Nor does it prove a fixed-P finite-width-to-population limit.
The important technical qualifications are the one-reference nature of (34)
and use of the clipped moment construction for existence, rather than an
unsupported local-Lipschitz claim in physical parameter coordinates.
