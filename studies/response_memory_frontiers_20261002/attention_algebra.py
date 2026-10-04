"""Single preregistered CPU algebra check; no training trajectory."""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np

SEED = 20261002
rng = np.random.default_rng(SEED)
d, n, s = 4, 16, 6
Q = rng.normal(size=(d, n)) / np.sqrt(n)
K = rng.normal(size=(d, n)) / np.sqrt(n)
h = rng.normal(size=(s, n))
c = rng.normal(size=(s, s))
eye = np.eye(d)
rotations = []
for i in range(s):
    R = np.zeros((d, d))
    for j, freq in enumerate([1.0, 0.01]):
        co, si = np.cos(i * freq), np.sin(i * freq)
        R[2*j:2*j+2, 2*j:2*j+2] = [[co, -si], [si, co]]
    rotations.append(R)

def fields(qw, kw, rope=False):
    Rs = rotations if rope else [eye] * s
    q = np.stack([Rs[i] @ qw @ h[i] for i in range(s)])
    k = np.stack([Rs[i] @ kw @ h[i] for i in range(s)])
    z = q @ k.T / np.sqrt(d)
    p = np.exp(z - z.max(axis=1, keepdims=True))
    p /= p.sum(axis=1, keepdims=True)
    dz = p * (c - (p * c).sum(axis=1, keepdims=True))
    gq = np.zeros_like(qw)
    gk = np.zeros_like(kw)
    for i in range(s):
        for j in range(s):
            gq += dz[i,j] * np.outer(Rs[i].T @ k[j], h[i]) / np.sqrt(d)
            gk += dz[i,j] * np.outer(Rs[j].T @ q[i], h[j]) / np.sqrt(d)
    return z, -gq, -gk, dz

def bdot(qw, kw, vq, vk):
    return vq @ qw.T + qw @ vq.T - vk @ kw.T - kw @ vk.T

def zdot(qw, kw, vq, vk, rope=False):
    Rs = rotations if rope else [eye] * s
    return np.array([[(h[i] @ vq.T @ Rs[i].T @ Rs[j] @ kw @ h[j]
                      + h[i] @ qw.T @ Rs[i].T @ Rs[j] @ vk @ h[j])
                     / np.sqrt(d) for j in range(s)] for i in range(s)])

def rel(x, scale):
    return float(np.linalg.norm(x) / max(1., np.linalg.norm(scale)))

_, fq, fk, dz = fields(Q, K)
forward_error = rng.normal(size=(s, n))
eq = 0.03 * rng.normal(size=(d, s)) @ forward_error
ek = 0.03 * rng.normal(size=(d, s)) @ forward_error
D = bdot(Q, K, eq, ek)
S = Q @ Q.T + K @ K.T
lam, U = np.linalg.eigh(S)
A = U @ (-(U.T @ D @ U) / (lam[:, None] + lam[None, :])) @ U.T
cq, ck = A @ Q, -A @ K
metrics = {
    'dense_matrix_balance_relative': rel(bdot(Q, K, fq, fk), fq),
    'uncorrected_defect_balance_norm': float(np.linalg.norm(D)),
    'corrected_matrix_balance_relative': rel(bdot(Q,K,fq+eq+cq,fk+ek+ck), D),
    'plain_gauge_logit_velocity_relative': rel(zdot(Q,K,cq,ck), cq),
    'gram_sum_condition': float(lam[-1] / lam[0]),
}

_, rfq, rfk, _ = fields(Q, K, True)
rdense = bdot(Q,K,rfq,rfk)
plane = lambda M: np.array([np.trace(M[j:j+2,j:j+2]) for j in range(0,d,2)])
ar = -plane(D) / (2 * plane(S))
Ar = np.diag(np.repeat(ar, 2))
rcq, rck = Ar @ Q, -Ar @ K
metrics.update({
    'rope_dense_plane_balance_relative': rel(plane(rdense), rfq),
    'rope_dense_full_matrix_balance_norm': float(np.linalg.norm(rdense)),
    'rope_corrected_plane_balance_relative': rel(plane(bdot(Q,K,rfq+eq+rcq,rfk+ek+rck)),D),
    'rope_plane_gauge_logit_velocity_relative': rel(zdot(Q,K,rcq,rck,True),rcq),
    'invalid_rope_full_gauge_logit_velocity_norm': float(np.linalg.norm(zdot(Q,K,cq,ck,True))),
})

# M = Q.T K and dL/dM = H.T (dL/dZ) H / sqrt(d).
G = h.T @ dz @ h / np.sqrt(d)
predicted = 2 * (G @ K.T @ A @ K - Q.T @ A @ Q @ G)
al, au = np.linalg.eigh(A)
diffs = {}
for eps in [1e-3, 1e-4, 1e-5]:
    drifts = []
    for sign in [1., -1.]:
        T = (au * np.exp(sign * eps * al)) @ au.T
        Tinv = (au * np.exp(-sign * eps * al)) @ au.T
        qq, kk = T @ Q, Tinv @ K
        _, ffq, ffk, _ = fields(qq,kk)
        drifts.append(ffq.T @ kk + qq.T @ ffk)
    diffs[str(eps)] = rel((drifts[0] - drifts[1]) / (2*eps) - predicted, predicted)
metrics['future_routing_derivative_fd_relative'] = diffs
identity_names = [key for key in metrics if key.endswith('_relative') and isinstance(metrics[key], float)]
passed = (all(metrics[k] < 1e-10 for k in identity_names)
          and diffs['1e-05'] < 1e-6
          and metrics['uncorrected_defect_balance_norm'] > 1e-6
          and metrics['invalid_rope_full_gauge_logit_velocity_norm'] > 1e-6
          and metrics['gram_sum_condition'] < 1e6)
out = {'status': 'PASS' if passed else 'FAIL_OR_INCONCLUSIVE', 'seed': SEED,
       'head_dimension': d, 'width': n, 'tokens': s, 'numpy': np.__version__,
       'python': platform.python_version(), 'metrics': metrics,
       'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'interpretation': 'Algebra only; no trained-trajectory evidence.'}
dest = Path('/home/amir/Codes/PDE/data/generated/response_memory_frontiers_20261002/attention_algebra')
dest.mkdir(parents=True, exist_ok=True)
(dest / 'metrics.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
