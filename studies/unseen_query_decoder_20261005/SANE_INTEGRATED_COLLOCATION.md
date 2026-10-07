# Order-independent integrated interpolation and a shorter causal source

2026-10-06. Lead-author bounded improvement in the current unseen-query
efficiency search. This is a source-solver lemma, not a complete small-exponent
decoder theorem. It retains the supplied dense fitting/analytic events and
the exact-real computational convention. No experiment or promotion is claimed.

## 1. The improvement

The existing collocation solver bounds interpolation before integrating it.
The integrated operator itself has a universal bound, independent of its
degree. Consequently the step size need not contain either the interpolation
degree or its logarithm. This changes the parameter-explicit matrix-call bound
from the previous loose logarithmic power six to power nine-halves, with
the same cubic inverse-normalized-gap factor. It does not compress these
matrix calls into a compact state by itself.

## 2. Exact integral-operator bound

Let K>=2 and let the nodes on [0,1] be

\[
 s_j=(1+\cos((j+1/2)\pi/K))/2,\qquad 0\le j<K.
\]

Write I_K for polynomial interpolation of degree below K. For values b_j
in any finite-dimensional normed real or complex vector space,

\[
 \sup_{0\le s\le1}\left\|\int_0^s I_Kb(u)\,du\right\|
 \le\frac{\pi}{2\sqrt2}\max_j\|b_j\|
 <2\max_j\|b_j\|.                                      \tag{1}
\]

Here is a proof without an interpolation-norm theorem. For scalar data,
put p=I_Kb and w(u)=1/(pi sqrt(u(1-u))). Discrete cosine orthogonality,
or expansion of the degree-(2K-2) polynomial |p|^2 into cosines, gives

\[
 \int_0^1 |p(u)|^2w(u)\,du=K^{-1}\sum_{j=0}^{K-1}|b_j|^2.
\]

For complex coefficients |p(u)|^2 is still a polynomial in the real
variable u of degree at most 2K-2. The cosine rule is exact because
K^{-1}sum_j cos(k(j+1/2)pi/K)=0 for 1<=k<2K. Cauchy--Schwarz gives

\[
 \left|\int_0^s p(u)du\right|
 \le\left(\int_0^1|p|^2w\right)^{1/2}
      \left(\int_0^s w^{-1}\right)^{1/2}
 \le\frac{\pi}{2\sqrt2}\max_j|b_j|,
\]

since integral_0^1 sqrt(u(1-u))du=pi/8. Apply this scalar inequality
to every norm-one dual functional of the vector integral. The dual
description of the finite-dimensional norm proves (1). No Hilbert norm
or dimension-dependent constant is required.

Suppose a vector-valued function g has a degree-below-K polynomial p
with sup_[0,1]||g-p||<=e. Exactness of interpolation on p and (1) imply

\[
 \sup_s\left\|\int_0^s(g-I_Kg)du\right\|\le3e.          \tag{2}
\]

On a physical interval of length h, both right sides acquire a factor h.
If g is holomorphic and bounded by M in a disk of radius 2h about the
interval midpoint, Taylor truncation gives e<2M 2^{-K}; hence the
integrated defect is at most 6Mh2^{-K}. Only the true trajectory's
time function is continued holomorphically, not a clipped numerical field.

## 3. Fully specified causal collocation scheme

Assume the same finite-dimensional autonomous extension as the existing
short-program proof: u'=F(u), ||F||<=M, Lip(F)<=Lambda, with Lambda>=1.
The actual trajectory derivative extends to disks of radius r about its
real anchors with bound M. Its prediction map has Lipschitz bound B>=1
in the displacement norm, uniformly over real sphere inputs. These are
supplied numerical/source interfaces, not assumptions newly asserted for
arbitrary differential equations.

For a finite horizon T>0, choose the ordinary step and shorten only the
last interval:

\[
 h=\min\{r/4,1/(8\Lambda)\}.
                                                               \tag{3}
\]

At a patch beginning at t_0 with numerical initial value b, iterate

\[
 U_j^{(0)}=b,\qquad
 U_j^{(k+1)}=b+\int_{t_0}^{t_0+hs_j}
       I_K(F(U_0^{(k)}),\ldots,F(U_{K-1}^{(k)}))(s)\,ds.
                                                               \tag{4}
\]

The nodes/interpolation are affinely rescaled to the actual patch length.
Equation (1) gives contraction at most 2hLambda<=1/4, independent of K.
Choose J=K iterations, and construct the patch path and committed endpoint
from the integrated interpolant of F(U^(J)). All stages are finite causal
operations on the preceding stage; no implicit-solve oracle is assumed.

Let e be the error at the patch start and let V be the exact trajectory
at the nodes. Put eta=6M2^{-K}. The exact-node defect of (4) is bounded by
e+h eta. The fixed point U* therefore satisfies

\[
 \|U^*-V\|_{\max}\le2(e+h\eta).
\]

Since F is globally bounded, (1) gives ||U*-(b,...,b)||_max<=2hM.
The finite-iteration error is at most zeta=2hM4^{-J}.

The endpoint integral weights of Chebyshev-root interpolation are positive
and sum to one. Explicitly they are

\[
 \omega_j=\frac1K\left[1-2\sum_{k=1}^{\lfloor(K-1)/2\rfloor}
       \frac{\cos(2k(j+1/2)\pi/K)}{4k^2-1}\right].
\]

Positivity follows from sum_{k=1}^a 2/(4k^2-1)=1-1/(2a+1)<1;
the constant polynomial gives their sum. Subtracting the exact endpoint
and using these weights, followed by (2), yields

\[
 e_{\rm next}\le(1+2h\Lambda)e
     +h\eta(1+2h\Lambda)+h\Lambda\zeta
 \le(1+2h\Lambda)e+8Mh2^{-K}.                           \tag{5}
\]

Here hLambda<=1/8 and J=K were used. Iterating from exact initial state
gives endpoint error at most 8MT exp(2Lambda T)2^{-K}. At an interior
time use (1) instead of the endpoint positive weights. The resulting
bound is

\[
 \sup_{0\le t\le T}\|u(t)-\widetilde u(t)\|
 \le32M(T+1)e^{2\Lambda T}2^{-K}.                       \tag{6}
\]

For example h<=1/8, and direct subtraction bounds each interior error
by (1+4hLambda)e+(1+4hLambda)h eta+2hLambda zeta, which is below
the displayed envelope after (5). The actual patch length is used in
all these inequalities, including the final shortened patch.

For prediction accuracy epsilon on [0,T], it suffices to take K to be
the least power of two not below

\[
 \max\left\{2,
 \frac{2\Lambda T+
       \log(1+128BM(T+1)/\varepsilon)}{\log2}\right\}.
                                                               \tag{7}
\]

This pays for the conditioning product explicitly instead of moving it
into a sufficient-width threshold. The power-of-two choice only aids
the already available trigonometric-node construction; it costs at most
a factor two. The fitting tail and freezing after T are exactly those
of the existing numerical source, not an assertion of exact fitting by
this finite numerical program.

## 4. Explicit substitution into the original neural source

Use the unchanged definitions n,m,d,L,gamma,Y,beta of COST_CONTRACT.md,
with Y>0, and fixed requested normalized accuracy exponent a_0=10.
For this paragraph define the local source parameters

\[
 \ell=\log(en),\quad B=\beta^{100L},\quad r=m/\gamma,
 \quad Z=(a_0+1)\ell+\log(e+B(1+r)).
\]

The normalized clock is tau=(gamma/m)t and displacement is divided by Y.
PHYSICAL_PARAMETER_ACCOUNTING.md supplies, on its inherited event,

\[
 M\le B(1+r),\quad \Lambda\le B(1+r)\sqrt\ell,
 \quad r_\tau^{-1}\le B\sqrt\ell,
\]

with observation sensitivity at most B. Choose the physical-source
normalized horizon no larger than
T=2[a_0 log n+log(1+66Br)]; this upper choice still covers the inherited
tail, since its H^2<=B. Then T<=C Z. In (3) use r_tau for the radius
(distinct from r=m/gamma); in (7) use epsilon=n^{-a_0}/2. The rounded
positive constants are universal. Both the number of patches and K=J
are at most

\[
 C\beta^{100L}(1+m/\gamma)Z\sqrt\ell.
\]

Every field evaluation uses O(mL) initialized matrix calls and produces
that many principal vector fields. Count the final evaluation used to
define the patch path as well. The initialized first-layer roots add d.
The resulting total is bounded by

\[
 C\left[d+
 mL\beta^{300L}(1+m/\gamma)^3Z^3\ell^{3/2}\right]
 \le C\left[d+
 mL\beta^{300L}(1+m/\gamma)^3Z^{9/2}\right].           \tag{8}
\]

This replaces the old sufficient Z^6 bound for this source schedule.
It does not change the full label allowance or require bounded activation
values. The dependence on beta is explicit and polynomial in beta^L.
There is no inverse-label factor inside (8); raw-label input costs and
the inherited stochastic and deterministic width conditions still apply.

## 5. Cost and interface boundaries

Let N_F=HK(J+1) for the patch/degree/iteration counts just specified.
The direct dense implementation requires at most

\[
 C N_F(Ln^2+dn)(m+K)
\]

exact-real arithmetic operations. It uses the linear-scratch cosine /
antiderivative schedule in COST_INTERFACE_PANEL.md, not a cached K-by-K
integration matrix. Its live dense stage storage is
O((Ln^2+dn)K), before any output coefficient arrays or bit precision.
These are source-generation costs, not the costs of the desired compact
decoder. A fast transform is unnecessary for (8) or for this bound.

The new node operator has smaller norm than the previous proved bound,
and endpoint weights, finite causal chronology, and displacement norm
identities are unchanged. Nonetheless the full noisy-row compiler,
source-selection precision and uniform query proof must be checked
against this revised chronology before replacing the final resource
table. In particular, squaring (8) to store every history pair is already
far from a log^5 memory theorem. A reduction of source calls alone is
not a proof of cheap late queries or a bit-cost theorem.

## 6. Inputs and check status

Read completely: SHORT_CAUSAL_TRAINING_PROGRAM.md and its complete CHECK;
PHYSICAL_PARAMETER_ACCOUNTING.md; COST_CONTRACT.md; the study README;
maintained docs/index.qmd and docs/notation.qmd. The prior-turn full
read of COST_INTERFACE_PANEL.md is the scheduling interface; the scalar
schedule needed above is also reproduced in PHYSICAL_PARAMETER_ACCOUNTING
Section 6. No outside research study beyond the already authorized source
interfaces was imported. Required rigorous-math and conjecture-research
skills were used; the custom notation skill remains permission-inaccessible.

The lead checked scalar quadrature exactness, Banach dualization, the
contraction and endpoint recurrences, shortened final steps, parameter
substitution, and the separation between source calls and compact
information. The result is an author-derived candidate pending separate
reconstruction. No numerical experiment or finite-bit claim is made.
