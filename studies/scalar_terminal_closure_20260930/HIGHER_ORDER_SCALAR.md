# The same terminal scalar construction for every finite memory order

Derived 2026-09-30 from the current manuscript, not from a higher-order
analogy. This is an exact finite-width identity followed by a conditional
terminal approximation. Internal algebra/proof check:
[HIGHER_ORDER_SCALAR_CHECK.md](HIGHER_ORDER_SCALAR_CHECK.md).
Numerical testing is separately specified in
[HIGHER_ORDER_EXPERIMENT_PLAN.md](HIGHER_ORDER_EXPERIMENT_PLAN.md).

## What changes, and what does not

The manuscript's order q counts shifted-Legendre modes 0 through q-1.
Order two retains modes 0 and 1; order three also retains mode 2. The full
closure therefore stores more forward and backward memory coordinates.
Nevertheless its exact prediction velocity has the same scalar response
form at every fixed order. At a terminal handoff we freeze those response
coefficients and use precisely the previous scalar ODE. No new evolving
scalar coordinates are needed just because q increases.

The reason is a cancellation among the mode-dilation terms: the derivative
of the reconstructed middle matrix depends on two endpoint sums of the
memories. Its value still depends on every matched pair of modes. These
are distinct assertions. The endpoint sums do not give an exact smaller
autonomous closure for the complete network.

## Exact model and reconciliation with the manuscript

Use two tanh hidden layers, m examples, width n, input normalization
u=x/sqrt(d), and the same moving A and w as before. All fields below use
the actual order-q reconstructed middle matrix B:

\[
h(x)=\tanh(Au),\quad g(x)=\tanh(Bh(x)),\quad f(x)=w^Tg(x)/n,
\]
\[
d(x)=w\odot(1-g(x)^2),\qquad
\ell(x)=(1-h(x)^2)\odot B^Td(x).
\]

Residual r_a=f(x_a)-y_a, loss L=sum_a r_a^2/m, rho=sqrt(L),
tau_dot=rho and tau(0)=1. The manuscript's unnormalized forward and
backward moments are bar h_(a,j), bar delta_(a,j). Define, for j=0,...,q-1,

\[
k_{a,j}=\bar h_{a,j}/\tau,\qquad v_{a,j}=-2\bar\delta_{a,j}.
\]

This uses exactly the q=1 study convention at j=0. Substituting into the
manuscript's moment equations gives

\[
\dot k_{a,j}=\frac{\rho}{\tau}
\left[h_a-(j+1)k_{a,j}-\sum_{i<j}(2i+1)k_{a,i}\right],
\tag{1}
\]
\[
\dot v_{a,j}=-2r_a d_a-\frac{\rho}{\tau}
\left[jv_{a,j}+\sum_{i<j}(2i+1)v_{a,i}\right].
\tag{2}
\]

The reconstructed matrix and outer-layer velocities are

\[
B=W_0+\frac1{mn}\sum_{a,j}(2j+1)v_{a,j}k_{a,j}^T,
\tag{3}
\]
\[
\dot w=-\frac2m\sum_a r_a g_a,\qquad
\dot A=-\frac2m\sum_a r_a\ell_a u_a^T.
\tag{4}
\]

Initialization is w=0, every v_(a,j)=0, k_(a,0)=h_0(x_a), and
k_(a,j)=0 for j>=1. This is the paper's unit constant forward prefix and
zero backward prefix, not q identical copies of the initial feature.
The mixing matrix W0 remains fixed and its true transpose is used.

For clarity, the additional q=2 equations are

\[
\dot k_{a,1}=\frac{\rho}{\tau}(h_a-k_{a,0}-2k_{a,1}),\qquad
\dot v_{a,1}=-2r_ad_a-\frac{\rho}{\tau}(v_{a,0}+v_{a,1}).
\]

For q=3 the third mode obeys

\[
\dot k_{a,2}=\frac{\rho}{\tau}(h_a-k_{a,0}-3k_{a,1}-3k_{a,2}),
\]
\[
\dot v_{a,2}=-2r_ad_a-\frac{\rho}{\tau}(v_{a,0}+3v_{a,1}+2v_{a,2}).
\]

The lower mode equations retain the same form, but their current fields
come from the order-q network; one cannot append modes to a saved q=1
trajectory and call that an independently evolved q=2 or q=3 closure.

## The cancellation

Introduce only the two endpoint sums

\[
k_a^*=\sum_{j<q}(2j+1)k_{a,j},\qquad
v_a^*=\sum_{j<q}(2j+1)v_{a,j}.
\tag{5}
\]

For q=2 these are k_0+3k_1 and v_0+3v_1. For q=3 they are
k_0+3k_1+5k_2 and v_0+3v_1+5v_2. The manuscript's forward endpoint
projection is k_a^*, and its backward endpoint projection is
-v_a^*/(2 tau). These sums need not be convex averages or bounded features.

For a fixed example, collect the mode vectors as columns K and V. Let
c_j=2j+1, D=diag(c), and T have diagonal T_jj=j and entries T_ji=c_i
when i<j. Equations (1)--(2) are

\[
\dot K=\frac{\rho}{\tau}[h\mathbf1^T-K(T+I)^T],\quad
\dot V=-2rd\mathbf1^T-\frac{\rho}{\tau}VT^T.
\]

The finite matrix identity

\[
T^TD+DT+D=cc^T
\tag{6}
\]

holds entrywise: on the diagonal, (2j+1)c_j=c_j^2; off the diagonal
the sole nonzero triangular contribution is c_i c_j. Differentiating
VDK^T and applying (6) gives

\[
\frac{d}{dt}(VDK^T)
=-2rd(k^*)^T+\frac{\rho}{\tau}v^*(h-k^*)^T.
\]

Summing over examples proves the exact identity

\[
\dot B=-\frac2{mn}\sum_a r_ad_a(k_a^*)^T
 +\frac{\rho}{mn\tau}\sum_a v_a^*(h_a-k_a^*)^T.
\tag{7}
\]

It agrees with the manuscript's differentiated projection formula without
dividing by rho, including at zero residual. Setting q=1 gives exactly
the previously checked q=1 expression.

## Exact scalar response and terminal evaluator

For any fixed query x, define the scalar response coefficients

\[
C(x,a)=\frac2m\left[
\frac{g(x)^Tg_a}{n}
+(u^Tu_a)\frac{\ell(x)^T\ell_a}{n}
+\frac{d(x)^Td_a}{n}\frac{h(x)^Tk_a^*}{n}\right],
\tag{8}
\]
\[
b(x)=\frac1{m\sqrt m\tau}\sum_a
\frac{d(x)^Tv_a^*}{n}\frac{h(x)^T(h_a-k_a^*)}{n}.
\tag{9}
\]

Here b is the study's scalar norm-response coefficient, not the
manuscript's residual-weighted backward history. Differentiating the query
output and using (4) and (7) gives, exactly,

\[
\dot f(x)=-\sum_a C(x,a)r_a+\|r\|b(x).
\tag{10}
\]

Evaluate at the training inputs to obtain the m by m matrix C and vector
b. Freeze them at a reached handoff and evolve

\[
\dot{\widehat r}=-C\widehat r+\|\widehat r\|b.
\tag{11}
\]

Also integrate the m residual coordinates and their Euclidean norm, starting
those integrals at zero. At a query, its frozen continuation is its handoff
prediction minus C(x,:) times the residual integrals, plus b(x) times the
norm integral. This uses 2m+1 moving scalars shared by all queries.
There is no division by the residual and the vector field vanishes at zero.

For the circle campaign, the same 64 real odd Fourier coefficients for
each of m+2 query functions give m^2+m+64(m+2) fixed numbers. With m=8:
17 moving + 712 fixed = 729 numbers for q=1, q=2 or q=3. The Fourier
representation has its own approximation error, which must be measured.
The uncompressed training phase and coefficient production still require
the full order-q state and the fixed mixer.

## Conditional theorem transfer and limits

At every fixed finite q, equations (1)--(4) factor as a sum of residual
components times smooth state-dependent vector fields, plus norm(r) times
another smooth field on tau>0. Equations (8)--(9) are smooth functions of
that finite state. Consequently the proof of
[TERMINAL_SCALAR_THEOREM.md](TERMINAL_SCALAR_THEOREM.md), Sections 2--4,
applies verbatim with these new fields and coefficients: provided its
contraction margin and full tube/small-tail hypotheses hold, the uniform
physical-time residual error is O(R^2), loss error O(R^3), and each fixed
smooth query-observable error O(R^2), where R is the handoff residual norm.
All constants in that theorem retain their formulas with the new tube
bounds H and J. Those bounds may depend on q and width.

This transfer proves neither that every initialized trajectory reaches a
certified tube nor that q=2 or q=3 approximates dense training sufficiently.
These are separate scientific questions. A positive empirical contraction
diagnostic does not by itself verify the tube conditions. Likewise the
729-number terminal evaluator does not supply an initialization-only,
sublinear-cost predictor of the entire training trajectory.

Scientific source: paper/main.tex, the learning-speed moment construction
and its exact differentiated reconstruction, SHA256
fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605.
This study uses the same current paper read for its earlier q=1 work;
no manuscript definition changed between the two calculations.
