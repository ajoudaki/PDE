# Yudovich--Orlicz Stability for Activation-Gated Energy Fields

## Claim level

This note proves a reusable stability rule.  It replaces the crude
clip-dependent Lipschitz estimate `exp(C R)` by an Osgood estimate whenever
the unclipped multiplier has projective moment growth at most
subexponential.  It does **not** prove that the depth-three adaptive
transpose field has that moment envelope; that is the remaining source-query
theorem.

The rule is useful precisely because it changes the required tail class.
Gaussian decay is no longer needed to defeat an artificial stability
factor.  A uniform `psi_1` envelope is sufficient, and a `psi_2` envelope is
more than sufficient.

## 1. Joint probability--coordinate norms

Let `I_n` be uniform on `{1,...,n}`, independent of all network randomness.
For a random field `v in R^n`, write

\[
 \|v\|_{p,*}
 :=\bigl(\mathbb E|v_{I_n}|^p\bigr)^{1/p}
 =\left(\mathbb E\frac1n\sum_{i=1}^n|v_i|^p\right)^{1/p}.
\tag{1}
\]

This norm measures the empirical law rather than the largest coordinate.
For `0 <= beta <= 1`, define the projective Yudovich envelope

\[
 [v]_{\mathcal Y_\beta}
 :=\sup_{p\ge2}p^{-\beta}\|v\|_{p,*}.
\tag{2}
\]

The case `beta=1/2` is subgaussian moment growth and `beta=1` is
subexponential moment growth.  In applications it is enough to prove (2)
one finite `p` at a time with the same majorant, because every target
accuracy invokes only finitely many orders before width is sent to infinity.

## 2. The multiplier interpolation lemma

**Lemma 2.1.**  Suppose `|a_i| <= 1` and

\[
 \|a\|_{2,*}\le\delta\le e^{-2}.
\]

If `[r]_{Y_beta} <= K`, then

\[
 \|r\odot a\|_{2,*}
 \le C_\beta K\,\delta
       \bigl[\log(e/\delta)\bigr]^\beta .
\tag{3}
\]

**Proof.**  Fix `p>2` and put `q=2p/(p-2)`.  Holder and interpolation
between `L^2` and `L^infty` give

\[
 \|ra\|_{2,*}
 \le \|r\|_{p,*}\|a\|_{q,*}
 \le Kp^\beta\delta^{1-2/p}.
\tag{4}
\]

Writing `s=log(1/delta)`, choose
`p=max(4,2s/beta)` when `beta>0`; the bounded case `beta=0` is immediate.
Then `delta^{-2/p}` is bounded by a constant depending only on `beta`, and
`p^beta <= C_beta log(e/delta)^beta`.  This proves (3).  No independence
between `r` and `a` was used.  QED.

The same conclusion holds when `|a| <= B`: rescale `a/B` and replace the
logarithm by `log(eB/delta)`.

## 3. Application to a smooth gate

Let `d:R->R` be bounded and Lipschitz.  For two fields `(z,r)` and
`(z_tilde,r_tilde)`, decompose

\[
 d(z)r-d(\widetilde z)\widetilde r
 =d(z)(r-\widetilde r)
  +[d(z)-d(\widetilde z)]\widetilde r.
\tag{5}
\]

The first term is ordinary energy-Lipschitz.  For the second, set

\[
 a=\frac{d(z)-d(\widetilde z)}{2\|d\|_\infty}.
\]

Then `|a|<=1` and

\[
 \|a\|_{2,*}
 \le C_d\|z-\widetilde z\|_{2,*}.
\]

Lemma 2.1 therefore yields, for small `D` controlling
`||z-z_tilde||_(2,*)`,

\[
 \|[d(z)-d(\widetilde z)]\widetilde r\|_{2,*}
 \le C_dK D[\log(e/D)]^\beta.
\tag{6}
\]

For arctangent, `d(s)=(1+s^2)^{-1}`, so the hypotheses hold globally.

## 4. Osgood completion theorem

Let `X` and `X^R` be two coupled network flows, the second using a smooth
clip of one activation-gated multiplier.  Suppose all deterministic source,
contraction, rank-one, mobility-chart, and bounded-gate rules give, in a
joint `L^2(Omega x coordinate)` state metric, the integral inequality

\[
 D(t)\le a_R+
 C\int_0^t D(s)[\log(eM/D(s))]^\beta\,ds,
 \qquad 0\le t\le T,
\tag{7}
\]

where `0<=beta<=1`, `0<=D<=M`, and `a_R` is the accumulated clipping
forcing.  Inequality (7) is exactly what (6) supplies for every otherwise
Lipschitz activation-gated product.  Constants may also include a localized
source operator norm, but they do not contain the clipping radius.

Then `D -> 0` uniformly on `[0,T]` whenever `a_R -> 0`.

For `0<=beta<1`, Bihari's inequality gives the explicit modulus

\[
 \sup_{t\le T}D(t)
 \le eM\exp\left\{-
 \left(
 [\log(eM/a_R)]^{1-\beta}
 -C(1-\beta)T
 \right)_+^{1/(1-\beta)}
 \right\}.
\tag{8}
\]

For `beta=1`,

\[
 \sup_{t\le T}D(t)
 \le eM\left(\frac{a_R}{eM}\right)^{e^{-CT}}.
\tag{9}
\]

The usual harmless regularization `D -> D+epsilon` proves these formulas
when `D` is only absolutely continuous or obeys an upper-Dini inequality.
The divergence

\[
 \int_{0^+}\frac{ds}{s[\log(eM/s)]^\beta}=\infty
 \quad\Longleftrightarrow\quad \beta\le1
\tag{10}
\]

is the sharp Osgood threshold for this argument.

## 5. Clip removal

Let `kappa_R` be one-Lipschitz and equal to the identity on `[-R,R]`.
If the clipped multiplier `r^R` obeys

\[
 \sup_{n,R}\sup_{t\le T}
 \|r^R(t)\|_{p,*}\le K_Tp^\beta,
 \qquad p\ge2,
\tag{11}
\]

then its clipping forcing satisfies, for every `p>2`,

\[
 \|(r^R-\kappa_R(r^R))\|_{2,*}
 \le R^{1-p/2}\|r^R\|_{p,*}^{p/2}
 \xrightarrow[R\to\infty]{}0.
\tag{12}
\]

In comparing the untruncated and truncated systems, write the bad product as

\[
 d(z)r-d(z^R)\kappa_R(r^R)
 =d(z)(r-r^R)
  +[d(z)-d(z^R)]r^R
  +d(z^R)[r^R-\kappa_R(r^R)].
\tag{13}
\]

Thus the Osgood coefficient uses the **clipped-flow** field `r^R`; no tail
assumption on the as-yet-uncontrolled untruncated field is needed.  Equations
(6)--(13) give a noncircular bootstrap.

For convergence at a prescribed tolerance, optimization in Lemma 2.1 uses
only a finite moment order `p=O(log(1/delta))`.  Hence (11) can be interpreted
projectively: establish each fixed order with a common computable majorant,
take width to infinity, and only then increase the requested order.  No
growing-order Tensor Program theorem is being assumed.

## 6. Consequence for depth three

For the depth-three arctangent flow, the only new multiplier after the
bottom mobility chart and top seed clipping is

\[
 r_2=G_2^*b_3,
 \qquad b_2=d(z_2)r_2.
\]

The former `exp(CR)` obstruction is therefore superseded by the following
strictly weaker source-query obligation:

> Prove, for the `r_2`-clipped flow, the projective moment estimate
> \[
> \sup_{n,R}\sup_{t\le T}
> \|r_2^R(t)\|_{p,*}\le K_Tp^\beta
> \]
> with some `beta<=1`, after the already certified source-operator
> localization and its removal.

This is a real reduction: it asks for value moments of one typed adaptive
query, not a pathwise Lipschitz constant, a maximum-coordinate tail, or the
full compact-time convergence theorem.  It remains unproved at the time of
this note.

### Finite-width tail-class correction

For the actual Gaussian initialization, the uniform choice `beta=1/2` is
impossible at finite width.  At `t=0`, conditional on `u,G_1,G_2`, each
`r_(2i)` is Gaussian in the endpoint `A` with random variance

\[
 S_i=\sum_mG_{2,mi}^2d(z_{3m})^2.
\]

The law of `S_i` has unbounded support, so
`E exp(lambda r_(2i)^2)=infinity` for every `lambda>0`.  Equivalently, no
width-uniform all-order `K sqrt(p)` moment envelope can hold.  The product of
the rare large source entry and the Gaussian endpoint has the natural
subexponential, rather than subgaussian, scale.

Thus `beta=1` is the sharp plausible projective target for an unlocalized
finite-width proof.  A width-first localization may still reveal a Gaussian
bulk limit, but it must keep its rare-event error separate.  See
`MARKED_CAUSAL_CAVITY_AUDIT.md`.
