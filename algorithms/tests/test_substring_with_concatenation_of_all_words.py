""" Test module for Substring with Concatenation of All Words """

from parameterized import parameterized

from algorithms.substring_with_concatenation_of_all_words import find_substring

@parameterized.expand([
    ("barfoothefoobarman", ["foo","bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12]),
    ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8]),
    ("ababababab", ["ababa","babab"], [0]),
    ("aaaaaaaaaaaaaa", ["aa","aa"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
])
def test_find_substring(string: str, words: list[str], expected: list[int]) -> None:
    """ Test function """
    solution = find_substring(string, words)
    assert sorted(solution) == expected
    print(f"s = {string:25s}, words = [{', '.join(words):23s}]")
    print(f"\treturned correct result of {solution}")
