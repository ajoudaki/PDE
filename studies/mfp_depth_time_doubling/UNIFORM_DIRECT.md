# Direct paired-Euler attack on the uniform time remainder

## Verdict

The time-combinatorial part of the desired estimate is true and admits a
short quantitative proof: a single coarse Euler step and two fine Euler
steps differ by an exact factor \(h^2\); telescoping over the \(t\) coarse
blocks and differentiating only the remaining defect three times gives
the sharp factor \(t^4h^5\).

For the actual Gaussian network, however, the hypotheses needed to apply
that lemma have not been proved.  The fixed-operator construction in
`OPERATOR_BRIDGE_CHECK.md` supplies only finite-generated-core \(C^3\)
regularity, while the fixed-time Price compiler supplies \(C^5\) bounds
whose constants grow with the whole time DAG.  Neither result supplies
the uniform generated-core fourth-derivative estimate isolated in
(4.1) below.  Moreover, that estimate cannot be obtained by declaring
the population network \(C^4\) on an open \(L^2\) ball: Section 5 gives an
explicit admissible activation for which even the bottom Nemytskii map is
not twice Frechet differentiable on \(L^2\).

Thus this note proves the direct Euler lemma completely and reduces the
network theorem to one precise non-output-derived estimate, but it does
not prove that estimate.  In the present state of the argument the
uniform network theorem remains open; treating the reduction as its proof
would repeat the invalid global-\(L^2\) shortcut already excluded in the
cubic audit.

## 1. A quantitative paired-Euler lemma

Let \(X\) be a real Banach space, \(x_0\in X\), and let the closed unit
ball \(U=\{x:\|x-x_0\|\le1\}\) be contained in the domains of

\[
 g:U\to X,\qquad f:U\to\mathbb R.
\]

Assume that \(g,f\in C^4(U)\), and, for one \(K\ge1\),

\[
 \max_{0\le r\le4}\sup_U\|D^rg\|\le K,
 \qquad
 \max_{1\le r\le4}\sup_U\|D^rf\|\le K.
 \tag{1.1}
\]

Here \(D^0g=g\), and all derivative norms are operator norms. Define

\[
 E_h(x)=x+hg(x),\qquad C_h=E_{2h},\qquad P_h=E_h\circ E_h,
\]

\[
 d_t(h)=f(C_h^t x_0)-f(P_h^t x_0).
 \tag{1.2}
\]

Suppose in addition that \(d_t(-h)=-d_t(h)\). Then, with

\[
 c_K=\frac1{64K^2},\qquad C_K=10^9K^{10},
 \tag{1.3}
\]

one has, for every integer \(t\ge1\) and

\[
 |h|\le c_K/t,
\]

\[
 \left|d_t(h)-\frac{d_t'''(0)}6h^3\right|
 \le C_Kt^4|h|^5.
 \tag{1.4}
\]

The numerical constant in (1.3) is intentionally coarse.  The exponent
\(t^4\) is the important point.

## 2. Uniform three-jet bounds for Euler strings

We first record the elementary estimates used below.  Consider a string

\[
 x_{q+1}(h)=x_q(h)+a_qh g(x_q(h)),\qquad |a_q|\le2,
 \tag{2.1}
\]

and write \(A_q=\sum_{i<q}|a_i|\), \(A=\sum_i|a_i|\). Assume
\(|h|A\le1/(16K^2)\). Direct differentiation of (2.1) gives

\[
\begin{aligned}
 \|x_{q+1}'\|&\le(1+|a_qh|K)\|x_q'\|+|a_q|K,\\
 \|x_{q+1}''\|&\le(1+|a_qh|K)\|x_q''\|
 +2|a_q|K\|x_q'\|+|a_qh|K\|x_q'\|^2,\\
 \|x_{q+1}'''\|&\le(1+|a_qh|K)\|x_q'''\|\\
 &\quad+3|a_q|K(\|x_q''\|+\|x_q'\|^2)\\
 &\quad+|a_qh|K(3\|x_q'\|\|x_q''\|+\|x_q'\|^3).
\end{aligned}
 \tag{2.2}
\]

The product of all homogeneous factors in (2.2) is at most

\[
 \prod_q(1+|a_qh|K)\le e^{K|h|A}<2.
 \tag{2.3}
\]

For \(r\ge0\), monotonicity of \(u^r\) gives the left-sum estimate

\[
 \sum_q |a_q|A_q^r
 \le\int_0^A u^r\,du=\frac{A^{r+1}}{r+1}.
 \tag{2.4}
\]

Applying (2.3)--(2.4) successively to the three lines of (2.2) proves,
when \(x_0\) is independent of \(h\),

\[
 \|x_q'\|\le2KA_q,\qquad
 \|x_q''\|\le12K^3A_q^2,\qquad
 \|x_q'''\|\le192K^5A_q^3.
 \tag{2.5}
\]

For completeness, constants satisfying (2.5) are obtained from the
terminating recursion

\[
 p_1=2K,
\]

\[
 p_2=2\left(Kp_1+\frac13Kp_1^2\right),
\]

\[
 p_3=2K\left[p_2+p_1^2+\frac14(3p_1p_2+p_1^3)\right].
 \tag{2.6}
\]

For \(K\ge1\), the right sides are bounded respectively by
\(2K,12K^3,192K^5\). This proves (2.5), rather than assuming a
continuous-time stability statement.

We also need to restart a string from an \(h\)-dependent convex
combination of two such strings.  The same calculation, retaining the
initial derivatives, gives

\[
 \|x_q'\|\le6KA_q,\qquad
 \|x_q''\|\le60K^3A_q^2,\qquad
 \|x_q'''\|\le1300K^5A_q^3.
 \tag{2.7}
\]

Indeed, if the initial bounds are \(p_rA_0^r\), the terminating recursion

\[
 q_1=2(p_1+K),
\]

\[
 q_2=2\left[p_2+Kq_1+\frac13Kq_1^2\right],
\]

\[
 q_3=2\left[p_3+K(q_2+q_1^2)
 +\frac14K(3q_1q_2+q_1^3)\right]
 \tag{2.8}
\]

majorizes the three recurrences.  Substitution of (2.5), followed by
\(K\ge1\), gives (2.7). Both recursions stop after three assignments.

Every Euler string used below has total coefficient at most \(2t\).
Consequently (1.3) implies both the hypothesis of (2.3) and

\[
 \|x_q-x_0\|\le |h|AK\le2c_KK<1/16.
 \tag{2.9}
\]

Convex interpolation preserves the unit ball.  Thus every invocation of
(1.1) below is justified.

## 3. Exact coarse/fine factorization and its remainder

Fix \(0\le j<t\), put \(m=t-j-1\), and set

\[
 y=P_h^j x_0,\qquad c=C_hy,\qquad p=P_hy.
\]

The local coarse/fine defect factors exactly as

\[
 p-c=h^2a(h,y),
\]

\[
 a(h,y)=\int_0^1
 Dg\bigl(y+\sigma hg(y)\bigr)[g(y)]\,d\sigma.
 \tag{3.1}
\]

Let \(H_{m,h}=f\circ C_h^m\). The fundamental theorem of calculus on
the segment from \(c\) to \(p\) gives

\[
 H_{m,h}(c)-H_{m,h}(p)=-h^2A_{j,t}(h),
 \tag{3.2}
\]

\[
 A_{j,t}(h)=\int_0^1
 DH_{m,h}\bigl(c+\lambda(p-c)\bigr)
 [a(h,y)]\,d\lambda.
 \tag{3.3}
\]

Equations (2.5)--(2.8), the chain rule, and (1.1) imply the explicit
bound

\[
 \sup_{|u|\le |h|}|A_{j,t}'''(u)|
 \le10^9K^{10}t^3.
 \tag{3.4}
\]

Here are the details of the last, sometimes hidden, estimate.  For a
curve \(z\), composition with \(g\) gives the three jet bounds

\[
 K\|z'\|,\quad
 K(\|z''\|+\|z'\|^2),\quad
 K(\|z'''\|+3\|z'\|\|z''\|+\|z'\|^3).
 \tag{3.5}
\]

For \(Dg(z)[v]\), the corresponding bounds are

\[
 K(\|z'\|\|v\|+\|v'\|),
\]

\[
 K\{(\|z''\|+\|z'\|^2)\|v\|
 +2\|z'\|\|v'\|+\|v''\|\},
\]

\[
 K\{(\|z'''\|+3\|z'\|\|z''\|+\|z'\|^3)\|v\|
 +3(\|z''\|+\|z'\|^2)\|v'\|
 +3\|z'\|\|v''\|+\|v'''\|\}.
 \tag{3.6}
\]

The same formulas hold with \(Dg\) replaced by \(Df\). Applying
(3.5)--(3.6) first to (3.1), then propagating the tangent by

\[
 z_{r+1}=z_r+2hg(z_r),qquad
 v_{r+1}=v_r+2hDg(z_r)[v_r],
 \tag{3.7}
\]

and finally applying (3.6) to \(Df(z_m)[v_m]\), yields, successively,

\[
 \|a\|\le K^2,\quad
 \|a'\|\le10K^3t,\quad
 \|a''\|\le256K^5t^2,\quad
 \|a'''\|\le12400K^7t^3,
 \tag{3.8}
\]

\[
 \|v\|\le2K^2,\quad
 \|v'\|\le256K^3t,\quad
 \|v''\|\le65536K^5t^2,\quad
 \|v'''\|\le3\cdot10^7K^7t^3.
 \tag{3.9}
\]

To verify that (3.9) does not hide a stability assertion, put
\(B=Dg(z)[v]\). At every step of (3.7), differentiation gives exactly

\[
 v_+'=v'+2B+2hB',\qquad
 v_+''=v''+4B'+2hB'',\qquad
 v_+'''=v'''+6B''+2hB'''.
 \tag{3.9a}
\]

The four required bounds are

\[
\begin{aligned}
 \|B\|&\le K\|v\|,\\
 \|B'\|&\le K(\|z'\|\|v\|+\|v'\|),\\
 \|B''\|&\le K\{(\|z''\|+\|z'\|^2)\|v\|
               +2\|z'\|\|v'\|+\|v''\|\},\\
 \|B'''\|&\le K\{(\|z'''\|+3\|z'\|\|z''\|
                  +\|z'\|^3)\|v\|\\
 &\hspace{39mm}+3(\|z''\|+\|z'\|^2)\|v'\|
 +3\|z'\|\|v''\|+\|v'''\|\}.
\end{aligned}
 \tag{3.9b}
\]

Move the last term \(2|h|K\|v^{(r)}\|\) in each applicable line into
the homogeneous product (2.3). Using

\[
 \sum_{s<t}s^r\le \frac{t^{r+1}}{r+1},
 \qquad |h|t\le c_K,
 \tag{3.9c}
\]

in increasing derivative order gives (3.9). For example, the first
three resulting right-side constants are bounded by

\[
 2K^2,\qquad 220K^3t,\qquad 64400K^5t^2,
\]

which were rounded upward in (3.9). Substitution of those rounded
bounds into the last line of (3.9b) gives a number below
\(3\cdot10^7K^7t^3\).

Inserting (2.7) and (3.9) in the last formula in (3.6) is bounded by
\(10^9K^{10}t^3\). This is (3.4). Each displayed constant is obtained
only by addition and multiplication of the preceding displayed bounds;
there is no supremum of \(d_t\) or of an output derivative in its
definition.

Now telescope the hybrids:

\[
 d_t(h)=\sum_{j=0}^{t-1}
 \{H_{t-j-1,h}(C_hP_h^jx_0)
   -H_{t-j-1,h}(P_hP_h^jx_0)\}
 =-h^2\sum_{j=0}^{t-1}A_{j,t}(h).
 \tag{3.10}
\]

Taylor's formula with integral remainder gives

\[
 A_{j,t}(h)=A_{j,t}(0)+hA_{j,t}'(0)
 +\frac{h^2}{2}A_{j,t}''(0)+R_{j,t}(h),
\]

\[
 |R_{j,t}(h)|\le\frac{|h|^3}{6}
 \sup_{|u|\le|h|}|A_{j,t}'''(u)|.
 \tag{3.11}
\]

Thus (3.4) and (3.10) yield a polynomial of degrees two through four
plus a remainder bounded by

\[
 \frac{10^9}{6}K^{10}t^4|h|^5.
 \tag{3.12}
\]

Oddness of \(d_t\) makes its second and fourth derivatives at zero vanish.
The coefficients of degrees two and four in (3.10)--(3.11) are precisely
those derivatives divided by \(2!\) and \(4!\), so they vanish. The
remaining coefficient is \(d_t'''(0)/6\). Enlarging (3.12) to the
constant in (1.3) proves (1.4).

## 4. Exact network obligation left by the lemma

For the population network, parity and the cubic coefficient have already
been proved:

\[
 D_{t,L}(-h)=-D_{t,L}(h),
 \qquad
 \frac{D_{t,L}'''(0)}6
 =-\frac{t(2t-1)}2J_{\phi,L}.
 \tag{4.0}
\]

Therefore Sections 1--3 would prove the requested theorem with

\[
 c_{\phi,L}=\frac1{64K_{\phi,L}^2},
 \qquad
 C_{\phi,L}=10^9K_{\phi,L}^{10},
 \tag{4.0a}
\]

provided one proves the following generated-core estimate directly for
the fixed Gaussian operators \(W_{a,0}=I_a+J_a^*\):

\[
 \boxed{
 \sup_{\substack{t\ge1,\ 0\le j<t\\ |h|t\le c_{\phi,L}}}
 t^{-3}|A_{j,t}'''(h)|
 \le K_{\phi,L},}
 \tag{4.1}
\]

where \(A_{j,t}\) is the explicit coarse/fine hybrid contraction (3.3),
formed from the actual population network, and \(K_{\phi,L}\) must be
constructed from \(M_\phi\), finitely many Gaussian moments, and \(L\).
Equation (4.1) is a proof obligation, not a proposed definition of an
allowed constant.

The existing results do not prove (4.1):

* `OPERATOR_BRIDGE_CHECK.md`, Section 4, constructs mixed derivatives
  only through order three on each *fixed finite* generated core.  The
  derivative in (4.1) contains a differentiated tangent and therefore
  fourth derivatives of the static network/gradient.
* `COMPILER_DEPTH_TIME.md` controls five derivatives for each fixed
  \(N\), but its expression weight is iterated once per reused-matrix
  action. Its resulting bound is \(B_\phi^{E_{L,N}}\), not a uniform
  \(K_{\phi,L}N^3\) bound for (4.1).
* An energy bound for the undifferentiated Hilbert parameters does not
  imply (4.1), because differentiated activations contain products of
  several \(L^2\) directions.

Consequently (4.1) requires a new, time-uniform moment-scale or Gaussian
Sobolev estimate for all generated tangent jets.  No such estimate is
present in the current proof set.

## 5. Why a global \(L^2\) smoothness shortcut is false

The missing estimate cannot be supplied by applying Section 1 to the
Hilbert parameter space and asserting that the network vector field is
\(C^4\) on an \(L^2\) ball.

Take the admissible normalized activation

\[
 \phi(x)=\frac{2+\cos x}
 {\{\mathbb E(2+\cos G)^2\}^{1/2}}.
 \tag{5.1}
\]

It is \(C^\infty\), bounded, has bounded derivatives of every order, and
\(\mathbb E\phi(G)^2=1\). Its second derivative is nonzero on a set of
positive Gaussian measure.

On any nonatomic probability space, the Nemytskii map
\(N_\phi:u\mapsto\phi(u)\) from \(L^2\) to \(L^2\) is not twice Frechet
differentiable at a Gaussian \(u\). If it were, its second derivative on
bounded directions would have to be

\[
 D^2N_\phi(u)[v,w]=\phi''(u)vw.
 \tag{5.2}
\]

Choose a set on which \(|\phi''(u)|\ge a>0\), and inside it choose sets
\(E_n\) of probability \(1/n\). With \(v_n=\sqrt n\,1_{E_n}\),

\[
 \|v_n\|_2=1,
 \qquad
 \|\phi''(u)v_n^2\|_2
 \ge a\sqrt n.
 \tag{5.3}
\]

This contradicts boundedness of a bilinear second Frechet derivative.
Thus even the first activation layer defeats the required open-ball
\(C^2(L^2,L^2)\) claim. The fixed-core directional calculus avoids this
counterexample, but a *uniform* version of that calculus is exactly the
unproved estimate (4.1).

## 6. Conclusion

The factor \(t^4\) is not the unresolved part: it follows sharply from
the exact paired-step factorization and the three-jet count.  What remains
unproved is a network-specific activation-envelope bound for those three
hybrid jets, uniform over \(t\) on \(|h|t\le c_{\phi,L}\). Until (4.1) is
proved by a valid generated-core moment argument, the claimed
\(C_{\phi,L}t^4|h|^5\) theorem cannot be declared rigorous.
