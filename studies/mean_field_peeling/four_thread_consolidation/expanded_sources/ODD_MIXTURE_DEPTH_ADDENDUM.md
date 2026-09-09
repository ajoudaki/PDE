# Later all-depth odd-mixture result: exact scope and supersession

This is a read-only audit of `odd_mixture_general_depth/REPORT.md` (all 643 lines), `REVIEW_SUMMARY.md`, `reviews/final/MANIFEST.json`, and all three complete final reviews. No mathematical research, new proof, experiments, or manuscript edits were performed.

## Ownership and exact reviewed bytes

Owning task is the same user task as the current root, `01a07bd4-a15f-7d42-9559-f59d7a9e96ff`, in an earlier alternative branch. Exact local session: `/home/codex-b/.codex/sessions/2026/09/08/rollout-2026-09-08T07-57-14-01a07bd4-a15f-7d42-9559-f59d7a9e96ff_01a07f97-90fc-7fc3-87ac-cbffb5bd72fd.jsonl`; completed turn `01a07f97-945f-7953-9116-aea4efc3b517`. Its user requested a generic-depth three-sample odd-mixture global theorem; the final answer explicitly stopped short of that target.

Current report and frozen final review input both hash to `cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037`. All three fresh isolated reviewers read all 643 lines, using only the immutable report as mathematical input. All three accepted the stated initialization and conditional continuation results with no required mathematical corrections. Flint explicitly recorded **FAIL as completion of the requested global trained theorem**. No whole-trained-theorem PASS should be inferred.

Review hashes verified against current bytes:

- Orion: `73508c3061130cd97f9e089cafc17fae4a8a6434c0935418f8dceafc99e7530b`.
- Larch: `4d83c2a13c8dad3aa4d2807be952754c251924caecd22087e068a93d4b98789a`.
- Flint: `986c13befd785c722b0dc8a415e6e017c47f7c7cdfd465a76e3c768b4ec6a454`.

## Accepted initialization theorem, superseding weaker earlier bounds

Use the identical activation in all hidden layers
\(\phi_\theta(z)=(1-\theta)z+\theta\arctan z\), \(0<\theta\le1\), at any fixed integer depth \(L\ge1\). There are exactly three normalized samples in any fixed dimension \(d\ge2\). Their Gram matrix \(\Gamma\) has diagonal one and strict off-diagonal bounds \(-1+\delta<\Gamma_{ij}<1-\delta\), \(0<\delta<1\); singular realizable Grams are allowed. Let \(Q_0=\Gamma\), \(q_0=1\), and recursively \(Q_\ell=\mathbb E[\phi_\theta(Z)\phi_\theta(Z)^T]\) for \(Z\sim N(0,Q_{\ell-1})\), with common diagonal \(q_\ell\) and normalized Gram \(C_\ell=Q_\ell/q_\ell\).

For the infimum over all strictly admissible triples in **each** fixed \(d\ge2\), uniformly in \(0<\delta\le1/4\), \(0<\theta\le1\), and every integer \(L\ge1\),
\[
\frac{e^{-80/3}}{73728}\frac{\delta^2\theta^2L}{(1+\theta L)^2}
\le \inf_\Gamma\lambda_{\min}(Q_L)
\le11520e^{128/3}\frac{\delta^2\theta^2L}{(1+\theta L)^2}.
\]
Thus the sharp absolute order is \(\delta^2\theta^2L/(1+\theta L)^2\); normalized conditioning has sharp order \(\delta^2\theta^2L/(1+\theta L)\). The stronger individual lower bound, valid for every \(0<\delta<1\), is
\[
\lambda_{\min}(Q_L)\ge
\frac{e^{-80/3}[\delta(2-\delta)]^2\theta^2L}{1152(1+8\theta L)^2}.
\]
The matching upper witness is the actual planar strict triple \((c,\sqrt{1-c^2}),(1,0),(c,-\sqrt{1-c^2})\), \(c=1-2\delta\), with test vector \((1,-2c,1)\); it embeds in every permitted dimension.

Useful distinct refinements: \((1+8\theta\ell)^{-1}\le q_\ell\le(1+\theta\ell/4)^{-1}\), and \(q_\ell\sim(2\theta\ell)^{-1}\) for fixed positive \(\theta\). Initialization normalized correlations satisfy \(|C_{\ell,ij}|\le|\Gamma_{ij}|\). First Hermite mass retention across arbitrary consecutive layers is at least \(e^{-80/3}\), with cubic contributions added at every layer. The layerwise absolute best-affine gap is asymptotic to \(1/(12\theta\ell^3)\), and its fraction of feature variance to \(1/(6\ell^2)\), at fixed \(\theta>0\). These are **initialization depth asymptotics**, not trained-time behavior or a width limit with growing depth.

Finite initialization is independent \(W^1_{ij}\sim N(0,1/d)\), \(W^\ell_{ij}\sim N(0,1/n)\) for \(2\le\ell\le L\), and rescaled readout \(C_i\sim N(0,n^{-2})\); predictor is \(n^{-1}C^Th^L\), loss \(\frac12\sum_i(f_i-y_i)^2\), raw metric \((d/n)\|dW^1\|_F^2+\sum_{\ell\ge2}\|dW^\ell\|_F^2+n^{-1}\|dC\|^2\), raw GD step \(n^{-2}\). For each separately fixed depth, empirical feature Grams converge in probability to \(Q_\ell\); initial hidden kernel blocks are \(O_{\mathbb P}(n^{-2})\), and initial readout/full kernel converges to \(Q_L\). This initialization result is label independent.

The \(\theta=0\) affine equilateral, all-positive-label obstruction remains: predictions sum to zero, zero-readout population is stationary, loss is \(3/2\) in this report's convention. This known boundary obstruction is not a new refutation at positive mixture.

## Accepted conditional strong population continuation theorem

For every separately fixed depth, use arbitrary fixed real neuron Hilbert spaces, bounded base actions plus Hilbert–Schmidt increments, bottom field in \(L^2(\Omega;\mathbb R^d)\), readout in \(L^2\), and actual Hilbert adjoints. These base actions are not asserted to have been canonically constructed from Gaussian initialization.

Put \(a=1-\theta\), \(s(z)=\sqrt{1+z^2}\), and choose smooth odd \(\tau\) equal to identity on \([-1,1]\), \(0\le\tau'\le1\), with derivative zero outside \([-2,2]\). The reference backward gate is
\[
D_R(z,q)=a q+\theta\frac{R}{s(z)}\tau\!\left(\frac{q}{Rs(z)}\right).
\]
The forward activation remains the true \(\phi_\theta\). Assume the reference flows exist on \([0,T]\), have common initial state, have uniformly bounded primal norms/operators, and satisfy
\[
\sup_{R,t,\ell,i}\left\|q^\ell_{i,R}\mathbf1_{\{|q^\ell_{i,R}|/\sqrt{1+(z^\ell_{i,R})^2}>u\}}\right\|_2
\le A e^{-cu}\quad(u\ge1).
\]
Then reference raw states **and raw directions** converge uniformly to a strong \(C^1\) true-gate solution, unique against all bounded-primal strong true-gate competitors from the same initial state. Consistent hypotheses on every finite horizon give a global solution and reached-state continuation/uniqueness. The reference-only comparison remains linear in its threshold at every fixed depth; the resulting Osgood argument imposes no extra smallness coupling among \(\theta,L,T\).

This is a useful distinct conditional criterion: it weights incoming tails by the actual arctangent curvature scale, so it is weaker than ordinary exponential incoming-field tails. It is not a proved trained GF/GD width limit: the required canonical reference bounds and weighted tails are not established.

## Accepted limitations and negative examples

- With \(Z=Q\), the ratio \(|Q|/\sqrt{1+Z^2}<1\); the weighted-tail premise can hold even when ordinary exponential tails fail.
- At an allowed arbitrary state with depth at least two, a rank-one Hilbert–Schmidt operator change can make a top preactivation one while a readout \(C=U^{-1/3}\), \(U\sim\mathrm{Unif}(0,1)\), has finite squared norm three. The relevant squared tail is \(3/(\sqrt2u)\), excluding an implication from bounded primal state to the weighted exponential premise.
- At \(Z=1\), \(Q=J=U^{-1/3}\) each lie in \(L^2\), but their product does not; nonzero gate curvature therefore prevents naive differentiation of the backward gate on the entire raw \(L^2\) state class.

These examples concern admissible states or differentiability, not states proved reachable by canonical training. They do not refute the desired initialized theorem. No sufficient positive training threshold \(\theta_*(\delta,L)\), no depth-uniform positive threshold, and no canonical global trained population/GF/GD theorem is proved or refuted by this report. Finite-dimensional global GF and the definability of each finite GD step are recorded, but they do not close these missing limits.
