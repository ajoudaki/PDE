# Coefficientwise local response bootstrap: independent audit

## Verdict and scope

The proposed coefficientwise bootstrap closes on a strictly positive
feature horizon independent of the Euler mesh and the middle clipping
threshold, conditional on the stated exact scalar Gaussian/response
representation. Its temporal ordering is acyclic. Its Gaussian
exponential estimate does not require independence across source times.

The result proved here is a uniform local bound for that finite-program
representation. The representation theorem, comparator stability,
removal of clipping, and identification with the prescribed finite
network remain separate proof steps. In particular the argument is
not a proof of all-horizon population well-posedness.

## Frozen-coefficient scalar system

Write \(a=\pi/2\), \(\phi=\arctan\), \(F(x)=x+x^3/3\), and
\(\chi=\phi\circ F^{-1}\), so
\[
 |\phi|\le a,\quad |\phi'|\le1,\quad |\phi''|\le2,\qquad
 |\chi|\le a,\quad |\chi'|\le1.
\]
Let \(\Delta>0\), \(S=M\Delta\le1\), and consider indices
\(0\le k\le M\). The finite scalar equations under audit are
\[
 X_{1,k}=F(Z_{1,0})+\Delta\sum_{r<k}q_{1,r},\qquad
 H_{1,k}=\chi(X_{1,k}),
\]
\[
 Z_{2,k}=\xi_{2,k}+\sum_{r<k}a_{2,kr}\delta_{2,r},
 \qquad H_{2,k}=\phi(Z_{2,k}),
\]
\[
 Z_{3,k}=\xi_{3,k}+\sum_{r<k}a_{3,kr}\delta_{3,r},
 \qquad H_{3,k}=\phi(Z_{3,k}),
\]
\[
 C_k=\Delta\sum_{r<k}H_{3,r},\qquad
 \delta_{3,k}=C_k\phi'(Z_{3,k}),
\]
\[
 q_{2,k}=\zeta_{2,k}+\sum_{v\le k}b_{3,kv}H_{2,v},\qquad
 \delta_{2,k}=\phi'(Z_{2,k})\tau_R(q_{2,k}),
\]
\[
 q_{1,k}=\zeta_{1,k}+\sum_{v\le k}b_{2,kv}H_{1,v}.
\]
Assume a differentiable clipping function satisfying
\[
 |\tau_R(x)|\le|x|,\qquad |\tau_R'(x)|\le1.
\]
The deterministic coefficients are
\[
 a_{\ell,ks}
 =\mathbb E\frac{\partial H_{\ell-1,k}}{\partial\zeta_{\ell-1,s}}
       +\Delta\,\mathbb E[H_{\ell-1,k}H_{\ell-1,s}],
 \qquad s<k,
\]
\[
 b_{\ell,ks}
 =\mathbb E\frac{\partial\delta_{\ell,k}}{\partial\xi_{\ell,s}}
       +\Delta\mathbf1_{\{s<k\}}
                         \mathbb E[\delta_{\ell,k}\delta_{\ell,s}],
 \qquad s\le k.
\]
All displayed source derivatives are formal derivatives of the scalar
program with its deterministic coefficients held fixed. They are not
derivatives of a covariance factorization. This convention is essential,
including when source covariance matrices are singular.

The four centered Gaussian source groups have covariance
\[
 \mathbb E[\xi_{\ell,k}\xi_{\ell,s}]
     =\mathbb E[H_{\ell-1,k}H_{\ell-1,s}],\qquad
 \mathbb E[\zeta_{\ell-1,k}\zeta_{\ell-1,s}]
     =\mathbb E[\delta_{\ell,k}\delta_{\ell,s}].
\]
Within each group arbitrary correlations across times are allowed.
The groups are independent as assumed in the representation theorem.

Define deterministic row sums
\[
 U_k=\sum_{s\le k}|b_{2,ks}|,\qquad
 V_k=\sum_{s\le k}|b_{3,ks}|.
\]
At \(k=0\), \(C_0=0\), both backward Gaussian variances are zero,
and \(U_0=V_0=0\).

## Bottom response: one factor of the source-time mesh

Suppose \(U_r\le1\) for every \(r<k\). Differentiating the bottom
recursion with respect to \(\zeta_{1,s}\) gives
\[
 \left|\frac{\partial X_{1,j}}{\partial\zeta_{1,s}}\right|
 \le\Delta\mathbf1_{\{s<j\}}
 +\Delta\sum_{r<j}\sum_{v\le r}|b_{2,rv}|
                   \left|\frac{\partial X_{1,v}}{\partial\zeta_{1,s}}\right|.
\]
Discrete Gronwall, also using \(|\chi'|\le1\), yields
\[
 \left|\frac{\partial H_{1,j}}{\partial\zeta_{1,s}}\right|
 \le\Delta e^S\quad(s<j\le k).
\]
Consequently, with the fixed constant
\[
 A=a^2+e,
\]
one has
\[
 |a_{2,js}|\le A\Delta\quad(s<j\le k).                   \tag{1}
\]
No size estimate on a realization of \(q_1\), and no derivative of a
Gaussian covariance, is used in this step.

## Middle response and its exponential envelope

Assume additionally \(V_r\le1\) for all \(r<k\). Put
\[
 \mathcal S_j=\sum_{s\le j}
       \left|\frac{\partial Z_{2,j}}{\partial\xi_{2,s}}\right|,
 \qquad
 \overline{\mathcal S}_j=\max_{v\le j}\mathcal S_v,
\]
\[
 E_j=\exp\left(A\Delta\sum_{r<j}(2|q_{2,r}|+V_r)\right).
\]
The source derivative of the clipped middle backward field satisfies
\[
 \left|\partial\delta_{2,r}\right|
 \le2|q_{2,r}|\,|\partial Z_{2,r}|
       +|\partial q_{2,r}|.
\]
For a derivative with respect to a \(\xi_2\) source,
\[
 |\partial q_{2,r}|
 \le\sum_{v\le r}|b_{3,rv}|\,|\partial Z_{2,v}|.
\]
Using (1), summing the absolute source derivatives, and applying
discrete Gronwall gives
\[
 \overline{\mathcal S}_j\le E_j\quad(j\le k).             \tag{2}
\]
For an individual \(\zeta_{2,s}\) derivative there is instead the
additional source term \(\mathbf1_{\{r=s\}}\). Its first effect on
\(Z_{2,j}\) carries \(a_{2,js}\), so the same argument gives
\[
 \left|\frac{\partial Z_{2,j}}{\partial\zeta_{2,s}}\right|
 \le A\Delta E_j,\qquad s<j\le k.                       \tag{3}
\]
There is no dependence on \(\zeta_{2,j}\) in \(Z_{2,j}\).

The envelope has uniform moments despite the unbounded Gaussian part
of \(q_2\). Indeed
\[
 |C_r|\le aS,\qquad |\delta_{3,r}|\le aS,
 \qquad \operatorname{Var}(\zeta_{2,r})\le a^2S^2,
\]
and
\[
 |q_{2,r}|\le|\zeta_{2,r}|+aV_r.
\]
If \(V_*=\max_{r<j}V_r\), Jensen's inequality over the finitely many
times, followed by the one-variable Gaussian exponential bound, gives,
for \(p\ge1\),
\[
 \begin{aligned}
 \mathbb E E_j^p
 &\le e^{pA(2a+1)SV_*}
       \mathbb E\exp\left(2pA\Delta\sum_{r<j}|\zeta_{2,r}|\right)\\
 &\le 2\exp\left(pA(2a+1)SV_*+2p^2A^2a^2S^4\right).
 \end{aligned}                                           \tag{4}
\]
For \(j=0\), \(E_0=1\) directly. For \(j>0\), the Jensen step is
\[
 \exp\left(2pA\Delta\sum_{r<j}|\zeta_{2,r}|\right)
 \le\frac1j\sum_{r<j}
              \exp(2pAj\Delta|\zeta_{2,r}|).
\]
Only the marginal variances of the Gaussian sources enter this
calculation. Neither their time independence nor independence of a
source from the bounded response shift is needed.

For explicit fixed constants, let
\[
 M_p=2^{1/p}\exp\left(A(2a+1)+2pA^2a^2\right).
\]
Under \(S,V_*\le1\), (4) implies \(\|E_j\|_p\le M_p\).
Equations (3) and the definition of \(a_3\) therefore give
\[
 |a_{3,js}|\le A_3\Delta,\qquad
 A_3=a^2+A M_1,\qquad s<j\le k.                         \tag{5}
\]

## Top response is bounded pointwise

Let
\[
 T_j=\sum_{s\le j}
       \left|\frac{\partial Z_{3,j}}{\partial\xi_{3,s}}\right|,
 \qquad \overline T_j=\max_{v\le j}T_v.
\]
Since \(C_j=\Delta\sum_{r<j}H_{3,r}\),
\[
 \sum_{s\le j}\left|
       \frac{\partial\delta_{3,j}}{\partial\xi_{3,s}}\right|
 \le\Delta\sum_{r<j}T_r+2aS T_j
 \le(1+2a)S\overline T_j.                               \tag{6}
\]
Together with (5), this implies the deterministic bound
\[
 \overline T_j\le\exp((1+2a)A_3S^2)\quad(j\le k).
\]
Taking expectations in (6) and adding the learned term gives
\[
 V_k\le(1+2a)S\exp((1+2a)A_3S^2)+a^2S^3
       \le C_3S,                                       \tag{7}
\]
where
\[
 C_3=(1+2a)\exp((1+2a)A_3)+a^2.
\]
In particular, the current row \(b_{3,k\cdot}\) is bounded before
estimating the current \(q_{2,k}\).

## Current middle backward field and bottom response

Equation (7) gives
\[
 \|q_{2,k}\|_2\le aS+aV_k\le QS,\qquad Q=a(1+C_3).
                                                               \tag{8}
\]
Here \(\|\cdot\|_2\) denotes the scalar probability-space \(L^2\) norm,
not a finite-width norm. The same bound holds at earlier indices under
the same bootstrap argument.

Differentiating the current middle backward field with respect to the
\(\xi_2\) source row and using (2) gives
\[
 \sum_{s\le k}
  \left|\frac{\partial\delta_{2,k}}{\partial\xi_{2,s}}\right|
 \le(2|q_{2,k}|+V_k)\overline{\mathcal S}_k.
\]
Cauchy--Schwarz and (4), (7), (8) yield
\[
 \begin{aligned}
 U_k
 &\le(2\|q_{2,k}\|_2+V_k)
                      \|\overline{\mathcal S}_k\|_2
       +S\max_{r\le k}\|\delta_{2,r}\|_2^2\\
 &\le[(2Q+C_3)M_2+Q^2]\,S=:C_2S.                      \tag{9}
 \end{aligned}
\]
In the last line \(S\le1\) and
\(\|\delta_{2,r}\|_2\le\|q_{2,r}\|_2\le QS\) were used.
There is no circular use of \(U_k\) in either (7) or (9).

## First-exit closure and source dependencies

Choose the explicit positive horizon
\[
 S_0=\min\left\{1,\frac1{2C_2},\frac1{2C_3}\right\}.
\]
Fix any \(S=M\Delta\le S_0\). If \(k\) were the first index at which
\(U_k>1\) or \(V_k>1\), all earlier rows satisfy the bootstrap
hypotheses. The estimates above give
\[
 V_k\le C_3S\le\frac12,\qquad
 U_k\le C_2S\le\frac12,
\]
a contradiction. For use of the earlier-index bound in (9), apply
(7)--(8) at each \(r\le k\); their premises involve only rows strictly
earlier than \(r\). Equivalently, induct simultaneously on the sharper
conclusions \(U_r\le C_2S\), \(V_r\le C_3S\).

The causal order for the current index is
\[
 a_{2,k\cdot}\ \longrightarrow\ H_{2,k}\
 \longrightarrow\ a_{3,k\cdot}\ \longrightarrow\
 \delta_{3,k}\ \longrightarrow\ b_{3,k\cdot}\
 \longrightarrow\ q_{2,k},\delta_{2,k}\
 \longrightarrow\ b_{2,k\cdot}.
\]
More explicitly:

- \(H_{1,k}\) uses only bottom response rows with time \(<k\).
- \(H_{2,k}\) uses only middle backward fields at times \(<k\).
- The derivative of \(H_{2,k}\) with respect to a past \(\zeta_2\)
  source consequently uses only \(b_3\) rows with time \(<k\).
- The top scalar recursion uses only its own \(\xi_3\) source group
  once its deterministic \(a_3\) row is fixed.
- The current \(b_3\) row determines the bounded shift of
  \(q_{2,k}\), after which the current \(b_2\) row is estimated.

Thus differentiating the explicit scalar program under the stated
frozen-coefficient convention introduces no omitted cross-source term.
If a different convention differentiates the deterministic coefficient
selection or a covariance square root, this audit does not apply to
that different derivative.

## Uniform local tail actually obtained

The closure gives, uniformly in \(k\le M\), \(M\), \(\Delta\), and \(R\),
\[
 q_{2,k}=\zeta_{2,k}+\beta_{2,k},\qquad
 \operatorname{Var}(\zeta_{2,k})\le a^2S^2,\qquad
 |\beta_{2,k}|\le aC_3S.
\]
The shift may depend on the Gaussian source; its deterministic amplitude
bound suffices. For \(x>0\),
\[
 \mathbb P\bigl(|q_{2,k}|>aC_3S+x\bigr)
 \le2\exp\left(-\frac{x^2}{2a^2S^2}\right).              \tag{10}
\]
Consequently \(\|q_{2,k}\|_p\le C S\sqrt p\) for \(p\ge2\), with
a constant independent of mesh and clipping. The same conclusion
holds for \(\delta_{2,k}\), since clipping and the gate do not increase
its absolute value.

This estimate is obtained on \(S\le S_0\). The constants above are
deliberately conservative; no claim is made that \(S_0\) contains the
full optimization feature horizon.

## Implementation of the comparison still to distinguish

The displayed bottom update is Euler in \(X_1=F(z^{(1)})\):
\[
 X_{1,k+1}=X_{1,k}+\Delta q_{1,k}.
\]
It is not exactly the map obtained by applying \(F\) after one ordinary
Euler step in \(z^{(1)}\). It is a valid discretization of the same
continuous transformed equation, and its scalar finite-program
response representation must be justified for that discretization.
This distinction does not alter any estimate above, but it matters
when stating which finite algorithm has been identified.
