# An open fitting class in fixed input dimension with arbitrarily many samples

Status: internally checked theorem; see ZERO_LABEL_OPEN_CHECK.md. This extends the supplied orthogonal-pair theorem and its proved active-field Gaussian tails. It does not assume a correlated population flow, a future kernel gap for the actual network, or zero labels in the final open class. No experiment was used.

The new supervisor assignment supplied the active-pair/orthogonal-zero-label reference idea. This attempt developed the open-neighborhood transfer independently, using the complete permitted `GAUSSIAN_POSITIVE_GEOMETRY.md`, `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, and `INTRINSIC_SYMMETRY_ROUTE.md`; no other agent's candidate or findings were read. The required skills and maintained notation remain as documented in `UNCONDITIONAL_POPULATION_ROUTE.md`.

## 1. Statement and scope

Fix any $m\ge3$, amplitude $a>0$, and orthonormal vectors $e_1,e_2,e_3,e_4\in\mathbb R^4$. Set

\[
x_1^0=e_1,\qquad x_2^0=e_2,
\]

and choose any $m-2$ distinct, nonantipodal unit vectors $x_3^0,\ldots,x_m^0$ in $\operatorname{span}\{e_3,e_4\}$. Put

\[
y^0=(a,-a,0,\ldots,0)\in\mathbb R^m,
\qquad X^0=[x_1^0,\ldots,x_m^0].
\tag{1}
\]

There is $\varepsilon>0$, depending on this fixed dataset and $a$, such that for every fixed unit-column $X\in\mathbb R^{4\times m}$ and $y\in\mathbb R^m$ satisfying

\[
\|X-X^0\|_F+\|y-y^0\|_2<\varepsilon,
\tag{2}
\]

the original network

\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|_2^2/m
\tag{3}
\]

under parameter mobilities $(n,1,n)$, independent Gaussian initialization

\[
A_{ij}(0)\sim N(0,1),\quad W_{ij}(0)\sim N(0,1/n),\quad w(0)=0,
\tag{4}
\]

satisfies

\[
\Pr\{\lim_{t\to\infty}\mathcal L_n(t)=0\}\longrightarrow1.
\tag{5}
\]

There are deterministic $T<\infty,c>0$, which can be chosen for the whole displayed neighborhood, such that for each fixed $(X,y)$ in it, with probability tending to one,

\[
\mathcal L_n(t)\le\mathcal L_n(T)e^{-c(t-T)}\qquad(t\ge T).
\tag{6}
\]

No probability supremum over the neighborhood is asserted. Its radius need not be uniform when passive inputs approach coincidence or antipodality. Choosing $\varepsilon<a/2$ keeps the first two label signs opposite; the neighborhood includes label vectors with every coordinate nonzero. For $m>4$, every configuration in it has $m>\operatorname{rank}X$. The amplitude $a$ is arbitrary and fixed independently of width. This is an open class around specified label ratios, not a theorem for every label vector or every dataset.

The proof first obtains a strict capture margin from an active-pair reference, then transfers that margin to the actual full training flow. The reference is an auxiliary system: the final flow updates all parameters using all $m$ residuals.

## 2. Exact equations and finite-horizon bounds

Write

\[
u_b=\tanh(Ax_b),\quad z_b=Wu_b,\quad h_b=\tanh z_b,
\quad D_b=1-u_b^2,\quad
b_b=w\odot(1-h_b^2),\quad B_b=W^\top b_b,
\quad\Gamma=X^\top X.
\]

Powers and products of neuron fields are coordinatewise. The original flow obeys

\[
\dot u_b=-\frac2mD_b\odot\sum_c\Gamma_{bc}r_cD_c\odot B_c,
\]
\[
\dot W=-\frac2{mn}\sum_b r_b b_bu_b^\top,
\qquad \dot w=-\frac2m\sum_b r_bh_b.
\tag{7}
\]

The full tangent kernel and its readout-plus-middle part are

\[
K_{bc}=\frac{h_b^\top h_c}{n}
 +\frac{b_b^\top b_c}{n}\frac{u_b^\top u_c}{n}
 +(x_b^\top x_c)\frac{c_b^\top c_c}{n},\qquad
c_b=D_b\odot B_b,
\]
\[
K_{\rm R+W}=H^\top H/n+Q_b\odot Q_U,
\quad (Q_b)_{bc}=b_b^\top b_c/n,\quad Q_U=U^\top U/n.
\tag{8}
\]

All three terms are positive semidefinite, and

\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr.
\tag{9}
\]

In particular $\|r(t)\|_2\le\|y\|_2$. Define the nonnegative accumulated residual

\[
p_n(t)=\frac2m\int_0^t\sum_b|r_b(v)|\,dv.
\]

Bounded activations and (7) give the exact estimates

\[
\|w(t)\|_\infty\le p_n(t),\quad
\|W(t)-W_0\|_F\le p_n(t)^2/2,\quad
p_n(t)\le2t\|y\|_2/\sqrt m.
\tag{10}
\]

The first-layer speed is then bounded in normalized Frobenius norm on every finite interval. These bounds prove global existence of the smooth finite-dimensional flow, and provide width-independent state/speed bounds on each fixed interval when $\|W_0\|_{\rm op}\le10$. That initialization event has probability tending to one by the Gaussian operator bound in maintained III.F.2.

## 3. The active reference, including its unused first coordinates

Use bars for the following finite reference, initialized with the same $A_0,W_0,w_0=0$ as (3). Its inputs are $X^0$, and it trains only the first two examples, with loss

\[
\overline{\mathcal L}_{\rm act}
=\bigl[(\bar f_1-a)^2+(\bar f_2+a)^2\bigr]/m.
\tag{11}
\]

It is useful to define its coefficient vector, distinct from its evaluated full residual,

\[
\widehat r=(\bar f_1-a,\bar f_2+a,0,\ldots,0).
\tag{12}
\]

Its equations are (7) with $X^0,\widehat r$. Because every passive input is orthogonal to $e_1,e_2$, its first preactivation $A(t)x_b^0=A_0x_b^0$ is constant for $b\ge3$. The remaining Gaussian first-layer projections in the passive plane remain independent of the entire active trained state: the latter is a measurable function only of $A_0e_1,A_0e_2,W_0$.

The complete orthogonal-pair proof in `GAUSSIAN_POSITIVE_GEOMETRY.md`, Section 11, constructs and identifies its active population flow. The only time conversion is that the mean-two-sample loss there is $m/2$ times (11): its time variable is $2t/m$. In its scalar ascent clock $s$, define

\[
g=(f_1-f_2)/2,\quad h_-=(h_1-h_2)/2,\quad
q_0=\|h_-(0)\|_2^2>0.
\]

Here and below a population norm is its $L^2$ norm. The supplied theorem proves a strong finite endpoint $s_*\le a/q_0$ with $g(s_*)=a$, and

\[
\frac{ds}{dt}=\frac4m(a-g),\qquad
a-g(s(t))\le ae^{-4q_0t/m}.
\tag{13}
\]

The active finite predictions, feature contractions, and their backward-field empirical laws converge on each fixed interval. Also

\[
\bar p_n(T):=\frac2m\int_0^T(|\widehat r_1|+|\widehat r_2|)\,dt
\longrightarrow s(T)\le s_*
\tag{14}
\]

in probability, by uniform active prediction convergence. Thus with $S=s_*+1$, $M=10+S^2/2$, the reference readout and action at any selected fixed $T$ obey $\|\bar w(T)\|_\infty\le S$, $\|\bar W(T)\|_{\rm op}\le M$, with probability tending to one. These constants do not grow with the choice of late $T$.

The active Gaussian reverse tails from the complete `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, Sections 3–4, apply to this orthogonal reference with the same time conversion. Its equal-sign presentation applies after replacing the second active input by $-e_2$: oddness gives the identical parameter flow, while $b_2,B_2$ are unchanged because the top gate is even. For each fixed $T,R$, there are $C_T,c_T>0$, independent of width and $R$, such that

\[
\Pr\left\{\max_{b=1,2}\sup_{t\le T}
 \frac{\|(|\bar B_b(t)|-R)_+\|_2}{\sqrt n}
 \le C_Te^{-c_TR^2}\right\}\longrightarrow1.
\tag{15}
\]

The source proves this by initialized-matrix sensitivity, Gaussian integration by parts including the learned increment, Gaussian concentration, and the orthogonal fixed-program limit. The passive first coordinates do not enter the active updates, so adding them does not change any hypothesis of that proof. No tail claim for passive backward fields is made or needed.

## 4. Passive predictions vanish and the full first-feature Gram has a gap

Let

\[
q_n(T)=\sup_{t\le T}\left(\sum_{b=3}^m|\bar f_b(t)|^2\right)^{1/2}.
\]

Then $q_n(T)\to0$ in probability. To prove this, condition on the active trained state at a fixed time and on its bounded-operator initialization event. For one passive unit input, its first preactivation vector is iid standard Gaussian and independent of this state. Write it as $G\in\mathbb R^n$. Its prediction is

\[
F(G)=\bar w^\top\tanh(\bar W\tanh G)/n.
\]

Oddness gives $\mathbb E_G F=0$, and

\[
|\nabla_GF|^2
\le\|\bar W\|_{\rm op}^2\|\bar w\|_2^2/n^2
\le C_T/n.
\tag{16}
\]

Gaussian Poincare yields $\mathbb E_GF^2\le C_T/n$. The needed form, $\operatorname{Var}(F)\le\mathbb E|\nabla F|^2$, follows directly from the Gaussian logarithmic-Sobolev inequality proved in the supplied nonorthogonal-extension Section 3.3: insert $q=1+\delta(F-\mathbb EF)$, expand both sides to order $\delta^2$, and let $\delta\to0$. Here $F$ is smooth and bounded, so the expansion is dominated; positivity holds for sufficiently small $\delta$.

For fixed $T$, (10) applied to the active coefficients gives deterministic bounds on the conditioning event. At passive samples $\bar u_b$ is fixed, so

\[
|\dot{\bar f}_b|
\le\|\dot{\bar w}\|_2/\sqrt n
 +(\|\bar w\|_2/\sqrt n)\|\dot{\bar W}\|_{\rm op}
\le C_T.
\]

A finite time net, Chebyshev's inequality from (16), and then refinement of the net prove the asserted uniform convergence for the finitely many passive samples. Correlations between different passive samples are immaterial to this argument.

Their first-feature Gram converges to the fixed matrix

\[
(Q_{\rm pas})_{bc}
=\mathbb E_{G\sim N(0,I_2)}
 [\tanh(G\cdot x_b^0)\tanh(G\cdot x_c^0)],
\qquad b,c\ge3,
\tag{17}
\]

where the passive plane is identified with $\mathbb R^2$. This matrix is positive definite. Indeed a zero quadratic form would make a linear combination of the ridge functions vanish under the full-support Gaussian law, hence everywhere. Choose a direction whose projections on the finitely many unit inputs are nonzero with distinct squares; restricting to that line and comparing the first $m-2$ odd Taylor coefficients of tanh gives an invertible Vandermonde matrix. This is the complete independence argument in `INTRINSIC_SYMMETRY_ROUTE.md`, Section 4, and uses exactly distinctness and nonantipodality.

The empirical cross-Gram between an active feature and a passive feature tends to zero at each fixed time. Conditional on the active state, its summands are independent centered passive functions, multiplied by bounded fixed active coordinates. Its conditional variance is at most $1/n$. The active first-feature Gram converges by the orthogonal theorem.

At its scalar endpoint that $2\times2$ active Gram is positive definite. Active exchange/sign symmetry makes its eigendirections common and contrast. The common first feature $(u_1+u_2)/2$ is nonzero by the natural-coordinate nonextinction proof in Section 11.3 of the supplied orthogonal theorem. The contrast first feature is nonzero because otherwise $u_1=u_2$, hence $h_1=h_2$, contradicting $g=a>0$. Therefore, with $Q_{{\rm act},*}$ the endpoint active first-feature Gram,

\[
\mu_*:=\min\{\lambda_{\min}(Q_{{\rm act},*}),
                    \lambda_{\min}(Q_{\rm pas})\}>0.
\tag{18}
\]

For all sufficiently late fixed $T$, continuity at the active endpoint and the preceding convergence give

\[
\Pr\{\bar Q_U(T)\succeq(\mu_*/2)I_m\}\longrightarrow1.
\tag{19}
\]

This proves the first-feature gap for the reference without constructing a population flow driven by passive residuals.

## 5. A uniform late reference capture margin

For sufficiently late fixed $T$, active prediction convergence also gives $\|\bar w(T)\|_2/\sqrt n\ge a/2$ with probability tending to one: the finite contrast satisfies

\[
|\bar g_n|=|\bar w^\top(\bar h_1-\bar h_2)/(2n)|
\le\|\bar w\|_2/\sqrt n,
\]

and its limit approaches $a$. On the bounds $\|\bar w\|_\infty\le S$, $\|\bar W\|_{\rm op}\le M$, put $Z_*=\sqrt8SM/a$. Since $\|\bar z_b\|_2/\sqrt n\le M$,

\[
\frac1n\sum_{j:|\bar z_{b,j}|>Z_*}\bar w_j^2
\le S^2M^2/Z_*^2=a^2/8.
\]

The total readout squared mass is at least $a^2/4$, so for every active or passive sample,

\[
\frac{\|\bar b_b\|_2^2}{n}
\ge\beta_*:=\frac{a^2}{8}\operatorname{sech}^4(Z_*)>0.
\tag{20}
\]

The Schur-product identity gives

\[
\bar K_W=\bar Q_U\odot\bar Q_b
\succeq\frac{\mu_*}{2}
 \operatorname{diag}(\|\bar b_b\|_2^2/n)
\succeq\lambda_* I_m,
\qquad \lambda_*:=\mu_*\beta_*/2>0.
\tag{21}
\]

To justify the first inequality, the Hadamard product of two positive semidefinite matrices is the Gram matrix of their tensor-product features; apply this to 
$\bar Q_U-\mu_*I/2$ and $\bar Q_b$.

The constants $S,M,\lambda_*$ are independent of how late $T$ is subsequently chosen. The reference full residual at (1) is bounded by

\[
\|\bar f(T)-y^0\|_2
\le\sqrt2\,a e^{-4q_0T/m}+o_{\mathbb P}(1),
\tag{22}
\]

using active convergence and Section 4.

We recall the deterministic capture criterion with its needed continuity. At a finite state with bounded reference readout supremum $P$, action norm $L$, and $K_{\rm R+W}\succeq\lambda I$, there is a radius $\rho>0$, depending only on $m,P,L,\lambda$ and unit input norms, on whose parameter ball $K_{\rm R+W}\succeq\lambda I/4$. In the canonical metric,

\[
\|\Delta u_b\|_2/\sqrt n\le\|\Delta\theta\|_{\rm par},\qquad
\|\Delta h_b\|_2/\sqrt n\le C\|\Delta\theta\|_{\rm par}.
\]

Writing the backward difference using the reference readout gives the same bound for $\Delta b_b$. Rank-one differences therefore control the tangent-feature matrix by $C\sqrt m\|\Delta\theta\|_{\rm par}$; taking its norm smaller than $\sqrt\lambda/2$ proves the kernel claim. If the center residual is smaller than $\rho\sqrt\lambda/2$, gradient flow cannot leave: while its kernel is at least $\lambda I/4$,

\[
\|\dot\theta\|_{\rm par}
\le-\frac2{\sqrt\lambda}\frac d{dt}\|r\|_2.
\tag{23}
\]

The remaining length is strictly less than $\rho$, and (9) gives exponential loss decay at rate $\lambda/m$. Choose conservative bounds $P=S+1,L=M+1,\lambda=\lambda_*/2$. Equations (19)–(22) choose one fixed sufficiently late $T$ at which the reference satisfies this test with a strict margin, with probability tending to one. This is a margin for subsequent uncut training on all samples.

## 6. Stability of the full perturbed flow needs only active tails

Fix this $T$. Couple the actual system for $X,y$ to the reference by the same Gaussian $A_0,W_0,w_0$. Define

\[
E_n(t)=\|U-\bar U\|_F^2/n
       +\|W-\bar W\|_F^2+\|w-\bar w\|_2^2/n,
\quad \delta=\|X-X^0\|_F+\|y-y^0\|_2.
\tag{24}
\]

On $[0,T]$, both systems obey common bounds on readout supremum, operator norm, normalized backward norms, and loss coefficients, for all sufficiently small fixed $\delta$. For the reference this uses its active loss, not its full evaluated residual. These bounds may depend on $T$, which is now fixed. Forward and upper-backward differences give

\[
\|H-\bar H\|_F/\sqrt n+
\|b-\bar b\|_F/\sqrt n+
\|B-\bar B\|_F/\sqrt n+\|f-\bar f\|_2
\le C_T\sqrt{E_n}.
\tag{25}
\]

The coefficient-vector difference is

\[
r-\widehat r=(f-\bar f)-(y-y^0)
 +(0,0,\bar f_3,\ldots,\bar f_m),
\]

so uniformly on the interval,

\[
\|r-\widehat r\|_2\le C_T\sqrt{E_n}+\delta+q_n(T).
\tag{26}
\]

Also $\|\Gamma-\Gamma^0\|_{\rm op}\le2\sqrt m\|X-X^0\|_F$, since both input matrices have unit columns. In subtracting the first equations of (7), first change the Gram, then the residual coefficients and $B$, and finally the gates against the reference. Equations (25)–(26) bound the first groups and the $W,w$ equations by

\[
C_T[E_n+\delta^2+q_n(T)^2]
\]

in the derivative of $E_n$. The only unbounded gate multiplier that remains is a sum of terms

\[
\Gamma^0_{bc}\widehat r_c
 (D_bD_c-\bar D_b\bar D_c)\bar B_c.
\tag{27}
\]

Every $c\ge3$ term is exactly zero, because $\widehat r_c=0$. Thus only the active reference fields $\bar B_1,\bar B_2$ require tails. On bounded features, 
$|D_bD_c-\bar D_b\bar D_c|\le C(|u_b-\bar u_b|+|u_c-\bar u_c|)$.
Pair (27) with the first-feature difference and split $|\bar B_c|\le2R$. Its low part is at most $C_TR E_n$. On the complement use boundedness of every feature difference and
$|\bar B_c|\mathbf1_{|\bar B_c|>2R}\le2(|\bar B_c|-R)_+$; Cauchy–Schwarz gives

\[
E_n'\le C_T(1+R)E_n+C_T[\delta^2+q_n(T)^2]
 +C_T\sum_{c=1}^2\frac{\|(|\bar B_c|-R)_+\|_2}{\sqrt n}.
\tag{28}
\]

This derivation does not suppress training on passive examples in the actual flow. Their actual residuals enter (26) and all the ordinary difference terms. Their backward fields need only the operator/readout $L^2$ bound.

Initially $W,w$ agree. Since tanh is 1-Lipschitz and $A_0^\top A_0/n\to I_4$,

\[
E_n(0)\le\|A_0(X-X^0)\|_F^2/n\le2\delta^2
\tag{29}
\]

with probability tending to one. Gronwall, (15), and (28) give, for every fixed $R\ge1$,

\[
\sup_{t\le T}E_n(t)
\le C_Te^{C_TR}
 [\delta^2+q_n(T)^2+e^{-c_TR^2}]
\tag{30}
\]

with probability tending to one. Since $q_n(T)\to0$, this yields arbitrary prescribed accuracy by first choosing a finite large $R$, then a fixed small $\delta>0$, then width large. It is not an appeal to finite-width continuity with a neighborhood shrinking with $n$.

## 7. Transfer of the capture margin and proof of the theorem

On the finite comparison bounds, (25) and the rank-one identity show that the actual and reference predictions and $K_{\rm R+W}$ differ by at most $C_T\sqrt{E_n}$. The sharp readout/action bounds needed for capture follow from the accumulated residuals, rather than from bounds growing with $T$. Indeed, (26) and $\bigl||r_b|-|\widehat r_b|\bigr|\le|r_b-\widehat r_b|$ give

\[
|p_n(T)-\bar p_n(T)|
\le C_T\left[\sup_{t\le T}\sqrt{E_n(t)}+\delta+q_n(T)\right].
\tag{31}
\]

Equations (10) and (14) then put the actual snapshot within the conservative bounds $S+1,M+1$ when the comparison error is small enough. Explicitly, $\bar p_n(T)\le s_*+1/2$ with probability tending to one; making the right side of (31) less than $1/2$ gives $p_n(T)\le S$, hence even the stronger action bound $\|W(T)\|_{\rm op}\le10+S^2/2=M$. Its residual differs from the small reference residual by at most $C_T\sqrt{E_n}+\delta$; its tangent gap remains above $\lambda_*/2$ if that error is sufficiently small.

The reference capture inequalities were strict. Choose an error tolerance preserving all of them; choose $R$ in (30) so its Gaussian-tail contribution is below half that tolerance; then choose a fixed positive neighborhood radius $\varepsilon$ so its $\delta^2$ contribution and (31) preserve the remaining margin. Finally let $n\to\infty$. The reference convergence events, Gaussian-tail event, and comparison event hold jointly with probability tending to one, since there are finitely many events.

The actual full finite-width flow is then in the deterministic capture ball at $T$. Formula (23) and exact loss dissipation control its entire infinite future and give (5)–(6), with a deterministic rate such as $c=\lambda_*/(2m)$. The width limit was used only on the single finite interval $[0,T]$.

Finally decrease $\varepsilon$, if necessary, so unit-column configurations in the neighborhood retain distinctness and nonantipodality and the first two label signs. The finitely many base distances to coincidence and antipodality are positive, so this reduction leaves a positive radius. The intersection with the set where all passive labels are nonzero is nonempty and open, for example by choosing their fixed magnitudes sufficiently small with any prescribed signs. This completes the candidate proof.

## Dependencies and remaining review obligations

The theorem is unconditional relative to the complete supplied orthogonal-pair proof and its active Gaussian-tail proof. It adds no population-existence or dynamical-tail premise for correlated inputs. The critical new identities are (26)–(28): the reference's inactive coefficients vanish, so its passive backward tails never enter the stability estimate. The passive reference predictions vanish by the conditional calculation (16), and its full first-feature gap follows from (17)–(19).

Scientific source versions are the hashes recorded in `UNCONDITIONAL_POPULATION_ROUTE.md`: `GAUSSIAN_POSITIVE_GEOMETRY.md`, `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, and `INTRINSIC_SYMMETRY_ROUTE.md`. The fixed-program/operator facts are complete maintained III.F.1–11 already read in this attempt. The subsequent discarded cluster exploration also read complete maintained C.1–C.2 in `docs/03-local-population.qmd`; no result from that exploration is a dependency of this proof. No input from another study, frozen archive, external paper, or another agent's draft was used.

Independent review should check the active-pair endpoint first-feature gap, the distinction between $\widehat r$ and the full evaluated reference residual, the normalization $2/m$, and the fact that (28) uses tails only for active reference indices. No staging, commit, or edits outside this assigned file were performed for this extension.
