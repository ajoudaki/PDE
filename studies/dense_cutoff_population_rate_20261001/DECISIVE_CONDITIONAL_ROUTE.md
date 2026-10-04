# A local edge-response criterion for the finite-width mean

This is a scoped internal theoretical derivation, 2026-10-01. No experiment,
manuscript edit, Git write, or other-study input was used. The question is
whether a finite response estimate can control the missing population bias,
without assuming the population comparison itself.

**Result.** A matched interpolation of Gaussian edge variances and edge
mobilities gives an exact width-doubling identity. One signed, local,
second-response estimate implies a strict root-width bound for the finite-width
mean under every fixed deterministic residual control. It does not by itself
prove finite fluctuations or the all-time comparison for adaptive residuals.
The response estimate is open. In particular, this note does **not** claim to
have found a verified single weak hypothesis giving the entire requested
theorem. It isolates the bias bridge without concealing it inside concentration.

## 1. Controlled canonical model and the interpolation

Fix the depth, training inputs, and an absolutely continuous deterministic
path \(b:[0,S]\to\mathbb R^m\), with \(b(0)=0\) and
\(\sum_a|b'_a(u)|\le1\) almost everywhere. In the actual dense flow,
\(db_a=-2r_a\,dt/m\); prescribed \(b\) replaces this residual feedback only
inside the proof comparison. The activity interval length \(S\) is independent
of width. Small labels and the Gram gap give the relevant bounded activity for
the actual and population flows.

The argument below is stated for bounded \(C^3\) activations with bounded
derivatives through order three; tanh satisfies this additional regularity.
Extension to the manuscript's full \(C^{1,1}\), possibly unbounded, class is
not asserted. Put \(v_a=x_a/\sqrt d\). At width \(N=2n\), divide every hidden
layer into two blocks of size \(n\). For \(0\le s\le1/2\), define the
deterministic edge profile, separately in each hidden matrix, by

\[
c_{ij}^{(\ell)}(s)=
\begin{cases}
2(1-s),&i,j\text{ belong to the same block},\\
2s,&i,j\text{ belong to different blocks}.
\end{cases}
\tag{1}
\]

Every row and column sum is \(N\). Initialize independent first-layer entries
as \(N(0,1)\), the readout at zero, and all hidden entries independently as

\[
W_{0,ij}^{(\ell)}\sim N(0,c_{ij}^{(\ell)}/N),\qquad 2\le\ell\le L.
\tag{2}
\]

Use the usual dense forward pass
\(z^{(1)}=W^{(1)}x/\sqrt d\),
\(z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\),
\(h^{(\ell)}=\phi_\ell(z^{(\ell)})\), and
\(f_N=w^\top h^{(L)}/N\).
The residual-free backward fields are
\(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\) and
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}\).
The controlled updates are

\[
\begin{aligned}
dW^{(1)}&=\sum_a\delta_a^{(1)}v_a^\top\,db_a,\\
dW_{ij}^{(\ell)}
 &=\frac{c_{ij}^{(\ell)}}N
   \sum_a\delta_{a,i}^{(\ell)}h_{a,j}^{(\ell-1)}\,db_a,
   &&2\le\ell\le L,\\
dw&=\sum_a h_a^{(L)}\,db_a.
\end{aligned}
\tag{3}
\]

Thus the edge mobility and its initialization variance carry the same factor.
This auxiliary profile is not a proposed replacement algorithm.

At \(s=0\), off-block entries are initialized at zero and have zero mobility;
they stay zero. Each diagonal block is exactly a canonical width-\(n\)
network driven by \(b\): its hidden variance is \(2/N=1/n\), and its hidden
update coefficient is also \(2/N=1/n\). Its first-layer and readout equations
are the canonical ones. The two blocks are independent because \(b\) is
deterministic. Hence, pathwise,

\[
f_{2n,0}^{b}(u,x)
 =\tfrac12\bigl(f_n^{b,1}(u,x)+f_n^{b,2}(u,x)\bigr).
\tag{4}
\]

At \(s=1/2\), all entries have variance \(1/N\), all mobilities are one, and
(3) is the canonical width-\(2n\) controlled network. In particular,

\[
\mathbb E f_{2n,0}^{b}=\mathbb E f_n^{b},\qquad
\mathbb E f_{2n,1/2}^{b}=\mathbb E f_{2n}^{b}.
\tag{5}
\]

Bounded activations give a deterministic width-independent bound on the
readout and prediction over \([0,S]\). The controlled ODE exists on every
fixed such interval: the top matrix has bounded velocity, and descending
through layers bounds successive matrix velocities in terms of already
bounded higher matrices. Constants may depend on an initialized finite
matrix's norm; the response hypothesis below supplies the required
expectation regularity.

## 2. The exact local response that differentiates the mean

For a deterministic profile \(c\), write \(Z=(W_0^{(2)},\ldots,W_0^{(L)})\)
for the initialized hidden entries, before averaging over them. Let

\[
q_N^b(u,x;c,Z,W_0^{(1)})=\frac{d}{du}f_N^b(u,x)
\tag{6}
\]

at almost every activity time. This quantity is constructed by solving (3)
and differentiating the dense forward output. It includes the dependence of
the full trained state on \(c,Z,W_0^{(1)}\). The derivative
\(\partial_{c_{ij}^{(\ell)}}q_N^b\) below keeps \(Z\) fixed: it is the
response to changing that edge's mobility in the entire past controlled
evolution, including any explicit mobility in (6). The derivative
\(\partial_{Z_{ij}^{(\ell)}}^2q_N^b\) keeps \(c\) fixed: it is the second
response to that one initialized hidden edge.

For a tagged edge \(e=(\ell,i,j)\), define its normalized expected response

\[
\mathcal R_{N,e}^b(u,x;s)
 =N^2\mathbb E\left[
 \partial_{c_e}q_N^b+\frac1{2N}\partial_{Z_e}^2q_N^b
 \right]_{c=c(s)}.
\tag{7}
\]

The expectation includes all initialization. The combination in (7),
including its plus sign, is essential. It accounts for both the mobility
change and the covariance change; keeping only either term changes the
problem.

Gaussian covariance differentiation gives

\[
\frac d{ds}\mathbb E q_N^b
 =\sum_e c'_e(s)\,
   \mathbb E\left[\partial_{c_e}q_N^b+\frac1{2N}\partial_{Z_e}^2q_N^b\right].
\tag{8}
\]

To verify the covariance term for one entry, write
\(Z_e=\sqrt{c_e/N}\,G_e\), differentiate, and use
\(\mathbb E[G_e A(G_e)]=\mathbb E[A'(G_e)]\). The factor is
\(1/(2N)\). Independence permits summing over entries. The response
hypothesis requires the integrability needed for differentiation; mere
finite-dimensional smoothness is not a replacement for that condition.
The open interval \(0<s<1/2\) suffices, with endpoint passage by integrable
domination.

Within-block permutations and simultaneous interchange of the two blocks
in every layer preserve the joint law. Thus at each layer the expectation
(7) has only two values, denoted
\(\mathcal R_{N,\mathrm{in}}^{(\ell),b}\) and
\(\mathcal R_{N,\mathrm{out}}^{(\ell),b}\).
There are \(N^2/2\) edges of each type; their derivatives \(c'_e\) are
respectively \(-2,+2\). Equation (8) becomes the exact identity

\[
\frac d{ds}\mathbb E q_N^b(u,x;s)
 =\sum_{\ell=2}^L
 \left(\mathcal R_{N,\mathrm{out}}^{(\ell),b}(u,x;s)
      -\mathcal R_{N,\mathrm{in}}^{(\ell),b}(u,x;s)\right).
\tag{9}
\]

There is no population field, query-Gram inverse, time mesh, clipping cap,
or assumption of independent trained neurons in (7)--(9).

## 3. One local hypothesis and its bias theorem

**Local response contrast hypothesis.** There is a nonnegative

\[
k\in L^2(\mu),\qquad k(x_a)<\infty\quad(1\le a\le m),
\]

and a constant \(C\), independent of even width \(N\), activity time,
and profile parameter, such that
the responses in (7) have the integrability required by (8), and

\[
\left|
\mathcal R_{N,\mathrm{out}}^{(\ell),b}(u,x;s)
-\mathcal R_{N,\mathrm{in}}^{(\ell),b}(u,x;s)
\right|
\le\frac{C k(x)}{\sqrt N}
\tag{H}
\]

for every hidden layer, almost every \(u,s\), and \(\mu\)-almost every test
input, as well as the training inputs. Only the selected fixed deterministic
driver \(b\) is required; a uniform estimate over all admissible drivers is
an optional stronger assertion. In the proposed actual-flow comparison,
the selected driver is the deterministic population residual driver, fixed
before sampling finite initialization. For the original finite-second-input-
moment contract, it would suffice to prove this with
\(k(x)\le C(1+\|x\|_2/\sqrt d)\). That envelope is part of what is missing;
it must not be replaced silently by a fourth-input-moment assumption.

The raw, unnormalized contrast in (7) is \(O(N^{-5/2})\). Each expected
edge response is expected on dimensional grounds to be \(O(N^{-2})\);
(H) asks for an additional root-width cancellation between two tagged edge
types. This scaling observation is motivation, not a proof of (H).

**Conditional mean theorem.** Suppose (H), and suppose the controlled
canonical networks have the qualitative finite-width population limit

\[
f_n^b(u,x)\longrightarrow f_\infty^b(u,x)
\quad\text{in probability at each fixed }u,x.
\tag{10}
\]

No rate is imposed in (10). Then

\[
\left(\int\sup_{0\le u\le S}
 |\mathbb E f_n^b(u,x)-f_\infty^b(u,x)|^2\,d\mu(x)\right)^{1/2}
 \le\frac{C_L S\|k\|_{L^2(\mu)}}{\sqrt n}.
\tag{11}
\]

Here (10) is the qualitative identification supplied by a controlled version
of the finite-program limit, not a rate consequence of (H). In the bounded
two-layer setting its passage from finite programs to the prescribed-control
flow uses the same deterministic-control stability as the existing cavity
note. For arbitrary depth, this controlled qualitative extension must be
checked rather than attributed to a theorem stated only for actual residual
feedback. Alternatively (11) identifies the rate to the width limit defined
by the following Cauchy argument, and population identification remains a
separate qualitative step.

**Proof.** Integrate (9) over \(s\in[0,1/2]\), use (5), and then integrate
in \(u\). The readout, hence the prediction, is zero at \(u=0\). Consequently

\[
\sup_{u\le S}
 |\mathbb E f_{2n}^b(u,x)-\mathbb E f_n^b(u,x)|
 \le\frac{C(L-1)S k(x)}{2\sqrt{2n}}.
\tag{12}
\]

For widths \(n,2n,4n,\ldots\), these bounds are summable, since
\(\sum_{j\ge0}2^{-j/2}=(1-2^{-1/2})^{-1}\). Thus the finite-width means
have a uniform-in-\(u\) limit, with error at most
\(C_L S k(x)/\sqrt n\). The deterministic bound on predictions gives
uniform integrability, so (10) identifies the limit with
\(f_\infty^b(u,x)\) at each rational activity time. Continuity extends the
identification to all activity times. The same summable bound in the stated
whole-input norm proves (11). No interchange of a probabilistic limit with
an unbounded time supremum is used. ∎

If the left side of (H) were instead \(Ck(x)/N\), the identical argument
would give \(O(1/n)\) mean bias. Thus the root-width hypothesis allows more
than the usual first weak finite-size correction.

## 4. The local hypothesis holds at initialization, with a stronger rate

Here take two hidden layers and tanh activations; in fact bounded activations
with four bounded top-activation derivatives suffice for this calculation.
Fix any instantaneous driver direction
\(\beta\in\mathbb R^m\), \(\sum_a|\beta_a|\le1\). This avoids demanding an
initial derivative of an arbitrary absolutely continuous driver. Since the
readout is zero, the directional activity velocity at initialization is

\[
q_{N,\beta}(0,x)
 =\sum_a\beta_a\frac1N\sum_i
   \phi_2(z_{a,i}^{(2)}(0))\phi_2(z_{x,i}^{(2)}(0)).
\tag{13}
\]

There is no explicit mobility dependence when initialized weights are held
fixed. Thus the first term in (7) is zero for this observable at initialization.

For one training sample \(a\) and the query \(x\), put

\[
H_j=(h_{a,j}^{(1)}(0),h_{x,j}^{(1)}(0))^\top,\quad
F(z_1,z_2)=\phi_2(z_1)\phi_2(z_2),\quad
Q_i=\frac1N\sum_j c_{ij}H_jH_j^\top.
\tag{14}
\]

The vectors \(H_j\in\mathbb R^2\) are iid and bounded, for every fixed
input pair, without any nondegeneracy assumption on that pair. Conditional
on all first-layer features, \((z_{a,i}^{(2)},z_{x,i}^{(2)})\) is Gaussian
with covariance \(Q_i\). Define the \(2\times2\) matrix

\[
A(Q)=\mathbb E_{Z\sim N(0,Q)}D^2F(Z).
\tag{15}
\]

Twice differentiating (13) in the tagged initialized edge gives its
contribution to (7) as

\[
\mathcal R_{N,(i,j)}^{a,x}(0;s)
 =\tfrac12\mathbb E[H_j^\top A(Q_i)H_j].
\tag{16}
\]

Gaussian covariance differentiation, now applied to \(D^2F\), shows
\(\|A(Q)-A(\widetilde Q)\|\le C\|Q-\widetilde Q\|\) because all fourth
derivatives of \(F\) are bounded. The formula remains valid at singular
covariances by continuous interpolation and requires no inverse.

Choose \(j\) in the row's block and \(k\) in the other block. Exchange the
iid feature vectors \(H_j,H_k\) in the expectation defining the response
for edge \((i,k)\). The tagged vector in (16) then becomes \(H_j\), while
the conditional covariance becomes

\[
\widetilde Q_i-Q_i
 =\frac{2(1-2s)}N
   (H_kH_k^\top-H_jH_j^\top).
\tag{17}
\]

Its norm is at most \(C/N\) deterministically. Combining (15)--(17), then
summing with weights \(\beta_a\), proves

\[
|\mathcal R_{N,\mathrm{out}}^{\beta}(0,x;s)
 -\mathcal R_{N,\mathrm{in}}^{\beta}(0,x;s)|\le C/N,
\tag{18}
\]

uniformly in \(s\), \(N\), and \(x\). The constant uses activation bounds,
not the query norm, because all first-layer features are bounded. In raw
single-edge units the contrast is \(O(N^{-3})\). This is stronger than (H)
at initialization, and the argument explicitly includes the mean. It does
not propagate the bound through training: once the first-layer fields
depend on the reused matrix, their exchange no longer changes only the
single covariance term in (17).

## 5. What this adds, and the limits of the reduction

This criterion supplies a genuine route for **bias**, rather than identifying
the finite mean with the population by declaration. It is local in the edge
being perturbed and uses only finite systems. It bounds a difference of
signed expected responses; it does not bound every response norm, every
Gaussian derivative, every carrier maximum, or the entire empirical kernel.
The population response produced by repeated forward/adjoint reuse is
retained automatically in both terms of (7).

Nevertheless, (9) also shows exactly how much work is still inside (H): it
is a derivative-level assertion that the auxiliary variance profile affects
the finite mean only weakly. Neither exchangeability nor a uniform bound
\(|\mathcal R_{N,e}|\le C\) yields its extra \(N^{-1/2}\). Calling (H) a
proved local curvature lemma, or claiming it is automatically substantially
weaker than every form of population consistency, would overstate this
derivation. A cavity proof would have to show that an edge's block type has
only root-width influence on its normalized expected response. No such proof
was completed here.

For the structured two-layer, orthonormal-input setting, the existing note
`POPULATION_CAVITY_ATTEMPT.md` already bounds prescribed-control training
prediction fluctuations about their finite means by \(CS^2/n\). Combining
that established result with (H) and qualitative identification gives a
strict root-width theorem for those prescribed-control training predictions.
For a test law supported on the training inputs, summing the finitely many
estimates is sufficient. For an arbitrary whole-input test law, the
corresponding fluctuation estimate must also be supplied. A bound proved for
each deterministic driver cannot be evaluated at the random actual driver.
Comparison against the deterministic population residual driver additionally
needs the damped all-time feedback stability developed in a separate route.

Thus one cannot honestly package all currently missing steps into (H) and
announce the full requested theorem. The useful new conclusion is a precise
population-free bias target that can accompany a first-response fluctuation
and stability theorem.

## 6. Hostile checks

**A slowly vanishing deterministic bias is excluded if (H) holds.** Suppose
at some fixed \((u,x)\) that the means have an additional component
\(a(u,x)n^{-1/4}\), with \(a(u,x)\ne0\), and no cancellation of that component
in the width difference. Their dyadic difference then has magnitude
\((1-2^{-1/4})|a(u,x)|n^{-1/4}\), contradicting (12). Concentration about
the finite mean alone would not detect this problem. Conversely, a generic
sequence with zero Gaussian derivatives and an externally added
width-dependent deterministic constant is **not** an instance of the
interpolation theorem: its block and dense endpoints would fail the exact
same-flow identity (5). Exact endpoint consistency is indispensable.

**The two auxiliary modifications must match.** Interpolating only variances
would produce two blocks at \(s=0\) whose hidden updates have coefficient

\(1/(2n)\), half the canonical \(1/n\). The endpoint would then not be the
desired width-\(n\) network. Interpolating only mobilities would likewise
give the wrong initialized block law. Equations (2)--(3) repair both defects.

**Direct interpolation from duplicated neurons is unsuitable.** Duplicating
each neuron and putting one half of the original hidden entry in each of its
four copies gives an exact width-doubling embedding of the dense dynamics.
But a linear covariance interpolation from that law to iid width-\(2n\)
initialization generally changes intermediate layer variances at order one:
the hidden covariance and the paired feature correlation both vary. Endpoint
agreement alone therefore does not make a small Gaussian-Hessian trace along
that path a realistic assumption. The block variance profile keeps row and
column variance sums fixed instead; proving its response contrast is still
necessary.

**No hidden time-grid limit.** The observable in (7) is the activity derivative
of the continuous controlled flow. The estimates are integrated over its
bounded activity interval. A finite-program version whose constants grow
with the number of instructions would not establish (H).

**No implicit clipping or architecture change in the conclusion.** All
endpoint networks are the original, unclipped dense networks with their
canonical normalizations. Intermediate profiled systems are used only in
the proof. Regularity has explicitly been strengthened to bounded \(C^3\)
activations for this candidate route.

## Inputs and status

Required canonical-notation and investigate-conjectures skills were read,
including neural-network conventions and research-contract/adversarial-audit
references. Assigned scientific inputs were this study's README, RESULT,
WIDTH_ROUTE, POPULATION_CAVITY_ATTEMPT, WEIGHTED_MOMENT_STATUS, and
LOSS_MATCHED_VARIATIONS, the dense setting in `paper/main.tex` (175--232),
the activation and population/fitting portions of `paper/proof_alltime.tex`,
and `docs/notation.qmd`. No links into other studies were followed.

Core source SHA-256:

```text
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
c8f8e27dd11ac98d0955e6ecc7d59c4eb346642b601ca63e6c4159413de6444e  WIDTH_ROUTE.md
c95075a84a47529d78873f9a6c342b950e640d51145a28577179de286d1f9e3b  POPULATION_CAVITY_ATTEMPT.md
```

The exact identities and conditional implication were internally derived;
(H) remains unproved. This is collaborative research, not an independent
promotion review.
