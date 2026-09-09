# Exact moderate sine activation: physical-energy route

This note concerns the exact original two-input L3 model and the fixed activation requested by the user. It is an independent proof attempt. It does not establish the global canonical population theorem. The new complete results below are: a strong endpoint lemma for any already-constructed physical population flow; an unconditional finite-horizon descent and raw-energy theorem for the prescribed raw GD step; and weak path-law tightness. These are useful reductions, not substitutes for strong population existence and identification.

Sources read: the exact model in `studies/mean_field_peeling/two_sample_activation_design/PROOF.md`; `SINE_INITIALIZATION.md`; the full raw two-sample source equations in `two_sample_separated_angle_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md`; the local theorem interfaces in `L3_LOCAL_COMPLETE_PROOF.md`; and the mathematical energy/tail discussion in `BOUNDED_ACTIVATION_ROUTE.md` and `practical_global_limit_assessment/ASSESSMENT.md`. No previous or sibling review was used. No experiment was performed and no existing source was modified.

## 1. Candidate and elementary constants

Put

\[
 v=(1-e^{-8})/2-4e^{-4},\qquad N=\sqrt{1+4v/25},
\qquad \Phi(z)=az+b\sin(2z),
\]
\[
 a=(1-4e^{-2}/5)/N,\qquad b=2/(5N).
\]

Here `v>0`, since it is the variance of the nonzero Gaussian-orthogonal residual `sin(2G)-2e^{-2}G`. In particular `N>1`. The exact derivatives are

\[
 \Phi'(z)=a+2b\cos(2z),\qquad
 \Phi''(z)=-4b\sin(2z).
\]

Since `e^2>4`,

\[
 0<m:=(1/5-4e^{-2}/5)/N\le\Phi'(z)<2,
 \qquad |\Phi''(z)|<2,
 \qquad \Phi(0)=0,\quad |\Phi(z)|\le2|z|.       \tag{1}
\]

No small coefficient or condition on the observation horizon is used in (1). The lemmas below in fact apply to any C2 activation with `phi(0)=0`, `||phi'||_infinity<=2` and `||phi''||_infinity<=2`; the lower slope is not needed for them. They hold for any input correlation in `[-1,1]`, so in particular for the user's separated inputs.

## 2. Raw norm and estimates on a primal ball

At finite width use the exact raw norm from the contract. A normalized vector has norm `||u||_n=||u||_Euclidean/sqrt(n)`. Suppose

\[
 \max_i\|z_i^1\|_n,\quad \|W^2\|_{op},\quad
 \|W^3\|_{op},\quad\|C\|_n\le B,\qquad B\ge1.      \tag{2}
\]

The following bounds follow successively from (1):

| Field | Norm bound |
|---|---:|
| `h^1` | `2B` |
| `z^2,h^2` | `2B^2,4B^2` |
| `z^3,h^3` | `4B^3,8B^3` |
| `delta^3,q^2` | `2B,2B^2` |
| `delta^2,q^1,delta^1` | `4B^2,4B^3,8B^3` |

The sample maximum is implicit in this table. Since the labels have modulus one,

\[
 \sum_i|r_i|\le16B^4+2\le18B^4.                  \tag{3}
\]

Let `V=-grad_raw L` be the actual physical vector field. Each of its four parameter blocks has raw norm at most `144B^7`, and hence

\[
 \|V\|_{raw}\le576B^7.                           \tag{4}
\]

For a middle block this uses

\[
 \|u\otimes_n h\|_F=\|u\|_n\|h\|_n.
\]

For the first block,

\[
 \sqrt{d/n}\,\|d^{-1}u x_i^T\|_F=\|u\|_n
\]

because `||x_i||^2=d`. Thus no dimension or width factor enters (4). The same argument applies to population fields, with Hilbert--Schmidt norms of the learned increments.

## 3. A dimension-explicit raw Lipschitz estimate

At width n, let two states both satisfy (2), and let `d_0` be their raw distance. Forward differences satisfy

\[
 \|\Delta z^1\|_n\le d_0,\quad
 \|\Delta h^1\|_n\le2d_0,\quad
 \|\Delta z^2\|_n\le4Bd_0,\quad
 \|\Delta h^2\|_n\le8Bd_0,
\]
\[
 \|\Delta z^3\|_n\le12B^2d_0,\quad
 \|\Delta h^3\|_n\le24B^2d_0,\quad
 \sum_i|\Delta r_i|\le64B^3d_0.                    \tag{5}
\]

For example,

`Delta z^2=W^2 Delta h^1+Delta W^2 h_tilde^1`,

and `||Delta W^2||op<=||Delta W^2||F<=d_0`. The last inequality in (5) uses

`|Delta f_i| <= ||Delta C||_n ||h_i^3||_n + ||C_tilde||_n ||Delta h_i^3||_n <=32B^3 d_0`.

For the backward gates, use

\[
 \|\Phi'(z)q-\Phi'(\widetilde z)\widetilde q\|_n
 \le2\|q-\widetilde q\|_n
       +2\|\widetilde q\|_\infty\|z-\widetilde z\|_n,
 \quad \|u\|_\infty\le\sqrt n\|u\|_n.
\]

Substitution of (5) and the field bounds gives, in causal order,

\[
 \|\Delta\delta^3\|_n\le26\sqrt n B^3d_0,\quad
 \|\Delta q^2\|_n\le28\sqrt n B^4d_0,\quad
 \|\Delta\delta^2\|_n\le72\sqrt n B^4d_0,
\]
\[
 \|\Delta q^1\|_n\le76\sqrt n B^5d_0,\quad
 \|\Delta\delta^1\|_n\le160\sqrt n B^5d_0.         \tag{6}
\]

For instance the middle gate difference is at most

`2(28 sqrt(n) B^4)d_0 + 2(sqrt(n) 2B^2)(4B)d_0 <=72 sqrt(n) B^4 d_0`.

Expanding each rank-one update and its residual then gives respective raw block Lipschitz bounds

\[
 3392\sqrt n B^9,\quad3248\sqrt n B^9,\quad
 2672\sqrt n B^9,\quad944\sqrt n B^9.
\]

Their sum is 10256. Consequently the conservative bound

\[
 \|V(\Theta)-V(\widetilde\Theta)\|_{raw}
 \le11000\sqrt n B^9\|\Theta-\widetilde\Theta\|_{raw}        \tag{7}
\]

holds whenever the two states satisfy (2). The primal set (2) is convex in the raw parameters, so the same bound controls the entire segment joining them. This is a finite-width estimate; its `sqrt(n)` factor is not dropped in a population argument.

## 4. Unconditional finite-time raw-GD energy

Fix an observation horizon T and an initialization with primal bounds at most `b_0>=1` and loss `E_0`. Put

\[
 R=\sqrt{2(T+1)E_0}+2,\qquad B=b_0+R+1,
 \qquad h=n^{-2}.
\]

Assume n is sufficiently large that

\[
 11000B^9n^{-3/2}\le1,\qquad576B^7n^{-2}\le1.      \tag{8}
\]

Then the actual simultaneous raw GD iterates through time T, and one additional endpoint if necessary, satisfy

\[
 \mathcal L(\Theta_k)\le E_0,\qquad
 \sum_{j<k}h\|V(\Theta_j)\|_{raw}^2\le2E_0,
\]
\[
 \|\Theta_k-\Theta_0\|_{raw}
 \le\sqrt{2khE_0}\le\sqrt{2(T+1)E_0}.             \tag{9}
\]

Proof. Stop provisionally before raw distance R from initialization. A raw displacement of size R changes either initial operator norm, the readout norm, or a first-layer sample norm by at most R, so (2) holds with room to spare. The second inequality in (8) and (4) keep the next Euler segment inside the larger primal ball B. Taylor's formula for the scalar loss and (7) give

\[
 \mathcal L(\Theta+hV)\le\mathcal L(\Theta)
      -h\|V\|_{raw}^2+	frac12(11000\sqrt n B^9)h^2\|V\|_{raw}^2
 \le\mathcal L(\Theta)-\tfrac12h\|V\|_{raw}^2.
\]

Summing proves the first two claims in (9). Cauchy--Schwarz for the sum of raw increments proves the third, which is strictly below R. This closes the induction and removes the stop. No population flow, tail bound, convergence theorem, or fixed-width comparison with continuous GF was assumed.

Under the prescribed random initialization, one may take `b_0=10`, `E_0<=2` on events with probability tending to one. Initial first-layer sample norms converge to one, the initial Gaussian action norms are bounded with probability tending to one, the readout norm tends to zero, and the two predictions tend to zero. Thus (8)-(9) give bounds uniform in width on events with probability tending to one for every fixed T.

This proves stable finite-horizon raw GD at the prescribed step; it does not identify its strong population limit.

## 5. Finite GF and weak path-law tightness

At every fixed width the finite-dimensional smooth vector field is locally Lipschitz. Its true gradient-flow energy identity is

\[
 \mathcal L(t)+\int_0^t\|\dot\Theta(s)\|_{raw}^2ds=E_0,
 \quad
 \|\Theta(t)-\Theta(0)\|_{raw}\le\sqrt{tE_0}.       \tag{10}
\]

It therefore cannot escape in finite time and is global. This is finite-dimensional existence only.

On any primal ball B, for a differentiable raw path write `s(t)=||dot Theta(t)||raw`. Successive forward differentiation gives

\[
 \|\dot z^1\|_n\le s,\quad\|\dot h^1\|_n\le2s,
 \quad\|\dot z^2\|_n\le4Bs,\quad\|\dot h^2\|_n\le8Bs,
\]
\[
 \|\dot z^3\|_n\le12B^2s,\qquad
 \|\dot h^3\|_n\le24B^2s.                        \tag{11}
\]

These inequalities hold almost everywhere also for linearly interpolated raw GD, with hidden fields recomputed from the interpolated parameters as required by the contract. Equations (9)-(11), together with initialized second-moment bounds, uniformly bound the average squared H1([0,T]) norm of the joint four-coordinate same-layer paths `(z_1,h_1,z_2,h_2)`.

Closed bounded H1 balls on a finite one-dimensional time interval have compact images in C([0,T]); this follows directly from the pointwise bound and the modulus `|x(t)-x(s)|<=sqrt(|t-s|)||x'||_L2`, followed by the Arzela--Ascoli theorem. Markov's inequality for the empirical average H1 norm therefore gives tightness of the empirical path laws in the weak topology on probability measures on C([0,T];R4), on the above high-probability events.

This is not W2 compactness: a bounded mean squared H1 norm does not by itself make squared path norms uniformly integrable. It does not identify a deterministic subsequential law, kernels, adjoints, or velocity laws.

## 6. Strong endpoint reduction for the population problem

Fix the canonical generated action spaces and initial bounded actions `A_0,B_0`. Work in the complete raw affine Hilbert state space

\[
 \mathfrak X=(\hbox{first-layer L2 field})\times
 HS(\mathcal H_1,\mathcal H_2)\times
 HS(\mathcal H_2,\mathcal H_3)\times\mathcal H_3,
\]

with actions `A=A_0+Delta A`, `B=B_0+Delta B`. The first factor may equivalently retain the full normalized first-layer weight field; unused directions are fixed. HS convergence implies operator-norm convergence.

**Continuity lemma.** For the candidate Phi, the complete forward/backward calculation and the true raw gradient are continuous on this raw state space. On a bounded raw set they have finite L2 or HS norms bounded by a polynomial in the primal bounds.

Proof. Forward continuity follows from the global Lipschitz property of Phi and bounded-action continuity. For the only less immediate map, if `(z_j,q_j)->(z,q)` in L2 x L2, then

\[
 \|\Phi'(z_j)q_j-\Phi'(z)q\|_2
 \le2\|q_j-q\|_2+\|[\Phi'(z_j)-\Phi'(z)]q\|_2\to0.   \tag{12}
\]

The last term tends to zero because `z_j->z` in measure, Phi' is continuous, and its square times `q^2` is bounded by `16q^2`, an integrable function. A subsequence argument or dominated convergence after almost-everywhere subsubsequence convergence gives the conclusion for the full sequence. Apply (12) in backward causal order; rank-one products are continuous from L2 x L2 to HS. This proves the lemma.

The scalar prediction is continuously Frechet differentiable in the raw state with the usual backpropagated gradient. To check the potential issue from Nemytskii nonlinearities, for any fixed `q in L2` use

\[
 |\Phi(z+u)-\Phi(z)-\Phi'(z)u|
 \le\min\{|u|^2,4|u|\}.
\]

Pair with q and split at `|q|>K`. The quadratic remainder on `|q|<=K` is at most `K||u||_2^2`; the Lipschitz remainder on the q-tail is at most `4||q 1_{|q|>K}||_2 ||u||_2`. Divide by `||u||_2`, let `||u||_2->0` at fixed K, then let K tend to infinity. Telescoping the three layers gives the stated scalar Frechet derivative. Its continuity is (12).

**Strong endpoint lemma.** Suppose a strong physical population solution has been constructed on `[0,T_*)`, with `T_*<infinity`. Then there exist a raw state `Theta_* in X` and a raw velocity `V_*` such that

\[
 \Theta(t)\to\Theta_*\quad\hbox{in the full raw Hilbert norm},
 \qquad V(\Theta(t))\to V_*=V(\Theta_*)
           \quad\hbox{in the raw norm},            \tag{13}
\]

as `t->T_*`. Every forward field, incoming backward field, gate output, and actual action/adjoint on a converging L2 probe has a corresponding strong limit.

Proof. The true energy identity gives, for `0<=s<t<T_*`,

\[
 \|\Theta(t)-\Theta(s)\|_{raw}
 \le\sqrt{(t-s)\int_s^t\|\dot\Theta(u)\|_{raw}^2du}
 =\sqrt{(t-s)[\mathcal L(s)-\mathcal L(t)]}.        \tag{14}
\]

Since the loss is nonnegative and decreasing, (14) makes the state Cauchy at the finite endpoint. Completeness produces Theta_*. The continuity lemma gives all the other claims. In fact the path extended by Theta_* is differentiable from the left at T_* with derivative V_*: integrate the converging velocities and divide by the time increment.

For every one of the finitely many incoming-field paths `q(t)` so extended, the image of `[0,T_*]` is a compact subset of L2. It follows that

\[
 \lim_{R\to\infty}\sup_{0\le t\le T_*}
 \|q(t)1_{|q(t)|>R}\|_2=0.                        \tag{15}
\]

For completeness, cover the compact image by finitely many L2 balls of radius eta. If `||q-f||_2<=eta`, split the q-tail according to `|f|>R/2`; on the remaining part `|q|<=2|q-f|`. This bounds the q-tail by `2eta+2||f 1_{|f|>R/2}||_2`. The finitely many reference tails vanish, followed by eta. Thus (15) is qualitative uniform integrability; no exponential tail rate is inferred.

The endpoint lemma rules out raw-state divergence and divergence of the raw velocity as a mechanism of failure of a finite-time strong extension. It does not supply local existence at Theta_*: continuity of a vector field on an infinite-dimensional Hilbert space is not an ODE existence or uniqueness theorem. The current source construction additionally needs a quantitative response/tail certificate, and (15) does not provide one. It must also retain all Gaussian histories when restarted; resetting C or the reverse-field sources would change the model.

## 7. Why positive bounded slope does not make the missing step routine

Even for this strictly increasing analytic Phi and Gaussian variables, the backward multiplication map is not locally Lipschitz on the ambient L2 state space. Let G be a standard Gaussian, `q=G`, `z=G`, and consider

\[
 \mathcal B(z,q)=\Phi'(z)q.
\]

There are disjoint intervals `I_j` going to positive infinity on which `sin(2z)>=3/4`; they all have positive Gaussian probability. Shorten them slightly so a fixed sufficiently small positive increment u remains in a larger interval with `sin(2z)>=1/2`. Put `E_j={G in I_j}` and `z_j=G+u 1_{E_j}`. The mean-value theorem and `Phi''=-4b sin(2z)` imply

\[
 \|\mathcal B(z_j,G)-\mathcal B(G,G)\|_2
 \ge2b\,\inf I_j\,u\,\mathbb P(E_j)^{1/2},
 \qquad \|z_j-G\|_2=u\mathbb P(E_j)^{1/2}.
\]

The perturbation norm tends to zero, but the ratio tends to infinity. The original q and z have Gaussian tails and every finite moment. This does not disprove uniqueness or the target theorem; it invalidates the shortcut of treating the raw L2 gradient as locally Lipschitz merely because Phi', Phi'' are bounded and Phi'>0.

The two-input first-layer controls also cannot generally be simultaneously flattened by a point coordinate change when rho is nonzero: their Lie bracket is nonzero for this Phi. The already supplied exact bracket calculation in `BOUNDED_ACTIVATION_ROUTE.md`, Section 3, applies because Phi' is positive and nonconstant. This is another route obstruction, not a counterexample to the actual physical flow.

## 8. Local source route and its restart boundary

The raw source formulas suggest a nonperturbative local bootstrap that differs from the old arctan coordinate transform. With population C(0)=0 and a stopped primal radius B, physical residual sum at most P, and `D=||Phi'||_infinity`,

\[
 \|C(t)\|_2\le P D^3B^3t,\quad
 \|\delta^3(t)\|_2\le P D^4B^3t,\quad
 \|\delta^2(t)\|_2\le P D^5B^4t.
\]

Thus reverse Gaussian source standard deviations are O(t). A local coefficient box has forward entries `|A_{k,j}|<=A_* h_j` and complete backward row sums `sum_j |D_{k,j}|<=D_* t_k`. In that box the source value equations give `||C||_p,||q^1||_p,||q^2||_p<=C t sqrt(p)` for small t, and the random response envelope has exponent O(t^2) times a Gaussian envelope. This closes only a short-time certificate after the expected-derivative and single-source h_j bounds are checked. A separate source-route agent is pursuing that full local calculation; it is not certified as a theorem by this note.

At a reached positive time the reverse fields are not zero and the old named Gaussian query histories remain part of the state. The O(t) initialization argument cannot simply be repeated from zero. One would need a tail or response estimate propagated from the actual reached state, with a continuation mechanism that cannot accumulate at a finite physical time. Equations (13)-(15) give a strong raw endpoint and qualitative tails, but not that quantitative restart certificate.

The exact remaining implication for this route is therefore:

> A finite-time raw strong endpoint produced by true loss dissipation admits an uncut local strong continuation on the same generated Gaussian action spaces, with enough causal tail/stability control to identify the finite algorithms and all requested observables.

That statement is not proved here. The finite-width GF/GD bounds, the strong endpoint reduction, and the local source heuristic must not be promoted to the requested all-finite-time population result.
