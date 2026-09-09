# Route A: dyadic fifth-remainder summability for the width-first depth-two OMFP

## 1. Exact target and verdict

Fix the actual one-input, two-hidden-layer, width-first population network
from `temporary_depth_time_doubling`.  Its population state is

\[
 \theta=(a,K,u)\in
 \mathcal P:=H_2\oplus\operatorname{HS}(H_1,H_2)\oplus H_1, \tag{1.1}
\]

with immutable reused-matrix action

\[
 W_0=I+J^*,\qquad W_0^*=I^*+J.                       \tag{1.2}
\]

At a current state put

\[
 x=\phi(u),\quad z=(W_0+K)x,\quad y=\phi(z),          \tag{1.3}
\]

\[
 \delta=a\phi'(z),\quad r=(W_0+K)^*\delta,
 \quad d=r\phi'(u),                                  \tag{1.4}
\]

and

\[
 \mathcal F(\theta)=\langle a,y\rangle,qquad
 g(\theta)=(y,\delta\otimes x,d).                    \tag{1.5}
\]

The fixed-operator intertwining theorem proves, for every fixed finite step
list, that the inverse-free Gaussian DAG is the Euler recursion

\[
 E_h\theta=\theta+hg(\theta).                         \tag{1.6}
\]

For \(m\ge1\), define

\[
 D_m(h)=F_{m,2}(2h)-F_{2m,2}(h).                      \tag{1.7}
\]

The fixed-horizon singular-Price compiler proves

\[
 D_m(h)=\kappa_mh^3+R_m(h),\qquad
 \kappa_m=-\frac{m(2m-1)}2J_{\phi,2},                \tag{1.8}
\]

and gives an explicit finite activation-envelope constant \(B_m\) with

\[
 |R_m(h)|\le B_m|h|^5.                               \tag{1.9}
\]

The desired weaker condition is

\[
 \sum_{j=0}^\infty \frac{B_{2^j}}{2^{5j}}<\infty.   \tag{1.10}
\]

**Verdict.**  Condition (1.10) is sufficient for a local dyadic scalar
feature-time limit and is strictly weaker than \(B_m=O(m^4)\).  It is not a
consequence of the existing OMFP compiler, causal factorization, \(L^2\)
energy bound, or Gaussian-source estimate.  There is no martingale or
cross-scale Gaussian orthogonality in the annealed width-first remainder.
The exact new obligation is a horizon-uniform, possibly only
scale-averaged, estimate on the reachable response/mixed-tangent system.

A more feasible sufficient theorem bypasses fifth derivatives entirely: a
first-variation reachable-tail/stability lemma gives an \(O(h)\) raw
coarse/fine error and hence dyadic summability.  Sections 6--8 state and
prove that reduction and identify the minimal new OMFP tail lemma.  That
tail lemma itself remains open under the general \(C^{12}\), bounded-
derivative, at-most-linear-growth activation class.

## 2. Exact dyadic implication

Let \(T=2mh\).  From (1.8)--(1.9),

\[
 |D_m(h)|
 \le |J_{\phi,2}|m^2h^3+B_mh^5
 =\frac{|J_{\phi,2}|T^3}{8m}
   +\frac{B_mT^5}{32m^5}.                            \tag{2.1}
\]

Thus, for \(G_m(T)=F_{m,2}(T/m)\),

\[
 |G_{2m}(T)-G_m(T)|
 \le\frac{|J_{\phi,2}|T^3}{8m}
 +\frac{B_mT^5}{32m^5}.                              \tag{2.2}
\]

The first series over \(m=2^j\) is geometric.  Under (1.10), the second is
summable.  Hence \(G_{2^j}(T)\) is Cauchy, uniformly for \(|T|\le T_0\) if
the constants and remainder bounds are uniform on that interval.  This is
the proposition proved and independently audited in
`temporary_depth_time_doubling/AUDIT_DYADIC_CONVERGENCE.md`.

The condition is much weaker than a quartic pointwise estimate.  For
example, it permits

\[
 B_{2^j}=\frac{2^{5j}}{(j+1)^2},                     \tag{2.3}
\]

which is almost quintic rather than quartic.

## 3. The truly minimal fifth-jet condition

Because \(D_m\) is odd and \(C^5\), Taylor's integral identity is

\[
 R_m(h)=\frac{h^5}{24}\int_0^1(1-s)^4D_m^{(5)}(sh)\,ds. \tag{3.1}
\]

Consequently no supremum constant \(B_m\) is logically necessary.  A
strictly weaker sufficient condition is

\[
 \sum_{j=0}^\infty 2^{-5j}
 \sup_{|T|\le T_0}
 \int_0^1(1-s)^4
 \left|D_{2^j}^{(5)}\!\left(\frac{sT}{2^{j+1}}\right)\right|ds
 <\infty.                                             \tag{3.2}
\]

Indeed, substitute \(h=T/2^{j+1}\) in (3.1) and telescope (2.2).
Condition (3.2) is the exact scale-integrated fifth-jet target.

The signed Price compiler expands every integrand in (3.2) as a finite sum
of Gaussian activation/response atoms.  Let \(\mathfrak M_m(h)\) be the
sum of the absolute values of all those marked atoms after causal
source-time factors have been extracted.  It is a completely finite,
activation-defined OMFP quantity for each fixed \(m,h\), and

\[
 |D_m^{(5)}(h)|\le\mathfrak M_m(h).                   \tag{3.3}
\]

Thus a non-output-derived sufficient OMFP lemma is

\[
 \sum_{j=0}^\infty 2^{-5j}
 \sup_{|T|\le T_0}\int_0^1(1-s)^4
 \mathfrak M_{2^j}\!\left(\frac{sT}{2^{j+1}}\right)ds
 <\infty.                                             \tag{3.4}
\]

The present compiler bounds \(\mathfrak M_m\) by
\(B_\phi^{E_{2,m}}\), where \(E_{2,m}\) grows far faster than linearly.
That bound makes (3.4) diverge and supplies no information about the actual
scale sum.

## 4. Why there is no scale martingale

### 4.1 The increments are deterministic

Each \(F_{m,2}(h)\), \(D_m(h)\), and \(R_m(h)\) is already a Gaussian
expectation after the width limit.  Hence the dyadic increments are
deterministic numbers.  There is no filtration with respect to which they
are nontrivial martingale differences.

One can couple all meshes through the same fixed \(I,J\) source, but mesh
refinement adds no independent Gaussian layer.  It only evaluates the same
immutable action at new adaptive queries.  Alternatively constructing a
fresh Gaussian realization at each mesh destroys the reused-matrix coupling
and gives no identity for the difference of expectations.

### 4.2 Conditional innovations do not help the annealed bias

In the finite-width cavity proof, each new row or column action has a fresh
orthogonal residual after projection on the revealed query spans.  The
centered residual is useful for fixed-program concentration.  Its annealed
mean is zero.  The coarse/fine bias is instead carried by the regression and
Stein response terms.  Those terms lie in the historical feature/cotangent
span and are coherent rather than martingale-orthogonal.

### 4.3 The small-step time Gram is maximally correlated

At \(h=0\), all time copies coalesce.  Every forward time Gram and every
cotangent time Gram has rank one.  Thus the fields at different time indices
are maximally correlated at precisely the point about which the fifth
compiler expands.  An estimate replacing a sum of \(m\) historical terms by
its square-root size through time-index orthogonality is therefore false at
the base point.

### 4.4 Same-sign depth-two witness

For the admissible identity activation, the exact depth-two Gaussian
recursion gives

\[
 [h^5]D_m(h)=
 -\frac{2452}{3}m^4+1896m^3
 -\frac{4403}{3}m^2+369m.                            \tag{4.1}
\]

This is negative for every integer \(m\ge1\).  For \(m=1\) the negative
coefficient can be written as

\[
 [h^5]D_m(h)=-\frac m3Q(m),\qquad
 Q(m)=2452m^3-5688m^2+4403m-1107.
\]

Here \(Q(1)=60>0\), \(Q(2)=4563>0\), and for \(m\ge3\),

\[
 2452-\frac{5688}{m}+\frac{4403}{m^2}
       -\frac{1107}{m^3}
 >2452-1896-41>0.                                    \tag{4.2}
\]

Thus even the leading fifth-order biases at successive dyadic scales are
coherent in sign.  This does not disprove dyadic convergence—the quartic
size is summable after division by \(m^5\)—but it decisively rules out a
proof based on cancellation or orthogonality of the leading fifth atoms.

## 5. What causal factorization achieves, and where it stops

For arbitrary step variables \((\varepsilon_i)\), the depth-two OMFP gives

\[
 \rho_{si}=\varepsilon_i\bar\rho_{si},\qquad
 \sigma_{si}=\varepsilon_i\bar\sigma_{si},
 \qquad i<s,                                        \tag{5.1}
\]

and hence the Volterra form

\[
 z_s=\xi_s+\sum_{i<s}\varepsilon_i
        (Q_{is}+\bar\rho_{si})\delta_i,              \tag{5.2}
\]

\[
 r_s=\chi_s+\sigma_{ss}x_s
 +\sum_{i<s}\varepsilon_i
        (K_{is}+\bar\sigma_{si})x_i.                 \tag{5.3}
\]

Therefore every unmarked historical chain is integrated against total step
variation rather than counted as a bare factor \(m\).  For a fixed marked
derivative order this removes the purely combinatorial exponential in the
history length.

It does not bound the normalized kernels.  Their exact recursions contain

\[
 q_s^i=\alpha_s^i\phi'(z_s)
       +a_s\phi''(z_s)\zeta_s^i,                     \tag{5.4}
\]

\[
 \widehat d_s^i=\phi'(u_s)\widehat r_s^i
                 +r_s\phi''(u_s)p_s^i.               \tag{5.5}
\]

Already in \(L^2\), (5.4) requires

\[
 \|a_s\zeta_s^i\|_2
 \le\|a_s\|_4\|\zeta_s^i\|_4,                     \tag{5.6}
\]

and (5.5) has the analogous \(r_sp_s^i\) product.  The proved energy
estimate controls only \(L^2\).  Repeating Holder at a higher moment raises
the required moment again.  Three common-step derivatives of the paired
defect additionally create mixed moving-source fields

\[
 I(\partial_\lambda x_s),\quad
 J(\partial_\lambda\delta_s),quad
 \partial_\lambda\partial_{\chi_i}x_s,quad
 \partial_\lambda\partial_{\xi_i}\delta_s.          \tag{5.7}
\]

No existing OMFP lemma bounds these uniformly or in the scale-summed norm
(3.4).

The Gaussian exponential estimate for a step-weighted sum of the raw
sources controls \(\sum_i|\varepsilon_i||\xi_i|\) and
\(\sum_i|\varepsilon_i||\chi_i|\).  It does not control the adjoint response
fields in (5.4)--(5.7).  The counterexample

\[
 x=Jc,\qquad x\text{ standard Gaussian},\qquad J^*x=c, \tag{5.8}
\]

with \(\|c\|_2=1\) and arbitrarily large \(\|c\|_p\), shows why an ambient
Gaussian-input moment bound cannot do so.

The dyadic weights \(2^{-5j}\) are applied only after the horizon-
\(2^j\) marked atoms have been evaluated.  They do not repair the missing
\(L^p\) estimate inside a single scale.

## 6. A weaker route that avoids the fifth remainder

For scalar continuous feature time, it is unnecessary to control three
derivatives of the transported local defect.  A first-variation stability
estimate suffices.

### Theorem 6.1 (first-variation OMFP reduction)

Fix \(T_0>0\).  Suppose there is a restart-invariant reachable class
\(\mathcal K_{T_0}\subset\mathcal P\) and constants \(G,L<\infty\) such
that, for every \(\theta,\widetilde\theta\in\mathcal K_{T_0}\),

\[
 \|g(\theta)\|_{\mathcal P}\le G,\qquad
 \|g(\theta)-g(\widetilde\theta)\|_{\mathcal P}
 \le L\|\theta-\widetilde\theta\|_{\mathcal P},      \tag{6.1}
\]

and every Euler string of total variation at most \(T_0\), including the
coarse/fine hybrids, remains in \(\mathcal K_{T_0}\).  Then, whenever
\(2mh\le T_0\),

\[
 |F_{m,2}(2h)-F_{2m,2}(h)|
 \le 2LG^2e^{2LT_0}\,m h^2.                          \tag{6.2}
\]

Consequently, at fixed \(T=2mh\),

\[
 |F_{m,2}(T/m)-F_{2m,2}(T/(2m))|
 \le LG^2e^{2LT_0}\frac{T^2}{2m},                   \tag{6.3}
\]

and the dyadic scalar outputs converge uniformly on \([0,T_0]\).

#### Proof

The one-macro-step state defect is exact:

\[
\begin{aligned}
 E_h^2\theta-E_{2h}\theta
 &=h\{g(\theta+hg(\theta))-g(\theta)\},\\
 \|E_h^2\theta-E_{2h}\theta\|_{\mathcal P}
 &\le LGh^2.                                         \tag{6.4}
\end{aligned}
\]

The Lipschitz constants of \(E_h\) and \(E_{2h}\) are at most
\(1+Lh\) and \(1+2Lh\).  Hybrid telescoping over \(m\) macro-steps and
\((1+Lh)^{2m}\le e^{2Lmh}\le e^{LT_0}\) give

\[
 \|E_h^{2m}\theta_0-E_{2h}^{m}\theta_0\|_{\mathcal P}
 \le LG e^{LT_0}m h^2.                               \tag{6.5}
\]

Since \(D\mathcal F=g\), (6.1) implies that \(\mathcal F\) is
\(G\)-Lipschitz on every generated line segment contained in the reachable
class.  Enlarging the class to those segments, if necessary, and allowing a
harmless factor two gives (6.2).  Substituting \(h=T/(2m)\) proves (6.3),
whose dyadic sum is geometric. \(\square\)

The constants in (6.2) are deliberately loose.  The substantive point is
that only first-variation stability is used.  No fifth output derivative,
third transported-defect derivative, or \(t^4\) theorem appears.

## 7. The minimal new reachable-tail lemma

The Lipschitz assumption in Theorem 6.1 is too strong on ambient \(L^2\)
balls, but its proof extends to a forced Osgood modulus.  For depth two, the
only non-Lipschitz products in comparing two gradients are

\[
 \widetilde a\{\phi'(z)-\phi'(\widetilde z)\},
 \qquad
 \widetilde r\{\phi'(u)-\phi'(\widetilde u)\}.       \tag{7.1}
\]

This identifies a substantially weaker new OMFP lemma than
\(\mathrm{UGC}_4\).

**Reachable multiplier lemma \(\mathrm{RML}_1(\phi,2,T_0)\).**  There are
events/classes containing every exact, Euler, coarse/fine, and forced hybrid
trajectory of total time at most \(T_0\), and a deterministic tail envelope
\(\tau_{T_0}(R)\downarrow0\), such that for every multiplier
\(q\in\{a_s,r_s\}\) on those trajectories,

\[
 \|q\mathbf1_{|q|>R}\|_2\le\tau_{T_0}(R),            \tag{7.2}
\]

and the modulus

\[
 \omega_{T_0}(\delta)
 :=C_\phi\delta+
 C_\phi\inf_{R\ge1}{R\delta+\tau_{T_0}(R)\}        \tag{7.3}
\]

has both:

\[
 \int_{0^+}\frac{d\delta}{\omega_{T_0}(\delta)}=\infty \tag{7.4}
\]

and a dyadically summable forced-stability modulus for local errors of size
\(h\omega_{T_0}(Gh)\).                              \tag{7.5}

A uniform \(\psi_1\) bound is a simple sufficient version of (7.2)--(7.5):
it gives \(\omega(\delta)\lesssim\delta\log(e/\delta)\), Bihari--Osgood
stability, and a positive-power dyadic mesh rate on every fixed compact
time interval.

### Lemma 7.1 (RML controls the gradient modulus)

On the energy ball proved in `UNIFORM_L2.md`, \(\mathrm{RML}_1\) implies

\[
 \|g(\theta)-g(\widetilde\theta)\|_{\mathcal P}
 \le\omega_{T_0}(C_\phi
          \|\theta-\widetilde\theta\|_{\mathcal P}) \tag{7.6}
\]

after enlarging the numerical activation constant.

#### Proof

Put

\[
 \Delta=\|a-\widetilde a\|_2+
 \|K-\widetilde K\|_{\rm HS}+
 \|u-\widetilde u\|_2.
\]

The energy estimate gives deterministic bounds for
\(\|a\|_2,\|K\|_{\rm HS},\|u\|_2\) and all un-tilded and tilded forward
and backward fields.  Bounded \(\phi'\) gives

\[
 \|x-\widetilde x\|_2\le M_\phi\Delta,              \tag{7.7}
\]

\[
 \|z-\widetilde z\|_2
 \le (2+\|K\|_{\rm HS})\|x-\widetilde x\|_2
 +\|K-\widetilde K\|_{\rm HS}\|\widetilde x\|_2
 \le C_\phi\Delta,                                  \tag{7.8}
\]

and \(\|y-\widetilde y\|_2\le C_\phi\Delta\).

For a bounded gate difference \(w\), split at height \(R\):

\[
 \|qw\|_2
 \le R\|w\|_2+\|q\mathbf1_{|q|>R}w\|_2
 \le R\|w\|_2+2M_\phi\tau_{T_0}(R).                \tag{7.9}
\]

Using

\[
 \delta-\widetilde\delta
 =(a-\widetilde a)\phi'(z)
 +\widetilde a\{\phi'(z)-\phi'(\widetilde z)\},      \tag{7.10}
\]

bounded \(\phi''\), (7.8), and (7.9) yields

\[
 \|\delta-\widetilde\delta\|_2
 \le C_\phi\Delta+
 C_\phi\inf_R\{R\Delta+\tau_{T_0}(R)\}.            \tag{7.11}
\]

Next,

\[
 r-\widetilde r
 =(W_0+K)^*(\delta-\widetilde\delta)
 +(K-\widetilde K)^*\widetilde\delta,               \tag{7.12}
\]

so the \(L^2\)-operator bound for \(W_0\) and the energy bounds control
this difference by the right side of (7.11).  Finally,

\[
 d-\widetilde d
 =(r-\widetilde r)\phi'(u)
 +\widetilde r\{\phi'(u)-\phi'(\widetilde u)\}.      \tag{7.13}
\]

A second use of (7.9), now with \(q=\widetilde r\), controls (7.13).
The tensor identity

\[
 \|\delta\otimes x-\widetilde\delta\otimes\widetilde x\|_{\rm HS}
 \le\|\delta-\widetilde\delta\|_2\|x\|_2
 +\|\widetilde\delta\|_2\|x-\widetilde x\|_2       \tag{7.14}
\]

then proves (7.6). \(\square\)

Under the explicit \(\psi_1\) version, the standard discrete
Bihari--Osgood comparison applied to (7.6) proves that coarse/fine Euler
paths converge with a dyadically summable positive-power rate.  The output
is Lipschitz on the energy ball by (7.7)--(7.8) and Cauchy--Schwarz, so the
scalar outputs converge as well.  This route requires only value and first-
variation tails, not the mixed four-jet ledger needed for \(t^4h^5\).

## 8. Can existing OMFP lemmas prove RML?

No.

The currently proved uniform estimates are:

1. an \(L^2\) energy bound for \(a,K,u,x,z,y,\delta,r,d\) at bounded total
   step variation;
2. causal source-time divisibility of every strictly historical response;
3. a horizon-free exponential bound for step-weighted sums of the raw
   Gaussian sources \(\xi_s,\chi_s\); and
4. all finite moments for every separately fixed finite history.

None implies (7.2) uniformly in the horizon.  A bounded family in \(L^2\)
need not be square-uniformly integrable.  Fixed-history \(L^p\) bounds can
diverge with the history.  The raw-source estimate does not include the
adaptive adjoint responses.  Finally, \(J^*Jc=c\) embeds arbitrary
\(L^2\) tail profiles behind a standard-Gaussian forward source, so no
ambient input-law estimate can replace a reachable-trajectory theorem.

Thus the exact minimal new OMFP obligation for the first-variation route is
RML, or an equivalent reachable forced-stability estimate.  For the literal
fifth-remainder route it is the stronger scale-averaged marked-atom estimate
(3.4).  Neither is proved in the existing machinery.

## 9. Source dependency and claim boundary

This route uses only the following established components:

- the actual finite-width network and fixed-step width identification from
  `temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md`;
- the inverse-free Gaussian DAG and singular Price compiler from
  `temporary_depth_time_doubling/COMPILER_DEPTH_TIME.md`;
- the fixed bounded \(I+J^*\) operator realization and Euler intertwining
  from `temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md` and
  `OPERATOR_BRIDGE_CHECK.md`;
- the causal source-time response factorization, \(L^2\) energy estimate,
  and weighted raw-source Gaussian bound from
  `temporary_depth_time_doubling/UNIFORM_L2.md`; and
- the exact depth-two identity fifth coefficient from
  `temporary_quantitative_width_first_bound_general_t/ALGEBRA_AND_OBSTRUCTION.md`.

No finite-width Taylor expansion, width/step limit interchange, Gram inverse,
or unproved ambient \(L^p\) connector estimate is used.

The proved conclusion of this note is the implication

\[
 \text{(1.10), (3.2), (3.4), or RML plus its stated stability property}
 \quad\Longrightarrow\quad
 \text{local dyadic scalar feature-time convergence}. \tag{9.1}
\]

The unconditional premise currently available is none of (1.10), (3.2),
(3.4), or RML.  Therefore a well-behaved generic nonlinear depth-two OMFP
continuous-time scalar limit is not proved here.  The route does show that
uniform \(C^5\) control and a pointwise \(O(m^4)\) fifth remainder are much
stronger than necessary: the smallest analytically meaningful missing bridge
is a reachable value/first-variation tail-stability lemma.
