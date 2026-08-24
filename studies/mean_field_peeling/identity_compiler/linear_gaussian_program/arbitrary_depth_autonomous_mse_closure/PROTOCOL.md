# Protocol: arbitrary-depth autonomous linear-MSE closure

Status: frozen before the proof attempt, then audited on 20 August 2026.
The protocol remains the target contract.  C1, C3, and C4 were proved; C2
and therefore C5 remain conditional for hidden depth `L>=3`.  See
`CANONICAL_NOTE.md` for the current claim boundary.

## Model

`L >= 1` is the number of trainable hidden layers and is fixed before the
width limit.  For one unit-normalized input, identity activation, equal width
`n`, and one scalar label, use

\[
 f_{n,L}=n^{-(L+1)/2}v_L^T W_{L-1}\cdots W_1v_0,
\]

where an empty matrix product is understood when `L=1`.  Every raw entry is
independent standard Gaussian at initialization and every raw parameter is
trained by

\[
 \dot\Theta=-\eta n\nabla_\Theta (y_\star-f_{n,L})^2.
\]

The limit is width first, uniformly on compact intervals of physical MSE
time.  Depth is not sent to infinity.

## Frozen meaning of compression

Two meanings of `O(1)` must not be conflated.

1. **Width/order compression (required):** the number of evolving fields and
   source objects is independent of `n`, physical time, and requested Taylor
   order.  A fixed countable path domain and an integral kernel on it are
   admissible.
2. **Uniform-depth computational cost (not required):** memory and work stay
   bounded as `L -> infinity`.  This stronger property is not claimed.

The desired arbitrary-fixed-depth result may use a source whose graded path
space depends on `L`.  It should nevertheless be expressible as one block
source operator and an O(1) list of evolving objects.

## Non-vacuity conditions

An admissible closure must be:

1. autonomous and restartable from its current state;
2. in physical MSE time rather than only feature-ascent time;
3. initialized by a deterministic source fixed once `L` is given;
4. independent of a growing moment or derivative hierarchy;
5. equipped with the direct readouts `f=y_star-e` and `loss=e^2`;
6. identified with finite-width Gaussian muP dynamics on positive compact
   time intervals, rather than only matched coefficient by coefficient.

## Claim ladder

- C1: normalization converts the finite-width muP flow into ordinary
  gradient flow of a multilinear chain.
- C2: Gaussian Wick words converge to a deterministic rooted-path source,
  whose fixed edge operators act by creation plus immediate annihilation.
- C3: one block operator built from those edge sources gives a closed
  autonomous Hilbert-space ODE/coordinate IDE for every fixed `L`.
- C4: the limit system is globally well posed, has the exact loss identity,
  and drives every nonzero scalar residual exponentially to zero.
- C5: finite-width output, feature kernel, and loss converge to those
  readouts uniformly on each compact physical-time interval.
- C6: at `L=2` the path closure is equivalent to the previously proved
  scalar spectral IDE; for `L>=3` the natural source is noncommutative.

## Falsifiers and hostile checks

The proposed result fails if any of the following occurs:

- an omitted factor of `n` makes even one layer update vanish or diverge;
- the proposed block-operator derivative does not equal the full feature
  kernel;
- path multiplication needs an unrecorded history variable;
- the Gaussian-word error survives at positive time although it vanishes for
  every fixed word;
- finite-width trajectories escape the bounded region needed for the
  word-to-ODE stability argument;
- `L=1` does not reduce to the bilinear closed form or `L=2` does not recover
  the known initial kernel `K(0)=3`;
- a scalar spectral measure is claimed for noncommuting depth sources without
  a simultaneous-reduction proof.

## Proof route and claim boundary

The primary route is the rooted Gaussian-word/path basis followed by a
compact-time Picard--Gronwall argument.  The conserved-balancedness route is
used only as a no-go audit for a naive scalar spectral generalization.

The 2024 Chizat--Colombo--Fernandez-Real--Figalli paper rigorously proves the
one-middle-matrix case and displays the same path construction for arbitrary
many middle matrices.  Its arbitrary-depth section explicitly calls those
arguments formal.  Therefore that paper is supporting provenance, not by
itself a proof of C5 here.  The fixed-`L`, one-sample Gaussian word lemma and
the positive-time stability step must be supplied explicitly.
