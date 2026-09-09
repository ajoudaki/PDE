# Rejected causal-shift attempt and surviving conditional skeleton lemma

> **Superseded verdict.**  The claimed application to the complete marked
> \(L=2\) OMFP grammar failed two independent adversarial audits; see
> `AUDIT_CAUSAL_COMPOSITE.md` and `ROUTE_CAUSAL_COMPOSITE_AUDIT.md`.
> Lemma 3.1 is false for arbitrary scalar response nodes, Corollary 3.2 does
> not control moving-pointer descendants, and the constant \(C\) below is
> assumed rather than proved uniform in horizon and source order.  Only
> Lemma 4.1, Lemma 6.1 (with \(c\ge0\)), and the generating-function estimate
> in Theorem 5.1 conditional on its charging and uniform-branching hypotheses
> survive.  Nothing in this note proves an OMFP propagator bound.

## 1. Result

This note attempted to close one of the graph-specific gaps left by the
analytic-scale argument.  The attempted causal claim was not established:
the full response grammar contains generated
\(p,q,\bar\rho,\bar\sigma\) subtrees and moving-pointer descendants omitted
from the proof below.  If one separately assumes a contextual charging
injection giving \(k-1\) distinct chronological factors for \(k\) shifts,
and a weighted branching constant uniform in horizon and source order, the
following conditional skeleton calculation applies.

After \(d\) common-step derivatives hit those explicit factors, the
resulting causal-shift propagator has the explicit cross-radius bound

\[
\boxed{
\left\|\partial_h^{[d]}P_N^{\mathrm{resp}}(h)V\right\|_{\rho'}
\le
A_N^d\,
\frac{\rho\,C^{d+1}(d+1)!}
{\delta^{d+2}(1-C\tau/\delta)^{d+2}}
\|V\|_\rho ,
}
\tag{1.1}
\]

where

\[
\delta=\rho-\rho'>0,\qquad
A_N=\sum_{i=0}^{N-1}|a_i|,\qquad
\varepsilon_i=a_i h,\qquad
\tau=\sum_i|\varepsilon_i|,
\tag{1.2}
\]

\(C\) majorizes the total finite branching of one response-shift
transition, \(C\tau<\delta\), \(\max_i|\varepsilon_i|\le1\), and
\(\partial_h^{[d]}\) denotes the part of the derivative which hits exactly
\(d\) displayed chronological step factors and no kernel. For every
coarse/fine hybrid used in step doubling,

\[
N\le2t,\qquad |a_i|\le2,\qquad A_N\le4t,
\tag{1.3}
\]

so (1.1) is \(O(t^d)\), uniformly in the horizon.

Here \(P_N^{\mathrm{resp}}\) is the subseries containing at least one
response shift; the identity subseries is handled separately. The lemma is
an exact statement about the causal shift skeleton. It does
not assume a same-radius Banach algebra. It also does not assert the
remaining stochastic-tail and nonlinear product estimate.

## 2. The only unweighted response in one depth-two time slice

Use the exact inverse-free depth-two equations

\[
z_s=\xi_s+\sum_{i<s}\varepsilon_i
      (Q_{is}+\bar\rho_{si})\delta_i,               \tag{2.1}
\]

\[
r_s=\chi_s+\sigma_{ss}x_s+
\sum_{i<s}\varepsilon_i
      (K_{is}+\bar\sigma_{si})x_i.                 \tag{2.2}
\]

They follow from the algebraic causal factorizations

\[
\rho_{si}=\varepsilon_i\bar\rho_{si},\qquad
\sigma_{si}=\varepsilon_i\bar\sigma_{si}
\quad(i<s).                                       \tag{2.3}
\]

The current response

\[
\sigma_{ss}=\mathbb E[a_s\psi''(z_s)]              \tag{2.4}
\]

is the only response term in a time-\(s\) slice without an explicit
historical step. The other cross-time dependencies occur in (2.1),
(2.2), or the state sums

\[
a_s=A+\sum_{i<s}\varepsilon_i y_i,\qquad
u_s=U+\sum_{i<s}\varepsilon_i d_i,                 \tag{2.5}
\]

and every such edge to time \(i<s\) carries \(\varepsilon_i\).

## 3. Causal charging

### Lemma 3.1

Fully unroll a scalar node of the exact \(L=2\) DAG into its
forward/reverse dependency graph, without differentiating a displayed
step factor. On any directed root-to-leaf branch containing \(k\ge1\)
adjoint-response vertices, there are \(k-1\) distinct time indices

\[
i_1<i_2<\cdots<i_{k-1}                              \tag{3.1}
\]

such that the branch coefficient contains

\[
\prod_{\ell=1}^{k-1}\varepsilon_{i_\ell}.          \tag{3.2}
\]

There may be one additional unweighted response vertex, but not two.

#### Proof

Read the branch backward from its terminal node. At a fixed time \(s\),
the forward historical response (2.1) and the reverse current response
(2.2) cannot both lie on the same dependency branch:

* choosing a historical summand in \(z_s\) immediately moves the branch
  to \(\delta_i\) at a strict earlier time \(i<s\);
* choosing the current summand \(\sigma_{ss}x_s\) in \(r_s\) moves the
  branch to \(x_s\), which is computed before \(z_s,\delta_s,r_s\), and
  hence encounters no second time-\(s\) response.

Thus a branch contains at most one response vertex at each time. After
an unweighted current response at time \(s\), reaching any further
response requires leaving time \(s\). By (2.1), (2.2), and (2.5), every
edge which leaves time \(s\) backward lands at a strict earlier time
\(i<s\) and contains the factor \(\varepsilon_i\). A historical response
already has exactly such a factor in its own summand.

Charge each response vertex except the last one on the branch to the
first strict backward time jump following it. The charged landing times
strictly decrease while the branch is read backward, so the charged
indices are distinct. Reversing their order gives (3.1), and their
edge factors give (3.2). There are exactly \(k-1\) charged vertices.
\(\square\)

### Corollary 3.2 (generated scalar derivatives)

After expanding any \(q\)-fold scalar derivative by the product and chain
rules, every root-to-leaf branch of every resulting monomial has the same
property, except that at most \(q\) of the factors in (3.2) can have been
removed by differentiating the explicit schedule. Hence a branch with
\(k\) response shifts retains at least

\[
(k-1-q)_+                                           \tag{3.3}
\]

chronological factors. Equivalently, at most \(q+1\) shifts are
unweighted on that branch.

#### Proof

Differentiating a kernel changes the node decorating an existing edge and
does not remove its explicit \(\varepsilon_i\). Differentiating an
explicit factor can remove one occurrence. A \(q\)-fold derivative can
make this choice at most \(q\) times. Apply Lemma 3.1 to each branch
before those choices. \(\square\)

This statement includes moving-pointer derivatives: differentiating a
moving query changes the kernel attached to its chronological edge; it
does not create a new cross-time edge without the step already present in
(2.1), (2.2), or (2.5).

## 4. Exact differentiated simplex bound

### Lemma 4.1

Let \(\varepsilon_i=a_i h\), and let

\[
e_r(|a|)=\sum_{i_1<\cdots<i_r}
          \prod_{\ell=1}^r|a_{i_\ell}|.
\]

For \(0\le d\le r\),

\[
\sum_{i_1<\cdots<i_r}
\left|
\partial_h^d\prod_{\ell=1}^r\varepsilon_{i_\ell}
\right|
\le
A_N^d\,\frac{\tau^{r-d}}{(r-d)!}.                  \tag{4.1}
\]

#### Proof

For each ordered \(r\)-tuple,

\[
\left|
\partial_h^d\prod_{\ell=1}^r\varepsilon_{i_\ell}
\right|
=\frac{r!}{(r-d)!}|h|^{r-d}
\prod_{\ell=1}^r|a_{i_\ell}|.
\]

The elementary symmetric bound

\[
e_r(|a|)\le\frac{A_N^r}{r!}
\]

therefore gives

\[
\frac{r!}{(r-d)!}|h|^{r-d}e_r(|a|)
\le
\frac{A_N^d(|h|A_N)^{r-d}}{(r-d)!}.
\]

Since \(|h|A_N=\tau\), this is (4.1). \(\square\)

## 5. Cross-radius causal propagator

For a positive source-order sequence

\[
\|b\|_\rho=\sum_{m\ge0}\frac{\rho^m}{m!}b_m,
\]

let \(S\) be the left shift, \((Sb)_m=b_{m+1}\). The exact Cauchy estimate
is

\[
\|S^kb\|_{\rho'}
\le\frac{k!\rho}{\delta^{k+1}}\|b\|_\rho,
\qquad k\ge1.                                     \tag{5.1}
\]

### Theorem 5.1

Suppose the positive majorant of the total finite branching of one
response-shift transition is \(CS\). Sum the pure response-shift skeleton
allowed by Lemma 3.1, with all non-shift kernels held as its edge
decorations, and let
\(\partial_h^{[d]}\) act on exactly \(d\) of their explicit chronological
factors. Assume \(\max_i|\varepsilon_i|\le1\), so additional
chronological factors may be erased in forming an upper majorant. Then
(1.1) holds.

#### Proof

Retain the \(r=k-1\) charged factors supplied by Lemma 3.1 and erase any
additional factors, which is a valid positive majorization under the
small-step assumption. Only \(r\ge d\) contributes. Lemma 4.1 and (5.1)
give

\[
\begin{aligned}
\|\partial_h^{[d]}P_N^{\mathrm{resp}}(h)V\|_{\rho'}
&\le
\sum_{r\ge d}
C^{r+1}A_N^d\frac{\tau^{r-d}}{(r-d)!}
\frac{(r+1)!\rho}{\delta^{r+2}}\|V\|_\rho .
\end{aligned}                                      \tag{5.2}
\]

Put \(\ell=r-d\) and \(x=C\tau/\delta\). The right side becomes

\[
A_N^d
\frac{\rho C^{d+1}}{\delta^{d+2}}
\sum_{\ell\ge0}\frac{(\ell+d+1)!}{\ell!}x^\ell
\|V\|_\rho .
\]

The binomial generating function gives

\[
\sum_{\ell\ge0}\frac{(\ell+d+1)!}{\ell!}x^\ell
=\frac{(d+1)!}{(1-x)^{d+2}},
\qquad |x|<1.                                     \tag{5.3}
\]

Substitution proves (1.1). \(\square\)

For \(d=0\), Theorem 5.1 reserves exactly one unweighted terminal/current
shift and gives

\[
\|P_N^{\mathrm{resp}}(h)V\|_{\rho'}
\le
\frac{\rho C}{\delta^2(1-C\tau/\delta)^2}\|V\|_\rho.
\tag{5.4}
\]

If the identity branch is included, add \(\|V\|_\rho\) to the right of
(5.4). Extra chronological non-response transitions are not included in
\(P_N^{\mathrm{resp}}\); controlling their nonlinear and stochastic
decorations is precisely the separate product/tail problem stated in
Section 6.

For \(d\le3\), (1.3) turns \(A_N^d\) into the required \(t^d\) and no
larger horizon power.

## 6. A horizon-uniform multiplicative Gaussian lemma

The following lemma is the precise pathwise substitute for an
ever-doubling Hölder tower.

### Lemma 6.1

Let \(c\ge0\), and let \(G_0,\ldots,G_{N-1}\) be jointly centered Gaussian, with
\(\mathbb E G_s^2\le V^2\), and let \(w_s\ge0\),
\(\tau=\sum_sw_s\). Suppose nonnegative random variables obey

\[
X_{s+1}
\le\{1+c w_s(1+|G_s|)\}X_s+w_sB_s.                \tag{6.1}
\]

Then, for every \(p\ge1\),

\[
\boxed{
\|X_N\|_p
\le
2^{1/(2p)}
\exp\{c\tau+p c^2\tau^2V^2\}
\left\|X_0+\sum_{s<N}w_sB_s\right\|_{2p}.
}
\tag{6.2}
\]

The constant is independent of \(N\) and does not require independence
among the \(G_s\).

#### Proof

Since \(1+x\le e^x\), discrete variation of constants in (6.1) gives

\[
X_N
\le
\left(X_0+\sum_{s<N}w_sB_s\right)
\exp\left\{c\tau+c\sum_{s<N}w_s|G_s|\right\}.       \tag{6.3}
\]

Convexity of the exponential gives, for every \(\lambda\ge0\),

\[
\mathbb E\exp\left(\lambda\sum_sw_s|G_s|\right)
\le
2\exp\left(\frac{\lambda^2\tau^2V^2}{2}\right).     \tag{6.4}
\]

Indeed, when \(\tau>0\), bound the exponential of the weighted average by
the weighted average of
\(\exp(\lambda\tau|G_s|)\), then use the one-dimensional Gaussian
estimate; the case \(\tau=0\) is immediate. Apply Hölder to (6.3) with
exponents \(2,2\), and use (6.4) with \(\lambda=2pc\). This gives

\[
\begin{aligned}
\|X_N\|_p
&\le
\left\|X_0+\sum_sw_sB_s\right\|_{2p}
e^{c\tau}
\left\|e^{c\sum_sw_s|G_s|}\right\|_{2p}\\
&\le
2^{1/(2p)}
e^{c\tau+p c^2\tau^2V^2}
\left\|X_0+\sum_sw_sB_s\right\|_{2p},
\end{aligned}
\]

which is (6.2). \(\square\)

Thus any exact tangent block reduced to (6.1) has horizon-uniform finite
moments at each required \(p\), with no recursive exponent doubling.
For the \(L=2\) DAG, the raw families \(\xi_s,\chi_s\) already satisfy
the variance premise by the width-first \(L^2\) energy estimate.

## 7. Exact scope

Lemma 3.1 and Theorem 5.1 prove the first graph-specific assertion needed
by a decreasing-radius OMFP proof: repeated unweighted current
contractions cannot occur consecutively, and common-step differentiation
costs at most one additional unweighted shift per derivative.

Lemma 6.1 proves uniform moment propagation once a coupled tangent block
has been reduced to the scalar multiplicative form (6.1). It does not
perform that reduction for the mutually dependent \(\bar\rho,\bar\sigma\)
kernels. In particular, the present results do not bound all nonlinear
kernels decorating the response edges.
In particular, this note does not prove uniform moment/tail propagation
for products such as

\[
a_s\psi''(z_s)\zeta_s^i,\qquad
r_s\psi''(u_s)p_s^i.
\]

Thus the causal source-shift obstruction is resolved on the exact
\(L=2\) grammar, while the stochastic-tail/product block remains open.
The scalar \(Ct^4h^5\) theorem is not claimed here.
