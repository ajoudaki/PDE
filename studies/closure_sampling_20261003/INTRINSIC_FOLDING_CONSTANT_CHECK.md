# Check of the explicit strict-root folding constants

2026-10-04. Bounded arithmetic and downstream-interface reconstruction.
The checked candidate is INTRINSIC_FOLDING_CONSTANT_ROUTE.md at SHA-256
`f2c56abd842fe90533cab3f9b0f558f91ac1c1601697c226ea8f3b97082014c4`.
The complete candidate and LABEL_DEPTH_RESCALING_ROUTE.md were read.
The earlier qualitative downstream argument was reconstructed in this
agent's INTRINSIC_STRICT_ROOT_CHAINING_CHECK.md; no sibling verdict or
new source-representation result was read for this check.

Other scientific inputs and hashes:

| Input | SHA-256 |
| --- | --- |
| INTRINSIC_STRICT_ROOT_ROUTE.md | `c3c1e5d10c32458ca08dbbbe6251efdb0ee400e5301a50aff943d7064d6ad7d1` |
| LABEL_DEPTH_RESCALING_ROUTE.md | `d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1` |
| ARCHITECTURE_CONSTANT_REFINEMENT.md | `b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7` |

**Verdict: conditional PASS, with no arithmetic repair required.** The
explicit coefficient \(\beta^{40L}S[d+1+\log(1/\xi)]\) for folding
and the combined \(\beta^{130L}[d+1+\log(1/\xi)]Y(m/\gamma)^{3/2}\)
are valid envelopes, conditional on the inherited passive-query insertion
identity and its arbitrarily high fixed polynomial success probability.
This check does not independently certify that new insertion theorem.
It verifies the constants of its endpoint estimate and the resulting
moment/concentration/chaining calculation. No experiment or numerical
parameter sweep was run.

## 1. Activity and singleton trace

Use exactly the candidate's finite constants, with \(\beta\ge10\),
\(L\ge2\), \(\lambda=\min(1,\gamma/m)\), and \(S=16Y/\lambda\).
The inherited label condition and \(\gamma\le B^2\) give
\[
 Y/\lambda\le\beta^{-60L},\qquad S\le\beta^{-59L}.
 \tag{1}
\]
Here \(B^2\le\beta^{2L}\) and \(16\le\beta^L\); no additional
small-label restriction has been imposed.

The rescaled-label recurrences give
\(K_{\max}\le\beta^{2L}\),
\(A_H,H_2\le\beta^{8L}\), \(D_H\le\beta^{5L}\),
\(\eta^{-1}\le\beta^{22L}\),
\(\mathcal B\le\beta^{3L}\), and \(E\le\beta^{7L}\).
These constants bound the augmented external-preactivation Hessian
blocks as well as the ordinary training Hessian. A passive unit query
satisfies the same RMS carrier bounds and bounded-gate parameter
derivative recurrences, so its normalized Hilbert--Schmidt endpoint is
bounded by \(H_2\), independent of dimension and the unused first matrix.

Put \(a_1=D_H/\eta\) and \(q=4eS^2a_1\). For the term with \(h\ge1\)
insertions, splitting the \((h+1)\)-st power gives respectively
\[
 H_2A_H\frac{(2SA_H)^h}{h!},\qquad
 2eH_2Sa_1\sqrt{2\mathcal B}(h+1)q^h.
\]
The second expression follows from
\((h+1)^{h+1}/h!\le e^{h+1}(h+1)\). Since
\(\sum_{h\ge1}(h+1)q^h=q(2-q)/(1-q)^2\), this reconstructs the
candidate's exact trace envelope (6), including its factors of two.
The zero-insertion term uses both Hilbert--Schmidt endpoints and is
\(H_2^2\).

From (1),
\[
 a_1\le\beta^{27L},\quad q\le4e\beta^{-91L}<1/4,
\quad SA_H\le\beta^{-51L},
\]
\[
 2eSa_1\sqrt{2\mathcal B}
                    \le2e\sqrt2\,\beta^{-30.5L}<1.
\]
At \(q\le1/4\), the displayed rational series sum is at most \(7/9\).
Also \(e^{2SA_H}-1\le1\). Because the defined recurrences have
\(H_2\ge A_H\ge1\),
\[
 \mathcal T\le H_2^2+H_2A_H+H_2
              \le3H_2^2\le\beta^{17L}.
 \tag{2}
\]
The direct external trace, learned-column term, and bounded activation
factors therefore give
\[
 D_q=B(\mathcal T+E)+Bs^2K_{\max}^2+1
 \le\beta^{17L+1}+\beta^{7L+1}+\beta^{4L+3}+1
 \le\beta^{20L}.
 \tag{3}
\]
The vanishing insertion terms may be made at most \(S\) at fixed
positive labels. This alters only the width threshold. The nonvanishing
trace and learned-column coefficients in (2)--(3) retain every factor.

## 2. Carrier moments and their probability scope

Assume the insertion identity with shift \(D_qS\), a cavity-measurable
reference of RMS at most \(sK_{\max}S\), and exceptional probability
\(\Pr(E_n\cap\Omega_{n,M}^c)\le C_Mn^{-M}\) for every fixed \(M\).
For its independent Gaussian root, the scalar normal moment bound gives
\(2sK_{\max}S\sqrt p\) at every fixed time/query. It follows directly
from
\(u^pe^{-u^2/4}\le(2p/e)^{p/2}\) and
\(\mathbb Ee^{g^2/4}=\sqrt2\).

On the exceptional event use the deterministic real bound
\(|k_i|\le K_{\max}S\sqrt n\). Choosing \(M=p+2\) makes its
probability/counting \(L^p\) contribution
\[
 K_{\max}S C_M^{1/p}n^{-1/2-2/p}\le S
\]
eventually. Remove successful-event indicators only from the nonnegative
Gaussian upper bound before conditioning on the cavity. Thus no Gaussian
law is conditioned on full-network survival. Minkowski in the joint
probability and normalized counting space requires no independence
between neurons. The top carrier and deterministic endpoint tail give
the valid coefficient
\[
 C_k=2sK_{\max}+D_q+B+3\le\beta^{25L}.
 \tag{4}
\]
This proves the stated \(C_kS\sqrt p\) moment envelope conditional on
the insertion hypothesis above.

The constants \(C_M\) may depend on fixed moment order, dimension and
other data: they multiply a strict negative width power. For a later
chaining order \(p\), this calculation is applied at order \(2p\),
and the width threshold must accommodate that order. No uniform-in-\(p\)
threshold or moment order growing with width is claimed. The event
\(E_n\) itself remains measurable with respect to training initialization
and contains no restriction on the independent passive Gaussian matrix.

## 3. Gaussian operator moments

For an \(n\)-by-\(k\) standard Gaussian matrix, two radius-\(1/4\)
unit-sphere nets of sizes at most \(9^n,9^k\) imply
\(\|G\|_{\rm op}\le2\max|u^\top Gv|\). The union-bound threshold is
\[
 2\sqrt{2[(n+k)\log9+u+\log2]}.
\]
For \(n,k\ge1\) this is at most
\(5(\sqrt n+\sqrt k+\sqrt u)\): after squaring, already
\(25(n+k+u)\) exceeds the first squared expression. Thus the proposed
tail bound (14) is valid.

Writing the positive excess above \(5(\sqrt n+\sqrt k)\) as \(5X\)
gives \(\Pr(X>t)\le e^{-t^2}\). Its fixed \(q\)-moment is at most
\(2\sqrt q\), for example by its exponential-square moment. Minkowski
then proves the candidate's (15). When \(n\ge k+p\),
\[
 \|1+\|G\|_{\rm op}/\sqrt n\|_{L^p}\le21.
\]
Probability Hölder and (4) at order \(2p\) therefore give a factor
\(\sqrt{21}\sqrt{2p}C_kS<8C_kS\sqrt p\) in (16). This step does
not assume independence of the Gaussian matrix and query carrier.
The \(k=0\) case needs no folding.

## 4. Forward and backward increment envelopes

The residual activity between two times is at most \(Sa/2\), where
\(a=|\tau(t)-\tau(s)|\), so every velocity bound (17) has the correct
factor \(1/2\). The active first-operator cap is nine: its initialized
cap is eight and its displacement is below one under (1).

The forward recurrence has propagation multiplier \(9s\) and forcing
\(B^2sK_{\max}/2\). Its exact geometric sum is bounded by
\[
 (9s)^{L-1}
 [9+sK_{\max}/2+B^2sK_{\max}/16],
\]
since \(9s-1\ge8\). This proves \(F\le\beta^{6L}\), in fact
\(F\le\beta^{5L}\). Consequently
\[
 C_g=\sqrt{2st_\phi F}\le\beta^{4L},\quad
 P=\sum_{j=0}^{L-1}(9s)^j\le\beta^{2L},\quad
 A_b\le\beta^{8L}.
 \tag{5}
\]
For the last bound, the two displayed terms defining \(A_b\) are at
most \(\tfrac12\beta^{2L}\) and
\(\tfrac12\beta^{6L+2}\), respectively, whose sum is at most
\(\beta^{8L}\).

The changed-gate counting-four estimate uses
\(|\Delta\phi'|^4\le(2s)^2t_\phi^2|\Delta z|^2\), so its
coefficient is exactly the \(C_g\) in (5). The changed-mixer term after
its gate is \(Bs^3K_{\max}^2S^3a/2\); the terminal changed-readout
term is \(sBSa/2\). Thus backward subtraction yields the candidate's
\([A_b+8C_gPC_k\sqrt p]S\sqrt h\), with
\(h=a+\|v-v'\|\). Here \(S^3\le S\) and \(a\le\sqrt h\).
Since \(8C_gPC_k\le8\beta^{31L}\le\beta^{32L}\), the full
coefficient is at most \(\beta^{33L}\sqrt p\).

The extra input-vector gradient term costs
\(sK_{\max}S\|v-v'\|\le\sqrt2sK_{\max}S\sqrt h\). Adding it
fits \(\beta^{34L}\sqrt pS\sqrt h\). Gaussian rotation costs at
most \(\pi\sqrt p\): the quarter-circle length is \(\pi/2\), and
the scalar Gaussian moment was bounded by \(2\sqrt p\). Therefore
\[
 \|\mathbf1_{E_n}[Z_n(t,v)-Z_n(s,v')]\|_{L^p}
                      \le\beta^{35L}pS\sqrt h.
 \tag{6}
\]
The event is unchanged by rotation because it is training-measurable.
The earlier endpoint continuity and deterministic tail arguments still
apply, so (6) has the required all-time scope.

## 5. Net constants and confidence

Put \(q_0=d+1\). Mesh radius \(2^{-j}/4\) in each factor gives a
product net of radius \(2^{-j}/2\). The sphere needs at most
\((9\cdot2^j)^d\) points and time at most \(5\cdot2^j\), so
\(9^{q_0}2^{jq_0}\) is valid. A previous-level nearest parent is at
distance at most \(2^{-j}\), as required in the candidate.

For a fixed \(p\ge4q_0\), the maximum-increment inequality raises
the net size to power \(1/p\). The resulting factor is at most
\(9^{1/4}<2\), and the geometric ratio is at most \(2^{-1/4}\).
The sum over positive levels is bounded by
\[
 \frac{2\,2^{-1/4}}{1-2^{-1/4}}<11.
\]
The finite coarse net contributes less than two, because every point
can be compared with time zero at the same query. Thus sixteen is a
valid envelope, and
\(16\beta^{35L}pS\le\beta^{36L}pS\).

Choose \(p=\max\{4(d+1),\log(2/\xi)\}\), fixed before width tends
to infinity. Markov at \(e\) times the supremum \(L^p\) norm gives
failure at most \(e^{-p}\le\xi/2\); the training-event complement
is at most \(\xi/2\) eventually. Conditional-mean invariance makes the
folding difference at most twice the centered supremum. Finally
\[
 p\le5[d+1+\log(1/\xi)],\qquad 2e,5\le\beta^L,
\]
which proves a \(\beta^{38L}\) folding envelope. The displayed
\(\beta^{40L}\) coefficient therefore has two additional powers of
\(\beta^L\) as slack. No exponentially large ambient-dimension net
constant remains in this coefficient.

## 6. Combined error and limitations

Let \(a=\gamma/m\). Then \(a\le B^2\), and
\(a^{3/2}/\min(1,a)\le B^3\), checking separately \(a\le1\) and
\(a\ge1\). Therefore
\[
 S\le16B^3Y(m/\gamma)^{3/2}
                  \le\beta^{3L}Y(m/\gamma)^{3/2}.
\]
Use confidence \(1-\xi/2\) for folding and for the restricted
compression. Replacing \(\log(1/\xi)\) by \(\log(2/\xi)\) costs
at most a factor two in \(d+1+\log(1/\xi)\). The folding coefficient
then fits \(\beta^{44L}\) times that linear factor. Adding the inherited
compression coefficient \(\beta^{124L}\) fits \(\beta^{125L}\), and
hence certainly the stated \(\beta^{130L}\). The union bound requires
no independence between these two success events.

The conclusion remains conditional on the underlying passive insertion
theorem, and remains a fixed-architecture, fixed-data, fixed-confidence
eventual-width result. The necessary threshold can depend on the chosen
order \(2p\), its exceptional-event exponent, and \(n\ge k+p\).
This is enough for linear displayed dependence on fixed ambient dimension
and log-confidence; it is not a simultaneous theorem for growing
dimension or confidence. The current label restriction is unchanged,
and zero labels are treated by the exact stationary model. No retained
arrays or runtime source requirements are changed by this constant
calculation.
