# Retaining individual memory modes in a scalar continuation

2026-10-01. New theoretical continuation prompted by the question whether
retaining information from the lower memory modes can improve scalarization.
No new training or numerical experiment is part of this note. This is a
candidate approximation with exact structural properties, not an empirical
improvement over the completed frozen-response experiments.

Scientific inputs: this study's HIGHER_ORDER_SCALAR.md and terminal theorem,
and the same unchanged current manuscript (SHA256
fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605).
The following finite-width model uses the actual learning-speed clock and
mode normalization. No other study is an input.

## 1. What depends on the memory order

At dimension two, the full order-q state has 3n+2qnm+1 moving scalars and
the fixed n-by-n mixer. The tested terminal evaluator has 17 moving and
712 fixed numbers for m=8 and its specified Fourier cutoff, for every q.
That independence comes from retaining only the total prediction-response
coefficients. It is a choice of approximation, not an assertion that the
higher modes have no useful information.

Mode zero inside a q=2 run was driven by the q=2 features throughout
training. It is generally different from mode zero in a separately trained
q=1 run. The construction below retains all modes of one reached q=2
state. It does not combine independently evolved closure trajectories.

Exactly in q=2, put k*=k_0+3k_1, v*=v_0+3v_1, and alpha=rho/tau.
The manuscript's mode equations give

    k*_dot = alpha (4h - 2k* - 2k_0),
    v*_dot = -8r d - alpha (v* + 2v_0).

Thus the endpoint sums used in the total response do not themselves
determine their next velocities. Separately retaining lower-mode
information is mathematically relevant to predicting changing responses.

## 2. Exact scalar construction at q=2

Reset physical time to zero at a reached handoff. For every training
example a and query x, all neural fields in the following fixed coefficients
are evaluated in the full q=2 network at that handoff. Use the established
fields h,g,d,ell, normalized input u=x/sqrt(dimension), and width n.

Define the fixed scalar contractions

\[
H(x,a)=h_x^Th_a/n,\qquad D(x,a)=d_x^Td_a/n,
\]
\[
C_{\rm outer}(x,a)=\frac2m\left[g_x^Tg_a/n
+(u_x^Tu_a)\ell_x^T\ell_a/n\right],
\]
\[
U_j^0(x,a)=h_x^Tk_{a,j}^0/n,\qquad
V_j^0(x,a)=d_x^Tv_{a,j}^0/n,\qquad j=0,1.
\]

U and V in this note are scalar contractions, not retained neuron vectors.
Also retain the initial training residuals r^0, the initial query outputs
f_x^0, and the handoff clock tau_0>0. Evolve only the m-vectors I,J and
the clock tau, starting at I=J=0 and tau=tau_0:

\[
\dot I_a=\widehat r_a,\qquad
\dot J_a=\widehat r_a-\frac{\widehat\rho}{\tau}J_a,
\qquad \dot\tau=\widehat\rho,
\qquad \widehat\rho=\|\widehat r\|/\sqrt m.
\tag{1}
\]

The residual is defined algebraically below, so (1) is autonomous. Put
s=tau_0/tau and reconstruct these scalar contractions:

\[
U_0=H+s(U_0^0-H),
\qquad U_1=s^2U_1^0+(s^2-s)(U_0^0-H),
\tag{2}
\]
\[
V_0=V_0^0-2D I_a,
\qquad V_1=sV_1^0+(s-1)V_0^0+2D I_a-4D J_a.
\tag{3}
\]

Every quantity in (2)--(3) has the same query/example indices (x,a).
The shared controls I_a,J_a do not acquire a query index. Define

\[
\widehat f_x=f_x^0-\sum_a C_{\rm outer}(x,a)I_a
+\frac1m\sum_a
\left[U_0V_0+3U_1V_1-U_0^0V_0^0-3U_1^0V_1^0\right].
\tag{4}
\]

At training queries, set rhat_a=fhat_(x_a)-y_a. In implementation one can
use the same expression with r_a^0 in place of f_(x_a)^0, so no labels
need to be queried after the handoff.

The approximation freezes the handoff neural fields and output Jacobian,
but transports the stored memories under its own residual and clock. It
retains both mode zero and mode one separately. It is not the exact full
q=2 model and is not a continuation from random initialization.

## 3. Derivation, initial matching, and stopping

With frozen neural fields, the exact projected memory equations are

\[
\dot U_0=\alpha(H-U_0),\quad
\dot U_1=\alpha(H-U_0-2U_1),
\]
\[
\dot V_0=-2D\widehat r_a,\quad
\dot V_1=-2D\widehat r_a-\alpha(V_0+V_1),
\quad \alpha=\widehat\rho/\tau.
\tag{5}
\]

Since s_dot=-alpha s, differentiating (2) verifies the first two
equations. From (1), I_a=integral rhat_a and
J_a=tau^{-1} integral tau(t)rhat_a(t)dt. Substitution into (3) verifies
the last two equations, with all initial values correct.

For clarity, the mode-one value formula follows by multiplying its ODE
by tau and using integration by parts:

    (tau V_1)' = -2D tau rhat_a - tau_dot V_0^0
                 + 2D tau_dot I_a,
    integral tau_dot I_a = tau I_a - integral tau rhat_a.

The factor 4 in (3) is necessary. There is no division by the residual.

Using (5), the derivative of the memory product is exactly

\[
\frac{d}{dt}(U_0V_0+3U_1V_1)
=-2D\widehat r_a(U_0+3U_1)
+\alpha(V_0+3V_1)(H-U_0-3U_1).
\tag{6}
\]

Thus differentiating (4) gives the same response formula as the actual
q=2 system, evaluated with frozen neural fields and the transported
individual memories. The outer contribution is exactly the handoff output
Jacobian applied to the frozen readout and read-in update directions.
At time zero, every contraction equals the full handoff contraction.
Consequently both output and output velocity agree with the actual
q=2 model for every represented query, before any query-basis error.

If rhat=0, then rhohat=0 and every component of (1) stops. The query
predictions stop as well. This is a stationary-state property, not a
guarantee that zero residual will be reached.

## 4. Global finite-time existence of this scalar proxy

For arbitrary finite fixed coefficients and tau_0>0, the right-hand side
is locally Lipschitz on tau>0. On its maximal forward solution tau is
nondecreasing, so 0<s<=1. The U coefficients in (2) are bounded there.
Equations (3)--(4) show that rhat is affine in (I,J), with coefficients
bounded uniformly for s in [0,1]. Thus for a finite coefficient-dependent
constant K,

\[
\|\widehat r\|\le K(1+\|(I,J)\|).
\]

For E=||I||^2+||J||^2,

\[
\dot E=2(I+J)^T\widehat r-2\alpha\|J\|^2
\le K_1(1+E)
\]

for a finite K_1, by Cauchy--Schwarz and the preceding affine bound.
Integrating gives E(t)+1 <= (E(0)+1)exp(K_1 t). The clock derivative is
then bounded on every finite interval, while tau>=tau_0. No finite-time
escape or approach to tau=0 is possible, so local uniqueness extends to
every finite physical time. This does not prove bounded states as t tends
to infinity, fitting, or approximation of the full closure.

## 5. What benefit is demonstrated, and what is not

The new construction retains all the memory transport in (5). The tested
frozen-C,b evaluator does not retain that motion. The remaining exact
full-model equations have terms

    U_j_dot = retained transport + h_x_dot^T k_(a,j)/n,
    V_j_dot = retained transport + d_x_dot^T v_(a,j)/n,

and time-varying H,D,C_outer. These omitted changes in neural fields can
be as important as the transported memories. Correcting one source of
error can also undo a cancellation with another source. Therefore neither
a better error constant nor a higher error order follows automatically.

There is a simple exact local example showing that this retained motion
can matter. It is an arbitrary admissible restart state, **not a claimed
state reached from the prescribed random initialization**. Take n=m=1,
q=2, label +1, one unit normalized input, h=tanh(a) nonzero, W0=0,
w=1, all keys and values zero, and tau=1. One may embed the input in
the circle by taking u=(1,0). Then B=g=ell=f=0, d=1, r=-1, rho=1.
The frozen response has C=b=0 and predicts f identically zero. In the
actual full closure, initially

    k_0_dot=k_1_dot=h,  v_0_dot=v_1_dot=2,
    A_dot=w_dot=B_dot=0,  B_ddot=16h,  f_ddot=16h^2.

Hence the true output is 8h^2 t^2+O(t^3). Equations (1)--(4) reproduce
that same second derivative, while the frozen-response evaluator misses
it. All vector fields are smooth near r=-1, so the new local output error
is O(t^3), versus a nonzero leading O(t^2) term for the old evaluator.
This demonstrates a particular missing mechanism. It supplies no fitting
or accuracy guarantee for the initialized circle experiments, no open-set
Gaussian reachability claim, and no improvement theorem near every fitted
endpoint.

Under additional terminal tube, speed, coefficient-Lipschitz, contraction
and small-tail certificates for both the full closure and this proxy,
each can be compared to the common frozen response at the handoff. For
query estimates include the theorem's query coefficient bounds as well.
The existing theorem and the triangle inequality then give residual and
query bounds proportional to R^2 and a loss bound proportional to R^3,
where R is the handoff residual norm. These are asymptotic error orders
along a family with R tending to zero only if the certified constants
stay bounded and the contraction margin stays bounded away from zero.
This conditional route alone gives the same orders as the original
construction, not an improved order. No certificate is asserted here
for the recorded training trajectories.

## 6. Extension to fixed q, counts, and query storage

Let T have diagonal entries T_jj=j and lower entries T_ji=2i+1 for
i<j, with all upper entries zero. Its distinct eigenvalues 0,...,q-1
make it diagonalizable for each finite q. The value homogeneous transport
is a finite linear combination of powers (tau_0/tau)^j, 0<=j<q.
The forward homogeneous transport uses T+I and powers with 1<=j<=q;
its fixed h forcing also adds a constant term. The value residual
forcing can therefore be expressed using the qm controls

\[
Z_{a,j}=\tau^{-j}\int_0^t\tau(s)^j\widehat r_a(s)\,ds,
\qquad \dot Z_{a,j}=\widehat r_a-j\alpha Z_{a,j},
\quad 0\le j<q.
\]

Along with tau, this gives qm+1 moving scalars; q=2 uses Z_0=I,Z_1=J.
The diagonalization depends only on q, not on a future trajectory. The
same affine-residual and nonpositive damping argument gives finite-time
well-posedness for every fixed q. Conditioning and constants may worsen
with q; no uniform-in-q approximation estimate is proved.

For training-only evaluation, retaining U_j^0,V_j^0,H,D,C_outer,r^0,tau_0
uses (2q+3)m^2+m+1 fixed numbers, before exploiting any symmetries. For
m=8,q=2 this is 457 fixed numbers plus 17 moving controls. The q1/q2/q3
moving counts of this proposed formulation are 9/17/25. These are counts
for this formulation, not new compression claims about the already
implemented 17-state residual/integral evaluator.

Each query additionally requires its initial prediction and
(2q+3)m fixed scalar contractions. An entire circle therefore needs a
separate finite representation of these functions and a separate error
bound. This overhead can be substantially greater than the previous ten
query functions. In particular, H,U_j,C_outer and f^0 are odd under
x -> -x, but D and V_j are even. The old odd-only Fourier representation
cannot be reused indiscriminately. Keeping full neural arrays to evaluate
these functions after handoff would defeat the scalar-storage claim.

The proposed q-dependent retained information is a real tradeoff to test,
not a demonstrated efficient replacement for the existing 729-number
circle model. No numerical accuracy, improved size/error law, or
sublinear-width result is asserted for it.

## 7. Separately trained q1 and q2 models

Keeping both independently evolved scalar models is possible, but does
not automatically determine a better dense approximation. If both fit
the training labels exactly, every affine mixture
(1-c)f_q1+c f_q2 also fits those same labels. Training fit therefore
cannot select c by itself, while predictions on unseen inputs may change.
A justified extrapolation requires a proved error relation or independent
validation information. Increasing q alone does not supply that relation;
the completed experiments already show nonmonotone endpoint errors.

This is distinct from retaining lower modes of one higher-order state,
whose exact transport equations are available and used above.

## Check status and reproduction

Root derived the q2 construction and the local restart example. Scoped
agents scalar_aggregate and scalar_control derived the same transport
construction and identified the scope and query-storage issues. These
were cooperative calculations within this study, not fresh isolated
promotion reviews. A separate internal check of the frozen note is
recorded in MEMORY_TRANSPORT_SCALAR_CHECK.md when available.
Reproduction is by substitution into (5), product differentiation in (6),
the displayed energy estimate and the explicit restart-state derivatives.
No numerical experiment, manuscript edit, or Git write was performed.
