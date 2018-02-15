#coding=utf-8
"""
Programm for chess analysis
"""

import numpy as np
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gs

# settings for plotting
mpl.rcParams['grid.linestyle'] = ' '    # no grid
mpl.rcParams['xtick.major.size'] = 0    # no ticks
mpl.rcParams['ytick.major.size'] = 0

# custom colormap
paired = plt.cm.Paired
chess_cm = mcolors.LinearSegmentedColormap.from_list('chessboard_1',
                                                     [paired(10), paired(11)],
                                                     N=2)

def draw_board():
    """draw chessboard with pyplot"""
    plt.figure(figsize=(10, 8))
    grid = gs.GridSpec(1, 3, width_ratios=[1, 4, 1])
    left = plt.subplot(grid[0])
    center = plt.subplot(grid[1])
    right = plt.subplot(grid[2])

    board = np.array(([0, 1]*4 + [1, 0]*4)*4)
    board.shape = (8, 8)
    center.imshow(board, cmap=chess_cm, extent=(.5, 8.5, .5, 8.5))
    center.set_xticklabels([0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

    for ax in (left, right):
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set(xlim=(0.5, 2.5), ylim=(0.5, 8.5))

    plt.tight_layout()

    return [left, center, right]
