# Global dissipation bounds and a population compactness obstruction

Status: independently derived route, frozen on 2026-09-18 before sharing
with the supervisor. No experiment, population discretization, external
theorem, or other current basin-route report was used. This is an internal
theory candidate, not promoted material.

Scientific input scope: complete `docs/observable_p1.md`; the population
equations, physical metric, and fixed-order existence portions of
`docs/global_nonlinear.md`; and this study's complete
`plateau_upper_escape.md`, `plateau_finite_critical.md`,
`protected_family.md`, and `rank_one_nonlinear_obstruction.md`.
The research and rigorous-mathematics skills and their applicable
research-contract, adversarial-audit, and proof-search references were read.
No study README, other study, or new basin-route result was read.

## 1. Contract and conclusions

The object is the exact d=3, p=1 population flow with canonical correlated
marks, ridge 1/4096, the full moving matrix and its actual transpose,
unhalved weighted square loss, and population-L2/Frobenius physical metric.
There are three unit input directions, positive probability weights p_i,
and labels y_i in {+1,-1}. Canonical initialization is w=g, c=0, M=D.
All statements about other starting states below are explicitly identified.

This route proves three statements.

1. Every canonical trajectory has physical displacement o(sqrt(t)),
   including all moving blocks. No uniform all-time bound is inferred.
2. With L_infinity=lim L(t), its time-averaged prediction norm squared and
   label correlation both tend to 1-L_infinity. If its prediction vector
   converges, the limiting prediction is orthogonal to its limiting
   residual. These hold even for escaping trajectories.
3. The actual exact-population critical set contains bounded sequences
   with no strongly convergent subsequence, at one fixed compatible
   positive loss, with w and M fixed. Every finite critical state has an
   infinite-dimensional affine readout fiber of critical states. Thus
   boundedness and analyticity cannot simply be replaced by a
   finite-dimensional compact analytic-gradient argument.

Item 3 is a demonstrated obstruction to a proof route; it is not a
nonconvergent orbit or an escaping canonical trajectory. The global
exclusion of positive-loss escape and deterministic saddle approach
remains unproved by this route.

## 2. Exact equations and universal subdiffusive displacement

In the initialized odd sector write b_1 in R6, B=b_2 in R3, and M in
R^(3x6). Define

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i(B)=\tanh(B\cdot v_i),\quad f_i=E_2[cH_i],
\]
\[
 r_i=f_i-y_i,\qquad d_i=E_2[Bc\operatorname{sech}^2(B\cdot v_i)].
\]

The full equations are

\[
 c'=-2\sum_i p_i r_iH_i,\qquad
 M'=-2\sum_i p_i r_i d_i a_i^T,
\]
\[
 w'=-2\sum_i p_i r_i\operatorname{sech}^2(w\cdot u_i)
                         (b_1^TM^Td_i)u_i.                 \tag{1}
\]

The supplied fixed-order continuation proof gives a solution through
every finite time and the energy identity

\[
 L(t)+\int_0^t\bigl(\|w'\|_2^2+\|c'\|_2^2+
                                      \|M'\|_F^2\bigr)ds=1. \tag{2}
\]

Let X be the product physical Hilbert space, and put
z(t)=(w(t)-g,c(t),M(t)-D). Bochner integration and Cauchy--Schwarz give

\[
 \|z(t)\|_X^2\le t\int_0^t\|z'(s)\|_X^2ds
                         =t(1-L(t)).                       \tag{3}
\]

The stronger asymptotic statement follows from the tail dissipation.
For t>A>0,

\[
 \frac{\|z(t)\|_X}{\sqrt t}
 \le\frac{\|z(A)\|_X}{\sqrt t}
       +\left(\int_A^\infty\|z'(s)\|_X^2ds\right)^{1/2}.
\]

First let t tend to infinity, then A tend to infinity. The last integral
vanishes by (2), proving

\[
 \|w(t)-g\|_2+\|c(t)\|_2+\|M(t)-D\|_F=o(\sqrt t).     \tag{4}
\]

This is stronger than the polynomial finite-time estimates used for
continuation. It still permits unbounded subdiffusive escape. In
particular, combined with `plateau_upper_escape.md`, if L_infinity lies
outside the finite signed-partition list there, then

\[
 \|c(t)\|_2+\|M(t)\|_F\longrightarrow\infty,
 \qquad \|c(t)\|_2+\|M(t)\|_F=o(\sqrt t).                \tag{5}
\]

No L-infinity bound on w-g or c is asserted in (4).

## 3. A global readout identity that survives escape

Use the weighted inner product
<f,h>_p=sum_i p_i f_i h_i, so ||y||_p^2=1. Define C(t)=||c(t)||_2^2.
Pairing the exact readout equation with c gives

\[
 C'=-4\langle f-y,f\rangle_p
   =2\{1-L-\|f\|_p^2\}.                                \tag{6}
\]

All pairings are justified on each finite interval by the supplied
bounded-characteristic existence result. The identity also gives
C'<=1, because <f,y>-||f||^2<=1/4 by completing the square. Thus
C(t)<=t; (4) strengthens this to C(t)/t tending to zero.

Integrating (6), dividing by 2T, and using monotone convergence of L(t)
to L_infinity yields

\[
 \frac1T\int_0^T\|f(t)\|_p^2dt\longrightarrow1-L_\infty.
                                                               \tag{7}
\]

Since L=||f||_p^2-2<f,y>_p+1, the same calculation gives

\[
 \frac1T\int_0^T\langle f(t),y\rangle_pdt
       \longrightarrow1-L_\infty,
 \qquad
 \frac1T\int_0^T\langle r(t),f(t)\rangle_pdt\longrightarrow0.
                                                               \tag{8}
\]

If f(t) converges to a vector f_*, finite-dimensional continuity turns
(7)--(8) into

\[
 \|f_*\|_p^2=\langle f_*,y\rangle_p=1-L_\infty,
 \qquad\langle f_*-y,f_*\rangle_p=0.                     \tag{9}
\]

This necessary condition holds without bounded upper parameters or a
population-state limit. It is consistent with the existing compatible
bad critical states f_i=sigma_i m, whose loss is 1-m^2. Therefore it
does not eliminate that failure mechanism. Equations (7)--(8) do not
assert prediction convergence.

## 4. The readout keeps a population history

The exact integral form from c(0)=0 is

\[
 c(t,B)=-2\sum_i p_i\int_0^t r_i(s)
                              \tanh(B\cdot v_i(s))\,ds. \tag{10}
\]

Thus c(t) lies in the closed linear span of the upper ridge features
visited through time t, rather than the span of the three current
features. The first assertion follows directly by Riemann approximation
of the continuous L2-valued integrand on a finite interval. The
instantaneous feature span need not contain the history integral.

Even a bounded allowed range of v does not produce a finite-dimensional
linear span. To see this, choose any distinct positive s_1,...,s_N below
that bound and use v_j=s_j e_1. If
sum_j A_j tanh(s_j B_1)=0 almost surely, continuity and the positive
density of B_1 make it zero on its whole open interval. Taylor expansion
at zero gives

\[
 \sum_j A_j s_j^{2k+1}=0,\qquad k=0,\ldots,N-1.          \tag{11}
\]

Every odd tanh Taylor coefficient is nonzero. Indeed writing
tanh z=sum_(k>=0)(-1)^k a_k z^(2k+1), its differential equation
tanh'=1-tanh^2 gives a_0=1 and
(2k+1)a_k=sum_(j+l=k-1)a_j a_l>0 for k>=1.
The matrix in (11) is a Vandermonde matrix in the distinct s_j^2,
times the nonzero diagonal s_j, so every A_j=0. N is arbitrary.

This does not assert that an arbitrary ridge history is generated by
the self-consistent flow. It proves that finite dimensionality cannot
be justified solely by bounded effective vectors or the integral form
(10). The history is represented by the current function c, as in the
original autonomous population model; (10) is not a proposed closure.

## 5. Infinite-dimensional critical fibers

Fix any finite critical state (w,c,M). Let K be the subspace of odd
upper L2 functions kappa satisfying the finitely many linear conditions

\[
 E_2[\kappa H_i]=0,\qquad
 E_2[B\kappa\operatorname{sech}^2(B\cdot v_i)]=0
                      \quad\hbox{for every }i.           \tag{12}
\]

There are at most twelve scalar conditions on an infinite-dimensional
odd L2 space, so K has infinite dimension. Its intersection with bounded
odd functions is also infinite-dimensional: applying the finite-rank
constraint map to any arbitrarily large independent family of bounded
odd functions leaves kernels of arbitrarily large dimension.

For every bounded kappa in K and real s, replacing c by c+s kappa
leaves all f_i and d_i unchanged. It consequently leaves every right
side in (1) zero, with w and M fixed. Hence

\[
                  (w,c+s\kappa,M)                       \tag{13}
\]

is an exact affine line of finite critical states with unchanged loss.
The linearization of the complete vector field annihilates every such
pure-readout direction. Accordingly any loss Hessian realizing this
linearization in the physical Hilbert metric has an infinite-dimensional
kernel and is not Fredholm. This follows from the definition of a
Fredholm operator, which requires a finite-dimensional kernel; no
convergence theorem is invoked here.

The usual finite-dimensional analytic-gradient convergence implication
therefore cannot be imported merely because the dictionary and input
set are finite. A population gradient inequality or a justified
finite-dimensional reduction would need its own proof. The failure of
the Fredholm hypothesis alone does not prove that all possible
gradient inequalities fail.

## 6. An explicit bounded noncompact family at compatible positive loss

For any independent input triple, use the exact finite stationary state
constructed in `rank_one_nonlinear_obstruction.md`. Its actual lower
field w has a_i=sigma_i a for nonzero a, its full current matrix is
M=e_1 a^T/|a|^2, and

\[
 v_i=\sigma_i e_1,\quad f_i=\sigma_i m,\quad
 d_i=\delta e_2,\quad M^Td_i=0,\quad
 L=1-m^2\in(0,1).                                      \tag{14}
\]

The source supplies bounded odd c and bounded w-g with exactly these
properties, on the unchanged canonical mark laws. In particular the
upper coordinates B_1,B_2,B_3 are independent, identically distributed,
centered, and bounded by R>0, with integrable positive densities.
Write sigma_B^2=E B_3^2>0, and set

\[
 h_n(B_3)=\sqrt2\sin(2^nB_3/R),\quad
 \beta_n=E[B_3h_n(B_3)],\quad
 \kappa_n=h_n-\frac{\beta_n}{\sigma_B^2}B_3.             \tag{15}
\]

These are odd and uniformly bounded; for example
|beta_n|<=sqrt2 R gives
||kappa_n||_infinity<=sqrt2(1+R^2/sigma_B^2).
They have E kappa_n=E[B_3 kappa_n]=0. Independence now gives, for
every input in (14),

\[
 E[\kappa_n H_i]=0,\qquad
 E[B\kappa_n\operatorname{sech}^2(B_1)]=0.              \tag{16}
\]

For the first two coordinates of the second identity, factor out
E kappa_n=0; for the third use E[B_3 kappa_n]=0. Thus each kappa_n
belongs to (12), and (w,c+kappa_n,M) is an exact stationary state with
the same positive loss and the same full nonzero rank-one cancellation.

The elementary vanishing of Fourier integrals for integrable densities
shows beta_n->0 and ||h_n||_2^2->1. Here it can be proved without an
external theorem: approximate the integrable density, or B_3 times that
density, in L1 by finite step functions; a nonzero-frequency exponential
has interval integral of magnitude at most 2 divided by its frequency;
the L1 approximation error bounds the remaining integral uniformly.
The sine product identity gives

\[
 E[h_nh_m]=E\cos((2^n-2^m)B_3/R)
              -E\cos((2^n+2^m)B_3/R)\longrightarrow0    \tag{17}
\]

as distinct n,m both tend to infinity, because both absolute frequencies
tend to infinity. Removing the vanishing projections beta_n B_3/sigma_B^2
preserves the limits. Therefore

\[
 \|\kappa_n\|_2\longrightarrow1,\qquad
 \|\kappa_n-\kappa_m\|_2^2\longrightarrow2
                  \quad(n\ne m,\ \min(n,m)\to\infty).   \tag{18}
\]

This bounded finite-state sequence has no Cauchy subsequence in the
physical L2 metric, hence none in the stronger L-infinity metric. The
added readouts are real analytic functions of B_3, so merely requiring
pointwise real analyticity does not repair this compactness failure.
No common derivative bound is asserted.

These are different stationary trajectories under different starting
states, not one nonconvergent trajectory and not canonical starts.
They refute precisely the ambient implication that bounded state
norms, finite effective vectors, fixed loss, stationarity, and individual
analyticity imply population-state precompactness.

## 7. Remaining implication and route disposition

The proved exact constraints still admit the compatible strict saddles
already constructed in the permitted sources. They do not yield a
uniform upper bound, finite trajectory length, compactness of the
specific canonical orbit, or avoidance of every saddle stable set.
The readout identity (9) is satisfied by those states, and the
subdiffusive estimate (4) permits unbounded motion.

Consequently this route does not establish that almost every population
initial state fits or that the single canonical initialized trajectory
fits every compatible triple. Nor does it construct a canonical
counterexample. A statement about almost every initial state additionally
needs a specified probability law on the population state space; there
is no finite-dimensional Lebesgue measure inherited merely from p=1.

Registry disposition: **blocked for a global basin theorem, complete for
the displayed universal identities and concrete compactness obstruction**.
The smallest missing bridge is an estimate for reached trajectories,
such as a genuine uniform state/regularity bound plus a proved gradient
inequality, or an invariant giving both saddle exclusion and escape
exclusion. A new such mechanism would reopen this route; ambient
boundedness or finite-dictionary assertions alone would not.
