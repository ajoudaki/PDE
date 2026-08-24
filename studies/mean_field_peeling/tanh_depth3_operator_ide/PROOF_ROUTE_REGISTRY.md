# Proof-route registry

The target in every route is `(AG_T)` from `FROZEN_CONTRACT.md`.  A route is
rejected if it adds a second training time or a state whose size grows with
time.

| Route | Intended mechanism | Principal audit |
|---|---|---|
| Cavity/low influence | delete one initial column, prove its trajectory influence stays `o(n^-1/2)` in the anisotropic contraction | ordinary Osgood stability loses the needed exponent |
| Annealed Malliavin | decompose `Gamma^*b` into creation plus response and control a signed directional tangent | one integration by parts may regenerate a higher response hierarchy |
| Gated-cotangent lift | evolve `B_l` and use bounded `d'/d` to avoid raw inverse gates | gated tails alone need not control perturbations when `d` is tiny |
| Compactness/energy | identify a unique curve of maximal slope and recover `K` from energy dissipation | rejected stand-alone: energy upgrades an already identified weak limit, but identifying its chain rule requires the missing square-tail continuity |
| Canonical counterexample | realize adaptive row/column selection from iid data in fixed time | ambient selectors and pulses are not known to be reachable |

## First frozen-contract audit

The one-column interpolation gives the exact decomposition

\[
 (\Gamma_2^*B_3)_j
 =\gamma_j^*B_3^{(j)}
  +\int_0^1\gamma_j^*\partial_sB_3^{(j,s)}\,ds,
\]

and the analogous formula one layer lower.  The cavity term is conditionally
Gaussian.  The response starts at normalized scale `n^{-1/2}`.

For `d=sech^2` and `e=d'`, the exact gate identities include

\[
 \partial_t\log d(u)=Q_1e(u),
\]

\[
 \partial_t\log d(Z_2)
 =\|Y\|_n^2Q_2e(Z_2)+\frac{e(Z_2)}{d(Z_2)}W_2,
\]

with an analogous top-layer identity and `|e/d|<=2`.  Thus the raw diagonal
cotangent is removable by an integrating factor.  The unresolved response
terms are transverse products such as

\[
 W_rH_r,\qquad Q_2\,\partial_sZ_2,
 \qquad d(Z_r)^{-1}G_r\partial_s\dot X_{r-1}.
\]

No deterministic estimate for these products follows from the available
normalized-`L2`, operator, and trace bounds.  This is the current cavity
bottleneck; it is strictly smaller than the original raw-diagonal problem.

Separately, canonical initialization admits the exact short-time theorem

\[
 \lim_{\delta\downarrow0}\limsup_n
 \Pr\!\left(\sup_{t\le\delta}|K_n(t)-K_n(0)|>\epsilon\right)=0.
\]

It rules out every vanishing-time extreme-neuron or mesoscopic-focusing
counterexample.  It does not restart automatically at positive time because
the current cotangent has become adapted to the same immutable Gaussian
residual that supplies the transpose action.

The parallel Malliavin audit gives the exact current-time formula

\[
 (\Gamma_\ell^*B_{\ell+1})_j
 =\delta_{\ell j}\!\left(B_{\ell+1}/\sqrt n\right)
  +\frac1{\sqrt n}\operatorname{tr}D_{\ell j}B_{\ell+1}.
\]

The divergence term is a controlled Gaussian creation field.  Therefore a
same-order bound on the diagonal response trace and its Hilbert--Schmidt
derivative, uniformly for moments `p <= c log n`, implies `(AG_T)`.
Differentiating an actual transpose, however, creates an order-one rank-one
operator tangent.  Absolute Holder estimates then request moment `2p`, and
iteration generates every weighted response order.  A fixed `psi_1` radius
cannot control the resulting exponential response at parameter proportional
to `pT`.  Thus a signed cancellation or trajectory-specific incoherence
estimate is essential; an absolute Malliavin hierarchy is not a proof.

A subsequent signed audit also rejects a deterministic dissipativity
shortcut.  For loss Hessian

\[
 H_{\mathcal L}=\nabla f\otimes\nabla f+(f-y)\nabla^2f,
\]

only the first term is positive.  The residual-Hessian term expands tangent
directions and even volume on open finite-dimensional tanh configurations.
The exact even-moment Stein recurrence contains both a response trace and a
response shear, and both can have the adverse sign.  The still-viable signed
target is an *annealed same-order* coercivity estimate for their sum, through
`p <= c log n`; neither MSE energy nor `d'/d=-2 tanh` proves it pathwise.

Finally, a quantitative tail envelope does give a deterministic local
restart interval.  It does not propagate itself: a bounded-coordinate
increment adapted to one frozen Gaussian column can create a `sqrt(n)`
transpose coordinate, destroying every superquadratic de la Vallée-Poussin
functional.  Splitting time more finely does not help because the escaped
mass can accumulate coherently on the same column.  This remains an ambient
proof-route counterexample, not a canonically reachable trajectory.

The growing-mesh tensor-program audit supplies another conditional route.
After `m` Euler steps each immutable matrix has at most `m+1` left and right
queries, and its exact conditional law is a regression mean plus an
independent Gaussian action on the two orthogonal complements.  If query
Gram matrices have a quantitative robust-rank lower bound and the Euler
flow has a matching averaged stability estimate, one can take

\[
 m_n\asymp\left(\frac{\log n}{\log\log n}\right)^{1/3}
\]

and pass directly to continuous time.  Those hypotheses are not automatic.
Two well-tailed queries differing by `e_J` already span the localized vector
`sqrt(n)e_J`; discarding that small innovation loses an order-one square
defect after tanh and the opposite transpose.  The exact reopen condition is
a trajectory-specific no-amplification theorem for weak query innovations.
