# Direct finite-width route: exact bounds and remaining symmetry gap

Status: bounded proof-search attempt, 2026-10-11. No new unconditional
arbitrary-label fitting theorem or actual-Gaussian-flow counterexample was
obtained. The exact identities and conditional bounds below were derived
and algebraically checked by the route author; independent checking remains
pending. This file is not a promotion packet.

The initial scientific input was only the supervisor's model and target.
After the initial independent attempt was reported, the supervisor authorized
the complete same-study `INTRINSIC_ENDPOINT_ROUTE.md` and
`INTRINSIC_ENDPOINT_CHECK.md`; both were read. Their symmetric simplex endpoint
lemma is treated as an existing conditional result and is not reproved here.
No other scientific sources, studies, experiments, or external theorems were
used. Required research, rigorous-proof, and canonical-notation instructions
were read. Only this assigned file was written; no Git writes were performed.

## 1. Model and finite-width contract

Fix unit columns \(x_a\in\mathbb R^d\), \(1\le a\le m\), and write

\[
X=[x_1\ \cdots\ x_m],\qquad
U=\tanh(AX),\qquad Z=WU,\qquad H=\tanh Z,
\]
\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},\quad
w\in\mathbb R^n,\qquad f=H^\top w/n,
\qquad r=f-y,\qquad \mathcal L=\|r\|_2^2/m.
\]

Tanh acts entrywise. Training is physical-time gradient flow with mobilities

\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L.
\]

Initialization is \(A_{ij}(0)\sim N(0,1)\),
\(W_{ij}(0)\sim N(0,1/n)\), mutually independent, and \(w(0)=0\).
The target was fitting with probability tending to one as \(n\to\infty\),
for fixed correlated data and arbitrary fixed label amplitude, retaining all
three trained layers. No population construction is assumed in the results
below. The constants may depend on the fixed \(X,y,m\) and a stated finite
time horizon, but not on \(n\), except through an explicitly bounded initial
operator norm.

For sample \(a\), let \(u_a,h_a\) denote the corresponding feature columns,
and define the backward vectors

\[
b_a=w\odot(1-h_a^2),\qquad
c_a=(1-u_a^2)\odot W^\top b_a.
\]

The exact tangent kernel for these mobilities is

\[
K_{ab}
=\frac{h_a^\top h_b}{n}
 +\frac{(b_a^\top b_b)(u_a^\top u_b)}{n^2}
 +\frac{(c_a^\top c_b)(x_a^\top x_b)}{n}.
\tag{1}
\]

Each summand is a Gram matrix. Write \(K_{\mathrm{R+W}}\) for the first
two summands. Direct differentiation gives

\[
\dot f=-\frac2mKr,\qquad
\dot w=-\frac2mHr,\qquad
\dot W=-\frac2{mn}\sum_a r_a b_a u_a^\top,
\qquad
\dot A=-\frac2m\sum_a r_a c_a x_a^\top.
\tag{2}
\]

These are exact identities and do not assert closure of any observable system.

## 2. Global existence and path length under a kernel gap

Define the physical speed in the mobility metric by

\[
v(t)^2=
\frac{\|\dot A\|_F^2}{n}+\|\dot W\|_F^2
 +\frac{\|\dot w\|_2^2}{n}.
\]

The gradient-flow identity and (1) give

\[
-\dot{\mathcal L}=v^2
=\frac4{m^2}r^\top Kr,
\qquad
\int_0^T v(t)^2\,dt\le\mathcal L(0)=\frac{\|y\|_2^2}{m}.
\tag{3}
\]

Consequently the mobility-metric path length on any finite interval is at
most \(\sqrt{T\mathcal L(0)}\). For fixed \(n\), this bounds all parameter
coordinates up to any finite time. The vector field is smooth on the whole
finite-dimensional parameter space, so a finite maximal existence time
would have a bounded state and a smooth local continuation, a contradiction.
The finite-width flow therefore exists for all \(t\ge0\).

Suppose \(K(t)\succeq\kappa I_m\), with \(\kappa>0\), on a time interval
starting at zero. Then

\[
v\ge\frac{2\sqrt\kappa}{\sqrt m}\sqrt{\mathcal L},
\qquad
\mathcal L(t)\le\mathcal L(0)e^{-4\kappa t/m}.
\]

At times of nonzero loss, \(v=(-\dot{\mathcal L})/v\), so integration yields

\[
\ell(t):=\int_0^t v(s)\,ds
\le\frac{\sqrt m}{2\sqrt\kappa}
  \int_0^t\frac{-\dot{\mathcal L}}{\sqrt{\mathcal L}}\,ds
=\frac{\sqrt m}{\sqrt\kappa}
 [\sqrt{\mathcal L(0)}-\sqrt{\mathcal L(t)}]
\le\frac{\|y\|_2}{\sqrt\kappa}.
\tag{4}
\]

If loss reaches zero, the vector field vanishes and the same inequality
extends by continuation. These are conditional path estimates, not a proof
that such a gap persists.

## 3. A precise audit of the saturated-reservoir bootstrap

The candidate mechanism was to retain a spanning fraction of initially
saturated second-layer rows while the readout fits the labels. The following
calculation makes the label restriction in one such argument explicit.

Put \(Q=\|X\|_{\mathrm{op}}\), \(C_0=\|W(0)\|_{\mathrm{op}}\), and

\[
C_X=\sqrt{m+C_0^2Q^2}.
\]

Since tanh is 1-Lipschitz, \(\|U-U(0)\|_F\le Q\|A-A(0)\|_F\),
and \(\|U\|_{\mathrm{op}}\le\sqrt{nm}\). The identity

\[
Z-Z(0)=[W-W(0)]U+W(0)[U-U(0)]
\]

therefore gives

\[
\frac{\|Z-Z(0)\|_F}{\sqrt n}
\le\sqrt m\|W-W(0)\|_F
 +C_0Q\frac{\|A-A(0)\|_F}{\sqrt n}
\le C_X\ell(t).
\tag{5}
\]

Choose a row set \(S\subset\{1,\ldots,n\}\) such that

\[
\min_a|Z_{ia}(0)|\ge M>0\quad(i\in S),
\qquad p=|S|/n,
\]

and define its sign vectors \(\varepsilon_i\in\{-1,1\}^m\) and sign-frame
gap by

\[
\varepsilon_{ia}=\operatorname{sgn}Z_{ia}(0),\qquad
\frac1n\sum_{i\in S}\varepsilon_i\varepsilon_i^\top
\succeq\kappa_0 I_m,\qquad\kappa_0>0.
\tag{6}
\]

Tracing (6) shows \(\kappa_0\le p\). Suppose also

\[
2e^{-M}\sqrt{mp}\le\frac{\sqrt{\kappa_0}}4.
\tag{7}
\]

Call a row in \(S\) bad at time \(t\) if some
\(|Z_{ia}(t)-Z_{ia}(0)|>M/2\), and let \(q(t)\) be the number of bad
rows divided by \(n\). By (5),

\[
q(t)\le\frac{4C_X^2\ell(t)^2}{M^2}.
\tag{8}
\]

On each remaining row, signs are preserved and all preactivation magnitudes
are at least \(M/2\), hence

\[
|H_{ia}(t)-\varepsilon_{ia}|\le2e^{-M}.
\]

Deleting bad sign vectors decreases the frame matrix in operator norm by
at most \(mq\). Thus, if \(q\le\kappa_0/(4m)\), its remaining smallest
singular value, with the \(n^{-1/2}\) normalization, is at least
\(\sqrt{3\kappa_0/4}\). The corresponding feature perturbation has
operator norm at most \(2e^{-M}\sqrt{mp}\). The triangle inequality and
(7) imply

\[
K(t)\succeq H(t)^\top H(t)/n
\succeq(\sqrt3/2-1/4)^2\kappa_0 I_m
\succ\frac{\kappa_0}4 I_m.
\tag{9}
\]

Bootstrap the weaker gap \(\kappa=\kappa_0/4\). Equations (4) and (8)
give

\[
q(t)\le\frac{16C_X^2\|y\|_2^2}{\kappa_0M^2}.
\]

The sufficient condition

\[
\|y\|_2<\frac{\kappa_0M}{8\sqrt m\,C_X}
\tag{10}
\]

makes \(q<\kappa_0/(4m)\). The strict improvement in (9), continuity,
and global existence close this particular bootstrap for all time. This is
only a conditional small-label certificate based on a prescribed initial
sign frame.

Increasing the saturation margin does not make certificate (10) available
for arbitrary fixed label amplitude under the Gaussian initialization.
Indeed, for any fixed sample \(a\),

\[
Mp\le\frac1n\sum_{i\in S}|Z_{ia}(0)|
\le\left(\frac1n\sum_{i=1}^nZ_{ia}(0)^2\right)^{1/2}.
\tag{11}
\]

Conditional on \(A(0)\), the entries of this column are independent normal
variables with variance \(\|u_a(0)\|_2^2/n\le1\). For every \(\eta>0\),
the elementary Gaussian-square moment-generating function gives

\[
\Pr\left\{\frac1n\sum_i Z_{ia}(0)^2>1+\eta\mid A(0)\right\}
\le\exp\left[-\frac n2\{\eta-\log(1+\eta)\}\right].
\tag{12}
\]

For completeness, write \(Z_{ia}(0)=\sigma G_i\), \(0\le\sigma\le1\).
Using \(\mathbb E e^{tG_i^2}=(1-2t)^{-1/2}\) and Markov's inequality at
\(t=\eta/[2(1+\eta)]\) proves (12), with the zero-variance case immediate.

Since \(\kappa_0\le p\) and \(C_X\ge\sqrt m\), the right side of (10)
is at most \(\sqrt{1+\eta}/(8m)\) whenever the column mean square is
at most \(1+\eta\), whose complement is bounded in (12). This bound is
simultaneous over every choice of \(M,S\), including choices made after
seeing initialization. For fixed \(M\), the sharper Gaussian tail
\(\Pr\{|Z_{ia}(0)|\ge M\mid A(0)\}\le2e^{-M^2/2}\) explains the
same tradeoff.

This conclusion concerns certificate (10), not the true basin of fitting
and not every possible use of saturation. In particular, it is not an
actual-flow failure event. A proof using row-conditional dynamics instead
of total path length might avoid this estimate. At the level of the exact
equations, second-layer saturation suppresses the row's own weight update
but does not by itself suppress the term \(W_i\dot U\) in
\(\dot Z_i=\dot W_iU+W_i\dot U\).

## 4. Exact initial reinforcement in the label direction

There is one useful identity specific to the zero readout. Define the
label-direction feature energy on hidden parameters by

\[
q(A,W)=\frac1n\|H(A,W)y\|_2^2
=y^\top\frac{H^\top H}{n}y.
\]

At initialization the hidden velocities vanish, while
\(\dot w(0)=2H(0)y/m\). Differentiating the hidden gradient flow once,
all terms containing a hidden velocity or \(w(0)\) vanish. For either
hidden parameter block \(\theta\), with mobility \(\mu_A=n\),
\(\mu_W=1\), the surviving term is

\[
\ddot\theta(0)
=\frac{4\mu_\theta}{m^2n}
 \sum_i[H(0)y]_i\nabla_\theta[H(0)y]_i
=\frac{2\mu_\theta}{m^2}\nabla_\theta q(A(0),W(0)).
\]

Because \(\dot A(0)=\dot W(0)=0\), differentiating \(q\) twice yields

\[
\ddot q(0)=\frac2{m^2}
 \left(n\|\nabla_Aq(A(0),W(0))\|_F^2
       +\|\nabla_Wq(A(0),W(0))\|_F^2\right)\ge0.
\tag{13}
\]

Thus the hidden initial acceleration ascends the label-direction readout
energy. No extension of (13) to a monotonic all-time quantity was obtained.
As residual directions change, the factors driving hidden motion no longer
match the gradient of this fixed-label energy.

## 5. A width-uniform observable modulus without backward-field maxima

The following exact estimate was obtained while examining whether simplex
sample symmetry can be handled directly at finite width. It does not require
a population path or an \(L^\infty\) bound on the first backward field.

Fix \(T<\infty\), put \(R=\|y\|_2\), and assume only
\(\|W(0)\|_{\mathrm{op}}\le C_0\). Define

\[
S=\frac{2RT}{\sqrt m},\qquad
M_*=C_0+R\sqrt{T/m},\qquad
C=\sqrt m+M_*Q,\qquad Q=\|X\|_{\mathrm{op}}.
\tag{14}
\]

For \(0\le t\le T\), (2), \(\|r(t)\|_2\le R\), and (3) imply

\[
\|w(t)\|_\infty\le S,\qquad
\|W(t)\|_{\mathrm{op}}\le M_*.
\tag{15}
\]

The first bound follows from
\(|\dot w_i|\le(2/m)\sum_a|H_{ia}r_a|\le2R/\sqrt m\);
the second follows from
\(\|W-W(0)\|_F\le\int_0^t v\le\sqrt{T\mathcal L(0)}\).

Tanh's derivative is bounded by one, so

\[
\frac{\|\dot U\|_F}{\sqrt n}\le Qv,
\qquad
\frac{\|\dot H\|_F}{\sqrt n}
\le\frac{\|\dot Z\|_F}{\sqrt n}
\le\sqrt m\|\dot W\|_F
   +M_*\frac{\|\dot U\|_F}{\sqrt n}
\le Cv.
\tag{16}
\]

Let \(B=[b_1\ \cdots\ b_m]\). Since
\(\dot b_a=\dot w\odot(1-h_a^2)-2w\odot h_a\odot\dot h_a\),

\[
\frac{\|\dot B\|_F}{\sqrt n}
\le\sqrt m\frac{\|\dot w\|_2}{\sqrt n}
   +2S\frac{\|\dot H\|_F}{\sqrt n}
\le(\sqrt m+2SC)v.
\tag{17}
\]

Realize the middle kernel as the Gram matrix of the \(m\) columns
\(b_a\otimes u_a\), using the \(n^{-2}\) normalization on the tensor
space. Their combined Hilbert--Schmidt norm is at most \(\sqrt mS\).
Their derivative norm is at most

\[
\frac{\|\dot B\|_F}{\sqrt n}
+S\frac{\|\dot U\|_F}{\sqrt n}
\le(\sqrt m+2SC+SQ)v,
\]

because each normalized \(\|u_a\|\le1\) and \(\|b_a\|\le S\).
The identity \((F^\top F)'=\dot F^\top F+F^\top\dot F\), first for
the readout features and then for these tensor features, gives

\[
\|\dot K_{\mathrm{R+W}}(t)\|_{\mathrm{op}}
\le D_Tv(t),
\qquad
D_T=2\sqrt mC
     +2\sqrt mS(\sqrt m+2SC+SQ).
\tag{18}
\]

Consequently, for every \(0\le s\le t\le T\),

\[
\|K_{\mathrm{R+W}}(t)-K_{\mathrm{R+W}}(s)\|_{\mathrm{op}}
\le D_T\sqrt{\mathcal L(0)(t-s)}.
\tag{19}
\]

All constants are independent of width once \(C_0\) is fixed. In particular,
large individual coordinates of \(W^\top b_a\) do not obstruct this
observable modulus.

The full kernel also has the elementary finite-horizon magnitude bound

\[
\|K(t)\|_{\mathrm{op}}
\le\operatorname{tr}K(t)
\le m\{1+S^2(1+M_*^2)\}.
\tag{20}
\]

Indeed \(\|h_a\|^2/n\le1\), \(\|b_a\|^2/n\le S^2\),
\(\|u_a\|^2/n\le1\), and
\(\|c_a\|/\sqrt n\le M_*S\). Equation (2) then gives

\[
\|\dot f(t)\|_2\le2R\{1+S^2(1+M_*^2)\}.
\tag{21}
\]

Thus predictions are uniformly Lipschitz and the readout-plus-middle kernel
is uniformly one-half Hölder on finite horizons, without a strong trajectory
limit. These bounds reduce uniform-in-time concentration of these observables
to concentration on a fixed finite time grid: cover \([0,T]\) with a mesh,
apply concentration at its finitely many points, and use (19), (21) between
points. They do not provide that grid-point concentration.

## 6. Why sample exchangeability alone does not close the simplex route

For a regular simplex and constant labels \(y=c\mathbf1\), define

\[
P=I_m-\frac1m\mathbf1\mathbf1^\top,
\qquad \bar f=\frac1m\mathbf1^\top f,
\qquad q_f=Pf,
\qquad e=\bar f-c.
\]

The exact contrast equation is

\[
\dot q_f=-\frac2mPKq_f-\frac{2e}{m}PK\mathbf1,
\]
\[
\frac12\frac d{dt}\|q_f\|_2^2
=-\frac2m q_f^\top Kq_f
 -\frac{2e}{m}q_f^\top K\mathbf1.
\tag{22}
\]

The first term is nonpositive. The second is forced by the sample-symmetry
defect \(PK\mathbf1\). The positive-semidefinite Cauchy--Schwarz bound

\[
|q_f^\top K\mathbf1|
\le(q_f^\top Kq_f)^{1/2}
   (\mathbf1^\top K\mathbf1)^{1/2}
\]

does not introduce a factor tending to zero with width. Nor does \(q_f=0\)
force \(PK\mathbf1=0\): at \(w=0\), predictions vanish for every hidden
state, while \(K=H^\top H/n\) need not have constant row sums.

Gaussian initialization and the simplex's orthogonal sample-permutation
symmetries make the *law* of \(f(t)\) permutation invariant at every fixed
time. This follows by rotating \(A(0)\) in input space and using equivariance
and uniqueness of the finite-width ODE. It implies equal expected predictions
and a permutation-invariant expected kernel. It gives no estimate on their
fluctuations. A width-independent random common-plus-contrast fluctuation
would still satisfy these expectation symmetries.

The existing endpoint lemma applies to a symmetric deterministic state; it
cannot be applied to a single Gaussian realization merely by replacing that
realization by its expectation. In particular, the expectation of a nonlinear
kernel need not be the kernel evaluated at expected state variables.

The narrower unresolved bridge suggested by (19)--(22) is finite-grid
concentration of the prediction and the required kernel symmetry statistics,
with no demand to identify the full parameter or response path. Establishing
that bridge remains a substantive probabilistic problem. No argument here
proves it or claims it is easier than the previously identified construction
problem.

## 7. Robust simplex endpoint coercivity for an actual finite state

The audited endpoint bound has a useful finite-state extension: exact sample
symmetry can be replaced by a quantitative defect. This extension does not
require a population state.

Use the finite-state model above on zero-sum unit inputs
\(\sum_a x_a=0\), including a regular simplex. In this section all neuron
norms and tensor norms use their probability normalizations \(n^{-1}\) and
\(n^{-2}\). Assume at the state in question that

\[
g=\frac1m\sum_a f_a>0,\qquad
\|w\|_\infty\le S_*>0,\qquad \|W\|_{\mathrm{op}}\le M_*>0.
\]

Let \(\Pi_\pi\) be the matrix of a sample permutation \(\pi\), and define
the symmetrized readout-plus-middle kernel and its actual defect by

\[
\bar K=\frac1{m!}\sum_{\pi}\Pi_\pi^\top K_{\mathrm{R+W}}\Pi_\pi,
\qquad
\varepsilon=\|K_{\mathrm{R+W}}-\bar K\|_{\mathrm{op}}.
\]

Write \(\lambda_{\mathrm{com}}\) and \(\lambda_{\mathrm{con}}\) for the
common and contrast eigenvalues of \(\bar K\). Define

\[
c_*=
\frac{g^4\operatorname{sech}^4(\sqrt2S_*M_*/g)}
 {4S_*^2M_*^2(m-1)(1+2S_*)^2}.
\]

Then

\[
\lambda_{\min}(K_{\mathrm{R+W}})
\ge
\min\left\{
\frac{mg^2}{S_*^2}-\varepsilon,\,
c_*-2\varepsilon
\right\}.
\tag{23}
\]

In particular, if
\(\varepsilon\le\frac14\min\{mg^2/S_*^2,c_*\}\), the actual finite-state
kernel gap is at least \(\frac12\min\{mg^2/S_*^2,c_*\}>0\).

Here is the complete adaptation of the audited argument. Since
\(\|w\|\ge g\), \(\|z_a\|\le M_*\), and \(\|w\|_\infty\le S_*\),
the threshold \(R_*=\sqrt2S_*M_*/g\) satisfies

\[
\int_{|z_a|>R_*}|w|^2
\le S_*^2\Pr\{|z_a|>R_*\}
\le S_*^2M_*^2/R_*^2=g^2/2.
\]

Thus every backward vector has

\[
\|b_a\|^2\ge
\frac{g^2}{2}\operatorname{sech}^4R_*.
\tag{24}
\]

For every pair \(a,b\),

\[
(e_a-e_b)^\top K_{\mathrm{R+W}}(e_a-e_b)
\le2(\lambda_{\mathrm{con}}+\varepsilon).
\]

Each of the two Gram contributions is nonnegative, so both
\(\|h_a-h_b\|\) and
\(\|b_a\otimes u_a-b_b\otimes u_b\|\) are bounded by
\(\sqrt{2(\lambda_{\mathrm{con}}+\varepsilon)}\).
The gates give
\(\|b_a-b_b\|\le2S_*\|h_a-h_b\|\), and subtracting the tensor
\((b_a-b_b)\otimes u_b\) yields

\[
\|u_a-u_b\|
\le\frac{(1+2S_*)\sqrt{2(\lambda_{\mathrm{con}}+\varepsilon)}}{\|b_a\|}.
\tag{25}
\]

At each neuron the first preactivations sum to zero. For any nonzero
preactivation at sample \(a\), some other sample has opposite weak sign.
Tanh preserves these signs. Therefore
\(|u_a|^2\le\sum_b|u_a-u_b|^2\) pointwise, and (25) implies

\[
\|u_a\|^2\le
\frac{2(m-1)(1+2S_*)^2(\lambda_{\mathrm{con}}+\varepsilon)}
 {\|b_a\|^2}.
\]

Choose \(a\) with \(f_a\ge g\). Tanh is 1-Lipschitz and vanishes at zero,
so \(g\le f_a\le S_*M_*\|u_a\|\). Combining this inequality with
(24) proves \(\lambda_{\mathrm{con}}+\varepsilon\ge c_*\).
Meanwhile symmetrization preserves the common quadratic form, so

\[
\lambda_{\mathrm{com}}
=\frac1m\mathbf1^\top K_{\mathrm{R+W}}\mathbf1
\ge m\left\|\frac1m\sum_a h_a\right\|^2
\ge\frac{mg^2}{S_*^2}.
\]

For every unit vector \(v\),
\(v^\top K_{\mathrm{R+W}}v\ge v^\top\bar Kv-\varepsilon\).
Taking the infimum and using the two bounds proves (23).

This result identifies an observable finite-width bridge: a small defect
\(\varepsilon\) and positive mean prediction already imply coercivity in
the actual state. It does not prove that training makes or keeps
\(\varepsilon\) small. The zero-sum condition and the present bounds are
deterministic; the required Gaussian concentration is still absent.

## 8. Route registry at freeze

| Mechanism | Exact result | Remaining obstacle | Status |
|---|---|---|---|
| Saturated second-layer reservoir | Conditional certificate (10), with uniform Gaussian cap (11)--(12) on that certificate | Row-conditional motion control would be needed to go beyond its label restriction | This specific bootstrap does not reach arbitrary amplitude |
| Label-direction self-reinforcement | Initial acceleration identity (13) | No all-time monotonicity or residual-alignment invariant | Partial, no fitting theorem |
| Direct simplex contrast control | Exact contrast balance (22); finite-horizon observable moduli (19), (21); robust finite-state endpoint gap (23) | Finite-grid concentration or another actual-flow bound on symmetry defects | Open |

The new exact estimates neither establish all-time fitting nor falsify it.
No rare initialization was promoted into a success theorem, no engineered
initialization or frozen-layer substitute was used, and no finite-time rank
statement was treated as a uniform kernel bound. The decisive missing claim
is still a probabilistic control of the actual jointly trained Gaussian flow,
now expressible at the level of a finite collection of observables if that
weaker route can be proved.
