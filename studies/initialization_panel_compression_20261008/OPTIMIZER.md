# Rank-safe optimizer and the precise transfer of the existing theorem

2026-10-08. Scoped theoretical candidate; no training experiment, implementation,
shared-code edit, Git staging, or promotion. The supervisor assigned this file
alone. The main result below preserves the existing logarithmic exponent five,
but retains the independently evolved vector of $m$ deficits. A separate
diagonal-metric construction removes that vector and is a genuine gradient
flow; its proved general selection bound gives exponent ten, so it does not
meet the stronger exponent-five target.

The mathematical inputs read were the complete approved
`studies/finite_panel_absolute_compression_20261005/PANEL_RUNTIME.md`,
`paper/integrated_appendix.tex` lines 3195–3447 and 11547–12520,
`DeepDense`, `DeepHarmonic`, their activation evaluator and the source-basis /
coordinate-metric helpers in `paper/figures/capture_trajectory.py`, and
`docs/notation.qmd`. Required proof, conjecture, canonical-notation and neural
notation instructions, their applicable contract/audit references, and the
shared process instructions were read. No other study's scientific contents,
another route's draft, or history was consulted. A storage-route coordination
message supplied its intended safe coefficient 64, already independently
observed here in the assigned paper passage; it did not supply a proof draft.

## 1. Contract and the two distinct rank restrictions

The reference is the paper's depth-$L$ dense network, $L\ge2$, with unit
inputs $v_a=x_a/\sqrt d$, zero stored readout at initialization, mean squared
training loss, and block mobilities $(n,1,\ldots,1,n)$. There are $m$
training points and $p\ge0$ additional passive points, giving a fixed finite
panel of $m+p$ points. Thus the total-panel symbol used in the supplied
`PANEL_RUNTIME.md` corresponds to $m+p$ here. The runtime argument does not require the training
inputs to span the input space. The covariance gap, normalized gap and label
scale are the paper's
\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
\lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m.
\]
All full-range label and source assumptions stay unchanged. The construction
uses only finite initialization-derived sources and fixed data; no future
reference trajectory is retained or queried. The approximation target is the
same-time supremum of prediction errors over the fixed panel and all physical
times, including the endpoint.

For compact widths \(q_j\), let $q$ be their supplied upper budget, so
$\max_jq_j\le q$. The existing readout
uses an inverse of \(Q_C=V_C^*V_C\), where
\(V_C\in\mathbb R^{q_L\times m}\). Thus \(Q_C>0\) implies
\(q_L\ge m\). Independently, exact preservation of a positive-definite
initialized training-feature Gram forces the source rank and selected width
to be at least \(m\). Deleting the explicit Python `budget < len(labels)`
rejection removes neither mathematical restriction.

The construction below has a definition for every positive width budget.
The existing accuracy theorem applies when that budget is sufficient to keep
its complete source space. That sufficient regime still has \(q_L\ge m\).
This is a distinction between definition and certification, not a claim that
arbitrary $m$-point data admit arbitrary-accuracy compression at $q<m$.

## 2. A bounded spectral reconstruction

Fix a scalar \(\tau>0\), retained with the model. Define a smooth cutoff
\(\chi:\mathbb R\to[0,1]\) by
\[
b(s)=\begin{cases}e^{-1/s},&s>0,\\0,&s\le0,\end{cases}
\qquad
\chi(s)=\frac{b(1-s)}{b(1-s)+b(s-1/2)}.
\]
The denominator is positive everywhere. Hence \(\chi=1\) on
\(( -\infty,1/2]\), \(\chi=0\) on \([1,\infty)\), and the transition
is smooth. For \(s\ge0\), put
\[
\mu_\tau(s)=\tau\chi(s/\tau),\qquad
g_\tau(s)=\frac1{s+\mu_\tau(s)}.
\tag{1}
\]
For \(s\le\tau/2\), the denominator is \(s+\tau\); for
\(s\ge\tau/2\), it is at least \(s\). Consequently
\[
0<g_\tau(s)\le2/\tau,\qquad
g_\tau(s)=1/s\quad(s\ge\tau),\qquad
0\le1-sg_\tau(s)\le1.
\tag{2}
\]
If \(Q=U\operatorname{diag}(s_i)U^T\succeq0\), define
\(g_\tau(Q)=U\operatorname{diag}(g_\tau(s_i))U^T\).
This definition is independent of the eigenbasis chosen at repeated
eigenvalues. It uses no pseudoinverse, rank test or eigenvector selection as
part of the mathematical state.

For completeness, the matrix map is locally Lipschitz without needing
differentiability of individual eigenvectors. If \(g_\tau\) has scalar
Lipschitz constant \(C\) on an interval containing the spectra of symmetric
matrices $A,B$, their orthonormal eigenbases $u_i,v_j$ give
\[
\begin{aligned}
\|g_\tau(A)-g_\tau(B)\|_F^2
 &=\sum_{i,j}|g_\tau(a_i)-g_\tau(b_j)|^2|u_i^Tv_j|^2\\
 &\le C^2\sum_{i,j}|a_i-b_j|^2|u_i^Tv_j|^2
 =C^2\|A-B\|_F^2.
\end{aligned}
\tag{3}
\]
The first and last equalities follow by expanding the squared Frobenius
norm and using orthonormality. The scalar derivative is bounded on every
compact interval (indeed on the nonnegative half-line). This proves the
regularity needed for the ODE below.

Keep the paper's first weights $A_C$, hidden mixers $B_C^{(j)}$, raw
readout $w_C$, and deficit $c_C\in\mathbb R^m$, with fixed positive
metrics $M_j$. Selected-layer vectors use $\|u\|_{M_j}=\sqrt{u^TM_ju}$;
sample vectors use the Euclidean norm, and operator norms use these domain
and target norms. Compute the ordinary coordinate forward pass
\[
z_C^{(1)}(v)=A_Cv,\quad
z_C^{(j)}(v)=B_C^{(j)}h_C^{(j-1)}(v),\quad
h_C^{(j)}(v)=\phi_j(z_C^{(j)}(v)).
\]
Let $V_C$ have columns $h_C^{(L)}(v_a)/\sqrt m$, let
\(V_C^*=V_C^TM_L\), and set
\[
Q_C=V_C^*V_C,\qquad
b_C=(y-c_C)/\sqrt m-V_C^*w_C.
\]
The new effective readout and predictions are
\[
\widehat w_C=w_C+V_Cg_\tau(Q_C)b_C,\qquad
f_C(v)=\widehat w_C^TM_Lh_C^{(L)}(v).
\tag{4}
\]
All quantities are defined even if $q_L<m$, $V_C=0$, or its rank changes.
In the singular direction $s=0$, the filter is the finite value $1/\tau$.
The complete readout map is bounded in the sense
\[
\|V_Cg_\tau(Q_C)\|\le\sqrt{2/\tau}.
\tag{5}
\]
Indeed its squared singular values are
\(s/(s+\mu_\tau(s))^2\); splitting at $s=\tau/2$ gives (5).

This is a regularized least-squares correction with exact constraints on
well-resolved spectral directions. In a $Q_C$-eigenbasis, the correction
has coefficient $b_i/(s_i+\mu_\tau(s_i))$. Equivalently, it is the unique
minimum-norm readout increment minimizing
\[
\frac12\|u\|_{M_L}^2+
\frac12\sum_{\mu_\tau(s_i)>0}
\frac{|(V_C^*u)_i-b_i|^2}{\mu_\tau(s_i)}
\]
subject to $(V_C^*u)_i=b_i$ whenever \(\mu_\tau(s_i)=0\).
Those hard constraints are feasible because their eigenvalues satisfy
$s_i\ge\tau>0$. Solving each scalar normal equation gives $u=V_Cg_\tau(Q_C)b_C$.
Directions orthogonal to the range of $V_C$ vanish by norm minimization.

## 3. Dynamics, energy and global well-posedness

Define the specified training responses just as in the paper:
\[
k_{C,a}^{(L)}=\widehat w_C,\qquad
\delta_{C,a}^{(j)}=\phi_j'(z_{C,a}^{(j)})\odot k_{C,a}^{(j)},\qquad
k_{C,a}^{(j)}=M_j^{-1}B_C^{(j+1)T}M_{j+1}\delta_{C,a}^{(j+1)}.
\]
Use the parameter norm
\[
\|\theta_C\|_{\rm par}^2=
\operatorname{tr}(A_C^TM_1A_C)+
\sum_{j=2}^L\|M_j^{1/2}B_C^{(j)}M_{j-1}^{-1/2}\|_F^2+
w_C^TM_Lw_C.
\]
Let \(\mathcal J_C\) have sample columns divided by $\sqrt m$,
\[
\left(\delta_{C,a}^{(1)}v_a^T,
 \bigl(\delta_{C,a}^{(j)}h_{C,a}^{(j-1)T}M_{j-1}\bigr)_{j=2}^L\right),
\]
in the hidden parameter Hilbert space. Its adjoint is for that parameter
norm and the Euclidean sample norm. The equations remain
\[
\dot\theta_{h,C}=2\mathcal J_Cc_C/\sqrt m,\qquad
\dot w_C=2V_Cc_C/\sqrt m,\qquad
\dot c_C=-2(Q_C+\mathcal J_C^*\mathcal J_C)c_C,
\tag{6}
\]
with $w_C(0)=0,c_C(0)=y$. All layers train; no forcing uses a dense runtime.

**Exact energy identity.** Set \(\rho_C=\|c_C\|_2/\sqrt m\).
From (6),
\[
-\frac d{dt}\rho_C^2
 =\frac4m c_C^T(Q_C+\mathcal J_C^*\mathcal J_C)c_C
 =\|\dot\theta_C\|_{\rm par}^2.
\tag{7}
\]
This is a deficit-energy identity; it is the actual prediction-loss identity
only in the consistent regime described below. No positive Gram margin is
used in (7).

**Global well-posedness.** For the stated smooth activations and fixed positive
metrics, (3) makes the vector field locally Lipschitz at every finite state.
Its local solution satisfies
\[
\rho_C(t)\le Y,\qquad
\int_0^t\|\dot\theta_C\|_{\rm par}^2\,ds\le Y^2,\qquad
\|\theta_C(t)-\theta_C(0)\|_{\rm par}\le Y\sqrt t.
\tag{8}
\]
The last estimate is Cauchy–Schwarz. A finite maximal existence time would
therefore leave both the raw parameters and $c_C$ in a compact finite
dimensional set. Features, (4), and the vector field are bounded there; local
existence at a limit point extends the solution, contradicting maximality.
Thus the solution is unique for all $t\ge0$, at every positive width.
This argument proves finite-time continuation; it does not prove finite total
path length, endpoint existence, or fitting in the rank-deficient regime.

**Actual prediction residual.** Direct multiplication in (4) gives
\[
r_C=(f_C(v_a)-y_a)_{a=1}^m
 =-c_C-\sqrt m\,[I-Q_Cg_\tau(Q_C)]b_C.
\tag{9}
\]
The correction operator in square brackets has eigenvalues between zero and
one and vanishes on eigenvalues at least \(\tau\). Equation (9) is the exact
consistency error. One must not label $\rho_C^2$ the prediction loss in the
general deficient-Gram case. Neither monotonicity of $\|r_C\|_2^2/m$ nor
$r_C\to0$ follows from (7). The construction removes a definition-level
rank obstruction; it does not evade the representational obstruction.

## 4. Width-budget initialization, including budgets below $m$

Assume the permitted initialization-only producer supplies a finite full
source space $E_j^{\rm full}$ at each layer, including the constant vector.
Choose an ordered orthonormal basis in the dense empirical norm, starting
with $\mathbf1_n$. Given an integer budget $q\ge1$, do the following.

* If $q\ge n$, full retention $q_j=n,M_j=I_n/n$ is available.
* If $q<n$ and $q\ge9$, retain the first
  \(r_j=\min(\dim E_j^{\rm full},\lfloor q/9\rfloor)\) basis vectors.
  Apply the paper's coordinate selection to this truncated source space;
  it returns $q_j\le9r_j\le q$ and the paper's exact isometry and metric
  comparison conditions.
* If $1\le q<9$, retain only the constant source, choose any single dense
  coordinate, and use the scalar metric $M_j=1$. This has exact constant
  isometry and the same comparison conditions, with $q_j=1\le q$.

Here $q$ is an upper width budget, as in the selection theorem. This simple
definition is conservative at very small budgets; it claims no optimal use
of those budgets. It has no sample-count rejection and requires no training
Gram factorization. An improved small-budget selector is an implementation
choice, not a missing mathematical definition.

For retained basis $U_j$ satisfying $U_j^TU_j/n=I$, selected row matrix
$P_j$, and selected coordinates $I_j$, use
\[
A_C(0)=(A_0)_{I_1},\qquad
B_C^{(j)}(0)=P_j\frac{U_j^TW_0^{(j)}U_{j-1}}nP_{j-1}^TM_{j-1}.
\tag{10}
\]
Exact selected-source isometry implies that the norm of each initialized
mixer is at most the corresponding dense operator norm. At low budgets,
however, the initialized compact features and their Gram need not equal the
selected dense ones: first-weight columns and initialized training features
have deliberately ceased to be mandatory exact sources. Their preservation
returns precisely when the full source space is retained.

The basis ordering, truncation and metric may be discontinuous functions of
the initialization at degenerate rank ties. This is a finite setup choice,
already present in coordinate selection; it is not a time-dependent
pseudoinverse or a discontinuity of the deployed vector field. All source
arrays and dense arrays are discarded after (10). Only the current compact
parameters, metrics, $c_C$, data and one floor scalar are retained.

This is not a cheap budget-adaptive preprocessing theorem. The definition may
first compile the full initialization-derived source family and then truncate
it. That disposable compilation can use dense arrays and substantial work even
when the deployed width is tiny. Only the retained runtime inventory is claimed
to obey the logarithmic theorem; preprocessing cost is a separate obligation.

## 5. Exact transfer of the exponent-five theorem

Take any \(0<\tau\le\lambda/4\), for example \(\tau=\lambda/8\).
On the existing complete source, selection and initialization event, and on
the existing full-range label allowance, the paper proves for its original
optimizer
\[
Q_C(t)\succeq\lambda I/4\qquad(t\ge0).
\tag{11}
\]
If the budget retains all source spaces, use the same selected initialization.
Equation (2) gives \(g_\tau(Q_C(t))=Q_C(t)^{-1}\) along the entire old
solution. Thus that old solution solves (4)–(6) with exactly the same initial
state. The global uniqueness proved above forces the new and old solutions
to coincide for every physical time. Their panel outputs and endpoints
therefore coincide too. This proves transfer without a perturbative estimate,
an additional label restriction, or a hidden change in the optimizer on the
certified regime.

In particular all source-error, stability and all-time approximation
certificates apply with their existing constants. The regularizer contributes
one scalar of retained state. Its spectral function can be evaluated from
the same $m$-by-$m$ Gram workspace; its description is fixed. A finite
scalar eigensolver needs $O(m^2)$ workspace already covered by the existing
inventory. Thus $q_j\le9R$, $R=O(\log(en)^{5/2})$, and the full retained
inventory $O(\log(en)^5)$ are unchanged. A rough sufficient budget is
\(q\ge9\max_j\dim E_j^{\rm full}\); the particular support chosen can be
smaller.

The theorem still depends on the supplied initialization-only source and
selection event. No independent proof of its outside insertion or finite-jet
producer dependencies was attempted. No quantitative success-width threshold
has been obtained here. The correct exact-real arithmetic convention is
inherited; no bit-complexity or numerical conditioning guarantee is asserted.

The moving state still contains
\[
q_1d+\sum_{j=2}^Lq_jq_{j-1}+q_L+m
\]
scalars. Neither the source truncation nor the spectral extension removes the
last $m$. Saying that this model has no sample-indexed persistent state
would be false.

## 6. Why a raw-readout natural gradient does not follow for full metrics

For a fixed positive metric, let $D_{a,j}$ denote the diagonal coordinate
gate with entries \(\phi_j'(z_{a,i}^{(j)})\). Its metric adjoint is
\[
D_{a,j}^*=M_j^{-1}D_{a,j}M_j.
\tag{12}
\]
The true metric gradient of the raw prediction $w^TM_Lh^{(L)}$ propagates
\(D_{a,j}^*k_{a}^{(j)}\), whereas the paper's specified optimizer propagates
\(D_{a,j}k_a^{(j)}\). Their difference is
\[
M_j^{-1}(D_{a,j}M_j-M_jD_{a,j})k_a^{(j)}.
\tag{13}
\]
Exact source inner-product isometry does not state that this commutator is
small on the dynamically reached carriers. The given proof controls the
specified gate and its paired initialized actions; it supplies no estimate
for (13). Consequently replacing the runtime by the genuine raw-readout
metric gradient is well defined, and has its own loss-energy identity, but
its approximation to the dense reference is an unproved additional claim
under the full-metric $q=O(R)$ selection interface.

## 7. Complete no-deficit alternative, with the exponent cost exposed

There is a constructive way to make (13) identically zero. For a source
basis $U\in\mathbb R^{n\times r}$ with $U^TU/n=I_r$, write $u_i^T$
for its rows. Start with all weights $a_i=1/n$, so
\(\sum_i a_i u_iu_i^T=I_r\). The space of symmetric $r$-by-$r$ matrices
has dimension $s=r(r+1)/2$. If more than $s$ weights remain positive,
their matrices have a nontrivial linear dependence
\(\sum_i\alpha_i u_iu_i^T=0\). Since the source contains the constant,
each $u_i\ne0$. Taking the trace shows that the nonzero dependence has
both signs. Let $t=\min_{\alpha_i>0}a_i/\alpha_i$ and replace
\(a_i\) by $a_i-t\alpha_i$. All weights stay nonnegative, at least one
becomes zero, and the matrix identity is preserved. Finite repetition gives
at most $s$ positive weights.

Set $M=\operatorname{diag}(a_i)$ on the retained coordinates. Then
\(P^TMP=I_r\). As \(\mathbf1_n=Uu\) for a vector $u$,
\(\|u\|_2^2=1\), so
\[
\mathbf1^TM\mathbf1=u^TP^TMPu=1.
\]
Thus the complete source isometry holds with a positive diagonal metric of
total mass one. The paper's metric conditions hold with comparison metric
equal to $M$. This argument is the full finite elimination proof; no
external cubature theorem is required.

With these diagonal metrics use the forward pass in Section 2, the raw
predictor \(f_C=w_C^TM_Lh_C^{(L)}\), the actual residual
\(r_{C,a}=f_C(v_a)-y_a\), and loss
\(\mathcal L_C=m^{-1}\sum_a r_{C,a}^2\). Store only the raw parameters.
Compute the same backward recursion using $w_C$ at the top and evolve
\[
\begin{aligned}
\dot A_C&=-\frac2m\sum_a r_{C,a}\delta_{C,a}^{(1)}v_a^T,\\
\dot B_C^{(j)}&=-\frac2m\sum_a r_{C,a}\delta_{C,a}^{(j)}
                       h_{C,a}^{(j-1)T}M_{j-1},\\
\dot w_C&=-\frac2m\sum_a r_{C,a}h_{C,a}^{(L)}.
\end{aligned}
\tag{14}
\]
Diagonal $M_j$ commute with every gate, so the chain rule gives the true
metric gradients of the predictions. Hence (14) is metric gradient flow and
\[
\frac d{dt}\mathcal L_C=-\|\dot\theta_C\|_{\rm par}^2.
\tag{15}
\]
The finite-time argument of (8), with actual loss in place of deficit energy,
proves unique global existence for every positive width. No Gram inverse or
persistent sample deficit appears. For a budget $q$, retaining a source
rank $r$ with $r(r+1)/2\le q$, always including the constant, gives a
definition at every $q\ge1$ through the same initialized projection (10).

On the complete-source branch, define $c_C=y-f_C$ along (14). Then
\(\dot c_C=-2(Q_C+\mathcal J_C^*\mathcal J_C)c_C\) by the chain rule,
and the original corrected-readout bracket is identically zero. The raw
gradient-flow solution therefore solves the old corrected system whenever
its Gram is positive. Conversely, its initial state embeds in that system;
local uniqueness and the old theorem's global Gram margin show equality for
all time. All of the old fitting and comparison estimates transfer exactly.

The cost is explicit: complete source rank $R$ gives
\(q_j\le R(R+1)/2\le R^2\). Hidden matrices then require
\(O(LR^4)\) moving scalars. With the authorized temporal rank
\(R=O(\log(en)^{5/2})\), this proves absolute logarithmic exponent ten,
not five. The diagonal metrics themselves cost only $O(LR^2)$, and the
persistent $m$-vector disappears, but those savings do not cancel the dense
hidden-matrix square. This is a valid weaker storage theorem, not a proof of
the requested stronger headline.

Redundant compatible data illustrate why a definition at $q<m$ is useful.
If inputs and labels are identical within $k$ groups, every network output
is also identical within each group. Let $S\in\mathbb R^{m\times k}$
have entry $1/\sqrt{n_b}$ at members of group $b$, where $n_b$ is
its size, and zero otherwise. Then $S^TS=I_k$, and the label, residual
and prediction vectors all lie in \(\operatorname{range}S\). Their
relevant feature Gram is $S^TQ_CS$, of size $k$, which can be positive
at $q\ge k<m$. There is no need for invertibility on the redundant
orthogonal sample directions. For merely clustered, distinct data this
exact invariant subspace need not exist; no generic accuracy claim for that
case is proved here.

## 8. Audits and remaining implications

The supplied `PANEL_RUNTIME.md` full-range estimate (16) reports the exponent
coefficient 32 and an integrated coefficient $44+32\sqrt{\log(en)}$.
The assigned current paper passage instead proves
\[
\mathcal B_n\le44+64\sqrt{\log(en)}
\]
at `paper/integrated_appendix.tex:12394`, with the corresponding
\(e^{64\sqrt{\log(en)}}\) prefactor at line 12462. The later coefficient-32
quantity is explicitly an optional original-tolerance refinement on the
smaller cap $Y/\lambda\le\beta^{-30L}$. The present transfer therefore
uses the paper's safe full-range coefficient 64; it does not import 32 into
the full-range theorem or shrink the label interval to improve an exponent.
The absolute logarithmic storage exponent remains five under this repair.

The fitting-energy argument in the supplied runtime and the assigned paper
does not require true gradient backpropagation: its Gram algebra is valid for
the specified optimizer. Its equality with prediction loss relies separately
on the invertible exact correction. Sections 2–3 preserve the Gram algebra
but expose exactly where the latter equality is lost below the floor.

The exact implications obtained here are:

* Every $q\ge1$ admits a globally defined autonomous, restartable version of
  the existing metric/deficit runtime after both source truncation and bounded
  spectral reconstruction. Its original full-source theorem is unchanged on
  the certified Gram domain, including exponent-five retained storage.
* That result retains an $m$-dimensional moving deficit and does not prove
  prediction-loss monotonicity or fitting on the deficient-Gram branch.
* A no-deficit natural gradient construction is globally well posed at every
  width and inherits the same approximation estimates through exact diagonal
  cubature; the proved general storage exponent is ten.
* To obtain all three stronger properties simultaneously—no persistent
  $m$-state, genuine metric gradient flow, and exponent-five retained
  storage—one still needs either a source-compatible diagonal selection with
  $q=O(R)$, or a sufficiently sharp bound on the commutator (13), or another
  new optimizer comparison. None is implied by the supplied sources.

These are internally derived candidates pending supervisor check; they are
not promoted results. The source-producer theorem remains inherited and
conditional throughout.

Input hashes at the metadata check, with repository HEAD
`785e47c6bdd60876c4e99f0ddb96cf43500f7305`:

* `capture_trajectory.py`:
  `8e26f402345e74151723008efcb60e183079c88a046f74e60e3381c842ab9463`.
* `integrated_appendix.tex`:
  `5d5c0c6ebe61d594f516eccc90360a7ca40cfa030656fa5af8452bcea5b7f137`.
* Approved `PANEL_RUNTIME.md`:
  `514d9e06cfd1cf23c496df0ece976812a39ea33f70112334c84326cfa0f0cd9f`.
* `docs/notation.qmd`:
  `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
