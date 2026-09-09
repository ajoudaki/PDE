# Candidate common-calculus theorem for every fixed linear depth

**Status:** proved in autonomous physical time after three independent
hostile reconstructions. Global feature-time well-posedness is explicitly
falsified for \(H\ge2\).  
**Forbidden ingredients:** no depth-two spectral invariant, no cyclic lift,
and no depth-specific free trace identity are used.

## 1. Statement

Fix \(H\ge1\), \(y_\star\in\mathbb R\), and \(\eta>0\). Use the canonical
model in the parent research contract with \(\phi(x)=x\). Then there is one
deterministic pointed Gaussian action source

\[
 \mathfrak G_H=(\mathcal H_1,\ldots,\mathcal H_H;
 u_0,a_0,\Gamma_1,\ldots,\Gamma_{H-1})                 \tag{1.1}
\]

with bounded true-adjoint actions
(\Gamma_\ell:\mathcal H_\ell\to\mathcal H_{\ell+1}), and a unique global
physical-time solution

\[
 S(t)=(A(t),u(t),P_1(t),\ldots,P_{H-1}(t),e(t))        \tag{1.2}
\]

in

\[
 \mathcal X_H=\mathcal H_H\times\mathcal H_1\times
 \prod_{\ell=1}^{H-1}\mathfrak S_1
 (\mathcal H_\ell,\mathcal H_{\ell+1})\times\mathbb R.\tag{1.3}
\]

Let \(G_\ell=\Gamma_\ell+P_\ell\), set

\[
 x_1=u,\qquad x_{\ell+1}=G_\ell x_\ell,
\]

and, backward,

\[
 b_H=A,\qquad b_\ell=G_\ell^*b_{\ell+1}.
\]

The limiting IDE/operator ODE is

\[
\boxed{
\begin{aligned}
 \dot A&=2\eta e\,x_H,&
 \dot u&=2\eta e\,b_1,\\
 \dot P_\ell&=2\eta e\,(b_{\ell+1}\otimes x_\ell),
      &&1\le\ell<H,\\
 K&=\|x_H\|^2+\|b_1\|^2+
   \sum_{\ell=1}^{H-1}\|b_{\ell+1}\|^2\|x_\ell\|^2,&
 \dot e&=-2\eta eK,
\end{aligned}}                                         \tag{1.4}
\]

with (A(0)=a_0,u(0)=u_0,P_\ell(0)=0,e(0)=y_\star). It is autonomous and
restartable, and

\[
 f(t)=\langle A(t),x_H(t)\rangle=y_\star-e(t),
 \qquad \mathcal L(t)=e(t)^2.                          \tag{1.5}
\]

For every \(T<\infty\), the canonical finite networks satisfy

\[
 \sup_{t\le T}
 \bigl(|f_n-f|+|K_n-K|+|e_n-e|+|e_n^2-e^2|\bigr)
 \xrightarrow{\mathbb P}0.                            \tag{1.6}
\]

Moreover every fixed current rooted-action signature converges uniformly,
and every current nuclear perturbation has uniformly tight
best-finite-rank tails. No cross-width norm convergence of the operators
themselves is claimed. Constants may depend on fixed
\(H,T,\eta,y_\star\), but not on width.

The theorem claims compact physical time. It does not claim a joint
width/long-time limit or a depth-uniform constant.

## 2. Exact finite and limiting compilation

For identity activation, `Forward`, `Reverse`, and `Gradient` in the parent
calculus give exactly

\[
 x_{\ell+1}=G_\ell x_\ell,\qquad
 b_\ell=G_\ell^*b_{\ell+1},                            \tag{2.1}
\]

and the block gradients in (1.4). The matrix blocks use the **ordinary**
Frobenius pairing \(\operatorname{Tr}(M^{\mathsf T}N)\), while vector
blocks use the normalized Hilbert pairing. For
\((b\otimes_nx)z=b\langle x,z\rangle_n=n^{-1}bx^{\mathsf T}z\),

\[
 \|b\otimes_nx\|_F=\|b\otimes_nx\|_1
 =\|b\|_n\|x\|_n.                                    \tag{2.2}
\]

Therefore the squared product-Hilbert norm of the feature vector field is
exactly \(K\), at finite width and in the limiting Hilbert spaces. The chain
rule gives

\[
 Df[V]=K,\qquad \dot f=2\eta eK=-\dot e.              \tag{2.3}
\]

At finite width \(e_n(0)=y_\star-f_n(0)\), so
\(f_n+e_n=y_\star\) exactly. In the limit, source orthogonality below gives
\(f(0)=0\), proving (1.5). No invariant beyond the generic gradient identity
has been used.

`SourceSplit` is also exact:

\[
 G_{\ell,n}(t)=G_{\ell,0,n}+P_{\ell,n}(t),\qquad
 P_{\ell,n}(t)=2\eta\int_0^t
 e_n(s)b_{\ell+1,n}(s)\otimes_nx_{\ell,n}(s)\,ds.      \tag{2.4}
\]

The same Bochner identity defines the limiting \(P_\ell\). It stores only a
current operator; its rank-one time decomposition is not part of the state.

## 3. One source theorem for all fixed depths

### Lemma 3.1 (polynomial pointed Gaussian source)

For every fixed \(H\), the independent normalized Ginibre actions and two
independent normalized Gaussian endpoint vectors converge jointly in the
following full-sequence sense. For any finite compatible rooted words
(P,Q) in the labeled actions and adjoints and roots
(r,s\in\{u,a\}),

\[
 \langle P_nr_n,Q_ns_n\rangle_n
 \xrightarrow{\mathbb P}
 \langle P r,Q s\rangle.                              \tag{3.1}
\]

Every finite collection converges jointly in probability, and

\[
 \max_{\ell<H}\|G_{\ell,0,n}\|_{\rm op}\le 3         \tag{3.2}
\]

with probability tending to one. The limit may be represented on a
**real** full Fock source. Let \(\mathcal F_{\mathbb R}\) be real full Fock
space over two creation colors for every matrix label, let

\[
 c_\ell=\ell(e_{\ell,+})+\ell(e_{\ell,-})^*,
\]

and put

\[
 \mathcal H=\mathcal F_{\mathbb R}\oplus\mathcal F_{\mathbb R},\qquad
 \Gamma_\ell=c_\ell\oplus c_\ell,\qquad
 u_0=(\Omega,0),\quad a_0=(0,\Omega).                  \tag{3.3a}
\]

Each typed layer space is a copy of \(\mathcal H\). In this representation

\[
 \|\Gamma_\ell\|=2,\qquad
 \|u_0\|=\|a_0\|=1,                                   \tag{3.3}
\]

every program transpose is the actual Hilbert adjoint, and for all
compatible words

\[
 \langle w(\Gamma)r_i,v(\Gamma)r_j\rangle
 =\delta_{ij}\tau(w^*v).                              \tag{3.4}
\]

#### Proof

Expand each scalar in (3.1) into raw Gaussian entries. Wick's formula splits
the expectation into pairings. A pairing survives the normalized free-index
count exactly when its labeled edges form the usual noncrossing circular
pairing; these are precisely the real Fock vacuum inner products. Pairings that
connect two copies lose at least one free index, so the variance is
(O_H(n^{-1})) for every fixed pair of words. Chebyshev and a finite union
bound give joint convergence in probability. Same-root endpoint contractions
produce the vacuum moment, whereas the two independent endpoint copies have
zero cross-root contractions. Mere orthogonality of \(u_0,a_0\) would not
be enough: the direct-sum construction makes their entire cyclic source
subspaces orthogonal. This also proves \(f_n(0)\to0\) in probability.

The Gaussian Bai--Yin edge theorem gives
(\|G_{\ell,0,n}\|_{\rm op}\to2) almost surely under a standard coupling for
each fixed label; a
finite union gives (3.2). Left creation operators are isometries, so each
real circular Fock action has norm two. Defining a transpose letter as the
Hilbert adjoint on the word core proves the adjoint assertion; boundedness
extends it to the completion. The proof claims only convergence in
probability: the variance estimate \(O(1/n)\) is not summable and by itself
does not imply almost-sure convergence. \(\square\)

Only fixed-word Wick counting and individual source operator bounds enter.
No spectral measure, cyclic matrix, or depth-specific trace identity is
present.

## 4. Internal well-posedness and the universal energy bound

Equip (1.3) with

\[
 \|S\|_{\mathcal X}=\|A\|+\|u\|+
 \sum_{\ell<H}\|P_\ell\|_1+|e|.                      \tag{4.1}
\]

Because \(\mathfrak S_1\hookrightarrow\mathcal B\), every forward and
backward word in (2.1) is a bounded multilinear map of the state. Rank one is
bilinear into trace class. Thus the right side of (1.4) is locally Lipschitz
on \(\mathcal X_H\); \(K\) is a locally Lipschitz nonnegative polynomial of
the same fields. Picard--Lindelöf gives a unique maximal solution and local
continuous dependence. This argument is identical for all \(H\).

This statement concerns the **physical** ODE (1.4). The unit
feature-gradient flow, obtained by deleting the factor \(2\eta e\), is not
global when \(H\ge2\). Every one of its \(H+1\) block energies has
derivative \(f\). If \(F'=f\), the balancedness identities and
Cauchy--Schwarz imply on the positive branch

\[
 f'=K\ge \frac{(H+1)f^2}{B+2F},
 \qquad f\ge C(B+2F)^{(H+1)/2}.
\]

The resulting \(dF/f\) integral is finite for \(H\ge2\), and the Fock
feature solution blows up at finite endpoints. No global feature clock or
feature-flow continuation is used below. All Picard slabs, energy bounds,
and convergence statements are in autonomous physical time.

The residual identity supplies the dimension-free continuation estimate

\[
 \frac d{dt}e^2=-4\eta e^2K,\qquad
 \int_0^T e(t)^2K(t)dt\le {|e(0)|^2\over4\eta}.        \tag{4.2}
\]

For every endpoint or operator block \(\theta_j\), its feature velocity
\(V_j\) contributes \(\|V_j\|^2\) to \(K\). Hence

\[
 \int_0^T\|\dot\theta_j(t)\|dt
 \le2\eta\sqrt T
      \left(\int_0^Te^2Kdt\right)^{1/2}
 \le |e(0)|\sqrt{\eta T}.                             \tag{4.3}
\]

For an operator block, feature velocity is rank one, so its trace and
Hilbert--Schmidt norms agree; (4.3) is genuinely a trace-norm bound. Summing
over the fixed \(H+1\) blocks bounds (4.1) on every compact interval.

For completeness, this bound really yields continuation in the
infinite-dimensional state space. On every ball

\[
 \|A\|+\|u\|+\sum_\ell\|P_\ell\|_1+|e|\le R,\qquad
 \max_\ell\|\Gamma_\ell\|_{\rm op}\le C,               \tag{4.4}
\]

finite product telescoping and
\(\|P_\ell\|_{\rm op}\le\|P_\ell\|_1\) bound every
forward/backward field, \(K\), the vector field, and its Lipschitz constant
by a number depending only on \(C,R,H,\eta\). Thus a finite maximal time
would contradict the standard local continuation theorem. The same
calculation after any time \(t_0\) uses \(e(t_0)\) and proves restart
bounds. Therefore the solution is global in physical time and restartable.

The finite systems obey the identical estimates, with \(e_n(0)\) in place
of the limiting \(e(0)=y_\star\). On the source event (3.2),
\(e_n(0)=y_\star-f_n(0)\) is tight, so all constants
needed below are uniform in width with probability tending to one.

## 5. Rooted-action topology and the varying-space lemma

Let a **current rooted program** be any fixed finite typed expression built
from the current endpoint fields, the current \(G_\ell,G_\ell^*\), finite
inner products, sums, and scalar products. Enumerate their scalar signatures
and the joint Gram matrices of every finite field tuple. Add, for every
current \(P_\ell\), its trace norm, fixed singular-value tests, and best-rank
tails

\[
 \tau_m(P_\ell)=\sum_{k>m}s_k(P_\ell).                 \tag{5.1}
\]

The resulting countable bounded sum metric \(d_{\rm ract}\) compares only
isomorphism classes of typed pointed actions; it never subtracts vectors or
operators belonging to different widths.

### Lemma 5.1 (dimension-free Picard transfer)

Suppose a sequence of source tuples satisfies Lemma 3.1 and has a common
operator bound \(M\). Let polynomial/rank-one ODEs of the common typed form
(1.4) start from those sources, and suppose all trajectories stay in a
common \(\mathcal X_H\)-ball on \([0,T]\). Then every fixed locally
Lipschitz scalar current-program signature \(\Sigma\) satisfies

\[
 \sup_{t\le T}|\Sigma(S_n(t))-\Sigma(S(t))|
 \xrightarrow{\mathbb P}0,                            \tag{5.2}
\]

where the displayed difference is between scalar signatures, not states.
In addition,

\[
 \lim_{N\to\infty}\limsup_{n\to\infty}
 \Pr\!\left\{\max_{\ell<H}\sup_{t\le T}
 \tau_N(P_{\ell,n}(t))>\varepsilon\right\}=0           \tag{5.2a}
\]

for every \(\varepsilon>0\).

#### Proof

Work first on a time interval of length \(\Delta\) on which the common
state ball and source bound give one Lipschitz constant (L) for the typed
vector field. Start Picard iteration from the constant initial state.

At every fixed Picard index \(m\), each endpoint is a finite algebraic
combination of rooted source words with scalar coefficient functions. Each
\(P_\ell^{[m]}\) is a finite sum of rank-one operators between such words.
The scalar coefficients are obtained only by addition, multiplication,
inner products, and time integration. Induction on \(m\) therefore shows
that they are continuous functions of a finite list of initial rooted
Grams. Approximating their time integrals by deterministic Riemann sums
shows that convergence of this finite Gram list implies uniform convergence
of every fixed-\(m\) scalar signature. Parallel evaluation at finitely many
time arguments gives every joint multi-time signature needed by a later
slab or a Riemann surrogate. This is the required coefficient induction;
“finite word” alone would not suffice if discontinuous coefficient rules
were allowed.

The standard Picard remainder on the common ball satisfies

\[
 \sup_{t\le\Delta}\|S^{[m+1]}(t)-S^{[m]}(t)\|_{\mathcal X}
 \le C{(L\Delta)^m\over m!},                           \tag{5.3}
\]

with the same bound in every finite dimension. There is no cross-width norm
in this argument. For a fixed scalar signature \(\Sigma\), write

\[
\begin{aligned}
 |\Sigma(S_n)-\Sigma(S)|
 &\le|\Sigma(S_n)-\Sigma(S_n^{[m]})|\\
 &\quad+|\Sigma(S_n^{[m]})-\Sigma(S^{[m]})|
       +|\Sigma(S^{[m]})-\Sigma(S)| .                 \tag{5.3a}
\end{aligned}
\]

The outer terms are estimated inside their own state spaces by (5.3) and
the common local Lipschitz constant of \(\Sigma\). The middle term is the
finite continuous source-Gram program just proved. Choose \(m\) first to
make the outer terms small, then take \(n\to\infty\). This proves (5.2) on
the first slab.

For nuclear tails, the common vector-field bound makes every trajectory
uniformly Lipschitz in time. The common polynomial Lipschitz estimates then
make

\[
 h_{\ell,n}(t)
 =2\eta e_n(t)b_{\ell+1,n}(t)\otimes_nx_{\ell,n}(t)
\]

uniformly Lipschitz in trace norm, with a constant \(C_{T,H,M}\). Approximate
the Bochner integral (2.4) by a left Riemann sum on \(N\) equal cells. The
sum has rank at most \(N+1\), including a possible partial final cell, and

\[
 \sup_n\sup_{t\le T}\tau_{N+1}(P_{\ell,n}(t))
 \le \sup_n\sup_{t\le T}
 \|P_{\ell,n}(t)-P_{\ell,n}^{(N)}(t)\|_1
 \le {C_{T,H,M}\over N}.                              \tag{5.4}
\]

The same holds in the limit. Bochner integrability without this
equicontinuity estimate would not imply a uniform nuclear tail.

For later slabs, do not declare the exact current state to be a finite
source program. Instead use the fixed Picard approximation from the
preceding slabs as the next program initial state. If \(E_j\) is the
within-space exact-versus-program error at the start of slab \(j\), ordinary
stability and the factorial Picard tail give

\[
 E_{j+1}\le e^{L\Delta}E_j+\varepsilon_m,\qquad
 \varepsilon_m\longrightarrow0
\]

uniformly in width. The number of slabs is finite. The resulting nested
approximation is still one finite continuous source-Gram program, so the
middle term in (5.3a) converges. The deterministic estimates hold on common
source/state events whose probabilities tend to one. This proves
(5.2)--(5.2a). \(\square\)

The content of Lemma 5.1 is strictly more general than any one linear depth:
it applies to every fixed typed polynomial/rank-one action ODE with the stated
source and ball certificates.

## 6. Direct finite-width identification

Lemma 3.1 supplies G1 and every fixed Picard/Euler program, hence G3. Section
4 supplies one common state ball, well-posedness, and restartability, hence
G2. Lemma 5.1 simultaneously removes the Picard/time truncation and proves
G4--G5. Applying it to (f,K,e,e^2), which are polynomial current-program
readouts, gives (1.6).

There is no interchange of a time derivative with a width limit. Width is
taken for a fixed Picard approximation; the dimension-free factorial tail is
removed afterward. There is no external feature-time clock: physical time
and residual are components of the same autonomous ODE.

## 7. Validation ladder outputs

The compiler specializes without changing a rule.

- \(H=1\): there are no actions or nuclear fields. In global feature time,
  \(A'=u,u'=A\), so the calculus regression readout is
  \(F_1(s)=\sinh(2s)\).
- \(H=2\): one Gaussian action and one current nuclear perturbation occur;
  \(K(0)=3\). On its maximal feature interval this is isomorphic in readouts
  to the established spectral IDE, but no spectral invariant enters this
  proof. The physical IDE is global.
- \(H=3\): two Gaussian actions and two current nuclear perturbations occur;
  \(K(0)=4\). Local fixed rooted-word differentiation gives the independent
  regression values
  \((F'(0),F^{(3)}(0),F^{(5)}(0))=(4,160,13888)\), but these numbers play no
  role in positive-time identification.

Thus one rule set covers all three stages and is already formulated for every
separately fixed \(H\). The cost grows with fixed depth; no depth-uniform
theorem is claimed.

## 8. Promotion audit

The final isolated reconstruction verified:

1. the variance loss in Lemma 3.1 for every compatible rooted word and two
   distinct endpoint sectors;
2. that individual operator-norm bounds suffice for all fixed-word Picard
   estimates;
3. the claim that every fixed Picard iterate has finite rooted-word/rank-one
   form despite its scalar coefficient integrals;
4. uniformity of (5.3) after the physical residual is coupled;
5. the Riemann-rank tail estimate (5.4) uniformly over finite width and time;
6. continuity of the raw kernel in the selected signature/state topology;
   and
7. the restart induction across time slabs without coordinate embeddings.

All seven items pass for the autonomous physical-time theorem. See
`../audits/LINEAR_PHYSICAL_FINAL_AUDIT_03.md`. The common calculus therefore
replaces the three old identity-activation proofs without importing their
depth-specific solution devices.
