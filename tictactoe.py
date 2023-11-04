"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import time

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    if x == o:
        return X
    elif x > o:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    temp = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                temp.append((i, j))
    return temp



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)

    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal and vertical
    for k in range(2):
        if k == 0:
            temp = X
        else:
            temp = O
        for i in range(3):
            counter = 0
            counter0 = 0
            for j in range(3):
                if board[i][j] == temp:
                    counter += 1
                if board[j][i] == temp:
                    counter0 += 1
            if counter == 3 or counter0 == 3:
                return temp

    #Diagonals
    if board[1][1] != EMPTY:
        temp = board[1][1]
        if (board[0][0] == temp and board[2][2] == temp) or (board[0][2] == temp and board[2][0] == temp):
            return temp

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                if winner(board) == None:
                    return False
                else:
                    return True
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
def if_empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                    return False
    return True

def best(board, alpha):
    if terminal(board):
        return utility(board)

    if player(board) == X:
        b = -2
        for i, j in actions(board):
            p = best(result(board, (i, j)), b)
            if p == "skip":
                continue
            if p > alpha:
                return "skip"
            if b < p:
                b = p
                coor = i, j
                if b == 1:
                    return best(result(board, coor), b)
    else:
        b = 2
        for i, j in actions(board):
            p = best(result(board, (i, j)), b)
            if p == "skip":
                continue
            if p < alpha:
                return "skip"
            if b > p:
                b = p
                coor = i, j
                if b == -1:
                    return best(result(board, coor), b)
    return best(result(board, coor), b)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if if_empty(board):
        return 0, 0
    if player(board) == X:
        b = -2
        for i, j in actions(board):
            p = best(result(board, (i, j)), b)
            if p == "skip":
                continue
            if b < p:
                b = p
                coor = i, j
    else:
        b = 2
        for i, j in actions(board):
            p = best(result(board, (i, j)), b)
            if p == "skip":
                continue
            if b > p:
                b = p
                coor = i, j
    return coor

    
