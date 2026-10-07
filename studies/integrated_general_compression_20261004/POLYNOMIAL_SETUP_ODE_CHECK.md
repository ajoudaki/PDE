# Cross-route audit of the frozen ODE setup candidate

2026-10-06. This is a scoped cross-route check, not an independent discovery,
promotion review, complete audit of `RESULT.md`, or endorsement of a completed
setup algorithm. No experiments were run and the candidate was not edited.

## Inputs and verdict

The entire frozen input `POLYNOMIAL_SETUP_ODE_ROUTE.md`, including its final
compressed-lift section, was read. Its SHA-256 at both the beginning and end
of the mathematical check was

```
e5fe6ba56bc97cd9d116ee132f882bb2286b5a1b66036676985ed782bf443670
```

The checked `RESULT.md` had SHA-256

```
c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278
```

and `docs/notation.qmd` had SHA-256

```
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023
```

The relevant `RESULT.md` inputs were its dense model and mobilities, dense
fitting and parameter normalization, all-time training-carrier bound, source
families and their RMS bounds, exact source metric, proof reference matrices,
and complete readout/deficit cancellation and scalar comparison. The existing
probabilistic source event and the source-metric theorem are imported
hypotheses. They were not re-proved in this audit. No other studies or
archived book were read.

The accessible rigorous-math skill and adversarial-audit reference were applied.
The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` remained
unreadable, including on the earlier escalated read. As authorized by the
supervisor, the fallback is the accessible skill, `docs/notation.qmd`, and
the user's explicit notation rules.

**Verdict:** the normalized-coordinate calculations, endpoint estimates,
defect stability lemma, source-coordinate precision bridge and full-state
lifting estimate are mathematically supported as stated, conditional on the
imported event. No blocking mathematical defect was found. One minor notation
collision should be corrected before integration. The candidate correctly
leaves efficient permitted coefficient recovery unresolved; this audit does
not upgrade that algorithmic claim.

## Normalized coordinates and gradient blocks

The candidate uses

\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),\qquad
f_n(v)=w^Th^{(L)}(v)/n.
\]

Under the physical mobilities \((n,1,\ldots,1,n)\), the ordinary
Euclidean gradient in these coordinates has blocks

\[
\nabla_{A/\sqrt n}f_n=\frac{\delta^{(1)}v^T}{\sqrt n},\qquad
\nabla_{W^{(j)}}f_n=\frac{\delta^{(j)}h^{(j-1)T}}n,\qquad
\nabla_{w/\sqrt n}f_n=\frac{h^{(L)}}{\sqrt n}.
\]

For example \(A=\sqrt n\,\theta_A\), so its gradient is
\(\sqrt n\) times the gradient with respect to \(A\). Its
normalized velocity is the physical first-matrix velocity divided by
\(\sqrt n\). Both give the first block above and the vector field
\(-2m^{-1}\sum_a r_a\nabla_\theta f_n(v_a)\). The readout
calculation is identical. Thus there is no missing factor of \(n\),
\(m\), or \(\sqrt d\); the last is already absorbed into
\(v=x/\sqrt d\), with \(\|v\|_2=1\).

The imported real-fitting bounds imply that a state within Euclidean
distance one of the true normalized state has normalized first-matrix
operator norm and mixer operator norms at most ten, and readout RMS at
most \(R=1+2Y/\sqrt\lambda\). The feature recursion
\(H_j=\max(1,b+10sH_{j-1})\), with the stated first-layer version,
therefore applies to all real sphere queries in that neighborhood.
Only derivative bounds and linear activation growth are used; bounded
activation values are not inserted.

## Endpoint Jacobian estimates and anchored Taylor remainder

Let \(E=\|u-\theta\|_2\), let \(D_h\) be the sum of
normalized first-matrix and hidden-matrix Frobenius differences, and
let \(D_w\) be the readout RMS difference. Then
\(D_h\le\sqrt L E\) and
\(D_h+D_w\le\sqrt{L+1}E\).

Forward subtraction gives, at each layer, a direct changed-matrix term
bounded by its Frobenius difference times the lower feature RMS and a
propagated term with multiplier at most \(10s\). The candidate's
\(F_z=H(10s)^{L-1}\) dominates each resulting coefficient. Hence
its (4) is valid for all sphere queries.

For a training sample, write the response difference as

\[
\delta_u^{(j)}-\delta_\theta^{(j)}
=\phi_j'(z_u^{(j)})(k_u^{(j)}-k_\theta^{(j)})
+[\phi_j'(z_u^{(j)})-\phi_j'(z_\theta^{(j)})]k_\theta^{(j)},
\]

where the products are coordinatewise. The second term uses only the
true endpoint carrier maximum \(M_n\) and has RMS at most
\(t_2M_nF_zD_h\). The changed-mixer term in the first part is at
most \(sB\|\Delta W\|_F\), and the upper-response difference
propagates with factor \(10s\). At the top the direct readout
contribution is \(sD_w\). Unrolling gives

\[
\frac{\|\delta_u^{(j)}-\delta_\theta^{(j)}\|_2}{\sqrt n}
\le (10s)^{L-1}
\{s(1+B)+Lt_2F_zM_n\}(D_h+D_w),
\]

which is the candidate's \(D(M_n)\) estimate. No perturbed-state
carrier maximum is needed.

For a hidden gradient block, splitting its outer product gives the
Frobenius bound

\[
H\frac{\|\delta_u^{(j)}-\delta_\theta^{(j)}\|_2}{\sqrt n}
+B\frac{\|h_u^{(j-1)}-h_\theta^{(j-1)}\|_2}{\sqrt n}.
\]

Adding the first-matrix and readout blocks gives exactly the sufficient
coefficient

\[
\sqrt{L+1}\left\{
[1+(L-1)H]D(M_n)+[1+(L-1)B]sF_z
\right\}=J(M_n).
\]

The un-subtracted block norms similarly sum to
\(H+[1+(L-1)H]B=G\). Ordinary Euclidean block norms are bounded
by these sums, proving the candidate's (5).

For the Taylor remainder, the candidate's exact identity is correct.
Indeed use

\[
\Delta z^{(j)}=W_\theta^{(j)}\Delta h^{(j-1)}
+\Delta W^{(j)}h_\theta^{(j-1)}
+\Delta W^{(j)}\Delta h^{(j-1)}
\]

inside
\(\Delta h^{(j)}=\phi_j'(z_\theta^{(j)})\Delta z^{(j)}+
a^{(j)}\), then propagate all linear terms backwards through the
true-state gates and mixers. The linear parameter terms give
\(\langle\xi_a(\theta),u-\theta\rangle\). The remaining terms
are precisely the three displayed sums in the candidate.

Their bounds are, respectively,

\[
\frac{t_2M_n}{2}\sum_{j=1}^L
\frac{\|\Delta z^{(j)}\|_2^2}{n}
\le\frac{L^2t_2M_nF_z^2}{2}E^2,
\]
\[
BsF_zD_h\sum_{j=2}^L\|\Delta W^{(j)}\|_F
\le LBsF_zE^2,
\qquad
sF_zD_wD_h\le sF_z\sqrt L E^2.
\]

These are exactly the three terms in \(C(M_n)\). The proof uses
a scalar activation Taylor formula and the true endpoint carrier bound;
it does not use a Hessian estimate on an uncontrolled parameter segment.

## Differential inequality and bootstrap constants

Put \(x=\|e_f\|_2/\sqrt m\), where
\(e_{f,a}=f_n(u,v_a)-f_n(\theta,v_a)\). The anchored Taylor
estimate replaces \(\langle e,\xi_a(\theta)\rangle\) by
\(e_{f,a}\) with error at most \(CE^2\). The gradient-difference
term is bounded using \(JE\). Cauchy--Schwarz in the sample index
therefore yields

\[
\frac12(E^2)'
\le-2x^2+2(C+J)xE^2+2J\rho E^2+E\|d\|_2.
\]

The maximum over \(x\ge0\) of the first two terms is
\((C+J)^2E^4/2\). Dividing by \(E>0\), and regularizing at
zero, gives the claimed

\[
E'\le2J\rho E+\frac12(C+J)^2E^3+\|d\|_2.
\]

The integrating factor uses
\(a(t)=2J\int_0^t\rho\le4JY/\lambda=A_n\). For
\(z=e^{-a}E\le2E_0\), its cubic term integrates to at most
\(4(C+J)^2Te^{2A_n}E_0^3\). The second hypothesis in (7) makes
this at most \(E_0/2\); the other terms sum to at most \(E_0\).
This proves the strict bootstrap improvement
\(z\le3E_0/2\). The first hypothesis ensures
\(E\le2e^{A_n}E_0\le1/2\), so the parameter-neighborhood stop
does not occur. The zero-defect, zero-initial-error case follows from
ordinary local uniqueness or the same regularization.

The affine dependence of \(J\) on the true training-carrier bound
\(M_n=2K_{\rm src}S\sqrt{\log(en)}\) makes
\(A_n=a_0+a_1\sqrt{\log(en)}\) at fixed admissible structural
parameters. The horizon \(T\) remains in the smallness condition
for the cubic term, but not in the linear amplification exponent.
The candidate expressly keeps this a finite-horizon defect theorem.

## Source-coordinate bridge

At every real query, the operator and readout bounds give carrier RMS
at most \(K_q=R(10s)^{L-1}\). Thus a true query carrier has
coordinate maximum at most \(\sqrt nK_q\). Substituting that
quantity into the verified backward estimate and finally converting
RMS to Euclidean norm gives

\[
\|\delta_u^{(j)}-\delta_\theta^{(j)}\|_2
\le n(10s)^{L-1}
\{s(1+B)+Lt_2F_zK_q\}\sqrt{L+1}E.
\]

Here both terms are bounded by the displayed expression using
\(\sqrt n\le n\). For forward features, the Euclidean bound
is \(\sqrt n\,sF_zD_h\le n\,sF_z\sqrt L E\).
For either initialized image, first apply
\(\|W_0v\|_\infty\le\|W_0v\|_2\le8\|v\|_2\).
This order matters: it avoids adding a further \(\sqrt n\) by
converting the base bound to a coordinate bound too early. It gives
exactly the candidate's sufficient \(C_{\rm src}nE\) bound for
all four families. Hence (8) and (10) imply coordinate accuracy
\(\eta\) uniformly over the specified time interval and sphere.

For \(\eta=n^{-a}\), fixed \(a>0\), and logarithmic horizon,
the reciprocal tolerance has logarithm
\(O(\log n+\sqrt{\log n})\). The cubic bootstrap condition
introduces only the separately displayed polynomial/logarithmic factors.
This confirms the numerical-tolerance claim. It supplies neither an
algorithm attaining that tolerance nor an activation bit-complexity bound.

The pairing qualification is also correct. Source values obtained by
evaluating the approximate state can be paired with their exact fixed
initialized-matrix images; applying the same scalar coefficient map
then preserves the pairing. Independent numerical approximations to
both members need not obey that identity. The candidate does not infer
coefficient recovery merely from ODE stability.

## Dense lift and normalization of matrix errors

From \(U_j^TU_j/n=I\) and \(P_j^TM_jP_j=I\), the maps

\[
\mathcal L_j=U_jP_j^TM_j,\qquad
\mathcal L_j^*=P_jU_j^T/n
\]

are adjoints for the dense normalized pairing and selected metric.
Their composition on selected coordinates is
\(\mathcal L_j^*\mathcal L_j=P_jP_j^TM_j\), the
\(M_j\)-orthogonal projector onto \(\operatorname{ran}P_j\).
Thus \(\mathcal L_j\) is a contraction into dense RMS norm and
recovers a source vector from its restriction exactly.

If \(\|u-p\|_\infty\le\eta\) with \(p\in E_j\), the
source-metric diagonal mass bound gives

\[
\frac{\|u-\mathcal L_ju_{I_j}\|_2}{\sqrt n}
\le\eta+\|(u-p)_{I_j}\|_{M_j}\le3\eta.
\]

The matrix contraction in the candidate can be verified without a
normalization convention left implicit. Write
\(O_j=U_j/\sqrt n\), so \(O_j^TO_j=I\). Then

\[
\mathcal L_jB\mathcal L_{j-1}^*
=O_j\,[P_j^TM_jBP_{j-1}]\,O_{j-1}^T.
\]

The middle factor equals

\[
(P_j^TM_j^{1/2})
(M_j^{1/2}BM_{j-1}^{-1/2})
(M_{j-1}^{1/2}P_{j-1}).
\]

The outside factors have operator norm one by source isometry. Thus
its Frobenius norm is bounded by the selected Hilbert--Schmidt norm
\(\|M_j^{1/2}BM_{j-1}^{-1/2}\|_F\), exactly as required.
The first-weight lift has the corresponding contraction after dividing
its Frobenius norm by \(\sqrt n\), and the readout lift contracts
into RMS norm.

Lift the proof reference matrices from `RESULT.md`. The difference
between the compressed lift and reference lift is at most
\(a_h+b_e\) in normalized parameter norm: hidden discrepancies
contract, while \(w_C-w_R=\zeta-p\) gives the raw-readout bound
\(\|w_C-w_R\|_{M_L}\le b_e\). Lifting the raw readout is
therefore justified even though the compressed predictor uses its
corrected effective readout.

The reference lift starts from the exact dense parameters. The first
matrix uses the exact source membership of the columns of \(A_0\);
the readout is initially zero; and the hidden lift retains \(W_0\)
plus only the reference increment. Its first-matrix and readout
projection errors each have integrated norm at most

\[
6\eta\int_0^T\rho(t)\,dt\le12(Y/\lambda)\eta.
\]

For a hidden block, put
\(\widehat\delta=\mathcal L_j\delta_{I_j}\) and
\(\widehat h=\mathcal L_{j-1}h_{I_{j-1}}\). The normalized
outer-product discrepancy satisfies

\[
\left\|\frac{\delta h^T-\widehat\delta\widehat h^T}{n}\right\|_F
\le3\eta H_{j-1}^{\rm src}
+3\eta(S\tau_j^{\rm src}+3\eta)
=3\eta(S\tau_j^{\rm src}+H_{j-1}^{\rm src})+9\eta^2.
\]

Multiplication by \(2|c_a|/m\), summation and residual integration
give the hidden-block bound
\(12(Y/\lambda)\eta(S\tau_j^{\rm src}+H_{j-1}^{\rm src}+3\eta)\).
Taking the Euclidean sum over the two endpoint blocks and hidden
blocks, then adding the compressed/reference discrepancy, proves
the candidate's (16), including its factor \(12\) and the constant
\(2\) inside the square root.

The inherited scalar bound on \(a_h+b_e\) consequently gives a
valid subpolynomial-amplification full-state bridge on the original
source interval. It is not by itself a restart theorem.

## Minor correction and remaining claim boundary

At candidate line 119, \(P\) is defined as \(1+(L-1)H\) and
used in \(J(M)\). At line 232, the same symbol is redefined as
the full parameter dimension \((L-1)n^2+n(d+1)\). These roles
should receive distinct symbols, for example \(P_h\) for the
former and \(P_{\rm dense}\) for the latter. The intended
constants are clear from their definitions, so this is a minor
presentation issue. Literal substitution of the second definition
into the earlier formula would obscure the width dependence that
the lemma is designed to prove.

No further mathematics is licensed by the successful checks above.
The global coefficient-solve section correctly separates a defect
certificate from solver convergence and from the user's prohibition
on reconstructing the complete dense training path. Its conditional
operation count does not claim a bound on iteration count.

The final lift section likewise correctly leaves the restarted
nonzero-readout theorem, analytic control from approximate anchors,
accumulated window/solver/projection errors, final source-rank budget,
and avoidance or substantial reduction of full-horizon dense-jet work
unproved. These remain substantive obligations for a complete permitted
initializer. The present cross-route check supports the displayed
stability and lift lemmas, not the unresolved setup algorithm.

## Revised-input hash addendum

The supervisor corrected the notation collision after the preceding audit.
The revised candidate's SHA-256 is

```
46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6
```

The change replaces the layer-sum coefficient \(P=1+(L-1)H\) by
\(P_{\rm layer}\), updates its occurrences in \(G\) and
\(J(M)\), and splits one display line. The later \(P\) continues
to denote the dense parameter count. To verify the exact change, this
audit reversed those three symbol substitutions and the one line break
in a read-only stream; SHA-256 of the reconstructed content was exactly
the original audited hash
`e5fe6ba56bc97cd9d116ee132f882bb2286b5a1b66036676985ed782bf443670`.
Thus there were no additional changes to the frozen mathematical input.

The minor notation issue is resolved. The preceding scoped mathematical
verdict applies unchanged to the revised hash; the algorithmic claims
remain conditional and incomplete as stated.
