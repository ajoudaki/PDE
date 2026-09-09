# Campaign 4: two independent parameter-block metrics

## Frozen mathematical object

The network, initialization, one-sample feature-ascent objective, and MFP
normalization are exactly those of the accepted canonical quadratic model.
Only the parameter-space metric is varied.  Write

$$
D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W,
\qquad \alpha,\beta\ge0,
$$

where $D_a$ differentiates readout weights, $D_u$ differentiates the first
hidden preactivations, and $D_W$ differentiates the middle weights.  The
previous Campaign-1 ray is the diagonal

$$
\alpha=\beta=\lambda.
$$

For total derivative order $k$, let $C_{k,w,a}$ be the exact MFP sector with
exactly $w$ middle-weight hits and $a$ readout hits.  The remaining
$k-w-a$ hits are first-hidden hits.  The full feature jet is therefore

$$
F_{\alpha,\beta}^{(k)}(0)
=
\sum_{w=0}^{k}\sum_{a=0}^{k-w}
C_{k,w,a}\,\alpha^{k-w-a}\beta^w.
$$

This is a genuine two-parameter family: no summation over sectors with the
same diagonal $\lambda$-degree is performed before the exact coefficients
are preserved.

## Primary mathematical decision

From the exact odd jets through order nine, formal inversion gives

$$
K_{\alpha,\beta}(y)
=F_{\alpha,\beta}'\!\left(F_{\alpha,\beta}^{-1}(y)\right)
=K(0)+\mu_0y^2-\mu_1y^4+\mu_2y^6-\mu_3y^8+O(y^{10}).
$$

The primary decision object is the first shifted Hankel determinant

$$
\Delta_1^+(\alpha,\beta)
=\mu_1\mu_3-\mu_2^2.
$$

The campaign asks whether

$$
\Delta_1^+(\alpha,\beta)\ge0
\qquad\text{for every }\alpha,\beta\ge0.
$$

A negative exact rational point is a rigorous counterexample for this
two-block-metric extension.  A floating grid is never a positivity
certificate.  A positive conclusion requires an exact coefficientwise,
factorization, Bernstein-subdivision, or exact semialgebraic certificate.

## Frozen validation gates

No order-nine sign result is accepted unless all gates below pass.

1. Every completed sector is written as an atomic standalone JSON artifact
   before the next sector begins.  A timeout may leave an incomplete
   campaign, but it may not erase completed exact sectors.
2. Checked 512-bit unsigned arithmetic is used.  Overflow throws rather than
   wrapping.
3. For every odd order $k=1,3,5,7,9$, diagonal substitution

   $$\alpha=\beta=\lambda$$

   reproduces every coefficient of the frozen Campaign-1 $\lambda$-jet.
4. At $(\alpha,\beta)=(1,1)$ the accepted canonical derivatives are

   $$
   111,
   \quad1\,685\,184,
   \quad77\,400\,633\,120,
   \quad7\,315\,868\,433\,079\,296,
   \quad1\,181\,161\,141\,825\,400\,561\,664.
   $$
5. A transparent whole-forest implementation, with a terminal Wick route
   independent of the connected sector recursion, agrees with the bivariate
   coefficients through at least order five.
6. At least one off-diagonal positive metric point, preselected as

   $$(\alpha,\beta)=(2,3),$$

   agrees exactly between the independent low-order route and the sector
   route.
7. Feature parity holds coefficientwise: every even output jet through order
   eight is zero.
8. Source, parent-source, runner, postprocessor, binary, frozen diagonal
   input, sector manifest, result, and certificate identities are recorded
   by SHA-256.  Tests required in a clean checkout may not depend on an
   ignored local binary.

## Frozen resource boundary

- Object: output feature jet only.
- Orders: odd orders $1,3,5,7,9$; even orders are exact parity zeros.
- Per-sector virtual-memory cap: 4 GiB.
- Cumulative production wall-clock cap after validation: 30 minutes.
- Sector execution is sequential for the primary run, so the per-sector
  memory bound is also the production-process memory bound.
- A timeout or memory failure is classified as inconclusive.  All completed
  atomic sectors remain partial exact facts but do not certify the missing
  full jet.
- Stop after $F^{(9)}(0)$.  Do not compute $Q_2$, $F^{(11)}$, or any other
  observable or derivative order in this campaign.

## Claim boundary

Passing Campaign 4 proves only the displayed finite-order formal-jet
inequality for the stated two-parameter metric family.  It is not an
all-order Stieltjes proof, and identifying the formal kernel with a global
mean-field trajectory remains a separate obligation.
