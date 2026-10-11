# Scoped check of the two-sample escape route

**Verdict: PASS for the statements as scoped.** No mathematical error or
missing hypothesis was found. This is a reused-context mathematical
check, not an independent promotion review.

The sole scientific input was the complete 400-line
TWO_SAMPLE_ESCAPE_ROUTE.md, with SHA-256

    df4ffa713a5e6b55448e215b80f45bfdc02d375f404ad9373af2d2ed6598b24e

No other scientific source, reviewer report, experiment, or Git operation
was used. The source was not edited.

## Complete statement check

1. **Equations and global existence.** The factors in (1)–(3) agree
   with mean-two-sample squared loss and mobilities $(n,1,n)$.
   The parameter metric is the inverse-mobility metric. Integrable
   squared speed bounds displacement on finite horizons and excludes
   finite-time escape of the smooth finite-dimensional ODE.

2. **Sublinear growth and readout identities.** Splitting the path
   length at a fixed time and sending that time to infinity gives
   displacement $o(\sqrt t)$ from finite total gradient energy.
   Consequently $R(t)=\|w(t)\|_2^2/n=o(t)$.
   Differentiation gives
   $R'=-2f^\top r=-2(\|r\|_2^2+y^\top r)$.
   Cesàro averaging therefore gives (6); convergent predictions give
   the projection-circle identity (7). No bounded-parameter
   assumption is needed.

3. **Strict initial decrease and readout lower bound.** Conditional
   on invertible $W(0)$, the two Gaussian first preactivation columns
   have a density because the inputs are linearly independent.
   The successive tanh and invertible matrix maps preserve absolute
   continuity on open images. Thus $H(0)y=0$ is a null event for
   fixed $y\ne0$, including width one. The triangle inequality and
   $\|f\|_2\le\sqrt2\|w\|_2/\sqrt n$ prove (8).

4. **Conditional saturation classification.** Under (9), the explicit
   velocities $\dot w,\dot W$ have limits; their square integrability
   forces those limits to be zero. Rank two of $U_\infty$ then
   forces saturation in every nonzero-readout row for each nonzero
   residual coordinate. A single nonzero residual coordinate would
   contradict $H_\infty r_\infty=0$. With both nonzero, their
   magnitudes are equal and all contributing rows have the same
   common/contrast orientation. This proves (10)–(11), and bounded
   $u_a$ makes $\|W(t)\|_{\mathrm{op}}\to\infty$ necessary.
   The convergence and rank assumptions are explicit; rank two is
   naturally impossible at width one, so that case is simply outside
   this conditional statement.

5. **Balance calculation.** The derivative
   $(\sinh^2 p)'=2(u/D)\dot p$ gives the claimed invariant when
   $\rho=0$. Substituting both cross terms from (2) gives exactly
   (13), including its sign and factor $2\rho/n$. The conclusions
   concerning bounded first preactivations and divergent middle norm
   follow at fixed finite width. No coercivity at nonzero correlation
   is asserted.

## Detailed check of Section 5

Assume its eventual cone, separated residuals, $-1<\rho\le0$, and a
strict loss drop. All gates are positive at finite arguments and
$u_a,h_a,b_a,B_a$ are nonnegative in this cone.
Equation (2) then gives, componentwise,

$$
\dot p_{j1}\ge\delta D_{j1}B_{j1},\qquad
-\dot p_{j2}\ge\delta D_{j2}B_{j2}.
$$

Thus every $p_{j2}$ decreases inside a bounded nonnegative interval.
The fixed-width lower bound
$d_2=\min_j\operatorname{sech}^2(p_{j2}(T))>0$ implies

$$
\int_T^\infty\sum_i w_iE_{i2}\sum_jW_{ij}\,dt<\infty.
$$

The proof's split of first-layer columns is exhaustive:

- If $p_{j1}$ is bounded, its monotonicity and its positive gate
  lower bound make $\int_T^\infty B_{j1}\,dt$ finite.
  Since all summands of $B_{j1}$ are nonnegative, the upper bound
  $(W_{ij}^2)'\le(2\|y\|_2/n)W_{ij}w_iE_{i1}$ has an integrable
  right side. Hence that entire column of $W$ is bounded.
- Otherwise $p_{j1}\to\infty$, so $u_{j1}\to1$, while
  $u_{j2}\le\tanh p_{j2}(T)<1$. After one common finite time for
  the finitely many such columns, their contributions to
  $z_{i1}-z_{i2}$ are nonnegative.

The bounded columns contribute at worst a fixed finite negative
amount. Therefore $z_{i1}\ge z_{i2}-C$ uniformly over rows and the
tail. Nonnegativity of both preactivations gives

$$
\cosh z_{i2}\le e^C\cosh z_{i1},\qquad
E_{i1}\le e^{2C}E_{i2}.
$$

The latter inequality has the required direction. It makes the upper
bound on $(\|W\|_F^2)'$ integrable by the preceding $p_2$ budget.
No lower bound on that derivative is needed to deduce an upper bound
on the nonnegative quantity $\|W\|_F^2$.

Bounded $W$ and bounded $u_2$ give $E_{i2}\ge e_2>0$.
Consequently
$\int_T^\infty\sum_iw_i\sum_jW_{ij}\,dt<\infty$.
The inequalities $0\le\tanh z\le z$ for $z\ge0$ and $0\le u_{ja}\le1$
then imply $\int_T^\infty(f_1+f_2)\,dt<\infty$.

Finally the strict drop and zero initial readout give
$\Delta=\|y\|_2^2-2\mathcal L(T)>0$. At every later time,

$$
2y^\top f=\|f\|_2^2+\|y\|_2^2-\|r\|_2^2
\ge\|f\|_2^2+\Delta.
$$

Since $f\ge0$ and $y\ne0$,
$f_1+f_2\ge\Delta/(2\|y\|_\infty)>0$.
This contradicts integrability and completes the proposition.
No readout upper bound or convergence assumption is hidden in this
argument.

## Hypothesis and counterexample checks

- The strict loss drop is essential. With zero hidden parameters
  and zero readout, opposite-sign labels can satisfy the residual
  inequalities forever at the zero predictor; there is no loss drop,
  and this stationary state is correctly excluded.
- The sign of $\rho$ is used exactly in the two monotonicity
  inequalities. The argument does not extend unchanged to acute
  inputs.
- Nonnegative middle weights and readout are essential for the
  positive budgets. Signed cancellation is not controlled.
- Constants such as $d_2$, $C$, and $e_2$ may depend on the fixed
  width and trajectory. This is sufficient for the stated
  finite-width impossibility, but gives no uniform Gaussian
  probability or rate.
- Fixed hidden sign gauges and input/label sign absorption preserve
  the loss and mobilities as claimed. They do not make a generic
  dense Gaussian matrix nonnegative.

Accordingly the source's final scope statement is accurate: it proves
the listed finite-width obstructions, especially impossibility of the
specified sign-coherent separated-residual tail. It proves neither
unconditional Gaussian fitting nor a positive-probability Gaussian
failure mechanism, and it does not use the separate bad-critical-point
avoidance candidate.
