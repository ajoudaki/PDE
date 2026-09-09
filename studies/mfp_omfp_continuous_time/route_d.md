# Route D: a closed spectral OMFP theorem for the identity activation

## 1. Result and claim boundary

This note gives a genuine, unconditional pressure test of the uniform
remainder mechanism.  It keeps the exact Gaussian initialization, every
reused matrix, and the required order of limits.  The price is a strong
activation restriction:

\[
                         \phi(x)=x.                 \tag{1.1}
\]

For this activation the nonlinear Nemytskii obstruction disappears and
the already width-limited reused-matrix DAG becomes a dimension-free
multilinear Euler system on a trace-class operator state.  We first
identify that state at every fixed nonzero schedule and only then prove
the local coarse/fine estimate.  No finite-width derivative is
interchanged with the width limit.

Write

\[
 D_{t,L}(h):=F_{t,L}(2h)-F_{2t,L}(h),              \tag{1.2}
\]

where every \(F_{N,L}(h)\) is first defined as the pointwise fixed-\(h\)
width limit of the actual network.  For integers \(q,r\geq0\), put

\[
 (q)_r=\begin{cases}q!/(q-r)!,&r\leq q,\\0,&r>q,\end{cases}             \tag{1.3}
\]

and define

\[
 K_L:=\max\left\{
 1,
 \max_{0\leq r\leq\min\{4,L\}}
       (L+1)(L)_r3^{L-r},
 \max_{1\leq r\leq\min\{4,L+1\}}
       (L+1)_r3^{L+1-r}
 \right\},
 \qquad c_L:={1\over16K_L}.                         \tag{1.4}
\]

Let \(C(K)\) be the explicit finite recursion in Section 4 below and put

\[
                         C_L:=C(K_L).               \tag{1.5}
\]

### Theorem 1.1 (identity-activation uniform fifth remainder)

For every hidden depth \(L\geq1\), every integer \(t\geq1\), and every
real \(h\) satisfying \(|h|\leq c_L/t\),

\[
 \boxed{
 \left|
 D_{t,L}(h)
 +{t(2t-1)L(L+1)^2(L+2)\over3}\,h^3
 \right|
 \leq C_Lt^4|h|^5 .}                              \tag{1.6}
\]

Equivalently, for the canonical coefficient

\[
 b^*_{t,L}(\rho):=
 \sup_{0<|h|\leq \rho/t}
 {\left|D_{t,L}(h)-\kappa_{t,L}h^3\right|\over |h|^5},
 \qquad
 \kappa_{t,L}:=-{t(2t-1)L(L+1)^2(L+2)\over3},       \tag{1.7}
\]

one has

\[
                    \boxed{b^*_{t,L}(c_L)\leq C_Lt^4.}                 \tag{1.8}
\]

In particular,

\[
\begin{array}{c|c|c|c}
L&K_L&c_L&\kappa_{t,L}\\ \hline
2&27&1/432&-24t(2t-1)\\
3&108&1/1728&-80t(2t-1).
\end{array}                                                    \tag{1.9}
\]

Thus the requested \(O(t^4)\) fifth remainder is proved for both
\(L=2\) and \(L=3\), in fact for every fixed depth, on a completely
explicit radius.  The theorem is restricted to the identity activation;
Section 9 explains exactly why this proof does not establish the result
for a nonlinear activation.

## 2. The exact width-first operator state

For each hidden layer let \(\mathcal H_a=L^2(\Omega_a)\).  The already
proved fixed-operator realization of adaptive Gaussian conditioning gives,
for each connector, bounded maps

\[
 I_a:\mathcal H_{a-1}\to\mathcal H_a,
 \qquad J_a:\mathcal H_a\to\mathcal H_{a-1},             \tag{2.1}
\]

whose images are independent first-chaos blocks and which are isometries
onto those blocks.  Put

\[
 W_{a,0}=I_a+J_a^*,\qquad W_{a,0}^*=I_a^*+J_a,
 \qquad\|W_{a,0}\|_{\rm op}\leq2.                       \tag{2.2}
\]

The \(I_a\) term is the fresh forward Gaussian action; \(J_a^*\) is its
complete adaptive transpose-response action.  Symmetrically, \(J_a\) is
the fresh transpose action and \(I_a^*\) is the forward-response action.
These are fixed operators, so singular history Grams require no inverse.

Let \(\mathfrak S_1(\mathcal H_{a-1},\mathcal H_a)\) be the trace-class
operators and define the Banach state

\[
 \mathcal X_L=\mathcal H_L\oplus\mathcal H_1\oplus
 \bigoplus_{a=2}^L
 \mathfrak S_1(\mathcal H_{a-1},\mathcal H_a),           \tag{2.3}
\]

with sum norm

\[
 \|(a,u,K_2,\ldots,K_L)\|_{\mathcal X_L}
 =\|a\|_2+\|u\|_2+\sum_{a=2}^L\|K_a\|_1.              \tag{2.4}
\]

Choose independent unit Gaussians \(A\in\mathcal H_L\) and
\(U\in\mathcal H_1\), in endpoint seed blocks, and put

\[
                         \theta_0=(A,U,0,\ldots,0).       \tag{2.5}
\]

For \(\theta=(a,u,K_2,\ldots,K_L)\), set

\[
 W_a(\theta)=W_{a,0}+K_a,qquad
 H_1=u,qquad H_a=W_a(\theta)H_{a-1},                    \tag{2.6}
\]

\[
 C_L=a,qquad C_{a-1}=W_a(\theta)^*C_a,                 \tag{2.7}
\]

and

\[
 \mathcal F(\theta)=\langle a,H_L\rangle,
 \qquad
 \mathcal G(\theta)=
 \bigl(H_L,C_1,(C_a\otimes H_{a-1})_{a=2}^L\bigr).      \tag{2.8}
\]

Here \((y\otimes x)v=y\langle x,v\rangle\), and

\[
                         \|y\otimes x\|_1=\|y\|_2\|x\|_2.             \tag{2.9}
\]

Thus \(\mathcal G\) maps \(\mathcal X_L\) to itself and is a polynomial
vector field.  Its Euler map is

\[
                         E_h=I+h\mathcal G.              \tag{2.10}
\]

### Lemma 2.1 (exact fixed-step intertwining)

For every finite real schedule \((\varepsilon_0,\ldots,
\varepsilon_{N-1})\), the inverse-free width-first Gaussian DAG for the
identity activation equals the operator Euler recursion

\[
 \theta^{s+1}=E_{\varepsilon_s}\theta^s,qquad
 F_{N,L}(\varepsilon)=\mathcal F(\theta^N).              \tag{2.11}
\]

Consequently (2.11) is the pointwise fixed-step limit of the actual
finite-width Gaussian network, including all reused-matrix dependencies.

#### Proof

After \(s\) updates,

\[
 K_a^s=\sum_{r<s}\varepsilon_r
                C_{a,r}\otimes H_{a-1,r}.               \tag{2.12}
\]

Therefore

\[
 K_a^sH_{a-1,s}
 =\sum_{r<s}\varepsilon_r
   \langle H_{a-1,r},H_{a-1,s}\rangle C_{a,r},           \tag{2.13}
\]

which is exactly the learned forward Gram term, while

\[
 (K_a^s)^*C_{a,s}
 =\sum_{r<s}\varepsilon_r
   \langle C_{a,r},C_{a,s}\rangle H_{a-1,r}              \tag{2.14}
\]

is exactly the learned reverse Gram term.  The fixed actions decompose as

\[
 W_{a,0}H=I_aH+J_a^*H,qquad
 W_{a,0}^*C=J_aC+I_a^*C.                                \tag{2.15}
\]

Gaussian integration by parts for the fixed first-chaos maps identifies
\(J_a^*H\) and \(I_a^*C\) with the complete sums of adaptive response
coefficients.  Because (2.15) is an intrinsic adjoint identity, it remains
valid for dependent moving queries and singular history Grams.  Equations
(2.13)--(2.15), followed by the rank-one update in (2.8), give a literal
induction through every forward and reverse node of the DAG.  This proves
the first assertion.

The exact full-step operator/DAG equality is the fixed-operator theorem in
temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md, Section 4.3.  The
adaptive row/column conditioning theorem in
temporary_depth_time_doubling/WIDTH_DEPTH_TIME.md proves convergence
and uniform integrability of the actual network to that same inverse-free
DAG at each fixed schedule.  Combining these results with
(2.12)--(2.15) proves the second assertion. \(\square\)

### Lemma 2.2 (dimension-free global derivatives near initialization)

On the closed unit ball \(\overline B(\theta_0,1)\subset\mathcal X_L\),

\[
 \|D^r\mathcal G(\theta)\|
 \leq(L+1)(L)_r3^{L-r},\qquad0\leq r\leq L,             \tag{2.16}
\]

and

\[
 |D^r\mathcal F(\theta)|
 \leq(L+1)_r3^{L+1-r},\qquad0\leq r\leq L+1.           \tag{2.17}
\]

#### Proof

On that ball, \(\|a\|_2,\|u\|_2\leq2\),
\(\|K_a\|_1\leq1\), and hence

\[
                         \|W_a(\theta)\|_{\rm op}\leq3.               \tag{2.18}
\]

Each of the \(L+1\) components of \(\mathcal G\) is one \(L\)-factor
word: \(H_L\), \(C_1\), or

\[
 C_a\otimes H_{a-1}
 =\bigl(W_{a+1}^*\cdots W_L^*a\bigr)
  \otimes
  \bigl(W_{a-1}\cdots W_2u\bigr).                      \tag{2.19}
\]

Operator composition is submultiplicative and (2.9) controls the
trace-class block.  An \(r\)-th derivative chooses an ordered list of
\(r\) distinct slots, giving \((L)_r\) terms; the remaining factors cost
at most \(3^{L-r}\).  The sum norm adds at most the \(L+1\) component
bounds.  This proves (2.16).  The scalar observable is one
\((L+1)\)-factor word, so the same slot count gives (2.17). \(\square\)

By (1.4), Lemma 2.2 implies on this ball

\[
 \|D^r\mathcal G\|\leq K_L\quad(0\leq r\leq4),
 \qquad
 |D^r\mathcal F|\leq K_L\quad(1\leq r\leq4).            \tag{2.20}
\]

## 4. The transported macro-defect lemma and its explicit constant

We record the deterministic lemma used below.  It is valid on any real
Banach space, so its constant is dimension free.

### Lemma 4.1 (uniform transported defect)

Let \(f\in C^4\), \(g\in C^4\) on the closed unit ball about \(x_0\),
and suppose

\[
 \|D^rg\|\leq K\quad(0\leq r\leq4),\qquad
 |D^rf|\leq K\quad(1\leq r\leq4),\qquad K\geq1.         \tag{4.1}
\]

Put \(E_h=I+hg\), \(C_h=E_{2h}\), and \(B_h=E_h^2\).  For
\(c=(16K)^{-1}\), there is an exact factorization

\[
 f(C_h^tx_0)-f(B_h^tx_0)=h^2Q_{t,x_0}(h),               \tag{4.2}
\]

valid for \(|h|\leq c/t\), with

\[
 \sup_{|h|\leq c/t}|Q_{t,x_0}^{(3)}(h)|
 \leq6C(K)t^4.                                         \tag{4.3}
\]

Here \(C(K)\) is the following terminating numerical recursion.  Set

\[
\begin{aligned}
 X_1&=8K,\\
 X_2&=2\{8KX_1+4cKX_1^2\},\\
 X_3&=2\{12K(X_1^2+X_2)+4cK(X_1^3+3X_1X_2)\},
\end{aligned}                                           \tag{4.4}
\]

\[
 G_0=K,\quad G_1=KX_1,\quad
 G_2=K(X_2+X_1^2),\quad
 G_3=K(X_3+3X_1X_2+X_1^3),                              \tag{4.5}
\]

\[
 A_r=\sum_{q=0}^r{r\choose q}G_qG_{r-q}\quad(0\leq r\leq3),           \tag{4.6}
\]

with \(A_{-1}=A_{-2}=0\), and

\[
 Z_r=X_r+c^2A_r+2rcA_{r-1}+r(r-1)A_{r-2}\quad(1\leq r\leq3).          \tag{4.7}
\]

Next set

\[
\begin{aligned}
 T_1&=2(Z_1+2K),\\
 T_2&=2\{Z_2+4KT_1+2cKT_1^2\},\\
 T_3&=2\{Z_3+6K(T_1^2+T_2)+2cK(T_1^3+3T_1T_2)\},
\end{aligned}                                           \tag{4.8}
\]

\[
 H_0=K,\quad H_1=KT_1,\quad
 H_2=K(T_2+T_1^2),\quad
 H_3=K(T_3+3T_1T_2+T_1^3).                              \tag{4.9}
\]

Put \(W_0=2A_0\), and for \(1\leq r\leq3\) define successively

\[
 W_r=2\left\{A_r
 +2c\sum_{q=1}^r{r\choose q}H_qW_{r-q}
 +2r\sum_{q=0}^{r-1}{r-1\choose q}H_qW_{r-1-q}\right\},              \tag{4.10}
\]

and finally

\[
 C(K)={1\over6}\sum_{q=0}^3{3\choose q}H_qW_{3-q}.                    \tag{4.11}
\]

Every range in (4.4)--(4.11) is finite and each right-hand side only
uses quantities already defined, so the recursion terminates.

#### Proof

The exact local identity is

\[
 B_hx=C_hx+h^2a_h(x),qquad
 a_h(x)=\int_0^1Dg(x+shg(x))g(x)\,ds.                  \tag{4.12}
\]

Apply \(A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j\) to the pullback
operators of \(C_h\) and \(B_h\).  This gives (4.2), with \(Q\) the
sum of exactly \(t\) transported local defects.

Every path used in this representation has total Euler coefficient at
most \(4t\).  Since \(|h|t\leq c\), its displacement before a possible
first exit is at most \(4cK\leq1/4\); the interpolation in (4.12) adds
at most \(c^2K^2\leq1/256\).  Thus all paths stay in the unit ball.

Differentiate a variable-step path

\[
 x_{m+1}=x_m+\alpha_mhg(x_m),qquad
 0\leq\alpha_m\leq2,qquad\sum_m\alpha_m\leq4t.         \tag{4.13}
\]

The homogeneous tangent products are bounded by

\[
 \prod_m(1+\alpha_m|h|K)
 \leq e^{4cK}<2.                                      \tag{4.14}
\]

Directly differentiating (4.13) once, twice, and three times and using
(4.14) gives

\[
                    \sup_m\|x_m^{(r)}\|\leq X_rt^r,
                    \qquad1\leq r\leq3,               \tag{4.15}
\]

with exactly the enlarged right-hand sides (4.4).  Faà di Bruno for
\(g(x(h))\), followed by Leibniz in (4.12), gives (4.5)--(4.7).
Repeating (4.15) from the interpolated point gives (4.8)--(4.9).

The transported defect direction obeys

\[
                         w^+=w+hDg(x)w.                \tag{4.16}
\]

Three differentiations of (4.16), followed by (4.14), give successively
(4.10), i.e. \(\|w^{(r)}\|\leq W_rt^r\).  The transported scalar is
\(Df(x)[w]\); three applications of Leibniz give the summand bound

\[
 \left|{d^3\over dh^3}Df(x(h))[w(h)]\right|
 \leq t^3\sum_{q=0}^3{3\choose q}H_qW_{3-q}.            \tag{4.17}
\]

There are \(t\) local defects.  Equations (4.11) and (4.17) prove
(4.3). \(\square\)

## 5. Width first, then the local estimate

Lemma 2.1 takes the actual finite-width network to its operator state at
each fixed nonzero schedule.  Only now apply Lemma 4.1, directly in the
width-first Banach space \(\mathcal X_L\), with

\[
                         f=\mathcal F,\qquad g=\mathcal G,
                         \qquad x_0=\theta_0.            \tag{5.1}
\]

The hypotheses are exactly (2.20).  Hence for \(|h|\leq c_L/t\),

\[
 D_{t,L}(h)=h^2Q_{t,L}(h),\qquad
 \sup_{|h|\leq c_L/t}|Q_{t,L}^{(3)}(h)|\leq6C_Lt^4.     \tag{5.2}
\]

At every finite width, simultaneously sending

\[
                         h\mapsto-h,\qquad a^0\mapsto-a^0              \tag{5.3}
\]

leaves every forward field and trained matrix fixed, negates every
cotangent and the output, and preserves the Gaussian initialization law.
Thus every finite-width expected output is odd in \(h\).  Its pointwise
fixed-\(h\) width limit is odd as well.  Consequently \(D_{t,L}\) and,
by (5.2), \(Q_{t,L}\) are odd.

Put \(\kappa_{t,L}=Q_{t,L}'(0)\).  Taylor's integral formula for the odd
\(C^3\) function \(Q_{t,L}\) gives

\[
\begin{aligned}
 |D_{t,L}(h)-\kappa_{t,L}h^3|
 &=|h|^2\left|Q_{t,L}(h)-hQ_{t,L}'(0)\right|\\
 &\leq {|h|^5\over6}
       \sup_{|s|\leq|h|}|Q_{t,L}^{(3)}(s)|\\
 &\leq C_Lt^4|h|^5.                                   \tag{5.4}
\end{aligned}
\]

This proves the remainder after the width limit has already been
identified.  There is no finite-width Taylor expansion and no
width/step derivative interchange.

## 6. Explicit activation coefficient

The independently proved singular Gaussian cubic recursion for the
width-first DAG
(temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md, (1.6) and (9.4))
gives, for the identity activation,

\[
 J_{x,L}={2L(L+1)^2(L+2)\over3},
 \qquad
 \kappa_{t,L}=-{t(2t-1)\over2}J_{x,L}.                 \tag{6.5}
\]

The nine activation integrals reduce here to

\[
 d=u=\ell=1,qquad v=m=r=s=j=e=0,                       \tag{6.6}
\]

and the finite forward/reverse recursion gives (6.5) directly.  Equation
(5.4) also implies \(D_{t,L}(h)/h^3\to\kappa_{t,L}\), so the coefficient
is unique.  Thus (6.5) identifies the coefficient produced by the
already width-first operator curve; it does not import an initialization
derivative through the opposite limit order.  Combining (5.4)--(6.5)
proves Theorem 1.1.

## 7. Dyadic consequence

Set

\[
 G_m(T)=F_{m,L}(T/m),\qquad m=1,2,4,\ldots .             \tag{7.1}
\]

In Theorem 1.1 put \(t=m\) and \(h=T/(2m)\).  For \(|T|\leq2c_L\),

\[
 \begin{aligned}
 |G_m(T)-G_{2m}(T)|
 &\leq {L(L+1)^2(L+2)\over3}
       {m(2m-1)|T|^3\over8m^3}
       +{C_L|T|^5\over32m}\\
 &\leq {1\over m}\left\{
 {L(L+1)^2(L+2)\over12}|T|^3
 +{C_L\over32}|T|^5\right\}.                         \tag{7.2}
 \end{aligned}
\]

The right-hand side is summable over dyadic \(m\).  Hence the
width-first expected Euler outputs converge uniformly on
\([-2c_L,2c_L]\) along dyadic meshes.  Because each \(G_m\) is the
polynomial operator iterate in Lemma 2.1, it is continuous, and hence the
limit is continuous.  This is a scalar width-first continuous-time
limit; identifying it with an actual finite-width continuous gradient
flow still requires a separate dimension-free exact-flow/Euler bridge.

## 8. Independent coefficient check at \(L=2\)

The direct identity-activation compiler, which does not use the Banach
majorant above, gives

\[
 [h^5]D_{t,2}(h)
 =-{2452\over3}t^4+1896t^3-{4403\over3}t^2+369t.        \tag{8.1}
\]

Thus the canonical fifth coefficient is genuinely quartic and has
nonzero leading term.  This independently confirms both that the
\(t^4\) power in (1.8) is attainable and that one cannot generally seek
an \(o(t^4)\) replacement.

## 9. Adversarial boundary: why the nonlinear case remains open

The proof closes because every activation derivative of order at least
two vanishes.  In the trace-class state norm (2.4), all generated maps
are then built only from bounded operator products and the rank-one
operation (2.9).  Aggregate transpose response is already present in the
same multilinear state: it is the fixed-adjoint action
\(a\mapsto W_2(\theta)^*\cdots W_L(\theta)^*a\), not a separately
estimated list of response coordinates.  This is the promised closure
under reused-matrix adjoint response.

For a genuinely nonlinear \(\phi\), the second state derivative contains
coordinatewise products such as

\[
                         \phi''(z)vw.                  \tag{8.1}
\]

Normalized \(\ell^2\) does not make pointwise multiplication a bounded
bilinear map: with \(v=\sqrt n\,e_1\), one has \(|v|_n=1\) but
\(|v^2|_n=\sqrt n\).  Adding an \(\ell^\infty\) norm is not dimension
free under Gaussian initialization, since the Gaussian maximum grows as
\(\sqrt{\log n}\).  Finite polynomial/Hermite chaos does not repair this
for a fixed nonlinear degree: repeated Euler composition increases the
chaos degree with the horizon, so bare hypercontractivity gives constants
that grow with \(t\), rather than with total step variation.

Therefore this note proves the canonical \(O(t^4)\) bound for the closed
identity subclass, including \(L=2\) and \(L=3\), but it does not prove
the same theorem for nonlinear activations.  A nonlinear extension still
needs a genuinely generated-core estimate controlling (8.1) and its
aggregate adjoint images by total step variation, not by history length.
