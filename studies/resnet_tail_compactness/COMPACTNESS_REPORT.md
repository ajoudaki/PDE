# Final bounded round: Hermite compactness versus flow amplification

**Date:** 25 July 2026  
**Model:** canonical dense Euclidean \(\mu\)P residual-\(\tanh\) benchmark  
**Budget:** one coupled positive-time run; 211.0 seconds wall time  
**Question:** Can the last finite-\(P\) convergence gap be closed, or at
least reduced to one uniquely identified obstruction?

## Executive verdict

This round gives a decisive **mechanism diagnosis**, but it does not prove
arbitrary-accuracy convergence.

The preceding report left two coupled possibilities:

1. higher Hermite shells inject a tail that is not yet compact;
2. a nonnormal, cutoff-dependent flow amplifies even a small shell defect.

The new coupled degree-\(3,5,7\) experiment gives a realized-direction
diagnostic of this split. At \(t=0.25\),

\[
\frac{\text{effective degree-7 shadow gain}}
     {\text{effective degree-5 shadow gain}}
=0.99862.
\]

At this one seed, resolution, horizon, and realized forcing direction, no
large difference between the two final-time effective quotients was
detected. This is not a worst-case propagator bound. The theorem-facing
Cauchy errors did not contract:

\[
\frac{E_{5\to7}^{\rm state}}{E_{3\to5}^{\rm state}}
=1.32193,
\qquad
\frac{E_{5\to7}^{\rm obs}}{E_{3\to5}^{\rm obs}}
=1.63581.
\]

The same ratios were \(1.32306\) and \(1.63414\) at the only earlier
checkpoint, \(t=0.125\). Thus the two measured checkpoints give the same
finite-level ordering:

> The aggregate shell forcing and actual Cauchy gaps remain noncontracting.
> The available final-time secant quotients show no large cutoff difference
> for this realized direction, but do not certify cutoff-uniform stability.

The theory audit also removes one formerly separate assumption. The frozen
shared-transpose operator is a bounded Hilbert adjoint, so a
Malliavin-gradient tail estimate is **not necessary merely to define or
control the transpose on a compact trajectory**. However, this bounded
operator is not compact, and the natural \(L^2\) vector field is not locally
Lipschitz on \(L^2\) balls because the adjoint contains an unbounded Gaussian
boundary coordinate. Energy bounds therefore do not create tail compactness
by themselves.

The final finite-\(P\) status is:

\[
\boxed{\text{No large realized-direction gain change was detected at
degrees 5 and 7.}}
\]

\[
\boxed{\text{A separate Malliavin-tail assumption is unnecessary for
boundedness and fixed-compact-trajectory consistency.}}
\]

\[
\boxed{\text{Collective strong Hermite-tail compactness remains unproved
and is adverse at the last observed rung.}}
\]

Consequently, it would be incorrect to claim that the pure-Hermite
arbitrary-accuracy theorem is now settled. The round has isolated one
remaining analytic obstruction, not eliminated it.

## 1. The sharper analytic formulation

### 1.1 Keep the two Gaussian roles distinct

Let \(\eta\) denote the source-neuron label and let

\[
H=L^2(\mu_\eta).
\]

Let \(\theta\) denote the target-row label and let \(\omega\) carry a common
isonormal process \(W:H\to L^2(\Omega)\). Define

\[
\mathcal R=L^2(\mu_\theta\otimes\mathbb P_\omega).
\]

For \(u\in H\), set

\[
(Iu)(\theta,\omega)=W_\omega(u).
\]

Take \(W\) to be the standard unit-covariance isonormal process. Then
\(I:H\to\mathcal R\) is an isometry. The physical frozen row carries the
external factor \(\sigma_w\). The Hilbert adjoint \(T_W=I^\ast\) is defined
by

\[
\langle T_W\beta,u\rangle_H
=
\mathbb E_{\theta,\omega}\!\left[\beta(\theta,\omega)W_\omega(u)\right],
\]

and satisfies

\[
\|T_W\beta\|_H\le \|\beta\|_{\mathcal R}.
\]

In Hermite coordinates,

\[
T_W\beta
=
\sum_\nu\phi_\nu\,
\mathbb E[\epsilon_\nu\beta].
\]

This is Bessel's inequality/Riesz representation. Gaussian integration by
parts can identify the same coefficients with expected Malliavin
derivatives when that regularity exists, but Malliavin differentiability is
not needed for boundedness of the transpose.

For the learned row \(c\in\mathcal R(H)\), define

\[
(R_cu)(\theta,\omega)=\langle c(\theta,\omega),u\rangle_H.
\]

Then

\[
R_c^\ast\beta=T_c\beta
=\mathbb E_{\theta,\omega}[c\,\beta],
\]

with

\[
\|T_c\beta\|_H
\le
\|c\|_{\mathcal R(H)}\|\beta\|_{\mathcal R}.
\]

Hence the total row and transpose,

\[
A_c=\sigma_w I+R_c,
\qquad
A_c^\ast=\sigma_wT_W+T_c,
\]

are bounded by \(\sigma_w+\|c\|_{\mathcal R(H)}\).

### 1.2 Exact match to the finite operator PDE

For the orthogonal Hermite projection \(P_K\), the finite PDE uses

\[
A_{c,K}=A_cP_K,
\qquad
A_{c,K}^\ast
=P_K\sigma_wT_W+T_c,
\quad c\in H_K.
\]

This is exactly the ideal algebra implemented by:

- `hcoef = P_K h`;
- `row = sigma_w * epsilon + c`;
- `transpose_coeff = E[row * beta]`;
- \(\dot c=-\gamma\sum_qe_q\beta_qP_Kh_q\).

Only the operator/source coordinate is truncated. The slow fields
\(B,a,h,p\) are not Hermite-projected. A common \(\omega\) is a coupling of
the local conditional laws, not a claim of physical correlation between
different continuous-depth locations.

### 1.3 What the energy identity gives

In the Lagrangian characteristic metric

\[
X
=
H^d\times H
\times L^2\!\left(
[0,1]\times\mu_\theta\times\mathbb P_\omega;H
\right),
\]

the finite cutoff system has

\[
-\dot{\mathcal L}_K
=
\|\dot B_K\|_H^2
+\|\dot a_K\|_H^2
+\int_0^1\|\dot c_K(s)\|_{\mathcal R(H)}^2\,ds.
\]

Therefore, for every fixed \(T\),

\[
\|Y_K(t)\|_X
\le
\|Y_K(0)\|_X+\sqrt{T\mathcal L(0)},
\]

and

\[
\|Y_K(t)-Y_K(s)\|_X
\le
\sqrt{|t-s|\mathcal L(0)}.
\]

These bounds are independent of \(K\). They give finite-time state bounds
and time equicontinuity for the smooth finite systems.

## 2. The analytic obstruction that remains

### 2.1 Bounded does not mean compact

The Riesz step removes the need for Malliavin differentiability to define
the transpose and prove consistency on a fixed compact trajectory. It does
not make \(T_W\) compact or prove collective compactness of the trained
cutoff family. Let

\[
\beta_\nu(\theta,\omega)=\epsilon_\nu(\omega).
\]

Then \(\{\beta_\nu\}\) is orthonormal in \(\mathcal R\), while

\[
T_W\beta_\nu=\phi_\nu.
\]

Consequently,

\[
\sup_{\|\beta\|_{\mathcal R}\le1}
\|(I-P_K)T_W\beta\|_H=1
\]

for every finite \(K\). Strong projection convergence is uniform on compact
sets, not on the energy-bounded ball.

### 2.2 Plain \(L^2\) local Lipschitzness is false

The problematic nonlinear map is

\[
(z,p)\longmapsto \tanh'(z)p.
\]

For two states,

\[
\delta\beta
=
\delta p\,\tanh'(z)
+\widetilde p\,
[\tanh'(z)-\tanh'(\widetilde z)].
\]

The second term contains \(\widetilde p\,\delta z\). On an \(L^2\) ball the
two factors are only \(L^2\), so their product is generally only \(L^1\).
The issue is present at initialization because

\[
p(1,\theta)=a(\theta)=A\theta_4
\]

is an unbounded Gaussian coordinate. Perturbations concentrated where
\(|a|\) is large make the local multiplier norm arbitrarily large.

Thus the proposed cutoff-independent \(L^2\)-Lipschitz proof is invalid.
The energy identity supplies boundedness, but not the stronger reachable
regularity required for stability and compactness.

### 2.3 Strongest rigorous compact-time reduction

Two valid routes remain.

**Compactness route.** If

\[
\{Y_K(t):K\ge1,\ 0\le t\le T\}
\]

is relatively compact in \(X\), and the limiting Hilbert Cauchy problem is
unique, then the energy equicontinuity, compact-set consistency, and
Arzelà--Ascoli imply

\[
Y_K\longrightarrow Y
\quad\text{in }C([0,T];X).
\]

**Forced-stability route.** If an infinite solution exists and projected
flows have a cutoff-uniform forced gain \(G_T\), then

\[
\sup_{t\le T}\|Y_K(t)-P_KY(t)\|_X
\le
G_T
\int_0^T
\|F_K(P_KY)-P_KF(Y)\|_X\,dt.
\]

Compactness of the fixed limiting trajectory makes the right-hand
consistency defect vanish.

The remaining proof obligation is therefore not necessarily “estimate a
separate Malliavin tail,” although Malliavin/source regularity remains one
possible sufficient route. It is:

> Propagate a source-mode-coercive reachable regularity class with explicit
> tail weights and compact embedding in \(X\), or directly prove collective
> strong tail tightness and uniqueness, together with a cutoff-uniform
> forced-stability modulus.

Generic Gaussian-Sobolev or Orlicz boundedness without coercive source-mode
weights is not enough: on an infinite-dimensional Gaussian space,
coordinate functions can remain orthogonal while sharing such unweighted
bounds.

## 3. The one bounded experiment

### 3.1 Design

The run co-evolved the active odd Hermite systems

\[
24\to80\to200,
\]

corresponding to complete odd degrees

\[
3\to5\to7.
\]

All systems used literal prefixes of the same parity-paired quadrature.

| item | value |
|---|---:|
| depth nodes \(N\) | 1 |
| tensor base order | 8 |
| base points \(M\) | 4096 |
| fast points \(R\) | 512 |
| time step | 0.025 |
| integrator | explicit midpoint |
| checkpoints | 0.125, 0.25 |
| cubature seed | 20260723 |
| wall time | 211.0 s |

For adjacent levels \(K<J\), it measured:

\[
H_{K,J}(t)=\|(I-P_K)Y_J(t)\|_X,
\]

\[
S_{K,J}(t)=\|P_KY_J(t)-Y_K(t)\|_X,
\]

\[
C_{K,J}(t)
=
\|P_KF_J(Y_J(t))-F_K(P_KY_J(t))\|_X,
\]

and the actual normalized output/Gram gap \(O_{K,J}(t)\).

The projective state error is

\[
E_{K,J}(t)=\sqrt{H_{K,J}(t)^2+S_{K,J}(t)^2}.
\]

With the exact zero initial defect, a two-checkpoint trapezoid approximated

\[
L_{K,J}=\int_0^{0.25}C_{K,J}(t)\,dt,
\]

and the directional final-time effective quotient was

\[
G^{\rm eff}_{K,J}=\frac{S_{K,J}(0.25)}{L_{K,J}}.
\]

This is an actual-tail final-time secant quotient, not a tangent-propagator
norm. Its denominator uses only \(t=0,0.125,0.25\), so the small difference
between the two quotients has no numerical error certificate.

### 3.2 Time-resolved result

| time | metric | degree \(3\to5\) | degree \(5\to7\) | upper/lower |
|---:|---|---:|---:|---:|
| 0.125 | outgoing state tail \(H\) | \(9.2131\times10^{-6}\) | \(1.1679\times10^{-5}\) | 1.2676 |
| 0.125 | low-state shadow \(S\) | \(4.4521\times10^{-4}\) | \(5.8905\times10^{-4}\) | 1.3231 |
| 0.125 | projective error \(E\) | \(4.4531\times10^{-4}\) | \(5.8917\times10^{-4}\) | 1.3231 |
| 0.125 | observable gap \(O\) | \(4.7983\times10^{-6}\) | \(7.8411\times10^{-6}\) | 1.6341 |
| 0.125 | feedback \(C\) | \(5.9976\times10^{-3}\) | \(7.9331\times10^{-3}\) | 1.3227 |
| 0.250 | outgoing state tail \(H\) | \(4.7710\times10^{-5}\) | \(6.0433\times10^{-5}\) | 1.2667 |
| 0.250 | low-state shadow \(S\) | \(1.3107\times10^{-3}\) | \(1.7328\times10^{-3}\) | 1.3220 |
| 0.250 | projective error \(E\) | \(1.3116\times10^{-3}\) | \(1.7338\times10^{-3}\) | 1.3219 |
| 0.250 | observable gap \(O\) | \(2.1913\times10^{-5}\) | \(3.5846\times10^{-5}\) | 1.6358 |
| 0.250 | feedback \(C\) | \(7.2584\times10^{-3}\) | \(9.6224\times10^{-3}\) | 1.3257 |

The integrated ledger is:

| adjacent rung | \(\int C\,dt\) | final \(S\) | \(G^{\rm eff}=S/\int C\) |
|---|---:|---:|---:|
| degree \(3\to5\) | \(1.20335\times10^{-3}\) | \(1.31070\times10^{-3}\) | 1.08921 |
| degree \(5\to7\) | \(1.59303\times10^{-3}\) | \(1.73275\times10^{-3}\) | 1.08771 |

Thus

\[
\frac{G^{\rm eff}_{5\to7}}{G^{\rm eff}_{3\to5}}
=0.99862.
\]

The observable gaps are absolutely small: \(2.19\times10^{-5}\) and
\(3.58\times10^{-5}\) of the fixed project metric, or about
\(0.0022\%\) and \(0.0036\%\). That supports practical low-order accuracy,
but their ordering is adverse for an arbitrary-accuracy convergence claim.

The final low-state shadow is dominated by the trained input map \(B\):

| rung | \(B\) shadow | \(a\) shadow | \(c\) shadow |
|---|---:|---:|---:|
| degree \(3\to5\) | \(1.30914\times10^{-3}\) | \(5.97561\times10^{-5}\) | \(2.29150\times10^{-5}\) |
| degree \(5\to7\) | \(1.73090\times10^{-3}\) | \(7.55931\times10^{-5}\) | \(2.63438\times10^{-5}\) |

This confirms that the high-to-low defect is not confined to an unused
learned coefficient. It propagates into a genuine slow state coordinate,
but without an increasing gain.

## 4. What this round settled

| question | result |
|---|---|
| Is Malliavin differentiability needed to define the frozen transpose or obtain consistency on a fixed compact trajectory? | **No.** The Riesz adjoint gives the correct bounded operator directly. It does not prove collective compactness. |
| Does the energy identity give cutoff-uniform finite-time state bounds and time equicontinuity? | **Yes.** |
| Does energy-boundedness imply Hermite compactness? | **No.** The frozen transpose is bounded but noncompact. |
| Is the plain \(L^2\) flow uniformly locally Lipschitz? | **No.** The unbounded Gaussian adjoint boundary gives a concrete multiplier obstruction. |
| Is there a large cutoff change in the realized final-time directional quotient at this seed and resolution? | **No detected large change.** The quotient ratio is 0.9986, without an error bar; this is not a uniform stability proof. |
| Do actual state and observable Cauchy increments contract by degree seven? | **No.** They grow by \(1.322\times\) and \(1.636\times\). |
| Is compact-time pure-Hermite convergence proved? | **No.** Collective tail compactness/strong reachable regularity remains. |
| Is the full all-time dense-network PDE conjecture proved? | **No.** Dense-limit identification, trained-depth homogenization, and all-time control are separate obligations. |

## 5. Final scientific conclusion

This round rejects the most convenient affirmative story: the actual Cauchy
increments have not turned over by degree seven. The higher shell creates
approximately \(32\%\) more projective state error. At one seed,
\(N=1\), one \(M/R/\Delta t\), and \(t\le0.25\), its realized final-time
secant quotient is close to the preceding one; this does not rule out
cutoff-dependent amplification in other directions, later times, higher
degrees, or the continuum-depth limit.

At the same time, it improves the mathematics by removing an overstrong
Malliavin-tail requirement and replacing the old seven-condition lemma with
a sharper compactness/stability theorem.

The most accurate final statement is:

> The pure-Hermite finite-\(P\) hierarchy remains a plausible practical
> low-order approximation, but its arbitrary-accuracy convergence is not
> presently supported by an observed Cauchy trend. The remaining
> compact-time analytic bundle is collective source-Hermite tail
> compactness/strong reachable regularity, uniqueness, and cutoff-uniform
> forced stability. This run detected no large gain change for one realized
> direction; it did not prove the stability clause.

No additional scientific run was launched after this result.

## 6. Provenance

- protocol SHA-256:
  `8b3f6a9ce80575f675454a5ebff63c33e347b28d33a77e0442a4385209eda1fd`
- runner SHA-256:
  `a12715d02987b0bbb7380e5f7ae35f1a673d58e01a930eefcdaeca8636f96085`
- result SHA-256:
  `fc5a88c0e65f6142ae202bc5d96f5049616fc8ecaf944c4ef5fee71d30dddc40`
