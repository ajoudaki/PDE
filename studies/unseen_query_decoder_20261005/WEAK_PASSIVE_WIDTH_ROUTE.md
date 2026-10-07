# Weak scalar estimates and the polynomial-width question

2026-10-07. Bounded author continuation suggested by the supervisor, not an
independent review. No experiment or implementation. The original model,
label allowance, current-state query interface, whole sphere, all physical
times, and fitted endpoint remain the target. Only this note is written.

**Outcome.** A rank-\(R\) covariance change has an \(R/n\) weak scalar
bound when the continued prediction has Hessian norm \(O(1/n)\). That
condition holds for a single final activation with uniformly bounded
normalized readout coordinates. It does not follow for earlier layers
from the operator and common-Gram bounds in the current passive proof.
An explicit bounded-activation continuation has a weak error of order
\(n^{-1/2}\). A separate example gives the same order of empirical
population bias with exact matching pair tables and bounded posterior
entropy. Neither example is claimed to be a reachable history of the
original Gaussian trained network.

Thus the suggested first-order cancellation is useful but insufficient
under the supplied interfaces. Even a stronger weak theorem would still
need a new transfer from conditional means to the existing dense-center
high-probability statement. The complete polynomial-onset theorem remains
open; this note supplies precise lemmas and obstructions to this proof route.

## 1. Objects and the unchanged question

Use the setup of FAST_FINITE_PASSIVE.md in full. In particular, \(n\)
is dense width, \(L\) is depth, \(Y=\|y\|_2/\sqrt m>0\), and
\(R\) bounds the current number of named history fields. The activation
cap satisfies

\[
 |\psi_\ell|\le\mathcal B,\qquad
 |\psi_\ell'|\le a_1,\qquad |\psi_\ell''|\le a_2,
\]

with the supplied polynomial-in-regularity bounds. These query caps agree
with the original activations on the physical good event; they do not
restrict the original activation class. Let \(\pi_c\) be the packet-array
posterior at a current scalar prefix \(c\), let \(\nu_c\) be its common
one-row marginal, and let \(\mu\) be the finite packet prior. The source
provides

\[
 D(\pi_c\Vert\nu_c^{\otimes n})\le K_*,\qquad
 D(\nu_c\Vert\mu)\le K_*/n.
 \tag{1}
\]

The relevant Gaussian answer at a fixed complete physical history has
mean \(m\in\mathbb R^n\) and covariance

\[
 \Gamma=vI-K,\qquad 0\preceq K\preceq vI,
 \qquad\operatorname{rank}K\le R,
 \qquad v\le\sigma_q^2+\mathcal B^2.
 \tag{2}
\]

Here \(v\) is a local variance, not a new input variable. The passive
proof replaces this covariance by \(vI\). Its current strong comparison
costs \(C\mathcal P\sqrt{R/n}\) in normalized prediction, where
\(\mathcal P\) is the supplied fixed-depth amplification.

For a passive layer the integrated row map is

\[
 T(b,u)=\mathbb E_{\nu_c,g}\left[
 \begin{pmatrix}V\,\psi(U^\top A b+\sqrt{s(b,u)}g)\\
                 \psi(U^\top A b+\sqrt{s(b,u)}g)^2
 \end{pmatrix}\right],
 \quad s(b,u)=\sigma_q^2+u-\|Pb\|^2,
 \tag{3}
\]

on its feasible moment domain. Here \(b\) is the cross-moment vector and
\(u\) the scalar second moment; the source prefix \(c\) stays fixed.
Below we combine the two moment arguments as \(\theta=(b,u)\).
The common marks have
\(\nu_c(UU^\top),\nu_c(VV^\top)\preceq I\), and
\(\|A\|\le\mathcal C\), \(\|P\|\le1\). The finite-array version
replaces the row expectation by its empirical average and uses the
preceding empirical moments. The source compares its output to the
population recursion by an RMS bound of order
\(\mathcal P\sqrt{(K_*+R+1)/n}\).

The requested improvement concerns those two bounds. It must not silently
change a comparison of conditional expectations into a high-probability
statement, or replace the prior \(\mu\) actually sampled at queries by
the proof-only posterior \(\nu_c\).

## 2. The exact weak covariance lemma

Let \(F:\mathbb R^n\to\mathbb R\) be a bounded \(C^2\) function,
with bounded first and second derivatives, and suppose

\[
 \sup_z\|D^2F(z)\|_{\rm op}\le H/n.
 \tag{4}
\]

For \(X_0\sim N(m,\Gamma)\) and \(X_1\sim N(m,\Gamma+K)\),
where \(K\succeq0\),

\[
 |\mathbb EF(X_1)-\mathbb EF(X_0)|
 \le\frac{H\operatorname{tr}K}{2n}
 \le\frac{HvR}{2n}
 \tag{5}
\]

under (2).

To prove it, take independent standard Gaussian vectors \(g,h\) and
\(X_u=m+\Gamma^{1/2}g+\sqrt u K^{1/2}h\). For \(u>0\),
differentiation and integration by parts in each coordinate of \(h\)
give

\[
 \frac{d}{du}\mathbb EF(X_u)
 =\frac12\mathbb E\operatorname{tr}(KD^2F(X_u)).
 \tag{6}
\]

For example, before integration by parts the derivative is
\(\mathbb E[\nabla F(X_u)^\top K^{1/2}h]/(2\sqrt u)\);
the derivative of \(\nabla F\) with respect to \(h\) contributes
\(\sqrt u D^2F K^{1/2}\). Bounded derivatives justify integration
and differentiation. The resulting bounded expression extends to
\(u=0\), including singular covariances. Integrate from zero to one
and use
\(|\operatorname{tr}(KH)|\le\operatorname{tr}K\|H\|_{\rm op}\)
for symmetric \(H\) and positive \(K\). This proves (5).

For a final-layer normalized readout

\[
 F(z)=\frac1n\sum_{i=1}^n\frac{w_i}{Y}\psi_L(z_i),
\]

the Hessian is diagonal, and (4) holds with
\(H=a_2\|w/Y\|_\infty\). Hence its weak covariance defect is at most

\[
 \frac{a_2\|w/Y\|_\infty(\sigma_q^2+\mathcal B^2)R}{2n}.
 \tag{7}
\]

The coordinate bound in (7) must be justified, not replaced by the
supplied RMS bound. A precise way to obtain it, if its hypotheses are
available, is as follows. Suppose physical training features satisfy
\(|h_{a,i}^{(L)}(t)|\le B\) and the residual obeys
\(\|r(t)\|_2\le\sqrt mY e^{-\lambda t}\), for \(\lambda>0\).
The actual readout equation and zero initialization give

\[
 |\dot w_i(t)|\le\frac2m\|r(t)\|_2\sqrt mB
 \le2BYe^{-\lambda t},\qquad
 \|w(t)/Y\|_\infty\le2B/\lambda.
 \tag{8}
\]

This is an exact conditional implication. It does not assert an
unprovided value of the physical decay rate. If, for example, an already
verified rate is \(\lambda=\gamma/m\), (7) has factor
\(2a_2Bm/\gamma\). No additional restriction on labels is introduced.

## 3. Earlier layers need a stronger continuation estimate

For an earlier-layer covariance interpolation, \(F\) in (4) is the
complete scalar prediction after the remaining nonlinear layers,
averaged over their independent conditional Gaussian matrices. Bounded
matrix operator norms and bounded final readout coordinates do not
imply (4) with width-independent \(H\).

An exact deterministic-continuation example makes this failure visible.
Let \(\mathbf1\in\mathbb R^n\) be the all-ones vector and
\(e_1\) its first coordinate vector, and put

\[
 M=\frac{\mathbf1e_1^\top}{\sqrt n},\qquad
 F(z)=\frac1n\mathbf1^\top\tanh(M\cos z)
     =\tanh\left(\frac{\cos z_1}{\sqrt n}\right).
 \tag{9}
\]

Activations act coordinatewise. Both are bounded real analytic with
bounded first and second real derivatives. The downstream matrix has
\(\|M\|_{\rm op}=1\); the readout has every coordinate equal to one
and normalized RMS one.

Take \(\Gamma=I-(3/4)e_1e_1^\top\), \(K=(3/4)e_1e_1^\top\),
and mean zero. Both covariances are strictly positive, \(R=1\), and
\(v=1\). If \(G\sim N(0,1)\), then

\[
 \mathbb EF(X_0)-\mathbb EF(X_1)
 =\mathbb E\tanh\left(\frac{\cos(G/2)}{\sqrt n}\right)
  -\mathbb E\tanh\left(\frac{\cos G}{\sqrt n}\right).
\]

The elementary Gaussian identity \(\mathbb E\cos(aG)=e^{-a^2/2}\)
follows by differentiating its characteristic function and integrating
by parts. Also
\(|\tanh x-x|\le |x|^3/3\): integrate
\(|1-\tanh'(x)|=\tanh^2x\le x^2\) from zero. Therefore

\[
 \mathbb EF(X_0)-\mathbb EF(X_1)
 \ge\frac{e^{-1/8}-e^{-1/2}}{\sqrt n}
                  -\frac{2}{3n^{3/2}}
 \ge\frac{e^{-1/8}-e^{-1/2}}{2\sqrt n},\qquad n\ge8.
 \tag{10}
\]

For the last inequality one can use
\(e^{-1/8}(1-e^{-3/8})\ge(7/8)(3/11)=21/88\).
The corresponding Hessian has a first-coordinate second derivative of
order \(n^{-1/2}\), so (4) would require \(H\) of order \(\sqrt n\).

This is not claimed to be a positive-probability training history of the
original network, nor a complete example with the exact remaining-layer
Gaussian posterior. It proves the narrower point that the deterministic
operator/readout bounds used in a layer hybrid do not imply the desired
scalar Hessian estimate. The forward rank-one matrix turns a change at
one coordinate into an aligned change at every output coordinate.
Its backward vector \(M^\top\mathbf1=\sqrt n e_1\) exposes the missing
coordinatewise influence control. A probabilistic bound exploiting the
actual conditional neural law could rule out this configuration; that
bound is a substantive new premise, not supplied by an operator norm.

## 4. Exactly what a second-order population expansion needs

Here is a useful abstract lemma retaining the genuine first-order
cancellation. Let \(\theta\in\mathbb R^q\) be deterministic and
\(\theta_n\) a random incoming moment vector. Set
\(\Delta=\theta_n-\theta\). Let

\[
 T_n(u)=\frac1n\sum_{i=1}^n t(Z_i;u),\qquad
 T(u)=\mathbb E_{\nu_c}t(Z;u),
 \tag{11}
\]

where the array has common marginal \(\nu_c\); it need not be iid.
Suppose the maps are \(C^2\) on all segments joining \(\theta\) to
\(\theta_n\), derivatives can pass through the expectation, and

\[
 \|DT(\theta)\|\le A_0,\quad
 \mathbb E\|DT_n(\theta)-DT(\theta)\|^2\le v_D^2,
 \quad\mathbb E\|\Delta\|^2\le v_\theta^2,
 \quad\sup_u\|D^2T_n(u)\|\le H_0.
 \tag{12}
\]

The last norm is the bilinear operator norm, and the supremum is over
those segments for every relevant array. Then

\[
 \|\mathbb ET_n(\theta_n)-T(\theta)\|
 \le A_0\|\mathbb E\Delta\|
                    +v_Dv_\theta+\tfrac12H_0v_\theta^2.
 \tag{13}
\]

Indeed Taylor's formula with integral remainder gives

\[
 T_n(\theta_n)=T_n(\theta)+DT_n(\theta)\Delta+\mathcal R,
 \qquad\|\mathcal R\|\le H_0\|\Delta\|^2/2.
\]

Exchangeability gives \(\mathbb ET_n(\theta)=T(\theta)\). Split the
linear term into \(DT(\theta)\mathbb E\Delta\) and
\(\mathbb E[(DT_n(\theta)-DT(\theta))\Delta]\), and use
Cauchy--Schwarz on the latter. This proves (13). The random empirical
derivative is correlated with the preceding empirical moments; its
linear term does not simply vanish.

If \(v_D^2\le D_0(K_*+R+1)/n\),
\(v_\theta^2\le V_0(K_*+R+1)/n\), and the incoming mean error is
\(O((K_*+R+1)/n)\), then (13) provides the desired one-stage order,
with explicit coefficient
\(\sqrt{D_0V_0}+H_0V_0/2\) and propagation factor \(A_0\).
A fixed-depth induction is legitimate if these bounds hold at every
stage with the necessary parameter control.

The current passive hypotheses do not establish (12). Differentiating
the mean part of (3) produces integrands containing \(VU^\top\);
their second moments involve products such as \(V_i^2U_j^2\).
Second derivatives involve \(V_iU_jU_k\), and a simple uniform
bound can require still higher mark moments. Separate second-moment
Gram bounds on \(U,V\) do not control these products. The finite
numerical cap only gives a possibly enormous cap with logarithm
\(C\chi\); using its actual magnitude in \(H_0,D_0\) can erase
the supposed width saving.

Variance derivatives require care as well. After integrating the fresh
Gaussian, a first derivative in variance uses \(\psi''/2\), and a
second derivative uses \(\psi^{(4)}/4\). Strip analyticity supplies
higher original-activation estimates via Cauchy bounds, but a chosen
cap must have its corresponding derivative bounds specified. The
feasible set \(u\ge\|Pb\|^2\) is convex, so a segment between two
feasible contexts avoids the artificial clipping kink. An arbitrary
guarded context outside that set does not automatically have this
smoothness. These requirements are in addition to, not consequences of,
the first-order weak inequalities in the existing note.

## 5. Exact pair matching does not supply the missing moments

The following example verifies the obstruction with finite packets,
exchangeable conditioning, exact common pair tables, and bounded entropy.
It is a counterexample to an estimate based only on these interfaces,
not a claimed neural realization.

Let \(n\ge8\). A prior row \((U,\xi)\) is zero with probability
\(1-4/n\). For each
\(\xi\in\{-7,-5,-3,-1,1,3,5,7\}\), it instead has
\(U=\sqrt n/2\) and that value of \(\xi\), with probability
\(1/(2n)\). Let \(\mu\) be this finite law. Start with iid rows,
then condition on the event \(E\) that exactly four rows are active,
\(\sum_i\xi_i=0\), and \(\sum_i\xi_i^2=84\). Write \(\pi\)
for the resulting array law.

The active multiset must be either

\[
 \{-7,-1,3,5\}\quad\text{or}\quad\{7,1,-3,-5\}.
 \tag{14}
\]

To verify this, two entries of magnitude seven already contribute more
than 84 to the sum of squares. With one such entry, the other squared
magnitudes must be 25, 9, and 1; the zero sum fixes their signs as in
(14). With no seven, the only four squared magnitudes adding to 84 are
25, 25, 25, and 9, whose signed values cannot sum to zero. The prior
gives both multisets equal weight, and all row placements are uniform.
Consequently the one-row posterior marginal is exactly \(\nu=\mu\).

The probability of \(E\) is

\[
 \Pr(E)=\frac{(n)_4}{8n^4}(1-4/n)^{n-4}
 \ge\frac{105}{2048}e^{-4},
 \quad (n)_4=n(n-1)(n-2)(n-3).
 \tag{15}
\]

Here \((n)_4/n^4\ge105/256\) for \(n\ge8\), and
\(\log(1-u)\ge-u/(1-u)\) gives
\((1-4/n)^{n-4}\ge e^{-4}\). Thus

\[
 D(\pi\Vert\nu^{\otimes n})=\log(1/\Pr(E))
 \le4+\log(2048/105),\qquad D(\nu\Vert\mu)=0.
 \tag{16}
\]

For the complete raw mark vector \((1,U,\xi)\), every array in the
conditional support has the same empirical pair table as its population:

\[
 Q=\begin{pmatrix}
 1&2/\sqrt n&0\\
 2/\sqrt n&1&0\\
 0&0&84/n
 \end{pmatrix}.
 \tag{17}
\]

It is positive definite for \(n\ge8\). Whitening by \(Q^{-1/2}\)
makes the empirical and population Grams exactly identity. In these
coordinates the rank-one mean mixer \(UU^\top/n\) still has operator
norm one, since \(n^{-1}\sum_iU_i^2=1\), and the readout \(U\)
has normalized RMS one. A small positive common ridge changes these
equalities by arbitrarily small controlled amounts; it does not remove
the order found below.

Take the first feature to be \(h_i=\tanh\xi_i\), and set

\[
 a=\frac{-\tanh7-\tanh1+\tanh3+\tanh5}{4}>0,
 \quad c_n=\frac{\tanh^27+\tanh^21+\tanh^23+\tanh^25}{n}.
 \tag{18}
\]

The strict positivity follows because \(\tanh3-\tanh1\) is the
integral of the decreasing positive function \(\operatorname{sech}^2\)
over \([1,3]\), and exceeds its integral over \([5,7]\).
The empirical incoming cross moment is
\(b_n^{\rm emp}=\pm2a/\sqrt n\), with equal probabilities; its
population value is zero. Its empirical second moment is exactly
\(c_n\), also the population value.

Use a second passive activation \(\cos\), mean coefficient one,
variance matrix \(P=0\), and fresh iid standard Gaussian marks \(g_i\).
For \(0<\sigma_q^2\le1\), put \(v_n=\sigma_q^2+c_n\). The
normalized scalar array output is

\[
 F_n=\frac1n\sum_i U_i
          \cos(U_i b_n^{\rm emp}+\sqrt{v_n}g_i).
 \tag{19}
\]

Its passive population counterpart uses the same \(\nu\), the same
variance, and incoming cross moment zero. Integrating the fresh Gaussians
and using (14) yields exactly

\[
 \mathbb E_{\pi,g}F_n=\frac{2e^{-v_n/2}\cos a}{\sqrt n},
 \qquad F_{\rm pop}=\frac{2e^{-v_n/2}}{\sqrt n}.
 \tag{20}
\]

Since \(c_n\le4/n\) and \(n\ge8\),

\[
 |\mathbb E_{\pi,g}F_n-F_{\rm pop}|
 \ge\frac{2e^{-3/4}(1-\cos a)}{\sqrt n}>0.
 \tag{21}
\]

The incoming empirical moment has zero mean error. Nevertheless the
next integrated map is
\(T(b)=2e^{-v_n/2}\cos(\sqrt n\,b/2)/\sqrt n\), with
\(T''(0)=-(\sqrt n/2)e^{-v_n/2}\). Its second-order coefficient
grows as \(\sqrt n\). Equivalently,
\(\nu U^4=n/4\) although \(\nu U^2=1\).
This identifies the exact missing hypothesis in (12). The entropy bound
and the common Grams are all satisfied with constant dimension and
constant information, but the proposed universal \(O((K_*+R)/n)\)
bound is false for this abstract passive system.

The conditioning in this example can also be approximated by the rounded
Gaussian shadow channel, without relying on a zero-noise channel. Restrict
to \(n=4^k\), acquire all six pair tests of \((1,U,\xi)\), and use
independent Gaussian scalar noise and grid width
\(\eta=h=n^{-3}\). Condition on the code equal to (17). Every array
in \(E\) has that code with probability \(p_0^6\), where
\(p_0=\Pr\{|G|\le1/2\}>0\). Every array outside \(E\) disagrees
in at least one of the count, \(\xi\), or \(\xi^2\) moments by at
least \(1/n\). In that scalar channel, reaching the indicated cell
requires \(|G|\ge n^2-1/2\), whose probability is at most
\(C e^{-c n^4}\), as follows by integrating the Gaussian tail.
Thus the conditioned noisy posterior has total variation distance at
most \(C e^{-c n^4}/[\Pr(E)p_0^6]\) from \(\pi\).
Its density relative to the product prior is at most
\([\Pr(E)p_0^6]^{-1}\), so its array entropy is still bounded by
a universal constant. Marginals, bounded row moments, and (20) change
by at most polynomial-in-\(n\) times this exponentially small error.
The weak root-width bias therefore persists. This strengthens the
finite-packet shadow-channel example; it still supplies no neural
provenance for the spiky marks or readout, or the detailed compatibility
of all mean/covariance coefficients with a trained Gaussian matrix history.

In actual neural training, (8) or another coordinatewise response bound
may exclude the spiky readout \(U\). A successful positive theorem must
use such additional structure throughout the continuation, including
backward influences and derivative moments. It cannot follow solely from
the upper Grams that the current weak-recursion proof records.

## 6. Fixed exceptional mass blocks a mean-based center transfer

The existing two-filtration proof uses high-mass intervals. The physical
and shadow arrays agree on a coupling event \(\mathcal G\); each good
prefix has conditional mass at least \(1-q_0\) in that event, with
fixed \(q_0=1/64\). This suffices for interval intersection. It does
not suffice to compare conditional means at vanishing error.

First, if a scalar \(X\) obeys \(|X-f_0|\le b\) outside an event
of mass \(q\), and \(|X-f_0|\le M\) globally, the available bound is

\[
 |\mathbb EX-f_0|\le b+Mq.
 \tag{22}
\]

Its \(q\)-term is necessary in general: take \(X=f_0\) with
probability \(1-q\), and \(X=f_0+M\) otherwise. The same obstruction
occurs after outer clipping to a known physical range. Clipping bounds
\(M\); it does not make fixed \(q\) tend to zero.

Second, at a common prefix, normalize the common matched output measure
on \(\mathcal G\) to a probability law \(R_c\). Each of the two
conditional output laws contains a multiple of \(R_c\) of weight at
least \(1-q_0\). Their conditional total variation distance is therefore
at most \(q_0\): take the smaller of those two weights as their common
submeasure. For outputs clipped to \([-M,M]\), this only gives

\[
 |\mathbb E[X_{\rm ph}\mid c]-\mathbb E[X_{\rm sh}\mid c]|
 \le2Mq_0.
 \tag{23}
\]

The relative weights are handled here without dividing an unconditional
TV bound by a rare-prefix probability. Even this correct conditional
comparison leaves a width-independent error.

The empirical Gram estimate in FAST_FINITE_PASSIVE.md (27) has a related
issue: it controls an RMS error multiplied by the good empirical-Gram
indicator, whose complement has fixed conditional mass. Zero full
expectation of an empirical linear fluctuation does not imply zero
expectation after that indicator is inserted. In fact
\(\mathbb E[\Delta1_G]= -\mathbb E[\Delta1_{G^c}]\) whenever
\(\mathbb E\Delta=0\). Without a global tail moment bound the latter
term cannot be bounded by \(O((K_*+R)/n)\).

If a normalized output cap is \(M\), forcing (22)--(23) below the
normalized benchmark \(b_n/Y\) needs bad conditional mass of order
\(b_n/(YM)\). The first-crossing argument then requires the underlying
scientific failure probability to be at most a constant times
\(\delta b_n/(YM)\). The existing proof expressly uses its scientific
events at fixed confidence shares. Reapplying them with this
width-dependent confidence needs new width, coefficient, and resource
estimates; it is not an allowed free numerical-precision tightening.

Finally a smooth-indicator route also has a precise cost. Suppose a weak
comparison has the form

\[
 |\mathbb Ef(X)-\mathbb Ef(Y)|\le\varepsilon\|f''\|_\infty
 \tag{24}
\]

for bounded twice differentiable scalar tests. Choose a smooth cutoff
equal to one on an interval and zero outside its enlargement by radius
\(a\), with second derivative at most \(C/a^2\). Such a cutoff is
obtained by rescaling a fixed smooth transition twice, one at each
endpoint. Applying (24) transfers interval probability with loss at most
\(C\varepsilon/a^2\). To keep that loss below a fixed constant one
therefore needs \(a\ge C\sqrt\varepsilon\). A weak error
\(\varepsilon=C(K_*+R)/n\) only recovers the former root-width
interval radius by this argument. A better quantile estimate would need
additional distributional information, not just (24).

## 7. Consequences for the original target

The earlier polynomial-onset note already isolates the additional prior
versus posterior sampling discrepancy. Nothing in a weak expansion of
\(\pi_c\) around \(\nu_c\) bounds a prior query estimator's error
around \(\nu_c\) more sharply. A posterior-valid control variate or a
counted posterior evaluation method remains a separate requirement.

A positive theorem along the suggested route would therefore need all
of the following substantive statements for the actual neural source:

1. A normalized scalar continuation Hessian bound, or a more specific
   covariance-contraction bound, strong enough to replace (2) by an
   \(R/n\) weak error without width-growing coefficients.
2. Derivative concentration and higher mark-moment control sufficient
   for (12)--(13), uniformly over the actual reachable prefixes and
   passive contexts, with the guarded/tail contributions included.
3. A mean-to-dense-center or direct quantile theorem that eliminates
   the fixed exceptional-mass terms in (22)--(23) at the unchanged
   probability and error benchmark.
4. A compact, counted evaluation mechanism handling the remaining
   posterior/prior discrepancy.

The exact lemmas (5), (8), and (13) are reusable partial results. Examples
(9)--(10) and (14)--(21) prevent inferring their needed hypotheses from
operator norms, common Grams, and entropy alone. All statements are
single-context mathematical implications; they do not themselves produce
the single whole-sphere/all-time success event required by the user.
No new decoder state, seed, or runtime is claimed, and no additional
scientific assumption has been inserted into the headline result.

## 8. Check status and provenance

| Statement | Author check and boundary |
|---|---|
| Covariance interpolation (5) | Complete differentiation, Gaussian integration by parts, and trace estimate above |
| Final readout implication (7)--(8) | Exact conditional algebra; physical decay/coordinate bounds must be supplied |
| Earlier-layer root-width weak example (10) | Complete analytic estimate; no neural reachability claim |
| Empirical expansion (13) | Exact Taylor decomposition including the correlated derivative term |
| Exact finite-posterior example (14)--(21) | Enumerated feasible magnitudes/signs, exact likelihood and Gram calculation, exact Gaussian expectation |
| Quantized noisy-channel extension | Explicit code likelihood ratio and Gaussian-tail bound; still an abstract source |
| Fixed-mass and smooth-indicator obstructions | Elementary sharp mean example, common conditional submeasure, and rescaled cutoff |
| Full polynomial-width neural conclusion | Open; the four bridges in Section 7 are not supplied |

FAST_FINITE_PASSIVE.md was reread completely for this continuation, at
SHA-256 `7f298bc637afffc207375692ee725290e752cdeb818b42f82563646f74416777`.
The complete previously read eight current-study inputs and their hashes
are recorded in POLYNOMIAL_ACCURACY_ONSET.md, whose frozen SHA-256 is
`5cc5fa8b166acde7169b5a839aa71acf69e6e3d8e25840c53bf10509680beb50`.
The new proof above uses only the passive note's scientific interfaces;
the other prior inputs identify the unchanged benchmark and scope.
No newly authorized cross-study source was needed or fetched.

The rigorous proof, conjecture, and canonical-notation instructions,
including the neural-network reference, remained current. Root AGENTS.md
was reread, at SHA-256
`d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97`;
RESEARCH_WORKFLOW.md remains at
`459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1`.
Checks were symbolic, not numerical experiments. The supervisor suggested
this weak route and received intermediate mathematical feedback, which
is disclosed author collaboration. Only WEAK_PASSIVE_WIDTH_ROUTE.md was
written; the frozen earlier note and shared README were left untouched.
