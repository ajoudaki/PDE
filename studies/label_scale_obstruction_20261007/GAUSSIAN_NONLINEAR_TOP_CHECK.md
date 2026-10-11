# Internal audit of the Gaussian nonlinear-top fitting proof

2026-10-10. This is a reused-context internal mathematical audit, **not an
independent promotion review**. The complete frozen scientific input was
`GAUSSIAN_NONLINEAR_TOP_POSITIVE.md`, SHA256

```text
36258656917ec2ead5a86a9e163e522ec0a39a56772d806e026ae9aa1fe0718f
```

The hash was verified before reading and again after completing the audit;
the frozen input remained unchanged. No other scientific source was read
during this audit; the relevant required skills had already been read and
were reused. No experiment or numerical simulation was run. The proof was
not edited.

## Verdict

**PASS for the stated linear-first-layer, nonlinear-top theorem.** I found
no substantive mathematical error in the frozen argument. In particular,
the Gaussian probability event, simultaneous-all-labels conclusion, exact
zero-readout initialization, finite-width infinite-time fitting, parameter
convergence, and deterministic width-independent decay constants all follow
from the displayed estimates.

One minor precision improvement is recommended: explicitly define the main
all-label initialization event as the geometry event (9) intersected with
\(\{\operatorname{rank}H(0)=m\}\). The latter event has probability one,
as the proof establishes, so this changes neither the theorem nor the
probability bound. It merely makes clear which null set is removed when the
initial strict loss decrease is used for every nonzero label direction.
The stronger rate event (20) already imposes full rank quantitatively.

The theorem does not establish tanh/tanh fitting. The linear first activation
and the strictly positive top derivative floor are essential assumptions in
the supplied proof, and its stated scope accurately discloses them.

## Exact dynamics, existence, and protected geometry

The forward pass is \(U=AX\), \(Z=WU\), \(H=\phi(Z)\),
\(f=H^\top w/n\), with loss \(\|f-y\|^2/m\). Differentiation gives all
three updates in (4), including the factors arising from mobilities
\((n,1,n)\). Thus the mobility norm and energy identity (5) are correct.

Because \(w(0)=0\), initial loss is \(Y^2=\|y\|^2/m\). The integrated
energy bound gives (6) for any two times in the local existence interval.
At a finite hypothetical maximal time, this uniform one-half-Hölder bound
makes all finite-dimensional parameter coordinates Cauchy. The vector field
is smooth at their finite limit, so ordinary local existence extends the
solution. This proves global finite-time existence without assuming bounded
activation values or bounded parameters for infinite time.

Writing \(\dot A=W^\top F\) and \(\dot W=FA^\top/n\), the derivatives
of \(W^\top W\) and \(AA^\top/n\) agree term by term. The matrix invariant
(7) is therefore exact for any admitted top activation. If \(C_0\) is at
most \(-\kappa I\) on a fixed \(d\)-dimensional subspace, the square
matrix \(A^\top P/\sqrt n\) has smallest singular value at least
\(\sqrt\kappa\). Consequently (8) follows by positive-semidefinite
ordering. There is no hidden assumption that this subspace is invariant
under the evolving weights.

## Gaussian probability certificate

Conditional on \(A(0)\), rotate its column space to the first \(d\)
coordinate directions. Right orthogonal invariance of the Gaussian matrix
\(W(0)\) gives independent Gaussian blocks \(B_0\) and \(E_0\) of the
stated shapes and variance. The nonzero eigenvalues of
\(A(0)A(0)^\top/n\) are those of \(A(0)^\top A(0)/n\), so the displayed
Frobenius moment controls the required deviation of \(D_0\) as well.

I independently checked the less immediate fourth-moment calculation. Put
\(k=n-d\) and \(T=E_0E_0^\top\). Conditional on \(T\), Gaussian quadratic
forms in the independent columns of \(B_0\) give

\[
 \mathbb E\|B_0^\top TB_0-I_d\|_F^2
 =\frac{d(d+1)}{n^2}\mathbb E\operatorname{tr}(T^2)
   +d\,\mathbb E(\operatorname{tr}(T)/n-1)^2.
\]

The elementary Gaussian moments are

\[
 \mathbb E\operatorname{tr}(T^2)=\frac{k(n+k+1)}n,
 \quad \mathbb E\operatorname{tr}(T)=k,
 \quad \operatorname{Var}(\operatorname{tr}T)=\frac{2k}n.
\]

Substitution reproduces exactly the formula for
\(\mathbb E\|S_0-I_d\|_F^2\) in the proof. Its upper bound
\(4(d^2+d)/n\) is valid for \(n\ge d+1\).

The two covariance failures at tolerance \(1/512\) contribute
\(2\cdot512^2(d^2+d)/n\). The \(S_0\) failure at tolerance \(1/2\)
contributes at most \(16(d^2+d)/n\). Their sum is precisely
\(524304(d^2+d)/n\). These events imply
\(\|B_0^\top B_0-D_0\|\le1/256\) and
\(I_d/2\preceq S_0\preceq3I_d/2\preceq2I_d\).

The two one-quarter nets have cardinalities at most \(9^n\) and \(9^{n-d}\).
The approximation of both arguments loses at most half the operator norm,
so threshold four for a net pairing gives operator bound eight. Since each
pairing is \(N(0,1/n)\), the stated exponential term in (1) is correct.
Independence of these failure events is not needed; the union bound suffices.

For the graph vector \(v=(u,-E_0^\top B_0u/64)\), the quadratic expansion
is correct. The inequality \(T^2\preceq64T\) reduces the last two terms to
at most \(-S_0/64\), and hence

\[
 v^\top C_0v\le-\|u\|^2/256,
 \qquad \|v\|^2\le(1+2/4096)\|u\|^2<2\|u\|^2.
\]

The resulting \(d\)-dimensional negative subspace has Rayleigh quotient at
most \(-1/512\). The dimension-intersection argument with a spectral
decomposition then gives (10) and persistent input geometry (8).

For some small widths event (9) may be empty; for example, \(S_0\) cannot
have rank \(d\) when \(n-d<d\). This is not a contradiction: the displayed
probability lower bound is then negative and explicitly identified as
uninformative. For fixed \(d\), the probability tends to one.

## Scalar balance, readout growth, and the logarithmic bound

The trace identity (11) is correct. Direct differentiation gives the same
summation indices in \(Z\phi'(Z)\) and \(\phi(Z)\), leaving exactly
the defect \(\psi=\phi-z\phi'\). The Cauchy--Schwarz factors in (12) reduce
to \(4M_\phi q\rho\), with no missing factor of \(m\) or \(n\).

The proof correctly avoids the analogous matrix identity, which would mix
different neuron derivatives. It uses only the valid scalar trace identity
and the separate first-layer matrix invariant.

Equations (13) follow by bounding operator norm through normalized
Frobenius norm and adding \(\|C_0\|_{\mathrm{op}}\). The sharper product
bound before (14) uses
\(\sqrt{x(x+c)}\le x+c/2\) for \(x,c\ge0\). The constant \(R_0\)
contains every additive term needed for (14), including \(|\phi(0)|/L_\phi\).
Thus allowing nonzero \(\phi(0)\) causes no gap.

The middle-layer tangent block has the stated normalization. The protected
geometry gives \(U^\top U/n\succeq\kappa X^\top X\), and each diagonal
activation-derivative matrix has every singular value at least \(c_\phi\).
Summing the resulting quadratic-form inequalities gives exactly (15), and
the conversion from loss to residual norm yields the factor
\(b=2\kappa\lambda_Xc_\phi^2/m\) in (16).

Almost-sure full rank of \(H(0)\) is valid: \(A(0)X\) has full column
rank, conditional top preactivations have nondegenerate Gaussian densities,
and the coordinatewise activation is a smooth increasing bijection. Its
transformed density is positive everywhere. Independent rows from such a
density give rank \(m\) almost surely for \(n\ge m\).

At any such initialization, every nonzero label direction satisfies
\(\dot{\mathcal L}(0)<0\). The strict decrease provides a positive
trajectory-dependent \(\delta\); subsequent loss monotonicity then makes
\(\|f(t)\|\ge\sqrt m\,\delta\) permanent. This is the correct use of
zero-readout initialization: positivity of \(q\) is derived, not assumed.

For \(q\le1\), (14) gives the lower bound (17), because

\[
 q^2+R_0+4M_\phi S
 \le(1+R_0+4M_\phi)(1+S).
\]

For \(q>1\), the chosen \(c_0\le1\) makes the same bound immediate. Thus
\(q>0\) after \(t_0\). On any remaining interval of positive residual,
\(S'=q\rho>0\), justifying the division in the proof. Integration of
\(d\rho/dS\le-bc_0/(1+S)\) gives (18), then a positive permanent lower
bound for \(q\), then (19). The zero-residual case is handled separately.
There is no circular assumption of bounded \(S\), bounded parameters, or
already-small labels.

## Quantifiers and finite parameter limits

After intersecting the two initialization events noted above, all subsequent
arguments are deterministic and apply to an arbitrary label vector. Hence
the conclusion holds for every finite \(y\) on the same event; no uncountable
probability union is being used. The choices \(t_0,\delta,c_0\) and the
rate may depend on the selected labels. For \(y=0\), every parameter
velocity is zero at initialization, as stated.

Equation (19) is proved for each fixed finite width and controls all later
physical times. Therefore the argument establishes actual finite-width
zero limiting loss before using the probability estimate; it does not merely
show convergence to arbitrarily small fixed tolerances in a width-first
limit.

The readout identity and \(\|f\|\le2\|y\|\) give
\(|(q^2)'|\le8Y\rho\), exactly as stated. Exponential residual decay makes
this integrable and bounds \(q\). The scalar balance bounds \(a\), and the
matrix invariant then bounds \(\|W\|_{\mathrm{op}}\). Substituting these
bounds and \(D\le L_\phi\) in (4) bounds each scaled parameter speed by a
constant times \(\rho\). Their integrals are finite, proving convergence
to finite parameter arrays. The constants need only be finite at the fixed
width in this part of the proof.

## Deterministic width-independent rates

The population initial feature covariance \(G_*\) is finite by linear
growth and is positive definite by the full support argument. Here full
support is used only to identify a fixed positive population eigenvalue;
the all-time fitting proof is supplied by the separate invariant and
logarithmic bound.

The probability argument for (20) checks out. Conditional covariance
\(\Sigma_n\) converges to \(X^\top X\). On a bounded covariance
neighborhood, Gaussian fourth moments and linear activation growth give a
uniform conditional variance bound for the empirical Gram. Continuity of
the Gaussian covariance square root and the integrable domination
\(C(1+\|g\|^2)\) identify the limiting expectation. The operator norm
bound \(w_*=8\) follows from the same two-net argument; choose any fixed
\(a_*\) strictly larger than \(\sqrt d\).

The decomposition used for (21), together with (6), yields exactly

\[
 \|H(t)-H(0)\|_F/\sqrt n
 \le L_\phi\sqrt m\,Y\sqrt t\,(a_*+w_*+Y\sqrt t).
\]

A fixed positive \(t_*\) satisfying the required bound therefore exists
for any fixed finite \(Y>0\). Singular-value perturbation gives the initial
kernel bound, and the residual decay exponent in (22) is correct. The
integral \(\int_0^{t_*}Y^2\sqrt t\,dt\) gives the stated \(S_*\).

The bounds on \(R_0\), \(c_*\), \(\overline S\), and \(\overline q\)
all have the correct monotonic directions. Substituting them into (19) and
squaring produces exactly (23). Every chosen constant depends on fixed
data, activation, and labels, but not on width. The required combined event
has probability tending to one. Extremely small rates for large labels
are a quantitative weakness, not a loss of positivity or an interchange of
limits.

## Explicit analytic activations

For \(\phi(z)=z+\varepsilon\arctan z\), the real derivative lies in
\([1,1+\varepsilon]\). Differentiating the defect yields
\(2\varepsilon z^2/(1+z^2)^2\), so oddness, monotonicity on the positive
half-line, and its limit \(\varepsilon\pi/2\) prove the stated global
defect bound.

For the strip assertion, interpret the permitted closed strips as
\(|\operatorname{Im}z|\le h<1\). The derivative
\(1+\varepsilon/(1+z^2)\) is holomorphic and bounded there, with poles
outside at \(\pm i\). It has a holomorphic primitive on the open strip,
fixed to agree with the real arctangent. Every higher derivative is a
rational function with poles only at \(\pm i\), bounded on each smaller
closed strip. The activation values themselves remain unbounded, as the
proof expressly states.

For \(z+\varepsilon\tanh z\), the derivative floor and upper bound hold
on the real axis. The stated derivative of the defect is nonnegative for
positive real \(z\), and its limit is \(\varepsilon\), proving the bound.
Tanh and each of its derivatives are bounded on closed strips
\(|\operatorname{Im}z|\le h<\pi/2\); adding the linear term preserves
boundedness of every positive-order derivative. Thus both examples meet
the stated real-axis and strip-analytic requirements. No claim of bounded
activation values is needed or valid for these examples.

## Required correction and remaining scope

No substantive correction is required for the theorem. The sole recommended
precision edit is to name the probability-one rank condition in the main
event. This audit does not establish novelty, approval for promotion, a
tanh/tanh result, fitting for linearly dependent inputs, or a compression
result. None of those claims is made by the audited proof.
