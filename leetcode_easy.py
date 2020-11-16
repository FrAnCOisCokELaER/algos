# #https://leetcode.com/problemset/all/?listId=wpwgkgt&difficulty=Easy
#
# #ex1
# # Write a function that reverses a string. The input string is given as an array of characters char[].
# # #
# # # Do not allocate extra space for another array,
#    you must do this by modifying the input array in-place with O(1) extra memory.
# # #
# # # You may assume all the characters consist of printable ascii characters.
# # # Example 1:
# # #
# # # Input: ["h","e","l","l","o"]
# # # Output: ["o","l","l","e","h"]
# # # Example 2:
# # #
# # # Input: ["H","a","n","n","a","h"]
# # # Output: ["h","a","n","n","a","H"]

#ex1 reverse string
# "abcd" -> "dcba
# "abcde" -> "edcba"
# O(1) extra allocation
#string type in python are immutable // as in java
def reverseString(astring):
    size = len(astring)
    for i in range(0, size//2):
        temp1 = astring[i]
        temp2 = astring[size-1-i]
        astring[i] = temp2
        astring[size-1-i] = temp1
    return astring

# #ex2
# # Given a binary tree, find its maximum depth.
# #
# # The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# #
# # Note: A leaf is a node with no children.
# #
# # Example:
# #
# # # Given binary tree [3,9,20,null,null,15,7],
# #     3
# #    / \
# #   9  20
# #     /  \
# #    15   7
# # return its depth = 3.

#minimal definition of a BST
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#push a  node in a root
def push(root, aval):
    if root:
        if aval < root.val:
            if root.left:
                push(root.left, aval)
            else:
                root.left = Node(aval)
        elif aval > root.val:
            if root.right:
                push(root.right, aval)
            else:
                root.right = Node(aval)
        else:
            print("node already present in the tree")
            return root
    else:
        print("no root defined")
        return -1

def inordertraversal(root):
    nodes = []
    if root:
        nodes += inordertraversal(root.left)
        nodes += [root.val]
        nodes += inordertraversal(root.right)
    return nodes

# # Example:
# #
# # # Given binary tree [3,9,20,null,null,15,7],
# #     3
# #    / \
# #   9  20
# #     /  \
# #    15   7
# # return its depth = 3.
# return all the possible paths first ?
def maxdepthdeprecated(root):
    # def allpaths(root, path):
    #     #     if not root:
    #     #         return path
    #     #     else:
    #     #         acc = list()
    #     #         acc+=[allpaths(root.right, path + [root.val])]
    #     #         acc+=[allpaths(root.left, path + [root.val])]
    #     #         return acc
    #     # #acc = []
    #     # all = allpaths(root, [])
    #     # return all
    def allpaths(root, path, acc):
        if not root:
            acc.append(path)
        else:
            allpaths(root.right, path + [root.val], acc)
            allpaths(root.left, path + [root.val], acc)
    acc = []
    allpaths(root, [], acc)
    return acc

#max of a tree (or subtree)
def maxdepth(root):
    if not root:
        return -1
    return max(maxdepth(root.left), maxdepth(root.right)) + 1

#additional cracking the code p256: check if all subtrees are balanced
def isbalanced(root):
    if not root:
        return True
    diff = maxdepth(root.left) - maxdepth(root.right)
    if diff is not 0:
        return False
    else:
        return isbalanced(root.left) and isbalanced(root.right)

#additional : cracking the code p 255
#List of Depths: Given a binary tree,
#design an algorithm which creates a linked list of all the nodes at each depth
#to finish : version recursive inordertraversal
def listatdepth(root):
    def reclistatdepth(root, level, lists):
        #base case
        if not root:
            return
        currentlevel = len(lists)
        if level is currentlevel:
            # create a new list because a new level is reached
            currlist = list()
            lists.append(currlist)
        else:
            # get all nodes at this level, the list should be already created
            currlist = lists[level]
        currlist.append(root)
        reclistatdepth(root.left, level+1, lists)
        reclistatdepth(root.right, level+1, lists)

    lists=[] #contains the list of nodes at each depth
    reclistatdepth(root,0,lists)
    return lists


# #ex3
# # Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# #
# # Note:
# #
# # Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# #
# # Example 1:
# #
# # Input: [2,2,1]
# # Output: 1
# # Example 2:
# #
# # Input: [4,1,2,1,2]
# # Output: 4
#thix version requires not additional memory but is in O(2*N*log(N)) ~= O(NlogN)
#a full linear can be implementaed with a map, each time an element is added to the map it is removed from the list
def alltwicebutone(alist):
    alist = sorted(alist)
    idx=0
    while idx < len(alist)-1:
        val1 = alist[idx]
        val2 = alist[idx+1]
        if(val1!=val2):
            return val1
        idx+=2
    return alist[len(alist)-1]

#
#
# #ex4
# # Write a program that outputs the string representation of numbers from 1 to n.
# #
# # But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
# #
# # Example:
# #
# # n = 15,
# #
# # Return:
# # [
# #     "1",
# #     "2",
# #     "Fizz",
# #     "4",
# #     "Buzz",
# #     "Fizz",
# #     "7",
# #     "8",
# #     "Fizz",
# #     "Buzz",
# #     "11",
# #     "Fizz",
# #     "13",
# #     "14",
# #     "FizzBuzz"
# # ]
#
# #ex5
# # Reverse a singly linked list.
# #
# # Example:
# #
# # Input: 1->2->3->4->5->NULL
# # Output: 5->4->3->2->1->NULL
# # Follow up:
# #
# # A linked list can be reversed either iteratively or recursively. Could you implement both?
#
#
# #ex6
# # Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# #
# # Example:
# #
# # Input: [0,1,0,3,12]
# # Output: [1,3,12,0,0]
# # Note:
# #
# # You must do this in-place without making a copy of the array.
# # Minimize the total number of operations.
#
# #ex7
# # Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# #
# # Given linked list -- head = [4,5,1,9], which looks like following:
# #
# # Note:
# #
# # The linked list will have at least two elements.
# # All of the nodes' values will be unique.
# # The given node will not be the tail and it will always be a valid node of the linked list.
# # Do not return anything from your function.
#
#
# #ex8
# # Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# #
# # You may assume that the array is non-empty and the majority element always exist in the array.
#
#
# #ex9
# #Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# # For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, ' \
# #                                                                 'which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# #
# # Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead,
# #     the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies
# #     to the number nine, which is written as IX. There are six instances where subtraction is used:
# #
# # I can be placed before V (5) and X (10) to make 4 and 9.
# # X can be placed before L (50) and C (100) to make 40 and 90.
# # C can be placed before D (500) and M (1000) to make 400 and 900.
# # Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# #ex10
# # Say you have an array for which the ith element is the price of a given stock on day i.
# #
# # Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# #
# # Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# # Example 1:
# #
# # Input: [7,1,5,3,6,4]
# # Output: 7
# # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# #              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# # Example 2:
# #
# # Input: [1,2,3,4,5]
# # Output: 4
# # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# #              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
# #              engaging multiple transactions at the same time. You must sell before buying again.
# # Example 3:
# #
# # Input: [7,6,4,3,1]
# # Output: 0
# # Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# #11
# # Given a 32-bit signed integer, reverse digits of an integer.
# # #
# # # Example 1:
# # #
# # # Input: 123
# # # Output: 321
# # # Example 2:
# # #
# # # Input: -123
# # # Output: -321
# # # Example 3:
# # #
# # # Input: 120
# # # Output: 21
# # # Note:
# # # Assume we are dealing with an environment which could only store integers
# # # ithin the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# #ex12
# # Count the number of prime numbers less than a non-negative number, n.
# #
# # Example:
# #
# # Input: 10
# # Output: 4
# # Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# #13
# # Given an array, rotate the array to the right by k steps, where k is non-negative.
# # #
# # # Example 1:
# # #
# # # Input: [1,2,3,4,5,6,7] and k = 3
# # # Output: [5,6,7,1,2,3,4]
# # # Explanation:
# # # rotate 1 steps to the right: [7,1,2,3,4,5,6]
# # # rotate 2 steps to the right: [6,7,1,2,3,4,5]
# # # rotate 3 steps to the right: [5,6,7,1,2,3,4]
# # # Example 2:
# # #
# # # Input: [-1,-100,3,99] and k = 2
# # # Output: [3,99,-1,-100]
# # # Explanation:
# # # rotate 1 steps to the right: [99,-1,-100,3]
# # # rotate 2 steps to the right: [3,99,-1,-100]
# # # Note:
# # #
# # # Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# # # Could you do it in-place with O(1) extra space?
#
# #14
# # Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# #
# # Note: For the purpose of this problem, we define empty string as valid palindrome.
# #
# # Example 1:
# #
# # Input: "A man, a plan, a canal: Panama"
# # Output: true
# # Example 2:
# #
# # Input: "race a car"
# # Output: false
#
# #15
# # Reverse bits of a given 32 bits unsigned integer.
# # # Example 1:
# # #
# # # Input: 00000010100101000001111010011100
# # # Output: 00111001011110000010100101000000
# # # Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# # # so return 964176192 which its binary representation is 00111001011110000010100101000000.
# # #
# # # Example 2:
# # #
# # # Input: 11111111111111111111111111111101
# # # Output: 10111111111111111111111111111111
# # # Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
# # # so return 3221225471 which its binary representation is 10101111110010110010011101101001.
# # #
# # # Note:
# # #
# # # Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
# # # will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# # # In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the' \
# # #                                                             ' input represents the signed integer -3 and the output represents the signed integer -1073741825.
# # #
# # # Follow up:
# # #
# # # If this function is called many times, how would you optimize it?
#
# #16
# # Implement int sqrt(int x).
# #
# # Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# #
# # Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# #
# # Example 1:
# #
# # Input: 4
# # Output: 2
# # Example 2:
# #
# # Input: 8
# # Output: 2
# # Explanation: The square root of 8 is 2.82842..., and since
# #              the decimal part is truncated, 2 is returned.
#
# #17
# # Implement strStr().
# # # #
# # # # Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# # # #
# # # # Example 1:
# # # #
# # # # Input: haystack = "hello", needle = "ll"
# # # # Output: 2
# # # # Example 2:
# # # #
# # # # Input: haystack = "aaaaa", needle = "bba"
# # # # Output: -1
# # # # Clarification:
# # # #
# # # # What should we return when needle is an empty string? This is a great question to ask during an interview.
# # # #
# # # # For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
# #18
# # Write a function to find the longest common prefix string amongst an array of strings.
# #
# # If there is no common prefix, return an empty string "".
# #
# # Example 1:
# #
# # Input: ["flower","flow","flight"]
# # Output: "fl"
# # Example 2:
# #
# # Input: ["dog","racecar","car"]
# # Output: ""
# # Explanation: There is no common prefix among the input strings.
# # Note:
# #
# # All given inputs are in lowercase letters a-z.
#
# #19
# # Write a program to find the node at which the intersection of two singly linked lists begins.
# #
# # For example, the following two linked lists:
# # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# # Output: Reference of the node with value = 8
# # Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5].' \
# #                                        ' From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There' \
# #                                        ' are 3 nodes before the intersected node in B.
# #
# # Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# # Output: Reference of the node with value = 2
# # Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4].' \
# #                                        ' From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
# #
# # Notes:
# #
# # If the two linked lists have no intersection at all, return null.
# # The linked lists must retain their original structure after the function returns.
# # You may assume there are no cycles anywhere in the entire linked structure.
# # Your code should preferably run in O(n) time and use only O(1) memory.
#
# #20
# # Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# #
# # Note:
# #
# # The number of elements initialized in nums1 and nums2 are m and n respectively.
# # You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# # Example:
# #
# # Input:
# # nums1 = [1,2,3,0,0,0], m = 3
# # nums2 = [2,5,6],       n = 3
# #
# # Output: [1,2,2,3,5,6]
#
# #21
# # Given a singly linked list, determine if it is a palindrome.
# #
# # Example 1:
# #
# # Input: 1->2
# # Output: false
# # Example 2:
# #
# # Input: 1->2->2->1
# # Output: true
# # Follow up:
# # Could you do it in O(n) time and O(1) space?
#
#
# #22
# # Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# #
# # An input string is valid if:
# #
# # Open brackets must be closed by the same type of brackets.
# # Open brackets must be closed in the correct order.
# # Note that an empty string is also considered valid.
#
# #23
# # Given a linked list, determine if it has a cycle in it.
# # #
# # # To represent a cycle in the given linked list, we use an integer pos which represents
# # # the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# # Input: head = [3,2,0,-4], pos = 1
# # Output: true
# # Explanation: There is a cycle in the linked list, where tail connects to the second node.
# #
# # Input: head = [1,2], pos = 0
# # Output: true
# # Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# #24
# # Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# # # #
# # # # push(x) -- Push element x onto stack.
# # # # pop() -- Removes the element on top of the stack.
# # # # top() -- Get the top element.
# # # # getMin() -- Retrieve the minimum element in the stack.
#
# #25
# # Given an integer n, return the number of trailing zeroes in n!.
# # Input: 3
# # Output: 0
# # Explanation: 3! = 6, no trailing zero.
# #
# # Input: 5
# # Output: 1
# # Explanation: 5! = 120, one trailing zero.
# #
# # Note: Your solution should be in logarithmic time complexity.
#
# #26
# # The count-and-say sequence is the sequence of integers with the first five terms as following:
# #
# # 1.     1
# # 2.     11
# # 3.     21
# # 4.     1211
# # 5.     111221
# # 1 is read off as "one 1" or 11.
# # 11 is read off as "two 1s" or 21.
# # 21 is read off as "one 2, then one 1" or 1211.
# #
# # Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
# #
# # Note: Each term of the sequence of integers will be represented as a string.
# # 1 is read off as "one 1" or 11.
# # 11 is read off as "two 1s" or 21.
# # 21 is read off as "one 2, then one 1" or 1211.
# # 1211 is read off as "one 1, one 2, then two 1s" or 111221.
# # 111221 is read off as "three 1s, two 2s, then one 1" or 312211.
#
#
# #27
# # Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# #
# # Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# # Given nums = [1,1,2],
# #
# # Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# #
# # It doesn't matter what you leave beyond the returned length.
#
# #Clarification:
# #
# # Confused why the returned value is an integer but your answer is an array?
# #
# # Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# #
# # Internally you can think of this:
# #
# # // nums is passed in by reference. (i.e., without making a copy)
# # int len = removeDuplicates(nums);
# #
# # // any modification to nums in your function would be known by the caller.
# # // using the length returned by your function, it prints the first len elements.
# # for (int i = 0; i < len; i++) {
# #     print(nums[i]);
# # }
#
# #28
# # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# # the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
# # will automatically contact the police if two adjacent houses were broken into on the same night.
# #
# # Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# # of money you can rob tonight without alerting the police.
# # Input: [1,2,3,1]
# # # Output: 4
# # # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# # #              Total amount you can rob = 1 + 3 = 4.
#
# #29
# # Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# #
# # The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# #
# # You may assume the integer does not contain any leading zero, except the number 0 itself.
# # Input: [1,2,3]
# # Output: [1,2,4]
# # Explanation: The array represents the integer 123.
#
# #30
# # Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# #
# # For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# #
# #    1
# #    / \
# #   2   2
# #  / \ / \
# # 3  4 4  3
# #
# # But the following [1,2,2,null,3,null,3] is not:
# #
# # 1
# # / \
# #     2
# # 2
# # \ \
# #     3
# # 3
# # Note:
# # Bonus points if you could solve it both recursively and iteratively.
#
# #31
# # You are climbing a stair case. It takes n steps to reach to the top.
# #
# # Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# #
# # Note: Given n will be a positive integer.
# # Input: 2
# # Output: 2
# # Explanation: There are two ways to climb to the top.
# # 1. 1 step + 1 step
# # 2. 2 steps
# #
# # Input: 3
# # Output: 3
# # Explanation: There are three ways to climb to the top.
# # 1. 1 step + 1 step + 1 step
# # 2. 1 step + 2 steps
# # 3. 2 steps + 1 step
#
# #32
# # Given two arrays, write a function to compute their intersection.
# # Note:
# #
# # Each element in the result should appear as many times as it shows in both arrays.
# # The result can be in any order.
# # Follow up:
# #
# # What if the given array is already sorted? How would you optimize your algorithm?
# # What if nums1's size is small compared to nums2's size? Which algorithm is better?
# # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#
# #33
# #Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# # Input: [3,0,1]
# # Output: 2
# # Note:
# # Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
# #34
# # Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# #
# # For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# # Given the sorted array: [-10,-3,0,5,9],
# #
# # One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
# #31
# Invert a binary tree.
#
# Example:
#
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
#central, left, right
def preordertraversal(node):
    res = []
    if node:
        res = [node.val]
        res = res + preordertraversal(node.left)
        res = res + preordertraversal(node.right)
    return res

def pushinvert(root, val):
    if root:
        rootval = root.val
        if val < rootval:
            #push on the right side
            if root.right:
                pushinvert(root.right, val)
            else:
                root.right = Node(val)
        elif val > rootval:
            #push on the left side
            if root.left:
                pushinvert(root.left, val)
            else:
                root.left = Node(val)
        else:
            return root #already present in the graph, do nothing
    else:
        return -1

#
# #32
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
# #32
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
#
# #33
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# #34
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
#
#
# #35
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.


if __name__ == "__main__":

    #ex1 reverse a string
    astringex1 = ['a','b','c','d']
    astringex1 = ['a', 'b', 'c', 'd', 'e']
    print(reverseString(astringex1))

    #ex2 max depth in an BST
    root = Node(5)
    push(root, 2)
    push(root, 1)
    push(root, 4)
    push(root, 10)
    push(root, 9)
    push(root, 11)
    push(root, 5)
    print(inordertraversal(root))
    print(maxdepthdeprecated(root))
    print(maxdepth(root))
    print(isbalanced(root))

    #ex2 suite
    res = listatdepth(root)
    print(res)

    #ex3 : alltwicebutone
    alist = [1, 2, 1, 2, 5]
    print(alltwicebutone(alist))

    #invert a binary tree
    preorderlist = preordertraversal(root)
    print(preorderlist)
    rootinvert = Node(5)
    for val in preorderlist:
        pushinvert(rootinvert, val)
    print(preordertraversal(rootinvert))
    toto = 0