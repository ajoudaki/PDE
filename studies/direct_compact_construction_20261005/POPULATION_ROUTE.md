# Population-law quadrature route

2026-10-05. Scoped independent theoretical attempt. No experiment was run.
This note uses only the maintained book and the files authorized in the
assignment. It does not use another route in this study. The repository
canonical-notation skill was present but unreadable under the task
permissions; the notation below follows "docs/notation.qmd" directly.

## 1. Outcome

There is an explicit, initialization-only family of finite autonomous models
obtained by quadrature of the canonical Gaussian population law. For every
fixed refinement order it has a finite ODE, fixed storage independent of
elapsed time, and a restartable state. On every fixed physical horizon its
quadrature refinement converges to a finite population closure; increasing the
closure order then converges to the maintained canonical population flow. In
the small-label regime the same energy argument is uniform enough to pass to
the fitted endpoint, so the nested qualitative limit is all-time and includes
that endpoint.

This does **not** prove the requested polylogarithmic-storage, strict
root-width comparison with a fresh dense network. Two logically independent
quantitative statements are missing:

1. an effective population-discretization theorem giving a polylogarithmic
   closure order and quadrature size at accuracy \(n^{-1/2}\); and
2. a strict \(n^{-1/2}\), fixed-confidence comparison of a fresh width-\(n\)
   dense flow with the deterministic population flow on the growing horizon
   \(O(\log n)\), with its finite-width bias controlled separately.

Neither statement follows from dense-versus-dense agreement. The first is a
deterministic quadrature problem; the second is a finite-width stochastic
problem.

## 2. Exact contract and the maintained population reference

Put \(v_a=x_a/\sqrt d\), so \(v_a^Tv_b=\mathbf 1_{\{a=b\}}\), and let
\(Y=\lVert y\rVert_2/\sqrt m\). The dense reference has two width-\(n\)
tanh hidden layers,

\[
 h^1_n(v)=\tanh(A_nv),\qquad
 h^2_n(v)=\tanh(W_nh^1_n(v)),\qquad
 f_n(v)=w_n^Th^2_n(v)/n .                              \tag{1}
\]

Initially the entries of \(A_n\) are independent \(N(0,1)\), those of
\(W_n\) are independent \(N(0,1/n)\), and \(w_n=0\). All three blocks follow
gradient flow of \(m^{-1}\sum_a(f_n(v_a)-y_a)^2\), with canonical mobilities
\((n,1,n)\). Labels may have arbitrary signs.

Maintained "docs/04-continuing-flows.qmd", Section B.1, applies exactly after
setting each of its sum-loss block constants to \(1/m\). It supplies a unique
global deterministic population action/adjoint flow and qualitative
finite-width convergence uniformly on every separately fixed compact physical
interval. Denote its prediction by \(f_\infty(t,v)\). Its initialized middle
object is one reused Gaussian action with its actual Hilbert adjoint, not an
iid kernel and not two independently sampled forward/backward maps.

Passive sphere queries require no new trained coordinate. If
\(g\sim N(0,I_d)\) is the full initialized first row and \(Z_a^1(t)\) are the
population preactivations on the training inputs, orthogonality gives

\[
 Z^1(t,v)=g^Tv+\sum_a(v_a^Tv)\{Z_a^1(t)-g^Tv_a\}.       \tag{2}
\]

The current population middle action then propagates this field. The same
identity holds at finite width. Fixed input nets and the uniform input
Lipschitz bounds on compact time intervals upgrade the maintained finite-list
measurement convergence to the whole fixed-dimensional sphere.

For orthogonal inputs, oddness of tanh gives an initialized top-feature Gram

\[
 Q_\infty(0)=\gamma I_m,\qquad
 \gamma=\mathbb E\tanh^2\!\left(\sqrt q\,G\right),\qquad
 q=\mathbb E\tanh^2(G),\quad G\sim N(0,1).              \tag{3}
\]

In particular \(\gamma>0\). The all-time statements below use the fixed-task
small-label condition

\[
                         Y\le c\,\gamma/m,              \tag{4}
\]

with a sufficiently small numerical \(c\). This condition depends only on
the label RMS, so it is insensitive to signs. The case \(Y=0\) is the exact
stationary zero predictor.

### Population fitting and its endpoint

The maintained theorem gives the global flow but does not itself assert
fitting. That addition follows by the same first-exit argument used in the
authorized compact-runtime sources. Here are the needed details.

Let \(\rho=\lVert(f_\infty(t,v_a)-y_a)_{a=1}^m\rVert_2/\sqrt m\).
While \(Q_\infty(t)\succeq(\gamma/2)I_m\), the readout block of the exact
tangent Gram and the energy identity give

\[
 \rho(t)\le Y e^{-\gamma t/m},\qquad
 \int_0^\infty\rho(t)\,dt\le mY/\gamma .                \tag{5}
\]

The parameter speed squared equals \(-d(\rho^2)/dt\). Combining this with
the first inequality in (5) bounds total parameter length by
\(C Y\sqrt{m/\gamma}\). The hidden velocities contain the readout/backward
size as an additional factor, so the two training-feature displacements are
at most

\[
                 C Y^2(m/\gamma)^{3/2}.                 \tag{6}
\]

Tanh and its derivative are bounded and Lipschitz, and the initialized action
has bounded operator norm. Thus (6), (4), and the singular-value perturbation
bound keep \(Q_\infty(t)\succeq(\gamma/2)I_m\), closing the first exit.
All population parameters have finite path length and converge. Forward
subtraction, uniformly for \(v\in S^{d-1}\), then gives

\[
 \sup_v|f_\infty(\infty,v)-f_\infty(t,v)|
 \le C Y(m/\gamma)e^{-\gamma t/m}.                      \tag{7}
\]

Only fixed \(m,d\) constants are suppressed. Equations (5)--(7) are not a
finite-width rate.

## 3. A law-only finite autonomous model

The construction has three initialization stages. All use only the Gaussian
initialization law, deterministic quadrature, and the dataset.

### 3.1 Finite initialized dictionary

On the two population spaces, enumerate bounded initialized words generated
by constants, bounded functions of rational linear combinations of the
first-row Gaussian coordinates, bounded products, and both orientations of
the one initialized Gaussian middle action. Retain a finite prefix on each
population, written as columns \(\psi_1,\psi_2\). Every action call is compiled
with the Gaussian source/response rule, so a reverse call includes the
response created by earlier forward calls. This is the step that would be
wrong if the reverse action were sampled afresh.

From finite Gaussian integrals compute

\[
 G_\ell=\mathbb E_\ell[\psi_\ell\psi_\ell^T],\qquad
 b_\ell=(G_\ell+\eta I)^{-1/2}\psi_\ell,\qquad
 M_0[i,j]=\mathbb E_2[b_{2,i}(A_0b_{1,j})],              \tag{8}
\]

where \(\eta>0\) is prescribed and \(A_0\) is the canonical initialized
action. The same joint Gaussian program computes all entries in (8). In
particular \(M_0^T\) is the contraction of the actual adjoint. The filters
defined by the \(b_\ell\) are positive contractions because
\(\mathbb E[b_\ell b_\ell^T]\preceq I\).

The generic enumeration is trajectory-free but has no useful rate. A
source-adapted proposed schedule would instead differentiate the population
equations at time zero, retain weighted time/spherical coefficients of the
four forward, reverse, and paired-action source families, and compute every
coefficient with the same Gaussian compiler. Every fixed derivative is a
finite initialized Gaussian program. Thus this proposed schedule also uses
no future population value or trained-path oracle.

### 3.2 Positive quadrature of the two joint mark laws

Apply deterministic positive Gaussian quadrature separately to

\[
 \operatorname{Law}(b_1,g)\quad\hbox{and}\quad
 \operatorname{Law}(b_2),                               \tag{9}
\]

where \(g\sim N(0,I_d)\). The two populations are not paired. Write the
returned lower nodes and weights as \((b_i,g_i,\pi_i)\) and the upper ones as
\((\beta_j,\rho_j)\); the weights in each population are positive and sum to
one. Gaussian truncation followed by a fine positive rule is sufficient for
the qualitative construction. Linear elimination may reduce a temporary
rule while preserving any declared finite list of moments. All temporary
source tables and unused quadrature nodes may be discarded after (8)--(9).

### 3.3 State, observations, and evolution

Let the moving state be lower rows \(u_i\in\mathbb R^d\), upper readouts
\(c_j\in\mathbb R\), and a middle coefficient matrix \(M\). Initialize
\(u_i=g_i\), \(c_j=0\), and \(M=M_0\). For any unit query \(v\), set

\[
\begin{aligned}
 h_i(v)&=\tanh(u_i^Tv),
 &a(v)&=\sum_i\pi_i b_i h_i(v),\\
 H_j(v)&=\tanh(\beta_j^TMa(v)),
 &F(v)&=\sum_j\rho_jc_jH_j(v),\\
 e(v)&=\sum_j\rho_j\beta_jc_j[1-H_j(v)^2],
 &q_i(v)&=b_i^TM^Te(v).
\end{aligned}                                             \tag{10}
\]

With training residuals \(R_a=F(v_a)-y_a\), evolve

\[
\begin{aligned}
 \dot u_i&=-\frac2m\sum_aR_a[1-h_i(v_a)^2]q_i(v_a)v_a,\\
 \dot c_j&=-\frac2m\sum_aR_aH_j(v_a),\\
 \dot M&=-\frac2m\sum_aR_a e(v_a)a(v_a)^T .
\end{aligned}                                             \tag{11}
\]

Equations (10)--(11) use only the saved current state, fixed marks, weights,
and data. They are autonomous and uniquely restartable. Both action
orientations use \(M\) and \(M^T\). The equations are gradient flow of the
mean loss in the constant metric with lower and upper particle weights and
the Frobenius middle metric. Hence

\[
 \frac d{dt}\frac1m\sum_aR_a^2
 =-\sum_i\pi_i|\dot u_i|^2-\sum_j\rho_j|\dot c_j|^2
   -\lVert\dot M\rVert_F^2\le0.                         \tag{12}
\]

There is no clock, stored path, source tape, dense initialization, or
population-response oracle in the running model.

## 4. Storage and work

Let the two dictionary lengths be \(r_1,r_2\), and let the quadrature use
\(P_1,P_2\) nodes. Counting moving variables, fixed marks, weights, the
initialization matrix if retained, and the dataset gives

\[
 S=O\!\left(P_1(r_1+d)+P_2(r_2+1)+r_1r_2+m(d+1)\right). \tag{13}
\]

One right-side evaluation, with the training queries streamed, costs

\[
 O\!\left(m\{P_1(d+r_1)+P_2r_2+r_1r_2\}\right)          \tag{14}
\]

scalar operations and \(O(S)\) working storage. Storage is independent of
the number of elapsed integration steps. These are exact-real counts;
conditioning and required scalar precision are separate initialization
obligations.

If \(r_1+r_2\) and \(P_1+P_2\) are bounded by powers of \(\log n\), (13)--(14)
are polylogarithmic for the fixed task. What is not proved is that the
orders required for error \(n^{-1/2}\) have these bounds.

## 5. What can be proved without a quantitative rate

### Proposition: qualitative quadrature and closure limit

For every fixed finite \(T\), choose nested initialized dictionaries whose
spans are dense in the two generated Gaussian-action spaces, let
\(\eta\downarrow0\), and refine positive rules in (9) in \(\mathcal W_2\).
Then the predictions from (10)--(11) satisfy the nested limit

\[
 \lim_{\mathrm{dictionary}\to\infty}
 \lim_{\mathrm{quadrature}\to\infty}
 \sup_{0\le t\le T}\sup_{v\in S^{d-1}}
       |F(t,v)-f_\infty(t,v)|=0.                        \tag{15}
\]

For labels satisfying (4), the refinements can be taken far enough that
their initialized training-feature Grams are at least
\((3\gamma/4)I_m\). The energy/first-exit argument of Section 2 then applies
uniformly to these finite models. Consequently (15) extends, in the same
nested order, to \(t\in[0,\infty]\), including the fitted endpoints.

#### Proof

At fixed dictionary and ridge, the marks \(b_1,b_2\) are bounded and \(g\)
has a finite second moment. On every fixed horizon, (12) and the bounded tanh
gates bound \(c\), \(M\), and the increments \(u-g\). Couple an exact mark law
and its atomic quadrature in \(\mathcal W_2\). Subtracting (10)--(11) on this
coupling gives

\[
 E(t)\le C_T\left(E(0)+\mathcal W_2(\hbox{lower marks})
                   +\mathcal W_2(\hbox{upper marks})
                   +\lVert M_0-\widetilde M_0\rVert_F\right)
       +C_T\int_0^tE(s)\,ds .                           \tag{16}
\]

Every factor is either bounded or paired with one square-integrable moving
coordinate. Gronwall proves characteristic and matrix convergence. Forward
subtraction proves output convergence at a fixed query; the uniform
\(L^2\) input-Lipschitz bound and a finite sphere net make it uniform in
\(v\).

For dictionary refinement, the positive filters defined after (8) converge
strongly to the identity. The exact target fields over
\([0,T]\times S^{d-1}\), their reverse queries, and the Hilbert--Schmidt
learned-increment derivative form compact sets in their respective spaces.
Uniform strong convergence on compact sets makes the omitted forward,
adjoint, and rank-source defects tend to zero.

A bare cutoff of the target reverse query is not sufficient here: its
Gronwall factor grows with the cutoff, while compactness in \(L^2\) gives no
tail rate. Orthogonality and tanh remove that issue exactly. For one lower
row, let \(z_a\) be its preactivation on training direction \(v_a\), and set

\[
 \Psi(z)=\frac z2+\frac{\sinh(2z)}4,
 \qquad X_a=\Psi(z_a)-\Psi(z_a(0)).                       \tag{16a}
\]

Since \(\Psi'(z)=1/[1-\tanh^2z]\) and
\(v_a^Tv_b=\mathbf1_{\{a=b\}}\), the exact and filtered equations both have

\[
             \dot X_a=-\frac2m R_a q(v_a).               \tag{16b}
\]

Thus the changing lower gate no longer multiplies the unbounded reverse
field in the subtraction. The inverse map from \(X_a\) to \(z_a\) is
one-Lipschitz because its derivative is \(1-\tanh^2z_a\le1\). Every passive
lower preactivation is the frozen orthogonal-complement Gaussian plus the
linear combination of these training preactivations.

The reverse-field difference is now controlled directly in \(L^2\): write
it as the current adjoint acting on the upper-backward difference, the
learned-action difference acting on the target upper backward field, and the
vanishing filtered-initial-adjoint defect. The upper backward field is the
bounded readout times a bounded Lipschitz gate, so its subtraction is linear
in the forward/readout error. The learned-rank difference is controlled in
Hilbert--Schmidt norm. Together with the forward and readout equations, these
estimates give an ordinary linear Gronwall inequality with source equal to
the vanishing forward, adjoint, and rank defects. This proves (15); no target
quantity occurs in (8)--(11). The independent reconstruction in
`POPULATION_CHECK.md` records the complete correction.

Finally, (12), an initialized Gram margin, and (4) give the order-uniform
versions of (5)--(7). Given an all-time tolerance, first choose a fixed \(T\)
making both endpoint tails small, then use (15) on that interval. Comparing
each later time to its own endpoint proves the all-time nested limit. This
last argument is qualitative: it supplies no refinement order for a given
tolerance. \(\square\)

This proposition is the strongest unconditional result of this route. It is
an explicit convergent hierarchy, not a polylogarithmic complexity theorem.

## 6. Exact quantitative lemmas that would close the requested theorem

Let

\[
 T_n=C(m/\gamma)\log(en).                               \tag{17}
\]

The endpoint tails (7) and their finite-width/finite-closure analogues are
then \(O(n^{-1})\) after increasing \(C\). The desired result would follow
from the next two lemmas.

### Q. Effective population source and quadrature

There is an initialization algorithm of Sections 3.1--3.2 which, using no
population trajectory values, returns orders satisfying

\[
 r_1+r_2+P_1+P_2\le C_{\rm task}\log^p(en)              \tag{18}
\]

for one fixed exponent \(p\), and whose autonomous solution obeys

\[
 \sup_{t\in[0,\infty]}\sup_v
       |F_n(t,v)-f_\infty(t,v)|\le C_{\rm task}n^{-1/2}. \tag{19}
\]

A natural candidate is the initialization-jet, weighted
time/spherical-harmonic dictionary from the authorized spherical-source
route. If its dense source count transferred effectively to the population
quadrature, then for fixed tanh and fixed data one would have

\[
 r_1+r_2
 \le C_{\rm task}\{(m/\gamma)\log^{3d/2+1}(en)+m+d\}.    \tag{20}
\]

Any polynomial-size positive cubature for this dictionary would already
make (13) polylogarithmic. The existing arguments do **not** prove this
transfer. In particular they do not bound the quadrature size required to
control nonlinear moving characteristics, action and adjoint defects, and
all passive sphere queries. Generic Gaussian quadrature convergence and
strong dictionary density have no tolerance-to-order rate. The numerical
closure in the maintained book explicitly has iterated limits and no
certified diagonal selector. This is the exact compact-to-population gap.

### W. Fresh dense network versus population at strict root rate

For each fixed confidence \(0<\delta<1\), a fresh dense initialization
independent of the deterministic quadrature satisfies

\[
 \mathbb P\!\left\{
  \sup_{0\le t\le T_n}\sup_v
  |f_n(t,v)-f_\infty(t,v)|>C_{\delta,\rm task}n^{-1/2}
 \right\}\le\delta,                                     \tag{21}
\]

and its own endpoint tail after \(T_n\) is \(O_{\mathbb P}(n^{-1})\).
The constant may depend on confidence and the fixed task, but not on \(n\).
This is the appropriate strict-root fixed-confidence quantifier for a
law-only model facing nondegenerate finite-width fluctuations.

The maintained global population theorem gives only \(o_{\mathbb P}(1)\) on
each separately fixed horizon. It gives neither a rate nor a result on the
growing horizon (17). A proof of (21) must control the reused Gaussian action
and adjoint through a growing adaptive transcript; a fixed-program limit is
insufficient.

Moreover, (21) requires two separate stochastic estimates. In local notation,

\[
 f_n-f_\infty=(f_n-\mathbb Ef_n)+(\mathbb Ef_n-f_\infty). \tag{22}
\]

The first term is fluctuation and the second is finite-width bias. Agreement
of two dense copies can at most address fluctuation around a common center;
it cannot identify that center with \(f_\infty\), and therefore cannot bound
the second term. A same-initialization dense comparison is even less
informative for (22). No dense-versus-dense result in the authorized inputs
supplies (21).

### Conditional all-time theorem

If Q and W hold, the model (10)--(11) has polylogarithmic retained storage and
right-side work by (13)--(14), is autonomous and restartable, and for every
fixed confidence \(1-\delta\),

\[
 \mathbb P\!\left\{
  \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
  |F_n(t,v)-f_n(t,v)|
  \le (C_{\rm task}+C_{\delta,\rm task})n^{-1/2}
 \right\}\ge1-\delta .                                  \tag{23}
\]

The comparison is at the same physical time. At and after \(T_n\), compare
each trajectory with its own fitted endpoint and use its \(O(n^{-1})\) tail;
this includes \(t=\infty\) without freezing either dynamics. Equation (23)
is a direct triangle inequality between two independently audited bridges,
not an inference from dense-versus-dense agreement.

## 7. Adversarial audit

- **Gaussian reuse:** (8) must use one joint source/response compiler. An
  independent reverse Gaussian action changes the model.
- **No hidden oracle:** initial derivatives are allowed because they are
  finite expressions in the Gaussian law and data. Evaluating the already
  solved population path to choose nodes or coefficients is not allowed.
- **No fixed-horizon substitution:** convergence for each fixed \(T\) does
  not give (21) at \(T_n\asymp\log n\).
- **No endpoint shortcut:** fitting of both systems and quantitative tails
  are needed; a compact-time theorem alone does not compare fitted endpoints.
- **No bias shortcut:** independent dense-copy agreement does not prove the
  second term in (22).
- **No hidden storage:** quadrature marks, weights, both action coefficients,
  data, caches, and required scalar precision must all be counted. Temporary
  preprocessing may be discarded, but its arithmetic work is presently
  unbounded by a polylogarithmic theorem.
- **Scope of the angular obstruction:** the authorized lower result rules out
  very small full-feature source spaces in the old quadratic-metric format.
  It does not rule out the observable population closure (10)--(11), but it
  also does not provide Lemma Q.

## 8. Status

The explicit autonomous population-quadrature hierarchy and its qualitative
all-time endpoint convergence are proved at the level stated above. The
requested strict root-width polylogarithmic theorem remains **open**, with
Lemmas Q and W as the exact missing bridges. Q is the first bottleneck for a
direct construction; W remains necessary even if Q is solved. Failure of
this route would be failure of this explicit witness, not an impossibility
theorem for every autonomous predictor.

Scientific inputs actually used: "docs/index.qmd", "docs/notation.qmd", the
finite dynamics in "docs/01-training-geometry.qmd", the orthogonal global
population theorem in "docs/04-continuing-flows.qmd" Section B.1, the finite
population-closure and numerical-closure sections of
"docs/07-observable-closure.qmd" and "docs/08-autonomous-computation.qmd", and
the authorized storage, spherical-source, error-prefactor, integrated-summary,
and orthogonal-tanh route files. No archived-book material was read.
