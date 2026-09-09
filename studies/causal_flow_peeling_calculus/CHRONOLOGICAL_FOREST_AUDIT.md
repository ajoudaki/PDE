# Chronological-Forest Audit

## Disposition

The first CCTC master estimate

\[
 M_{p,k}\le C^{p+k}p!\sqrt{k!}
\]

is false.  More importantly, its informal proof multiplied three bounds that
cannot be separated: nonlinear-tree symmetry, chronological volume, and
tied-Gaussian/equality contractions.  A weaker factorial estimate remains
conceivable only as a **joint**, leading-width, sign-aware theorem.

## 1. Scalar gate already requires factorial response growth

For `m>=1`,

\[
 \arctan^{(m)}(x)
 =\frac{(-1)^{m-1}(m-1)!}{2i}
 \big[(x-i)^{-m}-(x+i)^{-m}\big].
\tag{1}
\]

At `x=1`, along an infinite subsequence,

\[
 |\arctan^{(m)}(1)|
 \ge c^m(m-1)!.
\tag{2}
\]

The scalar Picard expansion for `x'=lambda arctan(x)` contains a legal star
whose root takes the `r`-th gate derivative and whose children take first
increments:

\[
 T_r(t)
 =\frac{F^{(r)}(x_0)F(x_0)^r}{(r+1)!}t^{r+1}.
\tag{3}
\]

Before the global Taylor symmetry in (3), this family has factorial, not
square-root-factorial, mass.  Thus any forest norm containing unnormalized
gate responses needs a full `C^k k!` budget.

The same conclusion follows from the previously proved Hermite asymptotic.
For `d(z)=(1+z^2)^(-1)`, normalized Hermite coefficients satisfy

\[
 |b_q|\asymp q^{-1/4}e^{-\sqrt q}.
\]

Since

\[
 \mathbb E\|D^kd(Z)\|^2
 =\sum_{q\ge k}(q)_k|b_q|^2,
\]

the term `q` near `k^2` alone gives

\[
 \|D^kd(Z)\|_2\ge c^k\frac{k!}{\operatorname{poly}(k)}.
\tag{4}
\]

Hence `C^k sqrt(k!)` cannot hold even for a single primitive gate.

## 2. Branching does not have a blanket simplex factorial

A chain of `k` strict causal times has volume `T^k/k!`.  A rooted tree only
orders ancestors.  If `tau_v` is the subtree below vertex `v`, its number of
linear extensions and time volume are

\[
 L(\tau)=\frac{k!}{\prod_v|\tau_v|},
 \qquad
 \operatorname{Vol}(\tau)=\frac{T^k}{\prod_v|\tau_v|}.
\tag{5}
\]

For a star, (5) is `T^k/k`, not `T^k/k!`.  At Euler mesh `h=T/M`, the same
limit comes from

\[
 h^k\sum_{m<M}m^{k-1}.
\]

Taylor factors `1/d_v!` at a branching vertex can restore the lost symmetry,
but the derivative `(d_v-1)!` in (1) cancels nearly all of it.  Therefore
time volume, gate derivatives, tree labels, and sibling permutations must be
counted together.

## 3. Fixed-width absolute bounds cannot be uniform in response depth

Let `G_ij=g_ij/sqrt(n)` and inspect one exact forward/transpose backtrack,

\[
 S_i=(GG^*)_{ii}=\frac1n\sum_{j=1}^ng_{ij}^2.
\]

Its moments are

\[
 \mathbb ES_i^k
 =\prod_{r=0}^{k-1}\left(1+\frac{2r}{n}\right).
\tag{6}
\]

For each fixed `k`, (6) tends to one as width tends to infinity.  At `n=1`,
however, it is `(2k-1)!!`.  Coupling `S_i` into the scalar star makes the
absolute coefficient as large as

\[
 C^k(k-2)!(2k-1)!!
 \gtrsim C^k\frac{(k!)^2}{k^{5/2}}.
\tag{7}
\]

Thus no all-`n`, all-`k` `C^k k!` bound follows from width normalization.
Fixed-order leading-width power counting and response-depth summation cannot
be interchanged termwise.

The obstruction is not proof that the signed/resummed object diverges.  For
example,

\[
 \mathbb Ee^{pTS_i}
 =\left(1-\frac{2pT}{n}\right)^{-n/2}
\]

where finite, while `e^{-TS_i}<=1`.  It proves that absolute forest bounds
can destroy the cancellation needed for a uniform continuum estimate.

## 4. Separate Wick and tree counting overcounts

With order `k`, unrestricted Gaussian pairings already contribute
approximately

\[
 (2k-1)!!\asymp C^k k!,
\]

and nonlinear Faà di Bruno forests naturally contribute another
`C^k k!`.  Multiplying these estimates yields the false scale `(k!)^2`.

The only plausible repair is a topological statement that most Wick/equality
gluings are incompatible with most zero-width-defect nonlinear forests.
Fixed-boundary planar-map intuition suggests exponential leading-width
growth, but it does not prove the required compatibility.

Equality partitions also require explicit moment-port bookkeeping.  For
`Z_i=sqrt(n)(S_i-1)`,

\[
 \mathbb EZ_i^2=2,
 \quad \mathbb EZ_i^3=8/\sqrt n,
 \quad \mathbb EZ_i^4=12+48/n.
\]

Two-copy contractions survive.  A theorem for each fixed `p` with an
unspecified constant `C_p` cannot imply a tail; the dependence on `p` must be
part of the joint estimate.

## 5. Volterra language does not provide an a priori bound

For a prescribed kernel `||K||<=L`, the resolvent is bounded by `e^(LT)`.
But a response self-energy can contain the response itself, schematically

\[
 K_R(t,s)=\mathbb E[G D(t)R(t,s)D(s)G^*].
\]

A bound `||K_R||<=C(1+||R||)` is circular and gives no a priori control.
Moreover absolute values can remove stabilizing sign, as the positive versus
negative exponential of `S_i` demonstrates.  A legal chain resummation must
preserve sign/positivity structure and bound its kernel independently of the
unknown resolvent.

## 6. Sharp surviving candidate

After independently closing unary response chains, define `Pi_0(tau;g,p)`
to be the tied Wick/equality gluings of zero width defect for a forest `tau`,
with observable grade `g` and explicit moment-port number `p`.  The remaining
candidate theorem is

\[
 \boxed{
 \sum_{|\tau|=k}L(\tau)
 \prod_{v\in\tau}
 \frac{|\arctan^{(d_v)}(x_v)|}{d_v!}
 \sum_{\pi\in\Pi_0(\tau;g,p)}|w(\tau,\pi)|
 \le C_{g,p}^k k!.
 }
\tag{JC}

The theorem must also give explicit admissible growth of `C_(g,p)` in `p`
and a finite-width remainder that is uniform after sign-preserving chain
resummation.  At the normalized coefficient level `b_k=F_k/k!`, a plausible
analytic recursion has the form

\[
 b_{k+1}
 \le s_k+L_{g,p}\sum_{r\ge2}\frac{C^r}{r}
 \sum_{k_1+\cdots+k_r=k}b_{k_1}\cdots b_{k_r}.
\tag{8}
\]

Its generating function is locally controlled by a logarithm, giving a
positive block radius but not an entire response series.  Finite blocks can
then be restarted only if the controlled constants are present-time state
certificates.

`(JC)` is a genuine candidate combinatorial lemma.  It is not yet a
completion theorem.  In addition one needs:

1. a non-circular, sign-aware unary-chain bound;
2. the explicit `p` dependence needed for occupation uniform integrability;
3. a finite-width/response-tail estimate compatible with the order
   `n -> infinity` then mesh removal;
4. uniqueness and restart in the resulting controlled state class.

Until these are proved, chronological forests are a structured restatement,
not yet a meaningful reduction of the continuous-time limit.
