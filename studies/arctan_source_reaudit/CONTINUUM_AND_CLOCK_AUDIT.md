# Independent audit of the arctangent OMFP continuum and clock

Status: PASS for the exact finite algebra, autonomous IDE, Gaussian-envelope
existence/uniqueness, kernel identity, and signed physical-time reduction.
This audit does not replace the separate audit of the finite-program source
theorem and width-identification argument.

## 1. Finite system and exact natural coordinate

On \(H_n=\mathbb R^n\), let
\(\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w\), and put

\[
 X=\phi(u),\quad Z=GX,\quad Y=\phi(Z),\quad
 f_n=\langle A,Y\rangle_n,
 \qquad \phi(x)=\arctan x.
\]

The \(A,u\) blocks carry the normalized Hilbert metric and the \(G\) block
the ordinary Frobenius metric.  If

\[
 c(u)=\phi'(u)=\frac1{1+u^2},\qquad
 d(Z)=\frac1{1+Z^2},\qquad B=A\odot d(Z),\qquad Q=G^*B,
\]

then direct differentiation gives

\[
 df_n=\langle Y,dA\rangle_n+
 \operatorname{tr}\!\left[\left(n^{-1}BX^{\mathsf T}\right)^{\mathsf T}dG\right]
 +\langle c(u)Q,du\rangle_n.
\]

Thus feature ascent is

\[
 A'=Y,\qquad u'=c(u)Q,\qquad G'=n^{-1}BX^{\mathsf T}.
\]

Define

\[
 \Theta(u)=u+u^3/3,\qquad r=\Theta(u),\qquad \iota=\Theta^{-1}.
\]

Since \(\Theta'=1/c\), the transformed equation is exactly \(r'=Q\).
With \(\Psi(r)=\arctan\iota(r)\), one has
\(\iota'=c\) and \(\Psi'=c^2\).  Therefore, writing
\((b\otimes x)v=b\langle x,v\rangle_n\),

\[
 A'=Y,\qquad r'=Q,\qquad G'=B\otimes X.
\]

No gradient rule has been changed: this is an invertible coordinate change.
Furthermore,

\[
 X'=c(r)^2Q,
 \qquad
 Z'=B\langle X^2\rangle_n+G\{c(r)^2Q\}.
\]

Consequently

\[
 f_n'=
 \langle Y^2\rangle_n+
 \langle B^2\rangle_n\langle X^2\rangle_n+
 \langle c(r)^2Q^2\rangle_n=:K_n\ge0.
\]

This is also the sum of the three squared block-gradient norms, so the
normalization and sign are independently fixed.

## 2. Autonomous OMFP IDE

Let the immutable pointed Gaussian action source be
\((H_R,H_C;a_0,r_0,\Gamma)\), where
\(r_0=u_0+u_0^3/3\), and retain the trained part as one current trace-class
operator \(q\).  Set \(G=\Gamma+q\).  The feature IDE is

\[
 A'=Y,\qquad r'=Q,\qquad q'=B\otimes X,
\]

where all pointwise fields are recomputed from the current state and the
same \(\Gamma\).  Since
\(\|B\otimes X\|_1=\|B\|_2\|X\|_2\), this vector field maps
\(L^2_R\times L^2_C\times\mathfrak S_1\) into itself.  The current \(q\)
compresses the complete learned rank-one history; no fresh Gaussian action
may replace \(\Gamma\) or \(\Gamma^*\).

## 3. Global feature-time well-posedness

Let \(a=\pi/2\).  Along every solution,

\[
 |A(s)-a_0|\le a|s|,
 \]

pointwise.  Hence \(A=a_0+\alpha\) with \(\alpha\) bounded on compact
feature intervals.  Also

\[
 \|A(s)\|_2\le\|a_0\|_2+a|s|,
 \qquad
 \|q(s)\|_1\le
 a\int_0^{|s|}\|A(\sigma)\|_2\,d\sigma,
\]

and

\[
 \|r(s)\|_2\le\|r_0\|_2+
 \int_0^{|s|}\|\Gamma+q(\sigma)\|_{\rm op}
 \|A(\sigma)\|_2\,d\sigma.
\]

These bounds preclude finite feature-time escape.

For uniqueness, the only map that is not locally Lipschitz in the ambient
\(L^2\) topology is \((A,Z)\mapsto A d(Z)\).  If \(a\) is sub-Gaussian and
\(h\) is bounded and Lipschitz, set \(w=h(z)-h(\widetilde z)\) and
\(\delta=\|z-\widetilde z\|_2\).  For \(p\ge2\),

\[
 \|aw\|_2
 \le \|a\|_{2p}\|w\|_{2p/(p-1)}
 \le C\sqrt p\,(L\delta)^{1-1/p}(2\|h\|_\infty)^{1/p}.
\]

Taking \(p\asymp\log(e/\delta)\) yields

\[
 \|a\{h(z)-h(\widetilde z)\}\|_2
 \le C\omega(\delta),\qquad
 \omega(\delta)=\delta\sqrt{\log(e/\delta)}
\]

for small \(\delta\), with a harmless increasing extension away from zero.
Moreover

\[
 \int_{0^+}\frac{d\delta}{\omega(\delta)}=\infty.
\]

For two Gaussian-envelope states, put

\[
 D=\|A-\widetilde A\|_2+\|r-\widetilde r\|_2+
 \|q-\widetilde q\|_1.
\]

Bounded functional calculus and the trace-to-operator inequality first give
\(\|X-\widetilde X\|_2+\|Z-\widetilde Z\|_2+
\|Y-\widetilde Y\|_2\le C D\).  Decomposing

\[
 B-\widetilde B=(A-\widetilde A)d(Z)+
 \widetilde A\{d(Z)-d(\widetilde Z)\}
\]

and applying the preceding multiplier bound to
\(\widetilde A=a_0+\widetilde\alpha\) gives

\[
 \|B-\widetilde B\|_2\le C\{D+\omega(CD)\}.
\]

The identities

\[
 Q-\widetilde Q=G^*(B-\widetilde B)
 +(q-\widetilde q)^*\widetilde B
\]

and

\[
 \|B\otimes X-\widetilde B\otimes\widetilde X\|_1
 \le\|B-\widetilde B\|_2\|X\|_2+
 \|\widetilde B\|_2\|X-\widetilde X\|_2
\]

then yield

\[
 D(s)\le D(0)+C_S\int_0^{|s|}
 \{D(\sigma)+\omega(C_SD(\sigma))\}\,d\sigma.
\]

The reciprocal integral of the modulus diverges, so Bihari--Osgood gives
uniqueness and continuous dependence.  Existence follows by clipping
\(a_0\), applying Picard--Lindelof to the bounded-multiplier system, and
then removing the clip.  The comparison may be oriented as

\[
 B_N-B_M=(A_N-A_M)d(Z_N)+A_M\{d(Z_N)-d(Z_M)\},
\]

so its Lipschitz constant grows only like \(C_SM\).  Hence

\[
 D(U_N,U_M)\le C_Se^{C_SM}\|a_0^{(N)}-a_0^{(M)}\|_2.
\]

The Gaussian clipping tail is
\(O((1+M)e^{-M^2/4})\), which beats \(e^{C_SM}\).  This closes existence,
not merely uniqueness of hypothetical solutions.

Strong continuity of the state and the same multiplier estimate imply
strong continuity of \(B,Q\).  The chain rule therefore gives, in the
limit,

\[
 F'(s)=K(s)\ge0,
\]

with finite continuous \(K\).

## 4. Signed physical MSE clock

For the full MSE \(\mathcal L=(y-F)^2\), loss-gradient descent is a signed
time change of feature ascent.  Define

\[
 \dot s=2\eta e,qquad e=y-F(s),\qquad s(0)=0.
\]

Since \(F\in C^1\), this scalar ODE is locally well posed.  Using
\(F'=K\ge0\),

\[
 \dot e=-2\eta eK(s),
 \qquad
 e(t)=y\exp\!\left[-2\eta\int_0^tK(s(\tau))\,d\tau\right].
\]

This formula is valid for positive, zero, and negative labels.  In
particular, the sign of \(e\) is preserved,
\(|e(t)|\le|y|\), and

\[
 |s(t)|\le2\eta|y|t.
\]

Thus the global two-sided feature solution supplies a unique global
physical trajectory.  Negative labels merely make \(s(t)\) decrease.
The physical state equations are

\[
 \dot A=2\eta eY,\qquad
 \dot r=2\eta eQ,\qquad
 \dot q=2\eta e(B\otimes X),\qquad
 \dot e=-2\eta eK.
\]

Finally,

\[
 \frac d{dt}(F(s(t))+e(t))=0,
\]

so \(F(s(t))+e(t)=y\), and

\[
 \dot{\mathcal L}=-4\eta K\mathcal L.
\]

## 5. Audit conclusion and boundary

No algebraic, analytic, sign, or negative-label flaw was found in these
parts of the proof.  In particular, the argument does not assume ambient
Frechet-Lipschitzness on an \(L^2\) ball; it uses the Gaussian-envelope
Osgood modulus.  The conclusion is uniqueness in that reachable envelope
class, not uniqueness for arbitrary \(L^2\) initial fields.  A complete
finite-width convergence theorem additionally needs the independently
proved pointed-action source theorem, Euler-program width identification,
and square-uniform-integrability argument for \(Q=G^*B\).
