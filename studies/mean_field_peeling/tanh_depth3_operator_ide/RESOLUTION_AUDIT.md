# Resolution audit: three-hidden-layer nonlinear operator IDE

Status: exact autonomous contract and several convergence theorems proved;
the unconditional nonzero-label compact-time width theorem remains open.

## 1. Activation verdict

Among the smooth scalar candidates audited, `tanh` is the strongest proof
substrate:

- every forward feature is coordinatewise bounded;
- the trained readout is a Gaussian field plus a bounded shift;
- the learned-adjoint parts are coordinatewise bounded current fields;
- `d=sech^2=1-tanh^2` is a polynomial in the activated coordinate; and
- `d'/d=-2 tanh` is bounded, so diagonal cotangent growth is removable by an
  exact integrating factor.

The proposed leaky arctangent has a useful derivative floor, but its linear
tail preserves arbitrary normalized-`L2` concentration and supplies no
quenching of a focused cotangent.  `arsinh` deterministically maps every
normalized-`L2` ball into empirical `psi_1`, but its forward fields remain
unbounded and it does not regularize an adaptive immutable transpose.

No smooth genuine scalar nonlinearity can eliminate the need for a
reachable-state estimate on ordinary `L2` balls.  If `phi'(s) != phi'(t)`,
take `A_n=sqrt(n)e_1` and preactivations `s e_1,t e_1`: the preactivation
difference vanishes in normalized `L2`, while
`A_n(phi'(s)-phi'(t))` has order-one norm.  This is an ambient rigidity
result, not a canonical-trajectory counterexample.

A separate perturbative audit found a cleaner near-identity candidate than
leaky arctangent,

\[
 \phi_\epsilon(x)=
 \frac{x+\epsilon(\sin x-e^{-1/2}x)}
 {\sqrt{1+\epsilon^2\mathbb E(\sin G-e^{-1/2}G)^2}}.
\]

It is globally bi-Lipschitz and all derivatives of order at least two are
`O(epsilon)`.  Nevertheless its first feature-time derivative already has a
nonvanishing adaptive-transpose response of order `epsilon`.  Therefore the
identity theorem plus an `o_n(1)` perturbation is not a valid proof for any
fixed nonzero `epsilon`.  This candidate remains interesting only if a
current response-operator formulation can itself be proved convergent.

## 2. Frozen one-time state equation

Let `G_l=Gamma_l+P_l`, with immutable joint Gaussian actions and their true
adjoints.  The current state is only

\[
 (Y,A,P_1,P_2),\qquad Y=\tanh u.
\]

Reconstruct

\[
 Z_2=G_1Y,\quad X_2=\tanh Z_2,\quad
 Z_3=G_2X_2,\quad X_3=\tanh Z_3,
\]

\[
 B_3=(1-X_3^2)A,\quad Q_2=G_2^*B_3,
\quad B_2=(1-X_2^2)Q_2,
\]

\[
 Q_1=G_1^*B_2,\qquad B_1=(1-Y^2)Q_1,\qquad
 f=\langle A,X_3\rangle,\qquad e=y-f.
\]

Then the exact candidate IDE is

\[
\begin{aligned}
 \dot Y&=2\eta e(1-Y^2)B_1,&
 \dot A&=2\eta eX_3,\\
 \dot P_1&=2\eta eB_2\otimes Y,&
 \dot P_2&=2\eta eB_3\otimes X_2.
\end{aligned}
\]

Its direct raw kernel is

\[
 K=\|X_3\|^2+\|B_3\|^2\|X_2\|^2
   +\|B_2\|^2\|Y\|^2+\|B_1\|^2,
\]

and exactly

\[
 \dot f=2\eta eK,\qquad \dot e=-2\eta eK.
\]

This state is Markovian, restartable, and has a constant number of current
vector/operator species.  It contains no two-training-time kernel, response
history, path measure, or time-growing rank-one list.

## 3. Proved convergence statements

1. The displayed finite-width algebra, kernel, and energy identities are
   exact.
2. Compact-time normalized-`L2`, operator, and trace-norm bounds are uniform
   in width.
3. Every fixed finite Euler mesh has the joint transpose-reusing Gaussian
   program limit represented by the frozen source.
4. At initialization the two immutable-adjoint fields have square-uniformly
   integrable coordinates.  Moreover
   \[
   K_n(0)\longrightarrow K_0\simeq0.7357209343.
   \]
5. The raw kernel is stochastically equicontinuous at initialization:
   \[
   \lim_{\delta\downarrow0}\limsup_n
   \Pr\!\left(\sup_{t\le\delta}|K_n(t)-K_n(0)|>\epsilon\right)=0.
   \]
   The same argument excludes concentration on every `o(n)` coordinate set
   on a vanishing time interval.
6. For the special zero label, the residual clock is `o_P(1)` on each fixed
   physical horizon, so the complete compact-time kernel statement follows.

Thus no canonical initialization-scale boundary layer can disprove the
target.  The unresolved regime is a fixed nonzero label and order-one
feature time.

## 4. Exact conditional theorem

It is sufficient to prove, uniformly for the exact and comparison flows,

\[
 \sup_{t\le T}\frac1n\sum_j
 \left[
 e^{| (\Gamma_2^*B_3(t))_j|/C_T}
 +e^{| (\Gamma_1^*B_2(t))_j|/C_T}
 \right]=O_{\mathbb P}(1). \tag{AG_T}
\]

Under `(AG_T)`, truncation gives the Osgood comparison modulus

\[
 \omega(r)\lesssim r\{1+\log_+(1/r)\},
 \qquad\int_{0^+}\frac{dr}{\omega(r)}=\infty.
\]

Consequently the IDE is unique in the reachable class, exact and Euler
flows are stable, clipping can be removed, and the finite predictor, raw
kernel, residual, and loss converge uniformly on compact physical time.

## 5. Why the remaining lemma is not cosmetic

The learned part is harmless, for example

\[
 P_2(t)^*B_3(t)=\int_0^t2\eta e(s)X_2(s)
 \langle B_3(s),B_3(t)\rangle\,ds,
\]

so it is coordinatewise bounded.  Only the two immutable adaptive transpose
queries remain.

- Cavity interpolation makes the fresh part conditionally Gaussian and
  removes every dangerous diagonal coefficient by the tanh integrating
  factor.  It leaves transverse anisotropic products not controlled by
  `L2 x L2` estimates.
- Malliavin integration by parts gives the exact creation--response split
  \[
  (\Gamma^*B)_j=\delta_j(B/\sqrt n)
  +n^{-1/2}\operatorname{tr}D_jB.
  \]
  Absolute estimates generate all weighted response orders and exhaust a
  fixed exponential radius.
- MSE dissipation does not supply a signed cure: the residual-Hessian part
  of the variational equation is indefinite, and the exact Stein recurrence
  contains trace and shear responses of either sign.
- A quantitative tail envelope yields a deterministic short restart step,
  but an arbitrary adaptive frozen transpose can destroy every
  superquadratic tail functional.  Fine time partitions allow coherent
  accumulation on the same column.
- Weak compactness plus the loss energy equality is circular unless the
  limiting nonlinear adjoint graph and chain rule have already been
  identified.
- Letting the Euler program length grow with width additionally requires a
  robust-rank/no-amplification theorem for its adaptive query spans.  Two
  individually well-tailed, nearly identical queries can hide a localized
  direction whose opposite transpose carries order-one square energy.

These are proof-route obstructions.  No positive-time canonical focusing
trajectory has been found.  Conversely, none of the available estimates
proves that canonical dynamics cannot create one.

Adjoining one current sensitivity operator does not repair the width proof.
At finite width `(Theta,J)` is algebraically Markov and `J=D Theta` computes
the first divergence correction.  Controlling that random trace by another
Stein/Sobolev step requires `H=D^2 Theta`, and recursive control raises the
order indefinitely.  Keeping the full finite Jacobian and all Gaussian
tensor amplifications is a tautological tangent lift of the microscopic
flow, not the kind of compressed operator IDE accepted here, and it has no
proved strong width limit.

## 6. Claim-level conclusion

| Claim | Status |
|---|---|
| Activation selection among the audited smooth scalar candidates | `tanh` selected |
| Exact finite algebra and direct raw kernel | proved |
| O(1)-species, one-time, restartable operator IDE | proved algebraically |
| Fixed-mesh Gaussian-source identification | proved |
| Initialization and vanishing-time raw-kernel convergence | proved |
| Zero-label compact-time theorem | proved |
| Nonzero-label compact-time theorem conditional on `(AG_T)` | proved |
| `(AG_T)` for the canonical positive-time trajectory | open |
| Canonical counterexample to `(AG_T)` | none known |

It would therefore be false to label the requested nonzero-label depth-three
extension either proved or disproved.  The algebraic contract is frozen and
passes the strict autonomy audit; its single surviving bridge is the
orientation-sensitive, positive-time immutable-adjoint estimate `(AG_T)`.
