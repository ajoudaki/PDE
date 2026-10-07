"""Small deterministic algebra checks for FC.29--34, not probability proofs.

Compare the small two-orientation mean/covariance formulas with direct
conditioning of all n*n Gaussian coordinates, including empty and singular
history Grams. Fixed seed and bounded dimensions; no training experiment.
"""

import numpy as np

rng = np.random.default_rng(20261007)
largest = 0.0
cases = 0
n = 4
for forward_count in range(4):
    for reverse_count in range(4):
        for noise in (0.2, 0.7):
            for singular in (False, True):
                V = rng.normal(size=(n, forward_count))
                U = rng.normal(size=(n, reverse_count))
                if singular:
                    if forward_count > 1:
                        V[:, -1] = V[:, 0]
                    if reverse_count > 1:
                        U[:, -1] = 2 * U[:, 0]
                Yf = rng.normal(size=V.shape)
                Xb = rng.normal(size=U.shape)
                q = rng.normal(size=n)
                delta = noise**2
                Q, K = V.T @ V / n, U.T @ U / n
                H, J = U.T @ Yf / n, Xb.T @ V / n
                C = np.linalg.inv(delta * np.eye(forward_count) + Q)
                D = np.linalg.inv(delta * np.eye(reverse_count) + K)
                if forward_count and reverse_count:
                    sylvester = np.kron(
                        np.eye(forward_count), delta * np.eye(reverse_count) + K
                    ) + np.kron(Q.T, np.eye(reverse_count))
                    E = np.linalg.solve(
                        sylvester, (-H @ C - D @ J).reshape(-1, order="F")
                    ).reshape((reverse_count, forward_count), order="F")
                else:
                    E = np.zeros((reverse_count, forward_count))
                small_mean = (Yf @ C @ V.T + U @ D @ Xb.T + U @ E @ V.T) / n

                precision = n * np.eye(n * n) + (
                    np.kron(V @ V.T, np.eye(n))
                    + np.kron(np.eye(n), U @ U.T)
                ) / delta
                right = (Yf @ V.T + U @ Xb.T).reshape(-1, order="F") / delta
                direct_mean = np.linalg.solve(precision, right).reshape(
                    (n, n), order="F"
                )
                action = np.kron(q.reshape(1, n), np.eye(n))
                direct_cov = (
                    action @ np.linalg.solve(precision, action.T)
                    + delta * np.eye(n)
                )

                v, dq = V.T @ q / n, q @ q / n
                f0 = dq - v @ C @ v
                c = np.sqrt(delta + f0)
                eigenvalues, eigenvectors = np.linalg.eigh(K)
                tvalues = []
                for a in eigenvalues:
                    a = max(0.0, a)
                    inverse = np.linalg.inv((delta + a) * np.eye(forward_count) + Q)
                    f = delta * (dq - v @ inverse @ v) / (delta + a)
                    h = (-f0 + delta * v @ C @ inverse @ v) / (delta + a)
                    tvalues.append(h / (np.sqrt(delta + f) + c))
                T = (eigenvectors * np.asarray(tvalues)) @ eigenvectors.T
                root = c * np.eye(n) + U @ T @ U.T / n
                errors = [
                    np.linalg.norm(small_mean - direct_mean),
                    np.linalg.norm(root @ root.T - direct_cov),
                    max(0.0, noise - np.linalg.eigvalsh(root)[0]),
                ]
                largest = max(largest, *errors)
                assert max(errors) < 2e-10, (forward_count, reverse_count, errors)
                cases += 1

print(f"PASS: {cases} two-orientation cases, maximum error {largest:.3g}")
