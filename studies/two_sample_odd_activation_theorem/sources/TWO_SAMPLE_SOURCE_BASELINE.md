# Two-sample raw source system and a conditional affine response bound

Status: the fixed-mesh identification below is proved for the main route's
nonlinear-part clipped programs and for the uncut affine program. The affine
response estimate is proved conditional only on the explicitly specified
uniform primal bound. This note does not prove that primal bound, a
nonlinear perturbation theorem, or a reduction of two-sample physical
gradient flow to a scalar feature clock.

The concrete baseline conclusion is (26)--(28): all four source-derivative
rows entering the two-sample analogues of the one-sample `a,b` coefficients
have explicit mesh-uniform bounds on any fixed feature interval for which
the affine primal bound holds. Single past-source entries are also bounded
by a constant times the step at the source time. The result includes
arbitrary labels and rho = -1.

Dependencies inspected for this calculation:

- `/tmp/l3-two-sample-Un7kw9/CONTRACT.md`;
- `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`,
  especially lines 211--455 (finite Gaussian conditioning, both matrices
  and orientations, formal derivatives, singular queries), and its
  following common-action construction;
- `/tmp/l3-activation-design-oaGjWO/READ_ME_FIRST.md`,
  `OFFSET_ARCTAN_GLOBAL_THEOREM.md`, and
  `OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md` (the one-sample conventions and
  the distinction between a response lemma and a full flow theorem).

The solve-math-rigorously skill was read in full. No simulation, agent,
activation search, or repository/source modification is used here.

The proof first specifies the raw two-sample program and its Gaussian
representation. It then proves a dimension-independent affine stability
estimate. An independent Gaussian probe, inserted at intermediate matrix
answers, identifies a signed formal derivative row by a finite-difference
identity. Choosing its signs yields the required absolute row bounds.

## 1. Raw coordinates, labels, and the finite program

Write

\[
 c_a=y_a/2,\qquad
 R_x=(\rho_{ab})_{a,b=1}^2=
 \begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad -1\le\rho<1.
\]

Thus \(\sum_a|c_a|=1\) and
\(\sum_b|c_b\rho_{ab}|\le1\). Use a positive mesh
\(0=s_0<\cdots<s_N\le S\), with
\(h_j=s_{j+1}-s_j\). Equal steps give \(h_j=\Delta\).
The symbols \(W_{2,j},W_{3,j},C_j\) denote the two hidden matrices and
the rescaled readout. A finite rank-one operator is
\(u\otimes_n v=uv^T/n\), and \(\langle u,v\rangle_n=u^Tv/n\).

At initialization, \(W_{2,0},W_{3,0}\) are the two independent Gaussian
matrices with entry variance \(1/n\), independent of the first-layer
root. A first-layer neuron has
\(w_0\sim N(0,I_d/d)\) and
\(Z^{(1)}_{0,a}=w_0\cdot x_a\), so its two coordinates have covariance
\(R_x\). The contract's readout initialization has normalized norm
\(O_{\mathbb P}(n^{-1})\) and population limit zero. Initially take
\(C_0=0\) in the displayed population/source programs; the small finite
readout is treated below.

The uncut forward and backward calls are

\[
 H^{(1)}_{j,a}=\phi(Z^{(1)}_{j,a}),\quad
 Z^{(2)}_{j,a}=W_{2,j}H^{(1)}_{j,a},\quad
 H^{(2)}_{j,a}=\phi(Z^{(2)}_{j,a}),
\]
\[
 Z^{(3)}_{j,a}=W_{3,j}H^{(2)}_{j,a},\quad
 H^{(3)}_{j,a}=\phi(Z^{(3)}_{j,a}),\quad
 \delta^{(3)}_{j,a}=C_j\phi'(Z^{(3)}_{j,a}),
\]
\[
 q^{(2)}_{j,a}=W_{3,j}^T\delta^{(3)}_{j,a},\quad
 \delta^{(2)}_{j,a}=\phi'(Z^{(2)}_{j,a})q^{(2)}_{j,a},\quad
 q^{(1)}_{j,a}=W_{2,j}^T\delta^{(2)}_{j,a},\quad
 \delta^{(1)}_{j,a}=\phi'(Z^{(1)}_{j,a})q^{(1)}_{j,a}.
\]

Products within a vector/population are coordinatewise. The requested
label-directed feature Euler updates are exactly

\[
 Z^{(1)}_{j+1,a}=Z^{(1)}_{j,a}
       +h_j\sum_b c_b\rho_{ab}\delta^{(1)}_{j,b},
\tag{1}
\]
\[
 W_{\ell,j+1}=W_{\ell,j}
       +h_j\sum_b c_b\delta^{(\ell)}_{j,b}
                              \otimes_n H^{(\ell-1)}_{j,b},
 \quad \ell=2,3,
\]
\[
 C_{j+1}=C_j+h_j\sum_b c_b H^{(3)}_{j,b}.
\tag{2}
\]

Equivalently the first field updates by
\(w_{j+1}=w_j+h_j\sum_b c_b\delta^{(1)}_{j,b}x_b/d\).
Taking its inner product with \(x_a\) gives (1), including the factor
\(1/d\) in the contract. No scalar change of first-layer coordinates is
made. In particular, two separate applications of the one-sample
transformation would not give (1).

For \(\rho=-1\), \(x_2=-x_1\), and (1) preserves
\(Z^{(1)}_{j,2}=-Z^{(1)}_{j,1}\). Everything below uses \(R_x\) directly;
there is no division by \(1+\rho\), \(1-\rho\), or \(\det R_x\).

These are the feature equations with coefficients \(c_a=y_a/2\).
The contract's physical equations instead have coefficients
\(-r_a=y_a-f_a\). For the uncut system, adjunction and the raw metric
give

\[
 \frac{df_a}{ds}=\sum_b c_b K_{ab},\qquad
 K_{ab}=\sum_{\ell=1}^4K^{(\ell)}_{ab},
\]
\[
 K^{(1)}_{ab}=\rho_{ab}\,\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b],
 \quad
 K^{(2)}_{ab}=\mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]
                     \mathbb E_1[H^{(1)}_aH^{(1)}_b],
\]
\[
 K^{(3)}_{ab}=\mathbb E_3[\delta^{(3)}_a\delta^{(3)}_b]
                     \mathbb E_2[H^{(2)}_aH^{(2)}_b],\qquad
 K^{(4)}_{ab}=\mathbb E_3[H^{(3)}_aH^{(3)}_b].
\tag{3}
\]

For example, differentiating \(\mathbb E_3[C H^{(3)}_a]\), then
substituting each forward derivative and moving each matrix through its
inner product, gives successively the four terms in (3). The first-layer
term is \(\sum_b c_b\rho_{ab}\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b]\)
by (1). Thus the off-diagonal blocks have the stated raw normalization.
A single physical clock would require the physical coefficient vector
to be proportional to \((c_1,c_2)\) along the trajectory; this note makes
no such additional assertion.

## 2. The main route's nonlinear-part clips in raw coordinates

Use precisely the activation and backward map specified by main:

\[
 \phi_e(z)=1+z+e\arctan z,\qquad
 \mathcal D_R(z,q)=q+e g(z)\tau_R(q),\qquad
 g(z)=\frac1{1+z^2},\quad e\ge0.
\]

Here \(\tau_R\) is a smooth clip, \(|\tau_R'|\le1\),
\(|\tau_R(q)|\le\min\{|q|,2R\}\), equal to the identity on
\([-R,R]\). The forward activation is always \(\phi_e\), with no clip.
Replace only the backward coordinate maps by

\[
 \delta^{(3)}_{j,a}=\mathcal D_R(Z^{(3)}_{j,a},C_j),\qquad
 \delta^{(2)}_{j,a}=\mathcal D_R(Z^{(2)}_{j,a},q^{(2)}_{j,a}),\qquad
 \delta^{(1)}_{j,a}=\mathcal D_R(Z^{(1)}_{j,a},q^{(1)}_{j,a}).
\tag{4}
\]

All linear backward terms remain intact. At \(e=0\), (4) is the exact
uncut affine backward calculation at every clipping level. With
\(\tau_R(q)=q\), (4) becomes the uncut gate
\(\phi_e'(z)q\).

For fixed \(R\), the partial derivatives are

\[
 \partial_z\mathcal D_R(z,q)=e g'(z)\tau_R(q),\qquad
 \partial_q\mathcal D_R(z,q)=1+e g(z)\tau_R'(q).
\]

Since \(|g'|\le1\), their absolute values are at most \(2eR\) and
\(1+e\). Thus this coordinate map is globally Lipschitz. In the raw
first-layer update the uncontrolled uncut multiplier would be
\(e g'(Z^{(1)})q^{(1)}\). It is the nonlinear part involving
\(q^{(1)}\) that must additionally be clipped, alongside the part
involving \(q^{(2)}\) in the middle layer. At the top the analogous
multiplier is \(e g'(Z^{(3)})C\); the top instance of (4) clips this
nonlinear readout contribution too. An \(L^2\) primal bound on a
multiplier alone does not bound its multiplication operator on \(L^2\).
This explains all three cap locations without imposing a cap on any
linear term or on the forward activation.

Both \(\phi_e\) and (4) are continuously differentiable globally
Lipschitz coordinate instructions with bounded first derivatives at
fixed \(R,e\). On bounded operator and vector-norm sets,
matrix actions and the rank-one updates are locally Lipschitz, since

\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
 \le\|u-\widetilde u\|_2\|v\|_2
        +\|\widetilde u\|_2\|v-\widetilde v\|_2.
\]

This supplies the local Lipschitz flow/Euler comparison on such sets.
It does not by itself assert global boundedness for an unbounded
activation, or cutoff removal for a nonlinear model.

## 3. Two-sample source representation at a fixed mesh

Index every Gaussian source by both time and sample. There are four
mutually independent centered Gaussian groups

\[
 \xi^{(2)}=(\xi^{(2)}_{j,a}),\quad
 \xi^{(3)}=(\xi^{(3)}_{j,a}),\quad
 \zeta^{(1)}=(\zeta^{(1)}_{j,a}),\quad
 \zeta^{(2)}=(\zeta^{(2)}_{j,a}),
\]

independent also of the first-layer Gaussian pair. The pair belongs to
population 1, \((\xi^{(2)},\zeta^{(2)})\) to population 2, and
\(\xi^{(3)}\) to population 3; \(\zeta^{(1)}\) belongs to population 1.
Separate populations have no paired neuron coordinates. For \(\ell=2,3\),

\[
 \mathbb E[\xi^{(\ell)}_{j,a}\xi^{(\ell)}_{v,b}]
    =\mathbb E_{\ell-1}[H^{(\ell-1)}_{j,a}H^{(\ell-1)}_{v,b}],
\]
\[
 \mathbb E[\zeta^{(\ell-1)}_{j,a}\zeta^{(\ell-1)}_{v,b}]
    =\mathbb E_\ell[\delta^{(\ell)}_{j,a}\delta^{(\ell)}_{v,b}].
\tag{5}
\]

These are full second moments of the matrix inputs, including means and
all cross-sample terms. They can be singular.

The raw bottom recursion is

\[
 Z^{(1)}_{k,a}=Z^{(1)}_{0,a}
   +\sum_{j<k}h_j\sum_b c_b\rho_{ab}
       \mathcal D_R(Z^{(1)}_{j,b},q^{(1)}_{j,b}).
\tag{6}
\]

For \(\ell=2,3\), define the deterministic two-sample coefficient arrays

\[
 A^{(\ell)}_{ka,jb}
   =\mathbb E_{\ell-1}
       \frac{\partial H^{(\ell-1)}_{k,a}}
            {\partial\zeta^{(\ell-1)}_{j,b}}
       +h_j c_b\,
          \mathbb E_{\ell-1}[H^{(\ell-1)}_{k,a}H^{(\ell-1)}_{j,b}],
 \quad j<k,
\tag{7}
\]
\[
 D^{(\ell)}_{ka,jb}
   =\mathbb E_\ell
       \frac{\partial\delta^{(\ell)}_{k,a}}
            {\partial\xi^{(\ell)}_{j,b}}
     +\mathbf1_{j<k}h_j c_b\,
          \mathbb E_\ell[\delta^{(\ell)}_{k,a}\delta^{(\ell)}_{j,b}],
 \quad j\le k.
\tag{8}
\]

We use \(D\) for the coefficient called `b` in the one-sample proof,
to reserve \(B\) for the primal bound below. The complete scalar equations
are

\[
 Z^{(\ell)}_{k,a}=\xi^{(\ell)}_{k,a}
       +\sum_{j<k}\sum_b A^{(\ell)}_{ka,jb}\delta^{(\ell)}_{j,b},
\]
\[
 q^{(\ell-1)}_{k,a}=\zeta^{(\ell-1)}_{k,a}
       +\sum_{j\le k}\sum_b D^{(\ell)}_{ka,jb}H^{(\ell-1)}_{j,b},
 \qquad \ell=2,3,
\tag{9}
\]

together with \(H^{(\ell)}=\phi_e(Z^{(\ell)})\), (4), (6), and

\[
 C_k=\sum_{j<k}h_j\sum_b c_bH^{(3)}_{j,b}.
\tag{10}
\]

Every derivative in (7)--(8) is the derivative of the explicit finite
scalar expression, holding all deterministic coefficients and covariance
parameters fixed. A source coordinate has its own formal argument even
when its Gaussian law equals another coordinate or is identically zero.
No derivative of a covariance square root is taken. Notice that the
response parts of (7)--(8) have no extra factor \(c_b\); label factors
already enter their derivative paths through (6) and (10). Only the
learned-rank additions have the explicit factor \(h_jc_b\).

Here is the precise extension of the finite-program dependency. Unroll
both trained matrices into their independent initial matrices and the
rank-one sums in (2). The extra forward term is

\[
 \sum_{j<k,b}h_jc_b\delta^{(\ell)}_{j,b}
                 \langle H^{(\ell-1)}_{j,b},H^{(\ell-1)}_{k,a}\rangle_n,
\]

and the extra transpose term is

\[
 \sum_{j<k,b}h_jc_bH^{(\ell-1)}_{j,b}
                 \langle\delta^{(\ell)}_{j,b},\delta^{(\ell)}_{k,a}\rangle_n.
\]

For each initial matrix, the Gaussian conditioning rule of the dependency
states that an answer to \(Wh\) has limiting form

\[
 \xi_h+\sum_{j,b}u_{j,b}\,
                     \mathbb E\partial_{\zeta_{j,b}}h,
\tag{11}
\]

where \(u_{j,b}\) are its previously queried transpose inputs and
\(\operatorname{Cov}(\zeta)=\mathbb E[uu^T]\). The hypotheses there are a
fixed finite program, iid root tuples independent of the Gaussian
matrices with finite second moments, and globally Lipschitz continuously
differentiable coordinate instructions with bounded first derivatives.
They hold for (4). Multiple sample slots just add finitely many matrix
queries. Both matrices, both orientations, and the joint first-layer root
are retained. Equation (11) follows there by conditioning on both
orientations, projecting away old forward inputs, and using Gaussian
integration by parts against the old transpose-source group. Interleaving
the other independent matrix does not discard any derivative path.

Freeze the finitely many learned contractions at the expectations
constructed causally by (5)--(10). Applying (11) to that program and then
adding its learned terms gives (7)--(9). Each frozen contraction concerns
nodes already available. Fixed-step empirical convergence of these nodes
makes the actual contraction errors tend to zero. The rank-one norm
inequality and a finite induction through the coordinate and matrix
instructions then transfer the same joint empirical \(W_2\) limit to
the actual feedback program.

The chronological order at a time is: both layer-2 forward queries, both
layer-3 forward queries, both layer-3 transpose queries, both layer-2
transpose queries, then the parameter updates. Therefore the forward
response sums have \(j<k\) and the transpose response sums have \(j\le k\).
There is no artificial triangular order between the samples at a given
stage. All coefficients required at a stage have been determined by the
previous stages of this order.

Singular query Gram matrices, including those at \(\rho=-1\) and from a
zero readout, are covered by the dependency's fixed-program independent
query-noise regularization and its continuous zero-noise limit. Its
hypotheses continue to hold for the pair of root coordinates and the clips
here. That argument uses continuity of Gaussian covariance square roots
and of the formal finite expressions, without inverting a limiting
singular Gram matrix. Individual coefficients follow the stated formal
extension convention; their contracted corrections are invariant.

For the uncut affine activation, the same argument applies directly:
after the learned contractions are frozen, every coordinate instruction
is affine and has a bounded derivative. The finite induction transferring
contractions uses only finitely many finite norms. It requires no
mesh-uniform primal assumption to identify any one fixed mesh. At that
mesh, changing the initial readout by \(O_{\mathbb P}(n^{-1})\) changes
the calculation by \(o_{\mathbb P}(1)\) through this same induction.

## 4. The derivative rows and current-time returns

The following equations specify the derivative paths that replace the
one-sample calculation for (4). Write
\(d^{(\ell)}_{j,a}=\phi_e'(Z^{(\ell)}_{j,a})\), and set
\(m^{(1)}=q^{(1)},m^{(2)}=q^{(2)},m^{(3)}=C\), with the readout shared
between samples. Define the local backward partial derivatives

\[
 p^{(\ell)}_{j,a}
   =e g'(Z^{(\ell)}_{j,a})\tau_R(m^{(\ell)}_{j,a}),\qquad
 v^{(\ell)}_{j,a}
   =1+e g(Z^{(\ell)}_{j,a})\tau_R'(m^{(\ell)}_{j,a}).
\]

For \(\ell=3\), the notation \(m^{(3)}_{j,a}\) means \(C_j\).
For a bottom source \(\zeta^{(1)}_{v,b}\), put
\(J_{k,a}=\partial_{\zeta^{(1)}_{v,b}}Z^{(1)}_{k,a}\).
Then \(J_{0,a}=0\), \(\partial H^{(1)}_{k,a}=d^{(1)}_{k,a}J_{k,a}\), and

\[
 J_{k+1,a}=J_{k,a}+h_k\sum_u c_u\rho_{au}
 \left[
 p^{(1)}_{k,u}J_{k,u}
 +v^{(1)}_{k,u}
   \left(\mathbf1_{(k,u)=(v,b)}
    +\sum_{j\le k,w}D^{(2)}_{ku,jw}d^{(1)}_{j,w}J_{j,w}\right)
 \right].
\tag{12}
\]

In particular the direct current query has a cross-sample effect

\[
 \frac{\partial H^{(1)}_{k+1,a}}
      {\partial\zeta^{(1)}_{k,b}}
 =h_k c_b\rho_{ab}
   d^{(1)}_{k+1,a}v^{(1)}_{k,b}.
\tag{13}
\]

For a source in population 2, let \(\partial\) denote its formal
derivative. The exact middle recursions are

\[
 \partial Z^{(2)}_{k,a}
  =\partial\xi^{(2)}_{k,a}
       +\sum_{j<k,b}A^{(2)}_{ka,jb}\partial\delta^{(2)}_{j,b},
\]
\[
 \partial q^{(2)}_{k,a}
  =\partial\zeta^{(2)}_{k,a}
       +\sum_{j\le k,b}D^{(3)}_{ka,jb}d^{(2)}_{j,b}
                                      \partial Z^{(2)}_{j,b},
\]
\[
 \partial\delta^{(2)}_{k,a}
  =p^{(2)}_{k,a}\partial Z^{(2)}_{k,a}
      +v^{(2)}_{k,a}\partial q^{(2)}_{k,a}.
\tag{14}
\]

For a population-3 source,

\[
 \partial Z^{(3)}_{k,a}
  =\partial\xi^{(3)}_{k,a}
       +\sum_{j<k,b}A^{(3)}_{ka,jb}\partial\delta^{(3)}_{j,b},
\]
\[
 \partial C_k=\sum_{j<k,b}h_jc_b d^{(3)}_{j,b}
                                      \partial Z^{(3)}_{j,b},
\]
\[
 \partial\delta^{(3)}_{k,a}
  =v^{(3)}_{k,a}\partial C_k
       +p^{(3)}_{k,a}\partial Z^{(3)}_{k,a}.
\tag{15}
\]

All sums over samples in (12)--(15) are retained. In particular the
current middle transpose return is the full block

\[
 D^{(3)}_{ka,kb}
    =\mathbf1_{a=b}\,\mathbb E[p^{(3)}_{k,a}],
\]
\[
 D^{(2)}_{ka,kb}
  =\mathbf1_{a=b}\,
       \mathbb E[p^{(2)}_{k,a}]
    +D^{(3)}_{ka,kb}\,
       \mathbb E[v^{(2)}_{k,a}d^{(2)}_{k,b}].
\tag{16}
\]

Thus the same-time return through the other matrix is present, including
its sample indices. For this particular explicit Euler schedule the
off-diagonal entries in the current block are zero: \(C_k\) uses only
strictly earlier top features, and each current forward preactivation
has only its own current formal forward source. Equation (16) proves
these zeros; cross-sample source correlations do not turn formal partial
derivatives into derivatives along the Gaussian support. Earlier-time
blocks are generally full. Equations (13)--(16) retain the actual
cross-sample propagation and do not assume independent sample copies.

## 5. Affine primal hypothesis and a deterministic response estimate

From now on set \(\phi_0(z)=1+z\) and remove every clip. Then

\[
 \delta^{(3)}_a=C,\qquad
 \delta^{(2)}_a=W_3^TC,\qquad
 q^{(1)}_a=W_2^TW_3^TC.
\tag{17}
\]

These are identities on the actual unperturbed affine network. The
formally named sample sources remain separate, as required in Section 3.

Here is a precise primal-bound hypothesis, using the usual normalized
finite vector norm \(\|v\|_n=\|v\|_2/\sqrt n\).

**Primal hypothesis P(B,S).** Let \(B\ge1\). For every mesh under
consideration with \(s_N\le S\), the actual unforced affine Euler states
satisfy, with probability tending to one as width tends to infinity,

\[
 \max_{k\le N}
 \max\{\max_a\|Z^{(1)}_{k,a}\|_n,
        \|W_{2,k}\|_{\rm op},\|W_{3,k}\|_{\rm op},\|C_k\|_n\}
 \le B.
\tag{18}
\]

The same \(B\) is used for all meshes. The width limit here is at each
fixed mesh; a probability bound uniform over an increasing number of
meshes is not required. A strict margin can always be supplied by
enlarging an available bound. Section 8 explains how a population primal
bound supplies (18), so this formulation does not require an additional
operator-norm convergence theorem.

For two states use the norm of their difference

\[
 d(\theta,\widetilde\theta)
  =\max_a\|Z^{(1)}_a-\widetilde Z^{(1)}_a\|_n
    +\|W_2-\widetilde W_2\|_{\rm op}
    +\|W_3-\widetilde W_3\|_{\rm op}
    +\|C-\widetilde C\|_n.
\tag{19}
\]

All forthcoming deterministic estimates hold identically for population
\(L^2\) norms and bounded actions. Put

\[
 b=2B,\qquad L=9b^2=36B^2,\qquad E=\exp(LS).
\tag{20}
\]

On the ball with each of the four primal sizes at most \(b\),

\[
 \|H^{(1)}_a\|_n\le2b,\quad
 \|H^{(2)}_a\|_n\le3b^2,\quad
 \|H^{(3)}_a\|_n\le4b^3,
\]
\[
 \|\delta^{(3)}_a\|_n\le b,\quad
 \|\delta^{(2)}_a\|_n\le b^2,\quad
 \|q^{(1)}_a\|_n\le b^3.
\]

Let \(\mathcal V_0\) be the four-component raw affine vector field from (1)--(2).
Its four components have Lipschitz constants, with respect to (19),
bounded respectively by \(b^2,2b^2,3b^2,3b^2\). To verify this, write
the individual state differences as \(u,v,w,t\) in the order in (19).
The forward and backward differences obey

\[
 \|\Delta H^{(1)}_a\|_n\le u,\quad
 \|\Delta H^{(2)}_a\|_n\le bu+2bv,
\]
\[
 \|\Delta H^{(3)}_a\|_n\le b^2u+2b^2v+3b^2w,
 \quad
 \|\Delta\delta^{(2)}_a\|_n\le b(w+t),
\]
\[
 \|\Delta q^{(1)}_a\|_n\le b^2(v+w+t).
\]

Insert these inequalities into the updates, use the rank-one difference
inequality, \(\sum|c_a|=1\), and
\(\sum_b|c_b\rho_{ab}|\le1\). The matrix-2 component is bounded by
\(b^2u+2b^2w+2b^2t\), and the matrix-3 component by
\(b^2u+2b^2v+3b^2t\). This gives the claimed constants and hence

\[
 d(\mathcal V_0(\theta),\mathcal V_0(\widetilde\theta))
       \le Ld(\theta,\widetilde\theta),
 \qquad \|\mathcal V_0(\theta)\|\le10b^3.
\tag{21}
\]

Here the first notation means the sum/max component norm, applied to the
two vector-field values. No coordinate supremum or matrix Frobenius
bound growing with width enters (21).

Next add external vector errors to exactly one class of intermediate
answers: to \(Z^{(2)}_{j,a}\), \(Z^{(3)}_{j,a}\),
\(q^{(2)}_{j,a}\), or \(q^{(1)}_{j,a}\), immediately after its trained
matrix call and before using the answer. This is also an additive error
after its unrolled initial-matrix answer and learned correction. Later
calls and parameter updates are recomputed. If the errors at a time
have norm at most \(e_j\), the change of the vector field at a fixed
state in this ball is bounded by \(\kappa e_j\), where

| Source/answer perturbed | Affected update components | \(\kappa\) |
| --- | --- | ---: |
| \(\xi^{(2)} / Z^{(2)}\) | \(W_3,C\) | \(2b\) |
| \(\xi^{(3)} / Z^{(3)}\) | \(C\) | \(1\) |
| \(\zeta^{(2)} / q^{(2)}\) | \(Z^{(1)},W_2\) | \(3b\) |
| \(\zeta^{(1)} / q^{(1)}\) | \(Z^{(1)}\) | \(1\) |

For example, a middle forward error \(e_a\) adds
\(C\otimes\sum_a c_ae_a\) to the \(W_3\) update and
\(W_3\sum_a c_ae_a\) to the \(C\) update, each of norm at most \(be_j\).
A middle transpose error adds at most \(be_j\) to the first-layer
update and \(2be_j\) to the \(W_2\) update. This proves the table.

Take errors \(\varepsilon\alpha_{j,a}g\), where
\(|\alpha_{j,a}|\le1\) are deterministic and \(g\) is a single vector
in the population where the answers live. The same vector is reused at
all chosen times and sample slots. Discrete Gronwall applied to (21)
and the table gives

\[
 d(\theta^\varepsilon_k,\theta^0_k)
       \le \kappa S E|\varepsilon|\|g\|_n.
\tag{22}
\]

If only one source time \(j<k\) is perturbed, the sharper bound is
\(\kappa h_jE|\varepsilon|\|g\|_n\). Indeed the error is introduced
in the state update at time \(j\), with its factor \(h_j\), and subsequent
factors are bounded by \(\prod_{r>j}(1+Lh_r)\le E\).

The comparison remains in the ball used in its derivation. On (18) and
\(\|g\|_n\le2\), choose fixed \(|\varepsilon|\) so small that
\(2\kappa S E|\varepsilon|<B/2\). Induction through the recurrence
gives this same strict bound at every next node, starting from zero
state difference. Thus the perturbed state cannot leave the ball of
radius \(b=2B\). This justifies (22) without a primal assumption on a
perturbed trajectory. The case \(S=0\) has no state update and is direct.

## 6. The Gaussian probe identity for formal derivatives

This section proves the connection used to convert (22) into source
bounds. It uses finite differences; no interchange of a width limit with
an unproved derivative or normalized-trace limit is needed.

Fix a mesh, an output coordinate expression \(V\) in one population, and
one of the source groups in that same population. Denote this group by
\(\eta=(\eta_{j,a})\). Take an iid \(N(0,1)\) vector \(g\), independent
of the entire initial network, and insert the errors
\(\varepsilon\alpha_{j,a}g\) at the corresponding answers as above.
There is no pairing of this vector with coordinates in another layer.
Run both the unperturbed and perturbed finite programs, sharing the
initial matrices and roots.

At any fixed \(\varepsilon\), apply Section 3 to the perturbed program
with \(g\) as an extra root in its own population. Use its own query
slots and coefficient recursion, so the formal convention is exactly
the one in (7)--(9). Consequently

\[
 \langle g,V^\varepsilon_n\rangle_n
       \ \longrightarrow\ \mathbb E[G V^\varepsilon]
       \quad\hbox{in probability},
\tag{23}
\]

where \(G\sim N(0,1)\). The scalar source groups of the perturbed
program are independent of this root. Their deterministic covariance
parameters and learned/source coefficients may depend on \(\varepsilon\).
This independence is exactly the independent-root conclusion of the
finite Gaussian conditioning rule, and does not assert independence
between a trained answer and the root that was inserted into it.

For the affine activation, with these deterministic coefficients fixed,
every scalar coordinate is an affine function of the root tuple and
the four Gaussian groups. This follows by finite induction from
(6), (9), (10), since every gate is the constant one. Let

\[
 T_{V,ja}(\varepsilon)=\partial_{\eta_{j,a}}V^\varepsilon
\]

be its deterministic formal coefficient. The only explicit appearances
of \(G\) in the scalar instructions are the inserted additions
\(\varepsilon\alpha_{j,a}G\). Their positions are exactly those of the
named source arguments. Differentiating this affine expression with
respect to \(G\), with the deterministic coefficients fixed, yields

\[
 \partial_G V^\varepsilon
       =\varepsilon\sum_{j,a}\alpha_{j,a}T_{V,ja}(\varepsilon),
 \qquad
 \mathbb E[G V^\varepsilon]
       =\varepsilon\sum_{j,a}\alpha_{j,a}T_{V,ja}(\varepsilon).
\tag{24}
\]

For the second equality, write the affine expression as
\(U+\varepsilon(\sum\alpha T)G\), where \(U\) is independent of
\(G\), then use \(\mathbb EG=0\), \(\mathbb EG^2=1\).
Equivalently it is the one-dimensional Gaussian integration-by-parts
identity. This establishes the probe identity, including its coefficient
normalization and which formal derivatives it measures.

For completeness, \(T_{V,ja}(\varepsilon)\to T_{V,ja}(0)\) at this
fixed mesh. Induct through the causal order in Section 3: affine
coordinate coefficients are continuous functions of earlier
deterministic coefficients; their second moments are continuous
functions of those coefficients and the earlier covariance entries.
Expected formal derivatives are their deterministic affine
coefficients. These observations pass every next covariance and
coefficient continuously. Gaussian square-root continuity, including
at singular covariance, supplies a joint realization if one is wanted.
There is no inverse covariance in this induction.

Since \(V^0_n\) is independent of the new root, conditionally on the
unperturbed network this pairing is centered Gaussian with variance
\(\|V^0_n\|_n^2/n\). Its tight normalized norm, supplied by the
unperturbed fixed-program limit, therefore gives
\(\langle g,V^0_n\rangle_n\to0\) in probability. If a stability estimate gives

\[
 \|V^\varepsilon_n-V^0_n\|_n
       \le C|\varepsilon|\|g\|_n
\]

on events of probability tending to one, Cauchy--Schwarz gives
\(|\langle g,V^\varepsilon_n-V^0_n\rangle_n|/|\varepsilon|
\le C\|g\|_n^2\).
First take width to infinity at fixed nonzero \(\varepsilon\), using
(23)--(24) and \(\|g\|_n\to1\). Then send \(\varepsilon\to0\) by the
just-proved finite-program continuity. The conclusion is

\[
 \left|\sum_{j,a}\alpha_{j,a}
               \mathbb E\partial_{\eta_{j,a}}V^0\right|\le C.
\tag{25}
\]

The signs may now be chosen as
\(\alpha_{j,a}=\operatorname{sgn}T_{V,ja}(0)\), with zero at a zero
coefficient. They are deterministic for this fixed mesh. Equation (25)
then bounds the entire absolute derivative row. A single nonzero
\(\alpha_{j,a}\) yields the one-entry estimate from the single-time
version of (22).

This argument covers off-support formal directions as well. Even if two
unperturbed sources coincide, the prescribed additive errors can be
different at their two query slots; (24) differentiates the exact named
finite expressions. No nonsingularity of any source group is assumed.

## 7. Explicit mesh-uniform affine source bounds

Assume P(B,S), and retain \(E=\exp(36B^2S)\). All the following bounds hold
for every output sample \(a\), every mesh, and every \(k\le N\).
The affine formal derivatives are deterministic, so the absolute value
of their expectation equals their expected absolute value.

The four rows entering (7)--(8) satisfy

\[
\begin{aligned}
 \sum_{j<k,b}\left|\mathbb E
      \frac{\partial H^{(1)}_{k,a}}{\partial\zeta^{(1)}_{j,b}}\right|
       &\le SE,\\
 \sum_{j<k,b}\left|\mathbb E
      \frac{\partial H^{(2)}_{k,a}}{\partial\zeta^{(2)}_{j,b}}\right|
       &\le24B^2SE,\\
 \sum_{j\le k,b}\left|\mathbb E
      \frac{\partial\delta^{(2)}_{k,a}}{\partial\xi^{(2)}_{j,b}}\right|
       &\le8B^2SE,\\
 \sum_{j\le k,b}\left|\mathbb E
      \frac{\partial\delta^{(3)}_{k,a}}{\partial\xi^{(3)}_{j,b}}\right|
       &\le SE.
\end{aligned}
\tag{26}
\]

Here is the substitution into (25). For bottom transpose forcing,
\(H^{(1)}\) changes by at most the state difference, and \(\kappa=1\).
For middle transpose forcing, \(H^{(2)}\) changes by at most
\(2b\) times the state difference and \(\kappa=3b\), giving
\(6b^2SE=24B^2SE\). For middle forward forcing,
\(\delta^{(2)}=W_3^TC\) changes by at most \(b\) times that difference
and \(\kappa=2b\), giving \(2b^2SE=8B^2SE\). For top forward forcing,
\(\delta^{(3)}=C\) changes by at most the difference and \(\kappa=1\).
None of these four outputs has a direct contribution from the current
source in its indicated group. In particular the two current derivative
blocks in the last two rows are identically zero.

For every fixed \(j<k\) and source sample \(b\), the corresponding
single entry in each row of (26) is bounded by the same expression with
\(S\) replaced by \(h_j\), while keeping \(E=\exp(36B^2S)\). This is a
mesh-scale bound on the entries, as well as a bound on their row sums.

Two useful forward-source row bounds, proved by the same argument, are

\[
 \sum_{j\le k,b}\left|
       \mathbb E\frac{\partial Z^{(2)}_{k,a}}{\partial\xi^{(2)}_{j,b}}
                         \right|
       \le1+16B^2SE,
\qquad
 \sum_{j\le k,b}\left|
       \mathbb E\frac{\partial Z^{(3)}_{k,a}}{\partial\xi^{(3)}_{j,b}}
                         \right|
       \le1+12B^2SE.
\tag{27}
\]

The constants are the output Lipschitz constants \(2b,3b^2\) times
\(\kappa=2b,1\), respectively. The added one is the direct source at
the current output query. Since \(H=1+Z\), (27) also holds for the
corresponding features. These bounds control expected absolute rows
as well, by the deterministic-derivative observation above.

The unperturbed primal bounds imply
\(\|H^{(1)}\|_2\le2B\), \(\|H^{(2)}\|_2\le3B^2\),
\(\|\delta^{(2)}\|_2\le B^2\), \(\|\delta^{(3)}\|_2\le B\).
Cauchy--Schwarz in the learned terms of (7)--(8), followed by
\(\sum_b|c_b|=1\), therefore gives the complete coefficient row bounds

\[
 \sum_{j<k,b}|A^{(2)}_{ka,jb}|\le S(E+4B^2),\qquad
 \sum_{j<k,b}|A^{(3)}_{ka,jb}|\le S(24B^2E+9B^4),
\]
\[
 \sum_{j\le k,b}|D^{(2)}_{ka,jb}|\le S(8B^2E+B^4),\qquad
 \sum_{j\le k,b}|D^{(3)}_{ka,jb}|\le S(E+B^2).
\tag{28}
\]

In addition, for \(j<k\),

\[
 |A^{(2)}_{ka,jb}|\le h_j(E+2B^2),\qquad
 |A^{(3)}_{ka,jb}|\le h_j(24B^2E+\tfrac92B^4),
\]
\[
 |D^{(2)}_{ka,jb}|\le h_j(8B^2E+\tfrac12B^4),\qquad
 |D^{(3)}_{ka,jb}|\le h_j(E+\tfrac12B^2),
 \qquad D^{(2)}_{ka,kb}=D^{(3)}_{ka,kb}=0.
\tag{29}
\]

In the notation used for main's continuation bootstrap, one may take
the following common entry and backward-row constants:

\[
 A_* =24B^2\exp(36B^2S)+\tfrac92B^4,\qquad
 M_* =S\bigl(8B^2\exp(36B^2S)+B^4\bigr).
\]

They give \(\lvert A^{(\ell)}_{ka,jb}\rvert\le A_*h_j\) for
\(\ell=2,3\), and
\(\sum_{j\le k,b}\lvert D^{(\ell)}_{ka,jb}\rvert\le M_*\).
If a forward block means a whole \(2\times2\) matrix with fixed times
\(k,j\), its maximum absolute row sum, and also its Euclidean operator
norm, are at most \(2A_*h_j\). Thus \(A=2A_*\), \(M=M_*\) meet that
block convention. These constants concern the actual affine baseline;
they are independent of the nonlinear-part cap since (4) at \(e=0\)
does not depend on that cap.

These are explicit finite constants for every finite \(B,S\). They do
not depend on the number of steps, the smallest step, or a covariance
condition number. Their only use of labels and input geometry was through
\(\sum|c_a|=1\) and \(\sum_b|c_b\rho_{ab}|\le1\). Thus the same formulas
apply at the antipodal endpoint and to opposite labels.

## 8. Interpreting a population or continuous-time primal bound

If the supplied primal bound is formulated on the actual population
affine Euler states, suppose its precise content is

\[
 \max_{k,a}\|Z^{(1)}_{k,a}\|_2\le B_0,\quad
 \max_k\{\|W_{2,k}\|_{\rm op},\|W_{3,k}\|_{\rm op},\|C_k\|_2\}
      \le B_0,\qquad B_0\ge1,
\tag{30}
\]

uniformly over the considered meshes on \([0,S]\). These actions can
be realized by the dependency's common-action construction with the
affine coordinate maps and joint two-sample roots: finite unions remain
finite programs; normalized Gaussian operator bounds and finite
adjunction pass to the countable generated probe spaces, then extend
by continuity. Affine maps satisfy its coordinate hypotheses directly.

Section 3 already gives fixed-mesh convergence of every field used in
the learned updates. The dependency's Gaussian net estimate supplies
\(\|W_{2,0}\|_{\rm op},\|W_{3,0}\|_{\rm op}\le10\) with probability
tending to one. At a fixed mesh, exact unrolling and these empirical
norm convergences consequently give

\[
 \max_k\|W_{2,k}^{(n)}\|_{\rm op}
    \le10+2SB_0^3+o_{\mathbb P}(1),\qquad
 \max_k\|W_{3,k}^{(n)}\|_{\rm op}
    \le10+3SB_0^3+o_{\mathbb P}(1).
\tag{31}
\]

For the first inequality, each summand is bounded by
\(h_j|c_b|\|\delta^{(2)}_{j,b}\|_n\|H^{(1)}_{j,b}\|_n\), whose
limit is at most \(2h_j|c_b|B_0^3\); sum the finitely many terms.
The second uses \(B_0\cdot3B_0^2\). The first-layer and readout
norms converge to values at most \(B_0\) at these finitely many nodes.
Thus P(B,S) holds with the explicit substitution

\[
 B=11+B_0+4SB_0^3.
\tag{32}
\]

The slack in (32) absorbs all fixed-mesh convergence errors. Equations
(26)--(29) with this value are therefore consequences of the population
primal bound (30) alone. No independent assumption about convergence of
the trained matrix operator norms was inserted.

If only a continuous affine population trajectory is initially known
to obey a bound \(B_0\) on \([0,S]\), (21) supplies the usual bounded-set
Euler comparison on that same action space. More explicitly, on a
larger ball with bound \(b\), the vector field is bounded by
\(10b^3\) and is \(9b^2\)-Lipschitz. Integrating the exact flow over
one step shows a local Euler error at most
\(45b^5h_j^2\). The error recurrence and
\(\sum_j h_j^2\le S|\pi|\), where \(|\pi|=\max_jh_j\), give total
error at most \(45b^5S\exp(9b^2S)|\pi|\). Choose \(b>B_0\) and then
\(|\pi|\) small enough that this is less than the distance to the ball
boundary. The same first-exit induction as after (22) justifies the
comparison. Hence a continuous-trajectory bound supplies a uniform
Euler bound for all sufficiently fine meshes. A bound on arbitrary
coarse Euler steps is not inferred from a flow bound.

## 9. Scope of the result and remaining premises

The requested affine baseline response bound has been established under
the stated uniform bound on the actual affine primal trajectory/Euler.
The identification step is the proved probe formula (24)--(25), so the
bound does not rely on assuming that a formal derivative equals a
finite-network trace. Both independent initial hidden matrices, both
transpose calls, all time/sample covariance slots, and the true raw
first-layer coupling remain in the argument.

The remaining premise for this baseline is the primal bound itself on
the interval to be used. Its precise norm content and the conversion
from a population version are (18) and (30)--(32). Constants grow with
that bound and with the finite interval. No bound on these constants as
\(S\to\infty\) is asserted.

For the main route with the specified \(\phi_e\) and nonlinear-part
clips (4), this note leaves the nonlinear perturbation/Volterra
estimates, cutoff removal, and the physical two-sample gradient-flow/GD
theorem to the main proof. It supplies the actual affine baseline
coefficient bound those estimates require. The affine reference retains
all parameter updates, and no parameter or feature is frozen. The
analysis makes no inference that a fixed small nonlinear amplitude
causes lazy training, nor does it introduce an amplitude tending to
zero with width.
There is no remaining formal-derivative/trace-identification gap within
the conditional affine baseline established above.
