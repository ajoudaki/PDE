# Audit: invariant Gaussian projection and the causal reachable frame

## Verdict

The tensor-program transpose predictor is the covariance-isometric transfer
of a Gaussian first-chaos projection.  It is exactly an \(L^2\) isometry and
is not an \(L^p\), BMO, or Orlicz contraction.  A bounded-arctan two-history
example makes the transferred predictor converge to cubic Gaussian chaos,
so no theorem based only on bounded histories and Bessel energy can work.

The actual Euler ordering is better than that generic example.  Exact divided
differences make each new feature direction carry the Euler increment, and
the first \(k=0\to1\) reachable innovation is sub-Gaussian.  The static
predictor obeys an exact causal recursion.  Its first unresolved term is a
specific projected raw-bulk velocity, not an abstract covariance inverse.

## 1. Coordinate-free predictor

For histories \(X=(X_2^0,\ldots,X_2^k)\), let
\(C=\mathbb E[XX^{\mathsf T}]\), and let \(H\sim N(0,C)\) be the associated
forward Gaussian history.  For a row variable \(B\), put

\[
 a=\mathbb E[HB],\qquad c=C^+a.
\]

Gaussian Stein shows that this agrees, modulo \(\ker C\), with the expected
derivative coefficients.  If \(\Pi_1\) is first-chaos projection and

\[
 U_X(c^{\mathsf T}H)=c^{\mathsf T}X,
\]

then the predictable static transpose term is

\[
 P_{\rm stat}=U_X\Pi_1B.
\]

This representation is invariant under redundant histories and singular
Gram matrices.  It has only the exact estimate

\[
 \|U_X(c^{\mathsf T}H)\|_2^2=c^{\mathsf T}Cc
 =\|c^{\mathsf T}H\|_2^2,
 \qquad \|P_{\rm stat}\|_2\le\|B\|_2.
\]

## 2. Exact generic counterexample

Let \(G\sim N(0,1)\), \({\rm He}_3(G)=G^3-3G\), and
\(V=(1+G^2){\rm He}_3(G)\).  Set

\[
 X^0=\arctan G,
 \qquad X_\varepsilon^1=\arctan(G+\varepsilon V).
\]

After subtracting the projection onto \(X^0\), write the residual as
\(\Delta_\varepsilon\) and normalize it by
\(\sigma_\varepsilon=\|\Delta_\varepsilon\|_2\).  The integral mean-value
formula gives

\[
 {\Delta_\varepsilon\over\sigma_\varepsilon}
 \longrightarrow
 {J\over\|J\|_2},
 \qquad
 J={\rm He}_3(G)-a\arctan G.
\]

The bounded subtraction does not change the cubic tail, so \(J\) has no
exponential moment.  Let \(q_\varepsilon\) be the normalized Gaussian
innovation paired with this residual and take

\[
 B_\varepsilon=A_0+\arctan q_\varepsilon,
 \qquad A_0\sim N(0,1)\text{ independent}.
\]

Although \(|B_\varepsilon|\le|A_0|+\pi/2\), Stein gives

\[
 P_\varepsilon
 =\beta{\Delta_\varepsilon\over\sigma_\varepsilon},
 \qquad
 \beta=\mathbb E(1+Z^2)^{-1}>0.
\]

Hence \(\sup_\varepsilon\|P_\varepsilon\|_{\psi_1}=\infty\).  The same
construction is realized by an iid Gaussian matrix, and its predictor is
the exact Gaussian-divergence compensator.  Thus independent Gaussian marks,
bounded nonlinearities, singular-covariance invariance, and first-chaos
energy do not imply the target.  The missing property is the frame bound
restricted to directions reachable by the training dynamics.

## 3. Exact Euler divided differences

Write \(D\phi,Dd,D\iota\) for divided differences.  With
\(\rho_\ell^k=\langle X_\ell^k,X_\ell^{k+1}\rangle\), define

\[
 V_1^k=D\phi(u^k,u^{k+1})D\iota(r^k,r^{k+1})Q_1^k,
\]

\[
 W_2^k=(\Gamma_1+P_1^k)V_1^k+\rho_1^kB_2^k,
 \qquad V_2^k=D\phi(Z_2^k,Z_2^{k+1})W_2^k,
\]

\[
 W_3^k=(\Gamma_2+P_2^k)V_2^k+\rho_2^kB_3^k.
\]

The rank-one Euler updates give, without a remainder,

\[
 \Delta X_1=hV_1,quad \Delta Z_2=hW_2,quad
 \Delta X_2=hV_2,quad \Delta Z_3=hW_3.
\]

Since \(A^{k+1}=A^k+hX_3^k\),

\[
 B_3^{k+1}-B_3^k=hF_3^k,
\]

where

\[
 F_3^k=X_3^kd(Z_3^{k+1})
 +A^kDd(Z_3^k,Z_3^{k+1})W_3^k.                 \tag{3.1}
\]

Let \(\mathcal T_k=U_k\Pi_{1,k}\).  Generation-order freshness means that
the old \(B_3^k\) has zero coefficient in the new formal Gaussian
innovation, so

\[
 \boxed{
 P_{\rm stat}^{k+1}=P_{\rm stat}^k
 +h\,\mathcal T_{k+1}F_3^k.}                         \tag{3.2}
\]

The \(k+1\) index is essential because (3.1) uses \(Z_3^{k+1}\).  A bound

\[
 \|\mathcal T_{k+1}F_3^k\|_{\psi_1}
 \le C_T\{1+\text{past predictor norms}\}
\]

would close directly by discrete Gronwall and would never require raw
coefficient total variation.

## 4. The first reachable innovation is safe

At zero learned initialization, centered \(A_0\) makes the initial
second-bulk predictor vanish, so \(R_2^0\) is fresh Gaussian.  The same
argument at the first bulk makes \(Q_1^0\) fresh Gaussian.  Since
\(\phi\circ\iota\) is globally Lipschitz,

\[
 |V_1^0|le \operatorname{Lip}(\phi\circ\iota)|Q_1^0|,
\]

and the forward-after-transpose Gaussian identity expresses
\(\Gamma_1V_1^0\) as a fresh Gaussian plus a bounded scalar multiple of
\(B_2^0\).  Therefore \(W_2^0,V_2^0\in\psi_2\).

The new residual satisfies exactly

\[
 (I-\operatorname{Proj}_{X_2^0})X_2^1
 =h(I-\operatorname{Proj}_{X_2^0})V_2^0,
\]

so it is \(O(h)\) in \(\psi_2\), not cubic chaos.  Stein differentiation in
its normalized new Gaussian direction produces a coefficient of order its
standard deviation; after synthesis the \(1/h\) normalization cancels and
the contribution remains \(O(h)\) in \(\psi_2\).  Thus the generic
two-history counterexample is not reachable at the first Euler step.

## 5. First exact open leaf

Substituting (3.1) into (3.2), the first term not controlled by the proven
facts is

\[
 \boxed{
 \mathcal T_{k+1}\!\left[
 A^kDd(Z_3^k,Z_3^{k+1})(\Gamma_2+P_2^k)V_2^k
 \right].}                                            \tag{5.1}
\]

The Gaussian \(A_0\) envelope and the divided difference remove the raw
amplitude maximum and the explicit \(1/h\), respectively.  They do not make
\(\mathcal T\) an Orlicz contraction.  In Gram--Schmidt form the new paired
history is

\[
 h(I-\operatorname{Proj}_{\rm past})V_2^k.
\]

The unresolved theorem is therefore a mesh-uniform reachable-frame estimate
for (5.1), coupled to the analogous first-bulk term.  A formal third temporal
difference contains \(\phi'''(Z_2)(\dot Z_2)^3\), but whether its regression
coefficient carries enough time-increment powers to suppress the cubic tail
is not decided by Bessel or envelope estimates.
