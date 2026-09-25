"""Exact low-rank, cached directional initialization for wide tanh networks.

The returned scalar tensors have the same definitions and index order as
scalar_aggregate_engine. Neuron arrays exist only during initialization.
Probe batches bound memory; no derivative directions or Q entries are dropped.
"""

import numpy as np

import scalar_aggregate_engine as aggregate


def _rank_action(left, right, values, scale, transpose=False):
    if transpose:
        left, right = right, left
    return scale * left[:, None] * (right @ values)[None, :]


class _Batch:
    def __init__(self, params, train_inputs, probe_inputs, order):
        self.params, self.train_inputs = params, train_inputs
        self.n, self.m = len(params[-1]), len(train_inputs)
        self.depth, self.order = len(params)-1, order
        self.inputs = np.vstack((train_inputs, probe_inputs))
        self.h = []
        current = self.inputs.T
        for matrix in params[:-1]:
            current = np.tanh(matrix @ current)
            self.h.append(current)
        self.gate = [1-value*value for value in self.h]
        self.back, self.delta = [None]*self.depth, [None]*self.depth
        self.back[-1] = params[-1][:, None]
        self.delta[-1] = self.back[-1]*self.gate[-1]
        for layer in range(self.depth-2, -1, -1):
            self.back[layer] = params[layer+1].T @ self.delta[layer+1]
            self.delta[layer] = self.gate[layer]*self.back[layer]
        self.first = []
        self.input_gram = probe_inputs @ train_inputs.T
        self.h_gram = [self._gram(value) for value in self.h]
        self.d_gram = [self._gram(value) for value in self.delta]

    def _direction(self, sample, layer, values, transpose=False):
        if layer == 0:
            return _rank_action(self.delta[0][:, sample], self.train_inputs[sample],
                                values, 1., transpose)
        return _rank_action(self.delta[layer][:, sample], self.h[layer-1][:, sample],
                            values, 1/self.n, transpose)

    def _acceleration(self, c, d, layer, values, transpose=False):
        """Apply A_cd=Dg_c[g_d], retaining its ordered moving-direction term."""
        first = self.first[d]
        if layer == 0:
            return _rank_action(first["delta"][0][:, c], self.train_inputs[c],
                                values, 1., transpose)
        return (_rank_action(first["delta"][layer][:, c], self.h[layer-1][:, c],
                             values, 1/self.n, transpose)
                + _rank_action(self.delta[layer][:, c], first["h"][layer-1][:, c],
                               values, 1/self.n, transpose))

    def _gram(self, base):
        return base[:, self.m:].T @ base[:, :self.m]/self.n

    def _first_gram(self, base, first):
        return (first[:, self.m:].T @ base[:, :self.m]
                + base[:, self.m:].T @ first[:, :self.m])/self.n

    def _mixed_gram(self, base, first, second, mixed):
        return (mixed[:, self.m:].T @ base[:, :self.m]
                + first[:, self.m:].T @ second[:, :self.m]
                + second[:, self.m:].T @ first[:, :self.m]
                + base[:, self.m:].T @ mixed[:, :self.m])/self.n

    def _first_fields(self, sample):
        h, z = [], []
        for layer in range(self.depth):
            previous = self.inputs.T if layer == 0 else self.h[layer-1]
            preactivation = self._direction(sample, layer, previous)
            if layer:
                preactivation += self.params[layer] @ h[layer-1]
            z.append(preactivation)
            h.append(self.gate[layer]*preactivation)
        delta, back = [None]*self.depth, [None]*self.depth
        back[-1] = self.h[-1][:, sample, None]
        delta[-1] = self.gate[-1]*back[-1]-2*self.h[-1]*h[-1]*self.back[-1]
        for layer in range(self.depth-2, -1, -1):
            back[layer] = (self.params[layer+1].T @ delta[layer+1]
                           + self._direction(sample, layer+1, self.delta[layer+1], True))
            delta[layer] = self.gate[layer]*back[layer]-2*self.h[layer]*h[layer]*self.back[layer]
        return dict(h=h, z=z, delta=delta, back=back,
                    h_gram=[self._first_gram(a, b) for a, b in zip(self.h, h)],
                    d_gram=[self._first_gram(a, b) for a, b in zip(self.delta, delta)])

    def _mixed_fields(self, c, d):
        first, second = self.first[c], self.first[d]
        h = []
        for layer in range(self.depth):
            previous = self.inputs.T if layer == 0 else self.h[layer-1]
            preactivation = self._acceleration(c, d, layer, previous)
            if layer:
                preactivation += self.params[layer] @ h[layer-1]
                preactivation += self._direction(c, layer, second["h"][layer-1])
                preactivation += self._direction(d, layer, first["h"][layer-1])
            h.append(self.gate[layer]*preactivation - 2*self.h[layer]*self.gate[layer]
                     * first["z"][layer]*second["z"][layer])
        delta = [None]*self.depth
        for layer in range(self.depth-1, -1, -1):
            if layer == self.depth-1:
                mixed_back = second["h"][-1][:, c, None]
            else:
                mixed_back = self.params[layer+1].T @ delta[layer+1]
                mixed_back += self._direction(c, layer+1, second["delta"][layer+1], True)
                mixed_back += self._direction(d, layer+1, first["delta"][layer+1], True)
                mixed_back += self._acceleration(c, d, layer+1, self.delta[layer+1], True)
            first_gate = -2*self.h[layer]*first["h"][layer]
            second_gate = -2*self.h[layer]*second["h"][layer]
            mixed_gate = -2*(first["h"][layer]*second["h"][layer]+self.h[layer]*h[layer])
            delta[layer] = (self.gate[layer]*mixed_back
                            + first_gate*second["back"][layer]
                            + second_gate*first["back"][layer]
                            + mixed_gate*self.back[layer])
        return h, delta

    def coefficients(self):
        theta = self.input_gram*self.d_gram[0]+self.h_gram[-1]
        for layer in range(1, self.depth):
            theta += self.h_gram[layer-1]*self.d_gram[layer]
        result = dict(f=self.params[-1] @ self.h[-1][:, self.m:]/self.n, Theta=theta)
        if self.order == 2:
            return result
        count = len(self.inputs)-self.m
        result["C"] = np.empty((count, self.m, self.m))
        for c in range(self.m):
            first = self._first_fields(c)
            self.first.append(first)
            value = self.input_gram*first["d_gram"][0]+first["h_gram"][-1]
            for layer in range(1, self.depth):
                value += (first["h_gram"][layer-1]*self.d_gram[layer]
                          + self.h_gram[layer-1]*first["d_gram"][layer])
            result["C"][:, :, c] = value
        if self.order == 3:
            return result
        result["Q"] = np.empty((count, self.m, self.m, self.m))
        for c in range(self.m):
            first = self.first[c]
            for d in range(self.m):
                second = self.first[d]
                mixed_h, mixed_delta = self._mixed_fields(c, d)
                hg = [self._mixed_gram(a, b, c1, d1) for a, b, c1, d1 in
                      zip(self.h, first["h"], second["h"], mixed_h)]
                dg = [self._mixed_gram(a, b, c1, d1) for a, b, c1, d1 in
                      zip(self.delta, first["delta"], second["delta"], mixed_delta)]
                value = self.input_gram*dg[0]+hg[-1]
                for layer in range(1, self.depth):
                    value += (hg[layer-1]*self.d_gram[layer]
                              + first["h_gram"][layer-1]*second["d_gram"][layer]
                              + second["h_gram"][layer-1]*first["d_gram"][layer]
                              + self.h_gram[layer-1]*dg[layer])
                result["Q"][:, :, c, d] = value
        return result


def initialize_probe_coefficients(params, train_inputs, probe_inputs, order=4, batch_size=128):
    """Initialize the original rectangular f/Theta/C/Q tensors in probe batches."""
    order = aggregate._order(order)
    batch_size = aggregate._positive_integer(batch_size, "batch_size")
    params, train_inputs = aggregate._validated_network(params, train_inputs)
    _, probe_inputs = aggregate._validated_network(params, probe_inputs)
    names = ("f", "Theta", "C", "Q")[:order]
    m, count = len(train_inputs), len(probe_inputs)
    result = {name: np.empty((count,)+(m,)*degree)
              for degree, name in enumerate(names)}
    for start in range(0, count, batch_size):
        stop = min(count, start+batch_size)
        values = _Batch(params, train_inputs, probe_inputs[start:stop], order).coefficients()
        for name in names:
            result[name][start:stop] = values[name]
    return result


def initialize_coefficients(params, inputs, order=4, batch_size=128):
    """Same training scalar initializer, with the exact cached low-rank algebra."""
    return initialize_probe_coefficients(params, inputs, inputs, order, batch_size)
