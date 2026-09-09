# Near-identity nonlinear OMFP: frozen research contract

Date: 25 August 2026.

## Canonical object

The actual two-hidden-layer mean-field feature-ascent network and its
pointwise fixed-step width limit already identified by the OMFP
row/column-conditioning theorem.  For every fixed finite step schedule,
width tends to infinity first.  Only after that identification may the
number of steps tend to infinity and the step size tend to zero.

## Activation class

For \(R\ge1\), let

\[
 \mathcal V_R=
 \left\{\varphi\in C^{12}(\mathbb R):
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R
 \right\}.
\]

For \(\varepsilon\in\mathbb R\), define

\[
 s_{\varepsilon,\varphi}
 =\left(\mathbb E[G+\varepsilon\varphi(G)]^2\right)^{1/2},
 \qquad
 \psi_{\varepsilon,\varphi}(x)
 =\frac{x+\varepsilon\varphi(x)}
        {s_{\varepsilon,\varphi}},
 \qquad G\sim N(0,1).
\]

This preserves the unit Gaussian RMS normalization.  If
\(|\varepsilon|R\le1/4\), then

\[
 3/4\le s_{\varepsilon,\varphi}\le5/4.
\]

The class is genuinely nonlinear: for example, bounded smooth
\(\varphi\) with \(\varphi''\not\equiv0\) are included.

## Target theorem

With

\[
 \Delta_{t,2}(h)
 =F_{2t,2}(h)-F_{t,2}(2h),
\]

seek explicit quantities

\[
 \varepsilon_0(R)>0,\qquad
 \rho_R>0,\qquad C_R<\infty,\qquad \beta<1,
\]

depending only on \(R\), numerical constants, and stated Gaussian moments,
such that, uniformly over
\(\varphi\in\mathcal V_R\), \(|\varepsilon|\le\varepsilon_0(R)\),
integers \(t\ge1\), and \(|h|\le\rho_R/t\),

\[
 \left|
 \Delta_{t,2}(h)
 -\frac{t(2t-1)}2J_{\psi_{\varepsilon,\varphi},2}h^3
 \right|
 \le C_R t^{4+\beta}|h|^5.
\]

Here \(J_{\psi,2}\) is the already proved finite Gaussian activation
integral, not an output derivative.  The ideal perturbative theorem has
\(\beta=0\).  Any explicit \(\beta<1\) suffices for scalar dyadic
convergence.

## Allowed coefficient provenance

Constants may use only:

1. \(R\) and the displayed normalization bounds;
2. finitely many numerical Gaussian moments or explicit Gaussian
   exponential integrals;
3. finite recursions whose initialization and update rules are fully stated;
4. the fixed depth \(L\), when testing a depth-three transfer.

They may not use terminal-output derivatives, a modulus of \(F_t\), the
unknown trained trajectory, a horizon-dependent minimum over the realized
state, Gram inverses, or a resampled-matrix surrogate.

## Required topology and internal estimate

The proof must work on the exact chronological OMFP DAG, combine response
coordinates into intrinsic aggregate adjoint actions before taking norms,
and control every generated field, first source tangent, mixed
step/source tangent through total order four, and transported local-defect
direction required by the exact paired-Euler factorization.

## Non-resolutions

The following do not resolve the target:

1. continuity in \(\varepsilon\) for each fixed \(t\);
2. an admissible radius \(\varepsilon_0(t)\) that tends to zero with \(t\);
3. ambient \(C^4(L^2,L^2)\) smoothness of the Nemytskii map;
4. an ambient \(L^p\) bound for \(J^*\) or \(I^*\);
5. a finite-width Taylor expansion followed by a diagonal limit;
6. a theorem only for affine perturbations;
7. assuming the desired generated-response estimate under a new name.

## Claim ladder

1. Exact: normalization, fixed-step width identification, response
   divisibility, paired-Euler defect factorization.
2. **Completed intermediate rung:** the exact fifth Taylor coefficient is
   \(O_{\psi,L}(t^4)\), with the explicit bound
   \((227/180)B_\psi^{E_{L,5}}t^4\), for every admissible activation and
   fixed depth.  This is a pointwise jet theorem, not an interval remainder.
3. Required new lemma: horizon-uniform perturbative generated-response
   estimate on bounded total step variation.
4. Consequence: a sub-\(t^5\) full interval remainder coefficient.
5. Consequence: scalar dyadic continuous-time convergence.
6. Stronger, separate rung: state convergence and restartable IDE.
7. Extension: a depth-three connector transfer preserving the
   sub-\(t^5\) exponent.

## Concrete falsifiers

* A smooth bounded \(\varphi\) for which every nonzero \(\varepsilon\)
  forces the canonical coefficient to grow at least like \(t^5\) along a
  dyadic subsequence falsifies the target theorem.
* Failure of ambient \(L^2\) smoothness only falsifies the naive Banach
  proof, not the generated-core conjecture.
* A perturbative estimate growing like
  \(\exp(c|\varepsilon|t)\) at \(h\asymp1/t\) falsifies the proposed
  uniform homotopy argument; growth in total time
  \(\exp(c|\varepsilon|\,t|h|)\) is admissible.
