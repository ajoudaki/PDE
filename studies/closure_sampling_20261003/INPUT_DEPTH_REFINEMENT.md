# Removing depth from the logarithmic storage exponent

2026-10-04. **Internally checked continuation** of this study's autonomous
neuron-compression investigation. The complete new source proof and its
separate reconstruction, the runtime assembly check, the source lower
bound and its check, and the training-span derivation were read completely
by the coordinator. No manuscript or maintained-book claim is made here.

The user keeps the label condition Y<=c gamma/m and asks to reduce the
input-dimension and depth powers in the logarithmic storage bound. The
gap-only label corollary is not used. The reference is the same realized
canonical dense width-n network, not a population limit. All fixed and
moving retained coordinates count, and the error norm remains the supremum
over the whole input sphere and all physical training time, including the
fitted endpoint.

## 1. Stronger storage theorem under the same assumptions

Fix d>=2, hidden depth L>=2, and m normalized training vectors
v_a=x_a/sqrt(d) on S^(d-1). Every original hidden layer has width n.
With real bounded-strip-holomorphic activations phi_l, the forward pass is

\[
 z^{(1)}(v)=Av,\qquad
 z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v)\quad(\ell\ge2),\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n(v)=w^\top h^{(L)}(v)/n.
\]

The entries of A_0 are independent N(0,1), those of each W_0 are
independent N(0,1/n), all initialized blocks are independent, and w_0=0.
Writing r_a=f_n(v_a)-y_a, the exact backward responses are
k_a^(L)=w, delta_a^(l)=phi_l'(z_a^(l)) multiplied coordinatewise by
k_a^(l), and k_a^(l)=W^(l+1) transpose times delta_a^(l+1).
Physical gradient flow is

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
 \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
 \tag{1}
\]

Define Q^(0)_{ab}=v_a^T v_b and
Q^(l)_{ab}=E[phi_l(Z_a)phi_l(Z_b)] for Z~N(0,Q^(l-1)). Set

\[
 \gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
 \lambda=\min(1,\gamma/m),\qquad
 Y=\|y\|_2/\sqrt m,\qquad \ell_n=\log(en).
\]

Retain 0<Y<=c lambda. For tanh this is exactly the requested
Y<=c gamma/m. The zero-label case is separately stationary.
Structural constants may depend on fixed d,L and the activation strip
and bound, but not on m,gamma,Y,n or elapsed time unless displayed.

The improved sufficient retained size is

\[
 \operatorname{size}\le
 C\lambda^{-2}\ell_n^{3d+2}+Cm(d+1).
 \tag{2}
\]

More explicitly, before absorbing logarithmic gap dependence into the
eventual width threshold, it is

\[
 C\lambda^{-2}\ell_n^{d+2}
       [\ell_n+\log(e/\lambda)]^{2d}+Cm(d+1).
 \tag{3}
\]

For ell_n>=log(e/lambda), (3) implies (2). With lambda=gamma/m,
the prefactor in (2) is C m^2/gamma^2, as in the previous result.
No polynomial dependence on m is hidden by asking log(n) to exceed a
power of m.

At every fixed confidence 1-eta and for all sufficiently large
n>=n_0(d,L,phi,m,gamma,Y,eta), the initialization-only autonomous
construction satisfies

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_C(t,v)-f_n(t,v)|\le C_{\rm data,\eta}/\sqrt n.
 \tag{4}
\]

Both flows fit and converge. The constant is independent of width and
time. This is not an event simultaneous over independently initialized
widths or a growing-dataset theorem. The reference flow, initialization,
label range, query domain, and comparison norm are unchanged.

The new exponent 3d+2 replaces 2[d(L+5)+1]. In particular d=L=2
changes from log^30(en) to log^8(en). Arbitrary fixed depth changes
constants and the width threshold, but no longer the displayed logarithmic
power. This is a sufficient exponent, not an optimality theorem.

The construction is the already specified autonomous optimizer in
STORAGE_QUADRATIC_IMPROVEMENT.md, with a smaller proved source space.
Its non-diagonal fixed metric, internal residual coordinates, corrected
readout, and all dense reduced matrices are counted. It is not asserted
to be ordinary gradient flow of an unchanged smaller dense network.
Preprocessing uses finite initial derivatives and initialized arrays;
no trained path, externally supplied residual, or fitted function is an
input. Its finite exact-real work, temporary memory, and precision remain
unbounded. The result is about retained representation size.

## 2. The proof improvement

The prior analytic-source proof controls responses of a query to training
updates and to input-angle changes. Its endpoint trace was bounded using
the largest lower-layer response. That bound propagated a width-dependent
lower-layer maximum through successive layers.

Let ||T||_{p,n}=(tr|T|^p/n)^(1/p). The actual endpoint derivative Dq
has ||Dq||_{2,n}<=C, using only the RMS forward response. The opposite
endpoint C_a, the derivative of a training activation with respect to
mobility coordinates, has operator norm at most C. If there are h>=1
residual-Hessian factors H_j between the endpoints, normalized Schatten
Holder gives

\[
 \frac1n|\operatorname{tr}(Dq\,H_1\cdots H_h C_a^\top)|
 \le \|Dq\|_{2,n}\|C_a\|_{\rm op}
                \prod_{j=1}^h\|H_j\|_{2h,n}.
 \tag{5}
\]

The reciprocal exponents add to one. The bounded base propagators can
be inserted between the factors with their existing total operator cost.
At h=0, use the normalized Schatten-2 norms of both endpoints.
The separate-sample exponential budgets give
||H_j||_{p,n}<=C[1+Sp(2B)^(1/p)], where S=C_0Y/lambda is the bounded
total-activity scale and B is the existing structural budget. The h-fold
time integral has factor (CS)^h/h!. The resulting series converges
under the already imposed smallness conditions S<=c and S^2B<=c.
It contains no maximum of the lower-layer query response.

Together with the Gaussian carrier bound CS sqrt(ell_n), this gives
query forward responses of maximum CS sqrt(ell_n) and angle derivatives
of maximum C sqrt(ell_n) at every fixed layer. Depth affects the fixed
constants, not the width-dependent power.

One more step is needed: the time derivative of a backward signal contains
a product of a carrier and a forward velocity. Using a maximum again
would lose part of the improvement. On the stopped budget, for every p>=4,

\[
 \|k\|_{p,n}\le CSp(2B)^{1/p},\qquad
 \|\dot z\|_{2,n}\le C\rho S,\qquad
 \|\dot z\|_\infty\le C\rho S\sqrt{\ell_n},
\]

where rho=||r||_2/sqrt(m). Interpolate the last two bounds at
q=2p/(p-2), then apply Holder to obtain

\[
 \|k\odot\dot z\|_{2,n}
 \le C\rho S^2p(2B\ell_n)^{1/p}.
 \tag{6}
\]

Choosing p of order log(e+2B ell_n) reduces this to
C rho S^2 log(e+ell_n). This is a deterministic consequence of a stopped
exponential budget, not a probabilistic theorem with a growing number of
deleted neurons. The probability proof still takes each deletion count
fixed before the width limit.

Equations (5)-(6) permit a common complex time/input-angle radius
r_n=c ell_n^(-1/2), at every fixed depth. Pole margins are strictly
positive. The complex Gaussian-reference correction has radius at most
C ell_n^(-1/2)log(e+ell_n), whose Gaussian supremum tends to zero
despite the polynomial-logarithmic parameter net. Thus the separate-sample
budgets close under the same label condition.

On the horizon T=C lambda^-1 ell_n, all required source coordinates have
the sufficient complex bound C sqrt(n). At accuracy epsilon=n^-1,
their temporal and angular polynomial degrees satisfy

\[
 p\le C\lambda^{-1}\ell_n^{3/2}
                  [\ell_n+\log(e/\lambda)],\qquad
 J\le C\ell_n^{1/2}[\ell_n+\log(e/\lambda)].
\]

Time and d-1 angles therefore require

\[
 R\le C\lambda^{-1}\ell_n^{d/2+1}
                   [\ell_n+\log(e/\lambda)]^d
\]

source coordinates. The inherited runtime uses O(R^2) retained reals.
This proves (3). The actual source tolerance and stability argument have
not changed, so the same strict root-width error and infinite-time tail
comparison transfer. No new population approximation is introduced.

For tanh, the new common angular radius has the correct width-dependent
order for these source coordinates. On a fixed input circle, one initial
feature has the form tanh(a cos(theta)+b sin(theta)). With
R=sqrt(a^2+b^2), it has a nonremovable pole at imaginary angle
arsinh(pi/(2R)). The largest R among n independent Gaussian rows is
asymptotic to sqrt(2 log n). Thus no common source strip can have a radius
of larger order than 1/sqrt(log n). ANGULAR_RADIUS_CHECK.md gives the
complete direct proof. This does not establish that the final storage
exponent is optimal: it concerns source analyticity, not output complexity.

## 3. What is and is not removable about input dimension

The source-space lower bound in DIMENSION_FREE_REPRESENTATION_ROUTE.md,
reconstructed in INPUT_DIMENSION_SOURCE_CHECK.md, shows that input
dimension is a real obstruction for this particular proof interface.
For sine first-layer activation, with probability tending to one every
linear space uniformly approximating all initialized feature vectors to
normalized Euclidean error C/sqrt(n) has dimension at least

\[
 c_d\left(\frac{\log n}{\log\log(en)}\right)^{d-1}.
 \tag{7}
\]

This includes data-dependent and initialization-dependent choices of the
space. The proof uses the explicit covariance exp(-1)sinh(v^T u), its
positive harmonic components, and concentration of the finite coefficient
covariance. Thus a different linear basis or better sampler cannot remove
d from the logarithmic exponent while retaining uniform approximation
of the entire feature vector.

This is not a lower bound on the learned scalar output, and not a lower
bound on every autonomous representation. The initial output is exactly
zero even though (7) holds. An output-specific representation could bypass
the stronger hidden-feature reconstruction requirement. The result does
not establish that 3d+2 is necessary, either for tanh or for the full class.

## 4. A separate dimension reduction with a logarithmic error loss

Let r be the rank of the training-input span V and put D=min(d,r+1).
If r+1>=d, use the original representation, with D=d and no folding.
For the remaining case r+1<d, proceed as follows.
The exact equation (1) leaves A on V-perpendicular fixed at initialization.
Those unused Gaussian columns are independent of the entire training
path. For a fixed unit e in V-perpendicular, consider the folded query

\[
 \widetilde v=P_Vv+\|P_{V^\perp}v\|e.
\]

The original realized network restricted to V+span{e} is exactly a
canonical width-n network with D input coordinates. Its training flow and
initialized Gram gap are unchanged. INTRINSIC_INPUT_DIMENSION_ROUTE.md
proves, using conditional Gaussian rotation and a finite residual-activity
net, the unconditional weaker estimate

\[
 \sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(t,v)-f_n(t,\widetilde v)|
 \le C_{\rm data,\eta}\sqrt{\log(en)/n}.
 \tag{8}
\]

Apply (2)-(4) on this same realized D-dimensional slice, and evaluate it on
the folded query. A union of the two high-probability events and the
triangle inequality give a fully autonomous representation with

\[
 \operatorname{size}\le
 C\lambda^{-2}\log^{3D+2}(en)+C[m(d+1)+dr],\qquad
 \sup_{t,v}|f_C(t,v)-f_n(t,v)|
 \le C_{\rm data,\eta}\sqrt{\log(en)/n}.
 \tag{9}
\]

The fixed query preprocessor stores an orthonormal basis of V and computes
its projection and a Euclidean norm. It has O(dr) retained coefficients.
The original unused random columns are not retained. This explicitly
permits fixed radial input preprocessing; it is not a claim about a purely
linear first layer in the original input coordinates. Training still
uses the reduced model's own residual and physical clock.

Equation (9) can remove a large ambient d from the logarithmic storage
exponent, since D<=m+1. Its error has an additional sqrt(log n), so it
does not settle the requested strict C/sqrt(n) dimension reduction.
The strict bound is proved on each fixed active-input/time slice, uniformly
over passive directions, but the supremum over active inputs and the
whole trajectory needs a further mixed-response estimate. The route note
states that estimate explicitly; neither the pointwise variance nor
changing the clock alone proves it.

## 5. Evidence and limits

The independent first depth route and its check are preserved in
DEPTH_EXPONENT_ROUTE.md and DEPTH_EXPONENT_CHECK.md. They prove a weaker
logarithmic improvement. The stronger asymmetric-endpoint argument and
stopped-product interpolation are recorded separately in
DEPTH_INDEPENDENT_EXPONENT.md, with its complete reconstruction in
DEPTH_INDEPENDENT_EXPONENT_CHECK.md. The source lower bound and the
training-span route retain their precise restricted conclusions.

The reconstruction checked source SHA-256
`5da4e4593a040c82a8b12b2c63dea334cf65a3d4dd7e1dc0d48921102adf2932`;
its report is
`1a4270394c39740b8d0eb65bad7adee47ca4e45056f3116830a69c27b6fe82bd`.
Only source status and the explicit refined-event wording changed afterward.
INPUT_DEPTH_ASSEMBLY_CHECK.md, report SHA-256
`e9dcb633bb58baf3bdba11182f233e84c77bdc535ae868c8bdd0e337a5d0c4b0`,
independently reconstructs the norm, physical clock, label normalization,
retained-state count, strict runtime transfer and weaker folding corollary.
Its two wording requests have been applied: the full-rank input case is
handled before choosing a transverse vector, and the historical trace
loss is described without attributing the newer carrier cap to the older
proof. Neither repair changes a bound.

The source lower-bound version checked by the coordinator has SHA-256
`daa25ee23fb36c87e06e8f6e1102d21eef2d6c5e836695ea07a88259e5b92ec9`;
the complete check is INPUT_DIMENSION_SOURCE_CHECK.md. The complete
intrinsic route, including its exact mixed-response Sobolev criterion and
the weaker-error composition, has SHA-256
`4714d01381ad2bc0aaf9cfcf1572ffedddff30ff0767188e691df42b55ec13e4`.
The independent prompt-only tanh pole reconstruction is
ANGULAR_RADIUS_CHECK.md, SHA-256
`2f64d4ae9879734fbcdfd3411607a542eb524b673dc7f5c780b45ca2aaf5a2f1`.
These are scoped internal checks of actual derivations. They are not
independent promotion reviews of the entire inherited theorem chain.

The current strict theorem improves the proof and basis size without
changing the inherited autonomous optimizer. It removes depth from the
logarithmic exponent and substantially reduces the coefficient of d.
It does not establish growing-dimensional uniformity, an optimal storage
exponent, efficient finite-precision setup, or a dimension-free strict
root-width autonomous representation. No experiment or Git mutation was
part of this continuation.
