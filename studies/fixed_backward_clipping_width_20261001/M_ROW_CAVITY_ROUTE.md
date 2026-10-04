# Strong response-row concentration and cap-dependent local consistency

2026-10-01. Scoped theoretical continuation of `M_UNIFORM_CAVITY_ROUTE.md`.
This note uses the same assigned model and source files, the earlier
owned derivation of the finite-vector constants, and the supervisor's
requested localization strategy. The separate law route supplied the
following interface: on physical covariance inputs with common variance
and mean-square increment bounds, and causal response inputs with common
small row masses, its conditional mean-map comparison is uniform in M>=1
in the strong norm defined below. That interface is used explicitly; it
is not proved again here. No checked file is edited.

**Conclusion.** The prescribed finite cavity sources are bounded by
`exp(C(1+M))/sqrt(n)` in the strong covariance/response-row norm. While the
deterministic finite mean tuple lies inside a common response-row domain,
one may localize the random cavity tuple to a larger common domain at
cost `exp(C(1+M))/sqrt(n)`. On that event the upper scalar reinsertion
uses a common small-activity condition, and the lower scalar comparison
costs only `exp(C(1+M))`. Together with the separate uniform strong
mean-map estimate, this yields a complete local mean-map defect of that
same exponential form. A first-exit argument for the deterministic mean
tuple is stated with its exact hypotheses at the end.

## 1. Setup and the strong norm

Use the prescribed-history system (1) of `M_UNIFORM_CAVITY_ROUTE.md` and
its activity clock

\[
 x=s(t)=\int_0^t\rho(u)\,du\in[0,S],
 \qquad \lambda_a(x)=r_a(t)/\rho(t),\qquad |\lambda_a|\le\sqrt m.
\]

All derivatives in this note are activity derivatives. The supplied K,V
are activity Lipschitz, and lambda is only required to be measurable.
The activity S is bounded above by a common small S_0. Constants may
depend on a positive lower bound for S when the displayed normalized
distances divide by S. In the fixed nonzero-label application, the
prescribed activities have upper and lower bounds proportional to that
fixed label size; no uniform statement as the labels vanish is needed.

Write U(x) for the finite vector state, L(x) for its Jacobian with
prescribed histories fixed, and Phi(x,y) for its state propagator.
For the lower feature h_a and upper clipped signal d_a, define

\[
 C^h_{n,ab}(x,y)=\langle h_a(x),h_b(y)\rangle_n,
 \qquad C^d_{n,ab}(x,y)=\langle d_a(x),d_b(y)\rangle_n,
 \quad \langle u,v\rangle_n=u^\top v/n.
\]

For a lower additive-carrier source, let J_b(y) be its state source with
the coefficient lambda_b removed, exactly as in the assigned cavity
note. For an upper additive-preactivation source use its source S_b(y).
Set

\[
\begin{aligned}
 T^h_{n,ab}(x,y)
 &=n^{-1}\operatorname{tr}[D_Uh_a(x)\Phi(x,y)J_b(y)],\\
 T^d_{n,ab}(x,y)
 &=n^{-1}\operatorname{tr}[D_Ud_a(x)\Phi(x,y)S_b(y)],\\
 Q^h_{n,ab}(x,y)&=\lambda_b(y)T^h_{n,ab}(x,y),\\
 Q^d_{n,ab}(x,y)&=\lambda_b(y)T^d_{n,ab}(x,y),\qquad y\le x,\\
 D_{n,a}(x)&=n^{-1}\sum_i(F_M)_z(z_{ai}(x),w_i(x)).
\end{aligned}                                                     \tag{1}
\]

The lower response has no atom. The upper response is
`diag(D_n(x)) delta_x + Q^d_n(x,y)dy`. Its atom is kept separate from
the past density. Bars denote full-Gaussian expectations in the
prescribed finite system, not expectations conditional on the original
fitting event.

For a covariance C use the maximum entry norm over both activity times.
For a causal kernel Q use

\[
 \|Q\|_{\rm row}
 =\sup_{x\in[0,S]}\max_a\sum_b\int_0^x|Q_{ab}(x,y)|\,dy.
\]

The strong distances between two tuples are

\[
\begin{aligned}
 d_H&=\|\Delta C_h\|_\infty+S^{-1}\|\Delta Q_h\|_{\rm row},\\
 d_D&=S^{-2}\|\Delta C_d\|_\infty
       +S^{-1}(\|\Delta D\|_\infty+\|\Delta Q_d\|_{\rm row}).
\end{aligned}                                                     \tag{2}
\]

The supremum occurs inside the random norm. This is stronger than the
pointwise expected error used in the original deterministic-majorant
argument. It is the reason one can use total derivative masses in the
separate law comparison without a deterministic entrywise majorant.

Throughout the proof, a symbol E_M denotes a bound of the form

\[
 E_M=\exp(C(1+M)).                                               \tag{3}
\]

There are only finitely many such bounds in use; C can increase between
lines. Finite products and fixed powers are absorbed by increasing C.

## 2. Finite-vector estimates used below

The earlier owned route proves

\[
 \|L(x)\|_{\rm op}\le C(M+1+\|W_0\|_{\rm op}^2).
\tag{4}
\]

The ordinary state tangent, the derivatives of the bounded local gates,
and the Hilbert--Schmidt variations of the Jacobian/propagator graph have
constants bounded by

\[
 C(1+M)^b(1+\|W_0\|_{\rm op})^b
       \exp\{CS_0(M+1+\|W_0\|_{\rm op}^2)\}.                 \tag{5}
\]

This does not justify an arbitrary normalized scalar pairing. In
particular, a product of upper velocities requires a coordinate moment
estimate for a reused Gaussian action. We prove the needed estimate and
list the derivative cases explicitly below. For precisely those cases,
Gaussian Poincare will give

\[
 \|X-\mathbb EX\|_{L^2}\le E_M/\sqrt n                         \tag{6}
\]

for the covariance integrands in (7), the response diagonal and target
derivative in (9)--(10), and the upper atom and its activity derivative.

The use of (6) below is legitimate for almost every activity time. The
coefficients lambda, K', and V' are deterministic and bounded; no
derivative of them is needed in any step.

### 2a. Coordinate moments of the passive reused action

Let `q_a=h'_a`, and write `Z_a=W_0q_a`. Explicitly,

\[
 q_a=-\frac2m\sum_b\lambda_b(u_a^\top u_b)
       \psi(\alpha_a)F_M(\alpha_b,P_b),\qquad
 \|q_a\|_\infty\le CM.                                      \tag{6a}
\]

At every fixed activity time, every fixed finite p>=1, and every fixed
weight parameters c_*,b_*>=0, one has

\[
 \sup_{i,a,x}\mathbb E\left[
 (1+K_W)^{b_*} e^{c_*K_W^2}|Z_{ai}(x)|^p\right]\le E_M,
 \qquad K_W=\|W_0\|_{\rm op}.                                \tag{6b}
\]

The width threshold may depend on p and the weight but is independent
of M. Only fixed-time moments are
claimed; temporal suprema of Z are unnecessary below.

Here is a proof that does not use strong row concentration, mean-map
localization, or population identification. Delete upper row i and use
the passive cavity identity (36)--(38) of `SMOOTH_CAVITY_ROUTE.md`:

\[
 Z_{ai}(x)=G^q_a(x)+\sum_c A^q_{ac}(x)d_{ci}(x)
       +\sum_b\int_0^x\lambda_b(y)R^q_{ab}(x,y)d_{bi}(y)\,dy
       +\varepsilon^q_{ai}(x).                               \tag{6c}
\]

On the cavity-measurable operator event `K_W^c<=K_0`, the conditional
Gaussian variance of G^q is `||q_a^c||_n^2<=C M^2`, by (6a).
The atom A^q is bounded independently of M because its lower direct
carrier derivative contains `(F_M)_P`, which is uniformly bounded.
The past trace R^q is bounded by E_M from (5). The actual reinserted
path satisfies `|d_bi|<=2S`. The passive Taylor remainder, established
before any scalar-law comparison in the assigned cavity note, has
each fixed conditional moment at most `E_M/sqrt(n)`; its proof only
uses the bounded derivatives of the finite-M graph and the independent
removed Gaussian vector. Therefore (6c) gives `||Z_ai||_Lp<=E_M` on
this cavity operator event. If that local proof uses a fixed norm cutoff
on the removed vector, its complement has exponentially small moment
contribution by (5) and the Gaussian vector norm tail.

On the complement of the cavity operator event use the deterministic
bound

\[
 |Z_{ai}|\le\|W_0(i,:)\|_2\|q_a\|_2
               \le CM\sqrt n K_W.
\]

The cavity operator tail is `Ce^{-cn}` and full operator moments of every
fixed order are bounded. Holder consequently makes its pth moment at
most `C M^p n^{p/2}e^{-cn/2}`, which is bounded by E_M above a fixed
width threshold. This proves the unweighted assertion for every fixed p.
Apply Holder once more to this assertion at order 2p and to the weight
at order two. Gaussian operator tails bound that weight moment uniformly
once n exceeds a fixed number depending on the weight. This proves
(6b). In particular, (6b) allows arbitrary dependence of Z and K_W.

### 2b. Upper-velocity pairings

Let g_root denote all standard Gaussian roots, so `W_0=G_0/sqrt(n)`.
For a root perturbation v, the first-variation bounds give

\[
 \|Dq_a[v]\|_2+\|DZ_a[v]\|_2
       +\|Dz_a[v]\|_2+\|Dw[v]\|_2
 \le A_M(K_W)\|v\|_2,                                      \tag{6d}
\]

where A_M(K_W) has the form (5). Indeed q is a bounded local graph
output with bounded derivatives for fixed M. For Z use
`DZ[v]=D W_0[v] q+W_0 Dq[v]`; its direct matrix term is bounded by
`||D G_0[v]||_F ||q||_n <= CM||v||_2`. No maximum coordinate of Z
appears in (6d).

The upper activity velocity has the exact decomposition

\[
 d'_a=a_a\odot Z_a+b_a,\qquad
 a_a=(F_M)_z(z_a,w),                                         \tag{6e}
\]
\[
 b_a=(F_M)_z(z_a,w)\odot
       \left[m^{-1}\sum_c(v'_cK_{ca}+v_cK'_{ca})\right]
       +(F_M)_w(z_a,w)\odot w'.
\]

The vectors a_a,b_a are coordinatewise bounded by fixed constants, and
their ordinary root Jacobians have operator norm at most A_M(K_W).
For a_a this follows from its explicit two scalar derivatives in z,w;
for b_a expand the displayed formula, use `v'_c=-2lambda_c d_c` and
`w'=-2m^{-1}sum_c lambda_c tanh(z_c)`, and differentiate only the smooth
graph factors. The coefficients K',lambda are fixed. All upper scalar
derivatives are bounded uniformly in M. Also
`||Z_a||_2 <= CM K_W sqrt(n)` and
`||d'_a||_2 <= C(1+M K_W)sqrt(n)`.

Consider `X=<d'_a(x),d'_b(y)>_n`. Differentiating (6e), the terms in
DX containing Da_a are the only terms not bounded by (6d) and these
normalized Euclidean norm bounds alone. They have the form

\[
 n^{-1}\langle Da_a(x)[v],
          Z_a(x)\odot\{a_b(y)\odot Z_b(y)+b_b(y)\}\rangle.
\]

Their squared root-gradient norm is bounded by

\[
 \frac{A_M(K_W)^2}{n^2}
       \sum_i C\{|Z_{ai}(x)Z_{bi}(y)|^2+|Z_{ai}(x)|^2\}.
\tag{6f}
\]

Holder and (6b), at sufficiently large fixed moment orders, bound each
weighted summand in expectation by E_M, uniformly in i,x,y. Summing n
terms proves that the expected squared root-gradient norm in (6f) is
at most E_M/n. The analogous terms at time y are identical. All other
terms use Da-free derivatives DZ or Db, whose operator bounds (6d)
pair with a vector of norm at most `C(1+M K_W)sqrt(n)`; Gaussian averaging
of (5) again gives E_M/n. Thus X satisfies (6).

For lower velocity pairings `<q_a(x),q_b(y)>_n`, both factors are
coordinatewise bounded by CM and have ordinary root-Jacobian bound
(6d), so the same conclusion follows directly. Initial covariance and
single-edge integrands in (7) are easier: their undifferentiated initial
outputs are bounded, and a term containing one Z uses its normalized
Euclidean bound. These arguments verify every integrand in (7), without
a generic rule for arbitrary products of graph outputs.

### 2c. Target derivatives of the upper response and the atom

Only one unbounded Z factor occurs in these traces. To verify that fact,
write `J^z_a=D_U z_a`. The upper output derivative is

\[
 D_Ud_a=\operatorname{diag}((F_M)_z)J^z_a
             +\operatorname{diag}((F_M)_w)E_w,
\]

where E_w selects the readout state block. Its activity derivative is

\[
\begin{aligned}
 (D_Ud_a)'={}&
 \operatorname{diag}((F_M)_{zz}z'_a+(F_M)_{zw}w')J^z_a
       +\operatorname{diag}((F_M)_z)(J^z_a)'\\
 &+\operatorname{diag}((F_M)_{wz}z'_a+(F_M)_{ww}w')E_w.
\end{aligned}                                                    \tag{6g}
\]

Here `z'_a=Z_a+m^{-1}sum_c(v'_cK_ca+v_cK'_ca)`, while

\[
 (J^z_a)'=W_0\operatorname{diag}(\psi'(\alpha_a)\alpha'_a)D_U\alpha_a
                      +m^{-1}\sum_cK'_{ca}E_{v_c}.
\]

Every alpha'_a coordinate is bounded by CM. Hence (6g) is a finite sum
of products of regular operator-bounded factors, with at most one
factor `diag(Z_a)`. A regular factor here has operator norm at most
A_M(K_W), and its root variation has ordinary Hilbert--Schmidt norm
at most `A_M(K_W)||v||_2`. This includes Phi by Duhamel and its
Hilbert--Schmidt variation, as well as all source and output factors.

For completeness, consider a normalized trace of such a product. If
there is no Z factor, telescoping the changed factor gives the bound
`A_M(K_W)||v||_2/sqrt(n)`, using the Hilbert--Schmidt norm `C sqrt(n)`
of an unchanged bounded-operator factor. If there is one Z factor,
its Hilbert--Schmidt norm is
`||Z_a||_2<=CM K_W sqrt(n)`, and its varied Hilbert--Schmidt norm is
`||DZ_a[v]||_2<=A_M(K_W)||v||_2`. A change in any other factor is
bounded in the trace by the Hilbert--Schmidt product of that changed
factor and the product containing diag(Z_a). After division by n,
this is again at most `A_M(K_W)||v||_2/sqrt(n)` with A_M enlarged.
A change in diag(Z_a) itself uses its varied Hilbert--Schmidt norm
and `C sqrt(n)` for the remaining regular product. This proof never
uses an operator-norm bound on diag(Z_a).

Apply this trace calculation to (10), using (6g) for the upper case.
The lower case has `(D_Uh_a)'` with bounded diagonal alpha'_a, hence
only regular factors. The direct atom derivative

\[
 D'_{n,a}=n^{-1}\sum_i
      \{(F_M)_{zz}(z_{ai},w_i)z'_{ai}
                       +(F_M)_{zw}(z_{ai},w_i)w'_i\}
\]

has the same one-Z structure. Gaussian averaging of (5) therefore
proves (6) for all the response and atom quantities required below.

This repairs the originally overbroad pairing/trace assertion in this
section. The passive-action moments (6b) precede the strong concentration
and localization; thus the repair does not use the estimate being proved.

## 3. Supremum over both covariance times

Let H denote either h or d, and put
`C(x,y)=<H_a(x),H_b(y)>_n`. The path H is absolutely continuous.
For all x,y, the two-variable fundamental theorem of calculus gives

\[
\begin{aligned}
 C(x,y)=C(0,0)
 &+\int_0^x\langle H'_a(u),H_b(0)\rangle_n\,du\\
 &+\int_0^y\langle H_a(0),H'_b(v)\rangle_n\,dv\\
 &+\int_0^x\int_0^y
           \langle H'_a(u),H'_b(v)\rangle_n\,dv\,du.
\end{aligned}                                                     \tag{7}
\]

For h, the derivative is a finite sum of bounded deterministic lambda
coefficients multiplying smooth graph outputs. For d, differentiating
`d=F_M(z,w)` adds bounded supplied K' coefficients multiplying smooth
graph outputs. Thus every integrand in (7) satisfies (6). The mixed
derivative in (7) differentiates the two separate copies of H once; it
never differentiates lambda, K', or V'.

Subtract expectations in (7), take the supremum over x,y inside the L2
norm, and apply Minkowski to the single and double integrals. Fubini is
justified by (5). Since S<=S_0<=1,

\[
 \left\|\sup_{x,y}|C(x,y)-\mathbb EC(x,y)|\right\|_{L^2}
 \le (1+2S+S^2)E_M/\sqrt n.
\tag{8}
\]

Taking the finite maximum over sample indices proves strong covariance
concentration. In the distance (2), the normalization by S is absorbed
into constants for the fixed nonzero-label problem.

No strong supremum over two passive-velocity times is asserted here.
The passive velocity comparison only needs estimates at a fixed target
time, uniformly in that target. Its source-history comparison is proved
separately in Section 9 below. In particular, that calculation does not
differentiate q or the measurable residual ratio.

## 4. Supremum over response targets, integrated over sources

Fix a source y and a pair a,b. Let T(x,y) be either T^h or T^d in (1).
For x>=y,

\[
 T(x,y)=T(y,y)+\int_y^x\partial_uT(u,y)\,du.                  \tag{9}
\]

The target derivative is obtained by differentiating the output factor
and Phi:

\[
 \partial_xT(x,y)
 =n^{-1}\operatorname{tr}
 \left[\{(D_UH_a)'(x)+D_UH_a(x)L(x)\}\Phi(x,y)J(y)\right],
\tag{10}
\]

where H and J stand for the corresponding lower or upper output/source
pair. For the upper output, the prime also differentiates its supplied
K coefficients. All terms in (10) are finite graph outputs covered by
(5)--(6). They have at most bounded current coefficients lambda and K'.
There is no differentiation in source time and no derivative of lambda.

Subtract expectations in (9) and use (6) and Minkowski. Uniformly in y,

\[
 \left\|\sup_{x\in[y,S]}|T(x,y)-\mathbb ET(x,y)|\right\|_{L^2}
 \le E_M/\sqrt n.                                            \tag{11}
\]

Now use the deterministic source factor in (1). Pathwise,

\[
\begin{aligned}
 \|Q_n-\bar Q_n\|_{\rm row}
 &\le\sum_{a,b}\int_0^S|\lambda_b(y)|
        \sup_{x\in[y,S]}|T_{n,ab}(x,y)-\bar T_{n,ab}(x,y)|\,dy.
\end{aligned}
\]

Applying Minkowski and (11) proves

\[
 \big\|\|Q_n-\bar Q_n\|_{\rm row}\big\|_{L^2}
 \le S E_M/\sqrt n.                                          \tag{12}
\]

The important order is a target supremum for each fixed source, then
source integration. No supremum over source times and no differentiation
of the response density in its source variable is required.

The direct upper atom D_n is a normalized smooth output, is zero at
x=0, and has an integrable activity derivative covered by (6). The
one-variable version of (7) therefore gives

\[
 \big\|\|D_n-\bar D_n\|_\infty\big\|_{L^2}
 \le S E_M/\sqrt n.                                          \tag{13}
\]

Equations (8), (12), and (13) yield

\[
 \|d_H(H_n,\bar H_n)+d_D(D_n,\bar D_n)\|_{L^2}
 \le E_M/\sqrt n.                                            \tag{14}
\]

Here D_n in the last line means the complete upper covariance/response
tuple; its atom was explicitly defined in (1).

## 5. A cavity tuple is close to the full deterministic mean

Let H_n^c,D_n^c be either the row-deleted or column-deleted tuple, always
normalized by 1/n. The earlier deletion argument gives a full/cavity
ordinary state difference bounded by (5). Its normalized covariance
differences are bounded by that quantity divided by sqrt(n), uniformly
over both output times. Its response traces differ by the same factor
uniformly over target and source: use the ordinary Hilbert--Schmidt
difference of the Jacobians, Duhamel, and telescope the trace factors.
Integrating the source coefficient supplies S, exactly as in (12).
The atom is another normalized smooth output.

Gaussian averaging of (5), including the removed vector moments, thus
gives

\[
 \|d_H(H_n^c,H_n)+d_D(D_n^c,D_n)\|_{L^2}
 \le E_M/\sqrt n.
\tag{15}
\]

No cutoff involving the removed vector is used to define these tuples.
Combining (14) and (15),

\[
 \|d_H(H_n^c,\bar H_n)+d_D(D_n^c,\bar D_n)\|_{L^2}
 \le E_M/\sqrt n.                                            \tag{16}
\]

Every quantity in the random tuple on the left is cavity measurable.
The comparison target is deterministic. This distinction permits the
localization in the next section without conditioning a removed Gaussian
row or column on its value.

## 6. Localization to common response rows

Fix inner and outer row bounds B_in < B_out, independent of M,n. Work
on an activity prefix on which the full deterministic mean tuple obeys

\[
 \|\bar Q_h\|_{\rm row}\le B_{\rm in}S,
 \qquad \|\bar D\|_\infty+\|\bar Q_d\|_{\rm row}
                                     \le B_{\rm in}S.
\tag{17}
\]

Assume also the common covariance bounds described in Section 7; those
do not need a response-row bootstrap. Choose a fixed positive margin
eta smaller than B_out-B_in. Define the cavity-measurable event

\[
 \mathcal A_n^c=
 \{\|W_0^c\|_{\rm op}\le K_0\}
 \cap\{d_H(H_n^c,\bar H_n)+d_D(D_n^c,\bar D_n)\le\eta\}.
\tag{18}
\]

The trace rows and atom of the cavity tuple lie in the outer domain on
this event. By (16), Markov, and the Gaussian operator tail,

\[
 \Pr((\mathcal A_n^c)^c)
 \le E_M/n+Ce^{-cn}.                                         \tag{19}
\]

The removed Gaussian row/column remains independent of this event.
The same estimates hold on every prefix with the same constants; source
integrals only become shorter.

On the complement, replace the auxiliary law tuple by one fixed safe
admissible tuple. Do not solve the scalar feedback equations at the bad
random tuple. A finite tagged response has L2 norm at most E_M by (5);
Holder and (19) therefore bound its discarded expected contribution by

\[
 E_M/\sqrt n+E_Me^{-cn/2}.                                   \tag{20}
\]

For a regular response density, the same bound includes its factor
`|lambda_b(y)|`; integrating y preserves (20) after normalization by S.
The estimate is uniform in the target. Bounded state outputs have the
stronger discarded bound E_M/n. Smooth passive velocities and their
tagged responses have fixed moments from (5), and hence satisfy (20).
The safe scalar tuple has the corresponding finite moments from the
separate law estimate, so its contribution on the bad event is bounded
the same way. The exponential terms are absorbed into `E_M/sqrt(n)`
above a fixed width threshold.

If a removed-vector norm cutoff is used during the local Taylor proof,
its exceptional contribution is exponentially small by its independent
Gaussian norm tail and the moments in (5). That auxiliary bound does not
alter (18) or the exact conditional Gaussian covariance identities.

## 7. Why the physical covariance domain is common

On the fixed operator cutoff, the finite histories satisfy the
cap-independent normalized bounds

\[
 \|h'_a(x)\|_n\le C(K_0x+x^3),\qquad
 \|d'_a(x)\|_n\le C(1+S_0^2K_0^2),
\tag{21}
\]

as proved from `|F_M(alpha,P)|<=|P|` and the uniform upper derivatives
in the earlier owned route. Consequently both empirical covariance
kernels have common mean-square increment constants. Their variances
obey `C_h,aa(x,x)<=1` and `C_d,aa(x,x)<=4x^2`.
The full deterministic mean tuple obeys the same type of bounds by
averaging (21) with Gaussian operator moments rather than conditioning
on the cutoff. Constants can be chosen to cover both and the population
tuple. Convex covariance interpolation preserves positive semidefiniteness
and these increment bounds, including singular covariances.

Thus the common law-input domain used here consists of these physical
covariance bounds and the outer response-row bound. The target variation
or pointwise density bound of a response row may still depend on M.
This note does not assert that arbitrary response kernels satisfying the
row bound preserve the covariance increment condition when the law map
is applied. The comparison only uses the actual finite/cavity/population
inputs, whose covariance regularity has separately been verified.

## 8. Scalar reinsertion on the good event

On (18), the upper scalar field has

\[
 z=\gamma+Q_h d+m^{-1}\sum_bv_bK_b,
 \qquad \|Q_h\|_{\rm row}\le B_{\rm out}S.
\]

The upper path maps satisfy
`||Delta w||sup+||Delta d||sup<=CS||Delta z||sup` and
`||Delta v||sup<=CS^2||Delta z||sup`. Therefore its feedback coefficient
is at most `C(1+B_out)S^2`. Choose the common S_0 so this is below 1/2.
This is independent of M and of any pointwise density bound.
The upper scalar field propagates its value remainder with a fixed
factor. A tagged response to a bounded path has the same homogeneous
absorption factor. A regular response at one specified source y needs
an additional qualification: differentiating the instantaneous upper
gate can produce a source term `Q_h(x,y) A(y)`. A row-mass bound alone
does not bound its supremum over x. The physical cavity density retains
the pointwise bound `|Q_h(x,y)|<=E_M |lambda(y)|` from (5), even on the
row-localized event. Use that bound for this source term. Its cost is
linear in E_M; the homogeneous absorption still depends only on the
small row mass. Thus the fixed-source upper tagged comparison has an
E_M prefactor, not necessarily a constant uniform in M. Alternatively
one can integrate source rows before estimating this term. No
pointwise-response bound is inferred from a row-mass bound.

For the lower scalar field,

\[
 P=\xi+D h+Q_d h+m^{-1}\sum_bk_bV_b,
 \qquad \|D\|_\infty+\|Q_d\|_{\rm row}\le B_{\rm out}S.
\]

Its current atom is inside the state ODE. The deterministic difference
bound uses `|(F_M)_alpha|<=CM`, `|(F_M)_P|<=1`, and the common row mass.
The resulting state and tagged-variation comparison constants are at
most

\[
 \exp\{C(1+M+B_{\rm out})S_0\}\le E_M.                      \tag{22}
\]

There is no factor involving the large density/target-regularity bound
in (22). For a tagged source at y, its atom is treated as a jump and the
regular response has its factor `lambda_b(y)`; neither requires dividing
by a residual.

The finite Taylor and differentiated Taylor remainders already have
fixed moments `E_M/sqrt(n)` on the cavity operator cutoff. Multiplying
by (22), or by the upper absorption and the specified-source factor
just described, preserves this form after increasing C in (3).
This proves two-sided scalar state and tagged-response consistency on
(18), including the atom. Off (18), use (20). A passive velocity uses
the same finite graph, its directly computed variation, and (22);
its physical-time discrepancy has the additional factor rho(t).

## 9. Conditional use of the separate strong mean-map estimate

The law route's interface is the following. For any two physical input
tuples in the common covariance/outer-row domain, the deterministic
expectation maps L and U obey

\[
 d_H(LD,L\widetilde D)\le C_LS\,d_D(D,\widetilde D),
 \qquad
 d_D(UH,U\widetilde H)\le C_U\,d_H(H,\widetilde H),
\tag{23}
\]

with constants independent of M and of response density bounds. The
conditional Gaussian derivative-measure moments and insertion moments
underlying these inequalities are uniform on that domain.

To apply it here, first condition on the cavity environment. The random
tuple and the strong distance in (16) are then deterministic, and the
removed Gaussian vector is independent. On (18), covariance interpolation
can therefore factor its strong supremum error outside the conditional
Gaussian expectation. The same operation applies to response-row and
atom errors. Applying (23) and then (16) costs `E_M/sqrt(n)`. On the
complement use the safe tuple and (19)--(20).

Combining this comparison with Section 8 gives, throughout every prefix
where (17) holds, the complete prescribed finite-mean defect

\[
 d_H(\bar H_n,L\bar D_n)
   +d_D(\bar D_n,U\bar H_n)
 \le E_M/\sqrt n.                                            \tag{24}
\]

In the left side the maps include the same prescribed coefficient
histories as the finite system. This is a full-population consistency
source; the population is not defined as the finite mean.
The passive prediction and key-contraction velocities have physical-time
mean consistency error at most `rho(t) E_M/sqrt(n)` by the same argument.

Here are the exact passive statistical bounds used in that last sentence.
Fix a target activity time x, and retain `q_a(x)=h'_a(x)` as a passive
output. Its coefficients lambda(x) are fixed. The covariance data needed
for the joint upper fields `W_0h` and `W_0q(x)` are

\[
 C^{hq}_{n,ab}(y,x)=\langle h_a(y),q_b(x)\rangle_n,
 \qquad C^{qq}_{n,ab}(x,x)=\langle q_a(x),q_b(x)\rangle_n.
\]

The latter has fixed-target root-width fluctuations by (6a),(6d).
For the former, differentiate only its h-history variable y:

\[
 C^{hq}_{n,ab}(y,x)=C^{hq}_{n,ab}(0,x)
       +\int_0^y\langle q_a(u),q_b(x)\rangle_n\,du.
\]

Both factors q in the integrand are coordinatewise bounded by CM and
have the ordinary root-Jacobian bound (6d). Gaussian Poincare and a
one-variable Minkowski integral give an `E_M/sqrt(n)` fluctuation with
supremum over y, uniformly in the fixed x. They do not differentiate
q_b(x), or take a supremum over x inside the random norm.

The passive past response at this fixed target has normalized trace
`n^(-1)tr[D_Uq_a(x)Phi(x,u)J_b(u)]`. All its factors are regular in the
sense of Section 2c: no activity derivative of D_Uq is needed. It has
fixed-(x,u) fluctuations `E_M/sqrt(n)`. Minkowski after integration in
u yields the same bound for its source-integrated error, including
the prescribed source coefficient. Its direct current-carrier atom is
a normalized bounded smooth output and has the same fixed-target bound.
Full-versus-cavity changes obey the corresponding estimates by the
same ordinary state and Hilbert--Schmidt deletion bounds as Section 5.

These covariance and passive-response bounds suffice for the fixed-target
version of the passive Gaussian comparison in Section 10 of the assigned
cavity note. The Gaussian q-coordinate variance is uniformly bounded on
the operator event by (21), even though the simpler coordinate bound on
q is CM. Its output is linear in this extra Gaussian coordinate, and the
core upper-path derivative moments are bounded on the common row domain.
Condition first on the cavity, factor the source-history supremum or
source integral error outside that Gaussian expectation, and apply the
fixed-target bounds just proved. Local state/tagged errors and discarded
events are controlled by Sections 6 and 8. This proves the claimed
physical-time velocity error, with a constant uniform in the fixed target
t. Finally it is integrated against rho(t). No time derivative of q,
no strong all-time passive covariance estimate, and no derivative of a
previous approximation bound is used.

## 10. The exact bootstrap implication

The preceding proof establishes (24) locally in the common domain. To
remove (17), the coordinator may use either of these equivalent inputs
from the separate law argument:

* a strict common-row image margin for the compared physical tuples; or
* a common population tuple with a strict row margin, together with the
  contraction (23) and a common-activity comparison on every prefix.

For the second formulation, choose `C_L C_U S_0<1/2`, and suppose the
population response row norms are at most `B_pop S`, with
`B_pop < B_in < B_out`. On a prefix satisfying (17), (23)--(24) and
substitution give a finite-mean/population distance at most
`C E_M/sqrt(n)`. If n is large enough that this is less than half the
fixed gap `B_in-B_pop`, the mean row norms stay strictly inside (17).

The prefix row norms are continuous in the target endpoint: the finite
state and its propagator are continuous, source coefficients are bounded
and integrable, and the new boundary source interval has vanishing mass.
Expectation preserves this continuity by (5). Initial regular row masses
and the upper atom are zero. Therefore a first exit contradicts the
strict bound. The needed width condition is at most

\[
 n\ge\exp(C(1+M)).                                            \tag{25}
\]

This step does not need a bootstrap of pointwise response density or
row-derivative bounds. It does require the common population margin and
the uniform strong comparison (23); they must be supplied by the separate
law route and checked for the same prescribed histories. Neither follows
from row concentration alone.

Subject to those explicitly identified law inputs, the double and triple
exponentials in the earlier coarse-domain route are avoided. This remains
a cap-dependent exponential estimate, not a uniform-in-M root-width
theorem. The latter still requires the weighted finite-vector tangent
and trace bounds left open in `M_UNIFORM_CAVITY_ROUTE.md`.
