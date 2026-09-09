# Isolated Gaussian-channel design 01

**Provenance:** clean-slate subagent “independent_dynamic_gaussian”, given
only the canonical equations and metric clarification; instructed not to
inspect the project.  
**Date:** 2026-08-24  
**Audit status:** alternate design evidence, not a promoted theorem

## Verdict

This agent independently proposed a one-time marked Gaussian-channel
operator equation. It recovered exact finite algebra, a rigorous fixed-grid
conditional-Gaussian mechanism, and compact-time norm bounds. It also
stopped before claiming the depth-three arctangent theorem: a
mesh-uniform two-channel first/second susceptibility estimate remained
unproved.

## Gaussian channel primitive

If one frozen Gaussian matrix has answered right queries \(V\) and left
queries \(W\), with \(Y=GV\) and \(Z=G^*W\), its exact finite-dimensional
conditional law is

\[
 G\mid(Y,Z)
 =M+P_W^\perp\widetilde G P_V^\perp,                  \tag{1}
\]

where

\[
 M=Y(V^*V)^+V^*+
 W(W^*W)^+Z^*P_V^\perp.                               \tag{2}
\]

Compatibility \(W^*Y=Z^*V\) makes this satisfy both query families.
Degenerate histories are handled on the quotient by zero-norm query
directions, not by assuming a uniformly invertible Gram matrix.

For a fixed Euler grid, exact rank-update elimination leaves a finite
sequence of coordinate maps, empirical contractions, and forward/transpose
queries to the initial Gaussian matrices. This is rigorously covered by the
fixed-program theorem audited separately. No grid-uniform conclusion
follows from (1)--(2).

## Acceptable final operator state

The proposed current equation is

\[
\begin{aligned}
 H_1&=U,&X_\ell&=\phi(H_\ell),&
 H_\ell&=\mathsf G_\ell X_{\ell-1},\\
 B_H&=A\phi'(H_H),&
 B_\ell&=\phi'(H_\ell)\mathsf G_{\ell+1}^*B_{\ell+1},
\end{aligned}
\]

\[
 \dot A=X_H,\qquad \dot U=B_1,\qquad
 \dot{\mathsf G}_\ell=B_\ell\otimes X_{\ell-1}.        \tag{3}
\]

Together with the immutable Gaussian-channel marking, (3) is a one-time
operator equation. In the RCGC contract it is represented more concretely
as \(\mathsf G_\ell=\Gamma_\ell+P_\ell\) with current trace-class
\(P_\ell\). The covariance/response Volterra chart is proof scaffolding,
not the final state.

## Depth-three bounds already obtained

For arctangent, \(M=\pi/2\),
\(a_2=\|A\|_n\), and
\(\gamma_\ell=\|G_\ell\|_{\rm op}\),

\[
\begin{aligned}
 a_2(s)&\le a_2(0)+Ms,\\
 \sqrt{r_3}&\le a_2,\quad
 \sqrt{r_2}\le\gamma_3a_2,\quad
 \sqrt{r_1}\le\gamma_2\gamma_3a_2,\\
 \gamma_3(s)&\le\gamma_3(0)+M\int_0^sa_2(r)\,dr,\\
 \gamma_2(s)&\le\gamma_2(0)+M\int_0^s\gamma_3(r)a_2(r)\,dr.
\end{aligned}                                         \tag{4}
\]

These establish finite-width nonexplosion, tight operator/state bounds, and
equi-Lipschitzness of the predictor. They do not give the required modulus
or uniform integrability for the middle backward field and raw kernel.

## Proposed missing theorem

For a grid \(\Pi\), let \(\mathcal D_\Pi^{(r)}Z\), \(r=1,2\), be correctly
rescaled typed source variations. The proposed certificate is: for some
\(p>4\) and every compact \(S\),

\[
 \sup_{\Pi,n}\sup_{t\le S}
 \mathbb E\|\mathcal D_\Pi^{(r)}Z(t)\|_{p,n}^p
 \le C_{S,p},\qquad r=1,2,                             \tag{5}
\]

for every forward, backward, and parameter field, plus a grid-uniform time
translation modulus.

The proposed proof expands coloured causal response trees. Simplex volume
gives \(S^m/m!\), while arctangent derivatives are bounded. Chains are
summable, but branching second variations create correlated mixed products.
The agent did not prove that the needed Orlicz/moment class survives
restart after alternating through both Gaussian channels.

## Claim boundary

Accepted:

- exact finite dynamics and rank-update elimination;
- fixed-grid Gaussian-channel semantics;
- current operator equation (3) as the formal autonomous target; and
- the a-priori bounds (4).

Open:

- whether (5) is sufficient without higher/all-order response control;
- the mixed-tail restart estimate;
- uniqueness/stability of the associated proof chart; and
- compact-time convergence of raw \(K_n\).

The isolated report therefore supports a concrete calculus direction but
does not pass the depth-three gate.

