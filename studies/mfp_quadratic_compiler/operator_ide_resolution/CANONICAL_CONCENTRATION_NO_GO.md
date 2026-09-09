# Canonical concentration no-go for the quadratic depth-two network

Status: candidate proof under final audit, 21 August 2026.  The algebraic,
outer-pole, and terminal mechanisms are certified, but Lemma 4.1 and the
post-cap de-stopping step still require the repairs stated in Section 10.
This note supersedes the earlier `CANONICAL_NO_GO_PROOF.md` draft.

Throughout,

\[
 \langle v,w\rangle_n=\frac1n v^{\mathsf T}w,
 \qquad L=L_n=\sqrt{\log n}.
\]

## 1. The theorem

Let \(A_i,u_j,W_{ij}\) be independent standard Gaussians and put

\[
 G(0)=\frac{W}{\sqrt n},\qquad X=u^{\odot2},\qquad
 Z=GX,\qquad B=A\odot Z,\qquad R=G^{\mathsf T}B.
\]

In feature time \(s\), evolve

\[
 A'=Z^{\odot2},\qquad X'=8X\odot R,\qquad
 G'=\frac2nBX^{\mathsf T}.                                      \tag{1.1}
\]

Define

\[
 f_n=\langle A,Z^{\odot2}\rangle_n
\]

and

\[
 K_n=f_n'
 =\langle Z^{\odot4}\rangle_n
 +4\langle X^{\odot2}\rangle_n\langle B^{\odot2}\rangle_n
 +16\langle X\odot R^{\odot2}\rangle_n.                       \tag{1.2}
\]

There is a constant \(\delta_0>0\), independent of \(n\), for which

\[
 \Pr\!\left\{
  \inf\{s:f_n(s)-f_n(0)\ge\delta_0\}
       \le \frac{0.090+o(1)}{\sqrt{\log n}}
 \right\}\longrightarrow1.                                    \tag{1.3}
\]

For a positive one-sample label \(y_\star>0\), the physical MSE flow is

\[
 \dot\theta=2\eta(y_\star-f_n)\theta'.                          \tag{1.4}
\]

After decreasing \(\delta_0\) so that \(\delta_0<y_\star/4\), its
\(\delta_0\)-hitting time tends
to zero in probability.  Consequently the finite-width outputs cannot
converge uniformly on a compact physical-time interval to a continuous
readout.  Thus the requirements in `FROZEN_CONJECTURE.md` are mutually
incompatible for the canonical iid-Gaussian sequence.

The proof is a concentration-layer theorem, not a finite-moment or
finite-jet obstruction.

## 2. Exact identities

The integrated trained matrix is

\[
 G(t)=G(0)+\frac2n\int_0^t B(s)X(s)^{\mathsf T}\,ds.             \tag{2.1}
\]

It follows that

\[
\begin{aligned}
 Z(t)&=G(0)X(t)
 +2\int_0^tB(s)\langle X(s),X(t)\rangle_n\,ds,\\
 R(t)&=G(0)^{\mathsf T}B(t)
 +2\int_0^tX(s)\langle B(s),B(t)\rangle_n\,ds.                 \tag{2.2}
\end{aligned}
\]

These formulas are used only in the proof; they are not a proposed
two-training-time closure.

### 2.1 A tagged column

Fix \(j\), and write

\[
 x=X_j,\quad g=G_{\cdot j},\quad z=Z-xg,\quad
 H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^{\mathsf T},
\]

\[
 h=g^{\mathsf T}D_Ag,\qquad
 \rho=g^{\mathsf T}D_Az,\qquad r=R_j=hx+\rho.                  \tag{2.3}
\]

Direct differentiation gives

\[
 x'=8xr,                                                       \tag{2.4}
\]

\[
 h'=\sum_i g_i^2(z_i+xg_i)^2
 +\frac{4x}{n}\sum_iA_i^2g_i(z_i+xg_i),                       \tag{2.5}
\]

and

\[
 \rho'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2,              \tag{2.6}
\]

where

\[
\begin{aligned}
\mathcal P={}&2\langle A^2z^2\rangle_n
+2\sum_i g_i^2z_i^2
+2Q_-\sum_iA_i^2g_i^2
+8g^{\mathsf T}D_AH_-D_Ag,\\
\mathcal E_0={}&\sum_i g_iz_i^3
+2Q_-\sum_iA_i^2g_iz_i
+8g^{\mathsf T}D_AH_-D_Az,\\
\mathcal E_2={}&\frac2n\sum_iA_i^2g_iz_i+\sum_i g_i^3z_i,
\qquad Q_-=\langle X_{-j}^2\rangle_n .                         \tag{2.7}
\end{aligned}
\]

Every term in \(\mathcal P\) is nonnegative.  Also

\[
 h'=\sum_i\left(g_iZ_i+\frac{2x}{n}A_i^2\right)^2
 -\frac{4x^2}{n^2}\sum_iA_i^4,                                \tag{2.8}
\]

and therefore

\[
 h'\ge-\frac{4x^2}{n}\langle A^4\rangle_n.                    \tag{2.9}
\]

### 2.2 A tagged row

For row \(i\), put \(a=A_i\), \(z=Z_i\), \(b=az\), and let

\[
 S_i=\sum_jG_{ij}^2X_j,\qquad
 R_j^{(-i)}=R_j-G_{ij}B_i,\qquad
 N_i=\sum_jG_{ij}X_jR_j^{(-i)}.                                \tag{2.10}
\]

Then, exactly,

\[
 a'=z^2,\qquad z'=(2Q+8S_i)az+8N_i,\qquad Q=\langle X^2\rangle_n.
                                                                    \tag{2.11}
\]

The definition

\[
 R_j^{(-i)}=\sum_{k\ne i}G_{kj}B_k                              \tag{2.12}
\]

is used when differentiating.  Thus no artificial terms from separately
differentiating \(R_j-G_{ij}B_i\) are omitted.

For a fixed initial column set \(D\), differentiation of
\(\sum_{j\in D}G_{ij}X_j\) gives the endpoint identity

\[
 8\int_0^t\sum_{j\in D}G_{ij}X_jR_j^{(-i)}\,ds
 =\left[\sum_{j\in D}G_{ij}X_j\right]_0^t
 -\int_0^t(2q_D+8S_{iD})B_i\,ds,                               \tag{2.13}
\]

where

\[
 q_D=\frac1n\sum_{j\in D}X_j^2,\qquad
 S_{iD}=\sum_{j\in D}G_{ij}^2X_j.                              \tag{2.14}
\]

The sets \(D\) below are fixed by initialization; there are no moving-layer
boundary terms.

## 3. The two outer scalar systems

Put \(\tau=Ls\).

For a natural-scale column, set

\[
 x=L^2U,\qquad h=H/L,\qquad \rho=LP.                           \tag{3.1}
\]

The limiting positive tagged system is

\[
 U_\tau=8U(HU+P),\qquad H_\tau=3,\qquad P_\tau=26U.             \tag{3.2}
\]

Its initialization cost is

\[
 I_c(a,b)=\frac a2+\frac{b^2}{6},\qquad U(0)=a,\qquad P(0)=b. \tag{3.3}
\]

For the absolute majorant we use \(b=|P(0)|\).  The system has
nonnegative coefficients.  Its blow-up time is denoted \(T_c(a,b)\).

For a row, set \(A_i=L\alpha\), \(Z_i=L\zeta\).  The limiting absolute
system is

\[
 \alpha_\tau=\zeta^2,\qquad \zeta_\tau=14\alpha\zeta,          \tag{3.4}
\]

with cost

\[
 I_r(\alpha_0,\zeta_0)=\frac{\alpha_0^2}{2}
 +\frac{\zeta_0^2}{6}.                                        \tag{3.5}
\]

### 3.1 Certified pole separation

Let

\[
 T_*:=\inf_{I_c(a,b)\le1}T_c(a,b),\qquad a,b\ge0.              \tag{3.6}
\]

The exact fixed-point certificate `outer_pole_certificate.c` proves

\[
 0.0838<T_*<0.0840.                                            \tag{3.7}
\]

It also certifies that the positive rate-(9/10) seed

\[
 (a,b)=\left(\frac{847}{540},\frac56\right)                   \tag{3.8}
\]

has

\[
 T_c(a,b)<0.088572.                                            \tag{3.9}
\]

The program uses outward-rounded (2^{-48}) fixed-point arithmetic; its
SHA256 digest is recorded beside the source.

For rows, the invariant (zeta^2-14\alpha^2) gives an analytic proof
that

\[
 \inf_{I_r\le1}T_r>0.11.                                      \tag{3.10}
\]

A derivation is included in Section 9.

The column flow has the homogeneity

\[
 T_c(\lambda^2a,\lambda b)=\lambda^{-1}T_c(a,b),\qquad
 I_c(\lambda^2a,\lambda b)=\lambda^2I_c(a,b).                 \tag{3.11}
\]

Hence

\[
 \inf\{I_c:T_c\le T\}=\left(\frac{T_*}{T}\right)^2.         \tag{3.12}
\]

## 4. Simultaneous causal peeling

This is the probabilistic lemma that transfers the scalar systems to the
canonical network.

### Lemma 4.1 (reduced mixed-time graph bound)

Fix \(T_0=0.090\), \(T_+=0.0915\), and
\(R_L=L^\varepsilon\), where \(0<\varepsilon<1/64\).  Split row and
column marks into fixed initialization dyadic layers.  In each graph
expansion:

1. retain and solve every maximal same-row and same-column scalar
   self-response before expanding any nonlocal return;
2. retain one-leg row- or column-deleted Gaussian cavity primitives as
   sources;
3. expand only feedback terms having two deleted Gaussian legs or an
   explicit \(n^{-1}\) trained/empirical charge.

Suppose all regular absolute row blocks have pole after \(0.11\), all
regular absolute column blocks have pole after \(T_+\), and every exposed
column is stopped at \(X_j=n^{1/3}\).  If the exposed set has

\[
 |E|\le n^{\kappa+o(1)},\qquad \kappa<\frac16,                 \tag{4.1}
\]

then, before fixed kernel action and up to \(\tau=T_0\), the following hold
simultaneously with probability tending to one:

\[
 Q=3+o(1),\qquad S_i=1+o(1)                                   \tag{4.2}
\]

in the integrated form needed in (2.11), every fixed regular empirical
word used below has its Gaussian value plus \(o(1)\), and

\[
 \max_i\sup_{t\le T_0/L}
 \left|\int_0^tN_i(s)\,ds\right|=o(L).                        \tag{4.3}
\]

For every exposed column, until the first cap,

\[
\begin{aligned}
 H_j(\tau)&=3\tau+o(1),\\
 P_j(\tau)&=P_j(0)+26\int_0^\tau U_j(v)\,dv+o(1),\\
 U_j'&=8U_j(H_jU_j+P_j),                                      \tag{4.4}
\end{aligned}
\]

uniformly in reciprocal coordinates down to
\(U_j^{-1}=L^2n^{-1/3}\).

#### Proof of Lemma 4.1

We give the graph argument because ordinary operator-norm conditioning is
not valid for adaptive diagonal weights.

Write each initial design occurrence as

\[
 G^0_{rc}=n^{-1/2}\gamma_{rc}.                                \tag{4.5}
\]

After Wick pairing, form the bipartite quotient graph of row and column
indices.  If a connected rooted graph has \(V\) index vertices, \(q\)
Gaussian pairs, and \(h\) trained \(n^{-1}\) edges, then it has at most
\(V-1\) free sums and weight

\[
 n^{V-1-q-h}.                                                 \tag{4.6}
\]

The distinct Gaussian support edges together with the trained edges connect
the quotient, so \(q+h\ge V-1\).  Thus (4.6) has nonpositive power.  A
normalized closed trace has the same count because of its explicit
\(n^{-1}\).  A surplus identification or return cycle lowers the power by
at least one.  A trained occurrence

\[
 \frac2n\int B_r(s)X_c(s)\,ds                               \tag{4.7}
\]

adds one normalized edge, at most one free tag, and one ordered time, so it
cannot increase the power.

Euler-zero pairings need not be noncrossing.  Gaussian stars are therefore
resummed before counting reduced graphs.  For \(m\) identical return pairs,

\[
 \frac{(2m-1)!!}{m!}
 =2^{-m}\binom{2m}{m}\le2^m.                                \tag{4.8}
\]

The analogous chi-square cumulants obey

\[
 \frac{|\kappa_m(\chi^2_\nu)|}{m!}
 \le \nu\frac{2^{m-1}}m.                                    \tag{4.9}
\]

After every local star and scalar subtree is collapsed, chronological
attachment histories of size \(m\) number at most \(C^m m!\); the ordered
time simplex cancels \(m!\).  A graph of Euler deficit \(d\) is obtained
from a tree history by at most \(2d\) endpoint choices, and its weighted
count is bounded by

\[
 C^m\sum_{d\ge0}(Cm^4/n)^d.                                  \tag{4.10}
\]

Choose an internal truncation

\[
 M=L^{1+\varepsilon+\eta},\qquad
 0<\eta<1-\varepsilon.                                       \tag{4.11}
\]

Then \(M\log M=o(\log n)\), so (4.10) is uniform through \(M\).
The nonlinear remainder is geometric after local resummation.  Its bound
is \(CtR_Lq^M/(1-q)=o(1)\) for a fixed \(q<1\); no factorial tail is
asserted.

The positive coefficient radius used here is not inferred from a signed
real pole.  The base row system (3.4) and base column system (3.2), with
absolute initial scores, are nonnegative IVPs.  The deterministic pole
classification leaves a fixed interval from \(T_0\) to \(T_+\) for regular
columns and from \(T_0\) to \(0.11\) for rows.  Their solutions therefore
occupy a compact positive tube at \(T_0\).  If \(F^\#\) is the absolute
local vector field and \(P^\#\) the absolute nonlocal portal, then, up to
the first tube exit,

\[
 \|u^P-u^0\|_\infty
 \le e^{K_*T_0}\|P^\#\|_{L^1},\qquad
 K_*=\sup_{\rm tube}\|DF^\#\|.                               \tag{4.12}
\]

The graph sum below is \(o(1)\), so (4.12) is smaller than the fixed tube
margin.  Scaling all portals by a complex parameter of modulus \(1+\rho\)
still stays in the tube for a fixed \(\rho>0\).  Cauchy's estimate then
makes every multiportal local derivative at most \(m!C^m\), exactly the
factor required in the history count.  This is a first-exit small-gain
argument, not an assumption of the conclusion.

To make the probability statement simultaneous, close (2p) external
kernel legs into

\[
 \operatorname{tr}_n[(\mathcal K\mathcal K^*)^p].             \tag{4.13}
\]

The same quotient count applies cyclically.  Local self-responses are
resummed before (4.13).  Taking a sufficiently large fixed \(p\) controls
all polynomially many row, external-time, and layer events; alternatively
\(p=c\log n\) gives the same result after replica-wise local resummation.
A deterministic polynomial time mesh and the positive-tube derivative
bound fill its gaps.  All graph histories are summed before Markov's
inequality, so the event contains the supremum over the admissible kernels
and times; it is not a pointwise expectation selected afterward by the
trajectory.

The ordinary layer sets are fixed by initial marks.  Initial tails obey

\[
 \mathbb E[X^m\mathbf1_{X>w}]
 \le C_mw^{m-1/2}e^{-w/2}.                                  \tag{4.14}
\]

In a layer of density \(p_w\), centered cross-layer returns have norm
\(O(w\sqrt{p_w})\); same-layer diagonal returns have already been resummed.
Summing (4.14) from \(R_L\) upward is \(e^{-cR_L}\) times a polynomial.
The bounded core contributes one open factor \(R_L\) and one ordered time,
so its feedback size is

\[
 \gamma_L=O(T_0R_L/L)=O(L^{-1+\varepsilon})=o(1).              \tag{4.15}
\]

No high power of \(R_L\) is paid repeatedly, because all repeated local
marks are inside the resummed block.

The early set is frozen after conditioning on an \(X\)-only parent deletion
and on the one-dimensional Gaussian scores.  Conditional residual columns
remain independent Gaussian regressions.  The proof is uniform over the
identity of \(E\), using only its size and the cap.  Its three worst portal
scales are

\[
 n^{\kappa-1/6+o(1)},\qquad
 n^{\kappa-1/3+o(1)},\qquad
 n^{2\kappa-1/3+o(1)},                                  \tag{4.16}
\]

all \(o(1)\) for \(\kappa<1/6\).  Thus the selectors are fixed before the
residual Gaussian exposure; no union over data-dependent subsets is used.

It remains to explain the one-leg sources.  Delete row \(i\).  Conditional
on its deleted bath and its initial score,

\[
 G_{i\cdot}^0
 =\frac{Z_i(0)}{nQ(0)}X(0)+\widetilde g_i,\qquad
 \operatorname{Cov}(\widetilde g_i)
 =\frac1nI-\frac{X(0)X(0)^{\mathsf T}}{n^2Q(0)}.               \tag{4.17}
\]

On the core, with

\[
 V_i(t)=\int_0^t X\odot R^{(-i)}\,ds,
\]

the action bound gives

\[
 \|V_i(t)\|_n^2
 \le tR_L\int_0^t\langle XR^2\rangle_n\,ds
 =O(L^{-1+\varepsilon}).                                     \tag{4.18}
\]

The curve \(V_i(t)\) has total Gaussian-metric length bounded by the same
square root.  Gaussian chaining, followed by the maximum over (n) rows,
therefore gives

\[
 \max_i\sup_t|G_{i\cdot}^0V_i(t)|
 =O(L^{(1+\varepsilon)/2+o(1)})=o(L).                         \tag{4.19}
\]

The conditional mean in (4.17) obeys the same bound.  Tail layers use the
exact endpoint identity (2.13); their \(q_D,S_{iD}\) and endpoint Gaussian
projection are \(o(1),o(1)\), and \(o(L)\), respectively.

The only direct row-to-bath source is \(4u_jG_{ij}B_i\); returning to row
\(i\) through an untrained edge adds a second \(G_{ij}^0\) leg.  The trained
row part has the explicit \(n^{-1}\) in (4.7).  The scalar trace return is
exactly the extracted \(8S_iB_i\) in (2.11).  Changes in global empirical
coefficients carry their displayed normalized average.  Therefore every
remaining full-minus-deleted feedback is a closed two-leg graph or has an
explicit normalized charge, and (4.6)--(4.13) apply.  The analogous column
deletion retains the one-leg initial score, extracts (hx) and the
(3,26) returns, and leaves only closed or trained feedback.

For a column-deleted bath, the endpoint change of \(B\) is \(o(1)\) in
normalized \(L^2\), by the core/tail split, (1.2), and (2.1)--(2.2).
Conditional Gaussian chaining therefore makes its one-leg score change
\(o(L)\), uniformly over \(E\).  The closed part is covered by the same
graph event.

Equations (4.2)--(4.4) now follow by inserting the Gaussian limits

\[
 Q\to3,\quad \langle B^2\rangle_n\to3,\quad
 \langle Z^2\rangle_n\to3,\quad
 \langle A^2\rangle_n\to1,\quad
 \frac1n\operatorname{Tr}(D_A GD_XG^{\mathsf T}D_A)\to1       \tag{4.20}
\]

into (2.5)--(2.7).  In (2.7), the four contributions to
\(\mathcal P\) are \(6,6,6,8\), totaling \(26\).  The first-exit
inequality (4.12) improves every provisional portal and moment threshold,
so no exit occurs before \(T_0\).  This proves Lemma 4.1.  \(\square\)

## 5. The exposed early block and a forced cap

Choose a fixed \(X\)-only parent set containing every cost-one column type
whose absolute positive pole is at most \(T_+\).  Conditional on the parent
deletion, its Gaussian column scores are independent.  Expose every column
with

\[
 T_c\!\left(\frac{X_j(0)}{L^2},
             \frac{|\widehat R_j(0)|}{L}\right)\le T_+.       \tag{5.1}
\]

Fixed score buffers absorb the \(o(1)\) difference between the parent-cavity
and full scores.

By (3.7), (3.12), and Gaussian large deviations,

\[
 |E|\le n^{\kappa+o(1)},\qquad
 \kappa=1-\left(\frac{0.0838}{0.0915}\right)^2
 =0.161224\ldots<\frac16.                                   \tag{5.2}
\]

The positive open cell around (3.8) has cost \(0.9+o(1)\), so conditional
binomial concentration (or the two-column second moment) gives

\[
 \#\{\hbox{positive-score seeds near (3.8)}\}
 =n^{0.1+o(1)}                                             \tag{5.3}
\]

with probability tending to one.  These are columns, not sample labels;
the network has the single positive label \(y_\star\).

Assume, for contradiction, that no column reaches \(X=n^{1/3}\) by
\(\tau=0.089\) and that fixed action has not occurred.  Lemma 4.1 applies.
For a seed in (5.3), put \(Y=1/U\).  The limiting equation gives

\[
 Y'=-8(H+PY).                                                \tag{5.4}
\]

At its pole, \(H=3\tau\ge c>0\), so the zero of \(Y\) is transverse.
The certified pole is before \(0.088572\), whereas the stopped finite cap
has \(Y=L^2n^{-1/3}=o(1)\).  The uniform \(o(1)\) reciprocal error in
(4.4) therefore forces that seed to reach the cap before \(0.089\), a
contradiction.  Thus either fixed action has already occurred or the first
cap time \(s_0\) satisfies

\[
 Ls_0<0.089.                                                \tag{5.5}
\]

Every column outside \(E\) has an absolute majorant pole after \(T_+\), and
the graph bootstrap is valid through \(T_0\).  Hence the first cap is also
the global column maximum.  At the capped leader \(j_\star\), (4.4) and (5.4)
give

\[
 h_{j_*}(s_0)\ge\frac cL,\qquad
 \Psi_{j_*}(s_0):=\rho_{j_*}+\frac12h_{j_*}x_{j_*}
 \ge\frac{c x_{j_*}}L.                                     \tag{5.6}
\]

## 6. Deterministic transport from the cap

Stop if the output has already increased by \(\delta_0\).  Otherwise, on
the graph event through \(T_0\), uniformly during the additional interval
used below,

\[
 \langle A^4\rangle_n\le L^C,\qquad
 |\mathcal E_0|\le\sqrt nL^C,\qquad
 |\mathcal E_2|\le n^{-1/2}L^C.                              \tag{6.1}
\]

The last two estimates follow directly from (2.7), the regular empirical
words, \(\sum_i g_i^6\le n^{-2}L^C\), and Cauchy--Schwarz.  They include all
other exposed columns; the exponents in (4.16) keep their contributions
inside (6.1).

Let

\[
 \Psi=\rho+\frac12hx.
\]

At a hypothetical first zero of \(\Psi\), one has \(r=hx/2\).  From
(2.4), (2.6), and (2.9),

\[
\begin{aligned}
 \Psi'
 &=x\mathcal P+\mathcal E_0+x^2\mathcal E_2
   +\frac x2h'+4hxr\\
 &\ge \mathcal E_0+x^2\mathcal E_2
   -\frac{2x^3}{n}\langle A^4\rangle_n
   +2h^2x^2.                                               \tag{6.2}
\end{aligned}
\]

For

\[
 n^{1/3}\le x\le C_\delta\sqrt{nL},\qquad h\ge c/(2L),       \tag{6.3}
\]

the last term in (6.2) dominates all three adverse terms in (6.1), with a
fixed positive margin.  Therefore \(\Psi\) cannot cross zero and

\[
 r\ge\frac12hx\ge\frac{c x}{L}.                              \tag{6.4}
\]

Using (2.9), (2.4), and (6.4), the possible loss in \(h\) before the upper
level in (6.3) is at most

\[
 C\int_{n^{1/3}}^{C_\delta\sqrt{nL}}
 \frac{x^2}{n}L^C\frac{L\,dx}{x^2}
 =n^{-1/2}L^{C+3/2}=o(L^{-1}),                             \tag{6.5}
\]

where the fixed graph moment degree is chosen before the harmless displayed
polylogarithm.  The sharper regular-word estimate gives the stated
\(o(L^{-1})\); equivalently one can enlarge the lower level by a fixed
polylogarithmic factor.  Thus the bootstrap \(h\ge c/(2L)\) is preserved.

The elapsed feature time is

\[
 \Delta s\le C L n^{-1/3},\qquad
 L\Delta s=O(L^2n^{-1/3})=o(1),                            \tag{6.6}
\]

so the terminal segment remains inside the graph horizon \(T_0=0.090\).

Finally,

\[
 (x^2)'=16x^2r,\qquad K_n\ge\frac{16}{n}xr^2.                \tag{6.7}
\]

Along the actual full trajectory,

\[
 \frac{df_n}{d(x^2)}=\frac{K_n}{(x^2)'}
 \ge\frac{r}{nx}\ge\frac{c}{nL}.                           \tag{6.8}
\]

Choose \(C_\delta\) large and fixed.  Integrating (6.8) from
\(x=n^{1/3}\) to \(x=C_\delta\sqrt{nL}\) gives

\[
 f_n(s_1)-f_n(s_0)
 \ge c\frac{C_\delta^2nL-n^{2/3}}{nL}\ge\delta_0.          \tag{6.9}
\]

Equations (5.5), (6.6), and (6.9) prove (1.3).

## 7. Physical time and the frozen-contract contradiction

At initialization, \(f_n(0)\to0\) in probability.  Before the
\(\delta_0<y_\star/4\) hit, \(y_\star-f_n\ge y_\star/2\) with probability tending to
one.  Therefore

\[
 t_{1,n}
 =\int_0^{s_1}\frac{ds}{2\eta(y_\star-f_n(s))}
 \le\frac{s_1}{\eta y_\star}\xrightarrow{\mathbb P}0.       \tag{7.1}
\]

Suppose the frozen contract held.  Then, on every fixed physical interval,
\(f_n\) would converge uniformly in probability to a continuous readout
\(f\), and \(f(0)=0\).  But (6.9) supplies random times \(t_{1,n}\to0\)
with a fixed output increase.  More explicitly,

\[
 \delta_0
 \le2\|f_n-f\|_{\infty}
 +\omega_f(t_{1,n})+o(1)\xrightarrow{\mathbb P}0,             \tag{7.2}
\]

where \(\omega_f\) is the modulus of continuity of the readout.  This is a
contradiction.

Moreover,

\[
 \sup_{0\le s\le s_1}K_n(s)
 \ge\frac{\delta_0}{s_1}\xrightarrow{\mathbb P}\infty,       \tag{7.3}
\]

so a finite continuous tangent-kernel readout fails as well.

The theorem does not exclude a generalized description with a discontinuous
initial trace.  Such an object is outside the frozen requirements.

## 8. Why the exponent (1/6) is decisive

The pole threshold \(T_+=0.0915\), together with the certified lower bound
\(T_*>0.0838\), gives

\[
 \kappa
 =1-(0.0838/0.0915)^2
 =0.161224\ldots<1/6.                                      \tag{8.1}
\]

Before the first \(n^{1/3}\) cap, the three worst exposed-block feedback
scales are exactly those in (4.16).  The smallest exponent margin is

\[
 \frac16-\kappa=0.005442\ldots>0.                            \tag{8.2}
\]

It absorbs every fixed polylogarithmic loss in the causal graph estimate.
This is why a fixed \(0.0915\) exposure buffer is used instead of a
shrinking phase-ranking window.

## 9. Analytic row-pole bound

For (3.4), let \(x=\alpha_0\ge0\), \(z=|\zeta_0|>0\), and

\[
 C=z^2-14x^2.
\]

Then

\[
 T_r=\int_x^\infty\frac{dA}{14A^2+C}.                         \tag{9.1}
\]

Put \(r=\sqrt{14}\,x/z\).  On the rate-one ellipse,

\[
 z^2=\frac{84}{3r^2+14},\qquad
 T_r^2=\frac{(3r^2+14)F(r)^2}{1176},                         \tag{9.2}
\]

where

\[
 F(r)=\int_r^\infty\frac{dy}{y^2+1-r^2}.                    \tag{9.3}
\]

For \(0\le r\le1\), write \(r=\cos\theta\); then
\(F=\theta/\sin\theta\).  On \(r\in[1/3,1]\), \(F\ge1\), so

\[
 T_r^2\ge\frac{43}{3528}>0.11^2.                            \tag{9.4}
\]

For \(r\le1/3\), monotonicity of \(\theta/\sin\theta\) gives a stronger
bound.  For \(r\ge1\), write \(r=\cosh q\); then

\[
 1176T_r^2=3q^2+17(q/\sinh q)^2.                              \tag{9.5}
\]

The elementary inequality

\[
 \log(\sinh q/q)\le q^2/6                                  \tag{9.6}
\]

follows by differentiating and using
\(\coth q-1/q\le q/3\).  With \(y=q^2\), (9.5) is at least

\[
 3y+17e^{-y/3}\ge9+9\log(17/9)>189/13,                       \tag{9.7}
\]

and therefore \(T_r^2>9/728>0.11^2\).  Negative initial signs are no
faster than the absolute positive system.  This proves (3.10).

## 10. Audit status

The proof was tested through independent routes that attempted:

- endpoint-factorized propagation without graph estimates;
- direct mixed-time Wick/traffic expansion;
- hostile low-order and high-moment graph searches;
- selector/adaptive-stopping attacks;
- reciprocal hitting-time and terminal-leader attacks.

Endpoint factorization alone was rejected because adaptive operators such as
\(D_1G_0^{\mathsf T}D_2G_0D_3\) still require the mixed-time graph lemma.
The accepted proof uses endpoint factorization only for exact charge
bookkeeping and proves the simultaneous graph event before any adaptive
selector is applied.

### 10.1 Open audit obligations

The following three points must be discharged before the status can be
upgraded from candidate to theorem.

1. The proof must be recast as a projected-root estimate, not an operator
   norm claim.  Recursively absorb every root-free zero-deficit empirical
   bubble, then prove that each remaining connected replicated component
   with \(r\) portal roots has \(n\)-power at most
   \(-r\delta\), for some
   \(0<\delta<1/6-\kappa\).  A fixed
   \(p>D/(2\delta)\) then controls \(n^{D+o(1)}\) projected roots.  The
   canonical portal charge table establishing this componentwise bound is
   not yet written.
2. In (4.18), \(V_i\) must first be defined on the row-deleted cavity path.
   Gaussian chaining then applies conditionally; a separate closed-feedback
   estimate must compare the full and cavity primitives.
3. Lemma 4.1 stops every exposed column at \(n^{1/3}\).  Section 6 requires
   a one-released-leader de-stopping lemma that propagates the projected
   regular-bath bounds until action occurs or
   \(X_{j_\star}=C_\delta\sqrt{nL}\).

The numerical certificate, exact identities, pole separation, exponent
\(\kappa<1/6\), and the deterministic implication from these three repaired
inputs to the concentration layer have passed independent checks.
