# Joint forward/backward budgets for activations with linear growth

2026-10-03. **Completed extension, internally reconstructed.**
The historical filename records its initial candidate status. The local
insertion estimates are now supplied by UNBOUNDED_INSERTION_CHECK.md,
reconstructed by the coordinator in DEPTH_INSERTION_CHECK.md. The
complete probability argument is reconstructed in
UNBOUNDED_ACTIVATION_CHECK.md. Together with the checked bounded
insertion lemma, these close every obligation listed in Section 3.
This is internal collaborative research, not promotion into the book.
Inputs
are the canonical manuscript dynamics and the present study's finite
cavity and response-modulus derivations. No external study or experiment.

Assume fixed depth and activations \(\phi_\ell\in C^3(\mathbb R)\)
with globally bounded first, second, and third derivatives; values may
grow linearly. Keep the
physical fitting tube, canonical initialization and zero readout.
The fixed positive sample weights \(p_a\) sum to one; the original case
is \(p_a=1/m\). Set
\[
 Y^2=\sum_a p_a y_a^2,\qquad
 \rho^2=\sum_a p_a(f(x_a)-y_a)^2,\qquad S=2Y/\kappa>0,
\]
where \(\rho(t)\le Ye^{-\kappa t}\). Zero labels give stationary
coincident trajectories and need no budget argument. The ordinary
backward quantities are
\[
 k^{(L)}=w,\qquad
 k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\qquad
 \delta_a^{(\ell)}
       =\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]
For neuron i in layer j, put
\[
 Z_i^{(j)}(t)=\max_a\sup_{u\le t}|z_{a,i}^{(j)}(u)|,\qquad
 K_i^{(j)}(t)=\max_a\sup_{u\le t}|k_{a,i}^{(j)}(u)|.
\]
Use the full joint supremum budget
\[
 H(t)=\frac1n\sum_{j,i}
 \exp\{\eta[Z_i^{(j)}(t)+K_i^{(j)}(t)/S]\}\le B.
 \tag{1}
\]
It implies logarithmic caps on both forward preactivations and scaled
backward carriers. Fixed-budget cavities use 2B. The initial forward
exponential budget converges to a finite constant by conditional Gaussian
laws and the layerwise law of large numbers. Include H(0)<B/2 in the
initialization event after choosing B large. Initialized forward maxima
are O(sqrt(log n)) with probability tending to one, by conditional
Gaussian tails and the physical RMS bound at each fixed layer. This
ensures every fixed-size deletion retains a positive initial feature-Gram
margin even though individual activation values are unbounded.

The initialization statement is convergence in probability, not an
unstopped exponential-moment assertion for a finite deep Gaussian
network. To verify it, condition successively on each preceding empirical
feature covariance. On any fixed bounded set of such covariances, the
conditional Gaussian exponential moments through order two are uniformly
bounded, so conditional Chebyshev gives an O(1/n) empirical fluctuation.
Their conditional means are continuous functions of covariance.
The usual initialized covariance induction, first restricted to these
bounded sets, proves convergence in probability layer by layer. The
conditional Gaussian union bound proves the initialized coordinate
maximum in the same way. No Gaussian marginal tail is asserted after
averaging over rare, arbitrarily large preceding covariances.

Uniform initialization of all fixed-size cavities follows by a separate
comparison, rather than a union bound on these O(1/n) laws of large
numbers. On the common initialized operator-norm event and initialized
coordinate bound C log(n), deleting p neurons in one layer changes the
subsequent feature vectors by at most C_p log(n) in Euclidean norm.
At each subsequent layer, a fresh initialized Gaussian row is independent
of the preceding feature difference. Its pairing with that difference
has variance at most C_p log(n)^2/n. Projecting that preceding difference
onto the stated deterministic norm ball if necessary makes the conditional
tail bound valid without conditioning on the fresh row's operator event.
Gaussian tails and a union over n^p deletion sets, the fixed layers and
samples, and all coordinates give retained preactivation differences
at most n^(-b), for any fixed b<1/2, with superpolynomially small
additional failure probability. Consequently every such cavity's initial
joint budget is at most exp(o(1)) times the full initial budget, up to
the omitted coordinates. The initial feature Gram also changes by o(1).
A strict full-initialization margin therefore supplies all required
fixed-p cavity initialization events without a p-dependent label bound.

## 1. Internal-neuron reciprocal inequalities

For 1<j<L, delete neuron i, its incoming initialized row y_i in W0^(j)
and outgoing initialized column x_i in W0^(j+1). They are independent
N(0,I/n) vectors conditional on the retained initialization.
The retained vector field has an external forward field x_i a_i(t)
at layer j+1 and reverse force
\[
 -2\sum_a p_a r_a
       D_\Theta h_a^{(j-1)}{}^\top y_i b_{a,i}(t).
 \tag{2}
\]
The actual controls are a_{a,i}=h_{a,i}^{(j)} and
b_{a,i}=delta_{a,i}^{(j)}. Before the joint budget stop their
amplitudes are O(log n), and their Lipschitz constants are
O(sqrt(n) polylog(n)) by the raw coordinate speed bounds.
The local insertion proof therefore needs polynomially small coordinate
thresholds and a matching uniform control net, exactly as for bounded
activations, with additional logarithmic factors only.

All retained forward derivative maps have bounded operator norm on the
physical tube, because every hidden matrix variation acts as
U_H h/sqrt(n) and the feature RMS is bounded. The nonlinear block
expansions use bounded activation derivatives, not bounded values;
activation values enter these bounds only through their RMS or the
scalar external controls.

The complete local Gaussian insertion event is justified in
UNBOUNDED_INSERTION_CHECK.md, including joint bilinear forms and the
omitted learned rows/columns.
Pair its response expansion with x_i to recover the actual carrier.
The endpoint trace calculation gives, retaining the actual control
amplitude instead of its global cap,
\[
 K_i^{(j)}
 \le G_{\delta,i}
       +CS(1+S^2B)(1+Z_i^{(j)})+o(1).
 \tag{3}
\]
Here G_delta,i is the supremum of the cavity Gaussian process
x_i^T delta_a^{(j+1),-i}, and the o(1) is uniform through the full
stop for fixed S,B. The learned outgoing column contributes at most
CS^3(1+Z_i), already included. The reverse-source term is a centered
bilinear form x_i^T R y_i on the uniform Gaussian control event.

Now pair the *forward* response expansion of h^(j-1) with y_i.
The x_i term is centered bilinear. Its reverse-source quadratic trace
has the form
\[
 -2\sum_a p_a\int_0^t r_a(s)b_{a,i}(s)
 \frac1n\operatorname{tr}
 \left[C_b(t)J(t,s)C_a(s)^\top\right]ds,
 \qquad C_a=D_\Theta h_a^{(j-1)}.
\]
The C_a have bounded operator norm. The negative-Gram contraction plus
the checked normalized Hilbert--Schmidt estimate for J-U0 bounds the
absolute normalized trace by C(1+S+S^2 sqrt(B)).
Since |b_{a,i}|<=C K_i, integration costs CS K_i. The learned
incoming row also costs CS K_i after pairing with the physical feature
vector: its Euclidean increment is CS K_i/sqrt(n). Therefore
\[
 Z_i^{(j)}
 \le G_{h,i}+CS(1+S^2\sqrt B)K_i^{(j)}+o(1).
 \tag{4}
\]
Here G_h,i=max_a sup|y_i^T h_a^{(j-1),-i}| is a Gaussian reference
supremum with width-independent exponential moments. The reference
feature path has bounded RMS and bounded variation in residual activity
by the physical forward-speed estimate.

Write kappa_i=K_i/S. Equations (3)--(4) are a coupled pair
\[
 \kappa_i\le G_{\delta,i}/S+C(1+S^2B)(1+Z_i)+o(1),
 \qquad
 Z_i\le G_{h,i}+CS^2(1+S^2\sqrt B)\kappa_i+o(1).
 \tag{5}
\]
Choose B first, then S so small that the product of their two feedback
coefficients is below 1/2 and S^2B<=1. Absorption yields
\[
 Z_i+\kappa_i\le
 C[1+G_{h,i}+G_{\delta,i}/S]+o(1),
 \tag{6}
\]
with a constant independent of B after these smallness choices.

## 2. First and last layers

At j=1, the incoming initialization is an independent Gaussian row in
R^d. Direct integration of the read-in equation gives
\[
 Z_i^{(1)}\le \max_a|(W_0^{(1)}v_a)_i|+CS K_i^{(1)}.
\]
The outgoing-column insertion is the original first-layer construction,
now with scalar controls of size O(log n). Its trace retains their
actual amplitude C(1+Zi), giving (3). Thus the same absorption applies.

At j=L, delete the top neuron, its incoming Gaussian row y_i, and its
readout coordinate w_i. There is no initialized outgoing Gaussian
column because w_i(0)=0. The omitted prediction is
w_i h_{a,i}^{(L)}/n, bounded by polylog(n)/n before (1).
Let \(\mathcal F_a^{\rm ret}\) be the retained unnormalized prediction,
\(r_a^0=\mathcal F_a^{\rm ret}/n-y_a\), and
\(d_a=w_i h_{a,i}^{(L)}/n\). With
\(q_a=W^{(L)\top}_{i,:}\delta_{a,i}^{(L)}\), the exact retained field is
\[
 -2\sum_a p_a(r_a^0+d_a)
 \left[\nabla_\Theta\mathcal F_a^{\rm ret}
       +D_\Theta h_a^{(L-1)\top}q_a\right].
 \tag{7}
\]
Here \(p_a=1/m\), or the fixed positive weights summing to one.
The offset therefore multiplies both the retained gradient and reverse
force. Its entire contribution has Euclidean norm at most
\(n^{-1/2}\operatorname{polylog}n\): the gradient has norm
\(C\sqrt n\), the forward derivative has bounded operator norm,
\(\|q_a\|_2\) is polylogarithmic, and \(|d_a|\) is
\(n^{-1}\operatorname{polylog}n\). The reverse force itself remains
essential, with \(b_{a,i}=w_i\phi_L'(z_{a,i}^{(L)})\).

The readout equation gives exactly
\[
 \sup_{u\le t}|w_i(u)|\le CS[1+Z_i^{(L)}(t)].
\]
The forward response calculation (4), now driven by the reverse source
alone and the small scalar offset, gives
\[
 Z_i^{(L)}
 \le G_{h,i}+CS^2(1+S^2\sqrt B)[1+Z_i^{(L)}]+o(1).
\]
After absorption, both Zi and |wi|/S have Gaussian-reference
exponential moments.

## 3. Checks completing the theorem

The empirical moment argument expands each layer's H_j^p
using a common cavity with p simultaneous deletions in that layer.
Its initial rows and outgoing columns are conditionally independent.
The backward Gaussian supremum has exponential moment L_eta(B)=B^{o(1)}
by DEPTH_RESPONSE_MODULUS; the forward Gaussian supremum has a bound
independent of B. Equation (6) therefore gives a moment base B^{o(1)}.
The finite number of layers can be handled separately: H=B implies
some H_j>=B/L. Choose B large enough for a strict margin, then S small.
Collision tuples use the corresponding higher fixed exponential moments.

The completed local and probability reconstructions verify all of:

1. The local insertion lemma indeed remains uniform for logarithmic
   forward-control amplitudes and the top scalar residual offset.
2. The trace bounds in (3) and (4) retain actual control amplitudes
   uniformly over the control net, and their remainders vanish.
3. The joint stopping-budget comparison includes preactivation
   discrepancies as well as backward carriers.
4. Common-cavity projected differences preserve independence for both
   incoming-row forward references and outgoing-column backward
   references.
5. The layerwise empirical moment constants are independent of moment
   degree before its final limit, and the initial budget event is proved.

The resulting Gaussian maximum is
max Zi<=C sqrt(log n), max Ki<=CS sqrt(log n).
After T=c log n, the physical RMS bound and raw backward derivative
give coordinate carrier drift O(n S exp(-kappa T)); taking c kappa>1
extends the estimate to all time. Forward coordinate drift is smaller.
The deterministic DEPTH_TRACKING_ROUTE then gives near-quarter
memory order and strict root-width prediction accuracy.

The combined theorem is stated in DEPTH_EXTENSION_RESULT.md. It includes
softplus, GELU and SiLU without altering either training algorithm.

## 4. Details of the common-cavity moment completion

The additional controls have only polylogarithmic amplitudes. Their
physical-time Lipschitz constants are still O(sqrt(n) polylog(n)):
the forward RMS speed is bounded by C S rho; downward differentiation
of the backward recursion uses the logarithmic carrier cap and the
bounded first three activation derivatives. Thus the same control-net
entropy exponents as in the bounded candidate have a strict margin.

The retained forward Jacobians have bounded operator norm using feature
RMS, without a coordinate bound on the retained activations. In their
Taylor expansions, a changed hidden matrix always carries 1/sqrt(n).
Terms containing a retained activation use its Euclidean norm C sqrt(n),
which cancels that denominator; products of two perturbations retain
the extra 1/sqrt(n). The scalar external controls are the only place
bounded values were used in the deleted-neuron source, and their new
logarithmic cap changes none of the polynomial exponents.

For the top-layer residual offset, use the exact equation (7).
The physical gradient norm is \(C\sqrt n\), while
\(|d_a|\) is \(\operatorname{polylog}(n)/n\). The additional reverse
offset \(d_aD_\Theta h_a^{(L-1)\top}q_a\) has the still smaller norm
\(\operatorname{polylog}(n)/n\). After time integration and the weak
variational amplification, both contributions are polynomially small.
No randomness or independence is needed for these remainders.

On the local insertion event, every retained preactivation and backward
carrier differs from its cavity counterpart by o(1), uniformly up to
the earlier of their two stops. Running coordinate maxima differ by
the same amount. Their joint exponentials therefore differ by a
multiplicative exp(o(1)) at fixed S. As in the bounded case, a cavity
cap 2B cannot be reached while the full cap remains below B.

For a fixed p-tuple of distinct neurons in one layer, compare each
singleton cavity with the common p-deletion cavity. For its omitted
incoming row y_i, both lower forward feature paths are independent of
y_i; for its omitted outgoing column x_i, both upper backward paths
are independent of x_i. Project each full difference path onto a
deterministic Euclidean ball whose radius divided by sqrt(n) is
polynomially small, as supplied by the local insertion event. The Euclidean
radius itself may grow as a small power of n; its Gaussian pairing radius
tends to zero. The projected differences remain independent
of the omitted Gaussian vector. The forward path has a bounded-activity
Lipschitz metric; the backward path has the checked square-root activity
metric. For the Gaussian supremum E_n of a projected difference,
E exp(lambda E_n) tends to 1 for every fixed lambda>=0. Defining the projections over the
entire independently stopped reference paths avoids conditioning on the
full network's root-dependent stopping time.

The common reference Gaussian suprema, conditional on the common cavity,
are independent across the deleted neurons. Equations (5)--(6) use
the singleton trace bound, whose coefficient does not depend on p.
After imposing S^2 B<=1 their exponential-moment base has the form
L_{C eta}(2B)=B^{o(1)}, times a fixed factor. Higher fixed exponential
moments control collision tuples and projected-difference errors. For
each fixed p, these errors vanish as n tends to infinity. Only after
that limit is p allowed to grow. Therefore neither the chosen budget
nor the small-label threshold acquires a dependence on p.

References with failed initialization are set to the zero coefficient
path for these conditional Gaussian estimates. On the common good
initialization event they agree with the actual stopped cavities. This
permits removing the full good-event indicator in moment upper bounds
without assuming a conditional Gaussian estimate on a failed tube.

The complete local block estimates have now been checked to use only
RMS feature bounds and polylogarithmic external control bounds.
UNBOUNDED_INSERTION_CHECK.md gives the exact field, Gaussian event,
nonlinear remainder, amplitude-sensitive trace, and top-layer
calculations. DEPTH_INSERTION_CHECK.md records the coordinator's
reconstruction of these steps. The complete probability
report UNBOUNDED_ACTIVATION_CHECK.md supplies the scalar absorption,
initialization, joint stop transfer, fixed-block moments, and all-time
tail. Their combination proves the claimed extension; no local
sensitivity or empirical-moment condition remains an assumption.
