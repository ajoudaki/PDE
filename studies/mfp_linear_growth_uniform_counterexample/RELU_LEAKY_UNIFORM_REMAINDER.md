# ReLU and leaky ReLU: a second-order obstruction to the uniform fifth remainder

## 1. Network and conclusion

Use the width-first `q=1`, two-hidden-layer model

\[
 H_j=\phi(u_j),\qquad z_i=n^{-1/2}\sum_jW_{ij}H_j,
 \qquad f_n=n^{-1}\sum_i A_i\phi(z_i),
\]

with the simultaneous feature/output-ascent update

\[
\begin{aligned}
 A_i^+&=A_i+h\phi(z_i),\\
 W_{ij}^+&=W_{ij}+{h\over\sqrt n}A_i\phi'(z_i)H_j,\\
 u_j^+&=u_j+h\phi'(u_j)n^{-1/2}
                   \sum_iW_{ij}A_i\phi'(z_i).
\end{aligned}
\tag{1.1}
\]

All initialization variables are independent standard Gaussians.  Put

\[
 \phi_{a,b}(x)=a x_+ + b x_-,\qquad x_-:=\min\{x,0\},
 0\le b<a,\qquad {a^2+b^2\over2}=1.                 \tag{1.2}
\]

Thus normalized ReLU has `(a,b)=(sqrt(2),0)`, and normalized leaky ReLU
with negative-side slope ratio `lambda in [0,1)` has

\[
 a=\sqrt{2\over1+\lambda^2},\qquad b=\lambda a.
\]

Let `widehat F_k(h)` be the output of the response-aware piecewise-linear
OMFP DAG at fixed nonzero `h` and

\[
 \widehat\Delta_t(h)=\widehat F_{2t}(h)-\widehat F_t(2h).
\]

Define

\[
 e={a^4+b^4\over2},\qquad
 A\sim N(0,1),\qquad Y\sim N(0,e),                  \tag{1.3}
\]

independently, and

\[
 p=Y+2bA,\qquad q=Y+2aA.                            \tag{1.4}
\]

Finally set

\[
 D_{a,b}
 =\gamma(0)\,\mathbb E\!\left[(a-b)A\,p q\,
             \mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}\right],
 \qquad \gamma(0)={1\over\sqrt{2\pi}}.             \tag{1.5}
\]

### Theorem 1 (conditional operator-DAG statement)

Assume the fixed-step indicator-DAG identification and the one-source
response-intertwining/boundary expansion isolated in Section 3.  Then, for
every fixed integer `t>=1`,

\[
 \widehat\Delta_t(h)=tD_{a,b}h^2+o_t(h^2)\quad(h\downarrow0),        \tag{1.6}
\]

and

\[
 D_{a,b}>0.                                                        \tag{1.7}
\]

The two-sided version, using the exact readout/Gaussian parity, is

\[
 \widehat\Delta_t(h)=tD_{a,b}h|h|+o_t(h^2).                       \tag{1.8}
\]

Consequently, for every `rho>0`, every `t>=1`, and every real `kappa`,

\[
 \sup_{0<|h|\le\rho/t}
 { |\widehat\Delta_t(h)-\kappa h^3|\over |h|^5}=+\infty.         \tag{1.9}
\]

Thus, once the two stated bridges are supplied, ReLU and every nontrivial conventional
leaky ReLU do not merely fail
an `o(t^5)` fifth-remainder estimate.  Their cubic-subtracted fifth
remainder coefficient is not finite even at `t=1`.

For normalized ReLU, (1.5) is elementary and gives

\[
 \boxed{
 D_{\rm ReLU}={\sqrt2\over\pi}\left(1-{1\over\sqrt5}\right)
 }\;=0.248841309660604\ldots .                                    \tag{1.10}
\]

## 2. The paired boundary lemma

The calculation needed below is local and retains the smooth part of the
network output.  Omitting that part gives an incorrect coefficient.

Let a potential, in a neighborhood of a regular switching surface
`r(x)=0`, have the first-order form

\[
 f(x)=f_0+g_-^T(x-x_0)+c\,r(x)_++O(|x-x_0|^2).                    \tag{2.1}
\]

The ascent metric may be any fixed positive symmetric metric.  Let `p` and
`q` be the normal velocities on the negative and positive sides.  Freeze
all coefficients at `x_0`.  For an initial normal coordinate `r(x)=hy`,
write

\[
 S(y)=y+p\mathbf1_{y<0}+q\mathbf1_{y>0},\qquad
 C(y)=y+2p\mathbf1_{y<0}+2q\mathbf1_{y>0}.                         \tag{2.2}
\]

The first map is one fine step and the second is one coarse step.  If
`m_f(y)` and `m_c(y)` are the numbers of positive-side gradient evaluations
in `2t` fine and `t` coarse steps, respectively, the parameter endpoints
differ, to first boundary-layer order, by

\[
 h\{m_f(y)-2m_c(y)\}\,cG\nabla r .                                \tag{2.3}
\]

The corresponding full-potential defect divided by `h` is therefore

\[
 c p\{m_f(y)-2m_c(y)\}
 +c\{(S^{2t}y)_+-(C^ty)_+\}.                                     \tag{2.4}
\]

The first term in (2.4) is the contribution of the smooth linear part in
(2.1).  It cannot be deleted.

### Lemma 2

For all real `p,q,c` compatible with the same switch, and every integer
`t>=1`,

\[
 \int_{\mathbb R}\left[
 cp\{m_f(y)-2m_c(y)\}
 +c\{(S^{2t}y)_+-(C^ty)_+\}
 \right]dy
 =tc\,p q\,\mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}.                \tag{2.5}
\]

#### Proof

The integrand vanishes outside a bounded interval.  On every sign-itinerary
interval it is affine.  Partition at the preimages of zero under the maps
in (2.2), and use

\[
 \int_\alpha^\beta(y+r)_+dy
 ={1\over2}\{(\beta+r)_+^2-(\alpha+r)_+^2\}.                      \tag{2.6}
\]

For one pair, the negative-start and positive-start integrals, divided by
`c`, are

\[
\begin{aligned}
 I_-&=\mathbf1_{\{p>0\}}
 \left[-{p^2\over2}+{(p+q)_+^2-q_+^2\over2}\right],\\
 I_+&=\mathbf1_{\{q<0\}}
 \left[pq+{p_+^2-(p+q)_+^2\over2}\right].                        \tag{2.7}
\end{aligned}
\]

Checking the four sign regimes and, when `p>0>q`, the two signs of `p+q`,
gives

\[
 I_-+I_+=pq\mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}.               \tag{2.8}
\]

Here is an exact all-`t` proof.  Put `delta=q-p` and

\[
 v(y)=py+\delta y_+.
\]

When `delta` is nonzero, (2.3) implies that the integrand in (2.5) is
`c/delta` times

\[
 v(S^{2t}y)-v(C^ty).                                             \tag{2.9}
\]

Let `L_S` denote push-forward of Lebesgue density by `S`, let
`I=(min(p,q),max(p,q))`, and set `s=sign(p-q)`.  Directly counting the one
or two preimages of a point gives

\[
 L_S1=1+s\mathbf1_I,
 \qquad
 L_S^N1=1+s\sum_{k=0}^{N-1}L_S^k\mathbf1_I.                     \tag{2.10}
\]

Moreover `C(2y)=2S(y)` and `v(2y)=2v(y)`.  Consequently, with

\[
 a_k=\int_Iv(S^ky)dy,
\]

the integral in (2.9) is

\[
 s\left\{\sum_{k=0}^{2t-1}a_k
       -4\sum_{k=0}^{t-1}a_k\right\}.                           \tag{2.11}
\]

All quantities in (2.11) are finite; the constant density terms cancel
before the integrals are taken.  It remains only to evaluate `a_k`.
Writing `L=|p-q|` gives the following exhaustive cases:

\[
\begin{array}{c|c}
\text{sign regime}&a_k\\ \hline
p,q>0&Lq\{(p+q)/2+kq\}\\
p,q<0&Lp\{(p+q)/2+kp\}\\
p<0<q&(k+1/2)(q^3-p^3)\\
p>0>q&pq(p-q)/2.
\end{array}                                                       \tag{2.12}
\]

The last line uses that `S` is rotation by `p` modulo `p-q` on the
trapping interval `(q,p)`, and hence preserves Lebesgue measure there.
Now

\[
 \sum_{k=0}^{2t-1}(A+Bk)-4\sum_{k=0}^{t-1}(A+Bk)
 =t(B-2A).                                                        \tag{2.13}
\]

Substitution of the first two lines of (2.12) into (2.11) gives
`t delta p q`; the third line gives zero; and the fourth gives
`-2t[pq(p-q)/2]=t delta p q`.  Multiplication by `c/delta` proves
(2.5).  If `delta=0`, there is no switch and both sides of (2.5) vanish.
The boundary cases `p=0` or `q=0` follow directly, or by continuity.
This also treats arbitrarily many repeated crossings in the attracting
case rather than misclassifying them as distinct boundary surfaces.  QED.

### Lemma 3 (marked reverse-mode intertwining)

Fix a finite-horizon response-aware OMFP DAG and one occurrence of an
initial activation gate.  At each Euler stage, regard the instantaneous
network evaluation graph as the scalar potential whose reverse sweep
produces that stage's ascent field.  Before taking any Gaussian expectation,
attach a formal mark to that gate and to every descendant occurrence of the
same source through the chronological training DAG.  On a cell on which all
other gate signs are fixed, include in the marked descendants the
differentials of every population moment and every Gaussian-regression
coefficient.  Then the complete one-mark, first-order sector uses the exact
reverse derivative of each instantaneous scalar output; composing these
stage derivatives gives the marked training trajectory and terminal output.

More precisely, let `r` be the distinguished preactivation, let
`ell=Dr`, and write the two one-sided gradients of the current scalar
output as

\[
 g_+=g_-+c\ell .                                                   \tag{2.14}
\]

If `G` is the ascent metric, the one-sided normal velocities in the marked
DAG are

\[
 p=\ell^TGg_-,\qquad q=\ell^TGg_+=p+c\ell^TG\ell .                \tag{2.15}
\]

For `2t` fine steps and `t` coarse steps, the complete one-source
boundary-layer contribution, conditional on the unmarked environment, is
exactly the integrand of Lemma 2.  Consequently its integral is

\[
 tc\,pq\,\mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}.                 \tag{2.16}
\]

#### Proof

Use the Gaussian `L^2` pairing for particle fields and the trace pairing for
matrix fields.  Every primitive node of the DAG has its exact adjoint under
these pairings.  This is immediate for sums, products, activation maps on a
fixed sign cell, learned rank-one contractions, and ordinary conditional
expectations.  A regression node is an orthogonal projection onto the span
of the already exposed queries; its reverse node is the adjoint projection.
The differentials of its Gram and cross-moment coefficients are included by
the mark and obey the ordinary product and inverse-free residual-span chain
rules.  Concretely, on a fixed-rank stratum its basis-invariant projector
`P` satisfies `P=P^*=P^2`; differentiating `P=P^*` gives
`DP[dot H]=(DP[dot H])^*`, which is precisely the missing adjoint term from
the moving regression span.  A population-zero residual is first deleted
from the span, so no inverse of a vanishing Gram eigenvalue is used.
Finally, for every fresh residual Gaussian source `J`, the
chronological query `V` is measurable before `J` is exposed.  Its forward
and reverse occurrences therefore obey the exact identity

\[
 \mathbb E\langle JV,U(J)\rangle
 =\mathbb E\langle V,D_J^*U(J)\rangle .                          \tag{2.17}
\]

Here `D_J^*` contracts the matrix derivative with the query in the matching
trace pairing.  If a reused matrix component has already been exposed, first
apply the exact conditional Gaussian decomposition; (2.17) applies to its
independent residual and the projection terms are covered by the regression
adjoints above.  On the fixed sign cell all marked functions are
polynomially dominated, so differentiation in the mark commutes with every
expectation in (2.17).  Induction in reverse topological order now gives,
for each instantaneous evaluation graph `N_s`,

\[
 \langle D\mathcal N_s\,\dot\theta,1\rangle
 =\langle\dot\theta,D\mathcal N_s^*1\rangle,                    \tag{2.18}
\]

including all paths passing through reused regressions and population
moments.  Thus the reverse sweep is the full gradient `g`, not the derivative
of only the visible terminal hinge.  Equations (2.14)--(2.15) follow.

Freeze the unmarked environment and the coefficients at `r=0`.  Whenever a
fine path and a coarse path choose different sides of the gate, their
parameter endpoints differ at first boundary order by

\[
 h\{m_f(y)-2m_c(y)\}\,cG\ell .                                  \tag{2.19}
\]

Pairing (2.19) with the smooth gradient `g_-` gives exactly

\[
 hc p\{m_f(y)-2m_c(y)\}.                                         \tag{2.20}
\]

The nonsmooth value contributes

\[
 hc\{(S^{2t}y)_+-(C^ty)_+\}.                                    \tag{2.21}
\]

These are precisely the two terms in (2.4), so Lemma 2 proves (2.16).

It remains to check completeness at order `h^2` after the gate coordinate
is integrated.  The gate tube has width `O(h)` and (2.20)--(2.21) have size
`O(h)`.  A Taylor remainder or a variation of any frozen smooth coefficient
has size `O(h^2)` in the tube and therefore integrates to `O(h^3)`.  A term
with a second, distinct source mark is not in the one-source sector; its
`O(h^3)` estimate additionally uses the joint-density hypothesis in Bridge
B.  Repeated visits to the distinguished source are not discarded in this
count: all of them occur in `m_f,m_c,S^{2t},C^t` and were summed exactly by
Lemma 2.  Hence there is no further one-source `h^2` term.  QED.

The qualification concerning moment and regression descendants is
essential.  Holding global coefficients fixed while differentiating the
visible scalar path would omit aggregate reused-adjoint contributions and
would give the wrong ReLU constant.

## 3. Boundary expansion and the actual-network bridge

The scalar identity in Section 2 and the initialization law in Section 4
are exact.  Two bridges are still required before they become a theorem
about the complete width-first output.

**Bridge A (fixed nonzero step).**  Prove the alternating adaptive
Gaussian-conditioning theorem for the bounded piecewise-polynomial query
maps generated by (1.1).  It must expose every reused `W/W^T` action,
define response coefficients by population regression rather than by
formally differentiating an indicator, prove non-atomicity at every queried
gate, handle a singular query Gram through its residual span, and establish
empirical moments and terminal uniform integrability.  The useful
a.e.-continuity inequality for an actual/ideal coupling is

\[
 {1\over n}\sum_i\mathbf1_{\{\operatorname{sgn}X_i
              \ne\operatorname{sgn}\bar X_i\}}
 \le {1\over n}\sum_i\mathbf1_{\{|\bar X_i|\le\varepsilon\}}
       +\varepsilon^{-2}\|X-\bar X\|_{n,2}^2.                    \tag{3.1}
\]

Here one sends `n` to infinity first and only then `epsilon` to zero.  This
avoids the false assertion of a small-ball bound uniform over every finite
width: exact ReLU has finite-width atoms when all lower features vanish.
The existing smooth OMFP theorem does not contain this indicator induction.

**Bridge B (small step after the width limit).**  Couple the chronological
Gaussian query fields by their full population Grams and prove localization
of the singular DAG as `h` tends to zero.  Mark initial Gaussian gate
sources.  Repeated occurrences of one source must be retained together and
reduced to Lemma 2; genuinely distinct sources require a joint Gaussian tube
estimate.  A node-by-node response-intertwining identity must then show that
the complete terminal sensitivity of one marked gate, including every
aggregate and reused-adjoint path, equals the smooth-background term in
(2.4).  Initial normal velocities alone do not prove that identity.  A
polynomial Gaussian envelope must finally justify removal of velocity
truncations.

Only after both bridges are proved may one conclude

\[
 \widehat\Delta_t(h)=h^2\sum_{\text{initial gate types}}
   \{\text{Gaussian surface density}\}
   \mathbb E[J_t]+o_t(h^2).                                      \tag{3.2}
\]

Neither bridge may be replaced by a finite-width sign-cell expansion
followed by an interchange of `n` and `h`.

Inside a fixed sign cell the network is smooth.  Its order-two paired
Euler term has zero annealed expectation by the exact readout/Gaussian sign
involution that gives `F_k(-h)=-F_k(h)`.  It is analytic in signed `h`, so
it cannot contribute to the `h|h|` term.  Thus the OMFP-DAG version of
(3.3) contains precisely the kink-surface contributions calculated next.

## 4. Evaluation for the two-hidden-layer network

At initialization

\[
 \mathbb E\phi'(G)^2=1,
 \qquad \mathbb E\phi'(G)^4=e.                                  \tag{4.1}
\]

### Lower gate

At a lower preactivation `u=0`, let `B~N(0,1)` be its backward field.  The
two one-sided normal velocities are

\[
 p=bB,\qquad q=aB.                                                \tag{4.2}
\]

The local hinge coefficient is proportional to `(a-b)B`.  If `b>0`, then
`p` and `q` have the same sign and the indicator in (2.5) is one; its
expected contribution is proportional to

\[
 (a-b)ab\,\mathbb E B^3=0.                                      \tag{4.3}
\]

For ReLU, `b=0`, so `pq=0` pointwise.  Thus the lower kink contributes
zero in every case covered by (1.2).

### Top gate

At a top preactivation `z=0`, the reused-matrix peel gives one fresh field
`Y~N(0,e)`, independent of the readout `A~N(0,1)`.  The explicit rank-one
matrix update and the reused-adjoint response each contribute one copy of
`A phi'(z)`.  Therefore the two normal velocities are exactly

\[
 p=Y+2bA,\qquad q=Y+2aA,                                        \tag{4.4}
\]

which is (1.4).  The output hinge coefficient, after summing the `n`
surfaces against their `1/n` readout normalization, is `(a-b)A`.
The top preactivation has density `gamma(0)` at zero.  Lemma 2 now gives
exactly `tD_(a,b)`.

It remains to prove its sign.  Since

\[
 \mathbb E[(a-b)A pq]=0,                                        \tag{4.5}
\]

(1.5) is equivalently

\[
 D_{a,b}
 =-\gamma(0)(a-b)\mathbb E
  [A p q\mathbf1_{\{p\le0,\ q\ge0\}}].                         \tag{4.6}
\]

On the event in (4.6), `q-p=2(a-b)A>=0`, hence `A>=0`, while `pq<=0`.
The inequalities are strict on a set of positive Gaussian measure whenever
`a>b`.  This proves (1.7).

An entirely explicit positive integral is

\[
 D_{a,b}=\gamma(0)(a-b)
 \int_0^\infty\int_{-2aA}^{-2bA}
 [-A(y+2bA)(y+2aA)]\,\gamma_e(y)\gamma(A)\,dy\,dA.                \tag{4.7}
\]

For ReLU, put `Y=sqrt(2)X`.  The wedge in (4.6) is

\[
 X\le0,\qquad X+2A\ge0.
\]

In polar coordinates `X=r cos(theta)`, `A=r sin(theta)`, its angular
interval is

\[
 \pi/2\le\theta\le\pi-\arctan(1/2).
\]

The two elementary integrals are

\[
 \int_0^\infty r^4e^{-r^2/2}dr={3\sqrt{2\pi}\over2},             \tag{4.8}
\]

and

\[
 \int_{\pi/2}^{\pi-\arctan(1/2)}
 \sin\theta\cos\theta(\cos\theta+2\sin\theta)d\theta
 =-{2\over3}\left(1-{1\over\sqrt5}\right).                    \tag{4.9}
\]

Substitution into (4.6) proves (1.10).

## 5. Uniform-remainder consequence and claim boundary

Fix `t`, `rho`, and `kappa`.  From (1.6),

\[
 {\widehat\Delta_t(h)-\kappa h^3\over h^5}
 ={tD_{a,b}\over h^3}-{\kappa\over h^2}+o_t(h^{-3}).             \tag{5.1}
\]

Because `D_(a,b)>0`, the absolute value is unbounded as `h` decreases to
zero.  Every sufficiently small positive `h` belongs to `(0,rho/t]`, so
(1.9) follows for the OMFP-DAG outputs.  No statement about growth of a finite fifth coefficient is
available or needed: the fifth-order remainder is destroyed three orders
earlier by kink crossings.

For the actual finite-width network with width sent to infinity first, the
conclusion is conditional on Bridges A and B in Section 3.  Until they are
proved, the honest verdict is that Lemma 2, the candidate reused-field law,
and the strictly positive Gaussian constant are proved, while their
intertwining with the complete width-first output remains open.

## 6. Audit points

1. No reversal of limits occurs in the DAG calculation.  The corresponding
   actual-network limit order still requires the bridge in Section 3.
2. The `h^2` term is not a formal ReLU derivative.  It is a Gaussian
   surface integral obtained from exact sign-cell dynamics.
3. The reused `W/W^T` contribution is the second copy of `A phi'(z)` in
   (4.4); omitting it changes both the variance ratio and the constant.
4. The smooth term `cp(m_f-2m_c)` in (2.4) is essential.  A hinge-only
   calculation gives a different, incorrect constant.
5. Lemma 2 handles repeat visits to one gate exactly.  The assertion that
   genuinely distinct source tubes are higher order belongs to Bridge B and
   is not silently assumed here.
6. Conditional on Bridge A, the derivative convention at zero is irrelevant because the fixed-step
   limiting preactivations give zero probability to an exact gate hit.
7. At `a=b=1` the kink vanishes, `D_(a,b)=0`, consistently recovering the
   smooth identity activation.
