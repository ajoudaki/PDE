# Post-freeze correction: one cross-sign estimate controls both modes

2026-09-16. This note records a bounded follow-up calculation requested by
the supervisor after `route_global.md` was frozen. It does not modify that
file, perform experiments, or claim a proof of the remaining cross-sign
estimate. It supersedes that route's suggestion that common-mode control
is an additional independent gap once its cross-sign estimate is known.

## Exact identities

Use the exact canonical p=1 population closure and the balanced data

\[
 u_+=(a,b),\quad u_-=(a,-b),\quad a,b>0,\quad a^2+b^2=1,
 \qquad y_+=1,\quad y_-=-1,\quad \rho=a^2-b^2.
\]

Retain the reflection-invariant subsystem and notation of the frozen
route. The normalized two-coordinate lower mark blocks are b_i, the
corresponding middle row vectors are m_i, and

\[
 a_i=E_1[b_i\tanh(w\cdot u_+)],\quad
 k_i=m_i^Tb_i,\quad B_i=m_i^Ta_i,\quad
 S_\pm=\operatorname{sech}^2(w\cdot u_\pm).
\]

The independent symmetric upper marks are beta_1,beta_2, and

\[
 Z_\pm=\beta_1B_1\mathbin{\pm}\beta_2B_2,\quad
 d_i=E_2[\beta_i c\operatorname{sech}^2Z_+].
\]

Feature time satisfies s_t=2(1-f(u_+)); equivalently one can use the
autonomous gradient-ascent parameter for
F=(f(u_+)-f(u_-))/2. The exact equations are

\[
 (m_i)_s=d_i a_i,\quad
 c_s=\tfrac12[\tanh Z_+-\tanh Z_-],
\]
\[
 w_s=\tfrac12\{S_+(d_1k_1+d_2k_2)u_+
                    +S_-(d_1k_1-d_2k_2)u_-\}.
\]

Define

\[
 C_{\rm cross}=E_1[k_1k_2S_+^2],\quad
 T_1=E_1[k_1^2(S_+^2+\rho S_+S_-)],\quad
 T_2=E_1[k_2^2(S_+^2-\rho S_+S_-)].
\]

Then both signal equations are

\[
 (B_1)_s=d_1\left(|a_1|^2+\frac{T_1}{2}\right)
                           +\frac{d_2}{2}C_{\rm cross},\qquad
 (B_2)_s=d_2\left(|a_2|^2+\frac{T_2}{2}\right)
                           +\frac{d_1}{2}C_{\rm cross}.       \tag{1}
\]

Here is a direct verification. Dot the row equation with u_+ and multiply
by b_i S_+ to differentiate a_i. This gives

\[
 (a_i)_s=\tfrac12E_1\!\left[b_i\{d_1k_1(S_+^2+\rho S_+S_-)
                           +d_2k_2(S_+^2-\rho S_+S_-)\}\right].
\]

Second-mark reflection fixes k_1, reverses k_2, and swaps S_+ with S_-.
Consequently E_1[k_1k_2 S_+S_-]=0. Using
(B_i)_s=(m_i)_s^Ta_i+m_i^T(a_i)_s proves (1). The same reflection gives
E_1[k_i^2S_+^2]=E_1[k_i^2S_-^2], so

\[
 T_1=\tfrac12E_1[k_1^2\{(S_+-S_-)^2+2(1+\rho)S_+S_-\}]\ge0,
\]
\[
 T_2=\tfrac12E_1[k_2^2\{(S_+-S_-)^2+2(1-\rho)S_+S_-\}]\ge0.       \tag{2}
\]

Only |rho|<=1 and positivity of the gates enter these inequalities.

## Complete sign argument and common-mode control

Assume B_2(0)>0. On any initial interval where B_2 remains positive,

\[
 c(s,\beta_1,\beta_2)=\frac12\int_0^s
 [\tanh(\beta_1B_1(v)+\beta_2B_2(v))
 -\tanh(\beta_1B_1(v)-\beta_2B_2(v))],dv
\]

is even in beta_1 and has the sign of beta_2 for s>0 and beta_2!=0.
Thus d_2>0 for positive s. This assertion uses only monotonicity and
oddness of tanh and the zero initial readout.

To determine d_1, pair beta_1 with -beta_1 in its expectation. Write
g(x)=sech^2(x), x=beta_1 B_1 and y=beta_2 B_2. Then

\[
 B_1d_1=\tfrac12E_2[xc\{g(x+y)-g(y-x)\}]\le0.              \tag{3}
\]

Indeed g is even and strictly decreasing in absolute value away from
zero. Since (x+y)^2-(y-x)^2=4xy, the bracket has sign opposite to xy.
The readout c has the sign of y. Every nonzero integrand in (3) is
therefore negative. If B_1=0, pairing directly gives d_1=0.

Now suppose the single additional estimate

\[
                         B_1C_{\rm cross}\le0               \tag{4}
\]

holds along the reached trajectory whenever B_2>0. If B_1!=0, (3) and
(4) make d_1 and C_cross have the same weak sign. If B_1=0, d_1=0.
Hence d_1 C_cross>=0 in all cases. Equations (1)–(2) give
(B_2)_s>=0. Starting from B_2(0)>0, a first-exit argument yields

\[
                         B_2(s)\ge B_2(0)>0.                \tag{5}
\]

The first equation in (1) simultaneously gives

\[
 (B_1^2)_s
 =2B_1d_1\left(|a_1|^2+\frac{T_1}{2}\right)
                            +d_2 B_1C_{\rm cross}\le0,
\]

and therefore

\[
                         |B_1(s)|\le|B_1(0)|.              \tag{6}
\]

No division by B_1 or separate treatment of a potential zero crossing is
needed in this last argument. Thus (4) gives both antisymmetric signal
preservation and common-mode control; these are not two independent
unproved dynamical estimates.

## Uniform readout separation follows as well

Let beta_max=1/sqrt(tau+eta), the fixed supremum envelope of each upper
mark, and take delta=beta_max/2. The exact Gaussian mark law satisfies
p_delta=P(|beta_2|>=delta)>0. Put

\[
 P=\beta_{\max}|B_1(0)|,\qquad q_0=\delta B_2(0)>0,
\quad h_0=\frac{\tanh(P+q_0)-\tanh(P-q_0)}2>0.
\]

For U=(tanh Z_+-tanh Z_-)/2, equations (5)–(6) imply |U|>=h_0 on
the event |beta_2|>=delta. To verify the minimization explicitly, for
q>0 write

\[
 D(p,q)=\frac{\tanh(p+q)-\tanh(p-q)}2
       =\frac{\sinh(2q)}{\cosh(2p)+\cosh(2q)}.
\]

It is even in p, decreasing in |p|, and strictly increasing in q;
the last property also follows by differentiating its first expression.
Here |p|<=P and q>=q_0. Thus

\[
                 E_2U^2\ge p_\delta h_0^2>0.             \tag{7}
\]

The feature-gradient identity F_s=||grad F||^2>=E_2U^2 now supplies
uniform dissipation. Consequently the physical residual and loss decay
exponentially, with rates 2 p_delta h_0^2 and 4 p_delta h_0^2 respectively,
under hypothesis (4). The finite feature-time bounds already established
for this closure then imply convergence of the full state. No new
independent common-mode or readout-mode assumption is required.

## Precise remaining gap

The open **dynamical** obligation for this sufficient-condition route is
to prove (4) on the canonically initialized reached trajectories over the
desired separation class, or replace it by a weaker estimate that still
controls (1). Positive semidefiniteness of the tangent matrix does not
determine this cross-entry sign. The note supplies neither that sign proof
nor a counterexample, and failure of (4) would defeat only this sufficient
route, not disprove convergence.

The conditional statement also explicitly assumes B_2(0)>0. That is proved
at the axis in the frozen route and holds in a neighborhood by continuity.
If one seeks all nonzero reflection-pair separations, initial positivity
must be verified for that full class rather than silently inferred from
the axis calculation. This is an initialization check, distinct from the
single unproved dynamical estimate (4). The already checked open angular
family near the axis uses finite-interval continuous dependence and does
not require (4).
