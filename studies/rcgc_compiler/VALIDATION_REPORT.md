# Compiler validation report

**Date:** 2026-08-24  
**Command (from repository root):**
`python -m unittest studies.rcgc_compiler.test_rcgc_compiler`

**Result:** six tests passed

The executable compiler reproduces the following ladder without
model-specific branches beyond the declared identity
\(\phi''\equiv0\):

| activation/depth | parameter/kernel terms | emitted curvature classes |
|---|---:|---|
| identity, every tested fixed depth \(1,2,3,7\) | \(H+1\) | none |
| generic nonlinear, \(H=1\) | 2 | local diagonal |
| generic nonlinear, \(H=2\) | 3 | local + \(2^-2^+\) |
| generic nonlinear, \(H=3\) | 4 | local + \(2^-2^+\) + \(2^-3^-3^+2^+\) |

For nonlinear \(H=3\), the nested term is emitted as

\[
 D_1G_2^*D_2G_3^*E_3G_3D_2G_2D_1.
\]

This validates the exact curvature recursion and the syntactic location of
the first multi-colour return. It does not validate its width degree,
limiting law, or mesh-uniform control; those remain analytic obligations.
