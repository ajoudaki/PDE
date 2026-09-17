# Orthogonal three-input tangent positivity: frozen partial resolution

2026-09-16. Scoped analytical candidate. No experiment, network-limit claim,
or promotion. Inputs were the established `docs/README.md`, `docs/NOTATION.md`,
`docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 and C.4.7.10
B/C.1/D.3, and the complete `three_coordinate_candidate.md`. No other study
artifact or parallel route was read.

**Status.** The full tangent Gram is positive definite at every finite feature
time except possibly a finite set on each compact interval. Its only possible
failure is identified exactly below; every failure has a strictly quadratic
transverse degeneracy. This route does **not** exclude failure at the
unit-label fitting time. Thus it does not prove the requested unit-label open
family. It supplies a precise missing condition and proves the perturbation
bridge conditional on that condition.

## 1. Exact contract and initialized flow

The normalized signed inputs are `e_1,e_2,e_3`, each with label one and mass
`1/3`; physical inputs are `sqrt(3)e_i`. The population closure has order
`p=1`, exact Gaussian coefficient expectations, ridge `eta=1/4096`, and the
constant metric

\[
 \|\delta X\|^2=E_1|\delta w|^2+E_2|\delta c|^2+\|\delta M\|_F^2.
\]

Use the scalar constants of the supplied candidate:

\[
\begin{gathered}
h_i=\tanh G_i,\quad k_i=\tanh(\zeta_i+\alpha h_i),\quad
Z_i=\tanh\Xi_i,\\
v=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt vG),\quad
\alpha=1-\tau,\quad \beta=E[h_i k_i],\quad
\sigma=E[k_i^2],\quad\gamma=1-\sigma,\\
R_h=\sqrt{v+\eta},\quad
R_k=\sqrt{\sigma+\eta-\beta^2/(v+\eta)},\quad
R_Z=\sqrt{\tau+\eta}.
\end{gathered}
\]

Here the lower pairs `(G_i,zeta_i)` are independent across coordinates,
`G_i~N(0,1)`, `zeta_i~N(0,tau)`, and the separate upper population has
independent `Xi_i~N(0,v)`. Define the two-component lower blocks and upper
coordinates

\[
B_i=\left(h_i/R_h,
 (k_i-\beta h_i/(v+\eta))/R_k\right)^T,\qquad z_i=Z_i/R_Z.
\tag{1}
\]

Writing lower coordinates in the interleaved order `(B_1,B_2,B_3)` is only
an orthogonal permutation of the exact inverse-Cholesky features. No metric
or coefficient changes. The initial active middle block has diagonal
two-component rows

\[
m(0)=\left(\frac{\alpha v}{R_hR_Z},
\frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}{R_kR_Z}\right)^T,
\tag{2}
\]

and zero off-diagonal blocks. In particular the actual reverse-response
term `tau gamma` is retained. The lower `G_i,k_i` correlation is the joint
one in (1), not independent sampling.

The constant features remain inactive: joint mark negation makes `w,c`
odd, all active features odd, gates even, and the constant row/column
velocities zero. Restricting notation to the active `3`-by-`6` block below
therefore describes an invariant solution of the full `4`-by-`7` equations.
It imposes no additional sparsity on that active matrix.

For a training input write

\[
\begin{gathered}
a_i=E_1[b_1\tanh w_i],\quad v_i=Ma_i,\quad
H_i=\tanh(z^Tv_i),\quad f_i=E_2[cH_i],\\
d_i=E_2[z\,c\,\operatorname{sech}^2(z^Tv_i)],\quad
Q_i=b_1^TM^Td_i.
\end{gathered}
\tag{3}
\]

The active feature column is `b_1=(B_1,B_2,B_3)`. All transposes in (3)
are the actual transpose of the forward matrix. The supplied candidate
proves unique characteristic existence on every finite feature interval,
permutation invariance, and the exact feature-time equations

\[
\begin{split}
c_s&=(H_1+H_2+H_3)/3,\\
M_s&=\tfrac13\sum_i d_i a_i^T,\\
(w_i)_s&=\tfrac13\operatorname{sech}^2(w_i)Q_i.
\end{split}
\tag{4}
\]

With `F=(f_1+f_2+f_3)/3` and
`C_0=E_2[((H_1(0)+H_2(0)+H_3(0))/3)^2]>0`, that result gives

\[
 f_i=F,\qquad F_s=\|\nabla F\|^2\ge C_0,\qquad F(0)=0.
\tag{5}
\]

Thus `F>0` for `s>0` and the unit-label fitting time `s_*` is uniquely
defined by `F(s_*)=1`, with `s_*<=1/C_0`. Physical time satisfies
`ds/dt=2(1-F)`, so its endpoint is `X(s_*)`.

## 2. Complete permutation reduction

Coordinate permutation acts simultaneously on the full lower pairs and
upper marks and preserves the initialized law, normalized features,
initial matrix, metric, and equations. Uniqueness therefore preserves
that symmetry. Every active matrix block and coefficient column has
the following form, with two-component vectors `m,n,A,B`:

\[
 M_{ij}=\big(m\,\delta_{ij}+n\big)^T,\qquad
 (a_i)_j=A\,\delta_{ij}+B.
\tag{6}
\]

Here `M_ij` is the row on lower block `j` in upper row `i`, and `(a_i)_j`
is lower block `j` in the coefficient of training input `i`. Multiplication
of this full matrix gives

\[
 v_i=p e_i+q\mathbf1,\qquad
 p=m\cdot A,\qquad
 q=m\cdot B+n\cdot A+3n\cdot B.
\tag{7}
\]

Likewise there are scalars `delta,rho` with

\[
 d_i=\delta e_i+\rho\mathbf1.
\tag{8}
\]

These are consequences of symmetry, not a diagonal-matrix approximation.
The longitudinal and transverse coefficients remain allowed to evolve.

Let `g_i=grad f_i` in the full physical metric and let
`K_ij=<g_i,g_j>`. Direct differentiation of (3) gives

\[
 g_i=\big(\operatorname{sech}^2(w_i)Q_i e_i,
                 H_i,d_i a_i^T\big).
\tag{9}
\]

Consequently

\[
 K_{ij}=E_2[H_iH_j]
       +(d_i\cdot d_j)(a_i\cdot a_j)
       +\delta_{ij}E_1[\operatorname{sech}^4(w_i)Q_i^2].
\tag{10}
\]

Permutation symmetry makes its diagonal and off-diagonal entries constant.
Its symmetric eigenvalue and its double transverse eigenvalue are

\[
\lambda_{\rm sym}=3\|\nabla F\|^2\ge3C_0,
\tag{11}
\]
\[
\lambda_{\rm tr}
=\tfrac12E_2(H_1-H_2)^2
 +\tfrac12\|d_1a_1^T-d_2a_2^T\|_F^2
 +E_1[\operatorname{sech}^4(w_1)Q_1^2].
\tag{12}
\]

The last summand uses the orthogonality of the three actual normalized
inputs; no output or hidden-layer orthogonality has been assumed.

## 3. Exact characterization of possible degeneracy

**Proposition.** At any feature time `s>0`,

\[
 K(s)\text{ is singular}\quad\Longleftrightarrow\quad
 p(s)=0\ \text{and}\ \rho(s)=0.
\tag{13}
\]

If `p!=0`, the three upper features are linearly independent. Indeed their
coefficient matrix is `V=pI+q 11^T`, and `z` has a positive density on the
open cube `(-1/R_Z,1/R_Z)^3`. An almost-sure linear relation among
`tanh(z^Tv_i)` extends by continuity to that cube. Its derivative at zero
gives `V^T t=0`. If `p+3q!=0`, both eigenvalues of `V` are nonzero. If
`p+3q=0`, the null vector must be `t=t_0 1`, and `q!=0`. On the line
`z=(r,0,0)`, the third derivative of the relation is a nonzero multiple of

\[
 t_0\big((p+q)^3+2q^3\big)=-6t_0q^3.
\]

Hence `t_0=0` as well. The upper readout Gram alone is positive definite.

If `p=0`, all upper features coincide:

\[
 H_i=H=\tanh(qS),\qquad S=z_1+z_2+z_3.
\tag{14}
\]

Since `F=E[cH]>0`, necessarily `q!=0`. Equations (3) give `d_i=rho 1`
and hence `delta=0`. If `rho!=0`, then `M^T d_i!=0`: otherwise
`M^T1=0`, and multiplying `v_i=Ma_i=q1` by `1^T` would give `3q=0`.

The active lower Gram is strictly positive definite. To verify this,
the joint law of `(G,zeta)` has positive density on all of `R^6`;
the coordinate maps to `(h,k)` are diffeomorphisms onto `(-1,1)^6`.
The invertible two-coordinate normalization in (1) preserves full-dimensional
support. A nonzero linear combination of `b_1` cannot vanish almost surely.
It follows that `Q_i=b_1^TM^Td_i` is nonzero in lower `L2`.
The factor `sech^4(w_i)` is strictly positive at every finite mark and
feature time. Thus the last term in (12) is strictly positive.

Finally, if `p=rho=0`, then `d_i=Q_i=0`; all hidden gradient blocks in
(9) vanish and the three readout gradients equal `H`. The full kernel is
`E[H^2]11^T`, which has rank one. This proves both directions of (13).

This proposition explicitly distinguishes full tangent positivity from
upper-feature rank. A collapse of the latter alone is not enough to
invalidate the requested perturbation argument.

## 4. Every possible singularity is isolated and quadratic

Suppose `s_0>0` satisfies the right-hand side of (13). Equations (4) give

\[
 w_s(s_0)=M_s(s_0)=0,\qquad c_s(s_0)=H.
\]

Therefore `a_{i,s}=v_{i,s}=H_{i,s}=0` there. Differentiating the actual
upper backward coefficient yields, for every `i`,

\[
 (d_i)_s(s_0)=E_2[zH\operatorname{sech}^2(qS)]
             =b\mathbf1,
\quad
 b=\tfrac13E_2[S\tanh(qS)\operatorname{sech}^2(qS)].
\tag{15}
\]

Permutation invariance gives the second equality. The integrand defining
`b` has the strict sign of `q` whenever `S!=0`. The continuous upper law
has `P(S=0)=0`, and `q!=0`; hence `b!=0`. In particular

\[
 \rho_s(s_0)=b\ne0.
\tag{16}
\]

All differentiations are legitimate on finite feature intervals: the
features, gates, `c`, `M`, and row increments have uniform finite bounds,
and the differentiated gates are bounded. Dominated convergence applies.
The fields and their gradients are continuously differentiable there.

Equation (16) makes `rho` nonzero at every sufficiently nearby time other
than `s_0`. By (13), every full-kernel singularity is isolated. Moreover

\[
 (Q_i)_s(s_0)=b\,b_1^TM^T\mathbf1\ne0
                  \quad\text{in lower }L^2.
\tag{17}
\]

The nonzero assertion uses `M^T1!=0`, proved from `q!=0` above, and the
strict lower Gram. Expanding the three squared norms in (12) around
`s_0` therefore gives

\[
 \lambda_{\rm tr}(s)
 =a_0(s-s_0)^2+o((s-s_0)^2),\qquad a_0>0.
\tag{18}
\]

For clarity, the row contribution to `a_0` alone is
`E_1[sech^4(w_1(s_0))((Q_1)_s(s_0))^2]>0`.

At `s=0` the initialized upper Gram is positive definite, by (2) and
the rank argument above or the supplied candidate. On every compact
feature interval the zero set of `lambda_tr` is closed. An infinite
closed subset of a compact interval has an accumulation point; that
would contradict the isolation just proved. Hence there are only
finitely many singular times on each compact interval.

In particular, for targets `y in (0,Y]` with fixed finite `Y`, the same
feature curve fits at its unique `s_y<=Y/C_0`. All but at most finitely
many such target amplitudes have a positive definite endpoint tangent
Gram. This statement does not identify whether `y=1` is exceptional.

## 5. Exact lower primitive and the unfinished cone argument

Put

\[
 T(x)=x/2+\sinh(2x)/4,\qquad T'(x)=\cosh^2x.
\]

Multiplying the lower equation in (4) by `T'(w_i)` gives
`T(w_i)_s=Q_i/3`. Equations (6),(8), using the actual `M^T`, give

\[
 Q_i-Q_j=\delta\,m\cdot(B_i-B_j).
\]

Thus the following identities are exact for every pair `i,j`:

\[
 T(w_i)-T(w_j)=T(G_i)-T(G_j)+\ell\cdot(B_i-B_j),
 \qquad \ell(0)=0,\quad \ell_s=\delta m/3,
\tag{19}
\]
\[
 m_s=\delta A/3,\qquad
 A=\tfrac12E_1[(B_i-B_j)(\tanh w_i-\tanh w_j)],
 \qquad p=m\cdot A.
\tag{20}
\]

The second formula in (20) follows by swapping coordinates `i,j` in
one expectation. The first follows by taking the diagonal-minus-off-
diagonal block of the complete matrix equation in (4).

These equations retain both lower coordinates, their initialized
correlation, and the common forcing that affects all `T(w_i)` equally.
They do not give a proved invariant positivity cone. In particular,
the second normalized feature is `k-beta h/(v+eta)`; its partial derivative
in `h` at fixed `k` is negative. Also the common lower forcing changes
the weights in the expectation defining `A`. Treating either normalized
feature as coordinatewise increasing, or discarding the common forcing
because it cancels from (19), would leave an unjustified step in a sign
argument for `p`.

The unresolved obligation is precisely to show

\[
 (p(s_*),\rho(s_*))\ne(0,0).
\tag{21}
\]

A proof of `p(s)>0` on the entire finite fitting interval would be
sufficient and stronger than necessary. The identities above neither
prove it nor provide a counterexample. Failure to find such a cone is
not evidence against (21).

## 6. Conditional perturbation bridge

For completeness, (21) would suffice for nonsymmetric input perturbations
with the original initialization, fixed equal masses, and unit labels.
This implication needs no input symmetry after perturbation.

At fixed finite feature dimensions, the map from `(w,c,M)` to the three
gradients is locally Lipschitz in the physical Hilbert metric, on bounded
state balls, and locally Lipschitz in the three normalized inputs. Indeed
`a` differences are bounded by the lower `L2` row difference; upper
preactivation differences are uniformly bounded by the bounded features
times the finite coefficient difference; readout differences use
Cauchy--Schwarz; reverse queries lie in the fixed bounded feature span.
In the lower gradient the reverse query is bounded in supremum norm,
so the lower-gate difference is controlled in `L2`. Input differences
add at most a constant times `||w||_2 max_i|Delta u_i|` to these estimates.
Thus the full kernel and vector field are continuous in this topology.

Assume (21). By (13), choose a small state/input neighborhood of
`(X(s_*),(e_1,e_2,e_3))` on which `K>=kappa I` for some `kappa>0`, and
the derivative `Df` from state to the three predictions has operator norm
at most `L`. For arbitrary data within this neighborhood the exact
physical equations give

\[
 r_t=-\tfrac23Kr,\qquad
 |r(t)|\le |r(0)|e^{-2\kappa t/3},\qquad
 \|X_t\|\le\tfrac{2L}{3}|r(t)|.
\tag{22}
\]

The total future state displacement is therefore at most
`L|r(0)|/kappa`. Start sufficiently close to the endpoint, with this
bound smaller than half the state-neighborhood radius; a first-exit
argument preserves the neighborhood and (22) for all future times.
The physical solution extends because it stays in a bounded Hilbert ball
and its locally Lipschitz vector field has bounded speed there. Its
future length is finite and its limiting residual is zero.

Finally choose one finite reference physical time at which the original
orthogonal solution is sufficiently close to its endpoint and has
sufficiently small residual. Finite-time continuous dependence on the
three input vectors places all sufficiently small nonsymmetric
perturbations in the same basin at that fixed time. Their subsequent
loss decays exponentially, at least at rate `4 kappa/3`.

This proves the bridge **conditional on (21)**. No width approximation,
general-dimensional trained-network limit, or closure-order limit is
inferred. The unit-label endpoint condition itself remains open in this
frozen route.
