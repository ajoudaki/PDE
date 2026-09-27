"""Complete dependency balls around every aggregate feedback/output seed.

The only approximation parameter here is ``depth``.  The seed set contains
every F, s, t constituent and every exact dot-s constituent.  Each expansion
adds every exact derivative child of every retained moment.  Missing children
are zero.  Runtime, initialization and the exact compiler signature filter
are inherited unchanged; no population evolves.

See NEXT_BOUNDARY_ROUTE.md for the bounded-mark convergence argument and its
limitations.  In particular finite-depth input-alias consistency is not
claimed, and the theorem does not certify practical low-depth accuracy.
"""
from __future__ import annotations

from true_aggregate_selective_fast import FastSelectiveClosure


class DependencyClosure(FastSelectiveClosure):
    def __init__(self, *args, depth=1, **kwargs):
        if isinstance(depth, bool) or int(depth) != depth or depth < 0:
            raise ValueError("Dependency depth must be a nonnegative integer")
        fixed = dict(dependency_depth=int(depth), augment_outputs=False,
                     preserve_essential=False, output_depth=0, boundary="zero")
        for key, value in fixed.items():
            if key in kwargs and kwargs[key] != value:
                raise ValueError(f"Complete dependency family requires {key}={value!r}")
            kwargs[key] = value
        super().__init__(*args, **kwargs)

    def compile(self, max_states=100000, max_terms=1000000, seconds=60.):
        # The shared compiler may hit a seed-selection cap before it normally
        # defines this field.  Initialize it here so the original cap survives
        # in the report instead of becoming an AttributeError.
        self.essential_trees = []
        super().compile(max_states=max_states, max_terms=max_terms, seconds=seconds)
        self.report.update(
            selection="complete dependency ball around F, s, t and dot-s constituents",
            family="complete_feedback_dependency",
            depth=self.dependency_depth,
            protected_gram_rows=False,
            finite_depth_alias_consistency_claim=False,
            bounded_mark_family_convergence="conditional theorem in NEXT_BOUNDARY_ROUTE.md; exact/controlled initialization and fixed finite queries",
            empirical_accuracy_claim=False,
            compile_seconds_is_hard_cap=False,
            compile_limit_note="Inherited cooperative budget checks; caller must impose any constructor-inclusive hard wall limit.",
        )
        return self


def compile_dependency(u, labels, k=4, order=1, queries=None, mark_bound=3.,
                       depth=1, max_states=100000, max_terms=1000000, seconds=60.):
    return DependencyClosure(u, labels, k=k, order=order, queries=queries,
        mark_bound=mark_bound, depth=depth).compile(
            max_states=max_states, max_terms=max_terms, seconds=seconds)
