#!/usr/bin/env python3
#coding=utf-8
"""
for testing chess.py

Unittests to be added
"""

import chess

if __name__ == "__main__":
    plt = chess.plt
    b = chess.Board()
    b.draw()
    plt.show()
    input('Press any button to continue... ')
    plt.close()
