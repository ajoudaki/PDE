# Diagonal growing-clipping transfer for the filtered comparison

Status: candidate synthesis, requiring a complete combined audit.
This is an auxiliary-to-canonical-CLIPPED finite-width trajectory
comparison. The clipping level may tend to infinity with width.
It is not removal of clipping from the canonical network, and is
not the requested global population or exact raw-GD theorem.

Use the exact algorithm, Gaussian seeds and query errors of
CAUSAL_FILTERED_QUERY_RANK.md, and the reference feature flow and
state distance in FILTERED_QUERY_CLIPPED_STABILITY.md. The first
note defines a causal perturbed algorithm, not supplied true queries.
The second compares it with the canonical clipped finite-width flow
using the same initial hidden matrices, bottom vector and tiny readout.
The two candidate proofs are explicit dependencies of this note.

Fix \(S>0\). For each \(n\ge2\), choose a deterministic clipping bound
\(R_n\ge1\) and one deterministic scalar map \(\tau_n\) such that
\[
 |\tau_n(v)|\le\min\{|v|,R_n\},\qquad
 |\tau_n(v)-\tau_n(w)|\le|v-w|,\qquad R_n=o(\log n).
 \tag{1}
\]
In particular, \(R_n\to\infty\) is permitted. The identity map is
not covered by a finite \(R_n\); no assertion about it is hidden in (1).
Examples of admissible bounds include
\(R_n=\max\{1,\sqrt{\log(e+n)}\}\), with any common clipping satisfying
the displayed bounds. No condition of simultaneous Gaussian events
over all maps is imposed.

Let \(E_n(S)\) be exactly the maximum in equation (9) of the stability
note for the algorithm and its reference at all mesh states through
\(N=\lceil Sn^2\rceil\). Thus it sums the Euclidean errors, divided
by \(\sqrt n\), in \(x^{(1)},z^{(2)},z^{(3)},a^{(2)},R^{(1)},W^{(4)}\)
and the ordinary Frobenius errors in \(M^{(2)},M^{(3)}\).
The reference is clipped with \(\tau_n\), and its initial fields
are computed exactly from the original canonical Gaussian seeds;
the algorithm's noisy warmup is compared to them, not identified
with them.

There exist events with probability tending to one and a deterministic
sequence \(d_n(S)\to0\) such that
\[
 E_n(S)\le n^{-1/24+d_n(S)}.
 \tag{2}
\]
The events have the same lower probability bound as equation (4) of
the rank note, after ignoring finitely many widths. Consequently
\(E_n(S)\to0\) in probability for every fixed finite \(S\).

## The clipping dependence is explicit, not assumed uniform

We first extract a quantitative constant from the deterministic
stability proof. With \(S,M\) fixed, its preceding uniform state,
operator, readout-coordinate and filter bounds are independent of \(R\).
Call a common larger constant \(C_0(S,M)\ge1\).
Its reference middle-backward time difference in (12) is bounded by
\(C_0(1+R)|s-t|\). Each of its five reference slow right sides
therefore has time-Lipschitz constant at most \(C_1(1+R)\):
the only new \(R\) factor enters through \(\delta^{(2)}\), and in
each product one subtracts one factor at a time. All other factors
already have \(R\)-independent bounds. Thus the sum of one-step
quadrature errors is at most \(C_2(1+R)\eta^2\).

Likewise the difference of the two top backward fields is bounded
by the readout error and a constant times the layer-three state error,
independently of \(R\). The ordinary query difference has the same
property, together with its query error. The sole extra clipping
factor in the middle backward difference is
\[
 2R\,\frac{\|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{3}
\]
Each of the five slow right-side differences is thus bounded by
\(C_3(1+R)\) times the sum of current state and query errors.
There is no product of two middle backward differences.

In the notation of that proof, filter contraction gives
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_4(D_k+b+\varepsilon+d_0),
 \tag{4}
\]
with \(C_4\) independent of \(R\). Substitution into its slow-state
inequality therefore yields
\[
 E_{k+1}\le E_k+
 C_5(1+R)\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{5}
\]
Here \(E_k,D_k\) are respectively the slow-state error and its
running maximum; they are not \(E_n(S)\).
Summing and using the same elementary discrete Gronwall calculation
as in the stability note gives, after combining (4)--(5),
\[
 E_n(S)\le C_6(1+R)\exp(C_6(1+R))
                    (b+\varepsilon+d_0+\eta),
 \tag{6}
\]
whenever the hypotheses of that deterministic theorem hold.
All \(C_i\) depend only on \(S,M\), not on the map within its stated
bounds, width, mesh or filter scale. Increasing \(S\) to
\(\max\{1,S\}\) handles the stability note's harmless \(S\ge1\)
normalization. This proves (6) with linear, not unspecified, clipping
dependence in the exponential.

## Apply the bound to the actual perturbed histories

The rank theorem applies to each prescribed \(\tau_n\), since its
constants and probability allowances are uniform in that deterministic
choice. It supplies a single event for this choice on which
\[
 \|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,\qquad
 \|W^{(4)}_0\|_\infty\le1,
\]
and every raw query error, divided by \(\sqrt n\), is at most
\[
 B_n=C_S n^{-1/24}\log(e+n)^{8/3}+C_S n^{-1/4}.
 \tag{7}
\]
The stability note uses a sum of two orientation errors at each
layer, so take \(b=2B_n\), not \(B_n\). Eventually \(b\le1\).
The direct-noise event in the rank theorem bounds the warmup errors
and gives \(d_0\le C_S n^{-1/4}\), by its equation (36) or direct
1-Lipschitzness of \(\phi\). Eventually \(d_0\le1\).
No conditional independence after selecting this event is used.

Its remaining parameters are
\(\varepsilon=n^{-1/8}\), \(\eta=n^{-2}\), and
\(N\eta\le S+1\), with \(0<\eta\le\varepsilon\le1\).
Thus all deterministic hypotheses are checked on the same event.
Apply (6) with \(M=8\) and \(R=R_n\). Since every other error is
bounded by a constant times the first term of (7), it follows that
\[
 E_n(S)\le
 C_S(1+R_n)\exp(C_S(1+R_n))
 n^{-1/24}\log(e+n)^{8/3}.
 \tag{8}
\]
The logarithm of the prefactor on the right, divided by \(\log n\),
tends to zero: \(R_n=o(\log n)\),
\(\log(1+R_n)=o(\log n)\), and
\(\log\log(e+n)=o(\log n)\). Enlarging a nonnegative deterministic
sequence \(d_n(S)\to0\) to absorb the constant in (8) proves (2).
The event probability tends to one by the rank theorem, which proves
the convergence in probability without any exchange of expectation,
clipping supremum or infinite-time limit.

## What remains after this diagonal transfer

Both processes in (2) still depend on the clipping \(\tau_n\).
The theorem says they are close to each other. It does not show that
either is close to the uncut canonical finite-width flow, nor that
their common asymptotic law exists. In particular, \(R_n\to\infty\)
alone does not prevent backward-field mass from reaching the cutoff.

The estimate has not proved a uniform clipped-tail envelope, uncut
uniqueness or autonomous restart, a limiting action-space construction,
or physical-clock/exact-GD convergence. The layer-register derivatives
and all required kernel/velocity observables still require their own
arguments. This diagonal bridge is stronger than holding the clipping
level fixed, but is not a substitute for any of these missing conclusions.
No experiment or new external theorem is used.
