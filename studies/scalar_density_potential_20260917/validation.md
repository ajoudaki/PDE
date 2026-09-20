# Author verification

Date: 2026-09-17. Author and checker: current primary agent.
Result: internally checked for the exact scopes in potential.md. No independent
review, numerical evidence, promotion, or general multiple-input fitting claim.

## Source coverage and provenance

The relevant source versions are frozen by manifest.sha256. HEAD at author
checking was 019e3630237e33f58b9636c0aa67a039bebf0182. The entire shared reading
guide and notation contract were read; truncated reads were repaired. The
initialized coefficient target of observable_p1.md and the finite equations
and bounded-mark existence/energy proof C.4.7.10.C.1/C.3 in global_nonlinear.md
were inspected. The new proof rederives its scalar coefficients, symmetry
reduction, Gaussian positivity, geometric minimization, and long-time estimates.
No other study is a scientific premise and no subagents were used.

## Checks actually performed

- Differentiated the finite-dictionary prediction in every moving block.
  The physical gradients are exactly the three negative velocities in (1),
  with the unhalved-loss factor 2 and x/sqrt(2) input normalization.
  The scalar reverse action is the same M. The displayed finite-time
  estimates follow from the energy identity and bounded marks, without
  any kernel lower bound or convergence assumption.
- Recomputed the retained initial coefficient by scalar Gaussian integration
  by parts. The same lower Gaussian g is used in b1 and w0; the upper
  population is a separate integration space. There is no missing noise
  term inside this declared forward-only scalar dictionary.
- Verified reflection invariance directly in the velocity, including the
  negative sign of b1 under g1 negation. The resulting a_minus=-a_plus,
  H_minus=-H_plus and equal d values yield all factors in (8).
- Checked Q=C-gamma B using Cauchy--Schwarz separately for gamma>=0 and
  gamma<0. At the antipodal endpoint gamma=-1 the formula remains positive.
  The forbidden coincident endpoint delta=0 would have zero a0 and K0;
  no rate is asserted there or uniformly near it.
- Derived e_dot=-2Theta e before the sign bootstrap. This proves e>0 on
  finite intervals independently of any claim that c, M or a is monotone.
  Positive a,M imply c has the sign of b2 and hence d>=0; their nondecreasing
  velocities close the continuation argument. At positive times the signs
  are strict because b2 is nonzero almost surely.
- Differentiated K as an integral against the frozen b2 marginal. The
  c-coordinate transport adds no term because the integrand is independent
  of c. The remaining derivative is exactly (10), with nonnegative sign.
  The quotient derivative (11) retains K_dot/K. No moving-metric term is
  dropped. Since K0<=K<=1, the potential cannot vanish while loss stays
  positive by a collapse of its denominator or cost.
- Checked the geometric minimizer by Cauchy--Schwarz both for deterministic
  readout shifts and for arbitrary mark-preserving transport couplings.
  The correction q=eH/K attains the lower bound, fits both labels, and
  uses only the present state. The target is the zero-loss set, with no
  externally supplied endpoint or preferred hidden representation.
- Independently squared all three reduced velocities. Their sum is
  4e^2Theta, matching -L_dot. To check the path estimate, used
  V(s)>=2 sqrt(K_t L_s) for s>=t, then V=V^2/V to integrate
  (-L_dot)/(2 sqrt(K_t L)). The inequality orientation is correct and
  requires monotonicity of K. The resulting finite path length makes the
  carrier state Cauchy in a complete Hilbert space; compactness is not
  substituted for strong convergence. Bounded marks and Lipschitz gates
  show uniform-input prediction convergence and identify a fitting endpoint.
- Distinguished actual paired activation motion from parameter motion:
  growing a forces nonzero lower activation displacement, and growing Ma
  forces upper activation displacement. The representation separation 4K
  is a direct same-mark L2 difference of the upper activations.
- Substituted the stationary counterexample into every block at t=0.
  Equal initial activations cancel the readout velocity, and c0=0 kills
  the remaining velocities. Uniqueness makes this an exact equilibrium.
  The alternate fitting state has finite second moments and a bounded
  readout, so these labels are representable. It is not claimed reachable.
  The no-go statement explicitly requires a finite potential and F(0)=0.
  It excludes an all-law strict-fitting assertion, not a generic-data one.
- Recomputed the finite-data least-norm correction, the pseudoinverse
  variant on the Gram range, and the inverse-Gram derivative. The exact
  symmetric expression is K_dot+2(Theta K+K Theta); no commutation is
  assumed. The concrete rational example has determinant -1149/5000,
  checking that Theta>=K alone is not enough algebraically. It is expressly
  not claimed to be a reachable pair of model kernels. The initialized
  derivative Phi_dot(0)=-4L0 and the Vandermonde positivity proof are exact;
  continued invertibility and estimate (15) for generic multiple inputs
  remain open.

## Reproduction and limits

The full analytic argument is in potential.md. Read it with the cited
established source sections; there are no experiments, external numerical
arrays, random seeds, or software tests needed to reproduce the argument.
The source/artifact manifest can be verified by running

    sha256sum -c studies/scalar_density_potential_20260917/manifest.sha256

from the repository root. Author checking supplies internal confidence only.
No claim is promoted into established material by this audit.
