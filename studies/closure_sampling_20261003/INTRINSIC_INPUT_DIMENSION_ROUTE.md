# Training-span reduction and the passive Gaussian directions

2026-10-04. Scoped theoretical continuation. Candidate frozen before exchanging
substantive route conclusions. This note proves an exact training reduction and
a conditional, fixed-slice root-width estimate, but **does not prove a new
whole-sphere, all-time compression theorem**. Its missing estimate is stated
explicitly below. No experiment, maintained-book edit, or Git write was made.

The complete assigned inputs were SAMPLE_COUNT_REFINEMENT.md,
GENERAL_ANALYTIC_COMPRESSION.md, WHOLE_QUERY_RESPONSE_SOURCE.md, and
STORAGE_QUADRATIC_IMPROVEMENT.md. The canonical-notation skill and its neural
reference, rigorous-math skill, and conjecture-investigation skill were applied.
No other study or sibling-route artifact was read.

## 1. Contract and the potential improvement

Use the actual initialized width-n model, physical gradient flow, fixed
training inputs, activations, and notation of SAMPLE_COUNT_REFINEMENT.md.
Thus normalized inputs are v=x/sqrt(d) in S^(d-1), the hidden depth is L,
the first-layer matrix is A, hidden matrices are W^(ell), and

\[
 f_n(t,v)=\frac1n w(t)^\top h^{(L)}(t,v),\qquad
 z^{(1)}(t,v)=A(t)v.
\]

The activations are bounded and holomorphic on a fixed horizontal strip.
Initialization has independent standard Gaussian entries in A_0,
independent N(0,1/n) hidden entries, and zero readout. The labels obey
Y<=c lambda, where lambda=min(1,gamma/m), with the same limiting initialized
Gram gap gamma as in the assigned theorem. Retained fixed and moving real
coordinates count. Setup may use initialization and the data but no supplied
trained trajectory.

Let V=span{v_1,...,v_m}, let r=dim(V), and let k=d-r. If k>0, choose a
fixed unit vector e in V-perp. Define the folded query

\[
 \widetilde v=P_Vv+\|P_{V^\perp}v\|_2 e.                 \tag{1}
\]

The promising reduction would replace d in the existing storage exponent by
D=min(d,r+1). It requires the following additional assertion:

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_n(t,v)-f_n(t,\widetilde v)|
       \le C_{\rm data,\eta}n^{-1/2}                  \tag{2}
\]

with probability at least 1-eta at every sufficiently large width. Constants
must be independent of n and time. This is a uniform fluctuation statement
about the same realization, not a population-training assumption.

## 2. The reduction of training is exact

Choose orthonormal matrices U in R^(d by r) and E in R^(d by k) spanning V
and V-perp. Put A_V(t)=A(t)U and G=A_0E. The exact first-weight equation is

\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top.
\]

Since v_a^top E=0, differentiation gives

\[
 A(t)E=G,\qquad
 A(t)v=A_V(t)u+Gz,
 \quad u=U^\top v,\ z=E^\top v.                         \tag{3}
\]

Every training forward pass has z=0. Its backward pass and all parameter
updates therefore depend only on A_0U, the initialized hidden matrices,
and the data. Uniqueness of the finite-dimensional smooth parameter ODE
shows that the complete training path

\[
 (A_V(t),W^{(2)}(t),...,W^{(L)}(t),w(t))
\]

is measurable with respect to that information. Denote this sigma-field
by F. Orthogonal invariance of independent Gaussian rows implies that G
has independent N(0,1) entries and is independent of F. This remains true
after conditioning on any training-path event measurable with respect to F.

Fix an F-measurable path and define its scalar map of a first preactivation
a in R^n by

\[
 \Psi_t(a)=\frac1n w(t)^\top
 \phi_L\!\left(W^{(L)}(t)\phi_{L-1}\!\left(\cdots
 W^{(2)}(t)\phi_1(a)\right)\right).                    \tag{4}
\]

This notation means exactly the original finite sequence of hidden layers.
On the supplied real bounded-operator event, if
sup_t ||w(t)||_2/sqrt(n)<=C_data and sup_t ||W^(ell)(t)||_op<=C_data,
the chain rule and the bounded real activation derivatives give

\[
 \sup_{t,a}\|\nabla_a\Psi_t(a)\|_2
 \le \frac{\sup_t\|w(t)\|_2}{n}
       \prod_{\ell=1}^L\|\phi_\ell'\|_\infty
       \prod_{\ell=2}^L\sup_t\|W^{(\ell)}(t)\|_{\rm op}
 \le C_{\rm data}/\sqrt n.                              \tag{5}
\]

All a in (5) are real. No passive-query coordinate maximum is used.

For fixed t,u,s, where s>=0 and ||u||^2+s^2=1, define the conditional mean

\[
 \overline f_n(t,u,s)
   =\mathbb E_g\Psi_t(A_V(t)u+s g),\qquad g\sim N(0,I_n).
                                                               \tag{6}
\]

It depends on the passive radius s and not its direction. At s=0 it equals
the exact realized prediction; in particular it preserves every training
prediction. The formula is an output expectation, not the result of replacing
each nonlinear layer by its mean. In general those operations disagree.

## 3. Root-width concentration on each fixed active-input/time slice

Here is a complete elementary moment argument, including uniformity in
the passive direction. Let q>=1 be a moment order and let C denote numerical
constants. For independent standard Gaussian vectors g,h, the rotation
g(theta)=g cos(theta)+h sin(theta) has derivative
g'(theta)=-g sin(theta)+h cos(theta). These are independent standard Gaussian
vectors for each theta. If a deterministic differentiable map Psi is
Lipschitz with constant B, then conditioning on g(theta) gives

\[
 \|\nabla\Psi(a+s g(\theta))\cdot s g'(\theta)\|_{L^q}
       \le C\sqrt q\,sB.                                \tag{7}
\]

The scalar Gaussian moment bound follows directly by integrating its density;
its variance is at most s^2 B^2. Integrating (7) from zero to pi/2 and applying
conditional Jensen to subtract the independent copy proves

\[
 \|\Psi(a+s g)-\mathbb E\Psi(a+s g)\|_{L^q}
       \le C\sqrt q\,sB.                                \tag{8}
\]

Now keep the entire n-by-k matrix G, and let xi(theta) be a constant-speed
shortest great-circle arc on S^(k-1). At every point, G xi(theta) and
G xi'(theta) are independent Gaussian vectors, since xi^top xi'=0.
Exactly the same argument gives

\[
 \|\Psi(a+sG\xi)-\Psi(a+sG\xi')\|_{L^q}
       \le C\sqrt q\,sB\|\xi-\xi'\|_2.                 \tag{9}
\]

The geodesic length is at most (pi/2)||xi-xi'||. Opposite points can use
any half-circle when k>=2; for k=1 the same independent-copy bound applied
to Psi(a+sg)-Psi(a-sg) gives the required two-point estimate, with a changed
constant. More directly, in that case the two individual centered values
are each controlled by (8).

For completeness, (9) yields a uniform bound without a width-dependent
covering loss. Take Euclidean 2^(-j) nets of S^(k-1) of cardinal at most
(C 2^j)^k, join each net point to a nearest point at the preceding scale,
and telescope a continuous sample path. For the increments at scale j,
choose their moment order q+j Ck. The inequality
||max_i |X_i|||_(L^q)<=N^(1/p) max_i||X_i||_(L^p), p>=q,
bounds their maximum by C 2^(-j) sB sqrt(q+jk). The sum over j is bounded
by C sB(sqrt(q)+sqrt(k)). Use (8) for a base point. Consequently

\[
 \left\|\sup_{\xi\in S^{k-1}}
 |f_n(t,Uu+sE\xi)-\overline f_n(t,u,s)|\right\|_{L^q(G)\mid F}
 \le \frac{C_{\rm data}s(\sqrt k+\sqrt q)}{\sqrt n}.
                                                               \tag{10}
\]

This includes the fixed endpoint t=infinity whenever the supplied parameter
convergence holds. It does not put the supremum over t or u inside the norm.
In particular, for each fixed t,u,s the folded representative and every
passive direction differ by O_P(n^(-1/2)), uniformly over that passive sphere.
For a fixed finite set of time/active-input slices, a union bound costs only
the square root of the logarithm of the number of slices. If that number is
independent of n, it is an allowable constant.

One also has a direct integrated-test statement. For any probability measure
mu on the (time,unit-query) domain that is independent of G conditional on F,
Fubini and (8) with q=2 imply

\[
 \mathbb E_G\int
 |f_n(t,v)-\overline f_n(t,U^\top v,\|E^\top v\|)|^2\,d\mu(t,v)
 \le C_{\rm data}/n.                                    \tag{11}
\]

This is an integrated squared-error estimate. It is not a sphere supremum
estimate; neither Fubini nor pointwise concentration interchanges those
quantifiers.

## 4. What a straightforward uniform argument actually gives

The supplied real path estimates bound parameter velocities by residual
activity. With rho(t)=||c(t)||_2/sqrt(m), introduce, for this proof only,

\[
 \tau(t)=\int_0^t\rho(s)ds,\qquad 0\le\tau\le S\le C Y/\lambda.
\]

The exact updates and bounded feature/backward RMS norms give
||dot A_V||_op/sqrt(n)+sum ||dot W^(ell)||_op+
||dot w||_2/sqrt(n)<=C_data rho. Together with (5) and the forward chain
rule, they bound the output's Lipschitz constant in tau uniformly over
the query sphere. On ||G||_op<=C sqrt(n) and
sup_t||A_V(t)||_op<=C_data sqrt(n), its query Lipschitz constant is also
C_data. The conditional mean has the same bounds, using
E||G||_op/sqrt(n)<=C_k. The latter expectation is at most the Frobenius
bound sqrt(k), which is already sufficient for fixed k. Markov's inequality
similarly makes ||G||_op/sqrt(n) bounded with any fixed prescribed confidence.

A mesh with spacing n^(-1) in the unit-query sphere and the finite tau
interval has at most (C_data n)^(d+1) points. At every mesh point, (8) and
Markov's inequality with q proportional to log(n/eta) give an exponentially
small tail. Union bounding and filling in the mesh proves

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_n(t,v)-\overline f_n(t,U^\top v,\|E^\top v\|)|
 \le C_{\rm data,\eta}\sqrt{\log(en)/n}.                 \tag{12}
\]

The endpoint follows by continuity in tau. Applying (12) both to v and its
folded query gives the same bound for |f_n(t,v)-f_n(t,v-tilde)|.
Equation (12) misses the target by sqrt(log n). It cannot be presented as
the requested root-width theorem by changing a constant.

## 5. Why the missing step requires additional neural structure

The deterministic Lipschitz bound (5) alone cannot give the desired
uniformity under a family of active translations. Here is a precise
counterexample to that proposed general lemma, not to the canonical model.

For large n, choose N=floor(sqrt(n)/(400 sqrt(log(en)))) and
D=100 sqrt(log(en)). In R^n use coordinates z_0,z_1,...,z_N and define

\[
 \Psi_n(z)=\operatorname{clip}_{[-1,1]}
 \left\{\frac1{\sqrt n}\max_{1\le j\le N}
       (z_j-|z_0-jD|)\right\}.                          \tag{13}
\]

Each function inside the maximum has Lipschitz constant sqrt(2), and maximum
and clipping preserve that bound. Thus Psi_n is bounded and has Lipschitz
constant sqrt(2/n). Choose active matrix A_V=sqrt(n)e_0, one passive
Gaussian column g, p_j=jD/sqrt(n)<=1/4, and s_j=sqrt(1-p_j^2).
These are legitimate unit-query coordinates (p_j,s_j). At these queries,
on the event max_(0<=i<=N)|g_i|<=D/10, the jth term uniquely wins: its
value is s_jg_j-|s_jg_0|, whereas every other term loses at least a fixed
fraction of D. Therefore

\[
 \Psi_n(A_Vp_j+s_jg)
       =\frac{s_j}{\sqrt n}(g_j-|g_0|).                 \tag{14}
\]

The exceptional probability is at most C n^(-49) for large n by the
Gaussian tail bound and a union bound. Its contribution to
each mean is o(n^(-1/2)) because Psi_n is bounded. Consequently the centered
values in (14) equal
s_j(g_j-|g_0|+E|g_0|)/sqrt(n)+o(n^(-1/2)). The maximum of N independent
standard Gaussians exceeds c sqrt(log N) with probability tending to one:
integrating the Gaussian density on [a,a+1/a] gives a tail lower bound
c a^(-1)exp(-a^2/2), and (1-p)^N<=exp(-Np). Since g_0 remains tight,

\[
 \sup_j|\Psi_n(A_Vp_j+s_jg)
           -\mathbb E\Psi_n(A_Vp_j+s_jg)|
       \ge c\sqrt{\log n/n}                            \tag{15}
\]

with probability tending to one. The corners can be smoothed without
changing these scales or the Lipschitz bound by convolution at a radius
o(1); this variant is smooth. No assertion is made that (13) is a canonical
Gaussian initialized neural network, has the inherited analytic query strip,
or can arise from its training rule. Its logical force is only that the
gradient norm, bounded output, and active-matrix operator bounds used in the
naive argument leave a real uniformity gap.

The existing analytic source theorem has a shrinking polylogarithmic query
strip. It controls coordinate approximation and hence the older compression
theorem. It does not itself supply width-independent high-moment increment
bounds for the *centered conditional output* in the active-input and time
variables. A finite analytic interpolation grid followed by fixed-slice
concentration still introduces a growing entropy factor, even if that factor
can be reduced to sqrt(log log n). Neither factor is allowed in (2).

There is a second, independent interface issue. Gaussian averaging cannot
replace the existing neuron source vectors in its deterministic bridge.
For example, with phi_1=tanh, u=0, and s=1,
E_G h^(1)(v)=0 but n^(-1)||h^(1)(v)||_2^2 converges to
E tanh(g)^2>0. Coordinate errors are of order one, whereas that bridge
requires n^(-1) source accuracy. Cancellation in the scalar output needs
a new output-level argument such as (2); it cannot be imported as a source
approximation statement.

## 6. Conditional construction if the missing estimate is supplied

If k>0, restrict the original realized network to V+span{e}. In the
orthonormal coordinates of that D=r+1 dimensional subspace, its first
matrix is [A_V,G e-coordinate], with independent standard Gaussian entries
at initialization. Its hidden matrices, readout, and training trajectory
are exactly those of the original model. Every training input lies in the
equatorial copy of V. Its initialized training covariance and gap are
unchanged, because all pairwise training inner products are unchanged.

The existing theorem therefore compresses this *same realized restricted
network* with its autonomous corrected-readout optimizer, total storage

\[
 C\lambda^{-2}[\log(en)]^{2[D(L+5)+1]}+Cm(d+1)+O(dr),    \tag{16}
\]

and root-width error on the restricted sphere, for all time and at the
endpoint. Constants depend on fixed structural dimension D and depth.
The O(dr) term stores the orthonormal projection. If (2) were proved,
evaluate the compressed model at (U^top v,||P_(V-perp)v||). The triangle
inequality would transfer its root-width guarantee to every original
query. Training still uses its own residuals and genuinely evolving hidden
matrices, with no original-width state retained.

The query transform in this construction computes a Euclidean norm. It is
a fixed deterministic preprocessing operation. If the representation
contract insists on an exactly linear first layer in the original d input
coordinates, that additional architectural requirement is not automatically
met by this construction. One must either allow the explicit fixed radial
preprocessing or prove an admissible replacement and count its storage.
This issue is separate from proving (2).

When r=d, there are no passive directions and no dimension improvement.
When d-r=1, D=d, so folding is also unnecessary. A useful exponent reduction
requires r+1<d. On training inputs alone, exact restriction to V already
works with dimension r, but that is a strictly smaller query domain.

## 7. Claim status and the next necessary estimate

| Claim | Status | Scope |
|---|---|---|
| Passive first-layer columns remain fixed and independent of training | Proved | Exact finite model |
| Conditional mean depends only on active input and passive radius | Proved | Every time, including the endpoint |
| Fixed-slice supremum over passive directions is O_P(n^(-1/2)) | Proved | Equation (10); fixed t,u,s |
| Integrated test squared error is O(n^(-1)) | Proved | Equation (11); passive-independent test measure |
| Whole-query/all-time passive replacement costs at most sqrt(log(n)/n) | Proved from supplied real path bounds | Equation (12) |
| Whole-query/all-time passive replacement costs O(n^(-1/2)) | Open | Equation (2) |
| Existing source-coordinate bridge directly permits Gaussian averaging | Invalid route | Order-one first-layer source defect |
| d can be replaced by r+1 in the full requested theorem | Conditional | Requires (2), plus the fixed query-map contract |

The highest-leverage missing theorem is tightness at root-width scale of
the centered process
sqrt(n)(f_n(t,v)-overline f_n(t,U^top v,||P_(V-perp)v||)), uniformly in
physical time and active input. A useful sufficient route would prove
width-independent high-moment increments in those variables, with an
integrable time/parameter activity metric. The passive-direction increments
are already supplied by (9). Any completion must use the actual Gaussian
neural initialization and training equations beyond the deterministic
gradient bound; no such completion is claimed here.

## 8. Bounded post-freeze Gaussian Sobolev attempt

This separately authorized appendix leaves Sections 1--7's claim levels
unchanged. The additional inputs DEEP_COMPLEX_SOURCE.md and
LABEL_SEPARATE_BUDGETS.md were read completely. The coordinator also supplied
the asymmetric Schatten trace observation below. No other route report was
read. The Sobolev route removes time entropy and identifies a finite list of
sufficient mixed estimates. Those estimates remain unproved here for L>=2.

### 8.1 An exact sufficient estimate without a time net

Use the periodic sphere parameterization v=v(theta), theta in T^(d-1), and
put z(theta)=E^top v(theta). Fix an integer h>(d-1)/2. Fourier expansion and
Cauchy--Schwarz give, with normalized torus measure,

\[
 \|g\|_\infty^2\le C_{d,h}\sum_{|\alpha|\le h}
                   \int|\partial_\theta^\alpha g|^2.     \tag{17}
\]

Indeed sum_j(1+|j|^2)^(-h) is finite, and the complementary weighted
Fourier square sum is equivalent to the displayed derivative norm.

For a driving training sample a, the residual-free forward directions are

\[
 R_a^{(1)}(v)=\delta_a^{(1)}(v_a^\top v),\qquad
 Q_a^{(\ell)}(v)=\phi_\ell'(z^{(\ell)}(v))\odot R_a^{(\ell)}(v),
\]
\[
 R_a^{(\ell)}(v)=\delta_a^{(\ell)}
       \frac{h_a^{(\ell-1)\top}h^{(\ell-1)}(v)}n
       +W^{(\ell)}Q_a^{(\ell-1)}(v),\qquad \ell\ge2.     \tag{18}
\]

These are exactly the source note's directions. Differentiating the readout
and hidden features with the actual parameter flow gives the scalar kernel

\[
 K_a(t,v)=\frac1n\left[
 h^{(L)}(t,v)^\top h_a^{(L)}(t)+w(t)^\top Q_a^{(L)}(t,v)\right],
 \qquad \partial_t f_n(t,v)=\frac2m\sum_a c_a(t)K_a(t,v). \tag{19}
\]

Given F, all c_a and training vectors in these equations are independent
of G. Define b_a=nK_a and its n-vector derivative
q_a=gradient_(z^(1)) b_a, keeping the explicit scalar v_a^top v fixed
during this first-preactivation derivative. The only G dependence is through
A_V(t)U^top v+G z(theta), so

\[
 \nabla_G K_a(t,v(\theta))
                 =q_a(t,v(\theta))z(\theta)^\top/n.      \tag{20}
\]

Define the concrete, nonnegative F-measurable mixed derivative energy

\[
 B_a(t;F)^2=\frac1n\sum_{|\alpha|\le h}\int
 \mathbb E_G\left\|\partial_\theta^\alpha
       [q_a(t,v(\theta))z(\theta)^\top]\right\|_F^2d\theta.
                                                               \tag{21}
\]

The rotation argument also gives a Gaussian variance inequality for any
square-integrable differentiable H with square-integrable gradient:

\[
 \|H-\mathbb E_GH\|_{L^2(G)}
                   \le(\pi/2)\|\nabla_GH\|_{L^2(G;F)}. \tag{22}
\]

To prove it, rotate between independent whole Gaussian matrices, condition
the directional derivative on the current matrix, integrate along the
quarter-circle, and apply Jensen to subtract the independent copy. Every
fixed finite-width neural derivative here has the needed integrability:
bounded activation derivatives and finitely many Gaussian linear factors
give finite moments.

Apply (22) to each angular derivative of K_a, then (17) and (20):

\[
 \left\|\sup_v\sqrt n|K_a(t,v)-\mathbb E_GK_a(t,v)|
       \right\|_{L^2(G)\mid F}\le C_{d,h}B_a(t;F).       \tag{23}
\]

The initial readout is zero. Center (19) conditional on F, integrate it
in physical time, and apply Minkowski to obtain on every finite horizon

\[
 \left\|\sup_{t,v}\sqrt n
 |f_n(t,v)-\overline f_n(t,U^\top v,\|E^\top v\|)|
       \right\|_{L^2(G)\mid F}
 \le\frac{C_{d,h}}m\sum_a\int_0^\infty
                              |c_a(t)|B_a(t;F)\,dt.     \tag{24}
\]

Thus a sufficient missing estimate is, with fixed prescribed confidence
over F and a width-independent constant,

\[
 \frac1m\sum_a\int_0^\infty|c_a(t)|B_a(t;F)\,dt
                                \le C_{\rm data,\eta}.  \tag{25}
\]

Uniform B_a<=C_data would suffice because m^(-1)sum_a|c_a|<=rho and total
residual activity is bounded. Finiteness in (25) permits monotone passage
in (24) to all time; parameter convergence supplies the endpoint. Conditional
Markov then proves the root-width passive averaging statement, and the
triangle inequality gives the folded comparison (2). No time net or time
derivative of a residual quotient is required.

### 8.2 The mixed product needed even at derivative order zero

Let J_ell=D_(z^(1)) z^(ell), with J_1=I. These n-by-n Jacobians have bounded
operator norm. Use k^(ell)(t,v), delta^(ell)(t,v) for the query's backward
fields. Differentiating (18) and propagating the readout pairing backward
gives the exact identity

\[
 \begin{aligned}
 q_a={}&J_L^\top[\phi_L'(z^{(L)})\odot h_a^{(L)}]\\
 &+\sum_{\ell=1}^LJ_\ell^\top
       [\phi_\ell''(z^{(\ell)})\odot R_a^{(\ell)}\odot k^{(\ell)}]\\
 &+\sum_{\ell=2}^L
      \frac{\delta^{(\ell)\top}\delta_a^{(\ell)}}n
      J_{\ell-1}^\top
       [\phi_{\ell-1}'(z^{(\ell-1)})\odot h_a^{(\ell-1)}].
 \end{aligned}                                               \tag{26}
\]

Unlabeled fields in this formula belong to the query. The middle line
comes from the differentiated gate in Q_a. The last line comes from the
differentiated scalar feature pairing in R_a. At the first layer R_a^(1)
is fixed under this preactivation derivative and adds no direct term.

The first and last lines have bounded RMS using the known Jacobian,
feature and backward RMS bounds. The remaining bound is

\[
 \frac1n\|q_a(t,v)\|_2^2\le C_{\rm data}\left[
 1+\sum_{\ell=1}^L\frac1n\sum_i
             |R_{a,i}^{(\ell)}(t,v)k_i^{(\ell)}(t,v)|^2\right].
                                                               \tag{27}
\]

Separate RMS estimates do not control these products. Empirical fourth
moments of both factors would suffice at order zero. Higher alpha in (21)
requires finite moments of their angular derivatives and associated forward
jets, only up to the fixed finite order h. Repeated RMS multiplication is
not a valid substitute.

### 8.3 Source interfaces and the remaining extension

The separate budgets control every fixed empirical moment of each training
carrier, and hence all training Hessian Schatten factors. They do not
contain passive-query carriers. The source note gives R_a and first angular
response RMS bounds and uniform polylogarithmic coordinate caps; it does
not state the mixed estimates (21).

There is a useful trace sharpening. In source equation (23), the endpoints
are DQ (or the derivative of an angular source) and the training feature
derivative C_a. Source equation (12) bounds the former in normalized
Schatten-2, while the latter has bounded operator norm and rank at most n.
For a Dyson term with j>=1 training Hessians, use Holder exponents 2 for
DQ, infinity for C_a, and 2j for each Hessian. Their reciprocals sum to one.
The j=0 term uses both endpoints in Schatten-2. The normalized training
Hessian moment estimate and the 1/j! factor sum at structurally small
residual activity. The trace bound is therefore independent of the lower
coordinate cap A_p retained by the older symmetric Holder estimate.

This is compatible with obtaining fixed-point finite moments for first
forward and angular responses: their cavity Gaussian terms have bounded
variance, while their row shifts involve individual training carriers.
One must retain those individual coordinates before taking maxima and
pass their expectations through the stopped insertion estimates. This
appendix does not silently infer a completed moment theorem from the old
maximum bound.

Even after first forward moments, (21) needs passive-query backward
carriers and higher angular derivatives. A plausible extension monitors
a fixed passive query with an extra carrier budget and zero loss
coefficient, leaving training unchanged. Its insertion endpoints and
direct observable terms, followed by the higher query jets, still require
verification. The existing whole-query backward source result deliberately
uses the weaker sqrt(n) magnitude and does not supply that extension.
This bounded attempt has not completed it.

### 8.4 A fully controlled shallow check

For L=1, the criterion does close directly. This checks the mechanism but
does not answer the requested L>=2 problem. The readout equation and finite
residual activity give ||w||_infty<=C_data, and rowwise first-weight motion
gives sup_t||A_V(t)_(i,:)||<=||(A_0U)_(i,:)||+C_data. Equation (26) becomes

\[
 q_{a,i}=\phi_1'(z_i)h_{a,i}^{(1)}
       +w_i^2\phi_1'(z_{a,i})\phi_1''(z_i)(v_a^\top v). \tag{28}
\]

All activation derivatives of each fixed order are bounded. After h angular
derivatives, the squared row contribution in (21) is bounded by
C_(data,h)(1+||(A_0U)_(i,:)||+||G_(i,:)||)^(2h). Taking the passive Gaussian
expectation and averaging rows leaves a fixed-degree empirical moment of
independent fixed-dimensional Gaussian active rows. Its expectation is
bounded uniformly in width; Markov gives the desired prescribed-confidence
bound, uniformly in time and training index. Thus (25) and the whole-query,
all-time root-width passive averaging statement hold in this shallow case.

For deeper networks, dense forward and transpose mixing creates precisely
the products (27) and their finite query derivatives. Width-independent
moments for those quantities would finish this route. No population bias
assumption or integrated-test replacement has been used to bypass them.

## 9. Checked composition at the weaker square-root-logarithmic error

The coordinator requested this final composition check after the Sobolev
appendix. No further route search is undertaken. The conclusion below is
explicitly weaker in accuracy than the original requested theorem.

If r+1<d, set D=r+1 and choose the d-by-D orthonormal matrix [U,e]. The
restricted first weights are A'_0=A_0[U,e]. Each original Gaussian row
projected onto orthonormal columns is a D-vector of independent standard
Gaussians, with independence across rows and from every hidden matrix.
Thus this is exactly the canonical D-dimensional initialization, not a
new initialization coupled only in distribution. Its normalized training
inputs are v'_a=(U^top v_a,0) in S^(D-1); the canonical unnormalized inputs
are sqrt(D)v'_a. Pairwise training inner products and all initialized
covariances Q^(ell), hence gamma and lambda, are unchanged.

Projecting the exact first-weight update onto [U,e] proves that this
restricted model has exactly the original training hidden matrices,
readout, residuals, and physical clock. Its last first-weight column stays
fixed. Therefore the existing compression theorem applies directly to
this same realized restricted model, with its own autonomous compressed
residuals and learned hidden matrices.

After setup retain U (dr coordinates), the restricted compressed model,
and the training data as already counted. Evaluate a unit original query
by the fixed preprocessing map

\[
 v\longmapsto
 \left(U^\top v,\sqrt{\|v\|_2^2-\|U^\top v\|_2^2}\right).
                                                               \tag{29}
\]

Its radicand is nonnegative because U is orthonormal. It maps the unit
sphere to S^(D-1) and every training input to v'_a. The vector e is needed
only to form the initialized compressed coefficients and need not remain
in runtime storage. Current projection and norm work arrays require at
most O(d+r) real coordinates, absorbed in the retained data/projection
count. Exact-real setup and evaluation are the standing arithmetic model.
The fixed norm operation is an explicit architectural extension if an
exactly linear first layer in the original coordinates was required.

Combine the restricted root-width compression error with the proved
folding estimate (12), using failure budgets eta/2 each. Independence
between those two events is unnecessary. The triangle inequality gives

\[
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
    |f_C(t,v)-f_n(t,v)|
             \le C_{\rm data,\eta}\sqrt{\log(en)/n}.     \tag{30}
\]

All times and the endpoint are covered. With the currently supplied
source theorem the retained size in this weaker corollary is already

\[
 C\lambda^{-2}[\log(en)]^{2[D(L+5)+1]}
                    +Cm(d+1)+Cdr.                     \tag{31}
\]

If r+1>=d, use the original d-dimensional compressed network without
folding. Then D=d, no projection storage is needed, and its stronger
root-width accuracy implies (30). This proves (30)--(31) with
D=min(d,r+1) in all cases, under the stated fixed-preprocessing allowance.
The small-label constant can be the minimum of the structural constants
needed by the original training bounds and restricted compression; its
form remains Y<=c lambda.

The coordinator is separately developing a stronger source theorem with
joint time/query radius c[log(en)]^(-1/2). **Conditional on that theorem**
with the same label range, horizon C lambda^(-1)log(en), polynomial-in-n
coordinate magnitudes, the paired coefficient identities, and the existing
training-carrier comparison input, the improved exponent composes as follows.
At source tolerance n^(-1), temporal degree is
O(lambda^(-1)log(en)^(5/2)) and each angular degree is O(log(en)^(3/2)),
once log(e/lambda)<=log(en). The D-dimensional source span then has
dimension O(lambda^(-1)log(en)^(3D/2+1)); squaring its size in the existing
autonomous runtime gives

\[
 \mathrm{size}\le C\lambda^{-2}[\log(en)]^{3D+2}
                            +Cm(d+1)+Cdr.              \tag{32}
\]

The associated accuracy remains (30). The new exponent in (32) is conditional
only on the incoming stronger source theorem and its stated interfaces;
the folding calculation adds no unproved fluctuation estimate. Neither
(30)--(31) nor conditional (32) supplies strict C/sqrt(n) accuracy on the
original full sphere. Removing the remaining sqrt(log n) factor still
requires a new estimate such as (25).
