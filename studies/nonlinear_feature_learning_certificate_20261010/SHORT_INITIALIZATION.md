# Two-pass initialization lemma

Scoped replacement for the initialization argument in the compact proof. The
passage below uses the preceding input-kernel lemma only for
\(Q^{(\ell)}\succ0\), \(\ell\ge1\). It does not claim empirical limits for
preactivation or feature accelerations beyond the first layer.

```latex
\begin{lemma}[Initial backward fields and positive block energies]
\label{fl:initial-activity}
Under the additional theorem's hypotheses, each layer's initial forward,
pre-gated backward, and gated backward fields have deterministic joint
empirical row-law limits in quadratic Wasserstein distance, in probability.
At layer one this includes the full initial weight and weight-acceleration
rows. Each hidden block's squared weight acceleration in inverse-mobility
norm converges in probability and in $L^1$ to a strictly positive constant.
The retained fields' squared RMS norms and the block energies are uniformly
integrable; the retained row tuples' squared-coordinate tails are uniformly
integrable in probability.
\end{lemma}

\begin{proof}
All network fields below are at initialization. Put $k=2/m$ and define
\begin{align*}
 P_a^{(L)}&=\sum_b y_bh_b^{(L)},&
 B_a^{(\ell)}&=\phi_\ell'(z_a^{(\ell)})\odot P_a^{(\ell)},&
 P_a^{(\ell)}&=W_0^{(\ell+1)\top}B_a^{(\ell+1)}\quad(\ell<L).
\end{align*}
Since hidden velocities vanish at zero, differentiating the physical flow
gives $\dot\delta_a^{(\ell)}(0)=kB_a^{(\ell)}$ and, with
$V_\ell=\ddot W^{(\ell)}(0)$,
\[
 V_1=k^2\sum_a y_aB_a^{(1)}v_a^\top,\qquad
 V_\ell=\frac{k^2}{n}\sum_a y_aB_a^{(\ell)}
 h_a^{(\ell-1)\top}\quad(\ell\ge2).
\]
The mobility norms are $\|V_1\|_F/\sqrt n$ and $\|V_\ell\|_F$
for $\ell\ge2$.

Expose the iid roots $g_i=W_{0,i:}^{(1)}$, all forward matrix actions in
increasing layer order, and then all reverse actions in decreasing order.
At a reverse call, set $H=[h_a^{(\ell)}]$, $Z=[z_a^{(\ell+1)}]$,
$U=[B_a^{(\ell+1)}]$, and
$Q_n=H^\top H/n$, $C_n=Z^\top U/n$, $D_n=U^\top U/n$.
On invertible $Q_n$, orthogonal Gaussian projection onto the already
observed constraint $WH=Z$ gives exactly
\begin{gather*}
 W^\top U\overset d=HQ_n^{-1}C_n+(I-\Pi_H)\Xi D_n^{1/2},
 \qquad \Pi_H=H(H^\top H)^{-1}H^\top,\\
 \mathbb E\!\left[\frac{\|\Pi_H\Xi D_n^{1/2}\|_F^2}{n}
       \,\middle|\,\mathrm{past}\right]
       =\frac{\operatorname{rank}H}{n}\operatorname{tr}D_n,
\end{gather*}
where $\Xi$ has iid standard Gaussian entries independent of the past.
This conditioning is valid adaptively: every query is determined by earlier
answers, and exposing its linear Gaussian projection leaves the orthogonal
residual independent of the other matrices' residuals. In this chronology
the present matrix has had exactly its forward call before its reverse call.

For completeness, appending independent Gaussian rows preserves a
deterministic empirical $\mathcal W_2$ limit: bounded-test conditional
variances are $O(n^{-1})$, their conditional means converge by the old
empirical law, and the Gaussian second moment converges. Continuous maps
of at most linear growth preserve $\mathcal W_2$ convergence by truncation
and uniform integrability of squared inputs. These rules cover the
Lipschitz activations, bounded derivative gates, and convergent linear
coefficients; same-layer second moments therefore converge. Positive
matrix square roots are continuous even at singular covariances. Thus the
forward pass gives $Z^{(\ell)}\sim N(0,Q^{(\ell-1)})$ and
$H_a^{(\ell)}=\phi_\ell(Z_a^{(\ell)})$. The input-kernel lemma gives
$Q^{(\ell)}\succ0$ for $\ell\ge1$; $Q^{(0)}$ is never inverted.

Write $\mathsf P,\mathsf B$ for limiting backward rows and
$D^{(\ell)}=\mathbb E[\mathsf B^{(\ell)}\mathsf B^{(\ell)\top}]$.
The top fields are continuous maps of at most linear growth. Downward
induction in the displayed conditional law gives
\[
 \mathsf P^{(\ell)}=((Q^{(\ell)})^{-1}C)^\top H^{(\ell)}+\Gamma,
 \quad C_{ba}=\mathbb E[Z_b^{(\ell+1)}\mathsf B_a^{(\ell+1)}],
 \quad \Gamma\sim N(0,D^{(\ell+1)}),
\]
with $\Gamma$ independent of the lower-layer forward tuple, including $g$
at layer one. The removed projection vanishes in RMS by its displayed
conditional expectation. The inverse Grams converge on events of
probability tending to one. Gating gives $\mathsf B^{(\ell)}$, and the
linear formula for $V_1$ retains its joint row law with $g$.

These backward Grams are positive definite. Since $L\ge2$,
$Q^{(L-1)}\succ0$, so a null vector $c$ of $D^{(L)}$ would imply
\[
 \Big(\sum_b y_b\phi_L(z_b)\Big)
 \Big(\sum_a c_a\phi_L'(z_a)\Big)=0\qquad(z\in\mathbb R^m).
\]
The first factor is not identically zero because $y^\top Q^{(L)}y>0$.
Analyticity makes the second factor identically zero; varying one coordinate
and using nonaffinity gives $c=0$. At each lower layer, conditional variance
in the preceding Gaussian formula gives
\[
 c^\top D^{(\ell)}c\ge\lambda_{\min}(D^{(\ell+1)})
       \sum_a c_a^2\mathbb E[\phi_\ell'(Z_a^{(\ell)})^2]>0
       \quad(c\ne0).
\]
Each marginal $Z_a^{(\ell)}$ is a nondegenerate Gaussian, and the nonzero
analytic derivative vanishes only on a discrete set.

Let $Q_n^{(0)}=Q^{(0)}$ and let $Q_n^{(j)}$ be the empirical feature
Grams. The exact outer-product formulas give, with $\circ$ denoting
entrywise multiplication,
\[
 \|V_\ell\|_{\rm mob}^2
 =k^4y^\top\!\left(Q_n^{(\ell-1)}\circ
             \frac{[B_a^{(\ell)}]^\top[B_a^{(\ell)}]}n\right)y
 \longrightarrow e_\ell
 =k^4y^\top(Q^{(\ell-1)}\circ D^{(\ell)})y>0.
\]
Indeed $Q\succeq0$, $D\succ0$ imply
$Q\circ D\succeq\lambda_{\min}(D)\operatorname{diag}(Q)$ by writing
$Q=\sum_jq_jq_j^\top$ and using
$Q\circ D=\sum_j\operatorname{diag}(q_j)D\operatorname{diag}(q_j)$.
Every relevant $Q$ has positive diagonal, including $Q^{(0)}$.

Finally $M_n=1+\|W_0^{(1)}\|_F/\sqrt n+
\sum_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}$ has uniformly bounded
moments of every fixed order, by Gaussian moments and the two-net Gaussian
operator tail in the fitting lemma. Linear activation growth and bounded
gates bound every displayed field RMS and mobility norm by a fixed
polynomial in $M_n$. This proves uniform integrability and the claimed
$L^1$ energy limits; empirical $\mathcal W_2$ convergence gives the
squared-coordinate tail assertion.
\end{proof}
```

## Dependency and call audit

- There are exactly \(2(L-1)\) hidden-matrix calls. The inverse matrices are
  only \(Q_n^{(\ell)}\), \(\ell\ge1\). There is no inverse of the possibly
  singular input Gram or of a backward Gram.
- A third call becomes necessary only if the proof insists on a deterministic
  empirical law for \(W_0^{(\ell)}\ddot h^{(\ell-1)}(0)\). None of the
  initialization conclusions above use that quantity.
- The omitted feature-acceleration positivity argument can be replaced
  downstream by the exact identity
  \[
  \sum_a\frac{y_a}{n}P_a^{(\ell)\top}\ddot h_a^{(\ell)}(0)
  =\frac1{k^2}\sum_{j\le\ell}\|V_j\|_{\rm mob}^2.
  \]
  It follows by \(\ddot h_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})
  \odot\ddot z_a^{(\ell)}\), the exact forward acceleration recursion,
  and the backward transpose relation. Its right side is positive and its
  pairing involves only the retained pre-gated fields. Cauchy--Schwarz gives
  a feature-acceleration lower bound, because these fields have bounded RMS.
  To propagate such a certificate to fixed small times with rowwise
  derivative gates, use the retained fields' squared-coordinate tail control
  and a deterministic truncation estimate. This needs no third Gaussian call.
- The required positive feature Grams can also be justified without further
  research input: the first activation has infinitely many nonzero Hermite
  degrees (a polynomial with bounded derivative would be affine), and
  \(|Q^{(0)}_{ab}|<1\) for \(a\ne b\), so a sufficiently high active
  Hadamard power is strictly diagonally dominant. It follows that
  \(Q^{(1)}\succ0\). At later layers, full Gaussian support and the
  nonconstant activation imply positive definiteness by varying one
  coordinate in any putative null combination. The replacement cites the
  input-kernel lemma to avoid repeating this argument.

The shorter statement deliberately drops deterministic limits for all-layer
feature accelerations. Any downstream citation requiring those limits must
instead use the pre-gated pairing identity and tail control above.
