"""Small deterministic numerical identities for the scalar implementation."""
import numpy as np
from cubic_scalar_ode import initialize, query_coefficients, integrate


def main():
    rng = np.random.default_rng(301)
    n = 13
    w = rng.normal(size=(n, 2))
    W = rng.normal(size=(n, n))/np.sqrt(n)
    angles = np.array([.1, .8, 1.9, 2.4])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    p = np.tanh(inputs@w.T)
    h = np.tanh(p@W.T)
    gamma = (1-h*h)[:, None, :]*h[None, :, :]
    beta = (gamma@W)*(1-p*p)[:, None, :]
    first_grad = beta[..., None]*inputs[:, None, None, :]
    middle_grad = gamma[..., :, None]*p[:, None, None, :]/n
    direct = (np.einsum('abij,cdij->abcd', first_grad, first_grad)/n
              + np.einsum('abij,cdij->abcd', middle_grad, middle_grad))
    model = initialize(w, W, inputs[:3], np.array([.1, -.1, .08]))
    np.testing.assert_allclose(model.response_gram, direct[:3,:3,:3,:3], atol=1e-14)
    query = query_coefficients(w, W, inputs[:3], inputs)
    expected = np.empty_like(query.cubic)
    for q in range(4):
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    expected[q,a,b,c] = (direct[a,q,b,c]+direct[q,a,b,c]
                        +direct[q,b,a,c]+direct[q,c,a,b])
    np.testing.assert_allclose(query.cubic, expected, atol=1e-14)
    state = rng.normal(size=model.size)*.15
    r,z,J,_ = model.unpack(state)
    assert np.linalg.eigvalsh(model.kernel(z,J)[0])[0] >= -1e-13
    np.testing.assert_allclose(model.predict(state, query)[:3], model.labels+r, atol=1e-13)
    one = initialize(w,W,inputs[:1],np.array([.1]))
    endpoint, info = integrate(one,target=1e-6)
    r,z,J,P = one.unpack(endpoint)
    K = float(one.initial_gram[0,0])
    S = float(one.response_gram[0,0,0,0])
    exact_r = -.1-2*K*z-(16/3)*S*z**3-(8/5)*S*S/K*z**5
    np.testing.assert_allclose(r,exact_r,atol=2e-10,rtol=0)
    np.testing.assert_allclose(P.ravel(),z**3/6,atol=2e-10,rtol=0)
    assert info['fitted'] and info['max_loss_rise'] == 0
    print('PASS: parameter-gradient Gram, query tensor, PSD kernel, aliases, m=1 integral identity and fitted endpoint')


if __name__ == '__main__':
    main()
