"""
https://leetcode.com/problems/longest-valid-parentheses

32. Longest Valid Parentheses (Hard)

Problem statement:

Given a string containing just the characters '(' and ')', return the length of the longest valid
(well-formed) parentheses substring.
"""

def longest_valid_parentheses_stack(string: str) -> int:
    """
    Find longest valid parentheses using a stack to store the starts of each longest valid
    substring. We do this by storing the position of each opening parenthesis, offset by the longest
    valid substring ending at that point, to correctly handle cases like `()()`. This is then
    popped from the stack to match with closing parentheses, as those are encountered, from where
    the current length is calculated. An unmatched closing parenthesis resets the current length.
    """
    starts = []
    longest = 0
    last_length = 0
    for pos, val in enumerate(string):
        if val == "(":
            # Store the start of the longest valid substring, which is the position of the `(`,
            # offset by the longest valid substring ending at that point, to correctly handle cases
            # like `()()`
            starts.append(pos - last_length)
            last_length = 0
        elif starts:
            # When we find a `)`, pop the start of the substring from the stack to calculate the
            # current substring length, and store that length for the next `(`
            start = starts.pop()
            length = pos - start + 1
            last_length = length
            longest = max(longest, length)
        else:
            # If we find an unmatched `)`, reset the current length
            last_length = 0
    return longest


def longest_valid_parentheses_two_pass(string: str) -> int:
    """
    Find longest valid parentheses by taking the maximum of a forward and backward pass. The forward
    pass detects unmatched right parentheses, while the backward pass detects unmatched left
    parentheses.
    """
    longest = 0

    lefts = rights = 0
    for val in string:
        if val == "(":
            lefts += 1
        else:
            rights += 1

        if rights > lefts:
            lefts = rights = 0
        elif lefts == rights:
            longest = max(longest, lefts + rights)

    lefts = rights = 0
    for val in reversed(string):
        if val == "(":
            lefts += 1
        else:
            rights += 1

        if lefts > rights:
            lefts = rights = 0
        elif lefts == rights:
            longest = max(longest, lefts + rights)
    return longest
