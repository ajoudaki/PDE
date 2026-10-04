# Adjacent-width and Stein follow-up to the direct cavity route

2026-10-03. Bounded follow-up authorized by the coordinator after freezing
`POPULATION_DIRECT_COUPLING.md` at SHA-256
`145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00`.
This is collaborative research, not an independent review. No experiments
or other study sources are used.

**Status.** The adjacent-width normalization bridge below is exact. The
leading deletion/normalization cancellation needed to turn it into a
summable bias bound has not been proved. The direct cavity remainder is
large enough to contribute to the leading prediction increment, so that
remainder cannot be discarded. Section 4 strengthens the direct route's
pathwise insertion to a conditional no-exit statement using its existing
amplitude-sensitive trace bounds. This repairs one localization obstacle
for a Gaussian Stein test, without supplying the population bias closure.

## 1. Exact normalization bridge

Use the fixed-depth model and small-label assumptions of the direct route.
Delete one neuron from every hidden layer of a width-\(n\) network,
leaving all original normalizations unchanged. Put \(k=n-1\) and
\(c=k/n\). The resulting width-\(k\) rectangular cavity still uses
prediction normalization \(1/n\), hidden-update normalization
\(1/n\), and initialized hidden variance \(1/n\).

To express this and the canonical width-\(k\) model in one family,
introduce two positive scalar parameters \(\alpha,\tau\). Let the
hidden initialization be
\(W_0^{(\ell)}=\sqrt{\tau/k}\,G^{(\ell)}\) for \(\ell\ge2\),
where the \(G^{(\ell)}\) have independent standard Gaussian entries.
First weights remain standard Gaussian and the stored readout remains
zero. The forward equations are unchanged except for prediction:
\[
 f_{k;\alpha,\tau}(t,x)=\frac{\alpha}{k}w(t)^\top h^{(L)}(t,x),
 \qquad r_a=f_{k;\alpha,\tau}(t,x_a)-y_a.
 \tag{1}
\]
Backward signals retain their original definitions, excluding the
prediction prefactor. Define training by
\[
 \begin{aligned}
 \dot W^{(1)}&=-2\sum_a p_a r_a\delta_a^{(1)}v_a^\top,\\
 \dot W^{(\ell)}&=-\frac{2\alpha}{k}\sum_a p_a r_a
                         \delta_a^{(\ell)}h_a^{(\ell-1)\top},\\
 \dot w&=-2\sum_a p_a r_a h_a^{(L)}.
 \end{aligned} \tag{2}
\]
These are squared-loss gradient flow with mobilities
\((k/\alpha,1,\ldots,1,k/\alpha)\). Substitution verifies both
endpoints:
\[
 (\alpha,\tau)=(c,c):\quad k/\alpha=n,\quad
         \alpha/k=1/n,\quad\tau/k=1/n;
 \qquad
 (\alpha,\tau)=(1,1):\quad\text{canonical width }k.
 \tag{3}
\]
Thus the diagonal segment from \((c,c)\) to \((1,1)\) exactly
renormalizes the retained cavity. This is a comparison family, not a
proposed change to either trained algorithm.

For any differentiable fixed-time observable \(F_k(\alpha,\tau;G)\),
the pathwise identity is
\[
 F_k(1,1;G)-F_k(c,c;G)
   =\int_c^1(\partial_\alpha+\partial_\tau)
                      F_k(s,s;G)\,ds.
 \tag{4}
\]
Here \(\partial_\alpha\) includes prediction normalization, the
hidden-update coefficient, and the resulting changes in the adaptive
residual and every trained parameter. Keeping only the explicit
prediction prefactor is not this derivative.

Where expectation and differentiation are justified, the Gaussian
variance derivative has the exact form
\[
 \partial_\tau\mathbb E F_k(\alpha,\tau)
 =\frac1{2k}\sum_{\ell=2}^L\sum_{i,j=1}^k
       \mathbb E\partial_{W_{0,ij}^{(\ell)}}^2
                         F_k(\alpha,W_0).
 \tag{5}
\]
Indeed each initialized entry has variance \(\tau/k\), and the
Gaussian heat identity contributes half the derivative of that variance.
The derivatives on the right include all subsequent adaptive training.
For smooth compactly supported functions of the initialized entries,
(5) follows by twice integrating the Gaussian density by parts. Passing
it to the original all-time trained observable requires integrability
or a quantitative localization argument; that passage is not supplied
by (4).

## 2. The exact cancellation still needed

For clarity suppose temporarily that the relevant expectations exist and
that (4) can be averaged. Let \(b_n\) be the width-\(n\) prediction
mean at one time/query, and let
\[
 D_n=\mathbb E[F_n-F_k(c,c)]
 \tag{6}
\]
be the mean effect of removing one neuron from every hidden layer, with
the natural retained-initialization coupling. Then
\[
 b_n-b_{n-1}
 =D_n-\int_c^1(\partial_\alpha+\partial_\tau)
                         \mathbb E F_k(s,s)\,ds.
 \tag{7}
\]
A bound
\[
 |b_n-b_{n-1}|\le n^{-3/2}e^{C\sqrt{\log(e+n)}}
 \tag{8}
\]
would be summable and would give a near-root tail to an identified
population limit. The summation itself is harmless: comparison with a
dyadic decomposition bounds the tail by
\(C n^{-1/2}e^{C'\sqrt{\log(e+n)}}\).

The new finite surgery lemma only bounds the two terms in (7)
individually at the scale \(n^{-1}e^{C\sqrt{\log n}}\), when the
normalization derivative has the corresponding stability bound. Their
cancellation at the smaller scale (8) is the needed theorem. It is not
an implication of exchangeability or concentration around a finite-width
center.

In particular the nonlinear state remainder cannot be dropped from
\(D_n\). The direct calculation writes the retained change as
\(V+U\), where
\[
 \|V\|_2\le e^{C\sqrt{\log n}},\qquad
 \|U\|_2\le n^{-1/2}e^{C\sqrt{\log n}}.
 \tag{9}
\]
The prediction gradient in mobility coordinates has norm
\(C/\sqrt n\). Therefore the uncontrolled contribution of \(U\)
to the prediction is
\[
 |D_\Theta f[U]|\le n^{-1}e^{C\sqrt{\log n}},
 \tag{10}
\]
which is the leading deletion scale. The near-root state error is too
large by a factor \(\sqrt n\) for (8). One must identify its
quadratic contribution and its match to (5), or exploit an alternative
weak cancellation.

A generic higher Taylor expansion does not automatically resolve this
under the stated regularity. The gradient-flow vector field contains
\(\phi'\); two parameter derivatives use \(\phi'''\), which
exists and is bounded. A uniform third-order remainder for that vector
field would generally ask for an additional derivative or a quantitative
modulus not assumed here. This is a limitation of that generic expansion,
not a counterexample to (8): Gaussian integration by parts and represented
responses may still avoid the extra derivative, as the exact first-step
calculation in the direct note demonstrates.

## 3. What the local Gaussian approximation gives a Stein test

Fix a finite list of tagged-neuron times and samples, and a retained
cavity. The direct note constructs a Gaussian source vector \(G\)
with its cavity covariance matrix \(Q\), and approximate innovations
\(I\) obtained by subtracting the explicit response terms from the
tagged fields. Its pathwise estimate is \(|I-G|\le\varepsilon_n\)
on the successful insertion event. Here the dimension is fixed in this
paragraph; path-space and growing-grid versions need their own norms.

If that estimate held for globally defined variables with a quantitative
integrable error, the ordinary Gaussian identity would yield a useful
Stein estimate. Specifically, for a bounded \(C^2\) scalar test
\(\psi\), a deterministic \(Q\), and
\(\mathbb E[(1+|G|)|I-G|]\le\epsilon\), comparison with
\(\mathbb E[G_i\psi(G)]=\sum_jQ_{ij}\mathbb E\partial_j\psi(G)\)
gives
\[
 \left|\mathbb E[I_i\psi(I)]
       -\sum_jQ_{ij}\mathbb E\partial_j\psi(I)\right|
 \le C_{\psi,Q}\epsilon.
 \tag{11}
\]
For the first term use
\(I_i\psi(I)-G_i\psi(G)
 =(I_i-G_i)\psi(I)+G_i[\psi(I)-\psi(G)]\).
For the derivative term use the Hessian bound on \(\psi\).
This proof neither differentiates the innovation error nor inverts its
covariance.

The initially frozen insertion theorem was not yet the integrable conditional
estimate needed in (11). Its full good event has probability tending to
one, without a numerical rate. The event depends on the omitted Gaussian
roots. Inserting its indicator into the Gaussian identity is therefore
invalid. A Lipschitz extension of the scalar observable can prove
concentration but need not preserve the innovation identity.

A cavity-measurable good-set indicator is safe. To use that localization
one needs a conditional insertion/control no-exit
statement: for every retained cavity in its specified good set, the
untruncated tagged dynamics and the Gaussian scalar comparison should
agree within \(\varepsilon_n\), except with conditional probability
of order \(\varepsilon_n\) or smaller, with controlled test values on
the exception. The uniform Gaussian-kernel event is one ingredient, but
the initially frozen pathwise proof uses the established full-network
control bounds instead of proving this conditional no-exit statement.
The following argument supplies this local strengthening.

Even after this step, (11) alone would not identify the population. Its
covariance and the response traces remain cavity-random. Quantitative
self-consistency and stable transport of represented responses are still
required. No approximate population fixed-point theorem is claimed here.

## 4. Conditional insertion without a full-dependent indicator

Fix a singleton cavity and condition on all its retained initialization.
Its good set in this section is entirely cavity measurable. Require the
physical tube with strict initial Gram margin, exponential fitting,
bounded residual activity, and the already established joint exponential
budget at most \(2B\), where \(B\) is the fixed budget used in the
finite carrier proof. Also require, through
\(T_n=C_T\log(e+n)\),
\[
 \max_{a,\ell,i}\{|z_{a,i}^{(\ell),0}|,
                         |k_{a,i}^{(\ell),0}|/S\}\le M_n/2,
 \qquad M_n=C_D\sqrt{\log(e+n)}.
 \tag{12}
\]
Here \(S\) is the study's fixed multiple of the small label RMS.
The constant \(C_D\) is chosen large; it does not shrink \(S\)
with width. The old full/cavity theorem supplies such cavities with
probability tending to one. No rate for that probability is used below.

Restore the omitted Gaussian row and column, and stop the full path if
any of the corresponding normalized coordinate quantities reaches
\(M_n\), or if the enlarged physical tube is left. Before this stop,
the scalar controls are bounded by \(C(1+M_n)\), so the new Gaussian
kernel event and nonlinear insertion proof apply with deterministic
constants. Their conditional failure can be made at most \(n^{-D}\).
The retained full coordinates differ from cavity coordinates by
\(\varepsilon_n\). Thus they cannot reach \(M_n\) while (12)
holds, for sufficiently large width.

For the omitted neuron let \(Z_i\) be its running preactivation
maximum and \(K_i\) its running backward-carrier maximum. The old
trace bounds retain the actual control amplitudes. They depend on the
cavity's moment budget, rather than on a moment assumption for the
inserted path. Specifically, `DEPTH_CAVITY_ROUTE.md`, Section 6,
and `UNBOUNDED_ACTIVATION_CANDIDATE.md`, equations (3)--(5), give
\[
 \begin{aligned}
 K_i/S&\le G_{{\rm back},i}
                +C(1+S^2B)(1+Z_i)+O(\varepsilon_n),\\
 Z_i&\le G_{{\rm forward},i}
                +CS^2(1+S^2\sqrt B)(K_i/S)
                +O(\varepsilon_n).
 \end{aligned} \tag{13}
\]
The \(G\)'s are the conditional Gaussian reference suprema, with
the backward supremum divided by \(S\). The forward reference uses
the cavity feature path's bounded variation in activity. The backward
reference uses the cavity budget's square-root activity modulus. The
elementary chaining calculation in the old source, Section 7, gives
\[
 \mathbb P\{G_{{\rm forward},i}+G_{{\rm back},i}>C+u
                  \mid\text{cavity}\}\le C e^{-cu^2}.
 \tag{14}
\]
These constants are deterministic and uniform over the specified cavity
good set. They follow directly from that set's budget and tube, so the
unconditional moment-probability bootstrap is not being reused after
conditioning.

The original small-label choice makes the product of the two feedback
coefficients in (13) less than \(1/2\), and makes \(S^2B\le1\).
Substitution and absorption therefore give
\[
 Z_i+K_i/S\le
          C[1+G_{{\rm forward},i}+G_{{\rm back},i}]
                  +O(\varepsilon_n).
 \tag{15}
\]
For a first-layer neuron, its incoming Gaussian input root replaces the
forward reference. At the last layer,
\(|w_i|/S\le C(1+Z_i)\), and the same forward absorption applies;
the omitted prediction offset has the inverse-root-width forcing already
included in the direct proof. Thus all layers obey the needed bound.

Choose \(C_D\) so that (14) makes the right side of (15) smaller
than \(M_n\) except with probability \(n^{-D}\). This excludes the
omitted-coordinate exit. The physical tube is also justified
conditionally, rather than assumed for the restored network. On the
omitted Gaussian norm and input-value event, its initial feature Gram
differs from the retained Gram by
\(n^{-1/2}\operatorname{polylog}n\). The omitted row and column
have bounded Euclidean norm; embedding them increases the initial hidden
operator bound by at most a fixed constant. The first-weight normalized
Frobenius change vanishes. The same deterministic small-label fitting
argument, with enlarged fixed bounds and the retained strict Gram margin,
then supplies the full physical tube. The Gaussian norm/input exceptions
are again at most \(n^{-D}\). Constants in that deterministic argument
are fixed before the label threshold, as in the original theorem.

Consequently, for every retained cavity in this good set, the restored
full path and the explicit Gaussian/response equations agree within
\(\varepsilon_n\) through \(T_n\), with conditional probability
at least \(1-Cn^{-D}\). Crude fitting tails extend any required field
consequences past \(T_n\) after choosing \(C_T\kappa>3\). This
statement does not assert a polynomial probability bound for the cavity
good set itself.

It now gives a legitimate local Stein comparison. On the conditional
exception define an auxiliary innovation equal to its reference Gaussian
vector; on success use the actual innovation. Its weighted error in
(11) is \(O(\varepsilon_n)\), by the pathwise bound and Gaussian
moments. For compactly supported \(C^2\) tests, replacing this auxiliary
innovation by any measurable finite innovation extension changes the
Stein functional by at most \(C_{\psi,Q}n^{-D}\): both
\(I_i\psi(I)\) and the required test derivatives are bounded.
This is a proof-only extension and does not alter training.

The safe resulting assertion is a Gaussian Stein identity conditional
on each individual cavity in its own good set. Those sets differ with
the omitted neuron, and their covariances and response traces differ as
well. It does not produce one common conditionally independent ensemble,
nor does it identify any deterministic finite-width center with the
population fixed point. Those nonsymmetric conditioning and bias issues
remain separate.

## 5. First variations with respect to tagged external histories

The local insertion has a useful C1 strengthening that avoids
differentiating its unknown error. Work on its successful full/cavity
event through \(T_n\), and write \(A_n=e^{C\sqrt{\log(e+n)}}\),
allowing a fixed number of enlargements. Add to the omitted neuron a
prescribed forward-preactivation history or a prescribed reverse-carrier
history \(\epsilon u_a(t)\), with \(\max_{a,t}|u_a(t)|\le1\).
The latter means the same explicit extra lower gradient force used in
the exact deletion identity. Differentiate at \(\epsilon=0\). The
cavity has no such neuron, so its path and all its reference kernels
remain fixed.

The full mobility-parameter derivative has norm at most \(A_n\).
For a forward pulse its direct forcing is the sum of the adaptive
rank-one term and \(-2p_a r_a B_a^\top e_i u_a\); their norms are
at most \(A_n\), and the residual-weighted part has bounded activity.
The remaining term integrates over \(T_n\). A reverse pulse has
forcing \(-2p_a r_a C_a^\top e_i u_a\). The unperturbed full
variational propagator has the same bound as the cavity propagator.
Variation of constants therefore bounds the full parameter derivative,
and the forward/backward recursions give
\[
 \max_{a,t}\{|\partial_\epsilon a_a|,
                         |\partial_\epsilon b_a|\}\le A_n,
 \tag{16}
\]
where \(a_a=h_{a,i}\), \(b_a=\delta_{a,i}\) are the insertion
controls. These are bounds at zero perturbation; a tube for a finite
nonzero perturbation is unnecessary.

Hold all insertion controls fixed when taking the retained parameter
Jacobian. Let \(D F_{\rm aug}\) denote that Jacobian at the actual
retained state and its actual sources, and let \(D F_0\) denote the
cavity Jacobian. Then
\[
 \|D F_{\rm aug}(t)-D F_0(t)\|_{\rm op}
                   \le\varepsilon_n A_n.
 \tag{17}
\]
The structure verifies (17), rather than a generic bound on a third
flow derivative. Every retained preactivation and backward coordinate
differs from its reference by \(\varepsilon_n\), while a changed
hidden matrix has operator norm at most \(A_n/\sqrt n\). In a
forward Jacobian the direct feature change appears divided by
\(\sqrt n\), and changed gates have coordinate maximum
\(C\varepsilon_n\). Thus all forward Jacobian changes are
\(\varepsilon_n A_n\) in operator norm. The prediction Hessian's
only large diagonal is \(k\phi''(z)\); its change is bounded by
\[
 |k-k^0|\,\|\phi''\|_\infty+
       |k^0|\,\|\phi'''\|_\infty|z-z^0|
                       \le\varepsilon_n A_n.
 \tag{18}
\]
The mixed weight terms retain their inverse-root-width factor. The
adaptive negative-Gram term changes by \(A_n/\sqrt n\), because
the original gradient has norm \(C\sqrt n\) and its change has
Euclidean norm \(A_n\). Finally the reverse-source Hessian is a
lower-network adjoint probe. Its reference coordinate maximum and its
segment change are \(\varepsilon_n A_n\), by the already checked
probe subtraction. The residual derivative multiplying that probe is a
rank-one term of inverse-root-width size. These account for every term
in the augmented Jacobian. Bounded \(\phi'''\) suffices in (18).

The derivatives of the learned omitted row and column remainders still
have size \(A_n/\sqrt n\). For example, differentiate their exact
rank-one update integrals: differentiating a scalar omitted control
uses (16), differentiating a retained vector uses the full parameter
derivative bound, and an undifferentiated retained vector has norm
\(C\sqrt n\) next to the update's factor \(1/n\). A differentiated
residual is at most \(A_n/\sqrt n\). The top omitted-prediction
offset has derivative \(A_n/n\), and hence forcing derivative
\(A_n/\sqrt n\).

Let \(\Theta'\) be the retained parameter derivative and let \(V'\)
be (11) of the direct note with controls replaced by
\(a'_a,b'_a\). This differentiation does not change any cavity kernel.
Set \(U'=\Theta'-V'\). Subtracting the two linear equations gives
the cavity variational equation for \(U'\), forced by
\((D F_{\rm aug}-D F_0)\Theta'\), the changes of the external
source derivative maps, and the learned-source derivative remainders.
The external derivative-map differences obey the same
\(\varepsilon_n A_n\) bound: their factors are the prediction
gradient, its forward/backward derivatives, and the forward Jacobians
already estimated in (17). Using (16), integrating up to \(T_n\),
and applying the cavity propagator gives
\[
 \sup_{t\le T_n}\|\Theta'(t)-V'(t)\|_2
                   \le\varepsilon_n A_n.
 \tag{19}
\]
The forward and backward reconstruction derivatives have the same
error. Pairing with the omitted row or column preserves this bound.
The centered quadratic forms remain controlled because the Gaussian
kernel event was uniform over all bounded scalar controls; the
derivative controls in (16) merely enlarge its final envelope. In the
learned row/column scalar equations, derivatives of the full empirical
pairings and residuals cost \(A_n/\sqrt n\), whereas the cavity
coefficients are held fixed. Thus the scalar Gaussian/response equations
(19) of the direct note hold with a C1 error
\(n^{-1/2}e^{C\sqrt{\log(e+n)}}\) for these tagged histories.

The proven norm is the operator norm from bounded external histories to
the supremum of the resulting field response. It does not assert
pointwise approximation of an off-diagonal memory density after sending
a pulse duration to zero.

## 6. Exact averaged identities for the response traces

The trace kernels in the direct note have an exact finite meaning that
fits this C1 norm. In any retained network fix layer \(\ell\), and
define \(B_a=D_\Theta\delta_a^{(\ell)}\) and
\(E_a=D_{e_a}\delta_a^{(\ell)}\), where \(e_a\) is an external
preactivation at that layer. For each coordinate \(i\), conduct a
separate derivative experiment with history \(e_{b,i}=\epsilon u_b\)
and all other coordinates zero. No experiments are actually run; these
are variational equations along the same unperturbed trajectory.
The diagonal response averaged over these separate derivatives is exactly
\[
 \begin{aligned}
 \frac1n\sum_i\partial_\epsilon\delta_{a,i}^{(\ell)}(t)
 &=\frac1n\operatorname{tr}E_a(t)\,u_a(t)\\
 &\quad+\sum_b\int_0^t\frac1n\operatorname{tr}
       [B_a(t)J(t,s)P_b(s)]\,u_b(s)\,ds\\
 &\quad-2\sum_b p_b\int_0^t r_b(s)
       \frac1n\operatorname{tr}
       [B_a(t)J(t,s)B_b(s)^\top]u_b(s)\,ds.
 \end{aligned} \tag{20}
\]
The sum on the left is understood with the coordinate-matched derivative
experiment for each \(i\), not with one pulse applied simultaneously
to all neurons. The first term is the direct algebraic derivative at
time \(t\). The middle term has absolute size \(A_n/n\), uniformly
over bounded histories, because \(P_b\) has rank one.

Similarly, let \(C_a=D_\Theta h_a^{(\ell-1)}\). Apply a reverse
carrier history \(q_{b,i}=\epsilon u_b\) at layer \(\ell-1\),
again in separate coordinate experiments. Its exact averaged forward
response is
\[
 \frac1n\sum_i\partial_\epsilon h_{a,i}^{(\ell-1)}(t)
 =-2\sum_b p_b\int_0^t r_b(s)
       \frac1n\operatorname{tr}
       [C_a(t)J(t,s)C_b(s)^\top]u_b(s)\,ds.
 \tag{21}
\]
This follows directly from the forcing
\(-2p_b r_b C_b^\top e_i u_b\) and forward differentiation.

Equations (20)--(21) identify the entire integrated trace response with
an empirical average of diagonal scalar responses. Applying the C1
insertion comparison to each of these tagged derivatives is therefore
the correct next trace-identification step. If the trace was originally
computed in a network with another deleted neuron, this step requires
the corresponding two-deletion comparison, possibly in neighboring
layers. Their single shared initialized edge must be handled explicitly;
it has size \(n^{-1/2}\) and is not a pair of independent omitted
Gaussian coordinates. No two-layer-deletion theorem is asserted here
without that check.

One can also remove adaptive residual differentiation at the level of
these averaged traces. Let \(J_{\rm fr}\) be the propagator with
only the residual-Hessian generator, so the residual trajectory is held
fixed when varying parameters. The difference \(J-J_{\rm fr}\) is
an integral of terms with the rank-\(m\) negative-Gram factor.
Both propagators have norm \(A_n\). Between either pair of endpoints
in (20)--(21), normalized trace of each integrand is at most
\(C_mA_n/n\); integrating over \(T_n\) preserves that envelope.
This explains quantitatively why the population's source derivatives
hold scalar residual coefficients fixed. It does not establish the
remaining exchangeability/localization comparison of their empirical
averages with deterministic population expectations.

## 7. Cavity weights and finite-width centers

The following localization argument addresses that comparison with a
finite-width center; it does not identify the center with the population.
Use neuron-permutation-equivariant cavity weights \(0\le\chi_i\le1\),
measurable with respect to the initialization with neuron \(i\) removed.
Choose them as Lipschitz scalar cutoffs of: initial feature-Gram margin,
the cavity joint exponential budget, and its maximum coordinate magnitude.
Use fixed plateaus and strictly larger support budgets. For the maximum,
use a plateau up to \(M_0=C\sqrt{\log(e+n)}\) and support below
\(2M_0\). Multiply by initial operator/Frobenius norm cutoffs with
fixed large plateaus. The constants are selected before the fixed
small-label threshold. The established qualitative finite-cavity theorem
gives \(\mathbb E\chi_i\to1\), in particular
\(\mathbb E\chi_i\ge1/2\) for large width.

Here are the deletion moduli needed for these weights. All statements
concern bounded training fields and fixed depth.

First, a common successful insertion event compares every cavity with
the full network whenever at least one of these weights is nonzero.
To construct it, use Section 4 for the restored neuron of any supported
cavity. Conditional failure is \(n^{-D}\); union over possible
supported indices costs a factor \(n\). For each other cavity, stop
its reference path at a budget twice the support budget and a maximum
twice the support maximum. The Gaussian-kernel lemma holds conditional
on that separately stopped cavity, with failure \(n^{-D}\), even
if it would eventually hit its stop. Initial Gram and physical-tube
margins transfer from the full initialization by the deterministic
deletion comparison. The new insertion bound, applied up to the earlier
stop, keeps each retained field within \(\varepsilon_n A_n\) of
the already controlled full path. Its strictly larger budget and maximum
cannot be reached. This is the same strict-margin continuation argument
as the old cavity proof, now using the improved rate. Union of all these
conditional exceptions still has polynomially small unconditional
probability. No independence is claimed after the intersection.

On this event, the initial feature-Gram difference between any two
cavities is \(\varepsilon_n A_n\). For the joint exponential budget,
the shared retained coordinates give the bound
\[
 C\varepsilon_n A_n e^{C\eta M_0}
                 +\frac{C}{n}e^{C\eta M_0},
 \tag{22}
\]
where the last term accounts for the differing omitted neurons. This
remains \(n^{-1/2}e^{C'\sqrt{\log(e+n)}}\). The Lipschitz
budget and Gram cutoffs inherit that modulus.

The raw maximum does not have a deterministic deletion modulus: deleting
the maximizing neuron can change it substantially. For its cutoff,
separate this missing-coordinate case. If neither missing neuron exceeds
the plateau threshold, a maximum in the transition region is attained
among shared retained coordinates, so its change is
\(\varepsilon_n A_n\). If the problematic missing neuron is \(j\),
condition on the initialization of cavity \(j\), regardless of whether
\(\chi_j\) is zero. The common-success bootstrap above puts this
cavity in its own larger, cavity-measurable good set whenever some
weight is supported. Section 4 and (14), applied with those larger
fixed budgets, bound the probability of that good set together with a
restored tagged-\(j\) value above the threshold by \(n^{-D}\).
Enlarge the coefficient in \(M_0\) and, if needed, decrease the fixed
label threshold before this application. The common full/cavity
comparison transfers the full tagged value to the missing coordinate
of cavity \(i\), with an \(\varepsilon_n A_n\) tolerance. This
uses the omitted neuron's own Gaussian conditioning even when only
\(\chi_i>0\). A union over pairs still costs only a polynomial factor.

Operator norms are likewise not deterministically Lipschitz under
deleting a row or column. Their cutoffs are handled on the usual fixed
initialized Gaussian operator-norm and first-weight Frobenius event,
where they all equal one. Its complement has probability \(e^{-cn}\)
for sufficiently large fixed norm bounds: an exponential-size sphere net
and Gaussian scalar tails prove the hidden operator bound, while the
chi-square exponential moment proves the Frobenius bound. All cavity
submatrix norms are bounded by their full initial matrix norms. Thus this
step does not use a trained operator-norm deletion modulus.

It follows that the weights can be chosen so that
\[
 \mathbb E|\chi_i-\chi_j|
 \le n^{-1/2}e^{C\sqrt{\log(e+n)}}+C n^{-D_0}
 \tag{23}
\]
for any prescribed fixed \(D_0\), after choosing the conditional
exponents above sufficiently large. The assertion is in expectation;
it does not falsely assert deterministic continuity of the raw maximum.

Now let \(\Phi_i\) be any exchangeable bounded scalar neuron
observable, with \(|\Phi_i|\le H_n\), where
\(H_n\le e^{C\sqrt{\log(e+n)}}\), and let
\(F_n=n^{-1}\sum_i\Phi_i\). The observable may be a proof-only
bounded extension of a field product or a diagonal response. Equivariance
gives the exact identity
\[
 \mathbb E[\Phi_i\chi_i]-\mathbb E[F_n\chi_i]
 =\mathbb E\left[\Phi_i\left(\chi_i-\frac1n\sum_j\chi_j\right)\right].
 \tag{24}
\]
Indeed interchanging indices \(i,j\) gives
\(\mathbb E[\Phi_j\chi_i]=\mathbb E[\Phi_i\chi_j]\).
Combining (23)--(24) bounds their difference by
\(n^{-1/2}e^{C\sqrt{\log(e+n)}}\).

Suppose this particular empirical observable has a bounded global
Gaussian-root Lipschitz extension \(\widetilde F_n\) with constant
\(n^{-1/2}e^{C\sqrt{\log(e+n)}}\), agreeing with \(F_n\) on
the full physical event just constructed. Put
\(c_n=\mathbb E\widetilde F_n\). Gaussian concentration and its
integrated tail give
\(\mathbb E|\widetilde F_n-c_n|
 \le n^{-1/2}e^{C\sqrt{\log(e+n)}}\).
Conditional no-exit on the support of \(\chi_i\) bounds
\(\mathbb E[|F_n-\widetilde F_n|\chi_i]\) by
\(C H_n n^{-D_0}\). Therefore
\[
 \left|\frac{\mathbb E[\Phi_i\chi_i]}{\mathbb E\chi_i}-c_n\right|
             \le n^{-1/2}e^{C\sqrt{\log(e+n)}}.
 \tag{25}
\]
This uses no rate for the probability that the original good event
fails. The support indicator remains cavity measurable when applying
the conditional Gaussian/response identities to its left side.

The Lipschitz-extension hypothesis in this last paragraph must be proved
for each desired observable. It is already available for predictions
from the self-averaging study result; applying it to empirical
covariances and integrated response traces requires their own structured
derivative estimates. Even once that is done, (25) identifies a weighted
conditional scalar response with a **finite-width center**. A stable
map from covariance and represented-response centers to the canonical
Gaussian population remains necessary. The weighted localization does
not supply that final stability theorem.
