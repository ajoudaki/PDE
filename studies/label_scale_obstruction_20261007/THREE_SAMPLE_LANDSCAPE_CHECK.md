# Internal reconstruction check of the three-sample landscape theorem

2026-10-11. **PASS for Theorem 7 of DEPENDENT_INPUT_PUSH.md and the
dependencies used in its proof.** No mathematical correction is required.
This is a scoped internal proof audit, not a promotion review and not a
Gaussian training theorem. The checker read the three complete frozen
inputs below, reconstructed the relevant arguments, and used no numerical
experiment, outside scientific source, other study, or other review.

| Frozen input | Verified SHA-256 |
|---|---|
| DEPENDENT_INPUT_PUSH.md | 5c98619efefa4e1a8e3e3ac058d622b6f346d87f06bdfa31647c17e51805a7fb |
| DEPENDENT_GEOMETRY_RENEWAL.md | ebb431742e1c29087069ed778a74f0b64c6aac5381c8d1825a6976ab0e61c12e |
| TANH_NECESSARY_GEOMETRY.md | 770527741d5a9acf76cb9c44e917be8eb9894edff6f02fc03c922f3ecb795b0f |

The checked claim is: for every three pairwise nonparallel unit inputs,
every fixed label vector \(y\in\mathbb R^3\), and every finite width
\(n\ge3\), the loss of the stated two-hidden-layer tanh network has no
finite local minimum satisfying
\[
0<\mathcal L<\|y\|_2^2/3.
\]
Neither exclusion of all bad stationary points nor almost-sure avoidance
of their limiting sets follows from this check.

## 1. Setup, normalization, and constant-loss perturbations

The inputs form \(X=(x_1,x_2,x_3)\). The network is exactly
\[
U=\tanh(AX),\quad Z=WU,\quad H=\tanh Z,\quad
f=H^\top w/n,\quad r=f-y,\quad\mathcal L=\|r\|_2^2/3.
\]
Write \(E=1-U^2\), \(D=1-H^2\), and
\(T=\operatorname{diag}(w)D\operatorname{diag}(r)\).
All gates are positive at finite parameters. Direct differentiation gives
\[
Hr=0,\qquad TU^\top=0,\qquad
[E\odot(W^\top T)]X^\top=0
\]
at a stationary point. For an affine parameter direction
\((\Delta A,C,\delta w)\),
\[
\xi=E\odot(\Delta A X),\quad
\delta^2U=-2U\odot E\odot(\Delta A X)^2,
\]
\[
\delta Z=CU+W\xi,\quad
\delta^2Z=2C\xi+W\delta^2U,\quad
D^2\mathcal L=\frac23\bigl(\|\delta f\|^2+r^\top\delta^2f\bigr).
\]
These formulas confirm the \(2/(3n)\) normalization of the residual
Hessian in the new theorem. The positive mobilities do not affect the
local-minimum statement.

Every nearby constant-loss move in the proof is legitimate. If the
original point minimizes loss in an open ball, a sufficiently nearby
point with the same loss has a smaller ball around it contained in the
first ball. It is therefore also a local minimum, stationary, and
second-order stationary. All the moves are arbitrarily small; no argument
transfers minimality to a remote point on the same loss level.

Neuron sign changes are invertible orthogonal parameter symmetries.
Simultaneously negating one input and its label preserves the entire loss,
because the network is odd. The gauges used in the proof preserve local
minimality and Hessian inertia.

## 2. Reconstructed minimal-circuit diagonal-form argument

For rank-two nonparallel unit triples,
\(\ker X=\operatorname{span}\{c\}\), every \(c_a\ne0\), and
\[
|c_a|<\sum_{b\ne a}|c_b|.
\]
The strict inequality follows from the equality case of the Euclidean
triangle inequality: equality would make the other two inputs parallel.

The more general minimal-unit-circuit theorem in the renewal input starts
from a nonzero ridge combination
\(F_b(a)=\sum_s b_s\tanh(a^\top x_s)\) with value and gradient zero.
Writing \(z=X^\top a\), criticality gives
\(b_s\operatorname{sech}^2z_s=\gamma c_s\), with \(\gamma\ne0\).
Consequently
\[
\sum_s c_sz_s=0,\qquad \sum_s c_s\sinh(2z_s)=0.
\]
Its Hessian, transported by the bijection from the input span to
\(c^\perp\), is a nonzero scalar multiple of the diagonal form with
entries \(c_s\tanh z_s\).

I checked the full sign argument, including zero entries. A zero entry
together with a positive or negative entry supplies the corresponding
sign on \(c^\perp\). If each sign occurs twice, two-coordinate vectors
already supply both signs. In the remaining case of one negative entry,
say \(k\), put
\[
p_i=\frac{c_i z_i}{-c_kz_k}>0\quad(i\ne k),\qquad s_i=|z_i|.
\]
Then \(\sum p_i=1\) and
\[
\sum p_i\frac{\sinh(2s_i)}{2s_i}
=\frac{\sinh(2s_k)}{2s_k}.
\]
The power series gives strict increase and convexity as a function of
\(s^2\), hence \(\sum p_i s_i^2\le s_k^2\). For
\(\chi(s)=\coth(s)/s\),
\[
\chi'(s)<0,\qquad
s\chi''(s)-\chi'(s)
=2\operatorname{csch}^2s\coth s
+\frac{3\operatorname{csch}^2s}{s}
+\frac{3\coth s}{s^2}>0.
\]
Thus \(\chi\) is decreasing and strictly convex as a function of \(s^2\).
Jensen and monotonicity imply \(\sum p_i\chi(s_i)\ge\chi(s_k)\).
Equality would force all magnitudes equal, contradicting the strict
circuit inequality in the one-negative case. Therefore
\[
\sum_s\frac{c_s^2}{c_s\tanh z_s}>0.
\]
Writing \(d_s=c_s\tanh z_s\) and
\(S_+=\sum_{i\ne k}c_i^2/d_i\), the vector
\(v_i=c_i/d_i\), \(v_k=-S_+/c_k\) lies in \(c^\perp\) and has value
\[
S_+\left(1+d_kS_+/c_k^2\right)<0.
\]
The positive direction is immediate from two positive entries. The
one-positive case follows by reversing all signs.

At \(z=0\), the ridge function is odd about the point. It cannot vanish
on a neighborhood: projections of the nonparallel inputs can be chosen
nonzero with distinct absolute values, and successively isolating the
slowest exponential in the scalar tanh functions proves their linear
independence. Analyticity and oddness give both signs arbitrarily nearby.
Together with regular zeros and indefinite critical zeros, this checks
the full no-extremum-at-level-zero dependency.

## 3. Reconstructed exclusion of rank-two first features

A positive-loss local minimum cannot have \(w=0\). At zero readout,
nearby hidden parameters preserve zero prediction; local minimality for
both signs of a readout coordinate would force an analytic ridge identity.
Choosing distinct absolute input projections and then applying scalar
tanh independence forces \(y=0\), contrary to positive loss.

If \(\operatorname{rank}U=2\), stationarity gives
\(T=t b^\top\ne0\), with \(\operatorname{row}U=b^\perp\).
Because \(n\ge3\), select a redundant row \(j\) and
\(v\in\ker U^\top\) with \(v_j\ne0\). For \(t_i\ne0\), the small change
\(W\mapsto W+\varepsilon e_i v^\top\) leaves \(WU,T,f,r\) fixed and
can make \((W^\top t)_j\ne0\).

Vary only first row \(j\) to nearby \(a\), initially, and decompose
\[
\tanh(X^\top a)-u_j=d(a)+\alpha(a)b,\quad
d(a)\in b^\perp,\quad \alpha(a)=F_b(a)/\|b\|^2.
\]
The unchanged feature rows span \(b^\perp\). A fixed linear right inverse
provides coefficients \(\ell_k(a)\to0\) with
\(d(a)=\sum_{k\ne j}\ell_k(a)u_k\).
Replacing the other middle columns by
\(W_{:,k}-W_{:,j}\ell_k(a)\) yields exactly
\[
Z(a)=Z+\alpha(a)W_{:,j}b^\top.
\]
There is no omitted product error: only feature row \(j\) changes, and
only the other middle columns are modified. The derivative of loss along
this preactivation curve at zero is
\[
\frac{2\|b\|^2}{3n}(W^\top t)_j\ne0.
\]
The ridge theorem gives both signs of arbitrarily small \(\alpha(a)\),
hence actual nearby descent. This verifies the complete rank-two lifting
dependency. It excludes a local minimum without asserting a negative
Hessian direction at the original point.

## 4. Rank-one reduction and zero-coordinate cases

Rank zero gives \(f=0\), excluded by the strict loss comparison.
At rank one, the flat middle directions and positive-semidefinite
Hessian force, for every redundant first row,
\[
T\operatorname{diag}(E_{j,:})X^\top=0.
\]
If at least two first rows are nonzero, all rows are redundant. A nonzero
row of \(T\) then has full support, and all first gate rows are
proportional. With \(U_{j,:}=\alpha_j u^\top\), cross multiplication gives
\[
(\alpha_j^2-\alpha_k^2)(u_a^2-u_b^2)=0.
\]
Constant nonzero sample magnitudes would imply \(c^\top\sigma=0\) for
a three-coordinate sign vector, violating the strict circuit inequalities.
Therefore all \(\alpha_j^2\) are equal and positive. This also excludes
zero rows. First-neuron gauges give \(U=\boldsymbol1_nu^\top\).

If exactly one first row is nonzero, the zero redundant rows instead force
\(T=t c^\top\). The remaining row satisfies \(c^\top u=0\), but
\(X(c\odot(1-u^2))\ne0\): otherwise all its absolute preactivations
would coincide. First-weight stationarity yields \((W^\top t)_j=0\).
Active top gates are proportional, and the ratio
\(\operatorname{sech}^2(qb)/\operatorname{sech}^2(qa)\), for
\(0\le a<b\), is strictly decreasing in \(q\ge0\).
All active slopes consequently have one absolute value. If zero, the
prediction is zero. Otherwise their common gate factor and
\((W^\top t)_j=0\) force the signed readout sum, and thus prediction,
to vanish. Inactive readouts contribute neither to \(t\) nor to prediction.

At the common-profile state let \(z=X^\top a\), \(u=\tanh z\),
\(e=1-u^2\), and \(b=c\oslash e\). The residual has full support and
\[
c^\top z=0,\qquad b^\top u=0.
\]
Grouping these two identities by positive magnitude proves the exhaustive
split: either all three \(|z_a|\) are distinct and nonzero, or one is zero
and the other two are equal. For two positive magnitudes, the matrix
formed by \(s\) and \(\sinh(2s)\) is invertible, and a singleton group
cannot have zero coefficient. One nonzero magnitude shared by all three
is excluded by the circuit inequalities.

In the distinct case, a zero readout would allow its middle row to vary
without affecting prediction. Its readout gradient would give
\(r^\top\tanh(qu)=0\) on an interval. Analyticity and the independence
of the three distinct scalar magnitudes would force \(r=0\).
In the symmetric case, all top features lie on one sample line. The
affine hyperplane preserving their nonzero readout sum is not contained
in a coordinate hyperplane for a currently zero readout. Arbitrarily
small constant-loss readout perturbations can therefore make all readouts
nonzero. These perturbations preserve local minimality by Section 1.

Zero middle columns are not silently assumed away. The necessary-geometry
input excludes them at positive local minima by varying the corresponding
inactive first row, then using stationarity and analytic ridge independence.
The new theorem's later repair of zero coordinates of \(W^\top w\) is
also valid without assuming middle-matrix invertibility.

The gate-ratio argument and top-neuron gauges now give
\[
W\boldsymbol1_n=s\boldsymbol1_n,\quad H=\boldsymbol1_nh^\top,\quad
h=\tanh(su),\quad d=1-h^2,\quad
r=\kappa c\oslash(d\odot e),\quad s>0,\ \kappa\ne0.
\]
Nonzero prediction excludes \(s=0\). Write
\(\lambda=W^\top w\) and \(S_w=\sum_iw_i\ne0\).

## 5. Reconstructed full Hessian and its cancellations

The accessible feature tangent plane is exactly \(b^\perp\), because
\(\operatorname{diag}(e)\operatorname{range}X^\top=b^\perp\).
On this plane define
\[
B(\xi,\eta)=-2\kappa\sum_a\frac{c_au_a}{e_a^2}\xi_a\eta_a,\qquad
Q(\xi,\eta)=\sum_ar_a\tanh''(su_a)\xi_a\eta_a.
\]
The minimal-circuit theorem applies to the ridge with coefficients
\(b=c\oslash e\): its value and gradient at the common first row vanish.
The tangent bijection transports \(B\) to \(\kappa\) times its
indefinite ridge Hessian. Thus \(B\) is indefinite.

For independent \(u,v\in b^\perp\), realize
\[
\delta U=\alpha u^\top+\beta v^\top,\qquad
C\boldsymbol1_n=-W\alpha,\qquad \delta w=0.
\]
Then \(\delta Z=(W\beta)v^\top\) and
\(\delta f=(\lambda^\top\beta)(d\odot v)/n\).
The residual contraction of \(2C\delta U\) is exactly zero since
\(r\odot d=\kappa b\), with \(b^\top u=b^\top v=0\).
Also \(\delta^2U_{ja}=-2u_a\xi_{ja}^2/e_a\), so the remaining
first-layer second derivative is precisely \(B\). When
\(\lambda^\top\beta=0\), the exact full loss Hessian is
\[
\frac{2}{3n}\left[
\sum_j\lambda_j B(\alpha_ju+\beta_jv,\alpha_ju+\beta_jv)
+Q(v,v)\beta^\top W^\top\operatorname{diag}(w)W\beta
\right].
\]
This confirms the squared-Jacobian cancellation under the stated
constraint, the mixed-product cancellation, and the retention of both
remaining curvature terms.

## 6. Distinct magnitudes: sign restrictions and inertia

I rederived Proposition 5 rather than assuming its sign conclusions.
Let \(v_a=u_a^2\), \(d_a^*=c_au_a/e_a\), and
\[
k(v)=\frac{(1-v)\operatorname{atanh}\sqrt v}{\sqrt v}.
\]
The power series gives \(k',k''<0\), while
\(\sum d_a^*=\sum d_a^*k(v_a)=0\). The coefficients at the two extreme
magnitudes have one sign \(\epsilon\), opposite to the middle coefficient.
For \(g(v)=\sqrt v\tanh(s\sqrt v)\), direct differentiation gives
\(g'>0,g''<0\), hence
\[
\frac{d^2g}{dk^2}=\frac{g''k'-g'k''}{(k')^3}<0.
\]
For \(F(v)=v/(1-v)\), the identity
\[
2k'(v)-(1-v)k''(v)
=-2\int_0^1\frac{(1-t^2)^2}{(1-vt^2)^3}\,dt<0
\]
instead gives \(d^2F/dk^2>0\). Strict Jensen yields
\[
a_r:=Q(u,u)\ne0,\qquad K:=B(u,u)\ne0,\qquad
\operatorname{sgn}K=-\operatorname{sgn}a_r.
\]
The \(\beta=0\) directions force \(K\lambda_j\ge0\).
Since \(\sum_j\lambda_j=sS_w\ne0\), one has \(a_rS_w<0\).
Pure top-slope variations in \(w^\perp\) have Hessian
\(2a_r\sum_iw_i(\delta s_i)^2/(3n)\). Two negative coefficients
\(a_rw_i\) would supply a supported negative direction; their negative
total sum forces exactly one negative coefficient, strictly dominating
the remaining positive ones.

Zero \(\lambda_j\) can be repaired while preserving loss. Give them small
increments of sign \(-a_r\), compensate in one existing nonzero
coordinate, and call the zero-sum change \(\delta\lambda\). Then
\[
\delta W=\frac{w\,\delta\lambda^\top}{\|w\|^2}
\]
has \(\delta W\boldsymbol1_n=0\) and
\(\delta W^\top w=\delta\lambda\). The denominator is nonzero; the donor
retains its sign if the perturbation is small. All \(\lambda_j/K>0\)
at the nearby local minimum.

Lemma 6's diagonal-form argument is also valid without circuit geometry.
Its strict Jensen inequality uses the distinct top magnitudes and gives
indefiniteness of \(Q\) on \(b^\perp\), from
\(b^\top u=0\) and \(\sum b_a\sinh(2su_a)=0\).
Choose \(v\) with \(Q(v,v)\) opposite in sign to \(a_r\). Put
\(L=B(u,v)\), \(M=B(v,v)\). Indefiniteness gives \(KM-L^2<0\).
For \(\alpha_j=-L\beta_j/K\), the first Hessian sum is
\[
(KM-L^2)\sum_j\frac{\lambda_j}{K}\beta_j^2<0
\qquad(\beta\ne0).
\]
The diagonal form with coefficients \(Q(v,v)w_i\) has exactly one
positive coefficient. Its pullback by any \(W\), singular or not, has
positive index at most one. Since
\(\dim\lambda^\perp=n-1\ge2\), its restriction there cannot be positive
definite. A nonzero \(\beta\in\lambda^\perp\) has nonpositive value.
The combined full Hessian is then strictly negative. No invertibility
assumption on the pullback is needed.

## 7. Symmetric magnitudes and full-rank inputs

For the symmetric profile, sample gauges give \(u=(a,-a,0)\) and
\(c_1=c_2\). Direct substitution gives \(B(u,u)=Q(u,u)=0\).
Since \(B\) is indefinite on a plane, \(B(u,v)\ne0\) for every
independent \(v\). The pure \(\alpha\) directions have zero full
Hessian and zero prediction differential. Their mixed Hessian against
arbitrary \(\beta\) directions is
\[
\frac{2}{3n}B(u,v)\sum_j\lambda_j\alpha_j\beta_j.
\]
No constraint \(\lambda^\top\beta=0\) is needed here: the
squared-Jacobian mixed term vanishes from the zero \(\alpha\) prediction
variation, and top curvature is quadratic only in \(\beta\).
Positive semidefiniteness forces every such mixed pairing to vanish,
hence \(\lambda=0\), contrary to \(\sum_j\lambda_j=sS_w\ne0\).

If \(X\) has rank three, the full-rank theorem in the necessary-geometry
input applies with \(n\ge m=3\). I checked its dependencies: redundant-row
derivative annihilation and full input rank force \(w=0\) at a
positive-loss second-order stationary point. The remaining mixed blocks
force \(W=0\) and \(Uy=0\). The Hessian then vanishes, but an accessible
first-row variation giving \(\delta U_j=y\), together with
\(W=t e_i e_j^\top\), \(w=t e_i\), produces
\[
\mathcal L(t)-\mathcal L(0)
=-\frac{2\|y\|^2}{3n}t^3+O(t^4).
\]
Such points are not local minima. Nonparallel triples have rank at least
two, so the checked rank cases are exhaustive. For \(y=0\), the claimed
strict loss interval is empty.

## 8. Verdict and exact limits

The theorem and its used dependencies pass this reconstruction. No missing
constant-loss locality condition, inaccessible feature variation, zero
denominator, omitted zero-readout or zero-column branch, incorrect
curvature sign, or omitted squared-Jacobian term was found.

The conclusion remains local-minimum exclusion below the zero-readout
loss. Some steps first move to nearby constant-loss points, so this is not
a uniform negative-index theorem at the original point. The proof supplies
neither Gaussian avoidance of all bad finite limits nor exclusion of
escape to infinity, and does not itself establish arbitrary-label fitting.
