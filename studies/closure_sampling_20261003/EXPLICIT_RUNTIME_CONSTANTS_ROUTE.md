# Explicit deterministic constants for the corrected-readout runtime

2026-10-04. Scoped derivation, frozen before reading sibling work or
receiving sibling source/label conclusions. Preliminary runtime progress
was reported to the coordinator before this final freeze.
This is a conditional deterministic calculation, not a new source theorem,
independent promotion review, or assertion of optimal constants. No other
study, experiment, maintained-book edit, or Git mutation was used.

The source interface coefficient is denoted by \(K\ge1\). Once the source
audit supplies an explicit \(K(d,L,B)\), every constant below is explicit in
\(d,L\) and the activation bound \(B\). In particular there is no remaining
constant described merely as depending on depth or dimension.

An especially simple, deliberately conservative certificate is

\[
 X=64B(K+1),\qquad Q=X^{16L+48},\qquad
 Y\le\lambda/Q.
 \tag{1}
\]

Subject also to the source theorem's own label condition, its initialized
gap event, and the unchanged source accuracy \(\epsilon=n^{-1}\le Y\),
the same autonomous runtime satisfies

\[
 \sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
 \le 40Q^2\frac{Y}{\lambda^{3/2}\sqrt n}.
 \tag{2}
\]

There is also a substantially less restrictive explicit label cap in (9)
below, with the fully displayed exponential coefficient (28). Thus (1)
is an optional simple certificate; its extra conservatism is not claimed
necessary. The powers of \(Y,\lambda,m,n\), the coordinate accuracy, and
the runtime are unchanged. No new width threshold is used to suppress an
exponential constant.

## 1. Precise input interface and activation norm

The network, metric construction, raw parameter evolution, internal
residual, and corrected readout are exactly equations (6)--(11) of
`STORAGE_QUADRATIC_IMPROVEMENT.md`. Inputs are \(v=x/\sqrt d\), with
\(\|v\|=1\); \(L\ge2\) is hidden depth, \(m\) is sample count, and
\(Y=\|y\|_2/\sqrt m\). All neuron norms use their fixed \(H_\ell\)
metrics and all sample operators use columns divided by \(\sqrt m\).
Hidden parameter norms are the Hilbert direct-sum norm of the first
matrix and weighted Hilbert--Schmidt mixer norms. A star is a Hilbert
adjoint, not the pointwise activation adjoint.

Take \(0<\lambda\le1\), and assume the realized initial normalized
top-feature Gram has gap at least \(\lambda/2\). The selected initial
Gram agrees with it exactly. Let \(K\ge1\) simultaneously bound:

1. every initialized dense mixer operator norm;
2. the multiplier in each coordinate approximation error \(K\epsilon\),
   for features, training backward responses, and **each member** of every
   paired forward/reverse initialized action;
3. the multiplier in the carrier event
   \(M\le1+KS\sqrt{\log(en)}\), where
   \(S=\int_0^T\rho_n(t)dt\) and \(M\) bounds the actual reference
   training-carrier coordinates through the source horizon.

Exact inclusion of the initial training features and forward images,
the initial first-layer columns, and the constant vector is as in the
assigned runtime source interface. These inputs must hold through
\(T=4\lambda^{-1}\log(en)\), or a larger specified horizon. Increasing
a previously chosen horizon to this value must be supported by the
source construction; it is not a conclusion of this deterministic note.

Set

\[
 B=\max\{1,\max_\ell\|\phi_\ell\|_\infty,
               \max_\ell\|\phi_\ell'\|_\infty,
               \max_\ell\|\phi_\ell''\|_\infty\}.
 \tag{3}
\]

For activations bounded by \(A\) on \(|\operatorname{Im}z|<a\), one
may use \(B=\max(1,A,2A/a,8A/a^2)\): the Cauchy integral formula on
radius \(a/2\) gives the last two bounds. This is an activation analytic
norm, with no implicit depth or dimension dependence.

The fixed metric obeys \(D/4\preceq H\preceq D\) and
\(\mathbf1^\top D\mathbf1\le4\). Thus a bounded feature has norm at
most \(2B\), and a diagonal multiplier has operator norm at most twice
its maximum entry. These facts account explicitly for every metric loss.

## 2. Global fitting and the actual smallness conditions

Define positive real constants

\[
 h=g=2B,\quad R=K+1,\quad
 \beta_\ell=g^{L-\ell+1}R^{L-\ell},\quad
 \beta=\max_\ell\beta_\ell,
\]
\[
 U=\left(\beta_1^2+h^2\sum_{\ell=2}^L\beta_\ell^2\right)^{1/2},
 \quad F_1=g,\quad F_\ell=g(h+RF_{\ell-1}),\quad
 F=\max_\ell F_\ell.
 \tag{4}
\]

Here \(U\|\widehat w_C\|\) bounds the norm of the hidden-direction
operator \(\mathcal J_C\). The constant \(F\) bounds the derivative
of every forward feature with respect to the hidden parameter tuple,
on the mixer tube \(\|B_C^{(\ell)}\|\le R\). For the first layer
the derivative costs \(g\); each later layer adds a matrix-direction
term of size \(gh\) and propagates the previous feature-direction
term with multiplier \(gR\). This proves the displayed recurrence.

Write \(s=Y/\lambda\) and \(\alpha=Y/\sqrt\lambda\). Stop the
compressed flow when a mixer reaches \(R\) or its normalized Gram
reaches \(\lambda/8\). The exact raw-parameter energy identity gives

\[
 \rho_C(t)\le Ye^{-\lambda t/4},\quad
 \int_0^\infty\rho_C\le4s,\quad
 \int_0^t\|\dot\theta_C\|\le\sqrt8\alpha<3\alpha.
 \tag{5}
\]

The corrected readout has orthogonal decomposition
\(\widehat w_C=(I-P_C)w_C+T_C(y-c_C)/\sqrt m\), where
\(T_C=V_C(V_C^*V_C)^{-1}\) and \(P_C=T_CV_C^*\).
Consequently

\[
 \|w_C\|\le3\alpha,\quad
 \|\widehat w_C\|\le\sqrt{40}\alpha<7\alpha,\quad
 \|\mathcal J_C\|\le7U\alpha,
\]
\[
 \|\theta_{h,C}(t)-\theta_{h,C}(0)\|
 \le56U s^2\sqrt\lambda,\quad
 \sup_{\ell,v}\|h_C^{(\ell)}(t,v)-h_C^{(\ell)}(0,v)\|
 \le56FU s^2\sqrt\lambda.
 \tag{6}
\]

The first hidden bound follows by integrating
\(\|\dot\theta_{h,C}\|\le14U\alpha\rho_C\); the second uses
the forward recurrence. If \(224FU s^2\le1\), the feature perturbation
is at most \(\sqrt\lambda/4\). Its normalized training operator has
the same bound by the RMS column estimate. The initial least singular
value is at least \(\sqrt{\lambda/2}\), so the new one is greater
than \(\sqrt{\lambda/8}\). The hidden displacement is at most
\(1/4\), giving a strict mixer margin too. Hence the stopping time
does not occur, and all these estimates hold globally. Finite path
length and the positive Gram margin give global continuation and a
fitted limit. The same estimates with the larger constants in (4)--(6)
also apply to the dense gradient flow: its activation and feature norm
constants are smaller and its raw readout is its effective readout.

For selected reference sources, coordinate error \(K\epsilon\)
and exact source isometry give
\(\|u_I\|\le\|u\|_n+3K\epsilon\). When
\(\epsilon\le\min(1,Y)\), put

\[
 D_\delta=3\beta+3K,\quad W=32(K+1),\quad
 J_0=h\sqrt L(7\beta+3K),\quad V_0=14FU.
 \tag{7}
\]

Then selected backward norms are at most \(D_\delta\alpha\), and
\(\|\mathcal J_C\|,\|\mathcal J_R\|\le J_0\alpha\).
The source transfer applied to the dense readout integral proves

\[
 \|w_R\|\le W\alpha,\quad
 \int_0^T\nu(t)dt\le(W/2)\alpha,\quad
 \nu=\|V_Rc_n/\sqrt m\|,\quad
 \|\dot V_C\|\le V_0\alpha\rho_C.
 \tag{8}
\]

For the middle estimate, source transfer gives
\(\nu\le\|V_nc_n/\sqrt m\|+3K\epsilon\rho_n\).
The first term integrates to at most \(3\alpha/2\) by dense path
length; the second is at most \(12K\epsilon s\le12K\alpha\)
for \(s\le1\). The readout transfer has twice that error.

A sufficient explicit runtime cap, used henceforth, is

\[
 c_{\rm rt}=\min\left\{1,(224FU)^{-1/2},(6J_0)^{-1}\right\},
 \qquad 0<s\le c_{\rm rt}.
 \tag{9}
\]

The last restriction is the additional smallness used in the geometric
comparison, rather than fitting alone. It is exactly the explicit
version of the original proof's instruction to shrink a structural
label constant; it adds no gap or sample-count power.

## 3. Source pairings, actions, and layer propagation

If \(u,v\) have coordinate source approximants with error
\(\delta=K\epsilon\), expansion around those approximants gives

\[
 |\langle u_I,v_I\rangle_H-\langle u,v\rangle_n|
 \le3\delta(\|u\|_n+\|v\|_n)+11\delta^2.
 \tag{10}
\]

Indeed, each selected cross term costs \(2\delta\) times an
approximant norm and each dense cross term costs \(\delta\); the
two error-error terms cost at most \(5\delta^2\). Replacing each
approximant norm by the actual norm plus \(\delta\) gives (10).
Thus valid coefficients for feature and response pairing errors are

\[
 P_h=6KB+11K^2,\quad P_\delta=18K\beta+11K^2,
 \qquad D_r=8P_h.
 \tag{11}
\]

The respective errors are at most \(P_h\epsilon\) and
\(P_\delta\alpha\epsilon\), since \(\epsilon\le\alpha\).
Integration against the reference residual gives both the training
readout defect and every query readout defect at most
\(D_r s\epsilon\).

An initialized paired action has norm defect at most
\(2K(K+1)\epsilon\). Its learned forward defect is at most
\(8D_\delta P_h s\alpha\epsilon\), and its learned reverse
defect is at most \(8hP_\delta s\alpha\epsilon\). These follow
directly by inserting (10) in the rank-one reference mixer integral;
the reference activity is at most \(4s\). Hence both orientations
are bounded by \(A_0\epsilon\), where

\[
 A_0=1+2K(K+1)+8D_\delta P_h+8hP_\delta,
 \qquad C_f=F(1+A_0).
 \tag{12}
\]

Let \(a\) denote the hidden tuple error from the selected reference
state. Forward subtraction gives, uniformly over all layers and queries,

\[
 \|z_C-z_{n,I}\|,\ \|h_C-h_{n,I}\|,\ \|V_C-V_R\|
 \le C_f(a+\epsilon).
 \tag{13}
\]

The first-layer preactivation costs \(a\). Later layers cost
\(ha+R\|\Delta h_{\ell-1}\|+A_0\epsilon\) before the gate.
The recurrence (4) multiplied by \(1+A_0\) bounds this expression,
since \(h\ge1\). Preactivation bounds are no larger than the same
envelope because \(g\ge1\).

Define the geometric errors exactly as in the assigned route:

\[
 e=(c_C-c_n)/\sqrt m,\quad u=\|e\|,\quad z=w_C-w_R,
 \quad p=T_Ce,\quad\zeta=z+p,\quad b=\|p\|+\|\zeta\|,
 \quad E=a+b,\quad r=\epsilon/\sqrt\lambda.
\]

All errors vanish initially. The exact corrected-readout difference is

\[
 \eta:=\widehat w_C-w_R
 =(I-P_C)\zeta-p-T_C(V_C-V_R)^*w_R-T_Cd_R,
\]

where \(d_R=V_R^*w_R-(y-c_n)/\sqrt m\). Since
\(\|T_C\|\le\sqrt8/\sqrt\lambda<3/\sqrt\lambda\), it follows that

\[
 \|\eta\|\le H_0[b+s(a+\epsilon)+sr],
 \qquad H_0=1+3WC_f+3D_r.
 \tag{14}
\]

For backward propagation define

\[
 Z_0=L(gR)^L(D_\delta+A_0+C_f),\qquad
 J_1=\sqrt L\{h\beta H_0+hZ_0+D_\delta C_f\}.
 \tag{15}
\]

The changed gate multiplies the actual reference carrier, so its norm
cost is at most \(gMC_f(a+\epsilon)\). The changed mixer costs
\(D_\delta\alpha a\), and the reverse source action costs
\(A_0\epsilon\), before multiplying by the next gate. Descending
through the layers adds at most \(L\) such contributions, each
propagated by powers of \(gR\). It gives

\[
 \max_{a,\ell}\|\delta_{C,a}^{(\ell)}-\delta_{n,a,I}^{(\ell)}\|
 \le\beta\|\eta\|+Z_0M(a+\epsilon),
\]
\[
 \|\mathcal J_C-\mathcal J_R\|
 \le J_1[b+M(a+\epsilon)+r].
 \tag{16}
\]

For the latter, a mixer-direction difference costs at most \(h\) times
the response difference plus \(D_\delta\alpha C_f(a+\epsilon)\).
The tuple norm adds at most \(\sqrt L\); normalized sample columns
introduce no factor of \(m\). The carrier factor is added once per
layer, rather than multiplied repeatedly.

Finally the source-only normalized Gram error
\(D=V_R^*V_R+\mathcal J_R^*\mathcal J_R-K_n/m\) satisfies

\[
 \|D\|\le D_0\epsilon,\qquad
 D_0=P_h+L(P_\delta h^2+9\beta^2P_h).
 \tag{17}
\]

The response-pair contribution costs \(P_\delta\alpha\epsilon\)
times a feature pairing bounded by \(h^2\); the feature-pair
contribution costs \(P_h\epsilon\) times a dense response pairing
bounded by \(9\beta^2\alpha^2\). Dropping \(\alpha\le1\)
gives (17), including the first-layer term. Dividing entries by \(m\)
then taking the matrix norm removes the apparent entry-count factor.

## 4. Quantified geometric cancellation and raw exponent

Let \(\Delta\mathcal K=K_C/m-K_n/m\),
\(\Delta V=V_C-V_R\), and \(\Delta\mathcal J=\mathcal J_C-\mathcal J_R\).
The exact identity

\[
 \Delta\mathcal K=V_C^*\Delta V+\Delta V^*V_R
       +\mathcal J_C^*\Delta\mathcal J
       +\Delta\mathcal J^*\mathcal J_R+D
\]

and \(T_CV_C^*=P_C\) bound the lifted forcing
\(\mathscr F=2\|T_C\Delta\mathcal K c_n/\sqrt m\|\) by

\[
\begin{split}
 \mathscr F\le{}&[2C_f\rho_n+6C_f\nu/\sqrt\lambda
                  +12J_0J_1sM\rho_n](a+\epsilon)\\
 &+12J_0J_1s\rho_n b+(12J_0J_1s+6D_0)\rho_n r.
\end{split}
 \tag{18}
\]

Put

\[
 \mathscr A=M\rho_n+\rho_C+\nu/\sqrt\lambda,\quad
 F_0=8C_f+24J_0J_1+6D_0,\quad T_0'=6V_0.
 \tag{19}
\]

Then \(\mathscr F\le F_0\mathscr A(E+r)\). Differentiating
\(T_C\) in its projection form gives

\[
 \dot T_C=(I-P_C)\dot V_C(V_C^*V_C)^{-1}
                         -T_C\dot V_C^*T_C,
 \qquad\|\dot T_Ce\|\le T_0's\rho_C\|p\|.
\]

The lifted residual energy therefore obeys

\[
 \tfrac12\partial_t\|p\|^2
 \le[-2+18J_0^2s^2]u^2+T_0's\rho_C\|p\|^2+\|p\|\mathscr F.
\]

The cap \(6J_0s\le1\) makes the bracket at most \(-1\). With
\(I(t)=\int_0^t(T_0's\rho_C\|p\|+\mathscr F)\), integration gives

\[
 \|p(t)\|+\int_0^t u^2/\|p\|\le I(t),\qquad
 \int_0^tu\le3I(t)/\sqrt\lambda.
 \tag{20}
\]

At \(p=0\), also \(e=0\). Apply the inequality first to
\((\|p\|^2+\delta^2)^{1/2}\), integrate, then let
\(\delta\downarrow0\); monotone convergence justifies the nonnegative
damping integral with quotient defined as zero at \(p=e=0\).

The readout cancellation is exact:

\[
 \dot\zeta=2\Delta Vc_n/\sqrt m+\dot T_Ce
             -2T_C\mathcal J_C^*\mathcal J_Ce
             -2T_C\Delta\mathcal Kc_n/\sqrt m.
\]

Its integrated hidden-Gram term is at most
\(18J_0^2s^2I\le I\). Combining with (20), and then bounding the
hidden parameter difference, yields

\[
 b(t)\le2C_f\int_0^t\rho_n(a+\epsilon)+3I(t),
 \quad
 a(t)\le I(t)+2J_1\int_0^t\mathscr A(E+r).
\]

The coefficient \(I\) in the latter uses
\(2J_0\alpha\int u\le6J_0sI\le I\). Therefore, with

\[
 G=4(T_0'+F_0)+2C_f+2J_1,
\]

the error satisfies

\[
 E(t)\le G\int_0^t\mathscr A(E+r),\qquad
 E(t)\le r\left[\exp\left(G\int_0^t\mathscr A\right)-1\right].
 \tag{21}
\]

The latter follows by differentiating the integral majorant plus its
constant initial value \(r\), so it retains the zero-error initial
condition. From (5), (8), and the carrier event,

\[
 \int_0^T\mathscr A\le[4M+4+W/2]s,
 \qquad M\le1+4Ks\sqrt{\log(en)}.
\]

Define

\[
 C_1=G(8+W/2),\qquad C_2=16KG,\qquad
 O_0=2hH_0+WC_f+D_r.
 \tag{22}
\]

For \(q=\sqrt{\log(en)}\), the explicit raw exponent is thus
\(C_1s+C_2s^2q\). The query output decomposition, using (13)--(14)
and its source pairing defect, gives the label-retaining estimate

\[
 \sup_{t\le T,v}|f_C-f_n|
 \le O_0\frac\epsilon{\sqrt\lambda}
       [s+e^{C_1s+C_2s^2q}-1].
 \tag{23}
\]

Every coefficient in this formula was explicitly defined. No bound on a
compressed coordinate carrier or minimum selected mass was used, and no
source approximation was differentiated.

## 5. Explicit tail and strict root-width coefficient

The same projection identities give

\[
 \|\dot T_C\|\le16\lambda^{-1}\|\dot V_C\|,
 \qquad\|\dot P_C\|\le6\lambda^{-1/2}\|\dot V_C\|.
\]

Since \(\|\dot w_C\|\le2h\rho_C\),
\(\|(y-c_C)/\sqrt m\|\le2Y\), and
\(\|\dot c_C\|_m\le2(h^2+J_0^2\alpha^2)\rho_C\), differentiation
of the corrected readout gives

\[
 \|\dot{\widehat w}_C\|\le W_1\lambda^{-1/2}\rho_C,
 \quad W_1=2h+50V_0+6(h^2+J_0^2).
\]

Here the \(50V_0\) is the sum of the projection and right-inverse
motion contributions, \(18V_0+32V_0\), after using \(s,\lambda\le1\).
The query feature derivative is at most \(V_0\alpha\rho_C\), hence
with

\[
 T_1=hW_1+7V_0
\]

the compressed prediction speed is at most
\(T_1\lambda^{-1/2}\rho_C\). The dense prediction speed is at most
\((2B^2+3V_0)\rho_n\le T_1\lambda^{-1/2}\rho_n\).
Both integrated tails are consequently bounded by

\[
 4T_1Y\lambda^{-3/2}e^{-\lambda t/4}.
 \tag{24}
\]

This controls every increment after \(T\), as well as the endpoint.
Combining (23)--(24) gives the raw all-time bound

\[
 \sup_{t\in[0,\infty],v}|f_C-f_n|
 \le O_0\frac\epsilon{\sqrt\lambda}
            [s+e^{C_1s+C_2s^2q}-1]
       +8T_1Y\lambda^{-3/2}e^{-\lambda T/4}.
 \tag{25}
\]

Let \(c\le c_{\rm rt}\) be any explicit common source/runtime cap,
with \(s\le c\). The inequalities

\[
 e^{C_1s+C_2s^2q}-1
 \le s(C_1+C_2cq)e^{C_1c+C_2c^2q},\qquad
 C_2c^2q\le q^2/4+C_2^2c^4,
\]

and \(\sup_{q\ge0}qe^{-q^2/4}=\sqrt{2/e}<1\) prove

\[
 n^{-1}[s+e^{C_1s+C_2s^2q}-1]
 \le\frac{s}{\sqrt n}
       [1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}].
 \tag{26}
\]

The factor \(\sqrt e\) comes from
\(n^{-1/2}=\sqrt e\,e^{-q^2/2}\). With
\(T=4\lambda^{-1}\log(en)\), (25) therefore yields

\[
 \sup_{t,v}|f_C-f_n|
 \le C_{\rm err}(K,L,B,c)\frac{Y}{\lambda^{3/2}\sqrt n},
 \tag{27}
\]
\[
 C_{\rm err}
 =O_0[1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}]+8T_1.
 \tag{28}
\]

This is a completely computable coefficient, with (4), (7), (11)--(12),
(14)--(15), (17), (19), and (22) defining its inputs. The source theorem
may require a smaller explicit \(c\); that only improves (28).

## 6. A single elementary envelope, and what remains conditional

For a shorter closed expression, set \(X=64B(K+1)\ge128\). Elementary
bounds on the preceding definitions give

\[
\begin{array}{c|c@{\qquad}c|c}
 \beta&X^L&U&X^{2L+1}\\
 F&X^{2L+2}&D_\delta&X^{L+1}\\
 J_0&X^{2L+3}&P_h&X^3\\
 P_\delta&X^{L+2}&A_0&X^{L+5}\\
 C_f&X^{3L+8}&H_0&X^{3L+10}\\
 Z_0&X^{5L+9}&J_1&X^{6L+12}\\
 D_0&X^{3L+5}&V_0&X^{4L+4}\\
 F_0&X^{8L+17}&G&X^{8L+19}\\
 C_1,C_2&X^{8L+21}&O_0&X^{3L+13}\\
 T_1&X^{4L+10}&&
\end{array}
 \tag{29}
\]

Each entry is an upper bound, not a definition. For example,
\(\sqrt L\le X^L\), \(gR\le X\), and the recurrence for \(F\)
has at most \(L\) terms each at most \(h(gR)^L\), giving the first
two rows; substitution and addition give the subsequent rows. The
generous exponent \(16L+48\) in (1) is larger than all exponents in
(29) and also bounds \(6J_0\) and \(\sqrt{224FU}\). Thus
\(Q^{-1}\le c_{\rm rt}\) and all of \(C_1,C_2,O_0,T_1\) are at
most \(Q\). At \(c\le Q^{-1}\), the exponential in (28) is at most
\(e^2\), and

\[
 C_{\rm err}\le
 Q[1+2e^2(Q+1)]+8Q<40Q^2.
\]

This proves (1)--(2). It trades a conservative explicit label coefficient
for a coefficient that is an explicit power of \(B(K+1)\). Using
(9) and (28) instead avoids that extra label restriction while keeping
all dependence visible.

The remaining scientific input is genuinely the source interface: this
note does not turn an unspecified source coefficient \(K\) into an
explicit function of \(d,L\), prove its probability event, or quantify
its sufficiently-large-width threshold. Once supplied, substitution
completes the requested dimension/depth accounting. There is no direct
dimension factor in the deterministic runtime because \(\|v\|=1\)
and all training operators are normalized by \(\sqrt m\). Zero labels
give the exact stationary zero predictor separately and require neither
\(n^{-1}\le Y\) nor a limit of this positive-label argument.

## Inputs and freeze

The complete scientific sources read were:

| File | SHA-256 |
| --- | --- |
| `ERROR_PREFACTOR_GEOMETRIC_ROUTE.md` | `2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c` |
| `ERROR_PREFACTOR_GEOMETRIC_CHECK.md` | `1238193e77ec198a4493104d0142b21c455c7ab928d2e0c9b530c98587126bf6` |
| `ERROR_PREFACTOR_REFINEMENT.md` | `78d06ebff561b20917c1e65088e18a4eae0a93bcbd6fa050d522ec490f47805c` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| `STORAGE_QUADRATIC_CHECK.md` | `b373ee9212997c6e60002b2cf0ad613b6b58865ab82cc9589bc70931603724d9` |
| `DATASET_LABEL_DEPENDENCE.md` | `bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52` |

The canonical-notation skill, its neural-response reference, and the
rigorous-math skill were read and applied. The route requires a separate
reconstruction of its numerical constants before being described as
internally checked.
