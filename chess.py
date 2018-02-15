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

plt.style.use('chess_style')

# custom colormap
paired = plt.cm.Paired
chess_cm = mcolors.LinearSegmentedColormap.from_list('chessboard_1',
                                                     [paired(10), paired(11)],
                                                     N=2)
out_cm = mcolors.LinearSegmentedColormap.from_list('chessboard_2',
                                                   [paired(0), paired(1)],
                                                   N=2)

class Board:
    """
    TODO: add description of this class
    """
    def draw(self):
        """draw chessboard with pyplot"""
        plt.figure(figsize=(10, 8))
        grid = gs.GridSpec(1, 3, width_ratios=[1, 4, 1])
        left = plt.subplot(grid[0])
        center = plt.subplot(grid[1])
        right = plt.subplot(grid[2])

        # make chessboard
        board = np.array(([0, 1]*4 + [1, 0]*4)*4)
        board.shape = (8, 8)
        center.imshow(board, cmap=chess_cm, extent=(.5, 8.5, .5, 8.5))
        center.set_xticklabels([0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

        # make outside areas (to place captured pieces)
        dump = np.array(([0, 1] + [1, 0])*4)
        dump.shape = (8, 2)
        for ax in (left, right):
            ax.imshow(dump, cmap=out_cm, extent=(.5, 2.5, .5, 8.5))
            ax.set_xticklabels([])
            ax.set_yticklabels([])

        plt.tight_layout()
        return [left, center, right]


class Piece:
    """
    Base class for chess pieces
    """
    is_captured = False
    has_captured = []
    positions = []

    def __init__(self, symbol, color, initial_pos, one_step, moves):
        """
        Params
            symbol      :   unicode character of the piece, string
            color       :   black or white, string
            initial_pos :   starting point, tuple (x, y)
            one_step    :   only one step per turn, boolean
            moves       :   list of tuples indicating the directions in which
                            the piece can move
        """
        self.sym = symbol
        self.color = color
        self.pos = initial_pos
        self.one_step = one_step
        self.moves = moves

    def __repr__(self):
        """return string describing the piece"""


class King(Piece):
    pass


class Queen(Piece):
    pass


class Bishop(Piece):
    pass


class Knight(Piece):
    pass


class Rook(Piece):
    pass


class Pawn(Piece):
    pass
