# Active gate primitives: exact cancellations and surviving products

Status: a stalled finite-pair route audit, not a new continuation
criterion or a negative theorem about the network. The calculations
concern the canonical finite-width ZERO-readout proxy and its fully
pruned reference. This note does not extend the result to the tiny
random initial readout.

Use normalized vector norms and inner products. Write
\(U=W^{(2)}\), \(V=\widehat W^{(2)}\),
\(h=h^{(1)}\), \(\widehat h=\widehat h^{(1)}\),
\(Q=I-P_E\), and \(d(z)=(1+z^2)^{-1}\).
The uncut active gate difference from the off-block note is
\[
 v=Q\,[d(z^{(2)})-d(\widehat z^{(2)})]\odot\widehat q^{(2)}.
 \tag{1}
\]
Its normalized \(L^1\) norm is at most \(C_Sd_E\), while its
normalized \(L^2\) norm is only bounded, not known to be small.

## 1. What a time primitive really removes

Put \(a(t)=\int_0^t v(s)\,ds\). Exact integration by parts gives
\[
 \int_0^t v\otimes h
       =a(t)\otimes h(t)-\int_0^t a\otimes h',
 \tag{2}
\]
\[
 \int_0^t (QV)^*v
       =(QV(t))^*a(t)-\int_0^t(QV')^*a.
 \tag{3}
\]
The rank-one convention is \(u\otimes w=uw^\top/n\), so its
Frobenius norm is \(\|u\|_n\|w\|_n\).
The coefficients and their time derivatives in (2)--(3) have
uniform bounds:
\[
 \|h\|_n\le a_0,\quad
 \|h'\|_n\le C_S,\quad
 \|V\|_{\rm op}+\|V'\|_{\rm op}\le C_S,
 \qquad a_0=\pi/2.
 \]
In particular the derivative bound for \(V'\) is just
\(\|\widehat\delta^{(2)}\|_n\|\widehat h\|_n\), not a
derivative of the middle gate. These identities do remove the
instantaneous multiplier \(v\) from propagation. They do not bound
\(\sup_t\|a(t)\|_n\), so they are not treated as a closed estimate.

This is the finite-pair counterpart of the bounded moving-range
mechanism: for
\(R_su=(U(s)^*u,u\otimes h(s))\), both \(R_s\) and \(R_s'\)
are bounded by primal estimates. It is not a separate solution
of the unresolved range equation.

## 2. Integrating the reference query leaves two L2 products

Let the coordinate vector
\[
 A(t)=\int_0^t Q\,[d(z^{(2)}(s))-d(\widehat z^{(2)}(s))]\,ds.
 \]
Since \(\widehat q^{(2)}(0)=0\), integration by parts gives
\[
 a(t)=A(t)\odot\widehat q^{(2)}(t)
          -\int_0^t A(s)\odot(\widehat q^{(2)})'(s)\,ds.
 \tag{4}
\]
The initial boundary would also vanish because \(A(0)=0\).
The established bounds imply
\[
 \|A(t)\|_n\le C_S\int_0^t d_E(s)\,ds,\quad
 \|A(t)\|_\infty\le t,\quad
 \|\widehat q^{(2)}\|_n+
       \|(\widehat q^{(2)})'\|_n\le C_S.
 \tag{5}
\]
Equation (4) therefore gives small \(L^1\) products and bounded
\(L^2\) products, but not small \(L^2\) products. The uniform
bound on the time derivative of the query does not remove this
specific spatial product. No assertion of failure for the actual
reachable pair is inferred from this lack of a bound.

## 3. The scalar characteristic and rank-memory commutator

All formulas in this section are restricted to \(E^c\).
Suppress the layer-two superscript, and put
\[
 m=\|h\|_n^2,\qquad g=Uh',\qquad
 \widehat m=\|\widehat h\|_n^2,\qquad
 \widehat g=V\widehat h'.
 \]
The exact forward equations are
\[
 z'=m\,d(z)q+g,\qquad
 \widehat z'=\widehat m\,d(\widehat z)\widehat q+\widehat g.
 \tag{6}
\]
Let \(F(z)=z+z^3/3\), \(Z=F(z)-F(\widehat z)\), and
\[
 c=\frac{z+\widehat z}
          {1+(z^2+z\widehat z+\widehat z^2)/3},\qquad |c|\le1.
 \]
Writing \(\Delta\) for actual minus reference gives
\[
 Z'=m\,\Delta q+\Delta m\,\widehat q
              +(1+z^2)\odot\Delta g+c\,\widehat g\odot Z.
 \tag{7}
\]
The large reference backward query is absent from the transport
coefficient in (7). This identity is finite dimensional; no
width-uniform \(L^2\) bound on the cubic vector \(Z\) is assumed.

The derivative part of \(\Delta g\) can be isolated using the
ACTUAL rank update. Set
\[
 H=U\Delta h,\qquad \kappa=\langle h,\Delta h\rangle_n.
 \]
Since \(U'=\delta^{(2)}\otimes h\),
\[
 H'=\kappa\,\delta^{(2)}+U(\Delta h)',\qquad
 \Delta g=H'-\kappa\,\delta^{(2)}+\Delta U\,\widehat h'.
 \tag{8}
\]
Multiply by \(1+z^2\), use
\(\delta^{(2)}=d(z)q\), and then use (6). The exact result is
\[
 \begin{split}
 (1+z^2)\odot\Delta g
 ={}&[(1+z^2)\odot H]'
       -\kappa q+(1+z^2)\odot(\Delta U\,\widehat h')\\
    &-2m\,z\,d(z)\odot q\odot H
       -2z\odot g\odot H.
 \end{split}
 \tag{9}
\]
There is no omitted rank-memory term in (9):
the derivative of \(U\) is exactly the scalar \(\kappa\) term,
and the derivative of \(1+z^2\) is exactly the last two terms.

The estimates \(|\kappa|\le a_0d_E\),
\(\|H\|_n\le C_Sd_E\), and
\(\|\Delta U\,\widehat h'\|_n\le C_Sd_E\) are available.
Thus \(\kappa q\) is \(L^2\)-small. But the actual weight
\(1+z^2\) on \(\Delta U\,\widehat h'\), and the last two products,
are not controlled in the needed norm. In particular
\(|z\,d(z)|\le1/2\) only turns the penultimate term into a
bounded coefficient times the UNCOMPRESSED product \(q\odot H\).
The new off-block lemma bounds specified Gaussian compressed
images of small-\(L^1\) vectors; no such image is present here.

## Outcome

No new small-\(L^2\) bound for the active primitive (1) was obtained.
The two attempted cancellations leave the explicit products (4)
and (9). Recovering \(\int v\otimes h\) by solving the active
matrix-difference equation for that same integral would merely
rewrite the unknown difference and is not used as an estimate.
These calculations do not close \(d_E\), do not re-estimate the
already controlled rare residual, and do not disprove global
continuation.
