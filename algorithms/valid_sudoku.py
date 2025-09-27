"""
https://leetcode.com/problems/valid-sudoku

36. Valid Sudoku (Medium)

Problem statement:

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

SIZE = 9
SQUARE_SIZE = 3
SQUARE_COUNT = SIZE // SQUARE_SIZE

def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Check if a given board is a valid sudoku by checking that each row, column and 3x3 square has
    no duplicated numbers. Uses a bitmask for efficiency - each bit corresponds to a number 1-9.
    """
    # pylint: disable=too-many-branches

    # Convert input to integers first
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == ".":
                board[row][col] = 0
            else:
                board[row][col] = int(board[row][col])

    # Check that each row is valid
    for row in range(SIZE):
        seen_mask = 0
        for col in range(SIZE):
            if board[row][col] != 0:
                val = 2 ** board[row][col]
                if seen_mask & val:
                    return False
                seen_mask |= val

    # Check that each column is valid
    for col in range(SIZE):
        seen_mask = 0
        for row in range(SIZE):
            if board[row][col] != 0:
                val = 2 ** board[row][col]
                if seen_mask & val:
                    return False
                seen_mask |= val

    # Check that each square is valid
    for row_square in range(SQUARE_COUNT):
        for col_square in range(SQUARE_COUNT):
            seen_mask = 0
            for row in range(SQUARE_SIZE):
                for col in range(SQUARE_SIZE):
                    val = board[SQUARE_SIZE * row_square + row][SQUARE_SIZE * col_square + col]
                    if val == 0:
                        continue
                    val = 2 ** val
                    if seen_mask & val:
                        return False
                    seen_mask |= val

    return True
