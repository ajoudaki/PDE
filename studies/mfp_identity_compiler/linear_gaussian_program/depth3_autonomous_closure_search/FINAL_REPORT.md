# Depth-three compressed autonomous closure: current resolution

> **Superseded on 20 August 2026.**  The later cyclic/trace-ideal construction
> in `../depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md` resolves the
> existence question.  The Haar bridge is retained by one explicit fixed free
> source, while its trained change is one current trace-class spatial field.
> Pointed strong source convergence plus Picard stability supplies the missing
> positive-time bridge.  The negative route audit below remains valid for
> ordinary commuting marginal spectra, but its final “open” status is no longer
> current.

## Bottom line

No description satisfying the frozen contract was found.  The problem is
therefore **open**, not disproved.

What was obtained is an exact finite-width reduction that identifies the
new obstruction relative to depth two.  Three hidden layers leave an
independent Haar-orthogonal bridge between two conserved outer spectral
spaces.  Every natural depth-two-style construction either retains that
width-dependent bridge, replaces it by an abstract noncommutative operator,
or expands it into an unbounded alternating-word/two-time hierarchy.  Each
option is explicitly forbidden.

Because no admissible candidate was frozen, no depth-three derivative
artifact was opened and the preregistered comparison through
\(F^{(13)}(0)\) was not run.  A finite Taylor table cannot repair the missing
positive-time source in any case.

## 1. Model and exact finite-width equations

Assume equal hidden width \(n\), consistently with the depth-two model in the
chat.  With

\[
x=A/\sqrt n,\qquad D=V/\sqrt n,\qquad
B=W/\sqrt n,\qquad y=u/\sqrt n,
\]

the feature is \(f=x^TDB y\).  Feature-ascent time satisfies

\[
x'=DB y,\qquad
D'=x(By)^T,\qquad
B'=(D^Tx)y^T,\qquad
y'=B^TD^Tx.
\tag{1.1}
\]

These equations follow by differentiating all four raw maps in
\(f_n=n^{-2}A^TVWu\) and applying the common \(\mu\)P factor \(n\).

## 2. Exact conserved quantities

Direct differentiation proves that

\[
C_L=DD^T-xx^T,\qquad
C_M=D^TD-BB^T,\qquad
C_R=B^TB-yy^T
\tag{2.1}
\]

are constant.  Also

\[
\|x\|^2-\|y\|^2
\tag{2.2}
\]

is constant because both squared norms have derivative \(2f\).

This establishes the first requested obligation completely.  Unlike depth
two, however, the three constant matrices act on three different layer
spaces and are not jointly diagonalizable through the moving maps.

## 3. Strongest exact current-time reduction

Let

\[
P=DB,\qquad a=\|x\|^2,\qquad b=\|y\|^2,\qquad q=a+b.
\]

Then the four-map flow projects exactly to

\[
\begin{aligned}
x'&=Py,\\
y'&=P^Tx,\\
P'&=C_Lxy^T+xy^TC_R+qxy^T,\\
q'&=4x^TPy.
\end{aligned}
\tag{3.1}
\]

The prediction and feature kernel are direct:

\[
F=x^TPy,
\tag{3.2}
\]

\[
K=F'
=\|Py\|^2+\|P^Tx\|^2
+a\|By\|^2+b\|D^Tx\|^2\ge0.
\tag{3.3}
\]

System (3.1) is autonomous and restartable at finite width, but it is not
compressed: \(P\) has \(n^2\) entries.

## 4. The fixed-source bottleneck

Diagonalize the two constant outer invariants:

\[
C_L=U\Lambda U^T,\qquad C_R=VMV^T,
\]

and set \(X=U^Tx,\ Y=V^Ty,\ Q=U^TPV\).  Then

\[
X_i'=\sum_jQ_{ij}Y_j,\qquad
Y_j'=\sum_iQ_{ij}X_i,\qquad
Q_{ij}'=(\lambda_i+\mu_j+q)X_iY_j.
\tag{4.1}
\]

At initialization, Gaussian polar invariance gives exactly in distribution

\[
Q(0)=(\Lambda+XX^T)^{1/2}
H_n
(M+YY^T)^{1/2},
\tag{4.2}
\]

where \(H_n\) is an independent Haar orthogonal matrix.  The two outer
endpoint spectral measures separately have the explicit depth-two law

\[
d\rho_x(\lambda)=\frac34\delta_{-1/2}(d\lambda)
+\frac{\sqrt{\lambda(4-\lambda)}}{2\pi(1+2\lambda)}
\mathbf1_{(0,4)}(\lambda)d\lambda.
\tag{4.3}
\]

They do not determine \(H_n\).  For each fixed \(i,j\),
\((H_n)_{ij}\to0\) in probability because its variance is \(1/n\), while

\[
\|H_nv\|=\|v\|
\]

for every \(v\).  Consequently a pointwise or classical averaged kernel
limit is zero even though the bridge has an order-one effect.

Repeated differentiation of (4.1) produces arbitrarily long ordered
compositions alternating between the two outer spectral resolutions and
\(H_n,H_n^T\).  Retaining all of them is the forbidden word hierarchy;
retaining \(H_n\) is a forbidden width-dependent matrix.  No finite
classical source transform resumming them was derived.

Thus requested obligation 2—an explicit complete admissible initialization
source—remains open.

## 5. Independent checks of the same obstruction

Two other exact routes reach the same point.

First, the endpoint second derivative is

\[
\begin{aligned}
x''
&=C_L^2x+(a+b)C_Lx\\
&\quad+\bigl(\|By\|^2+x^TC_Lx+a^2+ab\bigr)x
-D C_M D^Tx.
\end{aligned}
\tag{5.1}
\]

The last conjugate is moving, with

\[
(D C_M D^T)'=x(D C_M By)^T+(D C_M By)x^T.
\]

Further differentiation generates additional ordered powers and
inter-layer actions.

Second, the directed four-cycle block matrix

\[
\mathcal Q=
\begin{pmatrix}
0&0&0&x^T\\
y&0&0&0\\
0&B&0&0\\
0&0&D&0
\end{pmatrix}
\]

obeys the exact polynomial equation

\[
\mathcal Q'=(\mathcal Q^3)^T,
\qquad
\mathcal Q^T\mathcal Q-\mathcal Q\mathcal Q^T=\text{constant}.
\tag{5.2}
\]

This is concise but inadmissible: \(\mathcal Q\) is a width-dependent
nonnormal operator, and its conserved self-commutator is noncentral.
Replacing it by an abstract limiting operator would hide precisely the
unbounded information forbidden by the contract.

These are failures of particular witnesses, not a nonexistence theorem.

## 6. Output, loss, and physical clock

This requested item is exact independently of the unresolved source.
For one sample, full-MSE flow is a scalar reparameterization of feature
flow:

\[
\frac{ds}{dt}=2\eta[y_\star-F(s)].
\tag{6.1}
\]

Hence, conditional on any future valid feature closure,

\[
f(t)=F(s(t)),\qquad
L(t)=[y_\star-F(s(t))]^2.
\tag{6.2}
\]

The scalar clock introduces no second training-time coordinate and can be
adjoined as a current residual state.

## 7. Status of the six requested obligations

| Obligation | Status |
|---|---|
| 1. Exact finite-width identities and conserved quantities | Proved: (1.1), (2.1), (2.2), (3.1), and (5.2) |
| 2. Explicit fixed initialization source | Open: outer marginal sources are explicit, but the Haar bridge has no admissible classical compression yet |
| 3. Autonomous current-time field equations | Open under the contract; (3.1)/(4.1) are exact but width-dependent |
| 4. Output, loss, physical clock | Proved conditionally on the feature trajectory: (3.2), (3.3), (6.1), (6.2) |
| 5. Well-posedness | Finite-width polynomial ODE is locally well posed on its maximal interval; no admissible continuum vector field exists yet to analyze |
| 6. Compact-time width-limit identification | Open because obligations 2--3 are unresolved |

## 8. Exact logical conclusion

The valid depth-two spectral closure does not presently generalize to an
admissible depth-three closure by any of the four independently examined
mechanisms.  The exact unresolved statement is:

> Does the asymptotic Haar bridge in (4.2), under the nonlinear update
> (3.1), admit a fixed finite collection of restartable scalar fields on a
> finite-dimensional classical source?

No argument here proves that the answer is negative.  Therefore the correct
answer to the requested existence problem is **open**.
