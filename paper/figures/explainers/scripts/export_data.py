#!/usr/bin/env python3
"""Rebuild the JSON payloads embedded in the data-driven explainer figures.

Usage:
    python export_data.py --data data/generated/explainer_figures_20261009

Reads the run arrays under --data (see ../README.md for the commands that make
them) and writes spectra/*.npz and json/fig*.json beside them. build_html.py
injects these JSON files into templates/ to regenerate the figure fragments.
"""
import argparse
import base64
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre as L
from scipy.special import lpmv


def sig(v, p):
    return [float(f'{x:.{p}g}') for x in v]


def clock(t, rho):
    return 1+np.concatenate([[0], np.cumsum(0.5*(rho[1:]+rho[:-1])*np.diff(t))])


def sh_table(ct, ph, kmax):
    """Real spherical harmonics (Condon-Shortley phase) on a Gauss-Legendre x uniform grid."""
    rows = []
    for l in range(kmax+1):
        for m in range(-l, l+1):
            am = abs(m)
            nrm = math.sqrt((2*l+1)/(4*math.pi)*math.factorial(l-am)/math.factorial(l+am))
            p = lpmv(am, l, ct)
            if m == 0:
                rows.append(np.outer(nrm*p, np.ones(len(ph))).ravel())
            else:
                trig = np.cos(am*ph) if m > 0 else np.sin(am*ph)
                rows.append(np.outer(math.sqrt(2)*nrm*p, trig).ravel())
    deg = np.array([l for l in range(kmax+1) for _ in range(2*l+1)])
    return np.array(rows), deg


def spectra(z, kmax):
    Y, deg = sh_table(z['ct'], z['ph'], kmax)
    w = np.outer(z['wt'], np.full(len(z['ph']), 2*np.pi/len(z['ph']))).ravel()
    coefs = lambda F: (Y*w)@F.T
    energy = lambda c: np.array([np.sum(c[deg == l]**2, axis=0) for l in range(kmax+1)])
    total = lambda F: np.sum(w*F**2, axis=-1)
    return coefs, energy, total, deg


def fig15b_16b(z):
    t, r, h1, d2, Wt, n = z['t'], z['r'], z['h1'], z['d2'], z['W'], int(z['n'])
    m = r.shape[1]
    rho = np.linalg.norm(r, axis=1)/np.sqrt(m)
    tau = clock(t, rho)
    b = r[:, None, :]*d2/rho[:, None, None]
    a, i, j = 5, 6, 6
    TT = np.concatenate([[0], tau])
    ext = lambda v, pre: np.concatenate([[pre], v])
    G = np.linspace(0, tau[-1], 241)
    X = np.interp(G, TT, ext(h1[:, j, a], h1[0, j, a]))
    Y = np.interp(G, TT, ext(b[:, i, a], 0.))
    Wtrue = np.interp(G, TT, ext(Wt[:, i, j], 0.))
    Wrec = np.zeros((10, len(G)))
    for gi, s in enumerate(G):
        if s < 1e-9:
            continue
        u = np.linspace(0, s, 1501)
        P = np.array([L.legval(2*u/s-1, [0]*k+[1]) for k in range(10)])
        tot = np.zeros(10)
        for aa in range(m):
            hx = np.interp(u, TT, ext(h1[:, j, aa], h1[0, j, aa]))
            bx = np.interp(u, TT, ext(b[:, i, aa], 0.))
            mh, mb = np.trapz(P*hx, u, axis=1), np.trapz(P*bx, u, axis=1)
            tot += np.cumsum((2*np.arange(10)+1)/s*mh*mb)
        Wrec[:, gi] = -2/(m*n)*tot
    sc = np.abs(Wtrue).max()
    r5 = lambda v: sig(v, 5)
    full = dict(tau=r5(G), x=r5(X), y=r5(Y), W=r5(Wtrue/sc), Wq=[r5(w/sc) for w in Wrec],
                tauEnd=float(tau[-1]))
    idx = np.linspace(0, len(G)-1, 161).round().astype(int)
    pick = lambda key: np.array(full[key])[idx]
    d15 = dict(tau=sig(pick('tau'), 4), x=sig(pick('x'), 4), y=sig(pick('y'), 4), W=sig(pick('W'), 4),
               Wq=[sig(np.array(w)[idx], 3) for w in full['Wq']], tauEnd=round(full['tauEnd'], 4))
    kap = -np.polyfit(t[t > 24], np.log(rho[t > 24]), 1)[0]
    ts = np.linspace(0, 32, 161)
    d16 = dict(t=r5(ts), rho=r5(np.interp(ts, t, rho)), tau=r5(np.interp(ts, t, tau)), kap=float(kap),
               bt=r5(np.interp(np.linspace(0, tau[-1], 161), TT, ext(b[:, i, a], 0.))),
               tauEnd=float(tau[-1]))
    return d15, d16


def fig21b(z, out):
    coefs, energy, total, deg = spectra(z, 24)
    cf, ch = coefs(z['f'][None])[:, 0], coefs(z['h2'])
    sf, sh = energy(cf[:, None])[:, 0], energy(ch)
    np.savez(out/'spectra_sphere3_t32.npz', cf=cf, ch=ch, deg=deg, sf=sf, sh=sh,
             totf=total(z['f']), toth=total(z['h2']))
    KM, keep = 23, deg <= 23
    frac = sh/total(z['h2'])[None]
    order = np.argsort(1-frac[:4].sum(0))
    pick = [order[int(p*len(order))] for p in (0.5, 0.7, 0.8, 0.86, 0.9, 0.94, 0.97, 0.99)]
    funcs = [('network output f', cf[keep])]+[(f'hidden neuron {int(k)} (layer 2)', ch[keep, k]) for k in pick]
    odd = list(range(1, KM+1, 2))
    pct = np.percentile(frac[odd], [5, 50, 95], axis=1)
    pos = [c for c, l in enumerate(deg[keep]) if l % 2 == 1]
    KS = 19
    nkeep = sum(2*l+1 for l in range(1, KS+1, 2))
    lost = [1-frac[:K+1].sum(0) for K in range(1, 16, 2)]
    return dict(KM=KS, funcs=[dict(name=nm, c=sig(sig(np.array(c)[pos], 4)[:nkeep], 3)) for nm, c in funcs],
                odd=odd[:KS//2+1], p5=sig(sig(pct[0], 4)[:KS//2+1], 3), p50=sig(sig(pct[1], 4)[:KS//2+1], 3),
                p95=sig(sig(pct[2], 4)[:KS//2+1], 3), n=int(sh.shape[1]),
                lost50=[float(f'{np.median(v):.3g}') for v in lost],
                lost95=[float(f'{np.percentile(v, 95):.3g}') for v in lost])


def fig15c(z, restarts):
    t = z['t']
    keep = t <= 32+1e-9
    t, tau, rho, h1, d2, r, W, fq = (z[k][keep] for k in ('t', 'tau', 'rho', 'h1', 'd2', 'r', 'W', 'fq'))
    m = r.shape[1]
    b = r[:, None, :]*d2/rho[:, None, None]
    links = [(5, 6, 6), (0, 33, 50), (2, 35, 59)]
    G = np.linspace(0, tau[-1], 161)
    TT = np.concatenate([[0], tau])
    out = dict(tau=sig(G, 4), tauEnd=float(tau[-1]), links=[], restarts=[])
    for a, i, j in links:
        out['links'].append(dict(
            name=f'example {a}, link {j}→{i}',
            x=sig(np.interp(G, TT, np.concatenate([[h1[0, j, a]], h1[:, j, a]])), 4),
            y=sig(np.interp(G, TT, np.concatenate([[0], b[:, i, a]])), 4),
            W=sig(np.interp(G, TT, np.concatenate([[0], W[:, i, j]])), 4), fut=[]))
    for tr, R in restarts:
        rt, rtau = R['t'], R['tau']
        idx = np.linspace(0, len(rt)-1, 32).round().astype(int)
        errs = [sig([np.sqrt(np.mean((R['fq'][k, bq]-fq[np.argmin(abs(t-rt[k]))])**2)) for k in idx], 3)
                for bq in range(len(R['orders']))]
        out['restarts'].append(dict(t=tr, tauR=float(rtau[0, 0]), orders=[int(q) for q in R['orders']],
                                    tq=sig(rt[idx], 4), err=errs))
        rrho = np.linalg.norm(R['r'], axis=2)/np.sqrt(m)
        for li, (a, i, j) in enumerate(links):
            out['links'][li]['fut'].append([dict(
                tau=sig(rtau[idx, bq], 4), x=sig(R['h1'][idx, bq, j, a], 4),
                y=sig(R['r'][idx, bq, a]*R['d2'][idx, bq, i, a]/rrho[idx, bq], 4),
                W=sig(R['W'][idx, bq, i, j], 4)) for bq in range(len(R['orders']))])
    # Compact encoding: values as integers 0..999 on per-link ranges, then thinned.
    sel = np.linspace(0, len(G)-1, 121).round().astype(int)
    out['tau'] = [round(float(x), 4) for x in np.array(out['tau'])[sel]]
    for Lk in out['links']:
        allv = {k: np.concatenate([Lk[k]]+[f[k] for fr in Lk['fut'] for f in fr]) for k in ('x', 'y', 'W')}
        Lk['rx'] = [float(allv['x'].min()), float(allv['x'].max())]
        Lk['ry'] = [float(allv['y'].min()), float(allv['y'].max())]
        Lk['rw'] = [float(min(0, allv['W'].min())), float(allv['W'].max())]
        enc = lambda v, rg: [int(round(999*(x-rg[0])/(rg[1]-rg[0]))) for x in v]
        for k, rg in (('x', 'rx'), ('y', 'ry'), ('W', 'rw')):
            Lk[k] = enc(np.array(Lk[k])[sel], Lk[rg])
        for fr in Lk['fut']:
            for f in fr:
                ix = np.linspace(0, len(f['tau'])-1, 40).round().astype(int)
                f['tau'] = [round(float(x), 3) for x in np.array(f['tau'])[ix]]
                for k, rg in (('x', 'rx'), ('y', 'ry'), ('W', 'rw')):
                    f[k] = enc(np.array(f[k])[ix], Lk[rg])
    for R in out['restarts']:
        ix = np.linspace(0, len(R['tq'])-1, 24).round().astype(int)
        R['tq'] = sig(np.array(R['tq'])[ix], 3)
        R['err'] = [sig(np.array(e)[ix], 3) for e in R['err']]
    sel = np.linspace(0, len(out['tau'])-1, 101).round().astype(int)
    out['tau'] = [round(float(x), 3) for x in np.array(out['tau'])[sel]]
    for Lk in out['links']:
        for k in ('x', 'y', 'W'):
            Lk[k] = [Lk[k][i] for i in sel]
        for fr in Lk['fut']:
            for f in fr:
                ix = np.linspace(0, len(f['tau'])-1, 30).round().astype(int)
                for k in ('tau', 'x', 'y', 'W'):
                    f[k] = [f[k][i] for i in ix]
    return out


def fig16c_17c(z):
    t, tau, rho, r, d2, h1 = z['t'], z['tau'], z['rho'], z['r'], z['d2'], z['h1']
    a, i = 5, 6
    b = r[:, a]*d2[:, i, a]/rho
    ts = np.linspace(0, 112, 225)
    TT = np.concatenate([[0], tau])
    G = np.linspace(0, tau[-1], 241)
    d16 = dict(t=[round(float(x), 2) for x in ts], rho=sig(np.interp(ts, t, rho), 4),
               tau=[round(float(x), 4) for x in np.interp(ts, t, tau)],
               bt=sig(np.interp(G, TT, np.concatenate([[0], b])), 4), tauEnd=float(tau[-1]))
    keep = t <= 32+1e-9
    tau, rho, h1, d2, r = tau[keep], rho[keep], h1[keep], d2[keep], r[keep]
    TT, s = np.concatenate([[0], tau]), tau[-1]
    d17 = []
    for nm, (a, i, j) in zip('ABC', [(5, 6, 6), (0, 33, 50), (2, 35, 59)]):
        u = np.linspace(0, s, 40001)
        H = np.interp(u, TT, np.concatenate([[h1[0, j, a]], h1[:, j, a]]))
        B = np.interp(u, TT, np.concatenate([[0], r[:, a]*d2[:, i, a]/rho]))
        P = [L.legval(2*u/s-1, [0]*k+[1]) for k in range(12)]
        f = [np.trapz(p*H, u)*np.sqrt((2*k+1)/s) for k, p in enumerate(P)]
        g = [np.trapz(p*B, u)*np.sqrt((2*k+1)/s) for k, p in enumerate(P)]
        d17.append(dict(name=f'Link {nm}: example {a}, link {j}→{i}', f=sig(f, 4), g=sig(g, 4),
                        direct=float(np.trapz(H*B, u))))
    return d16, d17


def fig21c(z, out):
    coefs, energy, total, deg = spectra(z, 15)
    spec = lambda F: (coefs(F), energy(coefs(F))/total(F)[None])
    (cf, _), (ch, sh), (c1, s1) = spec(z['f'][None]), spec(z['h2']), spec(z['h1'])
    np.savez(out/'spectra_rich_target.npz', cf=cf[:, 0], ch=ch, sh=sh, c1=c1, s1=s1, deg=deg)
    KM, odd = 13, list(range(1, 14, 2))
    keep = np.isin(deg, odd)
    order = np.argsort(1-sh[:4].sum(0))
    pick = {'rich A': order[int(0.99*len(order))], 'rich B': order[int(0.95*len(order))],
            'typical': order[len(order)//2]}
    k1 = int(np.argmax(1-s1[1]))
    funcs = [dict(name='network output f (fit to a degree-3/5 target)', c=sig(cf[keep, 0], 3))]
    funcs += [dict(name=f'layer-2 neuron {k} ({nm})', c=sig(ch[keep, k], 3)) for nm, k in pick.items()]
    funcs += [dict(name=f'layer-1 neuron {k1} (a single ridge)', c=sig(c1[keep, k1], 3))]
    pct = np.percentile(sh[odd], [5, 50, 95], axis=1)
    return dict(KM=KM, funcs=funcs, odd=odd, p5=sig(pct[0], 3), p50=sig(pct[1], 3), p95=sig(pct[2], 3),
                n=int(sh.shape[1]))


def selection_order(H, D, tol=1e-4, upto=256):
    """Logarithmic selection on E = span of the recorded fields, extended greedily beyond dim E.

    E is the numerical span (column-normalized SVD, relative tolerance tol) of the
    forward and backward fields over the whole run. Pivoted QR on a basis of E picks
    dim E rows, as in capture_trajectory._logarithmic_selected_metric; further rows
    maximize det(G + v v^T)/det(G), as in its 'qr_leverage' panel strategy, so every
    prefix of the returned order is the selection for that budget.
    """
    from scipy.linalg import qr
    n = H.shape[0]
    table = np.hstack([H, D])
    norms = np.linalg.norm(table, axis=0)
    U, s, _ = np.linalg.svd(table[:, norms > 0]/norms[norms > 0], full_matrices=False)
    rank = int((s > tol*s[0]).sum())
    rows = U[:, :rank]*math.sqrt(n)                      # U^T U / n = I
    chosen = list(qr(rows.T, pivoting=True, mode='economic')[2][:rank])
    inverse = np.linalg.inv(rows[chosen].T@rows[chosen])
    scores = np.einsum('ij,jk,ik->i', rows, inverse, rows)
    taken = np.zeros(n, bool)
    taken[chosen] = True
    while len(chosen) < upto:
        i = int(np.where(taken, -np.inf, scores).argmax())
        v = inverse@rows[i]
        den = 1+rows[i]@v
        inverse -= np.outer(v, v)/den
        scores -= (rows@v)**2/den
        taken[i] = True
        chosen.append(i)
    return np.array(chosen), rows, rank


def fig19c(z, a=0, frames=96):
    """All layer-2 neurons at training input a: forward h, backward delta, frames uniform in the clock."""
    t, r = z['t'], z['r']
    H = z['h2'][:, :, a].T.astype(np.float64)          # (n, K)
    D = z['d2'][:, :, a].T.astype(np.float64)
    n = H.shape[0]
    order, rows, rank = selection_order(H, D)
    # Exact metric for each budget q >= dim E: M = I/q + (P/q)(G^-2 - G^-1)(P/q)^T, G = P^T P/q,
    # so P^T M P = I and <u,v>_n = u_I^T M v_I on E. Record the worst pairing error over the run.
    X = np.stack([H, D], 1)                               # (n, 2, K)
    full = np.einsum('ick,idk->kcd', X, X)/n
    sel_err = []
    for q in range(rank, len(order)+1):
        I = order[:q]
        P = rows[I]
        Gi = np.linalg.inv(P.T@P/q)
        M = np.eye(q)/q+(P/q)@(Gi@Gi-Gi)@(P/q).T
        XI = X[I]
        approx = np.einsum('ick,ij,jdk->kcd', XI, M, XI)
        err = np.linalg.norm(approx-full, axis=(1, 2))/np.linalg.norm(full, axis=(1, 2))
        sel_err.append(float(err[1:].max()))
    tau = clock(t, np.linalg.norm(r, axis=1)/math.sqrt(r.shape[1]))
    grid = np.linspace(tau[1], tau[-1], frames)
    idx = np.unique(np.searchsorted(tau, grid).clip(1, len(t)-1))
    dmax = np.abs(D[:, idx]).max(0)
    q8 = lambda v: np.round((np.clip(v, -1, 1)+1)*127.5).astype(np.uint8)
    b64 =lambda A: base64.b64encode(np.ascontiguousarray(A.T).tobytes()).decode()   # frame-major
    return dict(n=n, input=a, dimE=rank, t=sig(t[idx], 3), dmax=sig(dmax, 3),
                h=b64(q8(H[:, idx])), d=b64(q8(D[:, idx]/dmax)), order=order.tolist(),
                selErr=sig(sel_err, 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', type=Path, required=True)
    args = ap.parse_args()
    out = args.data/'json'
    spec = args.data/'spectra'
    out.mkdir(exist_ok=True)
    spec.mkdir(exist_ok=True)
    dump = lambda name, obj: (out/name).write_text(json.dumps(obj, separators=(',', ':'), ensure_ascii=False))
    z = np.load(args.data/'sphere3_t32'/'real.npz')
    d15, d16 = fig15b_16b(z)
    dump('fig15b.json', d15)
    dump('fig16b.json', d16)
    dump('fig21b.json', fig21b(z, spec))
    zl = np.load(args.data/'sphere3_t112'/'long.npz')
    restarts = [(tr, np.load(args.data/'legendre_restarts'/f'rs{tr}.npz')) for tr in (2, 4, 8)]
    dump('fig15c.json', fig15c(zl, restarts))
    d16c, d17c = fig16c_17c(zl)
    dump('fig16c.json', d16c)
    dump('fig17c.json', d17c)
    dump('fig21c.json', fig21c(np.load(args.data/'rich_target'/'rich2.npz'), spec))
    dump('fig19c.json', fig19c(np.load(args.data/'neuron_clouds'/'clouds.npz')))
    print('wrote', sorted(p.name for p in out.iterdir()))


if __name__ == '__main__':
    main()
