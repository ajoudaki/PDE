# Where passive nonadditivity enters during learning

2026-10-07. Scoped analytical diagnostic of the existing beyond-initialization
investigation. Inputs are CANDIDATE_SYSTEM.md, ANALYTICAL_LEARNING_PROFILES.md,
PASSIVE_CLOCK_CHECK.md, and BEYOND_INITIALIZATION_RESULT.md. No experiments,
external sources, or global approximation proof are added here.

The training cross Grams do not determine the passive output. The missing
observable is the readout projection of the passive feature's departure from
the geometric mixture of the two training features. Its exact identities below
separate where that departure is inherited, transported, and changed. They also
give diagnostics that distinguish a wrong clock from an inadequate passive
feature trajectory.

## 1. Setup and the observable the training reduction omits

Use the dense two-hidden-layer tanh model with width n, no biases, and
\(v_1=e_1,v_2=e_2,v_3=(2e_1+e_2)/\sqrt5\). Its parameters are
\(A\in\mathbb R^{n\times2}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), with

\[
z_{1,a}=Av_a,\quad h_{1,a}=\tanh z_{1,a},\quad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=\tanh z_{2,a},\quad
f_a=\langle w,h_{2,a}\rangle_n,
\qquad \langle x,y\rangle_n=\frac{x^\top y}{n}.
\]

Tanh and its derivative \(g(z)=\operatorname{sech}^2z\) act componentwise.
Only samples 1 and 2 train, with \(c_b=y_b-f_b\),
\(y=Y(1,s)\), \(s\in\{-1,1\}\), and loss
\(\mathcal L=(c_1^2+c_2^2)/2\). The block mobilities are \((n,1,n)\).
Write

\[
\delta_{2,a}=g(z_{2,a})\odot w,\qquad
\delta_{1,a}=g(z_{1,a})\odot W^\top\delta_{2,a}.
\]

Backward fields for input 3 are sensitivities of its output, not training
forces. The actual velocities are

\[
\dot A=\sum_{b=1}^2c_b\delta_{1,b}v_b^\top,\qquad
\dot W=\frac1n\sum_{b=1}^2c_b\delta_{2,b}h_{1,b}^\top,\qquad
\dot w=\sum_{b=1}^2c_bh_{2,b}.
\tag{1}
\]

Set \(\lambda_1=2/\sqrt5\), \(\lambda_2=1/\sqrt5\). Define the two
feature defects and their scalar output projection by

\[
q_\ell=h_{\ell,3}-\lambda_1h_{\ell,1}-\lambda_2h_{\ell,2},
\qquad
\varepsilon=f_3-\lambda_1f_1-\lambda_2f_2.
\]

Linearity of the readout gives the exact identity

\[
\varepsilon=\langle w,q_2\rangle_n.
\tag{2}
\]

In the symmetric population flow, \(f_2=sf_1\), so
\(f_3=(2+s)f_1/\sqrt5+\varepsilon\). In each finite realization use its
actual two training predictions in (2); imposing population symmetry would
introduce another error. For the reported opposite-label endpoint near
\((f_1,f_2)=(0.6,-0.6)\), the geometric term is approximately 0.26833
and the observed passive value 0.35790 leaves approximately 0.08957 in
\(\varepsilon\). This term is substantial after training has fitted.

Even knowledge of the full current feature Gram would only give the norm

\[
\|q_2\|_n^2=C^2_{33}+\sum_{a,b=1}^2\lambda_a\lambda_bC^2_{ab}
-2\sum_{a=1}^2\lambda_aC^2_{3a}.
\]

One also needs its alignment with w to obtain (2). The two training cross
Grams retain neither the passive norm nor this alignment.

## 2. Inherited nonlinearity and the two activation layers

The first-layer preactivations obey
\(z_{1,3}=\lambda_1z_{1,1}+\lambda_2z_{1,2}\) at every time, but tanh
does not preserve that relation. Thus \(q_1(0)\) and \(q_2(0)\) need not
vanish, although \(w(0)=0\) implies \(\varepsilon(0)=0\).
This is inherited nonlinear geometry, not a feature change caused by training.

Let \(G=W(0)\). The upper preactivation defect has the exact decomposition

\[
z_{2,3}-\sum_{a=1}^2\lambda_az_{2,a}=Wq_1
=Gq_1(0)+G[q_1-q_1(0)]+(W-G)q_1.
\tag{3}
\]

The three terms are the initialized lower defect passed through the initial
map, change of that lower defect passed through the same map, and its image
under the learned middle matrix. This is an additive identity at the current
full state; it is not the difference between three separately trained models.

To isolate the additional upper nonlinearity, define
\(z_{2,\mathrm{mix}}=\sum_{a=1}^2\lambda_az_{2,a}\) and the componentwise
secant gate

\[
\Gamma_2=\int_0^1g(z_{2,\mathrm{mix}}+\tau Wq_1)\,d\tau.
\]

The fundamental theorem of calculus gives

\[
q_2=\Gamma_2\odot Wq_1+
\left[\tanh z_{2,\mathrm{mix}}
-\sum_{a=1}^2\lambda_a\tanh z_{2,a}\right].
\tag{4}
\]

Use the same actual \(\Gamma_2\) on all three terms in (3) before projecting
on w. Together with the bracket in (4), this gives four additive contributions
to (2). Recomputing a different gate separately for each term would destroy
that identity. The integral definition handles \((Wq_1)_i=0\); no division
by a vanishing preactivation defect is required. The bracket is an upper-layer
failure of additivity, not a Jensen gap: the coefficients sum to \(3/\sqrt5\).

A second useful exact split is

\[
\varepsilon=\langle w,q_2(0)\rangle_n
+\langle w,q_2-q_2(0)\rangle_n.
\tag{5}
\]

The first term reads out inherited nonlinear features using the actual learned
readout; it is not a readout-only training control. The second measures changed
passive geometry in the same readout direction. Equation (5) separates inherited
and changed features without equating either with a counterfactual experiment.

## 3. Exact differential sources on one full trajectory

Differentiating (2) gives three parameter-block sources:

\[
\begin{aligned}
\dot\varepsilon={}&\langle\dot w,q_2\rangle_n\\
&+\left\langle w,
g(z_{2,3})\odot\dot W h_{1,3}
-\sum_{a=1}^2\lambda_a g(z_{2,a})\odot\dot W h_{1,a}
\right\rangle_n\\
&+\left\langle w,
g(z_{2,3})\odot W\dot h_{1,3}
-\sum_{a=1}^2\lambda_a g(z_{2,a})\odot W\dot h_{1,a}
\right\rangle_n.
\end{aligned}
\tag{6}
\]

These are readout learning, middle-matrix learning, and lower-feature motion.
Each can be signed; their time integrals add exactly to \(\varepsilon(t)\)
because its initial value is zero. At initialization only the readout source
can be nonzero. Split it further as
\(\langle\dot w,q_2(0)\rangle_n+
\langle\dot w,q_2-q_2(0)\rangle_n\) if inherited geometry is the question.

The same calculation is available from Gram observables. Define the current
\(C^\ell_{ab}=\langle h_{\ell,a},h_{\ell,b}\rangle_n\) and
\(D^\ell_{ab}=\langle\delta_{\ell,a},\delta_{\ell,b}\rangle_n\). Then

\[
\begin{aligned}
\dot\varepsilon=\sum_{b=1}^2c_b\bigg\{
&C^2_{3b}-\sum_{a=1}^2\lambda_aC^2_{ab}\\
&+C^1_{3b}D^2_{3b}
-\sum_{a=1}^2\lambda_a C^1_{ab}D^2_{ab}\\
&+\lambda_b(D^1_{3b}-D^1_{bb})\bigg\}.
\end{aligned}
\tag{7}
\]

The three lines correspond to (6). The last line uses
\(v_a^\top v_b=\mathbf1_{a=b}\) for training indices and
\(v_3^\top v_b=\lambda_b\). Equation (7) is regular even if a residual is
zero; no coefficient is estimated by dividing a measured velocity by a residual.

The first-layer source has a sharper interpretation. Since
\(\dot z_{1,b}=c_b\delta_{1,b}\) for b=1,2,

\[
\dot q_1=\sum_{b=1}^2\lambda_bc_b
[g(z_{1,3})-g(z_{1,b})]\odot\delta_{1,b}.
\tag{8}
\]

Thus training changes lower nonadditivity through the difference between the
query's and training sample's activation sensitivities. The initialized gates
already differ across inputs; their subsequent drift is a separate effect.

Each upper feature source also has a transport and a gate-mismatch part. For
middle learning its vector before projection on w equals

\[
g(z_{2,3})\odot\dot Wq_1+
\sum_{a=1}^2\lambda_a[g(z_{2,3})-g(z_{2,a})]\odot\dot Wh_{1,a}.
\tag{9}
\]

For lower motion it equals

\[
g(z_{2,3})\odot W\dot q_1+
\sum_{a=1}^2\lambda_a[g(z_{2,3})-g(z_{2,a})]\odot W\dot h_{1,a}.
\tag{10}
\]

These follow by substituting the definitions of q and collecting terms.
They identify whether a large passive source transports a lower defect or
arises because the same transported motion receives different upper gates.

To isolate gate *drift* along this trajectory, substitute
\(g(z_{\ell,a}(t))=g(z_{\ell,a}(0))+[g(z_{\ell,a}(t))-g(z_{\ell,a}(0))]\)
in the desired source. The bracket has the exact curvature representation

\[
g(z_{\ell,a}(t))-g(z_{\ell,a}(0))
=\int_0^t\tanh''(z_{\ell,a}(\tau))\odot\dot z_{\ell,a}(\tau)\,d\tau.
\tag{11}
\]

This isolates a gate factor in the actual source while holding its other actual
factors fixed. It does not remove the indirect effects of gates on those other
factors. Curvature is therefore a partition within (6), not an independent
fourth parameter-block source. The reported full-versus-affine difference is
a valid intervention comparison, but cannot be identified with (11), or with
the passive cubic error, by subtracting its endpoint from another experiment.

## 4. Corresponding diagnostics in the causal population system

Here all fields are the representative-neuron fields of CANDIDATE_SYSTEM.md,
and products are expectations within the appropriate population. Define
\(q_\ell^k=h_{\ell,3}^k-\sum_a\lambda_a h_{\ell,a}^k\) and

\[
\Delta C_b^\ell(k,j)=C^\ell_{3b}(k,j)
-\sum_{a=1}^2\lambda_aC^\ell_{ab}(k,j)
=\mathbb E[q_\ell^k h_{\ell,b}^j].
\]

The exact passive readout-history identity is

\[
\varepsilon^k=\mathbb E[w^kq_2^k]
=\Delta\sum_{j<k,b\le2}c_b^j\Delta C_b^2(k,j).
\tag{12}
\]

It requires current passive geometry against earlier training features, not
just a current passive Gram. To separate those roles at finite step size,

\[
\varepsilon^{k+1}-\varepsilon^k
=\mathbb E[(w^{k+1}-w^k)q_2^{k+1}]
+\mathbb E[w^k(q_2^{k+1}-q_2^k)].
\tag{13}
\]

The first term adds the new readout write, evaluated with the new query;
the second reinterprets previous writes through query movement. Using time-k
queries in both terms instead would require the extra product of increments.

Let \(\Delta\eta^k=\eta_3^k-\sum_a\lambda_a\eta_a^k\) and
\(\Delta R_b^h(k,j)=R^h_{3b}(k,j)-\sum_a\lambda_aR^h_{ab}(k,j)\).
Subtracting the candidate's upper preactivation equations gives

\[
\begin{aligned}
z_{2,3}^k-\sum_{a=1}^2\lambda_az_{2,a}^k
={}&\Delta\eta^k
+\sum_{j<k,b\le p}\Delta R_b^h(k,j)\delta_{2,b}^j\\
&+\Delta\sum_{j<k,b\le2}c_b^j
\Delta C_b^1(k,j)\delta_{2,b}^j.
\end{aligned}
\tag{14}
\]

The last term is the learned-middle contribution in (3). The Gaussian and
reciprocal terms together represent the initialized map acting on the evolving
lower defect. In particular

\[
\mathbb E[\Delta\eta^k\Delta\eta^j]=\mathbb E[q_1^kq_1^j],
\tag{15}
\]

so the Gaussian term must not be called a frozen initialization contribution.
Its covariance changes when lower features move. Formula (4), with the same
current secant gate on each summand of (14), gives additive current output
projections in the upper population. No arbitrary cross-population pairing is
used. These discrete identities require no continuum response density.

## 5. A discriminating measurement sequence

In the symmetric population flow, the orbit derivative of (7) is its right
side with \(c_b\) replaced by \(\ell_b\), where \(\ell=(1,s)\).
This is a derivative along the residual-free vector field, so it remains
defined at fitting; it need not be computed by dividing by a small residual.
Write the initialized training coefficients as
\(\nu=0.236450410504\), \(\kappa=0.181152636696\), so
\(F(u)=\nu u+\kappa u^3+O(u^5)\). Combining the passive coefficients
in PASSIVE_CLOCK_CHECK.md with (2) gives

\[
\begin{array}{c|cc}
s&\text{coefficient of }u\text{ in }\varepsilon
&\text{coefficient of }u^3\text{ in }\varepsilon\\
-1&0.003487192962&0.022445179955\\
+1&-0.013396124315&-0.059647423345
\end{array}
\]

These are \((k_1+sk_2)-(2+s)\nu/\sqrt5\) and
\(\kappa_{3,s}-(2+s)\kappa/\sqrt5\), respectively, with
\(k_b=\mathbb E[h_{2,3}(0)h_{2,b}(0)]\). Their orbit-derivative
prediction is the first coefficient plus three times the second coefficient
times \(u^2\). Comparing (7) with this prediction, and separating its three
lines, locates the accumulated defect discrepancy more sharply than a final
passive-output comparison alone.

The following measurements resolve different explanations of cubic failure:

1. Compare the measured passive output at the measured mode clock
   \(u(t)=\int_0^t[c_1(t')+s c_2(t')]/2\,dt'\) with its cubic orbit value. Also record
   the orthogonal residual mode \((c_1-s c_2)/2\). Persistence of the
   discrepancy after reparametrization identifies an observable error beyond
   a clock error; large orthogonal motion limits the population symmetry
   interpretation. The existing reported clock substitution leaves most of
   the opposite-label passive discrepancy unresolved.
2. Record (2) and (5), the RMS sizes of \(q_1,q_2\), and the signed projection
   of q2 onto w. Where both norms are nonzero, record
   \(\varepsilon/(\|w\|_n\|q_2\|_n)\). A growing feature norm and a growing
   readout alignment are different mechanisms. At a zero norm report the
   unnormalized projection, not an undefined cosine.
3. Integrate the three signed rates in (6) or (7) and verify reconstruction
   of (2). Then partition the feature rates using (8)--(11). This locates
   the error-producing source on the unchanged trajectory; it does not infer
   additive contributions from separately fitted ablations.
4. For the causal solver, record the full history contractions (12), the
   write/query split (13), and the projections of (14) through (4). This
   distinguishes current passive motion from changes to earlier training
   features written into w. Recording only \(C^2_{3b}(k,k)\) misses the latter.
5. Compare full, frozen-middle, and anchored-affine controls at comparable
   internal clock as well as physical time. These comparisons test mechanisms,
   while (6) supplies additive attribution. Persistence of error under frozen
   middle learning would rule out learned middle writes as its sole cause;
   it would not rule out lower transport or nonlinear activation evolution.

All finite-width defect norms and feature changes should use that realization's
initial panel. Numerical time integration of the source rates needs its own
reconstruction tolerance; discrete causal data should use (13) exactly.

## 6. A small, explicit continuation worth testing

There is a more informative candidate than adding a fitted fifth-order output
coefficient: retain the known quadratic preactivation displacement, but evaluate
tanh on it without expanding the activation. This tests nonlinear gating along
the initialized upper preactivation displacement. Later changes of that
direction, including the effect of lower-layer nonlinear evolution on it,
remain omitted mechanisms.

The required frozen random fields can be defined by an initialization program.
At finite width, set \(X_a=z_{1,a}(0)\), \(H_a=\tanh X_a\),
\(Z_a=GH_a\), \(Q=\tanh Z_1+s\tanh Z_2\), and \(\ell=(1,s)\).
For each panel index define

\[
\begin{aligned}
J_{1,a}&=g(X_a)\odot\sum_{b=1}^2
\ell_b S_{ab}\,g(X_b)\odot G^\top[g(Z_b)\odot Q],\\
L_a&=\sum_{b=1}^2\ell_b C^1_{ab}(0,0)[g(Z_b)\odot Q]+GJ_{1,a}.
\end{aligned}
\tag{16}
\]

Here \(S_{ab}=v_a^\top v_b\), \(\theta=(A,W,w)\), and the gradient below
uses the block mobilities \((n,1,n)\). Differentiating the residual-free training
orbit \(d\theta/du=\nabla(f_1+sf_2)\) shows
\(J_{1,a}=d^2h_{1,a}/du^2(0)\) and \(L_a=d^2z_{2,a}/du^2(0)\): its
initial hidden velocities vanish, \(w'(0)=Q\), and the two terms in L are
\(W''(0)H_a\) and \(G h_{1,a}''(0)\). This program specifies their joint
initialization law; the corresponding population limit is required for the
population approximation. It is not a training rollout.

Define the proposed continued upper features and readout by

\[
\widehat h_{2,a}(u)=\tanh\!\left(Z_a+\frac{u^2}{2}L_a\right),\qquad
\widehat w(u)=\int_0^u
[\widehat h_{2,1}(v)+s\widehat h_{2,2}(v)]\,dv,
\]
\[
\widehat\varepsilon(u)=\mathbb E\!\left[
\widehat w(u)\left(\widehat h_{2,3}(u)
-\sum_{a=1}^2\lambda_a\widehat h_{2,a}(u)\right)\right].
\tag{17}
\]

Keep the established proposed training clock
\(\dot u=Y-\nu u-\kappa u^3\), and predict

\[
\widehat f_3(u)=\frac{2+s}{\sqrt5}(\nu u+\kappa u^3)
+\widehat\varepsilon(u).
\tag{18}
\]

Equation (18) continues the passive defect while preserving that training
clock. It does not identify the auxiliary training outputs reconstructed
from (17) with the cubic clock beyond their common expansion.

This proposal has an algebraic consistency check. Since
\(\widehat h_{2,a}=\tanh Z_a+u^2g(Z_a)L_a/2+O(u^4)\), integrating its
training combination produces the \(1/6\) readout-write coefficient, while
the current query supplies the \(1/2\) coefficient. Thus (17)--(18) reproduce
the already derived passive linear and cubic coefficients exactly in the
specified population law. All higher coefficients come from the explicit
tanh evaluation along a frozen direction; none is fitted.

It is autonomous once its frozen joint law or quadrature for
\((Z_1,Z_2,Z_3,L_1,L_2,L_3)\) is supplied. A finite initialization program
can save these six n-vectors and discard G after constructing them; the fixed
storage is O(n), with an O(n^2) initial matrix calculation, and evaluation
of (17) still requires numerical integration. An exact population evaluation
needs the joint initial law, not just the few scalar contractions in the cubic
formula. The matrix \(M_{ab}\) alone does not specify (17). This note supplies
the initialization program, not a validated quadrature implementation or a
new constant-storage population closure.

The decisive diagnostic is to compare the true preactivation displacement
with \(u^2L_a/2\), and to compare its readout-weighted gate effects through
(6). If that direction remains accurate while the polynomial passive output
fails, (17) directly targets the missing activation evolution. If the direction
rotates substantially, one needs an evolving feature/response observable;
exactly reevaluating tanh on a wrong displacement will not repair it. No
moderate-amplitude improvement, error bound, or all-time guarantee for
(17)--(18) is asserted here.
