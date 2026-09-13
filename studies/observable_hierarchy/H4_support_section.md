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
