# Independent review of the rank-safe optimizer candidate

2026-10-08. **PASS for the scoped deterministic claims and conditional theorem
transfers described below.** This is not a new audit of the inherited stochastic
source theorem, its initialization-only producer, or its temporal-rank bound.
It does not establish accurate compression, fitting, or endpoint existence at
arbitrary widths below the sample count.

The frozen input was `OPTIMIZER.md`, SHA-256
`159c986ae19326ffba3ac84265e551b2452bd263f0d909c49b1f36f25bd115a8`.
I read that candidate completely, the assigned passages of
`paper/integrated_appendix.tex` (3195–3447 and 11547–12520), its complete
coordinate-selection dependency (11408–11546), its relevant full-retention and
inventory dependency near 12822–12854, and `docs/notation.qmd`.
The paper and notation hashes agree with the candidate's recorded hashes.
I read the required rigorous-proof, canonical-notation, and neural-network
instructions. I did not inspect another study, the study README, other drafts,
earlier reviews, or code. No training or implementation was performed.

## 1. Spectral reconstruction and degenerate spectra

The cutoff in equations (1)–(2) is well defined: its two denominator terms
cannot both vanish, its transition is smooth, and its denominator
\(s+\mu_\tau(s)\) is positive for every \(s\ge0\), including \(s=0\).
The bounds \(g_\tau(s)\le2/\tau\) and
\(0\le1-sg_\tau(s)\le1\) are correct. The equality
\(g_\tau(s)=1/s\) includes the threshold \(s=\tau\).

Equation (3) follows by writing the Frobenius norm in the two orthonormal
eigenbases. It proves local Lipschitz continuity of the matrix function on the
positive-semidefinite cone without differentiating eigenvectors. Composition
with the smooth Gram map therefore gives a locally Lipschitz function of the
raw finite-dimensional state, including at changing rank and repeated
eigenvalues. No positive Gram gap is needed for this conclusion.

With the selected top-layer metric, the squared singular values of
\(V_Cg_\tau(V_C^*V_C)\) are
\(s/(s+\mu_\tau(s))^2\). For \(s\le\tau/2\) this is at most
\(1/(2\tau)\), and for \(s\ge\tau/2\) it is at most \(1/s\le2/\tau\).
Thus equation (5) holds uniformly in the spectrum and the rank. At
\(V_C=0\), the correction is zero, despite the finite value
\(g_\tau(0)=1/\tau\).

The variational characterization is also correct. In a nonzero singular
direction, write the readout increment as \(\alpha\) times the corresponding
unit left singular vector. Its objective is
\(\alpha^2/2+(\sqrt{s}\alpha-b_i)^2/(2\mu_\tau(s))\), giving
\(\alpha=\sqrt{s}\,b_i/(s+\mu_\tau(s))\). When the penalty vanishes,
the hard constraint is feasible because \(s\ge\tau>0\). A zero singular
direction contributes only a constant to the objective. The norm term makes
the minimizer unique and removes orthogonal readout components.

## 2. Deficit energy, actual residual, and global continuation

The columns of \(\mathcal J_C\) and their parameter-space adjoint have the
correct factors of \(\sqrt m\). Consequently the squared norm of the combined
raw-parameter velocity is

\[
\frac4m\left(\|V_Cc_C\|_{M_L}^2+
                    \|\mathcal J_Cc_C\|_{\rm par}^2\right)
=\frac4m c_C^T(Q_C+\mathcal J_C^*\mathcal J_C)c_C
=-\frac d{dt}\frac{\|c_C\|_2^2}{m}.
\]

This verifies equation (7) without either gradient backpropagation or an
invertible Gram. At \(c_C=0\), every evolution equation vanishes; the formulas
do not divide by a residual.

The energy bound and Cauchy–Schwarz bound raw-parameter displacement by
\(Y\sqrt t\). On a hypothetical finite maximal interval, the raw parameters
and deficit therefore stay in a fixed compact set. Smooth activations and the
locally Lipschitz spectral reconstruction bound the vector field on that set.
The state then has a limit at the maximal time, and the local existence and
uniqueness theorem extends it. This proves global existence and uniqueness
at every positive selected width, for fixed positive metrics and fixed
\(\tau>0\). The argument also permits restarting from any finite saved state,
with its current deficit norm replacing the original \(Y\).

The actual prediction residual must be computed separately. Since
\(f_{C,\mathrm{train}}/\sqrt m=V_C^*w_C+Q_Cg_\tau(Q_C)b_C\), substitution
of \(b_C=(y-c_C)/\sqrt m-V_C^*w_C\) gives exactly

\[
r_C=-c_C-\sqrt m\,[I-Q_Cg_\tau(Q_C)]b_C.
\]

Thus equation (9), its sign, and its normalization are correct. Deficit energy
does not generally equal prediction loss. The candidate correctly withholds
prediction-loss monotonicity, fitting, finite total path length, and endpoint
existence on the deficient-Gram branch. Its all-time existence result concerns
finite-time continuation, not a uniform-in-time bound on all raw parameters.

## 3. Every positive budget has a valid initialization

The constant source has empirical norm one and ensures retained source rank
at least one. For \(q\ge9\), the proposed retained rank
\(r_j\le\lfloor q/9\rfloor\) lets the paper's deterministic selector give
\(q_j\le9r_j\le q\). Its metric formula yields both
\(P_j^TM_jP_j=I\) and the stated diagonal comparison conditions.
For \(1\le q<9\), one selected coordinate with \(M_j=1\) is an exact
isometry of the constant source and satisfies those same conditions.

Writing the initialized mixer as
\(P_jH_jP_{j-1}^TM_{j-1}\), where
\(H_j=U_j^TW_0^{(j)}U_{j-1}/n\), shows that its norm is at most the dense
mixer norm: the two selected source maps are isometries and the dense source
compression is contractive. This remains true after truncation. Preserving
the first-weight columns and initial training feature Gram, however, does not
follow after those sources are removed; the candidate explicitly says so.

These arguments check the definitions at \(q=1\), \(q=8\), \(q=9\),
\(q<m\), and at zero or deficient feature rank. They do not supply a
cheap low-budget source producer. The candidate's disclosure that a complete
source family may first be compiled and then truncated is necessary.

The full-coordinate fallback should retain its stated interpretation as an
available separate branch. Retaining \(n\) coordinates is not itself an
\(O(R)\) storage bound when \(n>9R\); the logarithmic inventory is obtained
by choosing the complete-source selected branch with \(q_j\le9R\).
The candidate's exact transfer explicitly makes that choice.

## 4. Exact transfer and its inventory

Assume the old theorem's complete-source, selection, initialization, and label
conditions, including its old solution with
\(Q_C(t)\succeq\lambda I/4\) for all \(t\ge0\). For
\(0<\tau\le\lambda/4\), the filter equals the inverse at every spectral
value on that old solution. The old state is therefore a solution of the new
ODE with exactly the same initial state. The independently proved uniqueness
of the new ODE identifies both solutions for all time. Old panel outputs,
fitting, endpoint limits, and approximation estimates transfer exactly.
There is no perturbation remainder or extra small-label assumption.

This is a correct conditional implication. It does not re-establish the old
source event, its probability, an effective width threshold, the finite-jet
producer, or the asserted finite-panel rank
\(R=O(\log(en)^{5/2})\). Those remain inherited hypotheses in this review.
The assigned paper states the safe full-range coefficient
\(44+64\sqrt{\log(en)}\); the later coefficient-32 refinement has the
smaller label cap. Using 64 in the conditional transfer is correct.

For the selected complete-source branch, the moving state contains exactly

\[
q_1d+\sum_{j=2}^Lq_jq_{j-1}+q_L+m
\]

raw scalar coordinates. Fixed metrics, data, the floor scalar, and Gram or
spectral workspace must also be counted. Their orders remain
\(O(LR^2+mLR+m^2+Rd+m(d+1)+p d)\), with passive-panel data counted when
retained. Thus the inherited fixed-panel, fixed-structural-parameter regime
still has logarithmic exponent five. No bound uniform in arbitrary growing
\(m,d,p,L\) follows by suppressing these factors.

The spectral workspace statement is a scalar-storage statement. I have not
certified a finite exact-arithmetic implementation of transcendental matrix
functional calculus or eigendecomposition, numerical conditioning, or a
finite-step approximation to this continuous ODE. None is supplied by the
global existence proof or by the storage count.

## 5. Diagonal metrics and the no-deficit alternative

For a diagonal gate \(D\) in a positive metric \(M\), its metric adjoint is
\(M^{-1}DM\). The difference from the candidate's specified gate is
\(M^{-1}(DM-MD)\), exactly equation (13). Source isometry alone does not
control that commutator. The candidate correctly avoids asserting that a
general full-metric raw-readout gradient flow inherits the old comparison.

The diagonal selection proof is complete. More than
\(r(r+1)/2\) positive weights give a linear dependence among their symmetric
rank-one matrices. Every row is nonzero because the constant belongs to the
source. Taking traces forces both signs in a nonzero dependence, so the stated
weight elimination preserves nonnegativity and removes at least one positive
weight. Repeating terminates with the claimed support. The identity
\(P^TMP=I\) and the constant source imply total diagonal mass one.
The paper's metric comparison conditions then hold with comparison metric
equal to \(M\).

Diagonal metrics commute with every activation gate. The equations (14) are
therefore the metric gradient flow of the stated mean squared prediction loss;
the parameter metric gives \(d\mathcal L_C/dt=-\|\dot\theta_C\|_{
\rm par}^2\). The same energy-continuation argument proves global existence
at any positive width, without a Gram inverse or independently evolving
deficit. On the complete-source branch, setting \(c_C=y-f_C\) embeds this
flow into the old corrected system while the Gram is positive. Local
uniqueness and the old global margin make this identification global. The
old deterministic estimates use source isometry and the metric comparisons,
which this diagonal selection satisfies; their dynamical proof does not
require the support-size bound of the earlier selector.

With \(q_j\le R(R+1)/2\), dense hidden matrices cost \(O(LR^4)\).
Conditional on the inherited temporal rank, the general proved logarithmic
exponent is ten. The absence of a moving deficit does not remove the fixed
training labels or transient residual computations. The candidate accurately
distinguishes that weaker result from exponent-five compression with no
sample-indexed moving state.

No blocking mathematical objection was found in these scoped claims. The
remaining stronger optimizer/storage assertion and the external source
production theorem are not covered by this PASS.
