# Polynomial dimension dependence of the strict-root folding error

2026-10-04. Bounded downstream refinement of the frozen
INTRINSIC_STRICT_ROOT_ROUTE.md at SHA-256
c3c1e5d10c32458ca08dbbbe6251efdb0ee400e5301a50aff943d7064d6ad7d1.
That file is unchanged. This note inherits its newly derived passive-query
insertion identity and its arbitrarily small polynomial exceptional
probability. It reconstructs the moment-order, dimension, confidence, and
activation/depth constants downstream of that identity. The coordinator
suggested tracking these constants; no sibling reconstruction was read.
No experiment, Git mutation, or maintained-source edit was performed.

The frozen candidate's insertion extension still requires its separate
reconstruction. Subject to that proof being accepted, the constants here
show that intrinsic storage does not conceal an exponential ambient
input-dimension factor in its error coefficient.

## 1. Statement and inherited constants

Keep the canonical Gaussian model, physical training, bounded-strip
activation class, gamma, beta, and label restriction from the frozen route.
In particular beta>=10, L>=2,

\[
Y\le(\gamma/m)\beta^{-62L},\qquad
\lambda=\min(1,\gamma/m),\quad S=16Y/\lambda,
\quad \kappa=\lambda/4.
\tag{1}
\]

Zero labels are exactly stationary; assume Y>0 in the proof. Let
V=span{v_a}, r=dim(V), and let v-tilde be the folded unit query defined
in the frozen route. Then for every 0<xi<1 and sufficiently large n,

\[
\Pr\left\{\sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(t,v)-f_n(t,\widetilde v)|
 \le \beta^{40L}S\,[d+1+\log(1/\xi)]\,n^{-1/2}\right\}
 \ge1-\xi.
\tag{2}
\]

The exponent 40 is a loose certified envelope. The width threshold can
depend on the fixed dimension, confidence, labels, and activation
parameters. The coefficient in (2) cannot absorb any additional such
dependence.

Combining (2) with the existing restricted compression theorem and its
error beta^(124L)Y(m/gamma)^(3/2)/sqrt(n) gives the convenient envelope

\[
\sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_C(t,v)-f_n(t,v)|
 \le \beta^{130L}[d+1+\log(1/\xi)]
           Y(m/\gamma)^{3/2}n^{-1/2}
\tag{3}
\]

with probability at least 1-xi. Thus the added ambient-dimension cost
in error is linear, while the expensive retained-source coefficient and
logarithmic exponent use D=min(d,r+1). No dimension-dependent strengthening
of (1) is imposed.

Here are the exact structural inputs used for the envelope. The rescaled
carrier source defines B,s,t_phi, K_ell, A_H,D_H,H_2, eta, mathcal B,
and E by its finite recurrences. Their certified bounds are

\[
B,s,t_\phi\le\beta,\quad
K_{\max}:=\max_\ell K_\ell\le\beta^{2L},\quad
A_H,H_2\le\beta^{8L},\quad D_H\le\beta^{5L},
\]
\[
\eta^{-1}\le\beta^{22L},\quad
\mathcal B\le\beta^{3L},\quad E\le\beta^{7L}.
\tag{4}
\]

All are defined in LABEL_DEPTH_RESCALING_ROUTE.md, equations (3), (7),
(13), and (23). E here is the scalar external-Hessian trace coefficient,
not the passive coordinate matrix. To avoid that conflict below, call
the latter U_perp. The inherited source estimates cover external
preactivation Hessian blocks as well as the ordinary training Hessians.
The complete label restriction gives

\[
Y/\lambda\le\beta^{-60L},\qquad S\le\beta^{-59L},
\tag{5}
\]

since gamma<=B^2 and 16<=beta^L. These stronger margins will bound
existing expressions; they do not add a hypothesis.

## 2. A quantified singleton shift

The new asymmetric trace has one passive-query endpoint in normalized
Schatten-2. Its norm is at most H_2 by the same augmented Hessian
recurrence: query carrier RMS is at most K_ell S, query gates are bounded,
and the query has norm one. The training endpoint has the source bounds
in (4), with its higher normalized Schatten moments. Write

\[
a_1=D_H/\eta,\qquad q=4eS^2a_1.
\]

Real negative-Gram base propagators are contractions. The h=0 term in
the normalized endpoint trace is at most H_2^2. For h>=1, the exponent
choice 2,2(h+1),...,2(h+1) gives the term

\[
H_2\,{S^h\over h!}
 [A_H+2Sa_1(h+1)(2\mathcal B)^{1/[2(h+1)]}]^{h+1}.
\]

Splitting its power and using
(h+1)^(h+1)/h! <= e^(h+1)(h+1) gives the explicit sum

\[
\mathcal T=H_2^2+H_2\left[
 A_H(e^{2SA_H}-1)
 +2eSa_1\sqrt{2\mathcal B}\,
                  {q(2-q)\over(1-q)^2}\right].
\tag{6}
\]

The last series formula is sum_(h>=1)(h+1)q^h=q(2-q)/(1-q)^2.
The source condition already has q<1; (5) gives a much larger margin.
Specifically a_1<=beta^(27L), q<=4e beta^(-91L)<1/4, and

\[
SA_H\le\beta^{-51L},\qquad
2eSa_1\sqrt{2\mathcal B}\le
                       2e\sqrt2\,\beta^{-30.5L}.
\]

Consequently e^(2SA_H)-1<=1, and the last summand inside the brackets
in (6) is at most one. The explicit recurrences have H_2>=A_H>=1.
It follows that

\[
\mathcal T\le3H_2^2\le\beta^{17L}.
\tag{7}
\]

In the singleton identity, the trace is multiplied by a deleted training
activation bounded by B and integrated against residual activity at most
S. The direct external trace is at most ES and is multiplied by a
query activation bounded by B. The learned-column term is at most
B s^2 K_max^2 S^3: the learned column has norm at most
B s K_max S^2/sqrt(n), and its query response has norm at most
sK_max Ssqrt(n). The centered quadratic fluctuations, rank-one residual
trace, and nonlinear remainders tend to zero; for fixed S>0 their
aggregate is at most S after increasing the width threshold.

Thus a valid explicit coefficient in the singleton estimate is

\[
D_q=B(\mathcal T+E)+Bs^2K_{\max}^2+1,
\qquad
|k_i^{(j)}(t,v)-x_i^\top\delta^{(j+1),-i}(t,v)|\le D_q S.
\tag{8}
\]

Using S<=1 only enlarged the learned-column term in defining D_q.
Equations (4) and (7) give D_q<=beta^(20L): its leading contribution
is at most beta^(17L+1), and all remaining terms are at most
beta^(7L+1), beta^(4L+3), and one. Their sum is below beta^(20L)
for beta>=10,L>=2. This coefficient is independent of d, the query,
time, confidence, and the later moment order. Constants in the vanishing
terms may depend on those fixed quantities; their role is solely in
selecting the eventual width.

## 3. Carrier moments really grow as sqrt(p)

Let F be the training initialization sigma-field and let E_n in F be
the training-only successful event of the frozen route. In particular
Pr(E_n)->1. It contains no condition on the independent passive first
matrix G=A(0)U_perp. For every fixed p>=2 and all sufficiently large n,

\[
\sup_{t\in[0,\infty],\,v\in S^{d-1},\,\ell}
 \left(\mathbb E\left[\mathbf1_{E_n}
                      \|k^{(\ell)}(t,v)\|_{p,n}^{p}\right]\right)^{1/p}
 \le C_k S\sqrt p,\qquad C_k\le\beta^{25L}.
\tag{9}
\]

Here and below counting norms use 1/n. The supremum in (9) is outside
the expectation; no moment of a query supremum is assumed.

For clarity, the exceptional-event argument is part of the proof. The
frozen query insertion construction gives, for every fixed M, a common
query/local good event Omega_(n,M), with

\[
\Pr(E_n\cap\Omega_{n,M}^c)\le C_M n^{-M}.
\tag{10}
\]

This follows from its superpolynomial control-net failure and arbitrarily
small polynomial Gaussian-row and Gaussian-grid failure. Increasing M
changes a fixed temporary coordinate-cap multiplier and the width
threshold, but not the nonvanishing trace coefficient D_q. This
separation is essential; a bare o(1) failure probability would not suffice.

At deterministic t<=T_n and v, the cavity reference in (8), frozen at
its own stops and zeroed on its own failed initialization event, is
independent of x_i. Its RMS is at most sK_max S. Hence

\[
\|x_i^\top\delta^{(j+1),-i}(t,v)\|_{L^p}
                    \le2sK_{\max}S\sqrt p.
\tag{11}
\]

The elementary scalar Gaussian bound used here follows from
u^p <= (2p/e)^(p/2) exp(u^2/4) and E exp(g^2/4)=sqrt(2) for a
standard normal g. No independence between different neurons is needed.
On E_n intersect Omega_(n,M), use (8), then remove good-event indicators
only from its nonnegative Gaussian upper bound before conditioning on
one cavity. On the exceptional event the all-real deterministic bound
is |k_i|<=K_max Ssqrt(n). Thus its contribution to the joint
probability/counting L^p norm is at most

\[
K_{\max}S\sqrt n\,[C_M n^{-M}]^{1/p}.
\tag{12}
\]

Choose M=p+2, with p fixed before n tends to infinity. Expression (12)
is at most S eventually. Minkowski and (11), after averaging over i,
give coefficient 2sK_max+D_q+1 multiplying Ssqrt(p). The top carrier
uses ||w||_infty<=BS. The deterministic tail after T_n adds at most S
eventually, uniformly over all queries and times, by the frozen route's
CS n exp(-kappa T_n)=O(n^(-7)) estimate. Therefore one may take

\[
C_k=2sK_{\max}+D_q+B+3\le\beta^{25L}.
\tag{13}
\]

The additional slack in the exponent allows all displayed numerical
sums. Formula (12) also explains why constants C_M depending on p and d
do not become hidden p- or d-dependent error coefficients: they multiply
a negative power of n at a fixed chosen p. Uniformity in t and v follows
from the uniform exceptional event and the uniform cavity RMS bound.

## 4. The Gaussian operator norm has no dimension loss at large width

Let k=d-r and G be n-by-k standard Gaussian. For k=0 there is no folding.
For k>=1, take Euclidean 1/4-nets on S^(n-1) and S^(k-1), with
cardinalities at most 9^n and 9^k. For every matrix,

\[
\|G\|_{\rm op}\le2\max_{u,v\text{ in these nets}}|u^\top Gv|.
\]

Each displayed scalar is standard normal. A union bound therefore gives

\[
\Pr\{\|G\|_{\rm op}>5(\sqrt n+\sqrt k+\sqrt u)\}\le e^{-u},
\qquad u\ge0.
\tag{14}
\]

Indeed the exact threshold from the union is
2sqrt(2[(n+k)log(9)+u+log(2)]), bounded by the threshold in (14).
Integrating the tail, or using the same exponential-moment inequality as
in (11), proves for every q>=2

\[
\left\|{\|G\|_{\rm op}\over\sqrt n}\right\|_{L^q}
 \le5(1+\sqrt{k/n})+10\sqrt{q/n}.
\tag{15}
\]

Thus when n>=k+p, with Z=||G||_op/sqrt(n),
||1+Z||_(L^p)<=21. This uses the operator norm; the earlier Frobenius
estimate would unnecessarily insert a power of sqrt(d).

Combining (9) at order 2p with probability Hölder gives, for p>=2,

\[
\left\|\mathbf1_{E_n}(1+Z)^{1/2}
                    \|k^{(\ell)}(s,v')\|_{4,n}\right\|_{L^p}
 \le8C_kS\sqrt p.
\tag{16}
\]

Here counting-norm monotonicity and Jensen give
E[1_E||k||_(4,n)^(2p)] <= E[1_E||k||_(2p,n)^(2p)] because 2p>=4.
The factor from Z is below sqrt(21), and the carrier moment contributes
sqrt(2p). No independence of G and the query carrier is asserted.

## 5. Explicit increment coefficients

Use the deterministic proof clock tau(t)=1-exp(-kappa t). Put

\[
a=|\tau(t)-\tau(s)|,\qquad b=\|v-v'\|_2,\qquad h=a+b.
\]

For the physical tube use hidden operator cap 9 and the active first
operator cap 9 after its small displacement from initialized cap 8.
The residual activity between s and t is at most Sa/2. Therefore

\[
\|\Delta w\|_{2,n}\le BSa/2,\quad
\|\Delta W^{(\ell)}\|_{\rm op}\le BsK_{\max}S^2a/2,
\quad
\|\Delta A_V\|_{\rm op}/\sqrt n\le sK_{\max}S^2a/2.
\tag{17}
\]

Define finite forward coefficients

\[
F_1=9+sK_{\max}/2,\qquad
F_\ell=9sF_{\ell-1}+B^2sK_{\max}/2,\qquad F=\max_\ell F_\ell.
\tag{18}
\]

Forward subtraction of the actual network proves

\[
\|z^{(\ell)}(t,v)-z^{(\ell)}(s,v')\|_{2,n}
              \le F[(1+Z)b+S^2a].
\tag{19}
\]

At the first layer use the active/passive decomposition. At each later
layer the propagated change costs 9s times the preceding bound and the
changed-matrix term costs B^2sK_max S^2a/2. This is exactly (18).
The finite geometric sum, 9s<=beta^2, and (4) give F<=beta^(6L).
For example
F <= (9s)^(L-1)[9+sK_max/2+B^2sK_max/16], which already gives the
stronger beta^(5L) bound; we keep the extra slack.

Let

\[
C_g=\sqrt{2s t_\phi F}\le\beta^{4L},\qquad
P=\sum_{j=0}^{L-1}(9s)^j\le\beta^{2L},
\]
\[
A_b=(9s)^{L-1}sB/2+
          (Bs^3K_{\max}^2/2)\sum_{j=0}^{L-2}(9s)^j
                  \le\beta^{8L}.
\tag{20}
\]

The two changed-gate bounds |Delta phi'|<=2s and
|Delta phi'|<=t_phi|Delta z| imply

\[
\|\Delta\phi'\|_{4,n}\le
                       C_g[(1+Z)b+S^2a]^{1/2}.
\]

Subtract the backward recursion and pair this changed gate with the
reference carrier at (s,v'). The changed matrix costs
Bs^3K_max^2 S^3 a/2 after multiplication by the gate; propagation costs
9s. At the top the changed readout costs sBSa/2. Consequently (16) gives

\[
\|\mathbf1_{E_n}\Delta\delta^{(1)}\|_{L^p(\ell^2_n)}
 \le [A_b+8C_gPC_k\sqrt p]S\sqrt h
 \le\beta^{33L}\sqrt p\,S\sqrt h.
\tag{21}
\]

We used S<=1, a<=sqrt(h), and
[(1+Z)b+S^2a]^(1/2)<=sqrt(1+Z)sqrt(h). The numerical envelope follows
from (13),(20): 8C_gPC_k<=8beta^(31L)<=beta^(32L), and adding A_b
costs at most another beta^L. The norm on the left denotes the
probability L^p norm of the normalized Euclidean vector norm.

Write f_bar=E_G[f_n|F] and Z_n=sqrt(n)(f_n-f_bar). The exact gradient is

\[
\nabla_G f_n(t,v)=n^{-1}\delta^{(1)}(t,v)(U_\perp^\top v)^\top.
\]

Thus the normalized Gaussian gradient of an output increment is bounded
by the left side of (21) plus sK_max S b. Since b<=2 and b<=sqrt(2h),
its L^p norm is at most beta^(34L)sqrt(p)Ssqrt(h). Gaussian rotation
has coefficient at most pi sqrt(p), using (11)'s scalar Gaussian bound
and the quarter-circle length pi/2. Hence

\[
\|\mathbf1_{E_n}[Z_n(t,v)-Z_n(s,v')]\|_{L^p}
             \le\beta^{35L}pS\sqrt{a+b}.
\tag{22}
\]

The training event is F-measurable, so the rotation changes no indicator.
This is the exact place where sqrt(p) carrier moments and the sqrt(p)
Gaussian derivative inequality combine into p. All constants in (22)
are independent of d; n must be large enough for its fixed moment order
and n>=k+p.

## 6. Chaining without exponential net constants

Put q_0=d+1. The index space [0,1] times S^(d-1), in the metric
|tau-tau'|+||v-v'||, has 2^(-j)/2-nets with cardinality at most
9^(q_0)2^(jq_0): use spacing 2^(-j)/4 for each factor. Connect each
level-j point to a nearest point of the previous net; the metric distance
is at most 2^(-j). Choose a fixed real moment order

\[
p\ge4q_0.
\]

There are at most 9^(q_0)2^(jq_0) such edges. By (22) and the elementary
maximum L^p inequality, their maximum increment has norm at most

\[
\beta^{35L}pS\,9^{q_0/p}
                         2^{-j(1/2-q_0/p)}.
\]

Here 9^(q_0/p)<=9^(1/4)<2, and the geometric ratio is at most
2^(-1/4). The sum over j>=1 is less than 11 beta^(35L)pS. A coarse
net adds less than 2 beta^(35L)pS, by comparing its points to time zero,
where every Z_n vanishes. Continuity, including the fitted endpoint,
then gives

\[
\left\|\mathbf1_{E_n}\sup_{t,v}|Z_n(t,v)|\right\|_{L^p}
            \le16\beta^{35L}pS\le\beta^{36L}pS.
\tag{23}
\]

The exponential net cardinality has been raised to 1/p with p proportional
to dimension. It has therefore produced a numerical factor, not an
exponential dimension coefficient. The mean is conditional on F, and is
the same at v and v-tilde. Folding costs at most twice (23).

Take p=max{4(d+1),log(2/xi)}. Markov at e times this L^p bound gives
exceptional probability at most exp(-p)<=xi/2. Eventually
Pr(E_n^c)<=xi/2 as well. Since

\[
p\le5[d+1+\log(1/\xi)],
\]

and 2e<=beta^L, 5<=beta^L, (23) actually proves (2) with exponent 38.
The stated exponent 40 leaves two further powers of beta^L as slack.
No p is allowed to grow with n in this argument: d and xi are fixed first.

## 7. Composition with intrinsic compression

The folding map and its dr projection storage are those of the frozen
candidate. The restricted model has exactly the same training inner
products, gamma, labels, hidden trajectory, and physical time. Its
compression error is beta^(124L)Y(m/gamma)^(3/2)/sqrt(n), independently
of its input dimension D. Split the desired failure budget xi equally
between folding and restricted compression.

For every gamma/m>0 with gamma<=B^2,

\[
S=16Y/\lambda
       \le16B^3Y(m/\gamma)^{3/2}
       \le\beta^{3L}Y(m/\gamma)^{3/2}.
\tag{24}
\]

To check the first inequality, set a=gamma/m. If a<=1, its ratio after
cancelling 16Y is a^(1/2)<=1; if a>=1, the ratio is a^(3/2)<=B^3.
The last inequality uses B<=beta, beta>=10,L>=2. Also
[d+1+log(2/xi)] <= 2[d+1+log(1/xi)]. Equations (2),(24) thus bound
the added folding coefficient by beta^(44L)[d+1+log(1/xi)] times
Y(m/gamma)^(3/2). Adding the original beta^(124L) coefficient is below
beta^(125L)[d+1+log(1/xi)], hence certainly below the envelope (3).

When r+1>=d, the original construction already satisfies (3), without
folding. Otherwise D=r+1, and the current inherited storage bound is

\[
\beta^{84LD}(D+3)^D(m/\gamma)^2[\log(en)]^{3D+2}
       +10m(d+1)+Cdr+C(d+r).
\]

Any separately checked improvement of the D-dimensional compression
coefficient composes in the same way. This note does not read or assume
one. The only dependence on the original ambient d introduced into the
error coefficient is the displayed linear factor; explicit preprocessing
storage remains polynomial. It does not claim a growing-dimension,
growing-confidence, or simultaneous-all-width probability theorem.
