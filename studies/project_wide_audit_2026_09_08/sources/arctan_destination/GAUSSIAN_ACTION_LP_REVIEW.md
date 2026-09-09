# Independent audit: Gaussian action higher-moment obstruction

## Verdict

**PASS.** The candidate proves the stated obstruction for every finite
\(p>2\): the canonical initial action on the entire generated coordinate
spaces has no bounded \(L^\infty\to L^p\) restriction and no bounded
\(L^p\to L^p\) restriction agreeing with its generated inputs. The same
conclusion holds for its population adjoint. The witnesses are bounded
inputs in the **same** spaces, obtained using the existing constants and
matrix actions, without additional roots. Every individual witness and
its output have all finite population moments.

I found no mathematical gap requiring correction. Below I expand the
candidate's compressed convergence and approximation arguments, including
the exact conditioning behind matrix reuse. This verdict concerns the
initial generated action only. It does not assert anything negative about
the trained trajectory or the desired global theorem.

## Audited artifacts and provenance

The following are the SHA256 hashes of the files actually read:

| Artifact | Absolute path | SHA256 |
| --- | --- | --- |
| Candidate | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/GAUSSIAN_ACTION_LP_OBSTRUCTION.md` | `66bab078eb40ac789cf4f818485db07aaec7c1b4f6c9b3b5eb254d5d89bf322c` |
| Common-space dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/LOCAL_ACTION_SPACE_AND_FLOW.md` | `a61dda52b01e6f44c2bc5cb345d442e84ff6a7dd0de30bc709aa85bf18490482` |
| Gaussian-conditioning dependency | `/tmp/l3-supervisor-recovery-59x8oL/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md` | `ba5cd7a52674a2031bf18ccb633bbb6eeeadd8f2a207369b38695d66ec40c03a` |

I read the solve-math-rigorously skill instructions myself. Mathematical
evidence was restricted to the candidate and these two dependencies. I
did not inspect master ledgers, prior reviews, other research notes, or
parent history, and did not use numerical experiments. The common-space
dependency's assertion that an earlier review passed was not treated as
evidence. Its clipped-flow conclusions are unnecessary for this verdict.

The candidate's line 65 names `/tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md`.
For this audit, that reference was resolved to the explicit dependency
path supplied by the user and hashed above. This is a reference-path
discrepancy, not a mathematical defect in the argument using that supplied
dependency.

## 1. Statement, domains, and admissible operations

Write
\[
 W:L^2(\Omega_2)\longrightarrow L^2(\Omega_3),\qquad
 W^*:L^2(\Omega_3)\longrightarrow L^2(\Omega_2).
\]
These are the population actions constructed in lines 18–93 of the
common-space dependency. The star is a Hilbert-space adjoint, characterized
by
\[
 E_3[VWU]=E_2[U W^*V].
\]
In the finite calculation, \(W_n^T\) means the ordinary matrix transpose.
The exact identity
\[
 n^{-1}v^TW_nu=n^{-1}u^TW_n^Tv
\]
passes to the displayed population adjoint identity through joint
second-moment convergence. The two notations must not be identified as
literal operations on the same underlying objects.

Both probability spaces have total mass one. Thus \(L^\infty\) and
\(L^p\), for \(p>2\), are contained in \(L^2\), so \(Wh\) is defined
for every input in the candidate's supremum. The issue is the existence
of a finite operator bound into \(L^p\), not the existence of the
underlying \(L^2\) action.

Fix \(0<\varepsilon\le1\), and abbreviate
\[
 f(x)=\psi(x/\varepsilon),\quad
 v=E f(G)^2,\quad
 g_0(x)=\tanh(x/\sqrt v).
\]
The plateau of \(\psi\) gives \(v>0\). Both coordinate maps are bounded,
smooth, and globally Lipschitz, with bounds
\[
 \operatorname{Lip}(f)\le\|\psi'\|_\infty/\varepsilon,
 \qquad \operatorname{Lip}(g_0)\le v^{-1/2}<\infty.
\]
Their constants need not be uniform as \(\varepsilon\downarrow0\), and
the candidate explicitly permits this. The only matrix queries are
\(W\mathbf1\), \(W^*f(W\mathbf1)\), and \(Wg_0(W^*f(W\mathbf1))\).
The constant vector on each layer is already an allowed root. The
deterministic number \(v\) is fixed before executing the program.

## 2. Exact first and second conditioning steps

Use \(\|u\|_n=\|u\|_2/\sqrt n\) and
\(\langle u,w\rangle_n=u^Tw/n\) for finite vectors. Let
\(W_n\) have independent \(N(0,1/n)\) entries, set
\[
 y=W_n\mathbf1,\quad e=f(y),\quad
 a_n=\langle y,e\rangle_n,\quad v_n=\|e\|_n^2,\quad
 P=I-\mathbf1\mathbf1^T/n.
\]
Each row sum \(y_i\) is standard Gaussian, and the row sums are
independent. Gaussian row projection gives the exact conditional law
\[
 W_n\mid y\ \overset d=\ y\mathbf1^T/n+Z_nP,
\]
where \(Z_n\) is an independent matrix with the original Gaussian law.
Consequently, conditional on \(y\),
\[
 q=W_n^Te\ \overset d=\ a_n\mathbf1+\sqrt{v_n}Pg,
 \qquad g\sim N(0,I_n),\quad g\perp y.
 \tag{A}
\]
Indeed, \(Z_n^Te\) has covariance \(v_n I_n\), and multiplication by
\(P\) imposes the exact compatibility constraint
\(\mathbf1^Tq=na_n\). This proves candidate equation (5), including
the finite correction along the constant vector.

For the second conditioning, \(e\) is fixed once \(y\) is known. On
\(v_n>0\), put \(r=q-a_n\mathbf1\); then \(Pr=r\). Conditioning the
remaining Gaussian matrix \(Z_nP\) on its contraction with \(e\)
gives
\[
 W_n\mid(y,q)\ \overset d=
 \frac{y\mathbf1^T}{n}
 +\frac{er^T}{nv_n}
 +P_{e^\perp}\widetilde W_nP,
 \quad P_{e^\perp}=I-\frac{ee^T}{nv_n},
 \tag{B}
\]
where \(\widetilde W_n\) is independent of the transcript. The first
two terms satisfy both constraints: multiplying them by \(\mathbf1\)
gives \(y\), and transposing and multiplying by \(e\) gives
\(a_n\mathbf1+r=q\). The final term satisfies both homogeneous
constraints and has the Gaussian covariance of the orthogonal residual.
This establishes candidate equation (6).

Now \(h=g_0(q)\) is measurable from \((y,q)\). Define
\[
 m_n=\langle\mathbf1,h\rangle_n,\quad
 s_n=\|Ph\|_n,\quad
 b_n=\frac{\langle q-a_n\mathbf1,h\rangle_n}{v_n}.
\]
Applying (B) to \(h\) gives precisely
\[
 W_nh\mid(y,q)\ \overset d=
 m_ny+b_ne+s_nP_{e^\perp}g',
 \qquad g'\sim N(0,I_n),
 \tag{C}
\]
with \(g'\) independent of \((y,q)\). In particular, the term
\(b_ne\) cannot be discarded or replaced by independent noise. It is
the dependence caused by using the same matrix in both directions.

There is no hidden division-by-zero issue. Since
\(f(y_i)=1\) when \(|y_i|\le\varepsilon/2\),
\[
 P(v_n=0)\le
 \bigl(1-P(|G|\le\varepsilon/2)\bigr)^n\longrightarrow0.
\]
On that exceptional event the actual program has \(e=q=h=W_nh=0\).
One can assign arbitrary values to the auxiliary coefficients there;
the event has no effect on convergence in probability.

## 3. Joint empirical convergence despite matrix reuse

All limits in this section take \(n\to\infty\) for fixed
\(\varepsilon\). Law of large numbers gives
\[
 a_n\to E[Gf(G)]=0,\qquad v_n\to v>0,
\]
where the zero uses that \(f\) is even. Realize (A) using independent
Gaussian vectors \(y\) and \(g\), and write
\(\bar g=n^{-1}\sum_j g_j\). Then
\[
 \|q-\sqrt v\,g\|_n
 \le |a_n|+|\sqrt{v_n}-\sqrt v|\,\|g\|_n
       +\sqrt{v_n}|\bar g|\longrightarrow0
 \tag{D}
\]
in probability. The Lipschitz bound of \(g_0\) gives
\[
 \|h-\tanh g\|_n\longrightarrow0.
\]
Thus the empirical joint law of the layer-2 tuple \((q_j,h_j)\)
converges in \(W_2\) in probability to
\((\sqrt v G,\tanh G)\). In particular,
\[
 m_n\to0,\qquad
 s_n^2=\|h\|_n^2-m_n^2\to
 \sigma^2:=E\tanh^2G>0.
\]

The pairing in \(b_n\) also converges, rather than merely its
marginals. Namely, (D) and the bound on \(h\) imply
\[
 \begin{aligned}
 &\left|\langle q-a_n\mathbf1,h\rangle_n
       -\sqrt v\,\langle g,\tanh g\rangle_n\right|\\
 &\quad\le
 \|q-a_n\mathbf1-\sqrt v\,g\|_n\|h\|_n
 +\sqrt v\,\|g\|_n\|h-\tanh g\|_n\longrightarrow0.
 \end{aligned}
\]
The iid average \(\langle g,\tanh g\rangle_n\) converges to
\(E[G\tanh G]\); its summands are integrable since
\(|G\tanh G|\le|G|\). Integration by parts yields
\[
 E[G\tanh G]=E\operatorname{sech}^2G=:c>0,
\]
with a vanishing boundary term because \(\tanh\) is bounded and the
Gaussian density tends to zero. It follows that
\[
 b_n\to b:=c/\sqrt v.
\]

To check the final layer-3 tuple, couple (C) with
\[
 t_i^0=b f(y_i)+\sigma g'_i.
\]
The removed Gaussian projection obeys, conditional on \((y,q)\),
\[
 E\bigl[\|(I-P_{e^\perp})g'\|_n^2\mid y,q\bigr]=1/n.
\]
Hence it tends to zero in probability by Markov's inequality. Since
\(s_n\le\|h\|_n\le1\), (C) gives
\[
 \begin{aligned}
 \|W_nh-t^0\|_n
 &\le |m_n|\|y\|_n+|b_n-b|\sqrt{v_n}
       +|s_n-\sigma|\|g'\|_n\\
 &\qquad+s_n\|(I-P_{e^\perp})g'\|_n
 \longrightarrow0
 \end{aligned}
 \tag{E}
\]
under this exact conditional-law coupling. The pairs \((y_i,g'_i)\)
are iid pairs of independent standard Gaussians. Their transformed
triples \((y_i,f(y_i),t_i^0)\) therefore have the deterministic limit
\[
 (Y,f(Y),\sigma H+b f(Y)),\qquad Y\perp H,quad Y,H\sim N(0,1).
 \tag{F}
\]

For clarity, the empirical convergence fact being used here is that iid
vectors with finite second moment have empirical laws converging in
\(W_2\) in probability. It follows by first restricting to a large
bounded set, partitioning that set into finitely many small cells and
applying the law of large numbers to cell frequencies, and controlling
the discarded squared-distance cost by the second-moment tails. All
the ideal tuples above have finite second moments. Coupling equal-index
tuples bounds the squared empirical \(W_2\) distance by the normalized
squared error in (D) or (E), proving the asserted joint convergence for
the actual program. In particular, continuous same-layer measurements
of at most quadratic growth converge: truncate the measurement on a
large ball, use weak convergence there, and use uniform integrability
of the squared norms for the remaining tail.

This is joint convergence of \((q,h)\) on layer 2 and of
\((y,e,W_nh)\) on layer 3. It does not assert independence of actual
coordinates after reuse. Nor does it pair a row-layer coordinate with a
column-layer coordinate in a population average. The vectors \(g\) and
\(g'\) belong to the respective conditional representations, not to an
identification of the two neuron populations.

## 4. Agreement with the source-rule dependency

The general finite-program lemma in lines 89–165 of the source
dependency applies to deterministic coefficients, finitely many
reusable independent Gaussian matrices, iid roots independent of those
matrices with finite second moments, and globally Lipschitz \(C^1\)
coordinate maps with bounded first derivatives. The constant-only
subprogram here satisfies those assumptions; the unused original roots
do not change its marginal law. The constants controlling the maps are
finite at each fixed \(\varepsilon\).

The first forward call has variance \(E\mathbf1^2=1\). The response
of the transpose call along its previous constant input is
\[
 E f'(Y)=E[Yf(Y)]=0.
\]
The first equality follows by Gaussian integration by parts for the
smooth bounded compactly supported function \(f\); the second is
oddness of \(Yf(Y)\). Thus \(q\) has limiting law \(\sqrt vG\).
In the last forward call the expected derivative of the input with
respect to the unstandardized transpose source \(q\) is
\[
 E g_0'(\sqrt vG)=c/\sqrt v.
\]
The final forward Gaussian source has variance
\(E\tanh^2G=\sigma^2\), and its covariance with the first source is
\(E\tanh G=0\). Joint Gaussianity then gives their independence.
The resulting law is exactly (F), which independently followed from
the finite conditioning calculation.

The relevant limiting input Gram entries are \(1\) and \(v>0\);
the two forward inputs have Gram matrix
\(\operatorname{diag}(1,\sigma^2)\). Thus this three-query calculation
does not require any auxiliary input roots to remove singularities.
The temporary noisy roots in the dependency's more general proof are
not inputs of the candidate's program.

## 5. All witnesses lie on the original generated spaces

This point is necessary: separate marginal constructions for each
\(\varepsilon\) would not by themselves prove an unbounded norm for
one fixed action. The common-space dependency supplies the needed
identification, and its approximation argument applies here as follows.

That dependency includes constants, rational combinations, matrix
queries in both directions, a countable family dense on compact sets,
and bounded clipping maps. Finite unions have consistent limiting laws.
The exact matrix inequalities yield continuous operators \(W,W^*\),
each with \(L^2\) norm at most 10, on the generated spaces. The
generation by coordinate slots and approximation of bounded cylinder
functions give density in \(L^2\). Exact finite linear identities and
the norm inequality ensure that the operators respect equality of
inputs in \(L^2\); they do not depend on the chosen expression.

The following explicitly realizes the candidate's non-enumerated maps
using those operators. Choose maps \(f_r,g_r\) from the included dense
family, composed with its clipping map \(\tau_1\), so that
\[
 |f_r|,|g_r|\le2,\qquad
 \sup_{|x|\le r}|f_r(x)-f(x)|\le r^{-1},\qquad
 \sup_{|x|\le r}|g_r(x)-g_0(x)|\le r^{-1}.
\]
Such clipping preserves the approximation: \(\tau_1\) is
1-Lipschitz and is the identity on \([-1,1]\), which contains the
ranges of the target maps. These compositions are already permitted
coordinate instructions.

On the existing spaces define
\[
 Y=W\mathbf1,\quad e=f(Y),\quad q=W^*e,
 \quad h=g_0(q),\quad T=Wh,
\]
and the countable-program approximants
\[
 e_r=f_r(Y),\quad q_r=W^*e_r,\quad
 h_r=g_r(q_r),\quad T_r=Wh_r.
\]
Since \(Y\) is an existing coordinate and \(f\) is measurable and
bounded, \(e\) already belongs to \(L^2(\Omega_3)\). The rest are
likewise defined by existing measurable operations and continuous
actions. More quantitatively,
\[
 \|e_r-e\|_2^2\le r^{-2}+9P(|Y|>r)\longrightarrow0,
 \qquad \|q_r-q\|_2\le10\|e_r-e\|_2.
\]
Also \(\|q_r\|_2\le20\), and therefore
\[
 \begin{aligned}
 \|h_r-h\|_2
 &\le \|g_r(q_r)-g_0(q_r)\|_2
        +v^{-1/2}\|q_r-q\|_2,\\
 \|g_r(q_r)-g_0(q_r)\|_2^2
 &\le r^{-2}+9P(|q_r|>r)
 \le r^{-2}+9\|q_r\|_2^2/r^2\longrightarrow0.
 \end{aligned}
\]
It follows that \(T_r\to T\) in \(L^2(\Omega_3)\). These estimates
use the Lipschitz constant of the fixed target \(g_0\); they require
no uniform Lipschitz bound on the approximating family.

The identification with the finite three-query law is also justified,
not simply assumed from this measurability argument. Run the original
and approximating finite programs with the same matrix. On the event
\(\|W_n\|_{\rm op}\le10\), the preceding estimates hold with empirical
norms and empirical tail frequencies. The first tail frequency tends
to \(P(|Y|>r)\), and the intermediate empirical second moments have
the same uniform bound \(\|q_r\|_n\le20\). Thus the finite comparison
error tends to zero by taking the width limit for fixed \(r\), and
then \(r\to\infty\). Each fixed approximating program has its law
on the original coordinate spaces. The population \(L^2\) comparison
and the finite comparison identify the candidate's program there with
(F). Real scalar coefficients can be absorbed into these target maps
or approximated by rationals in the same finite comparison.

Taking \(\varepsilon=1/k\), \(k\ge1\), places a countable sequence
of witnesses in one fixed pair \((\Omega_2,\Omega_3)\) for one fixed
pair of operators \((W,W^*)\). No population sigma-field is enlarged.
In fact the Gaussian symbols in the candidate can be realized from
the existing variables themselves:
\[
 G_\varepsilon=q_\varepsilon/\sqrt{v_\varepsilon}
 \quad\hbox{on }\Omega_2,
\]
\[
 H_\varepsilon=
 \frac{T_\varepsilon-(c/\sqrt{v_\varepsilon})e_\varepsilon}{\sigma}
 \quad\hbox{on }\Omega_3.
\]
The latter has standard Gaussian law and is independent of \(Y\)
by (F). It is a measurable function of generated variables, not a
new input seed. No independence between the variables
\(H_{1/k}\) for different \(k\) is claimed or needed.

## 6. Every moment inference

The limiting input has law \(h_\varepsilon\overset d=\tanh G\).
Because a standard Gaussian has positive probability arbitrarily far
out on either half-line,
\[
 \|h_\varepsilon\|_\infty=1,
 \qquad
 \|h_\varepsilon\|_p=(E|\tanh G|^p)^{1/p}\in(0,1).
\]
The latter number is independent of \(\varepsilon\). The essential
supremum equals 1 even though the function never attains 1 at a
finite argument.

Each fixed program has all finite population moments: \(Y\) and
\(q_\varepsilon\) are Gaussian, \(e_\varepsilon,h_\varepsilon\)
are bounded, and
\[
 T_\varepsilon\overset d=
 \sigma H+(c/\sqrt{v_\varepsilon})\psi(Y/\varepsilon)
\]
is a Gaussian plus a bounded random variable with a finite bound for
fixed \(\varepsilon\). For example, for \(r\ge1\),
\[
 E|T_\varepsilon|^r
 \le2^{r-1}\bigl(\sigma^r E|H|^r
                  +c^r v_\varepsilon^{-r/2}\bigr)<\infty.
\]
Smaller positive moments follow from the first moment. No uniformity
in \(\varepsilon\) is asserted here.

Conditional on \(Y\), the Gaussian term has mean zero. Convexity of
\(|\cdot|^p\), for the present \(p>2\), gives
\[
 E|T_\varepsilon|^p
 \ge c^p v_\varepsilon^{-p/2}
       E\psi(Y/\varepsilon)^p.
\]
There is no cancellation error in this inequality. With
\(\gamma(t)=(2\pi)^{-1/2}e^{-t^2/2}\), support and plateau give
\[
 v_\varepsilon\le
 \int_{-\varepsilon}^{\varepsilon}\gamma(t)\,dt
 \le2\gamma(0)\varepsilon,
\]
\[
 E\psi(Y/\varepsilon)^p\ge
 \int_{-\varepsilon/2}^{\varepsilon/2}\gamma(t)\,dt
 \ge\gamma(1)\varepsilon
 \quad(0<\varepsilon\le1).
\]
The last interval has length \(\varepsilon\), and its density is
at least \(\gamma(1)\). Consequently,
\[
 \|Wh_\varepsilon\|_p
 \ge\frac{c\,\gamma(1)^{1/p}}{\sqrt{2\gamma(0)}}
       \varepsilon^{1/p-1/2}\longrightarrow\infty
 \quad\text{for every finite }p>2.
\]
This proves divergence on the unit ball of \(L^\infty\). Dividing
by the positive constant \((E|\tanh G|^p)^{1/p}\) also proves
divergence of the \(L^p\)-operator ratio on bounded generated inputs.

As a separate check,
\[
 E T_\varepsilon^2=\sigma^2+c^2
\]
because \(H\) is independent of \(Y\), centered, and
\(E\psi(Y/\varepsilon)^2=v_\varepsilon\). This is consistent with
the \(L^2\) action bound. More explicitly,
\(c^2=(E[G\tanh G])^2\le E G^2 E\tanh^2G=\sigma^2\), so these
particular witnesses even satisfy
\(\|Wh_\varepsilon\|_2^2\le2\|h_\varepsilon\|_2^2\).

The higher moments are calculated from the already identified
population distribution. No convergence of finite-width moments of
order greater than two is inferred from \(W_2\) convergence. The
order of limits is fixed \(\varepsilon\), then infinite width, then
\(\varepsilon\downarrow0\); there is no triangular limit requiring
a width-uniform estimate in \(\varepsilon\).

## 7. Reverse direction and exact scope of the obstruction

At finite width \(W_n^T\) itself has independent \(N(0,1/n)\)
entries. Begin with the already available layer-3 constant and use
the program
\[
 \widehat Y=W^*\mathbf1,\quad
 \widehat e_\varepsilon=\psi(\widehat Y/\varepsilon),\quad
 \widehat q_\varepsilon=W\widehat e_\varepsilon,\quad
 \widehat h_\varepsilon=
       \tanh(\widehat q_\varepsilon/\sqrt{v_\varepsilon}),\quad
 \widehat T_\varepsilon=W^*\widehat h_\varepsilon.
\]
The same conditioning and approximation proof, with the populations
exchanged, proves both reverse norm obstructions on the same spaces.
It does not resample the matrix or replace the adjoint by an independent
action.

The candidate therefore establishes the full stated failure of
boundedness for the initial action and its adjoint on their generated
spaces. It supplies no claim that the constructed inputs occur during
training, no estimate with a uniform bound on coordinate sensitivities,
and no negative conclusion about global mean-field or gradient-flow
existence. Its final discussion stays within that scope. Apart from
the reference-path clarification recorded above, no correction is
needed for the mathematical statement or proof.
