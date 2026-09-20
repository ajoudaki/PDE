# Recovered projected-selector theorem — 2026-09-20

The user explicitly resumed this existing study. This is research-state
recovery, not a new theorem, fresh independent proof review, or promotion.
The eleven-study map and all 39 historical entries remain in HANDOFF.md and
RESULTS_INVENTORY_HANDOFF_20260920.md. They were read as administrative
navigation; no originating artifact from another study was retrieved or
used as a scientific input.

The overarching question remains what nonlinear training organizes in the
complete population state: hidden geometry, learning obstructions, bad basins,
rates, and predictions beyond training inputs. This continuation concerns
the selected optimizer and its mobility restriction. The older ordinary-GF
limiting-rate campaign remains paused.

## Exact model and quantifiers

The theorem concerns the exact canonical order \(p=1\), bias-free,
two-hidden-layer closure with \(\phi=\tanh\), inputs
\(x_i\in\sqrt2 S^1\), labels \(y_i\in\{-1,+1\}\), and positive masses
\(\mu_i\) summing to one. Duplicate inputs have equal labels and antipodal
inputs opposite labels. Merge compatible constraints with signed labels
and summed masses before forming inverses. The remaining count \(m\) is
arbitrary but finite.

The frozen correlated Gaussian marks, lower Cholesky normalization, ridge
\(\eta_1=1/4096\), and actual middle-matrix transpose are unchanged.
The full dictionaries have sizes five and three, including constants.
The populations remain function fields, with physical population \(L^2\)
norms for \(w,c\) and Frobenius norm for \(M\). Initialization is
\(h_0=(g,D)\), \(c_0=0\), where \(h=(w,M)\).

\[
a_h(x)=\mathbb E_1[b_1\phi(w\cdot x/\sqrt2)],\qquad
H_h(x)=\phi(b_2^\top M a_h(x)),\qquad
f_{h,c}(x)=\mathbb E_2[cH_h(x)].
\]
\[
(A_hc)_i=\sqrt{\mu_i}f_{h,c}(x_i),\quad
Y_i=\sqrt{\mu_i}y_i,\quad K_h=A_hA_h^*,\quad
e=A_hc-Y,\quad L=|e|^2.
\]
Thus \(|Y|=1\) and \(L(0)=1\). CANONICAL_FEATURES.md proves
\(\sigma=\lambda_{\min}(K_{h_0})>0\) for every such merged dataset.
This is a derived initialization fact, not an assumed future Gram bound.

## Complete sufficient parameter prescription

Use \(B_j=\operatorname{ess\,sup}|b_j|\) and set
\[
\begin{gathered}
a_1=4B_1B_2,\qquad a_2=8B_1B_2,\qquad a_3=2a_1^2+a_2,\\
r=\min\{1/2,\sigma/(8a_1)\},\qquad
C_J=\frac{32a_1^2}{\sigma^3}
       +\frac{4(a_3+a_1^2)}{\sigma^2},\\
J(h)=\tfrac12Y^\top K_h^{-1}Y,\qquad
b=\sqrt{2/\sigma},\qquad R=12/\sigma,\\
\epsilon=\sigma/8,\qquad 0<\eta\le\sqrt{\epsilon/4},\qquad
\delta=\min\{\epsilon/8,\sigma/16,1/(4bR)\}.
\end{gathered}
\]
Here \(\eta\) is the noise amplitude, distinct from the initialization
ridge \(\eta_1\). One explicit sufficient choice is
\[
\rho\ge\max\left\{
1,\ C_J+1+4J(h_0)/r^2,\ (R/r)^2,\
(2a_1/\sigma)^2,\ (4a_1/\delta)^2,\ 2a_3R/\delta
\right\}.
\]
It gives precisely the conditions in PROJECTED_SELECTOR_LEAD.md, equation (1):
\[
\rho\ge C_J+1+4J(h_0)/r^2,\qquad
R/\sqrt\rho\le r,\qquad 2a_1/(\sigma\sqrt\rho)\le1,\qquad
\ell:=2a_1/\sqrt\rho+a_3R/\rho\le\delta.
\]
All quantities come from fixed data and initialization. This is a sufficient
bound, not a proved necessary or sharp mobility threshold.

## Optimizer and independently defined target

Use the requested parameter notation
\[
\theta=(\sqrt\rho(h-h_0),c),\qquad
T_\theta=D_\theta e,\qquad
P_\theta=I-T_\theta^*(T_\theta T_\theta^*)^{-1}T_\theta.
\]
The source proof calls these coordinates \(z\); its reviewed bytes are
preserved. This full-Jacobian projection in the scaled coordinates differs
from the readout-only projection onto \(\ker A_h\) in the older construction.

The rule is
\[
\dot\theta=-2T_\theta^*e-\epsilon P_\theta\theta
             +\eta\sqrt L\,P_\theta U_t,\qquad \theta(0)=0.
\]
Directions have Hilbert norm at most one and are held between refreshes
at a fixed positive interval. Every conclusion holds for every permitted
direction sequence. The explicit signed choice among \(m+1\) independent
bounded readout fields gives different state paths with positive probability
for every \(m\). This is a random ODE, not ordinary SGD or Brownian forcing.

Independently of the evolution,
\[
h_*=\operatorname*{argmin}_{\|h-h_0\|\le r}
\left\{J(h)+\tfrac\rho2\|h-h_0\|^2\right\}
\]
exists uniquely and is interior. Set
\[
c_*=A_{h_*}^*K_{h_*}^{-1}Y,\qquad
\theta_*=(\sqrt\rho(h_*-h_0),c_*).
\]
Equivalently, this pair minimizes
\(\rho\|h-h_0\|^2/2+\|c\|^2/2\) subject to fitting in the hidden ball.
The optimizer does not evaluate the target, \(\nabla J\), moving-readout
transport, or projector derivatives. It still requires the current
full-Jacobian \(m\)-by-\(m\) Gram inverse and exact population contractions.

The selected predictor is
\[
f_*(x)=\sum_i\sqrt{\mu_i}(K_{h_*}^{-1}Y)_i
            \mathbb E_2[H_{h_*}(x_i)H_{h_*}(x)].
\]
The selection rule, initialization, physical norms, data, and \(\rho\)
determine this function. The allowed noise realization does not.

## Proved conclusions and the three roles of large \(\rho\)

All permitted paths from canonical initialization exist uniquely for all
time, remain in the certified region, and satisfy
\[
L(t)\le L(0)e^{-2\sigma t},\qquad
\|\theta(t)-\theta_*\|
\le\|\theta_*\|e^{-\epsilon t/2},\qquad
\|\theta_*\|^2\le1/\sigma.
\]
The potential
\[
\Psi=\tfrac12\|\theta-\theta_*\|^2
=\tfrac12\{\rho\|h-h_*\|^2+\|c-c_*\|^2\}
\]
satisfies \(\dot\Psi\le-\epsilon\Psi-L\) almost everywhere and
\(L\le2(1+a_1^2R^2/\rho)\Psi\) on the reached ball.
It controls the original physical norm since \(\rho\ge1\).
Physical travel is finite. Predictions converge exponentially and uniformly
on the circle, and locally uniformly on \(\mathbb R^2\), to the same
deterministic function for all permitted noise paths.

The exact identities
\[
T_\theta P_\theta=0,\qquad
\dot e=-2T_\theta T_\theta^*e,\qquad
\dot L=-4\|T_\theta^*e\|^2
\]
protect descent. Confinement supplies
\(T_\theta T_\theta^*\succeq K_h\succeq(\sigma/2)I\).
The tangent drift removes state freedom invisible to training outputs;
the small-curvature estimate proves attraction to its selected target.

| Condition | Proof obligation it supplies |
|---|---|
| \(\rho\ge C_J+1+4J(h_0)/r^2\) | Strong convexity and an interior unique selected target |
| \(R/\sqrt\rho\le r\), \(2a_1/(\sigma\sqrt\rho)\le1\) | Confinement and persistent Gram positivity |
| \(\ell\le1/(4bR)\) | Control of the normal component of distance to the target |
| \(\ell\le\sigma/16\) | Coercivity of the projected selection drift through the target multiplier bound |
| \(\ell\le\epsilon/8\) | Absorption of the nonlinear Taylor remainder in the potential estimate |

The \(\sigma/16\) bound is redundant given \(\epsilon/8=\sigma/64\);
it remains displayed to identify the separate step where it is used.

## Limitations and next bottleneck

The physical loss terms are
\[
\dot h\big|_{\rm loss}=-\rho^{-1}\nabla_hL,\qquad
\dot c\big|_{\rm loss}=-\nabla_cL.
\]
The **hidden/readout rate ratio is \(1/\rho\)**; the potentially large ratio
is **readout/hidden, \(\rho\)**. Multiplying the whole equation by \(\rho\)
gives hidden rate one and readout rate \(\rho\), with path equivalence only
after also replacing \(U_t\) by \(U_{\rho t}\) and dividing the refresh
interval by \(\rho\). A clock change does not remove the disparity.

| Claim | Recovered status |
|---|---|
| Exponential fitting and one common state/function for the declared optimizer and data | Proved; previously internally checked; not promoted |
| Initial Gram positivity, target existence, confinement, finite travel | Proved components, not unverified trajectory premises |
| Strong state convergence implies uniform predictions on bounded input sets | Exact implication; alone it does not imply agreement across runs |
| Every fitting state has the same unseen predictions | Falsified by this study's initialized-feature readout construction |
| Nonzero hidden learning for every dataset, or substantial hidden movement | Not proved; HIDDEN_MOVEMENT.md proves nonzero selection-objective gradients for explicit pairs and nearby configurations |
| Comparable layer rates for the simple learned selector with all three guarantees | Open |
| Original equal-rate GF/SGD, higher orders, finite-width, quadrature or finite-step transfer | Outside this theorem |
| Empirical validation of the latest optimizer | None in this recovery; no implementation or experiment was run |

Gram conditioning, the certified radius, the rate and physical prefactors
depend on the dataset. No geometry-independent positive rate or computational
cost bound is proved. Selection continues on the zero-loss manifold, so
sending the noise amplitude to zero does not recover ordinary loss GF.
Uniqueness holds for fixed selection choices, not across different \(\rho\)
or among all interpolants. Neither hidden block is frozen, but the proof
restricts hidden displacement to a certified neighborhood.

The next theoretical target is to relax the mobility disparity while retaining
every compatible finite circle dataset, exponential fitting in a declared
clock, and one limiting function across allowed noise. The distinct uses of
\(\rho\) above must be addressed. Assuming a future Gram gap, proving only
per-run convergence, rescaling time, or substituting a frozen-feature endpoint
would not resolve this target. This identifies the bottleneck; it supplies
neither a new solution nor an impossibility theorem.

## Recovery evidence and ownership

The lead read current AGENTS.md and workflow Part 1, the three requested
study records, docs/README.md and docs/NOTATION.md, and the relevant established
model blocks: C.4.7.9 state/existence, C.4.7.10 B/C.1 and D.3.
The complete canonical-feature, model, variational-selector, projected-selector,
passive-limit, hidden-movement, and three associated review files were read.
Truncated display spans were reread separately.

Direct SHA-256 checks show that all six main proof/dependency files and all
three review reports match the final values recorded in README.md. In
particular PROJECTED_SELECTOR_LEAD.md is
96df35354d2b54f111db6d60bba3b5ebc01b8211d0ab61530cba1ec6118a827d,
and its review is
257f4736c7ff447a4c83cc08bb714e951d4b71fef71804a9717d277bacf59dd7.
The three established source hashes also match the recorded versions.
Complete reads and sha256sum restore the existing check status; this is
not a new isolated review.

A fresh scoped read-only agent, recover_selector_restrictions, mapped the
same conditions using only assigned within-study proof files and required
process skills. Its table agrees with the map above, confirms the reviewed
candidate hash and repaired clock convention, and identifies no new apparent
gap. It wrote no files. The lead owns this note and the README checkpoint.
No scientific claim was upgraded or superseded; the ratio wording clarifies
the convention already correct in the proof.

Observed HEAD was 613e8d3061b1e424419489dedb784adde9989f0e, with an empty
index and unrelated concurrent changes. Only this note and README.md were
edited. No Git transaction, book/code edit, experiment, or promotion occurred.
