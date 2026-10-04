# A Gram-gap-only sufficient label condition from initialization geometry

**Latest checked result, 2026-10-04.** The separate-sample-budget proof and
its independent check now supply the full-source sufficient condition
\(Y\le c\lambda\). With the exact gap
\(\gamma=\lambda_{\min}(Q^{(L)})>0\), its cap
\(\bar\gamma=\min\{1,\gamma\}\), and
\(\beta=3(d-1)/2\), the gap-only sufficient condition improves to

\[
Y\le\frac{c\bar\gamma}
{[\log(e+1/\bar\gamma)]^{\beta}}.
\tag{Latest}
\]

There is no \(\varepsilon\) loss. Section 8 gives the exact implication
and attribution. The best checked sample-aware condition remains
\(Y\le c\min\{1,\gamma/m\}\); using geometry to eliminate \(m\)
does not enlarge that numerical threshold for a fixed dataset and does
not establish optimality.

The following original proof is preserved. Its frozen pre-addendum SHA256
is `f0ef616c05112f5b6425ec67e7bc56fb3da4e08b94ad820e7ef220f57a8c62f1`.
Its \(\beta+\varepsilon\) conclusion remains a valid historical corollary
of the earlier source condition. The Hilbert, Fourier and sample-count
arguments below are unchanged.

2026-10-04. Bounded continuation and complete check of the supervisor's
Hilbert-feature approximation argument. Scientific inputs were the complete
`GENERAL_ANALYTIC_COMPRESSION.md`, the complete
`DATASET_MAXIMUM_REFINEMENT.md`, and the supervisor's proposed argument.
No other study sources, trained-population premise, numerical experiments,
or training-time concentration estimates were used.

**Internally checked conditional corollary of the existing compression
theorem.** Let the input dimension \(d\ge2\), hidden depth \(L\ge2\), and
activation strip bounds be fixed. Let \(Q^{(L)}\) be the deterministic
initialized covariance defined below and suppose
\(Q^{(L)}\succeq\gamma I_m\), where \(0<\gamma\le1\). There is a structural
constant \(C\) such that

\[
m\le C[\log(e+1/\gamma)]^{3(d-1)/2}.
\tag{1}
\]

Consequently, for every fixed \(\varepsilon>0\), the already checked full
analytic compression theorem applies under the sufficient label condition

\[
0<Y\le
\frac{c_\varepsilon\gamma}
{[\log(e+1/\gamma)]^{3(d-1)/2+\varepsilon}},
\qquad Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
\tag{2}
\]

Here \(c_\varepsilon>0\) depends only on \(\varepsilon,d,L\), the common
activation strip width, and its uniform bound. The case \(Y=0\) is trivial.
An arbitrary positive spectral gap can be replaced by its minimum with one.
This removes explicit sample count from a sufficient condition by proving
that sample count and the population initialization gap cannot vary
independently. It is **not an enlarged numerical label threshold for a fixed
dataset**, and no optimality of its logarithmic exponent is claimed.

## 1. The exact assumption and the initialized covariance

Write \(v_a=x_a/\sqrt d\in S^{d-1}\). The network, Gaussian initialization,
loss and training flow are exactly those of
`GENERAL_ANALYTIC_COMPRESSION.md`: the first preactivation is \(Av_a\),
the subsequent preactivations are \(W^{(\ell)}h^{(\ell-1)}\), and the
prediction is \(w^\top h^{(L)}/n\). The entries of \(A_0\) are independent
standard normals, those of each \(W_0^{(\ell)}\) are independent
\(N(0,1/n)\), all arrays are independent, and \(w_0=0\).

The activation assumption used here is the actual, stronger assumption of
that theorem: every \(\phi_\ell\) is holomorphic and bounded by \(M\) on
the fixed horizontal strip \(|\operatorname{Im}z|<b\), and is real on the
real axis. Enlarge \(M\) to at least one. Cauchy's formula on real-centered
circles of radius \(b/2\) gives

\[
\sup_{x\in\mathbb R}|\phi_\ell^{(p)}(x)|
\le M p! a^p,\qquad a=2/b,\qquad p\ge0.
\tag{3}
\]

The population initialization covariance is defined only by the finite
Gaussian recursion

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\qquad Z\sim N(0,Q^{(\ell-1)}).
\tag{4}
\]

The gap in (1) is for (4), as in the theorem being refined. A realized
finite-width Gram gap by itself is not the hypothesis of (1).

## 2. A canonical Hilbert feature representation of (4)

Put \(H_0=\mathbb R^d\) and \(\Phi_0(v)=v\). If \(H\) is a separable
real Hilbert space, choose an orthonormal basis \((e_j)\), independent
standard normals \((\xi_j)\), and define the isonormal map

\[
G(u)=\sum_j\langle u,e_j\rangle_H\xi_j.
\]

The series converges in every finite \(L^r\) for \(u\in H\), with
\(\mathbb E[G(u)G(v)]=\langle u,v\rangle_H\). It is a continuous linear
map \(H\to L^r\). For integer \(p\ge1\), specifically,

\[
\|G(u)\|_{L^{2p}}\le\sqrt{2p}\,\|u\|_H,
\tag{5}
\]

because the Gaussian moment \((2p-1)!!\) is at most \((2p)^p\).

Recursively take an isonormal map \(G_\ell\) on \(H_{\ell-1}\), let
\(H_\ell\) be the real \(L^2\) space of its Gaussian coordinates, and set

\[
\Phi_\ell(v)=\phi_\ell\bigl(G_\ell(\Phi_{\ell-1}(v))\bigr)
\in H_\ell.
\tag{6}
\]

These spaces are separable; one can equivalently restrict each space to the
closed span of the feature values. By construction,

\[
\langle\Phi_\ell(v_a),\Phi_\ell(v_b)\rangle_{H_\ell}
=Q^{(\ell)}_{ab}.
\tag{7}
\]

This construction represents the initialized covariance only. In particular,
the Gaussian variables in (6) do not describe trained-neuron laws.

## 3. Hilbert differentiability and the derivative bound

Let \(D=d-1\). Use the standard surjective periodic sphere parameterization
\(v:\mathbb T^D\to S^{d-1}\):

\[
v(\theta)=\bigl(\cos\theta_1,
\sin\theta_1\cos\theta_2,\ldots,
(\textstyle\prod_{j=1}^{D-1}\sin\theta_j)\cos\theta_D,
(\textstyle\prod_{j=1}^{D-1}\sin\theta_j)\sin\theta_D\bigr).
\tag{8}
\]

For \(D=1\), this means \((\cos\theta_1,\sin\theta_1)\). Every pure
derivative with respect to one angle has Euclidean norm at most \(\sqrt d\),
uniformly in the other angles and in derivative order.

We prove, for each layer and each angular coordinate \(s\),

\[
\sup_\theta\|\partial_{\theta_s}^k\Phi_\ell(v(\theta))\|_{H_\ell}
\le A B_\ell^k(k!)^{3/2},\qquad k\ge0,
\tag{9}
\]

where one may choose

\[
A=\max\{M,\sqrt d,1\},\qquad
B_\ell=(1+aA\sqrt{2e})^\ell.
\tag{10}
\]

Thus all constants are independent of the sample count, inputs, labels,
gap and width. Mixed derivative estimates are not needed for the Fourier
argument below.

First we justify all differentiations. Suppose \(u(t)\) is a smooth curve
in a Hilbert space. The curve \(G(u(t))\) is smooth in every finite \(L^r\),
because \(G:H\to L^r\) is bounded and linear. Composition with a smooth
function whose derivatives are all bounded is smooth into every finite
\(L^r\), with the ordinary chain rule. This can be checked directly using
Taylor remainders and Hölder's inequality: for instance

\[
\|\phi(X+h)-\phi(X)-\phi'(X)h\|_{L^r}
\le\tfrac12\|\phi''\|_\infty\|h\|_{L^{2r}}^2.
\]

Higher derivatives follow by differentiating finite products; all required
moments exist, and each product is continuous by Hölder with sufficiently
large finite exponents. The same argument applies to difference quotients
of \(\phi^{(p)}\), since the next two derivatives are bounded. Starting
from (8), induction therefore establishes the smooth Hilbert curves needed
in every layer, before any quantitative estimate is used.

Now fix one angular coordinate and suppress it in the notation. Put
\(u=\Phi_{\ell-1}\) and \(g=G_\ell(u)\). The ordered-composition form of
Faà di Bruno's formula is

\[
\frac{d^k}{dt^k}\phi_\ell(g)
=k!\sum_{p=1}^k\frac{\phi_\ell^{(p)}(g)}{p!}
\sum_{\substack{j_1+\cdots+j_p=k\\j_i\ge1}}
\prod_{i=1}^p\frac{G_\ell(u^{(j_i)})}{j_i!}.
\tag{11}
\]

The \(p!\) denominator is essential. It cancels the activation derivative
factor from (3). For a fixed composition, Hölder's inequality and (5) give

\[
\left\|\prod_{i=1}^pG_\ell(u^{(j_i)})\right\|_{L^2}
\le(2p)^{p/2}\prod_{i=1}^p\|u^{(j_i)}\|_{H_{\ell-1}}.
\tag{12}
\]

There is no independence requirement between the Gaussian factors here.
Applying the induction hypothesis to (11)--(12) yields

\[
\|\Phi_\ell^{(k)}\|_{H_\ell}
\le M k! B_{\ell-1}^k
\sum_{p=1}^k(aA)^p(2p)^{p/2}
\sum_{j_1+\cdots+j_p=k}\prod_{i=1}^p\sqrt{j_i!}.
\tag{13}
\]

For every positive composition of \(k\) into \(p\) parts,

\[
\prod_{i=1}^p j_i!\le\frac{k!}{p!}.
\tag{14}
\]

One proof repeatedly transfers a unit from a smaller part greater than one
to a largest part; the product of factorials increases. Its maximum is
\((k-p+1)!\). Also
\(k!/(k-p+1)!=k(k-1)\cdots(k-p+2)\ge p!\), since each factor is at
least its counterpart in \(p(p-1)\cdots2\). This proves (14), including
the endpoint cases \(p=1,k\).

Since \(p!\ge(p/e)^p\), it follows that
\((2p)^{p/2}/\sqrt{p!}\le(2e)^{p/2}\). There are
\(\binom{k-1}{p-1}\) ordered compositions. With \(T=aA\sqrt{2e}\),
(13) becomes

\[
\begin{aligned}
\|\Phi_\ell^{(k)}\|_{H_\ell}
&\le M B_{\ell-1}^k(k!)^{3/2}
\sum_{p=1}^k\binom{k-1}{p-1}T^p\\
&=M B_{\ell-1}^k(k!)^{3/2}T(1+T)^{k-1}\\
&\le A[B_{\ell-1}(1+T)]^k(k!)^{3/2}.
\end{aligned}
\]

The case \(k=0\) follows from boundedness of the activation. This proves
(9)--(10). In particular the derivative order \(3/2\) is preserved across
depth; it is not multiplied by the number of layers.

## 4. Uniform approximation by a small Hilbert subspace

Complexify \(H_L\) for Fourier coefficients and write
\(F(\theta)=\Phi_L(v(\theta))\). Define its Bochner Fourier coefficients

\[
\widehat F(k)=\frac1{(2\pi)^D}
\int_{\mathbb T^D}F(\theta)e^{-ik\cdot\theta}\,d\theta,
\qquad k\in\mathbb Z^D.
\]

Let \(r=|k|_\infty\), choose a coordinate attaining that maximum, and
integrate by parts \(q\) times in that coordinate. Periodicity removes all
boundary terms, and (9), with \(B=B_L\), gives

\[
\|\widehat F(k)\|\le A\frac{B^q(q!)^{3/2}}{r^q}.
\tag{15}
\]

For \(r\ge1\), take \(q=\lfloor(r/(2B))^{2/3}\rfloor\). Using
\(q!\le q^q\), whenever \((r/(2B))^{2/3}\ge2\), the ratio in (15) is at
most \(2^{-q}\), and \(q\ge\tfrac12(r/(2B))^{2/3}\). Enlarging the
prefactor covers the remaining frequencies, including zero. Thus

\[
\|\widehat F(k)\|\le2A e^{-c|k|_\infty^{2/3}},\qquad
c=\frac{\log2}{2(2B)^{2/3}}.
\tag{16}
\]

The coefficients are absolutely summable. Their Fourier series equals
\(F\) uniformly: its Fejér sums converge uniformly to the continuous
Hilbert-valued function \(F\), while absolute summability identifies that
limit with the series. Equivalently this follows by applying every continuous
linear functional and scalar Fourier uniqueness.

Truncate to \(|k|_\infty\le J\). The shell at radius \(r\ge1\) contains
at most \(2D(2r+1)^{D-1}\) frequencies. Splitting the exponential in (16)
into two equal factors proves

\[
\sup_\theta\left\|F(\theta)-
\sum_{|k|_\infty\le J}\widehat F(k)e^{ik\cdot\theta}\right\|
\le E e^{-\tau J^{2/3}},\qquad \tau=c/2,
\tag{17}
\]

where, for example, one may choose

\[
E=\max\left\{1,
4AD\sum_{r=1}^\infty(2r+1)^{D-1}e^{-(c/2)r^{2/3}}\right\}<\infty.
\]

Because \(F\) is real, conjugate frequencies combine into real sine and
cosine terms. The truncated series takes its values in a real Hilbert
subspace \(E_J\subset H_L\) of dimension at most

\[
R_J=(2J+1)^D.
\tag{18}
\]

For each nonzero frequency pair its real and imaginary coefficient vectors
use at most two real dimensions, so (18) incurs no extra factor two.
Let \(P_J\) be the orthogonal projection onto \(E_J\). Surjectivity of (8)
and (17) imply

\[
\sup_{v\in S^{d-1}}\|(I-P_J)\Phi_L(v)\|_{H_L}
\le\epsilon_J:=E e^{-\tau J^{2/3}}.
\tag{19}
\]

Only existence of this approximation subspace is needed for the count
bound. The corollary introduces no stored feature representation and makes
no new computation claim about the compression algorithm.

## 5. From approximation rank to the Gram-gap/count relation

Define the projected Gram matrix
\((K_J)_{ab}=\langle P_J\Phi_L(v_a),P_J\Phi_L(v_b)\rangle\). It has rank
at most \(R_J\), and \(Q^{(L)}-K_J\) is the Gram matrix of the projection
errors. It is positive semidefinite and, by (19), has trace at most
\(m\epsilon_J^2\).

Let \(P\) be the orthogonal projection in sample space \(\mathbb R^m\)
onto the nullspace of \(K_J\). If \(m\ge2R_J\), then
\(\operatorname{tr}P\ge m/2\). The gap assumption gives

\[
\begin{aligned}
\gamma(m-R_J)
&\le\gamma\operatorname{tr}P
\le\operatorname{tr}(PQ^{(L)})\\
&=\operatorname{tr}\bigl(P(Q^{(L)}-K_J)\bigr)
\le m\epsilon_J^2.
\end{aligned}
\]

Consequently

\[
\gamma\le2E^2e^{-2\tau J^{2/3}}.
\tag{20}
\]

This trace argument improves the single-null-vector estimate
\(\gamma\le m\epsilon_J^2\), and avoids an unnecessary factor \(m\).

For \(m\ge2\cdot6^D\), put

\[
J=\left\lfloor\frac{(m/2)^{1/D}-1}{2}\right\rfloor.
\]

Then \(R_J\le m/2\) and \(J\ge\tfrac14(m/2)^{1/D}\). Therefore (20)
gives structural constants \(C_0\ge e\), \(b_0>0\) such that

\[
\gamma\le C_0\exp\{-b_0m^{2/(3D)}\}.
\tag{21}
\]

For example, take
\(b_0=2\tau4^{-2/3}2^{-2/(3D)}\), and enlarge \(C_0\) to cover
\(m<2\cdot6^D\), using \(\gamma\le1\). Taking logarithms in (21) yields

\[
m\le b_0^{-3D/2}[\log(C_0/\gamma)]^{3D/2}
\le C[\log(e+1/\gamma)]^{3D/2},
\]

which proves (1). The dimension exponent and all structural dependencies
are explicit. When \(d=1\), a positive definite Gram on the two-point
sphere forces \(m\le2\), so angular approximation is unnecessary.

## 6. Substitution into the existing small-label theorem

The complete input `DATASET_MAXIMUM_REFINEMENT.md` establishes that the
full source and compression construction applies if

\[
0<Y\le c\lambda e^{-C\sqrt{\log(em)}},\qquad
\lambda=\min\{1,\lambda_{\min}(Q^{(L)})/m\},
\tag{22}
\]

with structural constants. In particular, under the present gap assumption,
\(\lambda\ge\gamma/m\). Set

\[
s=\log(e+1/\gamma),\qquad \beta=3(d-1)/2.
\]

By (1), \(m\le C_1s^\beta\), with \(C_1\ge1\). Since
\(m^{-1}e^{-C\sqrt{\log(em)}}\) decreases with \(m\), the right side of
(22) is at least

\[
\frac{c\gamma}{C_1s^\beta}
e^{-C\sqrt{\log(eC_1s^\beta)}}
\ge c_2\gamma s^{-\beta}e^{-C_2\sqrt{\log(es)}}.
\tag{23}
\]

This already gives a slightly sharper gap-only sufficient condition than
(2). To obtain its simple power form, for every \(\varepsilon>0\) use

\[
C_2\sqrt{1+\log s}
\le C_2+C_2\sqrt{\log s}
\le C_2+\varepsilon\log s+\frac{C_2^2}{4\varepsilon}.
\]

Thus the final exponential in (23) is at least
\(e^{-C_2-C_2^2/(4\varepsilon)}s^{-\varepsilon}\). Taking
\(c_\varepsilon=c_2e^{-C_2-C_2^2/(4\varepsilon)}\) proves that (2)
implies (22).

All already proved conclusions of that theorem follow by this implication:
the same autonomous compression construction, fitting and convergence of
both flows, the stated retained-coordinate bound, and the uniform-in-time
comparison including endpoints. Their original constants and width
thresholds retain their original dependence. This argument does not add
a uniform growing-dataset theorem or a practical formula for the full
width threshold.

## 7. Scope and audit

The strip bound, not merely real analyticity or three bounded derivatives,
supplies the derivative estimate (3). Both counterexamples in the earlier
alternative route lie outside this strip-bounded class. Conversely, nothing
here assumes that the covariance kernel itself is holomorphic across unit
correlation. The needed approximation follows from the explicitly proved
Hilbert derivative estimate.

The rank/count bound uses the deterministic limiting initialization Gram
that is already an explicit hypothesis of the actual theorem. It adds no
new dataset geometry condition and no concentration statement along
training. Gaussian correlation among angular derivatives is allowed
throughout (12).

The statement is a parameterization improvement: for every dataset obeying
the existing population gap assumption, its sample count is bounded by
that gap. It does not improve the allowed label size obtained by inserting
that same dataset's actual \(m\) into (22), does not prove that labels
outside (2) fail, and does not identify an optimal dependence on label
direction or on the gap.

## 8. Final label refinement after the separate-budget checks

2026-10-04. This addendum uses the complete author derivation
`LABEL_SEPARATE_BUDGETS.md` and the independently frozen reconstruction
`LABEL_SEPARATE_BUDGETS_CHECK.md` (SHA256
`96f9766dc398b08b229581e64eb6590298b4ff95aaa4a7a7fac492cf29c2e059`).
The coordinator subsequently read both complete derivations, reconstructed
the changed interfaces, and agreed with the check. This is an internally
checked research refinement, not a promotion review or established book
result. It changes no part of Sections 1--7's coordinate or sample-count
proof.

The checked budget change establishes the full real-carrier and
complex-source theorem under

\[
0<Y\le c_0\lambda,\qquad
\lambda=\min\{1,\lambda_{\min}(Q^{(L)})/m\},
\tag{24}
\]

with structural \(c_0>0\). The improvement comes from separate empirical
carrier budgets for the training samples, followed by a sample union only
after the fixed-degree moment estimate. It removes the additional
\(\exp\{-C\sqrt{\log(em)}\}\) factor in the former source threshold;
it is not a consequence of the geometry lemma alone.

To make the gap convention exact, define in this addendum

\[
\gamma:=\lambda_{\min}(Q^{(L)})>0,\qquad
\bar\gamma:=\min\{1,\gamma\},\qquad
s:=\log(e+1/\bar\gamma),\qquad
\beta:=3(d-1)/2.
\tag{25}
\]

The covariance \(Q^{(L)}\) is precisely the recursively defined
initialization covariance in (4). Applying the unchanged geometry proof
with its lower bound \(\bar\gamma\) gives

\[
m\le C_1s^\beta,\qquad
\lambda=\min\{1,\gamma/m\}\ge\frac{\bar\gamma}{m}
\ge\frac{\bar\gamma}{C_1s^\beta}.
\tag{26}
\]

Therefore the gap-only condition

\[
0<Y\le\frac{c_0\bar\gamma}{C_1s^\beta}
\tag{27}
\]

implies (24) directly. No remaining logarithmic maximum penalty needs
to be absorbed, so the exponent is exactly \(\beta\), without
\(\varepsilon\). If \(0<\gamma\le1\), this is simply

\[
0<Y\le
\frac{c\gamma}{[\log(e+1/\gamma)]^{3(d-1)/2}}.
\tag{28}
\]

The case \(Y=0\) is stationary. A verified lower bound in place of the
exact smallest eigenvalue also gives a valid sufficient condition after
the same cap; the exact definition (25) identifies the strongest version
of this particular corollary for a known covariance.

For a fixed dataset, the best currently checked sample-aware sufficient
condition is (24), namely \(Y\le c_0\min\{1,\gamma/m\}\). Equation
(27) replaces the actual sample count by its largest value permitted by
the geometry bound at fixed \(d,L\) and activation strip bounds. It does
not assert a larger numerical admissible-label range for that dataset.
Neither (24) nor (27) is claimed necessary or optimal.

All existing compression conclusions and their original width-threshold
qualifications continue through the checked source theorem. In particular,
the dataset and its positive label magnitude remain fixed before width
tends to infinity; the final width threshold can depend on sample count,
confidence and a fixed moment degree. No trained-population assumption,
new dataset geometry hypothesis, or growing-dataset theorem is introduced.
