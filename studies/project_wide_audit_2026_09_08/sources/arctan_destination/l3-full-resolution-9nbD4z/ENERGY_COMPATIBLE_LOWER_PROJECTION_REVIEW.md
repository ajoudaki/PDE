# Adversarial audit: energy-compatible lower-field projection

Verdict: **PASS for the entire final nine-section note at its stated finite-width scope**, including the bounded-test source estimate and eventual exact canonical consistency at each fixed width.

Required mathematical fixes: **none**. All asserted dynamical, initialization, defect, and fixed-width consistency implications are valid, with the deterministic sufficiently-large-width restrictions already imposed in Sections 4 and 5. The report below reconstructs the full proof. The topology exclusions must be read in their width-uniform/population sense: Section 9 explicitly proves eventual exactness at fixed width. An optional wording clarification of that distinction is recorded below.

## Audited object and isolation

- Candidate: `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ENERGY_COMPATIBLE_LOWER_PROJECTION.md`.
- Certified final candidate SHA256: `d2d10248021a9cb01ab8a6f2358ecfbef4ce6abdad8107654e00dfa38870abb5`, independently computed after both appended sections were present.
- Superseded original SHA256: `9045b54f9f21e534388183bf48a3e1f8398f06e7aa290960a4505431b149dd6a`. The first 360 lines of the final candidate independently hash to this value, confirming that the earlier proof is byte-for-byte unchanged. The final candidate was nevertheless read in full, including both additions. No intermediate Section-8-only version is certified.
- Mathematical source: only that candidate. No ledgers, conversations, prior reviews, other agents' tests, other proofs, or repository sources were inspected.
- I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` in full and used its requirements for complete derivations, theorem hypotheses, and adversarial checking.
- No experiments, source-task operations, or repository edits were performed. The candidate was not edited. This report was created using `apply_patch`.
- Line references below refer to the audited candidate. Final file hashes are supplied with delivery; a report cannot conventionally contain its own final SHA256 without changing the file being hashed.

## 1. Precise claim certified

Set $c=\pi/2$, $M_0=8$, and choose the deterministic $v_1,v_2,v_3,\kappa_1,\kappa_3,a,f_*$ exactly as in (16) and (25), with $\kappa_1=v_1/2$, $\kappa_3=v_3/2$. In particular all three $v_j$ and both $\kappa_j$ are strictly positive. An explicit sufficient integer width threshold is

\[
N_0=\max\left\{
 \left\lceil\frac{16c}{\kappa_3a}\right\rceil,
 \lfloor2c\rfloor+1
\right\}.
\]

For every integer $n\ge N_0$, let $E_n$ be the intersection of (10) and (14), with the constants just specified. For every realized initial state in $E_n$ and every fixed cap $R>0$:

1. Equation (4) has a unique solution for every feature time $s\ge0$.
2. Equations (9), (12), (13), (19), (20), and (21) hold, with constants independent of $R,n$, and of the particular initial state in $E_n$, on each fixed finite feature horizon. The initial-interval bound applies when the horizon is smaller than $a$.
3. The prediction is strictly increasing: $f'\ge\kappa_3/4>0$ on $[0,a]$, and $f'\ge k=f_*^2/B(1)^2>0$ for $s\ge a$.
4. The exact clock $ds/dt=2(1-f(s))$, $s(0)=0$, exists for all physical times, remains below its first root $s_\dagger$, and tends to that root. Its total feature time is $s_\dagger\le S_\dagger=a+1/k$, a bound independent of the cap and width.
5. Under the stated independent Gaussian initialization, $\mathbb P(E_n)\to1$.
6. For $e_R=M(\delta^{(2)}-u_R)$, the normalized spacetime $L^1$ bound (29), all bounded measurable vector tests in (31), and the bounded-derivative empirical chain rule (32) hold with error at most $D(S)/R$. The physical source has the corresponding bound $D(S_\dagger)/R$ on every physical interval.
7. At each fixed width and horizon $S\ge a$, every cap $R\ge\sqrt n\,A_3(S)B(S)$ produces exactly the same canonical finite-width feature path on $[0,S]$. Taking $S=S_\dagger$ gives exact agreement with the canonical continuous physical flow at every physical time. This sufficient cap is width dependent.

The deterministic statement has the order of quantifiers

\[
\forall n\ge N_0\quad\forall\theta_0\in E_n\quad\forall R>0.
\]

It does not require a union bound over caps. It is not a claim of one common realized event for all widths on an unspecified infinite probability space.

The global-in-feature-time bounds are finite-horizon bounds: for example $b(S)>0$ for each finite $S$, not a claim that $\inf_{s\ge0}c_1(s)>0$. The physical trajectory is confined to a uniformly bounded feature horizon, so those finite-horizon estimates do give uniform bounds along its entire physical-time trajectory.

## 2. Projection inequality and local finite-dimensional regularity

Write $d=\delta^{(2)}$, $K_R=[-R,R]^n$, and $J(u)=\tfrac12(u-d)^TM(u-d)$. When $c_1>0$, (2) gives $M\succeq c_1I\succ0$. The finite box is nonempty, compact, and convex. Continuity gives a minimizer and strict convexity gives uniqueness.

At a minimizer $u\in K_R$, each segment $u+t(v-u)$, $0\le t\le1$, stays feasible. Its right derivative at zero gives

\[
(v-u)^TM(u-d)\ge0 \qquad(v\in K_R).
\]

Conversely, for any feasible $v$,

\[
J(v)-J(u)
=(v-u)^TM(u-d)+\tfrac12(v-u)^TM(v-u)\ge0.
\]

This proves (5) in both directions. Taking $v=0$ yields

\[
d^TMu\ge u^TMu\ge c_1\|u\|_2^2.
\]

Cauchy--Schwarz in the inner product induced by $M$ gives

\[
u^TMu\le d^TMu\le\sqrt{d^TMd}\sqrt{u^TMu}.
\]

Division is needed only when $u\ne0$; when $u=0$, (7) holds directly. Thus (6) and (7) are valid, including the zero case. No Euclidean nonexpansiveness claim is substituted for this metric inequality.

For local regularity, take $u=P_M(d)$, $v=P_N(e)$, with the same fixed box and $M,N\succeq\alpha I$, $\alpha>0$. The two variational inequalities imply

\[
(u-v)^T\{M(u-d)-N(v-e)\}\le0.
\]

Expand the bracket as

\[
M(u-v)+M(e-d)+(M-N)(v-e).
\]

Consequently

\[
\alpha\|u-v\|_2^2
\le\|u-v\|_2\bigl(
\|M\|_{\rm op}\|d-e\|_2
+\|M-N\|_{\rm op}\|v-e\|_2\bigr).
\]

This proves (8) by division when $u\ne v$, and directly when they agree. On a bounded neighborhood of an SPD matrix the smallest eigenvalue stays bounded below. For fixed $R,n$,

\[
\|v-e\|_2\le R\sqrt n+\|e\|_2
\]

is locally bounded. Thus the projection is locally Lipschitz in its finite-dimensional arguments. The state-to-$(M,d)$ maps are smooth, so their composition with the projection is locally Lipschitz on $c_1>0$.

The elementary local ODE theorem applies to this open finite-dimensional domain: a bounded, Lipschitz vector field on a sufficiently small closed ball gives a contraction of its integral equation for a short time, and hence a unique local solution and maximal extension. The hypotheses hold for every fixed $R,n$. Crossing an active face or edge of the box does not destroy continuity or local Lipschitz continuity.

This reasoning gives no dimension-uniform RMS stability estimate for changes between two states. In particular it does not replace control of a product of a changed gate and $q^{(2)}$ by separate RMS controls. The exclusion in lines 114–116 is substantive and correctly observed throughout the proof.

## 3. Exact gradient, metric, and energy normalization

Let $D_j=\operatorname{diag}(\phi'(z^{(j)}))$, and write $H_j=\|h^{(j)}\|_2^2/n$. The ordinary Euclidean gradients of the stated forward network are

\[
\begin{aligned}
\nabla_{z^{(1)}}f&=\frac1nD_1(W^{(2)})^T\delta^{(2)},\\
\nabla_{W^{(2)}}f&=\frac1n\delta^{(2)}(h^{(1)})^T,\\
\nabla_{W^{(3)}}f&=\frac1n\delta^{(3)}(h^{(2)})^T,\\
\nabla_{W^{(4)}}f&=\frac1n h^{(3)}.
\end{aligned}
\]

The parameter metric consistent with (4) has squared norm

\[
\|\dot\theta\|_g^2
=\frac{\|\dot z^{(1)}\|_2^2}{n}
+\|\dot W^{(2)}\|_F^2
+\|\dot W^{(3)}\|_F^2
+\frac{\|\dot W^{(4)}\|_2^2}{n}.
\]

Its gradient of $f$ therefore agrees with (4) when $u_R=\delta^{(2)}$. A feasible $\delta^{(2)}$ is exactly the unique minimizer of (3), since its objective is zero. This verifies the note's pointwise agreement claim, including all width factors.

There is also a direct forward derivation of the energy identity. With $u=u_R$,

\[
\begin{aligned}
(z^{(2)})'
&=(W^{(2)})'h^{(1)}+W^{(2)}D_1(z^{(1)})'\\
&=H_1u+W^{(2)}D_1^2(W^{(2)})^Tu=Mu,\\
(z^{(3)})'
&=H_2\delta^{(3)}+W^{(3)}D_2Mu.
\end{aligned}
\]

Differentiating the readout then gives exactly

\[
f'=H_3+\frac{\|\delta^{(3)}\|_2^2}{n}H_2
+\frac{(\delta^{(2)})^TMu}{n}.
\]

The lower squared speeds satisfy

\[
\frac{\|(z^{(1)})'\|_2^2}{n}
+\|(W^{(2)})'\|_F^2
=\frac{u^TW^{(2)}D_1^2(W^{(2)})^Tu}{n}
+\frac{H_1\|u\|_2^2}{n}
=\frac{u^TMu}{n}.
\]

The remaining squared speeds are precisely

\[
\|(W^{(3)})'\|_F^2
=\frac{\|\delta^{(3)}\|_2^2}{n}H_2,
\qquad
\frac{\|(W^{(4)})'\|_2^2}{n}=H_3.
\]

Thus

\[
f'=\|\theta'\|_g^2
+\frac{(\delta^{(2)}-u)^TMu}{n}
\ge\|\theta'\|_g^2\ge0.
\]

This checks (9), including its sign, the exact lower metric, both learned matrix terms, the rescaled readout, and the nonnegative work excess. The proof never requires that excess to vanish, either at fixed cap or in a cap limit.

## 4. Bounds established before coercivity

Fix a finite $S>0$, and consider only the existing portion of a solution on which $c_1>0$. Since $|\phi|\le c$, $|\phi'|\le1$, and $(W^{(4)})'=h^{(3)}$,

\[
\|W^{(4)}(s)\|_\infty\le1+cs\le B(S),
\qquad
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}\le B(S).
\]

The upper matrix update has rank one, so

\[
\|(W^{(3)})'\|_{\rm op}
\le\|(W^{(3)})'\|_F
=\frac{\|\delta^{(3)}\|_2\|h^{(2)}\|_2}{n}
\le cB(S).
\]

Integration gives $\|W^{(3)}(s)\|_{\rm op}\le M_0+cB(S)S=A_3(S)$. Also $|f(s)|\le cB(S)$ and $f(0)\ge-c$. Therefore the nonnegative sum of squared speeds obeys

\[
\int_0^s\|\theta'(r)\|_g^2\,dr
\le f(s)-f(0)\le cB(S)+c=D(S).
\]

The same bound holds for each individual squared speed. Cauchy--Schwarz in time gives

\[
\begin{aligned}
\|W^{(2)}(s)-W^{(2)}_0\|_F&\le\sqrt{sD(S)},\\
\frac{\|z^{(1)}(s)-z^{(1)}_0\|_2}{\sqrt n}&\le\sqrt{sD(S)}.
\end{aligned}
\]

Since operator norm is at most Frobenius norm, $\|W^{(2)}(s)\|_{\rm op}\le A_2(S)$. These are exactly (12)–(13).

No lower coercivity constant has been used here. Nor has a cap-independent bound on $u_R$, an inverse of $M$, or an existence assertion beyond the current local solution been used. This is the essential noncircular ordering of the argument.

## 5. Uniform initial interval, including negative initial prediction

Evaluate $A_2,A_3,B,D$ at $S=1$. Applying the 1-Lipschitz property of $\phi$ and the preceding displacement bound gives

\[
\frac{\|h^{(1)}(s)-h^{(1)}_0\|_2}{\sqrt n}\le\sqrt{sD(1)}.
\]

For the second layer, expand the exact product as

\[
z^{(2)}(s)-z^{(2)}_0
=W^{(2)}(s)(h^{(1)}(s)-h^{(1)}_0)
+(W^{(2)}(s)-W^{(2)}_0)h^{(1)}_0.
\]

The two normalized terms are bounded respectively by $A_2(1)\sqrt{sD(1)}$ and $c\sqrt{sD(1)}$. This gives the second line of (15). The identical decomposition at the third layer gives

\[
\frac{\|h^{(3)}(s)-h^{(3)}_0\|_2}{\sqrt n}
\le A_3(1)[A_2(1)+c]\sqrt{sD(1)}+c^2B(1)s
\le L\sqrt s.
\]

The last inequality uses $s\le1$. There is no assumption that a learned forward matrix is frozen in either decomposition.

The choice of $a$ in (16) actually ensures the stronger lower bounds

\[
\frac{\|h^{(1)}(s)\|_2}{\sqrt n}\ge\frac34\sqrt{\kappa_1},
\qquad
\frac{\|h^{(3)}(s)\|_2}{\sqrt n}\ge\frac34\sqrt{\kappa_3}
\]

on the existing portion of $[0,a]$. Hence the weaker bounds $H_1\ge\kappa_1/4$, $H_3\ge\kappa_3/4$ used in the note are valid.

These bounds also rule out a maximal endpoint at or before $a$: the preliminary bounds keep the finite-dimensional parameters bounded and $c_1\ge\kappa_1/4$ keeps them inside the ODE domain. The continuation argument in the next section applies here as well. Thus the initial estimates hold on the entire closed interval $[0,a]$, rather than merely conditionally on its existence.

The tiny readout assumption yields the deterministic bound

\[
|f(0)|\le
\frac{\|W^{(4)}_0\|_2}{\sqrt n}
\frac{\|h^{(3)}_0\|_2}{\sqrt n}
\le\frac{2c}{n}.
\]

No favorable sign of $f(0)$ is assumed. Since $f'\ge H_3\ge\kappa_3/4$ on this interval,

\[
f(a)\ge-\frac{2c}{n}+\frac{\kappa_3a}{4}
\ge\frac{\kappa_3a}{8}=f_*
\]

under the stated threshold $n\ge16c/(\kappa_3a)$. All constants defining $a$ were obtained before invoking this positivity. Monotonicity then preserves $f(s)\ge f_*$ at later existing times.

## 6. Global noncollapse and finite-dimensional continuation

For $a\le s\le S$, Cauchy--Schwarz and the readout bound give

\[
f_*\le f(s)
\le B(S)\frac{\|h^{(3)}(s)\|_2}{\sqrt n}.
\]

Because $\phi(0)=0$ and $\phi$ is 1-Lipschitz,

\[
\|h^{(3)}\|_2\le\|W^{(3)}h^{(2)}\|_2
\le A_3(S)\|h^{(2)}\|_2
\le A_3(S)A_2(S)\|h^{(1)}\|_2.
\]

This proves (18) and the later-time component of $b(S)$ in (19). Combining it with the initial interval gives $c_1(s)\ge b(S)>0$. This argument uses an upper readout bound and upper operator bounds; it neither assumes lower operator singular values nor assumes nonsaturated gates.

To make continuation explicit, suppose the maximal feature endpoint $T$ is finite and choose $S>\max\{T,a\}$. Equations (12)–(13) bound $z^{(1)}$ and $W^{(4)}$ in ordinary finite-dimensional norms, for this fixed $n$. The operator bounds for $W^{(2)},W^{(3)}$ also bound their Frobenius norms, since $\|W\|_F\le\sqrt n\|W\|_{\rm op}$. Equation (19) keeps the state in a closed bounded set with $c_1\ge b(S)>0$. This is a compact subset of the domain $c_1>0$.

For fixed $R,n$, the continuous vector field is bounded on this compact set. Thus the trajectory is Cauchy as $s\uparrow T$ and has a limit there. Local existence at this limit extends the solution, and local uniqueness makes that extension agree with the old trajectory. This contradicts maximality. This argument is applicable despite the nonsmooth active-set changes of the projection.

Importantly, this continuation proof does not depend on the later cap-independent velocity estimate (20). A bound on a continuous field on a compact set for each fixed $R,n$ suffices. There is no circular appeal to global coercivity or to uniform state stability.

## 7. Cap-independent supremum velocities and full-query derivative

After noncollapse is established, write $\Lambda(S)=c^2+A_2(S)^2$. Then

\[
b(S)I\preceq M\preceq\Lambda(S)I,
\qquad
\frac{\|\delta^{(2)}\|_2}{\sqrt n}
\le\frac{\|(W^{(3)})^T\delta^{(3)}\|_2}{\sqrt n}
\le A_3(S)B(S).
\]

Equation (7) consequently gives

\[
\frac{\|u_R\|_2}{\sqrt n}
\le\sqrt{\frac{\Lambda(S)}{b(S)}}A_3(S)B(S)=U(S),
\]

which is (20). If $S<a$, the initial lower bound may be used directly; alternatively the displayed minimum defining $b(S)$ is at most $\kappa_1/4$ and remains a valid lower bound. No estimate asserts $\|u_R\|_2\le\|\delta^{(2)}\|_2$ for a general non-diagonal metric.

The parameter velocity bounds are

\[
\frac{\|(z^{(1)})'\|_2}{\sqrt n}\le A_2U,
\quad\|(W^{(2)})'\|_F\le cU,
\quad\|(W^{(3)})'\|_F\le cB,
\quad\frac{\|(W^{(4)})'\|_2}{\sqrt n}\le c.
\]

Using the exact identities derived in Section 3 of this report,

\[
\frac{\|(z^{(2)})'\|_2}{\sqrt n}\le\Lambda U,
\qquad
\frac{\|(z^{(3)})'\|_2}{\sqrt n}\le c^2B+A_3\Lambda U.
\]

For $q^{(2)}=(W^{(3)})^T\delta^{(3)}$, differentiation gives

\[
(q^{(2)})'=((W^{(3)})')^T\delta^{(3)}
+(W^{(3)})^T(\delta^{(3)})'.
\]

The first summand is exactly $h^{(2)}\|\delta^{(3)}\|_2^2/n$, whose normalized norm is at most $cB^2$. For the second,

\[
(\delta^{(3)})'
=h^{(3)}\odot\phi'(z^{(3)})
+W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]

The elementary bound $|\phi''(x)|=2|x|/(1+x^2)^2\le2$ and the coordinatewise readout bound imply

\[
\frac{\|(\delta^{(3)})'\|_2}{\sqrt n}
\le c+2B(c^2B+A_3\Lambda U).
\]

Multiplication by $A_3$ and addition of the first summand give exactly the final line of (21).

The state trajectory is continuously differentiable because its vector field is continuous. Every differentiated expression here is a smooth function of that state. No derivative of $u_R$ is taken. Integrating these derivative bounds gives time-Lipschitz bounds in the displayed normalized norms. This is regularity along each trajectory, not a stability estimate between two different states and not a coordinate tail estimate.

For use in the scalar clock, a fully explicit upper bound on $f'$ is also available. Equations (6)–(7) and Cauchy--Schwarz give

\[
0\le(\delta^{(2)})^TMu_R
\le(\delta^{(2)})^TM\delta^{(2)}.
\]

Hence, on each finite horizon,

\[
0\le f'\le
\Lambda A_3^2B^2+c^2B^2+c^2.
\]

This verifies the asserted boundedness of $f'$ without differentiating the projection, and in fact without needing $U$ for this particular upper bound.

## 8. Readout ratio and exact physical clock

Define $v=\|W^{(4)}\|_2^2/n$. Since $(W^{(4)})'=h^{(3)}$,

\[
v'=\frac2n(W^{(4)})^Th^{(3)}=2f.
\]

Cauchy--Schwarz gives $f^2\le vH_3$, while (9) gives $f'\ge H_3$. Thus $f'\ge f^2/v$ wherever $v>0$. For $s\ge a$, $f\ge f_*>0$, which itself excludes $v=0$. There is no division by $v(0)$, and no difficulty if the readout vanishes at an earlier time.

On $[a,\infty)$,

\[
\left(\frac{f^2}{v}\right)'
=\frac{2ff'}v-\frac{f^2v'}{v^2}
=\frac{2f}{v}\left(f'-\frac{f^2}{v}\right)\ge0.
\]

Since $a\le1$, $v(a)\le B(1)^2$. Therefore

\[
f'(s)\ge\frac{f(s)^2}{v(s)}
\ge\frac{f(a)^2}{v(a)}
\ge\frac{f_*^2}{B(1)^2}=k>0.
\]

This proves (22)–(23). Merely having $f>0$ and a time-dependent upper bound for $v$ would not by itself imply eventual hitting; the monotone ratio supplies the fixed positive slope needed here.

The width restriction $n>2c$ ensures $f(0)\le2c/n<1$. Continuity, monotonicity, and $f(s)\ge f(a)+k(s-a)$ for $s\ge a$ imply a first root $f(s_\dagger)=1$ with

\[
0<s_\dagger\le a+1/k=S_\dagger.
\]

The case of a root before $a$ also satisfies this bound. The strict derivative bounds on the initial interval and afterwards imply strict increase, so there is no later plateau at level one or second crossing.

For the scalar ODE $s'=2(1-f(s))$, the function $f$ is $C^1$ and its derivative is bounded on $[0,S_\dagger]$, as verified above. Hence its scalar vector field is Lipschitz there. Below $s_\dagger$, it is strictly positive; at $s_\dagger$, it vanishes.

To check nonattainment directly, let $C_f$ bound $f'$ on this interval and set $y(t)=s_\dagger-s(t)$. Before a putative first hitting time,

\[
0<1-f(s(t))=f(s_\dagger)-f(s(t))\le C_fy(t),
\]

so $y'(t)\ge-2C_fy(t)$ and $y(t)\ge s_\dagger e^{-2C_ft}>0$. The root cannot be attained at a finite time. This is also a consequence of local uniqueness, as in the candidate. Boundedness of $s(t)$, together with local existence at its possible endpoint, gives continuation for all physical times.

The increasing bounded clock has a limit. If it were less than $s_\dagger$, continuity would leave its speed bounded below by a positive constant for all sufficiently large times, a contradiction. Therefore

\[
\lim_{t\to\infty}s(t)=s_\dagger,
\qquad
\int_0^\infty2(1-f(s(t)))\,dt=s_\dagger\le S_\dagger.
\]

The actual endpoint $s_\dagger$ can depend on $R,n$ and initialization; $S_\dagger$ is the common upper bound.

Finally, with $L=(f-1)^2$, the metric gradient of the unmodified loss would give the scalar factor $2(1-f)$ multiplying the feature field. Applying that exact factor to this auxiliary field yields

\[
\frac{d}{dt}L(s(t))
=2(f-1)f'\,2(1-f)
=-4(f-1)^2f'\le0.
\]

Thus (24), the clock normalization, and the bounded total feature time are all correct. These facts concern the auxiliary continuous-time trajectory; they do not assert a discrete gradient descent theorem or equality of the modified field with the unmodified gradient when clipping is active.

## 9. Gaussian initialization and conditional averaging

Let $F(x)=\mathbb E\arctan(\sqrt{x}G)^2$ for $x\ge0$. Its finiteness follows from bounded activation, and $F(x)>0$ for $x>0$, since $G\ne0$ almost surely. Thus $v_1=F(1)>0$, $v_2=F(v_1)>0$, and $v_3=F(v_2)>0$.

The continuity used by the candidate has an elementary quantitative verification. Put $g(t)=\arctan(\sqrt t)^2$. For $t>0$,

\[
0\le g'(t)=\frac{\arctan(\sqrt t)}{\sqrt t(1+t)}\le1,
\]

and the continuous derivative limit at zero is one. Therefore

\[
|F(x)-F(y)|
\le\mathbb E|g(xG^2)-g(yG^2)|
\le|x-y|\mathbb EG^2=|x-y|.
\]

This justifies the required continuity without any specialized convergence theorem.

Write $H_j=\|h^{(j)}_0\|_2^2/n$ in this section. The independent bounded first-layer summands have mean $v_1$ and

\[
\mathbb E|H_1-v_1|^2\le c^4/n.
\]

Conditional on $h^{(1)}_0$, each row of $W^{(2)}_0$ produces a centered Gaussian of variance

\[
\frac1n\sum_j(h^{(1)}_{0,j})^2=H_1.
\]

Different rows remain independent under this conditioning. Hence

\[
\mathbb E[H_2\mid h^{(1)}_0]=F(H_1),
\qquad
\operatorname{Var}(H_2\mid h^{(1)}_0)\le c^4/n.
\]

It follows that $H_2-F(H_1)\to0$ in probability, and the continuity of $F$ gives $H_2\to F(v_1)=v_2$ in probability. No unconditional independence of the second-layer activations is needed.

The vector $h^{(2)}_0$ is a function of $z^{(1)}_0,W^{(2)}_0$, and is independent of $W^{(3)}_0$. Conditional on $h^{(2)}_0$, the same row calculation gives independent $N(0,H_2)$ coordinates at the third preactivation, with

\[
\mathbb E[H_3\mid h^{(2)}_0]=F(H_2),
\qquad
\operatorname{Var}(H_3\mid h^{(2)}_0)\le c^4/n.
\]

Consequently $H_3\to v_3$ in probability. These conditionings are valid exactly at initialization; no analogous independence during training is used.

For an explicit elementary failure bound, define

\[
\Delta_1=H_1-v_1,
\quad\Delta_2=H_2-F(H_1),
\quad\Delta_3=H_3-F(H_2).
\]

Each has second moment at most $c^4/n$, and the Lipschitz bound for $F$ gives

\[
|H_3-v_3|\le|\Delta_1|+|\Delta_2|+|\Delta_3|.
\]

Chebyshev's inequality and a union bound therefore yield

\[
\mathbb P(H_1<v_1/2)\le\frac{4c^4}{nv_1^2},
\qquad
\mathbb P(H_3<v_3/2)\le\frac{108c^4}{nv_3^2}.
\]

Independence among the three errors is unnecessary.

For the matrix operator bound, a maximal $1/4$-separated subset of the Euclidean unit sphere is a $1/4$-net. The disjoint balls of radius $1/8$ about its points lie in the ball of radius $9/8$, so a volume comparison gives at most $9^n$ points. If $x_0,y_0$ approximate unit vectors $x,y$ within $1/4$,

\[
|y^TWx-y_0^TWx_0|
\le(\|y-y_0\|_2+\|x-x_0\|_2)\|W\|_{\rm op}
\le\tfrac12\|W\|_{\rm op}.
\]

Taking the supremum gives $\|W\|_{\rm op}\le2\max_{x_0,y_0}|y_0^TWx_0|$. Each fixed bilinear form for the stated Gaussian matrix has variance $1/n$, since the sum of squared coefficients is one. The elementary Gaussian tail bound therefore gives

\[
\mathbb P(\|W\|_{\rm op}>8)
\le9^{2n}\,2e^{-8n}
=2e^{-(8-2\log9)n}.
\]

The exponent is positive, and a union bound doubles this bound for the two matrices. This verifies the net size, the approximation factor, and the precise exponent in lines 328–333.

For independent standard normal coordinates, $n^{-1}\sum_iG_i^2$ has mean one and variance $2/n$. Thus

\[
\mathbb P(\|z^{(1)}_0\|_2/\sqrt n>2)\le\frac2{9n}.
\]

Writing $W^{(4)}_0=G^{(4)}/n$, the readout event in (14) is exactly $\|G^{(4)}\|_2/\sqrt n\le2$, so its failure probability has the same bound. Finally,

\[
\mathbb P(\|W^{(4)}_0\|_\infty>1)
\le\sum_{i=1}^n\mathbb P(|G_i^{(4)}|>n)
\le2n e^{-n^2/2}.
\]

Combining all these estimates gives, for example,

\[
\mathbb P(E_n^c)
\le\frac{4c^4}{nv_1^2}
+\frac{108c^4}{nv_3^2}
+\frac4{9n}
+4e^{-(8-2\log9)n}
+2n e^{-n^2/2}\longrightarrow0.
\]

This extra explicit bound is not needed by the note, but verifies its probability claim using only the elementary Gaussian and averaging facts it invokes. Intersecting the operator and activation events does not require conditional independence after imposing the operator event; the calculation precedes that intersection, which is handled by a union bound.

The event $E_n$, all constants, and $N_0$ are independent of $R$. Subsequent arguments are deterministic for every state in the event. This establishes the stated same-event uniformity over the uncountable set of positive caps without any probabilistic intersection over that set.

## 10. New Section 8: exact work excess and the bounded-test defect

All claims in candidate lines 362–425 are valid. They concern an actual equation evaluated along the current auxiliary path.

Let $d=\delta^{(2)}$, $u=u_R$, and $e_R=M(d-u)$. Fix a coordinate $i$. At an interior coordinate, both sufficiently small positive and negative variations are feasible in (5), which forces $[M(u-d)]_i=0$. At an upper face, take $v=u-\varepsilon e_i$, where $e_i$ here denotes the coordinate unit vector. Then

\[
-\varepsilon[M(u-d)]_i\ge0,
\]

so $e_{R,i}\ge0$. At a lower face, the allowed positive variation gives $e_{R,i}\le0$. Thus (27) has the correct signs even for a non-diagonal matrix $M$. It is the metric residual $e_R$, not necessarily the raw coordinate difference $d-u$, that vanishes at interior coordinates.

Since $R>0$, upper and lower faces are disjoint. Coordinate by coordinate,

\[
u_i e_{R,i}=R|e_{R,i}|.
\]

This includes interior coordinates, where both sides vanish, and boundary coordinates with a zero multiplier. Symmetry of $M$ now gives the exact identity

\[
\frac{(d-u)^TMu}{n}
=\frac{u^Te_R}{n}
=\frac Rn\sum_i|e_{R,i}|.
\]

Combining this with the exact energy decomposition established earlier in this report yields

\[
f'=\|\theta'\|_g^2+\frac Rn\sum_i|e_{R,i}|.
\]

Integrating on $[0,S]$ proves the stronger equality

\[
R\int_0^S\frac1n\sum_i|e_{R,i}(s)|\,ds
=f(S)-f(0)-\int_0^S\|\theta'(s)\|_g^2\,ds
\le D(S).
\]

This is precisely (29). No possibly negative term is discarded. Coercivity and the supremum bound on $u_R$ are not needed for this inequality; the same estimate applies when $S<a$.

Differentiating the second forward product gives $(z^{(2)})'=Mu_R$, as already verified. Therefore

\[
(z^{(2)})'-M\delta^{(2)}=-e_R.
\]

The canonical velocity here is evaluated at the auxiliary state itself. It is not the velocity along a different canonical solution, so no path-comparison assumption is hidden in (30).

For any measurable test $a(s)$ satisfying $|a_i(s)|\le1$,

\[
\left|\int_0^S\frac1n a(s)^T
\bigl[(z^{(2)})'-M\delta^{(2)}\bigr]\,ds\right|
\le\int_0^S\frac1n\sum_i|e_{R,i}|\,ds
\le\frac{D(S)}R.
\]

This estimate is deterministic and uniform over the entire indicated test class. The test may depend on the trajectory or on the defect itself. There is no independence or predictability requirement. In particular, the measurable coordinatewise sign of $e_R$ is an admissible test, so the underlying normalized spacetime $L^1$ estimate is real and not merely a claim for a selected collection of smooth tests.

If $\chi$ is $C^1$ with $\|\chi'\|_\infty\le1$, the trajectory $z^{(2)}$ is $C^1$, so the ordinary chain rule gives

\[
\frac1n\sum_i[\chi(z_i^{(2)}(S))-\chi(z_i^{(2)}(0))]
=\int_0^S\frac1n\sum_i
\chi'(z_i^{(2)}(s))(z_i^{(2)})'(s)\,ds.
\]

Substitution of $(z^{(2)})'=M\delta^{(2)}-e_R$ and the preceding test estimate give exactly (32). Boundedness of $\chi$ itself is unnecessary: at finite width on a finite horizon every coordinate is finite and the chain rule applies. It is the global derivative bound that controls the source pairing. For a derivative bound $C$ instead of one, the same proof gives $CD(S)/R$.

For physical time, write $\alpha(t)=2(1-f(s(t)))>0$ for every finite $t$. The exact equation becomes

\[
\frac{d}{dt}z^{(2)}(s(t))
=\alpha(t)M(s(t))\delta^{(2)}(s(t))
-\alpha(t)e_R(s(t)).
\]

On any finite $[0,T]$, the clock is strictly increasing and $C^1$, with positive derivative, so change of variables gives

\[
\begin{aligned}
\int_0^T\frac1n\sum_i
|\alpha(t)e_{R,i}(s(t))|\,dt
&=\int_0^{s(T)}\frac1n\sum_i|e_{R,i}(s)|\,ds\\
&\le\int_0^{S_\dagger}\frac1n\sum_i|e_{R,i}(s)|\,ds\\
&\le D(S_\dagger)/R.
\end{aligned}
\]

Every bounded physical-time test is controlled by this absolute source estimate, including trajectory-dependent tests. The same calculation gives the physical-time empirical chain rule with canonical term $\alpha M\delta^{(2)}$. The bound is independent of $T$; taking the increasing limit in the nonnegative source integral also bounds its total integral over all physical times.

This transfer does not discard a factor of two or require a positive lower bound on $\alpha$ uniform as $t\to\infty$. Nor does it establish a bound on the *unscaled* integral $\int|e_R(s(t))|\,dt$. The actual physical equation contains the factor $\alpha$, which is exactly what permits the substitution.

## 11. New Section 8: support and strict topology limitations

The support statement in lines 427–429 follows from the correct object $e_R$. If $e_{R,i}\ne0$, (27) implies $|u_{R,i}|=R$. Thus

\[
R^2\#\{i:e_{R,i}\ne0\}
\le\|u_R\|_2^2\le nU(S)^2.
\]

The support fraction is at most $U(S)^2/R^2$. The cardinality is of course an integer, so this also forces empty support for sufficiently large $R$ at each fixed $n$.

Neither this support estimate nor the spacetime $L^1$ estimate supplies a *width-uniform* vanishing normalized $L^2$ estimate. An elementary norm example makes the limitation precise. For an integer $m$, take $R=m$, $n=m^2$, and a constant vector $e=m e_1$ on the unit time interval. Then

\[
\frac{\#\operatorname{supp}e}{n}=\frac1{R^2},
\qquad
\frac{\|e\|_1}{n}=\frac1R,
\qquad
\frac{\|e\|_2}{\sqrt n}=1,
\qquad
\frac{R\|e\|_1}{n}=1.
\]

Even the projection sign and work identities are compatible with these numbers: set $M=I$, $u=m e_1$, and $d=2m e_1$, so $u=P_M(d)$ in the box of cap $m$. This is a direct algebraic demonstration of what these estimates alone cannot imply. It is not asserted to be a solution of the network ODE, and no numerical experiment is involved.

Uniform RMS bounds on $e_R$ in addition to its small $L^1$ norm would still allow this example. A vanishing $L^2$ conclusion would need more, such as suitable uniform integrability of the squared entries. Such input is not proved in the candidate.

Although $M^{-1}$ exists with $\|M^{-1}\|_{\rm op}\le1/b(S)$, this gives

\[
\frac{\|\delta^{(2)}-u_R\|_2}{\sqrt n}
\le\frac1{b(S)}\frac{\|e_R\|_2}{\sqrt n}.
\]

The right-hand side need not vanish uniformly in width by the available estimates. The inverse-matrix bound consequently does not turn (29) into vanishing RMS lower-parameter velocity defects. Similarly, (28) multiplies the $L^1$ source by $R$, so the integrated work excess is only bounded by $D(S)$, not shown to vanish uniformly in width.

A test weighted by a coordinatewise unbounded middle query, or a $\chi$ with unbounded derivative, is outside the stated test class. RMS control of that weight does not rescue the conclusion without a suitable small $L^2$ source bound. The note correctly refrains from inferring convergence of trajectories, nonlinear operator actions, prediction-energy identities, or population solutions from this one-equation source estimate.

There is one useful editorial clarification, not a mathematical repair: in lines 429–434, “does not show ... tends to zero” and “can remain order one” concern estimates uniform over width as the cap grows. At fixed width they do not describe the behavior for arbitrarily large caps; Section 9 proves that behavior is eventually exactly zero. For complete local explicitness, the author could add “uniformly in width” to the first phrase and “when width may grow with the cap” to the second. The surrounding population exclusions and the explicit fixed-width result in Section 9 already determine this interpretation.

## 12. New Section 9: eventual exact canonical interval consistency

All claims in candidate lines 440–468 are valid on the same event and with the same width threshold as the preceding theorem.

The key estimate holds along every auxiliary trajectory independently of its cap:

\[
\begin{aligned}
\|\delta^{(2)}(s)\|_\infty
&\le\|\delta^{(2)}(s)\|_2\\
&\le\|(W^{(3)}(s))^T\delta^{(3)}(s)\|_2\\
&\le\sqrt n\,A_3(S)B(S)
\qquad(0\le s\le S).
\end{aligned}
\]

The middle inequality uses $|\phi'|\le1$. This bound follows already from (12) and the definition of $\delta^{(2)}$; references to (19)–(20) in the candidate are harmless extra dependencies, and no circular estimate of a canonical solution is used.

Fix $n$, $S\ge a$, and a cap

\[
R\ge R_*(n,S):=\sqrt n\,A_3(S)B(S).
\]

On the entire auxiliary interval, $\delta^{(2)}$ lies in the closed box. Its objective in (3) is zero and strict positive definiteness of $M$ makes it the unique minimizer. Hence $u_R=\delta^{(2)}$ at every time on that interval. Equality in the displayed cap threshold suffices: a coordinate may lie on the box boundary, but feasibility still forces the minimizer to be the full vector and the modification to vanish.

It follows that the *whole parameter trajectory*, not just its second-preactivation equation, solves the raw canonical feature ODE on $[0,S]$. That raw field is smooth in the finite-dimensional parameter variables. Its local existence and uniqueness are elementary, and the constructed auxiliary path supplies existence throughout the entire interval. No prior global canonical theorem is required.

Two caps satisfying this threshold start at the same state and solve that same smooth raw ODE. Local uniqueness propagates agreement along their common interval, so their parameter paths are identical on $[0,S]$. Their predictions, forward activations, full backward fields, and work excesses therefore agree there as well, and the work excess is zero.

This is an interval statement with quantifiers

\[
\forall n\ge N_0,\ \forall S\ge a,\ \forall\theta_0\in E_n,\
\forall R\ge R_*(n,S).
\]

Its sufficient threshold is deterministic for the indicated width and horizon. It is independent of the individual realized initial state in $E_n$ and of any comparison path.

For physical time, take $S=S_\dagger$, which is fixed by the preceding cap-independent constants. For each such cap, its feature path agrees with the canonical path on that whole interval. All these paths have the same first root $f=1$, and their scalar clocks solve the identical locally Lipschitz ODE with the same initial condition. Consequently their clocks agree for every physical time.

The physical trajectory remains below that first root in $[0,S_\dagger]$. Therefore it solves the raw canonical continuous physical ODE for all $t\ge0$. This constructs a global physical solution and identifies it uniquely with any canonical local solution with that initialization, since the raw physical field is smooth as well. There is no appeal to a pre-existing population or global-flow theorem.

The conclusion is eventual equality, stronger than a fixed-width limiting approximation: for every fixed eligible $n$, all sufficiently large caps give identical canonical physical trajectories for all physical times. It does not establish a discrete optimization theorem.

The sufficient threshold grows as $\sqrt n$ for fixed $S$. This is not a proof that such growth is necessary; it is the width-dependent sufficient condition that was actually obtained. It provides neither a width-independent threshold nor a smaller asserted cap regime. It does not justify exchanging width and cap limits, a fixed-cap population construction, or a population limit of a growing-cap diagonal sequence. No such conclusion is asserted in Section 9.

## 13. Adversarial conclusions and scope exclusions

The following potential failure mechanisms do not produce gaps:

- Non-diagonal projection can distort Euclidean norms, but the proof uses its own metric inequality and introduces the coercivity factor only after proving noncollapse.
- A tiny or negative initial prediction does not enter a denominator. The initial displacement estimates establish a uniform interval, and its readout contribution supplies the positive prediction used afterwards.
- Bounded energy is not incorrectly treated as an immediate supremum-velocity estimate. It first gives displacement and operator bounds; the uniform supremum estimates follow after coercivity.
- Saturating lower gates or very small caps cannot cause a finite-time collapse consistent with the established positive prediction and bounded forward operators/readout.
- Nonsmooth changes of the active box constraints do not require differentiating the projection. Finite-dimensional local Lipschitz continuity is enough for the ODE; smooth network observables can be differentiated along its $C^1$ solution.
- The readout ratio is differentiated only where the readout norm and prediction are strictly positive. Its monotonicity supplies a fixed slope and a uniform first-root bound.
- Feature time and physical time are distinguished, including the factor two in the clock and the factor four in the loss derivative.
- The initial Gaussian arguments condition only on quantities independent of the next fresh matrix. They do not assert trained-coordinate independence or rely on a distribution theorem for reused matrices.
- The cap-independent constants are deterministic and the width restrictions are imposed before asserting the full theorem. There is no hidden cap-dependent probability event or width threshold.
- The source estimate uses the normal residual $M(\delta^{(2)}-u_R)$, whose support and signs are fixed by the box variational inequality. Its exact work identity yields a genuine normalized spacetime $L^1$ bound and all stated bounded-test consequences.
- The physical source includes the actual clock factor, so the infinite physical horizon introduces no unaccounted accumulation.
- Fixed-width eventual equality follows from a bound along the entire auxiliary trajectory and smooth raw-ODE uniqueness. It does not presume an uncut trajectory or a population theorem.

The certification covers every scoped finite-width claim in the entire final nine-section candidate, including the probability event, global auxiliary dynamics, physical clock, quantitative middle-equation defect and empirical chain rule, and exact canonical consistency at fixed width. It is not limited to a lemma fragment.

It does not certify a fixed-cap population flow, uniform RMS stability with respect to state perturbations, width-uniform vanishing $L^2$ defects or work excess, population clipping removal, an interchange of width and cap limits, a coordinate-tail bound, a discrete gradient descent result, or any full uncut population theorem. Those exclusions coexist with the explicitly certified eventual equality and zero work excess at each fixed finite width.

Final verdict: **PASS for the entire updated note at SHA256 `d2d10248021a9cb01ab8a6f2358ecfbef4ce6abdad8107654e00dfa38870abb5`. No mathematical fixes are required.** The former `9045...` candidate and any intermediate revision are superseded.
