# The all-source analytic scale: the closure that works and the same-radius obstruction

## 1. Verdict

There is a canonical candidate all-source scale for the cylindrical
fixed-operator OMFP grammar.  It is a **scale** of norms, not one Banach norm
on which every product and reused adjoint is bounded.  The natural weights
are

\[
                 w_m(\rho)=\frac{\rho^m}{m!}.                 \tag{1.1}
\]

They close products with a moment-exponent loss and close analytic
composition under an explicit small derivative-seminorm condition.  A
reused adjoint shifts the source order and obeys an explicit Cauchy estimate
from radius \(\rho\) to a strictly smaller radius \(\rho'\).  Ordered step
weights exactly cancel the factorial in the iterated Cauchy estimate for the
pure causal-shift majorant.  This gives a rigorous abstract cross-radius
shift bound, not yet a propagator theorem for the interspersed OMFP
products.

The stronger requirement in the question,

\[
 \|(I+\eta Dg)V\|_{\mathfrak X}
 \le (1+C_0|\eta|)\|V\|_{\mathfrak X},                \tag{1.2}
\]

in one fixed all-source analytic norm, is already incompatible with the
requested same-space product closure: a Banach algebra containing a raw
Gaussian would bound its powers exponentially, while their fixed positive
Gaussian moments grow superexponentially.  There is also a second
coefficientwise-majorant obstruction if the estimate is required to follow
from a separately bounded exact adjoint operation.  For the admissible
residual

\[
                         \varphi_0(x)=\frac1{1+x^2},              \tag{1.3}
\]

same-radius boundedness of the source-order shift forces geometrically
decaying-or-slower weights, whereas finiteness of the activation node forces
faster-than-geometric decay.  Sections 6--7 prove the contradiction.

Consequently no norm of the displayed form in the question can satisfy the
literal same-space product requirement.  In addition, no coefficientwise
positive-majorant realization can satisfy simultaneously

1. finiteness for every residual with
   \(\|\varphi^{(r)}\|_\infty\le MA^r r!\);
2. an untruncated, separately bounded realization of
   \(J^*V=\mathbb E[D_JV]\) at the same source radius; and
3. the same-norm one-step estimate (1.2).

Chronological simplex factors repair the shift only **between two distinct
radii**.  Thus a proof of the desired remainder, if true, must replace (1.2)
by a decreasing-radius propagator theorem and audit the complete OMFP graph
on that scale.  It cannot prove the list of requirements as literally
stated.

## 2. Intrinsic aggregation over all source histories

Fix one finite width-first chronology.  Let \(\mathcal H\) be the Hilbert
direct sum of every exposed forward and reverse isonormal source space,
including every moving query direction.  Redundant directions at a singular
Gram are identified in the Hilbert quotient.  Thus no coordinate inverse or
coordinatewise response coefficient is used.

For a cylindrical generated field \(V\), its \(m\)-th joint source derivative
is

\[
                 \mathcal D^mV\in
 L^p(\Omega;\mathcal H^{\widehat\otimes_\pi m}),       \tag{2.1}
\]

where \(\widehat\otimes_\pi\) is the symmetric projective tensor product.
Equivalently, if \(\mathscr H_m\) is the set of ordered source histories
\(\boldsymbol h=(h_1,\ldots,h_m)\), then

\[
 \|\mathcal D^mV\|_{p,\pi}
 :=\inf\left\{
      \left\|\sum_{\boldsymbol h}\|T_{\boldsymbol h}\|_\pi
      \right\|_{L^p}:
      \mathcal D^mV=\sum_{\boldsymbol h}T_{\boldsymbol h}
            \right\}.                                  \tag{2.2}
\]

The infimum is taken after opposite-layer pointer vectors belonging to the
same intrinsic aggregate have been combined.  Formula (2.2) is therefore
unchanged by adding a redundant Gaussian coordinate.  It is the projective
\(\ell^1\)-aggregation over all source histories requested in the question;
no source order is truncated.

For \(p\ge1\) and \(\rho>0\), define

\[
 \|V\|_{\rho,p}
 :=\sum_{m=0}^\infty\frac{\rho^m}{m!}
       \|\mathcal D^mV\|_{p,\pi}.                     \tag{2.3}
\]

One fixed exponent \(p_m\) at each order is not stable under the product
rule: the term \((\mathcal D^kU)(\mathcal D^{m-k}V)\) requires moments of
both factors above the target exponent.  The closed object is the full
moment scale \(\{\|\cdot\|_{\rho,p}:p\ge1\}\).  If one insists on a literal
sequence, one may set any \(p_m\ge1\); the impossibility theorem in Section 7
holds for every such choice.  In particular, changing the \(p_m\)'s cannot
repair the same-radius obstruction.

## 3. Operations which close on the scale

### Lemma 3.1 (product)

For \(p\ge1\),

\[
             \|UV\|_{\rho,p}
 \le \|U\|_{\rho,2p}\|V\|_{\rho,2p}.                 \tag{3.1}
\]

#### Proof

The source Leibniz rule and the projective cross-norm property give

\[
 \frac{\|\mathcal D^m(UV)\|_{p,\pi}}{m!}
 \le \sum_{k=0}^m
 \frac{\|\mathcal D^kU\|_{2p,\pi}}{k!}
 \frac{\|\mathcal D^{m-k}V\|_{2p,\pi}}{(m-k)!}.       \tag{3.2}
\]

Here Holder is applied only after intrinsic pointer aggregation.  Multiply
by \(\rho^m\), sum in \(m\), and use the Cauchy product identity. \(\square\)

### Lemma 3.2 (analytic activation composition)

Suppose \(\|\varphi^{(r)}\|_\infty\le MA^r r!\).  Put

\[
 R_q(V):=\sum_{m\ge1}\frac{\rho^m}{m!}
                  \|\mathcal D^mV\|_{q,\pi}.          \tag{3.3}
\]

Then

\[
 \|\varphi(V)\|_{\rho,p}
 \le \|\varphi(V)\|_p
     +M\sum_{r\ge1}A^rR_{rp}(V)^r.                    \tag{3.4}
\]

In particular, if \(\sup_{r\ge1}R_{rp}(V)\le R<A^{-1}\),

\[
 \|\varphi(V)\|_{\rho,p}
 \le M+\frac{MAR}{1-AR}.                              \tag{3.5}
\]

#### Proof

The exponential form of Faa di Bruno's formula is

\[
 \frac{\mathcal D^m\varphi(V)}{m!}
 =\sum_{r=1}^m\frac{\varphi^{(r)}(V)}{r!}
   \sum_{\substack{k_1+\cdots+k_r=m\\k_i\ge1}}
   \prod_{i=1}^r\frac{\mathcal D^{k_i}V}{k_i!}.       \tag{3.6}
\]

Use \(\|\varphi^{(r)}\|_\infty/r!\le MA^r\), the
projective cross norm, and Holder with \(r\) equal exponents.  Summation of
the resulting Cauchy products gives (3.4).  Formula (3.5) is the geometric
series bound. \(\square\)

For

\[
 \psi_\alpha(v)=c_\alpha\{v+\alpha\varphi(v)\},
 \qquad
 c_\alpha=\|G+\alpha\varphi(G)\|_2^{-1},              \tag{3.7}
\]

and \(|\alpha|M\le1/4\), the elementary bounds
\(4/5\le c_\alpha\le4/3\) turn (3.4) into a completely explicit
composition estimate.

### Lemma 3.3 (expectations, singular Grams, and rank-one updates)

Conditional or full Gaussian expectation is contractive:

\[
 \|\mathbb E_{\mathcal B}V\|_{\rho,p}
 \le\|V\|_{\rho,p}.                                   \tag{3.8}
\]

If \(b\otimes x\) is a learned rank-one update and the tensor is given its
projective norm, then

\[
 \|b\otimes x\|_{\rho,p}
 \le\|b\|_{\rho,2p}\|x\|_{\rho,2p}.                 \tag{3.9}
\]

Both statements remain valid at a singular source Gram.

#### Proof

Source differentiation commutes with expectation in the cylindrical core.
Jensen and the definition (2.2) prove (3.8).  The identity
\(\|u\otimes v\|_\pi=\|u\|\|v\|\), Leibniz, and the proof of Lemma 3.1
give (3.9).  Because the source tangent space was quotiented before taking
the projective norm, neither proof refers to a Gram inverse. \(\square\)

These lemmas prove closure of products, activation composition, Gaussian
expectations, and learned rank-one updates on the two-parameter scale.  They
also show why a single list of moment exponents is not the closed object.

## 4. The exact adjoint is a source-order shift

Let \(J\) be one fixed isonormal block.  After all opposite-layer pointer
vectors have been combined, the exact identity is

\[
                         J^*V=\mathbb E[D_JV].          \tag{4.1}
\]

For every remaining ordered history \(\boldsymbol h\), differentiation of
the intrinsic vector identity gives

\[
 D_{\boldsymbol h}(J^*V)
 =\mathbb E[D_JD_{\boldsymbol h}V].                   \tag{4.2}
\]

Consequently its positive majorant is the left shift

\[
                 (Sa)_m=a_{m+1},qquad
 a_m=\|\mathcal D^mV\|_{p,\pi}.                       \tag{4.3}
\]

This statement includes derivatives of moving pointer vectors: they are
terms of the intrinsic tensor in (4.2), not frozen coordinates.  It is also
why a finite source ledger is not closed.

### Lemma 4.1 (sharp type of Cauchy loss)

For \(0<\rho'<\rho\), let

\[
                  \|a\|_\rho=\sum_{m\ge0}
                       \frac{\rho^m}{m!}a_m,qquad a_m\ge0.          \tag{4.4}
\]

Then, for every integer \(k\ge1\),

\[
 \|S^ka\|_{\rho'}
 \le \frac{k!\rho}{(\rho-\rho')^{k+1}}\|a\|_\rho.   \tag{4.5}
\]

At equal radii, \(S\) is unbounded.

#### Proof

Writing \(n=m+k\), the ratio between the coefficient of \(a_n\) on the
left and its coefficient on the right is

\[
 \rho^{-k}\frac{n!}{(n-k)!}
       \left(\frac{\rho'}\rho\right)^{n-k}.           \tag{4.6}
\]

For \(x=\rho'/\rho\),

\[
 \sup_{n\ge k}\frac{n!}{(n-k)!}x^{n-k}
 \le\sum_{m\ge0}\frac{(m+k)!}{m!}x^m
 =\frac{k!}{(1-x)^{k+1}},                             \tag{4.7}
\]

which proves (4.5).  At \(\rho'=\rho\), the ratio for \(k=1\) is
\(n/\rho\), hence is unbounded. \(\square\)

Thus (4.1) closes from \(\mathfrak X_\rho\) to
\(\mathfrak X_{\rho'}\), but not as an endomorphism of
\(\mathfrak X_\rho\).

## 5. What chronological step simplices actually buy

Let \(e_0,\ldots,e_{N-1}\) be arbitrary real steps and
\(\tau=\sum_i|e_i|\).  For every \(k\),

\[
 \sum_{i_1<\cdots<i_k}\prod_{r=1}^k|e_{i_r}|
 \le\frac{\tau^k}{k!}.                                \tag{5.1}
\]

Suppose a causal history edge contributes at most \(CS\) in the source
majorant.  Combining (4.5) and (5.1) gives, with
\(\delta=\rho-\rho'\),

\[
 \begin{aligned}
 \|P_NV\|_{\rho'}
 &\le \|V\|_\rho+
   \sum_{k\ge1}\frac{(C\tau)^k}{k!}
      \|S^kV\|_{\rho'}\\
 &\le\left[1+\frac{\rho}{\delta}
       \frac{C\tau/\delta}{1-C\tau/\delta}\right]
      \|V\|_\rho,
 \qquad C\tau<\delta .                               \tag{5.2}
 \end{aligned}
\]

This is the rigorous radius-loss/time-simplex mechanism.  The ordered
simplex cancels the \(k!\) created by \(k\) source shifts.  It does not make
the shift bounded at \(\delta=0\).

For the depth-two OMFP chronology, Lemma 3.1 of
'temporary_depth_time_doubling/UNIFORM_L2.md' proves syntactic causal
divisibility of every old-source response by its source-time step.  It does
not prove that the fully expanded all-source graph is a pure chain of the
form used in (5.2).  Moreover, the current response
\(\mathbb E[a_s\psi''(z_s)]x_s\) is unweighted.  A complete scale proof must
therefore prove, from the exact graph, that every repeated use of an
unweighted current contraction is separated from the next contraction by a
chronological update, and must reserve a fixed radius loss for the finite
terminal contraction.  Equation (5.2) does not by itself prove that graph
statement.

## 6. An admissible residual with supergeometric Gaussian response jets

The residual (1.3) satisfies the envelope in the question with \(M=A=1\).
Indeed,

\[
 \varphi_0(x)=\frac1{2i}\left\{\frac1{x-i}-\frac1{x+i}\right\},
\]

and therefore

\[
 \|\varphi_0^{(r)}\|_\infty\le r!,
 \qquad r\ge0.                                        \tag{6.1}
\]

It is genuinely nonlinear.  Its Fourier transform is
\(\widehat\varphi_0(\xi)=\pi e^{-|\xi|}\).  Hence, for \(G\sim N(0,1)\),

\[
 b_{2k}:=\left|\mathbb E\varphi_0^{(2k)}(G)\right|
 =\int_0^\infty \xi^{2k}e^{-\xi-\xi^2/2}\,d\xi .     \tag{6.2}
\]

On \([\sqrt{k},\sqrt{k}+1]\), for \(k\ge1\),

\[
 \xi^{2k}\ge k^k,qquad
 \xi+\frac{\xi^2}{2}
 \le \frac{k}{2}+2\sqrt{k}+\frac32.
\]

Thus

\[
 b_{2k}\ge
 k^k\exp\left(-\frac{k}{2}-2\sqrt{k}-\frac32\right). \tag{6.3}
\]

In particular \((b_{2k})^{1/(2k)}\to\infty\).  Gaussian smoothing reduces
the raw \((2k)!\) derivative growth, but not to an exponential sequence.

## 7. Impossibility of one fixed all-source norm

### Proposition 7.1 (raw-Gaussian product no-go)

Let \(w_m>0\), \(p_m\in[1,\infty]\), and suppose a norm of the form
\(\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m,\pi}\) contains a standard raw
Gaussian \(G\).  There is no finite \(C_\times\) for which

\[
 \|UV\|_{\mathfrak X}
 \le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}    \tag{7.0}
\]

holds on a product-closed space containing \(G\).

#### Proof

If \(p_0=\infty\), then \(w_0\|G\|_\infty=\infty\), so \(G\) is not in the
space.  Let \(p_0<\infty\) and \(N_G=\|G\|_{\mathfrak X}<\infty\).
Iteration of (7.0) gives

\[
 \|G^n\|_{\mathfrak X}
 \le C_\times^{n-1}N_G^n.                              \tag{7.0a}
\]

On the other hand,

\[
 \|G^n\|_{\mathfrak X}
 \ge w_0\|G^n\|_{p_0}
 =w_0\|G\|_{np_0}^n.                                   \tag{7.0b}
\]

There is a numerical \(c_G>0\) such that
\(\|G\|_q\ge c_G\sqrt q\) for \(q\ge1\).  For example, integrate the
Gaussian density on
\([\sqrt q,\sqrt q+q^{-1/2}]\) and take a \(q\)-th root.  Taking \(n\)-th
roots in (7.0a)--(7.0b) would imply

\[
 w_0^{1/n}c_G\sqrt{np_0}
 \le C_\times^{1-1/n}N_G,
\]

which is impossible as \(n\to\infty\).  This uses only the zeroth source
order, so no higher-order history aggregation or exponent choice can repair
it. \(\square\)

### Theorem 7.2 (positive-majorant same-radius no-go)

Let \(w_m>0\) and \(p_m\ge1\).  Assume an all-source projective norm

\[
                 \|V\|_{\mathfrak X}
 =\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m,\pi}          \tag{7.1}
\]

has both of the following properties.

1. The coefficientwise estimate of the exact source contraction is bounded
   at the same radius on the untruncated positive source-majorant
   completion: for every finitely supported \(a_m\ge0\),

   \[
             \sum_{m\ge0}w_ma_{m+1}
             \le K\sum_{m\ge0}w_ma_m                 \tag{7.2}
   \]

   for some finite \(K\).
2. For every admissible activation and every unit raw Gaussian query \(Jc\),
   the node \(\psi_\alpha(Jc)\) has finite norm whenever \(\alpha\ne0\) is
   in the proposed interval.

Then these properties are inconsistent, already for \(\varphi_0\) in
(1.3).

#### Proof

Apply (7.2) to a sequence supported at \(m=n\).  This gives

\[
                       w_{n-1}\le Kw_n,
 \qquad\text{hence}\qquad
                       w_n\ge w_0K^{-n}.               \tag{7.3}
\]

Let \(\|c\|_2=1\), so \(Jc\) is a standard Gaussian.  For \(m\ge2\),

\[
 \mathcal D_J^m\psi_\alpha(Jc)
 =c_\alpha\alpha\,\varphi_0^{(m)}(Jc)c^{\otimes m}.   \tag{7.4}
\]

The projective norm of \(c^{\otimes m}\) is one, and every
\(L^{p_m}\)-norm dominates the absolute expectation.  Therefore

\[
 \|\psi_\alpha(Jc)\|_{\mathfrak X}
 \ge |c_\alpha\alpha|
       \sum_{k\ge1}w_{2k}b_{2k}.                      \tag{7.5}
\]

By (6.3) and (7.3), the \(k\)-th summand is at least

\[
 |c_\alpha\alpha|w_0K^{-2k}
 k^k e^{-k/2-2\sqrt{k}-3/2},                          \tag{7.6}
\]

which does not even tend to zero.  Thus (7.5) is infinite, contradicting
property 2. \(\square\)

The theorem is independent of the choice of moment exponents.  It also
survives arbitrarily small nonzero \(|\alpha|\): multiplying an infinite
positive series by a nonzero constant does not make it finite.

Theorem 7.2 has a deliberately precise scope.  It rules out a same-radius
proof which first takes absolute values over all source histories and then
estimates the adjoint by the unrestricted left shift.  Same-radius
boundedness of the actual adjoint on a smaller, constrained reachable set
would not by itself imply (7.2); proving that implication would require a
reachable-jet richness theorem.  Proposition 7.1, independently, already
rules out the literal same-space Banach product norm demanded in the
question.

### Corollary 7.3

The exact checklist in the question cannot hold.  Proposition 7.1 refutes
its single-space product closure.  If one additionally uses the stipulated
coefficientwise all-source adjoint majorant, Theorem 7.2 refutes that route
for the full activation class.  Neither proposition is a counterexample to
the scalar coarse/fine remainder inequality itself.

## 8. Consequence for the requested uniform remainder proof

The scale lemmas establish the following facts completely.

1. The intrinsic all-history aggregation is (2.2).
2. The analytic weights are \(\rho^m/m!\).
3. Products, activation composition, Gaussian expectations, and learned
   rank-one updates satisfy (3.1), (3.4), (3.8), and (3.9).
4. The exact reused adjoint has the radius-loss estimate (4.5).
5. Chronological simplices yield the cross-radius propagator (5.2).
6. No same-space Banach product norm of the requested form exists, by
   Proposition 7.1; and the unrestricted positive-majorant adjoint route is
   ruled out by Theorem 7.2.

What remains possible is a corrected theorem using a decreasing source
radius \(\rho_s\) and a moment scale, with total loss proportional to
\(\sum_s|e_s|\).  To obtain the desired \(t^4|\eta|^5\) remainder from that
route, one would still have to prove two graph-specific statements not
contained in the abstract scale lemma:

* every unweighted current adjoint is paired with either a subsequent step
  edge or one of a uniformly bounded number of terminal contractions; and
* the full moving-pointer product majorant remains below the threshold in
  (3.5) while the moment parameter is propagated through (3.1).

Those are genuine additional OMFP estimates.  They cannot be obtained from
the requested same-space Banach-algebra architecture, because Proposition
7.1 rules out that architecture.  A smaller reachable composite estimate
which never separates multiplication from the adjoint is not ruled out
here, but it is a different theorem from the checklist in the question.

## 9. Adversarial audit

An independent audit reconstructed every numerical inequality above.

1. The product Cauchy convolution (3.1), Faa di Bruno bound (3.4), shift
   constant (4.5), simplex sum (5.1), and Fourier lower bound
   (6.2)--(6.3) pass.
2. Proposition 7.1 is insensitive to every positive-order tensor/history
   convention because it uses only \(w_0\|G^n\|_{p_0}\).  Hence no
   history aggregation can evade it while retaining a same-space Banach
   product estimate.
3. Theorem 7.2 is intentionally restricted to the unrestricted positive
   source-majorant completion.  The earlier, stronger claim that boundedness
   of the actual reachable adjoint was “equivalent” to (7.2) was rejected:
   constrained reachable jets need not realize arbitrary finitely supported
   positive sequences.  That overclaim has been removed.
4. Equation (5.2) is only a pure causal-shift scale estimate.  It is not
   presented as closure of interspersed activation/product nodes or of the
   unweighted current response.
5. Therefore the audited conclusion is a structural no-go for the exact
   single-space checklist, not a disproof of the scalar remainder bound.
