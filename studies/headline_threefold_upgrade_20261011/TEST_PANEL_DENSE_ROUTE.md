# Test-panel dense variability

Scoped author: uniform_time_scope, 2026-10-11.

Two distinct conclusions are obtained. The actual trained-endpoint oracle
argument extends from orthogonal queries to every fixed query outside the
training span, with no new activation or label condition. For full-span
training, a separated single test input has a rigorously proved positive-time
crossing mechanism in the coupled frozen-feature comparator. Transfer of that
mechanism to the actual feature-learning dynamics remains open. It is not
presented as a counterexample to the requested dense-network theorem.

These are study results with direct author checks, not independent reviews or
promoted material. No experiment, paper edit, or Git write was performed.

## 1. Contract and authorized inputs

The revised Taylor query domain is a nonempty finite panel of test inputs
declared before initialization and distinct from training inputs. The working
comparison is

\[
\sup_{t\in(0,\infty]}
\frac{\sup_{x\in\mathcal X_{\rm test}}
 |f_{\rm model}(t,x)-f_n(t,x)|}
 {\sup_{x\in\mathcal X_{\rm test}}
 |f_n(t,x)-\widetilde f_n(t,x)|}
\xrightarrow{\mathbb P}0.
\tag{1}
\]

The coordinator is resolving the reciprocal wording and placement of the
spatial supremum. This note concerns the dense denominator for (1), retaining
the fully trained canonical model and fixed positive labels when making actual
network claims. It does not revisit the zero initial value or training-only
endpoint obstruction.

The supervisor authorized the current compact paper, this joint study, and the
directly relevant proof chain in
studies/general_nonlinear_endpoint_lower_20261010/. The sources used here are
its Gaussian-oracle endpoint assembly, projected innovation and scalar modules,
Section 6 of its oracle integration module, Sections 1–2 of its readout moment
module, its exact endpoint identity, and its frozen-kernel linear-response route.
Their relevant proofs were read, not merely their review verdicts. The current
paper's canonical setup, fitting proof, initial Gaussian feature identities,
and source conclusions remain their stated inputs. No claim is made to
reaudit the complete source-cavity construction in this note.

The rigorous-solution, canonical-notation, and conjecture-investigation skills
were applied, including the research-contract, evidence, and adversarial-audit
references. A comparator theorem is kept separate from a theorem about
feature-learning dynamics.

## 2. Actual endpoint theorem without orthogonality

Use exactly the canonical Gaussian network and sufficient small-label cap in
paper/compact.tex, and suppose every activation is nonaffine. Define

\[
S=\operatorname{span}\{v_1,\ldots,v_m\}\subset\mathbb R^d,
\qquad v_a=x_a/\sqrt d.
\]

Let \(v\) be any deterministic unit test direction with \(v\notin S\). Write

\[
v=v_S+v_\perp,\qquad v_S=P_Sv,\qquad
v_\perp=(I-P_S)v,\qquad \sigma=\|v_\perp\|>0.
\tag{2}
\]

**Endpoint extension.** For every \(\delta\in(0,1)\), there are
\(c_\delta>0\) and \(N<\infty\), depending on the fixed problem, the
fixed test direction, and \(\delta\), such that for every individual
\(n\ge N\),

\[
\Pr\left\{\text{both runs fit and }
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
 \ge c_\delta/\sqrt n\right\}\ge1-\delta.
\tag{3}
\]

Thus a test panel containing at least one fixed direction outside \(S\)
has an endpoint supremum lower bound. Orthogonality is unnecessary. A
positive distance from the span remains necessary for this proof, and
the constants may deteriorate as that distance tends to zero.

This also restores the weaker ratio-of-trajectory-suprema comparison on that
test-only panel. The old positive-time training witness is no longer in the
query domain, but (3) gives a test-domain trajectory denominator at least
\(c_\delta/\sqrt n\). Dividing the existing Legendre error
\(CY/(\sqrt n\log(en)^3)\), or selected error \(Y/n\), by this bound
and then sending the fixed failure budget to zero proves that weaker ratio
converges to zero in probability. It does not establish (1), which uses the
dense denominator separately at every time.

### 2.1 Exact first-layer conditional law

The oracle integrator in Section 6 of GELU_SILU_FLOW_ROUTE.md accesses
\(W_0^{(1)}\) only on the training span and accesses each initialized hidden
mixer through \(O_{\rm problem}(\log(en)^{9/2})\) adaptive matrix actions.
It returns an implicit parameter tuple \(\widehat\theta\) satisfying

\[
\|\widehat\theta-\theta(\infty)\|_{\rm par}
\le C_{\rm problem}n^{-16}
\tag{4}
\]

on an event with probability tending to one. The parameter norm is the paper's
mobility norm, with \(W^{(1)}\) and \(w\) divided by \(\sqrt n\).
Every first-layer learned increment has right factor in \(S\).

Let \(\mathcal T_n\) be the complete training transcript. The map
\(W_0^{(1)}P_S\) is known from its actions on the training directions.
Gaussian orthogonal projection gives

\[
G=W_0^{(1)}v_\perp/\sigma\sim N(0,I_n),
\]

independently of \(\mathcal T_n\): the initialized first-layer rows are
independent standard Gaussian vectors, their restrictions to \(S\) and
\(S^\perp\) are independent, and the transcript is a function of the former
restriction and the independent hidden matrices. Therefore the returned
first test preactivation is exactly

\[
\widehat z^{(1)}(v)=a+\sigma G,\qquad
a=\widehat W^{(1)}v_S.
\tag{5}
\]

The vector \(a\) is transcript measurable. The fresh \(G\) is also
conditionally independent of the residual hidden Gaussian matrices in the
two-sided deferred-decisions representation.

Add the transcript-measurable condition

\[
\|\widehat W^{(1)}P_S\|_{\rm op}/\sqrt n\le10
\tag{6}
\]

to the old good-transcript event. Its probability tends to one: the original
fitting tube gives the bound nine, and (4) bounds the normalized operator
error by \(o(1)\). The full-parameter fitting event is used only to establish
the probability of (6), not to condition the fresh Gaussian. On (6),

\[
\|a\|/\sqrt n\le B_1:=10\|v_S\|.
\tag{7}
\]

### 2.2 Replacement innovation constants

For each activation define \(c_j=|\phi_j(0)|\) and
\(s_j=\sup_{x\in\mathbb R}|\phi_j'(x)|\). Put

\[
\begin{aligned}
K_1&=s_1\sigma,\\
v_1&=\min_{|b|\le2B_1+1,\;u\in[\sigma/\sqrt2,\sigma]}
       \operatorname{Var}\phi_1(b+uG_0),\qquad G_0\sim N(0,1),\\
\kappa_1&=v_1/32,\qquad
H_1=c_1+s_1(B_1+2\sigma).
\end{aligned}
\tag{8}
\]

Nonconstancy and Gaussian full support make every variance positive.
Lipschitz growth gives its continuity on the compact parameter set, so
\(v_1>0\).

Apply the one-layer projected innovation lemma with preactivation-removal
projection zero and feature-removal projection \(P_{V_2}\), the oracle's
forward-input projector. Its rank is at most a deterministic
\(r_n=O_{\rm problem}(\log(en)^{9/2})=o(n)\). Formula (5) is the required
conditional law. Eventually

\[
r_n\le\frac{v_1n}{4K_1^2},\qquad n\ge\frac{8K_1^2}{v_1}.
\]

Consequently, uniformly over good transcripts,

\[
\Pr\left\{\frac{\|(I-P_{V_2})\widehat h^{(1)}(v)\|^2}{n}
 <\kappa_1\,\middle|\,\mathcal T_n\right\}
\le\frac{32K_1^2}{v_1n}.
\tag{9}
\]

On \(\|G\|\le2\sqrt n\), the feature norm is at most \(H_1\sqrt n\);
this event fails with probability at most \(2/(9n)\). The coordinates
need not have a common mean.

For later layers retain the old bound forty on the known part of every
hidden mixer. For \(2\le j\le L-1\), define

\[
\begin{aligned}
B_j&=40H_{j-1},&H_j&=c_j+42s_jH_{j-1},&K_j&=s_jH_{j-1},\\
v_j&=\min_{|b|\le2B_j+1,\;
u\in[\sqrt{\kappa_{j-1}/2},H_{j-1}]}
\operatorname{Var}\phi_j(b+uG_0),&
\kappa_j&=v_j/32.
\end{aligned}
\tag{10}
\]

All \(v_j>0\). The scale intervals are nonempty: Gaussian Poincare gives
\(v_1\le s_1^2\sigma^2\le H_1^2\), and inductively
\(v_j\le s_j^2H_{j-1}^2\le H_j^2\).
The old exact deferred-decisions representation and the same innovation
lemma propagate the lower innovation and upper norm through layer \(L-1\).
The total conditional failure is at most

\[
\frac1n\sum_{j=1}^{L-1}
\left(\frac{32K_j^2}{v_j}+\frac29\right)
\tag{11}
\]

eventually. All finitely many rank conditions hold because \(r_n=o(n)\).

### 2.3 Last-layer scalar and actual-endpoint transfer

Conditional on the transcript and successful lower query layers, the returned
test output retains the exact form

\[
\widehat f_n(v)=\frac1n\widehat w^\top
\phi_L(b+\sigma_L(I-P_{U_L})g),\qquad g\sim N(0,I_n),
\tag{12}
\]

with fresh \(g\), \(\|b\|/\sqrt n\le40H_{L-1}\), and
\(\sigma_L\in[\sqrt{\kappa_{L-1}},H_{L-1}]\).
The trained-readout bounds are unchanged. In the notation of the scalar
module, valid fixed constants are

\[
E=Y/(4H),\quad
M_4=16\beta^{114L}(Ym/\gamma)^4+1,\quad
B=40H_{L-1},\quad
\sigma_-=\sqrt{\kappa_{L-1}},\quad\sigma_+=H_{L-1},
\tag{13}
\]

where \(H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}\).
Fitting gives the readout-energy lower bound, and the source exponential
budget gives its empirical fourth moment. The error (4) transfers both to
the approximant exactly as in the original assembly.

For explicit coefficient dependence, put

\[
\begin{aligned}
R&=\max\{1,4B\sqrt{M_4}/E^2\},\\
d_R&=\min_{|a|\le R,\;u\in[\sigma_-/2,\sigma_+]}
\left\{\operatorname{Var}\phi_L(a+uG_0)
 -\big(\mathbb E[G_0\phi_L(a+uG_0)]\big)^2\right\},\\
v_0&=d_RE^2/16>0.
\end{aligned}
\tag{14}
\]

The Hermite tail in \(d_R\) is positive by nonaffinity and Gaussian full
support; continuity makes its compact minimum positive. The projected
scalar lemma gives

\[
\sup_a\Pr\{|\sqrt n\widehat f_n-a|\le c\}
\le\frac{2c}{\sqrt{2\pi v_0}}+O_{\rm problem}(n^{-1/4})
\tag{15}
\]

under the stated conditioning. Excluded events add \(o(1)\).

The query transfer remains valid despite the nonzero active component:
\(\|(\widehat W^{(1)}-W^{(1)}_\infty)v\|/\sqrt n\) is bounded by (4).
Forward subtraction, using (6), bounded hidden operators, Lipschitz
activations, and the common unused Gaussian component, gives

\[
|\widehat f_n(v)-f_n(\infty,\sqrt d\,v)|
\le C_{\rm problem}(1+\|G\|/\sqrt n)
\|\widehat\theta-\theta(\infty)\|_{\rm par}.
\tag{16}
\]

The first-layer discrepancy is no longer identically zero, but (16) is still
\(O(n^{-16})\) with probability tending to one. Average (15) over the
independent second run, transfer by (16), and charge both fitting failures.
The old allocation with \(c_\delta=\delta\sqrt{2\pi v_0}/16\) proves (3).

For \(v\in S\), \(\sigma=0\), the fresh Gaussian in (5) disappears, and
(8) supplies no positive variance. Pairwise separation from the training
directions does not imply that a query lies outside their span.

## 3. Separated-test crossings with full-span training: a comparator theorem

This section concerns the frozen initial tangent-kernel predictor
\(f_{{\rm RF},n}\), using the actual finite-depth Gaussian initialization.
Its hidden weights are frozen and its readout is trained with the paper's
readout mobility. It is a comparator, not the feature-learning predictor.

Take \(d=m=2\), any fixed \(L\ge2\),

\[
v_1=e_1,\qquad v_2=e_2,\qquad
v_*=(e_1+e_2)/\sqrt2,\qquad
y=\varepsilon(1,-1)^\top,
\tag{17}
\]

and \(\phi_j=\tanh\) at every layer. The test is nonparallel to both signed
training directions, with positive separation, and training spans
\(\mathbb R^2\). Tanh satisfies the activation assumptions on
\(|\operatorname{Im}z|<\pi/4\): the identity
\(|\cosh(x+iy)|^2=\sinh^2x+\cos^2y\ge1/2\)
bounds its derivative. It is nonaffine.

Oddness and symmetry make the population top training Gram and test column

\[
Q=qI_2,\qquad k=r(1,1)^\top,\qquad q>0,\quad r>0.
\tag{18}
\]

The training cross-covariance stays zero because independent centered
Gaussian preactivations have zero activated means. The test covariance stays
positive because the Gaussian Hermite covariance series has nonnegative
squared coefficients and a positive degree-one coefficient for tanh.
Also \(q<1\), so \(\gamma=q\) and \(m/\gamma\ge1\).
Fix \(0<\varepsilon\le(q/2)\beta^{-30L}\). Then \(Y=\varepsilon\)
satisfies the unchanged label cap and does not shrink with width.

The augmented population Gram on the three inputs is positive definite after
the first layer. A zero-variance linear combination would imply

\[
a\tanh g_1+b\tanh g_2+
c\tanh((g_1+g_2)/\sqrt2)=0
\]

everywhere, by continuity and Gaussian full support. Applying
\(\partial_{g_1}\partial_{g_2}\) gives
\((c/2)\tanh''((g_1+g_2)/\sqrt2)=0\), so \(c=0\).
Varying the remaining coordinates gives \(a=b=0\). At each later layer
the preactivation Gaussian has full support in \(\mathbb R^3\), so
coordinatewise nonconstant tanh again makes every nontrivial linear
combination have positive second moment.

Let \(Q_n,k_n\) be the actual empirical initialized top training Gram and
test column. Define \(h_t(s)=(1-e^{-ts})/s\), with \(h_t(0)=t\).
Since \(2/m=1\), the exact frozen predictor is

\[
f_{{\rm RF},n}(t,x_*)
=\varepsilon k_n^\top h_t(Q_n)(1,-1)^\top.
\tag{19}
\]

### 3.1 Finite-depth Gram fluctuations

Collect the six upper-triangular entries of each augmented empirical Gram.
The first-layer vector is an average of iid bounded random vectors, so its
root-width fluctuation converges to a centered Gaussian. This follows by
the scalar characteristic-function expansion for each linear combination.

For later layers, condition on the preceding empirical covariance \(S_n\).
The preactivation rows are iid \(N(0,S_n)\). The map
\(\Psi(S)=\mathbb E[\tanh Z\tanh Z^\top]\), \(Z\sim N(0,S)\), is
continuously differentiable near the limiting positive-definite \(S\).
To justify differentiation, derivatives of the Gaussian density with
respect to \(S\) are bounded by an integrable polynomial times a Gaussian
uniformly on a compact positive-definite neighborhood, while tanh products
are bounded.

The centered empirical row noise has a conditional characteristic function
converging in probability to a deterministic centered Gaussian characteristic
function. Its third moments are uniformly bounded because tanh is bounded.
Multiplying by the bounded characteristic function of the preceding
fluctuation proves joint convergence, with the new Gaussian noise independent
of the preceding limit. The expansion

\[
\sqrt n[\Psi(S_n)-\Psi(S)]
=D\Psi(S)[\sqrt n(S_n-S)]+o_{\mathbb P}(1)
\]

then completes induction. In particular the final Gram fluctuation is
Gaussian, and its covariance includes the final conditional row-noise
covariance as an additive positive-semidefinite contribution.

Put \(u=(1,-1)^\top\) and

\[
A_n=\sqrt n(k_n-k)^\top u,\qquad
B_n=\sqrt n k^\top(Q_n-qI_2)u.
\tag{20}
\]

The pair converges to a centered Gaussian \((A,B)\) with positive-definite
covariance. To check strictness, it suffices to examine the final conditional
row contribution. Its limiting tanh feature triple
\((H_1,H_2,H_*)\) has full support on \((-1,1)^3\), because the final
preactivation covariance is positive definite when \(L\ge2\).
The two relevant mean-zero row variables are

\[
H_*(H_1-H_2),\qquad r(H_1^2-H_2^2).
\tag{21}
\]

A constant linear combination of them would be constant on the whole open
cube. Setting \(H_1=H_2\) makes the constant zero. Holding
\(H_1\ne H_2\) fixed and varying \(H_*\) forces the first coefficient
to vanish; varying \(H_1^2-H_2^2\) forces the other to vanish because
\(r>0\). Thus this row covariance is positive definite. Earlier-layer
covariance contributions cannot remove it.

### 3.2 Two fixed times force a positive-probability crossing

The Taylor series of the analytic matrix function at the scalar matrix gives

\[
h_t(qI_2+E)=h_t(q)I_2+h_t'(q)E+O(\|E\|^2).
\]

Since \(k^\top u=0\), equations (19)–(20) imply

\[
\sqrt n f_{{\rm RF},n}(t,x_*)
\Longrightarrow\varepsilon\{h_t(q)A+h_t'(q)B\},
\tag{22}
\]

jointly at any finitely many fixed positive times. The independent-run
difference has the same form with a centered Gaussian pair whose covariance
is doubled.

For \(t>0\), \(h_t(q)>0\) and

\[
-\frac{h_t'(q)}{h_t(q)}
=\frac1q-\frac{t}{e^{qt}-1}.
\tag{23}
\]

This expression is strictly increasing in \(t\). Its derivative has the
sign of \((qt-1)e^{qt}+1\), which is zero at zero and has derivative
\(qt\,e^{qt}>0\) with respect to \(qt\). Thus the coefficient vectors
at any \(0<t_1<t_2\) are linearly independent.

Define
\(g_{{\rm RF},n}(t)=f_{{\rm RF},n}(t,x_*)-
\widetilde f_{{\rm RF},n}(t,x_*)\).
The pair of root-width differences at \(t_1,t_2\) therefore converges
to a Gaussian with positive-definite covariance and everywhere positive
density. For every fixed \(a>0\),

\[
\lim_{n\to\infty}
\Pr\{\sqrt n g_{{\rm RF},n}(t_1)>a,\;
       \sqrt n g_{{\rm RF},n}(t_2)<-a\}>0.
\tag{24}
\]

The event boundary has zero limiting probability. Each finite-width frozen
predictor is continuous, so (24) forces agreement of the two test predictions
at some \(t\in(t_1,t_2)\). This proves a nonvanishing-probability
interior crossing for a genuinely separated test and full-span training.

The frozen endpoint remains nondegenerate: the same matrix expansion with
\(h_\infty(s)=s^{-1}\) gives the positive-variance limit
\(\varepsilon(A/q-B/q^2)\). Endpoint anti-concentration and positive-time
crossings therefore coexist in this concrete comparator.

## 4. Actual feature-learning gap

The crossing theorem defeats a positive simultaneous lower profile for the
frozen comparator on this test. It does not substitute that comparator for
the actual dense trajectory in (1).

For a sufficient transfer condition, define

\[
R_n(t)=f_n(t,x_*)-f_{{\rm RF},n}(t,x_*),\qquad
\widetilde R_n(t)=\widetilde f_n(t,x_*)-
                  \widetilde f_{{\rm RF},n}(t,x_*).
\]

If one could show

\[
\sqrt n(R_n(t_j)-\widetilde R_n(t_j))
\xrightarrow{\mathbb P}0,\qquad j=1,2,
\tag{25}
\]

the strict margins in (24) would transfer to the actual dense difference.
A weaker quantitatively controlled joint remainder could also suffice.
Neither result is established here; (25) is stronger than one should
generally expect without accounting for the nonlinear leading fluctuation.

A width-independent pathwise \(O(Y^3)\) bound does not imply (25) for
fixed \(Y>0\). The authorized exact endpoint-identity note exhibits the
same issue at the fitted limit. Reducing a fixed positive label amplitude
does not justify dropping its root-width fluctuation for all larger widths.
A fully trained two-time fluctuation law, or a direct conditional argument
with nondegenerate temporal covariance, remains necessary.

The full-span endpoint problem also remains open after Section 2. Once
first-layer training actions reveal the whole input space, its fresh test
Gaussian component vanishes. A positive initial augmented feature-Gram gap
does not show that the test feature stays outside the adaptive
polylogarithmic training-query span. That adaptive projection-residual
estimate is a separate missing obligation.

## 5. Claim status and checks

| Claim | Status | Scope |
|---|---|---|
| Endpoint bound (3) | Proved extension of supplied oracle proof | Actual dense training; fixed test outside training span |
| Two-time law and crossing (22)–(24) | Proved | Actual deep initialization; frozen hidden weights; separated test and full-span training |
| Actual dense crossing for (17) | Open | Fully trained fluctuation transfer missing |
| Arbitrary full-span actual endpoint lower bound | Open | First oracle innovation unavailable |
| Simultaneous ratio theorem (1) | Not established | Endpoint theorem and comparator crossing do not settle it |

The direct author check verified the first-layer conditional law and
measurability, replacement innovation constants, parameter-to-query transfer,
the example's Gram gap and fixed label cap, the finite-depth Gram CLT,
strict covariance positivity, and independence of the two temporal coefficient
vectors. No numerical evidence is used. A fixed-time scalar small-ball bound
does not supply the missing fully trained temporal conclusion.

Source HEAD: ef8362764b4eb8144d7af8d6f8db080fdaaf82ca. The index was empty.
The following SHA-256 values identify files in the authorized
studies/general_nonlinear_endpoint_lower_20261010/ packet:

    8088619ca61fadf70871f3f96af907602097acc3a74f7b3ca742f6a553dfba3d  GAUSSIAN_ORACLE_ENDPOINT.md
    4ddb7d8ff0c6a7235bbf8292e565d08525bba70bd39ea3393292987f861417e4  GELU_SILU_PROJECTED_INNOVATION.md
    65571cb900e1ba791f56a95a78b00ef72c6d4a43954d6c8e8602bc5f4e45c5f2  GELU_SILU_PROJECTED_SCALAR.md
    f3b33474289c38cc38bfbb9eeb90d5aed7652b7a025f4c3171f11e5140908c1c  GELU_SILU_FLOW_ROUTE.md
    882de8bf0e33e7d7c6a62cb1afd29d633531ccc7a6b4cdb1942cccef98c4fa93  NONODD_MOMENT_ROUTE.md
    35dd8b70762ae977e889a998efc4a422564c2cd1974bf455865a47175182f721  ENDPOINT_IDENTITY.md
    6a3908239553f21875241bfad6592e7bf2e266f27b9bac6c85d1a3010e75f89f  LINEAR_RESPONSE_ROUTE.md
