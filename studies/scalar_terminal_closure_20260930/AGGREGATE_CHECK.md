# Independent check of the scalar aggregate route

Checked candidate: `AGGREGATE_ROUTE.md`, SHA256
`ce370ab7be96c212925a28850280ace8621d91ab94d846bba07947eb7593f33b`.
Checker: `/root/scalar_information`, 2026-09-30. The candidate was read in
full after the independent information route had been frozen and the supervisor
had authorized within-study comparison. Scientific inputs were this candidate
and the exact model in the study README/current manuscript. No other study,
archived book, or other review was read. Only this report was written.

**Verdict: the aggregate identities, loss-third-derivative formula, and scoped
same-source Gram obstruction pass this independent algebra check.** There is
one local inaccurate/ambiguous sentence concerning first derivatives and one
field-list clarification to make before reusing the statement. Neither changes
the proved loss separation. This is an internal research check, not promotion
or an initialized-q=1 impossibility result.

## 1. Exact residual and dissipation formulas

Differentiating the reconstruction gives precisely candidate (1). Contracting
`B hdot_a` with `d_a` uses

    <d_a,B[(1-h_a^2) odot ell_b]>=<ell_a,ell_b>,

so candidate (3) has the correct factors, index order `K_ba`, and sign of the
clock drift. Multiplying it by `2r_a/m` and summing gives candidate (5):
`U^2-<X,Y>` is the sum with `D_ab K_ba`, and `<X,Z>` is the sum with
`r_a V_ab(H_ba-K_ba)`. The coefficient `rho/(2 tau)` inside its bracket is
correct. Cauchy--Schwarz proves Proposition 1, including `U=0`.

The generator factor in (9) also checks: `u^T r=m rho`, so its rank-one term
is exactly `rho b`. It is not a positive-semidefinite identity. In the
width-one example, `B'=(-1/2-1/4)+(1/8)4=-1/4`, hence the stated positive
loss derivative `3/16` is correct. This example requires no statement about
reachability, which the candidate explicitly does not make.

## 2. Independent reconstruction of the third derivative

At candidate (11), put `s=1-h^2`, `t=s^2 odot h`,
`c_a=(Cy)_a/m`, and retain the candidate's normalized pairings. The identities
`B^T w=0`, `B h=0`, and `<w,v>=-1` follow directly from
`W0^T w=h` and `v=-W0 h/H`.

The exact first and second derivatives needed for the check are

    B'=2 w tensor h,
    g'_a=2 y_a H w,
    ell'_a=2 W s odot h,
    f'_a=y_a a,              a=2WH,
    h''_a=4W c_a t,
    w''=4H w,
    d''_a=4H w-8H^2 w^3,
    k''_a=0,                k'''_a=h''_a/tau.

Here `h'_a=k'_a=w'=d'_a=0`. For example, the lower-layer derivative follows
by differentiating `hdot_a=-(2/m) sum_b r_b C_ab s_a odot ell_b` once,
using `ell_b=0` and `r_b=-y_b`. The displayed `k'''` retains the physical
clock; differentiating `k'=(rho/tau)(h-k)` twice leaves only `h''/tau` at
this state.

Let `R_ab=G_ab+C_ab E_ab+D_ab K_ba`, so the residual equation is
`r'=-2Rr/m+rho V(H-K)/(m tau)`, with the stated index contractions.
At the state,

    R=WH y y^T, R'=0, r'=ay, r''=-a^2 y.

Direct product differentiation gives exactly the candidate's second derivatives

    G''_ab=8 y_a y_b H^2 W,
    E''_ab=8 W^2 S,
    D''_ab=8HW-16H^2 M4,
    K''_ba=4W y_b c_a S,
    (H_ba-K_ba)''=4W y_a c_b S.

The six contributions to `F'''=(1/m) sum_a y_a r'''_a` are as follows:

| Source | Contribution |
|---|---:|
| `-2R r''/m` | `a^3` |
| `G''` | `16H^2W` |
| `C odot E''` | `16 beta W^2 S` |
| `D'' K` | `16H^2W-32H^3 M4` |
| `D K''` | `8 beta W^2 S` |
| clock-memory term | `-4 beta W S/tau` |

The memory contribution uses `V_ab=-y_b` and
`sum_b y_b c_b/m=beta`. Its other product-rule terms vanish because `H-K`
and its first derivative vanish. Their sum is exactly candidate (15):

    F'''=a^3+32H^2W+beta(24W^2-4W/tau)S-32H^3 M4.

Finally, differentiating `L=mean_a(f_a-y_a)^2` three times gives

    L'''=mean_a[6 f'_a f''_a+2(f_a-y_a)f'''_a]
         =-6a^3-2F''',

which verifies (16). The memory-clock contribution is indispensable to the
leading small-amplitude separation.

**Local correction.** The sentence “All first derivatives of these six arrays
vanish” should be replaced by a specific list. The five arrays whose second
derivatives are displayed have zero first derivatives, and `H'` is also zero.
But if “six arrays” means the six originally defined arrays
`H,K,G,D,E,V`, it is false:

    V'_ab=<d'_a,v_b>+<d_a,v'_b>=2 y_b W.

This omitted nonzero derivative does not affect (15), for the product-rule
reason just given. Recommended wording: “The first derivatives of
`G,E,D,K,H-K` vanish. Although `V'_ab=2y_bW`, it gives no contribution because
`H-K` and its first derivative vanish.”

## 3. Exact paired-rotation check

For the width-two source in (17),

    W0^(-1)=(2I-Q)/3,
    w/alpha=((2-1/sqrt(2))/3,-1/(3sqrt(2))),
    Qw/alpha=((sqrt(2)-1)/3,sqrt(2)/3).

Thus, writing `c=(5-2sqrt(2))/18` and `d=(4sqrt(2)-5)/108`,

    W=c alpha^2,
    Delta S=alpha^4/2-3alpha^6/8,
    Delta M4=d alpha^4.

Substitution gives the stronger exact polynomial identity

    Delta F''' = -(2 beta c/tau) alpha^6
                 +beta[12c^2+3c/(2tau)] alpha^8
                 -[9 beta c^2+4d] alpha^10.

Since beta,c,tau are positive, this proves (18) and strict separation for all
sufficiently small positive alpha. The constants in the static W and fourth-
moment computations were also checked with exact rational arithmetic in
`Q(sqrt(2))` using Python's standard-library `Fraction`. An attempted optional
SymPy check was unavailable because SymPy was not installed; no package was
installed. No ODE integration or training experiment was used.

## 4. Source symmetry, robustness, and precise nonclosure scope

For a fixed invertible W0 with simple singular values, paired singular-vector
sign transformations satisfy `P W0=W0 Q`. Orthogonality then also gives
`W0^T P=Q W0^T`. Consequently every legal linear word maps transformed lower
fields by Q and upper fields by P, with final orthogonal factors cancelling
in same-population pairings. The reconstructed B transforms as `P B Q^T`.
The candidate's same-source assertion therefore holds, including both true
adjoint orientations.

At the explicit source, the singular values are 3 and 1; its spectral
projectors, hence the chosen P and Q, vary continuously on a neighborhood.
For a fixed sufficiently small alpha, the nonzero derivative gap and the
strict gate-domain bounds persist there. A finite Gaussian matrix law has
strictly positive density on that open neighborhood. This justifies the
claimed open-set source robustness. It supplies no lower probability bound
uniform in width. Embedding as a block at a larger fixed width changes the
normalizing constants but leaves a nonzero leading term; perturbation works
when the additional singular values are distinct and nonzero.

**Field-list clarification.** The preserved pairwise contractions are those
of the list later specified in the candidate:

    lower: h_a, k_a, ell_a; upper: g_a, d_a, v_a, w,

and their compatible linear words in W0,W0^T,B,B^T. The corresponding
`X,Y,Z` tensor Gram is preserved as well. “All current typed pairwise Grams”
should not be read as allowing arbitrary extra coordinatewise fields or
untransformed fixed test vectors. For example adding the lower gate
`1-h^2` to the dictionary can reveal the fourth moment through its squared
norm, and the constant-one vector is not generally transformed by Q.
A deterministic PSD factorization computed solely from the equal arrays
adds no information; a factor deliberately chosen using unretained neuron
coordinates would be a different encoding. With this precise list, the
proposition's indistinguishability argument is valid.

The input assumption is explicitly positive-definite C with m<=d. It admits
generic correlated data but does not cover every rank-deficient dataset.
The current states have finite coordinates and are valid points of the
q=1 vector field. Nothing checked here places them on the zero-readout,
zero-memory Gaussian initialized trajectory. Their label-aligned hidden
responses and specially selected readout/memory may be unreachable. The
candidate repeatedly states that restriction, so its conclusion is a
current-state Gram obstruction, not an initialized-trajectory lower bound,
not a population-limit obstruction, and not a proof against richer scalar
approximations.

## 5. Final check status

No error was found in (1)-(18), the strict local loss separation, or the
conditional dissipation certificate. The local derivative sentence should
be corrected and the preserved field list should accompany any abbreviated
statement of Proposition 2. The requested `o(epsilon^-2)` scalar approximation
and its all-time status remain open exactly as the candidate says. In
particular, this check provides no source approximation rate, fitting theorem,
population identification, or reachable-state obstruction.

## Addendum: verification of the targeted amendment

Amended candidate SHA256:
`8158b5301d68a71da0dcff3db16336c2c18f5efff7fa355ba83285496c6bb1d5`.
The original checked version and findings above remain recorded unchanged.

The amended scope now names lower fields `(h,k,ell)` and upper fields
`(g,d,v,w)` and explicitly excludes arbitrary additional coordinatewise gates
and fixed test vectors. The derivative passage now lists the arrays with
vanishing first derivatives and states `V'_ab=2y_bW`, explaining why its
product-rule contribution vanishes. These changes resolve both issues raised
in this check. The exact formulas and the qualified current-state conclusion
are unchanged. The amended candidate passes the bounded internal check with
no outstanding correction from this report.
