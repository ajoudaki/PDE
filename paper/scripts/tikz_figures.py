"""Explanatory TikZ figures for the paper.

Regenerates, from scratch:

    mechanism   response memory as a paired memory, and the product of errors
    moments     neuron histories as position/velocity/acceleration moments

Usage (from the repository root or anywhere):

    python paper/scripts/tikz_figures.py            # all figures
    python paper/scripts/tikz_figures.py moments    # a subset

Each figure is TikZ, compiled with pdflatex into paper/figures/<name>.pdf.
Requires numpy and a TeX installation with TikZ.  ``moments`` trains a small
network (a few seconds).
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

    # column headers with particle glyphs
    heads = ["position", "$+$ velocity", "$+$ acceleration"]
    for j in range(3):
        x0 = j * (PW + GX)
        cx, cy = x0 + 0.1, PH + 0.62
        emit(r"\fill[ink] (%.3f,%.3f) circle (1.6pt);" % (cx, cy))
        if j >= 1:
            emit(r"\draw[->,ink,line width=0.7pt] (%.3f,%.3f) -- ++(0.42,0.12);" % (cx + 0.06, cy + 0.02))
        if j >= 2:
            emit(r"\draw[->,ink,line width=0.6pt] (%.3f,%.3f) arc[start angle=200,end angle=320,radius=0.2];"
                 % (cx + 0.5, cy + 0.14))
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
                 r"at (%.3f,%.3f) {median error $%.0f\%%$};" % (x0 + PW, y0 + PH + 0.02, 100 * med))
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
    emit(r"\draw[ink!40,line width=0.6pt,dash pattern=on 1.8pt off 1.3pt] (%.3f,%.3f) -- ++(0.45,0) node[right,text=ink] {halfway};"
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


def polar(out, cx, cy, s, angles, curves, train=None, labels=None, ring_labels=False):
    """A circle function drawn with radius s*(3+f); rings mark f = -1, 0, +1."""
    for f, st in [(-1, "ink!9"), (1, "ink!9")]:
        out.append(r"\draw[%s,line width=0.4pt] (%.3f,%.3f) circle (%.3f);" % (st, cx, cy, s * (3 + f)))
    out.append(r"\draw[ink!28,line width=0.4pt,dash pattern=on 1.2pt off 1.2pt] (%.3f,%.3f) circle (%.3f);" % (cx, cy, 3 * s))
    if ring_labels:
        for f, lab in [(-1, r"$-1$"), (0, r"$0$"), (1, r"$+1$")]:
            out.append(r"\node[text=mute,font=\tiny,inner sep=0.5pt,anchor=south west] at (%.3f,%.3f) {%s};"
                       % (cx + 0.03, cy + s * (3 + f) - 0.02, lab))
    sel = np.linspace(0, len(angles) - 1, 720).astype(int)
    for values, style in curves:
        r = s * (3 + values[sel])
        xs, ys = cx + r * np.cos(angles[sel]), cy + r * np.sin(angles[sel])
        out.append(r"\draw[%s] %s -- cycle;" % (style, _pts(xs, ys)))
    if train is not None:
        for ang, lab in zip(train, labels):
            r = s * (3 + lab)
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
    rms = {p: a[f"common_rms_{p}"][1:] for p in (1, 3, 7)}
    sen = {p: a[f"common_sensitivity_{p}"][1:] for p in (1, 3, 7)}
    lo = 10 ** np.floor(np.log10(min(min(v.min() for v in rms.values()), min(v.min() for v in sen.values()))))
    hi = 10 ** np.ceil(np.log10(max(v.max() for v in rms.values())))
    ax = Axes(out, 1.2, -6.1, 11.0, 3.0, (0, 82), (lo, hi), ylog=True)
    yt = _log_ticks(lo, hi)[::2]
    ax.frame(xticks=[0, 10, 20, 40, 80], yticks=yt, ylabels=[_pow_label(t) for t in yt])
    for p in (1, 3, 7):
        c = ORDER_COLOR[p]
        ax.line(times[1:], sen[p], f"{c}!70,line width=0.6pt,dash pattern=on 0.8pt off 1.2pt")
        ax.line(times[1:], rms[p], f"{c},line width=0.8pt")
        ax.marks(times[1:], rms[p], f"{c},draw=white,line width=0.3pt", 1.7)
    ax.xlabel("physical training time $t$")
    ax.ylabel("RMS difference from dense", off=0.85)
    x0 = 12.6
    out.append(r"\draw[ink,line width=0.8pt] (%.3f,-3.6) -- ++(0.45,0); \filldraw[ink,draw=white,line width=0.3pt] (%.3f,-3.6) circle (1.7pt);" % (x0, x0 + 0.225))
    out.append(r"\node[anchor=west,text=ink] at (%.3f,-3.6) {measured, $2048$ angles};" % (x0 + 0.52))
    out.append(r"\draw[ink!70,line width=0.6pt,dash pattern=on 0.8pt off 1.2pt] (%.3f,-4.1) -- ++(0.45,0);" % x0)
    out.append(r"\node[anchor=west,text=ink] at (%.3f,-4.1) {numerical sensitivity};" % (x0 + 0.52))
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


def clock():
    t = np.linspace(0, 1, 1601)
    speed = .035 + 1.4 * np.exp(-((t - .31) / .057) ** 2) + .85 * np.exp(-((t - .77) / .085) ** 2)
    s_ = np.r_[0, np.cumsum((speed[1:] + speed[:-1]) * np.diff(t) / 2)]
    s_ = s_ / s_[-1]
    path = np.stack([1.5 * s_, .46 * np.sin(2 * np.pi * s_ - .6)], axis=1)
    velocity = np.gradient(path, t, axis=0)
    rho = .12 + .18 * (1 - t)
    g = rho + np.linalg.norm(velocity, axis=1)
    tau = 1 + np.r_[0, np.cumsum((g[1:] + g[:-1]) * np.diff(t) / 2)]
    out = [PREAMBLE]
    sel = np.linspace(0, len(t) - 1, 300).astype(int)
    events = [.24, .34, .65, .83]
    ecol = ["fwd", "grn", "gold", "lrn"]
    PW, PH = 8.6, 1.9
    axes = []
    for k, (clk, label) in enumerate([(t, "physical time $t$"), (tau, r"joint clock $\tau$")]):
        y0 = -k * (PH + 1.05)
        ax = Axes(out, 1.0, y0, PW, PH, (clk[0], clk[-1]), (-0.1, 1.65))
        ax.frame(yticks=[0, 0.75, 1.5])
        ax.line(clk[sel], path[sel, 0], "ink,line width=0.9pt")
        ax.title("one response, in " + label)
        axes.append((ax, clk))
    for ev, c in zip(events, ecol):
        j = int(np.argmin(abs(t - ev)))
        (a0, c0), (a1, c1) = axes
        out.append(r"\draw[%s!45,line width=0.45pt,dash pattern=on 1.2pt off 1.2pt] (%.3f,%.3f) -- (%.3f,%.3f);"
                   % (c, a0.X(c0[j]), a0.y0, a1.X(c1[j]), a1.y0 + a1.h))
        for ax, clk in axes:
            out.append(r"\fill[%s] (%.3f,%.3f) circle (1.8pt);" % (c, ax.X(clk[j]), ax.Y(path[j, 0])))
    # geometric insets: the path sampled uniformly in each coordinate
    for k, (clk, title, col) in enumerate([(t, "uniform in $t$", "mute"), (tau, r"uniform in $\tau$", "lrn")]):
        ox, oy, sc = 11.2, -k * (PH + 1.05) + 0.25, 2.6
        out.append(r"\draw[ink!15,line width=2.2pt,line cap=round] %s;" % _pts(ox + sc * path[sel, 0] / 1.5, oy + 0.7 + sc * path[sel, 1] / 1.5))
        marks = np.linspace(clk[0], clk[-1], 16)
        px, py = np.interp(marks, clk, path[:, 0]), np.interp(marks, clk, path[:, 1])
        for u, v in zip(px, py):
            out.append(r"\filldraw[%s,draw=white,line width=0.3pt] (%.3f,%.3f) circle (1.7pt);" % (col, ox + sc * u / 1.5, oy + 0.7 + sc * v / 1.5))
        out.append(r"\node[text=ink,anchor=south] at (%.3f,%.3f) {%s};" % (ox + sc / 2, oy + 1.45, title))
    out.append(r"\node[anchor=west,text=ink] at (1.0,%.3f) {learning-speed clock: $\dot\tau=\rho$ \qquad joint clock: $\dot\tau=\rho+\|\dot\Psi\|_2$, so that $\|d\Psi/d\tau\|_2\le1$};"
               % (-(PH + 1.05) - 1.15))
    out.append(POSTAMBLE)
    return "\n".join(out)


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
    "clock": clock,
}


def build(name):
    tex = BUILDERS[name]()
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
    unknown = [x for x in names if x not in BUILDERS]
    if unknown:
        sys.exit(f"unknown figure(s): {', '.join(unknown)}; choose from {', '.join(BUILDERS)}")
    for name in names:
        build(name)
