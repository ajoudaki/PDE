"""Shared visual style for the paper's data figures.

Every figure imports this module, so a method keeps one colour and one marker
everywhere. Methods carry the colour; baselines stay neutral grey.
"""
import matplotlib as mpl
import numpy as np

INK, MUTED, LIGHT = '#1f1f1e', '#6b6b68', '#e4e3de'
TEXT_WIDTH = 6.5  # inches, article class with 1 in margins

METHOD = {  # validated categorical slots (all-pairs colour-vision check)
    'legendre': dict(label='Legendre', color='#2a78d6', marker='s'),
    'harmonic': dict(label='Harmonic', color='#1baf7a', marker='D'),
    'taylor': dict(label='Taylor', color='#eb6834', marker='o'),
}
FAMILY = {'legendre': 'legendre', 'harmonic': 'harmonic', 'logarithmic': 'taylor', 'taylor': 'taylor'}
CONTROL = {
    'dense': dict(label='small dense', color='#55554f', marker='d', linestyle='-'),
    'low_rank': dict(label='low rank', color='#8f8e88', marker='v', linestyle=(0, (4, 2))),
    'frozen': dict(label='frozen features', color='#a3a29c', linestyle=(0, (6, 2, 1.5, 2))),
    'pair': dict(label='dense vs. dense', color=INK, linestyle=(0, (1, 1.8))),
}

RC = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['Nimbus Sans', 'Liberation Sans', 'DejaVu Sans'],
    'mathtext.fontset': 'custom', 'mathtext.rm': 'Nimbus Sans',
    'mathtext.it': 'Nimbus Sans:italic', 'mathtext.bf': 'Nimbus Sans:bold',
    'font.size': 8, 'axes.labelsize': 8, 'axes.titlesize': 8,
    'xtick.labelsize': 7, 'ytick.labelsize': 7, 'legend.fontsize': 7,
    'text.color': INK, 'axes.labelcolor': INK, 'axes.edgecolor': MUTED,
    'axes.linewidth': .6, 'axes.spines.top': False, 'axes.spines.right': False,
    'xtick.color': MUTED, 'ytick.color': MUTED,
    'xtick.labelcolor': INK, 'ytick.labelcolor': INK,
    'xtick.major.width': .6, 'ytick.major.width': .6,
    'xtick.major.size': 2.5, 'ytick.major.size': 2.5,
    'xtick.minor.visible': False, 'ytick.minor.visible': False,
    'lines.linewidth': 1.4, 'lines.markersize': 3.6, 'lines.markeredgewidth': 0,
    'legend.frameon': False, 'legend.handlelength': 1.8,
    'pdf.fonttype': 42, 'savefig.facecolor': 'white', 'figure.facecolor': 'white',
}


def use():
    mpl.rcParams.update(RC)


def panel(ax, letter, title):
    """Bold panel letter followed by a short task name, left-aligned above the axes."""
    ax.set_title(rf'$\mathbf{{{letter}}}$   {title}', loc='left', pad=6)


def log_ticks(axis, minor=False):
    """Decade ticks labelled as powers of ten, without minor clutter."""
    axis.set_major_locator(mpl.ticker.LogLocator(base=10, numticks=12))
    axis.set_major_formatter(mpl.ticker.LogFormatterMathtext())
    axis.set_minor_locator(mpl.ticker.LogLocator(base=10, subs='auto') if minor
                           else mpl.ticker.NullLocator())


def width_ticks(ax, widths):
    """Dense widths on a log axis, written compactly (512, 1k, 2k, ...)."""
    ax.set_xscale('log')
    ax.set_xticks(widths, [str(n) if n < 1000 else f'{n // 1024}k' for n in widths])
    ax.xaxis.set_minor_locator(mpl.ticker.NullLocator())


def direct_labels(ax, items, x, line=9.6, dx=3.0, ha='left'):
    """Write labels at (x, y) in data coordinates, nudged apart vertically.

    items: (y, text, colour) or (y, text, colour, note); a note is set smaller
    and muted under its label. line is one text line in points. Call after the
    axis limits and the figure layout are final.
    """
    if not items:
        return
    to_display, to_data = ax.transData, ax.transData.inverted()
    scale = ax.figure.dpi/72
    order = sorted(range(len(items)), key=lambda i: items[i][0])
    ys = np.array([to_display.transform((x, items[i][0]))[1] for i in order], dtype=float)
    heights = np.array([line*scale*(items[i][1].count('\n')+1+(.85 if len(items[i]) > 3 else 0))
                        for i in order])
    for _ in range(400):
        moved = False
        for i in range(1, len(ys)):
            overlap = (heights[i-1]+heights[i])/2-(ys[i]-ys[i-1])
            if overlap > .01:
                ys[i-1] -= overlap/2
                ys[i] += overlap/2
                moved = True
        if not moved:
            break
    x_display = to_display.transform((x, items[order[0]][0]))[0]
    offset = dx if ha == 'left' else -dx
    for y_display, height, i in zip(ys, heights, order):
        text, colour, note = items[i][1], items[i][2], (items[i][3] if len(items[i]) > 3 else None)
        top = y_display+height/2
        lines = text.count('\n')+1
        y = to_data.transform((x_display, top-lines*line*scale/2))[1]
        ax.annotate(text, (x, y), xytext=(offset, 0), textcoords='offset points',
                    ha=ha, va='center', color=colour, annotation_clip=False)
        if note:
            y = to_data.transform((x_display, top-(lines+.42)*line*scale))[1]
            ax.annotate(note, (x, y), xytext=(offset, 0), textcoords='offset points', ha=ha,
                        va='center', color=MUTED, fontsize=6.5, annotation_clip=False)


def save(fig, out, name):
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out/f'{name}.pdf')
    fig.savefig(out/f'{name}.png', dpi=300)
    print(out/f'{name}.pdf')
