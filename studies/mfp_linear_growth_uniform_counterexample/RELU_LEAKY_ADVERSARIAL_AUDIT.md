# Adversarial audit: exact ReLU and leaky ReLU

## Verdict

The scalar Gaussian boundary calculation and the candidate reused-field
constant are correct.  For the RMS-normalized leaky ReLU

\[
 \phi(x)=a x_+ +b x_-,\qquad 0\le b<a,\qquad
 {a^2+b^2\over2}=1,
\]

they would give, after the response-intertwining bridge listed below, for
each fixed integer `t>=1`,

\[
 \Delta_t(h)=tD_{a,b}h|h|+o_t(h^2),
 \qquad D_{a,b}>0.                                      \tag{A.1}
\]

Consequently the cubic-subtracted fifth quotient is infinite already at
`t=1`.  This is stronger than finite super-`t^5` growth.

The corresponding theorem for the **complete width-first output is not yet
proved**.  First, the actual network has not been identified with an
indicator-valued adaptive reused-`W/W^T` DAG.  Second, even inside the
proposed DAG one must prove a nodewise one-source response-intertwining
identity and exhaust all same-source order-two sectors.  Thus (A.1) is a
rigorously computed candidate, not an unconditional network theorem.

## 1. Exact local boundary calculation

Near one switching surface `r=0`, write the first-order potential as

\[
 f=f_0+g_-^T(x-x_0)+c\,r_++O(|x-x_0|^2).
\]

Let `G` be the ascent metric and let

\[
 p=\nabla r^TGg_-,\qquad
 q=\nabla r^TG(g_-+c\nabla r)
\]

be the negative- and positive-side normal velocities.  For one pair of
Euler steps, put `r=hy`, freeze the displayed coefficients, and integrate
the fine-minus-coarse defect over `y`.  A negative-side point crosses only
when `p>0`, and a positive-side point crosses only when `q<0`.  Retaining
the smooth term `g_-^T(x-x_0)`, direct integration gives

\[
 J_1(p,q,c)=cpq\,\mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}. \tag{A.2}
\]

The word "or" denotes a union with multiplicity one.  In the attracting
case `p>0>q`, the two starting-side integrals add to one copy of `cpq`, not
two copies.  For example, with `p=1,q=-2,c=-3/2`, they are `9/4` and `3/4`,
whose sum is `3=cpq`.

Iterating the two piecewise translations shows exactly

\[
 J_t(p,q,c)=tJ_1(p,q,c).                         \tag{A.3}
\]

This was independently checked by partitioning at every preimage of zero;
it remains valid in the attracting case, including repeated visits to the
same surface.  Distinct switching surfaces must not be substituted for
those repeated visits.

If the normal coordinate has a continuous density `rho` at zero, scaling
`r=hy` gives the right-sided boundary contribution

\[
 t\rho(0)J_1h^2+o_t(h^2).                       \tag{A.4}
\]

The smooth part of the potential is essential in (A.2).  Keeping only the
hinge value gives a different and incorrect coefficient whenever a
background normal velocity is present.

## 2. Initialization law at a top gate

For the two-hidden-layer network, let

\[
 H_j=\phi(u_j),\quad
 z_i={1\over\sqrt n}\sum_jW_{ij}H_j,\quad
 c_i=A_i\phi'(z_i).
\]

The initial normal velocity of `z_i` is

\[
 V_{i,n}=Q_n c_i+\sum_kK_{ik}c_k,
 \quad Q_n={1\over n}\sum_jH_j^2,
 \quad K_{ik}={1\over n}\sum_jW_{ij}W_{kj}\phi'(u_j)^2. \tag{A.5}
\]

Separate the diagonal summand.  Since

\[
 Q_n\longrightarrow1,\qquad K_{ii}\longrightarrow1,
\]

the one-sided explicit terms tend to `2bA` and `2aA`.  Conditional on the
lower variables and row `i`, the off-diagonal summands in (A.5) are centered
and independent over `k`.  Their conditional variance sum tends to

\[
 e={a^4+b^4\over2},
\]

and their fourth-moment Lindeberg sum tends to zero.  The covariance between
the two row projections defining `K_ik` and `z_k` is `O(n^-1)`, so the
off-diagonal limit is independent of the target `A,z`.  Hence

\[
 p=Y+2bA,\qquad q=Y+2aA,qquad
 A\sim N(0,1),\quad Y\sim N(0,e),               \tag{A.6}
\]

independently.  The limiting top preactivation is standard Gaussian.

After summing the `n` top surfaces against the `1/n` output normalization,
the hinge coefficient is `(a-b)A`.  Equations (A.2)--(A.6) therefore give

\[
 D_{a,b}=\gamma(0)\,\mathbb E\!
 \left[(a-b)A pq\,
 \mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}\right]. \tag{A.7}
\]

Its sign is strict.  The unconditional expectation of `(a-b)Apq` is zero,
so

\[
 D_{a,b}=-\gamma(0)(a-b)\mathbb E
 [Apq\mathbf1_{\{p\le0\le q\}}].               \tag{A.8}
\]

On the displayed wedge, `q-p=2(a-b)A>=0`, whence `A>=0` and `pq<=0`.
Both inequalities are strict on a positive-measure Gaussian set.  Thus
`D_(a,b)>0`.

At a lower gate the one-sided velocities are `bB,aB` with centered
Gaussian `B`.  Its expected coefficient is proportional to
`(a-b)ab E[B^3]=0`; for ReLU it vanishes pointwise because `b=0`.

For normalized ReLU, `(a,b)=(sqrt(2),0)` and `e=2`.  Evaluation of the
Gaussian wedge gives

\[
 D_{\rm ReLU}={\sqrt2\over\pi}
 \left(1-{1\over\sqrt5}\right).                 \tag{A.9}
\]

## 3. Parity and the scalar control case

Let `S(u,W,A)=(u,W,-A)`.  The exact finite-width update obeys

\[
 T_hS=ST_{-h},\qquad f_n(S\theta)=-f_n(\theta).
\]

Gaussian initialization is invariant under `S`, so every finite-width and
every existing width-limit output obeys `F_k(-h)=-F_k(h)`.  Thus the
right-sided `D h^2` term extends as `D h|h|`, consistently with parity.

The scalar model `f(A,z)=A z_+` is an important negative control: it has no
off-diagonal field `Y`, and its inactive velocity is zero, so (A.2) vanishes.
In fact, for `h>0`,

\[
 F_1(s)={s^2/2+s(\pi-\arctan s)\over\pi},
\]

\[
 F_2(h)=(1+h^2)^2F_1\!\left({2h\over1+h^2}\right),
\]

and therefore

\[
 F_2(h)-F_1(2h)=2h^3-{32\over3\pi}h^6+O(h^8).   \tag{A.10}
\]

There is no scalar `h^4` term.  Formula (A.10) rules out attributing the
network obstruction to a frozen top neuron; the aggregate reused field in
(A.5) is indispensable.

## 4. Fatal gap in the actual-network proof

The proposed nonsmooth bridge asserts, for every gate queried by a fixed
schedule,

\[
 \sup_nP(|X_n|\le\varepsilon,|V_n|\le R)
 \le C_{t,R}\varepsilon.                       \tag{A.11}
\]

This is false for ReLU.  At initialization, if all lower preactivations are
negative then all `H_j=0`, and hence every top `z_i=0`.  This event has
probability `2^-n`; for `n=1` it gives an atom of mass `1/2`, contradicting
(A.11).  For leaky ReLU at `n=1`, a product-normal preactivation has a
logarithmic density singularity, so a uniform linear small-ball estimate
still does not follow.

One could replace `sup_n` by a sufficiently-large-width statement, but the
following must then actually be proved:

1. ramp removal is uniform over those widths through every adaptive reused
   row and column query;
2. all limiting gate laws needed by the finite schedule are non-atomic,
   with quantitative small-ball control;
3. after summing over the `O(n^2)` pairs of distinct gate tubes, their total
   normalized interaction is `o(h^2)` uniformly in large width;
4. the velocity tails admit the uniform-integrability removal required
   after the tube calculation.

Merely saying that each limiting query has a Gaussian innovation does not
prove these four statements.  In particular, the query is adaptive and
shares the same `W/W^T`; the innovation and its variance have to be produced
by the full chronological conditioning argument.  The present project has
not supplied that nonsmooth, width-uniform induction.  Therefore the
actual-network version of (A.1) must remain conditional.

## 5. Smoothing audit

A smooth ramp approximation does not transfer a fifth-remainder theorem to
exact leaky ReLU.  Its derivative is separated from the discontinuous slope
by at least `(a-b)/2` in uniform norm, so the existing `d_1` stability lemma
does not apply.  Moreover, if fixed-step ramp outputs converge at two fixed
rates to `Dh^2` and `D(h/2)^2`, then

\[
 \inf_\kappa\max\left\{
 { |Dh^2-\kappa h^3|\over h^5},
 { |D(h/2)^2-\kappa(h/2)^3|\over(h/2)^5}
 \right\}
 ={4D\over5h^3}.                               \tag{A.12}
\]

Thus no smoothing family can have a fifth-remainder constant uniform through
the kink limit.  Expanding first at fixed ramp width and then shrinking the
ramp is the wrong order of limits.

The compact-bump ladder can nevertheless be grafted onto a **smooth**
softplus or leaky-softplus baseline.  The insertion theorem requires an
exact affine tail, whereas softplus is only asymptotically affine.  Choose a
smooth cutoff and replace the baseline `s` by

\[
 s_R=L+\chi_R(s-L),                             \tag{A.13}
\]

where `L` is its positive affine asymptote, `chi_R=1` to the left of `R`,
and `chi_R=0` to the right of `R+1`.  Exponential tail convergence gives
`d_1(s_R,s)<=C exp(-R)`, while `s_R` is exactly affine on every future bump
support.  The audited compact insertion and diagonal then apply.  For pure
softplus the derivative has infimum zero; add an arbitrarily small residual
linear leak first if a positive global lower slope is required.  This
produces a pathological smooth activation arbitrarily `d_1`-close to a
(leaky-)softplus, but it is not a proof about exact ReLU.

## 6. Audit of the proposed two-stage closure

The correct limit-order repair is to prove state evolution at each fixed
nonzero `h` first, and to do the kink-tube analysis only in the resulting
width-limit program.  This removes every need for a finite-width tube bound
uniform as `h` tends to zero.  It would close the actual-network theorem,
but only after the following two lemmas are proved.

### Lemma A: fixed-`h` a.e.-continuous alternating state evolution

For each fixed finite schedule and fixed nonzero `h`, prove:

1. the exact chronological Gaussian conditioning theorem for every adaptive
   `W` and `W^T` query, retaining all learned rank-one terms;
2. joint empirical-measure convergence for coordinate maps of polynomial
   growth that are continuous outside finitely many gate hyperplanes;
3. zero mass at every limiting queried gate, so the continuous-mapping
   extension really applies to every indicator;
4. singular-Gram-safe regression, by deterministic population-rank
   orthogonalization or an equivalent pseudoinverse-free residual-span
   construction;
5. convergence of every empirical Gram and regression cross moment, with
   polynomial moment bounds and uniform integrability for the terminal
   annealed output;
6. a definition of all responses by Gaussian regression covariances, and a
   proof that this regression DAG equals the proposed ReLU DAG.  Ordinary
   Stein differentiation of `phi'` is not available.

Only limiting non-atomicity is needed here: if `X_n` converges in law to `X`
and `P(X=0)=0`, then the indicator query follows by the a.e.-continuous
mapping theorem and uniform integrability.  The false estimate (A.11) is not
needed.  Non-atomicity itself is a proof obligation, not a consequence of
the words "Gaussian innovation": when a residual variance vanishes, one
must show that a remaining continuous source prevents an atom.

### Lemma B: boundary theorem inside the limiting DAG

After Lemma A, construct the fine and coarse limiting programs on one joint
Gaussian source space and prove:

1. a response-aware local-gradient intertwining identity: after freezing one
   initial gate source, the **complete** regression DAG, including every
   reused-adjoint path, has the full local-potential expression in (A.2);
   retaining only the terminal hinge value is not enough;
2. every state remains `O_t(h)` from initialization in the required `L^p`
   norms;
3. a one-source conditional coarea/tube lemma whose frozen value is (A.2),
   including domination of the coefficient and velocity tails;
4. an equivalence relation on source histories: all chronological visits to
   one initial gate are grouped by (A.3), while two genuinely distinct
   initial gate sources have bounded joint density and tube probability
   `O_t(h^2)`;
5. the total distinct-source interaction is `o_t(h^2)` in the population
   DAG;
6. the smooth-cell order-two term has zero expectation under the readout
   involution, and all truncation tails can be removed after `h` tends to
   zero.

The singular covariance at `h=0` does not require differentiating a square
root.  Couple all time copies by their full Gram matrix.  For example,

\[
 E|\xi_s-\xi_0|^2
 =Q_{ss}+Q_{00}-2Q_{s0}
 =E|H_s-H_0|^2,                                \tag{A.14}
\]

so an inductive `L^2` state bound gives the needed `O(h)` Gaussian-field
coupling even when the Gram loses rank.  The same identity applies to the
backward fields.  Individual inverse-Gram regression coefficients should
not be used in this argument; only their basis-invariant aggregate
projections are stable.

Thus the two-stage proposal is mathematically sufficient and materially
cleaner, but neither Lemma A nor Lemma B is presently written in complete
form in the study.  Stating "adaptive conditioning plus a.e. continuity"
does not by itself promote the operator calculation to the actual network.
