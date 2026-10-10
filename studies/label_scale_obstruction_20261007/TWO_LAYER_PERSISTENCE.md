# Two hidden layers: persistent geometry and the remaining Gaussian question

2026-10-10. Continuation of the arbitrary-fixed-label, multi-input question.
The requested unconditional fitting/compression theorem remains **open**.
The results below are narrower: almost-sure feature rank at each prescribed
finite time for the full class; an all-time Gaussian geometry theorem for a
linear first activation; an open finite-width non-fitting basin; and an
exact example showing why a small exceptional population cannot be discarded.
None is a high-width Gaussian non-fitting theorem or an incompressibility bound.

## 1. Contract and canonical equations

There are two hidden layers of width `n`, `m >= 2` sphere inputs
`||x_a|| = sqrt(d)`, and fixed labels `y`. Set
\[
z_a^{(1)}=Ax_a/\sqrt d,\quad h_a^{(1)}=\phi_1(z_a^{(1)}),\quad
z_a^{(2)}=Wh_a^{(1)},\quad h_a^{(2)}=\phi_2(z_a^{(2)}),\quad
f_a=w^\top h_a^{(2)}/n.
\]
Here `A,W,w` have shapes `n by d`, `n by n`, and `n`. Initially their
coordinates are independent `N(0,1)`, independent `N(0,1/n)`, and exactly
zero, respectively. Write
\[
r=f-y,\qquad \mathcal L=\|r\|^2/m,\qquad Y=\|y\|/\sqrt m.
\]
The mobility is `M = diag(n,1,n)` on the parameter blocks. Throughout this
note dots mean physical time and
\[
\|\theta\|_{M^{-1}}^2=\|A\|_F^2/n+\|W\|_F^2+\|w\|^2/n.
\]
For locally defined backward vectors
\(\delta_a=w\odot\phi_2'(z_a^{(2)})\), the exact equations are
\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(2)},\\
\dot W&=-\frac2{mn}\sum_a r_a\delta_a h_a^{(1)\top},\\
\dot A&=-\frac2m\sum_a r_a
 [\phi_1'(z_a^{(1)})\odot W^\top\delta_a]x_a^\top/\sqrt d.
\end{aligned}
\tag{1}
\]
Differentiating the loss gives
\[
\dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2,
\qquad
\|\theta(t)-\theta(s)\|_{M^{-1}}\le Y\sqrt{t-s}.
\tag{2}
\]
Indeed integrate the first equality and apply Cauchy--Schwarz on `[s,t]`.
At a hypothetical finite maximal time, the same bound makes the parameters
Cauchy; local existence at their finite limit extends the solution. Thus
every trajectory exists at all finite times. This does not prove boundedness
or fitting as time tends to infinity.

The full target retains general strip-analytic activations with bounded
derivatives, possibly unbounded activation values, fixed labels of arbitrary
size, positive initial population top-feature gap, and high probability at
each sufficiently large width. A restriction introduced in a proposition
below applies only to that proposition, not silently to the target.

## 2. An all-time Gaussian first-layer geometry theorem

**Theorem (linear first activation only).** Let `phi_1(z)=z`, with arbitrary
smooth second activation and arbitrary finite labels. For `n >= d+1`, the
prescribed Gaussian initialization has an event of probability at least
\[
1-\frac{524304(d^2+d)}{n}
 -2\exp\big((2n-d)\log9-8n\big)
\tag{3}
\]
on which, simultaneously for every finite label vector and all `t >= 0`,
\[
\frac{A(t)^\top A(t)}n\succeq\frac1{512}I_d.
\tag{4}
\]
The probability lower bound is informative only when its right side is
positive. For fixed `d` it tends to one. No small-label or small-motion
assumption is used.

### 2.1 The exact balance invariant

Define the matrix, only for this proof,
\[
B=-\frac2m\sum_a r_a\delta_a x_a^\top/\sqrt d.
\]
Equation (1) reduces to `dot A = W^T B` and `dot W = B A^T/n`. Hence
\[
C:=W^\top W-AA^\top/n
\quad\hbox{is constant,}
\tag{5}
\]
since both differentiated quadratic terms equal
\((AB^\top W+W^\top BA^\top)/n\).
The letter `C` in this section is this specific matrix, not an unspecified
constant.

Suppose its `d` smallest eigenvalues are at most `-1/512`. On their fixed
`d`-dimensional spectral subspace `V`, (5) implies
\[
\|A(t)^\top v\|^2/n=\|W(t)v\|^2-v^\top Cv
\ge\|v\|^2/512\qquad(v\in V).
\]
Choose an orthonormal basis matrix `P` for `V`. The square matrix
`A^T P / sqrt(n)` has all singular values at least `1/sqrt(512)`. Therefore
\[
A^\top A/n\succeq A^\top PP^\top A/n\succeq I_d/512,
\]
proving (4) deterministically on that initial spectral event.

### 2.2 Gaussian construction of the negative subspace

Choose an orthogonal input-column basis whose first `d` vectors span `A(0)`.
In this basis write
\[
A(0)A(0)^\top/n=\begin{pmatrix}D&0\\0&0\end{pmatrix},
\qquad W(0)=[B_0,E_0].
\]
Conditional on `A(0)`, the entries of `B_0` and `E_0` are independent
`N(0,1/n)`. Their shapes are `n by d` and `n by (n-d)`. The eigenvalues of
`D` are those of `A(0)^T A(0)/n`. Put
\(S=B_0^\top E_0E_0^\top B_0\).

The following event is sufficient:
\[
\|B_0^\top B_0-D\|_{\rm op}\le1/256,\quad
\tfrac12I_d\preceq S\preceq2I_d,\quad
\|E_0\|_{\rm op}\le8.
\tag{6}
\]
To bound its probability without importing a random-matrix theorem, Gaussian
second moments give
\[
\mathbb E\|A(0)^\top A(0)/n-I_d\|_F^2
=\mathbb E\|B_0^\top B_0-I_d\|_F^2=(d^2+d)/n.
\]
Markov's inequality at `1/512` and a union bound give failure probability
at most `524288(d^2+d)/n` for the first condition of (6).

For completeness set `k=n-d` temporarily and `M_0=E_0E_0^T`. Conditional
on `E_0`, the diagonal entries of `S` have variance
`2 tr(M_0^2)/n^2`, and its off-diagonal entries have variance
`tr(M_0^2)/n^2`; its conditional mean is `tr(M_0) I_d/n`.
Independence of the Gaussian columns and their fourth moments give
\[
\mathbb E\operatorname{tr}(M_0^2)=k(n+k+1)/n,\quad
\mathbb E\operatorname{tr}(M_0)/n=k/n,\quad
\operatorname{Var}(\operatorname{tr}(M_0)/n)=2k/n^3.
\]
Consequently
\[
\begin{aligned}
\mathbb E\|S-I_d\|_F^2
&=(d^2+d)\frac{k(n+k+1)}{n^3}
 +d\left(\frac{2k}{n^3}+\frac{d^2}{n^2}\right)\\
&\le\frac{4(d^2+d)}n.
\end{aligned}
\]
For the last inequality use `k <= n-1`, `d <= n`, and `n >= 1`.
Thus `||S-I_d||_op <= 1/2`, which suffices for the second condition of
(6), fails with probability at most `16(d^2+d)/n`.

Finally, each of the unit spheres in dimensions `n` and `n-d` has a
`1/4`-net of cardinality at most `9^n` and `9^(n-d)`: choose a maximal
separated set and compare volumes of disjoint balls of radius `1/8` inside
the ball of radius `9/8`. Approximation in both arguments of a bilinear
form gives `||E_0||_op <= 2 max_net |u^T E_0 v|`. Each pairing is Gaussian
with variance `1/n`, so the probability of `||E_0||_op > 8` is at most
`2 exp((2n-d) log 9 - 8n)`. These three bounds prove (3) for event (6).

For `u in R^d` take
\[
v=\begin{pmatrix}u\\-E_0^\top B_0u/64\end{pmatrix}.
\]
In the chosen basis the initial matrix `C` satisfies
\[
v^\top Cv=u^\top\left[B_0^\top B_0-D-S/32
+B_0^\top(E_0E_0^\top)^2B_0/4096\right]u.
\]
On (6), `E_0 E_0^T <= 64 I`, so the last two terms are at most
`-S/64 <= -I/128`. Thus `v^T C v <= -||u||^2/256`, whereas
`||v||^2 <= (1+2/4096)||u||^2 < 2||u||^2`. This is a `d`-dimensional
subspace on which the Rayleigh quotient is at most `-1/512`. The spectral
min--max principle, or diagonalization and a dimension-intersection
argument, proves the required negative eigenvalue statement.

### 2.3 What is protected

With `X=[x_1,...,x_m]/sqrt(d)`, (4) gives
\[
H^{(1)\top}H^{(1)}/n\succeq X^\top X/512.
\tag{7}
\]
This is a sample-space gap only when `X` has independent columns. It neither
covers nonlinear first activations nor guarantees a top-layer or full
tangent gap. The event (3) is independent of labels; its statement is
simultaneous in labels because the invariant proof is deterministic.

## 3. Non-fitting minima survive on every typical invariant level

Take `m=d=2`, `x_a=sqrt(2)e_a`, and
\[
\phi_1(z)=z,\qquad \phi_2(z)=(3+\cos z)/2,
\qquad y=(3a,-a),\quad a>0.
\tag{8}
\]
These activations belong to the stipulated strip-analytic class. The
Gaussian population top-feature Gram equals
\[
\frac{(1-e^{-1})^2}{8}I_2
+\left(\frac{3+e^{-1/2}}2\right)^2\mathbf1\mathbf1^\top,
\tag{9}
\]
so its smallest eigenvalue is strictly positive. To verify (9), the two
initialized first-layer columns have empirical covariance tending to `I_2`;
conditional Gaussianity of each row of `WA` then gives two independent
standard normals in the population limit. For `Z` standard normal,
`E cos Z = exp(-1/2)` and `E cos^2 Z = (1+exp(-2))/2`. These identities
follow by integrating the Gaussian characteristic function, and give (9).

On the event in Section 2, the invariant `C` has exactly two negative
eigenvalues. There are at most two because subtracting `AA^T/n` from the
positive-definite `W^T W` cannot make a negative subspace of dimension
greater than `rank A=2`: such a subspace would intersect `ker A^T`.
It has no zero eigenvalue almost surely: its determinant is a nonzero
polynomial in the Gaussian entries (it is nonzero at `A=0,W=I`). A nonzero
polynomial has a Lebesgue-null zero set by induction on the number of
variables and Fubini, applied to its one-variable coefficient polynomials.

Write its negative eigenpairs as `Cv_1=-alpha v_1` and
`Cv_2=-b v_2`, with orthonormal vectors and `alpha,b>0`. Set
\[
s=\frac{b+\sqrt{b^2+4\pi^2}}2,\qquad
A_*=[\sqrt{n\alpha}\,v_1,\sqrt{ns}\,v_2].
\]
Then `C+A_* A_*^T/n` has eigenvalues `0,s-b`, and the remaining positive
eigenvalues of `C`. Choose a factor `W_*` with this Gram and
\[
W_*v_1=0,\qquad W_*v_2=\sqrt{s-b}\,\mathbf1/\sqrt n.
\]
Such a factor is obtained by mapping the remaining eigenvectors into
orthogonal output directions perpendicular to `1`. Since `s(s-b)=pi^2`,
\[
W_*A_*=[0,\pi\mathbf1],\qquad
W_*^\top W_*-A_*A_*^\top/n=C.
\]
With `w_*=a 1` the predictions and residual are
\[
f_*=(2a,a),\qquad r_*=(-a,2a),\qquad
\mathcal L_*=5a^2/2>0.
\tag{10}
\]
The top activation derivatives vanish; also `H^{(2)}r_*=0`. Equation (1)
therefore makes every parameter velocity zero. This is a local minimum:
whenever all readout coordinates remain positive, `1 <= phi_2 <= 2` gives
`f_1-2 f_2 <= 0`. The point `f_*` is the Euclidean projection of `y` onto
that halfspace, as seen by subtracting `a(1,-2)` from `y`. The squared-loss
minimum over the halfspace is exactly (10).

Thus the balance invariant and a positive preceding-layer Gram do not
exclude non-fitting local minima, even on an invariant level drawn from
the typical Gaussian spectral event. This is **not** a reachability claim.

## 4. An open bad basin from zero readout and full-rank initial features

**Proposition.** For every fixed `n >= 2` and `a>0`, model (8) has a
nonempty open set of hidden initial parameters, with exact zero readout
and positive-definite empirical top-feature Gram, whose trajectories
converge to finite parameters with predictions `(2a,a)`. The prescribed
Gaussian law assigns this event strictly positive probability at each
fixed width. No probability lower bound uniform in width is asserted.

**Proof.** Start from
\[
A_0=[0,\mathbf1],\quad W_0=\pi I_n,\quad w_0=0.
\]
Both top preactivations are at extrema, so the hidden parameters stay
fixed. Direct substitution into (1) gives the exact readout trajectory
\[
w(t)=a(1-e^{-5t})\mathbf1.
\tag{11}
\]
It converges to the equilibrium with readout `a 1`.

We first prove a genuinely open attracting neighborhood of this equilibrium.
Near it, `W` is invertible, so `(A,W,w) -> (Z=WA,W,w)` is a smooth change
of coordinates with inverse `A=W^{-1}Z`. Use transverse coordinates
\[
\xi=(Z_{:1},Z_{:2}-\pi\mathbf1,e),\qquad
e=\mathbf1^\top w/n-a,
\]
and complementary coordinates `(W,v)`, where `v=w-(a+e)1` and `1^T v=0`.
The set `xi=0` is a manifold of equilibria of common loss `L_*`, provided
all `a+v_i` are positive. Taylor expansion of cosine and squared loss gives,
uniformly on a sufficiently small compact coordinate box,
\[
\mathcal L-\mathcal L_*
=\frac52 e^2+\frac a{4n}\sum_i(a+v_i)Z_{i1}^2
+\frac a{2n}\sum_i(a+v_i)(Z_{i2}-\pi)^2+O(\|\xi\|^3).
\tag{12}
\]
For example `f_1=2(a+e)-(1/(4n)) sum_i w_i Z_{i1}^2+O(||xi||^4)`
and `f_2=a+e+(1/(4n)) sum_i w_i (Z_{i2}-pi)^2+O(||xi||^4)`;
their residuals at `Z_:1=0,Z_:2=pi 1`, with `e` free, are
`-a+2e,2a+e`, producing (12).
The transverse Hessian is positive definite uniformly in the complementary
coordinates: its diagonal blocks on `xi=0` are
`a(a+v_i)/(2n)`, `a(a+v_i)/n`, and `5`.

Taylor's integral formula now gives positive constants `c_1,c_2,c_3`
(depending on this fixed width and neighborhood) such that, writing
`E=L-L_*`,
\[
c_1\|\xi\|^2\le E\le c_2\|\xi\|^2,
\qquad \|\nabla\mathcal L\|_M\ge c_3\sqrt E.
\tag{13}
\]
For the gradient inequality, the transverse derivative is the average
transverse Hessian times `xi`, hence has norm bounded below by a positive
multiple of `||xi||`. Smooth coordinate norm equivalence on the compact
box and the fixed positive mobility give (13).

While the trajectory remains in this box, (2) and (13) give
`E' <= -c_3^2 E`. Its metric path starting at `t_0` satisfies
\[
\int_{t_0}^t\|\dot\theta\|_{M^{-1}}\,ds
\le\frac{2}{c_3}\bigl(\sqrt{E(t_0)}-\sqrt{E(t)}\bigr).
\tag{14}
\]
This follows by writing the speed as `-E'/speed` and using (13). At
`E=0` the state is already an equilibrium, so there is no division by zero.
Choose a smaller neighborhood for which the right side of (14) is below
the metric distance to the outer boundary. A first-exit contradiction
proves trapping. Equations (13)--(14) then prove exponential loss-excess
decay, finite total path, and convergence to `xi=0`. This gives the claimed
open attracting neighborhood.

At a sufficiently large but finite time the exact trajectory (11) enters
that neighborhood. Continuous dependence of smooth finite-dimensional
flows pulls it back to an open set in the hidden-initial-parameter slice
`w_0=0`. This set contains `(A_0,W_0)`.

The base point has rank-one features, but arbitrarily nearby points have
rank two. Keep `W_0=pi I` and replace the first column of `A_0` by
`epsilon e_1/pi`, with `epsilon` small and nonzero. Put
`delta=(1-cos epsilon)/2>0`. Then
\[
H^{(2)}(0)=[2\mathbf1-\delta e_1,\mathbf1],\qquad
\det\bigl(H^{(2)}(0)^\top H^{(2)}(0)/n\bigr)
=\delta^2(n-1)/n^2>0.
\]
For sufficiently small `epsilon` this point remains in the pulled-back
basin. The positive-definite Gram condition is open, so its intersection
with that basin is a nonempty open set. The joint Gaussian density of
`A_0,W_0` is strictly positive everywhere, giving positive probability.

This does not refute the high-width theorem being sought. For example,
the certified neighborhood may be restricted to `W_ii > pi/2` for every
`i`; the probability of that particular neighborhood is then at most
\[
\exp(-\pi^2 n^2/8).
\]
Indeed each independent diagonal entry is `N(0,1/n)` and its upper-tail
probability is at most `exp(-pi^2 n/8)`. This bounds the selected certificate,
not the entire failure event. Also its initial empirical gap need not be
near the positive population value (9). The proposition disproves an
all-initializations guarantee and a probability-one fitting guarantee at
every fixed width, not sufficiently-large-width high-probability fitting.

### 4.1 The basin persists on the typical invariant levels of Section 3

The preceding base `W_0=pi I,A_0=[0,1]` has atypical positive invariant
`C`. This is not essential to the basin argument. At every base `(A_*,W_*)`
constructed in Section 3, `A_*` has two independent columns, even though
`W_*` is singular. Choose two row indices `I` for which the square matrix
`A_I` is invertible, and partition
\[
Z=WA=W_I A_I+W_{I^c}A_{I^c}.
\]
Then `(Z,A,W_{I^c},w)` are smooth local coordinates, with inverse
\[
W_I=(Z-W_{I^c}A_{I^c})A_I^{-1}.
\]
Use exactly the same transverse `xi` as in Section 4, now with complementary
coordinates `(A,W_{I^c},v)`. The loss depends only on `Z,w`, so its expansion
(12), transverse Hessian, coordinate norm equivalence, and trapping proof
are unchanged. Starting from this hidden base and zero readout again gives
(11), hence an open zero-readout basin near each such base.

There are full-rank feature starts in this basin even on the **same exact
invariant level**, not only on nearby levels. Keep `A=A_*` and replace
`W_*` by `R_epsilon W_*`, where `R_epsilon` rotates output coordinates
one and two through a small positive angle `epsilon`. This leaves `W^T W`,
`C`, and the initial first-layer Gram unchanged. Its preactivations are
`Z_:1=0,Z_:2=pi R_epsilon 1`. The first two cosine entries in the second
column differ because
\[
\cos\bigl(\pi(\cos\epsilon-\sin\epsilon)\bigr)
-\cos\bigl(\pi(\cos\epsilon+\sin\epsilon)\bigr)
=2\sin(\pi\cos\epsilon)\sin(\pi\sin\epsilon)>0
\]
for sufficiently small positive `epsilon`. The first feature column is
`2 1`, while the second is nonconstant. Thus the top-feature matrix has
rank two. The rotation can be arbitrarily small, so the perturbed
initialization stays in the basin and still converges to loss (10).

An ambient open neighborhood of this perturbed start retains full top
feature rank and has two invariant eigenvalues at most
`-min(alpha,b)/2`. The argument of Section 2 then protects its first-layer
Gram by `min(alpha,b) I_2/2` for all time. This neighborhood has positive
Gaussian probability at each fixed width. Thus a protected preceding
layer, exact zero readout, and full-rank initial top features can coexist
with non-fitting dynamics, including on every invariant level covered by
Section 3. The actual probability of such basins under wide Gaussian
initialization is still unquantified.

One can quantify the failure of the *residual-direction* criterion inside
these basins. Define the tangent Gram only here by
`K_ab=(grad f_a)^T M grad f_b`. For `m=2`, differentiation gives
`dot r=-K r` and
\[
-\frac d{dt}\log\mathcal L
=2\frac{r^\top Kr}{\|r\|^2}.
\]
Every zero-readout start has loss `5a^2`, whereas the basin endpoint has
loss `5a^2/2`. Therefore
\[
\int_0^\infty\frac{r(t)^\top K(t)r(t)}{\|r(t)\|^2}\,dt
=\frac{\log2}{2}<\infty.
\tag{14a}
\]
At the endpoint `r_*=(-a,2a)` lies exactly in the nullspace of the top
feature Gram and the full tangent Gram. This disproves an unconditional
deterministic residual-avoidance principle; it does not establish a
nonvanishing failure probability in the width limit.

## 5. An arbitrarily small corrective group can change the endpoint

This exact benchmark prevents discarding a small exceptional mass in a
putative Gaussian counterexample. In model (8), let a proportion
`1-p` of top neurons have feature vector `(2,1)` and a proportion `p` have
feature vector `(1,2)`, where `p n` is an integer and `0<p<1`. Realize these
by `Z` rows `(0,pi)` and `(pi,0)`, for example with `W=pi I` and
`A=Z/pi`. The top derivatives vanish, so hidden parameters are fixed for
all time, even while the readout trains from zero.

Let `u(t),v(t)` be the common readouts in the two groups. Then
\[
f_1=2(1-p)u+pv,\quad f_2=(1-p)u+2pv,
\qquad
\dot u=-2r_1-r_2,\quad\dot v=-r_1-2r_2.
\]
Both readout velocities start positive (`5a` and `a`). Nevertheless, the
constant feature Gram is
\[
G=\begin{pmatrix}4-3p&2\\2&1+3p\end{pmatrix},\qquad
\lambda_{\min}(G)=\frac{5-\sqrt{25-36p(1-p)}}2>0.
\tag{15}
\]
Since `m=2`, the residual equation is exactly `dot r=-G r`. Thus it fits
every label, and solving the two output equations at the endpoint gives
\[
u(\infty)=\frac{7a}{3(1-p)},\qquad
v(\infty)=-\frac{5a}{3p}.
\tag{16}
\]
The rare group changes readout sign and carries large compensating weights.
Its small mass does not imply a small eventual effect. As `p` decreases
to zero, the decay rate in (15) is asymptotic to `9p/5` and the second
readout in (16) is of order `1/p`.

This is a deterministic benchmark, not a claim that Gaussian dynamics
produces these two groups. It exposes the quantifier problem in a proposed
large-label counterexample. Writing `tau=a t`, the flow for (8) is gradient
ascent, in the same metric, of
\[
3f_1-f_2-\frac{f_1^2+f_2^2}{2a}.
\]
Its formal `a -> infinity` limit has readout velocity
`3 h_{i1}-h_{i2}` between one and five. But compact-`tau` control does not
justify behavior on `tau` of order `a`, still less all time. A group with
mass `p(a)>0` for every fixed finite `a` can matter at large enough width
and late enough time. Discarding it before the width/time limits would not
answer the fixed-label question.

## 6. Why the general activation and Gaussian-reserve extensions are open

For general `phi_1`, put `b_a=W^T delta_a` only in the following identity.
Differentiating the matrix in (5) now gives
\[
\begin{aligned}
\dot C=-\frac2{mn}\sum_a r_a\bigl[
&b_a h_a^{(1)\top}+h_a^{(1)}b_a^\top\\
&-(\phi_1'(z_a^{(1)})\odot b_a)z_a^{(1)\top}\\
&-z_a^{(1)}(\phi_1'(z_a^{(1)})\odot b_a)^\top\bigr].
\end{aligned}
\tag{17}
\]
It has no sign or cancellation supplied by the stated analytic assumptions.
For each top neuron, another direct balance calculation gives
\[
\frac d{dt}(n\|W_{i:}\|^2-w_i^2)
=-\frac4m w_i\sum_a r_a
 [z_{ia}^{(2)}\phi_2'(z_{ia}^{(2)})-\phi_2(z_{ia}^{(2)})].
\tag{18}
\]
These failures of quadratic balance do not exclude a different nonlinear
invariant; they prevent reusing (5) unchanged.

Even for a linear first activation, an initially unused Gaussian component
is not a persistent independent reserve. To see the feedback explicitly,
take `n>d=m` and `x_a=sqrt(d)e_a`, and at initialization write
\[
U=A(0),\quad Z=W(0)U,\quad H=\phi_2(Z),\quad Q=U^\top U/n,
\qquad R_{:a}=y_a[(Hy)\odot\phi_2'(Z_{:a})].
\]
Equation (1), zero readout, and differentiation give
\[
\ddot U(0)=\frac4{m^2}W(0)^\top R,\quad
\ddot W(0)=\frac4{m^2n}RU^\top,\quad
\ddot Z(0)=\frac4{m^2}[RQ+W(0)W(0)^\top R].
\tag{19}
\]
The Gaussian matrix `U` has full column rank almost surely. Conditional
on `U,Z`, the Gaussian row decomposition is
\[
W(0)=Z(U^\top U)^{-1}U^\top+V\Pi,
\]
where `Pi` is the orthogonal projection off the columns of `U` and `V`
has independent Gaussian entries of variance `1/n`, independent of `U,Z`.
The term `V Pi V^T R` consequently appears in (19). The same Gaussian
component influences the trained features at their first nonzero time
derivative. A row with `(Hy)_i=0` can still move because
`[W(0)W(0)^T R]_{i:}` need not vanish. Freezing that row's own readout
response does not freeze the shared lower layer.

More generally, if a fixed orthogonal projection `P` annihilates every lower feature
`h_a^{(1)}(s)` for `0 <= s <= T`, then (1) gives `W(t)P=W(0)P` on that
interval. But this unchanged component makes zero direct contribution to
the current preactivations, precisely because `P h_a^{(1)}(t)=0`.
Any useful persistent-reserve argument must address this feedback, rather
than treating trained feature vectors as independent Gaussian probes.

### 6.1 What finite-time support does prove without a label restriction

There is nevertheless a general finite-width support result, without
linearity or bounded activation values. Let `v=(A/sqrt(n),W)` collect the
hidden parameters in their Euclidean mobility coordinates. For fixed
finite `T`, denote by `F_T(v_0)` the hidden state at time `T` of the full
training flow starting from `v_0` and exact zero readout. Equation (2) gives
\[
\|F_T(v_0)-v_0\|\le Y\sqrt T\qquad\hbox{for every }v_0.
\tag{20}
\]
The bound is uniform over the initial hidden state because its initial
loss is always `Y^2`. Continuous dependence makes `F_T` continuous.

**Claim.** `F_T` is onto, and the random hidden state at each finite `T`
has full support in the entire hidden parameter space.

To prove onto, fix a target `z` and consider
`v -> z-[F_T(v)-v]` on the closed ball of radius `Y sqrt(T)` centered at
`z`. By (20) this is a continuous map of that ball to itself. The
[Brouwer fixed-point theorem, Theorem 3.6.13](https://math.mit.edu/classes/18.952/2018SP/files/18.952_book.pdf)
states that any continuous self-map of a finite-dimensional closed ball
has a fixed point. Its hypotheses hold for this ball and this map; a fixed
point satisfies `F_T(v)=z`. If `Y sqrt(T)=0`, the map `F_T` is the identity
and the conclusion is immediate. The preimage of any nonempty open target
set is therefore nonempty and open. The initial Gaussian density is
positive everywhere, so that preimage has positive probability.

For real-analytic activations one also gets the following precise genericity
statement. If `P(v)` is any real-analytic hidden-state statistic that is not
identically zero, then
\[
\Pr\{P(F_T(v_0))=0\}=0\qquad\hbox{for every fixed finite }T.
\tag{21}
\]
Here is a proof avoiding any density or independence assumption about the
trained state. The finite-time map is real analytic in initial parameters:
the analytic vector field has a holomorphic extension on a complex
neighborhood of each compact real trajectory segment; on sufficiently
short subintervals Picard iteration is a contraction there, uniform for
initial parameters in a smaller complex neighborhood. Its iterates are
holomorphic in those parameters and converge uniformly, so the solution
map is holomorphic locally. A finite subdivision of `[0,T]` and composition
give real analyticity at every real initial state. Local compactness and
finite-time existence from (2) are all that this argument uses.

Thus `P` composed with `F_T` is real analytic and, by surjectivity, not
identically zero. A nonzero real-analytic function on connected Euclidean
space has a null zero set. Explicitly, at each zero it has a nonzero
derivative of some finite minimal order; otherwise its local power series
vanishes and analytic continuation makes it identically zero. Removing
one differentiation from such a derivative places the point on a regular
zero hypersurface of a partial derivative. The implicit-function theorem,
countably many derivatives, and countably many local coordinate charts
cover the original zero set by measure-zero hypersurfaces. The initial
Gaussian law is absolutely continuous, proving (21).

The original positive population top-feature gap ensures such a rank
realization for **every `n >= m`**. Here are the details, including the
population matrices needed only for this argument. For `g ~ N(0,I_d)` let
\[
h(g)=\bigl(\phi_1(g^\top x_a/\sqrt d)\bigr)_{a=1}^m,\qquad
Q^{(1)}=\mathbb E[h(g)h(g)^\top],\qquad
Q^{(2)}=\mathbb E[\phi_2(Z)\phi_2(Z)^\top],\quad
Z\sim N(0,Q^{(1)}).
\]
The expectations exist because bounded derivatives imply at most linear
activation growth. Let `S` be the linear span of `h(g)` as `g` ranges over
`R^d`. This is the range of `Q^(1)`: its orthogonal complement consists
exactly of vectors `c` for which `E(c^T h(g))^2=0`. Continuity and the
positive Gaussian density make that equivalent to `c^T h(g)=0` for all
`g`. Thus `Z` has full support in `S`. Positive definiteness of `Q^(2)`
then says that the vectors `phi_2(z)`, for `z in S`, span `R^m`; otherwise
a nonzero vector orthogonal to all of them would be in its kernel.

Choose at most `m` first-layer rows whose feature vectors span `S` and
pad to `n` rows. Choose `m` vectors `z` in `S` with independent vectors
`phi_2(z)`. The first `m` rows of `W` can realize those preactivations
as linear combinations of the chosen first-layer features. The resulting
top-feature matrix has column rank `m`. Consequently its Gram determinant
is a nonzero real-analytic function of hidden parameters.

Apply (21) to `P(v)=det(H^(2)(v)^T H^(2)(v)/n)`. We have proved, for the
**full activation class, any fixed labels, and every `n >= m`**,
\[
\Pr\!\left\{\lambda_{\min}\!\left(
 H^{(2)}(T)^\top H^{(2)}(T)/n\right)>0\right\}=1
\qquad\text{for each prescribed finite }T.
\tag{22}
\]
This holds simultaneously on any prescribed countable time set. Along
almost every individual trajectory the same determinant is analytic in
time and nonzero at zero; any zeros therefore form a locally finite set.
This does **not** assert simultaneous positive rank at every real time,
a positive all-time gap, or absence of collapse at infinity. The open bad
basin of Section 4 is compatible with all these finite-time assertions.

Full support here concerns the joint hidden state, not an independently
distributed set of useful neurons, and its positive probabilities need
not be uniform in width or time. This proves a qualitative part of the
Gaussian persistence idea while leaving its decisive quantitative part open.

## 7. Literature applicability check and unresolved target

The inspected [Pham--Nguyen three-layer mean-field theorem](https://arxiv.org/html/2105.05228v1)
does not supply the missing theorem. Its inner layer uses `1/n` averaging
of width-independent weights, rather than this Gaussian `1/sqrt(n)` scale;
Assumption 1 requires bounded activations and a nowhere-zero second
activation derivative; Assumption 3 imposes convergence conditions.
Its trained-readout clause also requires initial loss strictly below the
zero-predictor loss. The present zero-readout initialization has equality.
No result from that paper is imported into the proofs above.

The closer [Chen--Yang--Zhao--Gu muP result](https://arxiv.org/html/2503.09565v1)
uses the same hidden-weight scaling, but initializes a random nonzero
readout and imposes additional generic-data and activation conditions.
Theorem 4.5 gives feature nondegeneracy at each iteration of the
infinite-width dynamics. Corollary 4.6 assumes the weights become exactly
stationary after a finite iteration. Neither supplies an all-time
quantitative gap or proves asymptotic fitting for the present zero-readout
flow. Only these statements and their assumptions were checked for
applicability; their proofs are not dependencies of this note.

The logical status is therefore:

- **Proved here:** arbitrary-label, all-time first-layer geometry in the
  linear-first-activation subclass; nonlinear bad minima on its typical
  invariant levels; a genuinely open non-fitting basin intersecting the
  zero-readout/full-rank slice at each finite width; the corrective-group
  benchmark; finite-time full hidden support and the stated analytic
  genericity; and the displayed feedback identities.
- **Not proved:** a nonvanishing bad-basin probability for fixed labels as
  width tends to infinity, or a high-probability fitting theorem excluding
  those basins. Neither possibility is ruled out.
- **Still separately required for the original compression claim:**
  quantitative all-time response/approximation control after an
  arbitrary-label fitting mechanism, if such a mechanism is proved.

The decisive remaining task is a Gaussian **reachable-trajectory** estimate:
show that a quantitatively useful residual-correcting group persists or is
created despite shared first-layer motion, or prove that it fails with
nonvanishing probability. A positive preceding-layer gap, Gaussian support
at initialization, finite-time analyticity, or a mostly saturated population
does not settle that estimate.
