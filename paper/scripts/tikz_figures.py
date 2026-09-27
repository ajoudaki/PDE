"""All TikZ figures of the paper.

Regenerates, from scratch:

    mechanism        response memory as a paired memory; the product of errors
    moments          neuron histories summarized by Legendre moments
    trajectory       learning at common physical times       (saved data)
    same_rank        memory vs trained factors at equal rank  (recorded numbers)
    learning_controls_quadrant_alternating  four-method main-text comparison
    learning_controls_gallery_a/b          five-task appendix in two parts
    same_rank_radial_preview  proposed radial alternative     (saved data; preview only)
    frozen_ntk_radial_preview  frozen empirical NTK comparison (saved data; preview only)
    factors          detailed same-rank comparison            (saved data)
    circles_deep     three-hidden-layer circle gallery        (saved data)
    circles_shallow  two-hidden-layer circle gallery          (saved data)
    orders           order trends and numerical sensitivity   (saved data)
    mnist            MNIST agreement and residuals            (saved data)
    clocks           a toy history in physical time and both clocks

Usage (from the repository root or anywhere):

    python paper/scripts/tikz_figures.py            # all figures
    python paper/scripts/tikz_figures.py moments    # a subset

Each figure is TikZ, compiled with pdflatex into paper/figures/<name>.pdf.
Requires numpy and a TeX installation with TikZ.  ``moments`` trains a small
network (a few seconds).  Saved data come from response_memory_source.npz and
radial_source_data.npz in paper/figures; ``same_rank`` uses the numbers in
studies/neural_response_memory_20260922/FACTOR_CONTROL_RESULTS.md.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre as leg

FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"

# ======================================================================
# mechanism

MECHANISM = r"""% Mechanism figure: a learned connection is a paired memory.
\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathreplacing}

\definecolor{fwd}{HTML}{2F6DB5}
\definecolor{bwd}{HTML}{C8553D}
\definecolor{lrn}{HTML}{6B4C9A}
\definecolor{ink}{HTML}{2B2B2B}
\definecolor{mute}{HTML}{8A8A8A}
\definecolor{wz}{HTML}{D9D9D9}

\tikzset{
  >={Stealth[length=2.2mm]},
  lab/.style={font=\footnotesize,text=ink},
  small/.style={font=\scriptsize,text=mute},
  flow/.style={->,line width=0.6pt,draw=ink!70},
  box/.style={draw=ink!25,line width=0.4pt,rounded corners=1.5pt},
}

% A moment vector: an n-vector drawn as a thin column of shaded cells.
% #1 = x, #2 = y (bottom), #3 = colour, #4 = list of shading levels
\newcommand{\momvec}[4]{%
  \foreach \v [count=\i from 0] in {#4}{
    \fill[#3!\v] (#1,#2+0.16*\i) rectangle ++(0.2,0.16);
  }
  \draw[ink!45,line width=0.35pt] (#1,#2) rectangle ++(0.2,0.96);
}

\begin{document}
\begin{tikzpicture}

% ================= panel (a) =================
\node[anchor=west,font=\small\bfseries,text=ink] at (-0.1,5.15)
  {(a) A learned connection is a paired memory};

% --- forward history ---
\draw[box] (0,3.05) rectangle (2.8,4.55);
\draw[fwd,line width=0.9pt,smooth,domain=0.15:2.6,samples=60]
  plot (\x,{3.75+0.42*sin(115*\x)*exp(-0.25*\x)+0.12*\x});
\fill[fwd] (2.6,{3.75+0.42*sin(115*2.6)*exp(-0.25*2.6)+0.12*2.6}) circle (1.6pt);
\node[lab,anchor=south west] at (0,4.55) {forward history $h_a^{(\ell-1)}$};
\node[small,anchor=north] at (1.4,3.05) {clock $\xi\in[0,\tau]$};

% --- backward history ---
\draw[box] (0,0.35) rectangle (2.8,1.85);
\draw[bwd,line width=0.9pt,smooth,domain=0.15:2.6,samples=60]
  plot (\x,{1.1+0.5*exp(-0.9*\x)*cos(170*\x)-0.05*\x});
\fill[bwd] (2.6,{1.1+0.5*exp(-0.9*2.6)*cos(170*2.6)-0.05*2.6}) circle (1.6pt);
\node[lab,anchor=south west] at (0,1.85) {backward history $r_a\delta_a^{(\ell)}/\rho$};
\node[small,anchor=north] at (1.4,0.35) {clock $\xi\in[0,\tau]$};

% --- projections onto moments ---
\draw[flow] (2.9,3.8) -- node[above,small]{$p_k$} (3.55,3.8);
\draw[flow] (2.9,1.1) -- node[above,small]{$p_k$} (3.55,1.1);

% --- moving moment vectors ---
\momvec{3.65}{3.3}{fwd}{55,20,70,35,10,45}
\momvec{4.0}{3.3}{fwd}{15,40,25,60,30,20}
\momvec{4.35}{3.3}{fwd}{30,10,45,15,50,25}
\node[lab] at (4.1,4.52) {$\bar h_{a,0}\,\bar h_{a,1}\,\bar h_{a,2}$};

\momvec{3.65}{0.6}{bwd}{40,65,15,30,55,20}
\momvec{4.0}{0.6}{bwd}{20,15,50,35,10,45}
\momvec{4.35}{0.6}{bwd}{10,35,20,15,40,30}
\node[lab] at (4.1,0.38) {$\bar\delta_{a,0}\,\bar\delta_{a,1}\,\bar\delta_{a,2}$};
\node[small,align=center] at (4.1,2.78) {fixed basis $p_k$,\\[-1pt]moving $n$-vectors};

% --- pairing ---
\coordinate (pair) at (5.95,2.45);
\draw[flow,fwd!80!ink] (4.6,3.8) .. controls (5.4,3.8) and (5.8,3.2) .. ($(pair)+(0,0.26)$);
\draw[flow,bwd!80!ink] (4.6,1.1) .. controls (5.4,1.1) and (5.8,1.7) .. ($(pair)+(0,-0.26)$);
\draw[line width=0.6pt,draw=lrn,fill=white] (pair) circle (0.24);
\node[lrn,font=\small] at (pair) {$\otimes$};
\node[font=\scriptsize,text=lrn,anchor=north,align=center] at (6.95,2.32)
  {$\sum_{a,k}(2k{+}1)$\\[1pt]$\bar\delta_{a,k}\,\bar h_{a,k}^{\!\top}$};
\node[small,anchor=south] at (6.95,2.5) {pair};

% --- reconstruction W = W0 + learned ---
\draw[flow] ($(pair)+(0.26,0)$) -- (7.75,2.45);
\begin{scope}[shift={(7.9,1.75)}]
  \fill[wz] (0,0) rectangle (1.4,1.4);
  \foreach \i in {1,...,6}{\draw[white,line width=0.3pt] (0,0.2*\i) -- (1.4,0.2*\i);
                            \draw[white,line width=0.3pt] (0.2*\i,0) -- (0.2*\i,1.4);}
  \node[lab] at (0.7,0.7) {$W_0^{(\ell)}$};
  \node[small,anchor=north] at (0.7,0) {kept, fixed};
  \node[lab] at (1.65,0.7) {$+$};
  \begin{scope}[shift={(1.9,0)}]
    \draw[ink!25,line width=0.4pt] (0,0) rectangle (1.4,1.4);
    \foreach \a/\o in {0.18/60,0.52/40,0.9/25}{
      \fill[lrn!\o] (0,\a) rectangle (1.4,\a+0.13);
      \fill[lrn!\o,opacity=0.8] (1.2-\a,0) rectangle (1.33-\a,1.4);}
    \node[small,anchor=north] at (0.7,0) {rank $\le mP$};
  \end{scope}
  \node[lab,anchor=south] at (1.65,1.45) {$\widehat W^{(\ell)}$};
\end{scope}

% --- feedback loop ---
\draw[->,line width=0.6pt,draw=lrn!85,rounded corners=6pt]
  (9.55,1.75) -- (9.55,-0.25) -- (-0.35,-0.25) -- (-0.35,2.45);
\draw[->,line width=0.6pt,draw=lrn!85] (-0.35,2.45) |- (-0.02,3.8);
\draw[->,line width=0.6pt,draw=lrn!85] (-0.35,2.45) |- (-0.02,1.1);
\node[small,fill=white,inner sep=1.5pt] at (4.6,-0.25)
  {responses of the reconstructed network feed the next memories};

% ================= panel (b) =================
\begin{scope}[shift={(11.75,0)}]
\node[anchor=west,font=\small\bfseries,text=ink] at (-0.1,5.15) {(b) Why pairing helps};
\node[small,anchor=west] at (-0.1,4.72) {$\int b\,h^{\!\top}$ splits into four pairings};

\def\cw{1.55}\def\ch{0.95}
\coordinate (g) at (0.9,2.05);
% headers
\node[lab] at ($(g)+(0.5*\cw,2*\ch+0.3)$) {$\Pi_P h$};
\node[lab] at ($(g)+(1.5*\cw,2*\ch+0.3)$) {$h-\Pi_P h$};
\node[lab,anchor=east] at ($(g)+(-0.08,1.5*\ch)$) {$\Pi_P b$};
\node[lab,anchor=east] at ($(g)+(-0.08,0.5*\ch)$) {$b-\Pi_P b$};
% cells
\fill[lrn!18] ($(g)+(0,\ch)$) rectangle ++(\cw,\ch);
\fill[bwd!22] (g) ++(\cw,0) rectangle ++(\cw,\ch);
\foreach \i in {0,1,2}{
  \draw[ink!35,line width=0.4pt] ($(g)+(\i*\cw,0)$) -- ++(0,2*\ch);
  \draw[ink!35,line width=0.4pt] ($(g)+(0,\i*\ch)$) -- ++(2*\cw,0);}
\node[lab,align=center] at ($(g)+(0.5*\cw,1.5*\ch)$) {kept\\[-1pt]\scriptsize memory};
\node[lab,text=mute] at ($(g)+(1.5*\cw,1.5*\ch)$) {$0$};
\node[lab,text=mute] at ($(g)+(0.5*\cw,0.5*\ch)$) {$0$};
\node[lab,align=center] at ($(g)+(1.5*\cw,0.5*\ch)$) {defect\\[-1pt]\scriptsize omitted$\times$omitted};
\node[small] at ($(g)+(\cw,-0.25)$) {mixed terms vanish by orthogonality};

% to trajectory error
\draw[flow] ($(g)+(1.5*\cw,-0.45)$) -- ++(0,-0.75)
  node[midway,right,small,align=left] {feedback\\stability};
\node[lab,draw=ink!25,rounded corners=1.5pt,inner sep=3pt,anchor=north]
  at ($(g)+(1.5*\cw,-1.25)$) {trajectory error $O_T(P^{-1})$ or $O_T(P^{-2})$};
\end{scope}

\end{tikzpicture}
\end{document}
"""

# ======================================================================
# moments

def moments():
    """Neuron histories of a small trained network, summarized by P moments."""
    # ------------------------------------------------------------------ training
    rng = np.random.default_rng(3)
    n, m, d = 512, 8, 2
    ang = np.pi / 4 * np.arange(m) + 0.3
    X = np.stack([np.cos(ang), np.sin(ang)], 1)
    y = 0.9 * np.cos(ang) + 0.6 * np.sin(3 * ang)
    W1 = rng.normal(size=(n, d))
    W2 = rng.normal(size=(n, n)) / np.sqrt(n)
    w = rng.normal(size=n) * 0.1
    dt, steps, a = 0.05, 8000, 2
    F, Bk, rhos = [], [], []
    for _ in range(steps):
        h1 = np.tanh(X @ W1.T / np.sqrt(d))
        h2 = np.tanh(h1 @ W2.T)
        r = h2 @ w / n - y
        rho = np.sqrt(np.mean(r**2))
        d2 = w * (1 - h2**2)
        d1 = (1 - h1**2) * (d2 @ W2)
        F.append(h1[a].copy())
        Bk.append(r[a] * d2[a] / rho)
        rhos.append(rho)
        W1 -= dt * (2 / m) * (r[:, None] * d1).T @ X / np.sqrt(d)
        W2 -= dt * (2 / (n * m)) * (r[:, None] * d2).T @ h1
        w -= dt * (2 / m) * (r @ h2)
    F, Bk, rhos = np.array(F), np.array(Bk), np.array(rhos)
    tau = np.concatenate([[0.0], np.cumsum(rhos[:-1] * dt)])


    def window(Z, t_end, grid=1200):
        u = np.linspace(0, t_end, grid)
        return np.stack([np.interp(u, tau, Z[:, i]) for i in range(Z.shape[1])], 1)


    def fit(Zu, P):
        x = np.linspace(-1, 1, Zu.shape[0])
        c = leg.legfit(x, Zu, P - 1)                 # c_k = (2k+1) moment_k / tau
        return c, leg.legval(x, c).T


    rows = [("forward $h$", window(F, tau[-1]), window(F, 0.5 * tau[-1])),
            (r"backward $r\delta/\rho$", window(Bk, tau[-1]), window(Bk, 0.5 * tau[-1]))]
    picks = [[452, 96, 23, 321, 182], [134, 190, 31, 64, 345]]
    cols = ["2F6DB5", "C8553D", "3A8A6B", "6B4C9A", "C09A2B"]

    # ------------------------------------------------------------------ drawing
    PW, PH, GX, GY = 4.6, 2.0, 0.5, 0.55
    out = []
    emit = out.append
    emit(r"""% Generated by tikz_figures.py -- do not edit by hand.
    \documentclass[tikz,border=3pt]{standalone}
    \usepackage{amsmath,amssymb}
    \usetikzlibrary{arrows.meta}
    \definecolor{ink}{HTML}{2B2B2B}
    \definecolor{mute}{HTML}{8A8A8A}""")
    for i, c in enumerate(cols):
        emit(r"\definecolor{n%d}{HTML}{%s}" % (i, c))
    emit(r"""\begin{document}
    \begin{tikzpicture}[font=\footnotesize,>={Stealth[length=1.6mm]}]""")

    # column headers with a sketch of the mode each order adds
    heads = ["mean", "$+$ linear trend", "$+$ quadratic shape"]
    modes = [lambda s: 0 * s, lambda s: s, lambda s: 1.5 * s**2 - 0.5]
    for j in range(3):
        x0 = j * (PW + GX)
        cx, cy = x0 + 0.1, PH + 0.62
        ss = np.linspace(-1, 1, 25)
        emit(r"\draw[ink,line width=0.8pt] " + " -- ".join(
            "(%.3f,%.3f)" % (cx + 0.35 * (v + 1), cy + 0.13 * modes[j](v)) for v in ss) + ";")
        emit(r"\node[anchor=west,text=ink] at (%.3f,%.3f) {$P=%d$: %s};" % (x0 + 1.05, cy, j + 1, heads[j]))

    LANES = len(picks[0])
    for ri, (rname, Zend, Zmid) in enumerate(rows):
        y0 = -ri * (PH + GY)
        fits = [fit(Zend, P)[1] for P in (1, 2, 3)]
        span = Zend.max(0) - Zend.min(0)
        lane = PH / LANES
        emit(r"\node[anchor=east,text=ink,align=right] at (-0.15,%.3f) {%s};" % (y0 + 0.5 * PH, rname))
        sel = np.linspace(0, Zend.shape[0] - 1, 200).astype(int)
        for j, P in enumerate((1, 2, 3)):
            x0 = j * (PW + GX)
            f = fits[j]
            med = np.median(np.sqrt(np.mean((f - Zend) ** 2, 0)) / np.maximum(span, 1e-12))
            Xp = lambda k: x0 + PW * k / (Zend.shape[0] - 1)
            emit(r"\fill[ink!3] (%.3f,%.3f) rectangle (%.3f,%.3f);" % (x0, y0, x0 + PW, y0 + PH))
            for q, i in enumerate(picks[ri]):
                vals = np.concatenate([Zend[:, i], *(g[:, i] for g in fits)])
                lo, hi = vals.min(), vals.max()
                base = y0 + PH - (q + 1) * lane
                Yp = lambda v: base + 0.1 * lane + 0.8 * lane * (v - lo) / (hi - lo)
                emit(r"\draw[n%d,line width=0.9pt] " % q +
                     " -- ".join("(%.3f,%.3f)" % (Xp(k), Yp(Zend[k, i])) for k in sel) + ";")
                emit(r"\draw[ink!75,line width=0.6pt,dash pattern=on 2.0pt off 1.4pt] " +
                     " -- ".join("(%.3f,%.3f)" % (Xp(k), Yp(f[k, i])) for k in sel) + ";")
            emit(r"\node[anchor=south east,text=mute,font=\scriptsize,inner sep=1pt] "
                 r"at (%.3f,%.3f) {median error $%.0f\%%$ of range};" % (x0 + PW, y0 + PH + 0.02, 100 * med))
            if ri == 1:
                emit(r"\node[anchor=north,text=mute,font=\scriptsize] at (%.3f,%.3f) {start};" % (x0 + 0.2, y0))
                emit(r"\node[anchor=north,text=mute,font=\scriptsize] at (%.3f,%.3f) {now};" % (x0 + PW - 0.2, y0))

    # legend for top block
    yl = -(PH + GY) - 0.62
    emit(r"\draw[ink,line width=0.9pt] (%.3f,%.3f) -- ++(0.45,0) node[right,text=ink] {history of five neurons};" % (0.2 + (PW + GX), yl))
    emit(r"\draw[ink!75,line width=0.6pt,dash pattern=on 2.0pt off 1.4pt] (%.3f,%.3f) -- ++(0.45,0) "
         r"node[right,text=ink] {kept by $P$ moments};" % (0.2 + 2 * (PW + GX), yl))
    emit(r"\node[anchor=west,text=mute,font=\scriptsize] at (0,%.3f) {learning clock, start to now};" % yl)

    # ------------------------------------------------------------------ populations
    emit(r"\node[anchor=west,font=\small\bfseries,text=ink] at (-2.3,%.3f) {Across all %d neurons, each moment is a population};"
         % (yl - 0.75, n))
    RH = 0.75
    R0 = yl - 0.75 - 0.35 - RH - 0.3


    def kde(v, grid):
        bw = 1.06 * v.std() * len(v) ** (-0.2)
        return np.exp(-0.5 * ((grid[:, None] - v[None]) / bw) ** 2).sum(1)


    for ri, (rname, Zend, Zmid) in enumerate(rows):
        base = R0 - ri * (RH + 0.45)
        Ce, Cm = fit(Zend, 3)[0], fit(Zmid, 3)[0]
        emit(r"\node[anchor=east,text=ink] at (-0.15,%.3f) {%s};" % (base + 0.3 * RH, rname))
        for k in range(3):
            x0 = k * (PW + GX)
            both = np.concatenate([Ce[k], Cm[k]])
            g0, g1 = np.percentile(both, 1), np.percentile(both, 99)
            grid = np.linspace(g0 - 0.12 * (g1 - g0), g1 + 0.12 * (g1 - g0), 200)
            de, dm = kde(Ce[k], grid), kde(Cm[k], grid)
            top = max(de.max(), dm.max())
            Xg = lambda v: x0 + PW * (v - grid[0]) / (grid[-1] - grid[0])
            Yd = lambda v: base + RH * v / top
            emit(r"\fill[ink!9] (%.3f,%.3f) -- " % (Xg(grid[0]), base) +
                 " -- ".join("(%.3f,%.3f)" % (Xg(g), Yd(v)) for g, v in zip(grid, de)) +
                 r" -- (%.3f,%.3f) -- cycle;" % (Xg(grid[-1]), base))
            emit(r"\draw[ink!65,line width=0.7pt] " +
                 " -- ".join("(%.3f,%.3f)" % (Xg(g), Yd(v)) for g, v in zip(grid, de)) + ";")
            emit(r"\draw[ink!40,line width=0.6pt,dash pattern=on 1.8pt off 1.3pt] " +
                 " -- ".join("(%.3f,%.3f)" % (Xg(g), Yd(v)) for g, v in zip(grid, dm)) + ";")
            emit(r"\draw[ink!25,line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);" % (x0, base, x0 + PW, base))
            for q, i in enumerate(picks[ri]):
                v = Ce[k, i]
                if grid[0] <= v <= grid[-1]:
                    emit(r"\draw[n%d,line width=1.2pt] (%.3f,%.3f) -- ++(0,-0.16);" % (q, Xg(v), base))
            if ri == 0:
                emit(r"\node[anchor=south,text=mute,font=\scriptsize] at (%.3f,%.3f) {moment $k=%d$};"
                     % (x0 + 0.5 * PW, base + RH + 0.02, k))
    yb = R0 - (RH + 0.45) - 0.45
    emit(r"\draw[ink!65,line width=0.7pt] (%.3f,%.3f) -- ++(0.45,0) node[right,text=ink] {now};" % (0.2 + (PW + GX), yb))
    emit(r"\draw[ink!40,line width=0.6pt,dash pattern=on 1.8pt off 1.3pt] (%.3f,%.3f) -- ++(0.45,0) node[right,text=ink] {halfway, in the clock};"
         % (1.6 + (PW + GX), yb))
    emit(r"\draw[n0,line width=1.2pt] (%.3f,%.3f) -- ++(0,-0.16) node[right=2pt,text=ink,anchor=west] {the five neurons above};"
         % (0.25 + 2 * (PW + GX), yb + 0.08))
    emit(r"\end{tikzpicture}")
    emit(r"\end{document}")
    return "\n".join(out) + "\n"


# ======================================================================
# Saved-data figures, redrawn in the same style as the explanatory ones.
# Data: paper/figures/response_memory_source.npz (trajectory, factors, orders,
# MNIST) and paper/figures/radial_source_data.npz (circle galleries).

RESPONSE_BUNDLE = FIGURES_DIR / "response_memory_source.npz"
RADIAL_BUNDLE = FIGURES_DIR / "radial_source_data.npz"

PREAMBLE = r"""\documentclass[tikz,border=3pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,calc}
\definecolor{fwd}{HTML}{2F6DB5}
\definecolor{bwd}{HTML}{C8553D}
\definecolor{lrn}{HTML}{6B4C9A}
\definecolor{grn}{HTML}{3A8A6B}
\definecolor{gold}{HTML}{C09A2B}
\definecolor{ink}{HTML}{2B2B2B}
\definecolor{mute}{HTML}{8A8A8A}
\begin{document}
\begin{tikzpicture}[font=\footnotesize,>={Stealth[length=1.8mm]}]
"""
POSTAMBLE = "\\end{tikzpicture}\n\\end{document}\n"
ORDER_COLOR = {0: "ink", 1: "bwd", 2: "gold", 3: "lrn", 7: "grn"}
TASKS = ["two_outliers_alternating", "quadrant_alternating", "quadrant_pairs",
         "quadrant_center_edges", "equal_mixed_odd"]
TASK_NAMES = ["Two outliers, alternating", "Quadrant, alternating", "Quadrant, paired labels",
              "Quadrant, center/edges", "Equally spaced, mixed"]
TASK_COLOR = ["fwd", "bwd", "grn", "lrn", "gold"]
TASK_SHORT = ["outliers, alternating", "quadrant, alternating", "quadrant, paired",
              "quadrant, center/edges", "equally spaced, mixed"]


def _pts(xs, ys):
    return " -- ".join(f"({x:.3f},{y:.3f})" for x, y in zip(xs, ys))


def _response_bundle():
    import json
    with np.load(RESPONSE_BUNDLE, allow_pickle=False) as z:
        meta = json.loads(str(z["metadata_json"]))
        arrays = {k: z[k] for k in z.files if k != "metadata_json"}
    return arrays, meta


class Axes:
    """A rectangular panel with linear or logarithmic axes, drawn in TikZ."""

    def __init__(self, out, x0, y0, w, h, xlim, ylim, xlog=False, ylog=False):
        self.out, self.x0, self.y0, self.w, self.h = out, x0, y0, w, h
        self.xlim, self.ylim, self.xlog, self.ylog = xlim, ylim, xlog, ylog

    def _t(self, v, lim, log):
        v = np.log10(v) if log else np.asarray(v, float)
        a, b = (np.log10(lim[0]), np.log10(lim[1])) if log else lim
        return (v - a) / (b - a)

    def X(self, v):
        return self.x0 + self.w * self._t(v, self.xlim, self.xlog)

    def Y(self, v):
        return self.y0 + self.h * self._t(v, self.ylim, self.ylog)

    def frame(self, xticks=(), yticks=(), xlabels=None, ylabels=None, ygrid=True, xgrid=False):
        o = self.out
        for k, t in enumerate(yticks):
            y = self.Y(t)
            if ygrid:
                o.append(r"\draw[ink!8,line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);" % (self.x0, y, self.x0 + self.w, y))
            lab = ylabels[k] if ylabels else f"${t:g}$"
            o.append(r"\node[anchor=east,text=mute,font=\scriptsize,inner sep=1.5pt] at (%.3f,%.3f) {%s};" % (self.x0, y, lab))
        for k, t in enumerate(xticks):
            x = self.X(t)
            if xgrid:
                o.append(r"\draw[ink!8,line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f);" % (x, self.y0, x, self.y0 + self.h))
            o.append(r"\draw[ink!30,line width=0.4pt] (%.3f,%.3f) -- ++(0,-0.06);" % (x, self.y0))
            lab = xlabels[k] if xlabels else f"${t:g}$"
            o.append(r"\node[anchor=north,text=mute,font=\scriptsize,inner sep=2pt] at (%.3f,%.3f) {%s};" % (x, self.y0 - 0.04, lab))
        o.append(r"\draw[ink!30,line width=0.45pt] (%.3f,%.3f) -- (%.3f,%.3f);" % (self.x0, self.y0, self.x0 + self.w, self.y0))

    def line(self, xs, ys, style):
        self.out.append(r"\draw[%s] %s;" % (style, _pts(self.X(np.asarray(xs)), self.Y(np.asarray(ys)))))

    def marks(self, xs, ys, style, r=1.4):
        for x, y in zip(np.atleast_1d(xs), np.atleast_1d(ys)):
            self.out.append(r"\filldraw[%s] (%.3f,%.3f) circle (%.2fpt);" % (style, self.X(x), self.Y(y), r))

    def title(self, text, anchor="south west"):
        self.out.append(r"\node[anchor=%s,text=ink,inner sep=1pt,font=\scriptsize] at (%.3f,%.3f) {%s};"
                        % (anchor, self.x0 if "west" in anchor else self.x0 + 0.5 * self.w, self.y0 + self.h + 0.08, text))

    def xlabel(self, text):
        self.out.append(r"\node[anchor=north,text=ink] at (%.3f,%.3f) {%s};" % (self.x0 + 0.5 * self.w, self.y0 - 0.38, text))

    def ylabel(self, text, off=0.75):
        self.out.append(r"\node[rotate=90,anchor=south,text=ink] at (%.3f,%.3f) {%s};" % (self.x0 - off, self.y0 + 0.5 * self.h, text))


def _log_ticks(lo, hi):
    return [10.0 ** e for e in range(int(np.ceil(np.log10(lo) - 1e-9)), int(np.floor(np.log10(hi) + 1e-9)) + 1)]


def _pow_label(t):
    e = int(round(np.log10(t)))
    return "$1$" if e == 0 else f"$10^{{{e}}}$"


def polar(out, cx, cy, s, angles, curves, train=None, labels=None, ring_labels=False,
          offset=3., rings=(-1, 0, 1), value_scale=1.):
    """Radius s*(offset+f/value_scale); ticks remain in physical output units."""
    for f in rings:
        if f != 0:
            out.append(r"\draw[ink!9,line width=0.4pt] (%.3f,%.3f) circle (%.3f);" % (cx, cy, s * (offset + f/value_scale)))
    out.append(r"\draw[ink!28,line width=0.4pt,dash pattern=on 1.2pt off 1.2pt] (%.3f,%.3f) circle (%.3f);" % (cx, cy, offset * s))
    if ring_labels:
        for f in rings:
            lab = f"${f:+g}$" if f else "$0$"
            out.append(r"\node[text=mute,font=\tiny,inner sep=0.5pt,anchor=south west] at (%.3f,%.3f) {%s};"
                       % (cx + 0.03, cy + s * (offset + f/value_scale) - 0.02, lab))
    sel = np.linspace(0, len(angles) - 1, 720).astype(int)
    for values, style in curves:
        r = s * (offset + values[sel]/value_scale)
        xs, ys = cx + r * np.cos(angles[sel]), cy + r * np.sin(angles[sel])
        out.append(r"\draw[%s] %s -- cycle;" % (style, _pts(xs, ys)))
    if train is not None:
        for ang, lab in zip(train, labels):
            r = s * (offset + lab/value_scale)
            out.append(r"\fill[ink] (%.3f,%.3f) circle (1.3pt);" % (cx + r * np.cos(ang), cy + r * np.sin(ang)))


def _legend_row(out, x, y, items, spacing):
    for (style, label, kind), dx in zip(items, spacing):
        if kind == "dot":
            out.append(r"\fill[%s] (%.3f,%.3f) circle (1.4pt);" % (style, x + 0.12, y))
        else:
            out.append(r"\draw[%s] (%.3f,%.3f) -- ++(0.45,0);" % (style, x, y))
        out.append(r"\node[anchor=west,text=ink,inner sep=1pt] at (%.3f,%.3f) {%s};" % (x + 0.52, y, label))
        x += dx


ORDER_STYLE = {0: "ink,line width=1.1pt", 1: "bwd,line width=0.75pt", 2: "gold,line width=0.75pt",
               3: "lrn,line width=0.8pt", 7: "grn,line width=0.8pt,dash pattern=on 2.4pt off 1.4pt"}


def trajectory():
    a, meta = _response_bundle()
    out = [PREAMBLE]
    times = a["common_times"]
    ang = a["history_angles"]
    train = np.arctan2(a["train_inputs"][:, 1], a["train_inputs"][:, 0])
    s, W = 0.34, 4.15
    for j, t in enumerate([0, 5, 20, 80]):
        i = int(np.flatnonzero(times == t)[0])
        cx = 1.75 + j * W
        curves = [(a["common_dense"][i], ORDER_STYLE[0])]
        curves += [(a[f"common_memory_{p}"][i], ORDER_STYLE[p]) for p in (1, 3, 7)]
        polar(out, cx, 0, s, ang, curves, train, a["train_labels"])
        out.append(r"\node[text=ink] at (%.3f,%.3f) {$t=%d$};" % (cx, 1.95, t))
    _legend_row(out, 2.3, -1.95, [(ORDER_STYLE[0], "dense", "line"), (ORDER_STYLE[1], "$P=1$", "line"),
                                  (ORDER_STYLE[3], "$P=3$", "line"), (ORDER_STYLE[7], "$P=7$", "line"),
                                  ("ink", "training labels", "dot")], [2.2, 2.0, 2.0, 2.0, 2.0])
    positive = times > 0
    rms = {p: a[f"common_rms_{p}"][positive] for p in (1, 3, 7)}
    sen = {p: a[f"common_sensitivity_{p}"][positive] for p in (1, 3, 7)}
    shown_times = times[positive]
    if not (np.all(np.diff(times) > 0) and all(np.all(v > 0) for v in rms.values())
            and all(np.all(v > 0) for v in sen.values())):
        raise ValueError("Trajectory log axes require increasing times and positive measurements")
    lo = 10 ** np.floor(np.log10(min(min(v.min() for v in rms.values()), min(v.min() for v in sen.values()))))
    hi = 10 ** np.ceil(np.log10(max(v.max() for v in rms.values())))
    ax = Axes(out, 1.2, -6.1, 11.0, 3.0, (shown_times[0], shown_times[-1]),
              (lo, hi), xlog=True, ylog=True)
    yt = _log_ticks(lo, hi)[::2]
    xticks = [t for t in [.5, 1, 2, 5, 10, 20, 40, 80] if shown_times[0] <= t <= shown_times[-1]]
    ax.frame(xticks=xticks, yticks=yt, ylabels=[_pow_label(t) for t in yt])
    # Shading is a numerical sensitivity scale from the axis floor up to the
    # coarse/fine change, not a confidence band around the measured error.
    for p in (1, 3, 7):
        c = ORDER_COLOR[p]
        boundary = _pts(ax.X(shown_times), ax.Y(np.maximum(sen[p], lo)))
        out.append(r"\fill[%s,opacity=0.08] (%.3f,%.3f) -- %s -- (%.3f,%.3f) -- cycle;"
                   % (c, ax.X(shown_times[0]), ax.y0, boundary, ax.X(shown_times[-1]), ax.y0))
    for p in (1, 3, 7):
        c = ORDER_COLOR[p]
        ax.line(shown_times, rms[p], f"{c},line width=0.45pt")
        ax.marks(shown_times, rms[p], f"{c},draw=white,line width=0.25pt", 1.35)
    ax.xlabel("physical training time $t$ (log scale)")
    ax.ylabel("RMS difference from dense", off=0.85)
    x0 = 12.6
    out.append(r"\node[anchor=west,text=ink] at (%.3f,-3.35) {%d shared times};" % (x0, len(times)))
    out.append(r"\filldraw[ink,draw=white,line width=0.25pt] (%.3f,-3.85) circle (1.35pt);" % (x0 + .225))
    out.append(r"\node[anchor=west,text=ink,font=\scriptsize] at (%.3f,-3.85) {measured on $2048$ angles};" % (x0 + .52))
    out.append(r"\draw[ink,line width=0.45pt] (%.3f,-4.3) -- ++(0.45,0);" % x0)
    out.append(r"\node[anchor=west,text=ink,font=\scriptsize] at (%.3f,-4.3) {lines guide the eye};" % (x0 + .52))
    out.append(r"\fill[ink,opacity=0.12] (%.3f,-4.86) rectangle ++(0.45,0.2);" % x0)
    out.append(r"\node[anchor=west,text=ink,font=\scriptsize,align=left] at (%.3f,-4.76) {coarse/fine sensitivity\\not an error bound};" % (x0 + .52))
    out.append(POSTAMBLE)
    return "\n".join(out)


def factors():
    a, meta = _response_bundle()
    out = [PREAMBLE]
    ang = a["factor_angles"]
    train = np.arctan2(a["train_inputs"][:, 1], a["train_inputs"][:, 0])
    lab = a["train_labels"]
    s, W = 0.34, 5.4
    rr = meta["factor_radial_rms"]
    panels = [("dense training", [(a["factor_dense"], ORDER_STYLE[0])], ""),
              ("response memory, $P=3$", [(a["factor_dense"], "ink!45,line width=1.4pt"),
                                          (a["memory_endpoint_3"], "lrn,line width=0.8pt")],
               "RMS difference $%.4f$" % rr["P3"]),
              (r"trained factors $W_0+AB$", [(a["factor_dense"], "ink!45,line width=1.4pt"),
                                            (a["factor_seed_20260924"], "bwd,line width=0.8pt"),
                                            (a["factor_seed_20260925"], "bwd,line width=0.8pt,dash pattern=on 2.4pt off 1.4pt")],
               "RMS difference $%.3f$ and $%.3f$" % (rr["20260924"], rr["20260925"]))]
    for j, (title, curves, note) in enumerate(panels):
        cx = 2.4 + j * W
        polar(out, cx, 0, s, ang, curves, train, lab)
        out.append(r"\node[text=ink] at (%.3f,1.95) {%s};" % (cx, title))
        if note:
            out.append(r"\node[text=mute,font=\scriptsize] at (%.3f,-1.85) {%s};" % (cx, note))
    out.append(r"\node[text=mute,font=\scriptsize] at (%.3f,-1.85) {quadrant, paired labels; rank $24$};" % 2.4)
    # bottom: error against rank bound, all tasks
    lo, hi = 1e-7, 3.0
    PW, GX, y0 = 2.72, 0.42, -5.6
    for i, case in enumerate(TASKS):
        mem = sorted([r for r in meta["factor_memory"] if r["case"] == case], key=lambda r: r["rank"])
        ranks = [r["rank"] for r in mem]
        ax = Axes(out, 0.9 + i * (PW + GX), y0, PW, 2.3, (ranks[0] / 1.35, ranks[-1] * 1.35), (lo, hi), xlog=True, ylog=True)
        yt = [1e-6, 1e-3, 1]
        ax.frame(xticks=ranks, yticks=yt, ylabels=[_pow_label(t) for t in yt] if i == 0 else [""] * 3)
        for seed, style in [(20260924, "bwd,line width=0.75pt"), (20260925, "bwd,line width=0.75pt,dash pattern=on 2.4pt off 1.4pt")]:
            rows = sorted([r for r in meta["factor_direct"] if r["case"] == case and r["factor_seed"] == seed and r["valid"]],
                          key=lambda r: r["rank"])
            xs, ys = [r["rank"] for r in rows], [r["circle_rms"] for r in rows]
            if xs:
                ax.line(xs, ys, style)
                for x, y in zip(xs, ys):
                    out.append(r"\filldraw[bwd,fill=white,line width=0.6pt] (%.3f,%.3f) rectangle ++(0.07,0.07);"
                               % (ax.X(x) - 0.035, ax.Y(y) - 0.035))
        xs = [r["rank"] for r in mem if r["valid"]]
        ys = [r["circle_rms"] for r in mem if r["valid"]]
        ax.line(xs, ys, "lrn,line width=0.85pt")
        for r in mem:
            if r["valid"]:
                fill = "white" if r["precision_limited"] else "lrn"
                out.append(r"\filldraw[lrn,fill=%s,line width=0.6pt] (%.3f,%.3f) circle (1.6pt);"
                           % (fill, ax.X(r["rank"]), ax.Y(r["circle_rms"])))
        ax.title(TASK_SHORT[i], anchor="south")
        if i == 2:
            ax.xlabel("rank of the learned correction")
    out.append(r"\node[rotate=90,anchor=south,text=ink] at (0.2,%.3f) {RMS difference};" % (y0 + 1.15))
    _legend_row(out, 3.2, -2.55, [("lrn,line width=0.85pt", "response memory", "line"),
                                  ("bwd,line width=0.75pt", "factors, seed 1", "line"),
                                  ("bwd,line width=0.75pt,dash pattern=on 2.4pt off 1.4pt", "factors, seed 2", "line")],
               [3.4, 3.0, 3.0])
    out.append(POSTAMBLE)
    return "\n".join(out)


def same_rank_radial_preview():
    """One-task radial alternative to Figure 4; does not change the manuscript."""
    a, meta = _response_bundle()
    angles, dense = a["factor_angles"], a["factor_dense"]
    train = np.arctan2(a["train_inputs"][:, 1], a["train_inputs"][:, 0])
    labels = a["train_labels"]
    memory = a["memory_endpoint_3"]
    factor = [a[f"factor_seed_{seed}"] for seed in (20260924, 20260925)]
    values = [memory, *factor]
    measured = [float(np.sqrt(np.mean((v-dense)**2))) for v in values]
    recorded = [meta["factor_radial_rms"][key] for key in ("P3", "20260924", "20260925")]
    if not np.allclose(measured, recorded, rtol=1e-12, atol=1e-14):
        raise ValueError("Radial factor-preview metrics differ from the saved records")
    if not all(v.shape == angles.shape and np.isfinite(v).all() and np.min(3+v) > 0
               for v in [dense, *values]):
        raise ValueError("Radial plots require matching finite arrays and positive radii")

    out = [PREAMBLE]
    scale, centers = .42, [2.1, 7.7, 13.3]
    dense_style = "ink,line width=1.15pt"
    reference_style = "ink!35,line width=1.8pt"
    memory_style = "lrn,line width=1.0pt"
    factor_styles = ["bwd,line width=1.0pt",
                     "bwd,line width=0.9pt,dash pattern=on 3pt off 1.8pt"]

    # Fill between the actual saved prediction and the dense reference using
    # the same radius and angle mapping. This is a visual gap, not an error band.
    select = np.linspace(0, len(angles)-1, 720).astype(int)
    theta = angles[select]
    def shade_gap(cx, prediction, color, opacity):
        rr = scale*(3+prediction[select])
        rd = scale*(3+dense[select])
        forward = _pts(cx+rr*np.cos(theta), rr*np.sin(theta))
        backward = _pts((cx+rd*np.cos(theta))[::-1], (rd*np.sin(theta))[::-1])
        out.append(r"\fill[%s,opacity=%.3f,even odd rule] %s -- %s -- cycle;"
                   % (color, opacity, forward, backward))

    for f in factor:
        shade_gap(centers[0], f, "bwd", .10)
    shade_gap(centers[2], memory, "lrn", .16)
    panels = [
        ("Trained factors", "bwd", [(dense, reference_style),
                                     *zip(factor, factor_styles)], r"$W_0+AB$, rank $24$"),
        ("Dense network", "ink", [(dense, dense_style)], "reference predictor"),
        ("Response memory", "lrn", [(dense, reference_style),
                                      (memory, memory_style)], r"$P=3$, rank bound $24$"),
    ]
    for cx, (title, color, curves, detail) in zip(centers, panels):
        polar(out, cx, 0, scale, angles, curves, train, labels, ring_labels=True)
        out.append(r"\node[text=%s,font=\small] at (%.3f,2.65) {%s};" % (color,cx,title))
        out.append(r"\node[text=mute,font=\scriptsize] at (%.3f,2.27) {%s};" % (cx,detail))
    out.append(r"\node[text=ink,font=\small] at (7.7,3.55) {Same training fit, different predictions between samples};")

    # The two red curves distinguish seeds of the same factor-training baseline.
    for k, (style, error) in enumerate(zip(factor_styles, measured[1:])):
        y = -2.28 - .36*k
        out.append(r"\draw[%s] (0.45,%.3f) -- ++(.45,0);" % (style,y))
        out.append(r"\node[anchor=west,text=bwd,font=\scriptsize] at (1.0,%.3f) {seed %d: RMS $%.3f$};"
                   % (y,k+1,error))
    out.append(r"\node[text=lrn,font=\scriptsize] at (%.3f,-2.28) {RMS $%.5f$};" % (centers[2],measured[0]))
    out.append(r"\node[text=mute,font=\scriptsize] at (%.3f,-2.64) {almost coincides with dense};" % centers[2])
    _legend_row(out, 5.7, -2.28, [(reference_style, "dense reference", "line")], [2.])
    _legend_row(out, 5.7, -2.64, [("ink", "training labels", "dot")], [2.])
    out.append(r"\node[text=ink,font=\scriptsize,align=center] at (7.7,-3.38) {"
               r"Every model reaches training MSE $0.001$ on the same eight points.\\"
               r"RMS compares fitted predictions with dense on $8192$ circle queries; radius is $3+f(\theta)$.};")
    out.append(POSTAMBLE)
    return "\n".join(out)


def frozen_ntk_radial_preview():
    """Matched-loss frozen empirical NTK, dense, and memory on a common scale."""
    import json
    with np.load(FIGURES_DIR / "frozen_ntk_source.npz", allow_pickle=False) as z:
        a = {key:z[key] for key in z.files if key != "metadata_json"}
        meta = json.loads(str(z['metadata_json']))
    angles, dense, frozen, memory = (a[k] for k in ('angles','dense','frozen_ntk','memory'))
    errors = meta['full_circle_rms_vs_dense']
    for key, prediction in [('frozen_ntk',frozen),('memory_P3',memory)]:
        actual = float(np.sqrt(np.mean((prediction-dense)**2)))
        if not np.isclose(actual, errors[key], rtol=1e-12, atol=1e-14):
            raise ValueError('Frozen-NTK preview metric mismatch')
    train = np.arctan2(a['train_inputs'][:,1],a['train_inputs'][:,0])
    # The NTK reaches +/-25.3, so the standard radius 3+f would reverse angles.
    # Use one explicitly labelled larger linear scale for every panel.
    offset, scale, centers = 30., .035, [2.1,7.7,13.3]
    if min(float(v.min()) for v in [dense,frozen,memory]) <= -offset:
        raise ValueError('Increase the common radial offset; never fold negative radii')
    out=[PREAMBLE]
    reference_style='ink!35,line width=1.8pt'
    sel=np.linspace(0,len(angles)-1,720).astype(int)
    theta=angles[sel]
    r0=scale*(offset+dense[sel]); rf=scale*(offset+frozen[sel])
    x0,y0=centers[0]+r0*np.cos(theta),r0*np.sin(theta)
    xf,yf=centers[0]+rf*np.cos(theta),rf*np.sin(theta)
    out.append(r"\fill[fwd,opacity=.12,even odd rule] %s -- %s -- cycle;"
               % (_pts(xf,yf),_pts(x0[::-1],y0[::-1])))
    panels=[('Frozen NTK','fwd',[(dense,reference_style),(frozen,'fwd,line width=1.0pt')],
             r'$K(t)=K(0)$, all parameter blocks'),
            ('Dense network','ink',[(dense,'ink,line width=1.1pt')], 'reference predictor'),
            ('Response memory','lrn',[(dense,reference_style),(memory,'lrn,line width=1pt')],r'$P=3$')]
    for cx,(title,color,curves,detail) in zip(centers,panels):
        polar(out,cx,0,scale,angles,curves,train,a['train_labels'],True,
              offset=offset,rings=(-20,-10,0,10,20))
        out.append(r"\node[text=%s,font=\small] at (%.3f,2.65) {%s};" % (color,cx,title))
        out.append(r"\node[text=mute,font=\scriptsize] at (%.3f,2.27) {%s};" % (cx,detail))
    out.append(r"\node[text=ink,font=\small] at (7.7,3.55) {The frozen kernel fits the labels but selects a different function};")
    out.append(r"\node[text=fwd,font=\scriptsize] at (2.1,-2.28) {RMS from dense $%.2f$};" % errors['frozen_ntk'])
    out.append(r"\node[text=fwd,font=\scriptsize] at (2.1,-2.64) {output range $[-25.34,25.34]$};")
    out.append(r"\node[text=lrn,font=\scriptsize] at (13.3,-2.28) {RMS from dense $%.5f$};" % errors['memory_P3'])
    out.append(r"\node[text=mute,font=\scriptsize] at (13.3,-2.64) {dense and memory stay near $\pm1.27$};")
    _legend_row(out,5.7,-2.28,[(reference_style,'dense reference','line')],[2.])
    _legend_row(out,5.7,-2.64,[('ink','training labels','dot')],[2.])
    out.append(r"\node[text=ink,font=\scriptsize,align=center] at (7.7,-3.48) {"
               r"Same initialization, canonical learning rates, eight training points and training MSE $0.001$.\\"
               r"All panels use the same linear radial scale: $30+f(\theta)$; ticks show signed output. RMS uses $8192$ queries.};")
    out.append(POSTAMBLE)
    return '\n'.join(out)


def learning_controls_preview(indices):
    """Four methods per row, both factor seeds; wider NTK units are explicit."""
    import json
    with np.load(FIGURES_DIR/'learning_controls_source.npz',allow_pickle=False) as z:
        a={k:z[k] for k in z.files if k!='metadata_json'}
        meta=json.loads(str(z['metadata_json']))
    out=[PREAMBLE]
    centers=[2.,6.5,11.,15.5]
    ref='ink!35,line width=1.7pt'
    for row,i in enumerate(indices):
        p=f'case_{i}_'; info=meta['tasks'][i]; cy=-6.35*row
        angles,dense,ntk,memory,factors=[a[p+k] for k in ['angles','dense','frozen_ntk','memory','factors']]
        train=np.arctan2(a[p+'train_inputs'][:,1],a[p+'train_inputs'][:,0])
        labels=a[p+'train_labels']
        errors=info['rms_vs_dense']
        for pred,expected in [(ntk,errors['frozen_ntk']),(memory,errors['memory']),
                              *zip(factors,errors['factors'])]:
            assert np.isclose(np.sqrt(np.mean((pred-dense)**2)),expected,rtol=1e-12)
        bound=max(np.abs(dense).max(),np.abs(memory).max(),np.abs(factors).max())
        offset=max(3.,float(np.ceil(bound+.5)))
        ntk_bound=np.abs(ntk).max()
        divisor=next(float(v) for v in (1,2,5,10,20,50,100,200,500,1000,2000)
                     if ntk_bound/v<offset-.2)
        scale=1.85/(offset+max(bound,ntk_bound/divisor))
        panels=[('Dense network','ink',[(dense,'ink,line width=1pt')],1.,'reference predictor'),
                ('Frozen NTK','fwd',[(dense,ref),(ntk,'fwd,line width=1pt')],divisor,
                 r'initial kernel, all blocks'),
                ('Trained factors','bwd',[(dense,ref),(factors[0],'bwd,line width=.95pt'),
                    (factors[1],'bwd,line width=.85pt,dash pattern=on 2.8pt off 1.6pt')],1.,
                    r'$W_0+AB$, rank $%d$'%info['rank']),
                ('Response memory','lrn',[(dense,ref),(memory,'lrn,line width=1pt')],1.,
                    r'$P=3$, rank bound $%d$'%info['rank'])]
        for col,(title,color,curves,unit,detail) in enumerate(panels):
            cx=centers[col]
            sel=np.linspace(0,len(angles)-1,720).astype(int); theta=angles[sel]
            if col:
                for prediction,_ in curves[1:]:
                    rd=scale*(offset+dense[sel]/unit); rr=scale*(offset+prediction[sel]/unit)
                    out.append(r'\fill[%s,opacity=.11,even odd rule] %s -- %s -- cycle;'%
                        (color,_pts(cx+rr*np.cos(theta),cy+rr*np.sin(theta)),
                         _pts((cx+rd*np.cos(theta))[::-1],(cy+rd*np.sin(theta))[::-1])))
            polar(out,cx,cy,scale,angles,curves,train,labels,True,offset=offset,
                  rings=(-unit,0,unit),value_scale=unit)
            out.append(r'\node[text=%s,font=\small] at (%.3f,%.3f) {%s};'%(color,cx,cy+2.4,title))
            out.append(r'\node[text=mute,font=\scriptsize] at (%.3f,%.3f) {%s};'%(cx,cy+2.08,detail))
        out.append(r'\node[anchor=west,text=ink,font=\small\bfseries] at (-.1,%.3f) {%s};'%
                   (cy+3.12,TASK_NAMES[i]))
        e=[r'reference',r'RMS $%.4g$'%errors['frozen_ntk'],
           r'RMS $%.4g\;/\;%.4g$'%tuple(errors['factors']),r'RMS $%.4g$'%errors['memory']]
        details=['',r'output scale $\times %g$'%divisor if divisor>1 else 'same output scale',
                 r'two seeds: solid / dashed','']
        for cx,(title,color,*_),err,detail in zip(centers,panels,e,details):
            out.append(r'\node[text=%s,font=\scriptsize] at (%.3f,%.3f) {%s};'%(color,cx,cy-2.12,err))
            if detail:
                out.append(r'\node[text=%s,font=\scriptsize] at (%.3f,%.3f) {%s};'%(color,cx,cy-2.45,detail))
        if row<len(indices)-1:
            out.append(r'\draw[ink!15] (-.1,%.3f) -- (17.6,%.3f);'%(cy-2.95,cy-2.95))
    bottom=-6.35*(len(indices)-1)-3.04
    _legend_row(out,3.6,bottom,[(ref,'dense reference','line'),('ink','training labels','dot')],[5.,3.])
    out.append(r'\node[text=ink,font=\scriptsize,align=center] at (8.75,%.3f) {'
               r'Same initialized network; each model at training MSE $\simeq0.001$, at its own fitting time.\\'
               r'RMS differences from dense use $8192$ circle queries. Signed ticks give output values; any wider NTK scale is marked explicitly.};'%(bottom-.62))
    out.append(POSTAMBLE)
    return '\n'.join(out)


def _circle_gallery(prefix, orders):
    with np.load(RADIAL_BUNDLE, allow_pickle=False) as z:
        d = {k: z[k] for k in z.files}
    out = [PREAMBLE]
    vmax = max(np.abs(d[f"{prefix}_{i}_P0"]).max() for i in range(5))
    s = 1.45 / (3 + vmax)
    W = 3.3
    for i in range(5):
        cx = 1.6 + i * W
        ang = d[f"{prefix}_{i}_angles"]
        dense = d[f"{prefix}_{i}_P0"]
        curves = [(dense, "ink!40,line width=1.5pt")] + [(d[f"{prefix}_{i}_P{p}"], ORDER_STYLE[p]) for p in orders]
        polar(out, cx, 0, s, ang, curves, d[f"{prefix}_{i}_train_angles"], d[f"{prefix}_{i}_labels"])
        out.append(r"\node[text=ink,font=\scriptsize] at (%.3f,1.75) {%s};" % (cx, TASK_NAMES[i]))
        for k, p in enumerate(orders):
            e = np.sqrt(np.mean((d[f"{prefix}_{i}_P{p}"] - dense) ** 2))
            txt = f"{e:.3g}" if e >= 1e-3 else f"{e:.2g}"
            if "e" in txt:
                mant, ex = txt.split("e")
                txt = r"%s{\times}10^{%d}" % (mant, int(ex))
            out.append(r"\node[anchor=east,text=%s,font=\scriptsize] at (%.3f,%.3f) {$P=%d$};"
                       % (ORDER_COLOR[p], cx - 0.12, -1.78 - 0.34 * k, p))
            out.append(r"\node[anchor=west,text=%s,font=\scriptsize] at (%.3f,%.3f) {$%s$};"
                       % (ORDER_COLOR[p], cx + 0.02, -1.78 - 0.34 * k, txt))
    items = [("ink!40,line width=1.5pt", "dense", "line")] + [(ORDER_STYLE[p], f"$P={p}$", "line") for p in orders] \
        + [("ink", "training labels", "dot")]
    _legend_row(out, 3.0, -3.05, items, [2.0] + [1.8] * len(orders) + [2.0])
    out.append(POSTAMBLE)
    return "\n".join(out)


def circles_deep():
    return _circle_gallery("deep", (1, 2, 3))


def circles_shallow():
    return _circle_gallery("shallow", (1, 3, 7))


def orders():
    a, meta = _response_bundle()
    out = [PREAMBLE]
    PW, PH, GX = 4.1, 3.2, 1.45
    for j, (field, title) in enumerate([("rms_8192", "RMS difference from dense"),
                                        ("combined_sensitivity", "numerical sensitivity")]):
        vals = [r[field] for r in meta["deep_orders"]]
        lo, hi = 10 ** np.floor(np.log10(min(vals))), 10 ** np.ceil(np.log10(max(vals)))
        ax = Axes(out, 1.0 + j * (PW + GX), 0, PW, PH, (0.8, 3.2), (lo, hi), ylog=True)
        yt = _log_ticks(lo, hi)
        ax.frame(xticks=[1, 2, 3], yticks=yt, ylabels=[_pow_label(t) for t in yt])
        for case, c in zip(TASKS, TASK_COLOR):
            rows = sorted([r for r in meta["deep_orders"] if r["case"] == case], key=lambda r: r["P"])
            xs, ys = [r["P"] for r in rows], [r[field] for r in rows]
            ax.line(xs, ys, f"{c},line width=0.8pt" + (",dash pattern=on 0.8pt off 1.2pt" if j else ""))
            ax.marks(xs, ys, f"{c},draw=white,line width=0.3pt", 1.7)
        ax.title(title)
        ax.xlabel("order $P$")
    # feature movement
    ranges = meta["feature_ranges"]
    ax = Axes(out, 1.0 + 2 * (PW + GX), 0, 3.2, PH, (0.4, 3.6), (0, 0.9))
    ax.frame(xticks=[1, 2, 3], yticks=[0, 0.25, 0.5, 0.75], ylabels=[r"$0$", r"$0.25$", r"$0.5$", r"$0.75$"])
    for layer, (lo_, hi_) in enumerate(ranges, 1):
        x = ax.X(layer)
        out.append(r"\draw[grn!55,line width=6pt,line cap=round] (%.3f,%.3f) -- (%.3f,%.3f);" % (x, ax.Y(lo_), x, ax.Y(hi_)))
        out.append(r"\node[text=mute,font=\scriptsize,anchor=south] at (%.3f,%.3f) {$%.2f$--$%.2f$};" % (x, ax.Y(hi_) + 0.08, lo_, hi_))
    ax.title("hidden features move")
    ax.xlabel("hidden layer")
    out.append(r"\node[rotate=90,anchor=south,text=ink] at (%.3f,%.3f) {activation RMS change};" % (ax.x0 - 0.75, PH / 2))
    items = [(f"{c},line width=1.2pt", n, "line") for c, n in zip(TASK_COLOR, TASK_SHORT)]
    _legend_row(out, 1.0, -1.2, items[:3], [4.4, 4.4, 4.4])
    _legend_row(out, 1.0, -1.65, items[3:], [4.4, 4.4])
    out.append(POSTAMBLE)
    return "\n".join(out)


def mnist():
    a, meta = _response_bundle()
    out = [PREAMBLE]
    x = a["mnist_dense"]
    digits = a["mnist_digits"]
    lo = min(x.min(), a["mnist_3"].min()) - 0.1
    hi = max(x.max(), a["mnist_3"].max()) + 0.1
    ax = Axes(out, 0.9, 0, 4.4, 4.4, (lo, hi), (lo, hi))
    ticks = [-1, -0.5, 0, 0.5, 1]
    ax.frame(xticks=ticks, yticks=ticks, xgrid=True)
    out.append(r"\draw[ink!35,line width=0.5pt,dash pattern=on 1.5pt off 1.5pt] (%.3f,%.3f) -- (%.3f,%.3f);"
               % (ax.X(lo), ax.Y(lo), ax.X(hi), ax.Y(hi)))
    for dg, c in [(3, "fwd"), (8, "gold")]:
        sel = digits == dg
        for u, v in zip(x[sel], a["mnist_3"][sel]):
            out.append(r"\fill[%s,opacity=0.45] (%.3f,%.3f) circle (0.55pt);" % (c, ax.X(u), ax.Y(v)))
    ax.title("response memory $P=3$ against dense")
    ax.xlabel("dense prediction")
    ax.ylabel("memory prediction", off=0.8)
    out.append(r"\fill[fwd] (1.15,4.05) circle (1.4pt); \node[anchor=west,text=ink] at (1.25,4.05) {digit 3};")
    out.append(r"\fill[gold] (1.15,3.7) circle (1.4pt); \node[anchor=west,text=ink] at (1.25,3.7) {digit 8};")
    res = {p: (a[f"mnist_{p}"] - x) * 1e3 for p in (1, 2, 3)}
    lim = np.ceil(max(np.abs(v).max() for v in res.values()))
    SH, GY = 1.2, 0.3
    for k, p in enumerate((1, 2, 3)):
        y0 = 4.4 - (k + 1) * SH - k * GY
        ax = Axes(out, 7.2, y0, 8.4, SH, (lo, hi), (-lim, lim))
        ax.frame(xticks=ticks if k == 2 else [], yticks=[-lim, 0, lim],
                 ylabels=[f"$-{lim:g}$", "$0$", f"$+{lim:g}$"])
        for u, v in zip(x, res[p]):
            out.append(r"\fill[%s,opacity=0.4] (%.3f,%.3f) circle (0.5pt);" % (ORDER_COLOR[p], ax.X(u), ax.Y(v)))
        rm = np.sqrt(np.mean((res[p] / 1e3) ** 2))
        out.append(r"\node[anchor=north west,text=%s] at (%.3f,%.3f) {$P=%d$};" % (ORDER_COLOR[p], 7.25, y0 + SH, p))
        out.append(r"\node[anchor=north east,text=mute,font=\scriptsize] at (%.3f,%.3f) {RMS $%.4f$};" % (15.6, y0 + SH, rm))
    out.append(r"\node[anchor=south west,text=ink,inner sep=1pt] at (7.2,4.48) {residual $(f_P-f_{\mathrm{dense}})\times10^{3}$, one shared scale};")
    out.append(r"\node[anchor=north,text=ink] at (11.4,%.3f) {dense prediction};" % (4.4 - 3 * SH - 2 * GY - 0.38))
    out.append(POSTAMBLE)
    return "\n".join(out)



# ======================================================================
# same_rank

SAME_RANK = r"""% Same-rank comparison: response memory vs directly trained low-rank factors.
% Data: studies/neural_response_memory_20260922/FACTOR_CONTROL_RESULTS.md
% (whole-circle RMS difference from dense; two hidden tanh layers, width 2048).
\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,calc}

\definecolor{fwd}{HTML}{2F6DB5}
\definecolor{bwd}{HTML}{C8553D}
\definecolor{lrn}{HTML}{6B4C9A}
\definecolor{ink}{HTML}{2B2B2B}
\definecolor{mute}{HTML}{8A8A8A}

\tikzset{
  lab/.style={font=\footnotesize,text=ink},
  small/.style={font=\scriptsize,text=mute},
  mem/.style={circle,fill=lrn,inner sep=0pt,minimum size=5.2pt},
  fac/.style={circle,draw=bwd,fill=white,line width=0.9pt,inner sep=0pt,minimum size=5.2pt},
}

% x position of a value on a log10 axis: 10^-3.6 -> 0, 10^0.4 -> W
\def\W{8.2}
\newcommand{\lx}[1]{{(log10(#1)+3.6)/4.0*\W}}

\begin{document}
\begin{tikzpicture}[y=-0.62cm]

% grid and axis
\foreach \e/\t in {-3/{10^{-3}},-2/{10^{-2}},-1/{10^{-1}},0/{1}}{
  \pgfmathsetmacro{\xx}{(\e+3.6)/4.0*\W}
  \draw[ink!10,line width=0.4pt] (\xx,0.35) -- (\xx,7.1);
  \node[small,anchor=north] at (\xx,7.15) {$\t$};
}
\node[lab,anchor=north] at ({0.5*\W},7.7)
  {whole-circle RMS difference from dense training};

% rows: label, rank, memory, factor seed 1, factor seed 2, ratio
\foreach \name/\rk/\m/\fa/\fb/\ra [count=\i] in {
  {Two outliers, alternating}/24/0.0729531/0.465456/0.460915/6,
  {Quadrant, alternating}/24/0.0456113/0.676639/1.54131/15,
  {Quadrant, paired labels}/24/0.00281761/0.375464/0.203580/72,
  {Quadrant, center/edges}/24/0.00487776/0.257864/0.249269/51,
  {Equally spaced, mixed}/12/0.000525665/0.0606940/0.0687051/115}{
  \pgfmathsetmacro{\xm}{\lx{\m}}
  \pgfmathsetmacro{\xa}{\lx{\fa}}
  \pgfmathsetmacro{\xb}{\lx{\fb}}
  \pgfmathsetmacro{\xlo}{min(\xa,\xb)}
  \pgfmathsetmacro{\xhi}{max(\xa,\xb)}
  \draw[ink!18,line width=2.2pt,line cap=round] (\xm,\i) -- (\xlo,\i);
  \draw[bwd!35,line width=0.8pt] (\xlo,\i) -- (\xhi,\i);
  \node[fac] at (\xa,\i) {};
  \node[fac] at (\xb,\i) {};
  \node[mem] at (\xm,\i) {};
  \node[lab,anchor=east] at (-0.25,\i) {\name};
  \node[small,anchor=west] at (-0.2,\i) {};
  \node[font=\scriptsize,text=ink!70,anchor=south] at ({0.5*(\xm+\xlo)},\i-0.02) {$\times\ra$};
  \node[small,anchor=west] at (\W+0.15,\i) {rank \rk};
}

% separated rank-56 row
\draw[ink!15,line width=0.4pt,dash pattern=on 1.5pt off 1.5pt] (-4.4,5.75) -- (\W+1.2,5.75);
\pgfmathsetmacro{\xm}{\lx{0.00466307}}
\pgfmathsetmacro{\xa}{\lx{0.516210}}
\pgfmathsetmacro{\xb}{\lx{0.251026}}
\draw[ink!18,line width=2.2pt,line cap=round] (\xm,6.5) -- (\xb,6.5);
\draw[bwd!35,line width=0.8pt] (\xb,6.5) -- (\xa,6.5);
\node[fac] at (\xa,6.5) {};
\node[fac] at (\xb,6.5) {};
\node[mem] at (\xm,6.5) {};
\node[lab,anchor=east] at (-0.25,6.5) {Two outliers, alternating};
\node[font=\scriptsize,text=ink!70,anchor=south] at ({0.5*(\xm+\xb)},6.48) {$\times54$};
\node[small,anchor=west] at (\W+0.15,6.5) {rank 56};

% legend
\node[mem] (l1) at (0.2,-0.35) {};
\node[lab,anchor=west] at (0.35,-0.35) {response memory};
\node[fac] (l2) at (3.25,-0.35) {};
\node[lab,anchor=west] at (3.4,-0.35) {trained factors $W_0+AB$ (two seeds)};

\end{tikzpicture}
\end{document}
"""

# ======================================================================
# clocks

def clocks():
    """Toy two-residual signal drawn in physical time and in both clocks."""
    T, P = 6.0, 4
    t = np.linspace(0, T, 60001)
    r1, r2 = np.exp(-4 * t), 0.05 * np.exp(-0.5 * t)
    rho = np.sqrt((r1**2 + r2**2) / 2)
    b1, b2 = r1 / rho, r2 / rho
    speed = np.hypot(np.gradient(b1, t), np.gradient(b2, t))


    def cumulative(f):
        return np.concatenate([[0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(t))])


    rows = [
        ("physical time $t$", t),
        (r"learning-speed clock, $\dot\tau=\rho$", cumulative(rho)),
        (r"joint clock, $\dot\tau=\rho+\|\dot b\|$", cumulative(rho + speed)),
    ]
    events = [0.5, 0.86, 1.5]          # physical instants linked across rows
    W, H, GAP = 8.4, 1.25, 0.45        # panel width, height, vertical gap (cm)
    ymax = float(b1.max())
    lo, hi = -0.25, ymax + 0.25          # vertical range incl. fit overshoot

    out = []
    emit = out.append
    emit(r"""% Generated by claude_figures.py -- do not edit by hand.
    \documentclass[tikz,border=2pt]{standalone}
    \usepackage{amsmath,amssymb}
    \definecolor{bwd}{HTML}{C8553D}
    \definecolor{lrn}{HTML}{6B4C9A}
    \definecolor{ink}{HTML}{2B2B2B}
    \definecolor{mute}{HTML}{8A8A8A}
    \begin{document}
    \begin{tikzpicture}[font=\footnotesize]""")

    event_x = []
    for i, (name, clock) in enumerate(rows):
        x = clock / clock[-1]
        u = np.linspace(0, 1, 2001)
        y = np.interp(u, x, b1)
        fit = leg.legval(2 * u - 1, leg.legfit(2 * u - 1, y, P - 1))
        err = float(np.sqrt(np.mean((fit - y) ** 2)))
        y0 = -i * (H + GAP)
        sy = lambda v: y0 + H * (v - lo) / (hi - lo)
        sel = np.linspace(0, len(u) - 1, 260).astype(int)
        emit(rf"\draw[ink!20,line width=0.4pt] (0,{y0:.3f}) -- ({W},{y0:.3f});")
        emit(r"\draw[bwd,line width=0.9pt] " +
             " -- ".join(f"({W * u[j]:.3f},{sy(y[j]):.3f})" for j in sel) + ";")
        emit(r"\draw[lrn,line width=0.8pt,dash pattern=on 2.4pt off 1.6pt] " +
             " -- ".join(f"({W * u[j]:.3f},{sy(fit[j]):.3f})" for j in sel) + ";")
        emit(rf"\node[anchor=west,text=ink] at ({W + 0.3},{y0 + 0.62 * H:.3f}) {{{name}}};")
        emit(rf"\node[anchor=west,text=mute,font=\scriptsize] at ({W + 0.3},{y0 + 0.28 * H:.3f}) "
             rf"{{RMS fit error ${err:.3f}$}};")
        event_x.append([(W * float(np.interp(e, t, x)), y0) for e in events])

    # faint links between the same physical instants in consecutive rows
    for k in range(len(events)):
        for i in range(len(rows) - 1):
            (xa, ya), (xb, yb) = event_x[i][k], event_x[i + 1][k]
            emit(rf"\draw[ink!30,line width=0.35pt,dash pattern=on 1pt off 1.2pt] "
                 rf"({xa:.3f},{ya:.3f}) -- ({xb:.3f},{yb + H:.3f});")
        for i in range(len(rows)):
            xa, ya = event_x[i][k]
            emit(rf"\draw[ink!30,line width=0.35pt,dash pattern=on 1pt off 1.2pt] "
                 rf"({xa:.3f},{ya:.3f}) -- ({xa:.3f},{ya + H:.3f});")

    yb = -(len(rows) - 1) * (H + GAP)
    emit(rf"\node[anchor=north,text=mute,font=\scriptsize] at ({0.5 * W},{yb - 0.08:.3f}) "
         r"{position within each coordinate, rescaled to $[0,1]$};")
    emit(rf"\draw[bwd,line width=0.9pt] (0,{H + 0.35}) -- ++(0.45,0) "
         r"node[right,text=ink] {backward history $b_1=r_1/\rho$};")
    emit(rf"\draw[lrn,line width=0.8pt,dash pattern=on 2.4pt off 1.6pt] (4.3,{H + 0.35}) "
         rf"-- ++(0.45,0) node[right,text=ink] {{fit with $P={P}$ Legendre modes}};")
    emit(r"\end{tikzpicture}")
    emit(r"\end{document}")

    return "\n".join(out) + "\n"


# ======================================================================
# driver

BUILDERS = {
    "mechanism": lambda: MECHANISM,
    "moments": moments,
    "trajectory": trajectory,
    "factors": factors,
    "circles_deep": circles_deep,
    "circles_shallow": circles_shallow,
    "orders": orders,
    "mnist": mnist,
    "same_rank": lambda: SAME_RANK,
    "clocks": clocks,
    "learning_controls_quadrant_alternating": lambda: learning_controls_preview([1]),
    "learning_controls_gallery_a": lambda: learning_controls_preview([2,1,3]),
    "learning_controls_gallery_b": lambda: learning_controls_preview([0,4]),
}

# Explicit opt-in: do not add candidate artwork to the default paper rebuild.
PREVIEW_BUILDERS = {"same_rank_radial_preview": same_rank_radial_preview,
                    "frozen_ntk_radial_preview": frozen_ntk_radial_preview}
PREVIEW_BUILDERS.update({f'learning_controls_{case}': (lambda i=i: learning_controls_preview([i]))
                         for i,case in enumerate(TASKS) if i != 1})
PREVIEW_BUILDERS['learning_controls_gallery']=lambda:learning_controls_preview([2,1,3,0,4])


def build(name):
    tex = (BUILDERS | PREVIEW_BUILDERS)[name]()
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / f"{name}.tex"
        src.write_text(tex)
        run = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", src.name],
                             cwd=tmp, capture_output=True, text=True)
        if run.returncode:
            sys.exit(f"pdflatex failed for {name}:\n{run.stdout[-2000:]}")
        FIGURES_DIR.mkdir(exist_ok=True)
        shutil.copy(Path(tmp) / f"{name}.pdf", FIGURES_DIR / f"{name}.pdf")
    print(f"wrote {FIGURES_DIR / name}.pdf")


if __name__ == "__main__":
    names = sys.argv[1:] or list(BUILDERS)
    unknown = [x for x in names if x not in (BUILDERS | PREVIEW_BUILDERS)]
    if unknown:
        sys.exit(f"unknown figure(s): {', '.join(unknown)}; choose from {', '.join(BUILDERS | PREVIEW_BUILDERS)}")
    for name in names:
        build(name)
