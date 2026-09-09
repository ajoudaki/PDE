# R2: shifted-arctan contrast dynamics

Status: discriminating trajectory lemmas proved; the two-sample target
and the required response estimate remain OPEN. Analytic work only.

The main finding is that zero-readout gradient ascent of the contrast
cannot lose its initial readout contrast kernel. A second finding is
an exact, contrast-weighted backward-energy budget which does not grow
with the feature horizon. These give a concrete direction for weighted
response control, but do not establish that control. Both the persistent
floor and an action budget survive positive-contraction regularizations
of the full hidden gradient. That extension identifies an algebraic
condition a reference construction can preserve.

## Scope and provenance

This note retains the entire contract in CONTRACT_AND_LEDGER.md and
addresses only registry route R2, with the fixed activation

\[
 \phi(z)=1+\gamma\arctan z,\qquad \gamma=1/10.
\]

Both requested skills and the investigate-conjectures references
research-contract.md, evidence-ledger.md, and adversarial-audit.md were
read. The contract and registry were read in full. Relevant construction,
response, and gradient sections of the specified one-sample proof were
read; its SHA256 was independently checked as
bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e.
No two-sample result is imported from that proof. After the root update,
EXACT_TWO_SAMPLE_REDUCTION.md was read in full. Its initialization
positivity/scaling and its no-uniform-short-interval result are accepted
as prior results and are not rederived below.

R1 owns exchange symmetry, the physical clock, and first-layer
cross-input dynamics. Here the statements about contrast ascent concern
any existing trajectory of

\[
 g=(f_1-f_2)/2,\qquad \theta'=\nabla g,
 \qquad W^{(4)}(0)=0.                                      \tag{1}
\]

Primes denote feature time. The root gives dot(theta)=4(1-g) grad(g)
on a deterministic symmetric population flow, subject to its stated
existence/symmetry premises. Those premises are retained here. The
lemmas below do not assume existence beyond the interval on which they
are applied. They do not identify actual finite-width training with (1):
finite-width residual symmetry is not pathwise, and its prescribed
readout is small rather than exactly zero.

Write w=W^(4), alpha for all hidden parameters, and

\[
 U_\ell=(H^{(\ell)}_1+H^{(\ell)}_2)/2,\qquad
 V_\ell=(H^{(\ell)}_1-H^{(\ell)}_2)/2,\qquad
 \kappa_\ell=\|V_\ell\|_2^2.
\]

All vector norms and pairings are on their own neuron probability
spaces. Operator increments have the contract's Hilbert--Schmidt
metric. At finite width the corresponding vector norm is normalized
by sqrt(n). Thus

\[
 g=\langle w,V_3(\alpha)\rangle,\qquad
 \kappa_3=\tfrac14(K^{(4)}_{11}+K^{(4)}_{22}-2K^{(4)}_{12}).
                                                               \tag{2}
\]

The proof proceeds through the readout's convex norm, the resulting
hidden-action budget, and its exact decomposition into sample modes.
We then identify which regularizations preserve these estimates and
state the remaining response obstruction precisely.

## 1. A persistent readout contrast floor: proved trajectory lemma

Let V=V_3(alpha). Along any existing regular trajectory (1), let D_s
denote the hidden-to-output linearized map for V at the current state.
The ascent equations and the chain rule give

\[
 w'=V,\qquad \alpha'=D_s^*w,\qquad
 w''=D_sD_s^*w.                                          \tag{3}
\]

These formulas require no unrestricted Frechet differentiability of
a nonlinear map L^2 -> L^2. The needed derivative along a continuously
differentiable L^2 path follows by writing an activation difference as
its preactivation difference times the integral of phi' along the
connecting segment. Bounded phi' and truncation of the fixed L^2
velocity justify convergence in L^2. Each linearized forward step has
the form

\[
 dZ^{(\ell)}_a=dW^{(\ell)}H^{(\ell-1)}_a
                    +W^{(\ell)}dH^{(\ell-1)}_a,
 \quad dH^{(\ell)}_a=\phi'(Z^{(\ell)}_a)dZ^{(\ell)}_a.
\]

Bounded activations, gates, and current operators make D_s bounded
between the stated tangent Hilbert spaces. Pairing these steps in
reverse order proves alpha'=D_s^*w with exactly the contract's metric.
Consequently (3) is valid for classical finite trajectories and for
existing population integral trajectories with the stated continuous
fields and bounded operators. This is not an existence assertion.

Set k=||V(0)||_2^2, and suppose k>0. On an interval where r=||w||_2>0,

\[
 rr'=\langle w,V\rangle=g,
\]
\[
 r''=\frac{\|V\|_2^2-(r')^2+\|\alpha'\|^2}{r}\ge0.       \tag{4}
\]

Indeed <w,w''>=||D_s^*w||^2=||alpha'||^2, and
|r'|<=||V|| by Cauchy--Schwarz. Since w(s)/s -> V(0),
r'(0+)=sqrt(k). Formula (4) implies r'>=sqrt(k) on the first
positive-r interval. Its increasing r cannot return to zero, so this
argument applies throughout the existing trajectory. Therefore

\[
 \kappa_3(s)\ge k,\qquad g(s)\ge ks.                    \tag{5}
\]

The first inequality follows from ||V||>=r'>=sqrt(k); the second
from r>=s sqrt(k) and g=rr'. This does NOT say that kappa_3 itself
is monotone: its derivative is 2<V,D_sD_s^*w>, which has no sign
from positive semidefiniteness alone.

Also, exactly,

\[
 g'=\|V\|_2^2+\|\alpha'\|^2,\qquad
 \|w(s)\|_2^2=2\int_0^s g(u)\,du,                       \tag{6}
\]
\[
 \int_0^s\|\alpha'(u)\|^2du
            =g(s)-\int_0^s\kappa_3(u)du.                \tag{7}
\]

If the trajectory continues up to feature time 1/k, (5) forces a
unique first fitting point s_*<=1/k with g(s_*)=1. It does not prove
the continuation required for this statement. Before that point,

\[
 \int_0^s\|\alpha'\|^2du\le1,\qquad
 \|\alpha(s)-\alpha(0)\|\le\sqrt{s},\qquad
 \|w(s)\|_2\le\sqrt{2s}.                                \tag{8}
\]

Thus contrast decay cannot be the reason a continued trajectory fails
to fit. The unresolved issue is construction and response control on
the requisite interval, not loss of this readout lower bound.

## 2. An exact contrast-weighted backward budget

Assume, on the interval in question, only the equal sample second
moments supplied by the root's symmetric population formulation:

\[
 \|H^{(j)}_1\|_2=\|H^{(j)}_2\|_2,\qquad j=1,2.          \tag{9}
\]

No derivation of (9) is attempted here. It gives <U_j,V_j>=0.
Define delta^(ell)_+ and delta^(ell)_- as the half-sum and
half-difference of the two contract backward fields. The exact
hidden-matrix ascent equation decomposes as

\[
 (W^{(\ell)})'
   =\delta^{(\ell)}_-\otimes U_{\ell-1}
      +\delta^{(\ell)}_+\otimes V_{\ell-1},\qquad\ell=2,3.
                                                               \tag{10}
\]

The Hilbert--Schmidt pairing of rank-one operators is the product
of the two vector pairings. The cross term in the squared norm of
(10) therefore vanishes by (9), without any independence assumption:

\[
 \|(W^{(\ell)})'\|_{\rm HS}^2
 =\|U_{\ell-1}\|_2^2\|\delta^{(\ell)}_-\|_2^2
       +\kappa_{\ell-1}\|\delta^{(\ell)}_+\|_2^2.        \tag{11}
\]

Since phi>5/6 pointwise, ||U_j||_2>=5/6. Combining (7) and (11)
proves the horizon-independent, attained-trajectory estimate

\[
 \int_0^s\sum_{\ell=2}^3
 \left[\frac{25}{36}\|\delta^{(\ell)}_-\|_2^2
          +\kappa_{\ell-1}\|\delta^{(\ell)}_+\|_2^2\right]du
 \le g(s)\le1\quad(s\le s_*).                           \tag{12}
\]

This is a substantive relative-contrast control: the potentially large
common backward field is charged in proportion to the feature contrast
through which it actually changes the matrix. The backward contrast
field has an unweighted squared-integral bound. Constants in (12) do
not deteriorate with rho or with the length of the feature interval.
The result is exact under (1), (9), and existence; it is not a bound
for arbitrary states or for arbitrary clipped dynamics.

There is also no possible collapse of the lower feature contrasts on
an existing pre-fit interval. Forward Lipschitzness gives

\[
 \kappa_3\le\gamma^2\|W^{(3)}\|_{\rm op}^2\kappa_2,
 \qquad
 \kappa_2\le\gamma^2\|W^{(2)}\|_{\rm op}^2\kappa_1.
\]

With M_ell(s)=||W^(ell)(0)||_op+sqrt(s), (5), (8) imply

\[
 \kappa_2(s)\ge\frac{k}{\gamma^2M_3(s)^2},\qquad
 \kappa_1(s)\ge\frac{k}{\gamma^4M_2(s)^2M_3(s)^2}.       \tag{13}
\]

Thus (12) can be converted to finite unweighted backward L^2-in-time
bounds depending on rho on any existing pre-fit interval. Such bounds
are weaker than the distributional response bounds needed below.

## 3. Specific arctan relative-gate control

For all real z,z',

\[
 |\phi'(z)-\phi'(z')|\le|\phi(z)-\phi(z')|.             \tag{14}
\]

To prove this, put a=arctan(z), a'=arctan(z'). Then
phi'(z)=gamma cos^2(a), and the derivative of cos^2 has absolute
value at most one. This proves (14) with the fixed activation scale.

At the top layer put
p_+=(phi'(Z_1^(3))+phi'(Z_2^(3)))/2 and
p_-=(phi'(Z_1^(3))-phi'(Z_2^(3)))/2. Then

\[
 |p_-|\le|V_3|,\quad 0<p_+\le\gamma,\quad
 \delta^{(3)}_-=wp_-,\quad \delta^{(3)}_+=wp_+.
\]

For a=1+pi/20, (10) consequently yields

\[
 \|(W^{(3)})'\|_{\rm HS}
 \le a\|wV_3\|_2+\gamma\|w\|_2\|V_2\|_2.              \tag{15}
\]

Equation (15) is the concrete relative-contrast smallness present in
the actual update. Equation (12), rather than treating its two terms
separately by their suprema, gives the stronger integrated control of
the actual gated terms wp_- and wp_+.

It would be incorrect to replace ||wV_3||_2 by g=<w,V_3> without
another estimate. Neither pointwise positivity nor such an L^2/L^1
comparison has been obtained from the convex-readout argument.

## 4. Which auxiliary regularizations preserve the mechanism

There is an exact extension of the readout lemma. Suppose an auxiliary
hidden flow with the same forward map and readout equation satisfies

\[
 w'=V(\alpha),\qquad \alpha'=P_sG_s,\qquad
 G_s=D_s^*w,\qquad 0\le P_s\le I.                         \tag{16}
\]

Here P_s is a self-adjoint positive contraction on the raw hidden
tangent Hilbert space; it may depend on the current state. Assume the
regularity needed for the chain rule along the auxiliary curve. Then

\[
 \langle w,w''\rangle=\langle G_s,P_sG_s\rangle\ge0,\qquad
 g'=\kappa_3+\langle G_s,P_sG_s\rangle,                   \tag{17}
\]
\[
 \|\alpha'\|^2=\|P_sG_s\|^2
                      \le\langle G_s,P_sG_s\rangle.      \tag{18}
\]

For (18), positivity and the discriminant of
<P(x+t y),x+t y> give |<Px,y>|^2<=<Px,x><Py,y>.
For unit y, <Py,y><=1 because P is a contraction. Taking the
supremum over unit y proves ||Px||^2<=<Px,x>. The proof of (4) now
has the nonnegative term <G_s,P_sG_s> in place of ||alpha'||^2.
Hence both the persistent floor (5) and the action/displacement
bounds (8) hold for (16), independently of the contraction. No
derivative of P_s is needed: w''=D_s alpha'.

A concrete algebraic choice for a matrix block is common row scaling:

\[
 P_\ell A=M_{\lambda_\ell}A,\qquad
             0\le\lambda_\ell(\omega_\ell)\le1,          \tag{19}
\]

where M_lambda multiplies output fields by lambda. The SAME row
multiplier acts on both sample terms of the full raw layer gradient.
It is a self-adjoint positive contraction on Hilbert--Schmidt
operators: for an orthonormal input basis (e_j),

\[
 \langle A,P_\ell A\rangle_{\rm HS}
   =\sum_j\mathbb E[\lambda_\ell(Ae_j)^2]\ge0,\qquad
 \|P_\ell A\|_{\rm HS}\le\|A\|_{\rm HS}.
\]

The analogous common row scaling on the raw first-weight vector
field has the same property. Under (9), the matrix contribution
to <G,P G> is exactly

\[
 \|U_{\ell-1}\|_2^2
       \|\sqrt{\lambda_\ell}\delta^{(\ell)}_-\|_2^2
 +\kappa_{\ell-1}
       \|\sqrt{\lambda_\ell}\delta^{(\ell)}_+\|_2^2.       \tag{20}
\]

The cross term vanishes for the same reason as in (11).
Thus the budget (12) survives with sqrt(lambda_ell) inserted into
the backward factors. It is uniform in the cap for any such family
of multipliers, on each existing symmetric auxiliary trajectory up
to g=1. A smooth scalar function of the sum of the two squared raw
queries is one way to make the row multiplier exchange equivariant.
Equal feature norms still require the symmetry/uniqueness premise.

This is an auxiliary design lemma, not a replacement training model.
It specifically requires G_s to be the FULL UNCUT gradient evaluated
at the auxiliary state. If clipped backward fields are propagated
into earlier gradients, their field must be checked separately: it
need not equal P_sG_s. Conversely, scaling the full gradient does
not by itself prove L^2 local Lipschitz or tail bounds for a raw
two-query construction. No construction or removal of these
multipliers is claimed here.

## 5. Exact remaining obstruction and research disposition

The useful new mechanism is (12): even a very long pre-fit feature
interval has only a fixed amount of contrast-weighted backward
squared action. The obstruction to turning this into the old response
proof is identifiable at the middle gate. Write

\[
 q^{(2)}_\pm=(q^{(2)}_1\pm q^{(2)}_2)/2,
 \quad p^{(2)}_\pm=(\phi'(Z^{(2)}_1)\pm\phi'(Z^{(2)}_2))/2.
\]

Exactly,

\[
 \delta^{(2)}_-=p^{(2)}_+q^{(2)}_-
                         +p^{(2)}_-q^{(2)}_+,
 \qquad |p^{(2)}_-|\le|V_2|.                            \tag{21}
\]

The energy bound weights the top common backward norm by the scalar
kappa_2=E[V_2^2]. The second term of (21), and its response derivatives,
involve a same-neuron product with q^(2)_+. No estimate in this note
permits replacing ||V_2 q^(2)_+||_2 by
||V_2||_2 ||q^(2)_+||_2. Independence is unavailable after adaptive
matrix reuse. Controlling the whole sum delta^(2)_- also does not
control its two summands separately. These are missing estimates;
no claim is made that the actual product violates a valid bound.

More generally, (7), (12), and (13) supply second-moment/action
control. The one-sample removal-of-clipping argument instead used
uniform exponential-square tails of the actual middle backward query
in its reference programs, sufficiently strong to defeat an
exp(CR)-type comparison factor. Second-moment control alone does not
imply those tails. Section 4 proves a replacement for regularizations
of the precise form (16), including the weakened backward budget (20).
It does not establish that a well-posed raw two-query reference family
has that form and the needed response estimates. Applying (5)--(12)
to an arbitrary internally clipped backpropagation scheme remains
unjustified; the uncut identities cannot be assumed during its
construction.

| Claim | Status and exact scope |
|---|---|
| Readout norm is convex; kappa_3(s)>=kappa_3(0) | Proved on every existing zero-readout contrast-ascent trajectory |
| kappa_3(0)>0 and its order is 1-rho | Prior result from the root note; not new R2 evidence |
| Contrast-weighted backward budget (12) | Exact under existing ascent and equal sample feature norms (9) |
| Fixed arctan relative-gate estimate (14) | Proved; gives the actual update estimate (15) |
| Floor and action budget survive (16) | Proved for any existing regular trajectory with a positive contraction; (20) is the sample-mode version under (9) |
| Weighted response/tail estimates close on the required horizon | Open; (21) identifies the unresolved correlated product |
| Shifted arctan satisfies the complete two-sample target | Open; no global existence, restart, width/GD convergence, or all-time nonlinearity claim is made here |

The next concrete discriminator for this mechanism is a weighted
exponential-moment response estimate, or an attained-trajectory
counterexample to that estimate, for the source derivatives generated
by p^(2)_- q^(2)_+ in (21), using the budget (12) or (20).
It must preserve the common/contrast covariance weights and survive
the reference approximation used for construction. An arbitrary
whole-space counterexample, an unweighted response row growing large,
or a bound proved only for a pre-assumed uncut solution does not settle
that discriminator.

Nothing here falsifies the activation or the target. No old artifact
is superseded: the ledger's missing-floor observation is refined by
(5), which supplies a strictly positive, rho-dependent dynamical floor
without supplying the missing long-interval response proof.
