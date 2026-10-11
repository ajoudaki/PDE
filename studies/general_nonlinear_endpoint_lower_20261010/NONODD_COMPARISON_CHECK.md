# Independent review of the nonodd endpoint comparison

2026-10-11. Verdict: **PASS for Section 5, equations (18)–(24), and for the
Section 2 scalar reduction.** The index qualification identified in (4)
was corrected and verified after the frozen review; see the final hash
confirmation below.
The centered endpoint comparison has the stated interpolation normalization,
the bound $D\le\beta^{16L}$, and the original label cap. It uses no
oddness or small-mean assumption. It does not establish endpoint
anti-concentration. The last paragraphs of Section 5 correctly identify a
remaining obligation; the conditional centering adds a transfer requirement
made explicit below.

This was an isolated, targeted mathematical review. I read the five complete
assigned scientific files listed below and the rigorous-math and
canonical-notation skills, including the neural-network reference. I did not
read a study README, history, another review, other studies, or unassigned
manuscript inputs. Sections 3–4 were read for context but their
source-moment assertions were not certified: their cited
`paper/compact_foundations.tex` was not an assigned input. That missing
source is not needed for either reviewed result. No manuscript or research
source was modified.

## Frozen inputs

SHA-256 hashes of the reviewed bytes:

| Input | SHA-256 |
| --- | --- |
| `NONODD_SCALAR_ROUTE.md` | `3d17b9556db340e66a0b25f155e745e791059b0c673a6299d969a832aaf11424` |
| `ODD_DEPTH_ENDPOINT.md` | `e0babb343a9de9a1c16cfbcbb775a7ec7a3f8d4800dcbc216699c5b21c913677` |
| `PRODUCT_QUERY_ROUTE.md` | `d405d3da64274381272d85a01298da21cf5975c3236345264d6a973412343dfd` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |

The first three paths are relative to this study. All equation references
below refer to `NONODD_SCALAR_ROUTE.md` unless another source is named.

## Conditioning and the readout estimate

Let $S=\operatorname{span}\{v_1,\ldots,v_m\}$ be proper and let the unit
query direction $v\in S^\perp$ be fixed before initialization. Condition
on the first-layer coordinates restricted to $S$, and on all initialized
hidden matrices. Call this information the active initialization. Orthogonal
Gaussian projections imply

\[
Z=W_0^{(1)}v\sim N(0,I_n)
\]

independently of the active initialization. The first-layer flow is a sum
of matrices with right factors $v_a^\top$, so

\[
\dot W^{(1)}v=0,\qquad W_t^{(1)}v=Z.
\]

The training trajectory depends only on the active initialization. Applying
the fitting proof to the restriction of the input to $S$ constructs a
fitting event measurable with respect to that same information. This does
not require the Gaussian query to satisfy a conditional sphere feature
bound: the comparison only uses training feature bounds, hidden operator
bounds, and the Gaussian law of $Z$.

Put $\lambda=\gamma/m\le1$, $\varepsilon=Y/\lambda$,

\[
B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n,\qquad
u_t=w_t/\sqrt n,\qquad
u_*=B_0(B_0^\top B_0)^{-1}y,\qquad e=\|u_*\|.
\]

The fitting constants used below are

\[
\begin{gathered}
H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}},\qquad
s=\max(1,\max_j\|\phi_j'\|_\infty),\\
D_j=s(9s)^{L-j},\quad U_1=D_1,\quad U_j=2HD_j\ (j\ge2),\\
F_1=sU_1,\qquad F_j=s(2HU_j+9F_{j-1}),\qquad F=F_L.
\end{gathered}
\]

Here $Q^{(j)}$ is the initialized uncentered population feature Gram
defined in the assigned manuscript, and the derivative norm is on the
real axis.

On the fitting event, $B_0^\top B_0\succeq(\gamma/2)I$, hence

\[
e^2=y^\top(B_0^\top B_0)^{-1}y
\le 2Y^2/\lambda.
\]

I independently checked the readout argument imported from the odd note.
On a finite interval let $M=\sup_t\|u_t\|$ and
$A_t=\int_0^t\rho(s)\,ds$, where
$\rho(t)=\|r(t)\|/\sqrt m$. The fitting coefficients give

\[
\frac{\|B_t-B_0\|_{\rm op}}{\sqrt m}\le2FMA_t,
\qquad A_t\le2\varepsilon.
\]

Using $B_t^\top u_t-y=r_t$ and $B_0^\top u_*=y$, the exact identity
is

\[
\frac12\partial_t\|u_t-u_*\|^2
=-2\rho(t)^2+\frac2m
  \langle(B_t-B_0)^\top u_*,r_t\rangle.
\]

Integration gives $\|u_t-u_*\|^2\le e^2+4FMeA_t^2$.
At a maximizing time, if $M\ge e$, this implies
$M\le2e+4FeA_t^2\le3e$. The last inequality follows from
$16F\varepsilon^2\le1$, which is implied by
$F\le\beta^{10L}$ and $\varepsilon\le\beta^{-30L}$.

Let $P$ project onto the range of $B_0$. Integrating the readout
equation on its orthogonal complement gives

\[
\|(I-P)u_\infty\|\le2FM(2\varepsilon)^2
\le24Fe\varepsilon^2.
\]

Endpoint interpolation gives
$B_0^\top(u_\infty-u_*)=-(B_\infty-B_0)^\top u_\infty$, whence

\[
\|P(u_\infty-u_*)\|
\le4\sqrt{2/\lambda}\,FM^2\varepsilon
\le72Fe\varepsilon^2.
\]

Thus the displayed $120Fe\varepsilon^2$ is a valid loose bound. None
of these steps uses oddness.

The original frozen source had one index defect at line 110: the
unnormalized statement

\[
\|\dot W_t^{(j)}\|_F\le2U_j\rho(t)\|u_t\|
\]

must explicitly be restricted to $2\le j\le L$. For the first layer
the correct version is

\[
\frac{\|\dot W_t^{(1)}\|_F}{\sqrt n}
\le2U_1\rho(t)\|u_t\|.
\]

This follows directly from the different first-layer mobility in (1).
Every use of the unnormalized bound in Sections 2 and 5 has $j\ge2$,
so correcting its stated range changes neither proof nor constants.

## Reconstruction of the mean-adapted comparison

All following expectations are conditional Gaussian expectations over
$Z$. The endpoint hidden matrices and readouts are fixed. The actual
query features satisfy

\[
h_\infty^{(1)}=\phi_1(Z),\qquad
h_\infty^{(j)}=\phi_j(W_\infty^{(j)}h_\infty^{(j-1)}).
\]

The means $\mu_\infty^{(j)}=\mathbb E_Zh_\infty^{(j)}$ are finite
because bounded first derivatives give linear growth and the hidden
operator norms are bounded. Define
$b_j=W_\infty^{(j)}\mu_\infty^{(j-1)}$. Starting from
$\widehat h^{(1)}=\phi_1(Z)$, construct each subsequent comparator
layer using

\[
\widehat\mu^{(j-1)}=\mathbb E_Z\widehat h^{(j-1)},\qquad
\widehat h^{(j)}=
\phi_j\!\left(W_0^{(j)}
 [\widehat h^{(j-1)}-\widehat\mu^{(j-1)}]+b_j\right).
\]

These are successive definitions, not a fixed-point problem. Each $b_j$
is fixed as a function of $Z$; its dependence on the trained state is
allowed in this argument.

Since
$\|W_0^{(j)}\|_{\rm op}\le8$, the comparator map at layer $j$
is $K_j^0=s(8s)^{j-1}$-Lipschitz. For a deterministic vector $c$,
Gaussian Poincaré therefore gives

\[
\operatorname{Var}_Z(c^\top\widehat h^{(j)})
\le\mathbb E_Z\|(D_Z\widehat h^{(j)})^\top c\|^2
\le(K_j^0)^2\|c\|^2.
\]

The applicable Poincaré inequality is
$\operatorname{Var}g(Z)\le\mathbb E\|\nabla g(Z)\|^2$
for Gaussian $Z$ and $g$ in Gaussian $W^{1,2}$. It follows by
orthonormal Hermite expansion, since each nonconstant coefficient receives
weight one in the variance and its total degree in gradient energy. The
Lipschitz maps here satisfy its integrability hypotheses. Summing the
scalar inequality over rows of a deterministic matrix $E$ proves (20).
No independence among $E$, the mixers, and the biases is used.

Put $E_j=W_\infty^{(j)}-W_0^{(j)}$, and define
$R_j=(\mathbb E_Z\|h_\infty^{(j)}-\widehat h^{(j)}\|^2)^{1/2}$.
The two preactivations are

\[
W_\infty^{(j)}(h_\infty^{(j-1)}-\mu_\infty^{(j-1)})+b_j,
\qquad
W_0^{(j)}(\widehat h^{(j-1)}-\widehat\mu^{(j-1)})+b_j.
\]

Subtracting proves (21) exactly. The squared $L^2$ norm of a centered
random vector $V-\mathbb EV$ is
$\mathbb E\|V\|^2-\|\mathbb EV\|^2\le\mathbb E\|V\|^2$.
Consequently the centered difference at the preceding layer has norm at
most $R_{j-1}$, with no factor two. Lipschitz continuity, the moving
operator bound nine, and (20) give

\[
R_1=0,\qquad
R_j\le s(9R_{j-1}+K_{j-1}^0\|E_j\|_F).
\]

The corrected hidden velocity estimate yields
$\|E_j\|_F\le4U_jM\varepsilon$. Unrolling this recursion therefore
gives precisely

\[
T_L=\sum_{j=2}^Ls(9s)^{L-j}U_jK_{j-1}^0,
\qquad R_L\le4M\varepsilon T_L\le12e\varepsilon T_L.
\]

For $\widehat f=u_*^\top\widehat h^{(L)}/\sqrt n$, the exact
decomposition displayed before (24), the scalar covariance estimate,
and contraction under centering give

\[
\begin{aligned}
\|f_n(\infty,\sqrt d\,v)-\widehat f\|_{2,c}
&\le\frac{K_L^0\|u_\infty-u_*\|
             +\|u_\infty\|R_L}{\sqrt n}\\
&\le\frac{120K_L^0Fe\varepsilon^2
             +36T_Le^2\varepsilon}{\sqrt n}.
\end{aligned}
\]

Since $e\le\sqrt2\varepsilon\sqrt\lambda$ and $\lambda\le1$,
$e^2\varepsilon\le\sqrt2e\varepsilon^2$. This proves (24).
The estimate is centered in $Z$, and does not bound its conditional
mean. The vector estimate $R_L$, in contrast, is uncentered.

The constants also check independently. The fitting proof gives
$H\le(2\beta)^L$ and $F\le\beta^{10L}$, while
$K_L^0\le\beta^{2L}$. For $L\ge2$, expanding a summand shows

\[
T_L=2Hs^3\sum_{j=2}^L(9s)^{2L-2j}(8s)^{j-2}
\le2LHs^3(9s)^{2L-4}\le\beta^{7L}.
\]

For example, the last loose bound follows from
$2L\le\beta^L$, $H\le\beta^{2L}$, $s\le\beta$, and
$9s\le\beta^2$. Therefore

\[
D\le120\beta^{12L}+36\sqrt2\,\beta^{7L}\le\beta^{16L}
\]

for $\beta\ge10$, $L\ge2$; after division by
$\beta^{16L}$, the sum is at most
$120\,10^{-8}+36\sqrt2\,10^{-18}<1$. No lower bound on
$Q_{11}^{(L)}$ from the odd endpoint theorem is required here.

## Section 2 scalar reduction

Equations (5)–(11) are correct for a vector $a$ fixed under the active
conditioning and fixed in training time. In particular $a=w_\infty$
is admissible, despite being the terminal readout. The observation about
$a=w_t$ describes the instantaneous response; applying the time
differentiation proof to a varying $a_t$ would require the additional
derivative of $a_t$, which the note does not claim to omit.

Differentiating the product for $J_t^{(L)\top}a$ produces exactly two
types of terms for each $j\ge2$:

\[
J_t^{(j-1)\top}\dot W_t^{(j)\top}
 [\phi_j'(z_t^{(j)})\odot p_t^{(j)}],
\qquad
(D_Zz_t^{(j)})^\top
 [\phi_j''(z_t^{(j)})\odot\dot z_t^{(j)}\odot p_t^{(j)}].
\]

Their bounds are, respectively,

\[
2K_{j-1}^+D_jU_j\rho(t)\|u_t\|\|a\|,
\qquad b_2(9s)^{j-1}\sqrt n\,M_j(t;a).
\]

The identity $9K_{j-1}^+=(9s)^{j-1}$ verifies the latter
coefficient. There is no first-layer time derivative because its query
preactivation equals $Z$. Integrating, applying Minkowski and Gaussian
Poincaré, and dividing by $n$ yields (9), including every power of $n$.

Endpoint passage is legitimate at fixed width: bounded hidden operators
give query norms at most $C(\sqrt n+\|Z\|)$; the velocity recursion
then bounds their time derivatives by
$C\rho(t)\|u_t\|(\sqrt n+\|Z\|)$. Backward factors have norm at
most $C\|a\|$. These bounds are Gaussian integrable and time
integrable because $\sup_t\|u_t\|<\infty$ and
$\int_0^\infty\rho\le2\varepsilon$. They also justify
differentiating the Gaussian means in (10).

For $a=w_\infty$,

\[
\|u_\infty\|\int_0^\infty\rho(t)\|u_t\|\,dt
\le18e^2\varepsilon
\le18\sqrt2e\varepsilon^2,
\]

which verifies (11). The mixed moments $M_j$ remain as written; the
argument does not prove the proposed bound (12). The first two terms of
(10) really do survive inside changed activation derivatives. Centering
the final scalar is not an operation that removes them.

## Remaining anti-concentration obligation

The stated limitation is accurate. Although $W_0^{(L)}$ initially has
independent Gaussian rows, the biases $b_j$ depend on the entire
trained trajectory, hence potentially on all those rows. Earlier
comparator layers may also depend on them. Conditioning on the biases
does not preserve the original independent Gaussian row law without a
new argument. The frozen-feature row CLT from the odd note therefore
cannot be inserted directly. The deterministic covariance upper bound
(20) supplies neither a covariance lower bound nor a CLT. An uncentered
population Gram diagonal is also not a centered conditional covariance
in the readout direction.

The centered nature of (24) must be retained in a later transfer. Let

\[
c=\mathbb E_Z[f_n(\infty,\sqrt d\,v)-\widehat f],\qquad
R=f_n(\infty,\sqrt d\,v)-\widehat f-c.
\]

Then $c$ is active-initialization measurable and uncontrolled, while
$\|R\|_2\le De\varepsilon^2/\sqrt n$. For two independent runs,
the actual endpoint difference is

\[
\widehat f-\widetilde{\widehat f}
 +(c-\widetilde c)+(R-\widetilde R).
\]

Thus a sufficient next result is a conditional small-interval estimate
for the comparator difference uniform over interval centers, on a
high-probability set of active initializations. An alternative may control
the shifts together with the comparator. An unconditional CLT alone does
not automatically provide this transfer because the shifts depend on the
same active initialization. A positive conditional variance, by itself,
also needs distributional or moment control to yield a specified
anti-concentration probability. These are qualifications on the future
step, not failures of (24), and the reviewed note claims no such lower
theorem or counterexample.

The sole required source correction within the reviewed results was to
append $2\le j\le L$ to the last bound in (4), or to display the
separately normalized first-layer bound alongside it. Both clarifications
are now present. The comparison and scalar-reduction results pass this
review. This verdict is an internal check, not promotion or a review of
the unassigned source-moment proof.

## Correction and final hash confirmation

The supervisor subsequently restricted (4) to $2\le j\le L$ and added
the correctly normalized first-layer bound immediately after it. I
verified those edits and the updated SHA-256 of the scalar-route note:

    e741f4acac3fbe222a7763912ecead367e8755f68ce9566cedf208c87a249db5

For an exact check of the change boundary, I removed only those two
edits in a read-only stream and hashed the result. It reproduced the
original frozen hash:

    3d17b9556db340e66a0b25f155e745e791059b0c673a6299d969a832aaf11424

Thus no other source change is included in this confirmation. The
correction resolves the sole required qualification and leaves all
reviewed constants and conclusions unchanged.
