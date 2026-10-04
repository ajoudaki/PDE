# Four-point latent-factor acquisition in the q=1 populations

Continuation, 2026-09-30. Main author: root. Scope: the user's explicitly
designated study, current manuscript, and its already reconciled q=1 model.
No learned dense middle layer, dense reference, other study, or compression
objective is used. The central result is a **conditional local trajectory
theorem with computer-assisted scalar sign certificates**, supplemented by
an exact all-time representation constraint. It is not a global fitting theorem.
Internal check status and frozen input hashes are recorded in README.md.

## 1. What is being learned

Choose two independent uniform latent signs sigma and tau. They produce four
equally weighted normalized inputs and their labels:

\[
 u_{\sigma\tau}=(c,\varepsilon\sigma,\varepsilon\tau),\quad
 c=\sqrt{1-2\varepsilon^2},\quad y_{\sigma\tau}=\sigma\tau,
 \qquad 0<\varepsilon<1/\sqrt2.                         \tag{1}
\]

The manuscript inputs are x=sqrt(3)u, so their norms are sqrt(3).
An arbitrary fixed orthogonal rotation of all inputs gives the same result;
the learning algorithm is not supplied the latent coordinate system.
The latent factors are encoded in the inputs, as they must be to be learnable,
but neither factor is a training target. In fact

\[
 \operatorname{mean}y\sigma=\operatorname{mean}y\tau=0. \tag{2}
\]

The common coordinate is a background or context. It permits this XOR task
in an odd, bias-free architecture: ordinary centered planar XOR would have
same-label antipodes and be impossible. The small parameter makes the
factor directions weak compared with the context. It is a **fixed dataset
parameter**, not a width limit or an activation linearization. All actual
features and dynamics remain exactly tanh.

The theorem holds for every sufficiently small fixed positive epsilon.
The proof establishes the existence of an epsilon threshold, not an explicit
numerical threshold. No claim for a particular moderate epsilon is inferred
from an asymptotic coefficient or from exploratory quadrature.

## 2. The exact population object and its explicit foundation

Use probability spaces Omega_1 and Omega_2 for the two neuron populations.
Random fields represent their joint laws, including the marks needed to reuse
the same initialized Gaussian source. Denote their expectations by E_1,E_2.
The first population carries A in R^3 and four keys K_a. The second carries
the readout W and four values V_a. For a query u, set

\[
 H(u)=\tanh(A\cdot u),\quad
 Z(u)=T H(u)+\tfrac14\sum_a V_a\langle K_a,H(u)\rangle_1,
 \quad G(u)=\tanh Z(u),\quad F(u)=\langle W,G(u)\rangle_2. \tag{3}
\]

T is the **fixed** canonical initialized Gaussian mixing source, with its
true adjoint. The notation
B=T+(1/4)sum V_a tensor K_a is only an abbreviation for (3); B is not an
independent trained state. Define

\[
 D_a=W(1-G_a^2),\qquad L_a=(1-H_a^2)B^*D_a,
 \quad r_a=F_a-y_a,\quad \rho=(\operatorname{mean}r_a^2)^{1/2}.
\]

The physical-time equations are precisely

\[
 \dot W=-2\operatorname{mean}r_aG_a,\quad
 \dot A=-2\operatorname{mean}r_aL_au_a,\quad
 \dot V_a=-2r_aD_a,\quad
 \dot K_a=(\rho/\tau)(H_a-K_a),\quad\dot\tau=\rho.       \tag{4}
\]

Initially A is standard Gaussian, independent of the source, W=V_a=0,
K_a=H_a(0), and tau=1. The manuscript dictionary is unchanged:
K_a=bar h_(a,0)/tau and V_a=-2 bar delta_(a,0). There is no hidden change
of learning rate or physical clock. See MANUSCRIPT_RECONCILIATION.md for
the zero-readout qualification and the joint-clock mass normalization.

**Population foundation assumed, not proved here.** The current manuscript
labels its fixed-order population limit a conjecture. Our statements assume
a regular unique equivariant population flow realizing the canonical fixed
source as a bounded operator on the generated L2 spaces, with the
differentiability and integrability used below. At startup,
for root-dependent H_a, the calls z_a=TH_a are jointly Gaussian with
covariance E_1 H_a H_b. For bounded C1 sources U(z) with bounded first
derivatives, the first reverse call has the law

\[
 T^*U=\sum_b\mathbb E_2[\partial_bU]H_b+\xi_U,
 \quad \mathbb E[\xi_U\xi_V]=\mathbb E_2[UV],           \tag{5}
\]

where the jointly Gaussian innovations are independent of A_0. The covariance
in (5) is the full source Gram, not a regression residual. All sources here
are products of tanh and its bounded derivatives, so satisfy this regularity.
At positive times no new independent Gaussian replacement is made. Separate
unmarked marginal densities do not supply (5) or define the later reused-source
flow. This study does not prove that such marginals form a finite Markov system.

The sign-flip and exchange symmetries imply F_a=y_a f. Before f=1 define

\[
 s=2\int_0^t(1-f(t'))dt',\quad\tau=1+s/2,
 \quad W'=G_y,\quad A'=\operatorname{mean}y_aL_au_a,
 \quad V_a'=y_aD_a,\quad K_a'=(H_a-K_a)/(2+s).           \tag{6}
\]

Primes below refer to s. It is a valid increasing clock near initialization.
At zero A'=V'=K'=G'=0. Physical second derivatives of the hidden energies
are four times the displayed feature-time second derivatives.

## 3. A measurable meaning of latent-factor learning

For either hidden response Q=H or G, form four sample-pattern fields

\[
 Q_0=\operatorname{mean}Q_{\sigma\tau},\quad
 Q_\sigma=\operatorname{mean}\sigma Q_{\sigma\tau},\quad
 Q_\tau=\operatorname{mean}\tau Q_{\sigma\tau},\quad
 Q_y=\operatorname{mean}\sigma\tau Q_{\sigma\tau}.       \tag{7}
\]

Let E_{1,chi}=E_1 H_chi^2 and E_{2,chi}=E_2 G_chi^2. They measure responses
to the context, each primitive factor, and their product, respectively.
The exact population symmetries make the four fields orthogonal at every
existing time and make the two factor energies equal. One proof is to use
signed inputs p_a=y_a u_a: translating (sigma,tau) by (alpha,beta) is the
orthogonal map diag(alpha beta,beta,alpha). Its invariant covariance is a
group convolution, diagonalized by these four characters. Undoing the label
gauge permutes the characters. The same argument applies to both layers.

This has an operational consequence. The least squared L2 norm of a
population linear readout that recovers a character chi exactly on the four
examples is

\[
 \min_{b:\langle b,Q_a\rangle=\chi(a)}\|b\|^2
       =1/E_{j,\chi}.                                  \tag{8}
\]

Indeed b=Q_chi/E_{j,chi} attains the constraints by orthogonality, and any
feasible b satisfies 1=<b,Q_chi>, so Cauchy--Schwarz gives the matching
lower bound. The claim applies when the energy is nonzero; if it is zero,
no such decoder exists and its minimum cost is interpreted as infinity.
An increasing factor energy therefore means a **strictly smaller norm
needed to decode that factor**, rather than just changing coordinate names.
It does not mean that training creates information absent at initialization.

## 4. The acquisition theorem

**Theorem (conditional on the population flow specified in Section 2).**
There exists epsilon_0>0 such that for each fixed 0<epsilon<epsilon_0,
both primitive-factor energies strictly increase and the context energy
strictly decreases in **each hidden population** on some positive initial
training interval. The first-layer XOR energy also strictly increases.
All these energies have zero initial first derivative.

More precisely, there are fixed real constants with rigorously enclosed
values as follows:

| Observable | Initial second derivative in s | Certified leading coefficient |
|---|---|---|
| First-layer factor, either bit | C_1 epsilon^6 + O(epsilon^8) | 0.192410 < C_1 < 0.192484 |
| Second-layer factor, either bit | C_2 epsilon^6 + O(epsilon^8) | 0.201751 < C_2 < 0.201810 |
| First-layer context | D_1 epsilon^4 + O(epsilon^6) | -0.047957 < D_1 < -0.047953 |
| Second-layer context | D_2 epsilon^4 + O(epsilon^6) | -0.055942 < D_2 < -0.055939 |
| First-layer XOR | C_y epsilon^8 + O(epsilon^10) | 2.82798 < C_y < 2.83330 |

The relative first-layer hierarchy also changes strictly:

\[
 (E_{1,\sigma}/E_{1,0})''(0)
       =C_{10}\varepsilon^6+O(\varepsilon^8),\quad
        0.631230<C_{10}<0.631426,
\]
\[
 (E_{1,y}/E_{1,\sigma})''(0)
       =C_{y1}\varepsilon^6+O(\varepsilon^8),\quad
        5.821575<C_{y1}<5.833118.                       \tag{9}
\]

Thus factors gain relative to background, and the label interaction gains
relative to its factors. This is selective representation change, not common
rescaling. The strict second derivatives, controlled epsilon remainders,
and continuity in s prove actual strict changes on a nonempty interval for
each such fixed dataset. They do not prove indefinite monotonicity.

### Proof architecture and the interaction that explains the signs

The full first-layer derivation is WEAK_FACTOR_ROUTE.md, equations (1)--(11).
For a root A, let h_chi(A) be (7) evaluated at that root, v_chi=E_1 h_chi^2,
and J(v)=E_2 G_y(0)^2, evaluated with the canonical Gaussian forward call.
The actual first reverse call gives exactly

\[
 \mathbb E[A''\mid A_0=A]
     =\tfrac12\sum_\chi J_\chi\nabla h_\chi(A)^2,
 \qquad
 E_{1,\eta}''(0)=\tfrac12\sum_\chi J_\chi
     \mathbb E_1[\nabla h_\eta^2\cdot\nabla h_\chi^2], \tag{10}
\]

where J_chi=partial J/partial v_chi. Equation (10) is a derived initialized
conditional drift; it is not substituted for the full population dynamics.

Write A_0=(X,Y,Z), p=tanh'(X), q=tanh''(X), v=E tanh^2 X,
a=E p^2, b=E q^2, T_1=E tanh'(sqrt(v)N)^2 and
T_2=E tanh''(sqrt(v)N)^2. The four first responses are

\[
 h_0=\tanh X+O(\varepsilon^2),\quad
 h_\sigma=\varepsilon Yp+O(\varepsilon^3),\quad
 h_\tau=\varepsilon Zp+O(\varepsilon^3),\quad
 h_y=\varepsilon^2YZq+O(\varepsilon^4).                \tag{11}
\]

The second layer's initial label signal has **two positive routes**:

\[
 J=T_1v_y+T_2v_\sigma v_\tau+O(\varepsilon^6)
   =\varepsilon^4(T_1b+T_2a^2)+O(\varepsilon^6).        \tag{12}
\]

The first term propagates a label interaction already present in the first
layer. The second forms it from two separate primitive-factor responses in
the second layer. Consequently J_sigma=T_2 v_tau+O(epsilon^4)>0 near
this geometry, and conversely. Improving either unsupervised factor helps
the supervised product **because the other factor is available**.

For example (10) yields the leading conditional readin drift

\[
 \mathbb E[Y''\mid X,Y,Z]
 =\varepsilon^4Y\{T_1Z^2q^2+T_2a p^2\}
       +O_{L^r}(\varepsilon^6),\qquad r<\infty.        \tag{13}
\]

Both displayed gains are nonnegative and the second is strictly positive at
every finite X. Equation (13) concerns conditional mean acceleration, not
the sign of every neuron's actual acceleration: the transpose innovation
has not disappeared from the actual state. It implies
(E Y^2)''=2 epsilon^4(T_1 b+T_2 a^2)+O(epsilon^6)>0.
The feature-energy theorem is stronger than this weight statement, since
motion of the context can otherwise offset a larger weight inside tanh.

For the second layer one must retain **all three** contributions. Put
U_a=y_aG_y tanh'(z_a) and Y_a^chi=chi(a)G_chi tanh'(z_a), and define
A_U=mean tanh'(A·u_a)u_a T*U_a, and likewise A_Y. Directly from (3)--(6),

\[
 E_{2,\chi}''(0)=2\mathbb E_1[A_U\cdot A_{Y^\chi}]
  +\tfrac2{16}\sum_{ab}\mathbb E_1[H_aH_b]
                              \mathbb E_2[U_bY_a^\chi]. \tag{14}
\]

The first term splits into conditional drift and the **full** innovation
covariance from (5); the second is the actual q=1 value-memory write.
WEAK_FACTOR_SECOND_LAYER.md, equations (1.1)--(6.1), gives the complete
calculation, controlled remainders, and exact polynomial coefficients.
The certified leading factor coefficient C_2 decomposes as

| Contribution | Outward interval |
|---|---|
| Readin conditional drift | (0.132866, 0.132914) |
| Fixed-source reverse covariance | (0.044569, 0.044576) |
| q=1 memory write | (0.024315, 0.024321) |

Every contribution cooperates in increasing the factor energy. For the
context, each is instead strictly negative. Dropping the transpose covariance
or freezing the readin would omit substantive parts of this calculation.

The controlled remainders in both route proofs follow from bounded tanh
derivatives and finite Gaussian polynomial moments. A fixed-Gaussian coupling
of the four Walsh forward calls justifies the small-variance expansions;
their normalized variances have positive limits. Only initialization is
expanded in epsilon. No independence assumption at trained times is used.

## 5. What happens to the output

Symmetry reduces the four training predictions to one amplitude f(s), but
does not reduce the populations to a scalar state. Let kappa=E_{2,y}(0).
It is positive for the small fixed datasets above. At initialization

\[
 f(s)=\kappa s+\tfrac13E_{2,y}''(0)s^3+o(s^3),\qquad
 \kappa=(0.260678\ldots)\varepsilon^4+O(\varepsilon^6). \tag{15}
\]

The cubic coefficient is strictly positive. To see this without any sign
quadrature, set chi=y in (14), so Y=U; diagonalizing the initial sample
Gram gives

\[
 E_{2,y}''(0)=2\mathbb E_1|A_U|^2
                +2\sum_\chi v_\chi\mathbb E_2 U_\chi^2>0. \tag{16}
\]

For epsilon>0 in this class, v_y>0, and U_y=G_y Q_0 with
Q_0=mean tanh'(z_a)>0 and G_y nonzero in L2, giving strictness.
Expanding W(s)=integral_0^s G_y(r)dr with G_y'(0)=0 proves (15).
In physical time, dot f(0)=2 kappa and dot L(0)=-4 kappa for
L=(1-f)^2. The output starts fitting the XOR, and learned feature motion
adds a positive cubic correction per accumulated residual.

This also explains a limitation of the perturbation result. The initial
label signal is only order epsilon^4. A short initial expansion cannot be
continued to the much longer times needed for fitting by assuming its
coefficients stay fixed. No global fit is inferred from (15).

## 6. An all-time constraint, including any finite fitted endpoint

For **every** first-layer tanh neuron at **every** state, independently of
training, let its four logits be x+sigma a+tau b. Then

\[
 |H_y|\le\min(|H_\sigma|,|H_\tau|).                    \tag{17}
\]

For the first inequality set Delta_+=tanh(x+a+b)-tanh(x-a+b) and
Delta_-=tanh(x+a-b)-tanh(x-a-b). These have the same sign, while
H_sigma=(Delta_++Delta_-)/4 and H_y=(Delta_+-Delta_-)/4.
The triangle inequality in this same-sign case proves (17); exchange a,b
for the other factor. The inequality against H_sigma is strict at finite
logits if a is nonzero, and analogously for b.

Integrating and using (8) yields, at every existing time,

\[
 E_{1,y}\le\min(E_{1,\sigma},E_{1,\tau}),\qquad
 \text{each factor is at least as cheap to decode as its XOR}. \tag{18}
\]

Thus the local acquisition theorem is compatible with a permanent constraint:
the first layer cannot discard both constituents and retain only a stronger
product response. This is an accessibility statement on the four inputs,
not a claim that individual neurons become pure factor detectors.

A quantitative endpoint consequence uses the actual second layer too.
For any state with synchronized signed output amplitude f, tanh is 1-Lipschitz,
so Jensen's inequality across the two tau values gives

\[
 \|G_y\|_2^2\le\|B\|^2(E_{1,\sigma}+E_{1,y})
                 \le2\|B\|^2E_{1,\sigma}.             \tag{19}
\]

Indeed G_y is the difference of the two half-differences under the sigma
flip; apply Jensen to their difference, Lipschitz continuity to each, and
the operator norm of B to the corresponding H differences. Their average
squared norm is E_{1,sigma}+E_{1,y}. Cauchy--Schwarz applied to
f=<W,G_y> proves, for either bit whenever ||W||_2 ||B||>0,

\[
 E_{1,\mathrm{bit}}\ge
       \frac{f^2}{2\|W\|_2^2\|B\|^2}.                \tag{20}
\]

Whenever a fitted endpoint has finite nonzero readout and bounded B, f=1
in (20): **both unsupervised factors necessarily survive in its first
representation.** There is no epsilon-uniform bound on these endpoint norms
in the present theorem. This conclusion does not assert that the factors
grew monotonically on the way there.

## 7. Constraints on the unseen-input function; the unsolved part

In this section u denotes normalized query coordinates, so the corresponding
manuscript query is x=sqrt(3)u, as in (1)--(3). The exact population symmetries give

\[
 F_t(u_0,-u_1,u_2)=-F_t(u_0,u_1,u_2),\quad
 F_t(u_0,u_1,-u_2)=-F_t(u_0,u_1,u_2),
 \quad F_t(u_0,u_2,u_1)=F_t(u_0,u_1,u_2).              \tag{21}
\]

The first two follow because each bit flip permutes the inputs and reverses
all labels; reversing all labels reverses W and F while preserving the
hidden features and values. Architectural oddness F_t(-u)=-F_t(u) then
also makes F_t odd in u_0. Thus all three coordinate planes are mandatory
zeros for the entire trajectory and every pointwise endpoint limit.

If a fitted endpoint exists and is C3 as a function of the query, repeated
division of odd functions by their coordinates gives the exact form

\[
 F_*(u)=u_0u_1u_2\,\Psi_*(u_0^2,u_1^2,u_2^2),\quad
 \Psi_*(r_0,r_1,r_2)=\Psi_*(r_0,r_2,r_1),
 \quad\Psi_*(c^2,\varepsilon^2,\varepsilon^2)
                         =\frac1{c\varepsilon^2}.    \tag{22}
\]

For completeness, division uses F/u_1=integral_0^1 partial_1 F(u_0,t u_1,u_2)dt,
then the other two coordinates. C3 makes the resulting quotient continuous;
its evenness allows it to be expressed in the squared coordinates. A
pointwise limit alone need not have this regularity; it still inherits (21).

Equation (22) leaves the amplitude function, extra zeros, and sign changes
undetermined. It is an endpoint **constraint**, not a characterization of
the selected fitted function. Neither global fitting nor endpoint existence
has been proved for these four-point canonical population dynamics.
The separate GLOBAL_MEMORY_ROUTE.md records a complete, author-checked attempt
at a general compensation identity and identifies the unbounded memory-defect
term preventing its use as a fitting theorem. It is not a dependency of the
acquisition result, and its counterpath is not an actual training trajectory.

## 8. Rigorous scalar certification and reproducibility

All signs in Section 4 reduce to polynomials in
I_n=E sech^(2n)(N) and J_n=E sech^(2n)(sqrt(v)N), n=1,...,7,
v=1-I_1. The exact first polynomials are in WEAK_FACTOR_ROUTE.md (8);
the exact second polynomials are in WEAK_FACTOR_SECOND_LAYER.md (6.1),
(4.2),(4.5),(4.6),(5.1),(5.3). The following scripts are proof support,
not empirical training or estimates of a finite-width trajectory:

- weak_factor_interval_certificate.py: directed interval quadrature and the
  first-layer coefficients.
- weak_factor_coefficient_certificate.py: directed polynomial evaluation of
  second-layer coefficients and the hierarchy ratios from the enclosed moments.

The interval method uses only Python's standard library, Decimal precision42,
outward arithmetic, and adjacent representable bounds around correctly rounded
Decimal exp and sqrt. Pi is enclosed by Machin's identity using exact Fraction
alternating sums (60 terms each). For each variance in (0,1], integrate the
standard-normal variable on [0,10] by composite Simpson with h=1/2000,
double it, and enclose the positive tail by 2 phi(10)/10.

Here is an explicit justification for the discretization error. Set
P_n(t)=(1-t^2)^n and D=(1-t^2)d/dt. The absolute value of the kth derivative
of sech^(2n)(sqrt(v)x), k<=4, is at most the coefficient L1 norm of D^kP_n,
since sqrt(v)<=1 and |tanh|<=1. Each derivative of standard normal density
up to order four has absolute value <10: expand the corresponding polynomials
1,x,x^2-1,x^3-3x,x^4-6x^2+3, and use
sup |x|^j exp(-x^2/2)=j^(j/2)exp(-j/2) for j>0.
For example the fourth bound is at most
(16 exp(-2)+12 exp(-1)+3)/sqrt(2pi)<10; the earlier ones are smaller.
Leibniz therefore bounds the fourth derivative of the integrand by
M_n=10 sum_(k=0)^4 binomial(4,k)||D^kP_n||_coeff,1.
The doubled Simpson error is at most 20 h^4 M_n/180. The code computes
these integer polynomial bounds exactly before outward conversion.
The uncertain outer variance v is itself enclosed and propagated in every
node. Hence the stated intervals include integration, tail, arithmetic,
and variance uncertainty, not just a floating-point quadrature tolerance.

Executed successfully, Python 3.10.12, from the repository root:

```bash
python studies/q1_population_mechanism_20260930/weak_factor_interval_certificate.py --output data/generated/q1_population_mechanism_20260930/weak_factor_interval_certificate_20260930_01/results.json
python studies/q1_population_mechanism_20260930/weak_factor_coefficient_certificate.py --moments data/generated/q1_population_mechanism_20260930/weak_factor_interval_certificate_20260930_01/results.json --output data/generated/q1_population_mechanism_20260930/weak_factor_coefficient_certificate_20260930_01/results.json
```

Use fresh output paths for reproduction; the scripts refuse overwriting.
The moment output records all inner/outer intervals, all error bounds,
precision, source hash, Python version and elapsed time. The coefficient
output records its own source hash and its moment-input hash.

Exploratory deterministic Gaussian quadratures in structured_initial_integrals.py
and weak_factor_constants.py selected this direction. The small-factor direct
four-dimensional quadrature did not meet the predeclared agreement threshold;
its signs were not used as evidence for the theorem. The exact epsilon
reduction and interval certification above replace that diagnostic gap.
Their contract, configurations, output paths and outcomes are recorded in
STRUCTURED_POPULATION_CONTRACT.md. No numerical training run was performed.

## 9. The substantive conclusion and its boundary

On this four-point task, a label signal with zero correlation to either
primitive bit nevertheless improves access to both bits in both hidden
populations, while suppressing the shared context. The mixed product term
in (12) explains why: the usefulness of one factor depends on the presence
of the other. The actual fixed-source covariance and q=1 memory writes
cooperate in the second layer. This differs from treating every direction
orthogonal to the labels as nuisance to be contracted.

An all-time architectural constraint keeps the first layer's constituents
at least as accessible as its interaction, and any bounded fitted endpoint
must retain both constituents. These are the proved trajectory and endpoint
constraints. Persistence of the initial improvement, a fitting theorem,
the final amplitude in (22), performance on an additional test distribution,
and the population-flow construction itself remain open. No priority claim,
promotion, or manuscript change is made.
