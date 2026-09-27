"""Exact compiler acceleration for the frozen selective zero-boundary model.

Only final-row generation changes. A necessary additive signature (decoration
counts and vertex counts by layer) rejects children absent from the retained
set before graph grafting/canonicalization. Every surviving proposal still
uses the original exact graft and coefficient combination. Selection, tree
ordering, initial values, runtime coefficients, penalties and ODE are unchanged.
The count of skipped raw proposals is reported separately; the number of fully
combined omitted terms is deliberately not claimed without generating them.
"""
from __future__ import annotations
from collections import defaultdict
from true_aggregate_ode import flatten, graft, degree
from true_aggregate_selective import SelectiveClosure


class FastSelectiveClosure(SelectiveClosure):
    def __init__(self,*args,**kwargs):
        if kwargs.get('boundary','zero')!='zero':
            raise ValueError('Exact signature prefilter supports zero boundary only')
        self._fast_compiling=False
        super().__init__(*args,**kwargs)

    def _prepare_signatures(self):
        n=len(self.colors)
        self._color_units=[1<<(16*i) for i in range(n)]
        self._layer_units=[1<<(16*(n+i)) for i in range(2)]
        self._signature_cache={}
        self._selected_signatures={self._signature(tree) for tree in self.trees}
        self._replacement_signatures={col:[(c,key,tr,self._signature(tr)-self._layer_units[tr[0]]) for c,key,tr in terms] for col,terms in self.local.items()}
        self._fast_signature_ready=True

    def _signature(self,tree):
        cached=self._signature_cache.get(tree)
        if cached is not None:return cached
        nodes,_=flatten(tree)
        # Counts are tiny in this retained family. The explicit guard prevents
        # any radix carry from invalidating the necessary-condition test.
        if len(nodes)+sum(len(decs) for _,decs in nodes)>=65536:
            raise ValueError('Tree exceeds exact radix-65536 signature capacity')
        value=sum(self._layer_units[layer]+sum(self._color_units[col] for col in decs) for layer,decs in nodes)
        self._signature_cache[tree]=value
        return value

    def derivative(self,tree,max_degree=None):
        # During construction/selection and after compilation this remains the
        # full public exact derivative; only frozen selected rows are filtered.
        if not (self._fast_compiling and hasattr(self,'boundary_rows')):
            return super().derivative(tree,max_degree)
        if not self._fast_signature_ready:self._prepare_signatures()
        out=defaultdict(float);parent_signature=self._signature(tree)
        nodes,_=flatten(tree)
        for vertex,(_,decorations) in enumerate(nodes):
            for color in sorted(set(decorations)):
                count=decorations.count(color)
                removed_signature=parent_signature-self._color_units[color]
                for coefficient,key,pattern,replacement_signature in self._replacement_signatures[color]:
                    self._raw_proposals+=1
                    if removed_signature+replacement_signature not in self._selected_signatures:
                        self._signature_rejected+=1
                        continue
                    if max_degree is not None and degree(tree)-1+degree(pattern)>max_degree:
                        continue
                    self._graft_proposals+=1
                    out[key,graft(tree,vertex,color,pattern)]+=coefficient*count
        return [(coefficient,key,child) for (key,child),coefficient in out.items() if coefficient!=0]

    def compile(self,max_states=100000,max_terms=1000000,seconds=60.):
        self._fast_signature_ready=False
        self._raw_proposals=0;self._signature_rejected=0;self._graft_proposals=0
        for name in ('boundary_rows','boundary_recipes'):
            if hasattr(self,name):delattr(self,name)
        self._fast_compiling=True
        try:super().compile(max_states,max_terms,seconds)
        finally:self._fast_compiling=False
        candidate_omitted=self.report['omitted_terms']
        self.report.update(compiler='exact additive-signature prefilter',
            signature_radix=65536,raw_derivative_proposals=self._raw_proposals,
            signature_rejected_raw_proposals=self._signature_rejected,
            exactly_grafted_raw_proposals=self._graft_proposals,
            combined_nonretained_signature_candidates=candidate_omitted,
            omitted_terms=None,full_derivative_terms=None,
            unresolved_boundary_terms=None,unresolved_fraction_of_omitted_terms=None,
            omitted_count_note='All missing children remain zero. Raw signature-rejected proposals are counted; fully combined omitted terms are not generated or counted.',
            runtime_equations_changed=False)
        return self


def compile_selective(u,labels,k=4,order=1,queries=None,mark_bound=3.,dependency_depth=0,augment_outputs=True,boundary='zero',preserve_essential=True,output_depth=1,max_states=100000,max_terms=1000000,seconds=60.):
    return FastSelectiveClosure(u,labels,k=k,order=order,queries=queries,mark_bound=mark_bound,dependency_depth=dependency_depth,augment_outputs=augment_outputs,boundary=boundary,preserve_essential=preserve_essential,output_depth=output_depth).compile(max_states,max_terms,seconds)

compile_selective_fast=compile_selective
