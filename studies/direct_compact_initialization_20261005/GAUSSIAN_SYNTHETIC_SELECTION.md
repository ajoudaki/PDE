# Direct Gaussian source selection with linear neuron count

2026-10-06. **Proved finite source-selection theorem, conditional on the
supplied computable source functions and cross pairings.** A source space of
dimension $R$ under a finite-dimensional Gaussian law admits a directly
constructed selection of at most $16R$ synthetic marks. A corrected,
generally non-diagonal metric preserves its true source inner products
exactly. Two such selections and a supplied cross-pairing matrix require
$O(R^2)$ retained metric/mixer entries. This is not a dense-network
approximation theorem or a construction of the required neural sources.

This scoped author contribution read current AGENTS.md, the maintained
notation contract, and the complete authorized
[quadratic-storage source](../closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md).
The proof and conjecture-investigation skills were applied. The required
canonical-notation skill remains permission denied; the previously
authorized explicit-notation fallback is retained. No other study was
inspected. The BSS primary theorem and its complete pertinent proof units
were read under the supervisor's explicit authorization. No experiment,
test, Git operation, or dense initialization was performed.

## 1. The source contract and theorem

Let $\mu$ be standard Gaussian probability on $\mathbb R^k$, where $k$ is
finite. A known computable Gaussian affine change of variables can be
included in the source program; a degenerate Gaussian is parameterized on
its support. Let

$$
p:\mathbb R^k\longrightarrow\mathbb R^R
$$

be a continuous computable function satisfying the exact identity

$$
\int p(z)p(z)^T\,d\mu(z)=I_R.                         \tag{1}
$$

Assume the constant function belongs to the span of its coordinates:
there is $c\in\mathbb R^R$ with $c^Tp(z)=1$ $\mu$-almost everywhere.
Continuity and Gaussian full support imply this equality at every
parameter point. Equation (1) gives $\|c\|_2=1$.

For an explicit quadrature construction, assume effective bounds for

$$
\int_{\|z\|_\infty>L}\|p(z)\|_2^2\,d\mu(z)
$$

as $L$ increases, and effective uniform evaluation, bounds, and moduli of
continuity of $p$ on bounded boxes. These are numerical input requirements,
not consequences of the phrase “finite second moments” alone.

Then a deterministic procedure using only this source program and Gaussian
integration can construct $N\le16R$ marks $z_1,\ldots,z_N$, the evaluation
matrix $P\in\mathbb R^{N\times R}$ with rows $p(z_i)^T$, and a positive
diagonal matrix $D\in\mathbb R^{N\times N}$ such that

$$
I_R\preceq G:=P^TDP\preceq4I_R.                    \tag{2}
$$

Indeed, the existence proof gives the stronger margins
$21I_R/20\preceq G\preceq15I_R/4$ before optional rational rounding of
the positive weights. The marks can be chosen as rational grid points.
They are deterministic quadrature marks in the Gaussian parameter space;
they are not asserted to be independent Gaussian samples.

Set $Z=D^{1/2}P$ and define

$$
H=D^{1/2}\left[
ZG^{-2}Z^T+I_N-ZG^{-1}Z^T
\right]D^{1/2}.                                    \tag{3}
$$

This positive definite metric satisfies

$$
\frac14D\preceq H\preceq D,\qquad P^THP=I_R.         \tag{4}
$$

Thus for every pair of coefficient vectors $a,b\in\mathbb R^R$,

$$
(Pa)^TH(Pb)
=a^Tb
=\int (a^Tp(z))(b^Tp(z))\,d\mu(z).                 \tag{5}
$$

The finite Gaussian quadrature in the proof is only a means of selecting
the marks. Its integration error does not appear in the exact identity
(5), because (1) is an exact hypothesis and (3) corrects the selected
Gram algebraically.

## 2. Proof of the selection theorem

The proof first obtains a finite positive quadrature with a constant
accuracy margin, whitens that finite frame, and sparsifies it with enough
spectral slack to absorb the quadrature error.

Choose a box so that its omitted second-moment tail is at most $1/16$.
Partition that box into finitely many small rectangular cells and choose
a rational mark in each cell. Give the mark the Gaussian mass of its
cell. If $\|p\|_2\le M$ on the box, then

$$
\|p(z)p(z)^T-p(z')p(z')^T\|_{\mathrm{op}}
\le2M\|p(z)-p(z')\|_2.
$$

Uniform continuity makes the quadrature error inside the box at most
$1/16$. The effective assumptions let the procedure certify these choices.
Finite evaluation and cell-weight rounding can be included by assigning
smaller initial error budgets. Consequently it can produce positive
weights $\alpha_j$ and marks $\zeta_j$, $1\le j\le J$, for which

$$
M_Q=\sum_{j=1}^J\alpha_jp(\zeta_j)p(\zeta_j)^T,\qquad
\|M_Q-I_R\|_{\mathrm{op}}\le\frac18.                 \tag{6}
$$

No bound on $J$ in terms of $R$ alone is claimed. In particular, a tensor
grid may be expensive in the mark dimension $k$.

The imported spectral sparsification statement is the general-vector BSS
theorem: for finitely many $v_j\in\mathbb R^R$ with
$\sum_jv_jv_j^T=I_R$, and a parameter $b>1$, nonnegative coefficients
$s_j$ supported on at most $bR$ indices exist such that

$$
I_R\preceq\sum_js_jv_jv_j^T
\preceq
\left(\frac{\sqrt b+1}{\sqrt b-1}\right)^2 I_R.
$$

We use integer $b=16$. This is Theorem 3.1 of
[Batson, Spielman, and Srivastava, *Twice-Ramanujan Sparsifiers*](https://www.cs.cmu.edu/~odonnell/hits09/batson-spielman-srivastava-twice-ramanujan-sparsifiers.pdf),
with the rank-one inverse preliminary in Section 2.3 and the full
barrier proof in Section 3.2. In this specialization, the lower and upper
shifts are $1,5/3$, the potential caps are $1/4,3/20$, and the initial
barriers are $-4R,20R/3$. The averaging condition is
$3/5+3/20=1-1/4$. After $16R$ steps the barriers are $12R,100R/3$;
division by $12R$ gives the factor $25/9$.

The hypotheses hold exactly for

$$
v_j=\sqrt{\alpha_j}\,M_Q^{-1/2}p(\zeta_j),
$$

because (6) makes $M_Q$ positive definite and
$\sum_jv_jv_j^T=M_Q^{-1/2}M_QM_Q^{-1/2}=I_R$. Congruence by
$M_Q^{1/2}$ in the BSS conclusion gives

$$
M_Q\preceq
\sum_js_j\alpha_jp(\zeta_j)p(\zeta_j)^T
\preceq\frac{25}{9}M_Q.
$$

Retain the positive support and set $D_{jj}=(6/5)s_j\alpha_j$ there.
Using $7I_R/8\preceq M_Q\preceq9I_R/8$ yields

$$
\frac{21}{20}I_R
\preceq P^TDP
\preceq\frac{15}{4}I_R.                             \tag{7}
$$

This proves (2) with $N\le16R$. It also explains why applying only the
$9R$, condition-factor-four specialization to an approximately normalized
quadrature is insufficient for the exact constants in (2): its additional
quadrature distortion would generally exceed four. The choice $16R$
provides room for that distortion.

To prove (4), $ZG^{-1}Z^T$ is the orthogonal projector onto
$\operatorname{range}(Z)$. On that range, $ZG^{-2}Z^T$ has eigenvalues
equal to the eigenvalues of $G^{-1}$; on its orthogonal complement the
bracket in (3) is the identity. Its spectrum is therefore in $[1/4,1]$.
Congruence by $D^{1/2}$ proves the metric comparison. Finally,

$$
P^THP=GG^{-2}G+G-GG^{-1}G=I_R,
$$

which proves the exact source isometry and completes the proof.

Two useful consequences require no new assumptions. Since $Pc=\mathbf1$,

$$
1\le\mathbf1^TD\mathbf1\le4,\qquad
\mathbf1^TH\mathbf1=1.
$$

Hence an arbitrary selected coordinate error with
$\|e\|_\infty\le\varepsilon$ satisfies
$\sqrt{e^THe}\le2\varepsilon$. Also, for any diagonal multiplier
$A=\operatorname{diag}(a_i)$,

$$
\|Au\|_H\le2\max_i|a_i|\,\|u\|_H,
\qquad \|u\|_H:=\sqrt{u^THu}.
$$

Indeed $H\preceq D$, $A^TDA\preceq(\max_i|a_i|)^2D$, and
$D\preceq4H$. These constants do not depend on the smallest selected
weight.

## 3. Effective deterministic construction and its actual cost

The BSS construction is deterministic in exact-real arithmetic. For a
finite pool of $J$ known vectors, its displayed implementation takes
$O(JR^3)$ arithmetic operations for this fixed parameter, in addition to
source evaluation and forming/whitening the quadrature matrix. This
operation count does not bound source-evaluation cost or finite-precision
bit complexity.

For arbitrary computable source values, equality comparisons in an
exact-real implementation need not be decidable. The strict margins in
(7) give an alternative rigorous procedure. Enumerate all subsets of the
finite quadrature pool of size at most $16R$, and all tuples of positive
rational weights on those subsets. Dovetail finite-precision evaluations
and certificates for

$$
I_R\prec P^TDP\prec4I_R.
$$

For example, approximate the symmetric Gram by a rational matrix with a
certified operator error $\eta$. Positive definiteness of that rational
matrix minus $(1+\eta)I_R$, and of $(4-\eta)I_R$ minus it, certifies the
desired inequalities. Rational positive definiteness can be checked by
exact elimination or principal minors. The finite evaluations and tests
are dovetailed so an inconclusive candidate never blocks the search.

There is a terminating candidate: the finite positive weights in (7) can
be approximated by positive rational weights on the same support while
preserving the strict inequalities, by continuity of this finite Gram.
The chosen marks remain the original rational quadrature marks. This
establishes computability without invoking a decidable test for equality
of arbitrary computable reals. It is an existence algorithm with no useful
general running-time bound.

At no stage is an original-width Gaussian neural array required. The
temporary arrays, if materialized, have quadrature size $J$, not original
network width $n$; $J$ can nevertheless exceed $n$. Storing the full pool
costs $O(J(R+k))$ real coordinates. Grid marks and source values can instead
be regenerated while scanning the pool; whitening, current Gram matrices,
and at most $16R$ selected rows use $O(R^2+kR)$ working coordinates,
excluding the source-evaluation workspace and precision bits. This
streaming observation gives no favorable bound on the work.

The retained metric has $N^2=O(R^2)$ entries. Retaining $P$ also costs only
$NR=O(R^2)$ entries, and it can be discarded once all needed initial
neuronal coefficients and mixers have been compiled. Retaining the raw
marks costs $kN=O(kR)$ coordinates. Thus a total $O(R^2)$ claim requires
either $k=O(R)$ or disposal of the marks after compilation, and separate
accounting for the source program, actual first-layer weights, decoder,
and any other retained state. None is hidden in a single “mark” coordinate.

Exact (4) is an exact-real algebraic statement, not a claim that arbitrary
transcendental entries have finite rational encodings. For a concrete
precision check, write $Q_H=D^{-1/2}HD^{-1/2}$. If a symmetric approximation
$\widetilde Q_H$ has operator error at most $\varepsilon$, then
$\widetilde H=D^{1/2}\widetilde Q_HD^{1/2}$ satisfies

$$
\|P^T\widetilde HP-I_R\|_{\mathrm{op}}\le4\varepsilon.
$$

This follows from $\|D^{1/2}P\|_{\mathrm{op}}^2\le4$. For
$\varepsilon<1/4$ it is still positive definite. The precision needed for
the weights, source evaluations, and downstream dynamics requires its own
error budget; no polylogarithmic bit bound follows from the coordinate
count.

## 4. Approximate population moments and whitening

There are two distinct approximation issues.

First, the finite quadrature may have only the accuracy (6) even when the
population identity (1) is exact. This causes no source-isometry error
after correction by (3).

Second, the population normalization itself may be approximate. Suppose
raw sources $\psi$ have true covariance $M=\mathbb E[\psi\psi^T]\succ0$.
If $M$ and a positive lower eigenvalue bound are effectively known, exact
computable whitening $p=M^{-1/2}\psi$ puts them in the theorem. Effective
moment integration plus certified positivity can supply this information.
If rank is not known, selecting the quotient by exact linear dependencies
is an additional task; a numerical small-eigenvalue cutoff does not prove
an exact rank statement.

If only $\widehat M$ is used, set
$\widetilde p=\widehat M^{-1/2}\psi$ and
$T=\mathbb E[\widetilde p\widetilde p^T]$. An identity such as
$\|T-I_R\|_{\mathrm{op}}\le\varepsilon$ does not make these sources exactly
orthonormal. Applying (3) to their selected values imposes the coefficient
inner product $I_R$, whereas their true source inner product is $T$.
For coefficients $a,b$, the discrepancy is

$$
|a^T(T-I_R)b|\le\varepsilon\|a\|_2\|b\|_2.
$$

If $T$ is known, the exact correction for this basis is instead

$$
H_T=D^{1/2}\left[
ZG^{-1}TG^{-1}Z^T+I_N-ZG^{-1}Z^T
\right]D^{1/2},                                    \tag{8}
$$

where $Z=D^{1/2}P$, $G=P^TDP$ for its selected evaluation matrix.
Multiplication gives $P^TH_TP=T$. If $I_R\preceq G\preceq4I_R$ and
$(1-\varepsilon)I_R\preceq T\preceq(1+\varepsilon)I_R$ with
$0\le\varepsilon<1$, then

$$
\frac{1-\varepsilon}{4}D
\preceq H_T\preceq(1+\varepsilon)D.
$$

To retain exactly the constants $D/4\preceq H_T\preceq D$, select instead
so that $T\preceq G\preceq4T$, by applying the theorem after true
whitening. Approximate whitening must not be relabeled an exact
population identity.

## 5. Two populations and the exact meaning of the mixer

For populations $\ell=1,2$, let $p_\ell$ have $R_\ell$ orthonormal
coordinates in $L^2(\mu_\ell)$ and let $(P_\ell,H_\ell)$ be the preceding
selections. Define the isometries

$$
U_\ell:\mathbb R^{R_\ell}\longrightarrow L^2(\mu_\ell),
\qquad (U_\ell a)(z)=p_\ell(z)^Ta,
$$

and their source spaces $S_\ell=\operatorname{range}(U_\ell)$.
Let $T_{21}:L^2(\mu_1)\to L^2(\mu_2)$ be a specified bounded operator,
or suppose its restricted forward/adjoint pairings below are supplied
directly with their intended meaning. The known matrix must be

$$
C=U_2^*T_{21}U_1\in\mathbb R^{R_2\times R_1},
\qquad
C_{ij}=\langle p_{2,i},T_{21}p_{1,j}\rangle_{L^2(\mu_2)}.       \tag{9}
$$

Set

$$
B=P_2CP_1^TH_1,\qquad
B^*=H_1^{-1}B^TH_2=P_1C^TP_2^TH_2.                \tag{10}
$$

Here $B^*$ is the adjoint between the two finite metric spaces, not an
independently chosen reverse matrix. Since $P_\ell^TH_\ell P_\ell=I$,

$$
BP_1a=P_2Ca,\qquad B^*P_2b=P_1C^Tb.                \tag{11}
$$

The map $P_\ell P_\ell^TH_\ell$ is the metric-orthogonal projection onto
$\operatorname{range}(P_\ell)$. Hence $B$ vanishes on the orthogonal
complement of the first selected source range and

$$
\|B\|_{H_1\to H_2}=\|C\|_{\mathrm{op}}
\le\|T_{21}\|_{\mathrm{op}}.                       \tag{12}
$$

The equality follows by taking inputs $P_1a$ attaining the Euclidean
operator norm of $C$, and the reverse inequality follows from contraction
of the source projection. If $C$ is replaced by $\widetilde C$, its
induced mixer error is exactly
$\|\widetilde B-B\|_{H_1\to H_2}=\|\widetilde C-C\|_{\mathrm{op}}$.

Let $\Pi_\ell=U_\ell U_\ell^*$ be the population source projection.
The population function represented by the first identity in (11), for
$f=U_1a$, is precisely

$$
U_2Ca=\Pi_2T_{21}f.                                \tag{13}
$$

It equals the full forward action only when $T_{21}f\in S_2$.
Likewise the reverse identity represents $\Pi_1T_{21}^*g$, and equals the
full reverse action only when $T_{21}^*g\in S_1$. Statements about values at
marks use the continuous source representative; equality of arbitrary
$L^2$ representatives at specified points is not automatic.

For a general source input, the omitted forward function is
$(I-\Pi_2)T_{21}f$. Its norm or its selected values are not controlled by
the isometry theorem. Point evaluation is not bounded on an arbitrary
$L^2$ complement. Thus even a small omitted $L^2$ component needs an
additional argument before it controls selected coordinate errors or
nonlinear feedback. The analogous issue applies to the reverse action.

With $R_1,R_2\le R$, each population uses at most $16R$ synthetic neurons;
the two metrics and the mixer have $O(R^2)$ entries in total. The pairing
matrix $C$ itself has at most $R^2$ entries and may be discarded after
forming $B$. If its computation requires inaccessible dense arrays, it
does not meet this theorem's direct-input assumption. Independent Gaussian
population marks alone do not determine the correct $C$ for a reused
random operator.

## 6. What this construction resolves

Under its stated effective finite-source assumptions, the continuous-law
selection problem has no remaining existence obstruction: constant-accuracy
positive Gaussian quadrature followed by spectral sparsification gives
$O(R)$ synthetic neurons, exact corrected source geometry, and
$O(R^2)$ metric/mixer storage. A deterministic terminating construction
does not need original-width initialized arrays.

The theorem does not prove that the full trained neural sources admit this
finite-dimensional Gaussian parameterization with a controlled $R$, that
the correct cross pairing (9) is directly computable, or that the omitted
forward and reverse actions remain small throughout training. It supplies
no comparison with a fresh dense network and no uniform-in-width running
time or bit-complexity bound.

Finally, non-diagonal $H$ changes the adjoint of a coordinatewise gate:
the metric adjoint of $\operatorname{diag}(a)$ is
$H^{-1}\operatorname{diag}(a)H$. Therefore substituting these metrics into
ordinary gradient flow without rederiving its derivatives is unjustified.
The theorem transfers the source-selection and linear-action part of the
authorized construction; it does not silently transfer a neural optimizer.

This author result is frozen at handoff; its hash is reported separately.
