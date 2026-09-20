# A natural-gradient constrained selector with path-independent limit

2026-09-19. Independent scoped candidate. Scientific inputs: complete
`MODEL_AND_GEOMETRY.md` and `CANONICAL_FEATURES.md` in this study only. Required
research and rigorous-mathematics skills, including the research-contract and
adversarial-audit references, were read. No other route, study history, numerical
experiment, external scientific source, or Git-index operation was used.

**Status at freeze:** the construction and proofs below are an independently
checked mathematical candidate, not an independent review or promoted result.
The candidate was completed before comparison with other routes.

The strongest conclusion is constructive but qualified. A weighted natural
loss gradient plus projected secondary regularization gives exact exponential
fitting and one deterministic limiting predictor for every path of an explicit,
nontrivial bounded random-ODE forcing class. It evaluates the full current
prediction Jacobian and its finite Gram inverse, but never evaluates the reduced
objective gradient or explicitly transports a readout through moving features.
The proof requires a large hidden weight and permits only controlled motion near
initialization. Consequently it does **not** establish a small perturbation of
the original physical gradient flow or substantial feature learning.

## 1. Contract and notation

Use exactly the population model, physical Hilbert spaces, fixed correlated
marks, canonical initialization, compatible finite circle data, and constants
from the two input files. Equal and antipodal constraints have been merged as
there. In particular,

\[
 F(h,c)=A_hc,\qquad e=F(h,c)-Y,\qquad |Y|=1,\qquad
 K_{h_0}\succeq\sigma I,\quad \sigma>0.
\]

The upper and lower populations and the true middle matrix are unchanged.
The question here is an explicitly modified optimizer, not a claim about the
unmodified physical loss flow. All statements concern exact population
integration at the fixed canonical order, and finite data of arbitrary size;
constants depend on their positive, potentially poorly conditioned \(\sigma\).
No time-discretization, particle, width, or order limit is taken.

Set \(\kappa=\sigma/2\), and retain \(a_1,a_3,r,C_J\) from the model file.
Thus \(K_h\succeq\kappa I\) for \(\|h-h_0\|\le2r\). Write

\[
 G_J=4a_1/\sigma^2,\qquad S=2/\kappa.
\]

Choose a finite, data-dependent \(\rho\ge1\) large enough that all the following
inequalities hold:

\[
 \rho\ge 2C_J,\qquad \rho\ge2G_J/r,\qquad
 G_J/\sqrt\rho\le1,\qquad S/\sqrt\rho\le r/2,\qquad
 a_1/(\kappa\sqrt\rho)\le1,                                      \tag{1}
\]

\[
 L_T:=2a_1/\sqrt\rho+a_3S/\rho
 \le \min\{\kappa/4,\sqrt\kappa/(4S)\}.                         \tag{2}
\]

These are genuine large-weight conditions, not small-regularization claims.
They can be met because all data constants are finite and \(\sigma>0\).
All coefficients use initialization and the training data only.

Introduce weighted coordinates in the same Hilbert space:

\[
 \xi=(u,c),\qquad u=\sqrt\rho(h-h_0),\qquad
 R=\tfrac12\|\xi\|^2
   =\tfrac\rho2\|h-h_0\|^2+\tfrac12\|c\|^2.
\]

For brevity let \(F(\xi)=A_{h_0+u/\sqrt\rho}c\), with Jacobian

\[
 T_\xi(v,d)=\rho^{-1/2}(DA_h[v])c+A_hd,\qquad
 U_\xi=T_\xi T_\xi^*,\qquad
 \Pi_\xi=I-T_\xi^*U_\xi^{-1}T_\xi.                          \tag{3}
\]

Here \(v\) is a hidden variation, including both physical hidden blocks, and
\(d\) is a readout variation. The matrix \(U\) has size \(m\times m\).
Whenever \(K_h\succeq\kappa I\), \(U\succeq K_h\succeq\kappa I\), and
\(\Pi\) is the orthogonal projection onto \(\ker T\).

## 2. The dynamics and admissible noise

Fix any bounded skew-adjoint operator \(\mathcal S\) of norm at most one
that is specified from the physical model, not an endpoint. One concrete
choice is the pointwise 90-degree rotation on the two coordinates of the lower
population's \(w\)-variation, with zero action on \(M\) and \(c\).
Let \(b:[0,\infty)\to\mathbb R\) be any measurable path with
\(|b(t)|\le b_{\max}<\infty\). It may be random, deterministic, or chosen
adversarially. For any fixed \(0<\varepsilon\le\kappa\), evolve

\[
 \dot\xi=-T_\xi^*e-\varepsilon\Pi_\xi\xi
       +\varepsilon b(t)\Pi_\xi\mathcal S\Pi_\xi\xi,\qquad
 \xi(0)=0.                                                       \tag{4}
\]

All initial fields therefore remain exactly canonical: \(h(0)=h_0,c(0)=0\).
The noise is tangent to both the current fitting fiber and the secondary
objective:

\[
 T_\xi n=0,\qquad \langle\xi,n\rangle=0,\qquad
 n=\varepsilon b(t)\Pi_\xi\mathcal S\Pi_\xi\xi.                  \tag{5}
\]

The second identity follows from skew-adjointness applied to \(\Pi\xi\).
The class does not require decay of \(b(t)\). Its state-dependent forcing
necessarily vanishes at the selected equilibrium, and later estimates prove
that its norm is bounded by a constant times the square root of the selection
energy. It is not additive Brownian noise, an Itô equation, or unrestricted SGD.

This is a nonzero class of allowable operators: on the infinite-dimensional
lower \(w\) subspace, imposing \(Tv=0\) and \(T\mathcal Sv=0\) excludes at most
\(2m\) scalar directions. Nonzero such \(v\) exist, and
\(\Pi\mathcal S\Pi v=\mathcal Sv\ne0\). The realized noise can still vanish
on particular symmetric trajectories; the theorem does not assert that every
nonzero path coefficient changes every instance's trajectory.

In physical coordinates, with \(G=\operatorname{diag}(\rho I,I)\), the first
term of (4) is

\[
 -G^{-1}DF(h,c)^*e.
\]

It is the natural gradient of \(\tfrac12\|e\|^2\) for the constant metric
\(G\). The regularizer is its metric gradient projected onto the exact current
fitting fiber. Consequently this construction changes the hidden mobility by
\(1/\rho\). A scalar adjustment of the loss convention changes only time.

## 3. Global well-posedness and exponential fitting

On \(\|\xi\|\le S\), conditions (1) keep \(\|h-h_0\|\le r/2\). The
source estimates give

\[
 \|T_\xi\|\le t_0:=\sqrt{1+a_1^2S^2/\rho},\qquad
 \operatorname{Lip}(T)\le L_T.                                  \tag{6}
\]

To verify the latter, subtract the hidden Jacobian blocks:

\[
 \rho^{-1/2}\|(DA_h)c-(DA_{\tilde h})\tilde c\|
 \le (a_3S/\rho)\|u-\tilde u\|
       +(a_1/\sqrt\rho)\|c-\tilde c\|.
\]

The readout blocks differ by at most
\((a_1/\sqrt\rho)\|u-\tilde u\|\). Summing proves (6).
Finite-matrix inversion with \(U\succeq\kappa I\) then makes \(\Pi\)
uniformly Lipschitz on this ball. Thus the vector field in (4) is measurable
in time and uniformly locally Lipschitz in state, with bounded coefficients
for bounded \(b\). The usual successive-approximation argument for an
integral equation on a short interval is a contraction under these bounds;
it gives a unique local absolutely continuous solution. The next estimate
keeps that solution strictly inside the ball and supplies uniform extension
intervals, proving existence for all time.

By the Hilbert-space chain rule, valid for absolutely continuous solutions
and the continuously differentiable \(F\),

\[
 \dot e=T\dot\xi=-Ue,\qquad
 \frac{d}{dt}|e|^2=-2\langle e,Ue\rangle\le-2\kappa|e|^2.
\]

Since \(e(0)=-Y\),

\[
 |e(t)|\le e^{-\kappa t},\qquad L(t)=|e(t)|^2\le e^{-2\kappa t}.    \tag{7}
\]

For \(s=\|\xi\|\), the projected regularizer and noise give

\[
 \tfrac12(s^2)'=-\langle T\xi,e\rangle
                 -\varepsilon\|\Pi\xi\|^2.
\]

The pointwise Jacobian bound is
\(\|T\|\le\sqrt{1+a_1^2s^2/\rho}\). Therefore, wherever \(s>0\),

\[
 s'\le\sqrt{1+a_1^2s^2/\rho}\,e^{-\kappa t}.
\]

The same integrated inequality holds through zeros by replacing \(s\) with
\(\sqrt{s^2+\delta^2}\) and letting \(\delta\downarrow0\). Integrating the
inverse-hyperbolic-sine derivative yields

\[
 s(t)\le\frac{\sqrt\rho}{a_1}
 \sinh\!\left(\frac{a_1(1-e^{-\kappa t})}{\kappa\sqrt\rho}\right)
 \le\frac{\sinh1}{\kappa}<S.                                  \tag{8}
\]

The last inequality uses convexity of sinh on \([0,1]\), which gives
\(\sinh x\le x\sinh1\), and \(\sinh1<2\). A first-exit argument closes the
bootstrap. There is a uniform margin to \(S\), and the uniformly Lipschitz
vector field permits continuation at any finite time. This proof uses no
finite-dimensional compactness assertion for a Hilbert-space ball.

The estimates are independent of the path and its oscillation frequency.
Only local existence constants depend on the finite bound \(b_{\max}\).

## 4. A unique constrained target, used only in the proof

The equations never evaluate \(\nabla J\). To identify their limit, use the
input's derived quantity \(J(h)=\tfrac12Y^TK_h^{-1}Y\).
On \(\|h-h_0\|\le r/2\), the map

\[
 h\longmapsto h_0-\rho^{-1}\nabla J(h)
\]

maps the closed ball to itself by (1) and has Lipschitz constant at most
\(C_J/\rho\le1/2\). Iterating it gives a Cauchy sequence because consecutive
differences form a geometric series; completeness gives its limit, continuity
makes it a fixed point, and the same strict Lipschitz bound proves uniqueness.
Call this deterministic point \(h_*\). Set

\[
 c_*=A_{h_*}^*K_{h_*}^{-1}Y,\qquad
 \lambda_*=K_{h_*}^{-1}Y,\qquad
 \xi_*=(\sqrt\rho(h_*-h_0),c_*).
\]

Then \(F(\xi_*)=Y\),

\[
 \|\lambda_*\|\le1/\kappa,\qquad \|c_*\|\le1/\sqrt\kappa,\qquad
 \|\xi_*\|^2\le G_J^2/\rho+1/\kappa\le1+1/\kappa<S^2.
\]

Here \(\kappa\le1/2\), because \(\sigma\le\|K_{h_0}\|\le1\).
The differential identity for \(J\) gives exactly

\[
 \xi_*=T_{\xi_*}^*\lambda_* .                                 \tag{9}
\]

The readout block is immediate. The hidden block is the fixed-point equation
\(\rho(h_*-h_0)=-\nabla J(h_*)=(DA_{h_*}[\cdot]c_*)^*\lambda_*\).
Thus \((h_*,c_*)\) is stationary for minimizing \(R\) subject to \(F=Y\).

Define the centered Lagrangian

\[
 V(\xi)=\tfrac12\|\xi\|^2-\tfrac12\|\xi_*\|^2
                       -\langle\lambda_*,F(\xi)-Y\rangle.
\]

Its gradient is \(\xi-T_\xi^*\lambda_*\), vanishing at \(\xi_*\). Let
\(\theta=L_T/\kappa\le1/4\). The Lipschitz bound for \(T\) proves

\[
 \|\nabla V(\xi)-(\xi-\xi_*)\|\le\theta\|\xi-\xi_*\|,\qquad
 \frac{1-\theta}{2}\|\xi-\xi_*\|^2
 \le V(\xi)\le
 \frac{1+\theta}{2}\|\xi-\xi_*\|^2.                            \tag{10}
\]

Indeed, integrate the gradient difference along the segment joining the two
points, which stays in the convex ball. On \(F=Y\), this is exactly
\(R-R(\xi_*)\); hence \(\xi_*\) is the unique constrained minimizer in
\(\|\xi\|\le S\). No claim of a global constrained minimizer outside this
certified neighborhood is required or proved.

## 5. Exponential selection and common predictor

Write \(d=\|\xi-\xi_*\|\) and \(p=\Pi_\xi\xi=\Pi_\xi\nabla V(\xi)\).
The Taylor remainder bound for \(F\), obtained by integrating \(T\) on the
same segment, is

\[
 \|T_\xi(\xi-\xi_*)-e\|\le\tfrac12L_Td^2.
\]

As \(\|T^*U^{-1}\|\le1/\sqrt\kappa\), this implies

\[
 \|(I-\Pi_\xi)(\xi-\xi_*)\|
 \le |e|/\sqrt\kappa+L_Td^2/(2\sqrt\kappa).
\]

Combine this with (10), \(d\le2S\), and the triangle inequality to get

\[
 \|p\|\ge\eta d-|e|/\sqrt\kappa,\qquad
 \eta:=1-\theta-L_TS/\sqrt\kappa\ge1/2.                       \tag{11}
\]

Noise contributes zero to \(\dot V\), because it is tangent to both terms
in its definition. Equation (4) gives

\[
 \dot V=-\varepsilon\|p\|^2-\langle T\nabla V,e\rangle.
\]

Use \(\|p\|^2\ge\eta^2d^2/2-|e|^2/\kappa\),
\(\|T\nabla V\|\le t_0(1+\theta)d\), and the elementary inequality
\(ab\le a^2/4+b^2\), with the corresponding factors rescaled, to obtain

\[
 \dot V\le-\frac{\varepsilon\eta^2}{4}d^2+C_e|e|^2
          \le-\nu V+C_e e^{-2\kappa t},                       \tag{12}
\]

where

\[
 C_e=\frac\varepsilon\kappa+
        \frac{t_0^2(1+\theta)^2}{\varepsilon\eta^2},\qquad
 \nu=\frac{\varepsilon\eta^2}{2(1+\theta)}.
\]

Because \(0<\varepsilon\le\kappa\), \(0<\nu\le\kappa/2<2\kappa\).
Multiplication by \(e^{\nu t}\) and integration prove

\[
 V(t)\le
 \left(V(0)+\frac{C_e}{2\kappa-\nu}\right)e^{-\nu t},\qquad
 \|\xi(t)-\xi_*\|\le
 \left[\frac{2}{1-\theta}
  \left(V(0)+\frac{C_e}{2\kappa-\nu}\right)\right]^{1/2}
 e^{-\nu t/2}.                                                \tag{13}
\]

Thus **every** permitted path converges to the same state. This is stronger
than uniqueness merely on training predictions. The circle-wide feature
Lipschitz estimate in the model file gives

\[
 \sup_{|x|=\sqrt2}|f_{h(t),c(t)}(x)-f_{h_*,c_*}(x)|
 \le\|c(t)-c_*\|+a_1\|c_*\|\|h(t)-h_*\|
 \le\left(1+\frac{a_1}{\sqrt{\rho\kappa}}\right)
       \|\xi(t)-\xi_*\|.                                    \tag{14}
\]

The limiting predictor is consequently deterministic on the entire circle,
not only modulo training-point nullspace. This conclusion uses state-norm
convergence, so it invokes no unproved interchange of time and expectation.
Finally, (10) gives the promised noise estimate

\[
 \|n(t)\|\le\varepsilon b_{\max}(1+\theta)
                    \sqrt{2V(t)/(1-\theta)}.
\]

## 6. Current information and invariance

Every dynamic quantity in (4) is computed from the current \((h,c)\), the
fixed marks and initialization, the finite training data, and the current
scalar forcing \(b(t)\). The full Jacobian keeps both hidden variations and
the actual \(M^T\) in the lower adjoint. No feature activation is frozen in
these evaluations. One finite \(m\times m\) inverse is used for the full
Jacobian's projection; no additional dual variable or hidden history is kept.

The fixed reference \(g,D\) and all the necessary expectations are determined
by the prescribed initialization and current joint laws
\(\Gamma_1=\operatorname{Law}(b_1,g,w)\),
\(\Gamma_2=\operatorname{Law}(b_2,c)\), together with \(M\). The concrete
pointwise rotation \(\mathcal S\) uses no coupling between separate
populations. Thus the rule is restartable from the declared current state
and future forcing.

Measure-preserving relabelings of either population act unitarily on the
respective Hilbert fields. They conjugate \(T,\Pi\), commute with the stated
pointwise \(\mathcal S\), and preserve all norms and expectations; (4) is
therefore equivariant and its represented predictor invariant. The same
statement holds under orthogonal re-expressions of dictionary coordinates
when all tensors and fixed initialization data are transformed together.
Arbitrary non-isometric changes of the physical metric are **not** claimed as
invariances. The noise operator's specified physical orientation is part of
the forcing rule and must also be transformed if spatial coordinates change.

## 7. How much hidden learning has actually been proved?

The endpoint solves

\[
 \rho(h_*-h_0)+\nabla J(h_*)=0.
\]

In this certified ball,

\[
 h_*=h_0\quad\Longleftrightarrow\quad\nabla J(h_0)=0.
\]

Thus the method does not freeze the hidden state, and its fixed point is a
current-data constrained optimum. Nevertheless, the supplied geometry alone
does not prove \(\nabla J(h_0)\ne0\) for **every** compatible multi-point
labeling. Universal strict hidden displacement is an open additional claim,
not a consequence of positive definiteness.

There is an exact nontrivial instance check. For one training direction,
\(J=1/(2K)\). Vary \(M\) along \(M_s=(1+s)D\), keeping \(w=g\).
If \(Z_0=b_2^TDa_{h_0}(x)\), then

\[
 \left.\frac d{ds}K(h_s)\right|_{s=0}
 =2E_2[\tanh(Z_0)Z_0\operatorname{sech}^2(Z_0)]>0.
\]

The integrand is positive when \(Z_0\ne0\), and \(K(h_0)>0\) ensures that
this event has positive probability. Hence \(DJ(h_0)[0,D]<0\), and
\(h_*\ne h_0\) for either compatible one-point label. The hidden displacement
is truly learned in these instances and for any other data with nonzero
\(\nabla J(h_0)\), while the estimate \(\|h_*-h_0\|\le G_J/\rho\) openly
shows the small-motion regime.

## 8. Comparison with simpler optimizer modifications

These are algebraic comparisons made after constructing the candidate; they
are not reports from another route.

1. **Ordinary quadratic weight decay added to loss.** Stationarity of
   \(\tfrac12\|A_hc-Y\|^2+\varepsilon R\) at exact fit forces
   \(\varepsilon c=0\), contradicting \(Y\ne0\). A finite positive weight
   therefore generally destroys exact interpolation. Projection in (4)
   avoids this obstruction exactly.
2. **Unweighted physical loss gradient plus projected secondary gradient.**
   For \(\dot z=-DF(z)^*e-\varepsilon\Pi_z\nabla R(z)\),
   \(\dot e=-DFDF^*e\) is still exact, and constrained equilibria are the
   same. However the weighted-radius proof (8) no longer applies: the
   primary term has a different metric. A global invariant neighborhood
   from the canonical \(c=0\) initialization has not been proved here.
   This is a gap for that closer candidate, not a no-go theorem.
3. **Pure Gauss--Newton normal fitting.** Replacing the first term in (4) by
   \(-T^*U^{-1}e\) yields \(e(t)=-e^{-t}Y\) exactly and the simpler radial
   bound \(\|\xi(t)\|\le(1-e^{-t})/\sqrt\kappa\). The same projection
   geometry can select the endpoint. This is another, larger change of
   fitting mobility; no need for it was found in the present proof.
4. **Nonsmooth exact penalties or augmented Lagrangians.** A finite
   quadratic penalty alone is not exact. An \(\ell^1\)-type exact penalty
   or a multiplier equation requires separate well-posedness, localization,
   and convergence arguments. This report does not claim those routes fail
   and does not import their results.

For each fixed certified \(\rho\), the secondary drift and the noise in (4)
can be made arbitrarily small on the invariant ball by choosing
\(\varepsilon\downarrow0\), at the cost of a vanishing selection rate.
That observation does not make the **whole** optimizer a small perturbation:
the \(1/\rho\) hidden mobility and the large objective weight remain.
At \(\varepsilon=0\) this proof gives fitting, but its endpoint-selection
argument disappears.

## 9. Claim ledger and remaining obstruction

| Claim | Status and exact scope |
|---|---|
| Positive canonical Gram for all finite compatible data after merging | Input theorem; no uniform conditioning claim. |
| Global solution from canonical initialization | Proved above for the modified natural-gradient ODE and bounded measurable forcing. |
| Exponential fitting | Exact inequality (7), every permitted forcing path. |
| Deterministic full predictor limit | Proved by (13)--(14), uniformly on the circle. |
| Unique constrained optimizer | Proved only in the certified weighted ball. |
| No dynamic evaluation of \(\nabla J\) or inverse-feature transport | Directly inspectable in (3)--(4); a full-Jacobian inverse remains. |
| Nonzero learned hidden endpoint | Proved when \(\nabla J(h_0)\ne0\), including every one-point instance. Universal multi-point strictness remains open. |
| Small perturbation of original physical gradient flow | Not proved; large anisotropic mobility is a substantive change. |
| Unrestricted persistent noise robustness | Not claimed; noise must be tangent and vanish with selection energy. |
| Strong feature-learning mechanism beyond a small neighborhood | Not proved; the construction deliberately uses a certified small-motion regime. |

The most consequential unresolved step toward the original request is a
localization proof for the ordinary physical loss gradient combined with
projected secondary regularization, without a large change in its mobility.
The present route supplies a complete nearby construction and a precise
endpoint criterion, while leaving that stronger optimizer-closeness claim
and universal strict hidden displacement unresolved.
