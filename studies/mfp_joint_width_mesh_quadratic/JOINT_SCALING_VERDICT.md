# Joint width--mesh scaling for the normalized quadratic loss flow

## 1. Model and verdict

Let

\[
 c=3^{-1/2},\qquad H=c\,u^{\odot2},\qquad
 z=n^{-1/2}WH,
 \qquad f_n=n^{-1}a^{\mathsf T}(c\,z^{\odot2})
\]

with all coordinates of \(a,u,W\) independent standard Gaussians at
initialization.  Put

\[
 \ell_n={1\over2}(1-f_n)^2,
 \qquad g_n=n\nabla_{(a,u,W)}f_n .
\]

The finite-width half-loss ODE and its explicit-Euler scheme are

\[
 \dot\theta=(1-f_n(\theta))g_n(\theta),                 \tag{1.1}
\]

\[
 \theta_{k+1}=\theta_k+h_n(1-f_n(\theta_k))g_n(\theta_k). \tag{1.2}
\]

Write \(L_n=\sqrt{\log n}\).  The following statement is unconditional.

**Theorem 1 (explicit ODE-consistent joint no-go).**  Suppose

\[
 h_n n^{14}
 \exp\!\left({6\cdot10^{11}n^9\over L_n}\right)
 \longrightarrow0.                                      \tag{1.3}
\]

Let \(\bar f_n^{h_n}\) and \(\bar\ell_n^{h_n}\) be the continuous
piecewise-linear parameter interpolation of (1.2), evaluated through the
network and the loss.  There are deterministic \(\delta,c_*>0\) and random
times \(\tau_n\le2/L_n\), with probability tending to one, such that

\[
 \left|\bar f_n^{h_n}(\tau_n)-f_n(0)\right|\ge\delta,
 \qquad
 \left|\bar\ell_n^{h_n}(\tau_n)-\ell_n(0)\right|\ge c_* . \tag{1.4}
\]

Consequently these joint Euler interpolants cannot converge in probability
uniformly on any fixed interval \([0,T]\) to a continuous predictor or loss
with the initialized trace.

Condition (1.3) is deliberately crude.  It is an explicit sufficient
condition for Euler--ODE consistency, not a sharp mesh threshold.

The complete status is therefore:

1. finite-width ODE first, then width: no continuous initialized mean-field
   limit, by the canonical covariant-Schur concentration theorem;
2. width first at every fixed finite Euler schedule, then mesh: no continuous
   initialized limit, by the all-order positive-polynomial initial-layer
   theorem;
3. simultaneous width and mesh: Theorem 1 rules out every diagonal obeying
   (1.3).  No theorem presently rules out every under-resolved diagonal, and
   no under-resolved diagonal has been proved to converge to a nontrivial
   continuous mean-field loss gradient flow.

In particular, failure of both iterated limits must not be promoted to a
theorem about every diagonal without a uniform-in-horizon width estimate or
a discrete version of the covariant-Schur extreme-column theorem.

## 2. Exact normalized feature field

Define

\[
 Y=c z^{\odot2},\qquad C=2c\,a\odot z,
 \qquad b=n^{-1/2}W^{\mathsf T}C .                       \tag{2.1}
\]

Direct differentiation gives

\[
 g_n(a,u,W)=\left(Y,\;2c\,u\odot b,\;n^{-1/2}CH^{\mathsf T}\right). \tag{2.2}
\]

Thus (1.2) is exactly the intended simultaneous muP Euler update; no
finite-width Taylor expansion is being substituted for it.

Let

\[
 \widehat z=n^{-1/2}Wu^{\odot2},\qquad
 \widehat f_n=n^{-1}a^{\mathsf T}\widehat z^{\odot2}.
\]

Then exactly

\[
 z=c\widehat z,\qquad f_n=c^3\widehat f_n,
 \qquad g_n=c^3\widehat g_n,                             \tag{2.3}
\]

where \(\widehat g_n=n\nabla\widehat f_n\).  Hence the normalized flow
is the raw quadratic feature flow under the scalar clock

\[
 {ds\over dt}=c^3(1-c^3\widehat f_n).                    \tag{2.4}
\]

The proved covariant-Schur theorem supplies a raw-output increase
\(\widehat\delta>0\) by raw feature time

\[
 s_n\le {0.09+o(1)\over L_n}                             \tag{2.5}
\]

with probability tending to one.  Decrease \(\widehat\delta\), if
necessary, so that \(c^3\widehat\delta<1/4\).  Since
\(f_n(0)\to0\) in probability, the residual in (2.4) is at least \(1/2\)
up to this hit, on an event of probability tending to one.  Therefore its
physical hitting time satisfies

\[
 t_n\le {2s_n\over c^3}< {2\over L_n}                    \tag{2.6}
\]

eventually.  At that time

\[
 f_n(t_n)-f_n(0)=\delta_0,
 \qquad \delta_0=c^3\widehat\delta>0.                   \tag{2.7}
\]

This proves the continuous finite-width initial layer for the normalized
activation, with no exchange of width and time limits.

## 3. Global existence of each finite-width loss ODE

Equip parameter space with

\[
 \langle v,w\rangle_*=n^{-1}v^{\mathsf T}w .             \tag{3.1}
\]

Then \(g_n=\operatorname{grad}_*f_n\), and (1.1) is
\(-\operatorname{grad}_*\ell_n\).  Consequently

\[
 {d\ell_n\over dt}
 =-{1\over n}\|\dot\theta\|_2^2.                       \tag{3.2}
\]

For every finite \(T\),

\[
 \|\theta(t)-\theta(0)\|_2
 \le\sqrt{Tn\ell_n(0)},\qquad 0\le t\le T.             \tag{3.3}
\]

The polynomial vector field is locally Lipschitz.  Bound (3.3) prevents
escape from every Euclidean ball in finite time, and the usual continuation
criterion proves global existence of (1.1).

With probability tending to one,

\[
 \mathcal E_n:=\{\|\theta(0)\|_2\le2n,\ \ell_n(0)\le2\} \tag{3.4}
\]

holds.  On \(\mathcal E_n\), (3.3) implies

\[
 \sup_{0\le t\le1}\|\theta(t)\|_2\le3n                \tag{3.5}
\]

for all sufficiently large \(n\).

## 4. Explicit polynomial envelope

Fix \(r>0\) and suppose \(\|\theta\|_2\le r\).  Since \(c\le1\),

\[
 \|H\|_2\le r^2,\qquad
 \|z\|_2\le {r^3\over\sqrt n},\qquad
 \|Y\|_2\le {r^6\over n},                              \tag{4.1}
\]

\[
 \|C\|_2\le {2r^4\over\sqrt n},\qquad
 \|b\|_2\le {2r^5\over n}.                             \tag{4.2}
\]

Equations (2.1)--(2.2) then give

\[
 |f_n(\theta)|\le {r^7\over n^2},\qquad
 \|g_n(\theta)\|_2\le {5r^6\over n},\qquad
 \|Df_n(\theta)\|_{\rm op}\le {5r^6\over n^2}.        \tag{4.3}
\]

The map \(g_n\) is a homogeneous polynomial of degree six.  For unit
vectors \(v,y\), the scalar polynomial

\[
 p(t)=\langle y,g_n(\theta+tv)\rangle
\]

has degree at most six.  On \(|t|\le r\), (4.3), used on the ball of
radius \(2r\), gives \(|p(t)|\le5(2r)^6/n\).  Markov's polynomial
inequality on \([-r,r]\) therefore gives

\[
 \|Dg_n(\theta)\|_{\rm op}
 \le {36\over r}{5(2r)^6\over n}
 ={11520r^5\over n}.                                    \tag{4.4}
\]

Put \(V_n=(1-f_n)g_n\).  From (4.3)--(4.4), on the ball \(r=4n\),

\[
 \|V_n\|_2\le4\cdot10^8 n^{10}=:M_n,                  \tag{4.5}
\]

\[
 \|DV_n\|_{\rm op}
 \le (1+|f_n|)\|Dg_n\|+\|g_n\|\|Df_n\|
 \le3\cdot10^{11}n^9=:K_n,                             \tag{4.6}
\]

and

\[
 \|Df_n\|_{\rm op}\le20480n^4=:D_n.                  \tag{4.7}
\]

All constants here are deterministic and have been rounded upward.

## 5. Euler--ODE comparison on the concentration layer

Let \(\Theta_n(t)\) solve (1.1), and let \(\bar\theta_n^h(t)\) be the
piecewise-linear parameter interpolation of (1.2).  As long as both paths
remain in the radius-\(4n\) ball, the exact one-step defect is bounded by

\[
 \left\|\Theta_n(t+h)-\Theta_n(t)-hV_n(\Theta_n(t))\right\|_2
 \le {1\over2}K_nM_nh^2.                                \tag{5.1}
\]

Indeed, write the defect as the double integral of
\(DV_n(\Theta_n(\cdot))V_n(\Theta_n(\cdot))\).  The usual discrete
Gronwall recursion gives, including linear interpolation,

\[
 \sup_{0\le t\le T_n}
 \|\bar\theta_n^h(t)-\Theta_n(t)\|_2
 \le2M_nh\exp(K_nT_n),                                  \tag{5.2}
\]

provided the right side is at most one.  This last condition closes the
radius-\(4n\) bootstrap using (3.5).

Take \(T_n=2/L_n\).  Equations (4.5)--(4.7) and (5.2) imply

\[
 \sup_{0\le t\le2/L_n}
 |f_n(\bar\theta_n^h(t))-f_n(\Theta_n(t))|
 \le 2\cdot10^{13}n^{14}h
 \exp\!\left({6\cdot10^{11}n^9\over L_n}\right).       \tag{5.3}
\]

Thus (1.3) makes the right side tend to zero.  Applying (5.3) at the
random ODE hitting time in (2.6)--(2.7) proves the predictor half of (1.4).
Because \(f_n(0)\to0\), after decreasing \(\delta_0\) once more if
needed,

\[
 \left|{1\over2}(1-f_n(0)-\delta_0)^2
       -{1\over2}(1-f_n(0))^2\right|\ge {\delta_0\over2} \tag{5.4}
\]

with probability tending to one.  Equation (5.3) and continuity of the
loss on the relevant bounded output interval prove the loss half of (1.4).

If uniform convergence to a continuous initialized readout held, evaluating
at \(\tau_n\to0\) would force the two differences in (1.4) to vanish.  This
contradiction completes the proof of Theorem 1.

## 6. The unresolved scaling window

The continuous concentration theorem reveals two natural scales, but does
not itself prove an Euler theorem at those scales.

* The pre-cap concentration layer has physical duration \(L_n^{-1}\).
* During the terminal one-leader release, the proof has

  \[
  X_j\le C\sqrt{nL_n},\qquad R_j\ge c_0X_j/L_n
  \]

  on the branch that reaches the terminal comparison scale before the
  fixed-action stop.  Hence that branch has a local relative rate at least
  of order \(\sqrt{n/L_n}\).  A stepwise resolution condition suggested by the
  exact update \(u_j^+=u_j(1+\text{const}\,hR_j)\) is

  \[
  h_n\sqrt{n/L_n}\longrightarrow0,
  \quad\text{i.e.}\quad
  h_n=o\!\left({(\log n)^{1/4}\over\sqrt n}\right).      \tag{6.1}
  \]

Condition (6.1) is a natural CFL scale, not a proved sufficient theorem.
The covariant-Schur proof deliberately avoids a full-state Hessian bound;
its moving-reciprocal and Schur cancellations would have to be rebuilt for
the discrete update before (6.1) could replace (1.3).

On the other side, the fixed-schedule Gaussian-program theorem is pointwise
in the number of steps.  It gives no concentration estimate uniform for
\(N_n\asymp T/h_n\).  Therefore the width-first initial-layer theorem also
cannot simply be applied on a joint diagonal.

The exact open bridge is consequently one of the following:

1. prove a discrete covariant-Schur theorem uniform under a stated mesh
   condition, ideally (6.1), which would extend the joint no-go; or
2. prove a growing-horizon finite-program theorem plus signed post-hit
   stability, which could identify an under-resolved diagonal limit.

Until one of these is supplied, there is no rigorous positive joint scaling,
but there is also no theorem excluding every possible under-resolved
diagonal.  Any such diagonal limit would be a discretization-selected
regularization; it would not be the width limit of the canonical finite-n
loss ODE, whose continuous initialized limit has already been ruled out.

## 7. Adversarial audit

1. **Limit order.**  The concentration theorem is applied to the actual
   finite-width ODE.  Euler comparison is then performed at the same width;
   no width/time interchange occurs.
2. **Normalization.**  Two uses of \(c x^2\) give exactly the factor \(c^3\)
   in both the output and its parameter gradient.
3. **Metric factor.**  Since \(g_n=n\nabla_E f_n\), the energy identity is
   \(\dot\ell_n=-\|\dot\theta\|_2^2/n\), not
   \(-\|\dot\theta\|_2^2\).
4. **Random hitting time.**  Estimate (5.3) is uniform on the whole stopped
   interval, so evaluating it at the random \(t_n\) is legitimate.
5. **Bootstrap.**  The ODE lies in radius \(3n\); (1.3) makes the Euler
   error less than one, keeping both paths in radius \(4n\).
6. **Claim boundary.**  The natural polynomial scale (6.1) is labelled
   conjectural.  The proved statement uses only (1.3).
7. **Endpoint limitation.**  A near-zero fixed loss change rules out
   compact-uniform continuous convergence.  It does not decide a terminal
   coarse/fine loss discrepancy after both meshes traverse the layer.
