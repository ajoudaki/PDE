#!/usr/bin/env python3
"""Probe the sign of f_D(grad f_D(x)) for the L=2 leading homogeneous map."""

import random


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def matvec(W, x):
    return [dot(row, x) for row in W]


def tmatvec(W, x):
    return [sum(W[i][j] * x[i] for i in range(len(W)))
            for j in range(len(W[0]))]


def leading_output(state, d):
    a, W, u = state
    v = [x ** d for x in u]
    z = matvec(W, v)
    return sum(a[i] * z[i] ** d for i in range(len(a)))


def leading_gradient(state, d):
    a, W, u = state
    v = [x ** d for x in u]
    z = matvec(W, v)
    c = [a[i] * z[i] ** (d - 1) for i in range(len(a))]
    b = tmatvec(W, c)
    ga = [x ** d for x in z]
    gW = [[d * c[i] * v[j] for j in range(len(u))]
          for i in range(len(a))]
    gu = [d * d * u[j] ** (d - 1) * b[j] for j in range(len(u))]
    return ga, gW, gu


def normalize(state):
    a, W, u = state
    scale = max([abs(x) for x in a + u] +
                [abs(x) for row in W for x in row] + [1e-300])
    return ([x / scale for x in a],
            [[x / scale for x in row] for row in W],
            [x / scale for x in u])


def trial(n, d, rounds=100000):
    lo = float("inf")
    witness = None
    for _ in range(rounds):
        state = (
            [random.gauss(0, 1) for _ in range(n)],
            [[random.gauss(0, 1) for _ in range(n)] for _ in range(n)],
            [random.gauss(0, 1) for _ in range(n)],
        )
        state = normalize(leading_gradient(state, d))
        state = normalize(leading_gradient(state, d))
        value = leading_output(state, d)
        if value < lo:
            lo, witness = value, state
        if value < -1e-8:
            return value, witness
    return lo, witness


if __name__ == "__main__":
    random.seed(1729)
    for degree in (2, 3, 4):
        value, _ = trial(3, degree, 10000)
        print(degree, value)
