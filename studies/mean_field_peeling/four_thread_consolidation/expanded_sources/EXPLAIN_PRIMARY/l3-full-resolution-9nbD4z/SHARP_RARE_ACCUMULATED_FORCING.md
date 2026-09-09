# Square-root-size control of accumulated rare training

This is a consequence of SINGLE_PRUNED_OFFBLOCK_OSGOOD.md and the
previously checked pruned Gaussian-query and scalar-comparison lemmas.
It improves the rare-size term in equation (28) of that note from
\(p^{1/3}\) to \(\sqrt{p\log(e/p)}\). It does not close the full-state
comparison or prove the all-finite-time population theorem.

The finite networks in this lemma have ZERO initial readout. They are
the canonical Gaussian hidden-weight proof comparators, not a claim
that the prescribed tiny Gaussian readout has already been removed
globally. Both networks are uncut, or both use the same prescribed
middle clipping with Lipschitz constant at most one and
\(|\tau(x)|\le |x|\). The constants are independent of that prescribed
clipping. No event simultaneous over all clipping levels is asserted.

## Statement

Fix a finite feature horizon \(S\). Compare the full network with the
fully pruned network for a middle index set \(E\), denoting the latter
by hats. Put \(p=|E|/n\). Vector norms below are ordinary Euclidean
norms; \(\|\cdot\|_{\rm F}\) is the ordinary matrix Frobenius norm.
Use the distance
\[
\begin{split}
d_E(s)={}&\frac{\|X^{(1)}-\widehat X^{(1)}\|_2}{\sqrt n}
 +\|W^{(2)}-\widehat W^{(2)}\|_{\rm op}\\
&+\|W^{(3)}-\widehat W^{(3)}\|_{\rm op}
 +\frac{\|W^{(4)}-\widehat W^{(4)}\|_2}{\sqrt n}.
\end{split}
\]
Let \(h(p)=p\log(e/p)\) and
\(\mu(d)=d\sqrt{1+\log_+(1/d)}\), both extended by zero at zero.
For any \(0<\eta<1\), there is an event of probability at least
\(1-\eta\), intersected with the initial operator-bound event, on
which the following holds simultaneously over every set \(E\).
There is a deterministic \(\varepsilon_n\to0\) when
\(\eta=1/n\), such that
\[
\begin{split}
&\left(\frac1n\sum_{i\in E}
 \sup_{0\le s\le S}|z_i^{(2)}(s)-\widehat z_i^{(2)}(s)|^2
 \right)^{1/2}\\
&+\sup_{0\le s\le S}
 \|P_E(W^{(2)}(s)-W_0^{(2)})\|_{\rm F}\\
&+\sup_{0\le t\le S}
 \frac1{\sqrt n}\left\|
 \int_0^t (P_EW^{(2)}(s))^\top
             P_E\delta^{(2)}(s)\,ds\right\|_2\\
&\qquad\le C_{S,M}\left[
 \sqrt{h(p)}+\varepsilon_n+
                    \int_0^S\mu(d_E(s))\,ds\right].
\tag{1}
\end{split}
\]
For example, with the same grid size \(N\) as the off-block lemma,
one may enlarge constants and take
\[
\varepsilon_n=
\sqrt{\frac{\log(30n^2N/\eta)}n}
+\frac{\log(30n^2N/\eta)}n+n^{-1/2}.
\tag{2}
\]
Here \(N\le\lceil nS\rceil+1\), with grid gaps at most \(1/n\).
The initial operator event and its exponentially small failure
probability are the ones already recorded for the Gaussian matrices.

## Proof

Write the actual and reference middle backward actions explicitly as
\[
q^{(2)}=(W^{(3)})^\top\delta^{(3)},\qquad
\widehat q^{(2)}
       =(\widehat W^{(3)})^\top\widehat\delta^{(3)}.
\]
The deleted columns of the pruned top matrix remain frozen. Hence
\[
P_E\widehat q^{(2)}
       =P_E(W_0^{(3)})^\top\widehat\delta^{(3)}.
\tag{3}
\]
PRUNED_GAUSSIAN_SUBSET_BOUND.md, with an allocated fraction of the
failure probability, gives simultaneously over \(E\) and time
\[
\frac{\|P_E\widehat q^{(2)}(s)\|_2}{\sqrt n}
       \le C_{S,M}\big[\sqrt{h(p)}+\varepsilon_n\big].
\tag{4}
\]
This is a query of the genuinely fully pruned network, whose active
trajectory is independent of the deleted initial top columns.
It is not a top-only copy driven by the actual bulk trajectory.

The actual/reference top comparison from equations (20)--(21) of
SINGLE_PRUNED_OFFBLOCK_OSGOOD.md uses only bounded readout,
operator bounds, and Lipschitz activation maps. It gives
\[
\frac{\|q^{(2)}(s)-\widehat q^{(2)}(s)\|_2}{\sqrt n}
       \le C_{S,M}\big[d_E(s)+\sqrt p\big].
\tag{5}
\]
Combining (3)--(5), and using \(\sqrt p\le\sqrt{h(p)}\), yields
\[
\frac{\|P_Eq^{(2)}(s)\|_2}{\sqrt n}
 \le C_{S,M}\big[\sqrt{h(p)}+\varepsilon_n+d_E(s)\big].
\tag{6}
\]
No tail bound on the actual backward field is used here. The unknown
state distance remains explicitly on the right.

For the scalar comparison set
\(e=P_E(z^{(2)}-\widehat z^{(2)})\), and retain the exact identity
\[
e'=\alpha_E P_E\delta^{(2)}+\rho_E,\qquad e(0)=0,
\tag{7}
\]
where
\[
\alpha_E=
\frac{\|\widehat h^{(1)}\|_2^2}n+
\frac1n\sum_i\phi'(\widehat z_i^{(1)})^2,\qquad
1/4\le\alpha_E\le(\pi/2)^2+1.
\]
The off-block lemma now supplies
\[
\int_0^S\frac{\|\rho_E(s)\|_2}{\sqrt n}\,ds
\le C_{S,M}\left[
 \sqrt{h(p)}+\varepsilon_n+
                   \int_0^S\mu(d_E(s))\,ds\right].
\tag{8}
\]
The scalar amplitude estimate in
DIRECT_SCALAR_PRUNED_REDUCTION.md gives
\[
\begin{split}
\left(\frac1n\sum_{i\in E}\sup_s |e_i(s)|^2\right)^{1/2}
\le{}&
\left(\frac1n\sum_{i\in E}\sup_s
                         |\widehat z_i^{(2)}(s)|^2\right)^{1/2}\\
&+2\int_0^S\frac{\|\rho_E(s)\|_2}{\sqrt n}\,ds\\
&+3^{1/3}p^{1/3}
 \left(\int_0^S\alpha_E(s)
           \frac{\|P_Eq^{(2)}(s)\|_2}{\sqrt n}\,ds\right)^{1/3}.
\end{split}
\tag{9}
\]
For a common clipping, the same proof uses
\(|\tau(q^{(2)})|\le|q^{(2)}|\) in the last term.
The simultaneous pruned forward-path bound from that same source
controls the first term by \(C_{S,M}[\sqrt{h(p)}+\varepsilon_n]\).

Let \(J\) denote the nonnegative time integral in the last line of
(9). Equation (6) and boundedness of \(\alpha_E\) imply
\[
J\le C_{S,M}\left[
 \sqrt{h(p)}+\varepsilon_n+\int_0^S d_E(s)\,ds\right].
\tag{10}
\]
The elementary improvement is
\[
p^{1/3}J^{1/3}\le\sqrt p+J.
\tag{11}
\]
Indeed if \(J\le\sqrt p\) the left side is at most \(\sqrt p\);
if \(J\ge\sqrt p\), then \(p\le J^2\) and the left side is at
most \(J\). The cases \(p=0\) or \(J=0\) are immediate.
Thus the cubic scalar estimate does not require a \(p^{1/3}\)
error once the actual rare backward action is compared with its
Gaussian pruned query.

Insert (8), (10), and (11) into (9), using \(\mu(d)\ge d\).
This proves the first term of (1). Equations (10)--(11) of
DIRECT_SCALAR_PRUNED_REDUCTION.md then control the other two terms
by the rare displacement and the integral in (8). Their quadratic
displacement terms are absorbed using the established uniform
primal bound. The matrix norm in those rank-one identities is
exactly the Frobenius norm here, since the finite update contains
\(\delta^{(2)}(h^{(1)})^\top/n\).

Allocate the total failure probability between the off-block,
pruned backward-query, and pruned forward-path events. No
independence between those events is needed. Their explicit
logarithmic errors are bounded by a constant times (2).
This proves (1).

## Exact remaining limitation

The modulus in (1) satisfies
\(\int_{0+}du/\mu(u)=\infty\), but (1) is NOT a closed inequality
for \(d_E\). It controls rare row training and its accumulated
bottom forcing. The active matrix difference and the active
transpose forcing still contain the uncompressed bulk gate
difference described in equations (29)--(30) of the off-block
note. No estimate for those terms is inferred from (1).
