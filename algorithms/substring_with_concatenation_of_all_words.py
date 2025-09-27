"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words

30. Substring with Concatenation of All Words (Hard)

Problem statement:

You are given a string s and an array of strings words. All the strings of words are of the same
length.

A concatenated string is a string that exactly contains all the strings of any permutation of words
concatenated.
- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd",
and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not
the concatenation of any permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the
answer in any order.
"""

from collections import defaultdict

def find_substring(string: str, words: list[str]) -> list[int]:
    """ Find starting indices of concatenated substrings """
    returns = []
    starts = [(None, 0) for _ in string]

    # Determine the number of duplicate words starting at some position,
    # using a dict of word -> (index, count)
    unique_words = {}
    for i, word in enumerate(words):
        tup = unique_words.get(word, (None, 0))
        unique_words[word] = (i, tup[1] + 1)

    word_len = len(words[0])

    for i in range(len(string) - word_len + 1):
        tup = unique_words.get(string[i:i + word_len])
        if tup is not None:
            starts[i] = tup

    # Go through string once for each word index, tracking current sequence of words
    # - Reset when there isn't a word at current position
    # - If current sequence has same word too many times, remove words from start of sequence
    # until fixed
    # - If current sequence length matches number of words, output it, and shift up start
    for w_offset in range(0, word_len):
        seen = defaultdict(int)
        seen_total = 0
        start = w_offset
        for si in range(w_offset, len(string), word_len):
            if starts[si][0] is None:
                seen = defaultdict(int)
                seen_total = 0
                start = si + word_len
            else:
                if starts[si][1] == seen[starts[si][0]]:
                    while starts[si][1] == seen[starts[si][0]]:
                        seen[starts[start][0]] -= 1
                        seen_total -= 1
                        start += word_len
                seen[starts[si][0]] += 1
                seen_total += 1
                if seen_total == len(words):
                    returns.append(start)
                    seen[starts[start][0]] -= 1
                    seen_total -= 1
                    start += word_len

    return returns
