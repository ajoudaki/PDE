# Affine-tail traversal: an integrated top-response estimate

Analytic sidecar, 2026-09-06. No numerical experiments, external theorem
imports, other agents, or changes to other files.

**Result.** For the exact two-sample top subsystem with a frozen positive
definite lower feature Gram, the full three-variable variational flow has
an integrated bound with a curvature cost depending on endpoint primal
values. For an exchange-symmetric Gram and opposite labels, that cost is
uniform over every zero-readout initial preactivation pair and every
feature-time interval: it is at most a power of \(3/2\). A small nonzero
initial readout contributes an explicit exponential in its absolute value.
The requested convex comparator \(\phi_c(z)=z+\log(1+e^z)\) closes an
especially direct positive route: its expanding curvature integrates to
at most \(\log2/[g-\max(h,0)]\). The moving-Gram version and the exact
signed lower-forcing error are proved in Section 7.
The remaining exponential in elapsed feature time is unavoidable even on
nonstationary trajectories with uniformly bounded primal states. These
are frozen-subsystem results, not a construction of the full trained
canonical population flow.

## 1. Contract and provenance

The mathematical inputs read in full were `CONTRACT_AND_LEDGER.md`,
`AFFINE_TAIL_ACTIVATION_ROUTE.md`, and `EXACT_TWO_SAMPLE_REDUCTION.md`
in this directory. The requested procedural files were read directly:
`/home/amir/.codex/skills/solve-math-rigorously/SKILL.md` and
`/home/amir/.codex/skills/investigate-conjectures/SKILL.md`, together with
the latter's `research-contract.md`, `evidence-ledger.md`, and
`adversarial-audit.md` references. No review files were needed.

The original activation, used in Sections 1--6, is fixed as

\[
 \phi(z)=1+\chi(z),\qquad \chi(z)=z+\tfrac12\tanh z,
 \quad p(z)=\phi'(z),\quad k=\tfrac32.
\]

Thus \(1\le p\le k\), \(p\) is even and decreases with \(|z|\), and
\(\phi''(z)=-\operatorname{sech}^2z\tanh z\). Write
\(M=\sup|\phi''|=2/(3\sqrt3)\); substituting \(r=|\tanh z|\)
reduces this maximum to that of \(r(1-r^2)\) on \([0,1]\).

At finite width, retain the contract's rescaled readout

\[
 w=W_i^{(4)},\qquad z_a=z^{(3)}_{a,i},\qquad
 G_{ab}=n^{-1}\langle h_a^{(2)},h_b^{(2)}\rangle.
\]

Freeze the two lower feature vectors, not either sample. The resulting
subsystem is the exact restriction of label-mode feature ascent
\(\theta'=\operatorname{grad}[(y_1f_1+y_2f_2)/2]\) to the top two
parameter blocks. All displayed neuron coordinates are unnormalized.
Feature time is denoted \(s\). For canonical physical flow this label-mode
clock requires the symmetry/existence premises in the reduction input;
it is not a pathwise identity for the finite Gaussian physical flow.

Conditionally on the frozen initial layer-two features, the actual fresh
Gaussian third-layer row gives \(z(0)\sim N(0,G)\), and independently
\(w(0)\sim N(0,n^{-2})\). We do not replace this finite readout by zero.
The intended population initial readout is zero. Its initial lower Gram
is exchange symmetric and positive definite, including at input
correlation \(-1\), as derived in the affine-tail input. A realized finite
empirical Gram need not be exchange symmetric. The general-Gram estimate
below covers it whenever it is positive definite; constants deteriorate
as its smallest eigenvalue tends to zero.

The observables tested here are the complete neuronwise tangent vector
and its propagator. This is not merely a bound on a trace, a selected
Hessian eigenvalue, or the instantaneous backward-query derivative.
No width limit, approximation hierarchy, or full-flow uniqueness is
asserted. Everything below is elementary finite-dimensional analysis.

## 2. Exact primal and variational equations, with both labels

Let \(G=\begin{pmatrix}g_{11}&g_{12}\\g_{12}&g_{22}\end{pmatrix}>0\)
be arbitrary and \(y_1,y_2\in\{-1,1\}\). Define

\[
 F(z)=\tfrac12\sum_{a=1}^2y_a\phi(z_a),\quad
 a(z)=\tfrac12(y_1p(z_1),y_2p(z_2))^T,\quad
 B(z)=\tfrac12\operatorname{diag}(y_1\phi''(z_1),y_2\phi''(z_2)).
 \tag{1}
\]

Here \(a=\nabla F\) and \(B=D a\). The exact three-variable system is

\[
 w'=F(z),\qquad z'=wGa(z).                                      \tag{2}
\]

Indeed the feature update of the third-layer row is
\(\tfrac1{2n}\sum_a y_awp(z_a)(h_a^{(2)})^T\). Multiplication by
each \(h_b^{(2)}\) proves (2), including the off-diagonal Gram terms.
For a variation \(u=\delta w\), \(v_a=\delta z_a\) at fixed \(G\),

\[
 \begin{aligned}
 u'&=\tfrac12(y_1p_1v_1+y_2p_2v_2),\\
 v_1'&=\tfrac12(g_{11}y_1p_1+g_{12}y_2p_2)u
       +\tfrac w2(g_{11}y_1\phi''_1v_1+g_{12}y_2\phi''_2v_2),\\
 v_2'&=\tfrac12(g_{12}y_1p_1+g_{22}y_2p_2)u
       +\tfrac w2(g_{12}y_1\phi''_1v_1+g_{22}y_2\phi''_2v_2).
 \end{aligned}                                                  \tag{3}
\]

In vector form, \(u'=a^Tv, v'=Ga\,u+wGBv\). Both cross-sample
couplings remain. The three-dimensional metric inherited from the
top parameter blocks, after removing the common factor \(1/n\), is

\[
 N^2=u^2+v^TG^{-1}v.                                            \tag{4}
\]

The orthogonal part of a row variation outside the span of the two
lower feature vectors is constant and does not affect these coordinates.

Write \(\lambda=\lambda_{\min}(G)>0\),
\(\Lambda=\lambda_{\max}(G)\), and

\[
 A=a^TGa,\qquad \alpha=\sqrt{\lambda/2},\qquad
 K=k\sqrt{\Lambda/2}.
\]

Because \(1/2\le |a|^2\le k^2/2\),

\[
 \alpha^2\le A\le K^2,\qquad F'=Aw,\qquad w''=Aw,\qquad
 (wF)'=F^2+Aw^2.                                                \tag{5}
\]

The field has at most linear growth: \(|F(z)|\le1+k|z|/\sqrt2\)
and \(|wGa|\le\Lambda k|w|/\sqrt2\). Differentiating

\(1+w^2+|z|^2\) therefore bounds its derivative by a constant times
itself; multiplication by the corresponding decreasing exponential
gives a finite bound on every finite interval. Local existence can be
obtained by contraction of the integral equation on a small ball: the
smooth field has finite local Lipschitz and magnitude bounds there.
The same bounds make the path Cauchy at a finite maximal endpoint and
permit continuation. Hence (2) is global in finite-dimensional feature
time. Differentiating its integral equation gives (3): bounded second
derivatives on each compact trajectory neighborhood control the Taylor
remainder, and the integrating-factor inequality controls the remainder
after division by the initial increment. Thus these are actual flow
derivatives, not independently chosen Hessian states.

## 3. Integrated energy for every positive definite Gram

Define the signed expanding curvature coefficient

\[
 \beta(s)=\max\{0,w(s)B_{11}(z(s)),w(s)B_{22}(z(s))\}.            \tag{6}
\]

Direct differentiation of the full metric, without taking a trace, gives

\[
 (N^2)'=4u\,a^Tv+2w\,v^TBv.
 \tag{7}
\]

Since \(|a^Tv|\le\sqrt A\sqrt{v^TG^{-1}v}\) and
\(|v|^2\le\Lambda v^TG^{-1}v\),

\[
 (N^2)'\le2(\sqrt A+\Lambda\beta)N^2.
\]

Consequently the following integrating-factor estimate holds on every
interval \([r,t]\):

\[
 N(t)\le N(r)\exp\left\{\int_r^t\sqrt{A(s)}\,ds
                              +\Lambda\int_r^t\beta(s)\,ds\right\}.
 \tag{8}
\]

For a zero tangent vector the claim follows by uniqueness. Otherwise
multiply (7)'s inequality by the exponential with twice the negative
integral and differentiate. This proves (8) without any diagonalization
or assumption that curvature at different times commutes.

There is a useful endpoint control for the second integral. Unless

\(w=F=0\) identically, (5) makes \(wF\) strictly increasing. A zero of

\(w\) can occur at most once: there \(F\ne0\), \(wF=0\), and the
strictly increasing product cannot return to zero. Because \(F'=Aw\),
either \(F\) is monotone, or it has just one extremum, attained at that
zero of \(w\). In the second case \(F\) keeps its sign, and the extremum
is a minimum of \(|F|\). In both cases its total variation satisfies

\[
 \operatorname{TV}_{[r,t]}F\le |F(r)|+|F(t)|.
\]

Thus, also covering the stationary case,

\[
 \int_r^t|w|\,ds
 \le\frac{|F(r)|+|F(t)|}{\alpha^2},\qquad
 \int_r^t\beta\,ds
 \le\frac M\lambda\bigl(|F(r)|+|F(t)|\bigr).                    \tag{9}
\]

Combining (8) and (9) proves the general-Gram integrated estimate

\[
 N(t)\le
 \exp\left\{K(t-r)+M\frac\Lambda\lambda
                         (|F(r)|+|F(t)|)\right\}N(r).          \tag{10}
\]

On an interval with \(wF\ge0\), replace the sum of endpoint absolute
values by \(|F(t)|-|F(r)|\). These bounds hold for all four label choices
and all initial states, in particular for the actual conditional
Gaussian law. They integrate the large readout multiplier through the
identity \(F'=Aw\); they do not bound its pointwise maximum.

For clarity, the endpoint dependence is controlled by primal norms,
not hidden trajectory data. For opposite labels,
\(|F|\le k|z_1-z_2|/2\). Moreover, differentiating
\(Q=K^2w^2+F^2\) and using (5) gives

\[
 Q'=2(K^2+A)wF\le2KQ,\qquad
 |F(t)|\le e^{K(t-r)}\sqrt{K^2w(r)^2+F(r)^2}.                  \tag{11}
\]

For a fixed Gram and fixed horizon, (10) therefore has at most an
exponential of a linear function of the initial Gaussian magnitudes.
It has every finite polynomial moment under the stated conditional
Gaussian initialization: the scalar inequality
\(c|x|\le\varepsilon x^2+c^2/(4\varepsilon)\), with sufficiently
small positive \(\varepsilon\), makes the Gaussian integral finite.
This is not a uniform maximum bound over all Gaussian neurons.

The corresponding exact approximate-balance identity is also available.
Put \(D=w^2-z^TG^{-1}z\) and \(E(z)=\phi(z)-zp(z)\). Then

\[
 D'=w\sum_a y_aE(z_a).                                        \tag{12}
\]

Here \(E(z)=1+\tfrac12\psi(z)\), where
\(\psi(z)=\tanh z-z\operatorname{sech}^2z\).
Its derivative \(2z\operatorname{sech}^2z\tanh z\ge0\) and its
limits \(\pm1\) show \(|\psi|\le1\). For opposite labels the
intercept cancels, so \(|D'|\le|w|\), and

\[
 |D(t)-D(r)|\le\frac2\lambda(|F(r)|+|F(t)|).                   \tag{13}
\]

This balance is a primal companion to (8), not a replacement for its
directional variational energy. Neither its sign nor its trace is used
to infer response stability.

## 4. A uniform signed-curvature budget in the symmetric contrast mode

Now suppose \(y=(1,-1)\) and

\[
 G=\begin{pmatrix}g&h\\h&g\end{pmatrix},\qquad g>|h|.
 \tag{14}
\]

The conclusion is valid with nonzero off-diagonal coupling of either
sign. Set \(m=(z_1+z_2)/2\), \(d=(z_1-z_2)/2\). Equations (2) give

\[
 m'=\tfrac{w(g+h)}4(p_1-p_2),\qquad
 d'=\tfrac{w(g-h)}4(p_1+p_2),\qquad
 F=\tfrac12(\chi(z_1)-\chi(z_2)).                              \tag{15}
\]

In particular \(\operatorname{sign}F=\operatorname{sign}d\).
On a nonstationary interval with \(wF\ge0\), a simultaneous sample
exchange and readout sign change lets us take \(w\ge0,d\ge0\).
This transformation preserves (14), the metric, and \(\beta\).
From (5), this aligned regime persists. Since

\(z_1^2-z_2^2=4md\) and \(p\) decreases with absolute argument,

\(m(p_1-p_2)\le0\). The plane \(m=0\) is invariant; uniqueness and
(15) imply that \(m\) keeps its sign and \(|m|\) is nonincreasing.

If \(m\ge0\), then \(z_1\ge0\), \(p_1\le p_2\), and sample one's
curvature term is nonpositive. Only sample two can expand, when
\(z_2>0\). Throughout this case

\[
 z_2'=-\tfrac w2(gp_2-hp_1),\qquad
 gp_2-hp_1\ge\lambda p_2,\qquad \lambda=g-|h|.                 \tag{16}
\]

For \(h\ge0\) use \(p_1\le p_2\); for \(h<0\) use
\(gp_2+|h|p_1\ge gp_2\ge\lambda p_2\).
The expanding coordinate thus moves monotonically through its positive
curved region. Define

\[
 L(s)=\log p(\max\{z_2(s),0\}).
\]

This is continuously differentiable, including at \(z_2=0\), because
\(p'(0)=0\). On \(z_2>0\), (16) implies

\[
 L'=\frac{-\phi''(z_2)}{p_2}\frac w2(gp_2-hp_1)
       \ge\lambda\beta.
\]

On \(z_2\le0\), both \(\beta\) and \(L'\) are zero. Since
\(0\le L\le\log k\), integration proves the budget below. If
\(m\le0\), then \(z_2\le0\), \(p_1\ge p_2\), and only sample one
can expand, when \(z_1<0\). The inequality
\(gp_1-hp_2\ge\lambda p_1\) follows by the same two sign cases for
\(h\). Use \(L=\log p(\min\{z_1,0\})\), whose derivative is again
at least \(\lambda\beta\). The case \(m=0\) has no positive curvature.
We have proved, for arbitrarily long aligned intervals,

\[
 \int_r^t\beta(s)\,ds\le\frac{\log k}{\lambda}.                \tag{17}
\]

This is a signed estimate: contraction from a coordinate that remains
in a curved region need not have a finite absolute integral. The
coordinate contributing expansion must traverse the region. No change
of variables divides by a vanishing coordinate velocity.

To include the exact nonzero Gaussian readout, there may be an initial
interval with \(wF<0\). On this interval let \(q=|w|\), \(j=|F|\).
They satisfy

\[
 q'=-j,\qquad j'=-Aq.
\]

For any terminal time \(b\) still in this interval,
\(j(s)\ge\alpha^2\int_s^b q(v)\,dv\). Hence

\[
 q(r)^2-q(b)^2
   =2\int_r^b q(s)j(s)\,ds
   \ge\alpha^2\left(\int_r^b q(s)\,ds\right)^2.
\]

The last equality for the double integral follows by splitting the
square \([r,b]^2\) into its two triangles. Thus the entire initial
unaligned portion, even if infinite, has
\(\int|w|\le|w(r)|/\alpha\). Once it ends, (5) permits only the
aligned regime. Combining this fact, \(\beta\le M|w|/2\), and (17),

\[
 \int_r^t\beta\,ds\le
       \frac{M|w(r)|}{2\alpha}+\frac{\log k}{\lambda}.           \tag{18}
\]

Inserting this into the full energy estimate proves the main theorem:

\[
 N(t)\le k^{\Lambda/\lambda}
    \exp\left\{K(t-r)+\frac{\Lambda M}{2\alpha}|w(r)|\right\}N(r).
 \tag{19}
\]

The term involving \(w(r)\) may be omitted whenever \(w(r)F(r)\ge0\).
In particular, from population zero readout it vanishes for every
initial \(z(0)\), and it stays absent at every reached-state restart.
The exceptional state \(w=F=0\) is stationary with \(\beta=0\) and
also satisfies the theorem. Equation (19) bounds the full \(3\times3\)
propagator in (4), including arbitrary readout and preactivation tangent
directions. It is uniform over all initial Gaussian preactivations in
the symmetric frozen system. It does not claim that an empirical
finite-width Gram is symmetric or that a pointwise curvature multiplier
is uniformly bounded.

One can express the affine growth using endpoint ratios. On a
nonstationary aligned interval set \(R=|w|+|F|/\alpha>0\). Then
\(R'=|F|+A|w|/\alpha\ge\alpha R\), so (19) implies

\[
 N(t)\le k^{\Lambda/\lambda}
       \left(\frac{R(t)}{R(r)}\right)^{K/\alpha}N(r).           \tag{20}
\]

The denominator is an active initial amplitude, not just an upper bound
on the initial primal norm. It cannot be dropped, as the next exact
trajectory test shows. For Gaussian data near zero contrast, the
elapsed-time form (19) is the useful uniform statement.

## 5. Why a time-independent bound from primal upper bounds is false

Fix (14), write \(\mu=g-h>0\), and start the actual frozen trajectory at

\[
 w(0)=0,\qquad z_1(0)=\varepsilon,\qquad
 z_2(0)=-\varepsilon,\qquad 0<\varepsilon<D_0,
\]

where \(D_0>0\) is fixed. This is a nonstationary orbit in the invariant
plane \(m=0\), not an arbitrary Hessian state. Its equations reduce to

\[
 w'=\chi(d),\qquad d'=\tfrac\mu2 w p(d),\qquad
 w^2=\frac4\mu\int_\varepsilon^d\frac{\chi(v)}{p(v)}\,dv.       \tag{21}
\]

The last identity follows by differentiating \(w^2\) with respect to

\(d\) where \(w>0\), and then by continuity at the initial point.
The first time \(T_\varepsilon\) at which \(d=D_0\) is finite: until
then \(w'\ge\chi(\varepsilon)>0\) and
\(d'\ge\mu w/2\). Throughout \([0,T_\varepsilon]\), (21) bounds

\[
 |z|\le\sqrt2D_0,\qquad
 0\le w^2\le\frac4\mu\int_0^{D_0}\frac{\chi(v)}{p(v)}\,dv.
 \tag{22}
\]

These bounds are independent of \(\varepsilon\). Also (11) gives

\(\chi(D_0)\le e^{KT_\varepsilon}\chi(\varepsilon)\), so

\(T_\varepsilon\to\infty\).

Let \(V\) be the full vector field in (2) and \(\Phi_s\) its flow.
The identity

\[
 D\Phi_s(X_0)V(X_0)=V(\Phi_s(X_0))                              \tag{23}
\]

follows directly because both sides solve (3) with initial value

\(V(X_0)\). Here \(V(X_0)=\chi(\varepsilon)(1,0,0)\). Thus the
unit initial readout variation has terminal readout response

\[
 \bigl[D\Phi_{T_\varepsilon}(X_0)(1,0,0)\bigr]_w
       =\frac{\chi(D_0)}{\chi(\varepsilon)}
       \ge\frac{D_0}{k\varepsilon}\longrightarrow\infty.       \tag{24}
\]

Consequently no finite function of fixed Gram eigenvalue bounds and
upper bounds on initial, terminal, or supremum primal norms alone can
bound the propagator over all durations. This refutes precisely that
time-independent strengthening, not (10), (19), or (20). Indeed on this
orbit all signed curvature is nonpositive: the obstruction is affine
growth during a long escape from small contrast, not failed traversal.

The exact curve \(m=0\) has Gaussian probability zero, but the obstruction
is not being asserted only on that curve. For each fixed \(\varepsilon\)
and its fixed \(T_\varepsilon\), continuous dependence of the flow and
its derivative gives an open neighborhood of the initial state with,
for example, twice the bound in (22) plus one and at least half the
amplification in (24). Such a neighborhood has positive conditional
probability under the nondegenerate finite Gaussian \((w,z)\) law; its
intersection with \(w=0\) has positive probability under the population
Gaussian \(z\) law. No uniform lower bound on these probabilities or
failure at any fixed bounded horizon is claimed.
These probabilities refer to the fixed frozen Gram's top-initialization
law; they do not assert that a finite empirical Gram is exactly
exchange symmetric with positive probability.

## 6. What survives a moving Gram and lower-layer forcing

For a prescribed \(C^1\) positive definite \(G(s)\), with no extra
preactivation forcing, equations (2), (3), and (5) remain exact with
the current \(G\); the variations in (3) hold \(G(s)\) fixed. Suppose

\(\lambda_*I\le G(s)\le\Lambda_*I\). In (4), use the current inverse
Gram and define

\[
 \nu(s)=\|G(s)^{-1/2}G'(s)G(s)^{-1/2}\|_{\rm op}.
\]

The energy has the additional exact term

\[
 (N^2)'=4ua^Tv+2wv^TBv
       -v^TG^{-1}G'G^{-1}v.                                  \tag{25}
\]

Its contribution to the exponent for \(N\) is at most

\(\tfrac12\int\nu\). The general endpoint estimate (9) survives
with \(\lambda_*\), because it used only \(F'=Aw\), the positive
lower bound for \(A\), and monotonicity of \(wF\).
If \(G(s)\) is exchange symmetric at every time, the coordinate proof
(15)--(18) also survives, with \(\lambda_*\),
\(\alpha_*=\sqrt{\lambda_*/2}\), and \(\Lambda_*\). Thus (19) holds
with these uniform constants and the additional metric-variation factor

\(\exp\{\tfrac12\int_r^t\nu(s)\,ds\}\). Mere eigenvalue bounds
do not bound this factor; the statement requires its displayed integral.

For the full trained label-mode feature flow, the exact top equations
instead have

\[
 w'=F(z),\qquad z'=wG(s)a(z)+\ell(s),\qquad
 \ell_{a,i}=(W^{(3)}(h_a^{(2)})')_i.                           \tag{26}
\]

On a differentiable full variation they become

\[
 u'=a^Tv,\qquad
 v'=Ga\,u+wGBv+\xi,\qquad
 \xi=w(\delta G)a+\delta\ell.                                 \tag{27}
\]

Here \(\delta G\) and \(\delta\ell\) are coupled lower-layer responses,
not independent bounded data. In particular,

\[
 F'=Aw+a^T\ell,\qquad
 (wF)'=F^2+Aw^2+w\,a^T\ell,                                  \tag{28}
\]

so the monotonicity, the one-turn argument, and the aligned-sector
invariance used above are no longer automatic. The exact balance is

\[
 D'=w\sum_a y_aE(z_a)
     +z^TG^{-1}G'G^{-1}z-2z^TG^{-1}\ell.                       \tag{29}
\]

The full energy identity (25) survives with \(+2v^TG^{-1}\xi\).
More generally, with additional readout tangent forcing \(\eta\), put

\(J=(\eta^2+\xi^TG^{-1}\xi)^{1/2}\). The same calculation gives

\[
 N(t)\le e^{H(r,t)}N(r)
             +\int_r^t e^{H(s,t)}J(s)\,ds,\quad
 H(s,t)=\int_s^t(\sqrt A+\Lambda_*\beta+\nu/2)\,du.             \tag{30}
\]

One obtains this even through \(N=0\) by applying the differential
inequality to \((N^2+\epsilon^2)^{1/2}\) and letting
\(\epsilon\downarrow0\). Equation (30) is conditional on the actual
curvature integral; it does not silently reuse (17) for a forced path.

A precise conditional traversal remnant is possible. If a forced path
with an exchange-symmetric Gram stays in \(w\ge0,z_1\ge z_2,m\ge0\),
the same \(L=\log p(\max\{z_2,0\})\) satisfies

\[
 \lambda_*\int_r^t\beta\,ds
 \le\log k+
   \int_r^t\mathbf1_{\{z_2>0\}}
       \frac{|\phi''(z_2)|}{p_2}|\ell_2|\,ds.                 \tag{31}
\]

Indeed its derivative equals the unforced expression plus

\(\mathbf1_{\{z_2>0\}}(\phi''(z_2)/p_2)\ell_2\), and the
unforced expression is at least \(\lambda_*\beta\).
There is the corresponding statement with \(z_1<0,\ell_1\) in the
sector \(m\le0\). Thus a controlled forcing budget and preserved sectors
would suffice; neither follows here from an ordinary primal norm bound.

Finally, finite physical GF has the two separate residual coefficients
\(c_a=-2(f_a-y_a)\), not the fixed coefficients \(y_a/2\).
Its top field is \(\dot w=\sum_a c_a\phi(z_a)\) and
\(\dot z=wG(c_ap_a)_{a=1,2}+\ell\); its variation also includes
\(\delta c_a\). No finite physical-time result follows by assigning
that flow the population feature clock.

## 7. Positive convex comparator: a direct log-derivative budget

The user's added discriminator is

\[
 \phi_c(z)=z+\log(1+e^z)+b_0,
 \quad p_c(z)=1+\sigma(z),\quad
 \phi_c''(z)=\sigma(z)(1-\sigma(z)),\quad
 \sigma(z)=\frac{e^z}{1+e^z},                                  \tag{32}
\]

where \(b_0\) is any fixed constant, including zero. Then
\(1<p_c<2\), \(0<\phi_c''\le1/4\), and
\(0<\log p_c<\log2\). All three-variable equations (1)--(8)
remain valid with this activation; in this section \(k_c=2\),
\(M_c=1/4\), and the upper rate in (5)--(8) is
\(K_c=\sqrt{2\Lambda}\). The intercept \(b_0\) cancels from opposite-label

\(F=(\phi_c(z_1)-\phi_c(z_2))/2\).

Take \(y=(1,-1)\) and first a constant exchange-symmetric Gram (14).
Starting from zero readout, if \(d(0)>0\), then \(F(0)>0\) by strict
monotonicity. Equations (5) imply \(w>0,F>0\) for positive time, while

\[
 d'=\frac{w(g-h)}4(p_{c,1}+p_{c,2})\ge0.
\]

Thus \(z_1\ge z_2\) and convexity gives \(p_{c,1}\ge p_{c,2}\).
There is no required condition on the mean preactivation. Define

\[
 c=g-\max(h,0)=\min(g,g-h)>0.
\]

If \(h\ge0\), then \(gp_{c,1}-hp_{c,2}\ge(g-h)p_{c,1}\).
If \(h<0\), then \(gp_{c,1}-hp_{c,2}\ge gp_{c,1}\). Hence

\[
 z_1'=\frac w2(gp_{c,1}-hp_{c,2})\ge\frac{cw p_{c,1}}2.
 \tag{33}
\]

The signed curvature matrix \(wB\) has its only positive entry in
sample one, so \(\beta=w\phi_c''(z_1)/2\). Differentiation gives
the exact identity and its consequence

\[
 \begin{split}
 \frac{d}{ds}\log p_c(z_1)
   &=\left(g-h\frac{p_{c,2}}{p_{c,1}}\right)\beta
     \ge c\beta,\\
 \int_r^t\beta\,ds
   &\le\frac1c\log\frac{p_c(z_1(t))}{p_c(z_1(r))}
     \le\frac{\log2}{c}.
 \end{split}                                                   \tag{34}
\]

Equivalently, the integral of \(w\phi_c''(z_1)\) is bounded by

\(2\log2/c\), with the factor two exactly as proposed. Sample two
has nonpositive signed curvature and is retained in the full energy
(7). When \(d(0)<0\), exchange the two samples and negate \(w\);
then sample two is the larger preactivation and carries the positive
curvature. When \(d(0)=0,w(0)=0\), the primal path is stationary and
the curvature budget is zero. This proves all cases of zero readout,
without an initialization-tail exception.

For the full tangent vector, (8) and (34) yield

\[
 N(t)\le 2^{\Lambda/c}\exp\{\sqrt{2\Lambda}(t-r)\}N(r).
 \tag{35}
\]

This holds on every interval of an aligned trajectory, including every
restart from a zero-readout orbit. It controls arbitrary tangent
directions, not just variations preserving the initial symmetry or
ordering. For an arbitrary nonzero initial readout, the unaligned
budget proved before (18) uses only (5), so it applies unchanged.
Consequently (35) acquires at most the factor

\(\exp\{\Lambda|w(r)|/(8\alpha)\}\),
\(\alpha=\sqrt{\lambda/2}\). This includes the exact small Gaussian
readout without replacing it by zero.

There is also a bounded Euler defect for this comparator. With
\(q=\sigma(z)\), substitution of \(z=\log(q/(1-q))\) gives

\[
 \phi_c(z)-zp_c(z)-b_0
   =-q\log q-(1-q)\log(1-q)\in[0,\log2].                     \tag{36}
\]

To check the range, its derivative with respect to \(q\) is

\(\log((1-q)/q)\); it increases to \(q=1/2\), then decreases,
and has zero limits at the endpoints. Thus (12) implies

\(|D'|\le(\log2)|w|\) for opposite labels. Approximate balance is
compatible with the positive traversal route; (34), rather than that
balance alone, controls amplification.

**Prescribed moving Gram.** Let

\(G(s)=\begin{pmatrix}g(s)&h(s)\\h(s)&g(s)\end{pmatrix}\)
be \(C^1\), with

\[
 \lambda_* I\le G(s)\le\Lambda_*I,\qquad
 c(s)=g(s)-\max(h(s),0)\ge c_*>0.
\]

One may always take \(c_*=\lambda_*\), though the displayed value
can be better. With no lower forcing, (5), the order preservation, and
(33) remain valid pointwise in time. The exact first line of (34) now
has the current \(g(s),h(s)\); hence

\[
 \int_r^t c(s)\beta(s)\,ds\le\log2,\qquad
 N(t)\le 2^{\Lambda_*/c_*}
   \exp\left\{\sqrt{2\Lambda_*}(t-r)
                    +\tfrac12\int_r^t\nu(s)\,ds\right\}N(r).
 \tag{37}
\]

This is for zero-readout or already aligned paths. The same nonzero
readout correction as above holds with \(\Lambda_*,\alpha_*\).
The metric term is exactly (25); no unproved bound on it is assumed.

**Exact error from additive lower forcing.** Now allow (26), with this
convex activation and a moving exchange-symmetric Gram. On any interval
where \(w\ge0,z_1\ge z_2\), let \(z_+=z_1,\ell_+=\ell_1\);
on an interval where \(w\le0,z_2\ge z_1\), let

\(z_+=z_2,\ell_+=\ell_2\). Let \(z_-\) be the other coordinate,
\(p_\pm=p_c(z_\pm)\), and \(q=|w|\). In either case

\[
 \beta=\frac q2\phi_c''(z_+),\qquad
 z_+'=\frac q2(gp_+-hp_-)+\ell_+.
\]

Therefore, with \(r_c(z)=\phi_c''(z)/p_c(z)\ge0\), the exact
integrated identity is

\[
 \int_r^t\left(g-h\frac{p_-}{p_+}\right)\beta\,ds
   =\log\frac{p_+(t)}{p_+(r)}
                         -\int_r^t r_c(z_+)\ell_+\,ds.        \tag{38}
\]

The coefficient on the left is at least \(c(s)\). Only forcing that
pushes the expanding coordinate backwards increases the bound. Writing

\((x)_-=\max(-x,0)\), define

\[
 \mathcal E_\ell(r,t)=\int_r^t r_c(z_+)(\ell_+)_-\,ds.
\]

Then (38) proves

\[
 \int_r^t\beta\,ds
       \le\frac{\log2+\mathcal E_\ell(r,t)}{c_*},\qquad
 \mathcal E_\ell(r,t)
       \le(3-2\sqrt2)\int_r^t(\ell_+)_-\,ds.                  \tag{39}
\]

For the last constant, write
\(r_c=q(1-q)/(1+q)\) with \(q=\sigma(z)\); its derivative has
numerator \(1-2q-q^2\), and its maximum at \(q=\sqrt2-1\) is

\(3-2\sqrt2\). Thus the forcing error is explicitly an integrated
backward displacement weighted by the log-derivative curvature.

The full forced tangent bound follows from (30). On an interval with
the stated maintained ordering and readout sign, every suffix has the
same property. Define

\[
 C(s,t)=2^{\Lambda_*/c_*}
 \exp\left\{\sqrt{2\Lambda_*}(t-s)
       +\frac{\Lambda_*}{c_*}\mathcal E_\ell(s,t)
       +\tfrac12\int_s^t\nu(u)\,du\right\}.
\]

Then, retaining the actual source
\(\xi=w(\delta G)a+\delta\ell\) and any readout tangent source,

\[
 N(t)\le C(r,t)N(r)+\int_r^t C(s,t)J(s)\,ds.                  \tag{40}
\]

The ordering/sign condition is substantive for a forced path. Its
exact failure terms are visible in

\[
 d'=\frac{w(g-h)}4(p_{c,1}+p_{c,2})
                  +\frac{\ell_1-\ell_2}{2},\qquad
 (wF)'=F^2+Aw^2+w\,a^T\ell.                                  \tag{41}
\]

If arbitrary forcing reverses the ordering relative to \(w\), the
expanding coordinate need not be the larger one, and the lower bound

\(g-hp_-/p_+\ge c(s)\) used in (38)--(39) is no longer established.
No bound on the number or cost of such unaligned excursions is supplied
here. In the canonical trained flow, controlling (41), the forcing
budget, Gram variation, and the tangent source remains the root's
continuation problem. Equations (34)--(40) are the completed positive
top-block mechanism and its exact conditional transfer formula.

## 8. Claim update and stopping point

| Claim | Status and exact scope |
|---|---|
| Full top variational integrating factor (8) and endpoint estimate (10) | Proved; any frozen positive definite two-sample Gram, both labels retained, any initial state |
| Uniform signed curvature budget (17)--(19) | Proved; exchange-symmetric frozen Gram, opposite labels; zero or nonzero initial readout as stated |
| Approximate balance (12)--(13) | Proved; companion primal identity, not a trace-to-response inference |
| Bound over all durations using only upper bounds on primal norms | Falsified; the explicit nonstationary trajectories (21)--(24), with positive-probability neighborhoods |
| Prescribed moving-Gram extension | Proved under the stated eigenvalue and metric-variation controls; symmetry needed for the uniform curvature budget |
| Convex strongly monotone comparator (34)--(37) | Proved; uniform signed curvature budget and full top propagator control, opposite labels, frozen or prescribed moving exchange-symmetric Gram |
| Convex comparator with additive lower forcing (38)--(40) | Exact identity and proved estimate on maintained aligned sectors; signed forcing cost, metric variation, and tangent sources displayed explicitly |
| Transfer to fully trained canonical Gaussian dynamics | Open; lower forcing, its tangent source, off-mode residuals, and population construction remain unbounded by this note |

The integrated-traversal entry left open by the earlier affine-tail note
is upgraded to a theorem for this frozen top mechanism. The convex
comparator also closes the user's added positive discriminator without
a restriction on the mean preactivation. The earlier note's previous
maximum-norm onset result is neither repeated nor contradicted. The
full two-label target, all-layer nontriviality, and GF/GD/population
identification remain unchanged. This sidecar stops at the integrated
estimate and its exact transfer limitations; no external audit is claimed.
