# Preregistered experiment: diagonal loop erasure

**Frozen before execution:** 23 August 2026.

This experiment tests the newly isolated mechanism in
`CHARACTERISTIC_TANGENT_REDUCTION_2026-08-23.md`.  It cannot prove the
row-leverage lemma or change C-13 to proved.  Its purpose is to falsify the
mechanism cheaply if the purported off-diagonal bath itself develops width
growth, the diagonal return degenerates, or the natural cavity coordinate
loses the (n^{-1/2}) scale.

## 1. Exact diagnostics

Along the exact unclipped feature flow define

\[
 K_{2,\rm pre}=\|X_1\|_n^2I+G_1D_1^2G_1^*,\qquad
 Z_2'=K_{2,\rm pre}B_2.
\]

For every middle coordinate put

\[
 \kappa_{2,i}=(K_{2,\rm pre})_{ii},\qquad
 Y_{2,i}=Z_{2,i}'-\kappa_{2,i}B_{2,i},\qquad
 C_{2,i}=\frac{d'(Z_{2,i})}{d(Z_{2,i})}Y_{2,i}.
\]

At the top,

\[
 K_2=D_2K_{2,\rm pre}D_2,\qquad
 Z_3'=\{\|X_2\|_n^2I+G_2K_2G_2^*\}B_3.
\]

For a frozen uniform sample of output rows (i), compute exactly

\[
 \kappa_{3,i}=\|X_2\|_n^2+(G_2K_2G_2^*)_{ii},\quad
 Y_{3,i}=Z_{3,i}'-\kappa_{3,i}B_{3,i},\quad
 C_{3,i}=\frac{d'(Z_{3,i})}{d(Z_{3,i})}Y_{3,i}.
\]

For a removed initial middle column (j), run the paired exact cavity flow
and report

\[
 \sqrt n\|Z_2-Z_2^{(-j)}\|_n,
 \qquad
 \sqrt n\|\Theta(Z_2)-\Theta(Z_2^{(-j)})\|_n,
 \quad \Theta(z)=z+z^3/3,                               \tag{1.1}
\]

as well as the analogous top quantities.  The second statistic is the exact
finite-difference version of the characteristic tangent coordinate; no
linearization is used.

We also report the RMS of (C_2) on the largest one percent of coordinates
ranked by (|R_2|), divided by its unconditional RMS.  This is only a stress
diagnostic for same-row leverage, not an independence test.

## 2. Frozen design

- widths: (128,256,512,1024);
- four independent seeds at every width;
- feature horizon (S=2);
- RK4 step (0.01), checkpoints every (0.1);
- four uniformly sampled middle columns per seed for paired cavities;
- sixteen uniformly sampled top rows per seed for exact top diagonal returns;
- repeat widths (128,256) at step (0.005) for the solver audit.

The same raw initialization is shared only inside each prescribed cavity
pair.  Widths and seeds are otherwise independent.

## 3. Frozen interpretation

The result is **mechanistically supportive** only if all conditions hold:

1. every predictor-energy identity defect is below (10^{-4}), and every
   primary diagnostic changes by at most five percent under step halving;
2. the one-percent quantile of both (kappa_2) and the sampled (kappa_3)
   stays above (0.02) at every checkpoint and width;
3. for (p=2,4,6,8), the median compact-time values of
   (|Y_2|_{p,n}/p) and (|C_2|_{p,n}/p) change by at most a factor (1.5)
   from the smallest to largest width, and their log--log width slopes are at
   most (0.10);
4. the medians of every quantity in (1.1), after multiplication by
   (sqrt n), change by at most a factor (1.5) from width 128 to 1024 and
   have log--log slopes at most (0.10); and
5. the conditional (C_2)-leverage ratio has median below (4) and no
   log--log width slope above (0.10).

Evidence **against this proof mechanism** is recorded if a valid run has
either (i) an upper log--log slope above (0.25) for one of the bath moment
or rescaled cavity statistics at both horizons 1 and 2, (ii) a diagonal
return one-percent quantile tending toward zero with slope below (-0.25), or
(iii) a leverage ratio growing with slope above (0.25).  Anything between
the two precommitted verdicts is inconclusive.  Passing would still leave the
multi-cavity theorem unproved.
