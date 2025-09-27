""" Test module for Valid Sudoku """

import pytest

from algorithms.valid_sudoku import is_valid_sudoku

def generate_board(partial_board: list[list[int]]) -> list[list[str]]:
    """ Generates a full board from a given partial board (starting from the top left) """
    board = [["." for _ in range(9)] for _ in range(9)]
    for row_index, row in enumerate(partial_board):
        for col_index, cell in enumerate(row):
            if cell == 0:
                board[row_index][col_index] = "."
            else:
                board[row_index][col_index] = str(cell)
    return board

VALID_BOARDS = [
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]],
    # Board with a value exactly once in every row, column and 3x3 square
    generate_board([
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]),
    # Empty board
    generate_board([]),
]

INVALID_BOARDS = [
    [["8","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]],
    # Row with duplicated value
    generate_board([[0, 0, 0, 0, 6, 0, 0, 0, 6]]),
    # Column with duplicated value
    generate_board([[0], [2], [0], [0], [0], [2], [0], [0], [0]]),
    # Square with duplicated value
    generate_board([[0, 0, 0], [0, 0, 4], [0, 4, 0]]),
]

@pytest.mark.parametrize("board", VALID_BOARDS)
def test_is_valid_sudoku_valid(board: list[list[str]]) -> None:
    """ Test function for valid boards """
    print("\nCorrectly classified as valid:")
    assert is_valid_sudoku(board)
    for row in board:
        print(" ".join(map(str, row)))
    print()

@pytest.mark.parametrize("board", INVALID_BOARDS)
def test_is_valid_sudoku_invalid(board: list[list[str]]) -> None:
    """ Test function for invalid boards """
    print("\nCorrectly classified as invalid:")
    assert not is_valid_sudoku(board)
    for row in board:
        print(" ".join(map(str, row)))
    print()
