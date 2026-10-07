# Cross-route audit of the frozen initial-amplitude candidate

2026-10-06. Scoped internal reconstruction and mathematical audit. This is
not independent discovery, a promotion review, or a complete audit of the
inherited source theorem. The candidate was not edited and no experiment
was performed.

## Frozen inputs and verdict

The complete 623-line `POLYNOMIAL_SETUP_INITIAL_ROUTE.md`, including
Section 6, was read at SHA-256

```
6cae513b17db1930326b13c381b6aacefa4ad2144ba41b2ae4ac9b8454d82f3f
```

The source of the inherited mathematical definitions was `RESULT.md`,
SHA-256

```
c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278
```

The notation contract was `docs/notation.qmd`, SHA-256

```
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023
```

The relevant complete `RESULT.md` inputs were its dense equations and
mobilities; fitting and initialized feature-gap statements; four Harmonic
source families and exact pairing; finite initial-jet map; supplied-budget
and cost statements; finite deletion and its local variational comparison;
source RMS, derivative and mixed-endpoint recurrences; source analytic
domain; and initial-jet execution formulas. No other study or archived
book was used. The probabilistic source theorem is an imported hypothesis.

The accessible rigorous-math and adversarial-audit instructions were used.
The required canonical-notation skill remained unreadable at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`, including
on the earlier escalated read. The supervisor-authorized fallback to the
accessible skill, notation contract and explicit user notation rules was
retained.

**Verdict:** no must-fix mathematical error was found in the finite
coefficient hierarchy, function-class claim, local complex-ball lemma,
bivariate cutoff, conservative arithmetic count, pairing argument, or
Section 6 identities. These support the stated conditional route. The
complex-label tube remains an additional unproved theorem; neither the
candidate nor this audit establishes polynomial setup for the full model
class. The favorable rates also retain the activation-backend and exact-real
qualifications expressly stated in the candidate.

## 1. Triangular amplitude hierarchy

In normalized dense coordinates
\(u=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), let
\(\xi_a=\nabla_u f_a\). The dense equations with labels
\(\zeta y\) are

\[
\dot u=\frac2m\sum_a c_a\xi_a,\qquad
c_a=\zeta y_a-f_a,
\qquad
\dot c=-\frac2mK_nc,
\quad (K_n)_{ab}=\xi_a^T\xi_b.
\]

All transposes are algebraic transposes when variables are complex.
At \(\zeta=0\), zero initialized readout makes the complete
parameter state stationary. Simultaneously replacing
\((\zeta,w,c)\) by \((-\zeta,-w,-c)\) leaves the hidden
equations unchanged and negates the readout equation. Uniqueness gives
the claimed parity: hidden parameters and forward fields are even,
whereas the readout, deficit and backward fields are odd.

At amplitude zero, only the readout gradient block contributes to the
tangent Gram. Its entries are \(h_{0,a}^Th_{0,b}/n\). Therefore
\(2Q_0=2H_0^TH_0/(mn)=G_0\), with the candidate's exact
normalization. The initialized feature-gap event makes this real symmetric
matrix positive definite. Differentiating the deficit equation by
normalized coefficient extraction yields

\[
(\partial_t+G_0)c_r
=-2\sum_{k=1}^{r-1}Q_kc_{r-k},
\]

and \(c_1=e^{-G_0t}y\). The missing \(k=r\) term vanishes
because \(c_0=0\). Initial data agree with the candidate.

The coefficient sums in its (2) are the direct products in the dense
rank-one equations. Since both \(c_0\) and \(\delta_0\) vanish,
the hidden parameter coefficient at order \(r\) uses only deficit
and backward coefficients of order at most \(r-1\). The forward
coefficient at order \(r\) is then obtained from those hidden
parameters. The equation for \(c_r\) uses \(Q_k\) only for
\(k<r\). Finally \(w_r\) uses \(c_rh_0\) and lower-order
terms, and backpropagation gives the order-\(r\) responses. This is
an actual triangular order, with no circular dependence on \(w_r\)
or \(c_r\) when constructing the hidden order-\(r\) coefficient.

The local-ball lemma checked below guarantees that these formal
coefficients equal actual amplitude derivatives near zero for every
fixed finite time horizon. No convergence at amplitude one is inferred
from triangularity.

## 2. Exponential-polynomial function class

Diagonalizing the fixed real symmetric matrix \(G_0\) is legitimate
for the proof. It is not an implementation primitive. Its eigenvalues
\(\omega_i\) are positive. The class consisting of finite sums
\(t^p e^{-\nu t}\), with
\(\nu=\sum_i k_i\omega_i\), is closed under the needed products.

A scalar forced equation with homogeneous factor \(e^{-\omega_i t}\)
has solution

\[
e^{-\omega_i t}\int_0^t s^p e^{-(\nu-\omega_i)s}\,ds.
\]

If \(\nu\ne\omega_i\), integration by parts produces a polynomial
of degree at most \(p\) multiplying \(e^{-\nu t}\), together
with a constant multiple of \(e^{-\omega_i t}\). If the frequencies
coincide, the result is
\(t^{p+1}e^{-\omega_i t}/(p+1)\). A plain primitive with
\(\nu>0\) similarly gives a polynomial of the same degree at
frequency \(\nu\), plus a constant. These computations verify
the candidate's closure statements without a frequency-separation
assumption.

Every deficit coefficient has positive frequency: this is true for
\(c_1\), and multiplication of a lower deficit by a Gram coefficient
cannot remove its positive frequency. Solving the forced deficit equation
only introduces another positive eigenfrequency. Consequently every
parameter-update forcing contains a positive-frequency deficit factor.
Its plain primitive never integrates a zero-frequency forcing term.

The stated degree bookkeeping is sufficient. A nonconstant Gram coefficient
starts at order two. In the forcing for \(c_r\), a term with
\(Q_k\), \(k\ge2\), has polynomial degree at most

\[
(k-2)+(r-k-1)=r-3.
\]

A resonance adds at most one degree, which is no greater than the
asserted deficit allowance \(r-1\). Hidden forcing combines a
positive-order deficit and response, giving at most \(r-2\),
including products with positive-order features. Readout forcing has
degree at most \(r-1\). Composition of an analytic activation uses
partitions into positive hidden orders, all at least two, and preserves
the forward degree bound \(r-2\). The same product argument controls
the feature and backward pieces of the tangent Gram. Initialized images
are fixed linear maps and do not change the class.

Frequency multiindices add under products, and their total counts are
bounded by the sum of the amplitude orders of the factors. A primitive
adds only zero frequency, and a deficit convolution can additionally
introduce an individual eigenfrequency. Hence \(\sum_i k_i\le r\)
is preserved. Counting nonnegative multiindices with that constraint
gives \({r+m\choose m}\); allowing the candidate's relaxed degree
range \(0\le p\le r\) gives its bound
\((r+1){r+m\choose m}\). Repeated eigenvalues or frequency sums
cannot increase the span dimension. These are finite-order identities,
not convergence estimates for the full amplitude expansion.

## 3. The local complex-ball lemma

The normalized ball has radius \(b/\sqrt n\). Operator perturbations
of the first normalized matrix and hidden matrices are bounded by their
Euclidean/Frobenius parameter discrepancies, so their operator caps remain
fixed. Real initialized preactivations can be arbitrarily large; only
their imaginary displacement matters for staying inside the activation
strip.

Forward differentiation with a unit normalized parameter increment gives
\(\|Dh^{(j)}\|_2/\sqrt n\le C\). The coordinate displacement
is consequently at most \(C\sqrt n\|u-u_0\|_2\). Choosing
\(b\) small gives a strict half-strip margin. A bootstrap along
straight parameter segments validates this derivative argument throughout
the ball. For the second derivative, the only additional width factor
is bounded by

\[
\frac{\|a\odot b\|_2}{\sqrt n}
\le\sqrt n\frac{\|a\|_2}{\sqrt n}
                 \frac{\|b\|_2}{\sqrt n}.
\]

The product rule and fixed number of layers then give
\(\|D^2h^{(j)}\|_2/\sqrt n\le C\sqrt n\), as stated.
Bounded first and second activation derivatives suffice here.

The initialized readout is zero, so throughout this ball
\(\|u_w\|_2\le b/\sqrt n\). Writing
\(f=u_w^Th^{(L)}/\sqrt n\), the first derivatives have bounded
operator norm. In the second derivative, the readout/hidden cross terms
use \(Dh/\sqrt n\), whereas the hidden/hidden term is bounded by
\(\|u_w\|_2\|D^2h\|_2/\sqrt n\). The latter is also bounded
independently of width. This verifies (13), including the mechanism
removing the apparent \(\sqrt n\) Hessian factor.

For the holomorphic vector field
\(F=-2m^{-1}\sum_a(f_a-\zeta y_a)Df_a^T\), differentiation gives
a sum of products of first derivatives and residual-weighted second
derivatives. The preceding bounds and
\(m^{-1}\sum_a|y_a|\le Y\) give a width-independent constant
\(C_1\) on the ball for \(|\zeta|\le1\). At its center,
\(f_a=0\), so \(\|F(u_0;\zeta)\|_2\le C_2|\zeta|\).
This uses complex absolute-value norms and no complex positive-semidefinite
Gram assertion.

The radial integral majorant is
\(C_2|\zeta||t|e^{C_1|t|}\). Inserting the radius in (11),
with \(|t|\le2T\), bounds it by

\[
\frac{b}{4\sqrt n}\frac{2T}{1+2T}<\frac{b}{4\sqrt n}.
\]

Thus the trajectory stays strictly inside the analytic ball. Holomorphy
on the full disk can also be justified directly by Picard iterates on
radial integrals: their differences have the factorial majorant from
iterated integration, and every partial iterate stays inside the same
ball because the finite exponential majorants are bounded by the displayed
strict bound. Their uniform limit is holomorphic jointly in \(t,\zeta\).
This supplies an explicit justification for the candidate's continuation
and uniqueness argument. Constants can be enlarged to leave a neighborhood
of the closed polydisk.

The forward and backward source formulas remain holomorphic there, with
bounded RMS. Coordinate conversion and initialized operator bounds give
the common \(C_3\sqrt n\) envelope separately for all four source
families. Uniformity over real unit queries follows from the same operator
recursions; a complex sphere tube is not claimed by this local lemma.

This lemma requires only the initialized operator event. Its amplitude
radius is small and does not prove the global tube of Section 2.

## 4. Conditional amplitude continuation and bivariate cutoff

The proposed complex-label tube is explicitly an obligation, not an
inherited result. Conditional on it, the conformal map is the earlier
initial-jet construction with interval length one and strip radius
\(b_n\). It takes the unit disk into the proposed label rectangle,
sends zero to zero, and sends the stated \(\xi_*<1\) to one.
The source bound on that rectangle gives Cauchy coefficient bound
\(Cn^A\) after composition and hence the geometric tail (9).

For clarity, the scale of the map's endpoint distance can be checked
directly. Since

\[
1-\vartheta
=\frac{\tanh(\chi+\pi/4)-\tanh\chi}
        {\tanh(\chi+\pi/4)},
\qquad \chi=\frac{\pi}{8b_n},
\]

the elementary exponential formula for \(\tanh\) makes
\(1-\vartheta\) comparable, with universal positive constants for
\(b_n\le1/4\), to \(e^{-2\chi}\). Thus
\(1-\xi_*=(1-\vartheta)^2/(1+\vartheta^2)\) is comparable
to \(e^{-4\chi}=e^{-\pi/(2b_n)}\). The sufficient order (10)
follows by using \(-\log\xi_*\ge1-\xi_*\) and retaining the
geometric-tail denominator. Polynomially small nodal tolerance therefore
gives polynomial \(K\) under (6), and \(K=n^{o(1)}\) under
(7). Neither conclusion is unconditional.

Cauchy in the small local amplitude disk gives the bound
\(C_3\sqrt n R_{n,T}^{-r}\) on \(g_r\) for \(|t|\le2T\).
Cauchy in time, evaluated on \([0,T]\), then gives the geometric
Taylor tail in (16). The map satisfies \(|\sigma(\xi)|\le2\),
because its image rectangle has \(b_n\le1/4\). Consequently
\(|[\xi^j]\sigma(\xi)^r|\le2^r\).

There are at most \((K+1)^2\) terms in the double coefficient
sum. For \(R_{n,T}\le1\), their combined perturbation is bounded
by the candidate's (17), with a harmless factor-two slack. The local
constant \(b\) may be decreased so that \(R_{n,T}\le1\),
as already permitted in the lemma and stated for (18). Solving this
bound for \(N\) gives (18). Also

\[
\log(1/R_{n,T})
=\tfrac12\log n+2C_1T+\log(1+2T)+O(1),
\]

which proves the growth rate in (19). The small local radius enters
logarithmically in this second cutoff, multiplied by the amplitude order
\(K\); it is not substituted into the global continuation map.
This distinction is correctly maintained throughout the candidate.

## 5. Actual initial algebra, operation count, and exact pairing

The finite polynomial-ring construction is executable coefficient algebra.
At time degree \(s+1\), the ODE gives the next coefficient by dividing
the time-degree \(s\) coefficient of its right-hand side by \(s+1\).
Each such right-hand side depends only on parameter coefficients already
computed at smaller time degree. All coefficients are polynomials in
\(\zeta\), truncated at degree \(K\). At zero label amplitude,
hidden state is stationary, and parity makes its preactivation increment
divisible by \(\zeta^2\). Thus scalar composition uses finitely
many derivatives at the initialized preactivation. For \(K\ge1\),
order at most \(K\) suffices even for derivative gates after accounting
for their multiplication by an odd backward field. Computing extra gate
coefficients would still cost only polynomially many derivatives.

A direct product of two \((K+1)\)-by-\((N+1)\) coefficient
arrays costs at most \(O((K+1)^2(N+1)^2)\). Horner composition
through at most order \(K\), repeated at each time-degree stage,
costs at most another factor \((K+1)(N+1)\). The conservative
fourth powers in (20) therefore dominate these executions. Dense
forward/backward matrix operations and rank-one updates supply at most
the displayed factor in \(n,d,m,L,m+N_x\). Sharing the training
coefficients across passive queries only reduces that loose upper bound.
The ring arrays and scalar composition scratch have polynomial size in
the same cutoffs. The note does not claim an optimal peak-memory bound.

Generating activation derivatives is separately charged. Analyticity alone
does not give a computational-cost or bit-complexity bound for that operation.
Under fixed structural parameters, \(K,N,N_x=n^{o(1)}\) makes the
displayed non-backend initial arithmetic \(n^{2+o(1)}\). This is
a conditional coefficient calculation, not an unconditional full setup
theorem. Node generation, quadrature, final source processing, selection
and assembly must retain their own bounds.

The execution uses actual ODE derivatives at \(t=\zeta=0\); all
activation derivatives are evaluated at initialized preactivations. It
does not assume a trained dense state, solve a nonlinear positive-time
trajectory as an input, or advance a dense state through the horizon.
This is the relevant provenance distinction. Merely avoiding sequential
time steps would not suffice, but the stronger initial-derivative fact is
proved here. Conditional evaluation of the resulting coefficient
polynomials at quadrature nodes is accounted for as polynomial evaluation.

For a fixed initialized matrix \(W_0\), mixed differentiation commutes
with its action. Every subsequent operation in (8), both Taylor cutoffs,
evaluation and scalar quadrature is linear and shared by the two members.
Thus the resulting finite coefficient vectors satisfy the exact
initialized-image identity. The transpose pair works identically. The
individual source bounds apply separately to each member, so no matrix
infinity-norm conversion of one member's coordinate error is required.
The retained joint harmonic/cosine modes are unchanged; additional
bivariate coefficients are setup arrays and do not become new source
generators. Accurate paired coefficients therefore preserve the existing
rank and retained-storage argument.

The statement that elementary angular Riemann quadrature can still use
polynomially many nodes at polynomial accuracy is consistent with the
source bounds: first angle/time derivatives are bounded by Cauchy using
the prescribed radii and polynomial coordinate envelope, harmonic degree
and retained-mode counts are polylogarithmic at those targets, and the
number of angle variables is fixed. This is weaker than the additional
small-node quadrature claim needed for total near-quadratic setup, which
the candidate explicitly does not prove internally.

## 6. Transported amplitude tangent and short-prefix analysis

The source proof uses mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,w)=\sqrt n\,u\) and
\(F_a=nf_a\). In these coordinates

\[
\dot\Theta=-\frac2m\sum_a r_a\nabla_\Theta F_a,
\qquad
D_\Theta r_a=\frac1n\nabla_\Theta F_a^T.
\]

Differentiating with respect to \(\zeta\) therefore gives exactly

\[
\dot U=-\left[
\frac2{mn}\sum_a\nabla_\Theta F_a\nabla_\Theta F_a^T
+\frac2m\sum_a r_aD_\Theta^2F_a
\right]U
+\frac2m\sum_a y_a\nabla_\Theta F_a,
\]

with zero initial tangent. Thus the factors in Section 6's Hessian,
variation-of-constants formula (21), and query derivative are correct.
The new query quantity contains the two-time propagator
\(\Phi(t,s)\). The current mixed source endpoint
\(D_\Theta z(t,v)\nabla_\Theta F_a(t)\) is instantaneous.
Although the finite-deletion proof already uses a variational propagator,
its existing estimates do not identify the new transported endpoint or
supply the claimed complex-amplitude bound.

For \(e=\partial_\zeta c\), differentiation of
\(\dot c=-2Qc\) gives
\(\dot e=-2Qe-2(\partial_\zeta Q)c\), with \(e(0)=y\).
Differentiating \(\dot\Theta=2m^{-1}\sum_a c_a\nabla F_a\)
gives the second identity in (22). These equations are compatible with
the previous tangent equation; they expose a possible damping mechanism
without proving it. The candidate requires complex fitting and an
improving stopped-domain coordinate bound, and correctly says that bounds
only on real amplitude derivatives do not establish this continuation.

For \(J=A+iB\) with real matrices \(A,B\), direct multiplication
gives
\(J^TJ=A^TA-B^TB+i(A^TB+B^TA)\). The imaginary term is
purely imaginary and symmetric, hence cancels in the Hermitian part.
The identity in Section 6 is exact. A gap conclusion would additionally
require quantitative control of \(B\); none is inferred for free.

The inherited residual estimate permits, for any fixed desired logarithmic
power, a sufficiently large constant in
\(t_0=O((m/\gamma)\log\log(en))\) to reduce residual RMS to
that inverse power. Its ratio to the original logarithmic horizon tends
to zero. With labels centered at the true anchor prediction, the anchor
is stationary at amplitude zero because its residual is zero, even with
nonzero readout. Its linearized dynamics use the full tangent Gram and
hidden coefficient order one can be present; the earlier parity-based
triangular ordering cannot simply be reused.

This is an exact stationary construction conditional on knowing the anchor.
The candidate does not prove that a numerical prefix provides a sufficiently
accurate anchor at the required cost. It correctly flags the missing
coordinate-sensitive analytic estimate and cavity comparison. A trained
anchor cannot be declared independently Gaussian, and cavity-centered
labels differ from full-network-centered labels in a root-dependent way.
The comparison must estimate that forcing difference. The stated generic
\(\sqrt n\) obstacle explains why a parameter-norm estimate alone
does not certify the proposed short prefix; it is not a no-go theorem
against more refined estimates.

## Claim boundary after this audit

The following distinctions survive the check:

- The hierarchy, finite function class, local analytic ball, and bivariate
  coefficient algorithm are proved finite constructions under their stated
  initialized-event assumptions.
- Continuing those coefficients to the actual labels with the favorable
  orders requires the new complex-label tube, on the full original label
  interval and an event uniform in requested accuracy. That tube is open.
- Polynomial or near-quadratic arithmetic conclusions are conditional on
  that tube and retain the separately charged activation backend; a complete
  near-quadratic setup further requires the stated quadrature and assembly
  accounting.
- The transported tangent system and short-prefix construction identify
  possible ways to attack the missing theorem. Neither proves the theorem,
  supplies a valid restart argument, or authorizes a hidden full dense rollout.

No must-fix change is required for the candidate to remain an explicitly
conditional research note. It must not be integrated as an unconditional
polynomial-setup theorem without resolving these recorded obligations.
