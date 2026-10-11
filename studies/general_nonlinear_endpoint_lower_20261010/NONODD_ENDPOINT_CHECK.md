# Independent check of the last-layer-nonodd endpoint theorem

2026-10-11. **Verdict: PASS for the stated theorem with odd layers
1 through $L-1$, arbitrary admitted final activation, and the explicit
centered-variance assumption (2).** Equations (1)–(9) of
NONODD_ENDPOINT_PROGRESS.md establish its actual trained endpoint bound
(3) with the original label cap. No substantive mathematical error or
missing hypothesis was found within this scope. This verdict does not
establish the endpoint claim when earlier layers are nonodd.

This was an isolated review of the five frozen inputs below. All five were
read completely; the audit targets the endpoint theorem, its odd-endpoint
estimates, Sections 1–4 of the innovation route, and the final-layer
examples. The scalar route, moment route, other studies, study history,
and previous reviews were not read. The remaining paper sections and
unused obstruction examples in the innovation note are outside the
verdict. The rigorous-math and canonical-notation skills, including the
neural-network reference, were applied. No necessary scientific input for
the audited theorem was missing.

## Frozen inputs

SHA-256 hashes for the original complete review:

| Input | SHA-256 |
| --- | --- |
| NONODD_ENDPOINT_PROGRESS.md | 4ad88dd4580ee8b53d914ecf1afe72bdbbc06ddd3dc06fb802c072295c348dce |
| NONODD_INNOVATION_ROUTE.md | 830ee71bdfe1faf99288dd8bab4416e2ba36e47a68344fd25fff685c4e195fc5 |
| ODD_DEPTH_ENDPOINT.md | e0babb343a9de9a1c16cfbcbb775a7ec7a3f8d4800dcbc216699c5b21c913677 |
| paper/compact.tex | 460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe |
| paper/compact_fitting.tex | 6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f |

The first three paths are relative to this study; the last two are relative
to the repository root. The reviewer modified no source; the author's
narrow corrections and their final hashes are checked below.

## Actual endpoint comparison

The inherited setup includes $\|x_a\|=\sqrt d$, uncentered population
training Gram $Q=Q^{(L)}\succ0$, zero initial readout, the stated Gaussian
initialization, and canonical mobilities. Write
\[
\lambda=\gamma/m\le1,\quad
B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n,\quad
u_t=w_t/\sqrt n,\quad
u_*=B_0(B_0^\top B_0)^{-1}y,\quad e=\|u_*\|.
\]
For the training span $S$, condition on
$\mathcal A_n=\sigma(W_0^{(1)}|_S,W_0^{(2)},\ldots,W_0^{(L)})$.
The first-layer velocity has right factors in $S$, so
$W^{(1)}(t)v=W_0^{(1)}v=Z$, where $Z\sim N(0,I_n)$ is independent
of $\mathcal A_n$. The training trajectory depends only on
$\mathcal A_n$. Applying the fitting proof in an orthonormal basis of
$S$ supplies the required fitting event without using $Z$.

The readout estimates do not use parity. On a finite interval put
$M=\sup_t\|u_t\|$ and $A=\int\rho\le2Y/\lambda$. Forward
differentiation gives
$\|B_t-B_0\|_{\mathrm{op}}/\sqrt m\le2FM\int_0^t\rho$, while
\[
\frac12\partial_t\|u_t-u_*\|^2
=-2\rho^2+\frac2m\langle(B_t-B_0)^\top u_*,r_t\rangle.
\]
Integration gives $\|u_t-u_*\|^2\le e^2+4FMeA^2$, hence
$M\le2e+4FeA^2\le3e$. This extends uniformly to infinite time.
Projection onto and perpendicular to the range of $B_0$ gives endpoint
error bounds $72Fe(Y/\lambda)^2$ and $24Fe(Y/\lambda)^2$,
respectively. Thus the stated $120Fe(Y/\lambda)^2$ bound is valid.
Here $e\le\sqrt2Y/\sqrt\lambda$, and the cap gives
$4FA^2\le16F(Y/\lambda)^2\le1$.

The Gaussian Poincare inequality used is
$\operatorname{Var}(g(Z))\le\mathbb E\|\nabla g(Z)\|^2$ for a
Lipschitz scalar function of standard Gaussian $Z$. The initialized
layer-$j$ query map is $K_j$-Lipschitz on the hidden-operator event.
For $j<L$ it is odd, so its mean is zero. Rowwise Poincare gives
\[
\mathbb E_Z\|E h_0^{(j)}\|^2\le K_j^2\|E\|_F^2
\]
for every $\mathcal A_n$-measurable matrix $E$, regardless of its
dependence on the initialized mixers. In layer-$j$ forward subtraction,
the changed mixer multiplies $h_0^{(j-1)}$. The estimate is therefore
only needed below the final layer. Combining it with the displacement
bounds and moving operator bound $9$ gives
\[
\|h_\infty^{(L)}-h_0^{(L)}\|_{L^2_Z}\le4MYT_L/\lambda.
\]

For $F_n=u_*^\top h_0^{(L)}/\sqrt n$ and
$R_n=f_n(\infty,\sqrt d\,v)-F_n$, the exact decomposition is
\[
R_n=\frac{(u_\infty-u_*)^\top h_0^{(L)}}{\sqrt n}
+\frac{u_\infty^\top(h_\infty^{(L)}-h_0^{(L)})}{\sqrt n}.
\]
Poincare bounds the centered first term without a mean-zero final
activation. Centering contracts the second term's $L^2_Z$ norm. Thus
\[
\|R_n-\mathbb E_ZR_n\|_2
\le\frac{120K_LFe(Y/\lambda)^2+4M^2YT_L/\lambda}{\sqrt n}
\le\frac{De(Y/\lambda)^2}{\sqrt n}.
\]
The last step uses $M\le3e$, $e\le\sqrt2Y/\sqrt\lambda$, and
$\lambda\le1$, giving $D=120K_LF+36\sqrt2T_L$.
The supplied coefficient bounds give $D\le\beta^{16L}$.
Consequently progress equations (4)–(6) concern the actual fully trained
endpoint and require no extra label restriction.

## Conditional anti-concentration and transfer

The innovation route's general positivity argument is valid. The query
copies have equal covariance columns with the training coordinates.
Their Gaussian preactivation difference is independent of their average
and of the training vector. Its variance is positive by nonconstancy of
every activation, which follows from $m\ge2$ and $Q\succ0$.
Analyticity makes the final activation derivative nonzero at almost every
Gaussian average. Since
$\mathbb E(H^\top Q^{-1}y)^2=y^\top Q^{-1}y>0$, conditioning
proves $V_{\rm pair}>0$, even for a singular preceding training
covariance. The explicit lower expression in innovation equation (5)
also has the correct factor.

The central limit argument first conditions on the lower layers and both
query copies, leaving independent top Gaussian rows. It does not initially
condition on all of $\mathcal A_n$. For preceding covariance $S$, let
$Q(S)$ be the resulting population training Gram and $d(S)$ the
difference of its query cross columns. The centered interpolation
influence is
\[
\Psi_S=
[\phi_L(U)-\phi_L(V)-d(S)^\top Q(S)^{-1}H]
H^\top Q(S)^{-1}y.
\]
Its mean is zero because
$\mathbb E[H(\phi_L(U)-\phi_L(V))]=d(S)$ and
$\mathbb E HH^\top=Q(S)$. Near the limiting covariance, the training
inverse is bounded, and Gaussian linear-growth estimates bound the third
moments uniformly. The inverse expansion has an
$O_{\mathbb P}(n^{-1})$ remainder, as a product of empirical errors of
order $n^{-1/2}$. Hence the centered paired predictor has the claimed
triangular normal limit of variance $V_{\rm pair}$.

No rate for convergence of the preceding covariance is needed: taking
the largest normal interval probability absorbs the uncontrolled
conditional population shift. The supplied deterministic-subsequence
argument justifies local uniformity. To obtain the stronger conditioning,
use conditional independence of the two queries:
\[
\Pr_Z(F_n\in[a-r,a+r]\mid\mathcal A_n)^2
\le\Pr_{Z,Z'}(|F_n(Z)-F_n(Z')|\le2r\mid\mathcal A_n).
\]
The averaged normal interval bound and Markov then give innovation
equation (9), including radius
$c_\delta=\delta^3\sqrt{2\pi V_{\rm pair}}/16$ and active probability
$1-\delta/2$. No top-row independence is asserted after conditioning
on $\mathcal A_n$. The artificial query copies do not require
$\dim S^\perp\ge2$.

In the endpoint theorem, oddness through layer $L-1$ sets all population
query cross covariances to zero. The final query Gaussian preactivations
are independent of each other and of the training preactivations. Define
\[
v_L=\operatorname{Var}[\phi_L(\sqrt{Q^{(L-1)}_{11}}G)],
\qquad e_0^2=y^\top Q^{-1}y.
\]
Then $V_{\rm pair}=2v_Le_0^2$, as in progress equation (7).
For $\delta=1/4$, the innovation theorem's radius is
$\sqrt\pi\sqrt{v_L}e_0/(512\sqrt n)$, exceeding
$r_n=\sqrt{v_L}e_0/(1024\sqrt n)$, at active probability $7/8$.

On the fitting event and $e\le\sqrt2e_0$, Chebyshev gives
\[
\Pr_Z(|R_n-\mathbb E_ZR_n|>r_n/2\mid\mathcal A_n)
\le8\cdot1024^2D^2(Y/\lambda)^4/v_L.
\]
The original cap and centered-variance assumption yield
\[
\frac{D(Y/\lambda)^2}{\sqrt{v_L}}
\le\beta^{16L-60L+20L}=\beta^{-24L}\le1/8192.
\]
The error probability is therefore at most $1/8$. Absorbing
$\mathbb E_ZR_n$ into the arbitrary center yields endpoint small-ball
probability at most $1/4+1/8=3/8$. Conditioning on an independent second
trained run gives separation and fitting probability at least
$35/64-o(1)>1/2$, at radius
$r_n/2=\sqrt{v_L}e_0/(2048\sqrt n)$. This checks both the constants
and the eventual individual-width assertion.

## Examples and qualifications

For each specified exact softplus, SiLU, and GELU function,
$\phi(x)-\phi(-x)=x$. Writing $\phi(x)=x/2+g(x)$ with even $g$,
Gaussian symmetry gives
\[
\operatorname{Var}[\phi(\sqrt qG)]
=q/4+\operatorname{Var}[g(\sqrt qG)]\ge q/4.
\]
The strip claims hold, including the paper's full-strip first derivative
requirement. For $|\operatorname{Im}z|<1$,
$\operatorname{Re}(1+e^z)>0$, defining the holomorphic softplus
logarithm. The logistic factors in SiLU derivatives are bounded, and
their nonconstant derivative factors decay exponentially as
$|\operatorname{Re}z|\to\infty$; multiplication by $z$ preserves
boundedness on this strip. GELU is entire; its displayed derivative
formulas and the vertical integral for $\Phi$ bound its derivatives on
every fixed horizontal strip. All three functions are nonaffine and
unbounded.

The odd-endpoint input explicitly checks the lower-layer second-moment
bound for tanh, arctan, sine, and $z+\tanh z$. The progress note also
originally called erf and arsinh “previously checked,” although those
checks are absent from the supplied odd-endpoint note. This was a minor
citation omission, corrected by the author as recorded below. Directly,
for $0\le t\le1$,
\[
\operatorname{erf}(t)
\ge\frac2{\sqrt\pi}(t-t^3/3)\ge t/2,\qquad
\operatorname{arsinh}(t)
=\int_0^t(1+u^2)^{-1/2}\,du\ge t/\sqrt2\ge t/2.
\]
Both are odd and increasing. Together with
$\mathbb E[G^2\mathbf1_{|G|\le1}]>1/8$, these inequalities give
$\mathbb E\phi(\sqrt qG)^2\ge\min(q,1)/32$.
Their derivatives are bounded on a fixed strip strictly within
$|\operatorname{Im}z|<1$ for arsinh, and on every fixed strip for erf.
Thus layerwise choices among the listed odd families give
$Q^{(L-1)}_{11}\ge32^{-(L-1)}$; all three final-layer examples satisfy
(2). Here “mixtures” means layerwise choices, as in the inherited
statement; arbitrary linear combinations need not retain this bound.

The centered-variance qualification must remain explicit. For example,
$\phi_\varepsilon(z)=1+\varepsilon(z+\tanh z)$ has Gaussian second
moment at least one but centered variance tending to zero with
$\varepsilon$. The theorem does not infer (2) from an uncentered
diagonal bound, cover nonodd earlier layers, or quantify a practically
useful sufficient width. These limitations are accurately stated.
This review authorizes no promotion or change to established material.

## Narrow correction recheck

The author subsequently added the explicit erf and arsinh inequalities
and the layerwise-choice meaning to the progress note. Both additions
agree with the independently reconstructed checks above and remove the
presentation omission. The innovation note's equation (19) now uses the
correct LaTeX opening-delimiter command after its negative thin-space
command. This is a rendering-only correction in an example
outside the endpoint theorem's dependency chain.

The changed passages were inspected directly. Their final SHA-256 hashes
are:

| Input | Final SHA-256 |
| --- | --- |
| NONODD_ENDPOINT_PROGRESS.md | d506e99347a30b4a53c368027004c7ebfecd93ca0a000ec5223538e23180c6d9 |
| NONODD_INNOVATION_ROUTE.md | 7405440fe7953e9660ad93ac193a47bb4cc1e92411d273c1c8c653b977387f48 |

The other three hashes are unchanged. The PASS verdict applies to these
final versions with the same scope and qualifications; no broad rerun was
necessary.

Final dependency clarification, checked 2026-10-11: Section 1 of
NONODD_INNOVATION_ROUTE.md now explicitly recalls $m,L\ge2$,
$\|x_a\|=\sqrt d$, and that data and activations are fixed before width
increases. These were already inherited from the canonical setup and used
in this review; the two added lines introduce no new assumption. Their
wording was inspected, and the latest innovation-note SHA-256 is
0121e871a3c4aa7356a33616948fe87b290b91d118a8eaf60d8737f9f4bb4853,
superseding its preceding final-hash entry. The progress theorem hash
remains d506e99347a30b4a53c368027004c7ebfecd93ca0a000ec5223538e23180c6d9.
The PASS verdict and its scope are unchanged.
