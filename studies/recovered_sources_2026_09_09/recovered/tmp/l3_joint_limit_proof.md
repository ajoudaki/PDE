# A joint width/gradient-flow limit for a genuinely nonlinear three-hidden-layer MLP

## 1. The theorem

Fix (p,d<\infty).  Let

\[
 (x_a,y_a)_{a=1}^p\subset \mathbb R^d\times\{-1,1\},
 \qquad \|x_a\|^2=d,
\]

and suppose the (x_a)'s are pairwise distinct.  For width (n), consider

\[
\begin{aligned}
 U_i^a&=w_i^\top x_a,&H_{1,i}^a&=\phi(U_i^a),\\
 S_{2,j}^a&=\sum_iB_{2,ji}H_{1,i}^a,&H_{2,j}^a&=\phi(S_{2,j}^a),\\
 S_{3,k}^a&=\sum_jB_{3,kj}H_{2,j}^a,&H_{3,k}^a&=\phi(S_{3,k}^a),\\
 f_{n,a}&=\sum_kc_kH_{3,k}^a,&
 L_n&=p^{-1}\sum_a(f_{n,a}-y_a)^2,
\end{aligned}
\tag{1.1}
\]

with the fixed, width-independent, analytic non-affine activation

\[
 \phi(z)=\sin z+\cos z.                                      \tag{1.2}
\]

Initialize all displayed entries independently by

\[
 w_i(0)\sim N(0,I_d/d),\qquad
 B_{2,ji}(0),B_{3,kj}(0)\sim N(0,1/n),\qquad
 c_k(0)\sim N(0,n^{-4}).                                    \tag{1.3}
\]

Use exact simultaneous full-batch GD, interpolate linearly at
\(t=k\eta_n\), and take

\[
 \eta_n=\exp(-e^n),\qquad
 \lambda_{w,n}=n/d,qquad
 \lambda_{B_2,n}=\lambda_{B_3,n}=1,qquad
 \lambda_{c,n}=1/n.                                         \tag{1.4}
\]

Thus every raw step tends to zero.  The very small displayed mesh is not a
network scaling: time is still \(t=k\eta_n\), and the limiting vector field
below has nonzero order-one velocities.  Its sole purpose is to make the
last, entirely finite-dimensional, Euler-error estimate automatic.  No
fixed-step large-width theorem is extrapolated to \(e^n\) steps.

**Theorem.**  There is an explicit \(T_0=T_0(p,d)>0\), defined in
(5.25), and a unique deterministic, autonomous, restartable three-population
action-law flow on \([0,T_0]\) such that, along the full sequence \(n\to\infty\),
the exact interpolated GD states converge in probability uniformly on every
\([0,T]\subset[0,T_0]\).  The topology is the current-action topology of
Section 4.  It determines every forward and backward field, both current
middle operators and their adjoints, every empirical Gram, the four NTK
blocks, output, and loss.  Moreover:

1. the empirical path laws of \(U,S_2,S_3\in C([0,T];\mathbb R^p)\)
   converge in \(W_2\);
2. all required velocity energies and kernel blocks converge, and their time
   integrals pass to the limit;
3. for a dataset-dependent \(T_*\in(0,T_0]\), all three hidden marginal
   variances stay finite and positive on \([0,T_*]\), every hidden layer has
   positive integrated velocity and nonzero macroscopic displacement, every
   one of the four parameter blocks has positive integrated NTK activity,
   the nonlinear regression residual is positive at every hidden layer, the
   full NTK matrix is nonconstant, and \(L(T)<L(0)\) for \(0<T\le T_*\).

The middle Gaussian arrays are not represented by an ordinary empirical law.
The limiting state retains their *current actions* on all reachable probes;
it retains neither a finite array nor a history.

## 2. Exact normalized dynamics

Put

\[
 C=nc,\qquad \langle u,v\rangle_n=n^{-1}u^\top v,
 \qquad u\otimes_n v=n^{-1}uv^\top,\qquad \gamma=2/p.
\]

Then (f_a=\langle C,H_3^a\rangle_n).  Define

\[
\begin{aligned}
 e_a&=f_a-y_a,&D_3^a&=C\odot\phi'(S_3^a),\\
 P_2^a&=B_3^\top D_3^a,&D_2^a&=\phi'(S_2^a)\odot P_2^a,\\
 P_1^a&=B_2^\top D_2^a.&
\end{aligned}                                                \tag{2.1}
\]

Direct differentiation of (1.1), including every factor of (n), gives the
exact normalized gradient flow

\[
\boxed{
\begin{aligned}
 \dot w_i&=-{\gamma\over d}\sum_a e_a\phi'(U_i^a)P_{1,i}^a x_a,\\
 \dot B_2&=-\gamma\sum_a e_aD_2^a\otimes_nH_1^a,\\
 \dot B_3&=-\gamma\sum_a e_aD_3^a\otimes_nH_2^a,\\
 \dot C&=-\gamma\sum_a e_aH_3^a.
\end{aligned}}                                               \tag{2.2}
\]

The exact GD recurrence in the normalized variables is precisely forward
Euler for (2.2) with step (eta_n).  If

\[
 G_{ab}=d^{-1}x_a^\top x_b,
\]

then

\[
 \dot U_i^a=-\gamma\sum_b e_bG_{ab}\phi'(U_i^b)P_{1,i}^b.    \tag{2.3}
\]

The four layerwise NTK matrices are exactly

\[
\begin{aligned}
 \Theta^{(1)}_{ab}
 &=G_{ab}\langle\phi'(U^a)P_1^a,\phi'(U^b)P_1^b\rangle_n,\\
 \Theta^{(2)}_{ab}
 &=\langle H_1^a,H_1^b\rangle_n\langle D_2^a,D_2^b\rangle_n,\\
 \Theta^{(3)}_{ab}
 &=\langle H_2^a,H_2^b\rangle_n\langle D_3^a,D_3^b\rangle_n,\\
 \Theta^{(4)}_{ab}&=\langle H_3^a,H_3^b\rangle_n.
\end{aligned}                                                \tag{2.4}
\]

Every block is positive semidefinite.  With
(Theta=\sum_{r=1}^4\Theta^{(r)}),

\[
 \dot f=-\gamma\Theta e,
 \qquad \dot L=-\gamma^2e^\top\Theta e\le0.                 \tag{2.5}
\]

Equations (2.1)--(2.5) also verify that (1.4) is balanced: whenever the
displayed coordinate fields have finite second moments, all four blocks and
all three hidden velocity energies are finite and order one.

## 3. The only external limit theorem, and exactly what is used

We use one external result, only for a **fixed finite computation**.  The
version below is Theorem G.4, with Setup G.2, Definition G.3 and Assumption
L.4, of Yang and Hu, *Tensor Programs IV: Feature Learning in Infinite-Width
Neural Networks*, supplement, pp. 12--21.  We state the part used here.

**Finite-program master theorem.**  A program starts with finitely many
independent matrices whose entries are iid \(N(0,\sigma_A^2/n)\), finitely
many coordinate vectors whose coordinate tuples are iid jointly Gaussian,
and scalar parameters having deterministic limits.  It then performs
finitely many operations of the following forms: multiplication by an
initial matrix or its transpose, coordinatewise pseudo-Lipschitz maps,
and normalized empirical moments followed by continuous scalar maps.  If
all coordinate maps and moment integrands are pseudo-Lipschitz jointly in
their vector and scalar arguments, then, almost surely, every scalar has the
recursively prescribed deterministic limit and, for every finite tuple of
program vectors and every pseudo-Lipschitz test \(q\),

\[
 {1\over n}\sum_{i=1}^n q(V_{1,i},\ldots,V_{r,i})
 \longrightarrow \mathbb E q(Z_{V_1},\ldots,Z_{V_r}).       \tag{3.1}
\]

For a reused multiplication \(AX\), the limit is

\[
 Z_{AX}=\widehat Z_{AX}+
 \sum_{A^TY\ {m earlier}} Z_Y\,
 \mathbb E{\partial Z_X\over\partial\widehat Z_{A^TY}},     \tag{3.2}
\]

where the hatted variables belonging to forward uses of \(A\) are jointly
Gaussian with covariance
\(\mathbb E\widehat Z_{AX}\widehat Z_{AX'}=sigma_A^2
\mathbb E Z_XZ_{X'}\); the hatted variables belonging to transpose uses are
defined analogously and form an independent Gaussian family.  Formula
(3.2) is the theorem's syntactic `ZDot' rule.  The derivative is taken in the
actual program expression, with already-computed moment scalars held fixed.
It therefore remains meaningful at singular Gaussian covariances.  For
nonsmooth maps the cited theorem gives an equivalent Moore--Penrose/Stein
definition; here all maps are smooth, so ordinary differentiation applies.

The hypotheses hold in every finite program below.  Indeed all derivatives
of \(\phi=\sin+\cos\) are bounded; products, the loss derivative, and the
smooth saturations used in the proof are pseudo-Lipschitz.  The vector
\(C(0)=n^{-1}Z_C\) is generated from a standard Gaussian initial vector and
the scalar \(n^{-1}\to0\).  The finitely many first-layer vectors
\((U^a(0))_a\) have iid coordinate tuples \(N(0,G)\), as Setup G.2 permits.

No continuous-time assertion, no rate, and no statement for a number of
program lines increasing with \(n\) is imported.  Those missing conclusions
are proved in Sections 5--7.

### 3.1 The exact finite-mesh Gaussian operator DAG

This subsection records all reused-matrix terms.  It is useful both for
identification and for checking the causal estimate in Section 5.  Fix a
finite serialized Euler mesh \(0=t_0<\cdots<t_N\), and write
\(\delta_k=t_{k+1}-t_k\).  At one time level we compute in the order

\[
 C,U,H_1,S_2,H_2,S_3,H_3,D_3,P_2,D_2,P_1,                 \tag{3.3}
\]

and then update simultaneously.  Put \(A_\ell=B_\ell(0)\).  The learned
matrices satisfy the exact identities

\[
 B_{\ell,k}=A_\ell-gamma\sum_{r<k}\delta_r
       \sum_b e_{r,b}D_{\ell,r}^b\otimes_nH_{\ell-1,r}^b,
 \qquad \ell=2,3.                                         \tag{3.4}
\]

For \(\ell=2,3\), let \(X_{\ell,k}^a=H_{\ell-1,k}^a\) and
\(Y_{\ell,k}^a=D_{\ell,k}^a\).  The master theorem gives hatted Gaussian
families \(\xi_{\ell,k}^a\) and \(\zeta_{\ell,k}^a\) with

\[
\begin{aligned}
 \mathbb E\xi_{\ell,k}^a\xi_{\ell,r}^b
   &=\mathbb E X_{\ell,k}^aX_{\ell,r}^b,\\
 \mathbb E\zeta_{\ell,k}^a\zeta_{\ell,r}^b
   &=\mathbb E Y_{\ell,k}^aY_{\ell,r}^b,
\end{aligned}                                              \tag{3.5}
\]

the two displayed families being independent for each layer and also
independent between layers.  Define, with the precise serialization in
(3.3),

\[
 \alpha_{\ell;k a,r b}
 =\mathbb E{\partial X_{\ell,k}^a\over
                    \partial\zeta_{\ell,r}^b},\qquad r<k,
 \quad
 \beta_{\ell;k a,r b}
 =\mathbb E{\partial Y_{\ell,k}^a\over
                    \partial\xi_{\ell,r}^b},\qquad r\le k. \tag{3.6}
\]

The fixed-mesh limiting fields are exactly

\[
\boxed{
\begin{aligned}
 S_{\ell,k}^a
 &=\xi_{\ell,k}^a
   +\sum_{r<k,b}\alpha_{\ell;k a,r b}Y_{\ell,r}^b
   -\gamma\sum_{r<k,b}\delta_r e_{r,b}Y_{\ell,r}^b
       \mathbb E[X_{\ell,r}^bX_{\ell,k}^a],\\
 P_{\ell-1,k}^a
 &=\zeta_{\ell,k}^a
   +\sum_{r\le k,b}\beta_{\ell;k a,r b}X_{\ell,r}^b
   -\gamma\sum_{r<k,b}\delta_r e_{r,b}X_{\ell,r}^b
       \mathbb E[Y_{\ell,r}^bY_{\ell,k}^a].
\end{aligned}}                                             \tag{3.7}
\]

All other nodes are obtained by applying (2.1)--(2.3) coordinatewise and
replacing normalized moments by expectations.  In particular the present
time response is triangular:

\[
\begin{aligned}
 \beta_{3;k a,k b}
 &=\delta_{ab}\,\mathbb E[C_k\phi''(S_{3,k}^a)],\\
 \beta_{2;k a,k b}
 &=\delta_{ab}\,\mathbb E\!\left[
      \phi''(S_{2,k}^a)P_{2,k}^a
      +\phi'(S_{2,k}^a)^2\beta_{3;k a,k a}
    \right].                                               \tag{3.8}
\end{aligned}
\]

For a saturation \(P\mapsto\tau_R(P)\), (3.8) changes in the second line to
\(\phi''\tau_R(P_2)+\phi'^2\tau_R'(P_2)\beta_3\).  There is no current-time
loop: current \(\beta_3\) is computed first, then \(P_2\), then current
\(\beta_2\), then \(P_1\).  Every other return from a transpose source to a
forward source crosses a strict inequality \(r<k\).  Equations (3.4)--(3.8),
not an independence approximation, are the Gaussian operator DAG used
below.

The master theorem proves (3.7) for each fixed mesh because (3.4) rewrites
every current multiplication using only the two initial Gaussian matrices,
coordinate maps and empirical moments.  It also gives uniform integrability
of every fixed-mesh polynomial moment appearing here by applying (3.1) to a
slightly higher even power.

## 4. The state space is a current action law

We now define the state claimed in the theorem; this prevents a hidden use
of the initial arrays or of the past.  There are three population symbols
\(E_1,E_2,E_3\), each carrying a distinguished constant \(1\), the current
coordinate marks \((U^a)_a\) on \(E_1\), \((S_2^a,C)_a\) on \(E_2\), and
\((S_3^a)_a\) on \(E_3\), and two typed arrows

\[
 B_2:E_1\to E_2,qquad B_3:E_2\to E_3                 \tag{4.1}
\]

together with formal adjoints.  A *current probe* is any finite expression
obtained from those marks by the following grammar:

1. apply a coordinatewise \(C^1\) function with rational coefficients and
   polynomial growth (the countable family is chosen dense on compact sets,
   and explicitly contains \(\phi,\phi',\phi''\));
2. add, multiply, or take a rational linear combination of same-population
   probes;
3. apply \(B_2,B_2^*,B_3,B_3^*\) when the types match;
4. take the inner product \(\mathbb E[XY]\) of same-population probes and use
   the resulting scalar in later coordinate maps.

For every finite same-population tuple, the state records its joint law and
all scalar probes.  Enumerate these records as \(R_m\) and set

\[
 d_{\rm act}(s,s')=
 \sum_{m\ge1}2^{-m}\bigl(1\wedge W_2(R_m(s),R_m(s'))\bigr), \tag{4.2}
\]

using absolute distance for scalar records.  Completion after quotienting
zero-distance states is the current-action space \(\mathfrak S\).  Different
enumerations give the same topology.

This is a law-level state.  To see that its arrows are actual operators,
start with the algebraic span of probes, quotient its null \(L^2\) seminorm,
and complete to Hilbert spaces \(\mathcal H_1,\mathcal H_2,\mathcal H_3\).
For an iid \(N(0,1/n)\) matrix, the elementary \(1/4\)-net argument gives

For completeness, a \(1/4\)-net of the unit sphere has at most \(9^n\)
points and \(\|A\|_{\rm op}\le2\max_{u,v\ {m in\ the\ nets}}|u^TAv|\).
Since each fixed \(u^TAv\) is \(N(0,1/n)\),

\[
 \mathbb P(\|A_\ell\|_{\rm op}>8)
 \le 2\,9^{2n}e^{-8n}.                                    \tag{4.3}
\]

The right side is summable.  Thus \(\|A_\ell\|_{\rm op}\le8\) eventually
almost surely.  From (3.4),

\[
 \|B_\ell(t)\|_{\rm op}
 \le8+\gamma\int_0^t\sum_a|e_a(s)|
       \|D_\ell^a(s)\|_2\|H_{\ell-1}^a(s)\|_2\,ds.       \tag{4.4}
\]

The short-time estimate proved next makes the right side finite uniformly.
Consequently the arrows extend boundedly to the completed Hilbert spaces.
The finite-width identity

\[
 \langle B_\ell X,Y\rangle_n=\langle X,B_\ell^TY\rangle_n
\]

passes to the limit for every pair of probes, so the displayed formal
adjoint is the Hilbert adjoint.  Conversely, (2.1)--(2.3) use only current
marks, these arrows and their adjoints, coordinate maps, and scalar inner
products.  Hence their vector field is a function of the current action law.

The initial arrays and the hatted sources in Section 3 are a construction of
the solution, not coordinates of \(\mathfrak S\).  Uniqueness in Section 5
will imply the semigroup identity \(\Phi_{t+s}=Phi_t\Phi_s\); this proves
autonomy and restartability without retaining a history.

## 5. Uniform short-time response theorem

This is the new estimate needed to pass from fixed programs to a joint
width/time limit.  We give the proof because omitting it would leave exactly
the fixed-step/continuous-time gap.

Write \(b=\sqrt2\), so that \(\|\phi^{(r)}\|_\infty\le b\) for every
\(r\ge0\), and set

\[
 D=2^{40}(1+p+d)^8,\qquad
 c_0=4e^8,\qquad C_0=1200eD.                              \tag{5.1}
\]

The intentionally generous constant \(D\) dominates the following finite
choices at one serialized gate: one of two middle layers, forward or
adjoint orientation, one of at most four product slots, one of \(p\) sample
labels at each of two ends, one of the three update types, and a first-layer
Gram factor \(|G_{ab}|\le1\).  Thus the actual number is at most
\(96(1+p)^2<D\).  Define recursively

\[
\begin{aligned}
 r_3&=D\{c_0+2C_0\},\\
 k_2&=D\{1+r_3+c_0^2\},\\
 r_2&=D\{c_0+k_2+2C_0\},\\
 k_1&=D\{1+k_2+r_2+k_2^2\},\\
 K&=4\max(1,c_0,C_0,r_3,r_2,k_2,k_1),\\
 A&=2^{24}D^2K^2,
\end{aligned}                                             \tag{5.2}
\]

and

\[
 T_0=\min\left\{
 1,{1\over 192eD},{1\over4C_0},{1\over4K},
 {1\over(32A K^2)^{1/3}}
 \right\}.                                                \tag{5.3}
\]

These are finite recursions of five assignments and hence terminate.  They
depend only on \(p,d\) and the displayed activation envelope.

For \(R\ge1\), let \(\tau_R(x)=R\tanh(x/R)\).  The \(R\)-cutoff dynamics
replace \(P_1\) by \(\tau_R(P_1)\) in (2.2)'s first line and replace
\(P_2\) by \(\tau_R(P_2)\) in the definition of \(D_2\).  No forward map is
changed.  Notice

\[
 |\tau_R(x)|\le |x|,\quad |\tau_R'(x)|\le1,\quad
 \sup_{R\ge1,x}|\tau_R^{(m)}(x)|\le 2^m m!\quad(m\ge2).    \tag{5.4}
\]

### Lemma 5.1 (all-source causal estimate)

For every \(T\le T_0\), simultaneously for all finite meshes, all
\(R\in[1,\infty]\), and all widths:

1. the limiting fixed-mesh DAG (3.7) has a unique solution and its response
   rows obey
   \[
   \sup_{k,a}\sum_{r,b}(|\alpha_{\ell;k a,r b}|+
                         |\beta_{\ell;k a,r b}|)\le KT;
                                                               \tag{5.5}
   \]
2. its adjoint fields obey
   \[
   \sup_{k,a,\ell}\|P_{\ell,k}^a\|_{\psi_2}\le KT,
   \quad
   \|X\|_{\psi_2}:=\inf\{s:\mathbb Ee^{X^2/s^2}\le2\};      \tag{5.6}
   \]
3. two limiting cutoff meshes \(\pi,\pi'\), constructed with the same
   hatted Gaussian sources, satisfy for every finite set of probes
   \[
   d_{2,\mathcal P}(Z^{R,\pi},Z^{R,\pi'})
       \le K_{\mathcal P,R}(|\pi|+|\pi'|);                    \tag{5.7}
   \]
4. for the actual finite-width continuous gradient flows \(Z_n\) and their
   cutoff versions \(Z_n^R\), every finite probe set satisfies
   \[
   \lim_{R\to\infty}\limsup_{n\to\infty}
   \mathbb P\!\left(\sup_{t\le T}
      d_{2,\mathcal P}(Z_n(t),Z_n^R(t))>\varepsilon\right)=0; \tag{5.8}
   \]
5. the uncut finite-width adjoint fields have the uniform moment envelope
   \[
   \limsup_{n\to\infty}\sup_{t\le T,a,\ell}
       \|P_{\ell,n}^a(t)\|_{L^q(n^{-1}\sum_i\delta_i\otimes\mathbb P)}
       \le KT\,e^{KTq},\qquad q\ge2.                         \tag{5.9}
   \]

Here \(d_{2,\mathcal P}\) is the sum of normalized \(L^2\) distances of
the listed vector probes and absolute distances of their scalar moments.
The \(\psi_2\) assertion is deliberately only about the limiting DAG:
finite-width reused-matrix coordinates can be products of Gaussians and
need not be subgaussian.  Estimate (5.9), not a false prelimit \(\psi_2\)
claim, is used in (5.8).

#### Proof: causal components

Differentiate a node in (3.3) with respect to one hatted source, keeping
moment scalars fixed as required by (3.2).  Recursively replace every
response coefficient by its defining derivative expectation.  The result
is a finite forest.  A connected component has one distinguished derivative
spine.  Every return to a previously computed forward field crosses an
update with a strictly earlier time, except for the terminating current
chain in (3.8).

The following table exhausts the gates.  The last column counts unbounded
adjoint marks which cannot be absorbed into \(b\).

\[
\begin{array}{c|c|c}
\text{gate}&\text{differentiated factor}&\text{marks}\;P\\ \hline
C\text{-update}&H_3&0\\
U\text{-update}&\phi'(U)P_1&1\;P_1\\
B_3\text{-update}&D_3\otimes H_2&0\\
B_2\text{-update}&\phi'(S_2)P_2\otimes H_1&1\;P_2\\
\mathbb E[D_3D_3]&C^2\phi'\phi'&0\\
\mathbb E[D_2D_2]&\phi'\phi'P_2P_2&2\;P_2\\
\beta_{3;k,k}&C\phi''&0\\
\beta_{2;k,k}&\phi''P_2+\phi'^2\beta_{3;k,k}&1\;P_2.
\end{array}                                                \tag{5.10}
\]

Leibniz' rule for a *first* source derivative chooses one factor, so it does
not split the distinguished spine.  Products of deterministic response
coefficients start separate forest components.  Charging the first mark in
(5.10) to the strict time edge entering its gate and the two covariance
marks to that covariance's time edge shows that a component with \(q\)
strict time edges contains at most

\[
                         2q+1.                              \tag{5.11}
\]

Allowing its terminal fresh Gaussian gives \(2q+2\).  This proves the
incidence assertion by induction on the serialization order: deleting the
latest strict edge deletes the latest update gate and at most its two
charged marks; what remains is either empty or a component with \(q-1\)
edges.  The only uncharged mark is the last line of (5.10), and (3.8) shows
that it terminates.  This also proves that no component is cyclic.

The ordered mesh weight has the exact bound

\[
 \sum_{r_1<\cdots<r_q}\delta_{r_1}\cdots\delta_{r_q}
 \le {T^q\over q!}.                                       \tag{5.12}
\]

At most \(D^{q+1}\) colored component shapes occur.  If every adjoint mark
has \(\psi_2\)-norm at most \(s\le1\), generalized Hölder and the Gaussian
bound \(\|X\|_m\le2s\sqrt m\) give, for \(m\le2q+2\),

\[
 \mathbb E\prod_{j=1}^m(1+|P_j|)
       \le(1+2s\sqrt m)^m.                                \tag{5.13}
\]

Consequently the absolute mass of nontrivial connected components is at
most

\[
 \mathcal C_s(T)=\sum_{q\ge1}{(DT)^q\over q!}
       (1+2s\sqrt{2q+2})^{2q+2}.                           \tag{5.14}
\]

Using \((1+x)^m\le2^{m-1}(1+x^m)\), \(q!\ge(q/e)^q\), and
\(2q+2\le4q\) for \(q\ge1\), one obtains, with
\(\rho=64eDs^2T\),

\[
 \mathcal C_s(T)
 \le 2(e^{4DT}-1)+32s^2T^2{\rho\over(1-\rho)^2}
 \le C_0T                                                     \tag{5.15}
\]

whenever \(48eDT\le1/4\), \(s\le1\), and \(T\le1\).
The constants in (5.1) dominate the elementary right side.  Forests are
sequences of connected components; hence their total dressing factor is
at most \((1-\mathcal C_s(T))^{-1}\le4/3\).

#### Proof: bootstrap and limiting tails

Since \(|H_3|\le b\) and
\(|e_a|\le1+b\mathbb E|C|\), the scalar comparison equation

\[
 {d\over dt}\|C\|_\infty\le2b(1+b\|C\|_\infty),\qquad C(0)=0,
\]

gives \(\|C(t)\|_\infty\le c_0T\).  In (3.7), \(P_2\) is a fresh Gaussian
of standard deviation at most \(b\|C\|_2\), plus bounded \(H_2\)'s times
the \(\ell^1\)-row of \(\beta_3\), plus the learned shift.  The latter is
bounded by \(D T\|C\|_2^2\).  Thus (5.10)--(5.15) give successively

\[
 \|\beta_3\|_{\ell^1}\le r_3T,\quad
 \|P_2\|_{\psi_2}\le k_2T,\quad
 \|\beta_2\|_{\ell^1}\le r_2T,\quad
 \|P_1\|_{\psi_2}\le k_1T.                               \tag{5.16}
\]

The same calculation bounds the two \(\alpha\)-rows by \(KT\).  These
inequalities follow directly from the assignments (5.2); their factor-four
slack makes each estimate improve the bootstrap assumptions
\(s\le KT\) and forest mass \(\le4/3\).  A first-exit argument over the
finite serialization proves (5.5)--(5.6), uniformly in the mesh and in
\(R\).  This is not circular: the assignments are made in the displayed
order \(C,\beta_3,P_2,\beta_2,P_1\), and the only common dressing factor was
already bounded by (5.15).

#### Proof: mesh stability and uniqueness

Put two meshes into one program using the same initial matrices and hatted
sources.  Subtract their integral recursions.  Expanding as above gives the
same forests with one marked root.  A quadrature or piecewise-constant
interpolation defect at that root is bounded by
\(D_R(|\pi|+|\pi'|)\); a state difference at the root is multiplied by the
nontrivial forest mass \(\mathcal C_s(T)\le1/4\).  Therefore

\[
 d_{2,\mathcal P}\le D_{\mathcal P,R}(|\pi|+|\pi'|)
            +{1\over4}d_{2,\mathcal P},
\]

which is (5.7) after division by \(3/4\).  The same expansion with no marked
defect proves uniqueness.  This argument also proves existence by Cauchy
completion of the meshes.  Because the constants depend only on the state
bounds, it applies after a restart; uniqueness then gives the semigroup
identity asserted in Section 4.

#### Proof: the finite-width all-source bound

It remains to justify that the preceding expansion controls the actual
arrays rather than only their limiting DAG.  Standardize every initial
middle entry as \(A_{ij}=g_{ij}/\sqrt n\).  Iterate Duhamel's formula and
serialize every product.  A term with \(q\) time integrals is a colored
causal graph with the same gate table (5.10).  Each matrix half-edge
contributes \(n^{-1/2}\), and each normalized moment or rank-one contraction
contributes \(n^{-1}\).  In the square of a normalized coordinate norm,
expose the Gaussian entries successively.  Gaussian integration by parts
either pairs the exposed half-edge, or differentiates the unique downstream
coordinate expression.  In the second case it follows precisely one of the
derivative-spine arrows in (5.10).  Because moment scalars carry a normalized
sum, a derivative landing on such a scalar loses one free index and
contributes a factor at most \(n^{-1/2}\); discarding that favorable factor
only enlarges the bound.  Deleting the latest time edge again leaves a graph
with at most two fewer unpaired Gaussian half-edges.  Induction therefore
gives at most \(2q+2\) Gaussian source marks in an amplitude and at most
\(4q+4\) in its square.  All powers of \(n\) left after a pairing are
nonpositive: pairing an edge restores at most the index sum whose
\(n^{-1/2}\) normalization it consumes; identifying two formerly free
indices lowers the power.

For clarity, the induction has only the following four index cases:

\[
\begin{array}{c|c|c}
\text{new edge}&\text{new free sums}&\text{net power of }n\\ \hline
A X\text{ or }A^TY&1&n\cdot n^{-1}=1\quad\text{after squaring/pairing}\\
Y\otimes_nX&1&n\cdot n^{-1}=1\\
\mathbb E_n[XY]&1&n\cdot n^{-1}=1\\
\text{derivative of a moment}&0&\le n^{-1/2}.
\end{array}                                                \tag{5.17}
\]

Coordinate maps add no index and all of their derivatives are bounded by
\(b\).  This proves the asserted power count for every graph, including
cross-pairings between two graphs.

For an \(L^r\) estimate, generalized Hölder and
\(\|g\|_m\le2\sqrt m\) bound the source marks of a \(q\)-edge component by

\[
 (2\sqrt{r(2q+2)})^{2q+2}.
\]

Combining this with (5.12), the \(D^{q+1}\) color bound, and
\(q!\ge(q/e)^q\), then summing the exponential series, yields

\[
 \|P_{\ell,n}^a(t)\|_r
 \le KT\sum_{q\ge0}{(KTr)^q\over q!}
 =KT e^{KTr}.                                               \tag{5.18}
\]

The same bound holds for a marked difference forest.  This proves (5.9).
It also proves convergence of the Duhamel series in every fixed \(L^r\), so
the expansion equals the unique finite-dimensional flow.

Finally, for \(r>2\),

\[
 \mathbb E_n\mathbb E[|P|^2\mathbf1_{|P|>R}]
 \le R^{-(r-2)}(KT)^{r}e^{KTr^2}.                          \tag{5.19}
\]

Taking \(r=\max\{3,\lfloor\log R/(2KT)\rfloor\}\) shows that the right
side tends to zero uniformly in \(n,t\).  The difference between the cutoff
and uncut flows is a forest with one root of the form
\(P-\tau_R(P)\); (5.19) bounds that root, and the remaining forest has mass
at most \(4/3\).  This proves (5.8) and completes the proof of Lemma 5.1.

## 6. Construction and joint convergence

We first fix \(R<\infty\).  On the event (4.3), use the finite-width norm

\[
 \|z\|_{n,R}=\sum_a\bigl(
 \|U^a\|_{2,n}+\|S_2^a\|_{2,n}+\|S_3^a\|_{2,n}\bigr)
 +\|C\|_{2,n}+\|B_2\|_{\rm op}+\|B_3\|_{\rm op}.          \tag{6.1}
\]

The cutoff vector field is locally Lipschitz in this norm with a constant
\(L_R=L_R(p,d,T_0)\) independent of \(n\).  Here is the complete estimate.
Composition by \(\phi\) or \(\phi'\) costs at most \(b\); multiplication by
\(\tau_R(P)\) costs at most \(R\); \(\tau_R\) is 1-Lipschitz; multiplication
by \(B_\ell\) costs \(\|B_\ell\|_{\rm op}\); and

\[
 \|u\otimes_n v\|_{\rm op}=\|u\|_{2,n}\|v\|_{2,n}.       \tag{6.2}
\]

Moreover \(C_i(0)=n^{-1}Z_i\), and the coordinate differential inequality
used below (5.15) gives a deterministic uniform bound on \(\|C\|_\infty\)
on the event \(\max_i|Z_i|\le n\).  Applying these five estimates in the
order \(S_3,D_3,P_2,D_2,P_1,U,B_2,B_3,C\) gives

\[
 \|F_R(z)-F_R(\widetilde z)\|_{n,R}
 \le D(1+R)^2(1+\|B_2\|_{\rm op}+\|B_3\|_{\rm op}
                 +\|\widetilde B_2\|_{\rm op}
                 +\|\widetilde B_3\|_{\rm op})^2
       \|z-\widetilde z\|_{n,R}.                           \tag{6.3}
\]

Equation (4.4) closes the operator-norm ball, so the right side is a finite
\(L_R\).  The standard Euler estimate, obtained by integrating
\(z(t+h)-z(t)-hF_R(z(t))\) and applying Gronwall, is consequently

\[
 \sup_{t\le T}\|z_{n,R}^{\delta}(t)-z_{n,R}(t)\|_{n,R}
 \le {M_R\over2L_R}(e^{L_RT}-1)|\delta|,                   \tag{6.4}
\]

where \(M_R=\sup\|DF_R(z)F_R(z)\|_{n,R}\) on the same ball and is also
independent of \(n\).  This is a direct proof of the uniform shadowing
needed here; it is valid only after cutoff, exactly where (6.3) closes.

For fixed \(R,\delta,T\), the Euler path contains finitely many operations,
so Section 3 proves its almost-sure convergence in every finite collection
of action probes.  Let \(n\to\infty\) in (6.4), and then
\(\delta\downarrow0\).  Lemma 5.1(3) identifies the result with the unique
continuous cutoff action flow \(z_R\).  Lemma 5.1(4) and its limiting marked
defect version now let \(R\to\infty\), yielding

\[
 z_n\longrightarrow z
 \quad\hbox{in probability in }C([0,T];\mathfrak S).       \tag{6.5}
\]

To pass from a finite collection of probes to (4.2), first choose \(M\) so
the tail \(\sum_{m>M}2^{-m}<\varepsilon\), apply the preceding argument to
the first \(M\) probes, and then let \(M\to\infty\).  This proves the full
sequence assertion, not merely subsequential convergence.

### 6.1 Path laws and uniform integrability

For any mesh interval \(I\) and any hidden vector path \(Z_i(t)\),

\[
 {1\over n}\sum_i\sup_{s,t\in I}|Z_i(t)-Z_i(s)|^2
 \le |I|\int_I{1\over n}\sum_i|\dot Z_i(r)|^2,dr.         \tag{6.6}
\]

The right side is a current probe controlled by (5.9); the same bound with
a fourth power follows from its \(q=4\) case.  Mesh-point convergence,
(6.6), and the fourth-moment bound give tightness and uniform square
integrability in \(C([0,T];\mathbb R^p)\).  Therefore the three empirical
path laws converge in \(W_2\).  The velocity squares, all Gram entries,
(2.4), output and loss are finite products of controlled probes.  Hölder
with (5.9) gives uniform integrability, so they converge uniformly on compact
time intervals and their time integrals converge as well.

### 6.2 Exact GD, rather than finite-width gradient flow

For completeness we now use the explicit small mesh in (1.4).  Let
\(\mathcal E_n\) be the event that every standardized Gaussian used at
initialization has absolute value at most \(n\).  A union bound over fewer
than \(3n^2+nd\) variables gives \(\mathbb P(\mathcal E_n^c)\to0\).
On \(\mathcal E_n\), boundedness of \(\phi,\phi',\phi''\) and direct use of
(2.1)--(2.3) give, for \(t\le T_0\),

\[
 \max_i|C_i(t)|\le e^{4T_0}(1+n^{-1}\max|Z_C|),\quad
 \max|B_\ell(t)|+\max|w(t)|+\max|P_\ell(t)|\le n^{10},     \tag{6.7}
\]

for all sufficiently large \(n\).  The same inequalities hold for Euler
iterates while they remain within distance one of the flow.  To verify the
second bound, successively use
\(|P_2|\le n\max|B_3|,b\max|C|\),
\(|\dot B_3|\le D\max|C|/n\),
\(|\dot B_2|\le D\max|P_2|/n\),
\(|P_1|\le nb\max|B_2|\max|P_2|\), and
\(|\dot w|\le D\max|P_1|\); starting from maxima at most \(n\), every
right side is below \(n^{10}\).  This intentionally crude induction closes
on the fixed interval.

On this box the Jacobian norm of the finite-dimensional vector field and
the norm of \(DF_nF_n\) are at most \(n^{40}\): each derivative contains at
most four sums of length \(n\), four bounded activation derivatives, and
four factors bounded by \(n^{10}\).  The elementary Euler/Gronwall estimate
therefore gives

\[
 \sup_{t\le T_0}\|z_n^{\rm GD}(t)-z_n^{\rm GF}(t)\|_{n,R}
 \le \eta_n n^{40}T_0e^{n^{40}T_0}.                        \tag{6.8}
\]

If necessary replace the exponent \(40\) by any larger fixed integer; the
displayed right side still tends to zero because
\(\eta_n=\exp(-e^n)\).  The bootstrap assumption that the iterates stay in
the unit enlargement follows from the same bound.  Combining (6.8) with
(6.5) proves the asserted joint limit for exact interpolated GD.  Notice why
the mesh was chosen explicitly: this step is finite-dimensional and does
not invoke a tensor program of growing length.

## 7. Explicit initial Gaussian geometry

This section verifies all nondegeneracy assertions directly.  It uses only
the continuous limiting DAG constructed above; every coefficient is a
finite Gaussian integral.

For standard jointly Gaussian \((X,Y)\) with correlation \(\rho\), elementary
characteristic-function differentiation gives

\[
 \mathbb E[\phi(X)\phi(Y)]
 =\mathbb E[\phi'(X)\phi'(Y)]=e^{\rho-1}.                  \tag{7.1}
\]

Let \(Z_1\sim N(0,G)\), and recursively define

\[
 Q_1=e^{\circ(G-\mathbf1)},\quad Z_2\sim N(0,Q_1),\quad
 Q_2=e^{\circ(Q_1-\mathbf1)},\quad Z_3\sim N(0,Q_2),\quad
 Q_3=e^{\circ(Q_2-\mathbf1)},                              \tag{7.2}
\]

where exponentiation is entrywise.  Then \(Z_1,Z_2,Z_3\) are the initial
preactivation laws and \(Q_r\) are the activation Gram matrices.

All three \(Q_r\) are positive definite.  Indeed
\(e^{x_a^Tx_b/d}=\sum_{m\ge0}(x_a^Tx_b/d)^m/m!\).  If a
coefficient vector annihilated this Gram matrix, it would annihilate every
tensor feature \(x\mapsto x^{\otimes m}\).  For each fixed point \(x_j\),

\[
 P_j(x)=\prod_{k\ne j}{(x-x_k)^T(x_j-x_k)\over\|x_j-x_k\|^2}
\]

vanishes on all \(x_k\), \(k\ne j\), and equals one at \(x_j\); hence every
coefficient vanishes.  Thus \(Q_1\succ0\).  Applying the same argument to
a Gram realization of \(Q_1\), whose vectors are distinct because
\(Q_1\succ0\), proves \(Q_2,Q_3\succ0\).

Put \(a=\gamma y\), and, with \(H_r=\phi(Z_r)\), define

\[
\begin{aligned}
 C_1&=\sum_\alpha a_\alpha H_3^\alpha,\\
 A_3^\mu&=C_1\phi'(Z_3^\mu),
 &R_3^{\mu\nu}&=\mathbb E[A_3^\mu A_3^\nu],\\
 J_3^{\mu\alpha}
 &=a_\alpha Q_3^{\mu\alpha}
   -\delta_{\mu\alpha}(Q_3a)_\mu.                         \tag{7.3}
\end{aligned}
\]

Let \(\Xi_3\sim N(0,R_3)\) be independent of \(Z_2\), and set

\[
\begin{aligned}
 L_2^\mu&=\Xi_3^\mu+\sum_\alpha J_3^{\mu\alpha}H_2^\alpha,\\
 A_2^\mu&=\phi'(Z_2^\mu)L_2^\mu,
 &R_2^{\mu\nu}&=\mathbb E[A_2^\mu A_2^\nu],\\
 J_2^{\mu\alpha}
 &=J_3^{\mu\alpha}Q_2^{\mu\alpha}
   -\delta_{\mu\alpha}\sum_\beta
      J_3^{\mu\beta}Q_2^{\mu\beta}.                      \tag{7.4}
\end{aligned}
\]

Finally let \(\Xi_2\sim N(0,R_2)\) be independent of \(Z_1\), and put

\[
\begin{aligned}
 L_1^\mu&=\Xi_2^\mu+\sum_\alpha J_2^{\mu\alpha}H_1^\alpha,\\
 A_1^\mu&=\phi'(Z_1^\mu)L_1^\mu,
 &R_1^{\mu\nu}&=\mathbb E[A_1^\mu A_1^\nu].              \tag{7.5}
\end{aligned}
\]

These formulas follow node by node from (3.2).  For example,

\[
 \mathbb E{\partial A_3^\mu\over\partial Z_3^\alpha}
 =a_\alpha\mathbb E[\phi'(Z_3^\alpha)\phi'(Z_3^\mu)]
  +\delta_{\mu\alpha}\mathbb E[C_1\phi''(Z_3^\mu)]
 =J_3^{\mu\alpha},                                       \tag{7.6}
\]

because \(\phi''=-\phi\); differentiating (7.4) gives the displayed
formula for \(J_2\).  Thus no gradient-independence assumption has entered.

The matrices \(R_1,R_2,R_3\) are positive definite.  If \(v\ne0\),

\[
 v^TR_3v=\mathbb E\left[(a^T\phi(Z_3))
                         (v^T\phi'(Z_3))\right]^2>0.       \tag{7.7}
\]

The inequality holds because \(Q_2\succ0\) gives a full-support density,
both factors are nonzero real-analytic functions, and the product of two
nonzero analytic functions on connected \(\mathbb R^p\) cannot vanish on a
set of full measure.  Independence of \(\Xi_3,Z_2\) gives

\[
 R_2=Q_2\circ R_3+
 \mathbb E[(\phi'(Z_2)\odot J_3\phi(Z_2))
            (\phi'(Z_2)\odot J_3\phi(Z_2))^T]\succ0,       \tag{7.8}
\]

and similarly \(R_1\succeq Q_1\circ R_2\succ0\).  The Schur product of
two positive-definite matrices is positive definite.  Also
\(G\circ R_1\succ0\), even if \(G\) is singular: realize \(G_{ij}=u_i^Tu_j\)
with \(u_i\ne0\), and realize \(R_{1,ij}=v_i^Tv_j\) with linearly
independent \(v_i\); then \(u_i\otimes v_i\) are linearly independent.

Every moment above is an explicit finite Gaussian integral.  More
literally, for \(Z\sim N(0,Q)\),

\[
\begin{aligned}
 &\mathbb E\prod_{j=1}^m\phi^{(r_j)}(Z_{i_j})\\
 &\quad=2^{-m/2}\sum_{\epsilon\in\{-1,1\}^m}
 \cos\!\left(\sum_j\epsilon_j\theta_{r_j}\right)
 \exp\!\left[-{1\over2}\sum_{j,k}\epsilon_j\epsilon_kQ_{i_ji_k}\right],
 \qquad \theta_r=-{\pi\over4}+{r\pi\over2}.              \tag{7.9}
\end{aligned}
\]

### 7.1 Initial jets and strict feature motion

Taylor expansion of the continuous DAG, justified by the dominated response
bounds, gives in \(L^2\)

\[
\begin{aligned}
 C(t)&=tC_1+O(t^2),&D_3(t)&=tA_3+O(t^2),\\
 P_2(t)&=tL_2+O(t^2),&D_2(t)&=tA_2+O(t^2),\\
 P_1(t)&=tL_1+O(t^2).                                    \tag{7.10}
\end{aligned}
\]

Consequently

\[
\begin{aligned}
 \Theta^{(1)}(t)&=t^2(G\circ R_1)+O(t^3),\\
 \Theta^{(2)}(t)&=t^2(Q_1\circ R_2)+O(t^3),\\
 \Theta^{(3)}(t)&=t^2(Q_2\circ R_3)+O(t^3),\\
 \Theta^{(4)}(0)&=Q_3.                                  \tag{7.11}
\end{aligned}
\]

Every leading matrix in (7.11) is positive definite.  Thus each parameter
block has positive finite integrated activity on every sufficiently short
nonzero interval.

There is feature motion in every hidden layer, not merely parameter motion.
Let

\[
 Y=\sum_a y_aH_3^a,\qquad \mathcal S={1\over2}\mathbb E Y^2.
\]

At initialization \(C=0,e=-y\).  From (2.2),

\[
 \dot\theta_{\rm hid}(t)=\gamma^2t\,\nabla_{\rm hid}\mathcal S+O(t^2).
                                                               \tag{7.12}
\]

For the first \(r\) hidden parameter blocks, the chain rule gives

\[
 \left\langle\nabla_{Z_r}\mathcal S,\ddot Z_r(0)\right\rangle
 =\gamma^2\sum_{j\le r}\|\nabla_{\theta_j}\mathcal S\|^2>0. \tag{7.13}
\]

Strict positivity follows from (7.11): the summands are label quadratic
forms of \(G\circ R_1,Q_1\circ R_2,Q_2\circ R_3\).  Hence
\(\ddot Z_r(0)\ne0\), and

\[
 \dot Z_r(t)=t\ddot Z_r(0)+O(t^2),\qquad
 Z_r(t)-Z_r(0)={t^2\over2}\ddot Z_r(0)+O(t^3).             \tag{7.14}
\]

This proves positive integrated velocity and nonzero displacement in all
three layers.

### 7.2 Nonlinearity, kernel movement, and loss decrease

Every initial marginal is standard normal.  If \(G_0\sim N(0,1)\), then

\[
 \mathbb E\phi(G_0)=e^{-1/2},\quad
 \mathbb E\phi(G_0)^2=1,\quad
 \mathbb E[G_0\phi(G_0)]=e^{-1/2}.
\]

Therefore

\[
 \inf_{a,b}\mathbb E|\phi(G_0)-aG_0-b|^2=1-{2\over e}>0.  \tag{7.15}
\]

Variance and the five regression moments are continuous under path-\(W_2\)
convergence because \(\phi\) is bounded and Lipschitz.  They remain positive
on a dataset-dependent \([0,T_*]\subset[0,T_0]\), proving survival of
nonlinearity and finite nondegenerate hidden marginals.

Put

\[
 M=(G\circ R_1)+(Q_1\circ R_2)+(Q_2\circ R_3),\qquad
 A_*=y^TMy>0.                                             \tag{7.16}
\]

The hidden blocks give
\(y^T(\Theta^{(1)}+\Theta^{(2)}+\Theta^{(3)})y=A_*t^2+O(t^3)\).
Since (7.12) moves the feature Gram in its own gradient direction, one more
application of the chain rule gives

\[
 y^T\Theta^{(4)}(t)y=y^TQ_3y+A_*t^2+O(t^3).               \tag{7.17}
\]

Thus \(y^T\Theta(t)y=y^TQ_3y+2A_*t^2+O(t^3)\), so the full kernel is not
constant.  Finally \(f(0)=0\), and (2.5) gives

\[
 \dot L(0)=-\gamma^2y^TQ_3y<0.                            \tag{7.18}
\]

After decreasing \(T_*\) if necessary, \(L(T)<L(0)\) for every
\(0<T\le T_*\).  This verifies every assertion in the theorem.
