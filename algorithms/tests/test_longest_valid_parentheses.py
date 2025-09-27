""" Test module for Longest Valid Parentheses """

from parameterized import parameterized

from algorithms.longest_valid_parentheses import (longest_valid_parentheses_stack,
                                                  longest_valid_parentheses_two_pass)

TEST_VALUES = [
    ("", 0),
    ("(()", 2),
    (")()())", 4),
    ("(())", 4),
    (")()())()()(", 4),
    ("(()))())(", 4),
    (")()()(()())()())", 14),
]

@parameterized.expand(TEST_VALUES)
def test_longest_valid_parentheses_stack(string: str, expected: int) -> None:
    """ Test function for stack """
    solution = longest_valid_parentheses_stack(string)
    assert solution == expected
    print(f"{string:16s} returned correct result of {expected}")

@parameterized.expand(TEST_VALUES)
def test_longest_valid_parentheses_two_pass(string: str, expected: int) -> None:
    """ Test function for two-pass """
    solution = longest_valid_parentheses_two_pass(string)
    assert solution == expected
    print(f"{string:16s} returned correct result of {expected}")
