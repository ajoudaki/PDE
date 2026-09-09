# Causal Source Compression Calculus

## Status

This note records a candidate completion mechanism discovered after the
Yudovich--Orlicz reduction.  Its finite-dimensional Gaussian and deterministic
approximation lemmas are proved below.  The full depth-three theorem remains
under adversarial audit until the coupled compression estimate and the
fixed-program branch argument have both been checked line by line.

The central idea is not to prove a tail for an arbitrary adaptive query.
Instead, replace the continuum of queries to a persistent Gaussian source by
a finite causal orthonormal dictionary, with a certified energy defect.  The
retained query outputs have a uniform diffuse tail by exact Gaussian
conditioning.  Osgood stability then turns the energy defect into a vanishing
flow defect without a clip-dependent exponential.

**Audit correction.**  The preceding conclusion is only conditional.  A
fixed compression tolerance gives a finite tail constant, but Osgood
stability requires quantitative control of that constant as the tolerance
vanishes.  The available Gram--Schmidt induction gives no such control and
can be far too large.  Sections 6--9 therefore describe a candidate
implication, not a proved mesh-removal or autonomy theorem.  Section 11
records the hostile audit at its actual claim level.

## 1. Oriented source dictionaries

Let `H_n=R^n` with normalized inner product, and let
`Gamma_ij=n^(-1/2)g_ij`.  Maintain two normalized-orthonormal families

\[
 E^+=(e_1^+,\ldots,e_a^+),\qquad
 E^-=(e_1^-,\ldots,e_b^-),
\]

in the domain and codomain of `Gamma`, together with the exact observations

\[
 U_k=\Gamma e_k^+,
 \qquad
 V_l=\Gamma^*e_l^-.
\tag{1}
\]

For a new forward input `x`, form

\[
 x_\perp=x-P_{E^+}x.
\]

If `||x_perp||_n <= delta`, use the compressed action

\[
 \widehat\Gamma x=\sum_{k=1}^a U_k\langle e_k^+,x\rangle_n.
\tag{2}
\]

Otherwise append `e_{a+1}^+=x_perp/||x_perp||_n`, make the exact causal
query `U_{a+1}=Gamma e_{a+1}^+`, and (2) is then exact on `x`.  The transpose
rule is identical with `+` and `-` exchanged.  On
`||Gamma||_op <= K`, every discarded action obeys

\[
 \|\Gamma x-\widehat\Gamma x\|_n\le K\delta,
 \qquad
 \|\Gamma^*b-\widehat\Gamma^*b\|_n\le K\delta.
\tag{3}
\]

Forward and transpose dictionaries belong to the same source.  No matrix is
freshened.

## 2. Exact orthogonal innovation rule

Let the current dictionaries and observations be part of the causal history.
If `e^+` is measurable with respect to that history and orthogonal to the
old forward dictionary, exact Gaussian projection gives

\[
 \Gamma e^+
 =\sum_{l=1}^b e_l^-\langle V_l,e^+\rangle_n
   +P_{E^-}^\perp g^+,
\tag{4}
\]

where, conditionally on the history, `g^+` has iid `N(0,1)` coordinates.
After observing (4), a new causal `e^-` orthogonal to the old transpose
dictionary satisfies

\[
 \Gamma^*e^-
 =\sum_{k=1}^{a+1}e_k^+\langle U_k,e^-\rangle_n
   +P_{E^+}^\perp g^-.
\tag{5}
\]

The two innovations in successive legal calls are the residual pieces of
one conditionally fresh Gaussian matrix; (4)--(5) are not an assertion that
all innovations across time are independent.

On `||Gamma||_op<=K`, every scalar coefficient in (4)--(5) has absolute
value at most `K`.  Each coordinate of either projected innovation has
conditional variance at most one.  Orthogonalizing the new input is what
removes recursion through old outputs of the same orientation.

## 3. Coordinate envelopes for the dictionaries

Suppose every forward input obeys `|x_i|<=c` and `||x||_n<=c`.  Whenever a
pivot is admitted its residual norm is at least `delta`.  If `C_m^+` bounds
the coordinates of the first `m` normalized forward pivots, Gram--Schmidt
gives the deterministic recursion

\[
 C_{m+1}^+
 \le \delta^{-1}\left(c+c\sum_{k\le m}C_k^+\right).
\tag{6}
\]

Thus every finite forward dictionary is coordinatewise bounded by a
computable constant depending only on `(c,delta,m)`.

For the top transpose inputs in the arctangent network,

\[
 b_3=A\,d(z_3),
 \qquad
 |b_{3,i}(t)|\le |A_i(0)|+\frac\pi2T.
\tag{7}
\]

On a normalized energy localization, all Gram--Schmidt coefficients are
bounded.  Induction analogous to (6) gives

\[
 |e_{m,i}^-|
 \le C_{\delta,m,T}\bigl(|A_i(0)|+1\bigr).
\tag{8}
\]

Consequently a uniformly chosen coordinate of every finite transpose pivot
has subgaussian moment growth, uniformly in width and in any hidden
`r_2` clip.  This conclusion uses the seed domination (7), not a maximum
coordinate bound.

Combining (4)--(8) inductively yields

\[
 \sup_{p\ge2}p^{-1/2}
 \left(
 \mathbb E\frac1n\sum_i|U_{k,i}|^p
 \mathbb E\frac1n\sum_i|V_{l,i}|^p
 \right)^{1/p}
 \le C_{K,T,\delta,M}
\tag{9}
\]

for every dictionary of size at most `M`.  The constant is independent of
width and of the hidden self-clip.

## 4. The compressed depth-three flow

Compress only the top source `Gamma_2`.  The lower source `Gamma_1` remains
exact.  This is sufficient because the uncontrolled multiplier is

\[
 r_2=G_2^*b_3.
\]

Choose a deterministic coarse grid `0=t_0<...<t_M=T`.  At `t_j`, causal
order is:

1. compute the current `x_2` from the lower state;
2. pivot/query its forward residual and compute the top forward pass;
3. compute `b_3`;
4. pivot/query its transpose residual;
5. continue the ODE using only the stored source actions until `t_(j+1)`.

Between grid points use the orthogonal projections (2), not a newly sampled
source.  At all times the learned operator

\[
 H_2(t)=\int_0^t b_3(s)\otimes_nx_2(s)\,ds
\]

is retained exactly.

For this compressed flow,

\[
 \widehat r_2(t)
 =\sum_{l=1}^bV_l\langle e_l^-,b_3(t)\rangle_n
 +\int_0^t x_2(s)\langle b_3(s),b_3(t)\rangle_n\,ds.
\tag{10}
\]

The coefficients in the first term are bounded by the energy of `b_3`.
The second term is coordinatewise bounded because `x_2` is bounded.  From
(9), on every physical localization,

\[
 \sup_{R}\sup_n\sup_{p\ge2}p^{-1/2}
 \left\|\sup_{t\le T}|\widehat r_2(t)|\right\|_{p,*}
 \le C_{T,\delta}.
\tag{11}
\]

Here `R` denotes an optional clip used only in
`b_2=d(z_2)kappa_R(r_2)`.  Formula (11) is proved for the compressed query;
it is not assumed for the exact query.

## 5. Uniform time modulus of the query inputs

The usual energy bounds are independent of the hidden clip because

\[
 \|b_3\|_n\le\|A\|_n,
 \quad
 \|r_2\|_n\le\|G_2\|_{op}\|b_3\|_n,
 \quad
 \|b_2\|_n\le\|r_2\|_n.
\tag{12}
\]

Writing `H_1=diag(d(u)^2)`, direct differentiation gives

\[
 \dot z_2
 =\bigl(\|x_1\|_n^2I+G_1H_1G_1^*\bigr)b_2,
\tag{13}
\]

and hence `x_2` is uniformly Lipschitz in normalized energy on every
localized compact-time envelope.

Likewise,

\[
 \dot z_3=\|x_2\|_n^2b_3+G_2\dot x_2,
\qquad
 \dot b_3=d(z_3)x_3+A d'(z_3)\dot z_3.
\tag{14}
\]

Although the last product need not be controlled in normalized `L^2`, it is
controlled in normalized `L^1`:

\[
 \|A d'(z_3)\dot z_3\|_{1,n}
 \le \|A\|_{2,n}\|d'(z_3)\dot z_3\|_{2,n}
 \le C_T.
\tag{15}
\]

Also, by (7),

\[
 |b_{3,i}(t)-b_{3,i}(s)|
 \le2\bigl(|A_i(0)|+\tfrac\pi2T\bigr).
\]

On the empirical fourth-moment localization, interpolation between `L^1`
and `L^4` gives

\[
 \|b_3(t)-b_3(s)\|_{2,n}
 \le C_T|t-s|^{1/3}.
\tag{16}
\]

Thus a mesh satisfying `h<=c_T delta^3` makes both current query inputs lie
within `C delta` of their last grid values.  Since that grid value was either
pivoted or discarded with residual at most `delta`, every between-grid
source defect is `O(K delta)`.

The same estimates hold for the compressed flow: projection has operator
norm at most one, and its source actions are bounded by the same localized
source norm.

## 6. Compression stability

Use the state `(A,w,H_1,H_2)` with `w=u+u^3/3`.  All deterministic network
operations are energy-Lipschitz on the physical localization except the two
activation-gated products

\[
 b_3=A d(z_3),
 \qquad
 b_2=r_2d(z_2).
\]

Compare the exact flow to the compressed flow using the compressed fields as
the reference multipliers.  The readout satisfies a seed-subgaussian bound,
and (11) supplies a subgaussian bound for the compressed `r_2`.  Lemma 2.1 of
`YUDOVICH_ORLICZ_STABILITY.md` therefore gives

\[
 D(t)\le C_T\delta+
 C_{T,\delta}\int_0^t
 D(s)\sqrt{\log(eM/D(s))}\,ds.
\tag{17}
\]

The constant depends on the fixed compression tolerance, but not on width or
on an `r_2` clip.  For each fixed dictionary tolerance, Bihari gives a
computable bound

\[
 \sup_{t\le T}D(t)\le\omega_{T,C_{T,\delta}}(\delta).
\tag{18}
\]

It is **not automatic** that the right side tends to zero: the crude
Gram--Schmidt/tail induction permits `C_(T,delta)` to grow much faster than
`sqrt(log(1/delta))`, which is the scale allowed by the subgaussian Osgood
formula.  Thus the current argument removes circular appeal to a tail of the
exact adaptive transpose query but leaves a quantitative complexity-versus-
defect gate:

\[
 \boxed{
 \omega_{T,C_{T,\delta}}(\delta)\longrightarrow0
 \quad\text{must be proved, not inferred from finiteness at fixed }\delta.
 }
\tag{19}
\]

In the bad-product decomposition, the exact multiplier equals the compressed
multiplier plus a state difference, and the latter is an ordinary energy
term.

Equation (17) is the main coupled estimate still requiring a line-by-line
audit in the full product state, especially its matrix/operator components
and the compact-time supremum.

## 7. Fixed-compression completion

For fixed `delta`, the coarse dictionary has at most `2(M+1)` vectors.  Add
smooth clips to the readout and hidden multiplier temporarily.  Between
coarse grid times the compressed vector field is dimension-uniformly
Lipschitz.  At each grid time, Gram--Schmidt is stable whenever an admitted
residual is separated from zero by the pivot threshold.

Fine Euler discretization is therefore uniform in width.  For fixed coarse
grid, pivot pattern, clips, and fine step count, the recursion is a fixed
persistent Gaussian program.  MFP evaluates it using the exact same
`Gamma_2/Gamma_2^*` and `Gamma_1/Gamma_1^*` pairs.

To avoid a discontinuous boundary, choose a pivot threshold in
`[delta,2delta]` outside the finite set of limiting residual norms generated
at the coarse calls.  Equivalently, use two-threshold hysteresis and retain
the ambiguous finite branches until their limits separate.  Every discarded
residual is then at most `2delta`, so the approximation order is unchanged.

The compressed readout and hidden multiplier have the uniform projective
tails needed by the Osgood theorem.  Hence both temporary clips can be
removed after the fine-mesh and width limits.  Denote the resulting
compressed limit character by `chi^(delta)`.

## 8. Candidate depth-three completion theorem

If the audited version of (17) holds **and** the quantitative gate (19) is
proved, then:

1. every fixed `delta` compressed flow has a unique compact-time width limit;
2. (18)--(19) make the exact finite-width flow and compressed flow uniformly
   close;
3. `chi^(delta)` is Cauchy as `delta->0` by comparing both compressed flows
   through the same exact finite-width flow;
4. the exact flow converges to the projective character `chi`;
5. predictor and raw-kernel convergence follow from the same state estimate,
   physical energy bounds, and uniform integrability;
6. the finite semigroup/restart identity passes to `chi`, while dictionaries
   disappear as approximation artifacts.

The master order of approximation is

\[
 \text{localize source/seed energies}
 \;\to\;
 \text{fix }\delta
 \;\to\;
 \text{fix temporary clips and fine mesh}
 \;\to\;
 n\to\infty
 \;\to\;
 h_{fine}\to0
 \;\to\;
 \text{remove clips}
 \;\to\;
 \delta\to0
 \;\to\;
 \text{remove localization}.
\tag{20}
\]

This construction supplies a finite approximation and a local error
certificate.  It does not store a two-time kernel or an unbounded response
registry in the limiting state.

## 9. Depth recursion and fixed-input colors

The source-compression rule is edge-local.  At a deeper edge, forward pivots
are still built from bounded arctangent features.  Starting at the top,
transpose pivots inherit a projective subgaussian envelope from the preceding
compressed transpose output, because multiplication by `d` is bounded and a
finite Gram--Schmidt recursion preserves the envelope.  Equations (4)--(5)
then propagate the same type to the next edge.

For every fixed depth this adds one source color and two finite dictionaries
per edge, not a new convergence oracle.  What must still be written for a
general-depth theorem is the induction giving a positive normalized-energy
time modulus for every backprop query path; its exponent may deteriorate with
depth but remains usable for a finite coarse grid.

A fixed finite training set only adds a finite sample color to each
dictionary.  Pivoting rather than inverse-Gram assumptions makes identical,
symmetric, or singular input configurations admissible.

## 10. Current kill gates

The candidate is rejected if any of the following occurs in the hostile
audit:

1. a pivot vector is not measurable before its oriented source call;
2. adaptive Gram--Schmidt destroys the coordinate envelope (8) or the
   innovation estimate (9);
3. either query path lacks the uniform time modulus (13)--(16);
4. the coupled exact/compressed difference cannot be reduced to (17) without
   reintroducing the unknown exact-query tail;
5. the retained-query moment constant grows too quickly relative to the
   discarded energy defect for (19) to hold;
6. the fixed pivot branches cannot be reconciled with fixed-program MFP;
7. raw-kernel uniform integrability requires an unproved stronger tail;
8. a new uncontrolled type appears immediately at depth four.

## 11. Hostile-audit disposition

The fixed-query Gaussian rule survives, but the proposed completion does
not.  The precise disposition is as follows.

### 11.1 What survives

The legal filtration order is

\[
 e_k^X\ \longrightarrow\ U_k=\Gamma e_k^X
 \ \longrightarrow\ e_k^B\ \longrightarrow\ V_k=\Gamma^*e_k^B.
\]

With this sequential order, (4)--(5) are exact conditional Gaussian
identities.  They must not be read as declaring both innovations fresh and
independent simultaneously.  At every fixed tolerance, fixed number of
queries, fixed causal branch, and deterministic seed/operator-energy stop,
the dictionary induction gives finite coordinate-moment constants.

The time regularity estimates also survive, with one scheduling caveat:
after a new forward observation the compressed `b_3` may jump, so the
transpose dictionary must be refreshed immediately; the Holder estimate is
then used only until the next grid call.

### 11.2 Quantitative obstruction

Taking a grid spacing of order `delta^3` permits order `delta^{-3}` pivots.
The elementary coordinate recursion can produce constants of the scale

\[
 K_\delta\lesssim (C/\delta)^{C\delta^{-3}},
\]

and even an orthogonal-energy estimate exposes leverage growing with the
number of pivots.  In contrast, if the multiplier is subgaussian, the
Yudovich--Osgood comparison with initial/source defect `epsilon_delta`
requires a condition of the form

\[
 K_\delta=o\!\left(\sqrt{\log(1/\epsilon_\delta)}\right).
\]

For a general subexponential exponent `beta<1`, the required condition is

\[
 K_\delta=o\!\left(\log(1/\epsilon_\delta)^{1-\beta}\right).
\]

Thus fixed-`delta` finiteness cannot justify (19).  Proving the needed bound
would require a genuinely dimension-free adaptive decoupling or
leave-one-coordinate theorem; that theorem is close in substance to the
original adaptive-source problem.

### 11.3 What the compressor does not approximate

The unseen source block is

\[
 P_{E^-}^{\perp}\Gamma P_{E^+}^{\perp}.
\]

For any fixed query count its operator norm remains order one as width tends
to infinity.  Hence the finite reconstruction never approximates the full
matrix in operator norm.  A valid comparison must keep the same latent
`Gamma` in both formal systems and compare only the learned increment and
the source actions actually visited by the dynamics.

### 11.4 Branch and autonomy gaps

A hard pivot predicate can fail to converge when a limiting residual lands
on its threshold.  A no-tie theorem, randomized generic threshold, or a
smooth/hysteretic replacement with its own residual certificate is still
needed.

Finally, the query dictionary is a causal transcript.  Showing convergence
of trajectories started at zero does not prove that, after discarding this
transcript, the proposed current typed character determines future source
actions.  Projective consistency supplies a process law, not a semigroup.
A separate Markov-sufficiency theorem must identify a present-time state
that determines the conditional source law and prove restart uniqueness for
the correlated state obtained at an intermediate time.

Accordingly this route is retained as an exact finite-query language and a
source of counterexamples to naive fresh-Gaussian reasoning.  It is not a
completed convergence calculus and is not presently a meaningful reduction
of the depth-three bottleneck.
