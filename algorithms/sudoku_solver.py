"""
https://leetcode.com/problems/sudoku-solver

37. Sudoku Solver (Hard)

Problem statement:

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""

from collections import defaultdict

SIZE = 9
SQUARE_SIZE = 3
SQUARE_COUNT = SIZE // SQUARE_SIZE

class SudokuSolver:
    """ Solves sudoku grids """
    def __init__(self, board: list[list[str]]) -> None:
        self.valids: list[list[set[str]]] = [[set(str(i + 1) for i in range(SIZE))
                                              for _ in range(SIZE)] for _ in range(SIZE)]
        self.board: list[list[str]] = board
        self.assigned_rows: list[set] = [set() for _ in range(SIZE)]
        self.assigned_cols: list[set] = [set() for _ in range(SIZE)]
        self.assigned_squares: dict[tuple[int, int], set[str]] = defaultdict(set)

    def set_value(self, row, col, val):
        """
        Set a value on the board, clear its set of possible values, and remove its value from valid
        neighbours.
        """
        self.board[row][col] = val
        self.valids[row][col] = set()
        self.remove_valid_neighbours(row, col)

    def remove_valid(self, row: int, col: int, value: str) -> None:
        """
        Remove a given value from the set of possible values for `board[row][col]`. If it was
        removed and only 1 other value remains, set the board cell to that value.
        """
        valid_set = self.valids[row][col]
        if value in valid_set:
            valid_set.remove(value)
            if len(valid_set) == 1:
                remaining_value = next(iter(valid_set))
                self.set_value(row, col, remaining_value)

    def remove_valid_neighbours(self, row: int, col: int) -> None:
        """
        Remove the value of `board[row][col]` from the valid set of its "neighbours" (all cells
        in the same row, column or 3x3 square).
        """
        val = self.board[row][col]
        if val != ".":
            for row2 in range(SIZE):
                self.remove_valid(row2, col, val)
            for col2 in range(SIZE):
                self.remove_valid(row, col2, val)
            for row2 in range(SQUARE_SIZE):
                for col2 in range(SQUARE_SIZE):
                    self.remove_valid(row2 + SQUARE_SIZE * (row // SQUARE_SIZE),
                                      col2 + SQUARE_SIZE * (col // SQUARE_SIZE), val)

    def update_locations(self, row: int, col: int,
                         locations: dict[str, tuple[int, int] | tuple[None, None]]) -> None:
        """ Update the valid locations with the value in the given cell """
        for valid in self.valids[row][col]:
            if valid in locations:
                # Use None to indicate that a value has multiple valid locations
                locations[valid] = (None, None)
            else:
                locations[valid] = (row, col)

    def process_locations(self, locations: dict[str, tuple[int, int] | tuple[None, None]]) -> bool:
        """ If locations contains unique values, set those on the board """
        updated = False
        for val, (row, col) in locations.items():
            # Set values with only 1 valid location
            if row is not None:
                self.set_value(row, col, val)
                updated = True
        return updated

    def backtracking(self, row_col = 0) -> bool:
        """
        Recursively try to populate each cell with some possible value.
        Backtrack if this doesn't lead to a solution.
        """
        while row_col < SIZE * SIZE:
            row = row_col // SIZE
            col = row_col % SIZE
            if self.valids[row][col]:
                for valid in self.valids[row][col]:
                    square = (row // SQUARE_SIZE, col // SQUARE_SIZE)
                    if (valid not in self.assigned_rows[row] and
                            valid not in self.assigned_cols[col] and
                            valid not in self.assigned_squares[square]):
                        self.board[row][col] = valid
                        self.assigned_rows[row].add(valid)
                        self.assigned_cols[col].add(valid)
                        self.assigned_squares[square].add(valid)

                        if self.backtracking(row_col + 1):
                            return True

                        self.board[row][col] = "."
                        self.assigned_rows[row].remove(valid)
                        self.assigned_cols[col].remove(valid)
                        self.assigned_squares[square].remove(valid)
                return False
            row_col += 1
        return True

    def set_unique_values(self) -> None:
        """
        Set values that are unique within the possible values of their row, column or 3x3 grid,
        meaning they can only be put in 1 place.
        """
        # Repeat this until no updates are made
        updated = True
        while updated:
            updated = False
            # Check for unique values in each row
            for row in range(SIZE):
                locations = {}
                for col in range(SIZE):
                    self.update_locations(row, col, locations)
                updated |= self.process_locations(locations)

            # Check for unique values in each column
            for col in range(SIZE):
                locations = {}
                for row in range(SIZE):
                    self.update_locations(row, col, locations)
                updated |= self.process_locations(locations)

            # Check for unique values in each 3x3 square
            for row_square in range(SQUARE_COUNT):
                for col_square in range(SQUARE_COUNT):
                    locations = {}
                    for row_local in range(SQUARE_SIZE):
                        for col_local in range(SQUARE_SIZE):
                            row = SQUARE_SIZE * row_square + row_local
                            col = SQUARE_SIZE * col_square + col_local
                            self.update_locations(row, col, locations)
                    updated |= self.process_locations(locations)

    def solve(self) -> None:
        """ Run the solver and returns whether it was successful """
        # For prefilled values, clear set of possible values
        for row in range(SIZE):
            for col in range(SIZE):
                val = self.board[row][col]
                if val != ".":
                    self.valids[row][col] = set()

        for row in range(SIZE):
            for col in range(SIZE):
                self.remove_valid_neighbours(row, col)

        self.set_unique_values()

        return self.backtracking()
