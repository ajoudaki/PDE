# Independent internal check of the smooth auxiliary routes

2026-10-01. **Verdict: the stated auxiliary results pass this check.**
No substantive mathematical error was found in the smooth initialized
fitting argument, unconditional finite-time estimates, scalar monotonicity
result, cubic initial coefficient and its mean formula, proof-method
counterexamples, or abstract restoration lemma. The covariance-interpolation
construction is valid, with the needed signed estimate explicitly unproved.
These conclusions do not prove the full population theorem or its
all-initialization all-time second moment.

## Scope and complete versions

The supervisor assigned the complete smooth all-initialization and
interpolation routes, the exact setup, and the restoration lemma. After a
concrete dependency request, the supervisor also authorized the complete
three hard-clip inputs supplying the tail calculation, block joining and
extension, and fixed-polynomial profile theorem. All seven files below were
read in full. Previously read same-study fitting, concentration, cavity,
weighted-remainder, and population inputs remained available. No sibling
mean-map results, prior auxiliary-review verdicts, other study, archive,
manuscript, experiment, or Git history was read. Only this report was written.

| Complete input | Lines | SHA-256 |
|---|---:|---|
| `SMOOTH_SETUP.md` | 93 | `a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6` |
| `SMOOTH_ALLINIT_ROUTE.md` | 325 | `db8b43883fb81c4e1afc3cb9961620bfda5b5ed0933f55ec57e422085b16ee8a` |
| `SMOOTH_INTERPOLATION_ROUTE.md` | 356 | `e534be2bc75db0f27eba6f8752d0593b4dd1e8dfad382eae1c325c42be5522e8` |
| `SMOOTH_RESTORATION.md` | 124 | `71e68a479072501e9fabee0b7f77256858584a9606ddbd993bb145d46470fc43` |
| `UNCONDITIONAL_TAIL_ROUTE.md` | 277 | `76400cfe15351b7c35305808958fd9df3cae4c918bbeab2f3172325d187bd6ed` |
| `BIAS_DIMENSION_ROUTE.md` | 548 | `760ba8c8fbd1dbcf7c5c92982eff1499e185fb88296931b7dbaf84d0f106f005` |
| `RESOLUTION_INTERPOLATION_ROUTE.md` | 330 | `f21b1fe75e739d068eabd093e5c737e70d407153a4f3ba1997dfa1746b3799fe` |

The reused fitting, concentration, and population versions are respectively
`edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2`,
`4331e895f388b238ced358cfa101390b80681c3797fa36b5b8ba7e319312d8f5`,
and `63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082`.
The assigned smooth files remained unchanged on the post-reading hash check.
The already-read rigorous-math, canonical-notation and neural-response, and
conjecture-investigation/adversarial-audit instructions were retained.

## 1. Smooth fitting, actual derivatives, and exceptional initializations

Write \(\psi=\operatorname{sech}^2\),
\(c_M(s)=M\tanh(s/M)\),
\(p_a=w\odot\psi(z_a)\), and \(d_a=c_M(p_a)\).
The residual is \(r_a=f_a-y_a\), its RMS is
\(\rho=\|r\|_2/\sqrt m\), and
\(S(t)=\int_0^t\rho(s)\,ds\).

The smooth fitting proof uses \(|c_M(s)|\le|s|\), bounded forward
activations, and the readout Gram. The derivation of
\(\dot r=-2\Gamma r+e\), with
\(e_a=p_a^\top\dot z_a/n\), correctly retains the ordinary output
derivative. The estimates
\(\|B-W_0\|_F\le2S^2\),
\(\|\dot z_a\|_2/\sqrt n\le C_hS\rho\), and
\(\|\Gamma(t)-\Gamma(0)\|_{\rm op}\le C_hS^2\)
give \(\dot\rho\le(-2\lambda+4C_hS^2)\rho\).
With the stated \(s_*\) and label restriction, the activity stop is
strictly excluded. No symmetric full-gradient Gram or smooth top-inactivity
claim is used.

The discrepancy calculation in all-initialization equation (7) is correct:

\[
|p-c_M(p)|\le |p|^3/(3M^2),\qquad
\left|n^{-1}(p_a-d_a)^\top\dot z_a\right|
\le \frac{8C_h}{3M^2}S^4\rho.
\]

Integrating \(S^4\rho\) gives \(S(\infty)^5/5\), hence precisely
\(8C_hY^5/(15M^2\lambda^5)\). This is an error evaluated at the same
actual trajectory. The route correctly declines to call it a flow comparison
or a vanishing-width error.

For arbitrary finite initialization, the unchanged readout equation gives

\[
\frac d{dt}\frac{\|w\|_2^2}{n}
=-4\langle r,f_{\rm tr}\rangle_m
=Y^2-4\|f_{\rm tr}-y/2\|_m^2.
\]

Together with \(w(0)=0\), this proves
\(\sup_{t\le T,x}|f_n(t,x)|^2\le Y^2T\).
The alternative identity
\(-4\rho^2-4\langle y,r\rangle_m\), integrated and combined with
time Cauchy–Schwarz, gives \(S(T)\le YT\).
These estimates and the bounded clips keep every state coordinate finite
on bounded intervals. Local Lipschitz continuity on \(\tau>0\), with
\(\tau\ge1\), therefore proves global finite-time existence even
though the residual norm is not differentiable at zero. No all-time moment
is obtained from these increasing bounds.

The imported exponential tail constants also check out. Entrywise Hoeffding
bounds at thresholds \(\lambda/6\) and \(\lambda/2\), together with
the covariance-map maximum-norm Lipschitz constant three, give Gram failure
probability at most \(4m^2e^{-n\lambda^2/72}\). Two sphere
\(1/4\)-nets give operator failure at most
\(2e^{-n(K^2/8-2\log9)}\). Thus all-initialization equation (12)
has the stated prefactor and exponent for a sufficiently large fixed cutoff.
Initialization is independent of the choice of hard or smooth clipping.
The finite-horizon exceptional-event estimate follows from the unconditional
query bound and the bounded population prediction, as stated conditionally
on an already constructed own smooth population.

## 2. The exact one-sample, width-one monotonicity argument

For \(m=n=1\), \(u\ne0\), \(y>0\), and nonzero initial feature,
the sign transformation in all-initialization Section 6 gives positive
\(\alpha,\kappa,\beta,z,g\) and nonnegative \(\eta,\nu\).
The transformed equations (15), including the factor \(\|u\|_2^2\)
in \(\dot\alpha\), follow from the actual smooth updates.
As long as \(q=y-\eta g\ge0\), the first three transformed state
coordinates are nondecreasing. The key's integrating-factor formula gives
\(0<\kappa\le\tanh\alpha\); thus \(\kappa\), \(\beta\),
\(z\), and \(g\) are also nondecreasing.

Consequently
\(\dot q\le-2g(0)^2q\). A trajectory cannot cross residual zero:
the state would reach an equilibrium of a locally Lipschitz autonomous ODE,
whose unique continuation is stationary. This establishes (16), including
the passive-query bound \(|f_1(t,x)|\le|w|=\eta\le y/g(0)\).
The degeneracies \(W_0=0\) or \(A_0u=0\) instead give identically
zero prediction and stationary trainable blocks, with the correctly retained
clock growth. The negative-label symmetry leaves \(A,v,k,B\) unchanged
and reverses \(y,w,r,d,\ell\), consistently with every equation.

The divergent expectation of the upper bound is correctly distinguished
from divergence of the actual prediction moment. On the event
\(W_0\in[1,2]\), \(g(0)\le2|A_0u|\). The latter nondegenerate
Gaussian variable has positive density at zero, so
\(\mathbb E[g(0)^{-2}]=\infty\). No lower bound on the actual
passive predictor is inferred from this.

## 3. Covariance interpolation and the imported finite-program result

The variance profile
\(S_{ij}^{\theta}=(1+\theta s_it_j)/N\) has the correct fully
connected and block endpoints. It preserves row and column variance sums
and uses one matrix with its actual transpose throughout. The block endpoint
is correctly joined by global residual, clock, and memory contractions.

The joining proof in `BIAS_DIMENSION_ROUTE.md` uses first differences,
bounded trained fields, cap contraction, the global gate Lipschitz bound,
and residual coercivity. Its residual kernels retain \(p_a\), rather
than substituting \(d_a\). It transfers to the smooth map. The proof
controls the decaying residual difference separately from persistent scalar
pairing fluctuations, so it does not integrate a nondecaying residual source.

The common bounded velocity extension can be taken permutation invariant
using the invariant McShane metric and clipping to its known envelope. It
is one function for all profiles. For this Lipschitz function, Gaussian
density differentiation and one weak integration by parts give exactly
interpolation equation (8). In particular,

\[
\sum_{ij}(S_{ij}^{\theta})^{-1}
=N^3/(1-\theta^2)
\]

gives the stated crude derivative bound
\(\sqrt N L_x(t)/(2\sqrt{1-\theta^2})\), which is integrable at
the block endpoint. The two symmetry classes each contain \(N^2/2\)
entries; their coefficient is therefore \(N/4\), as in (11).
The sufficient bound (12) has exactly the additional scale needed to produce
a root-width endpoint difference. It remains an explicit hypothesis.

The authorized fixed-polynomial proof is sound for its declared program
class. Expression expansion can be represented by finitely many rooted
trees and scalar-average components; Gaussian pairings and label collisions
form quotient multigraphs. Doubly stochastic variance weights make every
forest contribution profile independent. A collision has probability
\(O(1/N)\), and each extra edge is bounded by \(2/N\). After the
normalizations, every nonleading term has at least one factor \(1/N\).
The finite sum over monomials, pairings, and partitions is legitimate for
each fixed program with the stated finite root moments. The proof supplies
no bound uniform in program size, degree, or time approximation, exactly
as the smooth route states.

The symmetry-only and hard-clip diagnostics in the dependency are not being
used as counterexamples to the smooth network. The former reads individual
matrix entries outside the declared program class; the latter concerns the
hard clipping function. The smooth route's own replacement diagnostic is
checked below.

## 4. Cubic initial prediction derivative and its mean

For the one-sample setup of interpolation Section 4, let
\(h=\tanh A_0\), \(\psi=\operatorname{sech}^2A_0\),
\(z=W_0h\), \(g=\tanh z\), and
\(b(z)=\tanh z\operatorname{sech}^2z\), all at initialization.
The first hidden velocities and the initial key velocity vanish.
Since \(c_M'(0)=1\), direct differentiation gives

\[
A''=4y^2\psi\odot W_0^\top b(z),\quad
v''=4y^2b(z),\quad
z''=4y^2\{q_nb(z)+W_0(\psi^2\odot W_0^\top b(z))\}.
\]

The second key derivative is also zero. With
\(q_{2,n}=g^\top g/n\), the readout derivatives satisfy
\(w'''=8yq_{2,n}^2g+2yg''\). The prediction product rule contains
three copies of \(w'^\top g''\), so

\[
f_n'''(0)=8yq_{2,n}^3+8y\,g^\top g''/n
=8yq_{2,n}^3+32y^3(q_n\nu_n+Q_n).
\]

This verifies the coefficient 32 and the positive reused-transpose term
\(Q_n=n^{-1}\|\psi\odot W_0^\top b(z)\|_2^2\).
The derivative is the ordinary output derivative. Its independence of
\(M\) at this order follows only from \(c_M'(0)=1\), not from
inactivity of the smooth clip.

For the mean formula, conditioning on \(h,z\) gives independent Gaussian
rows with mean \(z_i h/\|h\|_2^2\) and covariance
\(n^{-1}(I-hh^\top/\|h\|_2^2)\). Summing with the weights
\(\psi_j^2/n\) gives exactly interpolation equation (21): its leading
terms are \(d_n\kappa(q_n)^2+a_n\nu(q_n)\), and its correction is

\[
\frac{d_n}{n}
\left\{\frac{\operatorname{Var}(Z_{q_n}b(Z_{q_n}))}{q_n^2}
-\frac{\nu(q_n)}{q_n}\right\}.
\]

The denominators are harmless uniformly as \(q_n\downarrow0\):
\(|b(z)|\le|z|\) yields variance at most \(3q_n^2\) and
\(\nu(q_n)\le q_n\). The expression in braces has absolute value
at most four. Covariance differentiation supplies bounded first and second
derivatives of \(\gamma,\nu,\kappa\) on \([0,1]\). Taylor expansion
of the bounded empirical vector \((q_n,a_n,d_n)\), whose mean is
\((q,a_*,d_*)\) and whose mean-square error is \(O(1/n)\), proves
the claimed mean error. The same conditional-variance and Taylor argument
for \(q_{2,n}^3\) and \(q_n\nu_n\) verifies all terms in (19).

This checks \(\mathbb E f_n'''(0)\) and its displayed limit. It does
not assert a uniform Taylor remainder for the flow, or identify a derivative
of an all-time population approximation by exchanging limits.

## 5. Analyticity and second-response counterexamples

The Gaussian example
\(H(\varepsilon)=\mathbb E\tanh^2(\varepsilon G)\) is smooth
on the real line by bounded fixed-order scalar derivatives and finite
Gaussian moments. The scalar Taylor series has its nearest nonremovable
complex poles at \(\pm i\pi/2\). Thus a subsequence of its even
coefficient roots stays bounded below. Multiplication by
\((2k-1)!!\), whose \(2k\)-th root diverges, makes the Taylor
radius of \(H\) zero. Rescaling by \(M\) preserves that conclusion.
This is a valid objection to summing a Gaussian response expansion solely
from scalar smoothness. It is not a formula for the neural predictor.

The normalized-L2 Hessian example is also correct: two unit directions
\(\sqrt n e_1\) produce a cap second derivative of normalized norm
\(|c_M''(p_0)|\sqrt n\). It refutes a general dimension-independent
bilinear Hessian bound, without claiming that the concentrated directions
are actual Gaussian network responses.

For the residual-clock example, \(|a|\le\alpha/2\) gives
\(K(a)\succeq(\alpha/2)I\). The formulas for
\(u=\partial_a r\) and \(v=\partial_a^2r\) solve their differentiated
linear equations with zero initial sensitivities. At \(a=0\), the
first sensitivity is perpendicular to the residual, so the norm chain rule
gives exactly

\[
\partial_a^2\|r(t,a)\|_2\big|_{a=0}
=v_1(t)+\frac{Y}{(\beta-\alpha)^2}
e^{\beta t}(e^{-\alpha t}-e^{-\beta t})^2.
\]

Here \(v_1\ge0\). The second term is nonintegrable when
\(\beta\ge2\alpha\), while the residual and its first sensitivity
are integrable. This disproves the proposed general inference from uniform
exponential fitting to an integrable pathwise clock Hessian. It does not
disprove the smooth neural prediction theorem or a weak averaged argument.

## 6. Restoration lemma and retained limits

The abstract lemma in `SMOOTH_RESTORATION.md` is correct. Integrating its
residual convolution by Tonelli gives

\[
\int_0^tR\le aV/\sqrt n+(C/\kappa)\int_0^tbD.
\]

Substitution into its state inequality gives initial term
\(a(1+CV)/\sqrt n\) and Gronwall coefficient
\(C(1+C/\kappa)b\), exactly the constants in (3). Integrating to
infinity then gives (4). Exponentially decaying source envelopes yield the
stated integrable residual bound by the explicit scalar convolution, with
a polynomial factor allowed when decay rates coincide.

The residual norm comparison (5) follows from its 1-Lipschitz property and
conditional expectation. It does not equate the mean norm with the norm
of the mean. Both clocks start at one, so integrating (6) correctly
controls their difference. The implication from the conditional squared
population error (7) to the unconditional probability estimate (8) is just
conditional Markov plus the good-event complement. It includes mean bias
only because (7) explicitly includes that bias as a hypothesis.

All routes correctly retain the decisive open statements: the signed
nonlinear covariance estimate or an equivalent mean-law theorem, the actual
population restoration hypotheses, and the exceptional-event all-time
moment. Neither the initial coefficient calculation nor the restoration
lemma proves them.

One minor wording refinement is warranted: the last paragraph of
`SMOOTH_ALLINIT_ROUTE.md` says that smooth clipping removes
“nondifferentiability.” It removes the clipping corners; the residual-norm
clock remains nonsmooth at zero, as the same route and the other two files
correctly explain. Also, any eventual use of the proposed observable
\(\dot h/\rho\) needs an explicit value or state-based formula at zero
residual. It is presently only a proposal, not a premise of a proved claim.
These precision notes do not change the auxiliary verdict.
