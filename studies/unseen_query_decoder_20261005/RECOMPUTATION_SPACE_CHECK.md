# Independent reconstruction of the conditional recomputation evaluator

2026-10-06. Audit scope: `RECOMPUTATION_SPACE.md`, Sections 1–5 only.
Sections 6–10 were read for context but their claims are not certified by
this report. The mathematical input is the already authorized complete
`GENERAL_DENSE_COMPARISON.md`; its linked studies were not opened.

**Verdict.** The globally controlled field, Picard reconstruction and
streamed spectral projection support the claimed conditional polylogarithmic
working-space evaluator. A fully specified statement needs the tolerance
allocation and input qualifications below. They do not change its stated
polylogarithmic exponent. This is not an audit pass for total compression:
the retained information behind the repeatable initialization interface is
still outside the working-space bound.

Reviewed final source SHA-256:
`b7f7e6e14d32b2e22fb1398474e7c3ce5f1033e60d010dc419bd7d8431f49d80`.
The source changed once during the review, from
`4612b710d3ae44283ecac95a65047ef8525802475a7b110aa0106abdd4d6ba39`;
the supervisor confirmed the change completed Section 10 and then froze
the source. Sections 1–5 were reread in full at the final hash.
For a scope-only fingerprint, the text before the `## 6.` heading has
SHA-256 `86ebcae201a960326cf6b6f7e629f2327e1c54bd9c8c9ba0df2b59dc0dfa1e15`
(computed by `sed '/^## 6\. /,$d' RECOMPUTATION_SPACE.md | sha256sum`).
The inherited dense-comparison source hash is
`ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9`.

## 1. Required clarifications and their consequences

1. **Projection error must distinguish operator and entrywise errors.**
   For an $N\times N$ output matrix and target Frobenius error
   $\varepsilon$, allocate at most $\varepsilon/(4\sqrt N)$ to the
   polynomial's uniform scalar error, and the same amount to the sum of
   coefficient errors. These are operator errors, and their Frobenius
   errors are at most $\varepsilon/4$ each. Allocate at most
   $\varepsilon/(2N)$ to the numerical error of each requested entry.
   An entrywise tolerance $\varepsilon/\sqrt N$ would be insufficient.
   Section 4's phrase about putting arithmetic errors into the same budget
   does not make this distinction explicit. The repair requires only
   $O(\log N)$ more precision bits and fits equation (17)'s asymptotic
   bound and the final exponent.

2. **The query and time need a finite-information input model.** Section 1
   states activation and training-data precision assumptions, but the
   unseen $v$ and arbitrary $t$ also require one. It suffices to have
   repeatable coordinate precision access to $v$, and precision access
   to $\min(t,T)$, with the symbol $\infty$ allowed. Count their evaluation
   space and the $O(d p)$ bits holding requested query coordinates.
   Equivalently, for a finite-input version, supply rational queries and
   capped times with their input lengths counted. The proof extends
   uniformly to all sphere queries with such access; it does not encode
   an arbitrary noncomputable real in one free register.

3. **Effective bounds are needed for a uniform compiler.** Selecting
   caps, the carrier coefficient, the field's Lipschitz upper bound and
   the endpoint time requires numerical upper bounds, and a positive
   numerical lower bound for the decay rate. For one fixed problem,
   rational bounds can be hardcoded above or below the inherited finite
   constants, yielding an existential conditional algorithm. A uniform
   algorithm taking arbitrary activation/data descriptions additionally
   needs these certificates supplied or computed. Opaque finite constants
   in the inherited theorem do not give an extraction algorithm. Their
   finite descriptions count with the problem data.

4. **Depth independence presumes a common activation complexity bound.**
   The exponent $\max\{10,4c+2\}$ is independent of $L,m,d$ for a class
   whose activation and derivative evaluators share the stated exponent
   $c$. It is not one absolute exponent over all strip-holomorphic
   activations without the additional computational hypothesis. The
   source correctly recognizes that strip holomorphy alone does not
   imply computability.

The first item is a numerical specification repair; the next three delimit
the conditional computational theorem. None supplies compact initialization
or changes the label/gap allowance.

## 2. Reconstruction of the globally controlled field

The inherited source gives the required fixed physical bounds, the
training-carrier maximum $C\sqrt{\log(en)}$, and whole-sphere exponential
prediction speed on its good event. The present audit accepts that event
at its inherited claim level, rather than reproving its stochastic source.

The displayed singular-value clipping is the Frobenius projection onto
the operator-norm ball. For every admissible comparison matrix $Q$,
$u_i^TQv_i\le B_W$ proves the stated variational inequality. Applying
that inequality to the two projected matrices proves nonexpansiveness.
The vector and first-matrix radial projections obey the corresponding
Euclidean statement. Their direct-sum scaled norm is therefore
nonexpansive as claimed.

Let $d_\theta$ denote the parameter difference norm displayed in source
equation (4). Bounded projected matrix norms and real bounded slopes give
forward feature RMS bounds and feature RMS differences $C d_\theta$.
The projected readout has bounded RMS. Since coordinate clipping cannot
increase the Euclidean norm, backward induction gives bounded backward
RMS even though the coordinate clipping threshold grows with $n$.

For backward differences the changed gate contributes at most
$C M_n d_\theta$, while the changed matrix and incoming backward
field contribute $C d_\theta+B_W$ times the next-layer difference.
Thus the induction is additive in its $M_n$ contributions:

\[
 \frac{\|\widehat\delta^{(\ell)}
       -\widehat{\widetilde\delta}^{(\ell)}\|_2}{\sqrt n}
 \le C_L(1+M_n)d_\theta.
\]

It does not produce $M_n^L$. The residual clip is nonexpansive and has
a fixed amplitude bound. The exact normalized rank-one identity
$\|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)$ proves a
width-independent velocity bound and a Lipschitz coefficient
$K_n\le C_L(1+M_n)$. First-layer and readout blocks have the displayed
RMS normalizations, so no extra factor of $n$ is missing.

On the inherited good trajectory no safeguard is active; the extended
flow is therefore the original flow by uniqueness for a globally
Lipschitz vector field. This reasoning does not require the rounded
initialization or off-trajectory Picard states to satisfy the good event.
The projected query predictor is globally Lipschitz in $d_\theta$ with
a fixed coefficient, using forward subtraction and bounded readout RMS.
No passive-query carrier estimate or sphere union bound is needed.

## 3. Picard truncation, quadrature and common-grid precision

For a bounded $K_n$-Lipschitz field, integrating the velocity bound gives
$\|\theta(t)-\theta_0(t)\|\le Bt$. Repeated integration of the
Lipschitz inequality yields exactly

\[
 \|\theta(t)-\theta_j(t)\|
 \le\frac{B K_n^j t^{j+1}}{(j+1)!}.
\]

Choose $T=O(\log(en))$ and
$J\ge C(K_nT+(a+1)\log(en))$. Since
$(j+1)!\ge((j+1)/e)^{j+1}$, taking $C$ sufficiently large makes
the error at most a fixed fraction of $n^{-a}$. The noncontractive
interval causes no problem. The resulting depth is
$O(\log(en)^{3/2})$, safely enlarged to $O(\log(en)^2)$ in the count.

Every positive Picard iterate has derivative bounded by $B$; the zeroth
is constant. The integrand is therefore $K_nB$-Lipschitz in time, so
the streamed midpoint rule's stated $O(K_nBT^2/Q)$ error is valid.
With a common deterministic grid, every coordinate request defines the
same virtual approximate vector. If each stage adds at most $\eta$ in
the parameter norm, subtracting the two integral recurrences gives

\[
 e_{j+1}\le TK_ne_j+\eta,
 \qquad e_J\le J(1+TK_n)^J\eta.
\]

Thus $\log(\eta^{-1})=O(\log(en)^3)$ is sufficient. In particular,
increasing the quadrature count does not increase stack depth. Its
counter has $O(\log Q)$ bits.
Rounding each of $Q$ streamed contributions must be allocated a tolerance
of order $\eta/Q$ after the coordinate-to-parameter norm factor is
included. This adds $\log Q+O_L(\log n)$ to the required arithmetic
precision, still $O(\log(en)^3)$. A large quadrature count is therefore
not being multiplied by an unbudgeted fixed rounding error.

Coordinate error at most $2^{-p}$ gives first-matrix RMS error at most
$\sqrt d\,2^{-p}$, hidden-matrix Frobenius error at most $n2^{-p}$
per layer, and readout RMS error at most $2^{-p}$. Hence
$p=C\log(en)^3$ covers all coordinate accumulation factors. Time
rounding is controlled by the same $B$-Lipschitz property. Each quadrature
term should be multiplied by its weight before accumulation, as the source
specifies; this keeps accumulator magnitudes polynomial in $n$.

The common input grid is essential. A spectral projection treats its
matrix as the exact matrix of these repeated $p$-bit outputs. It may
perform its own arithmetic at higher precision, but must not recursively
request a preceding Picard iterate at successively higher precision.
The source explicitly imposes this rule and thereby avoids that cascade.

## 4. Spectral projection reconstruction

For the symmetric dilation $H$, a singular-vector pair of $W$ gives
eigenvectors with eigenvalues $\pm\sigma$. Applying the odd scalar
clipping function therefore puts the singular-value clipping of $W$
in the upper-right block. This remains valid at zero and repeated singular
values; no eigenvector algorithm is required by the implementation.

For $g(\alpha)=\psi(R\cos\alpha)$, evenness gives a cosine series and
hence a Chebyshev polynomial. Its Fejér mean has coefficients bounded
by $2B_W$. The normalized kernel integrates to one and is bounded away
from zero by $C/(D\alpha^2)$. Splitting at $D^{-1/2}$ proves the stated
uniform error $C(R+B_W)D^{-1/2}$. Coefficient quadrature uses Lipschitz
constant at most $R+B_Wj$ at mode $j$, so its stated node count bounds
the sum of coefficient errors.

The two product identities for $T_{2r}$ and $T_{2r+1}$ follow from
$\cos(2r\alpha)=2\cos(r\alpha)^2-1$ and
$2\cos(r\alpha)\cos((r+1)\alpha)
 =\cos((2r+1)\alpha)+\cos\alpha$. Their matrix versions hold because
every factor is a polynomial of the same matrix. Their call depth is
$O(\log D)$, with a streamed inner index at matrix multiplication.

Each exact polynomial matrix has operator norm at most one. Inductively,
entrywise errors below one obey a bound of the form
$E_j\le C N(E_{\lceil j/2\rceil}+2^{-b})$ after increasing the
constant to absorb the error-product term. This gives amplification
$(CN)^{C\log D}$. The induction is closed by selecting precision first
so the resulting bound remains below one. The final sum costs another
$\log D$ bits. For a target entrywise arithmetic error $\tau$, it is
sufficient that

\[
 b\ge C\bigl(\log\tau^{-1}
              +\log N\log(D+1)+\log(D+1)\bigr).
\]

Taking $\tau=\varepsilon/(2N)$ and allocating the operator and
coefficient tolerances as in item 1 makes the entire projection's
Frobenius error at most $\varepsilon$. This is the explicit corrected
allocation missing from the source's compressed wording.

Scalar cosine can be evaluated after argument reduction at
$O(b+\log D)$ bits, using a bounded-argument Taylor series and a
computable approximation to $\pi$; all loop counters and series
accumulators fit polynomial space in these bit lengths. At rationally
indexed Fourier quadrature nodes the large integer mode can also be
reduced modulo the quadrature denominator before evaluating the angle.
Radial projections use streamed sums of squares and scalar square roots.
Neither part needs a stored matrix-function or eigendecomposition oracle.

## 5. Absolute exponent, total information and endpoints

Set $\ell_n=\log(en)$. The bounded field places each exact Picard
iterate within $BT$ of its initialization. The approximate iterates are
also bounded after their error budget is imposed. Polynomially bounded
initial coordinates therefore give a known polynomial matrix norm bound
$R$; one may enlarge it to a dyadic power for exact scaling.

With $p=O(\ell_n^3)$, the projection's desired accuracy has logarithm
$O(\ell_n^3)$, so $\log D=O(\ell_n^3)$ and
$b=O(\ell_n^4)$. One projection has
$O(\ell_n^3)$ recursive levels with $O(\ell_n^4)$ bits per level,
or $O(\ell_n^7)$ working bits. A nested network scalar evaluation
adds a factor depending on fixed depth. Nesting all $O(\ell_n^2)$
Picard levels gives $O_L(\ell_n^9)$ before the source's conservative
slack. A scalar activation evaluator costs $O(\ell_n^{4c})$; even
charging one copy at each Picard level gives $O(\ell_n^{4c+2})$.
Consequently the claimed $\ell_n^{\max\{10,4c+2\}}$ upper bound
survives the corrected projection tolerance. Width-loop counters and
query coordinates do not increase this exponent.

Strictly, nested stack depths multiply the per-Picard network/projection
depth by the Picard depth; they are not just their sum. Section 5's
actual multiplication accounts for this, despite the less precise final
sentence about recursion depth in Section 4.

The initialization subroutine's work space $S_0(n)$ is active only when
called at a leaf of this nested evaluation, so it adds once to the peak.
That does not include the information it reads. If $I_0(n,p)$ denotes
the retained initialization representation supporting repeatable $p$-bit
access, the complete information inventory is

\[
 I_0(n,p)+S_0(n)
 +O_{L,m,d,a,\mathrm{data},\phi}
       (\ell_n^{\max\{10,4c+2\}})
 +\text{any uncounted input-interface work space}.                 \tag{A}
\]

Fixed training data, activation programs and numerical certificates must
also be retained; their finite description sizes belong to the indicated
problem-dependent term or must be displayed separately. A direct array of
$nd+(L-1)n^2$ independently initialized coordinates to $p$ bits costs
order $n^2p$ bits. No compact substitute for $I_0$ is proved here. This
is exactly the distinction the source makes; (18) is not a total-storage
bound.

An initial parameter norm error $\varepsilon_0$ propagates by at most
$e^{K_nT}$, from the integral Lipschitz inequality. Since
$K_nT=O(\ell_n^{3/2})$, the stated input precision is sufficient and
the larger common grid covers it. The original good event is used only
for the exact trajectory.

For the endpoint, integrate the inherited speed to obtain

\[
 \sup_{v,t\ge T}|f_n(t,v)-f_n(T,v)|
 \le (C/\kappa)e^{-\kappa T}.
\]

The factor $1/\kappa$ must be included when choosing the fixed constant
in $T=C_a\ell_n$; it does not change its scale. The same bound includes
$t=\infty$. On $[0,T]$ the deterministic numerical estimates and the
projected predictor's Lipschitz bound are uniform in the sphere query.
For the query-input qualification, the projected feature map is Lipschitz
in $v$ on the ball of radius two, with a fixed coefficient: the first
matrix contributes $\|\bar A\|_{\rm op}/\sqrt n\le B_A$, then fixed
hidden operator and slope bounds multiply through the layers. Rounding
each query coordinate sufficiently accurately therefore preserves the
all-query estimate, including when the rounded point is slightly off the
sphere. No new query-dependent random event is needed.

## 6. Check provenance and status

This is a reconstruction of the displayed argument, including dimensions,
coordinate tolerances and recursive workspace. No numerical experiments,
external theorem imports, other agents' reports or other study materials
were used. The reviewer had already authored separate scoped work in this
study; this check is an independent reconstruction of another candidate,
not a fresh-context promotion review.

The rigorous-math and conjecture-investigation instructions previously
read remain applicable. The canonical-notation skill remains inaccessible;
the supplied user conventions and maintained notation contract were used,
as directed. The supervisor supplied the audit assignment and later
confirmed the frozen source version; no other review findings were supplied.

Classification: **conditional evaluator validated with explicit numerical
and input qualifications above; total compression unproved**. The source
should incorporate items 1–4 before calling its computational contract fully
specified. This report edits no candidate, established source or Git index.
HEAD before writing was `3834145d910202a84824d943fe7d7f65714d96f2`, with an
empty shared index.

## 7. Corrective-version verification

The reviewer reread Sections 1–5 completely at source SHA-256
`70827a6f74fc7c72c3c7cd8236021d8bcd93e06024b3f4ef8a6539dd0618cf0f`.
The new text supplies the separate operator and entrywise projection
tolerances, counted query/time precision interfaces, a common activation
complexity exponent, the multiplied nested-stack count, per-quadrature-term
rounding allocation, and the endpoint factor $1/\kappa$. Those corrections
are sufficient for the corresponding findings above; none changes the
space exponent.

The fixed-problem existential conditional evaluator is now validated at
this version. Its effective-constant paragraph correctly distinguishes
hardcoded rational certificates from their uniform extraction. For the
uniform-compiler interpretation, one remaining specification should be
explicit: supply numerical real slope and second-derivative envelopes,
or directly supply certified upper bounds for the field speed $B$, the
coefficient $C_K$ in $K_n\le C_K(1+M_n)$, the projected-prediction
Lipschitz constant and the tail amplitude. Physical parameter caps, the
carrier coefficient and a positive decay-rate lower bound alone do not
provide these numerical constants from an arbitrary activation-evaluation
program. Supplied derivative envelopes and caps yield them by the finite
layer recurrences already reconstructed here. This is an input-certificate
qualification, not a new mathematical stability gap.

The original dense-initialization information remains separately counted,
and no total-compression conclusion is certified. No changes were made to
the candidate or any other file in this corrective check.

## 8. Final certificate qualification resolved

At source SHA-256
`74adb390a71c76ef21831ac76005288d6827fdc8db072dc271b2c0ea32f2dba3`,
the reviewer checked the amended computational-input clause in Section 1.
It now explicitly supplies the activation slope and second-derivative
envelopes, field speed and Lipschitz bounds, and prediction/tail coefficients,
or certified recurrences deriving them from supplied inputs. Their finite
descriptions and evaluator workspace are counted. This resolves the
remaining uniform-compiler qualification in Section 7 of this check.

Final check status for Sections 1–5: **the conditional recomputation
evaluator is validated under its now-explicit computational and numerical
certificate assumptions**. This status includes neither the inherited
probabilistic theorem's independent verification nor a total-storage
compression theorem. The initialization representation remains a separate,
unresolved part of the requested compression target.
