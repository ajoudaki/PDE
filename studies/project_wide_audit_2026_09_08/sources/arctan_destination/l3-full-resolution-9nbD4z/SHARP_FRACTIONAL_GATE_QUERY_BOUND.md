# Sharp fractional-mass control of the actual gate difference

Candidate scoped lemma, pending independent audit. This note strengthens
the uncompressed gate estimate in ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md.
Its only probabilistic premise is that note's already specified common
all-set/time event and its prefix query estimate. The new argument is
deterministic on that event. It uses the actual reused-matrix query and
full/pruned state distances, not independent replacements.

The application here has exactly the zero-initial-readout scope of the
dependency, with Gaussian hidden initialization and either uncut dynamics
or a common prescribed dominated 1-Lipschitz middle clipping. A direct
positive-time extension to the canonical tiny readout needs its own
proof; the previously established finite-jet transfer does not provide it.
No global continuation conclusion is asserted.

## The fixed probabilistic input and the new estimate

Keep the separate neuron populations and canonical layer notation.
For each deleted middle set \(E\), hats denote its own single fully
pruned reference. Let \(y_E(t)\) be the squared state distance
\[
y_E(t)=\frac{\|x^{(1)}-\widehat x^{(1)}\|_2^2}{n}
 +\|W^{(2)}-\widehat W^{(2)}\|_{\rm F}^2
 +\|W^{(3)}-\widehat W^{(3)}\|_{\rm F}^2
 +\frac{\|W^{(4)}-\widehat W^{(4)}\|_2^2}{n},
\quad x^{(1)}=F(z^{(1)}).
\tag{1}
\]
The references share the full initial raw matrices and first layer,
but mask the deleted middle coordinates as in the dependency. Thus
\(y_E(0)=0\). Define the finite envelope
\[
Y_r(t)=\max_{|F|\le\lfloor nr\rfloor}y_F(t),\qquad 0\le r\le1.
\tag{2}
\]
It is nondecreasing in \(r\), with \(Y_r=0\) for \(r<1/n\).
There is no time supremum in this definition.

The actual top-transpose query and its coordinatewise maximal path are
\[
q^{(2)}=(W^{(3)})^T
       [W^{(4)}\odot\phi'(z^{(3)})],\qquad
q^{(2)}_{*,j}(t)=\sup_{0\le u\le t}|q^{(2)}_j(u)|.
\]
Set \(h(r)=r\log(e/r)\), with \(h(0)=0\), and
\(\Phi(x)=x[1+\tfrac12\log_+(1/x)]\), with \(\Phi(0)=0\).
The prefix estimate (6) of ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md says
that, on its common event, for each integer \(k=1,\ldots,n\),
\[
\max_{|F|\le k}\frac1n\sum_{j\in F}q^{(2)}_{*,j}(t)^2
\le C\left[
 t^2\{h(k/n)+\epsilon_n^2\}
 +t\int_0^t\Phi(Y_{k/n}(u))\,du
\right].
\tag{3}
\]
For \(k=0\), the left side is exactly zero. The constants depend only
on the fixed horizon and primal event, and not on \(n,E\), or the level
of the one prescribed common clipping. The original probability
allocation is unchanged.

For \(a\in[0,1]\), let \(\mathcal I_n(a,u)\) interpolate the *values*
\(\Phi(Y_{k/n}(u))\) linearly between neighboring size grid points:
if \(k=\lfloor na\rfloor<n\) and \(\theta=na-k\), put
\[
\mathcal I_n(a,u)
 =(1-\theta)\Phi(Y_{k/n}(u))
       +\theta\Phi(Y_{(k+1)/n}(u)).
\tag{4}
\]
At \(a=1\), set \(\mathcal I_n(1,u)=\Phi(Y_1(u))\).
At \(a=0\) it is zero. This is not an interpolation of trajectories,
and not \(\Phi\) applied to an interpolated \(Y\).

For arbitrary actual, adaptively selected weights \(0\le w_j\le1\),
of mean \(a=n^{-1}\sum_jw_j\), the new bound is
\[
\frac1n\sum_jw_jq^{(2)}_{*,j}(t)^2
\le C\left[
t^2h(a)+t^2\epsilon_n^2\min\{1,na\}
 +t\int_0^t\mathcal I_n(a,u)\,du
\right].
\tag{5}
\]
In particular, only the two deletion sizes adjacent to the actual
weight mass enter the history. No integral over all larger sizes is
needed. This statement includes \(0<a<1/n\) without assigning a
nonempty deleted set below the width floor.

## Proof of the fractional-mass inequality

Fix \(n,t\) and the realized path, and sort the nonnegative numbers
\(q^{(2)}_{*,j}(t)^2\) in descending order as
\(b_1\ge\cdots\ge b_n\ge0\). For \(k=0,\ldots,n\), let
\[
B_k=\frac1n\sum_{j=1}^k b_j,\qquad B_0=0.
\]
These are exactly the left sides of (3), including repeated values.
For \(na=k+\theta\), \(k<n\), the elementary fractional selection bound is
\[
\frac1n\sum_jw_jq^{(2)}_{*,j}(t)^2
\le B_k+\frac{\theta}{n}b_{k+1}
 =(1-\theta)B_k+\theta B_{k+1}.
\tag{6}
\]
To prove it, reorder the weights with the \(b_j\), and write
\[
\sum_jw_jb_j
=(k+\theta)b_{k+1}+\sum_jw_j(b_j-b_{k+1}).
\]
For \(j\le k\), the last summand is at most \(b_j-b_{k+1}\)
because \(w_j\le1\). For \(j>k\), it is nonpositive because
\(w_j\ge0\). This yields (6). For \(a=1\) the bound is the full
sum; for \(a=0\) all weights vanish. Equality is attained by filling
the first \(k\) coordinates and assigning weight \(\theta\) to the
next. Thus (6) is sharp given only the weight constraints.

Apply (3) at the two sizes in (6), using the exact zero at \(k=0\).
Since \(h''(r)=-1/r<0\) for \(r>0\), its continuous extension is
concave on \([0,1]\), and
\[
(1-\theta)h(k/n)+\theta h((k+1)/n)\le h(a).
\]
The width-error coefficient is
\((1-\theta)\mathbf1_{\{k\ge1\}}+\theta=\min\{1,na\}\).
The history interpolates exactly as (4). This proves (5).
All possible selected sets were already covered on the common event,
so sorting the actual field or selecting weights from another
trajectory uses no new probability bound or independence assertion.

## The actual uncompressed gate difference

Let \(\tau\) be the prescribed clipping; \(\tau(q)=q\) gives the
uncut case. Put \(Q_E=I-P_E\) and
\[
v_E=Q_E\,[\phi'(z^{(2)})-\phi'(\widehat z^{(2)})]
                  \odot\tau(\widehat q^{(2)}),\qquad
w_j=\mathbf1_{\{j\notin E\}}
 |\phi'(z^{(2)}_j)-\phi'(\widehat z^{(2)}_j)|^2.
\]
For arctangent, \(0\le\phi'\le1\), so \(0\le w_j\le1\).
Let \(a_E=n^{-1}\sum_jw_j\). The checked primal comparison estimates
(9) in the dependency give
\[
a_E(t)\le A(y_E(t)):=\min\{1,C_0y_E(t)\},\qquad
\frac{\|q^{(2)}-\widehat q^{(2)}\|_2^2}{n}
\le C[y_E(t)+p],\quad p=|E|/n .
\tag{7}
\]
Adding and subtracting \(\tau(q^{(2)})\), contractivity and domination
of \(\tau\) give
\[
|v_{E,j}|\le\sqrt{w_j}\,|q^{(2)}_j|
                         +|q^{(2)}_j-\widehat q^{(2)}_j|.
\]
Consequently, (5) proves
\[
\begin{split}
\frac{\|v_E(t)\|_2^2}{n}\le C\bigg[
&y_E(t)+p+t^2h(a_E(t))
 +t^2\epsilon_n^2\min\{1,na_E(t)\}\\
&+t\int_0^t\mathcal I_n(a_E(t),u)\,du
\bigg].
\end{split}
\tag{8}
\]
This is the actual uncompressed vector, not merely its image under
a deleted Gaussian matrix.

Because \(\Phi\) and \(Y_r\) are nondecreasing, the interpolant in
(4) is nondecreasing in \(a\). Also \(h\) is nondecreasing on
\([0,1]\). Thus one may replace \(a_E(t)\) by \(A(y_E(t))\)
in every term of (8). The interpolation floor remains exact.

## The sharper finite comparison hierarchy

The state-energy calculation (17) in the dependency supplies
\[
y_E(t)\le C\left[
t\{h(p)+\epsilon_n^2\}
 +\int_0^t\Phi(y_E(s))\,ds
 +\int_0^t\sqrt{y_E(s)}\,\frac{\|v_E(s)\|_2}{\sqrt n}\,ds
\right].
\tag{9}
\]
It retains all trained parameter blocks and uses the actual rare
backward energy estimate; it is not inferred from a source bound
alone. All \(y_E\) range over a uniformly bounded interval.

On that interval,
\(\sqrt y\sqrt{h(A(y))}\le C\Phi(y)\). For \(C_0y\le1\),
this follows from
\(h(C_0y)\le C_0y[1+\log_+(1/y)]\); for \(C_0y>1\),
use \(h(A(y))=1\), \(y\ge1/C_0\), and \(\Phi(y)\ge y\).
Likewise, Young's inequality bounds
\(\sqrt y\,\sqrt p\) and \(\sqrt y\,\epsilon_n\) by constants
times \(y+p\) and \(y+\epsilon_n^2\), respectively.
Taking the square root of (8), using \(s\le S\), and substituting
in (9) therefore yields
\[
\begin{split}
Y_p(t)\le C\bigg[
&t\{h(p)+\epsilon_n^2\}+\int_0^t\Phi(Y_p(s))\,ds\\
&+\int_0^t
\left\{Y_p(s)\,s\int_0^s
\mathcal I_n(A(Y_p(s)),u)\,du\right\}^{1/2}\,ds
\bigg].
\end{split}
\tag{10}
\]
Here the maximum over the finitely many sets of size at most
\(\lfloor np\rfloor\) is moved inside nonnegative integrals.
Monotonicity in \(y_E\) of the full expression involving
\(\mathcal I_n(A(y_E),u)\) justifies this step. For \(p<1/n\),
\(Y_p=0\) exactly; the inequality still holds.

Equation (10) has no Hardy size integral. In the direct gate bound
the pure entropy term is \(h(a)=a\log(e/a)\), instead of the earlier
\(\Psi(a)\) with an extra logarithm. The history is evaluated at
the two sizes adjacent to \(A(Y_p(s))\). This is a sharper actual
network estimate, but this nonlinear dependence on the *error size*
is still present. Whether (10) by itself enforces deletion continuity
requires a separate scalar argument; no Osgood conclusion, clipping
removal, or canonical population theorem is inferred here.

Explicit mathematical dependency:
ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md, specifically its fixed event,
prefix bound (6), primal comparisons (9), and state-energy bound (17).
The present proof does not use its layer-cake/Hardy estimate (14)
or hierarchy (19), nor a scalar counterexample to those older bounds.
All vector norms in this note are ordinary and every empirical
normalization is displayed explicitly. No experiment was used.
