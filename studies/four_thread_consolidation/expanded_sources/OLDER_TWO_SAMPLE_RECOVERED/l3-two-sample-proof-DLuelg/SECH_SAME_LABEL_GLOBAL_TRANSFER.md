# The same-label global theorem survives the sech refinement

Root modular transfer, 2026-09-06. UNREVIEWED. This is the same-label
subtheorem, not the full two-label target or the final self-contained
document. No opposite-label fitting-time bound is claimed.

Keep every model, initialization, raw update, clock and observable in
the two-sample contract. Use the single fixed scalar activation

  phi(z)=1+0.1 atan(sinh z).

For either equal-label pair and every fixed rho in [-1,1), the earlier
same-label proof transfers with unchanged numerical clock and bootstrap
constants. Its full conclusion includes uncut autonomous population
flow and reached-state restart uniqueness, full-sequence joint exact
raw GD / finite GF / population convergence on every finite physical
horizon, all four two-by-two raw kernel blocks, both directions of both
hidden operators, hidden paths and velocities, and strictly nonlinear,
nonlazy feature learning in every hidden layer. The argument below
specifies every activation-specific replacement in that modular proof.

Dependencies, each read completely by the root:

- SECH_GATE_ACTIVATION_DESIGN.md, SHA256
  c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24.
- TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, SHA256
  9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170.
- SAME_LABEL_GLOBAL_ASSEMBLY.md, SHA256
  510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44.
- SAME_LABEL_NONTRIVIALITY.md, SHA256
  76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6.
- The elementary common-program/operator construction explicitly imported
  by those notes from L3_GLOBAL_SELF_CONTAINED_PROOF.md, SHA256
  bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e.

The same-label bundle has a complete modular audit for shifted arctan.
That audit is not silently reassigned to this activation or this document.
No result from the pending cubic-control/sign-change notes is used here.

The new activation is smooth with bounded derivatives of each fixed
order, with 5/6<phi<7/6, 0<phi'<=1/10, and |phi''|<=1/5. The raw
two-sample short bootstrap uses exactly these upper bounds; it uses no
arctangent inverse coordinate or arctangent identity. Each of its source
derivative inductions, variance bounds and final Gaussian integrals is
therefore unchanged. In particular, on feature interval [0,3/2] both
actual cut reverse queries have E exp(q^2/16)<=2, the response row sums
are at most one, and the forward response kernels are bounded by 3/2.

The assembly's common spaces, bounded initial actions and actual
adjoints, fixed-cut Picard flow, linear-in-cap asymmetric comparison,
cut removal and local restart use only those bounds. Its scalar
gradient differentiability proof uses bounded phi', phi'' and truncation
of a fixed L2 backward field. Its same-label scalar clock additionally
uses phi>=m=5/6. Hence g' >=m^2, g(0)=0, and the fitting feature time
s_* is at most 36/25<3/2. The clock ds/dt=4(1-g) approaches s_* only
at infinite physical time, exactly as in the assembly. Global physical
restart compares any competitor against the cut reference and requires
no symmetry of the competitor.

The finite physical GF/GD comparison and stopping argument use bounded
activation/gates, Lipschitz gates, bounded reference readout and the
same two reference tails. Raw GD is still exact Euler with eta_n=n^-2;
there is no activation-dependent coordinate transform of GD. Inside-step
gate discrepancies have the same O(eta_n sqrt(n)) bound. The transferred
proof thus gives all listed observable and path/velocity conclusions
with the same right-interior/left-terminal velocity conventions. This
does not assign an exact scalar clock to finite random residuals.

There are just two numerical activation-specific replacements in the
nontriviality supplement. First, its forward separation event
Z_1>=1, Z_2<=-1 still implies

  phi(Z_1)-phi(Z_2)>=2(0.1)atan(sinh 1)>(0.1)pi/2.

Indeed sinh 1>1, from its power series, and atan is strictly increasing.
The source dominator, event probabilities and every feature Gram lower
bound in Section 1 are consequently unchanged. The two unbounded
marginal tails in Section 2 are likewise unchanged. Boundedness and
strict monotonicity of phi then give a strictly positive best-affine
error at each time, with a positive compact-time minimum, as there.

Second, in the top-delta rectangle in Section 3 use
delta^(3)_a=W^(4)(0.1)sech(Z^(3)_a). The same source bound gives
|Z^(3)_1|>=18/5 and |Z^(3)_2|<=1/2. Elementary series estimates give

  cosh(1/2)<5/4,
  cosh(18/5)>=1+(18/5)^2/2=187/25>5.

For the first inequality, the cosh series after its constant term begins
with 1/8, and successive ratios are at most 1/48; hence its sum is at
most 1+(1/8)/(1-1/48)=1+6/47<5/4. Evenness and monotonicity of cosh
on the positive half-line show that on that rectangle

  delta^(3)_1/delta^(3)_2
       <=cosh(1/2)/cosh(18/5)<1/4,
  delta^(3)_2> (4/5)m s_0(0.1).

Thus the SAME gate-ratio and positive-large-delta bounds used by the
supplement remain valid. The swapped rectangle gives the second
direction. The resulting top backward Gram is positive definite at
every positive feature time. The middle and bottom Gaussian-source
quadrant arguments need only this strict covariance, bounded response
shifts and positive gates, so they transfer without alteration.

The trace-product and forward-velocity pairings of Section 4 do not
depend on the formula for phi. They show every hidden raw block and
every sample's hidden feature velocity is nonzero at every positive
finite physical time. At initialization the same strict backward Grams
make each hidden second-order motion coefficient nonzero. The initial
feature and kernel expansions in Section 5 use the fixed smooth bounded
gates and the identified reused-matrix laws, not an arctangent-specific
identity. Their nonzero physical t^2 coefficients and nonconstant total
kernel therefore remain valid for the fixed sech activation.

All replacements preserve the input endpoint rho=-1 and need only
configuration-dependent strictly positive constants. The activation is
not sent to a linear limit. This transfer preserves the full established
same-label half while testing the new activation on opposite labels;
it supplies no missing global estimate for the latter.
