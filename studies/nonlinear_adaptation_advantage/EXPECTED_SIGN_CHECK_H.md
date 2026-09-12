# Internal check of the expected-sign attempt

Author: /root/harmonic_route, 2026-09-12.

**Scoped verdict: PASS. No required correction found.** The exchange-sector
identities hold for the specified canonical named-source program, including
singular source covariances. The complete-history Gaussian integration by
parts has the correct normalization, and the endpoint limit uses only the
invariant mixed moment. The finite-time memory counterexample, its rational
sign certificate, and the smoothing argument are valid.

The counterexample defeats the stated inference from positive source
covariance and inhibitory nonnegative memory. It is not an actual-neural
counterexample. Neither actual fitted-endpoint covariance sign nor any E₀
advantage has been established. This is an internal check, not a promotion
review.

## 1. Complete read scope and hashes

Read EXPECTED_SIGN_ATTEMPT.md completely, lines 1–305, including all
equations, proofs, limitations and provenance. Its verified SHA-256 is

    c88d6eab7be97171e1fd36ff0cf17ce7573d90744a2e645205f35dca6d1a048d

Its stated study dependencies were already completely read and remain at
their frozen hashes:

| Dependency | Complete coverage | SHA-256 |
|---|---|---|
| ROUTE_GAUSSIAN_SIGN.md | Lines 1–484 | 2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c |
| GAUSSIAN_SIGN_TRANSPORT.md | Lines 1–602 | 5f44ec005410cbdfa4557580c243ea77c1abce6a067882a722d2552578cb484c |

Established dependencies already completely read within the assigned scope
include global_nonlinear.md A.1–A.4, C.4.5.1 §§1–3 and its initialization
certificate, C.4.5.2 §§1–4, the relevant strong reference/selected equations,
and special_data_limits.md III.F in full. This check additionally reread
global_nonlinear.md lines 6190–6290 and special_data_limits.md lines
3945–3972 and 4052–4070. These verify the formal source convention,
same-batch query order, bounded source derivatives, and singular-support
qualification used below.

Relevant retained established/process hashes:

| Source | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

The required solve-math-rigorously and investigate-conjectures skills
remain applied from their complete prior reads. No other study, current
review, experiment, numerical integration, training, or Git operation
supplied an input. The assigned input was preserved.

## 2. Canonical named coefficients at singular covariance

The positive-label representation has identical coordinate instructions for
the two anchors and common controls $h_r/2$. It follows from
$v_2=-w_2$ and tanh oddness without changing the reference. Equation (E2)
retains both the actual response coefficient and the learned-rank coefficient
with the correct factor $h_r/2$.

For completeness, the coefficient-block symmetry requires a formal-program
argument, not only equality in law of output values. Let $\bar a=3-a$ and
let $\mathscr S$ swap the two initial row roots and every pair
$\xi_{ra},\zeta_{ra}$ of named sources. Induct over complete mesh stages.
Assume all earlier selected coefficient blocks commute with this swap.
The unrolled scalar expressions then satisfy

$$
H_{ka}^1(\mathscr S\omega)=H_{k\bar a}^1(\omega),\qquad
\delta_{ka}(\mathscr S\omega)=\delta_{k\bar a}(\omega).
\tag{H1}
$$

The readout expression is invariant. Within a stage, both forward inputs
are determined before either forward answer is used to update the state;
both reverse inputs are determined before either reverse answer is used
to update it. The swap therefore preserves the canonical expressions despite
the sequential notation for same-batch calls.

Differentiate (H1) as an identity in all formal arguments:

$$
(\partial_{\zeta_{rb}}H_{ka}^1)(\mathscr S\omega)
=\partial_{\zeta_{r\bar b}}H_{k\bar a}^1(\omega),
\tag{H2}
$$

and likewise for reverse-response derivatives with respect to $\xi$.
The prefix Gaussian law is swap-invariant because its covariance Grams are,
and the root law is exchange-invariant. Taking expectations in (H2) and
in the learned Gram term gives
$a_{ka,rb}=a_{k\bar a,r\bar b}$; the reverse block obeys the same rule.
This closes the induction from the symmetric initialization.

The argument differentiates the named expressions before imposing the
Gaussian support. It therefore includes variance-zero or linearly dependent
slots. No inverse, eigenvalue gap, or rank stability is required. Arbitrary
off-support rewritings of a singular Gaussian expression need not retain
individual coefficient symmetry; the claim here is correctly about the
canonical expressions in (E2) and C.4.5.2.

The two-by-two blocks consequently diagonalize under the orthogonal
sum/contrast change of coordinates. Expanding
$\mathbb E[H_{k+}^1H_{r-}^1]$ gives zero because the two diagonal terms
and the two cross terms respectively match. The source covariance rule
then proves (E3), and joint Gaussianity makes the entire finite forward
$+$ and $-$ source histories independent, even when either block is
singular. A positive semidefinite time Gram does not imply positive
individual off-diagonal entries. The input preserves that distinction.

Equations (E4)–(E5) have the correct normalization. In particular the
nonlinear readout and gate formulas still couple the two sectors; source
independence is not independence of trained fields.

## 3. Complete-history integration by parts and passage to the endpoint

The normalization is

$$
\beta_\pm^{\rm mesh}
=v_0^{-1}\mathbb E[\xi_{0\pm}\delta_{k\pm}],
\qquad \operatorname{Var}\xi_{0\pm}=v_0.
$$

The two factors of $\sqrt2$ in the sector variables cancel the factor two
in (E1). For a finite possibly singular Gaussian vector $\Xi$ with
covariance $C$, the contained integration-by-parts identity is
$\mathbb E[\Xi_iF]=\sum_jC_{ij}\mathbb E[\partial_jF]$.
Representing $\Xi=C^{1/2}G$ proves it without inverting $C$.
The fixed reference graph has integrable, indeed bounded first source
derivatives after the stated clipping argument and its removal.

Apply this identity to the complete forward history in the chosen sector,
conditioning on the independent other sector. One obtains exactly

$$
\beta_\pm^{\rm mesh}
=\frac1{v_0}\sum_{r\le k}C_\pm(0,r)
          \mathbb E[\partial_{\xi_{r\pm}}\delta_{k\pm}].
\tag{H3}
$$

The sum includes all historical and current named slots. The selected
coefficients and covariances are deterministic and held fixed; this is a
coordinate derivative of a fixed Gaussian program, not a derivative of its
law with respect to a task parameter.

For (E7), subtract the linear projection of the full same-sector Gaussian
vector onto $\xi_{0\pm}$. The remainder vector is jointly Gaussian and
uncorrelated with that scalar, hence independent of it. Its coordinates need
not be mutually independent. The total derivative at fixed remainder and
opposite sector is

$$
\frac{d\delta_{k\pm}}{d\xi_{0\pm}}
=\sum_{r\le k}\frac{C_\pm(0,r)}{v_0}
                    \partial_{\xi_{r\pm}}\delta_{k\pm}.
\tag{H4}
$$

Ordinary scalar Gaussian integration by parts makes its expected value
equal to $\beta_\pm^{\rm mesh}$, consistently with (H3).
Holding every later same-sector source numerically fixed does not implement
this direction of change.

At singular support, a permitted change of expression can change individual
expected derivatives by a covariance-null vector. Its contraction with the
row $C_\pm(0,\cdot)$ is zero. Thus (H3) is invariant even though arbitrary
individual named coefficients need not be.

For meshes ending at the deterministic $s_\dagger$, the established common
strong completion gives $\delta_{k\pm}^{\rm mesh}\to\delta_\pm(s_\dagger)$
in $L^2$. The same fixed $\xi_{0\pm}\in L^2$ is retained. Cauchy–Schwarz
therefore passes the left side of (H3) to the actual endpoint moment,
proving (E8). This does not pass individual derivatives, interchange a
derivative with a growing transcript, or assert a continuous response kernel.

The parity caveat is also correct. Exchange flips the complete contrast
history; simultaneous sign reversal of both histories uses tanh oddness.
Their composition flips the complete sum history. In a representation
$\xi_r=a_r\xi_0+\eta_r$, either relevant full-sector parity operation flips
the same-sector remainder as well as $\xi_0$. It need not give oddness or
monotonicity under changing $\xi_0$ alone with that remainder held fixed.

## 4. Finite memory counterexample and rational sign certificate

The constant Gaussian history has covariance $v_0$ in every entry. It is
positive semidefinite, entrywise positive, and singular; no extra independent
source is introduced. The nonnegative kernel in (E9) gives

$$
d(t)=Z-10\int_0^{(t-1)_+}\tanh d(r)\,dr.
$$

The method of steps uniquely gives $d(t)=Z$ through time one and
$d(t)=Z-10(t-1)\tanh Z$ through time two. This proves (E10).
The response remains bounded, odd, decreasing in the current $d$, and
pointwise inhibitory, $d\delta\le0$.

For $x>0$ let $\chi(x)=\tanh x-x\operatorname{sech}^2x$.
Then $\chi(0)=0$ and
$\chi'(x)=2x\tanh x\operatorname{sech}^2x>0$, so
$\tanh x/x$ decreases. Since $\tanh3>3/4$, for $0<x\le3$

$$
x-10\tanh x<-3x/2.
$$

Thus $g(x)=-x\tanh(x-10\tanh x)$ is nonnegative on $[-3,3]$ and
exceeds $1/4$ when $1/2\le|x|\le1$. The latter uses
$\tanh(3/4)>1/2$. These two elementary tanh bounds follow respectively
from $e^6>7$ and $e^{3/2}>3$, using positive partial exponential sums.

For $1/2\le x\le1$ and $0.39<v_0<0.4$, the Gaussian density exceeds
$1/8$: its prefactor exceeds $1/2$, and
$x^2/(2v_0)<13/10$ with $e^{13/10}<4$.
One explicit rational verification of the last inequality is

$$
e^{13/10}
\le\left(1+\frac{13}{10}+\frac{(13/10)^2}{2}
                    +\frac{(13/10)^3}{6}\right)
 +\frac{(13/10)^4/24}{1-13/50}<4.
\tag{H5}
$$

After the fourth term, each successive ratio is at most $13/50$.
The two intervals together have total length one, giving probability
strictly greater than $1/8$.

The negative contribution outside $[-3,3]$ has absolute value at most

$$
\mathbb E[|Z|\mathbf1_{\{|Z|>3\}}]
=\sqrt{2v_0/\pi}\,e^{-9/(2v_0)}
<e^{-45/4}<1/64.
\tag{H6}
$$

For the last comparison even the degree-two positive partial sum suffices:
$1+45/4+(45/4)^2/2=2417/32>64$.
Combining the positive interval contribution with (H6) proves
$\mathbb E[Z\delta(2)]>1/32-1/64=1/64$.
Initially it is $-\mathbb E[Z\tanh Z]<0$. Thus (E11) is a strict
finite-time reversal of this model's expected initial-source sign.

## 5. Smooth memory and scope of the counterexample

Choose a smooth nondecreasing $\vartheta$ with values in $[0,1]$,
equal to zero on $(-\infty,0]$ and one on $[1,\infty)$, and set

$$
K_\epsilon(t,r)=10\vartheta((t-r-1)/\epsilon).
$$

This is a concrete smoothing of the specified type. It preserves
nonnegativity and the bound ten, and its time-row $L^1$ difference from
$K$ is at most $10\epsilon$. A standard smooth transition can be constructed
from $\exp(-1/x)$ on $x>0$, extended by zero. It is identically zero for
$t\le1$, so the initial negative covariance is also retained.

Subtracting the integral equations and using $|\delta|\le1$ and the
one-Lipschitz tanh gives

$$
|d_\epsilon(t)-d(t)|
\le10\epsilon+10\int_0^t|d_\epsilon(r)-d(r)|\,dr.
$$

Iteration or Gronwall gives the stated uniform bound
$10\epsilon e^{20}$ on $[0,2]$. The same Volterra estimate supplies
uniqueness, and Picard iteration supplies the continuous solution.
The expected covariance difference is at most
$10\epsilon e^{20}\mathbb E|Z|$.
For example, since $\mathbb E|Z|<1$, taking
$0<\epsilon<e^{-20}/1280$ preserves a terminal lower bound greater than
$1/128$. No numerical integration is needed.

The example therefore genuinely retains the advertised positivity,
oddness, inhibition, and smooth nonnegative causal memory while reversing
its expected initial-source sign. It says nothing about reachability of
these coefficients by the actual tanh reference. It invalidates the
proposed comparison principle from those properties alone.

## 6. Final scoped assessment

| Claim | Verdict |
|---|---|
| Canonical coefficient-block symmetry, including singular covariance | PASS; requires the formal-program argument in §2 |
| Independent Gaussian exchange sectors and nonlinear coupling retained | PASS |
| Full-history integration by parts and coefficient normalization | PASS |
| Endpoint passage of the full invariant contraction only | PASS |
| Finite-time memory counterexample and rational sign margin | PASS |
| Smooth nonnegative-kernel version | PASS |
| Actual endpoint covariance sign or E₀ comparison | Not established and not claimed |

No correction is required. The important qualification is already part of
the named-source setup: symmetry of canonical coefficients is not inferred
merely from values on a singular Gaussian support. The full endpoint sign
remains a signed contraction of the actual entire source history.
