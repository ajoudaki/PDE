# Exact diagnostics and a conservative bounded-block modification

28 September 2026. Fresh elementary derivations for this study. These are
initialization diagnostics and coupling statements, not a trained
block-to-canonical-dense approximation theorem.

## 1. Orthogonal scrambling preserves a finite-block reuse discrepancy

Let G be k by k with independent N(0,1/k) entries. Its columns g_j satisfy

E ||g_j||^4 = 1 + 2/k, and E <g_i,g_j>^2 = 1/k for i != j.

Consequently E tr((G^T G)^2) = k(1+2/k) + k(k-1)/k = 2k+1.
For D consisting of B independent such blocks, n=Bk,

    E tr((D^T D)^2)/n = 2+1/k.

For any orthogonal U,V, W=UDV^T has exactly the same singular values as D,
including when U,V depend on D. The preceding expectation therefore still
equals 2+1/k. A dense n by n Gaussian matrix of variance 1/n gives 2+1/n.
Orthogonal blocks instead give exactly 1, irrespective of k.

This invariant is a concrete check on repeated matrix/transpose contractions.
It does not establish a lower bound for nonlinear trained prediction error.
It shows that one cannot establish all the needed contraction identities
merely by spreading each block's entries over the whole matrix.

## 2. Matching singular moments does not remove every block correction

Consider one k by k block W=U Sigma V^T, where U,V are independent Haar
orthogonal matrices and Sigma is deterministic. Set Lambda=Sigma^2 and
assume tr Lambda=k, tr Lambda^2=s k. Let w be a row. Uniform-sphere moments
give

    E ||w||^4 = (k+2s)/(k+2),
    E sum_j w_j^4 = 3 E ||w||^4/(k+2).

For completeness, for a uniform unit vector v in R^k, sign symmetry and
rotational invariance imply E v_i^4 = 3 E v_i^2 v_j^2 for i != j.
Expanding (sum v_i^2)^2=1 then gives E v_i^4=3/[k(k+2)] and
E v_i^2 v_j^2=1/[k(k+2)]. Apply these first to a row of U and Lambda,
then to the independent right rotation V.

Let h_j be independent centered variables, independent of W, with
v=E h_j^2 and r4=E h_j^4 finite. Expanding z=sum w_j h_j gives exactly

    E z^4 = (k+2s)/(k+2) [3v^2 + 3(r4-3v^2)/(k+2)].

If s=2, its large-k expansion is

    E z^4 = 3v^2 + 3(r4-v^2)/k + O(k^-2).

An ordinary Gaussian k-block has exactly

    E z^4 = 3v^2 + 3(r4-v^2)/k.

Thus fixing the spectral second moment at its dense limiting value does not
remove the generic first forward fourth-moment correction in this particular
biorthogonal block class. It is a statement about a fresh independent input,
not trained adaptive responses. If v>0, cancelling the displayed first-order
coefficient requires s=(5-r4/v^2)/2, which generally changes the desired
spectral second moment. This restricted tradeoff does not exclude other
structured constructions or observable-level corrections.

## 3. Bounded Gaussian blocks: an exact whole-path coupling

Replace each Gaussian block G by an independent draw from its conditional
law given ||G||_op <= M. Take any fixed M satisfying M^2/8 > 2 log 9.
This proposal is Gaussian rejection sampling, not an orthogonal block.

An elementary net bound proves that the rejection probability p_k obeys

    p_k <= 2 exp[-k(M^2/8 - 2 log 9)].

Indeed, a 1/4-net of the unit sphere can be chosen with at most 9^k points
by the usual disjoint-ball volume argument. For a matrix G, approximation
of both unit vectors in sup |u^T Gv| shows that the net supremum is at least
||G||_op/2. For fixed net vectors u,v, u^T Gv is N(0,1/k). The Gaussian
tail bound and a union bound over the two nets give the displayed estimate.

Couple the original and modified blocks by retaining G if it passes the
test and otherwise drawing independently from the conditional law. The
modified marginal law is exactly the conditional Gaussian law. For N_blk
independent initialized blocks across all layers, the probability that the
two entire initializations differ is at most N_blk p_k.

Under any common deterministic evolution rule with unique solutions, the
two full paths are identical whenever the initializations agree. Hence their
path-law total variation distance is at most N_blk p_k. This holds on every
common existence interval, and on [0,infinity) if global solutions exist;
it requires no stability estimate. The same observation applies to a fixed
deterministic moment algorithm and its well-defined time integrator.

The modified block operator norm is at most M deterministically, independently
of the number of blocks. To transfer an event from the original law with
additional failure at most delta, it suffices that

    k >= log(2 N_blk/delta)/(M^2/8 - 2 log 9).

This transfer is NOT uniform in B at fixed k. Nor does it imply closeness in
unbounded-output expectation without integrability controls. It changes only
rare block initializations, so it cannot be claimed to cancel a generic 1/k
trained bias. Its purpose is to remove the maximum-initial-block-norm issue.

For n=Bk, fixed storage remains O(L n k), and fixed actions on all m samples
remain O(L m n k). Moving moments remain O(L m n q), with learned actions
O(L m^2 n q) and triangular moment evolution O(L m n q) via prefix sums.
Outer weights, input dimension, and response work are additional ordinary
costs. Exact singular-value checking costs O(k^3) per proposed block using
a dense SVD; preprocessing therefore costs O(L B k^3/(1-p_k)) in expectation.
The rejection cap is not a free preprocessing operation.

## 4. Literature inspected and its restricted role

Le, Sarlos, Smola, *Fastfood — Approximating Kernel Expansions in Loglinear
Time* (2013), full primary PDF:
https://proceedings.mlr.press/v28/le13.pdf . Lemma 2 gives fast-transform
storage/action costs; Lemma 3 and Theorems 4/6 concern random-feature kernel
expectations, variances and concentration. These do not establish a deep
trained matrix-reuse theorem. Fast transforms are an ingredient precedent.

Giles, *Multilevel Monte Carlo Path Simulation* (2008), full primary PDF:
https://people.maths.ox.ac.uk/gilesm/files/OPRE_2008.pdf . Section 3's
complexity result assumes weak-error and level-difference variance bounds;
Section 4 discusses Richardson extrapolation. These provide a design
template, not the missing neural trained-bias or coupled-variance estimates.
The debiasing report in this study derives the generic identities directly.

No neural experiment or prior study's theorem is used in these diagnostics.
