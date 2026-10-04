# Conditional check of strict root-width folding and retained storage

2026-10-04. Scoped downstream reconstruction of
INTRINSIC_STRICT_ROOT_ROUTE.md, frozen at SHA-256
`c3c1e5d10c32458ca08dbbbe6251efdb0ee400e5301a50aff943d7064d6ad7d1`.
The complete frozen candidate was read. This check concerns Sections 2
and 5--7, plus the event and probability scope of Section 4. It does not
independently certify the new passive-backward insertion identity or its
stopped-domain bootstrap. No sibling verdict, new constant refinement,
other-study source, experiment, Git operation, or maintained-file edit
was used. Required canonical-notation, neural, rigorous-proof, and research
instructions were applied.

**Verdict: conditional PASS.** Given the fixed-query moments (19) with
the precise event and uniformity stated there, the one-half Hölder
estimate, Gaussian rotation bound, fixed-moment chaining through the
endpoint, exact restricted realization, and retained-coordinate count
follow. There is no logarithmic width loss in this implication. This
verdict does not certify (19)'s new insertion proof; its required form is
recorded explicitly below.

## 1. Exact event and moment hypotheses

Let the fixed unit training inputs span a subspace \(V\) of dimension
\(r\), and write \(k=d-r\). Choose the orthonormal coordinate matrices
\(U\in\mathbb R^{d\times r}\) and
\(E\in\mathbb R^{d\times k}\) deterministically from the fixed data.
Let \(\mathcal F\) contain \(A_0U\), the hidden initialization, and the
data, and put \(G=A_0E\). Rowwise Gaussian orthogonal invariance proves
that \(G\) has independent standard Gaussian entries and is independent
of \(\mathcal F\).

The first-weight equation implies \(\dot A E=0\), since
\(v_a^\top E=0\). The training ODE contains no \(G\), so its full path
is \(\mathcal F\)-measurable. For every real query \(v\),
\[
 z^{(1)}(t,v)=A_V(t)U^\top v+GE^\top v,\qquad A_V=AU.
 \tag{1}
\]
The event \(E_n\) needed below is \(\mathcal F\)-measurable, has
probability tending to one, and supplies the global real fitting and
parameter tube in (7) of the candidate. Only the separate carrier
budgets need be limited to its source horizon \(T_n\). This explicitly
distinguishes the all-time real tube from the finite-horizon budgets;
the candidate's displayed \(\sup_t\) bounds require this interpretation.
The inherited global real fitting event for the training model with
first coordinates \(U\) has precisely this measurability.

In particular \(E_n\) imposes no bound on \(G\), no passive-query
maximum restriction, and no full-initialization first-weight norm
restriction. On \(E_n\), for every real \(G\), all real query gates are
bounded and the deterministic backward induction gives
\[
 \sup_{t,v,\ell}\|k^{(\ell)}(t,v)\|_{2,n}\le CS,
 \qquad \sup_t\|w(t)\|_\infty\le BS,
 \tag{2}
\]
where \(\|a\|_{p,n}=(n^{-1}\sum_i|a_i|^p)^{1/p}\) and
\(S=16Y/\lambda\le1\). These estimates do not require Gaussian
concentration at the query.

The additional hypothesis audited downstream is: for every fixed real
\(q\ge2\),
\[
 \sup_{n\ge n_0(q)}\sup_{t\in[0,\infty],\,v\in S^{d-1},\,\ell}
 \mathbb E[\mathbf1_{E_n}\|k^{(\ell)}(t,v)\|_{q,n}^q]
                          \le C_qS^q.
 \tag{3}
\]
The constants and threshold may depend on fixed data, depth, dimension,
and \(q\); they cannot depend on the evaluated time, query, or width.
No simultaneous query supremum is inside (3). A finite number of fixed
moment orders suffices below. The inserted query is passive, and the
reference system remains the actual dense trained realization.

The probability passage in the candidate's Section 4 is compatible with
(3) if its local comparison event has arbitrarily high fixed polynomial
success probability. On \(E_n\), (2) gives the deterministic coordinate
bound \(|k_i|\le CS\sqrt n\). Hence an exceptional event of probability
at most \(C_Mn^{-M}\) contributes at most
\(C_qS^qn^{q/2-M}\) to a fixed-coordinate \(q\)-moment. Choose
\(M>q/2+2\). On the good event one can remove all event indicators
from a nonnegative Gaussian upper bound before conditioning on the
omitted root's cavity. The cavity reference must be defined using its
own stops and its own failed-initialization convention, so it remains
independent of that root. In this argument \(E_n\) need not be
independent of an omitted hidden-matrix root: its indicator is dropped
before the conditional Gaussian moment is evaluated.

These are necessary scope conditions, not a verification of the new
comparison itself. If (19) is obtained only after intersecting \(E_n\)
with a query event depending on \(G\), or only conditionally on
full-network survival, it is insufficient in that weaker form. The
frozen candidate instead explicitly states (3) with the original
\(\mathcal F\)-measurable event, which is the correct form.

## 2. The deterministic all-time extension is consistent

The candidate's all-time extension of (19) can be checked without its
new insertion calculation. Write \(\rho(t)\le Ye^{-\kappa t}\), where
\(\kappa=\lambda/4\), and use the real tube. For every real \(G\)
and unit query, the forward velocity recursion gives
\[
 \|\dot z^{(\ell)}(t,v)\|_{2,n}\le C\rho(t)S.
\]
There is no \(G\)-dependent parameter velocity: the first input term is
\(\dot A_VU^\top v\), and all other inhomogeneous terms are trained
matrix velocities times bounded features. Bounded mixers propagate the
estimate through depth.

Differentiating the backward recursion and applying (2) gives
\[
 \|\dot\delta^{(\ell)}(t,v)\|_{2,n}
       +\|\dot k^{(\ell)}(t,v)\|_{2,n}
       \le C\rho(t)(1+S^2\sqrt n).
 \tag{4}
\]
For its curvature term use
\(\|k\odot\dot z\|_{2,n}
\le\|k\|_\infty\|\dot z\|_{2,n}
\le CS^2\sqrt n\rho\); changed-matrix terms have size
\(C\rho S^2\), and the terminal readout velocity has RMS \(C\rho\).
Passing to coordinates and integrating gives
\[
 \sup_{t\ge T,v,i,\ell}
 |k_i^{(\ell)}(t,v)-k_i^{(\ell)}(T,v)|
 \le CS(\sqrt n+S^2n)e^{-\kappa T}
 \le CSn e^{-\kappa T},
 \tag{5}
\]
after adjusting a numerical constant. Since
\(\kappa T_n=8\log(en)\), this is at most \(CSn^{-7}\). Thus
finite-horizon moments of the required form extend to every time and
the fitted endpoint, with a changed fixed constant. This tail bound is
uniform over all real \(G\) on \(E_n\).

## 3. One-half Hölder increments from fixed carrier moments

Use the deterministic proof clock
\(\tau(t)=1-e^{-\kappa t}\), including \(\tau(\infty)=1\).
Integrating the actual weight velocities proves
\[
 \|w(t)-w(s)\|_{2,n}\le CS|\tau(t)-\tau(s)|,
\]
\[
 \|W^{(\ell)}(t)-W^{(\ell)}(s)\|_{\rm op}
 +\|A_V(t)-A_V(s)\|_{\rm op}/\sqrt n
            \le CS^2|\tau(t)-\tau(s)|.
 \tag{6}
\]
The factor comes from \(\int_s^t\rho(u)du
\le(Y/\kappa)|\tau(t)-\tau(s)|\), with \(Y/\kappa=S/4\).
The use of a deterministic clock avoids any Gaussian-dependent inverse
activity time.

Bounded slopes and mixers, (1), and (6) give for each layer
\[
 \|z^{(\ell)}(t,v)-z^{(\ell)}(s,v')\|_{2,n}\le C D,
\quad
 D=(1+\|G\|_{\rm op}/\sqrt n)\|v-v'\|
                       +S^2|\tau(t)-\tau(s)|.
 \tag{7}
\]
If \(s_\phi,t_\phi\) bound the first and second activation derivatives
on the real axis, pointwise
\[
 |\phi'(z)-\phi'(z')|^4
     \le(2s_\phi)^2t_\phi^2|z-z'|^2.
\]
Thus the normalized counting-four norm of the changed gate is at most
\(C D^{1/2}\). In backward subtraction, multiply that changed gate
by the carrier at the reference point \((s,v')\). Counting Hölder
therefore yields
\[
 \|\delta^{(1)}(t,v)-\delta^{(1)}(s,v')\|_{2,n}
 \le CS|\tau(t)-\tau(s)|
      +CD^{1/2}\sum_{\ell=1}^L\|k^{(\ell)}(s,v')\|_{4,n}.
 \tag{8}
\]
Indeed a changed mixer contributes at most
\(CS^3|\tau(t)-\tau(s)|\) by (2), while the terminal changed readout
has the first bound in (6). Downward induction gives (8).

For any fixed \(p\ge2\), (3) at order \(2p\) and counting-norm
monotonicity imply
\[
 \left\|\mathbf1_{E_n}\sum_\ell
             \|k^{(\ell)}(s,v')\|_{4,n}\right\|_{L^{2p}}
                                                        \le C_pS.
\]
All moments of \(\|G\|_{\rm op}/\sqrt n\) are uniformly bounded
in width for fixed \(k\). The Frobenius norm suffices: its square divided
by \(n\) is a normalized sum of \(nk\) Gaussian squares. Jensen for
their normalized average supplies the uniform fixed-moment bound.
Probability Hölder, without independence of the two factors in (8),
then gives
\[
 \|\mathbf1_{E_n}
  [\delta^{(1)}(t,v)-\delta^{(1)}(s,v')]\|_{L^p(\ell^2_n)}
 \le C_pS\bigl(|\tau(t)-\tau(s)|+\|v-v'\|\bigr)^{1/2}.
 \tag{9}
\]
The compact index diameter absorbs the linear time term. No supremum
query-carrier moment or coordinate maximum was substituted for (3).

## 4. Conditional Gaussian rotation preserves the correct event

For a fixed \(\mathcal F\) in \(E_n\), the trained matrices are
constants as functions of \(G\). Differentiation through the query
network therefore gives the exact Frobenius gradient
\[
 \nabla_G f_n(t,v)
            =n^{-1}\delta^{(1)}(t,v)(E^\top v)^\top.
 \tag{10}
\]
The transpose is algebraic here; all quantities in this real
concentration argument are real. In particular the query response in
(10) is an actual input derivative, even though a later compressed
optimizer uses different backward training signals.

Here is a complete dimension-free version of the rotation estimate. Let
\(G'\) be an independent Gaussian copy and put
\(G_\theta=G\cos\theta+G'\sin\theta\),
\(\dot G_\theta=-G\sin\theta+G'\cos\theta\). For each \(\theta\),
these two matrices are independent standard Gaussians. For a smooth
scalar function \(H\), conditional Jensen and the fundamental theorem
of calculus give
\[
 \|H-\mathbb EH\|_p
 \le\|H(G)-H(G')\|_p
 \le\int_0^{\pi/2}
        \|\langle\nabla H(G_\theta),\dot G_\theta\rangle_F\|_p
                                                     \,d\theta
 \le C\sqrt p\,\|\|\nabla H(G)\|_F\|_p.
 \tag{11}
\]
The last step conditions on \(G_\theta\) and uses the scalar Gaussian
\(p\)-moment. Here \(H=f_n(t,v)-f_n(s,v')\) is bounded on the real
Gaussian domain, and its gradient is bounded by (2), so the integrations
are justified. A cutoff-and-limit argument gives the same statement
under mere integrability if needed.

Crucially, one may multiply the conditional inequality by
\(\mathbf1_{E_n}\) and integrate over \(\mathcal F\): that indicator
is unchanged by every rotation of \((G,G')\). No query-success event is
conditioned on or inserted into this step. The moment estimate (3)
is allowed to be only an integrated \((\mathcal F,G)\)-moment; a
uniform moment bound for almost every individual \(\mathcal F\) is
unnecessary.

Define \(\bar f_n=\mathbb E_G[f_n\mid\mathcal F]\) and
\(Z_n=\sqrt n(f_n-\bar f_n)\). From (10),
\[
 \sqrt n\|\nabla_G[f_n(t,v)-f_n(s,v')]\|_F
 \le\|\delta^{(1)}(t,v)-\delta^{(1)}(s,v')\|_{2,n}
                     +CS\|v-v'\|.
\]
Combining this with (9)--(11) proves precisely
\[
 \|\mathbf1_{E_n}[Z_n(t,v)-Z_n(s,v')]\|_p
       \le C_pS\bigl(|\tau(t)-\tau(s)|+\|v-v'\|\bigr)^{1/2}.
 \tag{12}
\]
The conditional centering has been retained throughout.

## 5. Fixed-moment chaining includes the endpoint

Give \([0,1]\times S^{d-1}\) the metric
\(d_*((\tau,v),(\tau',v'))=|\tau-\tau'|+\|v-v'\|\).
A time mesh and an ambient Euclidean sphere net give nets of mesh
\(2^{-j}\) and size at most \(C_d2^{j(d+1)}\). The dimension exponent
is loose but valid. Connect each point to a nearest point of the previous
net; each connecting distance is at most \(C2^{-j}\).

Choose one fixed integer \(p>2(d+1)\). For the maximum of the scale-\(j\)
increments, (12) and
\(\|\max_i|X_i|\|_p^p\le\sum_i\|X_i\|_p^p\) give
\[
 C_pS,2^{-j/2}2^{j(d+1)/p}.
\]
This is summable in \(j\). Values on the finite first net are bounded
using (12) and \(Z_n(0,v)=0\). Minkowski on a finite tree, followed
by monotone convergence/Fatou, bounds the supremum on the union of nets
in \(L^p\) by \(C_pS\), uniformly in width.

On \(E_n\), trained parameters converge by the inherited real fitting
and finite residual activity. For every fixed real \(G\), the actual
query output is continuous on the sphere and through \(t=\infty\).
Its uniform bound \(|f_n|\le B^2S\) permits dominated convergence in
the conditional mean, so the centered process is continuous on the same
compact index space. Consequently the countable-net supremum equals the
full supremum, and
\[
 \left\|\mathbf1_{E_n}\sup_{t\in[0,\infty],v\in S^{d-1}}
                       |Z_n(t,v)|\right\|_p\le C_pS.
 \tag{13}
\]
The process can be defined arbitrarily at the endpoint outside \(E_n\);
all endpoint assertions in this calculation have its indicator.

For any fixed confidence \(1-\xi\), make
\(\Pr(E_n^c)\le\xi/2\) by increasing the width. Markov applied to
(13) supplies a width-independent bound on the remaining supremum with
failure at most \(\xi/2\). Neither a moment order growing with width
nor a \(\sqrt{\log n}\) multiplier enters this argument.

For fixed \(\mathcal F\), the conditional distribution of \(GE^\top v\)
depends only on \(\|E^\top v\|\), while the offset in (1) depends
only on \(U^\top v\). The conditional means at \(v\) and
\(\widetilde v=P_Vv+\|P_{V^\perp}v\|e\) are therefore exactly equal
when \(e\) is any fixed, data-chosen unit vector in \(V^\perp\).
Both queries lie on the same unit sphere. Their output difference is
at most twice the centered supremum divided by \(\sqrt n\), proving
the candidate's strict all-time whole-sphere folding conclusion.

## 6. Canonical restricted realization and storage provenance

When \(r+1<d\), set \(D=r+1\) and
\(Q=[U,e]\in\mathbb R^{d\times D}\). The columns of \(Q\) are
orthonormal and depend only on fixed data. Thus \(A_0Q\) has independent
standard Gaussian entries, is independent of every hidden initialized
matrix, and is exactly the canonical first-layer initialization in
dimension \(D\). This is a restriction of the same realization, not a
resampled network.

The normalized projected training inputs are \(Q^\top v_a\), of norm
one. To match the convention \(v'=x'/\sqrt D\), take
\(x'_a=\sqrt D\,Q^\top v_a\). Their pairwise normalized inner
products agree with the original ones, hence the limiting Gram recursion
and \(\gamma\) are unchanged. The first-weight dynamics restricted to
\(Q\) are exactly
\(\dot A Q=(2/m)\sum_a c_a\delta_a^{(1)}(Q^\top v_a)^\top\).
All remaining training equations agree. Uniqueness of the finite
training ODE therefore identifies the entire hidden/readout training
path, residual, and physical time with the original realization.

At runtime the compressor receives
\[
 \left(U^\top v,
     \sqrt{\|v\|^2-\|U^\top v\|^2}\right).
 \tag{14}
\]
Its norm is one and its lifted query under \(Q\) is exactly
\(\widetilde v\). The radicand is the squared norm of an orthogonal
projection and is nonnegative. The representation contract permits this
norm operation. Its expression near zero requires no smoothness
assumption: folding was controlled through the original sphere supremum,
and exact-real arithmetic is the existing resource convention.

Store \(U\) in \(dr\) real coordinates and use \(O(d+r)\) work
coordinates. The full complement basis \(E\) is unnecessary at runtime;
even \(e\) can be discarded after the restricted initialized arrays have
been compressed. The smaller model retains only the usual selected
neural arrays, fixed metrics, data, and solve caches. It retains neither
\(G\), \(A_0Q\) at original width, a conditional-mean evaluator, nor
any dense trained trajectory.

Apply the inherited compression theorem in dimension \(D\), with its
unchanged \(\beta,L,m,\gamma,Y\), and add the projection storage above.
This gives (31) of the candidate, including its separate data term.
The folding event and the compression event may be dependent; allocating
half the requested failure probability to each and using a union bound
is sufficient. Their errors add, both with the strict \(n^{-1/2}\)
rate and including the endpoint. The additional folding constant is
allowed to depend on fixed ambient dimension and confidence, as stated
by the candidate.

If \(r+1\ge d\), use the original dimension-\(d\) compressor and
omit the projection. In particular \(r=d\) has no unused Gaussian
columns and no folding direction is required. The construction proves
no source-dimension saving when the training span is already this large.

## 7. Remaining dependency and precise failure condition

Everything from (3) through (14) above is a closed downstream implication.
The unresolved item within this check's scope boundary is whether the
new passive-backward insertion calculation really proves (3), with no
stronger label assumption and with exceptional probabilities sufficient
for each fixed chosen moment. That is assigned to the separate insertion
checker.

There would be a substantive failure if the available moment bound held
only on a \(G\)-dependent success event that could not be removed using
the deterministic RMS bound and arbitrarily high polynomial exceptional
probabilities. Gaussian rotation would then leave that event, invalidating
the displayed conditional argument. The candidate explicitly avoids
this restriction, and its stated moment hypothesis has exactly the form
needed. This report certifies that conditional implication, not the
unreviewed core insertion lemma.
