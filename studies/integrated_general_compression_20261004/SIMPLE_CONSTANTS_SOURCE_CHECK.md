# Explicit power envelopes for the source and compact comparison

2026-10-04. Bounded presentation corollary within this study. This checks
numerical envelopes for the already derived source and autonomous compact
model. It does not quantify the stochastic source threshold or establish a
new Gaussian insertion theorem. Inputs are the complete recurrences in
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, equations (5)--(10), (22)--(25), and
(42)--(53), and the complete `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`.

Throughout, the hidden depth is an integer \(L\ge2\), the input dimension
is \(d\ge1\), \(\lambda=\gamma/m>0\), and
\(Y=\|y\|_2/\sqrt m>0\). The source activation parameters are
\[
b=\max_j|\phi_j(0)|,\qquad
s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\},
\qquad
t=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\}.
\]
Use the single persistent activation parameter
\[
\boxed{\beta=\max\{10,1+b,16/a,s,t\}.}
\tag{1}
\]
The full-strip bounded-first-derivative hypothesis remains the source
hypothesis; (1) bounds its persistent half-strip coefficients. Higher
derivative constants still enter the unquantified stochastic threshold.
Write \(z=Y/\lambda\) temporarily in this proof and assume
\[
\boxed{z\le\beta^{-30L}.}
\tag{2}
\]
Thus the source activity allowance \(S=16z\) satisfies
\(S\le\beta^{-26L}\), since \(16\le\beta^{4L}\).

## 1. Elementary absorptions and source base recurrences

All bounds below use \(b\le\beta-1\), \(s,t\le\beta\),
\(10s\le\beta^2\), and
\[
L\le\beta^{L-1},\qquad L+1\le\beta^{L-1},\qquad
4j\le\beta^j\quad(j\ge1),\qquad
\sum_{j=1}^L\beta^{rj}\le
\frac{\beta^{rL}}{1-\beta^{-r}}\quad(r>0).
\tag{3}
\]
The first two inequalities follow by induction from \(L=2\);
the third follows by induction from \(j=1\). Also
\(\log\beta\le\beta\), and \(30\le\beta^2\).

For the source forward recurrence, unrolling the affine map gives
\[
H_j\le22\beta(10\beta)^{j-1}\le3\beta^{2j}.
\]
For example its first value is at most \(21\beta\), and the subsequent
additive contributions sum to at most
\(\beta(10\beta)^{j-1}/(10\beta-1)\). Unrolling the augmented-port
derivative recurrence similarly gives
\[
P_j\le4j(10\beta)^{j-1}\le\beta^{3j-2}.
\]
Consequently, for \(1\le j\le L\),
\[
\boxed{H_j\le3\beta^{2j},\quad
k_j\le3\beta^{4L-2j},\quad
\tau_j\le3\beta^{4L-2j+1},\quad
P_j\le\beta^{3j-2},\quad f_j\le\beta^{3j-1}.}
\tag{4}
\]
These bounds use the actual source RMS recurrence and no global bound on
the activation values.

## 2. Trace constants and the numerical source allowance

Direct substitution of (4) into source (7)--(8), using the geometric sum
in (3), gives the following ledger:

| Source constant | Intermediate bound | Power bound |
|---|---:|---:|
| \(A_*\) | \(7\beta^{5L-3}\) | \(\beta^{5L-2}\) |
| \(D_*\) | \(2\beta^{6L-3}\) | \(\beta^{6L-2}\) |
| \(H_*\) | \(4\beta^{8L-3}\) | \(\beta^{8L-2}\) |
| \(E\) | \(4\beta^{6L-3}\) | \(\beta^{6L-2}\) |
| \(T_0\) | \(3\beta^{16L-4}\) | \(\beta^{16L-3}\) |
| \(D_0\) | \(8\beta^{16L-3}\) | \(\beta^{16L-2}\) |
| \(D_1\) | \(9216e^3\beta^{18L-8}\) | \(\beta^{18L-2}\) |
| \(C_F\) | \(9\beta^{6L-1}\) | \(\beta^{6L}\) |
| \(C_{\rm abs}\) | \(65\beta^{16L-3}\) | \(\beta^{16L-1}\) |

Here are the exponent checks for the terms that could otherwise be
hidden by this table. The mixed summand in \(A_*\) is at most
\(6\beta^{4L+j-3}\); the curvature summand in \(H_*\) is at most
\(3\beta^{4L+4j-3}\). The summand in \(E\) is at most
\(3\beta^{4L+2j-3}\). In \(D_0\), its outer factor is at most
\(2\beta\), and its inner sum is at most
\[
1+3\beta^{16L-4}+4\beta^{6L-3}+9\beta^{8L-2}
\le4\beta^{16L-4}.
\]
For \(D_1\), the coefficient \(9216e^3<200000\le\beta^6\).
In \(C_F\), the inner expression is at most
\(8\beta^{6L-2}+9\beta^{4L}+1\le9\beta^{6L-2}\).
All displayed comparisons hold already at \(L=2,\beta=10\), and the
ratios of the smaller powers decrease when either variable increases.

To check the real activity moduli of source (9), unroll both recurrences.
The first one gives
\[
V_j\le27j\beta^{4L+2j-3},\qquad
\max_jV_j\le\beta^{7L-2}.
\tag{5}
\]
Indeed every propagated forcing term has exponent \(4L+2j-3\).
For the reverse recurrence, its terminal value satisfies
\(G_L\le380L\beta^{6L-2}\). The propagated terminal contribution,
mixed-weight contributions, and curvature contributions at level \(j\)
are bounded respectively by
\[
380L\beta^{8L-2j-2},\quad
27L\beta^{8L-2j-1},\quad
379L\beta^{8L-2j-6}.
\]
The remaining constant contributions total at most
\(2\beta^{2L-2j-1}\). Hence
\[
G_j\le66L\beta^{8L-2j-1},\qquad
\max_jG_j\le\beta^{9L-2},\qquad W_{\rm G}\le\beta^{9L+1}.
\tag{6}
\]
For the last bound, the braces in the definition of \(W_{\rm G}\) are
at most \(2\beta^{9L-2}\), and \(256\le\beta^3\).

The source choices of \(\eta,\mathcal B,\Lambda\) therefore obey
\[
\eta^{-1}\le\beta^{25L+4},\qquad
\mathcal B=1024e^2L\le\beta^{L+3},\qquad
\Lambda\le(26L+8)\log\beta\le\beta^{2L}.
\tag{7}
\]
The first inequality uses \(1024\le\beta^4\); the second uses
\(1024e^2<7600\le\beta^4\). For the last one,
\((26L+8)\log\beta\le30L\log\beta\le\beta^{L+2}\le\beta^{2L}\).

Each nontrivial entry in the minimum defining \(S_*^{\rm src}\) is
at least \(\beta^{-p}\), with the following exponents:

| Entry in source (10) | \(p\) |
|---|---:|
| \((4A_*)^{-1}\) | \(5L-1\) |
| \(\sqrt{\eta/(4000D_*)}\) | \((31L+6)/2\) |
| \(\sqrt{\eta/(16eD_*\sqrt{2\mathcal B})}\) | \((63L+12)/4\) |
| \(\sqrt{\eta/\Lambda}\) | \((27L+4)/2\) |
| \((\eta^3/(D_1\mathcal B))^{1/4}\) | \((94L+13)/4\) |
| \((8D_0C_F)^{-1/2}\) | \((22L-1)/2\) |

These use \(4000\le\beta^4\), \(16e\le\beta^2\), and
\(\sqrt{2\mathcal B}\le\beta^{(L+4)/2}\). Every listed exponent
is at most \(26L\) for \(L\ge2\). We have proved
\[
\boxed{S_*^{\rm src}\ge\beta^{-26L}.}
\tag{8}
\]
In particular the sufficient source label allowance is at least
\(\lambda\beta^{-26L}/16\), and the common cap (2) satisfies it.

## 3. Carrier and query coefficients

Source (22) and (4) give
\[
C_G\le96\beta^{4L-1},\qquad
K_{\rm src}\le1552\beta^{20L-2}
\le\beta^{20L+2}\le\beta^{21L}.
\tag{9}
\]
For source (24), direct substitution and geometric summation give
\[
g\le9L\beta^{4L-1}\le\beta^{5L-1},\quad
r_j\le\beta^{5L+3j-3},\quad q_j\le\beta^{5L+3j-2},
\]
\[
j_j\le2\beta^{2j-1},\quad b_j\le2\beta^{2j},\quad
e_j\le2\beta^{5L+6j-4},\quad a_j\le3\beta^{5j-2},
\]
\[
\boxed{T_Q\le\beta^{14L-3},\qquad T_J\le\beta^{8L-1}.}
\tag{10}
\]
For clarity, the three forcing terms in the recurrence for \(e_j\)
are at most
\(\beta^{5L+6j-4}\), \(\beta^{5L+3j-4}\), and
\(9\beta^{4L+3j-4}\); its propagation factor is at most
\(\beta^2\). The leading exponents grow by six per layer, so their
propagated sum is bounded by the factor two in (10). The angular
recurrence has leading forcing \(2\beta^{5j-2}\), lower forcing
\(2\beta^{2j-1}\), and propagation factor \(\beta^2\); factor
three suffices, including \(a_1\le62\beta\). Finally
\(f_*H_*\le\beta^{11L-3}\), and
\(8f_*\max(f_jH_*+e_j)\le\beta^{14L-3}\);
\(24\le\beta^2\) proves the stated \(T_J\) bound.

Under \(S\le\beta^{-26L}\), both \(ST_Q\) and every
\(S^2H_{j-1}q_{j-1}\) are at most one. The braces multiplying
\(sK_{\rm src}\) in source (25) are at most
\(11\beta^{6L-8}\). Using the sharper bound
\(K_{\rm src}\le\beta^{20L+2}\) from (9), we obtain for \(j\ge2\)
\[
U_j\le22\beta^{26L-5}
 +32\sqrt{d+3}\,\beta^{8L-5}+2.
\]
Also \(U_1\le4\beta^{20L+3}\). These imply
\[
\boxed{U\le\beta^{26L}\sqrt{d+3}.}
\tag{11}
\]
For the query coefficient, the term
\(sK_{\rm src}S^2(T_J+H_{j-1}b_{j-1})\) is at most
\(2\beta^{-24L+2}\le1\). Thus
\[
V_j^{\rm qry}\le64\sqrt{d+3}\,\beta^{2L-2}+4
\le\beta^{2L}\sqrt{d+3}\quad(j\ge2).
\]
The first-layer bound is at most \(67\sqrt{d+3}\), and obeys the
same envelope. Therefore
\[
\boxed{V\le\beta^{2L}\sqrt{d+3},\qquad
c_q^{-1}=\max\{8,8V/a\}\le\beta^{2L+1}\sqrt{d+3}.}
\tag{12}
\]

## 4. Explicit storage envelope with the actual label size

Put \(\ell_n=\log(en)\). For \(d\ge2\), source (35), (11)--(12),
and \(a^{-1}\le\beta/16\) give
\[
A_n\le\frac{2^{16}9^d}{d!}
\beta^{26L+1+(2L+1)(d-1)}
(d+3)^{d/2}z^2\ell_n^{3d/2+1}.
\tag{13}
\]
The coefficient of \((d+3)^dz^4\ell_n^{3d+2}/(d!)^2\) in
\(2040(L+1)A_n^2\) is bounded by
\[
2040(L+1)2^{32}9^{2d}\beta^{48L+4Ld+2d}
\le\beta^{49L+4Ld+4d+12}
\le\beta^{(55+6d)L}.
\tag{14}
\]
Here \(2040\cdot2^{32}<10^{13}\le\beta^{13}\),
\(L+1\le\beta^{L-1}\), and \(9^{2d}\le\beta^{2d}\).
The last inequality uses \(2Ld\ge4d\) and \(6L\ge12\).

For \(d=1\), source (36) instead gives
\[
A_n\le263168\,\beta^{26L+1}\sqrt{d+3}\,z^2\ell_n^{5/2}.
\]
Since \(2040\cdot263168^2<10^{15}\le\beta^{15}\), its squared
storage coefficient is at most \(\beta^{53L+16}\le\beta^{61L}\),
again the last member of (14) at \(d=1\).

Consequently the convenient, slightly enlarged common envelope is
\[
\boxed{\operatorname{size}(C)\le
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
\left(\frac{Ym}{\gamma}\right)^4\log(en)^{3d+2}
+2040(L+1)(2m+d+1)^2+10m(d+1).}
\tag{15}
\]
The actual label factor has been retained. No width-dependent constant or
replacement of \(Y\) by its maximum allowed value occurs in (15).
All source/construction width gates, including the eventual temporal
condition in dimension one, still apply.

## 5. Compact runtime and comparison envelope

For this section only, use the proof abbreviations
\[
X=\beta^L\ge100,\qquad q=1+\lambda^{-1}\ge1.
\tag{16}
\]
They need not appear in the final theorem. The scalar Gaussian covariance
recursion has square-root diagonal bound \((2\beta)^L\le\beta^{2L}\):
its induction is \(u_j\le b+s u_{j-1}\), starting at \(u_0=1\).
Since \(\lambda_{\min}(Q_L)/m\le\max_a(Q_L)_{aa}\),
\[
\lambda\le X^4,\quad Y\le X^{-26}<1,\quad
S\le X^{-26},\quad \lambda^{-1/2}\le\sqrt q.
\tag{17}
\]
The runtime recurrence (5) satisfies
\[
H_c\le X^3,\qquad \max_jd_j^c\le X^3,\qquad F_c\le X^{15}.
\tag{18}
\]
Indeed \(H_j^c\le\beta^{3j}\), because both its first value and
its affine multiplier are bounded using \(20\beta\le\beta^3\).
Also \(d_j^c\le2\beta(\beta^3)^{L-j}\le X^3\),
\(u_j^c\le X^7\), and the last recurrence has first value at most
\(X^4\), propagation at most \(\beta^3\), and forcing at most
\(X^{11}\). Its geometric sum is at most \(3X^{14}\le X^{15}\).
In particular \(16H_c\sqrt{F_c}\le X^{23/2}\le X^{30}\), so
(2) implies the independent compact fitting allowance.

For its effective-readout allowance, Gram bound and endpoint coefficients,
runtime equations (7) and (11) imply
\[
R_c=5z\sqrt\lambda\le X^{-27},\quad
G_c\le X^7,\quad B_w^c\le X^8\sqrt q,\quad B_f\le X^{12}\sqrt q.
\tag{19}
\]
To verify every term, the bracket multiplying \(R_c^2\) in \(G_c\)
is at most \(X^6+4X^{13}\), while \(4H_c^2\le4X^6\).
The middle term of \(B_w^c\) is at most
\(48X^{-27}X^{15}X^{-30}=48X^{-42}\). The other two terms are
at most \(4X^3\) and \(4X^7\sqrt q\). Finally the two terms of
\(B_f\) are at most \(2X^{11}\sqrt q\) and \(2X^{-39}\).

The source constants needed by comparison satisfy
\[
H_{\max}\le X^3,\quad \tau\le X^4,\quad K_{\rm src}\le X^{21}.
\]
Source equations (42) then give
\[
\begin{gathered}
H_r,H_C,P_h\le X^4,\quad P_\delta\le X^5,\quad
D_r\le X^{-21},\quad D_C\le X^{-24},\quad W_r,O\le X^{-22},\
A_f,A_b\le X.
\end{gathered}
\tag{20}
\]
For example the corrections to the constant 18 in \(A_f,A_b\) are
at most one, so \(19\le X\) suffices.

The comparison forward recurrence has first feature coefficient at most
\(X\), propagation at most \(\beta^3\), and forcing at most
\(X^5\). Hence
\[
F,\max_jF_j^z\le X^9,\qquad C_r\le X^5,\qquad B_w\le X^6\sqrt q.
\tag{21}
\]
Here \(C_r\le X^4+2\), and
\(B_w\le1+4X^5\sqrt q\le X^6\sqrt q\).
The backward comparison recurrence has terminal value at most
\(X^{10}\sqrt q\), propagation at most \(\beta^3\), and
additive forcing at most \(X^{10}\sqrt q\). Thus
\[
B\text{ of source (46)}\ \le X^{14}\sqrt q.
\tag{22}
\]
This temporary backward-error coefficient is distinct from the final
envelope defined below.

For source (47), use \(L\le X\),
\(1+(L-1)H_C^2\le X^{10}\),
\(1+(L-1)H_C\le X^6\), and
\(D_C+D_r\le X^{-20}\). The six summands of its \(G\) are at
most, in their displayed order,
\[
X^{14},\quad X^4,\quad X^4\sqrt q,\quad
X^{-27},\quad X^{-11},\quad X^{-39}.
\]
Consequently
\[
G\le X^{15}\sqrt q,\quad P_v\le X^5,\quad
Q_v\le X^{21}\sqrt q,\quad A\le X^{22}q^{3/2},\quad
C_{\rm out}\le X^{11}\sqrt q.
\tag{23}
\]
The bound on \(A\) follows explicitly from
\(4X^{20}q^{3/2}+X^{21}\sqrt q+2X^{15}\sqrt q
\le X^{22}q^{3/2}\). The bound on \(C_{\rm out}\) follows
from \(X^{10}\sqrt q+X^{-13}+X^{-22}\).

The source tangent bound satisfies \(\mathcal K\le X^7\): its
leading term is at most \(X^6\), and its other terms sum to at most
\(2X^{-37}\). Therefore, with the exact definitions in source
(48)--(49),
\[
\boxed{C_{\rm out}\le X^{11}q^{1/2},\quad
a_0,b_0\le X^{22}q^{3/2},\quad
C_{\rm tail}\le X^{13}q^{1/2}.}
\tag{24}
\]
For \(b_0\), specifically, \(K_{\rm src}S^2\le X^{-31}\le1\).
For the tail, \(z(16\mathcal K+4B_f)\le20X^{12}\sqrt q\)
already suffices, even discarding its small factor \(z\le1\).

Define the one persistent comparison envelope
\[
\boxed{\mathsf B=\beta^{100L}(1+\lambda^{-1})^4.}
\tag{25}
\]
Equations (24) imply
\(C_{\rm out},a_0,b_0,C_{\rm tail}\le\mathsf B/100\), since
\(X\ge100\), \(q\ge1\), and the largest power of \(X\) in
(24) is 22. In particular every coefficient is at most \(\mathsf B\).

## 6. A numerical width cost for the label-scaled root error

The exact source comparison, unchanged, is
\[
\sup_{t\in[0,\infty],\,\|v\|=1}|f_C(t,v)-f_n(t,v)|
\le C_{\rm out}n^{-1}e^{a_0+b_0\sqrt{\ell_n}}
 +C_{\rm tail}e^{-8\ell_n}.
\]
For
\[
\boxed{n\ge\left\lceil\max\left\{
e^{64\mathsf B^2},\ (4\mathsf B/Y)^4\right\}\right\rceil,}
\tag{26}
\]
one has \(a_0+b_0\sqrt{\ell_n}\le\ell_n/4\): indeed its two
terms are at most \(\ell_n/64\) and \(\ell_n/8\).
The finite-horizon term is then at most
\(e^{1/4}\mathsf Bn^{-3/4}\le Y/(2\sqrt n)\).
Because \(Y\le1\), \(4\mathsf B/Y\ge4\), and (26) also implies
\(n^{15/2}\ge2\mathsf B/Y\), the tail is at most
\(\mathsf Bn^{-8}\le Y/(2\sqrt n)\). Thus
\[
\boxed{\sup_{t\in[0,\infty],\,\|v\|=1}|f_C(t,v)-f_n(t,v)|
\le Y/\sqrt n.}
\tag{27}
\]
This holds on the same source/initialization event and in addition to all
its construction width conditions. The stochastic source threshold is
still unquantified. Formula (26) is a displayed deterministic cost for
the chosen error coefficient; (27) is not an assertion that \(Y\) is a
sharp stability constant. Zero labels are the separate stationary case.

## Status and scope

Derived here: the source allowance (8), coordinate coefficients (9),
(11)--(12), storage envelope (15), compact comparison envelope (25), and
its deterministic root-conversion cost (26). The same-label cap (2)
also implies the numerical compact fitting allowance. The independent
dense fitting/Legendre allowances are checked in their own notes.

Inherited: the source insertion/selection interfaces, all-time dense and
compact fitting conclusions, and the exact comparison of source §13.
Open here: a numerical stochastic source success threshold, and any
improvement of that threshold or sharpness of the enlarged coefficients.
No experiment, activation-value bound, or trained moment assumption was
introduced.
