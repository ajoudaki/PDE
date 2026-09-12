# Continuation route: finite horizons, residual length, and the added-data gap

Frozen independent route, 2026-09-12. Author: `/root/continuation_route`.
Status: complete route report; the principal added-data selection target remains
open. The new mathematical statements below have been checked by their author,
but have not received an independent review and are not established book results.
No training experiment, Git mutation, or communication with another route was
performed.

## 1. Contract and strongest conclusion

The model is precisely the bias-free, two-hidden-layer tanh network with
normalized input \(u\in S^1\), stored Gaussian variances
\((1,1/n,1/n^2)\), mobilities \((n,1,n)\), and unhalved mean square loss.
On the canonical generated carrier write

\[
\theta=(w,K,c),\quad A=A_0+K,
\qquad
\|\Delta\theta\|_{\rm raw}^2
=\|\Delta w\|_2^2+\|\Delta K\|_{\rm HS}^2+\|\Delta c\|_2^2.
\]

The initialized action \(A_0\) and its actual adjoint are retained. The
initial state is \((g,0,0)\), \(g\sim N(0,I_2)\); at finite width the actual
small random readout is retained. The law is fixed from initialization:

\[
\mu_{\epsilon,\nu}=(1-\epsilon)\nu_*+\epsilon\nu,
\qquad
\nu_*={1\over2}\delta_{(e_1,1)}+{1\over2}\delta_{(e_2,-1)}.
\]

The desired strong interpretation is an order-one improvement on the added
law, compared with the reference-trained prediction, accompanied by an
order-one change of hidden representations caused by that added law, with
whole-circle identification of actual finite GF in the order width first,
then \(\epsilon\downarrow0\). An order-one decrease of the mixture loss
caused entirely by fitting its \(1-\epsilon\) reference mass does not settle
this interpretation.

Two useful results emerge.

1. The source argument of C.4.7 extends to **every separately fixed finite
   physical horizon** \(T\), with a radius \(\delta_{Y,T}>0\) depending on
   that horizon. There is no structural singularity at 40 in that argument.
   This yields a nonlinear determining law and actual finite-GF capture on
   any selected finite horizon, for sufficiently small contamination.
2. Its absolute source estimates can be rewritten in the cumulative
   residual length \(\ell=2\int\int |r|\,d\mu\,dt\). This removes the
   artificial factor \(e^{2T}\) from the raw norm estimates and identifies
   a sharper possible continuation variable. It does not, by itself,
   provide the required source cap for order-one residual lengths.

Neither statement controls a horizon \(T_\epsilon\) long enough to prove a
fixed positive added-data gain as \(\epsilon\downarrow0\). In fact, on
each fixed horizon the added-law effect is \(O(\epsilon)\), including
hidden displacement relative to the reference. The decisive missing
estimate is uniform nonlinear source/reachable-state control on the
relevant growing horizon, together with a residual-direction fitting
estimate for the added data.

## 2. Exact dynamics and the finite-horizon extension

For \(H^1=\tanh(w\cdot u)\), \(Z^2=AH^1\), \(H^2=\tanh Z^2\), set

\[
f=\langle c,H^2\rangle,
\quad r=f-y,
\quad \Delta^2=c\phi'(Z^2),
\quad Q=A^*\Delta^2,
\quad\phi=\tanh.
\]

The exact physical vector field is

\[
\mathcal F_\mu(\theta)=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\Delta^2(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).                 \tag{1}
\]

The full first row is required in (1); passive inputs are evaluated by
the same trained state. The raw norm is the exact GF metric, including
the HS increment norm. On a finite carrier it is

\[
\|\Delta W^1\|_F^2/n+\|\Delta W^2\|_F^2
 +\|\Delta W^3\|_2^2/n.
\]

**Proposition 1 (horizon-parametrized version of the nonlinear construction).**
For each \(Y\ge1\) and each fixed \(0<T<\infty\), there is
\(\delta_{Y,T}>0\) such that every law satisfying
\(\mathcal W_1(\mu,\nu_*)<\delta_{Y,T}\) has a unique strong raw solution
of (1) on \([0,T]\), from the specified canonical initialization.
Uniqueness also holds from its reached states, on the remaining part of
that interval. The construction is continuous in the law and its
prediction is defined on the whole circle. Actual finite GF satisfies

\[
\sup_{t\le T,u\in S^1}|f_{n,\mu}(t,u)-f_\mu(t,u)|
 \longrightarrow0\quad\hbox{in probability}.                \tag{2}
\]

The same conclusion holds when \(\mu\) is approached in \(\mathcal W_1\)
by arbitrary deterministic laws while width tends to infinity. It
includes the finite observation programs and paired hidden observations
specified in C.4.7.1. For fixed \(T\), \(0\le\epsilon\le\epsilon_{Y,T}\),
and arbitrary \(\nu\in\mathcal P(S^1\times[-Y,Y])\), one also has

\[
\sup_{t\le T}\|\theta_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)\|_{\rm raw}
 +\sup_{t\le T,u}|f_{\mu_{\epsilon,\nu}}(t,u)-f_*(t,u)|
 \le C_{Y,T}\epsilon.                                    \tag{3}
\]

All constants may deteriorate with \(T\). In particular, this statement
does not assert a common positive radius for all \(T\).

**Proof and complete dependency/parameter audit.** The proof uses the
specific estimates of C.4.7.2–C.4.7.6, whose complete bodies were read.
The following audit gives every place where the horizon enters and why
the same construction closes for a fixed replacement \(T\).

First, the reference exists for all physical times. C.4.5.1 constructs its
global feature equation, with scalar feature prediction \(b\) satisfying

\[
b_s=\|\theta_s\|_{\rm raw}^2\ge m>0,
\quad m={1\over2}\mathbb E\tanh^2(\sqrt qG),
\quad q=\mathbb E\tanh^2G>0.
\]

Here (m>0) follows directly since (q>0) and a nondegenerate Gaussian
is nonzero almost surely. Thus the first feature time \(s_\dagger\) at
which \(b=1\) is finite, at most (1/m). The exact physical clock
\(ds/dt=2(1-b)\) approaches \(s_\dagger\) only at infinite physical time.
All reference physical horizons lie in this one compact feature segment.
The Gaussian active-query tail proof C.4.5.2 applies on that segment.
For this extension no numerical certificate \(m\ge1/10\) is necessary:
one may replace every occurrence of 10 in its segment bounds by any
fixed \(S\ge1/m\). The fresh-pulse amplification and response sums are
finite for every such fixed \(S\); their Gaussian-plus-bounded
decomposition therefore supplies uniform reference active-query tails
at all physical times. This avoids an unverified numerical dependency.

For a finite-law raw Euler program on the new \([0,T]\), equations
C.4.7.NE and N9 give the deterministic constants

\[
C_0=Y(e^{2T}-1),\qquad R_0=Y+C_0,
\qquad \|K\|_{\rm HS}\le2TR_0C_0,
\qquad \|A\|\le10+2TR_0C_0.
\]

These are finite for each fixed \(T\); no smallness of \(T\) was used.
The one-reference transport bound NC is valid on the resulting raw
ball. Comparing a raw Euler interpolation with the existing reference
gives, at fixed cutoff \(R\ge1\),

\[
\sup_{t\le T}d(\theta^h_\lambda(t),\theta_*(t))
\le C_T e^{C_TR}
 \{(1+R)(\mathcal W_1(\lambda,\nu_*)+h)+e^{-cR^2}\}.       \tag{4}
\]

The reference tails alone enter (4). Their Gaussian decay beats the
linear-in-\(R\) exponent for every finite \(C_T\). Taking a cutoff
proportional to \(\sqrt{\log(e/(q+h))}\) gives a modulus tending to zero
as \(q+h\to0\). This is N30 with new finite constants.

The independent reference clock Euler anchor of C.4.7.N37–N47 also
works on the new horizon. Its state difference estimate has a finite
Lipschitz constant

\[
L=100(1+M+C_0+R_0)^4,\qquad M=10+2TR_0C_0,
\qquad E=e^{LT}.
\]

Fresh Gaussian pulses give the exact named-source coefficient cap

\[
B_{\rm cl}=2C_0+TP_0K_0E<\infty,                         \tag{5}
\]

where \(P_0,K_0\) are the finite expressions in N43–N44. A finite
graph is fixed before width tends to infinity, and the fresh pulse is
removed only after that limit. This proves the named coefficients
even transverse to singular Gaussian supports. Neither the zero
readout of these auxiliary programs nor the fresh pulse changes the
actual network initialization.

The raw-to-clock defect has the exact integral form N32 and named
derivative bounds N33–N36. Under a temporary source cap, the sum of
its \(L^p\) defects is \(C_{B,p,T}h\), and each backward pulse's summed
defect divided by its own step and atom mass is also at most
\(C_{B,p,T}h\). These constants remain finite for fixed \(B,p,T\).
Comparison of the raw and clock source equations gives N51,

\[
E_k\le C_{B,T}\{\eta_h+h+\sum_{j<k}h_jE_j\},\qquad
\eta_h\longrightarrow0.                                 \tag{6}
\]

The modulus \(\eta_h\) follows from (4) at the reference and the
clock Euler consistency estimate. Choose \(B=B_{\rm cl}+1\), then
choose \(h_*>0\) so that discrete Gronwall makes the right side of
(6) at most (1/2). The causal first-failed-row argument gives a
reference raw source cap \(B_*=B_{\rm cl}+1\).

Next the weighted coefficient transport equations N20–N31 compare
nearby laws with that reference raw program, on the identical mesh.
They use the same passive output query, retain every past source's
step and mass, and give

\[
E_k\le C_{B,T}e^{C_{B,T}T}
 \{\Phi_{B_*}(q)+q\}^{1/16},\qquad \Phi_{B_*}(q)\to0.      \tag{7}
\]

Their bounds need only finitely many moments, all supplied by the
temporary-cap source decomposition. Their derivation uses neither
\(T\le40\) nor a lower atom-mass bound. Put \(B=B_*+1\); choose
\(\rho_T>0\) to make (7) at most (1/2). A second causal
first-failed-row induction proves the nearby-law raw source cap.
Consequently every passive \(Q\) has a uniform Gaussian marginal tail
for the admitted Euler programs. The readout is bounded pointwise.

The remainder of C.4.7.4 uses only this tail estimate, raw bounds,
completeness, and joint continuity of (1). In particular its Osgood
comparison satisfies

\[
s'(t)\le L_Ts(t)\log(e/s(t)),\qquad
s(t)\le e^{1-e^{-L_Tt}}s(0)^{e^{-L_Tt}}.                  \tag{8}
\]

Every finite \(T\) has a positive exponent \(e^{-L_TT}\).
Finite-law, fine-mesh Euler approximants are therefore Cauchy in the
strong raw path space. Joint continuity passes their integral
equations to (1). Tails pass by positive-part cutoff convergence.
Equation (8) then proves uniqueness against any competing strong raw
solution, with tails required only for the constructed solution.
Restricting that solution proves reached restart. This constructs a
nonlinear law, rather than inferring one from linear response.

For (2), the fixed finite oracle argument in C.4.7.5 applies unchanged.
Each law and mesh is fixed before width tends to infinity. Realize the
finite population program on the actual initialized arrays, including
the actual readout additively. III.F.1–7 and global-nonlinear A.1–A.2
identify its values and all required second moments. These full
probability proofs were read, including adaptive conditioning,
singular-query regularization, source response, causal feedback, and
common-carrier adjunction. The finite raw comparison is NC, with the
proxy alone bearing tails. If the weaker exponential tail is used,
partition \([0,T]\) into finitely many intervals with \(C\ell<a/2\),
choose their cutoffs and incoming tolerances backwards, then fix the
law approximation and mesh, and only then take width to infinity.
This is exactly the finite partition proof NAP, which requires only
\(T<\infty\). Whole-circle and time nets are justified by the full-row
and speed bounds. No growing program is inserted into a fixed-program
theorem.

Finally (3) follows directly from C.4.7.6.1–6.4; identifying a finite
network derivative is unnecessary here. The source cap supplies
uniform passive exponential moments. Radial saturation gives

\[
\sup_{t\le T}|w_\mu(t)|^2
\le |g|^2+2Y(1+\sqrt T)
       \int_0^T\int |Q_\mu(s,u)|\,d\mu\,ds.
\]

Jensen and the passive exponential moment give a positive Gaussian
square moment for the row supremum, with an exponent allowed to depend
on \(T\). Hölder then bounds every fixed moment of
\(u_j\cosh^2(w_j)\phi'(w\cdot u)Q(u)\), uniformly on a smaller law
neighborhood. Thus the exact coordinate clocks
\(X_j=F(w_j)\), \(F'=\cosh^2\), have an \(L^2\)-integrable velocity.
Their contamination equation is

\[
\Theta_\epsilon'=\mathcal F_0(\Theta_\epsilon)
          +\epsilon\mathcal B_\nu(\Theta_\epsilon).         \tag{9}
\]

The inverse-gate forcing in (9) is bounded along these actual reached
paths. The reference-axis field \(\mathcal F_0\) is Lipschitz in clock
norm when one readout endpoint is bounded, as proved by the explicit
factorization in NV-reference-Lipschitz. The actual readout obeys
\(\|c(t)\|_\infty\le2YT\). Gronwall gives
\(\sup_t\|\Theta_\epsilon-\Theta_*\|\le C_{Y,T}\epsilon\).
The inverse clock is 1-Lipschitz; the forward maps and prediction are
Lipschitz on the resulting raw ball. This proves (3). All operations
used above have finite constants for the chosen horizon, completing
the extension. \(\square\)

## 3. What this extension does and does not select

Let \(R_\nu(f)=\int(f(u)-y)^2\,d\nu\). On any fixed horizon the
readout and label bounds give

\[
|R_\nu(f_{\mu_{\epsilon,\nu}}(t))-R_\nu(f_*(t))|
\le2(B_{Y,T}+Y)C_{Y,T}\epsilon,\qquad t\le T.              \tag{10}
\]

Indeed the two squared residuals differ by their prediction difference
times their residual sum. This calculation uses the added law as its
evaluation law and is uniform over that law. The right side tends to
zero. Likewise, bounded tanh and the forward estimates imply, for
either hidden layer,

\[
\sup_{t\le T,u}
\|H^\ell_{\mu_{\epsilon,\nu}}(t,u)-H^\ell_*(t,u)\|_2
\le C'_{Y,T}\epsilon.                                   \tag{11}
\]

The paired squared hidden displacement relative to the reference is
therefore \(O(\epsilon^2)\). Positive hidden displacement relative to
initialization does not contradict (11), because the reference already
moves its hidden representations.

Equations (10)–(11) prove that a fixed horizon, including any fixed
horizon above 40, cannot yield a lower bound independent of
\(\epsilon\) for the *additional* effect relative to the reference
at that same time. For an endpoint comparison, one must separately
control the reference transient. Once
\(\sup_u|f_*(T_\epsilon,u)-f_*^\infty(u)|\to0\), a gain
\(R_\nu(f_*^\infty)-R_\nu(f_{\mu_{\epsilon,\nu}}(T_\epsilon))\ge g_0>0\)
cannot be attributed to that transient, and it requires departure from
the fixed-horizon perturbative regime. Without this endpoint condition,
a transient reference predictor could itself outperform its endpoint
on the added law, so endpoint-relative gain alone would be ambiguous.

The quantifier distinction is exact:

\[
\forall T<\infty\ \exists\delta_T>0
\quad\not\Longrightarrow\quad
\exists\epsilon_0>0\ \forall\epsilon<\epsilon_0:
       \epsilon D_Y<\delta_{\tau/\epsilon}.
\tag{12}
\]

One can even use Proposition 1 to choose a slowly diverging horizon
\(T_\epsilon\) on which the added effect vanishes. For each integer
\(j\ge1\), choose a strictly decreasing positive sequence \(a_j\to0\)
so that \(a_j<\epsilon_{Y,j}\) and \(C_{Y,j}a_j\le1/j\).
For \(a_{j+1}<\epsilon\le a_j\), choose \(T_\epsilon=j\).
Then \(T_\epsilon\to\infty\), but (3) bounds the reference difference
by \(1/j\). Since the reference approaches its determining endpoint,

\[
\sup_u|f_{\mu_{\epsilon,\nu}}(T_\epsilon,u)-f_*^\infty(u)|\to0.
\]

This legitimate growing-horizon consequence still gives no added-data
gain. It is an explicit check against confusing unbounded horizon
existence with learning of the rare component.

## 4. A residual-length source lemma

The absolute bounds in C.4.7 use elapsed time and the envelope
\(Y(e^{2T}-1)\). Their exact recursions admit a sharper variable.
For a finite Euler program let

\[
\gamma_{ka}=-2h_kp_ar_{ka},\qquad
a_k=\sum_a|\gamma_{ka}|,\qquad
\ell_k=\sum_{j<k}a_j,
\qquad \ell_k\le\ell.
\]

The residuals and hence these coefficients are the actual deterministic
population residuals of the program. Named-source differentiation freezes
them, as in the source rule; it is not data differentiation.

**Proposition 2 (absolute source bounds in residual length).** Suppose
the already constructed backward coefficient rows have cap \(B\), in
the sense of C.4.7.N1. Put \(D_0=B+\ell^3\). Independently of the
number of steps, atoms, minimum weight, and physical horizon:

\[
\|c_k\|_\infty\le\ell_k,\qquad
\|K_k\|_{\rm HS}\le\ell_k^2/2,
\quad \|A_k\|\le M_0+\ell^2/2,                            \tag{13}
\]

\[
\|w_k\|_2\le\sqrt2+(M_0+\ell^2/2)\ell^2/2,
\quad Q_{ku}=\zeta_{ku}+J_{ku},
\quad |J_{ku}|\le D_0,
\quad \mathbb E\zeta_{ku}^2\le\ell^2.                    \tag{14}
\]

For every named backward pulse \(p=(s,b)\), every \(p_0\ge1\), and
\(\gamma_p\ne0\),

\[
\left\|{\max_{j\le k}|\partial_{\zeta_p}w_j|\over|\gamma_p|}
 \right\|_{L^{p_0}}
\le 2\exp\{3D_0\ell+2p_0\ell^4\}.                       \tag{15}
\]

The derivative vanishes identically if \(\gamma_p=0\). Consequently,
putting \(a_B=2e^{3D_0\ell+2\ell^4}\) and \(f_B=a_B+1\),

\[
|\alpha_{ku,p}|\le a_B|\gamma_p|,
\qquad |F_{ku,p}|\le f_B|\gamma_p|,
\qquad
\sum_p|\beta_{ku,p}|\le3\ell e^{3f_B\ell^2}.              \tag{16}
\]

When \(\ell=0\), all readout, learned increments, backward answers,
and response coefficients vanish; (13)–(16) are interpreted directly.

**Proof.** The readout update is a sum of coefficients \(
\gamma_{ka}\) multiplying functions bounded by one, proving the first
inequality of (13). The middle increment has norm at most
\(a_k\ell_k\). Since
\(\sum_ka_k\ell_k=(\ell_{\rm final}^2-\sum_ka_k^2)/2\le\ell^2/2\),
the second and third inequalities follow. The first-row increment is
at most \(a_k\|A_k\|\ell_k\) in \(L^2\), proving (14)'s row bound.

The exact source decomposition N5 writes \(Q\) as its Gaussian
source, its beta response, and its learned contribution. The latter
has coefficient sum at most

\[
\sum_{q<k}|\gamma_q|\,|\mathbb E[\Delta^2_{ku}\Delta^2_q]|
 \le \ell^2\sum_q|\gamma_q|\le\ell^3.
\]

The source covariance is the second moment of \(\Delta^2_{ku}\),
bounded by \(\ell^2\). This proves the remaining parts of (14).

For \(S=\sum_{j,a}|\gamma_{ja}||Q_{ja}|\), Jensen with weights
\(|\gamma_{ja}|/\ell_{\rm final}\) and the scalar Gaussian moment
bound gives, for \(\lambda\ge0\),

\[
\mathbb E e^{\lambda S}
 \le2\exp\{\lambda\ell D_0+\lambda^2\ell^4/2\}.           \tag{17}
\]

This uses no temporal or input independence. Indeed each
\(Q_{ja}=\zeta_{ja}+J_{ja}\), the shift is bounded by \(D_0\),
and \(\mathbb E e^{b|\zeta_{ja}|}\le2e^{b^2\ell^2/2}\).
Using the actual total coefficient mass in Jensen first and then its
upper bound \(\ell\) proves (17).

Let \(M_{k;p}=\max_{j\le k}|\partial_{\zeta_p}w_j|\).
The exact lower source equation N7, with
\(|\phi'|\le1\), \(|\phi''|\le2\), and the D-row cap, gives

\[
{M_{k;p}\over|\gamma_p|}
 \le\exp\{D_0\ell+2S\}.                                  \tag{18}
\]

The direct pulse is bounded by \(|\gamma_p|\); the later scalar
amplification at node \(j\) is at most
\(1+D_0a_j+2\sum_a|\gamma_{ja}||Q_{ja}|\). Multiplying these
factors and using \(1+x\le e^x\) proves (18). If the direct coefficient
is zero the entire linear causal pulse equation is zero. Applying
(17) with \(\lambda=2p_0\), taking the \(p_0\)-th root, and using
\(2^{1/p_0}\le2\) proves (15). Expected first-feature differentiation
and the learned term of F then prove the first two estimates in (16).

For the upper source equations N8, let \(U_k\) be the maximum,
through node \(k\), of the pointwise sum of absolute derivatives of
one forward query with respect to its named upper source slots.
The readout derivative row sum is at most \(\ell U_k\), and
the derivative row of \(\Delta^2=c\phi'(Z^2)\) is at most
\(\ell U_k+2\ell U_k=3\ell U_k\). The current direct forward
coefficient is one. Every earlier F coefficient is at most
\(f_B|\gamma_q|\), so the causal scalar inequality is

\[
U_k\le1+3\ell f_B\sum_{q<k}|\gamma_q|U_{t(q)}
 \le e^{3f_B\ell^2}.
\]

Discrete Gronwall in total coefficient mass proves the last bound.
Taking expectations of the upper derivative row gives the final
inequality of (16). \(\square\)

This produces the sufficient absolute cap inequality

\[
B\ge3\ell\exp\!\left(3\ell^2
  [1+2e^{3(B+\ell^3)\ell+2\ell^4}]\right).               \tag{19}
\]

For example \(B=1\) satisfies (19) for all sufficiently small
\(\ell>0\), by continuity and the vanishing right side at zero.
Thus a small-residual-length interval admits a source cap without a
small physical-time requirement. However, (19) remains an absolute
bootstrap, not an estimate that closes at every finite \(
\ell\). Its right side grows rapidly in \(B\), and it does not
replace the reference anchor when the total length is order one.
Failure of (19) is not divergence of the actual source coefficients.

For an existing strong GF path define

\[
\ell_\mu(t)=2\int_0^t\int|r_\mu(s,u,y)|\,d\mu\,ds.
\tag{20}
\]

The continuous counterparts of (13)–(14)'s raw bounds follow by the
same integral argument. Under contamination this clock has the exact
decomposition

\[
\ell_{\mu_{\epsilon,\nu}}(t)
=2(1-\epsilon)\int_0^t\int|r_\epsilon|\,d\nu_*\,ds
 +2\epsilon\int_0^t\int|r_\epsilon|\,d\nu\,ds.            \tag{21}
\]

If one could prove the first integral remains bounded uniformly and
the added residual remains bounded up to \(t=\tau/\epsilon\), then
(21) would be \(O(1+\tau)\). Those are additional estimates on the
changed-law trajectory. Reference residual decay proves neither of
them. The energy identity alone controls the squared velocity and
does not bound (20) uniformly in time.

## 5. Why the trained response does not close the missing step

C.4.6.2 proves a bounded homogeneous propagator \(U(t,s)\) at the
reference and a forcing estimate linear in integrated forcing.
The proof was read in full, including the singular-endpoint metric
and zero-mode compatibility. These estimates are useful but remain
reference linear estimates.

Even granting an ambient quadratic estimate that is stronger than
the source proves, an error \(h=\Theta_\epsilon-\Theta_*\) would obey
an equation of the form

\[
h'=\mathcal L(t)h+\epsilon b_\nu(t)
  +N(t,h)+\epsilon[\mathcal B_\nu(\Theta_*+h)
                         -\mathcal B_\nu(\Theta_*)].      \tag{22}
\]

The propagator bounds the integral of the last two terms; it does
not bound their production. If one provisionally had
\(\|h(t)\|\lesssim\epsilon t\) and \(
\|N(t,h)\|\lesssim\|h\|^2\), the crude remainder estimate is
\(O(\epsilon^2t^3)\), unusable at \(t\asymp1/\epsilon\).
The actual C.4.7 Taylor statement is only on compact families of
directions for fixed \(T\), so the provisional uniform quadratic
bound is not available either.

The scalar equation \(x'=\epsilon-x^2\), \(x(0)=0\), provides a
precise logical countercheck. Its homogeneous reference propagator
is identically one, its forcing is bounded, and its first variation
is \(t\). But its exact solution is
\(x(t)=\sqrt\epsilon\tanh(\sqrt\epsilon t)\); at
\(t=1/\epsilon\) the response prediction is one while the actual
solution tends to zero. This example is not a claim about the neural
model. It refutes the inference from bounded homogeneous propagation
and bounded forcing to a growing-horizon first-order approximation.

A possible successful mechanism must therefore control the nonlinear
motion along the manifold on which the two reference examples remain
fitted, or supply another equally strong structure. A projected
gradient law on that manifold would also need a positive residual
direction for the added data and a whole-circle observation map.
Neither such a nonlinear manifold theorem nor a quantitative
projected-kernel coercivity statement has been proved in this route.

There is a second continuation issue. The energy identity gives, for
any already existing path and finite (t>s),

\[
\|\theta(t)-\theta(s)\|_{\rm raw}
 \le Y\sqrt{t-s}.
\]

Thus a solution with a finite maximal time has a strong terminal
state. In an infinite-dimensional space this endpoint and continuity
of the vector field do not supply local existence from that state.
The needed source-tail/Euler approximation bounds have to persist to
the endpoint. C.4.7 avoids this issue on its constructed interval;
energy alone cannot extend that interval.

## 6. Claims, attacks, and next obligation

| Claim | Status and evidence |
|---|---|
| Nonlinear whole-circle law and finite-GF capture for every fixed \(T\), with \(T\)-dependent neighborhood | Derived Proposition 1; horizon audit of the complete C.4.7 source and approximation proof |
| A fixed positive contamination radius valid for every \(T\) | Open; (5)–(7) provide no such uniform radius |
| Uniform nonlinear capture at \(T_\epsilon\asymp1/\epsilon\) for a fixed open family of added atoms | Open; (12), (19), and (22) identify the missing estimates |
| Order-one additional risk gain or hidden adaptation on fixed \(T\) as \(\epsilon\to0\) | Excluded by (10)–(11) for this interpretation |
| Small residual length replaces small elapsed time in absolute source bounds | Proved Proposition 2 |
| Energy gives sufficient source regularity at a reached endpoint | Unsupported; terminal raw norm control omits source tails |
| Uniformly bounded trained response implies nonlinear continuation | Invalid inference, checked by (22) and the scalar example |
| An open nonorthogonal added-atom family with positive slow-time gain | Not constructed in this route |

The highest-leverage next obligation is a reachable-state estimate that
controls the reference residual contribution in (21) and the named
source cap on \(0\le t\le\tau/\epsilon\), for a fixed small
\(\tau>0\), without a radius that shrinks faster than the
contamination. Such an estimate would make the residual-length
reformulation useful. To reach the desired risk statement it must be
paired with a positive projected residual direction for the added
law, not just an upper bound on motion.

The result is open, not an impossibility theorem. The positive compact-
horizon extension and residual-length identities are retained even
though they do not settle the requested selection mechanism.

## 7. Source scope, coverage, and checks

The parent assignment authorized this study-owned output only, its
scratch namespace, the following established inputs, and strictly
necessary established dependencies. The study README, other routes,
other studies' scientific files, task history, and Git history were
not read. An initial broad filename query displayed other study
directory/README names only; no content was opened. Git status later
displayed unrelated changed filenames only for shared-checkout safety.
No scientific information crossed a study boundary.

Complete actual scientific read coverage:

- `docs/README.md` and `docs/NOTATION.md`, complete.
- `docs/global_nonlinear.md` 3981–4947: C.4.1–C.4.3, complete.
- `docs/global_nonlinear.md` 8977–11439: C.4.7, complete, including
  all source, completion, variation, width-order, and scope proofs.
- Strictly necessary established dependencies in that same file:
  1842–1902 \(A.1–A.4, complete\); 5474–5781
  \(C.4.5.1.1–3, complete\); 6103–6594 \(C.4.5.2, complete\);
  7169–7571 \(C.4.6.2, complete\).
- `docs/special_data_limits.md` 3785–4286: III.F.1–10, complete,
  including fixed-program probability, all source/regularization
  proofs, common action construction, HS metric, multiplier rules,
  and scalar differentiation.
- Shared `AGENTS.md` and `RESEARCH_WORKFLOW.md` were read; only Part 1
  is operative for this scoped research output. Required skills
  `solve-math-rigorously` and `investigate-conjectures` were read,
  including research-contract, adversarial-audit, and
  proof-search-orchestration references.

The initial combined tool output was truncated; the affected source
reads were repeated in bounded, complete chunks before analysis.
Additional metadata/heading searches do not expand the scientific read
scope. A general navigation passage 1760–1841 of global_nonlinear was
also displayed while locating the contained probability dependency;
it was not used for a scientific conclusion.

No external theorem beyond the contained established proofs is needed
for Propositions 1–2. The numerical certificate for \(m\ge1/10\), the
full C.4.6 finite-derivative bridge, and B.1's general theorem were not
audited here and are not relied upon for a new numerical or derivative
claim. Reference existence, positivity of \(m\), and source tails were
used in the nonnumeric form explained in Proposition 1.

Source hashes at read/check time (SHA-256):

| File | SHA-256 |
|---|---|
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `docs/README.md` | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |

Observed HEAD: `abab5537b4a248ada7fde7164c60a56fb864e881`.
Shared index and changed paths were inspected as metadata only before
writing. All edits belong to this one assigned report. Checks were
theoretical: coefficient-mass normalization (including zero pulses),
signed residual factors, loss factor two, HS/finite metric agreement,
singular-source convention, physical/feature clock distinction,
finite-program order, every horizon-dependent bootstrap choice,
fixed-vs-growing-horizon quantifiers, and reference-vs-added hidden
motion. There is no empirical or numerical training claim.
