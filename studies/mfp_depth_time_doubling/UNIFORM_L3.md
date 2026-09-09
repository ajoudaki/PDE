# Uniform time doubling at three hidden layers

## 1. Status and exact target

Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

\[
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
 \tag{1.1}
\]

For the width-first three-hidden-layer network, put

\[
 D_{t,3}(h)=F_{t,3}(2h)-F_{2t,3}(h).
\]

The proposed uniform theorem is

\[
 \left|D_{t,3}(h)
 +\frac{t(2t-1)}2J_{\phi,3}h^3\right|
 \le C_{\phi,3}t^4|h|^5,
 \qquad |h|\le c_{\phi,3}/t.                 \tag{1.2}
\]

Here \(J_{\phi,3}\) is the explicit Gaussian activation integral already
computed by the compact cubic recursion.  The limit order is always

\[
 n\to\infty\quad\hbox{at fixed nonzero }h,
 \qquad\hbox{then }h\to0.                    \tag{1.3}
\]

This note does **not** prove (1.2) under (1.1). It proves two ingredients:

1. an exact causal factorization showing that every historical reused-
   matrix response carries its source-time step size; and
2. a precise obstruction showing why the fixed \(L^2\)-operator bridge and
   fixed-history all-moment induction do not yield the horizon-uniform
   \(C^4\) estimate needed by the transported-defect theorem.

Thus the sharp \(t^4\) theorem remains open at \(L=3\). The exact
fixed-\((3,t)\) compiler theorem remains unconditional.

## 2. Exact population network

Let \(H_a=L^2(\Omega_a)\), \(a=1,2,3\), and use the fixed initialization
connectors

\[
 W_2=I_2+J_2^*:H_1\to H_2,
 \qquad
 W_3=I_3+J_3^*:H_2\to H_3,                 \tag{2.1}
\]

with adjoints \(W_a^*=I_a^*+J_a\). The \(I\)- and \(J\)-chaos blocks are
orthogonal, and every \(I_a,J_a\) is an isometry onto its assigned first
Gaussian chaos.  The trainable population parameter is

\[
 \theta=(A,K_3,K_2,u)
 \in H_3\oplus\operatorname{HS}(H_2,H_3)
 \oplus\operatorname{HS}(H_1,H_2)\oplus H_1. \tag{2.2}
\]

Starting from independent standard Gaussian endpoint seeds \(A,U\) and
\(K_2=K_3=0,\ u=U\), one evaluation is

\[
 z_1=u,\quad x_1=\phi(z_1),
\]

\[
 z_2=(W_2+K_2)x_1,\quad x_2=\phi(z_2),
\]

\[
 z_3=(W_3+K_3)x_2,\quad x_3=\phi(z_3),       \tag{2.3}
\]

\[
 r_3=A,\quad \delta_3=r_3\phi'(z_3),
\]

\[
 r_2=(W_3+K_3)^*\delta_3,\quad
 \delta_2=r_2\phi'(z_2),
\]

\[
 r_1=(W_2+K_2)^*\delta_2,\quad
 \delta_1=r_1\phi'(z_1).                    \tag{2.4}
\]

The output and gradient are

\[
 \mathcal F(\theta)=\langle A,x_3\rangle,
\]

\[
 g(\theta)=
 (x_3,\delta_3\otimes x_2,
       \delta_2\otimes x_1,\delta_1).        \tag{2.5}
\]

For a variable step sequence \(\varepsilon=(\varepsilon_s)\), the exact
population Euler recursion is

\[
 \theta_{s+1}=\theta_s+\varepsilon_s g(\theta_s). \tag{2.6}
\]

For every fixed finite sequence, the fixed-operator response identities
identify (2.3)--(2.6) with the inverse-free Gaussian DAG and, by the
width theorem, with the fixed-step limit of the actual finite-width
network.  This statement is pointwise in the step sequence and does not
interchange (1.3).

## 3. The exact coarse/fine reduction

Let

\[
 E_h\theta=\theta+hg(\theta),\qquad
 C_h=E_{2h},\qquad B_h=E_h^2.
\]

Whenever the generated derivatives below are quantitatively controlled,
the algebraic identity

\[
 B_h\theta=C_h\theta+h^2a_h(\theta),
\]

\[
 a_h(\theta)=\int_0^1
 Dg(\theta+shg(\theta))[g(\theta)]\,ds          \tag{3.1}
\]

and pullback telescoping give

\[
 D_{t,3}(h)=h^2Q_{t,3}(h),                       \tag{3.2}
\]

where \(Q_{t,3}\) is a sum of exactly \(t\) transported local defects.
The Gaussian sign involution makes \(D_{t,3}\), hence \(Q_{t,3}\), odd.
Therefore

\[
 \left|D_{t,3}(h)-Q_{t,3}'(0)h^3\right|
 \le { |h|^5\over6}
 \sup_{|v|\le |h|}|Q_{t,3}'''(v)|.             \tag{3.3}
\]

The compact cubic calculation gives, independently of any uniform
estimate,

\[
 Q_{t,3}'(0)=-\frac{t(2t-1)}2J_{\phi,3}.         \tag{3.4}
\]

Thus (1.2) would follow from

\[
 \sup_{|v|\le c_{\phi,3}/t}|Q_{t,3}'''(v)|
 \le 6C_{\phi,3}t^4.                            \tag{3.5}
\]

The abstract recursion in `UNIFORM_BSERIES.md` proves (3.5) if the
reachable population core has a horizon-independent \(C^4\) constant.
The rest of this note identifies exactly what that assertion means for
the reused responses.

## 4. Exact causal factorization of all historical responses

We state the lemma for arbitrary depth because no extra argument is needed
at \(L=3\).

**Lemma 4.1 (source-time divisibility).** Replace the common step by
independent scalar steps \(\varepsilon_0,\ldots,\varepsilon_{N-1}\).
For a connector \(a\), let \(\xi_{a,r}\) be its forward raw source at
time \(r\), and \(\chi_{a,r}\) its transpose raw source. If \(s>r\), then

\[
 \partial_{\chi_{a,r}}x_{a-1,s}
 =\varepsilon_r p^a_{sr},
 \qquad
 \partial_{\xi_{a,r}}\delta_{a,s}
 =\varepsilon_r q^a_{sr},                       \tag{4.1}
\]

where \(p^a_{sr},q^a_{sr}\) are generated fields defined without division
at \(\varepsilon_r=0\). Consequently

\[
 \rho^a_{sr}=\varepsilon_r\bar\rho^a_{sr},
 \qquad
 \sigma^a_{sr}=\varepsilon_r\bar\sigma^a_{sr},
 \qquad r<s,                                    \tag{4.2}
\]

with

\[
 \bar\rho^a_{sr}=\mathbb E[p^a_{sr}],
 \qquad
 \bar\sigma^a_{sr}=\mathbb E[q^a_{sr}].         \tag{4.3}
\]

The current response \(\sigma^a_{ss}\) need not contain a step factor.

**Proof.**  Use the chronological inverse-free DAG with independent step
variables. Before the evaluation at time \(r\), the parameter state
\(\theta_r\) is a function only of sources with time index below \(r\).
The new source \(\chi_{a,r}\) occurs only in the backward evaluation of
\(g(\theta_r)\). It cannot affect any feature at a later time until the
update

\[
 \theta_{r+1}=\theta_r+\varepsilon_rg(\theta_r),
\]

so every directed path from \(\chi_{a,r}\) to \(x_{a-1,s}\), \(s>r\),
contains the displayed edge \(\varepsilon_r\). Differentiating the DAG
and inducting over all nodes after that edge proves the first identity in
(4.1).  The quotient field is constructed by replacing that one edge by
one and then propagating the ordinary source tangent, so it remains
defined when \(\varepsilon_r=0\).

The source \(\xi_{a,r}\) can affect the backward fields during the current
evaluation, which explains the unscaled current response.  Its influence
on a later cotangent must again pass through the update at time \(r\).
The same directed-path induction proves the second identity.  Taking the
response expectations gives (4.2)--(4.3).  This proof is algebraic and
uses neither a Gram inverse nor nonsingularity. \(\square\)

For \(L=3\), Lemma 4.1 rewrites the complete response part of the DAG as

\[
 z_{2,s}=\xi_{2,s}
 +\sum_{r<s}\varepsilon_r
   (Q^1_{rs}+\bar\rho^2_{sr})\delta_{2,r},
\]

\[
 z_{3,s}=\xi_{3,s}
 +\sum_{r<s}\varepsilon_r
   (Q^2_{rs}+\bar\rho^3_{sr})\delta_{3,r},       \tag{4.4}
\]

\[
 r_{2,s}=\chi_{3,s}+\sigma^3_{ss}x_{2,s}
 +\sum_{r<s}\varepsilon_r
   (K^3_{rs}+\bar\sigma^3_{sr})x_{2,r},
\]

\[
 r_{1,s}=\chi_{2,s}+\sigma^2_{ss}x_{1,s}
 +\sum_{r<s}\varepsilon_r
   (K^2_{rs}+\bar\sigma^2_{sr})x_{1,r}.          \tag{4.5}
\]

The endpoint histories are

\[
 A_s=A+\sum_{r<s}\varepsilon_rx_{3,r},
 \qquad
 u_s=U+\sum_{r<s}\varepsilon_r\delta_{1,r}.     \tag{4.6}
\]

Equations (4.4)--(4.6) are an exact Volterra form: there is only one
unweighted current spatial response at each backward connector, and every
strictly historical term has its source-time step weight.

## 5. Normalized responses are transported source tangents

Lemma 4.1 also identifies the missing quantitative object. Perturb one
raw source \(\zeta_r\in\{\xi_{a,r},\chi_{a,r}\}\) while holding the
pre-evaluation state fixed. Let \(b_r\) be the resulting derivative of
the gradient evaluation at time \(r\). The normalized future parameter
tangent \(P_s^r\) satisfies exactly

\[
 P_{r+1}^r=b_r,
\]

\[
 P_{s+1}^r=P_s^r+\varepsilon_sDg(\theta_s)[P_s^r],
 \qquad s>r.                                    \tag{5.1}
\]

Indeed, differentiating (2.6) first gives

\[
 \partial_{\zeta_r}\theta_{r+1}
 =\varepsilon_rb_r,
\]

and thereafter gives the homogeneous tangent recursion.  Equation (5.1)
is valid on the fixed generated core, where the directional derivative is
already justified for every finite history. The fields
\(p^a_{sr},q^a_{sr}\) in Lemma 4.1 are forward/backward components of
(5.1).

Thus the historical sums in (4.4)--(4.5) are controlled uniformly if one
can bound all source injections \(b_r\), their transported tangents
\(P_s^r\), and their first three common-step derivatives by constants
depending only on total variation

\[
 \tau=\sum_s|\varepsilon_s|.                    \tag{5.2}
\]

This is the precise response estimate required at \(L=3\); the time
factor itself has already been exposed.

Two further points about a possible source-sensitivity proof can be closed
without estimating its size.

**Lemma 5.1 (step differentiation at an ordinary source node).** Fix one
primitive Gaussian block in the common operator construction. At ordinary
algebraic, activation, and creation nodes, common-step differentiation of
a first source derivative does not by itself create a second derivative
with respect to that same source block.

**Proof.** Let \(\mathscr D\) denote one local source derivative and
\(\partial\) the common-step derivative. On the fixed Gaussian space they
commute. The only nonlinear rules are

\[
 \mathscr D\phi^{(q)}(Y)=\phi^{(q+1)}(Y)\mathscr DY,
\]

\[
 \mathscr D(YZ)=(\mathscr DY)Z+Y\mathscr DZ.      \tag{5.3}
\]

Applying \(\partial^k\), \(k\le3\), to (5.3) produces products of value
jets and the single-source jets \(\mathscr D\partial^jY\); it never applies
\(\mathscr D\) twice. Creation is linear, so
\(\mathscr D(Jc)=c\) in its own block and zero in an orthogonal block.
This proves the stated nodewise claim. \(\square\)

Lemma 5.1 does **not** prove that a global \(L=3\) ledger containing only
first sensitivities closes. An annihilation response is a deterministic
coefficient times a history field; differentiating that output in a
different incident source block differentiates the history field and can
create mixed source sensitivities. A complete semiring proof must list
those mixed blocks and verify that the resulting finite list closes under
both connectors and all temporal updates. That verification is not
presently available.

The Gaussian accumulation suggested by the Volterra weights also has a
clean horizon-free estimate.

**Lemma 5.2 (weighted correlated-Gaussian envelope).** Let
\(G_0,\ldots,G_{m-1}\) be arbitrarily correlated centered Gaussians with
\(\mathbb EG_s^2\le V^2\). For \(w_s\ge0\), put
\(\tau=\sum_sw_s\). Then, for every \(\lambda\ge0\),

\[
 \mathbb E\exp\!\left(\lambda\sum_sw_s|G_s|\right)
 \le 2\exp\!\left({\lambda^2\tau^2V^2\over2}\right). \tag{5.4}
\]

**Proof.** If \(\tau=0\) the assertion is immediate. Otherwise Jensen's
inequality with weights \(w_s/\tau\) gives

\[
 e^{\lambda\sum_sw_s|G_s|}
 \le\sum_s{w_s\over\tau}e^{\lambda\tau|G_s|}.
\]

For a centered Gaussian of variance at most \(V^2\),

\[
 \mathbb Ee^{a|G|}
 \le\mathbb Ee^{aG}+\mathbb Ee^{-aG}
 \le2e^{a^2V^2/2}.
\]

Average this bound with the Jensen weights. \(\square\)

Lemma 5.2 shows that a pathwise Gronwall factor driven by a weighted sum
of raw Gaussian magnitudes has moments independent of the horizon.  It
does not by itself prove that every term in the \(L=3\) normalized tangent
recursion admits such a linear Gaussian envelope.  In particular, the
matrix-gradient blocks contain products of feature and cotangent fields;
a complete proof must construct a closed subexponential envelope for
those products and for all differentiated current responses.  That finite
semiring estimate is the remaining unproved step.

## 6. The missing \(L=3\) estimate

For a concrete formulation, choose the finite moment set

\[
 \mathcal P_4=\{2,4,8,16,32\}.
\]

A sufficient \(L=3\) response lemma would give activation-defined
\(R_{\phi,3}<\infty\) and \(c_{\phi,3}>0\) such that, whenever
\(\tau\le c_{\phi,3}\), the following quantities are at most
\(R_{\phi,3}(1+A)^k\) for every \(p\in\mathcal P_4\), \(0\le k\le3\),
and every horizon:

\[
 \|\partial_h^kY_s\|_{L^p},
 \qquad
 Y\in\{x_a,z_a,r_a,\delta_a:1\le a\le3\},       \tag{6.1}
\]

and

\[
 \left\|\partial_h^k
  \sum_{r<s}\varepsilon_r\bar\rho^a_{sr}\delta_{a,r}
 \right\|_{L^p},
 \qquad
 \left\|\partial_h^k
  \sum_{r<s}\varepsilon_r\bar\sigma^a_{sr}x_{a-1,r}
 \right\|_{L^p},                                 \tag{6.2}
\]

for \(a=2,3\). Here \(A=\sum_s|\partial_h\varepsilon_s|\); for the
coarse/fine strings \(A\le4t\). The same estimate is required for the
interpolated defect and transported tangent generated by (3.1).
Leibniz and Hölder over the finite set \(\mathcal P_4\), followed by the
explicit recursion of the abstract defect theorem, would then give
(3.5) and hence (1.2).

Lemma 4.1 proves that every summand in (6.2) has the correct step weight.
It does **not** bound the normalized tangents in (5.1).  The fixed-core
argument proves only that each one has all finite moments for a fixed
horizon.  Its bound may depend on the number of exposed source directions.
No estimate (6.1)--(6.2), or an equivalent horizon-free estimate, is
proved in the current study.

## 7. Why the existing operator bridge cannot supply (6.1)--(6.2)

The failure is stronger than the statement that \(J_a^*\) is not bounded
on ambient \(L^p\).

**Proposition 7.1 (no all-moment layer-transfer bound).** Fix \(p>2\)
and a connector \(W=I+J^*\). There are inputs \(x_m\) whose laws are all
exactly \(N(0,1)\), but for which

\[
 \|Wx_m\|_{L^p}\longrightarrow\infty.           \tag{7.1}
\]

Every coefficient used to construct \(x_m\) can be chosen in
\(\bigcap_{q<\infty}L^q\).

**Proof.** On the target Gaussian space choose events \(E_m\), measurable
in an unused chaos block, with probabilities \(e_m\downarrow0\), and put

\[
 c_m={\mathbf1_{E_m}\over\sqrt{e_m}}.
\]

Then \(c_m\in L^q\) for every finite \(q\),

\[
 \|c_m\|_2=1,
 \qquad
 \|c_m\|_p=e_m^{1/p-1/2}\longrightarrow\infty.
\]

Set \(x_m=Jc_m\). Since \(J\) is an isometry onto first Gaussian chaos,
every \(x_m\) is a standard Gaussian and hence has the same moments of
all orders. Also \(J^*x_m=c_m\). The variable \(Ix_m\) is a standard
Gaussian in a block independent of \(E_m\), so

\[
 \|Wx_m\|_p
 =\|Ix_m+c_m\|_p
 \ge \|c_m\|_p-\|Ix_m\|_p\longrightarrow\infty.
\]

This proves (7.1). \(\square\)

Both \(W_2\) and \(W_3\) in the three-layer model contain exactly this
connector.  Therefore no induction based only on Gaussian input moments,
all-moment membership, or the \(L^2\) operator norm of \(W_a\) can prove a
uniform \(L^p\) estimate. It must use the causal fact that the actual
coefficients \(c_m\) are transported network cotangents and that all
historical occurrences have the weights in (4.4)--(4.5).

There is a second independent obstruction to applying an ambient Banach
theorem.  On a nonatomic probability space,

\[
 v_m=\sqrt m\,\mathbf1_{[0,1/m]}
\]

satisfies \(\|v_m\|_2=1\) but \(\|v_m^2\|_2=\sqrt m\). Hence pointwise
multiplication \(L^2\times L^2\to L^2\) is unbounded. For a nonlinear
activation, the second Nemytskii derivative contains precisely this
product.  The population gradient is therefore not furnished with the
ambient \(C^4\) structure assumed by the abstract theorem.

Proposition 7.1 is not a counterexample to (1.2), because the pathological
\(c_m\)'s have not been shown reachable from the network initialization.
It is a rigorous obstruction to deriving (1.2) from the present fixed-
operator bridge.  Closing (1.2) requires a new dynamical estimate for the
special reachable class.

## 8. General-depth induction criterion

The causal factorization itself is depth-independent.  At every new
connector \(a\), the forward and backward assignments have the form

\[
 z_{a,s}=\xi_{a,s}
 +\sum_{r<s}\varepsilon_r
   (Q^{a-1}_{rs}+\bar\rho^a_{sr})\delta_{a,r},
\]

\[
 r_{a-1,s}=\chi_{a,s}+\sigma^a_{ss}x_{a-1,s}
 +\sum_{r<s}\varepsilon_r
   (K^a_{rs}+\bar\sigma^a_{sr})x_{a-1,r}.        \tag{8.1}
\]

Thus a general-depth proof can proceed inductively if one proves a
**causal layer-transfer lemma**: for each \(a\), bounded lower-layer value,
common-step, and normalized-source-tangent ledgers satisfying a total-
variation bound imply the corresponding upper-layer ledgers, with an
explicit map

\[
 R_a=\Gamma_{\phi,a}(R_{a-1}),                  \tag{8.2}
\]

independent of the horizon and of the ranks of all history Grams.  Starting
from the endpoint Gaussian ledger, the finite recursion

\[
 R_1=R_{\phi}^{\rm end},\qquad
 R_a=\Gamma_{\phi,a}(R_{a-1}),\quad2\le a\le L, \tag{8.3}
\]

would terminate after \(L-1\) assignments. A reverse pass of the same
form would close the cotangents.  The transported-defect theorem would
then give \(C_{\phi,L}=C_{K_{\phi,L}}\) and the explicit \(t^4\) factor.

Equations (8.1)--(8.3) identify the correct depth induction, but no map
\(\Gamma_{\phi,a}\) satisfying the required horizon-free normalized-
tangent estimates is currently proved.  Proposition 7.1 shows that
\(\Gamma_{\phi,a}\) cannot be an ambient \(L^p\) connector norm; it must
be a theorem about the reachable Volterra class.

## 9. Final conclusion

At \(L=3\), the exact coefficient, the width-first fixed-step
identification, the local \(h^2\) defect, oddness, and the \(t^4\) time
combinatorics are all established.  The historical response terms also
have the exact source-time factors required for a total-variation proof.

The remaining bridge is substantive: prove (6.1)--(6.2), equivalently a
causal layer-transfer lemma controlling (5.1), with constants independent
of the horizon.  The existing fixed-history core theorem proves
differentiability and finiteness but not this estimate.  Therefore an
unconditional statement of (1.2) under only (1.1) would presently be
incorrect.
