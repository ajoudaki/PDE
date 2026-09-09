## 9. Finite loss-GD pullback calculus

This section concerns a finite-dimensional Euler map at a supplied
state. It complements the moving continuous-flow jets and the fixed-program
Gaussian feature-ascent theorem: here the scalar residual is recomputed in
every raw loss-GD update. The result requires no initialization distribution,
Gaussian parity, population metric, or width-limit identification.

### 9.1. Raw mobilities, full square loss, and the Euler map

Flatten the finite stored parameters into a Euclidean vector \(\theta\).
Let \(D\) be a fixed positive-definite symmetric mobility matrix. For the
canonical width-\(n\), depth-\(L\) network, its blocks are
\[
 D=\operatorname{diag}
 (n\kappa_1 I,\kappa_2 I,\ldots,\kappa_L I,
                      n\kappa_{L+1}I),                 \tag{9.P1}
\]
with identities of the corresponding flattened block sizes. These are
ordinary Euclidean/Frobenius coordinates and the actual raw mobilities.
Put \(x=D^{-1/2}\theta\), and write the predictor in these coordinates as
\(f(x):=f_n(D^{1/2}x)\). This notation is restricted to this section.
For one sample with arbitrary label \(y\), use exactly the shared convention
\[
 r(x)=f(x)-y,\qquad \mathcal L(x)=r(x)^2,
 \qquad P(x)=-\mathcal L(x),\qquad v(x)=\nabla P(x).
                                                               \tag{9.P2}
\]
The chain rule gives
\(\nabla_x\mathcal L=D^{1/2}\nabla_\theta\mathcal L_n\).
Consequently the raw update and its coordinate representation are
\[
 \theta^+=\theta-\eta D\nabla_\theta\mathcal L_n,
 \qquad x^+=E_\eta x:=x+\eta v(x),
 \qquad v=-2r\nabla f.                                  \tag{9.P3}
\]
Thus \(\eta\) is the actual loss-GD step, and \(N\) below counts updates;
neither is physical time. The change of coordinates is linear and hence
preserves this exact Euler update. The residual in (9.P3) moves with the state.
The same coordinate argument applies to a fixed-batch mean-square loss
\(m^{-1}\sum_a(f_a-y_a)^2\), with \(P=-\mathcal L\); only the
one-sample specialization below uses the scalar factor in (9.P3).

We first allow any scalar observable \(u\) and vector field \(v\) on an
open subset of a finite-dimensional Euclidean space. Suppose both are
\(C^6\). For a fixed integer \(N\ge1\), choose an interval of steps
containing zero on which all iterates in
\[
 d_N^u(\eta)=u(E_\eta^{2N}x_0)-u(E_{2\eta}^{N}x_0)       \tag{9.P4}
\]
are defined in that open set. Such an interval exists locally for each
fixed \(N\), by continuity and the fact that every zero-step state is
\(x_0\). The paired scalar map is \(C^6\) on this interval by finite
composition. For \(v=\nabla P\), the sufficient hypothesis \(P\in C^7\)
ensures this regularity; the assumption is on the finite function, not on
an unidentified population state.

### 9.2. Exact finite operator words and their coefficient recursion

For an integer \(k\ge1\), define
\[
 \mathcal T_k u(x)=\frac1{k!}D^k u(x)[v(x),\ldots,v(x)].  \tag{9.P5}
\]
The vector \(v(x)\) is held fixed inside the displayed derivative of
\(u\). The resulting function \(\mathcal T_k u\) still depends on the
state; an outer operator differentiates that dependence. For example,
\[
 \mathcal T_1^2u=D^2u[v,v]+Du[Dv\,v],
 \qquad \mathcal T_2u=\tfrac12D^2u[v,v].                \tag{9.P6}
\]
Thus replacing a moving vector field by its initial value would already
lose a term at order two.

For integers \(1\le q\le j\), set
\[
 \mathcal W_{j,q}=
 \sum_{\substack{k_1+\cdots+k_q=j\\ k_i\ge1}}
       \mathcal T_{k_1}\cdots\mathcal T_{k_q},
 \qquad \Lambda_{j,q}=(\mathcal W_{j,q}u)(x_0).          \tag{9.P7}
\]
Products act from right to left. The finite recurrence is
\[
 U_{0,0}=u,\qquad U_{j,0}=0\ (j>0),\qquad
 U_{j,q}=0\ (j<q),
\]
\[
 U_{j,q}=\sum_{k=1}^{j-q+1}\mathcal T_kU_{j-k,q-1},
 \qquad \Lambda_{j,q}=U_{j,q}(x_0).                     \tag{9.P8}
\]
Partitioning the compositions in (9.P7) by their first part proves (9.P8);
every recursive call decreases the total order. This recurrence is a
finite derivative prescription, not a convergent infinite series.

Writing \([\eta^j]\) for the ordinary Taylor coefficient at zero, we have
\[
 [\eta^j]u(E_\eta^M x_0)
       =\sum_{q=1}^j\binom Mq\Lambda_{j,q},
 \qquad j\ge1,                                      \tag{9.P9}
\]
provided \(u,v\in C^j\) near \(x_0\) for that fixed order; the present
\(C^6\) hypotheses cover all orders needed below. Here \(M\) is any
nonnegative integer and \(\binom Mq=0\)
when \(q>M\). At order zero the coefficient is \(u(x_0)\).

To prove (9.P9), let \(\mathcal P_\eta u=u\circ E_\eta\).
The exact operator \(\mathcal B_\eta=\mathcal P_\eta-I\) satisfies
\[
 \mathcal P_\eta^M=(I+\mathcal B_\eta)^M
             =\sum_{q=0}^M\binom Mq\mathcal B_\eta^q.   \tag{9.P10}
\]
This binomial formula uses the single operator \(\mathcal B_\eta\);
it does not assume that different \(\mathcal T_k\)'s commute.
Taylor differentiation of \(u(x+\eta v(x))\) at zero gives
\([\eta^k]\mathcal B_\eta u=\mathcal T_k u\).
At a finite target degree \(j\), apply the product and chain rules to
the finite product in (9.P10): every factor must contribute positive order,
and the choices \(k_1+\cdots+k_q=j\) contribute precisely (9.P7).
No term with \(q>j\) contributes. For \(j\le5\), this operation
differentiates \(u\) at most \(j\) times and \(v\) at most \(j-1\)
times, within the stated regularity. Equivalently one may work with finite
Taylor polynomials modulo degree \(j+1\); no convergent infinite
operator expansion or operator-norm remainder is used. Evaluation at
\(x_0\) proves (9.P9).

Subtracting the coarse update in (9.P4) now gives
\[
 [\eta^j]d_N^u=\sum_{q=1}^jQ_{j,q}(N)\Lambda_{j,q},
 \qquad Q_{j,q}(N)=\binom{2N}q-2^j\binom Nq.          \tag{9.P11}
\]
The zero and first coefficients vanish. Every polynomial \(Q_{j,q}\)
has degree at most \(j-1\): if \(q<j\) this follows from its degree
\(q\), while if \(q=j\) the two leading coefficients are both
\(2^j/j!\) and cancel. This is a term-by-term cancellation and does not
require relations between the \(\Lambda_{j,q}\)'s.

### 9.3. The complete temporal table through degree five

The rows of (9.P11), in increasing \(q\), are
\[
\begin{array}{c|lllll}
j\backslash q&1&2&3&4&5\\ \hline
2&-2N&N\\
3&-6N&-2N^2+3N&2N(N-1)\\
4&-14N&-6N^2+7N&-\frac43N^3+6N^2-\frac{14}3N
 &2N^3-\frac{11}2N^2+\frac72N\\
5&-30N&-14N^2+15N&-4N^3+14N^2-10N
 &-\frac23N^4+6N^3-\frac{77}6N^2+\frac{15}2N
 &\frac43N^4-7N^3+\frac{35}3N^2-6N.
\end{array}                                                   \tag{9.P12}
\]
Each entry is obtained by multiplying the finite factors in
\(\binom Nq=N(N-1)\cdots(N-q+1)/q!\) and applying (9.P11).
Thus (9.P7)--(9.P8) and (9.P12) specify every coefficient through order five,
including every operator ordering, without a stored neural coefficient
table or an unspecified derivative compiler.

Taylor's integral formula yields the exact equality
\[
 d_N^u(\eta)=\sum_{j=2}^5\eta^j
             \sum_{q=1}^jQ_{j,q}(N)\Lambda_{j,q}
 +\frac{\eta^6}{5!}\int_0^1(1-s)^5
                    (d_N^u)^{(6)}(s\eta)\,ds.         \tag{9.P13}
\]
The superscript denotes the sixth derivative of the scalar function with
respect to its own step argument, evaluated at \(s\eta\). The entire
segment between zero and \(\eta\) lies in the chosen step interval,
so the stated \(C^6\) hypothesis verifies the integral formula's
assumption. This is a fixed-\(N\) identity; it supplies no uniform bound
on that derivative as \(N\) grows.

### 9.4. Generic cubic loss formula at arbitrary residual

For \(v=\nabla P\) and \(u=\mathcal L=-P\), put, at \(x_0\),
\[
 b=\nabla P,\quad H_P=\nabla^2P,\quad
 T_P=\langle b,H_Pb\rangle,\quad
 S_P=\|H_Pb\|_2^2,\quad U_P=D^3P[b,b,b].             \tag{9.P14}
\]
Then
\[
 d_N^{\mathcal L}(\eta)
 =-NT_P\eta^2-\frac{N(2N-1)}2(4S_P+U_P)\eta^3
                                  +O_N(\eta^4).       \tag{9.P15}
\]
Here is a direct derivation independent of the temporal table. For a
general \(v,u\), let \(a=Dv\,v\),
\(b_2=Dv(Dv\,v)\), and \(b_3=D^2v[v,v]\), all at \(x_0\).
Insertion of a cubic series in the Euler recurrence gives
\[
 E_\eta^M x_0=x_0+M\eta v+\binom M2\eta^2a
 +\eta^3\left\{\binom M3b_2+
            \frac{M(M-1)(2M-1)}{12}b_3\right\}
 +O_M(\eta^4).                                       \tag{9.P16}
\]
Indeed the quadratic increment at update \(k\) is \(k a\), and
the cubic increment is \(\binom k2 b_2+k^2 b_3/2\).
Summing uses
\(\sum_{k<M}k=\binom M2\),
\(\sum_{k<M}\binom k2=\binom M3\), and
\(\sum_{k<M}k^2/2=M(M-1)(2M-1)/12\). Taylor expansion of
\(u\) along (9.P16) shows that the quadratic paired coefficient is
\(N Du[a]\), and the cubic paired coefficient is
\[
 2N(N-1)Du[b_2]+\frac{N(2N-1)}2Du[b_3]
                       +2N^2D^2u[v,a].                \tag{9.P17}
\]
The terms \(M^2D^2u[v,v]/2\) at order two and
\(M^3D^3u[v,v,v]/6\) at order three cancel at equal elapsed time.
For \(v=\nabla P\), symmetry of \(H_P\) gives, in the order used
in (9.P17),
\[
 Du[a]=-T_P,\quad Du[b_2]=-S_P,\quad
 Du[b_3]=-U_P,\quad D^2u[v,a]=-S_P.
\]
For example \(\langle b,H_P^2b\rangle=\|H_Pb\|_2^2\),
and \(\langle b,D^2(\nabla P)[b,b]\rangle=D^3P[b,b,b]\).
Substitution proves (9.P15).

For the one-sample full square loss in (9.P2), additionally assume that
the predictor \(f\) is \(C^3\) near the supplied state for (9.P18)–(9.P21).
This is separate from the loss-field regularity used for the remainder:
a smooth squared loss alone need not make its predictor \(C^3\). Define
at the same arbitrary state
\[
 g=\nabla f,\quad H_f=\nabla^2f,\quad K=\|g\|_2^2,
 \quad B=\langle g,H_fg\rangle,\quad
 S=\|H_fg\|_2^2,\quad U=D^3f[g,g,g].                 \tag{9.P18}
\]
Since \(P=-r^2\),
\[
 b=-2rg,\qquad H_P=-2g\otimes g-2rH_f,
 \qquad H_Pb=4rK g+4r^2H_fg.
\]
Here \(g\otimes g\) is the ordinary Euclidean outer product on these
finite parameter coordinates. Taking the pairing and squared norm gives
\[
 T_P=-8r^2K^2-8r^3B,\qquad
 S_P=16r^2K^3+32r^3KB+16r^4S.                          \tag{9.P19}
\]
The product rule gives
\[
 D^3P[a_1,a_2,a_3]
 =-2rD^3f[a_1,a_2,a_3]
 -2\sum_{\mathrm{cyc}}Df[a_1]D^2f[a_2,a_3].           \tag{9.P20}
\]
Putting \(a_1=a_2=a_3=-2rg\) yields
\(U_P=16r^4U+48r^3KB\). Therefore
\[
\begin{aligned}
 d_N^{\mathcal L}(\eta)={}&8N(r^2K^2+r^3B)\eta^2\\
 &-8N(2N-1)
       (4r^2K^3+11r^3KB+4r^4S+r^4U)\eta^3
       +O_N(\eta^4).                                  \tag{9.P21}
\end{aligned}
\]
No parity or zero-output assumption was used. If \(r=0\) or \(g=0\)
at the supplied state, \(v=0\) there, every Euler iterate stays there,
and the entire paired difference is zero. For an affine predictor,
\(K\) is constant and \(B=S=U=0\); the exact expression is
\[
 r(x_0)^2\{(1-2K\eta)^{4N}-(1-4K\eta)^{2N}\},
\]
which has precisely the quadratic and cubic coefficients in (9.P21).

### 9.5. A convex-tube bound and the fixed-order boundary

Assume separately that a convex set \(C\) lies in the open domain of
\(C^1\) functions \(v,u\), with
\[
 \|v(x)\|_2\le M_T,\qquad \|Dv(x)\|_{\rm op}\le L_T,
 \qquad \|Du(x)\|_{\rm op}\le R_T\quad(x\in C).       \tag{9.P22}
\]
Take \(\eta\ge0\), \(2N\eta\le T\). Write
\(A=E_\eta^2\), \(B_0=E_{2\eta}\). Require that every composition
of at most \(N\) maps chosen from \(A,B_0\), starting at \(x_0\),
and every intermediate \(E_\eta\) state within such a composition,
lies in \(C\). This explicitly includes both Euler paths and all
hybrid paths used to compare them. Convexity includes the straight
segments needed for the derivative estimates; endpoint bounds on just two
paths would not suffice.

For such a starting state, the exact local defect is
\[
 Ax-B_0x=\eta\{v(x+\eta v(x))-v(x)\},
 \qquad \|Ax-B_0x\|_2\le L_TM_T\eta^2.                \tag{9.P23}
\]
Indeed, integrate \(Dv\) on the segment from \(x\) to
\(x+\eta v(x)\) and use (9.P22). Integrating \(Dv\) on a segment
between any two points of \(C\) also gives
\(\|E_\eta x-E_\eta y\|_2\le(1+\eta L_T)\|x-y\|_2\).
The same estimate twice bounds each fine macro-step by
\((1+\eta L_T)^2\) on the relevant pairs of states.

Telescope the \(N+1\) endpoints
\(A^{N-i}B_0^i x_0\), \(0\le i\le N\).
The difference between consecutive endpoints first creates one local
defect (9.P23), then propagates through at most \(N-1\) fine macro-steps.
Thus
\[
 \|E_\eta^{2N}x_0-E_{2\eta}^{N}x_0\|_2
 \le L_TM_T\eta^2\sum_{i=0}^{N-1}(1+\eta L_T)^{2i}
 \le L_TM_TN\eta^2e^{2L_TN\eta}.                       \tag{9.P24}
\]
Integrating \(Du\) between the two endpoints proves
\[
 |d_N^u(\eta)|\le R_TL_TM_TN\eta^2e^{2L_TN\eta},
 \qquad
 |d_N^u(T/(2N))|\le
       \frac{R_TL_TM_TT^2e^{L_TT}}{4N}.                \tag{9.P25}
\]
These expressions remain valid when any bound is zero. If (9.P22) and the
tube inclusion hold with the same constants for all dyadic refinements,
then (9.P25) is summable and the terminal scalar Euler sequence is Cauchy.
Equation (9.P24) gives the corresponding terminal state assertion.
This is a conditional finite-dimensional estimate, not a population
existence, identification, or arbitrary-partition theorem.

By contrast, the degree bound following (9.P11) says only that each individual
fixed-order term is \(O_{j,T}(N^{-1})\) at \(\eta=T/(2N)\).
The coefficient \(\Lambda_{j,q}\) remains fixed because the state,
observable, and vector field are fixed. That algebra does not control
the remainder in (9.P13) or the sum over increasing orders, and does not
verify the tube assumption (9.P22). In particular it cannot replace either
a width-uniform estimate or identification of a common population state.

### 9.6. Exact rational interface and independent checks

The existing `pde.exact_calculus` module supplies two small operations:

- `euler_pullback_words(order, steps)` returns a fresh dictionary from
  positive composition tuples `(k1,...,kq)` of `order` to the exact
  `Fraction` weight `binom(steps,q)`. Products act right to left as in
  (9.P7). Zero weights are omitted. Order zero returns `{(): Fraction(1)}`;
  a positive order with zero steps returns `{}`.
- `paired_euler_weights(order)` returns the `order` rows in (9.P11), each
  an immutable tuple of `order` rational coefficients in increasing powers
  of `N`. The degree-`order` coefficient cancels and is omitted. Order zero
  returns `()`; order one returns `((Fraction(0),),)`.

Both inputs must be nonnegative Python integers; booleans, floats and
`Fraction` inputs are rejected. No derivatives, network states, activation
moments or Gaussian expectations are evaluated by either operation.

For the first operation, a finite stack appends every possible positive
next part until the remaining degree is zero or the allowed word length
is exhausted. Every composition is reached once, proving completeness
and uniqueness; choosing its \(q\) active update slots gives the weight
\(\binom Mq\) in (9.P9). At degree \(j\ge1\), unrestricted compositions
number \(2^{j-1}\): the \(j-1\) gaps between unit symbols are independently
cut or not cut. Tuple construction therefore costs at most
\(O(j2^j)\) operations and storage; the degree is a caller-chosen finite
bound, not a promised efficient high-order regime.

The second operation recursively multiplies
\(\binom Nq=\binom N{q-1}(N-q+1)/q\) and multiplies its degree-\(k\)
coefficient by \(2^k-2^j\). This proves the emitted coefficient rows
directly from (9.P11). It uses \(O(j^2)\) rational operations and storage.
Both routines use exact integer/rational arithmetic; bit lengths can grow,
and neither retains a cache, mutates inputs, draws samples, or writes files.

The deterministic tests independently enumerate active update slots, check
every displayed rational polynomial, and compare differential-word evaluation
with direct scalar polynomial Euler composition for \(v(x)=1+x^2\),
\(u(x)=2x+x^3\), at \(x_0=1/3\) through degree six. That last comparison
checks moving-field differentiation and operator ordering using a different
construction. Domain rejection and return ownership are also checked. These checks do not establish a neural width limit or an analytic remainder bound.
