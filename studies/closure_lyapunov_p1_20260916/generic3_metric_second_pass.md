# Mixed loss/feature barriers: second pass of the metric route

Status: frozen 2026-09-16. The original independent pass remains in
`generic3_metric_route.md` and is not rewritten. This pass began only after
the supervisor supplied the following new result: distinct nonzero upper
tanh coefficient vectors modulo sign give independent ridge functions;
after absorbing labels into those vectors, readout stationarity forces
fitting unless a signed coefficient vanishes or two signed coefficients
are opposite. The supervisor also supplied the bounded-state subsequence
consequence. These are explicitly post-freeze inputs, not discoveries
claimed by the original independent route.

The active target remains convergence below every positive loss tolerance
for every permitted generic unit-labelled triple; horizons may depend on
geometry. No convergence counterexample is asserted. A potential may combine
different geometry terms; none of its individual distances needs to be
monotone. No computation or other agent was used in this pass.

**Outcome.** A loss sublevel gives a quantitative mixed exclusion of the
entire incompatible-coefficient set, weighted by the current readout norm.
This allows arbitrary individual distance fluctuations. It prevents
approach to that set if the readout is bounded. Exact radial balance
identities and the energy bound do not yet prove the missing boundedness
or prevent loss-persisting escape. The requested unconditional convergence
statement is still open after this bounded pass.

## 1. Clarification of the first-pass comparison quantity

The proved first-pass capture theorem is valid as stated. Its expression

\[
 \sqrt{\mathcal L(t)}+
 I\!\left(2\int_{t_0}^t\sqrt{\mathcal L(s)}\,ds\right)
\]

is an **auxiliary comparison quantity, not a function of the declared
saved state**. Accumulated residual is not supplied by that state. It
therefore does not satisfy the user's requirement for the proposed
state-only potential. It is permitted only inside the proof of the
conditional reached-state theorem, without adding memory to the closure.
Replacing the integral by a current displacement is not justified: the
established direction of comparison bounds displacement above by
accumulated residual and does not give the reverse control needed for
the capture argument.

## 2. A mixed loss barrier excluding incompatible coefficients

The canonical order-one upper marks have odd raw coordinates
`Z=(tanh xi_1,tanh xi_2)`, with independent `xi_i~N(0,v_0)`.
Put `tau=E[tanh^2(sqrt(v_0)G)]>0`, so `E[ZZ^T]=tau I_2`.
On the exactly preserved canonical mark-parity subspace, write

\[
 H_i=\tanh(Z\cdot v_i),\qquad
 \widetilde v_i=y_iv_i,\qquad
 m_i=y_if_i=E_2[c\tanh(Z\cdot\widetilde v_i)].
\]

The raw-coordinate definition incorporates the canonical upper Cholesky
factor: `v_i` is the odd part of `M a_i`, divided by `sqrt(tau+eta)`.
This uses the canonical simultaneous mark reversal proved in the supplied
C.4.7.10.C.1 source, not a symmetry imposed on the three directions or a
change of dictionary. It places no restriction on their orientation.

Let `C=||c||_2`. Since tanh is 1-Lipschitz and vanishes at zero,

\[
 |m_i|\le C\|\tanh(Z\cdot\widetilde v_i)\|_2
       \le C\sqrt\tau\,|\widetilde v_i|.               \tag{1}
\]

Oddness and the same Lipschitz estimate give

\[
 \begin{aligned}
 |m_i+m_j|
 &\le C\|\tanh(Z\cdot\widetilde v_i)
                     +\tanh(Z\cdot\widetilde v_j)\|_2\\
 &\le C\sqrt\tau\,|\widetilde v_i+\widetilde v_j|.
 \end{aligned}                                                   \tag{2}
\]

If `L<=ell<1/3`, then `sum_i(m_i-1)^2<=3ell`. In particular

\[
 m_i\ge1-\sqrt{3\ell}>0,\qquad
 m_i+m_j\ge2-\sqrt{6\ell}>0.                           \tag{3}
\]

The second estimate follows from
`|(m_i-1)+(m_j-1)|<=sqrt(2[(m_i-1)^2+(m_j-1)^2])`.
Combining (1)–(3) proves the simultaneous mixed barriers

\[
 \begin{aligned}
 C\sqrt\tau\,|\widetilde v_i|&\ge1-\sqrt{3\ell},\\
 C\sqrt\tau\,|\widetilde v_i+\widetilde v_j|
                         &\ge2-\sqrt{6\ell}\quad(i\ne j).
 \end{aligned}                                                  \tag{4}
\]

No term in (4) is claimed to be monotone. The product of readout size and feature separation is the
controlled object. Once a trajectory enters this loss sublevel it stays
there by the exact energy identity, so (4) holds at every later time.
If `C` is bounded, it gives a uniform positive distance from every
zero-vector and opposite-vector stratum of the bad set. Equal signed
vectors are allowed, as required by the supervisor's characterization.

At the exact bad set the thresholds are sharper and need no readout
bound: `vtilde_i=0` forces `m_i=0` and `L>=1/3`; an opposite pair forces
`m_j=-m_i` and

\[
 \mathcal L\ge\tfrac13\{(m_i-1)^2+(-m_i-1)^2\}
              =\tfrac23(m_i^2+1)\ge\tfrac23.             \tag{5}
\]

Thus crossing `1/3` would exclude actual bad states forever. The missing
point is asymptotic approach with increasing `C`, or coefficient escape
through increasing `M`; (4) alone does not exclude either.

## 3. Exact radial balance identities and their remaining sign

A natural attempt to bound `C` couples its radial size to the middle
matrix. The exact identities make the possible cancellation visible.
Set

\[
 \Psi(z)=\tanh z-z\operatorname{sech}^2z.
\]

With `z_i=b_2^TMa_i` and `s_i=w.u_i`, the exact equations give

\[
 \begin{aligned}
 \frac d{dt}\|c\|_2^2
    &=-\frac43\sum_i r_iE_2[c\tanh z_i],\\
 \frac d{dt}\|M\|_F^2
    &=-\frac43\sum_i r_iE_2[c z_i\operatorname{sech}^2z_i],\\
 \frac d{dt}\|w\|_2^2
    &=-\frac43\sum_i r_iE_1[q_i s_i\operatorname{sech}^2s_i].
 \end{aligned}                                                   \tag{6}
\]

For the middle line, contract `M'` with `M` and use
`d_i^T M a_i=E[c z_i sech^2 z_i]`. For comparison with the lower line,
actual transpose gives `d_i^T M a_i=E_1[q_i tanh s_i]`.
Subtracting proves

\[
 \begin{aligned}
 \frac d{dt}(\|c\|_2^2-\|M\|_F^2)
       &=-\frac43\sum_i r_iE_2[c\Psi(z_i)],\\
 \frac d{dt}(\|M\|_F^2-\|w\|_2^2)
       &=-\frac43\sum_i r_iE_1[q_i\Psi(s_i)].
 \end{aligned}                                                   \tag{7}
\]

These are genuine mixed-block identities and preserve all canonical
normalizations. The nonlinear remainders do not vanish. Differentiation
gives `Psi'(z)=2z sech^2(z)tanh(z)`, hence `Psi` is odd, has the sign
of `z`, and satisfies

\[
                 |\Psi(z)|\le\tfrac23|z|^3.              \tag{8}
\]

For (8), integrate `|Psi'(z)|<=2|z|^2` from zero, using
`|tanh z|<=|z|` and `sech^2 z<=1`. The multipliers `r_i c` in the
upper identity and `r_i q_i` in the lower one have no pointwise signs
provided by the current argument. The three residuals also mix in the
sums. Therefore neither difference in (7) has been proved constant or
monotone. Claiming a balancedness invariant by importing the linear
activation identity would omit precisely these terms.

Small current upper coefficients make their individual remainders cubic,
but this does not control the other samples' remainders or simultaneous
growth of the readout. The present estimates do not convert (7) into a
coercive mixed state potential. This is a gap of this attempted invariant,
not a refutation of the user's proposed broader class of mixed potentials.

## 4. What energy actually excludes about escape

Let `theta=(w,M,c)` in the exact raw Hilbert metric. The canonical energy
identity gives `integral_0^infty ||theta'||^2<=1`. Hence

\[
 \|\theta(t)-\theta(0)\|\le\sqrt t.
\]

More sharply, for any fixed `T<t`, Cauchy–Schwarz on the tail gives

\[
 \frac{\|\theta(t)-\theta(0)\|}{\sqrt t}
 \le\frac{\|\theta(T)-\theta(0)\|}{\sqrt t}
     +\left(\int_T^\infty\|\theta'(s)\|^2ds\right)^{1/2}.
\]

First take the limsup as `t->infinity` and then `T->infinity`. The tail
integral tends to zero, proving

\[
        \|w(t)-g\|_2+\|M(t)-D\|_F+\|c(t)\|_2
                         =o(\sqrt t).                  \tag{9}
\]

This improves the crude polynomial growth bounds but still permits
unbounded growth. For example a scalar speed `1/(1+t)` is square
integrable while its integral is unbounded; this elementary comparison
only explains the logical limitation of an energy estimate and is not
a proposed canonical trajectory or convergence counterexample.

Combining (4) and (9), after any verified crossing below `1/3`, excludes
bad-set approach faster than the reciprocal of the actual readout norm.
It does not exclude approach at that reciprocal scale. The identities
(7) have not supplied the additional sign or integrability that would
rule it out.

## 5. Frozen conclusion and precise unresolved bridge

The new information is the mixed loss barrier (4), the exact nonlinear
balance defects (7), and the unconditional sub-square-root escape bound
(9). They neither require nor imply monotonicity of individual
same-label or opposite-label distances.

To obtain the requested finite horizon for every positive tolerance using
the supervisor's stationary characterization, this route still needs an
argument excluding loss-persisting escape and incompatible coefficient
limits. No proof here ensures crossing the `1/3` loss threshold, bounds
`c,M` uniformly, or rules out their slower escape. These are substantive
unresolved conditions, not automatic consequences of initial rank,
finite energy, or the conditional capture theorem. The latter remains a
valid way to finish once a concrete reached state passes its test.
