# C-H4: a certified integer-expression dyadic radius

Author: scoped agent `/root/h4_route_family`. Date: 2026-09-13.
Status: frozen companion proof to `H4_family_explicit_cap.md`.

Define positive integers by the fixed, finite recursion

\[
E_0=8192,\qquad E_{j+1}=2^{E_j}\quad(0\le j<10),
\qquad E=E_{10},\qquad r_{\rm dyad}=2^{-E}.
\tag{D1}
\]

The ten applications of `pow2` are part of the fixed radius description,
not a loop whose length depends on accuracy. The exponent uses only positive
integer literals and `pow2`, and is therefore admitted by the coordinator's
literal/add/multiply/pow2 grammar. This companion proves

\[
0<r_{\rm dyad}<r_{\rm cap},
\qquad r_{\rm cap}=\exp\{-\Lambda\},\qquad
\Lambda=Z+4+2X+e^{3000},
\tag{D2}
\]

where \(Z,X\) and every constituent of \(r_{\rm cap}\) are exactly the
explicit constants (E2)–(E30) in `H4_family_explicit_cap.md`.
Consequently the entire supported class with
\(|u-e_i|\le2r_{\rm dyad}\), correct binary label, and each label mass one
half lies in the proved time-40 domain of that report. All its existence,
finite-GF identification, risk and paired activity conclusions apply.

## 1. Elementary inequalities used for the dominance bound

The exponential series gives \(2<e<3<4\): for the upper bound use
\(n!\ge2^{n-1}\) for \(n\ge1\), with strict inequality for some terms.
It follows that

\[
e^a<2^{2a}\quad(a>0),\qquad \log2>1/2.
\tag{D3}
\]

We use \(x=E_2\) and \(u=x^{16}\). In particular \(x\ge8192\).
For every integer \(p\le100\),

\[
100\log x\le100x<x^{16}=u.
\tag{D4}
\]

This permits all polynomial factors below to be absorbed into one additional
\(e^u\). For example \(c x^p e^{mu}<e^{(m+1)u}\) whenever
\(c,p\le100\) and the actual bounds satisfy
\(\log c+p\log x<u\); this last inequality holds here because
\(\log c\le100\) and \(p\log x\le100x\), whose sum is below \(u\).

The double-exponential absorption used below is also explicit. For
\(1\le j\le10\) and \(0\le c,p,m\le100\), with \(c\ge1\),

\[
c x^p e^{mu}\exp(e^{ju})<\exp(e^{(j+1)u}).
\tag{D5}
\]

Indeed the additional logarithm on the left is at most
\(100+100x+100u<102u\). The increase in the leading logarithm on the
right is \(e^{ju}(e^u-1)>102u\), since \(u\ge8192\) and the exponential
series gives \(e^{ju}\ge u^2/2\), \(e^u-1\ge u\).
Similarly,

\[
1+\exp(e^{ju})\exp(e^{ku})<\exp(e^{(\max(j,k)+1)u}),
\tag{D6}
\]

because its logarithm is at most
\(\log2+e^{ju}+e^{ku}<3e^{\max(j,k)u}<e^{(\max(j,k)+1)u}\).
All later absorptions are instances of (D4)–(D6), with the displayed
indices and polynomial degrees below.

## 2. Bounding the primitive constants below \(E_2\)

The constants of (E2) satisfy the following deliberately loose bounds:

\[
C,R<e^{80},\quad M<e^{200},\quad W<e^{400},\quad
P_0<e^{400},\quad K_0<e^{300},\quad L<e^{900}.
\tag{D7}
\]

For example \(M<10+80e^{160}<e^{200}\),
\(W<2+80e^{360}<e^{400}\), and
\(L<100(4e^{200})^4=25600e^{800}<e^{900}\).
For \(P_0\), its six summands in (E2), including their coefficients and
the outside factor, sum to at most \(20e^{360}<e^{400}\).
For \(K_0\), use \(1+4e^{280}<e^{300}\).
These numerical separations follow already from \(e>2\), for instance
\(e^{40}>2^{40}>100\) and \(e^{100}>2^{100}>25600\).

The reference amplification \(E\) in (E2), which is distinct from the
integer exponent \(E\) in (D1), is less than \(\exp(e^{1000})\), since
\(40e^{900}<e^{1000}\). Then

\[
B_{\rm cl}<\exp(e^{1001}),\quad B_*,B<\exp(e^{1002}),\quad
D_*,D<\exp(e^{1003}).
\tag{D8}
\]

For the first inequality,
\(B_{\rm cl}<2e^{80}+40e^{700}\exp(e^{1000})\).
The logarithm of this last sum is below \(e^{1000}+708<2e^{1000}<e^{1001}\).
Adding one or two for \(B_*,B\), and then adding at most \(80e^{240}\)
for \(D_*,D\), is absorbed by the indicated next unit increments in the
inner exponent. The strict inequalities use \(e^{1000}>708\) and \(e>2\).

In particular every one of
\(T,C,R,M,W,B_*,B,D_*,D\) is below \(\exp(e^{2000})\). Finally

\[
e^{2000}<2^{4000}<2^{8191}
<2^{8192}\log2=\log E_2,
\tag{D9}
\]

so \(\exp(e^{2000})<E_2=x\). This establishes a common explicit bound
for every primitive used in the remaining estimates. Also
\(e^{3000}<2^{6000}<E_1<x\).

## 3. The checked envelope table

The notation in this table is exactly that of (E4),(E8),(E12),(E19),(E25),
(E27),(E30) of the cap report. Every bound is strict and its right side
uses only \(x=E_2\), \(u=x^{16}\).

| Constants | Upper bound | Verification from their displayed definitions |
|---|---:|---|
| \(Q_{24},d_0\) | \(x^2,x^3\) | \(24C+D<25x\); \(2RT+2C<4x^2\). |
| \(P,f,I_4\) | \(e^u\) | Each exponent is below \(6x^3+192x^6<x^8\); logarithms of outside factors and the extra term in \(f\) leave a total below \(x^{16}\). |
| \(h_1,z_2,a_2,q_2,r_2\) | \(x^2,x^4,x^6,x^8,x^6\) | Substitute the primitive bounds into (E8), absorbing coefficients at most three into one further power of \(x\). |
| \(G,J,F_2\) | \(x^{12},x^{10},x^7\) | Respectively bounded by \(29x^{10}\), \(6x^9\), and \(6x^6\). |
| \(J_0,A_{\rm low},Z_{\rm low}\) | \(x^{14},x^{16}P,x^2P\) | Respectively bounded by \(6x^{13}\), \(30x^{15}P\), and \(2xP\). |
| \(C_v\) | \(e^{3u}\) | \(C_v<e^u(x^{14}+x^{17}e^u+x^2e^u)<x^{18}e^{2u}\); apply (D4). |
| \(C_\alpha,F_\Delta\) | \(e^{4u},e^{5u}\) | Add \((G+1)P\) and then \(F_2\), using (D4). |
| \(U_0,V_0\) | \(\exp(e^{2u}),\exp(e^{3u})\) | \(fd_0T<e^ux^4<e^{2u}\); multiply by \(d_0<x^3\) and use (D5). |
| \(A_U\) | \(\exp(e^{4u})\) | \(TF_\Delta V_0<x e^{5u}\exp(e^{3u})\); (D5) with \(j=3\). |
| \(A_C,A_V\) | \(\exp(e^{3u})\) | They are at most \(x^8U_0\) and \(x^7U_0\), respectively; (D5) with \(j=2\). |
| \(V_{\rm force}\) | \(\exp(e^{5u})\) | At most \(2\exp(e^{3u})+4x^2\exp(e^{4u})<x^3\exp(e^{4u})\); (D5). |
| \(V_{\rm prop}\) | \(e^{2u}\) | \(2f(RT+C)<4x^2e^u<x^3e^u\); (D4). |
| \(C_{\rm src}\) | \(\exp(e^{6u})\) | \(TV_{\rm prop}<xe^{2u}<e^{3u}\); then use (D6) for \(1+\exp(e^{5u})\exp(e^{3u})\). |
| \(Z\) | \(\exp(e^{7u})\) | \(Z<96xC_{\rm src}\le x^2C_{\rm src}\); (D5). |
| \(b_0,a,b_2,b_1\) | \(x^2,x^5,x^6,x^9\) | Direct substitution in (E25). |
| \(A_1,A_2,A_3,C_{\rm raw},\Gamma\) | \(x^{12},x^9,x^8,x^{13},x^{14}\) | The first three are at most \(6x^{11},6x^8,4x^7\); \(C_{\rm raw}<22x^{12}\); multiply by \(T<x\). |
| \(H,S\) | \(x^2,x^3\) | \(H<8x\), \(S<32x^2\). |
| \(R_c\) | \(\exp(e^{8u})\) | \(A<4x^{14}\exp(e^{7u})\), so \(R_c<16x^{17}\exp(e^{7u})<x^{18}\exp(e^{7u})\); (D5). |
| \(X\) | \(\exp(e^{9u})\) | \(X<x^{14}(1+\exp(e^{8u}))<2x^{14}\exp(e^{8u})\); (D5). |
| \(\Lambda\) | \(\exp(e^{10u})\) | \(\Lambda<\exp(e^{7u})+4+2\exp(e^{9u})+x<5x\exp(e^{9u})\); (D5). |

For additional detail on the largest polynomial entry, substituting the
bounds for \(G,Q_{24},J\) in (E12) gives
\(18x^{15}P+12x^{14}P\le30x^{15}P<x^{16}P\).
For the raw comparison, its three velocity coefficients are bounded by
\(2x^{10}+2x^{11}+2x^6\),
\(2x^8+2x^8+2x^6\), and \(x^6+1+2x^7\), respectively. These justify
the table's explicit degrees without counting an unexpanded expression as
one polynomial operation.

Since \(10x^{16}<x^{20}\), the final table entry proves

\[
\Lambda<\exp(\exp(x^{20})).
\tag{D10}
\]

## 4. Comparison with the integer tower

Every \(E_j\) is a power of two. For \(x=2^n\) with integer \(n\ge13\),

\[
x^{20}\le2^{x/2}.
\tag{D11}
\]

The exponent inequality is \(20n\le2^{n-1}\). At \(n=13\) it reads
\(260\le4096\). If it holds at \(n\), then
\(20(n+1)\le40n\le2^n\), so induction proves it for all such integers.
Applying (D3),(D11) with \(x=E_2\),

\[
\exp(x^{20})<2^{2x^{20}}
\le2^{2^{x}}=E_4.
\]

Here \(2x^{20}\le2^{1+x/2}\le2^x\), since \(x\ge2\). Applying (D3)
again and using \(2E_4<2^{E_4}\),

\[
\exp(\exp(x^{20}))<2^{2E_4}<2^{2^{E_4}}=E_6.
\tag{D12}
\]

Thus \(\Lambda<E_6\). Since \(E_7=2^{E_6}>2E_6\) and
\(E_{10}\ge E_7\), (D3) yields

\[
E_{10}\log2>E_{10}/2>E_6>\Lambda.
\tag{D13}
\]

Exponentiating the negatives proves (D2). Ten applications are sufficient;
no evaluation or optimization of the tower is needed.

## 5. Consequences for the executable law interface

The supported class for \(r_{\rm dyad}\) is a subset of the one proved for
\(r_{\rm cap}\), because \(2r_{\rm dyad}<2r_{\rm cap}\).
The original cap proof already used the conservative uniform bounds
\(q\le2r\), \(\varepsilon\le2r\). Hence there is no missing factor two
when substituting the dyadic radius.

In particular choose any rational endpoints in \([-1,1]\) for the two
conditional parameter distributions, each of total probability one, and
give the labels equal masses. Push their parameter values \(s\) to
\(\sqrt2u_i(r_{\rm dyad}s)\), with \(u_i\) from (E34). Every such input
satisfies \(|u_i(r_{\rm dyad}s)-e_i|\le2r_{\rm dyad}\). Nondegenerate
uniform intervals give nonatomic components; degenerate intervals give
atoms. Nonorthogonal atomic choices include \(s_+=0,s_-=1\), with Gram
entry \(-2r_{\rm dyad}/(1+r_{\rm dyad}^2)\ne0\).

All normalized coordinates in this dyadic version are rational numbers
with finite exact expression descriptions; physical coordinates have the
additional exact factor \(\sqrt2\). No denominator with \(E\) bits needs
to be expanded for symbolic identity or support checks. A midpoint
approximation of an interval of parameter length at most two gives the
same Wasserstein error bound \(r_{\rm dyad}/m\) per normalized conditional
law as (E39), because the coordinate map is \(2r_{\rm dyad}\)-Lipschitz.
The family and exponent are fixed independently of refinement and accuracy.

For an ordinary absolute precision request \(p\le E\), the exact enclosure
\(0<r_{\rm dyad}\le2^{-p}\) justifies returning zero as an approximation
with a recorded error bound. Comparisons of an ordinary finite integer
\(p\) against the tower can short-circuit when a lower bound exceeds \(p\).
The law itself remains the exact positive dyadic, and its distinct inputs
are not redefined by rounded coordinates. No uniform practical runtime is
claimed for requests whose precision would force expansion near \(E\) bits.

Only the own cap report, own first report and previously allowed established
sources were used. The companion adds no scientific retrieval, experiment,
implementation change or Git write. All bounds were checked symbolically
against the displayed formulas; independent review remains a separate gate.
