#https://leetcode.com/problemset/top-interview-questions/?difficulty=Medium&listId=wpwgkgt


# ex 1
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

#time complexity : O(M+N)
#space complexity : O(M+N)
from typing import Set, Any


def addtwonumbers(number1, number2):
    totalcount = 0
    for idx, val in enumerate(number1):
        totalcount += val*10**idx
    for idx, val in enumerate(number2):
        totalcount += val * 10**idx
    countstring = str(totalcount)
    return sorted(list(map(int, countstring)), reverse=True)


#ex 2

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longestsubstring(s):
    charset = set()
    maxcount = 0
    for char in s:
        if char not in charset:
            maxcount += 1
            charset.add(char)
        else:
            return maxcount
    return maxcount

# ex3
# **Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"

def ispalindrom(word):
    wordlength = len(word)
    if wordlength == 0 or wordlength == 1:
        return True
    elif word[0] != word[wordlength-1]:
        return False
    else:
        return ispalindrom(word[1:-1])

def longestpalindrom(word):
    #given an offset generate all possible substrings
    def substrings(word, offset):
        sublen = len(word) - offset
        if sublen <= 0:
            return list()
        acc = []
        for o in range(0,offset+1):
            if o + sublen <= len(word):
                acc.append(word[o:o+sublen])
        return acc
    globalacc = []
    for o in range(0, len(word)):
        globalacc.append(substrings(word, o))

    return globalacc

#ex4
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
# as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have
# no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
# because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
#     [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed



#ex5
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


    #combinatorial problem ( 3 in n)
    # def generatealltriplets(triplet, nums, globalacc):
    #     if len(triplet) == 3:
    #         globalacc.append(triplet)
    #     else:
    #         for idx, num in enumerate(nums):
    #             generatealltriplets(triplet + (num,), nums[0:idx] + nums[idx+1:], globalacc)
    #
    # globalacc = list()
    # triplet = tuple()
    # generatealltriplets(triplet, nums, globalacc)
    # return globalacc

def threesum(nums):
    def generatealltriplets(triplet, nums):
        if len(triplet) == 3:
            if sum(triplet) is 0:
                return triplet
        else:
            res = list()
            for idx, num in enumerate(nums):
                res.append(generatealltriplets(triplet + (num,), nums[0:idx] + nums[idx + 1:]))
            return res

    triplet = tuple()
    acc = list()
    for sublists in generatealltriplets(triplet, nums):
        for sub in sublists:
            for triplet in  sub:
                acc.append(triplet)
    return set(acc)


#ex6
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.

def digitstoletter(digits): #stirng of number
    telmap = dict()
    telmap[2] = ['a','b','c']
    telmap[3] = ['d', 'e', 'f']
    telmap[4] = ['g', 'h', 'i']
    telmap[5] = ['j', 'k', 'l']
    telmap[6] = ['m', 'n', 'o']
    telmap[7] = ['p', 'q', 'r']
    telmap[8] = ['p', 'q', 'r','s']
    telmap[9] = ['v', 'w', 'x', 'y', 'z']

    def toword(digits, word, acc):
        if not digits:
            acc.append(word)
        else:
            for achar in telmap[digits[0]]:
                toword(digits[1:], word+achar, acc)
    acc = []
    toword([int(d) for d in digits], '', acc)
    return acc
if __name__ == "__main__":

    #ex 1
    number1 = [2,4,3]
    number2 = [5,6,4]
    print(addtwonumbers(number1, number2))

    #ex 2
    print(longestsubstring("pwwkew"))

    #ex 3
    testpalindrom = 'abccba'
    print(ispalindrom(testpalindrom))
    testpalindrom = 'abcdba'
    print(ispalindrom(testpalindrom))
    print(longestpalindrom(testpalindrom))
    allsubstrings = [item for sublist in longestpalindrom(testpalindrom) for item in sublist]
    print(allsubstrings)
    allpalinfroms = list(map(ispalindrom, allsubstrings))
    print(allpalinfroms)

    #5
    nums = [-1, 0, 1, 2, -1, -4]
    #print(list(map(list,set(threesum(nums)))))

    print(threesum(nums))

    atuple = (1,2,3)
    print(sum(atuple))
    import functools
    print(functools.reduce(lambda a, b: a * 60 + b, atuple, 0))
    print(sorted(atuple, reverse=True))

    # ex6  digits to letter in  a recrusive way
    print(digitstoletter('2369584325'))