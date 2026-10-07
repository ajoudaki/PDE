# Cross-check of the constructive route

Reviewed artifact: `CONSTRUCTIVE_ROUTE.md`.

Final reviewed SHA256:
`3f915458fcbc28d276e150088e4c0c2e3c73a99574dd9e367d1259d4a7bb543b`.

The entire original route was read at
`e31089575e2bffe1124ca7298baacfe0e88542feb801bec247308c0305763191`.
The entire corrected route was read at
`93fc935a63f2e7f7d77ac5a4d828015db6db2730f343feee382a18f5bb0bbcee`;
the final additional paragraph about effective bounds, evaluator precision,
and query representation was then checked at the final hash above. The author
confirmed that this paragraph was the only subsequent source change.

This is an internal mathematical cross-check, not an independent promotion
review. The review used the explicit assignment, the maintained notation
contract, and the complete constructive route; no other route file was read.
No experiments, author-source edits, or book edits were performed. The
rigorous-math and conjecture-investigation instructions previously read remain
applicable. The custom notation skill remains inaccessible.

## Verdict

The corrected route's exact formulas and conditional numerical implications
check, including their displayed constants. The original finite-parameter
Gevrey hypothesis had a substantive norm obstruction; this was corrected
without claiming to solve the missing neural regularity problem. The final
source now also excludes hidden dimension dependence through the sample count,
distinguishes logarithmic slack from arbitrary subpolynomial slack, and counts
the finite descriptions and evaluation costs of quadrature bounds.

The result is a valid conditional storage mechanism, not an autonomous
compressor proved for the specified dense network. The final source states
that distinction repeatedly and retains the necessary identification,
regularity, compiler, output, and finite-width hypotheses as open.

## 1. Exact neural equations and stopping tail

With the prescribed loss and mobilities, differentiating
\(f_n=(W^{(L+1)})^Th^{(L)}/n\) gives

\[
\frac{\partial f_n}{\partial W^{(1)}}
 =\frac{\delta^{(1)}x^T}{n\sqrt d},\qquad
\frac{\partial f_n}{\partial W^{(\ell)}}
 =\frac{\delta^{(\ell)}(h^{(\ell-1)})^T}{n},\qquad
\frac{\partial f_n}{\partial W^{(L+1)}}=\frac{h^{(L)}}n.
\]

Multiplying by \((2/m)r_a\) and the block mobilities gives exactly the
three weight-update equations displayed in the source. No factor of \(n\),
\(m\), or \(\sqrt d\) is missing.

At zero readout all hidden velocities vanish, while
\(v=(W^{(L+1)})'(0)=(2/m)\sum_b y_bh_b^{(L)}(0)\). In differentiating the
top hidden equation, terms containing \(\delta_a^{(L)}(0)\) vanish and

\[
(\delta_a^{(L)})'(0)=v\odot\phi'(z_a^{(L)}(0)).
\]

Substitution produces the stated top hidden acceleration, including its
positive sign and factor \(2/(mn)\). This is an exact expression; it does
not prove that every admissible instance has nonzero acceleration, and the
source does not make that stronger claim.

The kernel prediction equation follows directly by the chain rule. Under
the displayed persistent gap and cross-kernel bound,

\[
\|r(t)\|_2\leq\|y\|_2e^{-2\lambda t/m},\qquad
|\partial_t f_n(t,x)|\leq(2B/m)\|y\|_2e^{-2\lambda t/m}.
\]

Integration gives exactly
\(B\|y\|_2\lambda^{-1}e^{-2\lambda T/m}\) for the tail. The stated
stopping time makes this at most \(\epsilon\). If the numerical approximation
already has error \(\epsilon\) through that time, holding its own computed
terminal output gives error at most \(2\epsilon\) afterward; the source says
an *additional* error \(\epsilon\), which is correct. Any final prescribed
error budget must allocate these terms separately.

The all-time lemma is conditional on the actual trajectory existing and
obeying those bounds. To infer a width-independent
\(T=O(\log(1/\epsilon))\), its gap and cross-kernel constants must be
controlled uniformly in width. The lemma itself is valid even if they depend
on width, but that would not automatically give the desired short horizon.
Initialized concentration and an initialized gap do not prove their
persistence. This remains part of the neural stability obligation.

## 2. Serial Gaussian integration: constants and memory

Let \(V=(2R)^s\). The four error allocations in the source check separately:

1. The union bound gives
   \(\mathbb P(G\notin[-R,R]^s)\leq2s e^{-R^2/2}\), so
   Cauchy–Schwarz bounds the omitted integral by
   \(M\sqrt{2s}e^{-R^2/4}\). The specified \(R\) makes this at most
   \(\epsilon/4\), including the branch in which the logarithm is
   nonpositive. If \(M=0\), every expectation is zero, as handled explicitly.
2. The maximum midpoint distance is \(R\sqrt s/N\), so the midpoint error
   is \(VK_RR\sqrt s/N\). The prescribed
   \(N\geq2(2R)^{s+1}K_R\sqrt s/\epsilon\) makes it at most
   \(\epsilon/4\). If \(K_R=0\), \(N=1\) is allowed.
3. An integrand error \(\epsilon/(4V)\), multiplied by cell volume
   \(V/N^s\) and summed over \(N^s\) cells, contributes at most
   \(\epsilon/4\).
4. The stated combined arithmetic error \(\epsilon/(4N^s)\) per summand
   and accumulator update contributes at most \(\epsilon/4\).

Thus the total absolute error is at most \(\epsilon\), uniformly over the
query set under the stated uniform assumptions.

The memory count is also sufficient. Each midpoint is a rational vector with
\(O(s(\log(R+1)+\log(N+1)))\) bits. The number \(N^s\), cell-volume
numerators and denominators, and loop indices use that same order of storage.
One can multiply and divide these integers using memory proportional to their
bit lengths. The signed partial sum has magnitude at most
\(V(B_R+1)+O(1)\); fractional precision
\(O(\log(1/\epsilon)+s\log N)\) suffices for the allocated rounding error.
No step needs to retain \(N^s\) function values.

The final clarification about supplied bounds is necessary and adequate:
for a total-space conclusion, upper-bound algorithms must be computable, and
their descriptions and workspaces count in \(Q\). The actual evaluator
accuracy is \(\epsilon/(4V)\), not merely \(\epsilon\). Its query input
representation and resulting error also count. Merely bounding the numerical
values \(M,B_R,K_R\) would not bound the size of algorithms describing them.

An explicit exponent check confirms the qualitative claim. Put
\(H=1+\log(1/\epsilon)\), and suppose the displayed quantities
\(s,Q,\log(1+M),\log(1+B_R),\log(1+K_R)\) are all at most
\(C H^c\), with a fixed \(c\geq0\). Then

\[
\log(R+1)=O_C(\log(H+1)),\qquad
\log(N+1)=O_C(H+H^c\log(H+1)).
\]

Substitution into the workspace bound gives, for example,

\[
O_C\!\left(H^{c+\max\{1,c\}}\log(H+1)\right)
\]

bits, including \(Q\). Hence a power such as
\(H^{c+\max\{1,c\}+1}\) suffices. Its exponent is independent of
dimension and sample count precisely when \(c\) is. The constant may still
depend strongly on both. This is a storage result; the enormous count
\(N^s\) of integrand evaluations has not disappeared.

For program use, \(J\) must count all scalar Gaussian source coordinates.
The stated covariance cost is then \(O(J^2)\) scalar entries, multiplied
by their required bit precision in a bit model. A supplied singular covariance
square root causes no conceptual difficulty for the quadrature lemma, but its
computation, rounding, and downstream sensitivity require the finite-precision
contract explicitly retained in the source.

## 3. The norm defect and its correction

The original source used the already defined complete finite parameter vector
\(\theta\) in a proposed bound
\(\|\theta^{(k)}(t)\|\leq MA^k(k!)^\sigma\), with \(M,A\) independent
of width. In the canonical ordinary Euclidean/Frobenius norm this fails
already at derivative order one in every nonzero-label instance with a
width-independent initialized top-feature Gram gap.

Let \(H\) be the \(n\times m\) matrix with columns \(h_a^{(L)}(0)\).
All hidden velocities are zero initially, so

\[
\|\theta'(0)\|_2^2
 =\|(W^{(L+1)})'(0)\|_2^2
 =\frac4{m^2}y^TH^THy
 =\frac{4n}{m^2}y^TK_n^{\mathrm{tr}}(0)y
 \geq\frac{4n\lambda_0}{m^2}\|y\|_2^2.
\]

For fixed \(y\ne0\) and \(\lambda_0>0\), no width-independent \(MA\)
can bound this first derivative. The corrected source preserves this exact
obstruction and replaces the impossible hypothesis by one about an explicitly
typed *hypothetical* population state.

Its state space is a finite product of a first-row \(L^2\) space,
Hilbert–Schmidt spaces for trained hidden increments, and an \(L^2\)
readout space, with the displayed sum norm. This is a Banach space. It does
not assume initialized Gaussian actions are Hilbert–Schmidt; only the trained
increments receive that norm. The correspondence with finite RMS first-row
and readout norms and ordinary Frobenius increment norms is consistent.

This correction removes the literal norm contradiction. It establishes
neither the existence of that population dynamics nor its identification with
the dense network, its time regularity, or an admissible finite representation.
The source explicitly states all four limits. A named infinite-dimensional
state cannot itself be counted as a bounded number of stored scalars.

## 4. Gevrey Taylor implication

In the explicit Banach norm, suppose the uniform derivative hypothesis holds
for the exact flows from every numerical starting state used, and suppose
their flow maps are Lipschitz with factor \(e^{Ct}\), taking \(C\geq0\)
without loss of generality. The integral Taylor remainder for an order-\(p\)
step of length \(h\) is

\[
\frac{h^{p+1}}{(p+1)!}
 \sup\|S^{(p+1)}\|_{\mathcal B}
 \leq M(Ah)^{p+1}((p+1)!)^{\sigma-1}.
\]

With \(h=q/[A(p+1)^{\sigma-1}]\) and \(0<q<1\), the elementary bound
\((p+1)!\leq(p+1)^{p+1}\) gives a local error at most \(Mq^{p+1}\).
For \(N=\lceil T/h\rceil\), exact-flow stability gives the recursion

\[
E_{j+1}\leq e^{Ch_j}E_j+Mq^{p+1},\qquad E_0=0,
\]

and hence \(E_j\leq jMq^{p+1}e^{CT}\). A Taylor polynomial inside each
step has the same estimate with \(j+1\leq N\). Thus the displayed
\(NM e^{CT}q^{p+1}\) bound is correct at nodes and between nodes. It needs
no separate stability theorem for the Taylor update, but it does need the
assumed common tube and derivative bounds at the numerical starting states.

For \(T\leq C_T H\), take \(p=\lceil KH\rceil\). Then
\(N=O(H^\sigma)\) and the error is bounded by

\[
C_1H^\sigma\exp\{(CC_T-K|\log q|)H\}.
\]

Choosing fixed \(K\) with \(K|\log q|>CC_T+2\) makes this at most
\(\epsilon\) for sufficiently small \(\epsilon\), after harmless constant
adjustments. Finite-precision and quadrature errors add separate local defects;
their total propagated error is controlled if each is, for example, at most
\(\epsilon/(N e^{CT})\) times an appropriate fixed error-budget fraction.
The logarithm of this inverse local tolerance is \(O(H)\). Computing those
defects with such precision remains part of the compiler assumptions, not a
consequence of the Taylor estimate.

If each order-\(p\) step adds at most \(C(d,m,L)p^b\) scalar Gaussian
sources, the total is \(J=O(C(d,m,L)H^{\sigma+b})\). Polynomial graph,
coefficient, integration, conditioning, and precision bounds then give a
fixed power of \(H\) storage only when every relevant polynomial degree is
independent of both \(d\) and \(m\). A bound such as \(J^m\) would be
polynomial for each fixed instance yet would not imply the intended exponent
across dimensions. The amended source now excludes that error explicitly.

The theorem at this point is conditional numerical analysis for a supplied
effective population program. The source has not constructed that program
for the nonlinear Gaussian network.

## 5. Representation and accuracy scope

The final source does not use an oracle evaluation, precomputed future
trajectory, or exact-real packing as its asserted mechanism. It instead
requires a causal transcript of finitely described Gaussian computations,
counts its coefficients and evaluator workspace, and labels the resulting
machine an autonomous hybrid representation. Restartability is legitimate
for such a supplied program because the current transcript is retained. A
smooth finite-dimensional autonomous ODE would need a separate construction,
as the source states.

The revised accuracy discussion is also necessary. From
\(\log(1/\epsilon_n)=\Theta(\log n)\) one gets only a substitution in the
storage bound. An error \(n^{-1/2+o(1)}\) may contain the factor
\(\exp(\sqrt{\log n})\), which is larger than every fixed logarithmic
power. Consequently it cannot replace an allowed tolerance
\(Cn^{-1/2}(\log n)^b\). The amended route explicitly requires the
finite-width comparison and numerical errors at the prescribed tolerance,
or a proved comparison to actual run-to-run discrepancy.

Data storage is now correctly stated as \((md+m)b_{\mathrm{data}}\) bits,
including its precision dependence and effect on prediction error. It is
not merely \(md+m\) bits, and accuracy-dependent precision cannot be absorbed
into a dimension-dependent constant.

The auxiliary example concerning \(\tanh(tG)\) is mathematically valid:
for \(t=i\tau\ne0\), poles occur at real
\(G=\pi(k+1/2)/\tau\). For Gaussian \(L^p\) with \(p\geq1\), the
singularity is not integrable near such a point, since the Gaussian density
is positive there. Real derivatives of every fixed order can nevertheless
exist. This correctly defeats an automatic complex-neighborhood argument;
it does not prove failure of a finite Gevrey order for the network.

## Remaining limits of the checked result

The exact neural equations, conditional stopping lemma, finite-space Gaussian
integration lemma, and conditional Gevrey-to-short-program implication pass
this mathematical cross-check in their final stated scope. No checked result
supplies the hypothetical population state's identification, its uniform
Gevrey regularity and common tube, the polynomial Gaussian compiler, uniform
whole-sphere decoder control, or the growing-order all-time finite-width
comparison. Persistent kernel bounds and any comparison to actual
self-variability also remain separate obligations.

The valid constructive lesson is therefore limited but concrete: tensor
quadrature node count is not automatically a retained-storage lower bound.
The target autonomous neural compression theorem remains open in this route.
