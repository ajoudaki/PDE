# Activation comparison during the unfrozen selection phase

Status: exploratory mechanism analysis, not a frozen choice.

## 1. Residual activations with a derivative floor

After harmless gain normalization, both

\[
\phi_\alpha(x)=\alpha x+(1-\alpha)\arctan x
\]

and

\[
\widehat\phi_\lambda(x)=\frac{x+\lambda\tanh x}{1+\lambda}
\]

have derivative in a fixed interval `[a,1]`, are odd, have at most linear
growth, and differ from a linear function by a bounded smooth term.

For residual tanh, a natural coordinate is also explicit.  Before gain
normalization, for `phi(x)=x+lambda*tanh(x)`,

\[
\Theta_\lambda(x)
=x-\sqrt{\frac{\lambda}{1+\lambda}}
\operatorname{artanh}\!\left(
 \sqrt{\frac{\lambda}{1+\lambda}}\tanh x
\right),
\tag{1}
\]

because `Theta'_lambda=1/(1+lambda sech^2 x)`.  It is a linear function plus
a bounded smooth correction.  Thus leaky arctangent does not uniquely win on
natural-coordinate or fixed-program complexity.  Its rational formulas are
somewhat simpler; residual tanh has faster curvature decay.

The derivative floor gives uniform equivalence of all weighted and raw
cotangents.  It does **not** deterministically prevent a reused Gaussian
transpose from concentrating a raw cotangent on a small coordinate set, and
it supplies no tail damping if such focusing occurs.

## 2. The power-damping family

A genuinely different family is defined by

\[
d_q(x)=\phi_q'(x)=(1+x^2)^{-q/2},
\qquad
\phi_q(x)=\int_0^x(1+s^2)^{-q/2}\,ds,
\qquad 0<q\le1.
\tag{2}
\]

Its natural coordinate is

\[
\Theta_q(x)=\int_0^x(1+s^2)^{q/2}\,ds.
\tag{3}
\]

For `0<q<1`, forward growth is `|x|^(1-q)` and the natural seed has growth
`|x|^(1+q)`.  At the elementary endpoint `q=1`,

\[
\phi_1(x)=\operatorname{arsinh}x,
\qquad
\Theta_1(x)=\frac12\left{x\sqrt{1+x^2}+\operatorname{arsinh}x\right}.
\tag{4}
\]

Moreover

\[
\frac{d_q'(x)}{d_q(x)}=-\frac{q x}{1+x^2},
\qquad
\left\|\frac{d_q'}{d_q}\right\|_\infty\le\frac q2.
\tag{5}
\]

The family interpolates between identity (`q=0`) and the critical
logarithmic activation (`q=1`).  Pure arctangent corresponds instead to the
faster derivative decay `(1+x^2)^(-1)`, i.e. the formal exponent `q=2`, and
has bounded output.

## 3. Tail-balance heuristic to be proved or falsified

If a preactivation and a weighted cotangent had sub-Gaussian tails, undoing
the derivative in (2) would multiply by approximately `|z|^q`.  The product
of a sub-Gaussian cotangent and `|z|^q` has the heuristic stretched-exponential
index

\[
\frac{2}{1+q}.
\tag{6}
\]

This is at least one precisely when `q<=1`; `q=1` is the exponential-tail
threshold used by an Osgood multiplier argument.  In the other direction,
the forward activation grows only as `|z|^(1-q)` (logarithmically at the
endpoint), which is strictly milder than the linear residual candidates.

This makes `arsinh` and the interior `0<q<1` family serious competitors to a
derivative-floor activation.  Equation (6) is only a static independent-tail
calculation.  The hard theorem concerns adaptively reused Gaussian actions,
and no activation may be selected from (6) without a reachable-trajectory
proof and hostile focusing audit.

## 4. Current provisional ranking criteria

| Candidate | Natural coordinate | Forward tail | Inverse derivative | Principal risk |
|---|---|---|---|---|
| leaky arctan | explicit, bi-Lipschitz | linear | bounded | no damping of adaptive cotangent focusing |
| normalized residual tanh | explicit, bi-Lipschitz | linear | bounded | same focusing risk; transcendental but tame maps |
| `phi_q`, `0<q<1` | pseudo-Lipschitz, usually hypergeometric | sublinear power | sublinear power | must prove an adaptive stretched-exponential invariant |
| `arsinh` (`q=1`) | explicit, quadratic growth | logarithmic | linear | critical `psi_1` endpoint; no slack in tail closure |
| arctangent control (`q=2` in derivative decay) | cubic natural coordinate | bounded | quadratic | known depth-three middle-adjoint tail gap |

No row in this table is yet a convergence theorem.

### A deterministic advantage of `arsinh` over every linear-tail residual

Let a family `z_n` satisfy `sup_n ||z_n||_2<=C` in normalized `L2`.
For every fixed `p<infinity`, logarithmic growth gives a constant `C_p` such
that

\[
|\operatorname{arsinh}x|^p\le C_p(1+x^2),
\]

and hence

\[
\sup_n\|\operatorname{arsinh}(z_n)\|_p<\infty.
\tag{6a}
\]

More sharply, if `R>0`, then on
`|arsinh(z)|>R` one has `|z|>sinh R`, so

\[
\begin{aligned}
\|\operatorname{arsinh}(z_n)
  \mathbf1_{\{|\operatorname{arsinh}(z_n)|>R\}}\|_2^2
&\le C^2
\sup_{|x|>\sinh R}
\frac{\operatorname{arsinh}(x)^2}{x^2}\\
&\le C^2\frac{R^2}{\sinh^2R}\longrightarrow0.
\end{aligned}
\tag{6b}
\]

Thus `arsinh` converts *every* bounded `L2` family into a square-uniformly
integrable family, without independence or a Gaussian-action hypothesis.
More generally, every strictly sublinear activation has the square-UI
property in (6b).  A linear-tail residual does not: applying it to
`sqrt(n)e_1` preserves an order-one square spike.

There is a stronger endpoint statement.  With the empirical Orlicz norm

\[
 \|x\|_{\psi_1,n}=\inf\{C>0:\langle e^{|x|/C}\rangle_n\le2\},
\]

the elementary inequality

\[
 e^{2|\operatorname{arsinh}z|}\le 4(1+z^2)
\tag{6c}
\]

and Jensen's inequality show that every normalized-`L2` ball is mapped by
`arsinh` into a bounded empirical `psi_1` ball.  The bound depends only on
the `L2` radius, not on width or on how the coordinates were generated.
No interior `0<q<1` has this all-moment consequence from `L2` alone: there
one obtains only `p(1-q)<=2`.

Consequently the MSE energy bounds would immediately regularize all forward
activation fields for `arsinh`, and the readout increment
`integral arsinh(Z_3) dt` inherits fixed higher moments (hence square UI) by
Jensen.  This is a proved selection advantage.  It does not regularize the
adaptive transpose field `G_2^*B_3`; that remains the decisive place where a
quenched Gaussian action can focus an otherwise uniformly integrable input.

The trained part of each adjoint is not the obstruction.  If
`P_2'=B_3 tensor X_2`, then

\[
 P_2(t)^*B_3(t)
 =\int_0^t X_2(s)\langle B_3(s),B_3(t)\rangle\,ds,
\tag{6d}
\]

up to the bounded physical residual factor.  Compact-time `L2` bounds make
the scalar contraction bounded, while (6c) and the Orlicz Minkowski
inequality control the time integral.  The same argument applies to
`P_1^*B_2` once `B_2` is controlled.  Thus the sharply reduced source terms
are the immutable actual-adjoint actions `Gamma_2^*B_3` and
`Gamma_1^*B_2`.

This reduction must not be overstated.  A bounded adaptive input can be
focused by an iid Gaussian matrix: choosing one row `I` and
`x_j=sign(G_{Ij})` produces `(Gx)_I` of order `sqrt(n)` while `x` is bounded.
Consequently Gaussian operator norm, exchangeability, and input `psi_1`
alone do not prove that an immutable adjoint preserves square tails.  A
successful theorem has to establish low influence/no row-or-column selection
for the *reachable gradient trajectory*.

### Conditional Osgood closure at the `psi_1` endpoint

Suppose the raw cotangent coefficients entering every nonlinear multiplier
have a compact-time empirical `psi_1` bound `B`.  Truncating a coefficient at
height `R` gives, for a bounded Lipschitz gate `d`,

\[
 \|a[d(z)-d(\widetilde z)]\|_2
 \le L_d R\|z-\widetilde z\|_2
   +2\|a\mathbf1_{|a|>R}\|_2.
\tag{6e}
\]

The `psi_1` tail makes the last term at most
`C_B(R+1)e^{-R/(2B)}`.  Optimizing at
`R asymp B log(1/E)` yields the rate-free Osgood modulus

\[
 \omega(E)\lesssim E\{1+\log_+(1/E)\},
 \qquad \int_{0^+}\frac{dE}{\omega(E)}=\infty.
\tag{6f}
\]

Therefore a uniform reachable `psi_1` lemma would supply uniqueness,
exact-versus-Euler stability, cutoff removal, and continuity of every
quadratic raw-kernel term without a quantitative width rate.  Equation (6f)
is a conditional theorem; proving the reachable immutable-adjoint tail lemma
is still the central missing step.

## 5. Two general selection theorems

### Bounded output and a derivative floor are incompatible in the real scalar smooth class

If `phi` is `C1` and `|phi'|>=a>0` on the real line, continuity prevents
`phi'` from changing sign.  The mean-value theorem then gives

\[
|\phi(x)-\phi(0)|\ge a|x|.
\tag{7}
\]

Thus every such activation is unbounded.  The tradeoff in the selection
problem is structural, not an artifact of the two named residual examples.

### Every genuine scalar smooth nonlinearity needs a canonical tail argument

Let `d=phi'` be nonconstant.  Choose `x0,x1` with `d(x0) != d(x1)`.  On a
normalized width-`n` population, take

\[
A_n=\sqrt n\,e_1,
\]

and let two preactivation fields agree except that their first coordinates
are `x0` and `x1`.  The input-state distance is

\[
\|z_n-\widetilde z_n\|_n=|x_1-x_0|/\sqrt n,
\]

whereas

\[
\|A_n\{d(z_n)-d(\widetilde z_n)\}\|_n
=|d(x_1)-d(x_0)|.
\tag{8}
\]

Hence the gradient map cannot have a width-independent local Lipschitz
constant on arbitrary normalized-`L2` balls.  For a `C1` scalar activation,
the only way to avoid (8) is constant derivative, hence an affine activation.

Equation (8) is a proof-route falsifier, not a canonical iid counterexample:
the selected theorem may still hold if its reachable Gaussian trajectories
obey a sufficiently strong delocalization/tail invariant.  It does prove
that changing among genuine smooth scalar nonlinearities cannot eliminate
the probabilistic convergence step altogether.
