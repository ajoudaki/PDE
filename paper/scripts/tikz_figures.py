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
# driver

BUILDERS = {
    "mechanism": lambda: MECHANISM,
    "moments": moments,
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
