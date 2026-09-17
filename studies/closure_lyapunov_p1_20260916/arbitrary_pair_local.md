# Arbitrary-orientation pairs: exact initialization rank and a local theorem

Status: independent analytical continuation, frozen before sharing approach
details, 2026-09-16. This extends the author's `route_local.md`, which remains
unchanged. No other studies or agents' current approaches were consulted.
The canonical source scope and skills are the same as in that frozen route;
the present task permits this study's artifacts. No computation or numerical
quadrature was run.

**Result.** The exact canonical order-one initialized upper coefficient map
has the form `(Phi(u_1),Phi(u_2))`, where `Phi` is odd and strictly increasing.
The initialized readout Gram is therefore positive definite for every pair
of unit directions `u,v` with `v!=u` and `v!=-u`, in arbitrary orientation.
This removes the angular restriction from the earlier **small-label** theorem,
with explicit geometry-dependent Gaussian-integral constants. Antipodal
opposite-label pairs reduce to one constraint and also admit a small-label
theorem in every orientation. Coincident opposite-label inputs cannot fit.
No global unit-label conclusion is asserted here.

## 1. Exact initialized coefficient map

Keep the canonical ridge `eta=1/4096`, the exact Cholesky normalization,
and the full correlated mark laws. Write

\[
 v_0=E\tanh^2G,\quad
 \tau=E\tanh^2(\sqrt{v_0}G),\quad \alpha=1-\tau,
\]

where `G` is standard Gaussian. On each independent lower coordinate block,
let `g~N(0,1)`, `zeta~N(0,tau)` be independent and put

\[
 X=\tanh g,\quad P=\zeta+\alpha X,\quad Y=\tanh P,
 \quad r=E[XY],\quad \ell=E[Y^2],\quad \chi=E[1-Y^2].
\]

Thus `v_0,tau,alpha,chi,r>0`. The raw lower block Gram is
`B=[[v_0,r],[r,ell]]`. The exact raw contraction row for upper coordinate
`Z_i=tanh xi_i`, where `xi_i~N(0,v_0)`, is

\[
 (\alpha v_0,\ \alpha r+\tau\chi),
\]

as derived directly from the supplied core contraction in the frozen route.
In particular its reverse-response term has not been dropped.

Define the two ridge regression coefficients `a,b` by

\[
 (a,b)=(\alpha v_0,\alpha r+\tau\chi)(B+\eta I)^{-1}.
                                                        \tag{1}
\]

These are fixed initialized coefficients, not trainable variables and not
a replacement normalization. For later use, their normal equations give

\[
 b=\frac{\alpha r\eta/(v_0+\eta)+\tau\chi}
          {\ell+\eta-r^2/(v_0+\eta)}>0,
 \qquad
 a=\frac{\alpha v_0-br}{v_0+\eta}.                    \tag{2}
\]

Let

\[
 m(x)=E_\zeta\tanh(\zeta+\alpha x),\qquad
 j(g)=a\tanh g+b\,m(\tanh g).
\]

For `t in [-1,1]`, with independent standard Gaussians `G,Z`, set

\[
 \Phi(t)=\frac1{\tau+\eta}
 E\left[j(G)\tanh\!\left(tG+\sqrt{1-t^2}\,Z\right)\right].
                                                        \tag{3}
\]

For any `u=(u_1,u_2) in S1`, the exact initialized upper preactivation and
activation are

\[
 z_0(u)=Z_1\Phi(u_1)+Z_2\Phi(u_2),\qquad
 H_0(u)=\tanh(z_0(u)).                                 \tag{4}
\]

To verify the normalization in this identity, with
`q(u)=E_1[psi_1 tanh(g.u)]`, the initial preactivation is precisely

\[
 \psi_2^T(G_2+\eta I)^{-1}C(G_1+\eta I)^{-1}q(u).
\]

The constant entries vanish. The two lower coordinate blocks are independent,
and the upper odd raw Gram is `tau I_2`. Multiplying each lower block by
(1) and averaging its `Y_i` over its own independent `zeta_i` gives (3)–(4).
The joint Gaussian pair `(g_i,g.u)` has unit variances and correlation `u_i`,
which explains the scalar argument in (3). This is an algebraic expression
for the canonical Cholesky construction, not a rotation or alteration of
that dictionary.

## 2. A fully analytic monotonicity estimate

It is not safe to assume `a>=0` in (1). The argument instead proves that
the entire conditional combination `x -> ax+b m(x)` is increasing, even
if its first coefficient is negative.

First obtain rational bounds on the initialized constants. For real `x`,
`sinh |x|>=|x|` implies

\[
 \tanh^2x\ge\frac{x^2}{1+x^2}.
\]

If `V~N(0,sigma^2)`, Cauchy–Schwarz applied to
`|V|/sqrt(1+V^2)` and `|V|sqrt(1+V^2)` gives

\[
 E\frac{V^2}{1+V^2}
 \ge\frac{(EV^2)^2}{E[V^2(1+V^2)]}
 =\frac{\sigma^2}{1+3\sigma^2}.
\]

Consequently

\[
 v_0\ge\tfrac14,\qquad \tau\ge\tfrac17,
 \qquad 0<\alpha\le\tfrac67.                          \tag{5}
\]

Define

\[
 \beta(x)=E_\zeta\operatorname{sech}^2(\zeta+\alpha x),
 \qquad \beta_0=\beta(0),\qquad q_0=529/1024>1/2.
\]

For `|x|<=1`,

\[
 q_0\beta_0\le\beta(x)\le\beta_0.                    \tag{6}
\]

For the upper bound, represent the even function `sech^2 z` by its level
sets, which are centered intervals. The Gaussian probability of an interval
`[-R-a,R-a]` decreases with `a>=0`: its derivative is
`phi_tau(R+a)-phi_tau(R-a)<=0`, because the centered Gaussian density
decreases with absolute argument. Integrating these interval probabilities
over levels proves that its convolution with the Gaussian is maximal at
zero. This proves `beta(x)<=beta_0`.

For the lower bound, the tanh addition identity gives, for real `z,a`,

\[
 \frac{\operatorname{sech}^2(z+a)+\operatorname{sech}^2(z-a)}2
 =\operatorname{sech}^2z\operatorname{sech}^2a
   \frac{1+\tanh^2z\tanh^2a}{(1-\tanh^2z\tanh^2a)^2}
 \ge\operatorname{sech}^2z\operatorname{sech}^2a.
\]

Gaussian symmetry thus gives
`beta(x)>=sech^2(alpha x) beta_0>=sech^2(6/7) beta_0`.
For `0<=z<=6/7`, the elementary factorial bound
`(2n)!>=2*12^(n-1)` for `n>=1` yields

\[
 \cosh z\le1+\frac{z^2/2}{1-z^2/12}
 \le1+\frac9{23}=\frac{32}{23}.
\]

Therefore `sech^2(6/7)>=529/1024=q_0`, completing (6).

Next we need an upper bound on the positive regression coefficient `b`.
Conditional Gaussian integration by parts gives

\[
 E[\zeta\tanh(\zeta+\alpha x)]=\tau\beta(x).
\]

Since `E zeta=0`, Cauchy–Schwarz implies
`Var(tanh(zeta+alpha x))>=tau beta(x)^2`. Averaging over `X`, and using
`r=E[Xm(X)]`, gives

\[
 \ell+\eta-\frac{r^2}{v_0+\eta}
 \ge\tau E\beta(X)^2+\eta
 \ge\tau\chi^2+\eta.                                  \tag{7}
\]

Here `E m(X)^2>=r^2/v_0>=r^2/(v_0+eta)`, so its omitted remainder is
nonnegative. Also `m(0)=0` and `m'(x)=alpha beta(x)<=alpha`, hence
`0<r<=alpha v_0`. With `0<chi<=1`, (2) and (7) therefore give

\[
 0<b\le\frac{\tau\chi+\eta/\chi}{\tau\chi^2+\eta}
       =\frac1\chi\le\frac1{q_0\beta_0}.              \tag{8}
\]

Write `R_eta=v_0/(v_0+eta)`. From (5) and the prescribed ridge,
`1024/1025<=R_eta<1`, in particular `R_eta>q_0`.
The sharper derivative bound `m'(x)<=alpha beta_0` gives
`r<=alpha beta_0 v_0`. Thus for every `|x|<=1`, equations (2), (6) and (8)
show

\[
 \begin{split}
 \frac d{dx}\{ax+bm(x)\}
 &=\alpha R_\eta+b\left(\alpha\beta(x)-\frac r{v_0+\eta}\right)\\
 &\ge\alpha R_\eta-b\alpha\beta_0(R_\eta-q_0)\\
 &\ge\alpha\left[1-R_\eta(q_0^{-1}-1)\right]\\
 &\ge\alpha(2-q_0^{-1})
   =\frac{34\alpha}{529}=:\delta_0>0.
 \end{split}                                                   \tag{9}
\]

The sign in the second line matters: `R_eta-q_0>0`, so an upper bound
on `b` gives a valid lower bound. Consequently `j` is odd and

\[
 j'(g)\ge\delta_0\operatorname{sech}^2g>0.             \tag{10}
\]

For `-1<t<1`, differentiate (3) on compact subintervals. With
`V=tG+sqrt(1-t^2)Z`, integration by parts in `G` and then `Z` cancels the
terms containing `tanh'' V` and yields

\[
 \Phi'(t)=\frac1{\tau+\eta}E[j'(G)\operatorname{sech}^2V]>0.
                                                        \tag{11}
\]

For clarity, before cancellation the derivative is
`E[j(G) tanh'(V)(G-tZ/sqrt(1-t^2))]/(tau+eta)`;
the first integration produces
`E[j'(G)tanh'(V)]+t E[j(G)tanh''(V)]`, and the second term cancels the
last summand exactly. Bounded derivatives and Gaussian integrability justify
these operations. The right side of (11) extends continuously to the
endpoints by dominated convergence.

One explicit uniform positive lower bound is

\[
 \Phi'(t)\ge\sigma_0:=
 \frac{\delta_0}{\tau+\eta}
 \Pr\{|G|\le1\}^{\!2}\operatorname{sech}^2(1)
                         \operatorname{sech}^2(\sqrt2)>0.
                                                        \tag{12}
\]

Indeed on `|G|,|Z|<=1` one has `|V|<=sqrt2`. Equations (10)–(11)
then give (12). Integrating (11) up to the endpoints proves strict
monotonicity on the closed interval. Gaussian symmetry also gives
`Phi(-t)=-Phi(t)` and `Phi(0)=0`.

This closes the scalar-monotonicity obligation analytically. It uses no
unverified numerical sign or assumed positivity of the raw coefficient `a`.

## 3. No collisions of initialized coefficient directions

Define the nonzero coefficient vector

\[
 \nu(u)=(\Phi(u_1),\Phi(u_2)),\qquad u\in S^1.
\]

Strict monotonicity and oddness imply that `Phi(t)` has the sign of `t`,
and that `|Phi(t)|` strictly increases with `|t|`.
Suppose `nu(v)=lambda nu(u)`.

If `lambda>1`, all nonzero coordinates satisfy `|v_i|>|u_i|` and zero
coordinates remain zero, contradicting `|u|=|v|=1`. If `0<lambda<1`,
reverse the roles of `u,v` to get the same contradiction. For `lambda=1`,
strict injectivity gives `v=u`. If `lambda<0`, apply the positive-scalar
argument to `-v`, using oddness, to obtain `v=-u`. The case `lambda=0`
is impossible because `nu(v)!=0`. Therefore

\[
 \nu(u),\nu(v)\text{ are linearly dependent}
 \quad\Longleftrightarrow\quad v=u\text{ or }v=-u.      \tag{13}
\]

This argument treats arbitrary orientations and coordinate zeros; it does
not use rotational symmetry of the dictionary.

## 4. Exact initialized readout Gram and its exceptions

For arbitrary `u,v in S1`, let `Z_1,Z_2` be independent copies of
`tanh(sqrt(v_0)G)` and define

\[
 h_u(Z)=\tanh(Z\cdot\nu(u)),\quad
 h_v(Z)=\tanh(Z\cdot\nu(v)),
\]
\[
 A_u=E h_u^2,\quad A_v=E h_v^2,\quad B_{uv}=E[h_uh_v],
 \quad
 \lambda(u,v)=
 \frac{A_u+A_v-\sqrt{(A_u-A_v)^2+4B_{uv}^2}}4.         \tag{14}
\]

These are fixed Gaussian integrals determined only by initialization and the
two input directions. The quantity `lambda(u,v)` is exactly the least
eigenvalue of the probability-weighted initialized readout Gram

\[
 T_0T_0^*=\frac12
 \begin{pmatrix}A_u&B_{uv}\\B_{uv}&A_v\end{pmatrix}.
\]

If `v!=u,-u`, then `lambda(u,v)>0`. To prove this, a null Gram direction
would give a nontrivial linear identity
`a_* tanh(Z.nu(u))+b_* tanh(Z.nu(v))=0` almost surely.
The law of `Z` has strictly positive density throughout `(-1,1)^2`.
Continuity extends this identity to the open square: a nonzero value would
give a nonzero value on an open neighborhood with positive probability.
Differentiate the identity at `Z=0`; since `tanh'(0)=1`, it gives
`a_*nu(u)+b_*nu(v)=0`, contradicting (13).

If `v=u`, the two hidden fields are identical and the Gram has rank one.
If `v=-u`, they are negatives and the Gram again has rank one. In both
cases the nonzero Gram mode is positive, because `nu(u)!=0` and positive
density make `A_u>0`. These are exactly the rank exceptions.

Continuity of (3)–(4) makes `lambda(u,v)` continuous. Thus any compact family
of pairs separated from both coincidence and antipodality has a common
strictly positive lower bound, namely the minimum of the explicit function
(14). No geometry-independent positive bound over all nondegenerate pairs
is claimed: `lambda` tends to zero when either rank exception is approached.

## 5. Small-label convergence for every nondegenerate pair

Fix any `u,v in S1` with `v!=u,-u` and use exactly the initialized closure
and physical metric of `route_local.md`. For the equally weighted law

\[
 \mu=\tfrac12\delta_{(u,+A)}+\tfrac12\delta_{(v,-A)},
 \qquad
 0<A\le\frac{\lambda(u,v)}{8\sqrt5},                  \tag{15}
\]

write `lambda=lambda(u,v)`, `rho=sqrt(lambda)/(2sqrt5)` and
`kappa=lambda/4`. Then the exact full population trajectory satisfies

\[
 \mathcal L(t)\le A^2e^{-\lambda t},\qquad
 \int_t^\infty\|\dot S(s)\|_{\rm physical}\,ds
 \le\frac{2A}{\sqrt\lambda}e^{-\lambda t/2}.            \tag{16}
\]

It stays within distance `rho/2` of initialization and converges to a state
fitting both labels. All evolving blocks are retained, including their
actual coupling through `M` and `M^T`. The complete joint laws converge under
the same-mark coupling; the characteristic increments `w-g,c` also converge
in supremum norm.

Here are the proof steps with the geometry dependence exposed. At a state
at physical distance at most `rho` from initialization, contractions of the
normalized features, `||D||<=2` and the Lipschitz property of tanh give,
uniformly over query inputs,

\[
 \|H_S(x)-H_0(x)\|_2
 \le\|M-D\|_F+2\|w-g\|_2
 \le\sqrt5\|S-S_0\|_{\rm physical}.
\]

The same bound applies to the operator norm of the difference of the two
weighted readout maps. Thus its least singular value stays at least
`sqrt(lambda)/2`, and its Gram stays above `kappa I_2`. The complete tangent
Gram dominates the readout Gram, so the unhalved loss obeys

\[
 \mathcal L'=-\|\dot S\|^2\le-4\kappa\mathcal L,
 \qquad
 \int_a^b\|\dot S\|dt
 \le\frac{\sqrt{\mathcal L(a)}-\sqrt{\mathcal L(b)}}{\sqrt\kappa}.
\]

The latter estimate follows by dividing the energy identity by
`||dot S||>=2sqrt(kappa L)` and integrating. It implies total length at
most `A/sqrt(kappa)<=rho/2`, so a first exit from the `rho` ball is impossible.
The canonical fixed-order existence theorem supplies all finite intervals.
This proves (16) and convergence. Integrability of `sqrt(L)` bounds the
supremum-norm readout and row velocities exactly as in the frozen local proof.

The fitting manifold and neutral-direction statements of that proof now hold
for every such pair: it is locally of codimension two, its physical Hessian
has two positive normal eigenvalues and an infinite-dimensional tangent
kernel, and its current-state readout correction is given by the bounded
right inverse of the current two-output readout map.

The same argument allows arbitrary labels `y_u,y_v` with
`sqrt((y_u^2+y_v^2)/2)<=lambda/(8sqrt5)`, replacing `A` in the bounds by
that initial residual norm. No odd-label symmetry was used in this
nondegenerate-pair argument.

## 6. Antipodal and coincident inputs

For an antipodal pair `(u,+A),(-u,-A)`, oddness holds for every represented
state, so the loss is exactly `(f(u)-A)^2`. The two constraints are compatible
but redundant. Set

\[
 \lambda_{\rm anti}(u)=E\tanh^2(Z\cdot\nu(u))>0.
\]

Applying the preceding one-output version of the singular-value, energy and
first-exit proof gives (16), with `lambda=lambda_anti(u)`, whenever
`0<A<=lambda_anti(u)/(8sqrt5)`. Thus arbitrary-orientation antipodal pairs
are covered in the small-label regime. Their fitting manifold has
codimension one rather than two. General antipodal labels must satisfy
`y_{-u}=-y_u` to fit; this compatibility condition is imposed by the
bias-free architecture itself.

For coincident inputs carrying opposite labels `+A,-A`, `A>0`, exact fitting
is impossible. Their loss is `f(u)^2+A^2`, and the prescribed initialization
has `f=0`. The data gradients cancel there, so the exact closure remains at
initialization by uniqueness. This is a genuine obstruction, not failure of
the proof. Coincident labels with equal targets instead give one compatible
constraint and admit the same one-output small-label argument.

## 7. Adversarial scope check

* The scalar sign proof retains the exact ridge and Gaussian reverse response;
  it does not posit a nonnegative first regression coefficient.
* Positive Gram rank follows from an explicit initialized map and positive
  Gaussian density, not empirical conditioning or a feature-freezing assumption.
* The full nonlinear dynamics are controlled inside a certified basin. The
  small-label hypothesis remains essential to this proof and is stated in
  (15); replacing `A` by one is not justified by changing the clock.
* The threshold is geometry dependent. No uniform positive threshold as the
  two opposite-label inputs approach coincidence can follow from this argument.
* Near antipodality the two-mode bound deteriorates, while the exactly
  antipodal compatible problem reduces to one mode. This difference reflects
  the proof's rank requirement and does not prove a dynamical discontinuity.
* Arbitrary orientation is proved despite the fixed coordinate dictionary;
  no rotational symmetry of the trained closure was assumed.
* This is a theorem for the exact order-one closure. It makes no global-time
  neural-width, closure-accuracy, or generalization assertion.

There is no remaining scalar-monotonicity gap in this candidate. Independent
checking is still required before promotion. The principal unresolved target
remains global convergence for unit labels in arbitrary distinct directions;
initialized readout rank alone does not keep that rank from collapsing during
large nonlinear motion.
