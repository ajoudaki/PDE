# A fitted q=1 predictor can retain a test-visible readout history

Root derivation, 2026-09-30. Claim type: exact finite-dimensional theorem.
Check status is recorded separately in README.md and ENDPOINT_HISTORY_CHECK.md.
This is study research, not an established manuscript or book result.

## 1. Question, model and result

The question left open by ROTATING_FEATURE_SPAN.md is whether its transient
training-invisible readout can survive at an actual fitted endpoint. Here it
does, on an open set of initializations. The result concerns one training
input and two neurons in each of two hidden layers. It neither assumes nor
proves general multi-input fitting or a beneficial test-risk comparison.

Use exactly the manuscript's learning-speed closure at q=1, with tanh,
zero biases, n=2, m=1, d=2, x_train=sqrt(2)e_1 and y=1. Write
A=[a,beta], where a,beta are columns. For the training input set

\[
h=\tanh a,\quad B=W_0+vk^T/2,\quad g=\tanh(Bh),\quad
f=w^Tg/2,\quad d=w\odot(1-g^2).
\]

The original physical-time equations are

\[
\dot w=2(1-f)g,\quad \dot v=2(1-f)d,\quad
\dot a=2(1-f)(1-h^2)\odot B^Td,\quad \dot\beta=0,
\]
\[
\dot k=|1-f|(h-k)/\tau,\quad \dot\tau=|1-f|,
\qquad w(0)=v(0)=0,\ k(0)=h(0),\ \tau(0)=1.
\tag{1}
\]

Thus B is a reconstruction, never an independently trained matrix. The
manuscript mapping is A=W^(1), k=bar h_{1,0}/tau, v=-2 bar delta_{1,0}.
All factors 2 and n=2 are retained; physical time is not rescaled in (1).

**Theorem.** Choose the finite initialization

\[
W_0=\begin{pmatrix}1&0\\0&10\end{pmatrix},\qquad
A_0=\begin{pmatrix}1/2&1\\1&0\end{pmatrix}.
\tag{2}
\]

Then the actual q=1 trajectory has a finite limiting state, interpolates its
training label, and its loss decays exponentially. At that endpoint, writing
g_* for the training feature and P_*=g_*g_*^T/\|g_*\|^2,

\[
w_{\perp,*}=(I-P_*)w_*\ne0.
\tag{3}
\]

Its extra prediction at the fixed unseen circle input x_q=sqrt(2)e_2 is
strictly negative:

\[
\frac12g_*(x_q)^Tw_{\perp,*}<0.
\tag{4}
\]

In fact the fitted classifier differs on an open arc from the minimum-norm
interpolating readout using these same final features. All of these properties
persist on a nonempty open neighborhood of (A_0,W_0). Consequently they have
positive probability under independent A_ij(0)~N(0,1) and W_0,ij~N(0,1/2).
No lower bound on that probability, or typical-width conclusion, is asserted.

The proof uses finite parameters throughout. The second neuron is strongly
but finitely saturated; its derivative and every memory variable continue to
follow (1). No frozen-neuron or limiting-activation model is substituted.

## 2. Feature time and an all-time cooperation lemma

Here first allow any finite n and a single normalized training input, y=1.
Write B=W_0+vk^T/n. Suppose a(0)>0 coordinatewise, W_0 is entrywise
nonnegative, and g(0)=tanh(W_0 tanh a(0))>0 coordinatewise. While f<1, set

\[
s=2\int_0^t(1-f(u))\,du,\qquad \tau=1+s/2.
\]

It is useful first to solve the following regular auxiliary ODE in s, even
beyond its first fitting point. A prime denotes d/ds only in Sections 2--5:

\[
w'=g,\quad v'=d,\quad a'=(1-h^2)\odot B^Td,\quad
k'=(h-k)/(2+s),\quad h=\tanh a,
\tag{5}
\]
\[
B=W_0+vk^T/n,\quad g=\tanh(Bh),\quad d=w\odot(1-g^2).
\]

This auxiliary extension is not the physical continuation past zero residual.
Only its segment ending at the first crossing F(s)=w(s)^Tg(s)/n=1 will be
used to construct the physical solution.

The region w,v>=0 and h>=k>=h(0)>0 is invariant. Indeed B is nonnegative;
w',v',a' are nonnegative there, and at h_i=k_i,
(h_i-k_i)'=h_i'>=0. At the lower face k_i=h_i(0), its derivative is
nonnegative. More explicitly the key solves

\[
k(s)=\frac{2h(0)+\int_0^s h(u)\,du}{2+s}.
\tag{6}
\]

Thus h,k,w,v are coordinatewise nondecreasing; B and Bh, and hence g, are
also nondecreasing. On every finite s interval,

\[
0\le w_i\le s,\quad 0\le v_i\le s^2/2,\quad 0<k_i\le h_i<1,
\]
\[
0\le a_i'\le s\sum_j(W_0)_{ji}+s^3/2.
\tag{7}
\]

The last bound uses d_j<=s and
(k_i/n)sum_j v_j d_j<=s^3/2. All state components therefore remain bounded
on finite intervals. Local existence and uniqueness follow from the smooth
vector field on s>-2; these bounds permit its continuation to every s>=0.

Define c_0=\|g(0)\|^2/n>0. Positivity and monotonicity give

\[
F'(s)=\frac{\|g(s)\|^2+w(s)^Tg'(s)}n\ge c_0,
\qquad c_0s\le F(s)\le s.
\tag{8}
\]

There is therefore a unique finite s_* with F(s_*)=1, and
1<=s_*<=1/c_0. Solve sdot=2(1-F(s)), s(0)=0 on [0,s_*).
The simple root and local uniqueness prevent finite-time arrival or crossing.
Monotonicity and (8) imply s(t) increases to s_*: a smaller limit would leave
sdot bounded positively away from zero. Substitution of this s(t) into (5),
with tau=1+s/2 and beta fixed, solves exactly (1). If e=1-F(s(t)), then

\[
\dot e=-2F'(s(t))e\le-2c_0 e,\qquad
\mathcal L(t)=e(t)^2\le e^{-4c_0t}.
\tag{9}
\]

All physical states converge to their finite values at s_*. This proves
fitting and convergence, without assuming either. The ODE construction and
the local Lipschitz property of (1) also identify it as the actual solution.

This lemma explains sustained cooperation in a restricted population cone.
Current features, historical keys and writes reinforce one another. It does
not assert that arbitrary Gaussian matrices or multiple inputs stay in it.

## 3. A strictly signed endpoint determinant

Return to (2) and n=2. Write g=(g_1,g_2),

\[
\gamma=\tanh(\tanh(1/2)),\quad
\eta=\tanh(10\tanh1),\quad
\varepsilon=1-\eta,\quad \delta=\operatorname{sech}^2(10\tanh1).
\]

By (8), 1<=s_*<=2/(gamma^2+eta^2)<=2/eta^2<4. Throughout the
trajectory g_2>=eta. Define

\[
D=w_{1,*}g_{2,*}-w_{2,*}g_{1,*}
 =\int_0^{s_*}[g_1(u)g_{2,*}-g_2(u)g_{1,*}]\,du.
\tag{10}
\]

For each integrand, g_{2,*}<=1 and g_2(u)>=1-epsilon give

\[
D\le-\int_0^{s_*}[g_{1,*}-g_1(u)]\,du+s_*\varepsilon.
\tag{11}
\]

The negative term records that the first neuron's final response exceeds its
past responses. We bound it away from zero; a transient Taylor expansion is
not used.

For 0<=s<=1, (7) gives a_1(s)<=1/2+s^2/2+s^4/8<=9/8.
Also z_1=h_1+v_1(k^Th/2)<=1+s^2/2<=3/2. Since all terms are
nonnegative,

\[
z_1'\ge h_1',\quad
h_1'=(1-h_1^2)^2[d_1+k_1(v^Td)/2]\ge(1-h_1^2)^2d_1,
\]
\[
w_1(s)=\int_0^s g_1(u)\,du\ge s\gamma.
\]

Consequently

\[
g_1'(s)\ge s\gamma(1-h_1^2)^2(1-g_1^2)^2\ge Cs,
\quad C=\gamma\operatorname{sech}^4(9/8)
                   \operatorname{sech}^4(3/2)>0.
\tag{12}
\]

Integrating in the triangular region 0<=u<=v<=s_* yields

\[
\int_0^{s_*}[g_{1,*}-g_1(u)]\,du
=\int_0^{s_*}u g_1'(u)\,du\ge\int_0^1 Cu^2\,du=C/3.
\tag{13}
\]

The elementary bounds

\[
\gamma>1/3,\quad \cosh(9/8)<2,\quad \cosh(3/2)<3,
\quad \tanh1>3/4,\quad e^{15}>2\cdot10^6
\tag{14}
\]

imply C>1/3888 and epsilon<2e^(-15)<10^(-6). Hence

\[
D<-\frac1{11664}+\frac4{10^6}<0.
\tag{15}
\]

For explicit verification of (14), e>8/3 and e<11/4 follow by lower and
upper bounds on its positive power series. Then tanh(1/2)>2/5 and
exp(4/5)>1+4/5+(4/5)^2/2>2 imply gamma>1/3.
The lower e bound gives tanh1>3/4 and e^15>(8/3)^15>2*10^6.
For the cosh bounds, exp(6/5)<(11/4)/(1-1/5)=55/16 and
exp(-6/5)<1/2 imply cosh(9/8)<cosh(6/5)<2.
Also sqrt(e)<5/3 gives exp(3/2)<55/12, so cosh(3/2)<(55/12+1)/2<3.
These are elementary inequalities, not measured training quantities.

The two-dimensional projection formula is

\[
w_{\perp,*}=\frac{D}{\|g_*\|^2}(g_{2,*},-g_{1,*})^T.
\tag{16}
\]

Thus (15) proves nonzero persistence at the fitted endpoint. In particular
w_{1,*}/w_{2,*}<g_{1,*}/g_{2,*}. The readout contains the accumulated past
ratio of responses, which need not equal their final ratio.

## 4. It changes unseen predictions and classification

Because beta=(1,0)^T is unchanged, the query x_q=sqrt(2)e_2 has
h(x_q)=(tanh1,0)^T at every time. Therefore

\[
g_1(x_q)=\tanh[(1+v_1k_1/2)\tanh1]>1/2,
\quad 0\le g_2(x_q)\le v_2/2.
\tag{17}
\]

Since z_2=10h_2+v_2(k^Th/2)>=10tanh1, one has
v_2'=w_2(1-g_2^2)<=s delta. Thus v_{2,*}<=s_*^2 delta/2<8delta,
and delta<4e^(-15)<2*10^(-6). It follows that

\[
g_1(x_q)g_{2,*}-g_2(x_q)g_{1,*}
>\frac38-8\cdot10^{-6}>0.
\tag{18}
\]

Combining (16), (18) and D<0 proves (4). In one-input notation the complete
endpoint decomposition is

\[
f_*(x)=\frac{g_*^Tg_*(x)}{\|g_*\|^2}
       +\frac{g_*(x)^Tw_{\perp,*}}2.
\tag{19}
\]

The first term uses the unique minimum-Euclidean-norm fitting readout
w_min=2g_*/\|g_*\|^2, because g_*^Tw_*=2 and orthogonal projection gives
P_*w_*=w_min. Both terms use the same final feature map.

There is a classification consequence without specifying a test truth.
At the endpoint det A_*=-a_{2,*}<0 and

\[
\det B_*=10+5v_{1,*}k_{1,*}+v_{2,*}k_{2,*}/2>0.
\tag{20}
\]

Invertibility and tanh(u)=0 iff u=0 imply g_*(x)!=0 for every nonzero x.
Since w_* and w_min are not parallel, their perpendicular lines in R^2
intersect only at zero. Therefore an actual classifier zero on the circle
cannot also be a minimum-norm classifier zero. The actual circle function
is real analytic, equals 1 at the training input and -1 at its antipode.
Its zeros are isolated (a nonisolated analytic zero would force the function
to vanish identically), hence finite on the circle. At least one zero between
those inputs changes sign. At that zero the minimum-norm function is nonzero
and keeps its sign in a neighborhood. On one side the actual classifier has
the opposite sign. The classifiers therefore disagree on an open arc, of
strictly positive uniform-circle measure.

This proves selection of a different boundary, not improvement relative to
an unknown true boundary. It makes no minimum-norm comparison across
different feature maps and no maximum-margin claim.

## 5. Why this is an open-set Gaussian event

Finite-time continuity alone would not imply continuity of arbitrary
infinite-time endpoints. Here the transverse crossing in feature time supplies
the missing argument.

Let p=(A_0,W_0). At the witness p_0, choose a finite S>s_* with F(S)>1.
The reference solution of (5) is bounded on [0,S] and F'>=c_0 there.
The smooth vector field and its first state/parameter derivatives are bounded
on a compact tube around this path. For nearby p, subtracting integral
equations gives a bound of the form

\[
\sup_{s\le S}\|U(s;p)-U(s;p_0)\|
\le C\|p-p_0\|e^{CS},
\]

up to first exit; choosing p sufficiently close excludes exit. Thus solutions
exist on [0,S] and depend continuously on p there, including F and F'.
Shrinking the neighborhood gives F'(s;p)>=c_0/2 and F(S;p)>1, while
F(0;p)=0. Each nearby path has a unique crossing s_*(p), and the slope bound
implies continuity of that crossing (a uniform perturbation epsilon in F
moves it by at most 2epsilon/c_0). Endpoint states are therefore continuous.

For these nearby states, even if some W_0 entries are negative, the same
construction sdot=2(1-F(s;p)) stays below the crossing and converges to it.
Equation (9) holds with c_0/2, proving physical fitting and convergence there.
The strict signs (15), (18) and nonzero determinants (20) persist. Hence so do
the nonzero extra query prediction and the classification disagreement.
Gaussian densities are strictly positive everywhere on the finite entries of
(A_0,W_0), so this open neighborhood has positive probability. A smaller open
ball with strictly positive off-diagonal entries also exists if desired.

## 6. What changes in the research state

The possibility of endpoint persistence is now proved by a finite, initialized
q=1 trajectory and an open neighborhood. Universal cancellation and universal
minimum-norm readout selection using final features are false in this model.
The old transient result remains valid, but its endpoint gap is closed for
this class. The general frequency, size, sign and predictive usefulness of
the historical term, especially for multiple genuinely distinct training
directions, remain open.

The mechanism is unequal sustained feature reinforcement: the growing first
response leaves a measurable gap between its historical average and final
value, while the second response changes too little to cancel that gap.
The exact error-driven writes, evolving keys and moving first layer are all
present. The theorem does not identify this phenomenon as exclusive to
response memory, or isolate which memory component is necessary for it.

Scientific inputs: the complete current paper/main.tex and its two included
appendices; docs/index.qmd and docs/notation.qmd; this study's README,
SYNTHESIS, complete ENERGY_ROUTE/CHECK, PREDICTOR_ROUTE,
ROTATING_FEATURE_SPAN/CHECK and SCALAR_CIRCLE_SELECTION/CHECK. No other study,
archived book, external theorem dependency or training experiment was used.
The derivation above is self-contained in (1)--(20); prior notes supply the
question and interpretation, not an unproved endpoint premise.
