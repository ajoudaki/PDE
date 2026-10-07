# A finite-network angular obstruction to the current compact architecture

2026-10-05. Author-derived theorem, not established book material. The proof
is self-contained apart from elementary Gaussian integration, Fourier
inversion for integrable transforms, polynomial harmonic decomposition,
and the bounded-variable concentration inequality proved below. Its actual
author check and frozen source hash are recorded in CHECK.md.

## 1. Reference model and the precise approximation being tested

Let d >= 2 be fixed and let v = x/sqrt(d) range over the unit sphere.
The canonical reference has two width-n hidden layers,

\[
 h_n(t,v)=\tanh(A_n(t)v),\qquad
 g_n(t,v)=\tanh(W_n(t)h_n(t,v)),\qquad
 f_n(t,v)=w_n(t)^\top g_n(t,v)/n.
\]

Initially A_n has independent N(0,1) entries, W_n has independent
N(0,1/n) entries, the arrays are independent, and w_n=0. The m training
vectors v_a are orthonormal, so m <= d. Write r_a=f_n(t,v_a)-y_a and
Y=||y||_2/sqrt(m). The squared mean loss and mobilities (n,1,n) give

\[
 \dot w_n=-\frac2m\sum_a r_ag_{n,a},\qquad
 \dot W_n=-\frac2{mn}\sum_a r_a d_a h_{n,a}^\top,\qquad
 \dot A_n=-\frac2m\sum_a r_a\ell_a v_a^\top,
\]

where d_a=w_n odot (1-g_{n,a}^2) and
ell_a=(1-h_{n,a}^2) odot (W_n^T d_a). These equations only specify the
reference: the new lower bound uses t=0 and therefore does not require a
fitting theorem, a sign restriction, or a label-size restriction. It
applies, in particular, throughout the requested small-label setting.

The historical compact construction chooses fixed linear source spaces in
neuron-coordinate space. One required source is h_n(t,v), uniformly over
queries and the source horizon. Each coordinate is approximated to 1/n,
which in particular bounds the empirical RMS error by 1/n. The theorem
below allows the weaker RMS accuracy C/sqrt(n). It permits **any** source
space, chosen using all initialized weights and data, with no independent
sampling or polynomial-basis restriction.

## 2. Theorem

Fix d >= 2, C < infinity, and 0 < delta < 1. For sufficiently large n,
with probability at least 1-delta, simultaneously for every linear
subspace V of R^n,

\[
 \sup_{v\in S^{d-1}}
 \frac{\operatorname{dist}(h_n(0,v),V)}{\sqrt n}
       \le\frac C{\sqrt n}
 \quad\Longrightarrow\quad
 \boxed{\dim V\ge c_d(\log n)^{3(d-1)/2}.}                 \tag{1}
\]

Here c_d>0 depends only on d; the eventual width can also depend on C
and delta. The probability concerns the actual finite first-layer
initialization, not a population surrogate assumed close to it. The
event remains valid after allowing V to depend on all other randomness.
There is no simultaneous statement over independently sampled widths.

For the current implementation retaining a full N-by-N metric on at least
dim V selected coordinates, this implies the all-retained storage bound

\[
 \boxed{\operatorname{storage}\ge
              c_d(\log n)^{3d-3}.}                       \tag{2}
\]

Equation (2) is a consequence for that storage format, not an information
lower bound for arbitrary encodings of the metric. It does not by itself
lower-bound learned state: the metric is fixed. Changing the representation
of the metric or dispensing with full-feature approximation changes the
contract and can escape this conclusion.

## 3. Gaussian Hermite coefficients of tanh

Let H_p be the probabilists' Hermite polynomial, defined by

\[
 e^{tz-t^2/2}=\sum_{p\ge0}H_p(z)t^p/p!.
\]

For a standard normal Z put
b_p=E[tanh(Z)H_p(Z)]/sqrt(p!). The normalized Hermite polynomials are an
orthonormal basis in Gaussian L^2. Orthogonality follows by taking the
expectation of two generating functions. For completeness, an L^2
function orthogonal to every polynomial has identically zero Gaussian
Laplace transform: Cauchy--Schwarz permits its entire power series, whose
coefficients vanish. Its Fourier transform then vanishes, so the function
is zero. Thus Parseval applies and sum b_p^2=E tanh^2(Z) <= 1.

We first establish the useful identity

\[
 \tanh z=\int_0^\infty\frac{\sin(tz)}{\sinh(\pi t/2)}\,dt
                         \quad(z\in\mathbb R).           \tag{3}
\]

Here is a derivation. For t>0, integrate sech^2(z)e^{-itz} around the
rectangle of height -i*pi and width [-R,R], oriented clockwise. The
vertical integrals vanish as R tends to infinity, and the lower edge is
e^{-pi*t} times the upper edge with reversed orientation. The only pole
is the double pole z=-i*pi/2. Since sech^2(z) has leading term
-(z+i*pi/2)^-2 there, the residue of the product is
i*t*exp(-pi*t/2). The residue theorem gives

\[
 \int_{\mathbb R}\operatorname{sech}^2(z)e^{-itz}\,dz
       =\frac{\pi t}{\sinh(\pi t/2)}.
\]

Both the function and this transform are integrable. Fourier inversion,
evenness, and integration from 0 to z give (3). All the latter integrals
are absolutely convergent, including at t=0.

The Hermite generating function gives
E[H_p(Z)e^{itZ}]=(it)^p e^{-t^2/2}. Substitution in (3) proves, for odd p,

\[
 |b_p|=\frac1{\sqrt{p!}}
       \int_0^\infty
       \frac{t^p e^{-t^2/2}}{\sinh(\pi t/2)}\,dt.         \tag{4}
\]

There is no cancellation: the sign is (-1)^((p-1)/2). Fubini follows
near zero from |sin(tZ)| <= t|Z|, and at infinity from exponential
decay of 1/sinh(pi*t/2). Even b_p vanish by oddness.

Restrict (4) to sqrt(p) <= t <= sqrt(p)+1. On this interval,

\[
 t^p\ge p^{p/2},\quad
 e^{-t^2/2}\ge e^{-p/2-\sqrt p-1/2},\quad
 \sinh(\pi t/2)^{-1}\ge2e^{-\pi(\sqrt p+1)/2}.
\]

The elementary sum-integral estimate
log(p!) <= p log p-p+1+log p supplies
sqrt(p!) <= sqrt(e*p)*(p/e)^(p/2). Consequently, with absolute positive
constants c and C,

\[
 \boxed{b_p^2\ge c p^{-1}e^{-C\sqrt p}
                   \quad(p\ge1\text{ odd}).}             \tag{5}
\]

Only the exponent sqrt(p), not the polynomial prefactor, matters below.

## 4. Spherical eigenvalues, derived directly

Let sigma be normalized surface measure on S^{d-1}. A real spherical
harmonic of degree k is the restriction of a homogeneous harmonic
polynomial of degree k. These finite-dimensional spaces are orthogonal:
the spherical Laplacian has eigenvalue -k(k+d-2), and integration by
parts makes it self-adjoint. Harmonic decomposition of homogeneous
polynomials gives their dimensions

\[
 \dim\mathcal H_k
 =\binom{k+d-1}{d-1}-\binom{k+d-3}{d-1}.                 \tag{6}
\]

For clarity, the decomposition follows recursively by applying the
Laplacian to |x|^(2j) times a harmonic homogeneous polynomial of degree l:
the multiplier is 2j(2l+2j+d-2), nonzero for j>0. Subtract those terms
to leave a harmonic polynomial. Counting monomials gives (6), with
out-of-range binomial coefficients interpreted as zero. For d=2 each
positive degree has dimension two.

For p>=k of the same parity, the kernel (v dot w)^p has the following
eigenvalue on H_k:

\[
 \mu_{p,k}
 =\frac{p!\,\Gamma(d/2)}
 {2^p((p-k)/2)!\,\Gamma((p+k+d)/2)}.                    \tag{7}
\]

It is zero for p<k or opposite parity. To verify (7), let P be a
homogeneous harmonic polynomial of degree k and G a standard d-variate
Gaussian. Gaussian translation gives

\[
 E[e^{t v\cdot G}P(G)]
 =e^{t^2/2}E[P(G+tv)]=e^{t^2/2}t^kP(v).
\]

The middle expectation equals P(tv) because Gaussian averaging is the
finite polynomial series exp(Delta/2)P, and Delta P=0. Equating
coefficients of t^p and writing G=RU, where U is uniform on the sphere
and independent of R, gives (7), using the directly integrated radial
moment E R^(p+k)=2^((p+k)/2) Gamma((p+k+d)/2)/Gamma(d/2).

We need a lower bound when k is odd. Write p=2q+1, k=2j+1. Formula (7)
implies exactly

\[
 \frac{\mu_{p,k}}{\mu_{p,1}}
       =\prod_{r=0}^{j-1}\frac{q-r}{q+1+d/2+r}.          \tag{8}
\]

For p>=C_d k, take C_d large enough that each factor is 1-u_r with
0<=u_r<=1/2. The inequality log(1-u)>=-2u then proves

\[
 \frac{\mu_{p,k}}{\mu_{p,1}}
                 \ge\exp[-C_d k^2/p].                  \tag{9}
\]

Indeed u_r=(1+d/2+2r)/(q+1+d/2+r), and its sum is at most
C_d(j+j^2)/p; j=0 gives the empty product one.

The k=1 eigenvalue is E[U_1^(p+1)]. The density of U_1 is
Gamma(d/2)/(sqrt(pi) Gamma((d-1)/2)) times
(1-u^2)^((d-3)/2). Integrate over
1-1/p <= u <= 1-1/(2p), for p>=2. On that interval u^(p+1) is
bounded below by an absolute positive constant and 1-u^2 is between
constant multiples of 1/p. This argument also covers d=2, where the
density exponent is negative. Hence

\[
 \mu_{p,1}\ge c_d p^{-(d-1)/2},\qquad
 \mu_{p,k}\ge c_d p^{-(d-1)/2}e^{-C_d k^2/p}.            \tag{10}
\]

Now define the covariance kernel of one actual initialized neuron,

\[
 K(v,w)=E_{a\sim N(0,I_d)}[\tanh(a\cdot v)\tanh(a\cdot w)]
       =\sum_{p\text{ odd}}b_p^2(v\cdot w)^p.            \tag{11}
\]

The last equality follows by the joint Gaussian Hermite generating
function. Since sum b_p^2<=1, it converges absolutely and uniformly.
Thus its eigenvalue on H_k for odd k is
nu_k=sum_{p>=k, p odd} b_p^2 mu_{p,k}, a sum of nonnegative terms.

Choose an odd p between k^(4/3) and k^(4/3)+2. For sufficiently large
k (depending only on d), (10) applies. Retaining only this p in the
sum, (5) and (10) give

\[
 \boxed{\nu_k\ge c_d k^{-2(d+1)/3}
                  e^{-C_d k^{2/3}}
                     \quad(k\ge1\text{ odd}).}           \tag{12}
\]

The finitely many remaining k are absorbed by decreasing c_d: each
nu_k is strictly positive by its p=k term. No independence assertion
about trained neurons has entered this calculation.

## 5. Transfer to every adaptive subspace of the finite network

Choose a small constant eta_d>0 and set

\[
 k_n=\lfloor\eta_d(\log n)^{3/2}\rfloor,\qquad
 D_n=\sum_{1\le k\le k_n,\ k\text{ odd}}\dim\mathcal H_k.
\]

Equation (6) implies D_n >= c_d k_n^(d-1) for sufficiently large n,
and also D_n <= C_d(1+k_n)^(d-1). One can see the lower bound by
summing the positive dimensions for odd k between k_n/2 and k_n;
for d=2 it is the direct count of two-dimensional spaces.

Choose eta_d such that the coefficient C_d eta_d^(2/3) in (12) is
less than 1/8. Polynomial factors in k_n contribute only log log n to
their logarithm. For sufficiently large n this ensures

\[
                \min_{k\le k_n,\ k\text{ odd}}\nu_k
                                \ge n^{-1/4}.           \tag{13}
\]

Let Y_alpha be an orthonormal basis of these odd harmonics. For neuron i,
whose initialized row is a_i, form the vector of coefficients

\[
 B_{i\alpha}=\int\tanh(a_i\cdot v)Y_\alpha(v)d\sigma(v).
\]

Bessel's inequality and |tanh|<=1 give sum_alpha B_(i alpha)^2<=1.
The rows are independent. Equations (7) and (11) show that
E[B_(i alpha)B_(i beta)] is diagonal, with corresponding entries nu_k.

For independent random variables in [-1,1], the bounded-variable
inequality gives
P(|n^-1 sum_i (X_i-E X_i)|>u)<=2exp(-n u^2/2).
For completeness its exponential-moment step is
E exp(t(X-E X))<=exp(t^2/2): the second derivative of the logarithm
of this moment generating function is a variance under a tilted law
still supported on [-1,1], hence at most one; its value and first
derivative at zero vanish. Chernoff optimization and the two signs give
the displayed inequality.

Apply it to each B_(i alpha)B_(i beta) in [-1,1], then take a union
bound and use operator norm <= D_n times the largest entry. Except on
an event of probability at most

\[
       2D_n^2\exp\{-\sqrt n/(8D_n^2)\},                 \tag{14}
\]

we obtain

\[
 \left\|B^\top B/n-E[B^\top B/n]\right\|_{\rm op}
                 \le\tfrac12 n^{-1/4},\qquad
 B^\top B/n\succeq\tfrac12 n^{-1/4}I_{D_n}.             \tag{15}
\]

Indeed use entry tolerance n^-1/4/(2D_n). The probability (14) tends
to zero, since D_n grows only as a power of log n. This proves an
actual finite-network statement; it does not assume the network is
already close to a population flow.

Let P_V be the Euclidean orthogonal projector onto any V of dimension r.
Apply Bessel to each coordinate of (I-P_V)h_n(0,v):

\[
 \int\frac{\|(I-P_V)h_n(0,v)\|_2^2}{n}\,d\sigma(v)
       \ge\frac{\|(I-P_V)B\|_F^2}{n}
       \ge (D_n-r)_+\,\tfrac12 n^{-1/4}.                \tag{16}
\]

For the last inequality, write B/sqrt(n)=U Sigma V^T by singular value
decomposition. Its D_n singular values squared are at least
n^-1/4/2 by (15). Consequently the trace of
Sigma^2 U^T(I-P_V)U is at least n^-1/4/2 times
D_n-tr(U^T P_V U), and this last trace is at most r.

On the event (15), (16) holds **simultaneously for all V**, including
spaces selected after seeing every row and any additional randomness.
The hypothesis of (1) bounds its left side by C^2/n. If r<D_n this
contradicts (16) for sufficiently large n. Therefore r>=D_n, proving
(1). The retained full symmetric metric has at least N(N+1)/2 scalar
slots and its exact source isometry requires N>=r. This proves (2) for
that implementation.

## 6. Consequences for transformed time and limits of the theorem

Every source approximation uniform throughout training includes the same
map v -> h_n(0,v). A monotone clock change, with any choice of its
initial coordinate, leaves that map unchanged. Using Legendre rather
than Chebyshev changes neither this necessary subspace nor the fact that
all degree-p polynomials in one fixed coordinate span the same space.
Even a joint, non-tensor choice of all time/query coefficients cannot
evade (1) if it still produces a fixed source space satisfying that
accuracy contract.

The previous all-retained upper exponent is 3d+2. The present obstruction
has exponent 3d-3: their difference is five, independent of d. Thus the
leading factor three in d is unavoidable **within the full-feature,
quadratic-metric architecture**. In particular for every fixed d>=2,
this architecture cannot have O((log n)^d) or
O((log n)^sqrt(d)) all-retained storage at the stated source accuracy.
This assertion allows arbitrary multiplicative constants depending on
fixed data; the powers of log n still separate as n tends to infinity.

Orthogonality does not change the initialized query-feature family.
Taking m=d is an allowed orthogonal configuration and avoids conflating
this obstruction with the separate possibility of reducing the effective
query dimension when m<d. The proof also holds for the full d-dimensional
source family when m<d. A construction which replaces that family by a
folded or averaged observable must instead be analyzed on its own terms.

The theorem does **not** show that the prediction approximation requested
by the user needs this much storage. At initialization f_n=0, regardless
of this source complexity. Cancellation at the readout and the training
signal can make predictions much simpler. Nor is (2) a lower bound on
the number of moving states of every autonomous model, a lower bound at
the fitted endpoint, or an Omega(n) result. Those would be different
theorems and are not inferred here.
