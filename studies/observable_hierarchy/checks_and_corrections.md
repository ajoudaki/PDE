# C-H1 checks and corrections

Author: `/root`; no training experiments were run.

## Independent routes

The frozen prompt-only routes are `route_observable.md` and `route_weak.md`.
Both prove current observable-algebra reconstruction within their stated scope.
The first identifies the failure of naive unbounded response differentiation;
the second supplies a weak reverse-adjoint cutoff construction. Both leave
canonical initialization and reached invariance/uniqueness open in their prompt
scope. Neither is a complete C-H1 proof. The supervisor read both reports fully.

The assembled theorem uses a finite instruction alphabet with real scalar marks,
rather than arbitrary smooth functions as internal labels. It supplies the
canonical alternating Gaussian source construction and the restarted Euler
comparison proving flow invariance. It preserves the routes' negative evidence.
The concern about the information content of continuous marks is assigned a
separate internal representation audit and independent relevance selection.

## Static deterministic identity check

Source: `check_weak_identity.py`. This is a fixed five-coordinate deterministic
state, with a nonorthogonal three-input law, shared observation nodes, both
action orientations, nonlinear gates, a bounded product, moving readout and a
frozen seed. It compares the weak formula with two independent evaluations:
forward directional differentiation and central finite differences. It also
checks convergence of the explicit reverse cutoff at increasing scalar marks.
No optimization trajectory is run.

The initial static graph used a direct product of an action output with a bounded
field. Although the finite identity remained valid, this was outside the safe
alphabet. Before review it was corrected by applying tanh to the action output
before that product. The original output is retained as nonqualifying evidence
in `data/generated/observable_hierarchy/static_identity_v1/result.json`.
Only the corrected source and `static_identity_v2` qualify for the grammar check.

Command from the repository root:

```
python studies/observable_hierarchy/check_weak_identity.py data/generated/observable_hierarchy/static_identity_v2
```

Exit zero, Python 3.10.12 and NumPy 1.26.4. Corrected weak RHS:
`0.0008986674151865981`; forward derivative `0.0008986674151865992`;
central difference `0.0008986674071564947`. At cutoff 1024 the observed absolute
error is `3.1715168186986775e-10`. These are sanity checks, not proof of an
order-uniform cutoff rate or hierarchy convergence.

## Established reference constant certificate

The exact rational Python certificate in global_nonlinear C.4.5.1.5 was extracted
unchanged from the source and rerun. Its source is preserved verbatim in
`dependencies_v1.md`. Extracted script SHA256:
`112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e`.

Command:

```
python data/generated/observable_hierarchy/reference_certificate_v1/certificate.py
```

Exit zero. Output:
`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.
All exact rational assertions passed. The result is retained under
`data/generated/observable_hierarchy/reference_certificate_v1/`. It checks
constants in an established dependency, not a new empirical training claim.

## Candidate corrections before paired review

Version 1 is retained unchanged. Version 2 changes the Osgood expression
`log(e/v)` to `1+log(1/v)`, because the same paragraph used `e` for a distance;
the intended constant was Euler's number. This removes an ambiguity without
changing the argument. The internal weak reviewer independently flagged it.

Review status and exact frozen versions belong in the README and the full
review reports. Neither deterministic checks nor internal audits replace the
fresh complete isolated reviews required for promotion.

The concrete version-3 insertion is `candidate_v3.md`. Before freezing it,
the literal frozen-forward construction count was corrected from two to three
instructions (projection, tanh, action); the existing `3j` allowance already
covered this. Hierarchy order is now `j`, distinct from network width `n`.
Characteristic frequencies are counted explicitly: at most `4j` real marks
including frequencies, plus `j` circle marks. The canonical layer superscripts
remain `(1),(2),(3)` while equation labels are `(H1)`–`(H19)`. A transient
automated relabeling that touched layer superscripts was repaired before freeze.
The candidate introduces its overlap with existing C.4.2 explicitly and is
formatted as the exact proposed C.4.7.8 addition.

Full internal reports are `internal_weak_v1.md` and
`internal_representation_v1.md`. Their restricted source scopes and conditional
internal verdicts are preserved. The separate selector's original report is
`selection_v1.md`: accept for assembly in a narrow C.4.7.8 subsection, with a
short guide update. It is not a scientific paired review. The parent read all
three reports completely. The full version-3 neutral review assignment and
input hashes are `review_assignment_v3.md` and `review_inputs_v3.json`.
