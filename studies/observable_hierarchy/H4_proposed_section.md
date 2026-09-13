##### D. Computation through physical time 40 on a fixed represented family

Parts A–C's short-time statements remain valid with their original law family.
This part supplies a different fixed law family and extends the same dictionary,
initialized Gaussian action, nonlinear closure and numerical computation through
physical time 40. The radius below is extremely small. Qualitative convergence
and operation at a declared numerical resolution are distinct assertions; no
trajectory accuracy certificate, rate, tolerance selector or cost-to-accuracy
bound is asserted.

###### D.1. Fixed family and target

Keep the bias-free two-hidden-layer tanh network, independent stored Gaussian
variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved squared loss and physical
GF. Write `u=x/sqrt(2)`, so `u in S¹`. The initialized Gaussian action is the
same canonical `A0` and its actual adjoint from III.F and C.4.7; only its
learned increment is Hilbert–Schmidt. Finite-network identifications below
retain the actual finite random initial readout. Its zero population limit is
not a finite network with zero initial readout.

Define once and for all

\[
 E_0=8192,\qquad E_{j+1}=2^{E_j}\quad(0\le j<10),\qquad
 \rho=2^{-E_{10}}>0,
 \qquad
 U(s)=\left({1-s^2\over1+s^2},{2s\over1+s^2}\right),\quad
 \mathsf R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
 \tag{H40.F1}
\]

For rational endpoints `-1<=a<=b<=1`, `-1<=c<=d<=1`, let `S` and `V` be
uniform on `[a,b]` and `[c,d]`, respectively, with a degenerate interval
interpreted as its point mass. Define the fixed represented family

\[
 \mathcal F=\left\{
 \tfrac12\operatorname{Law}(\sqrt2U(\rho S),+1)
 +\tfrac12\operatorname{Law}(\sqrt2\mathsf R U(\rho V),-1)
 :a,b,c,d\in\mathbb Q,\ -1\le a\le b\le1,\ -1\le c\le d\le1
 \right\}.                                                   \tag{H40.F2}
\]

Its exact description consists of the fixed eleven-node integer expression
for the exponent, four rational endpoints, the two fixed masses and labels,
and the displayed rational maps. Parameters and support do not shrink with
closure order, numerical refinement or requested accuracy. The identity
`(1-s²)²+4s²=(1+s²)²` proves unit norm, and

\[
 |U(s)-U(t)|={2|s-t|\over\sqrt{(1+s^2)(1+t^2)}}\le2|s-t|.
 \tag{H40.F3}
\]

This follows by expanding the squared distance. In particular the conditional
inputs are within `2rho` of their respective axes. The atomic choice
`a=b=0,c=d=1` has normalized input inner product
`-2rho/(1+rho²)`, strictly nonzero. The rational map is injective, as is its
quarter-turn, so two nondegenerate intervals give a nonatomic law. Thus the
family contains both types; no atom count or positive Gram eigenvalue is an
assumption.

The explicit support proof below supplies the strong canonical population GF
for each such law on `[0,40]`, with the same current-state equation and reached
restart as C.4.7. It also identifies that flow with the actual finite GF limit
in probability. The closure and numerical conclusions in D.3–D.4 are for each
separately fixed law, uniformly in physical time and over the entire input
circle. In particular the target has

\[
 R_\mu(f_\mu(40))\le\tfrac14,\qquad
 J_{\ell,\mu}(1/200)\ge10^{-13}\quad(\ell=1,2),                 \tag{H40.F4}
\]

where `R_mu(f)=int(f-y)² dmu` and `J` is the training-averaged squared
initial/current activation displacement on the same hidden population. These
are target-flow assertions, not acceptance thresholds for any finite run or
an assertion of activity at time 40.

###### D.2. Explicit supported time-40 construction

For a positive number `s`, put

\[
 \mathcal V_s=\{\mu:\mu(y=+1)=\mu(y=-1)=1/2,\quad
 |u-e_1|\le2s\text{ on }\{y=+1\},\quad
 |u-e_2|\le2s\text{ on }\{y=-1\}\},                            \tag{H40.E1}
\]

with inputs on the circle and the support conditions holding almost surely.
This proof gives an explicit `r_cap` such that the C.4.7 construction and
finite-GF identification hold on `V_r_cap`, then proves `rho<r_cap`. It does
not compare rho to an unnamed radius of the original neighborhood `U_1`.
On their intersection the two constructions agree by strong uniqueness on
the same canonical carrier. The reference mesh threshold is needed only
existentially for an eventual limit; it is not a numerical stopping rule.

Within this support proof, numbered subsections 2–6 and symbols E2–E33 refer
to the local displays below; N-labels refer to the complete source calculus
of C.4.7.3. All constants are explicit, finite and independent of atom count,
minimum weight, covariance rank, closure order and numerical accuracy.

**2. Explicit constants and the reference cap**

Set \(T=40\), and define

\[
\begin{gathered}
C=e^{80}-1,\qquad R=e^{80},\qquad
M=10+2TRC,\qquad W=2+2TRMC,\\
L=100(1+M+C+R)^4,\qquad E=e^{LT},\\
P_0=2(MC^2+2RMC+C^2+2RC+C+R),\qquad
K_0=1+2C(M+1),\\
B_{\rm cl}=2C+TP_0K_0E,\qquad B_*=B_{\rm cl}+1,\qquad B=B_*+1.
\end{gathered}
\tag{H40.E2}
\]

These are N9, N38–N47, and the conclusion of the raw-reference transfer.
They use \(10\) as a permissible initialized action-norm bound. The actual
canonical action has the stronger established bound two. For all raw Euler
programs, independently of a source cap,

\[
\|c\|_\infty\le C,\quad |r_a|\le R,\quad
\|A\|_{\rm op}\le M,\quad \|w\|_2\le W.
\tag{H40.E3}
\]

The complete N48–N51 argument supplies some \(h_* >0\) such that reference
raw Euler has every passive backward coefficient row bounded by \(B_*\)
on every mesh of maximal step at most \(h_*\). Its proof requires no
changed-law cap. Duplicating or splitting reference atoms preserves this
bound, by the source-mass argument preceding N21.

Under a temporary cap \(B\) on earlier backward rows, define

\[
\begin{gathered}
D=B+2RC^2T,\qquad Q_{24}=24C+D,\\
P=4R\exp(6RDT+192R^2T^2C^2),\\
f=4R\exp(6RDT+8R^2T^2C^2)+2R,\\
d_0=2RT+2C,\qquad U_0=e^{fd_0T},\qquad V_0=d_0U_0,\\
I_4=2\exp(6RDT+32R^2T^2C^2).
\end{gathered}
\tag{H40.E4}
\]

Here \(P=L_{24}(B)\) from N13. The bound
\(\|N(0,1)\|_{24}\le24\) follows directly from
\(\mathbb E G^{24}=23\cdot21\cdots1\le24^{12}\), which even gives
\(\|G\|_{24}\le\sqrt{24}\). N10 therefore gives
\(\|Q\|_{24}\le Q_{24}\). N14 gives \(|F_{i,p}|\le f m_p\).
N15 gives the pointwise upper source-row bounds

\[
\sum_p|U_{i;p}|\le U_0,\quad
\sum_p|C_{k;p}|\le2RTU_0,\quad
\sum_p|V_{i;p}|\le V_0.
\tag{H40.E5}
\]

The bound for a current upper row needs only the already constructed lower
rows: it does not assume the current unknown backward cap. This causal
order is retained throughout the proof.

All constants in this support proof are scalar positive real numbers. The letters
\(R\) and \(d_0\) in (E2),(E4) denote respectively the residual bound and
the upper-row factor; they are not the raw comparison cutoff or the
C.4.5 numerical error tolerance.

**3. Quantified source comparison under uniformly small input changes**

Consider a finite law with positive weights \(p_a\), labels \(y_a\in\{+1,-1\}\)
of total mass one half each, and normalized inputs \(u_a\). Its split
reference has the same names, weights and labels, with \(v_a=e_1\) for
label \(+1\) and \(v_a=e_2\) for label \(-1\). Suppose

\[
\max_a|u_a-v_a|\le\varepsilon.
\tag{H40.E6}
\]

Run both programs on the same mesh and common canonical source carrier,
as in N20–N21. For a past source \(p=(s,b)\), let \(m_p=h_sp_b\).
Take \(\eta\) to bound their raw sum distance at every node of the prefix,
and suppose

\[
\delta=\eta+\varepsilon\le1,
\qquad I=\delta^{1/16}.
\tag{H40.E7}
\]

Their selected source coefficients are deterministic, and named derivatives
freeze them, the residuals and the covariance laws, exactly as in N4–N8.
For each \(k\), define \(E_k\) as the supremum of the backward-row difference
over **all pairs of passive outputs** \((u,v)\) with \(|u-v|\le\varepsilon\).
Past source names are matched and the distinguished current source is matched.
This includes every paired active output and the identical pair \((u,u)\).
There is no comparison of a distant contaminant against an axis: every
training input obeys (E6).

**3.1 Field and gate constants

Set

\[
\begin{gathered}
h_1=1+W,\quad z_2=1+Mh_1,\quad
a_2=1+2Cz_2,\quad q_2=Ma_2+C,\quad r_2=1+Cz_2,\\
G=1+24h_1+q_2(1+2Q_{24})+r_2,\\
J=2Tr_2C^2+4RTC a_2,\qquad F_2=2r_2+4Rh_1.
\end{gathered}
\tag{H40.E8}
\]

At a paired output, factor subtraction using (E3) gives

\[
\begin{array}{lll}
\|Z^1-\bar Z^1\|_2\le h_1\delta,&
\|H^1-\bar H^1\|_2\le h_1\delta,&
\|Z^2-\bar Z^2\|_2\le z_2\delta,\\
\|\Delta^2-\bar\Delta^2\|_2\le a_2\delta,&
\|Q-\bar Q\|_2\le q_2\delta,&
|r-\bar r|\le r_2\delta.
\end{array}
\tag{H40.E9}
\]

For example the \(Z^2\) difference costs \(M\) times the \(H^1\) error and
the HS increment error; the \(\Delta^2\) difference costs the readout error
plus \(2C\) times the \(Z^2\) error. The final adjoint action costs \(M\)
times that error plus \(C\) times the HS error. The labels are unchanged.

The first-layer gate differences and any past training-query difference
satisfy

\[
\|\phi'(Z^1)-\phi'(\bar Z^1)\|_{12}\le GI,\quad
\|\phi''(Z^1)-\phi''(\bar Z^1)\|_{12}\le GI,\quad
\|Q-\bar Q\|_{12}\le GI.
\tag{H40.E10}
\]

Indeed \(|\phi'|\le1\), \(|\phi''|\le2\), and
\(|\phi'''|\le6\). For the latter, differentiate
\(\phi''=-2\phi\phi'\), and bound
\(2(\phi'^2+|\phi\phi''|)\le6\). Interpolation between \(L^2\) and the
bounded-gate norm gives power \(1/6\), with constant at most \(24h_1\).
For the last difference interpolate \(L^2\) and \(L^{24}\):

\[
\|Q-\bar Q\|_{12}
\le(q_2\delta)^{1/11}(2Q_{24})^{10/11}
\le q_2(1+2Q_{24})\delta^{1/16}.
\]

Every constant being weakened here is at least one, and \(\delta\le1\).
Also \(|r-\bar r|\le GI\), \(|u_a-v_a|\le I\), and
\(|\gamma_a-\bar\gamma_a|\le2m_aGI\).

From N26 and (E9), the complete reverse-coefficient row satisfies

\[
\sum_q|D_{ka,q}-\bar D_{kb,q}|\le E_k+J\delta.
\tag{H40.E11}
\]

The learned part contributes at most
\(2Tr_2C^2\delta+4RTC a_2\delta\): use
\(|\mathrm d\gamma_p|\le2m_pr_2\delta\), both backward fields bounded by
\(C\), and sum \(m_p\le T\). Because (E6) is uniform, no past-source
density estimate is needed to average an input-transport error.

**3.2 Lower pulse difference

Define the following explicit constants:

\[
\begin{gathered}
J_0=2G(1+2R),\\
A_{
\mathrm{low}}=18RGQ_{24}P+2RP(5GD+J),\qquad
Z_{\mathrm{low}}=2RP,\\
C_v=I_4(J_0+TA_{\mathrm{low}}+Z_{\mathrm{low}}),\qquad
C_\alpha=C_v+(G+1)P,\qquad F_\Delta=C_\alpha+F_2.
\end{gathered}
\tag{H40.E12}
\]

For every past backward pulse \(p\), subtraction of N7 yields

\[
\frac{\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2}{m_p}
\le C_v\left(I+\sum_{j<k}h_jE_j\right).
\tag{H40.E13}
\]

Here is a termwise verification of its constant. Put all differences of
the evolving pulse itself into the unbarred propagation. For its coordinate
maximum the propagation coefficient at step \(j\) is at most

\[
2Rh_j\left(D+2\sum_ap_a|Q_{ja}|\right).
\tag{H40.E14}
\]

The direct source, after division by \(m_p\), is
\(-2r_{sb}u_b\phi'(Z^1_{sb})\); its difference has \(L^4\) norm at most
\(J_0 I\). The remaining first term in N7 has varying factors
\(r,u,\phi'',Q,u\), followed by one unchanged normalized reference pulse.
Their telescoping contributions, before the common factor \(2h_jP\),
are bounded respectively by

\[
2GQ_{24},\quad 2RQ_{24},\quad RGQ_{24},\quad 2RG,
\quad 2RQ_{24},
\]

all multiplied by \(I\). Their sum is at most \(9RGQ_{24}I\), using
\(R,G,Q_{24}\ge1\). Hölder with three \(L^{12}\) factors puts every
product in \(L^4\). Thus this forcing costs at most
\(18h_jRGQ_{24}PI\).

In the second, memory term the varied factors are
\(r,u,\phi',D,\phi'_q,u_q\). All unchanged D rows have absolute sum at
most \(D\), their difference obeys (E11), and every unchanged normalized
reference pulse maximum has \(L^{12}\) norm at most \(P\). The five
non-D differences cost at most \(5RGDPI\), and the D difference costs
\(RP(E_j+JI)\), before multiplication by \(2h_j\). Consequently the
forcing at step \(j\), apart from the single direct source, has \(L^4\)
norm at most

\[
h_j A_{\mathrm{low}} I+h_jZ_{\mathrm{low}} E_j.
\tag{H40.E15}
\]

No maximum of an unbounded field discrepancy is used in these estimates:
Minkowski sums the time/source weights after each individual Hölder bound.

The random product of all propagation factors in (E14) is at most

\[
\mathcal I=\exp\left(2RDT+
 4R\sum_{j,a}h_jp_a|Q_{ja}|\right).
\]

N11 with \(\lambda=16R\) gives

\[
\|\mathcal I\|_4
\le2^{1/4}\exp(6RDT+32R^2T^2C^2)\le I_4.
\tag{H40.E16}
\]

Pathwise iteration, followed by Hölder \(L^4\cdot L^4\to L^2\), bounds the
maximum pulse difference by \(I_4\) times the sum of (E15) and the direct
source. This is precisely (E13) with the conservative sum in (E12).
The argument uses the temporary cap only on rows strictly before the
output node under construction.

Subtracting \(\alpha=\mathbb E[\phi'(Z^1)u\cdot v]\), applying (E13),
and applying Cauchy–Schwarz to the changed outside gate and input gives

\[
|\alpha_{ku,p}-\bar\alpha_{kv,p}|
\le m_p C_\alpha G_k,\qquad
G_k=I+\sum_{j<k}h_jE_j.
\tag{H40.E17}
\]

The direct learned term in \(F\) differs by at most \(m_pF_2\delta\):
its residual difference costs \(2m_pr_2\delta\), and its two first-feature
contraction differences cost \(4Rm_ph_1\delta\). Hence

\[
|F_{ku,p}-\bar F_{kv,p}|\le m_pF_\Delta G_k.
\tag{H40.E18}
\]

**3.3 Upper row difference

Set

\[
\begin{gathered}
A_U=TF_\Delta V_0,\qquad
A_C=2TU_0(r_2+2Rz_2),\\
A_V=U_0(4RTz_2+2+6Cz_2),\\
V_{\mathrm{force}}=A_C+A_V+2(RT+C)A_U,\qquad
V_{\mathrm{prop}}=2f(RT+C),\\
C_{\mathrm{src}}=1+V_{\mathrm{force}}e^{V_{\mathrm{prop}}T}.
\end{gathered}
\tag{H40.E19}
\]

Then, whenever all previous nearby-law rows have cap \(B\),

\[
E_k\le C_{\mathrm{src}}\left(I+\sum_{j<k}h_jE_j\right).
\tag{H40.E20}
\]

To verify this, let \(\mathcal U_k\) and \(\mathcal V_k\) be respectively
the suprema over paired outputs of
\(\|\sum_p|\mathrm dU_{ku;p}|\|_2\) and
\(\|\sum_p|\mathrm dV_{ku;p}|\|_2\). Let \(\mathcal C_k\) be the analogous
readout derivative row norm. The direct current impulses cancel. N29,
(E5), and (E18) give

\[
\mathcal U_k\le A_U G_k+f\sum_{j<k}h_j\mathcal V_j.
\tag{H40.E21}
\]

For the readout derivative, its changed residual coefficient contributes
\(2Tr_2U_0\delta\), its changed gate contributes
\(4RTz_2U_0\delta\), and its changed U row propagates with coefficient
\(2R\). Thus

\[
\mathcal C_k\le A_C I+2R\sum_{j<k}h_j\mathcal U_j.
\tag{H40.E22}
\]

For the upper backward field, the changed outside \(\phi'\) gate costs
\(4RTU_0z_2\delta\); the changed readout and outside \(\phi''\) gate cost
\((2+6Cz_2)U_0\delta\). The remaining differences are the C row itself
and \(c\phi''\) times the U row. Therefore

\[
\mathcal V_k\le\mathcal C_k+2C\mathcal U_k+A_V I.
\tag{H40.E23}
\]

Substitute (E21) into (E22)–(E23). Since \(G_j\le G_k\),
\(\sum_{j<k}h_j\le T\), and a double time sum is at most \(T\) times its
single sum, this gives

\[
\mathcal V_k\le V_{\mathrm{force}}G_k+
 V_{\mathrm{prop}}\sum_{j<k}h_j\mathcal V_j.
\]

Discrete Gronwall gives
\(\mathcal V_k\le V_{\mathrm{force}}e^{V_{\mathrm{prop}}T}G_k\).
Taking expected absolute values yields \(E_k\le\mathcal V_k\), proving
(E20). This also verifies that no current unknown \(E_k\) occurs on its
right side. A second discrete Gronwall consequence is

\[
E_k\le C_{\mathrm{src}}e^{C_{\mathrm{src}}T}
 (\eta+\varepsilon)^{1/16}.
\tag{H40.E24}
\]

This is the needed explicit specialization of N24/N31. It does not use the
unquantified constants in those displays.

**4. Explicit raw comparison with one fixed cutoff**

Define an individual raw-component bound \(b_0=2+M+W+C\), and then

\[
\begin{gathered}
a=b_0(b_0+1),\qquad b_2=1+2a,\qquad b_1=b_0(b_2+3),\\
A_1=b_0^2(b_0^3+1)+(b_0+1)b_1+(b_0+1)b_0^2,\\
A_2=b_0(b_0^3+1)+(b_0+1)b_2+(b_0+1)b_0^2,\\
A_3=b_0^3+1+(b_0+1)a,\\
C_{\mathrm{raw}}=2(A_1+A_2+A_3)+4(b_0+1)^2,
\qquad \Gamma=TC_{\mathrm{raw}}.
\end{gathered}
\tag{H40.E25}
\]

For a raw sum distance \(d\), law distance \(q\), and cutoff \(R_c\ge1\),
these constants give

\[
\|\mathcal F_\lambda(\theta)-\mathcal F_{\nu_*}(\bar\theta)\|_{(1)}
\le C_{\mathrm{raw}}\left((1+R_c)(d+q)+
 \tau_{R_c}(\bar c)+\int\tau_{R_c}(\bar Q)\,d\nu_*\right).
\tag{H40.E26}
\]

Here the middle-component norm is HS. A verification is included to remove
any generic constant: at a coupling pair with direction distance \(h\) and
label distance \(l\), the first and second preactivation differences are
bounded by \(b_0(d+h)\) and \(a(d+h)\), while the residual difference is
at most \(b_0^3(d+h)+l\). The upper backward difference is at most
\(b_2(1+R_c)(d+h)+2\tau_{R_c}(\bar c)\). The lower backward difference
is at most
\(b_1(1+R_c)(d+h)+2b_0\tau_{R_c}(\bar c)+2\tau_{R_c}(\bar Q)\).
These follow by the one-cutoff product bound N-T. Telescoping the lower,
middle, and readout velocity products gives respectively \(A_1,A_2,A_3\)
before the common factor two. Their combined tail coefficient is at most
\(4(b_0+1)^2\). The rank difference inequality has the same bound in HS
as in operator norm. Integrating over the coupling proves (E26).

For the capped reference raw Euler program set

\[
D_*=B_*+2RC^2T,\qquad H=4(C+D_*),\qquad S=32C^2.
\tag{H40.E27}
\]

N10 writes each reference \(Q=G+J\), with Gaussian variance at most
\(C^2\) and \(|J|\le D_*\). For \(R_c\ge2D_*\), its tail obeys

\[
\tau_{R_c}(Q)\le H e^{-R_c^2/S}.
\tag{H40.E28}
\]

Indeed \(|Q|\le C|G_0|+D_*\) for a standard normal \(G_0\), and the event
is contained in \(|G_0|>(R_c-D_*)/C\). Using
\(\mathbf1_{|G_0|>a}\le e^{(G_0^2-a^2)/4}\),
\(\mathbb E e^{G_0^2/4}=\sqrt2\), and
\(\mathbb E G_0^2e^{G_0^2/4}=2\sqrt2\), its RMS tail is at most
\(4(C+D_*)e^{-(R_c-D_*)^2/(8C^2)}\). Now
\(R_c-D_*\ge R_c/2\). The Gaussian identities follow by integrating the
Gaussian density and differentiating the scalar Gaussian integral.
The readout tail is zero once \(R_c\ge C\).

For two raw Euler programs on the same admitted mesh, (E26) therefore gives

\[
\eta\le\Gamma e^{\Gamma(1+R_c)}
 \left((1+R_c)q+H e^{-R_c^2/S}\right),
\quad R_c\ge\max(1,C,2D_*).
\tag{H40.E29}
\]

To see this directly, apply the triangle inequality to the two updates and
iterate the scalar recurrence with multiplier
\(1+h_kC_{\mathrm{raw}}(1+R_c)\); the product is at most
\(e^{\Gamma(1+R_c)}\), and the total forcing time is at most \(T\).
Both programs start identically. Their crude raw bounds (E3) suffice, so
this argument imposes no source cap on the nearby-law program. There is
no mesh-error floor in (E29).

**5. Explicit radius and closure of the cap**

The exact constants are

\[
\begin{gathered}
Z=16\{4+(T+1)C_{\mathrm{src}}\},\qquad z=e^{-Z},\\
A=1+\Gamma+H+Z,\qquad R_c=4SA,\qquad X=\Gamma(1+R_c),\\
\boxed{\displaystyle r=\exp\{-Z-4-2X-e^{3000}\}.}
\end{gathered}
\tag{H40.E30}
\]

All symbols on the right have been specified in (E2),(E4),(E8),(E12),
(E19),(E25),(E27); there is no unspecified positive constant.
Every constituent is finite and positive, so \(r>0\). Also
\(r<e^{-4}<1/4\) and \(r<e^{-e^{3000}}\).

For a finite law in \(\mathcal V_r\), its same-label coupling to the split
reference has \(\varepsilon\le2r\) and \(q\le2r\). The cutoff is valid:
\(S\ge1\), \(H=4(C+D_*)\), and \(A\ge H\) give
\(R_c\ge16(C+D_*)\ge\max(1,C,2D_*)\).

The law term in (E29) satisfies

\[
\Gamma(1+R_c)e^Xq\le2Xe^Xr
\le2ze^{-4}Xe^{-X}<z/4.
\tag{H40.E31}
\]

Here \(Xe^{-X}\le1\), and \(2e^{-4}<1/4\).
For the tail term it suffices to show
\(\log(4\Gamma H)+X+Z<R_c^2/S\). Since \(\Gamma,H\ge1\),
\(\log\Gamma\le\Gamma\), \(\log H\le H\), and \(\log4<2\),

\[
\log(4\Gamma H)+X+Z
<2+2\Gamma+H+Z+\Gamma R_c
\le2A+4SA^2\le6SA^2<16SA^2=R_c^2/S.
\tag{H40.E32}
\]

Thus the tail term in (E29) is below \(z/4\), and \(\eta<z/2\).
Furthermore \(\varepsilon\le2r<2ze^{-4}<z/2\), so
\(\delta=\eta+\varepsilon<z<1\), as needed for (E7).

At a first possibly failed nearby-law backward row, every earlier row has
cap \(B\), and all estimates of §3 apply in their causal order. Equation
(E24) gives

\[
E_k<C_{\mathrm{src}}e^{TC_{\mathrm{src}}}e^{-Z/16}
=C_{\mathrm{src}}e^{-4-C_{\mathrm{src}}}<1/4.
\tag{H40.E33}
\]

Use the pair \((u,u)\) in its definition. The reference row is at most
\(B_*\), so the nearby row is below \(B_*+1/4<B\); it cannot fail.
At zero readout the initial backward row is zero, giving the base case.
This proves the uniform passive coefficient cap \(B\) for **every** finite
law in \(\mathcal V_r\), independently of atom count, weights, rank, and
the admitted mesh. A fractional final step is another admitted step, so
the same bound covers recomputed fields on affine interpolation segments.

The conditional nature of the temporary cap has therefore been removed.
No information about the target trajectory was used to choose the radius.

**6. Completion, actual finite GF, and the risk/activity thresholds**

For each finite supported law, the proved cap gives
\(Q=G+J\), \(\operatorname{Var}G\le C^2\), \(|J|\le D\), uniformly for
each passive input and each interpolated time. The same argument as (E28)
gives uniform Gaussian tails above \(\max(C,2D,1)\). Below that threshold,
\(\tau_R(c)+\tau_R(Q)\le2C+D\). For example, with

\[
a_{\rm tail}=1/(32C^2),\quad
M_{\rm tail}=(2C+D+4(C+D))\exp(2D+C+1),
\]

one obtains the exponential estimate N-H for all \(R\ge1\). For large R
use \(R^2\ge R\); for the remaining R, the displayed prefactor dominates
the common second-moment bound. These constants are uniform on the entire
supported domain and do not require a maximum inside a population expectation.

Every law in \(\mathcal V_r\) has finite supported approximations with the
same label masses: partition each compact support cap separately and retain
its mass at a representative in that cap. Their Wasserstein distances tend
to zero, and they stay in \(\mathcal V_r\). Choose any refining mesh sequence
with maximal step tending to zero; it is eventually below \(h_*\).

These are precisely the hypotheses used by the complete proof C.4.7.4:
raw bounds, the HS comparison inequality with tails, uniform N-H on the
finite approximations, and fixed-law compact-domain field continuity.
The logarithmic cutoff argument N-O makes those Euler approximations
Cauchy in \(C([0,T];\mathcal E)\), independently of both choices. N-I
passes the current-state vector field to a strong autonomous \(C^1\) limit.
The tail passage N-P and the one-sided comparison against that constructed
solution give uniqueness against any competing strong raw solution on
the same prescribed carrier, and uniqueness of continuation from a reached
state. Thus all first-claim hypotheses of C.4.7.1 have been supplied on
\(\mathcal V_r\), rather than assumed through membership in an unnamed ball.

The complete proof C.4.7.5 uses one fixed finite comparison law and one
fixed sufficiently fine mesh before the width limit. Both may now be chosen
from the supported approximations just constructed. Its finite-program
identification retains the actual finite initial readout additively. Its
finite-GF/proxy comparison requires common crude finite energy bounds and
tails only for the proxy. Those hold here by the same argument and the
uniform cap above. It therefore gives actual finite-GF capture for each
fixed \(\mu\in\mathcal V_r\), and for arbitrary deterministic or iid
empirical laws tending to that \(\mu\), even if those actual empirical laws
are not themselves supported in the caps. Its observation induction gives
the paired initialized/current joint laws and quadratic contractions.
No finite-width moment bound uniform over changing laws, simultaneous
width/order rate, or numerical finite stopping criterion is added.

For every \(\mu\in\mathcal V_r\), the reference coupling costs at most
\(2r<e^{-e^{3000}}\). The last strict inequality follows from (E30), since
\(2e^{-4}<1\). Hence C.4.5's explicit binary-law risk/activity comparison
applies to actual finite GF with zero discretization defect. Its constants, strict margins and complete source proof are those of
C.4.5.1–3. In particular the reference
paired RMS is strictly greater than \(1/2500000\), and the perturbed squared
margin is bounded below by

\[
(1/2500000)^2-26\cdot10^{-18}
 -8\cdot12^2 e^{-e^{3000}}>1.59\cdot10^{-13}.
\]

The fixed time is physical \(1/200\). The risk comparison has a strict
limiting upper margin \(1/128<1/4\) at time 40. Uniform prediction and
paired observation convergence, now supplied on \(\mathcal V_r\), pass
these finite margins to the population flow exactly as in C.4.7.7.
Keeping the initial hidden field paired on its own layer is part of this
passage; differences between separate marginal hidden laws are insufficient.


**7. Dyadic domination of the support radius.**

Define positive integers by the fixed, finite recursion

\[
E_0=8192,\qquad E_{j+1}=2^{E_j}\quad(0\le j<10),
\qquad E=E_{10},\qquad r_{\rm dyad}=2^{-E}.
\tag{H40.D1}
\]

The ten applications of `pow2` are part of the fixed radius description,
not a loop whose length depends on accuracy. The exponent uses only positive
integer literals and `pow2`, and is therefore admitted by the literal/add/multiply/pow2 grammar. We prove

\[
0<r_{\rm dyad}<r_{\rm cap},
\qquad r_{\rm cap}=\exp\{-\Lambda\},\qquad
\Lambda=Z+4+2X+e^{3000},
\tag{H40.D2}
\]

where \(Z,X\) and every constituent of \(r_{\rm cap}\) are exactly the
explicit constants (E2)–(E30) in the preceding support proof.
Consequently the entire supported class with
\(|u-e_i|\le2r_{\rm dyad}\), correct binary label, and each label mass one
half lies in the proved time-40 domain of that proof. All its existence,
finite-GF identification, risk and paired activity conclusions apply.

**7.1. Elementary inequalities used for the dominance bound**

The exponential series gives \(2<e<3<4\): for the upper bound use
\(n!\ge2^{n-1}\) for \(n\ge1\), with strict inequality for some terms.
It follows that

\[
e^a<2^{2a}\quad(a>0),\qquad \log2>1/2.
\tag{H40.D3}
\]

We use \(x=E_2\) and \(u=x^{16}\). In particular \(x\ge8192\).
For every integer \(p\le100\),

\[
100\log x\le100x<x^{16}=u.
\tag{H40.D4}
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
\tag{H40.D5}
\]

Indeed the additional logarithm on the left is at most
\(100+100x+100u<102u\). The increase in the leading logarithm on the
right is \(e^{ju}(e^u-1)>102u\), since \(u\ge8192\) and the exponential
series gives \(e^{ju}\ge u^2/2\), \(e^u-1\ge u\).
Similarly,

\[
1+\exp(e^{ju})\exp(e^{ku})<\exp(e^{(\max(j,k)+1)u}),
\tag{H40.D6}
\]

because its logarithm is at most
\(\log2+e^{ju}+e^{ku}<3e^{\max(j,k)u}<e^{(\max(j,k)+1)u}\).
All later absorptions are instances of (D4)–(D6), with the displayed
indices and polynomial degrees below.

**7.2. Bounding the primitive constants below \(E_2\)**

The constants of (E2) satisfy the following deliberately loose bounds:

\[
C,R<e^{80},\quad M<e^{200},\quad W<e^{400},\quad
P_0<e^{400},\quad K_0<e^{300},\quad L<e^{900}.
\tag{H40.D7}
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
\tag{H40.D8}
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
\tag{H40.D9}
\]

so \(\exp(e^{2000})<E_2=x\). This establishes a common explicit bound
for every primitive used in the remaining estimates. Also
\(e^{3000}<2^{6000}<E_1<x\).

**7.3. The checked envelope table**

The notation in this table is exactly that of (E4),(E8),(E12),(E19),(E25),
(E27),(E30) of the preceding cap proof. Every bound is strict and its right side
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
\tag{H40.D10}
\]

**7.4. Comparison with the integer tower**

Every \(E_j\) is a power of two. For \(x=2^n\) with integer \(n\ge13\),

\[
x^{20}\le2^{x/2}.
\tag{H40.D11}
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
\tag{H40.D12}
\]

Thus \(\Lambda<E_6\). Since \(E_7=2^{E_6}>2E_6\) and
\(E_{10}\ge E_7\), (D3) yields

\[
E_{10}\log2>E_{10}/2>E_6>\Lambda.
\tag{H40.D13}
\]

Exponentiating the negatives proves (D2). Ten applications are sufficient;
no evaluation or optimization of the tower is needed.


Therefore `rho=r_dyad<r_cap`, and (H40.F3) gives
`F subset V_rho subset V_r_cap`. Every finite componentwise midpoint law stays
in the same supported domain. The horizon extension below uses the actual
strong solution, uniform passive Gaussian tails, initialized observable-space
invariance and actual finite-GF identification supplied by this construction.
It makes no assumption that `V_rho` is contained in a previously unnamed
Wasserstein ball.

###### D.3. Compatible closure on the explicit time-40 domain

Fix physical time `T=40` and the positive dyadic radius defined in D.1–D.2:

\[
 E_0=8192,\qquad E_{j+1}=2^{E_j}\ (0\le j<10),\qquad
 \rho=2^{-E_{10}}.
 \tag{H40.C1}
\]

Let `V_rho` consist of Borel laws on `sqrt(2) S1 x {+1,-1}` with mass
one half at each label and, almost surely,
`|u-e_1|<=2rho` for label `+1` and `|u-e_2|<=2rho` for label `-1`,
where `u=x/sqrt(2)`. Data Wasserstein distance uses
`|u-v|+|y-z|`. Fix one law `mu` in this class. The exact population
conclusions below apply to every such separately fixed law. The finite
numerical assertion in D.4 uses the represented rational-endpoint laws
of D.1, whose exact radius is (H40.C1).

The model is the bias-free two-hidden-layer tanh network with independent
stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual
`f-y`, and unhalved mean-square-loss physical GF. Write
`H_l=L2(Omega_l)`, `w in L2(Omega_1;R2)`, `c in H_2`, and
`A=A_0+K:H_1 -> H_2`, where only `K` is Hilbert–Schmidt. The retained
initialized action and its actual adjoint have their common canonical
Gaussian realization, `||A_0||op<=2`; initially `(w,K,c)=(g,0,0)` with
`g~N(0,I_2)`. With `phi=tanh`, use

\[
 \begin{gathered}
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),\\
 \Delta^2(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^2(u),\quad
 f(u)=E_2[cH^2(u)],\quad r(u,y)=f(u)-y,\\
 (w',K',c')=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\Delta^2(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).
 \end{gathered}
 \tag{H40.C2}
\]

Every expectation and rank contraction is within its stated layer. Here
\(\mathcal L_\mu=\int(f-y)^2\,d\mu\), and the raw metric is
\(\|(v,L,z)\|_{\rm raw}^2=\|v\|_2^2+\|L\|_{\rm HS}^2+\|z\|_2^2\).
The finite prediction with these conventions is
\(f_n(x)=n^{-1}(W_n^{(3)})^T
\phi(W_n^{(2)}\phi(W_n^{(1)}u))\).

**The reference trajectory supplied by the explicit cap.** D.2 proves
the passive source-row cap for all finite laws in `V_rho` on every
sufficiently fine raw Euler mesh, with constants independent of atom
count, weights and covariance rank. It proves this on the stated
supported class; no comparison of `rho` with an unnamed radius from
C.4.7.1 is needed. Its raw/action bounds, HS comparison estimate,
passive tails and supported finite-law approximations are exactly the
hypotheses of the completion argument in C.4.7.4. Consequently that
argument gives a canonical strong `C1` solution of (H40.C2) through
time 40, unique among strong raw solutions on the same initialized
carrier and uniquely restartable from each reached state. In particular

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta_\mu'(s)\|_{\rm raw}^2ds=1,
 \qquad\|c(t)\|_\infty\le2t,
 \qquad\theta_\mu=(w,K,c).
 \tag{H40.C3}
\]

The same construction supplies constants `a_tail,M_tail>0` such that

\[
 \sup_{t\le40,u\in S^1}\tau_R(Q(t,u))
       \le M_{\rm tail}e^{-a_{\rm tail}R^2},\qquad
 \tau_R(V)=\|V1_{|V|>R}\|_2,\quad R\ge1.
 \tag{H40.C4}
\]

Here is the Gaussian-tail passage explicitly. D.2's finite supported
programs have each passive answer `Q_j=G_j+J_j`, with Gaussian variance
bounded by `(e^80-1)^2` and a deterministic common bound on `|J_j|`.
The scalar Gaussian tail calculation in C.4.7.3 therefore gives uniform
Gaussian RMS tails at their nodes and affine interpolation times. Their
strong raw convergence implies `Q_j(t,u)->Q(t,u)` in `L2` at every
fixed `(t,u)`, by the bounded-multiplier and action continuity used in
C.4.7.4. Since `V -> (|V|-R)_+` is 1-Lipschitz on `L2`,

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2
       =2\lim_j\|(|Q_j|-R)_+\|_2\le2\sup_j\tau_R(Q_j).
\]

Rescale the cutoff and enlarge the prefactor on its remaining bounded
range to obtain (H40.C4). These are individual time/input tails with
common constants, not tails of a random supremum. Averaging them against
the training law preserves the bound.

The fixed-program identification and finite-GF/proxy comparison of
C.4.7.5 also apply on this explicit domain. Indeed their comparison law
and sufficiently fine mesh can be chosen from the supported finite
approximations used in D.2; their raw bounds and passive tails have just
been supplied. The finite program is fixed before width tends to
infinity, its learned ranks have the same HS/Frobenius contraction
identity, and its proxy retains the actual finite initial readout
additively. The law-independent finite GF energy bounds control the
other endpoint of the comparison. This identifies the reference above
with actual finite GF through time 40, for fixed `mu`, and for any
deterministic laws on `sqrt(2) S1 x [-1,1]` approaching `mu` in `W1`
with widths tending to infinity; those actual laws need not satisfy the
support cap. Convergence is in probability in the prediction and joint
second-moment observation senses of C.4.7.5. For iid empirical laws,
sample count and width may grow arbitrarily, with convergence in their
joint probability. No finite random readout has been replaced by zero.

**Dictionary, state and equations.** Retain exactly the full dictionary
of part B: the total-degree-at-most-`N` Chebyshev products in
`(tanh g_1,tanh g_2,tanh p_1,tanh p_2)` and
`(tanh xi_1,tanh xi_2)`, with
`xi_i=A_0 tanh g_i`, `p_i=A_0^* tanh xi_i`, followed by every bounded
valid initialized-word code through `N` not already present literally.
The ordering, rational code, bounded-operand rules and complete finite
source initialization are unchanged. In particular the exhaustive tail
uses both orientations of the same action and is not replaced by the
polynomial core alone. Let `psi_l,N` be the raw retained column and set

\[
 \begin{gathered}
 G_l=E_l[\psi_l\psi_l^T],\quad
 \eta_N=[1024(N+1)^2]^{-1},\quad L_lL_l^T=G_l+\eta_NI,
 \quad b_l=L_l^{-1}\psi_l,\\
 C_N=E_2[\psi_2(A_0\psi_1)^T],\qquad
 D_N=L_2^{-1}C_NL_1^{-T},\\
 \lambda_{1,N}=\operatorname{Law}_1(b_1,g),\qquad
 \lambda_{2,N}=\operatorname{Law}_2(b_2).
 \end{gathered}
 \tag{H40.C5}
\]

All contractions use the complete joint initialization program of B/C.2.
The fixed input `D_N^T` is the reverse contraction. These coefficients,
marks and ridge use no target trajectory or time mesh.

The exact saved state is a finite matrix `M` and the two current joint
population laws `Gamma_1=Law(b_1,g,w)` and `Gamma_2=Law(b_2,c)`, together
with fixed `D_N` and the data-law interface. Initially `w=g,c=0,M=D_N`.
For each `u` compute

\[
 \begin{gathered}
 a_N(u)=E_1[b_1\phi(w_N\cdot u)],\quad
 H_N^2(u)=\phi(b_2^TM_Na_N(u)),\quad
 f_N(u)=E_2[c_NH_N^2(u)],\\
 d_N(u)=E_2[b_2c_N(1-H_N^2(u)^2)],\quad
 Q_N(u)=b_1^TM_N^Td_N(u),\quad r_N=f_N-y,\\
 w_N'=-2\int r_N\phi'(w_N\cdot u)Q_N(u)u\,d\mu,
 \quad c_N'=-2\int r_NH_N^2(u)\,d\mu,\\
 M_N'=-2\int r_Nd_N(u)a_N(u)^T\,d\mu.
 \end{gathered}
 \tag{H40.C6}
\]

The population laws are pushed forward by these characteristics. These
equations are autonomous and have no retained Gaussian-action query,
history, cutoff limit, or omitted hierarchy field in their right side.

For analysis let `U_l v=b_l^T v`, `Q_l,N=U_lU_l^*`. Formula (H3.2)
applies to exactly (H40.C5), so these are positive contractions and
`U_l` is a contraction. On the canonical carrier put

\[
 B_N=Q_{2,N}A_0Q_{1,N},\quad
 K_N=U_2(M_N-D_N)U_1^*,\quad A_N=B_N+K_N=U_2M_NU_1^*.
 \tag{H40.C7}
\]

The current action is bounded and its reverse is its actual adjoint.
In particular, lifting the matrix equation gives exactly

\[
 K_N'=Q_{2,N}\left[-2\int r_N\Delta_N^2(u)\otimes H_N^1(u)\,d\mu\right]Q_{1,N},
 \quad H_N^1=\phi(w_N\cdot u),\quad
 \Delta_N^2=c_N\phi'(A_NH_N^1).
 \tag{H40.C8}
\]

No small operator-norm difference between `B_N` and `A_0` is assumed.

**Energy, existence and restart.** At fixed `N`, all feature coordinates
are bounded. On the fixed joint mark spaces the equations are locally
Lipschitz in bounded `w-g`, bounded `c`, and finite `M`: subtract finite
products, use the feature envelopes, `|u|=1`, and the bounded derivatives
of tanh. The unbounded frozen `g` appears only inside those gates.
Thus the contraction construction in C.4.7.9.4 applies. Its continuation
through the longer interval follows from the following bounds.

The three negative velocities are the gradients for the population
`L2` row/readout metrics and the ordinary coefficient Frobenius metric.
For example `delta f=d_N^T(delta M)a_N`. For atomic populations with
weights `p_{1,i},p_{2,j}`, the ordinary derivatives in `w_i,c_j` equal
`-p_{1,i}w_i'` and `-p_{2,j}c_j'`; the velocities already use the weighted
metric, so no further node weight is inserted in them. Therefore

\[
 \mathcal L_N'=-\|w_N'\|_2^2-\|c_N'\|_2^2-\|M_N'\|_F^2,
 \quad\mathcal L_N(0)=1,
\]
\[
 \begin{gathered}
 \|c_N(t)\|_\infty\le2t,
 \quad\|M_N-D_N\|_F\le2t^2,
 \quad\|K_N\|_{\rm HS}\le2t^2,\\
 \|A_N\|_{\rm op}\le2+2t^2,
 \quad\|w_N(t)\|_2\le\sqrt2+4t^2+2t^4.
 \end{gathered}
 \tag{H40.C9}
\]

Indeed `int |r_N| dmu<=1`, `|a_N|<=1`, `|d_N|<=||c_N||2`, and
`||D_N||op<=2`; integrating the readout, matrix and row speed bounds
gives these inequalities. At fixed order, with
`K_l=(sum_i ||b_l,i||infty^2)^(1/2)`, one also has
`||w_N'||infty<=4t K_1||M_N||op`. Thus `w_N-g,c_N,M_N` stay in a bounded
existence ball on each finite interval, and their bounded speeds give
Cauchy endpoints there. Local continuation proves existence through 40
and indeed through every finite time at fixed order. The same proof,
starting with a saved current joint law and its energy/readout bounds,
gives unique own-state continuation. No extra history or Gaussian roots
are introduced at restart.

**Generated spaces and the omitted sources.** Let `H_l^obs` be the
initialized observable `L2` spaces from C.4.7.8.5. Their bounded words
have dense span; rational marks generate the same completed spaces, as
proved in C.4.7.9.2. Both `A_0` and `A_0^*` preserve the appropriate
spaces, and actual adjunction makes them a reducing pair. Every finite
supported raw Euler step from initialization keeps `w,c` in these
spaces and adds to `K` a sum of ranks between them. Bounded coordinate
operations preserve the generated sigma fields, and each action preserves
the spaces; induction proves this assertion. D.2's time-40 strong
completion then keeps the exact trajectory in these closed spaces and
`K(t)` in their closed HS block. Its strong derivative `K'(t)` is in
that block as well. This uses the time-40 completion, not part A's
short-time existence statement.

Part B's filter proof applies without a horizon restriction. On a vector
`S_Nv` from a fixed earlier raw span,
`||(I-Q_l,N)S_Nv||2^2<=eta_N|v|^2/4`. Zero-padding fixes `|v|` as
`N` increases; density and contraction extend this to strong convergence
`Q_l,N -> I` on `H_l^obs`. Hence both `B_N -> A_0` and
`B_N^* -> A_0^*` converge strongly, with common operator bounds. For a
compact `L2` set this convergence is uniform, by a finite net and the
operator bound on the point-to-net error.

The exact fields `H^1(t,u),Delta^2(t,u)` have compact `L2` images on
`[0,40] x S1`, by strong raw continuity, bounded readout, and the
bounded-multiplier lemma of C.4.7.4. The derivative `K'(t)` is a compact
HS curve. Consequently the following proof error tends to zero:

\[
 \begin{split}
 \epsilon_N={}&\sup_{t,u}\|(B_N-A_0)H^1(t,u)\|_2
       +\sup_{t,u}\|(B_N^*-A_0^*)\Delta^2(t,u)\|_2\\
       &+\sup_t\|Q_{2,N}K'(t)Q_{1,N}-K'(t)\|_{\rm HS}\longrightarrow0.
 \end{split}
 \tag{H40.C10}
\]

For the HS term, approximate each target by a finite sum of ranks.
Strong convergence handles both factors of each rank, contraction bounds
the discarded HS remainder, and a finite net of the compact derivative
curve gives uniformity. No term in (H40.C10) is supplied to the equations,
initializer or order-selection rule.

**Direct comparison through time 40.** On the common carrier define
`e_N=||w_N-w||2+||K_N-K||HS+||c_N-c||2`. Bounds (H40.C3),(H40.C9) and
the exact rank equation give one common raw/action ball, independent of
`N`. Forward subtraction gives, uniformly in `u`,

\[
 \begin{gathered}
 \|H_N^1-H^1\|_2\le e_N,\qquad
 Z_N^2-Z^2=A_N(H_N^1-H^1)+(K_N-K)H^1+(B_N-A_0)H^1,\\
 \|Z_N^2-Z^2\|_2+\|H_N^2-H^2\|_2+|f_N-f|
                          \le C(e_N+\epsilon_N),\\
 \|\Delta_N^2-\Delta^2\|_2+\|Q_N-Q\|_2
                          \le C(e_N+\epsilon_N).
 \end{gathered}
 \tag{H40.C11}
\]

For the last line subtract
`(c_N-c)phi'(Z_N^2)+c[phi'(Z_N^2)-phi'(Z^2)]` and then
`A_N^*(Delta_N^2-Delta^2)+(K_N-K)^*Delta^2+(B_N^*-A_0^*)Delta^2`.
The reference readout is bounded, so these are `L2` estimates. The
remaining first gate uses a cutoff on the unchanged reference `Q`:

\[
 \|\phi'(w_N\cdot u)Q_N-\phi'(w\cdot u)Q\|_2
 \le C(e_N+\epsilon_N)+2R e_N+2\tau_R(Q(t,u)),\quad R\ge1.
 \tag{H40.C12}
\]

Below the cutoff use `Lip(phi')<=2`; above it use the bounded gates.
Only the exact reference needs tails. For the middle velocity, writing
`F_K` for the exact middle rank integral in (H40.C2), (H40.C8) gives

\[
 K_N'-K'=Q_{2,N}\{F_K(w_N,A_N,c_N)-F_K(w,A,c)\}Q_{1,N}
                    +(Q_{2,N}K'Q_{1,N}-K').
 \tag{H40.C13}
\]

Subtract its residual and rank factors, using
`||a tensor b-a' tensor b'||HS<=||a-a'||2||b||2+||a'||2||b-b'||2`.
The first term is at most `C(e_N+epsilon_N)` and the second is at most
`epsilon_N`. Subtracting the row and readout velocities with
(H40.C11)–(H40.C12), and using (H40.C4), therefore gives

\[
 D^+e_N\le C(1+R)(e_N+\epsilon_N)+CM_{\rm tail}e^{-a_{\rm tail}R^2},
 \qquad e_N(0)=0,
\]
\[
 \sup_{t\le40}e_N(t)
 \le CT e^{C(1+R)T}
       \{(1+R)\epsilon_N+M_{\rm tail}e^{-a_{\rm tail}R^2}\}.
 \tag{H40.C14}
\]

The error is absolutely continuous as a sum of norms of strong Hilbert
curves; the norm upper-derivative inequality also holds at zero. The
second line follows from the scalar exponential integrating factor.
First let `N -> infinity` at fixed cutoff, then let `R -> infinity`.
The negative quadratic exponent dominates `C(1+R)T` for the fixed
`T=40`, proving uniform raw convergence. No tail or higher-moment
assumption has been imposed on projected trajectories. Comparing any
competing strong raw path against the reference with zero initial error
uses the same tail-only bound and forces equality; reached continuation
uses its restriction. Thus the identification does not invoke uniqueness
of arbitrary formal hierarchy sequences.

**Observations.** Equation (H40.C11) proves convergence of predictions
uniformly on `[0,40] x S1` and of both current hidden fields uniformly
there in `L2`. The initial lower field is exact; the initial upper field
is `phi(B_N phi(g·u))` and converges uniformly in `u` by strong action
convergence on its compact target set. More generally the observation
induction of C.4.7.9.6 applies: seed errors tend to zero, the action norms
are uniformly bounded, both action directions converge on compact target
curves, and each bounded node has a common finite syntax envelope at its
fixed marks. Its action subtraction is
`A_NV_N-AV=A_N(V_N-V)+(K_N-K)V+(B_N-A_0)V`; bounded products use their
envelopes, and a bounded continuous gate times a named `L2` field uses
truncation of the fixed target field and compact-curve tail control.
These are exactly the hypotheses needed for every separately fixed
admitted same-layer tuple and its second moments.

In particular define, keeping the same initialized/current neuron and
input in each pair,

\[
 \mathcal P_{l,N}(t)=\operatorname{Law}_{\Omega_l\otimes\mu}
       (H_N^l(0,u),H_N^l(t,u)),\qquad
 R_{l,N}(t)=\|H_N^l(t,u)-H_N^l(0,u)\|_{L^2(\Omega_l\otimes\mu)}.
 \tag{H40.C15}
\]

Use the analogous definitions without `N` for the reference. The
common-carrier coupling bounds squared pair `W2` by the sum of the
two squared `L2` errors. The reverse triangle inequality bounds the RMS
error by the `L2` error of their paired differences. Thus both converge
uniformly in time. Since `|f_N|,|f|<=2T`,

\[
 \sup_{t\le40}|\mathcal L_N(t)-\mathcal L_\mu(t)|
 \le2(2T+1)\sup_{t,u}|f_N(t,u)-f_\mu(t,u)|\longrightarrow0.
 \tag{H40.C16}
\]

These target observations have the actual finite-network meaning already
established above. Full-row input continuity, bounded raw speeds and
finite time/input nets give the same uniform-time passages for bounded
hidden pairs and their training averages; no cross-layer neuron pairing
or cross-carrier operator-norm convergence is asserted. The risk and
early paired-activity bounds supplied by D.2 belong to this same target.
Convergence does not certify those bounds at a chosen finite order.

###### D.4. Finite numerical limits and whole-circle evaluation

Fix one represented law from D.1 with radius (H40.C1), rational endpoints
`-1<=a<=b<=1`, `-1<=c<=d<=1`, labels `+1,-1`, and component masses one
half. Its conditional coordinates are `u_1(rho s)` and `u_2(rho s)`,
where `u_2` is the quarter-turn of
`u_1(z)=((1-z^2)/(1+z^2),2z/(1+z^2))`. A degenerate interval is an
atom. Midpoints with `m` nodes per nondegenerate component give an exact
positive rational finite law `mu_m`; degenerate components use one node.
Its weights are `1/(2m)` or `1/2` and its normalized coordinates are
rational numbers with finite exact expressions. Both the target and
every exact midpoint rule are in `V_rho`, and D.1's transport estimate is

\[
 \mathcal W_1(\mu_m,\mu)
 \le\frac{\rho[(b-a)+(d-c)]}{4m}\le\frac\rho m.
 \tag{H40.N1}
\]

At order `N`, use part C's source regularization `epsilon>0`, initializer
cubature `Q`, independent population replay `P`, and rational arithmetic
precision `p`. Use the same Heun method with `J` steps of intended length
`h=40/J`. Between successive intended nodes interpolate the moving state
linearly and recompute the nonlinear fields. Denote the resulting
prediction by `fhat_{N,epsilon,Q,P,m,J,p}`. All adjustable resource
allowances are required to admit the requested finite operations; they
are not fixed caps on a refinement sequence.

The conclusion is

\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
 \lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}
 \lim_{p\to\infty}\mathfrak E=0,
 \tag{H40.N2}
\]

where `mathfrak E` is the sum of the prediction error in supremum norm
on `[0,40] x S1`, the two uniform-time paired `W2` errors, the two
uniform-time RMS errors, and the uniform-time risk error against the
reference of D.3. Each intermediate target exists in these metrics. Exact limiting
predictions are continuous; finite-precision rounded query evaluation
is required only to converge uniformly. The source-regularization limit is vacuous when the core initializer
does not use it. The law, radius, horizon, dictionary and ridge remain
fixed in their respective places in this iterated limit.

**Fixed-order mark and data limits.** The initialization proof in part C.2 is
unchanged: it concerns a fixed finite Gaussian graph before training,
whose bounded retained coordinates and formal derivatives have the
required polynomial Gaussian envelopes. At fixed positive `epsilon`,
every empirical source covariance prefix is its operand Gram plus
`epsilon I`; its positive pivots are retained. The Halton/Box–Muller
moment argument and finite coefficient induction give the `Q` limit.
Replay on `P` points evaluates the full joint mark tuple with all those
coefficients and factors frozen, so its joint laws, including lower
`g`, converge in `W2`. The two population indices are not paired.

After `Q -> infinity`, removal of `epsilon` uses continuity of positive
semidefinite covariance square roots and the same Gaussian envelopes for
the complete named source list. Singular limiting covariance is allowed;
no continuity of singular Cholesky factors or deletion of a zero-variance
named derivative is required. At fixed `N`, the feature ridge stays
positive. For every raw retained coordinate bound `B_l,j`,

\[
 |b_l|\le K_l:=\left(\sum_jB_{l,j}^2\right)^{1/2}/\sqrt{\eta_N}.
 \tag{H40.N3}
\]

This holds for empirical and exact Grams. Normalization and `D_N` are
continuous along the successive initializer limits, with common finite
matrix bounds. An independent replay need not reproduce the Gram used
for normalization or make its feature map a contraction. Only the
bounded-envelope estimate (H40.N3) is needed for the following inner
stability argument; the outer contraction argument uses the exact
initializer after all inner limits.

For general probability mark laws satisfying (H40.N3), `E|g|^2<infinity`
and finite `D`, the local characteristic construction of part C.3 applies to
exactly (H40.C6). Its weighted gradient calculation gives

\[
 \|c(t)\|_\infty\le2t,\quad |a|\le K_1,\quad |d|\le2K_2t,
 \quad\|M-D\|_F\le2K_1K_2t^2,
 \quad\|w'(t)\|_\infty\le4K_1K_2t\|M(t)\|_F.
 \tag{H40.N4}
\]

These bounds close existence in bounded `w-g,c,M` through 40 for each
fixed order, including atomic replay laws, without empirical contraction.
Couple two complete lower joint mark laws and two upper mark laws, and
write
`e=||w-wtilde||2+||c-ctilde||2+||M-Mtilde||F` and
`rho_b=||b_1-btilde_1||2+||b_2-btilde_2||2` on those couplings.
At a common input,
`|a-atilde|<=||b_1-btilde_1||2+K_1||w-wtilde||2`.
Subtract the three factors of `b_2^TMa`, then of `c h_2`, `b_2c phi'`
and `b_1^TM^Td`. Bounds (H40.N3)–(H40.N4) give `C(e+rho_b)` for all
field differences in their `L2` or finite Euclidean norms. In the lower
gate product the comparison query is pointwise bounded by
`K_1 K_2||Mtilde||F||ctilde||infty`, so it has the same bound.

For a data-law change the velocity integrand is Lipschitz into the
corresponding `L2`/Frobenius space. Indeed
`||phi(w·u)-phi(w·v)||2<=||w||2|u-v|`; its `a` integral inherits this
bound, upper fields and `q` inherit it through bounded finite features,
and the last lower gate costs
`2||w||2||q||infty|u-v|`. The explicit terminal `u` and label `y`
are Lipschitz as well. Integrating a data coupling with the Bochner
triangle inequality therefore costs `C W1(mu,mutilde)`, not its square
root. The scalar integrating factor yields

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 e(0)+CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)\}\right],
 \quad e(0)=\|g-\widetilde g\|_2+\|D-\widetilde D\|_F.
 \tag{H40.N5}
\]

The constant uses only common `K_l,||D||F,||g||2,T` bounds. Such bounds
hold along every fixed-order initializer/mark limit. At a reached restart,
replace `e(0)` by the discrepancy of the complete saved moving state.

Working weights need not sum exactly to one. For an exact ODE using
nonnegative finite measures write its two population measures as
`s_l lambda_l` and data measure as `s_d mu`, with normalized laws and
masses in `[1/2,2]`. The operational expressions contain the factors
`s_1` in `a`, `s_2` in `f,d`, and `s_d` outside each velocity; these
factors are retained. Its weighted energy identity gives
`L(0)<=s_d`, `int |r| d(s_d mu)<=s_d`, hence bounds of the form
(H40.N4) with enlarged constants. Product subtraction adds the mass
error `Delta_s=|s_1-stilde_1|+|s_2-stilde_2|+|s_d-stilde_d|`:

\[
 \sup_{t\le T}e(t)\le e^{CT}\left[
 e(0)+CT\{\rho_b+\mathcal W_1(\mu,\widetilde\mu)+\Delta_s\}\right].
 \tag{H40.N6}
\]

All `L2` distances here use the normalized coupling spaces. These
estimates also hold for input laws on the fixed neighborhood `|u|<=2`,
with enlarged constants, by replacing each unit input bound by two.
This covers directly rounded coordinates before the precision limit.
This is an estimate for exact ODEs with their literal finite measures,
not an energy or stability identity for a rounded Heun computation. In (H40.N2),
precision is removed first, so the normalized estimate (H40.N5) suffices
for the later ODE limits; (H40.N6) also accounts explicitly for mass
errors when comparing the finite measures before that limit.

For paired observations take the product of each same-layer joint mark
coupling and a data coupling, retaining initial and current values
together. The initial upper field uses the same `g,b_1,b_2,D` and lower
weights as the current calculation. The same-input `L2` field estimates
hold uniformly in time; initial errors add the corresponding `g,D,mark`
errors. Since the circle has diameter two,
`int |u-v|^2 dpi<=2 int |u-v| dpi`. Therefore

\[
 \sup_{t\le T}\mathcal W_2(\mathcal P_l(t),\widetilde{\mathcal P}_l(t))
 \le C\left[
 \sup_te(t)+\rho_b+e(0)+\Delta_s
                         +\mathcal W_1(\mu,\widetilde\mu)^{1/2}\right].
 \tag{H40.N7}
\]

Here pair laws use normalized product measures. On the rounded-input
neighborhood use `|u-v|^2<=4|u-v|`; only the constant changes. This
square-root term comes from squared transport cost; it does not weaken
the linear data term in the drift estimate. The reverse `L2` triangle inequality gives
the same convergence for RMS. With literal finite-measure weights,
`R_l,raw^2=s_l s_d R_l,normalized^2`. As the masses approach one these
have the same limit, including at zero displacement. The raw risk is
`s_d int(f-y)^2 dmu`; its difference is bounded by prediction error,
`C W1` for the fixed-state loss integrand and `C|s_d-stilde_d|`.
This proves the asserted paired/RMS/risk passages under each refinement.

**Time and arithmetic, including a compact query domain.** Fix
`N,epsilon,Q,P,m` and first use exact arithmetic. The finite ODE is
smooth. Its Heun stages remain bounded independently of `J`: with
`B_k=1+||c_k||infty`,

\[
 B_k^*\le(1+2h)B_k,\qquad
 B_{k+1}\le(1+2h+2h^2)B_k\le e^{(2+2T)h}B_k.
 \tag{H40.N8}
\]

Thus all stages have `1+||c||infty<=B_*=(1+2T)e^{(2+2T)T}`. Their
matrix velocity is at most `V_M=2B_*K_1K_2(B_*-1)`, and matrix
nodes/stages have norm at most `||D||F+2TV_M`; their row increments
are bounded by integrating
`2B_*K_1K_2(||D||F+2TV_M)(B_*-1)`. These finite bounds are valid at
`T=40` without a discrete energy inequality. On a slightly larger
bounded set the vector field is Lipschitz. The exact step and Heun step
each differ from Euler by `O(h^2)` there; the recurrence
`e_(k+1)<=(1+Ch)e_k+Ch^2` sums to `max e_k<=C_T h`.
Linear interpolation adds `O(h)`, proving the uniform-time mesh limit.

Now fix `J` also and let rational arithmetic precision `p` increase.
The finite initializer, fixed-pivot Cholesky operations and finite Heun
nodes converge by part C.4's locally consistent primitive algorithms and
finite-operation induction. Their exact positive source and feature
pivots supply eventual success margins at these fixed parameters. No
claim of a diagonal with unresolved shrinking pivots is made.

The data radius requires a further check. Its exponent `E=E_10` is a
fixed finite integer with an exact expression. The law rule may replace
the radius by zero when `E>4(p+8)+2`; then its coordinate displacement
is at most `2rho<10^(-p-8)`, and the bound and exact positive law are
retained. As `p->infinity` at fixed `E`, that branch eventually stops.
With adequate adjustable expression/scalar-bit and rule-node allowances,
the exact denominator `2^E` and each fixed midpoint coordinate can then
be formed. Their rational endpoints and positive weights are unchanged.
Direct coordinate and weight rounding tends to zero. More explicitly,
let `e_coord` be the largest coordinate `L1` rounding error and `e_weight`
the total absolute weight error. For total mass at least one half,
normalizing changes the weights from the exact rule by total variation
at most `2e_weight`. First couple masses on the exact rule nodes and
move the remainder over their data diameter at most four; then move each node to its rounded
coordinate. Thus the resulting transport error is
at most `e_coord+8e_weight`. Keep the separate mass defect in
(H40.N6) for the operational equations. A nonreference
exact midpoint may also round to an axis at some precisions; for a
fixed nonzero coordinate this likewise eventually stops. Exact axis
midpoints or a coarse midpoint rule that is itself the reference remain
valid quadrature cases. Neither type of numerical collapse redefines
the positive-radius target law.

At fixed array sizes, nearest `10^-p` weight rounding has total error
at most one half the number of weights times `10^-p`; all relevant
masses are eventually positive and tend to one. Normalizing returned
nonnegative weights only to interpret pair laws therefore changes them
by vanishing total variation. RMS and risk use the original weights;
their arithmetic outputs converge and the preceding mass calculation
identifies their limits. Rounded input coordinates lie in a common
compact neighborhood of the circle. Their squared-norm perturbation is
at most `4·10^-p`, inside the precision-dependent validation allowance;
repeated validation does not normalize the data or change its law.

Finiteness of the training program alone does not prove uniform
whole-circle arithmetic convergence. At fixed outer parameters and `J`,
take all finitely many adjacent exact endpoint pairs. For each pair the
exact interpolation/evaluation graph is a continuous function of
`(u,q) in S1 x [0,1]`, with `q` its interpolation fraction. Every
intermediate operand has compact image: start from these compact query
sets and sufficiently small closed bounded endpoint neighborhoods,
which are compact in these finite dimensions, and induct through the
finitely many continuous operations. Include the initial-field evaluation with
`g,D` in the same collection. All primitive domains requiring a
nonzero denominator retain a positive margin; tanh's implemented
denominator is at least one, and square-root consistency also holds at
zero. Part C.4's primitive error estimates are locally uniform on these
compact operand sets. Uniform continuity and induction through this
finite evaluation graph therefore give uniform convergence in `(u,q)`
and over the finitely many steps, even though the query domain is
uncountable.

Use directly rounded coordinates for each queried `u`; their Euclidean
error is at most `sqrt(2)10^-p/2`. Round `q` with error at most
`10^-p/2`. These arguments stay in the preceding compact neighborhoods,
so the same induction includes query rounding and interpolation.
The intended step `40/J` and its represented value differ by at most
`10^-p/2`, and the final represented time differs by at most
`J10^-p/2`. This error vanishes in the precision-first limit.
Equivalently define the output on the intended mesh by its interpolated
states; both conventions have that same limit. A finite output panel
is not used to infer a circle supremum.

After arithmetic and mesh limits, (H40.N1),(H40.N5) remove input
quadrature, followed by the `P`, `Q` and source-regularization limits
whose hypotheses were verified above. Their forward and paired bounds
give the observation convergence at every stage. The resulting exact
order is exactly (H40.C5)–(H40.C6); D.3 proves its outer `N` limit and
identifies the result with actual finite-network GF, retaining its
random finite initial readout. This proves (H40.N2).

At a numerical step endpoint the saved complete joint marks, weights,
`g,w,c,M,D`, finite law and arithmetic/step metadata determine every
following Heun step. Exact serialization therefore gives own-state
restart with no source tape or training history. The limiting population
restart follows from the characteristic uniqueness and (H40.N5) with
saved-state error in `e(0)`. A new Heun mesh from an interpolated interior
time need not reproduce the old finite mesh. These conclusions provide
qualitative iterated convergence on the fixed explicit family and horizon;
they assert no arbitrary diagonal, tolerance-to-resolution procedure,
useful conditioning, finite-run accuracy certificate, or simultaneous
closure-order/width rate.

###### D.5. Executable representation, storage and bounded validation

The library `pde.observable_laws` implements (H40.F1)–(H40.F3).
`supported_radius()` builds the fixed eleven-node integer expression;
`supported_law(a=...,b=...,c=...,d=...)` retains exact rational endpoints
and the fixed radius. The positive-integer expression operations are literal,
addition, multiplication and power of two. No scientific scope is inferred
from a floating coordinate or from a user-supplied tag. The time-40 validation
worker checks the saved radius against the canonical constructor before using
its supported-family tag. The separate positive rational-radius constructor
uses the same equations with explicitly exploratory scope.

For `m` midpoint nodes per nondegenerate conditional interval, a node has
parameter `a+(b-a)(2k+1)/(2m)` and mass `1/(2m)`. A degenerate interval has
one node of mass `1/2`. The exact conditional law and every midpoint rule
belong to the supported domain. The conditional mean distance from a uniform
parameter to its midpoint is its interval length divided by `4m`.
The Lipschitz constant `2rho` in (H40.F3), followed by the two half masses,
therefore gives

\[
 W_1(\mu_m,\mu)\le {\rho[(b-a)+(d-c)]\over4m}
 \le {\rho\over m}.                                      \tag{H40.I1}
\]

For fixed `m`, the exact midpoint coordinates are rational. This is an actual
finite integration rule for the nonatomic law, independent of population
integration. It does not replace that law by an unspecified sampling oracle.

The law description remains exact even when a finite realization deliberately
uses the reference directions. At decimal precision `p`, the implementation
may use radius zero if `E10>4(p+8)+2`; for float64 it takes `p=17` for this
decision. Comparison with the integer expression stops once an intermediate
value exceeds the finite cutoff and does not expand the tower. In this branch
`rho<2^[-4(p+8)-2]`, so each coordinate-vector replacement is at most `2rho`,
which is below `10^(-p-8)` because `2^4>10`. The exact descriptor, reason for
replacement and transport contribution are saved. This is a stated
approximation; tiny nonzero floating coordinates need not automatically round
to zero. A second flag identifies complete collapse caused by coordinate
rounding after exact coordinate construction.

More precisely, the replacement contributes at most
`rho[max(|a|,|b|)+max(|c|,|d|)]` to the normalized-direction transport cost.
The midpoint and replacement costs add. The implementation also records the
largest actual coordinate rounding error in L1 and the total weight rounding
error, as exact rationals computed from the retained working scalars.
Normalization only for the probability-law interpretation adds at most the
coordinate error plus eight times the weight error; the operational weights
remain literal. The mass and arithmetic arguments in D.4 account for them.

For every fixed law, `E10` is a fixed finite integer. As precision tends to
infinity, the deliberate replacement branch eventually ceases. With adequate
finite resource allowances the denominator can then be formed, the exact
rational rule evaluated, and all its coordinates rounded consistently. If
the caller's allowance is insufficient, the implementation rejects the request
instead of silently changing the radius or deleting nodes. The asymptotic
numerical theorem permits resource ceilings to increase to admit each fixed
finite computation; the default software ceilings are not mathematical
restrictions on the family or on the hierarchy. Resolving this radius at its
own scale is not a practical promise or a requirement of the operational
witnesses below.

Here is the full fixed-resolution storage and work contract. Let `P1,P2`
be the retained joint population sizes, `d1,d2` the dictionary dimensions,
`A` the data-node count, `B<=A` an input block size, and `J` the time-step
count through 40. The saved dynamic state is `w,c,M`; fixed retained data are
`b1,g,p1,b2,p2,D`, the law rule, the exact law description and the arithmetic
and integrator metadata. Its numerical scalar count is

\[
 S=P_1(d_1+5)+P_2(d_2+2)+2d_1d_2,\qquad
 S_{\rm data}=4A.                                         \tag{H40.I2}
\]

The two matrices are feature coefficient matrices of size `d2 by d1`.
There is no raw neuron-by-neuron middle matrix. `D` stores one initialized
action contraction; both training directions use `M` and `M^T`. The generic
initialized-word compiler finishes before evolution and its source transcript
is discarded. Evolution never asks for an arbitrary initialized action.

One RHS evaluation uses

\[
 O\!\left(A[P_1d_1+P_2d_2+P_1+P_2+d_1d_2]+S+A\right)
                                                              \tag{H40.I3}
\]

scalar operations, including validation and array handling. Input blocking
requires `O((P1+P2)B+(d1+d2)B+d1d2)` temporary scalar slots. Heun requires
two evaluations and a constant number of state/dynamic arrays; retaining
adjacent nodes for interpolation does not change this order. The total
evolution work is `J` times (H40.I3), and stage storage is `O(S+A)` plus the
displayed block workspace. A step counter and mesh metadata use `O(log(J+1))`
bits and can be bounded at the start of the run. No list indexed by elapsed
steps is retained.

The initializer has its own finite cost, before this runtime. For the tanh
polynomial core, writing `d=d1+d2`, direct Chebyshev tables and contractions
cost

\[
 O\big((Q+P)(N+1)d+Qd^2+(d_1^3+d_2^3)+Pd^2\big)          \tag{H40.I4}
\]

scalar operations, with table and square-matrix storage
`O((Q+P)((N+1)+d)+d²)`. Here `P=P1=P2` for the supplied initializer;
`Q` is the separate coefficient/Gram integration size. The generic branch
has a finite DAG with `G` nodes and `s` named sources. Its stored joint
tables/factors use `O((Q+P)(G+s+d)+s²+d²)` scalars. A direct bound for its
source differentiation, covariance, replay and normalization work is

\[
 O\big(Q[s(G+s^2)+s^2+d^2]+P(G+s^2)+d^3+Pd^2\big).      \tag{H40.I5}
\]

These costs depend on the finite dictionary and source union, including both
orientations, not on elapsed training time. Syntax/scalar resource checks
precede allocations and reject a request without substituting another
dictionary. The source regularizer is unused on the optimized core branch;
the complete generic path retains every named direction with its positive
regularizer until the stated limit removes it.

Scalar counts are not bit or wall-time bounds. In the rational backend a
retained scalar has `p` decimal places and integer units, requiring
`O(p+log(1+M_*))` bits for a finite magnitude bound `M_*` on the requested
computation. The scale `10^p` and Python integer/object storage are included
in the measured per-entry count. Basic integer/rational operation costs and
the finite rational elementary series multiply the scalar-operation work;
their temporary Fraction numerators/denominators also require storage.
C.4.7.10.C.4 gives the finite elementary construction and its convergence.
On each fixed bounded operand set its series need `O(p)` terms and may use
`O(p² log p)` temporary bits, with constants depending on that set. The
finite-horizon stage bounds of D.4 provide such a set at every fixed outer
resolution. No uniform affordable bound in order or accuracy is inferred.

If the total endpoint-description length is `b` bits, the symbolic law costs
`O(b+1)` bits plus its fixed expression tree. The collapsed branch compares
that tree with a number of bit length `O(log(p+1))`. On the resolved branch
the radius denominator alone costs `E10+1` bits. Exact midpoint coordinate
arithmetic has bit sizes bounded by a fixed multiple of
`E10+b+log(m+1)`; a deliberately loose factor sixteen is checked by the law
implementation before construction. Its finite rational arithmetic and the
storage of the `A` resulting coordinates must be added to (H40.I2)–(H40.I5).
Exact description bytes and actual rounding/collapse information accompany
the saved data. This accounts for an enormous represented law rather than
hiding its expansion cost in a real-number oracle.

At one requested time, the full initial/current pair arrays require
`2(P1+P2)A` scalars; their product weights and inputs require `O(P1+P2+A)`.
Prediction panels, exact observation serialization, and checkpoint strings
have additional finite output/transient costs. They need not be retained for
evolution. The bounded validation uses six fixed output times, independent
of the mesh, and never feeds their outputs into a later state. Its byte and
peak-RSS records distinguish state payloads, structural stage allowances,
serialized metadata, output files, elementary temporaries and process overhead.

The maintained worker `validate_observable_horizon.py` starts every declared
configuration from its prescribed Gaussian initializer and evolves through all
of its own steps to 40. At 20 it serializes its current joint state and law;
loading that state and repeating the remaining identical steps must reproduce
all retained arrays, metadata and final prediction exactly at the same backend
and reduction environment. No intermediate population state is imported, and
no approximation error is reset. Off-mesh observations use only adjacent
computed states and the affine interpolation convention, then evolution
continues from the actual right node.

The fixed bounded plan in `code/validation/observable_horizon_plan.json`
uses genuinely enriched orders `1,3,5`, whose dimensions and nonzero added
initialized-action information were proved in C.4.7.10.B. It includes supported
nonorthogonal atomic and nonatomic law descriptions, separate time,
initialization, population and input-integration refinements, rational
precision comparisons, and resolved exploratory arcs. Resource limits and
failure records are enforced by the shared supervisor; its optional worker
selection preserves the original H3 default. The analysis recomputes loss and
paired RMS from saved observations and reports all comparable declared pairs.
These finite panels and fixed observation times are diagnostics, not numerical
proofs of time-uniform or full-circle accuracy. Supported perturbations that
collapse at the declared precisions are explicitly labelled, so those runs
demonstrate operation at their resolution, not resolved perturbed-law behavior.

The full generation, independent reproduction and analysis commands are in
`code/README.md`. Their operational evidence is separate from D.1–D.4's
qualitative mathematical result and the inherited target learning bounds.
