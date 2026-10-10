# Geometric local convergence of the original frozen-top NTH

Status: internally checked theorem, 2026-10-10; complete scoped
reconstruction in [MATCHING_CHECK.md](MATCHING_CHECK.md).
No experiment, shared-book change, or promotion is claimed.

The scientific input scope was the complete `WORST_CASE_RESULT.md`, SHA-256
`d4044343dcd031df298dba5af42d512e5e72b925edcb79edf0392828b4020f09`.
Required process and mathematical-presentation skills were also read.
No other research report or study was read. The supervisor separately
suggested tracking the norm of the label-weighted input mean; that refinement
is derived here. An unsolicited supervisor summary of a possible
dense-pair lower bound was received but is neither used nor checked here.

## Statement and exact scope

Consider any finite unit-input dataset
\(v_1,\ldots,v_m\in\mathbb R^d\), with \(\|v_a\|_2\le1\),
and labels \(|y_a|\le1\). There are two hidden identity layers of width
\(n\). With the same normalization and metric as the source, put

\[
B=W^{(1)}/\sqrt n\in\mathbb R^{n\times d},\qquad
W=W^{(2)}\in\mathbb R^{n\times n},\qquad
c=u/\sqrt n\in\mathbb R^n.
\]

The prediction and loss are

\[
f_n(t,v)=c(t)^\top W(t)B(t)v,
\qquad
\mathcal L=\frac1{2m}\sum_{a=1}^m(f_n(t,v_a)-y_a)^2.
\tag{1}
\]

Training is Euclidean/Frobenius gradient flow in \((B,W,c)\), equivalently
mobilities \((n,1,n)\) in \((W^{(1)},W^{(2)},u)\). The readout starts at
\(c_0=0\). Initially \(\|B_0\|_{\rm op},\|W_0\|_{\rm op}\le4\).
No Gram gap, label balance, or label lower bound is required.

For arbitrary input vectors, define the source vector field and the
ordered hierarchy tensors below, writing \(\theta=(B,W,c)\) for the
parameter state:

\[
\begin{aligned}
V(v;B,W,c)&=\nabla_{(B,W,c)}f_n(v)
 =(W^\top c v^\top,\ c(Bv)^\top,\ WBv),\\
K_1(v;B,W,c)&=f_n(v),\\
K_{r+1}(v_0,\ldots,v_r;B,W,c)
 &=D_{(B,W,c)}K_r(v_0,\ldots,v_{r-1};B,W,c)
       [V(v_r;B,W,c)].
\end{aligned}
\tag{2}
\]

There is no permutation-symmetry assumption. Each input slot is linear.
The notation \(K_r(\cdot;0)\) means evaluation at the initial parameter
state \(\theta_0\), not at all-zero hidden weights.
The original order-\(q\) closure copies \(K_r(0)\), freezes rank \(q\),
and evolves, for \(r<q\),

\[
\dot K_r^{(q)}(v_0,v_{a_1},\ldots,v_{a_{r-1}};t)
 =\frac1m\sum_{a=1}^m
 (y_a-f_{n,q}(t,v_a))
 K_{r+1}^{(q)}(v_0,v_{a_1},\ldots,v_{a_{r-1}},v_a;t),
\quad f_{n,q}(t,v)=K_1^{(q)}(v;t).
\tag{3}
\]

The first slot may be a training input or a passive test input; passive
inputs do not enter the sum or acquire labels.

Define the fixed data summaries

\[
Q=\frac1m\sum_a v_av_a^\top,\qquad
b=\frac1m\sum_a y_av_a,\qquad
\|b\|_2\le1.
\tag{4}
\]

On the same physical interval as the source,
\(T=1/32768\), the dense flow and every finite closure \(q\ge2\)
exist uniquely. Simultaneously for all such orders, putting
\(j=2\lfloor q/2\rfloor+1\),

\[
\begin{aligned}
\sup_{0\le t\le T}\sup_{\|v\|_2=1}
 |f_n(t,v)-f_{n,q}(t,v)|
 &\le64(j+1)(j+2)\left(\frac{\|b\|_2}{4096}\right)^j\\
 &\le64\|b\|_2\,1024^{-q}.
\end{aligned}
\tag{5}
\]

When \(b=0\), both predictors vanish identically and the bound is
exact. All constants are independent of \(m,d,n,q\) and the dataset.
The initial tensors use only the initial network and the data. No dense
trajectory, future prediction, physical-time Taylor replacement, restart,
or different top-rank rule is used.

If the independent entries of \(B_0,W_0\) have law \(N(0,1/n)\), then
for every \(1\le d\le n\) the event used above has probability at least

\[
1-2e^{-c_*n},\qquad c_*=4-\tfrac32\log9>0.
\tag{6}
\]

On that one event, (5) holds for every admissible dataset and order.
For \(d>n\), (5) remains a deterministic conditional statement; no
dimension-uniform probability is claimed for the same norm cutoff.

For \(0<\varepsilon\le1\), the deterministic choice

\[
q_\varepsilon=
\max\left\{2,\left\lceil\frac{\log(64/\varepsilon)}{\log1024}
\right\rceil\right\}
\tag{7}
\]

gives error at most \(\|b\|_2\varepsilon\), and hence at most
\(\varepsilon\). In particular, absolute error \(n^{-p}\) for any fixed
\(p>0\) requires only \(q=O_p(\log n)\).

## Proof

The proof first controls each ordered source coefficient, then identifies
both physical trajectories with their own-residual ordered-integral
equations. Uniform contraction transports the explicitly bounded omitted
tail to the prediction error. Contracting source indices against the data
is an exact multilinear identity; it does not change the retained NTH.

### 1. Dimension-free coefficient bounds and parity

Suppose the three parameter-block norms are at most \(s\). Start from the
three variable leaves of \(c^\top WBv_0\). Applying one source derivative
replaces exactly one occurrence of a parameter block by the corresponding
quadratic expression in (2). Each term gains one variable leaf. After
\(k\) derivatives there are at most
\(3\cdot4\cdots(k+2)=(k+2)!/2\) terms, each with \(k+3\)
variable leaves and one occurrence of each of the \(k+1\) input vectors.
Matrix products, transposes, outer products, and scalar contractions are
bounded by the product of the operator/vector norms. This construction
contains no free trace or unconstrained dimension sum. Consequently

\[
|K_{k+1}(v_0,\ldots,v_k;B,W,c)|
\le\frac{(k+2)!}{2}s^{k+3}\prod_{i=0}^k\|v_i\|_2.
\tag{8}
\]

In particular, the initial coefficient bound is

\[
|K_{k+1}(v_0,\ldots,v_k;0)|
\le32\,4^k(k+2)!\prod_{i=0}^k\|v_i\|_2.
\tag{9}
\]

Let \(R(B,W,c)=(B,W,-c)\). The identities
\(f_n\circ R=-f_n\) and \(V(v;R\theta)=-RV(v;\theta)\)
give by induction
\(K_r(\cdot;R\theta)=(-1)^rK_r(\cdot;\theta)\).
Since \(R\theta_0=\theta_0\), every odd initial rank vanishes. Thus,
in an expansion indexed by \(K_{k+1}(0)\), only odd \(k\) can survive.

### 2. The exact dense flow stays bounded

Write the evolving prediction coefficient as
\(w(t)=B(t)^\top W(t)^\top c(t)\in\mathbb R^d\), so
\(f_n(t,v)=v^\top w(t)\). Since \(\|Q\|_{\rm op}\le1\), the
physical equations are exactly

\[
\dot B=W^\top c(b-Qw)^\top,\qquad
\dot W=c[B(b-Qw)]^\top,\qquad
\dot c=WB(b-Qw).
\tag{10}
\]

Within distance one of the initial state in the maximum of the three
block norms, all block norms are at most five. Thus \(\|w\|_2\le125\),
\(\|b-Qw\|_2\le126\), and each block velocity is at most
\(25\cdot126=3150\). A first exit before time \(T\) would require
distance one, whereas the displacement is at most \(3150T<1\).
The finite-dimensional polynomial vector field is locally Lipschitz;
local uniqueness and the bounded trajectory therefore give a unique
solution throughout \([0,T]\).

Apply (8) with \(k=1,s=5\) to
\(\dot f_n(t,v)=K_2(v,b-Qw(t);\theta(t))\). Taking the supremum over
unit \(v\) gives

\[
\|w(t)\|_2\le1875\int_0^t(\|b\|_2+\|w(s)\|_2)\,ds
\le\|b\|_2(e^{1875t}-1)<\|b\|_2\quad(0\le t\le T),
\tag{11}
\]

where the last strict inequality is for \(b\ne0\). The middle bound
can be obtained by integrating the scalar comparison equation
\(h'=1875(\|b\|_2+h),h(0)=0\). If \(b=0\), uniqueness in (10)
instead gives the stationary initial state directly.

### 3. Ordered integration retains the closure's own residual

For a continuous coefficient path \(z:[0,T]\to\mathbb R^d\), define

\[
a_z(t)=b-Qz(t)
 =\frac1m\sum_{a=1}^m(y_a-v_a^\top z(t))v_a.
\tag{12}
\]

The path-to-prediction map \(\mathcal F_q[z]\) is defined through its
pairing with every \(v\in\mathbb R^d\):

\[
v^\top\mathcal F_q[z](t)
=\sum_{k=1}^{q-1}
\int_{0<s_k<\cdots<s_1<t}
 K_{k+1}(v,a_z(s_1),\ldots,a_z(s_k);0)
\,ds_k\cdots ds_1.
\tag{13}
\]

The pairing is linear in \(v\), hence defines a unique vector.
The infinite version \(\mathcal F_\infty\) uses all \(k\ge1\).
The chronological order in (13) is fixed: the first appended source
index belongs to the latest integration time. No symmetry or replacement
of the ordered simplex by an unordered cube is assumed.

To verify the finite map, put
\(u_a(s)=(y_a-v_a^\top z(s))/m\), and for a sequence of sample indices
define

\[
I_{a_1\ldots a_k}[u](t)
=\int_{0<s_k<\cdots<s_1<t}\prod_{i=1}^k u_{a_i}(s_i)
\,ds_k\cdots ds_1,\qquad I_{\varnothing}=1.
\]

For each retained rank, write
\(\mathbf v=(v_0,v_{a_1},\ldots,v_{a_{r-1}})\) for its fixed input
slots. The reconstruction (using fresh summed indices on its right) is

\[
K_r^{(q)}(\mathbf v;t)
=\sum_{k=0}^{q-r}\sum_{a_1,\ldots,a_k}
 K_{r+k}(\mathbf v,v_{a_1},\ldots,v_{a_k};0)
 I_{a_1\ldots a_k}[u](t)
\tag{14}
\]

has the prescribed initial values and frozen top. Differentiating the
outer integration limit gives exactly (3), provided
\(z=\mathcal F_q[z]\). Indeed multilinearity and (12) identify its
rank-one equation with (13), and then its predictions are
\(f_{n,q}(t,v)=v^\top z(t)\). Thus each fixed point constructs an actual
solution of the original own-residual closure, including all retained
arrays. The finite array equations are polynomial and locally Lipschitz,
so this construction gives their unique solution as long as it exists.

The same ordered formula for the dense flow follows by repeatedly
integrating \(\dot K_r=\sum_a u_aK_{r+1,\ldots a}\), with
\(u_a=(y_a-f_n(v_a))/m\). After terms \(k=0,\ldots,N-1\), the
remainder is an \(N\)-fold ordered integral whose integrand is

\[
K_{N+1}(v,a_w(s_1),\ldots,a_w(s_N);\theta(s_N)).
\]

When integrating a tensor in this iteration, its external source vectors
are held fixed; dependence of \(a_w(s_i)\) on its already chosen time
does not introduce a derivative of the residual. By (11), each such
vector has norm at most \(2\|b\|_2\). From (8) and the simplex volume,
the remainder for unit \(v\) is at most

\[
\frac{125}{2}(N+1)(N+2)(10\|b\|_2 T)^N\longrightarrow0.
\tag{15}
\]

Therefore the dense path satisfies the exact identity
\(w=\mathcal F_\infty[w]\). This is a convergent series of ordered
source responses with the dense residual inside it, not a physical-time
Taylor truncation of the dense output.

### 4. Uniform contraction and the omitted tail

Suppose \(0<\|b\|_2\le1\), and use the complete space of continuous
paths with supremum Euclidean norm, restricted to its closed ball of
radius \(\|b\|_2\). There \(\|a_z\|_\infty\le2\|b\|_2\) and
\(\|a_z-a_{\widetilde z}\|_\infty\le
\|z-\widetilde z\|_\infty\). Put \(x=8T=1/4096\).
Equation (9) and the simplex volume give, for every finite or infinite
map,

\[
\|\mathcal F_q[z]\|_\infty
\le32\sum_{k\ge1}(k+1)(k+2)(x\|b\|_2)^k
\le\|b\|_2\,64[(1-x)^{-3}-1]<\frac{\|b\|_2}{16}.
\tag{16}
\]

A telescoping difference of the \(k\) source slots has \(k\) terms,
one difference slot and \(k-1\) slots of norm at most \(2\|b\|_2\).
The same calculation yields the common Lipschitz constant

\[
L\le16\sum_{k\ge1}k(k+1)(k+2)x^k\|b\|_2^{k-1}
\le\frac{96x}{(1-x)^4}<\frac1{32}.
\tag{17}
\]

The displayed strict inequalities are elementary at \(x=1/4096\):
\((1-x)^{-4}<4/3\), so the last bound in (17) is less than
\(1/32\); the scalar factor in (16) is at most
\(192x(1-x)^{-4}<1/16\).
All infinite series converge uniformly by these bounds. Successive
iteration of each map from the zero path is Cauchy, with differences
bounded by powers of \(L<1\); completeness gives its unique fixed
point in the ball; denote the finite fixed point by \(w_q\).
Equations (14) and (11)--(15) identify these fixed
points with the actual finite and dense physical trajectories. In
particular every finite closure exists on the whole interval, not just
formally at its initial state.

By parity, the first possibly nonzero omitted term in (13) has
\(k=j=2\lfloor q/2\rfloor+1\). With \(z_0=x\|b\|_2\), its entire
omitted tail on the path ball is bounded by

\[
\begin{aligned}
R_q
&\le32\sum_{k\ge j}(k+1)(k+2)z_0^k\\
&\le32(j+1)(j+2)z_0^j\frac{1+z_0}{(1-z_0)^3}.
\end{aligned}
\tag{18}
\]

For the second inequality, put \(k=j+\ell\) and use
\((j+\ell+1)(j+\ell+2)\le(j+1)(j+2)(\ell+1)^2\), followed by
\(\sum_{\ell\ge0}(\ell+1)^2z^\ell=(1+z)/(1-z)^3\).
Comparing the two own-residual fixed points gives

\[
\|w-w_q\|_\infty
\le\|\mathcal F_\infty[w]-\mathcal F_q[w]\|_\infty
  +\|\mathcal F_q[w]-\mathcal F_q[w_q]\|_\infty
\le R_q+L\|w-w_q\|_\infty.
\tag{19}
\]

At the chosen \(x\),
\((1+x)/[(1-x)^3(1-L)]<2\). Equations (18)--(19) prove the first
bound in (5). The equality
\(\sup_{\|v\|=1}|v^\top(w-w_q)|=\|w-w_q\|_2\) proves that the
estimate controls the whole test sphere with no factor in \(d\).
Finally, \((j+1)(j+2)\le4^j\) for every \(j\ge2\),
\(j\ge q\), and \(\|b\|_2^j\le\|b\|_2\), proving its second bound.
For \(b=0\), (13)--(14) at the zero path supply the stationary
closure and complete the omitted case.

### 5. The Gaussian event

For completeness, take a deterministic \(1/4\)-net of the unit sphere
in \(\mathbb R^d\) with cardinality at most \(9^d\). Such a net
comes from a maximal separated set: its disjoint radius-\(1/8\) balls
lie inside the radius-\(9/8\) ball. For any linear map \(A\), this net
gives \(\|A\|_{\rm op}\le(4/3)\max_v\|Av\|_2\).
For fixed unit \(v\), \(n\|B_0v\|_2^2\) is chi-square with \(n\)
degrees of freedom. Its moment-generating function
\((1-2t)^{-n/2}\), at \(t=4/9\), and exponential Markov give

\[
\Pr\{\|B_0v\|_2>3\}\le e^{-4n}9^{n/2}.
\]

The net union bound, with \(d\le n\), proves
\(\Pr\{\|B_0\|_{\rm op}>4\}\le e^{-c_*n}\).
The identical argument for the square matrix \(W_0\) proves (6).
This argument is independent of any dataset and uses no external
concentration result.

## Retained arrays, queries, and limits of the claim

For the literal training arrays of order \(q\), the number of moving
entries is \(\sum_{r=1}^{q-1}m^r\), and the frozen top has \(m^q\)
entries. The labels add \(m\) fixed scalars. These are the actual ranks
in (3); the proof does not charge the frozen top as moving state.

To supply the whole input sphere by finitely many passive queries, retain
the same hierarchy also with the first slot equal to each coordinate
vector \(e_1,\ldots,e_d\), leaving every driving slot a training index.
Input linearity gives the exact decoder

\[
f_{n,q}(t,v)=\sum_{i=1}^d v_i f_{n,q}(t,e_i).
\tag{20}
\]

Counting these passive arrays in addition to the training arrays gives

\[
N_{\rm moving}=(m+d)\sum_{r=1}^{q-1}m^{r-1},\qquad
N_{\rm frozen}=(m+d)m^{q-1}.
\tag{21}
\]

Thus for \(m\ge2\), their sum is at most
\(2(m+d)m^{q-1}\), and the moving part at most
\(2(m+d)m^{q-2}\). For \(m=1\), the exact counts are
\((1+d)(q-1)\) moving and \(1+d\) frozen. The redundant training
first slots could instead be decoded from the coordinate slots, but
(21) does not use that possible saving. Odd frozen tops vanish and can
be omitted, giving the same predictor as the preceding even order;
(21) is an upper count that does not need this simplification.

The fixed dataset costs at most \(md+m\) scalars if kept. Constructing
the initial coefficients is additional preprocessing, using the sampled
\(B_0,W_0\) and the data. The sampled matrices initially contain
\(nd+n^2\) entries and need not be retained after all NTH initial
coefficients are formed. No bound on coefficient-generation time, bit
precision, or numerical time-discretization error is asserted. The
retained-array count and (5) concern the exact autonomous ODE (3), which
can continue from its current finite arrays and fixed top.

For the hard-family dimensions \(d=m+1\), \(m\ge4\), (21) is at most
\(5m^q\). Combining with (7), absolute tolerance \(n^{-p}\) costs

\[
N_{\rm retained}\le\exp[O_p(\log m\,\log n)].
\tag{22}
\]

For \(m\asymp n^a\) with fixed \(0<a\le1/2\), this is
\(\exp[O_p((\log n)^2)]\); for fixed \(m,d\) it is polynomial
in \(n\). More generally the precise count keeps its factor \(m+d\),
so it should not be suppressed when \(d\) grows independently of \(m\).

This proves a geometric forward upper bound for the unchanged original
closure in the source's identity-activation, zero-readout, canonical-metric
model on its fixed physical window. It does not extend the horizon,
change the activation to a nonlinear one, or establish a bound for an
arbitrary encoding of tensors. It also does **not**, by itself, turn (22)
into a sufficient budget relative to an actual realized dense-pair
discrepancy: such a conclusion needs a lower bound on that discrepancy.
An upper concentration bound alone cannot supply that comparison. When
\(b=0\), both dense outputs and the closure are exactly zero, so
comparison ratios must handle that case without division by zero.

## Author check and independent reconstruction

The author checked the polynomial leaf count, chronological index order,
reconstruction of every retained rank, both models' distinct residuals,
the uniform dense remainder, parity at odd frozen tops, the \(b=0\)
case, the whole-sphere dual norm, the explicit contraction constants,
the Gaussian net exponent, and the separate moving/frozen counts.
The proof uses only finite-dimensional polynomial ODE uniqueness,
elementary contraction iteration, and the explicitly derived estimates.
No research experiment or numerical evidence enters the theorem.
A fresh scoped reconstruction of this complete proof and its matching
upper/lower assembly passed; see [MATCHING_CHECK.md](MATCHING_CHECK.md).
Promotion would require the separate repository promotion process.
