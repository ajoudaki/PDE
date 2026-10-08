# Small-label learning profiles beyond initialization

2026-10-07. Analytical predictions for the existing two-hidden-layer
nonlinear candidate. No experiments, code, new global proof, or changes
to shared notes were performed.

The main approximation is the nonlinear internal clock in Section 4:
its coefficients are initial Gaussian expectations, and feature-enhanced
fitting changes where the common learning orbit stops. The exponential
clock derived first is its small-label baseline, not the final proposed
finite-time approximation.

## 1. Scope and the expansion convention

Use two tanh hidden layers, training inputs
\[
v_1=e_1,\qquad v_2=e_2,
\]
and the passive input \(v_3=(2e_1+e_2)/\sqrt5\). There is no label \(y_3\).
The physical factor \(2/m\) equals one.
Write \(y_b=Y\ell_b\), where the fixed label direction \(\ell\) is bounded
and \(Y\) is small. Equal/opposite labels correspond to \((\ell_1,\ell_2)
=(1,1)\) and \((1,-1)\).

The calculation expands in label magnitude, not in time. Its coefficient
functions below retain the full exponential time dependence and apply at
fixed non-infinitesimal times, including \(t\) of order the initial
relaxation time. They are not merely initial accelerations.

A precise conservative interpretation is: expand the smooth finite-width
ODE at \(Y=0\) on a fixed finite time interval, then take the width limit of
the displayed coefficients. Those coefficients involve only the initial
Gaussian fields and finitely many forward/transpose returns. The initial
top training Gram converges to the scalar matrix used below. No uniform
in-width Taylor remainder, interchange with \(t=\infty\), or moderate-label
error certificate is proved here. Remainder notation records the regular
small-label expansion; it is not a new uniform dense-width theorem.

The exact symmetry \(y\mapsto-y,\ w\mapsto-w\), with hidden parameters
unchanged, makes hidden fields/Grams even in \(Y\) and predictions/readout
odd. Thus the first omitted representation term is fourth order, whereas
the first correction to a leading prediction is third order.

Inputs: the complete CANDIDATE_SYSTEM.md at SHA-256
a5fa62c596b5816859589be7af686829a5f4f65ddb8406138e15cf4468a45c31
and TWO_LAYER_MECHANISM_CHECK.md at
022b11454c281ac647e68f214a23f205de5029989ce88310702e320203b8623d,
together with the current route's existing derivations.

## 2. Initial Gaussian constants and the three clocks

Put
\[
T(x)=\tanh x,\qquad g(x)=\operatorname{sech}^2x.
\]
In the lower population let \(X_1,X_2\) be independent standard Gaussians,
\(X_3=(2X_1+X_2)/\sqrt5\), and \(H_a=T(X_a)\). Define
\[
\sigma^2=\mathbb E[T(X)^2],\qquad q_X=\mathbb E[g(X)^2],
\quad X\sim N(0,1).
\]
The upper initial Gaussian panel \(Z\) has covariance
\(\mathbb E[Z_aZ_b]=\mathbb E[H_aH_b]\).
In particular \(Z_1,Z_2\) are independent \(N(0,\sigma^2)\).
One must not replace \(Z_3\) by \((2Z_1+Z_2)/\sqrt5\).

For \(Z\sim N(0,\sigma^2)\), set
\[
\alpha=\mathbb E[g(Z)],\qquad
\beta=\mathbb E[g(Z)^2],\qquad
\nu=\mathbb E[T(Z)^2]=1-\alpha>0.
\]
The initial top training feature Gram is \(\nu I_2\).
The leading training residual therefore decays with
\[
r(t)=e^{-\nu t}.
\]
Define the integrated readout and representation clocks
\[
a(t)=\int_0^t r(s)\,ds=\frac{1-e^{-\nu t}}{\nu},\qquad
b(t)=\int_0^t r(s)a(s)\,ds=\frac{a(t)^2}{2}.
\tag{1}
\]
The factor \(1/2\) is important.

Let
\[
Q_y=y_1T(Z_1)+y_2T(Z_2).
\]
The leading readout and residual are
\[
w(t)=a(t)Q_y+O(Y^3),\qquad
c_b(t)=r(t)y_b+O(Y^3).
\tag{2}
\]
Every leading hidden update multiplies \(c\), of order \(Y\), by a
backward signal proportional to \(w\), also of order \(Y\).
Its time coefficient is therefore \(r(t)a(t)\), not \(r(t)\).
Integration gives \(b(t)\).

If \(J_{\ell,a}\) denotes the already checked initial feature acceleration
with the actual labels \(y\), then
\[
h_{\ell,a}(t)=h_{\ell,a}(0)+b(t)J_{\ell,a}+O(Y^4).
\tag{3}
\]
Here \(J_{\ell,a}=O(Y^2)\). Formula (3) extends the same initial mechanism
along the entire leading residual/readout trajectory.

## 3. Finite-time training feature profiles

Define the positive constants
\[
\begin{aligned}
\kappa_1&=\sigma^2q_X\alpha^2,\\
\kappa_W&=\sigma^2\nu\beta,\\
\kappa_{\rm forward}&=q_X\nu\beta,\\
\kappa_{\rm alignment}&=\sigma^2q_X\alpha^4,\\
\kappa_2&=\kappa_W+\kappa_{\rm forward}+\kappa_{\rm alignment}.
\end{aligned}
\tag{4}
\]
The two cross-feature similarities satisfy
\[
C^1_{12}(t)=y_1y_2\kappa_1 a(t)^2+O(Y^4),\qquad
C^2_{12}(t)=y_1y_2\kappa_2 a(t)^2+O(Y^4).
\tag{5}
\]
They begin at zero. Their second time derivatives at zero are
\(2y_1y_2\kappa_1\) and \(2y_1y_2\kappa_2\), matching the checked initial
calculation. The small-label prediction at finite time is the stronger
shape statement
\[
\frac{\nu^2 C^\ell_{12}(t)}{y_1y_2\kappa_\ell}
\simeq (1-e^{-\nu t})^2,\qquad \ell=1,2.
\tag{6}
\]
Equal labels give positive alignment; opposite labels reverse its sign.
The leading magnitude is the same. The clocks flatten after a few initial
relaxation times, unlike an indefinitely extrapolated \(t^2\) law.

The formal leading plateaus are \(y_1y_2\kappa_\ell/\nu^2\).
These are useful small-label test targets, not a proved uniform
small-label expansion at infinite time.

The three pieces of \(\kappa_2\) have distinct origins:

- \(\kappa_W\): learning the middle matrix itself.
- \(\kappa_{\rm forward}\): the correlated forward/transpose return of
  first-layer feature motion through the initialized interface.
- \(\kappa_{\rm alignment}\): the reciprocal alignment already visible
  in \(C^1_{12}\), transmitted to the upper nonlinear features.

Keeping only the learned-middle-matrix term misses both latter effects.

## 4. A better finite-time approximation: learn the orbit, not a fitted clock

For equal-magnitude labels write \(y=Y(1,s)\), \(s=\pm1\), with \(Y>0\).
The isotropic population law and the odd tanh activation imply
\[
f_2(t)=s f_1(t),\qquad c(t)=(r_Y(t),s r_Y(t)),
\quad r_Y(t)=Y-f_1(t).
\]
Swapping the two training inputs swaps their labels; for \(s=-1\), a
simultaneous global label sign change reverses outputs and the readout
while preserving hidden parameters. The initialization law is invariant
under that operation, giving the displayed output identity.

Consequently define the internal coordinate
\[
u(t)=\int_0^t r_Y(t')\,dt'.
\]
In the compatible population gradient realization, wherever this
reparameterization is used,
\[
\frac{d\theta}{du}=\nabla(f_1+s f_2),\qquad
\frac{du}{dt}=Y-F(u),\qquad F(u)=f_1(\theta(u)).
\tag{26}
\]
The gradient in (26) uses the inherited physical block/Hilbert metric,
not the unweighted Euclidean metric on raw finite-width parameters:
its finite-width squared norm is
\(\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n\).
Thus changing \(Y\) changes the speed and stopping point on the same
feature-learning orbit; it does not change that orbit's vector field.
Changing \(s\) mirrors the second input. The initialization law is also
invariant under that reflection, so the training orbit function \(F\)
is the same for the two signs, while cross Grams reverse sign.

This is an exact population symmetry reduction conditional on the
compatible continuous gradient realization. It is not an exact
one-dimensional reduction of a generic finite-width realization, whose
random initial features need not have that symmetry. Nor does (26)
alone provide a closed scalar equation: the orbit function must still
be specified.

### Its first nonlinear coefficient is explicit and positive

The internal orbit has
\[
F(u)=\nu u+\kappa u^3+O(u^5),
\]
with
\[
\begin{aligned}
\kappa=\frac23\Big\{&
(\sigma^2+q_X)
\big[\mathbb E[T(Z)^2g(Z)^2]+\nu\beta\big]\\
&+(3\beta-2\alpha)^2\mathbb E[T(X)^2g(X)^2]
+\alpha^4q_X\sigma^2\Big\}>0 .
\end{aligned}
\tag{27}
\]
Here \(X\sim N(0,1)\) and \(Z\sim N(0,\sigma^2)\).
There are no fitted trajectory coefficients.

The factor can be checked directly. Set
\(Q=T(Z_1)+sT(Z_2)\) and let \(J_{2,1}\) be the initial second
internal-time derivative of the first training sample's upper feature.
Along the orbit
\[
w(u)=uQ+\frac{u^3}{6}(J_{2,1}+sJ_{2,2})+O(u^5),\quad
h_{2,1}(u)=T(Z_1)+\frac{u^2}{2}J_{2,1}+O(u^4).
\]
The training symmetries identify the two cubic contractions, hence
\[
F'''(0)=4\mathbb E[QJ_{2,1}],\qquad
\kappa=\frac23\mathbb E[QJ_{2,1}].
\]
The learned-middle part of that expectation is
\(\sigma^2[\mathbb E(T^2g^2)+\nu\beta]\).
For the lower-layer part, adjointness turns it into
\(\mathbb E[g(X_1)^2B_1^2]\), where
\[
B_1=\zeta+(3\beta-2\alpha)H_1+s\alpha^2H_2,\qquad
\mathbb E\zeta^2=\mathbb E[T(Z)^2g(Z)^2]+\nu\beta,
\]
and \(\zeta\) is independent of the lower initial fields.
Expanding the square gives exactly the remaining terms in (27).

Every contribution is nonnegative, and their sum is positive. Feature
learning therefore increases the response of the trained output mode
at this order, rather than merely moving a similarity entry:
\[
\frac{dF}{du}=\nu+3\kappa u^2+O(u^4).
\tag{28}
\]

### The closed cubic-clock approximation

The proposed finite-time approximation is
\[
\dot u=Y-\nu u-\kappa u^3,\qquad u(0)=0,
\]
\[
f_1\simeq\nu u+\kappa u^3,\qquad f_2\simeq s f_1,\qquad
C^1_{12}\simeq s\kappa_1u^2,\qquad
C^2_{12}\simeq s\kappa_2u^2.
\tag{29}
\]
It is a one-scalar approximation to the full history-state system,
not a replacement theorem for that system. Its coefficients come
entirely from initialization.

The cubic right-hand side has a unique positive root \(u_*\), determined
by \(Y=\nu u_*+\kappa u_*^3\). Since \(\kappa>0\),
\(u_*<Y/\nu\). Thus the model predicts smaller feature changes than
the frozen exponential clock, while keeping
\[
C^2_{12}/C^1_{12}\simeq\kappa_2/\kappa_1.
\]
This separates two effects: the orbit's representation geometry and
the faster removal of the deficit along that orbit.

The cubic clock agrees with the finite-time label expansion already
derived. In fact
\[
u(t)=Ya(t)-\frac{\kappa Y^3}{\nu}
[a(t)^3-\Lambda(t)]+O(Y^5),
\tag{30}
\]
where \(\Lambda\) is given in (11) below.
Therefore it resums a specific feature-dependent fitting correction;
it does not introduce an unrelated empirical clock.

At moderate labels, (29) is a testable approximation, not a certified
truncation. Its predicted stopping point need not lie in the region
where the omitted orbit terms are small.

## 5. Passive prediction: leading curve and the cubic correction

Let
\[
k_b=\mathbb E[T(Z_3)T(Z_b)],\qquad b=1,2.
\]
The initial covariance ordering gives \(k_1>k_2>0\). At leading order
\[
f_3(t)=a(t)(k_1y_1+k_2y_2)+O(Y^3).
\tag{7}
\]
Thus equal labels \(y_1=y_2=Y>0\) give
\(Y(k_1+k_2)a(t)\); opposite labels \(y_1=Y,y_2=-Y\) give
\(Y(k_1-k_2)a(t)>0\).
Their leading ratio is independent of time.

The first feature-learning correction to this output is cubic, not
quadratic. It can be calculated without unspecified new response kernels.
Define the quadratic initial coefficient matrix
\[
M_{ab}=\mathbb E[J_{2,a}T(Z_b)],\qquad a,b\le3.
\tag{8}
\]
This matrix is not assumed symmetric, especially for active/passive
indices. The two-time top Gram has expansion
\[
C^2_{ab}(t,s)
=C^2_{ab}(0,0)+b(t)M_{ab}+b(s)M_{ba}+O(Y^4).
\tag{9}
\]
Put
\[
P_a=\frac12\sum_{b=1}^{2}M_{ab}y_b
+\frac16\sum_{b=1}^{2}M_{ba}y_b.
\tag{10}
\]
Each \(P_a\) is cubic in the labels. The unequal \(1/2\) and \(1/6\)
weights distinguish today's moving query from the earlier feature
written into the readout.

Define one transient clock
\[
\begin{aligned}
\Lambda(t)
&=3r(t)\int_0^t a(s)^2\,ds\\
&=\frac{3e^{-\nu t}}{\nu^3}
\left[\nu t-\frac32+2e^{-\nu t}
-\frac12e^{-2\nu t}\right].
\end{aligned}
\tag{11}
\]
It starts as \(t^3\) and decays to zero, whereas \(a(t)^3\) saturates.
The training outputs through cubic order are
\[
f_b(t)=(1-r(t))y_b+\Lambda(t)P_b+O(Y^5),\quad b=1,2.
\tag{12}
\]
The passive prediction is
\[
\begin{aligned}
f_3(t)
={}&a(t)(k_1y_1+k_2y_2)\\
&+a(t)^3\left[P_3-\frac{k_1P_1+k_2P_2}{\nu}\right]
+\frac{\Lambda(t)}{\nu}(k_1P_1+k_2P_2)
+O(Y^5).
\end{aligned}
\tag{13}
\]
Consequently a cubic passive deviation has both a saturating feature
contribution and a transient correction from the changing training
residual. Omitting residual feedback would incorrectly retain only
\(a^3P_3\).

To check the factors, the exact readout identity is
\[
f_a(t)=\sum_{b=1}^2\int_0^t c_b(s)C^2_{ab}(t,s)\,ds.
\]
Using (9),
\(\int_0^t r(s)b(s)\,ds=a(t)^3/6\) and
\(a(t)b(t)=a(t)^3/2\).
The training cubic term \(F_b\) therefore obeys
\(F_b+\nu\int_0^tF_b=a^3P_b\), whose solution is (12).
Substitution gives (13). This is coefficient bookkeeping, not a new
global approximation argument.

### Explicit Gaussian evaluation of \(M\)

The matrix in (8) is a finite initial Gaussian calculation.
For training \(j\), define
\[
d_j(Z)=g(Z_j)Q_y,\qquad
R_{jc}=\mathbb E[\partial_{Z_c}d_j(Z)].
\]
It has only training columns, and
\[
(R_{jc})_{j,c\le2}
=\begin{pmatrix}
y_1(3\beta-2\alpha)&y_2\alpha^2\\
y_1\alpha^2&y_2(3\beta-2\alpha)
\end{pmatrix}.
\]
For any panel indices \(a,b\), put
\[
\psi_{ab}(Z)=g(Z_a)T(Z_b),\qquad
U_{ab,d}=\mathbb E[\partial_{Z_d}\psi_{ab}(Z)].
\]
Explicitly,
\[
U_{ab,d}
=\mathbf1_{\{d=a\}}\mathbb E[T''(Z_a)T(Z_b)]
+\mathbf1_{\{d=b\}}\mathbb E[g(Z_a)g(Z_b)].
\]
Then \(M=M^W+M^A\), where
\[
M^W_{ab}
=\sum_{j=1}^2 y_j\,\mathbb E[H_aH_j]\,
\mathbb E[\psi_{ab}(Z)d_j(Z)],
\tag{14}
\]
and
\[
\begin{aligned}
M^A_{ab}
=\sum_{j=1}^2 y_j S_{aj}\Big\{&
\mathbb E[g(X_a)g(X_j)]
\mathbb E[\psi_{ab}(Z)d_j(Z)]\\
&+\sum_{c,d=1}^3R_{jc}U_{ab,d}\,
\mathbb E[g(X_a)g(X_j)H_cH_d]\Big\}.
\end{aligned}
\tag{15}
\]
Set \(R_{j3}=0\). Formula (15) uses the joint transpose-return law:
the first line is its correlated Gaussian contribution; the second is
its reaction-alignment contribution. No cross-population neuron pairing
is made. All expectations are finite Gaussian integrals specified above.
For the training cross entries it reproduces
\(M_{12}=M_{21}=y_1y_2\kappa_2\).

For the cubic-clock approximation (29), evaluate (8)--(10) with unit
label direction \((1,s)\), and call the resulting \(P_3\) coefficient
\(\kappa_{3,s}\). The passive orbit approximation is then simply
\[
f_3(t)\simeq(k_1+s k_2)u(t)+\kappa_{3,s}u(t)^3.
\tag{31}
\]
The coefficient is supplied by the explicit finite Gaussian expectations
(14)--(15), not a passive training label or a fit to its future output.
Expanding (31) using (30) reproduces (13), because the unit-direction
training coefficients are \(P_1=\kappa,P_2=s\kappa\).

## 6. Directional sensitivities have their own time profile

Here \(R^h_{ab}(t,s)\) means the density of the lower feature response
at \(t\) to the reverse primitive for sample \(b\) at \(s<t\);
\(R^\delta\) is the strict-past upper backward response density.
In this section these are leading perturbative coefficient densities,
equivalently the leading fixed-mesh strict-past coefficients divided by
the timestep. Their formulas do not establish convergence of the full
nonlinear response measures to densities; that question remains open.
At leading order in labels,
\[
\begin{aligned}
R^h_{ab}(t,s)
&=y_b r(s) S_{ab}\,
\mathbb E[g(X_a)g(X_b)]+O(Y^3),\\
R^\delta_{ab}(t,s)
&=y_b r(s)\mathbb E[g(Z_a)g(Z_b)]+O(Y^3).
\end{aligned}
\tag{16}
\]
These are order \(Y\), not order \(Y^2\). Their multiplication by an
order-\(Y\) upper backward field produces an order-\(Y^2\) forward
representation effect.

For orthogonal training inputs,
\[
R^h_{12}=R^h_{21}=O(Y^3),\qquad
R^\delta_{12}=y_2r(s)\alpha^2+O(Y^3),\quad
R^\delta_{21}=y_1r(s)\alpha^2+O(Y^3).
\tag{17}
\]
The reverse directed responses are already nonzero when the lower
directed cross response is absent at leading order. Opposite labels
give opposite directions even though every Gram remains symmetric.

The same-time atom must be included:
\[
\chi_a(t)=a(t)\mathbb E[Q_yT''(Z_a)]+O(Y^3).
\tag{18}
\]
For training samples this simplifies to
\[
\chi_a(t)=2a(t)y_a(\beta-\alpha)+O(Y^3).
\]
Adding the integrated strict-past diagonal response gives
\[
a(t)y_a[\beta+2(\beta-\alpha)]H_a
=a(t)y_a(3\beta-2\alpha)H_a,
\]
which is precisely the checked total first-return coefficient.
Treating the curvature atom as the whole reciprocal response would give
the wrong magnitude and can give the wrong sign.

The accumulated leading response grows with \(a(t)\), while responses
born at a late time \(s\) are suppressed by \(r(s)\).
Past sensitivities need not vanish when the current training deficit
has become small.

For the passive receiver,
\[
R^h_{3b}=y_b r(s)S_{3b}\mathbb E[g(X_3)g(X_b)]+O(Y^3),
\]
and the analogous upper formula uses
\(\mathbb E[g(Z_3)g(Z_b)]\).
Active fields have no formal dependence on a passive source; the
corresponding active-to-passive primitive derivatives are zero.
There is never a \(y_3\).

For label rather than primitive probes, the leading passive derivative
is simply \(\partial f_3(t)/\partial y_b=a(t)k_b+O(Y^2)\).
This is a different derivative from (16).

## 7. Ablations with distinct leading predictions

The following table gives the coefficient multiplying
\(y_1y_2a(t)^2\). Its first two rows are changes to actual training
updates. The reciprocal rows are deliberate changes to the scalar
candidate, not claimed gradient flows of a corresponding dense network.

| Model change | Lower cross coefficient | Upper cross coefficient |
|---|---:|---:|
| Full system | \(\kappa_1\) | \(\kappa_W+\kappa_{\rm forward}+\kappa_{\rm alignment}\) |
| Freeze learned middle matrix \(W=G\) | \(\kappa_1\) | \(\kappa_{\rm forward}+\kappa_{\rm alignment}\) |
| Freeze first layer \(A\) | \(0\) | \(\kappa_W\) |
| Remove reverse reciprocal terms, including the atom; retain forward response | \(0\) | \(\kappa_W+\kappa_{\rm forward}\) |
| Remove forward reciprocal terms; retain reverse response | \(\kappa_1\) | \(\kappa_W+\kappa_{\rm alignment}\) |
| Remove both reciprocal directions | \(0\) | \(\kappa_W\) |

The reciprocal ablations must recompute their own causal laws and
covariances. They are not obtained by subtracting a term from a completed
full-model trajectory.
At this order the reverse return creates lower feature alignment; its
changed Gaussian forward covariance transmits the
\(\kappa_{\rm alignment}\) piece upward. The explicit forward reciprocal
term creates \(\kappa_{\rm forward}\).
The learned-middle write supplies \(\kappa_W\) independently.

Freezing both hidden parameter blocks leaves readout-only learning:
the population predictor (7) is then exact and \(M=0\).
It is a useful baseline, not an explanation of the feature changes.

### Gate controls must say what is being removed

Freezing the numerical backpropagation gates at their initialized values
does not remove the leading gate-selected mechanism: the actual gates
only change at order \(Y^2\). Therefore it preserves the displayed
order-\(Y^2\) Gram profiles and order-\(Y^3\) output correction.
Its first differences are fourth order in hidden representations and
fifth order in predictions, on a regular small-label branch.

Replacing derivative gates by constants instead removes the initial
selection by responsive versus saturated neurons and changes the
quadratic coefficients already. It is generally no longer gradient
descent for the stated tanh network, so the original loss identity must
not be assigned to it.

In a scalar-response implementation, a frozen gate retains its dependence
on the initial primitive coordinate. Simply zeroing its current curvature
response without retaining that initial-coordinate dependence is a
reciprocity ablation, not an equivalent implementation of frozen gates.

## 8. Controlled tests and invalidation criteria

No tests have been run in this note. The following are predictions to
check against dense dynamics and against the candidate's own ablations:

The highest-value test is the amplitude-independent internal orbit:
across label magnitudes, plot the trained output mode against integrated
mode residual and the two cross Grams against that coordinate squared.
The predictions are \(F(u)\simeq\nu u+\kappa u^3\),
\(\Delta C^\ell_{12}\simeq s\kappa_\ell u^2\), and trained-mode tangent
kernel \(\nu+3\kappa u^2\).
For finite-width diagnostics use
\((c_1+s c_2)/2\) as the mode residual and
\((K_{11}+K_{22}+2sK_{12})/2\) as its kernel; the other residual mode
measures departure from population symmetry.
Using measured residuals to replot a trajectory is a diagnostic only.
The predictive approximation must solve (29) from its initial constants,
without inserting the measured future residual.

1. For decreasing \(Y\), both cross Grams divided by \(y_1y_2\) should
   approach the full \(a(t)^2\) curves over a fixed multi-relaxation-time
   window. Halving \(Y\) divides their leading changes by four.
2. The passive leading response divided by \(Y\) should approach (7).
   After removing that baseline, the first feature-learning signal is
   cubic: halving \(Y\) divides it by eight, and its time dependence is
   the two-clock expression (13), not an arbitrary cubic fit.
3. Passive cross-label effects can be isolated by comparing
   \(f_3(y_1,y_2)-f_3(y_1,0)-f_3(0,y_2)\). The linear baseline cancels;
   the leading remainder is cubic and is specified by (10)--(15).
4. The ablation coefficient differences in the table separate learned
   middle memory from the two reciprocal channels. Agreement only with
   the middle-matrix term would miss a genuine first-layer contribution.
5. Primitive-probe responses should distinguish the symmetric Gram
   changes from the directed signs in (17), and should retain the
   diagonal term (18).
6. An initialized-gate freeze should agree to the orders stated above.
   A discrepancy already at those leading orders points to a different
   ablation definition, an omitted initialization dependence, or an
   implementation error.

Finite width requires an additional control. Its initial top training
Gram \(K_0^{(n)}\) is not exactly \(\nu I\). Its exact readout-only residual
is \(e^{-K_0^{(n)}t}y\), and the integrated coefficient is
\[
(K_0^{(n)})^{-1}(I-e^{-K_0^{(n)}t})y
\]
when that Gram is invertible. A comparison should use this per-run
readout baseline or resolve its fluctuations before interpreting a small
cubic passive signal. Likewise subtract the run's initial cross Grams
rather than assuming their finite-width values are exactly zero.

Persistent disagreement after decreasing labels, improving time
resolution, and resolving width fluctuations would invalidate the
coefficient calculation or its implementation. Agreement only at
very short times would not test the saturating-clock prediction.

Moderate-label runs should test where the profiles cease to collapse:
whether feature-dependent residual decay changes the clock; whether
cross-feature changes overshoot their perturbative plateaus; how much
the passive cubic correction explains the deviation from readout-only
learning; and when moving gates separate from initialized-gate controls.
Such deviations identify nonlinear feedback beyond this expansion.
They are not, by themselves, failures of the full causal candidate.
