# Depth-four affine certificate and its fixed-depth extension

This is a new calculation for the original raw metric. The rigorous-math
skill, the audited power-ten `PROOF.md` and `AFFINE_SOURCE_CERTIFICATE.md`,
the quantitative `AFFINE_POLYNOMIAL_BOUNDS.md`, and the original
`AFFINE_CORE.md` and theorem were read. No earlier file is changed. This
note certifies the affine/primal/probe inputs, not cap removal or the full
nonlinear source theorem.

Write
\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad
\lambda=a^4r,\quad t=\lambda s,\quad
M=\left(\frac{3\sqrt5}{2\lambda}\right)^{1/5}.
\tag{1}
\]
Here s is the original feature time; the optimizer and raw metric are
unchanged. Let H be precisely the old numerical C_B. The bounds below
can use H as a common numerical prefactor. In particular they are
consistent with the *same* candidate amplitude
\(10^{-70}H^{-400}\delta^{10}\), independently of whether the remaining
source comparison can be closed at that amplitude.

## 1. A useful improvement of the initialized operator constant

The original upper bound ten can be replaced by four without changing
the canonical initialization. For an n by n matrix W with iid N(0,1/n)
entries, take a 1/4-net of the unit sphere of cardinality at most 9^n.
The net inequality is
\(\|W\|\le(4/3)\max_{u\in\mathcal N}\|Wu\|\).
For each fixed unit u, n\|Wu\|^2 is chi-square with n degrees of
freedom. Its exponential moment, optimized at 4/9, gives
\[
\Pr(\|Wu\|\ge3)
\le\exp[-(8-\log9)n/2].
\]
The union bound consequently gives
\[
\Pr(\|W\|>4)
\le\exp[-(4-\tfrac32\log9)n].
\tag{2}
\]
The exponent is positive. Applying this to the three initialized hidden
matrices and passing to the fixed-program generated action limits proves
norm at most four on every generated vector. The extension by continuity
has the same norm. This establishes the stronger constant on the same
canonical action spaces; it is not an additional initial-state assumption.
The initial forward propagation identities still give
\[
\|p_0\|=1,\quad \|A_{j,0}\|\le4\ (j=2,3,4),\quad
D_0=0,\quad \|A_{4,0}A_{3,0}A_{2,0}p_0\|=1.
\tag{3}
\]

## 2. Exact equations and balances

After odd label folding, let p be the active first projection divided by
r, and let D be the signed readout. Put
\[
x_1=p,\quad x_j=A_jx_{j-1}\ (j=2,3,4),\qquad
d_4=D,\quad d_j=A_{j+1}^*d_{j+1}\ (j=1,2,3).
\]
The normalized affine objective is \(F=\langle D,x_4\rangle\), and
the original prediction is g=\lambda F. Its raw gradient equations are
exactly
\[
p'=d_1,\qquad A_j'=d_j\otimes x_{j-1}\ (j=2,3,4),
\qquad D'=x_4.
\tag{4}
\]
All primes in this note denote t derivatives. The five component metrics
are L2, HS, HS, HS, L2. In particular normalizing the first projection
gives its exact raw metric, since its squared raw length is
\(\|dP_1\|^2/v=\|dp\|^2\).

Differentiating both sides, with no infinite-dimensional traces, proves
\[
A_4A_4^*-D\otimes D=A_{4,0}A_{4,0}^*,
\]
\[
A_jA_j^*-A_{j+1}^*A_{j+1}
=A_{j,0}A_{j,0}^*-A_{j+1,0}^*A_{j+1,0}
\quad(j=2,3),
\]
\[
A_2^*A_2-p\otimes p=A_{2,0}^*A_{2,0}-p_0\otimes p_0.
\tag{5}
\]
For example the derivative of A_jA_j^* is
\(d_j\otimes x_j+x_j\otimes d_j\). The derivative of
A_{j+1}^*A_{j+1} is the same expression, since
\(A_{j+1}^*d_{j+1}=d_j\). The endpoint computations give the other
two identities. If c=\|D\|, scalar differentiation gives
\[
\|p\|^2=1+c^2,\qquad (c^2)'=2F,
\tag{6}
\]
and successive use of (5) gives
\[
\|A_4\|^2\le16+c^2,\quad \|A_3\|^2\le32+c^2,
\quad \|A_2\|^2\le48+c^2.
\tag{7}
\]
Thus every primary norm is bounded by \(R=\sqrt{48+c^2}\).

There are two coercivity estimates, both needed below. The outer
balances imply
\[
\|d_3\|^2\ge c^4,\qquad
\|x_2\|^2\ge c^2(1+c^2).
\]
The A3 gradient alone therefore gives
\[
F'=\|\nabla F\|^2\ge c^6(1+c^2),\qquad
F^2\ge c^8/4+c^{10}/5,\qquad F\ge c^5/\sqrt5.
\tag{8}
\]
To verify the middle inequality without division at zero, differentiate
\(F^2-c^8/4-c^{10}/5\) and use (6); its derivative is nonnegative
and its initial value is zero.

A sharper large-c estimate uses *all* balances. If
\(q_j=\|x_j\|^2/\|x_{j-1}\|^2\), the first outer balance gives
q2\ge c^2. For j=2,3, (5) and the initial norm bound imply
\[
\|x_{j+1}\|^2
\ge \|A_j^*x_j\|^2-16\|x_j\|^2
\ge \frac{\|x_j\|^4}{\|x_{j-1}\|^2}-16\|x_j\|^2.
\]
Hence q_{j+1}\ge q_j-16. At c^2>32 these ratios are positive,
and
\[
\|x_j\|^2\ge(c^2-32)^j\quad(j=1,2,3,4).
\tag{9}
\]
The backward ratios obey the same calculation in reverse order:
\(\|d_3\|^2/\|d_4\|^2\ge c^2\), and each additional matrix
decreases the ratio by at most sixteen. Thus
\[
\|d_j\|^2\ge(c^2-32)^{5-j}\quad(j=1,2,3,4).
\tag{10}
\]
Each of the five gradient components in (4) has squared norm at least
\((c^2-32)^4\). Consequently
\[
F'\ge5(c^2-32)_+^4,\qquad
F^2\ge(c^2-32)_+^5.
\tag{11}
\]
The latter follows by differentiating
\(F^2-(c^2-32)_+^5\), including the region below the threshold.
No balance from depth three was assumed without differentiation.

## 3. Target, duration, and integrated Hessian

Writing the hidden variables collectively as h, the chain rule gives
\(D''=J_hJ_h^*D\), where J_h is the derivative of x4. Thus
\(\|D\|\) is convex: differentiating
\(\sqrt{\|D\|^2+\epsilon^2}\) twice gives a nonnegative result,
and then let epsilon decrease to zero. Its initial right slope is one
by (3). Therefore
\[
c(t)\ge t,\quad c'(t)=F/c\ge1,\quad
c'(t)\ge c^4/\sqrt5\quad(t>0).
\tag{12}
\]
Let T be the first hit F=3/(2\lambda). By (8), c\le M before it.
The level c=1 is reached by time one unless the target was reached
earlier. Integration of (12) afterwards gives
\[
T\le1+\sqrt5/3<2,\quad S=T/\lambda\le2/\lambda<M^5,
\quad c(T)\le M,
\tag{13}
\]
\[
r=\frac{3\sqrt5}{2a^4}M^{-5},\quad
r^2\le2880M^{-10},\quad r^{-1}\le M^5,
\quad M\le76^{1/5}\delta^{-1/10}.
\tag{14}
\]
These estimates also prove existence through the target. Indeed, on a
branch below it the primary operator bounds are finite; the rank-one
HS derivatives and the endpoint derivatives are bounded. Their raw
increments have strong limits at any finite maximal endpoint, and
local existence for the polynomial field continues from that point.
An infinite branch below the target contradicts (12).

Set b=R+1. Every cross block of the Hessian of F has norm at most b^3
on the radius-one raw tube around the affine reference. In the sum norm
the full Hessian norm is at most 4b^3. First,
\[
b^3\le c^3+3c^2+75c+500.
\tag{15}
\]
For this, use
\((48+c^2)^{3/2}\le c^3+72c+48^{3/2}\), obtained from
\(\sqrt{u+v}\le\sqrt u+\sqrt v\) after differentiation in u;
then expand (R+1)^3. The constant term is less than 500.

Before c=1, b^3\le512 and the elapsed time is at most one. Between
one and any terminal c at most sixteen, (12) therefore gives
\[
\int b^3dt\le512+\sqrt5\{3+75/2+500/3+\log16\}<982.
\tag{16}
\]
For c\ge16, (11) gives
\[
\frac{dt}{dc}\le c^{-4}(1-32/c^2)^{-5/2}
\le c^{-4}(1+128/c^2).
\tag{17}
\]
The final inequality follows by the mean value theorem: the derivative
of (1-u)^(-5/2) is at most four for 0\le u\le1/8.
Multiplying (15) by (17), the integrable terms have total integral
from sixteen to infinity at most
\[
\frac3{16}+\frac{75}{2\cdot16^2}+\frac{500}{3\cdot16^3}
+\frac{128}{2\cdot16^2}+\frac{384}{3\cdot16^3}
+\frac{9600}{4\cdot16^4}+\frac{64000}{5\cdot16^5}<1.
\]
Only the term c^{-1} remains. Equations (16)--(17) imply, for the
whole interval and also for any extension with terminal readout c\le N,
\[
\int 4b^3dt\le4000+4\log N\qquad(N\ge1).
\tag{18}
\]
For terminal c\le16 the left side is less than3928, so this statement
also covers that case. In original time the Hessian is multiplied by
\lambda and ds=dt/\lambda. Therefore the same integrated estimate
holds for the original raw affine Hessian. The affine variational
propagator, and the affine part of the radius-one comparison, have bound
\[
G\le e^{4000}M^4.
\tag{19}
\]
The power four, rather than nine, uses the large-c ratio argument.

The learned HS increments are O(M). A convenient explicit verification
is \(\|A_j'\|_{HS}\le R^4\): before c=1 their integrated norm is
at most49^2; after c=1 integrate
\(\sqrt5(48+c^2)^2c^{-4}\). This is bounded by
\(\sqrt5(M+96+768)\), hence by 5000M. The endpoint raw increments
are at most3M and M. These estimates also justify raw strong extension.

## 4. Cap-uniform primal and learned-moment comparison

Let E(s) be the sum of the original raw component distances from the
affine path. Stop at E=1. On this tube, the same bounded arctangent
and capped-gate expansion as in the depth-three proof gives
\[
\|V_{a,e,Rcap}(\Theta)-V_{a,0}(\Theta)\|_{sum}
\le500 e b^4,\qquad 0\le e\le1/2.
\tag{20}
\]
For completeness, write each capped backward step as
\(a q+e\tau_{Rcap}(q)/(1+z^2)\). Its excess over a q has norm
at most e\|q\|. The forward excess at each step has norm at most
e\pi/2. Recursing over at most four gates bounds each backward
product by (3/2)^4 times its affine primary product, and its gate
excess by 4(3/2)^3 e times that product. The three possible earlier
forward insertions in a matrix gradient have total coefficient at
most (\pi/2)(1+3/2+(3/2)^2)(3/2)^4. The sum of these bounds over
the five raw blocks is below 500 e b^4. Projection onto either
RMS-unit input has raw norm at most one. Thus (20) includes the
first block and uses no symmetry of the nearby state.

Subtract the affine fields after this same-state estimate. Equations
(18)--(20) give
\[
E(s)\le500 e e^{4000}M^4\lambda^{-1}\int_0^T b^4dt.
\]
Since b\le c+8, the interval before c=1 contributes at most4096.
Afterwards the expansion of (c+8)^4 and (12) give
\[
\int_0^T b^4dt
\le4096+\sqrt5\{M+32\log M+384+1024+4096/3\}
\le11000M.
\]
Consequently, with the deliberately ample common numerical H,
\[
E\le H eM^{10}.
\tag{21}
\]
The sharper unabsorbed prefactor is at most
\(5.5\cdot10^6e^{4000}\), since \(\lambda^{-1}\le M^5\).
The requirement H eM^10\le1/2 closes the tube and gives existence
through S for every cap.

Forward expansion on this tube yields, for 1\le\ell\le4,
\[
\|z^\ell_e-z^\ell_0\|_2+
\|h^\ell_e-h^\ell_0\|_2
\le H eM^{\ell+9}\le H eM^{13}.
\tag{22}
\]
One may retain the explicit prefactor from (21) while multiplying by
the finitely many powers of b\le8M and the at most four telescoping
terms; the result is still below H. For the prediction, retain the
exact affine coefficient \lambda:
\[
|g_e(S)-3/2|
\le \lambda b^4 E+10 e b^4\le H eM^9.
\tag{23}
\]
Here the first term uses the sum norm; no unnecessary factor five
is required because every partial derivative is at most \lambda b^4.

Every *original*, unnormalized affine forward field is bounded by an
absolute constant independent of M. In fact the active field at layer
\ell is a^{\ell-1}r x_\ell, and
\(\|x_\ell\|\le R^\ell\le7^\ell M^\ell\), whereas
\(r\le24\sqrt5 M^{-5}\). The inactive field is the frozen
initial Gaussian product with variance a^{2(\ell-1)}(1-v).
This freezing extends to A4A3A2 by telescoping the product difference:
at every fixed affine Euler prefix the learned product difference has
bounded ordinary Frobenius norm, and its normalized action on the
independent inactive Gaussian root tends to zero. Conditional second
moments also give orthogonality to the active fields. Thus (22), under
H eM^13\le1, bounds the actual nonlinear forward fields by another
absolute constant independent of M.

The original backward fields obey
\[
\|\delta^\ell_0\|_2\le C M^{5-\ell},\qquad
\|\delta^\ell_e-\delta^\ell_0\|_2
\le H eM^{14-\ell}\quad(1\le\ell\le4).
\tag{24}
\]
The second inequality telescopes the affine matrix/readout product,
whose derivative costs M^{4-\ell}, and uses (21); gate excesses are
smaller. It also bounds the nonlinear capped fields on the tube.
Consequently actual learned-moment coefficient errors, measured in
original strict density, satisfy
\[
|\Delta M_{A_\ell}|_d\le H eM^{\ell+8}
\quad(\ell=2,3,4),
\]
\[
|\Delta M_{B_\ell}|_d\le H eM^{19-2\ell}
\quad(\ell=2,3,4).
\tag{25}
\]
For example the largest backward moment compares two \delta^2
factors: their norms cost M^3, their difference costs eM^12, hence
the density error is eM^15. The complete original-time row error
costs at most the additional S\le M^5; thus its largest order is
H eM^20. These are bounds on learned moments themselves and do not
presuppose bounds on formal source-response coefficients.

## 5. Absolute nonaffinity margin

Convexity gives \(\|x_4\|=\|D'\|\ge1\). If c^2\le1,
\(\|x_2\|^2\ge[(16+c^2)(32+c^2)]^{-1}\ge1/561\);
if c^2\ge1, the outer balance gives \|x2\|^2\ge2.
For x3, if c^2\le17 use
\(\|x_3\|^2\ge(16+c^2)^{-1}\ge1/33\).
If c^2\ge17, the forward-ratio inequality gives
\[
\|x_3\|^2\ge c^2(1+c^2)(c^2-16)\ge306.
\]
Thus all affine sample preactivations, which are centered Gaussian
by the affine finite source program and its strong Euler limit, satisfy
\[
\operatorname{Var}z_i^1\ge1,\quad
\operatorname{Var}z_i^2\ge1/2244,\quad
\operatorname{Var}z_i^3\ge1/528,\quad
\operatorname{Var}z_i^4\ge1/64.
\tag{26}
\]
The variance is
\(a^{2(\ell-1)}[v\|x_\ell\|^2+(1-v)]\), by the inactive
freezing and orthogonality just proved.

The Gaussian initialization in fact gives a stronger bound than (26),
which is useful for keeping the old regression constant unchanged.
At every fixed normalized affine Euler mesh, each finite-width
coordinate of p and each A_j is a polynomial with nonnegative
coefficients in the independent centered Gaussian coordinates of
p0,A20,A30,A40. This follows inductively from (4), because the steps
and every 1/n normalization are positive. D0 is zero, and transposition
introduces no signs. Each forward coordinate x_ell equals its original
initialized path polynomial P0 plus a polynomial R with nonnegative
coefficients. Every monomial expectation in 2P0R+R^2 is zero or a
product of nonnegative even Gaussian moments. Therefore
\[
E\|x_{\ell,k}\|_n^2\ge E\|x_{\ell,0}\|_n^2=1.
\tag{26a}
\]
The final equality follows by conditioning through the independent
initial Gaussian layers. At fixed Euler mesh the norm recursions bound
every forward field by a fixed polynomial in the initial operator norms
and the initial RMS norm of p. Those initial norms have uniformly bounded
moments of every fixed order: the net argument (2) with a larger threshold
gives the operator tails, and the chi-square moment formula gives the
first-root bound. Thus these second moments are uniformly integrable.
Fixed-program convergence of second moments and
then strong affine Euler convergence give \(\|x_\ell(t)\|^2\ge1\).
Together with the frozen inactive variance this proves
\[
\operatorname{Var}z_i^\ell(t)\ge a^{2(\ell-1)}\ge1/64.
\tag{26b}
\]
This proof concerns expected polynomial coefficients, not positivity
of realized Gaussian matrix entries. In particular the exact old
variance lower bound 1/404, and its old eta_* from the quantitative
proof, are valid at depth four without modification. The explicit
balance-only margin (27) below remains an independent weaker option.

Put m_*^2=1/2244. The third-Hermite test from the quantitative proof
is self-contained and gives
\[
\mathcal R(\sigma G)
\ge\eta_4:=\frac{4\cdot2244e^{-1}}{27\pi\,2245^4}>0
\qquad(\sigma\ge m_*),
\tag{27}
\]
where \(\mathcal R(Z)=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2\).
Explicitly, integration by parts gives
\(E[\arctan(\sigma G)(G^3-3G)]
=-2\sigma^3E[G^2/(1+\sigma^2G^2)^2]\), whose absolute value is
increasing in sigma; restricting at sigma=m_* to |G|\le1 gives (27).
The optimal regression slope belongs to [0,1], so
z\mapsto arctan z minus that slope times z is 1-Lipschitz. Using
each regression minimizer as a competitor for the other variable proves
\[
|\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
\le\|Z-Z_0\|_2.
\]
Therefore H eM^13\le\sqrt{\eta_4}/2 preserves regression error at
least e^2\eta_4/4 for the nonlinear activation in every sample/layer
through the reference feature interval. This applies to the cap limit
once the separate strong cap-removal argument has been established.

## 6. A common enlarged affine initialization family

The normalized gradient field is homogeneous of degree four. Hence
the reference started from all hidden parameters multiplied by beta
and zero readout is exactly
\[
\Theta_\beta(t)=\beta\Theta_1(\beta^3t).
\tag{28}
\]
Take
\[
\beta_j=1+\frac{j}{10^7(48+M^2)^{3/2}}\quad(j=1,2,3),
\qquad
\beta_{far}=1+\frac1{10^6(48+M^2)^{3/2}}.
\tag{29}
\]
The original path extends beyond T for at least 1/(2704M^3) while
c\le2M: on that region its derivative c'=F/c is at most
\(R^4\le(48+4M^2)^2\le2704M^4\). If c starts below M,
that bound precludes its reaching 2M sooner; bounded raw derivatives
give existence until this exit. For beta in (29),
\(\beta^3T-T\le8(\beta-1)<1/(2704M^3)\).
Thus every enlarged path exists on the same original interval.
Homogeneity carries variational propagators to the extended base
path, and (18) gives a bound \(16e^{4000}M^4\).
Primary norms and raw increment bounds remain C M.

Adjacent scale gaps and the remaining far margin are bounded below by
\[
\frac1{10^7\,49^{3/2}M^3}>\frac1{4\cdot10^9M^3}.
\tag{30}
\]
At every fixed chronological affine mesh, Wick expansion gives
nonnegative-coefficient beta polynomials for the active coefficient
entries. Therefore, for beta\le beta3,
\[
f'(\beta)\le
\frac{f(\beta_{far})}{\beta_{far}-\beta}
\le4\cdot10^9 M^3 f(\beta_{far}).
\tag{31}
\]
Fine-mesh Euler estimates retain these bounds with a fixed absolute
factor: local polynomial fields and their variational equations
converge on the just-established common compact interval. There is
no mesh-dependent beta gap and no smallest-step requirement.

## 7. Exact source normalization and probe powers

Use the same sample matrix Q as the earlier source certificate and
\(S_0=\operatorname{diag}(r,\sqrt{1-r^2})\). For every hidden layer,
\[
Qz^\ell=a^{\ell-1}S_0x_\ell,\quad
Qh^\ell=a^\ell S_0\widehat h_\ell,\quad
Q\delta^\ell=a^{5-\ell}rS_0^{-1}d_\ell.
\tag{32}
\]
The full raw matrix updates then become
\(A_\ell'=\sum_{i=+,-}d_{\ell,i}\otimes\widehat h_{\ell-1,i}\),
because the product of their field factors is a^4r=\lambda.
The first-state and readout equations become x1'=d1 and
D'=\widehat h_{4,+}. This verifies normalization for the possibly
nonlinear program as well; it does not rescale the optimizer.

For source arrays, use script A and B to distinguish them from trained
matrix actions. Their exact transformations are
\[
\widehat{\mathsf A}_\ell
=a^{6-2\ell}rS_0^{-1}\mathsf A_\ell S_0^{-1},\qquad
\widehat{\mathsf B}_\ell
=a^{2\ell-6}r^{-1}S_0\mathsf B_\ell S_0.
\tag{33}
\]
In particular, on the active diagonal entry,
\[
\mathsf A_\ell=a^{2\ell-6}r\widehat{\mathsf A}_\ell,
\qquad
\mathsf B_\ell=a^{6-2\ell}r^{-1}\widehat{\mathsf B}_\ell.
\tag{34}
\]
The original strict density has one additional factor
\(\Delta t_j/h_j=\lambda\); hence forward densities obtain the
factor \(a^{2\ell-2}r^2\). Backward rows do not obtain this time
factor. The learned moments become exactly normalized time steps
times E[x_{\ell-1,k}x_{\ell-1,j}^T] or E[d_{\ell,k}d_{\ell,j}^T].

Here is the complete elementary probe cost rule for four populations:

| Injected answer at population ell | Raw-state forcing cost | Observed x_ell cost | Observed d_ell cost |
|---|---:|---:|---:|
| forward x_ell | C M^(4-ell) | C M^(ell-1), plus current identity | C M^(4-ell) |
| backward d_ell | C M^(ell-1) | C M^(ell-1) | C M^(4-ell), plus current identity |

For example a perturbation in x_ell enters precisely the later matrix
and readout updates, with complementary chain products of total degree
4-ell. A perturbation in d_ell enters precisely the first-state and
earlier matrix updates, with complementary products of degree ell-1.
The output costs are obtained by differentiating their chain products.
This explicitly includes inserting a forward coordinate answer at the
first preactivation and a backward answer at the top readout while
retaining the integrated state separately.

To turn these deterministic bounds into source coefficient bounds, use
the same finite-program independent-Gaussian probe identity as in the
audited certificate. Add epsilon times a fresh standard Gaussian root,
with arbitrary deterministic signs at a finite set of source slots,
to the indicated answer. Reflection of that root shows that covariance
and learned-moment parameters are even functions of epsilon. Their
first variation is zero, so the first answer variation is precisely
the formal derivative with those arrays frozen. Take the inner product
of the output with the fresh root. Taking signs of the deterministic
expected derivatives gives the row norm; a single insertion gives a
strict density, with its actual time step. The bounds above and (19)
supply the estimate before taking epsilon to zero. The current identity
terms are retained. This calculation uses only ordinary affine coordinate
instructions and the three independent initialized matrix actions; its
proof is unchanged by appending the third matrix call. It differentiates
neither a covariance square root nor a width limit.

Consequently the following are valid uniformly on the enlarged family,
including the derivative-only transfers associated with each coefficient:

| Source array | Normalized strict density (hence row) | Original-time norm needed |
|---|---:|---:|
| script A2, its forward transfer | H M^4 | strict density H |
| script A3, its forward transfer | H M^6 | strict density H |
| script A4, its forward transfer | H M^8 | strict density H |
| script B4, its backward transfer | H M^4 | row H M^9 |
| script B3, its backward transfer | H M^6 | row H M^11 |
| script B2, its backward transfer | H M^8 | row H M^13 |
| every local forward/backward source resolvent | row H M^7 | row H M^7 |
| top strict transfer x4 from d4 | strict density H M^10 | strict density H |

The normalized forward moments have powers M^2,M^4,M^6, and
the normalized backward moments have powers M^2,M^4,M^6 in top-to-bottom
order, smaller than the listed derivative powers. The local resolvent
power is 4+(ell-1)+(4-ell)=7. The top transfer power is 4+3+3=10.

All affine baseline arrays are sample diagonal. Therefore similarity
in (33) leaves their local resolvent row norms unchanged. The inactive
backward coefficients vanish. With normalized integration matrix I_t,
the inactive forward coefficients are exactly
\[
\widehat{\mathsf A}_{2,-}=2\beta^2I_t,\quad
\widehat{\mathsf A}_{3,-}=3\beta^4I_t,\quad
\widehat{\mathsf A}_{4,-}=4\beta^6I_t.
\]
Their original densities are bounded by absolute constants, since
the transform produces bounded powers of a, beta, and 1-v. Thus no
inverse inactive variance is hidden in the source table.

Every original forward Gaussian innovation has an absolute bounded
standard deviation. Its active factor is r times the corresponding
normalized earlier forward field, at most C r M^(ell-1), and the
inactive factor is bounded by freezing. The original backward Gaussian
innovations zeta1,zeta2,zeta3 have respective standard deviation bounds
\(C M^3,C M^2,C M\). There is no fresh top backward innovation.
The full incoming backward fields can be one power larger; they must
not be identified with these Gaussian sources.

For numerical accounting, initial/extended primary norms can be bounded
by 100M, a forcing or output probe cost by 5(100M)^3, and the propagator
by 16e^{4000}M^4. Multiplying the two largest costs, adding learned
moments, retaining direct terms, changing sample coordinates, and
converting density scales costs less than 10^20e^{4100}. The beta
derivative gap costs at most 4\cdot10^9M^3, still less than the
common numerical allowance 10^30e^{4200}. This is below
\[
H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4
\ge10^{30}e^{5640}.
\tag{35}
\]
Thus H is a valid common prefactor for the primitive affine table,
primal estimates and their beta-differentiated versions with the
additional indicated M^3 power. Products of several such bounds in a
later nonlinear comparison can, of course, require powers of H.

## 8. What the old amplitude already guarantees

Since \(M^{100}\le76^{20}\delta^{-10}\) and \(76^{20}<H\),
\[
e\le10^{-70}H^{-400}\delta^{10}
\quad\Longrightarrow\quad
eM^{100}\le10^{-70}H^{-399}.
\tag{36}
\]
In particular all tube, endpoint, bounded-forward, and absolute
nonaffinity restrictions in this note hold with enormous numerical
room. For the last one, (27) implies \(\sqrt{\eta_4}>10^{-7}\),
whereas H eM^13 is far smaller. The complete depth-four exponent-ten
theorem still requires the source-coefficient supersolution, nonlinear
response/tails and limit bridges; they are not claimed from (36) alone.

## 9. General fixed L and the precise depth dependence

For L\ge2 hidden layers, use the same definitions with
\(F=\langle D,A_L\cdots A_2p\rangle\), degree L+1, and
\(\lambda=a^Lr\). Differentiation proves all adjacent balances in
(5), now with j=2,...,L-1. The operator bounds are
\[
\|A_j\|^2\le16(L-j+1)+c^2,\quad \|p\|^2=1+c^2.
\]
Exactly the same forward/backward ratio argument gives, with
\(K_L=16(L-2)\),
\[
F'\ge(L+1)(c^2-K_L)_+^L,\qquad
F\ge(c^2-K_L)_+^{(L+1)/2}.
\tag{37}
\]
The radial inequality remains c'\ge1. One can choose
\[
M_L=\sqrt{K_L+(3/2)^{2/(L+1)}}\,\lambda^{-1/(L+1)},
\]
which bounds c at the target. Initial and late parts of the time
integral give T\le C_L. For sufficiently large c depending only on L,
\[
dt/dc\le c^{-L}(1+C_L/c^2).
\]
On the radius-one tube the Hessian has norm at most
\(L(\sqrt{16(L-1)+c^2}+1)^{L-1}\). Its product with dt/dc is
L/c plus an integrable O_L(c^-2) remainder. The earlier bounded
c interval is controlled by dt/dc\le1. Thus
\[
\int\|\nabla^2F\|dt\le C_L+L\log M_L,
\quad G\le e^{C_L}M_L^L.
\tag{38}
\]
This proves polynomial propagation for every fixed depth; it does not
leave an exponential in the long original time. The same integrated
forcing calculation gives
\[
E\le C_L eM_L^{2L+2},\qquad
\|\Delta z^\ell\|\le C_L eM_L^{2L+\ell+1}.
\tag{39}
\]
Homogeneity gives beta room of order M_L^{-(L-1)}. The elementary
probe exponents become
\[
|\mathsf A_\ell|_{d,s}\le
C_L M_L^{\max(0,2\ell-L-6)},\qquad
|\mathsf B_\ell|_{r,s}\le C_L M_L^{4L+1-2\ell},
\]
\[
|\text{local resolvent}|_r\le C_L M_L^{2L-1},\qquad
|\text{top strict transfer}|_{d,s}
\le C_L M_L^{\max(0,L-4)}.
\tag{40}
\]
For L4 the smaller M in (1), supplied by (8), and the explicit
4000 constant are preferable to the generic M_L construction.

Uniformity in arbitrary L is not supplied by this route: the early
curvature constant C_L, the primary and probe combinatorial constants,
the factors a^{-L}, the beta gap power L-1, and the source powers in
(40) all depend on L. This identifies a limitation of this certificate,
not impossibility of a depth-independent theorem or a counterexample
to exponent ten.

## 10. Explicit discharge of the conservative response interface

The source argument in SOURCE_RESPONSE.md, Sections 1--7, uses
only a weaker interface than this certificate. Every one of its
requirements follows as follows (M>1 throughout):

| Response-interface requirement | Bound proved here |
|---|---|
| S at most H M^5 and M at most 76^(1/5) delta^(-1/10) | (13)--(14), with S at most M^5 |
| all three beta gaps at least H^(-1) M^(-3) | (29)--(30), taking beta_in=beta1, beta_out=beta2 |
| primary bound H M | (7), (13), and (28)--(29) |
| affine/tube propagator H M^9 | (18)--(19), with the stronger power four |
| A2,V1; A3,V2; A4,V3 densities H, H M, H M^3 | all three are at most H by Section 7 |
| B2,W2; B3,W3; B4,W4 rows H M^18,H M^16,H M^14 | stronger powers 13,11,9 in Section 7 |
| every local R_i,L_i row H M^12 | stronger power seven in Section 7 |
| U1,U2,U3,U4 densities H,H M,H M^3,H M^5 | every density is at most H by the local probe rule |
| bounded original forward Gaussian standard deviations | Section 7, with explicit freezing proof in Section 4 |
| backward Gaussian source powers M^3,M^2,M | Section 7 |
| raw discrepancy H eM^15 | (21), with the stronger power ten |
| layer-ell forward discrepancy H eM^(ell+14) | (22), with the stronger power ell+9 |
| learned backward density H^2 eM^(24-2ell) | (25), with the stronger power 19-2ell and prefactor H |
| learned backward row at most H^3 eM^25 | (25) and S at most M^5, giving H eM^20 |

Here source notation V_i=a^2 U_i follows that response note; its
additional factor a^2 at most one only improves the upper bounds.
The first local transfer U1 maps a backward answer into the first
preactivation; it was explicitly included in the coordinate-probe
argument, so this row is not inferred from an ordinary matrix-answer
probe that would omit the first preactivation direct term.

The remaining requested entry is an *active lower bound*. This has a
direct proof in original variables. On the active sample sector let
I_s,kj=h_j for j<k. Then K1=r^2 I_s and all affine arrays are
entrywise nonnegative. The local resolvent expands into its finite
positive chronological series, so
\[
V_1=a^2(I-a^2K_1B_2)^{-1}K_1\ge a^2r^2 I_s.
\]
Since A2=beta^2 V1 plus a nonnegative learned moment and beta at least
one, the next local transfer satisfies
\[
V_2=a^2(I-a^2A_2B_3)^{-1}A_2
\ge a^2A_2\ge a^4r^2 I_s.
\]
The same calculation with A3=beta^2 V2 plus its nonnegative moment
gives V3 at least a^6 r^2 I_s. By (14),
\[
\min_{i=1,2,3}(V_i)_{kj}
\ge a^6 r^2 h_j
\ge\frac{45}{256}M^{-10}h_j
\ge H^{-2}M^{-10}h_j.
\tag{41}
\]
This holds at every strict slot on every enlarged reference, with no
restriction on the smallest step. It proves the exact positive lower
bound needed for dividing the forward supersolution defects. Thus
all explicitly conditional affine requirements in the conservative
source-response proof have been discharged by this note.
