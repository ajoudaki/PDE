# Actual top feedback and rare-middle localization

This note uses the exact trained top block, not an external middle
backward forcing. It proves a top virtual-work identity and a quantitative
rare-column deletion estimate. Neither supplies global continuation.
The remaining issue is dependence of the actual bulk middle trajectory
on the deleted initial Gaussian columns.

All inner products and vector norms below use normalized Euclidean
measure, or the corresponding probability-space convention.
Hilbert--Schmidt norms of the rank-one operators agree with the
Frobenius parameter metric. Write
\[
 h=h^{(2)},\quad W=W^{(3)},\quad C=W^{(4)},\quad
 z=Wh,\quad g=\phi(z),\quad D=\operatorname{diag}\phi'(z),
 \quad d=DC,\quad q=W^*d.
\]
Here \(\phi=\arctan\), \(a=\pi/2\), and feature time satisfies
\[
 C'=g,\qquad W'=d\otimes h,\qquad
 z'=m_2d+Wh',\qquad m_2=\|h\|_2^2.                         \tag{1}
\]
The middle/lower system additionally gives
\[
 h'=D_2A_2D_2q,\qquad
 A_2=m_1I+W^{(2)}D_1^2(W^{(2)})^*.
\]
All identities below apply to the prescribed finite network. The limiting
zero-readout initialization is used in the bounds; small nonzero readout
only changes their constants.

## Exact top virtual work

For any absolutely continuous middle-space vector \(v(s)\), define
\[
 {\cal P}_v=\langle C,DWv\rangle=\langle q,v\rangle.
\]
Differentiating every trained factor gives exactly
\[
 \begin{split}
 {\cal P}_v'
 ={}&\langle q,v'\rangle
     +\|d\|_2^2\langle h,v\rangle\\
    &+\langle Dg,Wv\rangle
     +\langle C\phi''(z)z',Wv\rangle.                     \tag{2}
 \end{split}
\]
The second term comes from \(W'\), the third from \(C'\), and the last
from the gate derivative. No frozen-operator approximation is used.

For comparison, set
\[
 \psi(x)=\phi(x)-x\phi'(x),\qquad
 {\cal J}=\langle C,\psi(z)\rangle.
\]
Since \(\psi'(x)=-x\phi''(x)\), equation (2) with \(v=h\) yields
\[
 \langle q',h\rangle+{\cal J}'
       =\|g\|_2^2+m_2\|d\|_2^2.                          \tag{3}
\]
Here \(|\psi|\le a\), so \(|{\cal J}(s)|\le a^2s\) for \(C(0)=0\).
In particular actual zero-readout top feedback obeys the initial
constraint
\[
 \langle q'(0),h(0)\rangle
 =\langle z(0),\phi'(z(0))\phi(z(0))\rangle\ge0.           \tag{4}
\]
This constraint need not hold for an externally selected \(q\).
At later times (3) is a storage identity, not a pointwise sign for
\(\langle q',h\rangle\); \({\cal J}'\) has no established sign.

## Coupling the tail test to the top block

Use the excess truncation
\[
 q_R=T_R(q),\qquad
 \eta_R(q)=
 \begin{cases}
 1-R/|q|,&|q|>R,\\
 0,&|q|\le R,
 \end{cases}
 \qquad v_R=\eta_R(q)h.
\]
Thus \(q_R=\eta_Rq\). Put
\(\delta_R=D_2q_R\), \(\delta_{\le R}=D_2(q-q_R)\).
Substituting \(v_R\) into (2) gives the exact coupled identity
\[
 \begin{split}
 \langle\delta_R,A_2\delta^{(2)}\rangle
 ={}&{\cal P}_{v_R}'
    -\|d\|_2^2\langle h,\eta_Rh\rangle\\
   &-\langle Dg,W(\eta_Rh)\rangle\\
   &-\langle C\phi''(z)z',W(\eta_Rh)\rangle
    -\langle q\eta_R',h\rangle.                          \tag{5}
 \end{split}
\]
The left side is exactly the localized lower power from the earlier
audit. It decomposes as
\[
 \begin{split}
 \langle\delta_R,A_2\delta^{(2)}\rangle
 ={}&m_1\|\delta_R\|_2^2+\|v_{1,R}\|_2^2\\
 &+m_1\langle\delta_R,\delta_{\le R}\rangle
       +\langle v_{1,R},v_{1,\le R}\rangle,               \tag{6}\\
 v_{1,R}&=D_1(W^{(2)})^*\delta_R,\qquad
 v_{1,\le R}=D_1(W^{(2)})^*\delta_{\le R}.
 \end{split}
\]
Equation (5) is thus a genuine top/lower relation for the indefinite
last term of (6).

Nevertheless its right side only provides the existing small signed
power, not a lower bound on that last term. To verify this precisely,
assume \(\sup_{s\le S}\|q(s)\|_2\le M\). Then
\[
 \|\eta_Rh\|_2\le\frac{aM}{R},\qquad
 |{\cal P}_{v_R}|=|\langle q_R,h\rangle|
                       \le\frac{aM^2}{R}.
\]
The top primal bounds give uniform bounds on \(\|W\|_{\rm op}\),
\(\|C\|_\infty\), \(\|d\|_2\), and \(\|z'\|_2\).
Every displayed top pairing in (5) is therefore \(O(R^{-1})\), uniformly
on the finite feature interval. Finally, almost everywhere,
\[
 q\eta_R'=\frac{R}{|q|}
                 \mathbf1_{\{|q|>R\}}q',
 \qquad
 |\langle q\eta_R',h\rangle|
       \le\frac{aM}{R}\|q'\|_2.
\]
Thus integrating (5) reproduces the \(O(R^{-1})\) bound on the signed
quantity (6). It does not make
\(\langle v_{1,R},v_{1,\le R}\rangle\) nonnegative or small.
The curvature term in (5) also has no sign: its actual factors are
\(W(\eta_Rh)\) and \(z'\), not the same vector.

## A quantitative top-only rare-column deletion lemma

Fix a time-independent middle set \(E\) of normalized mass \(p\), with
coordinate projection \(P_E\). On \([0,S]\), drive a copied top block by
\[
 \bar h=(I-P_E)h,
\]
where \(h\) is the actual network's middle trajectory. Its equations are
\[
 \bar C'=\phi(\bar W\bar h),\qquad
 \bar W'=\bar d\otimes\bar h,\qquad
 \bar d=\phi'(\bar W\bar h)\bar C,
 \quad \bar W(0)=W(0),\quad\bar C(0)=C(0)=0.              \tag{7}
\]
This is an auxiliary driven top block, not a changed model for the target.
It retains the actual nonlinear top training equations.

Suppose \(\|W(0)\|_{\rm op}\le M_0\). Both copies satisfy
\[
 \|C(s)\|_\infty,\|\bar C(s)\|_\infty\le as,\qquad
 \|W(s)\|_{\rm op},\|\bar W(s)\|_{\rm op}
       \le L:=M_0+\frac{a^2S^2}{2}.
\]
Since \(\|h-\bar h\|_2\le a\sqrt p\), define
\[
 K=a(1+2a^2S),\quad F=(1+2a^2S)L+aS,\quad
 H=aSF e^{KS},\quad
 J=(1+2a^2S)H+2a^2SL.
\]
Then the exact top comparison gives
\[
 \sup_{s\le S}
   \big(\|C-\bar C\|_2+\|W-\bar W\|_{\rm HS}\big)
       \le H\sqrt p,\qquad
 \sup_{s\le S}\|d-\bar d\|_2\le J\sqrt p.                 \tag{8}
\]
For completeness, if \(X=\|C-\bar C\|_2+\|W-\bar W\|_{\rm HS}\), the
upper derivative bounds are
\[
 \begin{split}
 \|z-\bar z\|_2
 &\le a\|W-\bar W\|_{\rm HS}+L\|h-\bar h\|_2,\\
 \|d-\bar d\|_2
 &\le\|C-\bar C\|_2+2aS\|z-\bar z\|_2,\\
 D^+X&\le KX+F\|h-\bar h\|_2.
 \end{split}
\]
Integrating the final scalar inequality proves (8). These constants are
finite at every finite \(S\); no middle backward tail is used.

The copied columns indexed by \(E\) never learn:
\[
 \bar W(s)P_E=W(0)P_E.                                   \tag{9}
\]
Moreover the exact rank history of the actual matrix gives
\[
 q(s)=W(0)^*d(s)
       +\int_0^s h(u)\langle d(u),d(s)\rangle\,du,
\]
and the second term has coordinatewise absolute value at most
\(a^3s^3/2\). Consequently
\[
 P_Eq(s)=P_EW(0)^*\bar d(s)+e_E(s),\qquad
 \|e_E(s)\|_2
       \le\left(M_0J+\frac{a^3S^3}{2}\right)\sqrt p.
                                                               \tag{10}
\]
This conclusion holds pathwise for every fixed set \(E\), including a
set selected after seeing the trajectory, because the deterministic
comparison is uniform over the choice of set.

## Exact remaining dependence

The copied top state \(\bar d\) is a deterministic functional of
\[
 W(0)(I-P_E)\quad\hbox{and the supplied actual path}\quad
 (I-P_E)h^{(2)}.
                                                               \tag{11}
\]
The unused columns \(W(0)P_E\) do not occur explicitly in (7).
But they do occur implicitly in its supplied actual bulk path through
the trained lower feedback. Therefore \(\bar d\) is not known to be
independent of those Gaussian columns.

This dependence has an exact variational description. Perturb only the
initial columns \(W(0)P_E\), and use a dot for this variation, retaining
a prime for feature time. Put
\(\dot K=\dot{\bar W}(I-P_E)\) and
\(\dot{\bar h}=(I-P_E)\dot h^{(2)}\). The active copied-top variation is
\[
 \begin{split}
 \dot{\bar z}&=\dot K\,\bar h+\bar W\dot{\bar h},\\
 \dot{\bar C}'&=\bar D\,\dot{\bar z},\\
 \dot{\bar d}&=\bar D\,\dot{\bar C}
       +\operatorname{diag}(\bar C\phi''(\bar z))
                                \dot{\bar z},\\
 \dot K'&=\dot{\bar d}\otimes\bar h
                  +\bar d\otimes\dot{\bar h},
 \qquad \dot K(0)=0,\quad\dot{\bar C}(0)=0.                \tag{11a}
 \end{split}
\]
All displayed copied-top coefficients are bounded on the finite interval.
The sole forcing is \(\dot{\bar h}\), the response of the actual bulk
middle trajectory to the deleted Gaussian columns. Thus the top itself
does not introduce an unbounded sensitivity coefficient in this
comparison. Controlling the forced system (11a) requires precisely that
bulk response, which includes the lower shared-layer feedback; setting
it to zero would silently change the target dynamics.

If that independence were available for a deterministic single-neuron
set \(E=\{i\}\), then conditional on \(\bar d\),
\[
 [W(0)^*\bar d]_i
       \sim N\!\left(0,\|\bar d\|_2^2\right),\qquad
 \|\bar d\|_2\le aS.
                                                               \tag{12}
\]
Equation (10), with \(p=1/n\), would put the actual coordinate within a
width-independent bounded error of this Gaussian variable. This would
give a uniform Gaussian tail up to a bounded shift. Equation (12) is
conditional, not an assertion about the actual coupled network:
conditioning on the actual bulk trajectory does not create independence.
For a randomly selected set the Gaussian selection issue is additional.

Thus the top-only comparison cleanly identifies what remains. A true
leave-one-column-out full-network construction must replace the supplied
bulk path in (11) by a path independent of that column and control the
resulting change in the queried top state. The lower response responsible
for this change includes precisely the shared first-layer term in (6).
No estimate controlling it has been established here.

The new facts are (2)--(5), which impose actual top-work constraints, and
the all-finite-\(S\) top-only deletion estimate (8)--(10). They preserve
both matrix orientations and all training equations of the target
trajectory. They do not establish a Gaussian tail, gated uniform
integrability, uniqueness, or global population continuation.
