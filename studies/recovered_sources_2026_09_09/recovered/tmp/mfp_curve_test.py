import argparse
import json
import numpy as np


def rhs(u, B, c, gamma):
    n = len(u)
    p = u * u
    v = gamma * (B @ p)
    q = v * v
    d = c * v
    du = 4.0 * gamma * gamma * u * (B.T @ d)
    dB = (2.0 * gamma * gamma / n) * d[:, None] * p[None, :]
    dc = gamma * q
    f = gamma * np.dot(c, q) / n
    K = (np.dot(du, du) / n
         + np.sum(dB * dB)
         + np.dot(dc, dc) / n)
    return du, dB, dc, f, K


def rk4(u, B, c, h, gamma):
    k1 = rhs(u, B, c, gamma)[:3]
    k2 = rhs(u + .5*h*k1[0], B + .5*h*k1[1], c + .5*h*k1[2], gamma)[:3]
    k3 = rhs(u + .5*h*k2[0], B + .5*h*k2[1], c + .5*h*k2[2], gamma)[:3]
    k4 = rhs(u + h*k3[0], B + h*k3[1], c + h*k3[2], gamma)[:3]
    return tuple(x + h*(a + 2*b + 2*d + e)/6 for x,a,b,d,e in zip((u,B,c),k1,k2,k3,k4))


def simulate(n, seed, gamma, ds, y_max):
    rng = np.random.default_rng(seed)
    u = rng.standard_normal(n)
    B = rng.standard_normal((n,n))/np.sqrt(n)
    c = rng.standard_normal(n)
    rows=[]; s=0.0; next_y=0.0
    f0 = rhs(u,B,c,gamma)[3]
    while s < 0.05:
        _,_,_,f,K = rhs(u,B,c,gamma)
        y = f-f0
        if y >= next_y:
            rows.append((s,y,K))
            next_y += .025
        if y >= y_max:
            break
        u,B,c = rk4(u,B,c,ds,gamma)
        s += ds
    return rows


def simulate_pair(n, seed, gamma, ds, y_max):
    rng = np.random.default_rng(seed)
    u0 = rng.standard_normal(n)
    B0 = rng.standard_normal((n,n))/np.sqrt(n)
    c0 = rng.standard_normal(n)
    states=[(u0.copy(),B0.copy(),c0.copy()),(-u0.copy(),B0.copy(),-c0.copy())]
    f0=[rhs(*st,gamma)[3] for st in states]
    rows=[]; s=0.; next_y=0.
    while s<.05:
        vals=[rhs(*st,gamma) for st in states]
        ys=[vals[i][3]-f0[i] for i in range(2)]
        y=.5*(ys[0]+ys[1]); K=.5*(vals[0][4]+vals[1][4])
        if y>=next_y:
            rows.append((s,y,K)); next_y+=.025
        if y>=y_max: break
        states=[rk4(*st,ds,gamma) for st in states]
        s+=ds
    return rows


def main():
    p=argparse.ArgumentParser(); p.add_argument('--width',type=int,default=512);p.add_argument('--seed',type=int,default=0);p.add_argument('--ds',type=float,default=1e-5);p.add_argument('--y-max',type=float,default=1.0);p.add_argument('--gamma',type=float,default=1.0);a=p.parse_args()
    print(json.dumps(simulate_pair(a.width,a.seed,a.gamma,a.ds,a.y_max)))
if __name__=='__main__':main()
