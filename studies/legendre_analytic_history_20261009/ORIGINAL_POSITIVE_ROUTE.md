# Unchanged Legendre method: prediction cancellation and the startup interval

This bounded calculation concerns exactly the original method in
`paper/compact_legendre.tex`: the clock starts at one, its physical-time
velocity is residual RMS, the forward prefix is constant, the backward
prefix is zero, and neither the clock nor the method is changed. There
are no restarts, frozen layers, fitted source coefficients, or adapted
response directions. The earlier window construction is not used here.

The search for a prediction-level improvement gives a useful cancellation:
the first discrepancy in predictions occurs at fifth order in physical
time, although the hidden parameter discrepancy occurs at fourth order.
However, its fifth-order coefficient has a nonzero deterministic
infinite-width limit, including for tanh. Thus this particular coefficient
does not receive an inverse-square-root-width gain. A uniform remainder
estimate remains necessary before turning the calculation into a
growing-order lower bound. This note does not claim that missing estimate.

## The exact projection defect and the two initial cancellations

Write hats for the unchanged Legendre model and no hats for dense flow,
with their common realized initialization. The network and mobilities are
those of the paper. For the original clock define the history functions

\[
h_a(\tau(t))=\widehat h_a(t),\qquad
b_a(\tau(t))=\frac{\widehat r_a(t)}{\widehat\rho(t)}
                  \widehat\delta_a(t),\qquad
\widehat\rho=\|\widehat r\|_2/\sqrt m.
\]

On \([0,1]\), these histories equal \(h_{0,a}\) and zero. These
definitions are proof objects; the actual stored-state equations contain
no division by a residual. At positive residual the original exact
defect is

\[
\dot{\widehat W}^{(\ell)}
=-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(\ell)}
                       \widehat h_a^{(\ell-1)\top}
+\mathcal E_\ell,
\qquad
\mathcal E_\ell=\frac{2\widehat\rho}{mn}
\sum_a e_{b,a}^{(\ell)}e_{h,a}^{(\ell-1)\top},
\tag{1}
\]

where \(e_g=g(\tau)-(\Pi_q^\tau g)(\tau)\).

At initialization the readout vanishes. Consequently all backward
responses and all feature velocities vanish. Writing \(\eta=\tau-1\),
the right-hand histories therefore have expansions

\[
b_a(1+\eta)=B_a\eta+O(\eta^2),\qquad
h_a(1+\eta)=h_{0,a}+\tfrac12H_a\eta^2+O(\eta^3),
\tag{2}
\]

where \(B_a=\partial_\tau b_a(1+)\) and
\(H_a=\partial_\tau^2h_a(1+)\). In general the backward history is
only continuous at the prefix join, and the forward history has only its
first derivative matched there.

The degree-below-\(q\) endpoint kernel satisfies the elementary bound

\[
|K_q^A(A,\xi)|
\le\frac1A\sum_{j<q}(2j+1)=\frac{q^2}{A},
\quad A=1+\eta,
\]

because \(|P_j|\le1\) on the real interval. The nonconstant pieces in
(2) have support of length \(\eta\). Integrating their size against this
kernel shows, for fixed width and order as \(\eta\downarrow0\),

\[
e_{b,a}=B_a\eta+O_{n,q}(\eta^2),\qquad
e_{h,a}=\tfrac12H_a\eta^2+O_{n,q}(\eta^3).
\tag{3}
\]

The projected onset terms themselves are bounded by constants times
\(q^2\eta^2\) and \(q^2\eta^3\), respectively. This identifies
\(q^2\eta\) as the first natural dimensionless parameter for this
startup interval, although it is not yet a uniform bound on the nonlinear
remainders in (2).

Substitution into (1) gives a hidden forcing beginning at third order in
time and a hidden parameter discrepancy beginning at fourth order. The
prediction Jacobian in a hidden block contains the backward response,
which is itself first order in time. This explains why the first direct
prediction discrepancy begins at fifth order. Its actual coefficient
must also include the resulting change of the readout evolution.

## A full fifth-order calculation for tanh

Take \(L=m=d=2\), \(v_1=e_1,v_2=e_2\), and labels
\(y=(y_*,0)\) with \(y_*>0\). Both activations are tanh. Orthogonality
and oddness give a positive diagonal population top Gram, so the setup
is admissible when \(y_*\) is chosen sufficiently small to satisfy the
paper's label cap. Let

\[
\begin{aligned}
h&=\tanh(W_0^{(1)}e_1),&
p&=\operatorname{sech}^2(W_0^{(1)}e_1),\\
z&=W_0^{(2)}h,&
g&=\tanh z,&s&=\operatorname{sech}^2z.
\end{aligned}
\]

These are initialized vectors in \(\mathbb R^n\), and all products below
between equal-length vectors are componentwise unless explicitly
transposed. Define the two physical derivatives

\[
u=\dot\delta_1^{(2)}(0)=y_*g\odot s,
\qquad
c=\ddot h_1^{(1)}(0)
=y_*p^{\odot2}\odot W_0^{(2)\top}u.
\tag{4}
\]

Indeed \(\dot w(0)=y_*g\), and differentiating the first-layer gradient
equation once gives
\(\ddot W^{(1)}(0)e_1=y_*p\odot W_0^{(2)\top}u\).
Multiplication by the first activation derivative gives the second
identity in (4). These derivatives are common to dense and Legendre
flows. The second sample has zero label, so its backward history has no
linear onset and it does not contribute to the leading defect.

Since \(Y=y_*/\sqrt2\), conversion of (2)--(3) back to physical time
in (1) cancels the clock factors and yields

\[
\mathcal E_2(t)=-\frac{y_*}{2n}u c^\top t^3+O_{n,q}(t^4).
\tag{5}
\]

Let \(\Delta W^{(2)}=\widehat W^{(2)}-W^{(2)}\) and similarly for
other variables. Subtracting the physical equations gives

\[
\Delta W^{(2)}(t)
=-\frac{y_*}{8n}u c^\top t^4+O_{n,q}(t^5).
\tag{6}
\]

The first-layer discrepancy is \(O_{n,q}(t^6)\): the changed hidden
matrix in a backward response is multiplied by the first-order readout,
and the other response changes occur no earlier. The current top-feature
discrepancy at sample one is therefore

\[
\Delta h_1^{(2)}(t)
=-\frac{y_*}{8n}(c^\top h)(s\odot u)t^4+O_{n,q}(t^5).
\]

The readout update has leading residual \(-y_*\). Its resulting change
is

\[
\Delta w(t)
=-\frac{y_*^2}{40n}(c^\top h)(s\odot u)t^5
+O_{n,q}(t^6).
\tag{7}
\]

Terms caused by the residual discrepancy enter the readout equation only
at fifth order and therefore do not alter (7). The direct hidden-matrix
contribution to the prediction is

\[
\frac{(t u)^\top\Delta W^{(2)}(t)h}{n}
=-\frac{y_*}{8n^2}\|u\|_2^2(c^\top h)t^5+O_{n,q}(t^6).
\]

The readout contribution follows from (7) and
\(g^\top(s\odot u)=\|u\|_2^2/y_*\). Adding them gives

\[
\widehat f(t,x_1)-f_n(t,x_1)
=-\frac{3y_*}{20}
  \frac{\|u\|_2^2}{n}\frac{c^\top h}{n}\,t^5
+O_{n,q}(t^6).
\tag{8}
\]

This coefficient is independent of \(q\). It includes the readout
feedback, which contributes one fifth of the direct hidden-parameter
term, with the same sign. Integrating only the instantaneous prediction
forcing from (5) would not give the correct coefficient.

For every fixed \(n,q\), the local expansion is justified by smoothness
of the original stored-state equations near the initial state:
\(\tau=1>0\) and \(\rho=Y>0\), so there is no singularity in the
norm or denominator in this neighborhood. This observation alone gives
no uniform size for the remainder neighborhood as \(n,q\) vary.

## The coefficient has no width suppression

Let \(U\sim N(0,1)\), and define the positive constants

\[
Q=\mathbb E\tanh^2U,\qquad
C=\mathbb E[\tanh^2U\operatorname{sech}^4U].
\]

Let \(Z\sim N(0,Q)\), and put
\(\psi(Z)=\tanh Z\operatorname{sech}^2Z\). Conditional on the first
layer, the rows of \(W_0^{(2)}\) are independent Gaussian vectors.
Thus the ordinary conditional law of large numbers and the first-layer
law of large numbers give

\[
\frac{\|u\|_2^2}{n}\longrightarrow
y_*^2\mathbb E\psi(Z)^2>0
\quad\hbox{in probability}.
\tag{9}
\]

For the other factor, put \(a=p^{\odot2}\odot h\). From (4),

\[
\frac{c^\top h}{n}
=\frac{y_*^2}{n}\sum_{i=1}^n
\psi((W_0^{(2)}h)_i)(W_0^{(2)}a)_i.
\]

Conditionally, the two Gaussian row products have variance
\(Q_n=\|h\|^2/n\) and covariance \(C_n=h^\top a/n\).
Gaussian regression therefore gives their product expectation
\((C_n/Q_n)\mathbb E[Z_n\psi(Z_n)]\), where
\(Z_n\sim N(0,Q_n)\). The first-layer laws give
\(Q_n\to Q\) and \(C_n\to C\). The summands have uniformly bounded
conditional second moments because \(\psi\) and the entries of \(a\)
are bounded. Conditional Chebyshev, followed by continuity of the
one-dimensional Gaussian expectation, proves

\[
\frac{c^\top h}{n}\longrightarrow
y_*^2\frac C Q\mathbb E[Z\psi(Z)]>0
\quad\hbox{in probability}.
\tag{10}
\]

Both strict inequalities hold because their integrands are positive
except on sets of Gaussian measure zero. The fifth-order coefficient in
(8) consequently converges in probability to

\[
-\frac{3y_*^5}{20}\frac C Q
  \mathbb E\psi(Z)^2\,\mathbb E[Z\psi(Z)]<0.
\tag{11}
\]

In particular, cancellation or random-neuron averaging does not supply
an \(n^{-1/2}\) factor for this startup coefficient. This is stronger
than observing nonanalyticity of the histories, but weaker than an
all-width/order lower bound on the trajectory norm.

As an independent normalization check, replacing both activations by the
identity and writing
\(G=W_0^{(1)\top}W_0^{(2)\top}W_0^{(2)}W_0^{(1)}/n\) gives, for
\(m=d=2\) and any label vector,

\[
\widehat f(t)-f_n(t)
=-\frac3{20}\|y\|_2^2(y^\top Gy)Gy\,t^5+O_{n,q}(t^6).
\]

Here \(G\to I_2\) in probability, confirming the same deterministic
bias mechanism for linear activations.

## The precise uniform bridge that remains

To convert (8)--(11) into a lower bound against a polylogarithmic choice
of \(q=q(n)\), it would suffice to prove, on events of probability
tending to one, constants \(p,s,C_*>0\) independent of \(n,q\) such
that for \(0\le t\le[q^p\log(en)^s]^{-1}\),

\[
\left|\widehat f(t,x_1)-f_n(t,x_1)+c_n t^5\right|
\le C_*q^p\log(en)^s t^6,
\qquad
c_n=\frac{3y_*}{20}\frac{\|u\|^2}{n}\frac{c^\top h}{n}.
\tag{12}
\]

The positive limit of \(c_n\) would then allow a sufficiently small
constant multiple of \(q^{-p}\log(en)^{-s}\) as witness time, producing
a lower bound of order \(q^{-5p}\log(en)^{-5s}\). For any fixed
polylogarithmic order this exceeds \(n^{-1/2}\) times any fixed power
of \(\log n\) eventually. The positive label coefficient can be very
small, so this asymptotic mechanism need not be visible at experimentally
accessible widths.

The Legendre kernel estimate above accounts for polynomial dependence on
\(q\) in the direct onset projection. It does not prove (12) for the
nonlinear closed flow. A naive analytic Picard argument in the RMS
parameter norm loses a factor \(\sqrt n\) when enforcing the coordinate
strip for tanh. The paper's dense carrier bound controls the reference
trajectory, not the original Legendre trajectory's coordinate derivatives.
Neither of those existing estimates, by itself, gives (12).

Thus the two candidate positive mechanisms have a precise present status.
The prediction Jacobian does improve the startup order to five, and
the onset occupies a shrinking Legendre resolution interval. But the
surviving coefficient has a nonzero width limit. Establishing a useful
polylogarithmic theorem for the unchanged method would require a further
mechanism strong enough to resolve this startup calculation; establishing
the uniform remainder (12) would instead rule out that theorem in this
admissible tanh example. No such additional mechanism or uniform tanh
remainder is proved in this note.
