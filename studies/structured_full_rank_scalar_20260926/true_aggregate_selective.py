"""Experimental sparse observable selection using the exact tree generator.

This is separate from the complete degree-R closure in true_aggregate_ode.py.
All F,s,t and every exact dot-s constituent are retained. By default every
immediate child of the output derivative is also retained. Optional dependency
expansion adds all exact children a fixed number of times. For final selected
rows, every missing child is explicitly set to zero. No convergence or accuracy
guarantee is asserted for this selection/boundary. State remains scalar current
contractions plus L; no sampled block evolves.
"""
from __future__ import annotations
import json
from pathlib import Path
import time
from collections import deque
import numpy as np
from true_aggregate_ode import Closure, CompileLimit, canonical, degree, node, flatten


class SelectiveClosure(Closure):
    def __init__(self,*args,dependency_depth=0,augment_outputs=True,boundary="zero",preserve_essential=True,output_depth=1,**kwargs):
        # Parent's degree9 constraint ensures its exact feedback construction;
        # this subclass never applies that degree as a retained-set rule.
        kwargs['degree']=9
        super().__init__(*args,**kwargs)
        self.boundary=boundary
        if boundary not in ("zero","current_gate_product"):raise ValueError("Unknown boundary")
        self.dependency_depth=int(dependency_depth)
        self.augment_outputs=bool(augment_outputs)
        self.preserve_essential=bool(preserve_essential)
        self.output_depth=int(output_depth)
        if self.output_depth<0:raise ValueError("Nonnegative output depth required")
        if self.dependency_depth<0:raise ValueError('Nonnegative dependency depth required')

    def compile(self,max_states=100000,max_terms=1000000,seconds=60.):
        started=time.monotonic();full_terms=0;retained_terms=0;omitted_terms=0
        self.trees=[];self.tree_ids={};self.rows=[];self.compiled=False
        def add(tree):
            tree=canonical(tree)
            if tree not in self.tree_ids:
                if len(self.trees)>=max_states:raise CompileLimit('state_limit')
                self.tree_ids[tree]=len(self.trees);self.trees.append(tree)
        def budget():
            if time.monotonic()-started>=seconds:raise CompileLimit('time_limit')
        try:
            for tr in self.Ftrees:add(tr)
            for tr in self.strees.values():add(tr)
            for pair in self.ttrees.values():
                for tr in pair:add(tr)
            for terms in self.Dterms.values():
                for c,key,tr in terms:add(tr)
            feedback_states=len(self.trees)
            if self.augment_outputs:
                frontier=list(self.Ftrees)
                for output_step in range(self.output_depth):
                    children=set()
                    for tr in frontier:
                        budget()
                        for c,key,child in self.derivative(tr):add(child);children.add(child)
                    frontier=sorted(children)
            self.essential_trees=[]
            if self.preserve_essential:
                essential=set(self.Ftrees)|set(self.strees.values())
                for pair in self.ttrees.values():essential.update(pair)
                for layer,colors in [(0,self.x),(1,self.h)]:
                    for a,ca in enumerate(colors):
                        for cb in colors[a:]:essential.add(node(layer,[ca,cb]))
                self.essential_trees=sorted(essential)
                for tr in self.essential_trees:
                    add(tr)
                    for c,key,child in self.derivative(tr):add(child)
            if self.boundary=="current_gate_product":
                # Joint fourth gate moments preserve same-vertex pair effects.
                for layer,colors in [(0,self.x),(1,self.h)]:
                    for a,ca in enumerate(colors):
                        add(node(layer,[ca,ca]))
                        for cb in colors[a:]:add(node(layer,[ca,ca,cb,cb]))
            base_states=len(self.trees)
            layer_sizes=[base_states]
            for expansion in range(self.dependency_depth):
                current=list(self.trees)
                for tr in current:
                    budget()
                    for c,key,child in self.derivative(tr):add(child)
                layer_sizes.append(len(self.trees))
            self.boundary_rows=[];self.boundary_recipes=[]
            recipe_ids={};recipe_cache={};resolved_terms=0
            for row_id,tr in enumerate(self.trees):
                budget();terms=self.derivative(tr);full_terms+=len(terms)
                row=[]
                for c,key,child in terms:
                    idx=self.tree_ids.get(child)
                    if idx is not None:
                        row.append((c,key,idx));retained_terms+=1
                        if retained_terms>=max_terms:raise CompileLimit('term_limit')
                    else:
                        omitted_terms+=1
                        if self.boundary=="current_gate_product":
                            if child not in recipe_cache:
                                recipe_cache[child]=self._gate_recipe(child,budget)
                            recipe=recipe_cache[child]
                            if recipe is not None:
                                if recipe not in recipe_ids:
                                    recipe_ids[recipe]=len(self.boundary_recipes);self.boundary_recipes.append(recipe)
                                self.boundary_rows.append((row_id,c,key,recipe_ids[recipe]));resolved_terms+=1
                                if retained_terms+resolved_terms>=max_terms:raise CompileLimit("term_limit")
                self.rows.append(row)
            self.compiled=True;reason='complete';self._pack();self._pack_boundary()
        except CompileLimit as exc:reason=str(exc)
        self.report={'status':reason,'complete':self.compiled,'selection':'exact feedback constituents plus optional direct output children and dependency expansion','boundary':self.boundary,'boundary_definition':'zero for missing children' if self.boundary=='zero' else 'peel same-color gate pairs, at most four decorations per vertex, to nearest retained core; multiply retained current gate moments; edges never cut; unresolved children zero','convergence_claim':False,'states':len(self.trees),'feedback_seed_states':locals().get('feedback_states'),'base_states':locals().get('base_states'),'dependency_depth':self.dependency_depth,'augment_outputs':self.augment_outputs,'output_depth':self.output_depth,'preserve_essential':self.preserve_essential,'essential_exact_rows':len(self.essential_trees),'dependency_layer_sizes':locals().get('layer_sizes',[]),'processed_states':len(self.rows),'retained_terms':retained_terms,'reconstructed_boundary_terms':locals().get('resolved_terms',0),'unresolved_boundary_terms':omitted_terms-locals().get('resolved_terms',0),'unresolved_fraction_of_omitted_terms':(omitted_terms-locals().get('resolved_terms',0))/max(1,omitted_terms),'boundary_recipes':len(getattr(self,'boundary_recipes',[])),'omitted_terms':omitted_terms,'full_derivative_terms':full_terms,'seconds':time.monotonic()-started,'m':self.m,'queries':self.M,'k':self.k,'order':self.order,'degree_cutoff':None,'maximum_retained_degree':max(map(degree,self.trees),default=0),'degree_counts':{d:sum(degree(t)==d for t in self.trees) for d in sorted(set(map(degree,self.trees)))},'mark_bound':self.mark_bound,'penalty_mode':self.penalty_mode,'runtime_representation':'selected scalar normalized decorated-tree contractions and L only'}
        return self


    def _gate_recipe(self,tree,budget):
        """Nearest retained edge-preserving core, deterministic breadth first."""
        nodes,edges=flatten(tree)
        choices=[(v,col) for v,(_,decs) in enumerate(nodes) for col in sorted(set(decs)) if self.colors[col][0] in ('x','h') and decs.count(col)>=2]
        if not choices:return None
        adjacency=[[] for _ in nodes]
        for a,b in edges:adjacency[a].append(b);adjacency[b].append(a)
        initial=(0,)*len(choices);pending=deque([initial]);seen={initial}
        while pending:
            removed=pending.popleft()
            if len(seen)%128==0:budget()
            if any(removed):
                decorations=[list(decs) for _,decs in nodes];peeled=[[] for _ in nodes]
                for count,(v,col) in zip(removed,choices):
                    for repeat in range(count):decorations[v].remove(col);peeled[v].append(col)
                def encode(v,parent):
                    return node(nodes[v][0],decorations[v],[encode(w,v) for w in adjacency[v] if w!=parent])
                core=canonical(encode(0,-1));core_id=self.tree_ids.get(core)
                if core_id is not None:
                    gates=[self.tree_ids.get(node(nodes[v][0],decs)) for v,decs in enumerate(peeled) if decs]
                    if all(idx is not None for idx in gates):return (core_id,*sorted(gates))
            totals=[0]*len(nodes)
            for count,(v,col) in zip(removed,choices):totals[v]+=count
            for i,(v,col) in enumerate(choices):
                if totals[v]+2>4 or removed[i]+2>nodes[v][1].count(col):continue
                nxt=list(removed);nxt[i]+=2;nxt=tuple(nxt)
                if nxt not in seen:seen.add(nxt);pending.append(nxt)
        return None

    def _pack_boundary(self):
        indices={key:i for i,key in enumerate(self.coeff_keys)}
        rows=[];coeffs=[];recipes=[];values=[]
        for row,c,key,recipe in self.boundary_rows:
            if key not in indices:indices[key]=len(self.coeff_keys);self.coeff_keys.append(key)
            rows.append(row);coeffs.append(indices[key]);recipes.append(recipe);values.append(c)
        self.boundary_row_index=np.asarray(rows,int);self.boundary_coeff_index=np.asarray(coeffs,int)
        self.boundary_recipe_index=np.asarray(recipes,int);self.boundary_values=np.asarray(values,float)
        width=max(map(len,self.boundary_recipes),default=0)
        self.recipe_indices=np.full((len(self.boundary_recipes),width),len(self.trees),int)
        for i,recipe in enumerate(self.boundary_recipes):self.recipe_indices[i,:len(recipe)]=recipe

    def rhs(self,time_value,state):
        if self.boundary=='zero':return super().rhs(time_value,state)
        if not self.compiled:raise RuntimeError('Incomplete compilation cannot evolve')
        q=np.clip(state[:-1],-1.,1.);L=float(state[-1]);fields=self.fields(q,L)
        coeff=np.array([self.coefficient(key,fields,L) for key in self.coeff_keys])
        weights=self.values*coeff[self.coeff_index]
        result=np.bincount(self.row_index,weights=weights*q[self.child_index],minlength=len(q))
        # Padding factor1 makes variable-length recipes one bounded product.
        padded=np.r_[q,1.]
        reconstructed=np.clip(np.prod(padded[self.recipe_indices],axis=1),-1.,1.)
        bweights=self.boundary_values*coeff[self.boundary_coeff_index]
        result+=np.bincount(self.boundary_row_index,weights=bweights*reconstructed[self.boundary_recipe_index],minlength=len(q))
        envelope=np.bincount(self.row_index,weights=np.abs(weights),minlength=len(q))+np.bincount(self.boundary_row_index,weights=np.abs(bweights),minlength=len(q))
        result-=envelope*(state[:-1]-q)
        return np.r_[result,fields[self.sig]*L]


def compile_selective(u,labels,k=4,order=1,queries=None,mark_bound=3.,dependency_depth=0,augment_outputs=True,boundary="zero",preserve_essential=True,output_depth=1,max_states=100000,max_terms=1000000,seconds=60.):
    return SelectiveClosure(u,labels,k=k,order=order,queries=queries,mark_bound=mark_bound,dependency_depth=dependency_depth,augment_outputs=augment_outputs,boundary=boundary,preserve_essential=preserve_essential,output_depth=output_depth).compile(max_states,max_terms,seconds)


if __name__=='__main__':
    from circle_tasks import BY_NAME
    u,labels=BY_NAME['pair_cos1'].data()
    rows=[]
    for depth,augment in [(0,False),(0,True),(1,False)]:
        model=compile_selective(u,labels,dependency_depth=depth,augment_outputs=augment,preserve_essential=False)
        rows.append(model.report)
    output=Path('data/generated/structured_full_rank_scalar_20260926/true_aggregate_quick_20260927/compiler/selective_counts.json')
    output.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows,indent=2))
