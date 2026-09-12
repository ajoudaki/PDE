# Internal audit of the explicit short-horizon stability component

**Verdict: PASS for the stated conditional scalar stability component.**
The source cap, Gaussian tail bound, all three comparison coefficients,
and exact-arithmetic propagation calculation are correct under their stated
same-carrier, same-base, bounded-region hypotheses. No required correction
was found. This is not a complete C-H3 theorem, implementation certificate,
trajectory experiment, or promotion review.

Reviewer: `/root/h3_effective_route`, independently assigned this component
after freezing a separate effective-dictionary route. The reviewer did not
author or modify the two audited files. Prior work did include a coarser
short-time N19 calculation, which is disclosed rather than represented as
blind isolation from the mathematical topic.

## 1. Frozen inputs and read coverage

Every line of `H3_stability_proof.md` (124 lines) and `H3_stability.py` was read.
Applicable established dependencies were read completely: global nonlinear
A.3; C.4.7.3's statement and source equations N2–N8 and all of N9–N19;
the previously read, unchanged C.4.7.1–2 and C.4.7.4–5 give the canonical
model, raw completion, energy bounds, and finite-GF interpretation. III.F.1–10
had also been read in full before this subtask, including finite-union laws,
singular source coordinates, and the actual adjoint construction.
The long-time reference-transfer proof in the rest of C.4.7.3 is unnecessary
for the short-time cap and was not used in this component audit.

A coarse line-range read for A.3 accidentally included adjacent A.4 and the
opening of B.1 through line 2065. That adjacent text was not used, and this
exposure was reported to the coordinator before the verdict. No other study
or other reviewer's findings were accessed.

| Frozen input | SHA-256 |
|---|---|
| H3_stability_proof.md | a5a68240508b3601faddbc30005626c144190fe38d02d1291787ef3ebeb69735 |
| H3_stability.py | a59194db71e5b17fcd8a4884a0a5839a16c93007cd4e06dc65dbd1bb22bcf65d |
| docs/global_nonlinear.md | 947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161 |

The two candidate hashes were checked again after execution and were unchanged.
Pre-edit HEAD was `431deb3ca9b881abaffd57da5562a07e5406f273`; the shared index
was empty. The review changed only this assigned report and created the
authorized fresh generated reproduction directory. No Git operation modified
HEAD or the index.

## 2. Source-cap audit

The rational constants C and R strictly dominate `exp(2T)-1` and `exp(2T)`.
Every occurrence of these constants in N10–N19 is monotone on their
nonnegative domains, so substitution of the rational upper bounds is valid.
With `B=1/32`, the exact upper bound is

    Psi <= 0.030328853085402327 < 0.03125,
    B-Psi >= 0.0009211469145976715.

The causal induction is valid without an unproved current-row cap. At step k,
the lower w and its source derivatives use rows from steps below k. Those give
the current alpha and F density through N12–N14. In the upper recursion N8,
the current derivative has one direct source coordinate and all memory indices
are strictly earlier. N15–N16 therefore bound the new beta row with the already
known F density. The first beta row is zero because the initial readout is zero.
Thus the strict inequality closes the induction over any separately finite
positive-step program of total length at most T. Zero-mass atoms may be deleted;
no lower bound on positive masses, source rank, number of atoms, or step count
is used. A shorter final step treats affine interpolation times without changing
the constants. These are finite program statements, not a growing-width
program theorem.

The learned contribution to the backward response row is at most
`2 R C² T`: N5 contains `gamma_s E[Delta_k Delta_s]`, and
`sum |gamma_s|<=2RT`, `|E[Delta_k Delta_s]|<=C²`.
Since `|H1|<=1`, the response remainder has absolute bound
`D=B+2 R C² T=0.03125103040301`. The centered source variance is at most C²
by N3. This checks every factor in the decomposition `Q=G+J`.

## 3. Canonical tail passage and scalar Gaussian bound

The brief Gaussian-isometry passage in proof lines 39–43 is justified by the
finite-union source law. To spell out the needed argument, fix one input and
time and choose the finite-law/Euler approximants on the canonical carrier.
If their upper backward inputs are `Delta_j`, their centered reverse sources
can be realized consistently with

    E[G_j G_k]=E[Delta_j Delta_k],
    ||G_j-G_k||2=||Delta_j-Delta_k||2.

The first equality is the uncentered-input covariance rule applied to the
finite union of the two programs. Unused additional nodes have zero formal
named derivatives and do not alter an existing program's marginal law;
singular or duplicate nodes retain their formal source coordinates. Strong
convergence of `Delta_j` makes `G_j` Cauchy in L2. Its limit is centered
Gaussian: each real linear Gaussian combination has its characteristic
function determined by a converging covariance, in particular for the
single limiting coordinate. The variance bound passes. Since `Q_j` also
converges strongly, `J_j=Q_j-G_j` converges in L2; an almost surely convergent
subsequence preserves `|J|<=D`. This proves the marginal decomposition used
by the note. It does not assert any independence between G and J.

For completeness put `sigma²=E G²<=C²`. When sigma>0, write G=sigma Z on
the same marginal space with Z standard normal. Then

    |Q|<=C|Z|+D,
    {|Q|>r} subset {|Z|>(r-D)/C},  r>=D.

The function being bounded is nonnegative, so no independence is needed.
The variance-zero case obeys `|Q|<=D` and has zero tail for r>=D. For positive
variance, with `a=(r-D)/C`,

    E[Q² 1_{|Q|>r}]
      <= E[(C|Z|+D)² 1_{|Z|>a}]
      <= 2 exp(-a²/4) [2 sqrt(2) C²+sqrt(2) D²].

The last inequality uses `(p+q)²<=2p²+2q²`,
`1_{|Z|>a}<=exp((Z²-a²)/4)`, and Gaussian integration. Taking the square
root is safely bounded by `4(C+D) exp(-a²/8)`. The formula remains valid at
r=D. Thus the code's tail formula is an upper bound, with no tail estimate
for an approximate path assumed. Its reproduced value at r=1/5 is
`1.159625253499717e-16`, below the asserted `1e-15`.

All uniformity here is in the marginal time/input estimates with the
supremum outside expectation. The proof correctly avoids asserting the same
Gaussian bound for a random supremum of fields. Integrating the individual
L2 tail bounds against a probability law preserves their bound.

## 4. Sharp action constant and comparison coefficients

A.3 supports the canonical bound `||A0||<=2`. Its Gaussian-process comparison
has increment difference `2(1-alpha)(1-beta)>=0`; softmax interpolation gives
the stated expectation inequality. The contained Poincare argument gives
variance at most one for the unnormalized Gaussian matrix spectral norm,
and Chebyshev gives the displayed finite-width bound. Fixed-input norm
inequalities then pass to the generated dense span and extend to the
canonical action. No finite matrix is asserted to have norm at most two
deterministically.

Energy gives `||c(t)||infinity<=2t`. Since
`||K'||HS<=2 integral |r| ||Delta2||2 ||H1||2<=4t`, integration gives
`||K(t)||HS<=2t²`. Therefore the canonical path fits strictly within
`a=2.01`, `c=.02` through T. These estimates give no corresponding certificate
for an arbitrary supplied approximate path; the note states that restriction.

The four basic comparison bounds use the reference readout's supremum bound
only where a changed upper gate multiplies that readout. The approximate
readout needs merely its L2 bound. The row bound uses
`||Q_approx||2<=a c`; the middle bound uses the Hilbert–Schmidt identity for
a rank and two-factor differences. Since the two states share A0,
`||A-Aref||op<=||K-Kref||HS=k`. These facts verify the declared metric and
prevent a changed-base operator error from being hidden in k.

Independent collection of the three velocity inequalities gives:

| Error component | Row velocity | Middle velocity | Readout velocity |
|---|---|---|---|
| x | `2a²c²+4Rc a²+4Rs` | `2c²a+4Rc a+2Rc` | `2ca+2Ra` |
| k | `2ac²+4Rac+2Rc` | `2c²+4Rc` | `2c+2R` |
| z | `2ac+2Ra` | `2c+2R` | `2` |

Their column sums are exactly Lx,Lk,Lz in the proof and implementation.
The only tail term is `2R * 2 tau_s(Qref)=4R tau_s(Qref)`. The reproduced
values are

    Lx=5.53612824,
    Lk=2.368824,
    Lz=L=8.2608,
    4R=4.08.

For an absolutely continuous represented path, the sum-norm error has upper
derivative bounded by the sum of derivative differences. Adding its full RHS
defect b and integrating the resulting scalar differential inequality gives
the stated exponential formula. The supplied fixed parameters make L>0;
there is no division-by-zero case in the implemented budget routine.

The reproduced conditional terminal bound is
`5.1046964863380474e-8 < 5.2e-8` when b<=1e-5 and the initial error is zero.
This is a bound in the raw sum norm. Prediction and upper-hidden observation
bounds require the separately displayed factors, and arbitrary action tuples
require their own finite induction. No such observation errors were silently
identified with the raw norm.

## 5. Exact-arithmetic implementation and fresh execution

The exponential enclosure is correct. After the Taylor sum through n, the
first omitted term is `term_n*x/(n+1)`. Every subsequent term ratio is at most
`x/(n+2)<1`, so the geometric denominator gives an upper tail bound. `_down`
and `_up` perform exact directed rational rounding to a 256-bit dyadic grid.
Rounding down the partial sum preserves the lower bound; rounding up the sum
plus tail preserves the upper bound. Every source-cap occurrence of exp is
replaced by a certified upper bound at a nonnegative rational argument.

For the Gaussian tail, range reduction and repeated downward-rounded squaring
preserve a positive lower bound for exp(exponent). Dividing by that lower
bound therefore yields an upper tail estimate. The final budget uses an upper
bound for exp(LT); its multiplier and all other factors are nonnegative.
The asserted strict inequalities use Fraction comparisons only. Floating
conversions occur solely in reported displays and do not enter the premises.

The unmodified script was run once in the fresh directory

    data/generated/observable_hierarchy/H3_stability_reproduce_20260912_effective_01/

using Python 3.10.12, CPU affinity `{0}`, one numerical thread, an 8 GiB
address-space limit, and 55-second CPU/subprocess limits. The executed program
argument vector was

    python -B studies/observable_hierarchy/H3_stability.py --output data/generated/observable_hierarchy/H3_stability_reproduce_20260912_effective_01

The parent wrapper set affinity and resource limits before invoking that exact
script; it did not alter source or calculations. Exit status was 0. The script
recorded runtime `0.08097394928336143` seconds and peak RSS `16300` KiB, far
below the supplied 60-second, one-core, 8-GiB budget. No trajectory was run.

The complete exact rational results and environment metadata are in
`data/generated/observable_hierarchy/H3_stability_reproduce_20260912_effective_01/result.json`,
SHA-256 `f1f260ce292805e9c1ac21d2d7fefa8468173d42ec3e7df72a6f1df071dc89ce`.
Its recorded source hash equals the audited implementation hash above.

## 6. Exact limitations and disposition

The PASS covers a source/tail constant and a **conditional error-propagation
calculation** at T=.005,Y=1. It does not certify any path's RHS defect,
approximate action norm, readout bound, or initial error. It supplies no
Gaussian/population/input quadrature implementation, time integrator,
arbitrary-epsilon refinement algorithm, or useful feature dictionary.

The small-law radius and fixed active family remain existential in the H2
input; this component does not certify membership of a prescribed perturbed
law or a positive resolved hidden-learning signal. Its Euler source-cap lemma
has a broader finite-law scope, but that does not automatically expand every
other theorem in the study. The fixed cutoff also leaves a nonzero tail floor;
an arbitrary-accuracy theorem must choose and certify further cutoff values
and all its other error sources.

The canonical finite-GF interpretation remains the established width-limit
statement. The exact scalar script is not a finite-width error bound or a
population dynamics reproduction. Same-base and same-population coupling
requirements are essential. Promotion would require the separate repository
gates for a complete concrete addition; this internal audit supplies none of
those approvals.
