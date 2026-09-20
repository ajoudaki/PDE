# Rank-two and full-rank variants on the exact nonlinear population model

Date: 2026-09-18. Lead-author integration of the frozen nonlinear construction
`rank_one_nonlinear_obstruction.md` and the subsequently requested, prompt-only
algebra in `rank_one_algebra_extensions.md`. The latter is an explicit
follow-up after the independent routes froze, not a fresh independent
nonlinear proof. No experiment, other study, or changed model is used.
These are ambient critical states, not reached initialized trajectories.

## 1. Shared exact state construction

Use every canonical convention and the complete proof of lower moment
realizability in Sections 2--3 of `rank_one_nonlinear_obstruction.md`.
In particular, for any three independent normalized input directions,
every prescribed triple of lower contractions with norm less than m_0
is realized by an actual finite odd field w, on the unchanged joint law
of (b_1,g), with bounded w-g. No free assignment of population moments is
being substituted for the closure equations.

Let e_1,e_2,e_3 be the upper coordinate basis and let f_1,...,f_6 be the
lower coordinate basis. Fix weights (1/4,1/4,1/2), labels (+1,+1,-1),
and signs sigma=(-1,+1,-1). Write the exact upper marks as (B_1,B_2,B_3).
As in the main proof set

\[
 H=\phi(B_1),\quad J=B_1\phi'(B_1),\quad
 U=H-\frac{E[HJ]}{E[J^2]}J,\qquad s^2=E[U^2]=E[UH]>0.
\]

Whenever Ma_i=sigma_i e_1, the choice

\[
 c=\frac{U}{2s^2}+B_2
\]

gives exactly

\[
 (f(x_1),f(x_2),f(x_3))=(-1/2,1/2,-1/2),\quad
 (p_i r_i)_{i=1}^3=(-3/8,-1/8,1/4),\quad
 d_i=\delta e_2,
 \qquad \delta=E[B_2^2]E[\phi'(B_1)]>0.
\]

Readout stationarity follows from sum_i p_i r_i sigma_i=0. The full
remaining equations are exactly those of the main proof. The loss is 3/4.
All marks and fields have the required parity, and c is bounded on the
canonical upper carrier. Omitting B_2 keeps the same predictions and makes
every d_i zero.

## 2. Only the left factors align; both relevant ranks are two

Choose 0<t<m_0/sqrt(5) and realize the actual lower contractions

\[
 a_1=t(-f_1+f_3),\quad a_2=t(f_1+f_3),\quad
 a_3=t(-f_1+2f_3).
\]

Set

\[
 M=t^{-1}(e_1 f_1^T+e_3 f_2^T).
\]

Then rank M=rank[a_1 a_2 a_3]=2, Ma_i=sigma_i e_1, and M^T e_2=0.
The three a_i are not all proportional and each is nonzero. With the
readout from Section 1 all three d_i are the same nonzero vector and

\[
 \sum_i p_i r_i a_i=\frac{-3a_1-a_2+2a_3}{8}=0.
\]

It follows that every individual middle-gradient term is nonzero rank one,
their sum vanishes, and the first-layer velocity is zero pointwise because
M^T d_i=0. Thus the exact nonlinear model realizes the common-left-factor
branch without common right factors. This works for every independent
input triple, because only the lower realization uses the input geometry.

## 3. Both the middle matrix and lower contraction matrix have full rank

Choose 0<t<m_0/sqrt(2), realize

\[
 a_1=t(-f_1+f_4),\quad a_2=t(f_1+f_5),\quad
 a_3=t(-f_1+f_6),
\]

and set

\[
 M=t^{-1}(e_1 f_1^T+e_2 f_2^T+e_3 f_3^T),\qquad
 c=\frac{U}{2s^2}.
\]

Then rank M=rank[a_1 a_2 a_3]=3, while Ma_i=sigma_i e_1. The lower
vectors are independent by their distinct f_4,f_5,f_6 coordinates.
Every d_i=0 by the exact upper expectation already checked in Section 1.
Readout stationarity and the same predictions are unchanged; the other
two gradients vanish individually. Thus even simultaneous full row rank
of M and independence of the three a_i do not exclude a positive-loss
critical state. Their composition can still identify the upper effective
vectors, and the derivative response can vanish.

## 4. The extra readout component need not be linear

In Section 1 and in the main construction one may replace B_2 by phi(B_2).
All parity, centering, predictions, and gradient cancellations remain exact.
Only the constant changes to

\[
 \delta=E[B_2\phi(B_2)]E[\phi'(B_1)]>0.
\]

The first expectation is strictly positive because phi=tanh has the same
sign as its nonzero argument and B_2 is nondegenerate. This variant gives
a readout expression that is bounded even when extended as a function to
all real upper coordinates: phi is bounded, as is z phi'(z). Boundedness
of the readout merely on the canonical carrier was already sufficient for
the state definition. This observation supplies no reachability theorem.

## 5. Scope

All constructions are on architecturally compatible data. Exact fitting
states exist, for example by the same moment lemma realizing a_i=epsilon f_i,
taking M=epsilon^{-1}[I_3 0], and choosing a readout in the span of the
independent centered features phi(B_i). Their Gram matrix is diagonal with
strictly positive entries by upper independence and nondegeneracy, so the
three desired predictions are attained by solving that diagonal system.

For each fixed small t or epsilon the chosen matrix is finite; no uniform
matrix bound as these auxiliary scales tend to zero is claimed. The
positive-loss critical states above are saddles by the own-study finite
critical-state theorem, and their compatibility or exact stationarity does
not require that saddle theorem. None is asserted to be approached by the
prescribed initialization. What fails is a static exclusion based on the
three gradient constraints, even with the displayed rank restrictions.
