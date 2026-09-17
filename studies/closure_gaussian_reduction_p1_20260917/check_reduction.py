"""Deterministic algebra checks; no training run or quadrature certification.

Budget: one CPU thread, <30 seconds, <256 MB. Stop on the first assertion.
Checks use the SAME positive tensor quadrature in all compared formulas, so
they check exact finite-rule identities up to rounding, not Gaussian accuracy.
"""

from itertools import product
import json
import numpy as np


def require_close(name, left, right, atol=2e-11):
    error = float(np.max(np.abs(np.asarray(left) - np.asarray(right))))
    scale = max(1.0, float(np.max(np.abs(right))))
    assert error <= atol * scale, (name, error, scale)
    checks[name] = error


checks = {}
nodes, weights = np.polynomial.hermite.hermgauss(7)
nodes, weights = np.sqrt(2) * nodes, weights / np.sqrt(np.pi)


def grid(dim):
    indices = np.array(list(product(range(len(nodes)), repeat=dim)))
    return nodes[indices], np.prod(weights[indices], axis=1)


lower, p1 = grid(4)
upper, p2 = grid(2)
g, noise = lower[:, :2], lower[:, 2:]
eta = 1 / 4096
nu = np.dot(weights, np.tanh(nodes) ** 2)
tau = np.dot(weights, np.tanh(np.sqrt(nu) * nodes) ** 2)
alpha = 1 - tau
h = np.tanh(g)
k = np.tanh(np.sqrt(tau) * noise + alpha * h)
H = np.tanh(np.sqrt(nu) * upper)
s = np.dot(p1, k[:, 0] ** 2)
beta = np.dot(p1, h[:, 0] * k[:, 0])
gamma = 1 - s
lh = np.sqrt(nu + eta)
lk = np.sqrt(s + eta - beta ** 2 / (nu + eta))
lH = np.sqrt(tau + eta)
b1 = np.column_stack((h / lh, (k - beta * h / (nu + eta)) / lk))
b2 = H / lH
dh = alpha * nu / (lh * lH)
dk = (alpha * beta * eta / (nu + eta) + tau * gamma) / (lk * lH)
D = np.column_stack((dh * np.eye(2), dk * np.eye(2)))

raw1 = np.column_stack((np.ones(len(p1)), h, k))
raw2 = np.column_stack((np.ones(len(p2)), H))
gram1 = raw1.T @ (p1[:, None] * raw1)
gram2 = raw2.T @ (p2[:, None] * raw2)
L1 = np.linalg.cholesky(gram1 + eta * np.eye(5))
L2 = np.linalg.cholesky(gram2 + eta * np.eye(3))
fullb1 = np.column_stack((np.full(len(p1), 1 / np.sqrt(1 + eta)), b1))
fullb2 = np.column_stack((np.full(len(p2), 1 / np.sqrt(1 + eta)), b2))
require_close("dictionary lower Cholesky", fullb1, np.linalg.solve(L1, raw1.T).T)
require_close("dictionary upper Cholesky", fullb2, np.linalg.solve(L2, raw2.T).T)
rawC = np.zeros((3, 5))
rawC[1:, 1:3] = alpha * nu * np.eye(2)
rawC[1:, 3:] = (alpha * beta + tau * gamma) * np.eye(2)
denseD = np.linalg.solve(L2, np.linalg.solve(L1, rawC.T).T)
fullD = np.zeros((3, 5))
fullD[1:, 1:] = D
require_close("initial contraction normalization", fullD, denseD)

angles = np.array([0.17, 1.08, 2.43])
U = np.column_stack((np.cos(angles), np.sin(angles)))
y = np.array([1.0, -1.0, 1.0])
mu = np.array([0.2, 0.5, 0.3])
representers = np.array([[0.4, -0.7], [-0.8, -0.3], [0.2, 0.9]])
coefficients = np.array([0.6, -0.2, 0.4])
readout_features = np.tanh(b2 @ representers.T)
c = readout_features @ coefficients
M = D + np.array([[0.07, -0.04, 0.08, 0.03], [-0.03, 0.02, -0.05, 0.06]])
w = g + 0.13 * np.tanh(b1 @ np.array([[0.2, -0.3], [0.6, 0.1], [-0.5, 0.4], [0.1, 0.7]]))


def evaluate(w, c, M, lower_features=b1, upper_features=b2):
    h1 = np.tanh(w @ U.T)
    a = lower_features.T @ (p1[:, None] * h1)
    latent = M @ a
    h2 = np.tanh(upper_features @ latent)
    f = (p2 * c) @ h2
    d = upper_features.T @ ((p2 * c)[:, None] * (1 - h2 ** 2))
    q = lower_features @ M.T @ d
    r = f - y
    wd = -2 * ((1 - h1 ** 2) * q * (mu * r)[None, :]) @ U
    cd = -2 * h2 @ (mu * r)
    Md = -2 * (d * (mu * r)[None, :]) @ a.T
    return (wd, cd, Md), (h1, a, latent, h2, f, d, q, r)


velocity, values = evaluate(w, c, M)
wd, cd, Md = velocity
h1, a, latent, h2, f, d, q, r = values
fullM = np.zeros((3, 5))
fullM[1:, 1:] = M
fullvelocity, fullvalues = evaluate(w, c, fullM, fullb1, fullb2)
require_close("constant removal w", wd, fullvelocity[0])
require_close("constant removal c", cd, fullvelocity[1])
require_close("constant removal M", Md, fullvelocity[2][1:, 1:])
require_close("constant row remains zero", fullvelocity[2][0, :], np.zeros(5))
require_close("constant column remains zero", fullvelocity[2][:, 0], np.zeros(3))

kernel = h2.T @ (p2[:, None] * h2)
kernel_cross = h2.T @ (p2[:, None] * readout_features)
require_close("F evaluation", kernel_cross @ coefficients, f)
kernel_gradient = np.einsum("pi,pa,pb,p->aib", b2, 1 - h2 ** 2, readout_features, p2)
require_close("gradient F gives d", np.einsum("aib,b->ia", kernel_gradient, coefficients), d)
require_close("partial F flow", -2 * kernel @ (mu * r), (p2 * cd) @ h2)

gates = 1 - h1 ** 2
C = np.einsum("pi,pj,pa,pb,p->abij", b1, b1, gates, gates, p1)
ad = -2 * np.einsum("b,ab,abij,jb->ia", mu * r, U @ U.T, C, M.T @ d)
ad_direct = b1.T @ (p1[:, None] * gates * (wd @ U.T))
require_close("lower contraction dynamics", ad, ad_direct)
latent_dot = Md @ a + M @ ad
fd_chain = (p2 * cd) @ h2 + np.sum(d * latent_dot, axis=0)
Kmiddle = (a.T @ a) * (d.T @ d)
Jlower = gates[:, :, None] * q[:, :, None] * U[None, :, :]
Klower = np.einsum("pai,pbi,p->ab", Jlower, Jlower, p1)
Klower_formula = (U @ U.T) * np.einsum("ia,abij,jb->ab", M.T @ d, C, M.T @ d)
require_close("lower tangent contraction", Klower_formula, Klower)
Kfull = kernel + Kmiddle + Klower
require_close("moving-argument prediction derivative", fd_chain, -2 * Kfull @ (mu * r))
for name, matrix in [("upper", kernel), ("middle", Kmiddle), ("lower", Klower), ("total", Kfull)]:
    smallest = float(np.linalg.eigvalsh(matrix).min())
    assert smallest >= -2e-12, (name, smallest)
    checks[name + " Gram minimum eigenvalue"] = smallest

eps = 2e-6
fp = evaluate(w + eps * wd, c + eps * cd, M + eps * Md)[1][4]
fm = evaluate(w - eps * wd, c - eps * cd, M - eps * Md)[1][4]
require_close("independent centered prediction derivative", (fp - fm) / (2 * eps), fd_chain, atol=2e-8)

v0, val0 = evaluate(g, np.zeros_like(c), D)
h10, a0, latent0, h20, f0, d0, q0, r0 = val0
require_close("initial w velocity", v0[0], np.zeros_like(g))
require_close("initial M velocity", v0[2], np.zeros_like(D))
Hy = h20 @ (mu * y)
dprime = b2.T @ ((2 * p2 * Hy)[:, None] * (1 - h20 ** 2))
wacc = 2 * ((1 - h10 ** 2) * (b1 @ D.T @ dprime) * (mu * y)[None, :]) @ U
Macc = 2 * (dprime * (mu * y)[None, :]) @ a0.T
vp = evaluate(g, eps * v0[1], D)[0]
vm = evaluate(g, -eps * v0[1], D)[0]
require_close("initial w acceleration", (vp[0] - vm[0]) / (2 * eps), wacc, atol=2e-8)
require_close("initial M acceleration", (vp[2] - vm[2]) / (2 * eps), Macc, atol=2e-8)


def J(w_state, M_state):
    data = evaluate(w_state, np.zeros_like(c), M_state)[1]
    hy = data[3] @ (mu * y)
    return np.dot(p2, hy * hy)


J_direction = (J(g + eps * wacc, D + eps * Macc) - J(g - eps * wacc, D - eps * Macc)) / (2 * eps)
acc_norm2 = np.einsum("pi,pi,p->", wacc, wacc, p1) + np.sum(Macc ** 2)
require_close("hidden acceleration equals twice gradient J", J_direction, acc_norm2 / 2, atol=2e-8)

print(json.dumps({"status": "PASS", "scope": "same-rule deterministic identities; no training experiment", "checks": checks}, indent=2))
