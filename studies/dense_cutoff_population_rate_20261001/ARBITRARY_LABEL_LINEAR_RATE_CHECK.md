# Complete internal reconstruction of the arbitrary-label linear population rate

2026-10-03. **Verdict: INTERNAL PASS for the theorem as stated.**

The frozen candidate `ARBITRARY_LABEL_LINEAR_RATE.md`, SHA-256
`56e6dfaadb443353307b99984d5eb6672bc20ab2ad7ff33256b0327ccf8b4ab7`, proves
strict \(n^{-1/2}\) convergence to the canonical dense population predictor
for two hidden identity-activation layers, one normalized training input,
arbitrary fixed labels, canonical independent Gaussian initialization,
exactly zero initial readout, and canonical feature-learning mobilities.
The norm includes the full physical-time supremum inside the query integral;
the query law needs only a second moment. The theorem is at fixed confidence,
with an explicitly bounded exceptional event. It does not assert an
unconditional all-time mean-square bound over that event.

No mathematical repair is required. This is collaborative internal checking,
not an isolated promotion review. The checker authored the geometry route
and saw the supervisor's preliminary spectral and Wick-moment ideas before
the candidate was frozen. No promotion or manuscript edit is authorized or
performed by this check.

## 1. Complete read scope and method

I read all 407 lines of the frozen candidate, including every displayed
equation, its provenance, and all seven sections. I reconstructed all
nontrivial proof steps from its stated hypotheses. Additional authorized
inputs were:

- The checker's complete `ARBITRARY_LABEL_GEOMETRY_ROUTE.md`, which proves
  the finite-target energy argument and conditional Gaussian passive law.
- The canonical equations and population description in `paper/main.tex`,
  including the setting and population paragraphs.
- The complete fixed-Gaussian-computation lemma, its proof, and the
  population-operator completion in `paper/proof_alltime.tex`, lines
  340--505. The small-label dynamical theorem is not used at large labels.
- The complete 349-line `POPULATION_RESPONSE_TRANSPORT.md`. Only the bounded
  initialized-operator construction is relevant to the candidate; its later
  small-label nonlinear stability argument is not a dependency of this
  theorem. A finite operator bound from the manuscript already suffices;
  the exact norm bound two is not needed for the rate proof.
- Previously read required mathematical-notation, rigorous-proof, and
  adversarial-audit instructions, and the permitted large-label source and
  check. No other study, experiment, or external random-matrix theorem was
  consulted.

The method was exact algebraic and analytic reconstruction: mobility
normalizations, continuation in finite and Hilbert spaces, every Wick
contraction count, coefficient majorization and infinite summation,
stopped feedback comparison, physical-time damping, and conditional Gaussian
query integration. No training or numerical experiment was run. The candidate
hash was checked before and after reconstruction; the candidate was not
edited. The final report records that hash to identify precisely which
argument passed. Additional source hashes at reconstruction were:

```text
ARBITRARY_LABEL_GEOMETRY_ROUTE.md: 414a766ac02a67660e0efc0c8f0d09f7c8c01e8ee53c4a3c1dab6f706c2d95fa
POPULATION_RESPONSE_TRANSPORT.md: a339eace94acdc797daade3bcc8f58a8c730f720dbb2d9e06c29cba6da3b925c
paper/main.tex: 60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95
paper/proof_alltime.tex: f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d
```

## 2. Canonical normalization, balances, and scalar geometry

With \(a=A x_0/\sqrt d\), \(v=a/\sqrt n\), and \(u=w/\sqrt n\),
the canonical physical flow is exactly the controlled system
\[
 u'=Wv,\qquad v'=W^\top u,\qquad W'=uv^\top
\]
multiplied by \(ds/dt=2(Y-P_n)\). In particular the hidden mobility is
one in the original coordinates: \(W'=wa^\top/n\). The prediction is
\(P_n=u^\top Wv\). No factor of \(n\), \(m\), or two is missing.

Differentiating gives
\[
 (WW^\top)'=uv^\top W^\top+Wvu^\top=(uu^\top)',
 \qquad (\|v\|^2)'=(\|u\|^2)'=2u^\top Wv.
\]
Since \(u(0)=0\), the balances in candidate (4) follow. Differentiating
\(u'=Wv\) and substituting both balances gives
\[
 u''=(W_0W_0^\top+(q_n+2\|u\|^2)I)u,
 \qquad u'(0)=W_0v(0).
\]
The coefficient \(2\|u\|^2\) is the exact contribution of trained
parameters. This retains full hidden feature learning.

The control vector field is the Euclidean gradient of \(P_n\) in the
normalized variables \((u,v,W)\). Thus
\(P_n'=\|u'\|^2+\|v'\|^2+\|W'\|_F^2\). For \(R=\|u\|>0\),
\(R'=P_n/R\) and \(R''\ge0\). At zero the right derivative is
\(\sqrt{Q_n}\), where \(Q_n=\|W_0v(0)\|^2\). This establishes
\(P_n'\ge Q_n\) without division by zero at initialization.

For any finite output bound \(H\), integrated squared velocity is at
most \(H\). On a control interval of length at most \(U\), each
parameter displacement is at most \(\sqrt{UH}\). If a maximal controlled
interval ended before the target, the remaining path would be Cauchy by
the bound \(\sqrt{H(s-r)}\); its polynomial vector field would extend
from the finite limit. This validates continuation up to a finite target
without assuming the unrestricted controlled curve exists globally.

The same proof works in the product Hilbert space of two vector fields
and a Hilbert--Schmidt hidden increment: bounded operator actions and
rank-one products are locally Lipschitz there. The initialized hidden
operator is fixed and bounded. The population continuation argument does
not require it to be Hilbert--Schmidt.

## 3. All-order Wick estimates

Write \(B=W_0^\top W_0\) and \(p=k+1\). Direct multiplication gives
\[
 \nu_{n,k}=\frac1n a_0^\top B^p a_0.
\]
The first-root vector \(a_0\) is independent standard Gaussian and
independent of \(W_0\), as required by the canonical initialization.

For a normalized trace of \(B^p\), a Wick pairing of its \(2p\)
matrix-entry occurrences contributes \(n^{V-p-1}\), where \(V\)
is the number of distinct formal row/column index classes after the
pairing's identifications. The quotient of the original closed walk is
connected. It has at most \(p\) distinct edges, so \(V\le p+1\).
This counts row and column vertices separately, even though both have
\(n\) possible numerical values.

When \(V=p+1\), the quotient is a tree with \(p\) distinct edges.
The length-\(2p\) closed walk traverses each edge exactly twice, once
in each direction. Each traversal returning toward the root closes the
last still-open edge, giving a Dyck path and a noncrossing pairing.
Conversely a noncrossing pairing gives exactly \(p+1\) vertex classes:
remove an adjacent paired pair recursively; its middle vertex is new and
its two outer indices are identified. This is an induction on \(p\),
starting from the one-vertex empty walk. Hence exactly \(C_p\) pairings
contribute one.

Every other pairing contributes at most \(1/n\); all contributions are
nonnegative. There are \((2p-1)!!\le(2p)^p\) pairings. The bias bound
in candidate (11) is consequently valid for every \(p,n\), not only for
fixed order or asymptotically large widths. Allowing accidentally equal
numerical values for distinct formal vertices changes none of these sums:
there are exactly \(n^V\) assignments, with no distinctness requirement.

For two normalized trace walks, all pairings without a cross-walk pair
cancel with the product of expectations. Every remaining pairing merges
the two connected walks into one connected quotient. It has at most
\(2p\) edges and \(2p+1\) vertices. Including both trace normalizations,
its contribution is at most \(n^{-1}\). Counting all pairings by
\((4p-1)!!\le(4p)^{2p}\) proves candidate (12). This deliberately loose
bound needs no genus expansion or restriction on the order.

Conditionally on \(W_0\), diagonalizing \(B^p\) and using independent
Gaussian squares gives
\[
 \mathbb E[\nu_{n,k}\mid W_0]=\operatorname{tr}(B^p)/n,
 \qquad
 \operatorname{Var}(\nu_{n,k}\mid W_0)
       =2\operatorname{tr}(B^{2p})/n^2.
\]
The expectation of the conditional variance is bounded by
\(2(4p)^{2p}/n\), since each normalized one-trace pairing contributes
at most one. Total variance, followed by the preceding bias bound, yields
\[
 \|\nu_{n,k}-C_{k+1}\|_{L^2}
       \le C(4(k+1))^{k+1}/\sqrt n.
\]
Also \(q_n=n^{-1}\sum_i a_{0,i}^2\) has mean one and variance
\(2/n\). The stated all-order estimates are correct.

The operator event follows from the specified two sphere nets:
\(\|W_0\|\le2\max|u^\top W_0v|\), each pairing is Gaussian with
variance \(1/n\), and there are at most \(81^n\) pairs. Choosing fixed
\(K\) with \(K^2/8>\log81\) gives an exponential failure bound.

## 4. Population identification and an independent continuation check

The measure
\[
 d\nu(\lambda)=\frac1{2\pi}\sqrt{\lambda(4-\lambda)}
           \mathbf1_{(0,4)}d\lambda
\]
has mass one. Substitution \(\lambda=4r\) gives the beta integral in
the candidate and its value \(C_{k+1}\), including \(k=0\).

The manuscript fixed-program lemma applies to every fixed alternating
word in \(W_0,W_0^\top\) acting on the Gaussian first root. Every
instruction is linear. Its same-layer second-moment convergence identifies
the limiting polynomial pairings; the candidate's Wick bound identifies
their values as the displayed Catalan numbers. This step uses only fixed
programs, with no growing-program or finite-time approximation assertion.

In the canonical population, \(T=W_0W_0^*\) is positive self-adjoint
and bounded, and \(b_0=W_0a_0\) is a vector of norm one. Its spectral
measure has the same moments as \(\nu\). Both measures have compact
support. Polynomial approximation of continuous functions on a common
compact interval therefore identifies the measures. Equivalently, the
polynomial cyclic subspace is isometric to polynomials in \(L^2(\nu)\).
The isometry intertwines \(T\) with multiplication by \(\lambda\).
The second-order ODE preserves that cyclic subspace because its remaining
coefficient is scalar. Thus the scalar equation represents the canonical
population trajectory, rather than a separate phenomenological model.

As an independent check, one can prove population continuation directly
from the scalar representation, without using the product-Hilbert argument.
The state \((\psi,\psi')\) lies in \(L^2(\nu)^2\), and multiplication
by \(\lambda\in[0,4]\) is bounded. Its cubic vector field is locally
Lipschitz. Set
\(R^2=\int\psi^2d\nu\) and \(P=\int\psi\psi'd\nu\).
Differentiation proves the conserved identity
\[
 \int(\psi')^2d\nu-\int(\lambda+1)\psi^2d\nu-R^4=1.
\]
It gives the stronger exact relation
\[
 P'=1+2\int(\lambda+1)\psi^2d\nu+3R^4\ge1,
 \qquad (R^2)'=2P.
\]
If \(0\le P\le H\) and \(0\le s\le U\), then
\(R^2\le2UH\); the conserved identity bounds
\(\int(\psi')^2d\nu\le1+10UH+4U^2H^2\). The bounded state and
locally Lipschitz vector field continue the scalar solution. Since
\(P'\ge1\), every finite output target is reached. This verifies
large-label population existence independently and requires no extension
of a small-label theorem beyond its hypotheses.

## 5. Analytic coefficients, random potentials, and bias summation

For nonnegative continuous potential \(a(s)\le A_Y\), the scalar
Volterra equation is
\[
 \psi_a(s,\lambda)=s+
        \int_0^s(s-v)(\lambda+a(v))\psi_a(v,\lambda)dv.
\]
Its iterated coefficients in \(\lambda\) are nonnegative; replacing
\(a\) by the constant \(A_Y\) increases every coefficient of both
\(\psi_a\) and \(\psi_a'\). The constant-potential solutions are the
hyperbolic-sine and hyperbolic-cosine series used in the candidate.
In their coefficients, the inequalities
\[
 \binom{k+r}{r}\le\binom{2k+2r+1}{2r},\qquad
 \binom{k+r}{r}\le\binom{2k+2r}{2r}
\]
give the two stated bounds, respectively. Summing the remaining even
series supplies the common \(\cosh(U\sqrt{A_Y})\) factor.

Convolving the reciprocal odd/even factorials gives a binomial sum.
For \(\psi_a^2\), its total factorial index is \(2k+2\); for
\(\psi_a\psi_a'\), it is \(2k+1\). Bounding the binomial sum by
the full power of two yields coefficients at most
\(C_Y B_Y^k/(2k)!\), uniformly in \(s\le U\) and in the complete
class of permitted potentials. The coefficient bound is uniform over
the realized finite potential; it does not require that potential to be
independent of \(\nu_n\).

The moment-error sum \(E_n\) is a well-defined nonnegative \(L^2\)
random variable. Minkowski's inequality and the all-order moment estimate
bound its norm by \(C_Y/\sqrt n\), because the successive ratio of
\[
 \frac{B_Y^k(4(k+1))^{k+1}}{(2k)!}
\]
tends to zero. Finite partial sums first establish the bound; monotone
convergence and completeness of \(L^2\) justify the infinite sum.

For every actual finite potential, integrating its product series against
\(\nu_n\) and \(\nu\), then subtracting termwise, costs at most
\(C_YE_n\). On the operator event each measure has compact support;
the entire series converges there absolutely. The same conclusion follows
from nonnegative coefficients and the moment bounds. There is no
interchange of an uncontrolled limit, nor an assumption that expectation
commutes with the nonlinear trained dynamics.

This step controls initialization bias as well as fluctuations. The proof
compares with the fixed measure \(\nu\) and fixed value \(q=1\), not
with a width-dependent mean or concentration center.

## 6. Bounded-output bootstrap and equal physical times

The population time \(U\) is selected by \(P(U)=Y+1\), so
\(U\le Y+1\). Stop the finite curve at \(U\) or \(P_n=Y+2\).
Before that stop, candidate (6) gives a width-independent state tube from
\(q_n\le2\) and \(\|W_0\|\le K\). In particular both scalar
potentials are bounded by a deterministic \(A_Y\). The proof never
assumes existence of the finite controlled path past its fitted point
without an accompanying output bound.

On \(\lambda\in[0,4]\), first-order-system subtraction gives candidate
(20). Separate the measure error using the just-proved uniform coefficient
bound, then integrate the scalar solution difference under \(\nu\).
For \(D(s)=|R_n(s)^2-R(s)^2|\), this gives
\[
 D(s)\le C_YE_n+C_Y\int_0^sD(v)dv.
\]
Gronwall controls \(D\), and the same product comparison controls
\(P_n-P\), proving (21).

If \(C_YE_n<1/2\), exiting at \(P_n=Y+2\) contradicts
\(P\le Y+1\). Bounded-output continuation excludes an earlier
singularity. The finite curve therefore exists through \(U\), where
\(P_n(U)>Y\). For sufficiently small \(E_n\), its zeroth-moment
term also gives \(Q_n\ge1/2\). The failure probability is bounded
by \(C_Y/n+Ce^{-cn}\): Chebyshev applied to \(E_n\) and \(q_n\),
and the initialized operator event suffice.

Both physical clocks remain inside \([0,U]\). Their difference obeys
\[
 \frac d{dt}(s_n-s_\infty)
 =-2a(t)(s_n-s_\infty)
      -2[P_n(s_\infty)-P(s_\infty)],\qquad a(t)\ge1/2.
\]
Integrating its damping kernel gives
\(\sup_t|s_n-s_\infty|\le2\sup_{s\le U}|P_n-P|\).
The population derivative \(P'\) is bounded on this compact controlled
interval. Thus the predictions agree to \(C_YE_n\) at equal physical
times, uniformly through infinity. This is not merely an error estimate
after aligning different network clocks.

## 7. Passive queries and the final probability statement

The first-weight columns orthogonal to \(x_0\) are independent standard
Gaussians conditional on the training roots. Their physical updates are
zero as an exact consequence of the one-sample outer-product update.
Equation (23) has the correct normalization: its passive term is
\(n^{-1/2}a_j^\top W^\top u\), with \(u=w/\sqrt n\).

For \(\beta=W^\top u\), direct differentiation gives
\[
 \beta'=v\|u\|^2+W^\top Wv.
\]
The controlled tube bounds this derivative by a width-independent
constant. The process starts at zero. Conditional on the training roots,
the fundamental theorem of calculus and Cauchy--Schwarz therefore yield
candidate (24). Gaussian independence supplies exactly
\(\sum_j b_j(x)^2\|\beta'(s)\|^2\) as its second moment, without an
extra factor of the ambient neuron dimension.

The good event depends only on the training roots and hence preserves
this conditional calculation. Tonelli applies to the nonnegative
time-supremum integrands. Both the training coefficient
\(c(x)^2\) and the passive coefficient \(\sum_jb_j(x)^2\) are bounded
by \(\|x\|^2/d\), so a second query moment is exactly sufficient.
Combining with \(\mathbb E E_n^2\le C_Y/n\) proves candidate (26).

For fixed \(\delta>0\), take width large enough that the bad-event
probability is at most \(\delta/2\), then apply Markov to the truncated
mean-square bound with threshold \(C_{\delta,Y,\mu}/\sqrt n\).
This proves the claimed unconditional fixed-confidence statement for the
actual unclipped flow. It does not discard a bad event inside an
unrestricted expectation.

The zero-label case is stationary. Negative labels use the exact
readout-sign symmetry. In input dimension one there is no passive
component; the training proof still applies. At the fitted endpoint both
training predictions equal the label, giving
\(f_\infty(\infty,x)=yx_0^\top x/d\). All constants may depend on
the fixed label, fixed input geometry, dimension, and query second moment;
none depends on width or physical time.

## 8. Claim boundary

The strict full-population rate is proved for the stated two-hidden-linear-
layer, one-training-input class. The proof retains canonical initialization,
trained hidden weights, equal physical times, and the complete passive-query
norm. It supplies both a quantitative deterministic population comparison
and an all-time fitting argument at arbitrary fixed labels.

It gives no slower-rate counterexample, no general nonlinear multi-sample
theorem, and no label-uniform constants as \(|y|\to\infty\). It is stronger
than concentration around a finite-width center within its special class,
because the common spectral population measure is identified and its
initialization error is quantitatively controlled. No unresolved defect
remains in the theorem at the reviewed hash.
