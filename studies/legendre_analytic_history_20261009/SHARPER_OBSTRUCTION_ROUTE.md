# A sharper prediction obstruction from the interior history join

This bounded theoretical route continues the unchanged original method in
this study. Its inputs are `ORIGINAL_OUTPUT_ANALYSIS.md`,
`ORIGINAL_METHOD_RESULT.md`, `CLOCK_ANALYSIS.md`, and the current
`paper/compact.tex`, `paper/compact_legendre.tex`, and
`paper/compact_fitting.tex`. No experiments, other studies, or paper edits
were used. The derivation below is an author result, not an independent
promotion review.

The interior-join mechanism gives a candidate strengthening of the proved
onset obstruction from \(q^{-10}\) to \(q^{-5}\). The argument below supplies
the required uniform estimates and the transfer to actual predictions.
Its central device is to compare two nearby times with opposite Legendre
phases. This prevents the smooth accumulated readout response from
cancelling the oscillatory direct contribution at both times.

## Statement and scope

Use the admissible identity-activation example \(m=d=L=2\), normalized
inputs \(v_1=e_1,v_2=e_2\), and any fixed nonzero sufficiently small label
vector \(y\in\mathbb R^2\). Put \(Y=\|y\|_2/\sqrt2\). Both models use the
same Gaussian initialization, the residual-RMS clock starts at one, and
the original constant forward and zero backward prefixes are retained.

On the common initialization/fitting event, there are constants \(c>0\),
\(q_0<\infty\), and \(0<t_1<t_2<\infty\), independent of width and order,
such that

\[
 \sup_{t\in[t_1,t_2]}\max_{a=1,2}
 |f_{\rm Leg}(t,x_a)-f_n(t,x_a)|\ge c q^{-5}
 \qquad(q\ge q_0).                                      \tag{1}
\]

The constants may depend very strongly on the fixed positive label size.
The event tends to probability one and is common to all finite orders.
Thus the proposed lower bound is uniform when \(q=q(n)\) grows with width.
The earlier onset result covers the finitely many \(q<q_0\).

Consequently the displayed absolute target
\(CY/[\sqrt n(\log(en))^3]\), if attained, requires

\[
 q\ge c_{\rm problem} n^{1/10}(\log(en))^{3/5}.           \tag{2}
\]

For the comparison with actual independent dense variability, combining
(1) with the upper certificate already recorded in
`ORIGINAL_METHOD_RESULT.md` excludes every \(q=n^\alpha\) with fixed
\(\alpha<1/10\). That separate certificate is not re-audited here. A
bound of the form \(q\ge n^{1/10-o(1)}\) does not, by itself, exclude all
orders literally smaller than \(n^{1/10}\) by subpolynomial factors.

## Exact clock-domain integral equations

Use the normalized physical matrices and readout from the onset proof,

\[
 A=W^{(1)}/\sqrt n\in\mathbb R^{n\times2},\qquad
 B=W^{(2)}\in\mathbb R^{n\times n},\qquad c=w/\sqrt n.
\]

The prediction and residual vectors are \(f=A^\top B^\top c\) and
\(r=f-y\). In physical time the dense equations are

\[
 \dot A=-B^\top cr^\top,\qquad
 \dot B=-c(Ar)^\top,\qquad \dot c=-BAr.                  \tag{3}
\]

For each model use its own clock
\(\xi=1+\int_0^t\rho(s)\,ds\), with
\(\rho=\|r\|_2/\sqrt2\), and retain physical time \(t\) as an extra
coordinate. Choose a fixed short interval of clock values
\([1,T_2]\) on which both residuals satisfy \(\rho\ge Y/2\), for all
orders on the common event. This is possible from the order-independent
physical bounds and the exact initial values \(r(0)=-y,c(0)=0\).

With primes denoting clock derivatives only in this paragraph, the dense
clock vector field is

\[
 A'=-B^\top c(r/\rho)^\top,\quad
 B'=-c[A(r/\rho)]^\top,\quad
 c'=-BA(r/\rho),\quad t'=1/\rho.                         \tag{4}
\]

It is Lipschitz, with constants independent of \(n,q\), in the difference
norm \(\|\Delta A\|_F+\|\Delta B\|_F+\|\Delta c\|_2+|\Delta t|\)
on the bounded short-time tube. Bounds on \(B\) itself use its operator
norm; no width-dependent bound on \(\|B_0\|_F\) is invoked.

Define the sample-column histories

\[
 h(\xi)=A(\xi),\qquad b(\xi)=c(\xi)[r(\xi)/\rho(\xi)]^\top,
\]

with \(h=A_0,b=0\) on \([0,1]\). Write \(Q_q^T=I-\Pi_q^T\) for the
degree-below-\(q\) projection complement on \([0,T]\), and define

\[
 H_q[b,h](T)=\int_0^T(Q_q^T b)(\xi)(Q_q^T h)(\xi)^\top\,d\xi.
                                                               \tag{5}
\]

Orthogonality and the unchanged reconstruction formula give exactly

\[
 \widehat B(T)=B_0-\int_1^T\widehat b(\xi)\widehat A(\xi)^\top\,d\xi
                  +H_q[\widehat b,\widehat h](T).        \tag{6}
\]

The dense equation is the same without \(H_q\). This integrated identity
is essential: estimating the absolute integral of the instantaneous
endpoint-error product discards the cancellation used below.

## Uniform Legendre estimates for the fixed dense histories

The dense histories in their own clock have bounded derivatives of every
fixed finite order on \([1,T_2]\), uniformly in width on the event. To see
this without invoking an analytic source theorem, differentiate (4) a
fixed number of times. Products are bounded using the operator norms,
the two-column Frobenius norms, and \(\rho\ge Y/2\). All positive-order
derivatives of \(B\) are bounded in Frobenius norm. Derivatives of
\(\rho^{-1}\) are bounded because its argument stays away from zero.
This finite induction gives the derivatives needed below.

For \(T>1\), put

\[
 \alpha=2/T-1=\cos\theta,\quad s=\sin\theta,\qquad
 H_k(x)=(x-\alpha)_+^k/k!,\quad -1\le x\le1.
\]

The symbol \(H_k\) in this paragraph is a scalar truncated power, not the
matrix \(H_q[b,h]\) in (5). For \(j>k\), repeated integration by parts in
Rodrigues' formula gives

\[
 \int_\alpha^1(x-\alpha)^kP_j(x)\,dx
 =\frac{k!(1-\alpha^2)^{k+1}P_j^{(k+1)}(\alpha)}
 {\prod_{r=-k}^{k+1}(j+r)}.                              \tag{7}
\]

The signs in (7) are positive. For \(k=0\), it is the integral identity
\(\int_\alpha^1P_j=(1-\alpha^2)P_j'/[j(j+1)]\).

The Legendre bounds proved in `compact_legendre.tex`, combined with its
differential equation and differentiated versions, give for each fixed
\(r\ge1\)

\[
 |P_j^{(r)}(\cos\theta)|
 \le C_r j^{r-1/2}s^{-r-1/2}\quad(s\ge j^{-1}).           \tag{8}
\]

For detail, the paper's energy argument gives
\(|P_j|\le Cj^{-1/2}s^{-1/2}\) and
\(|P_j'|\le Cj^{1/2}s^{-3/2}\) in this region. Differentiate
\((1-x^2)P_j''-2xP_j'+j(j+1)P_j=0\) repeatedly. At each induction
step the lower-order term is absorbed using \(js\ge1\). For
\(s<j^{-1}\), use the endpoint bound
\(|P_j^{(r)}|\le C_r j^{2r}\), which follows from the nonnegative
derivative expansion in the same paper. Multiplication by \(s^{2r}\)
in (7) therefore yields, uniformly even as \(T\downarrow1\),

\[
 \left|\int_\alpha^1(x-\alpha)^kP_j(x)\,dx\right|
 \le C_kj^{-k-3/2},\qquad
 \|Q_qH_k\|_{L^2(-1,1)}\le C_kq^{-k-1/2}.               \tag{9}
\]

The second assertion follows by multiplying the integral by
\(\sqrt{(2j+1)/2}\), squaring, and summing over \(j\ge q\).

The exceptional pair \(H_1,H_2\) gains a further power over multiplying
the two estimates in (9). Since \(H_2'=H_1\), orthogonality gives exactly

\[
 \langle Q_qH_1,Q_qH_2\rangle
 =\frac12\{(Q_qH_2)(1)^2-(Q_qH_2)(-1)^2\}.             \tag{10}
\]

Indeed, write \(H_1=(Q_qH_2)'+(\Pi_qH_2)'\); the second derivative
term is still a polynomial of degree below \(q\), so its inner product
with \(Q_qH_2\) vanishes. The endpoint formulas from the projection
kernel express both errors in (10) as half a sum or difference of the
two \(k=1\) integrals with indices \(q,q-1\). Formula (9) then proves
\(|\langle Q_qH_1,Q_qH_2\rangle|\le Cq^{-5}\), uniformly up to
\(T=1\).

Subtract the dense histories' right Taylor jets through degree four at
\(\xi=1\), using truncated powers on the prefix interval. The
remainders are globally \(C^4\), with bounded piecewise higher
derivatives. In the coordinate \(x=2\xi/T-1\), apply the self-adjoint
Legendre operator \(\mathcal Lg=-[(1-x^2)g']'\) twice. Boundary terms
vanish because of \(1-x^2\), including at the join because the first
four derivatives match. Its spectral eigenvalues \(j(j+1)\) give

\[
 \|Q_qR\|_2\le[q(q+1)]^{-2}\|\mathcal L^2R\|_2
 \le Cq^{-4}.                                           \tag{11}
\]

There is no backward constant term and no forward term of degree one.
Thus (9)--(11), including the special pair (10), give

\[
 \|Q_q^Tb_D\|_2\le Cq^{-3/2},\quad
 \|Q_q^Th_D\|_2\le Cq^{-5/2},\quad
 \|H_q[b_D,h_D](T)\|_F\le Cq^{-5}                       \tag{12}
\]

uniformly for every \(1\le T\le T_2\). This explicitly includes the
shrinking boundary layer \(T-1\asymp q^{-2}\).

## The surviving oscillation at an interior clock value

On a compact subinterval \(1<T_1\le T\le T_2\), the same dense source
has the stronger uniform expansion

\[
 H_q[b_D,h_D](T)
 =q^{-5}\{C(T)\sin(2q\theta(T))+D(T)\}+O(q^{-11/2}),   \tag{13}
\]

where \(C,D\) and their first derivatives are bounded independently of
width. The coefficient needed for the prediction argument is

\[
 C(T)=\frac{T(T-1)^{3/2}}{4\pi}\,b_D'(1+)h_D''(1+)^\top.
                                                               \tag{14}
\]

Here derivatives in (14) are with respect to the clock. No derivative
estimate for the error term in (13) is needed.

Here is a derivation of (13), including its phase and normalizations.
For fixed interior \(\theta\), the elementary integral representation
of \(P_j\) in the paper gives

\[
 P_j(\cos\theta)=\sqrt{\frac2{\pi j\sin\theta}}
 \cos((j+1/2)\theta-\pi/4)+O(j^{-3/2}).                  \tag{15}
\]

One can obtain the uniform version directly by splitting that integral
near its two endpoints. Away from the endpoints its complex integrand
has modulus bounded below one. At either endpoint, expansion of its
logarithm has a quadratic term with positive real Gaussian decay;
rescaling by \(j^{-1/2}\) gives the displayed Gaussian integral, and
the quartic remainder gives \(O(j^{-3/2})\). All constants are uniform
when \(\theta\) is in a compact subset of \((0,\pi)\). Differentiating
the integral any fixed number of times gives the corresponding leading
derivatives and one-power-smaller errors. This is a derivation from the
paper's integral formula, not an assumed clock-analyticity theorem.

Put

\[
 I_j(T)=\int_1^T(\xi-1)P_j(2\xi/T-1)\,d\xi.
\]

Equations (7), (15), and the Legendre equation give

\[
 I_j(T)=-\frac{T^2}{4}\sqrt{\frac2\pi}s^{3/2}j^{-5/2}
 \cos((j+1/2)\theta-\pi/4)+O(j^{-7/2}).                 \tag{16}
\]

For \(u=(\xi-1)_+\), \(v=u^2\), the endpoint identity in the
original coordinate is

\[
 \langle Q_qu,Q_qv\rangle=I_q(T)I_{q-1}(T)
 =\frac{T(T-1)^{3/2}}{2\pi}q^{-5}
       [\alpha+\sin(2q\theta)]+O(q^{-6}).               \tag{17}
\]

The first equality uses
\(e_v(T)=I_q+I_{q-1}\),
\(e_v(0)=(-1)^{q+1}(I_q-I_{q-1})\), and
\(\langle Q_qu,Q_qv\rangle=[e_v(T)^2-e_v(0)^2]/4\).
The second uses \(\cos a\cos b=[\cos(a-b)+\cos(a+b)]/2\)
and \(s=2\sqrt{T-1}/T\). The factor \(1/2\) from the quadratic
Taylor coefficient of \(h_D\) gives (14).

Only two other jet pairings can contribute at order \(q^{-5}\):
\((H_2,H_2)\) and \((H_1,H_3)\). Their orthonormal coefficients are,
respectively, proportional to \(j^{-3}\sin\chi_j\) and the pair
\(-j^{-2}\cos\chi_j,j^{-4}\cos\chi_j\), with
\(\chi_j=(j+1/2)\theta-\pi/4\). Squaring or multiplying and summing
shows that their leading terms are smooth multiples of \(q^{-5}\):

\[
 \langle QH_2,QH_2\rangle=\frac{s^5}{5\pi}q^{-5}+O(q^{-6}),
 \qquad
 \langle QH_1,QH_3\rangle=-\frac{s^5}{5\pi}q^{-5}+O(q^{-6}).
\]

Indeed \(\sum_{j\ge q}j^{-6}=q^{-5}/5+O(q^{-6})\), while the
oscillatory sum is \(O(q^{-6})\), by one summation by parts and the
bounded partial sums of \(e^{2ij\theta}\). The remaining jet pairs
are \(O(q^{-6})\) by (9). Pairing the \(O(q^{-4})\) forward remainder
with the \(O(q^{-3/2})\) backward tail gives \(O(q^{-11/2})\); all
other remainder terms are smaller. This proves (13).

## Transfer from fixed dense histories to the actual closure

Let \(E(T)\) be the supremum up to clock \(T\) of the physical-state and
physical-time difference norm used after (4). Projection contraction and
the Lipschitz dependence of \(b=c(r/\rho)^\top\) on state give

\[
 \|H_q[\widehat b,\widehat h]-H_q[b_D,h_D]\|_F
 \le C(q^{-3/2}E+E^2).                                  \tag{18}
\]

To verify (18), expand the bilinear expression into its two cross terms
and its difference-difference term. The dense tails have the bounds
(12); the other tails are bounded by the \(L^2\) norm of the difference,
at most \(C\sqrt{T_2-1}E\). No closure-history derivative appears.

Subtracting the integral equations, using (12), and taking running
suprema gives

\[
 E(T)\le C\int_1^T E(\xi)\,d\xi+Cq^{-5}
                  +Cq^{-3/2}E(T)+CE(T)^2.               \tag{19}
\]

Choose a fixed small bootstrap upper bound for \(E\), then choose \(q\)
large enough to absorb the last two terms. Gronwall's inequality gives
\(E\le Cq^{-5}\), improving the bootstrap and hence holding on the
whole interval. All constants are independent of width. Returning to
(18) improves that discrepancy to \(O(q^{-13/2})\).

In particular,

\[
 \Delta B(T)=H_q[b_D,h_D](T)+S_B(T)+O(q^{-13/2}),
 \qquad \|S_B'\|_F\le Cq^{-5}.                          \tag{20}
\]

The exact integral defining \(S_B\) is the difference of the ordinary
\(B\) clock vector fields in (4). The other state differences obey
\(\|\Delta A'\|_F+\|\Delta c'\|+|\Delta t'|\le Cq^{-5}\).

## Detection in predictions at the same physical time

Define

\[
 g_q(T)=f_{\rm Leg}(t_{\rm Leg}(T))
                         -f_n(t_{\rm Leg}(T))\in\mathbb R^2.
\]

Taylor expansion of the ordinary prediction map, followed by the
physical-time adjustment between the two clocks, gives from (13), (20)

\[
 g_q(T)=q^{-5}V(T)\sin(2q\theta(T))+R_q(T)+O(q^{-11/2}),
 \qquad \|R_q'\|\le Cq^{-5},                            \tag{21}
\]

where

\[
 V(T)=A_D(T)^\top C(T)^\top c_D(T).                       \tag{22}
\]

The smooth term \(R_q\) contains \(q^{-5}A_D^\top D^\top c_D\),
the accumulated \(S_B\) contribution, the first-layer and readout
differences, and the term
\(-\dot f_n(t_D(T))\Delta t(T)\). Their derivatives are \(O(q^{-5})\).
The discarded quadratic terms are \(O(q^{-10})\). This explicitly
compares the predictions at the same physical time.

Let \(u=B_0A_0y\) and \(G=A_0^\top B_0^\top B_0A_0\). The exact join
jets computed in the onset proof are

\[
 b_D'(1+)=-uy^\top/Y^2,
 \qquad h_D''(1+)=B_0^\top uy^\top/Y^2.
\]

Thus \(C(T)\) is a negative nonzero multiple of
\(uu^\top B_0\). At a sufficiently small positive physical time,
\(A_D=A_0+O(t^2)\) and \(c_D=ut+O(t^2)\), so

\[
 V(T)=-\frac{T(T-1)^{3/2}\|y\|^2}{4\pi Y^4}
          [t\|u\|^2Gy+O(t^2)].                          \tag{23}
\]

Since \(G\succeq I_2/2\), choose a fixed sufficiently small interior
clock interval \([T_1,T_2]\) on which \(\|V(T)\|\ge v_*>0\),
uniformly on the initialization event. The same estimates give a
uniform bound on \(V'\).

The function \(\theta(T)=\arccos(2/T-1)\) is smooth and strictly
increasing, with derivative bounded above and below by positive
constants on this interval. For every sufficiently large integer \(q\),
choose adjacent \(T_+,T_-\) in the interval with

\[
 \sin(2q\theta(T_+))=1,\qquad
 \sin(2q\theta(T_-))=-1,
 \qquad |T_+-T_-|\le C/q.
\]

Equation (21) then yields

\[
 g_q(T_+)-g_q(T_-)=2q^{-5}V(T_+)+O(q^{-11/2})+O(q^{-6}).
\]

Its norm is at least \(v_*q^{-5}\) for large \(q\). Therefore one of
the two vectors has norm at least \(v_*q^{-5}/2\), and one of its two
training coordinates has magnitude at least \(v_*q^{-5}/(2\sqrt2)\).
The corresponding physical times lie in one fixed positive interval,
proving (1).

## Adversarial checks and remaining review status

The \(q^{-4}\) instantaneous source estimate is not a \(q^{-4}\)
prediction lower bound. Its leading phase cancels under accumulation;
the exact formula (17) exhibits the surviving \(q^{-5}\) contribution.
The argument does not infer prediction error from a parameter norm:
(21)--(23) identify the nonzero prediction coefficient and eliminate
possible cancellation by a two-time difference.

The fixed dense histories are the only histories differentiated to high
order. Equations (18)--(20) control the actual order-dependent histories
by contraction and integral stability. The estimates hold uniformly in
width, order, and the near-join boundary layer; no fixed-\(q\) Taylor
remainder is later reused at growing \(q\).

The argument is an internally derived strengthening awaiting a fresh
independent audit, especially of the global hinge estimates (8)--(12),
the interior asymptotic normalization (16)--(17), and the same-physical-
time transfer (21). No promotion or paper change is asserted.
