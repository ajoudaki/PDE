# Shifted harmonic activation: current damping and the full causal response

Bounded theoretical sidecar, 2026-09-06. No claim to the final theorem.
Only the activation

\[
 \phi(z)=1+\varepsilon(\sin z+\cos z),\qquad \varepsilon=1/20
 \tag{1}
\]

is considered, in all three hidden layers, with opposite labels. The
architecture, Gaussian initialization, raw parameter metric, optimizer,
and physical scaling in the contract are unchanged. No experiments or
other agents were used. Only this file was written.

**Result.** The current top forward-source response is exactly
\(-f_{ka}\), with no historical-source identification. This gives a
mesh/cap-independent bound and an exact accumulated signed identity for
that actual response block on any finite feature interval. The full
retarded response additionally contains a curvature--sensitivity
covariance. An explicit second-update calculation in the prescribed
finite causal Gaussian law proves that its label-weighted contribution
is strictly positive at its first nonzero order. Both trained matrices
enter that coefficient. The middle response has a further uncancelled
curvature--query--sensitivity product. No new signed bound for the full
response on an arbitrary existing finite feature interval is established.
The old absolute-response bootstrap on \([0,3/2]\) transfers, with the
gate-sign correction specified below; it is not a consequence newly
obtained from damping.

## 1. Sources, scope, and exact normalization

The following four requested sources were read completely. SHA256 hashes
are of the bytes read, not of a hash mentioned inside an older ledger.
Paths in the first five rows have prefix
`/tmp/l3-two-sample-proof-DLuelg/`.

| Source | SHA256 | Use |
|---|---|---|
| `CONTRACT_AND_LEDGER.md` | `c52abcd4fdec0ce4ebb3689cf84cc2c4843aee086aff4b39095f22291fa44fff` | Canonical model and claim boundaries; full read |
| `ROUTE_REGISTRY.md` | `b6c893aca8bc1fc4e966c6ccb231ddf9826b7cd7e0cac40249801db1cbd1d5f8` | Closed routes; full read |
| `TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` | Finite scalar-law definition and elementary local estimates; full read |
| `ACTIVATION_STRUCTURE_ROUTE.md` | `8c90cd38714f88b2944af6650056ed00b7f2afefc040ce7ecae2407a7ac9ab2d` | Prior unshifted-harmonic route and its limits; full read |
| `SAME_LABEL_NONTRIVIALITY.md` | `76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6` | Full read solely to identify nontransferable positive-gate arguments |

The following were searched for dependency locations, not imported as
theorems: `EXACT_TWO_SAMPLE_REDUCTION.md`, SHA256
`432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60`;
`SAME_LABEL_GLOBAL_ASSEMBLY.md`, SHA256
`510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44`;
and `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`,
SHA256 `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`.
The last source's positive-gate conclusions near lines 1580--1595 and
1723--1782 were also read. Its finite-program identification theorem is
**not** an imported conclusion of this sidecar. All new response identities
below are proved directly in the finite Gaussian scalar law (4)--(6).
No specialized external theorem is used.

The investigate-conjectures skill and its research-contract,
evidence-ledger, and adversarial-audit references were read. Their role
here is to keep finite identities, local bounds, and unproved continuation
claims separate; no change to the program ledger is made.

Let \(y=(1,-1)\); reversing both labels and the readout gives the other
opposite-label ordering. Let \(C_{aa}=1\), \(C_{12}=\rho\in[-1,1)\).
The first root pair is centered Gaussian with covariance \(C\). The two
initial hidden matrices have independent \(N(0,1/n)\) entries. The
contract's rescaled readout has independent \(N(0,n^{-2})\) entries.
Its limiting scalar root is zero. Using zero readout in the scalar law
is the bootstrap's limiting-root convention, not a replacement of the
contract's finite-width initialization.

The loss is \(L=\sum_a(f_a-y_a)^2\). Physical GF has matrix velocities
\(-2\sum_a r_a\delta^{(\ell)}_a(H^{(\ell-1)}_a)^T/n\), readout
velocity \(-2\sum_a r_a H^{(3)}_a\), and bottom preactivation velocity
\(-2\sum_a C_{ba}r_a\delta^{(1)}_a\). On an existing symmetric uncut
population path, write \(f_a=y_a g\). Before fitting, the feature clock
\(ds/dt=4(1-g)\) gives the following feature Euler increments, with
\(\lambda=\Delta/2\):

\[
 \begin{aligned}
 W^{(\ell)}_{k+1}-W^{(\ell)}_k
  &=\frac{\lambda}{n}\sum_b y_b\delta^{(\ell)}_{kb}
                              (H^{(\ell-1)}_{kb})^T,\\
 w_{k+1}-w_k&=\lambda\sum_b y_b H^{(3)}_{kb},\\
 Z^{(1)}_{k+1,a}-Z^{(1)}_{ka}
  &=\lambda\sum_b C_{ab}y_b\gamma^{(1)}_{kb}
                                      \tau_1(q^{(1)}_{kb}).
 \end{aligned}                                                    \tag{2}
\]

Here and below \(w=W^{(4)}\), and

\[
 h(z)=\phi(z)-1,\quad \gamma(z)=\phi'(z),\quad
 h'=\gamma,\quad\gamma'=-h,\quad h^2+\gamma^2=b^2,
 \qquad b=\frac{\sqrt2}{20},\quad b^2=\frac1{200}.
 \tag{3}
\]

Thus \(m=5/6<\phi<a=7/6\), \(|\gamma|\le b<e=1/10\), and
\(|\phi''|\le b<c=1/5\). Lowercase \(h\) always means the centered
activation, not the feature \(H=\phi(Z)\).

The functions \(\tau_j=\tau_{R_j}\), \(R_j\ge1\), are exactly the
bootstrap's odd analytical reference cuts: identity on \([-R_j,R_j]\),
\(|\tau_j(q)|\le |q|\), and \(0\le\tau'_j\le1\). Uncut equations
mean \(\tau_j(q)=q\). These are reference laws, not proposed changes to
the optimizer. No physical-time or cap-removal conclusion is inferred
merely by writing them.

## 2. Complete finite causal law and symmetry

Use indices \(i=(k,a)\), \(j=(r,b)\); \(j\prec i\) means \(r<k\),
with both samples summed. Sources at different times/samples remain
distinct formal arguments, even when equal almost surely. For any finite
prefix \(0\le k\le M\), \(S=M\Delta\), the law under investigation is

\[
\begin{aligned}
 Z^{(1)}_{ka}
  &=G_a+\lambda\sum_{r<k,b}C_{ab}y_b
                  \gamma^{(1)}_{rb}\tau_1(q^{(1)}_{rb}),\\
 H^{(\ell)}_i&=\phi(Z^{(\ell)}_i),\\
 Z^{(\ell)}_i&=\xi^{(\ell)}_i+
                     \sum_{j\prec i}A^{(\ell)}_{i,j}\delta^{(\ell)}_j,
                                                   \quad\ell=2,3,\\
 w_k&=\lambda\sum_{r<k,b}y_b H^{(3)}_{rb},
       \qquad\delta^{(3)}_i=w_k\gamma^{(3)}_i,\\
 q^{(2)}_i&=\zeta^{(2)}_i+
                         \sum_{r\le k,b}B^{(3)}_{i,rb}H^{(2)}_{rb},
       \qquad\delta^{(2)}_i=\gamma^{(2)}_i\tau_2(q^{(2)}_i),\\
 q^{(1)}_i&=\zeta^{(1)}_i+
                         \sum_{r\le k,b}B^{(2)}_{i,rb}H^{(1)}_{rb}.
\end{aligned}                                                       \tag{4}
\]

The four centered Gaussian source groups are mutually independent and
independent of \(G\); within each group retain the entire covariance:

\[
 \mathbb E\xi^{(\ell)}_i\xi^{(\ell)}_j
       =\mathbb E H^{(\ell-1)}_iH^{(\ell-1)}_j,
 \qquad
 \mathbb E\zeta^{(\ell-1)}_i\zeta^{(\ell-1)}_j
       =\mathbb E\delta^{(\ell)}_i\delta^{(\ell)}_j.
 \tag{5}
\]

The deterministic coefficients, including **both trained matrices**, are

\[
\begin{aligned}
 A^{(\ell)}_{i,j}
  &=\mathbb E\partial_{\zeta^{(\ell-1)}_j}H^{(\ell-1)}_i
       +\lambda y_b\mathbb E H^{(\ell-1)}_iH^{(\ell-1)}_j,
                                                    &&j\prec i,\\
 B^{(\ell)}_{i,j}
  &=\mathbb E\partial_{\xi^{(\ell)}_j}\delta^{(\ell)}_i
       +\lambda\mathbf1_{r<k}y_b
                     \mathbb E\delta^{(\ell)}_i\delta^{(\ell)}_j,
                                                    &&r\le k.
\end{aligned}                                                       \tag{6}
\]

All source derivatives hold the selected deterministic coefficients and
Gaussian covariance parameters fixed. This is the definition of these
source-response coefficients. It does not freeze a trained matrix:
the second terms of both lines of (6) are its learned forward and
transpose actions, respectively. Differentiating the *law* or comparing
two laws would additionally vary these deterministic statistics; that is
a different derivative, and no comparison estimate for it is asserted.

All expectations of the displayed finite source derivatives exist. At
fixed finite caps this follows by finite smooth differentiation with
bounded gates and clipped factors. In the uncut finite law, each query
is its Gaussian source plus a bounded deterministic-coefficient feature
sum. Finite induction bounds every first derivative by a polynomial in
the finitely many absolute Gaussian coordinates, with finite constants
for that prefix. Gaussian polynomial moments are finite. This statement
asserts no mesh/cap-uniform bound on those constants.

For completeness, the learned terms follow immediately by unrolling (2):
the forward action pairs each old lower feature with the current lower
feature; the transpose action pairs each old delta with the current
delta. The expected-derivative terms are part of the stipulated Gaussian
law, not derived here from an unaudited width limit. Consequently
"canonical test" below means a test in this specified Gaussian Euler
law, not a new finite-width identification or convergence theorem.

Let \(\pi\) swap the two samples. The symmetry transformation is

\[
 (G,Z,H,\xi)_a\mapsto(G,Z,H,\xi)_{\pi a},\qquad
 (w,\delta_a,q_a,\zeta_a)
                  \mapsto(-w,-\delta_{\pi a},-q_{\pi a},-\zeta_{\pi a}).
 \tag{7}
\]

Indeed \(y_{\pi b}=-y_b\), \(C_{\pi a,\pi b}=C_{ab}\), and the cuts
are odd. Substitution in the bottom/readout updates and all forward and
reverse equations verifies (7). In (6) a derivative of an even-type
field with respect to an odd-type source, or the reverse, changes sign;
the learned terms do also. Thus
\(A_{\pi i,\pi j}=-A_{i,j}\), \(B_{\pi i,\pi j}=-B_{i,j}\).
Covariances (5) are unchanged by the corresponding signed permutations.

Starting with the exchange-invariant Gaussian root, the finite causal
construction preserves these statements inductively: construct bottom
fields, \(A^{(2)},Z^{(2)},A^{(3)},Z^{(3)},\delta^{(3)},B^{(3)},q^{(2)},
\delta^{(2)},B^{(2)},q^{(1)}\) in causal order. At each selection, both
the Gaussian covariance and the coefficient expectation have the stated
equivariance. This argument allows singular covariances, and does not
need a continuous-time uniqueness theorem. Therefore, in this law,

\[
 \mathbb Ew_k=0,\qquad f_{ka}:=\mathbb E[w_kH^{(3)}_{ka}]=y_a g_k,
 \qquad \mathbb E[w_kh^{(3)}_{ka}]=f_{ka}.
 \tag{8}
\]

Finite-width exchange is a symmetry in law, not equality of its two
sample predictions on each realization. Equation (8) is used for the
deterministic Gaussian law only.

## 3. Full retarded source variations

The following are exact finite equations, with no factorization of a
random sensitivity from a random field. Let \(v\) be an arbitrary
deterministic direction in the formal source slots. Write
\(P^{(\ell)}=D_vZ^{(\ell)}\), \(T^{(\ell)}=D_v\delta^{(\ell)}\),
\(Q^{(j)}=D_vq^{(j)}\), and \(u_k=D_vw_k\). Superscripts on \(v\)
identify its root or source group. Sources absent from a given variation
have direction zero. Fixed coefficients separate the local source maps;
their expectations are coupled again through (6).

At the bottom the full system is

\[
\begin{aligned}
 P^{(1)}_{ka}=v^G_a+\lambda\sum_{r<k,b}C_{ab}y_b
 \left[-h^{(1)}_{rb}\tau_1(q^{(1)}_{rb})P^{(1)}_{rb}
       +\gamma^{(1)}_{rb}\tau'_1(q^{(1)}_{rb})Q^{(1)}_{rb}\right],\\
 Q^{(1)}_{ka}=v^{\zeta^1}_{ka}
              +\sum_{r\le k,b}B^{(2)}_{ka,rb}
                                   \gamma^{(1)}_{rb}P^{(1)}_{rb},
 \qquad D_vH^{(1)}_i=\gamma^{(1)}_iP^{(1)}_i.
\end{aligned}                                                       \tag{9}
\]

At the middle,

\[
\begin{aligned}
 P^{(2)}_i&=v^{\xi^2}_i+\sum_{j\prec i}A^{(2)}_{i,j}T^{(2)}_j,\\
 Q^{(2)}_i&=v^{\zeta^2}_i+\sum_{r\le k,b}B^{(3)}_{i,rb}
                                   \gamma^{(2)}_{rb}P^{(2)}_{rb},\\
 T^{(2)}_i&=-h^{(2)}_i\tau_2(q^{(2)}_i)P^{(2)}_i
                  +\gamma^{(2)}_i\tau'_2(q^{(2)}_i)Q^{(2)}_i,
 \qquad D_vH^{(2)}_i=\gamma^{(2)}_iP^{(2)}_i.
\end{aligned}                                                       \tag{10}
\]

At the top,

\[
\begin{aligned}
 P^{(3)}_i&=v^{\xi^3}_i+\sum_{j\prec i}A^{(3)}_{i,j}T^{(3)}_j,\\
 u_k&=\lambda\sum_{r<k,b}y_b\gamma^{(3)}_{rb}P^{(3)}_{rb},\\
 T^{(3)}_i&=\gamma^{(3)}_i u_k-w_kh^{(3)}_iP^{(3)}_i.
\end{aligned}                                                       \tag{11}
\]

Equations (9)--(11) follow by the product and chain rules, using
\(\gamma'=-h\). They include the variation of the accumulated readout,
the current reverse returns, and every historical forward and reverse
return. In particular, deleting \(u_k\) is not a valid top response
calculation.

To recover all coefficients in (6), use unit forward-source directions
in (10)--(11) and unit reverse-source directions in (9)--(10). For example,
if \(D^{(\ell)}_{i,j}=\mathbb E\partial_{\xi^{(\ell)}_j}
\delta^{(\ell)}_i\) and
\(S^{(j)}_{i,p}=\mathbb E\partial_{\zeta^{(j)}_p}H^{(j)}_i\), then

\[
 A^{(2)}=S^{(1)}+\lambda y\,\mathbb E H^{(1)}H^{(1)},\quad
 A^{(3)}=S^{(2)}+\lambda y\,\mathbb E H^{(2)}H^{(2)},\qquad
 B^{(\ell)}=D^{(\ell)}+
       \lambda\mathbf1_{\mathrm{past}}y\,\mathbb E\delta^{(\ell)}\delta^{(\ell)}.
 \tag{12}
\]

The componentwise placement of \(y_b\) is exactly (6); (12) is only
shorthand. Neither hidden matrix is omitted or treated as its initial
action. A later response bound must close this entire loop of deterministic
statistics, not just the top local source map.

## 4. The exact current blocks and a new bounded actual response

For the source slot \(\xi^{(3)}_{kb}\), strict causality gives
\(\partial w_k=0\), \(\partial Z^{(3)}_{ka}=\mathbf1_{a=b}\), and
zero derivatives of all fields at earlier times. Thus

\[
 D^{(3)}_{ka,kb}=B^{(3)}_{ka,kb}
  =\mathbf1_{a=b}\mathbb E[w_k\phi''(Z^{(3)}_{ka})]
  =-\mathbf1_{a=b}f_{ka}.
 \tag{13}
\]

There is no learned same-time term in (6). In particular (13) is an
actual deterministic response coefficient, not a trace, a neuronwise
curvature bound, or a derivative of a reduced expression with coincident
Gaussian slots merged.

Substitute (13) into (10). Put
\(\kappa_i=(\gamma^{(2)}_i)^2\tau'_2(q^{(2)}_i)\ge0\). Then

\[
\begin{aligned}
 T^{(2)}_i={}&[-h^{(2)}_i\tau_2(q^{(2)}_i)-f_i\kappa_i]P^{(2)}_i\\
 &+\gamma^{(2)}_i\tau'_2(q^{(2)}_i)
   \left[v^{\zeta^2}_i+
           \sum_{j\prec i}B^{(3)}_{i,j}\gamma^{(2)}_jP^{(2)}_j\right].
\end{aligned}                                                       \tag{14}
\]

For a current middle forward-source slot the historical terms vanish,
so its exact block is

\[
 B^{(2)}_{ka,kb}=\mathbf1_{a=b}
 \left\{-\mathbb E[h^{(2)}_{ka}\tau_2(q^{(2)}_{ka})]
       -f_{ka}\mathbb E[(\gamma^{(2)}_{ka})^2
                                      \tau'_2(q^{(2)}_{ka})]\right\}.
 \tag{15}
\]

The second term is the propagated current damping. The first is not
removed by \(\mathbb Ew=0\): it involves a different neuron population
and its entire trained transpose query.

There is a useful global-in-feature-length bound for (13) alone. Define
\(V_k=(H^{(3)}_{k1}-H^{(3)}_{k2})/2\). Since the constant shift cancels,
\(|V_k|\le b\), \(w_{k+1}=w_k+\Delta V_k\), and hence

\[
 |w_k|\le b s_k,\qquad
 |f_{ka}|=|\mathbb E[w_kh^{(3)}_{ka}]|
         \le b^2s_k=\frac{s_k}{200},\qquad s_k=k\Delta.
 \tag{16}
\]

Thus the current two-by-two top response block has operator norm at
most \(s_k/200\), uniformly in the mesh, both caps, and \(\rho\).
Its actual contribution to the query is
\(-f_{ka}H^{(2)}_{ka}\), of absolute value at most \(a s_k/200\).
This is a control of that specified contribution, not of the sum over
all source times.

By (8), \(\mathbb E[w_kV_k]=g_k\). Squaring the readout update and
taking expectations gives the exact finite identity

\[
 2\Delta\sum_{k<M}g_k
   =\mathbb Ew_M^2-\Delta^2\sum_{k<M}\mathbb EV_k^2,
 \qquad
 \Delta\sum_{k<M}y_aB^{(3)}_{ka,ka}
   =-\frac12\mathbb Ew_M^2+
                         \frac{\Delta^2}{2}\sum_{k<M}\mathbb EV_k^2.
 \tag{17}
\]

Consequently

\[
 -\frac{b^2S\Delta}{2}\le\Delta\sum_{k<M}g_k
                                  \le\frac{b^2S^2}{2}.
 \tag{18}
\]

This is a genuine mesh/cap-independent accumulated **signed current
response** estimate, with a vanishing mesh defect. On any already
constructed continuous path where these expectations pass to the limit,
it becomes \(\int_0^S g(s)\,ds=\mathbb Ew(S)^2/2\).
The finite identity itself needs no such passage.

Calling the coefficient damping pointwise requires care. On an existing
uncut gradient feature flow,
\(g'=\|\nabla g\|_{\rm metric}^2\ge0\), because (2) without cuts is
gradient ascent of \(g=(f_1-f_2)/2\); thus \(g(0)=0\) gives \(g\ge0\).
Then \(y_aB^{(3)}_{ka,ka}=-g_k\) and the term \(-g\kappa\) have the
advertised signs in the continuous law. Arbitrary finite Euler steps
and internally cut references are not automatically gradient ascent
of that same objective. Equations (13), (16)--(18) hold there without
assuming \(g_k\ge0\). Sample-label multiplication is not a conjugation
or a positive metric.

## 5. The full deterministic expected response does not close at its mean

Fix a top forward-source direction \(v\). Suppress superscript 3 in
this paragraph and put
\(x_i=\mathbb EP_i\), \(r_i=\mathbb ET_i=(D^{(3)}v)_i\).
Taking expectations in (11), *without* discarding correlations, yields

\[
\begin{aligned}
 x_i&=v_i+\sum_{j\prec i}A^{(3)}_{i,j}r_j,\\
 r_i&=-f_i x_i+\mathcal T_i(v)-\mathcal C_i(v),\\
 \mathcal T_i(v)&=\lambda\sum_{r<k,b}y_b
                  \mathbb E[\gamma^{(3)}_i\gamma^{(3)}_{rb}P^{(3)}_{rb}],\\
 \mathcal C_i(v)&=\operatorname{Cov}
                         (w_kh^{(3)}_i,P^{(3)}_i).
\end{aligned}                                                       \tag{19}
\]

Here covariance means \(\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)]\).
Equation (19) is the full finite retarded equation for the expected top
source response. In particular
\(\mathbb E[w_k\phi''(Z_i)P_i]\ne-f_i\mathbb EP_i\) in general.
Even \(\mathcal T_i\) keeps the sensitivity correlated with both gates.
It is not \(\lambda\sum y_b\mathbb E[\gamma_i\gamma_{rb}]
\mathbb EP_{rb}\).

In matrix notation the precise finite equation is

\[
 (I+F A^{(3)})D^{(3)}=-F+\mathcal T-\mathcal C,
 \qquad F=\operatorname{diag}(f_i),
 \tag{20}
\]

where \(\mathcal T,\mathcal C\) have the values (19) on each source
column. Both are linear in the deterministic direction \(v\). The
matrix \(A^{(3)}\) is strictly past-time; it includes its learned term
and the entire middle reverse-source response. Its label-weighted sign
is not supplied by (13).

For any nonnegative deterministic time/sample weights \(\omega_i\),
the exact signed mean-response balance is

\[
 \sum_i\omega_i y_a x_i r_i
  =-\sum_i\omega_i g_k x_i^2
       +\sum_i\omega_i y_a x_i
                             [\mathcal T_i(v)-\mathcal C_i(v)].
 \tag{21}
\]

For example one may take \(\omega_{ka}=\Delta\). This is a balance
for the actual deterministic expected responses. It is not obtained
from a trace or a surrogate Jacobian. The mean forward response map
\(v\mapsto x\) is lower triangular with identity diagonal, so it is
invertible on every finite prefix. Thus (21) can be tested against any
specified mean sensitivity \(x\), using its corresponding source
direction. For a current impulse at its injection time,
\(\mathcal T=\mathcal C=0\) in that row. At later times these terms need
not vanish and cannot in general be discarded. The covariance is still
zero at the first update; Section 6 shows that it can become nonzero at
the second update.

The middle analogue is also explicit. Let
\(X_i=h^{(2)}_i\tau_2(q^{(2)}_i)+f_i\kappa_i\),
\(x^{(2)}_i=\mathbb EP^{(2)}_i\). Taking expectations in (14) gives

\[
\begin{aligned}
 \mathbb ET^{(2)}_i={}&-\mathbb EX_i\,x^{(2)}_i
                       -\operatorname{Cov}(X_i,P^{(2)}_i)\\
 &+\mathbb E\left[\gamma^{(2)}_i\tau'_2(q^{(2)}_i)
       \left(v^{\zeta^2}_i+
           \sum_{j\prec i}B^{(3)}_{i,j}\gamma^{(2)}_jP^{(2)}_j\right)\right],\\
 x^{(2)}_i={}&v^{\xi^2}_i+
                              \sum_{j\prec i}A^{(2)}_{i,j}\mathbb ET^{(2)}_j.
\end{aligned}                                                       \tag{22}
\]

An auxiliary quadratic identity makes the middle sign problem especially
visible, without replacing the deterministic response by this stronger
random-sensitivity object:

\[
\begin{aligned}
 y_a\mathbb E[P^{(2)}_iT^{(2)}_i]
  ={}&-g_k\mathbb E[\kappa_i(P^{(2)}_i)^2]
       -y_a\mathbb E[h^{(2)}_i\tau_2(q^{(2)}_i)(P^{(2)}_i)^2]\\
 &+y_a\mathbb E\left[\gamma^{(2)}_i\tau'_2(q^{(2)}_i)P^{(2)}_i
       \left(v^{\zeta^2}_i+
        \sum_{j\prec i}B^{(3)}_{i,j}\gamma^{(2)}_jP^{(2)}_j\right)\right].
\end{aligned}                                                       \tag{23}
\]

Only the first term has the proposed sign when \(g_k\ge0\). The
second retains the actual query and its correlated squared sensitivity.
The third contains the entire historical response of the trained third
matrix. Equations (9), (12), and (22) retain the feedback through the
trained second matrix as well.

There is a useful exact description of what is first missing from a
mean-only closure. From the first line of (11),

\[
 \mathcal C_i(v)=\sum_{j\prec i}A^{(3)}_{i,j}
  \left\{\operatorname{Cov}(w_kh^{(3)}_i,\gamma^{(3)}_j u_{r})
       -\operatorname{Cov}(w_kh^{(3)}_i,
                          w_rh^{(3)}_jP^{(3)}_j)\right\},
 \quad j=(r,b).
 \tag{24}
\]

The second covariance is a two-time curvature product weighted by the
actual past sensitivity. The identity \(\mathbb Ew=0\) does not impose
a sign or cancellation on it. Section 6 tests this exact term in the
finite law, rather than substituting an arbitrary ambient random vector.

## 6. Canonical second-update test of the missing covariance

Fix \(\rho<1\) and any finite caps \(R_1,R_2\ge1\). Use the actual
three-level causal program (4)--(6), with indices 0,1,2. The small-\(\Delta\)
calculation here keeps the number of updates fixed. It is an algebraic
test of a response coefficient, not a simulation, a claimed positive-time
continuum asymptotic, or a new initialization eligibility result.

Write \(U_a=Z^{(3)}_{0a}\), and
\(D=h(U_1)-h(U_2)=H^{(3)}_{01}-H^{(3)}_{02}\). Because all actual
initial deltas and queries vanish, the first hidden update is zero.
Consequently \(Z^{(\ell)}_{1a}=Z^{(\ell)}_{0a}\) almost surely in
the law, and

\[
 w_1=\lambda D,\qquad w_2=2\lambda D.
 \tag{25}
\]

These are **value identities only**. In particular, do not differentiate
the reduced second expression in (25) with respect to \(\xi^{(3)}_{1a}\).
That source slot and \(\xi^{(3)}_{0a}\) are still distinct.

Choose the single source direction \(v=\partial_{\xi^{(3)}_{1a}}\),
and set \(A_a=A^{(3)}_{2a,1a}\). Strict causality and (11) give exactly

\[
 P^{(3)}_{2a}=-A_a w_1h(U_a),\qquad
 u_2=\lambda y_a\gamma(U_a),
 \tag{26}
\]

and therefore

\[
\begin{aligned}
 D^{(3)}_{2a,1a}
   &=\lambda y_a\mathbb E[\gamma(Z^{(3)}_{2a})\gamma(U_a)]
       +A_a\mathbb E[w_2h(Z^{(3)}_{2a})w_1h(U_a)],\\
 -\mathcal C_{2a}(v)
   &=A_a\operatorname{Cov}
                         (w_2h(Z^{(3)}_{2a}),w_1h(U_a))\\
   &=2\lambda^2 A_a
                  \operatorname{Cov}(D h(Z^{(3)}_{2a}),D h(U_a)).
\end{aligned}                                                       \tag{27}
\]

This is already a concrete residual, at a later causal source row, with
the full current trained law in its expectations.

To verify its nonzero sign, the leading coefficient of \(A_a\) can be
calculated without ignoring either trained matrix. Define only for this
calculation the initialized moments

\[
 F_\ell=\mathbb E(H^{(\ell)}_{0a})^2,\qquad
 J_\ell=\mathbb E(\gamma^{(\ell)}_{0a})^2,\quad \ell=1,2.
 \tag{28}
\]

They do not depend on the sample. Direct current-reverse differentiation
of (9)--(10), followed by (6), gives the exact two-step formulas

\[
\begin{aligned}
 A^{(2)}_{2a,1a}
  &=\lambda y_a\left\{
       \mathbb E[H^{(1)}_{2a}H^{(1)}_{1a}]
       +\mathbb E[\gamma^{(1)}_{2a}\gamma^{(1)}_{1a}
                                      \tau'_1(q^{(1)}_{1a})]\right\},\\
 A_a
  &=\lambda y_a\mathbb E[H^{(2)}_{2a}H^{(2)}_{1a}]
      +A^{(2)}_{2a,1a}\mathbb E[
           \gamma^{(2)}_{2a}\gamma^{(2)}_{1a}\tau'_2(q^{(2)}_{1a})].
\end{aligned}                                                       \tag{29}
\]

In the first line \(C_{aa}=1\). The first term of each line is that
matrix's learned forward action; the other terms are the responses of
its trained input. The bottom update also contributes. Thus (29) is not
a frozen-lower-layer coefficient.

As \(\Delta\downarrow0\) in this fixed finite program,
\(q^{(j)}_{1a}\to0\), \(Z^{(\ell)}_{2a}\to Z^{(\ell)}_{0a}\) in
probability and in every needed bounded-function moment. Here is an
elementary justification adequate even for the singular historical
covariances. At time 1 the top delta is bounded by a constant times
\(\lambda\), its expected derivatives are \(O(\lambda)\), and hence
the middle query is a centered Gaussian of standard deviation
\(O(\lambda)\) plus a bounded \(O(\lambda)\) shift. Equations (10)
and (6) then give the same conclusion for the bottom query. The bottom
second-step displacement is \(O_{L^2}(\lambda^2)\); (29) and its
off-diagonal versions give \(A^{(2)},A^{(3)}=O(\lambda)\) at this fixed
prefix. For example the forward-source difference variance is exactly
\(\mathbb E(\xi^{(2)}_{2a}-\xi^{(2)}_{0a})^2
=\mathbb E(H^{(1)}_{2a}-H^{(1)}_{0a})^2\), which tends to zero.
Use the same identity for the third layer and the past-delta corrections
in (4). This proves the asserted convergence with the given joint source
covariances, without inverting any historical Gram. All gates and
features are bounded; the cuts equal the identity near zero and their
derivatives lie in \([0,1]\), so bounded convergence in probability
justifies the expectations in (29).

It follows that

\[
 \frac{A_a}{\lambda}\longrightarrow y_a L_0,
 \qquad L_0=F_2+(F_1+J_1)J_2>0.
 \tag{30}
\]

Strict positivity follows already from \(F_2\ge m^2\); all other
terms are nonnegative. Thus (27) proves

\[
 \lim_{\Delta\downarrow0}
 \frac{y_a[-\mathcal C_{2a}(\partial_{\xi^{(3)}_{1a}})]}{\lambda^3}
       =2L_0\operatorname{Var}(D h(U_a))>0.
 \tag{31}
\]

To check the strict inequality for every allowed \(\rho\), only a small
nondegeneracy fact is needed. The first feature pair has equal second
moments, positive sum, and nonzero difference with positive probability.
For \(-1<\rho<1\) this follows from the positive Gaussian density and
the nonconstant activation; at \(\rho=-1\) its difference is
\(2\varepsilon\sin G\), which is not zero almost surely. The pair Gram
is therefore positive definite (its two eigenvalues are the sum/difference
squared moments divided by two). The initialized second preactivation
pair is a nonsingular Gaussian, and the same argument makes its feature
Gram positive definite. Hence \(U\) has positive density on all of
\(\mathbb R^2\). For \(a=1\), the function \(Dh(U_1)\) is zero at
\((\pi/4,\pi/4)\) and equals \(b^2\) at \((\pi/4,-\pi/4)\).
It is continuous and nonconstant, so its variance is positive. Swapping
coordinates handles \(a=2\). This argument is used only to certify (31).

For each fixed cap pair, (31) gives strict positivity for all sufficiently
small positive meshes. The limit coefficient is independent of the caps.
It also supplies a test of the weighted balance (21), rather than only
a sign of one matrix entry. At such a mesh choose the deterministic
formal source direction

\[
 \widetilde v=e_{1a}+(1+A_a f_{1a})e_{2a},
 \qquad e_{ra}=\hbox{unit vector in the slot }\xi^{(3)}_{ra}.
 \tag{31a}
\]

The current addition contributes a deterministic constant to
\(P^{(3)}_{2a}\), and nothing to its covariance with
\(w_2h(Z^{(3)}_{2a})\). Since
\(\mathbb E[w_1h(U_a)]=f_{1a}\), (26) gives
\(x_{2a}(\widetilde v)=1\) and
\(\mathcal C_{2a}(\widetilde v)=\mathcal C_{2a}(e_{1a})\).
Taking the sole nonzero weight in (21) to be \(\omega_{2a}=1\), the
covariance residual in that balance is consequently
\(y_a x_{2a}[-\mathcal C_{2a}(\widetilde v)]>0\).
This is an admissible test of the stipulated formal source coefficients;
it is not asserted to be a physical parameter perturbation or a direction
in the support of a possibly singular source covariance. It specifically
excludes discarding this term as nonpositive for every source direction
and nonnegative weight. It does not show positivity of the total balance.

No uniform-in-width or fixed-positive-physical-time counterexample is
claimed. The learned reverse addition to \(B^{(3)}\) is still the term
in (6); (27)--(31) concern its expected-derivative component, exactly the
component in which the proposed curvature replacement was made. They
do not assume that an additional learned term cannot participate in a
larger cancellation.

In particular, the following closure is false even in the canonical
finite Gaussian program:

\[
 \mathbb E[w_k\phi''(Z^{(3)}_{ka})
             \partial_{\xi^{(3)}_{rb}}Z^{(3)}_{ka}]
       =-f_{ka}\mathbb E[
             \partial_{\xi^{(3)}_{rb}}Z^{(3)}_{ka}]
                      \quad\hbox{for every }r<k.
 \tag{32}
\]

The failure is an actual retarded mixed moment. It is not inferred from
the old saddle, a trace/determinant, an arbitrary-control trajectory,
or a generic covariance-versus-tail counterexample. Its positive
label-weighted sign prevents simply discarding it as dissipative.
It does not prove that it dominates other terms in a full energy, nor
that the response is unbounded.

## 7. What the existing short interval does and does not supply

The complete proof in `TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` was checked
for its use of gate signs. Its sensitivity estimates use
\(|\phi'|\le e=1/10\), \(|\phi''|\le c=1/5\), \(|\phi|\le a\),
\(|\tau(q)|\le|q|\), and \(|\tau'|\le1\). The induction and Gaussian
moment estimates use no lower bound or positive sign for \(\phi'\).
The sole strict-gate statement in its derivative base case must become
an equality without a sign assertion:

\[
 \partial_{\zeta^{(2)}_{0a}}\delta^{(2)}_{0a}
                  =\gamma(\xi^{(2)}_{0a}),
 \tag{33}
\]

which may be negative or zero. The forward-source derivatives there
are still zero, since \(\tau_2(0)=0\); one must not delete the
zero-variance reverse source. This establishes the same base case.

For clarity, the estimates to which this sign audit applies are its
bottom single-source injection \(\Delta e^2/2\), its middle injection
\((3/2)\Delta e^2/2\), the Gronwall factors involving
\(c\max|q|+e^2\sum|B|\), and the full top derivative
\(\gamma D w+w\phi''D Z\). Every factor was replaced by its absolute
bound before the published numeric constants were used. The current
middle return uses absolute values as well. Thus the identical induction
proves, for this finite scalar law on \(S\le3/2\),

\[
 \begin{aligned}
 \max_a\sum_{r\le k,b}|B^{(3)}_{ka,rb}|&\le3067/3200,\\
 \max_a\sum_{r\le k,b}|B^{(2)}_{ka,rb}|&\le
                                  71063018523/73728000000<0.97,\\
 |A^{(\ell)}_{ka,rb}|&<(3/2)\Delta/2\quad(r<k),\\
 \mathbb E\exp((q^{(j)}_{ka})^2/16)&<2\quad(j=1,2).
 \end{aligned}                                                     \tag{34}
\]

The algebra (9)--(11) also supplies a direct check on that substitution.
These bounds are the **transferred old short absolute estimate**, not a
new signed estimate or a longer interval. In particular a weighted norm
on that same prefix bounded trivially by (34) is not additional progress.
The sharper current estimate (16) and identity (17) are new information
specific to (1), but they do not bound the historical parts of (34) on
arbitrary \([0,S]\).

Beyond the proven interval, existence of a finite-primal path by itself
does not provide uniform bounds for \(S^{(1)},S^{(2)}\), hence not for
\(A^{(2)},A^{(3)}\). Each fixed finite capped program has finite
derivatives. This finiteness must not be substituted for an estimate
uniform in its number of time slots and caps. Equations (19)--(24)
state precisely the extra terms a signed argument would have to handle.

## 8. Positive-gate and nonfreezing arguments requiring replacement

The activation values remain strictly positive. The gates do not:
\(\gamma(z)=b\cos(z+\pi/4)\) changes sign and vanishes at
\(z=\pi/4+\pi\mathbb Z\). The following distinctions are required
where the older arguments were used.

1. **Raw coordinates and sensitivity bounds.** Equations (9)--(11),
   bounded-product comparisons, the chain rule, and the absolute local
   bootstrap survive. A global coordinate \(F'=1/\phi'\), an increasing
   inverse chart, and cancellations using it do not: \(1/\gamma\) has
   poles. No such chart is used here. Positive-gate Killing or
   fixed-sign-control results in the registry have hypotheses that fail
   for (1), and are not inherited.

2. **Ordered-feature separation.** The implication used in the old
   nontriviality supplement, \(Z_1\ge1,Z_2\le-1\Rightarrow H_1-H_2\)
   bounded below by a fixed positive constant, fails for a periodic
   activation. Its tail-rectangle construction needs new events confined
   to appropriate phase intervals and control of the attained shifts.
   A positive feature floor still controls a same-label sum, but gives
   no opposite-label contrast lower bound.

3. **Readout and top backward signs.** Opposite labels already remove
   the pointwise bound \(y w(s)\ge ms\). With (1), \(w\gamma(Z_a)\)
   also has no gate-based sign even if \(w\) were prescribed positive.
   The old top gate-ratio argument uses the arctan gate's positive tail
   profile; its specific rectangles and ratios do not transfer to an
   oscillatory gate. Equation (13) is a mean identity and does not repair
   these pointwise statements.

4. **Propagation of backward Gram nondegeneracy.** Gaussian query
   quadrants plus a bounded response shift no longer imply the same
   delta quadrants: multiplication by \(\gamma(Z_a)\) may reverse signs
   or vanish, correlated with the query. One needs joint gate/query
   events or a conditional nondegeneracy argument. Gate squares in
   kernel formulas remain nonnegative, and Gram matrices remain positive
   semidefinite; their strict positivity is a separate obligation.

5. **Preserving nonzero velocities under multiplication.** At Gaussian
   initialization, discrete gate zeros have probability zero. At a later
   reached law this cannot be inferred just from unbounded tails or an
   \(L^2\) bound. The usual implication
   \(V\ne0\Rightarrow\gamma(Z)V\ne0\) requires
   \(\mathbb P(V\ne0,\gamma(Z)\ne0)>0\); a sufficient replacement is
   \(\mathbb P(\gamma(Z)=0)=0\). This needs proof for the attained law.
   Some adjoint pairings can instead prove feature motion directly since
   deltas already contain the gate, but the requisite strict pairings
   must first be established. No all-layer nonfreezing claim is made here.

6. **Distributional nonlinearity at later times.** Bounded \(\phi\)
   and unbounded support of \(Z\) rule out a nonzero affine slope if
   \(\phi(Z)\) were affine almost surely. They do not rule out a constant
   feature for a periodic activation: an unbounded law can be supported
   on one periodic level set. The old strict-monotonicity final step
   therefore fails. A sufficient replacement would be positive attained
   mass on an interval with an absolutely continuous component, since
   this analytic nonconstant periodic function cannot equal an affine
   function on a set of positive Lebesgue measure. No such later-time
   support theorem is established here.

7. **Relative-gate inequalities.** Bounds of the form
   \(|\phi'(z)-\phi'(z')|\le C|\phi(z)-\phi(z')|\), used in some older
   activation/control arguments, fail globally here: take \(z=0\) and
   \(z'=\pi/2\). Both activations equal \(1+\varepsilon\), whereas
   the gates are \(\varepsilon\) and \(-\varepsilon\). Ordinary
   Lipschitz bounds in \(|z-z'|\) do survive.

These are failures of transfer hypotheses. They are not proofs of
freezing, loss of nonlinearity, or failure of the final theorem for (1).
The label symmetry (7), finite gradient Gram positivity, and the exact
harmonic identities do not require positive gates.

## 9. Precise next obstruction and claim ledger

The first new obstruction is the mixed *retarded* statistic

\[
 \mathcal K_{i,j}(v)=\operatorname{Cov}
            (w_kh^{(3)}_i,\ w_rh^{(3)}_jP^{(3)}_j(v)),
 \qquad j=(r,b)\prec i.
 \tag{35}
\]

It enters with the specified coefficient \(A^{(3)}_{i,j}\) in (24).
At the canonical second update it reduces to the explicit positive
covariance in (27)--(31); thus neither mean-zero readout nor exchange
symmetry cancels it. A next bounded theoretical step would have to
control its **contracted contribution in (21)** together with the
readout term \(\mathcal T\), or cancel it against a specified lower
response energy. Such a cancellation must also retain the concrete
middle term
\(\mathbb E[h^{(2)}\tau_2(q^{(2)})(P^{(2)})^2]\) in (23), and the
learned covariance terms in (6). This names the first missing mixed
observable and its exact location; it is not merely a request to
"assume the full response is bounded." No further route is pursued here.

One must distinguish the result from an impossibility theorem: (31)
rules out the mean-factorization closure (32) and treating the residual
as automatically dissipative. It does **not** rule out estimating that
residual by a coupled finite-interval energy, including an energy
depending on \(\rho\). The constants allowed by the original contract
are unchanged.

| Claim | Status and boundary |
|---|---|
| Full retarded equations (9)--(12), (19), (22), with both learned matrix actions | Exact in the stated finite causal Gaussian law |
| Current top response \(-f_{ka}\), current middle formula (15) | Proved; no merging of historical/current source slots |
| Current top norm \(\le s/200\) and signed sum (17)--(18) | Proved, mesh/cap-independent on any finite scalar-law prefix |
| Second-update curvature--sensitivity covariance has positive label-weighted leading coefficient | Proved by (26)--(31), for each \(\rho<1\), each fixed cap pair |
| Mean curvature can replace curvature inside every retarded derivative expectation | Falsified by that canonical finite-program coefficient |
| Old \([0,3/2]\) absolute-response/tail estimate for this activation | Transfers after the explicit sign audit; not new signed stability |
| Signed bound for the complete response on arbitrary existing finite feature intervals | Open; no such bound follows from dropping the explicit residuals |
| Global population construction, restart, full GF/GD/width convergence, every-time nonlinearity and all-layer nonfreezing | Not proved or upgraded by this sidecar |

The trace-to-norm route remains closed. No generic initial-state fact,
determinant identity, or first-chaos/action-only bound is promoted as a
replacement for controlling (35) in the trained causal recursion.
