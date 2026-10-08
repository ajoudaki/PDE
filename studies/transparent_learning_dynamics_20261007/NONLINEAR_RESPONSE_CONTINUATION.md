# Nonlinear response continuation on small activity windows

2026-10-07. Scoped continuation of the two-hidden-layer candidate.

## Result and limitation

There is a genuine nonlinear local continuation theorem for the first
response densities, conditional on explicit primal exponential budgets
and already constructed past responses. It is not a bounded-tangent
assumption: on the new window the unknown response kernels are obtained
by a contraction, and their bounds follow from the equations.

The first window requires no past tangent input. A later window needs
quantified moments of its previously constructed tangent history.
The resulting density bound excludes additional diagonal atoms.
However, finite total residual activity alone does not prove that these
windows cover all time. The continuation constants depend on old tangent
history, and the moment estimates lose integrability unless stronger
information is available. Thus this note neither shrinks the admitted
labels globally nor proves the original all-time susceptibility claim.

Inputs were the complete CANDIDATE_SYSTEM.md at SHA-256
a5fa62c596b5816859589be7af686829a5f4f65ddb8406138e15cf4468a45c31,
CANDIDATE_CLOSURE_CHECK.md at
c00e4fb7a511e972831e59b6f523581955cee1f0007201ce7f24dbd77684171d,
the previously read CAUSAL_KERNEL_DYNAMICS.md, and my own
CONTINUOUS_SUSCEPTIBILITY.md and OSGOOD_RESPONSE_STABILITY.md.
No other study or literature was used.

## 1. The actual nonlinear tangent equations

Use \(u_a=z_{1,a}\), \(v_a=z_{2,a}\), and \(k_a=b_{1,a}\). The top carrier
is \(w\). Put
\[
h_a=\phi_1(u_a),\qquad q_a=\phi_2(v_a),\qquad
d_a=w\phi_2'(v_a),\qquad
\beta_b(t)=2c_b(t)/m,\quad
a(t)=\sum_{b\le m}|\beta_b(t)|.
\]
For passive indices set \(\beta_b=0\). The input Gram satisfies
\(|S_{ab}|\le1\). Write
\[
C_{ab}(t,s)=\mathbb E[h_a(t)h_b(s)],\qquad
D_{ab}(t,s)=\mathbb E[d_a(t)d_b(s)],\qquad
\chi_a(t)=\mathbb E[w(t)\phi_2''(v_a(t))].
\]

Every strict-past response has its source learning factor. Write
\[
R^h_{ab}(t,s)=\beta_b(s)r_{ab}(t,s),\qquad
R^\delta_{ab}(t,s)=\beta_b(s)\rho_{ab}(t,s),\qquad s<t.
\tag{1}
\]
This is a factorization, not division by a possibly zero residual. The
normalized fields below are defined by their equations even when
\(\beta_b(s)=0\); multiplying by \(\beta_b(s)\) recovers the physical
probe response. Induction in the finite Euler circuit gives exactly this
factorization with an additional mesh factor on its response masses.

Let \(p_{ab},v_{ab}^{\rm tan},t_b\) denote the normalized responses of
\(u_a,v_a,w\), respectively, to a primitive probe born at \(s\).
The upper \(v^{\rm tan}\) excludes the direct same-time Gaussian impulse.
For brevity write \(V_{ab}=v_{ab}^{\rm tan}\). Define
\[
\begin{aligned}
j_{ab}(r,s)
={}&\chi_a(r)\phi_1'(u_a(r))p_{ab}(r,s)\\
&+\sum_i\int_s^r\beta_i(q)
[\rho_{ai}(r,q)+D_{ai}(r,q)]
\phi_1'(u_i(q))p_{ib}(q,s)\,dq .
\end{aligned}
\]
Then the lower equations are
\[
\begin{aligned}
p_{ab}(t,s)
={}&S_{ab}\phi_1'(u_b(s))\\
&+\sum_j S_{aj}\int_s^t\beta_j(r)
\left[
\phi_1''(u_j(r))k_j(r)p_{jb}(r,s)
+\phi_1'(u_j(r))j_{jb}(r,s)
\right]dr,\\
r_{ab}(t,s)&=\mathbb E[\phi_1'(u_a(t))p_{ab}(t,s)].
\end{aligned}
\tag{2}
\]
The upper equations are
\[
\begin{aligned}
t_b(t,s)
={}&\phi_2'(v_b(s))
+\sum_j\int_s^t\beta_j(r)\phi_2'(v_j(r))V_{jb}(r,s)\,dr,\\
V_{ab}(t,s)
={}&[r_{ab}(t,s)+C_{ab}(t,s)]w(s)\phi_2''(v_b(s))\\
&+\sum_j\int_s^t\beta_j(r)[r_{aj}(t,r)+C_{aj}(t,r)]
\left[\phi_2'(v_j(r))t_b(r,s)
+w(r)\phi_2''(v_j(r))V_{jb}(r,s)\right]dr,\\
\rho_{ab}(t,s)
={}&\mathbb E\left[
\phi_2'(v_a(t))t_b(t,s)
+w(t)\phi_2''(v_a(t))V_{ab}(t,s)\right].
\end{aligned}
\tag{3}
\]
All deterministic population coefficients are frozen under the defining
probe. Thus (2)--(3) contain first tangents only. Their random coefficients
are the actual nonlinear derivative gates and carriers, not a linear
activation approximation.

The separate diagonal measure remains
\(\mathbf1_{\{a=b\}}\chi_a(t)\delta_t(ds)\). Nothing below folds that atom
into \(\rho\).

## 2. Primal assumptions and an exponential-integral estimate

On the relevant bounded horizon assume:

- All first and second activation derivatives are bounded by \(L\ge1\).
  Strip analyticity supplies these bounds and the continuity needed below.
- \(|C_{ab}|,|D_{ab}|\le K\), with \(K\ge1\).
- With \(K_{\rm car}(t)=\max_{j\le m}|k_j(t)|\), there are \(A\ge1\),
  \(M\ge2\) such that
  \[
  \sup_t\mathbb E e^{K_{\rm car}(t)/A}\le M,\qquad
  \sup_t\mathbb E e^{|w(t)|/A}\le M.
  \tag{4}
  \]
- Primal fields are jointly measurable and continuous in the required
  population \(L^q\) norms. Uniform \(L^2\) continuity together with
  uniform exponential tails gives the needed continuity for the carriers
  and readout at every finite \(q\). Other primal preactivations only need
  convergence in probability for their bounded derivative gates.

Neither activation values nor preactivations are assumed bounded.
The feature values enter through the displayed Gram bound, not through
a pointwise feature cap. Individual training-carrier budgets imply the
first bound in (4), with a factor at most \(m\) in \(M\).

Set
\[
W=\max\{1,A(8!M)^{1/8}\}.
\tag{5}
\]
Then \(\sup_t\|w(t)\|_8\le W\) and \(|\chi_a(t)|\le LW\).

The following estimate avoids a pathwise carrier maximum. If \(X(t)\ge0\),
\(\sup_t\mathbb E e^{X(t)/A}\le M\), and
\(\delta=\int_I a(t)\,dt\), then
\[
\left\|\exp\left(\lambda\int_I a(t)X(t)\,dt\right)\right\|_q
\le M^{\lambda A\delta},
\qquad q\lambda A\delta\le1.
\tag{6}
\]
For \(\delta>0\), Jensen first bounds the exponential of the weighted
integral by the weighted integral of the exponential. Concavity of
\(x^\theta\), with \(\theta=q\lambda A\delta\le1\), then bounds that
expectation by \(M^\theta\). Taking the \(q\)-th root proves (6).
The case \(\delta=0\) is immediate. The same proof works for Euler sums.

Only \(\sup_t\mathbb E e^{X(t)/A}\) is used. The stronger
\(\mathbb E e^{\sup_tX(t)/A}\) is not assumed.

## 3. A proved fresh-probe window

Fix \(I=[\tau,T]\), and first consider probe times \(s\ge\tau\).
They have no pre-\(\tau\) tangent history. Put
\[
\delta=\int_\tau^T a(t)\,dt,\quad
X=2L^2,\quad Z=X+K,\quad
U_0=L(1+ZW),\quad Y=2L(1+W)U_0.
\]
Also define
\[
\begin{aligned}
c_p&=L^3W+LA\log M,\\
c_u&=L(1+Z)+LZA\log M,\\
\mathcal L_u&=L^2(1+W)[2W+4U_0(1+W)].
\end{aligned}
\]
All are explicit primal constants. Suppose
\[
\begin{gathered}
\delta\le1,\qquad 8LZA\delta\le1,\qquad c_u\delta\le\log2,\\
c_p\delta+L^2(Y+K)\delta^2\le\log2,\qquad
4L^4\mathcal L_u\delta^2\le\tfrac12 .
\end{gathered}
\tag{7}
\]
These conditions hold on a sufficiently small activity window for every
finite set of primal constants; they are not a global label restriction.

**Fresh-probe theorem.** Equations (2)--(3), with given primal paths, have
a unique bounded continuous deterministic kernel pair in the box
\[
|r_{ab}(t,s)|\le X,\qquad |\rho_{ab}(t,s)|\le Y,
\qquad \tau\le s\le t\le T.
\tag{8}
\]
The corresponding random first tangents satisfy, uniformly in their
source indices and source time,
\[
\left\|\sup_{s\le t\le T}\max_a|p_{ab}(t,s)|\right\|_4\le2L,\qquad
\left\|\sup_{s\le t\le T}
\max\{|t_b(t,s)|,\max_a|V_{ab}(t,s)|\}\right\|_4\le2U_0.
\tag{9}
\]
Uniqueness here is in the stated box, which is the class selected by the
uniform Euler bounds below.

### Lower map

Given a deterministic \(\rho\) with norm at most \(Y\), solve the linear
random Volterra equation (2). For a fixed source, its absolute envelope
is bounded by
\[
p_*\le
L\exp\left[
L\int_s^T a(r)K_{\rm car}(r)\,dr+
L^3W\delta+L^2(Y+K)\delta^2
\right].
\tag{10}
\]
The double integral in (2) is bounded after exchanging integration order
by \(\delta\int a(r)p_*(r)\,dr\); ordinary integral Gronwall then gives
(10). Its random time coefficient is integrable almost surely by (4)
and Fubini, so the linear Volterra equation itself exists by successive
iteration. Formula (6) and (7) give (9)'s lower bound and
\(\|r\|_\infty\le X\).

For two inputs \(\rho,\widetilde\rho\), subtraction gives an inhomogeneous
term bounded by \(L^2\delta^2\|\rho-\widetilde\rho\|_\infty\widetilde p_*\).
The same resolvent estimate and Hölder, using the two \(L^4\) bounds,
give
\[
\|r-\widetilde r\|_\infty
\le4L^4\delta^2\|\rho-\widetilde\rho\|_\infty.
\tag{11}
\]

### Upper map

Given \(r\) with norm at most \(X\), solve (3)'s linear random Volterra
equations. With \(I_w=\int_s^T a(r)|w(r)|\,dr\),
\[
U_*\le L(1+Z|w(s)|)
\exp\{L(1+Z)\delta+LZI_w\}.
\tag{12}
\]
Indeed the sum of the two integral inequalities for \(t_b,V_{\cdot b}\)
has coefficient at most \(L(1+Z)+LZ|w(r)|\).
Hölder with exponents \(8,8\), followed by (6), gives
\(\|U_*\|_4\le2U_0\). Hence
\[
\|\rho\|_\infty
\le L(1+W)\|U_*\|_2\le Y.
\]

If \(r,\widetilde r\) differ by \(\varepsilon\), subtraction and the same
resolvent give
\[
\|\Delta U_*\|_2
\le L\varepsilon[2W+4U_0\delta(1+W)].
\]
To check the unbounded factor: the inhomogeneous bound is
\[
L\varepsilon\left[
|w(s)|e^J+
L(1+Z|w(s)|)(\delta+I_w)e^{2J}\right],
\quad J=L(1+Z)\delta+LZI_w.
\]
The polynomial part has an \(L^4\) bound using \(\|w\|_8\), and
\(\|e^{2J}\|_4\le e^{2c_u\delta}\le4\) follows from the factor \(8\)
in (7). Therefore
\[
\|\rho-\widetilde\rho\|_\infty
\le\mathcal L_u\|r-\widetilde r\|_\infty.
\tag{13}
\]

Compose the upper map with the lower map. Equations (11)--(13) and (7)
make it a contraction, of constant at most \(1/2\), on the closed \(r\)
ball. It maps that ball into itself. Its iterates are uniformly Cauchy,
and the fixed point gives (8)--(9). Continuity follows from the linear
Volterra equations and primal \(L^q\) continuity, using (10)--(12) for
uniform integrability. This proves the nonlinear theorem.

## 4. Continuation must also transport old probes

Restarting only the fresh-probe theorem would discard the old response
memory and would not continue the actual candidate. Here is a sufficient
old-history extension.

Suppose the kernels and their random tangents have already been
constructed on \(0\le s\le t\le\tau\). Define the normalized old gated
upper tangent
\[
\zeta_{jb}(r,s)=
\phi_2'(v_j(r))t_b(r,s)
+w(r)\phi_2''(v_j(r))V_{jb}(r,s).
\]
For the following suprema, sources range over \(b\le m,\,0\le s\le\tau\).
Use these finite, previously proved history summaries:
\[
\begin{aligned}
P_0&=\max\left\{L,\sup_{b,s}\max_a\|p_{ab}(\tau,s)\|_8\right\},\\
H_0&=\sup_{b,s}\int_s^\tau a(r)\max_a\|p_{ab}(r,s)\|_8\,dr,\\
T_0&=\max\left\{L,\sup_{b,s}\|t_b(\tau,s)\|_8\right\},\\
J_0&=LW+
\sup_{b,s}\int_s^\tau a(r)\max_j\|\zeta_{jb}(r,s)\|_8\,dr.
\end{aligned}
\tag{14}
\]
There is no new bound on unknown future tangents in (14). These are
certificates from the completed history. If they have not been proved
finite, this continuation theorem cannot be invoked.

On \([\tau,T]\) put
\[
X=4LP_0,\quad Z=X+K,\quad U_0=T_0+ZJ_0,\quad
Y=2L(1+W)U_0,
\]
and retain \(c_p=L^3W+LA\log M\) and
\(c_u=L(1+Z)+LZA\log M\). Set
\[
\mathcal L_u=L(1+W)[2J_0+4LU_0(1+W)].
\]
It is sufficient to choose \(\delta=\int_\tau^T a\) so that
\[
\begin{gathered}
\delta\le1,\quad8LZA\delta\le1,\quad c_u\delta\le\log2,\\
c_p\delta+L^2(Y+K)\delta^2\le\log2,\quad
L^2\delta(Y+K)H_0\le P_0,\\
L^3\delta(2H_0+8\delta P_0)\mathcal L_u\le\tfrac12.
\end{gathered}
\tag{15}
\]
Every finite history summary permits some positive activity window.

**Old-history continuation theorem.** Under (14)--(15), the previously
constructed response law has a unique continuation in the box
\(|r|\le X,|\rho|\le Y\) for all new rows \(t\in[\tau,T]\) and all
source times \(0\le s<t\). It includes fresh sources and old sources.
The new random tangents obey \(L^4\) bounds
\[
\sup_{b,s}\|p_*\|_4\le4P_0,\qquad
\sup_{b,s}\|U_*\|_4\le2U_0.
\tag{16}
\]

### Proof of the additional estimates

For an old source split (2) at \(\tau\). Its lower initial condition is
\(p(\tau,s)\). In the nested memory integral, sources \(q<\tau\) now
contribute an inhomogeneous term with \(L^8\) norm at most
\[
L^2\delta(Y+K)H_0.
\]
The remaining homogeneous resolvent is the new-window exponential in
(10). Hölder and (15) therefore give
\(\|p_*\|_4\le2[P_0+L^2\delta(Y+K)H_0]\le4P_0\).
The lower output is bounded by \(X\).

For two prospective upper response kernels, the old portion of the
inhomogeneous difference costs
\(L^2\delta H_0\|\Delta\rho\|_\infty\), while the new portion costs
\(L^2\delta^2\widetilde p_*\|\Delta\rho\|_\infty\).
The resolvent and Hölder yield
\[
\|\Delta r\|_\infty
\le L^3\delta(2H_0+8\delta P_0)\|\Delta\rho\|_\infty.
\tag{17}
\]
This is the crucial old-history cost: it is generally order \(\delta\),
not order \(\delta^2\).

For the upper equation, its past portion becomes the forcing
\[
[r_{ab}(t,s)+C_{ab}(t,s)]w(s)\phi_2''(v_b(s))
+\sum_j\int_s^\tau\beta_j(q)
[r_{aj}(t,q)+C_{aj}(t,q)]\zeta_{jb}(q,s)\,dq.
\]
Its time-supremum has \(L^8\) norm at most \(ZJ_0\), and its change
under an input change \(\Delta r\) is at most
\(J_0\|\Delta r\|_\infty\). The readout-tangent initial condition is
\(t_b(\tau,s)\), of norm at most \(T_0\).
The same calculation as (12)--(13) gives (16), the bound \(Y\), and
\[
\|\Delta\rho\|_\infty\le\mathcal L_u\|\Delta r\|_\infty.
\tag{18}
\]
The product of (17) and (18) is at most \(1/2\). The fixed-point
construction consequently extends all old and new responses.
Boundary values at \(t=\tau\) remain the already constructed values.

## 5. What this proves for response measures and Euler limits

On any covered window, every new response row satisfies
\[
|R^h_{ab}(t,s)|\le X|\beta_b(s)|,\qquad
|R^\delta_{ab}(t,s)|\le Y|\beta_b(s)|,\qquad s<t.
\tag{19}
\]
Thus its strict-past total variation is at most
\(\max(X,Y)\int_0^t a(s)\,ds\). Its mass in an interval of length shrinking
to zero tends to zero by absolute continuity of the activity integral.
No extra atom can concentrate at \(s=t\). The only diagonal atom is the
explicit \(\chi_a(t)\delta_t\).

For actual finite Euler circuits the same estimates apply to
\[
R^h_{ab}(k,j)=\Delta\beta_b^j r_{ab}^{\Delta}(k,j),\qquad
R^\delta_{ab}(k,j)=\Delta\beta_b^j\rho_{ab}^{\Delta}(k,j),\quad j<k,
\]
with sums replacing integrals. Positive-factor bounds use
\(1+x\le e^x\); (6) holds for weighted sums. A strict margin in (7) or
(15) gives uniform constants and a uniform contraction margin.

To conclude that these discrete responses converge to the displayed
continuous kernels, one additionally needs the primal Euler paths to
converge in their common realization and to satisfy the same exponential
budgets uniformly in the mesh. Uniform \(L^2\) primal convergence plus those
uniform tails gives the finite-\(q\) convergence used in the tangent maps.
For a fixed continuous trial kernel, truncate the carriers, pass its
bounded-coefficient Riemann sums to the linear Volterra equations, and
remove the truncation using (6), (10), and (12). This gives uniform
consistency on the triangular time domain. Subtracting the continuous
fixed-point equation from its discrete version then bounds kernel error
by consistency error divided by the common contraction margin.

This is an explicit conditional derivative-passage argument, not just
formal differentiation. The associated random tangent fields converge in
the integrable norms used to define their expectations.

There is an important provenance distinction. The Osgood comparison of
exact dense flow with Euler only needed exact-reference carrier tails.
It does not, by \(L^2\) closeness alone, give a uniform exponential budget
for Euler carriers. If the available source provides only exact-flow
budgets, that extra mesh-uniform premise remains to be established before
using this paragraph for the actual Euler response limit.

## 6. Why finite total activity does not finish the continuation

The theorem imposes no new cap on the labels. Given finite constants,
one can always choose a sufficiently short activity window. Nevertheless
the following two obstructions prevent an unqualified all-time conclusion.

### A. Old-history amplification is part of the next step size

The constants \(P_0,H_0,T_0,J_0\) enter the next kernel caps \(X,Y\) and
the contraction condition (15). A finite number
\(\int_0^\infty a(t)\,dt\) does not bound those tangent-history quantities.
The admissible increments may shrink as the response grows. There is
no established lower bound on the total activity covered by indefinitely
many admissible windows. Replacing them by a fixed partition of the
residual-activity budget would silently omit (17).

### B. The estimate consumes old tangent integrability

The continuation above assumes old \(L^8\) history summaries and produces
new \(L^4\) bounds for \(p,t,V\). The gated upper tangent also multiplies
\(V\) by \(w\), so it is immediately controlled in \(L^2\), not in \(L^8\).
One cannot reuse (14) on the next window merely by citing (16).

The estimates have higher-moment versions: start with higher old moments,
replace the factor \(8\) in the exponential condition by the corresponding
Hölder exponent, and obtain a prescribed finite lower moment after the
window. This proves any specified finite chain when its required moment
certificates and activity margins are supplied. It does not preserve all
moments under an arbitrary positive activity increment from the fixed
exponential premise (4).

This limitation reflects a real property of exponential estimates, not
just notation. A bound on \(\mathbb E e^{|k|/A}\) only controls moment
generating functions up to its supplied exponential radius. The
variational resolvents contain
\(\exp(L\int a|k|)\). Finite activity need not remain below that radius
after accumulated amplification. Osgood stability of primal values does
not control this derivative.

For example, the nonlinear gated equation
\(\dot u=Z\sin u,\ u(0)=0\), with nonnegative unit-rate exponential \(Z\),
has zero unperturbed solution and \(\mathbb E e^{Z/2}=2\), but its
initial-probe derivative is \(e^{tZ}\), whose expectation diverges at
\(t\ge1\). This is an obstruction to an abstract inference from (4) and
finite activity, not a claimed counterexample to the canonical
Gaussian-initialized neural model.

Uniform sub-Gaussian carrier control would remove this particular
exponential-radius restriction, because every linear exponential moment
would then be finite. It would not by itself bound the old-history
amplification constants in (15). That is a separate continuation estimate.

## 7. Scope of the progress

The nonlinear two-layer first-response system has a constructive
small-activity window theorem, including an explicit old-probe extension.
It accommodates unbounded activation values and identifies a sufficient
condition excluding all extra diagonal atoms. Its proof works through
the actual first tangent equations, with correlations between carriers
and tangents retained.

What remains is a uniform control of the certified history summaries,
enough integrability to restart them, and—if only exact-flow tails are
available—a mesh-uniform primal-tail argument. Neither finite residual
activity nor the original label admissibility has been shown here to
supply these missing bounds. There is therefore no additional global
label shrinkage and no all-time susceptibility theorem claimed.
