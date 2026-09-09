# Canonical concentration no-go for the quadratic depth-two network

Status: repaired proof submitted for end-to-end adversarial audit, 22 August
2026.  This note replaces the proof mechanism in
`CANONICAL_CONCENTRATION_NO_GO.md`; the older note is retained as an audit
history.

Throughout,

\[
 \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
 \qquad L=L_n=\sqrt{\log n}.
\]

## 1. The theorem

Let \(A_i,u_j,W_{ij}\) be independent standard Gaussians and set

\[
 G(0)=W/\sqrt n,\qquad X=u^{\odot2},\qquad
 Z=GX,\qquad B=A\odot Z,\qquad R=G^{\mathsf T}B.
\]

In feature time \(s\), evolve

\[
 A'=Z^{\odot2},\qquad X'=8X\odot R,
 \qquad G'=\frac2nBX^{\mathsf T}.                         \tag{1.1}
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
 +16\langle X\odot R^{\odot2}\rangle_n.                  \tag{1.2}
\]

There is a deterministic \(\delta_0>0\) such that

\[
 \Pr\!\left\{
   \inf\{s:f_n(s)-f_n(0)\ge\delta_0\}
   \le \frac{0.0862+o(1)}{\sqrt{\log n}}
 \right\}\longrightarrow1.                               \tag{1.3}
\]

For a positive one-sample label \(y_\star>0\), physical MSE time is

\[
 \dot\theta=2\eta(y_\star-f_n)\theta'.                    \tag{1.4}
\]

After taking \(\delta_0<y_\star/4\), the physical \(\delta_0\)-hitting time
tends to zero in probability.  Therefore \(f_n\) cannot converge uniformly on any fixed
physical-time interval to a continuous readout.  In particular, no
autonomous operator/traffic/measure IDE can satisfy all requirements of
`FROZEN_CONJECTURE.md` for this canonical iid-Gaussian sequence.

## 2. Exact identities

The trained matrix has the exact Volterra form

\[
 G(t)=G(0)+\frac2n\int_0^tB(s)X(s)^{\mathsf T}\,ds,          \tag{2.1}
\]

and hence

\[
\begin{aligned}
 Z(t)&=G(0)X(t)
  +2\int_0^tB(s)\langle X(s),X(t)\rangle_n\,ds,\\
 R(t)&=G(0)^{\mathsf T}B(t)
  +2\int_0^tX(s)\langle B(s),B(t)\rangle_n\,ds.
\end{aligned}                                               \tag{2.2}
\]

For a tagged column \(j\), write

\[
 x=X_j,\quad g=G_{\cdot j},\quad z=Z-xg,
 \quad H_-=G_{\cdot,-j}D_{X_{-j}}G_{\cdot,-j}^{\mathsf T},
\]

\[
 h=g^{\mathsf T}D_Ag,\qquad
 \rho=g^{\mathsf T}D_Az,\qquad r=R_j=hx+\rho.               \tag{2.3}
\]

Direct differentiation gives

\[
 x'=8xr,                                                     \tag{2.4}
\]

\[
 \rho'=x\mathcal P+\mathcal E_0+x^2\mathcal E_2,            \tag{2.5}
\]

where

\[
\begin{aligned}
\mathcal P={}&2\langle A^2z^2\rangle_n
 +2\sum_i g_i^2z_i^2
 +2Q_-\sum_iA_i^2g_i^2
 +8g^{\mathsf T}D_AH_-D_Ag\ge0,\\
\mathcal E_0={}&\sum_i g_iz_i^3
 +2Q_-\sum_iA_i^2g_iz_i
 +8g^{\mathsf T}D_AH_-D_Az,\\
\mathcal E_2={}&\frac2n\sum_iA_i^2g_iz_i+\sum_i g_i^3z_i,
\qquad Q_-=\langle X_{-j}^2\rangle_n.
\end{aligned}                                               \tag{2.6}
\]

Moreover,

\[
 h'=\sum_i\left(g_iZ_i+\frac{2x}{n}A_i^2\right)^2
 -\frac{4x^2}{n^2}\sum_iA_i^4,
\]

so

\[
 h'\ge-\frac{4x^2}{n}\langle A^4\rangle_n.                 \tag{2.7}
\]

The tag-deleted equations used after the cap are also exact:

\[
\begin{aligned}
 g-g_0&=\frac2n\int xA(xg+z)\,ds,\\
 g_k-g_{k0}&=\frac2n\int X_kA(xg+z)\,ds,\\
 z-z_0&=\int(2Q_-I+8H_-)A(xg+z)\,ds,\\
 A-A_0&=\int(xg+z)^{\odot2}\,ds.
\end{aligned}                                               \tag{2.8}
\]

For a row \(i\), put \(a=A_i,z_i=Z_i,b_i=a z_i\), and

\[
 S_i=\sum_jG_{ij}^2X_j,\qquad
 R_j^{(-i)}=\sum_{k\ne i}G_{kj}B_k,
 \qquad N_i=\sum_jG_{ij}X_jR_j^{(-i)}.
\]

Then

\[
 a'=z_i^2,qquad
 z_i'=(2Q+8S_i)a z_i+8N_i,qquad Q=\langle X^2\rangle_n.     \tag{2.9}
\]

For every fixed initial column set \(D\),

\[
8\int_0^t\sum_{j\in D}G_{ij}X_jR_j^{(-i)}\,ds
=\left[\sum_{j\in D}G_{ij}X_j\right]_0^t
-\int_0^t(2q_D+8S_{iD})B_i\,ds,                             \tag{2.10}
\]

where \(q_D=n^{-1}\sum_{j\in D}X_j^2\) and
\(S_{iD}=\sum_{j\in D}G_{ij}^2X_j\).  Fixed initialization layers are used,
so no moving-boundary term is hidden in (2.10).

## 3. Certified outer separation

Put \(\tau=Ls\).  For a natural extreme column, set

\[
 x=L^2U,\qquad h=H/L,\qquad \rho=LP.
\]

The positive tagged system is

\[
 U_\tau=8U(HU+P),\qquad H_\tau=3,\qquad P_\tau=26U,          \tag{3.1}
\]

with cost

\[
 I_c(a,b)=a/2+b^2/6,qquad U(0)=a,\quad P(0)=b.              \tag{3.2}
\]

For a row, \(A_i=L\alpha,Z_i=L\zeta\) give

\[
 \alpha_\tau=\zeta^2,qquad \zeta_\tau=14\alpha\zeta,
 \qquad I_r=\alpha_0^2/2+\zeta_0^2/6.                       \tag{3.3}
\]

The exact fixed-point program `outer_pole_certificate.c` proves

\[
 0.0838<T_*:=\inf_{I_c\le1}T_c<0.0840                       \tag{3.4}
\]

and, for the rate-one seed

\[
 (a_*,b_*)=(335/192,7/8),
\]

the stronger bound \(T_c(a_*,b_*)<0.083964\).  By the exact homogeneity

\[
 T_c(\lambda^2a,\lambda b)=\lambda^{-1}T_c(a,b),\qquad
 I_c(\lambda^2a,\lambda b)=\lambda^2I_c(a,b),               \tag{3.5}
\]

the positive rate-\(19/20\) seed has pole before \(0.086153\).  It has an
open neighbourhood of the same property.  Analytically, the row invariant
\(\zeta^2-14\alpha^2\) gives

\[
 \inf_{I_r\le1}T_r>0.11.                                    \tag{3.6}
\]

Finally,

\[
 \inf\{I_c:T_c\le T\}=(T_*/T)^2.                            \tag{3.7}
\]

Set

\[
 T_+=0.0862,qquad T_0=0.08617,
\]

\[
 \kappa=1-(0.0838/0.0862)^2=0.0549092651\ldots,              \tag{3.8}
\]

\[
 \beta=\frac16-\kappa=0.1117574015\ldots,
\quad d=\frac{2\kappa+\beta}{2}=0.1107879659\ldots,
\quad \zeta=\beta-d>0.                                     \tag{3.9}
\]

Thus

\[
 2\kappa<d<\beta,qquad d<1/6.                              \tag{3.10}
\]

## 4. The causal transfer theorem

The purpose of this section is to state and prove the probability theorem
that transfers (3.1) to the canonical network.  It is important that local
blocks are stopped at a moving reciprocal level before absolute graph
estimates are taken.

### 4.1 Covariant tagged blocks

Let \(Y=U^{-1}\) and \(D=H+PY\).  On a positive tagged branch,

\[
 Y_\tau=-8D,qquad H_\tau=3,qquad P_\tau=26/Y.               \tag{4.1}
\]

For the cap \(Y=\epsilon_n=L^2n^{-1/3}\), use \(y=Y\) as the independent
variable:

\[
 T_y=-\frac1{8D},\qquad H_y=-\frac3{8D},
 \qquad P_y=-\frac{13}{4yD}.                                \tag{4.2}
\]

If \(\theta\) is any finite collection of local insertion parameters, write
\(C_\alpha=y\partial_\theta^\alpha P\),
\(D_\alpha=\partial_\theta^\alpha H+C_\alpha\), and
\(\sigma=\log(y_0/y)\).  Faà di Bruno gives

\[
\begin{aligned}
 \dot T_\alpha&=-\frac{y}{8D^2}D_\alpha+\frac y8\mathcal R_\alpha,\\
 \dot H_\alpha&=-\frac{3y}{8D^2}D_\alpha
                  +\frac{3y}{8}\mathcal R_\alpha,\\
 \dot C_\alpha&=-C_\alpha-\frac{13y}{4D^2}D_\alpha
                  +\frac{13y}{4}\mathcal R_\alpha,
\end{aligned}                                               \tag{4.3}
\]

where \(\mathcal R_\alpha\) contains only lower-order derivatives.  On a
transverse branch \(D\ge n^{-o(1)}\).  Induction in \(\alpha\) and
variation of constants show, for
every fixed order,

\[
 \partial_\theta^\alpha(T,H,P)
 =n^{o(1)}(1+\log(y_0/y))^{C_\alpha}.                        \tag{4.4}
\]

This is a moving-level statement.  Raw fixed-time derivatives such as
\(\partial_\theta^3Y\) can be of order \(Y^{-1}\); their endpoint-motion
terms cancel only in (4.3).

Every ordered local history is first changed from time to the fixed phase
simplex using \(d\tau=-dy/(8D)\).  Pure repeated tagged insertions are solved
inside this block.  The only genuine polynomial phase factors are recorded
explicitly:

\[
 X(T_{\epsilon_n})=n^{1/3},\qquad
 \int X\,d\tau=n^{o(1)},\qquad
 n^{-1}\int X^2\,d\tau=n^{-2/3+o(1)}.                       \tag{4.5}
\]

There is no canonical unnormalised \(X^2\) portal: coincident \(Z\)-legs
carry their Gaussian/empirical \(n^{-1}\), and \(G'\) has its displayed
\(n^{-1}\).  Equation (4.5) is therefore a complete ledger of local
polynomial losses.

### 4.2 Reduced graph lemma

Choose an \(X(0)\)-measurable parent layer containing every column type
whose positive majorant pole can be at most \(T_+\).  Delete this layer and
first evolve the regular bath.  Fixed initialization dyadic layers and the
Gaussian tail estimate

\[
 \mathbb E[X^m\mathbf1_{X>w}]
 \le C_mw^{m-1/2}e^{-w/2}                                  \tag{4.6}
\]

reduce the ordinary tail to a summable sequence.  Same-row and same-column
stars are retained in their exact scalar blocks.  The row gap (3.6) and the
regular column gap \(T_+-T_0\) bound those blocks on the required interval.

After these resummations, recursively project every root-free Euler-zero
Gaussian/empirical bubble onto its conditional expectation.  For example,
\(n^{-1}\sum_jX_j^2\) is replaced by \(3\) plus its centered remainder.
This is an algebraic conditional-expectation projection on the initial
independent Gaussian variables, not an assumption about the trajectory.

Every remaining nonlocal root is generated by one of

\[
 Z=GX,\qquad R=G^{\mathsf T}B,qquad
 G'=\frac2nBX^{\mathsf T},                                  \tag{4.7}
\]

because (A'=Z^2) and (X'=8XR) only branch or propagate an existing
difference.  Assign charges

\[
 -\tfrac12\quad\hbox{to an initial Gaussian leg},\qquad
 -1\quad\hbox{to a trained or normalized empirical edge},
\]

\[
 +\kappa\quad\hbox{to a free exposed label},\qquad
 +\tfrac13\quad\hbox{to an exposed endpoint (X)}.          \tag{4.8}
\]

The weakest single root has charge

\[
 -\frac12+\frac13+\kappa=-\beta.                            \tag{4.9}
\]

A trained root has charge at most
\(-1+2/3+\kappa=-(1/3-\kappa)\), and a two-ended exposed bridge
has charge at most \(-2\beta\).  A change to a new row or column necessarily
creates one of the charged incidences in (4.7); repeated visits to the same
label are already in its local block.  Wick pairing cannot increase the
power, because each pairing pays (n^{-1}) and its Kronecker constraints can
only reduce the number of free labels.  A centered root-free bubble gains a
strict surplus identification.

Consequently, before cross-clock losses, every connected replicated
component with \(r\) nonlocal roots has \(n\)-power at most

\[
 -r\beta+o(1).                                              \tag{4.10}
\]

For fixed replica order, local stars have exponential rather than factorial
growth after division by their ordered time simplexes.  The covariant blocks
(4.2)--(4.5) have \(n^{o(1)}\) fixed-order derivatives.  Hence the absolute
sum of all reduced histories of a fixed \(2p\)-th moment is \(C_pn^{o(1)}\).
Taking \(p\) fixed but sufficiently large controls any prescribed polynomial
family of projected observables.  No \(p\asymp\log n\) operator estimate is
used.

The one-leg row primitive is not hidden in (4.10).  In the \(n\)-normalised
row-deleted cavity, put

\[
 \bar F_i=\mathbf1_C\bar X\odot\bar R,
 \qquad V_i^{\rm cav}(t)=\int_0^t\bar F_i(s)\,ds.
\]

Then exactly

\[
\begin{aligned}
\int_0^tN_{i,C}
={}&G_{i\cdot}^0V_i^{\rm cav}
 +G_{i\cdot}^0\int_0^t(F_i-\bar F_i)\\
&+\int_0^t(G_{i\cdot}-G_{i\cdot}^0)F_i,                    \tag{4.11}
\end{aligned}
\]

where \(F_i=\mathbf1_CX\odot R^{(-i)}\).  The first term is conditionally
Gaussian because (V_i^{\rm cav}) is independent of the deleted row.  If
\(X\le R_L=L^\varepsilon\) on the core, action gives its Gaussian metric
length \(O(L^{(\varepsilon-1)/2})\); Borell plus the maximum over \(n\) rows
is \(O(L^{(1+\varepsilon)/2})=o(L)\).  The last term is bounded by (2.1),
Cauchy--Schwarz, and the same action.  The middle term is a closed two-leg
feedback and is covered by (4.10).  Fixed tail layers use (2.10).  Thus

\[
 \max_i\sup_{t\le T_+/L}\left|\int_0^tN_i\right|=o(L).      \tag{4.12}
\]

Equations (4.6)--(4.12), together with the row gap, give all fixed row and
regular-bath moments used below, including the one-row/one-column deleted
versions and (C^1) one-tag clock comparison.

### 4.3 Weighted clock coarea

Against the common deleted regular bath, insert one parent tag at a time and
let \(\Theta_j\) be its exact reciprocal cap clock.  Conditional on the bath,
its radial Gaussian marks are independent across \(j\).  Homogeneity and the
\(C^1\) comparison with (3.1) give a uniform transverse radial derivative.
The coarea formula and Gaussian moderate deviations therefore give the
conditional clock density \(q_{j,b}\):

\[
 \sup_{t\le T_+}q_{j,b}(t)
 +\int_{t\le T_+}q_{j,b}(t)\,dt
 \le L^C n^{-I_*},
 \qquad I_*=(0.0838/0.0862)^2.                              \tag{4.13}
\]

Candidate membership is the coordinatewise fixed-threshold event
\(\{\Theta_j\le T_+\}\); it is not an order-statistic or fixed-cardinality
selection.  Conditional independence and (4.13) imply the factorial
intensity estimate

\[
\mathbb E_b\sum_{j\ne k}
 \mathbf1_{\{\Theta_j,\Theta_k\le T_+\}}
 \mathbf1_{\{|\Theta_j-\Theta_k|\le\epsilon\}}
 \le L^C n^{2\kappa}\epsilon.                              \tag{4.14}
\]

Pair-leave-out restoration changes the weighted density by \(n^{o(1)}\) in
\(C^1\), by (4.2)--(4.12), so (4.14) is preserved.  With
\(\epsilon=n^{-d}\), (3.10), Markov, and the first-moment version of (4.13)
give, with probability tending to one,

\[
 |E|\le n^{\kappa+o(1)},\qquad
 \min_{j\ne k\in E}|\Theta_j-\Theta_k|\ge n^{-d}.           \tag{4.15}
\]

### 4.4 Reinserting the separated tags

Let \(e\) be the earliest cavity clock.  Up to its cap, every other tag \(f\)
is later by \(\Delta=n^{-d}\).  Two-sided transversality gives, along the
\(e\)-phase,

\[
 Y_f(T_e(y))\ge c(y+\Delta).                                \tag{4.16}
\]

A cross-clock component with \(r\ge3\) roots loses at most

\[
 \int\frac{y\,dy}{(y+\Delta)^r}
 =O(\Delta^{-(r-2)}),                                       \tag{4.17}
\]

while \(r=2\) is logarithmic and \(r=1\) has no gap loss.  Therefore

\[
 r\beta-d(r-2)=r(\beta-d)+2d>d.                             \tag{4.18}
\]

The one-ended external bridge has the stronger deficit

\[
 \alpha=\frac12-\kappa-d=0.3343\ldots>d,                    \tag{4.19}
\]

and a leader-scale portal must leave and return, so it pays
\(2\beta>d\).  The fixed-moment graph expansion and (4.18) thus make the
full/cavity reciprocal error \(o(n^{-d})\).  This first-exit estimate
preserves (4.16) and de-stops itself.  Consequently the first full cap is
unique, has time at most (T_0/L), and at that time

\[
 X_e=n^{1/3},\qquad
 \max_{f\ne e}X_f\le n^{d+o(1)},                            \tag{4.20}
\]

\[
 h_e\ge c/L,qquad
 \Psi_e:=\rho_e+h_eX_e/2\ge cX_e/L.                         \tag{4.21}
\]

The existence of this cap follows from the positive rate-\(19/20\) seed:
there are \(n^{1/20+o(1)}\) such seeds, and their cap clocks are below
\(T_0\).  Tags outside \(E\) have a fixed positive majorant margin to
\(T_+\), so none can cap first.

## 5. Releasing the unique first tag

Let \(s_0\) be the cap time, write \(j=e\), and release this column while all
probability estimates are taken on the master event of Section 4.  Stop at
fixed action, or at

\[
 x=C\sqrt{nL}.                                               \tag{5.1}
\]

At \(s_0\), the master event also gives, for one fixed \(p>6\),

\[
 \frac1n\sum_{k\ne j}|\sqrt n\,u_k|^p=n^{o(1)},\qquad
 \frac1n\sum_{k\ne j}
 \left|\frac{v_k}{1+X_k}\right|^p=n^{o(1)},                 \tag{5.2}
\]

where

\[
 u_k=g_k^{\mathsf T}D_Ag,qquad
 v_k=g_k^{\mathsf T}D_Az,qquad R_k=xu_k+v_k.                \tag{5.3}
\]

These are fixed-degree one-column-deleted Gaussian moments: the cross part
of \(v_k\) is conditionally Gaussian with variance
\(n^{-1}\|Az_{-k}\|_2^2=n^{o(1)}\), its self part is
\(X_kg_k^{\mathsf T}D_Ag_k\), and \(u_k\) has variance
\(n^{-1}\|Ag_k\|_2^2=n^{-1+o(1)}\).  Thus (5.2) follows from the same
fixed-\(p\) master event, without conditioning on the identity of the winner.

Bootstrap \(h\ge c/(2L)\) and \(\Psi\ge0\).  Then

\[
 x'\ge cx^2/L,
\]

so, up to (5.1),

\[
 D_0:=\int ds\le n^{-1/3+o(1)},\quad
 D_1:=\int x\,ds=n^{o(1)},\quad
 D_2:=\int x^2\,ds\le n^{1/2+o(1)}.                         \tag{5.4}
\]

Use unnormalised vector norms in the rest of this section.  From (2.8),
the fixed moments at \(s_0\), and \(d<1/6\),

\[
 \|\Delta z\|_2\le n^{d+1/6+o(1)}.                         \tag{5.5}
\]

The entrywise design bound gives, for every vector \(w\),

\[
 \|H_-w\|_\infty
 \le \|G\|_{\max}\Bigl(\sum_{k\ne j}X_k^2\Bigr)^{1/2}
       \|G^{\mathsf T}w\|_2
 \le n^{o(1)}\|w\|_2.                                     \tag{5.6}
\]

Consequently

\[
 \|\Delta z\|_\infty\le n^{1/6+o(1)}.                    \tag{5.7}
\]

Interpolation yields

\[
 \|\Delta z\|_4\le n^{d/2+1/6+o(1)}=o(n^{1/4}),
\quad
 \|\Delta z\|_8\le n^{d/4+1/6+o(1)}.                      \tag{5.8}
\]

Equations (2.8), (5.4), and (5.8) then give

\[
 \|\Delta A\|_4\le n^{d/2+o(1)}=o(n^{1/4}),
 \quad \|\Delta A\|_\infty=n^{o(1)},                      \tag{5.9}
\]

\[
 \|\Delta A\|_1\le n^{2/3+o(1)},qquad
 \|\Delta A\|_2\le n^{1/6+o(1)}.                         \tag{5.10}
\]

Thus \(\langle A^4\rangle_n=n^{o(1)}\).  The same equations give

\[
 \|\Delta g\|_2\le n^{-1/2+o(1)},qquad
 \max_{k\ne j}\|\Delta g_k\|_2\le n^{d-5/6+o(1)},
 \quad \|\Delta G\|_{\rm op}\le n^{-1/3+o(1)}.           \tag{5.11}
\]

From (5.2), (5.5), and (5.9)--(5.11),

\[
 |u_k|\le n^{-1/3+o(1)},qquad
 |v_k|\le n^{d+1/6+o(1)}.                                  \tag{5.12}
\]

Therefore

\[
 \left|\log\frac{X_k(s)}{X_k(s_0)}\right|
 \le 8D_1n^{-1/3+o(1)}+8D_0n^{d+1/6+o(1)}=o(1),             \tag{5.13}
\]

and every rival remains \(n^{d+o(1)}\).  This closes all bootstraps used in
(5.5)--(5.11).

The error terms in (2.6) now satisfy

\[
 |\mathcal E_0|\le n^{1/2+d+o(1)},qquad
 |\mathcal E_2|\le n^{-1/2+o(1)}.                           \tag{5.14}
\]

Indeed, the first two terms of \(\mathcal E_0\) are at most
\(n^{1/2+o(1)}\), while

\[
 |g^{\mathsf T}D_AH_-D_Az|
 \le\|Ag\|_2\|H_-\|_{\rm op}\|Az\|_2
 \le n^{1/2+d+o(1)}.
\]

The two terms of \(\mathcal E_2\) are bounded using
\(\|g\|_\infty=n^{-1/2+o(1)}\).

At a hypothetical first zero of \(\Psi\), \(r=hx/2\).
Equations (2.5)--(2.7)
give

\[
 \Psi'\ge2h^2x^2-
 \left(n^{1/2+d+o(1)}+x^2n^{-1/2+o(1)}
       +2x^3n^{-1+o(1)}\right)>0,                            \tag{5.15}
\]

because \(x\ge n^{1/3}\), \(d<1/6\), and
\(x\le C\sqrt{nL}\).  Also

\[
 \int(h')_-\,ds\le n^{-1/2+o(1)}=o(L^{-1}),                \tag{5.16}
\]

so \(h\ge c/(2L)\).  Hence \(\Psi\) cannot cross zero and

\[
 r\ge cx/L.                                                 \tag{5.17}
\]

The elapsed outer time is

\[
 L(s_1-s_0)=O(L^2n^{-1/3})=o(1),                            \tag{5.18}
\]

so the release remains below (T_+).

Finally,

\[
 (x^2)'=16x^2r,\qquad K_n\ge\frac{16}{n}xr^2,
\]

and therefore, along the actual trajectory,

\[
 \frac{df_n}{d(x^2)}=\frac{K_n}{(x^2)'}
 \ge\frac{r}{nx}\ge\frac c{nL}.                            \tag{5.19}
\]

Choosing \(C\) large and fixed in (5.1), integration of (5.19) gives

\[
 f_n(s_1)-f_n(s_0)\ge\delta_0.                              \tag{5.20}
\]

Together with the first-cap alternative, this proves (1.3).

## 6. Physical-time contradiction

At initialization, \(f_n(0)\to0\) in probability.  Before the
\(\delta_0\) hit, \(y_\star-f_n\ge y_\star/2\) with probability tending
to one.  Thus the
physical hitting time is at most

\[
 \int_0^{s_1}\frac{ds}{2\eta(y_\star-f_n(s))}
 \le\frac{s_1}{\eta y_\star}\xrightarrow{\mathbb P}0.      \tag{6.1}
\]

If the frozen contract held, \(f_n\) would converge uniformly in probability
on a fixed physical interval to a continuous \(f\) with \(f(0)=0\).  At the
random hitting times \(t_{1,n}\to0\), however,

\[
 f_n(t_{1,n})-f_n(0)\ge\delta_0.
\]

Uniform convergence and the modulus of continuity of \(f\) would give

\[
 \delta_0\le2\|f_n-f\|_\infty+\omega_f(t_{1,n})
 \xrightarrow{\mathbb P}0,
\]

a contradiction.  This proves the theorem.  \(\square\)

## 7. Reproducibility and logical dependencies

The numerical input is only (3.4) and the displayed seed bound.  It is
certified by outward-rounded integer arithmetic in
`outer_pole_certificate.c`; the adjacent SHA256 file fixes the audited
source.  The row bound (3.6) is analytic.

The probability proof uses no two-training-time state or proposed limiting
IDE.  Two-time quantities occur only inside finite-width Volterra estimates.
All moment orders are fixed before (n\to\infty).  Unbounded Gaussian marks
are handled by fixed initialization layers, exact local resummation, and
the row/column pole gaps.  Candidate selection is a coordinatewise fixed
clock threshold, for which the weighted coarea estimate (4.14) is proved
before full reinsertion.  The terminal release uses only the exact identities
(2.8), fixed moments from the master event, and (d<1/6).
