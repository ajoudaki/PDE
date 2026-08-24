# Working lemmas for the resolution campaign

Status: only explicitly labelled results are proved.  The transfer from the
frozen-bottom control to the full quadratic network remains a proof
obligation.

## 1. Exact frozen-bottom boundary layer

Freeze \(u\), hence \(X=u^{\odot2}\) and
\(Q_n=\langle X^2\rangle_n\), while training \(A,G\) by

\[
A_i'=Z_i^2,\qquad G_{ij}'=\frac2nA_iZ_iX_j,\qquad Z=GX.
\]

Then every row is an independent scalar system conditional on \(X\):

\[
A_i'=Z_i^2,\qquad Z_i'=2Q_nA_iZ_i,                       \tag{1.1}
\]

and

\[
Z_i^2-2Q_nA_i^2=c_i                                      \tag{1.2}
\]

is invariant.  Conditional on \(X\), \(Z_i(0)\) are independent
\(N(0,Q_n)\) variables, independent of \(A_i(0)\), and
\(Q_n\to3\) in probability.

Put \(L_n=\sqrt{\log n}\).  For a fixed sufficiently small
\(\varepsilon>0\), the number of rows satisfying

\[
A_i(0)\in[L_n,(1+\varepsilon)L_n],\qquad
Z_i(0)\in[L_n,(1+\varepsilon)L_n]
\]

tends to infinity in probability.  This follows conditionally from the
binomial law and the exponent

\[
1-\frac12-\frac1{2Q_n}\longrightarrow\frac13.
\]

On any such row, (1.2) and \(Q_n\in[3-\varepsilon,3+\varepsilon]\)
give a scalar Riccati solution whose blow-up time is at most \(C/L_n\).
Indeed, writing

\[
\alpha_i^2=A_i(0)^2-\frac{Z_i(0)^2}{2Q_n}>cL_n^2,
\]

one has

\[
A_i'=2Q_n(A_i^2-\alpha_i^2)
\]

and hence

\[
s_\infty
=\frac1{4Q_n\alpha_i}
  \log\frac{A_i(0)+\alpha_i}{A_i(0)-\alpha_i}
\le\frac C{L_n}.                                         \tag{1.3}
\]

Let \(f_n^{\rm fr}\) be the corresponding feature output and let
\(\tau_{\delta,n}^{\rm fr}\) be the first time it has increased by a fixed
\(\delta>0\).  Before the scalar pole, choose
\(M_n=C_\delta n^{1/3}\).  Once \(A_i\ge2A_i(0)\), (1.2) gives
\(Z_i^2\ge cA_i^2\), and therefore the exact kernel identity yields

\[
\begin{aligned}
f_n^{\rm fr}(s_{M_n})-f_n^{\rm fr}(0)
&=\int_0^{s_{M_n}}K_n^{\rm fr}(s)\,ds\\
&\ge\frac1n\int_0^{s_{M_n}}Z_i^4\,ds
 =\frac1n\int_{A_i(0)}^{M_n}Z_i^2\,dA_i\\
&\ge \frac{cM_n^3}{n}.
\end{aligned}                                             \tag{1.4}
\]

Choosing \(C_\delta\) sufficiently large proves

\[
\boxed{\tau_{\delta,n}^{\rm fr}
       =O_{\mathbb P}\!\left((\log n)^{-1/2}\right).}       \tag{1.5}
\]

For a fixed positive physical target \(y_\star\) and
\(0<\delta<y_\star\), the feature clock
\(ds/dt=2\eta(y_\star-f)\) gives the same vanishing upper bound for the
physical \(\delta\)-hitting time.  Negative targets follow in distribution
from \(A\mapsto-A,\ s\mapsto-s\).

Thus the frozen-bottom model itself has no uniform compact-time limit with a
continuous output readout at \(t=0\).

## 2. Why this does not yet prove the full theorem

For the full flow,

\[
Z'=2Q B+8HB,\qquad H=G D_XG^*\succeq0.
\]

Although \(B^THB\ge0\) and this term contributes positively to the total
kernel, \(HB\) has no coordinatewise sign.  Therefore (1.1) is not a valid
rowwise lower comparison.  A complete transfer requires either

1. a stopped, initialization-measurable, selection-uniform cavity bound for
   at least one joint Gaussian tail row; or
2. a deterministic collective comparison showing that any cancellation of
   all such rows forces the output increment even earlier.

The direct selected-row influence estimates

\[
\int_0^{s_M}A_iZ_i\,ds=O(M),\qquad
\Delta G_{ij}=O(MX_j/n)
\]

are compatible with such a transfer for \(M=O(n^{1/3})\), but by themselves
do not control the nonlinear full-versus-cavity response of the other rows.

## 3. A universal projective-space cure is impossible

This lemma is a stress test, not yet a theorem about the canonical quadratic
network.  Let \(\xi_i\) be iid standard Gaussians and consider

\[
x_i'=x_i^2.
\]

The maximal characteristic is \(x_i(s)=\xi_i/(1-s\xi_i)\), and the common
finite-width lifetime is

\[
\tau_n=\frac1{\max_i\xi_i^+}\longrightarrow0
\quad\hbox{almost surely}.                                \tag{3.1}
\]

Continuing the rational expression through its pole does not produce a raw
moment solution: for every \(s>0\) and \(p\ge1\),

\[
\mathbb E\left|\frac{\xi}{1-s\xi}\right|^p=\infty.        \tag{3.2}
\]

The residual multiplier does not remove the defect.  For

\[
\dot x_i=2\eta(y-f_n)x_i^2,\qquad
f_n=\frac1n\sum_i x_i,\qquad K_n=\frac1n\sum_i x_i^2,
\]

write \(F_n(s)=n^{-1}\sum_i\xi_i/(1-s\xi_i)\).  For every
\(0<\varepsilon<y\), the physical time at which
\(f_n=y-\varepsilon\) obeys

\[
T_{n,\varepsilon}
\le \frac1{2\eta\varepsilon\max_i\xi_i^+}
\longrightarrow0.                                        \tag{3.3}
\]

Thus \(f_n(0)\to0\), whereas \(f_n(t)\to y\) for every fixed \(t>0\),
and \(K_n\) diverges in the initial layer.  Projective compactification,
Hida distributions, and coordinatewise moment hierarchies can encode a
generalized continuation only by losing positivity, finite raw readouts, or
semiflow uniqueness.  Consequently none of those spaces supplies a
*universal* repair for an unbounded Gaussian polynomial flow.

This result does not decide the frozen conjecture: the scalar equation has
not been exhibited as an invariant subsystem or factor of the canonical
quadratic network, whose physical finite-width flow has additional exact
energy control.

## 4. Collective rare-block mechanism

Let \(J\) be a block of \(m=pn\) rows with \(A_i>0\), and put

\[
F_J=\frac1n\sum_{i\in J}A_iZ_i^2,
\qquad r_J=G_J^*B_J.
\]

Its exact derivative is

\[
F_J'
=\frac1n\sum_{i\in J}\{Z_i^4+4QB_i^2\}
 +16\langle Xr_JR\rangle_n.                              \tag{4.1}
\]

If the last term is replaced by a coercive self-block contribution
\(c n^{-1}\sum_JA_i^2Z_i^2\), then the elementary minimization

\[
z^4+c a^2z^2\ge c_1(az^2)^{4/3}\qquad(a\ge0)
\]

and Jensen's inequality on \(pn\) coordinates give

\[
F_J'\ge c_2p^{-1/3}F_J^{4/3}.                             \tag{4.2}
\]

For a Gaussian tail block with initial scale \(\ell\),
\(F_J(0)\asymp p\ell^3\) under a joint \((A,Z)\)-tail selection, so
(4.2) reaches the collective scale \(pM^3\asymp1\),
\(M=p^{-1/3}\), in \(O(\ell^{-1})\) time.  This proves that rowwise
comparison is unnecessary *once* block coercivity and external-work control
are established.

The remaining P4 lemma is precisely to justify that replacement for the
stopped canonical flow.  The centered conditional Gaussian covariance has a
stable-bulk lower bound; adaptive spiky columns add positive semidefinite
directions but destroy a uniform upper covariance bound.  A valid proof must
show that those directions either leave a fixed escaping quantile or that
their cancellation by the complementary rows already has order-one kernel
action.  This is not yet proved.

## 5. Proved stable-bulk covariance lower bound

Let (T=o(1)) and stop before (f(s)-f(0)=\delta).  The exact action
identities give

\[
\sup_{s\le T}\|u(s)-u(0)\|_n^2\le T\delta,
\qquad
\sup_{s\le T}\|G(s)-G(0)\|_{\rm op}^2\le T\delta.        \tag{5.1}
\]

The second estimate follows directly from

\[
\|G'\|_{\rm op}^2
\le4\langle B^2\rangle_n\langle X^2\rangle_n\le K.
\]

Fix (0<a<b<\infty) and let

\[
S_0=\{j:a\le|u_j(0)|\le b\}.
\]

With probability tending to one, (|S_0|/n\to c_{a,b}>0).  At every
(s\le T), all but at most (4T\delta n/a^2) members of (S_0) satisfy
(|u_j(s)|\ge a/2), hence (X_j(s)\ge a^2/4).

Let (J) be a joint Gaussian tail block of (m=pn) rows, with
(p=o(1)), tail scale (ell), and (p\ell^2=o(1)).  Conditionally on
(X(0)) and the selected values (Z_i(0)), its initial rows have the exact
decomposition

\[
g_i(0)=\frac{Z_i(0)}{nQ_0}X(0)+r_i,qquad
r_i\stackrel{\rm iid}{\sim}
N\!\left(0,\frac1n(I-P_{X(0)})\right).                    \tag{5.2}
\]

A Gaussian net/order-statistic argument gives the following uniform
resilience statement: if (ε=o(1)), then, with probability tending
to one, every subset (S\subset S_0) obtained by deleting at most
(ε n) columns satisfies

\[
\inf_{v:\,\operatorname{supp}v\subset J}
\frac{\|P_S R_J^*v\|_n}{\|v\|_n}
\ge \sqrt{c_{a,b}}-o(1).                                  \tag{5.3}
\]

Indeed the full rectangular Gaussian minimum singular value is
(\sqrt{c_{a,b}}-\sqrt p-o(1)), while the largest energy removable in any
(ε n) coordinates is
(O\{\varepsilon\log(1/\varepsilon)+p\}), uniformly over the
(pn)-dimensional row sphere.  The rank-one conditional mean in (5.2) has
operator norm (O(\sqrt p\,\ell)=o(1)), and (5.1) controls the trained
perturbation.

Consequently there is a deterministic (c_*>0) such that, uniformly on the
stopped interval,

\[
\boxed{G_J(s)D_{X(s)}G_J(s)^*\succeq c_*I_J}              \tag{5.4}
\]

with probability tending to one.  Arbitrarily large adaptive columns only
add positive-semidefinite mass and cannot invalidate this lower bound.

Equation (5.4) settles self-channel coercivity.  It supplies no upper bound:
a spiky column can create a very large low-rank eigenvalue.  Controlling a
possible cancellation of that direction by the complementary rows is the
remaining adaptive-Wishart obligation.

## 6. Static complement resilience is false

The remaining obligation cannot be discharged by a statement uniform over
all complement vectors.  This already fails with (X\equiv1).  Split the
conditionally centered Gaussian row matrix into (R_J,R_C), and write

\[
H_{JJ}=R_JR_J^*,\qquad H_{JC}=R_JR_C^*.
\]

For (m=pn=o(n)), conditional on (R_J), the cross matrix has the law

\[
H_{JC}\ \stackrel d=\ (R_JR_J^*)^{1/2}\frac{W}{\sqrt n},
\]

with (W) an (m\times(n-m)) standard Gaussian matrix.  The usual extreme
singular-value bounds therefore give (s_{\min}(H_{JC})\ge c>0) with
probability tending to one.  Consequently, for any block vector (b) and
any prescribed target (y),

\[
c=H_{JC}^*(H_{JC}H_{JC}^*)^{-1}(y-H_{JJ}b)              \tag{6.1}
\]

satisfies (H_{JJ}b+H_{JC}c=y) and
(‖c‖_2\le C(‖b‖_2+‖y‖_2)).  At a state with
(A_i,Z_i\asymp\ell) on (J), choosing the target in (6.1) to cancel the
(2QB_J+8H_{JJ}B_J) drift makes the rare-block derivative nonpositive at
complement cost (O(p\ell^4)) per unit feature time.  Over a time
(O(\ell^{-1})), this is only (O(p\ell^3)=o(1)).

Thus (5.4), positive semidefiniteness, and instantaneous action bounds do not
imply rare-block escape.  Formula (6.1) is not itself a canonical stochastic
counterexample, because it chooses the complement after observing the rare
block.  The exact unresolved statement is now causal: starting from the iid
initialization, can the actual complement (B_C(t)=A_C(t)Z_C(t)) enter and
track the random pseudoinverse tube (6.1) on the (O(\ell^{-1})) time scale?
A successful proof must use dynamical causality/independence (or produce a
reachable canonical cancellation), not a uniform covariance lemma.

## 7. Exact positive/negative passivity transform

There is a sharper structure behind the causal question.  Put

\[
M=2QI+8G D_XG^*\succeq 2QI,
\qquad Z'=M B,
\qquad B=D_AZ.
\]

On any interval not containing a zero crossing of an (A_i), split the rows
into (P=\{A_i>0\}) and (N=\{A_i<0\}), and set

\[
D_+=D_{\sqrt{A_P}},\quad D_-=D_{\sqrt{-A_N}},\qquad
y=D_+Z_P,\quad x=D_-Z_N.
\]

Define

\[
S_+=D_+M_{PP}D_+,quad S_-=D_-M_{NN}D_-,quad
C=D_+M_{PN}D_-,
\]

and the nonnegative diagonal matrices

\[
d_+=D_{Z_P^2/(2A_P)},\qquad
d_-=D_{Z_N^2/(2(-A_N))}.
\]

Direct differentiation, using (A'=Z^2), gives the exact port-Hamiltonian
form

\[
\boxed{
y'=d_+y+S_+y-Cx,qquad
x'=C^*y-S_-x-d_-x.}                                      \tag{7.1}
\]

Thus positive rows are unstable, negative rows are a dissipative load, and
the cross-interconnection is skew with respect to the Euclidean energy.  In
particular,

\[
f=\langle y^2\rangle_n-\langle x^2\rangle_n,
\]

and differentiating (7.1) reproduces exactly

\[
f'=\langle Z^4\rangle_n+2\langle B,MB\rangle_n=K.        \tag{7.2}
\]

The cross-work cancels instead of acquiring an uncontrolled sign in the
derivative of the unsigned storage:

\[
\frac d{ds}\{\langle y^2\rangle_n+\langle x^2\rangle_n\}
=\langle Z_P^4\rangle_n-\langle Z_N^4\rangle_n
2\langle y,S_+y\rangle_n-2\langle x,S_-x\rangle_n.       \tag{7.3}
\]

There is also an exact controller-mismatch decomposition.  Since
(M\succeq m_0I), (m_0=2Q), its Schur complement satisfies

\[
S_+-CS_-^{-1}C^*
=D_+\{M_{PP}-M_{PN}M_{NN}^{-1}M_{NP}\}D_+
\succeq m_0D_+^2.                                       \tag{7.4}
\]

Writing

\[
r=S_-^{1/2}x-S_-^{-1/2}C^*y,
\]

one has

\[
\langle B,MB\rangle_n
=\langle r,r\rangle_n
\langle y,(S_+-CS_-^{-1}C^*)y\rangle_n,                 \tag{7.5}
\]

and the negative load equation becomes

\[
x'=-S_-^{1/2}r-d_-x.                                    \tag{7.6}
\]

Zero crossings cause no jump because the corresponding transformed
coordinate tends to zero, and each (A_i) crosses at most once.  Hence the
identities extend piecewise across the whole finite trajectory.

Equations (7.4)--(7.6) prove that even a perfectly quasi-static negative load
cannot remove the direct (2Q A_i) instability on positive rows: it leaves a
Schur residual at least (2Q D_+^2).  Any non-quasi-static cancellation is
measured by (r), whose squared norm is already a term in the output action.
This is a genuine reduction of the P5 obligation, but not its completion:
for a vanishing rare block the action needed to create a specially aligned
(r) can itself be (o(1)).  What remains probabilistic is to rule out the
rapid formation of precisely that alignment from the iid initial load.

## 8. Exact escape criterion and causal response formula

Let (J) be a positive rare block, (E_J=n^{-1}‖B_J‖_2^2), and
(U_J=n^{-1}‖Z_J^{\odot2}‖_2^2).  If on an interval

\[
Q\ge q_0,qquad H_{JJ}\succeq h_0I,qquad
\frac1nB_J^*H_{JC}B_C\ge-\rho E_J,qquad
\rho<h_0+q_0/4,                                          \tag{8.1}
\]

then, with (α=4q_0+16h_0-16\rho>0), (4.1) gives

\[
F_J'\ge U_J+\alpha E_J.                                  \tag{8.2}
\]

The algebraic inequality

\[
F_J^4\le pE_J^2U_J
\]

and one-variable minimization imply

\[
F_J'\ge \frac{3}{2^{2/3}}\alpha^{2/3}p^{-1/3}F_J^{4/3}. \tag{8.3}
\]

For joint (A,Z\asymp\ell) selection,
(F_J(0)\asymp p\ell^3), so (8.3) forces escape in
(O(\ell^{-1})).  Since (K\ge U_J+4q_0E_J), the stopped output must hit
every fixed sufficiently small (δ) before the comparison solution blows
up.  Thus (8.1)'s last inequality is an exact sufficient condition; no
rowwise positivity is needed.

The complement has an equally exact causal representation.  With

\[
M_C=2QI+8H_{CC},
\]

let (Φ_C(t,s)) be the propagator of the homogeneous complement equation
appearing in (Z_C').  Variation of constants gives

\[
H_{JC}(t)B_C(t)
=\beta_C(t)+\int_0^t\mathcal R(t,s)B_J(s),ds,            \tag{8.4}
\]

where

\[
\begin{aligned}
\beta_C(t)&=H_{JC}(t)D_{A_C(t)}\Phi_C(t,0)Z_C(0),\\
\mathcal R(t,s)&=8H_{JC}(t)D_{A_C(t)}
                  \Phi_C(t,s)H_{CJ}(s).
\end{aligned}                                            \tag{8.5}
\]

For frozen coefficients the signed controller is spectrally transparent.
If (S=M_C^{1/2}D_{A_C}M_C^{1/2}), then its response to a constant rare
forcing contains (e^{tS}-I).  The elementary spectral inequality
(e^{tS}-I\succeq tS), together with initial signed weighted-Wishart
concentration, makes the negative response (o(1)E_J) at time
(t=O(\ell^{-1})).  Conversely, (e^{tS}-I\succeq-I) and the Schur
complement show that an infinitely fast static response can saturate the
algebraic cancellation bound.  The distinction is therefore exactly causal.

At initialization the required estimate is true with room to spare:

\[
\frac{\langle Xr_Jr_C\rangle_n}{E_J}
=O_{\mathbb P}\!\left(
  \frac1{\ell^2\sqrt{np}}+p\ell^2\right)=o_{\mathbb P}(1). \tag{8.6}
\]

What is not yet proved is its stopped propagation through (8.4).  A sufficient
form is uniform control of the adaptive weighted cross Gram

\[
\big‖H_{J,N}(t)D_{-A_N(t)}H_{N,J}(t)\big‖_{\rm op}=O_{\mathbb P}(1) \tag{8.7}
\]

together with a leave-block-out estimate for (β_C).  Small normalized
(L^2) motion does not imply (8.7), because it permits concentration on a few
feature columns.  Thus (8.7), or a stronger spectral-lag substitute that
avoids it, is the current first probabilistic proof obligation.

## 9. Robust controlled-Riccati escape

The amount of adverse forcing actually needed to suppress one rare row has a
scale-invariant deterministic lower bound.  Consider

\[
a'=z^2,\qquad z'=\gamma(s)az+r(s),\qquad \gamma(s)\ge\gamma_0>0, \tag{9.1}
\]

with \(a(0),z(0)\in[L,2L]\).  There are constants
\(\varepsilon_0,C_0>0\), depending only on \(\gamma_0\), such that

\[
\int_0^{C_0/L}r(s)^2\,ds\le\varepsilon_0L^3            \tag{9.2}
\]

forces (9.1) to leave every bounded subset before \(C_0/L\).

One direct proof is a dyadic shell induction.  If at the start of a shell
\(a,z\ge S\), then on an interval \(c_0/S\) the negative integral of \(r\)
is at most

\[
\left(\frac{c_0}{S}\int r^2\right)^{1/2}
\le \sqrt{c_0\varepsilon_0}\,S,
\]

where the last inequality uses \(S\ge L\).  Choosing \(\varepsilon_0\) small
and \(c_0\) large makes this less than half of the positive drift supplied by
\(\gamma_0az\), while \(a'=z^2\) advances \(a\) through the same shell.  Thus
\((a,z)\) reaches the \(2S\) shell.  Summing the shell times gives
\(\sum_{k\ge0}c_0/(2^kL)=C_0/L\), whereas the single total control budget in
(9.2) becomes eight times smaller relative to each successive shell.

For a canonical row,

\[
\gamma_i=2Q+8H_{ii},\qquad
r_i=8\sum_{k\ne i}H_{ik}B_k,                             \tag{9.3}
\]

and the stopped lower bound on \(Q\) supplies the required \(\gamma_0\).  Hence
a single joint-tail row satisfying

\[
\int_0^{C_0/L}r_i(s)^2\,ds=o(L^3)                        \tag{9.4}
\]

forces the output to hit first: on a no-hit finite-width interval the exact
action bounds keep every coordinate finite, contradicting (9.1)'s escape.

This replaces the earlier weighted-primitive condition by a transparent
control-energy condition.  For an independent Gaussian background the
natural cavity scale is \(O(1)\) per unit feature time, so its cost over
\(O(L^{-1})\) is \(O(L^{-1})\), four powers below (9.4)'s threshold.  The
unresolved issue is again adaptive selection: the complement can in
principle synthesize a forcing of size \(L^2\) on the rare block at total
normalized cost \(pL^3=o(1)\).  Proving that the canonical causal response
does not create that alignment would complete the negative theorem.

## 10. Fixed-threshold double-limit audit

The tempting order

\[
\lim_{\ell\to\infty}\liminf_{n\to\infty}
\mathbb P\{\tau_{\delta,n}\le C_\delta/\ell\}
\]

does not by itself regularize the block operator.  For the narrow box
\(I_\ell=[\ell,\ell+c/\ell]\),

\[
p_\ell=\mathbb P\{A,Z\in I_\ell\}
\sim C_c\ell^{-2}e^{-2\ell^2/3}.                         \tag{10.1}
\]

At each fixed \(\ell\), let \(j_*\) maximize \(X_j(0)\).  Then
\(X_{j_*}(0)\sim2\log n\), while
\(\|G_{J,j_*}(0)\|_2^2\to p_\ell\).  Hence

\[
\lambda_{\max}\{H_{JJ}(0)\}
\ge X_{j_*}(0)\|G_{J,j_*}(0)\|_2^2
=(2p_\ell+o_{\mathbb P}(1))\log n\longrightarrow\infty.  \tag{10.2}
\]

Thus \(H_{JJ}\) is not uniformly close in operator norm to a scalar in the
\(n\)-first limit.  The stable-bulk lower bound (5.4) survives, because the
spike is positive semidefinite, but a proof may not replace the full block by
its mean.  Truncating \(X\) merely moves the obligation to an audited removal
of the omitted rank-one tail.

There is a second scale obstruction.  If

\[
F_J'\ge a_\ell F_J^{4/3}-E_J,\qquad
a_\ell\asymp p_\ell^{-1/3},
\]

then

\[
\frac d{ds}F_J^{-1/3}
\le-\frac{a_\ell}{3}+\frac{E_J}{3F_J^{4/3}}.             \tag{10.3}
\]

Since \(F_J(0)\asymp p_\ell\ell^3\to0\), an unweighted \(o(1)\) error can
erase the entire seed.  The required estimate is stage-weighted:

\[
\int_0^{C/\ell}E_J(s)F_J(s)^{-4/3}\,ds
=o\!\left(p_\ell^{-1/3}/\ell\right).                     \tag{10.4}
\]

The heuristic integrated background displacement
\(\sqrt{p_\ell}p_\ell^{-1/3}=p_\ell^{1/6}\) does not imply (10.4), and
same-time Gronwall is singular near the moving pole.  The double limit remains
a useful formulation of the desired theorem, but it does not replace the
causal weighted-work lemma.

## 11. Exact tagged-column transport and the superseded scalar spike

Fix a feature column \(j\), and write

\[
x=X_j,\qquad g=G_{\cdot j},\qquad
z=G_{\cdot,-j}X_{-j},\qquad Z=z+xg.
\]

Let

\[
h=g^*D_Ag,\qquad \rho=g^*D_Az,\qquad r=R_j=hx+\rho,
\qquad Q_-=\frac1n\|X_{-j}\|_2^2,
\]

and put \(H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^*\).  Direct
differentiation gives the exact equations

\[
x'=8xr,                                                   \tag{11.1}
\]

\[
h'=\sum_i g_i^2(z_i+xg_i)^2
+\frac{4x}{n}\sum_iA_i^2g_i(z_i+xg_i),                   \tag{11.2}
\]

and

\[
\rho'=x\,\mathcal P+\mathcal E_0+x^2\mathcal E_2,        \tag{11.3}
\]

where

\[
\begin{aligned}
\mathcal P={}&
\frac2n\sum_iA_i^2z_i^2
+2\sum_i g_i^2z_i^2
+2Q_-\sum_iA_i^2g_i^2
+8g^*D_AH_-D_Ag,\\
\mathcal E_0={}&
\sum_i g_i z_i^3
+2Q_-\sum_iA_i^2g_i z_i
+8g^*D_AH_-D_Az,\\
\mathcal E_2={}&
\frac2n\sum_iA_i^2g_i z_i+\sum_i g_i^3z_i .
\end{aligned}                                             \tag{11.4}
\]

Every term in \(\mathcal P\) is nonnegative.  At iid initialization,
uniformly for a marked \(x=O(\log n)\) whose selection only gives the column
a diffuse Gaussian tilt,

\[
\mathcal P\longrightarrow 6+6+6+8=26,\qquad
\mathcal E_0=O_{\mathbb P}(\sqrt{\log n}),\qquad
\mathcal E_2=O_{\mathbb P}(n^{-1}),                       \tag{11.5}
\]

and

\[
h'=3+o_{\mathbb P}(1),\qquad h(0)=O_{\mathbb P}(n^{-1/2}). \tag{11.6}
\]

The corresponding exact initialization contraction for \(r'\) is

\[
\mathbb E(r_j'\mid X)
=7Qx+8\langle X\rangle_nx+\frac{16x^2}{n}
=29x+\frac{7x^3}{n}+\frac{24x^2}{n}+o(x).                \tag{11.7}
\]

Equation (11.7) does **not** propagate as the scalar law
\(r'=29x+7x^3/n\).  The exact term \(8hxr\) in \(r'\) becomes leading
as soon as \(x/\log n\to\infty\).  This supersedes the earlier proposed
\(n^{3/5}\) frozen-bath spike.

The self-consistent outer candidate keeps the transported diagonal.  With
\(L=\sqrt{\log n}\), \(\tau=Ls\), and

\[
x=L^2U,\qquad h=H/L,\qquad \rho=LP,\qquad r=L(HU+P),
\]

(11.1)--(11.6) formally give

\[
\boxed{
U_\tau=8U(HU+P),\qquad H_\tau=3,\qquad P_\tau=26U.}       \tag{11.8}
\]

This system has a finite positive pole for every \(U(0)>0\) after the
initial adverse \(P(0)\) has turned around.  Near that pole,
\(r\sim hx\), so the exact marked action identity

\[
\int\frac{16}{n}xr^2\,ds=\frac2n\int r\,dx               \tag{11.9}
\]

predicts a fixed output increment already at

\[
x\asymp\sqrt{\frac n h}
\asymp n^{1/2}(\log n)^{1/4}.                            \tag{11.10}
\]

Unlike \(n^{3/5}\), this scale changes the marked output in each row only by
a polylogarithmic amount and leaves the column balance perturbation
\(x/(2n)=o(1)\).

Equations (11.1)--(11.4) are proved identities; (11.8)--(11.10) are a
candidate canonical concentration mechanism, not yet a theorem.  The exact
P7 obligation is twofold:

1. prove the tagged extreme limit (11.8), uniformly up to the first column
   reaching a slowly growing polylogarithmic multiple of \(\log n\); and
2. on the resulting stopped state, propagate
   \(h'\ge0\) and \(\rho'\ge c x\) until (11.10), or show that failure of
   either inequality has already spent a fixed amount of the kernel action.

A theorem at both stages would give a canonical initial layer and settle the
frozen closure conjecture negatively.  Initialization contractions alone do
not suffice.

## 12. Competing extreme poles: a strict column--row separation

This section records an exact comparison inside the two proposed outer
systems.  It does **not** yet assert the stopped extreme local law needed to
identify those systems with the finite network.

For a tagged column, let (V=HU+P).  Along (11.8), if (U(0)=a>0),
(H(0)=0), and (P(0)=b>0), then

\[
U_\tau=8UV,\qquad
V_\tau=29U+8HUV\ge29U.                                  \tag{12.1}
\]

Consequently

\[
V^2\ge b^2+\frac{29}{4}(U-a).                           \tag{12.2}
\]

Put (d^2=(29/4)a-b^2).  When (d^2>0), integration of
(dU/d\tau\ge8U\sqrt{b^2+(29/4)(U-a)}) gives the rigorous
outer-system pole bound

\[
T_{\rm col}(a,b)
\le \frac1{4d}
\left(\frac\pi2-\arctan\frac bd\right).                \tag{12.3}
\]

At initialization the natural large-deviation cost of the column type is

\[
I_{\rm col}(a,b)=\frac a2+\frac{b^2}{6}.                 \tag{12.4}
\]

The interior type (a=3/2,b=1) has (I_{\rm col}=11/12), hence a
polynomial number (n^{1/12+o(1)}) of candidates, and (12.3) gives

\[
T_{\rm col}(3/2,1)<0.1006.                              \tag{12.5}
\]

For comparison, a natural-scale extreme row has the proposed outer system

\[
a_\tau=z^2,\qquad z_\tau=14az,                           \tag{12.6}
\]

with invariant (z^2-14a^2) and Gaussian cost

\[
I_{\rm row}(a_0,z_0)=\frac{a_0^2}{2}+\frac{z_0^2}{6}.   \tag{12.7}
\]

The pole time in (12.6) is the elementary integral

\[
T_{\rm row}(a_0,z_0)
=\int_{a_0}^{\infty}
\frac{da}{z_0^2+14(a^2-a_0^2)}.                         \tag{12.8}
\]

Direct one-variable minimization of (12.8) on
(I_{\rm row}=1), with (a_0,z_0\ge0), gives

\[
\inf T_{\rm row}=0.11305\ldots .                        \tag{12.9}
\]

Thus the proposed outer dynamics have a strict, macroscopic rescaled-time
gap: the polynomial column family (12.5) reaches its pole before *any*
natural Gaussian row type can do so.  This is potentially the missing cure
for the sixth-moment obstruction in (11.4): a row-localized pulse cannot
arise before the first column passage if a simultaneous stopped extreme
local law is valid.

The exact P8 obligation is now sharply stated.  Before
(\tau=0.105), and stopped when either the kernel action is fixed or some
column first reaches (M L^2) for a sufficiently large fixed (M), prove
simultaneously that

1. all row tails remain in the pre-pole regime governed by (12.6);
2. the tagged-column contractions in (11.4) converge uniformly to the
   coefficients (3,26); and
3. at least one of the (n^{1/12+o(1)}) columns of type (12.5) reaches the
   column stop.

One must then prove a short post-stop transport to (11.10).  Mixed
row--column extremes, faster but rarer column shells, and adaptive Gaussian
conditioning are part of this one local-law obligation; they may not be
discarded by a pointwise moment bound.

## 13. Pole homogeneity, the rejected synchronized shell, and an independent tail bath

The column outer flow has the exact scaling

\[
(a,b,\tau)\mapsto(\lambda^2a,\lambda b,\tau/\lambda),
\qquad
T_{\rm col}(\lambda^2a,\lambda b)
=\lambda^{-1}T_{\rm col}(a,b).                         \tag{13.1}
\]

If

\[
T_*:=\inf\{T_{\rm col}(a,b):I_{\rm col}(a,b)\le1\},
\]

then every minimizer has cost one.  Moreover, for every \(\varepsilon>0\),

\[
\inf\{I_{\rm col}(a,b):T_{\rm col}(a,b)
       \le T_*+\varepsilon\}
=\left(\frac{T_*}{T_*+\varepsilon}\right)^2.           \tag{13.2}
\]

Indeed scaling a subcritical-cost type to cost one shortens its pole, which
gives the lower bound in (13.2); scaling a cost-one minimizer inward gives
equality.  Consequently a window

\[
\varepsilon_n=A\frac{\log L}{L^2},\qquad
L=\sqrt{\log n},                                       \tag{13.3}
\]

contains only a polylogarithmic number of possible early pole types, while a
slightly inward-scaled minimizer box contains a positive power of \(L\)
such types with high probability.  A clock depending only on \((a,b)\) is
not accurate enough to rank them: the \(\mathcal E_0\) term in (11.3) gives
a genuine tag-specific clock correction of order \(L^{-2}\).  Any valid
clock must retain the full quenched single-tag cavity data.

The earlier synchronized-shell repair is false.  Continuously distributed
pole times spread a shell of \(m\) candidates: near the first pole their
ordered sizes have the scale

\[
x_{(k)}\asymp \frac{L^2m}{k},\qquad
\sum_kx_{(k)}^2=O(L^4m^2),                              \tag{13.4}
\]

so a fixed fraction does not reach the action scale together.  Uniform
positivity for every laggard is false as well.  If column \(k\) is localized,
then the laggard cavity error contains

\[
8x_k^2(g_j^*D_Ag_k)(g_k^*D_A^2g_k),                    \tag{13.5}
\]

which has random sign and can make \(\rho_j\) negative.  The viable route is
therefore an isolated leader, not a synchronized block.

There is a clean way to avoid conditioning on a data-dependent candidate
set.  Let \(\mathcal M\) be the compact cost-one minimizer set for \(T_*\).
Since \(a=0\) gives \(U\equiv0\),

\[
a_*:=\min\{a:(a,b)\in\mathcal M\}>0.                   \tag{13.6}
\]

Fix \(0<a_0<a_*\) and define the initialization-measurable tail superset

\[
S_n:=\{j:X_j(0)\ge a_0L^2\}.                           \tag{13.7}
\]

It depends only on \(u\), hence is independent of \((A,G)\), and

\[
|S_n|=n^{1-a_0/2+o_{\mathbb P}(1)}=o(n),\qquad
\frac1n\sum_{j\in S_n}X_j(0)^2
=n^{-a_0/2+o_{\mathbb P}(1)}L^{O(1)}=o(1).             \tag{13.8}
\]

By compactness, every sufficiently near-fast column belongs to \(S_n\).
Delete all of \(S_n\) to form a common bath.  Conditional on that bath and
on \(X\), the columns \(g_j\), \(j\in S_n\), are genuinely independent
Gaussians.  The difference between a full initial score and its bath score
has the sharp uniform scale

\[
n^{-a_0/4}L^{O(1)},                                    \tag{13.9}
\]

not \(n^{-1/2}L^{O(1)}\), but (13.9) is smaller than every
fixed inverse power of \(L\).  Thus, once a quenched single-tag clock is
known to be \(C^1\) and radially transverse, an unconditional two-tag coarea
bound gives

\[
\mathbb E\#\{j\ne k:\ j,k\hbox{ early},
 |\widehat\Theta_j-\widehat\Theta_k|\le L^{-D}\}
\le L^C L^{-D}.                                        \tag{13.10}
\]

Choosing \(D>C\) produces an inverse-polylogarithmic clock gap without ever
conditioning on the selected early set.

The remaining P9 lemma is no longer a counting or selection statement.  It
is the following dynamical assertion: for the \(S_n\)-deleted bath, uniformly
over every reinserted near-fast tag, prove a stopped \(C^1\) cavity law and
radial transversality up to \(x=n^\gamma\), \(0<\gamma<1/2\), with row sixth
moments controlled by the strict gap (12.9).  The admissible instantaneous
full--cavity error scale is

\[
\eta_n=n^{-a_0/4}L^C+n^{\gamma-1/2}L^C=o(L^{-D}),       \tag{13.11}
\]

not the previously claimed \(n^{-1/2}L^C\).  Once (13.11) and the
corresponding integrated phase estimate are proved, the inverse-polylog
clock gap isolates one leader.  Equations (11.1)--(11.4) then give
\(r\ge cx/L\), and the exact identity (11.9) forces a fixed output increment
by \(x\asymp\sqrt{nL}\).  At present this stopped \(C^1\) bath theorem is the
single unresolved bridge to a canonical no-go result.
