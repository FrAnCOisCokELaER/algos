# #https://leetcode.com/problemset/top-interview-questions/?difficulty=Medium&listId=wpwgkgt
#
#
# # ex 1
# # You are given two non-empty linked lists representing two non-negative integers.
# # The digits are stored in reverse order and each of their nodes contain a single digit.
# # Add the two numbers and return it as a linked list.
# # You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# # Example:
# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8
# # Explanation: 342 + 465 = 807.
#
# #time complexity : O(M+N)
# #space complexity : O(M+N)
# from typing import Set, Any
#
#
def addtwonumbers(number1, number2):
    totalcount = 0
    for idx, val in enumerate(number1):
        totalcount += val*10**idx
    for idx, val in enumerate(number2):
        totalcount += val * 10**idx
    countstring = str(totalcount)
    return sorted(list(map(int, countstring)), reverse=True)
#
#
# #ex 2
#
# # Given a string, find the length of the longest substring without repeating characters.
# #
# # Example 1:
# #
# # Input: "abcabcbb"
# # Output: 3
# # Explanation: The answer is "abc", with the length of 3.
# # Example 2:
# #
# # Input: "bbbbb"
# # Output: 1
# # Explanation: The answer is "b", with the length of 1.
# # Example 3:
# #
# # Input: "pwwkew"
# # Output: 3
# # Explanation: The answer is "wke", with the length of 3.
# #              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
def longestsubstring(s):
    charset = set()
    currcount = maxcount =  0
    for char in s:
        if char not in charset:
            currcount += 1
            charset.add(char)
        else:
            if currcount > maxcount:
                maxcount = currcount
            currcount = 0
            charset.clear()
    return maxcount
#
# # ex3
# # **Given a string s, find the longest palindromic substring in s.
# # You may assume that the maximum length of s is 1000.
# # Example 1:
# # Input: "babad"
# # Output: "bab"
# # Note: "aba" is also a valid answer.
# # Example 2:
# # Input: "cbbd"
# # Output: "bb"
#
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
#
# #ex4
# # Implement atoi which converts a string to an integer.
# # The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# # Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
# # as possible, and interprets them as a numerical value.
# # The string can contain additional characters after those that form the integral number, which are ignored and have
# # no effect on the behavior of this function.
# # If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
# # because either str is empty or it contains only whitespace characters, no conversion is performed.
# # If no valid conversion could be performed, a zero value is returned.
# # Note:
# # Only the space character ' ' is considered as whitespace character.
# # Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
# #     [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# # Example 1:
# # Input: "42"
# # Output: 42
# # Example 2:
# #
# # Input: "   -42"
# # Output: -42
# # Explanation: The first non-whitespace character is '-', which is the minus sign.
# #              Then take as many numerical digits as possible, which gets 42.
# # Example 3:
# #
# # Input: "4193 with words"
# # Output: 4193
# # Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# # Example 4:
# #
# # Input: "words and 987"
# # Output: 0
# # Explanation: The first non-whitespace character is 'w', which is not a numerical
# #              digit or a +/- sign. Therefore no valid conversion could be performed
#
#
# #ex5 container with most water
# # Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
# # are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# #     forms a container, such that the container contains the most water.
#
#
# #ex6
# # three sum problem
# # Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# # Find all unique triplets in the array which gives the sum of zero.
# #
# # Note:
# #
# # The solution set must not contain duplicate triplets.
# #
# # Example:
# #
# # Given array nums = [-1, 0, 1, 2, -1, -4],
# #
# # A solution set is:
# # [
# #   [-1, 0, 1],
# #   [-1, -1, 2]
# # ]
#

#combinatorial problem ( 3 in n)  (3!)
def threesum(nums):
    def generatealltriplets(triplet, nums, globalacc):
        if len(triplet) == 3:
            if sum(triplet) is 0:
                globalacc.append(triplet)
        else:
            for idx, num in enumerate(nums):
                generatealltriplets(triplet + (num,), nums[0:idx] + nums[idx+1:], globalacc)

    globalacc = list()
    triplet = tuple()
    generatealltriplets(triplet, nums, globalacc)
    return globalacc

#def threesum(nums):
#     def generatealltriplets(triplet, nums):
#         if len(triplet) == 3:
#             if sum(triplet) is 0:
#                 return triplet
#         else:
#             res = list()
#             for idx, num in enumerate(nums):
#                 res.append(generatealltriplets(triplet + (num,), nums[0:idx] + nums[idx + 1:]))
#             return res
#    triplet = tuple()
#    acc = list()
#    return generatealltriplets(triplet, nums, acc)

#
#
# #ex7
# # Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# #
# # A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# #
# # Example:
# #
# # Input: "23"
# # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# # Note:
# #
# # Although the above answer is in lexicographical order, your answer could be in any order you want.
#
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
#
# #ex8
# # Given a linked list, remove the n-th node from the end of list and return its head.
# #
# # Example:
# #
# # Given linked list: 1->2->3->4->5, and n = 2.
# #
# # After removing the second node from the end, the linked list becomes 1->2->3->5.
# # Note:
# #
# # Given n will always be valid.
# #
# # Follow up:
# #
# # Could you do this in one pass?
#
#
# #ex9
# # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# #
# # For example, given n = 3, a solution set is:
# #
# # [
# #   "((()))",
# #   "(()())",
# #   "(())()",
# #   "()(())",
# #   "()()()"
# # ]
#
#
# #ex10
# # Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# #
# # Return the quotient after dividing dividend by divisor.
# #
# # The integer division should truncate toward zero.
# #
# # Example 1:
# #
# # Input: dividend = 10, divisor = 3
# # Output: 3
# # Example 2:
# #
# # Input: dividend = 7, divisor = -3
# # Output: -2
# # Note:
# #
# # Both dividend and divisor will be 32-bit signed integers.
# # The divisor will never be 0.
# # Assume we are dealing with an environment which could only store integers within the
# # 2-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
#
#
#
# #ex11
# # Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# #
# # Your algorithm's runtime complexity must be in the order of O(log n).
# #
# # If the target is not found in the array, return [-1, -1].
# #
# # Example 1:
# #
# # Input: nums = [5,7,7,8,8,10], target = 8
# # Output: [3,4]
# # Example 2:
# #
# # Input: nums = [5,7,7,8,8,10], target = 6
# # Output: [-1,-1]
#

# def findpositions(alist, val):
#     #dichotomy to find the index in log(n)
#     #starting from this index run in foundidx - i and foundidx + i until the value change
#     #return the index

# #ex12
# # Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# #
# # Each row must contain the digits 1-9 without repetition.
# # Each column must contain the digits 1-9 without repetition.
# # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# # The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# #
# # Example 1:
# #
# # Input:
# # [
# #   ["5","3",".",".","7",".",".",".","."],
# #   ["6",".",".","1","9","5",".",".","."],
# #   [".","9","8",".",".",".",".","6","."],
# #   ["8",".",".",".","6",".",".",".","3"],
# #   ["4",".",".","8",".","3",".",".","1"],
# #   ["7",".",".",".","2",".",".",".","6"],
# #   [".","6",".",".",".",".","2","8","."],
# #   [".",".",".","4","1","9",".",".","5"],
# #   [".",".",".",".","8",".",".","7","9"]
# # ]
# # Output: true
# # Example 2:
# #
# # Input:
# # [
# #   ["8","3",".",".","7",".",".",".","."],
# #   ["6",".",".","1","9","5",".",".","."],
# #   [".","9","8",".",".",".",".","6","."],
# #   ["8",".",".",".","6",".",".",".","3"],
# #   ["4",".",".","8",".","3",".",".","1"],
# #   ["7",".",".",".","2",".",".",".","6"],
# #   [".","6",".",".",".",".","2","8","."],
# #   [".",".",".","4","1","9",".",".","5"],
# #   [".",".",".",".","8",".",".","7","9"]
# # ]
# # Output: false
# # Explanation: Same as Example 1, except with the 5 in the top left corner being
# #     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
# #ex13
# # Given a collection of distinct integers, return all possible permutations.
# # #
# # # Example:
# # #
# # # Input: [1,2,3]
# # # Output:
# # # [
# # #   [1,2,3],
# # #   [1,3,2],
# # #   [2,1,3],
# # #   [2,3,1],
# # #   [3,1,2],
# # #   [3,2,1]
# # # ]
#
#
# #ex14
# #
# # You are given an n x n 2D matrix representing an image.
# #
# # Rotate the image by 90 degrees (clockwise).
# #
# # Note:
# #
# # You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# #
# # Example 1:
# #
# # Given input matrix =
# # [
# #   [1,2,3],
# #   [4,5,6],
# #   [7,8,9]
# # ],
# #
# # rotate the input matrix in-place such that it becomes:
# # [
# #   [7,4,1],
# #   [8,5,2],
# #   [9,6,3]
# # ]
# # Example 2:
# #
# # Given input matrix =
# # [
# #   [ 5, 1, 9,11],
# #   [ 2, 4, 8,10],
# #   [13, 3, 6, 7],
# #   [15,14,12,16]
# # ],
# #
# # rotate the input matrix in-place such that it becomes:
# # [
# #   [15,13, 2, 5],
# #   [14, 3, 4, 1],
# #   [12, 6, 8, 9],
# #   [16, 7,10,11]
# # ]
#
#
# #15
# # Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# #
# # If the fractional part is repeating, enclose the repeating part in parentheses.
# # Input: numerator = 1, denominator = 2
# # Output: "0.5"
# # Input: numerator = 2, denominator = 3
# # # # Output: "0.(6)"
#
# #16
# # A message containing letters from A-Z is being encoded to numbers using the following mapping:
# # 'A' -> 1
# # 'B' -> 2
# # ...
# # 'Z' -> 26
# # Given a non-empty string containing only digits, determine the total number of ways to decode it.
# # Input: "12"
# # Output: 2
# # Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
# #17
# # Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# #
# # A region is captured by flipping all 'O's into 'X's in that surrounded region.
# #
# # X X X X
# # X O O X
# # X X O X
# # X O X X
# #
# # After running your function, the board should be:
# #
# # X X X X
# # X X X X
# # X X X X
# # X O X X
# #
# # Explanation:
# #
# # Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
# # 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells
# # are connected if they are adjacent cells connected horizontally or vertically.
#
# #18
# # Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# #
# # Only one letter can be changed at a time.
# # Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# # Note:
# #
# # Return 0 if there is no such transformation sequence.
# # All words have the same length.
# # All words contain only lowercase alphabetic characters.
# # You may assume no duplicates in the word list.
# # You may assume beginWord and endWord are non-empty and are not the same.
# # Input:
# # beginWord = "hit",
# # endWord = "cog",
# # wordList = ["hot","dot","dog","lot","log","cog"]
# #
# # Output: 5
# #
# # Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# # return its length 5.
# #
# # Input:
# # beginWord = "hit"
# # endWord = "cog"
# # wordList = ["hot","dot","dog","lot","log"]
# #
# # Output: 0
# #
# # Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
# #19
# # Given a binary tree, determine if it is a valid binary search tree (BST).
# #
# # Assume a BST is defined as follows:
# #
# # The left subtree of a node contains only nodes with keys less than the node's key.
# # The right subtree of a node contains only nodes with keys greater than the node's key.
# # Both the left and right subtrees must also be binary search trees.
# #  2
# #    / \
# #   1   3
# #
# # Input: [2,1,3]
# # Output: true
# #
# #  \
# #   1   4
# #      / \
# #     3   6
# #
# # Input: [5,1,4,null,null,3,6]
# # Output: false
# # Explanation: The root node's value is 5 but its right child's value is 4.
#
# #20
# # Given a list of non negative integers, arrange them such that they form the largest number.
# # Input: [10,2]
# # Output: "210"
# # Input: [3,30,34,5,9]
# # Output: "9534330"
# # Note: The result may be very large, so you need to return a string instead of an integer.
#
# #21
# # A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# #
# # Return a deep copy of the list.
# #
# # Input:
# # {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# #
# # Explanation:
# # Node 1's value is 1, both of its next and random pointer points to Node 2.
# # Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
# # Note:
# #
# # You must return the copy of the given head as a reference to the cloned list.
#
#
# #22
# # Implement pow(x, n), which calculates x raised to the power n (xn).
# # Example 1:
# #
# # Input: 2.00000, 10
# # Output: 1024.00000
# #
# # Example 2:
# #
# # Input: 2.10000, 3
# # Output: 9.26100
# #
# # Note:
# #
# # -100.0 < x < 100.0
# # n is a 32-bit signed integer, within the range [−231, 231 − 1]
#
# #23
# # Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
# # Example 1:
# #
# # Input: [2,3,-2,4]
# # Output: 6
# # Explanation: [2,3] has the largest product 6.
# #
# # Example 2:
# #
# # Input: [-2,0,-1]
# # Output: 0
# # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
# #24
# #You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# #fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# # Example 1:
# #
# # Input: coins = [1, 2, 5], amount = 11
# # Output: 3
# # Explanation: 11 = 5 + 5 + 1
#
# #25
# # Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# # Input: [3,2,1,5,6,4] and k = 2
# # Output: 5
# # Input: [3,2,3,1,2,4,5,5,6] and k = 4
#
# # Output: 4
#
# #26
# # wiggle sort
# # Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# # Input: nums = [1, 5, 1, 1, 6, 4]
# # Output: One possible answer is [1, 4, 1, 5, 1, 6].
# #
# # #27
# # Given a collection of intervals, merge all overlapping intervals.
# # Input: [[1,3],[2,6],[8,10],[15,18]]
# # Output: [[1,6],[8,10],[15,18]]
# # Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# # Input: [[1,4],[4,5]]
# # Output: [[1,5]]
# # Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# #
# # #28
# # Given an unsorted array of integers, find the length of longest increasing subsequence.
# # Input: [10,9,2,5,3,7,101,18]
# # Output: 4
# # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# # There may be more than one LIS combination, it is only necessary for you to return the length.
# # Your algorithm should run in O(n2) complexity.
# # Follow up: Could you improve it to O(n log n) time complexity?
# #
# # #29
# # . Palindrome Partitioning
# #
# # Given a string s, partition s such that every substring of the partition is a palindrome.
# #
# # Return all possible palindrome partitioning of s.
# #
# # Example:
# #
# # Input: "aab"
# # Output:
# # [
# #   ["aa","b"],
# #   ["a","a","b"]
# # ]
#
# #30
# # Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# #
# # You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# #
# # Input:
# # 	Tree 1                     Tree 2
# #           1                         2
# #          / \                       / \
# #         3   2                     1   3
# #        /                           \   \
# #       5                             4   7
# # Output:
# # Merged tree:
# # 	     3
# # 	    / \
# # 	   4   5
# # 	  / \   \
# # 	 5   4   7
# #
# # Note: The merging process must start from the root nodes of both trees.
#
#
# #31
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
#
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#
# #32
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
# #32
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days
# you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
#
#
# #33
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
# #34
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
# #34
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
# #35
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
#
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
    #
    print("threesum exercise")
    nums = [-1, 0, 1, 2, -1, -4]
    #print(list(map(list,set(threesum(nums)))))

    print(threesum(nums))

    atuple = (1,2,3)
    print(sum(atuple))
    import functools
    print(functools.reduce(lambda a, b: a * 60 + b, atuple, 0))
    print(sorted(atuple, reverse=True))

    # ex6  digits to letter in  a recrusive way
    #print(digitstoletter('2369584325'))