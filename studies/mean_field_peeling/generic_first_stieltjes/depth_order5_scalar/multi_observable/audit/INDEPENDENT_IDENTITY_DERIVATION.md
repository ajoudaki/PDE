# Independent hostile derivation of observable identities

This note was written after the hostile contract was frozen but before inspecting
the producer's proposed `Gamma_04` recurrence.  It audits identities that do not
depend on that recurrence.

## 1. Universal parameter jets and an observable head

Let

\[
 p(\theta)=n\nabla f(\theta),\qquad D=p\cdot\nabla_\theta,
 \qquad \dot\theta=p(\theta).
\]

Ordinary differentiation of the flow gives the universal parameter jets

\[
 \theta^{(1)}=p,qquad \theta^{(2)}=Dp,qquad
 \theta^{(3)}=D^2p,qquad \theta^{(4)}=D^3p.
\]

They do not depend on the observable.  If `O` is a scalar observable, its first
four derivatives are the following observable-specific contractions:

\[
\begin{aligned}
 O'={}&O_1[p],\\
 O''={}&O_2[p,p]+O_1[Dp],\\
 O'''={}&O_3[p,p,p]+3O_2[p,Dp]+O_1[D^2p],\\
 O^{(4)}={}&O_4[p,p,p,p]+6O_3[p,p,Dp]+3O_2[Dp,Dp]\\
 &\quad+4O_2[p,D^2p]+O_1[D^3p],
\end{aligned}
\]

where `O_r` denotes the symmetric `r`-th derivative tensor evaluated at
initialization.  Thus an amortized compiler may reuse the parameter-flow jets and
their already contracted MFP backbone, while each new observable supplies only
the derivative tensors and contractions its head needs.  This is an exact
finite-width statement.  It does not by itself prove that a proposed finite set
of averaged scalar contractions closes after Wick--Stein reduction.

## 2. Hidden activation Gram

Put `X^(r)=D^r x^ell|_0`.  The finite-width product rule gives

\[
 \frac{d^k}{ds^k}\frac{\langle x^\ell,x^\ell\rangle}{n}\bigg|_{0}
 =\frac1n\sum_{r=0}^k{k\choose r}
   \langle X^{(r)},X^{(k-r)}\rangle.                 \tag{2.1}
\]

Whenever the limits of the individual expectations exist and the finite sum may
be passed through the limit, (2.1) yields

\[
 Q_\ell^{(k)}(0)=\sum_{r=0}^k{k\choose r}\Gamma^\ell_{r,k-r}. \tag{2.2}
\]

Symmetry of the inner product gives `Gamma_rs=Gamma_sr`.  Consequently

\[
 Q_\ell''=2\Gamma_{02}+2\Gamma_{11},                 \tag{2.3}
\]

and

\[
 Q_\ell^{(4)}=2\Gamma_{04}+8\Gamma_{13}+6\Gamma_{22}. \tag{2.4}
\]

Thus the proposed dictionary

\[
 \Gamma_{11}=w_\ell,quad \Gamma_{02}=q02_\ell,quad
 \Gamma_{22}=q22_\ell,quad \Gamma_{13}=q13_\ell
\]

implies

\[
 Q_\ell''=2(w_\ell+q02_\ell),qquad
 Q_\ell^{(4)}=2\gamma04_\ell+8q13_\ell+6q22_\ell,
\]

provided the dictionary itself is verified against the backbone definitions.
Equations (2.1)--(2.4) are exact independently of that verification.

## 3. Readout-reflection parity

Let `T` negate only the Gaussian readout weights.  It is an orthogonal involution,
the initialization law is invariant under `T`, and

\[
 f(T\theta)=-f(\theta),\qquad p(T\theta)=-T p(\theta).
\]

If `theta(s;theta0)` is the feature-ascent trajectory, uniqueness of the finite
dimensional smooth ODE gives

\[
 \theta(s;T\theta_0)=T\theta(-s;\theta_0).           \tag{3.1}
\]

Hidden activations are invariant under applying `T` at a fixed parameter point,
so (3.1) implies

\[
 x^\ell(s;T\theta_0)=x^\ell(-s;\theta_0),\qquad
 X_\ell^{(r)}(T\theta_0)=(-1)^rX_\ell^{(r)}(\theta_0). \tag{3.2}
\]

Therefore every annealed hidden-activation Gram or RMS is even in `s`; all its
odd feature-ascent derivatives vanish.  More locally,
`E Gamma^ell_rs=0` whenever `r+s` is odd.  This is exact at finite width after
taking expectation.  It is not a samplewise assertion for one initialization.

## 4. RMS derivatives

Under unit Gram `Q_ell(0)=1`.  Write

\[
 Q_\ell(s)=1+\frac{q_2}{2}s^2+\frac{q_4}{24}s^4+O(s^6),
\]

using the parity just proved.  Expanding `sqrt(1+x)=1+x/2-x^2/8+O(x^3)` gives

\[
 R_\ell''=\frac{q_2}{2},\qquad
 R_\ell^{(4)}=\frac{q_4}{2}-\frac34q_2^2.            \tag{4.1}
\]

Substitution of (2.3)--(2.4) yields

\[
 R_\ell''=w_\ell+q02_\ell,
\]

\[
 R_\ell^{(4)}=\gamma04_\ell+4q13_\ell+3q22_\ell
              -3(w_\ell+q02_\ell)^2.                \tag{4.2}
\]

## 5. Exact label-one MSE time composition

Let `s(0)=0` and

\[
 \dot s=c(1-F(s)),\qquad c=2\eta.
\]

Readout parity gives `F(0)=F''(0)=F^(4)(0)=0`.  With
`A=F'(0)` and `B=F'''(0)`, repeated differentiation at zero gives

\[
\begin{aligned}
 s_1&=c,\\
 s_2&=-c^2A,\\
 s_3&=c^3A^2,\\
 s_4&=-c^4(A^3+B),\\
 s_5&=c^5(A^4+7AB).
\end{aligned}                                      \tag{5.1}
\]

For an even `Q(s)` with `q2=Q''(0)`, `q4=Q^(4)(0)`, the chain rule and (5.1)
then give

\[
\begin{aligned}
 Q_t''(0)&=c^2q2,\\
 Q_t'''(0)&=-3c^3Aq2,\\
 Q_t^{(4)}(0)&=c^4(q4+7A^2q2),\\
 Q_t^{(5)}(0)&=-5c^5\big((3A^3+B)q2+2Aq4\big).
\end{aligned}                                      \tag{5.2}
\]

The coefficient `C=F^(5)(0)` first enters `s_6`, so its absence from (5.2) is
required, not accidental.

## 6. Order-seven free-tree family count: roadmap evidence only

Suppressing the harmless global powers of `n`, a contraction monomial in
`D^k f` can be represented by a free tree: each vertex is a derivative tensor of
`f`, each incident edge consumes one tensor index, and every edge contracts a pair
of indices.  Initially `f` is the one-vertex tree.  When `D=grad(f) dot grad`
differentiates a tensor at vertex `v`, it raises that tensor's rank by one and
contracts the new index with a new `grad f`; graphically it attaches one leaf to
`v`.  Induction therefore identifies the raw contraction *shapes* in `D^k f`
with unlabeled free trees on `k+1` vertices.  Every shape occurs with a positive
integer coefficient because it has at least one leaf-removal growth history, so
there are no cancellations between shapes.

As an independent enumeration check, Prüfer sequences were converted to trees and
canonicalized by the standard center/rooted-parenthesis code.  The numbers of
unlabeled free trees for `2,...,8` vertices were

\[
 1,1,2,3,6,11,23.
\]

Thus the abstract raw `D^7 f` shape count is 23.  This does **not** construct the
23 tensor formulas with coefficients, perform their width/Wick audit, or establish
an order-seven MFP recurrence.  In the authoritative report it belongs only in the
order-seven roadmap until those additional obligations are completed.

