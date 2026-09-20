# Independent reflected-three-input route

Status: exact reduction, a proved finite-time exit from the positive-residual
cone, and a finite interpolation certificate. No unconditional exponential
potential is proved. The cone-exit result rules out one proof mechanism; it
does not rule out exponential convergence of the actual flow.

This scoped route used only the supervisor's model and initialization and the
exact coefficient target in `docs/observable_p1.md`. It did not read the
study's previous proofs or other studies. No simulation was run.

## Model and genuinely three-point family

Write normalized inputs as

\[
u_0=e_1,\qquad u_\pm=(\delta,\pm s),\quad
s=\sqrt{1-\delta^2},\qquad 0<\delta<1.
\]

The physical data are \((\sqrt2u_+,1)\), \((\sqrt2u_-,1)\),
and \((-\sqrt2u_0,-1)\), with weights \(1/4,1/4,1/2\).
These are three distinct inputs with no antipodal pair. The label map has two
classes. Oddness of both hidden activations gives \(f(-u)=-f(u)\) for every
state, so the last fitting equation is exactly \(f(u_0)=1\). This identity
does not make either of the other two inputs redundant with the last one.

Let

\[
L_1=(\nu+\eta)^{-1/2},\quad L_2=(\tau+\eta)^{-1/2},\quad
b_1=L_1\tanh g_1,\quad b_2=L_2\tanh(\sqrt\nu Z),
\]

and let \(m_0=M(0)>0\) be the exact coefficient specified in the assignment.
The upper mark \(b_2\) has a symmetric law whose density is positive on
\((-L_2,L_2)\). The populations remain separate.

The flow preserves the following lower-population identities:

\[
w_1(g_1,-g_2)=w_1(g_1,g_2),\quad
w_2(g_1,-g_2)=-w_2(g_1,g_2),\quad w(-g)=-w(g).
\]

It also preserves \(c(-Z)=-c(Z)\). To verify the lower reflection, substitute
the reflected state into the vector field: the two equal-weight, equal-label
inputs \(u_+,u_-\) exchange, while \(u_0\) stays fixed. For simultaneous
lower-mark negation, \(b_1\) and \(w\) both negate, the lower gates stay
unchanged, and the velocity negates. The upper identity follows because each
upper activation negates with \(b_2\). The identities hold initially and are
therefore preserved by uniqueness of the given flow. In particular,
\(a(u_+)=a(u_-)=B\), while we write \(a(u_0)=A\).

Define

\[
h_A(b)=\tanh(bMA),\quad h_B(b)=\tanh(bMB),\quad
F_i=E_2[c h_i],\quad e_i=1-F_i\quad (i=A,B).
\]

The exact loss is

\[
\mathcal L=\frac12(e_A^2+e_B^2).
\]

There are two independent fitting constraints, \(F_A=F_B=1\), on this
reflection-invariant trajectory. The equality between the two reflected
predictions comes from the initialized flow's symmetry, not from an
architectural identity valid at every state.

## Exact reduced equations and kernel

Put

\[
q_0=\operatorname{sech}^2w_1,\quad
q_\pm=\operatorname{sech}^2(\delta w_1\pm s w_2),
\]
\[
\Psi_A=b_1q_0e_1,\qquad
\Psi_B=\frac{b_1}{2}(q_+u_++q_-u_-),\qquad
J_{ij}=E_1[\Psi_i\cdot\Psi_j].
\]

The symmetrized \(\Psi_B\) is the gradient of \(B\) on the preserved
reflection subspace. Set
\(d_i=E_2[b_2c\operatorname{sech}^2(b_2Ma_i)]\), with \(a_A=A,a_B=B\).
The physical factors in the assignment give exactly

\[
\dot c=e_Ah_A+e_Bh_B,\qquad
\dot M=e_Ad_AA+e_Bd_BB,
\]
\[
\dot w=M(e_Ad_A\Psi_A+e_Bd_B\Psi_B),
\]
\[
\dot A=M(e_Ad_AJ_{AA}+e_Bd_BJ_{AB}),\qquad
\dot B=M(e_Ad_AJ_{AB}+e_Bd_BJ_{BB}).
\]

In particular

\[
J_{AB}=\frac\delta2 E_1[b_1^2q_0(q_++q_-)]>0,
\qquad J_{AA},J_{BB}>0
\]

at every finite state. The positivity uses \(0<\delta<1\), positive tanh
gates, and the positive measure of \(b_1\ne0\).

For \(i,j\in\{A,B\}\), define

\[
K_{ij}=E_2[h_ih_j]+d_id_j(a_ia_j+M^2J_{ij}).
\]

Differentiating the two predictions gives the closed residual equation with
state-dependent coefficients

\[
\dot e=-K e,\qquad
\dot{\mathcal L}=-e^TKe
=-E_1|\dot w|^2-E_2|\dot c|^2-\dot M^2.
\]

This is an exact equation along the full moving population state. It is not
an autonomous two-dimensional closure, since \(K\) depends on that state.

## The positive-residual cone necessarily ends in finite time

**Proposition.** For every \(0<\delta<1\), starting from the prescribed
initialization, there is a finite first time \(T\) at which \(e_A(T)=0\).
At this time \(e_B(T)>0\) and \(\dot e_A(T)<0\). Until \(T\), both
errors are nonnegative, \(M,A,B\) are nondecreasing, \(A>B>0\), and
\(c\) has the sign of \(b_2\). Thus the actual trajectory exits the
nonnegative-error cone transversely through the larger prediction's face.

Proof. Initially

\[
A_0=L_1\nu,\qquad
B_0=L_1E[\tanh g_1\tanh(\delta g_1+s g_2)],
\qquad 0<B_0<A_0.
\]

For completeness, for \(u>0\) and any \(v\), the identity

\[
\frac{\tanh(u+v)+\tanh(u-v)}2
=\tanh u\frac{1-\tanh^2v}{1-\tanh^2u\tanh^2v}
\]

places this symmetric average strictly between zero and \(\tanh u\),
with equality in the upper bound only if \(v=0\). Apply this after fixing
\(|g_1|>0\), pairing the two signs of \(g_2\), and taking \(u=\delta|g_1|\).

Consider any interval on which \(e_A,e_B\ge0\). Starting with
\(M=m_0>0\), \(A>B>0\), and \(c=0\), the readout equation makes
\(b_2c\ge0\). It is strictly positive off \(b_2=0\) at every positive
time in that interval. Thus \(d_A,d_B\ge0\), and the displayed equations
for \(A,B,M\) give their monotonicity. On the half-population \(g_1>0\),
\(b_1>0\), and

\[
\dot w_1=Mb_1\left(e_Ad_Aq_0+
\frac\delta2 e_Bd_B(q_++q_-)\right)\ge0,
\]
\[
\dot w_2=\frac{s}{2}Mb_1e_Bd_B(q_+-q_-).
\]

When \(w_1,w_2\ge0\), one has
\(|\delta w_1+s w_2|\ge|\delta w_1-s w_2|\), hence \(q_+\le q_-\).
The inequality reverses when \(w_2\le0\), and the second velocity vanishes
at \(w_2=0\). Therefore

\[
w_1\ge g_1>0,\qquad |w_2|\le|g_2|\quad(g_1>0).
\]

The other half follows by the preserved symmetries. The same tanh identity
then proves

\[
A-B\ge E_1\left[|b_1|
\{\tanh|w_1|-\tanh(\delta|w_1|)\}\right]>0.
\]

These sign and ordering statements close by continuity for the entire
nonnegative-error interval.

We now give uniform quantitative bounds on that interval. Write

\[
S(t)=\int_0^t(e_A+e_B)\,dr,\quad
h_*(b)=\tanh(bm_0B_0),\quad \kappa=E_2 h_*^2>0.
\]

Since both positive upper preactivation scales \(MA,MB\) are at least
\(m_0B_0\), integration of the readout equation gives

\[
|h_*(b)|S(t)\le |c(b,t)|\le S(t),\qquad
F_B(t)\ge\kappa S(t).
\]

The cone has \(F_B\le1\), so \(S\le\kappa^{-1}\). Using
\(|a_i|\le L_1\), \(|d_i|\le L_2S\), and \(|\Psi_i|\le L_1\),
integration with respect to the nondecreasing variable \(S\) yields

\[
M(t)\le m_0+\frac{L_1L_2}2S(t)^2\le\bar m,
\qquad \bar m=m_0+\frac{L_1L_2}{2\kappa^2},
\]
\[
\sup_g|w(g,t)-g|
\le L_1L_2\left(\frac{m_0}2S(t)^2+
\frac{L_1L_2}{8}S(t)^4\right)\le R,
\]
\[
R=\frac{L_1L_2m_0}{2\kappa^2}
 +\frac{(L_1L_2)^2}{8\kappa^4}.
\]

Let \(p=P(1\le|G|\le2)>0\). On this event,
\(1\le |w_1|\le2+R\), and

\[
\tanh|w_1|-\tanh(\delta|w_1|)
=\int_{\delta|w_1|}^{|w_1|}\operatorname{sech}^2v\,dv
\ge(1-\delta)\operatorname{sech}^2(2+R).
\]

Consequently the explicit constant

\[
\Gamma=pL_1\tanh(1)(1-\delta)\operatorname{sech}^2(2+R)>0
\]

satisfies \(A-B\ge\Gamma\) throughout the cone. For \(b>0\),
the upper tanh derivative on the relevant interval is bounded below by
\(\operatorname{sech}^2(L_1L_2\bar m)\), so

\[
h_A(b)-h_B(b)\ge b m_0\Gamma
\operatorname{sech}^2(L_1L_2\bar m).
\]

By upper oddness, the corresponding absolute-value inequality holds at
negative \(b\). Hence

\[
F_A-F_B\ge\chi S,
\]
\[
\chi=m_0\Gamma\operatorname{sech}^2(L_1L_2\bar m)
E_2[|b_2||h_*(b_2)|]>0.
\]

Since \(e_B=e_A+(F_A-F_B)\), we have \(S'=e_A+e_B\ge\chi S\).
Also \(F_A,F_B\le S\), so \(S'\ge2-2S\), and thus
\(S(t)\ge1-e^{-2t}\) as long as the cone persists. If it persisted to
\(t_0=\tfrac12\log2\), then \(S(t_0)\ge1/2\), after which
\(S(t)\ge\tfrac12e^{\chi(t-t_0)}\). This contradicts
\(S\le\kappa^{-1}\). In particular its exit time is no greater than

\[
\frac{\log2}{2}+\frac1\chi\log\frac2\kappa.
\]

At every positive cone time, \(c\) has strict sign \(b_2\) and \(A>B\),
so \(F_A>F_B\), or \(e_A<e_B\). The first cone boundary is therefore
\(e_A=0<e_B\). At that boundary,

\[
\dot e_A=-K_{AB}e_B<0,
\]

because \(E_2h_Ah_B>0\), and both other contributions to \(K_{AB}\)
are nonnegative there. This proves the proposition.

The explicit bound is only a finite-time certificate; its constants are very
small or large and are not advertised as useful numerical estimates.

## Finite interpolation exists; the obstruction is not expressivity

Keep \(w=g\) and \(M=m_0\) fixed for this construction. Let
\(G_{ij}=E_2[h_ih_j]\), with \(A=A_0>B=B_0>0\). The two functions
\(h_A,h_B\) are linearly independent in \(L^2(P_2)\). Indeed a vanishing
linear combination on this population vanishes on an interval by continuity;
its linear and cubic Taylor coefficients at \(b=0\) give

\[
v_A(m_0A)+v_B(m_0B)=0,\quad
v_A(m_0A)^3+v_B(m_0B)^3=0.
\]

The determinant is nonzero because \(A>B>0\). Thus
\(D=G_{AA}G_{BB}-G_{AB}^2>0\). The explicit bounded readout

\[
c_* =\frac{G_{BB}-G_{AB}}D h_A
      +\frac{G_{AA}-G_{AB}}D h_B
\]

satisfies \(E_2[c_*h_A]=E_2[c_*h_B]=1\), and therefore fits all three
original examples exactly at a finite admissible state.

Since \(h_A>h_B>0\) on \(b>0\), the inequalities
\(G_{AA}>G_{AB}>G_{BB}\) hold. Moreover any odd readout that fits both
constraints at such ordered positive \(A,B,M\) must change sign relative
to \(b\): if \(bc\ge0\) almost everywhere and the output is nonzero,
then \(E[c(h_A-h_B)]>0\), contradicting equality of the two outputs.
For the displayed \(c_*\), the sign change is exactly once on \(b>0\).
To check this, \(h_B/h_A\) is strictly increasing in \(b>0\), because
\(x/\sinh x\) is strictly decreasing. The ratio at which \(c_*\) changes
sign is the weighted average

\[
\frac{G_{AB}-G_{BB}}{G_{AA}-G_{AB}}
=\frac{E[h_A(h_A-h_B)(h_B/h_A)]}
       {E[h_A(h_A-h_B)]},
\]

strictly between the endpoint values of that ratio. Thus \(c_*\) is
negative for sufficiently small positive \(b\) and positive for larger
positive \(b\). No such claim has yet been proved for the trained readout.

## What would suffice for an exponential state potential

At any state with \(M>0\) and \(A>B>0\), the same independence proof
makes the readout Gram \(G\) positive definite. Since \(K-G\) is a sum
of Gram matrices, \(K\succeq G\). If the actual trajectory were proved to
stay in a set with fixed constants

\[
0<m_*\le M\le m^*,\qquad B\ge b_*>0,\qquad A-B\ge\gamma_*>0,
\qquad A\le L_1,
\]

then continuity and compactness would give
\(\lambda_*:=\min\lambda_{\min}G>0\). The state potential
\(\Phi=\mathcal L\) would then satisfy

\[
\dot\Phi\le-2\lambda_*\Phi,\qquad
\mathcal L(t)\le\mathcal L(0)e^{-2\lambda_*t}.
\]

The finite-time cone proof establishes such bounds only until its necessary
exit. Extending the necessary nonvanishing and separation bounds after that
exit is an open obligation, not a conclusion of this route.

Finally, exponential loss itself would force a finite limiting state. From
the energy identity and \(\mathcal L(0)=1\),
\(|M(t)|\le m_0+\sqrt t\) and \(\|c(t)\|_2\le\sqrt t\). The exact
equations then bound

\[
\|\dot c\|_\infty\le2\sqrt{\mathcal L},\quad
|\dot M|\le2L_1L_2\sqrt t\sqrt{\mathcal L},\quad
\|\dot w\|_\infty\le2L_1L_2(m_0+\sqrt t)\sqrt t\sqrt{\mathcal L}.
\]

All three bounds are integrable if \(\mathcal L\le Ce^{-\lambda t}\).
Thus saturation by unbounded displacement cannot secretly realize a claimed
exponential result. If the ordered lower sector and positive \(M\) survive
to that finite limit, the readout must acquire a sign change relative to
\(b_2\). A proof that assumes both perpetual readout positivity and that
ordered sector cannot produce the requested exponential potential.

## Weaker cones after the first overshoot

The following calculations test weaker hypotheses; they do not assert that
the actual trajectory remains in any of these regions.

Suppose at a state that \(M>0\), \(A>B>0\), and \(b_2c\ge0\), and write
\(e_A=-q e_B\), with \(e_B>0\). If \(0\le q\le B/A\), then

\[
\dot c=e_B(h_B-qh_A)
\]

has the sign of \(b_2\). This follows from the strict decrease of
\(\tanh z/z\) for \(z>0\). Also \(d_B\ge d_A\ge0\), so

\[
\dot M=e_B(Bd_B-qAd_A)\ge e_B B(d_B-d_A)\ge0.
\]

This weaker residual-ratio condition therefore protects readout positivity
and connector growth at the instant under consideration. It does not by
itself protect the lower sign sector. At a boundary point \(g_1>0,w_1=0\),
the normal velocity is

\[
\dot w_1=Mb_1e_B\left[-q d_A+
\delta d_B\operatorname{sech}^2(sw_2)\right].
\]

For \(q d_A>0\), this is negative at sufficiently large \(|w_2|\).
Thus a proposed invariant cone based only on these inequalities fails the
vector-field boundary test. This is an obstruction to that cone argument,
not a proof that the specified trajectory crosses the lower boundary.

There is an exact accumulated-force criterion that identifies what additional
control would protect the lower sector. Define

\[
P(v)=\frac v2+\frac{\sinh(2v)}4,\qquad
I_A(t)=\int_0^t M(r)e_A(r)d_A(r)\,dr.
\]

Since \(P'(v)=\cosh^2v\), the first-coordinate equation gives

\[
\frac{d}{dt}P(w_1)
=b_1M e_A d_A+
\frac{\delta b_1}2 M e_Bd_B\frac{q_++q_-}{q_0}.
\]

Whenever \(M e_Bd_B\ge0\) throughout the interval, for \(g_1>0\) this
implies

\[
P(w_1(g,t))\ge P(g_1)+b_1 I_A(t).
\]

Therefore the scalar inequality \(I_A(t)\ge-1/L_1\) protects
\(w_1(g,t)>0\) for every \(g_1>0\): the right side is at least
\(P(g_1)-\tanh g_1>0\). The last inequality follows from
\(P'(v)=\cosh^2v\ge1\) and \(g_1>\tanh g_1\).

Conversely, the same threshold is necessary to protect all lower marks.
At each fixed finite horizon the energy estimate and the equations give a
finite uniform bound on \(w-g\). For fixed \(g_1\) and \(|g_2|\to\infty\),
the gates \(q_\pm\) therefore vanish uniformly on that horizon, and the
first-coordinate solution converges to \(W\) satisfying

\[
P(W(g_1,t))=P(g_1)+b_1 I_A(t).
\]

One may justify this limit directly in the integral equation by the uniform
gate bound and the Lipschitz continuity of the remaining axial vector field
on the bounded first-coordinate range. Now
\(P(g_1)/b_1\to1/L_1\) as \(g_1\downarrow0\). If
\(I_A(t)<-1/L_1\), the right side is negative for all sufficiently small
positive \(g_1\). At sufficiently large finite \(|g_2|\), the actual
\(w_1\) is then negative too. Continuity supplies a positive-measure set
of such marks. Under \(M e_Bd_B\ge0\), the threshold consequently gives
an exact necessary-and-sufficient criterion for this pointwise sign sector
at a given time.

The missing step is a lower bound for \(I_A\) along the trained trajectory,
or a different argument that controls \(A-B\) after that pointwise sector
fails. Neither follows from dissipation alone. Within the region
\(M>0,A>B>0,b_2c\ge0\), the face \(e_B=0>e_A\) has
\(\dot e_B=-K_{AB}e_A>0\); hence the smaller prediction's error cannot
exit through that face while this region lasts. This protects \(e_B\),
but leaves readout sign, connector sign, and feature separation unresolved.
