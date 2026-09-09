# Unconditional local three-hidden-layer limit: assembled statement

This is the statement assembled from the six proof notes listed below.
It is a local theorem, not the requested all-finite-time theorem.
A proof of global continuation has not been obtained.

## Network, exact algorithm, and interval

There is one input and one target, both equal to one. All three hidden
layers have width \(n\). The first preactivation \(z^{(1)}\) and the
rescaled readout \(W^{(4)}\) are \(n\)-vectors. The two hidden matrices
\(W^{(2)},W^{(3)}\) are \(n\) by \(n\). With \(\phi=\arctan\), set
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 f_n=\frac{(W^{(4)})^\top h^{(3)}}n,\qquad
 r_n=f_n-1,\qquad L_n=r_n^2,
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot(W^{(3)})^\top\delta^{(3)},\quad
 \delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)}.
 \tag{1}
\]
The initialization blocks are independent, with
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{2}
\]
Use the exact raw updates, with \(\eta_n=n^{-2}\),
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,
\]
\[
 W^{(\ell)}_{k+1}
 =W^{(\ell)}_k-\frac{2\eta_n r_{n,k}}n
           \delta^{(\ell)}_k(h^{(\ell-1)}_k)^\top,
 \qquad\ell=2,3,
\]
\[
 W^{(4)}_{k+1}=W^{(4)}_k-2\eta_n r_{n,k}h^{(3)}_k.
 \tag{3}
\]
Physical time is \(t=k\eta_n\). Between these times interpolate the
raw parameters linearly and recompute all hidden preactivations and
features from the interpolated parameters. Finite gradient flow
means the differential equations with the same right-hand sides
divided by \(\eta_n\).
At GD mesh nodes, velocities mean right-hand derivatives; use the
left-hand derivative at \(T_0\) if it is a terminal mesh node.

Here is one explicit, very conservative positive interval. Let
\[
 a=\pi/2,\quad A=a^2+e,\quad
 M_p=2^{1/p}\exp\!\big(A(2a+1)+2pA^2a^2\big)\quad(p=1,2),
\]
\[
 A_3=a^2+AM_1,\quad
 C_3=(1+2a)\exp((1+2a)A_3)+a^2,\quad Q=a(1+C_3),
\]
\[
 C_2=(2Q+C_3)M_2+Q^2,\qquad
 S_0=\min\{1,(2C_2)^{-1},(2C_3)^{-1}\},\qquad
 T_0=\frac14\min\{S_0,(4a^2)^{-1}\}.
 \tag{4}
\]
The constants are deliberately not optimized. They are finite explicit
numbers determined by \(\arctan\), not by an unproved continuation
or moment assumption.

## Conclusions on this interval

There are three fixed neuron probability spaces, with bounded initial
matrix actions \(W^{(2)}_0,W^{(3)}_0\) and their reverse actions.
They are constructed from the joint limits of finite Gaussian matrix
calculations, preserving every reused transpose. There is a unique
local uncut population state
\[
 X^{(1)}(t),\qquad W^{(2)}(t),\qquad
 W^{(3)}(t),\qquad W^{(4)}(t),\qquad 0\le t\le T_0.
 \tag{5}
\]
Here \(X^{(1)}=F(Z^{(1)})\), \(F(z)=z+z^3/3\);
the two matrices are bounded actions between the adjacent population
spaces; and the readout is the typical population coordinate.
Initially \(Z^{(1)}_0\) is standard Gaussian and \(W^{(4)}_0=0\).
This is a finite list of evolving fields and operators, not a
finite-scalar description.

Use (1) on these spaces, replacing finite transposes by their reverse
actions, denoted by a star, and using ordinary pointwise products.
Then
\[
 f=E_3[W^{(4)}H^{(3)}],\quad r=f-1,\quad L=r^2,
\]
\[
 \frac{dX^{(1)}}{dt}=-2r\,(W^{(2)})^*\delta^{(2)},\quad
 \frac{dW^{(2)}}{dt}=-2r\,\delta^{(2)}\otimes H^{(1)},
\]
\[
 \frac{dW^{(3)}}{dt}=-2r\,\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{dt}=-2r\,H^{(3)}.                       \tag{6}
\]
The rank-one action is explicitly
\((U\otimes V)B=U E[VB]\).
Uniqueness holds among continuous integral solutions on these fixed
spaces with bounded operator and mean-square parameter norms.
The same uniqueness holds when restarting from a reached state on
any remaining subinterval of the constructed interval.

In the raw coordinate \(Z^{(1)}\), (6) is the gradient flow of
\(L\): use ordinary mean-square lengths for the vector fields and
the square-summed matrix length for trained matrix changes.
The present state alone determines its derivatives; the Gaussian
response coefficients in the proof are not prescribed external
inputs to its evolution.

For each fixed same-layer finite list of network measurements,
the joint empirical law of both finite GD and finite gradient flow
converges uniformly in \(t\in[0,T_0]\), in probability, to the
corresponding population law. Convergence includes second moments.
The class includes finite compositions of the current states,
globally Lipschitz coordinate functions, bounded products, and
both orientations of both current matrices; finitely many specified
times may be used jointly. It also includes the named backward
fields in (1) and the hidden preactivation and feature velocities.
No coordinatewise pairing across distinct hidden layers is asserted.

Equivalently, for any such finite same-layer coordinate list and any
fixed continuous measurement \(\psi\) of at most quadratic growth,
its empirical average approaches its population expectation uniformly
in time. Thus prediction, residual, and loss converge uniformly.
The four finite kernel blocks
\[
 \frac{\|\delta^{(1)}\|_2^2}{n},\qquad
 \frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2},\qquad
 \frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2},\qquad
 \frac{\|h^{(3)}\|_2^2}{n}
 \tag{7}
\]
converge uniformly to the expectation formulas in
LOCAL_GRADIENT_STRUCTURE.md.
For every hidden layer, the empirical law of its entire preactivation
path converges, including second moments of the supremum norm, to
the law of its population path. Integrated squared velocities
converge to the corresponding population integrals.

With the same finite initialization, GD and finite gradient flow
also approach one another uniformly in the state distance consisting
of the normalized Euclidean difference in \(F(z^{(1)})\), the two
matrix operator-norm differences, and the normalized Euclidean
readout difference. No operator-norm comparison across different
widths or between different underlying spaces is asserted.

Every hidden layer learns a nonconstant feature trajectory.
More precisely, there are nonzero square-integrable variables
\(V^{(\ell)}\) such that
\[
 Z^{(\ell)}(t)-Z^{(\ell)}_0=2t^2V^{(\ell)}+o(t^2),\qquad
 H^{(\ell)}(t)-H^{(\ell)}_0
   =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2)
 \tag{8}
\]
in mean square, and both displayed leading variables have positive
mean-square size. The three hidden kernel blocks are positive
constant multiples of \(t^2+o(t^2)\); hidden feature squared-speed
integrals have positive \(T^3\) leading coefficients. Explicit
initial Gaussian formulas are given in LOCAL_FEATURE_LEARNING.md.
The total kernel is nonconstant, the loss decreases, and the
activation's best affine-approximation error on each hidden
distribution remains strictly positive on a common initial interval.

## How the premises are discharged

The proof is the following chain of proved lemmas, not a list of
additional assumptions on the original network.

1. L3_FIXED_MESH_SOURCE_IDENTIFICATION.md proves the exact finite
   Gaussian source representation, including both independent
   matrices, both transposes, empirical training feedback, and
   singular covariance cases.
2. LOCAL_ACTION_SPACE_AND_FLOW.md realizes those finite calculations
   on common population spaces and proves the fixed-clipping flow
   and its fixed-clipping width limit.
3. LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md proves a tail bound uniform
   in the Euler mesh and clipping level on the explicit \(S_0\).
   Its displayed scalar equations are precisely the equations
   proved in item 1 and realized by item 2.
4. LOCAL_CUTOFF_BRIDGE.md uses this bound to remove clipping,
   prove local uniqueness and restartability, and establish
   convergence from the actual raw GD, not merely from a
   transformed or population-feedback scheme. In particular its
   stated representation premise is discharged by items 1--3.
5. LOCAL_GRADIENT_STRUCTURE.md proves that the resulting autonomous
   evolution is a genuine gradient flow with all four kernel
   contributions.
6. LOCAL_FEATURE_LEARNING.md derives the strictly nonzero initial
   hidden movement from this flow and the initial Gaussian action
   laws. Its local-flow premise is discharged by items 1--5.

None of these statements proves the all-finite-time continuation
requested in the main goal.


---

# Fixed-mesh source identification for clipped three-hidden-layer arctangent flow

This is a fixed finite-program result. Its constants may depend on the number of steps, the step size, and the clipping level. It proves neither mesh-uniform response bounds nor a continuous-time limit.

## Statement and conventions

Fix an integer N, a feature step Delta > 0, and a smooth clipping function tau_R with bounded derivative, |tau_R(q)| <= |q|, |tau_R'(q)| <= 1, and |tau_R(q)| <= 2R. Let phi(z)=arctan(z), d=phi', F(z)=z+z^3/3. Let A_0,B_0 be independent n by n matrices with independent N(0,1/n) entries, independent of iid standard Gaussian Z^(1)_0. Initially C_0=0.

Consider the exact finite-width discrete calculation

\[
X^{(1)}_0=F(Z^{(1)}_0),\quad
H^{(1)}_k=\phi(F^{-1}(X^{(1)}_k)),\quad
Z^{(2)}_k=A_kH^{(1)}_k,\quad H^{(2)}_k=\phi(Z^{(2)}_k),
\]
\[
Z^{(3)}_k=B_kH^{(2)}_k,\quad H^{(3)}_k=\phi(Z^{(3)}_k),\quad
\delta^{(3)}_k=C_k\odot d(Z^{(3)}_k),\quad
q^{(2)}_k=B_k^\top\delta^{(3)}_k,
\]
\[
\delta^{(2)}_k=d(Z^{(2)}_k)\odot\tau_R(q^{(2)}_k),\quad
q^{(1)}_k=A_k^\top\delta^{(2)}_k,
\]
\[
X^{(1)}_{k+1}=X^{(1)}_k+\Delta q^{(1)}_k,\quad
A_{k+1}=A_k+\frac\Delta n\delta^{(2)}_k(H^{(1)}_k)^\top,
\]
\[
B_{k+1}=B_k+\frac\Delta n\delta^{(3)}_k(H^{(2)}_k)^\top,
\qquad C_{k+1}=C_k+\Delta H^{(3)}_k.
\]

For every fixed same-layer tuple of its nodes through step N, its empirical law converges in probability in W_2 to the scalar construction below. In particular, all the pairwise contractions used below converge. Covariance matrices may be singular.

There are four mutually independent centered Gaussian groups

\[
(\xi^{(2)}_k)_k,\quad(\xi^{(3)}_k)_k,\quad
(\zeta^{(1)}_k)_k,\quad(\zeta^{(2)}_k)_k,
\]

also independent of Z^(1)_0, with covariances

\[
\mathbb E\xi^{(\ell)}_k\xi^{(\ell)}_s
=\mathbb E H^{(\ell-1)}_kH^{(\ell-1)}_s,\qquad
\mathbb E\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_s
=\mathbb E\delta^{(\ell)}_k\delta^{(\ell)}_s,
\quad\ell=2,3.
\]

The scalar equations are

\[
X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{r<k}q^{(1)}_r,
\quad H^{(1)}_k=\phi(F^{-1}(X^{(1)}_k)),
\]
\[
Z^{(2)}_k=\xi^{(2)}_k+\sum_{s<k}a^{(2)}_{ks}\delta^{(2)}_s,
\quad q^{(1)}_k=\zeta^{(1)}_k+\sum_{s\le k}b^{(2)}_{ks}H^{(1)}_s,
\]
\[
Z^{(3)}_k=\xi^{(3)}_k+\sum_{s<k}a^{(3)}_{ks}\delta^{(3)}_s,
\quad q^{(2)}_k=\zeta^{(2)}_k+\sum_{s\le k}b^{(3)}_{ks}H^{(2)}_s,
\]

with H^(ell)=phi(Z^(ell)), C_k=Delta sum_{r<k} H^(3)_r, delta^(3)_k=C_k d(Z^(3)_k), delta^(2)_k=d(Z^(2)_k)tau_R(q^(2)_k), and

\[
a^{(\ell)}_{ks}
=\mathbb E\frac{\partial H^{(\ell-1)}_k}
                    {\partial\zeta^{(\ell-1)}_s}
 +\Delta\mathbb E H^{(\ell-1)}_kH^{(\ell-1)}_s,
\qquad s<k,
\]
\[
b^{(\ell)}_{ks}
=\mathbb E\frac{\partial\delta^{(\ell)}_k}
                    {\partial\xi^{(\ell)}_s}
 +\Delta\mathbf1_{s<k}\mathbb E\delta^{(\ell)}_k\delta^{(\ell)}_s,
\qquad s\le k.
\]

Every derivative is a derivative of the explicit finite coordinate expression with respect to the named Gaussian source coordinate. Previously calculated deterministic coefficients and covariance parameters are held fixed. Distinct source coordinates remain distinct formal arguments even if their joint Gaussian law is singular. Coefficients themselves need not be invariant under a different off-support extension; their contracted correction is invariant.

## Finite Gaussian conditioning, with two matrices

We first prove the needed source rule for a fixed finite calculation with deterministic scalar coefficients, globally Lipschitz C^1 coordinate instructions having bounded first derivatives, and finitely many independent Gaussian matrices, each reusable in both directions. The root coordinate tuples are iid with finite second moments and independent of the matrices. The initial tuple may contain both Z and F(Z); no Lipschitz assertion about F as a root-generating function is needed.

Condition on the complete adaptive transcript. For one selected matrix W, write its previous observations as

\[
WV=Y,\qquad W^\top U=Q.
\]

The other matrices cause no change to the following formula. Conditional residuals of the independent matrices remain independent: inductively, a query is measurable from the current transcript, and its newly observed answer imposes a linear constraint only on the queried matrix. Coordinate calculations reveal no further randomness.

When the two input Gram matrices are invertible, Gaussian orthogonal projection gives

\[
W\mid\mathcal H\ \overset d=
Y(V^\top V)^{-1}V^\top
+U(U^\top U)^{-1}Q^\top P_{V^\perp}
+P_{U^\perp}\widetilde W P_{V^\perp}.
\tag{1}
\]

For a new input h, put alpha_n=(V^T V)^(-1)V^T h and h_perp=h-V alpha_n. Then

\[
Wh=Y\alpha_n+U\beta_n+
\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g,
\quad
\beta_n=(U^\top U/n)^{-1}(Q^\top h_\perp/n),
\tag{2}
\]

in conditional law, with fresh standard Gaussian g. The transpose formula is identical with the two sides interchanged.

Assume for the moment that all limiting input Gram matrices are positive definite. Induction on the finite transcript proves joint W_2 empirical convergence: all coefficients in (2) converge by the previous induction hypothesis; the removed projection has conditional mean squared normalized norm rank(U)/n; after removing it, conditional averaging of independent Gaussian coordinates gives joint weak convergence and second-moment convergence. Globally Lipschitz coordinate instructions preserve W_2 convergence. This works unchanged with two interleaved matrices.

## Why the response coefficient is the source derivative

Here is the identification step, rather than an invocation of a general tensor-program theorem. Use lowercase letters for the limiting scalar variables. Let the previous forward inputs be v_r, and the previous transpose inputs be u_s. Let Gamma_U=(E u_s u_t)_{st}. By induction write

\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=\mathbb E\partial_{\zeta_s}v_r,
\]
\[
q_s=\zeta_s+\text{a linear combination of previous forward inputs}.
\]

Unavailable/future-source derivatives are zero. Let alpha be the limiting least-squares coefficients and h_perp=h-sum_r alpha_r v_r. Orthogonality gives E[v_r h_perp]=0 for every old forward input. Therefore the non-Gaussian correction in every q_s drops out of its pairing with h_perp:

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

The Gaussian group zeta is independent of the roots and all other Gaussian groups and has covariance Gamma_U. Gaussian integration by parts yields

\[
\mathbb E[\zeta h_\perp]
=\Gamma_U\,\mathbb E\nabla_\zeta h_\perp.
\]

Thus (2)'s limiting coefficient is

\[
\beta=\mathbb E\nabla_\zeta h
       -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]

After substituting the decompositions of y_r into (2), their old responses cancel the second term. The resulting rule is exactly

\[
\boxed{\quad
(Wh)_{\mathrm{lim}}
=\xi_h+\sum_s u_s\,\mathbb E\partial_{\zeta_s}h.
\quad}
\tag{3}
\]

The new Gaussian source is xi_h=sum_r alpha_r xi_r+sigma g_scalar, where sigma^2=E h_perp^2. Hence Cov(xi_h,xi_r)=E[h v_r] and Var(xi_h)=E h^2. The fresh scalar innovation is independent of every old source. As a result, source groups belonging to distinct oriented matrices W, W^T remain mutually independent, even though W and W^T themselves are dependent. The same argument applies separately to A_0 and B_0 at every interleaved call.

This proof uses the complete derivative of h as its finite coordinate expression. It does not discard derivative paths passing through calls to the other matrix.

## Removing singular-Gram difficulties

For each matrix call, temporarily replace its input h by h+epsilon chi, where chi is a new independent standard Gaussian input vector, revealed immediately before that call. At fixed epsilon>0, the limiting squared distance of a new input from its previous same-direction input span is at least epsilon^2: project the new independent chi off that fixed-dimensional span and use conditional second-moment calculations. Consequently all limiting query Gram matrices are positive definite, and the preceding proof applies. The chi variables are additional independent roots; the source rule (3) applies to the perturbed query inputs.

For the fixed finite program, couple perturbed and unperturbed calculations using the same original matrices and roots. On the event that all the finitely many matrix operator norms and input-noise normalized norms are bounded, induction through the instructions gives

\[
\max_v\|v^\epsilon-v\|_n\le C\epsilon,
\tag{4}
\]

where C depends on the fixed program but not on n or epsilon<=1. The event has probability tending to one. The matrix bound follows, for example, by a fixed-net Gaussian tail bound and a union bound over the two matrices.

The scalar source constructions converge as epsilon decreases to zero as well. A detailed finite induction suffices: source covariance entries are second moments of previously constructed inputs; Gaussian covariance square roots are continuous even at singular positive-semidefinite matrices; all previously constructed scalar coordinate functions and their source derivatives are continuous in the finite deterministic coefficient list. Their first derivatives have deterministic bounds at each fixed instruction because the coordinate instructions have bounded first derivatives. Therefore Gaussian coupling, W_2 convergence, and dominated convergence pass both second moments and expected source derivatives to the epsilon=0 recursion. No inverse or pseudoinverse is used in this last continuity step. Combining this fact with (4) identifies the unperturbed empirical limit with (3).

For completeness, degenerate Gaussian Stein also directly explains the absence of ambiguity. If zeta has covariance Gamma and u has second-moment matrix Gamma, then

\[
\mathbb E[\zeta f]=\Gamma\mathbb E\nabla f,
\qquad
u^\top(I-\Gamma^+\Gamma)v=0\quad\text{a.s.}
\]

for every deterministic v. Thus replacing E grad f by Gamma^+ E[zeta f] may change its entries, but cannot change the response sum u^T E grad f. One must not assert convergence of finite pseudoinverses at a rank drop.

## Application and the empirical training coefficients

Unroll A_k and B_k into their initial matrices plus their finite learned rank-one sums. Each forward trained call has the extra term

\[
\Delta\sum_{s<k}\delta^{(\ell)}_s
                \langle H^{(\ell-1)}_s,H^{(\ell-1)}_k\rangle_n,
\]

and each transpose trained call has the extra term

\[
\Delta\sum_{s<k}H^{(\ell-1)}_s
                \langle\delta^{(\ell)}_s,\delta^{(\ell)}_k\rangle_n.
\]

Freeze these finitely many contractions at the population values constructed causally. This produces an oracle with deterministic coefficients, to which the proved finite conditioning/source lemma applies. At each stage the population contraction involves only already constructed variables, so this definition is not circular.

The oracle and actual finite Euler calculation agree asymptotically. Indeed, fixed clipping gives |delta^(2)|<=2R; bounded arctangent gives |C_k|<=N Delta pi/2 and bounded delta^(3). The product defining delta^(3) can therefore be extended to a globally Lipschitz C^1 map by smoothly clipping C outside a slightly larger interval. Every other required coordinate map is already globally Lipschitz. Root tuples have finite second moments. All oracle norms and all initial matrix operator norms are bounded with probability tending to one. On that event,

\[
|\langle u,v\rangle_n-\langle\bar u,\bar v\rangle_n|
\le \|u-\bar u\|_n\|v\|_n+
    \|\bar u\|_n\|v-\bar v\|_n.
\]

Finite induction through the unrolled calculation bounds actual/oracle error by a constant times the largest oracle contraction error. Every such error converges to zero by the lemma. No growing-mesh estimate is used. Adding the learned terms to (3) gives exactly the stated a and b formulas.

The causal call order at step k is A_0 H1_k, B_0 H2_k, B_0^T delta3_k, A_0^T delta2_k. Thus forward response sums use s<k, while transpose response sums use s<=k. This order also proves that every covariance extension and every derivative coefficient is known when needed.

As explicit checks on the current-source terms,

\[
b^{(3)}_{kk}=\mathbb E[C_k\phi''(Z^{(3)}_k)],
\]
\[
b^{(2)}_{kk}
=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
 +b^{(3)}_{kk}\mathbb E[d(Z^{(2)}_k)^2\tau_R'(q^{(2)}_k)].
\]

The second term on the last line is a current-step return through the other matrix; omitting it would be incorrect. Earlier-source derivatives also retain every such path.

Finally, replacing C_0=0 by iid N(0,n^-2) changes no fixed-mesh limit. Couple the two finite calculations; the initial normalized C difference is O_P(n^-1), its initial coordinate supremum is bounded with probability tending to one, and the same fixed-step Lipschitz comparison applies. This last statement is only for fixed N, Delta, R.

## Scope of the result

The displayed scalar representation, the four independent Gaussian source groups, all current/previous response terms, and singular covariance cases are justified at each fixed clipped finite mesh. Individual off-support derivative coefficients require the stated formal-expression convention. This proof supplies no bound uniform in N, Delta tending to zero, or R tending to infinity.


---

# A common population state and the clipped flows

This note constructs the state on which the local three-hidden-layer
limit will live. It proves global existence for each fixed clipping
level, not global existence for the unclipped population equation.
The finite-Gaussian calculation used below is proved in
/tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md.

Throughout, \(\phi(z)=\arctan z\), \(a=\pi/2\), and
\(F(z)=z+z^3/3\). Write \(E_\ell\) for expectation over the neuron
population of hidden layer \(\ell\). These are three separate
populations; a neuron index in one layer is not paired with an index
in another.

## Constructing both directions of both initial matrices

Consider the following countable collection of finite calculations.
At finite width their roots are \(z^{(1)}_0\) and \(F(z^{(1)}_0)\),
where \(z^{(1)}_{0,i}\) are independent standard Gaussians. Include
the constant vector on each layer, rational linear combinations,
and multiplication by either initial Gaussian matrix
\(W^{(2)}_0,W^{(3)}_0\), in either direction. Include
\(\phi,F^{-1}\), the smooth clipping functions used below at integer
levels, and a countable family of bounded globally Lipschitz
coordinate functions dense among continuous functions on every
compact subset of each finite-dimensional coordinate space.
Products are included only after clipping their varying factors to
fixed bounded intervals, so these coordinate instructions are
globally Lipschitz. Smooth versions can be used for the countable
dense family. Treat \(F(z^{(1)}_0)\) as part of the initial root tuple;
no global Lipschitz claim about \(F\) is needed.

Any finite union of these calculations is another finite calculation.
The fixed-program Gaussian conditioning proof therefore gives
consistent, deterministic joint limiting laws of all their nodes,
separately for each layer. Countably many consistent finite laws
define a countable random coordinate collection on its product
measurable space. Denote the resulting probability spaces by
\(\Omega_1,\Omega_2,\Omega_3\), retaining exactly the information
generated by their coordinate slots.

For a square-integrable scalar population variable \(U\), write
\[
 |U|_{2,\ell}=(E_\ell U^2)^{1/2}.
\]
This is a population mean-square size, not a new normalization of a
finite vector. Finite vector sizes remain \(\|u\|_2/\sqrt n\).
Let \(\mathcal H_\ell=L^2(\Omega_\ell)\), the set of population
variables with finite mean-square size, identifying variables equal
with probability one.

The finite matrices have operator norms at most \(10\) with
probability tending to one. A \(1/4\)-net on each unit sphere has
at most \(9^n\) points, and the scalar Gaussian bound gives
\[
 \mathbb P(\|W^{(\ell)}_0\|_{\rm op}>10)
 \le 2\,9^{2n}\exp(-100n/8),\qquad \ell=2,3.
\]
For every finite rational linear combination of existing nodes,
pass the exact finite matrix norm inequality to its limiting second
moment. There are only countably many such combinations. Consequently
the assignment to the corresponding matrix-answer node satisfies
\[
 |W^{(\ell)}_0 U|_{2,\ell}\le10|U|_{2,\ell-1}.             \tag{1}
\]
If two expressions define the same input in mean square, (1) shows
that they define the same output. Thus the assignment is a linear
map on the span of the coordinate nodes.

That span is dense in \(\mathcal H_\ell\): bounded functions of
finitely many coordinate slots approximate any square-integrable
variable on the generated probability space; bounded continuous
functions approximate those finite-coordinate functions in mean
square; and the included countable bounded Lipschitz family
approximates the continuous functions on compact sets. Clipping
and restricting to a compact set control the discarded tails.
Equation (1) extends each initial matrix action uniquely to every
square-integrable input. The same construction extends its reverse
action. Passing the exact finite transpose identity gives
\[
 E_\ell[V\,W^{(\ell)}_0U]
 =E_{\ell-1}[U\,(W^{(\ell)}_0)^*V].                      \tag{2}
\]
The star names precisely this reverse action. Both directions are
retained throughout training, not independently resampled.

Real scalar coefficients and other globally Lipschitz coordinate
maps can be approximated by this collection when needed. For each
fixed finite calculation propagate its approximation errors and
use (1) at every matrix call. This identifies all fixed-step clipped
Euler calculations below on these same three spaces with the
finite-width laws given by Gaussian conditioning.

## State and clipped equations

For \(U\in\mathcal H_\ell\), \(V\in\mathcal H_{\ell-1}\), define
\[
 (U\otimes V)B=U\,E_{\ell-1}[VB].                        \tag{3}
\]
Its operator norm is \(|U|_{2,\ell}|V|_{2,\ell-1}\); its reverse
action is \(V\otimes U\).

Choose smooth odd functions \(\tau_R\), for integers \(R\ge1\), with
\[
 \tau_R(x)=x\ (|x|\le R),\quad
 |\tau_R(x)|\le\min\{|x|,2R\},\quad
 0\le\tau_R'(x)\le1.                                    \tag{4}
\]
For example integrate a smooth even function equal to one on
\([-1,1]\), zero outside \([-2,2]\), and between zero and one,
after scaling its argument by \(R\).

The state is
\[
 X^{(1)}\in\mathcal H_1,\quad
 W^{(2)}:\mathcal H_1\to\mathcal H_2,\quad
 W^{(3)}:\mathcal H_2\to\mathcal H_3,\quad
 W^{(4)}\in\mathcal H_3.
\]
The matrix actions are bounded linear maps. Initially they are the
two actions just constructed, \(X^{(1)}_0=F(Z^{(1)}_0)\), and
\(W^{(4)}_0=0\). The forward and clipped backward calculations are
\[
 Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\phi(Z^{(1)}),
 \quad Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),
\]
\[
 Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}),
 \quad \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),
\]
\[
 \delta^{(2)}_R
 =\phi'(Z^{(2)})
   \tau_R\!\left((W^{(3)})^*\delta^{(3)}\right).          \tag{5}
\]
Products are within their stated layer. In feature time \(s\),
\[
 \frac{dX^{(1)}}{ds}=(W^{(2)})^*\delta^{(2)}_R,\quad
 \frac{dW^{(2)}}{ds}=\delta^{(2)}_R\otimes H^{(1)},
\]
\[
 \frac{dW^{(3)}}{ds}=\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{ds}=H^{(3)}.                            \tag{6}
\]
Clipping is a proof device. In general (6) is not gradient ascent
for the original predictor; no bound below assumes it is.

Use the state distance
\[
 \begin{aligned}
 d(\theta,\widetilde\theta)={}&
 |X^{(1)}-\widetilde X^{(1)}|_{2,1}
 +\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}\\
 &+\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}
 +|W^{(4)}-\widetilde W^{(4)}|_{2,3}.
 \end{aligned}                                         \tag{7}
\]
For finite-width states replace population mean-square sizes by
ordinary Euclidean sizes divided by \(\sqrt n\). All bounds below
hold with the same constants in either setting.

## Bounds independent of clipping

On \(0\le s\le S\), integration of the readout equation gives
\[
 |W^{(4)}(s)|\le as\quad\hbox{with probability one}.      \tag{8}
\]
Thus \(|\delta^{(3)}(s)|_{2,3}\le as\). Using (3)--(5),
\[
 \|W^{(3)}(s)\|_{\rm op}\le10+\frac{a^2s^2}{2},
\]
\[
 \|W^{(2)}(s)\|_{\rm op}
 \le10+\frac{10a^2s^2}{2}+\frac{a^4s^4}{8}.              \tag{9}
\]
Indeed
\(|\delta^{(2)}_R|_{2,2}\le
\|W^{(3)}\|_{\rm op}|\delta^{(3)}|_{2,3}\).
The first equation of (6) then bounds both the mean-square velocity
of \(X^{(1)}\) and its displacement on every fixed \(S\).
All four velocities in (7) are bounded by a finite constant depending
only on \(S\), not on \(R\).

Harmless enlargements of these bounds also hold for transformed
Euler with \(M\Delta\le S\), and for nonzero readouts with an initial
coordinate bound at most one: sum the same polynomial estimates.
No gradient identity is required. The identical bounds hold for
an uncut finite feature flow, since
\(|\delta^{(2)}|_{2,2}\le
\|W^{(3)}\|_{\rm op}|\delta^{(3)}|_{2,3}\).

On these bounded sets, (6) has Lipschitz constant at most
\(C_S(1+R)\) in (7). To see the important product estimates, first
use the pointwise readout bound in
\[
 \begin{aligned}
 &|W^{(4)}\phi'(Z^{(3)})
 -\widetilde W^{(4)}\phi'(\widetilde Z^{(3)})|_{2,3}\\
 &\qquad\le |W^{(4)}-\widetilde W^{(4)}|_{2,3}
       +2aS|Z^{(3)}-\widetilde Z^{(3)}|_{2,3}.
 \end{aligned}
\]
The displayed coefficient uses a zero-initial-readout reference.
For two paths with initial coordinate readout bounds at most one,
replace \(2aS\) by \(2(1+aS)\). This and the operator bounds make
the full backward action
\((W^{(3)})^*\delta^{(3)}\) Lipschitz in (7). Changing the middle
gate in (5) costs at most
\(4R|Z^{(2)}-\widetilde Z^{(2)}|_{2,2}\), since the clipped
factor is at most \(2R\). Changing its input costs at most the
difference of the full backward actions. The forward and reverse
maps and (3) give the asserted bound. Only the readout itself
needs a common pointwise bound, not its difference.

## Existence, uniqueness, and the fixed-clipping width limit

For fixed \(R\), iterate the integral equations (6) on a short
interval. Work in a closed set of continuous paths with slightly
enlarged operator and mean-square bounds, and impose the pointwise
bound \(|W^{(4)}(s)|\le as\). Every integral iterate preserves
the latter. The path set is complete in the supremum of (7):
a common pointwise bound survives mean-square convergence.
A sufficiently short interval makes the integral map a contraction
and preserves the other enlarged bounds. Its unique fixed point
is the local solution. No differentiability of every coordinate
map on an unrestricted \(L^2\) ball is asserted.

The bounds (8)--(9) allow this argument to restart finitely many
times on any fixed finite \(S\), for fixed \(R\). Thus each clipped
flow exists uniquely for all feature times. Its state velocity is
bounded and its vector field is Lipschitz, so integrating a one-step
Euler defect gives the recurrence
\[
 e_{k+1}\le(1+C_S(1+R)\Delta)e_k+C_{R,S}\Delta^2.
\]
It follows that
\[
 \sup_{s\le S}
 d(\theta^{R,\mathrm{Euler}}(s),\theta^R(s))
 \le C_{R,S}\Delta.                                    \tag{10}
\]
Use constant Euler interpolation here; movement inside one step
is included in the bound. The same estimate is uniform in finite
width on the indicated initialization event.

At fixed \(R,\Delta,M\), Gaussian conditioning and the finite-step
oracle comparison identify the finite Euler empirical laws with
the population Euler laws on these common spaces. Tiny Gaussian
readout initialization changes no such limit: its normalized
size tends to zero and its coordinate maximum is bounded with
probability tending to one. Apply (10), first fixing \(\Delta\)
while width tends to infinity, then sending \(\Delta\) to zero.
This proves the fixed-\(R\) width limit uniformly on \([0,S]\).

This statement includes every fixed finite calculation from the
current state using matrix actions in either direction, globally
Lipschitz coordinate maps, and bounded products. Its difference
is bounded by a constant times (7). Joint empirical convergence
includes second moments, initially by the Gaussian calculation
and then by the mean-square comparisons in (10). Hence continuous
measurements of at most quadratic growth on each finite node list
converge as well. A measurement is an ordinary function of the
listed coordinates, averaged over neurons; trained coordinates
are not asserted independent.

All conclusions here concern fixed clipping unless explicitly
stated otherwise. Removing clipping requires the separate
mesh-uniform local tail estimate and comparison argument.
Extending the resulting uncut flow beyond that local interval
requires a further continuation theorem.


---

# Coefficientwise local response bootstrap

## Frozen-coefficient scalar system

Write \(a=\pi/2\), \(\phi=\arctan\), \(F(x)=x+x^3/3\), and
\(\chi=\phi\circ F^{-1}\), so
\[
 |\phi|\le a,\quad |\phi'|\le1,\quad |\phi''|\le2,\qquad
 |\chi|\le a,\quad |\chi'|\le1.
\]
Let \(\Delta>0\), \(S=M\Delta\le1\), and consider indices
\(0\le k\le M\). The finite scalar equations under audit are
\[
 X_{1,k}=F(Z_{1,0})+\Delta\sum_{r<k}q_{1,r},\qquad
 H_{1,k}=\chi(X_{1,k}),
\]
\[
 Z_{2,k}=\xi_{2,k}+\sum_{r<k}a_{2,kr}\delta_{2,r},
 \qquad H_{2,k}=\phi(Z_{2,k}),
\]
\[
 Z_{3,k}=\xi_{3,k}+\sum_{r<k}a_{3,kr}\delta_{3,r},
 \qquad H_{3,k}=\phi(Z_{3,k}),
\]
\[
 C_k=\Delta\sum_{r<k}H_{3,r},\qquad
 \delta_{3,k}=C_k\phi'(Z_{3,k}),
\]
\[
 q_{2,k}=\zeta_{2,k}+\sum_{v\le k}b_{3,kv}H_{2,v},\qquad
 \delta_{2,k}=\phi'(Z_{2,k})\tau_R(q_{2,k}),
\]
\[
 q_{1,k}=\zeta_{1,k}+\sum_{v\le k}b_{2,kv}H_{1,v}.
\]
Assume a differentiable clipping function satisfying
\[
 |\tau_R(x)|\le|x|,\qquad |\tau_R'(x)|\le1.
\]
The deterministic coefficients are
\[
 a_{\ell,ks}
 =\mathbb E\frac{\partial H_{\ell-1,k}}{\partial\zeta_{\ell-1,s}}
       +\Delta\,\mathbb E[H_{\ell-1,k}H_{\ell-1,s}],
 \qquad s<k,
\]
\[
 b_{\ell,ks}
 =\mathbb E\frac{\partial\delta_{\ell,k}}{\partial\xi_{\ell,s}}
       +\Delta\mathbf1_{\{s<k\}}
                         \mathbb E[\delta_{\ell,k}\delta_{\ell,s}],
 \qquad s\le k.
\]
All displayed source derivatives are formal derivatives of the scalar
program with its deterministic coefficients held fixed. They are not
derivatives of a covariance factorization. This convention is essential,
including when source covariance matrices are singular.

The four centered Gaussian source groups have covariance
\[
 \mathbb E[\xi_{\ell,k}\xi_{\ell,s}]
     =\mathbb E[H_{\ell-1,k}H_{\ell-1,s}],\qquad
 \mathbb E[\zeta_{\ell-1,k}\zeta_{\ell-1,s}]
     =\mathbb E[\delta_{\ell,k}\delta_{\ell,s}].
\]
Within each group arbitrary correlations across times are allowed.
The groups are independent as assumed in the representation theorem.

Define deterministic row sums
\[
 U_k=\sum_{s\le k}|b_{2,ks}|,\qquad
 V_k=\sum_{s\le k}|b_{3,ks}|.
\]
At \(k=0\), \(C_0=0\), both backward Gaussian variances are zero,
and \(U_0=V_0=0\).

## Bottom response: one factor of the source-time mesh

Suppose \(U_r\le1\) for every \(r<k\). Differentiating the bottom
recursion with respect to \(\zeta_{1,s}\) gives
\[
 \left|\frac{\partial X_{1,j}}{\partial\zeta_{1,s}}\right|
 \le\Delta\mathbf1_{\{s<j\}}
 +\Delta\sum_{r<j}\sum_{v\le r}|b_{2,rv}|
                   \left|\frac{\partial X_{1,v}}{\partial\zeta_{1,s}}\right|.
\]
Discrete Gronwall, also using \(|\chi'|\le1\), yields
\[
 \left|\frac{\partial H_{1,j}}{\partial\zeta_{1,s}}\right|
 \le\Delta e^S\quad(s<j\le k).
\]
Consequently, with the fixed constant
\[
 A=a^2+e,
\]
one has
\[
 |a_{2,js}|\le A\Delta\quad(s<j\le k).                   \tag{1}
\]
No size estimate on a realization of \(q_1\), and no derivative of a
Gaussian covariance, is used in this step.

## Middle response and its exponential envelope

Assume additionally \(V_r\le1\) for all \(r<k\). Put
\[
 \mathcal S_j=\sum_{s\le j}
       \left|\frac{\partial Z_{2,j}}{\partial\xi_{2,s}}\right|,
 \qquad
 \overline{\mathcal S}_j=\max_{v\le j}\mathcal S_v,
\]
\[
 E_j=\exp\left(A\Delta\sum_{r<j}(2|q_{2,r}|+V_r)\right).
\]
The source derivative of the clipped middle backward field satisfies
\[
 \left|\partial\delta_{2,r}\right|
 \le2|q_{2,r}|\,|\partial Z_{2,r}|
       +|\partial q_{2,r}|.
\]
For a derivative with respect to a \(\xi_2\) source,
\[
 |\partial q_{2,r}|
 \le\sum_{v\le r}|b_{3,rv}|\,|\partial Z_{2,v}|.
\]
Using (1), summing the absolute source derivatives, and applying
discrete Gronwall gives
\[
 \overline{\mathcal S}_j\le E_j\quad(j\le k).             \tag{2}
\]
For an individual \(\zeta_{2,s}\) derivative there is instead the
additional source term \(\mathbf1_{\{r=s\}}\). Its first effect on
\(Z_{2,j}\) carries \(a_{2,js}\), so the same argument gives
\[
 \left|\frac{\partial Z_{2,j}}{\partial\zeta_{2,s}}\right|
 \le A\Delta E_j,\qquad s<j\le k.                       \tag{3}
\]
There is no dependence on \(\zeta_{2,j}\) in \(Z_{2,j}\).

The envelope has uniform moments despite the unbounded Gaussian part
of \(q_2\). Indeed
\[
 |C_r|\le aS,\qquad |\delta_{3,r}|\le aS,
 \qquad \operatorname{Var}(\zeta_{2,r})\le a^2S^2,
\]
and
\[
 |q_{2,r}|\le|\zeta_{2,r}|+aV_r.
\]
If \(V_*=\max_{r<j}V_r\), Jensen's inequality over the finitely many
times, followed by the one-variable Gaussian exponential bound, gives,
for \(p\ge1\),
\[
 \begin{aligned}
 \mathbb E E_j^p
 &\le e^{pA(2a+1)SV_*}
       \mathbb E\exp\left(2pA\Delta\sum_{r<j}|\zeta_{2,r}|\right)\\
 &\le 2\exp\left(pA(2a+1)SV_*+2p^2A^2a^2S^4\right).
 \end{aligned}                                           \tag{4}
\]
For \(j=0\), \(E_0=1\) directly. For \(j>0\), the Jensen step is
\[
 \exp\left(2pA\Delta\sum_{r<j}|\zeta_{2,r}|\right)
 \le\frac1j\sum_{r<j}
              \exp(2pAj\Delta|\zeta_{2,r}|).
\]
Only the marginal variances of the Gaussian sources enter this
calculation. Neither their time independence nor independence of a
source from the bounded response shift is needed.

For explicit fixed constants, let
\[
 M_p=2^{1/p}\exp\left(A(2a+1)+2pA^2a^2\right).
\]
Under \(S,V_*\le1\), (4) implies \(\|E_j\|_p\le M_p\).
Equations (3) and the definition of \(a_3\) therefore give
\[
 |a_{3,js}|\le A_3\Delta,\qquad
 A_3=a^2+A M_1,\qquad s<j\le k.                         \tag{5}
\]

## Top response is bounded pointwise

Let
\[
 T_j=\sum_{s\le j}
       \left|\frac{\partial Z_{3,j}}{\partial\xi_{3,s}}\right|,
 \qquad \overline T_j=\max_{v\le j}T_v.
\]
Since \(C_j=\Delta\sum_{r<j}H_{3,r}\),
\[
 \sum_{s\le j}\left|
       \frac{\partial\delta_{3,j}}{\partial\xi_{3,s}}\right|
 \le\Delta\sum_{r<j}T_r+2aS T_j
 \le(1+2a)S\overline T_j.                               \tag{6}
\]
Together with (5), this implies the deterministic bound
\[
 \overline T_j\le\exp((1+2a)A_3S^2)\quad(j\le k).
\]
Taking expectations in (6) and adding the learned term gives
\[
 V_k\le(1+2a)S\exp((1+2a)A_3S^2)+a^2S^3
       \le C_3S,                                       \tag{7}
\]
where
\[
 C_3=(1+2a)\exp((1+2a)A_3)+a^2.
\]
In particular, the current row \(b_{3,k\cdot}\) is bounded before
estimating the current \(q_{2,k}\).

## Current middle backward field and bottom response

Equation (7) gives
\[
 \|q_{2,k}\|_2\le aS+aV_k\le QS,\qquad Q=a(1+C_3).
                                                               \tag{8}
\]
Here \(\|\cdot\|_2\) denotes the scalar probability-space \(L^2\) norm,
not a finite-width norm. The same bound holds at earlier indices under
the same bootstrap argument.

Differentiating the current middle backward field with respect to the
\(\xi_2\) source row and using (2) gives
\[
 \sum_{s\le k}
  \left|\frac{\partial\delta_{2,k}}{\partial\xi_{2,s}}\right|
 \le(2|q_{2,k}|+V_k)\overline{\mathcal S}_k.
\]
Cauchy--Schwarz and (4), (7), (8) yield
\[
 \begin{aligned}
 U_k
 &\le(2\|q_{2,k}\|_2+V_k)
                      \|\overline{\mathcal S}_k\|_2
       +S\max_{r\le k}\|\delta_{2,r}\|_2^2\\
 &\le[(2Q+C_3)M_2+Q^2]\,S=:C_2S.                      \tag{9}
 \end{aligned}
\]
In the last line \(S\le1\) and
\(\|\delta_{2,r}\|_2\le\|q_{2,r}\|_2\le QS\) were used.
There is no circular use of \(U_k\) in either (7) or (9).

## First-exit closure and source dependencies

Choose the explicit positive horizon
\[
 S_0=\min\left\{1,\frac1{2C_2},\frac1{2C_3}\right\}.
\]
Fix any \(S=M\Delta\le S_0\). If \(k\) were the first index at which
\(U_k>1\) or \(V_k>1\), all earlier rows satisfy the bootstrap
hypotheses. The estimates above give
\[
 V_k\le C_3S\le\frac12,\qquad
 U_k\le C_2S\le\frac12,
\]
a contradiction. For use of the earlier-index bound in (9), apply
(7)--(8) at each \(r\le k\); their premises involve only rows strictly
earlier than \(r\). Equivalently, induct simultaneously on the sharper
conclusions \(U_r\le C_2S\), \(V_r\le C_3S\).

The causal order for the current index is
\[
 a_{2,k\cdot}\ \longrightarrow\ H_{2,k}\
 \longrightarrow\ a_{3,k\cdot}\ \longrightarrow\
 \delta_{3,k}\ \longrightarrow\ b_{3,k\cdot}\
 \longrightarrow\ q_{2,k},\delta_{2,k}\
 \longrightarrow\ b_{2,k\cdot}.
\]
More explicitly:

- \(H_{1,k}\) uses only bottom response rows with time \(<k\).
- \(H_{2,k}\) uses only middle backward fields at times \(<k\).
- The derivative of \(H_{2,k}\) with respect to a past \(\zeta_2\)
  source consequently uses only \(b_3\) rows with time \(<k\).
- The top scalar recursion uses only its own \(\xi_3\) source group
  once its deterministic \(a_3\) row is fixed.
- The current \(b_3\) row determines the bounded shift of
  \(q_{2,k}\), after which the current \(b_2\) row is estimated.

Thus differentiating the explicit scalar program under the stated
frozen-coefficient convention introduces no omitted cross-source term.
If a different convention differentiates the deterministic coefficient
selection or a covariance square root, this audit does not apply to
that different derivative.

## Uniform local tail actually obtained

The closure gives, uniformly in \(k\le M\), \(M\), \(\Delta\), and \(R\),
\[
 q_{2,k}=\zeta_{2,k}+\beta_{2,k},\qquad
 \operatorname{Var}(\zeta_{2,k})\le a^2S^2,\qquad
 |\beta_{2,k}|\le aC_3S.
\]
The shift may depend on the Gaussian source; its deterministic amplitude
bound suffices. For \(x>0\),
\[
 \mathbb P\bigl(|q_{2,k}|>aC_3S+x\bigr)
 \le2\exp\left(-\frac{x^2}{2a^2S^2}\right).              \tag{10}
\]
Consequently \(\|q_{2,k}\|_p\le C S\sqrt p\) for \(p\ge2\), with
a constant independent of mesh and clipping. The same conclusion
holds for \(\delta_{2,k}\), since clipping and the gate do not increase
its absolute value.

This estimate is obtained on \(S\le S_0\). The constants above are
deliberately conservative; no claim is made that \(S_0\) contains the
full optimization feature horizon.

## Implementation of the comparison still to distinguish

The displayed bottom update is Euler in \(X_1=F(z^{(1)})\):
\[
 X_{1,k+1}=X_{1,k}+\Delta q_{1,k}.
\]
It is not exactly the map obtained by applying \(F\) after one ordinary
Euler step in \(z^{(1)}\). It is a valid discretization of the same
continuous transformed equation, and its scalar finite-program
response representation must be justified for that discretization.
This distinction does not alter any estimate above, but it matters
when stating which finite algorithm has been identified.


---

# Local cutoff removal and the actual-GD bridge

This note proves the analytic bridge from the finite-program tail
estimate in LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md. One identification
premise remains explicit: the scalar representation in that audit
must describe the actual clipped Gaussian-matrix Euler programs.
This note does not prove that representation. Subject to that
premise, no tail hypothesis on an uncut solution is required.
All conclusions below are local on a fixed positive interval.

## Setting and the precise representation premise

Let \(\phi=\arctan\), \(a=\pi/2\),
\[
F(z)=z+z^3/3,\qquad \chi=\phi\circ F^{-1}.
\]
Both \(F^{-1}\) and \(\chi\) are 1-Lipschitz, and \(|\chi|\le a\).
There are three layer probability spaces and bounded initial
operators \(W_0^{(2)},W_0^{(3)}\) between adjacent \(L^2\) spaces,
together with their adjoints. These are the population actions
generated by the two independent Gaussian initial matrices.
The transformed state is
\[
\Theta=(X^{(1)},W^{(2)},W^{(3)},W^{(4)}),
\]
and its forward and backward measurements are
\[
Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\chi(X^{(1)}),
\quad Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),
\]
\[
Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}),
\quad \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),
\]
\[
q^{(2)}=(W^{(3)})^*\delta^{(3)},\qquad
\delta_R^{(2)}=\phi'(Z^{(2)})\tau_R(q^{(2)}),\qquad
q_R^{(1)}=(W^{(2)})^*\delta_R^{(2)}.
\]
Choose continuously differentiable clipping maps satisfying
\[
\operatorname{Lip}(\tau_R)\le1,\quad
\tau_R(x)=x\ (|x|\le R),\quad
|\tau_R(x)|\le |x|,\quad |\tau_R(x)|\le2R.
\]
Take integer \(R\ge1\); write \(R=\infty\) for the identity map.
Only the middle backward field is clipped. The feature-time
vector field is
\[
\mathcal V_R(\Theta)=
\left(q_R^{(1)},\
\delta_R^{(2)}\otimes H^{(1)},\
\delta^{(3)}\otimes H^{(2)},\
H^{(3)}\right),                                        \tag{1}
\]
where \((u\otimes v)w=u\,\mathbb E[vw]\).
Initially \(W_0^{(4)}=0\) and \(X_0^{(1)}=F(Z_0^{(1)})\), with
\(Z_0^{(1)}\sim N(0,1)\).

The finite-width version uses \(x^{(1)}=F(z^{(1)})\), replaces
adjoints by transposes, and uses \(uv^{\mathsf T}/n\) for \(u\otimes v\).
Each population \(L^2\) norm is replaced by \(\|v\|_2/\sqrt n\).
Its initial hidden matrices have independent \(N(0,1/n)\) entries,
and its first-layer coordinates are iid standard Gaussians.

Here is the sole scalar-representation premise used below:

**Representation premise.** For every fixed clipping level \(R\)
and fixed finite transformed Euler mesh on \([0,S_0]\), the
population action Euler program has exactly the scalar
Gaussian/response representation audited in
LOCAL_RESPONSE_BOOTSTRAP_AUDIT.md, with the prescribed initialization
and the frozen-coefficient derivative convention. In particular,
for some deterministic \(K<\infty\), independent of \(R\), mesh,
and time index,
\[
\mathbb E\exp\left(\frac{(q_{R,k}^{(2)})^2}{K^2}\right)\le2.
                                                               \tag{2}
\]
One can enlarge \(K\) to pass from the audit's Gaussian-plus-bounded
shift bound to (2).

The identity of these scalar laws with the action Euler laws is
essential. A tail bound for a separately specified scalar recursion
would not suffice. Joint fixed-program limits and common population
actions are constructed by the finite Gaussian mechanism described
below; the representation premise is an additional identification
of those laws with the audited scalar formulas.

Measure two states on the same spaces by
\[
\begin{aligned}
d(\Theta,\widetilde\Theta)
={}&\|X^{(1)}-\widetilde X^{(1)}\|_{L^2}
 +\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}\\
&+\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}
 +\|W^{(4)}-\widetilde W^{(4)}\|_{L^2}.                 \tag{3}
\end{aligned}
\]
Write \(d_n\) for its finite-width counterpart. No operator-norm
distance between operators acting on different widths is asserted.
Across widths the conclusion concerns their joint measured laws.

## Uniform primal bounds and fixed-cutoff well-posedness

Fix a feature horizon \(S\le S_0\). The following bounds depend on
\(S\), an initial operator bound \(M\), and an initial normalized
readout bound, but not on \(R\) or width. With zero readout,
\[
\|W^{(4)}(s)\|_\infty\le as,\qquad
\|W^{(4)}(s)\|_{L^2}\le as.
\]
For every finite cutoff, and for an uncut solution while it exists,
\[
\|\delta^{(3)}\|_{L^2}\le\|W^{(4)}\|_{L^2},\qquad
\|\delta_R^{(2)}\|_{L^2}
\le\|q^{(2)}\|_{L^2}
\le\|W^{(3)}\|_{\rm op}\|W^{(4)}\|_{L^2}.
\]
Successively integrating the last three blocks of (1) gives finite
polynomial bounds on \(W^{(3)},W^{(2)}\). For instance the coarser
bounds
\[
Q=aS,\qquad R_3=M+aQS,\qquad R_2=M+aR_3QS              \tag{4}
\]
bound the readout \(L^2\) norm and the two operator norms.
Also
\[
\|q_R^{(1)}\|_{L^2}\le R_2R_3Q.
\]
These estimates hold for positive-step Euler paths whose step sum
is at most \(S\), and for their straight interpolants.
With a nonzero initial readout of \(L^2\) norm at most one, use
\(Q=1+aS\) instead. The norm of every block of (1), in the norm
associated with (3), is bounded by a constant \(C\) independent of
cutoff and width.

Suppose both hidden operator norms and readout \(L^2\) norms are
bounded as above, and a reference state's readout has pointwise
bound \(B\). Successive forward differences give
\[
\|Z^{(2)}-\widetilde Z^{(2)}\|_{L^2}
\le a\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
 +R_2\|X^{(1)}-\widetilde X^{(1)}\|_{L^2},
\]
\[
\|Z^{(3)}-\widetilde Z^{(3)}\|_{L^2}\le C d.
\]
For the top gate, place the bounded readout in the second term:
\[
\delta^{(3)}-\widetilde\delta^{(3)}
=\phi'(Z^{(3)})(W^{(4)}-\widetilde W^{(4)})
 +[\phi'(Z^{(3)})-\phi'(\widetilde Z^{(3)})]
       \widetilde W^{(4)}.
\]
Therefore
\[
\|\delta^{(3)}-\widetilde\delta^{(3)}\|_{L^2}
 +\|q^{(2)}-\widetilde q^{(2)}\|_{L^2}\le C d.           \tag{5}
\]
The constant uses the reference pointwise bound \(B\); it does not
use a pointwise bound on the other readout.

For two states clipped at the same \(R\), (5), boundedness of
\(\tau_R\), and \(\operatorname{Lip}(\phi')\le2\) give
\[
\|\delta_R^{(2)}-\widetilde\delta_R^{(2)}\|_{L^2}
\le C(1+R)d.
\]
The rank-one inequality
\[
\|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
\le\|u-\widetilde u\|_{L^2}\|v\|_{L^2}
 +\|\widetilde u\|_{L^2}\|v-\widetilde v\|_{L^2}
\]
now proves
\[
\|\mathcal V_R(\Theta)-\mathcal V_R(\widetilde\Theta)\|
\le C(1+R)d.                                           \tag{6}
\]
All these estimates are identical at finite width.

For each fixed \(R\), Picard iteration in continuous paths with
the norm (3) gives existence and uniqueness on a short interval.
The set imposing a common readout pointwise bound is closed in
\(L^2\): a convergent sequence has an almost-everywhere convergent
subsequence preserving that bound. The integral update of the
readout preserves the bound \(as\), and (4) permits continuation
to all of \([0,S]\). The same proof works at finite width.
The Euler local error is at most
\(\tfrac12 C^2(1+R)\Delta^2\), because of the velocity bound and
(6). A discrete Gronwall estimate consequently gives
\[
\sup_{s\le S}d(\Theta_{R,\Delta}(s),\Theta_R(s))
\le C_{R,S}\Delta,                                     \tag{7}
\]
and the identical estimate in \(d_n\), uniformly in width on the
initial operator-bound event. The estimates (4) directly control
the Euler paths, so no assumption about monotonicity of a clipped
predictor is used.

## The asymmetric estimate and removal of clipping

Compare an uncut state \(A\), or a state clipped at \(R'\ge R\),
with a reference state \(B\) clipped at \(R\). In (5) take \(B\)
as the bounded-readout reference. Writing \(D_A=\phi'(Z_A^{(2)})\)
and \(D_B=\phi'(Z_B^{(2)})\), exactly
\[
\begin{aligned}
\delta_{R'}^{(2)}(A)-\delta_R^{(2)}(B)
={}&D_A[\tau_{R'}(q_A^{(2)})-\tau_{R'}(q_B^{(2)})]\\
&+(D_A-D_B)\tau_R(q_B^{(2)})\\
&+D_A[\tau_{R'}(q_B^{(2)})-\tau_R(q_B^{(2)})].
\end{aligned}                                                        \tag{8}
\]
This also holds when \(R'=\infty\). The last bracket vanishes on
\(|q_B^{(2)}|\le R\) and is at most \(2|q_B^{(2)}|\) otherwise.
To avoid discontinuous tail measurements define the 1-Lipschitz
continuous function
\[
b_R(q)=(|q|-R/2)_+.
\]
Then \(|q|\mathbf1_{\{|q|>R\}}\le2b_R(q)\), and (8) implies
\[
\|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
\le C(1+R)d(A,B)+C\|b_R(q_B^{(2)})\|_{L^2}.             \tag{9}
\]
The constant depends only on the common primal bounds and the
reference readout pointwise bound, not on \(R'\).

By (7) and (5), for each fixed \(R\) the Euler \(q^{(2)}\) variables
converge in \(L^2\) to \(q_R^{(2)}(s)\), at every fixed \(s\).
An almost-everywhere convergent subsequence and Fatou's lemma
therefore pass (2) to the exact clipped solution:
\[
\mathbb E\exp((q_R^{(2)}(s))^2/K^2)\le2
\qquad(0\le s\le S).                                  \tag{10}
\]
The constant is the same for every \(R\) and \(s\).
If \(\mathbb E e^{q^2/K^2}\le2\), then
\[
\mathbb E[q^2\mathbf1_{\{|q|>u\}}]
\le4K^2e^{-u^2/(2K^2)}.
\]
For example, use
\(q^2e^{-q^2/(2K^2)}\le2K^2/e\) and the exponential moment.
Consequently
\[
\sup_{s\le S}\|b_R(q_R^{(2)}(s))\|_{L^2}
\le 2K e^{-R^2/(16K^2)}=:\varepsilon_R.                \tag{11}
\]

Subtracting two integral equations and applying scalar Gronwall
to (9) yields
\[
\sup_{s\le S}d(\Theta_{R'}(s),\Theta_R(s))
\le e^{C(1+R)S}
\left[d(\Theta_{R'}(0),\Theta_R(0))+CS\varepsilon_R\right].
                                                               \tag{12}
\]
For common initialization, the right side tends to zero as
\(R\to\infty\), uniformly in \(R'\ge R\). The clipped solutions
therefore have a limit \(\Theta\) in the complete space of
continuous paths with distance (3). It retains the primal bounds
and the readout pointwise bound.

There is no unresolved passage through an unbounded product here:
(5) gives \(q_R^{(2)}\to q^{(2)}(\Theta)\) in \(L^2\), and (9),
now evaluated at the limiting state and its clipped reference,
gives
\[
\sup_{s\le S}
\|\mathcal V_\infty(\Theta(s))-\mathcal V_R(\Theta_R(s))\|
\le C(1+R)\sup_s d(\Theta(s),\Theta_R(s))+C\varepsilon_R
\longrightarrow0.
\]
Pass to the limit in the integral equations. The result is an
uncut solution of (1), and the uniform velocity convergence also
makes it continuously differentiable in the Banach norm.

If \(\widetilde\Theta\) is any other uncut integral solution with
the same initialization and bounded primal norms on this interval,
apply (9) against \(\Theta_R\). No tail bound for
\(\widetilde\Theta\) is used. Its own bound may change \(C\), but
\(e^{CR}\varepsilon_R\to0\) still holds. Thus (12) implies
\(\widetilde\Theta=\Theta\). This proves uniqueness in the
bounded-primal solution class on the common population spaces.

This uniqueness also permits restarting along the constructed
trajectory inside the same local interval. Fix
\(0\le\sigma<S\le S_0\), and let \(\widetilde\Theta\) be any
bounded-primal uncut solution on \([\sigma,S]\) with
\(\widetilde\Theta(\sigma)=\Theta(\sigma)\). Compare it with
the restriction of \(\Theta_R\), whose initial discrepancy at
\(\sigma\) is already controlled by (12). For constants
\(C_0,C_1\) independent of \(R\),
\[
\begin{aligned}
\sup_{\sigma\le s\le S}
d(\widetilde\Theta(s),\Theta_R(s))
\le{}&e^{C_1(1+R)(S-\sigma)}
\left[d(\Theta(\sigma),\Theta_R(\sigma))
 +C_1(S-\sigma)\varepsilon_R\right],\\
d(\Theta(\sigma),\Theta_R(\sigma))
\le{}&C_0S e^{C_0(1+R)S}\varepsilon_R .
\end{aligned}
\]
Both right sides tend to zero because
\(\varepsilon_R=2K e^{-R^2/(16K^2)}\). Hence
\(\widetilde\Theta=\Theta\) on \([\sigma,S]\).
This is restart uniqueness only within the already constructed
feature interval; it supplies no continuation beyond \(S_0\).

## Fixed-program laws, empirical feedback, and the finite tails

The standard finite Gaussian construction needed here is independent
of the scalar-response identification premise. At fixed \(R,\Delta\),
expand both learned matrices as finite sums of rank-one updates.
Replace their empirical contractions temporarily by the deterministic
population contractions. This defines a finite oracle program.
Its coordinate operations are globally Lipschitz: \(\chi\) is
globally Lipschitz, the middle product has a bounded clipped factor,
and the top readout factor is deterministically bounded by \(aS\)
and can be clipped at that bound without changing oracle values.
The root tuple may include \((Z_0^{(1)},F(Z_0^{(1)}))\), which has
finite second moments.

Gaussian conditioning applies separately to each of the two initial
matrices and its reused transpose. At each new query its input is
measurable with respect to the preceding history. Conditional on old
forward and transpose answers, the residual of the queried matrix
is a fresh Gaussian matrix projected orthogonally to its old input
and output query spans. The other matrix's conditional residual is
unchanged. This sequential argument preserves the required
conditional residual independence even though the queries use both
matrices.

As in TWO_HIDDEN_LAYER_PROOF.md, add independent Gaussian noise of
size \(\epsilon\) to each of finitely many query inputs. Limiting
Gram matrices then have positive Schur complements. Conditioning,
the law of large numbers for the fresh Gaussian coordinates, and
vanishing normalized norms of finite-rank projections give joint
\(\mathcal W_2\) limits, including all contractions. Remove the
input noises using the initial operator bounds and Lipschitz
stability of this fixed finite program. Constants may depend on
its size and on \(R,\Delta\); no uniformity in the program length
is needed here.

For clarity, an oracle preactivation need not equal the action of
its stored finite matrix memory. Their exact difference is a finite
sum of earlier backward vectors multiplied by empirical-minus-
population activation contractions. The corresponding transpose
discrepancy uses activation vectors multiplied by backward
contraction errors. All these scalar errors tend to zero in
probability by the joint \(\mathcal W_2\) limit. Fixed-step
induction, using (6), then compares the oracle with empirical-feedback
clipped Euler and proves the same joint limits for the latter.
This argument is performed before sending \(\Delta\) to zero.

Taking a countable family of finite programs, closed under finite
unions, rational linear combinations, the two matrices and their
transposes, and bounded Lipschitz coordinate operations, constructs
common layer probability spaces. The initial operator bounds pass
to their dense probe classes and extend both initial actions and
adjoints to the generated \(L^2\) spaces. Finite adjunction identities
pass to the limit. This is the common action construction used
above. The representation premise is exactly what identifies its
clipped Euler coordinate laws with the scalar laws satisfying (2).

Combining fixed-program convergence with (7), first at fixed
\(\Delta\) and then letting \(\Delta\to0\), proves fixed-\(R\)
finite-clipped-flow convergence of every finite joint list of the
globally Lipschitz forward/backward measurements, in \(\mathcal W_2\).
The elementary coupling bound used in every same-width comparison is
\[
\mathcal W_2\left(\frac1n\sum_i\delta_{v_i},
                  \frac1n\sum_i\delta_{\widetilde v_i}\right)
\le\frac{\|v-\widetilde v\|_2}{\sqrt n}.
\]
The vector-field bound in (4) supplies time equicontinuity.

In particular, write \(\Theta_{n,R}\) for the finite clipped flow
from zero readout and let
\[
a_{n,R}(s)=
\left(\frac1n\sum_i b_R(q_{n,R,i}^{(2)}(s))^2\right)^{1/2},
\qquad
a_R(s)=\|b_R(q_R^{(2)}(s))\|_{L^2}.
\]
For every fixed \(R\),
\[
\sup_{s\le S}|a_{n,R}(s)-a_R(s)|
\longrightarrow0\quad\text{in probability}.            \tag{13}
\]
Indeed \(b_R\) is 1-Lipschitz, its squared measurement is continuous
with quadratic growth, and thus its norm converges at each fixed
time by \(\mathcal W_2\) convergence. Also (5) and the uniform state
velocity bound make \(q_{n,R}^{(2)}(s)\), and hence \(a_{n,R}(s)\),
Lipschitz in \(s\), with a common constant on the initial
operator-bound event. A finite time net upgrades the convergence
to (13). No finite-width exponential moment, nor a discontinuous
indicator measurement, is required.

## Finite uncut flow and the small prescribed readout

The prescribed finite initialization has
\[
W_{i,0}^{(4)}\sim N(0,n^{-2}),\qquad
\frac{\|W_0^{(4)}\|_2}{\sqrt n}=O_{\mathbb P}(n^{-1}).
\]
The two initial Gaussian operator norms are bounded by a fixed
\(M\) with probability tending to one. Couple the uncut finite flow
to \(\Theta_{n,R}\) using the same first-layer roots and matrices,
but keep the latter's readout initially zero. By (9),
\[
\sup_{s\le S}d_n(\Theta_n^{\rm flow}(s),\Theta_{n,R}(s))
\le e^{C(1+R)S}
\left[
\frac{\|W_0^{(4)}\|_2}{\sqrt n}
 +C\int_0^S a_{n,R}(u)\,du
\right].                                               \tag{14}
\]
The finite uncut flow exists on this interval by its polynomial
primal estimates; this step does not invoke an unproved uncut
stability theorem. The bounded-readout reference in (5) also means
that no coordinatewise-smallness assumption on the nonzero
readout is needed in (14).

At fixed \(R\), (11), (13), and (14) give an asymptotic bound
\(CS e^{C(1+R)S}\varepsilon_R\). This tends to zero as
\(R\to\infty\). Combining (14), fixed-\(R\) action-law convergence,
and (12) proves the local uncut finite-flow action-law limit.

The norm estimate is strong enough for additional gate-containing
measurements. Equation (8) first controls \(\delta^{(2)}\), then
operator bounds control \(q^{(1)}=(W^{(2)})^*\delta^{(2)}\).
Finite joint laws of \(Z^{(1)},q^{(1)}\) therefore converge in
\(\mathcal W_2\), uniformly in time. Their population \(L^2\) paths
are continuous and have compact time images. Their squared tails
are uniformly integrable. Clipping \(q^{(1)}\) at an additional
fixed level and then removing that auxiliary clip proves the
corresponding statements for
\(\phi'(Z^{(1)})q^{(1)}\) and
\(\phi'(Z^{(1)})^2q^{(1)}\). The same argument treats subsequent
bounded gates and operator calls in the named network velocities.
This requires no Gaussian tail for \(q^{(1)}\).

## Exact raw GD on its variable computational clock

Use the prescribed raw GD with \(\eta=n^{-2}\). For this local
comparison no global coercivity theorem is needed. Set
\[
\varepsilon=\frac{\|W_0^{(4)}\|_2}{\sqrt n},\qquad
\bar S=\min\{S_0,1/(4a^2)\},\qquad T_0=\bar S/4,
\qquad K_\eta=\lceil T_0/\eta\rceil.
\]
Work on the event \(\varepsilon\le1/(8a)\), whose probability
tends to one, and take \(\eta\le\bar S/24\). For any prefix
whose previous feature increments are positive and whose current
clock \(s_k\) is at most \(\bar S\), the exact readout updates give
\[
\frac{\|W_k^{(4)}\|_2}{\sqrt n}\le\varepsilon+as_k,
\qquad
|f_{n,k}|\le a\varepsilon+a^2s_k\le\frac38.
\]
It follows at the current node that
\[
\frac54\eta\le\alpha_k=2\eta(1-f_{n,k})
\le\frac{11}{4}\eta<3\eta.
\]
Starting from \(s_0=0\), induct on the physical steps. If
\(k\eta\le T_0\) and \(s_k\le3k\eta\), then
\[
s_{k+1}\le3k\eta+3\eta
\le3T_0+3\eta\le\frac78\bar S.
\]
This closes the positive-clock induction for every step needed
on \([0,T_0]\), including the last interpolation endpoint.
Consequently
\[
0<\alpha_k\le3\eta,\qquad
s_k=\sum_{j<k}\alpha_j\le3k\eta
\quad(0\le k\le K_\eta),
\]
where the increment assertion is used for \(k<K_\eta\).
The positive-step primal estimates (4), with the initial
readout added, now apply on this prefix independently of width.
For the rest of this section take \(S=\bar S\).
Define \(x_k^{(1)}=F(z_k^{(1)})\). Coordinatewise, its update is
exactly
\[
\begin{aligned}
x_{k+1}^{(1)}
={}&x_k^{(1)}+\alpha_k q_{n,k}^{(1)}\\
&+\alpha_k^2 z_k^{(1)}\phi'(z_k^{(1)})^2
                         (q_{n,k}^{(1)})^2
 +\frac{\alpha_k^3}{3}\phi'(z_k^{(1)})^3
                         (q_{n,k}^{(1)})^3.
\end{aligned}                                                        \tag{15}
\]
Products and powers in (15) are coordinatewise. The other three
blocks already are Euler updates for the uncut field (1).
Uniform operator and readout bounds give
\(\|q_{n,k}^{(1)}\|_2/\sqrt n\le C\).
Since \(\sup_z|z|\phi'(z)^2<\infty\), the additional vector in
(15) has normalized Euclidean norm at most
\[
C(\alpha_k^2\sqrt n+\alpha_k^3 n).
\]
Consequently, on every prefix certified by the local bootstrap,
its summed norm is at most
\[
CS\left((\max_k\alpha_k)\sqrt n
             +(\max_k\alpha_k)^2n\right)
\le C_S(\eta\sqrt n+\eta^2n)\longrightarrow0.            \tag{16}
\]

Compare this perturbed uncut Euler path with the exact finite
clipped reference \(\Theta_{n,R}(s_k)\). Subtracting one reference
step and using (9) gives
\[
d_{k+1}\le[1+C(1+R)\alpha_k]d_k
 +C\alpha_k a_{n,R}(s_k)
 +C_R\alpha_k^2
 +C(\alpha_k^2\sqrt n+\alpha_k^3n).                     \tag{17}
\]
Here \(d_k=d_n(\Theta_n^{\rm GD}(s_k),\Theta_{n,R}(s_k))\).
Its initial value is the small normalized readout norm.

The randomness of the partition \((s_k)\) causes no tail issue.
The Lipschitz bound for \(a_{n,R}\) used in (13) gives pathwise,
for every partition with maximum step \(A_n\),
\[
\sum_{k<K}\alpha_k a_{n,R}(s_k)
\le\int_0^{s_K} a_{n,R}(u)\,du+C S A_n
\le\int_0^S a_{n,R}(u)\,du+C S A_n                    \tag{18}
\]
for \(K\le K_\eta\). It applies also to partial final intervals.
Thus (13), discrete
Gronwall in the positive increments \(\alpha_k\), and (16) give
\[
\begin{aligned}
\max_{0\le k\le K_\eta}d_k\le e^{C(1+R)S}\Big[
&\frac{\|W_0^{(4)}\|_2}{\sqrt n}
 +C\int_0^S a_{n,R}(u)\,du\\
&+C_R\eta+C_S(\eta\sqrt n+\eta^2n)\Big],
\end{aligned}                                                        \tag{19}
\]
All relevant clocks, including the last interpolation endpoint,
are at most \(7S/8\) by the local bootstrap.
For fixed \(R\), take \(n\to\infty\); then let \(R\to\infty\).
The right side tends to zero in probability by (11).

For interpolation of the original raw parameters, apply the exact
cubic identity (15) with any fractional step
\(0\le\alpha\le\alpha_k\). It gives the same vanishing bound between
the transform of the raw linear interpolant and the transformed
Euler interpolant. Thus (19) also controls the specified
interpolation uniformly between its nodes.

## Return to physical time and the local conclusions

Use \(\bar S,T_0\) from the local bootstrap above.
All previous arguments apply with \(S=\bar S\).
The zero-readout reference and limiting population paths obey
\(|f_R(s)|,|f(s)|\le a^2s\le1/4\). Their physical clocks are the
unique solutions of
\[
\frac{ds_R}{dt}=2[1-f_R(s_R)],\qquad
\frac{ds}{dt}=2[1-f(s)],\qquad s_R(0)=s(0)=0.            \tag{20}
\]
The predictors are uniformly Lipschitz in feature time because
the output map is Lipschitz in (3) on the primal bounds and the
state velocities are uniformly bounded. Thus (20) is an ordinary
scalar Lipschitz initial-value problem.

For the actual finite feature flow, the readout equation gives
\(\|W^{(4)}(s)\|_2/\sqrt n\le\varepsilon+as\).
Hence \(|f_n(s)|\le3/8\) while \(s\le\bar S\), on the same
event \(\varepsilon\le1/(8a)\). Its physical clock therefore
has derivative in \([5/4,11/4]\subset(0,3)\) until any first
exit from this feature interval. Since \(3T_0<\bar S\), the
first exit cannot occur before \(T_0\). The local GD induction
gives the identical upper bound on its interpolated clock.
Thus all clocks under comparison stay strictly below \(\bar S\)
on this physical interval, without using predictor monotonicity
or a global optimization theorem.
The GD clock is linearly interpolated in physical time and has
slope \(2(1-f_{n,k})\) on its \(k\)-th physical step.

The output difference of two states is at most \(C d\). Comparing
the scalar clocks and using (14) or (19), scalar Gronwall gives
their uniform difference on \([0,T_0]\) bounded by a constant times
the corresponding feature-path error, plus the vanishing one-step
interpolation error for GD. Multiplying a clock discrepancy by
the uniform reference velocity bound controls its state effect.
Therefore the two exact finite-width algorithms satisfy
\[
\sup_{t\le T_0}
d_n\bigl(\Theta_n^{\rm GD}(t),\Theta_n^{\rm flow}(t)\bigr)
\longrightarrow0\quad\text{in probability}.            \tag{21}
\]
Both limits are compared to the same zero-readout clipped finite
reference before removing \(R\). Thus (21) does not require a
prior uncut Lipschitz bound.

Their finite joint measured laws converge uniformly on
\([0,T_0]\) to the unique local population solution reparametrized
by (20). Predictions and losses converge uniformly as well.
Since \(F^{-1}\) is 1-Lipschitz, these conclusions include the
original first-layer preactivation, not only its transform.
The limit operator statement is an action-law statement on the
generated population spaces, as explained after (3).

Uniqueness also applies to the raw physical equations. For a
competing raw integral solution with bounded primal norms, the
first-layer equation supplies absolutely continuous coordinate
paths with velocity \(2(1-f)\phi'(Z^{(1)})q^{(1)}\).
The scalar chain rule on each such path gives
\[
 F(Z^{(1)}(t))
 =F(Z^{(1)}_0)+\int_0^t2(1-f(u))q^{(1)}(u)\,du.
\]
The right side belongs to \(L^2\). Thus the transformed coordinate
belongs to the class in (3), even if not assumed at the outset.

Define its feature clock while \(1-f>0\). With zero initial
readout, \(|W^{(4)}|\le as\) and \(|f|\le a^2s\).
Before the clock reaches \(\bar S\), it obeys \(|f|\le1/4\)
and \(0<s'\le5/2\). It cannot reach \(\bar S\) by
\(T_0=\bar S/4\), nor can \(1-f\) vanish there. It therefore
defines a feature-time solution throughout its physical interval.
Feature-time uniqueness identifies it with the constructed
trajectory up to its clock endpoint, and scalar-clock uniqueness
in (20) identifies the physical trajectories. From a reached
state the same argument uses
\(|W^{(4)}(s_*)|\le as_*\), the restart comparison above, and
\(s(t)\le(5/2)t<\bar S\). This proves raw physical restart
uniqueness within the same local interval.

For the velocity conclusions below, at every GD mesh node use the
right-hand derivative of the raw linear interpolant and of its
recomputed preactivations. If \(T_0\) is itself a terminal mesh
node, use the left-hand derivative there. This convention does
not affect any integrated quantity.

The named uncut backward fields and kernel blocks follow by the
additional clipping/uniform-integrability argument after (14).
For hidden trajectory laws and integrated squared speeds, use
the exact feature-time preactivation velocities
\[
\frac{dZ^{(1)}}{ds}=\phi'(Z^{(1)})q^{(1)},
\]
\[
\frac{dZ^{(2)}}{ds}
=\mathbb E[(H^{(1)})^2]\delta^{(2)}
 +W^{(2)}[\phi'(Z^{(1)})^2q^{(1)}],
\]
\[
\frac{dZ^{(3)}}{ds}
=\mathbb E[(H^{(2)})^2]\delta^{(3)}
 +W^{(3)}\left[\phi'(Z^{(2)})\frac{dZ^{(2)}}{ds}\right].
                                                               \tag{22}
\]
All are continuous \(L^2\) paths by the same truncation argument.
Their finite laws and squared norms converge uniformly. For GD,
the difference between the derivatives of the recomputed
preactivations and the left-endpoint versions of (22) is handled
by clipping the relevant velocity coordinates at a fixed level.
At that level gate changes vanish with the step, and the
complement is bounded by their uniformly integrable squared tails.
This proves convergence of integrated squared speeds on
\([0,T_0]\). Integrating a jointly measurable version of each
population velocity and applying Fubini supplies absolutely
continuous coordinate paths with the stated \(L^2\) values.
Finally, for an absolutely continuous scalar path,
\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^{T_0}|\dot z(t)|^2\,dt.
\]
Joint finite-grid laws and this estimate give each hidden-layer
trajectory law in \(\mathcal W_2(C([0,T_0]))\).

These conclusions remove cutoff and comparison hypotheses on this
positive local interval. Their sole scalar identification dependency
is the representation premise above. Nothing here extends the
audited tail estimate beyond \(S_0\), and no all-horizon population
well-posedness or interchange with infinite physical time is claimed.


---

# The local limit is an actual gradient flow

This note supplies the gradient assertion once the uncut local
solution has been constructed. It introduces no additional
existence or tail premise.

Use the three population spaces and matrix actions in
LOCAL_ACTION_SPACE_AND_FLOW.md. Averages in a layer are denoted by
\(E_\ell\). Retain the forward equations
\[
 H^{(1)}=\phi(Z^{(1)}),\quad
 Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),\quad
 Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}).
\]
Set
\[
 f=E_3[W^{(4)}H^{(3)}],\qquad r=f-1,\qquad L=r^2,
\]
\[
 \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),\quad
 \delta^{(2)}=\phi'(Z^{(2)})(W^{(3)})^*\delta^{(3)},\quad
 \delta^{(1)}=\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)}.
 \tag{1}
\]
The derivatives exclude the residual. Each belongs to its layer's
mean-square space, since the gates are bounded and the matrix
actions are bounded.

The trained changes of \(W^{(2)},W^{(3)}\) are square-summable
operators, even though the initial Gaussian actions need not be.
Precisely, the size of a square-summable operator \(A\) is
\[
 \|A\|_{\rm HS}^2=\sum_j\|Ae_j\|_{L^2}^2,
\]
for any orthonormal basis of its input space; this sum does not
depend on the basis. This is the population counterpart of a
matrix's ordinary squared Frobenius norm. For the rank-one action
\((U\otimes V)B=U E[VB]\), the size is
\(\|U\otimes V\|_{\rm HS}=\|U\|_{L^2}\|V\|_{L^2}\).
An integral of the continuous rank-one velocities therefore has
finite HS size on a bounded time interval.

To justify this assertion for the cutoff limit as well, the
comparison estimate in LOCAL_CUTOFF_BRIDGE.md proves uniform
mean-square convergence of \(\delta^{(2)}_R\) and
\(\delta^{(3)}_R\) to their uncut values, as well as convergence
of \(H^{(1)}_R,H^{(2)}_R\). The rank-one difference inequality
holds in HS norm just as in operator norm. Thus the integrals of
the matrix velocities converge in HS norm. Their limits are the
same matrix actions already obtained in operator norm.

Consider the raw parameter space with coordinates
\[
 (Z^{(1)},\,W^{(2)}-W^{(2)}_0,\,
 W^{(3)}-W^{(3)}_0,\,W^{(4)}).
\]
Its squared length for a variation is
\[
 E_1[(dZ^{(1)})^2]
 +\|dW^{(2)}\|_{\rm HS}^2
 +\|dW^{(3)}\|_{\rm HS}^2
 +E_3[(dW^{(4)})^2].                                   \tag{2}
\]
All affine states in this space have bounded matrix actions:
the HS size bounds the operator norm of each trained change.

The predictor is differentiable in the norm (2). Here is the
needed elementary remainder argument, avoiding an incorrect
claim that every pointwise nonlinearity is differentiable as a
map from all of \(L^2\) to \(L^2\). For any fixed \(B\in L^2\),
the bounded first and second derivatives of \(\phi\) give
\[
 \begin{aligned}
 &\left|E B[\phi(Z+e)-\phi(Z)-\phi'(Z)e]\right|\\
 &\quad\le C R\,E e^2
       +2\|B\,\mathbf1_{\{|B|>R\}}\|_{L^2}\|e\|_{L^2}.
 \end{aligned}                                         \tag{3}
\]
On \(|B|\le R\) use the quadratic Taylor remainder; on the
complement use its bound \(2|e|\). First fix \(R\) and send
\(\|e\|_{L^2}\) to zero, then send \(R\) to infinity. The
remainder in (3) is \(o(\|e\|_{L^2})\).

Successive forward differences are \(O(\|d\theta\|)\) in mean
square: use bounded activations, Lipschitz \(\phi\), bounded
matrix actions, and
\(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\).
Expand the scalar predictor from the top layer downward.
At each layer apply (3) with the fixed backward coefficient at
the original state. Terms containing both a matrix change and
an activation change are \(O(\|d\theta\|^2)\), by the operator
inequality and Cauchy--Schwarz. The same is true of the product
of a readout change and a top activation change. This proves
the norm derivative
\[
 \begin{aligned}
 df={}&E_1[\delta^{(1)}dZ^{(1)}]
 +E_2[\delta^{(2)}\,dW^{(2)}H^{(1)}]\\
 &+E_3[\delta^{(3)}\,dW^{(3)}H^{(2)}]
 +E_3[H^{(3)}dW^{(4)}].
 \end{aligned}                                         \tag{4}
\]
Equivalently its gradient in (2) is
\[
 \nabla f=
 \left(\delta^{(1)},\,
       \delta^{(2)}\otimes H^{(1)},\,
       \delta^{(3)}\otimes H^{(2)},\,
       H^{(3)}\right).                                 \tag{5}
\]
The rank-one entries follow from the identity
\(\langle U\otimes V,A\rangle_{\rm HS}=E[U\,AV]\).
The gradient is continuous. For example, bounded gates converging
in probability multiply a fixed \(L^2\) variable continuously
in \(L^2\), by truncating that fixed variable; combine this
observation with forward continuity and reverse operator bounds
in (1). Local Lipschitz continuity of the uncut gradient is
neither asserted nor needed for the differentiability claim.

The already constructed feature-time solution has
\(X^{(1)}=F(Z^{(1)})\) and
\(dX^{(1)}/ds=(W^{(2)})^*\delta^{(2)}\).
Since \((F^{-1})'(F(z))=\phi'(z)\), its raw first coordinate
satisfies \(dZ^{(1)}/ds=\delta^{(1)}\) in mean square.
One direct chain-rule justification uses coordinate absolute
continuity and the bound \(|(F^{-1})'|\le1\), then approximates
the mean-square velocity by bounded variables. This also gives
mean-square continuity of the resulting velocity.
Together with the other three integral equations, (5) yields
\[
 \frac{d\theta}{ds}=\nabla f(\theta).                    \tag{6}
\]

On the local interval chosen in LOCAL_CUTOFF_BRIDGE.md,
\(|f|<1\). Its physical clock solves
\(ds/dt=2(1-f)\). Hence the physical evolution is exactly
\[
 \frac{d\theta}{dt}=-2r\,\nabla f=-\nabla L.             \tag{7}
\]
In particular, the derivative of its predictor is
\[
 \frac{df}{dt}=-2r\,\kappa,\qquad
 \frac{dL}{dt}=-4r^2\kappa,
\]
where the four nonnegative kernel contributions are
\[
 \begin{aligned}
 \kappa_1&=E_1[(\delta^{(1)})^2],\\
 \kappa_2&=E_2[(\delta^{(2)})^2]\,E_1[(H^{(1)})^2],\\
 \kappa_3&=E_3[(\delta^{(3)})^2]\,E_2[(H^{(2)})^2],\\
 \kappa_4&=E_3[(H^{(3)})^2],\qquad
 \kappa=\kappa_1+\kappa_2+\kappa_3+\kappa_4.
 \end{aligned}                                         \tag{8}
\]

This state is autonomous: the present four objects determine
every quantity in (1), then determine the four velocities.
The Gaussian response coefficients used to prove the limit are
not external inputs to (7). Both initial matrix actions and all
their trained changes are contained in the current matrix
operators. Local uniqueness and restartability on the constructed
interval are supplied by the cutoff comparison, not by a claim
that the uncut gradient is locally Lipschitz.

Nothing in this note proves that the local solution can be
continued to every finite physical time. That is a separate
outstanding part of the requested theorem.


---

# Local feature learning in all three hidden layers

This lemma concerns the canonical local population flow with arctangent
activation and initially zero output weights. It assumes that the local
flow and its Gaussian operator actions have been constructed. It does
not construct that flow, identify it with a trained finite network, or
assert existence for all time. The small-time conclusions below require
only strong continuity in the natural second-moment spaces, the canonical
integral equations, and bounded initial operator actions.

## Setup and the local statement

For layer \(\ell\), let \(\mathcal H_\ell=L^2(\Omega_\ell)\), with
inner product \(\langle u,v\rangle_\ell=\mathbb E[uv]\). Write
\(\|u\|_\ell^2=\mathbb E[u^2]\). Let
\(W^{(2)}(s):\mathcal H_1\to\mathcal H_2\) and
\(W^{(3)}(s):\mathcal H_2\to\mathcal H_3\) be the bounded operator
actions supplied by the local construction, and let a star denote their
Hilbert-space adjoints. For \(u\in\mathcal H_\ell\) and
\(v\in\mathcal H_{\ell-1}\), define the rank-one operator
\[
 (u\otimes v)x=u\langle v,x\rangle_{\ell-1}.
\]
Its Hilbert--Schmidt norm is \(\|u\|_\ell\|v\|_{\ell-1}\).
This is the population version of \(uv^{\mathsf T}/n\), when finite
vectors have inner product \(u^{\mathsf T}v/n\).

Set \(\phi(x)=\arctan x\), \(d(x)=\phi'(x)=(1+x^2)^{-1}\),
and \(a=\pi/2\). The variable \(s\) is feature time. The local
canonical equations are
\[
 H^{(\ell)}=\phi(Z^{(\ell)}),\qquad
 Z^{(2)}=W^{(2)}H^{(1)},\qquad Z^{(3)}=W^{(3)}H^{(2)},
\]
\[
 D_\ell u=d(Z^{(\ell)})u,\qquad
 \delta^{(3)}=D_3W^{(4)},\qquad
 q^{(2)}=(W^{(3)})^*\delta^{(3)},\qquad
 \delta^{(2)}=D_2q^{(2)},\qquad
 q^{(1)}=(W^{(2)})^*\delta^{(2)},
\]
\[
 \frac{dZ^{(1)}}{ds}=D_1q^{(1)},\quad
 \frac{dW^{(2)}}{ds}=\delta^{(2)}\otimes H^{(1)},\quad
 \frac{dW^{(3)}}{ds}=\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{ds}=H^{(3)}.                              \tag{1}
\]
These equations can equivalently be assumed in integral form. The
states are continuous in their \(L^2\) spaces; the weights are continuous
in operator norm, as also follows from their rank-one integral updates.
All limits below are in these \(L^2\) spaces unless otherwise stated.

Initially \(W^{(4)}_0=0\). The Gaussian initialization supplies
\(Z^{(1)}_0\sim N(0,1)\), the independent Gaussian initial actions
\(W^{(2)}_0,W^{(3)}_0\), and the forward laws
\[
 Z^{(2)}_0\sim N(0,m_1),\qquad Z^{(3)}_0\sim N(0,m_2),\qquad
 m_\ell=\|H^{(\ell)}_0\|_\ell^2>0.                       \tag{2}
\]
Thus, for a standard Gaussian \(G\),
\[
 m_1=\mathbb E\phi(G)^2,\quad
 m_2=\mathbb E\phi(\sqrt{m_1}G)^2,\quad
 m_3=\mathbb E\phi(\sqrt{m_2}G)^2.
\]
The notation \(D_{\ell,0}\) means multiplication by
\(d(Z^{(\ell)}_0)\).

Define the initial backward fields, each on its indicated population,
\[
 \beta_3=H^{(3)}_0d(Z^{(3)}_0)\in\mathcal H_3,\quad
 P_2=(W^{(3)}_0)^*\beta_3\in\mathcal H_2,\quad
 B_2=D_{2,0}P_2\in\mathcal H_2,\quad
 P_1=(W^{(2)}_0)^*B_2\in\mathcal H_1.                    \tag{3}
\]
Define the bounded self-adjoint operators
\[
 \mathcal A^{(2)}_0
 =m_1 I+W^{(2)}_0D_{1,0}^{\,2}(W^{(2)}_0)^*,
\]
\[
 \mathcal A^{(3)}_0
 =m_2 I+W^{(3)}_0D_{2,0}\mathcal A^{(2)}_0
                         D_{2,0}(W^{(3)}_0)^*.           \tag{4}
\]
Finally put
\[
 V_1=D_{1,0}P_1,\qquad
 V_2=\mathcal A^{(2)}_0B_2,\qquad
 V_3=\mathcal A^{(3)}_0\beta_3.                           \tag{5}
\]

As \(s\downarrow0\), the local flow satisfies
\[
 W^{(4)}(s)=sH^{(3)}_0+o(s),\quad
 \delta^{(3)}(s)=s\beta_3+o(s),\quad
 q^{(2)}(s)=sP_2+o(s),
\]
\[
 \delta^{(2)}(s)=sB_2+o(s),\qquad q^{(1)}(s)=sP_1+o(s),  \tag{6}
\]
and, for all three hidden layers,
\[
 \frac{dZ^{(\ell)}}{ds}=sV_\ell+o(s),\qquad
 Z^{(\ell)}(s)-Z^{(\ell)}_0
       =\frac{s^2}{2}V_\ell+o(s^2),
\]
\[
 \frac{dH^{(\ell)}}{ds}=sD_{\ell,0}V_\ell+o(s),\qquad
 H^{(\ell)}(s)-H^{(\ell)}_0
       =\frac{s^2}{2}D_{\ell,0}V_\ell+o(s^2).            \tag{7}
\]
Every \(V_\ell\) and every \(D_{\ell,0}V_\ell\) has strictly
positive \(L^2\) norm. Thus the second-order changes are genuine in
each preactivation and each hidden feature.

## Strong limits without differentiability assumptions on an \(L^2\) map

The following elementary multiplier fact is sufficient. If
\(x_s\to x_0\) in probability, \(v_s\to v_0\) in \(L^2\), and
\(g\) is bounded and continuous, then
\[
 g(x_s)v_s\longrightarrow g(x_0)v_0\quad\text{in }L^2.   \tag{8}
\]
Indeed, the part containing \(v_s-v_0\) is bounded by
\(\|g\|_\infty\|v_s-v_0\|_2\). For the other part, first restrict
to \(|v_0|\le K\), where bounded convergence in probability gives
convergence of its squared expectation, and then let \(K\to\infty\).
The remaining bound is
\(4\|g\|_\infty^2\mathbb E[|v_0|^2\mathbf1_{\{|v_0|>K\}}]\).
Only the fixed reference \(v_0\in L^2\) is used.

The same argument justifies the chain rule along a differentiable
\(L^2\) curve. If \(x(s+h)-x(s)=hv_h\) and \(v_h\to v\) in
\(L^2\), then
\[
 \frac{\phi(x(s+h))-\phi(x(s))}{h}
 =v_h\int_0^1 d\bigl(x(s)+rh v_h\bigr)\,dr
 \longrightarrow d(x(s))v\quad\text{in }L^2.
\]
The integral multiplier is bounded by one and converges in probability
to \(d(x(s))\). This is a chain rule along the given curve, not an
assertion of Frechet differentiability of a Nemytskii map on \(L^2\).

The integral equation for \(W^{(4)}\) and continuity of \(H^{(3)}\)
give \(W^{(4)}(s)/s\to H^{(3)}_0\). Apply (8), then operator-norm
continuity of \(W^{(3)}\), then (8) again, and finally operator-norm
continuity of \(W^{(2)}\). This proves every limit in (6).

All right-hand sides of (1) are continuous by (8), so the integral
equations give strong derivatives. The chain rule above yields the
exact identities
\[
 \frac{dZ^{(2)}}{ds}=\mathcal A^{(2)}(s)\delta^{(2)},\qquad
 \mathcal A^{(2)}(s)
 =\|H^{(1)}(s)\|_1^2 I
       +W^{(2)}(s)D_1(s)^2(W^{(2)}(s))^*,
\]
\[
 \frac{dZ^{(3)}}{ds}=\mathcal A^{(3)}(s)\delta^{(3)},\qquad
 \mathcal A^{(3)}(s)
 =\|H^{(2)}(s)\|_2^2 I
       +W^{(3)}(s)D_2(s)\mathcal A^{(2)}(s)
                         D_2(s)(W^{(3)}(s))^*.           \tag{9}
\]
For example, the first identity uses
\((\delta^{(2)}\otimes H^{(1)})H^{(1)}
=\|H^{(1)}\|_1^2\delta^{(2)}\) and
\(dH^{(1)}/ds=D_1^2(W^{(2)})^*\delta^{(2)}\).
The second follows from
\(dZ^{(3)}/ds=\|H^{(2)}\|_2^2\delta^{(3)}
 +W^{(3)}D_2\,dZ^{(2)}/ds\).

The operators in (9) are uniformly bounded near zero and converge
strongly on every fixed \(L^2\) vector to the operators in (4).
To verify this, apply (8) successively to the bounded gates and use
operator-norm continuity of the weights. No operator-norm convergence
of the gate multiplication operators is needed. Combining this strong
convergence with (6) proves the derivative expansions in (7).
Integration proves the state expansions; a further use of (8) and the
curve chain rule proves the feature expansions.

## Initial transpose conditioning and strict positivity

Here is the initial Gaussian conditioning calculation needed for (3).
For a finite Gaussian matrix \(W\) with entry variance \(1/n\), an
independent nonzero input \(h\), and \(y=Wh\), conditioning on \(h,y\)
gives
\[
 W=\frac{yh^{\mathsf T}}{\|h\|_2^2}
        +\widetilde W P_{h^\perp}
 \quad\text{in conditional law},
\]
where \(\widetilde W\) is an independent matrix with the same entry
variance. If \(u\) is measurable from \(h,y\) and auxiliary randomness
independent of this conditional residual, then
\[
 W^{\mathsf T}u
 =h\,\frac{y^{\mathsf T}u/n}{\|h\|_2^2/n}
  +\sqrt{\|u\|_2^2/n}\,P_{h^\perp}g
 \quad\text{in conditional law},                       \tag{10}
\]
with a fresh standard Gaussian vector \(g\). The removed projection
has conditional normalized mean square \(1/n\). Thus, when the input
contractions have their canonical limits, its scalar transpose law is
\(c h+\sigma G\), with
\(c=\mathbb E[yu]/\mathbb E[h^2]\) and
\(\sigma^2=\mathbb E[u^2]\). The innovation \(G\) is independent
of the existing same-population initial data. Importantly, the
innovation variance is \(\mathbb E[u^2]\), without subtraction of
the response component.

First apply (10) to \(W^{(3)}_0\), input \(H^{(2)}_0\), output
\(Z^{(3)}_0\), and transpose input \(\beta_3\). It gives the joint
same-population law
\[
 P_2=c_3H^{(2)}_0+\sigma_3G^{\mathrm b}_2,\qquad
 c_3=\frac{\mathbb E[Z^{(3)}_0\beta_3]}{m_2}>0,\qquad
 \sigma_3^2=\mathbb E[\beta_3^2]>0,                      \tag{11}
\]
where \(G^{\mathrm b}_2\sim N(0,1)\) is independent of
\(Z^{(2)}_0\). Both inequalities follow because
\(z\phi(z)d(z)>0\) for \(z\ne0\), and the Gaussian variance
\(m_2\) is positive. Consequently
\[
 B_2=d(Z^{(2)}_0)
       \bigl(c_3\phi(Z^{(2)}_0)+\sigma_3G^{\mathrm b}_2\bigr),
\]
\[
 \sigma_2^2:=\mathbb E[B_2^2]
 =\mathbb E\left[d(Z^{(2)}_0)^2
          \bigl(c_3^2\phi(Z^{(2)}_0)^2+\sigma_3^2\bigr)\right]>0.
                                                                    \tag{12}
\]

For the second application, condition on the bottom initialization,
\(Z^{(2)}_0=W^{(2)}_0H^{(1)}_0\), and the entire independent initial
matrix \(W^{(3)}_0\). The field \(B_2\) is then fixed and introduces
no further information about the conditional residual of
\(W^{(2)}_0\). Formula (10) therefore gives
\[
 P_1=c_2H^{(1)}_0+\sigma_2G^{\mathrm b}_1,\qquad
 c_2=\frac{\mathbb E[Z^{(2)}_0B_2]}{m_1}
 =\frac{c_3}{m_1}
       \mathbb E[Z^{(2)}_0d(Z^{(2)}_0)\phi(Z^{(2)}_0)]>0. \tag{13}
\]
Here \(G^{\mathrm b}_1\) is standard Gaussian, independent of
\(Z^{(1)}_0\); the successive fresh innovations can be chosen as
independent groups in the canonical initial source construction.
The factor \(c_3\) in (13) retains the return through the third-layer
matrix. Treating \(B_2\) as an independent centered multiplier would
lose this term.

Only initial finite Gaussian queries are involved in (10)--(13).
Their contractions converge by conditional Gaussian averaging: the
forward activation averages are bounded; in the transpose step the
rank-one projection error vanishes in normalized \(L^2\); bounded
gates preserve that convergence. Pairwise contractions then converge
by Cauchy--Schwarz. This calculation uses no trained-state limit.

By (12)--(13), \(P_1\ne0\), \(B_2\ne0\), and \(\beta_3\ne0\)
in their \(L^2\) spaces. Moreover,
\[
 \mathcal A^{(2)}_0\succeq m_1I,\qquad
 \mathcal A^{(3)}_0\succeq m_2I.                         \tag{14}
\]
For any nonzero \(v\), the first inequality implies
\(\|\mathcal A^{(2)}_0v\|\ge m_1\|v\|\), by taking its inner
product with \(v\); the second gives the corresponding bound with
\(m_2\). Finally, multiplication by \(d(Z^{(\ell)}_0)\) has zero
kernel because \(d(z)>0\) for every finite \(z\). These observations
prove the strict positivity asserted after (7).

## Physical time, kernel blocks, and squared speeds

Let \(f(s)=\langle W^{(4)}(s),H^{(3)}(s)\rangle_3\).
Equation (6) gives \(f(s)=m_3s+o(s)\). In a sufficiently small
neighborhood of zero, \(f(s)<1\), so define physical time by
\[
 \frac{ds}{dt}=2(1-f(s)),\qquad s(0)=0.
\]
Equivalently,
\(t(s)=\int_0^s[2(1-f(u))]^{-1}\,du\). It follows that
\[
 s(t)=2t+o(t),\qquad 1-f(s(t))=1+o(1).                  \tag{15}
\]
This is precisely the residual factor for squared loss \((f-1)^2\).
In particular, with the left-hand sides evaluated at feature time
\(s(t)\),
\[
 Z^{(\ell)}-Z^{(\ell)}_0=2t^2V_\ell+o(t^2),\qquad
 H^{(\ell)}-H^{(\ell)}_0=2t^2D_{\ell,0}V_\ell+o(t^2).
\]

Define the four population kernel blocks at physical time \(t\) by
\[
 \kappa_1(t)=\|D_1q^{(1)}\|_1^2,\quad
 \kappa_2(t)=\|H^{(1)}\|_1^2\|\delta^{(2)}\|_2^2,\quad
 \kappa_3(t)=\|H^{(2)}\|_2^2\|\delta^{(3)}\|_3^2,\quad
 \kappa_4(t)=\|H^{(3)}\|_3^2,
\]
where every right-hand side is evaluated at \(s=s(t)\). Put
\[
 \gamma_1=\|D_{1,0}P_1\|_1^2>0,\qquad
 \gamma_2=m_1\|B_2\|_2^2>0,\qquad
 \gamma_3=m_2\|\beta_3\|_3^2>0.
\]
Then
\[
 \kappa_\ell(t)=4\gamma_\ell t^2+o(t^2)\quad(\ell=1,2,3),
 \qquad \kappa_4(t)=m_3+o(1).                           \tag{16}
\]
In particular all three hidden kernel blocks are strictly positive
at every sufficiently small positive time. These coefficients are
finite using only the second moments established above. For example,
\[
 \gamma_1=\mathbb E\left[d(Z^{(1)}_0)^2
           \bigl(c_2^2\phi(Z^{(1)}_0)^2+\sigma_2^2\bigr)\right]>0.
\]

To state the squared-speed consequence precisely, use the \(L^2\)
norm for the vector blocks \(Z^{(1)},W^{(4)}\) and the
Hilbert--Schmidt norm for the two matrix velocities. Let
\(\mathcal J_\ell(T)\) be the integral from \(0\) to \(T\) of the
squared velocity of block \(\ell\). Equation (1) and the time change
give the exact identity
\[
 \mathcal J_\ell(T)
 =\int_0^T4(1-f(s(t)))^2\kappa_\ell(t)\,dt.
\]
Therefore
\[
 \mathcal J_\ell(T)=\frac{16}{3}\gamma_\ell T^3+o(T^3)
       \quad(\ell=1,2,3),\qquad
 \mathcal J_4(T)=4m_3T+o(T).                            \tag{17}
\]
The initial matrix actions need not be Hilbert--Schmidt; only their
rank-one velocities and subsequent increments use that norm.

The hidden features themselves have positive squared-speed integrals
as well. Equations (7) and (15) give
\[
 \frac{dZ^{(\ell)}}{dt}=4tV_\ell+o(t),\qquad
 \frac{dH^{(\ell)}}{dt}=4tD_{\ell,0}V_\ell+o(t),
\]
and hence
\[
 \int_0^T\left\|\frac{dZ^{(\ell)}}{dt}\right\|_\ell^2dt
       =\frac{16}{3}\|V_\ell\|_\ell^2T^3+o(T^3),
\]
\[
 \int_0^T\left\|\frac{dH^{(\ell)}}{dt}\right\|_\ell^2dt
       =\frac{16}{3}\|D_{\ell,0}V_\ell\|_\ell^2T^3+o(T^3).
                                                                    \tag{18}
\]
All six leading coefficients in (18) are strictly positive. These
are local statements conditional on the canonical flow/action
construction; they make no assertion about the extent of its horizon.

## The kernel changes and the activation remains genuinely nonlinear

The expansions also prove nonconstancy of the total kernel.
Equations (4)--(5) and adjunction give
\[
 \langle\beta_3,\mathcal A^{(3)}_0\beta_3\rangle_3
 =m_2\|\beta_3\|_3^2+m_1\|B_2\|_2^2+\|D_{1,0}P_1\|_1^2
 =\gamma_1+\gamma_2+\gamma_3>0.
\]
Since \(H^{(3)}(s)=H^{(3)}_0+
(s^2/2)D_{3,0}V_3+o(s^2)\), expanding its squared norm gives
\[
 \kappa_4(s)=m_3+s^2(\gamma_1+\gamma_2+\gamma_3)+o(s^2).
\]
In feature time the sum of the three hidden kernel contributions
has the same positive \(s^2\) coefficient. In physical time,
\[
 \kappa(t)
 =m_3+8(\gamma_1+\gamma_2+\gamma_3)t^2+o(t^2).           \tag{19}
\]
Hence \(\kappa\) is not constant on any sufficiently small initial
interval. The gradient identity also gives
\(L(t)=1-4m_3t+o(t)\), and \(L(t)<1\) for small positive \(t\).

For each layer the initial preactivation is a nondegenerate
Gaussian. Its variance is positive. The mean-square error of the
best affine approximation to the activation is
\[
 \inf_{\alpha,\beta\in\mathbb R}
 E_\ell[(\phi(Z^{(\ell)})-\alpha Z^{(\ell)}-\beta)^2]
 =
 \operatorname{Var}(\phi(Z^{(\ell)}))
 -\frac{\operatorname{Cov}(Z^{(\ell)},\phi(Z^{(\ell)}))^2}
        {\operatorname{Var}(Z^{(\ell)})}.               \tag{20}
\]
Initially (20) is strictly positive. Otherwise \(\arctan z\)
would agree with an affine function with probability one under a
full-support Gaussian law; continuity would make them agree for
every real \(z\), which is false. The first and second moments
in (20) are continuous along the constructed mean-square paths,
because \(\phi\) is bounded and Lipschitz. Thus the variance and
(20) remain strictly positive on a common positive initial
interval for all three hidden layers.

