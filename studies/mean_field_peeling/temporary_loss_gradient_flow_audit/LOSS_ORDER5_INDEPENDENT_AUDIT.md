# Independent audit of the loss order-five formula

## Verdict

The pullback algebra, every temporal coefficient through order five, the
quadratic/cubic reduction, and the integral remainder in
`LOSS_ORDER5_AND_MESH_STATUS.md` pass.

The result is a fixed-step width-first jet theorem only under the stated
regularity and OMFP-intertwining hypotheses.  It supplies no uniform
continuous-time theorem without an activation-envelope-derived bound on the
sixth derivative or, preferably, the state-level reachable stability bound.

## Algebra check

With

\[
 U_h=I+A_h,\qquad A_h=\sum_{k\ge1}h^kT_k,
\]

the binomial theorem is valid because there is one operator `A_h`:

\[
 [h^m]U_h^N
 =\sum_{r=1}^m{N\choose r}
 \sum_{k_1+\cdots+k_r=m}T_{k_1}\cdots T_{k_r}.
\]

Therefore

\[
 q_{m,r}(t)={2t\choose r}-2^m{t\choose r}.
\]

Independent rational expansion of this expression reproduces every entry
of the rows `m=2,3,4,5` in the main note.

## Low-order contraction check

Let

\[
 A=\|\nabla f\|^2,qquad
 C=D^3f[g,g,g],qquad
 H=\|Dg[g]\|^2,
\]

and use the initialization parity `D^2f[g,g]=0`.  Direct differentiation of
`P=f-f^2/2` and `ell=1/2-P` gives

\[
\begin{array}{lll}
 \Lambda_{2,1}=A^2/2,&\quad&\Lambda_{2,2}=2A^2,\\
 \Lambda_{3,1}=-C/6,&&
 \Lambda_{3,2}=-2A^3-3C/2-2H,\\
 &&\Lambda_{3,3}=-4A^3-2C-4H.
\end{array}
\]

Contracting these values against the audited `q` rows yields

\[
 [h^2]D_t^\ell=tA^2,
\]

\[
 [h^3]D_t^\ell
 =-{t(2t-1)\over2}(4A^3+C+4H),
\]

with the same sign and fine-minus-coarse orientation as the main note.

## Remainder and claim boundary

Taylor's theorem gives

\[
 R_{6,t}(h)
 ={h^6\over5!}\int_0^1(1-s)^5
 (D_t^\ell)^{(6)}(sh)\,ds
\]

provided the paired scalar map is `C^6` on the entire segment.  Fixed-`t`
regularity does not bound this integral uniformly when `t` grows like
`1/h`.  Width-first use additionally requires direct population-DAG
regularity and uniform integrability; finite-width Taylor expansion cannot
be interchanged with width.  Hard ReLU/leaky-ReLU are outside the `C^6`
hypothesis and require the separately open boundary calculus.

