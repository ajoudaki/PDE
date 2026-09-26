# Exact canonical p=1 initialization: an independent no-series reduction

Status: frozen independent candidate, 2026-09-21. This is an exact derivation of the initialized kernel of the specified finite closure. It obtains a finite Gaussian-source integral representation, but does **not** obtain the stronger requested finite normal form consisting only of products of the original tanh and its derivatives at jointly Gaussian arguments. That stronger reduction remains open in this attempt. No impossibility statement is made.

This attempt used only the permitted established sources listed at the end. It was frozen before receiving another attempt's reasoning or conclusions. There is no training calculation, numerical experiment, activation approximation, or infinite activation series here.

## 1. Target and meaning of the requested normal form

Write \(\phi=\tanh\), \(u(\theta)=(\cos\theta,\sin\theta)\), and \(x(\theta)=\sqrt2\,u(\theta)\). Closure order is \(p=1\); it is independent of neural width and of any population quadrature count. All expectations below are exact population expectations.

In the user's layer notation, the initialized readin is \(W^{(1)}=G\), the finite middle coefficient matrix is \(W^{(2)}=M=D_1\), and the population readout is \(W^{(3)}=0\). The requested readout kernel is

\[
 K(\theta,\theta')
 =E_2\left[
 \phi\!\left(b_2^TD_1E_1[b_1\phi(G\cdot u(\theta))]\right)
 \phi\!\left(b_2^TD_1E_1[b_1\phi(G\cdot u(\theta'))]\right)
 \right].                                                    \tag{1}
\]

The two population expectations have their own probability spaces. Lower and upper Gaussian marks are not paired by coordinate index.

The strong target is a finite expression in expectations of products of factors \(\phi^{(r)}(X_j)\), where \((X_j)_j\) is a finite jointly Gaussian vector whose mean and covariance have been computed from permitted initialization data, with no hidden use of the unknown kernel and no activation polynomial approximation. An expectation of a composite function of Gaussian roots is exact, but by itself is a weaker representation. Replacing a composite function by a newly named activation does not close this distinction.

## 2. Canonical sources and the actual reverse response

Let \(G_1,G_2,Z_1,Z_2\) be independent standard Gaussians on the lower population. Set

\[
 v=E\phi(G)^2,
 \qquad \Xi_i\sim N(0,v)\quad\text{independently on the upper population},
\]
\[
 H_i=\phi(\Xi_i),\qquad
 \tau=E\phi(\sqrt v\,Z)^2,\qquad
 \alpha=E\phi'(\sqrt v\,Z)=1-\tau.
                                                               \tag{2}
\]

The forward source covariance is \(E[\phi(G_i)\phi(G_j)]=v\delta_{ij}\). The finite source/response rule, applied to the actual transpose of the same action, gives

\[
 h_i=\phi(G_i),\qquad
 \zeta_i=\sqrt\tau Z_i,\qquad
 R_i=\zeta_i+\alpha h_i,\qquad
 k_i=\phi(R_i).                                                \tag{3}
\]

Indeed, the reverse source covariance is \(E[H_iH_j]=\tau\delta_{ij}\), and the derivative response is \(E[\partial_{\Xi_j}H_i]=\alpha\delta_{ij}\). Thus the Gaussian part \(\zeta\) is independent of the lower roots \(G\), while the full reverse answer \(R\) retains the displayed response.

Every instruction used here is a finite composition of linear maps and tanh, with bounded first derivatives. The roots have all moments. These are the hypotheses of the finite smooth-program source rule in `global_nonlinear.md`, §3. The rule holds with frozen coefficient and covariance parameters. No growing query count or time evolution is used.

Define the exact scalar constants

\[
 s=E\phi(\sqrt\tau Z+\alpha\phi(G))^2,\qquad
 \beta=E[\phi(G)\phi(\sqrt\tau Z+\alpha\phi(G))],\qquad
 \gamma=1-s=E\phi'(R).                                       \tag{4}
\]

The constants \(v,\tau,s\) are strictly between zero and one, and \(\alpha,\gamma>0\). Also \(\beta>0\): the function \(m(t)=E_Z\phi(\sqrt\tau Z+\alpha t)\) is odd and strictly increasing, so \(t\,m(t)>0\) for \(t\ne0\); apply this to \(t=\phi(G)\). Cauchy–Schwarz gives \(\beta^2\le vs\).

## 3. A completed finite peeling calculation: the middle coefficient matrix

At order one the raw features are exactly

\[
 \psi_1=(1,h_1,h_2,k_1,k_2)^T,\qquad
 \psi_2=(1,H_1,H_2)^T.
\]

The two coordinate pairs \((h_i,k_i)\) are independent. Joint sign reversal of \((G_i,Z_i)\) makes both entries odd. Thus

\[
 G_1=\begin{pmatrix}1&0&0\\0&vI_2&\beta I_2\\0&\beta I_2&sI_2\end{pmatrix},
 \qquad G_2=\operatorname{diag}(1,\tau I_2).                    \tag{5}
\]

The scalar contraction formula (H3.1) is

\[
 E_2[B A_0F]
 =\sum_i E_1[Fh_i]E_2[\partial_{\Xi_i}B]
  +\sum_i E_1[\partial_{\zeta_i}F]E_2[BH_i].                  \tag{6}
\]

For completeness, the source of \(A_0F\) has covariance \(E[Fh_i]\) with \(\Xi_i\), and its response is \(\sum_iH_iE[\partial_{\zeta_i}F]\). Subtracting the source regression \(\sum_i E[Fh_i]\Xi_i/v\) leaves a centered Gaussian independent of \(\Xi\); its pairing with \(B(\Xi)\) is zero. Gaussian integration by parts gives \(E[B\Xi_i]=vE[\partial_{\Xi_i}B]\). Boundedness of the features and derivatives removes the boundary term and justifies the integration. This proves (6) for the features used here.

For \(B=H_i,F=h_j\), the first term is \(\alpha v\delta_{ij}\) and the second is zero. For \(B=H_i,F=k_j\), they are respectively \(\alpha\beta\delta_{ij}\) and \(\tau\gamma\delta_{ij}\), because \(\partial_{\zeta_i}k_j=\delta_{ij}\phi'(R_j)\). The constant row and column vanish. Consequently

\[
 C=E_2[\psi_2(A_0\psi_1)^T]
 =\begin{pmatrix}0&0&0\\0&\alpha v I_2&(\alpha\beta+\tau\gamma)I_2\end{pmatrix}.
                                                               \tag{7}
\]

This is an actual completed Gaussian peeling calculation. In particular it retains the reverse/reuse contribution \(\tau\gamma\). As a check, Gaussian integration by parts in \(\zeta\) also gives

\[
 \alpha\beta+\tau\gamma=E[R\phi(R)],
\]

since \(E[\zeta\phi(R)]=\tau E\phi'(R)\). This identity does not discard the response in \(R\).

Use precisely \(\eta=1/4096\), and abbreviate

\[
 A=v+\eta,\qquad B=s+\eta-\beta^2/A,\qquad C_0=\tau+\eta.
                                                               \tag{8}
\]

All are positive; in particular \(B\ge\eta+s\eta/(v+\eta)>0\). Inverse-lower-Cholesky normalization gives

\[
 b_1=\left((1+\eta)^{-1/2},\frac{h}{\sqrt A},
                \frac{k-\beta h/A}{\sqrt B}\right),\qquad
 b_2=\left((1+\eta)^{-1/2},\frac{H}{\sqrt{C_0}}\right),        \tag{9}
\]

and the only nonzero entries of \(D_1=L_2^{-1}CL_1^{-T}\) are

\[
 (D_1)_{H_i,h_i}=\frac{\alpha v}{\sqrt A\sqrt{C_0}},\qquad
 (D_1)_{H_i,k_i}=\frac{\delta}{\sqrt B\sqrt{C_0}},\qquad
 \delta=\alpha\beta\eta/A+\tau\gamma>0.                     \tag{10}
\]

The transpose on the right of the Cholesky normalization is essential. Equations (5)–(10) reproduce the exact canonical construction, including the ridge, and not an empirical-Gram diagonalization.

## 4. Exact circle reduction of every input contraction

For \(\rho\in[-1,1]\), let \(G,V,Z\) be independent standard Gaussians and define

\[
 Y_\rho=\rho G+\sqrt{1-\rho^2}\,V,
\]
\[
 P(\rho)=E[\phi(G)\phi(Y_\rho)],
\]
\[
 Q(\rho)=E[\phi(\sqrt\tau Z+\alpha\phi(G))\phi(Y_\rho)].       \tag{11}
\]

For an arbitrary unit input \(u=(u_1,u_2)\), \((G_i,G\cdot u)\) has the same law as \((G,Y_{u_i})\). The lower reverse noise \(Z_i\) remains independent of that pair. Hence, exactly,

\[
 E_1[h_i\phi(G\cdot u)]=P(u_i),\qquad
 E_1[k_i\phi(G\cdot u)]=Q(u_i).                              \tag{12}
\]

The constant pairing vanishes by oddness. Substituting (9)–(12) into the initialized preactivation gives

\[
 b_2^TD_1E_1[b_1\phi(G\cdot u)]
       =\ell(u_1)H_1+\ell(u_2)H_2,                          \tag{13}
\]

where the fully explicit deterministic coefficient function is

\[
 \ell(\rho)=\frac1{C_0}\left[
       \frac{\alpha v}{A}P(\rho)
       +\frac{\delta}{B}\left(Q(\rho)-\frac{\beta}{A}P(\rho)\right)
                         \right].                          \tag{14}
\]

An equivalent formula avoids Cholesky factors. Put

\[
 S=\begin{pmatrix}v&\beta\\\beta&s\end{pmatrix},\qquad
 \Delta=(v+\eta)(s+\eta)-\beta^2=AB>0.
\]

Then

\[
 \ell(\rho)=\frac{(\alpha v,\,\alpha\beta+\tau\gamma)}{\tau+\eta}
                (S+\eta I)^{-1}
                \binom{P(\rho)}{Q(\rho)},                  \tag{15}
\]

or, after inversion,

\[
 \ell(\rho)=
 \frac{[\alpha(v(s+\eta)-\beta^2)-\beta\tau\gamma]P(\rho)
       +[\alpha\beta\eta+(v+\eta)\tau\gamma]Q(\rho)}
      {(\tau+\eta)\Delta}.                                 \tag{16}
\]

Thus the canonical matrix algebra has removed all five- and three-dimensional feature notation from the kernel. It has not assumed that \(Q\) is a Gaussian-pair tanh moment.

The answer obtained by this independent attempt is the exact no-series identity

\[
\begin{split}
 K(\theta,\theta')=E_{\Xi_1,\Xi_2\stackrel{\rm iid}{\sim}N(0,v)}
  &\phi\!\left(\ell(\cos\theta)\phi(\Xi_1)
              +\ell(\sin\theta)\phi(\Xi_2)\right)\\
 {}×&\phi\!\left(\ell(\cos\theta')\phi(\Xi_1)
              +\ell(\sin\theta')\phi(\Xi_2)\right).
\end{split}                                                  \tag{17}
\]

Its coefficient construction uses scalar Gaussian integrals for \(v,\tau\), two-dimensional Gaussian integrals for \(s,\beta\), two-dimensional moments for \(P\), and three-dimensional Gaussian integrals for \(Q\). The final expectation is two-dimensional. These are exact integrals; selecting a numerical rule to evaluate them would introduce a separate approximation. No rule has been selected here.

## 5. Why canonical initialization does not cancel the remaining composition in this reduction

There are two separate issues: the exact source operation being computed, and algebraic cancellation inside that operation.

First, let \(U_\ell a=b_\ell^Ta\) and \(Q_\ell=U_\ell U_\ell^*\). The initialized finite action is

\[
 U_2D_1U_1^*=Q_2A_0Q_1.                                    \tag{18}
\]

This is exactly the operator identity in the canonical hierarchy. It is not the unfiltered action \(A_0\). A fresh unprojected forward call on a lower input independent of the action would have a centered Gaussian answer. Replacing (18) by that fresh call changes the requested finite-order model.

The source calculation can be done in the correct order to verify (13). Put \(F=Q_1\phi(G\cdot u)\). Its coordinate-i coefficients in the raw \((h_i,k_i)\) basis are

\[
 \binom{d_h}{d_k}=(S+\eta I)^{-1}\binom{P(u_i)}{Q(u_i)}.
\]

For the appended call \(A_0F\), formula (6) gives

\[
 E_2[H_iA_0F]
 =\alpha(vd_h+\beta d_k)+\tau\gamma d_k.
\]

The upper filter satisfies \(Q_2Y=\sum_iH_i E_2[H_iY]/(\tau+\eta)\) whenever the constant pairing of \(Y\) is zero. Therefore applying \(Q_2\) gives (15). The innovation orthogonal to the old \(\Xi\) fields has zero pairing with \(H_i\); it is integrated out by this scalar projection. It must not be put back as a fresh Gaussian variance inside the final activation.

Second, the response-dependent coefficient of \(Q(\rho)\) in (14) is \(\delta/(BC_0)>0\). Thus the explicit matrix algebra does not set this contribution to zero. This positivity does not exclude an as-yet-undiscovered identity among the scalar moments.

There is a particularly small exact test case. Oddness gives

\[
 P(0)=Q(0)=0,\quad P(1)=v,\quad Q(1)=\beta.
\]

Consequently

\[
 t_*:=\ell(1)
 =\frac1{C_0}\left[\frac{\alpha v^2}{A}
                   +\frac{\delta\beta\eta}{AB}\right]>0,
                                                               \tag{19}
\]

and the axis diagonal is already

\[
 K(0,0)=E_{\Xi\sim N(0,v)}\phi(t_*\phi(\Xi))^2.             \tag{20}
\]

This supplies a minimal scalar target for any proposed stronger identity. It has no input-angle interaction and no unresolved integration over additional dictionary coordinates. Any general finite reduction of (17) must, in particular, handle (20).

As a structural comparison only, setting the ridge to zero would give \(\ell(1)=\alpha v/\tau\): the lower axis input then lies exactly in the retained lower span, but the upper composition in (20) still appears. The actual result throughout this report uses \(\eta=1/4096\); zero ridge is not substituted into the target.

At positive ridge, the two axis preactivations have exactly one nonzero upper coefficient each, so \(K(0,\pi/2)=0\) by independence and oddness. The diagonal is positive by (19). These elementary checks agree with (17). The fourfold dictionary symmetry does not justify assuming that every kernel value depends only on \(\theta-\theta'\).

## 6. Exact first unresolved operation, and a constructive no-series reformulation

The earliest operation in the source chronology whose strict normal-form evaluation is not completed is applying the original activation to the reverse response,

\[
 \phi(\zeta+\alpha\phi(G)).                                 \tag{21}
\]

This occurs in the lower retained feature \(k\), before evaluating \(\beta,s,Q\). The source rule derives (21) exactly; it does not remove its inner \(\phi(G)\). If the coefficient constants are regarded as separately precomputed exact data, then the remaining strict-normal-form task is the outer expectation (17), already present in (20).

One can remove the shifted argument in (21) by an exact change of Gaussian density, with no series. Let \(T\sim N(0,\tau)\) be independent of \((G,V)\), and define

\[
 L(G,T)=\exp\left(\frac{\alpha T\phi(G)}\tau
                    -\frac{\alpha^2\phi(G)^2}{2\tau}\right).
                                                               \tag{22}
\]

For every bounded measurable \(F(G,V)\) and bounded measurable \(q\), translating the one-dimensional Gaussian density yields

\[
 E[F(G,V)q(\sqrt\tau Z+\alpha\phi(G))]
       =E[F(G,V)q(T)L(G,T)].                                \tag{23}
\]

To prove it, condition on \((G,V)\), use the density of \(N(\alpha\phi(G),\tau)\), and divide it by the density of \(N(0,\tau)\). Completing the square gives precisely (22). The conditional integral of \(L\) is one; all terms are integrable. Alternatively, \(|\phi(G)|\le1\) bounds \(L\) by \(\exp(\alpha|T|/\tau)\), which has finite Gaussian expectation.

In particular,

\[
 \beta=E[\phi(G)\phi(T)L(G,T)],\qquad
 s=E[\phi(T)^2L(G,T)],\qquad
 \gamma=E[\phi'(T)L(G,T)],
\]
\[
 Q(\rho)=E[\phi(T)\phi(Y_\rho)L(G,T)].                      \tag{24}
\]

Every activation argument in (24) is now jointly Gaussian. This is a useful exact constructive reformulation, but the exponential weight \(L\) remains. It is not a finite product of original activations or derivatives and therefore does not meet the strong requested normal form. Expanding \(L\) would introduce an infinite series; that step is deliberately not taken. Treating \(L\) as an additional admissible factor would change the required representation class and must be stated as such.

One further exact peeling check is available without changing density. For \(|\rho|<1\), differentiation followed by integration by parts in \(G,V\) gives

\[
 P'(\rho)=E[\phi'(G)\phi'(Y_\rho)],
\]
\[
 Q'(\rho)=\alpha E[\phi'(G)\phi'(\sqrt\tau Z+\alpha\phi(G))
                                      \phi'(Y_\rho)].         \tag{25}
\]

Here is the cancellation explicitly. For any bounded smooth \(f\) with bounded derivative,

\[
 \frac d{d\rho}E[f(G)\phi(Y_\rho)]
 =E\left[f(G)\phi'(Y_\rho)
                  \left(G-\frac\rho{\sqrt{1-\rho^2}}V\right)\right].
\]

The \(G\) integration by parts gives \(E[f'(G)\phi'(Y_\rho)]+\rho E[f(G)\phi''(Y_\rho)]\); the \(V\) term cancels the second summand. Take \(f=\phi\) for the first formula and \(f(g)=E_Z\phi(\sqrt\tau Z+\alpha\phi(g))\) for the second. Bounded derivatives justify differentiation and Fubini. The endpoint values follow by dominated convergence. Thus further Gaussian differentiation preserves an exact derivative product, but one derivative is still evaluated at (21)'s shifted argument. This identifies the operation still needing a new identity; it is not an impossibility proof.

## 7. Scope of the established Gaussian/forest identities

The finite conditioning identities in `gaussian_calculus.md`, §§1–2, and `global_nonlinear.md`, §3, peel Gaussian **matrix actions** into Gaussian sources plus the required responses. Equations (3), (6), and (7) are their explicit application here.

The finite forest theorems in `gaussian_calculus.md`, §7.2 and “Finite contraction, observable and physical-loss calculus,” §B, have finite polynomial decorations and finitely many Gaussian edge factors. Their exact finite pairing proofs apply to the polynomial contractions they specify. They do not, as stated, convert the composite tanh in (21) or (20) into finitely many original-activation Gaussian moments. This is a statement about the hypotheses of those results, not a claim that an exact nonpolynomial peeling theorem is impossible.

No argument here infers impossibility from a non-Gaussian intermediate. The completed results are (7), (14)–(17), and the weighted Gaussian identities (23)–(25). The remaining proof obligation is an exact, finite, noncircular transformation of the moments containing (21) and (17)—or even the scalar test (20)—into the stipulated product-only Gaussian normal form, without an activation or likelihood-ratio series. This attempt does not supply that transformation.

## 8. Provenance and claim ledger

Permitted scientific inputs actually read:

- `docs/observable_p1.md`, complete: exact p=1 dictionary, source law, ridge, Gram blocks, raw contraction, Cholesky normalization, and initialized finite equations.
- `docs/NOTATION.md`, complete: populations, actual adjoint, input scaling, readout convention, and distinction between width and closure order.
- `docs/global_nonlinear.md`, §3, including the complete finite source/response and singular-Gram statements; C.4.7.10.B's dictionary construction and (H3.1)–(H3.3); and C.4.7.10.C.1 through the canonical equations (H3.N1)–(H3.N2).
- `docs/gaussian_calculus.md`, introductory §§1–2 and §4, the finite forest portion of §7.2, and the complete finite Gaussian forest evaluation/concentration §B.
- Required process skills: `solve-math-rigorously`, `investigate-conjectures`, its research-contract reference, and its adversarial-audit reference.

No other study, history, author report, competing attempt, maintained code, or external mathematical source was read. No new theorem was attributed to an unread source.

| Claim | Status | Exact boundary |
|---|---|---|
| Canonical reverse source is (3) | Established-source identity, independently specialized | Same reused action and actual adjoint |
| Raw initialized coefficient contraction is (7) | Exact, derived here | Includes \(\tau\gamma\) |
| Circle kernel equals (17) with (14) | Exact, derived here | Canonical p=1 ridge and full population expectations |
| Axis target reduces to (20) | Exact, derived here | \(t_*>0\), no constant feature contribution |
| (24) uses only Gaussian activation arguments | Exact, derived here | Extra exponential density weight remains |
| Strict finite product-only Gaussian normal form | Open in this attempt | No series, no new composite activation, no target-dependent covariance |
| Such a strict finite form is impossible | Not claimed | Non-Gaussian intermediates do not establish this |
| Initialization represents unfiltered \(A_0\) | False as an operator identification | The specified finite closure uses \(Q_2A_0Q_1\) |

This frozen candidate is ready for comparison with independent constructions. The strongest current exact result is the explicit low-dimensional integral (17), not the stronger product-only normal form.
