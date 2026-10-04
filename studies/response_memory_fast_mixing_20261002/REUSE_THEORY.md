# A spectral obstruction to replacing the initialized environment

Claim type: exact finite-dimensional identity and asymptotic consequence under
explicit Gaussian-probe assumptions. Author derivation, not independently
checked yet. This is NOT a trained-network universality theorem.

The paper retains the same initialized matrix in its forward and transpose
actions. A replacement intended only to reproduce one forward random feature
map can therefore target the wrong object. Here is a concrete discriminator
and a candidate repair that retain that scientific distinction.

## 1. Exact nonlinear return energy

Let W be a deterministic n-by-n real matrix, C=W W^T, and assume C_ii=1.
Let h~N(0,I_n), independent of W if W is itself random. Let psi be odd and
square-integrable under a standard normal Z. Define

    v = E psi(Z)^2,       a = E Z psi(Z),
    mu4 = tr(C^2)/n,      epsilon = max_{i != j}|C_ij|.

For n=1 take epsilon=0. Then

    E ||W^T psi(W h)||²/n = v + a²(mu4-1) + R,
    0 <= R <= (v-a²) epsilon²(mu4-1).                    (1)

Here psi acts coordinatewise. The formula is conditional on W and uses no
independence among the coordinates of W h. In particular mu4 is the average
fourth power of the singular values, not the fourth moment of individual
entries. Since C is a correlation matrix, mu4>=1 and epsilon<=1.

Proof. Define normalized probabilists' Hermite polynomials e_k by
`exp(tz-t²/2)=sum He_k(z)t^k/k!`, e_k=He_k/sqrt(k!). Gaussian generating
functions give E e_k(Z)e_l(Z)=1[k=l]. For jointly unit-variance Gaussian
Z1,Z2 with covariance c, their joint generating function after the two
normalizations is exp(c s t), hence

    E e_k(Z1)e_l(Z2) = 1[k=l] c^k.                    (2)

These polynomials are complete in Gaussian L². One verification is that a
function orthogonal to all polynomials is orthogonal to exp(tZ-t²/2) for
all real t by its convergent L² generating series. The Gaussian-weighted
signed measure has an entire Laplace transform (Cauchy--Schwarz provides
an integrable majorant on every bounded complex disk); all its derivatives
at zero vanish. Its Fourier transform is therefore zero. Fourier uniqueness
for finite measures follows by convolving with Gaussian approximate identities
and passing to their weak limit, so the function vanishes almost everywhere.

Expand psi=sum c_k e_k in L². Oddness kills the even coefficients; c_1=a
and sum_{k odd}c_k²=v. Equation (2), extended by L² approximation and
Cauchy--Schwarz, gives

    E psi(Z1)psi(Z2) = sum_{k odd} c_k² c^k.

Since W h has covariance C,

    E ||W^T psi(W h)||²/n
       = (1/n) sum_{i,j} C_ij E psi((Wh)_i)psi((Wh)_j).

Diagonal terms total v. The k=1 off-diagonal terms total a²(mu4-1).
All remaining terms have even powers C_ij^(k+1), k>=3, so are nonnegative.
Each is at most epsilon² C_ij² because |C_ij|<=1. Summing their coefficients
and then the off-diagonal entries proves (1). If a=0, this particular leading
spectral discriminator vanishes; no separation is asserted then.

## 2. Fast structured environments with a prescribed spectrum

Let H be the normalized Sylvester Hadamard matrix at a power-of-two width,
so H^T H=I and every entry has magnitude 1/sqrt(n). Let D_L,D_R,D_S be
diagonal sign matrices and P a permutation. Set

    W = D_L H diag(s) D_S P H D_R,
    (1/n) sum_i s_i² = 1.                              (3)

Its singular values are exactly |s_i|, its covariance diagonal is exactly1,
and its forward and transpose actions use the same stored arrays in reverse
order. It needs O(n) fixed scalars and O(n log n) arithmetic per vector.
This is a mathematical operation count; implementation speed is a separate
measurement. A random permutation of the s_i is included before forming (3).

For bounded prescribed s_i² and a uniform random permutation, epsilon tends
to zero in probability. Here is a self-contained bound. For i!=j the product
of Hadamard row signs has half+1 and half-1, so C_ij up to an outer sign is

    (2/n) sum_{k=1}^{n/2} lambda_{pi(k)} - mean(lambda),
    lambda_i=s_i² in [0,M].

Reveal the first n/2 elements of a random permutation. If N=n, r=n/2,
the Doob martingale increment of the partial-sample sum at reveal k is
`(N-r)/(N-k) * (revealed value - previous remaining mean)`, with absolute
value <=M. After multiplying by2/n each increment has magnitude <=2M/n.
For a mean-zero variable bounded in [-c,c], convexity bounds its conditional
exponential moment by cosh(tc)<=exp(t²c²/2). Multiplying these conditional
bounds and optimizing the Chernoff parameter gives

    P(|C_ij|>t) <= 2 exp(-n t²/(4M²)).                 (4)

A union bound over fewer than n² entries gives epsilon=O_P(sqrt(log n/n)).
This argument does not need independence of the covariance entries.
Combining (1) and (4), if mu4 tends to a finite limit m4,

    E_h ||W^T psi(W h)||²/n -> v + a²(m4-1)            (5)

in probability over the spectrum permutation. This concerns the conditional
expectation over Gaussian h; concentration for one probe is not proved here.

Choose s_i as midpoint quantiles of the quarter-circle density
`sqrt(4-s²)/pi`, 0<=s<=2, followed by exact RMS normalization. Riemann-sum
convergence of bounded continuous functions gives mean s²->1 and mean s⁴->2;
the two integrals are1 and2 by s=2sin(theta). Its CDF is
`[s sqrt(4-s²)/2 + 2 asin(s/2)]/pi`. Thus m4=2 and (5) gives v+a².
Flat s_i=1 instead gives C=I and exactly v at every width.

## 3. The iid Gaussian reference, and the Fastfood distinction

For iid W_ij~N(0,1/n), independent h~N(0,I_n), write s_h=||h||/sqrt(n).
Condition on h and z=W h. Gaussian linear regression gives

    W = z h^T/||h||² + G (I-hh^T/||h||²),

where G has iid N(0,1/n) entries independent of z. Conditional on h the
z_i are iid N(0,s_h²). The two contributions to W^T psi(z) are orthogonal,
and integrating G yields

    E_G ||W^T psi(z)||²/n
      = (z^T psi(z))²/(n||h||²) + (n-1)||psi(z)||²/n².

For psi=tanh, set v_s=E psi(sZ)², a_s=E[sZ psi(sZ)],
b_s=E[(sZ)² psi(sZ)²]. Integrating z gives exactly

    (1-1/n) a_s²/s² + b_s/(n s²) + (1-1/n)v_s.

At s=0 use the continuous limit (the event h=0 has probability zero).
All terms are bounded since |psi|<=1 and a_s²/s²<=v_s. As s_h->1 in
probability, continuity and boundedness imply convergence to v+a².
Thus the spectrum-corrected fast operator matches this PARTICULAR Gaussian
return observable; the flat-spectrum replacement has an order-one gap a².

The two-Hadamard Gaussian-diagonal Fastfood core corresponds instead to
s_i=|g_i|/sqrt(mean g²), with iid g_i~N(0,1). Its mu4 tends to3 by the law
of large numbers, rather than2. Its largest squared singular value is
O_P(log n): Gaussian tail bounds and a union bound give max g_i²=O_P(log n),
while mean g²->1. Conditional use of (4) therefore still makes epsilon->0
(e.g. O_P(log(n)^(3/2)/sqrt(n))). Equation (5) gives v+2a².
This statement is for the explicitly specified Fastfood CORE, not every
variant, row rescaling, learned transform or implementation called Fastfood.
Its original static-kernel guarantees are not contradicted: they address a
different observable. The current study introduces no priority claim for this
spectral fact or for structured transforms generally.

For tanh, deterministic quadrature gives approximately v=0.39429449,
a=0.60570551. The limiting return energies are therefore approximately
0.39429 (orthogonal), 0.76117 (Gaussian/quarter-circle) and1.12805
(Gaussian-diagonal core). Their initial per-coordinate forward distribution
under the stipulated Gaussian probe is the same standard normal in the
exact-unit-diagonal structured models.

## 4. Relation to actual feature learning; remaining obligations

The paper's first-layer physical update uses W0^T delta, where delta is
endogenous and correlated with W0 and the earlier layers. The calculation
above isolates a concrete nonlinear reuse statistic that a forward-only
replacement misses. It does not identify the whole backward field. Even
matching every singular moment does not alone prove nonlinear adaptive reuse
universality. Multiple calls can expose structured singular-vector correlations.

Next decisive test: actual initialized two-hidden-layer tanh training with
the original self-consistent response-memory equations, varying width and
comparing empirical function/feature trajectories across mixer ensembles.
The correct reference is distributional/population behavior, not same-seed
matrix closeness. Strong alternatives include plain fast orthogonal mixing,
the Fastfood core, frozen-feature training and a directly trained low-rank
increment. Actual end-to-end speed and total state must be measured only
after numerical parity and useful feature learning are established.
