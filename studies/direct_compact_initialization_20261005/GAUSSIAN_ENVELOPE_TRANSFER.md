# Transferring pointwise envelopes through Gaussian source selection

2026-10-06. **Proved functional transfer lemma, conditional on the supplied
pointwise envelopes and effective source basis.** Adding one envelope
function per source family to the selection space controls all selected
residuals in the corrected metric. No label assumption, training theorem,
or dense-network comparison is used or proved.

This note uses the complete frozen
[Gaussian synthetic selection theorem](GAUSSIAN_SYNTHETIC_SELECTION.md),
SHA-256
3eb17a6963242bf9336e645a203fd6e67983e626de0ef39a85d917cb44a9e384.
Its proof-skill, notation, and disclosed canonical-skill fallback conditions
are retained. No undocumented envelope construction from another agent is
assumed. The frozen selection file is unchanged.

## 1. Setup and selected-residual theorem

Let $\mu$ be standard Gaussian probability on $\mathbb R^k$, with a
degenerate Gaussian first parameterized on its support if necessary. Let
$S$ be a finite-dimensional space of continuous real functions in
$L^2(\mu)$. For an arbitrary index set $\mathcal I$, suppose functions
$u_\theta$ and source approximants $s_\theta\in S$ are given for every
$\theta\in\mathcal I$. For example, an index may contain both time and
input; no discretization of this index set is used below.

Assume a known continuous nonnegative function $e\in L^2(\mu)$ satisfies
the pointwise envelope inequality

$$
|u_\theta(z)-s_\theta(z)|\le e(z)
\quad\text{for every }\theta\in\mathcal I
\text{ and every }z\in\mathbb R^k,
\qquad
\|e\|_{L^2(\mu)}\le\varepsilon.                     \tag{1}
$$

For several source families, assume one such envelope for each family.
Form the augmented source space

$$
S_+=\operatorname{span}(S,1,e_1,\ldots,e_J),
\qquad r=\dim S_+.                                 \tag{2}
$$

Choose an orthonormal continuous basis $p_1,\ldots,p_r$ of $S_+$ in
$L^2(\mu)$. Apply the frozen selection theorem to this basis, under its
stated effective moment and evaluation hypotheses. It supplies
$N\le16r$ marks $z_i$, the evaluation matrix $P_{ij}=p_j(z_i)$, and
positive definite $H$ and positive diagonal $D$ satisfying

$$
P^THP=I_r,\qquad \frac14D\preceq H\preceq D.        \tag{3}
$$

For any pointwise defined function $v$, write
$v_I=(v(z_1),\ldots,v(z_N))^T$ and
$\|v_I\|_H=\sqrt{v_I^THv_I}$. Exact isometry on $S_+$ says

$$
s_I^THt_I=\int st\,d\mu\qquad(s,t\in S_+).
                                                               \tag{4}
$$

Then the entire family in (1) satisfies

$$
\sup_{\theta\in\mathcal I}
\|(u_\theta-s_\theta)_I\|_H
\le2\|e\|_{L^2(\mu)}
\le2\varepsilon.                                  \tag{5}
$$

**Proof.** Fix any $\theta$ and put $\delta=u_\theta-s_\theta$. The
diagonal structure of $D$ and the pointwise envelope give

$$
\begin{aligned}
\|\delta_I\|_H^2
&\le \delta_I^TD\delta_I\\
&\le e_I^TDe_I\\
&\le4e_I^THe_I\\
&=4\|e\|_{L^2(\mu)}^2.
\end{aligned}
$$

The first and third inequalities use (3), and the last equality uses
$e\in S_+$ and (4). No coordinatewise monotonicity of the generally
non-diagonal matrix $H$ was assumed. The right side is independent of
$\theta$, proving (5). This proof also covers $e=0$ without division by
the envelope. The original residual obeys
$\|\delta\|_{L^2(\mu)}\le\varepsilon$ directly from (1).

## 2. Pairing error with explicit constants

Let $u=s+\delta$ and $v=t+\gamma$, with $s,t\in S_+$ and

$$
\|s\|_{L^2(\mu)}\le A,\qquad
\|t\|_{L^2(\mu)}\le B.
$$

Suppose their two pointwise residual envelopes have been included in the
same augmented selection space and have $L^2$ norms at most
$\varepsilon$ and $\eta$, respectively. Then

$$
\left|u_I^THv_I-\int uv\,d\mu\right|
\le3A\eta+3B\varepsilon+5\varepsilon\eta.            \tag{6}
$$

**Proof.** By (4), the source-source terms cancel. Expanding the
remaining terms gives

$$
\begin{aligned}
u_I^THv_I-\int uv\,d\mu
={}&\left(s_I^TH\gamma_I-\int s\gamma\,d\mu\right)\\
&+\left(\delta_I^THt_I-\int\delta t\,d\mu\right)\\
&+\left(\delta_I^TH\gamma_I-\int\delta\gamma\,d\mu\right).
\end{aligned}
$$

The source norms at the marks equal their population norms by (4).
Equation (5) bounds the selected residual norms by $2\varepsilon$ and
$2\eta$, while (1) bounds their population norms by $\varepsilon$ and
$\eta$. Cauchy--Schwarz in the two inner-product spaces bounds the three
displayed brackets in absolute value by

$$
2A\eta+A\eta,\qquad
2B\varepsilon+B\varepsilon,\qquad
4\varepsilon\eta+\varepsilon\eta,
$$

respectively. Their sum is (6). This estimate is uniform over any index
sets for which the same envelopes and source norm bounds hold.

For bounded tanh features, in particular initial features, suppose
$|u(z)|,|v(z)|\le1$ and the two envelope norms are at most a common
$\varepsilon$. The triangle inequality gives

$$
\|s\|_{L^2(\mu)},\ \|t\|_{L^2(\mu)}\le1+\varepsilon.
$$

Consequently (6) specializes to

$$
\left|u_I^THv_I-\int uv\,d\mu\right|
\le6\varepsilon+11\varepsilon^2.                  \tag{7}
$$

This applies to any pair in a uniformly enveloped feature family. For
$m$ such features, the difference between the selected Gram and the
population Gram has operator norm at most
$m(6\varepsilon+11\varepsilon^2)$: for any unit vectors $a,b$,
the corresponding bilinear form is bounded by the maximum entry error
times $\|a\|_1\|b\|_1\le m$. Thus division of these Grams by $m$
removes that factor. This is a Gram estimate only; no training conclusion
is being inferred.

## 3. Rank, evaluation, and computability requirements

The dimension bound is algebraic:

$$
r\le\dim S+1+J,
$$

or $r\le\dim S+J$ if the constant function is already in $S$. Each
envelope adds at most one basis dimension, even if it controls
uncountably many times and inputs. It may add none if it is already in
the source span.

For an explicit orthonormalization step, given an orthonormal basis
$p_1,\ldots,p_q$ of the current space, define

$$
e_\perp=e-\sum_{j=1}^q
\left(\int ep_j\,d\mu\right)p_j.
$$

If $\|e_\perp\|_{L^2(\mu)}>0$, append
$e_\perp/\|e_\perp\|_{L^2(\mu)}$; if it is zero, the span is unchanged.
In either case the **original envelope $e$**, rather than just its
orthogonal remainder, belongs to the resulting span, as needed in the
proof of (5).

The effective construction must know an independent basis and be able
to certify its positive Gram eigenvalue bound, or possess exact
dependency certificates for discarded functions. Equality to zero of an
arbitrary computable real is not generally decidable, so a numerical
rank cutoff does not establish this requirement. Near dependence may
increase conditioning and arithmetic precision even though it adds at
most one scalar basis direction. The mathematical dimension statement
does not give a uniform rank-discovery or bit-complexity algorithm.

Every retained source and envelope must have computable point
evaluations, effective uniform bounds and moduli on bounded Gaussian
parameter boxes, and effective second-moment tails. These hypotheses
permit the moment integrals and finite quadrature used by the selection
theorem. For a certified finite independent basis, they pass to its
orthonormalization by finite linear combinations, with the actual
conditioning factors accounted for. The envelope and its accuracy bound
must be computable from the permitted source information; defining
$e(z)$ as an inaccessible supremum of unknown trajectory errors does
not provide an initializer.

The pointwise assumption in (1) matters. A bare $L^2$ bound on
$u_\theta-s_\theta$ does not control its values at finitely many
deterministic marks. If the true functions, their approximants, and
the envelope are all continuous on Gaussian support, then an
almost-everywhere inequality for each index implies the same inequality
everywhere: a strict violation would persist on an open set of positive
Gaussian measure. This provides one legitimate way to obtain (1).
Without such a pointwise extension, the bounds must at least be known
at every mark the selection may choose.

## 4. Resource increment and scope

Reselecting on the augmented space gives at most
$16(\dim S+1+J)$ neurons, and corrected metric storage of order
$(\dim S+1+J)^2$. For a fixed number of envelopes and an already
included constant, the increase in this quadratic storage upper bound
is $O(J\dim S+J^2)$. The selection is rerun on the augmented space;
the proof does not assert that the old selected marks can be retained
and repaired by adding only one mark per envelope.

The bound is on basis dimension and final selected size. Source program
descriptions, retained Gaussian mark coordinates, setup quadrature,
conditioning, and numerical precision keep the separate accounting
requirements of the frozen selection theorem. Two populations may use
the lemma separately, but a pairing across distinct populations still
needs the specified cross operator or cross-pairing matrix; it is not
created by independent selections.

This note supplies no analytic-envelope construction, no estimate on
forward/transpose closure defects, and no propagation bound for a
trained network. Those inputs can be combined with this lemma only
after their pointwise, effective, and uniformity assumptions have been
proved. No assumption on labels is needed for the statements here.

This author result is frozen at handoff; its hash is reported separately.
