# A causal response formulation of the fixed neural Gaussian law

2026-10-07. Complete proof candidate for a finite chronological query program. This is an exact equivalence of the scalar aggregate laws, including singular and redundant histories. It is not a continuous-time or all-time theorem.

Scientific inputs: the supervisor's response-law assignment, the complete UNCLIPPED_FINITE_HISTORY.md, and this route's own finite-history conditioning results. The unclipped source changed during this derivation; I reread it completely at SHA-256 9d842305cf984f2f5841466faf878e99f8f40815cebbc9f5ec341f9642b9ee81. Its added well-definedness convention is compatible with the assumptions below. I did not open its newly mentioned audit report or use that report's verdict as proof evidence. No other route, external source, experiment or study was consulted. The retained-history notation correction in FIXED_HISTORY_RATE.md is respected: no initial feature-Gram gap is reused as a history parameter.

The formulation below has no Gram inverse, no minimum-eigenvalue parameter and no retain/omit test. Its reaction coefficients are expected derivatives of the local scalar circuit with all deterministic global coefficients held fixed. Inverses and pseudoinverses appear only in the equivalence proof. Singular Gaussian coordinates can make individual derivative coefficients extension-dependent; their actual response fields are nevertheless invariant.

## 1. Program, chronology and regularity

Fix a finite canonical neural query program, such as a fixed finite Euler computation expressed through the exact rank-one histories. Its initialized matrices connect distinct layer populations and have no self-connections. Each population's limiting scalar fields are computed from its own Gaussian roots and primitive Gaussian fields, and shared deterministic coefficients. Coordinate operations never identify the neuron coordinate of one population with that of another.

The nonmatrix operations are smooth versions of those in the unclipped source: globally Lipschitz activations, bounded Lipschitz derivative gates, finite linear combinations with deterministic coefficients, and population expectations used to define shared scalar coefficients. For the local response argument, the row operations are $C^1$, and their first derivatives have at most polynomial growth. The assigned analytic activations satisfy this requirement: bounded strip derivative gives real-line bounds on both $\phi'$ and $\phi''$. Products with a backward field then have polynomially bounded first derivatives.

Every shared coefficient is a prescribed finite function of already computed population expectations and fixed data. When taking a local derivative below, its value is frozen, even if its defining formula involves moments of the field being perturbed. No differentiability of those global coefficient maps is required for this local derivative. The same freezing convention applies to every covariance and response coefficient already constructed.

The finite list of matrix queries has a fixed total chronological order. At one interface, write:

* $H_t$ for the scalar lower-population input of a forward query at event $t$, and $g_t$ for its upper-population answer;
* $D_s$ for the scalar upper-population input of a reverse query at event $s$, and $x_s$ for its lower-population answer.

Here $s<t$ means order in this finite instruction list, not physical training time. A query input is computed before its answer. For a neural Euler program, $H_t$ is a feature and $D_s$ is a backward signal for a specified sample and step. The training residuals and all trained rank-one contributions remain the same deterministic-coefficient scalar operations as in the source law.

Layer/interface indices are suppressed until needed. Every formula below is applied separately at each initialized matrix.

## 2. Primitive Gaussian fields and actual response definitions

For each interface, introduce centered Gaussian families $\eta_t$ and $\xi_s$ with covariances

\[
\mathbb E[\eta_t\eta_u]=\mathbb E[H_tH_u],\qquad
\mathbb E[\xi_s\xi_r]=\mathbb E[D_sD_r].
\tag{1}
\]

The family $\eta$ belongs to the upper population and $\xi$ to the lower one. All distinct primitive families, and the initial Gaussian root families, are independent. Correlations within one family are precisely (1), and its covariance may be singular. The right-hand sides are deterministic population expectations, not empirical data from a dense trajectory.

The local circuit is extended to formal real values of each of its primitive coordinates. When defining derivatives, regard the entries $\eta_t,\xi_s$ as separate coordinates even if their Gaussian law satisfies linear relations. Hold all other primitive entries and all deterministic coefficients fixed. This describes adding an external probe to one primitive field.

Define

\[
R^h_{t,s}
=\mathbb E\!\left[\frac{\partial H_t}{\partial\xi_s}\right],
\qquad s<t,
\qquad
R^\delta_{s,t}
=\mathbb E\!\left[\frac{\partial D_s}{\partial\eta_t}\right],
\qquad t<s.
\tag{2}
\]

The derivative is the total derivative through the already constructed local coordinate circuit. It is not the derivative with respect to an independently varied answer $x_s$ or $g_t$, and it is not a derivative of the Gaussian whitening variables. Set the coefficients to zero when the corresponding primitive has not yet been introduced.

Equivalently, with every deterministic population coefficient frozen,

\[
\begin{aligned}
R^h_{t,s}
&=\left.\frac{d}{d\epsilon}
\mathbb E[H_t(\ldots,\xi_s+\epsilon,\ldots)]\right|_{\epsilon=0},\\
R^\delta_{s,t}
&=\left.\frac{d}{d\epsilon}
\mathbb E[D_s(\ldots,\eta_t+\epsilon,\ldots)]\right|_{\epsilon=0}.
\end{aligned}
\tag{3}
\]

The local row circuit and its first derivatives have polynomial Gaussian growth at every finite stage. Indeed, the field-value envelope is at most linear in the finite Gaussian vector, while differentiating a bounded-gate product adds at most one such field factor. Induction over finitely many operations therefore gives polynomial bounds for the derivative. Gaussian moments justify (2) and differentiation under expectation in (3). These assertions also follow directly for the analytic canonical neural operations.

The proposed answer formulas are

\[
g_t=\eta_t+\sum_{s<t}D_sR^h_{t,s},
\qquad
x_s=\xi_s+\sum_{t<s}H_tR^\delta_{s,t}.
\tag{4}
\]

The sums include every earlier opposite-direction query at that interface, whether linearly independent, repeated, or identically zero. No history Gram is inverted to evaluate (2)–(4).

The signs in (4) are positive. They are fixed by the Gaussian conditioning identities proved below. Training deficits and learning-rate factors belong in the underlying local neural circuit; they then enter the response coefficients through differentiation of that circuit, not through an additional sign convention.

**Finite-program equivalence theorem.** For every fixed program satisfying Section 1, equations (1)–(4) construct a causal scalar law with finite moments and finite expected responses. This law agrees with the retained Gaussian regression law in all population row histories, predictions, pairings and deterministic coefficients. The result includes singular primitive covariance and zero query innovations. Admissible changes of a smooth off-support extension leave the response fields unchanged, though individual derivative coefficients can change in covariance-null directions.

## 3. Why this is a causal Gaussian construction

At a forward event $t$, the entire input $H_t$ and every earlier $H_u$ already exist as functions in the lower population. Thus the new covariance entries $\mathbb E[H_tH_u]$ and $\mathbb E[H_t^2]$ are known before the new answer is formed. The enlarged matrix is a Gram matrix in $L^2$, hence positive semidefinite. It extends the covariance of the already constructed $\eta$ family.

For any such positive-semidefinite extension, one can append a centered Gaussian coordinate with those covariances. A proof is to project the new formal vector onto the finite span of the previous vectors in the Hilbert space defined by that Gram matrix, and add an independent standard Gaussian with the residual norm as multiplier. A zero residual norm adds no independent coordinate. The projection is a mathematical existence construction; no inverse is part of (1)–(4).

The appended coordinate can be chosen independent of the other primitive families, because its required correlations concern only its own earlier family and all covariance entries are deterministic. The response $R^h_{t,s}$ is also determined from the already available $H_t$ circuit before the new $\eta_t$ is used. Equation (4) then defines $g_t$.

At a reverse event the same argument applies to $D_s$, its covariance with earlier $D_r$, the next $\xi_s$ and the known derivatives of $D_s$. This is induction in the fixed chronological order, not a simultaneous nonlinear fixed-point problem. The construction never asks for an unknown future query or future realized dense field.

Once the finite construction is complete, the resulting joint primitive Gaussian law could equivalently be sampled from its completed deterministic covariance matrices. Their entries were obtained causally from the initial data and prior scalar laws. This is different from selecting coefficients from a realized future finite-width field table.

The construction uniquely determines the law of all row fields and deterministic coefficients when the local circuit extension is fixed. Section 7 shows that allowable changes of an off-support extension do not affect the response fields. There is no claim here that arbitrary Lipschitz nonsmooth row operations have a canonical derivative on a singular Gaussian support; the stated $C^1$ hypothesis avoids that unrelated ambiguity.

## 4. Gaussian integration by parts with singular covariance

We use the following elementary identity, including its singular case. Let $\xi$ be a centered Gaussian vector with covariance $Q\succeq0$, and let $Z$ be an independent collection of other Gaussian primitives. For a $C^1$ function $F(\xi,Z)$ whose value and first derivatives have polynomial growth,

\[
\mathbb E[\xi F]=Q\,\mathbb E[\nabla_\xi F].
\tag{5}
\]

To prove it, write $\xi=AU$ with $U$ a vector of independent standard normals and $AA^\top=Q$. For each coordinate $U_j$, one-dimensional integration by parts against its Gaussian density gives

\[
\mathbb E[U_j F(AU,Z)]
=\mathbb E[(A^\top\nabla_\xi F(AU,Z))_j].
\]

Boundary terms vanish by polynomial growth, and Gaussian integrability permits conditioning on and then integrating $Z$. Multiplication by $A$ proves (5). No inverse or positive covariance eigenvalue is used.

Two consequences will be used repeatedly.

First, if $D$ is any scalar query-history vector with $\mathbb E[DD^\top]=Q$, then

\[
D^\top(I-Q^\dagger Q)v=0\quad\text{almost surely}
\tag{6}
\]

for every deterministic $v$. Its squared expectation is zero because $(I-Q^\dagger Q)v$ lies in the null space of $Q$.

Second, if two admissible functions $F_1,F_2$ agree almost surely under the joint Gaussian law, then

\[
Q\,\mathbb E[\nabla_\xi(F_1-F_2)]=0.
\tag{7}
\]

This follows immediately from (5). Thus their expected gradients differ only in a covariance-null direction.

## 5. The regression law can retain all query indices

The source's scalar law retains only positive-innovation directions. For the equivalence proof it is useful to write the same law with all preceding query columns, using pseudoinverses.

Let $H$ be the full vector of earlier forward inputs, $F$ their answers, $D$ the full vector of earlier reverse inputs, and $B$ their answers. At a forward query $h$, define

\[
\begin{aligned}
Q_H&=\mathbb E[HH^\top],&
a&=Q_H^\dagger\mathbb E[Hh],&
e&=h-H^\top a,\\
Q_D&=\mathbb E[DD^\top],&
b&=Q_D^\dagger\mathbb E[Be],&
\sigma^2&=\mathbb E[e^2].
\end{aligned}
\tag{8}
\]

The complete-history regression answer is

\[
g=F^\top a+D^\top b+\sigma Z_{\mathrm{new}}.
\tag{9}
\]

Its reverse counterpart exchanges the two populations and orientations. Empty products are zero. All expectations in (8) use the population to which their arguments belong.

Here is why (9) is exactly the retained-history law, including at singular histories. Every omitted query is a deterministic linear combination of the retained same-direction inputs, and its answer is the same combination of their answers. Hence

\[
H=T_HH_{\mathrm{ret}},\quad F=T_HF_{\mathrm{ret}},
\qquad
D=T_DD_{\mathrm{ret}},\quad B=T_DB_{\mathrm{ret}},
\tag{10}
\]

with deterministic full-column-rank matrices $T_H,T_D$ whenever those retained histories are nonempty. Each matrix includes the identity rows corresponding to its retained queries.

Projection of $h$ onto the span of $H$ is identical to projection onto the span of $H_{\mathrm{ret}}$. Thus its residual and variance are unchanged, and $F^\top a$ is the corresponding retained-answer combination. For the second term, use

\[
T^\top(TQT^\top)^\dagger T=Q^{-1}
\tag{11}
\]

when $T$ has full column rank and $Q>0$. To verify (11), set $A=TQ^{1/2}$; then $A^\top(AA^\top)^\dagger A=I$ because $A$ has full column rank. This last identity follows by an orthonormal singular-vector decomposition, or by solving the minimum-norm left-inverse equations. Multiplying by $Q^{-1/2}$ proves (11).

Substitution of (10) and (11) in $D^\top b$ gives precisely the retained reverse-history term. If the new innovation variance is zero, $e=0$ almost surely, so (9) is just the prescribed linear combination of past forward answers. Consequently the identities (10) remain valid as the program proceeds. This proves the equivalence inductively.

This section uses pseudoinverses only to compare two descriptions. The response formulation itself still contains none.

## 6. Equivalence by chronological cancellation

Assume all previous answers obey (4), and consider a new forward query $h=H_t$. Assemble all earlier forward queries and all earlier reverse queries in vectors $H,D$ as in Section 5. Extend previous response arrays by zeros when a primitive did not yet exist.

Let $R_H$ have entries

\[
(R_H)_{u,s}
=\mathbb E\!\left[\frac{\partial H_u}{\partial\xi_s}\right],
\qquad u<t,\ s<t,
\]

and let $r$ have entries $r_s=\mathbb E[\partial h/\partial\xi_s]$. Let $S$ be the matrix of previous backward response coefficients, with zero entries for forward queries later than the corresponding reverse query. The induction hypothesis gives, within their respective populations,

\[
F=\eta+R_HD,\qquad B=\xi+SH.
\tag{12}
\]

The projection residual $e$ in (8) satisfies $\mathbb E[He]=0$, even if $Q_H$ is singular: $\mathbb E[Hh]$ lies in the range of $Q_H$, since every covariance-null linear combination of $H$ vanishes almost surely. Therefore

\[
\mathbb E[Be]
=\mathbb E[\xi e]+S\mathbb E[He]
=\mathbb E[\xi e].
\tag{13}
\]

In the lower population, all other primitive families and roots are independent of $\xi$. Apply (5), with every deterministic coefficient frozen:

\[
\mathbb E[\xi e]
=Q_D\mathbb E[\nabla_\xi e]
=Q_D(r-R_H^\top a).
\tag{14}
\]

By (6), multiplication of the regression coefficient by the actual query vector removes the range projection:

\[
D^\top b
=D^\top Q_D^\dagger Q_D(r-R_H^\top a)
=D^\top(r-R_H^\top a)
\quad\text{almost surely}.
\tag{15}
\]

Combine (12) and (15) in (9):

\[
\begin{aligned}
g
&=(\eta+R_HD)^\top a
 +D^\top(r-R_H^\top a)+\sigma Z_{\mathrm{new}}\\
&=\eta^\top a+\sigma Z_{\mathrm{new}}+D^\top r.
\end{aligned}
\tag{16}
\]

The Gaussian variable

\[
\eta_t=\eta^\top a+\sigma Z_{\mathrm{new}}
\tag{17}
\]

has covariance $\mathbb E[H_uh]$ with every previous $\eta_u$ and variance $\mathbb E[h^2]$, because $h=H^\top a+e$ is an orthogonal $L^2$ decomposition. It can be generated with a fresh standard normal independent of all previous primitive families; when $\sigma=0$ that term vanishes. Thus (16) is exactly the forward response formula (4) with the Gaussian law (1).

The reverse cancellation is symmetric but worth stating. For a new $d=D_s$, set $e'=d-D^\top b$, where $b$ is its projection coefficient onto earlier reverse inputs. Since $\mathbb E[De']=0$ and $F=\eta+R_HD$,

\[
\mathbb E[Fe']=\mathbb E[\eta e'].
\]

If $R_D$ is the matrix of earlier derivatives $\mathbb E[\partial D_r/\partial\eta_t]$ and $r^\delta_t=\mathbb E[\partial d/\partial\eta_t]$, integration by parts gives

\[
\mathbb E[\eta e']
=Q_H(r^\delta-R_D^\top b).
\]

The earlier reverse answers are $B=\xi+R_DH$. Their reaction contribution cancels in the reverse version of (9), leaving

\[
x_s=\xi_s+H^\top r^\delta,
\]

where the new centered Gaussian $\xi_s$ has covariance $\mathbb E[D_sD_r]$ with each previous $\xi_r$ and variance $\mathbb E[D_s^2]$. This is the reverse equation in (4).

Starting with empty histories proves equivalence for every event in the finite program. Between queries both constructions use the same deterministic local operations and global expectations. Therefore they produce the same complete scalar row laws, the same predictions and pairings, and the same deterministic coefficients.

## 7. Zero innovations and null-covariance ambiguity

Suppose a new forward input obeys $h=H^\top a$ almost surely. Then $e=0$ and $\sigma=0$. Formula (14) implies

\[
Q_D(r-R_H^\top a)=0.
\]

By (6), $D^\top r=D^\top R_H^\top a$ almost surely. The Gaussian extension has $\eta_t=\eta^\top a$, so (4) gives

\[
g_t=F^\top a,
\]

exactly the omitted-query answer in the source. Its response coefficient vector need not equal $R_H^\top a$ componentwise; equality after multiplication by the query fields is sufficient and is guaranteed. Reverse zero innovations work in the same way.

Now change the smooth formal extension of a local query function while preserving its value almost surely and its causal dependence on the already introduced primitives. The expected gradient change with respect to $\xi$ lies in $\ker Q_D$ by (7). Thus its contribution $D^\top\Delta R^h$ is zero almost surely. The corresponding statement holds for $\eta$, $Q_H$ and $H^\top\Delta R^\delta$.

This proves invariance of the actual response fields under allowable off-support extension changes, even when individual response coefficients are not intrinsic. Induction then preserves all later field values almost surely, their moments and their primitive covariance extensions; the same argument applies again at the next query. Such a change must remain $C^1$ with integrable polynomial derivative growth and must not introduce dependence on future coordinates. The canonical extension obtained from the chronological circuit already satisfies these requirements.

In particular:

* A repeated query may introduce a repeated Gaussian coordinate rather than a new innovation, with no ambiguity in its answer.
* An identically zero query has zero answer even if an off-support extension has a nonzero derivative in a null direction.
* Singular initial Gaussian root covariance is harmless.
* No nonzero-label condition or positive initial feature-Gram condition is needed merely for this equivalence.

## 8. Computing the responses without inverses

The derivative in (2) can be computed by ordinary forward differentiation of the finite local circuit. Each primitive coordinate is given its unit perturbation when introduced; all deterministic coefficients have derivative zero.

For example, at this interface,

\[
\frac{\partial x_s}{\partial\xi_r}
=\mathbf1_{\{r=s\}}
+\sum_{t<s}R^\delta_{s,t}
\frac{\partial H_t}{\partial\xi_r},
\tag{18}
\]

and

\[
\frac{\partial g_t}{\partial\eta_u}
=\mathbf1_{\{u=t\}}
+\sum_{s<t}R^h_{t,s}
\frac{\partial D_s}{\partial\eta_u}.
\tag{19}
\]

Coordinate activations and gates use their usual chain and product rules. Operations involving other interfaces in the same population are differentiated through their already constructed local circuits as well. Averaging the resulting derivative fields gives (2). These formulas include indirect dependence through earlier local responses; replacing them by direct derivatives with respect to an answer would generally omit terms.

At a finite horizon this description retains the covariance matrices of primitive query fields, the finite local field histories needed by the program, and the expected derivative arrays. All counts depend on query count, panel size and depth, not on width. A scalar Gaussian realization uses at most one new scalar innovation per query, though a rank-deficient covariance may require fewer. This is a mathematical Gaussian description, not an assertion about an exact finite-bit random seed or an efficient quadrature scheme.

The statistical law of $H,D$ still contains nonlinear coactivation information. The two covariance arrays alone are not asserted to determine the local circuit's future. The response construction consists of that circuit together with (1)–(4), not a covariance-only Markov closure.

## 9. Checks, implications and limits

With no earlier reverse query, the first forward answer is its centered Gaussian field with feature covariance. At the first reverse query, (4) gives a Gaussian field with backward covariance plus the mean local derivative of that backward input multiplied by the earlier feature fields. This reproduces the directly proved first backward correction in the original causal route.

For the elementary scalar case $D_s=c\,\eta_t$, with deterministic $c$ and one previous forward input $H_t$, the reverse law is

\[
x_s=\xi_s+cH_t,\qquad
\mathbb E[\xi_s^2]=c^2\mathbb E[H_t^2].
\]

The deterministic $cH_t$ term is the correction that an independent-Gaussian-action ansatz misses. The formula remains valid at $c=0$ without division.

The theorem proved here is finite chronological equivalence between the regression aggregate law and the response aggregate law. Under the hypotheses of UNCLIPPED_FINITE_HISTORY.md, the same fixed-program neural limit is therefore expressed by (1)–(4). Under the additional quantitative regularity conditions in FIXED_HISTORY_RATE.md, the previously proved fixed-program comparison targets this same law. Rewriting the law without inverses does not remove the retained-gap dependence of that earlier error proof.

No continuum limit of the response sums, boundedness of a response operator uniformly in program length, quantitative well-conditioning, finite autonomous memory, or all-time approximation has been proved here. The new result removes inverse-history matrices from the formulation and identifies the correction coefficients as causal local susceptibilities. Uniform control of those susceptibilities is a separate mathematical problem.
