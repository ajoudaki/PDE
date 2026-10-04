# Independent check of the initialized Gram-gap/count argument

2026-10-04. Scoped internal mathematical check, not a promotion review.

**Verdict: the geometry theorem passes.** For fixed input dimension
\(d\ge2\), fixed hidden depth and uniformly strip-bounded activations, a
positive initialized covariance gap implies

\[
m\le C[\log(e+1/\bar\gamma)]^\beta,\qquad
\bar\gamma=\min\{1,\lambda_{\min}(Q^{(L)})\},\qquad
\beta=\frac{3(d-1)}2.
\tag{1}
\]

The exponent follows from a depth-stable Hilbert derivative bound of
order \(3/2\), Fourier approximation and a nullspace trace estimate.
The Gaussian products need not be independent, and the real approximation
rank has no extra factor two.

If the separately pending source theorem supplies the label regime
\(Y\le c\lambda\), where
\(\lambda=\min\{1,\lambda_{\min}(Q^{(L)})/m\}\), then (1) gives the
gap-only sufficient condition with exactly exponent \(\beta\), without
an extra positive power. This report does not verify that enlarged source
label regime or the whole-query source construction.

## Scope and versions

The two complete new scientific inputs were:

| File | SHA-256 |
| --- | --- |
| GEOMETRY_GAMMA_ONLY_LABELS.md | f0ef616c05112f5b6425ec67e7bc56fb3da4e08b94ad820e7ef220f57a8c62f1 |
| SAMPLE_COUNT_REFINEMENT.md | c04d0a21e95988191a4612e406504c515cf0073f62663cfbd455c499d6cc6d4c |

The geometry hash identifies the original version reviewed, before the
author's separately announced appended corollary. Its complete proof
was checked, and the exact-\(\beta\) substitution was checked from the
named synthesis and the explicit pending-input premise.

The second file is the root synthesis named in the assignment. Its runtime
claims are compared against the runtime construction already independently
reconstructed in STORAGE_QUADRATIC_CHECK.md; that prior report was not
changed. Shared instructions were reread, and the already-read required
canonical-notation and rigorous-math skills remain applicable. No budget
proof, whole-query source report, other route file, other study, book or
external scientific input was fetched. No experiment was used.

The assertion “\(Y\le c\lambda\) is sufficient for the actual source
theorem” is an assumed, separately checked input throughout this report.
It was pending when this assignment began; later coordinator notification
that its separate checks completed is not a substitute for a source audit
within this report. The synthesis's improved source dimension is likewise
a separate input for the storage integration audit.

## 1. Setup and the Hilbert realization

Write \(v_a=x_a/\sqrt d\in S^{d-1}\). Suppose every activation is real
on the real axis, holomorphic on \(|\operatorname{Im}z|<b\), and bounded
there by a common constant \(M\ge1\). Cauchy's formula on the circle of
radius \(b/2\), centered at a real point, gives

\[
\sup_{x\in\mathbb R}|\phi_\ell^{(p)}(x)|
\le M p! a^p,\qquad a=2/b,\qquad p\ge0.
\tag{2}
\]

The initialized covariance is the finite Gaussian recursion

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}).
\tag{3}
\]

Set \(H_0=\mathbb R^d\) and \(\Phi_0(v)=v\). For a separable real Hilbert
space \(H\), an orthonormal basis \((e_j)\) and independent standard
Gaussian variables \((\xi_j)\) define

\[
G(u)=\sum_j\langle u,e_j\rangle_H\xi_j.
\tag{4}
\]

The difference of any two finite partial sums is Gaussian with variance
equal to the squared Hilbert norm of the omitted coefficient vector.
Its \(L^r\) norm therefore tends to zero for every finite \(r\ge1\).
Thus (4) defines a bounded linear map \(H\to L^r\), consistently across
these spaces, with covariance \(\mathbb E[G(u)G(v)]=\langle u,v\rangle_H\).
For integer \(p\ge1\), the Gaussian moment gives

\[
\|G(u)\|_{L^{2p}}
=[(2p-1)!!]^{1/(2p)}\|u\|_H
\le\sqrt{2p}\,\|u\|_H,
\tag{5}
\]

since every factor of \((2p-1)!!\) is at most \(2p\).

At layer \(\ell\), take an isonormal map \(G_\ell\) on \(H_{\ell-1}\),
let \(H_\ell\) be the real \(L^2\) space of its countable Gaussian
coordinates, and define

\[
\Phi_\ell(v)
=\phi_\ell(G_\ell(\Phi_{\ell-1}(v)))\in H_\ell.
\tag{6}
\]

These Hilbert spaces are separable. The previous feature in (6) is a
deterministic Hilbert vector when supplied to the next isonormal map.
By induction, the preactivation vector at the finite inputs is jointly
Gaussian with covariance \(Q^{(\ell-1)}\). Applying (3) proves

\[
\langle\Phi_\ell(v_a),\Phi_\ell(v_b)\rangle_{H_\ell}
=Q^{(\ell)}_{ab}.
\tag{7}
\]

This realizes only the deterministic initialized covariance. No trained
population model or time-dependent Gaussian law has been introduced.

## 2. Differentiation and the ordered composition formula

Put \(D=d-1\). The source uses the smooth periodic sphere parameterization

\[
v(\theta)=\left(
\cos\theta_1,\,
\sin\theta_1\cos\theta_2,\ldots,\,
\left(\prod_{j=1}^{D-1}\sin\theta_j\right)\cos\theta_D,\,
\left(\prod_{j=1}^{D-1}\sin\theta_j\right)\sin\theta_D
\right),
\tag{8}
\]

with \(v(\theta)=(\cos\theta,\sin\theta)\) for \(D=1\). It is surjective
onto \(S^{d-1}\). Every pure derivative in one angular coordinate has
Euclidean norm at most \(\sqrt d\), uniformly in order and all angles:
each coordinate is a product of sines and cosines, and differentiating
repeatedly in one angle preserves the bound one for each coordinate.

Differentiability of (6) precedes the quantitative estimate. If \(u(t)\)
is smooth into \(H\), then \(G(u(t))\) is smooth into every finite \(L^r\).
For bounded \(\phi''\), Taylor's remainder gives

\[
\|\phi(X+h)-\phi(X)-\phi'(X)h\|_{L^r}
\le\frac12\|\phi''\|_\infty\|h\|_{L^{2r}}^2.
\tag{9}
\]

This proves the first derivative of the composition. Repeating it for
\(\phi^{(p)}\), and differentiating finite products using Hölder with
sufficiently large finite exponents, proves every higher derivative.
Every Gaussian derivative factor is available in all required moment
spaces. The same argument supplies continuity in the other angles.
No quantitative mixed derivative estimate is needed below.

For one angular variable, write \(u=\Phi_{\ell-1}\) and \(g=G_\ell(u)\).
For \(k\ge1\), the ordered-composition form of Faà di Bruno is

\[
\frac{d^k}{dt^k}\phi_\ell(g)
=k!\sum_{p=1}^k\frac{\phi_\ell^{(p)}(g)}{p!}
\sum_{\substack{j_1+\cdots+j_p=k\\j_i\ge1}}
\prod_{i=1}^p\frac{G_\ell(u^{(j_i)})}{j_i!}.
\tag{10}
\]

To check the combinatorial factor, group compositions by multiplicities
\(m_j\) of their parts. There are \(p!/\prod_jm_j!\) orderings, so
the coefficient becomes \(k!/\prod_j[m_j!(j!)^{m_j}]\), with
\(\sum_jm_j=p\) and \(\sum_jjm_j=k\), as obtained by repeated
differentiation. The \(p!\) denominator in (10) is therefore essential.

Hölder applied to the \(p\) squared factors, followed by (5), gives

\[
\left\|\prod_{i=1}^pG_\ell(u^{(j_i)})\right\|_{L^2}
\le\prod_{i=1}^p\|G_\ell(u^{(j_i)})\|_{L^{2p}}
\le(2p)^{p/2}\prod_{i=1}^p\|u^{(j_i)}\|_{H_{\ell-1}}.
\tag{11}
\]

This holds for arbitrary Gaussian correlations, including identical
factors. No independence of angular derivatives is used.

## 3. The order \(3/2\) is stable across depth

Let

\[
A=\max\{M,\sqrt d,1\},\qquad
T_0=aA\sqrt{2e},\qquad B_\ell=(1+T_0)^\ell.
\]

We prove, for each pure angular derivative,

\[
\sup_\theta\|\partial_{\theta_s}^k
\Phi_\ell(v(\theta))\|_{H_\ell}
\le A B_\ell^k(k!)^{3/2},\qquad k\ge0.
\tag{12}
\]

For \(\ell=0\), the bound after (8) gives this with \(B_0=1\).
For \(k=0\) at higher layers, it follows from bounded activation values.
For \(k\ge1\), insert (2), (11) and the previous-layer bound into (10).
The activation derivative's \(p!\) cancels the denominator, giving

\[
\|\Phi_\ell^{(k)}\|
\le M k! B_{\ell-1}^k
\sum_{p=1}^k(aA)^p(2p)^{p/2}
\sum_{j_1+\cdots+j_p=k}\prod_{i=1}^p\sqrt{j_i!}.
\tag{13}
\]

For every positive composition of \(k\) into \(p\) parts,

\[
\prod_i j_i!\le(k-p+1)!\le k!/p!.
\tag{14}
\]

For the first inequality, transfer a unit from any non-largest part
greater than one to a largest part. If the receiving part is \(a\)
and the donating part is \(b\le a\), the factorial product changes by
\((a+1)/b\ge1\). Iteration leaves \((k-p+1,1,\ldots,1)\).
For the second,
\(k!/(k-p+1)!=k(k-1)\cdots(k-p+2)\ge p(p-1)\cdots2=p!\).
Both endpoint cases \(p=1,k\) are included.

Moreover, \(\log p!\ge\int_1^p\log t\,dt\ge p\log p-p\), so
\((2p)^{p/2}/\sqrt{p!}\le(2e)^{p/2}\).
There are \(\binom{k-1}{p-1}\) ordered compositions. Therefore (13)
becomes

\[
\begin{aligned}
\|\Phi_\ell^{(k)}\|
&\le M B_{\ell-1}^k(k!)^{3/2}
\sum_{p=1}^k\binom{k-1}{p-1}T_0^p\\
&=M B_{\ell-1}^k(k!)^{3/2}T_0(1+T_0)^{k-1}\\
&\le A[B_{\ell-1}(1+T_0)]^k(k!)^{3/2}.
\end{aligned}
\]

This proves (12). Depth changes \(B_\ell\), but not the factorial order.
All constants are independent of the sample count, dataset, width,
labels and gap.

## 4. Fourier truncation and its real rank

Set \(F(\theta)=\Phi_L(v(\theta))\), and complexify \(H_L\) for its
Bochner Fourier coefficients

\[
\widehat F(k)=\frac1{(2\pi)^D}
\int_{\mathbb T^D}F(\theta)e^{-ik\cdot\theta}\,d\theta.
\]

For \(r=|k|_\infty>0\), integrate by parts \(q\) times in a coordinate
with \(|k_s|=r\). Periodicity removes all boundary terms. With \(B=B_L\),

\[
\|\widehat F(k)\|\le A B^q(q!)^{3/2}/r^q.
\tag{15}
\]

Put \(x=(r/(2B))^{2/3}\). If \(x\ge2\), choose \(q=\lfloor x\rfloor\).
Then \(q\ge x/2\), and \(q!\le q^q\) gives

\[
\frac{B^q(q!)^{3/2}}{r^q}
\le\left(\frac{Bq^{3/2}}r\right)^q
\le2^{-q}\le e^{-cr^{2/3}},
\qquad c=\frac{\log2}{2(2B)^{2/3}}.
\]

If \(x<2\), then \(cr^{2/3}<\log2\), so the elementary bound
\(\|\widehat F(k)\|\le A\) proves, also at frequency zero,

\[
\|\widehat F(k)\|\le2A e^{-c|k|_\infty^{2/3}}.
\tag{16}
\]

The shell at radius \(r\ge1\) has
\((2r+1)^D-(2r-1)^D\le2D(2r+1)^{D-1}\) frequencies.
Thus the coefficient norms are summable. Their uniformly convergent
series equals \(F\): product Fejér kernels are positive, have integral
one and concentrate at zero, so uniform continuity proves their uniform
convergence for Hilbert-valued \(F\). Absolute summability identifies
that limit with the series.

Split the exponential in (16) into two equal factors. Outside
\(|k|_\infty\le J\), the first factor is at most
\(e^{-(c/2)J^{2/3}}\), and the sum of the second factor times the shell
count is finite. Therefore a structural \(E\ge1\) gives

\[
\sup_\theta\left\|F(\theta)-
\sum_{|k|_\infty\le J}\widehat F(k)e^{ik\cdot\theta}\right\|
\le E e^{-\tau J^{2/3}},\qquad \tau=c/2.
\tag{17}
\]

Because \(F\) is real, conjugate frequencies \(k,-k\) combine into

\[
2\operatorname{Re}\widehat F(k)\cos(k\cdot\theta)
-2\operatorname{Im}\widehat F(k)\sin(k\cdot\theta).
\]

Each pair uses at most two real vectors for two frequencies; the zero
coefficient is real. Hence the truncated polynomial takes values in a
real subspace \(E_J\) of dimension at most \(R_J=(2J+1)^D\).
For its orthogonal projection \(P_J\), best approximation and surjectivity
of (8) imply

\[
\sup_{v\in S^{d-1}}\|(I-P_J)\Phi_L(v)\|
\le\epsilon_J:=Ee^{-\tau J^{2/3}}.
\tag{18}
\]

This subspace is only a proof device for the geometric count. It is not
an extra representation retained by the compressed runtime.

## 5. The trace estimate and the exact exponent

Define \((K_J)_{ab}=\langle P_J\Phi_L(v_a),P_J\Phi_L(v_b)\rangle\).
It has rank at most \(R_J\). Orthogonality implies that
\(Q^{(L)}-K_J\) is exactly the Gram of the projection errors. It is
positive semidefinite with trace at most \(m\epsilon_J^2\).

Let \(\Pi\) be the sample-space orthogonal projection onto \(\ker K_J\).
Since \(Q^{(L)}\succeq\bar\gamma I_m\),

\[
\begin{aligned}
\bar\gamma(m-R_J)
&\le\bar\gamma\operatorname{tr}\Pi
\le\operatorname{tr}(\Pi Q^{(L)})\\
&=\operatorname{tr}[\Pi(Q^{(L)}-K_J)]
\le\operatorname{tr}(Q^{(L)}-K_J)
\le m\epsilon_J^2.
\end{aligned}
\tag{19}
\]

For the penultimate step, put \(\mathcal E=Q^{(L)}-K_J\succeq0\).
Then
\(\operatorname{tr}(\Pi\mathcal E)
=\operatorname{tr}(\mathcal E^{1/2}\Pi\mathcal E^{1/2})
\le\operatorname{tr}\mathcal E\), since \(0\preceq\Pi\preceq I\).
No commutation is required. If \(m\ge2R_J\), (19) gives

\[
\bar\gamma\le2E^2e^{-2\tau J^{2/3}}.
\tag{20}
\]

For \(m\ge2\cdot6^D\), put \(t=(m/2)^{1/D}\ge6\) and
\(J=\lfloor(t-1)/2\rfloor\). Then \(R_J\le m/2\) and
\(J\ge(t-3)/2\ge t/4\). Equation (20) yields

\[
\bar\gamma\le C_0e^{-b_0m^{2/(3D)}},
\qquad b_0=2\tau4^{-2/3}2^{-2/(3D)}>0.
\tag{21}
\]

Enlarge the structural \(C_0\ge e\) to cover
\(m<2\cdot6^D\), using \(\bar\gamma\le1\). Taking logarithms proves

\[
m\le b_0^{-3D/2}[\log(C_0/\bar\gamma)]^{3D/2}
\le C[\log(e+1/\bar\gamma)]^{3D/2}.
\tag{22}
\]

This is (1), with \(\beta=3(d-1)/2\). The trace step cancels the factor
\(m\) that a single-null-vector estimate would unnecessarily retain.
The hypothesis concerns the deterministic initialized covariance gap,
not an arbitrary realized finite-width Gram gap. It imposes no new
input-separation, sign or training-time concentration condition.
For \(d=1\), the two-point sphere gives \(m\le2\) under a positive gap.

## 6. Conditional substitution into the new label regime

Let \(\gamma=\lambda_{\min}(Q^{(L)})>0\),
\(\bar\gamma=\min(1,\gamma)\), and
\(\lambda=\min(1,\gamma/m)\). Since
\(\bar\gamma/m\le1\) and \(\bar\gamma/m\le\gamma/m\),
\(\lambda\ge\bar\gamma/m\).
Set \(s=\log(e+1/\bar\gamma)\) and choose \(C_1\ge1\) in (22), so
\(m\le C_1s^\beta\). Then

\[
\lambda\ge\frac{\bar\gamma}{C_1s^\beta}.
\tag{23}
\]

Assume that \(0<Y\le c_{\rm src}\lambda\) suffices for the source
theorem, as the separately assigned input. The gap-only condition

\[
0<Y\le\frac{c_{\rm src}}{C_1}
\frac{\bar\gamma}{[\log(e+1/\bar\gamma)]^\beta}
\tag{24}
\]

implies that source condition by (23). Its exponent is exactly \(\beta\).
No step requires an additional \(\varepsilon>0\).

The original geometry note instead uses the older source threshold
\(c\lambda e^{-C\sqrt{\log(em)}}\). Its additional exponential becomes
\(e^{-C'\sqrt{\log(es)}}\). The inequality
\(C'\sqrt{\log s}\le\varepsilon\log s+C'^2/(4\varepsilon)\)
bounds that factor below by a constant times \(s^{-\varepsilon}\),
producing the older \(\beta+\varepsilon\) corollary. This is compatible
with (24), but is not a proof of the enlarged source input.

Equation (24) removes explicit \(m\) by using the largest sample count
permitted by the gap. It does not improve the numerical threshold from
that same dataset's actual \(m\) in \(c_{\rm src}\lambda\).
Neither argument proves optimality or a matching obstruction.

## 7. Integration audit of SAMPLE_COUNT_REFINEMENT.md

The synthesis is consistent with the previously checked runtime,
conditional on its separate source inputs.

**Reference and optimizer scope.** The original equations retain the
canonical factors \(2/m\), \(2/(mn)\), \(2/m\), Gaussian initialization,
zero readout and physical time. The different compressed optimizer is
disclosed at the beginning and in the construction. Its algebraic
effective readout makes the internal residual equal to labels minus the
current compressed output. Its positive residual Gram is specified
without claiming it is the true parameter-gradient tangent Gram.
Thus ordinary-gradient-flow compression is not asserted under the new
storage count.

**Output constant (5).** The checked finite-horizon runtime estimate is

\[
C\lambda^{-1/2}e^{CY/\lambda^{5/2}}n^{-1}
\exp\{(CY^2/\lambda^{7/2})\sqrt{\ell_n}\}.
\tag{25}
\]

At \(\ell_n\ge C(1+Y^4/\lambda^7)\), this is at most
\(C_{\rm core}/\sqrt n\), where
\(C_{\rm core}=C\lambda^{-1/2}e^{CY/\lambda^{5/2}}\).
The weighted-norm tail proof gives \(C_{\rm tail}n^{-p}\), with
structural \(p\ge1\), after a sufficiently large horizon constant.
The tail constant is independent of width and time, though it may
have additional fixed-data dependence. For fixed data, enlarge \(n_0\)
so that \(n^{p-1/2}\ge C_{\rm tail}/C_{\rm core}\).
The tail is then at most \(C_{\rm core}/\sqrt n\). Absorbing the finite
sum into the structural multiplicative constant proves precisely the
synthesis's conservative formula

\[
C_{\rm err}\le C\lambda^{-1/2}\exp(CY/\lambda^{5/2}).
\]

This is valid because the synthesis expressly permits the enlarged
fixed-data width threshold. It neither suppresses the tail constants
without justification nor gives a uniform formula for that threshold.

**All fixed and moving storage.** The runtime retains \(O(R)\) neurons
per layer, and \(O(R^2)\) entries in its metrics, optional inverses or
factorizations, moving mixers and small fixed initialized arrays.
First-layer weights cost \(O(dR)\). Exact preservation of the full-rank
initial Gram forces \(m\le N_L\le9R\). Thus every \(N_\ell m\) training
feature/response cache and each \(m\times m\) Gram/solve cache also fits
in \(O(R^2)\) at fixed depth. Internal residual coordinates are counted,
and data and labels add \(m(d+1)\). The Hilbert/Fourier proof above
requires no additional stored arrays.

Consequently, if the separate whole-query source result supplies
\(R\le C\lambda^{-1}\ell_n^a\), the checked runtime does give

\[
\operatorname{size}\le C\lambda^{-2}\ell_n^{2a}+Cm(d+1).
\]

The disappearance of the old \(m^4\) term rests on that improved source
bound; this geometry check does not independently certify it.
The logarithmic simplification in synthesis formula (8) is correct:
if \(\ell_n\ge\log(e/\lambda)\), then

\[
\ell_n^{2d(L+4)+2}
[\ell_n+\log(e/\lambda)]^{2d}
\le2^{2d}\ell_n^{2d(L+5)+2}=2^{2d}\ell_n^{2a}.
\]

This concerns a logarithmic gap factor, not domination of a polynomial
in \(m\) by \(\log n\). For \(d=2,L=2\), \(a=15\), so the stated
\(\log^{30}(en)\) factor is correct. For tanh, \(Q_{aa}\le1\) implies
\(\gamma\le\operatorname{tr}Q/m\le1\), so the cap is inactive.

**Source-check status.** The frozen synthesis header marks the
samplewise-budget refinement as still being checked. Its descriptions
of the “complete enlarged source/carrier label range” or conditions
“proved here” must be reconciled with the final separate source-check
status. The coordinator later reported completion of those checks,
but this geometry report does not independently discharge that proof
obligation. No other examined integration claim contradicts the runtime.

The initialized geometry theorem and the exact-\(\beta\) substitution
are independently reconstructed. The combined runtime conclusions are
conditional here on the separately assigned source-label and whole-query
source results.
