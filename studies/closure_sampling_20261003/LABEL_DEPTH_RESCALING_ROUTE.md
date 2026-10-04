# Rescaling the carrier exponent removes the double exponential label cap

2026-10-04. Scoped independent derivation, frozen before exchange of new
route findings. This is an internal continuation of the existing compression
investigation, conditional on its specified local insertion and continuation
interfaces. It is not a promotion review. No experiment, Git operation,
maintained-book change, or manuscript change was made.

The source and complex-query proof admits the sufficient restriction

\[
             0<Y/\lambda\le\beta^{-32L},\qquad
             \lambda=\min(1,\gamma/m),                    \tag{1}
\]

where the activation-only number \(\beta\) is defined below. Its carrier
maximum coefficient, complex radius coefficient, and source-dimension
coefficient can retain the expressions in the reconciled explicit source
route. The essential changes are to retain the fourth power of activity
in the endpoint-series feedback and to put \(\log(1/\eta)\) inside the
activity smallness condition when rescaling the budget exponent \(\eta\).

This note proves the source restriction, including all query conditions;
it does not eliminate the separate deterministic runtime restriction in
the existing assembly. With that runtime left unchanged, its evaluable
condition \(Y/\lambda\le Q^{-1}\), where \(Q\le\beta^{280L^2}\),
would still suffice jointly. The improvement of the source cap from a
double exponential to (1) must not be mistaken for a proof that this
older runtime cap is already linear rather than quadratic in depth.

## 1. Inputs, model, and explicit physical constants

Scientific inputs read were the current study's
`EXPLICIT_LABEL_CONSTANTS_ROUTE.md`, `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`
including its reconciliation, `EXPLICIT_ARCHITECTURE_CONSTANTS.md`,
`EXPLICIT_LABEL_SOURCE_CHECK.md`, `LABEL_SEPARATE_BUDGETS.md` and its check,
`DEPTH_INDEPENDENT_EXPONENT.md` and its check, `DEEP_COMPLEX_SOURCE.md`,
and the relevant named prerequisites `DATASET_LABEL_DEPENDENCE.md` and
`DEEP_ACTIVATION_EXTENSION.md`. The explicitly authorized prior inputs
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`, and
`DEPTH_CAVITY_PROBABILITY_CHECK.md` in
`../dense_cutoff_population_rate_20261001/` were read completely; their
further references and appended unrelated unbounded-activation claims are
not inputs here. Required canonical-notation, neural-network, rigorous-proof,
and research-contract/audit instructions were read. No other new route
findings were used before this file was frozen.

Fix \(L\ge2\), \(d,m\ge1\), unit inputs \(v_a=x_a/\sqrt d\), and
the canonical Gaussian width-\(n\) network
\[
z_a^{(1)}=Av_a,\quad z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\quad
f_a=w^\top h_a^{(L)}/n,
\]
with independent initial entries \(A_{ij}\sim N(0,1)\),
\(W_{ij}^{(\ell)}\sim N(0,1/n)\), and \(w(0)=0\). Set
\[
r_a=f_a-y_a,\quad Y=\|y\|_2/\sqrt m,\quad
k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},\quad
k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]
The loss is \(m^{-1}\sum_a r_a^2\), the mobilities are
\((n,1,\ldots,1,n)\), and physical training is
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(\ell)}=-\frac2{mn}\sum_a
r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{2}
\]
The limiting initialized covariance is defined by
\(Q^{(0)}_{ab}=v_a^\top v_b\) and
\(Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)]\),
where \(Z\sim N(0,Q^{(\ell-1)})\). Assume
\(\gamma=\lambda_{\min}(Q^{(L)})>0\).

The activations are real on the real axis, holomorphic on
\(|\operatorname{Im}z|<a\), and uniformly bounded there by \(B_\phi\).
Use exactly the common constants
\[
B=\max(1,B_\phi),\quad s=\max(1,4B/a),\quad
t=\max(1,32B/a^2),\quad \beta=\max(10,B,s,t,16/a).
\tag{3}
\]
They bound activation values and the first two derivatives on the safe
strip. The initialized, real, and complex hidden operator caps are
\(8,9,10\), respectively. The elementary Gaussian-net event with cap
eight is retained from the explicit route, including the normalized
first-weight operator bound. Define the real fitting constants
\[
b_\ell=s(9s)^{L-\ell},\quad F_1=sb_1,\quad
F_\ell=s(B^2b_\ell+9F_{\ell-1}),\quad
C_*=\max(1,B^2b_1,F_L).
\tag{4}
\]
The real energy proof, with a strict initialized normalized gap at least
\(\lambda/2\), supplies
\(\rho=\|r\|_2/\sqrt m\le Ye^{-\lambda t/4}\) and
\(\int_0^\infty\rho\le4Y/\lambda\) if
\(Y/\lambda\le(8\sqrt{C_*})^{-1}\). Fixed-size cavities inherit
this margin for sufficiently large width. Set
\[
 S=16Y/\lambda,\quad \ell_n=\log(en),\quad
 T=32\lambda^{-1}\ell_n,\quad
 d\mu=(2/m)\sum_a|r_a|\,|dt|.
\tag{5}
\]
Real activity is at most \(S/2\). Each contour consisting of its real
segment and the shrinking non-real pieces has activity at most \(S\)
eventually. Its readout satisfies \(\|w\|_\infty\le BS\), and its
residual RMS is at most \(2Y\). These are the existing strict tube
and short-contour arguments; the coefficients of the eventual smallness
conditions below are all explicit.

## 2. Hessian bounds with the exponent visible

For a sample \(a\), stop the empirical carrier budget
\[
\mathcal H_a=\frac1n\sum_{\ell<L,i}
 \exp\!\left(\frac\eta S\sup_z|k_{a,i}^{(\ell)}(z)|\right)
\tag{6}
\]
at \(\mathcal B\), and each autonomous cavity at its own doubled
budget \(2\mathcal B\). The supremum is over its current stopped real
interval or complex time rectangle. No query-angle or sample maximum is
inside this exponential. Temporarily fix \(0<\eta\le1\).

Retain the finite deterministic recurrences
\[
K_\ell=2B(10s)^{L-\ell},\quad P_1=2,\quad
P_\ell=B+10sP_{\ell-1}+1,
\]
\[
A_H=2sP_L+2s^2\sum_{\ell=2}^L K_\ell P_{\ell-1}
                         +tP_L^2K_L,\quad
D_H=t\sum_{\ell=1}^{L-1}P_\ell^2,
\]
\[
H_2=2sP_L+2s^2\sum_{\ell=2}^L K_\ell P_{\ell-1}
                         +t\sum_{\ell=1}^LP_\ell^2K_\ell.
\tag{7}
\]
Here \(\|k_a^{(\ell)}\|_2/\sqrt n\le K_\ell S\). In mobility
coordinates \(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\),
the numbers \(P_\ell\) bound preactivation derivative operators,
also with an external preactivation vector inserted at any one layer.

For a vector use the normalized counting norm, and for a rectangular map
use \(\|M\|_{p,n}=n^{-1/p}\|M\|_{S_p}\). The pointwise inequality
\(x^p\le(p/e)^pe^x\) and (6) give
\[
 \|k_a^{(\ell)}\|_{p,n}
 \le\frac{S}{\eta}\frac pe(2\mathcal B)^{1/p},\quad
 \|k_a^{(\ell)}\|_\infty
 \le\frac S\eta\log(2n\mathcal B),\qquad \ell<L.
\tag{8}
\]
The exact Hessian of \(F_a=nf_a\) consists of mixed terms of rank
at most \(n\), and terms
\(D z_a^{(\ell)\top}\operatorname{diag}
(\phi_\ell''k_a^{(\ell)})D z_a^{(\ell)}\).
The top carrier uses its deterministic coordinate bound. Consequently,
including the augmented Hessian and all its response endpoint blocks,
\[
\|D^2F_a\|_{p,n}
 \le A_H+\frac{SD_H}{\eta}p(2\mathcal B)^{1/p},\quad
\|D^2F_a\|_{2,n}\le H_2,
\]
\[
\|D^2F_a\|_{\rm op}
 \le A_H+\frac{SD_H}{\eta}\log(2n\mathcal B).
\tag{9}
\]
Normalized residual mixtures satisfy the same bounds by the triangle
inequality, even when the sample changes between factors in a product.

The negative-Gram variational base is contractive on positive real time.
All its short backward/complex pieces together have norm cost at most
two eventually. Thus
\[
\|\mathcal J\|_{\rm op}
 \le2\exp\!\left[S A_H+
       \frac{D_HS^2}{\eta}\log(2n\mathcal B)\right].
\tag{10}
\]
The genuine nonvanishing requirement is
\(D_HS^2/\eta\le1/4000\). It leaves the inherited
\(n^{1/1000}\) variational cap after increasing width. The fixed
prefactor in (10) may enter that threshold; its coefficient of \(\log n\)
may not.

## 3. Keep the activity power in the endpoint feedback

For \(h\ge1\), the term with \(h\) residual-Hessian insertions between
two response endpoints has integrated normalized trace at most
\[
\frac{2S^h}{h!}
\left[A_H+\frac{SD_H}{\eta}(h+2)
                    (2\mathcal B)^{1/(h+2)}\right]^{h+2}.
\tag{11}
\]
Assigning Schatten exponent \(h+2\) to its \(h+2\) factors produces
exactly the trace normalization \(1/n\), regardless of the ambient
parameter dimension. Split the power using
\((u+v)^{h+2}\le2^{h+1}(u^{h+2}+v^{h+2})\). The sum of its first
part is \(4A_H^2(e^{2A_HS}-1)\). The second is at most
\[
\frac{8e^2D_H^2S^2\mathcal B}{\eta^2}
 \sum_{h\ge1}\left(\frac{2eD_HS^2}{\eta}\right)^h(h+2)^2.
\]
Here \((h+2)^{h+2}/h!\le e^{h+2}(h+2)^2\). For
\(0\le q\le1/2\),
\(\sum_{h\ge1}q^h(h+2)^2\le36q\). Therefore if
\(A_HS\le1\) and \(2eD_HS^2/\eta\le1/2\), adding the
zero-insertion Hilbert--Schmidt term gives the trace bound
\[
2H_2^2+4A_H^2(e^2-1)
 +\frac{576e^3D_H^3\mathcal B S^4}{\eta^3}.
\tag{12}
\]
The first two terms are independent of \(\eta\). Replacing them by
a power of \(\max(A_H,D_H/\eta)\) would discard this essential fact.

Define the finite coefficients
\[
E=t\sum_{\ell=1}^L(10s)^{2(\ell-1)}K_\ell,\quad
K_{\max}=\max_\ell K_\ell,
\]
\[
D_0=\max\{1,\ B[2H_2^2+4A_H^2(e^2-1)+E]
                       +Bs^2K_{\max}^2\},\qquad
D_1=576e^3 B D_H^3.
\tag{13}
\]
The direct external trace is at most \(ES\) by carrier RMS. The
learned outgoing-column contribution is at most
\(Bs^2K_{\max}^2S^3\). The incoming/outgoing cross form is centered;
the adaptive-residual rank-one trace and insertion remainders vanish
with width by the inherited uniform event. Multiplying (12) by the
exterior activation and activity bounds gives the singleton shift
\[
\sup_{a,z}|k_{a,i}^{(j)}(z)
   -x_i^\top\delta_a^{(j+1),-i}(z)|
\le S\left[D_0+\frac{D_1\mathcal B S^4}{\eta^3}\right]+o(1).
\tag{14}
\]
This uses \(S\le1\), and its constants are independent of deletion
count and empirical moment degree. In the budget exponential its cost is
\[
               \eta D_0+\frac{D_1\mathcal B S^4}{\eta^2}.
\tag{15}
\]
The fourth power of \(S\) in (15) is retained rather than weakened
to a second power with an \(\eta\)-dependent fixed shift.

## 4. The cutoff can preserve an exponent-independent modulus

Normalize real activity by \(u=\mu([0,t])/S\), extend its range to
\([0,1]\) by freezing, and put \(v=|u-u'|\le1\). Direct integration
of (2) gives
\[
\|\Delta w\|_\infty\le BSv,\quad
\|\Delta A\|_F/\sqrt n\le sK_1S^2v,\quad
\|\Delta W^{(\ell)}\|_F\le BsK_\ell S^2v.
\]
Define
\[
V_1=sK_1,\qquad V_\ell=B^2sK_\ell+10sV_{\ell-1}.
\tag{16}
\]
Then the training preactivation increment has RMS at most
\(V_\ell S^2v\). For a non-top carrier, (6) implies the tail estimate
\[
\|k\mathbf1_{|k|>SR}\|_{2,n}
 \le\frac{4S}\eta\sqrt{2\mathcal B}\,e^{-\eta R/4}.
\tag{17}
\]
Indeed, with \(x=\eta|k|/S\), use
\(x^2e^{-x/2}\le16\) and sum the budget. For \(v>0\), choose
\[
R=\frac4\eta\log\frac{8\sqrt{2\mathcal B}}{\eta v},\qquad
\Lambda=\log(e+\mathcal B)+\log(1/\eta).
\tag{18}
\]
Multiplication of (17) by the changed-gate bound \(2s\) gives
\(sSv\). The low-carrier part gives \(tV_\ell S^3Rv\).
For \(\mathcal B\ge2\),
\[
R\le\eta^{-1}[10\Lambda+4\log(1/v)].
\]
Consequently the explicit restriction
\[
                        S^2\Lambda/\eta\le1             \tag{19}
\]
gives \(S^2Rv\le14\sqrt v\): use \(\Lambda\ge1\),
\(v\le\sqrt v\), and \(v\log(1/v)\le2\sqrt v/e\).
At \(v=0\) the increment is zero by continuity.

Thus exactly the previous, \(\eta\)-independent recurrence works:
\[
G_L=sB+2BtV_L,\qquad
G_\ell=10sG_{\ell+1}+Bs^3K_{\ell+1}^2+14tV_\ell+s,
\quad G=\max(1,G_1,\ldots,G_L).
\tag{20}
\]
At the top use the readout coordinate bound. At a lower layer the
changed matrix costs \(Bs^3K_{\ell+1}^2S^3v\); propagation costs
\(10s\) times the next response difference; the two gate terms were
just computed. Downward induction proves
\[
\|\delta_a^{(\ell)}(u)-\delta_a^{(\ell)}(u')\|_{2,n}/S
                      \le G\sqrt{|u-u'|}.
\tag{21}
\]
This is samplewise and cavity measurable. Its dimension and depth
dependence are exactly the displayed finite recurrence, not an implicit
constant depending on \(\eta\).

For an omitted root \(x\sim N(0,I_n/n)\), set
\(Z=\sup_u|x^\top\delta_a(u)|/S\). The process starts at zero.
The explicit dyadic Gaussian estimate in the original route, using
grids of spacing \(4^{-k}\), gives
\[
\Pr\{Z>32G(1+z)\mid\text{cavity}\}\le e^{-z^2},\qquad
\mathbb E[e^{qZ}\mid\text{cavity}]\le
\mathcal M(q):=e^{32qG}
 [1+32qG\sqrt\pi\,e^{256q^2G^2}].
\tag{22}
\]
The grid at level \(k\) has at most \(2\cdot4^k\) increments of
standard deviation at most \(2G2^{-k}\). Thresholds
\(2G2^{-k}\sqrt{2[z^2+4(k+1)]}\) have total failure less than
\(e^{-z^2}\) and sum at most \(32G(1+z)\). Integrating that tail
and completing the square proves the second bound. This also supplies
every fixed higher moment needed for collision tuples.

## 5. A closed finite choice of all budget and label constants

Choose, in this order,
\[
\eta=\min\{1,B^{-1},D_0^{-1},(128G)^{-1}\},\qquad
\mathcal B=64e^2L,
\qquad \Lambda=\log(e+\mathcal B)+\log(1/\eta),
\tag{23}
\]
and
\[
\begin{split}
S_* =\min\bigg\{&1,\ (4A_H)^{-1},\
 \sqrt{\frac\eta{4000D_H}},\
 \sqrt{\frac\eta{16eD_H\sqrt{2\mathcal B}}},\
 \sqrt{\frac\eta\Lambda},\
 \left(\frac{\eta^2}{D_1\mathcal B}\right)^{1/4},\
 (2sK_1)^{-1/2}\bigg\},
\end{split}
\]
\[
 c_{L,\phi}^{\rm src}
 =\min\{(8\sqrt{C_*})^{-1},\ S_*/16\}.
\tag{24}
\]
All denominators are positive. Equations (3)--(4), (7), (13), (16),
(20), and (23)--(24) are an explicit finite recurrence with no dependence
on \(d,m,\gamma,Y\), width, confidence, or empirical moment degree.

If \(0<Y/\lambda\le c_{L,\phi}^{\rm src}\), the real tube,
variational condition, endpoint convergence, and cutoff modulus hold.
The last term also gives normalized first-weight displacement at most
\(1/2\), leaving a strict margin inside the complex cap ten.
The asymmetric query trace conditions are verified in the next section.

Since \(\eta G\le1/128\), (22) gives
\(\mathcal M(2\eta)<6\): its first exponent is at most \(1/2\),
its second at most \(1/16\), and
\(e^{1/2}<2,\sqrt\pi<2,e^{1/16}<2\). The complex correction has
second moment \(\mathbb E e^{2\eta Z_{\rm correction}}\le2\)
eventually, as verified below. Hence its combined first moment is
\[
\mathcal M_c(\eta)=\sqrt{2\mathcal M(2\eta)}<4.
\tag{25}
\]
Moreover (23)--(24) make (15) at most two. The distinct-root moment
base is therefore at most \(4e^2\), and the layer-summed moment ratio is
\[
\frac{(L-1)\mathcal M_c(\eta)
       \exp[\eta D_0+D_1\mathcal B S^4/\eta^2]}{\mathcal B}
                       \le\frac1{16}.                  \tag{26}
\]
For each fixed empirical moment degree \(p\), the limiting probability
that any sample hits its budget is at most \(m16^{-p}\). Distinct roots
are independent conditional on their common cavity; collision tuples use
the finite values \(\mathcal M(q)\) at fixed \(q=p\eta\), and their
normalized counts vanish. The common-cavity comparison and surviving-prefix
transfer use \(e^{\eta o(1)/S}=1+o(1)\). The singleton coefficient
in (14) never becomes a deletion-count-dependent constant. Taking width
to infinity first and then the infimum over fixed \(p\) removes the
budgets. No growing-block limit or conditioning on full survival occurs.

## 6. Query traces, radius, and complex moments retain their coefficients

For the explicit source recurrences use the reconciled substitutions
\[
u_\ell=P_\ell,\quad f_\ell=sP_\ell,\quad
k_\ell=K_\ell,\quad t_\ell=sK_\ell,\quad
j_\ell=20(10s)^{\ell-1},\quad b_\ell=sj_\ell,
\]
\[
                    (h_0,h_1,h_2)=(A_H,D_H/\eta,H_2).
\tag{27}
\]
Use propagation factor ten, and derivative bounds \(s,t\). All RMS
and Hilbert--Schmidt endpoint recurrences are unchanged: explicitly,
\[
g=t_1+B\sum_{\ell=2}^L t_\ell,\quad
r_\ell=u_\ell g,\quad q_\ell=f_\ell g,
\]
\[
e_1=tr_1u_1,\quad
e_\ell=tr_\ell u_\ell+s(q_{\ell-1}+t_\ell Bf_{\ell-1}
                                      +10e_{\ell-1}),
\]
\[
a_1=tj_1u_1+2s,\quad
a_\ell=tj_\ell u_\ell+s(b_{\ell-1}+10a_{\ell-1}),
\]
\[
f_*=\max_\ell f_\ell,\quad
E_Q=\max_\ell(f_\ell H_2+e_\ell),\quad E_J=\max_\ell a_\ell,
\quad T_Q=8f_*E_Q,\quad T_J=8f_*E_J.
\tag{28}
\]
The symbols \(r_\ell\) here are the source's RMS response coefficients,
whereas \(r_a\) in (2) is a residual. The scalar index distinguishes them.

In the asymmetric trace the endpoint exponents are \(2,\infty\),
and each of the \(h\ge1\) Hessians has exponent \(2h\).
The integrated term is at most
\[
2f_*E\frac{S^h}{h!}
 [A_H+2S(D_H/\eta)h(2\mathcal B)^{1/(2h)}]^h.
\]
The split series is controlled by
\(e^{2SA_H}-1\) and
\(\sqrt{2\mathcal B}\sum_{h\ge1}(4eS^2D_H/\eta)^h\).
Both are bounded by one under
\[
SA_H\le1/4,\qquad
16eS^2(D_H/\eta)\sqrt{2\mathcal B}\le1,
\tag{29}
\]
which are explicit entries of (24). At zero insertions use both endpoint
Hilbert--Schmidt bounds. Thus (28)'s trace constants are valid with no
\(\eta^{-1}\) enlargement of their values.

Put
\[
K_{\rm src}=32\max(1,\max_\ell K_\ell,\max_\ell sK_\ell),
\quad G_d=8\sqrt{d+3},
\]
\[
U_1=4sK_{\rm src},\quad
U_\ell=2\{sK_{\rm src}(B^2+f_{\ell-1}^2+T_Q+Bq_{\ell-1})
                      +G_dq_{\ell-1}+1\},
\]
\[
V^{\rm qry}_1=2(2G_d+2sK_{\rm src}+1),\quad
V^{\rm qry}_\ell=2\{G_db_{\ell-1}
                +sK_{\rm src}(T_J+Bb_{\ell-1})+1\}.
\tag{30}
\]
The superscript distinguishes the query coefficient from (16)'s activity
coefficient, resolving the duplicate \(V_\ell\) in the two source notes.
The singleton shift (14) is finite for fixed \(L,S,\eta\). Thus its
ratio to \(S\sqrt{\ell_n}\) tends to zero. The existing polynomial
Gaussian grid improves the carrier maximum to
\(K_{\rm src}S\sqrt{\ell_n}\) with exactly this coefficient; the
larger fixed shift changes only when that bound starts to hold.
The row-insertion identity, (28), and the Gaussian source grids give
\[
\max|R_a^{(\ell)}|\le U_\ell S\sqrt{\ell_n},\qquad
\max|J_j^{(\ell)}|\le V_\ell^{\rm qry}\sqrt{\ell_n}.
\]
With \(U_*=\max U_\ell\), \(V_*=\max V_\ell^{\rm qry}\), take
\[
c=\min\{(8d)^{-1},\ a/[32(4U_*+(d-1)V_*)]\},\quad
r_n=c\ell_n^{-1/2},\quad
M_0=8\max(B,\max_\ell sK_\ell).
\tag{31}
\]
The imaginary preactivation displacement is at most
\(c[4YSU_*+(d-1)V_*]\le a/32\), since (24) gives \(S,Y\le1\).
This retains the strict pole margin. No label restriction depending on
\(d\) has been used: dimension occurs explicitly in (30)--(31).

For completeness the vanishing complex Gaussian correction remains
vanishing after exponent rescaling. The stopped source bounds give
\(\|\dot z_a^{(\ell)}\|_{2,n}\le2r_\ell\rho S\) and
\(\|\dot z_a^{(\ell)}\|_\infty\le2U_\ell\rho S\sqrt{\ell_n}\).
For any real \(p\ge4\), interpolate to exponent \(2p/(p-2)\)
and use (8). This yields
\[
\|k_a^{(\ell)}\odot\dot z_a^{(\ell)}\|_{2,n}
\le\frac{2\rho S^2}\eta\max(r_\ell,U_\ell)
                         p(2\mathcal B\ell_n)^{1/p}.
\tag{32}
\]
The top carrier satisfies the same loose bound because \(\eta\le B^{-1}\).
Take \(p=\max(4,\log(2\mathcal B\ell_n))\). Eventually
\(p\le2\log(e+\ell_n)\) and the last exponential factor is at most
\(e\). Let \(N=\max_\ell(r_\ell,U_\ell)\), and define
\[
J_L^{\rm time}=2sB+4etN,\qquad
J_\ell^{\rm time}=10sJ_{\ell+1}^{\rm time}
                        +2Bs^3K_{\ell+1}^2+4etN.
\tag{33}
\]
Differentiation of the actual backward recursion proves
\[
\|\dot\delta_a^{(\ell)}\|_{2,n}
\le J_\ell^{\rm time}\rho
            [1+(S^2/\eta)\log(e+\ell_n)].
\tag{34}
\]
The changed-matrix term here is bounded by
\(2Bs^3K_{\ell+1}^2\rho S^2\); the changed gate uses (32).
The normalized complex-minus-real reference therefore has radius at most
\[
\tfrac14 c\max_\ell J_\ell^{\rm time}\,ell_n^{-1/2}
                       [1+(S^2/\eta)\log(e+\ell_n)],
\tag{35}
\]
because the short contour length is at most \(2r_n\) and
\(\rho/S\le2Y/S=\lambda/8\le1/8\). Its horizontal and vertical
Lipschitz bounds have the same bracket times fixed coefficients.
The two-parameter dyadic Gaussian net hence has mean
\(O(\ell_n^{-1/2}[\log(e+\ell_n)]^{3/2})\) and tail scale
\(O(\ell_n^{-1/2}\log(e+\ell_n))\), both tending to zero for the
fixed choices (23)--(24). This proves the fixed moment target in (25).
The constants hidden in this last asymptotic multiply vanishing quantities;
they select only the eventual width, unlike the coefficients in (24).

All other changes to the local insertion graph are fixed multipliers of
polylogarithmic coordinate caps, control amplitudes, and derivative bounds.
The uniform net entropy remains \(n^{5/8}\operatorname{polylog}n\);
the weak propagator (10) leaves the Gaussian exponent and nonlinear
remainder powers unchanged. Rectangular cavity comparisons transfer all
doubled caps, and lower-layer query traces precede the next pole exclusion.
These checks preserve the source proof's stop-removal order: local transfer,
carrier maximum, query responses, query poles, complex moment, then budgets.

The approximation coefficients consequently retain the previous bounds
\[
K_{\rm src}\le\beta^{4L},\quad
c^{-1}\le\beta^{40L}(d+3)^{3/2},\quad
R\le\beta^{50Ld}(d+3)^{3d/2}
                    \lambda^{-1}\ell_n^{3d/2+1}.
\tag{36}
\]
Their defining recurrences (27)--(31) do not change in value with \(\eta\).
Four whole-query source families have coordinate magnitude at most
\(M_0\sqrt n\). The horizon and source accuracy \(n^{-1}\) remain the
same. For \(d=1\), use both time-only queries \(v=\pm1\); the previous
factor-two allowance is still present. Exact initialized matrix-image
pairing, initialization-only preprocessing, and coefficient retention are
unchanged.

## 7. An elementary exponential envelope for the evaluated label cap

Here are sufficient bounds on the actual recurrences, with \(L\ge2\)
and \(\beta\ge10\):

| Quantity | Upper bound |
| --- | --- |
| \(C_*\) | \(\beta^{6L}\) |
| \(P_\ell,K_\ell\) | \(\beta^{2L}\) |
| \(D_H\) | \(\beta^{5L}\) |
| \(A_H,H_2\) | \(\beta^{8L}\) |
| \(E\) | \(\beta^{7L}\) |
| \(D_0\) | \(\beta^{20L}\) |
| \(D_1\) | \(\beta^{18L}\) |
| \(V_\ell\) | \(\beta^{6L}\) |
| \(G\) | \(\beta^{12L}\) |
| \(\eta^{-1}\) | \(\beta^{22L}\) |
| \(\mathcal B\) | \(\beta^{3L}\) |
| \(\Lambda\) | \(\beta^{23L}\) |

These are bounds on defined expressions, rather than assignments to an
unspecified source constant. Use \(10s\le\beta^2\) and
\(L\le\beta^{L-1}\). Solving the affine forward recurrence gives
\(P_\ell\le3\beta^{2\ell-2}\le\beta^{2\ell-1}\); the bound for
\(K_\ell\) is immediate. Substitution into (7) gives
\(D_H\le\beta^{5L}\), while the three contributions to \(H_2\)
are at most \(2\beta^{2L+1}\), \(2\beta^{5L+1}\), and
\(\beta^{7L}\); their sum is at most \(\beta^{8L}\).
The same estimates bound \(A_H\). In (13),
\(2+4(e^2-1)<28\), so its first trace coefficient is at most
\(\beta^{17L}\). Also \(E\le\beta^{7L}\), and therefore
\(D_0\le\beta^{20L}\). Since \(576e^3<10^5\),
\(D_1\le\beta^{15L+6}\le\beta^{18L}\).

Each affine recurrence for \(V\) is bounded by at most \(L\) forcing
terms, of size at most \(\beta^{2L+3}\), propagated at most \(L-1\)
steps by \(\beta^2\). This gives \(V\le\beta^{6L}\).
In (20), forcing and terminal coefficients are at most
\(\beta^{6L+4}\); at most \(L\) propagations and their sum give
\(G\le\beta^{12L}\). Equation (23) then gives
\(\eta^{-1}\le\beta^{22L}\). Finally
\(64e^2L\le\beta^{3L}\), and
\(\Lambda\le\mathcal B+\eta^{-1}\le\beta^{23L}\).
The bound for \(C_*\) follows from the finite geometric sum for
\(F_L\) in the original explicit route.

The reciprocals of all entries of the minimum defining \(S_*\) are at
most \(\beta^{24L}\). To check the only substantial products, the
variational square root costs at most \(\beta^{(27L+4)/2}\); the query
square root costs at most \(\beta^{(28.5L+2)/2}\); the modulus square
root costs at most \(\beta^{45L/2}\); and the feedback fourth root
costs at most \(\beta^{65L/4}\). Each is below \(\beta^{24L}\).
The remaining reciprocal entries are smaller. Since \(16\le\beta^L\)
and \(8\sqrt{C_*}\le\beta^{4L}\), (24) in particular gives
\[
                 c_{L,\phi}^{\rm src}\ge\beta^{-32L}.
\tag{37}
\]
This proves (1). The exponents have slack and are not asserted optimal.
For the uncapped gap, \(\gamma\le B^2\) and
\(\lambda\ge\gamma/(mB^2)\). Thus the fully explicit source statement
\[
                    0<Y\le(\gamma/m)\beta^{-34L}
\tag{38}
\]
also suffices. There is no input-dimension or sample-count coefficient in
(37)--(38); data enter through the stated normalized gap.

## 8. Claim level and remaining assembly obligation

The fixed exponent \(\eta=1\) in the preceding explicit label route was
a proof choice. Its moment budget \(\mathcal B\sim e^D\mathcal M_c\)
made the sufficient coefficient doubly exponential in depth. Equations
(12), (18), and (23) avoid that loss without changing the underlying
flow, cavity, source family, or query domain. The rescaled budget is a
proof device and adds no retained state to the compressed optimizer.

The conclusion is conditional on the named inherited Gaussian insertion
and continuation interfaces, whose strict width-power margins were checked
above. It remains a fixed-architecture, fixed-data, sufficiently-large-width
statement. The width threshold is unquantified and can be large as
\(\eta\) or \(Y\) shrink. Neither a growing-depth theorem nor necessity
of the new exponential label cap is claimed. Zero labels are stationary.

For assembling the full all-time compression bound, intersect (24) with
the separately evaluated runtime label condition. The old explicit
runtime envelope alone gives the safe joint choice
\(Y/\lambda\le\beta^{-280L^2}\), because this is smaller than (1).
A linear-depth restriction for that full assembly requires its own
runtime improvement; it is not obtained by silently moving a nonvanishing
runtime coefficient into the width threshold.
