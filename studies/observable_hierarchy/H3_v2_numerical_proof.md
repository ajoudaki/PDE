# Numerical consistency of finite observable population dynamics

Fix \(T=1/200\), write \(u=x/\sqrt2\in S^1\), and fix one represented
law \(\mu=\mathrm{ArcLaw}(\omega,a,b,c,d)\). Its rational parameters satisfy
\(1/3\le\omega\le2/3\), \(-1/20\le a\le b\le1/20\), and
\(-1/20\le c\le d\le1/20\). The first component has mass \(\omega\),
label \(+1\), and direction
\[
 U(s)=((1-s^2)/(1+s^2),2s/(1+s^2)),\qquad s\sim\mathrm{Unif}[a,b].
\]
The second has mass \(1-\omega\), label \(-1\), and direction \(RU(s)\)
with \(s\sim\mathrm{Unif}[c,d]\), where
\(R=\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\).
A degenerate interval denotes an atom. The family contains nonorthogonal
atomic and nonatomic laws, with exact finite input descriptions.

The short-time existence proposition supplies its unique canonical strong
Gaussian population gradient flow through \(T\), and identifies that flow
with the actual finite-network gradient-flow limit. The fixed conventions
are the bias-free two-hidden-layer tanh model, mobilities \((n,1,n)\),
unhalved squared loss, and physical time.

## 1. Finite equations and assertion

At order \(N\ge1\), retain all total-degree-at-most-\(N\) Chebyshev products
in the lower coordinates
\[
 (\tanh g_1,\tanh g_2,\tanh p_1,\tanh p_2),\qquad
 p_i=A_0^*\tanh(A_0\tanh g_i),
\]
and the upper coordinates \((\tanh\xi_1,\tanh\xi_2)\),
\(\xi_i=A_0\tanh g_i\). Append every bounded valid initialized-word code
through \(N\) not already present literally, in the exact coding and order
of the dense-closure proposition. Word scalars and envelopes are exact
rationals; there is no empirical-rank test. Denote the raw columns by
\(\psi_\ell\), their lengths by \(d_\ell\), and set
\[
 \eta_N=\frac1{1024(N+1)^2},\quad G_\ell=E[\psi_\ell\psi_\ell^T],
 \quad L_\ell L_\ell^T=G_\ell+\eta_NI,\quad
 b_\ell=L_\ell^{-1}\psi_\ell,\quad
 D=L_2^{-1}CL_1^{-T},\quad C=E_2[\psi_2(A_0\psi_1)^T].       \tag{1}
\]
The joint marks are \(\lambda_1=\operatorname{Law}(b_1,g)\) and
\(\lambda_2=\operatorname{Law}(b_2)\). With \(w(0)=g,c(0)=0,M(0)=D\), put
\[
\begin{aligned}
 h_1(u)&=\tanh(w\cdot u),&a(u)&=E_1[b_1h_1(u)],\\
 h_2(u)&=\tanh(b_2^TMa(u)),&f(u)&=E_2[ch_2(u)],\\
 d(u)&=E_2[b_2c(1-h_2(u)^2)],&q(u)&=b_1^TM^Td(u).
\end{aligned}
\]
For \(r(u,y)=f(u)-y\), the finite equations are
\[
 \dot w=-2\int r(1-h_1^2)q\,u\,d\mu,\qquad
 \dot c=-2\int rh_2\,d\mu,\qquad
 \dot M=-2\int rda^T\,d\mu.                                \tag{2}
\]
These are exactly the contractions in the implementation. Both action
orientations use the one evolving \(M\) and its actual transpose.

The independent numerical parameters are as follows. A positive rational
\(\varepsilon\) adds \(\varepsilon I\) to generic source Grams; \(Q\)
Halton points compute initializer coefficients, Grams and \(C\); \(P\)
points replay the resulting complete joint mark laws with those coefficients
frozen. The two-arc midpoint rule has at most \(A=2m\) data points. Explicit
Heun uses \(J\) steps of intended length \(h=T/J\). Linear interpolation
of successive states defines all intermediate times; nonlinear activations
are evaluated on that state. The rational backend has precision \(p\ge20\)
and grid \(10^{-p}\mathbb Z\). All law parameters, \(\varepsilon\), and
the intended step are declared exactly. Resource allowances are adjustable
and must admit each requested finite computation.

**Theorem.** For every fixed represented law, \(N,\varepsilon,Q,P,m,J\),
the rational implementation, with adequate resource allowances, succeeds
for all sufficiently large \(p\) and converges to the corresponding exact
finite computation. Successive limits
\[
 p\to\infty,\quad J\to\infty,\quad m\to\infty,\quad
 P\to\infty,\quad Q\to\infty,\quad\varepsilon\downarrow0       \tag{3}
\]
give (1)–(2). The outer limit \(N\to\infty\) gives the canonical flow
through the same fixed \(T\). Convergence includes predictions uniformly
in \(t\in[0,T]\) and \(u\in S^1\), and, uniformly in time, the laws
\[
 \mathcal P_\ell(t)
 =\operatorname{Law}_{\lambda_\ell\otimes\mu}
       (h_\ell(0,u),h_\ell(t,u))                            \tag{4}
\]
in \(W_2\), and their RMS displacements
\[
 R_\ell(t)=\left(\int|z_2-z_1|^2\,d\mathcal P_\ell(t)(z)\right)^{1/2}.
                                                                  \tag{5}
\]
The upper initial coordinate uses the same \(g,b_1,b_2,D\) as the current
coordinate. At finite precision, normalize returned nonnegative product
weights only when interpreting (4) as a probability law; their total
mass tends to one in the first limit. The reported RMS, which uses the
actual returned weights, has the same limit. No vector-field weights
are changed by this convention.

Thus the limiting error is zero in the nested order
\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
 \lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}\lim_{p\to\infty}.
                                                                  \tag{6}
\]
Each intermediate target exists in the stated observation metrics. The
\(\varepsilon\) limit is vacuous for the core implementation. This is
an iterated assertion: it gives neither an arbitrary diagonal nor a
universal computable tolerance schedule, affordable computation at every
order, or a broader family/horizon. The unbounded precision statement
uses the integer/rational backend; float64 and Decimal are additional
executable options.

## 2. Gaussian integration and adaptive initialization

We include the integration facts needed for adaptively chosen finite
coefficients. For the base-\(b\) radical inverse \(U_{k,b}\) of
\(1\le k\le Q\),
\[
 \frac1{bQ}\le U_{k,b}\le1-\frac1{bQ},\qquad
 D_{Q,b}\le\frac{1+(b-1)(\lfloor\log_bQ\rfloor+1)}Q.         \tag{7}
\]
An index has at most \(\lfloor\log_bQ\rfloor+1\) digits, giving the endpoint
bounds. Split \(0\le k<Q\) into base-\(b\) aligned blocks: there are
at most \((b-1)(\lfloor\log_bQ\rfloor+1)\) blocks, and a block of length
\(b^j\) has one point in each interval of length \(b^{-j}\), with
unnormalized interval discrepancy at most one. Replacing its index zero
by index \(Q\) changes any interval count by at most one, proving (7).
For distinct prime bases, fixing leading digit strings fixes residues
modulo coprime prime powers. The Chinese remainder bijection gives one
residue modulo their product and frequency error at most \(1/Q\).
Approximating rectangles by digit cylinders proves joint equidistribution.

Write \(X_k=-\log U_{k,b}\), \(M_Q=\log(bQ)\). Layer cake gives, for \(r>0\),
\[
 Q^{-1}\sum_{k\le Q}X_k^r1_{X_k>L}
 \le I_r(L)+D_{Q,b}M_Q^r,\quad
 I_r(L)=L^re^{-L}+\int_L^\infty rt^{r-1}e^{-t}\,dt.          \tag{8}
\]
When \(M_Q\le L\) the left side is zero. Otherwise, using
\(D_{Q,b}\le b\log(bQ)/(Q\log b)\), it is at most
\[
 I_r(L)+(b^2/\log b)L^{r+1}e^{-L}\quad(L\ge r+1),
\]
because \(z^{r+1}e^{-z}\) decreases there. This is uniform in \(Q\).
Pairwise Box–Muller pushes uniform Lebesgue measure to the joint standard
Gaussian, by the polar change of variables. Its singular endpoints have
measure zero, so truncation away from them proves weak convergence of
its Halton rules. With \(s\) pairs, their output satisfies
\[
 |z|^r1_{|z|>R}\le(2s)^{r/2}
       \sum_{j=1}^s X_j^{r/2}1_{X_j>R^2/(2s)},             \tag{9}
\]
since \(|z|^2\le2s\max_jX_j\). Hence all polynomial moments and their
uniform tails converge. Weak convergence and these tails imply \(W_r\)
convergence for every finite \(r\ge1\): couple common masses in small
cells of a bounded box with Gaussian-null boundaries; bound the remaining
transport by tail \(r\)-moments; enlarge the box and shrink the cells.

If \(\theta_Q\to\theta\) is a finite coefficient vector, and
\(F(\theta,z)\) is continuous with a common bound \(C(1+|z|^k)\) for
\(\theta\) near its limit, then
\[
 Q^{-1}\sum_{j\le Q}F(\theta_Q,z_j)\longrightarrow EF(\theta,Z). \tag{10}
\]
On a ball this follows from uniform continuity and weak convergence;
off it use a moment larger than \(k\) in (9). Applied to joint maps,
the same argument gives their \(W_r\) convergence when the required
moments are bounded. Crucially, \(\theta_Q\) may have been computed using
earlier integrals on the same cloud.

The generic compiler processes the complete typed union of retained words,
forward actions on each lower word, reverse actions on each upper word,
and their dependencies. Each literal action has a named source. Literal
duplicates share a node; empirical equality never identifies nodes. Each
population uses one joint Gaussian cloud, on separate probability spaces.
When a new action operand is \(v\), its source cross covariance with an
older operand \(v_j\) is \(E_Q[vv_j]\), and its variance is
\(E_Q[v^2]+\varepsilon\). Every older operand table and old Cholesky row
is preserved. Thus the entire covariance prefix is exactly its empirical
operand Gram plus \(\varepsilon I\), which is positive definite even
for dependent or zero operands. Appending one Cholesky row realizes the
new joint Gaussian without replacing old values.

An action equals its named Gaussian source plus
\(\sum_j E_Q[\partial_jv]v_j\) over old opposite-orientation actions.
The derivative is that of the explicit expression in named sources,
with covariance and response coefficients frozen. At an action the
reverse traversal adds its direct source derivative and propagates
through frozen response links. It does not differentiate the
opposite-population graph operand, Gaussian roots or estimated coefficients.
Coordinate nodes obey the usual chain/product rules. This is the formal
AD rule of the canonical finite Gaussian program, including nested responses.

Induct over the finite causal ordering. Each value and formal derivative
is continuous in finitely many Gaussian coordinates and earlier
coefficients, with a uniform polynomial Gaussian envelope on compact
coefficient sets. Bounded gates and derivatives, finite products and
response sums preserve these properties. Equation (10) applies to every
new coefficient/covariance. For fixed positive \(\varepsilon\), Cholesky
is continuous at every positive definite prefix. This proves convergence
as \(Q\to\infty\) of all coefficients, joint outputs, raw Grams and
the forward contraction \(C\). The reverse contraction is a diagnostic
from the same full program; it is not substituted into the dynamics.

For fixed \(Q,\varepsilon\), replay on \(P\) points uses exactly these
frozen factors and coefficients. It refits none of them. Equation (10)
therefore gives joint \(W_2\) convergence as \(P\to\infty\), including
the retained \(g\) coordinate. Reusing the existing cloud at \(P=Q\)
is the same rule and changes no limit.

After \(Q\to\infty\), remove \(\varepsilon\). Induct over the sources
again. New coefficients and covariances are expectations of continuous,
polynomially bounded functions of preceding jointly Gaussian sources.
Represent each complete source vector by its covariance's positive
semidefinite square root times a standard Gaussian. Such square roots
are continuous: every subsequence has a convergent subsubsequence of
bounded positive square roots; its limit squares to the limiting matrix,
and uniqueness identifies that limit. The uniform moment argument proves
continuity of all new expectations. This coupling is for the proof only;
it leaves all named sources and formal derivatives intact. Consequently
the limit is the canonical source recursion even for singular covariances.
Neither continuity of singular Cholesky factors nor deletion of a
zero-variance derivative slot is assumed.

The core calculation has the same limiting contractions. Set
\[
 v=E\tanh^2G>0,\quad \tau=E\tanh^2(\sqrt vG)>0,\quad
 \alpha=E[1-\tanh^2(\sqrt vG)]>0.
\]
Its lower joint law is \(g\sim N(0,I_2)\),
\(p=\sqrt\tau Z+\alpha\tanh g\), with \(Z\) independent, and its upper
law is \(\xi\sim N(0,vI_2)\). For bounded retained smooth functions
\(F(g,p),B(\xi)\),
\[
 E_2[BA_0F]=
 \sum_i E_1[F\tanh g_i]E_2[\partial_{\xi_i}B]
 +\sum_i E_1[\partial_{\zeta_i}F]E_2[B\tanh\xi_i],\quad
 \zeta=\sqrt\tau Z.                                      \tag{11}
\]
Append \(A_0F\) in the full source rule: its response gives the second
term, while its centered source has covariance \(E_1[F\tanh g_i]\)
with \(\xi_i\). Subtract Gaussian regression on \(\xi\); the remainder
is centered and independent of \(B\). Integration by parts
\(E[B\xi_i]=vE[\partial_{\xi_i}B]\) proves the first term. Boundedness
of \(B\) and its fixed-word derivatives justifies the Gaussian boundary
limit. This integrates out an innovation in one contraction without
replacing a joint action law.

The code computes both terms of (11), with the chain factors
\(1-\tanh^2p_i\) and \(1-\tanh^2\xi_i\). Its finite \(Q\) versions of
\(v,\tau,\alpha\) are strictly positive: the first Halton Gaussian
coordinate is nonzero, and exact finite \(\operatorname{sech}^2\) is
positive. Equation (10) proves their convergence, that of (11), and
that of the raw Grams. A tail using only these core actions uses the
same coordinates and derivatives; any new action triggers the generic
compiler. Source regularization is unused in the core calculation.

Each raw retained coordinate has a deterministic finite bound \(B_{\ell,j}\).
Chebyshev products have bound one, from \(T_k(\cos\theta)=\cos(k\theta)\).
Let \(B_\ell^2=\sum_jB_{\ell,j}^2\). For exact or empirical raw Grams,
\[
 |b_\ell|\le B_\ell/\sqrt{\eta_N}=:K_\ell,                 \tag{12}
\]
since \(L_\ell L_\ell^T\ge\eta_NI\). Ridge normalization is continuous
at fixed \(N\). The three transposes in (1) agree with inverse-lower
Cholesky normalization in the code. Every successive joint mark law
therefore converges in \(W_2\), and \(D\) converges in Frobenius norm.
The relevant \(D\)'s and second moments of \(g\) are bounded along
each such convergence. No contraction property of empirical marks
is needed for the next argument.

## 3. Fixed-dimensional existence and stability

Consider any probability mark laws with \(|b_\ell|\le K_\ell\),
\(E|g|^2<\infty\), and finite \(D\), and data with \(|y|\le1\).
On the Banach space of bounded increments \(w-g\), bounded \(c\), and
finite \(M\), (2) is locally Lipschitz: gates have bounded derivatives,
input norms are one, and other operations are bounded integrals and
finite products. The unbounded fixed \(g\) appears only inside gates.
Picard iteration is therefore a contraction on a sufficiently small
closed time-space ball and gives a unique local solution.

For \(\mathcal L=\int(f-y)^2d\mu\), differentiation under the bounded
integrals gives
\[
 \dot{\mathcal L}=-\|\dot w\|_2^2-\|\dot c\|_2^2-\|\dot M\|_F^2,
 \qquad\mathcal L(0)\le1.
\]
Indeed the negatives of (2) are respectively its population \(L^2\),
population \(L^2\), and Frobenius gradients. Thus \(\int|r|d\mu\le1\),
and
\[
 \|c(t)\|_\infty\le2t,\quad |a|\le K_1,\quad |d|\le2K_2t,\quad
 \|M(t)-D\|_F\le2K_1K_2t^2,\quad
 \|\dot w(t)\|_\infty\le4K_1K_2t\|M(t)\|_F.                \tag{13}
\]
These bounds prevent escape from a bounded Banach ball on \([0,T]\).
Local continuation gives existence and uniqueness there for general
or atomic mark laws, and an autonomous solution map.

Couple two lower joint laws and two upper mark laws. On these couplings,
define
\[
 e=\|w-\widetilde w\|_2+\|c-\widetilde c\|_2
                         +\|M-\widetilde M\|_F,\qquad
 \rho_b=\|b_1-\widetilde b_1\|_2+\|b_2-\widetilde b_2\|_2.
\]
For the same \(u\),
\[
 |a-\widetilde a|\le\|b_1-\widetilde b_1\|_2+
                                      K_1\|w-\widetilde w\|_2.
\]
Splitting the three factors of \(b_2^TMa\), then the factors of \(f,d,q\),
and using (13), bounds
\(\|h_2-\widetilde h_2\|_2,|f-\widetilde f|,|d-\widetilde d|,
\|q-\widetilde q\|_2\) by \(C(e+\rho_b)\). In particular the lower
gate product is controlled by
\[
 \|(h_1^2-\widetilde h_1^2)\widetilde q\|_2
 \le2\|\widetilde q\|_\infty\|w-\widetilde w\|_2,
\]
and the multiplier is bounded by (12)–(13).
For distinct directions,
\(\|h_1(u)-h_1(v)\|_2\le\|w\|_2|u-v|\); all other fields inherit a
bound \(C|u-v|\). Labels enter affinely, and the explicit \(u\) factor
is Lipschitz. Integrating a coupling of the data therefore bounds
the drift change by \(CW_1(\mu,\widetilde\mu)\). All constants use
only common \(K_\ell,\|D\|_F,\|g\|_2,T\) bounds. Subtracting (2),
integrating and summing the geometric series for its integral
inequality gives
\[
 \sup_{t\le T}e(t)\le e^{CT}
 \bigl(\|g-\widetilde g\|_2+\|D-\widetilde D\|_F+
              CT[\rho_b+W_1(\mu,\widetilde\mu)]\bigr).      \tag{14}
\]
This verifies both the existence and the stability hypotheses needed
by every numerical mark-law limit.

For the arc midpoint rule, mean parameter error is at most interval
length divided by \(4m\). Since \(|U'(s)|=2/(1+s^2)\le2\), mean direction
error is at most \(1/(20m)\). Couple mixture components identically;
labels then agree, and degenerate intervals have zero error.
The data rules converge in \(W_1\). Equation (14) first removes \(m\),
then \(P\), then the initializer errors \(Q,\varepsilon\) proved above.

## 4. Time and arithmetic limits

Fix \(N,\varepsilon,Q,P,m\) and first use exact arithmetic. The finite
ODE is smooth. Its Heun nodes and stages are bounded independently of
\(J\), without assuming a discrete energy inequality. Set
\(B_k=1+\|c_k\|_\infty\). Since \(|f-y|\le B_k\), its first stage
satisfies \(B_k^*\le(1+2h)B_k\), and
\[
 B_{k+1}\le(1+2h+2h^2)B_k\le e^{(2+2T)h}B_k.
\]
Thus all stages have bound \(B_*=(1+2T)e^{(2+2T)T}\). Their matrix
velocity is at most \(V_M=2B_*K_1K_2(B_*-1)\), hence
\(\|M\|_F\le\|D\|_F+2TV_M\). Their row velocity is then at most
\(2B_*K_1K_2(\|D\|_F+2TV_M)(B_*-1)\), also bounding \(w-g\).
On a slightly larger bounded set the vector field is Lipschitz.
The exact solution has one-step Euler defect \(O(h^2)\), since its
velocity is Lipschitz in time; Heun differs from Euler by \(O(h^2)\).
Consequently \(e_{k+1}\le(1+Ch)e_k+Ch^2\), and summing gives
\(\max_ke_k\le C_Th\). Linear interpolation adds \(O(h)\).
This proves uniform-time consistency; a stronger order is unnecessary.

Now fix all finite parameters including \(J\) and let \(p\to\infty\).
Put \(\delta=10^{-p}\). The rational backend retains integer units
over scale \(10^p\). Nearest rounding, including negative ties, has
error at most \(\delta/2\). Addition/subtraction of represented
values are exact; multiplication and division round once. These
operations are locally uniformly consistent, with a nonzero
denominator margin for division. Integer powers terminate by repeated
squaring. Integer square root has error less than \(\delta\);
consistency at zero uses
\(|\sqrt x-\sqrt y|\le\sqrt{|x-y|}\).

The elementary functions are finite algorithms. Exact power-of-two
reduction puts a positive logarithm argument in \([1,2)\). Its series
\(2\sum_{k\ge0}z^{2k+1}/(2k+1)\), \(0\le z\le1/3\), has a geometric
tail; the implemented tolerances give total log error at most
\(\delta/2+\delta/(4\cdot10^5)\), including the multiple of \(\log2\).
For exponential, reduce \(|x|/2^s\le1/2\), sum Taylor terms, and square
exactly. The amplification of the omitted tail is at most
\(2^se^{2|x|}\); the guard \(\lceil2|x|\rceil+s+5\) decimal places
dominates it. The pre-rounding error is at most \(10^{-5}\delta\).
Reciprocation for negative arguments cannot amplify the discrepancy
because both positive exponentials are at least one.

Pi is computed by the alternating series for
\(16\arctan(1/5)-4\arctan(1/239)\); the tangent addition identity
identifies pi, and the error is at most \(20\,10^{-p-5}\).
Exact rational reduction modulo its computed \(2\pi\) places trig
arguments inside \((-16/5,16/5)\). After the first generated term,
Taylor terms decrease absolutely, so the alternating tail at stopping
is at most \(10^{-p-5}\). With pi computed at precision \(p+5\),
the sine/cosine error on \(|x|\le M\) is at most
\[
 \delta/2+10^{-p-5}+40(M/6+1)10^{-p-10}.                  \tag{15}
\]
Periodicity handles changes in the reduction quotient. Tanh uses
\(e=e^{-2|x|}\), \(\pm(1-e)/(1+e)\), with denominator at least one.
Thus every elementary routine terminates and is locally uniformly
consistent on its continuous domain.

For fixed finite Gaussian clouds, exact Halton uniforms are strictly
between zero and one and eventually round positive. If the rounded
uniform is below one, it is at most \(1-\delta\); the log bound above
ensures a negative computed logarithm. If it rounds to one, its
radius is zero. All Box–Muller points eventually exist and converge.
Every exact source Gram plus \(\varepsilon I\) and feature Gram plus
\(\eta_N I\) is positive definite. Induction over finite Cholesky
operations proves convergence, and each exact positive pivot supplies
a margin ensuring eventual success. The core variances/response
have the same strict-margin property. Matrix inputs in this pipeline
are already converted to the chosen arithmetic, as required by the
Cholesky helper.

Dictionary decisions use exact words/rationals. Skipping a numerically
zero response coefficient is equivalent to multiplying by zero, so
it preserves consistency even at a limiting zero. Weight rounding
has total error at most the number of weights times \(\delta/2\);
validators permit that number times \(10^5\delta\). Each exact arc
coordinate rounds with error at most \(\delta/2\), so two squarings
and addition perturb its unit squared norm by less than \(4\delta\),
inside the \(10^5\delta\) allowance. Repeated validation does not
renormalize the data. Thus the shrinking-tolerance validation checks
also eventually pass; continuity alone would not establish this.

All remaining fixed computations are finite compositions of these
consistent operations. Induction proves convergence of the state
and observations at each of the finitely many steps. It is uniform
over input direction and interpolation fraction: their domains
are compact, intermediate values bounded, and primitive convergence
locally uniform. For evaluating all \(u\in S^1\), take their directly
rounded coordinates; the same unit-norm bound applies. Intended
time \(J(T/J)\) and represented time differ by at most \(J\delta/2\).
This proves the first limit of (3), including eventual precision
success, before removing the time step. It does not cover a diagonal
with positive pivots shrinking faster than precision resolves.

## 5. Observations, composition and own-state restart

Section 3 bounds prediction errors and both current activation errors
in \(L^2\), uniformly in \(u,t\), by \(C(e+\rho_b)\).
Initial lower error is at most \(\|g-\widetilde g\|_2\), and initial
upper error has the same product bound with \(M=D,w=g\).
Keeping both coordinates on the same mark coupling therefore proves
joint-pair \(W_2\) convergence. For data-law changes the additional
squared transport cost is at most \(CE|u-v|^2\le C'E|u-v|\), by the
input estimates and bounded circle diameter. This proves convergence
of the training averages in (4); \(u,y\) may also be retained in the
coupled law. The reverse triangle inequality in \(L^2\) bounds the
change of (5) by the \(L^2\) error of its displacement coordinate.
Rounded RMS converges too, by square-root continuity including zero.

Sections 2–4 remove every inner error in (6). The dense-closure
proposition supplies the final outer limit for exactly (1): its
positive filters converge strongly to identity, both directions of
\(Q_{2,N}A_0Q_{1,N}\) converge strongly, and projected middle
Hilbert–Schmidt sources converge on the exact trajectory's compact
targets. The short-time proposition supplies the strong reference
and Gaussian reverse-query tails. Their one-reference comparison
therefore gives strong trajectory convergence and precisely these
uniform-circle, pair-law and RMS observations. The family, horizon,
dictionary, ridge and GF conventions agree, proving (6).

The equations are autonomous. A checkpoint stores
\(b_1,g,w,p_1,b_2,c,p_2,M,D\), finite data and arithmetic metadata.
Rational values use hexadecimal integer units and precision;
Decimal uses exact strings and float64 hexadecimal values. Loading
recovers the same working values and validates without changing
weights. Thus, at a step endpoint, identical arithmetic, data,
step sizes and block size reproduce the same subsequent working
states. No source tape, clock, previous velocity or growing history
enters the step map. The limiting population solution has its own
restart property by uniqueness in Section 3; (14), with restart
state error included in \(e(0)\), proves convergence to that restart.
Interpolating an interior observation does not assert that a fresh
Heun mesh from that time equals the previous finite mesh.

## 6. Work, storage and scalar bits

The following bounds count scalar operations; scalar bit cost is
additional. With equal population counts \(P\), the retained state
contains
\[
 S=P(d_1+d_2+7)+2d_1d_2                                  \tag{16}
\]
scalars, and data contain \(4A\). Metadata and exact input/syntax
descriptions have additional finite bit size. Each retained pair
array has \(2PA\) scalars; the streamed RMS option avoids those arrays.
The coefficient-first products \(b_2(Ma)\), \(b_1(M^Td)\), and
\(b_2(Da_0)\) give right-side work
\[
 O\bigl(A[P(d_1+d_2+1)+d_1d_2]+S+A\bigr).                 \tag{17}
\]
Heun multiplies this by \(O(J)\). At block size \(B\le A\), workspace is
\[
 O(S+A+PB+B(d_1+d_2)+d_1d_2).                             \tag{18}
\]
A constant number of stages or endpoints changes only the constant;
memory need not grow with elapsed steps. Forward prediction on \(V\)
directions has the corresponding forward-only cost with \(A=V\).
A finite panel is not a certificate for a continuum supremum.

Let \(K\) be the full typed compiler DAG node count, \(s\) its number
of named sources, and \(d=d_1+d_2\). At most \(E=2K+s^2\) coordinate
and response edges occur. A conservative generic initializer work bound is
\[
 O\bigl(QsE+Qs^2+s^3+(Q+P)E+(Q+P)d^2+d^3\bigr),           \tag{19}
\]
plus generation of finitely many prime bases and
\(O((Q+P)(s+2)\log(Q+P+1))\) digit operations and elementary Gaussian
transforms. Each AD walk visits at most \(E\) edges on \(Q\) entries,
at most \(s\) times; pair covariances, new Cholesky rows, replay,
Grams, contractions and normalization give the other terms.
Its workspace is \(O((Q+P)(K+s+d)+s^2+d^2)\) scalars.
The core has fixed Gaussian dimensions four and two, work
\(O((Q+P)(N+1)d+(Q+P)d^2+d^3)\), and workspace
\(O((Q+P)(d+N+1)+d^2)\). Releasing coefficient tables before replay
improves constants.

Exact word construction adds finite integer/DAG work. Every natural
code has strictly smaller dependency codes, so the iterative decoder
terminates. Cached child hashes and iterative syntax equality avoid
expanding shared polynomial trees. Prefix memoization uses
\(O(N+K)\) syntax nodes, with exact scalar/envelope bit sizes counted.
Syntax caches can persist between initializer calls; they are not
source coefficient tables or training history. The small recursive
core-tail evaluator does not impose an order ceiling: code
\(62=\tanh(A_0 1)\) already introduces a non-core action, after
which the dispatch uses the iterative full compiler.

For a retained rational scalar bounded by \(M_*\), the maximum units
and scale bit size is
\[
 \beta=O(p+\log(1+M_*)).                                 \tag{20}
\]
Thus retained numerical storage is \(O((S+A)\beta)\) bits plus
metadata. Workspace scalar counts above likewise require their
maximum scalar bit size. Gaussian endpoint bounds give
\(|z|\le C_s\sqrt{\log(b_{\max}\max(P,Q))}\); finite coefficient
induction, bounded marks and (13) bound remaining magnitudes.
At fixed outer parameters they are uniform for sufficiently large
precision. The retained-byte diagnostic includes rational units
and scales; it is not a process-wide peak memory measurement.

Basic-operation work must be weighted by integer arithmetic cost.
Elementary calls additionally hold exact temporary Fractions. On
fixed bounded operand sets, away from zero for logarithm/division,
a conservative bound is \(O(p^2\log(p+2))\) bits per temporary rational
and \(O(p)\) series iterations, with operand-dependent constants.
For log/exp, term denominators divide a power of one \(O(p)\)-bit
base denominator times the product of \(O(p)\) small integer factors;
the common denominator therefore has \(O(p^2+p\log(p+2))\) bits.
The computed pi has \(O(p\log(p+2))\) denominator bits; reduction
and \(O(p)\) trig powers enlarge this to \(O(p^2\log(p+2))\).
Geometric and Taylor tails give \(O(p)\) iterations.
Exact squaring has a fixed operand-dependent
number of stages. Weighting (17)–(19) by these integer costs and
adding temporary Fraction storage yields finite bit-work/space
bounds. Large operands can make the constants large.
API byte/work estimates are adjustable resource guards, not certified
peak-bit bounds, and must grow as required along all refinements,
including precision. There is no fixed precision ceiling in the
integer/rational algorithm under the usual unbounded-resource
interpretation of these finite computations.

This proves all stated numerical limits and resource assertions.

---

## Author provenance and dependency boundary

This is an internally checked author proof candidate, not an independent
promotion review or established addition. No trajectory was generated
for this proof. Dependencies read completely are the short-time
H3_v2_scope_proof.md, the all-moment H3_v2_cubature_proof.md, the complete
H3_v2_basis_synthesis.md, Section 5 of H3_v2_route_basis.md, and the complete
H3_v2_hierarchy_proof.md, with their explicitly scoped maintained-model
and Gaussian-rule dependencies. The full H3_v2_fixed_audit.md supplies
the checked primitive tail constants, whose derivations are included above.
The current guide, corrections, and all six numerical/word sources were
read completely; final source identities are listed below.

Canonical module names must bind to these candidate implementations
before this proof is attributed to an executable package. A package
name alone does not identify its source. The study loader supplies
that binding. The outer mathematical implication uses the dense-closure
and short-time propositions with their stated hypotheses; promotion
status remains separate from this author proof.

Frozen numerical-source SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| H3_v2_fixed.py | 75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225 |
| H3_v2_arithmetic.py | 2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb |
| H3_v2_words.py | b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5 |
| H3_v2_initialization.py | 6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2 |
| H3_v2_compiler.py | 1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac |
| H3_v2_solver.py | 711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605 |
