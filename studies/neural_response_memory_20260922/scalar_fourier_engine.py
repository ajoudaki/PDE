"""Finite scalar contraction/Fourier closure of the three-layer P=1 model.

The compiler and initializer use trees and neuron arrays.  ``rhs`` uses only
scalar coordinates and a compiled monomial table; no neuron state is retained.
The practical cutoff here deletes whole monomials and is unsaturated.
"""
from __future__ import annotations

from collections import defaultdict, deque
from functools import lru_cache
import time
import resource
import numpy as np
from scipy.sparse import csr_matrix


class CompilationLimit(RuntimeError):
    def __init__(self, reason, stats):
        super().__init__(reason)
        self.stats = stats


def node(layer, fields=(), children=()):
    return (int(layer), tuple(sorted(fields)), tuple(sorted(children)))


def field(kind, layer, sample=-1):
    return (kind, int(layer), int(sample))


def merge(a, b):
    if a[0] != b[0]:
        raise ValueError("Root layer mismatch")
    return node(a[0], a[1] + b[1], a[2] + b[2])


@lru_cache(None)
def size(tree):
    return 1 + len(tree[1]) + sum(1 + size(c) for c in tree[2])


@lru_cache(None)
def has_query(tree):
    return any(f[0] == 'h' and f[2] == -1 for f in tree[1]) or any(
        has_query(c) for c in tree[2])


def _graph(tree):
    nodes, adj = [], []
    def add(t, parent=-1):
        i = len(nodes)
        nodes.append((t[0], t[1]))
        adj.append([])
        if parent >= 0:
            adj[i].append(parent)
            adj[parent].append(i)
        for c in t[2]:
            add(c, i)
    add(tree)
    return nodes, adj


def _root(nodes, adj, i, parent=-1):
    return node(nodes[i][0], nodes[i][1],
                [_root(nodes, adj, j, i) for j in adj[i] if j != parent])


@lru_cache(None)
def canonical(tree):
    nodes, adj = _graph(tree)
    return min(_root(nodes, adj, i) for i in range(len(nodes)))


def nonconstant(tree):
    return bool(tree[1] or tree[2])


@lru_cache(None)
def differentiated_sites(tree):
    """(rooted remainder, differentiated species, multiplicity)."""
    nodes, adj = _graph(tree)
    out = defaultdict(int)
    for i in range(len(nodes)):
        rooted = _root(nodes, adj, i)
        for f in set(rooted[1]):
            fs = list(rooted[1])
            fs.remove(f)
            out[(node(rooted[0], fs, rooted[2]), f)] += rooted[1].count(f)
    return tuple((r, f, count) for (r, f), count in out.items())


# Expression key: rooted tree or None, detached canonical trees,
# cosine power, sine power, drive (-2=one,-1=rho,>=0=residual), L inverse power.
def primitive(kind, layer, sample=-1):
    return {(node(layer, [field(kind, layer, sample)]), (), 0, 0, -2, 0): 1.}


def one(layer):
    return {(node(layer), (), 0, 0, -2, 0): 1.}


def add(*exprs):
    out = defaultdict(float)
    for expr in exprs:
        for k, v in expr.items():
            out[k] += v
    return {k: v for k, v in out.items() if v != 0}


def scale(expr, value=1., drive=-2, lp=0, cosine=0, sine=0):
    out = {}
    for (root, trees, cc, ss, d, p), v in expr.items():
        if drive != -2 and d != -2:
            raise ValueError("Unexpected product of two driving factors")
        out[(root, trees, cc + cosine, ss + sine,
             d if drive == -2 else drive, p + lp)] = value * v
    return out


def product(a, b):
    out = defaultdict(float)
    for (ar, af, ac, ass, ad, ap), av in a.items():
        for (br, bf, bc, bs, bd, bp), bv in b.items():
            if ad != -2 and bd != -2:
                raise ValueError("Unexpected product of two drives")
            root = br if ar is None else ar if br is None else merge(ar, br)
            out[(root, tuple(sorted(af + bf)), ac + bc, ass + bs,
                 ad if bd == -2 else bd, ap + bp)] += av * bv
    return {k: v for k, v in out.items() if v != 0}


def average(expr):
    out = defaultdict(float)
    for (root, forest, cc, ss, d, p), v in expr.items():
        trees = forest + ((canonical(root),) if nonconstant(root) else ())
        out[(None, tuple(sorted(trees)), cc, ss, d, p)] += v
    return dict(out)


def initialized_action(target_layer, expr):
    return {(node(target_layer, children=[root]), forest, cc, ss, d, p): v
            for (root, forest, cc, ss, d, p), v in expr.items()}


class Templates:
    """Exact polynomial response-lift templates; no truncation here."""
    def __init__(self, U):
        self.U = np.asarray(U, dtype=float)
        self.M = self.U.shape[1]
        self.gram = self.U.T @ self.U
        self.factor = -2. / self.M
        self.cache = {}

    @staticmethod
    def gate(layer, sample):
        h = primitive('h', layer, sample)
        return add(one(layer), scale(product(h, h), -1.))

    def matrix(self, layer, v, transpose=False):
        target = layer - 1 if transpose else layer
        out = initialized_action(target, v)
        for a in range(self.M):
            local = self.moment('B' if transpose else 'A', layer, a)
            pair = self.moment('A' if transpose else 'B', layer, a)
            out = add(out, scale(product(local, average(product(pair, v))),
                                 self.factor, lp=1))
        return out

    @lru_cache(None)
    def delta(self, layer, a):
        if layer == 3:
            return product(primitive('c', 3), self.gate(3, a))
        return product(self.gate(layer, a),
                       self.matrix(layer+1, self.delta(layer+1, a), True))

    def moment(self, kind, layer, a):
        # The B species is indexed by its link but lives at its source layer.
        root_layer = layer - 1 if kind == 'B' else layer
        return {(node(root_layer, [field(kind, layer, a)]), (), 0, 0, -2, 0): 1.}

    def matrix_dot(self, layer, v):
        out = {}
        for a in range(self.M):
            A, B = self.moment('A', layer, a), self.moment('B', layer, a)
            pB = average(product(B, v))
            ph = average(product(primitive('h', layer-1, a), v))
            out = add(out,
                      scale(product(self.delta(layer, a), pB), self.factor,
                            drive=a, lp=1),
                      scale(product(A, ph), self.factor, drive=-1, lp=1),
                      scale(product(A, pB), -self.factor, drive=-1, lp=2))
        return out

    @lru_cache(None)
    def h_dot(self, layer, sample):
        if layer == 1:
            pre = {}
            for a in range(self.M):
                if sample < 0:
                    pre = add(pre,
                              scale(self.delta(1, a), self.factor*self.U[0,a],
                                    drive=a, cosine=1),
                              scale(self.delta(1, a), self.factor*self.U[1,a],
                                    drive=a, sine=1))
                else:
                    pre = add(pre, scale(self.delta(1,a),
                                         self.factor*self.gram[sample,a], drive=a))
        else:
            pre = add(self.matrix_dot(layer, primitive('h', layer-1, sample)),
                      self.matrix(layer, self.h_dot(layer-1, sample)))
        return product(self.gate(layer, sample), pre)

    def rhs(self, species):
        if species in self.cache:
            return self.cache[species]
        kind, layer, a = species
        if kind == 'h':
            out = self.h_dot(layer, a)
        elif kind == 'c':
            out = add(*(scale(primitive('h', 3, b), self.factor, drive=b)
                        for b in range(self.M)))
        elif kind == 'A':
            out = scale(self.delta(layer, a), drive=a)
        elif kind == 'B':
            out = scale(primitive('h', layer-1, a), drive=-1)
        else:
            raise KeyError(species)
        self.cache[species] = out
        return out


def angular_size(pattern):
    trees, cc, ss = pattern
    return 2 + cc + ss + sum(size(t) for t in trees)


def primitive_fields(W1, W20, W30, c, U, theta, A2=None, B2=None,
                     A3=None, B3=None, L=1.):
    """Compute exact P=1 lifted fields from physical outer and moment state."""
    W1, W20, W30, c, U = map(np.asarray, (W1, W20, W30, c, U))
    n, M = W1.shape[0], U.shape[1]
    A2 = np.zeros((n,M)) if A2 is None else np.asarray(A2)
    A3 = np.zeros((n,M)) if A3 is None else np.asarray(A3)
    h10 = np.tanh(W1 @ U)
    B2 = h10.copy() if B2 is None else np.asarray(B2)
    W2 = W20 - 2./(M*n*L) * (A2 @ B2.T)
    h20 = np.tanh(W2 @ h10)
    B3 = h20.copy() if B3 is None else np.asarray(B3)
    W3 = W30 - 2./(M*n*L) * (A3 @ B3.T)
    h30 = np.tanh(W3 @ h20)
    out = {field('c',3): c[:,None]}
    for layer, h in enumerate((h10,h20,h30), 1):
        for a in range(M):
            out[field('h',layer,a)] = h[:,a,None]
    for kind, layer, vals in [('A',2,A2),('B',2,B2),('A',3,A3),('B',3,B3)]:
        for a in range(M):
            out[field(kind,layer,a)] = vals[:,a,None]
    theta = np.asarray(theta)
    h = np.tanh(W1 @ np.stack([np.cos(theta),np.sin(theta)]))
    out[field('h',1)] = h
    h = np.tanh(W2 @ h)
    out[field('h',2)] = h
    out[field('h',3)] = np.tanh(W3 @ h)
    return out


class DiagramEvaluator:
    """Initialization/audit only. Each edge message uses the original W0."""
    def __init__(self, fields, W20, W30, theta):
        self.fields = fields
        self.weights = {2: np.asarray(W20), 3: np.asarray(W30)}
        self.theta = np.asarray(theta)
        self.n = W20.shape[0]
        self.cache = {}
        self.scalar_cache = {}

    def rooted(self, t):
        if t in self.cache:
            return self.cache[t]
        cols = len(self.theta) if has_query(t) else 1
        val = np.ones((self.n, cols))
        for f in t[1]:
            val *= self.fields[f]
        if np.any(val):
            for child in t[2]:
                W = self.weights[max(t[0], child[0])]
                msg = W @ self.rooted(child) if t[0] > child[0] else W.T @ self.rooted(child)
                val *= msg
        self.cache[t] = val
        return val

    def tree(self, t):
        if t not in self.scalar_cache:
            self.scalar_cache[t] = self.rooted(t).mean(axis=0)
        return self.scalar_cache[t]

    def angular_integrand(self, pattern):
        trees, cc, ss = pattern
        v = np.cos(self.theta)**cc * np.sin(self.theta)**ss
        for t in trees:
            v = v * self.tree(t)
        return v

    def expression(self, expr, residual, rho, L):
        """Independent numeric evaluation of an untruncated rooted template."""
        result = None
        for (root, forest, cc, ss, d, p), coef in expr.items():
            val = coef * self.rooted(root)
            for t in forest:
                val = val * self.tree(t)
            val = val * (np.cos(self.theta)**cc * np.sin(self.theta)**ss)
            val = val * (rho if d == -1 else residual[d] if d >= 0 else 1.) / L**p
            result = val if result is None else result + val
        return result


class ScalarFourierSystem:
    def __init__(self, U, y, K, J=8, max_patterns=4000, max_terms=200000,
                 compile_seconds=120., include_energy=False,
                 max_memory_bytes=2*1024**3):
        self.U, self.y = np.asarray(U, float), np.asarray(y, float)
        if self.U.shape != (2, len(self.y)):
            raise ValueError('U must have shape (2,M)')
        self.M, self.K, self.J = len(y), int(K), int(J)
        self.nweights = 2*self.J+1
        self.training_patterns, self.angular_patterns = [], []
        self.training_index, self.angular_index = {}, {}
        self.training_rows, self.angular_rows = [], []
        self.dropped_terms, self.generated_terms, self.retained_terms = 0, 0, 0
        self.compile_started = time.monotonic()
        self.max_patterns, self.max_terms = max_patterns, max_terms
        self.max_memory_bytes = max_memory_bytes
        self.compile_seconds = compile_seconds
        self.templates = Templates(self.U)
        self._pending = deque()
        self.output_indices = []
        for a in range(self.M):
            t = canonical(node(3,[field('c',3),field('h',3,a)]))
            self.output_indices.append(self._register(t, False))
        output_tree = canonical(node(3,[field('c',3),field('h',3)]))
        self.angular_output_index = self._register(((output_tree,),0,0), True)
        self.energy_index = None
        if include_energy:
            self.energy_index = self._register(((output_tree,output_tree),0,0), True)
        while self._pending:
            angular, index = self._pending.popleft()
            pattern = self.angular_patterns[index] if angular else self.training_patterns[index]
            row = self._compile_row(pattern, angular)
            (self.angular_rows if angular else self.training_rows)[index] = row
            self._check_limit()
        self.compile_time = time.monotonic() - self.compile_started
        self.ntrain, self.nangular = len(self.training_patterns), len(self.angular_patterns)
        self.dimension = self.ntrain + self.nangular*self.nweights + 1
        self._pack_tables()

    def statistics(self):
        return dict(K=self.K, J=self.J, training_patterns=len(self.training_patterns),
                    angular_patterns=len(self.angular_patterns), retained_terms=self.retained_terms,
                    generated_terms=self.generated_terms, dropped_terms=self.dropped_terms,
                    peak_rss_bytes=1024*resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    compile_seconds=getattr(self,'compile_time',time.monotonic()-self.compile_started),
                    dimension=getattr(self,'dimension',None))

    def _check_limit(self):
        if len(self.training_patterns)+len(self.angular_patterns)>self.max_patterns:
            raise CompilationLimit('pattern cap', self.statistics())
        if self.retained_terms>self.max_terms:
            raise CompilationLimit('retained-term cap', self.statistics())
        if 1024*resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>self.max_memory_bytes:
            raise CompilationLimit('memory cap', self.statistics())
        if time.monotonic()-self.compile_started>self.compile_seconds:
            raise CompilationLimit('compilation time cap', self.statistics())

    def _register(self, pattern, angular):
        patterns, index, rows = ((self.angular_patterns,self.angular_index,self.angular_rows)
                                 if angular else
                                 (self.training_patterns,self.training_index,self.training_rows))
        if pattern not in index:
            s = angular_size(pattern) if angular else size(pattern)
            if s > self.K:
                raise ValueError('Requested readout exceeds cutoff')
            index[pattern] = len(patterns)
            patterns.append(pattern)
            rows.append(None)
            self._pending.append((angular,index[pattern]))
            self._check_limit()
        return index[pattern]

    def _compile_row(self, pattern, angular):
        trees, cc0, ss0 = pattern if angular else ((pattern,),0,0)
        terms = defaultdict(float)
        for ti, t in enumerate(trees):
            other = trees[:ti]+trees[ti+1:]
            for rem, species, count in differentiated_sites(t):
                for (root, forest, cc, ss, drive, lp), coef in self.templates.rhs(species).items():
                    self.generated_terms += 1
                    if self.generated_terms % 512 == 0:
                        self._check_limit()
                    joined = canonical(merge(rem,root))
                    all_trees = tuple(sorted(other+forest+((joined,) if nonconstant(joined) else ())))
                    if angular:
                        tr = tuple(t for t in all_trees if not has_query(t))
                        aq = tuple(t for t in all_trees if has_query(t))
                        ap = (aq,cc0+cc,ss0+ss)
                        fits = angular_size(ap)<=self.K and all(size(t)<=self.K for t in tr)
                    else:
                        if cc or ss or any(has_query(t) for t in all_trees):
                            raise AssertionError('Angular dependency entered training block')
                        tr, ap = all_trees, None
                        fits = all(size(t)<=self.K for t in tr)
                    if not fits:
                        self.dropped_terms += 1
                        continue
                    terms[(tr,ap,drive,lp)] += count*coef
        result = []
        for (tr,ap,drive,lp),coef in terms.items():
            if coef == 0:
                continue
            indices = tuple(self._register(t,False) for t in tr)
            ai = self._register(ap,True) if angular else -1
            result.append((coef,indices,ai,drive,lp))
        self.retained_terms += len(result)
        return result

    def _table(self, rows, angular):
        records = [(i,term) for i,row in enumerate(rows) for term in row]
        arity = max((len(t[1]) for _,t in records),default=0)
        ix = np.full((len(records),arity),self.ntrain,dtype=np.int32)
        rr, coef, drives, powers, ac = [], [], [], [], []
        for k,(r,(c,indices,a,d,p)) in enumerate(records):
            ix[k,:len(indices)] = indices
            rr.append(r); coef.append(c); drives.append(d+2); powers.append(p); ac.append(a)
        table = dict(indices=ix, rows=np.array(rr,dtype=np.int32),
                     coefficients=np.asarray(coef), drives=np.array(drives,dtype=np.int32),
                     powers=np.array(powers,dtype=np.int32))
        if angular:
            pairs = sorted(set(zip(rr,ac)))
            pidx = {p:i for i,p in enumerate(pairs)}
            table['edge_ids'] = np.array([pidx[p] for p in zip(rr,ac)],dtype=np.int32)
            rowcounts = np.bincount([p[0] for p in pairs],minlength=self.nangular)
            table['indptr'] = np.r_[0,np.cumsum(rowcounts)]
            table['columns'] = np.array([p[1] for p in pairs],dtype=np.int32)
        return table

    def _pack_tables(self):
        self.train_table = self._table(self.training_rows,False)
        self.angular_table = self._table(self.angular_rows,True)

    def initialize(self, W1, W20, W30, c, quadrature=256):
        started = time.monotonic()
        theta = 2*np.pi*np.arange(quadrature)/quadrature
        fields = primitive_fields(W1,W20,W30,c,self.U,theta)
        ev = DiagramEvaluator(fields,W20,W30,theta)
        z = np.zeros(self.dimension)
        z[:self.ntrain] = [ev.tree(t)[0] for t in self.training_patterns]
        weights = np.ones((quadrature,self.nweights))
        for k in range(1,self.J+1):
            weights[:,2*k-1] = np.cos(k*theta)
            weights[:,2*k] = np.sin(k*theta)
        Q = z[self.ntrain:-1].reshape(self.nangular,self.nweights)
        for i,p in enumerate(self.angular_patterns):
            Q[i] = ev.angular_integrand(p) @ weights / quadrature
        z[-1] = 1.
        self.initialization_seconds = time.monotonic()-started
        return z

    def _values(self, table, q, drive, L):
        return (table['coefficients'] * np.prod(q[table['indices']],axis=1) *
                drive[table['drives']] / np.power(L,table['powers']))

    def rhs(self, t, z):
        q = np.r_[z[:self.ntrain],1.]
        r = q[self.output_indices]-self.y
        rho = np.linalg.norm(r)/np.sqrt(self.M)
        drive = np.r_[1.,rho,r]
        L = z[-1]
        out = np.empty_like(z)
        vals = self._values(self.train_table,q,drive,L)
        out[:self.ntrain] = np.bincount(self.train_table['rows'],weights=vals,minlength=self.ntrain)
        tab = self.angular_table
        vals = self._values(tab,q,drive,L)
        data = np.bincount(tab['edge_ids'],weights=vals,minlength=len(tab['columns']))
        mat = csr_matrix((data,tab['columns'],tab['indptr']),shape=(self.nangular,self.nangular))
        Q = z[self.ntrain:-1].reshape(self.nangular,self.nweights)
        out[self.ntrain:-1] = (mat @ Q).ravel()
        out[-1] = rho
        return out

    def training_output(self,z):
        return np.asarray(z)[self.output_indices]

    def fourier_coefficients(self,z):
        return np.asarray(z)[self.ntrain:-1].reshape(self.nangular,self.nweights)[self.angular_output_index].copy()

    def circle_output(self,z,theta):
        coeff = self.fourier_coefficients(z)
        theta = np.asarray(theta)
        out = np.full(theta.shape,coeff[0])
        for k in range(1,self.J+1):
            out += 2*(coeff[2*k-1]*np.cos(k*theta)+coeff[2*k]*np.sin(k*theta))
        return out
