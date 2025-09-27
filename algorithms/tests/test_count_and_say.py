""" Test module for Substring with Concatenation of All Words """

from parameterized import parameterized

from algorithms.count_and_say import count_and_say

@parameterized.expand([
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
])
def test_count_and_say(n: int, expected: str) -> None:
    """ Test function """
    string = count_and_say(n)
    assert string == expected
    print(f"n = {n} returns the expected output of: {string}")
