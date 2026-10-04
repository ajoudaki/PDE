# Internal check of the all-layer forward construction

2026-09-30. Checked the complete ALL_LAYER_FORWARD.md, including Section 8,
within the supervisor's assigned scope. This is an internal mathematical
check, not an independent promotion review. The author's prior history and
other routes were not read for this check. The supervisor separately supplied
the fixed-width existence argument examined below.

After the noted wording corrections, the checked candidate's SHA-256 was
`5cc3fb46e4caa10a8df36e1dd9bc02c485272d9283c114b155dcdf95b3165b48`
(`ALL_LAYER_FORWARD.md`, recorded by the supervising task).

**Outcome:** the claimed driven representation theorem is valid under its
stated smoothness, bounded-input, finite-label-second-moment, and
zero-readout assumptions. The result proves \(O(M^{-1})\) error for all
forward histories and for the **last** backward history, with the different
error norms and storage costs stated in the candidate. It does not prove the
earlier backward histories, quadratic \(O(M^{-2})\) error, autonomous
compressed training, sample-free runtime, or subquadratic peak memory.

## 1. Normalization and constants

The metric speed in (2) has the correct canonical factors:
first-layer and readout squared speeds are divided by \(n\), whereas hidden
matrix squared speeds are not. With \(V=\sqrt{TL_0}\), Cauchy--Schwarz yields
all three bounds in (6). In particular, \(|w|_n\le V\), so
\[
 D_\ell=A^{L-\ell+1}Q^{L-\ell}V,\qquad Q=K_0+V,
\]
correctly bounds the normalized Euclidean adjoints.

The nuclear-norm source calculation has exactly the needed \(1/n\):
\[
 \|\delta_\ell h_{\ell-1}^{\mathsf T}/n\|_*
   =|\delta_\ell|_n|h_{\ell-1}|_n .
\]
Thus \(\|\dot W_\ell\|_*\le2BD_\ell\rho\), and the displayed
\(\kappa_\ell=2BD_\ell T\rho_0\) is independent of width and sample count.

Forward variation (13) is also correctly normalized:
\[
 |\dot W_\ell h_{\ell-1}|_n
 \le\|\dot W_\ell\|_{\rm op}|h_{\ell-1}|_n
 \le Bq.
\]
The first-layer term uses exactly \(\|x\|/\sqrt d\le R\).
The constants \(c_\ell,b_\ell,a_z,b_z,d_i,f_i,\gamma_i\) are built by a
fixed number of recursions from \(L,T,L_0,R,A,B,K_0\), plus
\(\|\phi''\|_\infty\) for Section 8. None hides a factor of \(n\), sample
count, or an input-net size.

The pointwise speed bounds (15) are correct. They imply \(q\le C\rho\),
so a flat activity clock contains no parameter motion. This justifies the
activity-clock forward representation without an implicit inverse-clock
regularity assumption.

## 2. Whole-input and population error are distinguished correctly

The forward norm is
\[
 \|g\|_{X,n}=\sup_{x\in X}\|g(x)\|_2/\sqrt n.
\]
It controls each forward history simultaneously over the full permitted
input set. It is not merely an empirical-data estimate, and no input net is
used. It consequently controls the joint neuron-input \(L^2\) norm for
every input probability law supported on \(X\).

The original wording calling this a “population RMS norm” was ambiguous
because the candidate also uses a data population. The author corrected it
during this check to identify the neuron RMS norm uniformly over input and
the weaker data-population consequence.

Section 8 proves uniform-input error for \(\delta_L\) and the scalar output
\(f\), but only joint \(L^2(P;\ell_n^2)\) error for the residual-weighted
source \(r\delta_L\) and its history. That distinction is necessary with
only \(y\in L^2(P)\), and the candidate makes it.

## 3. Snapshot approximation, rank cap, and descriptor count

For a truncated increment \(A_{\ell,r}\), the bound
\[
 \|A_\ell-A_{\ell,r}\|_{\rm op}\le\kappa_\ell/(r+1)
\]
is correct for \(r<n\). Truncation also satisfies
\(\|A_{\ell,r}\|_{\rm op}\le\|A_\ell\|_F\le V\).
The approximate circuit therefore has bounded hidden operators and bounded
activation coordinates, with no assumption that it is already accurate.
The decomposition used in (16) proves the recurrence
\[
 e_\ell\le AQe_{\ell-1}+AB\kappa_\ell/(r+1).
\]

The choice \(r=\min(n,M)\) needs the following split, which the candidate
explicitly supplies:

- If \(M<n\), then \(r=M\), and \(1/(M+1)\le1/M\).
- If \(M\ge n\), then \(r=n\), the truncation is exact, and the actual
  snapshot truncation error is zero.

One must not infer \(b_\ell/(n+1)\le b_\ell/M\) in the second case. The
candidate instead invokes exact storage, so (22) is valid. The identical
case split validates the last-backward \(O(M^{-1})\) statement after (37).

Since \(\int_0^Tq\le V\), cells of path-length threshold \(V/M\) number at
most \(M+1\), including a possible final cell opened at the endpoint.
For each cell, \(nd\) coordinates store \(W_1\), and at most
\(2nr+r\) coordinates store each hidden rank-\(r\) increment.
The resulting count (23) and its looser bound
\[
 O(nd+Ln^2+ndM+LnM^2)
\]
are valid. The latter retains the exact dense Gaussian initialization
explicitly. It does not replace it by an exact-real pseudorandom seed.

Section 8 additionally retains \(n\) readout coordinates and \(K+1\)
physical-time moments per cell, for extra cost \(O(M[n+K+1])\).
No label vector, sample-indexed field, function-valued response coordinate,
or dense historical trained matrix is omitted from the claimed descriptor
count.

This is a retained-representation count. The author explicitly allows a
dense supplied canonical driver and dense temporary SVD work. Counting the
complete executing system adds that state; the report does not claim an
end-to-end subquadratic-memory training algorithm.

## 4. Causal coefficients and the physical-time issue

For the forward histories, the coefficient in (19) depends only on cell
clock endpoints, current \(\tau\), and the fixed polynomial \(p_k\).
For the intended finite polynomial/Legendre family, antiderivatives give
ordinary scalar computations. The prefix uses the exact initial network.

The error bound follows by integrating the uniform cell error against
\(|p_k|\le1\) and dividing by \(\tau\). The total forward history clock mass
is \(\tau-1\), so the proof does not lose a factor of \(T\) or \(\rho_0\).

For arbitrary merely specified bounded functions \(p_k\), (19) is still an
exact mathematical coefficient formula, but a computational encoding claim
would also need a representation/evaluation rule for those functions.
The actual polynomial family treated in the candidate has that rule;
this observation does not affect the asserted Legendre construction.

For the last backward history, the cancellation
\(\rho(r/\rho)\delta_L=r\delta_L\) correctly changes integration to
physical time. Clock endpoints alone would not determine (34).
The candidate expressly avoids that error by storing
\[
 m_{ja}(t)=\int_{I_j\cap[0,t]}\tau(s)^a\,ds
 \quad(0\le a\le K).
\]
Active moments evolve with \(\dot m_{ja}=\tau(t)^a\), and completed moments
are fixed. Substitution of \(p_k(v)=\sum_{a=0}^kc_{ka}v^a\) yields
\[
 \beta_{jk}(t)=\sum_{a=0}^kc_{ka}\tau(t)^{-a-1}m_{ja}(t),
\]
exactly as in (36). The coefficients are causal and require no future
trajectory. They continue to be well defined if \(\rho=0\), because the
source \(r\delta_L\) then vanishes \(P\)-almost everywhere.

The bound in (37) correctly costs at most physical-time mass \(T/\tau\le T\).
It is not silently replacing physical-time integration by activity-time
integration.

## 5. Last-layer backward estimate

The decisive extra property is the coordinatewise bound
\(\|w(t)\|_\infty\le2BT\rho_0\), valid from the exact readout equation.
Consequently
\[
 \delta_L(t)-d_L^j
 =(w(t)-w(t_j))\odot\phi'(z_L(t))
  +w(t_j)\odot[\phi'(z_L(t))-\phi'(z_L^j)]
\]
is controlled by normalized readout displacement and normalized
preactivation error, without any width-dependent multiplier norm.
This proves (30). The scalar output estimate (31) follows from normalized
Cauchy--Schwarz and is correctly normalized by \(1/n\).

The exact decomposition
\[
 r\delta_L-(f^j-y)d_L^j
 =r(\delta_L-d_L^j)+(f-f^j)d_L^j
\]
gives (32), because the first field difference is uniform in input and
\(\|r\|_{L^2(P)}\le\rho_0\). Only a second label moment is used.

The proof cannot be iterated to lower backward layers using the same
estimates: their multiplier \(W_{\ell+1}^{\mathsf T}\delta_{\ell+1}\)
has only the established normalized \(L^2\) bound, rather than a uniform
coordinate bound. The candidate states this limitation correctly.

## 6. Exact Gaussian event

For the two \(1/4\) nets, cardinality at most \(9^n\), the factor two in
\(\|G\|_{\rm op}\le2\max|u^\mathsf TGv|\) and the variance \(1/n\) of each
fixed bilinear form are correct. Thus (26) follows by the Gaussian tail and
a union bound.

Set \(C=2(L-1)/\eta\). The candidate's choice gives
\(a^2=4\log9+2\log C\), so each matrix's bad probability is at most
\(2C^{-n}\). Union over \(L-1\) matrices gives
\(2(L-1)C^{-n}\le\eta\) for every \(n\ge1\).
The event therefore is genuinely width-uniform. Independence between
trained responses and Gaussian matrices is not invoked.

For \(L=1\), no hidden-matrix event is required and the rank-error terms
are zero, as stated. Zero readout makes the initial loss \(\mathbb E y^2\)
deterministic under a fixed population. The Gaussian first layer requires
no separate operator bound in this proof.

## 7. Fixed-width existence strengthening

The supervisor suggested removing the separately assumed classical-flow
existence. That strengthening is valid under the smooth class in the
candidate.

At fixed finite \(n,d,L\), on a bounded parameter ball, bounded inputs and
\(\phi\in C_b^2\) make the gradient-flow vector field continuously
differentiable under the population integral. Its parameter derivatives
are dominated by \(C_{\rm ball}(1+|y|)\), integrable because \(y\in L^2(P)\).
It is therefore locally Lipschitz and has a unique local classical flow.

The exact loss identity holds on its existence interval. For each finite
\(T\), (1) gives bounded displacement in the flow metric, hence bounded
ordinary Euclidean parameter displacement at fixed width (the first layer
and readout acquire at most a factor \(\sqrt n\)). Finite-time escape from
every bounded ball is impossible. Local ODE continuation then extends the
solution globally.

This argument does not need width-uniform ordinary Euclidean parameter
bounds. The global-existence improvement is optional for the candidate's
conditional statement; it removes an unnecessary hypothesis without
changing the encoding result.

## 8. Corrections and final claim boundary

Two wording corrections were requested and the author confirmed saving them:

1. The norm at (3) now explicitly says neuron RMS uniformly over input,
   with data-population \(L^2\) as a weaker consequence.
2. The sentence after (21) no longer uses \(q\) both for metric speed and
   moment count. For \(K+1\) coordinates it now states the \(K+1\) factor
   for \(\ell^1\) aggregation and \(\sqrt{K+1}\) for \(\ell^2\) aggregation.

No substantive proof correction was required. The result is an internal
pass for the stated **driven, first-order, all-forward and top-backward**
representation theorem. All lower backward fields, second-order rates,
autonomous closure, and an implementation-level peak-memory theorem remain
unproved here.
