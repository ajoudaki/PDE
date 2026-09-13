# C-H4 family route: an explicit supported domain through time 40

Author: scoped agent `/root/h4_route_family`. Date: 2026-09-13.
Status: candidate proof, frozen for comparison after completion. This is a
new quantitative route; the earlier frozen `H4_route_family.md` is preserved.
No promotion, numerical training experiment, implementation change, or Git
write is claimed.

## 1. Statement and relation to the established domain

For the two-hidden-layer tanh model, initialization, loss, mobilities, raw
spaces, and canonical Gaussian action of C.4.7.1, there is an explicitly
represented positive number \(r\), defined in (E30), with the following
property. Put

\[
\mathcal V_r=\left\{\mu:
 \mu(y=+1)=\mu(y=-1)=\tfrac12,\quad
 |x/\sqrt2-e_1|\le2r\ \text{on }\{y=+1\},\quad
 |x/\sqrt2-e_2|\le2r\ \text{on }\{y=-1\}\right\},
\tag{E1}
\]

where support conditions mean almost surely and every input lies on
\(\sqrt2S^1\). For every \(\mu\in\mathcal V_r\), the C.4.7.4–5 construction
and finite-width identification apply on physical time \([0,40]\).
In particular they give a strong autonomous population flow, reached-state
uniqueness, the stated joint same-layer paired observation limits, and
actual finite-GF capture. Its population risk at time 40 is at most \(1/4\),
and its two training-averaged paired squared hidden displacements at time
\(1/200\) are each at least \(10^{-13}\).

This proves an **explicit supported domain** for that construction. It does
not compare \(r\) with an arbitrarily selected, unnamed radius of the original
open Wasserstein neighborhood \(U_1\). The proof below replaces its small-law
bootstrap by a quantified uniform-support bootstrap and then checks every
assumption needed by the same completion and observation arguments. On the
intersection with \(U_1\), reached-state uniqueness identifies the two flows.
No response-in-contamination statement from C.4.7.6 is asserted here.

The exact finite-description subfamily in §7 includes nonorthogonal atomic
laws and nonatomic laws. Its domain is fixed before approximation order or
accuracy is selected. All new constants are given by finitely many arithmetic
operations and exponentials. The reference mesh threshold \(h_* >0\) is used
only for eventual convergence, as permitted by the assignment; this report
does not claim a computable mesh stopping threshold or a width rate.

## 2. Explicit constants and the reference cap

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
\tag{E2}
\]

These are N9, N38–N47, and the conclusion of the raw-reference transfer.
They use \(10\) as a permissible initialized action-norm bound. The actual
canonical action has the stronger established bound two. For all raw Euler
programs, independently of a source cap,

\[
\|c\|_\infty\le C,\quad |r_a|\le R,\quad
\|A\|_{\rm op}\le M,\quad \|w\|_2\le W.
\tag{E3}
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
\tag{E4}
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
\tag{E5}
\]

The bound for a current upper row needs only the already constructed lower
rows: it does not assume the current unknown backward cap. This causal
order is retained throughout the proof.

All constants in this report are scalar positive real numbers. The letters
\(R\) and \(d_0\) in (E2),(E4) denote respectively the residual bound and
the upper-row factor; they are not the raw comparison cutoff or the
C.4.5 numerical error tolerance.

## 3. Quantified source comparison under uniformly small input changes

Consider a finite law with positive weights \(p_a\), labels \(y_a\in\{+1,-1\}\)
of total mass one half each, and normalized inputs \(u_a\). Its split
reference has the same names, weights and labels, with \(v_a=e_1\) for
label \(+1\) and \(v_a=e_2\) for label \(-1\). Suppose

\[
\max_a|u_a-v_a|\le\varepsilon.
\tag{E6}
\]

Run both programs on the same mesh and common canonical source carrier,
as in N20–N21. For a past source \(p=(s,b)\), let \(m_p=h_sp_b\).
Take \(\eta\) to bound their raw sum distance at every node of the prefix,
and suppose

\[
\delta=\eta+\varepsilon\le1,
\qquad I=\delta^{1/16}.
\tag{E7}
\]

Their selected source coefficients are deterministic, and named derivatives
freeze them, the residuals and the covariance laws, exactly as in N4–N8.
For each \(k\), define \(E_k\) as the supremum of the backward-row difference
over **all pairs of passive outputs** \((u,v)\) with \(|u-v|\le\varepsilon\).
Past source names are matched and the distinguished current source is matched.
This includes every paired active output and the identical pair \((u,u)\).
There is no comparison of a distant contaminant against an axis: every
training input obeys (E6).

### 3.1 Field and gate constants

Set

\[
\begin{gathered}
h_1=1+W,\quad z_2=1+Mh_1,\quad
a_2=1+2Cz_2,\quad q_2=Ma_2+C,\quad r_2=1+Cz_2,\\
G=1+24h_1+q_2(1+2Q_{24})+r_2,\\
J=2Tr_2C^2+4RTC a_2,\qquad F_2=2r_2+4Rh_1.
\end{gathered}
\tag{E8}
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
\tag{E9}
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
\tag{E10}
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
\tag{E11}
\]

The learned part contributes at most
\(2Tr_2C^2\delta+4RTC a_2\delta\): use
\(|\mathrm d\gamma_p|\le2m_pr_2\delta\), both backward fields bounded by
\(C\), and sum \(m_p\le T\). Because (E6) is uniform, no past-source
density estimate is needed to average an input-transport error.

### 3.2 Lower pulse difference

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
\tag{E12}
\]

For every past backward pulse \(p\), subtraction of N7 yields

\[
\frac{\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2}{m_p}
\le C_v\left(I+\sum_{j<k}h_jE_j\right).
\tag{E13}
\]

Here is a termwise verification of its constant. Put all differences of
the evolving pulse itself into the unbarred propagation. For its coordinate
maximum the propagation coefficient at step \(j\) is at most

\[
2Rh_j\left(D+2\sum_ap_a|Q_{ja}|\right).
\tag{E14}
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
\tag{E15}
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
\tag{E16}
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
\tag{E17}
\]

The direct learned term in \(F\) differs by at most \(m_pF_2\delta\):
its residual difference costs \(2m_pr_2\delta\), and its two first-feature
contraction differences cost \(4Rm_ph_1\delta\). Hence

\[
|F_{ku,p}-\bar F_{kv,p}|\le m_pF_\Delta G_k.
\tag{E18}
\]

### 3.3 Upper row difference

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
\tag{E19}
\]

Then, whenever all previous nearby-law rows have cap \(B\),

\[
E_k\le C_{\mathrm{src}}\left(I+\sum_{j<k}h_jE_j\right).
\tag{E20}
\]

To verify this, let \(\mathcal U_k\) and \(\mathcal V_k\) be respectively
the suprema over paired outputs of
\(\|\sum_p|\mathrm dU_{ku;p}|\|_2\) and
\(\|\sum_p|\mathrm dV_{ku;p}|\|_2\). Let \(\mathcal C_k\) be the analogous
readout derivative row norm. The direct current impulses cancel. N29,
(E5), and (E18) give

\[
\mathcal U_k\le A_U G_k+f\sum_{j<k}h_j\mathcal V_j.
\tag{E21}
\]

For the readout derivative, its changed residual coefficient contributes
\(2Tr_2U_0\delta\), its changed gate contributes
\(4RTz_2U_0\delta\), and its changed U row propagates with coefficient
\(2R\). Thus

\[
\mathcal C_k\le A_C I+2R\sum_{j<k}h_j\mathcal U_j.
\tag{E22}
\]

For the upper backward field, the changed outside \(\phi'\) gate costs
\(4RTU_0z_2\delta\); the changed readout and outside \(\phi''\) gate cost
\((2+6Cz_2)U_0\delta\). The remaining differences are the C row itself
and \(c\phi''\) times the U row. Therefore

\[
\mathcal V_k\le\mathcal C_k+2C\mathcal U_k+A_V I.
\tag{E23}
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
\tag{E24}
\]

This is the needed explicit specialization of N24/N31. It does not use the
unquantified constants in those displays.

## 4. Explicit raw comparison with one fixed cutoff

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
\tag{E25}
\]

For a raw sum distance \(d\), law distance \(q\), and cutoff \(R_c\ge1\),
these constants give

\[
\|\mathcal F_\lambda(\theta)-\mathcal F_{\nu_*}(\bar\theta)\|_{(1)}
\le C_{\mathrm{raw}}\left((1+R_c)(d+q)+
 \tau_{R_c}(\bar c)+\int\tau_{R_c}(\bar Q)\,d\nu_*\right).
\tag{E26}
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
\tag{E27}
\]

N10 writes each reference \(Q=G+J\), with Gaussian variance at most
\(C^2\) and \(|J|\le D_*\). For \(R_c\ge2D_*\), its tail obeys

\[
\tau_{R_c}(Q)\le H e^{-R_c^2/S}.
\tag{E28}
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
\tag{E29}
\]

To see this directly, apply the triangle inequality to the two updates and
iterate the scalar recurrence with multiplier
\(1+h_kC_{\mathrm{raw}}(1+R_c)\); the product is at most
\(e^{\Gamma(1+R_c)}\), and the total forcing time is at most \(T\).
Both programs start identically. Their crude raw bounds (E3) suffice, so
this argument imposes no source cap on the nearby-law program. There is
no mesh-error floor in (E29).

## 5. Explicit radius and closure of the cap

The promised exact constants are

\[
\begin{gathered}
Z=16\{4+(T+1)C_{\mathrm{src}}\},\qquad z=e^{-Z},\\
A=1+\Gamma+H+Z,\qquad R_c=4SA,\qquad X=\Gamma(1+R_c),\\
\boxed{\displaystyle r=\exp\{-Z-4-2X-e^{3000}\}.}
\end{gathered}
\tag{E30}
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
\tag{E31}
\]

Here \(Xe^{-X}\le1\), and \(2e^{-4}<1/4\).
For the tail term it suffices to show
\(\log(4\Gamma H)+X+Z<R_c^2/S\). Since \(\Gamma,H\ge1\),
\(\log\Gamma\le\Gamma\), \(\log H\le H\), and \(\log4<2\),

\[
\log(4\Gamma H)+X+Z
<2+2\Gamma+H+Z+\Gamma R_c
\le2A+4SA^2\le6SA^2<16SA^2=R_c^2/S.
\tag{E32}
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
\tag{E33}
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

## 6. Completion, actual finite GF, and the risk/activity thresholds

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
applies to actual finite GF with zero discretization defect. Its verified
constants, margins, and complete source proof were read in the first route;
the same established input is retained here. In particular the reference
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

## 7. A fixed explicit family and law integration

For the fixed \(r\) in (E30), use

\[
u_1(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),\quad
u_2(t)=\left(-\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\right).
\tag{E34}
\]

For rational \(b\in[1/2,1]\), set \(a=br\) and define

\[
A_b=\tfrac12\delta_{(\sqrt2u_1(0),+1)}+
     \tfrac12\delta_{(\sqrt2u_2(a),-1)},
\]
\[
N_b=\tfrac12\operatorname{Law}(\sqrt2u_1(aZ_0),+1)+
     \tfrac12\operatorname{Law}(\sqrt2u_2(aZ_0),-1),
\quad Z_0\sim\operatorname{Unif}[-1,1],
\]
\[
\mu_{b,\alpha}=(1-\alpha)A_b+\alpha N_b,
\quad \alpha\in\mathbb Q\cap[0,1].
\tag{E35}
\]

Their descriptions are finite expression trees with the fixed radius tag
(E30) and two ordinary rational parameters. Norm one follows from
\((1-t^2)^2+4t^2=(1+t^2)^2\). Also

\[
|u_i(t)-e_i|=2|t|/\sqrt{1+t^2}\le2|t|,
\quad |u_i'(t)|=2/(1+t^2)\le2.
\tag{E36}
\]

Thus every law in (E35) lies in \(\mathcal V_r\), and its reference
Wasserstein distance is at most \(a\le r\): for \(A_b\), only its second
half-mass moves; for \(N_b\), use \(\mathbb E|Z_0|=1/2\).
Its atomic member has the strictly nonzero Gram entry
\(-2a/(1+a^2)\). The parametrizations are injective on \([-a,a]\), so
\(N_b\) is nonatomic. Cross-cluster inner products are
\(2(s-t)(1+st)/[(1+s^2)(1+t^2)]\), and vanish only when \(s=t\) in
this interval, a null subset of the parameter square.

For an integrand \(G\), the exact law integral is

\[
\begin{split}
\int G\,d\mu_{b,\alpha}
={}&\frac{1-\alpha}{2}
 [G(\sqrt2u_1(0),+1)+G(\sqrt2u_2(a),-1)]\\
&+\frac\alpha4\sum_{i=1}^2
 \int_{-1}^1G(\sqrt2u_i(az),y_i)\,dz,
\quad(y_1,y_2)=(+1,-1).
\end{split}
\tag{E37}
\]

For \(m=2^j\), use midpoint parameters
\(z_{j,k}=-1+(2k+1)/m\), and replace the nonatomic part by the exact finite law

\[
N_{b,j}=\frac1{2m}\sum_{i=1}^2\sum_{k=0}^{m-1}
 \delta_{(\sqrt2u_i(az_{j,k}),y_i)}.
\tag{E38}
\]

Weights are rational; atom locations are exact finite elementary expressions
in the fixed explicitly represented radius and rational inputs. They are
computable real coordinates, not claimed to be rational coordinates.
All finite laws remain in \(\mathcal V_r\). Transporting each parameter cell
to its midpoint gives

\[
\mathcal W_1\bigl(\mu_{b,\alpha},
 (1-\alpha)A_b+\alpha N_{b,j}\bigr)\le\alpha a/2^j.
\tag{E39}
\]

The conditional mean parameter error is \(1/(2m)\), and (E36) multiplies
it by at most \(2a\), proving the bound. For an \(L_G\)-Lipschitz integrand
the integration error is at most \(L_G\alpha a/2^j\); for a supplied
effective continuity modulus \(\omega_G\), it is at most
\(\omega_G(2a/2^j)\). This is an executable law-integration refinement rule.
It does not purport to supply a separate algorithm for population Gaussian
contractions. The approximation index changes the finite comparison law,
not the target family or its radius.

## 8. Exact representation and evaluation of enormous constants

Store the definitions as a directed acyclic arithmetic expression graph;
do not expand the decimal digits of every exponential. Every leaf is an
explicit integer and every node is one of addition, subtraction,
multiplication, reciprocal of a proved positive quantity, or exponential.
The graph defines a computable real with a finite exact description.
Membership and positivity use the symbolic inequalities (E31)–(E36), so
neither floating-point underflow nor cancellation decides them.

For clarity, writing \(r=e^{-\Lambda}\), (E30) explicitly supplies
\(\Lambda=Z+4+2X+e^{3000}>0\). To enclose \(r\) with absolute error
\(2^{-p}\), a certified lower bound \(\Lambda>p+1\) permits the enclosure
\([0,2^{-p}]\), since \(e>2\). This is a legitimate underflow branch.
For a general finite precision request, refine rational interval bounds for
\(\Lambda\) until either its lower bound exceeds \(p+1\), or its upper
bound is below \(p+2\). These two open conditions cover the real line, so
one occurs after finitely many refinements. In the second branch the
exponent has an explicit finite bound; interval exponential evaluation then
gives the requested enclosure. Positive-expression comparisons can stop
recursively as soon as a lower bound exceeds the current threshold, without
materializing the full value of a large intermediate exponential.

The graph may denote numbers whose explicit expansions require an
astronomical finite resource. No useful computational cost is claimed.
The formula is nevertheless operationally different from an unnamed
existential radius: all inputs, operations, positivity facts and stopping
alternatives for absolute evaluation are specified. Finite-law quadrature
inherits computability of these coordinates and the supplied integrand.
Ordinary floating point will represent the perturbation as zero, and must
not be used to infer that its actual Gram entry vanishes.

## 9. Provenance, actual checks, and limitations

Allowed scientific inputs for this new route were the agent's own frozen
first report and its original established sources. No other route, study
history, task history or new scientific source was retrieved. The complete
original read coverage is recorded in `H4_route_family.md`: full
`docs/NOTATION.md`; C.4.7.1–5 and .7; complete C.4.5 statement and proof
units .1–3. The minor earlier endpoint exposure of the C.4.6 introductory
paragraph remains disclosed there; it was not used here.

The source hashes were rechecked before this new proof and were unchanged:

| Source | SHA-256 |
|---|---|
| `docs/global_nonlinear.md` | `77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

Required skills and applicable references remain those completely read for
the first route. HEAD at the metadata-only startup check was
`e32496236aefb04985f00dcf7f421f19043dda22`; the shared index had no staged
paths. The parent remains sole Git writer.

Checks performed here are symbolic/manual: each lower-pulse forcing term,
its source-mass normalization and Hölder exponents; the random integrating
factor; the upper row recursion; the HS raw comparison constants; the
Gaussian cutoff bound; both radius inequalities; the causal first-failure
induction; closure of the supported family under finite approximation; and
the exact law descriptions and quadrature error. No numerical experiment or
independent review has yet checked this candidate. The proof uses the
established source calculus and reference raw cap, whose complete relevant
specializations were read; it is not a new audit of all III.F dependencies.

The result supplies a fixed nontrivial, explicitly represented family in a
proved time-40 domain with the required risk and activity thresholds. It
does not show a useful-size perturbation regime, any advantage over frozen
features, an all-time changed-law flow, finite-width rates, an explicit mesh
stopping rate, or the separate C-H4 hierarchy compression theorem.
