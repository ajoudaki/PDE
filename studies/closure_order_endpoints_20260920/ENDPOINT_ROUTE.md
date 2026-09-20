# Endpoint route: small opposite labels in the exact canonical hierarchy

Status: frozen independent-route candidate; complete analytical derivation,
self-checked, not independently reviewed or promoted. No training computation
was performed. Date: 2026-09-20.

## Scope and source record

The assigned target is comparison of fitted whole-circle endpoints as the
canonical closure order increases, retaining its actual ridge and physical
metric. This route uses only the supervisor-authorized established sources:

- `docs/NOTATION.md`;
- `docs/global_nonlinear.md`, C.4.5 statement and C.4.5.1–2 in full;
- C.4.7.9 in full, C.4.7.10.B and C.1 through (H3.N6), and D.3 in full;
- the introductory/roadmap framing and navigation in `docs/README.md`.

Required process inputs were the rigorous-math and investigate-conjectures
skills, their research-contract/adversarial-audit references, and workflow
Part 1. No other study or route was read. The broader C.4.5.3 raw-GD transfer
is not a premise. This candidate makes no new finite-width endpoint assertion.
The assigned scope replaces author startup/study-history reading.

Source snapshot: HEAD `8a15e0f196ed31af54160c651bdfbf2f109eecf7`.
SHA256 of `docs/NOTATION.md`:
`199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
SHA256 of `docs/global_nonlinear.md`:
`81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
Tracked status was clean before the owned-file edit. No Git index mutation.

## Result and limits

For every fixed amplitude

\[
0<\alpha\le10^{-3},\qquad
\mu_\alpha=\tfrac12\delta_{(\sqrt2e_1,\alpha)}
             +\tfrac12\delta_{(\sqrt2e_2,-\alpha)},                 \tag{1}
\]

use the exact canonical dictionary, ridge
\(\eta_p=[1024(p+1)^2]^{-1}\), exact Gaussian contractions, population
laws, and equations (H40.C5)–(H40.C6). There exists an integer \(p_0\),
independent of \(\alpha\), such that every \(p\ge p_0\) has a fitted
endpoint \(f_{p,\alpha}^{\infty}\in C(S^1)\). The canonical population
GF for (1) has an explicit feature-orbit endpoint \(f_\alpha^\infty\),
and

\[
\lim_{p\to\infty}\sup_{t\ge0}\sup_{u\in S^1}
 |f_{p,\alpha}(t,u)-f_\alpha(t,u)|=0,
\qquad
\lim_{p\to\infty}\|f_{p,\alpha}^\infty-f_\alpha^\infty\|_\infty=0.
                                                                    \tag{2}
\]

Thus endpoints at orders \(p,q\to\infty\) are Cauchy in the whole-circle
supremum norm. There is no monotonicity assertion for successive orders,
no rate in \(p\), and no assertion about the finitely many \(p<p_0\).
The constant \(p_0\) is justified by strong convergence, not numerically
evaluated. The target is the full nonlinear canonical GF with its initialized
Gaussian action and actual adjoint. No symmetric finite dictionary, modified
ridge, frozen hidden block, action-norm convergence, or assumed all-order
coercivity is used.

The family has orthogonal training directions and small labels. It is not an
open law family around the unit-label reference, and this theorem does not
settle the unit-label reference endpoint. At each fixed nonzero amplitude,
both hidden layers and all three trainable blocks move. The quantitative
motion tends to zero as \(\alpha\downarrow0\); this is not a uniform
nonlazy statement in that amplitude limit.

The proof has three steps. The original feature orbit constructs the exact
small-label target. An eventual initial readout-Gram bound and a gradient
length estimate trap all sufficiently large closures in one fitting ball.
The established compact-source comparison then applies on every finite
physical horizon; the new uniform tail bound upgrades it to (2).

## 1. Exact small-label canonical GF

Use \(u=x/\sqrt2\), \(\phi=\tanh\), and the canonical spaces
\(H_\ell=L^2(\Omega_\ell)\). The C.4.5.1 feature orbit starts from
\((w,K,c)=(g,0,0)\), where \(g\sim N(0,I_2)\), and uses
\(A=A_0+K\), \(\|A_0\|\le2\). In the notation of that section,

\[
h=\tfrac12(H^2_1-H^2_2),\quad b=\langle c,h\rangle,
\quad c_s=h,\quad (w,K)_s=J^*c.                              \tag{3}
\]

This is a globally defined unique feature orbit with the full action and
its actual adjoint. Its canonical-law symmetry gives \(f_1=b=-f_2\).
The proved identities are

\[
b_s=\|\theta_s\|_{\rm raw}^2\ge m\ge1/10,
\quad \|\theta(s_2)-\theta(s_1)\|_{\rm raw}
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))},                       \tag{4}
\]

where the raw metric is row \(L^2\), learned-middle HS, and readout
\(L^2\). Also \(\|c(s)\|_\infty\le s\) and \(\|h(s)\|_2\le1\),
so \(0\le b(s)\le s\) before the unit level.

There is a unique \(s_\alpha\) with \(b(s_\alpha)=\alpha\), and

\[
\alpha\le s_\alpha\le10\alpha\le10^{-2}.                    \tag{5}
\]

Define \(t(s)=\int_0^s[2(\alpha-b(v))]^{-1}dv\) for
\(s<s_\alpha\). Its integrand is positive; boundedness of the continuous
\(b_s\) on \([0,s_\alpha]\) implies
\(\alpha-b(s)\le C(s_\alpha-s)\), so \(t(s)\to\infty\).
Its inverse satisfies

\[
s_\alpha'(t)=2(\alpha-b(s_\alpha(t))),\quad s_\alpha(0)=0.    \tag{6}
\]

Here \(s_\alpha(t)\) denotes the time-dependent clock and
\(s_\alpha\) without argument its terminal value. Substitution of the
two residuals \((b-\alpha,\alpha-b)\) into the probability-weighted
unhalved-loss GF proves that (3) under (6) is exactly that physical GF.
The population readout starts at zero as prescribed by the small-readout
limit. This does not alter finite-network initialization.

Writing \(e_\alpha(t)=\alpha-b(s_\alpha(t))\), (4) gives

\[
0<e_\alpha(t)\le\alpha e^{-t/5},\qquad
\|\theta_\alpha(t)-\theta_\alpha^\infty\|_{\rm raw}
 \le\sqrt{10}\,\alpha e^{-t/5},\qquad
\|\theta_\alpha(t)-\theta(0)\|_{\rm raw}\le\sqrt{10}\alpha.
                                                                    \tag{7}
\]

The target endpoint is (3) stopped at its first level \(b=\alpha\),
evaluated on the whole circle. It fits (1). On its state ball the scalar
prediction gradient has raw norm at most
\(\sqrt{1+\|c\|_2^2(1+\|A\|^2)}<2\). Integration on a segment between
two states therefore yields

\[
\|f_\alpha(t)-f_\alpha^\infty\|_\infty
 \le2\sqrt{10}\,\alpha e^{-t/5}<7\alpha e^{-t/5}.             \tag{8}
\]

Uniqueness within the canonical strong raw class also follows from the
one-reference cutoff comparison detailed below with zero source error.
Thus (3) is not a different optimizer or merely a formal symmetric branch.

## 2. Eventual coercivity proved for the canonical closures

Let \(U_{\ell,p}a=b_{\ell,p}^Ta\),
\(Q_{\ell,p}=U_{\ell,p}U_{\ell,p}^*\), and

\[
B_p=Q_{2,p}A_0Q_{1,p},\qquad
A_p=U_{2,p}M_pU_{1,p}^*=B_p+K_p,
\quad K_p=U_{2,p}(M_p-D_p)U_{1,p}^*.                         \tag{9}
\]

The exact ridge proof supplies \(\|U_{\ell,p}\|\le1\),
\(\|B_p\|\le2\), and strong convergence of \(B_p,B_p^*\) to
\(A_0,A_0^*\) on the initialized observable spaces. It also supplies
global existence at each fixed \(p\) for every bounded-label data law.
Only the convergence theorem there was restricted in time/law; the
fixed-order existence proof was not.

Define the initialized training readout Gram by

\[
G_p^0[a,b]=\langle\phi(B_p\phi(g_a)),
                         \phi(B_p\phi(g_b))\rangle,
\qquad a,b\in\{1,2\}.                                     \tag{10}
\]

Strong action convergence and the Lipschitz activation show
\(G_p^0\to v I_2\), where
\(v=E\tanh^2(\sqrt qG)>1/5\) and \(q=E\tanh^2G\), by the
C.4.5.1 certificate. Eigenvalue continuity here follows directly from
\(|z^T(G_p^0-vI)z|\le\|G_p^0-vI\|_{\rm op}|z|^2\).
Choose \(p_0\) such that

\[
\lambda_{\min}(G_p^0)\ge3/20\qquad(p\ge p_0).             \tag{11}
\]

Initialization is independent of \(\alpha\), hence so is \(p_0\).
No parity or coordinate-swap property of the full dictionary is needed.

The closure uses its actual physical state metric

\[
\|\delta\Theta\|_{p}^2
 =\|\delta w\|_2^2+\|\delta M\|_F^2+\|\delta c\|_2^2,
\quad \Theta_p=(w_p,M_p,c_p).                              \tag{12}
\]

The Frobenius term in (12) must not be replaced by the HS norm of
\(K_p\): the latter is only bounded above by the former. Put
\(d_p=\|\Theta_p-\Theta_p(0)\|_p\) and \(\delta=1/100\).
If \(d_p\le\delta\), each training hidden feature satisfies

\[
\begin{split}
\|H^2_{p,a}(t)-H^2_{p,a}(0)\|_2
&\le\|A_p\|\|\phi(w_{p,a})-\phi(g_a)\|_2+\|K_p\|_{\rm HS}\\
&\le(3+d_p)d_p\le(3+\delta)\delta.
\end{split}                                                \tag{13}
\]

All hidden feature norms are at most one. Subtracting the two factors
in each entry of their Gram \(G_p(t)\) gives an entrywise difference
at most \(2(3+\delta)\delta\); the operator norm of a two-by-two
matrix is at most twice its largest entry magnitude. Consequently

\[
\|G_p(t)-G_p^0\|_{\rm op}\le4(3+\delta)\delta
 =301/2500<1/8,
\quad \lambda_{\min}G_p(t)\ge1/40=:\gamma.                 \tag{14}
\]

The strict inequality \(3/20-301/2500=37/1250>1/40\) leaves slack.

Let \(r=(f_{p,1}-\alpha,f_{p,2}+\alpha)\) and
\(\mathcal L_p=|r|^2/2\). The physical gradient identity and the
readout block alone imply, while in this ball,

\[
\mathcal L_p'=-\|\Theta_p'\|_p^2,
\qquad \|\Theta_p'\|_p^2\ge\|c_p'\|_2^2
 =r^TG_p(t)r\ge2\gamma\mathcal L_p.                       \tag{15}
\]

The factors follow from
\(c_p'=-(r_1H^2_{p,1}+r_2H^2_{p,2})\), not from a change of clock.
Since \(\mathcal L_p(0)=\alpha^2\),

\[
\sqrt{\mathcal L_p(t)}\le\alpha e^{-\gamma t}.
                                                                    \tag{16}
\]

More usefully, wherever the loss is positive,

\[
\|\Theta_p'\|_p
 \le{-\mathcal L_p'\over\sqrt{2\gamma\mathcal L_p}},
\quad
\int_a^b\|\Theta_p'\|_pdt
 \le\sqrt{2/\gamma}\,[\sqrt{\mathcal L_p(a)}-
                              \sqrt{\mathcal L_p(b)}].     \tag{17}
\]

This is obtained by dividing
\(\|\Theta_p'\|_p^2=-\mathcal L_p'\) by its lower bound
\(\|\Theta_p'\|_p\ge\sqrt{2\gamma\mathcal L_p}\) and integrating
the derivative of \(\sqrt{\mathcal L_p}\). If the loss reaches zero,
all residual-driven velocities vanish thereafter, and the same result
follows by a limit from positive-loss times.

Before any first exit from \(d_p<\delta\), (17) gives

\[
d_p(t)\le\sqrt{80}\,\alpha\le\sqrt{80}/1000<1/100.
                                                                    \tag{18}
\]

Continuity contradicts an exit. Fixed-order global existence then proves
(14)–(18) for every physical time, for every \(p\ge p_0\).
In particular, the coefficient-metric endpoint exists and

\[
\|\Theta_p(t)-\Theta_p^\infty\|_p
 \le\sqrt{80}\alpha e^{-t/40}.                            \tag{19}
\]

The \(L^2\)/Frobenius state space is complete, so this follows from
the Cauchy estimate (17). The endpoint lies in the stated characteristic
class as well: \(\|c_p'\|_\infty\le2\sqrt{\mathcal L_p}\), and
for fixed \(p\), the bounded-feature row estimate gives
\(\|w_p'\|_\infty\le C_p\sqrt{\mathcal L_p}\). The constants
are finite since \(M_p,c_p\) stay bounded; the residual is integrable.

For a passive input \(u\), the three prediction-gradient norms in
(12) are at most \(\|A_p\|\|c_p\|_2\), \(\|c_p\|_2\), and one.
For the matrix block, \(\nabla_M f=d(u)a(u)^T\) and the contraction
bounds give \(|d|\le\|c_p\|_2\), \(|a|\le1\). Thus on the convex
\(\delta\)-ball the prediction is Lipschitz, uniformly on the circle,
with constant
\(\sqrt{1+\delta^2[1+(2+\delta)^2]}<2\). Therefore

\[
\|f_{p,\alpha}(t)-f_{p,\alpha}^\infty\|_\infty
 \le2\sqrt{80}\alpha e^{-t/40}<18\alpha e^{-t/40}.         \tag{20}
\]

The endpoint fits both labels by (16). Each predictor is continuous in
\(u\), by bounded action and the first-row \(L^2\) bound; the uniform
limit (20) makes the endpoint continuous as claimed.

## 3. Identification with canonical GF on every fixed horizon

It would be invalid simply to cite the time-40 theorem for (1), since
its law family has labels \(\pm1\). Instead its direct comparison
argument applies with hypotheses checked here.

First, the initialized observable spaces used in the filter proof contain
the entire feature-orbit segment \(0\le s\le s_\alpha\). To see this,
their bounded-word spans are dense in the \(L^2\) spaces of the generated
sigma fields, and the spaces reduce \(A_0,A_0^*\). The frozen roots
belong by bounded truncation. The C.4.5.1 clock Picard construction uses
these roots, the same actions, finite ranks, products with bounded gates,
and measurable scalar functions \(j(X,g)\). At each iteration these
operations remain measurable in the respective generated sigma fields;
\(|j(X,g)-g|\le|X|\) keeps their \(L^2\) integrability. Their limits
stay in the closed spaces, and their learned increments stay in the
corresponding closed HS block. This is a direct invariance argument; it
does not extend the smaller-law theorem by citation.

For a fixed \(T<\infty\), the target's \(H^1(t,u)\) has a compact
\(L^2\) image on \([0,T]\times S^1\), by strong continuity and the
input Lipschitz bound. Its two training upper backward fields
\(\Delta_a^2=c\phi'(AH_a^1)\) have compact \(L^2\) images, since
the target readout is bounded and bounded multiplication is strongly
continuous on fixed \(L^2\) vectors. Its \(K'(t)\) is a compact
HS curve. Strong convergence of uniformly bounded operators is uniform
on compact sets, by taking a finite net. Finite-rank approximation of
HS operators and a second finite net therefore give

\[
\begin{split}
\epsilon_p(T)={}&\sup_{t\le T,u}\|(B_p-A_0)H^1(t,u)\|_2
 +\max_a\sup_{t\le T}\|(B_p^*-A_0^*)\Delta_a^2(t)\|_2\\
 &+\sup_{t\le T}\|Q_{2,p}K'(t)Q_{1,p}-K'(t)\|_{\rm HS}
 \longrightarrow0.                                      \tag{21}
\end{split}
\]

For the HS step, each rank \(v\otimes z\) becomes
\(Q_{2,p}v\otimes Q_{1,p}z\), whose error vanishes by strong
convergence; contractions control the omitted finite-rank remainder.
No \(\epsilon_p\) is an input to the actual closure.

Second, C.4.5.2 (R17)–(R18) supplies common Gaussian RMS tails for the
two target reverse fields \(Q_a=A^*\Delta_a^2\) throughout the entire
unit-reference feature interval. Our segment is a subset by (5). Thus
there exist finite constants \(C_0,c_0,R_0>0\), independent of physical
time along this segment, with

\[
\max_a\sup_{t\ge0}\tau_R(Q_a(t))
 \le C_0e^{-c_0(R-R_0)^2}\qquad(R\ge R_0).                \tag{22}
\]

Only the two training reverse queries need tails. Passive predictions
use forward comparison, so no unproved whole-circle reverse-tail
statement is inserted.

For completeness the comparison is as follows. Couple the closures and
the target on the canonical carrier and put

\[
E_p(t)=\|w_p-w\|_2+\|K_p-K\|_{\rm HS}+\|c_p-c\|_2.
\]

The uniform action, raw-state, and target readout bounds above give
\(\|H_p^1-H^1\|_2\le E_p\) and, uniformly in passive \(u\),

\[
Z_p^2-Z^2=A_p(H_p^1-H^1)+(K_p-K)H^1+(B_p-A_0)H^1,
\quad
\|H_p^2-H^2\|_2+|f_p-f|\le C(E_p+\epsilon_p).             \tag{23}
\]

Subtracting \(c_p-c\) first in the upper backward field and then using
the bounded target \(c\) proves
\(\|\Delta_{p,a}^2-\Delta_a^2\|_2\le C(E_p+\epsilon_p)\).
The reverse subtraction is
\(A_p^*(\Delta_p^2-\Delta^2)+(K_p-K)^*\Delta^2+
(B_p^*-A_0^*)\Delta^2\), giving the same bound. For the lower gate,
split the unchanged target reverse field at magnitude \(R\):

\[
\|\phi'(w_p\cdot e_a)Q_{p,a}-\phi'(w\cdot e_a)Q_a\|_2
 \le C(E_p+\epsilon_p)+2RE_p+2\tau_R(Q_a).                \tag{24}
\]

Below the cutoff use \({\rm Lip}(\phi')\le2\); above it use the
bounded gates. The middle equation is precisely

\[
K_p'-K'=Q_{2,p}\{F_K(w_p,A_p,c_p)-F_K(w,A,c)\}Q_{1,p}
              +(Q_{2,p}K'Q_{1,p}-K'),                    \tag{25}
\]

where \(F_K\) is the full residual-driven rank equation for the same
law (1). Its residual and rank-factor subtractions are bounded in HS
norm by \(C(E_p+\epsilon_p)\), using
\(\|v\otimes z-\bar v\otimes\bar z\|_{\rm HS}
\le\|v-\bar v\|_2\|z\|_2+\|\bar v\|_2\|z-\bar z\|_2\).
The row and readout subtractions use (23)–(24). Therefore

\[
D^+E_p\le C(1+R)(E_p+\epsilon_p)
                  +CC_0e^{-c_0(R-R_0)^2},\qquad E_p(0)=0. \tag{26}
\]

All constants are finite and independent of \(p,R\); no higher moment
or tail of the approximate trajectory is assumed. The sum of norms is
absolutely continuous, and its upper derivative has this bound even
when a component norm vanishes. The exponential integrating factor gives

\[
\sup_{t\le T}E_p(t)\le
 CT e^{C(1+R)T}{(1+R)\epsilon_p+C_0e^{-c_0(R-R_0)^2}\}.
                                                                    \tag{27}
\]

Let \(p\to\infty\) at fixed \(R\), then \(R\to\infty\). The negative
quadratic exponent dominates the positive linear one, proving uniform
raw convergence on every fixed horizon. Equation (23) proves the same
for whole-circle predictions. The same estimate against any canonical
strong raw solution, with zero omitted source, proves uniqueness on
each finite interval on which the comparison solution has the ordinary
energy/action/readout bounds.

The target and finite closures retain their nonlinear hidden dynamics;
neither the argument nor (21) calls for frozen features.

## 4. Endpoint and all-time passage; hidden-block activity

Put \(a_p(T)=\sup_{t\le T,u}|f_{p,\alpha}(t,u)-f_\alpha(t,u)|\).
Then \(a_p(T)\to0\) for each fixed \(T\). At the endpoints,

\[
\|f_{p,\alpha}^\infty-f_\alpha^\infty\|_\infty
 \le a_p(T)+18\alpha e^{-T/40}+7\alpha e^{-T/5}.            \tag{28}
\]

For \(t\ge T\), integrate the path-length estimates from \(T\) to
\(t\); the same two tail bounds give
\(|f_p(t,u)-f(t,u)|\le a_p(T)+18\alpha e^{-T/40}
+7\alpha e^{-T/5}\). For \(t\le T\) use \(a_p(T)\) itself.
Taking first \(p\to\infty\), then \(T\to\infty\), proves both
claims in (2). This is exactly the uniform tail bridge absent from
finite-horizon convergence alone. Raw endpoint convergence in row/HS/
readout norms follows by the same argument using (7),(19),(27).

Activity is retained at the common physical time \(t_{\rm act}=1/4\).
Because \(0\le b(s)\le s\), equation (6) gives

\[
\alpha(1-e^{-2t})\le s_\alpha(t)\le2\alpha t,
\qquad \alpha/3<s_\alpha(1/4)\le\alpha/2<1/100.            \tag{29}
\]

The lower scalar comparison follows by multiplying
\(s'+2s\ge2\alpha\) by \(e^{2t}\). The strict inequality uses
\(e^{1/2}>3/2\). C.4.5.1 (R32)–(R34), valid on this same feature
orbit, gives for each training atom and each hidden layer

\[
\|H_a^\ell(s)-H_a^\ell(0)\|_2\ge s^2/200.
                                                                    \tag{30}
\]

Hence the training-averaged paired hidden RMS at time \(1/4\) exceeds
\(\alpha^2/1800\) in both layers. First-row motion is at least the
first hidden RMS because tanh is one-Lipschitz.

The middle block also moves independently of that inference. In the
notation of C.4.5.1 (R24), its proved expansion is

\[
K(s)=\frac{s^2}{4}(U_1\otimes H_1^1(0)-U_2\otimes H_2^1(0))
        +\mathcal R(s),\qquad
\|\mathcal R(s)\|_{\rm HS}\le45s^4/32.                   \tag{31}
\]

The two initial lower features are orthogonal with squared norm
\(q>39/100\), and \(\|U_a\|_2^2>3/100\). Thus the norm of the
coefficient of \(s^2\) is
\(\frac14\sqrt{q(\|U_1\|_2^2+\|U_2\|_2^2)}>1/30\).
For \(s\le1/100\), (31) implies \(\|K(s)\|_{\rm HS}>s^2/100\),
and at time \(1/4\) this exceeds \(\alpha^2/900\).
Also (C.4.5.1 R12) gives \(\|c(s)\|_2\ge s\sqrt m>0\).

For each fixed \(\alpha>0\), the finite-horizon convergence above
passes these strict positive margins to all sufficiently large \(p\).
For the upper initial/current pair, initial feature convergence follows
separately from \(B_p\to A_0\); both times are coupled on the same
population carrier. Thus the closures eventually have paired hidden
RMS at least \(\alpha^2/3600\) in both layers and learned-middle
HS norm at least \(\alpha^2/1800\) at time \(1/4\). Nonzero
\(K_p\) implies nonzero \(M_p-D_p\). Their readout and first row move
as well. The activity order threshold may depend on \(\alpha\).

## 5. Logical obstruction outside the proved fitting neighborhood

Finite-horizon convergence plus separate exact fitting is not alone an
endpoint theorem, even for elementary autonomous squared-loss GF. This
example is a logical obstruction, not a counterexample to the canonical
tanh hierarchy.

For \(\varepsilon>0\), use the fixed Euclidean state \((x,z)\),
initial state zero, labels \((1,1)\), and unhalved two-point mean loss

\[
L_\varepsilon(x,z)=\tfrac12[(x-1)^2+
                         ((1+\varepsilon)x+\varepsilon z-1)^2].
                                                                    \tag{32}
\]

Its Hessian is positive definite, since the two-by-two prediction matrix
\(\left(\begin{smallmatrix}1&0\\1+\varepsilon&\varepsilon
\end{smallmatrix}\right)\) is invertible. Its linear gradient ODE
therefore converges to the unique interpolant \((1,-1)\). Explicitly,
subtract this equilibrium: the difference solves
\(v'=-A_\varepsilon^TA_\varepsilon v\); orthogonal diagonalization
gives exponential decay in each positive eigenvalue.
At \(\varepsilon=0\), \(L_0=(x-1)^2\) and the same initialization
gives \(x(t)=1-e^{-2t},z(t)=0\), ending at \((1,0)\).
The vector-field coefficients converge, so solutions converge on every
fixed horizon: subtraction and the finite-dimensional integrating-factor
bound give \(\sup_{t\le T}|\theta_\varepsilon(t)-\theta_0(t)|
\le C_T\varepsilon\).

To make the missed observable a whole-circle predictor that still agrees
with the training predictions, set

\[
F_\varepsilon(u)=xu_1+[(1+\varepsilon)x+\varepsilon z]u_2
                  +z\,u_1u_2(u_1+u_2),\qquad u\in S^1.    \tag{33}
\]

The added odd cubic vanishes at both training inputs. Every positive
\(\varepsilon\) endpoint is
\(u_1+u_2-u_1u_2(u_1+u_2)\), while the limiting-flow endpoint is
\(u_1+u_2\). At \(u=(1,1)/\sqrt2\) the gap is \(1/\sqrt2\).
All models fit exactly and their predictors converge uniformly on every
compact time/circle domain, yet their endpoints do not converge. Their
smallest Hessian eigenvalue tends to zero. The explicit estimate (14),
rather than fitting alone, rules out this slow-direction mechanism for
the small-label canonical result above.

## Check record and remaining scope

Self-checks performed: exact metric/factor tracing from (H3.N2), independent
readout-only derivation of (15), strict rational bootstrap margins, explicit
time reparameterization of the canonical feature orbit, compact-source and
Gaussian-cutoff comparison with only training-query tails, and adversarial
checks of symmetry, ridge, limit order, and hidden-block activity. The
source versions and actual checks are recorded above. No external theorem,
quadrature experiment, fitted coefficient, or trajectory-dependent order
selection was used. This is a self-checked candidate pending independent
review, not an established-library result.

The strict constants were also checked with the following deterministic
standard-library Python command in the repository root; exit status zero,
output `PASS: Gram margin, trapping radius, and active middle-block constants.`

```python
from fractions import Fraction as F
radius = F(1,100)
gap = 4*(3+radius)*radius
assert gap == F(301,2500)
assert F(3,20)-gap == F(37,1250) > F(1,40)
assert 80*F(1,1000)**2 < radius**2
assert F(39,100)*F(6,100)/16 > F(1,30)**2
assert F(1,30)-F(45,32)*F(1,100)**2 > F(1,100)
print('PASS: Gram margin, trapping radius, and active middle-block constants.')
```

Open: comparison at unit opposite labels; a useful computable order threshold
or rate; large-order coercivity for broader laws; any monotonicity of
successive finite orders; simultaneous neural-width/order/infinite-time
limits. The small-label theorem itself assumes none of those claims.
