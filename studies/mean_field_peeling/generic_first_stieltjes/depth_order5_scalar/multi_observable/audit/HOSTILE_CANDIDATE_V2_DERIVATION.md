# Corrected independent five-slot `Gamma_04` candidate

This derivation was frozen before producer-formula inspection.  It repairs the
explicit carrier-aliasing failure preserved in the v1 note.

The exact parameter product rule gives

\[
 W_r=\sum_{a+b=r-1}{r-1\choose a}\Delta_aX_b^T,
\]

and hence, after parity,

\[
 Z_4=G_4+(9\Gamma_{02}+8\Gamma_{11}+a_{41})\Delta_1
          +(1+a_{43})\Delta_3.
\]

Here `G4` is a genuinely new fifth forward-Gaussian coordinate, distinct from
the four coordinates already present in the order-five moving contraction.
Applying the fourth activation Bell polynomial and contracting

\[
 E[X_0X_4],\quad E[\partial_{E_1}X_4],\quad
 E[\partial_{J_3}X_4]
\]

with an independently implemented five-slot Wick--Stein reducer produces the
state

\[
 (\gamma04,a41,a43)_0=(0,0,0),
 \quad l41=9q02+8w+a41,\quad l43=1+a43,
\]

and canonical transition counts `83/20/1`.  The complete explicit formulas are
the deterministic stdout of `hostile_gamma04_derivation_v2.py`; their code and
output hashes are frozen in `HOSTILE_CANDIDATE_V2_FREEZE.json`.

This proves only an independent formal candidate.  Promotion still requires
the equality/width/transpose ledger, exact cross-route atom comparisons,
controls, regression, and the annealed-limit boundary in the hostile contract.

