# No-self-loop diagram audit

**Date:** 23 August 2026.

**Verdict:** diagonal-return resummation is necessary, but it is not enough
to justify Wick singleton or collision gains.  After resummation, the
coefficient of an explicit raw Gaussian edge remains adapted to that edge.
Gaussian integration by parts differentiates the coefficient and creates a
second response.  A concrete Gaussian star transport shows that centered
index-changing edges, zero row sum, bounded operator norm, and time-simplex
weights can still produce lognormal amplification.  This falsifies a generic
diagram lemma, not the canonical network conjecture, whose actual source is
Frobenius-delocalized.

## 1. Earliest invalid centering

After a Duhamel expansion, an apparent singleton edge has the form

\[
 \xi_e F_e(\xi),                                      \tag{1.1}
\]

where the dressed return blocks inside \(F_e\) still depend on \(\xi_e\).
It is therefore false to delete (1.1) by centering.  Exactly,

\[
 \mathbb E[\xi_eF_e(\xi)]=\mathbb E[\partial_eF_e(\xi)],              \tag{1.2}
\]

and, if \(\xi^{(e)}\) denotes the disorder with edge \(e\) set to zero,

\[
 F_e(\xi)-F_e(\xi^{(e)})
 =\xi_e\int_0^1\partial_eF_e(\xi^{(e)}+s\xi_e e)\,ds.                 \tag{1.3}
\]

For the tangent system, \(F_e\) already contains first-response
propagators.  Its derivative contains second responses and products of first
responses.  Thus (1.2) does not lower diagram depth or derivative order.
Iterating it through a \(p\)-th moment recreates the all-reaching
high-derivative hierarchy.

The scalar example

\[
 F_t(\xi)=e^{t\xi-t^2/2},\qquad \xi\sim N(0,1),                       \tag{1.4}
\]

has

\[
 \mathbb E[\xi F_t]=t,\qquad
 \partial_\xi^rF_t=t^rF_t,\qquad
 \|F_t\|_p=e^{(p-1)t^2/2}.                                           \tag{1.5}
\]

Time ordering and exact resummation alone therefore do not imply polynomial
moment growth.

## 2. Gaussian star counterexample to the generic transport lemma

Let \(\xi_1,\ldots,\xi_m\) be iid standard Gaussians and use vertices
\(0,1,\ldots,m\).  Put

\[
 K_{0k}=K_{k0}=\frac{\xi_k}{\sqrt m},\qquad
 b_0=0,\qquad b_k=-1\quad(k\ge1),                                    \tag{2.1}
\]

with all other off-diagonal entries zero.  Adding
\(\|K_{\rm off}\|_{\rm op}I\) makes \(K\) PSD without changing the
zero-row-sum transport

\[
 [\mathcal T_{K,b}y]_i=\sum_kK_{ik}b_k(y_k-y_i).                      \tag{2.2}
\]

Moreover,

\[
 \|K_{\rm off}\|_{\rm op}
 =\left(m^{-1}\sum_{k=1}^m\xi_k^2\right)^{1/2},                       \tag{2.3}
\]

so its moments are dimension-free.  Starting from
\(y_0(0)=1,y_k(0)=0\), the leaf coordinates stay zero while

\[
 y_0'=s_my_0,qquad
 s_m=m^{-1/2}\sum_{k=1}^m\xi_k\sim N(0,1).                            \tag{2.4}
\]

Hence

\[
 y_0(t)=e^{ts_m},\qquad \|y_0(t)\|_p=e^{t^2p/2}.                      \tag{2.5}
\]

Thus the following properties do not suffice for a \(C_Tp\) propagator
bound: no self-loops, centered \(m^{-1/2}\)-Gaussian index-changing edges,
zero row sum, bounded operator norm, normalized amplitudes, and exact
time-simplex factors.

## 3. What remains model-specific

The example uses a localized source.  The canonical column derivative starts
as

\[
 D_gB_3(0)=\frac{X_{2,j}(0)}{\sqrt n}
 \operatorname{diag}\{A_{0,i}d'(Z_{3,i}(0))\},                       \tag{3.1}
\]

whose Hilbert--Schmidt energy is spread over \(n\) rows.  The target norm is
also an averaged Frobenius norm.  A valid theorem could therefore exclude
(2.5) by proving that the actual response never concentrates enough mass on
a coherent amplified mode.

That missing statement must be explicit—for example, a propagated inverse
participation, leverage-entropy, or jointly dressed block-cavity estimate.
It must be stable under disorder-adapted restart data and use at most a
constant-factor increase in moment order.  It cannot be inferred from the
generic structural properties falsified above.
