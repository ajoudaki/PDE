# Arbitrary joint diagonals: a frozen-bottom theorem and the exact full-network gap

## 1. Statement

Let \(c=3^{-1/2}\).  Freeze the first-layer features

\[
 H_j=c\,u_j^2,\qquad Q_n={1\over n}\sum_jH_j^2,
\]

and train the top weights and connector by half-square-loss Euler descent.
Conditional on \(H\), the top rows have coordinates

\[
 A_i(0)\sim N(0,1),\qquad Z_i(0)\sim N(0,Q_n),
\]

independently, and evolve by

\[
\begin{aligned}
 A_i^{k+1}&=A_i^k+c\,s_k(Z_i^k)^2,\\
 Z_i^{k+1}&=Z_i^k+2cQ_n s_kA_i^kZ_i^k,\\
 f_k&={c\over n}\sum_iA_i^k(Z_i^k)^2,\qquad
 s_k=h_n(1-f_k).
\end{aligned}                                             \tag{1.1}
\]

For \(0<\delta<1\), put

\[
 \tau_n(\delta)
 =h_n\min\{k:|f_k|\ge\delta\}.
\]

**Theorem 1 (all arbitrary diagonals, frozen bottom).**  For every
deterministic \(h_n\downarrow0\),

\[
 \boxed{\tau_n(\delta)\longrightarrow0
        \quad\hbox{in probability}.}                     \tag{1.2}
\]

Thus the conclusion is independent of the relative rates of width and
mesh.  The naturally interpolated predictor and loss have a fixed change
at times tending to zero and cannot converge compact-uniformly to a
continuous initialized trace.

For the actual two-hidden-layer network, in which \(u\) is also trained,
Theorem 1 does not presently transfer.  Sections 5--7 identify the exact
missing bridge and give algebraic counterexamples to the two tempting
monotonicity shortcuts.  Consequently the arbitrary-diagonal theorem for
the full network remains open; no counterexample diagonal is proved.

## 2. Uniform control of all negative rows

Fix \(T>0\), and argue on the event that no hit occurs before time \(T\).
Then, for every \(kh_n\le T\),

\[
 (1-\delta)h_n\le s_k\le(1+\delta)h_n.                   \tag{2.1}
\]

Since the first line of (1.1) only increases \(A_i\), while \(A_i^k<0\),

\[
 |A_i^k|\le A_{i,-}^0:=(-A_i^0)_+ .
\]

The second line of (1.1) and \(|1-x|\le1+x\), \(x\ge0\), give

\[
\begin{aligned}
 |Z_i^{k+1}|
 &\le |Z_i^k|
 \{1+2cQ_n(1+\delta)h_nA_{i,-}^0\}\\
 &\le |Z_i^k|
 \exp\{2cQ_n(1+\delta)h_nA_{i,-}^0\}.
\end{aligned}
\]

Therefore, simultaneously for every \(kh_n\le T\),

\[
 A_i^k(Z_i^k)^2
 \ge
 -A_{i,-}^0(Z_i^0)^2
 \exp\{4cQ_n(1+\delta)T A_{i,-}^0\}.                    \tag{2.2}
\]

Here (2.2) is also true after \(A_i^k\) becomes nonnegative, because its
left side is then nonnegative.

The law of large numbers gives \(Q_n\to1\).  On \(Q_n\le2\), condition on
the first layer and write \(Z_i^0=\sqrt{Q_n}V_i\), where the \(V_i\) are
iid standard Gaussians, independent of the \(A_i^0\).  Define the explicit
finite Gaussian integral

\[
 B_T
 :=
 1+4c\,\mathbb E\!\left[
 G_-\,\exp\{8c(1+\delta)T G_-\}\right],
 \qquad G_-=(-G)_+.                                     \tag{2.3}
\]

The summands in (2.2) have a uniformly finite second moment for
\(Q_n\in[1/2,2]\).  Conditional Chebyshev, followed by \(Q_n\to1\), yields

\[
 {c\over n}\sum_i
 A_{i,-}^0(Z_i^0)^2
 e^{4cQ_n(1+\delta)T A_{i,-}^0}
 \le B_T                                                   \tag{2.4}
\]

with probability tending to one.  Hence the aggregate contribution of
every row that is negative at time \(k\) is bounded below by \(-B_T\),
uniformly over all \(kh_n\le T\).  No union bound over the growing number
of steps is used.

## 3. A fixed favorable Gaussian tail block

On \(Q_n\in[1/2,2]\), put \(V_i=Z_i^0/\sqrt{Q_n}\) as above.  For a fixed
\(\ell>1\), let

\[
 \mathcal S_\ell
 =\{i:A_i^0\in[\ell,\ell+1],\
          V_i\in[\ell,\ell+1]\}.
\]

Conditional on the first layer,

\[
 |\mathcal S_\ell|\sim{\rm Binomial}(n,p_\ell),\qquad
 p_\ell=\Pr\{G\in[\ell,\ell+1]\}^2>0.
\]

Thus

\[
 {|\mathcal S_\ell|\over n}\ge {p_\ell\over2}             \tag{3.1}
\]

with probability tending to one.  Every row in this set starts in the
positive quadrant and remains there.

Let

\[
 y_i^k=\min(A_i^k,Z_i^k),\qquad
 \gamma=c(1-\delta).
\]

Since \(Q_n\ge1/2\), equations (1.1), (2.1), and positivity imply

\[
 y_i^{k+1}\ge y_i^k+\gamma h_n(y_i^k)^2,\qquad
 y_i^0\ge{\ell\over\sqrt2}.                              \tag{3.2}
\]

For the scalar comparison \(y^+=y+\gamma h_ny^2\), while \(y<M\),

\[
 {1\over y}-{1\over y^+}
 ={\gamma h_n\over1+\gamma h_ny}
 \ge{\gamma h_n\over1+\gamma h_nM}.                     \tag{3.3}
\]

Consequently, for every fixed \(M<\infty\), once
\(\gamma h_nM\le1\), all rows in \(\mathcal S_\ell\) reach \(y_i^k\ge M\)
by a time bounded by

\[
 kh_n\le {2\sqrt2\over\gamma\ell}+h_n.                  \tag{3.4}
\]

This is a direct discrete estimate; no Euler-to-ODE limit is invoked.

## 4. Proof of Theorem 1

Fix an arbitrary \(T>0\).  Choose

\[
 \ell>{4\sqrt2\over\gamma T},
\]

and then choose the finite number

\[
 M^3={2(B_T+2\delta)\over c p_\ell}.                     \tag{4.1}
\]

Both choices depend on \(T,\delta,c\), but not on \(n\).  Since
\(h_n\to0\), eventually \(\gamma h_nM\le1\), and (3.4) places the common
level-\(M\) hit before \(T\).

Suppose no output hit occurred by then.  Rows in \(\mathcal S_\ell\)
contribute at least \(M^3\) each; all other currently nonnegative rows
contribute nonnegatively; and (2.4) controls every currently negative row.
Using (3.1) and (4.1),

\[
\begin{aligned}
 f_k
 &\ge c\,{|\mathcal S_\ell|\over n}M^3-B_T\\
 &\ge {cp_\ell\over2}M^3-B_T
 =2\delta>\delta ,
\end{aligned}
\]

a contradiction.  Hence

\[
 \Pr\{\tau_n(\delta)>T\}\longrightarrow0.
\]

As \(T>0\) was arbitrary, this proves (1.2).

If the first grid crossing overshoots, continuously interpolate the one
parameter update between its two endpoints.  The network output is a
continuous polynomial along that segment, so it takes one of the values
\(\delta\) or \(-\delta\) at a time at most \(\tau_n(\delta)+h_n\).
Since \(f_0\to0\), the corresponding loss differs from \(1/2\) by a fixed
amount.  This proves the interpolation assertion.

## 5. Why coefficientwise positivity does not prove the full theorem

For deterministic schedules, Gaussian expectation turns the
positive-coefficient formal Euler polynomial into an annealed monotonicity
statement.  On the finite-width loss path, however,

\[
 s_k=h_n(1-f_k)
\]

is an initialization-dependent scalar containing negative polynomial
coefficients.  Conditioning on survival \(\{|f_j|<\delta:j\le k\}\)
also destroys the independent centered-Gaussian law that makes Wick
positivity work.  Thus neither the pointwise inequality (2.1) nor formal
coefficientwise positivity yields a quenched comparison of the adaptive
trajectory.

There is in fact no pathwise split-step order, even infinitesimally.  At
width one and with the irrelevant normalization suppressed, let

\[
 f(a,w,u)=aw^2u^4,\qquad g=\nabla f,\qquad E_h=I+hg.
\]

A direct second-order expansion gives

\[
 f(E_h^2\theta)-f(E_{2h}\theta)
 =h^2\,g(\theta)^{\mathsf T}Dg(\theta)g(\theta)+O(h^3),  \tag{5.1}
\]

where

\[
\begin{aligned}
g^{\mathsf T}Dg\,g
={}&8aw^4u^{12}+32aw^6u^{10}
 +8a^3w^2u^{12}\\
&+128a^3w^4u^{10}+192a^3w^6u^8.                       \tag{5.2}
\end{aligned}
\]

For every \(a<0\) and \(wu\ne0\), (5.2) is strictly negative.  Moreover
\(|aw^2u^4|\) can be made arbitrarily small.  Hence fine feature steps can
give a smaller raw output than their coarse counterpart while the state is
strictly inside any prescribed pre-hitting output strip.  Gaussian
expectation removes the odd-in-\(a\) coefficient (5.2); that annealed
cancellation is unavailable after survival conditioning.

## 6. Why freezing the first layer is not a pathwise lower comparison

Again use the width-one raw quadratic model.  One feature step is

\[
\begin{aligned}
 a^+&=a+s w^2u^4,\\
 w^+&=w+2sawu^4,\\
 u^+&=u+4saw^2u^3.
\end{aligned}                                             \tag{6.1}
\]

The frozen-bottom step omits only the last line.  Take \(a=-1\), choose
\(\varepsilon>0\), and impose

\[
 R=w^2u^2={1/2+\varepsilon\over s},\qquad
 w^2u^4=\rho,
\]

where \(\rho>0\) is arbitrarily small.  Then

\[
 {u^+\over u}=1-4sR=-1-4\varepsilon.                    \tag{6.2}
\]

The updated \(a^+\) and \(w^+\) are identical in the full and frozen
steps, but the full terminal output equals the frozen terminal output
times \((1+4\varepsilon)^4\).  For small \(s\rho\), that common frozen
output is negative.  Therefore

\[
 f_{\rm full}^+<f_{\rm frozen}^+ .
\]

Choosing \(\rho\) so that
\((1+4\varepsilon)^4\rho<\delta\) keeps both outputs strictly inside the
pre-hitting strip.  This construction works for arbitrarily small \(s\);
the required \(w\) is an \(s\)-dependent Gaussian extreme.  It disproves
the pathwise deletion comparison needed to transfer Theorem 1.

## 7. Exact discrete reused-adjoint obstruction

For the full raw quadratic feature update, use

\[
 X_j=u_j^2,\quad Z=GX,\quad B=A\odot Z,\quad R=G^{\mathsf T}B.
\]

One step of size \(s\) is

\[
\begin{aligned}
 X_j^+&=X_j(1+4sR_j)^2
       =X_j+8sX_jR_j+16s^2X_jR_j^2,\\
 G_{ij}^+&=G_{ij}+{2s\over n}B_iX_j .
\end{aligned}                                             \tag{7.1}
\]

For a fixed initial column set \(D\), put
\(S_{iD}=\sum_{j\in D}G_{ij}X_j\).  Exact multiplication gives

\[
\begin{aligned}
 S_{iD}^+-S_{iD}
={}&8s\sum_{j\in D}G_{ij}X_jR_j
 +16s^2\sum_{j\in D}G_{ij}X_jR_j^2\\
&+{2s\over n}B_i\sum_{j\in D}X_j^2
 +{16s^2\over n}B_i\sum_{j\in D}X_j^2R_j\\
&+{32s^3\over n}B_i\sum_{j\in D}X_j^2R_j^2 .           \tag{7.2}
\end{aligned}
\]

The first and third terms are the discrete counterparts of the terms
participating in the continuous endpoint cancellation.  The three
higher-step-order terms—the second, fourth, and fifth terms—especially
the \(s^2GXR^2\) term, are exact rather than Taylor remainders.  On an
under-resolved extreme column with \(sR=O(1)\) or larger they are
leading-order and have no useful common sign.

There are two distinct discrete scales.  At the natural pre-cap
concentration scale \(L_n=\sqrt{\log n}\), a tagged column has
\(R_j\asymp L_n\).  Thus

\[
 h_nL_n\asymp1                                           \tag{7.3}
\]

is a nonperturbative **pre-cap** test regime.  In the continuous outer
variables

\[
 X=L_n^2U,\qquad R=L_n(HU+P),
\]

the exact bottom update becomes

\[
 U^+=U\{1+4(h_nL_n)(HU+P)\}^2.                          \tag{7.4}
\]

Neither the continuous tagged ODE nor the width-first finite-schedule
theorem identifies the growing-horizon dynamics of (7.4) together with
the exact response terms (7.2).

The terminal release becomes nonperturbative at a much finer mesh.  On a
branch which reaches the terminal comparison scale before the fixed-action
stop, the continuous theorem has

\[
 X\le C\sqrt{nL_n},\qquad R\ge c_0X/L_n .
\]

Thus the local relative rate reaches at least order
\(\sqrt{n/L_n}\), and the corresponding discrete release scale is

\[
 h_n\sqrt{n/L_n}\asymp1,
 \qquad
 h_n\asymp{\sqrt{L_n}\over\sqrt n}
 ={(\log n)^{1/4}\over\sqrt n}.                         \tag{7.5}
\]

This is parametrically smaller than \(L_n^{-1}\).  In particular, even
the whole intermediate band

\[
 {(\log n)^{1/4}\over\sqrt n}
 \ \lesssim\ h_n\ \ll\ {1\over\sqrt{\log n}}            \tag{7.6}
\]

can under-resolve the leader release while still resolving the pre-cap
outer clock.  No discrete covariant-Schur theorem presently controls this
band.  Equations (7.3) and (7.5) are diagnostic scales, not proved phase
boundaries.

The missing full-network theorem can now be stated precisely:

> Uniformly over every sequence \(h_n\downarrow0\), and conditional on
> survival in a fixed output strip, prove that a fixed favorable Gaussian
> tail block either retains a scalar Riccati lower channel long enough to
> force a hit, or that the reused-column/complement response which destroys
> that channel itself forces a fixed output or loss change.

This is a discrete causal anti-cancellation theorem.  The continuous
covariant-Schur result does not imply it because (7.2) contains
nonperturbative source orders, while the positive-polynomial theorem does
not imply it because (5.1)--(6.2) refute the required pathwise orders.

## 8. Claim boundary

Theorem 1 completely closes arbitrary joint width--mesh scaling for the
frozen-bottom model.  It strongly supports, but does not prove, the same
initial-layer conclusion for the full network.  The release scale (7.5),
the unresolved intermediate band (7.6), and the pre-cap scale (7.3) are
separate test regimes for a counterexample or a discrete covariant-Schur
theorem.  None is asserted to be sharp.  At present:

* no full-network arbitrary-diagonal positive theorem is proved;
* no diagonal producing a continuous initialized full-network flow is
  proved;
* the exact gap is the survival-conditioned discrete causal
  anti-cancellation statement above.
