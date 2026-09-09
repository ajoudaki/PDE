# Independent adversarial mathematical review

Review date: 2026-09-06.

**Verdict: REQUIRED REPAIR — one minor mathematical overstatement at candidate line 459.** The numbered response identities, the second-update covariance calculation and weighted test, and the complete transferred short-interval absolute bootstrap pass within the stipulated finite Gaussian law. The required correction does not change those results or their constants. An unqualified PASS for every sentence of the exact candidate would overlook the explicit first-update counterexample below.

Candidate reviewed: [SHIFTED_HARMONIC_CAUSAL_RESPONSE.md](/tmp/l3-two-sample-proof-DLuelg/SHIFTED_HARMONIC_CAUSAL_RESPONSE.md).

Exact candidate SHA256:

    f307c71a0f704ae139929d8e3d512e6dd8dc9bf3eeda1f9ee12d6da2354ac4ff

Mathematical dependency reviewed: [TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md](/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md).

Exact dependency SHA256:

    9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170

Both hashes were checked again after the mathematical audit and were unchanged. The candidate has 876 lines; the dependency has 352 lines. References below use **C** for the candidate and **P3** for this dependency, with line numbers referring to these exact bytes.

## 1. Scope and source isolation

I read both specified files completely. I read no other project, mathematical, history, ledger, review, or skill file, retrieved no external source, spawned no agents, and ran no experiments. The candidate was not edited.

As instructed, C (4)–(6), lines 115–173, are the specified finite Gaussian law. In particular, the mutually independent Gaussian source groups, their within-group covariances, and the expected formal derivatives defining the deterministic coefficients are premises of this review. They are not conclusions that this candidate must derive from a finite network.

Accordingly, this review does not certify the finite-width identification assertions or external dependencies described in P3 lines 6–10 and 75–108. It also does not certify agreement with an unread contract, the history of earlier routes, or the historical provenance statements in C lines 11–14 and 33–62. This is a scope boundary, not a missing proof charged against the candidate.

The dependency digest at C line 42 exactly matches the file actually reviewed. That digest fixes the mathematical dependency for this review. The other source digests in C lines 40–54 are reported historical read hashes. I did not inspect those sources or compare their current hashes. A subsequent change in a live ledger would not by itself invalidate the mathematical dependency or establish a defect here.

The distinction between the zero scalar readout root and the finite-width initialization is explicit at C lines 64–71. Nothing below promotes the former into an identification theorem for the latter.

## 2. Required correction: a residual need not be nonzero at a later time

**Location:** C lines 452–459, specifically “At later times neither vanishes” at line 459.

**Severity:** minor but literal mathematical overstatement. It is unnecessary for the main argument.

The top initial delta vanishes as a formal expression:

\[
w_0=0,\qquad \delta^{(3)}_{0b}=0.
\]

Consequently, independently of whether the coefficients \(A^{(3)}_{1b,0c}\) vanish,

\[
Z^{(3)}_{1b}=\xi^{(3)}_{1b}
\]

as a formal expression. For every deterministic top source direction \(v\),

\[
P^{(3)}_{1b}=v^{\xi^3}_{1b}
\]

is deterministic. Thus

\[
\mathcal C_{1b}(v)
=\operatorname{Cov}(w_1h^{(3)}_{1b},v^{\xi^3}_{1b})=0.
\]

The covariance operator is therefore identically zero at time 1, including for a source impulse injected at time 0. This is stronger than the existence of a specially chosen direction with zero covariance.

For the explicit impulse \(v=e_{0a}\), the candidate's value equalities give

\[
P^{(3)}_{1a}=0,\qquad
\mathcal C_{1a}(e_{0a})=0,\qquad
\mathcal T_{1a}(e_{0a})
=\lambda y_a\mathbb E[\gamma(U_a)^2]\ne0.
\]

The last expectation is positive because \(U_a\) is a Gaussian with positive variance and the zeros of \(\gamma\) are discrete. No singular-slot identification is used in these derivatives.

**Required replacement:** “At later times these terms need not vanish and cannot in general be discarded; the covariance can first become nonzero at the second update, as shown below.”

This correction is consistent with C Section 6 and does not weaken its counterexample to the proposed mean factorization. I found no other required mathematical repair within the requested scope.

## 3. Normalization, causal construction, and formal differentiation

**C lines 64–111 and 115–190; P3 lines 19–73 and 130–149: PASS within the stated setup.**

The elementary activation identities are correct:

\[
h=\varepsilon(\sin z+\cos z),\quad
\gamma=\varepsilon(\cos z-\sin z),\quad
h'=\gamma,\quad \gamma'=-h,\quad
h^2+\gamma^2=2\varepsilon^2=1/200.
\]

Hence \(|h|,|\gamma|,|\phi''|\le b=\sqrt2/20\), and
\(5/6<1-b\le\phi\le1+b<7/6\). These supply all of the stated absolute bounds.

Given the physical velocities written in C lines 73–76 and \(r_a=y_a(g-1)\), division by \(4(1-g)\) gives a factor \(y_a/2\). Thus the feature-step normalization \(\lambda=\Delta/2\), including the matrix factor \(1/n\), is consistent. This checks the displayed conversion; it does not derive the stipulated physical metric from an unread contract.

Strict past-time dependence in \(A\), together with the order of forward fields and reverse queries, prevents a same-time circular solve. In particular, \(H^{(2)}_k\) is available before constructing the time-\(k\) top Gaussian source and its delta, and the current \(B^{(3)}\) row is available before \(q^{(2)}_k\) and \(B^{(2)}_k\). The latter does not enter the already constructed bottom field \(Z^{(1)}_k\).

The convention at C lines 167–173 is essential and is applied consistently: partial derivatives act on the finite coordinate maps while their selected deterministic coefficients and covariance parameters are fixed. A Gaussian coordinate of zero variance still has a formal derivative. Almost-sure equality between two coordinates does not identify their ambient partial derivatives.

For example, at time zero,

\[
q^{(2)}_{0a}=\zeta^{(2)}_{0a},\qquad
\delta^{(2)}_{0a}
=\gamma(\xi^{(2)}_{0a})\tau_2(\zeta^{(2)}_{0a}).
\]

The attained value is zero, and its forward-source derivative is zero on the law. Its own reverse-source derivative is \(\gamma(\xi^{(2)}_{0a})\), which must be retained. C lines 712–723 correctly replace the strict positivity assertion in P3 lines 137–140 by this unsigned identity. In contrast, the top \(\delta^{(3)}_0\) is identically zero even as a formal expression, because \(w_0\) is the empty sum. This distinction also proves the finding in Section 2 of this review.

The integrability assertion at C lines 175–182 is sufficient. At fixed finite caps, the finite recursion has bounded gates and cut factors, and finite first derivatives. In the uncut case each query is its Gaussian coordinate plus a bounded feature sum with finite deterministic coefficients; finite differentiation gives polynomial bounds in the absolute Gaussian coordinates. Causal induction supplies finite moments for the next coefficients. This establishes finite-prefix integrability without any uniform bound in the number of slots.

No Gaussian integration by parts, inverse covariance, or nonsingular historical Gram is needed for these steps.

## 4. Sample symmetry

**C lines 192–225: PASS.**

Under sample exchange, \(y_{\pi b}=-y_b\) and \(C_{\pi a,\pi b}=C_{ab}\). The bottom update is preserved because the odd cut changes sign along with the reverse field. The readout changes sign, the forward features exchange, and both delta populations and reverse queries undergo the stated signed exchange.

The derivative term in \(A\) has an unsigned output and a signed source; the derivative term in \(B\) has a signed output and an unsigned source. Both therefore acquire the required minus sign under simultaneous sample exchange. The learned terms have the same transformation: their two-field products are unchanged in sign, while \(y_b\) changes sign. This verifies

\[
A_{\pi i,\pi j}=-A_{i,j},\qquad
B_{\pi i,\pi j}=-B_{i,j}.
\]

Each source covariance is invariant under its appropriate signed permutation. A centered Gaussian law, including a singular one, is determined by that covariance; no positive definiteness is required for this symmetry argument. Induction in the stated causal order therefore gives

\[
\mathbb Ew_k=0,\qquad f_{k2}=-f_{k1},\qquad
f_{ka}=y_ag_k,\qquad \mathbb E[w_kh^{(3)}_{ka}]=f_{ka}.
\]

The distinction at C lines 223–225 between deterministic population predictions and a finite realization's two predictions is correct.

## 5. Complete source variations and both trained matrix actions

**C lines 227–298, 318–343, 403–448, and 461–507: PASS, subject to the wording correction already identified.**

Differentiating \(\gamma(Z)\tau(q)\) gives precisely

\[
-h(Z)\tau(q)P+\gamma(Z)\tau'(q)Q.
\]

This checks the bottom update in (9), the middle delta in (10), and the signs in (14). Differentiating \(w_k\gamma(Z^{(3)}_i)\) gives

\[
\gamma^{(3)}_iu_k-w_kh^{(3)}_iP^{(3)}_i,
\]

with the full accumulated readout variation
\(u_k=\lambda\sum_{r<k,b}y_b\gamma^{(3)}_{rb}P^{(3)}_{rb}\).
There is no omitted readout derivative.

All reverse sums include the current row, and all forward feedback sums are strictly historical. Thus (9)–(11) retain each return allowed by (4). The deterministic closure (12) also retains both \(A^{(2)}\) and \(A^{(3)}\), and both learned transpose covariance additions in \(B^{(2)}\) and \(B^{(3)}\). Holding these selected statistics fixed during a source derivative does not remove the learned actions already present in them.

For the expected top response, the exact decomposition is

\[
\mathbb E[w_kh_iP_i]
=f_i\,\mathbb EP_i+\operatorname{Cov}(w_kh_i,P_i).
\]

Together with \(x=v+A^{(3)}r\), this gives (19) and

\[
(I+FA^{(3)})D^{(3)}=-F+\mathcal T-\mathcal C.
\]

The order \(FA^{(3)}\) in (20) is correct. The readout term retains
\(\mathbb E[\gamma_i\gamma_jP_j]\); replacing it by a product of expectations would require a further argument absent here.

The map \(v\mapsto x=(I+A^{(3)}D^{(3)})v\) is a finite lower-triangular map with identity diagonal, since \(A^{(3)}\) is strictly past-time and \(D^{(3)}\) is causal. Thus the invertibility claim at C lines 455–457 is correct, including for a singular source covariance when working in the stipulated formal coordinates.

Multiplication by \(\omega_i y_ax_i\) gives (21) because \(y_af_i=g_k\). It does not assert that this label multiplication defines a positive metric.

At the middle, (22) is the exact expectation/covariance decomposition with
\(X_i=h_i^{(2)}\tau_2(q_i^{(2)})+f_i\kappa_i\).
Multiplying (14) by \(y_aP_i^{(2)}\) and taking expectations gives (23). Both the mixed query term and the historical \(B^{(3)}\) term remain. The auxiliary random-sensitivity quadratic identity is not substituted for a deterministic-response norm estimate.

Finally, substitution of \(P_i=v_i+\sum_{j\prec i}A_{i,j}T_j\) into its covariance gives (24). The deterministic \(v_i\) has zero covariance. The statistic \(\mathcal K\) in (35) enters \(\mathcal C\) with coefficient \(-A^{(3)}_{i,j}\), and hence enters the residual \(-\mathcal C\) with coefficient \(+A^{(3)}_{i,j}\). This sign agrees with the second-update calculation.

## 6. Current blocks, absolute bound, and signed finite sum

**C lines 302–399: PASS.**

For a current top source slot, \(w_k\) and all past fields have zero derivative, while
\(\partial_{\xi^{(3)}_{kb}}Z^{(3)}_{ka}=\mathbf1_{a=b}\).
Since the learned part of \(B\) excludes \(r=k\),

\[
B^{(3)}_{ka,kb}
=-\mathbf1_{a=b}\mathbb E[w_kh^{(3)}_{ka}]
=-\mathbf1_{a=b}f_{ka}.
\]

This is an entry of the actual specified coefficient matrix, not a derivative after collapsing coincident source values.

The same-time reverse contribution to the middle variation is
\(-f_i(\gamma_i^{(2)})^2\tau'_2(q_i^{(2)})P_i^{(2)}\).
Consequently (14) and the diagonal current-middle formula (15) follow. The term
\(-\mathbb E[h_i^{(2)}\tau_2(q_i^{(2)})]\) is not removed by the top readout's zero mean. The nonnegativity of \(\kappa_i\) uses a square and \(\tau'_2\ge0\), not a positive gate.

With \(V_k=(H^{(3)}_{k1}-H^{(3)}_{k2})/2\), the constant shift cancels, so
\(|V_k|\le b\) and \(w_{k+1}=w_k+\Delta V_k\). Hence

\[
|w_k|\le bs_k,\qquad
|f_{ka}|\le b^2s_k=s_k/200.
\]

The diagonal current top block therefore has operator norm at most \(s_k/200\), and its query contribution has absolute value at most \(as_k/200\), as asserted.

Symmetry gives \(\mathbb E[w_kV_k]=(f_{k1}-f_{k2})/2=g_k\). The exact update-square identity is

\[
\mathbb Ew_{k+1}^2-\mathbb Ew_k^2
=2\Delta g_k+\Delta^2\mathbb EV_k^2.
\]

Summation proves both identities in (17), including the sign of the Euler defect. The estimates \(\mathbb Ew_M^2\le b^2S^2\) and
\(\Delta^2\sum_{k<M}\mathbb EV_k^2\le b^2S\Delta\) give (18).
Although the sharper lower bound explicitly contains \(\Delta\), it is uniformly bounded in the mesh: for \(M\ge1\), \(\Delta\le S\); \(M=0\) is trivial.

The continuous readout identity is correctly conditional on an already constructed path and passage of expectations to the limit. The assertion \(g'\ge0\) is likewise restricted to a genuine uncut gradient feature flow. The finite Gaussian Euler law and its cut references have not thereby been shown to have \(g_k\ge0\).

In particular, when \(g>0\), the unweighted two-sample block \(\operatorname{diag}(-g,g)\) is not negative semidefinite. The candidate correctly confines the damping interpretation to the specified label-weighted expression.

## 7. Second-update calculation and its analytic limit

### 7.1 Value identities versus derivatives

**C lines 515–563: PASS.**

Initial attained deltas and queries vanish. The first bottom update is zero; the lower-feature equalities then imply equality of the time-0 and time-1 forward Gaussian sources in mean square by (5). The zero attained past deltas give
\(Z^{(\ell)}_{1a}=Z^{(\ell)}_{0a}\) for every hidden layer.
Thus \(w_1=\lambda D\) and \(w_2=2\lambda D\) hold as value identities.

For \(v=e_{1a}\), however, the uncollapsed formal equations give

\[
u_1=0,\qquad
P^{(3)}_{1b}=\mathbf1_{a=b},\qquad
T^{(3)}_{1b}=-\mathbf1_{a=b}w_1h(U_a).
\]

There is no time-0 contribution to \(P^{(3)}_{2a}\), since the initial top delta is formally zero. It follows exactly that

\[
P^{(3)}_{2a}=-A_aw_1h(U_a),\qquad
u_2=\lambda y_a\gamma(U_a).
\]

In particular, differentiating the reduced value \(2\lambda D\) would give the wrong readout derivative. The candidate avoids this error.

Substituting these expressions into \(T^{(3)}_{2a}\) gives the first line of (27). Its covariance part is

\[
-\mathcal C_{2a}(e_{1a})
=2\lambda^2A_a\operatorname{Cov}
\bigl(Dh(Z^{(3)}_{2a}),Dh(U_a)\bigr),
\]

with exactly the displayed sign and factor two.

### 7.2 The coefficient includes the second matrix and bottom motion

**C lines 565–595: PASS.**

For a current reverse source at time 1,
\(\partial_{\zeta^{(1)}_{1a}}q^{(1)}_{1b}=\mathbf1_{a=b}\)
and \(Z^{(1)}_1\) has no derivative in that current slot. Therefore

\[
\partial_{\zeta^{(1)}_{1a}}Z^{(1)}_{2a}
=\lambda y_a\gamma^{(1)}_{1a}\tau'_1(q^{(1)}_{1a}),
\]

using \(C_{aa}=1\). Multiplication by the current feature gate and addition of the learned feature moment prove the first line of (29).

Similarly,

\[
\partial_{\zeta^{(2)}_{1a}}Z^{(2)}_{2a}
=A^{(2)}_{2a,1a}
\gamma^{(2)}_{1a}\tau'_2(q^{(2)}_{1a}).
\]

This proves the second line of (29). No other same-time sample contributes a direct reverse-source derivative. The resulting limit

\[
A_a/\lambda\longrightarrow
y_a\{F_2+(F_1+J_1)J_2\}
\]

includes the third matrix's learned moment \(F_2\), the second matrix's learned moment \(F_1J_2\), and the bottom-response contribution \(J_1J_2\).

### 7.3 Small-mesh convergence without a historical Gram inverse

**C lines 597–627: PASS.**

At time 1, \(\delta^{(3)}_{1a}=\lambda D\gamma(U_a)\) is \(O(\lambda)\) even pointwise. Its response coefficients are also \(O(\lambda)\). More explicitly, the only time-0 derivative terms are

\[
B^{(3)}_{1a,0b}
=\lambda y_b\mathbb E[\gamma(U_a)\gamma(U_b)],
\]

and the current block is \(-\mathbf1_{a=b}f_{1a}=O(\lambda)\).
Its learned covariance addition against the time-0 delta is zero.
Thus \(q^{(2)}_1\) is a Gaussian source with \(O(\lambda)\) standard deviation plus a bounded \(O(\lambda)\) shift.

For the middle forward derivatives at this step, derivatives of the attained time-0 delta with respect to forward sources vanish. The time-1 forward row has its current identity injection, while the reverse response coefficients just calculated are \(O(\lambda)\). The formula for \(T^{(2)}\), \(|\tau(q)|\le|q|\), and \(|\tau'|\le1\) therefore give expected middle derivative rows of order \(O(\lambda)\). The time-0 learned delta covariance is again zero. Consequently \(B^{(2)}_1=O(\lambda)\), \(\|\delta^{(2)}_1\|_2=O(\lambda)\), and \(q^{(1)}_1\) has the same Gaussian-plus-bounded-shift estimate.

The bottom displacement at time 2 is \(O_{L^2}(\lambda^2)\). The coefficients in (29), including their off-diagonal versions, are \(O(\lambda)\) by bounded gates and features. Coefficients against time-0 reverse sources also have an \(O(\lambda)\) initial injection and bounded finite subsequent response; their attained delta factors are zero in any case.

For the forward Gaussian increments, (5) gives exactly

\[
\|\xi^{(2)}_{2a}-\xi^{(2)}_{0a}\|_2^2
=\mathbb E|H^{(1)}_{2a}-H^{(1)}_{0a}|^2.
\]

The bounded derivative of \(\phi\) and the bottom displacement make this tend to zero. The remaining middle forward correction is an \(O(\lambda)\) coefficient times an \(O_{L^2}(\lambda)\) delta. Repeating the covariance-difference identity at the third layer proves the claimed convergence there as well. These estimates use the given joint covariances directly and do not invert them.

For each fixed cap, \(q^{(j)}_1\to0\) implies
\(\tau'_j(q^{(j)}_1)\to1\) in probability. All gate and feature products in (29) are bounded, so their expectations converge. Moreover, \(|D|\le2b\), and the bounded, Lipschitz function \(h\) gives

\[
Dh(Z^{(3)}_{2a})-Dh(U_a)\longrightarrow0
\quad\text{in }L^2.
\]

This also justifies passage to the covariance in (27). No uniform integrability of an unbounded sensitivity has been silently assumed in this limit.

### 7.4 Strict positivity, endpoint correlation, and quantifiers

**C lines 618–653: PASS.**

\(L_0=F_2+(F_1+J_1)J_2>0\) follows already from \(F_2\ge m^2\).
For an exchange-symmetric feature pair, its Gram eigenvalues are

\[
\tfrac12\mathbb E(H_1+H_2)^2,\qquad
\tfrac12\mathbb E(H_1-H_2)^2.
\]

The first is positive by the feature floor. The second is positive for \(-1<\rho<1\) by full Gaussian support and nonconstancy. At \(\rho=-1\), the actual first-layer difference is \(2\varepsilon\sin G\), which is not almost surely zero. Thus the first feature Gram is positive definite even at that allowed endpoint.

The middle initialized Gaussian pair is consequently nonsingular, and the same argument makes its feature Gram positive definite. Hence the top initialized pair \(U\) has a positive density on all of \(\mathbb R^2\).

For \(a=1\), \(Dh(U_1)\) has value zero at \((\pi/4,\pi/4)\) and value \(b^2\) at \((\pi/4,-\pi/4)\). Continuity and positive density make its variance strictly positive. Exchange handles \(a=2\), whose corresponding variable has the same variance after the sign change induced by swapping.

It follows that

\[
\lim_{\Delta\downarrow0}
\frac{y_a[-\mathcal C_{2a}(e_{1a})]}{\lambda^3}
=2L_0\operatorname{Var}(Dh(U_a))>0.
\]

The justified quantifiers are

\[
\forall\rho\in[-1,1),\
\forall\,1\le R_1,R_2<\infty,\
\exists\Delta_0(\rho,R_1,R_2)>0,\
\forall\,0<\Delta<\Delta_0:
\quad y_a[-\mathcal C_{2a}(e_{1a})]>0
\]

for both samples, taking the smaller of their two thresholds if necessary. The leading coefficient is independent of the cap pair. This does not claim a uniform positive margin or a uniform threshold as \(\rho\uparrow1\), nor a cap-uniform threshold. The number of updates remains two, so \(S=2\Delta\to0\); it is not an asymptotic statement at fixed positive feature or physical time.

### 7.5 The mean-direction weighted test

**C lines 654–703: PASS.**

The unadjusted impulse has \(x_{2a}=-A_af_{1a}\), so the sign of a matrix entry alone would not suffice for the weighted balance. The candidate supplies the necessary adjustment:

\[
\widetilde v=e_{1a}+(1+A_af_{1a})e_{2a}.
\]

The added current direction contributes the deterministic constant
\(1+A_af_{1a}\) to \(P^{(3)}_{2a}\), and changes neither \(u_2\) nor its covariance with \(w_2h(Z^{(3)}_{2a})\). Hence

\[
P^{(3)}_{2a}(\widetilde v)
=1-A_a\{w_1h(U_a)-f_{1a}\},\qquad
x_{2a}=1.
\]

With \(\omega_{2a}=1\) and all other weights zero, the residual in (21) is exactly \(y_a[-\mathcal C_{2a}(e_{1a})]>0\).
The direction is deterministic, even though its coefficients depend on the selected deterministic law. Its possible failure to lie in the support of the Gaussian covariance is irrelevant to the explicitly stipulated ambient formal derivative test, and the candidate states this restriction.

This falsifies the universal factorization in (32) and the proposed universal nonpositive sign for the covariance contribution. It does not establish positivity of the complete balance, dominance over the readout or learned covariance terms, an unbounded response, or a physical parameter instability.

## 8. Full audit of the transferred P3 bootstrap

**C lines 705–757; P3 lines 110–325: PASS.**

I checked the full induction, not merely whether its conclusion has the desired numerical values. Throughout this section let \(A_*=3/2\) denote P3's kernel bound, to distinguish it from an individual response coefficient. The estimates use \(a=7/6\), \(e=1/10\), \(c=1/5\), \(|C_{ab}|\le1\), \(|y_b|=1\), \(|\tau(q)|\le|q|\), and \(|\tau'|\le1\).

### 8.1 Base case and bottom injection

**P3 lines 130–205.**

The corrected reverse derivative was checked in Section 3 above. The attained forward derivatives still vanish, so \(U_0=V_0=0\).

A single bottom reverse-source injection has preactivation size at most \(\Delta e/2\). Differentiating the feature contributes another factor \(e\), giving \(\Delta/200\). The product variation is bounded by
\(c|q||dZ|+e|dq|\), and the query response by \(e\sum|B||dZ|\) plus the single direct source. The two update samples contribute a total absolute coefficient at most one after the factor \(1/2\); they do not introduce an extra factor two.

The discrete comparison at P3 lines 174–177 is valid for the running maximum with nonnegative coefficients. It gives the stated \(E^{(1)}_j\).

Under past \(U_r,V_r\le1\),
\(\|q^{(2)}_r\|_2\le aS/10+a\le161/120=:Q_0\).
Therefore the bottom Gaussian source has standard deviation at most \(Q_0/10\), and its response shift is bounded by \(a\).

For two correlated Gaussian coordinates, the maximum-exponential bound follows from
\(e^{t|x|}\le e^{tx}+e^{-tx}\) and summation over the two samples. Time Jensen does not require temporal independence. Its exponent here is at most

\[
\frac{73}{200}+\frac9{200}\left(\frac{161}{1200}\right)^2<\frac25.
\]

Thus \(\mathbb EE^{(1)}_j<6\), and

\[
|A^{(2)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{50}\right)
=\frac\Delta2\frac{1279}{900}
<A_*\Delta/2.
\]

No gate sign enters any of these estimates.

### 8.2 Middle total forward row and reverse-source injection

**P3 lines 209–261.**

There is one direct current identity entry in a fixed output row, not one for each source slot. Summing source derivatives and then the two update samples turns \(A_*\Delta/2\) into \(A_*\Delta\). This yields the stated \(E^{(2)}_j\).

The single reverse-source preactivation injection is at most \(A_*\Delta/20\); multiplication by the output feature gate gives \(A_*\Delta/200\). The reverse query's Gaussian variance is at most \((7/40)^2\). Time Jensen and the same two-sample Gaussian bound give, for \(p\ge1\),

\[
\mathbb E(E^{(2)}_j)^p
\le4\exp\left(\frac{219p}{400}
+\frac{3969p^2}{1280000}\right).
\]

The \(p=1\) estimate gives \(\mathbb EE^{(2)}_j<8\). The \(p=2\) estimate gives

\[
\|E^{(2)}_j\|_2
\le2\exp\left(\frac{219}{400}
+\frac{7938}{1280000}\right)<\frac72.
\]

The elementary exponential comparisons used by P3 are valid. In particular, the last exponent is below \(5/9\), \(e<68/25\), and
\((68/25)^5<(7/4)^9\). Likewise the bottom comparison follows from
\((11/4)^2<(3/2)^5\).

Consequently

\[
|A^{(3)}_{ja,sb}|
<\frac\Delta2\left(\frac{49}{36}+\frac3{25}\right)
=\frac\Delta2\frac{1333}{900}
<A_*\Delta/2.
\]

The small positive margin in this last inequality is real.

### 8.3 Top row, learned transpose term, and current middle row

**P3 lines 263–306.**

Differentiating both readout and gate gives the full top delta row bound

\[
\frac\Delta{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
\le\frac{73}{300}S\max_{v\le j}T_v.
\]

The first term is essential. The past-only forward recursion then gives
\(\max T_v\le\exp(657/800)<5/2\). The stated elementary comparison with \(e^{5/6}\) is valid: \(3^5 2^6=15552<15625=5^6\).

The learned top covariance row has size at most \(a^2S^3/100\). Its factor is \((\Delta/2)\times2\) samples, and its delta bound uses \(|w|\le aS\), so it has not been omitted or undercounted. Hence

\[
V_k\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}=:V_*<1.
\]

Before estimating the current \(U_k\), this gives

\[
\|q^{(2)}_{ka}\|_2
\le\frac7{40}+\frac76V_*
=\frac{24829}{19200}=:Q_*.
\]

The current middle derivative row is bounded by
\((|q^{(2)}_{ka}|/5+V_k/100)E^{(2)}_k\).
Cauchy–Schwarz applies without independence between the query and sensitivity. The learned middle covariance row is at most \(SQ_*^2/100\). Thus

\[
U_k
\le\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}.
\]

The rational equality checks: \(24829^2=616479241\); the two terms have numerators \(69213580800\) and \(1849437723\) over the common denominator \(73728000000\). The numerator for \(97/100\) at that denominator is \(71516160000\), strictly larger.

The dependency's induction order is sound. Only past \(U,V\) enter the forward coefficient and sensitivity estimates. The current \(V_k\) is proved before \(Q_*\) and the current \(U_k\). No current \(U_k\) is assumed in proving itself.

### 8.4 Actual-query exponential moments

**P3 lines 308–325.**

Both queries have the form \(q=\zeta+\beta\), with \(|\beta|\le a\). The middle source variance is at most \((7/40)^2\), and the bottom source variance at most \((Q_*/10)^2<(7/40)^2\).

The pointwise inequality \(q^2\le2\zeta^2+2a^2\) gives

\[
\mathbb E e^{q^2/16}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]

The Gaussian square integral is finite because its denominator is positive. The final elementary bounds \(e^{49/288}<5/4\) and the remaining factor \(<4/3\) even give a product \(<5/3\). No independence of \(\beta\) from \(\zeta\) is used.

This proves the complete transfer of (34), including both actual-query envelopes, for every mesh with \(S\le3/2\) and every finite cap pair \(R_1,R_2\ge1\). The only positive-gate assertion inside the local derivative proof needing alteration is the already corrected base-case sentence. The response proof itself uses absolute bounds throughout.

P3 lines 333–341 are a separate, conditional same-label continuation discussion; they are not part of the transferred opposite-label bootstrap. Its positive feature floor can control a same-label sum, but supplies no opposite-label contrast lower bound. P3 lines 343–352 expressly leave comparison, cap removal, identification, nonfreezing, and global continuation to further work. Those conclusions have not been imported by the sign audit.

## 9. Nontransferability and remaining obligations

**C lines 759–830 and 832–876: PASS as mathematical distinctions, without certifying the historical descriptions of unread documents.**

Each identified obstruction is valid for this activation:

1. \(\gamma(z)=b\cos(z+\pi/4)\) changes sign and vanishes at \(\pi/4+\pi\mathbb Z\). A global coordinate with derivative \(1/\gamma\) has poles. Absolute raw-coordinate estimates remain available.

2. Ordered preactivations do not give ordered periodic features. For example, \(z_1=2\pi\ge1\) and \(z_2=-2\pi\le-1\) have identical activations. A positive lower bound on \(\phi\) controls a same-label sum, not the contrast.

3. Opposite-label readout increments have no pointwise positive lower bound of the same-label kind. The sign of \(w\gamma(Z_a)\) also cannot be inferred from the sign of \(w\). The mean identity (13) does not restore either pointwise assertion.

4. A query quadrant alone does not determine a delta quadrant after multiplication by a sign-changing, correlated gate. Gram matrices and gate-square kernel terms remain nonnegative, but their strict positivity needs a separate joint or conditional argument.

5. Gaussian initialization assigns zero probability to the discrete gate-zero set. General later-time \(L^2\) or unbounded-support information does not do so. Interpreting “nonzero velocity” as nonzero in probability or in \(L^2\), the relevant condition is positive probability of \(V\ne0\) and \(\gamma(Z)\ne0\). Proving \(\mathbb P(\gamma(Z)=0)=0\) is sufficient, but is not established merely by those weak attained-law bounds.

6. Bounded \(\phi\) on an unbounded support excludes a nonzero affine slope. It does not exclude a constant feature: a law supported on \(2\pi\mathbb Z\) has \(\phi(Z)=1+\varepsilon\). A nonzero absolutely continuous component would suffice to exclude any affine identity, since the analytic function \(\phi(z)-(\alpha z+\beta)\) cannot vanish on a set of positive Lebesgue measure unless it is identically zero; this periodic nonconstant \(\phi\) is not affine.

7. The relative-gate inequality fails exactly at the exhibited points: \(\phi(0)=\phi(\pi/2)=1+\varepsilon\), while \(\gamma(0)=\varepsilon\) and \(\gamma(\pi/2)=-\varepsilon\). Ordinary Lipschitz bounds in preactivation distance survive.

The local covariance example does not imply that no larger coupled energy can control the residual. The first explicitly missing statistic is the contracted two-time curvature covariance in (35), together with the readout term, middle mixed query term, and learned transpose additions. A finite value of every derivative for each fixed program is not a uniform estimate as the time mesh or caps vary. The candidate maintains these distinctions.

The final claim table at C lines 863–872 is supported in the stipulated scope: the current-block identities and bounds, the positive second-update coefficient, its failure of mean factorization, and the local absolute estimates are established. Arbitrary-interval signed stability, population construction and restart, physical GF/GD comparisons, width convergence, every-time nonlinearity, and all-layer nonfreezing remain unproved here.

## 10. Disposition

The exact candidate requires the single sentence-level correction at C line 459 identified in Section 2. No repair to equations (1)–(35), the second-update weighted test, the small-mesh quantifiers, or the transferred bootstrap constants is required by this audit.

After that correction, the substantive finite-law result merits PASS within the narrow scope stated above. This report makes no finite-width identification, global continuation, or full signed-response stability certification, and it leaves the candidate unchanged.
