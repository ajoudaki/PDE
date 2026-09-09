# Audit of the explicit width-first fifth-order bound

## Canonical target

At each fixed step size first define

$$
F_k(h)=\lim_{n\to\infty}F_{k,n}(h),
$$

and only afterward study $h\to0$.  The target is to construct, solely from a
stated weighted activation envelope and Gaussian activation integrals,
numbers

$$
B_\phi<\infty,
\qquad
h_\phi>0,
$$

such that

$$
|F_2(\eta/2)-F_1(\eta)-\kappa_\phi\eta^3|
\le B_\phi|\eta|^5
$$

for every $|\eta|\le h_\phi$.

## Present status: open

Two independent obligations are incomplete.

### 1. Fixed-step network identification

The exact Gaussian conditioning identities and the reused-row and
reused-column response cancellations have been derived.  The remaining
probability theorem has only an induction blueprint.  A complete proof still
has to:

1. define a stopped stage-indexed coupling for every alternating row and
   column query;
2. construct the fresh innovations jointly, preserving every previously
   prescribed cross-covariance;
3. augment the coupled state by all tangent fields whose empirical averages
   define $\rho$ and $\sigma$;
4. prove the good-event induction without using Gram inverse moments;
5. prove uniform raw high moments for the original, unstopped network and use
   them to remove the bad event; and
6. prove uniform integrability of the terminal annealed output.

The exact regression algebra makes this program plausible under bounded
derivatives and at most linear growth, but plausibility is not pointwise
identification.

### 2. Explicit operator majorants

Under a safe weighted $C^{12}$ envelope, singular-covariance Price calculus
proves that the Gaussian operator outputs are $C^5$.  Taylor's integral
identity then gives

$$
\Delta(\eta)-\kappa_\phi\eta^3
=
\frac1{24}\int_0^\eta
(\eta-t)^4\Delta^{(5)}(t)\,dt.
$$

If explicit activation-only bounds

$$
|\mathsf F_1^{(5)}(t)|\le \overline J_{1,5},
\qquad
|\mathsf F_2^{(5)}(t)|\le \overline J_{2,5}
$$

were proved on the required intervals, then

$$
B_\phi
=
\frac1{120}
\left(
\overline J_{1,5}+\frac{\overline J_{2,5}}{32}
\right)
$$

would be admissible.  The current note has not proved these two numbers.  Its
symbols

$$
c_j=\sup_h\|C^{(j)}(h)\|_1
$$

and $a_{j,s}$ are still unknown covariance-trajectory suprema and unspecified
mixed integrand envelopes.  A complete construction must attach explicit
coefficient-degree pairs $(A_{j,s},P_{j,s})$ to every reachable mixed
derivative, propagate them through every Leibniz and Bell-polynomial rule,
and replace each new covariance bound by the sum of the already computed
Price majorants of its entries.

An explicit small rank radius also requires activation-defined fourth-jet
majorants for every Gram determinant used by the cavity proof.  For example,
if

$$
\det Q(h)=deh^2+R_Q(h),
\qquad
|R_Q(h)|\le \frac{D_Q}{24}|h|^4,
$$

then

$$
|h|\le\sqrt{\frac{12de}{D_Q}}
$$

implies $\det Q(h)\ge deh^2/2$.  The analogous cotangent condition uses
$d\tau$ and an explicit $D_K$.  The existing determinant asymptotics do not
supply $D_Q,D_K$.

## Formal consequence once both obligations are proved

The fifth-order estimate would imply

$$
|\Delta(\eta)|
\le
\left(|\kappa_\phi|+B_\phi\eta^2\right)|\eta|^3.
$$

For

$$
|\eta|
\le
\min\left\{
h_\phi,
\sqrt{\frac{\varepsilon}{1+B_\phi}}
\right\},
$$

one has

$$
B_\phi\eta^2
\le
\frac{B_\phi}{1+B_\phi}\varepsilon
\le\varepsilon,
$$

and hence

$$
|\Delta(\eta)|
\le
(|\kappa_\phi|+\varepsilon)|\eta|^3.
$$

This implication is exact.  Its two premises are the open parts above.

