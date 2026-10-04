# Internal review of the initial-acceleration mechanism

**Verdict: PASS, with the gap direction and scope made explicit.** The exact
initial acceleration, its limiting expected energy, and a width-uniform
\(O(\varepsilon^2)\) remainder are valid under the stated initialization and
bounded-operator assumptions. The mixed model has the larger expected
acceleration energy. This supplies an actual initialized-learning discriminator
that the independent-Gaussian-probe return energy cannot detect.

The result is local in physical time and in second-layer scale. It does not
explain the experiments at \(\varepsilon=1\), establish a full trajectory gap,
or distinguish response memory from other methods with the same initial
read-in/readout dynamics. The q=1 memory correction vanishes at the derivative
order used here.

This review uses the assignment and the already-reviewed q=1 equations in
`TRAINING_PROTOCOL.md` (SHA-256
`2a622aaff0c6a61eff84bc58df8439cab6707a450d1c7a64be924d3cee5dcd08`).
It did not read another candidate note, another study, or external literature.
No source was edited. A small independent CPU differentiation check is saved
in `data/generated/response_memory_fast_mixing_20261002/training_review/initial_acceleration_cpu.json`.

## Exact initialized derivative

There is one training example \(x\in\mathbb R^d\), with
\(\|x\|_2=\sqrt d\), and label \(y\in\{-1,1\}\). Let
\(A\in\mathbb R^{n\times d}\), \(w,H,D\in\mathbb R^n\), and scalar
\(\tau\) be the q=1 state. The initialized matrix is \(W_0=\varepsilon M\),
where \(\varepsilon>0\), \(M\in\mathbb R^{n\times n}\) is independent of
(A(0)), and (A(0)) has independent (N(0,1)) entries. Write

\[
a(t)=A(t)x/\sqrt d,\quad h(t)=\tanh a(t),\quad
z(t)=W_0h(t)-\frac{2D(t)H(t)^\top h(t)}{n\tau(t)},
\quad g(t)=\tanh z(t),\quad f(t)=w(t)^\top g(t)/n.
\]

Use \(w(0)=D(0)=0\), \(H(0)=h(0)\), and \(\tau(0)=1\). Below,
\(a=a(0)\), \(h=h(0)\), \(z_0=\varepsilon Mh\), and

\[
D_g=\operatorname{diag}(1-h_i^2),\qquad
\psi(u)=\tanh(u)\operatorname{sech}^2(u).
\]

Thus \(a_i\) are independent standard Gaussians, and \(h_i=\tanh(a_i)\)
are independent, symmetric, centered, bounded variables. The symbol \(D_g\)
is a diagonal derivative matrix; it is distinct from the raw backward moment
\(D(t)\).

With residual \(r=f-y\), the physical equations give

\[
r(0)=-y,\quad \delta(0)=0,\quad \ell(0)=0,\quad
\dot A(0)=\dot h(0)=\dot D(0)=0,\quad
\dot w(0)=2y\tanh(z_0).
\]

The remaining initial derivatives are \(\dot H(0)=h\) and
\(\dot\tau(0)=1\), since \(\rho(0)=|r(0)|=1\). The initial residual is
nonzero, so the residual absolute value creates no differentiability problem
in a neighborhood of the initial state.

Because \(w(0)=0\), differentiating
\(\delta=w\odot(1-g^2)\) gives

\[
\dot\delta(0)=2y\psi(z_0).
\]

Both the memory term and its first derivative vanish in the backward action:
it contains \(H(D^\top\delta)/(n\tau)\), with \(D(0)=\delta(0)=0\).
The derivative of the outer first-layer gate also multiplies a zero backward
action at time zero. Hence

\[
\dot\ell(0)=2y\varepsilon D_gM^\top\psi(\varepsilon Mh).
\]

Using \(\dot A=-2r\ell x^\top/\sqrt d\), \(\ell(0)=0\), and \(y^2=1\),

\[
\ddot A(0)=4\varepsilon D_gM^\top\psi(\varepsilon Mh)
\frac{x^\top}{\sqrt d}.
\]

Since \(\|x\|_2^2/d=1\), multiplying by \(x/\sqrt d\) introduces no extra
factor. Finally \(\dot a(0)=0\), so the second derivative of tanh contributes
only its first derivative times \(\ddot a(0)\). Therefore

\[
\boxed{\ddot h(0)=4\varepsilon D_g^2M^\top\psi(\varepsilon Mh).}
\]

There is no missing factor of \(n\): the supplied physical readout and read-in
mobilities already absorb the (1/n) output normalization. For a different
input norm or label magnitude, those extra factors would need to be restored;
the present statement uses the specified normalization and \(y^2=1\).

## Expected weak-scale limit

Define \(S=M^\top M\) and

\[
J_\varepsilon(M)=\frac{\mathbb E_a\|\ddot h(0)\|_2^2}
{16\varepsilon^4n}
=\frac1n\mathbb E_a\left\|D_g^2M^\top
\frac{\psi(\varepsilon Mh)}{\varepsilon}\right\|_2^2.
\]

For one independent standard normal \(Z\), define

\[
\nu=\mathbb E\tanh^2Z,\qquad b=\mathbb E(1-\tanh^2Z)^4,\qquad
c=\mathbb E[(1-\tanh^2Z)^4\tanh^2Z].
\]

Since \(\psi'(0)=1\), the candidate leading energy is

\[
J_0(M):=\frac1n\mathbb E_a\|D_g^2Sh\|_2^2.
\]

For each row \(i\), expand

\[
\mathbb E(1-h_i^2)^4\left(\sum_jS_{ij}h_j\right)^2.
\]

Cross terms with \(j\ne k\) vanish: at least one centered independent factor
appears to the first power. The \(j=k=i\) term is \(cS_{ii}^2\); each
\(j=k\ne i\) term is \(\nu b S_{ij}^2\). Since \(S\) is symmetric,

\[
\boxed{J_0(M)=c\,\frac1n\sum_iS_{ii}^2
+\nu b\left[\frac{\operatorname{tr}(S^2)}n
-\frac1n\sum_iS_{ii}^2\right].}
\]

This calculation is conditional on deterministic \(M\). It therefore also
holds conditionally for a random \(M\) independent of \(a\). Independence is
essential to this factorization; it is not an arbitrary adaptive-state
identity.

## A width-uniform error bound

The small-ε expansion can be justified with an explicit bound rather than
interchanging limits formally. For all real \(u\),

\[
|\psi(u)|\le|u|,\qquad
|\psi(u)-u|\le\frac43|u|^3.
\]

For the second inequality, use
\(\psi(u)=\tanh u-(\tanh u)^3\),
\(|\tanh u|\le|u|\), and

\[
|u-\tanh u|=\int_0^{|u|}\tanh^2 t\,dt
\le |u|^3/3.
\]

Assume \(\|M\|_{\mathrm{op}}\le C\), uniformly in \(n\). Independence,
symmetry, and \(|h_j|\le1\) imply

\[
\mathbb E|(Mh)_i|^6\le15\|M_{i,:}\|_2^6.
\]

For completeness, expansion of the sixth power leaves only multiplicity
patterns (6), (4+2), and (2+2+2), with coefficients (1,15,90).
All contributing moments of \(h_j\) are at most one. These terms are bounded
coefficientwise by the expansion of
\(15(\sum_jM_{ij}^2)^3\). No separate moment assumption is being imported.

Let \(v=Mh\),
\(u_\varepsilon=D_g^2M^\top\psi(\varepsilon v)/\varepsilon\), and
\(u_0=D_g^2M^\top v\). Since \(\|D_g^2\|_{\mathrm{op}}\le1\),

\[
\left(\frac1n\mathbb E\|u_\varepsilon-u_0\|_2^2\right)^{1/2}
\le\frac{4\sqrt{15}}3 C^4\varepsilon^2,
\qquad
\left(\frac1n\mathbb E\|u_\varepsilon+u_0\|_2^2\right)^{1/2}
\le2C^2\sqrt\nu.
\]

The first bound uses \(\|M_{i,:}\|\le C\), and the second uses
\(\mathbb E\|Mh\|^2=\nu\|M\|_F^2\le\nu nC^2\).
Cauchy–Schwarz applied to the difference of squared norms proves

\[
|J_\varepsilon(M)-J_0(M)|
\le\frac{8\sqrt{15}}3 C^6\sqrt\nu\,\varepsilon^2.
\]

For the comparison in the assignment, the normalization
\(\|M\|_F^2/n=1\) improves this to

\[
\boxed{|J_\varepsilon(M)-J_0(M)|\le K\varepsilon^2,
\qquad K=\frac{8\sqrt{15}}3 C^4\sqrt\nu.}
\]

Indeed, \(n^{-1}\sum_i\|M_{i,:}\|^6\le C^4\), and
\(n^{-1}\mathbb E\|Mh\|^2=\nu\). These replace the preceding bounds by
\((4\sqrt{15}/3)C^3\varepsilon^2\) and \(2C\sqrt\nu\), respectively.
The result is uniform in dimension, left/right orthogonal bases, and every
normalized singular array with operator norm at most \(C\).

This proof derives a sixth-moment bound for an **initial independent bounded
linear field**. It does not establish sixth moments for a general adaptive
backward field later in training. The distinction should remain explicit.

## Mixed and unmixed bases: exact sign and finite-width conclusion

Take orthogonal \(U,V\in\mathbb R^{n\times n}\), with
\(|V_{ij}|=1/\sqrt n\), and nonnegative singular values satisfying
\(n^{-1}\sum_i s_i^2=1\). Define

\[
M_{\mathrm{mix}}=U\operatorname{diag}(s)V^\top,\qquad
M_{\mathrm{unmix}}=U\operatorname{diag}(s),\qquad
\mu_4=\frac1n\sum_i s_i^4.
\]

The flat entries of \(V\), which may be a signed/permuted normalized Hadamard
matrix, imply \((M_{\mathrm{mix}}^\top M_{\mathrm{mix}})_{ii}=1\).
For the unmixed matrix that diagonal is \(s_i^2\). Both have
\(n^{-1}\operatorname{tr}(S^2)=\mu_4\), so

\[
J_0(M_{\mathrm{mix}})=c+(\mu_4-1)\nu b,\qquad
J_0(M_{\mathrm{unmix}})=\mu_4c.
\]

Thus the assignment's negative gap is specifically

\[
J_0(M_{\mathrm{unmix}})-J_0(M_{\mathrm{mix}})
=(\mu_4-1)(c-\nu b).
\]

To prove strict negativity, let \(X=\tanh^2Z\), let (X') be an independent
copy, and put \(F(x)=(1-x)^4\). Then

\[
c-\nu b=\operatorname{Cov}(X,F(X))
=\frac12\mathbb E[(X-X')(F(X)-F(X'))]<0.
\]

The law of \(X\) is nondegenerate, and \(F\) is strictly decreasing on
([0,1)). Therefore the gap is strictly negative whenever \(\mu_4>1\).
For a flat spectrum, or the normalized \(n=1\) case, \(\mu_4=1\) and no
separation is asserted.

If \(\mu_{4,n}\to m_4>1\) and the operator norms are uniformly bounded,
write \(\Delta=(m_4-1)(\nu b-c)>0\). For all sufficiently large \(n\), the
leading mixed-minus-unmixed gap is at least \(\Delta/2\). The uniform remainder
then gives, whenever \(0<\varepsilon^2\le\Delta/(8K)\),

\[
J_\varepsilon(M_{\mathrm{mix}})-J_\varepsilon(M_{\mathrm{unmix}})
\ge\Delta/4>0.
\]

Quarter-circle quantiles with RMS normalization satisfy \(m_4=2\) and a
uniform singular-value bound. Thus this is a separation for every sufficiently
small fixed positive ε at all sufficiently large widths. It does not require
or, by itself, prove individual large-width limits of \(J_\varepsilon\) for
an arbitrary sequence of orthogonal bases at fixed nonzero ε.

For numerical orientation only, Gaussian quadrature gives
\(\nu\approx0.39429449\), \(b\approx0.34150921\), and
\(c\approx0.03378319\). For \(m_4=2\), the weak-scale limits are approximately
0.16843839 mixed and 0.06756637 unmixed; their difference is 0.10087201.
The strict sign above is analytic and does not depend on quadrature accuracy.

## What is isolated, and what remains outside the result

The pair has exactly the same left covariance,

\[
M_{\mathrm{mix}}M_{\mathrm{mix}}^\top
=M_{\mathrm{unmix}}M_{\mathrm{unmix}}^\top
=U\operatorname{diag}(s^2)U^\top,
\]

and exactly the same singular spectrum. For an independent Gaussian probe,
the nonlinear return energy is invariant under right orthogonal multiplication:
rotate the Gaussian probe and use invariance of the output norm. Therefore
that entire independent-Gaussian-probe diagnostic is identical for the pair,
even though the actual initialized feature-acceleration energy differs.
For the actual non-Gaussian initial feature \(h=\tanh a\), its mean is zero
and covariance is \(\nu I_n\), so the second-layer **preactivation** covariance
\(\mathbb E[z_0z_0^\top]=\varepsilon^2\nu MM^\top\) also agrees exactly.
This does not establish equality of the full non-Gaussian forward law or of
the post-tanh feature covariance.

The mechanism is explicit in the leading formula. In the unmixed case,
\((Sh)_i=s_i^2h_i\), so the returned field is paired with its own nonlinear
gate \((1-h_i^2)^4\); their negative covariance suppresses energy. Mixing moves
part of the returned energy into contributions from other coordinates, whose
initial features are independent of the local gate, replacing \(c\) by the
larger product \(\nu b\). This isolates a concrete initial gate/return
interaction that singular values and an independent Gaussian probe overlook.

It does not prove equality of every other initial forward statistic, nor is
such equality needed for the computed derivative. The exact calculation is
stronger than inferring this interaction solely from a later Gram discrepancy,
but weaker than a claim that it uniquely explains the full empirical training
gap at scale one.

Additional boundaries are essential:

- The statement concerns expectation over initialized first-layer Gaussian
  rows. It is not a concentration theorem for a single network.
- The absolute acceleration energy per coordinate has the prefactor
  \(16\varepsilon^4\). Its normalized separation should not be presented as
  an order-one absolute effect as ε tends to zero.
- It concerns the continuous physical vector field at initialization. A
  finite-step Heun or positive-time consequence needs its own discretization
  or temporal remainder statement.
- The memory term contributes zero at this order. The same mechanism occurs
  when only read-in/readout weights learn around fixed \(W_0\), and in other
  models whose initialized dynamics agree through this derivative. It is not
  a response-memory-exclusive phenomenon.
- The uniform small-scale estimate gives no conclusion at ε equal to one
  unless its quantitative bound or another argument actually reaches that
  scale. It also says nothing about fitting, generalization, or a full-horizon
  separation.

A CPU float64 automatic directional-derivative check of the full q=1 RHS at
\(n=7,d=4,y=-1,\varepsilon=0.13\) agreed with the displayed acceleration to
\(1.74\times10^{-18}\). This is a sanity check; the derivation and uniform
bound above provide the mathematical justification.

## Candidate and implementation addendum

The subsequently supplied candidate and producer were read and hashed before
this additional audit:

| Input | SHA-256 |
|---|---|
| `INITIAL_ACCELERATION.md` | `18782aedaa1a1744acf7647553443bd3644b947488796b76bd4ad6136974ddc5` |
| `check_initial_acceleration.py` | `01e7d884487cc0f4594231708d68d77d7b30abb93a9e68702e8f3d9bf481e517` |
| `acceleration02/results.json` | `0a9d69175b7a590f6d71dbc1ed2a8917c6bf4f879a74c56bdbfb603f07e9d7ef` |

The candidate's formulas and small-scale conclusion agree with the independent
derivation above. Its fixed-finite-system statement
\(\|h(t)-h(0)\|^2/(nt^4)\to\|\ddot h(0)\|^2/(4n)\) is valid because
\(\dot h(0)=0\) and the local trajectory is twice differentiable. It does
not assert a width-uniform positive-time remainder.

The implementation represents \(M_{\mathrm{mix}}=H\operatorname{diag}(s)H\)
and \(M_{\mathrm{unmix}}=H\operatorname{diag}(s)\) correctly, where here \(H\)
is the normalized Hadamard matrix, not the stored memory. The mixed operator
is symmetric in this particular test, so using its forward routine as its
transpose is correct. The unmixed transpose has the factors reversed.
The factor `(1-h*h)**2` is squared by the final energy calculation, yielding
the required fourth power of the first-layer derivative. The nonzero-scale
response is exactly \(\psi(\varepsilon Mh)/\varepsilon\).

Its paired Gaussian-probe check rotates the input appropriately, making the
two forward vectors equal before comparing return norms. This tests the exact
right-orthogonal invariance, rather than comparing two noisy empirical means.
The Monte Carlo initial rows are independent within the prescribed batch and
paired between the two matrices and scales. Reported standard errors use those
initializations as the sampling units. The four-standard-error check is a
numerical acceptance rule, not a finite-sample probability certificate.

The unchanged producer was rerun into the fresh
`data/generated/response_memory_fast_mixing_20261002/acceleration_review/`
directory under a 9-second external timeout. It finished in 2.81 recorded
seconds. **Every field of the original result except elapsed runtime matched
exactly**, including all means, standard errors, quadrature results, and source
hashes. The finite-width linear predictions are 0.1684176280 mixed and
0.0675611665 unmixed; both simulated means pass the declared four-error rule.
Covariance and paired Gaussian-probe discrepancies are respectively
\(6.66\times10^{-16}\) and \(2.25\times10^{-16}\).

At \(\varepsilon=1\), the reproduced means are 0.0510125526 mixed and
0.0206452056 unmixed, with paired unmixed-minus-mixed gap
(-0.0303673469) and standard error \(7.42\times10^{-5}\). This is a
descriptive initial-acceleration result for the chosen \(n=256,U=V=H\)
case. It does not turn the uniform small-scale theorem into a scale-one
theorem or explain a finite training horizon.

The corrected SciPy 256/512-node quadrature agrees to
\(1.63\times10^{-13}\), below the retained \(10^{-8}\) threshold. The
candidate transparently records the original 128/256-node failure and the
pre-Monte-Carlo repair. This review confirms the repaired calculation; it did
not separately inspect the earlier failure directory or certify its chronology.
No spectrum, sample count, scale, or numerical criterion was changed by the
reviewer.

The exact independent physical-time JVP oracle has also been saved as
`acceleration_review/jvp_oracle.py`, with its result and source hash in
`jvp_results.json`. It differentiates the complete raw-moment RHS in the
direction of its initial velocity, and recovers \(\ddot h(0)\) through the
first-layer chain rule. It does not import the candidate's acceleration
implementation. The rerun and oracle used CPU only and together remained
below the additional 10-second CPU allowance.
