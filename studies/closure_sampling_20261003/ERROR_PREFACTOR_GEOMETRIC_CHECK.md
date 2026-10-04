# Internal reconstruction of the polynomial-prefactor route

2026-10-04. **PASS for the stated conditional deterministic theorem and
its assembly with the supplied source event.** No correction to the frozen
candidate is required. This is a scoped internal check, not a promotion
review or a fresh check of the inherited stochastic source proof.

The checked candidate is `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md`, SHA-256
`2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c`.
Its complete text, including all definitions, derivations, tails, storage
assembly, and qualifications, was read after the final formatting freeze.
The author confirmed that no pending edits remained.

The result checked is

\[
\sup_{t\in[0,\infty],v\in S^{d-1}}|f_C(t,v)-f_n(t,v)|
 \le \frac{C}{\sqrt{\lambda n}},\qquad
\lambda=\min(1,\gamma/m),\qquad 0<Y\le c\lambda,
\]

with structural \(C,c\), conditional on the existing source, carrier,
Gram, and fitting event. The coordinate source tolerance remains exactly
\(n^{-1}\), and the existing retained size
\(C\lambda^{-2}\log^{3d+2}(en)+Cm(d+1)\) is unchanged. In the uncapped
case the error prefactor is \(C\sqrt{m/\gamma}\). The original realized
dense trajectory and physical clock are unchanged.

## 1. Coverage, provenance, and independence limits

The checker first developed the independent partial estimate in
`ERROR_PREFACTOR_SCALED_ROUTE.md`, froze it, and only then received the
geometric route. That partial estimate did not obtain the cancellation
checked here. The checker exchanged mathematical summaries with the
author/coordinator before this full reconstruction. Therefore this is a
separate internal reconstruction by a nonauthor of the geometric proof,
but is not a blind or promotion-isolated review. No claim of either is
made.

The complete scientific inputs actually read were:

| File | SHA-256 |
| --- | --- |
| `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md` | `2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| `STORAGE_QUADRATIC_CHECK.md` | `b373ee9212997c6e60002b2cf0ad613b6b58865ab82cc9589bc70931603724d9` |
| `GENERAL_WEIGHTED_COMPARISON.md` | `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306` |
| `DATASET_LABEL_DEPENDENCE.md` | `bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52` |
| `INPUT_DEPTH_REFINEMENT.md` | `9d468fe3469436c1c10cf01f9194cff7fea71339c8964578b83047b4f5c79a3d` |
| `SAMPLE_COUNT_REFINEMENT.md` | `d1de9321308530b9cd648e3ffd25f4987f42b2a343260d087cae924fd13f7242` |

Shared process instructions, the canonical-notation skill and its neural
reference, the rigorous-math skill, and the conjecture contract/audit
references were read. Source references outside this list were not
retrieved. Historical smaller label regimes and larger storage counts in
the older runtime check do not replace the current supplied conclusions.

Actual checks were direct algebraic reconstruction, Hilbert-space norm
estimates, zero-norm and zero-label checks, and explicit parameter/width
accounting. The files were read with `cat`; versions were checked with
`sha256sum`. No experiment, numerical test, external theorem, Git
operation, or maintained-book edit was used or needed for these identities.

## 2. Source transfer and sample normalization

All normalized sample vectors are Euclidean, with the physical residual
written \(c/\sqrt m\). Neuron norms use the fixed \(H_\ell\) metrics;
matrix directions use the corresponding Hilbert–Schmidt norms. Write

\[
s=Y/\lambda,\qquad \alpha=Y/\sqrt\lambda,
\qquad \epsilon\le\min(1,Y).
\]

The column of the hidden-direction operator \(\mathcal J_C\) for sample
(a) is its complete raw hidden update direction divided by \(\sqrt m\).
Its Gram \(\mathcal J_C^*\mathcal J_C\) therefore has exactly the hidden
part of \(K_C/m\). Its operator norm is bounded by the square root of the
mean squared direction norm, hence by \(C\alpha\), without an extra
sample-count factor. The rank-one mixer norm is the product of the
backward and forward vector norms. The first-layer norm includes the
unit input vector, so it has the same bound. This reconstructs candidate
(4)–(7), with the direction Gram understood as the specified training
Gram rather than a parameter-gradient identity.

To check candidate (8), let \(\widetilde V_n\) contain one source-space
approximant to each full feature column, divided by \(\sqrt m\), and let
\(\widetilde V_R\) be its selected restriction. The column errors imply

\[
\|V_n-\widetilde V_n\|\le\epsilon,
\qquad \|V_R-\widetilde V_R\|\le C\epsilon.
\]

These follow by a Frobenius bound on the normalized columns. Exact source
isometry gives \(\|\widetilde V_R b\|=\|\widetilde V_n b\|\) for every
sample vector (b), even though the spaces may depend on initialization.
The triangle inequality proves

\[
\|V_Rb\|\le\|V_nb\|+C\epsilon\|b\|.
\]

Apply this with \(b=c_n/\sqrt m\). The original readout equation is
\(\dot w_n=2V_n(c_n/\sqrt m)\). Its mobility norm is included in the
full parameter speed, whose integral is \(C\alpha\). Consequently

\[
\int_0^T\nu\le C\alpha+C\epsilon s\le C\alpha,
\qquad \nu=\|V_Rc_n/\sqrt m\|.
\tag{A}
\]

The last inequality uses \(\epsilon\le Y\) and
\(s\sqrt\lambda\le c\). This attacks the most important possible loss
of an extra inverse gap: replacing the original readout speed by a
generic \(C\rho_n\) bound would indeed fail to prove (A), but the actual
energy bound supplies it.

The readout source approximation follows by integrating the feature
approximation with its residual coefficients. Its coordinate error is
\(C\epsilon s\); finite Riemann sums and closedness of the finite source
space justify the integral statement without measurable coefficient
selection. Therefore \(\|w_R\|\le C\alpha+C\epsilon s\le C\alpha\).
Every selected backward response has norm at most its original norm plus
\(C\epsilon\le C\alpha\). These are precisely the selected estimates
used later; none is asserted beyond the source horizon.

## 3. Observation identity, backward differences, and Gram forcing

Set \(q=V_C^*V_C\succeq gI\), \(g=c_0\lambda\),
\(T_C=V_Cq^{-1}\), and \(P_C=T_CV_C^*\). Direct multiplication gives

\[
T_C^*T_C=q^{-1},\quad V_C^*T_C=I,
\quad P_C^*=P_C=P_C^2.
\]

Thus \(\|T_C\|\le g^{-1/2}\) and \(P_C\) is an orthogonal projector.
For \(e=(c_C-c_n)/\sqrt m\), \(z=w_C-w_R\), and
\(d_R=V_R^*w_R-(y-c_n)/\sqrt m\), expanding the actual readout
reconstruction gives exactly

\[
\widehat w_C-w_R
 =(I-P_C)z-T_Ce-T_C(V_C-V_R)^*w_R-T_Cd_R.
\tag{B}
\]

The signs in (B) agree with residuals defined as labels minus predictions.
With \(p=T_Ce\) and \(\zeta=z+p\), one has
\((I-P_C)z=(I-P_C)\zeta\). The source pairing estimate gives
\(\|d_R\|\le Cs\epsilon\), and the hidden forward subtraction gives
\(\|V_C-V_R\|\le C(a+\epsilon)\). These facts prove the claimed bound

\[
\|\widehat w_C-w_R\|
\le C[b+s(a+\epsilon)+\epsilon/\sqrt\lambda],
\quad b=\|p\|+\|\zeta\|.
\]

The backward subtraction multiplies a changed activation gate by the
actual selected dense carrier, whose coordinate maximum is (M).
The metric comparison \(D/4\preceq H\preceq D\) bounds every diagonal
multiplier in (H) by twice its coordinate supremum. It therefore proves
the required \(M(a+\epsilon)\) term with no selected minimum-mass
dependence. Other backward terms use bounded mixers, the already bounded
upper response error, and a changed mixer times a response of norm
\(C\alpha\). Converting the resulting column estimates to operator norms
adds no (m). This verifies candidate (17), including its source term
\(M\epsilon+\epsilon/\sqrt\lambda\).

In the selected-reference Gram, each feature pairing error is
\(C\epsilon\). Each response pairing error is at most
\(C\epsilon(\alpha+\epsilon)\\), and response norms are \(C\alpha\).
The products defining a hidden Gram entry hence have error at most
\(C\epsilon\). After division by (m), an entrywise bound gives an
operator bound of the same order. This verifies \(\|D\|\le C\epsilon\)
in candidate (18), without treating the actual selected sources as exact
members of the source space.

The factorization (19) is exact: expand the differences of the two feature
Grams and the two hidden-direction Grams before adding (D). The five
terms in \(F=2\|T_C\Delta\mathcal K(c_n/\sqrt m)\|\) are bounded by

\[
\begin{array}{c|c}
\text{term}&\text{bound up to a structural factor}\\ \hline
T_CV_C^*\Delta V(c_n/\sqrt m)&(a+\epsilon)\rho_n\\
T_C\Delta V^*V_R(c_n/\sqrt m)&(a+\epsilon)\nu/\sqrt\lambda\\
T_C\mathcal J_C^*\Delta\mathcal J(c_n/\sqrt m)
&s\rho_n\|\Delta\mathcal J\|\\
T_C\Delta\mathcal J^*\mathcal J_R(c_n/\sqrt m)
&s\rho_n\|\Delta\mathcal J\|\\
T_CD(c_n/\sqrt m)&\epsilon\rho_n/\sqrt\lambda .
\end{array}
\]

Inserting the backward estimate gives candidate (20) exactly. The
asymmetric use of \(\nu\) in the second row is necessary and valid.

## 4. Residual energy, cancellation, and zero norms

Differentiating \(T_C=V_Cq^{-1}\), using
\(\dot q=\dot V_C^*V_C+V_C^*\dot V_C\), yields

\[
\dot T_C=(I-P_C)\dot V_Cq^{-1}-T_C\dot V_C^*T_C.
\tag{C}
\]

Since \(q^{-1}e=T_C^*p\) and
\(\|\dot V_C\|\le C\alpha\rho_C\), both terms in (C) applied to
(e) have norm at most \(Cs\rho_C\|p\|\). This uses only a
compressed feature derivative; no derivative of a selected reference
source or source error is taken.

The exact residual equation has the sign

\[
\dot e=-2(q+\mathcal J_C^*\mathcal J_C)e
             -2\Delta\mathcal K(c_n/\sqrt m).
\]

Multiplying by \(T_C\) and pairing with (p) gives the main dissipation

\[
-2\langle p,V_Ce\rangle=-2\|e\|^2.
\]

The hidden Gram need not be dissipative in this lifted metric. The proof
does not assume that it is. Its absolute contribution is bounded by

\[
2\|p\|\|T_C\|\|\mathcal J_C\|^2u
 \le C\frac{\alpha^2}{\lambda}u^2=Cs^2u^2,
\qquad u=\|e\|,
\]

because \(\|p\|\le u/\sqrt g\). Thus structural smallness of (s)
absorbs this contribution with no additional power of (m) or the gap.
This directly checks the potentially dangerous noncommuting-Gram term.

For a fully justified treatment at zero, put
\(p_\delta=(\|p\|^2+\delta^2)^{1/2}\). The preceding squared-norm
inequality implies

\[
\dot p_\delta\le
-c_1\frac{u^2}{p_\delta}+Cs\rho_C\|p\|+F.
\]

Integrate, using \(p_\delta(0)=\delta\), and let \(\delta\downarrow0\).
The nonnegative damping integrands increase to
\(u^2/\|p\|\), defined as zero when (p=0). This is consistent because
\(V_C^*p=e\), so (p=0) implies (u=0). Monotone convergence gives

\[
\|p(t)\|+c_1\int_0^t\frac{u^2}{\|p\|}
 \le\int_0^t(Cs\rho_C\|p\|+F).
\tag{D}
\]

Also \(u\ge\sqrt g\|p\|\), hence
\(u^2/\|p\|\ge\sqrt g\,u\). Dropping either term on the left of
(D) proves both estimates in candidate (25). No continuity claim for an
undefined quotient is needed.

The raw readout difference obeys
\(\dot z=2V_Ce+2\Delta V(c_n/\sqrt m)\). Therefore the \(2V_Ce\)
terms cancel exactly in \(\dot\zeta=\dot z+\dot p\). The remaining
hidden-Gram term has norm at most \(C\alpha^2u/\sqrt\lambda\).
Using (D) to integrate (u) turns its coefficient into
\(C\alpha^2/\lambda=Cs^2\), which is bounded. This proves candidate
(26)–(27); it does not require ordinary-gradient dynamics or a gate
adjoint identity.

## 5. Closure and complete parameter accounting

The exact hidden velocity difference is

\[
2\mathcal J_Ce+2(\mathcal J_C-\mathcal J_R)c_n/\sqrt m.
\]

Its residual-error coefficient is \(C\alpha\). Equation (D) therefore
changes that coefficient to \(C\alpha/\sqrt\lambda=Cs\), proving
candidate (28)–(29). Summing the hidden and two readout error norms and
inserting the five forcing bounds above gives

\[
E(t)\le C\int_0^t A(r)
                  (E(r)+\epsilon/\sqrt\lambda)\,dr,
\qquad A=M\rho_n+\rho_C+\nu/\sqrt\lambda.
\]

The source and energy inputs give

\[
\int_0^T A\le Cs(1+M).
\]

There is no hidden \(\lambda^{-1/2}\) in this integral: its only unusual
term is controlled by (A). Differentiating the scalar integral majorant
with initial value \(\epsilon/\sqrt\lambda\) proves the candidate's
raw estimate. The source action bounds and (B) then transfer it to every
sphere query. This checks candidate (30)–(32) and the observable step.

All operator and Gram margins used here are supplied independently by
the global fitting proof. In particular, the argument does not need the
comparison error to be exponentially tiny to keep an inverse defined.
This closes the possible hidden-width loophole in a comparison-based
first-exit argument.

## 6. Tail, root-width conversion, and storage

Equation (C) implies \(\|\dot T_C\|\le C\lambda^{-1}\|\dot V_C\|\).
Direct differentiation of the projector, or multiplication using (C),
gives

\[
\dot P_C=(I-P_C)\dot V_CT_C^*
                   +T_C\dot V_C^*(I-P_C),
\]

so \(\|\dot P_C\|\le C\lambda^{-1/2}\|\dot V_C\|\).
These estimates improve the older product-rule bounds without requiring
minimum coordinate masses. For
\(b_C=(y-c_C)/\sqrt m\), differentiate
\(\widehat w_C=(I-P_C)w_C+T_Cb_C\). The four contributions have bounds

\[
C\rho_C,\quad
C Y^2\lambda^{-3/2}\rho_C,\quad
C Y^2\lambda^{-3/2}\rho_C,\quad
C\lambda^{-1/2}\rho_C,
\]

respectively. Since \(Y\le c\lambda\) and \(\lambda\le1\), their sum is
\(C\lambda^{-1/2}\rho_C\). The feature derivative contribution to
\(\dot f_C\) is \(C\alpha^2\rho_C\), which obeys the same bound.
Integration of the residual decay gives

\[
\sup_v|f_C(\infty,v)-f_C(t,v)|
 \le CY\lambda^{-3/2}e^{-c\lambda t}.
\]

The dense source tail is bounded by this sufficient expression. For
\(t\ge T\), each increment from its value at (T) is bounded directly
by the integrated speed tail, so the same-time triangle comparison is
valid for every later time and the endpoint. No stored endpoint or
stopped runtime is used.

Before simplifying anything, the checked all-time bound is

\[
C\lambda^{-1/2}\epsilon e^{Cs(1+M)}
 +CY\lambda^{-3/2}e^{-c\lambda T}.
\tag{E}
\]

Substituting \(\epsilon=n^{-1}\), \(M\le1+Cs\sqrt{\log(en)}\), and
\(T=C_T\lambda^{-1}\log(en)\) gives

\[
C\lambda^{-1/2}n^{-1}
 e^{Cs+Cs^2\sqrt{\log(en)}}
 +CY\lambda^{-3/2}n^{-1},
\]

after a structural choice of \(C_T\). Young's inequality bounds the
first exponential by
\(C\sqrt n\,e^{Cs+C's^4}\). The last factor is structural because
\(s\le c\), and \(Y\lambda^{-3/2}=s\lambda^{-1/2}\). Thus (E) proves
the claimed \(C/\sqrt{\lambda n}\) rate without moving any data
exponential into a width threshold.

The actual remaining width qualifications are the inherited stochastic
source/Gram event, the existing logarithmic gap convention in the source
dimension, and \(n^{-1}\le Y\). The proof does not claim a quantitative
or growing-dataset version of that inherited probability threshold.

The source tolerance, horizon order, and family count are unchanged;
the variables \(p,\zeta\) are analysis-only combinations of existing
states. Therefore no source degree, selected-neuron count, metric storage,
training cache, or moving state is added. The retained-size conclusion
follows directly from the supplied depth-refined source theorem and
quadratic runtime count. The zero-label case is separately the exact
zero predictor and does not invoke \(n^{-1}\le Y\).

## 7. Disposition and limitations

All newly claimed deterministic implications reconstruct with the stated
constant dependencies. The strongest apparent failure mechanisms—loss of
the selected readout path-length bound, noncommuting hidden-Gram terms in
the lifted metric, an unhandled zero norm, extra sample factors, source
derivatives, a small-mass dependence, a missing endpoint estimate, or a
data exponential hidden in width—do not survive the checks above.

This verdict validates the new comparison and its stated conditional
assembly. It does not independently reprove the inherited complex-source
probability event, improve its quantitative width threshold, prove an
optimal prefactor, give growing-data uniformity, change the optimizer to
ordinary gradient flow, or authorize promotion. Those are outside the
claim being checked. The earlier scalar-error route remains a valid
partial estimate but its unresolved exponential is superseded by this
matched vector calculation for the same runtime.

## 8. Separate check of the coordinator's label-dependent corollary

After the base verdict above was completed, the coordinator proposed
retaining the vanishing factor as \(Y\downarrow0\). This subsection checks
that additional corollary; it is not presented as part of the frozen
candidate or as an independent discovery by this checker. The stronger
conclusion is valid:

\[
\sup_{t,v}|f_C(t,v)-f_n(t,v)|
 \le C\frac{Y}{\lambda^{3/2}}n^{-1/2}
 =C\frac{s}{\sqrt\lambda}n^{-1/2}.
\tag{F}
\]

For exact parameter tracking, the observation identity (B) gives

\[
\|\widehat w_C-w_R\|
 \le C[b+s(a+\epsilon)+s\epsilon/\sqrt\lambda],
\]

because \(\|d_R\|\le Cs\epsilon\). The displayed candidate weakens the
last term to \(C\epsilon/\sqrt\lambda\), but its proof supplies the
sharper form without any extra hypothesis. The full output estimate is
therefore \(C[E+s\epsilon/\sqrt\lambda]\).

Since (E(0)=0), the integral majorant in Section 5 actually gives

\[
E(t)\le\frac\epsilon{\sqrt\lambda}(e^{B(t)}-1),\qquad
B(t)\le Cs(1+M).
\]

Set \(x=\sqrt{\log(en)}\). The carrier bound implies
\(B(t)\le Cs+Cs^2x\). Hence

\[
e^{B(t)}-1\le B(t)e^{B(t)}
 \le Cs(1+sx)e^{Cs+Cs^2x}.
\]

Uniformly over \(0\le s\le c\) and \(x\ge1\),

\[
(1+sx)e^{Cs+Cs^2x-x^2/2}\le C.
\]

For an explicit elementary bound, use
\(Cs^2x\le x^2/4+C's^4\) and the finite supremum of
\((1+cx)e^{-x^2/4}\) on \(x\ge1\). Thus with the unchanged
\(\epsilon=n^{-1}\), the finite-horizon error is at most
\(Cs\lambda^{-1/2}n^{-1/2}\). The endpoint term in (E) is already
\(Cs\lambda^{-1/2}n^{-1}\), so (F) follows on the same source event and
with the same horizon, storage, and width qualifications.

This refinement does not divide by (s) in the construction or proof.
The positive-label proof is uniform over the bounded ratios (s), and
(Y=0) remains the separately exact zero output. With
\(\lambda=\gamma/m\), the sharper prefactor is
\(CY(m/\gamma)^{3/2}\le C\sqrt{m/\gamma}\) under the label cap.

The subsequently supplied synthesis `ERROR_PREFACTOR_REFINEMENT.md`,
SHA-256 `59c1fd545ec22c87cea9b3d57b81de13956c758af2700cdbbee55ad85dbffb2f`,
was read completely. Its Section 4 agrees with the derivation in this
subsection, including the uniform supremum in its final paragraph. Its
statements of the inherited width qualification, fixed-data probability
quantifier, unchanged source accuracy and storage, and distinction from
ordinary gradient flow are also consistent with the checked result.
The report-status prose in that version still described the internal
reconstruction as ongoing; this administrative status does not alter the
mathematical conclusion. No scientific correction to that synthesis is
required.
