# Independent check of the weak-factor second-layer calculation

Date: 2026-09-30. Checker: `weak_factor_second_check`.

**Verdict:** the exact startup identity, Walsh factors, full-transpose
contribution, leading coefficients, moment polynomials, and stated remainder
orders pass this independent mathematical check under the assigned regular
population-flow assumptions. The separately supplied directed interval
certificate also passes its mathematical audit and exact reproduction. It
rigorously establishes positive primitive-bit and negative context
coefficients. No material algebraic correction is required.

The initial scientific input was the supervisor's explicit population model
and the frozen `WEAK_FACTOR_SECOND_LAYER.md`, SHA256
`8f1a558285028573ffb101eadb61603f94cbe666a6bee6236cd7b1d193ee7fd7`.
The hash was verified before reading. No study history, README, other route,
prior check, book, external source, or trajectory was read. Subsequently the
supervisor explicitly supplied the two certificate scripts and their frozen
outputs identified in Section 6; those are the only additional scientific
inputs. The
`solve-math-rigorously` skill was applied. This is an internal scoped check,
not a promotion review. The certificate was re-executed as recorded below;
the candidate's ordinary quadrature was not used as a sign proof.

## 1. Reconstructing the acceleration from the assigned dynamics

Let sample averaging mean one quarter of the sum over the four samples.
At initialization, (W=V=0), (K=H), and consequently (D=L=0).
The assigned feature-clock equations therefore imply

\[
W'=G_y,\qquad A'=V'=K'=0,\qquad H'=Z'=G'=0.
\]

Differentiating (D_a=W\phi'(Z_a)) once gives

\[
D_a'=G_y\phi'(Z_a),\qquad
V_a''=y_aG_y\phi'(Z_a)=U_a.
\]

Since (D=0), differentiating (L_a=\phi'(A\cdot u_a)B^*D_a)
only retains its (D_a') term. Hence

\[
A''=\frac14\sum_a\nabla H_a\,T^*U_a=A_U.
\]

Here \(\nabla H_a=\phi'(A\cdot u_a)u_a\). The second derivative of
the memory operator only retains (V_a''\otimes H_a): every term involving
a derivative of a key or first-layer feature is multiplied by (V_a) or
(V_a'), both zero. It follows that

\[
Z_a''=T[\nabla H_a\cdot A_U]
       +\frac14\sum_bU_b\,\mathbb E_1H_bH_a.
\]

For the measured character (k), (G_k'=0), so

\[
\mathcal E_k''=2\mathbb E_2G_kG_k''
=\frac24\sum_a\mathbb E_2Y_a^kZ_a'',
\qquad Y_a^k=k_aG_k\phi'(Z_a).
\]

Applying the actual transpose to the first summand yields

\[
\mathcal E_k''
=2\mathbb E_1 A_U\cdot A_{Y^k}
 +\frac2{16}\sum_{a,b}C_{ab}\mathbb E_2U_bY_a^k.
\]

This verifies (1.1), including its factor (2/16). In particular, no
additional key-motion term is missing. The formula uses the population
transpose stipulated in the assignment and is not a calculation for a
separately trained dense matrix.

## 2. Fourier normalization and the true transpose

Write \(H_a=\sum_\chi\chi_aH_\chi\), and likewise for other sample
arrays. Flipping the Gaussian coordinate (Y) or (Z) multiplies each
(H_\chi) by its corresponding Walsh sign. Thus distinct first-layer
characters are orthogonal in expectation. The four initial forward calls
(Z_\chi=TH_\chi) are independent centered Gaussians with variances
(v_\chi=\mathbb E_1H_\chi^2).

The exact transformed sources are

\[
U_\chi=G_yQ_{y\chi},\qquad
Y_\chi^k=G_kQ_{k\chi}.
\]

Each of these has parity \(\chi\) under the two bit flips. Therefore
different source characters have zero cross expectation, and
\(\mathbb E_2\partial_{Z_\psi}U_\chi\) vanishes for
\(\psi\ne\chi\). There is no extra factor in the transpose drift:

\[
\partial_{Z_b}U_\chi
=\frac14\sum_\psi\psi_b\partial_{Z_\psi}U_\chi,
\qquad
\sum_b\mathbb E_2\partial_{Z_b}U_\chi H_b
=\sum_\psi\mathbb E_2\partial_{Z_\psi}U_\chi H_\psi.
\]

Differentiating the exact sources, before any small-factor truncation,
gives

\[
\beta_\chi=\mathbb E_2[Q_{y\chi}^2+G_yR_y],\qquad
\gamma_\chi^k=\mathbb E_2[Q_{k\chi}^2+G_kR_k].
\]

The assigned source law consequently implies

\[
T^*U_\chi=\beta_\chi H_\chi+\xi_\chi,
\quad
T^*Y_\chi^k=\gamma_\chi^kH_\chi+\eta_\chi^k,
\quad
\mathbb E_1\xi_\chi\eta_\psi^k
=\mathbf1_{\chi=\psi}\mathbb E_2U_\chi Y_\chi^k.
\]

The covariance is the full source Gram. Subtracting the drift projection
would change the assigned model and the checked answer. Because these
centered Gaussian reverse variables are independent of the initial readin,
their cross terms with the drift vanish. Also,

\[
A_U=\sum_\chi\nabla H_\chi T^*U_\chi.
\]

This proves the decomposition (2.4). Independently, inserting
\(C_{ab}=\sum_\chi v_\chi\chi_a\chi_b\) into the memory sum makes
each sample sum equal to four times its normalized Walsh coefficient.
The factor (16) cancels, giving (2.5), namely
\(2\sum_\chi v_\chi\mathbb E_2U_\chi Y_\chi^k\).

## 3. Leading terms and controlled remainders

For \(h=\tanh X\), let \(p=\phi'(X)\), \(k=\phi''(X)\), and
\(\ell=\phi'''(X)\). Expanding the actual input
\(\sqrt{1-2\varepsilon^2}X+\varepsilon\sigma Y+
\varepsilon\tau Z\) and taking normalized Walsh coefficients gives

\[
H_0=h+O(\varepsilon^2),\quad
H_1=\varepsilon Yp+O(\varepsilon^3),\quad
H_2=\varepsilon Zp+O(\varepsilon^3),\quad
H_y=\varepsilon^2YZk+O(\varepsilon^4).
\]

Differentiating these expansions with respect to the initial readin
coordinates gives precisely (3.1). In particular,

\[
\mathbb E_1|\nabla H_0|^2=a+O(\varepsilon^2),\qquad
\mathbb E_1|\nabla H_1|^2
=\varepsilon^2(a+b)+O(\varepsilon^4).
\]

There is no missing contribution from differentiating the context input
coefficient: its difference from one is order \(\varepsilon^2\), and it
only affects the displayed remainders.

Here is a direct justification for the remainder strengths. On a compact
interval around zero with \(|\varepsilon|<1/\sqrt2\), all required
parameter derivatives of the first-layer expressions are bounded by
polynomials in \(|X|+|Y|+|Z|\). All fixed-order tanh derivatives are bounded,
and every Gaussian polynomial has every finite moment. Consequently Taylor
expansion, readin differentiation, and expectations are valid to the finite
orders used here in every finite Gaussian (L^r).

The quantities (H_1/\varepsilon) and (H_y/\varepsilon^2) have smooth
(L^r) extensions, so the normalized variances
(v_1/\varepsilon^2) and (v_y/\varepsilon^4) are smooth and positive
near zero; their limits are (a>0) and (b>0). Also (v_0\to\kappa>0).
With four fixed independent standard normals (N_\chi), couple the calls as

\[
Z_0=\sqrt{v_0}\,N_0,\quad
Z_1=\varepsilon\sqrt{v_1/\varepsilon^2}\,N_1,\quad
Z_2=\varepsilon\sqrt{v_2/\varepsilon^2}\,N_2,\quad
Z_y=\varepsilon^2\sqrt{v_y/\varepsilon^4}\,N_y.
\]

This has exactly the required Gaussian law for every small nonzero
\(\varepsilon\), including either sign. It proves (3.2) with controlled
(L^r) remainders. Expectations and products preserve their orders by
Hölder's inequality. The exact source derivative identities above then give
(3.4) and (3.5). For example,

\[
\beta_0=\varepsilon^4
\{b\mathbb E(K^2+JL)+a^2\mathbb E(L^2+KM)\}
+O(\varepsilon^6),
\]

and \(\gamma_y^1=\varepsilon^2a\mathbb E(K^2+JL)+O(\varepsilon^4)\).
The latter term would indeed be lost by differentiating just the leading
truncation of (Y_y^1). Relabeling both sample bits identifies
\(\varepsilon\) and \(-\varepsilon\) for each scalar energy. The
smoothness just established, together with these parities and the displayed
source orders, justifies the even remainder increments in (4.7) and (5.4).
No convergence of an infinite time or parameter series is used.

## 4. Independent coefficient calculation

Using the candidate's definitions of (B_0,B_1,C_0,T), the leading readin
drifts are

\[
\begin{split}
(d_U)_x&=B_0hp+B_1(Y^2+Z^2)pk+TY^2Z^2k\ell,\\
(d_U)_y&=B_1Yp^2+TYZ^2k^2,\\
(d_U)_z&=B_1Zp^2+TY^2Zk^2,
\end{split}
\qquad
d_1=(C_0hp+TY^2pk,TYp^2,0).
\]

Thus (D_U=\varepsilon^4d_U+O_{L^r}(\varepsilon^6)) and
(D_{Y^1}=\varepsilon^2d_1+O_{L^r}(\varepsilon^4)). Averaging their
dot product uses \(\mathbb EY^2=1\), \(\mathbb EY^4=3\), and
\(\mathbb E(Y^2+Z^2)Y^2=4\). In the notation of the candidate this gives

\[
\mathfrak D_1=B_0C_0A_0+(B_0T+2B_1C_0)A_1
+(4B_1T+T^2)A_2+TC_0A_3+3T^2A_4+B_1TA_5.
\]

The isolated (T^2A_2) comes from the (y)-coordinate product;
(3T^2A_4) comes from the (x)-coordinate product. Both are needed.

For the covariance and memory terms, direct multiplication of the leading
sources yields

\[
\begin{split}
\mathbb E_2U_0Y_0^1
&=\varepsilon^6(abP+3a^3Q)+O(\varepsilon^8),\\
\mathbb E_2U_1Y_1^1
&=\varepsilon^4a^2P+O(\varepsilon^6).
\end{split}
\]

For example the first integrand is
\((JD+KBC)(KD+LBC)JKB^2\). Its surviving Gaussian terms are
(D^2B^2J^2K^2) and (B^4C^2JK^2L); the remaining terms contain an odd
independent Gaussian. Channels (2) and (y) enter the complete
acceleration only at order eight or higher. Multiplying by the exact leading
gradient norms gives

\[
\mathfrak N_1
=a(abP+3a^3Q)+(a+b)a^2P
=a^2(a+2b)P+3a^4Q.
\]

Multiplying by the leading first-layer variances instead gives

\[
\mathfrak M_1
=\kappa(abP+3a^3Q)+a^3P.
\]

For context, (D_{Y^0}=J_0(hp,0,0)+O_{L^r}(\varepsilon^2)), hence

\[
\mathfrak D_0=J_0(B_0A_0+2B_1A_1+TA_3).
\]

The order-four source product is
\(\mathbb E_2\Lambda\mathcal M gJ=bP_0+a^2Q_0\).
All other context channels are suppressed by at least two further powers
after multiplying their gradient norms or variances. This gives

\[
\mathfrak N_0=a(bP_0+a^2Q_0),\qquad
\mathfrak M_0=\kappa(bP_0+a^2Q_0).
\]

These independently reproduce all three contributions in (4.7) and (5.4),
including the overall factor two.

## 5. Scalar polynomial audit and claim boundary

Set (p=\operatorname{sech}^2X). Direct differentiation gives

\[
\phi''=-2hp,\quad \phi'''=4p-6p^2,\quad
\phi''''=(-8+24p)hp,\quad h^2=1-p.
\]

Substituting these into every inner and outer expectation verifies all of
(6.1). In particular the less immediate identities are

\[
\begin{split}
(\phi''')^2+\phi''\phi''''&=32p^2-112p^3+84p^4,\\
h p\phi''\phi'''&=-8p^3+20p^4-12p^5,\\
p(\phi'')^2\phi'''&=16p^4-40p^5+24p^6,\\
p^2+h\phi''&=3p^2-2p.
\end{split}
\]

The same identities at the outer Gaussian verify (V,Q,Q_0,J_0), while
the remaining entries follow from \((\phi'')^2=4(p^2-p^3)\) and direct
multiplication. The outer variance is exactly \(\kappa=1-I_1\);
certification must propagate its uncertainty into the outer moments.

Therefore the scalar obligations are exactly

\[
\mathfrak D_1+\mathfrak N_1+\mathfrak M_1>0,
\qquad
\mathfrak D_0+\mathfrak N_0+\mathfrak M_0<0.
\]

The printed ordinary quadrature values were not used to establish these
signs. Section 6 supplies rigorous strict enclosures. Together with the
controlled remainders, they prove the corresponding signs for all
sufficiently small positive fixed \(\varepsilon\). They do not provide a
numerical range of admissible \(\varepsilon\).

For an actual twice continuously differentiable equivariant population
flow, (\mathcal E_k'(0)=0) and a strict signed second derivative imply
the stated strict increase or decrease on a nonempty initial feature-clock
interval. Since (ds/dt=2) at initialization and is positive nearby, the
physical-time second derivative has the same sign; explicitly it is four
times the feature-clock second derivative at zero. Flow existence,
uniqueness, regularity, interchange with population expectations, and the
canonical transpose construction remain assumptions, not results of this
audit. The exact zero bit-label correlations and the absence of any global
fitting or generalization conclusion are correctly stated in the candidate.

## 6. Directed interval certificate: source audit and reproduction

The supervisor explicitly added the following frozen inputs. All paths are
relative to this repository.

- `studies/q1_population_mechanism_20260930/weak_factor_interval_certificate.py`,
  SHA256 `51c7570b1f34a066287f286295868c87283ac45f16d0895d4b4d716c7010be54`.
- `data/generated/q1_population_mechanism_20260930/weak_factor_interval_certificate_20260930_01/results.json`,
  SHA256 `316a83c28ccba4415d47d54f6bdb7ad2cd1a307150e86e0b9694ce4feded62cf`.
- `studies/q1_population_mechanism_20260930/weak_factor_coefficient_certificate.py`,
  SHA256 `9d0b0322bcc59a88c6ca5bef1b6ac69911bd035c2cd92006b08e4e511605bba5`.
- `data/generated/q1_population_mechanism_20260930/weak_factor_coefficient_certificate_20260930_01/results.json`,
  SHA256 `586699805890bb62ee02dee03a2a091fafcfe63f4fb07f68e8cc3dae92349f1a`.

The first three hashes were checked against the assignment; the fourth was
recorded on reading. The unrelated first-layer postprocessor and ratios are
outside this audit.

For variance (v\in(0,1]), the implemented integral is exactly

\[
\mathbb E\operatorname{sech}^{2n}(\sqrt v\,N)
=2\int_0^\infty\varphi(x)
  \operatorname{sech}^{2n}(\sqrt v\,x)\,dx,
\qquad
\varphi(x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}}.
\]

The substitution to a standard Gaussian is useful: the same tail bound and
derivative bound work for both the inner and outer integrals. I checked the
following components directly.

**Outward arithmetic.** Integer, string, and Decimal constructors in the
executed paths are exact. Additions, subtractions, products, and reciprocals
use directed lower and upper contexts. Products take all endpoint pairs;
reciprocals require an interval excluding zero. The implementation widens
the correctly rounded nearest Decimal exponential and square root by one
adjacent representable number in each outward direction. Monotonicity then
encloses the corresponding operation on the entire argument interval. All
executed square-root arguments and divisors are strictly positive, and no
overflow or underflow occurs in the certificate's ranges. Repeated interval
products preserve containment even when dependencies make them wider.

**The constant \(\pi\).** Each arctangent series uses exact rational
arithmetic and is bounded by its alternating partial sum and the next
partial sum. The Machin identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) gives the stated combination of
endpoints. For completeness, if (a=\arctan(1/5)), then
\(\tan(2a)=5/12\) and \(\tan(4a)=120/119\). Subtracting
\(b=\arctan(1/239)\) gives \(\tan(4a-b)=1\), and
\(0<4a-b<\pi/2\); this verifies the identity and its branch. The final
rational-to-Decimal conversion is outward.

**The uniform fourth-derivative bound.** Define
\(P_{n,0}(t)=(1-t^2)^n\) and recursively
\(P_{n,j+1}(t)=(1-t^2)P_{n,j}'(t)\). The integer coefficient recursion
in `derivative_bound` implements exactly this identity. If (c_{n,j})
is the sum of the absolute coefficients of (P_{n,j}), then

\[
\left|\frac{d^j}{dx^j}
 \operatorname{sech}^{2n}(\sigma x)\right|
\le\sigma^j c_{n,j}\le c_{n,j},\qquad 0<\sigma\le1.
\]

The first five Gaussian-density derivatives are the density times
\(1,-x,x^2-1,3x-x^3,x^4-6x^2+3\). They are all bounded in absolute
value by (10). One elementary verification uses
\(\sup_{x\ge0}x^m e^{-x^2/2}=(m/e)^{m/2}\) for (m>0), and
\((2\pi)^{-1/2}<1/2\). With (e>2), this bounds
\(x^m\varphi(x)\) for (m=0,1,2,3,4\) by
\(1/2,1/2,1/2,1,2\), respectively. The fourth-derivative polynomial
is therefore bounded by (2+6/2+3/2=6.5<10), and the lower orders are
smaller. The product rule consequently gives

\[
\sup_x\left|\frac{d^4}{dx^4}
 \{\varphi(x)\operatorname{sech}^{2n}(\sigma x)\}\right|
\le10\sum_{j=0}^4\binom4j c_{n,j}.
\]

This is precisely the bound used in the script, uniformly over the entire
certified outer-variance interval.

**Quadrature and tail.** Composite Simpson integration on ([0,R]), for
a (C^4) integrand, an even number (N) of equal subintervals, and
step (h=R/N), has absolute error at most
\(Rh^4\sup|f^{(4)}|/180\). Here (R=10), (h=1/2000), and
(N=20000) is even. Multiplying by two for the half-line symmetry gives
the exact rational error factor in the implementation. The smooth
integrands satisfy the theorem's hypotheses by the derivative argument
above. At each node, interval evaluation includes every variance in the
input interval; the uniform Simpson error therefore applies simultaneously
to every such exact variance.

Since \(0<\operatorname{sech}^{2n}\le1\), the missing tail is nonnegative
and at most

\[
2\int_R^\infty\varphi(x)\,dx
\le\frac2R\int_R^\infty x\varphi(x)\,dx
=\frac{2\varphi(R)}R.
\]

This is the script's outward `tail` expression. It is added only to the
upper integral bound, while the Simpson error widens both endpoints.

**Variance and coefficient propagation.** The inner moment enclosure is
first used to form (1-I_1) by outward subtraction. Its interval is strictly
inside ((0,1)), as required by the uniform derivative estimate. The outer
integration uses the entire resulting variance interval, including its
uncertainty. I matched every second-layer formula in the postprocessor to
the independently derived formulas in Sections 4–5; its `second_latent`
and `second_context` include the overall factor two in the accelerations.
It uses only interval arithmetic for the polynomial evaluation.

The following commands were executed from `/home/amir/Codes/PDE`, both
with exit status zero:

```sh
python studies/q1_population_mechanism_20260930/weak_factor_interval_certificate.py --output data/generated/q1_population_mechanism_20260930/weak_factor_second_check_20260930_01/moments.json
python studies/q1_population_mechanism_20260930/weak_factor_coefficient_certificate.py --moments data/generated/q1_population_mechanism_20260930/weak_factor_second_check_20260930_01/moments.json --output data/generated/q1_population_mechanism_20260930/weak_factor_second_check_20260930_01/coefficients.json
```

Every endpoint of the moment, variance, tail, and error bounds and every
second-layer coefficient bound reproduced exactly. Runtime metadata and
output paths account for differences in complete output-file hashes. The
new files have SHA256
`b5b395ba3327c42718ba7c38f679535354950e54f1162b1a7cc2e936c099b9b7`
for `moments.json` and
`c290711e5fe8784c5b2d1caa35fe47329cedb440c8c0880254d8918edc3e8fb3`
for `coefficients.json` in the checker-owned generated directory above.

Rounded outward for readability, the certified full coefficients satisfy

\[
2(\mathfrak D_1+\mathfrak N_1+\mathfrak M_1)
\in[0.2017517989,\ 0.2018090698],
\]

\[
2(\mathfrak D_0+\mathfrak N_0+\mathfrak M_0)
\in[-0.0559419042,\ -0.0559396146].
\]

Both strict scalar sign obligations are therefore closed by the directed
certificate. Under the assigned canonical population construction and local
regularity assumptions, there exists \(\varepsilon_0>0\) such that every
fixed \(0<\varepsilon<\varepsilon_0\) has strictly positive startup
acceleration for each primitive-bit second-layer energy and strictly
negative startup acceleration for context. For each such fixed parameter,
the claimed nonempty initial intervals follow from the actual flow's
assumed (C^2) energy regularity.
