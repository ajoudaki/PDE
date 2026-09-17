# Generic three-input geometry: stationary alternatives and a compactness theorem

Root analytical route, 2026-09-16. Scope is the exact initialized canonical
p=1 closure, three equally weighted directions, labels (+1,+1,-1), physical
unhalved loss and unchanged population L2/Frobenius metric. This route does
not assume a data reflection or antipodal pair. No numerical experiment,
external convergence theorem, or different study is used.

The first stationary-state mechanism was developed locally, then supplied
to the metric route for its separately identified second pass. The compactness
refinement below was developed after that exchange. A separate bounded check
is recorded in generic3_compactness_check.md; its actual scope is distinct
from a fresh review of the whole study. No promotion is asserted.

## 1. Exact current upper features

The canonical simultaneous mark-reversal invariant subspace is preserved
for every data law. This is the parity result of docs/global_nonlinear.md
C.4.7.10.C.1 (H3.CS7) and its complete invariant-subsystem proof. It requires
no reflection of the inputs: w is odd under full lower-mark reversal, c is
odd under upper-mark reversal, and M has only its odd-to-odd block. The
initialized state lies in this subspace and uniqueness preserves it.

Consequently, writing Z=(tanh xi_1,tanh xi_2), every reached upper field is

\[
 H_i=\tanh(Z\cdot v_i),\qquad
 v_i=\frac{(M a(u_i))_{\mathrm{odd}}}{\sqrt{\tau+\eta}}
       \in\mathbb R^2,
\]

where eta=1/4096 and tau=E[tanh^2 xi_1]. This is exactly the canonical
Cholesky normalization of the upper odd block; it is not a new coordinate
metric or a replacement action. The law of Z has positive smooth density
on (-1,1)^2. Introduce label-adjusted fields and predictions only within
this proof:

\[
 V_i=y_iH_i=\tanh(Z\cdot(y_iv_i)),\qquad
 m_i=y_if(u_i)=E_2[cV_i].
\]

All targets for m_i are one, so the exact loss and readout equation are

\[
 \mathcal L=\frac13\sum_i(m_i-1)^2,
 \qquad \dot c=\frac23\sum_i(1-m_i)V_i.                 \tag{1}
\]

This notation changes no physical variable and stores no additional state.

## 2. Linear independence, including collinear coefficient vectors

For at most three nonzero vectors v_i, the functions tanh(Z dot v_i) are
linearly independent provided v_i!=v_j and v_i!=-v_j for i!=j. The vectors
may otherwise be collinear. This strengthens the earlier sufficient
noncollinearity condition at initialization.

Suppose a linear combination with coefficients t_i is zero in upper L2.
Positive density and continuity extend the identity throughout the open
square. Choose z so all s_i=v_i dot z are nonzero and s_i!=+/-s_j. This
avoids only finitely many lines, since all v_i and v_i+/-v_j are nonzero.
Restrict to Z=a z for small real a and use

\[
 \tanh x=x-x^3/3+2x^5/15+O(x^7).
\]

The coefficients of a,a^3,a^5 give

\[
 \sum_i(t_i s_i)(s_i^2)^k=0,\qquad k=0,1,2,
\]

using only as many rows as there are functions. The relevant Vandermonde
determinant is nonzero because the s_i^2 are distinct. Thus all t_i=0.
In particular, the only finite-coefficient linear dependencies among
three such fields arise from zero fields or equal/opposite field groups.

At a readout-stationary state, (1) is zero. Suppose no label-adjusted
coefficient y_i v_i is zero and no pair y_i v_i, y_j v_j is opposite.
Equal vectors are allowed. Group the identical V_i. The corresponding
m_i are also identical within each group, because the readout is common.
The remaining group fields are independent by the preceding lemma.
Their coefficients in (1) are the group size times 1-m_i, so each is
zero. Therefore m_i=1 for all i and the loss is zero.

Every full stationary state is readout-stationary. A nonfitting full
stationary state must therefore have a zero upper field or a label-adjusted
opposite pair. For different labels this means identical upper fields;
for the same label it means opposite upper fields. Equal same-class
fields are compatible with fitting and are NOT excluded by this argument.
This stationary characterization does not prove that the initialized
trajectory avoids the incompatible set.

## 3. Compactness of the entire upper-feature family

The family

\[
 \{\tanh(Z\cdot v):v\in\mathbb R^2\}
\]

is relatively compact in L2(Omega_2), even without a bound on M.
To see this, take any sequence v_n. A bounded subsequence has a convergent
further subsequence and the features converge in L2 by the Lipschitz gate.
Otherwise take a subsequence with |v_n| tending to infinity and
v_n/|v_n| tending to a unit vector d. For Z dot d!=0,

\[
 \tanh(Z\cdot v_n)\longrightarrow\operatorname{sign}(Z\cdot d).
\]

The exceptional line has zero probability because Z has a density.
Bounded convergence gives L2 convergence. Thus every limiting field is
either tanh(Z dot v) for finite v (including zero) or sign(Z dot d) for
some unit direction d. This compactness concerns the features only; it
does not assert compactness of the full state or boundedness of weights.

Any collection of at most three nonzero fields in this closure is linearly
independent after identifying equal and opposite fields. Here is the
additional boundary argument. In an almost-sure zero linear combination,
group sign fields with the same jump line, using opposite directions to
absorb their signs into coefficients. On each open cell between the finitely
many lines, all terms are continuous. Positive density extends the identity
through that cell. At a nonzero point of one jump line lying in the open
square and not on any other line, the finite tanh fields and all other sign
fields are continuous. The two one-sided limits differ by twice the
coefficient of that sign field, which must therefore vanish. Remove every
sign field in this way. The remaining finite tanh fields are independent
by Section 2. This proves the claim, including mixtures of finite tanh
and saturated sign fields.

## 4. A conditional convergence theorem allowing fluctuating geometry

**Theorem.** Suppose the actual initialized three-input trajectory has
reached a time t_0 with L(t_0)<1/3 and its readout satisfies

\[
                  \sup_{t\ge t_0}\|c(t)\|_2<\infty.
                                                               \tag{2}
\]

Then L(t) tends to zero. No uniform lower bound on the full readout Gram,
no monotonic pairwise distance, and no bound on M or w is assumed.

Proof. The exact energy identity makes the loss decrease to a limit and
gives integral_{t_0}^infty ||c'(t)||_2^2 dt<infinity. Hence there are times
t_n tending to infinity with ||c'(t_n)||_2 tending to zero. By Section 3,
pass to a common subsequence along which all three signed fields V_i(t_n)
converge strongly in L2 to limiting fields V_i^*. The readout bound (2)
bounds the three margins, so pass to a further subsequence with m_i(t_n)
converging to m_i^*.

Put ell=L(t_0)<1/3. Every reached margin obeys

\[
                 m_i(t)\ge1-\sqrt{3\ell}>0.             \tag{3}
\]

If V_i^*=0, the bound |m_i(t_n)|<=||c(t_n)||_2||V_i(t_n)||_2 would force
m_i^*=0, contradicting (3). If V_i^*=-V_j^*, the bound

\[
 |m_i(t_n)+m_j(t_n)|
 \le\|c(t_n)\|_2\|V_i(t_n)+V_j(t_n)\|_2
\]

would force m_i^*=-m_j^*, again contradicting (3). If V_i^*=V_j^*,
the same bound with differences shows m_i^*=m_j^*.

Passing to the limit in the finite sum (1), using strong field convergence
and convergent scalar margins, gives

\[
                  \sum_i(1-m_i^*)V_i^*=0.
\]

Group identical fields. There are no zero or opposite fields. By Section 3
the remaining group fields are independent; within each group the margins
are equal. Therefore every margin equals one. The loss at t_n tends to
zero. Its nonincreasing limit is consequently zero, proving the theorem.

For each positive tolerance the conclusion supplies a finite attainment
time by the definition of convergence. It supplies no evaluated rate,
finite parameter endpoint or full-state convergence. Such claims would
need further estimates. The result is conditional on both finite-time
entry below 1/3 and the all-time readout bound; neither is proved for every
generic initialized unit-label triple.

## 5. Relation to the desired mixed potential

The user clarified that a potential may mix attractive and repulsive
effects while individual distances move either way. Nothing above imposes
pairwise monotonicity. The stationary alternatives and compactness theorem
identify useful geometry that a successful mixed potential could control:
avoid loss-persisting degeneration of signed upper features and control
readout growth. The norm can be bounded jointly with separation; the
separate mixed inequalities in generic3_metric_second_pass.md quantify
that tradeoff below the same loss threshold.

The initialized same-class expansion theorem is only a stress test, not
a counterexample to this desired mixed potential or to fitting. No
configuration with proved failure of convergence has been constructed.
Failure to close the remaining estimates says nothing about whether
such a potential exists. Exact zero loss at finite time is also not the
target: convergence to every positive tolerance is the relevant claim.

## Checks and scope

Root reconstructed the canonical mark parity and upper normalization,
checked all three coefficients of tanh used in the Vandermonde argument,
included equal-vector groups explicitly, verified every finite and
saturated feature limit, and proved the required subsequence conclusion
without assuming compactness of the weight state or taking a strong limit
of the readout. The proof needs only bounded readout, not a weak readout
limit, because the three scalar margins can be extracted directly.
The independent post-freeze compactness check has its own full report.

This is a rigorous restricted result, not the requested unconditional
generic convergence theorem and not a state-only decaying potential.
The exact primary missing implications are now visible: why every generic
initialized unit-label trajectory enters a sufficiently low-loss region,
and why a suitable combined geometric bound prevents loss-persisting
unbounded-readout escape. Neither is replaced by initial Gram positivity.
