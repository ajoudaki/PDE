# An exact relational realization using a finite activation algebra

This is a prompt-scoped theoretical candidate, authored on 2026-10-07. Its
scientific inputs are only the supervisor's supplied compressed equations and
the clarification that their coordinatewise backward gate is intentional even
for a nondiagonal metric. No book, other study, external literature, or numerical
experiment was used. Required mathematical, research-contract, adversarial-audit,
and canonical-notation instructions were read. This is a derived candidate, not
an independent review or promoted result.

The construction below gives an exact autonomous system of scalar similarities,
transfer responses, and residuals. A fixed multiplication tensor supplies the
information that a Gram matrix loses under a nonlinear activation. Its moving
state has at most the original compressed model's number of relevant parameters;
its fixed coefficient storage has a cubic width overhead. It is a genuine
quotient when the data-generated invariant algebras are proper subspaces. In the
generic full-rank case it is an explicit relational chart, not an additional
dimension reduction. No neuron or parameter is called a particle.

## 1. Supplied model and exact scope

Let the training indices be \(a=1,\ldots,m\), with labels \(y_a\). Fix a further
finite set of validation inputs before time zero. Training and validation inputs
together have fixed feature vectors \(v_a\in\mathbb R^d\). Validation labels are
neither provided nor used. All sums driving the evolution below run over the
training set only.

There are \(L\) nonlinear layers of widths \(q_\ell\le q\), with fixed SPD
metrics \(M_\ell\). Set
\(\langle u,v\rangle_{M_\ell}=u^\top M_\ell v\). The compressed model has
moving maps \(A:\mathbb R^d\to\mathbb R^{q_1}\),
\(B_\ell:\mathbb R^{q_{\ell-1}}\to\mathbb R^{q_\ell}\) for
\(\ell\ge2\), a readout \(w\in\mathbb R^{q_L}\), and residual state
\(c\in\mathbb R^m\). Its forward pass is

\[
z_a^{(1)}=Av_a,\qquad
z_a^{(\ell)}=B_\ell h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}).
\]

The activation acts coordinatewise. Analyticity on the supplied strip gives
the required smoothness; this construction does not truncate its power series.
Write

\[
V=\frac1{\sqrt m}[h_1^{(L)},\ldots,h_m^{(L)}],\qquad
\widehat w=w+V(V^\top M_LV)^{-1}
 \left[\frac{y-c}{\sqrt m}-V^\top M_Lw\right],
\qquad f_a=\widehat w^\top M_Lh_a^{(L)}.
\]

Work on any interval on which \(V^\top M_LV\) remains positive definite.
Consequently \(f_a=y_a-c_a\) on training inputs, and the training loss is
\(\mathcal L=m^{-1}\sum_a c_a^2\).

The supplied backward directions are, exactly,

\[
\delta_a^{(L)}=\phi'(z_a^{(L)})\odot\widehat w,\qquad
\delta_a^{(\ell)}=
 \phi'(z_a^{(\ell)})\odot B_{\ell+1}^{*}\delta_a^{(\ell+1)},
\qquad
B_\ell^*=M_{\ell-1}^{-1}B_\ell^\top M_\ell.
\]

For a nondiagonal metric, the coordinatewise gate need not be self-adjoint in
that metric. These are the stipulated update directions, not a claim about the
gradient of the corrected predictor. In particular, no identification of the
supplied \(K\) with a true tangent kernel is needed.

The evolution is

\[
\begin{aligned}
\dot A&=\frac2m\sum_{a=1}^m c_a\delta_a^{(1)}v_a^\top,\\
\dot B_\ell&=\frac2m\sum_{a=1}^m
 c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}M_{\ell-1},\\
\dot w&=\frac2m\sum_{a=1}^m c_a h_a^{(L)},\qquad
\dot c=-\frac2mKc,
\end{aligned}
\]

where

\[
\begin{aligned}
K_{ab}={}&\langle h_a^{(L)},h_b^{(L)}\rangle_{M_L}
 +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle_{M_1}\,v_a^\top v_b\\
&+\sum_{\ell=2}^L
 \langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle_{M_\ell}
 \langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle_{M_{\ell-1}}.
\end{aligned}
\]

Only these equations are assumed. Approximation to a dense system is a separate
imported certificate, discussed at the end.

## 2. Why a Gram matrix alone is insufficient

Already with metric \(I\), three coordinates, and \(\phi=\tanh\), consider

\[
z=(1,-1,0)^\top,\qquad
\widetilde z=(1,1,-2)^\top/\sqrt3,\qquad
\mathbf1=(1,1,1)^\top.
\]

The two pairs \((\mathbf1,z)\) and \((\mathbf1,\widetilde z)\) have the
same Gram matrix: both preactivations have squared norm \(2\) and zero pairing
with \(\mathbf1\). Their activated pairing with the unit differs:

\[
\mathbf1^\top\tanh z=0,\qquad
\mathbf1^\top\tanh\widetilde z
 =2\tanh(1/\sqrt3)-\tanh(2/\sqrt3)>0.
\]

Indeed, with \(t=\tanh(1/\sqrt3)>0\), the latter expression is
\(2t^3/(1+t^2)\). Thus even including the unit vector does not make ordinary
similarities determine the next nonlinear feature. This refutes that particular
Gram-only closure, not all possible relational models. What is missing is the
alignment of multiplication with the feature geometry.

## 3. Constructing semantic landmark functions at time zero

Let \(U_0\) be the span of all the fixed training and validation vectors
\(v_a\), with the Euclidean inner product. Write \(r_0=\dim U_0\).
For each layer, construct the smallest subspace
\(U_\ell\subseteq\mathbb R^{q_\ell}\) with the following properties:

1. \(U_\ell\) contains the coordinatewise unit \(\mathbf1\) and is closed
   under coordinatewise multiplication.
2. \(A(0)U_0\subseteq U_1\) and \(w(0)\in U_L\).
3. For \(\ell\ge2\),
   \(B_\ell(0)U_{\ell-1}\subseteq U_\ell\) and
   \(B_\ell(0)^*U_\ell\subseteq U_{\ell-1}\).

This is a finite constructive definition. Start with the listed seed vectors.
Adjoin products of existing basis vectors and images under the initial forward
and adjoint maps. Replace each growing span by an independent basis, and repeat
until none grows. Every nonterminal sweep adds at least one dimension, so there
are at most \(\sum_\ell q_\ell\) such sweeps. At termination, bilinearity and
linearity extend the tested closure from basis elements to the full spaces.
Conversely, every family satisfying 1–3 contains every vector ever adjoined, so
the terminating family is minimal.

These are functions generated by initial input patterns, initial readout
patterns, their forward and backward transports, and their coactivations.
The construction does not choose hidden units as landmarks. Fix a deterministic
ordering of those operations and orthonormalize the resulting independent words
in the appropriate metric. Let the resulting basis matrices be

\[
E_0^\top E_0=I_{r_0},\qquad
E_\ell^\top M_\ell E_\ell=I_{r_\ell},\qquad
\operatorname{range}(E_\ell)=U_\ell,
\quad r_\ell\le q_\ell.
\]

Each basis element retains its provenance as a linear combination of generated
feature or response words. Orthogonalization improves representation; it does
not turn the words into neuron identifiers. Zero or dependent words are simply
discarded at this initialization stage.

This construction can depend on validation inputs, but not on validation labels
or future trajectories. Its inclusion of validation inputs ensures their future
forward passes are represented. Section 7 proves that they never drive learning.

## 4. The fixed activation algebra

For \(i,j,k=1,\ldots,r_\ell\), store the scalar coefficients

\[
u_i^{(\ell)}=\langle e_i^{(\ell)},\mathbf1\rangle_{M_\ell},\qquad
T_{ijk}^{(\ell)}=
 \langle e_i^{(\ell)},e_j^{(\ell)}\odot e_k^{(\ell)}\rangle_{M_\ell}.
\]

Thus \(T_{ijk}=T_{ikj}\); generally it is not symmetric in the first index
and the other two. Coordinatewise multiplication is commutative and associative,
but an arbitrary SPD metric does not satisfy
\(\langle x\odot y,z\rangle_M=\langle x,y\odot z\rangle_M\).
No Frobenius-algebra or self-adjoint-multiplication assumption is made.

For coefficient vectors \(x,y\in\mathbb R^{r_\ell}\), define

\[
\mathcal P_\ell(x,y)_i=\sum_{j,k}T_{ijk}^{(\ell)}x_jy_k.
\]

Since products remain in \(U_\ell\), this is exactly the coefficient vector
of \((E_\ell x)\odot(E_\ell y)\). In particular
\(\mathcal P_\ell(u^{(\ell)},x)=x\).

To evaluate a nonlinear scalar function \(\psi\), form the multiplication
matrix

\[
\mathsf L_\ell(x)_{ij}=\sum_kT_{ikj}^{(\ell)}x_k,
\qquad
\Psi_\ell(x)=\psi(\mathsf L_\ell(x))u^{(\ell)}.
\]

Here \(\psi(\mathsf L)\) has a finite, explicit meaning. Multiplication by
\(E_\ell x\) on a subalgebra of \(\mathbb R^{q_\ell}\) is annihilated by
the polynomial whose distinct roots are the distinct entries of \(E_\ell x\).
The polynomial has no repeated roots. Therefore \(\mathsf L\) is diagonalizable
over \(\mathbb R\). If its distinct eigenvalues are \(\lambda\), define

\[
\psi(\mathsf L)=
 \sum_{\lambda\in\operatorname{spec}(\mathsf L)}\psi(\lambda)
 \prod_{\substack{\mu\in\operatorname{spec}(\mathsf L)\\\mu\ne\lambda}}
 \frac{\mathsf L-\mu I}{\lambda-\mu}.
\]

The empty product is \(I\). This rule uses a finite matrix spectrum,
polynomial evaluation, and scalar evaluations of the original activation; it
neither reconstructs the moving layer maps nor evolves hidden unit values.
Spectral values can be computed during evaluation but are not persistent
particles or additional dynamical state.

To verify the rule, interpolate \(\psi\) by a polynomial \(p\) on the
finite set of entries of \(E_\ell x\). Closure under multiplication gives
\(p(E_\ell x)=E_\ell p(\mathsf L_\ell(x))u^{(\ell)}\), and interpolation
gives \(p(E_\ell x)=\psi(E_\ell x)\). Hence

\[
E_\ell\Psi_\ell(x)=\psi(E_\ell x).
\]

Use \(\Phi_\ell\) for \(\psi=\phi\) and \(\Phi_\ell'\) for
\(\psi=\phi'\). The prime here means scalar derivative before functional
calculus, not the full Jacobian of \(\Phi_\ell\).

Eigenvalue coincidences cause no mathematical singularity: the distinct-spectrum
formula then uses the merged eigenvalue, and the represented map is the smooth
map \(E_\ell^\top M_\ell\psi(E_\ell x)\). The displayed interpolation
formula can nevertheless be numerically ill-conditioned near collisions. Exact
closure is established here; a uniformly stable numerical implementation of
this formula is not claimed. One may use stable matrix-function evaluation
instead, but its error must be accounted for separately.

## 5. Scalar state, forward evaluation, and evolution

Store fixed input similarities
\(\xi_a=E_0^\top v_a\), and evolve

\[
R_1=E_1^\top M_1AE_0,\qquad
R_\ell=E_\ell^\top M_\ell B_\ell E_{\ell-1}\ (\ell\ge2),\qquad
\rho=E_L^\top M_Lw,\qquad c.
\]

Each entry \(R_{\ell,ij}\) is the signed response pairing between a fixed
target landmark and the image of a fixed source landmark. Each \(\rho_i\)
is a readout–landmark pairing. They are not hidden unit positions, velocities,
or neuron parameters. They do retain transfer-operator information; the
construction makes that information explicit rather than claiming it absent.

From the current state evaluate, for every fixed input,

\[
\zeta_a^{(1)}=R_1\xi_a,\qquad
\zeta_a^{(\ell)}=R_\ell\eta_a^{(\ell-1)},\qquad
\eta_a^{(\ell)}=\Phi_\ell(\zeta_a^{(\ell)}).
\]

Define the training feature matrix in this representation by

\[
C=\frac1{\sqrt m}[\eta_1^{(L)},\ldots,\eta_m^{(L)}],\qquad
\widehat\rho=\rho+C(C^\top C)^{-1}
 \left[\frac{y-c}{\sqrt m}-C^\top\rho\right].
\]

Compute backward responses only for training inputs:

\[
\begin{aligned}
d_a^{(L)}&=\mathcal P_L\bigl(\Phi_L'(\zeta_a^{(L)}),\widehat\rho\bigr),\\
d_a^{(\ell)}&=\mathcal P_\ell\bigl(
 \Phi_\ell'(\zeta_a^{(\ell)}),R_{\ell+1}^\top d_a^{(\ell+1)}\bigr).
\end{aligned}
\]

The transpose represents the Hilbert-space adjoint because the landmark bases
are metric-orthonormal. The multiplication tensor implements the stipulated
coordinate gate. These are distinct operations even though both appear in the
same recursion.

All required similarities are ordinary dot products of these coefficient
vectors. In particular,

\[
\begin{aligned}
K_{ab}={}&\eta_a^{(L)\top}\eta_b^{(L)}
 +(d_a^{(1)\top}d_b^{(1)})(\xi_a^\top\xi_b)\\
&+\sum_{\ell=2}^L(d_a^{(\ell)\top}d_b^{(\ell)})
 (\eta_a^{(\ell-1)\top}\eta_b^{(\ell-1)}).
\end{aligned}
\]

The autonomous equations are

\[
\begin{aligned}
\dot R_1&=\frac2m\sum_{a=1}^m c_a d_a^{(1)}\xi_a^\top,\\
\dot R_\ell&=\frac2m\sum_{a=1}^m
 c_a d_a^{(\ell)}\eta_a^{(\ell-1)\top},\qquad 2\le\ell\le L,\\
\dot\rho&=\frac2m\sum_{a=1}^m c_a\eta_a^{(L)},\qquad
\dot c=-\frac2mKc.
\end{aligned}
\]

The output, including on validation inputs, is
\(f_a=\widehat\rho^\top\eta_a^{(L)}\). On training inputs,
\(\sqrt m C^\top\widehat\rho=y-c\), so the residual identity is exact.

There is no future coefficient, time-indexed forcing, history variable,
trajectory interpolation, or evolving hidden matrix outside this state. The
right-hand side is evaluated by finite algebra operations on fixed tensors and
current scalar state. The equations can restart from any state reached on the
interval where the correction is defined.

## 6. Exactness and the quotient statement

First, a unital subalgebra of \(\mathbb R^{q_\ell}\) is closed under
\(\phi\) and \(\phi'\): the interpolation argument in Section 4 applies
to every vector in that subalgebra.

Next, the reachable subspaces remain invariant. If current forward and backward
vectors lie in their respective \(U_\ell\), a rank-one update
\(\delta h^\top M_{\ell-1}\) maps \(U_{\ell-1}\) into \(U_\ell\).
Its metric adjoint is \(h\delta^\top M_\ell\), which maps \(U_\ell\)
into \(U_{\ell-1}\). It vanishes on the metric-orthogonal complements in
the respective source spaces. The update to \(A\) maps \(U_0\) into
\(U_1\), and its action on \(U_0^\perp\) is zero. The readout update is
in \(U_L\). Initial maps satisfy these invariances by construction.

A noncircular verification is obtained by lifting a solution of the scalar
system to the original variable space:

\[
\begin{aligned}
A(t)&=A(0)+E_1[R_1(t)-R_1(0)]E_0^\top,\\
B_\ell(t)&=B_\ell(0)+E_\ell[R_\ell(t)-R_\ell(0)]
 E_{\ell-1}^\top M_{\ell-1},\\
w(t)&=E_L\rho(t).
\end{aligned}
\]

Induction on the forward layers gives
\(z_a^{(\ell)}=E_\ell\zeta_a^{(\ell)}\) and
\(h_a^{(\ell)}=E_\ell\eta_a^{(\ell)}\). The corrected readout satisfies
\(\widehat w=E_L\widehat\rho\). Since both the initial maps and their
updates preserve the forward and adjoint subspaces,
\(B_\ell^*E_\ell=E_{\ell-1}R_\ell^\top\). Backward induction therefore
gives \(\delta_a^{(\ell)}=E_\ell d_a^{(\ell)}\). Differentiating the
lifting formulas and substituting the scalar equations yields every supplied
map/readout equation, with exactly the original factors and metrics. Dot-product
preservation gives the supplied \(K\) and residual equation.

Conversely, the invariant original evolution has these scalar projections and
obeys these equations. Smoothness of \(\phi\), fixed finite dimensions, and
invertibility of the correction Gram matrix make both vector fields locally
Lipschitz on the stated domain. Local uniqueness therefore identifies the
trajectories for as long as they exist in that domain.

The lifting formulas prove equivalence; they are not used to evaluate the scalar
right-hand side. The original maps can be discarded after initialization of the
fixed coefficients and the scalar state if recovering unobserved map components
is not an output requirement.

Directions orthogonal to the reachable subspaces cannot affect the declared
observables. The quotient removes them. When the subspaces are full, the
transformation is a chart of the original compressed relevant state and there
is no new state compression. The algebra tensor is essential in either case.

## 7. Mechanistic consequences

The elementary learning event has an explicit relational interpretation. For
\(\ell\ge2\),

\[
\dot R_{\ell,ij}
=\frac2m\sum_{a=1}^m c_a
 \langle e_i^{(\ell)},\delta_a^{(\ell)}\rangle_{M_\ell}
 \langle e_j^{(\ell-1)},h_a^{(\ell-1)}\rangle_{M_{\ell-1}}.
\]

A training sample changes a transfer response by the product of its backward
overlap with the receiving landmark, its forward overlap with the sending
landmark, and its residual. Nonlinear interactions enter through the fixed
coactivation multiplication table; metric geometry enters through similarities
and the transpose adjoint. This separates two structures that a Gram-only model
would conflate.

The matrix \(K\) is positive semidefinite, although it is not asserted to be
the tangent kernel of the corrected predictor. Indeed it is the Gram matrix of
the concatenated sample vectors

\[
\left(
\eta_a^{(L)},\quad d_a^{(1)}\otimes\xi_a,\quad
(d_a^{(\ell)}\otimes\eta_a^{(\ell-1)})_{\ell=2}^L
\right).
\]

Consequently
\(d\|c\|^2/dt=-4c^\top Kc/m\le0\). If \(c=0\), all stored-state
derivatives vanish. Neither fact proves convergence to zero residual, global
well-posedness, or dense-model accuracy.

Validation points have no terms in the sums, no backward directions used by the
right-hand side, and no labels in initialization or evaluation. Adding fixed
validation inputs may enlarge the chart but cannot change the original training
trajectory: both charts lift to the same original initial-value problem, whose
locally unique solution is independent of which outputs are observed. This is
the precise sense in which validation is passive.

## 8. Rank changes, costs, and coefficient provenance

The landmark bases are fixed at time zero. Later dependence among training
features, preactivations, or response patterns never requires a basis change or
a division by their rank. Singular \(R_\ell\), zero residuals, repeated
activation values, repeated landmarks, and vanishing gates are allowed. The one
unrepaired singularity is the original readout correction: if \(C^\top C\)
loses rank, both formulations leave their stated domain. Replacing its inverse
by a pseudoinverse without further assumptions changes the supplied model.

The number of moving scalars is

\[
r_1r_0+\sum_{\ell=2}^Lr_\ell r_{\ell-1}+r_L+m.
\]

Fixed algebra tensors and units require
\(\sum_\ell(r_\ell^3+r_\ell)\) scalars. Fixed input coefficients require
\(Nr_0\) scalars for \(N\) declared inputs. Labels require \(m\) scalars.
Basis-provenance records, if retained for interpretation or audit, have additional
polynomial cost and do not contain future trajectories. Raw basis matrices need
not be retained for evolution. The input span has \(r_0\le\min(d,N)\);
input Gram operations can be done using the fixed \(N\times N\) input Gram
matrix and initial compressed input responses.

At fixed depth, storage is \(O(qr_0+Lq^3+Nr_0+m)\), and a straightforward
evaluation has polynomial cost. If scalar activation and dense matrix-function
evaluation are treated as primitives with cubic matrix cost, forward/backward
algebra work is of order \(O(NLq^3)\), the explicit training kernel costs
\(O(m^2Lq+m^2r_0)\), and the readout correction adds ordinary \(m\)-dimensional
linear algebra. Those are arithmetic-operation estimates, not precision-uniform
bit-complexity bounds. Initial algebra generation is a finite polynomial sequence
of products, initial map applications, and rank tests in spaces of dimension at
most \(\sum_\ell q_\ell\). Conditioning can make floating-point rank
decisions and matrix-function evaluation difficult even though the exact
construction is defined.

If the supplied compressed widths are polylogarithmic in ambient width, this
fixed cubic overhead remains polylogarithmic in ambient width, with the declared
sample count, input dimension, depth, metric conditioning, and precision
dependencies kept explicit. This statement adds no bound on those other
quantities.

All fixed coefficients and initial state use only the declared time-zero inputs,
initial compressed maps/readout, known metrics, and training labels/residuals.
Initial backward map applications are applications of the known time-zero
adjoints, not observations from a training trajectory. No coefficient is fitted
to future dense or compressed outputs.

## 9. What this proves, and the remaining implication

The exact claim is now a finite-dimensional theorem under the supplied model and
the correction's invertibility condition: the above algebra-enriched relational
system produces precisely its declared training and validation predictions.
There is no approximation step inside that theorem. It is not a Gram-only closure.

Suppose an independently supplied certificate gives, on an event of probability
at least \(1-p\),

\[
\sup_{0\le t\le T}\max_{a\in\mathcal I}
|f_a^{\mathrm{dense}}(t)-f_a^{\mathrm{compressed}}(t)|\le E(n,q)
\]

for a declared index set \(\mathcal I\), and ensures the compressed solution
exists with invertible correction on that interval. Exact equality of the
compressed and relational predictions gives the identical bound, event,
observable, and time horizon for the relational system. No larger validation
class, longer horizon, stronger norm, or improved probability follows. The
certificate itself was not supplied for verification and is not proved here.

There are two distinct limitations. First, in the full-rank case the relational
transfer table retains the same information as the relevant compressed layer
map. Exact conjugacy alone cannot be sold as further compression or as an
elimination of transfer-operator state. Its added content is the semantic
sample-generated chart and the explicit separation of activation algebra,
metric geometry, and residual-driven transfer writes. If the intended demand
for transparency excludes every evolving transfer table that can encode a layer
map, this construction does not meet that stronger demand.

Second, a stronger reduction to only a small collection of sample similarities,
with no activation algebra or equivalent orientation data, remains unsupported;
Section 2 gives a concrete obstruction to the simplest version. Neither that
counterexample nor this candidate proves a no-go theorem for all richer
relational observables. The weakest external implication for dense prediction is
the imported compressed-model certificate. The weakest additional implication
for a stronger scientific claim is that the generic full-rank transfer chart
provides the intended degree of transparency; this is a criterion of the
research objective, not something established by exact conjugacy.
