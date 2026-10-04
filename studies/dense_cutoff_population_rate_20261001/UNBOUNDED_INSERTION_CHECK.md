# Internal reconstruction of insertion with linearly growing activations

2026-10-03. **Local extension checks, conditional on the bounded candidate's
local lemma being accepted in its stated form.** This is a collaborator
reconstruction by the author of `DEPTH_CAVITY_ROUTE.md`, not an isolated
promotion review or a fresh independent check of that bounded lemma.
The source read completely is `UNBOUNDED_ACTIVATION_CANDIDATE.md`, SHA-256
`7d29744d71dd14aca1f9eb4710b3608a8105838d5054834b6502c373cee2de1d`.
The bounded source is frozen at SHA-256
`32c2c67bbd13b26e46a590cb2a01d7bd1ac360cd174ddd2494b5d38d29677487`.
Final bounded-source reconciliation: the coordinator repaired formatting, defined the strict initialization event, made activation removal explicit, and reconciled the checked tracking statement and fixed positive weights. The resulting bounded source has SHA-256
`e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`.
Its local estimates used in this check are unchanged. The preceding hash records the exact version used for the reconstruction.

No sibling check of the unbounded candidate was read. The manuscript,
two-layer finite source/checks, canonical notation and required proof skills
were already read within this assignment. No experiment or Git mutation.

The conclusion is that the local insertion estimates do extend to
\(\phi_\ell\in C^3\) with bounded first, second and third derivatives,
without bounded values, on the source's joint supremum-budget stop.
I found one literal omission in the prose for top-layer deletion: the
small residual offset multiplies the reverse force as well as the retained
gradient. The additional term is smaller than the already allowed
remainder, and the exact equation below supplies the correction. No
unclosed local estimate is identified. The final theorem also requires the
separate probability reconstruction and the bounded local reconstruction.

## 1. Physical bounds and what changes in the local proof

Use the canonical network and Euclidean mobility coordinates
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w),
 \qquad \mathcal F_a=nf_a.
\]
Let \(S=2Y/\kappa>0\), with \(\rho\le Ye^{-\kappa t}\), and retain
the manuscript's physical operator and feature RMS bounds. Set
\[
 Z_i^{(j)}(t)=\max_a\sup_{u\le t}|z_{a,i}^{(j)}(u)|,
 \quad K_i^{(j)}(t)=\max_a\sup_{u\le t}|k_{a,i}^{(j)}(u)|,
\]
and suppose the joint proof budget
\[
 \frac1n\sum_{j,i}\exp\{\eta[Z_i^{(j)}+K_i^{(j)}/S]\}\le2B
 \tag{1}
\]
holds on a reference cavity. This gives
\(Z_i\le C\log n\), \(K_i\le CS\log n\) at fixed \(S,B\).
Linear growth, following from bounded first derivative, gives
\[
 |\phi_\ell(z)|\le |\phi_\ell(0)|+\|\phi_\ell'\|_\infty|z|
 \le C(1+|z|).
 \tag{2}
\]
Hence the deleted forward control has logarithmic amplitude; the reverse
control already had logarithmic amplitude in the bounded proof.

All retained forward Jacobians remain uniformly bounded in Euclidean
operator norm. The matrix-variation contribution is

\[
 U_{H^{(\ell)}}h_a^{(\ell-1)}/\sqrt n,
 \quad
 \|U_{H^{(\ell)}}h_a^{(\ell-1)}/\sqrt n\|_2
 \le C\|U_{H^{(\ell)}}\|_F,
\]
because the feature RMS is bounded. No feature coordinate bound is used.
The exact Hessian identity (11) in `DEPTH_CAVITY_ROUTE.md` therefore
holds with the same rank, operator, and normalized Schatten estimates.
Its cross-weight terms use \(\|\delta_a^{(\ell)}\|_2/\sqrt n\le CS\),
again independent of bounded activation values. Its only unbounded
multipliers are carrier diagonals, including the top carrier \(w\),
which is included in (1). In particular
\[
 \|D^2\mathcal F_a\|_{\rm op}\le C(1+CS\log n),
 \quad \|\nabla\mathcal F_a\|_2\le C\sqrt n,
\]
and, for \(p\ge2\),
\[
 \|D^2\mathcal F_a\|_{p,n}
  +\|D_\Theta\delta_a^{(j+1)}\|_{p,n}
 \le C[1+Sp(2B)^{1/p}].
 \tag{3}
\]
The deterministic \(p=2\) bounds remain \(C\), since carrier RMS is
\(CS\). This is the only modification needed in the reference Hessian
part of the local lemma: the budget now also includes the top carrier.

The actual control speeds are still at most
\(C\sqrt n(\log n)^C\). Forward physical speeds have normalized norm
\(CS\rho\). In backward differentiation the changed gate multiplies a
carrier bounded by \(CS\log n\); its coordinate speed is bounded by
its Euclidean speed. The readout speed has RMS \(C\rho\), and the
first three activation derivatives are bounded. These give the same
polynomial logarithmic factors and the same single \(\sqrt n\) factor.

## 2. Interior deletion and the two exact small sources

For \(1<j<L\), delete a fixed set \(I\) of neurons from layer \(j\),
including their incoming rows and outgoing columns. This is rectangular
removal of the activations themselves, not setting omitted preactivations
to zero; the latter would insert \(\phi_j(0)\) and be wrong for many
admissible activations. Keep normalization \(n\). Conditional on the
retained initialization, the omitted initialized incoming rows \(y_i\)
and outgoing columns \(x_i\) are independent \(N(0,I_n/n)\).

Let \(e_a\) enter the retained preactivation at layer \(j+1\), and let
\(q_a\) enter as a reverse force at the retained activation layer \(j-1\).
The exact retained equation is
\[
 \dot\Theta=-\frac2m\sum_a r_a
 \left[\nabla_\Theta\mathcal F_a(\Theta,e)
   +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right],
 \qquad r_a=\mathcal F_a(\Theta,e)/n-y_a.
 \tag{4}
\]
The actual sources are \(e_a=\sum_iW^{(j+1)}_{:,i}a_{a,i}\),
\(q_a=\sum_iW^{(j)\top}_{i,:}b_{a,i}\), with
\(a_{a,i}=h_{a,i}^{(j)}\) and \(b_{a,i}=\delta_{a,i}^{(j)}\).
For terminal running maxima \(Z_i,K_i\), their amplitudes satisfy
\[
 \sup_{a,u\le t}|a_{a,i}(u)|\le C(1+Z_i(t)),\qquad
 \sup_{a,u\le t}|b_{a,i}(u)|\le CK_i(t).
 \tag{5}
\]
Use these actual amplitudes when estimating traces; their global
logarithmic caps are used only for the uniform Gaussian event.

The actual column and row updates give
\[
 \|W^{(j+1)}_{:,i}(t)-x_i\|_2
 \le CS^2[1+Z_i(t)]/\sqrt n,
 \qquad
 \|W^{(j)\top}_{i,:}(t)-y_i\|_2
 \le CSK_i(t)/\sqrt n.
 \tag{6}
\]
Indeed the normalized upper response has size \(CS\), the incoming
feature RMS has size \(C\), and residual activity has mass \(CS\).
After multiplication by the controls, the two source remainders have
Euclidean norm at most
\[
 \frac{C_r}{\sqrt n}
 \sum_{i\in I}\{S^2(1+Z_i)^2+SK_i^2\}
 \le C_rn^{-1/2}(\log n)^C.
 \tag{7}
\]
They can be adaptive, since the estimate is along the actual existing
solution and no Gaussian independence is used for these small terms.

## 3. Local Gaussian event and nonlinear remainders

The linearized coefficients in (4) remain exactly
\[
 P_a=-\frac2{mn}\nabla\mathcal F_a\delta_a^{(j+1)\top},
 \quad Q_a=-\frac2m r_a(D_\Theta\delta_a^{(j+1)})^\top,
 \quad T_a=-\frac2m r_a(D_\Theta h_a^{(j-1)})^\top.
 \tag{8}
\]
The variational equation retains its negative Gram and residual Hessian.
The weak maximum in (1), small fixed \(S\), and total activity give
the same propagator bound \(\|J(t,s)\|\le n^{1/1000}\).
Logarithmic source amplitudes and speeds only insert logarithmic factors
in the linear response operator and its control modulus. Thus the local
exponents \(a=1/100\), \(b=1/10\), net accuracy \(n^{-1/8}\),
and nonlinear cap \(n^{-1/25}\) remain valid:
\[
 \log N\le C_rn^{5/8}(\log n)^C,
 \qquad\text{coordinate and pairing tails}
 \le C_r\exp(-c_rn^{79/100}).
 \tag{9}
\]
After the union bound the event can still have failure at most
\(C_r\exp(-n^{7/10})\). Gaussian source norms, all forward and
backward linear variations, all lower reverse probes, and both centered
quadratic and independent-vector bilinear forms are included. The event
is uniform over the deterministic control class, so later adaptive
selection of the actual controls is legitimate.

Here are the places where activation values occur in the nonlinear
calculation. In the forward recursion a reference activation multiplying
\(\Delta H/\sqrt n\) uses its Euclidean norm \(C\sqrt n\).
A changed activation satisfies
\(\|\Delta h\|_2\le C\|\Delta z\|_2\), from the bounded first
derivative. The cross product
\((\Delta H/\sqrt n)\Delta h\) retains \(1/\sqrt n\).
All scalar Taylor remainders use only bounded second or third activation
derivatives. In the gradient outer product
\(\delta h^\top/\sqrt n\), the two linear terms use the RMS norms
of \(h,\delta\); the quadratic term retains \(1/\sqrt n\).
The reverse-probe Hessian uses only lower forward Jacobians, bounded
derivatives, and probe carriers, hence has the unchanged bound (22) of
the bounded source. None of these steps uses \(\|\phi\|_\infty\).

Explicitly, if \(V\) is the linear response and \(U\) its unknown
remainder, \(\|V\|_2\le n^a\), its linear vector coordinates are at
most \(n^{-b}\), and \(u=\|U\|_2\le n^{-1/25}\), define
\[
 R=n^{a-b}+n^{-b}u+u^2,
 \qquad P=n^{-1/2}(n^{2a}+n^au+u^2).
\]
The full vector-field remainder, including the adaptive residual, is
still bounded by
\[
 C_r(\log n)^C
 \left[\rho^0\{n^{2a-b}+n^{a-b}u+n^{-b}u^2+R\}+P\right].
 \tag{10}
\]
The controls in (5) introduce only further logarithmic factors. The
largest residual-weighted powers are \(n^{-8/100}\) and \(u^2\).
Variation of constants over \(O(\log n)\) time, with amplification
\(n^{1/1000}\), makes them \(o(n^{-1/25})\). Sources (7) are
smaller. Consequently all retained preactivations and carriers differ
from their cavity counterparts by \(O_r(n^{-1/30})\), and the relevant
forward and backward response vectors differ in ordinary Euclidean
norm by at most \(C_rn^{1/100}\). These conclusions include the
preactivation bound needed for the joint stop transfer.

## 4. Both traces retain the actual control amplitude

For the carrier comparison, pair the upper-response expansion with
\(x_i\). The response driven by \(x_i a_i\) gives a quadratic form;
the one driven by \(y_i b_i\) gives a centered bilinear form. Uniform
Gaussian concentration is already in (9). The normalized trace of the
quadratic response is linear in the forward control, so the endpoint
Schatten proof gives
\[
 \frac1n|\operatorname{tr}R_i^{xx}(t)|
 \le CS(1+S^2B)\sup_{a,u\le t}|a_{a,i}(u)|+o(1).
 \tag{11}
\]
No passage from a control net to arbitrary controls changes this
amplitude dependence: the trace estimate is deterministic for each
control, and the Gaussian fluctuation estimate is uniform on the
whole logarithmic control class. The net approximates fluctuations,
not the amplitude in the deterministic estimate.
The learned column in (6), paired with the actual upper response,
costs \(CS^3(1+Z_i)\). Thus
\[
 K_i\le G_{\delta,i}+CS(1+S^2B)(1+Z_i)+o(1).
 \tag{12}
\]

For the forward comparison, pair the lower-feature expansion with
\(y_i\). There is no direct forward-source effect on the lower
activation \(h^{(j-1)}\). Let \(C_a=D_\Theta h_a^{(j-1)}\), with
\(\|C_a\|\le C\). Its reverse quadratic trace is exactly
\[
 -\frac2m\sum_a\int_0^t r_a(s)b_{a,i}(s)
 \frac1n\operatorname{tr}\{C_b(t)J(t,s)C_a(s)^\top\}\,ds.
 \tag{13}
\]
The contraction contribution is bounded by \(C\), since its rank is
at most \(n\). For the remaining term, the same normalized Schatten
Dyson calculation as in the bounded proof, without endpoint carrier
factors, gives
\[
 \sup_{s\le t}\frac{\|J(t,s)-U_0(t,s)\|_{\rm HS}}{\sqrt n}
 \le CS+CS^2\sqrt{2B}.
 \tag{14}
\]
One way to verify it is to use exponent \(2h\) on the \(h\) residual
Hessians. Its \(h\)-th term is bounded by

\[
 \frac1{h!}\left[CS+CS^2(2h)(2B)^{1/(2h)}\right]^h.
\]
The bounded part sums to \(CS\); the carrier part is a geometric
series times \(\sqrt{2B}\), with leading size \(CS^2\sqrt{2B}\).
This proves (14), keeping the identity inside the contraction.
Equations (13)--(14) therefore cost
\(CS(1+S+S^2\sqrt B)\sup|b_i|\). The factor \(1+S\) can be
absorbed in a fixed constant. The cross term from \(x_i\) is centered
and uniformly small. The learned incoming row in (6) paired with the
actual feature costs \(CSK_i\). Hence
\[
 Z_i\le G_{h,i}+CS(1+S^2\sqrt B)K_i+o(1).
 \tag{15}
\]
This is the second candidate inequality with its small-label factor
intact. It would be lost by using only a generic operator bound on \(J\).

Writing \(\kappa_i=K_i/S\), (12)--(15) have coefficients
\(C(1+S^2B)\) from \(Z_i\) to \(\kappa_i\) and
\(CS^2(1+S^2\sqrt B)\) in the opposite direction. At fixed \(B\),
choose \(S\) so their product is below \(1/2\) and \(S^2B\le1\).
Solving these two scalar inequalities gives
\[
 Z_i+K_i/S\le C[1+G_{h,i}+G_{\delta,i}/S]+o(1),
 \tag{16}
\]
with a fixed constant independent of \(B\) after these choices.

## 5. First and top layers

At the first layer there is no reverse source in the retained equations.
Direct integration gives
\[
 Z_i^{(1)}\le\max_a|(W_0^{(1)}v_a)_i|+CSK_i^{(1)}.
\]
Its outgoing-column trace is still (12), with forward amplitude
\(C(1+Z_i)\). The independent incoming Gaussian row has fixed dimension
\(d\) and all linear-exponential moments. The same scalar absorption
therefore applies, with this row replacing \(G_h\).

At the top layer delete the incoming row and its readout coordinate.
Let \(\mathcal F_a^{\rm ret}=w_{-I}^\top h_{a,-I}^{(L)}\),
\[
 r_a^0=\mathcal F_a^{\rm ret}/n-y_a,\quad
 d_a=\frac1n\sum_{i\in I}w_i h_{a,i}^{(L)},\quad
 q_a=\sum_{i\in I}W^{(L)\top}_{i,:}\delta_{a,i}^{(L)}.
\]
The exact retained equation is
\[
 \dot\Theta=-\frac2m\sum_a(r_a^0+d_a)
 \left[\nabla\mathcal F_a^{\rm ret}
            +D_\Theta h_a^{(L-1)\top}q_a\right].
 \tag{17}
\]
The candidate's prose only named the offset contribution
\(-2m^{-1}\sum_a d_a\nabla\mathcal F_a^{\rm ret}\). Equation
(17) also contains \(-2m^{-1}\sum_a d_aD_\Theta h_a^{(L-1)\top}q_a\).
On the joint cap,
\(\max|d_a|\le C_r(\log n)^2/n\),
\(\|q_a\|_2\le C_r(\log n)^C\),
\(\|\nabla\mathcal F_a^{\rm ret}\|\le C\sqrt n\), and the
forward derivative has bounded operator norm. Thus the entire offset
force has Euclidean norm at most
\[
 C_rn^{-1/2}(\log n)^C.
 \tag{18}
\]
It is an allowed adaptive small source, independent of no Gaussian
variable. A derivative or Lipschitz bound on this source is unnecessary
for the pathwise remainder estimate. The unperturbed reference is the
autonomous cavity with its own \(r^0\).

The only Gaussian source is the incoming row \(y_i\), so the forward
trace proof (13)--(15) is unchanged and no bilinear \(x_i,y_i\) term
is needed. The exact readout equation and total activity give
\[
 K_i^{(L)}=\sup|w_i|\le CS(1+Z_i^{(L)}).
\]
Substitution into (15) gives
\[
 Z_i^{(L)}\le G_{h,i}+CS^2(1+S^2\sqrt B)(1+Z_i^{(L)})+o(1).
\]
After decreasing \(S\), the last \(Z_i\) term is absorbed. This
controls both the top preactivation and the readout. Deleting multiple
top neurons only increases fixed-\(r\) source constants, not the small
label threshold.

## 6. Joint stops, common cavities, and the moment constants

The local estimate in Section 3 controls every retained preactivation
and carrier by \(\epsilon_{n,r}=C_rn^{-1/30}\). Consequently their
running maxima satisfy the same difference bound, and the joint
exponentials differ by at most
\[
 \exp\{\eta\epsilon_{n,r}(1+1/S)\}=1+o(1)
\]
for fixed \(S>0\). A cavity stop at \(2B\) cannot precede the full
stop at \(B\); omitted zero-filled coordinates cost only \(r/n\).
This is the same strict-margin common-prefix argument as in the bounded
case, now with both components in the exponent.

For an omitted row \(y_i\), both singleton and common-deletion lower
feature paths exclude \(y_i\); their difference is independent of it.
For an omitted column \(x_i\), both upper-response paths exclude
\(x_i\). Their difference is independent of that column. Euclidean
projection onto a deterministic ball of radius \(C_rn^{1/100}\)
preserves this independence and agrees on the successful prefix.
The Gaussian pairing radius is \(C_rn^{-1/2+1/100}\), not the
Euclidean radius. Forward feature paths have a bounded-activity
Lipschitz metric; backward paths have the cutoff modulus from the
bounded source, which still uses only feature RMS, carrier budget, and
bounded first two derivatives. Thus the projected Gaussian suprema
are \(o(1)\) with superpolynomial tails, also for the new forward
comparison. They are defined before restricting to the full stop.

The forward Gaussian reference \(G_h\) has normalized coefficient norm
\(C\) and total normalized variation \(CS^2\), including its initial
Gaussian value. Its fixed exponential moments are uniformly bounded.
For the backward reference, the two-time bound in the bounded source
continues to hold because the top changed-gate term is now covered by
the top carrier's term in the joint budget. In particular, after
\(S^2\log(e+B)\le1\), it has a deterministic square-root activity
metric bound independent of \(B\). The fixed exponential moments of
\(G_\delta/S\) are then bounded independently of \(B\) as well; using
the weaker \(B^{o(1)}\) form in the candidate is sufficient.

Within one common-deletion cavity the incoming/outgoing Gaussian pairs
are independent across omitted neurons. For an interior neuron \(G_h\)
depends on \(y_i\) and \(G_\delta\) on \(x_i\), which are also
independent conditional on the cavity. The first and top layers use
only their stated Gaussian roots. Therefore (16) has an exponential
moment base independent of the number of distinct omitted neurons.
All collision multiplicities use higher fixed moments of these same
Gaussian suprema. This checks the crucial independence from the later
empirical moment degree. Fixed-degree remainders and width thresholds
may depend on that degree.

## 7. Initialization and final claim boundary

The initialized joint budget contains only forward preactivations, since
all carriers vanish at zero readout. Given the previous empirical feature
covariance, each new preactivation row is conditionally Gaussian in the
fixed sample dimension. On a fixed bounded covariance set,
\(\exp(\eta\max_a|z_a|)\) has a bounded second moment and a continuous
mean as a function of covariance. Conditional Chebyshev and the known
initialized covariance convergence imply convergence in probability of
each empirical budget. A fixed finite layer sum therefore has a finite
limit. Gaussian conditional tails also give an initial \(C\sqrt{\log n}\)
maximum on these events. This makes \(H(0)<B/2\) available for large
fixed \(B\). It does not assert an unconditional exponential moment
after mixing arbitrarily large random covariances.

For all fixed-size cavities, a common full initialization event suffices.
At the deletion layer the omitted activation vector has norm
\(C_r\sqrt{\log n}\). Operator propagation bounds every subsequent
feature difference by \(C_r\log n\), allowing a harmless weaker bound.
At each following layer its current Gaussian matrix is independent of
that preceding feature difference. Project the difference onto this
deterministic Euclidean ball before a conditional tail bound. Each
coordinate difference has variance at most \(C_r(\log n)^2/n\).
A union over fixed \(r\), \(n^r\) same-layer sets, fixed samples and
layers, and all coordinates makes all retained preactivation differences
at most \(n^{-b_0}\), for any fixed \(b_0<1/2\), with
superpolynomially small additional failure. Thus the cavity initialized
budget is \(\exp(o(1))H(0)+O(r/n)\). Normalized feature differences
also preserve a smaller fixed initialized Gram gap. These choices do
not impose an \(r\)-dependent label threshold.

The five additional obligations in the unbounded candidate are therefore
met by the explicit calculations above: logarithmic controls and the top
offset, actual-amplitude traces, joint stop transfer, two-direction
common-cavity independence, and moment-degree-independent constants with
valid initialization. The top equation should be stated as (17), or its
extra reverse-offset term explicitly included among small remainders.

This report does not itself replace the independent reconstruction of
the bounded local insertion proof, nor does it certify a complete new
all-time theorem without the separate probability and deterministic
tracking checks. Once those are accepted, no further local
bounded-value assumption is required for the extension to activations
with bounded first three derivatives and linearly growing values.
