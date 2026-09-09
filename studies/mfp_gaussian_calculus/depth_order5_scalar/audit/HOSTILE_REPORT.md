# Hostile audit: arbitrary fixed depth, unit Gram, order five

## Verdict

There are two distinct claims, and they have different verdicts.

1. **Full fixed-dimensional M-only scalar recurrence through order five:**
   **PASS.**  The six chronological scalar passes contain no Gaussian,
   covariance, response, tangent, derivative operator, pseudoinverse, or
   hidden 66-state IR.  Their exact expansions agree with every frozen
   coefficient of the accepted H=2,3,4 maps.
2. **The particular one-forward/one-backward normal form requested in the
   prompt:** **NOT SATISFIED.**  The audited witness has the causal order
   F1/R1/F2/R2/F3/R3.  No compression of these six passes to a single forward
   state followed by a single backward state has been supplied, and no
   impossibility theorem for such a compression has been proved.

Thus the order-five M-only closure claim is no longer open, but the stronger
two-sweep compactness claim remains open.  It would be inaccurate either to
call the six-pass witness the requested two-sweep recurrence or to infer from
the six-pass dependency obstruction that no two-sweep recurrence can exist.
The concrete dependency chain is `F2 <- R1`, `R2 <- F2`, `F3 <- R2`, and
`R3 <- F3`; merely concatenating the 14 forward-oriented and 15
reverse-oriented coordinates does not remove those causal dependencies.

The hostile contract was frozen at SHA-256
`f356a1c448ae38dc572bed1630d4f007b3690fa3da8d68db1c9d7a0ef5bc66c3`
before either full producer was inspected.

## 1. Frozen formulas and exact map comparisons

Route A froze its complete analytic transition tables and separately written
depth assembler under manifest SHA-256
`0699148b5d5fcd77a821908f333e230e36e148afad710e2421c36ab89c7441f8`.
Route S froze its complete candidate under SHA-256
`d731ec66b067b8739df305426c6aa6d06bbc309d5fd624bd16d1c283ca649728`.

The accepted maps were independently loaded and canonicalized under the
pre-frozen hashes in `FROZEN_REFERENCE_MANIFEST.json`.  Exact rational
comparison gives:

| depth | A terms / discrepancies | B terms / discrepancies | C terms / discrepancies |
|---:|---:|---:|---:|
| 2 | 3 / 0 | 46 / 0 | 974 / 0 |
| 3 | 4 / 0 | 160 / 0 | 6,519 / 0 |
| 4 | 5 / 0 | 350 / 0 | 17,641 / 0 |

The separately written Route A and Route S depth assemblers also agree
atom-for-atom at H=1,2,3,4 for each of

`A, B, C, S5, AC, Bm2, m2norm, Am3`.

That comparison is useful but must not be overstated: Route S reused Route
A's already-frozen *moving* local transition tables.  It is an independent
chronological assembler/canonicalizer, not a second independent derivation of
those local Wick contractions.  The decisive evidence is instead the full
Route A analytic derivation plus the independently frozen accepted H=2,3,4
maps and independent canonical loader.  The exact audit JSON has SHA-256
`432f8b66c6607bec84221e21281b7346dcb56e50cb64feae8ea5dd4ee00399dd`;
the cross-assembler comparison has SHA-256
`6fe8a825ea25727da79744c3cf556719a7a98c92e4754fffe6871cac1a106113`.

## 2. Literal grammar and honest state census

The public transition roots are finite polynomials in rational integers,
one-dimensional `M_nu` atoms, `b_l=d^(H-l)`, `tau_(l-1)`, and previously
computed deterministic scalars.  A literal scan of all 38 roots finds 39
distinct M-atom types, exactly six exponent slots per atom, maximum derivative
slot five, and no forbidden object or operator.

The six propagated state dimensions are

| pass | F1 | R1 | F2 | R2 | F3 | R3 |
|---|---:|---:|---:|---:|---:|---:|
| dynamic scalars | 7 | 8 | 4 | 4 | 3 | 3 |

Hence there are 14 forward-oriented and 15 reverse-oriented dynamic
coordinate types, 29 total.  Route S reports 30 because it retains the known
coordinate `B00=b`; Route A substitutes this deterministic power of `d` and
does not propagate it.  In addition, later passes/cache contractions use five
R1 source outputs, three R2 source outputs, and one R3 source output per layer,
plus four order-five terminal accumulators.  These caches are stated rather
than hidden.  No minimality claim is made.

As in the order-three precedent, per-layer states must be retained or
recomputed for later reverse passes.  The number of coordinate *types* and
the transition grammar are independent of H, but this is not a constant-
memory or constant-total-work claim.

## 3. Tensor identity and closure of all six families

Let `p=grad f`, `A=Hp`, `B=T[p,p]`, `m2=D^2p=B+HA`, and
`m3=D^3p`.  The exact finite-width identity used by the recurrence is

\[
D^5f=2V[p^5]+10\langle A,U[p^3]\rangle
+10\langle B,m_2\rangle+4\|m_2\|^2
+12\langle A,m_3\rangle.
\]

Expanding `m2` and `m3` gives the audited six-family identity

\[
\begin{aligned}
D^5f={}&2V[p^5]+22U[Hp,p,p,p]+14T[T[p,p],p,p]\\
&+30T[H^2p,p,p]+36T[Hp,Hp,p]+16\|H^2p\|^2.
\end{aligned}
\]

The earlier 7-forward/9-backward frozen sector closed only the first three
families and had C discrepancies 857, 5,795, and 15,612 at H=2,3,4.  The
F2/R2/F3/R3 passes close exactly the three formerly unresolved families;
the full recurrence has zero discrepancies.  There is therefore no surviving
peeling branch in the six-pass formulation.

The full finite-width product-rule, equality-partition, free-width-sum,
transpose-response, and inverse-free Wick--Stein census is recorded in the
independent analytic report frozen at SHA-256
`ed657dc149e9a1b1f5c9acb267e381b11e2556e42d7d7aad9f12fd099b6af8f1`
under report-manifest SHA-256
`1418ab4edfb24ead8bc53b6a09bf49df6d6cd56eaf0edb7c67cc3c8c0c126914`.
Its six exhaustive leading local cases have net width power zero; an extra
same-type equality loses a free index sum and is subleading.  The strict
earlier-layer ranges retain every transpose response before Wick--Stein
elimination.

The terminal contraction is

\[
\boxed{
A_H=\tau_H,\qquad
B_H=2S_{3,H}+4\mathcal H_H,\qquad
C_H=2S_{5,H}+10AC_H+10Bm2_H+4M2_H+12Am3_H.}
\]

It follows algebraically that

\[
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}.
\]

This audit does not infer positivity, a Stieltjes measure, or convergence of
the Pad\'e series from those two definitions.

## 4. Lower-order projection and derivative ceiling

The recurrence gives `A_H=tau_H=1+d+...+d^H`.  Its projected order-three
transition roots `V`, `P`, `J3`, `B11`, and `K10` agree symbolically with
Section 7.1, each with zero discrepancies, rather than merely reproducing a
few terminal values.

Finite differentiation through order five uses only `phi,...,phi^(5)`.  In
the Wick-Stein elimination, pairing a forward innovation with the base
activation raises the activation derivative while consuming the innovation's
positive time grade; total grade is at most five.  The three eliminators also
fail explicitly if a branch tries to create `phi^(6)`.  No such branch occurs,
and independent scans of the frozen outputs give maximum derivative slot
exactly five.  Thus every terminal atom is a declared one-dimensional
`M_(nu0...nu5)`.

## 5. Parity, controls, and empirical regression

Readout reflection is an exact finite-width argument.  Under readout sign
flip, `f -> -f` and `D -> -D`, hence

\[
\mathbb E f_n=\mathbb E D_n^2f_n=\mathbb E D_n^4f_n=0.
\]

Exact substitutions in the unit-Gram maps give:

* constant one: `(A,B,C)=(1,0,0)` at H=2,3,4;
* deep linear: `(3,48,1464)`, `(4,160,13888)`, and
  `(5,400,73240)` at H=2,3,4;
* normalized affine `phi=(1+x)/sqrt(2)`:
  `(7/4,31/4,615/8)`, `(15/8,12,13447/64)`, and
  `(31/16,479/32,179193/512)`.

The canonical unnormalized quadratic does not preserve unit forward Grams.
Its accepted values are therefore a companion check of the layer-tagged /
arbitrary-Gram maps, not a substitution into this unit quotient:

| H | A | B | C |
|---:|---:|---:|---:|
| 2 | 111 | 1,685,184 | 77,400,633,120 |
| 3 | 14,175 | 139,445,032,896 | 4,298,284,752,832,899,360 |
| 4 | 138,351,807 | 59,385,566,223,611,232,192 | 81,427,352,525,619,060,193,821,492,876,576 |

The preregistered normalized-sine finite-width regression used all 7,700
networks.  H=3 has `z=1.2002`, `p=0.4026`; H=4 has `z=0.4749`,
`p=0.3647`.  Both frozen gates pass.  This is empirical corroboration, not
part of the algebraic proof.

## 6. Annealed theorem scope

Exact finite-width fifth-order identities need `phi in C^5` and sufficient
integrability; polynomial growth of derivatives through order five is a safe
finite-algebra envelope.  This alone does not identify the annealed limit.

For each separately fixed H, a sufficient theorem-level hypothesis is

\[
\phi\in C^\infty,\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r})\quad\text{for every }r\ge0.
\]

The finite jet is then a finite NETSOR-transpose-plus program.  Setup 3.6 and
Theorem 3.7 of Golikov--Yang, *Non-Gaussian Tensor Programs*, supply
convergence in every finite `L^p` in this strong tier, hence `L^1`
convergence of `D_n^k f_n` for `k=1,3,5` and the annealed coefficients.
Under only convergence in probability, the separate sufficient bridge is,
for some `epsilon>0`,

\[
\sup_n\mathbb E|D_n^k f_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\},
\]

which gives uniform integrability.  No claim is made for H growing with
width, depth-uniform bounds, positive training time, arbitrary batch size, or
an all-orders expansion.

## 7. Publication-integrity replay: resolved

The initially generated composite had duplicated/malformed preamble text.
That finding is resolved by the clean canonical document
`ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md`, frozen at SHA-256
`24d9f63d79319b514969c0e1fe85608721f4c4033615810c93157631c3a30f12`
under manifest SHA-256
`6753aa7af1a11b962c3fe52dc54abbe9eaa8c49fac32a07cc887ea768844e3c1`.

The final publication replay parsed its 38 displayed transition formulas and
compared them literally with all three frozen transition JSONs: 38 expected,
38 embedded, zero missing, zero extra, and zero unequal.  Required claim-
scope markers are present, including the explicit six-pass closure and open
two-sweep compression.  The deterministic `run_checks` replay additionally
returned C counts 974/6,519/17,641, zero discrepancies at all three depths,
derivative ceiling five, passing cross-assembler sectors, and the passing
normalized-sine gate.  The canonical document is therefore publication-
integrity **PASS** in its frozen bytes.
