# Actual endpoint variability for the full nonaffine analytic class

2026-10-11. Continuation of the general nonlinear endpoint question.
This is the assembly note for a different proof, using a finite Gaussian
matrix-oracle transcript instead of comparison with a frozen-feature
predictor. The auxiliary numerical trajectory is a proof device: the
conclusion concerns the original, fully trained dense gradient flow.

Status: internally checked theorem. The numerical approximation, Gaussian
lemmas, and endpoint assembly have separate reconstruction reports listed
in Section 8. This is a study result, not a promoted book theorem. The
fitting and analytic-source proofs of the current compact paper remain
explicit inputs; those existing proofs have not been replaced by an
assumption about an unproved endpoint fluctuation.

## 1. Statement and unchanged qualifications

Use the canonical network, Gaussian initialization, squared loss and block
mobilities of `paper/compact.tex`. There are $L\ge2$ hidden layers,
width $n$, $m\ge2$ inputs of norm $\sqrt d$, zero initial readout, and
fixed nonzero labels. Each layer activation satisfies exactly the compact
paper's strip-analytic assumptions and is nonaffine, meaning it is not of
the form $z\mapsto az+b$ on the real axis; the layerwise activations may
differ. They are not centered, normalized or otherwise changed, and their
values need not be bounded. Write

\[
Y=\|y\|_2/\sqrt m>0,\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
0<Y\le(\gamma/m)\beta^{-30L},\quad \gamma/m\le1.
\]

Here $Q^{(L)}$ and $\beta$ have exactly their paper definitions. Retain
the proper-span geometry of the current endpoint result: the training
directions $x_a/\sqrt d$ span a proper subspace of $\mathbb R^d$.
Choose a fixed unit vector $v$ orthogonal to that subspace, before
initialization. All parameters, data, labels and activations are fixed
separately before $n$ tends to infinity.

**Theorem.** For every $0<\delta<1$, there are constants
$c>0$ and $N<\infty$, depending on this fixed problem and $\delta$ but
not on $n$, such that at each individual $n\ge N$,

\[
\Pr\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
       \ge \frac c{\sqrt n},\quad
 \text{both ordinary dense runs reach their fitted limits}
 \right\}\ge1-\delta.                                      \tag{1}
\]

The two runs have independent initializations and the same training data.
This implies the corresponding supremum bound on any separated query
region containing this orthogonal query. Relative to the paper's activation
class, its only added activation condition is nonaffinity at every layer.
It does not impose oddness, centering, bounded activation values, another
label cap, or width-dependent labels.
It does not extend the geometry to full-span training data, quantify a
polynomial width threshold, or assert a positive bound at every training
time.

## 2. Exact Gaussian conditioning under adaptive matrix queries

All notation in this section is local. Let $G_1,\ldots,G_k$ be independent
$n\times n$ matrices with independent $N(0,1/n)$ entries, independent
of an initial sigma field. A finite deterministic algorithm can request
$G_j z$ or $G_j^\top z$, choosing the matrix, orientation and vector
from the initial sigma field and all preceding answers. It has no other
access to the entries of these matrices. Its complete transcript includes
the vectors, answers and every deterministic calculation from them.

For each matrix let $V_j$ be the span of the forward query vectors and
$U_j$ the span of the transpose query vectors. Let $P_{V_j},P_{U_j}$
be the orthogonal projectors. Conditional on the transcript, jointly,

\[
G_j=M_j+(I-P_{U_j})G'_j(I-P_{V_j}),                             \tag{2}
\]

where the $G'_j$ are mutually independent fresh matrices with the same
Gaussian entry law, independent of the transcript. The known conditional
mean is

\[
M_j=G_jP_{V_j}+P_{U_j}G_j(I-P_{V_j}).                           \tag{3}
\]

Both terms are known from the answers: forward answers determine $G_j$
on $V_j$, and transpose answers determine $P_{U_j}G_j$. Rank-deficient
query lists cause no difficulty; use their spans or their Moore--Penrose
inverses. Each projector has rank at most the number of corresponding
queries. In particular

\[
\|M_j\|_{\rm op}\le2\|G_j\|_{\rm op}.                       \tag{4}
\]

**Proof.** For a fixed list of linear observations, the Gaussian matrix
viewed in Frobenius Euclidean space splits into its observed orthogonal
projection and an independent Gaussian in the nullspace of the
observations. The nullspace here consists of the matrices $A$ satisfying
$AP_{V_j}=0$ and $P_{U_j}A=0$, hence exactly
$(I-P_{U_j})A(I-P_{V_j})$. The complement projection is (3).

For adaptive observations, proceed inductively through the algorithm.
Conditional on the preceding transcript, the next vector and its matrix
index are fixed. Conditioning the remaining Gaussian on that one linear
answer projects its still-unrevealed part onto the new nullspace. The
previous nullspace intersected with the new constraints is precisely the
space obtained by adding the new vector to $U_j$ or $V_j$. The other
matrices retain their independent conditional Gaussian laws. Thus the
fixed-list formula holds after every step, including the final adaptive
step. This also proves conditional independence across matrices. Padding
with zero queries handles a transcript-measurable early stopping rule
with a deterministic upper bound on its length. The projection argument
uses only the elementary characteristic function of a Gaussian vector,
and remains valid for singular observation covariances. This proves (2).

Importantly, the theorem does not condition on unobserved weight norms,
the successful numerical approximation event, or the actual full training
trajectory. Such conditioning would generally invalidate (2).

## 3. How the training transcript is formed

Section 6 of [GELU_SILU_FLOW_ROUTE.md](GELU_SILU_FLOW_ROUTE.md) constructs a deterministic
high-order integration of the original training equations to
$T=32(m/\gamma)\log(en)$. It uses a number of initialized hidden-matrix
forward and transpose actions bounded by a fixed power of $\log(en)$,
with all problem parameters fixed. It returns weights whose physical
parameter distance from the actual fitted endpoint is $O(n^{-16})$ on
an event whose probability tends to one. The constants here may depend
on the fixed problem. This is the one input to (2) requiring a numerical
approximation proof; it must not be replaced by an assertion that the
exact infinite training path has finite rank.

The first matrix is queried only on the training span. For each hidden
matrix, every learned increment is a finite sum of outer products of
computed forward and backward Taylor coefficients. These increments are
known from the transcript; multiplication by them needs no new access to
the initialized matrix. Coordinatewise activations and their derivatives,
Taylor-series arithmetic, scalar products and residual calculations also
need no such access. Only actions of the initialized matrices are charged
as queries. No final weight entry is inspected to choose a query vector.

Let $\widehat W^{(j)},\widehat w$ denote the returned weights and readout.
For $j\ge2$, (2) gives, conditional on the entire training transcript,

\[
\widehat W^{(j)}=A_j+(I-P_{U_j})G'_j(I-P_{V_j}),                \tag{5}
\]

where $A_j=M_j+\widehat W^{(j)}-W_0^{(j)}$ is known. All projector
ranks are $o(n)$. The unused first-layer column

\[
Z=W_0^{(1)}v\sim N(0,I_n)
\]

is independent of the transcript and the residual matrices in (5).
It remains exactly unchanged, because first-layer increments have all
their input directions in the training span.

## 4. Measurable good transcripts

There are fixed positive constants bounding, with probability tending to
one, the following quantities of the returned weights:

\[
0<a_0\le\|\widehat w\|^2/n\le a_1<\infty,\qquad
\frac1n\sum_i\widehat w_i^4\le a_4<\infty,\qquad
\max_{2\le j\le L}\|A_j\|_{\rm op}\le40.                    \tag{6}
\]

The constants in this section are local, fixed-problem constants, not
new assumptions. Every event in (6) is measurable from the transcript.

To justify the readout lower bound, the fitting theorem gives final
training feature RMS at most $2H$, where
$H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}$. Exact interpolation implies

\[
Y\le2H\|w_\infty\|/\sqrt n.
\]

The approximation error therefore allows $a_0=(Y/(4H))^2$ eventually.
The fitting readout upper bound and that same approximation allow
$a_1=(2Y\sqrt{m/\gamma}+1)^2$. The exact source moment extraction in
[NONODD_MOMENT_ROUTE.md, Sections 1--2](NONODD_MOMENT_ROUTE.md) gives

\[
\frac1n\sum_i\sup_{t\in[0,\infty]}|w_i(t)|^4
       \le\beta^{114L}(Ym/\gamma)^4                           \tag{6a}
\]

on an event of probability tending to one. It follows by keeping the
top carrier $k^{(L)}=w$ in the source proof's empirical exponential
budget, using $x^4\le(4/e)^4e^x$, and adding the fitting tail. No
independence of trained coordinates is asserted. The numerical physical
parameter error changes the normalized fourth norm by at most
$n^{1/4}O(n^{-16})=o(1)$. Thus one can take
$a_4=16\beta^{114L}(Ym/\gamma)^4+1$ eventually. This step uses an
averaged fourth-moment estimate, not a coordinate maximum growing with
$\log n$.

For the known matrix part, on the original initialization and fitting
events, $\|W_0^{(j)}\|\le8$, $\|W_\infty^{(j)}\|\le9$.
Consequently the approximate learned increment has operator norm at most
$18$ eventually; (4) gives $\|A_j\|\le16+18<40$. This proves that
the transcript-measurable event in (6) has probability tending to one.
The original initialization and fitting events are used only to establish
this probability. They are not added to the conditioning in (5).

## 5. Query innovation through every layer

For clarity, here are the only activation facts used below. Put

\[
 c_j=|\phi_j(0)|,\qquad
 s_j=\sup_{x\in\mathbb R}|\phi_j'(x)|,\qquad
 t_j=\sup_{x\in\mathbb R}|\phi_j''(x)|.
\]

They are finite under the paper's assumptions, and
$|\phi_j(z)|\le c_j+s_j|z|$ on the real axis. Nonaffinity implies
nonconstancy. Hence every compact minimum of
$\operatorname{Var}(\phi_j(a+\sigma G))$ with $\sigma$ bounded away
from zero is positive. For the final layer it also implies

\[
 \operatorname{Var}(\phi_L(a+\sigma G))
 -\bigl(\mathbb E[G\phi_L(a+\sigma G)]\bigr)^2>0,             \tag{7a}
\]

uniformly on compact $(a,\sigma)$-sets with $\sigma>0$. Equality in the
first statement would make the activation constant on the support of a
Gaussian; equality in (7a) would make it affine there. Continuity and full
Gaussian support then contradict nonconstancy or nonaffinity, respectively.
Compactness makes both lower bounds uniform. No named-family identity is
used.

Conditional on a good transcript, evaluate the returned network at the
orthogonal input, starting from $\widehat h^{(1)}=\phi_1(Z)$.
After exposing the preceding query layers, the next preactivation has
exact conditional law

\[
\widehat z^{(j)}=A_j\widehat h^{(j-1)}
 +\frac{\|(I-P_{V_j})\widehat h^{(j-1)}\|}{\sqrt n}
       (I-P_{U_j})g_j,\qquad g_j\sim N(0,I_n).                 \tag{7}
\]

The Gaussian vector $g_j$ is fresh at this step. Earlier query layers
use only $Z,G'_2,\ldots,G'_{j-1}$, which are conditionally independent
of $G'_j$; this proves (7), rather than assuming fresh randomness after
training.

The lemma in [GELU_SILU_PROJECTED_INNOVATION.md](GELU_SILU_PROJECTED_INNOVATION.md)
applies to (7). In detail, a coordinatewise
nonconstant Lipschitz function of a projected Gaussian with mean RMS
bounded and variance bounded above and away from zero has covariance
trace at least a fixed multiple of $n$, while its covariance operator
norm is bounded. Removing another subspace of dimension $o(n)$ loses
only $o(n)$ trace. Gaussian Poincare applied to the projected feature
norm then shows that its norm remains at least a fixed multiple of
$\sqrt n$, with probability $1-O(1/n)$.

Apply this first to $\phi_1(Z)$ and $V_2$, and then successively to
(7) and $V_{j+1}$. Upper norms are controlled simultaneously from linear
growth and $\|g_j\|/\sqrt n\le2$ except with probability $O(1/n)$.
Starting from $H_1=c_1+2s_1$, a permissible upper recursion is
$H_j=c_j+42s_jH_{j-1}$. The mean in (7) then has RMS at most
$40H_{j-1}$. Since $L$ is fixed, the final preactivation in (7) has,
with conditional probability $1-o(1)$ over the lower query layers, mean
RMS bounded by a fixed constant and a noise coefficient in a fixed compact
interval contained in $(0,\infty)$.

## 6. Final nonlinear readout and passage to the true endpoint

Condition further on successful lower query layers, through $L-1$ only;
do not condition on any norm or success event involving the fresh final
Gaussian. The final prediction has exactly the form in
[GELU_SILU_PROJECTED_SCALAR.md](GELU_SILU_PROJECTED_SCALAR.md),

\[
\widehat f_n(\sqrt d\,v)
   =\frac1n\sum_i\widehat w_i
     \phi_L\big(b_i+\sigma[(I-P_{U_L})g]_i\big).               \tag{8}
\]

Here the mean RMS, $\sigma$ and the readout satisfy the fixed bounds
already established. That lemma proves two conclusions uniformly over
these conditioned quantities: variance at least $c_0/n$ for a fixed
$c_0>0$, and Gaussian approximation for the centered prediction, after
multiplication by $\sqrt n$, with error tending to zero.

The variance argument uses Hermite degrees at least two. Outside an
$o(n)$ set of high-leverage coordinates, the off-diagonal squared
Gaussian correlations have uniformly vanishing row sums. The higher
Hermite Gram matrices are consequently diagonally dominant. Nonaffinity
supplies a positive Hermite-tail variance on bounded means and noise
scales. The empirical readout fourth moment prevents the readout from
concentrating on the omitted coordinates or on the large-mean coordinates.
This supplies a scalar lower bound even though a uniform lower bound on
the entire feature covariance matrix is false.

The normal approximation uses bounded first and second derivatives.
For the $\sqrt n$-scaled scalar in (8), the gradient norm is bounded
and the Hessian operator norm is $O(n^{-1/4})$, since
$\max_i|\widehat w_i|\le(na_4)^{1/4}$. The Gaussian
integration-by-parts/Stein estimate in that lemma gives a uniform
small-ball bound. Hence, for every fixed $\delta>0$, one can choose
$c_\delta>0$, independent of $n$, so that

\[
\sup_{a\in\mathbb R}
\Pr\left\{|\widehat f_n(\sqrt d\,v)-a|
                  \le c_\delta/\sqrt n\right\}
        \le\delta/2+o(1).                                    \tag{9}
\]

The excluded transcript and lower-query events contribute only $o(1)$.
The small-ball estimate is uniform in the center, including centers
depending on an independent second network.

Finally, the physical parameter approximation and the fitting tube give
$|\widehat f_n(\sqrt d\,v)-f_n(\infty,\sqrt d\,v)|
=O(n^{-16})$ outside an event of probability $o(1)$. This deterministic
subtraction bound follows by propagating the hidden operator differences
and the normalized readout difference; the first-layer column is unchanged.
One may restrict $\|Z\|/\sqrt n\le2$, with another $o(1)$ loss.
Thus (9) applies to the true endpoint with half the radius eventually.
For a completely explicit failure allocation, define an endpoint prediction
to be zero on the event that its fitted limit does not exist. This extension
is used only in the proof. Let $v_0>0$ be the uniform variance lower bound
for $\sqrt n\,\widehat f_n$ supplied by the scalar lemma with the
constants above. Averaging its bound over transcripts and lower layers,
then over the independent second extended endpoint, gives

\[
\Pr\{\text{both fit and }|f_n(\infty,\sqrt d\,v)
 -\widetilde f_n(\infty,\sqrt d\,v)|\ge c/\sqrt n\}
 \ge1-\frac{4c}{\sqrt{2\pi v_0}}-o(1).                        \tag{10}
\]

Here the factor four uses the approximate small-ball radius $2c/\sqrt n$
and charges the first-run approximation failure and the second-run fitting
failure separately. Choosing $c=\delta\sqrt{2\pi v_0}/16$ makes the
fixed failure term $\delta/4$; the remaining terms are eventually below
$3\delta/4$. This proves (1) at every sufficiently large individual
width. Only the first run needs an auxiliary approximant.

## 7. What is and is not being claimed about the proof device

The proof does not freeze any hidden layer in the actual network. It does
not replace training by a random-feature model. It does not assume that
conditioning on the entire trained weights preserves Gaussianity.
Instead it first approximates the true trajectory accurately enough,
conditions on the limited matrix observations of that particular
approximation, proves a lower bound for it, and transfers the lower bound
back by an error that is smaller than $n^{-1/2}$.

Nor is the auxiliary integration advertised as a new compression method
or an empirical procedure. Its role is to show that the training dynamics
can be approximated without revealing all Gaussian directions. The
existing label assumption is used for fitting, source bounds, and that
approximation. No comparison between a perturbation error and a possibly
tiny frozen-feature variance is required.

## 8. Proof inputs and checks

The model, activation class and sufficient label cap are those of
`paper/compact.tex`, with the sole additional activation condition that
every layer activation be nonaffine.
The fitted endpoint and tail estimates are proved in
`paper/compact_fitting.tex`. The complex-time source bounds, complex
carrier maximum, strip margin and empirical exponential budget are proved
in `paper/compact_foundations.tex`; the internal bounds are explicitly
identified in the numerical and moment modules above. That class permits
unbounded activation values. The new endpoint argument uses no special
identity of GELU, SiLU, odd functions, or any other named family.

The following internal checks have distinct scopes:

- [ORACLE_INTEGRATOR_CHECK.md](ORACLE_INTEGRATOR_CHECK.md): the finite
  oracle algorithm, physical normalization, complex continuation at
  numerical starts, accumulated error, fitting tail and information access.
- [PROJECTED_GAUSSIAN_CHECK.md](PROJECTED_GAUSSIAN_CHECK.md): weighted
  covariance, uniform small-ball estimate, projected innovation and their
  exact quantifiers. Its statement corrections are incorporated.
- [GAUSSIAN_ORACLE_ASSEMBLY_CHECK.md](GAUSSIAN_ORACLE_ASSEMBLY_CHECK.md):
  joint deferred decisions, measurable good transcripts, source moment
  extraction, layerwise interfaces and actual-endpoint transfer.

These reports record source hashes and limits of their verdicts. In
particular they do not claim a new audit of every line of the existing
source-cavity theorem. The proof dependencies are the stated, proved
current-paper fitting/source results, not the incomplete centered
comparison in Sections 1--5 of `GELU_SILU_FLOW_ROUTE.md` or the
mean-adapted comparator route. No paper or book file was modified.

The activation-generic replacements in Sections 1, 5 and 6, together with
the corresponding generic constants in the two projected-Gaussian modules,
are reconstructed separately in
`GENERAL_ACTIVATION_ENDPOINT_CHECK.md`. The older reports continue to
check the unchanged oracle, conditioning, source-moment and endpoint-transfer
parts of the proof; their former GELU/SiLU constants are not reused.
