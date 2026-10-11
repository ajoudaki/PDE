# Zero-readout capture at every amplitude of a constructed label direction

2026-10-10. Scoped continuation within this study. This note proves a new
capture lemma and applies it to the rank-one tanh construction already in
the study. It does not modify the separate saturated positive theorem.

Scientific inputs were the supervisor's proposed invariant-tube argument
and the complete files `TANH_BAD_BASIN.md` and `TANH_REPLICATION_CLASS.md`.
Their SHA-256 values at reading were, respectively,
`f975c3bd44d9ad97ca22102908e69a181ac1bd4de491781497e9ce65d3d55a53`
and `3e0bcb142b985d5e79c8a56f6a66ee91e06fe22b3a41bb1a262c1f8eaf32e14b`.
No experiments or external scientific retrieval were performed.

Status: complete proposed proof, author-checked; not yet independently
checked or promoted. The conclusion concerns every positive amplitude
along one fixed, constructed label direction. It does not concern every
label vector, nor does it give a width-uniform Gaussian failure probability.

## 1. Capture lemma with a scale-independent residual threshold

Let \(h:\mathbb R^k\to\mathbb R^m\) be a smooth feature map near a
fixed \(\theta_*\in\mathbb R^k\), and put \(h_*=h(\theta_*)\).
Assume \(h_*\ne0\). Let \(r_0\in\mathbb R^m\) obey

\[
r_0^\top h_*=0,\qquad Dh(\theta_*)^\top r_0=0,
\qquad Q:=\nabla_\theta^2(r_0^\top h)(\theta_*)\succ0.
\tag{1}
\]

In particular \(r_0\ne0\). For constants \(M>0\) and \(s>0\),
take labels

\[
y=s(h_*-Mr_0)
\tag{2}
\]

and write the common readout as \(s b\), with evolving scalar \(b\).
Define the unscaled reduced loss

\[
\ell_M(\theta,b)=\frac1m\|b h(\theta)-h_*+Mr_0\|_2^2.
\tag{3}
\]

The actual reduced prediction is \(s b h(\theta)\), its loss is
\(s^2\ell_M\), and its Euclidean gradient flow in the physical variables
\((\theta,sb)\) is exactly

\[
\begin{aligned}
\dot\theta
&=-s^2\nabla_\theta\ell_M
=-\frac{2s^2 b}{m}Dh(\theta)^\top
       [b h(\theta)-h_*+Mr_0],\\
\dot b
&=-\partial_b\ell_M
=-\frac2m h(\theta)^\top[b h(\theta)-h_*+Mr_0].
\end{aligned}
\tag{4}
\]

The scalar \(s\) is fixed, not an evolving variable. Thus (4) preserves
the physical readout learning rate; it does not replace it with a
chosen mobility for \(b\).

**Lemma.** Under (1), there is a finite \(M_0\), independent of \(s\),
such that for every \(M>M_0\) and every \(s>0\), the solution of (4)
starting from \((\theta_*,0)\) exists globally and converges
exponentially to \((\theta_*,1)\). The limiting actual loss is

\[
\mathcal L_*=\frac{s^2M^2}{m}\|r_0\|_2^2>0.
\tag{5}
\]

The bound on hidden displacement below and the time needed to reach
\(b=1/2\) do not depend on \(s\). The final convergence rate can depend
on \(s\).

### Explicit constants

Set \(F(\theta)=r_0^\top h(\theta)\), and choose a closed ball
\(\|\theta-\theta_*\|_2\le\rho\) so that

\[
\mu I_k\preceq\nabla^2F(\theta)\preceq\Lambda I_k
\tag{6}
\]

there for some \(0<\mu\le\Lambda<\infty\). This is possible by (1)
and continuity. On the same ball choose finite bounds

\[
\|h(\theta)\|_2\le H,\qquad
\|Dh(\theta)\|_{\rm op}\le D,\qquad
\|D^2h(\theta)[v,z]\|_2\le E\|v\|_2\|z\|_2.
\tag{7}
\]

Let \(H_0=\|h_*\|_2>0\). Choose

\[
K>\frac{3DH}{\mu},\qquad C=5DH+\Lambda K.
\]

It suffices to choose \(M\) greater than the following finite maximum:

\[
M_0=
\max\left\{
\frac K\rho,
\frac{6DK}{H_0},
\frac{4\Lambda K^2}{H_0^2},
\frac{24HE}{\mu},
\frac{64C^2}{\mu H_0^2}
\right\}.
\tag{8}
\]

All constants in (6)-(8) depend on the local feature geometry and \(r_0\),
not on \(s\).

### Proof: invariant tube

Write \(\delta=\theta-\theta_*\). Taylor's integral formula and (1),
(6) give, on the ball,

\[
\frac\mu2\|\delta\|_2^2\le F(\theta)
\le\frac\Lambda2\|\delta\|_2^2,\qquad
\delta^\top\nabla F(\theta)\ge\mu\|\delta\|_2^2,
\qquad
\|\nabla F(\theta)\|_2\le\Lambda\|\delta\|_2.
\tag{9}
\]

Consider the compact convex tube

\[
\mathcal T_M=
\{(\theta,b):\|\delta\|_2\le K/M,\ 0\le b\le2\}.
\tag{10}
\]

The first condition in (8) puts it inside the chosen ball. At the hidden
boundary \(\|\delta\|_2=K/M\), for \(0\le b\le2\),

\[
\begin{aligned}
\delta^\top Dh^\top[b h-h_*+Mr_0]
&=\delta^\top Dh^\top(bh-h_*)+M\delta^\top\nabla F\\
&\ge-3DH\|\delta\|_2+M\mu\|\delta\|_2^2\\
&=\frac K M(\mu K-3DH)>0.
\end{aligned}
\tag{11}
\]

Consequently the first equation in (4) points strictly inward at that
boundary whenever \(b>0\). When \(b=0\), its hidden component is zero.

Put \(e=h(\theta)-h_*\), so \(\|e\|_2\le DK/M\). For
\(0\le b\le1/2\), the bracket controlling \(\dot b\) has the lower
bound

\[
\begin{aligned}
h^\top h_*-b\|h\|_2^2-MF
&\ge h^\top h_*-\tfrac12\|h\|_2^2-MF\\
&=\tfrac12(H_0^2-\|e\|_2^2)-MF\\
&\ge\frac{H_0^2}{2}
-\frac{D^2K^2}{2M^2}-\frac{\Lambda K^2}{2M}
\ge\frac{H_0^2}{4}.
\end{aligned}
\tag{12}
\]

For the last inequality, (8) gives
\(DK/M<H_0/6\), hence also \(D^2K^2/M^2<H_0^2/4\), and
\(\Lambda K^2/M<H_0^2/4\). Thus

\[
\dot b\ge\frac{H_0^2}{2m}>0
\quad\text{throughout the part of the tube with }0\le b\le1/2.
\tag{13}
\]

At the upper boundary \(b=2\), use \(F\ge0\) and
\(h=h_*+e\) to get

\[
2\|h\|_2^2-h^\top h_*+MF
\ge H_0^2+3h_*^\top e+2\|e\|_2^2
\ge H_0^2-3H_0DK/M>H_0^2/2.
\tag{14}
\]

Hence \(\dot b<0\) there. The solution starts at the center of the
hidden ball and enters \(b>0\) immediately by (13). It cannot first
leave through \(b=0\) or \(b=2\), by their strict inward signs. At
any other first exit through the hidden boundary, \(b>0\), and (11)
also makes the velocity strictly inward. This proves forward invariance
of (10). Compactness and smooth local existence give global existence.

Integrating (13) shows that the first time \(T\) at which \(b=1/2\)
satisfies

\[
T\le\frac m{H_0^2}.
\tag{15}
\]

Afterwards the trajectory remains in

\[
\mathcal T_M^+=
\{(\theta,b):\|\delta\|_2\le K/M,\ 1/2\le b\le2\},
\tag{16}
\]

because (13) points upward at its lower boundary. The proof of invariance
uses the sign of \(s^2\), never its magnitude.

### Proof: strong convexity after readout growth

The Hessian of \(\ell_M\), divided by \(2/m\), has blocks

\[
\begin{aligned}
A_{\theta\theta}
&=b^2Dh^\top Dh
+b\sum_a(bh_a-h_{*,a})\nabla^2h_a
+Mb\nabla^2F,\\
A_{\theta b}
&=Dh^\top(2bh-h_*)+M\nabla F,\\
A_{bb}&=\|h\|_2^2.
\end{aligned}
\tag{17}
\]

These are Hessian blocks, not neural-network parameters. On (16), bounds
(6)-(9) and \(b\in[1/2,2]\) imply

\[
A_{\theta\theta}
\succeq(M\mu/2-6HE)I_k
\succeq(M\mu/4)I_k,
\qquad
\|A_{\theta b}\|_2\le5DH+\Lambda K=C,
\qquad
A_{bb}\ge H_0^2/4.
\tag{18}
\]

For the first bound, the possibly negative middle term in (17) has
operator norm at most \(bE\|bh-h_*\|_2\le6HE\); the fourth bound in
(8) then applies. For the last, \(\|h-h_*\|_2\le DK/M<H_0/2\).

Write \(a=M\mu/4\), \(d=H_0^2/4\). For any
\(v\in\mathbb R^k\), \(z\in\mathbb R\), Young's inequality gives

\[
\begin{aligned}
v^\top A_{\theta\theta}v+2zA_{\theta b}^\top v+A_{bb}z^2
&\ge a\|v\|_2^2-2C|z|\|v\|_2+dz^2\\
&\ge\frac a2\|v\|_2^2
   +\left(d-\frac{2C^2}{a}\right)z^2\\
&\ge\frac a2\|v\|_2^2+\frac d2z^2.
\end{aligned}
\]

The final inequality follows from the last condition in (8), which
implies \(a>4C^2/d\). Restoring the factor \(2/m\), we have

\[
\nabla^2\ell_M\succeq\lambda I_{k+1}
\quad\text{on }\mathcal T_M^+,
\qquad
\lambda=\frac{\min(M\mu,H_0^2)}{4m}>0.
\tag{19}
\]

The point \((\theta_*,1)\) is critical by (1), with
\(\ell_*:=\ell_M(\theta_*,1)=M^2\|r_0\|_2^2/m\). The set (16) is
convex, so integrating (19) along line segments gives

\[
\ell_M-\ell_*\ge\frac\lambda2
\bigl(\|\delta\|_2^2+(b-1)^2\bigr),
\qquad
\|\nabla\ell_M\|_2^2\ge2\lambda(\ell_M-\ell_*).
\tag{20}
\]

For the second inequality, apply the supporting quadratic inequality at
the current point with comparison point \((\theta_*,1)\), then use
\(u^\top v-\lambda\|v\|^2/2\le\|u\|^2/(2\lambda)\).
This also proves there is no other critical point in (16).

Finally, (4) gives the exact dissipation identity

\[
\frac{d}{dt}\ell_M
=-s^2\|\nabla_\theta\ell_M\|_2^2-|\partial_b\ell_M|^2
\le-2\lambda\min(s^2,1)(\ell_M-\ell_*).
\]

For every \(t\ge T\), therefore,

\[
0\le\ell_M(t)-\ell_*
\le[\ell_M(T)-\ell_*]
e^{-2\lambda\min(s^2,1)(t-T)}.
\tag{21}
\]

The distance bound in (20) proves exponential convergence to
\((\theta_*,1)\), and multiplying the limiting loss by \(s^2\)
gives (5). This completes the proof.

## 2. Application to the full tanh network

Use the canonical bias-free network on normalized inputs
\(X_a\in\mathbb R^d\):

\[
U_{ja}=\tanh(A_{j:}X_a),\qquad
H=\tanh(WU),\qquad f=H^\top w/n,\qquad
\mathcal L=\|f-y\|_2^2/m,
\]

with actual mobilities \((n,1,n)\) for \((A,W,w)\). Here \(X_a\)
is exactly the object called \(\bar x_a\) in the two source files.
The rank-one symmetric subspace is

\[
A_{j:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=s b.
\tag{22}
\]

Its restricted inverse-mobility metric is
\(\|\delta p\|_2^2+\delta q^2+s^2\delta b^2\). The permutation
symmetries of the loss and metric make it invariant. In the physical
variables \((p,q,sb)\), the metric is Euclidean. Consequently its
physical dynamics are exactly (4) with

\[
\theta=(p,q),\qquad
h(\theta)_a=\tanh\bigl(q\tanh(p^\top X_a)\bigr).
\tag{23}
\]

This argument and the direct normalization checks appear in Sections 2
and 3 of `TANH_REPLICATION_CLASS.md` and Section 4 of
`TANH_BAD_BASIN.md`. No width limit or optimizer change occurs.

Assume \(q_*\ne0\), (1), and the strict splitting conditions

\[
\alpha_0:=\sum_a r_{0,a}\tanh''(q_*u_a)u_a^2>0,
\qquad
q_*B_0\succ0,
\tag{24}
\]

where

\[
u_a=\tanh(p_*^\top X_a),\qquad
B_0=\sum_a r_{0,a}\tanh'(q_*u_a)
                \tanh''(p_*^\top X_a)X_aX_a^\top.
\]

At the target profile \((p_*,q_*,s)\), the actual residual is
\(sMr_0\). For a coherent physical perturbation
\((\delta\theta,\delta c)\), with \(c\) the common readout,
the reduced loss Hessian is exactly

\[
\frac2m\left[
\|h_*\delta c+sDh(\theta_*)\delta\theta\|_2^2
+s^2M\,\delta\theta^\top Q\delta\theta
\right].
\tag{25}
\]

The possible residual-weighted mixed readout term vanishes by
\(Dh(\theta_*)^\top r_0=0\). Equation (25) is positive definite:
if it is zero, positive definiteness of \(Q\) first forces
\(\delta\theta=0\), and then \(h_*\ne0\) forces
\(\delta c=0\).

The full-network splitting coefficients in the exact rank-one Hessian
decomposition are

\[
s\alpha=s^2M\alpha_0>0,
\qquad sq_*B=s^2M q_*B_0\succ0.
\tag{26}
\]

Thus the full Hessian has precisely the tangent kernel of the affine
critical manifold

\[
\mathcal M_{n,s}=
\{A_{j:}=p_*^\top\ \forall j,\quad
  W\mathbf1=q_*\mathbf1,\quad
  \mathbf1^\top w/n=s\}.
\tag{27}
\]

Every point of this manifold has the target prediction, residual, and
positive loss (5); its gradients vanish by the same moments (1).
The exact Hessian decomposition and local trapping proof in Sections 2
and 5 of `TANH_REPLICATION_CLASS.md` now give an open full-parameter
attracting neighborhood at each fixed \(n\) and \(s>0\).

For completeness, that trapping uses only the following local facts.
Choose fixed affine coordinates \((\xi,\eta)\) normal and tangent to
(27). The loss is constant and critical on \(\xi=0\), while its
normal Hessian is positive definite at the symmetric center. On a
sufficiently small neighborhood, Taylor's formula gives
\(c\|\xi\|^2\le\mathcal L-\mathcal L_*\le C\|\xi\|^2\)
and \(\|\nabla\mathcal L\|_{M_n}\ge c_0\sqrt{\mathcal L-\mathcal L_*}\).
Loss dissipation therefore gives exponential loss-excess decay and
total remaining path length at most
\(2\sqrt{\mathcal L(t_0)-\mathcal L_*}/c_0\) in the physical metric.
An inner starting neighborhood makes this smaller than the distance
to the outer boundary, so the path stays trapped and converges to (27).
These neighborhood sizes may depend on \(n,s\).

By the lemma, for one fixed \(M>M_0\) and every \(s>0\), the symmetric
zero-readout initialization

\[
A_{j:}(0)=p_*^\top,\qquad
W_{ij}(0)=q_*/n,\qquad w(0)=0
\tag{28}
\]

converges to the center of (27). At every fixed \(n,s\), it therefore
enters the full attracting neighborhood at some finite time. Continuous
dependence on the hidden initial parameters makes the preimage of this
neighborhood a nonempty open set on the exact slice \(w(0)=0\).
All initial states in that set converge to (27) at positive loss.

## 3. Existing finite data instantiate every hypothesis

The eighteen-input construction in Sections 2 and 3 of
`TANH_BAD_BASIN.md` has

\[
d=2,\qquad p_*=(1,0)^\top,\qquad q_*=1.
\]

Its inputs are distinct nonantipodal unit vectors with every pairwise
inner product greater than \(1/8\). Let \(r_0\) be its residual from
the explicit nine-by-nine moment system, without any label scaling.
Its displayed residual identities give

\[
r_0^\top h_*=0,\qquad Dh(\theta_*)^\top r_0=0,
\qquad Q=I_3,\qquad \alpha_0=1,\qquad B_0=I_2.
\tag{29}
\]

Here is the check of the hidden Hessian, which is the new lemma's central
assumption. Write \(u_a=\tanh(p_*^\top X_a)\),
\(\chi_a=\tanh'(p_*^\top X_a)\),
\(\tau_a=\tanh''(p_*^\top X_a)\),
\(\psi_a=\tanh'(u_a)\), and \(\sigma_a=\tanh''(u_a)\).
At \(q_*=1\), the residual-contracted hidden Hessian has blocks

\[
\begin{aligned}
Q_{pp}&=\sum_a r_{0,a}
       [\sigma_a\chi_a^2+\psi_a\tau_a]X_aX_a^\top=0+I_2,\\
Q_{pq}&=\sum_a r_{0,a}
       [\sigma_a u_a\chi_a+\psi_a\chi_a]X_a=0+0,\\
Q_{qq}&=\sum_a r_{0,a}\sigma_a u_a^2=1.
\end{aligned}
\]

Each zero or identity is one of the explicit source moments. Thus no
new data construction or unproved generic-moment assumption is needed.

Fix any \(M>M_0\) for these features and this residual. Then the
nonzero direction

\[
v=h_*-Mr_0
\tag{30}
\]

has the following property: for every \(s>0\) and every \(n\ge m\),
the exact canonical flow with labels \(y=sv\) has a nonempty open
zero-readout bad basin. Both feature matrices can be required to have
full column rank initially. Indeed their simultaneous full-rank set is
open and dense for distinct nonantipodal unit inputs, as proved in
Section 5 of `TANH_BAD_BASIN.md` or Section 7 of
`TANH_REPLICATION_CLASS.md`; intersect it with the open bad basin.
At every limiting point of (27), both feature matrices have rank one.
Full-rank hidden realizations also permit arbitrary-label interpolation
by the linear readout, so these positive-loss minima are nonglobal.

The independent canonical Gaussian hidden law
\((A_0)_{ij}\sim N(0,1)\),
\((W_0)_{ij}\sim N(0,1/n)\) has positive density everywhere.
Consequently that open full-rank bad basin has positive probability for
every fixed \((n,s)\). No lower bound uniform in \(n\) or \(s\) follows.

Because \(h_*\perp r_0\), the ratio of limiting loss to initial loss
on the symmetric reference trajectory is exactly

\[
\frac{\mathcal L_*}{\mathcal L(0)}
=\frac{M^2\|r_0\|_2^2}
       {\|h_*\|_2^2+M^2\|r_0\|_2^2}.
\tag{31}
\]

It is independent of \(s\), and approaches one as \(M\to\infty\).
For any prescribed label norm \(a>0\), taking \(s=a/\|v\|_2\)
therefore gives a bad-basin example at that exact norm. Fixing \(a\)
independently of \(n\) produces arbitrary positive, width-independent
label amplitudes.

The same extension by extra inputs and zero extra residual entries used
in Section 6 of `TANH_BAD_BASIN.md` keeps (29) valid for any fixed
\(m>18\); the constants and the sufficient \(M_0\) may change.

## 4. What this strengthens and what remains open

The earlier zero-readout capture argument first fixed the direction
\(h_*-r_0\) and required a sufficiently small label scale. This note
fixes the different direction \(h_*-Mr_0\), for one sufficiently large
\(M\), and proves capture at every positive scale along that direction.
It does not establish arbitrary-scale capture for the original
\(M=1\) direction.

The new proof supplies an explicit dynamical capture mechanism valid for
every relative hidden/readout mobility \(s^2>0\). Large residual normal
curvature keeps the hidden coordinates within \(K/M\), the readout
enters \([1/2,2]\) in a scale-independent time, and the reduced loss
is strongly convex on that trapped region. The full splitting conditions
then convert the symmetric path into an open basin of the actual dense
network.

These examples still do not refute sufficiently-large-width,
high-probability fitting: their Gaussian basin probabilities may vanish
as width increases. They do rule out almost-sure fitting at each fixed
width for this constructed input/label family, and remove a small-label
restriction from the available open-basin obstruction. No claim is made
for all datasets, all label directions, or generic Gaussian failure.
