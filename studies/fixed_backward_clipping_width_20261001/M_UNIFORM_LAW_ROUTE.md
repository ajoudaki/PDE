# Growing smooth caps: population law stability

2026-10-01. Scoped mathematical route. Inputs read completely: SMOOTH_SETUP.md,
SMOOTH_RESULT.md, and SMOOTH_MEAN_MAP_ROUTE.md. Required research, proof, and
canonical-notation instructions also apply. No other study, manuscript, Git
history, experiment, or external scientific source is an input.

**Conclusion.** The prescribed-history response law has an activity threshold
independent of \(M\ge1\). Its covariance/response map is contractive on one
common small-activity domain. The lower derivative bounds required for this
statement are Gaussian moment bounds, rather than global pathwise bounds.
They yield deterministic **conditional expected entrywise tensors**, which
are sufficient for the random covariance and response-input comparisons.

There is also a separate, useful comparison on any bounded coarse domain:
the lower map is time-integrated in an unnormalized running norm and the
upper map is Lipschitz in that norm. Thus an approximate fixed point can be
compared by Volterra Gronwall even when its domain constants depend on \(M\).
This avoids a claim that empirical cavity responses already satisfy the
common small-domain bounds. The statistical cavity defect and admissibility
of its conditional Gaussian inputs remain separate hypotheses here.

## 1. Exact system and quantified claims

Use the activity coordinate \(x\in[0,S]\) and the complete prescribed-history
system (3) of SMOOTH_MEAN_MAP_ROUTE. In particular, with
\(\psi(a)=\operatorname{sech}^2a\),

\[
F_M(\alpha,p)=M\tanh(p\psi(\alpha)/M),
\]

\[
\begin{aligned}
h_a&=\tanh(a\cdot u_a),\\
p_a&=\xi_a+D_a h_a+
 \sum_b\int_0^x Q_{d,ab}(x,v)h_b(v)\,dv
 +m^{-1}\sum_b k_bV_{ba},\\
a'&=-\frac2m\sum_b\lambda_b F_M(a\cdot u_b,p_b)u_b,
 &k_a'&=(h_a-k_a)/(1+x),\\
z_a&=\gamma_a+\sum_b\int_0^xQ_{h,ab}(x,v)d_b(v)\,dv
 +m^{-1}\sum_bv_bK_{ba},\\
d_a&=F_M(z_a,w),
 &w'&=-\frac2m\sum_b\lambda_b\tanh z_b,
 &v_a'&=-2\lambda_a d_a.
\end{aligned}                                                    \tag{1}
\]

Here \(a(0)=a_0\sim N(0,I_d)\), \(k_a(0)=\tanh(a_0\cdot u_a)\), and

\(w(0)=v(0)=0\). The lower Gaussian history \(\xi\) is independent of

\(a_0\); its covariance is \(C_d\). The upper Gaussian history

\(\gamma\) has covariance \(C_h\). The two representatives are on separate
probability spaces. All law inputs and supplied histories are fixed when
taking a representative derivative. The supplied functions satisfy

\[
|\lambda_a|\le\sqrt m,\quad |K_{ba}|\le1,\quad
|V_{ba}(x)|\le Lx^3,
\]

and \(K,V\) are activity-Lipschitz with fixed constant \(L\). The lower and
upper output laws are denoted by \(\mathcal L_M(D)\) and
\(\mathcal U_M(H)\), where

\[
H=(C_h,Q_h),\qquad D=(C_d,D_{\rm atom},Q_d).
\]

The notation \(D_{\rm atom}\) denotes the vector written \(D_a\) in (1).
Its output is the expectation of the current derivative

\[
\partial_{\gamma_a(x)}d_a(x)
 =c'_M(w\psi(z_a))w\psi'(z_a).
\]

It is retained separately from the regular response density \(Q_d\).
The lower response \(Q_h\) has no atom.

The first claim is that the entire domain of Section 1 of
SMOOTH_MEAN_MAP_ROUTE can be chosen with constants

\[
L_h,B_h,L_d,B_d,S_*>0
\]

independent of \(M\ge1\), so that (1) preserves the domain for

\(0<S\le S_*\). Its deterministic comparisons (21), (26) and the
conditional averaged entrywise versions of (41), (45), (46) hold
with constants independent of \(M\). “Entire domain” includes positive
semidefinite covariance kernels, their mean-square Lipschitz increments,
bounded causal response densities, Lipschitz current-time response rows in

\(L^1\), and the separate Lipschitz atom. It does not require an empirical
initial lower covariance to equal the population covariance.

The second claim concerns two inputs in any one bounded coarse domain.
Its constants can depend on that domain and on \(M\). It does not require
the map to preserve that coarse domain.

## 2. Scalar derivatives uniform in \(M\)

For each fixed derivative order \(q\), there are constants \(c_q\),
independent of \(M\ge1\), such that

\[
|\partial_\alpha^rF_M(\alpha,p)|\le c_q|p|,
\qquad 0\le r\le q,                                      \tag{2}
\]

\[
|\partial_\alpha^r\partial_p^jF_M(\alpha,p)|\le c_q,
\qquad j\ge1,\quad r+j\le q.                             \tag{3}
\]

For (2), set \(u=p\psi(\alpha)/M\). Derivatives of \(\psi\) are

\(\psi\) times bounded polynomials in \(\tanh\alpha\). Every term with

\(r\ge1\) is therefore a bounded coefficient times

\(M u^k\tanh^{(k)}u\), \(k\ge1\). The quotient

\(u^{k-1}\tanh^{(k)}u\) is bounded, giving \(c|p|\). The case \(r=0\)
uses \(|\tanh u|\le|u|\). For (3), differentiating \(j\) times in \(p\)
first gives

\[
M^{1-j}\psi(\alpha)^j\tanh^{(j)}u.
\]

Further \(\alpha\) derivatives produce bounded gate factors and powers
of \(u\) multiplying positive-order derivatives of tanh. These products
are bounded, and \(M^{1-j}\le1\).

The deterministic upper bounds are

\[
|h_a|,|k_a|\le1,\quad |w(x)|,|d_a(x)|\le c x,
\quad |v_a(x)|\le c x^2.                                 \tag{4}
\]

Thus all upper mixed derivatives containing a \(w\) derivative are
bounded independently of \(M\); pure \(z\) derivatives are bounded by

\(c_q S\). All upper tensor proofs from the existing mean-map route
therefore already have constants uniform in \(M\ge1\).

The lower pure-state coefficients in (2) have no globally uniform bound.
This is a real failure of the original *pathwise global* majorant argument,
not a counterexample to the population comparison.

## 3. One Gaussian envelope, uniform over meshes and admissible laws

In the common domain the lower Gaussian satisfies

\[
\xi(0)=0,\quad
\|\xi_a(x)-\xi_a(y)\|_{L^2}\le L_d|x-y|.
\]

There exist constants \(c,C\), depending on the fixed sample count, and a
nonnegative reference random variable \(Z_*\), with

\[
\Pr(Z_*>r)\le C e^{-cr^2}\quad(r\ge1),                    \tag{5}
\]

such that the random variable

\[
\frac{\max_a\sup_{0\le x\le S}|\xi_a(x)|}{L_dS}
\]

is stochastically dominated by \(Z_*\). The same statement holds for every
sampled finite mesh, every convex covariance interpolation, and
conditionally on an environment whenever the conditional covariance obeys
these same deterministic domain bounds.

Here is a direct construction of the bound. At dyadic level \(j\), there
are at most \(m2^j\) new increments with standard deviation at most

\(L_dS2^{-j}\). Gaussian tails and a union bound show that the probability
that one exceeds

\[
A L_dS2^{-j}(\sqrt{j+1}+r)
\]

is at most \(C e^{-cr^2}2^{-j}\) when \(A\) is sufficiently large.
Sum over \(j\) and telescope the dyadic paths. Since

\(\sum_j2^{-j}(\sqrt{j+1}+r)\le C(1+r)\), this proves (5), first on
the dyadic set and then on the continuous Gaussian version. Enlarging

\(Z_*\) below a fixed threshold makes it a literal stochastic dominator.
The proof only uses the stated variance inequalities, so it is conditional
and uniform in the covariance law. In particular

\[
\mathbb E[(1+Z_*)^k e^{aZ_*}]<\infty
\]

for every fixed \(k,a<\infty\).

By (1), (4), and the domain bounds,

\[
\max_{a,x}|p_a(x)|
\le S\{L_d Z_*+c B_d+cLS^2\}                             \tag{6}
\]

in the sense of domination of all increasing bounds derived from the
actual Gaussian supremum. Thus the lower drift derivatives through any
fixed order are bounded by a common scalar

\[
\Lambda(z)=C\{1+S(L_dz+B_d+1)\}.                          \tag{7}
\]

The initial Gaussian \(a_0\) needs no envelope: (2), (3), and every tanh
derivative bound are uniform in \(a_0\).

## 4. Conditional expected entrywise tensors

Fix a mesh and repeat the positive tensor construction (35)--(38) of
SMOOTH_MEAN_MAP_ROUTE. Replace each lower nonlinear derivative bound by

\(\Lambda(z)\), retaining the deterministic response coefficients, mesh
weights, causal supports, Kronecker source tensors, and separate upper
pure-\(z\) factors \(S\). Denote the resulting tensor by

\(b_X[I;z]\), where \(I\) is an ordered tuple of history derivative
slots. It is nonnegative and increasing in \(z\). For each realized
lower Gaussian history it dominates the derivative tensor when \(z\)
is its normalized supremum.

For \(q=1,2,3\), the positive recurrences give

\[
\sum_{|I|=q} b_{h_i}[I;z]
 +\sum_{|I|=q} b_{k_i}[I;z]
 +\sum_{|I|=q} b_{a_i}[I;z]
 \le S P_q(\Lambda(z))e^{C_q S\Lambda(z)}.                \tag{8}
\]

Here \(P_q\) is a fixed polynomial with nonnegative coefficients;
neither it nor \(C_q\) depends on \(M\), the mesh, or \(S\le S_*\).
For clarity, this estimate does not require absorption of

\(S\Lambda(z)\) for every realization. At first order the source sum
is bounded and the propagated state sum satisfies

\(J_{1,i+1}\le(1+C\Lambda\Delta_i)J_{1,i}
+C\Lambda\Delta_i\). Iteration gives the first-order case of (8).
At orders two and three the highest-order unknown enters linearly with
the same coefficient; the remaining terms are the partition products of
already bounded lower orders. Variation of constants gives (8), with a
larger fixed polynomial and exponential constant. A finite-dimensional
state consisting also of cumulative positive memory bounds handles the
Volterra terms; their coefficients are bounded by the fixed domain
constants. This proves (8) without a mesh-dependent coefficient. In choosing the
domain constants below, dependence on the lower response input occurs
through its row mass and atom bound, both at most \(CSB_d\). Bounding
past state tensors by their running maximum therefore makes the recurrence
constants numerical when \(SB_d\le1\); a separate bare \(B_d\) is not
needed in the Gronwall coefficient.

With one past source \((j,b)\) fixed, its first entry is through a drift
step or an integrated response weight with factor \(\Delta_j\). Causal
propagation and the same induction therefore give

\[
\sum_{|I|=q-1}b_{h_i}[(j,b),I;z]
 \le\Delta_jP_q(\Lambda(z))e^{C_qS\Lambda(z)}
 \quad(j<i).                                             \tag{9}
\]

Repeated occurrences of a source at its first entry have one

\(\Delta_j\), not one factor per occurrence. The partition construction
retains this diagonal contact. The upper bounds are deterministic as
before: total masses \(cS\) for \(w,d\), \(cS^2\) for \(v\), fixed past
source masses \(c\Delta_j\), and current upper source masses \(cS\).

Define the deterministic tensors

\[
\bar b_X[I]=\mathbb E_{Z_*} b_X[I;Z_*].                   \tag{10}
\]

Tonelli, (5), (7), and (8) imply

\[
\sum_{|I|=q}\bar b_{h_i}[I]\le C_qS,\qquad
\sum_{|I|=q-1}\bar b_{h_i}[(j,b),I]\le C_q\Delta_j.        \tag{11}
\]

The constants are uniform for \(M\ge1\), \(S\le S_*\). Products such as

\(h_i h_j\) have deterministic expected Hessian masses \(CS\), and

\(d_i d_j\) have masses \(CS^2\). A response observable uses the third
tensor with one distinguished response slot, just as in the fixed-cap
proof.

Crucially, (10) gives

\[
\mathbb E[|\partial_I X|\mid\mathcal E]\le\bar b_X[I]     \tag{12}
\]

uniformly over every admissible environment and covariance interpolation.
It does **not** claim a deterministic pathwise bound for all Gaussian
histories.

To interpolate singular covariances without destroying the increment
bound, let \(X_0,X_1\) be independent centered Gaussians with covariances

\(\Gamma_0,\Gamma_1\), and put

\(X_\theta=\sqrt{1-\theta}X_0+\sqrt\theta X_1\). Gaussian integration
by parts in their underlying standard Gaussian coordinates gives

\[
\frac d{d\theta}\mathbb Ef(X_\theta)
 =\frac12\sum_{ij}(\Gamma_1-\Gamma_0)_{ij}
      \mathbb E\partial_{ij}f(X_\theta),\quad0<\theta<1.    \tag{13}
\]

This identity needs no inverse covariance. Truncation of the underlying
Gaussians, followed by the integrable bounds above, justifies integration
by parts and differentiation. Integration over \(\theta\), with dominated
convergence at the endpoints, is valid. Adding independent \(\varepsilon I\)
noise to every mesh coordinate is unnecessary; such noise would not
preserve a mesh-uniform increment bound.

If the covariance errors are environment measurable, (12)--(13) give

\[
\left|\mathbb E[f(X_1)-f(X_0)\mid\mathcal E]\right|
 \le\frac12\sum_{ij}\bar b_f[ij]|\delta\Gamma_{ij}|.      \tag{14}
\]

Taking an \(L^p(\mathcal E)\) norm entrywise and using Minkowski proves
the fixed-cap comparison with

\(\sup_{ij}\|\delta\Gamma_{ij}\|_{L^p}\). No expected random supremum
has been introduced.

For response-input errors, append one parameter derivative slot and retain
each insertion location, as in (42)--(43) of the existing route. The
resulting coefficient of each absolute input error is a nonnegative tensor
increasing in \(z\). Replace it by its expectation against \(Z_*\).
Conditional on the environment the input error is fixed, so it factors
out before this averaging. The tensor sums yield

\[
\sup_i\left(\|\delta h_i\|_{L^p}
 +\sum_j\|\delta\partial_{\xi_j}h_i\|_{L^p}\right)
 \le CS e_p,
\]

\[
\sup_i\left(\|\delta d_i\|_{L^p}
 +\sum_j\|\delta\partial_{\gamma_j}d_i\|_{L^p}\right)
 \le CS^2\eta_p,                                         \tag{15}
\]

when the displayed differences are Gaussian-conditionally averaged outputs.
Here \(e_p,\eta_p\) are exactly the entrywise-error row norms (44), or
their continuum forms (46), in SMOOTH_MEAN_MAP_ROUTE. The statement is
deliberately about conditional averages; an unaveraged random envelope
times an environment error would instead require conditional bounds or
Hölder with stronger moments. The present interpolation has the required
conditional bounds.

## 5. Common invariant domain and contraction

The lower drift satisfies

\[
\|a'(x)\|_{L^q}+\|h'(x)\|_{L^q}
 \le C_q x(L_d+B_d+1)                                    \tag{16}
\]

for each fixed \(q\), by the pointwise variance bound

\(\|\xi_a(x)\|_{L^q}\le C_qL_dx\). Its source response starts with

\(-2m^{-1}\lambda_b F_{M,p}u_b\), which is bounded uniformly by (3).
The propagated response and its current-time derivative are bounded by
polynomials times \(\exp(CS\Lambda(Z_*))\). Their expectations are
uniformly bounded by (5). Differentiating \(h\) introduces only bounded
tanh derivatives and the moment bounds in (16). This proves the lower
covariance increment bound, response density bound, and \(L^1\)-row
Lipschitz bound with constants independent of \(M\).

To choose the domain constants without circularity, require first

\(SL_d,SB_d\le1\). Under these restrictions (5)--(16) give numerical
lower constants independent of the eventual \(L_d,B_d\). Choose

\(L_h,B_h\) larger than those constants. The upper equations and their
source equations (23) in SMOOTH_MEAN_MAP_ROUTE then give finite

\(L_d,B_d\) depending only on these chosen lower constants and the fixed
data. All upper derivative coefficients are uniform in \(M\) by (3)--(4).
Finally decrease \(S_*\) to enforce the initial restrictions and all
upper absorption bounds. This yields a common complete convex domain.

The continuum passage uses the same cell-average approximation as the
fixed-cap route. The pathwise local Lipschitz coefficient is now

\(\Lambda(Z_*)\), rather than a deterministic constant. The error is
bounded by its convergent input/quadrature error times a polynomial in

\(Z_*\) and \(\exp(CS\Lambda(Z_*))\). Uniform integrability from (5)
therefore gives the covariance and response limits. For response rows one
uses the explicit source equations, retaining their source-cell factor;
state convergence alone is not being used to infer derivative convergence.
All conditional entrywise comparisons pass by Tonelli and the same bounds.

Let \(d_H,d_D\) be the normalized distances (5) in the existing route.
Equations (11)--(15) give

\[
d_H(\mathcal L_M D,\mathcal L_M\widetilde D)
 \le C_LS\,d_D(D,\widetilde D),
\qquad
d_D(\mathcal U_M H,\mathcal U_M\widetilde H)
 \le C_Ud_H(H,\widetilde H),                              \tag{17}
\]

with \(C_L,C_U\) independent of \(M\ge1\). Decrease \(S_*\) once more
so that \(C_LC_US_*<1\). The square of the full map contracts the complete
domain, and its unique fixed point is also the unique fixed point of the
unsquared map. This proves the first claim.

The same proof permits \(M=\infty\), interpreted as

\(F_\infty(\alpha,p)=p\psi(\alpha)\). This is a statement about the
prescribed population law only, not an identification or width estimate for
the unclipped finite network.

Passive lower velocity observables also remain admissible. They obey a
bound \(C|p|\), and their finite-order tensors have polynomial Gaussian
envelopes with deterministic expected masses \(C\), rather than \(CS\).
Products such as \(qq\) have the corresponding polynomial envelopes. The
passive upper Gaussian has variance bounded by these lower second moments;
its linear-factor observable is treated exactly as in Section 8 of the
existing route. Thus the population velocity comparison has uniform
constants whenever its input comparison lies in the common domain.

## 6. Causal comparison on a coarse domain

This part does not use the common-domain contraction. Fix \(S\le1\),

\(M\ge1\), and \(B\ge1\). Consider two admissible covariance/response
inputs whose deterministic response densities, atoms, and necessary
regularity bounds are at most \(B\). Their covariance kernels need only
have the bounded variances and increments needed to define the Gaussian
histories. The map need not carry this coarse domain into itself. Every
convex interpolation stays in the same coarse input domain.

For differences of two inputs, define the unnormalized running errors

\[
\begin{aligned}
E_H(t)&=\sup_{x,y\le t}\max_{a,b}|\delta C_{h,ab}(x,y)|
 +\sup_{x\le t}\max_a\sum_b\int_0^x
               |\delta Q_{h,ab}(x,u)|\,du,\\
E_D(t)&=\sup_{x,y\le t}\max_{a,b}|\delta C_{d,ab}(x,y)|
 +\sup_{x\le t}\max_a|\delta D_a(x)|
 +\sup_{x\le t}\max_a\sum_b\int_0^x
               |\delta Q_{d,ab}(x,u)|\,du.
\end{aligned}                                             \tag{18}
\]

Then there is a finite \(A=A(M,B)\), independent of the mesh, such that

\[
E_H(\mathcal L_M D,\mathcal L_M\widetilde D;t)
 \le A\int_0^t E_D(s)\,ds,                               \tag{19}
\]

\[
E_D(\mathcal U_M H,\mathcal U_M\widetilde H;t)
 \le A E_H(t).                                            \tag{20}
\]

These inequalities also hold with each absolute input error replaced by
its entrywise \(L^p\) norm before the deterministic time and source
suprema/integrals. Fixed-\(M\) deterministic pathwise tensors suffice for
this extension.

Here is the time factor in (19), including response contact terms. On a
mesh, the lower read-in state is

\[
a_i=a_0+\sum_{r<i}\Delta_r b_r,
\qquad b_r=-\frac2m\sum_b\lambda_b(x_r)
                      F_M(a_r\cdot u_b,p_{rb})u_b.        \tag{21}
\]

A fixed history source \((r,b)\) first enters this state through the drift
update at node \(r\), with factor \(\Delta_r\). Subsequent propagation is
causal. The positive tensor recurrence, with this source slot fixed and
all other slots summed, gives for \(q=1,2,3\)

\[
 \sum_{|I|=q-1}b_{h_i}[(r,b),I]\le A\Delta_r
 \quad(r<i).
\]

To verify the bound, the first fixed-source forcing is at most a bounded
drift derivative times \(\Delta_r\). At each higher order, terms containing
the fixed source have either a previously propagated fixed-source tensor,
or a product containing exactly one such tensor after its distinguished
slot is located. All other factors have bounded total derivative sums.
Their causal linear inequality preserves the factor \(\Delta_r\), with
a finite Gronwall multiplier. Repeated appearances of the same numerical
source in other slots do not add extra powers of \(\Delta_r\).

The product \(h_kh_l\) has the same fixed-slot bound by the product rule.
In covariance interpolation, group the two covariance slots by their
larger time index \(r\). Choose one slot having index \(r\), counting a tie
at most twice. Fix it, and sum the other covariance slot, sample indices,
and any distinguished response slot. The preceding estimate gives

\[
\sum_{i,j}b_{h_kh_l}[i,j]|\delta\Gamma_{ij}|
 \le A\sum_{r<\max(k,l)}\Delta_r
      \sup_{i,j\le r}|\delta\Gamma_{ij}|.                 \tag{22}
\]

For the integrated lower response, use its third derivative tensor and
sum the distinguished response slot. It may occur later than \(r\);
the fixed-slot estimate already sums every remaining slot, so this
causes no restriction. Both covariance slots still have times at most
\(r\), which is the only property needed to bound their covariance error.
This proves (22) for covariance and integrated-response outputs alike.
It retains the diagonal covariance and repeated-source contact terms.

In continuum terms \(Q_h(t,u)\) has a direct term involving

\(F_{M,p}\) at its source \(u\), which has no extra propagation integral.
Its contribution to (18) is nevertheless integrated over \(u\). This is
the source time integral in (22); there is no claim of (19) for the
pointwise density norm \(\sup_{t,u}|\delta Q_h(t,u)|\).

For response-input perturbations, differentiate (21) in the interpolation
parameter. Every direct insertion at drift time \(r\) is bounded by

\[
|\delta D(x_r)|+
 \sum_b\int_0^{x_r}|\delta Q_{d,ab}(x_r,u)|\,du,
\]

and carries \(\Delta_r\). Its first history derivative has the same
insertion bound times fixed-\(M,B\) derivative sums. Propagated
parameter derivatives solve a linear causal inequality with bounded
coefficients. Iterating that inequality bounds the output by

\(A\sum_r\Delta_r E_D(x_r)\). This proves the parameter part of (19),
including the integrated output response. Interpolating covariance and
response inputs separately proves (19) on meshes. For monotone running
errors its continuum bound follows from the same integral tensor
construction, or from refining meshes and using upper Riemann sums.

For the upper map, current Gaussian coordinates do enter \(d(t)\), so no
time factor is claimed. Its Hessian, third derivative, and response
insertion tensors have finite total masses depending on \(B\). All their
source indices and parameter insertion times are \(\le t\), yielding
(20). The current atom is included in this bound. These observations
prove both causal inequalities without an exchange of a random supremum
and expectation.

For an explicit generous constant, write

\(H_0=1+M+B\). For every fixed derivative order at most four, one may
take

\[
A(M,B)\le \exp(C H_0^{12}).                              \tag{23}
\]

Indeed all fixed-order derivatives of \(F_M\) are bounded by \(CM\),
and differentiation of the finite-dimensional state drift and linear
memory fields introduces at most a fixed power of \(1+B\). The
positive first-variation inequalities therefore have coefficient at most

\(CH_0^4\). Their mesh product is bounded by \(e^{CH_0^4S}\). At each
of the next three orders the highest derivative still enters linearly
with that same coefficient; its forcing is a finite polynomial in the
previous derivative bounds and coefficients bounded by a fixed power of

\(H_0\). This gives a polynomial prefactor times

\(e^{C_qH_0^4S}\), which is bounded by (23) after enlarging \(C\).
Fixed-source grouping, products, and a parameter insertion require only finitely
many such bounds. The exponent 12 is a loose common bound, not an
optimized growth claim. Neither covariance eigenvalues nor the number
of history coordinates occur in it.

## 7. Approximate fixed points and the meaning for growing caps

Suppose a deterministic tuple \((H_n,D_n)\) and an exact population tuple

\((H_*,D_*)\) both lie in a coarse domain with bound \(B_M\), and

\[
E_H(H_n,\mathcal L_M D_n;t)\le\varepsilon_M,
\qquad
E_D(D_n,\mathcal U_M H_n;t)\le\varepsilon_M               \tag{24}
\]

for every \(t\le S\). Allow different defects by taking their maximum.
The tuples need not lie in the common contraction domain. Put

\(e_H(t)=E_H(H_n,H_*;t)\) and similarly \(e_D\). Equations (19)--(20)
give

\[
e_H(t)\le\varepsilon_M+A\int_0^t e_D(s)\,ds,
\qquad e_D(t)\le\varepsilon_M+A e_H(t).
\]

Iterating the scalar integral inequality (its \(k\)th iterate has

\(t^k/k!\)) yields

\[
e_H(S)\le(1+AS)\varepsilon_M e^{A^2S},\qquad
e_D(S)\le\{1+A(1+AS)e^{A^2S}\}\varepsilon_M.             \tag{25}
\]

There is no requirement \(AS<1\). Thus any fixed common activity regime
can be used; the cost of a coarse response domain appears in the error
constant, rather than forcing the labels to shrink with \(M\).

In particular, if other parts of the proof supply

\[
B_M\le\exp(C(1+M)^p),\qquad
\varepsilon_M\le\exp(C(1+M)^p)/\sqrt n                   \tag{26}
\]

for some fixed finite \(p\), then (23)--(25) give a bound of the form

\[
e_H(S)+e_D(S)
 \le\frac{\exp\{\exp[\exp(C'(1+M)^{p'})]\}}{\sqrt n}    \tag{27}
\]

for some fixed finite \(p'\). When \(B_M\le\operatorname{poly}(M)e^{CM}\)
and the defect has the same single-exponential form, one can take
\(p'=1\): the twelfth power in (23) is absorbed by changing the constant
inside the first exponential of the triple tower. Formula (26) is a hypothesis imported from
the finite-width/cavity route, not proved by this law-map note. The same
caveat applies to any subsequent all-time feedback constant. A choice

\[
M(n)=\{\log\log\log(n+e^{e^e})\}^{1/(2p')}
\]

tends to infinity and makes the numerator in (27) equal to

\(n^{o(1)}\). The resulting rate is \(n^{-1/2+o(1)}\), not a uniform

\(C n^{-1/2}\) theorem. An additional cap-independent statistical and
feedback argument would be needed for the latter claim.

## 8. Boundaries and audit

The common population threshold and conditional expected entrywise
majorants are established here. They do not establish that a finite-width
conditional covariance/response tuple lies in the common domain. In
particular, operator propagator bounds may still give only

\(M\)-dependent density and row-Lipschitz constants. Replacing those by
uniform constants without proof would invalidate an application of (17).

The coarse causal argument addresses precisely this issue at the law-map
comparison stage: use the actual finite coarse bounds in (19)--(25),
without claiming an invariant coarse domain or a uniform finite-width
response estimate. It still requires that both compared tuples exist and
that the conditional Gaussian cavity interpolation and defects in (24)
are valid in that domain. It supplies no cavity independence statement.

The retained contact terms are the upper current response atom and the
single-time lower drift contacts in repeated tensor indices. The retained
norm is the source-integrated response-row norm, which is essential for
(19). The covariance interpolation is valid at singular covariance and
never uses an inverse. Conditional error factors are taken outside the
Gaussian average before the derivative envelope is averaged. No bound on

\(\mathbb E\sup|\delta C|\) is substituted for a bound on

\(\sup\mathbb E|\delta C|\).

The laws are still the original same-matrix transpose response laws. The
coefficient histories are prescribed only for the intermediate law
comparison; autonomy and all-time restoration are separate parts of the
overall proof. No all-initialization all-time second-moment tail claim is
made here.
