# Fresh bounded check of the universal compression paper

Reviewed 2026-10-11. Source: Hong-Yi Wang, Di Luo, Tomaso Poggio, Isaac L. Chuang, and Liu Ziyin, *A universal compression theory for lottery ticket hypothesis and neural scaling laws*, published ICLR 2026, [26-page proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/bc71544dfef150412977e59d221b6597-Paper-Conference.pdf).

This is an isolated, venue-neutral mathematical audit of Theorems 3, 5, 7, and 8, with the related definitions and proofs. The complete supplied text, including all appendices and experimental descriptions, was read. Printed pages 3, 5, 8, 15–22 were visually checked using the local PDF; the corresponding `fresh_check_page_*.png` files are in the assigned generated-data directory. No prior review, study history, other study, supplementary code, or external cited paper was inspected. Consequently, the external Remez citation is not independently verified here: the finding below concerns an invalid inference even granting the inequality printed in this paper. The requested single-report format supersedes the general review skill's multi-artifact format. The review, severity, rigorous-math, and canonical-notation instructions were applied.

## Assessment

Assumption 1 does **not** imply the width-uniform error claimed in Theorem 3. A fixed polynomial deep-set function gives a direct counterexample to its displayed bound, even when compression is allowed to choose arbitrary nonnegative weights and need not preserve moments. This invalidates a foundational bound used by the supplied proofs of Theorems 4, 7, and 5. The example does not, by itself, disprove their ultimate polylogarithmic-size conclusions.

Theorem 8's supplied optimality proof has two independent invalid steps: Lemma 2 is false, and the asserted conversion from Voronoi-cell volumes to counts inside arbitrary polynomial superlevel sets is false. The claimed optimality rate is therefore unproved by this argument; this audit does not establish that the rate is false under a suitable quantitative analytic function class.

Even setting these proof defects aside, Theorem 5 is a conditional statement about a specified equivariant training map and scalar observable whose composition satisfies Assumption 1, with fixed object dimension. It does not prove an autonomous polylogarithmic state for a network whose hidden layers all widen, or an error bound uniform over all training times through a fitted limit.

## Setup and notation

Preserve the paper's symbols: there are $d$ objects $w_i\in\mathbb R^m$, where $m$ is fixed in the asymptotic argument; $m$ is not the number of training samples here. Assumption 1 (p. 3) requires a representation

\[
f_d(w_1,\ldots,w_d)=h\!\left(\sum_{i=1}^d g(w_i)\right),
\]

with $h,g$ independent of $d$ and Taylor-expandable. For weighted objects it defines the extension

\[
f_d(\theta')=h\!\left(\sum_j c_jg(w_j)\right),\qquad c_j\ge0.
\]

The moment method preserves total mass $\sum_jc_j=d$ and tensor moments through order $k$, leaving at most $N_{m,k}=\binom{m+k}{k}$ active objects in one cluster. Theorem 3 claims an error $O(dr^{k+1})$, where $r$ is the cluster diameter. Its intended constant must be independent of $d$: that width dependence is explicitly asserted in Appendix A.3 and used in the subsequent asymptotics. If the constant can grow arbitrarily with $d$, it cannot support those uses.

## M1 — Theorem 3: confirmed counterexample to its width-uniform bound

Take $m=1$, $k=1$, a fixed $a>0$, and $d$ divisible by three. Let the original objects contain $d/3$ copies of each of $-a,0,a$, all with unit weights. Thus $r=2a$ and $N_{1,1}=2$.

Define a fixed five-dimensional feature map and a fixed scalar function by

\[
g(w)=(1,w,w^2,w^3,w^4),\qquad
h(s_0,s_1,s_2,s_3,s_4)
=\det\begin{pmatrix}
s_0&s_1&s_2\\
s_1&s_2&s_3\\
s_2&s_3&s_4
\end{pmatrix}.
\]

Both are polynomials independent of $d$. For $v(w)=(1,w,w^2)^\top$, the resulting symmetric function is

\[
f_d(\theta)=\det\!\left(\sum_i v(w_i)v(w_i)^\top\right).
\]

For the stated objects, the matrix is

\[
d\begin{pmatrix}
1&0&2a^2/3\\
0&2a^2/3&0\\
2a^2/3&0&2a^4/3
\end{pmatrix},
\qquad
f_d(\theta)=\frac{4d^3a^6}{27}.
\]

Every weighted set supported on at most two points gives a matrix $\sum_jc_jv(w_j)v(w_j)^\top$ of rank at most two. Therefore its value of $f_d$ is zero. This applies to every choice of nonnegative weights, whether or not moments are preserved, and even if the two support locations are allowed to move. The smallest possible error obeys

\[
\frac{|f_d(\theta')-f_d(\theta)|}{dr^2}
=\frac{d^2a^4}{27}\longrightarrow\infty.
\]

This directly contradicts the intended $O(dr^{k+1})$ bound. The ball may be arbitrarily small: choose any fixed small $a$. One can also let $a=d^{-1/4}$, obtaining a shrinking diameter while the displayed ratio still diverges.

The wording “finite radii” does not exclude this example under the paper's own interpretation: Appendix B, p. 19, explicitly treats polynomials as satisfying its global analytic assumption. If strictly finite complex radii were intended, the same construction can be made rational: replace each component by $g_j(w)=w^j/(1+w^2)$, $j=0,\ldots,4$, and set $h(s)=D(s)+1/(1+D(s)^2)$, where $D(s)$ is the displayed determinant. The original determinant becomes $4d^3a^6/[27(1+a^2)^2]$; every two-point compressed determinant remains zero. The output error remains of order $d^3a^6$, with both maps real analytic and having complex singularities.

The proof defect is visible already in Eq. (34), p. 15. Its coefficient includes

\[
d\,Dh(dg(w_0))\,a_{k+1},
\]

where $a_{k+1}$ is a Taylor coefficient of $g$. Independence of the **formula** for $h$ from $d$ does not bound its derivative at the moving argument $dg(w_0)$. For example, $h(s)=s^2$, $g(w)=1+w^2$, and $w_0=0$ give $Dh(d)=2d$, producing a coefficient proportional to $d^2$. The proof also replaces the full function difference by the first unmatched homogeneous term in Eq. (33), without controlling the higher-order remainder. The determinant example shows why such higher terms cannot be discarded uniformly in $d$.

**Classification:** Clearly False for the width-uniform Theorem 3 statement; Major Flaw M1. Requiring quantitative uniform control of the outer map and Taylor remainders would materially narrow the theorem, while retaining the useful moment-matching strategy. This is not merely a missing harmless constant.

**Dependency:** Theorems 4 and 7 sum this local bound, and Theorem 5 explicitly invokes those results. Their supplied error proofs are therefore unsupported. The counterexample itself is exactly retained with three support points, so it is not a counterexample to eventual polylogarithmic support size. That distinction is essential.

## M2 — Theorem 7: additional gaps when the order grows

Appendix A.6 explicitly fixes $m$ while permitting $k$ to grow. In addition to M1, its passage to Eq. (46) does not establish constants uniform in $k$.

First, a radius of convergence $\rho$ alone does not imply Taylor coefficients are $O(\rho^{-k})$ at the exact boundary radius. For example, $g(w)=(1+w^2)^{-2}$ has radius one about zero and even-order coefficients $(-1)^j(j+1)$. Their magnitudes are unbounded. A coefficient bound at a strictly smaller radius, together with a bound on the analytic extension, is a different and potentially usable statement. The paper does not supply it for the relevant cluster centers and compositions.

Second, the geometric estimate used earlier is $r\le C_mR[(N_{m,k}+1)/N]^{1/m}$, with geometric constants. Raising $r$ to $k+1$ raises $C_mR$ to the same power. Such factors cannot be hidden in a $k$-independent prefactor when optimizing $k$. Their omission matters to the exponential constant in Eq. (44).

Third, there is an explicit algebraic discrepancy. Starting from Eq. (46) as printed and using $\log N_{m,k}=m\log k-\log(m!)+O(k^{-1})$, one obtains

\[
\log(\Delta E/d)
=(k+1)\log k-\frac{k+1}{m}\log(m!N)-k\log\rho+O(1).
\]

The last line of Eq. (47) replaces these terms by 

\[
(k+1)\log k-\frac{k+1}{m}\log(m!N\rho)+O(1),
\]

which differs by order $k$ when $m>1$ and $\rho\ne1$. Even accepting its input bound, the leading stationary value is $k\sim\rho(m!N)^{1/m}/e$, rather than the printed $k\sim(m!N\rho)^{1/m}/e$.

**Classification:** Major Flaw M2 in the supplied growing-order estimate, compounded by M1. The specific bound (44) and its derivation are not verified. The broad polylogarithmic rate remains plausible for appropriately bounded analytic functions in fixed object dimension; no such repaired theorem is claimed here.

## M3 — Theorem 8: the supplied optimality proof is invalid

The construction begins sensibly: a polynomial space with dimension exceeding $d'$ contains a nonzero polynomial $q$ vanishing at all $d'$ compressed support points. Then $g=q^2\ge0$ has zero integral against the compressed measure. The unproved task is a quantitative positive lower bound on its values at the original nodes, uniform over the admissible $q$.

**Lemma 2 is false as printed.** Set $D=[-1,1]$, $p(x)=x$, $k=1$, and $t=1/2$. Its normalized superlevel-set volume is

\[
\frac{|\{x\in D:|p(x)|\ge1/2\}|}{|D|}=\frac12,
\]

whereas Eq. (57) demands at least $1-(t/2)^{1/k}=3/4$. The proof's error is Eq. (63): from $1\le T_k(A)t$ and a **lower** bound on $T_k(A)$, one cannot infer that 1 is bounded by the substituted lower bound. This is a logical direction error even if the cited Remez inequality (58) is granted.

**The discrete point-count inference is independently false.** Theorem 8, immediately before Eq. (67), asserts that its Voronoi-volume definition of quasi-uniformity gives

\[
\#(X_d\cap S)\ge \frac{d}{c_D}|S|.
\]

It does not. A counterexample within the type of set actually needed is $D=[0,1]^2$ and

\[
x_i=((i-1/2)/d,1/2),\qquad i=1,\ldots,d.
\]

Each Voronoi cell intersected with $D$ is a vertical strip of area $1/d$, satisfying Definition 3 with $C_D=1$. Nevertheless, the normalized degree-one polynomial $q(x,y)=2y-1$ vanishes at every original node. Its set $S_{1/2}=\{|q|\ge1/2\}\cap D$ has area $1/2$ and contains zero nodes. Thus the very sampling implication used to turn a continuous lower bound into Eq. (67) fails even for a degree-one polynomial superlevel set and arbitrarily large $d$.

This does not show that no better original distribution can be chosen, or that no valid sampling estimate exists with additional hypotheses. It shows that the stated definition and printed argument do not prove the needed estimate. Choosing a well-spaced grid and proving an appropriate degree-dependent discrete norming inequality would be additional mathematics, not an inference already supplied here.

**Quantifiers need a common function class.** The adversarial $q$ depends on the compressed support and its degree grows with $d'$. This is naturally a worst-case statement over a function class, not automatically a lower bound for one fixed width-independent pair $h,g$. The construction normalizes $q$ on the real domain but does not place it in a common bounded analytic neighborhood with the uniform constants needed by an upper theorem. The assumption that each individual function is analytic is not itself such a common norm bound. Consequently, claiming a matching upper and lower minimax rate requires a precise shared class and constant dependence.

The missing primes in Eq. (70), the negative sign assigned to $B$ after Eq. (71), and the power of $B$ in Eq. (73) appear locally correctable. They are not the controlling concerns above.

**Classification:** Confirmed false auxiliary lemma and confirmed false sampling inference; Major Flaw M3 in the optimality proof. The rate itself is **unestablished by this proof**, not refuted here. Substantial ideas remain reusable: polynomial dimension counting, vanishing at the compressed nodes, and squaring to obtain nonnegativity.

## Theorem 5: what its conditional dynamical statement covers

The symmetry step in Lemma 3 is sound: if $f\circ R(\sigma)=f$ and $T\circ R(\sigma)=R(\sigma)\circ T$, then $f\circ T\circ R(\sigma)=f\circ T$. A fixed sequence of ordinary gradient updates on a neuron-permutation-invariant loss is equivariant; Appendix C also explains how to hold the mini-batch sequence fixed. These are useful exact observations.

For its explicit two-layer model, the paper gives an autonomous weighted update: retain neuron parameters $w_j$ and constant masses $c_j$, evaluate the weighted network, and replace each parameter gradient by $c_j^{-1}\partial L/\partial w_j$ on positive-weight neurons. This is a concrete training construction. Its existence does not establish the claimed approximation rate, whose proof inherits M1–M2.

Even if the compression estimates were repaired, the theorem's scope would remain conditional:

- It assumes the particular composite $f\circ T$ satisfies Assumption 1. Equivariance proves its symmetry, not its required analytic representation or quantitative bounds. The paragraph after Theorem 5 explicitly acknowledges that preservation of Assumption 1 through training is not established.
- It estimates one scalar observable after a specified map $T$. Taking $T=T_t$ for different training durations requires quantitative bounds for each duration. No uniform estimate over $t\ge0$, convergence to fitted limits, or interchange of width and long-time limits is proved.
- Its compression is coupled to the given initial parameter set, and stochastic examples can share a mini-batch path. This is useful pathwise conditioning. It does not supply an all-time probability or error theorem over random initialization and stochastic training.
- The asymptotic proof keeps $m$ fixed. For compression of a hidden layer, an object includes its incoming and outgoing parameter vectors; their dimension grows when neighboring layers widen. The paragraph after Theorem 5 expressly leaves the deep-network compression scaling open. Thus a bound proportional to $\log^m d$ does not establish fixed-degree polylogarithmic total state for all-wide deep networks.
- Absorbing $c_j$ into an outgoing weight proves equality of network **functions**. It does not automatically identify the modified weighted optimizer with ordinary training of the reparameterized small network at the original learning rates.

The best supported characterization is therefore **a conditional compression program for specified symmetric observables of equivariant maps, with explicit weighted training rules and finite experiments**. Calling it an established all-wide deep-network closure or an all-time fitted-limit approximation would exceed both its stated scope and its verified mathematics.

## Severity, surviving contribution, and verification limits

| ID | Checked finding | Effect |
|---|---|---|
| M1 | Direct counterexample to the width-uniform Theorem 3 bound | Invalidates the shared local estimate in the presented proofs of Theorems 4, 7, and 5 |
| M2 | Growing-order constants and algebra do not justify Theorem 7's exponential estimate | Polylogarithmic conclusion is unsupported by the supplied proof; not independently disproved |
| M3 | False Lemma 2 and false discrete sampling inference | Theorem 8's optimality argument is invalid; an appropriately formulated lower rate remains open in this audit |

The useful surviving content includes nonnegative moment-matching compression, the symmetry/equivariance connection, explicit weighted training rules in the examples, and numerical evidence for selected finite training tasks. Those contributions are not erased by the proof defects. Conversely, empirical agreement does not establish the missing width, order, or time-uniform analytic estimates.

Confidence is high in the counterexamples and the specific algebraic and logical findings: they are elementary and were checked against the printed equations. This was not a complete external-citation audit, code reproduction, or proof that every possible repaired compression theorem fails. No numerical research experiment was run.
