# Gaussian score representation of the reciprocal contractions

2026-10-07. Scoped internal identity check. Scientific inputs were exactly
`CANDIDATE_SYSTEM.md`, `causal_filtered_integrator.py`,
`causal_panel_simulator.py`, and `causal_population_simulator.py`.
No scientific training runs, other-study material, or global approximation
arguments were used. This is a representation of the existing finite causal
system. Its implementation is **not selected** for the current numerical audit.

The two reciprocal contractions can be recovered exactly from Gaussian score
moments at population level, including singular histories. Individual formal
response coefficients cannot in general be recovered. Replacing tangent
averages by empirical score averages introduces a different quadrature error;
when retained rank is comparable to population size, that error can be order
one in the contracted field.

## 1. Exact contraction identity

Fix a finite time index \(k\), training size \(m\), and panel size \(p\ge m\).
The fields and formal derivatives have the meanings in equations (1)--(5) of
`CANDIDATE_SYSTEM.md`: \(h_{1,a}^k=\phi_1(z_{1,a}^k)\) and
\(\delta_{2,a}^k=w^k\phi_2'(z_{2,a}^k)\). A formal derivative freezes all
population coefficients and differentiates the local scalar circuit.
For the filtered integrator it freezes `write_deficit`, the effective force
\(\widetilde c^j\), as well as \(C,D,R\) and the primitive covariances.
It does not differentiate the residual filter or any population average.

Flatten a history by time first and sample second. Write
\(\boldsymbol\xi_{<k}=(\xi_b^j)_{j<k,b\le p}\) and
\(\boldsymbol\delta_{2,<k}=(\delta_{2,b}^j)_{j<k,b\le p}\).
Likewise, \(\boldsymbol\eta_{\le k}\) and
\(\boldsymbol h_{1,\le k}\) include every time through \(k\).
Define the deterministic matrices

\[
\begin{aligned}
 Q_D&=\mathbb E_{\rm upper}
       [\boldsymbol\delta_{2,<k}\boldsymbol\delta_{2,<k}^\top]
     =\mathbb E_{\rm lower}
       [\boldsymbol\xi_{<k}\boldsymbol\xi_{<k}^\top],\\
 Q_C&=\mathbb E_{\rm lower}
       [\boldsymbol h_{1,\le k}\boldsymbol h_{1,\le k}^\top]
     =\mathbb E_{\rm upper}
       [\boldsymbol\eta_{\le k}\boldsymbol\eta_{\le k}^\top],\\
 B_h&=\mathbb E_{\rm lower}
       [h_1^k\boldsymbol\xi_{<k}^\top],\qquad
 B_\delta=\mathbb E_{\rm upper}
       [\delta_2^k\boldsymbol\eta_{\le k}^\top].
\end{aligned}
\tag{1}
\]

Here \(h_1^k,\delta_2^k\in\mathbb R^p\) are panel vectors within their
respective populations. Let \(R_h\in\mathbb R^{p\times kp}\) and
\(R_\delta\in\mathbb R^{p\times(k+1)p}\) be the corresponding flattened
formal response arrays. Then

\[
 B_h=R_hQ_D,\qquad B_\delta=R_\delta Q_C,
\tag{2}
\]

and, with \(Q^+\) denoting the Moore--Penrose inverse,

\[
\begin{aligned}
 R_h\boldsymbol\delta_{2,<k}
   &=B_hQ_D^+\boldsymbol\delta_{2,<k}
       &&\text{almost surely in the upper population},\\
 R_\delta\boldsymbol h_{1,\le k}
   &=B_\delta Q_C^+\boldsymbol h_{1,\le k}
       &&\text{almost surely in the lower population}.
\end{aligned}
\tag{3}
\]

Every expectation in (1) pairs fields from one population. Equation (3)
transfers deterministic coefficients to the other population; it never pairs
arbitrarily numbered lower and upper neurons. The matrices \(Q_D,Q_C\) are
**uncentered** field Grams. Replacing them by centered field covariances would
change both the primitive law and the range argument below.

For completeness, consider a centered Gaussian column \(G\) with covariance
\(Q=LL^\top\), where \(L\) has full column rank \(r\), and write \(G=LZ\)
with \(Z\sim N(0,I_r)\). Let \(F(U,G)\) be a differentiable vector function;
the auxiliary root \(U\) is independent of \(Z\). Assume the function and its
first derivatives have polynomial growth, or integrable bounds sufficient
for the following integration by parts. Conditioning on \(U\), integration
against the standard Gaussian density gives

\[
\mathbb E[F(U,LZ)Z^\top]
 =\mathbb E[D_GF(U,G)]L.
\tag{4}
\]

Indeed, in each scalar coordinate the density satisfies
\(\partial_z e^{-z^2/2}=-ze^{-z^2/2}\); integration by parts has zero
boundary term under polynomial growth. Multiplying (4) by \(L^\top\)
proves \(\mathbb E[FG^\top]=RQ\), where
\(R=\mathbb E[D_GF]\). For any other random vector \(X\) with
\(\mathbb E[XX^\top]=Q\), each \(v\in\ker Q\) satisfies
\(\mathbb E[(v^\top X)^2]=v^\top Qv=0\).
A finite orthonormal basis of the kernel therefore gives
\(X\in\operatorname{range}Q\) almost surely. Consequently
\(RQ Q^+X=RX\), proving (3). Independence of \(X\) from \(G\) is not needed
for this algebra, but the actual causal system uses distinct populations.

The source activation assumptions are enough at a fixed finite program with
finite deterministic coefficients: bounded first and second derivatives and
at most linear activation growth make the local fields and first tangents
polynomially bounded in the Gaussian roots, by induction through the finite
linear-combination and multiplication rules. Thus the integration-by-parts
and moment assumptions used here hold. This is a finite-program statement.

At rank zero \(Q^+=0\) and \(X=0\) almost surely, so no division by a zero
variance is needed. This includes the initially zero \(\delta_2^0\).

## 2. Formal responses, current time, and passive inputs

Equation (2) determines \(RQ Q^+\), not \(R\) on the covariance kernel.
For example, let \(G=(Z,Z)^\top\), \(F(G)=G_1\), and \(X=(Y,Y)^\top\),
with \(Z,Y\) standard Gaussian. The formal derivative is \(R=(1,0)\),
whereas \(\mathbb E[FG^\top]Q^+=(1/2,1/2)\). Both contract with \(X\)
to give \(Y\). If the second coordinate represented an unused passive probe,
zeroing that column after taking the full pseudoinverse would incorrectly
halve the result. A projected coefficient array must not be reported or
tested as the canonical formal \(R\) array.

For the forward contraction, all lower features depend only on active
strict-past formal \(\xi\) coordinates. Therefore (1)--(3) can simply be
restricted to \(j<k,b\le m\), retaining all \(p\) evaluated outputs.

The backward contraction has a useful exact split that preserves the
current-time curvature and works for active and passive evaluated inputs.
Let

\[
 E=(\eta_b^j)_{j<k,b\le m},\qquad
 H=(h_{1,b}^j)_{j<k,b\le m},\qquad
 Q=\mathbb E_{\rm upper}[EE^\top]
  =\mathbb E_{\rm lower}[HH^\top],
\]

and, for each \(a\le p\), define

\[
 t_a=\mathbb E_{\rm lower}[Hh_{1,a}^k]
     =\mathbb E_{\rm upper}[E\eta_a^k],\qquad
 \kappa_a=\mathbb E_{\rm upper}[w^k\phi_2''(z_{2,a}^k)].
\tag{5}
\]

With all coefficients frozen, \(w^k\) and
\(z_{2,a}^k-\eta_a^k\) are functions of \(E\) alone. The only current
formal primitive entering \(\delta_{2,a}^k\) is \(\eta_a^k\), and its
mean derivative is \(\kappa_a\). Gaussian integration by parts in the
joint vector \((E,\eta_a^k)\) therefore gives

\[
 \mathbb E_{\rm upper}[\delta_{2,a}^kE^\top]
 =R_{\delta,a,\mathrm{past}}Q+\kappa_a t_a^\top,
\tag{6}
\]

where \(R_{\delta,a,\mathrm{past}}\) differentiates the active past while
holding the current formal primitive fixed. Since \(H\in\operatorname{range}Q\),
the **complete** backward reciprocal term for output \(a\) is

\[
 \kappa_a h_{1,a}^k+
 \left\{\mathbb E_{\rm upper}[\delta_{2,a}^kE^\top]
                  -\kappa_a t_a^\top\right\}Q^+H.
\tag{7}
\]

The subtraction in braces is necessary: current and past Gaussian
coordinates are correlated. Treating current time as independent fresh
noise would omit it. At \(k=0\) the past is empty; \(\kappa_a=0\) because
\(w^0=0\). For a passive \(a\), (7) retains its own current curvature term
and its response to active past coordinates. No passive label or passive
training write is introduced. Past passive formal probes have zero response.

The formal derivative also differs from differentiating a conditional
Gaussian parametrization. If
\(\eta_a^k=t_a^\top Q^+E+\zeta_a\), with \(\zeta_a\) independent of
\(E\), then differentiating at fixed \(\zeta_a\) adds
\(\kappa_a t_a^\top Q^+\) to the mean past derivative. That derivative
cannot be substituted for \(R_{\delta,a,\mathrm{past}}\) in (6).

## 3. Factor form and correspondence with the sampler

The inverse in (3) is unnecessary when a compatible factor is already
available. For \(Q=LL^\top\), set \(X=LV\), where
\(V=L^+X\) satisfies \(\mathbb E[VV^\top]=I_r\). Equation (4) gives

\[
 RX=\mathbb E[FZ^\top]V.
\tag{8}
\]

This uses one score moment per retained independent Gaussian direction.
For (7), a factor of the active-past \(Q\) gives \(E=LZ,H=LV\) and
\(b_a=L^+t_a\). Its past contribution is
\(\{\mathbb E[\delta_{2,a}^kZ^\top]-\kappa_a b_a^\top\}V\).

In `_ColoredGaussianFamily`, with exact arithmetic and no discarded
nonzero innovations, the source history matrix equals
`basis @ coefficients.T` and the primitive history matrix equals
`seeds @ coefficients.T`. Columns of `basis` have empirical squared norm
\(N\), and `basis.T @ basis / N` is the identity. Thus an empirical version
of (8), with `current_field` of shape `[N,p]`, would be

```python
score = current_field.T @ target_seeds / N
correction = source_basis @ score.T
```

For the forward term the source basis belongs to upper
\(\delta_2\) history and the score pairs lower \(h_1\) with lower
\(\xi\) seeds; only already introduced strict-past seeds are used.
For the backward term the source basis belongs to lower \(h_1\) history
and the score pairs upper \(\delta_2\) with upper \(\eta\) seeds.
The full-history backward factor includes current time. Formula (7) is an
alternative when retaining the known current curvature explicitly.

This code-shaped formula describes an estimator, not an equality with the
current simulator's finite-\(N\) tangent contraction. Dropping a nonzero
innovation also changes the represented covariance: the raw source history
need not lie in the retained factor's range. A small Gram reconstruction
error alone does not bound the response contraction error without control
of the response in the discarded directions.

## 4. Finite quadrature risk and diagnostic meaning

The growth with rank can be seen without a training example. Suppose one
scalar \(F\) is independent of a standard Gaussian score vector
\(Z\in\mathbb R^r\), so its exact score moment is zero. For \(N\)
independent rows, set
\(\widehat b=N^{-1}\sum_i F_iZ_i\). Then

\[
 \mathbb E\|\widehat b\|^2
   =\frac{r}{N}\mathbb E[F^2].
\tag{9}
\]

Indeed the terms with different row indices vanish, and each diagonal term
has mean \(\mathbb E[F^2]\mathbb E\|Z\|^2=r\mathbb E[F^2]\).
For any empirical source basis satisfying \(V^\top V/N=I_r\), the
correction has sample mean square
\(\|V\widehat b\|^2/N=\|\widehat b\|^2\) identically. Thus even an
exactly zero population response can acquire order-one field noise when
\(r/N\) is order one. The example establishes the danger, not a universal
error formula for the nonlinear adaptive simulator.

The existing simulator estimates coefficients from the same ensembles that
produce subsequent fields and Gaussian factors. Those coefficients and
factors are random functions of reused rows. Ordinary independent-row
unbiasedness and standard errors cannot be asserted for the resulting score
estimator merely by freezing coefficients in the formal derivative. A
small residual of a fitted moment identity using the same data is also
insufficient evidence against overfitting. Factorization avoids explicit
division by tiny covariance eigenvalues, but it does not remove score noise
or the accumulating number of estimated directions.

Before selecting such an implementation, useful checks would include
independently resampled frozen-circuit comparisons, contraction comparisons
with tangent averages rather than canonical-response coefficient equality,
rank-to-population ratios, independent-seed variability, sensitivity to
discarded innovations, current-time identity checks, and passive-role
checks. These checks have not been run in this scoped identity task.

The selected fresh frozen-coefficient audit has a sound narrower meaning.
Fix saved \(C,D,R,\widetilde c\) and primitive covariances externally;
draw independent first-layer roots, upper \(\eta\), and lower \(\xi\)
families with all prescribed within-family time correlations; then evaluate
the frozen local circuit. Rows are independent samples of that fixed
circuit. Comparing its newly estimated moments with the saved coefficients
tests their self-consistency. It does not construct a corrected autonomous
trajectory or resolve time-discretization error. The audit should identify
whether the primitive covariance target is the saved raw field Gram or the
original sampler's retained-factor Gram, because discarded innovations can
make them different. The effective filtered force remains frozen throughout.

The exact identity supports the representation. The current numerical
choice is to retain tangent responses and use fresh frozen-circuit sampling
as a diagnostic; no score-based causal solver is proposed here.
