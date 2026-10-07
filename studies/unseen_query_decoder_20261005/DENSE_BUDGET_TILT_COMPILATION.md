# Constructive acquisition of a calibrated row tilt

2026-10-06. Bounded author derivation. No experiment, Git operation,
promotion, or complete neural-decoder claim.

A calibrated exponential row law and its log normalizer can be acquired
constructively with absolute-polylogarithmic workspace and retained bits,
allowing arbitrary acquisition time. The algorithm enumerates a finite
multiplier grid and checks certified moment and entropy estimates using
streaming quadrature in the log domain. A two-pass maximum-and-sum
procedure avoids exponentiating huge log weights.

A rounded current prefix is handled by applying the feasibility argument
again with an enlarged moment box. No continuity of the optimizing
multiplier is assumed. The resulting law has relative entropy at most
\(2h\) and moment error at most \(4\eta T\) under the original all-prefix
information/noise event and the stated rounding tolerance.

## 1. Fixed-prefix compilation statement

Let \(\mu=N(0,I_D)\) be the row prior, and let
\(F=(F_1,\ldots,F_P):\mathbb R^D\to\mathbb R^P\) be the current
fixed-prefix row circuit. Assume

\[
 |F_r(z)|\le B,\qquad
 |F_r(z)-F_r(z')|\le L_F\|z-z'\|_\infty,\qquad B,L_F\ge1.
 \tag{1}
\]

For the current observed moments \(c\in\mathbb R^P\), suppose there
exists a proof-only probability law \(\nu_0\) satisfying

\[
 D(\nu_0\Vert\mu)\le h,\qquad
 \left|\int F_r\,d\nu_0-c_r\right|\le a
                   \quad(1\le r\le P),                    \tag{2}
\]

where \(h>0\), \(a\ge0\). Fix a strict-slack allowance \(s>0\).
Define

\[
 \psi(\lambda)=\log\int e^{\lambda^TF(z)}\,\mu(dz),\qquad
 d\nu_\lambda=e^{\lambda^TF-\psi(\lambda)}\,d\mu.
 \tag{3}
\]

The compiler returns a dyadic vector \(\widehat\lambda\) and, for any
requested \(\tau>0\), a dyadic \(\widehat\psi\) satisfying

\[
 D(\nu_{\widehat\lambda}\Vert\mu)<2h,\qquad
 \left|\int F_r\,d\nu_{\widehat\lambda}-c_r\right|
                  <a+\tfrac32s,\qquad
 |\widehat\psi-\psi(\widehat\lambda)|\le\tau.                \tag{4}
\]

The first two inequalities concern the exact law at the returned
multiplier. Its cached-normalizer error has the separate controlled
effect proved in DENSE_BUDGET_CONDITIONING.md, Section 4.

For the finite-bit construction, take \(c,a,h,s,B,L_F\) as supplied
rational data or conservative rational certificates; Section 5 handles
the replacement of an ideal prefix by its finite representation. The
row evaluator has the inherited counted precision interface. Workspace
and retained bits are polynomial of absolute
degree in the circuit description, its counted precision workspace,
the bits of \(c,a\), and

\[
 D+P+\log(1+B)+\log(1+L_F)
 +|\log h|+|\log s|+\log(1+1/\tau).                         \tag{5}
\]

For the source application, these quantities are absolute-polylogarithmic
in \(n\). This is a parameterwise construction from supplied certificates,
not a uniform compiler for arbitrary raw activation code. The acquisition
runtime is unrestricted.

If \(h=0\), (2) forces \(\nu_0=\mu\), so the zero multiplier and zero
normalizer work without search. Indeed \(r\log r-r+1\) is nonnegative
and vanishes only at \(r=1\); its integral is relative entropy.
An empty moment vector is handled by the same zero multiplier.

## 2. Strict slack gives a bounded exact multiplier

The existence proof in EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md applies
with tolerance \(a+s\). Set

\[
 J(\lambda)=\lambda^Tc-(a+s)\|\lambda\|_1-\psi(\lambda).
 \tag{6}
\]

Comparing \(\nu_0\) with \(\nu_\lambda\) in relative entropy gives
\[
 \psi(\lambda)\ge\lambda^T\int F\,d\nu_0-D(\nu_0\Vert\mu),
 \qquad J(\lambda)\le h-s\|\lambda\|_1,\qquad J(0)=0.
 \tag{7}
\]
All integrals are finite because \(F\) is bounded. Thus the continuous
\(J\) attains a maximum at some \(\lambda_*\) with
\(\|\lambda_*\|_1\le h/s\). Differentiation of the bounded exponential
integrand gives \(\nabla\psi=\int F\,d\nu_\lambda\).
The coordinate directional derivatives at the maximum give a vector
\(v\), with \(|v_r|\le1\) and
\(v_r=\operatorname{sign}\lambda_{*,r}\) when that coordinate is
nonzero, such that

\[
 \int F\,d\nu_{\lambda_*}=c-(a+s)v,\qquad
 D(\nu_{\lambda_*}\Vert\mu)
 =\lambda_*^T\int F\,d\nu_{\lambda_*}-\psi(\lambda_*)
 =J(\lambda_*)\le h.                                      \tag{8}
\]

No moment-covariance rank, empirical Gram gap, or optimizer regularity
is required.

## 3. A finite grid contains a robustly acceptable tilt

Choose a rational \(\Lambda\ge\max\{1,h/s\}\) with
\(\Lambda\le2(1+h/s)\), using upward dyadic rounding. Put

\[
 \theta=\min\left\{\frac1{8B},\,\frac{s}{64B^2},\,
                  \frac{h}{16B(1+4B\Lambda)}\right\}.       \tag{9}
\]

Take a dyadic mesh \(\theta/(2P)<\Delta\le\theta/P\).
Enumerate all integer multiples of \(\Delta\) in the coordinate cube
of radius \(\Lambda\), discarding those with \(\ell^1\) norm above
\(\Lambda\). Rounding \(\lambda_*\) toward zero gives an enumerated
\(\lambda^\circ\) with
\[
 d:=\|\lambda^\circ-\lambda_*\|_1\le\theta,\qquad
 \|\lambda^\circ\|_1\le\Lambda.
\]
Boundedness of \(F\) implies
\[
 |\psi(\lambda^\circ)-\psi(\lambda_*)|\le Bd,\qquad
 \left|\log\frac{d\nu_{\lambda^\circ}}{d\nu_{\lambda_*}}\right|
                         \le2Bd.
 \tag{10}
\]
Since \(Bd\le1/8\), \(e^u-1\le2u\) for \(0\le u\le1/2\) gives
\[
 \left|\int F_r\,d\nu_{\lambda^\circ}
            -\int F_r\,d\nu_{\lambda_*}\right|
 \le2B(e^{2Bd}-1)\le8B^2d\le s/8.                          \tag{11}
\]
Subtract the entropy formulas
\(D(\nu_\lambda\Vert\mu)=\lambda^T\int F\,d\nu_\lambda-\psi(\lambda)\).
Using (10)–(11) gives
\[
 |D(\nu_{\lambda^\circ}\Vert\mu)-D(\nu_{\lambda_*}\Vert\mu)|
              \le(2B+8\Lambda B^2)d\le h/8.                \tag{12}
\]
Hence some grid point has moment error at most \(a+9s/8\) and entropy
at most \(9h/8\).

For each candidate, Section 4 computes moment estimates \(\widehat m_r\)
and a temporary normalizer estimate \(\widehat\psi_0\) with
\[
 |\widehat m_r-\int F_r\,d\nu_\lambda|
       \le\varepsilon_m:=\min\{s/16,h/[64(1+\Lambda)]\},
 \qquad|\widehat\psi_0-\psi(\lambda)|\le h/64.               \tag{13}
\]
Compute \(\widehat D=\lambda^T\widehat m-\widehat\psi_0\), allowing
additional arithmetic error \(h/64\). Then
\[
             |\widehat D-D(\nu_\lambda\Vert\mu)|
                      \le3h/64<h/16.                      \tag{14}
\]
Return the first grid point passing the finite tests
\[
 \max_r|\widehat m_r-c_r|\le a+5s/4,\qquad
                         \widehat D\le3h/2.               \tag{15}
\]
The point furnished by (11)–(12) passes: its computed errors are at
most \(a+19s/16<a+5s/4\) and \(9h/8+h/16<3h/2\).
Every accepted point satisfies (4), because adding (13)–(14) gives
moment error at most \(a+21s/16<a+3s/2\) and entropy below
\(3h/2+h/16<2h\). Thus the finite search terminates without exact
feasibility decisions. Refine the accepted log normalizer to the
separately requested accuracy \(\tau\).

The logarithm of the candidate count, and its loop counters, have size
\[
 O\!\left(P[1+\log(1+\Lambda)+\log P+\log(1/\theta)]\right).
 \tag{16}
\]
Only the current candidate is live; no candidate table is retained.

## 4. Log-domain quadrature with counted workspace

Fix \(\|\lambda\|_1\le\Lambda\), put \(K=\Lambda B\), and request
moment error \(\epsilon_m>0\) and log-normalizer error
\(\epsilon_\psi>0\), both at most one. Choose the largest dyadic power
of two satisfying
\[
 0<t\le\min\{1/16,\epsilon_m/(64B),\epsilon_\psi/64\}.        \tag{17}
\]

### Finite box and relative tail

Choose \(A\ge1\) with
\[
 A^2\ge4K+2\log(2D/t),\qquad \mathcal B=[-A,A]^D.           \tag{18}
\]
One may use the first integral power of two whose square exceeds a
certified upper bound on the right side. The Gaussian coordinate tail
bound and a union bound give
\[
 p:=\mu(\mathcal B^c)\le2D e^{-A^2/2}\le t e^{-2K}.
\]
Since \(e^{-K}\le e^{\lambda^TF}\le e^K\), its normalizer is at least
\(e^{-K}\); hence
\[
          q:=\nu_\lambda(\mathcal B^c)\le e^{2K}p\le t.
 \tag{19}
\]
Restricting and normalizing the tilted law on the box changes any
moment by at most \(2Bt\).

No Gaussian normalizing-constant oracle is necessary. Define
\[
 I_\lambda=\int_{\mathcal B}e^{\lambda^TF(z)-\|z\|^2/2}\,dz,
 \qquad I_0=\int_{\mathcal B}e^{-\|z\|^2/2}\,dz.
\]
Then
\[
 \log(I_\lambda/I_0)
 =\psi(\lambda)+\log(1-q)-\log(1-p),\qquad
 |\log(I_\lambda/I_0)-\psi(\lambda)|\le4t.                  \tag{20}
\]
This uses \(|\log(1-u)|\le2u\) for \(0\le u\le1/2\).

### A grid with short counters

Let
\[
 g_\lambda(z)=\lambda^TF(z)-\|z\|^2/2,\qquad
 g_0(z)=-\|z\|^2/2.
\]
Their Lipschitz constants in the maximum coordinate norm are at most
\(\Lambda L_F+DA\) and \(DA\). Partition each coordinate interval
into \(q_0\) equal subintervals of length \(\ell=2A/q_0\), choosing
the least positive integer \(q_0\) for which
\[
 \ell/2\le\frac{t}{16(1+DA+\Lambda L_F+L_F)}.                \tag{21}
\]
There are \(N=q_0^D\) midpoint nodes. Their coordinates are rational,
and
\[
 \log N\le CD[1+\log A+\log(1+DA+\Lambda L_F+L_F)+\log(1/t)].
 \tag{22}
\]
In particular the nodes and index counters have polynomial bit length
in (5), despite the possibly enormous number of nodes.

Within a cell, either log weight and each \(F_r\) vary by at most
\(t/16\) from their midpoint values. Each midpoint quadrature integral
therefore differs from the true box integral by a factor between
\(e^{-t/16}\) and \(e^{t/16}\). Its log ratio error is at most \(t/8\).
After normalization, the ratios between true cell masses and grid
weights lie between \(e^{-t/8}\) and \(e^{t/8}\). Their total variation
is at most \(e^{t/8}-1\le t/4\). Replacing \(F_r\) in each cell by its
midpoint value then gives moment error at most
\(2B(t/4)+t/16\le Bt\). Including (19), the exact grid moment error
is at most \(3Bt\).

### Two passes and bounded exponentials

The log weights satisfy
\[
                 |g_\lambda(z)|\le K+DA^2/2.               \tag{23}
\]
This magnitude can be \(\exp[\operatorname{polylog}(n)]\).
Its integer bit length is its logarithm, which remains polylogarithmic.
Evaluate \(g\) deterministically to absolute error \(t/100\), with
fixed rounding and precision. Evaluating each \(F_r\) to error
\(t/[1000(1+\Lambda)]\), and allocating the arithmetic errors separately,
suffices. The requested precision grows with \(\log\Lambda\).

In a first grid traversal retain the maximum computed log weight \(b\).
In a second traversal regenerate the same computed values and form
\[
                  v_i=e^{\widehat g_i-b},\qquad
                  S=\sum_{i=1}^N v_i.                     \tag{24}
\]
At least one term equals one, so \(1\le S\le N\). Discard any term
whose log gap \(\widehat g_i-b\) is below \(-G\), where
\[
                         G\ge\log(100N/t).                \tag{25}
\]
For an explicit integer choice, take
\(G=2+\lceil\log_2N\rceil+\lceil\log_2(100/t)\rceil\).
The binary lengths of the rational inputs determine these ceilings
without an exact transcendental comparison.
The total discarded mass is at most \(Ne^{-G}\le t/100\).
All retained exponential arguments lie in \([-G,0]\), and \(G\)
is only polynomial in the logarithmic parameters. Two passes avoid
the cumulative-discard issue that would arise from repeatedly changing
a one-pass maximum.

Keep \(P\) signed moment accumulators
\[
                     S_r=\sum_i v_i\,\widehat F_r(z_i).
\]
Their magnitudes are at most \((B+1)N\). Allocate error at most
\[
                       t/[1000N(1+B)]                     \tag{26}
\]
per weight/contribution, with smaller fixed allocations where needed
for multiplication and summation. This uses
\(O(\log N+\log(1+B)+\log(1/t))\) fractional bits. The moments
are \(S_r/S\); after all allocations the denominator is at least
\(1/2\), so no small-normalizer division remains.

For the log normalizer the grid volume cancels:
\[
 \widehat\psi=
 (b_\lambda+\log S_\lambda)-(b_0+\log S_0).
 \tag{27}
\]
Although the two terms can be large, their integer parts need only
the logarithm of (23) in bits; fractional accuracy is \(O(t)\).
Cancellation therefore costs
\(\log(K+DA^2)+\log(1/t)\) bits, not \(K\) bits.

Elementary numerical routines suffice. For an exponential at \(-u\),
\(0\le u\le G\), evaluate the positive Taylor series for \(e^u\)
and invert. The remainder is at most
\(e^G G^{J+1}/(J+1)!\). For requested error \(2^{-b}\), taking
\(J\ge C(G+b+1)^2\) suffices: the elementary bound
\(J!\ge(J/2)^{J/2}\) makes the logarithm of the remainder at most
\(-b\log2\) for a sufficiently large absolute \(C\).
Intermediate
integer length is \(O(G)\). For a logarithm, extract \(S=2^k v\),
\(1\le v<2\), and use
\[
 \log v=2\sum_{j=0}^{\infty}
        \frac{[(v-1)/(v+1)]^{2j+1}}{2j+1}.
\]
The ratio is at most \(1/3\), so its geometric tail gives the desired
accuracy with polynomially many terms and bits. The same series at
\(v=2\) computes \(\log2\). Thus no new normalizer, exponential,
logarithm, or Gaussian-quantile oracle is required.

Perturbing all log weights by at most \(t/100\) changes their log sum
by at most \(t/100\) and their normalized law by at most
\(e^{2t/100}-1\). Combine this with the discarded mass, finite
accumulation errors, row-value error, and (19)–(22). Their sum is
below \(\epsilon_m\) for the moments and \(\epsilon_\psi\) for the
log normalizer, by the generous constants in (17). Reducing individual
arithmetic tolerances by a fixed factor preserves every space bound.

The live workspace consists of the \(D\) grid counters and coordinates,
the current row evaluation, maxima and log sums, \(P\) accumulators,
and the stated precision arithmetic. No grid or sample panel is stored.
This proves the numerical subroutine used in (13).

## 5. Rounded prefixes: preserve feasibility, not the optimizer

In the source noisy history let \(\delta=\eta T>0\). On its common
information/noise event, the actual one-row posterior gives a witness
\(\nu_0\) satisfying
\[
 D(\nu_0\Vert\mu)\le h,\qquad
 \left|\int F_r(z;c_{<r})\,d\nu_0-c_r\right|\le\delta
                 \quad\hbox{at every prefix}.             \tag{28}
\]

Let the retained prefix obey \(\|\widehat c-c\|_\infty\le\rho\),
and use the supplied global circuit bound
\[
 \sup_z|F_r(z;\widehat c_{<r})-F_r(z;c_{<r})|\le L_C\rho.
 \tag{29}
\]
Its logarithmic constant is polylogarithmic. For the compiler's actual
input \(\widehat F_r(z)=F_r(z;\widehat c_{<r})\), the same witness gives
\[
 \left|\int\widehat F_r\,d\nu_0-\widehat c_r\right|
                \le\delta+(1+L_C)\rho.                    \tag{30}
\]
Choose
\[
                         \rho\le\delta/(1+L_C).             \tag{31}
\]
This requires only polylogarithmic precision. Run the compiler afresh
on \(\widehat F,\widehat c\) with \(a=2\delta\), \(s=\delta\).
The witness and its entropy bound are unchanged, and (4) gives
\[
 D(\nu_{\widehat\lambda}\Vert\mu)<2h,\qquad
 \left|\int F_r(z;\widehat c_{<r})\,d\nu_{\widehat\lambda}
                                     -\widehat c_r\right|
                    <\tfrac72\delta<4\delta.              \tag{32}
\]
No proximity of old and new multipliers was assumed. The proof uses
feasibility and strict slack alone, including when moment coordinates
are singular or dependent. It also accounts for the change of row
functions themselves. Ignoring (29) and rounding only the center
would not establish the claim.

Comparison back to the ideal \(F_r,c_r\), if required, adds at most
another \(\delta\) using (29)–(31). The principal statement (32)
calibrates the actually retained rounded-prefix circuit.

## 6. Acquisition model and remaining limits

The finite search and quadratures can run after the current prefix
has been acquired. Each row evaluation holds that prefix fixed.
It does not update the training scalar recursion, read a dense root,
or require any future prefix values. The compiler is deterministic
and independent of the finite cubature seed used for late queries.
It therefore preserves the independence premise of the row-integration
lemma in DENSE_BUDGET_CONDITIONING.md.

Only \(P\) multipliers and one normalizer are cached, in addition to
the existing current-prefix circuit and certificates. Their magnitudes
obey
\[
 \|\widehat\lambda\|_1\le\Lambda,\qquad
                  |\psi(\widehat\lambda)|\le B\Lambda.
\]
Equations (9), (16), and the requested normalizer accuracy give the
retained-bit bound. The space count is a fixed-degree polynomial in
the given dimensions and logarithmic bounds, not a dimension-dependent
power of \(\log n\).

Runtime can be enormous. The finite loops, counters, and acquisition
schedule must be included in any autonomous implementation, but the
assigned preprocessing/acquisition model imposes no runtime bound on
this stage. This result makes no fixed wall-clock acquisition claim
and does not authorize storing a table of future learned responses.

For scalar-register computation, original activation evaluations remain
the original primitives. A bit-space claim uses the inherited counted
polynomial-space precision interface for activations, fixed inputs,
and row instructions. No polynomial-time activation interface is added,
and strip analyticity by itself does not imply computability of arbitrary
activation constants. This is exactly the qualification of the existing
decoder.

The result removes the multiplier-acquisition and normalizer-oracle gaps
for the calibrated row-law integration route under this acquisition model.
It does not identify that law with the collective posterior, bound actual
passive-query physical amplification, or show that likelihood clipping
preserves the tiny learned-moment identities. Thus it does not prove
the full dense-budget decoder or its exact \(2b_n+1/n\) conclusion.

## 7. Claim and process record

| Claim | Status | Scope |
|---|---|---|
| A bounded strict-slack multiplier exists | Proved | Feasible witness (2) |
| A finite dyadic search terminates with (4) | Proved | Certified moment and log-normalizer routine |
| The routine has absolute-polylogarithmic workspace | Proved | Bounds (1), counted row precision interface |
| Rounded-prefix compilation needs optimizer continuity | Not required | Feasibility survives by (30)–(32) |
| Compiled row law completes the physical decoder | Open | Collective and propagation estimates remain separate |

Scientific inputs were the author's complete DENSE_BUDGET_CONDITIONING.md
and the previously read complete EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md,
plus the supervisor's bounded compilation assignment. Previously read
research/rigorous-proof skills and the authorized canonical-notation
fallback remained current. No other scientific source, study, experiment,
or Git operation was used. Only this assigned file was created.
