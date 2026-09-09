# Isolated full mathematical audit of the two-sample short response lemma

Date: 2026-09-06.

**Verdict: PASS. No required repairs.**

This verdict covers the complete short feature-time lemma, including its fixed-program finite realization, equations (1)–(16), and the two actual-query exponential-square bounds, for every fixed finite mesh with \(M\Delta\le 3/2\), every finite \(R_1,R_2\ge1\), both choices of each label, and every \(\rho\in[-1,1]\). It does not certify a global two-sample theorem, clipping removal, a continuous-time construction, or a physical-time comparison.

## 1. Inputs, hashes, and isolation

The only mathematical source documents consulted were:

1. `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md`
   - Read in full: lines 1–352, 14,263 bytes.
   - SHA256: `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170`.
2. `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`
   - Mathematical content read: Section 3 only, lines 258–476, including its four subsections. A heading-location scan was used to locate the section; no mathematical argument from another section was imported. No preceding definitions needed to be read.
   - Whole-file size: 81,999 bytes.
   - Whole-file SHA256: `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`.
   - SHA256 of the exact Section 3 slice, including its heading and trailing blank line, as emitted by `sed -n '258,476p'`: `950273bdf1d6186ffd4b4b7c2524ad0449278912f3d4914934c61f65efaa4bec`.

The dependency hash printed in the candidate agrees exactly with the actual dependency hash. Both source hashes were rechecked after the audit and were unchanged.

The procedural instructions were read directly and completely from `/etc/codex/skills/solve-math-rigorously/SKILL.md`, SHA256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`. They supplied procedure, not mathematical evidence. No previous review, research or contract file, task history, other agent, external source, experiment, simulation, or numerical search was used. The checks below are algebraic and analytic.

References below to candidate lines refer to the first file; references to dependency lines refer only to the permitted Section 3.

## 2. Assumptions and exact finite realization — verified

The activation satisfies

\[
\phi'(z)=\frac1{10(1+z^2)},\qquad
\phi''(z)=-\frac{z}{5(1+z^2)^2}.
\]

Consequently \(0<\phi'\le1/10\) and \(|\phi''|\le1/5\), using \(|z|\le(1+z^2)^2\). For the activation range, the addition formula gives \(\pi/4=\arctan(1/2)+\arctan(1/3)<1/2+1/3=5/6\); therefore \(\pi/20<1/6\) and \(5/6<\phi<7/6\). The clipping assumptions give all of \(\tau_R(0)=0\), \(\tau'_R(0)=1\), \(|\tau_R(q)|\le|q|\), \(|\tau_R|\le2R\), and \(|\tau'_R|\le1\).

The Gram matrix \(C\) has eigenvalues \(1+\rho\) and \(1-\rho\), so the specified bottom Gaussian tuples exist, including both singular endpoint cases. The readout is exactly zero initially, as required for the base case; it is not a centered but nonzero random initialization.

To verify candidate lines 75–108, fix \(M,\Delta,R_1,R_2\) and write the finite update as

\[
W_k^{(\ell)}=W_0^{(\ell)}+
\frac{\Delta}{2n}\sum_{r<k,b}y_b
\delta_{rb}^{(\ell)}(h_{rb}^{(\ell-1)})^T.
\]

Multiplying on the right by the current forward input gives exactly

\[
W_k^{(\ell)}h_{ka}^{(\ell-1)}
=W_0^{(\ell)}h_{ka}^{(\ell-1)}+
\frac\Delta2\sum_{r<k,b}y_b\delta_{rb}^{(\ell)}
\frac{\langle h_{rb}^{(\ell-1)},h_{ka}^{(\ell-1)}\rangle}{n}.
\]

Taking the transpose action on the current reverse input instead gives

\[
(W_k^{(\ell)})^T\delta_{ka}^{(\ell)}
=(W_0^{(\ell)})^T\delta_{ka}^{(\ell)}+
\frac\Delta2\sum_{r<k,b}y_b h_{rb}^{(\ell-1)}
\frac{\langle\delta_{rb}^{(\ell)},\delta_{ka}^{(\ell)}\rangle}{n}.
\]

Thus both learned coefficients in (2) have the correct factor \(\Delta/2\), the correct historical label \(y_b\), and the strict time restriction \(r<k\). They involve uncentered second moments. There is no extra label multiplying an initial-matrix source derivative and no factor \(1/2\) in that derivative response.

Section 3's initial-matrix response rule supplies the other terms in (2). For a forward action, only past reverse inputs are available, giving \(r<k\). Both current sample forward fields are computed before reverse queries; hence the reverse response includes both samples with \(r\le k\). Processing a second same-direction query at the current time changes the within-group Gaussian covariance, but does not create an additional opposite-direction response term. The simultaneous Euler convention in the candidate therefore matches these coefficients exactly.

The hypotheses of the fixed-program result apply:

- There are the required three populations, two independent Gaussian initial matrices with entry variance \(1/n\), and iid bottom root tuples across neurons. The two samples within a tuple need not be independent.
- At fixed caps, the bottom increment and middle gate are globally Lipschitz \(C^1\) coordinate functions. For example, the two partial derivatives of \(\phi'(z)\tau_R(q)\) are bounded by \(2R/5\) and \(1/10\).
- The readout obeys the deterministic bound \(|W_k^{(4)}|\le a k\Delta\le aS\). Replacing the readout argument of the top gate by a smooth bounded function equal to the identity on a neighborhood of this interval gives a globally Lipschitz \(C^1\) instruction with the same values and first derivatives at all attained states.
- After unrolling the learned matrices, only finitely many empirical inner products must be restored. For bounded normalized vector norms, an inner-product discrepancy is bounded by the sum of the two vector discrepancies times the corresponding norms. Multiplication by a convergent scalar coefficient obeys the analogous bound. Finite Lipschitz induction therefore restores these contractions from their limits.

This verifies identification of the stated finite Euler scheme at each fixed mesh and fixed pair of caps. The bounds later proved for the scalar law are uniform in those choices; the finite-width convergence argument is not asserted to be uniform in a number of queries growing with width.

## 3. Audit of the permitted Gaussian dependency and singular derivatives — verified

The conditional projection in dependency (3.3) satisfies both constraints \(WV=Y\) and \(W^TU=Q\): the compatibility identity \(U^TY=Q^TV\) supplies the overlapping part, and the residual is \(P_{U^\perp}\widetilde W P_{V^\perp}\). With an adaptive transcript, the next input is already measurable before its matrix observation. Applying this conditional Gaussian projection successively is valid, and the two residual matrices remain conditionally independent. Thus adaptation does not justify replacing a reused matrix by an independent matrix, and the dependency does not make that replacement.

For a new forward input, its residual component \(h_\perp\) is orthogonal in the limiting second-moment inner product to all old forward inputs. Consequently the old-forward part of each reverse answer has zero contraction with \(h_\perp\). Gaussian integration by parts gives

\[
\mathbb E[\zeta h_\perp]
=\Gamma_U\left(
\mathbb E\nabla_\zeta h-\sum_r\alpha_r\mathbb E\nabla_\zeta v_r
\right).
\]

In the positive-definite case this identifies the coefficient \(\beta\) in dependency (3.4). Substituting the old forward decompositions cancels the projected derivative terms and leaves exactly

\[
\xi_h+\sum_s u_s\,\mathbb E\partial_{\zeta_s}h.
\]

The new source is \(\sum_r\alpha_r\xi_r+\sigma G\), where \(\sigma^2=\mathbb E h_\perp^2\). Its covariance with old forward sources is \(\mathbb E[h v_r]\), and its variance is \(\mathbb E h^2\). This verifies the full uncentered covariance rule and the independence of distinct source groups. The reverse orientation uses the same calculation.

The empirical induction is sufficient for this application. The discarded Gaussian projection has normalized mean-square size equal to its fixed rank divided by \(n\), times a bounded-in-probability variance multiplier. The conditional bounded-test variance and second-moment variance estimates in dependency lines 355–373 tend to zero. Joint weak convergence together with convergence of the squared norm makes quadratic tails uniformly integrable: subtract the converging integrals of \(\min(\|x\|^2,L)\) from the converging total second moments, then let \(L\) increase. Hence the required continuous quadratic-growth contractions converge. No independence between reused coordinate values is assumed in this argument.

For completeness, the elementary matrix-norm tightness used in Section 3's perturbation comparison does not require importing another section. Take a \(1/4\)-net of each unit sphere with at most \(9^n\) elements. For fixed unit vectors \(u,v\), \(u^TWv\sim N(0,1/n)\), and the net approximation gives \(\|W\|\le2\max_{u,v}|u^TWv|\). Thus

\[
\mathbb P(\|W\|>8)\le2\,9^{2n}e^{-8n}\longrightarrow0.
\]

The normalized squared norm of a fresh Gaussian input noise has mean one and variance \(2/n\). These facts provide the bounded-norm events needed for the finite \(O(\epsilon)\) perturbation comparison in dependency lines 441–447.

At a singular source covariance, write \(\zeta=LG\) with \(G\) standard Gaussian and \(LL^T=\Gamma\). Conditioning on the independent other groups, componentwise Gaussian integration by parts yields

\[
\mathbb E[\zeta f(\zeta)]
=L\mathbb E[Gf(LG)]
=LL^T\mathbb E\nabla f(\zeta)
=\Gamma\mathbb E\nabla f(\zeta).
\]

The derivatives here are ambient derivatives of the complete displayed expression with deterministic parameters fixed. They are not derivatives of a version simplified on the support of the Gaussian law. At fixed caps and finite query count, the coordinate expressions have bounded first derivatives after the extensions above, so the integration by parts is integrable.

Section 3.4 correctly removes the positive-definiteness restriction. Fresh input noise of size \(\epsilon\) makes every new same-direction Gram Schur complement at least \(\epsilon^2\). The finite comparison is \(O(\epsilon)\) on the bounded-norm events. On the scalar side, the finite causal derivative recursion gives bounded coefficients and derivatives on compact parameter sets; continuity of covariance square roots, continuity of the \(C^1\) derivatives, and dominated convergence give convergence as \(\epsilon\to0\). No convergence of inverse singular Grams is needed. If \(v\in\ker\Gamma\) and \(\Gamma=\mathbb E[uu^T]\), then \(\mathbb E(u^Tv)^2=0\); hence any null-space change of response coefficients contracts to zero with the response inputs.

In particular, the zero-time convention in candidate lines 130–140 is correct. Although \(\zeta^{(2)}_{0a}=0\) almost surely,

\[
\delta^{(2)}_{0a}
=\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a})
\]

must remain the formal expression. Its forward-source derivative vanishes on the attained law, while

\[
\partial_{\zeta^{(2)}_{0a}}\delta^{(2)}_{0a}
=\phi'(\xi^{(2)}_{0a})>0
\]

there. The readout and \(\delta^{(3)}_0\) vanish as formal expressions, so \(B^{(3)}_0=0\); the attained vanishing forward derivatives of \(\delta^{(2)}_0\) give \(B^{(2)}_0=0\). This proves \(U_0=V_0=0\) without deleting any source slot. Perfect sample correlation does not merge the two formal slots either.

## 4. Causal construction and simultaneous induction — verified

The scalar law is constructible in the order asserted. The current bottom fields use only past bottom queries. Their law and reverse-source derivatives determine \(A^{(2)}\) and the current forward source covariance for layer 2. This constructs \(Z^{(2)}\), then \(A^{(3)}\), the current layer-3 forward covariance, and \(Z^{(3)}\). The readout uses only past top features, so the current \(\delta^{(3)}\), \(B^{(3)}\), and reverse covariance for \(\zeta^{(2)}\) are then available. Finally one constructs \(q^{(2)},\delta^{(2)},B^{(2)}\), and the current \(\zeta^{(1)}\).

Each covariance extension is a matrix of second moments of inputs whose laws have already been constructed, so it is positive semidefinite. Its coefficients are deterministic. Correlation with earlier slots within that source group is retained; no current covariance parameter has to be solved by a self-consistency equation.

The induction carries the full previously proved conclusions, including \(V_r\le V_*:=3067/3200\), not just their weaker consequences \(U_r,V_r\le1\). Candidate lines 290–291 explicitly retain this stronger information. The steps are:

1. Past \(U,V\le1\) bound the bottom sensitivities and the current \(A^{(2)}\).
2. Past \(V\le1\) bounds the current middle forward sensitivities and \(A^{(3)}\).
3. These forward coefficients bound the current top response \(V_k\le V_*\).
4. That current bound and the already established past \(V_r\le V_*\) give the current and past sharpened \(q^{(2)}\) norms.
5. Those norms and the middle derivative estimate bound the current \(U_k\).

No step needs the current \(U_k\) before step 5. The current \(V_k\) appears in the middle return derivative only after step 3 proves its bound. The use of the full earlier conclusions is ordinary simultaneous induction and requires no amendment to the candidate.

## 5. Raw bottom derivative, including cross-input gates — verified

Fix a single source slot \(\zeta^{(1)}_{sb}\), and let \(d\) denote its formal derivative. For each update sample \(c\), the complete derivative is

\[
d[\phi'(Z^{(1)}_{rc})\tau_{R_1}(q^{(1)}_{rc})]
=\phi''(Z^{(1)}_{rc})\tau_{R_1}(q^{(1)}_{rc})dZ^{(1)}_{rc}
+\phi'(Z^{(1)}_{rc})\tau'_{R_1}(q^{(1)}_{rc})dq^{(1)}_{rc},
\]

with

\[
dq^{(1)}_{rc}
=\mathbf1_{(r,c)=(s,b)}+
\sum_{v\le r,c'}B^{(2)}_{rc,vc'}\phi'(Z^{(1)}_{vc'})dZ^{(1)}_{vc'}.
\]

Both terms in the raw gate derivative are therefore present. In particular, the term involving \(\phi''\tau\) is evaluated at the update sample \(c\); it cannot be discarded or replaced by a same-output-sample gate when \(C_{ac}\ne0\).

All derivatives \(dZ^{(1)}_{vc}\) vanish for \(v\le s\). The single direct injection into any later output has size at most \(\Delta/20\). For the propagated contribution, the full cross-input coefficient satisfies

\[
\frac12\sum_c|C_{ac}y_c|=\frac{1+|\rho|}{2}\le1.
\]

Writing \(D_j=\max_{v\le j,c}|dZ^{(1)}_{vc}|\), the resulting comparison for \(j>s\) is

\[
D_j\le\frac\Delta{20}+
\Delta\sum_{s<r<j}
\left(\frac{\max_c|q^{(1)}_{rc}|}{5}+\frac{U_r}{100}\right)D_r.
\]

The comparison sequence with equality has successive multiplier \(1+c_r\), so its product is bounded by \(\exp(\sum c_r)\). Adding unused nonnegative early terms to the exponent and multiplying by the final activation derivative gives exactly

\[
|\partial_{\zeta^{(1)}_{sb}}H^{(1)}_{ja}|
\le\frac\Delta{200}E^{(1)}_j.
\]

Thus (6) contains the correct single-slot injection, both sample interactions, and the full raw-coordinate gate derivative.

For past times, Minkowski's inequality and \(V_r\le1\) give

\[
\|q^{(2)}_{ra}\|_2\le\frac{aS}{10}+a\le\frac{161}{120}=Q_0,
\qquad
\operatorname{Var}(\zeta^{(1)}_{ra})\le(Q_0/10)^2.
\]

Here the covariance definition and \(|\delta^{(2)}|\le|q^{(2)}|/10\) justify the second statement. Also \(\max_a|q^{(1)}_{ra}|\le\max_a|\zeta^{(1)}_{ra}|+a\). Neither norm estimate uses independence of the Gaussian source and its response shift.

## 6. Gaussian maxima and time correlations — verified

For any centered Gaussian pair, with no restriction on correlation and individual variances at most \(v\), and \(\lambda\ge0\),

\[
e^{\lambda\max_a|G_a|}\le\sum_a e^{\lambda|G_a|},
\qquad
\mathbb E e^{\lambda|G_a|}
\le\mathbb E(e^{\lambda G_a}+e^{-\lambda G_a})
\le2e^{\lambda^2v/2}.
\]

This proves (7), including variance zero and correlations \(\pm1\). The factor four is correct.

For \(j\ge1\), put \(t=j\Delta\). The precise time-Jensen step, for any random variables \(X_r\), is

\[
\exp\left(c\Delta\sum_{r<j}X_r\right)
=\exp\left(\frac1j\sum_{r<j}ctX_r\right)
\le\frac1j\sum_{r<j}e^{ctX_r}.
\]

It imposes no independence in time. Applying the same marginal bound to every summand and using \(t\le S\) proves (8) and (12). When \(j=0\), the exponentials equal one and their stated bounds hold directly.

For the bottom exponential, the maximal exponent is exactly

\[
\frac{73}{200}+\frac9{200}\left(\frac{161}{1200}\right)^2
=\frac{11705921}{32000000}<\frac25.
\]

Consequently \(\mathbb E E^{(1)}_j<6\), and

\[
|A^{(2)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{50}\right)
=\frac\Delta2\frac{1279}{900}
<\frac\Delta2\frac32.
\]

The margin inside the parentheses is \(71/900\).

## 7. Middle sensitivities and the second forward coefficient — verified

For a forward-source derivative, \(\zeta^{(2)}\) is held fixed. The chain rule therefore gives exactly candidate lines 219–222. Summing the absolute derivatives over all forward slots gives the direct term one in each row, since only the row's own current \(\xi^{(2)}_{ja}\) has a direct derivative. With \(\overline R_r=\max_{v\le r}R_v\),

\[
R_j\le1+A\Delta\sum_{r<j}
\left(\frac{\max_a|q^{(2)}_{ra}|}{5}+\frac{V_r}{100}\right)\overline R_r.
\]

The two update samples turn \(A\Delta/2\) into \(A\Delta\). The row sum over source slots does not contribute another factor two to the direct term. Product-form Gronwall proves (10).

For one reverse source \(\zeta^{(2)}_{sb}\), the direct term in \(d\delta^{(2)}_{sb}\) is at most \(1/10\). Multiplying by a forward coefficient gives a single injection at most \(A\Delta/20\). The subsequent comparison has the same coefficients as above. Multiplying by the final activation derivative yields \(A\Delta E^{(2)}_j/200\), proving (11).

Because \(|\delta^{(3)}|\le aS/10\le7/40\), every middle reverse Gaussian has variance at most \(49/1600\). The argument of Section 6, applied to \((E^{(2)}_j)^p\), gives

\[
\mathbb E(E^{(2)}_j)^p
\le4\exp\left\{
pAS\left(\frac a5+\frac1{100}\right)
+\frac12\left(\frac{pAS}{5}\right)^2\frac{49}{1600}
\right\}
\le4e^{219p/400+3969p^2/1280000}.
\]

The coefficient of \(p^2\) is therefore correct. At \(p=1\) the exponent is \(704769/1280000<3/5\), which gives \(\mathbb E E^{(2)}_j<8\). At \(p=2\), taking the square root gives

\[
\|E^{(2)}_j\|_2
\le2\exp\left(\frac{354369}{640000}\right)<\frac72,
\qquad
\frac59-\frac{354369}{640000}=\frac{10679}{5760000}>0.
\]

Thus (13) has the correct square-root operation and exponent. Equations (11)–(12) imply

\[
|A^{(3)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{25}\right)
=\frac\Delta2\frac{1333}{900}
<\frac\Delta2\frac32.
\]

The claimed strict margin is \(17/900>0\).

## 8. Current top response and current middle response — verified

Let \(D^{(3)}_j\) denote the maximum total absolute forward-source derivative row of \(\delta^{(3)}_j\), and let \(T_j\) be as in the candidate. Differentiating the readout contributes

\[
\frac1{10}\frac\Delta2\sum_{r<j,b}\frac1{10}T_r
=\frac\Delta{100}\sum_{r<j}T_r.
\]

Differentiating the top gate contributes at most \(aS T_j/5\). Therefore

\[
D^{(3)}_j\le\frac\Delta{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
\le\frac{73}{300}S\max_{v\le j}T_v.
\]

The strict-past forward recursion and the bound for \(A^{(3)}\) then give

\[
\max_{v\le j}T_v\le e^{A(73/300)S^2}
\le e^{657/800}<\frac52.
\]

Moving the absolute value inside the expectation in each response coefficient bounds its entire row by \(\mathbb E D^{(3)}_k\). The learned row contributes at most

\[
\frac\Delta2\sum_{r<k,b}
\|\delta^{(3)}_{ka}\|_2\|\delta^{(3)}_{rb}\|_2
\le\frac{a^2S^3}{100}.
\]

It follows that

\[
V_k\le\frac{73}{300}S\frac52+\frac{a^2S^3}{100}
\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}=V_*<1.
\]

This is a current-time bound. It gives, without any current bottom response bound,

\[
\|q^{(2)}_{ka}\|_2\le\frac7{40}+\frac76V_*
=\frac{24829}{19200}=Q_*.
\]

The already completed induction steps give the same bound at all past times.

For the current middle derivative, the \(r=k\) terms in the return must be retained. The exact row estimate is

\[
\sum_{s\le k,b}|\partial_{\xi^{(2)}_{sb}}\delta^{(2)}_{ka}|
\le\left(\frac{|q^{(2)}_{ka}|}{5}+\frac{V_k}{100}\right)E^{(2)}_k.
\]

Cauchy–Schwarz applies even though \(q^{(2)}_{ka}\) and \(E^{(2)}_k\) may be correlated. Using also \(\mathbb E E^{(2)}_k\le\|E^{(2)}_k\|_2\), its expected value is at most

\[
\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right).
\]

The learned bottom-response row is bounded by

\[
\frac\Delta2\sum_{r<k,b}
\|\delta^{(2)}_{ka}\|_2\|\delta^{(2)}_{rb}\|_2
\le\frac{S}{100}Q_*^2\le\frac3{200}Q_*^2.
\]

All factors, including the two samples and the exclusion of \(r=k\) from the learned term, are correct. Exact arithmetic gives

\[
\frac{Q_*}{5}+\frac{V_*}{100}=\frac{257491}{960000},
\qquad Q_*^2=\frac{616479241}{368640000},
\]

\[
U_k\le\frac{1802437}{1920000}
+\frac{1849437723}{73728000000}
=\frac{71063018523}{73728000000}<\frac{97}{100}<1.
\]

The first numerator after conversion to the common denominator is \(69213580800\). The margin below \(97/100\) is exactly

\[
\frac{453141477}{73728000000}>0.
\]

This verifies the stated large rational number and closes the simultaneous induction.

## 9. Remaining exponential comparisons and both query tails — verified

All exponential comparisons used above admit the exact elementary certificates claimed in the candidate. The series of \(e\) through degree five, followed by a geometric tail estimate starting at degree six, gives

\[
e<\frac{163}{60}+\frac7{4320}
=\frac{11743}{4320}<\frac{68}{25}<\frac{11}{4}<3.
\]

For the three more delicate comparisons:

- \((11/4)^2<(3/2)^5\) reduces to \(242<243\), giving \(e^{2/5}<3/2\).
- \(3^3<2^5\) is \(27<32\), giving \(e^{3/5}<2\).
- \((68/25)^5<(7/4)^9\) reduces to
  \(381139961249792<394078193359375\), giving \(e^{5/9}<7/4\).

For the top estimate, \(657/800<5/6\) has margin \(29/2400\), and

\[
3^5\,2^6=15552<15625=5^6
\]

gives \(e^{5/6}<3^{5/6}<5/2\). These are strict analytic comparisons, not decimal approximations.

For each \(j\in\{1,2\}\), each time, and each sample, the full query is

\[
q^{(j)}=\zeta^{(j)}+\beta^{(j)},\qquad |\beta^{(j)}|\le a,
\]

because both response row sums are below one. The two variance bounds are

\[
\operatorname{Var}(\zeta^{(2)})\le\frac{49}{1600},\qquad
\operatorname{Var}(\zeta^{(1)})\le\left(\frac{24829}{192000}\right)^2
<\left(\frac7{40}\right)^2.
\]

For the strict comparison, \(24829<33600\). There is no independence requirement on \(\beta^{(j)}\) and \(\zeta^{(j)}\). The pointwise inequality \(q^2\le2\zeta^2+2a^2\) and the one-dimensional Gaussian integral give

\[
\mathbb E e^{q^2/16}
\le e^{a^2/8}\mathbb E e^{\zeta^2/8}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]

The Gaussian integral is finite since \(49/6400<1\); at variance zero its value is one. The last comparison can be checked without any approximate evaluation:

\[
\frac{49}{288}<\frac15,\qquad
e^{1/5}\le\sum_{r\ge0}(1/5)^r=\frac54,\qquad
1-\frac{49}{6400}=\frac{6351}{6400}>\frac9{16}.
\]

Thus the displayed expectation is strictly less than \((5/4)(4/3)=5/3<2\). This proves (5) for both \(q^{(1)}\) and \(q^{(2)}\), including dependence of each shift on its source. It also controls either sign of either query: for \(t>0\), Markov's inequality gives

\[
\mathbb P(|q^{(j)}|\ge t)<2e^{-t^2/16},
\]

and hence the same upper bound for each of the events \(q^{(j)}\ge t\) and \(q^{(j)}\le-t\). This is a marginal estimate uniform over mesh slots; no mesh-uniform maximum-over-time tail is claimed.

## 10. Boundary cases, scope, and required repairs

The case \(M=0\) has \(S=0\), empty update sums, \(U_0=V_0=0\), zero actual reverse queries, and exponential moments equal to one. The forward coefficient claim is then vacuous. For \(M\ge1\), the Jensen argument uses only positive \(j\Delta\le S\), so no division by zero or hidden small-mesh assumption occurs. All propagated exponents have nonnegative summands.

The calculations use \(|y_b|=1\), \(|C_{ab}|\le1\), and the full row sum \((1+|\rho|)/2\le1\). They therefore include common and opposite labels, \(\rho=-1\), \(\rho=1\), cancellation of the readout, and any singular source covariances generated later. No positivity of a Gram inverse is used after the dependency's perturbation is removed. Constants in the response and tail estimates contain neither clipping radius.

The final scope discussion, candidate lines 327–352, is conditional and does not enlarge the proved lemma. In particular, a label-mode lower bound \(g'\ge m^2\), if established for a correctly constructed uncut common-label flow with \(g(0)=0\), gives the stated hitting-time bound \(1/m^2=36/25<3/2\). That arithmetic is correct. The candidate explicitly leaves the construction, symmetry and gradient premises, clipping removal, physical comparisons, and opposite-label continuation outside this result. None is needed for the short fixed-program response lemma audited here.

**Required repairs: none. Final verdict: PASS for the stated short feature-time lemma and its fixed-program identification.**
