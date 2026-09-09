import numpy as np


def relu(x):
    return np.sqrt(2.0) * np.maximum(x, 0.0)


def drelu(x):
    return np.sqrt(2.0) * (x > 0.0)


def step(a, w, u, h):
    n = a.size
    hu = relu(u)
    z = w @ hu / np.sqrt(n)
    c = a * drelu(z)
    b = w.T @ c / np.sqrt(n)
    return (
        a + h * relu(z),
        w + h * np.outer(c, hu) / np.sqrt(n),
        u + h * b * drelu(u),
    )


def output(a, w, u):
    n = a.size
    return np.mean(a * relu(w @ relu(u) / np.sqrt(n)))


def trial(rng, n, h):
    a = rng.standard_normal(n)
    w = rng.standard_normal((n, n))
    u = rng.standard_normal(n)
    fine = step(a, w, u, h)
    fine = step(*fine, h)
    coarse = step(a, w, u, 2.0 * h)
    return output(*fine) - output(*coarse)


if __name__ == "__main__":
    rng = np.random.default_rng(870231)
    for n, reps in [(100, 4000), (200, 2000), (400, 600)]:
        for h in (0.04, 0.02, 0.01):
            vals = np.array([trial(rng, n, h) for _ in range(reps)])
            scaled = vals / h**2
            print(n, reps, h, scaled.mean(), scaled.std(ddof=1) / np.sqrt(reps))
    print("prediction", np.sqrt(2.0) / np.pi * (1.0 - 1.0 / np.sqrt(5.0)))
