# Adversarial audit of the unconditional depth--time theorem

## Verdict: PASS

The unconditional theorem obtained from `WIDTH_DEPTH_TIME.md` and
`COMPILER_DEPTH_TIME.md` is valid for every fixed finite pair
\((L,t)\).  This verdict concerns the exact-compiler coefficient

\[
 \kappa^{\rm cmp}_{\phi,L,t}
 =\frac{8\mathcal J^{\rm cmp}_{3,t,L}
       -\mathcal J^{\rm cmp}_{3,2t,L}}6,
\]

and does **not** use the compact coefficient, the nine-moment recursion,
or any statement in `CUBIC_DEPTH_TIME.md`.

Precisely, if

\[
 \phi\in C^{12},\qquad \mathbb E\phi(G)^2=1,
\]

and

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty,
 \qquad B_\phi=\max\{4,M_\phi\},
\]

then the actual width-first outputs satisfy

\[
 \left|F_{t,L}(2\eta)-F_{2t,L}(\eta)
 -\kappa^{\rm cmp}_{\phi,L,t}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le\frac12,
\]

where the terminating integer recursion defining \(E_{L,N}\) is
(5.1)--(5.5), (5.11)--(5.12) of `COMPILER_DEPTH_TIME.md`.

## Bridge-by-bridge audit

### 1. Exact finite-width dynamics

The scaling is internally consistent.  From

\[
 f=n^{-1}a^TH_L,
\]

the update \(\theta^{s+1}=\theta^s+hn\nabla f\) gives

\[
 a^{s+1}=a^s+hH_L^s,
 \quad
 W_\ell^{s+1}=W_\ell^s+\frac h{\sqrt n}
 C_\ell^s(H_{\ell-1}^s)^T,
 \quad
 Z_1^{s+1}=Z_1^s+hC_1^s.
\]

Summing these updates gives exactly the strictly past-time learned terms
in (2.11)--(2.13).  The raw initialization-matrix chronology has
\((2N+1)(L-1)\) actions, including the terminal forward sweep.

### 2. Adaptive reused-matrix conditioning

Lemma 4.1 conditions each next row or transpose query on the complete
chronological pre-innovation sigma-field.  The projector decomposition

\[
 M=P_CM+MP_H-P_CMP_H+P_C^\perp\widetilde M P_H^\perp
\]

is the exact conditional Gaussian law.  Its proof preserves independence
of the residuals of all other connectors, even when a query depends on
previous actions of those connectors.  The row and column regression
formulas (4.4)--(4.7) have the correct normalizations and include the
enlarged cross block needed after the current forward action.

This explicitly handles the potentially dangerous dependence of a later
feature query on earlier transpose actions of the same matrix.

### 3. Response terms and inverse-free DAG

The two Gaussian integration-by-parts calculations give

\[
 \mathcal R=SQ+KP^T,
 \qquad
 \mathbb E[dH_*]=K\rho+Sq,
 \qquad
 \mathbb E[yC_*]=Q\sigma+Pk.
\]

Substitution into the exact conditional regressions cancels both
cross-projection terms.  The surviving raw actions are exactly

\[
 \xi_{\ell,s}+\sum_{r<s}\rho_{\ell,sr}C_\ell^r,
 \qquad
 \chi_{\ell,s}+\sum_{r\le s}\sigma_{\ell,sr}H_{\ell-1}^r.
\]

Adding the exact learned terms produces the DAG in Section 5.  No matrix
inverse remains in that population recursion.

### 4. Rank, concentration, and uniform integrability

For nonconstant \(\phi\) and fixed \(h\ne0\), Section 7 proves strict
positivity of every finite feature and cotangent history Gram.  The proof
uses a new conditional Gaussian innovation at each extension.  It treats
separately the otherwise missed affine case \(\phi'(x)=p\ne0\), where the
top cotangent innovation comes through the preceding readout update.

Sections 8--10 list every empirical Gram and cross block used in a
regression.  The stopped raw/extended/ideal coupling has a finite moment
tower,

\[
 2m\,8^{3(2N+1)(L-1)+1},
\]

and the action error decomposition (9.8b) contains all four required
terms: preceding-field error, coefficient error, innovation-scale error,
and removed finite-rank projection.  The raw polynomial energy majorant
then removes stopping and gives terminal uniform integrability.  Hence,
for every fixed \(h\ne0\),

\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^N=F_{N,L}(h).
\]

At \(h=0\), the finite-width expectation is directly zero because the
initial readout is independent and centered; this agrees with the DAG.
Thus the identification covers every step used in the final inequality.

### 5. Singular-covariance regularity

Lemma 3.1 of `COMPILER_DEPTH_TIME.md` is genuinely inverse-free.  It
regularizes \(C(h)\) by \(C(h)+\epsilon I\), applies Price's formula in
the nonsingular problem, and passes to \(\epsilon=0\) using the uniform
square-root estimate and a polynomial Gaussian envelope.  Its mixed
derivative hypothesis is sufficient for five Price iterations.

Chronological application to the DAG is triangular: each covariance,
response, and coefficient used in a call was constructed at an earlier
call.  The derivative budget is at most ten beyond the one source
derivative in a response, so \(C^{12}\) is sufficient.  Consequently
\(F_{N,L}\in C^5([-1,1])\), including at the rank-one repeated-time
covariances at \(h=0\).

### 6. Non-circular coefficient and explicit remainder constant

The exact compiler defines \(\mathcal J^{\rm cmp}_{r,N,L}\) by the
finite Price recursion before identifying it with
\(F_{N,L}^{(r)}(0)\).  At \(h=0\), its terms reduce to finite products of
the explicit one-dimensional moments

\[
 \mathbb E\left[G^a\prod_{r=0}^{12}
                  \phi^{(r)}(G)^{\beta_r}\right].
\]

Thus \(\kappa^{\rm cmp}_{\phi,L,t}\) is activation-defined and is not a
renaming of an unknown output derivative.

The syntax/envelope recursion (5.1)--(5.5) terminates after explicitly
stated finite numbers of iterations.  The one-call estimate propagates

\[
 S\longmapsto B_\phi^{r_N}S^{p_N}
\]

through exactly \(M_{L,N}\) Gaussian calls, starting at
\(B_\phi^{2L}\).  Solving that scalar recursion gives

\[
 E_{L,N}=2L p_N^{M_{L,N}}
 +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1},
\]

and hence the activation-envelope estimate

\[
 \sup_{|h|\le1}|F_{N,L}^{(5)}(h)|
 \le B_\phi^{E_{L,N}}.
\]

The right side is defined entirely from \(M_\phi,L,N\), not from an
output supremum, trajectory, or continuity modulus.

### 7. Cancellation and Taylor remainder

The sign transformation in Section 7 makes every \(F_{N,L}\) odd.  The
nodewise one-mark compiler calculation gives

\[
 F_{N,L}'(0)=N\sum_{j=0}^L
 \bigl(\mathbb E\phi'(G)^2\bigr)^j,
\]

so the linear terms in \(F_{t,L}(2\eta)-F_{2t,L}(\eta)\) cancel.
Taylor's integral remainder through degree four then gives the factor

\[
 \frac{32\overline{\mathcal J}_5(F_{t,L})
       +\overline{\mathcal J}_5(F_{2t,L})}{120}.
\]

Horizon monotonicity and \(33/120<1\) yield the displayed
\(B_\phi^{E_{L,2t}}|\eta|^5\) bound for \(|\eta|\le1/2\).

### 8. Three-hidden-layer specialization

For \(L=3\) and horizon \(N=2t\),

\[
 M_{3,2t}=(4t+1)(3-1)=8t+2.
\]

Substitution into the general exponent gives exactly

\[
 E_{3,2t}
 =6p_{2t}^{8t+2}
 +r_{2t}\frac{p_{2t}^{8t+2}-1}{p_{2t}-1}.
\]

No hidden \(L\)- or \(t\)-dependent constant remains.

## Forbidden-shortcut check

- No finite-width Taylor expansion is used.
- No interchange of \(n\to\infty\) and \(h\to0\) is used.
- No unspecified \(o(\eta^3)\) occurs in the theorem.
- No remainder constant is defined by an output or trajectory supremum.
- No continuity-defined radius is used.
- Reused \(W/W^T\) dependencies and all empirical conditioning data are
  included explicitly.
- Singular covariance differentiation is proved rather than assumed.
- The exact coefficient is constructed from Gaussian activation
  integrals before its derivative interpretation.

## Exact scope; not defects

This PASS does not establish either of the following stronger claims:

1. the compact nine-moment identity
   \(\kappa_{\phi,L,t}=-t(2t-1)J_{\phi,L}/2\);
2. a time-uniform remainder of the form
   \(C_{\phi,L}t^4|\eta|^5\) on \(|\eta|\le c_{\phi,L}/t\).

Those claims require additional arguments.  The unconditional result
audited here is the fixed-finite-\((L,t)\), exact-compiler theorem only.
