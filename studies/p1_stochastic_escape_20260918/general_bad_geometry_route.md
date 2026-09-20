# General bad-state geometry: a proof of the weaker local-minimum claim

**Frozen independent route, 2026-09-19.** Author: scoped agent
`all_bad_local_geometry`. Scientific inputs were only the complete
`docs/observable_p1.md`, `docs/NOTATION.md`, and the neutral assignment. No
other study, current proof, author history, other route, experiment, or external
scientific source was used. Required workflow and proof/research skills were
read. This is a complete proof candidate with a self-audit; independent checking
and promotion have not occurred.

Source SHA-256:

```
docs/observable_p1.md
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba
docs/NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
```

## Result and remaining obligation

In the full odd canonical population state class, with its population-L2 and
Frobenius topology, **every local minimum has zero training loss**. This holds
for arbitrary finite real labels, positive data weights, and unit inputs
pairwise neither parallel nor antiparallel. In particular, every positive-loss
equilibrium has lower-loss states in every neighborhood.

This proves the assignment's weaker target. It does **not** prove that every
positive-loss equilibrium has a finite-order descending straight line, or
exclude an equilibrium whose every nonflat straight line has a positive even
leading coefficient. The distinction remains material even for analytic sums
of squares; an example is given at the end. No reachability or convergence
claim about the canonical initialized flow is made.

The mechanism is specific. Small sets of lower-population marks may be
reassigned at arbitrarily small L2 cost. At a local minimum this forces a
certain finite sum of equal-norm tanh ridges to attain a global minimum at a
finite point. Such a sum cannot attain a finite global minimum unless it is
zero. Flat changes of the free readout then contradict positive residual when
the middle matrix is nonzero. The zero-matrix case is treated separately.

## 1. Exact state space and carrier facts

Use the nonconstant carriers from `observable_p1.md`:

\[
b_1:\Omega_1\to\mathbb R^{2d},\qquad
b_2:\Omega_2\to\mathbb R^d.
\]

Both populations are the prescribed Gaussian mark spaces with simultaneous
mark negation. Their laws, carriers, and normalization constants remain fixed.
The state is

\[
w\in L^2_{\rm odd}(\Omega_1;\mathbb R^d),\quad
c\in L^2_{\rm odd}(\Omega_2),\quad
M\in\mathbb R^{d\times2d},
\]

with the ordinary product L2/Frobenius norm. No restriction is placed on any
entry of M. The omitted constant row and column are the inactive constants of
the full odd invariant class, rather than an additional truncation.

For unit inputs \(u_a\), \(1\le a\le m\), put

\[
a_a(w)=E_1[b_1\tanh(w\cdot u_a)],\quad
z_a=Ma_a,\quad
T_c(z)=E_2[c\tanh(b_2\cdot z)],
\]
\[
f_a=T_c(z_a),\quad r_a=f_a-y_a,\qquad
\mathcal L=\sum_a\mu_a r_a^2,
\quad\mu_a>0.
\]

The normalization \(\sum_a\mu_a=1\) can be imposed but is immaterial here.
All displayed quantities are finite: b1 and b2 are bounded, tanh is bounded,
and L2 is contained in L1 on a probability space.

The canonical carriers have the following additional properties.

1. Both are odd under mark negation. The lower population is nonatomic and
   admits a measurable half-space F with \(F\cap(-F)=\varnothing\) and
   \(F\cup(-F)\) of full measure, for example \(G_1>0\).
2. The law of b1 has a positive density on a full-dimensional open set. To
   verify this, \((G,Z)\mapsto(h,k)\) is invertible on \((-1,1)^{2d}\):
   \(G_i=\operatorname{arctanh}h_i\) and
   \(Z_i=(\operatorname{arctanh}k_i-\alpha h_i)/\sqrt\tau\).
   Its Jacobian is nonsingular and the original Gaussian density is positive.
   The carrier normalization is an invertible linear transformation. In
   particular, \(E_1[b_1b_1^T]\) is positive definite and the first component
   of b1 is nonzero almost surely.
3. The law of b2 has a positive density on an open cube containing zero,
   since its coordinates are independent positive rescalings of tanh of
   nondegenerate Gaussians. Thus \(E_2[b_2b_2^T]\) is positive definite.

The constants used here satisfy \(\tau>0\) and positive normalization
denominators by the established coefficient formulas.

For fixed c, the map \(T_c\) is C2, and indeed real analytic, in finite z.
Bounded b2 and integrable c justify differentiating on compact sets; the
derivatives of tanh are bounded there. In particular

\[
\nabla T_c(z)=E_2[c\,b_2\operatorname{sech}^2(b_2\cdot z)].
\]

## 2. Equal-norm tanh sums have no attained finite global extrema

**Lemma 1.** If the unit vectors \(u_1,\ldots,u_m\) are pairwise neither
parallel nor antiparallel, and \(q\ne0\), then

\[
S(v)=\sum_a q_a\tanh(u_a\cdot v),\qquad v\in\mathbb R^d,
\]

attains neither a global minimum nor a global maximum at a finite v.

First construct a rotationally invariant random vector Z in \(\mathbb R^d\)
with full support and with every unit projection having distribution function

\[
P(u\cdot Z\le x)=\frac1{1+e^{-2x}}.
\tag{1}
\]

A self-contained construction is supplied below. It gives

\[
\tanh(u\cdot v)=E[\operatorname{sign}(u\cdot(v+Z))].
\tag{2}
\]

Define the piecewise constant function
\(C(x)=\sum_a q_a\operatorname{sign}(u_a\cdot x)\) off the finitely many
hyperplanes. C is nonconstant. For d at least 2, choose a point on
\(u_a^\perp\) lying on no other hyperplane; crossing that hyperplane changes
C by \(2q_a\). Such a point exists because the hyperplanes are distinct and
a finite union of proper subspaces cannot cover \(u_a^\perp\). For d=1 the
input condition permits at most one vector, and the conclusion is immediate.

Let cmin and cmax be the smallest and largest values on the open chambers.
Every nonempty open chamber has positive probability under v+Z, for every
finite v, because Z has full support. Equation (2) therefore gives

\[
c_{\min}<S(v)<c_{\max}\quad\text{for every finite }v.
\]

For x in a chamber, \(S(tx)\to C(x)\) as \(t\to\infty\). Consequently
\(\inf S=c_{\min}\) and \(\sup S=c_{\max}\), with neither attained. This
proves the lemma. It also proves linear independence of the lower tanh ridges:
an identically zero sum would attain both extrema, and hence have q=0.

### Construction for (1), without a specialized external theorem

Let \(V_k\) be independent exponential random variables of rates \(2k^2\).
Then

\[
V=\sum_{k\ge1}V_k\in(0,\infty)\quad\text{almost surely},
\]

because \(E V=\sum_k(2k^2)^{-1}<\infty\). Let G be an independent standard
Gaussian vector in \(\mathbb R^d\), and take \(Z=\sqrt V G\). Conditional
on every V in \((0,\infty)\), this is a nondegenerate Gaussian; thus Z has
full support and is rotationally invariant.

Here is an elementary identification of its scalar marginal. If E and F are
independent exponential variables of rate 1, then the characteristic function
of \((E-F)/(2k)\) is

\[
\frac1{1+t^2/(4k^2)}.
\]

The characteristic function of \(\sqrt{V_k}G_1\), where G1 is a standard
scalar Gaussian, is the same, by conditioning on Vk. Therefore

\[
\sqrt{\sum_{k=1}^N V_k}\,G_1
\ \stackrel{\rm law}=\
\frac12\sum_{k=1}^N\frac{E_k-F_k}{k}.
\tag{3}
\]

The maximum AN of N independent rate-1 exponentials has the same law as
\(\sum_{k=1}^N E_k/k\). To check this, its ordered spacings are independent
exponentials with rates N,N-1,...,1: the first waiting time is the minimum of
N exponentials, and after that waiting time the surviving residual variables
are again independent rate-1 exponentials by the memoryless property.
Applying this recursively gives the stated spacings and sum.

Moreover

\[
P(A_N-\log N\le x)
 =(1-e^{-x}/N)^N\longrightarrow e^{-e^{-x}}.
\]

The limiting variable has the law of \(-\log E\). Using an independent
maximum BN, the right side of (3) thus converges in distribution to
\(\tfrac12\log(F/E)\), with E,F independent rate-1 exponentials. The left
side converges in distribution to \(\sqrt V G_1\), by the almost sure
convergence of the variances, coupling it with a single independent G1.
Finally,

\[
P\left(\tfrac12\log(F/E)\le x\right)
=E[1-e^{-e^{2x}E}]
=\frac1{1+e^{-2x}}.
\]

This proves (1) for every unit projection. Symmetry and the absence of atoms
then give (2). The equal-norm input condition is used exactly in obtaining
the same scalar marginal for every input projection.

## 3. What rare-mark changes force at a local minimum

**Lemma 2.** At any local minimum in the stated product topology,

\[
r_a M^T\nabla T_c(z_a)=0\qquad\text{for every }a.
\tag{4}
\]

Hold c,M fixed. Regarding the loss as a smooth finite-dimensional function of
\((a_1,\ldots,a_m)\), define

\[
A_a=2\mu_a r_a M^T\nabla T_c(z_a)\in\mathbb R^{2d}.
\]

At the fixed state its first variation is
\(\sum_a A_a\cdot\delta a_a\), with a remainder bounded by a constant times
\(\sum_a|\delta a_a|^2\) for sufficiently small changes.

For a measurable E contained in the fundamental half F, replace w on E by a
fixed vector v and on -E by -v, leaving it unchanged elsewhere. Denote the new
state by wE. It is odd and lies in L2. Since b1 and tanh are odd,

\[
\delta a_a
=2\int_E b_1(\omega)
 [\tanh(v\cdot u_a)-\tanh(w(\omega)\cdot u_a)]\,dP_1.
\]

Boundedness of b1 gives \(|\delta a_a|\le C P_1(E)\), uniformly in v.
For

\[
P_b(v)=\sum_a (A_a\cdot b)\tanh(v\cdot u_a),
\]

the corresponding loss difference is therefore

\[
\mathcal L(w_E,c,M)-\mathcal L(w,c,M)
=2\int_E[P_{b_1(\omega)}(v)-P_{b_1(\omega)}(w(\omega))],dP_1
+O(P_1(E)^2).
\tag{5}
\]

For each fixed v, local minimality implies the integrand in (5) is nonnegative
almost everywhere on F. Otherwise there would be a positive-measure subset
on which it is at most \(-\varepsilon\). Intersecting with \(|w|\le K\)
for some finite K leaves positive measure. Nonatomicity then supplies subsets
E of arbitrarily small positive measure within it. The L2 change is bounded by
\(2(K+|v|)^2P_1(E)\) in squared norm, whereas (5) is at most
\(-2\varepsilon P_1(E)+O(P_1(E)^2)<0\). This contradicts the local minimum.

Apply this argument to countably many rational v, discard the union of their
null sets, and use continuity in v. For almost every mark in F,

\[
P_{b_1(\omega)}(w(\omega))\le P_{b_1(\omega)}(v)
\quad\text{for all }v\in\mathbb R^d.
\]

The value w(omega) is finite almost surely. Lemma 1 forces every coefficient
\(A_a\cdot b_1(\omega)\) to vanish. Oddness extends this statement from F
to the entire population. Since the carrier covariance is positive definite,
\(A_a=0\) for all a. Positive data weights give (4).

The small sets E can depend on the desired neighborhood. This is a local
minimum argument, not yet a fixed-direction Taylor argument.

## 4. A readout direction can preserve all outputs and change a derivative

**Lemma 3.** For arbitrary finite \(z_1,\ldots,z_m\in\mathbb R^d\), any
chosen \(z_*\) among them, and any nonzero \(v\in\mathbb R^d\), there is
a bounded odd readout k such that

\[
T_k(z_a)=0\quad\text{for every }a,
\qquad v\cdot\nabla T_k(z_*)>0.
\tag{6}
\]

Let H be the finite-dimensional span in \(L^2(\Omega_2)\) of
\(b\mapsto\tanh(b\cdot z_a)\), evaluated at b2. Set

\[
D(b)=(b\cdot v)\operatorname{sech}^2(b\cdot z_*).
\]

It suffices to prove \(D(b_2)\notin H\). Indeed, for the orthogonal
projection PH onto H, take \(k=D(b_2)-P_HD(b_2)\). It is bounded and odd,
is orthogonal to every retained upper activation, and satisfies

\[
v\cdot\nabla T_k(z_*)=E_2[kD(b_2)]=\|k\|_{L^2}^2>0.
\]

Suppose instead that D lies in H. The resulting equality of real-analytic
functions of b holds almost everywhere on the open cube with positive b2
density. Continuity makes it hold on the cube, and the real-analytic identity
theorem extends it to all of \(\mathbb R^d\). Zero z's can be omitted, and
equal or opposite nonzero z's can be combined into a single representative.

If \(z_*=0\), D is the nonzero unbounded linear function b.v, whereas any
finite sum of tanh ridges is bounded, a contradiction.

If \(z_*\ne0\), choose e outside the finite union of hyperplanes that would
make e.v zero, any e.zj zero, or two distinct representative slopes equal in
absolute value. On b=te, absorb slope signs into coefficients. The claimed
identity becomes

\[
t\beta\operatorname{sech}^2(\alpha_*t)
=\sum_j q_j\tanh(\alpha_jt),
\quad\beta\ne0,\quad\alpha_*,\alpha_j>0,
\]

with the \(\alpha_j\)'s distinct. Sending t to infinity yields
\(\sum_jq_j=0\). If the smallest remaining slope is less than alpha*,
multiply the identity, after cancelling the limiting constant, by the
exponential of twice that slope times t. The limit is zero on the left and
\(-2q_j\) on the right, because

\[
\tanh(\alpha t)-1=-2e^{-2\alpha t}+O(e^{-4\alpha t}).
\]

Thus that coefficient is zero. Remove such slopes one by one. For the
remaining slopes, all at least alpha*, multiply by
\(e^{2\alpha_*t}/t\). The left side tends to \(4\beta\), while the right
side tends to zero. This is a contradiction and proves (6).

## 5. No bad local minimum when M is nonzero

Suppose the state is a local minimum with \(r_*\ne0\) and \(M\ne0\).
Choose \(x\in\mathbb R^{2d}\) with \(v=Mx\ne0\), and apply Lemma 3 to
zstar and v, obtaining k.

For every sufficiently small real epsilon, replacing c by c+epsilon k leaves
all predictions and the loss exactly unchanged. These nearby equal-loss
states are also local minima: a sufficiently small ball around each lies
inside the original local-minimum neighborhood.

Apply (4) at c and at c+epsilon k, and subtract. Since the residuals and z's
are unchanged, \(\varepsilon\ne0\) and \(r_*\ne0\) give

\[
M^T\nabla T_k(z_*)=0.
\]

Taking its scalar product with x contradicts
\(v\cdot\nabla T_k(z_*)>0\). Thus every local minimum with nonzero M has
zero residual at every sample.

## 6. The zero-matrix case

At M=0, every prediction is zero independently of w,c. If the labels are all
zero there is no positive loss. Otherwise put

\[
R(v)=\sum_a\mu_a y_a\tanh(v\cdot u_a),\qquad
S(w)=\sum_a\mu_a y_a a_a(w)=E_1[b_1R(w)].
\]

R is nonconstant by Lemma 1 and its linear-independence consequence.

Arbitrarily near any w there is an odd wprime with \(S(w')\ne0\). If S(w)
is already nonzero, no change is needed. If it is zero, choose two finite
vectors v0,v1 with \(R(v_0)\ne R(v_1)\). On a positive-measure subset of F,
one of \(R(v_i)-R(w(\omega))\) is bounded away from zero; after subdividing,
its sign and the sign of the first component of b1 are fixed there. The latter
component is nonzero almost everywhere, so its magnitude can also be bounded
away from zero on a positive-measure subset. Intersect with a set where w is
bounded. A paired replacement by vi on an arbitrarily small positive-measure
subset changes the first component of S by a nonzero integral and costs
arbitrarily little in L2. This proves the claim.

Similarly, arbitrarily near any c is an odd cprime with
\(\gamma=E_2[c'b_2]\ne0\). If needed add a small nonzero multiple of
\(b_2\cdot v\); the positive definite b2 covariance ensures a nonzero change
of gamma.

If the original M=0 state were a positive-loss local minimum, choose such
wprime,cprime sufficiently near it. With M still zero, its loss is identical,
so this new state is itself a local minimum. But the directional derivative
in a matrix direction N is

\[
D_M\mathcal L[N]
=-2\gamma^T N S(w').
\]

Taking \(N=\gamma S(w')^T\) makes this equal to
\(-2|\gamma|^2|S(w')|^2<0\), a contradiction. This completes the theorem.

## 7. Why the stated straight-line conjecture is still open here

The theorem is strictly weaker than the user's condition concerning leading
coefficients along every straight line. For example, the everywhere
nonnegative analytic sum of squares

\[
F(x,y)=(1-x^6)^2+(y-x^2)^2
\]

has an equilibrium at the origin and \(F(0,0)=1\). Along
\((x,y)=t(a,b)\), every nonzero direction has positive even leading loss
change: it is \(b^2t^2\) when b is nonzero, and \(a^4t^4\) when b=0.
Nevertheless \(F(x,x^2)=(1-x^6)^2<1\) for sufficiently small nonzero x.
This is a logical separator, not a p=1 counterexample.

For the population model, the unresolved obligation is to replace the
neighborhood-dependent rare-mark replacements and equal-loss readout moves
by **one fixed admissible state direction** whose loss has a negative first
nonzero coefficient of finite order (or to construct an actual canonical
counterexample). Lemma 2 uses finite changes of w on shrinking sets, so its
proof does not supply that bridge. The fact that the loss has a smooth finite
readout map does not make it analytic along every L2 lower-weight direction:
higher directional derivatives can require higher moments of that direction.
Bounded lower directions avoid this particular integrability issue, but the
single-direction construction remains absent.

The theorem concerns arbitrary supplied states in the odd canonical carrier
space. It establishes no approach to, avoidance of, or escape time from any
particular equilibrium under the prescribed initialized dynamics.

## Self-audit and exact scope

- The proof preserves the frozen joint lower carriers and independent upper
  population. It uses the full matrix M and its ordinary transpose.
- All replacements preserve oddness and have finite L2 norm. No atom is added,
  no population measure is changed, and no finite-width surrogate is used.
- The Gaussian-mixture argument and the upper ridge-derivative independence
  argument are proved above; no specialized external theorem is assumed.
- Nonatomicity is used only to choose arbitrarily small mark sets. Finite
  quadrature populations do not satisfy this hypothesis, so the theorem is
  not a finite-population statement.
- The equal input norms are essential to the supplied proof of Lemma 1.
  Pairwise nonparallel/nonantiparallel inputs exclude the exact ridge
  dependencies that would defeat it.
- At M=0 the proof supplies nearby flat moves followed by a first-order
  matrix descent. At nonzero M it rules out a local-minimum neighborhood by
  contradiction. Neither argument has been promoted to a straight-line
  leading-coefficient claim.
- No experiment was performed. Source facts, parity, signs, factors in the
  variations, zero-M and zero-label cases, the paired-set remainder, and the
  ridge asymptotics were checked directly against the displayed formulas.
