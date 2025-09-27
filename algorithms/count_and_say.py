"""
https://leetcode.com/problems/count-and-say

38. Count and Say (Medium)

Problem statement:

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive
identical characters (repeated 2 or more times) with the concatenation of the character and the
number marking the count of the characters (length of the run). For example, to compress the string
"3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1"
with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.
"""

def count_and_say(n: int) -> str:
    """ Iteratively generate the run-length encoding of the string "1" """
    string = "1"
    for _ in range(n-1):
        next_string = ""
        last = ""
        last_length = 0
        for c in string:
            if c == last:
                last_length += 1
            else:
                if last_length:
                    next_string += str(last_length) + last
                last = c
                last_length = 1
        string = next_string + str(last_length) + last
    return string
