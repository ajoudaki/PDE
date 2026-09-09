# Sine-preserving local steps and a produced capped return-source bound

2026-09-08. This independent branch read only `CONTRACT.md` and
`development/BOUNDED_SINE_PICARD.md` from the research program. No experiments or
external results are used below.

## Status

For the explicitly different, fixed activation

\[
\phi(z)=1+\tfrac12\sin z,
\qquad B=\tfrac32,\quad D=\tfrac12,
\]

this report proves three useful statements at actual finite width.

* There is an energy-dissipating return cap, applied with one common radial
  factor to the three return fields at each first-layer row. It retains all
  three trained blocks, the raw metric, and the actual initialized matrix and
  its transpose.
* An exact local first-layer step keeps sine intact. Its consistency defect in
  the raw norm is at most a constant times the time mesh, with that constant
  independent of both width and cap. Its stability constant still grows
  exponentially with the cap.
* A leave-one-initial-column comparison produces a width-uniform Gaussian tail
  estimate for the capped return field on every fixed time interval. Its tail
  scale is bounded by \(K_T\exp(K_T(1+M)T)\), where \(M\) is the return cap.

The last estimate is a source-production result, rather than a linear
evolution estimate with unknown future coefficients supplied. It is too weak
to remove the cap: its scale grows much faster than the clipping threshold.
The report also proves that a cap-independent exponential tail bound would
give global-in-time cap Cauchy convergence through an explicit Osgood estimate.
That uniform source bound is **not proved** here. Consequently this report
does not establish the contract's global canonical population theorem or its
full finite-width/raw-GD bridge.

All estimates allow singular input Gram matrices. They use only
\(\|u_i\|=1\), \(|\Gamma_{ij}|\le1\), and three inputs, without inverting
\(\Gamma\). The coefficient \(1/2\) is independent of width, data and horizon.

## 1. Finite model and a common radial cap

Use normalized finite layer norms
\(\|x\|_n^2=n^{-1}\sum_a|x_a|^2\). Write
\(u_i=x_i/\sqrt d\), \(w=\sqrt d\,W\), \(A=A_0+U\). Then the raw state norm is

\[
\|X\|_{\rm raw}^2=\|w\|_n^2+\|U\|_F^2+\|C\|_n^2,
\quad X=(w,U,C).
\]

Here \(U\) is the actual matrix increment. Its associated normalized kernel
is \(\mathcal U_{ab}=nU_{ab}\), so
\(\|\mathcal U\|_{L^2(n^{-2})}=\|U\|_F\).
The forward and backward fields are exactly

\[
z_i=w u_i,\quad h_i=\phi(z_i),\quad v_i=Ah_i,
\quad k_i=\phi(v_i),\quad f_i=\langle C,k_i\rangle_n,
\]
\[
r_i=f_i-y_i,\qquad b_i=C\phi'(v_i),\qquad q_i=A^Tb_i.
\]

At a first-layer row \(a\), let
\(\mathbf q(a)=(q_1(a),q_2(a),q_3(a))\), and define

\[
P_M(q)=\begin{cases}q,&|q|\le M,\\Mq/|q|,&|q|>M.\end{cases}
\]

This is Euclidean projection on the radius-\(M\) ball, hence is
1-Lipschitz. For completeness, the projection inequalities
\((x-P_Mx)\cdot(P_My-P_Mx)\le0\) and its counterpart with \(x,y\) swapped,
added together, give
\(|P_Mx-P_My|^2\le(x-y)\cdot(P_Mx-P_My)\); Cauchy--Schwarz gives the claim.
Write \(P_M(q)=\rho_M(|q|)q\), with \(\rho_M\in[0,1]\).

The capped physical equations are

\[
\dot w=-\sum_i r_i\phi'(z_i)(P_M\mathbf q)_i u_i^T,
\tag{1.1}
\]
\[
\dot U=-\frac1n\sum_i r_i b_i h_i^T,
\qquad \dot C=-\sum_i r_i k_i.
\tag{1.2}
\]

This cap is a proof device. It is not the contract's uncapped algorithm. In
particular, the finite initialization remains

\[
W_{ak}\sim N(0,1/d),\quad (A_0)_{ab}\sim N(0,1/n),
\quad C_a(0)\sim N(0,n^{-2}),\quad U(0)=0.
\]

Let the true first-layer raw gradient at row \(a\) be
\(g(a)=\sum_i r_i\phi'(z_i(a))q_i(a)u_i\).
The first equation is \(\dot w(a)=-\rho_M(|\mathbf q(a)|)g(a)\), so direct
differentiation of \(E=\tfrac12\sum_i r_i^2\) gives

\[
\dot E=-\langle\rho_M(|\mathbf q|)|g|^2\rangle_n
-\|\dot U\|_F^2-\|\dot C\|_n^2\le0.
\tag{1.3}
\]

Using unrelated caps for the three \(q_i\) would not give this identity when
\(\Gamma\) has off-diagonal entries. The common radial factor is essential.

## 2. Bounds that do not depend on the cap or width

Fix \(T<\infty\), and assume for the moment
\(\|A_0\|_{\rm op}\le a_0\), \(\|C(0)\|_\infty\le c_0\).
Put \(Y_1=\sum_i|y_i|\). Bounds slightly larger than those from (1.3) will be
convenient because they also apply to the approximation below:

\[
\bar C=(c_0+BY_1T)e^{3B^2T},\quad
\bar S=3B\bar C+Y_1,
\]
\[
\bar U=T\bar SBD\bar C,\quad
\bar A=a_0+\bar U,\quad
\bar Q=\sqrt3\bar A D\bar C.
\tag{2.1}
\]

Indeed, \(\sum_i|r_i|\le3B\|C\|_\infty+Y_1\), and
\(|\dot C(a)|\le B\sum_i|r_i|\). Integrating this scalar inequality yields
the displayed \(\bar C\). Next,

\[
|\dot{\mathcal U}(a,b)|
\le\sum_i|r_i|\,|b_i(a)|\,|h_i(b)|\le\bar SBD\bar C.
\]

Consequently, on \([0,T]\),

\[
\|C\|_\infty\le\bar C,\quad \sum_i|r_i|\le\bar S,
\quad \|b_i\|_\infty\le D\bar C,
\]
\[
\|\mathcal U\|_\infty,\ \|U\|_F\le\bar U,
\quad\|A\|_{\rm op}\le\bar A,
\quad\|\mathbf q\|_{H_n^3}\le\bar Q.
\tag{2.2}
\]

Both physical Gaussian queries \(h_i,b_i\) are bounded by constants in (2.2).
There is no bound asserted for an arbitrary Gaussian image of an arbitrary
bounded adapted vector.

Since \(|P_Mq|\le|q|\), the same constants give

\[
\|\dot w\|_n\le D\bar S\bar Q,
\quad \|\dot h_i\|_n\le D^2\bar S\bar Q,
\quad\|\dot U\|_{\rm op}\le\bar SBD\bar C.
\]

Therefore

\[
\|\dot v_i\|_n
\le\bar S B^2D\bar C+\bar A D^2\bar S\bar Q=:\bar V,
\]
\[
\|\dot b_i\|_n
\le BD\bar S+\bar C D\bar V=:J_T.
\tag{2.3}
\]

In particular the bounded backward query paths have a time-Lipschitz constant
in normalized \(L^2\) independent of \(M,n\). These estimates use the actual
equations and their actual adjoint. They also prove global existence of each
finite-dimensional capped flow: its field is locally Lipschitz, and the state
and its speed stay finite on every compact interval. The uncapped finite flow
has the same compact-time bounds and the same conclusion.

## 3. Exact comparison estimate, including a changed initial matrix

Consider two capped trajectories with the same cap \(M\), respective fixed
initial matrices \(A_0,\widetilde A_0\), and state difference

\[
e=\bigl(\|w-\widetilde w\|_n^2+
\|U-\widetilde U\|_F^2+\|C-\widetilde C\|_n^2\bigr)^{1/2}.
\]

Both are assumed to satisfy the common bounds (2.1)--(2.2). Set
\(F=A_0-\widetilde A_0\), and define the two forcing sizes

\[
H_F(t)=\bigl\|(F\widetilde h_i(t))_{i=1}^3\bigr\|_{H_n^3},
\qquad
B_F(t)=\bigl\|(F^T\widetilde b_i(t))_{i=1}^3\bigr\|_{H_n^3}.
\tag{3.1}
\]

The following constants are independent of \(M,n\):

\[
K_v=\sqrt3(\bar A D+B),\quad
K_r=\sqrt3B+\bar C D K_v,
\]
\[
K_b=\sqrt3D+\bar C D K_v,
\qquad K_q=\bar A K_b+\sqrt3D\bar C.
\]

Subtract the forward equations in the form
\(v-\widetilde v=A(h-\widetilde h)+(U-\widetilde U)\widetilde h+F\widetilde h\).
Subtract the adjoint equations in the form
\(q-\widetilde q=A^T(b-\widetilde b)+(U-\widetilde U)^T\widetilde b+F^T\widetilde b\).
Bounded sine derivatives and (2.2) give, successively,

\[
\|\mathbf h-\widetilde{\mathbf h}\|\le\sqrt3D e,
\quad\|\mathbf v-\widetilde{\mathbf v}\|\le K_v e+H_F,
\]
\[
|r-\widetilde r|\le K_r e+\bar C D H_F,
\quad\|\mathbf b-\widetilde{\mathbf b}\|\le K_b e+\bar C D H_F,
\]
\[
\|\mathbf q-\widetilde{\mathbf q}\|
\le K_q e+\bar A\bar C D H_F+B_F.
\tag{3.2}
\]

Norms of stacked fields in this section are in \(H_n^3\). For instance,
\(|f_i-\widetilde f_i|\le B\|C-\widetilde C\|_n+
\bar C D\|v_i-\widetilde v_i\|_n\), which proves the residual bound.

The first-layer velocity difference is bounded by

\[
D\bar Q|r-\widetilde r|
+D\bar S M\|w-\widetilde w\|_n
+D\bar S\|\mathbf q-\widetilde{\mathbf q}\|.
\tag{3.3}
\]

The middle term is where the cap enters: it bounds the product of the change
in \(\phi'(z)\) and the capped return field. The other two follow from
Cauchy--Schwarz over the three inputs and nonexpansiveness of \(P_M\).

The other two velocity differences satisfy

\[
\|\dot U-\dot{\widetilde U}\|_F
\le\sqrt3BD\bar C|r-\widetilde r|
+B\bar S\|\mathbf b-\widetilde{\mathbf b}\|
+D\bar C\bar S\|\mathbf h-\widetilde{\mathbf h}\|,
\]
\[
\|\dot C-\dot{\widetilde C}\|_n
\le\sqrt3B|r-\widetilde r|
+D\bar S\|\mathbf v-\widetilde{\mathbf v}\|.
\tag{3.4}
\]

Substitution of (3.2) into (3.3)--(3.4) produces a finite constant \(L_T\),
depending only on the displayed bounds, such that

\[
D^+e(t)\le L_T(1+M)e(t)+L_T(H_F(t)+B_F(t)).
\tag{3.5}
\]

Here \(D^+\) is the upper right derivative; the same integrated inequality
holds through points where \(e=0\). One can take \(L_T\) to be one plus the
sum of all coefficients of \(e,H_F,B_F\) after the displayed substitution,
also including \(D\bar S\). Thus (3.5) hides no stochastic or
trajectory-dependent constant. Multiplying by
\(e^{-L_T(1+M)t}\) and integrating proves

\[
e(t)\le e^{L_T(1+M)t}e(0)
+L_T\int_0^t e^{L_T(1+M)(t-s)}(H_F(s)+B_F(s))\,ds.
\tag{3.6}
\]

This comparison supplies coefficient paths through two autonomous solutions.
It is not a Dyson expansion with the unknown physical coefficients supplied
in advance.

## 4. Sine-preserving local step: the consistency defect is cap-independent

For a mesh interval \([t_k,t_{k+1}]\), compute all physical fields from the
current state \(X_k\). Keep \(r^k\), \(P_M\mathbf q^k\), \(h^k,b^k,k^k\)
fixed during this interval, and solve

\[
\frac{d}{dt}w(a,t)
=-\sum_i r_i^k\phi'(w(a,t)\cdot u_i)
(P_M\mathbf q^k(a))_i u_i,
\tag{4.1}
\]
\[
\frac{d}{dt}U=-\frac1n\sum_i r_i^k b_i^k(h_i^k)^T,
\qquad \frac{d}{dt}C=-\sum_i r_i^k k_i^k.
\tag{4.2}
\]

Equation (4.1) is an ordinary \(d\)-dimensional equation separately at each
row, with bounded smooth vector field. It is solved as a local equation; no
sine Taylor series or elementary-differential majorant is taken. The next
matrix queries use the recomputed bounded \(h_i=\phi(wu_i)\) and
\(b_i=C\phi'(Ah_i)\). Every frozen coefficient is available at the beginning
of the current step. There is no future trajectory supplied as data.

This is an auxiliary approximation, not raw GD. In particular it is not
claimed to inherit (1.3). Nevertheless its readout obeys the discrete bound

\[
\|C_{k+1}\|_\infty
\le(1+3B^2\Delta t_k)\|C_k\|_\infty+BY_1\Delta t_k.
\]

Using \(1+x\le e^x\) proves (2.1) for its mesh values and linear readout
interpolation. The same kernel increment bound proves (2.2) for \(U\).
Its raw speed is bounded independently of \(M,n\), since
\(\|P_M\mathbf q^k\|\le\bar Q\). Write this speed bound as \(V_T^*\).

Let \(F_M\) denote the exact capped field (1.1)--(1.2), and let \(X_\eta\)
be the continuous interpolation (4.1)--(4.2) on a mesh of maximum length
\(\eta\). Recompute all fields from \(X_\eta(t)\) when evaluating
\(F_M(X_\eta(t))\). Then

\[
\|X_\eta(t)-X_k\|_{\rm raw}\le V_T^*\eta.
\tag{4.3}
\]

For the first-layer consistency defect, the current sine derivative is the
same in (4.1) and in \(F_M(X_\eta(t))\). Only \(r\) and the return control
have been frozen. Consequently,

\[
\|\dot w_\eta-(F_M(X_\eta))_w\|_n
\le D\bar Q|r(X_\eta)-r(X_k)|
+D\bar S\|\mathbf q(X_\eta)-\mathbf q(X_k)\|.
\]

Apply (3.2) with \(F=0\) and (4.3). The right side is bounded by
\(D(\bar QK_r+\bar SK_q)V_T^*\eta\), which does not contain \(M\).
The bounds (3.4) for the other blocks also do not contain \(M\). Thus

\[
\|\dot X_\eta-F_M(X_\eta)\|_{\rm raw}\le K_T\eta,
\tag{4.4}
\]

with \(K_T\) independent of cap and width. Comparison with the exact capped
flow, using (3.5) with zero matrix forcing, yields

\[
\sup_{t\le T}\|X_\eta(t)-X_M(t)\|_{\rm raw}
\le K_T T\eta\,e^{L_T(1+M)T}.
\tag{4.5}
\]

This is a genuine sine-preserving nonlinear approximation with an exact
consistency estimate. Resumming the local sine evolution removes \(M\) from
the local defect; it does not remove \(M\) from comparison of two reached
states. For \(M=\infty\), the row equation (4.1) remains individually
well-defined at finite width, but (4.5) gives no width-uniform error bound.

## 5. A legal cavity construction produces capped source tails

### 5.1 The comparison and its Gaussian query

Fix a first-layer row/initial-matrix column \(j\), and write

\[
A_0=\widetilde A_0+\frac1{\sqrt n}g e_j^T,
\tag{5.1}
\]

where \(\widetilde A_0\) has column \(j\) set to zero and
\(g\sim N(0,I_n)\) is independent of all its other columns and of \(W(0),C(0)\).
Run the same capped equations with \(\widetilde A_0\), the same \(W(0),C(0)\),
and \(\widetilde U(0)=0\). Tildes denote this auxiliary cavity trajectory.

This removes a column only for a comparison argument. The target process
retains its full Gaussian matrix. No unbounded needle is used as a forward
training query. The only Gaussian contraction needed from the cavity path is

\[
G_i(t)=\frac1{\sqrt n}g^T\widetilde b_i(t).
\tag{5.2}
\]

Conditional on the cavity data, this is an actual centered Gaussian process.
On the cavity initial event
\(\|\widetilde A_0\|_{\rm op}\le a_0\),
\(\|C(0)\|_\infty\le c_0\), estimates (2.2)--(2.3) imply

\[
\mathbb E_gG_i(t)^2\le D^2\bar C^2,
\qquad
\mathbb E_g|G_i(t)-G_i(s)|^2\le J_T^2|t-s|^2.
\tag{5.3}
\]

These constants are independent of \(M,n\), even though the cavity query
itself depends on both.

Here is an elementary uniform bound following from (5.3). For any continuous
centered Gaussian process satisfying variance bound \(\sigma^2\) and increment
variance bound \(J^2|t-s|^2\),

\[
\mathbb P\left(\sup_{t\le T}|G(t)|>
c(\sigma+JT)(1+x)\right)\le c e^{-x^2/2},\qquad x\ge0,
\tag{5.4}
\]

for a numerical constant \(c\). To verify this directly, use the dyadic grids
\(kT2^{-m}\). There are at most \(2^m\) new nearest-parent increments at level
\(m\), each with standard deviation at most \(JT2^{-m+1}\). The one-variable
Gaussian tail and a union bound show that every level-\(m\) increment is at
most
\(JT2^{-m+1}(x+\sqrt{4(m+1)\log2})\), simultaneously at all levels, except on
an event of probability at most \(c e^{-x^2/2}\). Indeed the sum of level
failure probabilities is bounded by a constant times
\(e^{-x^2/2}\sum_m2^{-m}\). The sum of the displayed increment thresholds is
at most \(cJT(1+x)\). Bound \(G(0)\) by its Gaussian tail and use continuity
to pass from the dense grids to all times. This proves (5.4). Applying a union
bound to three processes gives the corresponding estimate for
\(G_*:=\sup_{t\le T}|(G_i(t))_{i=1}^3|\).

### 5.2 Small trajectory forcing and the returned column

For the matrix difference in (5.1), the exact forcing sizes (3.1) obey

\[
H_F(t)\le\frac{\sqrt3 B\|g\|_n}{\sqrt n},
\qquad B_F(t)=\frac{|(G_i(t))_{i=1}^3|}{\sqrt n}.
\tag{5.5}
\]

The first identity uses
\(F\widetilde h_i=g\widetilde h_i(j)/\sqrt n\) and
\(|\widetilde h_i(j)|\le B\); the second uses
\(F^T\widetilde b_i=e_jG_i\). The initial state difference \(e(0)\) is zero,
because \(A_0\) is treated as the fixed operator and \(U(0)=\widetilde U(0)=0\).
Equation (3.6) now gives

\[
\sup_{t\le T}e(t)
\le\frac{L_T T e^{L_T(1+M)T}}{\sqrt n}
\bigl(\sqrt3B\|g\|_n+G_*\bigr).
\tag{5.6}
\]

On the full initial event

\[
\mathcal E_n=\{\|A_0\|_{\rm op}\le a_0,
\ \|C(0)\|_\infty\le c_0\},
\tag{5.7}
\]

the cavity initial bounds hold because
\(\widetilde A_0=A_0(I-e_je_j^T)\), and
\(\|g\|_n=\|A_0e_j\|_{\ell^2}\le a_0\).
The first-layer return at the selected coordinate is exactly

\[
q_i(t,j)=G_i(t)+\frac1{\sqrt n}g^T(b_i-\widetilde b_i)(t)
+(U(t)^Tb_i(t))_j.
\tag{5.8}
\]

The increment-kernel bound gives

\[
|(U^Tb_i)_j|
=\left|\frac1n\sum_a\mathcal U_{aj}b_i(a)\right|
\le\bar U D\bar C.
\]

For the middle term of (5.8), Cauchy--Schwarz, (3.2), and (5.5)--(5.6) give

\[
\frac{|g^T(b_i-\widetilde b_i)|}{\sqrt n}
\le\sqrt n\|g\|_n\|b_i-\widetilde b_i\|_n
\le K_T e^{L_T(1+M)T}(1+G_*)
\quad\hbox{on }\mathcal E_n.
\]

Thus, enlarging deterministic \(K_T,L_T\) if necessary,

\[
\sup_{t\le T}|\mathbf q_M(t,j)|
\le K_T e^{L_T(1+M)T}(1+G_*)
\quad\hbox{on }\mathcal E_n.
\tag{5.9}
\]

Combining this with (5.3)--(5.4) proves the source estimate

\[
\mathbb P\left(\mathcal E_n\cap
\left\{\sup_{t\le T}|\mathbf q_M(t,j)|>
K_T e^{L_T(1+M)T}(1+x)\right\}\right)
\le K_T e^{-x^2/K_T},\qquad x\ge0.
\tag{5.10}
\]

The event \(\mathcal E_n\) depends on \(g\). We did **not** condition the
Gaussian law on that event. We conditioned (5.2) on cavity data, proved (5.4)
on the cavity initial event, and used that \(\mathcal E_n\) implies that
cavity event. This preserves the Gaussian calculation.

The result is uniform over \(n,j\). Integrating its tail, and averaging over
\(j\), gives, for every \(p\ge2\),

\[
\left[\mathbb E\left(1_{\mathcal E_n}\frac1n\sum_j
\sup_{t\le T}|\mathbf q_M(t,j)|^p\right)\right]^{1/p}
\le K_T e^{L_T(1+M)T}\sqrt p.
\tag{5.11}
\]

The fixed good event has probability tending to one with the actual contract
initialization. For example choose \(a_0=8,c_0=1\).
A \(1/4\)-net of the unit sphere has at most \(9^n\) points, by disjoint-ball
volume comparison. The approximation of both arguments in
\(\sup_{|x|=|y|=1}|x^TA_0y|\) gives
\(\|A_0\|_{\rm op}\le2\max_{x,y\text{ in the net}}|x^TA_0y|\).
Each fixed contraction is \(N(0,1/n)\), whence

\[
\mathbb P(\|A_0\|_{\rm op}>8)
\le2\exp\bigl(2n\log9-8n\bigr).
\]

Also
\(\mathbb P(\|C(0)\|_\infty>1)\le2n e^{-n^2/2}\).
No zero-readout replacement has entered the proof.

### 5.3 Why this does not remove the cap

The source scale produced by (5.10) is

\[
S_{T,M}=K_Te^{L_T(1+M)T}.
\]

The bound gives decay for return thresholds much larger than \(S_{T,M}\).
For fixed \(T>0\), however, \(M/S_{T,M}\to0\). It therefore does not even
show that the set \(\{|\mathbf q_M|>M\}\) has small probability as
\(M\to\infty\). Inserting (5.11) into a cap-removal argument silently loses
the decisive uniformity.

The source of this dependence has been identified exactly: it is the
\(D\bar S M\|w-\widetilde w\|_n\) term in (3.3). The local sine flow was
already kept intact. Merely invoking bounded derivatives of every order does
not reduce this term.

## 6. Precisely sufficient source improvement and its global Cauchy consequence

This section is a conditional theorem, included to quantify the remaining
obligation. It is not an assertion that the condition holds.

Consider all cap levels for the same initialization and same matrix at each
width. Work in the joint norm over initialization and a uniformly chosen
first-layer row, restricted to the fixed good event (5.7). Suppose there are
constants \(A,b>0\), depending on \(T\) and the fixed data but on neither cap
nor width, such that for every \(K\ge0\),

\[
\sup_{M,n}
\left[\mathbb E\left(1_{\mathcal E_n}\frac1n\sum_j
Q_M(j)^2\,1_{\{Q_M(j)>K\}}\right)\right]^{1/2}
\le Ae^{-bK},
\quad Q_M(j)=\sup_{t\le T}|\mathbf q_M(t,j)|.
\tag{6.1}
\]

A uniform subexponential tail for \(Q_M\) would imply (6.1), after reducing
the positive exponent \(b\). A polynomial factor arising from integration
of the tail can be absorbed into that reduction.

For \(N\ge M\), let

\[
d(t)=\left[\mathbb E\left(1_{\mathcal E_n}
\sup_{s\le t}\|X_M(s)-X_N(s)\|_{\rm raw}^2\right)\right]^{1/2}.
\]

Compare first at a common cap \(M\). In the middle term of (3.3), split the
second trajectory into \(Q_N\le K\) and \(Q_N>K\). On the first set use
\(|\phi'(z)-\phi'(\widetilde z)|\le D|z-\widetilde z|\); on the second use
\(|\phi'(z)-\phi'(\widetilde z)|\le2D\).
This replaces that term, after taking the joint norm, by

\[
D\bar S Kd(t)+2D\bar S Ae^{-bK}.
\]

Changing the cap at the second trajectory contributes at most a constant
times
\(\|(P_N-P_M)\mathbf q_N\|\le\|Q_N1_{Q_N>M}\|\le Ae^{-bM}\).
All other differences are those in (3.2)--(3.4). To justify using the path
supremum, its increase from time \(s\) to \(t\) is at most the integral of
the norm of the velocity difference over \([s,t]\). Minkowski's inequality
then bounds the increase of \(d\) by the integral of the joint velocity
norm, which is bounded using \(d(u)\) at intermediate time \(u\).
Therefore, for constants
\(c_1,c_2\) independent of \(M,N,n,K\),

\[
D^+d(t)\le c_1(1+K)d(t)+c_2Ae^{-bK}+c_2Ae^{-bM},
\qquad d(0)=0.
\tag{6.2}
\]

This estimate allows the cutoff \(K\) to be optimized; it need not equal the
cap. Let \(A_*\ge\max(A,1)\). For \(0<d\le A_*\), choose
\(K=b^{-1}\log(A_*/d)\). Then the first two terms in (6.2) are bounded by
\(c_3d\log(eA_*/d)\), with \(c_3\) independent of caps and width. Write
\(\epsilon_M=c_2Ae^{-bM}\), and \(y=d+\epsilon_M\). The function
\(x\mapsto x\log(eA_*/x)\) is increasing on \((0,A_*]\), so, while
\(y\le A_*\),

\[
D^+y\le c_4y\log(eA_*/y),\qquad y(0)=\epsilon_M.
\]

Setting \(v=\log(eA_*/y)\) gives \(D^-v\ge-c_4v\), and integration gives

\[
d(t)\le eA_*
\left(\frac{\epsilon_M}{eA_*}\right)^{e^{-c_4t}}.
\tag{6.3}
\]

For a fixed finite \(T\), the right side is less than \(A_*\) for all
\(t\le T\) once \(M\) is sufficiently large, justifying the preceding
restriction by a first-exit argument. Hence there are \(c_T,C_T>0\) such that

\[
\sup_{n,N\ge M}
\left[\mathbb E\left(1_{\mathcal E_n}
\sup_{t\le T}\|X_M(t)-X_N(t)\|_{\rm raw}^2\right)\right]^{1/2}
\le C_Te^{-c_TM}.
\tag{6.4}
\]

One can take an exponential rate proportional to \(b e^{-c_4T}\). Thus a
fixed positive exponential source-tail rate suffices for every finite
training horizon. It is not necessary to demand that the tail rate dominate
the product of the horizon and a cap-dependent Gronwall coefficient.

At fixed finite width, \(\sup_{t\le T,j}|\mathbf q_\infty(t,j)|<\infty\).
For every cap larger than that finite value, the uncapped flow also solves
the capped equations; finite-dimensional uniqueness makes the two flows
identical. Thus sending \(N\to\infty\) at fixed \(n\) in (6.4) gives the
same estimate between \(X_M\) and the actual finite-width raw GF. This step
does not replace the finite initialization.

This conditional argument handles cap removal on the actual finite model.
It still presupposes a separately verified canonical fixed-cap Gaussian
program limit before it can be combined with (4.5) into a population
construction. It also does not by itself prove bounded-primal uniqueness
without a reached-state tail condition, restartability from every reached
state, or the raw-GD velocity and integrated-speed observables.

## 7. What exact local resummation leaves open

For a single row with a supplied return control, the uncapped local equation
is

\[
\dot w=-\sum_i r_i(t)q_i(t)\phi'(w\cdot u_i)u_i.
\]

Its flow exists on finite intervals whenever the three controls are
integrable, because its vector field has integrable pointwise bounds. Two
solutions or controls are compared using a factor bounded by

\[
\exp\left(D\int_0^T\sum_i|r_i(s)q_i(s)|\,ds\right).
\tag{7.1}
\]

This follows by subtracting the vector fields, using the Lipschitz constant
\(D\) of \(\phi'\), and integrating the resulting scalar inequality. The
features themselves remain bounded throughout. Hence feature boundedness and
an exponential sensitivity factor can coexist after every sine subtree has
already been resummed.

For the special case \(\Gamma=I\), a familiar scalar flattening removes
this sensitivity from the closed feature equation. Away from the Gaussian
null set \(\cos z_i(0)=0\), put \(\ell_i=\operatorname{atanh}(\sin z_i)\).
Then
\(h_i=1+\tfrac12\tanh\ell_i\) and
\(\dot\ell_i=-\tfrac12r_iq_i\). This is only a diagnostic special case.
For general \(\Gamma\), the transformation instead gives

\[
\dot\ell_i=-\tfrac12\sum_j\Gamma_{ij}r_jq_j
\frac{\cos z_j}{\cos z_i},
\]

where it is defined, and cross-input motion can carry \(z_i\) through a zero
of \(\cos z_i\). There is no global bounded-coefficient transformed equation
of this form. Equivalently, the vector fields
\(X_i(w)=\cos(w\cdot u_i)u_i\) need not commute:

\[
[X_i,X_j]=\Gamma_{ij}
\left[-\cos(w\cdot u_i)\sin(w\cdot u_j)u_j
+\cos(w\cdot u_j)\sin(w\cdot u_i)u_i\right].
\]

Thus independent scalar local solutions cannot simply be combined into the
general-Gram flow. No orthogonality assumption has been inserted into the
proved estimates above.

### A tagged-row or short-slab refinement encounters a specific correlated term

One can replace the uniform cap in the local first-layer comparison by the
actual row-dependent coefficient

\[
\lambda_a(t)=D\sum_i|\widetilde r_i(t)|
|(P_M\widetilde{\mathbf q}(t,a))_i|,
\qquad \Lambda_a(s,t)=\int_s^t\lambda_a(u)\,du.
\]

For instance, by the subtraction leading to (3.3), the two row paths satisfy
an integral comparison with the first-layer error at time \(s\) and the
incoming forcing multiplied by \(e^{\Lambda_a(s,t)}\). The incoming forcing
includes

\[
D\bar S\,|\mathbf q(a)-\widetilde{\mathbf q}(a)|
\quad\hbox{and}\quad
D|r-\widetilde r|\,|P_M\mathbf q(a)|.
\tag{7.2}
\]

Keeping this row-dependent weight is legitimate. Replacing its effect by an
expected tagged-row response is not yet justified. The exact identity

\[
\mathbf q-\widetilde{\mathbf q}
=A^T(\mathbf b-\widetilde{\mathbf b})
+(U-\widetilde U)^T\widetilde{\mathbf b}
+F^T\widetilde{\mathbf b}
\]

puts the term

\[
M_{e^{\Lambda(s,t)}} A^T
(\mathbf b-\widetilde{\mathbf b})
\tag{7.3}
\]

inside the comparison. Here \(M\) denotes pointwise multiplication on the
first layer, not the return cap. In a linearized version, the same term
contains

\[
M_{e^{\Lambda(s,t)}}A^T M_{C\phi''(v_i)}A\,\delta h_i.
\tag{7.4}
\]

The increment \(\mathbf b-\widetilde{\mathbf b}\) depends on the removed
column \(g\). Only \(\widetilde{\mathbf b}\) is independent of that column.
Thus the primitive Gaussian calculation (5.2) controls
\(F^T\widetilde{\mathbf b}\), but does not control the correlated contraction
of \(g\) with \(\mathbf b-\widetilde{\mathbf b}\) in (5.8), or the weighted
incoming field (7.3).

An average bound for \(e^{\Lambda_a}\), even if available, does not by itself
bound (7.3) in the raw norm. Hölder's inequality would require an
\(L^p\), \(p>2\), bound for \(A^T(\mathbf b-\widetilde{\mathbf b})\), with
the appropriate smallness inherited from the cavity perturbation. The
\(L^2\) operator bound gives no such estimate. Moving the weight through
\(A^T\), or declaring the difference query independent of the removed column,
would change the calculation.

Consequently, a proposed short-slab estimate with only an
\(O((t-s)^2)\) loss of a Hölder exponent needs a new conditional comparison
bound for (7.3) or (7.4). The existing primitive Gaussian path estimate does
not supply that rate. Splitting the interval in (3.6) without such an
improvement simply multiplies the factors
\(e^{L_T(1+M)(t_{k+1}-t_k)}\), recovering the same exponent
\(L_T(1+M)T\). This identifies the exact unresolved correlated term; it is
not an impossibility claim about a finer cavity analysis.

The remaining specific improvement is now measurable: replace the
\(e^{L_T(1+M)T}\) sensitivity contribution in the actual returned-column
identity (5.8) by an estimate strong enough to imply (6.1), uniformly in the
cap. Signed Gaussian response cancellations, rather than further bounded
sine Taylor expansion, would have to supply that improvement in this route.
The present estimates neither establish such cancellations nor prove they
are impossible.

## Claim ledger

| Claim | Status |
|---|---|
| Common radial return cap dissipates the true raw loss | Proved by (1.3) |
| Bounded queries, bounded increments and cap-independent time regularity of backward queries | Proved by (2.1)--(2.3) |
| Exact state comparison with both directions of the original matrix retained | Proved by (3.1)--(3.6) |
| Sine-preserving local update with cap-independent consistency defect | Proved by (4.1)--(4.4) |
| Width-uniform approximation of the fixed-cap finite flow | Proved by (4.5), with cap-dependent stability |
| Actual capped return-source Gaussian tails | Proved by (5.10), with exponentially cap-dependent scale |
| Cap-independent compact-time subexponential source tails | Open; (5.10) does not imply them |
| Such a source bound implies global compact-time strong cap Cauchy convergence at actual finite width | Proved conditionally by (6.1)--(6.4) |
| Canonical population construction, required uniqueness and continuation, actual GF/raw-GD joint limit | Not established by this report |

This is a bounded partial result. It is not a full candidate for the
contract's resolution and should not be represented as having passed the
required isolated full-report reviews.
