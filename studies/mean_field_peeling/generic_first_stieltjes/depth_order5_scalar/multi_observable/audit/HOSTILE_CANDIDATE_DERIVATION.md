# Superseded hostile candidate v1: forward-carrier aliasing failure

This candidate was frozen before either new producer recurrence was inspected.
It is **falsified and superseded** by `hostile_gamma04_derivation_v2.py`.

The first implementation reused the old four-forward-slot chaos and encoded the
new fresh fourth-jet innovation in slot 4, which was already the moving
third-jet innovation.  Its 82-term `Gamma_04` formula consequently inserted
spurious covariances and omitted the genuinely fresh fifth slot.  The corrected
five-slot route has 83 terms.  This file is retained as negative audit evidence;
none of its transition coefficients may be used.

Let `W_r` denote the ordinary `r`-th feature-ascent derivative of a hidden
weight matrix and let `X_r`, `Delta_r` denote moving feature and reverse jets.
Because

\[
 W_r=\sum_{a+b=r-1}{r-1\choose a}\Delta_aX_b^T,
 \qquad r\ge1,
\]

the fourth preactivation jet is

\[
 Z_4=W_0X_4+4W_1X_3+6W_2X_2+4W_3X_1+W_4X_0.
\]

After readout-parity removes odd-total feature covariances, the direct reverse
channels in `Z_4` are

\[
 (6\Gamma_{02}+8\Gamma_{11}+3\Gamma_{02})\Delta_1
 +\Delta_3
 =(9q02+8w)\Delta_1+\Delta_3.
\]

The transpose response of `W_0X_4` adds two scalar coefficients, so the local
normal form must have

\[
 Z_4=G_4+l41\,\Delta_1+l43\,\Delta_3,
 \quad l41=9q02+8w+a41,
 \quad l43=1+a43.
\]

The activation Bell polynomial is

\[
 X_4=\phi^{(4)}Z_1^4+6\phi^{(3)}Z_1^2Z_2
     +3\phi^{(2)}Z_2^2+4\phi^{(2)}Z_1Z_3+\phi^{(1)}Z_4.
\]

The three candidate outputs are

\[
 \Gamma_{04}^+=E[X_0X_4],\qquad
 a41^+=E[\partial_{E_1}X_4],\qquad
 a43^+=E[\partial_{J_3}X_4].
\]

The structural three-state argument above survives, but the v1 Wick table does
not.  The corrected independent derivation and hashes are in
`hostile_gamma04_derivation_v2.py` and `HOSTILE_CANDIDATE_V2_FREEZE.json`.
