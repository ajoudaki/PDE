# Malliavin Banach-Scale and Gevrey--Borel Completion Audit

## Verdict

A Malliavin/response Banach scale is an honest way to organize fixed-order
Gaussian peeling without claiming a false same-space algebra. It predicts
the correct nonanalytic coefficient growth and makes every loss of response
regularity explicit. It does not complete the flow.

For loss exponent greater than one, a Banach-scale estimate alone does not
even imply existence of a real evolution. Gevrey coefficient bounds do not
identify a function because of flat-function ambiguity. Borel completion
additionally requires common sectorial continuation, growth bounds, and
identification of every finite-width real flow with its Borel sum. At depth
three, those conditions require at least the missing reachable
occupation/tangent theorem and are plausibly stronger.

The route is **KILL as an automatic completion of MFP**. Its tame scale and
the exact toy Borel calculation remain useful diagnostics.

## 1. Most favorable typed source-functional scale

Write

\[
\Gamma_{l,ij}=n^{-1/2}\xi_{l,ij},\qquad \xi_{l,ij}\sim N(0,1),
\]

and let \(\mathsf H_n\) be the Cameron--Martin space of all initialization
sources. Use typed vector norms

\[
|v|_{p,n}
=\left(\mathbb E\frac1n\sum_i|v_i|^p\right)^{1/p}.                 \tag{1}
\]

Split every trained matrix as

\[
G_l=\Gamma_l+K_l.
\]

For the learned part use the normalized projective factorization

\[
K=n^{-1}\sum_\nu a_\nu c_\nu^T,\qquad
\|K\|_{\Pi,p}
:=\inf\sum_\nu\big\||a_\nu|_n|c_\nu|_n\big\|_{L^p}.               \tag{2}
\]

Then

\[
Kx=\sum_\nu a_\nu\langle c_\nu,x\rangle_n
\]

is dimensionally controlled. The immutable \(\Gamma_l\) remains a
distinguished Gaussian-source operation; it is not absorbed into (2).

For a typed source functional \(F\), define

\[
\|F\|_{\rho,p}
=\sum_{r\ge0}\frac{\rho^r}{r!}
\|D^rF\|_{L^p(\mathsf H_n^{\otimes r};E_n)}.                      \tag{3}
\]

The embeddings lose response radius and integrability:

\[
\rho_2\ge\rho_1,\quad p_2\ge p_1
\quad\Longrightarrow\quad
\mathbb J_{\rho_2,p_2}\hookrightarrow\mathbb J_{\rho_1,p_1}.
\]

There is no same-space multiplication theorem. The valid tame rule is

\[
\|FG\|_{\rho,p}
\le\|F\|_{\rho,p_1}\|G\|_{\rho,p_2},
\qquad \frac1p=\frac1{p_1}+\frac1{p_2}.                           \tag{4}
\]

Every response factor consumes a separate Hölder budget.

A more honest state retains the complete tail profile
\(\mathbf a=(a_r)_{r\ge0}\):

\[
\|F\|_{\rho,\mathbf a}
=\sum_{r\ge0}\frac{\rho^r}{r!}
\sup_{p\ge2}(L\sqrt p)^{-a_r}\|D^rF\|_p.                          \tag{5}
\]

Here \(a_r=m\) means at most \(m\) uncapped Gaussian leaves. Product and
Nemytskii response rules are

\[
(\mathbf a\star\mathbf b)_r
=\max_{0\le j\le r}(a_j+b_{r-j}),                                 \tag{6}
\]

and

\[
(\mathcal C\mathbf a)_0=0,\qquad
(\mathcal C\mathbf a)_r
=\max_{\pi\in\Pi_r}\sum_{B\in\pi}a_{|B|}.                         \tag{7}
\]

This is a scale of tame products, not a Banach algebra.

For arctangent,

\[
\phi^{(m)}(x)
=\frac{(-1)^{m-1}(m-1)!}{2i}
\big((x-i)^{-m}-(x+i)^{-m}\big),
\]

so

\[
\|\phi^{(m)}\|_\infty\le(m-1)!.
\]

Faà di Bruno gives

\[
D^r\phi(F)=
\sum_{\pi\in\Pi_r}\phi^{(|\pi|)}(F)
\bigotimes_{B\in\pi}D^{|B|}F.                                    \tag{8}
\]

After shrinking \(\rho\), (8) is a dimension-independent atomic cap:
the value is bounded while its response ports inherit the input profile.

## 2. Exact Gaussian source action

For one standard Gaussian \(g\), Hölder gives, with
\(p=1/\eta\), \(q=1/\eta'\), and \(\eta'<\eta\),

\[
\|gF\|_p
\le C(\eta-\eta')^{-1/2}\|F\|_q.                                 \tag{9}
\]

The exact response identity is

\[
gF=\delta(Fe)+D_eF.                                                \tag{10}
\]

For a transpose matrix query,

\[
R_j=(\Gamma^TB)_j
=n^{-1/2}\sum_i\xi_{ij}B_i
=n^{-1/2}\delta_j(B)
+n^{-1/2}\sum_iD_{\xi_{ij}}B_i.                                  \tag{11}
\]

A normalized Meyer estimate has the form

\[
\|\Gamma^TB\|_{p,n}
\le C_p\left(
\|B\|_{p,n}+\|D_\Gamma B\|_{p,\mathrm{tr},n}
\right),                                                          \tag{12}
\]

with no explicit width loss. Passing from \(\rho\) to \(\rho'<\rho\)
bounds the contraction in (12) by a response-radius loss. This contraction
is precisely the persistent-source adaptivity; it cannot be dropped as a
fresh Gaussian term.

Atomic fixed-order estimates can therefore be dimension-independent. What
is not known uniformly in response order is the contraction/collision bound
for the reachable program class.

## 3. Loss greater than one does not generate a flow

Classical Ovsyannikov theory treats a one-radius loss,

\[
\|V(x)-V(y)\|_{a'}
\le\frac{L}{a-a'}\|x-y\|_a,
\]

with compatible holomorphy and base-point bounds. It yields a local
holomorphic solution in every smaller space.

The formally analogous statement for exponent \(\sigma>1\) is false without
additional smoothing or resolvent structure. Let

\[
X_a=\left\{x:\sup_m e^{a m^{1/\sigma}}|x_m|<\infty\right\},
\qquad (Ax)_m=mx_m.
\]

Then

\[
\|Ax\|_{a'}\le
C_\sigma(a-a')^{-\sigma}\|x\|_a.                                 \tag{13}
\]

Choose

\[
x_m^0=e^{-m^{1/\sigma}}m^{-2}\in X_1.
\]

The unique coordinatewise solution is

\[
x_m(t)=e^{mt}x_m^0,
\]

which belongs to no \(X_{a'}\) at any \(t>0\). Its formal derivatives obey

\[
\|A^kx^0\|_{a'}\asymp C^k(k!)^\sigma.                             \tag{14}
\]

Thus (13) yields a Gevrey formal hierarchy, not an evolution theorem.

This counterexample also defeats the advertised loss-only interpretation of
the generalized theorem in
[Luo--Yin](https://arxiv.org/pdf/1507.05250). The same issue appears in the
translation equation on spatial Gevrey classes: complex-time translation
has exponential Fourier growth that a sublinear Gevrey weight cannot absorb.
By contrast, the rigorous scale theorem of
[Friesen--Kutoviy](https://arxiv.org/pdf/1805.10597) imposes substantially
milder evolution-system loss restrictions and does not supply the needed
network result.

## 4. Exact Borel requirements and flat-function obstruction

Suppose

\[
\widetilde f(t)=\sum_{k\ge0}a_kt^k,\qquad
\|a_k\|\le CA^k\Gamma(1+\alpha k).                                \tag{15}
\]

The order-\(1/\alpha\) Borel transform is

\[
\widehat f(\xi)
=\sum_{k\ge0}\frac{a_k}{\Gamma(1+\alpha k)}\xi^k.                 \tag{16}
\]

To recover a function, (16) must analytically continue around the chosen
direction and satisfy

\[
\|\widehat f(\xi)\|\le Ce^{B|\xi|^{1/\alpha}}.                    \tag{17}
\]

The corresponding Laplace transform is

\[
f(t)=\frac1\alpha t^{-1/\alpha}
\int_0^{e^{id}\infty}
e^{-(\xi/t)^{1/\alpha}}\widehat f(\xi)
\xi^{1/\alpha-1}\,d\xi.                                          \tag{18}
\]

Uniqueness from the asymptotic series requires a time sector with opening
strictly greater than \(\pi\alpha\); at the threshold there are nonzero flat
functions. See the precise ultraholomorphic Watson criterion in
[Lastra--Malek--Sanz](https://arxiv.org/abs/1402.1669).

In particular, a real-axis Gevrey remainder cannot identify the flow. The
function

\[
g(t)=e^{-t^{-1/\alpha}},\qquad t>0,
\]

has every Taylor coefficient zero while being nonzero. Even a sequence
\((-1)^ng(t)\) has identical coefficients and uniform Gevrey remainders but
does not converge at positive time.

## 5. Exact toy Stieltjes summation

Let \(A\sim N(0,1)\) and put \(z=t^2\). Then

\[
F(z)=\mathbb E\frac1{1+zA^2}
\sim\sum_{m\ge0}(-1)^m(2m-1)!!\,z^m.                              \tag{19}
\]

The ordinary Borel transform in \(z\) is exactly

\[
\widehat F(\xi)
=\sum_{m\ge0}
\frac{(-1)^m(2m-1)!!}{m!}\xi^m
=(1+2\xi)^{-1/2}.                                                  \tag{20}
\]

Therefore, for \(z>0\),

\[
F(z)=\frac1z\int_0^\infty
e^{-\xi/z}(1+2\xi)^{-1/2}\,d\xi.                                 \tag{21}
\]

Equivalently,

\[
F(t)=
\sqrt{\frac{\pi}{2t^2}}e^{1/(2t^2)}
\operatorname{erfc}\!\left(\frac1{\sqrt2\,t}\right).              \tag{22}
\]

In the variable \(t\), the order-two Borel transform is

\[
\widehat F_2(\xi)=(1+2\xi^2)^{-1/2},                              \tag{23}
\]

whose singularities lie at \(\pm i/\sqrt2\). Positive-direction summation is
unobstructed. This success comes from the exact Stieltjes sign and sector
structure, not merely from the Gevrey coefficient estimate.

## 6. Calibration at depths one and two

At depth one,

\[
u'=Aq(u),\qquad A'=\phi(u),\qquad q=\phi'.
\]

Bounded activation gives

\[
\|A(t)\|_p+\|u(t)\|_p\lesssim_T1+\sqrt p.                          \tag{24}
\]

At initialization,

\[
D_A(Aq(u))=q(u),\qquad D_u(Aq(u))=Aq'(u),
\]

so the first response incurs a half-Gaussian loss. This matches the exact
worst coefficient growth

\[
\|f^{(k)}(0)\|\ \text{of order}\ C^k(k!)^{3/2}.                   \tag{25}
\]

But a bare positive-time tangent estimate gives only

\[
|P(t)|+|Q(t)|\le C_Te^{C_T|A_0|},
\]

whose \(L^p\) norm grows exponentially in \(p\). Recovering polynomial
response tails requires trajectory structure beyond the scale calculus,
already at the first rung.

At depth two, with

\[
z_2=\Gamma_1x_1,\qquad b_2=Aq(z_2),\qquad
r_1=\Gamma_1^Tb_2,
\]

one has

\[
D_{\xi_{ij}}z_{2,a}
=n^{-1/2}\mathbf1_{\{a=i\}}x_{1,j},
\]

and exactly

\[
\left(\sum_{ij}\|D_{\xi_{ij}}z_2\|_n^2\right)^{1/2}
=\|x_1\|_n.                                                       \tag{26}
\]

The transpose response is

\[
D_{\xi_{ij}}r_{1,a}
=n^{-1/2}\mathbf1_{\{a=j\}}b_{2,i}
+n^{-1/2}\Gamma_{1,ia}A_iq'(z_{2,i})x_{1,j}.                     \tag{27}
\]

The first tensor in (27) has squared response norm \(\|b_2\|_n^2\).
The second has squared norm

\[
\|x_1\|_n^2\left[
\frac1n\sum_iA_i^2q'(z_{2,i})^2
\sum_a\Gamma_{1,ia}^2
\right],                                                          \tag{28}
\]

which has dimension-independent fixed-\(p\) bounds at initialization.
Equations (26)--(28) recover a nontrivial MFP forward/transpose response by
the scale rules alone.

The learned term is

\[
K_1(t)^Tb_2(t)
=\int_0^t x_1(s)
\langle b_2(s),b_2(t)\rangle_n\,ds.                               \tag{29}
\]

Its two factors give formal Gaussian grade two. The scale records it, but
neither compact-time stability nor Borel summability follows.

## 7. Depth-three grade explosion

Let \(Q_l\) denote the worst uncapped Gaussian grade of \(b_l\).
The terminal field has \(Q_D=1\). The direct source term at the next layer
adds one grade, while the learned term analogous to (29) doubles it.
Consequently the safe restart-stable recursion is

\[
Q_D=1,\qquad Q_l=2Q_{l+1},                                       \tag{30}
\]

so

\[
Q_1=2^{D-1}.
\]

The corresponding safe time-derivative order is

\[
s_D=1+\frac{Q_1}{2}=1+2^{D-2}.                                   \tag{31}
\]

Thus the formal upper orders are

\[
D=1:\ (k!)^{3/2},\qquad
D=2:\ (k!)^2,\qquad
D=3:\ (k!)^3.                                                     \tag{32}
\]

Only the depth-one saturation is established. Equations (30)--(32) are
worst-case scale bookkeeping, not lower bounds on the true flow. Improving
them requires a large-width occupation/concentration cap.

At depth three, \(b_2\) has the safe moment scale \(O(p)\), and the learned
term contains

\[
\langle b_2(s),b_2(t)\rangle_n.
\]

Naive Hölder gives \(O(p^2)\). Showing that the normalized average restores a
smaller grade is exactly a reachable two-time occupation theorem. At finite
width and derivative order far above \(n\), collision terms prevent assuming
such averaging uniformly.

For the depth-three safe value \(s=3\), (15) has
\(\alpha=s-1=2\). Ordinary Watson uniqueness would require a time sector of
opening greater than \(2\pi\), unavailable on the ordinary punctured time
plane. Ramified or accelerated summation would be a new major structure, not
a standard consequence of peeling.

## 8. Width convergence and one-time restart

If \(a_{n,k}\to a_k\) for every fixed \(k\), MFP gives only a formal limiting
series. Commutation of width limit and Borel reconstruction would require:

1. a uniform version of (15);
2. one common continuation sector for every \(\widehat f_n\);
3. uniform growth (17);
4. local uniform convergence throughout that sector;
5. proof that each real finite-width observable equals the corresponding
   Borel sum.

Only then could dominated convergence be applied to (18).

At finite width an exact one-time state is

\[
\mathscr S_n(t)
=\big[\Xi_n;u_t,A_t,K_{1,t},\ldots,K_{D-1,t}\big],
\qquad G_{l,t}=\Gamma_l+K_{l,t}.                                  \tag{33}
\]

It is autonomous, with \(K_l'=n^{-1}b_{l+1}x_l^T\). An acceptable limiting
state would be a completion of finite source-response programs with a
computable finite-program approximation modulus. If its vector field
generated a semigroup, it would be genuinely restartable.

The formal truncation algorithm is clear: compute response coefficients,
peel each finite program, form the generalized Borel transform, continue it,
and Laplace-integrate. What is missing is every quantitative step that makes
this algorithm effective and identifies it with the real flow.

## 9. Claim-level conclusion

- **Established:** tame Hölder/projective rules, arctangent response cap,
  exact source identity (11), toy summation (19)--(23), depth-two response
  tensors (26)--(28), and the loss-only counterexample (13)--(14).
- **Conditional bookkeeping:** the worst grade recursion (30)--(32) and a
  finite response-program Borel algorithm.
- **Falsified:** automatic evolution from a loss exponent greater than one,
  identification from real Gevrey remainders, and automatic Borel completion
  of coefficientwise MFP limits.
- **Open:** positive-time jet membership, a depth-three occupation cap,
  common sectorial continuation, uniform Borel growth, real-flow
  identification, and a finite-program truncation modulus.

Those open leaves include the original tangent/occupation problem and add
strong complex-time obligations. The Banach scale is therefore useful
syntax, but not a viable shortcut to the compact-time limit.
