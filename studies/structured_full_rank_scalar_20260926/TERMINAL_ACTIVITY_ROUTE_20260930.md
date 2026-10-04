# Terminal stability from finite residual activity in the P=1 closure

2026-09-30. Scoped theoretical continuation; no experiments, no promotion.
The statements below are proved for their stated assumptions. In particular,
uniform residual damping is a condition, not an established property of the
P=1 response-memory flow. The note proves error propagation bounds; it does
not supply the scalar aggregate truncation or its error-source estimate.

The main conclusion is that residual damping and residual-proportional
approximation errors replace physical-time amplification by amplification
in total learning activity. A weighted error functional gives this directly.
For externally bounded errors in the realized output operators, the terminal
predictor bound has no exponential amplification at all.

## Scope and information contract

The target is the specified two-hidden-layer tanh network with unrestricted
fixed middle initialization W0 and the P=1 memory closure. Its predictions
must be approximated on the training inputs and on a bounded query-input
set. The desired second-level approximation retains genuinely fewer scalar
aggregate states than width at matched accuracy; particles, histograms,
population densities, a frozen neuron dictionary, an unrestricted full
moment list, and coefficients fitted to a future reference trajectory are
not admissible answers. None is introduced here.

The route establishes conditional all-time stability and terminal stopping
estimates that an admissible aggregate construction could use. It does not
infer a number of required aggregate coordinates from path length alone.
All constants below display their mathematical dependencies; a constant
depending on a width-growing norm of W0 is not a width-independent result.

Allowed scientific inputs were the supervisor's self-contained equations
and sections 1–3 of AGGREGATE_SCALAR_CONSTRUCTION.md. Actual read coverage
was lines 1–240 of that file: this accidentally included the beginning of
section 4, through its finite-time bounds and the start of its Gaussian
cutoff argument. This scope overrun was reported to the supervisor. No other
route notes, other agents' findings, other studies, or archived book material
were read. The candidate mechanism was frozen before any comparison with
other routes. Required skills and shared process instructions were read.

## 1. Exact finite-width equations and activity bounds

There are m training inputs u_a in R^d, with |u_a|≤U, and width n. Every
query considered also satisfies |u|≤U. Write

\[
 h_a=\tanh(wu_a),\quad v_a=\tanh(Wh_a),\quad
 f_a=n^{-1}c^Tv_a,\quad r_a=f_a-y_a,
 \qquad \rho=\|r\|_m,
\]

where \(\langle p,q\rangle_m=m^{-1}p^Tq\) and
\(\|p\|_m=\sqrt{\langle p,p\rangle_m}\). For neuron vectors and matrices
use \(\|v\|_n=|v|/\sqrt n\) and
\(\|X\|_{F,n}=\|X\|_F/\sqrt n\). Matrix operator norms are Euclidean
operator norms, equivalently operator norms between the corresponding
equally normalized vector spaces.

Let \(d_a=c\odot\tanh'(Wh_a)\) and
\(e_a=\tanh'(wu_a)\odot W^Td_a\). The stipulated P=1 equations are

\[
\begin{aligned}
 W&=W_0-\frac{2}{mnL}AB^T,&
 \dot w&=-\frac2m\sum_a r_ae_au_a^T,&
 \dot c&=-\frac2m\sum_a r_av_a,\\
 \dot A_a&=r_ad_a,& \dot B_a&=\rho h_a,&\dot L&=\rho,
\end{aligned}                                                    \tag{1}
\]

with A(0)=0, B_a(0)=h_a(0), and L(0)=1. Define

\[
 s(t)=\int_0^t\rho(\tau)\,d\tau=L(t)-1,
 \qquad M=B/L,\qquad H=(h_1,\ldots,h_m).
\]

Then, exactly,

\[
 W=W_0-\frac{2}{mn}AM^T,\qquad
 \dot M=\frac{\rho}{1+s}(H-M).                         \tag{2}
\]

Thus M is the normalized running feature average, including its initial
unit of activity. Every entry of M lies in [-1,1]. This normalization is
useful analytically and introduces no approximation.

Put \(C_0=\|c(0)\|_n\), \(G=\|W_0\|_{\rm op}\), and

\[
 C(s)=C_0+2s,\qquad Q(s)=C_0s+s^2.
\]

On every interval on which the solution exists,

\[
\begin{aligned}
 \|c\|_n&\le C(s),& \|A\|_{F,n}&\le\sqrt m\,Q(s),&
 \|M\|_{F,n}&\le\sqrt m,\\
 \|W\|_{\rm op}&\le G+2Q(s),&&&
 \|w-w(0)\|_{F,n}&\le2U\{GQ(s)+Q(s)^2\}.
\end{aligned}                                                    \tag{3}
\]

To verify the first two bounds, use |tanh|≤1, |tanh'|≤1 and
\(m^{-1}\sum_a|r_a|\le\rho\):

\[
 \|\dot c\|_n\le2\rho,\qquad
 \|\dot A\|_{F,n}^2
 =\sum_a r_a^2\|d_a\|_n^2
 \le m\rho^2 C(s)^2.
\]

Integration in s gives (3), since \(Q'=C\). The bound on W follows from
\(\|AM^T\|_{\rm op}\le\|A\|_F\|M\|_F\). Finally,

\[
 \|\dot w\|_{F,n}
 \le2U\rho C(s)\{G+2Q(s)\}.
\]

Integrating this inequality and again using Q'=C gives the last bound.
These bounds require no positivity of an output kernel.

They also prove global finite-time existence in the finite-width system.
Indeed, \(|f_a|\le C(s)\), so
\(\dot s\le C_0+2s+\|y\|_m\). Multiplying this inequality by
\(e^{-2t}\) and integrating bounds s on every finite interval. Equation
(3), B=(1+s)M, and L=1+s then keep every dynamic coordinate bounded on
such an interval. The vector field is locally Lipschitz for L>0, including
at r=0 because the norm \(r\mapsto\rho\) is Lipschitz. A solution in a
bounded subset with L≥1 can be continued by the local existence argument.

### Finite-activity endpoint theorem

If

\[
 S=\int_0^\infty\rho(t)\,dt<\infty,                 \tag{4}
\]

then w,c,A,M,B,L and W converge to finite limits, every training residual
converges to zero, and f(t,u) converges uniformly for |u|≤U to a terminal
predictor f_infinity(u).

Here is the complete argument. Bounds (3) give bounded coefficient factors
in all velocities. In addition,
\(\|\dot M\|_{F,n}\le2\sqrt m\rho/(1+s)\).
Consequently each coordinate has integrable speed and is Cauchy as
t→infinity. Its limit is finite. Continuity of tanh and the displayed
formulas gives a limiting residual vector. If its norm were positive,
rho would be bounded below by a positive constant for all sufficiently
large times, contradicting (4). Hence the limiting residual is zero.

For uniform query convergence, differentiation and Cauchy–Schwarz give

\[
 \left|\frac{d f(u)}{dt}\right|
 \le\rho J(s),\qquad
 J(s)=2+2C(s)^2+\frac{4C(s)Q(s)}{1+s}
       +2U^2C(s)^2\{G+2Q(s)\}^2.                   \tag{5}
\]

In detail, (2) implies
\(\|\dot W\|_{\rm op}\le\rho[2C(s)+4Q(s)/(1+s)]\).
The derivative of the output is bounded by
\(\|\dot c\|_n+\|c\|_n[
\|\dot W\|_{\rm op}+\|W\|_{\rm op}U\|\dot w\|_{F,n}]\),
which is (5). Define the monotone upper bound

\[
 J_*(S)=2+2C(S)^2+4C(S)Q(S)
             +2U^2C(S)^2\{G+2Q(S)\}^2.
\]

Integration yields the explicit terminal estimate

\[
 \sup_{|u|\le U}|f_\infty(u)-f(t,u)|
 \le J_*(S)\int_t^\infty\rho(\tau)\,d\tau.         \tag{6}
\]

This proves uniform convergence as well as a stopping-error bound in
remaining activity. It does not assert that remaining activity can be
computed from the present residual without an additional damping estimate.

For the exact Gaussian-block population model at P=1 with c(0)=0, the
endpoint conclusion also holds conditional on (4). To see this without
assuming a bounded supremum over Gaussian blocks, fix a block seed with
finite G and w(0). Coordinatewise, |c_i|≤2s,
|A_ia|≤sqrt(m)s², and |M_ia|≤1. Its shared backward contraction obeys
\(|V_a(u)|\le2\sqrt m\,s^3\), where
\(V_a=k^{-1}\int A_a^Td(u)\,d\mu\). Hence its first-weight speed satisfies

\[
 \|\dot w\|_F
 \le4\sqrt k\,U\rho\{s\|G\|_{\rm op}+2\sqrt m\,s^3\}.
\]

All local coordinates therefore have limits when S<infinity. The bounds on
c,A,M are uniform in the block seed, so the bounded-convergence argument
passes the feature contractions and outputs to their limits. Uniformity in
|u|≤U follows by first taking the supremum inside each block: local
coordinate convergence implies uniform convergence on this bounded input
set, and the tanh outputs remain bounded. The same positive-limit
contradiction proves r→0. This endpoint argument applies to the block
population; the finite-width constants involving G in (5)–(6) do not
automatically become uniform constants for an unbounded Gaussian law.

## 2. Exact residual equation: where positivity can fail

Differentiate the output along (1)–(2). Define

\[
\begin{aligned}
 (K_0)_{ab}
 &=\frac{2}{mn}\big[v_a^Tv_b+(u_a^Tu_b)e_a^Te_b\big]
   +\frac{2}{mn^2}(d_a^Td_b)(h_a^Th_b),\\
 D_{ab}&=\frac{2}{mn^2}(d_a^Td_b)h_a^T(M_b-h_b),\\
 q_a&=-\frac{2}{mn^2(1+s)}
         \sum_b(d_a^TA_b)h_a^T(h_b-M_b).
\end{aligned}                                                    \tag{7}
\]

The symbol q here is a drift vector, not the normalized residual. Then

\[
 \dot r=-(K_0+D)r+q\rho.                            \tag{8}
\]

For verification, the middle-matrix contribution is

\[
\begin{aligned}
 n^{-1}d_a^T\dot W h_a
 ={}&-\frac{2}{mn^2}\sum_b r_b(d_a^Td_b)M_b^Th_a\\
    &-\frac{2\rho}{mn^2(1+s)}
          \sum_b(d_a^TA_b)(h_b-M_b)^Th_a.
\end{aligned}
\]

The w and c derivatives give the first two terms in K0. Splitting
M_b=h_b+(M_b-h_b) gives (7)–(8).

K0 is symmetric positive semidefinite: its three summands are Gram
matrices of, respectively, v_a, u_a tensor e_a, and d_a tensor h_a,
with positive scale factors. D need not be symmetric, and the q rho term
is not a linear gradient-kernel term. Replacing (8) by
\(\dot r=-K_0r\) therefore changes the P=1 target.

For a fixed state x=(w,c,A,M,s), define the residual operator

\[
 N_x(z)=(K_0(x)+D(x))z-q(x)\|z\|_m.                 \tag{9}
\]

Its argument z is a hypothetical residual vector at that fixed state.
The sufficient condition

\[
 \lambda_{\min}\!\left(\operatorname{sym}(K_0+D)\right)
       -\|q\|_m\ge\lambda>0                       \tag{10}
\]

implies, for all z,z',

\[
 \langle z-z',N_x(z)-N_x(z')\rangle_m
 \ge\lambda\|z-z'\|_m^2.                          \tag{11}
\]

Indeed, the linear term has the lower bound in (10), while the absolute
value of the norm-difference term is at most
\(\|q\|_m\|z-z'\|_m^2\), by Cauchy–Schwarz and
\(|\|z\|_m-\|z'\|_m|\le\|z-z'\|_m\).
A more conservative sufficient condition is

\[
 \lambda_{\min}(K_0)-\|D\|_{\rm op}-\|q\|_m
 \ge\lambda>0.                                    \tag{12}
\]

Both conditions concern the actual feature-memory lag. At initialization
M=H and A=0, so D=q=0. This initialization identity alone does not
control their later values or preserve a positive eigenvalue gap.

If (11) holds along a trajectory, setting z'=0 in (11) and differentiating
rho²/2 gives

\[
 \rho(t)\le\rho(0)e^{-\lambda t},\qquad
 S\le\rho(0)/\lambda,\qquad
 \int_t^\infty\rho\le\rho(t)/\lambda.              \tag{13}
\]

The norm inequality at rho=0 is obtained by continuity, and zero residual
is absorbing by uniqueness. Equations (6) and (13) then give a certified
terminal predictor error bounded by J_*(rho(0)/lambda) rho(t)/lambda.

A noncircular way to certify (13) is an invariant-neighborhood argument.
Suppose a radius-R state ball about x(0) has residual contraction (11)
with constant lambda and speed bound \(\|\dot x\|\le b\rho\).
If \(b\rho(0)/\lambda<R\), the trajectory cannot first exit that ball:
up to a hypothetical exit its displacement is at most
\(b\int_0^t\rho\le b\rho(0)/\lambda<R\).
It therefore stays inside, and (13) holds globally. Establishing such a
ball from the actual initialization is an additional theorem obligation;
it is not supplied by the architecture or by this note.

## 3. A global comparison lemma with amplification only in activity

The lemma is stated for an error functional E, so that it can later be
used for a scalar-aggregate closure without introducing hidden full neuron
coordinates. It does not assert that the required error inequalities hold
for a particular closure.

Let E(t)≥0 measure a chosen state/aggregate discrepancy and let
\(R(t)=\|r(t)-\widetilde r(t)\|_m\). Suppose both are locally absolutely
continuous and, almost everywhere,

\[
\begin{aligned}
 E'&\le a\widetilde\rho E+bR+\varepsilon_x\widetilde\rho,\\
 R'&\le-\lambda R+c\widetilde\rho E
                        +\varepsilon_r\widetilde\rho,
\end{aligned}                                                    \tag{14}
\]

where a,b,c,epsilon_x,epsilon_r≥0 and lambda>0. Let
\(\widetilde s(t)=\int_0^t\widetilde\rho\),
\(\kappa=a+bc/\lambda\),
\(\varepsilon=\varepsilon_x+b\varepsilon_r/\lambda\), and
\(Z=E+bR/\lambda\). Then

\[
 Z(t)\le e^{\kappa\widetilde s(t)}Z(0)
       +\varepsilon\frac{e^{\kappa\widetilde s(t)}-1}{\kappa}.
                                                               \tag{15}
\]

The fraction means \(\widetilde s(t)\) when kappa=0. In particular, a
finite bound on total surrogate activity makes (15) uniform for all t.

The proof is a cancellation, not a physical-time estimate. Multiply the
second inequality in (14) by b/lambda and add it to the first. The terms
bR and -bR cancel, giving

\[
 Z'\le\kappa\widetilde\rho E+\varepsilon\widetilde\rho
     \le\kappa\widetilde\rho Z+\varepsilon\widetilde\rho.
\]

Multiplication by \(e^{-\kappa\widetilde s(t)}\), followed by integration,
proves (15). Thus no \(e^{CT}\) factor is introduced even when physical
time is infinite.

### How residual factorization produces the hypotheses

For example, suppose two comparable states obey

\[
\begin{aligned}
 \dot x&=\mathcal G(x)r+g(x)\rho,\\
 \dot{\widetilde x}
 &=\mathcal G(\widetilde x)\widetilde r
                  +g(\widetilde x)\widetilde\rho+\xi,
 &\|\xi\|&\le\varepsilon_x\widetilde\rho,\\
 \dot r&=-N_x(r),\\
 \dot{\widetilde r}&=-N_{\widetilde x}(\widetilde r)+\zeta,
 &\|\zeta\|_m&\le\varepsilon_r\widetilde\rho.
\end{aligned}                                                    \tag{16}
\]

These equations must be consistent with the respective observable maps;
the residual equations are not extra adjustable dynamics. Assume on the
states being compared that

\[
\begin{aligned}
 \|\mathcal G(x)\|+\|g(x)\|&\le b,\\
 \|\mathcal G(x)-\mathcal G(\widetilde x)\|
       +\|g(x)-g(\widetilde x)\|&\le a\|x-\widetilde x\|,\\
 \|N_x(z)-N_{\widetilde x}(z)\|_m
       &\le c\|x-\widetilde x\|\|z\|_m,
\end{aligned}                                                    \tag{17}
\]

and N_x satisfies (11). Subtract the state equations, using x as the
base point for r-tilde r and tilde r as the base residual for the
coefficient difference. Since |rho-tilde rho|≤R, the norm derivative is
the first inequality of (14). Subtract the residual equations by writing

\[
 -N_x(r)+N_{\widetilde x}(\widetilde r)
 =-[N_x(r)-N_x(\widetilde r)]
  -[N_x(\widetilde r)-N_{\widetilde x}(\widetilde r)].
\]

The first bracket dissipates R by (11), and (17) bounds the second by
c E tilde rho. This proves the other inequality in (14). At zero norms,
the same estimates hold in the upper right derivative sense and hence
almost everywhere; no division by a zero residual is required.

If epsilon_r<lambda, the surrogate itself satisfies

\[
 \widetilde\rho(t)
 \le\widetilde\rho(0)e^{-(\lambda-\varepsilon_r)t},\qquad
 \widetilde S\le\frac{\widetilde\rho(0)}{\lambda-\varepsilon_r}.
                                                               \tag{18}
\]

To obtain this, take the inner product of its residual equation with
tilde r, use (11) with z'=0, and use the stated bound on zeta.
Thus (15) can have an a priori finite activity budget for both systems.
Crucially, errors in (16) vanish with the surrogate residual. A uniform
absolute-in-time truncation defect is a different hypothesis and does
not give (18) or an absorbing zero-loss state.

The comparison lemma remains valid whenever (14) has been derived in an
aggregate norm. To use it for fewer-than-width scalar states, one must
still prove (14) in that norm with a,b,c,lambda and both defects controlled
independently of width and with a favorable coordinate count. A full
population comparison norm whose only known approximation requires all
moments would not meet the scalar-compression contract.

### Variant allowing stable nonnormal residual propagation

Pointwise positive definiteness is sufficient, not logically necessary.
Suppose instead the residual difference satisfies

\[
 e'=-C(t)e+v(t),\qquad
 \|v(t)\|_m\le(cE(t)+\varepsilon_r)\widetilde\rho(t),
\]

and the propagator U(t,s) of the homogeneous equation has the verified
integral bounds

\[
 \int_0^T\|U(t,0)\|\,dt\le M_0,\qquad
 \sup_{s\ge0}\int_s^\infty\|U(t,s)\|\,dt\le M_1<\infty.
                                                               \tag{19}
\]

Variation of constants is verified by differentiation. Taking norms and
integrating its formula over t, then interchanging nonnegative integrals,
gives

\[
 \int_0^T R(t)\,dt
 \le M_0R(0)+M_1\int_0^T(cE+\varepsilon_r)\widetilde\rho.
\]

Inserting this into the integrated first inequality of (14) yields

\[
 E(T)\le E(0)+bM_0R(0)
 +(a+bcM_1)\int_0^T E\widetilde\rho
 +(\varepsilon_x+bM_1\varepsilon_r)\widetilde s(T).
                                                               \tag{20}
\]

The same integrating-factor argument bounds (20) by an exponential in
tilde s, with a+bcM1 in place of kappa. This is an alternative propagation
criterion; finite total activity and (19) must be established separately.
Stable eigenvalues at each instant alone do not establish (19), especially
for a time-dependent or nonnormal C(t).

## 4. Direct operator-error bounds for the final predictor

There is a sharper statement when discrepancies between the realized
output operators themselves are already known. This is a propagation
result, not a way to obtain these discrepancies from a scalar closure.

Suppose

\[
 \dot r=-K(t)r+q(t)\rho,\qquad
 \dot{\widetilde r}=-\widetilde K(t)\widetilde r
                              +\widetilde q(t)\widetilde\rho,
\]

and the approximate operator
\(z\mapsto\widetilde K(t)z-\widetilde q(t)\|z\|_m\)
satisfies (11) with lambda. Assume

\[
 \|K-\widetilde K\|_{\rm op}+\|q-\widetilde q\|_m
 \le\delta,\qquad S=\int_0^\infty\rho<\infty.
\]

Subtracting the equations, using the approximate operator for the
residual-difference part, gives R'≤-lambda R+delta rho. Hence

\[
 \int_0^\infty R(t)\,dt\le\frac{R(0)+\delta S}{\lambda}.
                                                               \tag{21}
\]

For a query u, write its exact and approximate output equations as

\[
 \dot f_u=-k_u(t)r+q_u(t)\rho,\qquad
 \dot{\widetilde f}_u=-\widetilde k_u(t)\widetilde r
                              +\widetilde q_u(t)\widetilde\rho.
\]

Here k_u is a linear functional on residual space, with dual norm relative
to ||.||_m; for a row vector this norm is sqrt(m) times its Euclidean norm.
The P=1 formulas for these coefficients are (7) with the output index a
replaced by u. Assume uniformly on the query set and time that

\[
 \|k_u-\widetilde k_u\|_*+|q_u-\widetilde q_u|\le\eta,
 \qquad \|\widetilde k_u\|_*+|\widetilde q_u|\le B.
\]

The output-derivative difference has magnitude at most eta rho+B R.
Integration and (21) prove

\[
 \sup_{t\ge0,u}|f_u(t)-\widetilde f_u(t)|
 \le \sup_u|f_u(0)-\widetilde f_u(0)|
       +\eta S+\frac B\lambda\{R(0)+\delta S\}.    \tag{22}
\]

If both predictors have limits, the same bound holds for their terminal
predictors. No exponential in physical time or activity appears in (22).
For a state-dependent closure, however, delta and eta refer to operators
on the two actual trajectories; bounding their feedback is precisely what
section 3 addresses. Treating delta as a small known number without that
bridge would assume the difficult part of the approximation problem.

## 5. Clock alignment and why division by rho is unnecessary

Since |rho-tilde rho|≤R,

\[
 |s(t)-\widetilde s(t)|\le\int_0^tR.
\]

Under (14), if E≤E_* and tilde S is finite, integration of its second
inequality gives the uniform clock bound

\[
 \sup_t|s(t)-\widetilde s(t)|
 \le\frac{R(0)+(cE_*+\varepsilon_r)\widetilde S}{\lambda}.
                                                               \tag{23}
\]

In particular the terminal clock values differ by at most this quantity.
They need not be equal.

If both comparable state paths have a speed bound in their own activity
coordinates, say \(\|dx/ds\|\le B_x\) and
\(\|d\widetilde x/d\widetilde s\|\le B_x\), they extend continuously
to their finite activity endpoints and then constantly beyond them.
Let X(s) and tilde X(s) denote these extended paths. Comparing first at a
common physical time and then shifting one activity coordinate by at most
the clock mismatch proves

\[
 \sup_{s\ge0}\|X(s)-\widetilde X(s)\|
 \le\sup_{t\ge0}\|x(t)-\widetilde x(t)\|
       +B_x\sup_{t\ge0}|s(t)-\widetilde s(t)|.     \tag{24}
\]

For s below either terminal activity, choose the physical time on that
trajectory with activity s and shift the other trajectory. Above both
terminal activities compare the endpoints by taking t→infinity. These
cases prove (24), including unequal terminal activities and stationary
zero-residual intervals.

By contrast, the inverse clock obeys dt/ds=1/rho while rho>0 and becomes
singular near fitting. The normalized residual r/rho need not be Lipschitz
there. For example r=r0 exp(-t) has s=r0(1-exp(-t)), so
t(s)=-log(1-s/r0), which diverges at a finite s endpoint. Estimates in
the original residual-factored equations, followed by (23)–(24), avoid
this singularity. Normalizing the computational clock by an unknown
future terminal activity would require unavailable information and is
not part of the proposed mechanism.

## 6. Necessary distinctions and counterexamples

**Zero residual stopping is exact, but fitting is not automatic.** At r=0,
rho=0 and every derivative in (1) vanishes. This only says a reached
zero-loss state is absorbing. With bias-free tanh and a training input
u=0 carrying y≠0, the corresponding output is always zero. For the
single-example dataset, the physical parameters remain fixed while
L'=|y|; activity is infinite and fitting is impossible. More generally,
duplicate inputs with conflicting labels prevent interpolation for any
initialization. Thus no architecture-only statement can guarantee (4)
over the dataset class stated in the source.

**Loss convergence alone does not imply finite activity.** The scalar
system x'=exp(-x), x(0)=0, has residual r=exp(-x)=1/(1+t), decreasing
loss r²/2, and x=log(1+t). Its residual tends to zero, but its activity
and state displacement are infinite. The missing property is quantitative
damping strong enough to make the residual integrable.

**Activity amplification can be real.** Let r'=-r, r(0)=1 and
z'=a r z. This is a smooth residual-factored system with total activity
one and terminal z=e^a z(0). A discrepancy epsilon in z(0) is amplified
to epsilon e^a. Thus finite activity does not justify removing the
activity exponential from a general feedback estimate such as (15).
The stronger bound (22) uses stronger, direct operator-error information.

**Small absolute defects do not preserve zero-loss stopping.** The
perturbed scalar equation tilde r'=-tilde r+epsilon has terminal residual
epsilon and infinite residual activity. Although the additive defect is
uniformly small, it does not vanish with the residual. This is why the
source convention in (16) matters for terminal fitting and clock bounds.

**Matching fitted training values says little about the terminal query
predictor.** In both systems take r'=-r, r(0)=1. Let a query output start
at zero and satisfy f_u'=-a r in one system and
tilde f_u'=-(a+1)r in the other. Both training residuals converge to zero,
yet the terminal query outputs differ by one. The cross-output operators
in (22), or equivalent observable controls, are essential.

**Finite path length does not supply a scalar-compression rate.** Bounds
on S and speed establish rectifiability and endpoint existence. They do
not bound how many independent aggregate observables the velocity and
query map require, how truncation error depends on aggregate order, or
the metric complexity of the family of admissible reachable states. Even
short paths can lie in arbitrarily many independent coordinate directions.
This observation is a limitation of the path-length argument, not a
no-go theorem for arbitrary nonlinear scalar closures.

## 7. Claim status and the next mathematical obligation

Exact: (2), (7), (8), zero-residual stopping, and the explicit activity
bounds (3)–(6) follow from the stipulated P=1 equations. Conditional on
finite activity, the finite-width and Gaussian-block population terminal
states exist and fit their training data.

Conditional propagation theorem: residual contraction, relative error
sources and state sensitivity bounds imply (15), (18), and clock alignment
(23)–(24). Verified integral residual propagation can replace pointwise
contraction through (19)–(20). Direct realized-operator errors imply (22).
These statements do not assume the P=1 flow is a gradient flow.

Open for the requested scalar construction: an admissible finite list of
aggregate states with a nontrivial width-saving count, a residual-relative
source bound for its autonomous equations, and residual stability on the
actual nonlinear reachable region. The highest-leverage bridge is to
derive (14) in the proposed aggregate error norm with an explicit
source-size-versus-coordinate-count bound. A positive terminal activity
result without that bridge would establish propagation, not compression.

Author check: every displayed identity and inequality was re-derived from
(1), with tanh bounds, the zero-residual case, operator normalizations,
terminal-clock mismatch, and absence of a PSD assumption checked directly.
No numerical experiments or external theorem imports were used. This is
an author-checked route candidate, not an independent review or promoted
result. The supervisor is responsible for comparison with complete
relevant maintained sources and any acceptance decision.
