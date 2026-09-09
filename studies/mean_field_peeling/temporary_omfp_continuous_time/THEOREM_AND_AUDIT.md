# OMFP mesh removal: a sufficient criterion and a closed pressure test

Status: proved statements and open boundaries separated explicitly;
identity-activation assembly passed independent re-audit, 25 August 2026.

## 1. The criterion actually needed for a continuous-time limit

Let \(E_h:X\to X\) be a population one-step map on a Banach state space and
let \(X_h\) be the piecewise-linear interpolation of \(E_h^kx_0\).  Fix a
compact time interval \([0,T]\).  Suppose every variable-step path of total
variation at most \(T\) stays in a common reachable set \(\mathcal K_T\), and
on that set

\[
 \|E_hx-x\|\le M_Th,
 \qquad
 \|E_hx-E_hy\|\le(1+L_Th)\|x-y\|,                 \tag{1.1}
\]

\[
 \|E_h^2x-E_{2h}x\|\le h\rho_T(h),
 \qquad
 \sum_{j\ge0}\rho_T(h_02^{-j})<\infty .           \tag{1.2}
\]

Then the dyadic interpolants converge uniformly on \([0,T]\).  Indeed, at
common coarse grid points, with \(y_j=E_{2h}^jx_0\) and
\(z_j=E_h^{2j}x_0\),

\[
 \|y_{j+1}-z_{j+1}\|
 \le h\rho_T(h)+(1+L_Th)^2\|y_j-z_j\|.
\]

Iteration for \(2jh\le T\), followed by (1.1) between common grid points,
gives the explicit sewing estimate

\[
 \boxed{
 \|X_h-X_{2h}\|_{C([0,T];X)}
 \le \frac T2e^{L_TT}\rho_T(h)+2M_Th .}            \tag{1.3}
\]

Thus a local split defect \(O(h^{1+\alpha})\), for any \(\alpha>0\), is
enough.  A fifth-order scalar expansion is neither necessary nor, by itself,
enough to identify a state flow.

For scalar width-first outputs, an even weaker exact criterion is available.
Put

\[
 \Delta_m(h)=F_{2m}(h)-F_m(2h),\qquad
 D_m(h)=\Delta_m(h)-\kappa_mh^3,                    \tag{1.4}
\]

and define the canonical coefficient

\[
 b_m^*(\rho)=
 \sup_{0<|h|\le \rho/m}\frac{|D_m(h)|}{|h|^5}.     \tag{1.5}
\]

If \(|\kappa_m|\le K_\phi m^2\) and

\[
 \boxed{\displaystyle
 \sum_{j\ge0}\frac{b_{2^j}^*(\rho)}{2^{5j}}<\infty,} \tag{1.6}
\]

then \(G_m(T)=F_m(T/m)\) converges uniformly along dyadic \(m\), on every
\([-R,R]\) with \(R\le2\rho\).  To see this, set \(h=T/(2m)\):

\[
 \|G_{2m}-G_m\|_{L^\infty[-R,R]}
 \le \frac{K_\phi R^3}{8m}
     +\frac{b_m^*(\rho)R^5}{32m^5}.                \tag{1.7}
\]

Consequently every bound \(b_m^*(\rho)\le C_\phi m^{5-\delta}\), with
arbitrary \(\delta>0\), suffices.  The formerly targeted \(m^4\) is a clean
sharp law, but it is stronger than needed.  Bare \(o(m^5)\) does not suffice:
\(m^5/\log m\) produces a harmonic series on dyadic scales.

### 1.1 A reachable-tail criterion for nonlinear depth two

For the actual depth-two population step, in the original bottom-weight
coordinate, write

\[
 X=\phi(u),\quad Z=GX,\quad Y=\phi(Z),\quad
 B=A\phi'(Z),\quad Q=G^*B,\quad D=\phi'(u)Q,
\]

\[
 S_h(A,u,q)=(A,u,q)+h(Y,D,B\otimes X),\qquad G=\Gamma+q. \tag{1.8}
\]

The following is a proved sufficient condition.  For every positive finite
partition \(\pi=(h_0,\ldots,h_{N-1})\) of total mass at most \(T\), suppose
the corresponding width-first states satisfy, for some
\(1/2\le\alpha\le1\),

\[
 \sup_{\pi}\sup_{k\le N}\sup_{p\ge2}
 p^{-\alpha}\|Q_k^\pi\|_p\le K_T<\infty,             \tag{1.9}
\]

and suppose the same estimate holds after restart from the closure of the
reachable tube.  Then the exact width-first discrete states converge
uniformly along dyadic meshes to a unique restartable population IDE.

Here is the quantitative mechanism.  If \(R\) satisfies
\(\|R\|_p\le Kp^\alpha\), and \(c\) is bounded and Lipschitz, Hölder
interpolation with \(p=\lceil\log(e/\delta)\rceil\) gives

\[
 \|R\{c(v)-c(\widetilde v)\}\|_2
 \le C\delta\{\log(e/\delta)\}^{\alpha},
 \qquad \delta=\|v-\widetilde v\|_2.                 \tag{1.10}
\]

All other depth-two state differences are controlled by the Gaussian
envelope and the trace-norm rank-one identity.  Hence the population field
has the Osgood modulus

\[
 \|g(U)-g(\widetilde U)\|
 \le C_T\omega_\alpha(C_T\|U-\widetilde U\|),
 \qquad
 \omega_\alpha(r)=r\{\log(e/r)\}^{\alpha}.           \tag{1.11}
\]

Because \(S_hU=U+hg(U)\) is the actual gradient step,

\[
 \|S_h^2U-S_{2h}U\|
 \le C_Th^2\{\log(e/h)\}^{\alpha}.                   \tag{1.12}
\]

Propagating (1.12) by the scalar Osgood flow yields consecutive dyadic-mesh
bounds of the form

\[
 C_T2^{-j}(1+j)^\alpha
       e^{C_T(1+j)^\alpha}\quad(\alpha<1),
\]

or

\[
 C_T\{2^{-j}(1+j)\}^{e^{-C_TT}}\quad(\alpha=1).       \tag{1.13}
\]

Both series converge.  This proves state convergence, and the left-step
integral representation then identifies the autonomous IDE.  Thus a
restart-uniform subexponential bound for only the reused transpose action
\(Q\) is enough; fifth-order response jets are not needed for the existence
of the flow.

## 2. Banach-OMFP for the identity activation

The nonlinear OMFP source is not a smooth map on ambient \(L^2\).  There is,
however, a nontrivial subclass in which it becomes one and in which the sharp
fifth-order bound can be proved completely: the normalized identity
activation \(\phi(x)=x\).  This pressure test retains every reused matrix and
its adjoint.

For depth \(L\ge1\), let \(H_a=L^2(\Omega_a)\).  The immutable initialization
connector

\[
 W_{a,0}=I_a+J_a^*:H_{a-1}\to H_a,
 \qquad \|W_{a,0}\|_{\rm op}\le2                 \tag{2.1}
\]

is the fixed-operator realization of the forward and transposed Gaussian
actions.  Let

\[
 X_L=H_L\oplus H_1\oplus
       \bigoplus_{a=2}^L\mathfrak S_1(H_{a-1},H_a) \tag{2.2}
\]

with the sum of the two Hilbert norms and the trace norms.  Write a state as

\[
 \theta=(a,u,q_2,\ldots,q_L),\qquad W_a=W_{a,0}+q_a. \tag{2.3}
\]

Define the forward and reverse fields

\[
 x_1=u,\quad x_a=W_ax_{a-1},
 \qquad
 r_L=a,\quad r_{a-1}=W_a^*r_a,                    \tag{2.4}
\]

and

\[
 f(\theta)=\langle a,x_L\rangle,
\qquad
 g(\theta)=
 \bigl(x_L,r_1,(r_a\otimes x_{a-1})_{a=2}^L\bigr). \tag{2.5}
\]

Here \((b\otimes x)v=b\langle x,v\rangle\), so
\(\|b\otimes x\|_1=\|b\|_2\|x\|_2\).  The exact population gradient step is

\[
 E_h\theta=\theta+hg(\theta).                      \tag{2.6}
\]

No matrix is resampled in (2.1)--(2.6); both \(W_{a,0}\) and
\(W_{a,0}^*\) are the same immutable pointed source.

At initialization, \(a\) and \(u\) are unit Gaussian vectors in their source
Hilbert spaces and \(q_a=0\).  For every fixed nonzero \(h\) and fixed number
of steps \(N\), the finite-width identity network is a finite marked
straight-line program in the initial Gaussian matrices and their transposes.
The fixed-width theorem proved in
temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md, Theorem 1.3 and
Sections 9--10, identifies every forward and transposed adaptive action,
every response term, all empirical Grams, and the terminal output in
\(L^1\).  Its hypotheses hold because the identity activation is
nonconstant, normalized, \(C^\infty\), and has bounded derivatives.  In the
fixed-operator realization of
temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md, Section 4.3,
(4.9)--(4.12), the identity DAG recursion is exactly (2.4)--(2.6):
activation nodes are the identity and every learned connector increment is
\(h(r_a\otimes x_{a-1})\).  That section proves, by chronological induction,
that the learned Gram actions and every adaptive \(W/W^*\) response agree
with the inverse-free DAG, including at singular history Grams.  Therefore
the theorem's limiting DAG is the state above, not an additional model.
Terminal uniform integrability is part of the width theorem.  Hence

\[
 F_{N,L}(h)=f(E_h^N\theta_0)                        \tag{2.7}
\]

after taking width to infinity at this fixed ((N,h)).  Equation (2.7) is the
width-first identification; nothing below reverses that order of limits.

## 3. Explicit smoothness constants

Put \((k)_r=k!/(k-r)!\) for \(0\le r\le k\), and \((k)_r=0\) for \(r>k\).
On the closed unit ball about \(\theta_0\),

\[
 \|a\|_2,\|u\|_2\le2,
 \qquad \|W_a\|_{\rm op}\le3.                    \tag{3.1}
\]

Each component of (g) is one multilinear word of exactly (L) factors:
this is immediate for \(x_L\) and \(r_1\); for
\(r_a\otimes x_{a-1}\), the two endpoint vectors and the
\((L-a)+(a-2)=L-2\) connectors again give \(L\) factors.  The scalar \(f\)
is one word of \(L+1\) factors.  Differentiating an affine factor twice gives
zero.  Hence, in the norm (2.2),

\[
 \|D^rg(\theta)\|
 \le (L+1)(L)_r3^{L-r},\qquad 0\le r\le4,          \tag{3.2}
\]

\[
 \|D^rf(\theta)\|
 \le (L+1)_r3^{L+1-r},\qquad 1\le r\le4.          \tag{3.3}
\]

Indeed, \((L)_r\) is exactly the number of ordered choices of the \(r\)
distinct factors hit by the derivatives; every untouched factor has norm at
most three, every variation component has norm at most the \(X_L\)-norm of
that variation, and the \(L+1\) vector-field components are summed in (2.2).

Define the explicit depth constant

\[
 K_L=\max\!\left\{
 1,
 \max_{0\le r\le4}(L+1)(L)_r3^{L-r},
 \max_{1\le r\le4}(L+1)_r3^{L+1-r}
 \right\}.                                         \tag{3.4}
\]

In particular,

\[
 K_2=27,\qquad K_3=108.                             \tag{3.5}
\]

The following finite recursion makes the remainder constant completely
explicit.  For \(K\ge1\), set \(c_K=(16K)^{-1}\) and

\[
 X_1=8K,
\]

\[
 X_2=2\{8KX_1+4c_KKX_1^2\},
\]

\[
 X_3=2\{12K(X_1^2+X_2)
          +4c_KK(X_1^3+3X_1X_2)\}.                \tag{3.6}
\]

Put

\[
 G_0=K,\quad G_1=KX_1,\quad
 G_2=K(X_2+X_1^2),\quad
 G_3=K(X_3+3X_1X_2+X_1^3),                         \tag{3.7}
\]

and, for (0\le r\le3),

\[
 A_r=\sum_{q=0}^r{r\choose q}G_qG_{r-q}.           \tag{3.8}
\]

With \(A_{-1}=A_{-2}=0\), define

\[
 Z_r=X_r+c_K^2A_r+2rc_KA_{r-1}+r(r-1)A_{r-2},
 \qquad 1\le r\le3.                               \tag{3.9}
\]

Starting with

\[
 T_1=2(Z_1+2K),
\]

set

\[
 T_2=2\{Z_2+4KT_1+2c_KKT_1^2\},
\]

\[
 T_3=2\{Z_3+6K(T_1^2+T_2)
             +2c_KK(T_1^3+3T_1T_2)\}.             \tag{3.10}
\]

Next put

\[
 H_0=K,\quad H_1=KT_1,\quad
 H_2=K(T_2+T_1^2),\quad
 H_3=K(T_3+3T_1T_2+T_1^3).                         \tag{3.11}
\]

Let \(W_0=2A_0\), and successively for \(1\le r\le3\),

\[
 W_r=2\left\{A_r
 +2c_K\sum_{q=1}^r{r\choose q}H_qW_{r-q}
 +2r\sum_{q=0}^{r-1}{r-1\choose q}H_qW_{r-1-q}
 \right\}.                                         \tag{3.12}
\]

Finally,

\[
 C_K=\frac16\sum_{q=0}^3{3\choose q}H_qW_{3-q}.   \tag{3.13}
\]

Every index in (3.6)--(3.13) belongs to the fixed set
\(\{0,1,2,3\}\), and every right-hand side uses only previously defined
quantities.  The recursion therefore terminates and \(C_K<\infty\).

## 4. Sharp fifth-order pressure test

Let

\[
 \Delta_{t,L}(h)=F_{2t,L}(h)-F_{t,L}(2h).          \tag{4.1}
\]

Put \(C_h=E_{2h}\), \(B_h=E_h^2\), and \(P_Mv=v\circ M\).  The fundamental
theorem of calculus gives the exact local identity

\[
 B_hx=C_hx+h^2a_h(x),\qquad
 a_h(x)=\int_0^1Dg(x+shg(x))g(x)\,ds.              \tag{4.2a}
\]

For a \(C^1\) test \(v\), define

\[
 R_hv(x)=-
 \int_0^1Dv(C_hx+sh^2a_h(x))[a_h(x)]\,ds.          \tag{4.2b}
\]

The noncommutative telescoping identity
\(A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j\),
applied to the pullbacks \(P_{C_h},P_{B_h}\), gives

\[
 Q_t(h)=
 \sum_{j=0}^{t-1}
 [P_{C_h}^{\,t-1-j}R_hP_{B_h}^{\,j}f](\theta_0).   \tag{4.2c}
\]

Thus the exact paired-Euler factorization is

\[
 F_{t,L}(2h)-F_{2t,L}(h)=h^2Q_t(h),                \tag{4.2}
\]

where \(Q_t\) is a sum of exactly \(t\) transported local defects.  The
parity used here is direct.  Let \(S\) negate \(a\) and leave
\((u,q_2,\ldots,q_L)\) fixed.  Then

\[
 f(S\theta)=-f(\theta),\qquad Sg(\theta)=-g(S\theta),
\]

so

\[
 S E_h=E_{-h}S.
\]

The centered Gaussian initialization law is invariant under \(S\).
Consequently \(F_{N,L}(-h)=-F_{N,L}(h)\), (4.2) is odd, and \(Q_t\) is
odd.  Three step-size differentiations cost at most \(t^3\), while the
defect sum costs one further factor \(t\).  Applying the chain and product
rules with the bounds (3.2)--(3.3), the terminating recursion
(3.6)--(3.13) gives

\[
 \sup_{|h|\le c_K/t}|Q_t'''(h)|\le6C_Kt^4.         \tag{4.3}
\]

This is exactly the transported-defect theorem proved in
temporary_depth_time_doubling/UNIFORM_BSERIES.md, Theorem 4.1; its
adversarial audit in AUDIT_UNIFORM_BSERIES.md passes the abstract theorem.
Here every hypothesis of that theorem has been verified explicitly:
\(X_L\) is Banach, (3.2)--(3.4) give its single constant \(K_L\), and the
parity was proved above.  In particular, this invocation is not the
unproved nonlinear generated-core hypothesis discussed in Section 5.

For completeness, the quantitative induction behind (4.3) differentiates a
variable-step Euler path \(x^+=x+\alpha hg(x)\), \(0\le\alpha\le2\), whose
total coefficient is at most \(4t\).  The homogeneous tangent product is
bounded by

\[
 \prod(1+\alpha |h|K)
 \le e^{4c_KK}<2.                                  \tag{4.4}
\]

The first-exit estimate is also explicit: before the local-defect
interpolation,

\[
 \|x_m-\theta_0\|
 \le |h|K\sum_j\alpha_j\le4c_KK=\frac14.
\]

The interpolation in (4.2a)--(4.2b) adds at most
\(c_K^2K^2\le1/256\), so every point remains strictly in the unit ball on
which (3.2)--(3.3) hold.  The first three normalized path jets are bounded
respectively by \(X_1t,X_2t^2,X_3t^3\); the local defect jets by
\(A_rt^r\); the post-defect path jets by \(T_rt^r\); and the transported
direction jets by \(W_rt^r\).  These are precisely the successive recursions
(3.6)--(3.12), obtained from the first three differentiated Euler
recurrences and Leibniz's rule.  A final Leibniz rule for \(Df[w]\), followed
by summation over the exactly \(t\) defect locations, is (4.3).

Since \(Q_t(0)=Q_t''(0)=0\), Taylor's integral formula gives

\[
 \left|h^2Q_t(h)-Q_t'(0)h^3\right|
 \le \frac{|h|^5}{6}\sup_{|s|\le|h|}|Q_t'''(s)|.  \tag{4.5}
\]

The independently proved width-first cubic theorem in
temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md, (1.6), applies to the
same \(F_{N,L}\) identified in (2.7).  Since its coarse-minus-fine
discrepancy is the left side of (4.2), comparison with (4.2) gives the
signed identity

\[
 Q_t'(0)=-\frac{t(2t-1)}2J_{x,L}.                   \tag{4.5a}
\]

Section 9.3 of that theorem evaluates its terminating Gaussian activation
recursion for the identity activation as

\[
 J_{x,L}=\frac{2L(L+1)^2(L+2)}3.                   \tag{4.6}
\]

Combining (4.2)--(4.6) proves the width-first theorem

\[
 \boxed{
 \left|
 \Delta_{t,L}(h)
 -\frac{t(2t-1)L(L+1)^2(L+2)}3h^3
 \right|
 \le C_{K_L}t^4|h|^5,
 \quad |h|\le\frac1{16K_Lt}.}                     \tag{4.7}
\]

The two requested pressure tests are therefore

\[
 \left|\Delta_{t,2}(h)-24t(2t-1)h^3\right|
 \le C_{27}t^4|h|^5,
 \qquad |h|\le\frac1{432t},                       \tag{4.8}
\]

and

\[
 \left|\Delta_{t,3}(h)-80t(2t-1)h^3\right|
 \le C_{108}t^4|h|^5,
 \qquad |h|\le\frac1{1728t}.                     \tag{4.9}
\]

This is an unconditional result for the actual reused-matrix width-first
network with \(\phi(x)=x\), not a resampled Gaussian program.

At fixed total time, put \(G_{m,L}(T)=F_{m,L}(T/m)\) and set
\(h=T/(2t)\) in (4.7).  For \(|T|\le(8K_L)^{-1}\),

\[
 |G_{2t,L}(T)-G_{t,L}(T)|
 \le \frac{L(L+1)^2(L+2)}{12t}|T|^3
      +\frac{C_{K_L}}{32t}|T|^5.                  \tag{4.10}
\]

The right side is dyadically summable.  In fact, because (2.6) is Euler's
method for the locally Lipschitz polynomial field (g), the whole state,
not merely its readout, converges to the unique local IDE

\[
 \dot\theta=g(\theta),\qquad \theta(0)=\theta_0.    \tag{4.11}
\]

## 5. What this proves—and does not prove—for nonlinear activations

For a nonlinear activation, the exact paired-Euler algebra and the \(t^4\)
time combinatorics remain valid.  The Banach realization above does not.
Two elementary obstructions prevent promoting bounded scalar derivatives of
\(\phi\) to the needed ambient smoothness:

1. Pointwise multiplication is not bounded
   \(L^2\times L^2\to L^2\).  Thus a non-affine Nemytskii map is not generally
   \(C^2:L^2\to L^2\), even when every scalar derivative of \(\phi\) is
   bounded.
2. The reused adjoint connector has no ambient \(L^p\) estimate for \(p>2\).
   If \(c\in L^2\setminus L^p\) and \(x=J_ac\), then \(x\) is a first-chaos
   Gaussian but \(J_a^*x=c\notin L^p\).

The exact depth-two response DAG is nevertheless Volterra: every historical
response carries its true step weight.  This suggests the following
intrinsic, generated-core condition.  Factor the paired discrepancy as

\[
 \Delta_m(h)=h^2Q_m(h),\qquad
 Q_m(h)=\sum_{j=0}^{m-1}A_{j,m}(h),                 \tag{5.1}
\]

and expand \(m^{-3}A_{j,m}'''(h)\) completely into generated fields and
**aggregate** adjoint response actions, recombining response coordinates
before taking absolute values.  Let \(\mathfrak E_m(h)\) be the maximum over
(j) of the resulting finite sum of absolute Gaussian expectations.

If, for some explicit \(\alpha<1\),

\[
 \sup_{|h|\le\rho_\phi/m}\mathfrak E_m(h)
 \le C_\phi m^\alpha,                              \tag{5.2}
\]

then

\[
 \sup_{|v|\le\rho_\phi/m}|Q_m'''(v)|
 \le C_\phi m^{4+\alpha},                          \tag{5.3}
\]

and consequently

\[
 b_m^*(\rho_\phi)\le\frac{C_\phi}{6}m^{4+\alpha}. \tag{5.4}
\]

Equations (1.6) and (5.4) then prove the scalar continuous-time limit because

\[
 \sum_{j\ge0}2^{-(1-\alpha)j}<\infty.              \tag{5.5}
\]

This implication is proved.  Condition (5.2), however, is not presently
proved for a general nonlinear activation, even at \(L=2\).  The unclosed
terms are the coupled moving-query/source-response jets such as

\[
 a_s\phi''(z_s)\zeta_s^i,
 \qquad r_s\phi''(u_s)p_s^i,                       \tag{5.6}
\]

together with future actions \(I(\partial_hx_s)\),
\(J(\partial_h\delta_s)\) and the differentiated aggregate response actions.
A scalar Gaussian weighted-Gronwall bound controls the causal transport, but
does not control this coupled block.

Even the arctangent natural coordinate does not remove the discrete-time
gap.  With

\[
 \Theta(u)=u+u^3/3,
 \qquad c(u)=(1+u^2)^{-1},
\]

an actual gradient step \(u^+=u+hc(u)Q\) gives exactly

\[
 \Theta(u^+)=\Theta(u)+hQ
 +h^2u c(u)^2Q^2+\frac{h^3}{3}c(u)^3Q^3.           \tag{5.7}
\]

The continuous natural-coordinate IDE keeps only the (hQ) term.  To make
(5.7) an \(L^2\) local defect one needs, at minimum, a reachable \(L^6\)
bound for \(Q\).  The current \(L^2\)/trace-state theory does not prove that
bound uniformly over width-first meshes.  At \(L=3\), the same issue appears
at both connectors and is strictly stronger.

Therefore the rigorous boundary is:

* the minimal scalar summability theorem (1.6) is proved;
* the restartable state sewing theorem (1.1)--(1.3) is proved;
* the sharp \(t^4h^5\) pressure test is proved for the identity activation at
  \(L=2,L=3\), and in fact for every finite \(L\), by (4.7);
* the nonlinear \(L=2\) generated-response estimate (5.2), and hence its
  \(L=3\) connector transfer, remain open.

The linear all-depth result isolates the lesson for the general-depth
program: depth and time combinatorics are already under control.  The missing
fundamental extension is an intrinsic tame calculus for aggregate adaptive
adjoint responses on the reachable OMFP core, not another terminal-output
Taylor compiler.
