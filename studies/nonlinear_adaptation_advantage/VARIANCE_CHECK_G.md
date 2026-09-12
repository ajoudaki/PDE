# Scoped internal check of the auxiliary variance counterexample

Date: 2026-09-12. Checker: `gaussian_sign_route`, after freezing its own
expected-sign candidate.

**Verdict: PASS for the stated auxiliary counterexample.** The scalar
invariant, complete projected tangent comparator, full-circle Gram and
whitening, global continuation, and uniform adverse risk bound (V5) are
correct. No correction is required for that claim. This is an internal
mathematical check, not an isolated promotion review and not an E₀ result.

The complete and only scientific input for this check was
`VARIANCE_ARGUMENT_CHECK.md`, SHA256

```text
40942327a54d47fef88a7d644590f7767c57c2ab5b94026af8069d4d03d00209
```

Its contents were read in full. Its explicit task family was sufficient;
the linked route, other reports, and further scientific sources were not
read. The input hash was checked again before writing and was unchanged.
Required skills and shared process instructions were followed. No experiment,
numerical integration, source alteration, or Git write was performed.

## 1. Scalar invariant, kernel, and global existence

For `r=a tanh w-q`, differentiation using the two stated Euclidean gradient
equations gives

\[
(a^2)'=-4ra\tanh w=(\sinh^2w)'.
\]

Thus `a²-sinh²w=I`, and `a` remains positive because `a²>=I>0`.
The **complete** scalar prediction kernel is the sum of both squared
parameter derivatives,

\[
K=\tanh^2w+a^2\operatorname{sech}^4w
 =1+(I-1)\operatorname{sech}^4w.
\]

This checks (V1), including the readout block. On every local existence
interval, `r'=-2Kr` integrates to (V2). In particular
`min(I,1)<=K<=max(I,1)`, so for `q!=0` and every positive local time,
`f=q(1-exp(-2 integral K))` has the sign of `q` and satisfies
`0<|f|<|q|`. Its sign is also that of `w` because `a>0`.

The continuation argument is noncircular. Put `u=sinh²w>=0`. On a maximal
local interval the preceding residual formula and invariant imply

\[
f^2=\frac{(I+u)u}{1+u}\ge\min(I,1)u,
\quad
u\le\frac{q^2}{\min(I,1)},
\quad
a^2\le I+\frac{q^2}{\min(I,1)}.
\]

These bounds hold before any proposed finite endpoint. They keep both
parameters in a fixed bounded set, where the smooth vector field is bounded
and locally Lipschitz. The solution has a limit at a proposed finite
endpoint and continues from it. Thus it exists for all finite times.
For `q=0`, uniqueness gives the stationary initial state directly.

For `q!=0`, `w(t)!=0` for all `t>0`. Therefore `I>1` gives `K(t)<I`
at every positive time, and the nonlinear residual square is strictly
larger than `q² exp(-4It)`. For `0<I<1` the strict comparison reverses.
For `I=1` the kernel is identically one and the two prediction flows
coincide. All three classifications in the input are correct.

## 2. Full-circle Gram and whitening

Using normalized circle measure and
`h²=(3-4cos(4alpha)+cos(8alpha))/8`, direct trigonometric integration gives

\[
\Gamma=\frac1{16}
\begin{pmatrix}
3&0&-2&0\\
0&3&0&2\\
-2&0&3&0\\
0&2&0&3
\end{pmatrix}.
\]

For example `cos(alpha)cos(3alpha)=(cos(2alpha)+cos(4alpha))/2`
gives `Gamma13=-1/8`, whereas
`sin(alpha)sin(3alpha)=(cos(2alpha)-cos(4alpha))/2` gives `Gamma24=1/8`.
The other off-diagonal integrals vanish by the displayed frequencies or
odd sine factors. Each of the two nontrivial two-by-two blocks has
eigenvalues `1/16` and `5/16`.

Because the positive square root is symmetric,
`psi=Gamma^(-1/2)phi` has identity Gram and
`c^Tphi=(Gamma^(1/2)c)^Tpsi`. Thus the stated `y=Gamma^(1/2)c` is the
correct coefficient vector. Every whitened feature still vanishes at the
anchors. No task outcome enters this transformation.

The numerical inequalities (V4) check exactly:

\[
\|y\|^2\ge\frac1{16}
 \left[2\left(\frac R{16}\right)^2
      +2\left(\frac R{48}\right)^2\right]
 =\frac{5R^2}{9216},
\]

and, since `|phi_i|<=1` and the original coefficients are positive,

\[
\|y\|=\|q-q_0\|_2\le\sum_i c_i
 \le2\frac R8+2\frac R{24}=\frac R3<1.
\]

The transformed coefficients `y_j` can have either sign or vanish. The
scalar proof permits both, so whitening introduces no missing restriction.

## 3. Complete anchor projection and comparator

For every state of the auxiliary ten-parameter model, the first anchor
prediction is exactly `z1` and the second exactly `z2`. All four `psi_j`
vanish there. Hence their two raw gradients are exactly the corresponding
coordinate vectors, their Gram is the identity, and the full orthogonal
projection drops exactly the `z1,z2` directions at every state.

Starting at the stated reference, the projected flow therefore keeps
`z1=1,z2=-1`. Its residual is
`sum_j (a_j tanh w_j-y_j)psi_j`. Orthonormality makes the projected squared
loss the sum of four scalar squared residuals. Its Euclidean projected
gradient flow is exactly the four copies of the scalar system with `I=2`.
No orthogonality between `q0` and the dictionary is required: the fixed
base predictions cancel exactly in this residual.

At the reference, the surviving raw derivatives are

\[
\partial_{a_j}f=0,\qquad \partial_{w_j}f=\sqrt2\,\psi_j.
\]

They give the full frozen kernel `2 sum_j psi_j(alpha)psi_j(beta)`.
Every raw direction is accounted for; the zero readout derivatives are a
property of this reference, not a readout-only comparator. Consequently
the frozen residual in component `j` is `-y_j exp(-4t)` and its squared
risk is `y_j² exp(-8t)`, with the same unhalved loss and time as the
nonlinear system.

## 4. Uniform finite adverse constant

For `I=2`, the invariant gives `u=sinh²w<=f²`, so along every component
`a²=2+u<=2+y_j²<=3`. Thus

\[
2-K=2\tanh^2w-\tanh^4w
 \ge\tanh^2w=\frac{f^2}{a^2}\ge\frac{f^2}{3}.
\]

Since `K>=1`, equation (V2) gives
`|f(t)|>=|y_j|(1-exp(-2t))`. Hence, writing
`D_j(T)=integral_0^T(2-K)dt`,

\[
D_j(T)\ge\frac{y_j^2}{3}J(T),\qquad
J(T)=T-(1-e^{-2T})+\frac{1-e^{-4T}}4>0\quad(T>0).
\]

The expression for `J` is the integral of the stated strictly positive
integrand away from zero. The exact adverse component gap is

\[
y_j^2e^{-8T}\{e^{4D_j(T)}-1\}
 \ge\frac43 y_j^4e^{-8T}J(T).
\]

This also holds when `y_j=0`. Cauchy–Schwarz on the four nonnegative
numbers `y_j²` gives `sum y_j⁴>=||y||⁴/4`. Therefore the summed gap is
at least

\[
\frac13\left(\frac{5R^2}{9216}\right)^2e^{-8T}J(T)
 =\frac{25R^4}{254803968}e^{-8T}J(T)>0,
\]

because `3*9216²=254803968`. This checks both the direction and the exact
constant of (V5). The bound is uniform on the entire stated four-coefficient
box for each fixed `R>0,T>0`. Integrating a uniform pointwise adverse bound
against any probability distribution on that box preserves the same bound;
no independence assumption on that averaging distribution is needed.

## 5. Scope of the passing verdict

The input correctly distinguishes this finite-dimensional auxiliary
prediction map and its explicitly chosen reference from the actual E₀
Gaussian two-hidden network and its reached reference. Its full-circle
example uses only the explicitly supplied uniform-density, zero-target-tail
slice. No density/target robustness extension, actual E₀ adverse sign,
relative-component advantage, sampling claim, or finite-Gaussian transfer
is established or needed for this auxiliary inference counterexample.

The check supports precisely this conclusion: readout linearity, nonlinear
tanh feature training, exact anchor constraints, and varying active task
components alone do not force favorable task-averaged risk relative to the
complete frozen tangent comparator. Additional actual-reference structure
is necessary to deduce such a sign for E₀.

Pre-write metadata: HEAD
`fbe203c51ebd62805b0fdd9ec3824d6d8aac7859`, staged index empty. The only
written path was this report. The verification method was direct analytic
reconstruction of every displayed identity and bound; no computation or
experiment supplied scientific evidence.
