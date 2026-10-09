# Terminal program representations: exact TP expectations and a streamed numerical optimizer

2026-10-08. Scoped independent route, updated only after the supervisor supplied
the user's declared-query clarification and authorized the named imports.
Status: candidate arguments pending independent reconstruction. No experiment,
code change, paper edit, Git operation, or independent probability-proof audit.
The focused update below incorporates the authorized, internally reconstructed
adaptive-clock source construction; its third logarithmic power supersedes
the fifth-power inventory used in this note's first version.

The strongest representation conclusion is positive and conditional: the
authorized finite-panel construction can be compiled into a finite numerical
arithmetic program whose resident real-scalar inventory is polynomial in
\(m,d,\gamma^{-1}\) and polylogarithmic in \(n\), at fixed activation,
depth and admissible label parameters. The strongest authorized inventory is
\(O(\log^3(en))\) at fixed problem parameters, with its additional
\(\log^2(en)\log^2(e+\log(en))\) term displayed below. Streaming an arbitrarily long finite
Euler calculation does not increase that inventory by the step count. This
is a numerical tensor-arithmetic program, not an application of the standard
population tensor-program master theorem to its selected small matrices.
The distinction matters because the latter represents training by growing
Gaussian source and response histories. Neither distinction is a no-go
theorem for the other representation.

Two missing upgrades must remain visible: the imported scalar count does not
prove a polylogarithmic bit count, and the imported dense-pair lower bound
concerns a whole-trajectory panel norm, not variability of terminal outputs
at each run's own loss stopping time.

## 1. Contract and canonical dense model

The current contract has \(m\) training examples and \(p=O(1)\) passive
query inputs, all declared at initialization. Passive labels are unavailable
and unused. The requested observables are the \(p\) predictions at a
specified loss stopping rule. Setup, total integration work, resident state,
temporary workspace, executable description, and scalar precision are
different resources. There is no fast-setup requirement in this route.

Write \(v_i=x_i/\sqrt d\), with \(\|v_i\|_2=1\), and let
\(A=W^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\), \(2\le\ell\le L\), and
\(w=W^{(L+1)}\in\mathbb R^n\). The model is

\[
z_i^{(1)}=Av_i,\qquad z_i^{(\ell)}=W^{(\ell)}h_i^{(\ell-1)},
\qquad h_i^{(\ell)}=\phi_\ell(z_i^{(\ell)}),\qquad
f_{n,i}=w^Th_i^{(L)}/n.
\]

For training indices \(a\le m\), put \(r_a=f_{n,a}-y_a\) and
\(\mathcal L_n=m^{-1}\sum_a r_a^2\). Define the residual-free backward
coordinates

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)T}\delta_a^{(\ell+1)}.
\]

With block mobilities \((n,1,\ldots,1,n)\), the exact flow is

\[
\begin{aligned}
\dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,\\
\dot W^{(\ell)}&=-\frac2{mn}\sum_a
r_a\delta_a^{(\ell)}h_a^{(\ell-1)T},\\
\dot w&=-\frac2m\sum_a r_ah_a^{(L)}.
\end{aligned}                                                    \tag{1}
\]

The first entries are independent \(N(0,1)\), hidden entries independent
\(N(0,1/n)\), and \(w(0)=0\). Layers are independent at initialization.
Activations are real on the real line and holomorphic on a complex strip
with bounded first derivative there. Their values may grow linearly.
For numerical claims, activation values and derivatives also need an
effective evaluation procedure; analyticity alone is not a computability
assumption. Bounded derivative on the complex strip supplies bounded real
higher derivatives by Cauchy's formula on a smaller strip. No bounded-value
activation hypothesis is introduced.

The allowed model has full nonlinear hidden updates, both directions of
the same initialized Gaussian matrices, and the stated physical clock.

## 2. What the exact finite-step TP compiler retains

Fix a mesh length \(h>0\) and \(N\) explicit Euler updates of (1).
Unrolling trained matrices is an exact finite identity:

\[
W_k^{(\ell)}=W_0^{(\ell)}-
\frac{2h}{mn}\sum_{s<k,b}r_{s,b}
\delta_{s,b}^{(\ell)}h_{s,b}^{(\ell-1)T}.                       \tag{2}
\]

Consequently all matrix calls use the initial Gaussian matrices, with
learned increments evaluated by scalar contractions. The initial
first-layer population can be represented by one \(g\sim N(0,I_d)\):
\(Z_0^{(1)}(v)=g^Tv\). In the scalar recursion, first-layer training
preactivations obey

\[
Z_{k,a}^{(1)}=g^Tv_a-
\frac{2h}{m}\sum_{s<k,b}r_{s,b}(v_b^Tv_a)\Delta_{s,b}^{(1)}.     \tag{3}
\]

For each hidden matrix and each orientation introduce its Gaussian
source group. Write \(\xi_{k,a}^{(\ell)}\) for forward sources and
\(\zeta_{k,a}^{(\ell-1)}\) for transpose sources. Distinct groups and
the initial root are independent; within a group,

\[
\begin{aligned}
\mathbb E\xi_{k,a}^{(\ell)}\xi_{s,b}^{(\ell)}
 &=\mathbb E_{\ell-1}H_{k,a}^{(\ell-1)}H_{s,b}^{(\ell-1)},\\
\mathbb E\zeta_{k,a}^{(\ell-1)}\zeta_{s,b}^{(\ell-1)}
 &=\mathbb E_\ell\Delta_{k,a}^{(\ell)}\Delta_{s,b}^{(\ell)}.
\end{aligned}                                                    \tag{4}
\]

Their independence does not make matrix actions independent: each action
also has a response to uses in the opposite direction. With all current
forwards preceding all current backwards, these actions are

\[
\begin{aligned}
Z_{k,a}^{(\ell)}={}&\xi_{k,a}^{(\ell)}+
\sum_{s<k,b}\Delta_{s,b}^{(\ell)}
\left\{\mathbb E_{\ell-1}
 \frac{\partial H_{k,a}^{(\ell-1)}}
 {\partial\zeta_{s,b}^{(\ell-1)}}
-\frac{2h}{m}r_{s,b}
 \mathbb E_{\ell-1}H_{s,b}^{(\ell-1)}H_{k,a}^{(\ell-1)}\right\},\\
Q_{k,a}^{(\ell-1)}={}&\zeta_{k,a}^{(\ell-1)}+
\sum_{s\le k,b}H_{s,b}^{(\ell-1)}
\left\{\mathbb E_\ell
 \frac{\partial\Delta_{k,a}^{(\ell)}}
 {\partial\xi_{s,b}^{(\ell)}}
-\frac{2h}{m}{\bf1}_{s<k}r_{s,b}
 \mathbb E_\ell\Delta_{s,b}^{(\ell)}\Delta_{k,a}^{(\ell)}\right\}.
\end{aligned}                                                    \tag{5}
\]

Here \(H=\phi(Z)\),
\(\Delta^{(L)}=W_k^{(L+1)}\phi_L'(Z^{(L)})\),
\(\Delta^{(\ell)}=\phi_\ell'(Z^{(\ell)})Q^{(\ell)}\), and

\[
W_k^{(L+1)}=-\frac{2h}{m}\sum_{s<k,b}r_{s,b}H_{s,b}^{(L)},
\qquad f_{k,a}=\mathbb E_L[W_k^{(L+1)}H_{k,a}^{(L)}].           \tag{6}
\]

Every source derivative in (5) differentiates the finite formal
coordinate expression, with deterministic coefficients and covariance
parameters held fixed. Sources remain distinct formal arguments even
when their Gaussian law is singular. Current-source response terms
\(s=k\) in the transpose equation must be retained.

Equations (2), (3), and the learned terms of (5) are direct substitutions
of the Euler updates. The initial-action rule underlying the other terms
is the finite Gaussian conditioning/source-derivative rule in the complete
fixed-mesh section of `docs/03-local-population.qmd`, lines 3242--3569.
The general TP rule is Definition G.3 in Yang and Hu's
[TP IV supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf).
Its fixed-program master theorem uses Gaussian initialization and
pseudo-Lipschitz coordinate instructions. The present finite programs
satisfy these hypotheses because strip bounds give bounded derivatives,
values have at most linear growth, and finite sums/products have polynomial
growth. Zero readout is a degenerate Gaussian root. This identifies fixed
Euler programs; it supplies no finite-width error rate or stopping theorem.

### Sharing syntax and extending the panel

The formulas have a directed acyclic graph, not an expanded tree. Store a
coordinate instruction once and reference it. Differentiating that graph
with deterministic coefficients held fixed takes one ordinary automatic
differentiation pass per required source derivative, or one reverse pass
for a gradient. No exponential expansion into monomials is necessary.

Let \(s=O(d+LmN+Lp)\) bound the root and matrix-source count when the
passive inputs are evaluated only at the final mesh state. A conservative
shared coordinate graph has
\(K=O(dmN+Lm^2N^2+LpmN+dp)\) arithmetic edges. The covariance and
response tables contain \(O(s^2)\) deterministic scalar expectations.
These are sufficient bounds for the displayed representation, not lower
bounds for all representations. Memoized expectation evaluation stores
\(O(K+s^2)\) scalar/syntax records, plus numerical integration workspace.

Even under the earlier undeclared-query contract, a fixed deterministic
query could be appended after training. Equation (3) at \(k=N\) uses
the new dot products \(v_b^Tv\); (5) appends one forward source per
hidden layer, correlated with the stored training sources by (4).
It requires \(O(LmN)\) new covariances and responses per query, but no
passive backward history and no new training updates. This observation is
stronger than needed after the declared-query clarification. It does not
make the growing training tables small.

### A compact generator is a weaker positive result

A fixed interpreter can regenerate the above graph from data, \(N,h\),
the query list, and a requested precision. Indices take \(O(\log N)\)
bits. Thus a program generator can have description length linear in the
data description plus logarithmic integer metadata even when its expanded
graph and evaluation workspace are large. Recomputing coefficient tables
at query time is permitted by that description-only claim. It does not
certify a small resident numerical trained state or a fast evaluator.

Conversely, a claim that every terminal program must retain the entire
TP history is false for this broad program-description model. The growing
tables belong to the memoized interpreter, not to every finite executable
description. A Gaussian-expectation symbol by itself is not an implemented
numerical operation.

## 3. Focused repair: expectations are finite computable integrals, even at singular covariance

This section gives a concrete implementation bridge for each fixed program,
but deliberately does not assert a polynomial complexity bound.

At every chronological scalar node the required quantity is

\[
\theta_j=\mathbb E\,\psi_j(C_j^{1/2}G;\theta_1,\ldots,\theta_{j-1}),
\qquad G\sim N(0,I_s),                                       \tag{7}
\]

where \(C_j\) is a positive-semidefinite covariance assembled from
earlier scalar nodes. A fixed-program induction using bounded activation
derivatives gives computable polynomial bounds for \(\psi_j\) and its
first derivatives on each bounded set of earlier coefficients. The
coefficients themselves have finite computable upper bounds by taking
Gaussian polynomial moments in the same chronology. Their constants and
degrees may grow rapidly with \(N\).

Here is an elementary quantitative continuity bound sufficient for singular
covariances. If \(A,B\succeq0\) are \(s\)-square matrices and
\(\delta=\|A-B\|_F\), then

\[
\|A^{1/2}-B^{1/2}\|_F\le 2s^{1/4}\sqrt\delta.                 \tag{8}
\]

For \(\delta=0\) this is immediate. For \(\delta>0\), put
\(X=(A+\lambda I)^{1/2}-(B+\lambda I)^{1/2}\). The identity

\[
(A+\lambda I)^{1/2}X+X(B+\lambda I)^{1/2}=A-B
\]

and its Frobenius pairing with \(X\) imply
\(\|X\|_F\le\delta/(2\sqrt\lambda)\), because both square roots
have eigenvalues at least \(\sqrt\lambda\). Each regularization
changes its square root in Frobenius norm by at most \(\sqrt{s\lambda}\),
by diagonalization and \(\sqrt{a+\lambda}-\sqrt a\le\sqrt\lambda\).
The triangle inequality with \(\lambda=\delta/(4\sqrt s)\) proves
(8). A numerical covariance may first be symmetrized and projected onto
the positive-semidefinite cone; eigenvalue truncation is the nearest
Frobenius projection, and in particular its error is no more than twice
the preprojection error relative to the exact covariance. Exact rank
detection or a pseudoinverse is unnecessary.

Couple (7) at two coefficient lists by the same \(G\). The mean-value
bound for \(\psi_j\), Cauchy--Schwarz, Gaussian moments, and (8) give
a computable local modulus of the form

\[
|\theta_j-\widetilde\theta_j|
\le K_j\left(e_{j-1}+\sqrt{e_{j-1}}\right)+\eta_j,
\quad e_{j-1}=\max_{i<j}|\theta_i-\widetilde\theta_i|,           \tag{9}
\]

where \(\eta_j\) is the numerical integration/rounding error at that
node. The dependence of covariance entries on earlier coefficients is
included in \(K_j\). Backward selection of finitely many tolerances
\(\eta_j\) therefore gives any prescribed terminal accuracy.

To implement one integral, use an explicit envelope
\(|\psi_j(C_j^{1/2}G)|\le A(1+\|G\|_2)^q\). Outside the ball
\(\|G\|_2\le R\), its absolute expectation is at most

\[
\frac{A}{R^2}\mathbb E(1+\|G\|_2)^{q+2}.                    \tag{10}
\]

The moment is a finite sum of Gaussian radial moments. Choose \(R\)
to put (10) below half the tolerance. Integrate on \([-R,R]^s\)
by a finite rectangular Riemann grid. The envelope on the derivative of
the integrand times the Gaussian density gives an explicit Lipschitz
constant there; grid spacing smaller than the remaining tolerance divided
by that constant, volume, and \(\sqrt s\) controls the remainder.
Effective activation and elementary-function evaluation controls each
summand. Thus this is a terminating finite numerical procedure, not an
expectation oracle. Its cost can be exponential in \(s\) and much worse
in the required local tolerance.

Repeated use of the square-root modulus (9) can produce a certified
precision requirement proportional to \(2^M\log(1/\varepsilon)\)
for \(M\) scalar nodes. This is a weakness of this sufficient bound,
not a numerical lower bound. A uniform spectral gap would improve the
square-root estimate locally; no such gap is supplied for every history
Gram, and exact singularity is permitted. This finite-program repair
settles numerical evaluability, while leaving quantitative program growth,
GF approximation, and terminal variability calibration open.

## 4. A genuinely small resident numerical program from the authorized panel construction

The following inputs are imported conditionally, not re-proved here:

1. `initialization_panel_compression_20261008/PANEL_BOUND.md`, read
   completely, supplies the finite source spaces, paired initial actions,
   selected metrics, corrected optimizer, comparison certificate, exact
   inventory, and per-update arithmetic counts.
2. `initialization_panel_compression_20261008/INITIALIZATION.md`, read
   completely, supplies a finite initial-jet and conformal compiler for
   those spaces, including a finite quadrature and all discarded setup
   arrays. Its source/fitting/selection hypotheses remain explicit.
3. `adaptive_clock_compression_20261008/RESULT.md`, `FLARING_ROUTE.md`,
   and `FLARING_CHECK.md`, all read completely, supply and internally
   reconstruct a larger complex-time source domain. The complete adaptive
   panel lemma and residual-radius integral in `ADAPTIVE_APPROXIMATION.md`
   were also checked. The changed-domain proof uses the same selected
   runtime and improves the retained logarithmic power from five to three.

The panel proof assumes its stated small-label allowance and positive
training-feature population gap \(\gamma\). It is not a theorem for
all label magnitudes. Put \(Y=\|y\|_2/\sqrt m\),
\(\ell_n=\log(en)\), \(\lambda=\gamma/m\), and
\(S=16Y/\lambda\). The predecessor fixed-strip source recipe gives
the fifth-power term
\(C(L+1)(m+p)^2[U_{\rm fin}(S)/a]^2(Y/\lambda)^4\ell_n^5\),
with the input and initialization charges in `PANEL_BOUND.md` (29).
The current adaptive-domain recipe improves this to

\[
\begin{split}
D\le C\beta^{CL}(m+p)^2\bigg[
 &\left(\frac{Ym}{\gamma}\right)^4\ell_n^3\\
 &+\left(\frac m\gamma\right)^2\ell_n^2
       \log^2(e+\ell_n)\bigg]
 +C(m+p)d+D_{\rm alg}.
\end{split}                                                  \tag{11}
\]

Here \(\beta\) is the fixed activation envelope and \(D_{\rm alg}\)
counts the activation/runtime evaluator. The displayed dependence on
\(m,d,\gamma^{-1}\) is polynomial. It counts fixed metrics, metric
inverse caches, current model matrices, deficit variables, and ordinary
runtime buffers. Dense initialization, jets, temporal coefficients,
source bases and selection workspaces are discarded before runtime.
The leading label/gap factor is not replaced by its small-label allowance,
and the separate lower-logarithm term is not discarded. This is eventual
at each fixed admissible problem and confidence; no effective polynomial
width threshold or uniform theorem for parameters growing with width is
claimed.

Here is a finite prescription and its derivation. The activation-strip
width is \(a\), and \(U=U_{\rm fin}(S)\), \(H_j\), and \(\tau_j\)
are the explicit recurrences of `PANEL_BOUND.md` (4). The latter two bound
feature RMS and backward-response RMS divided by \(S\). Define

\[
\begin{gathered}
\mathcal K=H_L^2+S^2\left[\tau_1^2+
 \sum_{j=2}^L\tau_j^2H_{j-1}^2\right],\qquad
\nu=\lambda/4,\qquad T_0=32\ell_n/\lambda,\\
r_n=\frac{a}{64YSU\sqrt{\ell_n}},\qquad
h(t)=\frac{\log(1+2\mathcal K r_ne^{\nu t})}{2\mathcal K},
\qquad d_h=\frac{\nu}{2\mathcal K}\le\frac18,\\
\varrho(t)=\frac{h(t)}{2(1+d_h)}.
\end{gathered}                                                \tag{12a}
\]

The internally reconstructed enlarged source event supplies holomorphy
and coordinate bound \(M_0\sqrt n\) on the disk of radius
\(\varrho(t)\) around each \(0\le t\le T_0\). The radius is
nondecreasing with Lipschitz constant \(d_h/[2(1+d_h)]\). Predetermined
panels \(t_{b+1}=\min(T_0,t_b+\varrho(t_b)/2)\) therefore have count

\[
\begin{aligned}
J&\le1+5\int_0^{T_0}\frac{dt}{h(t)}\\
 &\le1+40960\frac Ua\left(\frac Y\lambda\right)^2\sqrt{\ell_n}
 +80\frac{\mathcal K}{\lambda}
       \log\left(1+\frac{4\ell_n}{\log2}\right).
\end{aligned}                                                \tag{12b}
\]

For the first inequality, each full panel contributes at least
\(1/(2+\operatorname{Lip}(\varrho))\) to
\(\int dt/\varrho\). For the second, split at
\(2\mathcal K r_ne^{\nu t}=1\). Before that time,
\(h(t)\ge r_ne^{\nu t}/2\); after it,
\(2\mathcal K h(t)\ge\log2+\nu(t-t_c)/2\). Integrating gives
\(2/(\nu r_n)+(4\mathcal K/\nu)
\log(1+\nu T_0/(2\log2))\), and
\(1/(\nu r_n)=4096(U/a)(Y/\lambda)^2\sqrt{\ell_n}\).

For source tolerance \(\eta\), set

\[
\begin{gathered}
K=\max\left(0,\left\lceil\log_2
 \frac{8M_0\sqrt n}{\eta}\right\rceil\right),\qquad
k=\dim\operatorname{span}\{v_1,\ldots,v_{m+p}\},\\
R=2m+k+1+2(2m+p)J(K+1),\qquad q_j\le9R,\\
D\le1020(L+1)R^2+36R+10m(k+1)+pk+(m+p)
       +D_{\rm alg}+3(m+p)d.
\end{gathered}                                               \tag{12c}
\]

Indeed each disk gives normalized Taylor coefficients of coordinate
magnitude at most \(M_0\sqrt n\). On its half-radius panel the
degree-\(K\) tail is at most \(M_0\sqrt n\,2^{-K}\le\eta/8\).
All \(J(K+1)\) coefficient vectors per curve span a fixed source
space; there are at most \(2(2m+p)\) required curves per layer.
The initial additions give \(2m+k+1\). Exact panel-span reduction
and the unchanged selector give the last two lines of (12c).

For the all-time absolute output target \(Y/n\), the explicit source
tolerance is

\[
\eta=\min\{1,Y,S,Y/(2n\overline{\mathcal A}_n)\},\qquad
\overline{\mathcal D}e^{-8\ell_n}\le Y/(2n),                  \tag{12d}
\]

with the numerical comparison coefficients in `RESULT.md` and
`PANEL_BOUND.md` (15a). In particular
\(\overline{\mathcal A}_n\) has factor
\((1+\sqrt{\ell_n})e^{64\sqrt{\ell_n}}\); hence the directly
checkable degree gate \(K+1\le8\ell_n\) holds eventually for
fixed parameters. Use \(U/a\le\beta^{60L}\),
\(\mathcal K\le\beta^{14L}\), and
\(\mathcal K/\lambda\ge1\), then square (12b) with
\((u+v+w)^2\le3(u^2+v^2+w^2)\). This proves (11), including its
separate \((m/\gamma)^2\ell_n^2\log^2(e+\ell_n)\) term. The
event's additional gates include F.17 and its activity/operator
conditions; the logarithmic simplification does not remove them.

The current construction remains finite and initialization-only without
a cheap-setup hypothesis. A uniform subrectangle of the enlarged domain
permits the initial-jet conformal compiler. Uniform convergence on a
slightly larger disk than all real-anchor coordinates, followed by
Cauchy's derivative formula, approximates the finitely many later-anchor
derivatives through order \(K\). The chain-rule operator
\((\mathfrak t'^{-1}\partial_\xi)^j\) converts these into physical
derivatives. Finite linear combinations of initial jets therefore
produce the scaled panel coefficients. Applying each initialized matrix
to its computed preimage preserves the required exact image pairing;
the approximation tolerance is allocated before selection. All jets,
panels, and coefficients are discarded afterward. No unknown trajectory
is an oracle coefficient. The inherited origin-jet order was already
\(\exp[O(\log^{3/2}n)]\) for values; no improved order, conditioning,
or setup-work bound for these derivative requests is claimed here.

The new domain is a mathematical input with scoped internal reconstruction,
not a consequence of real loss decay alone. Its proof derives response
time derivatives from provisional stops before Gaussian insertion, freezes
the real Gram to obtain a unitary vertical-time propagator, and controls
its variation by residual activity. The independent stopped-cavity
extensions preserve the conditional Gaussian law. Relevant unchanged
dependency passages and versions are recorded in Section 7 below; this
route does not claim a fresh complete review of the underlying source
theorem.

The runtime state consists of selected first/hidden matrices, raw
readout \(w_C\), and training deficit \(c_C\). With top training
feature matrix \(H_C\) and its selected metric \(M_L\), its effective
readout is explicitly

\[
\widehat w_C=w_C+H_C(H_C^TM_LH_C)^{-1}
(y-c_C-H_C^TM_Lw_C).                                         \tag{13}
\]

Its training prediction is \(y-c_C\). The imported optimizer uses
metric adjoints, the effective readout, and a specified positive
deficit Gram. In this route the full right-hand side is the imported
finite optimizer; formula (13) alone is not offered as a new ODE.

### Streamed arithmetic compiler lemma

Suppose a finite ODE \(\dot u=F(u)\), with \(u\in\mathbb R^D\),
has a right-hand-side evaluator taking \(C_F\) scalar arithmetic
operations and \(W_F\) working scalars. Fixed coefficients are counted
in \(D\). Its \(N\)-step Euler calculation
\(u_{k+1}=u_k+hF(u_k)\) can be performed by one loop body of length
\(O(C_F+D)\), with at most \(2D+W_F+O(1)\) resident scalars and an
\(O(\log(N+1))\)-bit step counter. Keeping the old state until the
right-hand side has been evaluated preserves the simultaneous Euler
update; reusing that buffer proves the inventory. A fixed-stage method
changes only the constant. A loss test after each update uses the
already counted current features/deficit and one additional scalar.

The proof is constructive: products are nested scalar loops, coordinate
nonlinearities call the activation backend, metric adjoints use matrix
products, and the training Gram solve uses a finite factorization with
the imported positive-gap condition. No history table or additional
Gaussian expectation is needed by this runtime.

For maximum selected width \(q\), the imported sufficient cost is

\[
C_F=O(Lmq^2+mdq+Lqm^2+m^3+LmqA_\phi),                        \tag{14}
\]

where \(A_\phi\) is the declared activation/derivative work. The usual
extra workspace \(O(Lmq+m^2)+W_\phi\) and a right-hand-side buffer
are covered by its conservative inventory, up to the stated evaluator
allowance. A final forward query costs
\(O(Lq^2+dq+LqA_\phi)\) after refreshing (13). Panel-span reduction
replaces \(d\) by its rank in the neural calculation and adds the
retained input projection. This proves small state and a small update
body, even if accuracy requires extremely many updates.

This arithmetic program deserves the descriptive phrase “TP-style” only
if that phrase means tensor operations and scalar nonlinearities. The
selected matrices, non-diagonal metrics, and Gram solves do not satisfy
the iid Gaussian setup of the standard TP master theorem. The
approximation certificate comes from the source-selection and corrected
flow argument. Renaming its runtime a tensor program supplies no extra
limit theorem.

## 5. Numerical stopping and what the scalar bound does not prove

For completeness a generic numerical transfer is available on a fixed
compact time interval. Suppose \(F\) is \(K\)-Lipschitz in a tube
around the exact trajectory, \(\|F\|\le B\), and each evaluated
Euler right-hand side has error at most \(\rho\). Integration of
\(F(u(t+s))-F(u(t))\) bounds the one-step truncation error by
\(KBh^2/2\). If \(e_k\) is the state error,

\[
e_{k+1}\le(1+Kh)e_k+h\rho+KBh^2/2,
\qquad
e_k\le e^{KT}\{e_0+T\rho+KBT h/2\}.                        \tag{15}
\]

Choosing errors so that the right side stays inside the tube closes
the estimate by first exit. Thus arbitrary prescribed finite-time
accuracy follows with a finite step count and finite arithmetic
precision, given effective tube constants. The repeated-step count
does not multiply the resident real-scalar inventory.

Stopping needs its own continuity condition. If the exact loss crosses a
positive level \(\theta\) and \(-\dot{\mathcal L}\ge\nu>0\) in a
neighborhood of that crossing, a uniform loss error \(\delta\) and a
grid spacing \(h\) move the first crossing by at most
\(\delta/\nu+h\), provided no earlier crossing lies outside that
neighborhood. If the exact loss is monotone and the crossing is unique,
the earlier-exclusion condition follows from the same uniform error
bound after choosing a sufficiently small \(\delta\). For a query
prediction with time derivative bounded by \(V\), the additional
stopping error is at most \(V(\delta/\nu+h)\).

A fitting estimate \(-\dot{\mathcal L}\ge c\mathcal L\) gives
\(\nu=c\theta/2\) on a level band around a positive \(\theta\).
The following stronger transfer uses residual magnitude and avoids
dividing by a small loss level. It supersedes that generic hitting-time
estimate whenever its two explicit inequalities hold.

Put \(\rho_n=\sqrt{\mathcal L_n}\). Suppose along the dense flow

\[
-\rho_n'(t)\ge\frac\lambda2\rho_n(t),\qquad
|f_n'(t,v_i)|\le B\rho_n(t).                                 \tag{15a}
\]

Integrating between any \(s<t\) gives

\[
|f_n(t,v_i)-f_n(s,v_i)|
\le\frac{2B}{\lambda}[\rho_n(s)-\rho_n(t)].                   \tag{15b}
\]

Let the positive residual threshold be \(a_*<\rho_n(0)\), and
let \(\tau_n\) be its dense first hitting time. Suppose numerical
predictions have error at most \(e\) at every grid time on the full
training/passive panel, and the numerical residual RMS has downward
change at most \(e\) in one step. If \(k\ge1\) is its first stopped
step, its residual RMS lies in \((a_*-e,a_*]\). The reverse triangle
inequality for training residual vectors gives
\(|\rho_n(t_k)-\widetilde\rho_k|\le e\); hence
\(|\rho_n(t_k)-a_*|\le2e\). Applying (15b) in the appropriate
time order and adding the same-time query error proves

\[
\max_{i>m}|\widetilde f_i(t_k)-f_n(\tau_n,v_i)|
\le e\left(1+\frac{4B}{\lambda}\right).                     \tag{15c}
\]

The bound concerns stopped predictions directly and is independent of
\(a_*^{-1}\). For fixed \(B,\lambda\), a smaller source/numerical
tolerance by the factor in (15c) changes \(K\) additively and leaves (11)'s logarithmic
power unchanged. Verifying the constants and the numerical decrement
condition belongs to the concrete solver transfer; (15c) states every
hypothesis used here. Exact zero-loss stopping still need not occur in
finite time. Own-state stopping, dense-time stopping, and infinite
fitted endpoints must not be silently identified.

Bound (11) is in real scalars. For a finite-bit implementation, let
\(b\) denote the maximum stored word length, including coefficient
magnitudes and denominators. Storage is \(O(Db)\) bits, not \(O(D)\).
The imported documents explicitly do not bound conditioning of selected
metrics, numerical source production, or \(b\) by a polynomial in
\(\log n,m,d,\gamma^{-1}\). Continuity yields some finite precision;
it does not yield the desired dependence. An exact-real inverse or
activation call must not be advertised as a free finite-bit operation.

### Terminal outputs versus a retained optimizer

If only the declared \(p\) stopped predictions are requested after all
computation, the final retained object can be their rounded values and
a fixed decoder. If each output has magnitude at most \(M\), rounding
to error \(\varepsilon\) needs
\(O(p[\log(1+M)+\log(1/\varepsilon)])\) bits. This follows by
rounding to multiples of a power of two no larger than
\(\varepsilon\). The source state can then be discarded.

This observation uses no mathematical compression of training; it
clarifies why final-output storage is weaker than a retained numerical
optimizer. It is not forbidden trajectory playback: the values were
computed by a specified solver, and no future query is promised. The
stronger conditional construction (11)--(15) retains an evaluable model
and a small update body, so it does not rely on this minimal endpoint
interpretation.

## 6. The dense-pair benchmark must match the stopped observable

`PANEL_BOUND.md` imports a lower bound of order
\(Y\sqrt\gamma/(\sqrt n\log(en)^{5/2})\) for the discrepancy of two
independent dense trajectories in a maximum-over-time panel norm. Its
proof witnesses an early training time. A uniform-in-time compression
bound can therefore be calibrated to that trajectory benchmark at any
chosen stopping time. It does not compare error to the usually smaller
discrepancy between the two stopped output vectors.

A concrete sanity check lies inside the zero-readout squared-loss model.
For one sample with \(y>0\), initial output zero, and
\(0<\theta<y^2\), suppose the continuous training loss reaches
\(\theta\). At its first hitting time,

\[
f_n=y-\sqrt\theta.                                         \tag{16}
\]

Indeed continuity gives \((f_n-y)^2=\theta\). The branch
\(y+\sqrt\theta\) would require passing through zero residual and
hence crossing the threshold earlier. Thus the training prediction at
its own first hitting time is deterministic across initializations,
although the earlier trajectory can vary. This remains true for an
admitted genuinely nonlinear activation whenever stopping is reached.
It refutes the inference from positive path variability to positive
stopped-output variability, not the compression construction. In this
special case the exact formula (16) is itself a compact answer.

For an actual terminal dense-pair criterion a separate lower bound, an
exact treatment of zero-variability cases, or another direct relative
error argument is required. The route does not replace the actual
benchmark by a presumed \(n^{-1/2}\) noise scale.

## 7. Dependency and hostile-audit record

Established within this scoped argument, pending reconstruction:

- The finite-step trained-increment formulas (2)--(6), shared-DAG and
  scalar-table counts, and passive-query extension.
- The elementary covariance square-root bound (8), terminating fixed
  Gaussian integral evaluation, and a finite accuracy-selection route.
- The streamed arithmetic compiler, (15)'s explicit Euler estimate, and
  the distinction between resident scalar count and bit count.
- The stopped-output sanity check (16).

Conditional positive result: importing the internally reconstructed
adaptive-domain source event and unchanged selection, fitting and
comparison interfaces, plus effective activation evaluation and a
positive-loss stopping rule satisfying (15a)--(15c), produces the small
resident numerical program described by (11)--(15). The current
real-coordinate exponent is three; five is its fixed-strip predecessor.
The explicit additional lower-logarithm term in (11) remains. Its
absolute prediction guarantee is inherited, and
its comparison with trajectory dense variability is inherited. The
claim against actual stopped-output variability remains unproved here.

Strongest surviving objections: the inherited stochastic source theorem
has not been independently reconstructed in this route; the numerical
precision may depend badly on the selector; the stopping rule may be
ill-conditioned or be an infinite-time endpoint; and the stopped
variability benchmark may vanish or be substantially below its trajectory
counterpart. These are separate issues. Failure to bound setup work is
not an objection under the current size-only contract.

External TP source used: Yang and Hu, TP IV supplement, complete relevant
framework/computational sections G--H and the derivative conventions in
L. Its master theorem is used only for fixed programs. Its discussion
of growing covariance tables is a cost analysis of that representation,
not a universal terminal-memory lower bound. All numerical repair and
streaming bounds above are derived here rather than imported from that
discussion.

Authorized maintained inputs read: `docs/index.qmd`, `docs/notation.qmd`,
the complete fixed-mesh source-identification section of
`docs/03-local-population.qmd`, the complete integrated-initial-query
section of `docs/02-gaussian-reuse.qmd`, and the exact-compiler and
work/storage subsections of `docs/08-autonomous-computation.qmd`.
The two named initialization-panel notes were read completely only after
the explicit scope extension. The focused update then read `RESULT.md`,
`FLARING_ROUTE.md`, and `FLARING_CHECK.md` completely in the authorized
adaptive-clock study, along with the complete adaptive panel lemma and
residual-radius integral passage in `ADAPTIVE_APPROXIMATION.md`.

The dependency check inspected the complete Sections 1--2, 5, and 9 of
`SOURCE_INSERTION_COMPLETION.md`: the independently stopped-reference
definition, derivative/activity/base-product assumptions, actual ordered
trace products, and Gaussian rectangle/moment bounds. It also inspected
the complete Sections 2--5 and 7--8 of `UNBOUNDED_COMPRESSOR_BRIDGE.md`:
source constants and allowance, samplewise budgets, scalar absorption,
real Gaussian-reference moments, derivative improvement and qualitative
fixed-moment budget removal. The adaptive proof supplies precisely the
changed contour geometry, residual-integral bounds and global coefficient
modulus at those interfaces. Those inspected passages introduce no new
requirement to retain temporal panels or Gaussian histories at runtime.
This targeted check preserves the imported internal-audit status; it is
not a fresh verification of every insertion identity or the full paper.

At this update the following dependency hashes match those in
`FLARING_CHECK.md`: `ADAPTIVE_APPROXIMATION.md` starts `fd6daf74a3c9`,
`PANEL_BOUND.md` starts `9622e6938eb1`,
`SOURCE_INSERTION_COMPLETION.md` starts `2680c170bb8d`, and
`UNBOUNDED_COMPRESSOR_BRIDGE.md` starts `e018f0291b44`.
The current `FLARING_ROUTE.md` hash starts `688efd057dae`; its opening
change record identifies the typo correction and explicit
finite-anchor-derivative corollary after the audited frozen version.
The present read checked that corollary and the count directly.

No unapproved study input, frozen archive, live sibling route, or empirical
output was consulted. Required rigorous
math, canonical notation, neural-response, research-contract,
adversarial-audit and proof-search instructions were applied.
