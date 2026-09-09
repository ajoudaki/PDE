# Fractional gate estimate at the prescribed canonical tiny readout

Candidate scoped corollary, pending isolated audit. This combines the
direct positive-time rare-path estimates in
CANONICAL_TINY_READOUT_RARE_PATH.md with a finite fractional selection
argument. It uses the prescribed independent \(W^{(4)}_0=G^{(4)}/n\)
in both the full and every fully pruned network. It neither compares
with an evolved zero-readout flow nor asserts global population
continuation.

Fix \(S,M,n,\eta\), the prescribed common dominated 1-Lipschitz clipping
\(\tau\), and the event of that dependency. The identity map gives the
uncut case. Use its actual query \(q^{(2)}\), coordinatewise maximal
path \(q^{(2)}_*\), squared state distances \(y_E\), and envelopes
\(Y_r=\max_{|E|\le\lfloor nr\rfloor}y_E\). In particular,
\(Y_r=0\) for \(r<1/n\); there is no time supremum in \(Y_r\).
Its functions are
\[
h(a)=a\log(e/a),\qquad
\Phi(y)=y[1+\tfrac12\log_+(1/y)],
\]
with zero values at zero. Choose \(C_0\ge1\) such that its gate mass
satisfies \(a_E\le A(y_E):=\min\{1,C_0y_E\}\). Constants below depend
only on \(S,M\), including this fixed \(C_0\), not on width, deletion,
weights, or the level of the one prescribed clipping.

For \(0\le a<1\), write \(na=k+\theta\), \(k=\lfloor na\rfloor\),
\(0\le\theta<1\), and define
\[
\mathcal I_n(a,u)=(1-\theta)\Phi(Y_{k/n}(u))
                   +\theta\Phi(Y_{(k+1)/n}(u)).
\tag{1}
\]
Set \(\mathcal I_n(1,u)=\Phi(Y_1(u))\).
This interpolates the values of \(\Phi\), not the paths before applying
\(\Phi\). It is nonnegative and nondecreasing in \(a\), since its
node values are. It is zero at \(a=0\).

For every \(0\le w_i\le1\), however selected from the actual paths,
with \(a=n^{-1}\sum_i w_i\), the direct canonical query estimate is
\[
\frac1n\sum_i w_i q^{(2)}_{*,i}(t)^2
\le C\left[
(t^2+n^{-2})\{h(a)+\epsilon_n^2\min(1,na)\}
+t\int_0^t\mathcal I_n(a,u)\,du\right].
\tag{2}
\]
To see this, sort \(q^{(2)}_{*,i}(t)^2\) as
\(b_1\ge\cdots\ge b_n\ge0\), and put \(B_j=n^{-1}\sum_{i=1}^j b_i\),
including \(B_0=0\). Reordering the weights accordingly gives
\[
\sum_i w_ib_i=(k+\theta)b_{k+1}
                   +\sum_iw_i(b_i-b_{k+1})
\le\sum_{i=1}^k b_i+\theta b_{k+1}.
\]
Thus the weighted sum divided by \(n\) is at most
\((1-\theta)B_k+\theta B_{k+1}\). At \(a=1\) use \(B_n\);
at \(a=0\) the sum is zero. Apply the dependency's prefix estimate
(35) to each positive grid size, and keep \(B_0=0\) exactly.
Concavity of \(h\) gives the entropy \(h(a)\).
The width coefficient is
\((1-\theta)\mathbf1_{\{k\ge1\}}+\theta=\min(1,na)\).
The history becomes (1), with the present mass \(a\) fixed throughout
the inner integral. This proves (2). In particular when \(0<a<1/n\),
the history is \(na\,\Phi(Y_{1/n}(u))\), not zero.

Write the actual uncompressed gate vector as
\[
v_E=Q_E[\phi'(z^{(2)})-\phi'(\widehat z^{(2)})]
                         \odot\tau(\widehat q^{(2)}),
\qquad
a_E=\frac1n\sum_{i\notin E}
 |\phi'(z_i^{(2)})-\phi'(\widehat z_i^{(2)})|^2.
\]
The weights here belong to \([0,1]\). The dependency's (39), followed
by (2), proves, with \(p_E=|E|/n\),
\[
\begin{split}
\frac{\|v_E(t)\|_2^2}{n}\le C\bigg[
&y_E(t)+p_E+
(t^2+n^{-2})\{h(a_E(t))+\epsilon_n^2\min(1,na_E(t))\}\\
&+t\int_0^t\mathcal I_n(a_E(t),u)\,du\bigg].
\end{split}
\tag{3}
\]
No independence of these gate weights and the query is required:
the finite selection inequality holds for every weight vector on
the single common event. Every mass-dependent expression in (3)
is nondecreasing. One can therefore replace \(a_E(t)\) throughout
by \(A(y_E(t))\).

The resulting finite comparison hierarchy is
\[
\begin{split}
Y_p(t)\le C\bigg[
&t\{h(p)+\epsilon_n^2\}+\int_0^t\Phi(Y_p(s))\,ds\\
&+\int_0^t\left\{Y_p(s)s\int_0^s
          \mathcal I_n(A(Y_p(s)),u)\,du\right\}^{1/2}\,ds
\bigg].
\end{split}
\tag{4}
\]
Here is the absorption, including the nonzero initialization.
The dependency's (34) gives
\(I_E\le Cn^{-2}[h(p_E)+\epsilon_n^2]\) for nonempty \(E\),
and \(I_\varnothing=0\). Thus its state estimate (38) implies
\[
y_E(t)\le C\left[
t\{h(p_E)+\epsilon_n^2\}+\int_0^t\Phi(y_E(s))\,ds
+\int_0^t\sqrt{y_E(s)}\,\frac{\|v_E(s)\|_2}{\sqrt n}\,ds
\right].
\tag{5}
\]
For \(y\ge0\) one has
\(\sqrt{y\,h(A(y))}\le\sqrt{C_0}\Phi(y)\). Indeed if
\(0<C_0y\le1\), put \(L=\log(1/y)\ge0\) and use
\(h(C_0y)\le C_0y(1+L)\) and
\(\sqrt{1+L}\le1+L/2\). If \(C_0y\ge1\), use
\(h(A(y))=1\), \(\sqrt y\le\sqrt{C_0}y\), and \(\Phi(y)\ge y\).
At zero the inequality is exact.

Taking the square root term by term in (3), multiplying by
\(\sqrt y\), using \(\sqrt{s^2+n^{-2}}\le s+n^{-1}\le S+1\),
and applying Young's inequality gives
\[
\sqrt y\,\frac{\|v_E(s)\|_2}{\sqrt n}
\le C\left[
\Phi(y)+p_E+\epsilon_n^2+
\left\{ys\int_0^s\mathcal I_n(A(y),u)\,du\right\}^{1/2}\right],
\quad y=y_E(s).
\tag{6}
\]
The entropy with coefficient \(n^{-1}\) is included in the displayed
modulus, not thrown away. For the width term use
\(\epsilon_n\sqrt y\,\sqrt{\min(1,nA(y))}
\le (y+\epsilon_n^2)/2\).
The factor \(s\) in the history remains unchanged. Substituting in
(5), and using \(p_E\le h(p_E)\), gives (4) first for an individual
set. For fixed \(s\), the last expression in braces in (6) is
nondecreasing in \(y\): both \(y\) and the nonnegative inner integral
are nondecreasing. Replace each \(y_E(s)\) by \(Y_p(s)\) for
\(|E|\le\lfloor np\rfloor\), then take the finite maximum.
This justifies (4) without choosing a common maximizing set in time.
For \(p<1/n\) the left side is zero; at \(t=0\) all state terms
vanish, while (2) correctly retains the initial query mass.

All estimates have the dependency's probability at least
\[
1-\eta-\mathbb P(\Omega_M^c)
-e^{-(1-\frac12\log2)n}-2n e^{-n^2/2}.
\]
No new probability event has been added. Uniform constants for one
prescribed clipping do not assert a simultaneous event over all
clipping choices. With \(M=10,\eta=1/n\), the failure probability
tends to zero and \(\epsilon_n\to0\).

This is a direct canonical positive-time hierarchy with all trained
parameter blocks retained. Its history still evaluates the deletion
envelope at a mass determined by the current error, not by the
original deletion fraction. No assertion that (4) forces deletion
continuity, clipping removal, unique population restartability, or the
requested global theorem is made.

Explicit mathematical dependency:
CANONICAL_TINY_READOUT_RARE_PATH.md, including its finite definitions,
common-event theorem, equations (34), (35), (38), and (39).
The fractional selection and every new implication are proved here.
No scalar obstruction, master ledger, prior review, or finite-jet
result is used as mathematical input.
