# Two-input restrictions on escape with bounded middle weights

2026-10-11. Scoped theoretical contribution to the existing study. Scientific
inputs were the complete assigned files `GAUSSIAN_RANK_ONE_COMPLETION.md`,
`TWO_SAMPLE_ESCAPE_ROUTE.md`, `GAUSSIAN_POSITIVE_GEOMETRY.md`, and
`GLOBAL_FAILURE_ALTERNATIVES.md`, together with `docs/notation.qmd`. Required
mathematical and research skills were read. No experiment, alternate
initialization, frozen-layer substitution, external theorem, or Git operation
was used. These are internally derived partial results, not promotion claims.

The new conclusion is conditional but stronger than merely classifying a
convergent feature tuple. For two nonparallel unit inputs, bounded middle
weights and bounded readout already force the predictions to converge to one
of four explicit projections if the limiting loss is positive. If, in
addition, the first features, middle weights, and readout converge, positive
loss requires a singular limiting middle matrix. Saturation with a nonzero
limiting backward signal cannot produce such a limit, at any correlation in
\((-1,1)\). A further result excludes an eventual nonnegative-weight,
separated-residual tail for every such correlation, extending the assigned
source's obtuse-pair result to acute pairs. Neither boundedness nor the
required state convergence is proved for the canonical Gaussian flow.

## 1. Exact model and training equations

Let \(x_1,x_2\in\mathbb R^d\) be fixed unit inputs with
\(\rho=x_1^\top x_2\in(-1,1)\), and let
\(y=(y_1,y_2)^\top\ne0\) be fixed. For width \(n\), the parameters are
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). Define
\[
p_a=Ax_a,\quad u_a=\tanh p_a,\quad z_a=Wu_a,\quad
h_a=\tanh z_a,\quad f_a=\frac1n w^\top h_a,
\quad r_a=f_a-y_a,\quad
\mathcal L=\frac12(r_1^2+r_2^2).
\]
Put \(U=(u_1,u_2)\), \(H=(h_1,h_2)\), and define the actual backward
vectors and activation derivatives
\[
D_a=1-u_a^2,\qquad E_a=1-h_a^2,\qquad
b_a=w\odot E_a,\qquad B_a=W^\top b_a.
\]
The prescribed mobilities \((n,1,n)\) give
\[
\begin{aligned}
\dot w&=-r_1h_1-r_2h_2,\\
\dot W&=-\frac1n(r_1b_1u_1^\top+r_2b_2u_2^\top),\\
\dot A&=-r_1(D_1\odot B_1)x_1^\top
         -r_2(D_2\odot B_2)x_2^\top,\\
\dot p_1&=-r_1D_1\odot B_1-\rho r_2D_2\odot B_2,\\
\dot p_2&=-\rho r_1D_1\odot B_1-r_2D_2\odot B_2.
\end{aligned}                                                    \tag{1}
\]
All vector products not written as inner products are entrywise.
Initialization remains \(A_{ij}(0)\) iid \(N(0,1)\),
\(W_{ij}(0)\) iid \(N(0,1/n)\), independently, and exactly \(w(0)=0\).

The results below are deterministic after assuming a strict loss decrease:
there is a \(T\) such that
\[
\mathcal L(T)<\mathcal L(0)=\frac12\|y\|_2^2.                 \tag{2}
\]
This happens almost surely under the prescribed Gaussian law. Indeed,
\(\dot w(0)=H(0)y\). Conditional on invertible \(W(0)\), the random
matrix \(AX\), \(X=(x_1,x_2)\), has a density because \(X\) has rank two.
Successive entrywise tanh maps and multiplication by invertible \(W(0)\)
are diffeomorphisms onto open images. Thus \(H(0)\) has a density and
\(H(0)y=0\) is null. The Gaussian middle matrix is invertible almost surely:
its determinant is a nonzero polynomial, whose zero set is null, as follows
by induction on the number of variables and the one-variable root bound.
The energy identity below therefore gives \(\dot{\mathcal L}(0)<0\).

For later use, the exact energy identity is
\[
-\dot{\mathcal L}
=\frac1n\|\dot A\|_F^2+\|\dot W\|_F^2
 +\frac1n\|\dot w\|_2^2.                                    \tag{3}
\]
It gives global existence: parameter path length on a finite interval
\([0,t]\), in this fixed metric, is at most
\(\sqrt{t\mathcal L(0)}\). A finite maximal existence endpoint would
therefore have a finite parameter limit, from which the smooth ODE extends.
The loss decreases to a limit \(\mathcal L_\infty\ge0\).

## 2. Bounded middle weights and readout force prediction convergence

**Proposition 1.** Assume (2) and
\[
\sup_{t\ge0}\bigl(\|W(t)\|_F+\|w(t)\|_2\bigr)<\infty.
                                                                  \tag{4}
\]
If \(\mathcal L_\infty>0\), then \(f(t)\) converges. Its limit is one
of the following four vectors:
\[
\begin{gathered}
(0,y_2),\qquad (y_1,0),\\
\left(\frac{y_1+y_2}{2},\frac{y_1+y_2}{2}\right),\qquad
\left(\frac{y_1-y_2}{2},-\frac{y_1-y_2}{2}\right).
\end{gathered}                                                    \tag{5}
\]
Only vectors with loss strictly between zero and \(\|y\|_2^2/2\)
can occur. Thus entries in (5) can coincide or be excluded for particular
labels. No convergence of \(U,W,w\) is assumed in this proposition.

To prove it, work with \(q=(U,W,w)\). Multiplying the last two equations
of (1) entrywise by \(D_a\) gives an autonomous smooth ODE for \(q\):
\[
\begin{aligned}
\dot u_1&=-r_1D_1^2\odot B_1
           -\rho r_2D_1\odot D_2\odot B_2,\\
\dot u_2&=-\rho r_1D_1\odot D_2\odot B_1
           -r_2D_2^2\odot B_2,
\end{aligned}                                                    \tag{6}
\]
together with the \(W,w\) equations. These equations extend smoothly to
the closed cube \(U\in[-1,1]^{n\times2}\). Under (4), \(q\) stays
in a compact set, and its velocity is bounded. The squared quantities on
the right of (3), evaluated using (1), are smooth functions of \(q\).
Their derivatives along (6) are bounded on this compact set. They are
therefore uniformly continuous in time and integrable by (3), and each
tends to zero. For completeness, a nonnegative uniformly continuous
integrable function cannot stay above \(\varepsilon>0\) along an
unbounded sequence: uniform continuity would supply disjoint intervals
of a fixed positive length on which it is at least \(\varepsilon/2\),
contradicting integrability.

Let \((U_*,W_*,w_*)\) be any accumulation point of \(q(t)\). All starred
forward and backward quantities are evaluated by the formulas in Section 1.
The limiting equations include
\[
H_*r_*=0,\qquad
r_{*,1}b_{*,1}u_{*,1}^\top+
r_{*,2}b_{*,2}u_{*,2}^\top=0.                                \tag{7}
\]
Moreover \(\mathcal L_* =\mathcal L_\infty<\|y\|_2^2/2\), so
\(w_*\ne0\) and \(f_*\ne0\). Since \(W_*\) and \(U_*\) are
finite, every entry of \(E_{*,a}\) is strictly positive.

If exactly one residual, say \(r_{*,1}\), is nonzero, choose a row with
\(w_{*,i}\ne0\). The second equation in (7) forces \(u_{*,1}=0\).
Then \(h_{*,1}=0\), so \(f_{*,1}=0\); the vanishing second residual
gives \(f_{*,2}=y_2\). This is the first vector in (5). The other
one-residual case is identical with the samples exchanged.

Suppose both residuals are nonzero. Again using a row with nonzero readout,
the second equation in (7) forces \(u_{*,1},u_{*,2}\) to be proportional.
Neither can vanish: if one vanished, the other would vanish, giving
\(f_*=0\). Hence write
\[
u_{*,2}=c\,u_{*,1},\qquad c\ne0.
\]
For each row \(i\) with \(w_{*,i}\ne0\), let
\(z=z_{*,i1}\), so \(z_{*,i2}=cz\). The two equations in (7) give
\[
r_{*,1}\tanh z+r_{*,2}\tanh(cz)=0,
\qquad
r_{*,1}\operatorname{sech}^2z
c r_{*,2}\operatorname{sech}^2(cz)=0.                        \tag{8}
\]
Eliminating the nonzero residual ratio yields
\[
\sinh(2cz)=c\sinh(2z).                                     \tag{9}
\]
If \(|c|\ne1\), (9) implies \(z=0\). Indeed,
\(v\mapsto\sinh v/v\) is even and strictly increasing for \(v>0\):
its derivative has numerator \(v\cosh v-\sinh v\), which vanishes
at zero and has positive derivative \(v\sinh v\). Thus every
nonzero-readout row would have zero top feature and \(f_*=0\), a
contradiction. Consequently \(c=s\in\{1,-1\}\).
The second equation in (8) then gives \(r_{*,2}=-s r_{*,1}\), while
oddness gives \(f_{*,2}=s f_{*,1}\). Solving gives the appropriate last
two vectors in (5).

Every accumulation point of \(f(t)\) therefore belongs to a finite set.
The curve \(f\) is continuous and bounded. Such a curve has just one
accumulation point if its accumulation set is finite: otherwise choose
disjoint small balls around the finite candidates. Infinitely many passages
between two balls would produce an unbounded sequence of times outside
their union, and compactness would produce an additional accumulation point.
This contradiction proves convergence and the proposition.

## 3. A two-coordinate saturation obstruction

The following elementary ODE fact is the step that uses two-input geometry.

**Lemma.** Let \(|\rho|<1\), and suppose real differentiable
\(p_1,p_2\) satisfy
\[
\begin{aligned}
\dot p_1&=c_1(t)\operatorname{sech}^2p_1
            +\rho c_2(t)\operatorname{sech}^2p_2,\\
\dot p_2&=\rho c_1(t)\operatorname{sech}^2p_1
            +c_2(t)\operatorname{sech}^2p_2,
\end{aligned}                                                    \tag{10}
\]
where \(c_1(t)\to c\ne0\) and \(c_2(t)\to-c\). Then the two
coordinates cannot both tend to \(+\infty\), and cannot both tend
to \(-\infty\).

Changing both signs reduces the negative-infinity case to the
positive-infinity case. Exchanging the two coordinates, if necessary,
reduces to \(c>0\). For sufficiently large time \(c_1>0\) and
\(c_2<0\). If \(\rho\le0\), the second equation in (10) makes
\(p_2\) strictly decreasing, excluding its limit \(+\infty\).
If \(0<\rho<1\), then
\[
\frac d{dt}(p_2-\rho p_1)
=(1-\rho^2)c_2\operatorname{sech}^2p_2<0.
\]
Thus \(p_2\le\rho p_1+C\). If both coordinates tended to
\(+\infty\), this bound would imply \(p_1-p_2\to+\infty\), and
therefore
\[
\frac{\operatorname{sech}^2p_1}
     {\operatorname{sech}^2p_2}
=\frac{\cosh^2p_2}{\cosh^2p_1}\longrightarrow0.
\]
The second equation in (10), divided by its strictly positive second
gate, would then give
\(\dot p_2/\operatorname{sech}^2p_2\to-c<0\).
Again \(p_2\) is eventually decreasing, a contradiction.

## 4. Any convergent bounded-middle bad limit annihilates its backward signal

**Proposition 2.** Assume (2), and suppose
\[
U(t)\to U_*,\qquad W(t)\to W_*\text{ finite},\qquad
w(t)\to w_*.
                                                                  \tag{11}
\]
If \(\mathcal L_\infty>0\), then, for each sample with
\(r_{*,a}\ne0\),
\[
W_*^\top b_{*,a}=0,
\qquad b_{*,a}=w_*\odot\operatorname{sech}^2(W_*u_{*,a})\ne0.
                                                                  \tag{12}
\]
In particular \(W_*\) is singular. Hence if (11) holds and \(W_*\)
is invertible, the actual network fits: \(\mathcal L(t)\to0\).

Under (11), Proposition 1 applies. In addition, \(\dot A\to0\) by
the compact-state argument in its proof. Since \(X=(x_1,x_2)\) has
column rank two, (1) then implies
\[
r_{*,a}D_{*,a}\odot B_{*,a}=0,\qquad a=1,2.                 \tag{13}
\]
For example, this follows by multiplying \(\dot A\) by
\(X(X^\top X)^{-1}\), which separates its two sample coefficients.

If only \(r_{*,1}\) is nonzero, the proof of Proposition 1 gives
\(u_{*,1}=0\), hence \(D_{*,1}=\mathbf1\), and (13) gives
\(B_{*,1}=0\). This proves (12) in that case, and the other one-residual
case is the same.

If both residuals are nonzero, the earlier classification gives
\[
u_{*,2}=s u_{*,1},\quad h_{*,2}=s h_{*,1},\quad
r_{*,2}=-s r_{*,1},\quad B_{*,2}=B_{*,1},\qquad s\in\{1,-1\}.
                                                                  \tag{14}
\]
For any first neuron \(j\) with \(|u_{*,j1}|<1\), equation (13)
already implies \(B_{*,j1}=0\). It remains to consider
\(|u_{*,j1}|=1\). Absorb the sample sign by replacing
\(x_2,y_2,p_2,r_2\) with \(s x_2,s y_2,s p_2,s r_2\).
Because the network is odd, the parameter loss and flow are exactly
unchanged; the new correlation is \(s\rho\in(-1,1)\). The two
preactivations of neuron \(j\) now tend to the same signed infinity,
and their coefficients in (1) are
\[
c_1(t)=-r_1(t)B_{j1}(t),\qquad
c_2(t)=-s r_2(t)B_{j2}(t).
\]
If \(B_{*,j1}\ne0\), these coefficients converge to opposite
nonzero limits by (14). Lemma (10) gives a contradiction. Thus
\(B_{*,j1}=0\) for saturated coordinates too, proving (12).

Finally, strict loss decrease implies \(w_*\ne0\). Every top gate is
positive because \(W_*\) is finite, so the displayed \(b_{*,a}\) in
(12) is nonzero. A nonzero vector in \(\ker W_*^\top\) proves
singularity.

This excludes an escape with bounded, nonsingular limiting middle weights,
even if some first-layer preactivations diverge. It does not exclude an
escape for which the middle weights diverge, the readout diverges, or the
bounded fields fail to converge. Initial Gaussian invertibility does not
prove invertibility of a limiting matrix.

## 5. A nonnegative separated-residual tail is impossible at every correlation

**Proposition 3.** Assume (2). For any \(-1<\rho<1\), there cannot exist
\(T<\infty\) and \(\delta>0\) such that, componentwise for all
\(t\ge T\),
\[
W\ge0,\quad w\ge0,\quad p_1\ge0,\quad p_2\ge0,
\qquad r_1\le-\delta,\quad r_2\ge\delta.                    \tag{17}
\]
No boundedness or convergence assumption is imposed here. Interchanging
the samples gives the opposite residual arrangement. Fixed hidden-neuron
sign gauges and sample-sign absorption give the equivalent signed variants,
because they preserve the loss and prescribed metric exactly.

All quantities \(u_a,h_a,b_a,B_a\) are nonnegative in (17). Increase
\(T\) until (2) holds there, and set \(R_y=\|y\|_2\), so
\(|r_a|\le R_y\). We first treat \(0<\rho<1\), the extension beyond
the assigned source. For each first neuron define
\[
q_{j1}=p_{j1}-\rho p_{j2},\qquad
q_{j2}=p_{j2}-\rho p_{j1}.
\]
Equation (1) gives the exact monotonicities
\[
\dot q_{j1}=(1-\rho^2)|r_1|D_{j1}B_{j1}\ge0,
\qquad
\dot q_{j2}=-(1-\rho^2)r_2D_{j2}B_{j2}\le0.                \tag{18}
\]
Partition the finitely many coordinates according to whether \(q_{j1}\)
is bounded above or tends to \(+\infty\).

For a bounded \(q_{j1}\), nonnegativity of \(p_{j2}\) gives
\(q_{j2}=(1-\rho^2)p_{j2}-\rho q_{j1}\ge-\rho q_{j1}\).
Thus both monotone \(q\) coordinates have finite limits, and the inverse
linear relations show that both \(p\) coordinates are bounded. Their
derivatives \(D_{j1},D_{j2}\) consequently have positive lower bounds.
Integrating (18) proves
\[
\int_T^\infty B_{j1}(t)\,dt<\infty,
\qquad \int_T^\infty B_{j2}(t)\,dt<\infty.                 \tag{19}
\]
Furthermore,
\[
\frac d{dt}W_{ij}^2
=\frac2n W_{ij}w_i
 \bigl(|r_1|E_{i1}u_{j1}-r_2E_{i2}u_{j2}\bigr)
\le\frac{2R_y}{n}W_{ij}w_iE_{i1}.                          \tag{20}
\]
Summing (20) over \(i\) and using (19) bounds the whole middle-weight
column \(W_{:,j}\).

For each remaining coordinate, \(q_{j1}\to\infty\) and
\(q_{j2}\le q_{j2}(T)\). Therefore
\[
p_{j1}-p_{j2}=\frac{q_{j1}-q_{j2}}{1+\rho}\to+\infty.
                                                                  \tag{21}
\]
In particular \(u_{j1}\ge u_{j2}\) after a common finite time for
these coordinates. The bounded columns treated above can contribute only
a bounded negative amount to \(z_{i1}-z_{i2}\). Hence there is a fixed
\(C\ge0\) such that, for all sufficiently large times and all rows,
\[
z_{i1}\ge z_{i2}-C.
\]
Since both preactivations are nonnegative, this implies
\[
E_{i1}\le e^{2C}E_{i2},\qquad
B_{j1}\le e^{2C}B_{j2}.                                   \tag{22}
\]
For a coordinate in (21),
\(D_{j1}/D_{j2}=\cosh^2p_{j2}/\cosh^2p_{j1}\to0\).
The second first-layer equation in (1), together with (22), now gives
\[
\dot p_{j2}
\le\bigl(\rho R_y e^{2C}D_{j1}-\delta D_{j2}\bigr)B_{j2}
\le-\frac\delta2D_{j2}B_{j2}                              \tag{23}
\]
after another finite time. Thus \(p_{j2}\) is then nonincreasing
and nonnegative. Its gate has a positive lower bound, and integration of
(23) proves \(\int_T^\infty B_{j2}<\infty\), after adding the finite
prefix. Along with (19), this proves
\[
\int_T^\infty\sum_j B_{j2}(t)\,dt<\infty.                 \tag{24}
\]
Summing (20) over \(i,j\) and using (22), (24) bounds \(\|W\|_F\)
on the whole tail.

For completeness, when \(-1<\rho\le0\), the same conclusion follows
more directly. Equation (1) gives
\[
\dot p_{j1}\ge\delta D_{j1}B_{j1},\qquad
-\dot p_{j2}\ge\delta D_{j2}B_{j2}.
\]
The second coordinate decreases within a finite nonnegative interval,
so its gate is bounded below and (24) follows immediately. Partition
coordinates according to whether the nondecreasing \(p_{j1}\) is
bounded. For bounded coordinates its gate is bounded below and the first
inequality supplies \(\int B_{j1}<\infty\); (20) bounds their middle
columns. For unbounded coordinates \(p_{j1}\to\infty\), whereas
\(p_{j2}\) remains bounded. Thus \(u_{j1}\ge u_{j2}\) eventually.
Exactly the argument leading to (22) applies, and summing (20) again
bounds \(W\).

For either correlation case, bounded \(W\), bounded \(u_2\), and
fixed finite width imply a constant \(e_2>0\) with \(E_{i2}\ge e_2\).
Equation (24) consequently gives
\[
\int_T^\infty\sum_{i,j}w_i(t)W_{ij}(t)\,dt<\infty.
\]
By nonnegativity and \(\tanh z\le z\) for \(z\ge0\),
\[
0\le f_a\le\frac1n\sum_iw_i z_{ia}
\le\frac1n\sum_{i,j}w_iW_{ij}.
\]
Thus \(f_1+f_2\) is integrable on the tail. But strict loss decrease
gives \(\Delta=\|y\|_2^2-2\mathcal L(T)>0\), and for every later time
\[
2y^\top f=\|f\|_2^2+\|y\|_2^2-\|r\|_2^2\ge\Delta.
\]
Since \(f_1,f_2\ge0\), it follows that
\(f_1+f_2\ge\Delta/(2\|y\|_\infty)>0\). This contradicts tail
integrability and proves Proposition 3.

Proposition 3 supersedes the correlation restriction in Section 5 of
`TWO_SAMPLE_ESCAPE_ROUTE.md`; it does not assert that a Gaussian trajectory
eventually has the sign pattern (17). A dense Gaussian middle matrix need
not admit a fixed row/column sign gauge making it nonnegative.

## 6. Why the direct balancedness potential does not extend to correlation

A tempting extension of the orthogonal first/middle invariant fails at an
exact integrability condition. Fix one first neuron and write
\(p=(p_1,p_2)^\top\), \(u=\tanh p\),
\(D=\operatorname{diag}(\operatorname{sech}^2p_1,
\operatorname{sech}^2p_2)\), and
\(G=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\).
Let \(v_a=-r_aB_{ja}\). Its first-coordinate dynamics and the norm of the
corresponding middle column satisfy
\[
\dot p=GDv,\qquad
\frac n2\frac d{dt}\|W_{:,j}\|_2^2=u^\top v.                \tag{25}
\]
Suppose a twice differentiable scalar \(F(p)\) were to satisfy
\(\dot F=u^\top v\) for every instantaneous driving vector \(v\).
Its gradient would necessarily be
\[
\nabla F=G^{-1}D^{-1}u
=\frac1{1-\rho^2}
\begin{pmatrix}
q(p_1)-\rho q(p_2)\\
q(p_2)-\rho q(p_1)
\end{pmatrix},
\qquad q(z)=\frac12\sinh(2z).                              \tag{26}
\]
The two cross partials in (26) are
\(-\rho\cosh(2p_2)/(1-\rho^2)\) and
\(-\rho\cosh(2p_1)/(1-\rho^2)\). For \(\rho\ne0\) they
disagree on every open set containing points with
\(|p_1|\ne|p_2|\). Such an \(F\) therefore does not exist on a
nonempty open subset of \(\mathbb R^2\). At \(\rho=0\),
\(F=\tfrac12\sum_a\sinh^2p_a\) does work and reproduces the known
columnwise invariant.

This rules out only this particular potential depending on the two
preactivations and cancelling arbitrary backward forcing. It does not
rule out a larger-state invariant, an inequality on reachable states,
or a probabilistic argument.

## 7. Claim boundary and next bottleneck

The exact new results are Propositions 1--3 and Lemma (10). They apply
at each finite width, preserve all trained layers, and use no width limit.
The Gaussian law supplies the strict initial decrease, but it does not
currently supply any of the additional boundedness or convergence assumptions.

The unresolved implication is precise: either prove that the canonical
two-input Gaussian trajectory cannot have unbounded middle weights or
readout, and control its limiting singularity, or construct an actual
nonfitting Gaussian event with probability bounded below as width grows.
The present deterministic restrictions establish neither alternative.
They also do not transfer to three or more inputs: the two-coordinate
monotonicity in Lemma (10) uses that the corrective direction has unit
self-pairing and smaller absolute cross-pairing with the single other input.
Several persistently active samples can have a combined direction with
different geometry.

Recommended route status: partial result; broad Gaussian boundedness and
unconditional fitting remain open. Reopen the bounded-middle subroute when
a convergence mechanism or a singular-limit avoidance argument for the
actual zero-readout Gaussian slice becomes available. Reopen the unbounded
middle subroute only with a separate mechanism; the compact-state proof
above cannot be applied when (4) fails.
