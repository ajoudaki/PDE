# Independent complete proof review B2

**Verdict: CLEAN. No required correction found in the supplied version.**

The exact finite representation, its converse, the four query derivative bounds,
the supplied-path covering estimate, and the retained-memory continuity bounds
are valid under their stated hypotheses. The supplied text expressly leaves
causal finite-query construction, nonlinear solution stability, population
identification, and derivative/kernel convergence open; this review does not
upgrade those claims.

## Scope, isolation, and full-read ledger

This was an independent review of only the frozen mathematical inputs under
/tmp/pde_query_review_2. No checkout, studies, history, previous reviews, other
tasks, or external mathematical sources were inspected. No delegation, training,
trajectory integration, or numerical experiment was used. The checks below are
direct finite-dimensional algebra and analysis.

The complete solve-math-rigorously and investigate-conjectures skills were read
from /etc/codex/skills, together with research-contract.md, adversarial-audit.md,
and evidence-ledger.md from the latter skill's references. No experimental or
multi-route proof-search procedure was needed for this bounded proof audit.

All supplied mathematical files were read in full, with line-numbered output:

| Input | Lines read | Bytes | SHA-256 before and after |
|---|---:|---:|---|
| docs/NOTATION.md | 1–98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/finite_dynamics.md | 1–214 | 8355 | 486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c |
| docs/integrated_queries.md | 1–242 | 10764 | fbe02d7d7c85167242cca00393fdb01f62c2357e5d94900cc1b439157b93850e |

This is all 554 mathematical lines, not a selected-hunk or change-only review.
INPUTS.json was also read in full. Its SHA-256 before and after is
521dafbbbc12bbc70de988503c2923afcc63480554fd15ad51d42692f959592a.
The three document hashes match that manifest. All four input files were
rehashed after this report was written, and remained unchanged.

## Canonical conventions and complete finite-dynamics dependency

The canonical model uses L hidden layers, first preactivation W^(1)x/sqrt(d),
unscaled hidden matrix actions, and readout a^T h^(L)/n. The backward vectors
are n times derivatives with respect to preactivations and exclude the
residual. The finite RMS and pairings throughout the reviewed chapter are
explicitly ||v||_2/sqrt(n) and u^T v/n. The matrix norm is the ordinary operator
norm. Thus a rank-one matrix b'h^T/n has operator norm
||b'||_2 ||h||_2/n, without any extra normalization.

I checked all of finite_dynamics.md, including statements not directly needed
for the integrated-query bounds:

1. **Gradients and mobilities, lines 9–64.** Backpropagation starts with
   grad_z f = a odot phi'(z)/n and propagates by the actual matrix transpose.
   The three weight gradients are delta x^T/(n sqrt(d)),
   delta h^T/n, and h/n. Applying loss gradient (2/m) sum r grad f
   and mobilities n kappa_1, kappa_ell, n kappa_(L+1) gives exactly
   equation (2). Every raw-GD block must use the same old state, as stated.
   Empty middle-layer ranges at L=1 cause no problem.

2. **Kernel normalization, lines 66–109.** For the first block,
   (n kappa_1)/(n^2 d) times (delta_a^T delta_b)(x_a^T x_b)
   equals kappa_1 G_ab (delta_a^T delta_b/n). For a middle block,
   kappa_ell/n^2 times the two dot products gives the two normalized
   pairings in (3). For the last block, n kappa_(L+1)/n^2 gives
   kappa_(L+1)(h_a^T h_b/n). Each is a Gram kernel in a positive
   metric, hence positive semidefinite. Summing blocks yields
   dot f = -(2/m) K r and
   dot L = -(4/m^2) r^T K r = -||D^(-1/2) dot theta||_2^2.
   Integration gives (5) with exactly the displayed reciprocal mobilities.

3. **Global finite-width flow, lines 111–153.** C^2 activations make the
   finite loss C^2 and its vector field locally Lipschitz. A ball on which
   the field is bounded by M and Lipschitz with constant K gives a
   contraction on continuous curves when the time interval is smaller
   than the ball radius divided by M and has K times length less than one.
   The energy identity and Cauchy–Schwarz give (6). At a hypothetical finite
   maximal time, that estimate makes the parameter path Cauchy. Since D
   is positive definite at fixed n, its limit is a finite Euclidean state
   and the same local construction extends the flow. Thus no bounded
   activation assumption or GD stability assertion is hidden in the proof.
   Restricting (6) to each block gives (7), with sqrt(n) only in the
   first and last blocks. The middle Frobenius bound also bounds its
   operator norm. The corresponding increment estimate between s and t
   uses t-s and the initial-loss bound.

4. **Width-independent finite-horizon estimates, lines 155–189.**
   The first-block Frobenius norm divided by sqrt(n), the readout RMS,
   and the middle operator norms are bounded by their initial values
   plus (7). Multiplying by ||x_a||_2/sqrt(d) yields the first
   preactivation RMS bound. Hidden matrix multiplication propagates it.
   The scalar estimate |phi(z)| <= |phi(0)| + sup|phi'| |z|
   transfers it to activation RMS. Multiplication by bounded activation
   derivatives and reverse operator actions yields the backward RMS
   induction. Cauchy–Schwarz then controls every kernel entry.
   Fixed depth, fixed data dimension, bounded initial loss, and the stated
   initial norms are essential and are present.

5. **Initialization event, lines 191–209.** Under the canonical independent
   Gaussian initialization, the first squared Frobenius norm divided by n
   has mean d and variance 2d/n. Chebyshev's inequality therefore gives
   its convergence to d in probability. The readout squared RMS has mean
   n^(-2), so Markov's inequality gives convergence to zero. A maximal
   1/4-separated unit-sphere set covers the sphere and has at most 9^n
   elements: the disjoint balls of radius 1/8 lie inside a radius-9/8 ball.
   Approximating each of the two unit vectors in a bilinear form changes
   it by at most (1/2)||W||_op, so
   ||W||_op <= 2 max_net |u^T W v|. A fixed net form has distribution
   N(0,1/n). Its moment-generating function is exp(lambda^2/(2n));
   optimizing the exponential Markov bound gives
   P(|u^T W v| > M/2) <= 2 exp(-n M^2/8).
   Union over at most 9^(2n) pairs gives the exact displayed estimate.
   Choosing M with M^2/8 > 2 log 9 and using fixed depth proves the
   claimed high-probability event. Forward bounds and the readout
   Cauchy–Schwarz bound then control initial loss.

6. **Scope, lines 211–214.** These finite estimates do not establish
   bounded multiplication by population coordinates, a population limit,
   source identification, or response stability. The final caveat is valid.

The notation contract also distinguishes the stored small readout from
order-one readout, physical time from feature time and proof meshes, matrix
transpose from a population adjoint, and finitely many function fields from
a finite scalar state. No contradictory convention occurs in the primary
chapter.

## Exact L=3 arctangent representation and converse

The primary chapter fixes one scalar input and label, both equal to one.
Thus d=m=1, the first weight vector equals z^1, and full-square loss is
(f-1)^2. With the stated mobilities (n,1,1,n), removing the common
physical factor -2(f-1) gives exactly (13.2):

    (z^1)' = delta^1,
    (W^(2))' = delta^2 (h^1)^T/n,
    (W^(3))' = delta^3 (h^2)^T/n,
    a' = h^3.

There is no missing factor of n, 2, or residual in the feature equations.
The clock ds/dt=-2(f-1) gives physical gradient flow whenever the proposed
feature parametrization represents that orbit. The text does not assert
that every deterministic physical initial state admits a forward,
increasing feature clock on an arbitrary [0,S]. In particular it makes
no unsupported global clock or convergence claim.

For arctangent, phi'(z)=1/(1+z^2), so F(z)=z+z^3/3 has
F'(z)=1/phi'(z)>0. It maps the real line bijectively to itself and
its inverse has derivative phi'(F^(-1)(X)). Hence

    (X^1)' = (W^(2))^T delta^2 = (W^(2))^T b'.

The integrals in (13.3) give W^(ell)=W_0^(ell)+M_ell exactly.
The trained contribution to X^1 is

    integral_0^s integral_0^v
        h^1(u) [b'(u)^T b'(v)]/n du dv
    = integral_0^s h^1(u)
        b'(u)^T [b(s)-b(u)]/n du.

Continuous finite-dimensional integrands on the compact triangular domain
justify changing the integration order. This proves (13.4), including its
single factor 1/n. Multiplying M_2 and M_3 by the corresponding current
forward vectors yields the first two equations of (13.5). Multiplying
M_3^T by the current delta^3 yields its transpose-memory equation, with
the same normalized pairing. The readout integral and b' equation are
exactly the remaining feature equations.

For the converse, differentiating R_1 in (13.4) produces no upper-endpoint
term, since b(s)-b(s)=0. The derivative of its interior factor gives

    R_1'(s) = [integral_0^s h^1(u)b'(u)^T/n du] b'(s)
            = M_2(s)^T b'(s).

It follows that (X^1)'=(W^(2))^T b' and therefore
(z^1)'=phi'(z^1) odot (W^(2))^T b'=delta^1.
Differentiating the matrix and readout integrals supplies their three
equations. The forward definitions and b'=delta^2 provide the rest of
the reconstructed network. Zero primitive and the stated initial data
ensure the correct initial state. Thus the converse has no integration
constant or compatibility gap.

The four initial-matrix actions are precisely
W_0^(2)h^1, (W_0^(2))^T b, W_0^(3)h^2, and
(W_0^(3))^T delta^3. Both orientations are actions of the same underlying
matrix; no independent reverse operator is substituted.

Canonical Gaussian initialization is stated correctly, including stored
readout variance n^(-2). The exact identities hold for arbitrary
deterministic initial states on a finite C^1 feature solution. The later
bounds are conditional; the chapter does not use the finite-dynamics
RMS event as if it supplied every hypothesis of (13.6).

## All derivative and supplied-path bounds

Assume (13.6). Set c=pi/2. The scalar bounds
|phi|<=c, |phi'|<=1, and |phi''|<=2 hold globally. In particular,

    ||delta^3||_2/sqrt(n) <= B,
    ||q^2||_2/sqrt(n) <= B^2,
    ||b'||_2/sqrt(n) = ||delta^2||_2/sqrt(n) <= B^2.

The infinity bound on a is sufficient for the derivative multiplication
below; it is not silently replaced by an RMS bound.

| Differentiated quantity | Verified RMS upper bound |
|---|---|
| (h^1)' = phi'(z^1)^2 odot (W^(2))^T delta^2 | B^3 |
| (z^2)' = (||h^1||_2^2/n) delta^2 + W^(2)(h^1)' | c^2 B^2+B^4 = Z_2 |
| (h^2)' = phi'(z^2) odot (z^2)' | Z_2 |
| (z^3)' = (||h^2||_2^2/n) delta^3 + W^(3)(h^2)' | c^2 B+B Z_2 = Z_3 |
| (delta^3)' = h^3 odot phi'(z^3)+a odot phi''(z^3) odot (z^3)' | c+2B Z_3 |

Consequently the four queried arguments h^1, b, h^2, delta^3 have
derivative RMS bounds B^3, B^2, Z_2, c+2BZ_3, respectively. The
chapter's common constant C is valid, positive, and depends only on B.
Integrating the derivative bound gives the displayed RMS Lipschitz
estimate without a dimension-dependent embedding.

For S>0, take N=ceil(CS/epsilon) equal subintervals, so N+1 mesh points
suffice and each gap is at most epsilon/C. For S=0 use the single
point zero. The preceding point (with zero selected at the left
endpoint) is within epsilon/C. Ordinary operator boundedness therefore
gives

    ||A(v(s)-v(pi(s)))||_2/sqrt(n)
    <= ||A||_op epsilon <= B epsilon.

The last inequality is legitimate for all four actions because (13.6)
also holds at time zero and ||A^T||_op=||A||_op. The point count is
independent of n for fixed B,S,epsilon. It covers each supplied path in
time; it does not cover all width-varying values by a common spatial net
or produce the query arguments causally.

## Retained-memory integration by parts

Write delta b=b-tilde b and delta h=h-tilde h only within this review.
The exact difference is

    M-tilde M
    = integral delta b' h^T/n + integral tilde b' delta h^T/n
    = delta b(s)h(s)^T/n
      - integral delta b (h')^T/n
      + integral tilde b' delta h^T/n.

The lower boundary term vanishes by the two zero primitives. The identity
||vw^T/n||_op=||v||_2||w||_2/n follows from Cauchy–Schwarz, with
equality on w/||w||_2 when both vectors are nonzero; zero vectors satisfy
it as well. Taking suprema proves (13.10):

    e_M <= (B_h+S L_h)e_b + S L_b e_h.

For R=integral M^T b', split

    R-tilde R
    = integral (M-tilde M)^T b'
      + tilde M(s)^T delta b(s)
      - integral (tilde M')^T delta b.

Here the lower boundary term vanishes, and
||tilde M||_op<=S L_b B_h and ||tilde M'||_op<=L_b B_h.
After dividing vector norms by sqrt(n), the three terms are bounded by
S L_b e_M, S L_b B_h e_b, and S L_b B_h e_b.
This is exactly (13.11). The proof requires the stated uniform
derivative bounds, but does not require convergence of b' or tilde b'.

For top memory, use the decomposition

    delta^3(h^2)^T - tilde delta^3(tilde h^2)^T
    = (delta^3-tilde delta^3)(h^2)^T
      + tilde delta^3(h^2-tilde h^2)^T.

The same normalized rank-one identity and integration over length S
give (13.12) with coefficients S B_2 and S D_3. All estimates are
dimension independent under their respective hypotheses. They are
continuity estimates on supplied path classes, not stability estimates
for coupled modified dynamics.

## Adversarial checks and retained inference gaps

1. **Transcript and causality.** Values of the actual sampled queries can
   depend on unretained matrix actions. The supplied-path residual bound
   does not establish measurability from the retained transcript.
   The chapter accurately says this measurability is not shown, rather
   than asserting an impossibility theorem. No Gaussian innovation
   conditioning or causal finite-program construction has been proved.

2. **Nonlinear stability and tails.** For two paths satisfying their
   corresponding b' equations with the same zero primitive, subtracting
   and adding phi'(z^2) odot tilde q^2 gives exactly (13.13).
   On |tilde q^2|<=Q, the mean value theorem bounds the multiplier
   difference by 2|z^2-tilde z^2|, giving 2Q times its RMS.
   On the complement, |phi'|<=1 gives the safe bound 2 times the
   tail RMS. The triangle inequality proves (13.14).
   A uniform q^2 RMS bound does not imply uniform tail decay.
   The example sqrt(n)e_1 has RMS one and, when n>Q^2, tail RMS one.
   With z=e_1 and tilde z=0, the multiplier difference at coordinate
   one is 1/2-1=-1/2. Multiplication by sqrt(n)e_1 therefore has
   RMS exactly 1/2 while the z-distance is 1/sqrt(n).
   This defeats a uniform vanishing continuity modulus based only on
   those RMS controls. It is not a reachability or initialization claim.

3. **Strong compactness.** For S>0 the ell^2 paths s e_j have uniform
   supremum norm S and Lipschitz constant one, but the distance of two
   distinct values at a fixed s>0 is sqrt(2)s. No norm-convergent
   subsequence exists at that time. Thus temporal regularity alone
   supplies no strong spatial compactness. The degenerate S=0 case
   is not used as a counterexample.

4. **Derivative and raw-kernel observables.** Since b'=delta^2,
   differentiating the initial lower transpose response gives exactly
   (13.15). For j^(-1)sin(js)v, the supremum norm is at most ||v||/j,
   its derivative is cos(js)v, and direct integration yields
   ||v||^2[S/2+sin(2jS)/(4j)] for the squared time-L^2 norm.
   For S>0 this tends to S||v||^2/2, despite uniform convergence of
   the primitive to zero and bounded derivatives. Thus the uniform
   integrated-response estimate alone cannot give velocity convergence
   or convergence of the quadratic first-layer raw kernel. The example
   is correctly presented as an invalid-inference witness, not a
   counterexample reached by the canonical network.

5. **No hidden claim upgrade.** Retaining all rank memories preserves
   exactness but does not produce a scalar state dimension independent
   of width, an autonomous population restart, a width limit, or cap
   removal. None is claimed. The physical-flow estimates in the
   dependency do not automatically supply stability in feature time.

## Claim ledger and final assessment

| Claim | Status after this review | Scope |
|---|---|---|
| Canonical finite gradients, kernels, energy identity | Proved | Fixed finite model with stated metric and loss |
| Global finite-width continuous gradient flow | Proved | C^2 activations, finite initial state, positive mobilities |
| Uniform finite-horizon RMS/kernel bounds | Proved under stated hypotheses | Fixed depth/data and bounded initial norms/loss |
| Exact arctangent memory representation and converse | Exact under assumptions | Finite C^1 feature solution and compatible initial data |
| Four initial-query derivative bounds and time net | Proved under stated hypotheses | The supplied path satisfying (13.6) |
| Lower and top memory continuity | Proved under stated hypotheses | The specified C^1 path classes |
| RMS-only continuity, temporal-regularity-only compactness, primitive-to-derivative inference | Refuted in the indicated unrestricted classes | The explicit deterministic examples |
| Causal query construction, coupled solution stability, population/width identification, derivative/kernel convergence, cap removal, population restart | Open / not established here | No upgrade follows from this chapter |

There are no required mathematical, normalization, initialization, clock, or
canonical-notation corrections in these supplied files. The exact conditional
results are supported by complete checks above, and the remaining bridges are
identified rather than implicitly assumed.
