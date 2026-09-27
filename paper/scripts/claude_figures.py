"""Figures added on the ``claude`` branch.

Regenerates, from scratch, every figure this branch adds to the paper:

    mechanism   response memory as a paired memory, and the product of errors
    state_map   descriptions of training by type of state and growth in time
    clocks      a toy history in physical time and in both clocks
    same_rank   response memory against trained low-rank factors, same rank
    moments     neuron histories as position/velocity/acceleration moments

Usage (from the repository root or anywhere):

    python paper/scripts/claude_figures.py            # all figures
    python paper/scripts/claude_figures.py clocks     # a subset

Each figure is TikZ, compiled with pdflatex into paper/figures/<name>.pdf.
Requires numpy and a TeX installation with TikZ.  ``same_rank`` uses the
numbers recorded in
studies/neural_response_memory_20260922/FACTOR_CONTROL_RESULTS.md; ``clocks``
uses a toy signal; ``moments`` trains a small network (a few seconds).
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
# state_map

STATE_MAP = r"""% Map of descriptions of training: type of state in the width limit
% (operator / population / scalar) against growth with training length.
\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta,calc,positioning}

\definecolor{fwd}{HTML}{2F6DB5}
\definecolor{bwd}{HTML}{C8553D}
\definecolor{lrn}{HTML}{6B4C9A}
\definecolor{ink}{HTML}{2B2B2B}
\definecolor{mute}{HTML}{8A8A8A}

\tikzset{
  >={Stealth[length=2.2mm]},
  lab/.style={font=\footnotesize,text=ink},
  small/.style={font=\scriptsize,text=mute},
  card/.style={draw=ink!25,fill=white,rounded corners=2pt,line width=0.45pt,
               font=\footnotesize,text=ink,align=center,inner sep=4pt,
               text width=3.25cm,minimum height=1.15cm},
  hi/.style={card,draw=lrn,line width=0.9pt,fill=lrn!7},
  open/.style={card,dashed,draw=ink!30,fill=none},
  move/.style={->,line width=0.7pt,draw=ink!60},
  mlab/.style={font=\scriptsize,text=ink!75,fill=white,inner sep=1.2pt},
}

\begin{document}
\begin{tikzpicture}

\def\cw{4.3}   % column width
\def\rh{2.15}  % row height

% column bands
\foreach \c in {0,1,2}{
  \fill[ink!3] (\c*\cw+0.08,-0.2) rectangle (\c*\cw+\cw-0.08,2*\rh-0.1);
}
\node[lab,align=center] at (0.5*\cw,2*\rh+0.35) {operators\\[-1pt]\scriptsize\color{mute}$n\times n$ matrices};
\node[lab,align=center] at (1.5*\cw,2*\rh+0.35) {populations\\[-1pt]\scriptsize\color{mute}$n$-vectors, finitely many};
\node[lab,align=center] at (2.5*\cw,2*\rh+0.35) {width-free\\[-1pt]\scriptsize\color{mute}scalars and kernels};
\node[small] at (1.5*\cw,2*\rh+1.05) {type of evolving state as width grows};

% row labels
\node[lab,rotate=90,align=center] at (-0.45,1.5*\rh-0.15) {fixed in time};
\node[lab,rotate=90,align=center] at (-0.45,0.5*\rh-0.15) {grows with steps};

% cells
\node[card] (dense) at (0.5*\cw,1.5*\rh-0.15)
  {Dense network\\[1pt]\scriptsize\color{mute}$Hn^2$, Markovian};
\node[hi] (rm) at (1.5*\cw,1.5*\rh-0.15)
  {\textbf{Response memory}\\[1pt]\scriptsize\color{mute}$HmnP$ moving, $W_0$ fixed};
\node[open] (sc) at (2.5*\cw,1.5*\rh-0.15)
  {\scriptsize exact scalar closure fails\\[-1pt]{\color{mute}\scriptsize restricted class, \S5}\\[3pt]
   \scriptsize NTH, order $p$: $m^p$\\[-1pt]{\color{mute}\scriptsize proved near the lazy limit}};
\node[card] (hist) at (1.5*\cw,0.5*\rh-0.15)
  {Stored response history\\[1pt]\scriptsize\color{mute}$HmnK$, exact};
\node[card] (dmft) at (2.5*\cw,0.5*\rh-0.15)
  {Tensor Programs\\[-1pt]and DMFT\\[1pt]\scriptsize\color{mute}$Hm^2K^2$, exact limit};

% moves
\draw[move] (dense.south) .. controls ++(0,-0.9) and ++(-1.0,0) .. (hist.west)
  node[mlab,pos=0.62,below left=1pt,align=right,fill=none] {eliminate\\learned weights};
\draw[move,draw=lrn,line width=0.9pt] (hist.north) -- (rm.south)
  node[mlab,midway,left=2pt,text=lrn,align=right,fill=none] {compress time\\$K$ steps $\to P$ moments};
\draw[move] (hist.east) -- (dmft.west)
  node[mlab,midway,above=5pt,fill=none] {$n\to\infty$};

% off-axis strip
\draw[ink!15,line width=0.4pt] (0.08,-0.55) -- (3*\cw-0.08,-0.55);
\node[small,anchor=north,align=center] at (1.5*\cw,-0.62)
  {off the axis, each exact about a different object:\\
   neural tangent kernel (frozen features)\enspace$\cdot$\enspace
   deep linear (no nonlinearity)\enspace$\cdot$\enspace
   one hidden layer (no depth)};

\end{tikzpicture}
\end{document}
"""

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
    emit(r"""% Generated by claude_figures.py -- do not edit by hand.
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
    "state_map": lambda: STATE_MAP,
    "clocks": clocks,
    "same_rank": lambda: SAME_RANK,
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
