# Independent dense-bias route: a qualitative all-time theorem and the missing rate

Status: complete candidate proof of the qualitative theorem below, checked by its author; not independently reviewed or promoted. The requested strict root-width comparison remains open. No experiment was run.

This scoped route used only the assignment, shared instructions, required accessible skills, and the maintained book passages listed at the end. It did not inspect another route or another study. The supervisor supplied the candidate construction of an independently initialized network of diverging logarithmic width; the proof below was completed independently before comparison with the other routes. The required canonical-notation skill at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was unreadable, including on a narrow escalated read. Following the supervisor's disclosed fallback, this note applies the user's explicit notation requirements and `docs/notation.qmd`.

## 1. Precise positive result

Let \(u_a=x_a/\sqrt d\), \(1\le a\le m\), be orthonormal vectors in \(\mathbb R^d\), and fix real labels \(y=(y_1,\ldots,y_m)\). At width \(N\), use

\[
h_N^{(1)}(u)=\tanh(A_Nu),\qquad
h_N^{(2)}(u)=\tanh(W_Nh_N^{(1)}(u)),\qquad
f_N(t,u)=\frac{w_N(t)^Th_N^{(2)}(t,u)}N.
\]

The initialization consists of independent entries
\(A_{N,ij}(0)\sim N(0,1)\), \(W_{N,ij}(0)\sim N(0,1/N)\), and the exactly zero stored readout \(w_N(0)=0\). All three blocks evolve by gradient flow of

\[
\mathcal L_N=\frac1m\sum_{a=1}^m(f_N(u_a)-y_a)^2
\]

with block mobilities \((N,1,N)\). The notation here corresponds to the book's \((W^{(1)},W^{(2)},W^{(3)})=(A_N,W_N,w_N)\). Time is the physical gradient-flow time for this mean loss.

Put

\[
q=\mathbb E\tanh^2G,\qquad
\lambda=\mathbb E\tanh^2(\sqrt q G)>0,
\qquad G\sim N(0,1).
\]

Fix \(M=10\). For \(s\ge0\), define the explicit scalar bounds

\[
D_1(s)=\frac{Ms^2}{2}+\frac{s^4}{8},\qquad
D_2(s)=\frac{s^2}{2}+\left(M+\frac{s^2}{2}\right)D_1(s).
\]

Choose any fixed \(s_0\in(0,1]\) satisfying

\[
\sqrt m D_2(s_0)\le\frac12\sqrt{\lambda/2},
\qquad
\kappa=\lambda/8,
\qquad
\|y\|_2\le \frac{\kappa s_0}{2\sqrt m}.
\tag{1}
\]

Such an \(s_0\) exists because \(D_2(s)\to0\) as \(s\downarrow0\). These hypotheses allow every fixed sign pattern and every sufficiently small nonzero label vector; no width-dependent shrinking of the labels is used.

**Qualitative theorem.** There is a deterministic predictor \(f(t,u)\), continuous on \([0,\infty)\times S^{d-1}\), with a continuous limiting predictor \(f(\infty,u)\), such that

\[
\sup_{t\in[0,\infty]}\sup_{u\in S^{d-1}}
|f_N(t,u)-f(t,u)|\longrightarrow0
\quad\text{in probability as }N\to\infty.
\tag{2}
\]

For the endpoint in (2), the finite flow has an endpoint on events whose probability tends to one. Equivalently, define the displayed error to be \(+\infty\) on the complement of those events. This convention makes no unsupported assertion about arbitrary small-width Gaussian initializations.

Consequently, let \(q_n\) be any deterministic integers tending to infinity and initialize a width-\(q_n\) network directly and independently of the width-\(n\) reference. Both networks use the preceding canonical initialization and their own standard mobilities. Then

\[
\sup_{t\in[0,\infty]}\sup_{u\in S^{d-1}}
|f_n(t,u)-f_{q_n}(t,u)|\longrightarrow0
\quad\text{in probability.}
\tag{3}
\]

In particular \(q_n=\lceil\log(en)\rceil\) gives a direct, autonomous, genuinely nonlinear construction with parameter storage

\[
dq_n+q_n^2+q_n=O_d((\log(en))^2).
\tag{4}
\]

The initial data require \(dq_n+q_n^2\) independent scalar Gaussian draws, followed by setting the readout to zero. Neither initialization nor evolution queries the dense reference, its coefficients, or its trajectory. A full-batch vector-field evaluation takes \(O(m(q_n^2+dq_n))\) scalar operations, apart from the cost of scalar activation evaluations, and can use \(O(q_n^2+dq_n+mq_n+md)\) live scalar storage. A predictor query costs \(O(q_n^2+dq_n)\). This is a finite ODE theorem, not a proved bit-complexity or numerical-discretization bound.

No rate is asserted in (2) or (3). In particular, (3) does **not** give an error of \(C_{d,m,y,\delta}/\sqrt n\), nor an explicit width needed for a prescribed accuracy. Choosing a slowly growing width from a qualitative limit cannot supply either claim.

## 2. Exact finite dynamics and a uniform small-label bound

For a training input, write \(r_a=f_N(u_a)-y_a\) and

\[
\delta_a^{(2)}=w_N\odot\tanh'(W_Nh_N^{(1)}(u_a)),\qquad
\delta_a^{(1)}=\tanh'(A_Nu_a)\odot W_N^T\delta_a^{(2)}.
\]

The exact equations are

\[
\dot A_N=-\frac2m\sum_a r_a\delta_a^{(1)}u_a^T,
\quad
\dot W_N=-\frac2{mN}\sum_a r_a\delta_a^{(2)}h_N^{(1)}(u_a)^T,
\quad
\dot w_N=-\frac2m\sum_a r_a h_N^{(2)}(u_a).
\tag{5}
\]

Define the accumulated residual control by

\[
s(t)=\frac2m\int_0^t\|r(\tau)\|_1\,d\tau.
\tag{6}
\]

All subsequent inequalities in this section are deterministic, on an initialization satisfying

\[
\|W_N(0)\|_{\mathrm{op}}\le M,
\qquad
\lambda_{\min}\left(\frac1N H_N(0)^TH_N(0)\right)\ge\lambda/2,
\tag{7}
\]

where the \(a\)-th column of \(H_N\) is \(h_N^{(2)}(u_a)\).

Because \(|\tanh|,|\tanh'|\le1\), equation (5) gives

\[
\|w_N(t)\|_\infty\le s(t),\qquad
\frac{\|\delta_a^{(2)}(t)\|_2}{\sqrt N}\le s(t),\qquad
\|\dot W_N(t)\|_F\le s(t)\dot s(t).
\]

Thus

\[
\|W_N(t)-W_N(0)\|_F\le s(t)^2/2,
\qquad
\|W_N(t)\|_{\mathrm{op}}\le M+s(t)^2/2.
\tag{8}
\]

The first equation in (5), the unit lengths of the inputs, and the triangle inequality imply

\[
\frac{\|\dot A_N(t)\|_F}{\sqrt N}
\le\dot s(t)\left(M+\frac{s(t)^2}{2}\right)s(t).
\]

Integrating with respect to \(s\) gives

\[
\frac{\|A_N(t)-A_N(0)\|_F}{\sqrt N}\le D_1(s(t)).
\tag{9}
\]

For every unit passive input \(u\), Lipschitz continuity of tanh, (8), and (9) now give

\[
\frac{\|h_N^{(1)}(t,u)-h_N^{(1)}(0,u)\|_2}{\sqrt N}
\le D_1(s(t)),
\]

\[
\begin{aligned}
\frac{\|h_N^{(2)}(t,u)-h_N^{(2)}(0,u)\|_2}{\sqrt N}
&\le\|W_N(t)-W_N(0)\|_{\mathrm{op}}
       \frac{\|h_N^{(1)}(0,u)\|_2}{\sqrt N}\\
&\quad+\|W_N(t)\|_{\mathrm{op}}
       \frac{\|h_N^{(1)}(t,u)-h_N^{(1)}(0,u)\|_2}{\sqrt N}\\
&\le D_2(s(t)).
\end{aligned}
\tag{10}
\]

The smallest singular value of \(H_N(t)/\sqrt N\) differs from that at zero by at most \(\|H_N(t)-H_N(0)\|_F/\sqrt N\). Therefore (1), (7), and (10) show, as long as \(s(t)\le s_0\), that

\[
\lambda_{\min}\left(\frac1N H_N(t)^TH_N(t)\right)\ge\lambda/8=\kappa.
\tag{11}
\]

The prediction tangent matrix \(K_N\) is the sum of the three positive semidefinite block Gram matrices; its readout block is \(H_N^TH_N/N\). In particular the exact residual equation and (11) give

\[
\dot r=-\frac2mK_Nr,
\qquad
\frac d{dt}\|r\|_2^2
=-\frac4m r^TK_Nr
\le-\frac{4\kappa}{m}\|r\|_2^2.
\]

Writing \(b=\|y\|_2\) and \(\alpha=2\kappa/m\), integration yields

\[
\|r(t)\|_2\le be^{-\alpha t},
\qquad
s(t)\le\frac2{\sqrt m}\int_0^tbe^{-\alpha\tau}d\tau
\le\frac{\sqrt m b}{\kappa}\le s_0/2.
\tag{12}
\]

At a putative first time with \(s=s_0\), the last inequality contradicts that equality. The finite ODE is smooth; on every bounded time interval before such a first exit, (8), (9), and the readout bound keep all parameters in a finite-dimensional bounded set. Its solution therefore continues. This proves (8)–(12) for all time, global existence on (7), and the sharper tail estimate

\[
s(\infty)-s(t)\le\frac{\sqrt m b}{\kappa}e^{-\alpha t}.
\tag{13}
\]

For a passive unit input, differentiating its forward pass and using (5) gives

\[
\frac{\|\dot h_N^{(2)}(t,u)\|_2}{\sqrt N}
\le\|\dot W_N(t)\|_{\mathrm{op}}
  +\|W_N(t)\|_{\mathrm{op}}
      \frac{\|\dot A_N(t)\|_F}{\sqrt N}.
\]

Set \(B=M+s_0^2/2\) and \(C_0=1+s_0^2(1+B^2)\). Since \(\|w_N\|_2/\sqrt N\le s_0\), substitution of the preceding velocity bounds proves

\[
\sup_{u\in S^{d-1}}|\partial_t f_N(t,u)|\le C_0\dot s(t),
\quad
\sup_u|f_N(t,u)-f_N(\infty,u)|
\le \frac{C_0\sqrt m b}{\kappa}e^{-\alpha t}.
\tag{14}
\]

The same integrable velocity bounds show that \(A_N,W_N,w_N\) themselves have finite limits in their indicated finite-dimensional norms. Thus the endpoint in (14) is the network at its parameter endpoint.

Finally, on the additional initialization event
\(\|A_N(0)\|_{\mathrm{op}}/\sqrt N\le R\), (9) gives the input estimate

\[
|f_N(t,u)-f_N(t,v)|\le L_0\|u-v\|_2,
\qquad
L_0=s_0B(R+D_1(s_0)),
\tag{15}
\]

uniformly for \(t\in[0,\infty]\). This follows by passing \(u-v\) successively through \(A_N\), tanh, \(W_N\), tanh, and the normalized readout pairing.

## 3. Probability of the initialization event

For fixed \(d\), \(\|A_N(0)\|_F^2/N\to d\) in probability by the scalar law of large numbers. Hence \(R=2\sqrt d\) is valid with probability tending to one. The contained Gaussian matrix-net proof in book III.F.2 gives

\[
\Pr(\|W_N(0)\|_{\mathrm{op}}>10)
\le2\,9^{2N}e^{-100N/8}\to0.
\]

For the Gram part of (7), the first-layer training tuples are iid \(N(0,I_m)\), because the \(u_a\) are orthonormal. The first-feature Gram therefore obeys

\[
Q_{N,ab}=\frac1N h_N^{(1)}(0,u_a)^Th_N^{(1)}(0,u_b)
\longrightarrow q\,\mathbf1_{\{a=b\}}
\]

in probability: different coordinates have independent odd tanh values, and the diagonal expectation is \(q\).

Conditional on the entire first matrix, the second-layer row tuples are independent centered Gaussian vectors with covariance \(Q_N\). Conditional variance of any averaged product of their tanh values is at most \(1/N\). Their conditional means converge to the Gaussian expectation at covariance \(qI_m\): couple the Gaussian vector as \(Q_N^{1/2}G_m\), use continuity of the positive semidefinite square root in fixed dimension, and bounded continuity of the product. At that diagonal covariance the off-diagonal expectations are zero and the diagonal expectation is \(\lambda\). Thus

\[
\frac1N H_N(0)^TH_N(0)\longrightarrow\lambda I_m
\]

in probability. Since the dimension \(m\) is fixed, entrywise convergence implies operator-norm convergence, which proves (7) with probability tending to one. This conditional independence is used only at initialization, before matrix reuse.

Denote by \(E_N\) the intersection of the three initialization events just proved. Then \(\Pr(E_N)\to1\), and all constants in (12)–(15) are independent of width on \(E_N\).

## 4. The compact-time population bridge and passive queries

The maintained book's theorem B.1, in `docs/04-continuing-flows.qmd`, covers exactly two hidden tanh layers with orthogonal normalized training inputs. Its loss is the unhalved sum. Taking its fixed multipliers \(\kappa_1=\kappa_2=\kappa_3=1/m\) gives exactly (5), with no clock ambiguity. The zero stored readout is permitted by its independent vanishing-supremum initialization option. Both tanh activations are bounded and continuously differentiable, with bounded Lipschitz derivatives. The Gaussian variances match its \(\sigma_1=\sigma_2=1\).

B.1 constructs a deterministic global autonomous population evolution and proves convergence in probability, uniformly on every fixed physical interval, of the specified finite measurements. Its proof explicitly obtains the continuous finite-flow limit before proving the raw-GD bridge. This proof, rather than a rate inferred from its GD statement, is the bridge used here.

For completeness, a finite passive panel is a permitted extension of that argument. Updates in (5) lie in the training input span, so for every fixed unit \(u\), exactly

\[
A_N(t)u=A_N(0)u+
\sum_{a=1}^m(u\cdot u_a)
\big(A_N(t)u_a-A_N(0)u_a\big).
\tag{16}
\]

Append the finitely many Gaussian roots \(A_N(0)u\) for the desired panel to the initial iid first-layer root tuple. Within the first layer these roots can be correlated with the training roots; the finite-program theorem explicitly permits iid tuples with arbitrary covariance. These roots remain independent of \(W_N(0)\). At each fixed transformed Euler mesh, append (16), tanh, the current matrix action (initialization plus its finite rank-one update list), tanh, and the current normalized readout pairing. This is a fixed finite program of the type used in B.1 and A.1. Its coordinate transform \(J\) is continuous with at most linear growth; bounded derivatives in its frozen root are not assumed.

The same-root transformed-state stability of B.1 controls the clock variables in RMS, the matrix difference in operator norm, and the readout difference in RMS, with bounded readout supremum. Equation (16) converts the clock errors into RMS passive first-field errors because \(J\) is Lipschitz in its clock. The forward product estimate then controls the passive top activation and prediction. Thus both finite and population proof-mesh errors for each fixed passive panel are \(O_T(\Delta)\), where \(\Delta\) is the auxiliary mesh, uniformly in width. At fixed \(\Delta\), A.1 and III.F give convergence of all required oracle contractions. Taking width to infinity first and then \(\Delta\) to zero proves

\[
\max_{u\in P}\sup_{0\le t\le T}|f_N(t,u)-f(t,u)|\to0
\quad\text{in probability}
\tag{17}
\]

for every finite passive panel \(P\) and fixed \(T\).

The finite program retains both orientations of the same matrix; its transpose response is not replaced by independent Gaussian randomness. The proofs used here are III.F.1–7 and A.1, read completely, together with B.1 read completely. This yields a qualitative bridge only. In particular, no bound uniform in an increasing number of program instructions or shrinking regularization is imported.

## 5. From the bridge to all times, the sphere, and independent compact initialization

Use (17) first on a countable dense subset of the sphere. Consistency of finite panels gives one deterministic limiting field on that subset. Inequality (15) passes to the limit: if its deterministic limiting values violated that inequality at two fixed inputs and one fixed time, convergence in probability of those values and \(\Pr(E_N)\to1\) would contradict (15). By continuity in time, the bound holds at all finite times. The field consequently has a unique \(L_0\)-Lipschitz extension to the whole sphere at every time.

For \(\rho>0\), take a finite \(\rho\)-net \(P_\rho\) on the sphere. On \(E_N\), the finite and limiting input Lipschitz bounds give

\[
\sup_{0\le t\le T}\sup_u|f_N(t,u)-f(t,u)|
\le\max_{v\in P_\rho}\sup_{0\le t\le T}|f_N(t,v)-f(t,v)|+2L_0\rho.
\]

Given a tolerance, choose the finite net first and then use (17). This proves compact-time, whole-sphere convergence in probability.

The same fixed-time limit argument transfers (14) in its two-finite-time form to the population field. Therefore \(f(t,\cdot)\) is uniformly Cauchy as \(t\to\infty\), has a continuous endpoint, and satisfies

\[
\sup_u|f(t,u)-f(\infty,u)|
\le \frac{C_0\sqrt m b}{\kappa}e^{-\alpha t}.
\tag{18}
\]

Put \(D=C_0\sqrt m b/\kappa\). For every fixed \(T\), on \(E_N\),

\[
\sup_{t\in[0,\infty]}\sup_u|f_N(t,u)-f(t,u)|
\le\sup_{0\le t\le T}\sup_u|f_N(t,u)-f(t,u)|+2De^{-\alpha T}.
\]

Choose \(T\) first to make the deterministic last term small, then send \(N\to\infty\). This proves (2), including the endpoint, without interchanging an uncontrolled width and infinite-time limit.

Apply (2) separately at widths \(n\) and \(q_n\). The triangle inequality through their same deterministic population predictor proves (3). A union bound is sufficient; independence is compatible with the construction but is not needed for this implication. This completes the qualitative theorem.

## 6. Hidden learning is retained at a fixed label scale

The construction trains every block and uses the exact canonical nonlinear vector field. It also has a population certificate of actual hidden motion whenever \(y\ne0\).

Let \(g_a\) be the independent standard Gaussian training roots in the first population, \(H_a^{(1)}(0)=\tanh g_a\), and \(\xi_a=W^{(2)}_0H_a^{(1)}(0)\). Within the second population the \(\xi_a\) are independent \(N(0,q)\). Define the second-population fields

\[
S=\frac2m\sum_b y_b\tanh\xi_b,
\qquad U_a=S\tanh'(\xi_a).
\]

The readout satisfies \(W^{(3)}(t)/t\to S\) in \(L^2\) and is bounded in supremum by \(O(t)\). The equations and bounded-multiplier continuity then give the strong second-order initial increments

\[
\frac{W^{(2)}(t)-W^{(2)}_0}{t^2/2}
\longrightarrow\frac2m\sum_a y_a U_a\otimes H_a^{(1)}(0)
\quad\text{in Hilbert--Schmidt norm},
\tag{19}
\]

\[
\frac{Z_a^{(1)}(t)-g_a}{t^2/2}
\longrightarrow\frac{2y_a}{m}\tanh'(g_a)(W^{(2)}_0)^*U_a
\quad\text{in }L^2.
\tag{20}
\]

To justify these limits without a nonexistent global Frechet derivative of tanh on an \(L^2\) ball, first divide the readout equation's integral by \(t\). Strong continuity of the bounded activation gives its displayed limit. Next \(\Delta_a^{(2)}(t)/t\to U_a\) in \(L^2\): subtract the varying readout first, and use bounded-multiplier continuity for the fixed limit \(S\). The actual adjoint is bounded, the trained increment tends to zero, and the first gate is a bounded multiplier, so \(\Delta_a^{(1)}(t)/t\to\tanh'(g_a)(W^{(2)}_0)^*U_a\). Integrating the parameter equations, with \(r_a(t)\to-y_a\), gives (19) and (20).

The squared Hilbert--Schmidt norm of the right side of (19) is

\[
\frac{4q}{m^2}\sum_a y_a^2\,\mathbb E_2[U_a^2]>0.
\]

Indeed \(\mathbb E_1[H_a^{(1)}(0)H_b^{(1)}(0)]=q\mathbf1_{a=b}\); if \(y\ne0\), the random variable \(S\) has positive variance, and \(\tanh'(\xi_a)>0\) everywhere.

For every \(a\) with \(y_a\ne0\), the right side of (20) is also nonzero. The actual adjoint identity gives

\[
\mathbb E_1\left[H_a^{(1)}(0)(W^{(2)}_0)^*U_a\right]
=\mathbb E_2[\xi_aU_a]
=\frac{2y_a}{m}\mathbb E[\xi\tanh\xi\tanh'(\xi)]\ne0,
\]

where \(\xi\sim N(0,q)\). Cross terms vanish by independence and oddness of \(\tanh\xi_b\); the final integrand is positive except at zero. Therefore the adjoint field is nonzero, and multiplication by the everywhere positive \(\tanh'(g_a)\) does not annihilate it. The bounds and limits are at fixed nonzero labels and do not decay with width.

These certificates establish nonzero middle-parameter and first-hidden motion near initialization. They do not assert a uniform lower bound on hidden velocity at every later time. Tanh is also nonaffine under both nondegenerate initialized Gaussian laws; its best affine-fit error is positive. Thus the construction is not an affine activation or readout-only replacement.

## 7. The exact remaining finite-width bias obstruction

The target would require, for an independently generated compact predictor \(\widetilde f_n\),

\[
\Pr\left\{\sup_{t\in[0,\infty],u\in S^{d-1}}
|f_n(t,u)-\widetilde f_n(t,u)|
\le C_{d,m,y,\delta}/\sqrt n\right\}\ge1-\delta
\]

for all sufficiently large \(n\), with no logarithmic factor in the error and only polylogarithmic compact storage. This theorem is not proved here.

There are two distinct quantitative obligations. First, the dense network must be compared with a common deterministic object at the stated rate, including its finite-width expectation bias. Second, the compact construction must approximate that deterministic object to the same tolerance with its allowed resources. Neither follows from (2).

For example, at a fixed query \((t,u)\), a concentration estimate
\(f_n-\mathbb Ef_n=O_{\mathbb P}(n^{-1/2})\) leaves
\(\mathbb Ef_n-f\) uncontrolled. Two independent copies have the same bias, so their difference can concentrate at root width even when each has a much larger common bias. The deterministic sequence \(X_n=b+n^{-1/4}\) is the minimal illustration: independent-copy differences are zero, but the bias from \(b\) is \(n^{-1/4}\). This observation is a proof-route obstruction, not evidence that the actual network has such a bias.

The complete B.1 proof uses a fixed transformed Euler mesh. Its oracle correction contains finitely many empirical contractions minus their population values. It proves that each discrepancy tends to zero for a fixed program, then sends the mesh size to zero. A.1 additionally chooses smooth cutoffs first, takes width to infinity, and removes the approximation afterwards. III.F.5 removes singular-query regularization after width convergence. None supplies a rate uniform in the growing program length, cutoff, or rank-loss regularization needed to set the final error to \(n^{-1/2}\). In particular, the displayed \(O_T(\Delta)\) time-mesh error cannot be balanced against an unstated quantitative width error.

The deterministic bounds in Sections 2–5 resolve long-time propagation and spatial equicontinuity for the qualitative theorem. They do not estimate the finite-width source discrepancy. A direct route to the strict target therefore still needs a quantitative weak-bias and fluctuation theorem for the reused-matrix nonlinear flow, together with a compact approximation theorem with an explicit accuracy cost. Taking \(q_n=\lceil\log(en)\rceil\) in a qualitative convergence statement resolves neither obligation.

## Source provenance and check record

Source HEAD inspected before writing: `3834145d910202a84824d943fe7d7f65714d96f2`. The common index was empty. Concurrent untracked studies and maintenance modifications were observed only as metadata and were not read or changed. Only this assigned report was written; no Git operation or experiment was performed.

Read completely for the argument:

- `docs/index.qmd` and `docs/notation.qmd`.
- `docs/04-continuing-flows.qmd`, B.1, physical lines 7–648: theorem hypotheses, transformed equations, global well-posedness, fixed-mesh width passage, exact-GD bridge, and scope. Stable heading: `sec-docs-global-nonlinear-l1903`.
- `docs/02-gaussian-reuse.qmd`, A.1, physical lines 1803–1823: complete continuous-value specialization and proof. Stable heading: `sec-docs-global-nonlinear-l1842`. A.2–A.4 and the introductory exact Gaussian-conditioning sections were also read; the proof above uses bounded-multiplier continuity from A.4, not an unproved source derivative formula.
- `docs/12-three-sample-learning.qmd`, III.F.1–7, physical lines 316–728: complete fixed-program law, matrix bound, adaptive conditioning, response identity, singular-query proof, scalar feedback, and joint bounded action/adjoint construction. Stable heading: `sec-docs-special-data-limits-l3785`.

Recorded SHA-256 hashes:

| Source | SHA-256 |
| --- | --- |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `docs/04-continuing-flows.qmd` | `78728dbbcc551392f7dd6cf7b91bad42324e5b540655d4242e830e9c38774a43` |
| `docs/02-gaussian-reuse.qmd` | `a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92` |
| `docs/12-three-sample-learning.qmd` | `06d6e45f1d7d6c280fb0c5dcac3303b49d56bec4d4a7df632cd73af5091d1d15` |

Author checks: exact mean-loss factors in (5); initial readout zero; the orthogonal-input reconstruction (16); the minimum-singular-value perturbation and first-exit margins; the order of the width/time/input-net limits; zero labels; both Gaussian layers' conditioning; the endpoint convention outside the fitting event; all storage counts; and the distinction between qualitative convergence and a strict root-width estimate. These are proof checks, not an independent review or a machine-verified result.
