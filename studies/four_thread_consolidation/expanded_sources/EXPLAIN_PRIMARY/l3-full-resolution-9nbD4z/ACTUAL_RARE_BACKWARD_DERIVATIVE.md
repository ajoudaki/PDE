# An actual rare backward-derivative estimate

## Scope and statement

This is a finite-width estimate for the canonical ZERO-initial-readout
proxy and its fully pruned references. It does not establish transfer
to the prescribed tiny random readout or close the full-state
comparison. Both networks are uncut, or both use the same prescribed
coordinatewise clipping \(\tau\), with Lipschitz constant at most one
and \(|\tau(x)|\le|x|\). Constants are independent of that prescribed
clipping; no event simultaneous over every clipping level is claimed.

Use normalized vector norms \(\|u\|_n=\|u\|_2/\sqrt n\),
normalized inner products, and ordinary matrix operator/Frobenius
norms. Rank updates use \(u\otimes v=uv^\top/n\).
Fix a finite feature horizon \(S\) and an initial operator bound \(M\).
Write \(P=P_E\), \(Q=I-P\), \(p=|E|/n\). Hats denote the SINGLE
fully pruned reference for \(E\), and \(d_E\) is the distance (1) in
SINGLE_PRUNED_OFFBLOCK_OSGOOD.md. Set
\[
 h(p)=p\log(e/p),\qquad
 \mu(d)=d\sqrt{1+\log_+(1/d)},\qquad h(0)=\mu(0)=0.
 \]
Let \(N\le\lceil nS\rceil+1\) be a grid size with gaps at most
\(1/n\). For \(n\ge2\) and \(0<\eta<1\), put
\[
 b_n=\frac{\log(32n^2N/\eta)}n,\qquad
 \epsilon_n=\sqrt{b_n}+b_n+n^{-1/2}.
 \tag{1}
\]
There is a common event with failure at most \(\eta\), intersected
with the full initial-operator event, on which all the following
bounds hold for every \(E\) and every \(s\in[0,S]\).
The full initial-operator failure probability remains separate.

With
\[
 q=(W^{(3)})^*\delta^{(3)},\qquad
 \widehat q=(\widehat W^{(3)})^*\widehat\delta^{(3)},\qquad
 \widehat g_E=PW^{(2)}_0(\widehat h^{(1)})',
 \]
the pruned derivative and velocity queries satisfy
\[
 \|P\widehat q'(s)\|_n+\|\widehat g_E(s)\|_n
 \le C_{S,M}\,[\sqrt{h(p)}+\epsilon_n].
 \tag{2}
\]
The actual derivative satisfies
\[
 \|Pq'(s)\|_n
 \le C_{S,M}\left[
 \|P\delta^{(2)}(s)\|_n+\|\widehat g_E(s)\|_n
             +\sqrt{h(p)}+\mu(d_E(s))+\epsilon_n\right],
 \tag{3}
\]
and consequently
\[
 \|Pq'(s)\|_n
 \le C_{S,M}\left[
 \|P\delta^{(2)}(s)\|_n
             +\sqrt{h(p)}+\mu(d_E(s))+\epsilon_n\right].
 \tag{4}
\]
The rare backward action on the right is retained explicitly. It
comes from genuine rare-to-rare top feedback, not an independent
Gaussian coefficient.

## 1. Uniform finite-width derivative bounds needed for the grids

All ordinary primal vector norms, velocities, and trained operator
norms needed below are bounded on the initial norm event. The
following slightly cruder second-time-derivative bounds suffice:
\[
 \|(\widehat\delta^{(3)})'\|_n\le C_{S,M},\qquad
 \|(\widehat\delta^{(3)})''\|_n
       +\|(\widehat h^{(1)})''\|_n\le C_{S,M}\sqrt n
 \quad\hbox{a.e.}
 \tag{5}
\]
For clarity, these bounds can also be proved on the active-data
events needed for conditional independence.

For deleted TOP columns, use
\[
 \Omega_E^{\rm top}
 =\{\|W^{(2)}_0\|_{\rm op}\le M,\
                  \|W^{(3)}_0Q\|_{\rm op}\le M\}.
 \]
On this event the reference quantities used by the active dynamics
have uniform bounds. In particular the controlled query is
\(q_a=Q(\widehat W^{(3)})^*\widehat\delta^{(3)}\), not the full
unused \(\widehat q\). The latter can involve unrestricted deleted
top columns before the full initial norm event is imposed.

The chain proving (5) is noncircular. The first-derivative primal
formulas give \(\widehat z^{(3)\prime}\) and
\(\widehat\delta^{(3)\prime}\) bounded in \(L^2_n\), hence
\(q_a'\) bounded in \(L^2_n\). The identity
\[
 \widehat\delta^{(2)}
       =Q\widehat D_2\,\tau(q_a)
 \]
then gives
\(\|\widehat\delta^{(2)\prime}\|_n\le C_{S,M}\sqrt n\).
Indeed the gate derivative costs at most
\(2\|\widehat z^{(2)\prime}\|_n\|q_a\|_\infty\), and
\(\|q_a\|_\infty\le\sqrt n\|q_a\|_n\). The clipping derivative
satisfies \(|(\tau(q_{a,i}))'|\le|q_{a,i}'|\) a.e.; no second
derivative of \(\tau\) is used.

Write
\(\widehat A_2=\widehat m_1I+
\widehat W^{(2)}\widehat D_1^2(\widehat W^{(2)})^*\).
The matrix derivatives obey
\[
 \|\widehat A_2'\|_{\rm op}\le C_{S,M}\sqrt n,\qquad
 \|\widehat W^{(2)\prime}\|_{\rm op}
       +\|(\widehat W^{(3)}Q)'\|_{\rm op}\le C_{S,M}.
 \]
Consequently \(\widehat z^{(2)\prime\prime}\),
\(\widehat h^{(2)\prime\prime}\), and
\(\widehat z^{(3)\prime\prime}\) have \(L^2_n\) norm at most
\(C_{S,M}\sqrt n\). Products are bounded using
\(\|u^2\|_n\le\sqrt n\|u\|_n^2\).

In particular, with \(\widehat C=\widehat W^{(4)}\),
\[
 \begin{split}
 \widehat\delta^{(3)\prime\prime}
 ={}&(\widehat D_3^2+
            2\widehat h^{(3)}\phi''(\widehat z^{(3)}))
                       \odot\widehat z^{(3)\prime}\\
    &+\widehat C\phi'''(\widehat z^{(3)})
                      \odot(\widehat z^{(3)\prime})^2\\
    &+\widehat C\phi''(\widehat z^{(3)})
                      \odot\widehat z^{(3)\prime\prime},
 \end{split}
 \]
which proves its part of (5).

For deleted INCOMING rows, instead use
\[
 \Omega_E^{\rm in}
 =\{\|QW^{(2)}_0\|_{\rm op}\le M,\
                  \|W^{(3)}_0Q\|_{\rm op}\le M\}.
 \]
The active lower matrix \(Q\widehat W^{(2)}\) is bounded there.
The same active argument bounds
\(\widehat\delta^{(2)\prime}\) by \(C_{S,M}\sqrt n\), and hence
\(\widehat X^{(1)\prime\prime}\) by that amount.
Since \(\widehat h^{(1)}=\chi(\widehat X^{(1)})\), with
\(|\chi'|\le1\) and \(|\chi''|\le4\), the product-square bound
proves the remaining part of (5) using only active data.
This is the event used for the incoming-row Gaussian query.

## 2. Four independent Gaussian coefficient families

For short formulas put
\[
 L=W^{(2)},\quad K=\widehat W^{(2)},\quad
 W=W^{(3)},\quad V=\widehat W^{(3)},\quad
 B=\operatorname{diag}(W^{(4)}\phi''(z^{(3)})).
 \]
Hats on gates and \(B\) refer to the pruned path. Let
\[
 G=P(W^{(3)}_0)^* .
 \]
Its nonzero rows form an independent Gaussian \(m\)-by-\(n\)
matrix with variance \(1/n\). Consider the four right coefficient
paths
\[
 \begin{split}
 C_0&=I,\\
 C_1&=\widehat B\,VQ,\\
 C_2&=\widehat B\,VQ\,\widehat D_2K,\\
 C_3&=\widehat B\,VQ\,\widehat D_2\widehat A_2Q.
 \end{split}                                                   \tag{6}
\]
Every occurrence of \(V\) in (6) has a right \(Q\). Thus every
coefficient is measurable with respect to
\((z^{(1)}_0,W^{(2)}_0,W^{(3)}_0Q)\) and is independent of \(G\).
The full \(K\) and \(\widehat A_2\) are allowed: their deleted
incoming rows contain no deleted TOP column.

On \(\Omega_E^{\rm top}\), all four coefficient paths have
operator norm at most \(C_{S,M}\) and a.e. derivative operator
norm at most \(C_{S,M}\sqrt n\). This follows from the preceding
bounds and
\(\|\widehat D_\ell'\|_{\rm op},
\|\widehat B'\|_{\rm op}\le C_{S,M}\sqrt n\).
Select each entire coefficient path to be zero outside
\(\Omega_E^{\rm top}\). This preserves its independence of \(G\).

Apply the conditional Gaussian net argument and the sorted-block
lemma of SINGLE_PRUNED_OFFBLOCK_OSGOOD.md to these four families,
with total failure allocation \(\eta/4\). At fixed time and fixed
sets \(E,F\), the two-net tail is
\[
 2\,9^{|E|+|F|}
       \exp[-nt^2/(8C_{S,M}^2)].
 \]
Union over the four families, all \(E,F\), both sizes, and the \(N\)
grid times explains the logarithm \(32n^2N/\eta\) in (1).
After imposing the full initial operator event, interpolation costs
\(C_{S,M}/\sqrt n\).

It follows simultaneously for all actual, adaptively chosen vectors
\(u\), all times, sets \(E\), and \(j=0,1,2,3\), that
\[
 \|GC_ju\|_n
 \le C_{S,M}\left[
 Q_0(\sqrt{h(p)}+\epsilon_n)
                +\ell\sqrt{\log(eQ_0/\ell)}\right]
 \tag{7}
\]
whenever \(\|u\|_n\le Q_0\) and
\(\|u\|_{1,n}\le\ell\le Q_0\).
Zero values are interpreted as in the sorted-block lemma.
In particular a uniformly \(L^2_n\)-bounded vector whose
\(L^1_n\) norm is at most \(C_{S,M}d_E\) has image bounded by
\(C_{S,M}[\sqrt{h(p)}+\mu(d_E)+\epsilon_n]\).
An \(L^1_n\) bound \(C_{S,M}(d_E+\sqrt p)\) gives the same result,
because \(\mu(d+\sqrt p)\le
C[\mu(d)+\sqrt{h(p)}]\).

## 3. Pointwise pruned derivative and velocity queries

The deleted reference top columns are frozen, so
\[
 P\widehat q'=G\,\widehat\delta^{(3)\prime}.
 \tag{8}
\]
Select \(\widehat\delta^{(3)\prime}\) to be zero outside
\(\Omega_E^{\rm top}\). Its entire path is independent of \(G\),
has \(L^2_n\) norm \(O(1)\), and has time-Lipschitz constant
\(O(\sqrt n)\) by (5).
The fixed-time conditional Gaussian vector bound, union over all
sets and grid times, and interpolation on the full initial norm
event give the first bound in (2), with failure \(\eta/4\).

For \(\widehat g_E=PW^{(2)}_0\widehat h^{(1)\prime}\), select the
reference vector path using \(\Omega_E^{\rm in}\), not
\(\Omega_E^{\rm top}\). It is independent of the deleted incoming
rows. Its normalized norm is \(O(1)\), and (5) gives its
time-Lipschitz constant \(O(\sqrt n)\). The same query proof,
with another allocation \(\eta/4\), gives the second bound in (2).
The logarithmic query costs are only
\(\log(4nN/\eta)/n\), dominated by (1).
Neither independence is asserted after conditioning on the full
initial-operator event; that event is imposed afterward.

## 4. Exact top telescoping and its nonindependent self-return

Let
\[
 u_2=h^{(2)\prime}=D_2A_2\delta^{(2)},\qquad
 \widehat u_2=Q\widehat D_2\widehat A_2\widehat\delta^{(2)},
 \]
and \(m_2=\|h^{(2)}\|_n^2\).
The exact formulas are
\[
 q'=h^{(2)}\|\delta^{(3)}\|_n^2+W^*\delta^{(3)\prime},
 \tag{9}
\]
\[
 \delta^{(3)\prime}
       =D_3h^{(3)}+Bz^{(3)\prime},\qquad
 z^{(3)\prime}=m_2\delta^{(3)}+Wu_2.
 \tag{10}
\]
The actual learned top columns on \(E\) satisfy
\[
 \|(W-W^{(3)}_0)P\|_{\rm F}
 \le\int_0^S\|\delta^{(3)}\|_n\|Ph^{(2)}\|_n\,ds
 \le C_S\sqrt p .
 \tag{11}
\]
Since \(\|\delta^{(3)\prime}\|_n\le C_{S,M}\), (9) implies
\[
 Pq'=G\delta^{(3)\prime}+r_E,\qquad
 \|r_E\|_n\le C_{S,M}\sqrt p.
 \tag{12}
\]

The primal comparison maps give
\(\|q-\widehat q\|_n\le C_{S,M}(d_E+\sqrt p)\),
\(\|Q(z^{(2)}-\widehat z^{(2)})\|_n\le C_{S,M}d_E\),
and analogous bounds for top features and backward fields.
Telescope (10) in the order
\[
 \begin{split}
 \delta^{(3)\prime}-\widehat\delta^{(3)\prime}
 ={}&r_{\rm sm}+u_0+\widehat B\,VPu_2
                    +\widehat B\,VQ(u_2-\widehat u_2),\\
 u_0={}&(B-\widehat B)z^{(3)\prime},
 \end{split}                                                   \tag{13}
\]
where EXACTLY
\[
 r_{\rm sm}
 =D_3h^{(3)}-\widehat D_3\widehat h^{(3)}
 +\widehat B(m_2\delta^{(3)}
                    -\widehat m_2\widehat\delta^{(3)})
 +\widehat B(W-V)u_2 .
 \]
This vector has \(L^2_n\) norm at most
\(C_{S,M}(d_E+\sqrt p)\). The vector \(u_0\) has bounded
\(L^2_n\) norm and \(L^1_n\) norm at most that same quantity,
because \(B-\widehat B\) is bounded in \(L^\infty\) and
\(\|B-\widehat B\|_n\le C_{S,M}(d_E+\sqrt p)\).
Thus \(Gr_{\rm sm}\) is small by the operator bound, and
\(Gu_0=GC_0u_0\) is controlled by (7).

The term \(G\widehat BVPu_2\) is NOT treated as a conditional
Gaussian product: \(VP=W^{(3)}_0P=G^*\) contains the deleted
columns themselves. Use the deterministic operator bound instead:
\[
 \|G\widehat BVPu_2\|_n\le C_{S,M}\|Pu_2\|_n.
 \tag{14}
\]
The exact scalar-reduction identity gives
\[
 PA_2\delta^{(2)}
       =\alpha_E P\delta^{(2)}+\rho_E+\widehat g_E.
 \]
Since \(Pu_2=PD_2A_2\delta^{(2)}\) and \(D_2\) is bounded,
\[
 \|Pu_2\|_n
 \le C_S\|P\delta^{(2)}\|_n+\|\rho_E\|_n+\|\widehat g_E\|_n.
 \tag{15}
\]
This is the retained actual rare self-feedback.

## 5. Exact bulk telescoping: only three additional small-L1 vectors

For shorter formulas write \(\delta=\delta^{(2)}\) and
\(\widehat\delta=\widehat\delta^{(2)}\).
The bulk velocity difference is exactly
\[
 Q(u_2-\widehat u_2)
 =Q(D_2-\widehat D_2)A_2\delta
  +Q\widehat D_2(A_2-\widehat A_2)\delta
  +Q\widehat D_2\widehat A_2(\delta-\widehat\delta).
 \tag{16}
\]
The first term is the vector
\[
 u_1=Q(D_2-\widehat D_2)A_2\delta,
 \]
with bounded \(L^2_n\) norm and \(L^1_n\) norm at most
\(C_{S,M}d_E\). After the outer \(\widehat B VQ\), it is
exactly \(GC_1u_1\).

For the second term expand the full mobility difference:
\[
 \begin{split}
 A_2-\widehat A_2
 ={}&(m_1-\widehat m_1)I
       +(L-K)D_1^2L^*\\
    &+K(D_1^2-\widehat D_1^2)L^*
       +K\widehat D_1^2(L-K)^* .
 \end{split}                                                   \tag{17}
\]
Every term except the third has operator norm at most
\(C_{S,M}d_E\). The third produces
\[
 u_2^{\rm gate}
       =(D_1^2-\widehat D_1^2)L^*\delta ,
 \]
with bounded \(L^2_n\) norm and \(L^1_n\) norm at most
\(C_{S,M}d_E\). Its outer coefficient is exactly \(GC_2\).
Here the inner \(L^*\delta\) may depend on the deleted top
columns; that dependence is allowed in the adaptive input vector.

For the third term of (16), in the uncut case,
\[
 \delta-\widehat\delta
 =P\delta+QD_2(q-\widehat q)
                   +Q(D_2-\widehat D_2)\widehat q .
 \tag{18}
\]
The rare part costs \(C_{S,M}\|P\delta\|_n\) by bounded
operators. The middle part costs \(C_{S,M}(d_E+\sqrt p)\).
The final vector
\[
 u_3=Q(D_2-\widehat D_2)\widehat q
 \]
has bounded \(L^2_n\) norm and \(L^1_n\) norm at most
\(C_{S,M}d_E\). Its outer coefficient is exactly \(GC_3\).
Thus (7) applies to all three exceptional vectors.

For common clipping, replace \(q-\widehat q\) in (18) by
\(\tau(q)-\tau(\widehat q)\), and replace \(\widehat q\) in
\(u_3\) by \(\tau(\widehat q)\). All bounds are unchanged.
The outer \(D_2\) in \(u_2=h^{(2)\prime}\) is still the
activation derivative, not a derivative of \(\tau\).

## 6. Combination and probability accounting

Give the off-block/residual event of
SINGLE_PRUNED_OFFBLOCK_OSGOOD.md failure allocation \(\eta/4\).
Its logarithm becomes \(\log(24n^2N/\eta)/n\), dominated by
(1), and it supplies
\[
 \|\rho_E(s)\|_n
       \le C_{S,M}[\sqrt{h(p)}+\mu(d_E(s))+\epsilon_n].
 \tag{19}
\]
Combine (7), (8), and (12)--(19). This proves (3).
The separately established incoming-row velocity query in (2)
then proves (4).

The four allocations are: \(\eta/4\) for all four Gaussian
operator families together; \(\eta/4\) for the pruned backward
derivative query; \(\eta/4\) for the pruned forward velocity query;
and \(\eta/4\) for the previously proved residual estimate.
All are uniform over sets and time before selecting an actual
rare set. No independence between their good events is needed.
For \(\eta=1/n\) the width error tends to zero.

This establishes a rare backward DERIVATIVE estimate. It retains
the actual rare backward action in (4), and it does not differentiate
a primal bound to infer a response bound. Any energy or full-state
consequence requires its own argument.
