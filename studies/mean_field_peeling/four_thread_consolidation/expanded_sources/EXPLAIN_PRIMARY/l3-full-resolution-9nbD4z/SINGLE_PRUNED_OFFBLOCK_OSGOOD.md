# A single-pruned Gaussian estimate for the actual off-block residual

## Scope and conclusion

This is a finite-width estimate for the full versus fully pruned
zero-readout proxy, with the same canonical Gaussian initialization
of the first layer and the two hidden matrices, and with both initial
readouts exactly zero. Here "actual" refers to the unpruned trajectory
of this proxy, not to the tiny-random-readout finite target.
This note does not establish a global transfer to that finite target.
It bounds the
off-block residual in DIRECT_SCALAR_PRUNED_REDUCTION.md; it does not
assume the full/pruned distance is small. It does not itself bound that
distance or prove global continuation.

Both networks below are uncut. The proof also applies when BOTH use
the same prescribed middle clipping \(\tau\), with
\(|\tau(x)|\le |x|\) and Lipschitz constant at most one. Comparing an
uncut network with a differently clipped reference would require an
additional clipping-error term and is not claimed.

Fix \(S,M\), let \(a=\pi/2\), and use normalized vector norms
\(\|v\|_n^2=n^{-1}\sum_i v_i^2\) and
\(\|v\|_{1,n}=n^{-1}\sum_i|v_i|\). Matrix operator norms are ordinary
Euclidean operator norms. All constants below depend only on the
established primal bounds on \([0,S]\) and the initial operator bound
\(M\), not on width or a maximum backward coordinate.

For each deleted middle set \(E\), write \(P=P_E\), \(Q_E=I-P_E\).
Hats denote its single fully pruned reference. Thus
\[
 P\widehat W^{(2)}=PW^{(2)}_0,\qquad
 \widehat h^{(2)}_E=\widehat\delta^{(2)}_E=0.
\]
Write \(U=W^{(2)}\), \(V=\widehat W^{(2)}\),
\(D_1=\operatorname{diag}(\phi'(z^{(1)}))\), and similarly for hats.
Take the distance
\[
 \begin{split}
 d_E={}&\|X^{(1)}-\widehat X^{(1)}\|_n
       +\|W^{(2)}-\widehat W^{(2)}\|_{\rm op}\\
      &+\|W^{(3)}-\widehat W^{(3)}\|_{\rm op}
       +\|W^{(4)}-\widehat W^{(4)}\|_n .
 \end{split}                                                   \tag{1}
\]
Any larger full-state distance, including one with HS matrix
differences, may be used. Here \(X^{(1)}=F(z^{(1)})\), so both
\(F^{-1}\) and \(h^{(1)}=\phi(F^{-1}(X^{(1)}))\) are 1-Lipschitz.

Set
\[
 h(p)=p\log(e/p),\qquad
 \mu(d)=d\sqrt{1+\log_+(1/d)},
 \quad h(0)=\mu(0)=0.
\]
Choose a grid with \(N\le \lceil nS\rceil+1\) points and gaps at most
\(1/n\). For \(n\ge2\) and \(0<\eta<1\), put
\[
 q_n=\frac{\log(6n^2N/\eta)}{n},\qquad
 \nu_n=\sqrt{q_n}+q_n+n^{-1/2}.
 \tag{2}
\]
There is an event of probability at least \(1-\eta\), intersected
with the common initial-operator event, on which simultaneously for
every \(E\) and every \(s\in[0,S]\),
\[
 \left\|
 P_EA_2Q_E\delta^{(2)}
       -P_EW^{(2)}_0(\widehat h^{(1)})'
 \right\|_n
 \le C_{S,M}\left[\sqrt{h(|E|/n)}+\mu(d_E)+\nu_n\right].
 \tag{3}
\]
The full residual \(\rho\) in that earlier note obeys the same bound:
\[
 \|\rho(s)\|_n
 \le C_{S,M}\left[\sqrt{h(|E|/n)}+\mu(d_E(s))+\nu_n\right].
 \tag{4}
\]
For fixed \(S\), choosing \(\eta\) proportional to \(1/n\) makes
\(\nu_n\) vanish. The initial-operator event has the separately
recorded exponentially small failure probability. Equations (3)--(4)
are quantitative bounds, not a claim that \(d_E\) is controlled.

## 1. Conditional Gaussian restricted-column bounds

The reference matrix
\[
 C_E(s)=\widehat D_1(s)^2\,V(s)^*Q_E
 \tag{5}
\]
depends only on the fully pruned active initial data. In particular it
is independent of \(G_E=P_EW^{(2)}_0\), whose entries in its nonzero
rows are independent \(N(0,1/n)\). Deleted rows of \(V\) do not enter
(5). On an active-data initial-operator event, the existing primal
bounds give
\[
 \sup_s\|C_E(s)\|_{\rm op}\le M_S,\qquad
 \sup_s\|C_E'(s)\|_{\rm op}\le L_S\sqrt n .
 \tag{6}
\]
Indeed
\[
 C_E'=(\widehat D_1^2)'V^*Q_E+
                 \widehat D_1^2(V')^*Q_E,
\]
\(\|(\widehat D_1^2)'\|_{\rm op}\le
4\sqrt n\|(\widehat z^{(1)})'\|_n\), and
\(\|Q_EV'\|_{\rm op}\le
\|\widehat\delta^{(2)}\|_n\|\widehat h^{(1)}\|_n\).
Select the entire zero path outside that active-data event. This
selection preserves independence from \(G_E\). No conditioning on the
full, undeleted operator event is used for this independence.

For deterministic \(E,F\), of sizes \(m,l\), and Euclidean unit
vectors \(u\in\mathbb R^m,v\in\mathbb R^l\), condition on the active
data. At a fixed time,
\[
 u^TG_EC_EP_Fv
 \text{ is centered Gaussian of variance at most }M_S^2/n.
\]
The usual two \(1/4\)-nets, of sizes at most \(9^m,9^l\), therefore give
\[
 \mathbb P\big(\|G_EC_EP_F\|_{\rm op}>t
                  \mid\text{active data}\big)
 \le 2\,9^{m+l}\exp[-nt^2/(8M_S^2)].
 \tag{7}
\]
This argument allows arbitrary dependence of \(C_E\) on the retained
Gaussian rows and on the retained top columns.

Take
\[
 t^2=\frac{8M_S^2}{n}\left[
 (m+l)\log9+m\log(en/m)+l\log(en/l)
                      +\log(6n^2N/\eta)\right].
\]
Union over sets of both sizes, the \(n^2\) size pairs, and the \(N\)
grid times gives failure at most \(\eta/3\). Since \(h(p)\ge p\),
on the resulting event
\[
 \|G_EC_E(s)P_F\|_{\rm op}
 \le C_S\sqrt{h(|E|/n)+h(|F|/n)+q_n}
 \tag{8}
\]
at grid times, simultaneously over \(E,F\).

Now impose the full initial operator bound. Every selected path is
then genuine and \(\|G_E\|_{\rm op}\le M\). The interpolation loss
from (6) is at most \(ML_S/\sqrt n\). Consequently, for ALL times,
\[
 \|G_EC_E(s)P_F\|_{\rm op}
 \le C_{S,M}\left[
 \sqrt{h(|E|/n)+h(|F|/n)+q_n}+n^{-1/2}\right].
 \tag{9}
\]
The event controls all \(F\), including sets chosen using the actual
trajectory. It is enough to take \(F\subseteq E^c\); columns in \(E\)
are zero in (5). Importantly, the reference is always the one with
ONLY \(E\) pruned, not the one with \(E\cup F\) pruned.

## 2. Sparse blocks convert small L1 into a logarithmic bound

The following deterministic consequence of (9) is the key step.
Let \(\mathcal M_E=G_EC_E(s)\). For any vector \(v\), possibly selected
using the entire actual initialization and trajectory, suppose
\[
 \|v\|_n\le Q,\qquad \|v\|_{1,n}\le\ell\le Q.
 \tag{10}
\]
If \(Q=0\) or \(\ell=0\), then \(v=0\). Otherwise let
\[
 k=\left\lceil n(\ell/Q)^2\right\rceil\in\{1,\ldots,n\}.
 \tag{11}
\]
Partition the coordinates by decreasing \(|v_i|\) into consecutive
blocks \(I_1,I_2,\ldots\) of size \(k\), with the last block possibly
smaller. Every block before the last is full. For \(j\ge2\),
\[
 \|v_{I_j}\|_n
 \le \frac1{\sqrt{kn}}\sum_{i\in I_{j-1}}|v_i|.
 \]
Hence
\[
 \sum_j\|v_{I_j}\|_n
 \le Q+\sqrt{n/k}\,\ell\le2Q.
 \tag{12}
\]
Apply (9) to every block and use monotonicity of \(h\). Since
\(k/n\le(\ell/Q)^2+1/n\) and \(k/n\le1\),
\[
 h(k/n)\le h((\ell/Q)^2)+h(1/n).
 \]
For a sum at most one this is subadditivity of \(h\); if the sum
exceeds one, it follows from \(h(x)\ge x\) and \(h(k/n)\le1\).
Also \(h(1/n)\le q_n\) for \(n\ge2\). Finally
\[
 Q\sqrt{h((\ell/Q)^2)}
 \le \sqrt2\,\ell\sqrt{\log(eQ/\ell)}.
 \]
Thus
\[
 \|\mathcal M_Ev\|_n
 \le C_{S,M}\left[
 Q\big(\sqrt{h(|E|/n)}+\nu_n\big)
             +\ell\sqrt{\log(eQ/\ell)}\right].
 \tag{13}
\]
The last expression is defined to be zero at \(\ell=0\).
The ceiling in (11) handles \(\ell/Q<n^{-1/2}\); the case
\(\ell=Q\) gives \(k=n\). No lower bound on a nonzero \(\ell\), or
upper bound on a coordinate of \(v\), was imposed.

## 3. Replacing the actual lower gate in an off-block operator

Use the simultaneous adaptive submatrix event from
ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md, with failure allocation
\(\eta/3\). It controls ALL signed diagonals and ALL deleted sets.
For
\[
 a_j=\phi'(z_j^{(1)})^2-\phi'(\widehat z_j^{(1)})^2,
 \]
one has \(|a_j|\le1\) and, because \(F^{-1}\) is 1-Lipschitz,
\[
 \frac1n\sum_j a_j^2
       \le \min\{1,16d_E^2\}.
 \tag{14}
\]
Apply that lemma to the nonnegative diagonal \(a_j^2\). The exact
factorization of the operator norm gives
\[
 \begin{split}
 \|G_E\operatorname{diag}(a)\|_{\rm op}^2
 &=\|G_E\operatorname{diag}(a^2)G_E^*\|_{\rm op}\\
 &\le C\big[h(|E|/n)+h(\min\{1,16d_E^2\})+q_n\big].
 \end{split}
 \tag{15}
\]
For every \(d\ge0\),
\(\sqrt{h(\min\{1,16d^2\})}\le C\mu(d)\): substitute for
\(d\le1/4\), and use \(h\le1\le16d^2\) for \(d\ge1/4\).
Thus
\[
 \|G_E(D_1^2-\widehat D_1^2)\|_{\rm op}
 \le C\big[\sqrt{h(|E|/n)}+\mu(d_E)+\sqrt{q_n}\big].
 \tag{16}
\]
This uses the square of the gate difference and its L2 bound, not
the weaker L1 bound on a single power of that difference.

Define the actual and reference off-block maps
\[
 \mathcal N_E=PU D_1^2U^*Q_E,\qquad
 \mathcal M_E=G_E\widehat D_1^2V^*Q_E.
 \tag{17}
\]
Their difference is exactly
\[
 \begin{split}
 \mathcal N_E-\mathcal M_E
 ={}&P(U-V)D_1^2U^*Q_E\\
 &+G_E(D_1^2-\widehat D_1^2)U^*Q_E\\
 &+G_E\widehat D_1^2(U-V)^*Q_E.
 \end{split}
 \tag{18}
\]
The first and third terms cost \(C_Sd_E\). Equation (16) treats the
second, proving
\[
 \|\mathcal N_E-\mathcal M_E\|_{\rm op}
 \le C_{S,M}\big[\sqrt{h(|E|/n)}+\mu(d_E)+\nu_n\big].
 \tag{19}
\]
There is no small-support restriction at the right endpoint in
(19). It is a comparison of two operators, not a small bound on
either full rare-to-bulk operator separately.

## 4. Apply the bound to the actual off-block residual

Write \(q=q^{(2)}=(W^{(3)})^*\delta^{(3)}\) and use hats for the
reference. The bounded primal maps give
\[
 \|Q_E(z^{(2)}-\widehat z^{(2)})\|_n\le C_Sd_E,\qquad
 \|h^{(2)}-\widehat h^{(2)}\|_n
                         \le C_Sd_E+a\sqrt{|E|/n}.
 \tag{20}
\]
The second inequality includes the forced zero reference activation
on \(E\). Since both readouts are bounded in \(L^\infty\) and both
top matrices in operator norm,
\[
 \|q-\widehat q\|_n\le C_S(d_E+\sqrt{|E|/n}),\qquad
 \|q\|_n+\|\widehat q\|_n\le Q_S .
 \tag{21}
\]
For completeness, the top comparison uses
\[
 \|\delta^{(3)}-\widehat\delta^{(3)}\|_n
 \le\|W^{(4)}-\widehat W^{(4)}\|_n
       +2aS\|z^{(3)}-\widehat z^{(3)}\|_n,
 \]
followed by the ordinary matrix-times-vector difference identities.
No \(L^p\) estimate on \(q\) or \(\widehat q\) is involved.

On \(E^c\), the exact backward difference is
\[
 Q_E(\delta^{(2)}-\widehat\delta^{(2)})
 =Q_ED_2(q-\widehat q)+v,\qquad
 v=Q_E(D_2-\widehat D_2)\widehat q.
 \tag{22}
\]
The first term is small in \(L^2\) by (21). For the second term,
boundedness and Lipschitz continuity of \(\phi'\) give
\[
 \|v\|_n\le Q_S,\qquad
 \|v\|_{1,n}
 \le 2\|Q_E(z^{(2)}-\widehat z^{(2)})\|_n
                           \|\widehat q\|_n
 \le C_Sd_E.
 \tag{23}
\]
There is no claim that \(\|v\|_n\) is small. Applying (13) with
\(\ell=\min\{C_Sd_E,Q_S\}\) instead gives the actual compressed bound
\[
 \|\mathcal M_Ev\|_n
 \le C_{S,M}\big[\sqrt{h(|E|/n)}+\mu(d_E)+\nu_n\big].
 \tag{24}
\]
The logarithmic term for fixed \(Q_S\) is bounded by \(C_S\mu(d_E)\)
for all distances: for sufficiently small \(d_E\) substitute in (13),
and for larger \(d_E\) use the bounded L2 norm and \(\mu(d_E)\ge d_E\).

The residual in (3) has the EXACT decomposition
\[
 \begin{split}
 b_E:={}&P_EA_2Q_E\delta^{(2)}
               -G_E(\widehat h^{(1)})'\\
 ={}&(\mathcal N_E-\mathcal M_E)Q_E\delta^{(2)}
       +\mathcal M_EQ_ED_2(q-\widehat q)
       +\mathcal M_Ev .
 \end{split}
 \tag{25}
\]
Here the scalar part of \(A_2\) vanishes between \(E\) and \(E^c\),
and \((\widehat h^{(1)})'
=\widehat D_1^2V^*Q_E\widehat\delta^{(2)}\).
The three terms are bounded by (19), (21), and (24), respectively.
This proves (3), with no circular assumption that \(d_E\) is small.

For the common clipping extension, replace the first term in (22)
by \(Q_ED_2[\tau(q)-\tau(\widehat q)]\), and replace
\(\widehat q\) in \(v\) by \(\tau(\widehat q)\). Its L2 and L1 bounds
are unchanged. Equation (25) then uses that modified first term.

## 5. The entire scalar-reduction residual and accumulated effects

The same expansion (18), with \(Q_E\) replaced by \(P_E\), controls
the difference between the actual rare self-block and the pruned
self-block by the right side of (19). The scalar parts differ by
at most \(C_Sd_E\). The already proved uniform pruned Gram estimate,
with failure allocation \(\eta/3\), gives
\[
 \|P_EA_2P_E-\alpha_E I_E\|_{\rm op}
 \le C_{S,M}\big[\sqrt{h(|E|/n)}+\mu(d_E)+\nu_n\big],
 \tag{26}
\]
where
\(\alpha_E=\|\widehat h^{(1)}\|_n^2+
n^{-1}\operatorname{Tr}(\widehat D_1^2)\).
This step only combines the existing reference Gram lemma with
(16); it does not require the actual gate to be independent.
The reference Gram error has the displayed bound because
\(h(p)\le1\), its square-root and linear width terms are included
in \(\nu_n\), and its interpolation error is \(O(n^{-1/2})\).

Since
\(\rho=(P_EA_2P_E-\alpha_EI_E)\delta_E+b_E\)
and \(\|\delta_E\|_n\le C_S\), equations (3) and (26) prove (4).
Consequently
\[
 \int_0^S\|\rho(s)\|_n\,ds
 \le C_{S,M}\left[
 \sqrt{h(|E|/n)}+\nu_n+\int_0^S\mu(d_E(s))\,ds\right].
 \tag{27}
\]
Combining this with the checked scalar-amplitude, Gaussian-reference,
and rank-memory estimates in DIRECT_SCALAR_PRUNED_REDUCTION.md gives
small accumulated rare training and rare first-layer forcing up to
the remaining full-state error integral:
\[
 \begin{split}
 &\sup_{t\le S}\|P_E(W^{(2)}(t)-W^{(2)}_0)\|_{\rm HS}
 +\sup_{t\le S}
      \left\|\int_0^t(P_EW^{(2)})^*\delta_E\,ds\right\|_n\\
 &\qquad\le C_{S,M}\left[
 (|E|/n)^{1/3}+\sqrt{h(|E|/n)}+\widetilde\nu_n
                         +\int_0^S\mu(d_E(s))\,ds\right].
 \end{split}
 \tag{28}
\]
Here \(\widetilde\nu_n\to0\) also includes the separately allocated
uniform Gaussian reference-path event from that note. Probability
allocations can be divided once more to include that event; no
independence among good events is needed.

The modulus is Osgood:
\(\int_{0+}du/\mu(u)=\infty\).
This describes the modulus appearing in the proved estimates.
It does not assert a closed Osgood inequality for \(d_E\).

## 6. Exact remaining bulk coordinate, not an implicit closure

The preceding improvement treats the OFF-BLOCK query
\(\mathcal M_Ev\). The same \(v\) enters the active parameter
comparison without that Gaussian compression. In the uncut case,
\[
 \begin{split}
 (Q_E(U-V))'
 ={}&[Q_ED_2(q-\widehat q)]\otimes h^{(1)}
        +v\otimes h^{(1)}\\
    &+Q_E\widehat\delta^{(2)}
                  \otimes(h^{(1)}-\widehat h^{(1)}).
 \end{split}
 \tag{29}
\]
The source \(v\otimes h^{(1)}\) has HS norm
\(\|v\|_n\|h^{(1)}\|_n\); (23) does not make this small.
Similarly the transformed first-layer comparison contains
\[
 (Q_EV)^*v
 \tag{30}
\]
in addition to the accumulated rare forcing already handled in (28).
The output of (30) occupies the entire first layer, so the sparse
Gaussian-row estimate (13) cannot be applied to it as written.

Integrating (29) and solving it for
\(\int v\otimes h^{(1)}\) only rewrites the unknown active matrix
difference; it is not an independent cancellation estimate. The
existing rare rank-memory formula applies to \(\delta_E\), not to
the active difference \(v\) in (29). Therefore this note upgrades
the exact off-block residual from an unestimated term to (3)--(4),
but the active matrix/first-layer comparison (29)--(30) remains open.
No all-time population existence, uniqueness, or response-moment
claim follows.
