# A scalar replacement for the terminal stage

2026-09-30. Author derivation in the structured full-rank study. This is a
conditional, quantitative terminal-stage construction. It does not close the
active feature-learning phase or establish an efficient general scalar closure.
No training experiments were run for this note.

The useful fact is stronger than zero-residual stopping: after a certified
handoff, freezing the **current learned aggregate response coefficients** gives
an autonomous scalar system whose output error is proportional to the MSE at
handoff, uniformly over all subsequent physical time. Freezing at initialization
does not receive this guarantee unless initialization itself meets the small-
residual and stability conditions.

## 1. Exact response form of the P1 target

Use the two-hidden-layer population model in sections 1–2 of
`AGGREGATE_SCALAR_CONSTRUCTION.md`, at memory order P=1. Let m be the number
of training inputs. Brackets between neuron vectors mean the normalized
population inner product, or n^{-1} times their dot product at finite width.
Write b_a=B_a/L and a_a=A_a/L. Then

\[
W=W_0-\frac2{mn}\sum_a A_a b_a^\top,
\qquad
\dot W=-\frac2{mn}\sum_a
\left[r_a\delta_{2,a}b_a^\top+
\rho a_a(h_{1,a}-b_a)^\top\right],
\quad \rho=\left(m^{-1}\sum_a r_a^2\right)^{1/2}.
\]

For any input u, including a passive input, differentiating its network output
and using the canonical first-layer/readout updates gives

\[
\dot f(u)=-\frac2m\sum_a C(u,a)r_a+\rho d(u),                 \tag{1}
\]

where all quantities on the right are current population contractions:

\[
\begin{aligned}
C(u,a)={}&\langle h_2(u),h_{2,a}\rangle
 +(u\cdot u_a)\langle\delta_1(u),\delta_{1,a}\rangle\\
 &+\langle\delta_2(u),\delta_{2,a}\rangle
          \langle h_1(u),b_a\rangle,\\
d(u)={}&-\frac2m\sum_a\langle\delta_2(u),a_a\rangle
          \langle h_1(u),h_{1,a}-b_a\rangle .
\end{aligned}                                                   \tag{2}
\]

The input u includes the canonical input normalization. In block-population
notation the same contractions are expectations of within-block normalized
inner products. The initialized G and its actual transpose remain in the
responses; (1) has not replaced either action by an independence assumption.

On training inputs put K_ab=2 C(u_a,b)/m and d_a=d(u_a). For a passive input
put k(u)_a=2 C(u,a). With the training-vector inner product
\(\langle v,w\rangle_m=m^{-1}v^\top w\), the exact equations are

\[
\dot r=-Kr+\rho d,\qquad
\dot f(u)=-\langle k(u),r\rangle_m+\rho d(u).                 \tag{3}
\]

K need not be symmetric or positive semidefinite. Its dependence on the
history lag is retained in (2). This matters when checking stability.

## 2. Hypotheses and the finite scalar replacement

Reset physical time to zero at the handoff. The RMS norm is denoted by
\(\|\cdot\|_m\); its induced matrix norm is the ordinary Euclidean operator
norm. Let K_0,d_0,k_0(u),d_0(u),r_0,f_0(u) be the current values. Suppose

\[
\lambda_0:=\lambda_{\min}\left((K_0+K_0^\top)/2\right)
                  -\|d_0\|_m>0.                              \tag{4}
\]

Assume the target coefficients are absolutely continuous and, almost
everywhere along the subsequent trajectory, satisfy

\[
\|\dot K\|_{\rm op}+\|\dot d\|_m\le A\rho,
\qquad
\|\dot k(u)\|_m+|\dot d(u)|\le B_u\rho.                    \tag{5}
\]

These are **hypotheses to establish for the target on a specified region**,
not consequences of knowing its initial kernel. Assume continuation while
these bounds hold. If they are known only in a state tube, also suppose
\(\|\dot z\|\le V\rho\) there and the distance from the initial state to
the tube boundary exceeds \(2V\rho_0/\lambda_0\). This last condition closes
the state-exit bootstrap. Equivalently, one may establish (5) and continuation
globally on the relevant trajectory region.

Require

\[
\rho_0<\frac{\lambda_0^2}{4A},                             \tag{6}
\]

with no restriction from (6) when A=0. Strict inequality can be replaced by
the conservative test \(\rho_0\le\lambda_0^2/(8A)\).

The replacement keeps only m training residuals and one scalar per requested
passive output:

\[
\boxed{
\dot{\bar r}=-K_0\bar r+\bar\rho d_0,\quad
\bar\rho=\|\bar r\|_m,\qquad
\dot{\bar f}(u)=-\langle k_0(u),\bar r\rangle_m
                         +\bar\rho d_0(u).}                 \tag{7}
\]

It starts from the handoff values. The coefficients are constants after
handoff. No populations or initialized-matrix actions are needed during
(7). Its state count is m plus the number of requested outputs. Fixed
coefficient storage is O(m^2) plus O(m) per passive input. A whole-circle
decoder still needs a representation of u↦(f_0(u),k_0(u),d_0(u)); this note
does not hide that representation in the state count.

## 3. Theorem and proof

Under (4)–(6), the target and replacement exist for all remaining time in
the stated region. They satisfy

\[
\rho(t)\le\rho_0e^{-\lambda_0t/2},\qquad
\bar\rho(t)\le\rho_0e^{-\lambda_0t},\qquad
S:=\int_0^\infty\rho(t)\,dt\le\frac{2\rho_0}{\lambda_0}.   \tag{8}
\]

Their residual discrepancy e(t)=\|r(t)-\bar r(t)\|_m obeys

\[
\sup_{t\ge0}e(t)\le\frac A2S^2,
\qquad
\int_0^\infty e(t)\,dt\le\frac A{2\lambda_0}S^2.           \tag{9}
\]

Put \(M_u=\|k_0(u)\|_m+|d_0(u)|\). The output guarantee is

\[
\boxed{
\sup_{t\ge0}|f(t,u)-\bar f(t,u)|
\le\frac12\left(B_u+\frac{M_uA}{\lambda_0}\right)S^2
\le\frac{2}{\lambda_0^2}
       \left(B_u+\frac{M_uA}{\lambda_0}\right)\rho_0^2.}     \tag{10}
\]

Thus the error is O(training MSE at handoff), including the terminal output.
Uniform B_u,M_u give the same bound uniformly on a query set, hence also for
circle RMS. Computing or representing that continuum remains separate.
When comparing a family of handoff points, this O(MSE) statement requires
uniform bounds on A,B_u,M_u and a uniform positive lower bound on λ_0;
the displayed pointwise estimate itself needs no such additional convention.

**Proof.** Write s(t)=∫_0^tρ. From (5), the total coefficient displacement
\(\|K-K_0\|+\|d-d_0\|_m\) is at most As(t). Therefore

\[
D^+\rho\le-[\lambda_0-As(t)]\rho.                         \tag{11}
\]

Up to a first time As reaches λ_0/2, (11) gives the first bound in (8)
and s≤2ρ_0/λ_0. Condition (6) makes As strictly smaller than λ_0/2,
contradicting such a first time. The optional state-tube condition likewise
prevents exit because total state displacement is at most VS. Continuation
then proves (8). If ρ reaches zero, the stipulated target vector field stops;
the inequalities continue to hold thereafter.

The frozen map F_0(v)=−K_0v+\|v\|_m d_0 is λ_0-contracting in the RMS norm:

\[
\langle v-w,F_0(v)-F_0(w)\rangle_m
\le-\lambda_0\|v-w\|_m^2.                                \tag{12}
\]

Indeed, the symmetric part of K_0 supplies its minimum eigenvalue, while
\(|\|v\|_m-\|w\|_m|\le\|v-w\|_m\) bounds the second term by
\(\|d_0\|_m\|v-w\|_m^2\). This also proves the frozen bound in (8)
and global existence of (7), whose vector field is globally Lipschitz.

Writing the target residual equation as F_0(r) plus its coefficient defect
gives

\[
D^+e\le-\lambda_0e+As(t)\rho(t),\qquad e(0)=0.             \tag{13}
\]

Since \(\int_0^\infty s(t)\rho(t)dt=S^2/2\), integration of the
exponentially damped variation-of-constants bound proves both statements
in (9). For the passive output, subtract (7) from (3), use the frozen
coefficients on the residual difference and (5) on their displacement:

\[
|\dot f(u)-\dot{\bar f}(u)|\le M_u e(t)+B_u s(t)\rho(t).
\]

Integrate from equal initial values and apply (9). This proves (10). ∎

## 4. What this resolves and what it does not

This proves the user's proposed terminal simplification under a concrete
stability margin and response-variation bounds. For prescribed output
tolerance ε, a handoff with MSE of order ε is sufficient, with the displayed
constants. Subsequent elapsed training time is absent from the error bound.

The construction freezes a learned terminal response, not the initial feature
space. It therefore does not forbid earlier feature learning. However, a
standalone scalar solver still needs an accurate scalar active phase that
supplies those handoff coefficients. Inaccurate coefficients are not repaired
by fitting the training data. Deriving (5) with useful width-uniform constants
for every Gaussian-block trajectory also remains a separate task; finite-width
local smoothness alone does not prove such constants uniform in width.

For general Gaussian-block initializations one must state whether constants
are deterministic population bounds, bounds conditional on empirical moment
control, or high-probability bounds. A maximum over individual block operator
norms is not automatically width-uniform. No such maximum has been hidden
in an unconditional claim here.

The state bound is a terminal-stage bound, not evidence that the active-phase
state count is sublinear at matched accuracy. It is nevertheless a rigorous
reason to organize future cutoff design around the finite active phase and
residual-weighted source errors, instead of approximating every population
moment uniformly for infinite physical time.
