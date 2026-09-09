# Positive signed-work coefficient with the prescribed tiny readout

Candidate combined lemma, pending complete independent audit of this
note and its two explicit proof dependencies. This is a statement
about an actual initial response coefficient under the canonical
initialization, not a theorem of global continuation.

Use exactly \(\phi=\arctan\), independent initial
\(z^{(1)}_j\sim N(0,1)\), entries of \(W^{(2)},W^{(3)}\sim N(0,1/n)\),
and rescaled \(W^{(4)}_j\sim N(0,n^{-2})\). All four blocks are
independent. All trained blocks obey the canonical feature-time
equations, with no residual included in the backward fields.

For each middle column \(i\), apply an auxiliary infinitesimal
initial top-matrix perturbation \(\xi e_i^T/\sqrt n\), with standard
Gaussian \(\xi\) independent of initialization. Write
\(\zeta_i=\operatorname{variation}_i z^{(2)}\) and
\[
a_i(s)=\int_0^s\operatorname{variation}_i\delta^{(2)}(u)\,du,\qquad
c_i(s)=\operatorname{diag}(\phi'(z^{(2)}(s)))^{-1}a_i(s),\qquad
\beta(x)=-\frac{2x}{1+x^2}.
\]
Define the full signed primitive work, including its retained memory,
\[
\mathscr W_n(s)=\frac1n\sum_{i=1}^n\mathbb E_\xi\!
\left[c_i^T\operatorname{diag}(\beta(z^{(2)}))
\left(q^{(2)}\odot\zeta_i-(z^{(2)})'\odot c_i\right)\right],
\quad
q^{(2)}=(W^{(3)})^T
   [W^{(4)}\odot\phi'(z^{(3)})].
\tag{1}
\]
All quantities on the right are at feature time \(s\).
The expectation conditions on the actual initialized trajectory.
It does not average a resampled or independent trained matrix.
Let
\[
J_n^{\rm can}=\frac1{5!}\frac{d^5}{ds^5}\mathscr W_n(0).
\]
The derivative is taken at each finite width first.

Then \(J_n^{\rm can}\to J_*>0\) in probability, with the following
explicit constant. Set
\[
\psi(x)=\phi(x)\phi'(x),\qquad
\mu_1=\mathbb E\phi(G)^2,\quad
\mu_2=\mathbb E\phi(\sqrt{\mu_1}G)^2,\quad
b_1=\mathbb E[\phi(G)^2\phi'(G)^2],
\]
where \(G\) is standard Gaussian. For \(v>0\), write \(Z_v=\sqrt vG\)
and define
\[
A(v)=\mathbb E\psi(Z_v)^2+
 v\mathbb E\!\left[(\phi'(Z_v)^2+\phi(Z_v)\phi''(Z_v))^2\right],\qquad
\gamma(v)=\frac{\mathbb E[Z_v\psi(Z_v)]}{v}.
\]
For \(Z=\sqrt{\mu_1}G\),
\[
J_*=-\frac{A(\mu_2)\gamma(\mu_2)b_1}{4\mu_1^2}
        \mathbb E[Z\beta(Z)]\,\mathbb E[Z\psi(Z)]>0.
\tag{2}
\]

To prove the assertion, couple the initialization to exact zero readout
using \(W^{(4)}(0)=\rho G_4\), with independent standard Gaussian \(G_4\).
Write \(P_n(\rho)=[s^5]\mathscr W_n^\rho(s)\).
GAUSSIAN_SIGNED_PRIMITIVE_WORK_JET.md proves, by exact conditioning
on both Gaussian hidden matrices and conditional concentration,
\[
P_n(0)\to J_*\quad\hbox{in probability and }L^1.
\]
It includes every trained factor, both covariance cross terms, the
finite-width empirical-product bias, and the complete signed work in
(1). Its independent Gaussian roots and all normalizations are the
same as here.

TINY_READOUT_SIGNED_JET_TRANSFER.md proves for this very same
finite coefficient that \(P_n(\rho)\) has degree at most six in
\(\rho\), with all seven random polynomial coefficients tight.
It does so by expanding the actual finite jets into finitely many
parameterless Gaussian programs and polynomial prefactors made from
their empirical contractions. Tensor Programs III, Theorem 2.10,
controls those contractions. A separately proved conditional Gaussian
quadratic-form estimate and fixed Vandermonde interpolation then give
the coefficient bounds. The theorem's hypotheses are explicitly
verified there. No empirical-scalar-feedback extension, rank-stability
premise, or expectation-convergence theorem for arbitrary polynomial
tests is assumed.
Consequently
\[
P_n(n^{-1})-P_n(0)=O_{\mathbb P}(n^{-1}).
\]
But \(P_n(n^{-1})=J_n^{\rm can}\) under exactly the initialization
of this note. Addition of the vanishing difference proves (2) in
probability. In particular
\(\Pr(J_n^{\rm can}>J_*/2)\to1\).
No \(L^1\) claim for the canonical tiny-readout coefficient is inferred
from tightness alone.

The result excludes an exact cancellation of the whole signed work
as a local identity on a canonical initialization event of probability
tending to one: such an identity would make its fifth coefficient
zero. It also excludes a nonpositive fifth-coefficient claim.
It does NOT by itself exclude a nonpositive bound for the complete
function at positive times, because lower coefficients need not
vanish for tiny readout. Nor does it prove positivity on a common
time interval, a width-uniform Taylor remainder, response-amplitude
growth, failure of a positive-constant Gronwall estimate, or failure
of the global population theorem. Any quantitative signed estimate
must accommodate the explicit positive initial coefficient; it
cannot rely on simply dropping this full term by exact cancellation.

Explicit dependencies:

- GAUSSIAN_SIGNED_PRIMITIVE_WORK_JET.md, with its three listed primitive
  identities as dependencies.
- TINY_READOUT_SIGNED_JET_TRANSFER.md, including its complete finite-jet
  equations, conditional quadratic-form proof, and checked application
  of [Tensor Programs III, v3, Theorem 2.10](https://arxiv.org/pdf/2009.10685v3).

All conclusions remain finite-coefficient statements. The unchanged
full all-finite-time canonical mean-field/gradient-flow theorem is open.
