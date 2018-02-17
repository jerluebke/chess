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
import matplotlib.text as text

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

    def __init__(self):
        self.fig, self.axes = self.draw()
        self.selected = None
        self.wp1 = Piece(self.axes, '\u265f', 'white', (1, 2), True, None)
        self.bp1 = Piece(self.axes, '\u265f', 'black', (7, 7), True, None)
        self.axes[1].add_artist(self.wp1)
        self.axes[1].add_artist(self.bp1)
        self.fig.canvas.draw()

        pick_id = self.fig.canvas.mpl_connect('pick_event', self.select)
        set_id = self.fig.canvas.mpl_connect('button_press_event', self.set_piece)


    def draw(self):
        """draw chessboard with pyplot"""
        fig = plt.figure(figsize=(10, 8))
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
        return fig, [left, center, right]

    def select(self, event):
        if isinstance(event.artist, Piece):
            self.selected = event.artist

    def set_piece(self, event):
        if self.selected is None:
            return
        if event.dblclick:
            self.selected.set_position((round(event.xdata), round(event.ydata)))
            self.fig.canvas.draw()
            self.selected = None


class Piece(text.Text):
    """
    Subclass of mpl.text.Text
    Base class for chess pieces
    """
    is_captured = False
    has_captured = []
    positions = []

    textprops = {'verticalalignment'    :   'center',
                 'horizontalalignment'  :   'center',
                 'fontsize'             :   50}

    def __init__(self, axes, symbol, color, initial_pos, one_step, moves):
        """
        Params
            board       :   Board instance which contains the Piece
            symbol      :   unicode character of the piece, string
            color       :   black or white, string
            initial_pos :   starting point, tuple (x, y)
            one_step    :   only one step per turn, boolean
            moves       :   list of tuples indicating the directions in which
                            the piece can move
        """
        self.ax = axes[1]     # center
        self.sym = symbol
        self.color = color
        self.pos = initial_pos
        self.one_step = one_step
        self.moves = moves
        super().__init__(*self.pos, self.sym, self.color, **self.textprops)
        self.set_picker(True)

    # def __repr__(self):
    #     """return string describing the piece"""



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
