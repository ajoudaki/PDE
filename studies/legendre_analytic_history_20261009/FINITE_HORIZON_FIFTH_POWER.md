# Fifth-power accuracy on each fixed physical-time interval

Date: 2026-10-10. Author calculation; this note is a partial result toward,
not a solution of, the all-time one-tenth-order question. Scientific inputs
are the current paper's `compact.tex`, `compact_foundations.tex`,
`compact_fitting.tex`, `compact_legendre.tex`, and this study's
`CROSS_TAIL_IDENTITIES.md` and `SHARPER_OBSTRUCTION_ROUTE.md`. The two study
notes supply scalar Legendre identities, not a general-model conclusion.
No algorithm, clock, prefix, activation hypothesis, or label condition is
changed. Constants in this note may depend on the fixed finite horizon;
that dependence must not be suppressed when discussing all-time accuracy.

## Partial theorem

Fix the original admissible problem, a confidence, and a finite physical
time horizon \(T>0\), all independently of width. There is a constant
\(C_T\), depending on those fixed quantities but not on \(n,q\), such
that eventually at that confidence, the original Legendre model satisfies

\[
 \sup_{0\le t\le T,\ \|x\|=\sqrt d}
 |f_{\rm Leg}(t,x)-f_n(t,x)|
 \le \frac{\exp(C_T\sqrt{\log(en)})}{q^5},
 \qquad q\ge\exp(C_T\sqrt{\log(en)}).                 \tag{1}
\]

The initialization event is the paper's fitting, source and carrier event.
For sufficiently large width it works for every integer order satisfying
the displayed threshold. The label vector is fixed, with \(Y>0\); (1) does not
assert a uniform bound as their norm tends to zero.

Consequently the deterministic order

\[
 q=\left\lceil n^{1/10}
             \exp\bigl((\log(en))^{3/4}\bigr)\right\rceil
   =n^{1/10+o(1)}                                      \tag{2}
\]

achieves \(o(Y/[\sqrt n\log(en)^3])\) on every fixed finite interval.
This quantifier does **not** cover the supremum over all physical times.

The proof uses dense histories in their own residual clock, whose finite
derivatives are controlled by the existing source theorem. Projection
contraction then transfers their estimates to the actual closure through
an integral bootstrap. In particular no high derivative of the closure
history is assumed or estimated.

## 1. A regular clock segment and dense derivative bounds

Use Euclidean mobility coordinates
\(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\).
All parameter differences below use their Euclidean block norm. Absolute
hidden matrices use operator norms, never their growing Frobenius norms.
Use feature and backward-response RMS norms, divided by \(\sqrt n\),
and sample RMS norms, divided by \(\sqrt m\).

Write \(\rho_D=\|f_n(X)-y\|_2/\sqrt m\). The real fitting tube bounds
the training Jacobian by a constant depending only on the fixed problem.
The equation \(\dot r_D=-2J_DJ_D^*r_D\) therefore implies
\(|\dot\rho_D|\le C\rho_D\), with sample-space adjoints taken in the
RMS norm. Since \(\rho_D(0)=Y>0\),

\[
 \rho_D(t)\ge Y e^{-C(T+1)}=:c_T>0
 \quad (0\le t\le T+1).                              \tag{3}
\]

The dense clock \(\tau_D(t)=1+\int_0^t\rho_D\) is invertible there.
Set \(A_* =\tau_D(T+1)\) and parameterize the dense trajectory by
\(\xi\in[1,A_*]\). Here \(A_*\le1+2Ym/\gamma\); all constants below
are uniform in its realized value.

The source theorem gives an RMS-bounded complex neighborhood of the dense
forward and backward fields of physical-time radius
\(c/\sqrt{\log(en)}\). For any of the training fields, the Banach-space
Cauchy integral formula on a disk of half that radius gives

\[
 \sup_{t\le T+1}\frac{\|\partial_t^k h_a^{(j)}(t)\|_2
       +\|\partial_t^k\delta_a^{(j)}(t)\|_2}{\sqrt n}
 \le C_{T,k}[\log(en)]^{k/2},\quad 0\le k\le4.       \tag{4}
\]

The same estimate holds for each training prediction, using its bounded
holomorphic readout pairing. Products, the square root defining
\(\rho_D\), and reciprocals are differentiated only along the real
interval where (3) holds. Their derivatives through order four obey
bounds of the same form, with constants enlarged using \(c_T^{-1}\).
Repeated application of \(\partial_\xi=\rho_D^{-1}\partial_t\) proves

\[
 \sup_{1\le\xi\le A_*}
 \bigl(\|\partial_\xi^k h_D\|_{\rm RMS}
             +\|\partial_\xi^k b_D\|_{\rm RMS}\bigr)
 \le C_T[\log(en)]^2,
 \quad 0\le k\le4,                                  \tag{5}
\]

where \(b_{D,a}=(r_{D,a}/\rho_D)\delta_{D,a}\). The RMS here also
averages the finitely many samples; layer maxima may be taken. For the
bound on reciprocals through order four, derivatives of \(\rho_D\)
through that same order suffice. These come directly from the prediction
bounds in (4), not from any derivative estimate for the closure.

On the prefix \([0,1]\), extend \(h_D\) constantly and \(b_D\) by zero.
The zero initial readout implies

\[
 b_D(1)=0,\qquad \partial_\xi h_D(1+)=0.              \tag{6}
\]

Indeed every initial feature-weight velocity contains a backward response,
which vanishes at zero readout. Division by \(\rho_D(0)=Y\) is legitimate.

## 2. Fifth-power dense cross tail, uniformly in the interval end

Let \(Q_q^A=I-\Pi_q^A\), where \(\Pi_q^A\) is the degree-below-\(q\)
Legendre projection on \([0,A]\). For each \(1\le A\le A_*\), define

\[
 H_\ell[b,h](A)=\frac2{mn}\sum_a\int_0^A
       (Q_q^Ab_a^{(\ell)})(Q_q^Ah_a^{(\ell-1)})^\top\,d\xi.
                                                               \tag{7}
\]

Subtract right Taylor jets through degree four at the join from the
piecewise dense histories. The remaining functions have four matching
derivatives across the join. In \(x=2\xi/A-1\), twice applying
\(\mathcal L=-\partial_x((1-x^2)\partial_x)\) and integrating against
Legendre polynomials yields

\[
 \|Q_q^AR\|_{L^2,\rm RMS}
 \le [q(q+1)]^{-2}\|\mathcal L^2R\|_{L^2,\rm RMS}
 \le C_T[\log(en)]^2q^{-4}.                           \tag{8}
\]

Boundary terms vanish at the outer endpoints because of \(1-x^2\);
they cancel at the join by the matching derivatives. Four bounded
derivatives suffice to interpret the second application weakly and to
bound its square-integrable result. Approximation by smooth functions
justifies the integrations if desired.

For every fixed \(k\ge1\), the truncated powers satisfy uniformly in
\(A\in[1,A_*]\)

\[
 \|Q_q^A(\xi-1)_+^k\|_{L^2}\le C_kq^{-k-1/2}.        \tag{9}
\]

For completeness, mapping the join to \(a=2/A-1\), Rodrigues' formula
and \(k+1\) integrations give, for \(j>k\),

\[
 \int_a^1(x-a)^kP_j(x)\,dx
 =\frac{k!(1-a^2)^{k+1}P_j^{(k+1)}(a)}
             {(j-k)(j-k+1)\cdots(j+k+1)}.
\]

The Legendre energy bound and its differentiated equation give
\(|P_j^{(r)}(\cos\vartheta)|\le C_rj^{r-1/2}
(\sin\vartheta)^{-r-1/2}\) for \(\sin\vartheta\ge j^{-1}\).
In the remaining region use \(|P_j^{(r)}|\le C_rj^{2r}\).
The displayed moments are therefore \(O(j^{-k-3/2})\), uniformly even
when \(A\downarrow1\). Multiplying by the squared normalization
\((2j+1)/A\) and summing proves (9). These scalar energy and derivative
identities, including their endpoint bounds, are derived in the two
study inputs named above and the paper's projection lemma.

The exceptional ramp--quadratic pair has one extra cancellation. Set
\(u=(\xi-1)_+\), \(v=u^2\). Orthogonality and \(v'=2u\) give

\[
 \langle Q_q^Au,Q_q^Av\rangle
   =\tfrac14\bigl((Q_q^Av)(A)^2-(Q_q^Av)(0)^2\bigr).
\]

The projection endpoint kernel expresses these errors using the two ramp
moments of degrees \(q,q-1\), bounded above by \(Cq^{-5/2}\).
Consequently this pairing is \(O(q^{-5})\), not the \(O(q^{-4})\)
obtained by multiplying its two norms. Small orders are absorbed in the
constant. All other jet pairings are bounded by (9): the smallest possible
remaining degree pairs are \((1,3)\) and \((2,2)\). Remainders use (8).
Together with (5)--(6), this proves, uniformly in \(A\),

\[
 \begin{split}
 \|Q_q^Ab_D\|_{L^2,\rm RMS}&\le C_T[\log(en)]^2q^{-3/2},\\
 \|Q_q^Ah_D\|_{L^2,\rm RMS}&\le C_T[\log(en)]^2q^{-5/2},\\
 \sum_{\ell=2}^L\|H_\ell[b_D,h_D](A)\|_F
       &\le C_T[\log(en)]^4q^{-5}.                    \tag{10}
 \end{split}
\]

## 3. Transfer without differentiating the closure histories

Parameterize the closure by its own clock and append its physical time
as a comparison coordinate. Initially both clocks and both states agree.
As long as \(\widehat\rho\ge c_T/2\), the ordinary dense clock vector
field is \(-2J^*r/\rho\), and the time coordinate has derivative
\(1/\rho\). Compare both at the same clock value.

On a small fixed discrepancy tube around the dense path, subtraction of
these vector fields costs at most
\(C_T\sqrt{\log(en)}\) times the parameter discrepancy. To verify
this, forward subtraction uses only the real operator bounds. Backward
subtraction is

\[
 \delta_{\rm Leg}-\delta_D
 =\phi'(z_{\rm Leg})\odot(k_{\rm Leg}-k_D)
  +[\phi'(z_{\rm Leg})-\phi'(z_D)]\odot k_D.
\]

Only the dense carrier in the second term needs a coordinate bound; the
source event supplies \(\|k_D\|_\infty\le C\sqrt{\log(en)}\).
Layer induction therefore bounds the response and training-Jacobian
differences by \(C\sqrt{\log(en)}\) times the parameter difference.
This is exactly the actual dense-to-closure subtraction in the paper,
and does not require bounded closure carriers. The functions
\(r/\rho\) and \(1/\rho\) are Lipschitz on \(\rho\ge c_T/2\).
The same argument proves the history difference bounds at equal clocks.

Let \(E(A)\) be the running maximum, up to clock \(A\), of the sum
of parameter discrepancy and physical-time discrepancy. Projection is
contractive in \(L^2\), so (10) and bilinear expansion of (7) imply

\[
 \sum_\ell\|H_\ell[\widehat b,\widehat h](A)
                       -H_\ell[b_D,h_D](A)\|_F
 \le C_T[\log(en)]^3\bigl(q^{-3/2}E(A)+E(A)^2\bigr). \tag{11}
\]

Factors from the bounded clock interval and finite sample/layer sums
are included in \(C_T\). Prefix differences vanish. In the bilinear
expansion the two linear terms contain, respectively, the dense tails
\(q^{-3/2}\) and \(q^{-5/2}\); the quadratic term uses only projection
contraction and the history difference bounds just proved.

Reconstruction is exactly the integral of the closure's own ordinary
clock gradient plus \(H_\ell[\widehat b,\widehat h](A)\). The first
layer and readout have no such extra term. The physical-time coordinate
has the ordinary integral \(\int_1^A1/\widehat\rho\). Subtracting the
two integral systems now gives

\[
 E(A)\le C_T\sqrt{\log(en)}\int_1^AE(\xi)\,d\xi
       +C_T[\log(en)]^4q^{-5}
       +C_T[\log(en)]^3(q^{-3/2}E(A)+E(A)^2).         \tag{12}
\]

Stop first when either \(E\) reaches a sufficiently small fixed
multiple of \([\log(en)]^{-3}\), or the residual tube is left, or
\(A=A_*\). Under the threshold in (1), the last two terms containing
\(E(A)\) can be absorbed into the left side. Gronwall's inequality
on the bounded clock interval gives

\[
 E(A)\le C_T[\log(en)]^4
        \exp(C_T\sqrt{\log(en)})q^{-5}.              \tag{13}
\]

Enlarging the threshold constant makes this bound strictly smaller than
the stopping tolerance and than the fixed tolerance ensuring
\(\widehat\rho\ge c_T/2\). Hence neither stop can occur. This also
justifies continuing the closure clock all the way to \(A_*\): its
residual cannot vanish on this segment. The original physical fitting
bounds supply existence; the comparison supplies this clock invertibility.

Finally \(|\widehat t(A_*)-(T+1)|\le E(A_*)<1/2\), so every closure
physical time in \([0,T]\) is represented on this common clock segment.
Whole-sphere prediction subtraction at equal clocks uses bounded
operators and readouts and costs a fixed constant times the parameter
discrepancy. Dense predictions have bounded physical-time speed uniformly
over the sphere, by their gradient and residual bounds. Replacing the
dense time at the same clock by the closure's physical time therefore
costs another fixed constant times \(E\). Absorb the logarithmic factor
in (13) into its exponential to obtain (1).

## 4. Why this does not finish the user's request

The dense-variability target shrinks like \(n^{-1/2}\), up to logarithms.
The existing tail estimate requires a physical horizon proportional to
\(\log n\), not fixed, to reach this scale. The lower bound (3) then
shrinks as a power of \(n\); its reciprocals in the clock derivatives
and Lipschitz coefficients can no longer be absorbed into
\(\exp(C_T\sqrt{\log(en)})=n^{o(1)}\).

In particular one cannot insert \(T=T(n)\) into (1) and call its
constant fixed. Nor can one exchange the quantifiers "every fixed
finite interval" and "the entire trajectory." The late-time clock
boundary layer is a genuine remaining proof obligation. The preceding
theorem removes the need to control high derivatives of the closure
on regular clock segments; it does not remove that boundary layer.
